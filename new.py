# from flask import Flask
# from data import db_session
# from data.jobs import Jobs
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


def main():
    name = input()
    global_init(f"{name}")
    db_sess = create_session()
    for job in db_sess.query(Jobs).all():
        x, start = str(job.start_date).split()
        y, end = str(job.end_date).split()
        start = int(start.split(":")[0]) * 60 + int(start.split(":")[1]) + int(start.split()[2]) / 60
        end = int(end.split(":")[0]) * 60 + int(end.split(":")[1]) + int(end.split()[2]) / 60
        if (end / 60 - start / 60) < 20:
            print(job)


if __name__ == '__main__':
    main()
