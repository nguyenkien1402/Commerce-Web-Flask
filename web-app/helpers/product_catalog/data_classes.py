from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    """
    Data class for products.
    """
    name: str
    description: str
    image: str
    labels: List[str]
    price: float
    created_at: int
    id: str = None

    @staticmethod
    def deserialize(document):
        """
        Helper function for parsing a Firebase document to product object
        :param
            document: A snapshot of firebase document
        :return:
            A product object
        """
        data = document.to_dict()
        if data:
            return Product(
                id=document.id,
                name=data.get('name'),
                description=data.get('description'),
                image=data.get('image'),
                labels=data.get('labels'),
                price=data.get('price'),
                created_at=data.get('created_at')
            )
        return None


@dataclass
class PromoEntry:
    """
    Data class for promotions.
    :return:
    """
    label: str
    score: float
    id: str = None

    @staticmethod
    def deserialize(document):
        """
        Helper function to parse a firebase document to PromoEntry object.
        :param
            document: a snapshot of firebase document
        :return:
            A PromoEntry object
        """
        data = document.to_dict()
        if data:
            return PromoEntry(
                id=document.id,
                label=data.get('label'),
                score=data.get('score')
            )
        return None