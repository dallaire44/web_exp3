from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request


application = Flask(__name__)

client = MongoClient('localhost:27017')
db = client.QualificationData

@application.route("/addQualification",methods=['POST'])
def addQualification():
    print("-----" + str(request.json))
    try:
        json_data = request.json['info']
        jobName = json_data['job']
        textContent = json_data['text']
        link1Input = json_data['link1']
        link2Input = json_data['link2']
        link3Input = json_data['link3']

        db.Qualifications.insert_one({
            'job':jobName,'text':textContent,'link1':link1Input,'link2':link2Input,'link3':link3Input
            })
        return jsonify(status='OK',message='inserted successfully')

    except Exception as e:
        return jsonify(status='ERROR',message=str(e))



@application.route('/')
def showQualificationsList():
    return render_template('list.html')


@application.route('/getQualification',methods=['POST'])
def getQualification():
    try:
        qualificationId = request.json['id']
        qualification = db.Qualifications.find_one({'_id':ObjectId(qualificationId)})
        qualificationDetail = {
                'job':qualification['job'],
                'text':qualification['text'],
                'link1':qualification['link1'],
                'link2':qualification['link2'],
                'link3':qualification['link3'],
                'id':str(qualification['_id'])
                }
        return json.dumps(qualificationDetail)
    except Exception as e:
        return str(e)

@application.route('/updateQualification',methods=['POST'])
def updateQualification():
    try:
        qualificationInfo = request.json['info']
        qualificationId = qualificationInfo['id']
        job = qualificationInfo['job']
        text = qualificationInfo['text']
        link1 = qualificationInfo['link1']
        link2 = qualificationInfo['link2']
        link3 = qualificationInfo['link3']

        db.Qualifications.update_one({'_id':ObjectId(qualificationId)},{'$set':{'job':job,'text':text,'link1':link1,'link2':link2,'link3':link3}})
        return jsonify(status='OK',message='updated successfully')
    except Exception as e:
        return jsonify(status='ERROR',message=str(e))






@application.route("/getQualificationList",methods=['POST'])
def getQualificationList():
    try:
        qualifications = db.Qualifications.find()
        
        qualificationList = []
        for qualification in qualifications:
            print(qualification)
            qualificationItem = {
                    'job':qualification['job'],
                    'text':qualification['text'],
                    'link1':qualification['link1'],
                    'link2':qualification['link2'],
                    'link3':qualification['link3'],
                    'id': str(qualification['_id'])
                    }
            qualificationList.append(qualificationItem)
    except Exception as e:
        return str(e)
    return json.dumps(qualificationList)

@application.route("/deleteQualification",methods=['POST'])
def deleteQualification():
    try:
        qualificationId = request.json['id']
        db.Qualifications.remove({'_id':ObjectId(qualificationId)})
        return jsonify(status='OK',message='deletion successful')
    except Exception as e:
        return jsonify(status='ERROR',message=str(e))



if __name__ == "__main__":
    application.run()
