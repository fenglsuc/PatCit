npl_citation_schema = {
    "type": "object",
    "properties": {
        "npl_publn_id": {"type": "number"},
        "DOI": {"type": "string"},
        "ISSN": {"type": "string"},
        "ISSNe": {"type": "string"},
        "PMCID": {"type": "string"},
        "PMID": {"type": "string"},
        "authors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "first": {"type": "string"},
                    "middle": {"type": "string"},
                    "surname": {"type": "string"},
                    "genname": {"type": "string"},
                },
            },
        },
        "target": {"type": "string"},
        "title_j": {"type": "string"},
        "title_abbrev_j": {"type": "string"},
        "title_m": {"type": "string"},
        "title_main_m": {"type": "string"},
        "title_main_a": {"type": "string"},
        "year": {"type": "number"},
        "issue": {"type": "number"},
        "volume": {"type": "number"},
        "from": {"type": "number"},
        "to": {"type": "number"},
        "issues": {"type": "array"}
        # 'page': {"type": "string"},
        # 'type': {"type": "string"},
        # 'unit': {"type":},
        # 'when': {"type": "string"}
        # 'idno': {"type":},
    },
    "required": ["npl_publn_id"],
}
