from pydantic import BaseModel
from huggingface_hub import InferenceClient
import os
from agent import Agent

huggingface_token = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="novita",
    api_key=huggingface_token,
)


def format_prompt(message, history):
    prompt = "<s>"
    for user_prompt, bot_response in history:
        prompt += f"{user_prompt} "
        prompt += f"\n{bot_response}"
    prompt += f"{message}<think>\n"
    return prompt

def generate(agent: Agent):
    # temperature = float(agent.temperature)
    # if temperature < 0.5:
    #     temperature = 0.5
    # top_p = float(agent.top_p)

    # generate_kwargs = dict(
    #     temperature=temperature,
    #     max_new_tokens=agent.max_new_tokens,
    #     top_p=top_p,
    #     repetition_penalty=agent.repetition_penalty,
    #     do_sample=True,
    #     seed=42,
    # )

    formatted_prompt = format_prompt(f"{agent.system_prompt}\n {agent.prompt}", agent.history)

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            {
                "role": "user",
                "content": formatted_prompt
            }
        ],
    )

    # print(completion.choices[0].message)

    # stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    # output = ""

    # for response in stream:
    #     output += response.token.text
    output = completion.choices[0].message["content"]
    return output