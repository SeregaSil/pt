from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse, PlainTextResponse
from sqlalchemy.ext.asyncio import AsyncSession
from paramiko import SSHClient, AutoAddPolicy
from pydantic.networks import IPvAnyAddress

from database import get_async_session
from schemas import LinuxHostInfo
from scan import lsb_release, uname, arch
from service import create_scan_linux_host_info, get_all_scan_hosts, get_host_by_id

import logging

router = APIRouter(tags=['Scan'], prefix='/scan')

@router.post('')
async def scan_host(ip_address: IPvAnyAddress = Form(), port: int = Form(),
                    login: str = Form(), password: str = Form(),
                    db: AsyncSession = Depends(get_async_session)):
    try:
        logging.info(f'Attempt to connect to {login}@{ip_address}:{port}')
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname=str(ip_address), username=login, password=password, port=port, timeout=5.0)
    except Exception as ex:
        logging.exception(f'Error connection to host {login}@{ip_address}:{port}')
        return PlainTextResponse(status_code=400, content='Ошибка подлючения к хосту')
    
    logging.info(f'Successful connection to host {login}@{ip_address}:{port}')
    scan_info = LinuxHostInfo(login=login, ip_address=str(ip_address), port=port)
    lsb_release(client, scan_info)
    uname(client, scan_info)
    arch(client, scan_info)
    
    client.close()
    
    await create_scan_linux_host_info(scan_info, db)
    
    return RedirectResponse('/pages', status_code=301)

@router.get('/hosts')
async def get_all_hosts(db: AsyncSession = Depends(get_async_session)):
    return await get_all_scan_hosts(db)

@router.get('/host/{host_id}')
async def get_host_info(host_id: int, db: AsyncSession = Depends(get_async_session)):
    return await get_host_by_id(host_id, db)