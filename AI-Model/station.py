import csv

def station_data():
    f = open('station_info.csv', 'r')
    rdr = csv.reader(f)

    info = {}
    data = []

    for line in rdr:
        data.append(line)
    f.close()

    for d in data:
        station = d[2].split()

        if station[0] == '서울특별시':
            info[d[1]] = station[1]

    return info


if '__main__':
    data = station_data()

    data['봉천']

    print(data['봉천'])

