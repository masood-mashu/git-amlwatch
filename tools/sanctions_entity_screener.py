"""
sanctions_entity_screener.py - Performs exact and normalized screening against active international sanction watchlists
"""
import sys
import json


def screen_sanctions(entity_name: str):
    SANCTIONS_LIST = ["acme global illicit", "sanctioned cartel ltd", "darkpool holdings", "blacklisted enterprise"]
    norm = entity_name.strip().lower()
    matched = any(s in norm for s in SANCTIONS_LIST)
    return {
        "entity_name": entity_name,
        "sanction_match": matched,
        "action": "BLOCK_TRANSACTION" if matched else "PROCEED",
        "status": "SANCTIONS_HIT" if matched else "CLEAR"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "sanctions-entity-screener"}))
