#如果我们对交互的流程和样式不满意，就优化增强 Bot 父类的 run() 方法；
#如果我们需要更多对话内容，就定义更多不一样的 Bot 子类；
#如果想增加对话系统级的操作，比如提供系统帮助指令，可以修改 Garfield 和 Bot 类的 run() 方法来实现。



#1.公共父类 Bot


import time

class Bot:
    wait = 1
    
    def __init__(self):
        self.q = ''
        self.a = ''
        
    def _think(self, s):
        return s
    
    def run(self):
        time.sleep(Bot.wait)
        print(self.q)
        self.a = input()
        time.sleep(Bot.wait)
        print(self._think(self.a))


#2.各个Bot子类
class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name?"
        
    def _think(self, s):
        return f"Hello{s}"

class GreetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"
        
    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"


import random
class FavoriteColorBot(Bot):
    def __init__(self):
        self.q = "what's your favorite color?"
    
    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"


#3.一个主流程BotZhao把上面的这些 Bot 串起来

class BotZhao:
    def __init__(self, wait= 1):
        Bot.wait = wait
        self.bots = []
        
    def add(self, bot):
        self.bots.append(bot)
        
    def _prompt(self, s):
        print(s)
        print()
        
    def run(self):
        self._prompt("This is BotZhao system. Let's talk.")
        for bot in self.bots:
            bot.run()

#4.初始化一个 Garfield 实例来具体运行
botzhao = BotZhao(1)
botzhao.add(HelloBot())
botzhao.add(GreetingBot())
botzhao.add(FavoriteColorBot())
botzhao.run()