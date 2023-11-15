from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import LinuxHostInfo
from models import LinuxHost

async def create_scan_linux_host_info(scan_info: LinuxHostInfo, db: AsyncSession):
    host = LinuxHost(**scan_info.model_dump())
    db.add(host)
    await db.commit()
    
async def get_all_scan_hosts(db: AsyncSession):
    query = (select(LinuxHost))
    return (await db.scalars(query)).all()


async def get_host_by_id(host_id: int, db: AsyncSession):
    return await db.get(entity=LinuxHost, ident=host_id)