import sys
import time
import threading
import logging

class Logger:
	pass

def __get_logger(level):
	return {
		'debug': logging.debug,
		'info': logging.info,
		'warning': logging.warning,
		'error': logging.error,
		'critical': logging.critical,
		'exception': logging.exception
	}.get(level, None)

def log(message, level='info'):
	def decorator(func):
		def log_method_wrapper(self, *args, **kwargs):
			__get_logger(level)(f'{message}'.format(self))
			return func(self, *args, **kwargs)
		return log_method_wrapper
	return decorator
