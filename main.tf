terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.48"
    }
    opensearch = {
      source  = "opensearch-project/opensearch"
      version = "= 2.2.0"
    }
  }
  required_version = "~> 1.5"
}

provider "aws" {
  region = "us-east-1"
}

provider "opensearch" {
  url         = aws_opensearchserverless_collection.graphgrc_kb.collection_endpoint
  healthcheck = false
}

resource "aws_iam_role" "graphgrc_kb" {
  name = "AmazonBedrockExecutionRoleForKnowledgeBase_graphgrc_kb"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "bedrock.amazonaws.com"
        }
        Condition = {
          StringEquals = {
            "aws:SourceAccount" = "587066264960"
          }
          ArnLike = {
            "aws:SourceArn" = "arn::bedrock:us-east-1:587066264960:knowledge-base/*"
          }
        }
      }
    ]
  })
}

resource "aws_opensearchserverless_access_policy" "graphgrc_kb" {
  name = "graphgrc-kb"
  type = "data"
  policy = jsonencode([
    {
      Rules = [
        {
          ResourceType = "index"
          Resource = [
            "index/graphgrc-kb/*"
          ]
          Permission = [
            "aoss:CreateIndex",
            "aoss:DeleteIndex",
            "aoss:DescribeIndex",
            "aoss:ReadDocument",
            "aoss:UpdateIndex",
            "aoss:WriteDocument"
          ]
        },
        {
          ResourceType = "collection"
          Resource = [
            "collection/graphgrc-kb"
          ]
          Permission = [
            "aoss:CreateCollectionItems",
            "aoss:DescribeCollectionItems",
            "aoss:UpdateCollectionItems"
          ]
        }
      ],
      Principal = [
        aws_iam_role.graphgrc_kb.arn,
        "arn:aws:sts::587066264960:assumed-role/JumpCloud--Main--AdminRole/admin@alexsmolen.com"
      ]
    }
  ])
}

resource "aws_opensearchserverless_security_policy" "graphgrc_kb_encryption" {
  name = "graphgrc-kb"
  type = "encryption"
  policy = jsonencode({
    Rules = [
      {
        Resource = [
          "collection/graphgrc-kb"
        ]
        ResourceType = "collection"
      }
    ],
    AWSOwnedKey = true
  })
}

resource "aws_opensearchserverless_security_policy" "graphgrc_kb_network" {
  name = "graphgrc-kb"
  type = "network"
  policy = jsonencode([
    {
      Rules = [
        {
          ResourceType = "collection"
          Resource = [
            "collection/graphgrc-kb"
          ]
        },
        {
          ResourceType = "dashboard"
          Resource = [
            "collection/graphgrc-kb"
          ]
        }
      ]
      AllowFromPublic = true
    }
  ])
}

resource "aws_opensearchserverless_collection" "graphgrc_kb" {
  name = "graphgrc-kb"
  type = "VECTORSEARCH"
  depends_on = [
    aws_opensearchserverless_access_policy.graphgrc_kb,
    aws_opensearchserverless_security_policy.graphgrc_kb_encryption,
    aws_opensearchserverless_security_policy.graphgrc_kb_network
  ]
}

resource "opensearch_index" "graphgrc_kb" {
  name                           = "bedrock-knowledge-base-default-index"
  number_of_shards               = "2"
  number_of_replicas             = "0"
  index_knn                      = true
  index_knn_algo_param_ef_search = "512"
  mappings                       = <<-EOF
    {
      "properties": {
        "bedrock-knowledge-base-default-vector": {
          "type": "knn_vector",
          "dimension": 1536,
          "method": {
            "name": "hnsw",
            "engine": "faiss",
            "parameters": {
              "m": 16,
              "ef_construction": 512
            },
            "space_type": "l2"
          }
        },
        "AMAZON_BEDROCK_METADATA": {
          "type": "text",
          "index": "false"
        },
        "AMAZON_BEDROCK_TEXT_CHUNK": {
          "type": "text",
          "index": "true"
        }
      }
    }
  EOF
  force_destroy                  = true
  depends_on                     = [aws_opensearchserverless_collection.graphgrc_kb]
}

