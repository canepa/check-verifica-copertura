import logging    # first of all import the module
## logger.debug("This is just a harmless debug message")
## logger.info("This is just an information for you")
## logger.warning("OOPS!!!Its a Warning")
## logger.error("Have you try to divide a number by zero")
## logger.critical("The Internet is not working....")

# Setup logging
def logsetup():
    logging.basicConfig(filename='cron-programs.log', filemode='a', format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',datefmt='%Y-%m-%d,%H:%M:%S')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger

