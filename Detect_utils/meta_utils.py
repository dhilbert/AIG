import pandas as pd


"""
2019.07.28 SW

메타데이터(입력데이터:csv형태)에 대한 로딩/필터링

* 메타데이터에 대한 스키마/입력데이터 형태에 대한 메타 정리가 필요함

"""


def load_csv(filename):
    inputs = []
    dataframe = pd.read_csv(filename)
    for i in range(len(dataframe)):
        data = dataframe[i:i+1]
        meta = {}
        for k in dataframe:
            m = str(data[k])
            m = " ".join(m.split("\n")[0].split()[1:])
            meta[k] = m
        inputs.append(meta)
    return inputs


def load_xlsx(filename):
    inputs = []
    dataframe = pd.read_excel(filename)
    for i in range(len(dataframe)):
        data = dataframe[i:i+1]
        meta = {}
        for k in dataframe:
            m = str(data[k])
            m = " ".join(m.split("\n")[0].split()[1:])
            meta[k] = m
        inputs.append(meta)
    return inputs


def get_grams(stem):
    stem = stem.replace("를", "을")
    stem = stem.replace("가", "이")
    stem = stem.replace("는", "은")

    stem_sentences = stem.split("\\n")
    bi_gram = []
    tri_gram = []
    quad_gram = []
    
    for stem_sentence in stem_sentences:
        stem_tokens = stem_sentence.split()
        bi_gram += list(zip(*[stem_tokens[i:] for i in range(2)]))
        tri_gram += list(zip(*[stem_tokens[i:] for i in range(3)]))
        quad_gram += list(zip(*[stem_tokens[i:] for i in range(4)]))

    return stem, bi_gram,  tri_gram#, quad_gram


if __name__ == '__main__':
    # a= load_csv("/Users/namang/PycharmProjects/AIG_Detectior/samples/services.csv")
    a = load_xlsx("/Users/namang/PycharmProjects/AIG_Detectior/samples/i_scream_sample.xlsx")
    # b, bgram, tgram, qgram = load_hml("/Users/namang/PycharmProjects/AIG_Detectior/samples/sample1.txt")
