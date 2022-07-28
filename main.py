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
class Function(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def showhelp(self):
        pass

class BaiduSearch(ProcessProduce,Function):
    def __init__(self,content):
        super().__init__()
        self.content=content
        self.cmd=f'open -a "/Applications/Google Chrome.app" "https://www.baidu.com/s?wd=%s"'% self.content
    def run(self):
        os.system(self.cmd)
    def showhelp(self):
        print('hint:baidu <search content>')

class BilibiliSearch(ProcessProduce,Function):
    def __init__(self,content):
        super().__init__()
        self.content=content
        self.cmd=f'open -a "/Applications/Google Chrome.app" "https://search.bilibili.com/all?keyword=%s"'% self.content
    def run(self):
        os.system(self.cmd)
    def showhelp(self):
        print('hint:bilibili <search content>')

class GitHubSearch(ProcessProduce,Function):
    def __init__(self,content):
        super().__init__()
        self.content=content
        self.cmd=f'open -a "/Applications/Google Chrome.app" "https://github.com/search?q=%s"'% self.content
    def run(self):
        os.system(self.cmd)
    def showhelp(self):
        print('hint:github <search content>')


#简单工场:
class Watcher:
    def __init__(self,cmd,content):
        self.cmd=cmd
        self.content=content

    def createFactory(self):
        if self.cmd =='help':
            for cmd in command:
                print(cmd)
        elif self.cmd == 'baidu':
            return BaiduSearch(self.content)
        elif self.cmd == 'bilibili':
            return BilibiliSearch(self.content)
        elif self.cmd == 'github':
            return GitHubSearch(self.content)
        else:
            print('command error')

command = ['bilibili', 'baidu','github']

if __name__ == '__main__':
    while(1):
        cmdline=input()
        cmd=cmdline.split()[0]
        content=cmdline.replace('{0} '.format(cmd),'',1)
        try:
            factory=Watcher(cmd,content).createFactory()
            if content == 'help':
                factory.showhelp()
            else:
                factory.run()
        except AttributeError:
            pass



