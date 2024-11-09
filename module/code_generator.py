from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from module.types import SUMMARY_TEMPLATE

class CodeGenerator():
    def __init__(self, request):
        self.request = request

    def _generate_code(self) -> str:
        """
        This method generate code for given query.
        """
        summary_prompt_template = PromptTemplate(input_variables=["text"], template=SUMMARY_TEMPLATE)

        llm = ChatOllama(model="smollm:135m")
        print("Model loaded sucessfully")
        # define chain
        chain = summary_prompt_template | llm | StrOutputParser()
        # invoke chain
        response = chain.invoke(input={"text": self.request})
        return response
    