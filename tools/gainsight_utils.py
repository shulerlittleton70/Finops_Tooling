import requests

class GainsightClient:
    def __init__(self, base_url: str, access_key: str):
        """
        Initialize the Gainsight API client.
        """
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Accesskey': access_key,
            'Content-Type': 'application/json'
        }

    def _post(self, endpoint: str, data=None):
        """
        Internal POST wrapper.
        """
        url = f"{self.base_url}{endpoint}"
        resp = requests.post(url, headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()

    def query_companies(self, select: list, where: dict = None, limit: int = 100, offset: int = 0):
        """
        General-purpose query to the Company object.
        """
        body = {'select': select, 'limit': limit, 'offset': offset}
        if where:
            body['where'] = where
        return self._post("/v1/data/objects/query/Company", data=body)

    def upsert_companies(self, records: list):
        """
        Insert or update records into the Company object.
        """
        return self._post("/v1/data/objects/Company", data={'records': records})

    # ----------------------------
    # COMMON COMPANY QUERIES
    # ----------------------------

    def get_active_companies(self, limit=100):
        return self.query_companies(
            select=["Name", "ARR", "Stage", "RenewalDate", "HealthScore"],
            where={
                "conditions": [
                    {"name": "Status", "operator": "EQUALS", "value": "Active"}
                ],
                "expression": "A"
            },
            limit=limit
        )

    def get_churned_companies(self, limit=100):
        return self.query_companies(
            select=["Name", "ARR", "Stage", "RenewalDate"],
            where={
                "conditions": [
                    {"name": "Status", "operator": "EQUALS", "value": "Churned"}
                ],
                "expression": "A"
            },
            limit=limit
        )

    def get_companies_with_low_health(self, threshold=50, limit=100):
        return self.query_companies(
            select=["Name", "ARR", "CSM", "HealthScore"],
            where={
                "conditions": [
                    {"name": "HealthScore", "operator": "LESSTHAN", "value": threshold}
                ],
                "expression": "A"
            },
            limit=limit
        )

    def find_companies_by_csm(self, csm_name, limit=100):
        return self.query_companies(
            select=["Name", "ARR", "Stage", "HealthScore"],
            where={
                "conditions": [
                    {"name": "CSM", "operator": "EQUALS", "value": csm_name}
                ],
                "expression": "A"
            },
            limit=limit
        )

    def get_companies_due_for_renewal(self, before_date, limit=100):
        """
        Returns companies with upcoming renewals before a given ISO date (YYYY-MM-DD).
        """
        return self.query_companies(
            select=["Name", "ARR", "RenewalDate", "Stage"],
            where={
                "conditions": [
                    {"name": "RenewalDate", "operator": "LESSTHAN", "value": before_date}
                ],
                "expression": "A"
            },
            limit=limit
        )

    def get_recently_created_companies(self, after_date, limit=100):
        """
        Returns companies created after a given ISO date (YYYY-MM-DD).
        """
        return self.query_companies(
            select=["Name", "ARR", "CreatedDate"],
            where={
                "conditions": [
                    {"name": "CreatedDate", "operator": "GREATERTHAN", "value": after_date}
                ],
                "expression": "A"
            },
            limit=limit
        )

    def get_companies_by_industry(self, industry, limit=100):
        return self.query_companies(
            select=["Name", "ARR", "Industry", "HealthScore"],
            where={
                "conditions": [
                    {"name": "Industry", "operator": "EQUALS", "value": industry}
                ],
                "expression": "A"
            },
            limit=limit
        )
