import os
import json
import re

output = []
output1 = {}
output2 = {}
output3 = {}
output4 = {}

path = "./top250.json"
propath = os.path.abspath(path)
with open(propath, 'r', encoding='utf-8') as f:
    load_dict = json.load(f)

regularDierctActor = re.compile(r':\s([\u4e00-\u9fa5-\w·\sôá]+)\s')
regularInfo = re.compile(r'\s{28}(\d{4})\s/\s(.*)\s/\s(.*)\n')

for movie in load_dict:
    direct_actor = regularDierctActor.findall(movie['movie_board'])
    info = regularInfo.findall(movie['movie_board'])

    temp = {}
    temp['ranking'] = movie['ranking'][0].strip()
    temp['movie_name'] = movie['movie_name'][0].strip()
    temp['director'] = direct_actor[0].strip()
    temp['score'] = movie['score'][0].strip()
    temp['score_num'] = movie['score_num'][0].strip()
    temp['time'] = info[0][0].strip()
    temp['loaction'] = info[0][1].split( )
    temp['sort'] = info[0][2].split( )

    if len(direct_actor) == 2:
        temp['actor'] = direct_actor[1].strip()
    else:
        temp['actor'] = None

    output.append(temp)

#统计导演
for item in output:
    if output1.get(item['director']):
        output1[item['director']] = output1[item['director']] + 1
    else:
        output1[item['director']] = 1

#统计国家
for item in output:
    length = len(item['loaction'])
    for index in range(length):
        if output2.get(item['loaction'][index]):
            output2[item['loaction'][index]] = output2[item['loaction'][index]] + 1
        else:
            output2[item['loaction'][index]] = 1

#统计类型
for item in output:
    length = len(item['sort'])
    for index in range(length):
        if output3.get(item['sort'][index]):
            output3[item['sort'][index]] = output3[item['sort'][index]] + 1
        else:
            output3[item['sort'][index]] = 1

#统计年代
for item in output:
    year = int(item['time'])
    if year < 1960:
        if output4.get('<1960'):
            output4['<1960'] = output4['<1960'] + 1
        else:
            output4['<1960'] = 1
    elif year >= 1960 and year < 1970:
        if output4.get('1960~1970'):
            output4['1960~1970'] = output4['1960~1970'] + 1
        else:
            output4['1960~1970'] = 1
    elif year >= 1970 and year < 1980:
        if output4.get('1970~1980'):
            output4['1970~1980'] = output4['1970~1980'] + 1
        else:
            output4['1970~1980'] = 1
    elif year >= 1980 and year < 1990:
        if output4.get('1980~1990'):
            output4['1980~1990'] = output4['1980~1990'] + 1
        else:
            output4['1980~1990'] = 1
    elif year >= 1990 and year < 2000:
        if output4.get('1990~2000'):
            output4['1990~2000'] = output4['1990~2000'] + 1
        else:
            output4['1990~2000'] = 1
    elif year >= 2000 and year < 2010:
        if output4.get('2000~2010'):
            output4['2000~2010'] = output4['2000~2010'] + 1
        else:
            output4['2000~2010'] = 1
    else:
        if output4.get('>2010'):
            output4['>2010'] = output4['>2010'] + 1
        else:
            output4['>2010'] = 1

with open("./echart/director.json", "w", encoding="utf-8") as f:
    json.dump(output1, f)

with open("./echart//country.json", "w", encoding="utf-8") as f:
    json.dump(output2, f)

with open("./echart//type.json", "w", encoding="utf-8") as f:
    json.dump(output3, f)

with open("./echart//year.json", "w", encoding="utf-8") as f:
    json.dump(output4, f)