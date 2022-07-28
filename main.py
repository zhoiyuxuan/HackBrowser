from abc import ABCMeta, abstractmethod
from subprocess import PIPE,Popen
import os

#抽象工厂
class ProcessProduce:
    cmd=''
    proc=Popen(
        cmd,  # cmd特定的查询空间的命令
        stdin=None,  # 标准输入 键盘
        stdout=PIPE,  # -1 标准输出（演示器、终端) 保存到管道中以便进行操作
        stderr=PIPE,  # 标准错误，保存到管道
        shell=True)

#抽象产品
class SearchFunction(metaclass=ABCMeta):
    @abstractmethod
    def search(self):
        pass

class BaiduSearch(ProcessProduce,SearchFunction):
    def __init__(self,content):
        super().__init__()
        self.content=content
        self.cmd=f'open -a "/Applications/Google Chrome.app" "https://www.baidu.com/s?wd=%s"'% self.content
    def search(self):
        os.system(self.cmd)

class BilibiliSearch(ProcessProduce,SearchFunction):
    def __init__(self,content):
        super().__init__()
        self.content=content
        self.cmd=f'open -a "/Applications/Google Chrome.app" "https://search.bilibili.com/all?keyword=%s"'% self.content
    def search(self):
        os.system(self.cmd)

class Watcher:
    def __init__(self,cmd,content):
        self.cmd=cmd
        self.content=content

    def runCMD(self):
        if self.cmd not in command:
            print('command error')
        elif self.cmd == 'baidu':
            return BaiduSearch(self.content).search()
        elif self.cmd == 'bilibili':
            return BilibiliSearch(self.content).search()


command = ['bilibili', 'baidu']

if __name__ == '__main__':
    while(1):
        cmdline=input()
        cmd=cmdline.split()[0]
        content=cmdline.replace('{0} '.format(cmd),'',1)
        Watcher(cmd,content).runCMD()



