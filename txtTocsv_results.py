# -*- coding: utf-8 -*-

import re
import os

#csvへの変換を行う
def getmeta(f, f2) :
	
	a = ""
	b = ""
	c = ""
	
	for l in f :
		
		
		if re.search(r"競走成績",l):
			
			f.readline()
			a = f.readline()
			f.readline()
			b = f.readline()
			#レース名など
			d = a[:-1].strip() + "," + b[3:7] + "," + b[17:27] + "," + b[56:63] + ","
		
		if re.search(r"R",l) and re.search(r"H",l) :
				#ラウンドなど
				a = l[3:5] + "," + l[12:15] + "," 
				f.readline()
				f.readline()
				c = f.readline()
				
				#レース結果取得
				while c != "\n":
					
					e = c[2:4] + "," + c[6] + "," + c[8:12] + "," + c[13:20] + "," + c[22:24] + "," + c[27:29] + "," + c[31:36] + "," + c[38] + "," + c[43:47] + "," + c[52:58]
					c = f.readline()
					f2.write(d + a + e + "\n")
				
				
					
file_list = os.listdir('result_txt')
m = ""
filename = ""
head = "レース名,日にち,日付,開催地,ラウンド名,種別,着,艇,登番,選手名,ﾓｰﾀｰ,ﾎﾞｰﾄ,展示,進入,ｽﾀｰﾄﾀｲﾐﾝｸ,ﾚｰｽﾀｲﾑ\n"
i = 0

#7ファイルずつまとめて変換を行う
for m in file_list:			
	
	f = open("result_txt/" + m,"r")
	if i % 7 == 0 :
		filename = m.split(".")[0] + ".csv"
		
		f2 = open("result_csv/" + filename,"w")
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
	