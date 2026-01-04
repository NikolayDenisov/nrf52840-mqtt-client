from sqlalchemy import String, Float, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class SensorData(Base):
    __tablename__ = "sensor_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[str] = mapped_column(String(64), index=True)
    sensor: Mapped[str] = mapped_column(String(32))
    temperature_c: Mapped[float] = mapped_column(Float)
    humidity_rh: Mapped[float] = mapped_column(Float)
    ts: Mapped[int] = mapped_column(BigInteger, index=True)
