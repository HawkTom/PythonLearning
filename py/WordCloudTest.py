from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import jieba

with open("cloud.txt",'r',encoding='gbk') as f:
    data = f.read()

wordlist = jieba.cut(data,cut_all=False)
wl_space_word = ' '.join(wordlist)
# print(wl_space_word)

image = numpy.array(Image.open('21.png'))
# # stopwords = set(STOPWORDS)
# # stopwords.add()
font = r"C:\Windows\Fonts\STXINGKA.TTF"
wc = WordCloud(background_color="White", font_path=font,
               max_words=2000,  mask= image,
                max_font_size=75, random_state=42,            # 设置有多少种随机生成状态，即有多少种配色方案
                scale=1.5, width=1960, height=1080)

wc.generate(wl_space_word)



image_colors = ImageColorGenerator(image)
plt.figure('asdg')
plt.imshow(wc.recolor(color_func=image_colors),interpolation='bilinear')
# plt.title('Alice')
plt.axis("off")
plt.show()

