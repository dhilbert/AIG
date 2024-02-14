import inspect
import re

MSCHOOL_FLAG = "중등 수학 1"
CATEGORY1 = "2. 문자와 식"
CATEGORY2 = "1. 문자의 사용과 식의 계산"

SERVICE_KEY = "service_name"
MSCHOOL = "MIDDLE"

STEM_CATEGORY = "LinearEquation"

SELECT_NUMS1 = ["➀", "➁", "➂", "➃", "➄"]
SELECT_NUMS2 = ["①", "②", "③", "④", "⑤"]


def stem_mapping(input=5, target=3):
    """
    :param input: 입력
    :param target: 출력
    :return: 아
    """
    score = 0
    for i, t in zip(input, target):
        if type(i) == str:
            i = i.split()
            t = t.split()
        for i_token in i:
            if i_token in t:
                score += 1

    return score


def mapping_meta(meta, stem, stem_dict):
    vocab = {}

    service_name = meta[SERVICE_KEY]
    if MSCHOOL_FLAG in service_name:
        vocab = stem_dict[MSCHOOL]["1"]

    if CATEGORY1 == meta["category1"]:
        vocab = vocab["3"]

    if CATEGORY2 == meta["category2"]:
        vocab = vocab[STEM_CATEGORY]["1"]["Basic"]

    detected = []

    for item in vocab.items():
        for in_item in item[1].items():
            score = stem_mapping(stem, in_item[1])
            if score:
                detected.append((score, in_item[0], in_item[1]))

    detected = sorted(detected, key=lambda a: a[0], reverse=True)

    return detected


def get_func_ann(func_dict, func_id):
    if func_id not in func_dict:
        return "n"
    func = func_dict[func_id]
    func_args_defaults = func.__defaults__
    func_args_name = func.__code__.co_varnames[:func.__code__.co_argcount]

    if not len(func_args_name):
        return None

    source_code = inspect.getsource(func)
    if '"""' not in source_code:
        return "r"

    source_code = source_code[source_code.find('"""') + 3:]
    source_code = source_code[:source_code.find('"""')]
    source_code = source_code.replace(":param ", "")
    arg_items = source_code.split("\n")

    arguments = []
    i = 0
    for args in arg_items:
        args = args.strip()

        if ":return:" in args:
            continue

        if not args:
            continue
        k, v = args.split(": ")

        v = v.strip()
        t = None
        if "[" in v:
            [v, v_info] = v.split("[")
            [t, r_info] = v_info.split("]")
            r_info = r_info.strip()
            r_info = r_info.replace("{", "").replace("}", "")
            [min_, max_] = r_info.split(":")
        d = ""
        if i < len(func_args_defaults):
            d = func_args_defaults[i]

        if t:
            arguments.append((k, v, d, t, min_, max_))
        else:
            arguments.append((k, v, d))
        i += 1

    if not len(arguments):
        return "e"

    return arguments


def get_func_items(func):
    source_code = inspect.getsource(func)
    stem_part = source_code[source_code.find("stem ="):source_code.find("answer =")]
    answer_part = source_code[source_code.find("answer ="):]
    answer_part = answer_part[:answer_part.find("\n")]
    comment_part = source_code[source_code.find("comment ="):]
    comment_part = comment_part[:comment_part.find("\n\n")]

    stem = stem_part.replace("stem = ", "").replace('\"', "").replace("\'", "").replace("\\n", "")
    answer = answer_part.replace("answer = ", "").replace('\""', "").replace("\'", "")
    comment = comment_part.replace("comment = ", "").replace('\"', "").replace("\'", "").replace("\\n", "")

    stem = stem.replace("\\", "").replace("  ", "")
    answer = answer.replace("\\", "")
    comment = comment.replace("\\", "").replace("\n", "").replace("  ", "")

    return stem, answer, comment


def filter_items(strings):
    for item in re.findall("\$\$/?[ㄱ-힇]+\$\$", strings):
        strings = strings.replace(item, "")

    return strings


def select_stem(stem):
    flag2 = False
    if SELECT_NUMS1[0] not in stem:
        if SELECT_NUMS2[0] not in stem:
            return False
        flag2 = True

    if flag2:
        [just_stem, selects] = stem.split(SELECT_NUMS2[0])
        [select1, selects] = selects.split(SELECT_NUMS2[1])
        [select2, selects] = selects.split(SELECT_NUMS2[2])
        [select3, selects] = selects.split(SELECT_NUMS2[3])
        [select4, select5] = selects.split(SELECT_NUMS2[4])
    else:
        [just_stem, selects] = stem.split(SELECT_NUMS1[0])
        [select1, selects] = selects.split(SELECT_NUMS1[1])
        [select2, selects] = selects.split(SELECT_NUMS1[2])
        [select3, selects] = selects.split(SELECT_NUMS1[3])
        [select4, select5] = selects.split(SELECT_NUMS1[4])

    select_dict = [
        {"1": select1.strip()},
        {"2": select2.strip()},
        {"3": select3.strip()},
        {"4": select4.strip()},
        {"5": select5.strip()}

    ]

    return [just_stem, select_dict]


