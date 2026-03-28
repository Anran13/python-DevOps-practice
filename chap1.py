import re

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
Rostam Batmanglij <rostam@vpwk.com>,
Chris Tomson <ctomson@vpwk.com,
Bobbi Baio <bbaio@vpwk.com'''

print(re.search(r'Rostam', cc_list))
print(re.search(r'[R,B]obb[i,y]', cc_list))
print(re.search(r'Chr[a-z][a-z]', cc_list))
print(re.search(r'[A-Za-z]+', cc_list))
print(re.search(r'[A-Za-z]+@[a-z]+\.', cc_list))
print(re.search(r'\w+', cc_list))
print(re.search(r'\w+@+\w+\.+\w+', cc_list))

print(f'\n')
print(f'Find every parts of matched characters:')
print(re.search(r'(\w+)@(\w+)\.(\w+)', cc_list))
matched = re.search(r'(\w+)@(\w+)\.(\w+)', cc_list)
print(matched.group(0))
print(matched.group(1))
print(matched.group(2))
print(matched.group(3))
print(matched.groups())

print(f'\nCall by name:')
matched = re.search(r'(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
print(matched.group('name'))
print(matched.group('SLD'))
print(matched.group('TLD'))

print(f'\nFind all:')
matched = re.findall(r'\w+@\w+\.\w+', cc_list)
print(matched)
matched = re.findall(r'(\w+)@(\w+)\.(\w+)', cc_list)
print(matched)
print([x[0] for x in matched])
print([x[1] for x in matched])
print([x[2] for x in matched])

print(f'\nFind all:')
matched = re.finditer(r'(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
for m in matched:
    print(m.groupdict())

print(re.sub("\d", "#", "The phone names will be replaced by 1234"))
print(re.sub("(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)", "\g<TLD>.\g<SLD>.\g<name>", cc_list))

print(f'\nCompiling: ')
regex = re.compile(r'\w+\@\w+\.\w+')
print(regex.search(cc_list))
print(regex.findall(cc_list))