from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from db.models import OfferModel


class OfferRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, offer: OfferModel):
        try:
            self.db.add(offer)
            self.db.commit()
            self.db.refresh(offer)
            return offer
        except Exception as e:
            self.db.rollback()
            raise e

    def find_by_id(self, offer_id: str):
        return self.db.query(OfferModel).filter_by(id=offer_id).first()

    def delete(self, offer: OfferModel):
        self.db.delete(offer)
        self.db.commit()
        return offer

    def find_offer_by_product_id(self, product_id: str):
        return self.db.query(OfferModel).filter_by(product_id=product_id).all()
    
    def update_offer(self, newOffer: OfferModel):
        try:
            self.db.add(newOffer)
            self.db.commit()
            self.db.refresh(newOffer)

            return newOffer
        except DatabaseError as e:
            print(e)
            raise (e)
        
    def find_by_product_id(self, product_id: str):
        return self.db.query(OfferModel).filter_by(product_id=product_id).all()