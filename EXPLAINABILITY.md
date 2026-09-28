# GitAMLWatch Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitAMLWatch** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitAMLWatch consumes core banking transaction ledgers, wire transfer instructions, customer profile records, and international sanction watchlists. These data sources include transaction amounts, counterparty identifiers, ISO currency codes, timestamp logs, and account risk classifications. The agent ingests these inputs in raw JSON, CSV, and payment messaging formats and parses them into standardized financial transaction objects for downstream verification. Bank secrecy logs and external regulatory watchlists such as OFAC and PEP databases are also monitored as sensitive data sources to ensure compliance mandates are strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When a transaction batch is received, the agent first evaluates structuring and smurfing patterns using the structuring-smurfing-detector tool to identify deposits designed to evade the $10,000 reporting threshold. Next, the reasoning engine invokes the transaction-velocity-monitor tool to compute rolling 90-day volume variances and detect anomalous transaction spikes. Furthermore, counterparty legal names are screened using the sanctions-entity-screener tool against international sanction databases. Finally, the agent correlates all financial findings against predefined AML policies to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated suspicious activity report.

---

## 3. Constraints, Limitations, and Known Issues

GitAMLWatch operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitAMLWatch operates under strict operational constraints to prevent financial miscalculations and regulatory non-compliance across execution frameworks. The agent is deliberately limited to ledger verification and statutory rule checking and cannot execute autonomous fund transfers or real-money banking disbursements. Another known issue and limitation is that cross-border currency conversions with volatile exchange rates may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
