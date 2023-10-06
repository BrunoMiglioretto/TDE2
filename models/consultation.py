from datetime import datetime

from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Doctor, Patient


class Consultation(Base):
    __tablename__ = "consultation"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    time: Mapped[str] = mapped_column(
        "time", DATETIME, nullable=False, unique=False, default=datetime.now()
    )
    patient: Mapped["Patient"] = relationship(back_populates="consultations")

    def __init__(self, time, patient):
        self.time = time
        self.patient = patient
