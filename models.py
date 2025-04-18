from dataclasses import dataclass


@dataclass
class CatalogItem:
    title: str
    href: str
    price: str
    price_discount: str
    color_active: str


@dataclass
class ProductPageItem:
    title: str
    price: str
    price_discount: str
    color_active: str
    profile_color: str
    layout: str
