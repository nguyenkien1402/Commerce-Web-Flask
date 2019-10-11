
from dataclasses import dataclass

@dataclass
class CartItem:
    """
    Data class for items in cart
    """
    item_id: str
    modify_time: str
    uid: str
    document_id: str = None

    @staticmethod
    def deserialize(document):
        """
        Helper function for parsing a Firestore document to a CartItem object
        :param document: a snapshot of Firebase document
        :return:
            A CartItem object
        """
        data = document.to_dict()
        if data:
            return CartItem(
                document_id=document.id,
                item_id=data.get('item_id'),
                modify_time=data.get('modify_item'),
                uid=data.get('uid')
            )
        return None