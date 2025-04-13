from pydantic import BaseModel
class Agent(BaseModel):
    prompt: str
    history: list = ""
    system_prompt: str = ""
    temperature: float = 0.0
    max_new_tokens: int = 1048
    top_p: float = 0.15
    repetition_penalty: float = 1.0

class CodeGenAgent(Agent):
    system_prompt: str = "You are a coding agent that generates C# script based on the instructions. Return only the generated C# code and nothing else. Don't generate code not in the aforementioned language. Please don't return somthing like 'here is the C# code'. Return anything other than the C# code is considered as failure on the task, espcially reuturning part of the instructions."

class ValidationAgent(Agent):
    system_prompt: str = "You are a validation agent that is an expert is C# that checks if the code generated that complies with the generation instructions and the generared code compiles correctly. If both conditions return true, say true, otherwise returns false. Returns only true or false and nothing else, other wise is considered as failure on the task. Returns nothing is also considered as failure on the task."

class CleanupAgent(Agent):
    system_prompt: str = "You are coding agent that extracts the functioning code from the generated code. Please remove any intructions that is not compilable as prompt. Return only the functioning code and nothing else. Return your evaluation rather than the cleaned up code is considered failure on the task. Return your explaination is also considered as failure on the task."
