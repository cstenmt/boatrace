作成日 2018/1/4 

■環境
python version :3.5
os : windows


■事前準備
スクリプトを実行する前に、lhafileというモジュールをインストールして頂く必要があります。
カレントディレクトリを　python-lhafile-0.2.1　にしてから、

py setup.py build
py setup.py install

を実行してください。
設定によっては、py　は python　かもしれないです。

■ファイル・ディレクトリ説明

XXXXの部分には
plyers:選手別データ
results:成績表
timetable:番組表
のいづれかが入ります。

XXXX_lzh:lzhのダウンロード先です。　
XXXX_txt:解凍されたlzhファイルの保存先です。
XXXX_csv:　csvファイルが出力されます。

download_xxxx:サイトから、lzhファイルをダウンロードします。
unlzh_xxxx:lzhファイルを解凍します。
txtTocsv_xxxx:ttxtファイルをcsvに変換します。

■使用方法

download_xxxx →　unlzh_xxxx　→　txtTocsv_xxxx　の順で実行してください。

resultsとtimetableについては、スクリプトを編集し、対象期間を変更する必要があります。
現状では、2002にから、2017になっています。
詳細は各スクリプトのコメントをご覧ください。











