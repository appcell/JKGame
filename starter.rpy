


label starter_start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene hotel night

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    

    # 此处显示各行对话。
    
    
    jotaro_nvl """

    来到日本出差，迄今已过了三周。

    每天追查“箭”的下落，，完全没有休息的机会。加上研究院规定的论文任务，这次出差让我身心俱疲。

    像今天这样凌晨才得以入睡，几乎已经是常态了。
               
    {clear}
    """

    $ renpy.music.set_volume(0.4, 0, 'sound')
    play sound "sound/phonering.mp3"
    
    """
    “叮铃铃铃…”
    """
    
    jotaro_nvl """
    刚躺上枕头，就听见恼人的电话铃声。

    凌晨两点打来电话，大概又是非处理不可的紧急事故吧。

    今晚看来也无法休息了。我叹了口气，起身拿起话筒。
    
    {clear}
    """

    show jotaro normal
    jotaro "这里是空条。有什么事吗？"
    hide jotaro
    
    secretary "空条博士，抱歉这么晚还打扰您，实在是有急事。{p}
               
    2丁目那里出现了替身使者，正把一个小孩挟持做人质。"

    secretary "车已经在楼下等您了，请快去看看吧！"
    
    jotaro_nvl """
    ——啊啊，果然是替身使者的麻烦。
    
    从十年前被卷入起，解决层出不穷的替身问题就成了逃不开的职责。
    
    虽然累得险些睁不开眼，我还是披上了外套。
    
    {clear}
    """
    
    window hide dissolve
    
    $ renpy.music.set_volume(0.2, 0, 'sound')
    play sound "sound/carstart.mp3" fadeout 1.0
    scene road night
    with fadehold
    
    pause
    
    jotaro_nvl """
    在车上，下属陆续做了汇报。
    
    制造事端的替身使拥有黏液状的远程替身，凡是沾到的东西都会隐形。劫持了一个小学生之后，他以此向银行勒索。
    
    单纯地打倒他并非难事。问题是，被劫持的学生在哪里？
    
    这样想着，我来到了现场。
    
    {clear}
    """
    
    window hide dissolve
    
    $ renpy.music.set_volume(1.0, 0, 'sound')
    
    play sound "sound/CarDoor2.mp3"
    
    scene bankgate night
    with fadehold
    
    pause
    
    secretary "空条博士！您总算是来了。"
    
    show jotaro normal
    jotaro "唔。{p}那个替身使者还是拒绝合作？"
    hide jotaro
        
    secretary "没错。他还说如果我们攻击，他就用黏液堵住孩子的气管。"
    
    
    jotaro_nvl """
    事情果然没那么简单。
    
    原本计划的攻击本体让替身不得不回防、乘机寻找人质的方法，这下就不起作用了。
    
    余下的方案只有将他瞬间打晕。但以白金之星的攻击距离，很难不被提前发现。
    
    如果有个擅长远程的替身使者在身边...
               
    ...
    
    我及时制止了自己的想法。
    
    {clear}
    """
    
    show jotaro normal
    jotaro "..."
    hide jotaro
    
    secretary "您刚才说了什么吗，博士？"
    
    show jotaro normal
    jotaro "没什么。{p}绑架者的位置你们清楚吗？"
    hide jotaro
    
    secretary "这个...是在这栋楼的第一层没有错，但他自己也隐形了，所以..."
    
    """
    没办法，只好放手一搏了。
    
    普通人窒息三分钟以上，对大脑就会造成不可逆的损伤，孩子应当更紧急一些。
    
    因此一旦开始行动，两分钟之内就要找到并解决这个隐形的家伙。
    
    还好和老头子在一起时有过经验。对付隐形者，可以借助烟雾判断对方的位置。
    
    {clear}
    """
    
    show jotaro normal
    jotaro "封锁逃生通道，向室内释放浓烟。能做到吗？准备好的话告诉我。"
    hide jotaro
    
    secretary "准备好了，博士，只等您一声令下。"
    
    """
    脱下外套和鞋子，尽量不弄出声响。白金之星忠实地浮现在身后。{p}按下手表上的计时器，走向被浓烟围绕的银行侧门。
    
    {clear}
    """
    
    show jotaro normal
    jotaro "开始。"
    hide jotaro

    window hide dissolve
    
    scene corridor
    with fadehold
    
    pause
    
    jotaro_nvl """
    有了烟雾和白金之星精密视力的帮助，一分钟后，在文件柜后发现了那家伙。
    
    可惜的是，他已经先一步发现我了。
    
    那男人静悄悄地用文件把自己围住，打算用粘液从背后偷袭。
    
    以为这样就能逃掉吗？真是可笑。
    
    用白金之星迅速清理掉他脸上的隐形粘液，我揪住领子，把他从衣柜里提了出来。
    
    {clear}
    """
    
    show jotaro normal
    jotaro "人质在哪？"
    hide jotaro

    robber "咳...咳咳！{p}你难道觉得我会招供？ {p}
            
            如果你们找到人质，岂不是要给我强加绑架的罪名？我可不会承认哦。"
    
    """
    时间不多了。
     
    再这样下去人质极有可能被撕票，我不由得抓得更紧了。
    
    {clear}
    """
    
    robber "你很想打晕我吧？只要我没有死，就可以保持替身的形态。有人质的话会...咳咳...很危险哦。"
    
    "他露出嘲讽的神情，似乎打定主意我已经束手无策。而我确实一时想不到好的办法。"
    
    show jotaro normal
    jotaro "…"
    hide jotaro
    
    jotaro_nvl """
    还剩30秒。
    
    强大如白金之星也无法在30秒内搜查整个楼层，何况人质可能不在这里。
    
    尽管不想承认，但我实实在在地开始紧张了。
    
    {clear}
    """
    
    window hide dissolve
    
    pause
    
    scene floor
    with dissolve
    
    jotaro_nvl """
    …等等。
               
    {clear}
    """
    
    jotaro_nvl """
    就在这时，我看见他的领口有什么东西在闪烁。{p}某种绿色、半透明的东西，微弱地动着。
    
    一根极细的绿色丝线。看起来就像...
    
    像…
    
    心脏砰砰地狂跳起来。
    
    丝线缩回了衣服里，很快又从裤腿钻出来，延伸至地板上，顺着墙角滑向走廊。
               
    {clear}
    
    """
    
    scene corridor
    with dissolve
    
    show jotaro normal
    jotaro "…"
    hide jotaro
    
    robber "喂，你，你干什么——"
    
    """
    几乎不受理智控制，我一把拎起这家伙，沿着地上游动的丝线狂奔。
    """
    
    window hide dissolve
    
    scene bank night
    with fadehold
    
    window show dissolve
    
    """
    推开隔间拉门的一刹那，绑架犯的脸上明显失去了血色。
    """
    
    robber "你是怎么..."
    
    play sound "sound/falling.mp3"
    
    show jotaro normal
    jotaro "闭嘴。"
    hide jotaro
    
    jotaro_nvl """
    我用一记手刀击昏了他。
               
    白金之星沿着丝线，用精密度A的手指剥离丝线另一头的粘液。
               
    很快，被绑架少年的鼻子和嘴凭空地显露出来。
    
    而我站在一边，全身都抖得厉害。
    
    自那以来，第一次，紧张得几乎站不住脚。
    
    是命运的作弄吗？
    
    指引我来到人质身边的丝线，在那个瞬间里，看起来几乎像是十年前友人的——
    
    ——绿之法皇。
    
    明知失去的东西无法复得，十年间，却还是抱着一丝幻想。
    
    如果是他，如果他还活着，如果…
               
    {clear}
    
    随着白金之星的动作，渐渐地，整张脸都被清理出来。头发也变得可以看清了。
    
    是个十岁左右的男孩，赤红色的头发。因为窒息太久而昏迷。
    
    但还有救。
    
    通过白金之星，能感觉到心脏还在微弱地跳动。
    
    不顾一切地，想要救活这个孩子。
    
    {clear}
    """
    
    menu:
        "先搬到空气良好的室外":

            jump starter_pull_to_outdoor

        "先做急救措施":

            jump starter_cpr

