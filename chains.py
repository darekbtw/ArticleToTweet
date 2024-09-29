import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(model_name="llama-3.1-70b-versatile", temperature=0, groq_api_key=os.getenv('my_api_key'))
        
    def summarizeArticle(self, cleanText):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scrapted text is from a website article.
            Summarize the text above so that it is under 250 characters. Spaces and new lines count as 1 character. Treat the summary to be used as a social media post. 
            No hashtags.
            NO PREAMBLE.
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data':cleanText})
        return res.content


if __name__ == "__main__":
    chain = Chain()