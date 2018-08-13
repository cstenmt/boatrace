# -*- coding: utf-8 -*-
import requests
import time
#変数初期化
baseurl = "http://www1.mbrace.or.jp/od2/B/"
url = ""
file_name = ""
year = 0
mon = 0
first = ""
second = ""
day = 0

#20XXのXの部分を入れる　例：2002 -2017なら2と18
for year in range(2,18):
	print()
	for mon in range(1,13):
			
		for day in range(1,32):	
		
			time.sleep(1)
			first = "20" + '{0:02d}'.format(year) + '{0:02d}'.format(mon)
			second = "/b" + '{0:02d}'.format(year)  + '{0:02d}'.format(mon) + '{0:02d}'.format(day)
			#リンク作成
			url = baseurl + first + second +  ".lzh"
			file_name = url.split("/")[-1] 
			
			r = requests.get(url)
			
			#成功したら、書き込み
			if r is not None:
				
				
				
				if r.status_code == 200:
					f = open("timetable_lzh/" + file_name,'wb')
					f.write(r.content)
					f.close()
					print( url+ "を取得しました")
			else :
				print(file_name + "がダウンロードできませんでした")
	
			
			