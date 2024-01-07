import sys
def load(file):
    try:
        with open(file) as f:
            loadtext = f.read().strip().split('\n')
            loadtext = [x.lower() for x in loadtext]
            return loadtext
            # ll=[]
            # for x in loadtext:
            #     ls = x.lower()
            #     ll.append(ls)
            # loadtext = ll
            return ll
    except IOError as e:
        print("%s as error : %s terminating file" % (e,file))
    sys.exit(1)
    
