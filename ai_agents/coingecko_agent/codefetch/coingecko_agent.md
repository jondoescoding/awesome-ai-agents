```
Project Structure:
├── codefetch
├── coin_gecko_agent.py
├── README.md
├── requirements.txt
└── tools.py
```

coin_gecko_agent.py
```
1 | ####
2 | # IMPORTS
3 | ####
4 | 
5 | # Python Built In Libraries
6 | from typing import Annotated # used to set additional metadata for a variable  
7 | from typing_extensions import TypedDict # a type that allows you to define dictionaries with specific key-value types
8 | 
9 | # Langchain / Langraph
10 | from langgraph.graph import StateGraph, START
11 | from langgraph.graph.message import add_messages
12 | from langgraph.prebuilt import ToolNode, tools_condition
13 | from langchain_groq import ChatGroq
14 | 
15 | # Local Imports
16 | from tools import get_trending_tokens, search
17 | 
18 | ####
19 | # UI - Streamlit I
20 | ####
21 | import streamlit as st
22 | 
23 | with st.sidebar:
24 |     groq_api_key = st.text_input("Groq API Key", key="chatbot_api_key", type="password")
25 |     "[Get an Groq API key](https://console.groq.com/keys)"
26 |     "[![View the source code](https://badgen.net/static/Github/Repository/black?icon=github)](https://github.com/jondoescoding/awesome-ai-agents/tree/main/ai_agents/coingecko_agent)"
27 | 
28 | 
29 | if groq_api_key:
30 |     llm = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key)
31 | else:
32 |     st.warning(body="API key is not set. Please set the Groq API key.")
33 |     st.stop()
34 | 
35 | ####
36 | # LOGIC - LANG-GRAPH
37 | ####
38 | tools = [get_trending_tokens, search]
39 | llm_with_tools = llm.bind_tools(tools=tools) # this is to make the LLM aware of the tools it has
40 | 
41 | class State(TypedDict):
42 |     messages: Annotated[list, add_messages]
43 | 
44 | graph_builder = StateGraph(State) # the stategraph controls the structure of what our future chatbot will expect
45 | 
46 | # FUNCTIONS
47 | def chatbot(state: State):
48 |     return {"messages": [llm_with_tools.invoke(state["messages"])]} # this takes the LAST message as input and returns an updated dict list under the messages within the State class
49 | 
50 | # NODES - Unit of work in the graph
51 | tools_node = ToolNode(tools=[get_trending_tokens, search])
52 | graph_builder.add_node(
53 |     "chatbot", # name of the node
54 |     chatbot # function which is called whenever the node is used within the graph
55 | )
56 | graph_builder.add_node("tools", tools_node)
57 | graph_builder.add_conditional_edges(
58 |     "chatbot",
59 |     tools_condition,)
60 | graph_builder.add_edge("tools", "chatbot")
61 | graph_builder.add_edge(START, "chatbot") # START tells the graph where to start
62 | #graph_builder.add_edge("chatbot", END) # END tells the graph where to end
63 | graph = graph_builder.compile() # allows to graph to become runnable 
64 | 
65 | 
66 | ####
67 | # UI - Streamlit II
68 | ####
69 | st.title("🦎💬 CoinGecko Chatbot")
70 | 
71 | if "messages" not in st.session_state:
72 |     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
73 | 
74 | for msg in st.session_state.messages:
75 |     st.chat_message(msg["role"]).write(msg["content"])
76 | 
77 | if prompt := st.chat_input():
78 |     if not groq_api_key:
79 |         st.info("Please add your Groq API key to continue.")
80 |         st.stop()
81 | 
82 |     st.session_state.messages.append({"role": "user", "content": prompt})
83 |     st.chat_message("user").write(prompt)
84 |     response = graph.invoke({"messages": [("user", prompt)]})
85 |     msg = response["messages"][-1].content # pulls ONLY the AI's response from the response dict
86 |     st.session_state.messages.append({"role": "assistant", "content": msg})
87 |     st.chat_message("assistant").write(msg)
```

tools.py
```
1 | from typing import Dict, Any, Union, List
2 | from langchain_core.tools import tool
3 | from pycoingecko import CoinGeckoAPI
4 | from langchain_community.tools.tavily_search import TavilySearchResults
5 | from dotenv import load_dotenv
6 | import os
7 | 
8 | 
9 | load_dotenv()
10 | 
11 | cg = CoinGeckoAPI(demo_api_key=os.getenv('coingecko_api_key'))
12 | 
13 | os.environ["TAVILY_API_KEY"] = os.getenv('TAVILY_API_KEY')
14 | tavily_client = TavilySearchResults(max_results=2, search_depth="advanced")
15 | 
16 | @tool
17 | def search(user_query: str) -> Dict:
18 |     """
19 |     Triggered if the user asks for a web search online. The passed user query should be used to search for content online to provide context.
20 | 
21 |     Keywords: search for, search, online, web search, fetch information
22 | 
23 |     Args:
24 |         user_query: str -> The query that should be searched for online.
25 |     
26 |     Returns:
27 |         Dict[str, Any]: Responses to the user quesry which contains multiple web search results.
28 |     """
29 |     return tavily_client.invoke({"query": user_query})
30 | 
31 | @tool
32 | def get_trending_tokens() -> Dict[str, Any]:
33 |     """
34 |     This tool should be triggered if the user asks to see the trending coins from CoinGecko. 
35 | 
36 |     The tool will then output the top 7 trending tokens for the last 24 hours.
37 | 
38 |     Keywords: trending, top tokens, coingecko
39 | 
40 |     Args:
41 |         None
42 |     
43 |     Returns:
44 |         Dict[str, Any]: Cleaned dictionary containing the top 3 trending tokens data
45 |         with specified fields removed.
46 |     """
47 |     def clean_nested_data(data: Union[Dict, List, Any]) -> Union[Dict, List, Any]:
48 |         """
49 |         Recursively cleans nested data structures by removing specified fields.
50 |         
51 |         This function removes:
52 |         - Any field containing 'price_change' in its name
53 |         - The 'market_cap_1h_change' field
54 |         
55 |         Args:
56 |             data: The data structure to clean (can be a dict, list, or simple value)
57 |             
58 |         Returns:
59 |             The cleaned data structure with specified fields removed
60 |         """
61 |         # Create a list of fields we want to exclude
62 |         fields_to_exclude = [
63 |             'price_change',
64 |             'market_cap_1h_change',
65 |             'market_cap_change_percentage_24h'
66 |         ]
67 |         
68 |         # Handle dictionaries
69 |         if isinstance(data, dict):
70 |             return {
71 |                 key: clean_nested_data(value)
72 |                 for key, value in data.items()
73 |                 if not any(excluded in key.lower() for excluded in fields_to_exclude)
74 |             }
75 |         
76 |         # Handle lists
77 |         if isinstance(data, list):
78 |             return [clean_nested_data(item) for item in data]
79 |         
80 |         # Return unchanged data for other types
81 |         return data
82 | 
83 |     # Get raw data from CoinGecko
84 |     raw_data = cg.get_search_trending()
85 |     
86 |     # Create a new dictionary with only the top 3 coins
87 |     limited_data = raw_data.copy()
88 |     
89 |     # Limit the coins list to the first 3 entries while preserving other data
90 |     if 'coins' in limited_data and isinstance(limited_data['coins'], list):
91 |         limited_data['coins'] = limited_data['coins'][:1] # Only returns the "coins" section of the API
92 |     
93 |     # Clean the limited data and return it
94 |     return clean_nested_data(limited_data)
```