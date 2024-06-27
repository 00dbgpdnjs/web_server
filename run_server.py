''' Run server module'''

from server import create_app, socketio

server = create_app()

# 실행 시 기존에는 run.sh에서 flask run ~ 했는데,
#  서버를 가동시킬 때 socketio로 가동시켜야 해서
#  더 설정해줘야 함

if __name__=='__main__': # 이 모듈이 호출되었을 때
	socketio.run(app=server, debug=True, host='0.0.0.0', port='5678')