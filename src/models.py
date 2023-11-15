from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import INET
from database import Base

class LinuxHost(Base):
    __tablename__ = 'linux_host'
    
    id = Column('linux_host_id', Integer, nullable=False, primary_key=True)
    
    login = Column('login', String, nullable=False)
    ip_address = Column('ip_address', INET, nullable=False)
    port = Column('port', Integer, nullable=False)
    
    distributor_id = Column('distributor_id', String, nullable=True)
    description = Column('description', String, nullable=True)
    release = Column('release', String, nullable=True) 
    codename = Column('codename', String, nullable=True)
    kernel_name = Column('kernel_name', String, nullable=True)
    nodename = Column('nodename', String, nullable=True)
    kernel_release = Column('kernel_release', String, nullable=True)
    kernel_version = Column('kernel_version', String, nullable=True)
    architecture = Column('architecture', String, nullable=True)
    