label starter_pull_to_outdoor:
    """
    对不起，这个分支我还没想好怎么写。
    
    但花花再不喘气就死了啊！所以如果你选了这个分支，就直接game over啦。
    
    先假设你选了急救好了。
    """
    
    jump starter_cpr
    
label starter_cpr:
    jotaro_nvl """    
    将男孩平放在地上，双手垫在他颈后。
    
    深吸一口气，抑制住咳嗽的冲动，嘴对嘴地用力呼出。
    
    一下，两下，三下...
    
    ...
    
    十四下，十五下...
               
    {clear}
    
    这样做的时候，冷汗几乎浸透了外套。
    
    让他安然无恙地活下去吧，我在内心祈求。
    
    紧紧地，仿佛要把自己的生命过渡给他似的，贴着他的唇大口地呼吸着。
    
    {clear}
    """
    
    unknown "咳...."
    
    jotaro_nvl """
    男孩的胸口动了动。几乎无法觉察地，他回应了我的呼吸。
    
    眼眶不知不觉热得发烧。
    
    倘若世上真的有奇迹，现在就是它发生的绝佳时机了。
               
    {clear}
    
    男孩胸腔的起伏越来越重，接着一阵剧烈的猛咳。长长的睫毛翕动着，慢慢地，他睁开了眼睛。
    
    像傍晚的天空一样的、紫色的眼睛，因为窒息和咳嗽而盈满泪水。
    
    那双与重要的友人相同的眼睛，跨越岁月的浓烟，目不转睛地凝视着我。
               
    {clear}
    
    """

    window hide dissolve
    
    pause
    
    window show dissolve

    jotaro_nvl """
    十年了。
    
    十年前的那一天，借助白金之星将肉芽从他的额前拔出时，也是那样的眼神。
    
    那时他睁开眼后说的第一句话是：“你为什么要救我呢？”
    
    {clear}
    """
    
    unknown "你为什么会哭呢？"
    
    jotaro_nvl """
    面前的男孩睁开眼后这样问道。
    
    我哭了吗？
               
    原来脸上的炙热并不是烟尘的缘故吗？…

    他认真的眼神无论如何都不像是说谎。
    
    我不由得移开了视线。
               
    {clear}
    """
    
    show jotaro normal
    jotaro "...{p}烟太浓了。去外面吧。"
    hide jotaro
    
    unknown "…咳咳…"
    
    jotaro_nvl """
    不想再失态更多，不由分说地抱起他向外走去。
    
    余下的事情，就交给SPW好了。
               
    {clear}
    """

