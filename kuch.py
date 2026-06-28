import sys
from src.exception import CustomException
try:
    x = int("abc")
except Exception as e:
    raise CustomException(e, sys)