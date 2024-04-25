from sqlalchemy import create_engine
from sqlalchemy import String, Column, BigInteger, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///wallet_service_db')

Base = declarative_base()


class Transactions(Base):
  __tablename__ = 'transactions'
  sr_id = Column(String(250), primary_key=True)
  txid = Column(String(250))
  address = Column(String(250), primary_key=True)
  amount = Column(Integer)
  wallet_id = Column(Integer)
  fee = Column(Integer)
  sr_timestamp = Column(BigInteger)
  tx_timestamp = Column(BigInteger)
  wallet_password = Column(String(2000))


Base.metadata.create_all(engine)
