#-*- coding: utf-8 -*-

import latex2mathml.converter
import hml_equation_parser as hp
from xml.etree.ElementTree import fromstring, Element, ElementTree
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


def convertSpace2nbsp(string: str) -> str:
    return string.replace(' ', r'&nbsp;')

def parseHmlSample(xmlText: str) -> ElementTree:
    hwpml = fromstring(xmlText)
    body = hwpml.find("BODY")
    section = body.find("SECTION")

    docRoot = Element("HmlParser")

    paragraphs = section.findall("P")

    for paragraph in paragraphs:

        paragraphNode = Element("Paragraph")

        if paragraph.get("PageBreak") == "true":
            paragraphNode.attrib["NewPage"] = "true"
        else:
            paragraphNode.attrib["NewPage"] = "false"

        # I suupposed that there is one text tag or no text tag in one paragraph.
        # If there are more than one text, you must use `findall` method to find all text tags.
        
        text = paragraph.find("TEXT")
        if text is not None:
            for child in text.getchildren():
                if child.tag == "CHAR":
                    value = child.text

                    if value is not None:  # For EQUATION tag, there is a </CHAR> tag and it has no information.
                        leafNode = Element("Char")
                        leafNode.text = value
                        paragraphNode.append(leafNode)

                elif child.tag == "EQUATION":
                    script = child.find("SCRIPT")
                    value = script.text
                    
                    leafNode = Element("Equation")
                    leafNode.text = value
                    paragraphNode.append(leafNode)
                    
                else:
                    #print("not supported tag: {}".format(child.tag))
                    pass

            docRoot.append(paragraphNode)

    return ElementTree(docRoot)


def convertFromFile(path: str, _type: str, _useTag: bool) -> dict:
    doc = hp.parseHmlSample(path)
    return convert2html(doc, _type, _useTag)

def convertFromString(xmlString: str, _type: str, _service_id: str,  _useTag: bool) -> dict:
    doc = parseHmlSample(xmlString)
    return convert2html(doc, _type, _service_id, _useTag)


def convertEquationSample(doc):
    for paragraph in doc.findall("Paragraph"):
        for child in paragraph.getchildren():
            if child.tag == "Equation":
                child.text = hp.eq2latex(child.text)
    return doc

