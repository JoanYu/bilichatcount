from xml.dom.minidom import parse
import xml.dom.minidom
import jieba

DOMTree = xml.dom.minidom.parse("bilichat.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print ('Root element : %s' % collection.getAttribute("shelf"))

danmus = collection.getElementsByTagName("d")
with open('danmu.txt','w') as f:
    for danmu in danmus:
        f.write(danmu.childNodes[0].data)
        f.write('\n')

with open('danmu.txt', 'r', encoding='UTF-8') as novelFile:
    novel = novelFile.read()

with open('punctuation.txt', 'r', encoding='UTF-8') as punctuationFile:
    for punctuation in punctuationFile.readlines():
        novel = novel.replace(punctuation[0], ' ')

with open('meaningless.txt', 'r', encoding='UTF-8') as meaninglessFile:
    mLessSet = set(meaninglessFile.read().split('\n'))
mLessSet.add(' ')

danmuList = list(jieba.cut(novel))
danmuSet = set(danmuList) - mLessSet
danmuDict = {}

for word in danmuSet:
    danmuDict[word] = danmuList.count(word)

danmuListSorted = list(danmuDict.items())
danmuListSorted.sort(key=lambda e: e[1], reverse=True)

topWordNum = 0
for topWordTup in danmuListSorted:
    if topWordNum == 20:
        break
    print(topWordTup)
    topWordNum += 1