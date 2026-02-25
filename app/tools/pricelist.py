from langchain.tools import tool
from app.services.pricelist import PricelistService

service = PricelistService()


from langchain.tools import tool
from app.services.pricelist import PricelistService

service = PricelistService()


@tool
def search_pricelist(query: str) -> str:
    """
    Gunakan tool ini untuk mencari harga produk berdasarkan
    nama produk, kapasitas storage, dan tipe market.
    """

    results = service.search_by_query(query, mode="sell")

    if results == "NEED_STORAGE":
        return (
            "Produk tersebut tersedia dalam pilihan penyimpanan "
            "64GB, 128GB, dan 256GB.\n"
            "Silakan pilih kapasitas yang Anda inginkan."
        )

    if not results:
        return "Produk tidak ditemukan dalam pricelist kami."

    formatted = []
    for item in results:
        formatted.append(
            f"- {item['name']} {item['storage']}GB "
            f"({item['market_type']}) — Rp{item['price']:,}"
        )

    return (
        "Berikut harga yang tersedia:\n\n"
        + "\n".join(formatted)
    )