from sqlalchemy import (
    Column,
    String,
    Text,
    BigInteger,
    Date,
    Enum,
    TIMESTAMP,
    text
)
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AIModel(Base):
    __tablename__ = 'models'

    id = Column(CHAR(36), primary_key=True, nullable=False)
    name = Column(String(255), unique=True, nullable=True)
    description = Column(Text, nullable=True)
    num_parameters = Column(BigInteger, nullable=True)
    release_date = Column(Date, nullable=True)
    architecture = Column(String(255), nullable=True)
    license = Column(String(255), nullable=True)
    developed_by = Column(String(255), nullable=True)
    status = Column(
        Enum('ACTIVE', 'DEPRECATED', 'IN_DEVELOPMENT', 'RUMORED'),
        nullable=True
    )
    created_at = Column(
        TIMESTAMP,
        nullable=True,
        server_default=text('CURRENT_TIMESTAMP')
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=True,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )

