import requests
import json

class Me:
    def __init__(self, stName, stId, userId, stMobile, id, stuClass):
        self.stName = stName
        self.stId = stId
        self.userId = userId
        self.stMobile = stMobile
        self.id = id
        self.stuClass = stuClass
        self.data = {
    "stuClass": self.stuClass,
    "schoolId": "10530",
    "schoolName": "湘潭大学",
    "stId": self.stId,
    "userId": self.userId,
    "stName": self.stName,
    "locationAddr": "湖南省湘潭市岳塘区湘潭大道辅路",
    "id": self.id,
    "departments": "302e63bf3d6840a981608c411cecfe34",
    "isContact": "N",
    "isFever": "0",
    "isWuhan": "N",
    "nowArea": "湖南省湘潭市雨湖区",
    "familyaddress": "北二环路湘潭大学琴湖公寓",
    "familyStatus": "0",
    "diagnosisTreatment": "",
    "nowStatus": "0",
    "healthStatus": "3",
    "isLevel": "N",
    "isbackLive": "N",
    "trafficTool": "",
    "backTrafficTool": "",
    "levelDate": "",
    "backtime": "",
    "arriveAddr": "",
    "trafficNo": "",
    "backTrafficNo": "",
    "professional": "9D7B8587B2C44DA8E0539349FD0A7824",
    "personType": "",
    "personCategory": "null",
    "temperature": 36.5,
    "remarks": "null",
    "timeToLeaveHuBei": "",
    "dateOfDisengagement": "",
    "otherSymptoms": "",
    "nowStatusStartTime": "",
    "familyStatusStartTime": "",
    "feverStartTime": "",
    "coughStartTime": "",
    "fatigueStartTime": "",
    "diarrheaStartTime": "",
    "coldStartTime": "",
    "headacheStartTime": "",
    "noseStartTime": "",
    "runnyStartTime": "",
    "throatStartTime": "",
    "conjunctivaStartTime": "",
    "isAppearDiagnosis": "N",
    "isVaccinate": "1",
    "vaccineType": "2",
    "injectTimes": "3",
    "otherDesc": "null",
    "isContactWithDiagnosis": "N",
    "isInSchool": "",
    "stMobile": self.stMobile
}

    def submit(self):
        url = 'https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak'
        headers = {
            'Cookie': 'IN001=1004|Yr2NB; IN010=10003|Yr2NB; IN008=8002|Yr2M+; tgw_l7_route=b4a2b070a06be49f6d4bc2cc256e8b19',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.4(0x13040010) MiniProgramEnv/Mac MiniProgram'
        }

        res = requests.post(url, json=self.data, headers=headers)
        return res

if __name__=='__main__':
    stName = ["王涵宇", "蒋文丰", "王瑞泽", "魏旭辉"] # 你的名字
    stId = ["201905820507", "201905135419", "201905556623", "201905556525"] #你的学号
    userId = ["A3231001163755965259275601", "A3231003156689466575672600", "A3231002156907574660646304", "A3231003156697452900697601"] #抓包拿到的userId
    stMobile = ["19967231936", "15507470821", "17377918196", "18274327201"] # 你的电话号码
    id = ["E2915B8271473337E0539349FD0AE2B3", "E2AD5E139219AC60E0539349FD0A5E5D", "E2AD5E59DF61AF44E0539349FD0A14F2", "E2915B826C523337E0539349FD0AE2B3"] #抓包拿到的id
    stuClass = ["9999", "9999", "9999", "9999"]

    for i in range(len(stName)):
        student = Me(stName[i], stId[i], userId[i], stMobile[i], id[i], stuClass[i])
        res = student.submit()
        print(student.stName, res.text)