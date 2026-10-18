
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

def get_respnse(
        prompt:str,
        system_prompt:str =None,
        model:str ="openai/gpt-oss-120b"
)->str:
    try:
    
    
        llm=ChatGroq(model=model, timeout=30,max_retries=2)

        message=[]

        if system_prompt:

            message.append(("system",system_prompt))


        message.append(("user",prompt))

    
        res=llm.invoke(message)
        return res.content
    except Exception as e:
        print(f"There is an error :{e}")
        raise




if __name__=="__main__":
    try:
        answer=get_respnse(
            prompt="how to find the square of any number",
            system_prompt="you are a python teacher"
        
        )
    

        print(answer)
    except Exception as e:
        print(f"the response cond't been generated :{e}" )



