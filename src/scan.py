from paramiko import SSHClient
from schemas import LinuxHostInfo

import logging

def lsb_release(client: SSHClient, scan_info: LinuxHostInfo):
    try:
        logging.info('Start command: lsb_release -as')
        _, stdout, _ = client.exec_command('lsb_release -as')
        data = stdout.read().decode()[:-1].split('\n')
        scan_info.distributor_id = data[0]
        scan_info.description = data[1]
        scan_info.release = data[2]
        scan_info.codename = data[3]
        logging.info('Success command: lsb_release -as')
    except Exception:
        logging.exception('Fail command: lsb_release -as')
    return LinuxHostInfo

def uname(client: SSHClient, scan_info: LinuxHostInfo):
    try:
        logging.info('Start command: uname -snr')
        _, stdout, _ = client.exec_command('uname -snr')
        data = stdout.read().decode()[:-1].split(' ')
        scan_info.kernel_name = data[0]
        scan_info.nodename = data[1]
        scan_info.kernel_release = data[2]
        logging.info('Success command: uname -snr')
    except Exception:
        logging.exception('Fail command: uname -snr')
    
    try:
        logging.info('Start command: uname -v')
        _, stdout, _ = client.exec_command('uname -v')
        data = stdout.read().decode()[:-1]
        scan_info.kernel_version = data
        logging.info('Success command: uname -v')
    except Exception:
        logging.exception('Fail command: uname -v')
    
    return LinuxHostInfo

def arch(client: SSHClient, scan_info: LinuxHostInfo):
    try:
        logging.info('Start command: arch')
        _, stdout, _ = client.exec_command('arch')
        data = stdout.read().decode()[:-1]
        scan_info.architecture = data
        logging.info('Success command: arch')
    except Exception:
        logging.exception('Fail command: arch')
    return LinuxHostInfo