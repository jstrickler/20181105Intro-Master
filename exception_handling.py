#!/usr/bin/env python
import logging
from configparser import ConfigParser

config = ConfigParser()

config.read('mystuff.ini')

log_level = config['general']['log_level']

if log_level == 'critical':
    log_flag = logging.CRITICAL
elif log_level == 'error':
    log_flag = logging.ERROR
elif log_level == 'warning':
    log_flag = logging.WARNING
elif log_level == 'info':
    log_flag = logging.INFO
elif log_level == 'debug':
    log_flag = logging.DEBUG


logging.basicConfig(filename='mystuff.log', level=log_flag)

values = [0, 2.6, 3.9, 'abc', 1.7, 2.8, 0, 5.4, 4.1]

m = 22.1

for v in values:
    try:
        result = m / v
    except ZeroDivisionError as err:
        print(err)
        logging.critical("Zero division!!")
    except (TypeError, ValueError) as err:
        print(err)
        logging.warning("Bad type")
    except Exception as err:  # will catch *any* error
        logging.warning("Unexpected!")
        print(err)
    else:
        print("result is {}".format(result))
    finally:
        print("Cleaning up...")
