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

def log_with_loading(func):
	loading_chars = ['▖', '▗', '▝', '▘']
	index = 0

	def log_wrapper(*args, **kwargs):
		if index == len(loading_chars):
			index = 0

		sys.stdout.write(f'\r{loading_chars[index]}')
		index += 1

		return func(*args, **kwargs)

def log(message, level='debug'):
	def decorator(func):
		def log_message_wrapper(self, *args, **kwargs):
			__get_logger(level)(str(message).format(self))
			return func(self, *args, **kwargs)
		return log_message_wrapper
	return decorator
