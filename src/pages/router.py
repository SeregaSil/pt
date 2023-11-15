from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from routers import get_all_hosts, scan_host, get_host_info

router = APIRouter(tags=['Pages'], prefix='/pages')

templates = Jinja2Templates(directory='templates')

@router.get('')
def get_scan_page(request: Request, hosts = Depends(get_all_hosts)):
    return templates.TemplateResponse('scan.html', {
        'request': request,
        'title': 'Scan',
        'hosts': hosts
    })


@router.get('/host/{host_id}')
def init_scan_host(request: Request, host_info=Depends(get_host_info)):
    return templates.TemplateResponse('host.html', {
        'request': request,
        'title': 'Host',
        'host': host_info
    })