import codecs
import re


"""
2019.07.28 SW

타겟데이터(Stem 사전:txt 형태)에 대한 로딩 및 정리

format : 중등\t1\t1\tPF\t1\tPF\t넘버\t"문항"\n

"""


def load_target(filename):
    stem_dict = {}
    targets = []
    with codecs.open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not len(line.split('"')) > 1:
                continue

            stem = line.split('"')[1]
            items = line.split('"')[0].strip().split("#")
            #print("ITEMS", items)
            targets.append(items)
            stem = stem_parsing(stem)
            if items[5] not in stem_dict:
                stem_dict[items[5]] = {items[8]: stem}
            else:
                stem_dict[items[5]][items[8]] = stem

    target_dict = {}
    for target in targets:
        if target[0] not in target_dict:
            target_dict[target[0]] = {}

        if target[1] not in target_dict[target[0]]:
            target_dict[target[0]][target[1]] = {}

        if target[2] not in target_dict[target[0]][target[1]]:
            target_dict[target[0]][target[1]][target[2]] = {}

        if target[3] not in target_dict[target[0]][target[1]][target[2]]:
            target_dict[target[0]][target[1]][target[2]][target[3]] = {}

        if target[4] not in target_dict[target[0]][target[1]][target[2]][target[3]]:
            target_dict[target[0]][target[1]][target[2]][target[3]][target[4]] = {}

        if target[5] not in target_dict[target[0]][target[1]][target[2]][target[3]][target[4]]:
            target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]] = {}

        if target[6] not in target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]]:
            target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]] = {}

        if target[7] not in target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]]:
            target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]] = {}

        if "all" not in target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]]:
            target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]]["all"] = {}

        target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]][target[7]][target[8]] = \
            stem_dict[target[5]][target[8]]

        target_dict[target[0]][target[1]][target[2]][target[3]][target[4]][target[5]][target[6]]["all"][target[8]] = \
            stem_dict[target[5]][target[8]]


    return target_dict


def stem_parsing(stem):
    for item in re.findall("{[a-zA-Z]+?[_]+?[a-zA-Z]+?[0-9+]?}", stem):
        stem = stem.replace(item, " $$TOKEN$$ ")
    for item in re.findall("{[a-zA-Z]?[0-9+]?}", stem):
        stem = stem.replace(item, " $$TOKEN$$ ")

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

    return stem, bi_gram, tri_gram, quad_gram


def load_unit(filename):
    d = {}
    with codecs.open(filename, encoding='utf-8') as f:
        for line in f:
            items = line.strip().split("\t")
            #print("U_ITEM", items)
            d[items[1]] = items[0]

    return d


def stem_update(filename_vocab, filename_new):
    vocabs = {}
    with codecs.open(filename_new, encoding="utf-8") as f:
        for line in f:
            items = line.strip().split(",")
            if len(items) > 5:
                vocabs[items[5]] = items[-2:]

    with codecs.open(filename_vocab + ".txt", encoding="utf-8") as f:
        with codecs.open(filename_vocab + "3.txt", "w", encoding="utf-8") as w:
            for line in f:
                items = line.strip().split("\t")
                if len(items) > 3:
                    stem_id = "%s_%s" % (items[5], items[7])
                    if stem_id in vocabs:
                        new_info = vocabs[stem_id]
                        w.write("%s\t%s\t%s\n" % ("\t".join(items[:6]), "\t".join(new_info), "\t".join(items[7:])))
                    else:
                        w.write("%s\t%s\t%s\n" % ("\t".join(items[:6]), "_\t_", "\t".join(items[7:])))


if __name__ == '__main__':
    target = load_target("/Users/namang/PycharmProjects/I_scream_unittest/Dictionary/stem_vocab.txt")
    #print(target)
