from flask import Flask,render_template,jsonify,json,request

application = Flask(__name__)

@application.route('/')
def showQualificationsList():
    return render_template('list.html')

if __name__ == "__main__":
    application.run()
