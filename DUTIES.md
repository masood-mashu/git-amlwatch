# Segregation of Duties (SOD) Policy: GitAMLWatch

This document establishes the role boundaries and segregation of duties for the GitAMLWatch agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring transaction monitoring rules, preparing customer risk tiering manifests, and generating automated AML compliance diffs.
This role cannot approve or merge its own changes into protected financial branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming wire batches, structuring flags, and sanctions screening matches.
This role operates as an impartial auditor to verify compliance with Bank Secrecy Act and FinCEN regulatory benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Chief Compliance Officers and BSA officers.
Human approval is required for all production AML deployments, SAR filings, and transaction blocking overrides.
