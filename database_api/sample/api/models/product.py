
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from database_api.sample.api.models.category import Category


@dataclass
class Product:
    id: int | None
    name: str
    price: Decimal
    created_at: datetime
    category: Category
