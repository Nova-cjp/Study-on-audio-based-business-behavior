# -*- coding: utf-8 -*-

import os
from sentiment_analysis_dict.utils import ToolGeneral


pwd = os.path.dirname(os.path.abspath(__file__))
tool = ToolGeneral()    


class Hyperparams:
    '''Hyper parameters 超参数'''
    # 加载情感词典
    deny_word = tool.load_dict(os.path.join(pwd,'dict','not.txt'))#否定词
    # posdict = tool.load_dict(os.path.join(pwd,'dict','positive.txt'))#正面情感词
    # negdict = tool.load_dict(os.path.join(pwd,'dict', 'negative.txt'))#负面情感词
    posdict = tool.load_dict(os.path.join(pwd,'dict','output_positive.txt'))#正面情感词
    negdict = tool.load_dict(os.path.join(pwd,'dict', 'output_negative.txt'))#负面情感词
    pos_neg_dict = posdict|negdict
    # 加载程度副词词典
    mostdict = tool.load_dict(os.path.join(pwd,'dict','most.txt'))
    verydict = tool.load_dict(os.path.join(pwd,'dict','very.txt'))
    moredict = tool.load_dict(os.path.join(pwd,'dict','more.txt'))
    ishdict = tool.load_dict(os.path.join(pwd,'dict','ish.txt'))#大概/…左右/差不多 的词性
    insufficientlydict = tool.load_dict(os.path.join(pwd,'dict','insufficiently.txt'))
    overdict = tool.load_dict(os.path.join(pwd,'dict','over.txt'))
    inversedict = tool.load_dict(os.path.join(pwd,'dict','inverse.txt'))




