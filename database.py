from sqlalchemy import create_engine, text
import os

db_connection = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._asdict()))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), id=id)
    row = result.fetchone()
    if row is None:
      return None
    else:
      return dict(row.items())
