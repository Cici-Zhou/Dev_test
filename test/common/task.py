from multiprocessing.managers import SyncManager
from typing import List

class MyManager(SyncManager):
    pass

def getManager():
    m = MyManager()
    m.start()
    return m

class Task(object):
    def __init__(self, suite, parent: List, child: List, serialnum):
        '''
        这个任务将测试套件包装了一下，有点像一个链条上面的节点，指定了父节点和子节点，只不过这些节点可能
        不仅仅只有一个

        :param suite: 测试套件
        :param parent: 父节点
        :param child: 子节点
        :param serialnum: 测试套件的编号，就是第一列的序列号
        '''
        self.parent = parent
        self.child = child
        self.serialnum = serialnum
        self.suite = suite
        self.result = None

    # 设置当前的对象的运行状态
    def setresult(self, result):
        self.result = result

    def getresult(self):
        return self.result

    def getserialnum(self):
        return  self.serialnum

    def getparent(self):
        return self.parent

    def getchild(self):
        return self.child

    def getsuite(self):
        return self.suite

    def __repr__(self):
        return 'serialnum:{},parent:{},child:{},result:{}'.format(self.serialnum,self.parent,self.child, self.result)

# 注册之后， 再生成该类的实例能在多个进程里面传递
MyManager.register('Task', Task)