resource "aws_bedrockagent_knowledge_base" "graphgrc_kb" {
  name     = "graphgrc-kb"
  role_arn = aws_iam_role.graphgrc_kb.arn
  knowledge_base_configuration {
    vector_knowledge_base_configuration {
      embedding_model_arn = data.aws_bedrock_foundation_model.kb.model_arn
    }
    type = "VECTOR"
  }
  storage_configuration {
    type = "OPENSEARCH_SERVERLESS"
    opensearch_serverless_configuration {
      collection_arn    = aws_opensearchserverless_collection.graphgrc_kb.arn
      vector_index_name = "bedrock-knowledge-base-default-index"
      field_mapping {
        vector_field   = "bedrock-knowledge-base-default-vector"
        text_field     = "AMAZON_BEDROCK_TEXT_CHUNK"
        metadata_field = "AMAZON_BEDROCK_METADATA"
      }
    }
  }
  depends_on = [
    aws_iam_role_policy.bedrock_kb,
    aws_iam_role_policy.graphgrc_kb_s3,
    opensearch_index.graphgrc_kb,
    time_sleep.aws_iam_role_policy_graphgrc_kb
  ]
}

resource "time_sleep" "aws_iam_role_policy_graphgrc_kb" {
  create_duration = "20s"
  depends_on      = [aws_iam_role_policy.bedrock_kb]
}

resource "aws_s3_bucket" "graphgrc_kb" {
  bucket        = "graph-grc-kb-dev-dataset"
  force_destroy = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "graphgrc_kb" {
  bucket = aws_s3_bucket.graphgrc_kb.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "graphgrc_kb" {
  bucket = aws_s3_bucket.graphgrc_kb.id
  versioning_configuration {
    status = "Enabled"
  }
  depends_on = [aws_s3_bucket_server_side_encryption_configuration.graphgrc_kb]
}

data "aws_bedrock_foundation_model" "kb" {
  model_id = "amazon.titan-embed-text-v1"
}

resource "aws_iam_role_policy" "bedrock_kb" {
  name = "AmazonBedrockFoundationModelPolicyForKnowledgeBase_graphgrc_kb"
  role = aws_iam_role.graphgrc_kb.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = "bedrock:InvokeModel"
        Effect   = "Allow"
        Resource = data.aws_bedrock_foundation_model.kb.model_arn
      }
    ]
  })
}

resource "aws_iam_role_policy" "graphgrc_kb_s3" {
  name = "AmazonBedrockS3PolicyForKnowledgeBase_graphgrc_kb"
  role = aws_iam_role.graphgrc_kb.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "S3ListBucketStatement"
        Action   = "s3:ListBucket"
        Effect   = "Allow"
        Resource = aws_s3_bucket.graphgrc_kb.arn
        Condition = {
          StringEquals = {
            "aws:PrincipalAccount" = "587066264960"
          }
      } },
      {
        Sid      = "S3GetObjectStatement"
        Action   = "s3:GetObject"
        Effect   = "Allow"
        Resource = "${aws_s3_bucket.graphgrc_kb.arn}/*"
        Condition = {
          StringEquals = {
            "aws:PrincipalAccount" = "587066264960"
          }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "graphgrc_kb_oss" {
  name = "AmazonBedrockOSSPolicyForKnowledgeBase_graphgrc_kb"
  role = aws_iam_role.graphgrc_kb.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = "aoss:APIAccessAll"
        Effect   = "Allow"
        Resource = aws_opensearchserverless_collection.graphgrc_kb.arn
      }
    ]
  })
}

resource "aws_bedrockagent_data_source" "graphgrc_kb" {
  knowledge_base_id = aws_bedrockagent_knowledge_base.graphgrc_kb.id
  name              = "GraphGRCKBDataSource"
  data_source_configuration {
    type = "S3"
    s3_configuration {
      bucket_arn = aws_s3_bucket.graphgrc_kb.arn
    }
  }
}
