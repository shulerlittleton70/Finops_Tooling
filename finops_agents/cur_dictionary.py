# finops_agents/cur_dictionary.py

CUR_FIELDS = {
    # Identity
    "identity/LineItemId": "A unique identifier for the line item record.",
    "identity/TimeInterval": "The start and end of the usage interval in ISO8601 format.",

    # Bill
    "bill/BillType": "Type of bill (Anniversary, Refund, etc.).",
    "bill/BillingEntity": "The AWS entity issuing the bill.",
    "bill/BillID": "The unique identifier for the bill.",
    "bill/BillingPeriodStartDate": "Start date of the billing period.",
    "bill/BillingPeriodEndDate": "End date of the billing period.",
    "bill/InvoiceId": "The ID of the invoice containing the charges.",
    "bill/PayerAccountId": "The account that is paying the bill.",
    "bill/BillName": "The name of the bill as defined by the user.",

    # Line Item
    "lineItem/UsageAccountId": "The AWS account that used the resource.",
    "lineItem/LineItemType": "The type of line item (Usage, DiscountedUsage, RIFee, etc.).",
    "lineItem/UsageType": "The usage category (e.g., BoxUsage:t2.micro).",
    "lineItem/Operation": "The operation performed (e.g., RunInstances).",
    "lineItem/AvailabilityZone": "AWS Availability Zone where the usage occurred.",
    "lineItem/ResourceId": "The unique resource identifier (e.g., EC2 instance ID).",
    "lineItem/UsageStartDate": "Start time for the usage interval.",
    "lineItem/UsageEndDate": "End time for the usage interval.",
    "lineItem/UsageAmount": "The amount of usage (e.g., hours, GB).",
    "lineItem/NormalizationFactor": "Factor used to normalize usage across instance types.",
    "lineItem/NormalizedUsageAmount": "Normalized usage amount for RI/SP eligibility.",
    "lineItem/CurrencyCode": "The currency used for the charge.",
    "lineItem/UnblendedRate": "Cost per unit of usage without discounts.",
    "lineItem/UnblendedCost": "Total cost before applying blended rates.",
    "lineItem/BlendedRate": "Rate after blending costs across linked accounts.",
    "lineItem/BlendedCost": "Total cost after applying blended rates.",
    "lineItem/LineItemDescription": "A human-readable description of the line item.",
    "lineItem/TaxType": "Type of tax (if applicable).",

    # Pricing
    "pricing/PublicOnDemandCost": "The public on-demand cost for this usage.",
    "pricing/PublicOnDemandRate": "The public on-demand rate per unit.",
    "pricing/Unit": "The unit of measure for usage (e.g., Hours, GB).",

    # Product
    "product/ProductName": "Name of the AWS product or service.",
    "product/region": "The AWS region for the usage.",
    "product/instanceType": "The EC2 instance type (e.g., t3.medium).",
    "product/operatingSystem": "Operating system (e.g., Linux).",
    "product/tenancy": "Tenancy (e.g., Shared, Dedicated).",
    "product/sku": "Stock Keeping Unit - unique AWS product code.",
    "product/usageFamily": "Group of similar usage types.",
    "product/databaseEngine": "RDS database engine (if applicable).",

    # Reservation
    "reservation/ReservationARN": "The Amazon Resource Name of the reservation.",
    "reservation/NumberOfReservations": "The number of reservations applied.",
    "reservation/EffectiveCost": "The amortized cost of the reservation.",
    "reservation/UnusedHours": "Number of unused reserved hours.",
    "reservation/UnusedQuantity": "Amount of reserved usage that went unused.",
    "reservation/UtilizationPercentage": "How much of the reservation was used.",

    # Savings Plan
    "savingsPlan/SavingsPlanArn": "The ARN of the savings plan.",
    "savingsPlan/SavingsPlanRate": "Rate for the savings plan.",
    "savingsPlan/UsedCommitment": "Amount of commitment used.",
    "savingsPlan/AmortizedRecurringCommitment": "Recurring cost split over time.",
    "savingsPlan/SavingsPlanEffectiveCost": "Cost after applying the savings plan.",

    # Discount
    "discount/TotalDiscount": "Sum of all discounts (RIFee, credits, SP).",
    "discount/DiscountAmount": "The amount of discount applied to this line item.",
    "discount/DiscountRate": "Percentage of discount applied.",

    # Cost Category
    "costCategory/Name": "Name of the Cost Category rule that applied.",
    "costCategory/Value": "The value of the cost category assigned.",

    # Tags (dynamic and optional)
    "resourceTags/user:Environment": "Custom tag identifying environment (e.g., Prod, Dev).",
    "resourceTags/user:Owner": "Custom tag for resource ownership.",
    "resourceTags/user:Application": "Custom tag for application identification.",
    "resourceTags/user:Team": "Custom tag for team ownership.",
}

def describe_field(field_name: str) -> str:
    return CUR_FIELDS.get(field_name, "Unknown field")

def get_field_dictionary_text() -> str:
    return "\n".join(f"- `{k}`: {v}" for k, v in CUR_FIELDS.items())
