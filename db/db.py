


import os

class db(object):

    def __init__(self,*args,**kwargs):
        return

    def is_exists(self,*args,**kwargs):
        raise NotImplementedError

    def get_cursor(self,*args,**kwargs):
        raise NotImplementedError

    @staticmethod
    def create(path):
        raise NotImplementedError

    def detect(self):
        raise NotImplementedError

    def exec_cmd(self,cmd):
        raise NotImplementedError

class sql(db):

    def exec_script(self,script):
        """cmd to exec sql statements"""
        raise NotImplementedError
        


    
class sqlite3(sql):

    myext='sqlite3'

    def __init__(self,path,**kwargs):
        self.path=path
        if self.is_exists(path) is not True:
            raise ValueError('no db found')

    @staticmethod
    def is_exists(path):
        return os.path.exists(path)
    

    def exec_script(self,script):
        cur=self.get_cursor()
        return cur.executescript(script)
    
    def get_cursor(self,*args,**kwargs):
        #should not exec when not exists
        try: return self.cur
        except: pass
        try: self.con
        except AttributeError:
            from sqlite3 import connect
            self.con= connect(self.path)
        self.cur= self.con.cursor()
        return self.cur

    @staticmethod
    def is_exists(path):
        return os.path.isfile(path) #cursory way

    @staticmethod
    def create(path):
        """wont do anything if something there already"""
        if os.path.isdir(path) is True:#existing pth
            raise ValueError('specify a file')

        assert os.path.isdir(os.path.split(path)[0]) is True
        myext=sqlite3.myext
        rt,xt=os.path.splitext(path)
        if myext not in xt:
            path=path+'.'+myext

        from sqlite3 import connect
        con=connect(path)
        con.close()
