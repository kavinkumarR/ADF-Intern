"""Day4 task"""
import collections
import re
import uuid
import logging
import sys


class Files:
    """Base class"""
    def __init__(self):
        self.var_sen = ""
        self.var_nk = []

    def getfile_name(self):
        """file read function"""
        var_fil = input('Enter the file name:')
        with open(var_fil, "r") as var_fi:
            self.var_sen = var_fi.read()
            var_fi.close()
        logger.info("getfile name function get executed")


    def file_write(self, obj_f):
        """File write function"""
        obj_f.action3()
        unique_fi = str(uuid.uuid4())
        with open(unique_fi, 'w') as op_fil:
            var_k = " ".join(self.var_nk)
            op_fil.write(var_k)
        logger.info("file_write function get executed")


class Function(Files):
    """this class is child class inherits base class Files"""
    def __init__(self):
        super().__init__()
        self.var_strlist = []
        self.var_to = 0
        self.var_ing = 0
        self.var_word_dict = {}
        self.var_pal = []

    def action1(self):
        """finds no of words with start as'To' and end as 'ing' also words which is palindrome and
        words with counter index"""
        self.var_strlist = list(self.var_sen.split())
        var_k = 1
        for i in self.var_strlist:
            if i[:2] == "To":
                self.var_to += 1
            if i[-3:] == "ing":
                self.var_ing += 1
            var_r = i[::-1]
            if i == var_r:
                self.var_pal.append(i)
            self.var_word_dict[var_k] = i
            var_k += 1

    def action2(self):
        """this function find unique word and save as list in var_uni"""
        var_c = collections.Counter(self.var_strlist)
        var_di = dict(var_c)
        var_uni = list(var_di.keys())
        logger.info("action2 function get executed")
        return var_uni

    def action3(self):
        """This function split words using vowels and make 3rd letter in capital,
        make every 5th word as capital and replace space with '-' and next line with ';'"""
        vol_list = re.split('a|e|i|u|o|A|E|I|U|O', self.var_sen)
        var_fst = 1
        var_sec = []
        for i in vol_list:
            if len(i) > 3:
                i = i[:2] + i[2].upper() + i[3:]
            if var_fst % 5 == 0:
                i = i.upper()
            i = i.replace(" ", "-")
            i = i.replace("\n", ";")
            var_sec.append(i)
            var_fst += 1
        self.var_nk = var_sec[:]
        logger.info("action3 function get executed")

    def display(self, obj_para):
        """Display the values"""
        obj_para.action1()
        var_temp = obj_para.action2()
        print("Number of Words with 'To' as prefix is " + str(self.var_to))
        print("Number of Words with 'ing' as ending is " + str(self.var_ing))
        print("Palindromes  are :" + str(self.var_pal))
        print("Max repeated Word  " + str(var_temp[0]))
        print("Unique Words are :" + str(var_temp))
        print("Words with index as dict: " + str(self.var_word_dict))
        logger.info("display function get executed")


"""def test_action1():
    To test the action 1
    obj_fun = Function()
    obj_fun.var_sen = " hi thing how are u mam"
    obj_fun.action1()
    assert obj_fun.var_to == 0"""


if __name__ == "__main__":
    logging.basicConfig(filename="logmsg.log", filemode='w', format="%(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("started")
    obj_fun1 = Function()
    obj_fun1.getfile_name()
    obj_fun1.display(obj_fun1)
    obj_fun1.file_write(obj_fun1)
    logger.info("completed")
