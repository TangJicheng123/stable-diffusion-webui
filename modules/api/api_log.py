import socket
from datetime import datetime

def get_log_head():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    result = f"[{current_time}] [{hostname}] [{ip_address}]"
    return result
