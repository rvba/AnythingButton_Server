from pydantic import BaseModel
from huggingface_hub import InferenceClient
import os
from agent import Agent

huggingface_token = os.getenv("HF_TOKEN")


client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1", token=huggingface_token)


def format_prompt(message, history):
    prompt = "<s>"
    for user_prompt, bot_response in history:
        prompt += f"[INST] {user_prompt} [/INST]"
        prompt += f" {bot_response}</s> "
    prompt += f"[INST] {message} [/INST]"
    return prompt

def generate(agent: Agent):
    temperature = float(agent.temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(agent.top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=agent.max_new_tokens,
        top_p=top_p,
        repetition_penalty=agent.repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(f"{agent.system_prompt}, {agent.prompt}", agent.history)
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
    return output