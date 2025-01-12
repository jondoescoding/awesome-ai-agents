from typing import Annotated # used to set additional metadata for a variable  

from typing_extensions import TypedDict # a type that allows you to define dictionaries with specific key-value types

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
from coingecko_tools import get_trending_tokens

load_dotenv()


llm = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("groq_api_key"))
tools = [get_trending_tokens]
llm_with_tools = llm.bind_tools(tools=tools) # this is to make the LLM aware of the tools it has

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State) # the stategraph controls the structure of what our future chatbot will expect

# FUNCTIONS
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]} # this takes the LAST message as input and returns an updated dict list under the messages within the State class

# NODES - Unit of work in the graph
tools_node = ToolNode(tools=[get_trending_tokens])
graph_builder.add_node(
    "chatbot", # name of the node
    chatbot # function which is called whenever the node is used within the graph
)
graph_builder.add_node("tools", tools_node)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot") # START tells the graph where to start
#graph_builder.add_edge("chatbot", END) # END tells the graph where to end
graph = graph_builder.compile() # allows to graph to become runnable 

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("\nAssistant:", value["messages"][-1].content)


while True:
    try:
        user_input = input("\nUser: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        print("Error retrieving data from Coin Gecko")
        # fallback if input() is not available
        #user_input = "What do you know about LangGraph?"
        #print("\nUser: " + user_input)
        #stream_graph_updates(user_input)
       #break

