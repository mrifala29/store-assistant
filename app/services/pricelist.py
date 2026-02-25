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

        product_names = self.get_unique_product_names(mode)

        detected_product = None
        for name in product_names:
            if name.lower() in query_lower:
                detected_product = name
                break

        if not detected_product:
            return []

        # deteksi storage
        requested_storage = None
        for s in [64, 128, 256]:
            if str(s) in query_lower:
                requested_storage = s
                break

        # deteksi market
        requested_market = None
        if any(word in query_lower for word in ["ibox", "digimap", "blibli", "resmi"]):
            requested_market = "Resmi Indonesia"
        elif "beacukai" in query_lower:
            requested_market = "Terdaftar Beacukai"

        results = []

        for item in items:
            if item["name"] != detected_product:
                continue

            if requested_market and item["market_type"] != requested_market:
                continue

            if requested_storage:
                if item["storage"] == requested_storage:
                    results.append(item)
            else:
                return "NEED_STORAGE"

        return results
    
    def get_unique_product_names(self, mode: str = "sell"):
        items = self.get_all(mode)
        
        return list(set(item["name"] for item in items))

    def search_by_budget(self, min_price: int, max_price: int, mode: str = "sell") -> List[Dict]:
        items = self.get_all(mode)
        return [
            item for item in items
            if min_price <= item["price"] <= max_price
        ]