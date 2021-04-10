import logging

logger = logging.getLogger(__name__)

logger.error('API call is failed')

# key,valueの形式で書くと解析しやすい
logger.error({
    'action':'create',
    'status':'fail',
    'message':'api call is fail'
})