import logging
import os


class DescLog:

    def __init__(self, path=None):
        log_home = os.environ.get("PYQUEUE_LOG_HOME")
        if path is not None:
            filepath = f"{path}/desc.log"
        elif log_home is not None:
            filepath = f"{log_home}/desc.log"
        else:
            filepath = f"desc.log"
        logging.basicConfig(filename=filepath, level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

