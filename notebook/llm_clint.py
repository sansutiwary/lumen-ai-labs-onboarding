
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

def get_respnse(
        prompt:str,
        system_prompt:str =None,
        model:str ="openai/gpt-oss-120b"
)->str:
    
    
    llm=ChatGroq(model=model)

    message=[]

    if system_prompt:

        message.append(("system",system_prompt))


    message.append(("user",prompt))

    res=llm.invoke(message)

    return res.content




if __name__=="__main__":
    answer=get_respnse(
        prompt="how to find the square of any number",
        system_prompt="you are a python teacher"
        
    )

    print(answer)



