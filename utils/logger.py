import logging, coloredlogs

def settingsColor():
    format = '%(asctime)s | %(name)s | %(levelname)s => %(message)s'
    coloredlogs.install(level=logging.DEBUG, fmt=format)

def getLoggerAplication(className="root"):
    return logging.getLogger(name=className)