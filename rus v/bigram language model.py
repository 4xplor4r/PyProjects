


import re, random

materials = 'Мальчик пошел гулять, мальчик идет за обедом!\nМальчик забрал мед. Мальчик. Лох. Мальчик пошел.'
SIMBOLS = '#$-";:'
for simbol in SIMBOLS:
    materials = materials.replace(simbol, '')
materials = materials.lower().replace('\n', ' ')
materials = materials.replace(',', '.')
materials = materials.replace('!', '.')
materials = materials.replace('?', '.')
print(materials)
data = set(materials.replace('.', '').split(' '))
print(data)
model = dict()
for word in data:
    print(word)
    var = re.findall(word + r" (\w+)" , materials)
    model[word] = var 
    print(var)
print(model)


prefix = 'мальчик'
length = 20
# print(random.choice(model[prefix]))
for i in range(length):
    word = model[prefix]
    if word == []:
        word = random.choice(list(model.keys()))
        print(word, end=' ')
        continue
    res = random.choice(word)
    print(res, end=' ')
    prefix = res





'''
import sys
from PIL import Image
img = Image.new('RGB', (16, 16), color = 'white')
img.save('C:/Users/nsusc/Desktop/wt.png')

# 16 * (16 - x + 1)

with Image.open('C:/Users/nsusc/Desktop/wt.png') as im:
    y = 0
    x = 0
    print(im.size)
    for x in range(im.size[0] // 2):
        for y in range(im.size[1] // 2):
            im.putpixel((x, y), (255, 16 * y, 16 * x))
    print()
    for x in range(im.size[0] // 2):
        for y in range(im.size[1] // 2, im.size[1]):
            im.putpixel((x, y), (255, 255, 0))
    for x in range(im.size[0] // 2, im.size[0]):
        for y in range(im.size[1] // 2):
            im.putpixel((x, y), ((22 - x) * 16, y * 16, 255))
    for x in range(im.size[0] // 2, im.size[0]):
        for y in range(im.size[1] // 2, im.size[1]):
            im.putpixel((x, y), (16 * (22 - x), 255, 16 * y))
    # draw.line((0, 0) + im.size, fill=128)
    # draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # write to stdout
    im.save(sys.stdout, "PNG")
    im.show()
'''