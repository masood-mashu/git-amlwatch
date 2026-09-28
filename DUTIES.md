# Separation of Duties for GitAMLWatch

## Maker Role: TransactionAnalyst
TransactionAnalyst who processes banking ledgers, wire instructions, and counterparty filings.

## Checker Role: BSAComplianceOfficer
BSAComplianceOfficer who verifies AML risk scoring, sanctions checks, and SAR recommendations.

## Dual-Control Verification Pipeline
1. Ingest core banking transactional telemetry and counterparty payment metadata.
2. Calculate rolling transaction velocity and variance against historical customer baselines.
3. Screen sender and beneficiary identifiers against global sanction lists.
4. Issue SAR filings and regulatory audit packages with deterministic evidence logs.
