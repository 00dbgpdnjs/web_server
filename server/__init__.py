'''app (web server) for deep learning service deployment'''

from flask import Flask
import config # config.py

def create_app() -> Flask:
    '''create app for service'''
    app = Flask(__name__) # arg : 앱 이름(__name__ : 디렉토리명(server))
    app.config.from_object(config)
    
    from .views import main_views
    
    app.register_blueprint(
        main_views.bp,
        
    )
    
    return app

    