import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion 

async def analyze_conversation(conversation, totaltokens):
    kernel = sk.Kernel()  
    service_id="chat-gpt"
    

    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    service_id = "default"
    kernel.add_service(
        AzureChatCompletion(service_id=service_id, deployment_name=deployment, endpoint=endpoint, api_key=api_key),
    )
    
    plugins_directory = "prompts"

    funFunctions = kernel.import_plugin_from_prompt_directory(plugins_directory, "plugins")
    

    callFunction = funFunctions["Call"]
    
    
    result = await kernel.invoke(callFunction, sk.KernelArguments(input=conversation, total_tokens=totaltokens)) 
    return  result;  