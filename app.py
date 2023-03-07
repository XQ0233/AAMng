from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Liaoning, Shenyang',
    'salary': '1,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Liaoning, Dalian',
    'salary': '2,000'
  },
  {
    'id': 3,
    'title': 'Frotend Engineer',
    'location': 'Liaoning, Benxi',
    'salary': '3,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Liaoning, Tieling',
    'salary': '4,000'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name="Qhd")

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)