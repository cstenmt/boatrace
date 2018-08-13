# -*- coding: utf-8 -*-
import requests
import time
#変数初期化
#http://www1.mbrace.or.jp/od2/K/201611/k161130.lzh
baseurl = "http://www1.mbrace.or.jp/od2/K/"
url = ""
file_name = ""
year = 0
mon = 0
first = ""
second = ""
day = 0

#20XXのXの部分を入れる　例：2002 -2017なら2と18
for year in range(2,18):
	
	for mon in range(1,13):
			
		for day in range(1,32):	
		
			time.sleep(0.5)
			#リンク作成
			first = "20" + '{0:02d}'.format(year) + '{0:02d}'.format(mon)
			second = "/k" + '{0:02d}'.format(year)  + '{0:02d}'.format(mon) + '{0:02d}'.format(day)
			
			url = baseurl + first + second +  ".lzh"
			file_name = url.split("/")[-1] 
			print(url)
			r = requests.get(url)
			
			if r is not None:
				
				
				#成功したら、書き込み
				if r.status_code == 200:
					f = open("result_lzh/" + file_name,'wb')
					f.write(r.content)
					f.close()
				else :
					print(file_name + "がダウンロードできませんでした")
		
			
			