def detect_category(item, stem_dict, unit_dict):
    try:
        try:
            c1 = item["etc_category1"]
            #print("C1", c1)
            if "중학교" in c1:
                category = stem_dict["Middle"]
                c_idx = c1[c1.find("학년")-1]
                category = category[c_idx]
            else:
                category = stem_dict["Elementary"]
                c_idx = c1[c1.find("학년") - 1]
                category = category[c_idx]
            c2 = item["etc_category2"]
            if c2 == "방정식":
                c2 += str(c_idx)
            c2 = unit_dict[c2]

            for c_item in category.items():
                if c2 in c_item[1].keys():
                    category = c_item[1][c2]
                    break
            
        except Exception:
            if "일차부등식과 연립일차방정식" == item["category1"]:
                category = stem_dict["Middle"]
                c_idx = '2'
                category = category[c_idx]

                if "연립일차방정식" in item["category2"]:
                    c2 = unit_dict["방정식2"]
                    for c_item in category.items():
                        if c2 in c_item[1].keys():
                            category = c_item[1][c2]
                            break

        try:
            #c_unit = item["category2"]
            c_unit = item["etc_category2"]
            c3 = unit_dict[c_unit]
            c3_token = c3
        except Exception:
            c_unit = item["etc_category2"]
            c3 = unit_dict[c_unit]
            c3_token = c3
        if "Basic" in c3 or "Practical" in c3 or "Solving" in c3:
            if "LinearEquation" in c2 and "Sys" not in c2:
                c3_token = "LinEqu" + c3[c3.rfind("_")+1:]
            elif "LinearInequality" in c2:
                if "Practical" in c3:
                    c3_token = "LinIneq" + c3[c3.rfind("_")+1:]
                else:
                    c3_token = "LinearIne" + c3[c3.rfind("_")+1:]
            else:
                c3_token = "SysLinEqu" + c3[c3.rfind("_") + 1:]

        for c_item in category.items():
            if c3_token in c_item[1].keys():
                category = c_item[1][c3_token]
                break

        c_sub_unit = item["etc_category3"]
        category = category[c_sub_unit]
        try:
            c_sub_sub_unit = item["etc_category4"]
            category = category[c_sub_sub_unit]
        except KeyError:
            category = category["all"]

        return [c3, category, c_idx, c_unit]
    except Exception:
        # print(c_sub_unit)
        return ["e", "r", "r", "r"]

def detect_category_jp(item, stem_dict, unit_dict):
    try:
        try:
            c1 = item["etc_category1"]
            if "중학교" in c1:
                category = stem_dict["Middle"]
                c_idx = c1[c1.find("학년")-1]
                category = category[c_idx]
            else:
                category = stem_dict["Elementary"]
                c_idx = c1[c1.find("학년") - 1]
                category = category[c_idx]
            c2 = item["etc_category2"]
            if c2 == "방정식":
                c2 += str(c_idx)
            c2 = unit_dict[c2]

            for c_item in category.items():
                if c2 in c_item[1].keys():
                    category = c_item[1][c2]
                    break

        except Exception:
            if "일차부등식과 연립일차방정식" == item["category1"]:
                category = stem_dict["Middle"]
                c_idx = '2'
                category = category[c_idx]

                if "연립일차방정식" in item["category2"]:
                    c2 = unit_dict["방정식2"]
                    for c_item in category.items():
                        if c2 in c_item[1].keys():
                            category = c_item[1][c2]
                            break

        try:
            c_unit = item["category2"]
            c3 = unit_dict[c_unit]
            c3_token = c3
        except Exception:
            c_unit = item["etc_category2"]
            c3 = unit_dict[c_unit]
            c3_token = c3
        if "Basic" in c3 or "Practical" in c3 or "Solving" in c3:
            if "LinearEquation" in c2 and "Sys" not in c2:
                c3_token = "LinEqu" + c3[c3.rfind("_")+1:]
            elif "LinearInequality" in c2:
                if "Practical" in c3:
                    c3_token = "LinIneq" + c3[c3.rfind("_")+1:]
                else:
                    c3_token = "LinearIne" + c3[c3.rfind("_")+1:]
            else:
                c3_token = "SysLinEqu" + c3[c3.rfind("_") + 1:]

        for c_item in category.items():
            if c3_token in c_item[1].keys():
                category = c_item[1][c3_token]
                break

        c_sub_unit = item["category3"]
        category = category[c_sub_unit]

        try:
            c_sub_sub_unit = item["category4"]
            category = category[c_sub_sub_unit]
        except KeyError:
            category = category["all"]

        return [c3, category, c_idx, c_unit]
    except Exception:
        # print(c_sub_unit)
        return ["e", "r", "r", "r"]

def detect_stem(vocab, stem):
    detected = []

    for item in vocab.items():
        score = stem_mapping(stem, item[1])
        # if score:
        detected.append((score, item[0], item[1][0]))

    detected = sorted(detected, key=lambda a: a[0], reverse=True)

    return detected

# 기탄문항 id값 추출
def detect_gt_item_id(item):
    
    item_id = "GT_" + str(item["category1"]) + str(item["category2"])+"_"+ str(item["category5"])
    
    return item_id

#if __name__ == '__main__':
    # metas = load_xlsx("samples/i_scream_sample.xlsx")
    # stem_dict = load_target("samples/Stem_dict.txt")
    #
    # sample1 = load_hml("samples/sample1.txt")
    # sample2 = load_hml("samples/sample2.txt")
    # sample3 = load_hml("samples/sample3.txt")
    #
    # print("입력 문항 : " + sample1[0])
    # detected = mapping_meta(metas[1], sample1, stem_dict)
    # print(detected[0])
    # print("=" * 100)
    #
    # print("입력 문항 : " + sample2[0])
    # detected = mapping_meta(metas[1], sample2, stem_dict)
    # print(detected[0])
    # print("=" * 100)
    #
    # print("입력 문항 : " + sample3[0])
    # detected = mapping_meta(metas[1], sample3, stem_dict)
    # print(detected[0])
    # print("=" * 100)

    #print(get_func_ann.__code__.co_varnames)
