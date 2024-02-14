import requests
import json
from collections import OrderedDict

url = "http://cms.iscream.cceapi.com/cms_api/get_questions"

querystring = {"questions":"76032"}

key_etc_category = "etc_category"
key_category = "category"


def load_data(solo, min_id=None, max_id=500):
    """
    :param min_id: 최소 id
    :param max_id: 최대 id
    """

    if min_id is not None:
        ids = list(range(min_id, max_id, 1))
        ids = ",".join([str(i) for i in ids])
    else:
        ids = str(solo)
    querystring["questions"] = ids

    headers = {
        'User-Agent': "PostmanRuntime/7.16.3",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "06871714-cea0-4279-87d7-2f70a563ab0c,2989a3ec-862a-406b-9cdd-c231fa7b014f",
        'Host': "cms.iscream.cceapi.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    loads = json.loads(response.text)

    return loads


def split_data(full_json):
    item = full_json
    # new_items = []
    # for item in items:
    new_item = {}
    new_item["service_id"] = item["service_id"]
    new_item["id"] = item["question_id"]
    new_item[key_etc_category + "1"] = item[key_etc_category + "1"].strip()
    new_item[key_etc_category + "2"] = item[key_etc_category + "2"].strip()
    new_item[key_etc_category + "3"] = item[key_etc_category + "3"].strip()
    new_item[key_etc_category + "4"] = item[key_etc_category + "4"].strip()
    
    if item[key_etc_category + "5"] != None:
        new_item[key_etc_category + "5"] = item[key_etc_category + "5"].strip()
        
    new_item[key_category + "1"] = item[key_category + "1"].strip()[3:].replace(",", ";")
    new_item[key_category + "2"] = item[key_category + "2"].strip()[3:].replace(",", ";")
    new_item[key_category + "3"] = item[key_category + "3"].strip()[3:].replace(",", ";")
    new_item[key_category + "4"] = item[key_category + "4"].strip()[3:].replace(",", ";")
    #new_item[key_category + "5"] = item[key_category + "5"].strip()
    new_item["chapter_code"] = item["chapter_code"].strip()

    new_item["body_html"] = decoding_html(item["body_html"]) + "\\n" + decoding_html(item["list_html"], True)

    # new_items.append(new_item)

    return new_item


def decoding_html(str_html, list_html=False):
    str_html = str_html.replace(">", "> ").replace("<", " <").replace("\n", " ").strip()
    h_tokens = str_html.split()
    nums = ['➀', '➁', '➂', '➃', '➄']

    str_block = ""
    flag_lt = False
    flag_item = False

    i = 0
    for h_token in h_tokens:
        item_count = 0

        if list_html:
            if "<li" in h_token:
                str_block += "%s " % nums[i]
                i += 1

        if "hspace" in h_token:
            continue

        if ">" in h_token:
            h_token = h_token[h_token.find(">") + 1:]
            flag_lt = False
            if not h_token:
                continue

        if flag_lt:
            continue

        if "<" in h_token:
            h_token = h_token[:h_token.find("<")]
            flag_lt = True
            if not h_token:
                continue

            if ">" in h_token:
                h_token = h_token[h_token.find(">") + 1:]
                flag_lt = False
                if not h_token:
                    continue

        if "$$" == h_token:
            flag_item = not flag_item
            if not flag_item:
                item_count = 1

        if h_token:
            if item_count:
                str_block += "%s " % "$$TOKEN$$"
            elif not flag_item:
                str_block += "%s " % h_token.replace("&nbsp;", " ").replace("\\\\", "")

    return str_block


def mapping_detect_json(id_items, strings, arguments, answer_id, selects=None, e=""):
    detects = [("r", 0), ("error_message", e)]

    if id_items == []:
        if "CATEGORY" in e:
            detects = [("r", 3), ("error_message", e)]
        else:
            detects = [("r", 4), ("error_message", e)]
        return dict(OrderedDict(detects))

    model_info = ("model",
                  OrderedDict([("grade", id_items[0]), ("model_id", id_items[1]), ("model_note", id_items[2])]))

    item_info = ("item_id", {"item": id_items[-1]})

    detects.append(model_info)
    detects.append(item_info)

    stem_info = ("stem_format", {"stem": strings[0]})
    answer_info = ("answer_format", {"answer": strings[1]})
    comment_info = ("comment_format", {"comment": strings[2]})

    detects.append(stem_info)
    detects.append(answer_info)
    detects.append(comment_info)

    # 고정
    requests_info = ("request_count",
                     OrderedDict([("min", 1), ("max", 1000), ("value", 10), ("default", 10)]))

    detects.append(requests_info)

    arg_info = []
    if type(arguments) != str and arguments:
        for argument in arguments:
            arg_ = [("title", argument[0]), ("note", argument[1])]
            if len(argument) > 3:
                arg_ += [("min", argument[-2]), ("max", argument[-1]), ("type", argument[-3]),
                         ("value", argument[-4]), ("default", argument[-4])]
            else:
                arg_ += [("min", 1), ("max", 1000), ("type", "int"), ("value", argument[-1]), ("default", argument[-1])]
            arg_info.append(OrderedDict(arg_))

    if selects:
        arg_ = [("title", answer_id)]
        arg_ += [("note", "객관식 %s 선택을 위한 필드 구성" % answer_id)]
        arg_ += [("type", "select")]
        arg_ += [("items", selects), ("default", "1")]
        arg_info.append(OrderedDict(arg_))
    else:
        arg_ = [("title", answer_id)]
        arg_ += [("note", "정답")]
        arg_ += [("type", "int")]
        arg_info.append(OrderedDict(arg_))

    detects.append(("arguments", arg_info))

    return dict(OrderedDict(detects))

# 기탄문제용 최종 output json
def mapping_detect_gt_json(item, item_id, strings, e=""):
    detects = [("r", 0), ("error_message", e)]

    if item == []:
        if "CATEGORY" in e:
            detects = [("r", 3), ("error_message", e)]
        else:
            detects = [("r", 4), ("error_message", e)]
        return dict(OrderedDict(detects))

    model_info = ("model",
                  OrderedDict([("grade", item["category1"]), ("model_id", item_id), ("model_note", item["category3"])]))

    #item_info = ("item_id", {"item": id_items[-1]})

    detects.append(model_info)
    #detects.append(item_info)

    stem_info = ("stem_format", {"stem": strings[0]})
    answer_info = ("answer_format", {"answer": strings[1]})
    comment_info = ("comment_format", {"comment": strings[2]})

    detects.append(stem_info)
    detects.append(answer_info)
    detects.append(comment_info)

    # 고정
    requests_info = ("request_count",
                     OrderedDict([("min", 1), ("max", 1000), ("value", 10), ("default", 10)]))

    detects.append(requests_info)

    #arg_info = []
    #if type(arguments) != str and arguments:
    #    for argument in arguments:
    #        arg_ = [("title", argument[0]), ("note", argument[1])]
    #        if len(argument) > 3:
    #            arg_ += [("min", argument[-2]), ("max", argument[-1]), ("type", argument[-3]),
    #                     ("value", argument[-4]), ("default", argument[-4])]
    #        else:
    #            arg_ += [("min", 1), ("max", 1000), ("type", "int"), ("value", argument[-1]), ("default", argument[-1])]
    #        arg_info.append(OrderedDict(arg_))

    #if selects:
    #    arg_ = [("title", answer_id)]
    #    arg_ += [("note", "객관식 %s 선택을 위한 필드 구성" % answer_id)]
    #    arg_ += [("type", "select")]
    #    arg_ += [("items", selects), ("default", "1")]
    #    arg_info.append(OrderedDict(arg_))
    #else:
    #    arg_ = [("title", answer_id)]
    #    arg_ += [("note", "정답")]
    #    arg_ += [("type", "int")]
    #    arg_info.append(OrderedDict(arg_))

    #detects.append(("arguments", arg_info))

    return dict(OrderedDict(detects))



#if __name__ == '__main__':
#    d = load_data(77141)
#    items = split_data(d)
#    for item in items:
#        print(item)
