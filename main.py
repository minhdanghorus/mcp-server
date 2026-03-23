import asyncio
import os

from dotenv import load_dotenv

# from langgraph.prebuilt import create_react_agent. // deprecated
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

stdio_server_params = StdioServerParameters(
    command="D:\\mcp-servers\\shellserver\\.venv\\Scripts\\python.exe",
    args=["D:\\mcp-servers\\shellserver\\servers\\math_server.py"],
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("human", "{input}"),
#     ("placeholder", "{agent_scratchpad}"),
# ])


async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")

            # LangChain Tools (Tools that LangChain can use it)
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 54 + 2 * 3?")]})
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
