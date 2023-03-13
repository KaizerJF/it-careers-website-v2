from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Taguig, Philippines',
  'salary': 'Php.40,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Makati, Philippines',
  'salary': 'Php.35,000'
}, {
  'id': 3,
  'title': 'Software Engineer',
  'location': 'Pasig, Philippines',
  'salary': 'Php.40,000'
}, {
  'id': 4,
  'title': 'Web Developer',
  'location': 'Mandaluyong, Philippines',
  'salary': 'Php.50,000'
}, {
  'id': 5,
  'title': 'Data Scientist',
  'location': 'Alabang, Philippines',
  'salary': 'Php.70,000'
}]


@app.route("/")
def main_app():
  return render_template('index.html', jobs=JOBS)


@app.route('/api/jobs')
def joblist():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
