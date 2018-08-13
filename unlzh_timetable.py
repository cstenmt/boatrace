import lhafile
import os
import re
#https://trac.neotitans.net/wiki/lhafile/

#ディレクトリ内のファイル名一覧
file_list = os.listdir('timetable_lzh')
m = ""
f = ""
out = ""
name = ""
for m in file_list :
  #拡張子がlzhなら
  if re.search(".lzh",m):
   #解凍する
   f = lhafile.Lhafile("timetable_lzh/" + m)
   info = f.infolist()
   name = info[0].filename
   out = open("timetable_txt/" + name,"wb").write(f.read(name))
   print(name + "を作成しました")
