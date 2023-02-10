from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class SqliteConn:
    def __init__(self, **engine_kwargs):
        conn_url = self.get_conn_url()

        if 'echo' not in engine_kwargs:
            engine_kwargs['echo'] = False

        self.engine = create_engine(conn_url, **engine_kwargs)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

    def get_conn_url(self) -> str:
        conn_str = f'sqlite:///crime.db'
        return conn_str

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

_DB_CONN: SqliteConn = None

def init_db(**engine_kwargs) -> None:
    global _DB_CONN
    if _DB_CONN is not None:
        print('DB already initialised')
    else:
        print('Initializing DB')
        _DB_CONN = SqliteConn(**engine_kwargs)

def get_db() -> SqliteConn:
    if _DB_CONN is None:
        raise ValueError('DB hasn\'t been initialised')
    return _DB_CONN
