#걍 추가해본글 2222
import requests
import pandas as pd
import pprint
import tourist_attraction

test_a = tourist_attraction.get_tourist_sites()

for item in test_a:
 print(item)