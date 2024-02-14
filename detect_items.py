from Detect_utils.io_utils import *
from Detect_utils.meta_utils import *
from Detect_utils.stem_utils import *
from Detect_utils.detect import *

from stem_directory import FUNC_DICT

def load_detector():
    filename_stem = "Dictionary/stem_vocab.txt"
    filename_unit = "Dictionary/unit_vocab.txt"

    stem_dict = load_target(filename_stem)
    unit_dict = load_unit(filename_unit)
    
    return stem_dict, unit_dict


def detect(unit_dict, stem_dict, inputjson):
    # 입력 형태가 내가 호출해서 받아오는 형태로 구성했는데, 아마 실제 API 연결에서는 다를 테니 그에 맞게 수정해주시면 됩니다.
    # 해당 변경 사항에 맞게, 해당 메소드의 min_id, max_id 등 변수를 고쳐주시면 더 깔끔할듯
    # items = load_data(solo_id, min_id=min_id, max_id=max_id)
    items = inputjson

    '''여기서부터는 아마도 변경사항 없음'''

    # 호출된 json이 다수일 것으로 판단하여, 분리 메소드 구성
    item = split_data(items)

    err = 0

    e = ""
    
    # 단원 기준 매핑

    # 초등
    if items['chapter_code'].startswith('CC'):
        [category_name, category_vocab, grade, c_unit] = detect_category(item, stem_dict, unit_dict)
        func_dict = FUNC_DICT
    
    '''단원 기준 매핑에 실패할 경우, 에러처리 필요 (간이 형식으로 했으므로, 추가바람)'''
    if category_vocab == "r":
        err += 1
        e = "CATEGORY MAPPING ERR : %s" % item["id"]
        print(e)
        return mapping_detect_json([], [], [], "", e=e), e

    # stem 파싱
    body = get_grams(item["body_html"])


    # stem을 활용한 문항 탐지
    detected = detect_stem(category_vocab, body)
    if not detected:
        err += 1
        e = "DETECT ERR : %s" % item["id"]
        print(e)
        return mapping_detect_json([], [], [], "", e=e), e
    

    # 탐지 결과 도출된 적합 모델 id 구성
    detected_item = detected[0]
    detected_id = detected_item[1]
    item_id = "%s_%s" % (category_name, detected_id)
    num_id = int(detected_id[detected_id.rfind("_") + 1:])
    
    # 함수 호출
    func = func_dict[item_id]

    # 함수의 주석 호출 (argument 값)
    arguments = get_func_ann(func_dict, item_id)
    # 함수의 stem, answer, comment 추출
    strings = list(get_func_items(func))
    
    # 선다형 여부 판단
    selects = select_stem(strings[0])
    item_infos = [int(grade), category_name, c_unit, num_id]
    
    # 선다형일 경우
    if selects:
        [stem, selects] = selects
        strings[0] = stem
        answer_id = strings[1][strings[1].find("{") + 1: strings[1].find("}")]
        result = mapping_detect_json(item_infos, strings, arguments, answer_id, selects, e)

    # 아닐 경우
    else:
        answer_id = strings[1][strings[1].find("{") + 1: strings[1].find("}")]
        result = mapping_detect_json(item_infos, strings, arguments, answer_id, e=e)
    
    return result, e


if __name__ == '__main__':
    # 미리 사전 로딩해야 하는 거 아시쥬?
    stem_dict, unit_dict = load_detector()
    
    # 탐지
    results, e = detect(unit_dict, stem_dict,  77130)
    # results, e = detect(unit_dict, stem_dict, inputjson)

    #for result in results:
    #    print(result)
