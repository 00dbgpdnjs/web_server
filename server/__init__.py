'''app (web server) for deep learning service deployment'''

from flask import Flask
from flask_socketio import SocketIO
import config # config.py

socketio = SocketIO() # Socket.io 객체 생성

def create_app() -> Flask:
    '''create app for service'''
    app = Flask(__name__) # arg : 앱 이름(__name__ : 디렉토리명(server))
    app.config.from_object(config)
    
    from .views import main_views
    
    app.register_blueprint(
        main_views.bp,
        
    )
    
    socketio.init_app(app) # socket.io 등록
    
    return app

    