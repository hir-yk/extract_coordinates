# 必要なライブラリをインポート
import simplekml
import csv
import sys

# 引数でファイル名を取得。指定がない場合は"default.csv"をデフォルトとします。
filename = sys.argv[1] if len(sys.argv) > 1 else "coordinates.csv"

# KMLオブジェクトを作成
kml = simplekml.Kml()

# CSVファイルを開き、それぞれの行に対してプロセスを行います
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # ヘッダー行をスキップ
    for row in reader:
        # 行から緯度、経度、標高を取得
        lat, lon, alt = map(float, row)
        
        # KMLにポイントを追加
        pnt = kml.newpoint(coords=[(lon,lat,alt)])

# KMLファイルを保存
kml.save("output.kml")
