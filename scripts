def r_file(mode):
    if mode in [0,1]:
        global stext
        global e_text
        texts=open(r'F:\Python\REVERSETEXTS\texts.txt')
        jointhing=input('With:')
        #mode=int(input('Mode(0->normal 1->reversed):'))
        stext=list(texts)
        for i in range(0,len(stext)-1):
            stext.append(list(stext[i]))
            stext.remove(stext[i])
        #print(e_text)
        e_text=''.join(stext)
        #print(e_text)
        if mode==0:
            #pass
            e_text=list(e_text)
            print(jointhing.join(e_text))
        elif mode==1:
            e_text=list(e_text)
            e_text.reverse()
            #pass
            print(jointhing.join(e_text))
    else:
        print('Invaild Mode please Restart program!')

def r_text(mode):
    if mode in [0,1]:
        texts=input('Text:')
        jointhing=input('With:')
        #mode=int(input('Mode(0->normal 1->reversed):'))
        stext=list(texts)
        if mode==0:
            print(jointhing.join(stext))
        elif mode==1:
            stext.reverse()
            print(jointhing.join(stext))
    else:
        print('Invaild Mode please Restart program!')
                
def c_text(mode):
    global texts
    global stext
    global jthing
    global jointhing
    global uselesst
    if mode in [0,1]:
        texts=input('Text:')
        jointhing=input('With:')
        uselesst=jointhing
        stext=list(texts)
        #print(uselesst)
        #print(stext)
        for i in range(0,len(stext)-1):
            if uselesst not in stext:
                break
            else:
                stext.remove(uselesst)
                #print(stext)     
        if mode==0:
            jthing=''.join(stext)
            print(jthing)
        elif mode==1:
            stext=list(stext)
            stext.reverse()
            jthing=''.join(stext)
            print(jthing)
    else:
        print('Invaild Mode please Restart program!')
