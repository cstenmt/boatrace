# -*- coding: utf-8 -*-

import re
import os

#csvへの変換を行う
def getmeta(f, f2) :
	
	a = ""
	b = ""
	c = ""
	
	for l in f :
		
		
		if re.search(r"番組表",l):
			
			f.readline()
			#レース名
			a = f.readline()
			f.readline()
			#日にち、日付、開催地
			b = f.readline()
			
			d = a[:-1].strip() + "," + b[3:7] + "," + b[17:28] + "," + b[51:58].strip() + ","
			
		if re.search(r"Ｒ",l) and re.search(r"Ｈ",l)  :
				#ラウンド、種別
				a = l[1:3] + "," + l[5:8] + "," 
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				c = f.readline()
				
				#番組表取得
				while c != "\n":
					
					if re.search(r"BEND",c):
						
						break
					
					e = c[0] + "," + c[2:6] + "," + c[6:10] + "," + c[10:12] + "," + c[12:14] + "," + c[14:16] + "," + c[16:18] + "," + c[19:23] + "," + c[24:29] + "," + c[30:34] + "," + c[36:40] + "," + c[41:43] + "," + c[44:49] + "," + c[50:52] + "," + c[53:58] + "," + c[59:61] + "," + c[61:63] + "," + c[63:65] + "," + c[65:67] + "," + c[67:69] + "," + c[69:71] + "," + c[71:73]
					c = f.readline()
					f2.write(d + a + e + "\n")
				
				
					
file_list = os.listdir('timetable_txt')
m = ""
filename = ""
head = "レース名,日にち,日付,開催地,ラウンド名,種別,艇番,選手登番,選手名,年例,出身,体級,重別,全国勝率,2率,当地勝率,2率,モーターNo,2率,ボートNo,2率,今節成績1,2,3,4,5,6,早見\n"

i = 0

#7ファイルずつまとめて変換を行う
for m in file_list:			
	
	f = open("timetable_txt/" + m,"r")
	if i % 7 == 0 :
		filename = m.split(".")[0] + ".csv"
		
		f2 = open("timetable_csv/" + filename,"w")
		f2.write(head)
	
	#csv変換
	getmeta(f,f2)
	
	if i % 7 == 6:
		
		f2.close()
		print(filename + "を生成しました")
	f.close()
	i += 1
	
if i % (7 - 1) != 6:
	
	f2.close()
	print(filename + "を生成しました")
	