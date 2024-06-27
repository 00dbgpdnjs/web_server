'''Config for flask app (web-server)'''

import os
from secret import csrf_token_secret

# main workplace
BASE_DIR = os.path.dirname(__file__) # __file__ (config.py)이 있는 디렉토리

# Secret key for CSRF token
SECRET_KEY = csrf_token_secret

# 전송받은 파일을 저장할 path
# - UI에서 "서버 전송하기" 버튼 누르면 파일이 전송되기 때문
UPLOAD_FILE_DIR = 'server/static/files/upload/' 
TEMP_FILE_DIR = 'server/static/files/temp/' 

# TODO
# - Database config