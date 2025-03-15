### Users模块
> 负责模拟社交网络中用户的操作
+ Sub-moudle
  + Environment：负责用户观察到的个人环境与公共环境
    + args:
      + action(Actions)：负责定义社交网络中用户的行为
    + func:
      + async get_posts_env:获取所能看见的帖子
        + args: None
        + return: str:描述用户能够看见的帖子
      + async get_followers_env:获取受关注的数量
        + args: None
        + return:  str:i have n followers
      + async get_followes_env:获取受关注的数量
        + args: None
        + return:  str:i have n followes
      + async to_text_prompt: 将关注以及帖子信息转化为str
        + args:
          + include_posts（bool）:是否包括帖子信息
          + include_followers（bool）：是否包括被关注者信息
          + include_follows（bool）：是否包括关注者信息
  + Actions：负责构建用户在社交网络中所能够执行的所用动作
    + args:
      + agent_id(int)
      + channel(Channel)
    + func:
      + get_function_list：获取用户所有的操作集合
        + args:None
        + return: list[Function]:用户可以做的所有操作函数的集合，即Actions类中所有操作的函数集合
      + async perform_action：将要做的操作通知Channel以便平台进行反应
        + args:
          + message(Message):要传递的信息
          + type(str):要进行的操作类型
        + return: dict:描述操作结果以及返回信息
      + async action_name: 用户可以进行的所有操作
  + SocialGraph:负责维护整个社交网络中所有用户之间的关系
    + sub-moudle:
      + Neo4jHandler:连接图数据库
      + SocialGraph:社交网络连接图模块

  + Agent：社交网络中用户基本模拟单元
    + args:
      + agent_id(int)
      + user_info(UserInfo)
      + channel(Channel)
      + platform(PlatForm)
      + model_type(str)
      + agent_graph(SocialGraph)
      + action_prompt(str)
      + env（Environment（Actions(agent_id,channel)））
      + system_message(BaseMessage):调用大模型时的提示信息
      + memory(ChatHistoryMemory):用户历史信息
    + func
      + perform_agent_graph_action:模型收到指令后模拟用户在社交平台操作的步骤
        + args:None
        + return: None
+ Base-args:
  + db_path(str)：数据库所在url
  + user_csv_path（str）：所有用户csv文件
  + model_configs（dict）：模型基本配置
  + action_prompt_path(str)：agent提示句存储文件地址
+ Func:
  + readPrompt:
    + args:
      + promptPath(str)：agent提示词文件地址
    + return：
      + str:agent提示

  + generateGraph: 生成SocialGraph
    + args:
      + agent_info_path(str)：网络中用户基本信息url
      + platformChannel(Channel)：所用的社交网络接受通道
      + num_users(int):实验用到的用户数量
      + start_time(datatime)：模拟实验开始时间
      + platform(PlatForm)：实验所需要的社交平台
      + action_prompt(str)：用户操作指示命令,定义了对应的用户行为
      + model_configs(dict)：模型的基本设置
        + model_random_seed:(int): Random seed to randomly assign model to each agent. (default: 42)
        + cfgs (list, optional): List of configuration. (default: `None`)
        + neo4j_config (Neo4jConfig, optional): Neo4j graph database configuration. (default: `None`)
    + return: 
      + dict:A dictionary of agent IDs mapped to their respective agent class instances.
  + running：实验整理流程
    + args: 
      + timestep（int）:实验的轮数
      + infra(PlatForm)：实验的社交平台（持续运行）
    + return：None
  + 
### PlatForm模块
> 负责模拟社交平台的反应、接受用户操作
+ Sub-moudle:
  + Channel: 接受用户信息模块
  + Database：数据库处理模块
  + PlatFormUtils：平台基本工具，包含静态函数
  + recommend：用户刷新获取帖子时的推荐算法；利用Transformer实现基本的推荐
  + typing：平台中用户操作值对应表
+ Base-args:
  + post_csv_path（str）:初始网络中帖子存储csv文件
  + channel(Channel)：接受信息的通道
  + clock(Clock)：记录实验过程中的时间，方便数据库插入与操作顺序查看
  + start_time(datetime)：实验开始时间
  + allow_self_rating(bool)：允许自我评论
  + refresh_rec_post_count(int) = 1：用户刷新后获取到的最新的帖子
  + max_rec_post_len(int) = 2 ：当帖子数目少于设定数目时不做推荐算法
  + following_post_count（int）=3：当被关注的用户发布帖子时，返回的帖子数目（按照帖子点赞数排序？）
+ Func:
### Clock模块
> 负责模拟实验过程中时间流逝
### Analysis模块
> 对于模拟之后的实验数据进行分析，暂定