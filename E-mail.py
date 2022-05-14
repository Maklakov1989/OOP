import re
f_obj = open("Text.txt", 'r', encoding='utf-8')
text = f_obj.read()
print(text)
sentence = re.findall("[^.!?)]+[.!?]+[ \n]", text)
words = re.findall('\w{4,100}', text)
new_list = [el for el in words if words.count(el) < 10]
pattern1 = re.compile('[\w+./]+[a-z]+[$ .\w]')
link = pattern1.findall(text)
link2 = re.findall('[^. ]+\w+[.]+\w+[/]',text)
print(link2)




