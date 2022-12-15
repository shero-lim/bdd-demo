import logging


def log_formatter():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logfile = './log.txt'
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
