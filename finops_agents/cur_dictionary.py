# finops_agents/cur_dictionary.py

CUR_FIELDS = {
    "product_code": "AWS service name (e.g., AmazonEC2)",
    "usage_start_date": "Start of usage period",
    "blended_cost": "Blended cost for the usage",
    "linked_account_id": "Linked AWS account identifier",
    "resource_id": "Unique resource identifier",
    "availability_zone": "The zone in which the resource was used",
    # Add more as needed...
}

def describe_field(field_name: str) -> str:
    """
    Returns a human-readable description of a CUR field.
    """
    return CUR_FIELDS.get(field_name, "Unknown field")

