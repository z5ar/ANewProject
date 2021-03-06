chs={'1':'b','q':'p','a':'m','z':'f','2':'d','w':'t','s':'n','x':'l','e':'g','d':'k','c':'h','r':'j','f':'q','v':'x','5':'zh','t':'ch','g':'sh','b':'r','y':'z','h':'c','n':'s','u':('i','y'),'j':('u','w'),'m':('ü','yu'),'8':'a','i':'o','k':'e',',':'ê','9':'ai','o':'ei','l':'ao','.':'ou','0':'an','p':'en',';':'ang','/':'eng','-':'er'}
tones={'a':{' ':'ā','6':'á','3':'ă','4':'à','7':'a'},'o':{' ':'ō','6':'ó','3':'ŏ','4':'ò','7':'o'},'e':{' ':'ē','6':'é','3':'ĕ','4':'è','7':'e'},'i':{' ':'ī','6':'í','3':'ĭ','4':'ì','7':'i'},'u':{' ':'ū','6':'ú','3':'ŭ','4':'ù','7':'u'},'ü':{' ':'ǖ','6':'ǘ','3':'ǚ','4':'ǜ','7':'ü'}}
intro='''---------------------------------
版本 6
2020/03/22
更新内容:
1.修复了Windows下多行输入的BUG
2.增加了输入文件路径提示
---------------------------------'''
ga=['1','q','a','z','2','w','s','x','e','d','c','r','f','v','5','t','g','b','y','h','n']
ra=['u','j','m']
from platform import system as psys
from os import getcwd
if psys()=='Windows':
    from os import system as osys

def func():
    print('''请选择：
0->退出
1->输入多行
其他内容->输入一行''')
    choice=input()
    if choice=='0':
        exit()
    elif choice=='1':
        minput()
    else:
        sinput()

def sinput():
    print('请输入：')
    mstr=input()
    dealWith(mstr)

def minput():
    fp=getcwd()
    if psys()=='Windows':
        fp+='\\input.txt'
    else:
        fp+='/input.txt'
    inf=open(fp,'w+')
    inf.close()
    print('请打开%s，并将内容输入到该文件中。'%fp)
    print('输入完成后',end='')
    if psys()=="Windows":
        osys("pause")
    else:
        print('请在此输入任何内容继续。')
        input()
    with open(fp,'r') as f:
        mstr=f.readline()
        while mstr:
            dealWith(mstr)
            mstr=f.readline()
            

def dealWith(mstr):
    tword=dict()
    for i in range(0,len(mstr)):
        if mstr[i]=='|':
            break
        elif mstr[i] in ['3','4','6','7',' ']:
            tword['tone']=mstr[i]
            if 'ga' in tword:
                word=chs[tword['ga']]
                if 'ra' in tword:
                    if tword['ra']=='m' and tword['ga'] not in ['s','x']:
                        word+='u'
                    else:
                        word+=chs[tword['ra']][0]
                if 'ma' in tword:
                    if tword['ma']==',':
                        word+='e'
                    else:
                        word+=chs[tword['ma']]
                if 'ra' not in tword and 'ma' not in tword:
                        word+='i'
            elif 'ra' in tword:
                word=chs[tword['ra']][1]
                if 'ma' in tword:
                    word+=chs[tword['ma']]
                    if chs[tword['ma']]=='ê':
                        word=word[:-1]+'e'
                else:
                    if tword['ra']=='j':
                        word+='u'
                    elif tword['ra']=='u':
                        word+='i'
            elif 'ma' in tword:
                word=chs[tword['ma']]
            for key,value in {'ieng':"ing",'yeng':'ying','ueng':'ong','uei':"ui",'ien':"in",'uen':'un','üen':'ün','iou':'iu'}.items():
                if key in word:
                    word=word.replace(key,value)
                    break
            flag=False
            for tc in ['a','o','e']:
                if tc in word:
                    word=word.replace(tc,tones[tc][mstr[i]])
                    flag=True
                    break
            if not flag:
                tstr=word[::-1]
                for ch in tstr:
                    if ch in ['i','u','ü']:
                        tstr=tstr.replace(ch,tones[ch][mstr[i]])
                        break
                word=tstr[::-1]
            print(word,end=' ')
            tword=dict()
        elif mstr[i] not in chs:
            print('\b'+mstr[i],end='')
        else:
            if mstr[i] in ga:
                tword['ga']=mstr[i]
            elif mstr[i] in ra:
                tword['ra']=mstr[i]
            else:
                tword['ma']=mstr[i]
    print()
if __name__=='__main__':
    print(intro)
    try:
        func()
    except KeyboardInterrupt:
        print('')
    except Exception:
        print("程序出错！错误信息：",Exception)
    if psys()=="Windows":
        osys("pause")