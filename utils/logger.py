import logging
import os


os.makedirs("reports", exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("reports/automation.log", mode="a"),
        logging.StreamHandler()
    ],
    force=True
)


logger = logging.getLogger(__name__)