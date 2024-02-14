#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import json
import random
import base64
from database import *
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)

api = Api(app)

GRADE_UNIT = {
    1:"덧셈과 뺄셈",
    2:"나눗셈1",
    3:"곱셈1",
    4:"길이와 시간",
    5:"분수와 소수",
    6:"곱셈2",
    7:"나눗셈2",
    8:"분수",
    9:"들이와 무게",
    10:"큰 수",
    11:"곱셈과 나눗셈",
    12:"규칙 찾기",
    13:"분수의 덧셈과 뺄셈1",
    14:"소수의 덧셈과 뺄셈",
    15:"자연수의 혼합 계산",
    16:"약수와 배수",
    17:"규칙과 대응",
    18:"약분과 통분",
    19:"분수의 덧셈과 뺄셈2",
    20:"분수와 소수의 계산",
    21:"수의 범위와 어림하기",
    22:"분수의 곱셈",
    23:"소수의 곱셈",
    24:"평균과 가능성",
    25:"분수의 나눗셈1",
    26:"소수의 나눗셈1",
    27:"바와 비율",
    28:"분수의 나눗셈2",
    29:"소수의 나눗셈2",
    30:"비례식과 비례배분"
}

class getinfo(Resource):
    def post(self):
        try:
            guno = request.get_json()['guno']
            count = request.get_json()['count']
            lbno = request.get_json()['lbno']

            print("guno :", guno)
            print("count :", count)
            print("lbno :", lbno)

            unit_value = GRADE_UNIT[guno]
            print(unit_value)
            question_info = getQuestionInfo(unit_value, lbno)
            print(len(question_info))
            result = []

            if len(question_info) >= count:
                while True:
                    choice = random.randint(0,len(question_info)-1)
                    if question_info[choice] not in result:
                        result.append(question_info[choice])

                    if len(result) == count:
                        break
            else:
                result = question_info
                while True:
                    choice = random.randint(0,len(question_info)-1)
                    result.append(question_info[choice])

                    if len(result) == count:
                        break

            return result
        except Exception as e:
            return {'error': str(e)}



api.add_resource(getinfo, '/getinfo')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=21731)

