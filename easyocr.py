# import easyocr
# reader = easyocr.Reader(['ch_sim','en'], gpu = True) # need to run only once to load model into memory
# result = reader.readtext('god.jpeg', details=1)

import os

cmd = 'easyocr -l ch_sim en -f notion.jpeg --detail=1 --gpu=False'
result = os.system(cmd)

print(result)