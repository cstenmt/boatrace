import lhafile
import os
import re
#https://trac.neotitans.net/wiki/lhafile/

#ディレクトリ内のファイル名一覧
file_list = os.listdir('result_lzh')
m = ""
f = ""
out = ""
name = ""
for m in file_list :
  #拡張子がlzhなら
  if re.search(".lzh",m):
   #解凍する
   f = lhafile.Lhafile("result_lzh/" + m)
   #解凍されたファイルの名前取得
   info = f.infolist()
   name = info[0].filename
   #書き込む
   out = open("result_txt/" + name,"wb").write(f.read(name))
   print(name + "を作成しました")
