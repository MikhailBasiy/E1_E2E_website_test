from dataclasses import dataclass


@dataclass
class Item:
    title: str
    href: str
    price: int
    price_discount: int
    color_active: str