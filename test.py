from bs4 import BeautifulSoup
from selenium import webdriver
import time

chrome_path = "C:/Users/NUTC/Desktop/music-mood-classifier-master/chrome/chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get('http://www.yahoo.com.tw')
# web.set_window_position(0,0) #瀏覽器位置
# web.set_window_size(700,700) #瀏覽器大小


# web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
# time.sleep(5)

# web.close()
		# 不重複的網頁
# https://www.youtube.com/watch?v=

# import mpv
# player = mpv.MPV(ytdl=True)
# player.play('https://youtu.be/DOmdB7D-pUU')

# import time
# words = ""
# for item in words.split():
#     print('\n'.join([''.join([(item[(x-y) % len(item)] 
#     if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') 
#     for x in range(-30, 30)]) 
#     for y in range(12, -12, -1)]))
#     time.sleep(1.5);
	
	# word = jieba.cut(user_content[count].text.strip(),cut_all=False)
	
	# cut_word.append("/".join(word).strip());
	# print(cut_word);
	#去頭去尾換行之類的字符
	# print ("/".join(word))#結疤段詞	
	# print(user_tag[count].text)
	
	# print("==========================================================================")




 
# print ('word_len{%d}' % len(list(cut_word)))
# jieba_extract=[]
# for cut_word in cut_word:
# 	keywords = jieba.analyse.extract_tags(cut_word, topK=20, withWeight=True, allowPOS=())
# 	# 访问提取结果
# 	for item in keywords:
# 	    # 分别为关键词和相应的权重
# 	    print (item[0],item[1])
# 	    jieba_extract.append(item[0])
# 	    print("====================")
	    
	    # print('keyword{%d}'%len(list(keywords)))
		
	 
	# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
	# 即仅提取地名、名词、动名词、动词
	# keywords = jieba.analyse.textrank(cut_word, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
	# # 访问提取结果
	# for item in keywords:
	#     # 分别为关键词和相应的权重
	#     print (item[0], item[1]);
	    
	#     print("1==================="+cut_word)
	#     # print('1keyword{%d}'%len(list(keywords)))

				
# from sklearn.feature_extraction import DictVectorizer #用於轉換 dict 為 sklearn estimators 可用的向量
# from sklearn.feature_extraction.text import TfidfTransformer #將矩陣轉換為 TF 或 TF-IDF 表示
# from collections import defaultdict #使用 dict 儲存資料


# 				# convert to vectors
# c_dvec = DictVectorizer()
# c_tfidf = TfidfTransformer()
# c_vector = c_dvec.fit_transform(jieba_extract)
# c_X = c_tfidf.fit_transform(c_vector) #將一千篇所有鄉民留言的斷詞文字矩陣轉成向量並計算tf-idf
#分類留言的情緒
 # get pushes

# build and train the classifier