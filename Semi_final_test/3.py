import os
import sys
def m():
    try:
        a = sys.argv[1]
        #print(A)
        file = open('output.txt', 'w')
        try:
            #print(sys.getsizeof(A))
            file.write(str(os.stat(str(a)).st_size))
            file.close()
            return 0
        except:
            file.write('Can\'t open file' + ' ' + a)
            file.close()
            return 2
    except:
        file = open('output.txt', 'w')
        file.write('Usage: stat filename\n')
        file.close()
        return 1

exit(m())