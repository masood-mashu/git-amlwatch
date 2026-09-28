# Explainability & Governance Statement

## Decision Architecture
GitAMLWatch flags suspicious financial activities by combining threshold compliance checks, velocity time-series math, and fuzzy entity watchlist matching. If three deposits of $9,800 occur across 48 hours, the structuring detection rule triggers an automatic flag with transaction hashes and temporal deltas.

## Input Data Provenance
Inputs include ISO 20022 payment messages, banking transaction ledgers, customer risk tiers, and OFAC/UN sanction list manifests.

## Operational Limits & Non-Goals
GitAMLWatch analyzes digital and wire transactions; it cannot monitor offline cash handoffs without banking ledger entry. False positive screening thresholds must be calibrated per financial institution risk appetite.
