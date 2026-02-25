import json
from pathlib import Path
from typing import List, Dict

DATA_PATH = Path("app/database/pricelist_dummy.json")


class PricelistService:

    def __init__(self):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_all(self, mode: str = "sell") -> List[Dict]:
        key = "sell_price" if mode == "sell" else "buy_price"
        return self.data.get(key, [])

    def search_by_query(self, query: str, mode: str = "sell"):
        items = self.get_all(mode)
        query_lower = query.lower()

        results = []

        for item in items:
            name_match = item["name"].lower() in query_lower
            storage_match = str(item["storage"]) in query_lower

            if name_match and storage_match:
                results.append(item)

        return results

    def search_by_budget(self, min_price: int, max_price: int, mode: str = "sell") -> List[Dict]:
        items = self.get_all(mode)
        return [
            item for item in items
            if min_price <= item["price"] <= max_price
        ]