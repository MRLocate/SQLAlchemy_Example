from sqlalchemy import Boolean, Column, String, Date, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# What should our data types be and what length should we use for strings?
# https://www.includehelp.com/python/find-length-of-longest-string-in-pandas-dataframe-column.aspx
# Don't worry about indexes, keys, etc..
class Crime(Base):
    __tablename__ = 'crimes'

    id = Column(Integer, primary_key=True)
    lsoa_code = Column(String(10), nullable=False)
    borough = Column(String(50), nullable=False)
    major_category = Column(String(50), nullable=False)
    minor_category = Column(String(50), nullable=False)
    value = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
