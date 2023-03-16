import os

from typing import Dict
from urllib.parse import quote

from pydantic import BaseSettings


# PROJECT ROOT 상대경로
PROJECT_ROOT: str = os.path.dirname(
    os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
LOG_DIR = os.path.join(PROJECT_ROOT, 'src', 'logs')
APP_DIR = os.path.join(PROJECT_ROOT, 'src', 'app')

class Settings(BaseSettings):
    # PROJECT_NAME
    PROJECT_NAME: str = "FASTAPI"
    API_ENTRYPOINT: str = "/api"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DEBUG: bool = True
    
    # DB INFO Settings
    DB_URI_TEMPLATE: Dict[str, str] = {
        'SQLITE': "sqlite:///{}{}{}{}{}./myapi.db" # main.py 동일 경로에 myapi.db 위치
        , 'MARIADB': "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4"
        , 'progresDB': "postgresql://{}:{}@{}:{}/{}"
    }
    DB_CONNECTION_INFO: Dict[str, Dict[str, str]] = {
        'SQLITE': {
            'user': ''
            ,'pwd': ''
            ,'host': ''
            ,'port': ''            
            ,'database': ''
        },
        'MARIADB': {
            'user': 'root'
            ,'pwd': '1234'
            ,'host': 'localhost'
            ,'port': '3306'            
            ,'database': 'allocation'
        },
        'postgresDB': {
            'user': 'allocation'
            ,'pwd': 'abc123'
            ,'host': 'localhost'
            ,'port': '5432'            
            ,'database': 'postgres'
        }
    }

    def get_db_uri(
        self
        , uri_type: str
        , user: str
        , pwd: str
        , host: str
        , port: str
        , database: str
    ) -> str:
        """
        DB URI by DB TYPE

        Args:
            uri_type (str): DB TYPE
            user (str): user
            pwd (str): pwd
            host (str): host
            port (str): port
            database (str): database

        Returns:
            str: DB URI
        """
        return self.DB_URI_TEMPLATE[uri_type].format(
            user
            , pwd
            , host
            , port
            , database
        )
    
    def get_api_url(self) -> str :
        return f"http://{self.HOST}:{self.PORT}/api"
    
settings = Settings()