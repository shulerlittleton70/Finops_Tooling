# finops_agents/cur_dictionary.py

CUR_FIELDS = {
    "product_code": "The AWS service generating the cost (e.g., AmazonEC2)",
    "usage_type": "The type of usage (e.g., BoxUsage, DataTransfer)",
    "blended_cost": "The effective cost after blended rates or reserved instance pricing",
    "unblended_cost": "The unmodified, per-account raw rate of spend",
    "resource_id": "The unique identifier of the resource (EC2 instance ID, etc.)",
    "availability_zone": "The AZ where the service was used",
    "linked_account_id": "The AWS account that incurred the cost",
    "usage_start_date": "Start timestamp of the usage period",
    "usage_end_date": "End timestamp of the usage period",
    "cost_category": "Mapped cost category based on business rules",
    # Add more definitions as needed
}

def describe_field(field_name: str) -> str:
    return CUR_FIELDS.get(field_name, "Unknown field")

def get_field_dictionary_text() -> str:
    return "\n".join(f"- `{k}`: {v}" for k, v in CUR_FIELDS.items())
