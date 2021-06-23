import collections
import re
import uuid

class Files:
    def __init__(self):
        self.sen=""
        self.fi=""
        self.nk=[]
    def getfile_name(self):
        try:
            fil = input("Enter the file name:")
            self.fi = open(fil, "r")
            self.sen = self.fi.read()
            self.fi.close()
        except:
            print("File not found")
            exit()
    def file_write(self,f):
        f.action3()
        unique_fi = str(uuid.uuid4())
        op_fil=open(unique_fi,'w')
        k=" ".join(self.nk)
        op_fil.write(k)
class Function(Files):
    def __init__(self):
        self.str_List=[]
        self.to = 0
        self.ing = 0
        self.word_dict = {}
        self.pal = []
        self.uni=[]
    def action1(self):
        self.str_List = list(self.sen.split())
        k = 1
        for i in self.str_List:
            if (i[:2] == "To"):
                self.to += 1
            if (i[-3:] == "ing"):
                self.ing += 1
            r = i[::-1]
            if (i == r):
                self.pal.append(i)
            self.word_dict[k] = i
            k += 1
    def action2(self):
        c = collections.Counter(self.str_List)
        di = dict(c)
        self.uni = list(di.keys())
    def action3(self):
        li = re.split('a|e|i|u|o|A|E|I|U|O', self.sen)
        n = 1
        nk = []
        for i in li:
            if (len(i) > 3):
                i = i[:2] + i[2].upper() + i[3:]
            if (n % 5 == 0):
                i = i.upper()
            i = i.replace(" ", "-")
            i = i.replace("\n", ";")
            nk.append(i)
            n += 1
        self.nk=nk[:]

    def display(self,fu):
        fu.action1()
        fu.action2()
        print("Number of Words with 'To' as prefix is " + str(self.to))
        print("Number of Words with 'ing' as ending is " + str(self.ing))
        print("Palindromes  are :" + str(self.pal))
        print("Max repeated Word  " + str(self.uni[0]))
        print("Unique Words are :" + str(self.uni))
        print("Words with index as dict: " + str(self.word_dict))




if __name__ == "__main__":
    f = Function()
    f.getfile_name()
    f.display(f)
    f.file_write(f)

