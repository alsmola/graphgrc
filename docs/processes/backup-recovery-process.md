---
type: process
title: Backup and Recovery Process
owner: infrastructure-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [infrastructure-team, engineering-team]
---

# Backup and Recovery Process

Process for backing up critical data and systems and testing recovery capabilities.

## Roles and Responsibilities

- **Infrastructure Team:** Configures and monitors backups, performs restores
- **Engineering Team:** Identifies critical data and applications for backup
- **Security Team:** Ensures backups are secure (encrypted, access-controlled)

## Prerequisites

- Backup solution configured (AWS Backup, RDS automated backups, etc.)
- Critical data and systems identified
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) defined

## Process Steps

### Step 1: Backup Scope Definition

Identify all critical data and systems requiring backup.

**Critical systems:**
- Production databases (RDS, DynamoDB)
- Object storage (S3 buckets with customer data)
- Configuration and infrastructure code (Git repositories)
- Logs and audit trails
- Encryption keys (AWS KMS, Secrets Manager)
- Documentation and runbooks

**Backup requirements per system:**
- RPO (maximum acceptable data loss): 24 hours for databases, 1 hour for critical transaction data
- RTO (maximum acceptable downtime): 4 hours
- Retention period: 30 days (see data-retention-standard.md for details)

**Owner:** Infrastructure Team, Engineering Team
**Duration:** Initial setup, reviewed annually

### Step 2: Automated Backup Configuration

Configure automated backups for all critical systems.

**Database backups (RDS):**
- Automated daily snapshots, retained for 30 days
- Transaction logs retained for point-in-time recovery (PITR)
- Snapshots copied to secondary region (disaster recovery)

**Object storage (S3):**
- Versioning enabled on all buckets with critical data
- Lifecycle policy to retain deleted objects for 30 days
- Cross-region replication for disaster recovery

**Infrastructure as Code:**
- Git repositories automatically backed up (GitHub, GitLab)
- Configuration management code versioned

**Secrets and keys:**
- AWS Secrets Manager and KMS key backups (automatic AWS service)

**Owner:** Infrastructure Team
**Duration:** Initial configuration, ongoing monitoring

### Step 3: Backup Monitoring

Monitor backup jobs for success and alert on failures.

**Monitoring:**
- AWS Backup dashboard reviewed daily
- Automated alerts for failed backups (Slack, PagerDuty)
- Weekly backup compliance report (all systems backed up successfully)

**Alert response:**
- Investigate failed backups within 2 hours
- Retry backup job
- Escalate if persistent failures

**Owner:** Infrastructure Team
**Duration:** Ongoing, daily monitoring

### Step 4: Backup Security

Ensure backups are encrypted and access-controlled.

**Security requirements:**
- All backups encrypted at rest (AWS KMS)
- Backup access restricted to infrastructure team (IAM policies)
- Separate AWS account for backup storage (security isolation)
- Backup deletion requires MFA (prevent accidental or malicious deletion)
- Immutable backups where possible (vault lock)

**Owner:** Infrastructure Team, Security Team
**Duration:** Initial configuration, quarterly audits

### Step 5: Recovery Testing

Test backup restoration regularly to verify recovery capabilities.

**Testing frequency:**
- Database restore: Quarterly
- Full disaster recovery drill: Annually
- Application recovery: Annually

**Test process:**
1. Select recent backup snapshot
2. Restore to isolated test environment (not production)
3. Verify data integrity (checksums, row counts, sample queries)
4. Test application functionality against restored data
5. Measure time to restore (validate RTO)
6. Document results and any issues

**Success criteria:**
- Data restored successfully
- No data corruption
- RTO met (restore within 4 hours)
- Application functional with restored data

**Owner:** Infrastructure Team
**Duration:** Quarterly tests (2-3 hours per test)

### Step 6: Disaster Recovery Drill

Conduct annual full disaster recovery drill simulating complete production failure.

**Scenario:** Primary AWS region is unavailable, must restore from backups in secondary region.

**Drill steps:**
1. Declare disaster recovery scenario
2. Restore latest backups to DR region
3. Reconfigure DNS/load balancers to point to DR environment
4. Verify application availability and data integrity
5. Measure time to full recovery
6. Document lessons learned

**Owner:** Infrastructure Team, Engineering Team
**Duration:** 4-8 hours (annual drill)

### Step 7: Backup Documentation

Maintain up-to-date recovery runbooks.

**Documentation includes:**
- List of all backed-up systems
- Backup schedules and retention policies
- Step-by-step restore procedures for each system
- Emergency contacts
- RTO/RPO for each system
- Known issues and workarounds

**Owner:** Infrastructure Team
**Duration:** Updated quarterly or after any infrastructure changes

## Backup Retention

**Production data:**
- Daily backups retained for 30 days
- Weekly backups retained for 3 months
- Monthly backups retained for 1 year (optional, for audit/compliance)

**Infrastructure snapshots:**
- 30 days for most systems
- Configuration code retained indefinitely (Git)

## Restore Request Process

**Non-emergency restore (e.g., accidental deletion):**
1. Engineer submits restore request ticket
2. Infrastructure team reviews request and approves
3. Restore performed to isolated environment or specific timeframe
4. Data verified and handed off to requester
5. Restore documented in ticket

**Emergency restore (production incident):**
1. Incident commander authorizes restore
2. Infrastructure team restores immediately
3. Document restore in incident ticket

## Validation and Evidence

- Backup compliance reports (weekly, monthly)
- Restore test results (quarterly, annual DR drill)
- Recovery runbook documentation
- Backup monitoring dashboards and alerts
- Incident reports for any restore operations

## References

- Related controls: INF-04, OPS-04
- Related standards: data-retention-standard.md
- AWS Backup Best Practices: https://docs.aws.amazon.com/aws-backup/latest/devguide/best-practices.html

---

<!-- Backlinks auto-generated below -->
