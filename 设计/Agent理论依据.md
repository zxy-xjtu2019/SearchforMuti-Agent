### Agent定义
　
Agent是一个运行于**动态环境**的具有较高**自治能力**的实体，其根本目标是接受另外一个实体的委托并为之提供帮助和服务，能够在该目标的驱动下主动采取包括社交、学习等手段在内的变化进行适当的反应

### Agent本质
+ 目标与本质：为Agent提供帮助跟服务
+ 实现方法：自治
+ Agent技术本质：研究如何使用一个或多个**实体**尽可能不打扰用户，依靠自身能力，采用各种可能得方法和技术完成用户所委托的较为复杂与繁琐的任务
<br><font color = red>
该部分来自于李祥民老师分享的建模书籍
<br>注意文章中定义的自治性、社会能力、反应能力等agent特性不可被量化，可以作为一个使用agent的说明书，其中各种属性特点是需要关注的地方，但不能作为量化的属性；在工程化的角度来看，该属性特点应该是在**workflow**以及**任务拆解**这两个方面考虑
</font>

### 多Agent特性
+ 每个Agent能力有限，需要协作
+ 系统的控制是分布的
+ 知识数据是分散的
+ 计算异步进行

### 多Agent组成
+ 多个Agent(应该是有具体任务/角色)
+ 多Agent的联合意图（最终任务）
+ 常识（不同Agent之前应该都具有的知识/能力）
+ 公共行为规范（交互、全局操作需要规范否则不好实现，同时也容易存在消息错误的问题）
+ 生存环境（系统/任务的边界内部）

<font color = blue>全局连贯性是多智能体系统整体的重要特性</font>

### 多Agent最大问题：交互协议的描述与表达
#### 协议知识点整理
+ 协议组成
  + 消息传递、应答策略
  + 参与者角色
  + 语义限制
  + 参与者固定规则
+ CA通信协议
<br><font color = blue>在交互过程中，agent所扮演的角色可以根据对应的需求发生改变</font>

> 思考（针对Agent的使用方式）
> + Agent
> + 交互方式




> 思考(针对Agent的本质发展)：
> + 量化本质是不是一个去动态化的过程？
>   + 我们更加倾向于将各种事情量化，但是在这个过程中不可避免的删去了将所处理的事情的特征。
>   + 以情感分析为例，我们针对情感建模，将其进行量化，但是人是复杂的动物，对于“静态”的事物有着复杂甚至矛盾的情感，我们试图标签化群体/个体，是否忽略了多个标签交互形成的动态的反应？
> + Agent包括大模型火热的原因是否来自于其不可解释性？
>   + 在此之前我们使用代码的方式处理问题，将问题一点一点拆解，一步一步解决，但是这只是针对某一具体任务，或者说太过于静态的代码无法更好的适配动态的环境变化。
> + 生命不可能凭空产生，人类对于Agent的作用是否就是prompt?我们负责创造、使用，但是对于llm背后的发展不能完全的掌握
> 
> <br>