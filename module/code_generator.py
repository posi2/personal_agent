from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

class CodeGenerator():
    def __init__(self, request):
        self.request = request

    def _generate_code(self, ):
        summary_template = """
          Write a function for {text} with comments and function definition.
        """
        summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)

        llm = ChatOllama(model="smollm:135m")
        print("Model loaded sucessfully")

        chain = summary_prompt_template | llm | StrOutputParser()

        response = chain.invoke(input={"text": self.request})
        return response
    