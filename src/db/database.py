import psycopg as pg
import environs
from src.utils import ROOT_DIR

# Set up the environs
env = environs.Env()

env.read_env(str(ROOT_DIR / '.env'))

# Singelton
class Database(object):

    __instance = None

    def __new__(cls):
        if Database.__instance is None:
            Database.__instance = super().__new__(cls)
            Database.__instance.__init__()
        
        return Database.__instance.__conn

    def __init__(self) -> None:
        self.__conn = pg.connect(
            # host = 'localhost
            dbname = env.str('db_name'),
            user = env.str('db_user'),
            password = env.str('db_password')
            # port = 5432
        ) 

if __name__ == '__main__':
    conn = Database()
    print(conn)