'''Main views'''

from asyncio import sleep
from datetime import datetime
from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
)
from werkzeug.utils import secure_filename
from server.forms import FileUploadForm
from config import UPLOAD_FILE_DIR

# socket.io 글로벌 객체 import
from server import socketio # server가 init 자체임

bp = Blueprint('main', __name__, url_prefix='/') # main으로 오면 앞에 '/' 붙임

@bp.route('/') # home으로 접속했을 때
def index():
    '''메인 페이지'''
    form = FileUploadForm()
    return render_template(
        'main.html',
        form=form,
    )
    # return 'Hello ACIN academy' # main에 접속했을 때 -> 원래는 html 반환해야하는데 문자열만 반환하면 알아서 만들어서 보내줌(빈 html에 저 문자열만 넣어서 보냄)


# # 이전 버전 (I 딥러닝 배포)
# @bp.route('/process', methods=['POST'])
# def process():
#     '''딥러닝 요청에 대한 답변'''
#     if request.method == 'POST': # request라는 http 약속대로 채워진걸 받음
#         files = request.files.getlist('file') # attach_file_handler에서 form_data.append('file', FILE_ARRAY[i]) 즉 'file'이라 해서
#         # 파일들을 메모리에만 저장하지 않고 /files 에 저장
#         for file in files:
#             prefix_name = f"{datetime.utcnow().strftime('%y%m%d_%H_%M_%S.%f')}_."
#             safe_fileame = prefix_name + secure_filename(file.filename) # 수상한 파일명 거름
#             file.save(UPLOAD_FILE_DIR + safe_fileame)
        
#         # 딥러닝 알고리즘
#         # 결과를 클라이언트에게 전달
#         return jsonify({
#             'content' : 'success'
#         })
            
    
#     return jsonify({'content': 'fail'}) 

# 비동기 처리: async, await, socket.io 등 반영
@bp.route('/process/<socket_id>', methods=['POST'])
async def process(socket_id):
    '''딥러닝 요청에 대한 답변'''
    if request.method == 'POST': # request라는 http 약속대로 채워진걸 받음
        files = request.files.getlist('file') # attach_file_handler에서 form_data.append('file', FILE_ARRAY[i]) 즉 'file'이라 해서
        # 파일들을 메모리에만 저장하지 않고 /files 에 저장
        for file in files:
            prefix_name = f"{datetime.utcnow().strftime('%y%m%d_%H_%M_%S.%f')}_."
            safe_fileame = prefix_name + secure_filename(file.filename) # 수상한 파일명 거름
            file.save(UPLOAD_FILE_DIR + safe_fileame)
        
        # 딥러닝 알고리즘
        # - 딥러닝 학습 -> epoch 10회 수행한다고 가정
        NUM_EPOCH = 10
        print('socket_id :', socket_id)
        for x in range(10):
            # Socket.io 통신 : 한 에폭이 끝날 때마다 몇 퍼센트 남았는지 알려줌
            percent = (x+1)/NUM_EPOCH * 100
            print(f'percent: {percent}%')
            # emit
            # - 1st : 변수명(클라이언트 단에서 값을 참조하기 위해)
            # - to : 특정 사용자의 프로그레스바만 업뎃되게
            socketio.emit('process_status', percent, to=socket_id) 
            await sleep(1)
        
        
        # 결과를 클라이언트에게 전달
        return jsonify({
            'content' : 'success'
        })
            
    
    return jsonify({'content': 'fail'})