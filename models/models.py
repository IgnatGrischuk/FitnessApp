from sync_db.sync_db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship


class Trainer(Base):
    __tablename__ = 'trainers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    sur_name = Column(String, nullable=False)

    user = relationship("Trainer", back_populates="trainers")


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    sur_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    posts = relationship("Client", back_populates="clients")
