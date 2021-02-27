from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    db_sess = db_session.create_session()
    for job in db_sess.query(Jobs).filter(Jobs.is_finished == 0):
        x, start = job.start_date.split()
        y, end = job.end_date.split()
        start = int(start.split(":")[0]) * 60 + int(start.split(":")[1]) + float(start.split(":")[2]) / 60
        end = int(end.split(":")[0]) * 60 + int(end.split(":")[1]) + float(end.split(":")[2]) / 60
        if (end - start) < 20:
            print(job)


if __name__ == '__main__':
    main()
