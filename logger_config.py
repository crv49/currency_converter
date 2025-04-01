import logging

def setup_logging():
    logger = logging.getLogger("currency_converter")
    logger.setLevel(logging.INFO)

# Set up handlers if they dont exist
    if not logger.handlers:
        fh = logging.FileHandler("converter.log", mode = "w")
        fh.setLevel("INFO")

        sh = logging.StreamHandler()
        sh.setLevel("INFO")

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)
        
    return logger
