import logging

import logging_lesson

# logging.basicConfig(filename='test.log', level=logging.INFO)　# ログをファイルに出力する場合

# formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(level=logging.INFO, format=formatter)  # ログのフォーマットを指定

logging.basicConfig(level=logging.INFO)
logging.info('info from main')

# ロガーを作成
logger = logging.getLogger(__name__)

logging_lesson.do_something() # ここで表示されるログについて、メインのログか別モジュールで呼ばれたログかがわかる

"""
    フィルター
"""
class NoPassFileter(logging.Filter):
    def filter(self, record) -> bool:
        log_message = record.getMessage()
        return 'password' not in log_message

logger.addFilter(NoPassFileter())
logger.info('from main')
logger.info('from main password = "wwwxxx"')