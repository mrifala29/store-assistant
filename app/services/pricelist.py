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

    def search_by_name(self, name: str, mode: str = "sell") -> List[Dict]:
        items = self.get_all(mode)
        return [
            item for item in items
            if name.lower() in item["name"].lower()
        ]

    def search_by_budget(self, min_price: int, max_price: int, mode: str = "sell") -> List[Dict]:
        items = self.get_all(mode)
        return [
            item for item in items
            if min_price <= item["price"] <= max_price
        ]