import sys

import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtGui import QStandardItemModel, QStandardItem


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableView(self)
        self.table.horizontalHeader().setVisible(False)
        layout = QVBoxLayout(self)
        layout.addWidget(self.table)
        model = QStandardItemModel(200, 1, self.table)
        self.table.setModel(model)
        companies = ("I'm + (verb/动词). I’m going now\n我(即将)… 我现在就去",
                     "I’m a + (noun/名词). I’m a teacher\n我是一名…	我是一名老师",
                     "I'm good at	. I’m good at playing basketball\n我擅长…	我擅长打篮球",
                     "I’m getting	. I’m getting sushi for lunch\n我要...	我午餐要吃寿司",
                     "I'm trying to + (verb/动词). I’m trying to study for the test\n我正在努力...	为了考试 我正在努力学习",
                     "I’m going	. I’m going to Thailand next week\n我将要去…	下周我将要前往泰国",
                     "I'm gonna + (verb/动词). I’m gonna make an appointment\n我准备...	我准备去预约",
                     "I’m in	. I’m in a basketball club\n我在…(团体内部)	我在篮球俱乐部",
                     "I'm not used to	. I’m not used to cold weather\n我不习惯…	我不习惯寒冷的天气",
                     "I'm not sure if + (subject/主词) + (verb/动词). I’m not sure if he is reli- able\n我不确定…是否…	我不确定他这个人是否可靠",
                     "I'm looking forward to	. I’m looking forward to your birthday party\n我期待着…	我很期待你的生日聚会",
                     "I'm calling to + (verb/动词). I’m calling to book a room\n我正在打电话要…	我正在打电话要订一间房",
                     "I'm working on	. I’m working on my motorcycle\n我正在(忙着)做…	我正在修理我的摩托车",
                     "I'm sorry to + (verb/动词). I’m sorry to tell you that I can’t come\n我很抱歉...	很抱歉告诉你 我不能来了",
                     "I'm thinking of/about + (verb-ing/动词-ing). I’m thinking of going to Australia\n我正在考虑…	我正在考虑前往澳大利亚",
                     "I'm dying to + (verb/动词). I’m dying to finish work today\n我非常想...	我非常想在今天完成工作",
                     "I'm having a hard time + (verb-ing/动词-ing). I’m having a hard time learning Spanish\n正处在某个艰难时期 学习西班牙语让我痛苦不堪",
                     "I’m afraid	. I’m afraid I can’t come\n我恐怕/担心…	恐怕我不能来了",
                     "I’m not really happy with	. I’m not really happy with my new hair- cut\n我对…不满意	我对自己的新发型不满意",
                     "I have + (noun/名词). I have two dogs\n我有...	我有两条狗",
                     "I used to + (verb/动词). I used to work at Apple\n我以前…	我以前在苹果公司工作",
                     "I have to + (verb/动词). I have to clean the house today\n我必须...	我今天必须打扫屋子",
                     "I have been + (verb-ing/动词-ing). I have been working all day\n我一直都在...	我一整天都在工作",
                     "I wanna + (verb/动词). I wanna find a girlfriend\n我想...	我想要找个女朋友",
                     "I would like to + (verb/动词). I would like to see the menu please\n我乐意做/愿意做…	我想看一下菜单",
                     "I need to + (verb/动词). I need to see a doctor\n我需要...	我需要去看医生",
                     "I plan to + (verb/动词). I plan to study abroad\n我打算...	我打算出国留学",
                     "I am about to + (verb/动词). I am about to go to sleep\n我快要...	我快要睡觉去了",
                     "I didn't mean to + (verb/动词). I didn’t mean to bother you\n我并不是故意… 我并不想打扰你",
                     "I don't have time to + (verb/动词). I don’t have time to chat on Wechat\n我没有时间(做)…	我没空在微信上聊天",
                     "I don’t know how to + (verb/动词). I don’t know how to use it\n我不晓得如何… 我不晓得如何使用它",
                     "I don’t like + (noun/名词). I don’t like video games\n我不喜欢…	我不喜欢电子游戏",
                     "I promise (not) to + (verb/动词). I promise not to start without you\n我保证(不)…	我保证自己会和你一起开始",
                     "I feel like + (verb-ing/动词-ing). I feel like going shopping\n我觉得想(做)…	我想去购物",
                     "I was busy + (verb-ing/动词-ing). I was busy talking with my boss\n我当时正忙着… 那时候我正忙着跟老板谈话",
                     "I want to + (verb/动词). I want to speak with her\n我想要(做)…	我想与她对话",
                     "I want you to + (verb/动词). I want you to pick me up\n我要你(做)…	我要你来接我",
                     "I have something	. I have something to help your headache\n我有办法/东西… 我有办法可以治你的头痛",
                     "I think he should + (verb/动词). I think he should eat some breakfast\n我觉得他应该… 我觉得他应该吃点儿早餐",
                     "I should have + (past participle/过去分词). I should have bought a ticket\n我原本应该…	我原本应该应该买下那张票",
                     "I wish I could + (verb/动词). I wish I could join the meeting\n我希望自己能…(假设) 我希望自己能够参加此次会议",
                     "I bet	. I bet there will be a traffic jam\n我敢肯定...	我敢肯这里即将 出现交通拥堵的情况",
                     "I cannot wait to + (verb/动词). I cannot wait to get to the beach\n我等不及...	我等不及要去海滩了",
                     "I have no idea	. I have no idea how to play mahjong\n我不知道...	我对打麻将一窍不通",
                     "I have got to + (verb/动词). I have got to be home by 9pm\n我必须…	我得在九点之前回到家",
                     "I wonder if	？I wonder if I can afford a BMW\n我想知道是否...	我想知道自己是否能买得起一台宝马汽车",
                     "I would rather	than	. I would rather take the subway than ride the bus\n我宁愿…也不愿…	我宁愿去坐地铁也不要坐公共汽车",
                     "I’ve been + (verb-ing/动词-ing). I have been thinking about changing jobs\n我一直在...	我一直在考虑换工作的事情",
                     "I've decided to + (verb/动词). I’ve decided to exercise daily\n我已经决定…	我已经决定每天锻炼身体",
                     "I've heard that + (subject/主词) + (verb /动词). I’ve heard that he likes you\n我听说…	我听说他喜欢你",
                     "I’ve had enough of	. I’ve had enough of this dish\n我已经受够了… 这道菜我已经吃腻了",
                     "I'll help you + (verb/动词). I’ll help you move tomorrow\n我会来帮你…	明天我会来帮你搬家",
                     "I’ll let you know	. I’ll let you know if I’m free on Monday\n我会告知你…	要是我周一有空的话 就告知你一声",
                     "I’d like you to + (verb//动词). I’d like you to call me when you arrive\n我想要你...	你抵达的时候 要给我打电话",
                     "I’d hate for you to + (verb/动词). I’d hate for you to have an accident\n我不愿意你…	我希望你可以平安无事",
                     "I’d be grateful	. I’d be grateful if you can help me move\n我会表示感激…  要是你能来帮搬家的话 我将会感激不尽",
                     "Can I + (verb/动词)? Can I come to the party\n我能否...吗	我能来参加派对吗",
                     "Could I + (verb/动词)? Could I get your phone number\n我能否…吗(更礼貌)	能给我 您的电话号码吗",
                     "Could you + (verb/动词)? Could you tell me how to get there\n您能否...吗	您能否可以告诉我 该如何到那里",
                     "Excuse me,	. Excuse me, where is the bathroom\n劳驾…	劳驾 请问洗手间在哪里",
                     "Let me + (verb/动词). Let me show you how to do it\n让我来…	让我来向您演示 该如何使用它",
                     "Are you	? Are you a student\n你(您)是…吗	你是一名学生吗",
                     "Are you into + (noun/名词)? Are you into Kpop\n你喜欢…吗	你喜欢韩国流行乐吗",
                     "Are you trying to + (verb/动词). Are you trying to cook Chinese food\n你正在尝试...吗 你正在尝试做中国菜吗",
                     "Are you sure + (subject/主词) + (verb/动词). Are you sure you can finish on time\n你确定...吗	你确定自己能准时完成吗",
                     "Are you used to? + (verb-ing/动词-ing). Are you used to running marathons\n你习惯…吗	你习惯跑马拉松吗",
                     "Do you + (verb/动词)? Do you smoke\n你(动作)…吗	你抽烟吗",
                     "Do you mind if I + (verb/动词)? Do you mind if I use the bathroom\n是否介意我…吗 你是否介意让我使用一下洗手间",
                     "Do you like + (noun/名词)? Do you like BBQ\n你喜欢…吗	你喜欢烧烤吗",
                     "Do you want me to + (verb/动词)? Do you want me to get it for you\n你要我…吗	要我替你拿那个吗",
                     "Do you have	? Do you have an iPhone\n你有…吗	你有iPhone手机吗",
                     "Do you feel like + (verb-ing/动词-ing)? Do you feel like going out for dinner\n你想(做)…吗	你想不想去外边吃晚餐",
                     "Do you know	? Do you know where I can get a taxi\n你知道...吗	你知道 在哪里可以搭出租车吗",
                     "Did you use to + (verb/动词)? Did you use to work at a bank\n你曾经…吗	你曾经在银行工作过吗",
                     "Have you  ? Have you eaten yet\n你已经…吗	你已经吃过饭了吗",
                     "Have you ever	? Have you ever been to Egypt\n你曾经…吗	你曾经去过埃及吗",
                     "You should + (verb/动词). You should come to watch the game\n你应该…	你应该来看这场比赛",
                     "You could have + (past participle/过去分词). You could have told me earlier\n你原本应该…	你原本应该早一点告诉我",
                     "You can never + (verb/动词) too	. You can never be too careful\n再…也不为过	小心驶得万年船",
                     "You have to + (verb/动词) in order to + (verb/动词). You have to study hard in order to graduate\n为了…(目的)你就必须…	你想毕业的话 就必须努力学习",
                     "You're supposed to + (verb/动词). You’re supposed to do it this way\n你应该…	你应该这么做",
                     "You seem + (adjective/形容词). You seem smart\n你看起来(似乎)…	你看起来挺机灵的",
                     "You'd better + (verb/动词). You’d better call a doctor\n你最好...	你最好去看一下医生",
                     "Thank you for	. Thank you for the gift\n为…表达感谢	谢谢你的礼物",
                     "If I were you, I would + (verb/动词). If I were you, I would take the job\n要是我的话…就会…	要是我的话 我就会接受这份工作",
                     "If you’d like to + (verb/动词). If you’d like to get coffee sometime, please call me\n你要是愿意的话…	要是你哪天想喝咖啡的话 就给我打电话吧",
                     "as	as possible. We will run as far as possible\n尽力…	我们将会竭尽所能",
                     "We went	. We went to the store to buy milk\n我们去了…(过去时)	我们去了商买牛奶",
                     "We need	. We need a place to stay\n我们需要…	我们需要一处住所",
                     "Let's not + (verb/动词). Let’s not talk about it\n让我们不要…	我们不要讨论它",
                     "She is not only + (adjective/形容词) but also + (adjective/形容词). She is not only beautiful but also smart\n她不但…而且...	她不但长得漂亮 而且也很聪明",
                     "He is as + (adjective/形容词) as	. He is as old as I am\n他的(特质)与…一样	他跟我是同龄人",
                     "He is so + (adjective/形容词) that	. He is so stubborn that I can’t talk to him\n他是那么…以至于…	他实在是太固执了 甚至我都无法与他谈了",
                     "As far as + (subject/主词) + (verb/动词). As far as I know it’s cancelled\n据了解…	据我所知 (那个)已经取消了",
                     "Be careful	. Be careful when you cross the street\n小心	过马路的时候你要小心",
                     "But this doesn’t mean that + (subject/主词) + (verb/动词). But this doesn’t mean that you can eat it\n但是这并不能说明…	但是这并不表示你就可以吃了它",
                     "By the way	./? By the way, do you have any gum\n顺便问一下	顺便问一下 你有口香糖吗",
                     "Compared to + (noun/名词). Compared to English, Chinese is more difficult\n与…相比	英语和汉语相比 汉语还是更难一些",
                     "Don't + (verb/动词). Don’t stay out too late\n不要...	不要在外边待得太晚",
                     "Don’t ever + (verb/动词). Don’t ever buy a new car\n千万不要…	千万别买新车",
                     "Even though	. Even though I have no job I’m still happy\n虽然…	虽然我没有工作 但是我依旧很快乐",
                     "Even if	. Even if it’s unhealthy, I still enjoy video games\n虽然…	即使它很不健康 但是我还是喜欢玩电子游戏",
                     "How are you + (verb-ing/动词-ing)? How are you going to get there\n你打算怎么…	你打算怎么去那儿",
                     "How do you + (verb/动词)? How do you know each other\n你怎么(做)…	你们之间是怎么认识的",
                     "How much + (verb/动词)? How much does the job pay\n多少钱	这份工作的薪资是多少",
                     "How often do/does	? How often do you travel for business\n多久一次...	你多久出差一次",
                     "How long does it take to + (verb/动词)? How long does it take to drive to work\n要花多少…(时间/钱)	开车去上班要花多少时间",
                     "Is it + (adjective/形容词)? Is it far from here\n(那个)…吗(一般疑问句)	那个离这儿远吗？",
                     "If it hadn’t been for  	. If it hadn’t been for my coach, I would have given up\n要不是…的话	要不是我的教练 我肯定早就放弃了",
                     "It’s too bad that  	. It’s too bad that he got fired\n…真是太糟糕/可惜	他被解雇真是太可惜了",
                     "It’s my fault for + (verb-ing/动词-ing). It’s my fault for being late\n…是我的错	迟到是我的错",
                     "It’s not that  	 but  	. It’s not that he’s boring, but I think he’s ugly\n不是...而是...	我并不是说他很无聊 而是我认为他长得不好看",
                     "It's very kind of you to + (verb/动词). It’s very kind of you to pay for everything\n你真个好人…(表达谢意)	您真的是个好人 替我们支付了全部的费用",
                     "It’s a little  	. It’s a little too big for me\n有一点点…	对我来说 它有点儿太大了",
                     "It's hard for me to + (verb/动词). It’s hard for me to ride a bicycle\n对我来说…很难 对我而言 骑自行车很难",
                     "It’s up to + (subject/主词). It’s up to mom where we eat\n由…说了算	吃饭的地方就让妈妈来做决定吧",
                     "It’s your turn  	. It’s your turn to do the dishes\n轮到你了	轮到你来洗碗了",
                     "It may surprise you, but + (subject/主词) + (verb/动词). It may surprise you, but she is blind\n可能会让你惊讶…但是…  也许这会让你感到惊讶 但她是位盲人",
                     "It's gonna be + (adjective/形容词). It’s gonna be difficult to learn\n将会成为…	这个可能很会很难学",
                     "It looks like + (noun/名词). It looks like she’s into you\n...似乎看起来...	她似乎喜欢你",
                     "It takes + (time/时间) + to + (verb/动词). It takes 1 hour to exercise properly\n…要花费…	我用了一个小时以正确的方式锻炼身体",
                     "It's no use + (verb-ing/动词-ing). It’s not use waking up so early\n…没有效果	这么早醒过来没有用",
                     "It's time to + (verb/动词). It’s time to eat dinner\n…的时间到了	晚餐的时间到了",
                     "It's too bad. It’s too bad I’m busy tomorrow\n…太糟糕/遗憾	很遗憾 我明天会很忙",
                     "No matter what,	. No matter what, we need to arrive by 7am\n不论如何…	不论如何我们都要在七点钟之前抵达",
                     "No wonder	. No wonder she was so tired this morning\n难怪…	难怪今天早上她这么累",
                     "Now that I think about it,	. Now that I think about it, that shirt was too expensive\n现在我想起来…  现在我想起来 当时那件T恤衫确实太贵了",
                     "Once you + (verb/动词). Once you open a bag of cookies, you can’t stop eating them\n一旦你...	一旦你打开那袋饼干 你肯定会吃个不停",
                     "On one hand	, but on the other hand,	. On one hand I think BBQ would be delicious, but on the other hand, noodles are easier to make\n一方面…另一方面… 一方面我觉得烧烤会很好吃 但是另一方面 煮面条会更方便一些",
                     "Please make sure that + (subject/主词) + (verb/动词). Please make sure that you call before 3pm\n请确认…	请确认你会在下午三点之前给我打电话",
                     "Please + (verb/动词). Please help me\n请…	请帮帮我",
                     "Should I + (verb/动词). Should I ask her out\n我应该…吗	我应该找她约会吗",
                     "Shouldn’t we + (verb/动词)? Shouldn’t we ask the teacher\n我们不应该…吗 我们不应该问一下老师吗",
                     "Speaking of + (subject/主词)? Speaking of TV shows, have you seen 2 Broke Girls\n谈到…	说到电视剧 你有没有看过电视剧《破产女孩》",
                     "Thanks to + (subject/主词). Thanks to dad, we’ve found our dog\n为…表达感谢	谢谢爸爸 咱家的狗已经找到了",
                     "That's why + (subject/主词) + (verb/动词). That’s why Tom Cruise is the best actor\n这就是…的原因 这就是汤姆克鲁思是最佳男演员的原因",
                     "The first thing I’m going to do  	 is  	. The first thing I’m going to do when I get to Italy is eat pasta\n首先要做的事情是...	我在意大利要做的第一件事情 就是去品尝意大利面",
                     "The more	the more	. The more I study Chinese the more I enjoy it\n越…就越…	汉语学得越深入 越是让我乐在其中",
                     "There is nothing as	as	. There is nothing as good as mom’s cooking\n没什么可以和…一样 没什么东西能与妈妈做的饭相提并论",
                     "There is something wrong with + (noun/名词). There is something wrong with the pasta\n…有问题	这个意大利面有问题",
                     "There is nothing I like better than + (noun/名词). There is nothing I like better than ice cream in the summer\n我最喜欢…	在夏天 我最喜欢的就是冰淇淋",
                     "There's no way + (subject/主词) + (verb/动词). There’s not way I can come\n不可能...	我不可能来了",
                     "There's no need to + (verb/动词). There’s no need to give it back\n没有必要(做)…	没有必要还给我了",
                     "This is	. This is the best restaurant in London\n这是…	这是伦敦最棒的一间餐馆",
                     "Was + (subject/动词)? Was your trip fun\n一般疑问句(过去时)	你那次旅行玩得开心吗",
                     "We hope + (subject/动词) + (verb/动词). We hope you had a good time\n我们希望…	我们希望你度过了一段美好的时光",
                     "What do you think about	? What do you think about seeing The Avengers\n你觉得…怎么样 (一起)去看电影《仇者联盟》你意下如何",
                     "Why don't we + (verb/动词)? Why don’t we go see it tomorrow\n我们为什么不… 明天我们为什么不去看呢",
                     "We’d better + (verb/动词). We’d better leave now to make it on time\n我们最好…	我们最好现在就出发 (这样)就能准时抵达了",
                     "We may as well + (verb/动词). We may as well quit now\n我们不妨…为好 我们不妨现在就退出吧",
                     "What can I do + (subject/动词)? What can I do to help complete the project\n我该怎么办	我该怎么做才能协助完成这个项目呢",
                     "What did you + (verb/动词)? What did you do last night\n你做了什么(过去时)	昨天晚上你在干嘛",
                     "What do you + (verb/动词)? What do you like about it\n你想要什么	你喜欢什么",
                     "What if	? What if we cancel the class\n如果…怎么样	如果我们取消课程会怎么样",
                     "What I’m trying to say is  	. What I’m trying to say is I think you can eat more healthy foods\n我想要表达的是…	我想说的是 我觉得你该多吃一些更健康的食品",
                     "What’s the matter with + (verb-ing/动词-ing)? What’s the matter with eating a midnight snack\n(动作)…会怎么样 吃点儿宵夜会怎么样",
                     "What would you do if + (subject/主词) + (verb/动词)? What would you do if you got a flat tire\n要是你 你会怎么做…	如果你遇到爆胎的情况 你会怎么做",
                     "What’s your favorite + (noun/名词)? What’s your favorite band\n你最喜欢的是什么	你最喜欢的乐队是什么",
                     "What’s the + (noun/名词)? What’s the temperature outside\n对特指的事物提问	外边的温度是多少",
                     "What’s this  	? What’s this movie about\n这个…是什么	这部电影讲述了什么故事",
                     "What are you + (verb-ing/动词-ing)? What are you thinking about\n你正在...	你正在思考什么",
                     "What time	? What time does the movie start\n几点	电影几点开始",
                     "What do you like	? What do you like doing in your free time\n你喜欢做…	你平时业余时间都喜欢做些什么",
                     "What does	? What does your father do\n对第三人称提问 你的父亲是做什么工作的",
                     "When is	? When is your birthday\n...是哪一天	你的生日是哪一天",
                     "When can you + (verb/动词)? When can you come to Beijing\n你何时能…	你何时能来北京",
                     "Where can I + (verb/动词)? Where can I park my car\n我在哪里可以… 我的车可以停在哪儿",
                     "Where did you + (verb/动词)? Where did you buy that candy\n你在哪里…(过去时) 你的糖是在哪里买的",
                     "Who is (verb-ing/动词-ing)? Who is coming to play football\n谁是…	谁来踢球",
                     "Why not + (verb/动词)? Why not sit down and relax\n有何不可	坐下来放松一下 有何不可",
                     "Why did + (subject/主词) + (verb/动词)? Why did you go to the UK\n为什么…(过去时)	你为何要去英国",
                     "Why would + (subject/主词) + (verb/动词)? Why would she do that\n为什么要…(表达猜测)	她为什么要那样做",
                     "Would you care for + (noun/名词)? Would you care for a tea\n你要不要...	你要不要喝茶",
                     "Would you like to + (verb/动词)? Would you like to dance\n你愿意…	愿意共舞一曲吗",
                     "Will you + (verb/动词)? Will you apply for the job\n你会不会…	你会不会应聘这份工作")

        self.resize(1200, 1000)
        mainLayout = QVBoxLayout()


        model.setHorizontalHeaderLabels(['Company'])

        table = QTableView()
        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)



        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()

        search_field.setStyleSheet('font-size: 35px; height: 60px;')
        search_field.textChanged.connect(filter_proxy_model.setFilterRegularExpression)
        mainLayout.addWidget(search_field)


        #vh = table.verticalHeader()
        #vh.setSectionResizeMode(PySide6.QtWidgets.QHeaderView.ResizeMode.Fixed)
        #vh.setDefaultSectionSize(55)
        table.setStyleSheet('font-size: 25px;')
        table.setWordWrap(False)
        table.setTextElideMode(PySide6.QtCore.Qt.TextElideMode.ElideNone)
        #table.resizeRowsToContents()
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)


        self.setLayout(mainLayout)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
