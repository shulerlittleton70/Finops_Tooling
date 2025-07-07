# 🛠️ AWS Setup Guide for FinOps Agents (Athena + CUR + LLM)

This guide walks through the required AWS configuration to enable your `finops_agents` assistant to query AWS Cost and Usage Reports (CUR) using Athena and securely provide credentials via `.env`.

---

## 🔧 Part 1: Enable and Configure AWS Cost and Usage Report (CUR)

Follow this excellent guide:  
🔗 [CloudForecast: AWS Athena + CUR Integration](https://www.cloudforecast.io/blog/aws-athena-cur-integration/)

### Summary of Steps:

1. **Create an S3 Bucket**
   - Example: `my-cur-bucket`

2. **Enable CUR in AWS Console**
   - Navigate to: *Billing > Cost and Usage Reports*
   - Create a new report:
     - ✅ Enable Athena integration
     - ✅ Include resource IDs
     - ✅ Use GZIP compression
     - ✅ Set delivery options to Daily or Hourly
     - Deliver to `s3://my-cur-bucket/cur/`

3. **Wait for CUR to Generate**
   - May take up to 24 hours for the first report to appear

---

## 📈 Part 2: Set Up Athena + Glue Table

After CUR files start appearing in your S3 bucket:

### A. Create a Table in Athena via Glue

1. Go to **Athena > Data Sources > AWS Glue**
2. Select **Add Table > From S3**
3. Provide the path: `s3://my-cur-bucket/cur/`
4. Format:
   - Delimiter: `,`
   - Compression: `GZIP`
5. Set a table name (e.g., `aws_cur_table`) and database (e.g., `cur_db`)

> ⚠️ Make note of your `database name`, `table name`, and Athena result bucket

---

## 🔐 Part 3: IAM Setup for LLM Agent Access

Create a dedicated IAM user for your LLM agent (used via `.env` file).

### A. Create IAM User

1. Go to **IAM > Users > Add User**
2. Name the user: `finops-agent`
3. Select: ✅ *Programmatic access*

### B. Attach IAM Policy

Attach a custom policy with permission to Athena, Glue, and CUR S3 bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AthenaAccess",
      "Effect": "Allow",
      "Action": [
        "athena:StartQueryExecution",
        "athena:GetQueryExecution",
        "athena:GetQueryResults",
        "athena:ListQueryExecutions",
        "athena:GetWorkGroup"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3Access",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::my-cur-bucket",
        "arn:aws:s3:::my-cur-bucket/*"
      ]
    },
    {
      "Sid": "GlueAccess",
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetDatabases",
        "glue:GetTable",
        "glue:GetTables"
      ],
      "Resource": "*"
    }
  ]
}
