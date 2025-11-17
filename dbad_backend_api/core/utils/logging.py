import logging
import logging.config
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).parent

LOG_CONFIG_FILE = BASE_DIR / "logging.yaml"

def setup_logging(config_file: Path = LOG_CONFIG_FILE):
    """Load logging config from YAML file."""
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)

# Create a shared logger instance
logger = logging.getLogger("app")  # use "app" as a global logger
