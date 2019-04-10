for i in range(8):
    if i > 0:
        fo = open(r'trial'+str(i)+'\params.txt','r')
        p = fo.read()
        fo.close
        
        fo = open('all_params.py','a')
        fo.write('Trial'+str(i))
        fo.write(p)
        fo.close()
        p = ''