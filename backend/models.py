from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Product(BaseModel):
    name: str
    quantity: Optional[float] = None
    checked: Optional[bool] = False


