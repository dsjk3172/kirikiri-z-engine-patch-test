import re
import os.path

path = os.getcwd()
fileiist = os.listdir(f"{path}/원본")

for i in fileiist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-8')
    ReadFile2 = open(f"{path}/번역본/{i}", 'r' , encoding='UTF-16')
    WriteFile = open(f"{path}/결과물/{i}", 'w', encoding='UTF-8')
    lines = ReadFile.readlines()

    r = re.compile('.*[一-鿕ぁ-ゔァ-ヴー].*\[c\]')
    a = re.compile('.*[絵未].* vo=.*')
    b = re.compile('.*[桃子].* vo=.*')
    d = re.compile('.*[咲希].* vo=.*')
    e = re.compile('.*[八純].* vo=.*')
    f = re.compile('.*[月].* vo=.*')
    g = re.compile('\[幸\]')
    h = re.compile('\[幸 ff\]')

    for j in lines:
        aaa = ReadFile2.readline().strip("\n")
        
        if a.search(j):
            c = ' text="에미"]'
            contents = re.sub('\]', c, j)

        elif b.search(j):
            c = ' text="모모코"]'
            contents = re.sub('\]', c, j)

        elif d.search(j):
            c = ' text="사키"]'
            contents = re.sub('\]', c, j)

        elif e.search(j):
            c = ' text="하스미"]'
            contents = re.sub('\]', c, j)

        elif f.search(j):
            c = ' text="츠키"]'
            contents = re.sub('\]', c, j)
        
        elif g.search(j):
            c = ' text="유키"]'
            contents = re.sub('\]', c, j)

        elif h.search(j):
            c = ' text="유키"]'
            contents = re.sub('\]', c, j)

        else:
            contents = re.sub(r, aaa, j)
        WriteFile.write(contents)
WriteFile.close()