label starter_after:
    

    window hide dissolve
    
    scene hotel day
    with fadelong
    
    pause


    jotaro_nvl """
    两周后。
               
    {clear}
    """
    
    play sound "sound/doorknock.mp3"
    
    pause

    secretary "空条博士，这是您要的资料。"

    show jotaro normal
    jotaro "谢谢。"
    hide jotaro

    jotaro_nvl """
    两周前的晚上，我从绑架犯手里救了一个男孩。
    
    在行动过程中，男孩亮出了和我已故的朋友、花京院典明的绿之法皇、类似的替身，外貌也和他极其相似。

    对这件事在意到失眠多日的我，让下属调查了他的档案。
               
    {clear}
    """
    
    secretary "男孩叫花京院典明，11岁，目前在市立公晓小学就读五年级，也是个替身使者。"

    """
    这样说着，她意味深长地向我瞥了一眼。
    """

    secretary "替身是绿色、半透明的人形，可以变化成多种形状，有很强的远距离操控能力，被取名为绿之法皇。"
               
    secretary "花京院典明从小就表现出了强大的替身能力，在对其父母的调查中也证实了这一点。"
    
    show jotaro normal
    jotaro "…"
    hide jotaro

    jotaro_nvl """
    尽管已经预料到，实际听到这些信息时，内心还是深受震撼。

    是巧合吗？是世界终于仁慈地给了第二次机会吗？

    手指几乎抖得握不住笔，面对秘书真是太失礼了。
               
    {clear}
    """

    window hide dissolve

    show jotaro normal
    jotaro "不用读了，把文件放在这里就好。"
    hide jotaro
    
    """
    深呼吸一口气，至少在同事面前要保持冷静。
    """

    show jotaro normal
    jotaro "收养的事情怎么样了？"
    hide jotaro

    secretary "这…博士，{p}花京院君的父母都还健在，只怕他们很难同意。"
    
    jotaro_nvl """
    呵…对了。
    
    知道这个男孩与过去的花京院典明的相似之处时，我就决心要收养他。
    
    只有待在我的身边，他才能得到较好的保护。
    
    经历了埃及和两周前的绑架案以后，我对此深信不疑。
    """

    show jotaro normal
    jotaro "你劝过他们了吗？"
    hide jotaro

    secretary "还没有。{p}不过空条博士，强行将未成年人从监护人身边带走，不论法律还是道义上都说不过去…"
               
    secretary "…财团也有些担心，希望您不要作冲动的决定。"

    """
    我放下笔，不容置疑地盯着她。
    """

    show jotaro normal
    jotaro "让一个上小学的替身使者和普通人一起生活，后果只会比两周前更严重。
            
            {p}倘若真的关心这孩子，应该理解我的决定。"
    hide jotaro

    secretary "可…{p}那可是孩子的父母啊，博士。"

    show jotaro normal
    jotaro "他的父母也很困扰吧？孩子有替身父母却看不见，大概会觉得受到欺骗了吧？"
    hide jotaro

    secretary "…这…的确，您说的没错。{p}
               
               花京院的父母对孩子的精神状态很担忧，交流过程中也多次相互争吵。"

    show jotaro normal
    jotaro "那好。{p}SPW下属的儿童慈善基金会，可以帮助问题儿童恢复正常。{p}你知道该怎么做了吧？"
    hide jotaro

    secretary "…我知道，但是…"

    show jotaro normal
    jotaro "最多十天，希望能见到花京院典明本人站在这里。就这样。"
    hide jotaro
    
    play sound "sound/Closing1.mp3"
    
    pause
    


    jotaro_nvl """
    {clear}

    秘书离开以后，终于可以长出一口气。

    说给别人的理由，连自己都无法取信。{p}私下里我知道，自己只是一厢情愿地，想要再见到那个友人罢了。

    有些东西，失去了就不能回来。但如果有回来的机会，成熟的男人就不应再犯同样的过错。

    这次，一定会让你幸福地生活下去。
    
    我暗暗地下定了决心。
    
    {clear}
    """

    return
