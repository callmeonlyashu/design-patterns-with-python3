import logging
import logging.config
import yaml
import os

cwd = os.getcwd()

with open(f'{cwd}/config/config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('Logger has started')