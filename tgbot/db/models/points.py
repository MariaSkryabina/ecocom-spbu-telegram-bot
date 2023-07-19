from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID, TEXT, BOOLEAN, DOUBLE_PRECISION
from sqlalchemy.orm import mapped_column, Mapped
from tgbot.db.models.base import Base


class Points(Base):
    __tablename__ = "rso_points"

    photo_id: Mapped[str] = mapped_column(TEXT, primary_key=True, nullable=False)
    address: Mapped[str] = mapped_column(TEXT, nullable=False)
    route: Mapped[str] = mapped_column(TEXT, primary_key=True, nullable=False)
    latitude: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False)
    longitude: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False)
    paper: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    pat: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    glass: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    alum: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    pp_h: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    pp_s: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    batteries: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    cups: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    bulbs: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    notes: Mapped[str] = mapped_column(TEXT, nullable=False)

    def dict(self):
        return {
            "photo_id": self.photo_id,
            "address": self.address,
            "route": self.route,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "paper": self.paper,
            "pat": self.pat,
            "glass": self.glass,
            "alum": self.alum,
            "pp_h": self.pp_h,
            "pp_s": self.pp_s,
            "batteries": self.batteries,
            "cups": self.cups,
            "bulbs": self.bulbs,
            "notes": self.notes
        }
