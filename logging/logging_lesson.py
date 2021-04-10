import logging

'''
    別のモジュールなどでログレベルを指定する時にはloggerを作成する
'''

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logging_lesson.log')
logger.addHandler(h)

def do_something():
    logger.info('from logging_lesson')
    logger.debug('from logging_lesson')