import re

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
Rostam Batmanglij <rostam@vpwk.com>,
Chris Tomson <ctomson@vpwk.com,
Bobbi Baio <bbaio@vpwk.com'''

print(re.search(r'Rostam', cc_list))
print(re.search(r'[R,B]obb[i,y]', cc_list))
print(re.search(r'Chr[a-z][a-z]', cc_list))