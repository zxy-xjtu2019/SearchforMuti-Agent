### Agent python函数设计
> 目的：构建自己可以轻松使用的agent函数;不存在完美的函数，所以要求能使用、易说明即可


#### 目录文件及定义
+ Agent
  + llms:用于对模型
    + jsonrepair:对于不合规范的json进行处理得到便于模型处理的json文件
    + token_counter:针对AutoGpt进行修改，用于计算模型所调用的tokens数

#### 类别定义
+ Agent
> 该类定义Agent的构建、单agent行为、多Agent的操作；要求支持定制化
  + 属性
    + baseUrl（string）:定义调用大模型的地址
    + useKey（string）:调用模型使用的key
    + model（string）:使用哪一个大模型
    + type（string）：定义该Agent类型，每一种类型要求对应prompt，要求Agent去扮演对应的角色
      + base:基础Agent，要求构建的时候给出对应的任务要求（主要适配单Agent，当不知道任务该如何定义时使用）
      + stream:消息流传递，主要负责消息的处理、过滤；在多Agent交互过程中主要负责消息的处理，以便更好的传递消息
      + useTool:使用某一工具或者具体操作函数，负责任务中具体工作的操作，（多Agent中对于具体任务具体操作的具体定义）
      + workflow:用于对整体任务进行分解，要求给出具体的，合乎规范的workflow{[target]、[step1,step2,...,stepn]、[output][others]}
    + function[list]:定义该Agent可以使用的函数
  + 方法
    + init:初始化定义，要求给出baseUrl,useKey,model,type
    + input：处理输入、要求符合任务要求，Agent处理工作要求
    + run:调用该Agent，给出输入、历史消息；输出返回所调用大模型的消息
    + output:处理Agent调用的消息以便存储、输出、处理
+ Action
> Agent使用函数的定义，适配于具体任务具体工作的具体定义;该函数不需要定义死，可以作为选择性的文件放在code里面
  + 属性
    + type:该方法属于哪一个Agent
  + 方法
+ Interaction
> 该类定义多Agent之间的交互方式，要求有最基本的定义，可扩展
  + 属性
    + task:任务类型，要求对于多智能体交互任务要有最基本的定义，方便prompt的构建
    + workflow[list]：要求明确任务所划分的所有子任务，给出具体的输入、输出要求格式
    + subTask:当前agent需要处理的任务
  + 方法
    + chooseAgent：选择相关的Agent（下一个要交互的Agent）
    + chooseMseeage:选择所需要使用的信息
    + messageStore：存储相关的历史信息
    + 
+ Memory
> 该类定义Agent交互之间的历史消息，协助通信相关动作
  + 属性
    + address：信息存储位置，信息存储方式应该根据不同的任务要求定义不同格式，不同的任务要求文件的排列格式不同
    + type：属于历史信息、传递消息、prompt操作
  + 方法
    + getData：获得所需要的数据
    + inputData：对数据进行处理操作,作为即将使用的数据输入
    + output：对数据进行处理，作为即将存储的数据
    + storeData:存储相关的数据