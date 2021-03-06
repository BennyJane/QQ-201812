import re
import datetime
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS
import seaborn as sns
from PIL import Image
import numpy as np

#Days WeekDays的表格，两者都会使用聊天信息里边时间的一部分

def get_date(data):
    dates = re.findall(r'\d{4}-\d{2}-\d{2}',data)
    days = [date[-2:] for date in dates]
    plt.subplot(221)#最后的显示为四部分，Days占第一部分
    sns.countplot(days)#days就是数据集，countplot统计days每一天的重复数量就是每一天聊天数目
    plt.title('Days')

    #isocalendar()ISO标准化日期，返回三个值的元组（年份、星期天week number，星期几weekday） 星期一为1，星期天为7
    weekdays = [datetime.date(int(date[:4]),int(date[5:7]),int(date[-2:])).isocalendar()[-1] for date in dates]
#    for date in dates:
#        weekdays = [datetime.date(int(date[0:4]), int(date[5:7]), int(date[-2:])).isocalendar()[-1]]

    plt.subplot(222)
    sns.countplot(weekdays)
    plt.title('WeekDays')

#一天24小时的分布图
def get_time(date):
    times = re.findall(r'\d+:\d{2}:\d{2}',date)
    hours = [time.split(":")[0] for time in times] #对每一个time分割出代表小时的那部分

    plt.subplot(223)
    #因为qq消息导出格式里，小时0—9是以个位形式出现，所以用个位的来对应
    sns.countplot(hours,order=['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','0','1','2','3','4','5','6'])
    plt.title("Hours")

#词云的制作
def get_wordcloud(text_date):
    word_list = ["".join(jieba.cut(sententce)) for sententce in text_date]
    new_text = ''.join(word_list)
    #背景图片的设置
    pic = Iamge.open(123.jpg)
    mang_mask = np.array(pic)

    plt.subplot(224)    #数字是什么意思？
    wordcloud = WordCloud(
        background_color="white",
        font_path = '/homt/shen/Downloads/fonts/msyh.ttc',
        mask = mang_mask,
        stopwords = STOPWORDS,).generate(new_text)
    plt.imshow(wordcloud)
    plt.axis('off')

#匹配文本内容，调用上一个函数
def get_content(date):
    pa = re.compile(r'd{4}-\d{2}-\d{2}.*?\d+:\d{2}:\d{2}.*?\n(.*?)\n\n',re.DOTALL)
    content = re.findall(pa,data)
    get_wordcloud(content)

#调用主函数
def main():
    filename = "228.txt"
    with open(filename, encoding="UTF-8") as f:
            data = f.read()
    get_date(data)
    get_time(data)
