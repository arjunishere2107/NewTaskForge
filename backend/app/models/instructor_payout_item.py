from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base


class InstructorPayoutItem(Base):
    __tablename__ = "instructor_payout_items"

    id = Column(Integer, primary_key=True, index=True)

    payout_id = Column(Integer, ForeignKey("instructor_payouts.id"))

    earning_ledger_id = Column(
        Integer,
        ForeignKey("instructor_earning_ledger.id")
    )

    amount = Column(Float, nullable=False)