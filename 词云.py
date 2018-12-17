# coding=utf-8
import re
import datetime
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
from PIL import Image
import numpy as np


# 词云的制作
def get_wordcloud(text_date):
    word_list = ["".join(jieba.cut(sententce)) for sententce in text_date]
    new_text = ''.join(word_list)
    # 背景图片的设置
#    pic = Image.open("12.jpg")
#    mang_mask = np.array(pic)
#可以不要背景图
    plt.subplot(224)  # 数字是什么意思？
    wordcloud = WordCloud(
        background_color="white",
        width=2000,
        height = 860,
        scale = 0.4,
        font_path='C:\\Windows\\Fonts\\STFANGSO.ttf',
#        mask=mang_mask,
        stopwords=["表情","图片"], ).generate(new_text)
        #删除不要显示的文字

    plt.imshow(wordcloud)
    wordcloud.to_file('F:/简历准备/优复数学/数据分析/56.jpg')
    plt.axis('off')


# 匹配文本内容，调用上一个函数
def get_content(data):
    pa = re.compile(r'\d{4}-\d{2}-\d{2}.*?\d+:\d{2}:\d{2}.*?\n(.*?)\n\n', re.DOTALL)
    content = re.findall(pa, data)
    get_wordcloud(content)

# 调用主函数
def main():
    filename = "F:/简历准备/优复数学/数据分析/优复01.txt"
    with open(filename, encoding="UTF-8") as f:
        data = f.read()
    get_content(data)
    plt.show()


if __name__ == '__main__':
    main()