def convert2html(doc: ElementTree, _type: str, _service_id: str,  _useTag: bool) -> dict:
    #doc = convertEquationSample(doc)  # find equations from ElementTree and convert them to latex string            
    # for paragraph in doc.findall(config["NodeNames"]["paragraph"]):
    #     for child in paragraph.getchildren():
    #         if child.tag == config["NodeNames"]["equation"]:
    #             child.text = hmlEquation2latex(child.text)

    body_list = []
    list_list = []
    answer_list = []
    explanation_list = []

    BODY_START_TEXT = '(문제)'
    LIST_START_TEXT = '(선택지)'
    ANSWER_START_TEXT = '(답):'
    ANSWER_START_TEXT2 = '(정답)'
    ANSWER_START_TEXT3 = '(답)'
    EXPLANATION_START_TEXT = '(해설)'
    EXPLANATION_END_TEXT = '(문항정보)'
    EXPLANATION_END_TEXT2 = '(문항타입)'

    CONVERT_TABLE = True
    TABLE_START_TEXT = '$$표$$'
    TABLE_END_TEXT = '$$/표$$'
    TABLE_START_HTML = '<table border="1" bordercolor="black" cellspacing="0" cellpadding="0" width ="100%" height="100%" align = "center" ><tr align ="center"><td>'
    TABLE_END_HTML = '</td></tr></table>'

    current_type = None

    for paragraph in doc.findall("Paragraph"):
        paragraphStringList = []
        
        # if paragraph.get(config["NodeAttributes"]["newPage"]) == "true":
        #     paragraphStringList.append("\n<br/>======================<br/>\n")

        for child in paragraph.getchildren():
            if child.tag == "Char":
                
                text = child.text
                if not current_type and BODY_START_TEXT in child.text:
                    current_type = BODY_START_TEXT
                    text = text.lstrip(current_type)
                elif current_type and LIST_START_TEXT in child.text:
                    current_type = LIST_START_TEXT
                    text = text.lstrip(current_type)
                elif current_type and ANSWER_START_TEXT in child.text:
                    current_type = ANSWER_START_TEXT
                    text = text.lstrip(current_type)
                elif current_type and ANSWER_START_TEXT2 in child.text:
                    current_type = ANSWER_START_TEXT
                    text = text.lstrip(ANSWER_START_TEXT2)
                elif current_type and ANSWER_START_TEXT3 in child.text:
                    current_type = ANSWER_START_TEXT
                    text = text.lstrip(ANSWER_START_TEXT3)
                elif current_type and EXPLANATION_START_TEXT in child.text:
                    current_type = EXPLANATION_START_TEXT
                    text = text.lstrip(current_type)
                elif current_type and EXPLANATION_END_TEXT in child.text:
                    current_type = EXPLANATION_END_TEXT
                elif current_type and EXPLANATION_END_TEXT2 in child.text:
                    current_type = EXPLANATION_END_TEXT

                if current_type == BODY_START_TEXT and text.startswith('①'):
                    current_type = LIST_START_TEXT

                if current_type in [BODY_START_TEXT, LIST_START_TEXT, ANSWER_START_TEXT, EXPLANATION_START_TEXT]:
                    text = text.replace('\n', '')
                    if len(text) <= 0:
                        continue
                    # print('Char: ['+text+']')
                    if _useTag:
                        text = convertSpace2nbsp(text)
                    if current_type == BODY_START_TEXT and len(body_list) > 0:
                        pass
                    elif not current_type in [LIST_START_TEXT] and _useTag: 
                        text = '<span style="vertical-align: baseline;">'+text+'</span>'
                    if CONVERT_TABLE:
                        if _useTag:
                            text = text.replace(TABLE_START_TEXT, TABLE_START_HTML)
                            text = text.replace(TABLE_END_TEXT, TABLE_END_HTML)   
                    paragraphStringList.append(text)

            elif child.tag == "Equation":

                output = child.text 
                output = output.lstrip('\n')
                # output = output.replace('\ ', '')  # 빈칸

                
                # 일단 &는 제거
                if "&" in output:
                    output = output.replace("&", "")
                # 중괄호 종료가 부족한 경우
                while output.count("{") > output.count("}"):
                    output = output + " }"
                # 중괄호 종료가 많은 경우
                while output.count("{") < output.count("}"):
                    #output = output + " }"
                    k = output.rfind("}")
                    output = output[:k] + "" + output[k+1:]

                #Therefore 
                output = output.replace("Therefore", " THEREFORE ")
                output = output.replace("THEREFORE", " THEREFORE ")
                
                #Times
                # if "Times" in output:
                #     output = output.replace("Times", "\\times")
                

                #\%
                if "%" in output:
                    output = output.replace("%", "\%")
                    if "\\%" in output:
                        output = output.replace("\\%", "\%")
                # # 이탤릭 제거 rm =
                if "rm" in output:
                    output = output.replace("rm", " rm ")
                
                #LEFT, RIGHT 띄어쓰기 문제
                if "LEFT" in output:
                    output = output.replace("LEFT", " LEFT")
                #    output = output.replace(" LEFT", " \left")
                if "RIGHT" in output:
                    output = output.replace("RIGHT", " RIGHT")
                #    output = output.replace(" RIGHT", " \right")

                # CDOTS 띄어쓰기 문제
                if "CDOTS" in output:
                    output = output.replace("CDOTS", " CDOTS ")
                # # UNDER \underline
                # if "UNDER" in output:
                #     output = output.replace("UNDER", " \\underline ")

                while "div" in output:
                    output = output.replace("div", "DIV")
                while "DIV" in output:
                    output = output.replace("DIVIDE", "\div")
                    output = output.replace("DIV", "\div")
                if "Div" in output:
                    output = output.replace("Div", "\div")

                #BOX 띄어쓰기 문제
                if "BOX" in output:
                    output = output.replace("BOX", "BOX ")
                if "box" in output:
                    output = output.replace("box", "BOX ")
                if "Box" in output:
                    output = output.replace("Box", "BOX ")
            
                temp_output = output
                # if "BOX" in temp_output and not "BOX{" in temp_output:
                #     temp_output = temp_output.replace("BOX", "BOX ")
                # if not "BOX{" in temp_output:
                temp_output = temp_output.replace("{", " { ")
                temp_output = temp_output.replace("}", " } ")
                temp_output = temp_output.replace(". ", " ")
                output = temp_output
                # 숫자 혹은 문자가 정해진 기호가 아니면 중괄호로 묶어버리자
                output_list = []
                for o in temp_output.split(' '):
                    temp_o = o
                    if o.replace('.','',1).isdigit():
                        temp_o = '{'+o+'}'
                    else:
                        temp_o2 = ''
                        # digit 가 문자열 내에 있는지 확인
                        bracket_opened = False
                        for to2 in temp_o:
                            if to2.replace('.','',1).isdigit():
                                if not bracket_opened:
                                    temp_o2 = temp_o2 + '{' + to2
                                    bracket_opened = True
                                else:
                                    temp_o2 = temp_o2 + to2
                            elif bracket_opened:
                                temp_o2 = temp_o2 + '}' + to2
                                bracket_opened = False
                            else:
                                temp_o2 = temp_o2 + to2
                        if bracket_opened:
                            temp_o2 = temp_o2 + '}'
                        temp_o = temp_o2
                    
                    output_list.append(temp_o)
                output = ' '.join(output_list)    
                
                output = output.replace("LEFT (", "(")
                output = output.replace("RIGHT )", ")")
                output = output.replace("LEFT {", "{")
                output = output.replace("RIGHT }", "}")
                output = output.replace("LEFT [", "[")
                output = output.replace("RIGHT ]", "]")

                # # TODO: 중괄호로 묶어줘야 할듯함.
                for unit in ["cm", "kg"]:
                    if unit in output:
                        output = output.replace(unit, "{"+unit+"}")

                output = hp.eq2latex(output)  # 수식 -> latex
               

                # 예외처리...
                # BOX
                if "HULKBOX" in output:
                    output = output.replace("HULKBOX \, \, \, \, \, \, \,", "{ \\boxed {\, \, \, \, \, \, \,} }")
                    if "HULKBOX" in output:
                        output = output.replace("HULKBOX", "")

                if "\\times { \\boxed{ \\times" in output:
                    output = output.replace("\\times { \\boxed{ \\times", " { \\boxed{ \\times")
                if "\\times \\boxed{ \\times" in output:
                    output = output.replace("\\times \\boxed{ \\times", "\\boxed{ \\times")



                output = output.lstrip()                
                if _type == 'mathml':
                    output = latex2mathml.converter.convert(output)
                    output = output.lstrip()
                    if _useTag:
                        output = '<span class="ccctex " style="">'+output+'</span>'
                else:
                    # output = output.replace(' ', '\ ')  # 빈칸
                    if _useTag: 
                        output = '<span class="ccctex " style="">$$  {'+output+'}  $$</span>'

                output = output.lstrip()

                if current_type in [BODY_START_TEXT, LIST_START_TEXT, ANSWER_START_TEXT, EXPLANATION_START_TEXT]:
                    paragraphStringList.append(output)
        
        paragraphString = ''.join(paragraphStringList).lstrip()

        if len(paragraphString) > 0:       
            if current_type == BODY_START_TEXT:
                body_list.append(paragraphString)
            elif current_type == LIST_START_TEXT:
                list_list.append(paragraphString)
            elif current_type == ANSWER_START_TEXT:
                answer_list.append(paragraphString)
            elif current_type == EXPLANATION_START_TEXT:
                explanation_list.append(paragraphString)

    if len(list_list) <= 0:
        if _service_id == "jp":
            text = '<span style="vertical-align: baseline;">(記述式問題です。)</span>'
        else:
            text = '<span style="vertical-align: baseline;">(주관식 문항입니다.)</span>'
        list_list.append(text)

    return {'r': 0, 'body_list':body_list, 'list_list':list_list, 'answer_list':answer_list, 'explanation_list':explanation_list}


template = env.get_template('template.html')
body_template = env.get_template('body_html.html')
choice_template = env.get_template('list_html.html')
answer_template = env.get_template('answer_html.html')
comment_template = env.get_template('explanation_html.html')

def convert2htmlFromString(xmlString: str, _type: str, _service_id: str) -> dict:
    result = convertFromString(xmlString, _type, _service_id, True)
    
    body_html = body_template.render(body_list=result['body_list'])
    list_html = None
    if result['list_list']:
        list_html = choice_template.render(choice_list=result['list_list'])
    answer_html = answer_template.render(answer=', '.join(result['answer_list']))
    explanation_html = comment_template.render(comment_list=result['explanation_list'])
    return {'r': 0, 'body_html':body_html, 'list_html':list_html, 'answer_html':answer_html, 'explanation_html':explanation_html, 'service_id': _service_id}