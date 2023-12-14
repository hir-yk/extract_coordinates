
import csv
import sys

# 引数に指定されたファイル名がなければ'nmea.txt'をデフォルトとして使用します。
filename = 'nmea.txt' if len(sys.argv) < 2 else sys.argv[1]

def convert_to_degrees(coordinate, direction):
    """
    NMEAフォーマットの緯度または経度を十進表記の度に変換します。
    """

    deg_digits = 2 if direction in ['N', 'S'] else 3
    degrees = float(coordinate[:deg_digits])
    minutes = float(coordinate[deg_digits:])
    coordinate_decimal = degrees + minutes / 60

    if direction in ['S', 'W']:
        coordinate_decimal *= -1

    return coordinate_decimal


# CSVファイルを作成し、緯度と経度と標高を書き込みます。
with open('coordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 列名を書き込みます。
    writer.writerow(["緯度", "経度", "標高"])

    # NMEAデータを含むtxtファイルを開きます。
    with open(filename, 'r') as file:

        for line in file:
            fields = line.split(',')

            if len(fields) < 15:
                continue

            if fields[2] and fields[3] and fields[4] and fields[5] and fields[11]:  

                lat, lon, altitude = fields[2], fields[4], fields[11]

                lat = convert_to_degrees(lat, fields[3])
                lon = convert_to_degrees(lon, fields[5])
                
                # 標高をfloat型に変換します
                altitude = float(altitude)

                writer.writerow([lat, lon, altitude])


