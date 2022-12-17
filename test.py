import asc

asc.setAlmV2()
asc.setThreads(0)

asc.setOption(asc.options_t.uppers)
asc.setOption(asc.options_t.ascSplit)
asc.setOption(asc.options_t.ascAlter)
asc.setOption(asc.options_t.ascESplit)
asc.setOption(asc.options_t.ascRSplit)
asc.setOption(asc.options_t.ascUppers)
asc.setOption(asc.options_t.ascHyphen)
asc.setOption(asc.options_t.ascWordRep)
asc.setOption(asc.options_t.mixDicts)
asc.setOption(asc.options_t.confidence)

def status(text, status):
    print(text, status)

#загружаем собранный индекс
asc.loadIndex("./ascind.asc", "", status)

f1 = open('./test.txt')
f2 = open('./result.txt', 'w')

for line in f1.readlines():
    res = asc.spell(line)
    f2.write("%s\n" % res[0])

f2.close()
f1.close()
