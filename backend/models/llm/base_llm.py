from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def chat_completion(self, model_name, conversation_history):
        pass