import logging


class DescLog:

    def __init__(self, path=None):
        if path is not None:
            filepath = f"{path}/desc.log"
        else:
            filepath = f"desc.log"
        logging.basicConfig(filename=filepath, level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

