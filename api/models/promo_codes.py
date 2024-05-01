from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(50), unique=True, nullable=False)
    discount_amount = Column(DECIMAL(10, 2), nullable=False)
    start_date = Column(DATETIME, default=datetime.now, nullable=False)
    end_date = Column(DATETIME, default=datetime.now, nullable=False)
