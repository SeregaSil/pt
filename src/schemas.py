from pydantic import BaseModel, Field
from pydantic.networks import IPvAnyAddress


class BaseHost(BaseModel):
    login: str = Field(..., examples=['kali'])
    ip_address: IPvAnyAddress = Field(..., examples=['192.168.13.129'])
    port: int = Field(..., examples=['22'])

class ScanHost(BaseHost):
    password: str = Field(..., examples=['kali'])
    
class LinuxHostInfo(BaseHost):    
    distributor_id: str | None = None
    description: str | None = None
    release: str | None = None
    codename: str | None = None
    kernel_name: str | None = None
    nodename: str | None = None
    kernel_release: str | None = None
    kernel_version: str | None = None
    architecture: str | None = None

class LinuxHostView(LinuxHostInfo):
    id: int