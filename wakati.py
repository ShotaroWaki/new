from janome.tokenizer import Tokenizer
import pandas as pd
#import model.py
import MeCab
import os

word_model_df = pd.DataFrame()


t = Tokenizer(wakati=True)

# 取り出したい品詞
select_conditions = ['動詞', '形容詞', '名詞']

# 分かち書きオブジェクト
tagger = MeCab.Tagger('')

# Neologdの指定版 最新語に対応する
# tagger = MeCab.Tagger('-d /usr/lib64/mecab/dic/mecab-ipadic-neologd')

# 安定するらしい
tagger.parse('')


def wakati_text(text):

    # 分けてノードごとにする
    node = tagger.parseToNode(text)
    terms = []

    while node:

        # 単語
        term = node.surface

        # 品詞
        pos = node.feature.split(',')[0]

        # もし品詞が条件と一致してたら
        if pos in select_conditions:
            terms.append(term)

        node = node.next

    # 連結おじさん
    text_result = ' '.join(terms)
    return text_result
