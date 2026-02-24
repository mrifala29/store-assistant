from langchain.tools import tool
from app.services.pricelist import PricelistService

service = PricelistService()


@tool
def search_pricelist(query: str) -> str:
    """
    Gunakan tool ini jika user bertanya tentang harga iPhone
    atau rekomendasi berdasarkan budget.
    """

    results = service.search_by_name(query, mode="sell")

    if not results:
        return "Produk tidak ditemukan."

    formatted = []
    for item in results:
        formatted.append(
            f"{item['name']} {item['storage']}GB "
            f"({item['market_type']}) - Rp{item['price']:,}"
        )

    return "\n".join(formatted)