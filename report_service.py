from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
print("API Key configured:", "OPENAI_API_KEY" in os.environ)

# langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model='gpt-4o-mini')

def investment_report(symbol, company, stock):
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '''
                Want assistance provided by qualified individuals enabled with experience on understanding charts 
                using technical analysis tools while interpreting macroeconomic environment prevailing across world 
                consequently assisting customers acquire long term advantages requires clear verdicts 
                therefore seeking same through informed predictions written down precisely!
            '''),
            (
               'user', '''
                    {company}에 주식을 투자하려고 합니다. 아래의 기본 정보, 재무제표를 참고하여 마크다운 형식의 투자 보고서를 보기 깔끔하게, 투자 초보자도 이해할 수 있게 한국어로 작성하세요.
                    
                    - 기본정보 : {business_info} \n
                    - 재무제표 : {financial_statements}
                ''' 
            )
        ]
    )
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    response = chain.invoke({
        'company':company,
        'business_info': stock.get_basic_info(),
        'financial_statements': stock.get_financial_statement()
    })
    
    return response