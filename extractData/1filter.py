import json
import re
import os
'https://discord.com/channels/@me/897118245692264478/926739865503154206'

directory = 'Unoffcial Desmos Discord Server extracted files'
data_good_s = []
for filename in os.scandir(directory):
    if filename.is_file():
    
        with open(filename.path, encoding='utf-8') as f:
            data_s = json.load(f)

        
        pattern = re.compile(r"(https://www.desmos.com/calculator/.{10})")


        for j in range(len(data_s['messages'])):
            result_s = pattern.search(data_s['messages'][j]['content'])

            if result_s is not None:
                objj={"content":result_s.group(1),"author":data_s['messages'][j]['author']['name']}
            
            
                data_good_s.append(objj)


        with open("submissions_filtered.json","w", encoding='utf-8') as s:
            json.dump(data_good_s, s, ensure_ascii=False, indent=4)       
