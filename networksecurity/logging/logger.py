import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=log_file_path,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)