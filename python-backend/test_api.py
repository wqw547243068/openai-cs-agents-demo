from agents import Agent, Runner

from load_env import base_url, api_key, model_name
from openai import AsyncOpenAI
# NameError: name 'set_default_openai_client' is not defined
from agents import set_default_openai_client, set_default_openai_api, set_tracing_disabled

custom_client = AsyncOpenAI(
	base_url=base_url,
	api_key=api_key,
)
set_default_openai_client(client=custom_client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)


agent = Agent(name="Assistant", model=model_name,instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "你好.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.

