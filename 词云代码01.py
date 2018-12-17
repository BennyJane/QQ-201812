#网络代码
import jieba
from os import path  #用来获取文档的路径

#词云
from PIL import Image
import numpy as  np
import matplotlib.pyplot as plt
#词云生成工具
from wordcloud import WordCloud,ImageColorGenerator
#需要对中文进行处理
import matplotlib.font_manager as fm

#背景图
bg=np.array(Image.open("man.jpg"))

#获取当前的项目文件加的路径
d=path.dirname(__file__) 
#读取停用词表
stopwords_path='stopwords.txt'
#添加需要自定以的分词
jieba.add_word("侯亮平")
jieba.add_word("沙瑞金")
jieba.add_word("赵东来")

#读取要分析的文本
text_path="人民的名义.txt"
#读取要分析的文本，读取格式
text=open(path.join(d,text_path),encoding="utf8").read()
#定义个函数式用于分词
def jiebaclearText(text):
    #定义一个空的列表，将去除的停用词的分词保存
    mywordList=[]
    #进行分词
    seg_list=jieba.cut(text,cut_all=False)
    #将一个generator的内容用/连接
    listStr='/'.join(seg_list)
    #打开停用词表
    f_stop=open(stopwords_path,encoding="utf8")
    #读取
    try:
        f_stop_text=f_stop.read()
    finally:
        f_stop.close()#关闭资源
    #将停用词格式化，用\n分开，返回一个列表
    f_stop_seg_list=f_stop_text.split("\n")
    #对默认模式分词的进行遍历，去除停用词
    for myword in listStr.split('/'):
        #去除停用词
        if not(myword.split()) in f_stop_seg_list and len(myword.strip())>1:
            mywordList.append(myword)
    return ' '.join(mywordList)
text1=jiebaclearText(text)
#生成
wc=WordCloud(
    background_color="white", 
    max_words=200,
    mask=bg,            #设置图片的背景
    max_font_size=60,
    random_state=42,
    font_path='C:/Windows/Fonts/simkai.ttf'   #中文处理，用系统自带的字体
    ).generate(text1)
#为图片设置字体
my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
#产生背景图片，基于彩色图像的颜色生成器
image_colors=ImageColorGenerator(bg)
#开始画图
plt.imshow(wc.recolor(color_func=image_colors))
#为云图去掉坐标轴
plt.axis("off")
#画云图，显示
plt.figure()
#为背景图去掉坐标轴
plt.axis("off")
plt.imshow(bg,cmap=plt.cm.gray)

#保存云图
wc.to_file("man.png")
-------------------

1.简介
   本文是在基于python的词云生成（一）的基础上，进一步对云词进行编写，本文还使用了jieba分词对中文进行分词处理，以做出更好的效果。 
   jieba分词包（https://pypi.python.org/pypi/jieba/）：在自然语言处理过程中，为了能更好地处理句子，往往需要把句子拆开分成一个一个的词语，这样能更好的分析句子的特性，这个过程叫做——分词，jieba 是一个python实现的分词库，对中文有着很强大的分词能力。 
   支持三种分词模式： 
   a. 精确模式，试图将句子最精确地切开，适合文本分析； 
   b. 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义； 
   c. 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。 
   并且还支持自定义词典。

2.本文目标
   使用jieba分词包对一篇中文小说进行分词，并把分词的结果用词云的方式进行统计形成一个根据词语出现频率的不同生成词云的关键字大小不同的图片，并且对词云图片设置背景图。为了使分词效果更好，这里还把文章中的停用词去掉以达到更好的效果。


