import os

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'data','config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH,'report', 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
print('CONFIG_FILE', CONFIG_FILE)
