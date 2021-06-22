import collections
import re
import uuid

class Files:
    def getfile_name(self):
        try:
            fil = input("Enter the file name:")
            self.fi = open(fil, "r")
            self.sen = self.fi.read()
            self.fi.close()
        except:
            print("File not found")
            exit()

    def functions(self):
        self.str_List = list(self.sen.split())
        self.to = 0
        self.ing = 0
        self.word_dict = {}
        self.pal = []
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
        c = collections.Counter(self.str_List)
        di = dict(c)
        self.uni = list(di.keys())
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

    def display(self):
        print("Number of Words with 'To' as prefix is " + str(self.to))
        print("Number of Words with 'ing' as ending is " + str(self.ing))
        print("Max repeated Word  " + str(self.uni[0]))
        print("Palindromes  are :" + str(self.pal))
        print("Unique Words are :" + str(self.uni))
        print("Words with index as dict: " + str(self.word_dict))

    def file_write(self):
        unique_fi = str(uuid.uuid4())
        op_fil=open(unique_fi,'w')
        k=" ".join(self.nk)
        op_fil.write(k)


if __name__ == "__main__":
    f = Files()
    f.getfile_name()
    f.functions()
    f.display()
    f.file_write()