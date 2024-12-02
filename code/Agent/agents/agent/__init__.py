# from .agent import Agent
from registry import Registry

agent_registry = Registry(name="AgentRegistry")

from .baseAgent import BaseAgent
from .conversation import ConversationAgent

from .reflection import ReflectionAgent
