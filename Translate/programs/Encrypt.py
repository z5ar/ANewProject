intro='''---------------------------------
版本 2
2020/03/22
1.修复了iong问题
---------------------------------'''
ecs=[{'zhi':'5','chi':'t','shi':'g','ri':'b','zi':'y','ci':'h','si':'n','ying':'u/','yuan':'m0','yue':'m,','yin':'up','yun':'mp','yi':'u','wu':'j','yu':'m','ye':'u,'},
{'zh':'5','ch':'t','sh':'g','b':'1','p':'q','m':'a','f':'z','d':'2','t':'w','n':'s','l':'x','g':'e','k':'d','h':'c','j':'r','q':'f','x':'v','r':'b','z':'y','c':'h','s':'n','y':'u','w':'j'},
{'ang':';','eng':'/','ing':'u/','ong':'j/','ai':'9','ei':'o','ui':'jo','ao':'l','ou':'.','iu':'u.','ie':'u,','ue':'m,','er':'-','an':'0','en':'p','in':'up','un':'jp','ün':'mp','a':'8','o':'i','e':'k','i':'u','u':'j','ü':'m','ê':','}]
tones={'1':' ','2':'6','3':'3','4':'4',' ':'7'}
from platform import system as psys
if psys()=='Windows':
    from os import system as osys
from os import getcwd
from random import shuffle

def func():
    print('''请选择：
0->退出
1->输入多行
其他内容->输入一行''')
    choice=input()
    print('''温馨提示：
输入拼音，分别用1,2,3,4，(空格)表示一声，二声，三声，四声，轻声。
轻声请用且必须用空格表示。拼音与拼音之间请不要有多余的空格。
标点符号请用全角符号。每一行的最后请用"|"结束。
例如：
这是一句不长不短的话。
zhe4shi4yi1ju4bu4chang2bu4duan3de hua4。|''')
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
    ret,tstr,tret=str(),str(),str()
    for ch in mstr:
        if ch=='|':
            ret+=ch
            break
        elif ch in ['1','2','3','4',' ']:
            for titem in ecs:
                for key,value in titem.items():
                    if key in (tstr if titem!=ecs[1] else tstr[:2]) :
                        tstr=tstr.replace(key,'',1)
                        tret+=value
                        if titem != ecs[2]:
                            break
                if tstr=='':
                    break
            if ('r' in tret) or ('f' in tret) or ('v' in tret):
                if 'j' in tret:
                    tret=tret.replace('j','m')
            if 'uj' in tret:
                tret=tret.replace('uj','m')
            tret=list(tret)
            shuffle(tret)
            ret+=''.join(tret)+tones[ch]
            tret,tstr=str(),str()
        elif (ch not in ecs[0]) and (ch not in ecs[1]) and (ch not in ecs[2]):
            ret+=ch
        else:
            tstr+=ch
    print(ret)

if __name__ == "__main__":
    print(intro)
    try:
        func()
    except KeyboardInterrupt:
        print('')
    except Exception:
        print("程序出错！错误信息：",str(Exception))
    if psys()=="Windows":
        osys("pause")