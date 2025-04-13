# class Agent:
#     def __init__(self, name, role, function):
#         self.name = name
#         self.role = role
#         self.function = function
    
#     # def query_llm(self, prompt):
#     #     """Stimulates querying the LLM with a role specific prompt."""
#     #     system_prompt =  f"You are a: {self.name} Your role: {self.role} Your function: {self.function}"
#     #     full_prompt= f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
#     #     {system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
#     #     # Based on your role and function, give the modified new prompt for the following with a new prompt. 
#     #     Do not give me anything else other than the prompt:{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
#     #     return full_prompt.replace("\n", " ").replace("\\n", "")

# class TopicAgent(Agent):
#     def query_llm(self, document):
#         """Summarize the topics of the document."""
#         system_prompt = f"You are a: {self.name}. Your role:{self.role}. Your function: {self.function}"

#         full_prompt=f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
#         {system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
#         Document: {document}
#         #Take the input document and segment it into a list of topics. Incorporate as many aspects as possible from the document. Return only the topics and nothing else. Do not restate your role or task.'.<|eot_id|><|start_header_id|> assistant<|end_header_id|>"""
#         return full_prompt.replace("\n", " ").replace("\\n", "")
    

# class InstructionEnhancementAgent(Agent):
#     def query_llm(self, prompt, topics):
#         """Incorporate the topics into the task instructions."""
#         system_prompt = f"You are a: {self.name}. Your role:{self.role}. Your function: {self.function}"

#         full_prompt=f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
#         {system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
#         # Task Instruction: {prompt}
#         Input Topics: {topics}
#         # Make the task instruction more contextually specific with the input topics. Return only the improved task instruction and nothing else. Do not restate your role or task. Do not make assumptions. Mentioning any locations,names, dates, or numbers that is not in the input topic is considered a failure on the task'.<|eot_id|><|start_header_id|> assistant<|end_header_id|>"""
#         # Enrich the input prompt question with document as context to improve the specificity of the input prompt. Be thorough with the topic extraction. Ensure that all information is strictly derived from the document without assumptions. Return only the enriched prompt and nothing else. Do not restate your role or task.'.<|eot_id|><|start_header_id|> assistant<|end_header_id|>"""
#         return full_prompt.replace("\n", " ").replace("\\n", "")
    

# class ConcisionAgent(Agent):
#     def query_llm(self, prompt):
#         """Make the topic specific task instructions more concise."""
#         system_prompt = f"You are a: {self.name}. Your role:{self.role}. Your function: {self.function}"

#         full_prompt=f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
#         {system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
#         Instructions: {prompt}
#         #Take the provided instructions and make it more concise. Refine it to focus on broad categories rather than specific sub points. Do not go over 100 words.'.<|eot_id|><|start_header_id|> assistant<|end_header_id|>"""
#         return full_prompt.replace("\n", " ").replace("\\n", "")
    

# class FormatAgent(Agent):
#     def query_llm(self, prompt, prompt_template):
#         """Incorporate the concise task instructions with the prompt template"""
#         system_prompt = f"You are a: {self.name}. Your role:{self.role}. Your function: {self.function}"

#         full_prompt=f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
#         {system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
#         # Template: {prompt_template}
#         Original Task: {prompt}
#         # Modify the instructions of the template based on the original task. Do not change the template format. Do not fill in the template input surrounded by square brackets. Editing template inputs or modify its structure is considered failure on the task. Do not give me anything else other than the modified prompt template.<|eot_id|><|start_header_id|> assistant<|end_header_id|>"""
#         # Make sure the final prompt is format compliant. Only modify the lines with input elements surrounded by '[]' when it is absolutely necessary.Return the full modified prompt template after checking for adherence.<|eot_id|><|start_header_id|> assistant<|end_header_id|>
#         return full_prompt.replace("\n", " ").replace("\\n", "")
    
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