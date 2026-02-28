from langchain.tools import tool
from app.services.pricelist import PricelistService

service = PricelistService()


@tool
def search_pricelist(query: str) -> dict:
    """
    Tool WAJIB untuk semua pertanyaan terkait:
    - ketersediaan
    - stok
    - harga
    - keberadaan produk
    """

    results = service.search_by_query(query, mode="sell")

    if results == "NEED_STORAGE":
        return {
            "message": (
                "Produk tersedia dalam kapasitas 64GB, 128GB, dan 256GB. "
                "Silakan sebutkan kapasitas yang Anda inginkan."
            )
        }

    if not results:
        return {
            "message": "Produk tersebut tidak tersedia di database kami."
        }

    lines = [
        f"- {item['name']} {item['storage']}GB "
        f"({item['market_type']}) — Rp{item['price']:,}"
        for item in results
    ]

    return {
        "message": "Produk tersedia dengan detail berikut:\n" + "\n".join(lines)
    }