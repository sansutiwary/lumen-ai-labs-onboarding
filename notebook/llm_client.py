
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from functools import lru_cache
import logging

load_dotenv()
###
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

logger=logging.getLogger(__name__)

@lru_cache(maxsize=4)
def get_llm(model:str):
    return ChatGroq(model=model, timeout=30,max_retries=3)


def get_response(
        prompt:str,
        system_prompt:str =None,
        model:str ="openai/gpt-oss-120b"
)->str:
    try:
    
    
        llm=get_llm(model)

        message=[]

        if system_prompt:

            message.append(("system",system_prompt))


        message.append(("user",prompt))

    
        res=llm.invoke(message)
        return res.content
    except Exception:
        logger.exception("LLM API request failed")
        raise




if __name__=="__main__":
    try:
        answer=get_response(
            prompt="how to find the square of any number",
            system_prompt="you are a python teacher"
        
        )
   

        print(answer)
    except Exception as e:
        print(f"the response cond't been generated :{e}" )



