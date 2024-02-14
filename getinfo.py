#-*-coding:utf-8-*-

import os
import json
import random
import base64
import traceback
import logging

from database import *
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from stem_directory import FUNC_DICT, FUNC_DICT_M
from func2html import *
from gt_generate import generate
from xml.etree.ElementTree import fromstring, Element, ElementTree
from hml2html import convert2htmlFromString
from detect_items import load_detector, detect

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, support_credentials=True)

api = Api(app)

# 로그
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('access.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

w_dict, _ = load_positions("./dictionary_11pt.txt")

def hml2html(hml):
    _hml = base64.b64decode(hml).decode('utf-8')
    _type = 'latex'
    _service_id = 'kr'

    return convert2htmlFromString(_hml, _type, _service_id)

# 문항 생성
def getGenerate(question):
    func_name = question["ETC_CATEGORY5"]
    logger.info(func_name)
    chapter_code = question["CHAPTER_CODE"]
    difficulty = question["DIFFICULTY"]

    if question["QUESTION_TYPE"] == "gt":
        body_html, answer_html, explanation_html, list_html = generate(
            func_name)

        res = {
            "r": 0,
            "id": func_name,
            "body_html": body_html,
            "list_html": list_html,
            "answer_html": answer_html,
            "explanation_html": explanation_html,
            "image_list": []
        }
    elif question["QUESTION_TYPE"] == "keyten":
        res = {
            "r": 0,
            "id": func_name,
            "body_html": question["BODY_HTML"],
            "list_html": question["LIST_HTML"],
            "answer_html": question["ANSWER_HTML"],
            "explanation_html": question["BODY_EXT"],
            "image_list": []
        }
    else:
        if chapter_code.startswith("CC"):
            func = FUNC_DICT[func_name]
        else:
            func = FUNC_DICT_M[func_name]

        if question["QUESTION_TYPE"] == "py":
            hmls_material, hmls_stem_material, hmls_answer_material, svgs = func2hmls(
                func, 1, w_dict, polygon=True)
        else:
            hmls_material, hmls_stem_material, hmls_answer_material, svgs = func2hmls(
                func, 1, w_dict)

        res = hml2html(hmls_material[0])

        res["image_list"] = svgs
        res["id"] = func_name

    res["difficulty"] = difficulty
    
    return res

class getinfo(Resource):
    def post(self):
        try:
            guno = request.get_json()['guno']
            count = request.get_json()['count']
            lbno = request.get_json()['lbno']
            d_type = request.get_json()['d_type']

            #unit_value = GRADE_UNIT[guno]
            # lbno 찾기
            lbno = getLearningObj(guno)
            
            print("guno :", guno)
            print("count :", count)
            print("lbno :", lbno)
            print("dtype :", d_type)
            
            if d_type == 1:
                difficulty = {
                    "low": 4,
                    "middle": 6,
                }
            elif d_type == 2:
                difficulty = {
                    "low": 2,
                    "middle": 5,
                    "high": 3
                }
            elif d_type == 3:
                difficulty = {
                    "middle": 3,
                    "high": 7
                }
            
            question_info = getQuestionInfo(lbno, d_type)
            
            if d_type == 1:
                q_temp = {
                    "low": [],
                    "middle": [],
                }
            elif d_type == 2:
                q_temp = {
                    "low": [],
                    "middle": [],
                    "high": []
                }
            elif d_type == 3:
                q_temp = {
                    "middle": [],
                    "high": []
                }
            
            # 난이도 별 문항 분류
            for q in question_info:
                if int(q["DIFFICULTY"]) == 1 or int(q["DIFFICULTY"]) == 2:
                    q_temp["low"].append(q)
                elif int(q["DIFFICULTY"]) == 3:
                    q_temp["middle"].append(q)
                else:
                    q_temp["high"].append(q)
            
            # 난이도 별 문항 수 조정
            z_len = []
            for i, d in enumerate(q_temp):
                if len(q_temp[d]) == 0:
                    z_len.append(i)
                    
            print(z_len)
            if len(z_len) == 1:
                if d_type == 1:
                    if z_len == [0] :
                        difficulty = {
                            "low": 0,
                            "middle": 10
                        }
                elif d_type == 2:
                    if z_len == [0]:
                        difficulty = {
                            "low": 0,
                            "middle": 6,
                            "high": 4
                        }
                    elif z_len == [2]:
                        difficulty = {
                            "low": 2,
                            "middle": 8,
                            "high": 0
                        }
            
            questions = []
            
            for key, value in difficulty.items():
                if len(q_temp[key]) == value:
                    continue
                if len(q_temp[key]) < value:
                    random_choice = random.choices(q_temp[key], k=value-len(q_temp[key]))
                    for r in random_choice:
                        q_temp[key].append(r)
                else:
                    q_temp[key] = random.sample(q_temp[key], value)
                    
            for key, value in q_temp.items():
                for v in value:
                    questions.append(v)
                    
            '''
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
            '''
            
            result = []
            for q in questions:
                logger.info("{id} {lbno} {difficult}".format(id=q["ETC_CATEGORY5"], lbno=q["LBNO"], difficult=q["DIFFICULTY"]))
                gen = getGenerate(q)
                result.append(gen)
            
            return result
        except Exception as e:
            logger.info(traceback.format_exc())

api.add_resource(getinfo, '/getinfo')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11731)#, debug=True)
    #app.run(host='10.9.184.4', port=11731)
