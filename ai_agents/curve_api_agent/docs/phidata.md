<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/introduction</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/examples/introduction</url>
  <content>Here you’ll find examples that’ll help you use phidata, from basic **agents and workflows** to advanced **fine-tuning and evaluations**. If you have more, please [contribute](https://github.com/phidatahq/phidata-docs) to this list.

You can run each recipe individually or clone the [phidata cookbook](https://github.com/phidatahq/phidata/tree/main/cookbook) and run it from there.

[​](#agents)

Agents
----------------------

[

Web Search
----------

An Agent that can search the web.



](https://docs.phidata.com/examples/agents/web-search)[

Recipe Creator Agent
--------------------

An Agent that can recommend recipes.



](https://docs.phidata.com/examples/agents/recipe-creator-agent)[

Finance Agent
-------------

An Agent that can analyze financial data.



](https://docs.phidata.com/examples/agents/finance-agent)[

Books Recommendation Agent
--------------------------

An Agent that gives personalised book recommendations to read.



](https://docs.phidata.com/examples/agents/books-recommendation-agent)[

Shopping Agent
--------------

An Agent that helps you shop online.



](https://docs.phidata.com/examples/agents/shopping-partner-agent)[

Weekend Planner Agent
---------------------

An Agent to plan out your weekend with fun activities.



](https://docs.phidata.com/examples/agents/timeout-agent)[

Agent Team
----------

A Team of Agents that can work together.



](https://docs.phidata.com/examples/agents/agent-team)[

Reasoning Agent
---------------

An Agent that can reason and provide a step-by-step solution.



](https://docs.phidata.com/examples/agents/reasoning-agent)[

Python Agent
------------

An Agent that can write and run python code.



](https://docs.phidata.com/examples/agents/python-agent)[

Data Analyst
------------

An Agent that can analyze data using DuckDB.



](https://docs.phidata.com/examples/agents/data-analyst)[

Structured Output
-----------------

An Agent that can respond with pydantic objects.



](https://docs.phidata.com/examples/agents/structured-output)[

Python Function Agent
---------------------

An Agent that can call python functions.



](https://docs.phidata.com/examples/agents/python-function-as-tool)[

Image Agent
-----------

An Agent that can use an image as input.



](https://docs.phidata.com/examples/agents/image-agent)[

Generate Image Agent
--------------------

An Agent that can generate an image.



](https://docs.phidata.com/examples/agents/generate-image-agent)[

Cal.com Agent
-------------

An Agent that can use Cal.com to schedule meetings.



](https://docs.phidata.com/examples/agents/calcom-agent)[

Image to Text Agent
-------------------

An Agent that takes an input image and generates results.



](https://docs.phidata.com/examples/agents/image-to-text)[

Research Agent
--------------

An Agent that can research and write articles.



](https://docs.phidata.com/examples/agents/research-agent)[

ModelsLabs Agent
----------------

An Agent that can generate videos using ModelsLabs.



](https://docs.phidata.com/examples/agents/models-labs-agent)[

Slack Agent
-----------

An Agent that can interact with Slack.



](https://docs.phidata.com/examples/agents/slack-agent)[

Discord Agent
-------------

An Agent that can interact with Discord.



](https://docs.phidata.com/examples/agents/discord-agent)[

Firecrawl Agent
---------------

An Agent that can search the web using Firecrawl.



](https://docs.phidata.com/examples/agents/firecrawl-agent)[

Github Agent
------------

An Agent that can interact with Github.



](https://docs.phidata.com/examples/agents/github-agent)[

RAG Agent
---------

An Agent that can use a knowledge base to answer questions.



](https://docs.phidata.com/examples/agents/rag-agent)[

Popcorn Pal Agent
-----------------

An Agent that can recommend movies.



](https://docs.phidata.com/examples/agents/popcorn-pal-agent)[

Globe Hopper Agent
------------------

An Agent that can plan travel itineraries.



](https://docs.phidata.com/examples/agents/globe-hopper-agent)[

Baidu Search Agent
------------------

An Agent that can search the web using Baidu.



](https://docs.phidata.com/examples/agents/baidu-search-agent)[

Youtube Timestamp Agent
-----------------------

An Agent that can extract the timestamps with summary from a Youtube video.



](https://docs.phidata.com/examples/agents/youtube-timestamp-agent)[

Study Scout Agent
-----------------

An Agent that can help you learn about a topic with a detailed study plan and resources.



](https://docs.phidata.com/examples/agents/study-scout-agent)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/introduction</url>
  <content>To run agents in production, we need to:

1.  Serve them using an application like **FastApi**, **Django** or **Streamlit**.
2.  Manage their sessions, memory and knowlege in a database.
3.  Monitor, evaluate and improve their performance.

Phidata not only makes building Agents easy but also provides templates that can be deployed to AWS with 1 command. Here’s how they work:

*   Create your codebase using a template: `phi ws create`
*   Run your application locally: `phi ws up`
*   Run your application on AWS: `phi ws up prd:aws`

We strongly believe that data used by AI applications should be stored securely inside your VPC.

We fully support BYOC (Bring Your Own Cloud) and encourage you to use your own AWS account.

Templates
---------

We recommend starting with the `agent-app` template and adding your own agents.</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Agent - Phidata</title>
  <url>https://docs.phidata.com/reference/agent</url>
  <content>`model``Optional[Model]``None`Model to use for this Agent (alias: "provider")`name``Optional[str]``None`Agent name`agent_id``Optional[str]``None`Agent UUID (autogenerated if not set)`agent_data``Optional[Dict[str, Any]]``None`Metadata associated with this agent`introduction``Optional[str]``None`Agent introduction. This is added to the chat history when a run is started.`user_id``Optional[str]``None`ID of the user interacting with this agent`user_data``Optional[Dict[str, Any]]``None`Metadata associated with the user interacting with this agent`session_id``Optional[str]``None`Session UUID (autogenerated if not set)`session_name``Optional[str]``None`Session name`session_data``Optional[Dict[str, Any]]``None`Metadata associated with this session`memory``AgentMemory``AgentMemory()`Agent Memory`add_history_to_messages``bool``False`Add chat history to the messages sent to the Model. (alias: "add\_chat\_history\_to\_messages")`num_history_responses``int``3`Number of historical responses to add to the messages.`knowledge``Optional[AgentKnowledge]``None`Agent Knowledge (alias: "knowledge\_base")`add_context``bool``False`Enable RAG by adding context from AgentKnowledge to the user prompt.`retriever``Optional[Callable[..., Optional[list[dict]]]]``None`Function to get context to add to the user\_message`context_format``Literal["json", "yaml"]``"json"`Format of the context`add_context_instructions``bool``False`If True, add instructions for using the context to the system prompt`storage``Optional[AgentStorage]``None`Agent Storage`tools``Optional[List[Union[Tool, Toolkit, Callable, Dict, Function]]]``None`A list of tools provided to the Model.`show_tool_calls``bool``False`Show tool calls in Agent response.`tool_call_limit``Optional[int]``None`Maximum number of tool calls allowed.`tool_choice``Optional[Union[str, Dict[str, Any]]]``None`Controls which (if any) tool is called by the model.`reasoning``bool``False`Enable reasoning by working through the problem step by step.`reasoning_model``Optional[Model]``None`Model to use for reasoning`reasoning_agent``Optional[Agent]``None`Agent to use for reasoning`reasoning_min_steps``int``1`Minimum number of reasoning steps`reasoning_max_steps``int``10`Maximum number of reasoning steps`read_chat_history``bool``False`Add a tool that allows the Model to read the chat history.`search_knowledge``bool``True`Add a tool that allows the Model to search the knowledge base (aka Agentic RAG)`update_knowledge``bool``False`Add a tool that allows the Model to update the knowledge base.`read_tool_call_history``bool``False`Add a tool that allows the Model to get the tool call history.`add_messages``Optional[List[Union[Dict, Message]]]``None`A list of extra messages added after the system message and before the user message.`system_prompt``Optional[str]``None`System prompt: provide the system prompt as a string`system_prompt_template``Optional[PromptTemplate]``None`System prompt template: provide the system prompt as a PromptTemplate`use_default_system_message``bool``True`If True, build a default system message using agent settings and use that`system_message_role``str``"system"`Role for the system message`description``Optional[str]``None`A description of the Agent that is added to the start of the system message.`task``Optional[str]``None`The task the agent should achieve.`instructions``Optional[List[str]]``None`List of instructions for the agent.`guidelines``Optional[List[str]]``None`List of guidelines for the agent.`expected_output``Optional[str]``None`Provide the expected output from the Agent.`additional_context``Optional[str]``None`Additional context added to the end of the system message.`prevent_hallucinations``bool``False`If True, add instructions to return "I dont know" when the agent does not know the answer.`prevent_prompt_leakage``bool``False`If True, add instructions to prevent prompt leakage`limit_tool_access``bool``False`If True, add instructions for limiting tool access to the default system prompt if tools are provided`markdown``bool``False`If markdown=true, add instructions to format the output using markdown`add_name_to_instructions``bool``False`If True, add the agent name to the instructions`add_datetime_to_instructions``bool``False`If True, add the current datetime to the instructions to give the agent a sense of time`user_prompt``Optional[Union[List, Dict, str]]``None`User prompt: provide the user prompt as a string`user_prompt_template``Optional[PromptTemplate]``None`User prompt template: provide the user prompt as a PromptTemplate`use_default_user_message``bool``True`If True, build a default user prompt using references and chat history`user_message_role``str``"user"`Role for the user message`response_model``Optional[Type[BaseModel]]``None`Provide a response model to get the response as a Pydantic model (alias: "output\_model")`parse_response``bool``True`If True, the response from the Model is converted into the response\_model`structured_outputs``bool``False`Use the structured\_outputs from the Model if available`save_response_to_file``Optional[str]``None`Save the response to a file`team``Optional[List["Agent"]]``None`An Agent can have a team of agents that it can transfer tasks to.`role``Optional[str]``None`When the agent is part of a team, this is the role of the agent in the team`add_transfer_instructions``bool``True`Add instructions for transferring tasks to team members`debug_mode``bool``False`debug\_mode=True enables debug logs`monitoring``bool``False`monitoring=True logs Agent information to phidata.app for monitoring`telemetry``bool``True`telemetry=True logs minimal telemetry for analytics</content>
</page>

<page>
  <title>Product updates - Phidata</title>
  <url>https://docs.phidata.com/changelog/overview</url>
  <content>Release 2.7.10
--------------

New Features:
-------------

*   **ClickUp Tool**: Added support for managing tasks on ClickUp.

Improvements:
-------------

*   **Postgres custom table schema:** Add custom table schema parameter for Postgres tools.

New Examples:
-------------

*   **LLM-OS v1:** Add a streamlit application example for LLM-OS. A application that uses an LLM with advanced operating-system level capabilities.
*   **GeoBuddy:** An AI-powered geography agent that analyzes images to predict locations based on visible cues like landmarks, architecture, and cultural symbols.

Bug Fixes:
----------

*   **Text Search Compatibility:** Resolved an issue where Text Search was not forward-compatible with recent versions.
*   **Custom Function Parsing:** Fixed an issue where function parsing for custom functions did not pass all parameters to the AI.
*   **Claude Memory Handling:** Addressed an issue in Claude where memory was not correctly handled during streaming.
*   **Gemini RepeatedComposite and other parsing issues:** Gemini messages were incompatible with memory and storage in some cases. This has been resolved.

Tools and Fixes
---------------

New Features
------------

*   **RedditTools**: Added RedditTools with cookbook examples.
*   **TelegramTools**: Introduced TelegramTools with a cookbook example.

Improvements
------------

*   **GeminiEmbedder Defaults**: Updated the defaults on the GeminiEmbedder to use a more up-to-date model and incorporate recommendations from their [docs](https://docs.phidata.com/embedder/gemini#params)

Bug Fixes:
----------

*   **Playground Imports**: Fixed imports of `docx` being required for using the playground.
*   **AzureOpenAI Compatibility**: Resolved compatibility issues with AzureOpenAIEmbedder and AzureOpenAIChat.
*   **SlackTool Exceptions**: Fixed cases where SlackTool threw an exception when the “user” field was blank or not available.
*   **Response Models**: Fixed cases where Response Models didn’t work with `show_tool_calls`, ensuring the response model is used if one is available.
*   **Claude Memory Blocks**: Fixed an issue where memory blocks in raw Claude fromat with TextBlock, etc.
*   **Model Switching**: Fixed cases where switching models from ChatGPT to Gemini with the same history caused issues.

Support for OpenAI o1
---------------------

New Features:
-------------

*   Google Calendar Tool Added

Bug Fixes:
----------

*   Fixed `get_embedding_and_usage` function of `FastEmbedEmbedder`.
*   Fixed `developer` as a role being incorrect for `OpenAILike` models.
*   Fixed `insert` function of `LanceDb` .

New Example
-----------

*   New Marketing Workflow example added

Improvements and Fixes
----------------------

This release introduces new capabilities, such as image-to-image generation, MongoDB vector support, and enhanced chunking methods, alongside significant bug fixes and usability enhancements.

### New Features:

*   **Image-to-Image Generation Support**: Extended FalTools to support image-to-image generation.
*   **MongoDB Integrations**: Added MongoDB support across agent storage, knowledge base, agent memory, and workflow storage.
*   **Download Image Utility**: Introduced a utility to download agent-generated images directly for enhanced workflows.

### Improvements:

*   **Audio Transcript Handling**: Refined the handling of audio transcripts to ensure accurate message output when processing audio files.
*   **Optimized Chunking**: Enhanced fixed and recursive chunking methods to improve document processing performance.
*   **HuggingFace Embedder**: Resolved compatibility issues with HuggingFace embedder for better reliability.
*   **Ollama Embedder**: Upgraded the Ollama embedder for more robust and efficient embedding capabilities.
*   **OpenAI o1 Model Specification Support**: Added support for OpenAI o1 model specifications, enabling compatibility with the latest OpenAI features.
*   **Spider Tool Improvements**: Addressed performance issues with the Spider tool to enhance reliability.
*   **LanceDB Enhancements**: Added support for accessing existing database tables in LanceDB.
*   **Github tool repo creation**: Added support for repo creation via the Github tool.
*   **ScrapeGraph tool addition**: Adds integration with ScrapeGraph AI for smart web scraping and markdown conversion capabilities.

### Bug Fixes:

*   **OpenAI rejecting functions with too large description**: This issue was discovered with Composio tools, but affected all tools. Resolved and made tool definitions better match JSON Schema.
*   **Google Embedder Compatibility**: Fixed an issue with Pydantic 2.10.x that caused the rejection of the Google embedder, restoring full functionality.
*   **ChromaDB Upsert Issue**: Resolved bugs that caused errors during upsert operations in ChromaDB.
*   **Async Error Messaging**: Improved error messages for unsupported async operations in models.
*   **Gemini Tool Parameters**: Fixed an issue with parameter handling in Gemini tools.

Extending Vector database support
---------------------------------

This update adds new vector database integrations, improvements to DuckDuckGo tool and Gemini model and new cookbooks.

### New Features:

*   **Cassandra Integration as a Vector Database**: Introduced support for Apache Cassandra as a Vector Database, leveraging CassIO for vector storage and retrieval.
*   **ClickHouse as a Vector Database**: Added support for ClickHouse as a Vector Database.

### Improvements

*   **DuckDuckGo Modifier**: Added a `modifier` parameter to the DuckDuckGo tool, allowing users to refine searches with site-specific queries, file type filters, and safe search toggles.
*   **Enhanced Error Handling for python-docx**: Improved error messaging for scenarios where the `python-docx` library is not installed, providing clearer guidance and smoother debugging.

### Bug Fixes

*   **Qdrant Default Embedder**: Removed OpenAI as the default embedder for Qdrant, enabling user-configurable embeddings.
*   **Gemini Import Fix**: Fixed an issue where missing OpenAI library dependencies caused errors when using Gemini.

Confluence Tool & Fixes
-----------------------

This update introduces the Confluence tool for collaboration, improves tool compatibility, and resolves deep copy issues for Ollama chat agents.

### New Features

*   **Confluence Tool**: Added a new tool using the Atlassian Confluence SDK, enabling operations such as listing pages in a space, creating and updating pages, retrieving page content by title, and getting space details.

### Improvements

*   **Tool Compatibility**: Enhanced older custom functions with manually specified descriptions and parameters to align with the updated tool-building system.

### Bug Fixes

*   **Deep Copy for Ollama Chat Agents**: Addressed an issue where manually set clients caused errors during agent model copying, ensuring all properties are properly handled.

Audio Support and Enhancements
------------------------------

This release enhances multimodal capabilities with audio support, improves session page performance, and fixes various bugs for better stability and usability.

### New Features

*   **Audio Response Support**: Added support for audio responses, enhancing multimodal interaction capabilities.
*   **Audio Generation Tools**: Integrated Eleven Labs for Audio Generation.
*   **Cohere Embedder**: Introduced a new Cohere Embedder class with a corresponding cookbook example to demonstrate its usage.
*   **File Agent Storage Support**: Added JSON and YAML as storage options for agent session data.

### Improvements

*   **Version Checker for OpenAI**: Added a warning for users with OpenAI versions below 1.52.0 to ensure compatibility with features like `audio` in `ChatCompletionMessage`.
*   **Agent Response Handling**: Enhanced processing of agent responses to support lists, improving handling of multi-item outputs.

### Bug Fixes

*   **AWS Bedrock Tool Descriptions**: Fixed an issue where the transfer tool description was missing, causing incompatibility with AWS Bedrock Claude.
*   **Response Content Handling**: Resolved crashes on the session page caused by non-string response content.
*   **Deep Copy Agent Memory**: Addressed deep copy errors when using agent memory on the playground.
*   **Session Page Enhancements**: Fixed the refresh button.
*   **Fix Tool Parsing for Ollama**: Fixed JSON schema tool parsing by transforming `['string', 'null']` parameters to `'string'` for compatibility.
*   **Response Parsing for Gemini Tool**: Improved response parsing to handle unserializable objects in `tool_calls` for Gemini on the playground.
*   **Memory Handling for Google Provider**: Fixed an issue in `monitoring_data` where memory was removed for all providers, causing blank titles on Phidata.app; now only modifies memory for Google provider.
*   **RecursiveChunking ID Conflict**: Resolved an issue in RecursiveChunking where processing large files with multiple chunks caused duplicate chunk record IDs, leading to `psycopg.errors.UniqueViolation`.

Multi-Modal Tools
-----------------

This update introduces new multimodal tools, enhances the multimodal capabilities of existing models, and includes several quality-of-life improvements.

New Features
------------

*   **Giphy Tool**: Added Giphy integration to enhance creative collaboration.
*   **Native image upload support for Claude**: Added native support for uploading images natively to the Anthropic API.
*   **Youtube Knowledge base**: Added support for new YouTube knowledge base, allowing it to be loaded directly using YouTube video links.

Improvements
------------

*   **API key validation**: Added API key validation for model classes.
*   **Gemini audio**: Improved native audio upload support for Gemini Model.
*   **YoutubeTools**: A new Youtube tool which allows generation of timestamps
*   **Workspace Configuration Flexibility**: Refactored type-checking logic using `isinstance()` to enhance flexibility and maintainability.
*   **Web Crawler Stability**: Switched to crawl4ai async to resolve issues and improve performance.
*   **Memory Optimization**: Improved memory usage in large-scale workflows for better efficiency.
*   **User Interface**: Refined the UI for better tracking of team activities.

Bug Fixes
---------

*   **Role-Based Access Control Bugs**: Resolved issues affecting access permissions.
*   **Gemini Functions**: Fixed errors when functions had no specified parameters.

Gemini Improvements
-------------------

### Improvements

*   Improvements to Gemini Multimodality.

Gemini 2 Update
---------------

### New Features

*   **Gemini Multimodal Support**: Added support for multimodal (image, video, text) input processing with Gemini.
*   **Mem0 Integration Example**: Introduced a cookbook example demonstrating Mem0 integration for Agent memory.
*   **CSV URL Knowledgebase**: Added functionality to create and manage knowledgebases from CSV URLs.

### Improvements

*   **Vertex AI Gemini 2 Update**: The Vertex AI class has been updated to support the Gemini 2 model.

### Bug Fixes

*   **Structured Output Fix**: Resolved issues with Ollama structured output to ensure consistent data formatting.

From Text to Media: A Multi-Modal Leap
--------------------------------------

This update introduces image and video multi-modal support for the agent playground and adds image and video generation tools like FAL, replicate, and ModelLabs.

### Highlights

*   **Support for video**: Agents now natively support video.
*   **Multi-Modal rendering on Agent Playground**: Agent Playground can now render images and videos.

### New Features

*   **New Tools**: Added Replicate, FAL, and ModelLabs tools to generate video and images.

### Improvements

*   Various cookbook examples were added to cover real-world agent use cases.

Enhanced Agent Visibility, RAG Improvements, and Workflow Tools
---------------------------------------------------------------

This update introduces exciting new features, performance enhancements, and crucial fixes to ensure better usability and functionality.

### Highlights

*   **Multimodal Agents**: Agents now natively support image and audio with video coming soon.
*   **Agentic Workflows are now generally available**: Build deterministic multi-agent pipelines using Workflows.
*   **Agent can share state between tool calls**: New session\_state variable allows Agents to maintain and share state across function calls.
*   **Agents in teams can respond directly to the user**: now responses of team members do not need to go through the team leader.
*   **Context Injection**: Agents can be provided context that is resolved in real-time during execution.
*   **Human-in-the-loop**: Tool calls can now be confirmed (or approved) before being executed.
*   **Advanced chunking**: Support for Semantic and Agentic chunking (and more).

### New Features

*   **Show Reasoning in the Playground**: Provides users with insights into the agent’s thought process and decision-making, offering a behind-the-scenes look at how the agent operates within the Playground.
*   **Show Tool Call in the Playground**: Display tool call results and metrics on hover within the Playground.
*   **Sessions Page Enhancements**: Added context, reasoning, and tools integration to the Sessions page.
*   **Delete Custom Endpoint for Playground**: Introduced the ability to delete endpoints directly within the Playground.
*   **Show References in the Playground**: You can now view the sources used for RAG.
*   **Chunking Strategies in RAG**: Introduced five levels of chunking strategies in RAG: Semantic Chunking, Fixed Chunking, Agentic Chunking, Document Chunking, and Recursive Chunking.
*   **Unified Reranker for Vector Databases**: Implemented a unified reranking feature across various vector databases, including LanceDB, with support for CohereReranker.
*   **Milvus Vector Database Integration**: Added support for Milvus as a vector database option.
*   **Support for Multi-Modalities**: Added support for processing audio, video, and image data to enhance agent capabilities.
*   **Context Injection**: Improved context handling to enhance agent responses and usability.
*   **Pre-hook and post-hook for function calls**: enabling users to validate arguments, add human-in-the-loop flows and validate results of tool calls.

### Improvements

*   **Duplicate Endpoint Prevention**: Enhanced endpoint creation logic to prevent duplicates.
*   **Workflow Session Logging**: Improved logging mechanisms for workflow sessions.
*   **Ollama Tool Call Streaming**: Updated the Ollama tool to improve call streaming capabilities.
*   **Logging Updates for Gemini**: Enhanced logging functionality for Gemini models.
*   **Ollama LLM Class Updates**: Resolved issues in tool calling to improve usage reliability.
*   **Product Manager Agent Workflow Example**: Added a new example to demonstrate the practical use and capabilities of workflow.
*   **Dynamic Prompt**: System prompt, user prompt and instructions can now be passed as functions resolved during run-time.

### Bug Fixes

*   **Session Read-All Fix**: Fixed an issue where titles were not created when users provided a list of messages instead of a single message.
*   **Ollama Tool Response Issue**: Addressed inconsistencies where Ollama tools always returned empty responses.

### Breaking Changes

*   **`Agent.add_context` is now `Agent.add_references`** as the context terminology is now used for context injection. Similarly, `context_format` is now `references_format`.

New Integrations
----------------

This update is packed with new integrations, significant improvements to existing tools, and crucial fixes to enhance functionality and user experience.

### New Features

*   **InternLM Support**: Added feature request integration for InternLM25.
*   **Google Vertex AI Integration**: Expanded compatibility with Google Model Vertex AI.
*   **Discord Integration Tool**: Seamlessly connect and collaborate within Discord.
*   **Baidu Search Tool**: Introducing Baidu Search integration for enhanced search capabilities in Phidata workflows.

### Improvements

*   **Agent Monitoring Sync**: Optimized synchronization between Reasoning Agent and Main Agent
*   **Knowledge Cookbooks**: Improved usability with enhanced S3, embedder, and document cookbooks; added an example using LanceDB as a vector database.
*   **License Clarifications**: Updated license for better transparency and understanding.
*   **Default Model Adjustments**: Refined the default model example for OpenAI; new guidance to avoid errors when changing models.
*   **Qwen2.5 Coding Agent**: Performance enhancements and stability improvements.
*   **Installation Improvements**: Added support for “psycopg\[binary\]” in installation commands

### Bug Fixes

*   **Phi Tool Templates**: Integrated new templates and added a comprehensive cookbook.
*   **Knowledge Base Cookbooks**: Addressed inconsistencies for a seamless experience.
*   **Context Creation**: Fixed an issue where empty contexts couldn’t be created without a knowledge base.
*   **Ollama Knowledge Example**: Resolved errors for improved functionality and reliability.</content>
</page>

<page>
  <title>Could Not Connect To Docker - Phidata</title>
  <url>https://docs.phidata.com/faq/could-not-connect-to-docker</url>
  <content>If you have Docker up and running and get the following error, please read on:

Quick fix
---------

Create the `/var/run/docker.sock` symlink using:

In 99% of the cases, this should work. If it doesnt, try:

Full details
------------

Phidata uses [docker-py](https://github.com/docker/docker-py) to run containers, and if the `/var/run/docker.sock` is missing or has incorrect permissions, it cannot connect to docker.

**To fix, please create the `/var/run/docker.sock` file using:**

If that does not work, check the permissions using `ls -l /var/run/docker.sock`.

If the `/var/run/docker.sock` does not exist, check if the `$HOME/.docker/run/docker.sock` file is missing. If its missing, please reinstall Docker.

**If none of this works and the `/var/run/docker.sock` exists:**

*   Give your user permissions to the `/var/run/docker.sock` file:

*   Give your user permissions to the docker group:

More info
---------

*   [Docker-py Issue](https://github.com/docker/docker-py/issues/3059#issuecomment-1294369344)
*   [Stackoverflow answer](https://stackoverflow.com/questions/48568172/docker-sock-permission-denied/56592277#56592277)</content>
</page>

<page>
  <title>Examples - Phidata</title>
  <url>https://docs.phidata.com/more-examples</url>
  <content>Research Agent
--------------

Let’s build a research agent to generate a report using Exa.

Agentic RAG
-----------

We were the first to pioneer Agentic RAG using our Auto-RAG paradigm. With Agentic RAG (or auto-rag), the Agent can search its knowledge base (vector db) for the specific information it needs to achieve its task, instead of always inserting the “context” into the prompt.

This saves tokens and improves response quality.

Structured Outputs
------------------

Agents can return their output in a structured format as a Pydantic model.

Create a file `structured_output.py`

Reasoning Agent
---------------

Reasoning is an experimental feature that helps agents work through a problem step-by-step, backtracking and correcting as needed.</content>
</page>

<page>
  <title>Monitoring - Phidata</title>
  <url>https://docs.phidata.com/monitoring</url>
  <content>You can set `monitoring=True` on any agent to log that agent’s sessions or set `PHI_MONITORING=true` in your environment to log all agent sessions.

Create a file `monitoring.py` with the following code:

### Authenticate with phidata

Authenticate with phidata by running the following command:

or by exporting the `PHI_API_KEY` for your workspace from [phidata.app](https://www.phidata.app/)

### Run the agent

Run the agent and view the session on [phidata.app/sessions](https://www.phidata.app/sessions)

Debugging
---------

Phidata also includes a built-in debugger that will show debug logs in the terminal. You can set `debug_mode=True` on any agent to view debug logs or set `PHI_DEBUG=true` in your environment.

Run the agent to view debug logs in the terminal:

*   [Authenticate with phidata](#authenticate-with-phidata)
*   [Run the agent](#run-the-agent)
*   [Debugging](#debugging)</content>
</page>

<page>
  <title>Agent UI - Phidata</title>
  <url>https://docs.phidata.com/agent-ui</url>
  <content>Let’s take it for a spin, create a file `playground.py`

### Authenticate with phidata

Authenticate with phidata by running the following command:

or by exporting the `PHI_API_KEY` for your workspace from [phidata.app](https://www.phidata.app/)

### Run the playground

Install dependencies and run the Agent Playground:

### View the playground

*   Open the link provided or navigate to `http://phidata.app/playground` (login required)
*   Select the `localhost:7777` endpoint and start chatting with your agents!

Demo Agents
-----------

The Agent Playground includes a few demo agents that you can test with. If you have recommendations for other agents we should build, please let us know in the [community forum](https://community.phidata.com/).</content>
</page>

<page>
  <title>Workflows - Phidata</title>
  <url>https://docs.phidata.com/workflows</url>
  <content>Workflows are deterministic, stateful, multi-agent programs that are built for production applications. They’re incredibly powerful and offer the following benefits:

*   **Full control and flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order. This is critical for reliability.
*   **Pure python**: Control the agent process using standard python. Having built 100s of AI products, no framework will give you the flexibility of pure-python.
*   **Built-in state management and caching**: Store state and cache intermediate results in a database, enabling your agents to re-use results from previous executions.

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class.
2.  Add one or more agents to the workflow.
3.  Implement your logic in the `run()` method.
4.  Cache results in the `session_state` as needed.
5.  Run the workflow using the `.run()` method.

Example: Blog Post Generator
----------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### Create the Workflow

Create a file `blog_post_generator.py`

### Run the workflow

Install libraries

Run the workflow

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.</content>
</page>

<page>
  <title>Getting Help - Phidata</title>
  <url>https://docs.phidata.com/getting-help</url>
  <content>Thank you for building with phidata. If you need help, please come chat with us on [discord](https://discord.gg/phidata) or post your questions on the [community forum](https://community.phidata.com/).

Looking for dedicated support?
------------------------------

We’ve helped many companies build AI products, the general workflow is:

1.  **Build agents** to perform tasks specific to your product.
2.  **Serve your agents** via an API and connect them to your product.
3.  **Monitor, evaluate and improve** your AI product.

We provide dedicated support and development, [book a call](https://cal.com/phidata/intro) to get started. Our prices start at **$20k/month** and we specialize in taking companies from idea to production within 3 months.</content>
</page>

<page>
  <title>Install & Upgrade - Phidata</title>
  <url>https://docs.phidata.com/how-to/install</url>
  <content>[​](#install-phidata)

Install phidata
----------------------------------------

We recommend installing `phidata` using `pip` in a python virtual environment

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install phidata

Install the latest version of `phidata`

If you encounter errors, try updating pip using `python -m pip install --upgrade pip`

* * *

[​](#upgrade-phidata)

Upgrade phidata
----------------------------------------

To upgrade `phidata`, run this inside your virtual environment

    pip install -U phidata --no-cache-dir</content>
</page>

<page>
  <title>Upgrade to v2.5.0 - Phidata</title>
  <url>https://docs.phidata.com/migration/2-5-0</url>
  <content>This guide will help you migrate your code to v2.5.0

Key Changes
-----------

1.  Constructor: `Assistant()` -> `Agent()`
2.  LLM/Model: `llm` -> `model`
3.  Knowledge Base: `knowledge_base` -> `knowledge`
4.  RunResponse: Pydantic model for string response
5.  Structured Output: Changes in how structured output is handled

Detailed Migration Steps
------------------------

### 1\. Update Import Statements

### 2\. Update Arguments

Replace `llm` with `model` and `model` with `id`.

### 3\. Update Knowledge Base

Replace `knowledge_base` with `knowledge`.

### 4\. Output model response as a string

### 5\. Handle structured outputs

Replace `output_model` with `response_model`.

If you are using OpenAI models, you can set `structured_outputs=True` to get a structured output.

*   [Key Changes](#key-changes)
*   [Detailed Migration Steps](#detailed-migration-steps)
*   [1\. Update Import Statements](#1-update-import-statements)
*   [2\. Update Arguments](#2-update-arguments)
*   [3\. Update Knowledge Base](#3-update-knowledge-base)
*   [4\. Output model response as a string](#4-output-model-response-as-a-string)
*   [5\. Handle structured outputs](#5-handle-structured-outputs)</content>
</page>

<page>
  <title>Clone Cookbook - Phidata</title>
  <url>https://docs.phidata.com/examples/how-to/use-cookbook</url>
  <content>The [phidata cookbook](https://github.com/phidatahq/phidata/tree/main/cookbook) contains in-depth examples and code. From basic **agents, function calling, structured output** to advanced **fine-tuning and evaluations**.

Clone the cookbook
------------------

Fork & clone the phidata repo

We recommend forking the [phidata](https://github.com/phidatahq/phidata) repo first so you can customize the cookbooks, and contribute your own recipes back to the repo.

Fork & clone the [phidata](https://github.com/phidatahq/phidata) repo

    git clone https://github.com/phidatahq/phidata
    

`cd` into the `phidata` directory

Create a virtual environment

Create a virtual environment with the required libraries and install the project in editable mode. You can use a helper script or run these steps manually.

Run any recipe

Set your `OPENAI_API_KEY`

Install `openai` and `duckduckgo-search`

    pip install openai duckduckgo-search
    

Run the `agents/web_search.py` recipe

    python cookbook/agents/01_web_search.py</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/_sites/docs.phidata.com/introduction#simple-and-elegant</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Web Search Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/web-search</url>
  <content>Create a file `web_search.py` with the following code:

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    
    web_agent = Agent(
        name="Web Agent",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    web_agent.print_response("Whats happening in France?", stream=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai duckduckgo-search phidata</content>
</page>

<page>
  <title>AI Recipe Creator Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/recipe-creator-agent</url>
  <content>    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    from phi.tools.exa import ExaTools
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=[
            "https://www.poshantracker.in/pdf/Awareness/MilletsRecipeBook2023_Low%20Res_V5.pdf",
            "https://www.cardiff.ac.uk/__data/assets/pdf_file/0003/123681/Recipe-Book.pdf",
        ],
        vector_db=PgVector(table_name="recipes", db_url=db_url),  # we are using PgVector here, you can also use other vector dbs
    )
    knowledge_base.load(recreate=False)
    
    recipe_agent = Agent(
        name="RecipeGenie",
        knowledge_base=knowledge_base,
        search_knowledge=True,
        tools=[ExaTools()],
        markdown=True,
        instructions=[
            "Search for recipes based on the ingredients and time available from the knowledge base.",
            "Include the exact calories, preparation time, cooking instructions, and highlight allergens for the recommended recipes.",
            "Always search exa for recipe links or tips related to the recipes apart from knowledge base.",
            "Provide a list of recipes that match the user's requirements and preferences.",
        ],
    )
    
    recipe_agent.print_response(
        "I have potatoes, tomatoes, onions, garlic, ginger, and chicken. Suggest me a quick recipe for dinner", stream=True
    )</content>
</page>

<page>
  <title>Finance Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/finance-agent</url>
  <content>Create a file `finance_agent.py` with the following code:

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.yfinance import YFinanceTools
    
    finance_agent = Agent(
        name="Finance Agent",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai yfinance phidata</content>
</page>

<page>
  <title>Books Recommendation Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/books-recommendation-agent</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.exa import ExaTools
    
    
    agent = Agent(
        description="you help user with book recommendations",
        name="Shelfie",
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You are a highly knowledgeable book recommendation agent.",
            "Your goal is to help the user discover books based on their preferences, reading history, and interests.",
            "If the user mentions a specific genre, suggest books that span both classics and modern hits.",
            "When the user mentions an author, recommend similar authors or series they may enjoy.",
            "Highlight notable accomplishments of the book, such as awards, best-seller status, or critical acclaim.",
            "Provide a short summary or teaser for each book recommended.",
            "Offer up to 5 book recommendations for each request, ensuring they are diverse and relevant.",
            "Leverage online resources like Goodreads, StoryGraph, and LibraryThing for accurate and varied suggestions.",
            "Focus on being concise, relevant, and thoughtful in your recommendations.",
        ],
        tools=[ExaTools()],
    )
    agent.print_response(
        "I really found anxious people and lessons in chemistry interesting, can you suggest me more such books"
    )</content>
</page>

<page>
  <title>Shopping Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/shopping-partner-agent</url>
  <content>    from phi.agent import Agent
    from phi.model.google import Gemini
    from phi.tools.firecrawl import FirecrawlTools
    
    agent = Agent(
        name="shopping partner",
        model=Gemini(id="gemini-2.0-flash-exp"),
        instructions=[
            "You are a product recommender agent specializing in finding products that match user preferences.",
            "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 50%.",
            "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Flipkart, Myntra, Meesho, Nike, and other reputable platforms.",
            "Verify that each product recommendation is in stock and available for purchase.",
            "Avoid suggesting counterfeit or unverified products.",
            "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response.",
            "Format the recommendations neatly and ensure clarity for ease of user understanding.",
        ],
        tools=[FirecrawlTools()],
    )
    agent.print_response(
        "I am looking for running shoes with the following preferences: Color: Black Purpose: Comfortable for long-distance running Budget: Under Rs. 10,000"
    )</content>
</page>

<page>
  <title>Weekend Planner Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/timeout-agent</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.exa import ExaTools
    
    agent = Agent(
        description="you help the user plan their weekends",
        name="TimeOut",
        model=OpenAIChat(id="gpt-4o"),
        instructions=[
            "You are a weekend planning assistant that helps users create a personalized weekend itinerary.",
            "Always mention the timeframe, location, and year provided by the user (e.g., '16–17 December 2023 in Bangalore'). Recommendations should align with the specified dates.",
            "Provide responses in these sections: Events, Activities, Dining Options.",
            "- **Events**: Include name, date, time, location, a brief description, and booking links from platforms like BookMyShow or Insider.in.",
            "- **Activities**: Suggest engaging options with estimated time required, location, and additional tips (e.g., best time to visit).",
            "- **Dining Options**: Recommend restaurants or cafés with cuisine highlights and links to platforms like Zomato or Google Maps.",
            "Ensure all recommendations are for the current or future dates relevant to the query. Avoid past events.",
            "If no specific data is available for the dates, suggest general activities or evergreen attractions in the city.",
            "Keep responses concise, clear, and formatted for easy reading.",
        ],
        tools=[ExaTools()],
    )
    agent.print_response(
        "I want to plan my coming weekend filled with fun activities and christmas themed activities in Bangalore for 21 and 22 Dec 2024."
    )</content>
</page>

<page>
  <title>Agent Team - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/agent-team</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Reasoning Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/reasoning-agent</url>
  <content>Create a file `reasoning_agent.py` with the following code:

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    
    task = (
        "Three missionaries and three cannibals need to cross a river. "
        "They have a boat that can carry up to two people at a time. "
        "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
        "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
    )
    
    reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True)
    reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai phidata
    

Run the agent

    python reasoning_agent.py</content>
</page>

<page>
  <title>Python Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/python-agent</url>
  <content>Create a file `python_agent.py` with the following code:

    from pathlib import Path
    
    from phi.agent.python import PythonAgent
    from phi.model.openai import OpenAIChat
    from phi.file.local.csv import CsvFile
    
    cwd = Path(__file__).parent.resolve()
    tmp = cwd.joinpath("tmp")
    if not tmp.exists():
        tmp.mkdir(exist_ok=True, parents=True)
    
    python_agent = PythonAgent(
        model=OpenAIChat(id="gpt-4o"),
        base_dir=tmp,
        files=[
            CsvFile(
                path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                description="Contains information about movies from IMDB.",
            )
        ],
        markdown=True,
        pip_install=True,
        show_tool_calls=True,
    )
    python_agent.print_response("What is the average rating of movies?")
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai phidata</content>
</page>

<page>
  <title>Data Analyst - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/data-analyst</url>
  <content>Create a file `data_analyst.py` with the following code:

    import json
    from phi.model.openai import OpenAIChat
    from phi.agent.duckdb import DuckDbAgent
    
    data_analyst = DuckDbAgent(
        model=OpenAIChat(model="gpt-4o"),
        semantic_model=json.dumps(
            {
                "tables": [
                    {
                        "name": "movies",
                        "description": "Contains information about movies from IMDB.",
                        "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                    }
                ]
            }
        ),
        markdown=True,
    )
    data_analyst.print_response(
        "Show me a histogram of ratings. "
        "Choose an appropriate bucket size but share how you chose it. "
        "Show me the result as a pretty ascii diagram",
        stream=True,
    )
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai duckdb phidata</content>
</page>

<page>
  <title>Structured Output - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/structured-output</url>
  <content>    from typing import List
    from rich.pretty import pprint  # noqa
    from pydantic import BaseModel, Field
    from phi.agent import Agent, RunResponse  # noqa
    from phi.model.openai import OpenAIChat
    
    
    class MovieScript(BaseModel):
        setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
        ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
        genre: str = Field(
            ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
        )
        name: str = Field(..., description="Give a name to this movie")
        characters: List[str] = Field(..., description="Name of characters for this movie.")
        storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")
    
    
    # Agent that uses JSON mode
    json_mode_agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        description="You write movie scripts.",
        response_model=MovieScript,
    )
    
    # Agent that uses structured outputs
    structured_output_agent = Agent(
        model=OpenAIChat(id="gpt-4o-2024-08-06"),
        description="You write movie scripts.",
        response_model=MovieScript,
        structured_outputs=True,
    )
    
    
    # Get the response in a variable
    # json_mode_response: RunResponse = json_mode_agent.run("New York")
    # pprint(json_mode_response.content)
    # structured_output_response: RunResponse = structured_output_agent.run("New York")
    # pprint(structured_output_response.content)
    
    json_mode_agent.print_response("New York")
    structured_output_agent.print_response("New York")</content>
</page>

<page>
  <title>Image Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/image-agent</url>
  <content>Create a file `image_agent.py` with the following code:

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        markdown=True,
    )
    
    agent.print_response(
        "What are in these images? Is there any difference between them?",
        images=[
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        ],
    )
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai phidata</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/python-function-as-tool</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Generate Image Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/generate-image-agent</url>
  <content>Create a file `generate_image_agent.py` with the following code:

    from phi.agent import Agent
    from phi.tools.dalle import Dalle
    from phi.model.openai import OpenAIChat
    
    image_agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[Dalle()],
        description="You are an AI agent that can generate images using DALL-E.",
        instructions="When the user asks you to create an image, use the `create_image` tool to create the image.",
        markdown=True,
        show_tool_calls=True,
    )
    
    image_agent.print_response("Generate an image of a white siamese cat")
    
    images = image_agent.get_images()
    if images and isinstance(images, list):
        for image_response in images:
            image_data = image_response.get("data")  # type: ignore
            if image_data:
                for image in image_data:
                    image_url = image.get("url")  # type: ignore
                    if image_url:
                        print(image_url)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai phidata
    

Run the agent

    python generate_image_agent.py
    

View the image

Open the image URL in your browser to view the image.</content>
</page>

<page>
  <title>Cal.com Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/calcom-agent</url>
  <content>    agent = Agent(
        name="Calendar Assistant",
        instructions=[
            f"You're scheduing assistant. Today is {datetime.now()}.",
            "You can help users by:",
            "- Finding available time slots",
            "- Creating new bookings",
            "- Managing existing bookings (view, reschedule, cancel) ",
            "- Getting booking details",
            "- IMPORTANT: In case of rescheduling or cancelling booking, call the get_upcoming_bookings function to get the booking uid. check available slots before making a booking for given time",
            "Always confirm important details before making bookings or changes.",
        ],
        model=OpenAIChat(id="gpt-4"),
        tools=[CalCom(user_timezone="America/New_York")],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent.print_response("What are my bookings for tomorrow?")</content>
</page>

<page>
  <title>Image to Text Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/image-to-text</url>
  <content>Create a file `image_to_text.py` with the following code:

    from pathlib import Path
    
    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        markdown=True,
    )
    
    image_path = Path(__file__).parent.joinpath("multimodal-agents.jpg")
    agent.print_response(
        "Write a 3 sentence fiction story about the image",
        images=[str(image_path)],
    )
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai phidata</content>
</page>

<page>
  <title>Research Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/research-agent</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.newspaper4k import Newspaper4k
    
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo(), Newspaper4k()],
        description="You are a senior NYT researcher writing an article on a topic.",
        instructions=[
            "For a given topic, search for the top 5 links.",
            "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
            "Analyse and prepare an NYT worthy article based on the information.",
        ],
        markdown=True,
        show_tool_calls=True,
        add_datetime_to_instructions=True,
        # debug_mode=True,
    )
    agent.print_response("Simulation theory", stream=True)</content>
</page>

<page>
  <title>ModelsLabs Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/models-labs-agent</url>
  <content>ModelsLabs is a video generation tool that allows you to generate videos based on a text prompt.

Create a file `models_labs_agent.py` with the following code:

    from phi.agent import Agent
    from phi.tools.models_labs import ModelsLabs
    
    # Create an Agent with the ModelsLabs tool
    agent = Agent(tools=[ModelsLabs()], name="ModelsLabs Agent")
    
    agent.print_response("Generate a video of a beautiful sunset over the ocean", markdown=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Set environment variables

    export MODELS_LAB_API_KEY=****
    

Run the agent

    python models_labs_agent.py
    

*   [Usage](#usage)</content>
</page>

<page>
  <title>Slack Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/slack-agent</url>
  <content>Create a file `slack_agent.py` with the following code:

    from phi.agent import Agent
    from phi.tools.slack import SlackTools
    from phi.model.openai import OpenAIChat
    
    agent = Agent(model=OpenAIChat(id="gpt-4o"), tools=[SlackTools()], show_tool_calls=True)
    
    agent.print_response("Send a warm message to the #general channel", markdown=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai slack-sdk phidata
    

Set environment variables</content>
</page>

<page>
  <title>Discord Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/discord-agent</url>
  <content>Discord is a popular messaging platform that allows you to interact with your friends, family, and colleagues.

Create a file `discord_agent.py` with the following code:

    import os
    from phi.agent import Agent
    from phi.tools.discord_tools import DiscordTools
    
    # Create an agent with Discord tools
    discord_agent = Agent(
        name="Discord Agent",
        instructions=[
            "You are a Discord bot that can perform various operations.",
            "You can send messages, read message history, manage channels, and delete messages.",
        ],
        tools=[DiscordTools()],
    )
    
    # Replace with your Discord IDs
    channel_id = "YOUR_CHANNEL_ID"
    server_id = "YOUR_SERVER_ID"
    
    # Example 1: Send a message
    discord_agent.print_response(f"Send a warm message to channel {channel_id}", stream=True)
    
    # Example 2: Get channel info
    discord_agent.print_response(f"Get information about channel {channel_id}", stream=True)
    
    # Example 3: List channels
    discord_agent.print_response(f"List all channels in server {server_id}", stream=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Set environment variables

    export DISCORD_BOT_TOKEN=****</content>
</page>

<page>
  <title>Firecrawl Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/firecrawl-agent</url>
  <content>Firecrawl is a tool that allows you to search the web using Firecrawl.

Create a file `firecrawl_agent.py` with the following code:

    from phi.agent import Agent
    from phi.tools.firecrawl import FirecrawlTools
    
    agent = Agent(tools=[FirecrawlTools(scrape=False, crawl=True)], show_tool_calls=True, markdown=True)
    agent.print_response("Summarize this https://finance.yahoo.com/")
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Set environment variables

    export FIRECRAWL_API_KEY=****
    

Run the agent

    python firecrawl_agent.py</content>
</page>

<page>
  <title>RAG Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/rag-agent</url>
  <content>RAG (Retrieval-Augmented Generation) is a technique that allows you to use a knowledge base to answer questions.

Create a file `rag_agent.py` with the following code:

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.embedder.openai import OpenAIEmbedder
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.lancedb import LanceDb, SearchType
    
    # Create a knowledge base from a PDF
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        # Use LanceDB as the vector database
        vector_db=LanceDb(
            table_name="recipes",
            uri="tmp/lancedb",
            search_type=SearchType.vector,
            embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        ),
    )
    # Comment out after first run as the knowledge base is loaded
    knowledge_base.load(recreate=False)
    
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        # Add the knowledge base to the agent
        knowledge=knowledge_base,
        show_tool_calls=True,
        markdown=True,
    )
    agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai lancedb tantivy pypdf sqlalchemy</content>
</page>

<page>
  <title>Github Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/github-agent</url>
  <content>Github is a popular code hosting platform that allows you to collaborate with your team.

Create a file `github_agent.py` with the following code:

    from phi.agent import Agent
    from phi.tools.github import GithubTools
    
    agent = Agent(
        instructions=[
            "Use your tools to answer questions about the repo: phidatahq/phidata",
            "Do not create any issues or pull requests unless explicitly asked to do so",
        ],
        tools=[GithubTools(base_url="enter_base_url_here")],
    )
    
    agent.print_response("List open pull requests", markdown=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Set environment variables

    export GITHUB_ACCESS_TOKEN=****</content>
</page>

<page>
  <title>Popcorn Pal - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/popcorn-pal-agent</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.exa import ExaTools
    
    popcorn_pal_agent = Agent(
        name="Popcorn Pal",
        tools=[
            ExaTools(),
        ],
        model=OpenAIChat(id="gpt-4o"),
        description=(
            "You are Popcorn Pal, a movie recommendation agent that searches and scrapes movie websites to provide detailed recommendations, "
            "including ratings, genres, descriptions, trailers, and upcoming releases."
        ),
        instructions=[
            "Use Exa to search for the movies.",
            "Provide results with the following details: movie title, genre, movies with good ratings, description, recommended viewing age, primary language,runtime, imdb rating and release date.",
            "Include trailers for movies similar to the recommendations and upcoming movies of the same genre or from related directors/actors.",
            "Give atleast 5 movie recommendations for each query",
            "Present the output in a well-structured markdown table for readability.",
            "Ensure all movie data is correct, especially for recent or upcoming releases.",
        ],
        markdown=True,
    )
    
    popcorn_pal_agent.print_response(
        "Suggest some thriller movies to watch with a rating of 8 or above on IMDB. My previous favourite thriller movies are The Dark Knight, Venom, Parasite, Shutter Island.",
        stream=True,
    )</content>
</page>

<page>
  <title>Globe Hopper Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/globe-hopper-agent</url>
  <content>    from phi.model.openai import OpenAIChat
    from phi.agent import Agent
    from phi.tools.exa import ExaTools
    
    globe_hopper_agent = Agent(
        name="Globe Hopper",
        model=OpenAIChat(id="gpt-4o"),
        tools=[ExaTools()],
        markdown=True,
        description="You are an expert itinerary planning agent. Your role is to assist users in creating detailed, customized travel plans tailored to their preferences and needs.",
        instructions=[
            "Use Exa to search and extract relevant data from reputable travel platforms.",
            "Collect information on flights, accommodations, local attractions, and estimated costs from these sources.",
            "Ensure that the gathered data is accurate and tailored to the user's preferences, such as destination, group size, and budget constraints.",
            "Create a clear and concise itinerary that includes: detailed day-by-day travel plan, suggested transportation and accommodation options, activity recommendations (e.g., sightseeing, dining, events), an estimated cost breakdown (covering transportation, accommodation, food, and activities).",
            "If a particular website or travel option is unavailable, provide alternatives from other trusted sources.",
            "Do not include direct links to external websites or booking platforms in the response."
        ],
    )
    
    globe_hopper_agent.print_response(
        "I want to plan an offsite for 14 people for 3 days (28th-30th March) in London within 10k dollars. Please suggest options for places to stay, activities, and co working spaces and a detailed itinerary for the 3 days with transportation and activities",
        stream=True,
    )</content>
</page>

<page>
  <title>Youtube Timestamp Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/youtube-timestamp-agent</url>
  <content>Youtube Timestamp Agent is an agent that can extract the timestamp from a Youtube video.

Create a file `youtube_timestamp_agent.py` with the following code:

youtube\_timestamp\_agent.py

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.youtube_tools import YouTubeTools
    
    agent = Agent(
        name="YouTube Timestamps Agent",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YouTubeTools()],
        show_tool_calls=True,
        instructions=[
            "You are a YouTube agent. First check the length of the video. Then get the detailed timestamps for a YouTube video corresponding to correct timestamps.",
            "Don't hallucinate timestamps.",
            "Make sure to return the timestamps in the format of `[start_time, end_time, summary]`.",
        ],
    )
    agent.print_response(
        "Get the detailed timestamps for this video https://www.youtube.com/watch?v=M5tx7VI-LFA", markdown=True
    )
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai youtube_transcript_api
    

Run the agent

    python youtube_timestamp_agent.py</content>
</page>

<page>
  <title>Baidu Search Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/baidu-search-agent</url>
  <content>**BaiduSearch** enables an Agent to perform web searches using the Baidu search engine and retrieve structured results.

Create a file `baidusearch_agent.py` with the following code:

    from phi.agent import Agent
    from phi.tools.baidusearch import BaiduSearch
    
    agent = Agent(
        tools=[BaiduSearch()],
        description="You are a search agent that helps users find the most relevant information using Baidu.",
        instructions=[
            "Given a topic by the user, respond with the 3 most relevant search results about that topic.",
            "Search for 5 results and select the top 3 unique items.",
            "Search in both English and Chinese.",
        ],
    )
    agent.print_response("What are the latest advancements in AI?", markdown=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai baidusearch pycountry
    

Run the agent

    python baidusearch_agent.py</content>
</page>

<page>
  <title>Study Scout Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/study-scout-agent</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.youtube_tools import YouTubeTools
    from phi.tools.exa import ExaTools
    
    study_partner = Agent(
        name="StudyScout",  # Fixed typo in name
        model=OpenAIChat(id="gpt-4o"),
        tools=[ExaTools(), YouTubeTools()],
        markdown=True,
        description="You are a study partner who assists users in finding resources, answering questions, and providing explanations on various topics.",
        instructions=[
            "Use Exa to search for relevant information on the given topic and verify information from multiple reliable sources.",
            "Break down complex topics into digestible chunks and provide step-by-step explanations with practical examples.",
            "Share curated learning resources including documentation, tutorials, articles, research papers, and community discussions.",
            "Recommend high-quality YouTube videos and online courses that match the user's learning style and proficiency level.",
            "Suggest hands-on projects and exercises to reinforce learning, ranging from beginner to advanced difficulty.",
            "Create personalized study plans with clear milestones, deadlines, and progress tracking.",
            "Provide tips for effective learning techniques, time management, and maintaining motivation.",
            "Recommend relevant communities, forums, and study groups for peer learning and networking.",
        ],
    )
    study_partner.print_response(
        "I want to learn about Postgres in depth. I know the basics, have 2 weeks to learn, and can spend 3 hours daily. Please share some resources and a study plan.",
        stream=True,
    )</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/workspace/introduction</url>
  <content>A phidata template creates a **Workspace**, which is just an umbrella term for your codebase.

Create new workspace
--------------------

Run `phi ws create` to create a new workspace using a phidata template

  

Setup existing workspace
------------------------

Run `phi ws setup` to setup an existing directory as a phidata workspace

Start workspace
---------------

Run `phi ws up` to create workspace resources

Stop workspace
--------------

Run `phi ws down` to delete workspace resources

Patch workspace
---------------

Run `phi ws patch` to update workspace resources

  

Restart workspace
-----------------

Run `phi ws restart` to stop resources and start them again

Command Options
---------------

### Environment (`--env`)

Use the `--env` or `-e` flag to filter the environment (dev/prd)

### Infra (`--infra`)

Use the `--infra` or `-i` flag to filter the infra (docker/aws/k8s)

### Group (`--group`)

Use the `--group` or `-g` flag to filter by resource group.

### Name (`--name`)

Use the `--name` or `-n` flag to filter by resource name

### Type (`--type`)

Use the `--type` or `-t` flag to filter by resource type.

### Dry Run (`--dry-run`)

The `--dry-run` or `-dr` flag can be used to **dry-run** the command. `phi ws up -dr` will only print resources, not create them.

### Show Debug logs (`--debug`)

Use the `--debug` or `-d` flag to show debug logs.

### Force recreate images & containers (`-f`)

Use the `--force` or `-f` flag to force recreate images & containers</content>
</page>

<page>
  <title>Workspace Settings - Phidata</title>
  <url>https://docs.phidata.com/templates/workspace/settings</url>
  <content>The `WorkspaceSettings` object, usually defined in the `workspace/settings.py` file is used to defines common settings used by your workspace apps and resources.

Its not mandatory and doesn’t serve any other purpose except to hold configuration used by workspace apps and resources. The values in the `WorkspaceSettings` object can also be set using Environment variables or a `.env` file.

Example
-------

An example `WorkspaceSettings` used by the `llm-app` template. View this file on [github](https://github.com/phidatahq/llm-app/blob/main/workspace/settings.py)

Usage
-----

Use the workspace settings to

*   Name resources
*   Get the workspace root path using `ws_settings.ws_root`

*   Hold AWS constants like `availability zone` and `subnets`</content>
</page>

<page>
  <title>Workspace Resources - Phidata</title>
  <url>https://docs.phidata.com/templates/workspace/resources</url>
  <content>The `workspace` directory in a codebase contains the resources that are created/deleted using `phi ws up`/`phi ws down`.

Any `.py` file in the `workspace` containing a `DockerResources`, `AwsResources` or `K8sResources` object can be used to define the workspace resources.

To add your own resources, just create a python file, define resources and add them to a `DockerResources`, `AwsResources` or `K8sResources` object.

Example
-------

### DockerResources

workspace/dev\_resources.py

    from phi.docker.app.fastapi import FastApi
    from phi.docker.app.postgres import PgVectorDb
    from phi.docker.app.streamlit import Streamlit
    from phi.docker.resources import DockerResources
    
    #
    # -*- Resources for the Development Environment
    #
    
    # -*- Dev image
    dev_image = DockerImage(
        ...
    )
    
    # -*- Dev database running on port 5432:5432
    dev_db = PgVectorDb(
        ...
    )
    
    # -*- Streamlit running on port 8501:8501
    dev_streamlit = Streamlit(
        ...
    )
    
    # -*- FastApi running on port 8000:8000
    dev_fastapi = FastApi(
        ...
    )
    
    # -*- Dev DockerResources
    dev_docker_resources = DockerResources(
        env=ws_settings.dev_env,
        network=ws_settings.ws_name,
        apps=[dev_db, dev_streamlit, dev_fastapi, dev_jupyter_app],
    )
    

### AwsResources

workspace/prd\_resources.py

    from phi.aws.app.fastapi import FastApi
    from phi.aws.app.streamlit import Streamlit
    from phi.aws.resources import AwsResources
    from phi.aws.resource.ecs import EcsCluster
    from phi.aws.resource.ec2 import SecurityGroup, InboundRule
    from phi.aws.resource.rds import DbInstance, DbSubnetGroup
    from phi.aws.resource.reference import AwsReference
    from phi.aws.resource.s3 import S3Bucket
    from phi.aws.resource.secret import SecretsManager
    from phi.docker.resources import DockerResources
    from phi.docker.resource.image import DockerImage
    
    #
    # -*- Resources for the Production Environment
    #
    
    # -*- Production image
    prd_image = DockerImage(
        ...
    )
    
    # -*- S3 bucket for production data
    prd_bucket = S3Bucket(
        ...
    )
    
    # -*- Secrets for production application
    prd_secret = SecretsManager(
        ...
    )
    # -*- Secrets for production database
    prd_db_secret = SecretsManager(
        ...
    )
    
    # -*- Security Group for the load balancer
    prd_lb_sg = SecurityGroup(
        ...
    )
    # -*- Security Group for the application
    prd_sg = SecurityGroup(
        ...
    )
    # -*- Security Group for the database
    prd_db_port = 5432
    prd_db_sg = SecurityGroup(
        ...
    )
    
    # -*- RDS Database Subnet Group
    prd_db_subnet_group = DbSubnetGroup(
        ...
    )
    
    # -*- RDS Database Instance
    prd_db = DbInstance(
        ...
    )
    
    # -*- Streamlit running on ECS
    prd_streamlit = Streamlit(
        ...
    )
    
    # -*- FastApi running on ECS
    prd_fastapi = FastApi(
        ...
    )
    
    # -*- Production DockerResources
    prd_docker_resources = DockerResources(
        env=ws_settings.prd_env,
        network=ws_settings.ws_name,
        resources=[prd_image],
    )
    
    # -*- Production AwsResources
    prd_aws_resources = AwsResources(
        env=ws_settings.prd_env,
        apps=[prd_streamlit, prd_fastapi],
        resources=[prd_lb_sg, prd_sg, prd_db_sg, prd_secret, prd_db_secret, prd_db_subnet_group, prd_db, prd_bucket],
    )</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/apps/introduction</url>
  <content>Apps are tools like `FastApi`, `PgVector`, `Streamlit`, `Jupyter`, `Django` that we define as python classes and run using `phi start` or `phi ws up`.

When running Apps using phidata, think of them as infrastructure as code but at a higher level of abstraction. Instead of defining containers, volumes etc. we define the application we want to run. We run **Applications as Code** instead of Infrastructure as Code.

The same `App` can run on docker, AWS (ECS) or Kubernetes (EKS). The App creates the underlying resources like LoadBalancers, Services, Deployments. As the underlying resources become more complex, the concept of Apps become more appealing.

Example
-------

Lets run a Jupyter notebook and PgVector on docker.

Copy the following contents to a file `resources.py` and run `phi start resources.py`

*   Each App is a pydantic object providing input and type validation.
*   Note how the `mount_workspace` automatically mounts the directory
*   Note how `PgVectorDb` sets the required settings and creates the volume.

While this is a simple example, these concepts become very powerful for complex applications.

Motivation
----------

Apps provide the **“Application Layer”** for our AI products.

The software we write needs to be served by an Application, and this Application needs to **run the same** locally for development and in the cloud for production. By defining **Applications as Code**, we bring the benefits of **Infrastructure as Code** to the software layer.

Defining **Applications as Code** also allows us to package “software systems” into templates. Meaning every phidata template can run locally using docker or on AWS with 1 command.

Finally, defining **Applications as python objects** means we can import them in our code like regular objects making the following code possible:

Checkout some example apps you can run on docker:

*   [PgVector](https://docs.phidata.com/examples/integrations/pgvector)
*   [Jupyter](https://docs.phidata.com/templates/apps/examples)

Defining **Applications as Code** offers many benefits, such as:

*   [Install requirements on startup](https://docs.phidata.com/templates/apps/features#install-requirements-on-startup)</content>
</page>

<page>
  <title>Examples - Phidata</title>
  <url>https://docs.phidata.com/templates/apps/examples</url>
  <content>Run PgVector on Docker
----------------------

Create a file `resources.py` with the following contents:

    from phi.docker.app.postgres import PgVectorDb
    from phi.docker.resources import DockerResources
    
    # -*- PgVector running on port 5432:5432
    vector_db = PgVectorDb(
        pg_user="ai",
        pg_password="ai",
        pg_database="ai",
        debug_mode=True,
    )
    
    # -*- DockerResources
    dev_docker_resources = DockerResources(apps=[vector_db])
    

Start resources using:

**Press Enter** to confirm and verify container status on the docker dashboard.

Run Jupyter on Docker
---------------------

A jupyter notebook is a must have for AI development. Update the `resources.py` file to:

    from os import getenv
    
    from phi.docker.app.jupyter import Jupyter
    from phi.docker.app.postgres import PgVectorDb
    from phi.docker.resources import DockerResources
    
    # -*- PgVector running on port 5432:5432
    vector_db = PgVectorDb(
        pg_user="ai",
        pg_password="ai",
        pg_database="ai",
        debug_mode=True,
    )
    
    # -*- Jupyter running on port 8888:8888
    jupyter = Jupyter(
        mount_workspace=True,
        env_vars={"OPENAI_API_KEY": getenv("OPENAI_API_KEY")},
    )
    
    # -*- DockerResources
    dev_docker_resources = DockerResources(
        apps=[vector_db, jupyter],
    )
    

Start resources using:

### View Jupyterlab UI

*   Open [localhost:8888](http://localhost:8888/) to view the Jupyterlab UI. Password: **admin**
*   The directory is automatically mounted in the notebook.

Stop resources
--------------</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/introduction</url>
  <content>Resources are the infrastructure components for your application. Similar to [Apps](https://docs.phidata.com/templates/apps/introduction), we define them as python classes and create using `phi start` or `phi ws up`.

Examples
--------

*   **Local Resources**: Docker containers and images
*   **Cloud Resources**: RDS database, S3 bucket, ECS services, task definitions, security groups
*   **Kubernetes Resources**: Services, deployments

  

Motivation
----------

Resources provide the **“Infrastructure Layer”** for our AI products. The software we write needs to be served by an Application, which in turn needs to run on an Infrastructure Resoure.

Defining **Applications as Code** and **Infrastructure as Code** allows us completely write our application as python code - providing numerous benefits like re-usability, version control, unit testing, formatting.

Phidata currently provides:

*   [Docker Resources](https://docs.phidata.com/templates/resources/docker/introduction)
*   [AWS Resources](https://docs.phidata.com/templates/resources/aws/introduction)</content>
</page>

<page>
  <title>Features - Phidata</title>
  <url>https://docs.phidata.com/templates/apps/features</url>
  <content>[​](#install-requirements-on-startup)

Install requirements on startup
------------------------------------------------------------------------

Apps can install requirements on container startup. Update the `Jupyter` app to:

resources.py

    ...
    # -*- Jupyter running on port 8888:8888
    jupyter = Jupyter(
        mount_workspace=True,
        install_requirements=True,
        requirements_file="requirements.txt",
        env_vars={"OPENAI_API_KEY": getenv("OPENAI_API_KEY")},
    )
    ...
    

Create a `requirements.txt` file in the same directory

requirements.txt

    openai
    

[​](#patch-resources)

Patch resources
----------------------------------------</content>
</page>

<page>
  <title>Building an Agent API - Phidata</title>
  <url>https://docs.phidata.com/templates/agent-api/run-local</url>
  <content>The Agent Api let’s us serve agents using a [FastApi](https://fastapi.tiangolo.com/) server and store memory and knowledge in a Postgres database. Run it locally using docker or deploy to production on AWS.

Setup
-----

Create your codebase
--------------------

Create your codebase using the `agent-api` template

This will create a folder `agent-api` with the following structure:

Serve your Agents using FastApi
-------------------------------

[FastApi](https://fastapi.tiangolo.com/) is an exceptional framework for building RestApis. Its fast, well-designed and loved by everyone using it. Most production applications are built using a front-end framework like [next.js](https://nextjs.org/) backed by a RestAPI, where FastApi shines.

Your codebase comes pre-configured with [FastApi](https://fastapi.tiangolo.com/) and [PostgreSQL](https://www.postgresql.org/), along with some sample routes. Start your workspace using:

**Press Enter** to confirm and give a few minutes for the image to download (only the first time). Verify container status and view logs on the docker dashboard.

*   Open [localhost:8000/docs](http://localhost:8000/docs) to view the API Endpoints.
*   Test the `/v1/playground/agent/run` endpoint with

Building your AI Product
------------------------

The `agent-app` comes with common endpoints that you can use to build your AI product. This API is developed in close collaboration with real AI Apps and are a great starting point.

The general workflow is:

*   Your front-end/product will call the `/v1/playground/agent/run` to run Agents.
*   Using the `session_id` returned, your product can continue and serve chats to its users.

Delete local resources
----------------------

Play around and stop the workspace using:

Next
----

Congratulations on running your AI API locally. Next Steps:

*   [Run your Agent API on AWS](https://docs.phidata.com/templates/agent-api/run-aws)
*   Read how to [update workspace settings](https://docs.phidata.com/templates/how-to/workspace-settings)
*   Read how to [create a git repository for your workspace](https://docs.phidata.com/templates/how-to/git-repo)
*   Read how to [manage the development application](https://docs.phidata.com/templates/how-to/development-app)
*   Read how to [format and validate your code](https://docs.phidata.com/templates/how-to/format-and-validate)
*   Read how to [add python libraries](https://docs.phidata.com/templates/how-to/install)
*   Chat with us on [discord](https://discord.gg/4MtYHHrgA8)

*   [Setup](#setup)
*   [Create your codebase](#create-your-codebase)
*   [Serve your Agents using FastApi](#serve-your-agents-using-fastapi)
*   [Building your AI Product](#building-your-ai-product)
*   [Delete local resources](#delete-local-resources)
*   [Next](#next)</content>
</page>

<page>
  <title>PythonAgent - Phidata</title>
  <url>https://docs.phidata.com/reference/agents/python</url>
  <content>`model``Optional[Model]``None`Model to use for this Agent (alias: "provider")`name``Optional[str]``None`Agent name`agent_id``Optional[str]``None`Agent UUID (autogenerated if not set)`agent_data``Optional[Dict[str, Any]]``None`Metadata associated with this agent`introduction``Optional[str]``None`Agent introduction. This is added to the chat history when a run is started.`user_id``Optional[str]``None`ID of the user interacting with this agent`user_data``Optional[Dict[str, Any]]``None`Metadata associated with the user interacting with this agent`session_id``Optional[str]``None`Session UUID (autogenerated if not set)`session_name``Optional[str]``None`Session name`session_data``Optional[Dict[str, Any]]``None`Metadata associated with this session`memory``AgentMemory``AgentMemory()`Agent Memory`add_history_to_messages``bool``False`Add chat history to the messages sent to the Model. (alias: "add\_chat\_history\_to\_messages")`num_history_responses``int``3`Number of historical responses to add to the messages.`knowledge``Optional[AgentKnowledge]``None`Agent Knowledge (alias: "knowledge\_base")`add_context``bool``False`Enable RAG by adding context from AgentKnowledge to the user prompt.`retriever``Optional[Callable[..., Optional[list[dict]]]]``None`Function to get context to add to the user\_message`context_format``Literal["json", "yaml"]``"json"`Format of the context`add_context_instructions``bool``False`If True, add instructions for using the context to the system prompt`storage``Optional[AgentStorage]``None`Agent Storage`tools``Optional[List[Union[Tool, Toolkit, Callable, Dict, Function]]]``None`A list of tools provided to the Model.`show_tool_calls``bool``False`Show tool calls in Agent response.`tool_call_limit``Optional[int]``None`Maximum number of tool calls allowed.`tool_choice``Optional[Union[str, Dict[str, Any]]]``None`Controls which (if any) tool is called by the model.`reasoning``bool``False`Enable reasoning by working through the problem step by step.`reasoning_model``Optional[Model]``None`Model to use for reasoning`reasoning_agent``Optional[Agent]``None`Agent to use for reasoning`reasoning_min_steps``int``1`Minimum number of reasoning steps`reasoning_max_steps``int``10`Maximum number of reasoning steps`read_chat_history``bool``False`Add a tool that allows the Model to read the chat history.`search_knowledge``bool``True`Add a tool that allows the Model to search the knowledge base (aka Agentic RAG)`update_knowledge``bool``False`Add a tool that allows the Model to update the knowledge base.`read_tool_call_history``bool``False`Add a tool that allows the Model to get the tool call history.`add_messages``Optional[List[Union[Dict, Message]]]``None`A list of extra messages added after the system message and before the user message.`system_prompt``Optional[str]``None`System prompt: provide the system prompt as a string`system_prompt_template``Optional[PromptTemplate]``None`System prompt template: provide the system prompt as a PromptTemplate`use_default_system_message``bool``True`If True, build a default system message using agent settings and use that`system_message_role``str``"system"`Role for the system message`description``Optional[str]``None`A description of the Agent that is added to the start of the system message.`task``Optional[str]``None`The task the agent should achieve.`instructions``Optional[List[str]]``None`List of instructions for the agent.`guidelines``Optional[List[str]]``None`List of guidelines for the agent.`expected_output``Optional[str]``None`Provide the expected output from the Agent.`additional_context``Optional[str]``None`Additional context added to the end of the system message.`prevent_hallucinations``bool``False`If True, add instructions to return "I dont know" when the agent does not know the answer.`prevent_prompt_leakage``bool``False`If True, add instructions to prevent prompt leakage`limit_tool_access``bool``False`If True, add instructions for limiting tool access to the default system prompt if tools are provided`markdown``bool``False`If markdown=true, add instructions to format the output using markdown`add_name_to_instructions``bool``False`If True, add the agent name to the instructions`add_datetime_to_instructions``bool``False`If True, add the current datetime to the instructions to give the agent a sense of time`user_prompt``Optional[Union[List, Dict, str]]``None`User prompt: provide the user prompt as a string`user_prompt_template``Optional[PromptTemplate]``None`User prompt template: provide the user prompt as a PromptTemplate`use_default_user_message``bool``True`If True, build a default user prompt using references and chat history`user_message_role``str``"user"`Role for the user message`response_model``Optional[Type[BaseModel]]``None`Provide a response model to get the response as a Pydantic model (alias: "output\_model")`parse_response``bool``True`If True, the response from the Model is converted into the response\_model`structured_outputs``bool``False`Use the structured\_outputs from the Model if available`save_response_to_file``Optional[str]``None`Save the response to a file`team``Optional[List["Agent"]]``None`An Agent can have a team of agents that it can transfer tasks to.`role``Optional[str]``None`When the agent is part of a team, this is the role of the agent in the team`add_transfer_instructions``bool``True`Add instructions for transferring tasks to team members`debug_mode``bool``False`debug\_mode=True enables debug logs`monitoring``bool``False`monitoring=True logs Agent information to phidata.app for monitoring`telemetry``bool``True`telemetry=True logs minimal telemetry for analytics</content>
</page>

<page>
  <title>Gemini Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/gemini#params</url>
  <content>The `GeminiEmbedder` class is used to embed text data into vectors using the Gemini API. You can get one from [here](https://ai.google.dev/aistudio).

Usage
-----

cookbook/embedders/gemini\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dimensions` | `int` | `768` | The dimensionality of the generated embeddings |
| `model` | `str` | `models/text-embedding-004` | The name of the Gemini model to use |
| `task_type` | `str` | \- | The type of task for which embeddings are being generated |
| `title` | `str` | \- | Optional title for the embedding task |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Optional dictionary of parameters for the embedding request |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Optional dictionary of parameters for the Gemini client |
| `gemini_client` | `Optional[Client]` | \- | Optional pre-configured Gemini client instance |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Building an Agent App - Phidata</title>
  <url>https://docs.phidata.com/templates/agent-app/run-local</url>
  <content>The Agent App let’s us serve agents using a [FastApi](https://fastapi.tiangolo.com/) server, test them using a [Streamlit](https://streamlit.io/) UI and store memory and knowledge in a Postgres database. Run it locally using docker or deploy to production on AWS.

Setup
-----

Create your codebase
--------------------

Create your codebase using the `agent-app` template

This will create a folder `agent-app` with the following structure:

Test your Agents using Streamlit
--------------------------------

[Streamlit](https://streamlit.io/) allows us to build micro front-ends for testing our Agents. Start the `app` using:

**Press Enter** to confirm and give a few minutes for the image to download (only the first time). Verify container status and view logs on the docker dashboard.

*   Open [localhost:8501](http://localhost:8501/) to view your AI Agent.
*   The streamlit apps are defined in the `app` folder
*   The `Agents` are defined in the `agents` folder.

Serve your Agents using FastApi
-------------------------------

Streamlit is great for building micro front-ends but any production application will be built using a front-end framework like [next.js](https://nextjs.org/) backed by a RestApi built using [FastApi](https://fastapi.tiangolo.com/).

Your Agent App comes ready-to-use with FastApi endpoints. Start the `api` using:

*   Open [localhost:8000/docs](http://localhost:8000/docs) to view the API Endpoints.
*   Test the `/v1/playground/agent/run` endpoint with

Building your AI Product
------------------------

The `agent-app` comes with common endpoints that you can use to build your AI product. This API is developed in close collaboration with real AI Apps and are a great starting point.

The general workflow is:

*   Your front-end/product will call the `/v1/playground/agent/run` to run Agents.
*   Using the `session_id` returned, your product can continue and serve chats to its users.

Delete local resources
----------------------

Play around and stop the workspace using:

or stop individual Apps using:

Next
----

Congratulations on running your AI App locally. Next Steps:

*   [Run your Agent App on AWS](https://docs.phidata.com/templates/agent-app/run-aws)
*   Read how to [update workspace settings](https://docs.phidata.com/templates/how-to/workspace-settings)
*   Read how to [create a git repository for your workspace](https://docs.phidata.com/templates/how-to/git-repo)
*   Read how to [manage the development application](https://docs.phidata.com/templates/how-to/development-app)
*   Read how to [format and validate your code](https://docs.phidata.com/templates/how-to/format-and-validate)
*   Read how to [add python libraries](https://docs.phidata.com/templates/how-to/install)
*   Chat with us on [discord](https://discord.gg/4MtYHHrgA8)</content>
</page>

<page>
  <title>Setting Environment Variables - Phidata</title>
  <url>https://docs.phidata.com/faq/environment_variables</url>
  <content>To configure your environment for applications, you may need to set environment variables. This guide provides instructions for setting environment variables in both macOS (Shell) and Windows (PowerShell and Windows Command Prompt).

macOS
-----

### Setting Environment Variables in Shell

#### Temporary Environment Variables

These environment variables will only be available in the current shell session.

To display the environment variable:

#### Permanent Environment Variables

To make environment variables persist across sessions, add them to your shell configuration file (e.g., `.bashrc`, `.bash_profile`, `.zshrc`).

For Zsh:

To display the environment variable:

Windows
-------

### Setting Environment Variables in PowerShell

#### Temporary Environment Variables

These environment variables will only be available in the current PowerShell session.

To display the environment variable:

#### Permanent Environment Variables

To make environment variables persist across sessions, add them to your PowerShell profile script (e.g., `Microsoft.PowerShell_profile.ps1`).

Add the following line to the profile script:

Save and close the file, then reload the profile:

To display the environment variable:

### Setting Environment Variables in Windows Command Prompt

#### Temporary Environment Variables

These environment variables will only be available in the current Command Prompt session.

To display the environment variable:

#### Permanent Environment Variables

To make environment variables persist across sessions, you can use the `setx` command:

Note: After setting an environment variable using `setx`, you need to restart the Command Prompt or any applications that need to read the new environment variable.

To display the environment variable in a new Command Prompt session:

By following these steps, you can effectively set and display environment variables in macOS Shell, Windows Command Prompt, and PowerShell. This will ensure your environment is properly configured for your applications.</content>
</page>

<page>
  <title>Command line authentication - Phidata</title>
  <url>https://docs.phidata.com/faq/phi-auth</url>
  <content>If you run `phi auth` and you get the error: `CLI authentication failed` or your CLI gets stuck on

It means that your CLI was not able to authenticate with your Phidata account on [phidata.app](https://phidata.app/)

The quickest fix for this is to export your `PHI_API_KEY` environment variable. You can do this by running the following command:

Your API key can be found on [phidata.app](https://phidata.app/) in the sidebar under `API Key`.

Reason for CLI authentication failure:

*   Some browsers like Safari and Brave block connection to the localhost domain. Browsers like Chrome work great with `phi auth`.</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/agents/introduction</url>
  <content>Engineers use phidata to build agents with memory, knowledge, tools and reasoning.

Example: Research Agent
-----------------------

Let’s create a research agent that can search the web, read the top links and write a report for us. We **“prompt”** the agent using `description` and `instructions`.

Capturing the Agent’s response in a variable
--------------------------------------------

While `Agent.print_response()` is useful for quick experiments, we typically want to capture the agent’s response in a variable to either pass to the frontend, another agent or use in our application. The `Agent.run()` function returns the response as a `RunResponse` object.

By default `stream=False`, set `stream=True` to return a stream of `RunResponse` objects.

RunResponse
-----------

The `Agent.run()` function returns either a `RunResponse` object or an `Iterator[RunResponse]` when `stream=True`.

### RunResponse Attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `content` | `Any` | `None` | Content of the response. |
| `content_type` | `str` | `"str"` | Specifies the data type of the content. |
| `context` | `List[MessageContext]` | `None` | The context added to the response for RAG. |
| `event` | `str` | `RunEvent.run_response.value` | Event type of the response. |
| `event_data` | `Dict[str, Any]` | `None` | Data associated with the event. |
| `messages` | `List[Message]` | `None` | A list of messages included in the response. |
| `metrics` | `Dict[str, Any]` | `None` | Usage metrics of the run. |
| `model` | `Model` | `OpenAIChat` | OpenAI model is used to run by default. |
| `run_id` | `str` | `None` | Run Id. |
| `agent_id` | `str` | `None` | Agent Id for the run. |
| `session_id` | `str` | `None` | Session Id for the run. |
| `tools` | `List[Dict[str, Any]]` | `None` | List of tools provided to the model. |
| `created_at` | `int` | \- | Unix timestamp of the response creation. |

*   [Example: Research Agent](#example-research-agent)
*   [Capturing the Agent’s response in a variable](#capturing-the-agents-response-in-a-variable)
*   [RunResponse](#runresponse)
*   [RunResponse Attributes](#runresponse-attributes)</content>
</page>

<page>
  <title>Connecting to Tableplus - Phidata</title>
  <url>https://docs.phidata.com/faq/connecting-to-tableplus</url>
  <content>If you want to inspect your pgvector container to explore your storage or knowledge base, you can use TablePlus. Follow these steps:

Step 1: Start Your `pgvector` Container
---------------------------------------

Run the following command to start a `pgvector` container locally:

*   `POSTGRES_DB=ai` sets the default database name.
*   `POSTGRES_USER=ai` and `POSTGRES_PASSWORD=ai` define the database credentials.
*   The container exposes port `5432` (mapped to `5532` on your local machine).

Step 2: Configure TablePlus
---------------------------

1.  **Open TablePlus**: Launch the TablePlus application.
2.  **Create a New Connection**: Click on the `+` icon to add a new connection.
3.  **Select `PostgreSQL`**: Choose PostgreSQL as the database type.

Fill in the following connection details:

*   **Host**: `localhost`
*   **Port**: `5532`
*   **Database**: `ai`
*   **User**: `ai`
*   **Password**: `ai`

*   [Step 1: Start Your pgvector Container](#step-1-start-your-pgvector-container)
*   [Step 2: Configure TablePlus](#step-2-configure-tableplus)</content>
</page>

<page>
  <title>Advanced Example - News Report Generator - Phidata</title>
  <url>https://docs.phidata.com/workflows/news-report-generator</url>
  <content>Let’s work through a slightly more complex example of a news report generator. We want full control over the workflow, including the ability to stream the output. We also want to cache the results of the web search and the scrape.

In this workflow, we will generate a comprehensive news report on a given topic.

1.  First we will search the web for articles on the topic:
    *   Use cached search results if available and use\_search\_cache is True.
    *   Otherwise, perform a new web search.
2.  Next we will scrape the content of each article:
    *   Use cached scraped articles if available and use\_scrape\_cache is True.
    *   Scrape new articles that aren’t in the cache.
3.  Finally we will generate the final report using the scraped article contents.

The caching mechanism is implemented using the `session_state` which is a dictionary that is persisted across workflow runs. This really helps with performance and cost.

Full Code
---------

Run the workflow
----------------

Install dependencies

Run the workflow

Test if the results are cached, run the workflow again with the same parameters.

Video
-----

Checkout the recording of the workflow running and see how the results are cached in the 2nd run.</content>
</page>

<page>
  <title>ArXiv Research Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/use-case/arxiv-research</url>
  <content>Use Cases

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/use-case/arxiv-research.mdx)

[World Building](https://docs.phidata.com/examples/use-case/worldbuilding)[Clone Cookbook](https://docs.phidata.com/examples/how-to/use-cookbook)</content>
</page>

<page>
  <title>Python Function Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/agents/python-function-agent</url>
  <content>Create a file `python_function_agent.py` with the following code:

    import json
    import httpx
    
    from phi.agent import Agent
    
    
    def get_top_hackernews_stories(num_stories: int = 10) -> str:
        """Use this function to get top stories from Hacker News.
    
        Args:
            num_stories (int): Number of stories to return. Defaults to 10.
    
        Returns:
            str: JSON string of top stories.
        """
    
        # Fetch top story IDs
        response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        story_ids = response.json()
    
        # Fetch story details
        stories = []
        for story_id in story_ids[:num_stories]:
            story_response = httpx.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
            story = story_response.json()
            if "text" in story:
                story.pop("text", None)
            stories.append(story)
        return json.dumps(stories)
    
    
    agent = Agent(tools=[get_top_hackernews_stories], show_tool_calls=True, markdown=True)
    agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Install libraries

    pip install openai phidata
    

Run the agent

    python python_function_agent.py</content>
</page>

<page>
  <title>OpenAI - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/openai</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Get your key [from OpenAI here](https://platform.openai.com/account/api-keys).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export \`OPENAI\_API\_KEY\`

    export OPENAI_API_KEY=sk-xxx
    

4

Run OpenAI Agent

    python cookbook/providers/openai/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/openai/basic.py)</content>
</page>

<page>
  <title>Format & Validate - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/format-and-validate</url>
  <content>Formatting the codebase using a set standard saves us time and mental energy. Phidata templates are pre-configured with [ruff](https://docs.astral.sh/ruff/) that you can run using a helper script or directly.

Validate
--------

Linting and Type Checking add an extra layer of protection to the codebase. We highly recommending running the validate script before pushing any changes.

Phidata templates are pre-configured with [ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy.readthedocs.io/en/stable/) that you can run using a helper script or directly. Checkout the `pyproject.toml` file for the configuration.</content>
</page>

<page>
  <title>PgVector - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/pgvector</url>
  <content>The PgVector Agent uses PgVector as Knowledge Base and Storage for the Agent.

    from phi.agent import Agent
    from phi.storage.agent.postgres import PgAgentStorage
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    agent = Agent(
        storage=PgAgentStorage(table_name="recipe_agent", db_url=db_url),
        knowledge_base=PDFUrlKnowledgeBase(
            urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
            vector_db=PgVector(table_name="recipe_documents", db_url=db_url),
        ),
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to search the knowledge base
        search_knowledge=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
    )
    # Comment out after first run
    agent.knowledge_base.load(recreate=False)  # type: ignore
    
    agent.print_response("How do I make pad thai?", markdown=True)
    

Usage
-----

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

Run PgVector

    docker run -d \
      -e POSTGRES_DB=ai \
      -e POSTGRES_USER=ai \
      -e POSTGRES_PASSWORD=ai \
      -e PGDATA=/var/lib/postgresql/data/pgdata \
      -v pgvolume:/var/lib/postgresql/data \
      -p 5532:5432 \
      --name pgvector \
      phidata/pgvector:16
    

Install libraries

    pip install -U pgvector pypdf "psycopg[binary]" sqlalchemy phidata
    

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/integrations/pgvector/agent.py)</content>
</page>

<page>
  <title>Docker - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/docker/introduction</url>
  <content>[Docker](https://docs.docker.com/get-started/overview/) is a game-changing technology that enables us to run applications locally. We package our [Apps](https://docs.phidata.com/templates/resources/docker/templates/apps/introduction) into **Containers** that include everything needed to run the application

Docker Resources
----------------

Phidata enables us to define docker resources as pydantic objects so we can build our application layer purely in python. In most cases you will not be creating the **Docker Resources** directly, instead we’ll use [Apps](https://docs.phidata.com/templates/resources/docker/templates/apps/introduction) to create the resources for us.

### Benefits

*   Define containers and images as pydantic objects with input and type validation.
*   Allows re-use and testing of resources.
*   Import them in software layer like regular python objects.
*   Package multiple resources into [Apps](https://docs.phidata.com/templates/resources/docker/templates/apps/introduction) so we can define **“Applications as Code”**.
*   Enable AI features that interact with the resource from python code.

Container
---------

The `DockerContainer` class defines a container, for example use the following code to define a container running the [whoami](https://github.com/traefik/whoami) image. Start it using `phi start resources.py`

Test it by opening [http://localhost:80](http://localhost/) or using:

The same can be defined as an `App`:

Stop resources using `phi stop resources.py`

Image
-----

The `DockerImage` class defines an image, for example use the following code create your own python image and run it in a container. Build it using `phi start resources.py`</content>
</page>

<page>
  <title>AWS Resources - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/aws/introduction</url>
  <content>AWS Resources enable us to create AWS services as pydantic objects, completing our vision of writing software, application and infrastructure code entirely in python.

Examples
--------

### S3 Bucket

Copy the following code to a file `resources.py` and run `phi start resources.py` to create a bucket called `my-bucket-885`.

Make sure to delete the bucket using `phi stop resources.py`

### Secret Manager

Copy the following code to a file `resources.py` and run `phi start resources.py` to create a secret called `my-secret`.

Read the secret in another file called `read_my_secret.py`

Run this file using `python read_my_secret.py`.

Delete the secret using `phi stop resources.py`</content>
</page>

<page>
  <title>Workspace Settings - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/workspace-settings</url>
  <content>The `WorkspaceSettings` object in the `workspace/settings.py` file defines common settings used by your apps and resources. Here are the settings we recommend updating:

### Workspace Name

The `ws_name` is used to name your apps and resources. Change it to your project or team name, for example:

*   `ws_name="booking-ai"`
*   `ws_name="reddit-ai"`
*   `ws_name="vantage-ai"`

The `ws_name` is used to name:

*   The image for your application
*   Apps like db, streamlit app and fastapi server
*   Resources like buckets, secrets and loadbalancers

Checkout the `workspace/dev_resources.py` and `workspace/prd_resources.py` file to see how its used.

Image Repository
----------------

The `image_repo` defines the repo for your image.

*   If using dockerhub it would be something like `phidata`.
*   If using ECR it would be something like `[ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com`

Checkout the `dev_image` in `workspace/dev_resources.py` and `prd_image` in `workspace/prd_resources.py` to see how its used.

Build Images
------------

Setting `build_images=True` will build images locally when running `phi ws up dev:docker` or `phi ws up prd:docker`.

Checkout the `dev_image` in `workspace/dev_resources.py` and `prd_image` in `workspace/prd_resources.py` to see how its used.

Read more about:

*   [Building your development image](https://docs.phidata.com/templates/how-to/development-app#build-your-development-image)
*   [Building your production image](https://docs.phidata.com/templates/how-to/production-app#build-your-production-image)

Push Images
-----------

Setting `push_images=True` will push images after building when running `phi ws up dev:docker` or `phi ws up prd:docker`.

Checkout the `dev_image` in `workspace/dev_resources.py` and `prd_image` in `workspace/prd_resources.py` to see how its used.

Read more about:

*   [Building your development image](https://docs.phidata.com/templates/how-to/development-app#build-your-development-image)
*   [Building your production image](https://docs.phidata.com/templates/how-to/production-app#build-your-production-image)

AWS Settings
------------

The `aws_region` and `subnet_ids` provide values used for creating production resources. Checkout the `workspace/prd_resources.py` file to see how its used.

*   [Workspace Name](#workspace-name)
*   [Image Repository](#image-repository)
*   [Build Images](#build-images)
*   [Push Images](#push-images)
*   [AWS Settings](#aws-settings)</content>
</page>

<page>
  <title>Run on AWS - Phidata</title>
  <url>https://docs.phidata.com/templates/agent-api/run-aws</url>
  <content>Let’s run the **Agent API** in production on AWS.

AWS Setup
---------

Update Credentials

To run on AWS, you need **one** of the following:

1.  The `~/.aws/credentials` file with your AWS credentials
2.  **or** `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` environment variables

To create the credentials file, install the [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and run `aws configure`

Update region and subnets

Add 2 [subnets](https://us-east-1.console.aws.amazon.com/vpc/home?#subnets:) to the `workspace/settings.py` file (required for ECS services)

    ws_settings = WorkspaceSettings(
        ...
        # -*- AWS settings
        # Add your Subnet IDs here
        subnet_ids=["subnet-xyz", "subnet-xyz"],
        ...
    )
    

Please check that the subnets belong to the selected `aws_region`

Update Secrets
--------------

RDS database password

Update the RDS database password in `workspace/secrets/prd_db_secrets.yml`

workspace/secrets/prd\_db\_secrets.yml

    # Secrets used by prd RDS database
    MASTER_USERNAME: api
    MASTER_USER_PASSWORD: "api9999!!"
    

API Secrets

Add any other secrets used by your api to `workspace/secrets/prd_api_secrets.yml`

workspace/secrets/prd\_api\_secrets.yml

    SECRET_KEY: "very_secret"
    # OPENAI_API_KEY: "sk-***"
    

Create AWS resources
--------------------

Create AWS resources using:

This will create:

1.  [ECS Cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html) for the application.
2.  [ECS Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) and [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) that run the application on the ECS cluster.
3.  [LoadBalancer](https://aws.amazon.com/elasticloadbalancing/) to route traffic to the application.
4.  [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) that control incoming and outgoing traffic.
5.  [Secrets](https://aws.amazon.com/secrets-manager/) for managing application and database secrets.
6.  [RDS Database](https://aws.amazon.com/rds/) for Knowledge Base and Storage.

**Press Enter** to confirm and grab a cup of coffee while the resources spin up.

*   The RDS database takes about 5 minutes to activate.
*   These resources are defined in the `workspace/prd_resources.py` file.
*   Use the [ECS console](https://us-east-1.console.aws.amazon.com/ecs/v2/clusters) to view services and logs.
*   Use the [RDS console](https://us-east-1.console.aws.amazon.com/rds/home?#databases:) to view the database instance.

Production FastApi
------------------

*   **Open the LoadBalancer DNS** + the `/docs` endpoint to view the API Endpoints.
*   Test the `/v1/playground/agent/run` endpoint with

    {
      "message": "howdy",
      "agent_id": "example-agent",
      "stream": true
    }
    

Updating Production
-------------------

Follow [this guide](https://docs.phidata.com/templates/agent-api/templates/how-to/production-app) to update your production application. You'll need to:

1.  Create a new image
2.  Update the ECS task definition and services.

Delete AWS resources
--------------------

Play around and then delete AWS resources using:

or delete individual resource groups using:

Next
----

Congratulations on running your Agent API on AWS. Next Steps:

*   Read how to [update workspace settings](https://docs.phidata.com/templates/how-to/workspace-settings)
*   Read how to [create a git repository for your workspace](https://docs.phidata.com/templates/how-to/git-repo)
*   Read how to [manage the production application](https://docs.phidata.com/templates/how-to/production-app)
*   Read how to [format and validate your code](https://docs.phidata.com/templates/how-to/format-and-validate)
*   Read how to [add python libraries](https://docs.phidata.com/templates/how-to/install)
*   Read how to [add a custom domain and HTTPS](https://docs.phidata.com/templates/how-to/domain-https)
*   Read how to [implement CI/CD](https://docs.phidata.com/templates/how-to/ci-cd)
*   Chat with us on [discord](https://discord.gg/4MtYHHrgA8)</content>
</page>

<page>
  <title>Create Git Repo - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/git-repo</url>
  <content>Create a git repository to share your application with your team.

1

Create a git repository

Create a new [git repository](https://github.com/new).

2

Push your code

Push your code to the git repository.

terminal

    git init
    git add .
    git commit -m "Init LLM App"
    git branch -M main
    git remote add origin https://github.com/[YOUR_GIT_REPO].git
    git push -u origin main
    

3

Ask your team to join

Ask your team to follow the [setup steps for new users](https://docs.phidata.com/templates/how-to/templates/how-to/new-users) to use this workspace.</content>
</page>

<page>
  <title>Development Application - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/development-app</url>
  <content>Your development application runs locally on docker and its resources are defined in the `workspace/dev_resources.py` file. This guide shows how to:

1.  [Build a development image](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/development-app#build-your-development-image)
2.  [Restart all docker containers](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/development-app#restart-all-containers)
3.  [Recreate development resources](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/development-app#recreate-development-resources)

Workspace Settings
------------------

The `WorkspaceSettings` object in the `workspace/settings.py` file defines common settings used by your workspace apps and resources.

Build your development image
----------------------------

Your application uses the `phidata` images by default. To use your own image:

*   Open `workspace/settings.py` file
*   Update the `image_repo` to your image repository
*   Set `build_images=True`

### Build a new image

Build the development image using:

To `force` rebuild images, use the `--force` or `-f` flag

* * *

Restart all containers
----------------------

Restart all docker containers using:

* * *

Recreate development resources
------------------------------

To recreate all dev resources, use the `--force` flag:

*   [Workspace Settings](#workspace-settings)
*   [Build your development image](#build-your-development-image)
*   [Build a new image](#build-a-new-image)
*   [Restart all containers](#restart-all-containers)
*   [Recreate development resources](#recreate-development-resources)</content>
</page>

<page>
  <title>Install & Setup - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/install</url>
  <content>Install phidata
---------------

We highly recommend:

*   Installing `phidata` using `pip` in a python virtual environment.
*   Creating an `ai` directory for your ai workspaces

Create a virtual environment

Open the `Terminal` and create an `ai` directory with a python virtual environment.

Install phidata

Install `phidata` using pip

  

If you encounter errors, try updating pip using `python -m pip install --upgrade pip`

* * *

Upgrade phidata
---------------

To upgrade `phidata`, run this in your virtual environment

    pip install -U phidata --no-cache-dir
    

* * *

Setup workspace
---------------

If you have an existing `phidata` workspace, set it up using

* * *

Reset phidata
-------------

To reset the phidata config, run

This does not delete any physical data</content>
</page>

<page>
  <title>Run on AWS - Phidata</title>
  <url>https://docs.phidata.com/templates/agent-app/run-aws</url>
  <content>Let’s run the **Agent App** in production on AWS.

AWS Setup
---------

Update Secrets
--------------

Create AWS resources
--------------------

Create AWS resources using:

This will create:

1.  [ECS Cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html) for the application.
2.  [ECS Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) and [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) that run the application on the ECS cluster.
3.  [LoadBalancer](https://aws.amazon.com/elasticloadbalancing/) to route traffic to the application.
4.  [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) that control incoming and outgoing traffic.
5.  [Secrets](https://aws.amazon.com/secrets-manager/) for managing application and database secrets.
6.  [RDS Database](https://aws.amazon.com/rds/) for Knowledge Base and Storage.

**Press Enter** to confirm and grab a cup of coffee while the resources spin up.

*   The RDS database takes about 5 minutes to activate.
*   These resources are defined in the `workspace/prd_resources.py` file.
*   Use the [ECS console](https://us-east-1.console.aws.amazon.com/ecs/v2/clusters) to view services and logs.
*   Use the [RDS console](https://us-east-1.console.aws.amazon.com/rds/home?#databases:) to view the database instance.

Production Streamlit
--------------------

**Open the LoadBalancer DNS** provided when creating the Streamlit App

*   Enter the `APP_PASSWORD` from the `prd_app_secrets.yml` file (default: `admin`)
*   Enter a username and test your AI Agent.

Production FastApi
------------------

*   **Open the LoadBalancer DNS** + the `/docs` endpoint to view the API Endpoints.
*   Test the `/v1/playground/agent/run` endpoint with

Updating Production
-------------------

Follow [this guide](https://docs.phidata.com/templates/agent-app/templates/how-to/production-app) to update your production application. You'll need to:

1.  Create a new image
2.  Update the ECS task definition and services.

Delete AWS resources
--------------------

Play around and then delete AWS resources using:

or delete individual resource groups using:

Next
----

Congratulations on running your Agent App on AWS. Next Steps:

*   Read how to [update workspace settings](https://docs.phidata.com/templates/how-to/workspace-settings)
*   Read how to [create a git repository for your workspace](https://docs.phidata.com/templates/how-to/git-repo)
*   Read how to [manage the production application](https://docs.phidata.com/templates/how-to/production-app)
*   Read how to [format and validate your code](https://docs.phidata.com/templates/how-to/format-and-validate)
*   Read how to [add python libraries](https://docs.phidata.com/templates/how-to/install)
*   Read how to [add a custom domain and HTTPS](https://docs.phidata.com/templates/how-to/domain-https)
*   Read how to [implement CI/CD](https://docs.phidata.com/templates/how-to/ci-cd)
*   Chat with us on [discord](https://discord.gg/4MtYHHrgA8)

*   [AWS Setup](#aws-setup)
*   [Update Secrets](#update-secrets)
*   [Create AWS resources](#create-aws-resources)
*   [Production Streamlit](#production-streamlit)
*   [Production FastApi](#production-fastapi)
*   [Updating Production](#updating-production)
*   [Delete AWS resources](#delete-aws-resources)
*   [Next](#next)</content>
</page>

<page>
  <title>DuckDb Agent - Phidata</title>
  <url>https://docs.phidata.com/reference/agents/duckdb</url>
  <content>`model``Optional[Model]``None`Model to use for this Agent (alias: "provider")`name``Optional[str]``None`Agent name`agent_id``Optional[str]``None`Agent UUID (autogenerated if not set)`agent_data``Optional[Dict[str, Any]]``None`Metadata associated with this agent`introduction``Optional[str]``None`Agent introduction. This is added to the chat history when a run is started.`user_id``Optional[str]``None`ID of the user interacting with this agent`user_data``Optional[Dict[str, Any]]``None`Metadata associated with the user interacting with this agent`session_id``Optional[str]``None`Session UUID (autogenerated if not set)`session_name``Optional[str]``None`Session name`session_data``Optional[Dict[str, Any]]``None`Metadata associated with this session`memory``AgentMemory``AgentMemory()`Agent Memory`add_history_to_messages``bool``False`Add chat history to the messages sent to the Model. (alias: "add\_chat\_history\_to\_messages")`num_history_responses``int``3`Number of historical responses to add to the messages.`knowledge``Optional[AgentKnowledge]``None`Agent Knowledge (alias: "knowledge\_base")`add_context``bool``False`Enable RAG by adding context from AgentKnowledge to the user prompt.`retriever``Optional[Callable[..., Optional[list[dict]]]]``None`Function to get context to add to the user\_message`context_format``Literal["json", "yaml"]``"json"`Format of the context`add_context_instructions``bool``False`If True, add instructions for using the context to the system prompt`storage``Optional[AgentStorage]``None`Agent Storage`tools``Optional[List[Union[Tool, Toolkit, Callable, Dict, Function]]]``None`A list of tools provided to the Model.`show_tool_calls``bool``False`Show tool calls in Agent response.`tool_call_limit``Optional[int]``None`Maximum number of tool calls allowed.`tool_choice``Optional[Union[str, Dict[str, Any]]]``None`Controls which (if any) tool is called by the model.`reasoning``bool``False`Enable reasoning by working through the problem step by step.`reasoning_model``Optional[Model]``None`Model to use for reasoning`reasoning_agent``Optional[Agent]``None`Agent to use for reasoning`reasoning_min_steps``int``1`Minimum number of reasoning steps`reasoning_max_steps``int``10`Maximum number of reasoning steps`read_chat_history``bool``False`Add a tool that allows the Model to read the chat history.`search_knowledge``bool``True`Add a tool that allows the Model to search the knowledge base (aka Agentic RAG)`update_knowledge``bool``False`Add a tool that allows the Model to update the knowledge base.`read_tool_call_history``bool``False`Add a tool that allows the Model to get the tool call history.`add_messages``Optional[List[Union[Dict, Message]]]``None`A list of extra messages added after the system message and before the user message.`system_prompt``Optional[str]``None`System prompt: provide the system prompt as a string`system_prompt_template``Optional[PromptTemplate]``None`System prompt template: provide the system prompt as a PromptTemplate`use_default_system_message``bool``True`If True, build a default system message using agent settings and use that`system_message_role``str``"system"`Role for the system message`description``Optional[str]``None`A description of the Agent that is added to the start of the system message.`task``Optional[str]``None`The task the agent should achieve.`instructions``Optional[List[str]]``None`List of instructions for the agent.`guidelines``Optional[List[str]]``None`List of guidelines for the agent.`expected_output``Optional[str]``None`Provide the expected output from the Agent.`additional_context``Optional[str]``None`Additional context added to the end of the system message.`prevent_hallucinations``bool``False`If True, add instructions to return "I dont know" when the agent does not know the answer.`prevent_prompt_leakage``bool``False`If True, add instructions to prevent prompt leakage`limit_tool_access``bool``False`If True, add instructions for limiting tool access to the default system prompt if tools are provided`markdown``bool``False`If markdown=true, add instructions to format the output using markdown`add_name_to_instructions``bool``False`If True, add the agent name to the instructions`add_datetime_to_instructions``bool``False`If True, add the current datetime to the instructions to give the agent a sense of time`user_prompt``Optional[Union[List, Dict, str]]``None`User prompt: provide the user prompt as a string`user_prompt_template``Optional[PromptTemplate]``None`User prompt template: provide the user prompt as a PromptTemplate`use_default_user_message``bool``True`If True, build a default user prompt using references and chat history`user_message_role``str``"user"`Role for the user message`response_model``Optional[Type[BaseModel]]``None`Provide a response model to get the response as a Pydantic model (alias: "output\_model")`parse_response``bool``True`If True, the response from the Model is converted into the response\_model`structured_outputs``bool``False`Use the structured\_outputs from the Model if available`save_response_to_file``Optional[str]``None`Save the response to a file`team``Optional[List["Agent"]]``None`An Agent can have a team of agents that it can transfer tasks to.`role``Optional[str]``None`When the agent is part of a team, this is the role of the agent in the team`add_transfer_instructions``bool``True`Add instructions for transferring tasks to team members`debug_mode``bool``False`debug\_mode=True enables debug logs`monitoring``bool``False`monitoring=True logs Agent information to phidata.app for monitoring`telemetry``bool``True`telemetry=True logs minimal telemetry for analytics</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/embedder/introduction</url>
  <content>An Embedder converts complex information into vector representations, allowing it to be stored in a vector database. By transforming data into embeddings, the embedder enables efficient searching and retrieval of contextually relevant information. This process enhances the responses of language models by providing them with the necessary business context, ensuring they are context-aware. Phidata uses `OpenAIEmbedder` as the default embedder, but other embedders are supported as well. Here is an example:

The following embedders are supported:

*   [OpenAI](https://docs.phidata.com/embedder/openai)
*   [Gemini](https://docs.phidata.com/embedder/gemini)
*   [Ollama](https://docs.phidata.com/embedder/ollama)
*   [Voyage AI](https://docs.phidata.com/embedder/voyageai)
*   [Azure OpenAI](https://docs.phidata.com/embedder/azure_openai)
*   [Mistral](https://docs.phidata.com/embedder/mistral)
*   [Fireworks](https://docs.phidata.com/embedder/fireworks)
*   [Together](https://docs.phidata.com/embedder/together)
*   [HuggingFace](https://docs.phidata.com/embedder/huggingface)
*   [Qdrant FastEmbed](https://docs.phidata.com/embedder/qdrant_fastembed)</content>
</page>

<page>
  <title>OpenAI Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/openai</url>
  <content>Phidata uses `OpenAIEmbedder` as the default embeder for the vector database. The `OpenAIEmbedder` class is used to embed text data into vectors using the OpenAI API. Get your key from [here](https://platform.openai.com/api-keys).

Usage
-----

cookbook/embedders/openai\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"text-embedding-ada-002"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `1536` | The dimensionality of the embeddings generated by the model. |
| `encoding_format` | `Literal['float', 'base64']` | `"float"` | The format in which the embeddings are encoded. Options are “float” or “base64”. |
| `user` | `str` | \- | The user associated with the API request. |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `organization` | `str` | \- | The organization associated with the API request. |
| `base_url` | `str` | \- | The base URL for the API endpoint. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the API request. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for configuring the API client. |
| `openai_client` | `Optional[OpenAIClient]` | \- | An instance of the OpenAIClient to use for making API requests. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Ollama Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/ollama</url>
  <content>The `OllamaEmbedder` can be used to embed text data into vectors locally using Ollama.

Usage
-----

cookbook/embedders/ollama\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"openhermes"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `4096` | The dimensionality of the embeddings generated by the model. |
| `host` | `str` | \- | The host address for the API endpoint. |
| `timeout` | `Any` | \- | The timeout duration for API requests. |
| `options` | `Any` | \- | Additional options for configuring the API request. |
| `client_kwargs` | `Optional[Dict[str, Any]]` | \- | Additional keyword arguments for configuring the API client. Optional. |
| `ollama_client` | `Optional[OllamaClient]` | \- | An instance of the OllamaClient to use for making API requests. Optional. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Voyage AI Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/voyageai</url>
  <content>The `VoyageAIEmbedder` class is used to embed text data into vectors using the Voyage AI API. Get your key from [here](https://dash.voyageai.com/api-keys).

Usage
-----

cookbook/embedders/voyageai\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"voyage-2"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `1024` | The dimensionality of the embeddings generated by the model. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the API request. Optional. |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `base_url` | `str` | `"https://api.voyageai.com/v1/embeddings"` | The base URL for the API endpoint. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retries for API requests. Optional. |
| `timeout` | `Optional[float]` | \- | The timeout duration for API requests. Optional. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for configuring the API client. Optional. |
| `voyage_client` | `Optional[Client]` | \- | An instance of the Client to use for making API requests. Optional. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Azure OpenAI Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/azure_openai</url>
  <content>The `AzureOpenAIEmbedder` class is used to embed text data into vectors using the Azure OpenAI API. Get your key from [here](https://ai.azure.com/).

Usage
-----

cookbook/embedders/azure\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"text-embedding-ada-002"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `1536` | The dimensionality of the embeddings generated by the model. |
| `encoding_format` | `Literal['float', 'base64']` | `"float"` | The format in which the embeddings are encoded. Options are “float” or “base64”. |
| `user` | `str` | \- | The user associated with the API request. |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `api_version` | `str` | `"2024-02-01"` | The version of the API to use for the requests. |
| `azure_endpoint` | `str` | \- | The Azure endpoint for the API requests. |
| `azure_deployment` | `str` | \- | The Azure deployment name for the API requests. |
| `base_url` | `str` | \- | The base URL for the API endpoint. |
| `azure_ad_token` | `str` | \- | The Azure Active Directory token for authentication. |
| `azure_ad_token_provider` | `Any` | \- | The provider for obtaining the Azure AD token. |
| `organization` | `str` | \- | The organization associated with the API request. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the API request. Optional. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for configuring the API client. Optional. |
| `openai_client` | `Optional[AzureOpenAIClient]` | \- | An instance of the AzureOpenAIClient to use for making API requests. Optional. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Mistral Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/mistral</url>
  <content>The `MistralEmbedder` class is used to embed text data into vectors using the Mistral API. Get your key from [here](https://console.mistral.ai/api-keys/).

Usage
-----

cookbook/embedders/mistral\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"mistral-embed"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `1024` | The dimensionality of the embeddings generated by the model. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the API request. Optional. |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `endpoint` | `str` | \- | The endpoint URL for the API requests. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retries for API requests. Optional. |
| `timeout` | `Optional[int]` | \- | The timeout duration for API requests. Optional. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for configuring the API client. Optional. |
| `mistral_client` | `Optional[MistralClient]` | \- | An instance of the MistralClient to use for making API requests. Optional. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Fireworks Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/fireworks</url>
  <content>The `FireworksEmbedder` can be used to embed text data into vectors using the Fireworks API. Fireworks uses the OpenAI API specification, so the `FireworksEmbedder` class is similar to the `OpenAIEmbedder` class, incorporating adjustments to ensure compatibility with the Fireworks platform. Get your key from [here](https://fireworks.ai/account/api-keys).

Usage
-----

cookbook/embedders/fireworks\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"nomic-ai/nomic-embed-text-v1.5"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `768` | The dimensionality of the embeddings generated by the model. |
| `api_key` | `str` | \- | The API key used for authenticating requests. |
| `base_url` | `str` | `"https://api.fireworks.ai/inference/v1"` | The base URL for the API endpoint. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Together Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/together</url>
  <content>The `TogetherEmbedder` can be used to embed text data into vectors using the Together API. Together uses the OpenAI API specification, so the `TogetherEmbedder` class is similar to the `OpenAIEmbedder` class, incorporating adjustments to ensure compatibility with the Together platform. Get your key from [here](https://api.together.xyz/settings/api-keys).

Usage
-----

cookbook/embedders/together\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"nomic-ai/nomic-embed-text-v1.5"` | The name of the model used for generating embeddings. |
| `dimensions` | `int` | `768` | The dimensionality of the embeddings generated by the model. |
| `api_key` | `str` |  | The API key used for authenticating requests. |
| `base_url` | `str` | `"https://api.Together.ai/inference/v1"` | The base URL for the API endpoint. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>HuggingFace Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/huggingface</url>
  <content>The `HuggingfaceCustomEmbedder` class is used to embed text data into vectors using the Hugging Face API. You can get one from [here](https://huggingface.co/settings/tokens).

Usage
-----

cookbook/embedders/huggingface\_embedder.py

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dimensions` | `int` | \- | The dimensionality of the generated embeddings |
| `model` | `str` | `all-MiniLM-L6-v2` | The name of the HuggingFace model to use |
| `api_key` | `str` | \- | The API key used for authenticating requests |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Optional dictionary of parameters for the HuggingFace client |
| `huggingface_client` | `Any` | \- | Optional pre-configured HuggingFace client instance |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Qdrant FastEmbed Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/qdrant_fastembed</url>
  <content>The `FastEmbedEmbedder` class is used to embed text data into vectors using the [FastEmbed](https://qdrant.github.io/fastembed/).

Usage
-----

cookbook/embedders/qdrant\_fastembed.py

    from phi.agent import AgentKnowledge
    from phi.vectordb.pgvector import PgVector
    from phi.embedder.fastembed import FastEmbedEmbedder
    
    embeddings = FastEmbedEmbedder().get_embedding("The quick brown fox jumps over the lazy dog.")
    
    # Print the embeddings and their dimensions
    print(f"Embeddings: {embeddings[:5]}")
    print(f"Dimensions: {len(embeddings)}")
    
    # Example usage:
    knowledge_base = AgentKnowledge(
        vector_db=PgVector(
            db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
            table_name="qdrant_embeddings",
            embedder=FastEmbedEmbedder(),
        ),
        num_documents=2,
    )
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dimensions` | `int` | \- | The dimensionality of the generated embeddings |
| `model` | `str` | `BAAI/bge-small-en-v1.5` | The name of the qdrant\_fastembed model to use |</content>
</page>

<page>
  <title>SentenceTransformers Embedder - Phidata</title>
  <url>https://docs.phidata.com/embedder/sentencetransformers</url>
  <content>The `SentenceTransformerEmbedder` class is used to embed text data into vectors using the [SentenceTransformers](https://www.sbert.net/) library.

Usage
-----

cookbook/embedders/sentence\_transformer\_embedder.py

    from phi.agent import AgentKnowledge
    from phi.vectordb.pgvector import PgVector
    from phi.embedder.sentence_transformer import SentenceTransformerEmbedder
    
    embeddings = SentenceTransformerEmbedder().get_embedding("The quick brown fox jumps over the lazy dog.")
    
    # Print the embeddings and their dimensions
    print(f"Embeddings: {embeddings[:5]}")
    print(f"Dimensions: {len(embeddings)}")
    
    # Example usage:
    knowledge_base = AgentKnowledge(
        vector_db=PgVector(
            db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
            table_name="sentence_transformer_embeddings",
            embedder=SentenceTransformerEmbedder(),
        ),
        num_documents=2,
    )
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dimensions` | `int` | \- | The dimensionality of the generated embeddings |
| `model` | `str` | `all-mpnet-base-v2` | The name of the SentenceTransformers model to use |
| `sentence_transformer_client` | `Optional[Client]` | \- | Optional pre-configured SentenceTransformers client instance |</content>
</page>

<page>
  <title>Prompts - Phidata</title>
  <url>https://docs.phidata.com/agents/prompts</url>
  <content>We prompt Agents using `description` and `instructions` and a number of other settings. These settings are used to build the **system** prompt that is sent to the language model.

Understanding how these prompts are created will help you build better Agents.

The 2 key parameters are:

1.  **Description**: A description that guides the overall behaviour of the agent.
2.  **Instructions**: A list of precise, task-specific instructions on how to achieve its goal.

System message
--------------

The system message is created using `description`, `instructions` and a number of other settings. The `description` is added to the start of the system message and `instructions` are added as a list after `## Instructions`. For example:

Will translate to (set `debug_mode=True` to view the logs):

Set the system message directly
-------------------------------

You can manually set the system message using the `system_prompt` parameter.

User message
------------

The input `message` sent to the `Agent.run()` or `Agent.print_response()` functions is used as the user message.

### User message when `enable_rag=True`

If the Agent is provided `knowledge`, and the `enable_rag=True`, the user message is set to:

Default system message
----------------------

The Agent creates a default system message that can be customized using the following parameters:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `description` | `str` | `None` | A description of the Agent that is added to the start of the system message. |
| `task` | `str` | `None` | Describe the task the agent should achieve. |
| `instructions` | `List[str]` | `None` | List of instructions added to the system prompt in `<instructions>` tags. Default instructions are also created depending on values for `markdown`, `output_model` etc. |
| `additional_context` | `str` | `None` | Additional context added to the end of the system message. |
| `expected_output` | `str` | `None` | Provide the expected output from the Agent. This is added to the end of the system message. |
| `extra_instructions` | `List[str]` | `None` | List of extra instructions added to the default system prompt. Use these when you want to add some extra instructions at the end of the default instructions. |
| `prevent_hallucinations` | `bool` | `False` | If True, add instructions to return “I don’t know” when the agent does not know the answer. |
| `prevent_prompt_injection` | `bool` | `False` | If True, add instructions to prevent prompt injection attacks. |
| `limit_tool_access` | `bool` | `False` | If True, add instructions for limiting tool access to the default system prompt if tools are provided |
| `markdown` | `bool` | `False` | Add an instruction to format the output using markdown. |
| `add_datetime_to_instructions` | `bool` | `False` | If True, add the current datetime to the prompt to give the agent a sense of time. This allows for relative times like “tomorrow” to be used in the prompt |
| `system_prompt` | `str` | `None` | System prompt: provide the system prompt as a string |
| `system_prompt_template` | `PromptTemplate` | `None` | Provide the system prompt as a PromptTemplate. |
| `use_default_system_message` | `bool` | `True` | If True, build a default system message using agent settings and use that. |
| `system_message_role` | `str` | `system` | Role for the system message. |

Default user message
--------------------

The Agent creates a default user message, which is either the input message or a message with the `context` if `enable_rag=True`. The default user message can be customized using:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `enable_rag` | `bool` | `False` | Enable RAG by adding references from the knowledge base to the prompt. |
| `add_rag_instructions` | `bool` | `False` | If True, adds instructions for using the RAG to the system prompt (if knowledge is also provided). For example: add an instruction to prefer information from the knowledge base over its training data. |
| `add_history_to_messages` | `bool` | `False` | If true, adds the chat history to the messages sent to the Model. |
| `num_history_responses` | `int` | `3` | Number of historical responses to add to the messages. |
| `user_prompt` | `Union[List, Dict, str]` | `None` | Provide the user prompt as a string. Note: this will ignore the message sent to the run function. |
| `user_prompt_template` | `PromptTemplate` | `None` | Provide the user prompt as a PromptTemplate. |
| `use_default_user_message` | `bool` | `True` | If True, build a default user prompt using references and chat history. |
| `user_message_role` | `str` | `user` | Role for the user message. |</content>
</page>

<page>
  <title>Tools - Phidata</title>
  <url>https://docs.phidata.com/agents/tools</url>
  <content>**Agents use tools to take actions and interact with external systems**.

Tools are functions that an Agent can run to achieve tasks. For example: searching the web, running SQL, sending an email or calling APIs. You can use any python function as a tool or use a pre-built **toolkit**. The general syntax is:

Phidata provides many pre-built **toolkits** that you can add to your Agents. For example, let’s use the DuckDuckGo toolkit to search the web.

For more control, write your own python functions and add them as tools to an Agent. For example, here’s how to add a `get_top_hackernews_stories` tool to an Agent.

Read more about:

*   [Available toolkits](https://docs.phidata.com/tools/toolkits)
*   [Using functions as tools](https://docs.phidata.com/tools/functions)

Attributes
----------

The following attributes allow an `Agent` to use tools

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `tools` | `List[Union[Tool, Toolkit, Callable, Dict, Function]]` | \- | A list of tools provided to the Model. Tools are functions the model may generate JSON inputs for. |
| `show_tool_calls` | `bool` | `False` | Print the signature of the tool calls in the Model response. |
| `tool_call_limit` | `int` | \- | Maximum number of tool calls allowed. |
| `tool_choice` | `Union[str, Dict[str, Any]]` | \- | Controls which (if any) tool is called by the model. “none” means the model will not call a tool and instead generates a message. “auto” means the model can pick between generating a message or calling a tool. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. “none” is the default when no tools are present. “auto” is the default if tools are present. |
| `read_chat_history` | `bool` | `False` | Add a tool that allows the Model to read the chat history. |
| `search_knowledge` | `bool` | `False` | Add a tool that allows the Model to search the knowledge base (aka Agentic RAG). |
| `update_knowledge` | `bool` | `False` | Add a tool that allows the Model to update the knowledge base. |
| `read_tool_call_history` | `bool` | `False` | Add a tool that allows the Model to get the tool call history. |

*   [Using a Toolkit](#using-a-toolkit)
*   [Writing your own Tools](#writing-your-own-tools)
*   [Attributes](#attributes)</content>
</page>

<page>
  <title>Memory - Phidata</title>
  <url>https://docs.phidata.com/agents/memory</url>
  <content>Phidata provides 3 types of memories for building a great Agent experience (AX):

1.  **Chat History:** previous messages from the conversation, we recommend sending the last 3-5 messages to the model.
2.  **User Memories:** notes and insights about the user, this helps the model personalize the response to the user.
3.  **Summaries:** a summary of the conversation, which is added to the prompt when chat history gets too long.

Before we dive in, let’s understand the terminology:

*   **Session:** Each conversation with an Agent is called a **session**. Sessions are identified by a `session_id`.
*   **Run:** Every interaction (i.e. chat) within a session is called a **run**. Runs are identified by a `run_id`.
*   **Messages:** are the individual messages sent to and received from the model. They have a `role` (`system`, `user` or `assistant`) and `content`.

Built-in Memory
---------------

Every Agent comes with built-in memory that can be used to access the historical **runs** and **messages**. Access it using `agent.memory`

The list of runs between the user and agent. Each run contains the input message and output response.

The full list of messages sent to the model, including system prompt, tool calls etc.

### Example

Persistent Memory
-----------------

The built-in memory only lasts while the session is active. To persist memory across sessions, we can store Agent sessions in a database using `AgentStorage`.

Storage is a necessary component when building user facing AI products as any production application will require users to be able to “continue” their conversation with the Agent.

Let’s test this out, create a file `persistent_memory.py` with the following code:

### Run the agent

Install dependencies and run the agent:

You can view the agent sessions in the sqlite database and continue any conversation by providing the same `session_id`.

Read more in the [storage](https://docs.phidata.com/agents/storage) section.

User preferences and conversation summaries
-------------------------------------------

Along with storing chat history and run messages, `AgentMemory` can be extended to automatically classify and store user preferences and conversation summaries.

To do this, add a `db` to `AgentMemory` and set `create_user_memories=True` and `create_session_summary=True`

User memories are stored in the `AgentMemory` whereas session summaries are stored in the `AgentStorage` table with the rest of the session information.

Example
-------

personalized\_memories\_and\_summaries.py

Attributes
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `memory` | `AgentMemory` | `AgentMemory()` | Agent’s memory object used for storing and retrieving information. |
| `add_history_to_messages` | `bool` | `False` | If true, adds the chat history to the messages sent to the Model. Also known as `add_chat_history_to_messages`. |
| `num_history_responses` | `int` | `3` | Number of historical responses to add to the messages. |
| `create_user_memories` | `bool` | `False` | If true, create and store personalized memories for the user. |
| `update_user_memories_after_run` | `bool` | `True` | If true, update memories for the user after each run. |
| `create_session_summary` | `bool` | `False` | If true, create and store session summaries. |
| `update_session_summary_after_run` | `bool` | `True` | If true, update session summaries after each run. |</content>
</page>

<page>
  <title>Storage - Phidata</title>
  <url>https://docs.phidata.com/agents/storage</url>
  <content>    import typer
    from typing import Optional, List
    from phi.agent import Agent
    from phi.storage.agent.postgres import PgAgentStorage
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector, SearchType
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
    )
    # Load the knowledge base: Comment after first run
    knowledge_base.load(upsert=True)
    storage = PgAgentStorage(table_name="pdf_agent", db_url=db_url)
    
    def pdf_agent(new: bool = False, user: str = "user"):
        session_id: Optional[str] = None
    
        if not new:
            existing_sessions: List[str] = storage.get_all_session_ids(user)
            if len(existing_sessions) > 0:
                session_id = existing_sessions[0]
    
        agent = Agent(
            session_id=session_id,
            user_id=user,
            knowledge=knowledge_base,
            storage=storage,
            # Show tool calls in the response
            show_tool_calls=True,
            # Enable the agent to read the chat history
            read_chat_history=True,
            # We can also automatically add the chat history to the messages sent to the model
            # But giving the model the chat history is not always useful, so we give it a tool instead
            # to only use when needed.
            # add_history_to_messages=True,
            # Number of historical responses to add to the messages.
            # num_history_responses=3,
        )
        if session_id is None:
            session_id = agent.session_id
            print(f"Started Session: {session_id}\n")
        else:
            print(f"Continuing Session: {session_id}\n")
    
        # Runs the agent as a cli app
        agent.cli_app(markdown=True)
    
    
    if __name__ == "__main__":
        typer.run(pdf_agent)</content>
</page>

<page>
  <title>Knowledge - Phidata</title>
  <url>https://docs.phidata.com/agents/knowledge</url>
  <content>**Agents use knowledge to supplement their training data with domain expertise**.

Knowledge is stored in a vector database and provides agents with business context at query time, helping them respond in a context-aware manner. The general syntax is:

Vector Databases
----------------

While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly. Here’s how vector databases are used with Agents:

Example: RAG Agent with a PDF Knowledge Base
--------------------------------------------

Let’s build a **RAG Agent** that answers questions from a PDF.

### Step 1: Run PgVector

Let’s use `PgVector` as our vector db as it can also provide storage for our Agents.

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **PgVector** on port **5532** using:

### Step 2: Traditional RAG

Retrieval Augmented Generation (RAG) means **“stuffing the prompt with relevant information”** to improve the model’s response. This is a 2 step process:

1.  Retrieve relevant information from the knowledge base.
2.  Augment the prompt to provide context to the model.

Let’s build a **traditional RAG** Agent that answers questions from a PDF of recipes.

### Step 3: Agentic RAG

With traditional RAG above, `add_context=True` always adds information from the knowledge base to the prompt, regardless of whether it is relevant to the question or helpful.

With Agentic RAG, we let the Agent decide **if** it needs to access the knowledge base and what search parameters it needs to query the knowledge base.

Set `search_knowledge=True` and `read_chat_history=True`, giving the Agent tools to search its knowledge and chat history on demand.

Attributes
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `knowledge` | `AgentKnowledge` | `None` | Provides the knowledge base used by the agent. |
| `search_knowledge` | `bool` | `True` | Adds a tool that allows the Model to search the knowledge base (aka Agentic RAG). Enabled by default when `knowledge` is provided. |
| `add_context` | `bool` | `False` | Enable RAG by adding references from AgentKnowledge to the user prompt. |
| `retriever` | `Callable[..., Optional[list[dict]]]` | `None` | Function to get context to add to the user message. This function is called when add\_context is True. |
| `context_format` | `Literal['json', 'yaml']` | `json` | Specifies the format for RAG, either “json” or “yaml”. |
| `add_context_instructions` | `bool` | `False` | If True, add instructions for using the context to the system prompt (if knowledge is also provided). For example: add an instruction to prefer information from the knowledge base over its training data. |</content>
</page>

<page>
  <title>Structured Output - Phidata</title>
  <url>https://docs.phidata.com/agents/structured-output</url>
  <content>One of our favorite features is using Agents to generate structured data (i.e. a pydantic model). Use this feature to extract features, classify data, produce fake data etc. The best part is that they work with function calls, knowledge bases and all other features.

Let’s create an Movie Agent to write a `MovieScript` for us.

    from typing import List
    from rich.pretty import pprint
    from pydantic import BaseModel, Field
    from phi.agent import Agent, RunResponse
    from phi.model.openai import OpenAIChat
    
    
    class MovieScript(BaseModel):
        setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
        ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
        genre: str = Field(
            ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
        )
        name: str = Field(..., description="Give a name to this movie")
        characters: List[str] = Field(..., description="Name of characters for this movie.")
        storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")
    
    
    # Agent that uses JSON mode
    json_mode_agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        description="You write movie scripts.",
        response_model=MovieScript,
    )
    # Agent that uses structured outputs
    structured_output_agent = Agent(
        model=OpenAIChat(id="gpt-4o-2024-08-06"),
        description="You write movie scripts.",
        response_model=MovieScript,
        structured_outputs=True,
    )
    
    
    # Get the response in a variable
    # json_mode_response: RunResponse = json_mode_agent.run("New York")
    # pprint(json_mode_response.content)
    # structured_output_response: RunResponse = structured_output_agent.run("New York")
    # pprint(structured_output_response.content)
    
    json_mode_agent.print_response("New York")
    structured_output_agent.print_response("New York")
    

Run the script to see the output.

    # Using JSON mode
    MovieScript(
    │   setting='The bustling streets of New York City, filled with skyscrapers, secret alleyways, and hidden underground passages.',
    │   ending='The protagonist manages to thwart an international conspiracy, clearing his name and winning the love of his life back.',
    │   genre='Thriller',
    │   name='Shadows in the City',
    │   characters=['Alex Monroe', 'Eva Parker', 'Detective Rodriguez', 'Mysterious Mr. Black'],
    │   storyline="When Alex Monroe, an ex-CIA operative, is framed for a crime he didn't commit, he must navigate the dangerous streets of New York to clear his name. As he uncovers a labyrinth of deceit involving the city's most notorious crime syndicate, he enlists the help of an old flame, Eva Parker. Together, they race against time to expose the true villain before it's too late."
    )
    
    # Use the structured output
    MovieScript(
    │   setting='In the bustling streets and iconic skyline of New York City.',
    │   ending='Isabella and Alex, having narrowly escaped the clutches of the Syndicate, find themselves standing at the top of the Empire State Building. As the glow of the setting sun bathes the city, they share a victorious kiss. Newly emboldened and as an unstoppable duo, they vow to keep NYC safe from any future threats.',
    │   genre='Action Thriller',
    │   name='The NYC Chronicles',
    │   characters=['Isabella Grant', 'Alex Chen', 'Marcus Kane', 'Detective Ellie Monroe', 'Victor Sinclair'],
    │   storyline='Isabella Grant, a fearless investigative journalist, uncovers a massive conspiracy involving a powerful syndicate plotting to control New York City. Teaming up with renegade cop Alex Chen, they must race against time to expose the culprits before the city descends into chaos. Dodging danger at every turn, they fight to protect the city they love from imminent destruction.'
    )</content>
</page>

<page>
  <title>Reasoning - Phidata</title>
  <url>https://docs.phidata.com/agents/reasoning</url>
  <content>Reasoning is an **experimental feature** that enables an `Agent` to think through a problem step-by-step before jumping into a response. The Agent works through different ideas, validating and correcting as needed. Once it reaches a final answer, it will validate and provide a response. Let’s give it a try. Create a file `reasoning_agent.py`

Run the Reasoning Agent:

How to use reasoning
--------------------

To add reasoning, set `reasoning=True`. When using reasoning with tools, do not use `structured_outputs=True` as gpt-4o cannot use tools with structured outputs.

You can also use tools with a reasoning agent, but do not use `structured_outputs=True` as gpt-4o cannot use tools with structured outputs. Lets create a finance agent that can reason.

Run the script to see the output.

More reasoning examples
-----------------------

### Logical puzzles

Run the script to see the output.

### Mathematical proofs

Run the script to see the output.

### Scientific research

Run the script to see the output.

### Ethical dilemma

Run the script to see the output.

### Planning an itinerary

Run the script to see the output.

### Creative writing

Run the script to see the output.</content>
</page>

<page>
  <title>Teams - Phidata</title>
  <url>https://docs.phidata.com/agents/teams</url>
  <content>    from phi.agent import Agent
    from phi.tools.hackernews import HackerNews
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.newspaper4k import Newspaper4k
    
    hn_researcher = Agent(
        name="HackerNews Researcher",
        role="Gets top stories from hackernews.",
        tools=[HackerNews()],
    )
    
    web_searcher = Agent(
        name="Web Searcher",
        role="Searches the web for information on a topic",
        tools=[DuckDuckGo()],
        add_datetime_to_instructions=True,
    )
    
    article_reader = Agent(
        name="Article Reader",
        role="Reads articles from URLs.",
        tools=[Newspaper4k()],
    )
    
    hn_team = Agent(
        name="Hackernews Team",
        team=[hn_researcher, web_searcher, article_reader],
        instructions=[
            "First, search hackernews for what the user is asking about.",
            "Then, ask the article reader to read the links for the stories to get more information.",
            "Important: you must provide the article reader with the links to read.",
            "Then, ask the web searcher to search for each story to get more information.",
            "Finally, provide a thoughtful and engaging summary.",
        ],
        show_tool_calls=True,
        markdown=True,
    )
    hn_team.print_response("Write an article about the top 2 stories on hackernews", stream=True)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/workflows/introduction</url>
  <content>Workflows are deterministic, stateful, multi-agent pipelines that power many of our production use cases. They are incredibly powerful and offer the following benefits:

*   **Control and Flexibility**: You have full control over the multi-agent process, how the input is processed, which agents are used and in what order.
*   **Built-in Memory**: You can store state and cache results in a database at any time, meaning your agents can re-use results from previous steps.
*   **Defined as a python class**: You do not need to learn a new framework, its just python.

How to build a workflow:

1.  Define your workflow as a class by inheriting from the `Workflow` class
2.  Add one or more agents to the workflow
3.  Implement your logic in the `run()` method
4.  Cache results in the `session_state` as needed
5.  Run the workflow using the `.run()` method

Example: Blog Post Generator
----------------------------

Let’s create a blog post generator that can search the web, read the top links and write a blog post for us. We’ll cache intermediate results in the database to improve performance.

### Create the Workflow

Create a file `blog_post_generator.py`

### Run the workflow

Install libraries

Run the workflow

Now the results are cached in the database and can be re-used for future runs. Run the workflow again to view the cached results.</content>
</page>

<page>
  <title>Session State - Phidata</title>
  <url>https://docs.phidata.com/workflows/session-state</url>
  <content>All Workflows come with a `session_state` dictionary that you can use to cache intermediate results. Provide your workflows with `storage` and a `session_id` to enable caching.

For example, you can use the `SqlWorkflowStorage` to cache results in a Sqlite database.

Then in the `run()` method, you can read from and add to the `session_state` as needed.

When the workflow starts, the `session_state` for that particular `session_id` is read from the database and when the workflow ends, the `session_state` is stored in the database.

View the [Blog Post Generator](https://docs.phidata.com/workflows/introduction#full-example-blog-post-generator) for an example of how to use session state for caching.</content>
</page>

<page>
  <title>Streaming - Phidata</title>
  <url>https://docs.phidata.com/workflows/streaming</url>
  <content>Workflows are all about control and flexibility. You have full control over the multi-agent process, how the input is processed, which agents are used and in what order.

You also have full control over how the output is streamed.

Streaming
---------

To stream the output, yield an `Iterator[RunResponse]` from the `run()` method of your workflow.

    # Define the workflow
    class GenerateNewsReport(Workflow):
        agent_1: Agent = ...
    
        agent_2: Agent = ...
    
        agent_3: Agent = ...
    
        def run(self, ...) -> Iterator[RunResponse]:
            # Run agents and gather the response
            # These can be batch responses, you can also stream intermediate results if you want
            final_agent_input = ...
    
            # Generate the final response from the writer agent
            agent_3_response_stream: Iterator[RunResponse] = self.agent_3.run(final_agent_input, stream=True)
    
            # Yield the response
            yield agent_3_response_stream
    
    
    # Instantiate the workflow
    generate_news_report = GenerateNewsReport()
    
    # Run workflow and get the response as an iterator of RunResponse objects
    report_stream: Iterator[RunResponse] = generate_news_report.run(...)
    
    # Print the response
    pprint_run_response(report_stream, markdown=True)
    

Batch
-----

Simply return a `RunResponse` object from the `run()` method of your workflow to return a single output.

    # Define the workflow
    class GenerateNewsReport(Workflow):
        agent_1: Agent = ...
    
        agent_2: Agent = ...
    
        agent_3: Agent = ...
    
        def run(self, ...) -> RunResponse:
            # Run agents and gather the response
            final_agent_input = ...
    
            # Generate the final response from the writer agent
            agent_3_response: RunResponse = self.agent_3.run(final_agent_input)
    
            # Return the response
            return agent_3_response
    
    
    # Instantiate the workflow
    generate_news_report = GenerateNewsReport()
    
    # Run workflow and get the response as a RunResponse object
    report: RunResponse = generate_news_report.run(...)
    
    # Print the response
    pprint_run_response(report, markdown=True)</content>
</page>

<page>
  <title>Sql Agent - Phidata</title>
  <url>https://docs.phidata.com/examples/use-case/sql</url>
  <content>Use Cases

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/use-case/sql.mdx)

[Hackernews Team](https://docs.phidata.com/examples/teams/hackernews)[World Building](https://docs.phidata.com/examples/use-case/worldbuilding)</content>
</page>

<page>
  <title>World Building - Phidata</title>
  <url>https://docs.phidata.com/examples/use-case/worldbuilding</url>
  <content>Use Cases

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/use-case/worldbuilding.mdx)

[Sql Agent](https://docs.phidata.com/examples/use-case/sql)[ArXiv Research Agent](https://docs.phidata.com/examples/use-case/arxiv-research)</content>
</page>

<page>
  <title>Azure - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/azure</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export Environment Variables

      export AZURE_OPENAI_API_KEY=***
      export AZURE_OPENAI_ENDPOINT=***
      export AZURE_OPENAI_MODEL_NAME=***
      export AZURE_OPENAI_DEPLOYMENT=***
      # Optional:
      # export AZURE_OPENAI_API_VERSION=***
    

4

Run azure Agent

    python cookbook/providers/azure_openai/basic.py</content>
</page>

<page>
  <title>Claude - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/claude</url>
  <content>[​](#example)

Example
------------------------

Use `Claude` with your `Agent`:

[​](#usage)

Usage
--------------------

You can get your API key [from Anthropic here](https://anthropic.com/).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U anthropic phidata
    

3

Export \`ANTHROPIC\_API\_KEY\`

    export ANTHROPIC_API_KEY=xxx
    

4

Run Claude Agent

    python cookbook/providers/claude/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/claude/basic.py)</content>
</page>

<page>
  <title>Cohere - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/cohere</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U cohere phidata
    

3

Export \`CO\_API\_KEY\`

    export CO_API_KEY=xxx
    

4

Run Cohere Agent

    python cookbook/providers/cohere/basic.py</content>
</page>

<page>
  <title>Fireworks - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/fireworks</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U fireworks phidata
    

3

Export \`FIREWORKS\_API\_KEY\`

    export FIREWORKS_API_KEY=xxx
    

4

Run fireworks Agent

    python cookbook/providers/fireworks/basic.py</content>
</page>

<page>
  <title>Gemini - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/gemini</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Get your key [from Google here](https://ai.google.dev/aistudio).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U google-generativeai phidata
    

3

Export \`GOOGLE\_API\_KEY\`

    export GOOGLE_API_KEY=***
    

4

Run Gemini Agent

    python cookbook/providers/google/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/google/basic.py)</content>
</page>

<page>
  <title>Groq - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/groq</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U groq phidata
    

3

Export \`GROQ\_API\_KEY\`

    export GROQ_API_KEY=xxx
    

4

Run Groq Agent

    python cookbook/providers/groq/basic.py</content>
</page>

<page>
  <title>Mistral - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/mistral</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U mistralai phidata
    

3

Export \`MISTRAL\_API\_KEY\`

    export MISTRAL_API_KEY=xxx
    

4

Run Mistral Agent

    python cookbook/providers/mistral/basic.py</content>
</page>

<page>
  <title>Ollama - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/ollama</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Install [ollama](https://ollama.com/) and run a model.

1

Run your chat model

    ollama run llama3.1
    

Message `/bye` to exit the chat model

2

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

3

Install libraries

    pip install -U ollama phidata
    

4

Run Ollama Agent

    python cookbook/providers/ollama/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/ollama/basic.py)</content>
</page>

<page>
  <title>Together - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/together</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Get your key [from Together here](https://api.together.xyz/settings/api-keys).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U together openai phidata
    

3

Export \`TOGETHER\_API\_KEY\`

    export TOGETHER_API_KEY=xxx
    

4

Run Together Agent

    python cookbook/providers/together/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/together/basic.py)</content>
</page>

<page>
  <title>AWS Bedrock - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/aws_bedrock</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U boto3 phidata
    

3

Export Environment Variables

      export AWS_ACCESS_KEY_ID=***
      export AWS_SECRET_ACCESS_KEY=***
      export AWS_DEFAULT_REGION=***
    

4

Run AWS Bedrock Agent

    python cookbook/providers/bedrock/basic.py</content>
</page>

<page>
  <title>DeepSeek - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/deepseek</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export Environment Variables

      export DEEPSEEK_API_KEY=***
    

4

Run DeepSeek Agent

    python cookbook/providers/deepseek/basic.py</content>
</page>

<page>
  <title>HuggingFace - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/huggingface</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Get your API key [from HuggingFace here](https://huggingface.co/settings/tokens).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U huggingface_hub phidata
    

3

Export Environment Variables

    export HF_TOKEN=***
    

4

Run HuggingFace Agent

    python cookbook/providers/huggingface/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/huggingface/basic.py)</content>
</page>

<page>
  <title>OpenRouter - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/openrouter</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export \`OPENROUTER\_API\_KEY\`

    export OPENROUTER_API_KEY=***
    

4

Run OpenRouter Agent

    python cookbook/providers/openrouter/basic.py</content>
</page>

<page>
  <title>Nvidia - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/nvidia</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Get your key [from Nvidia here](https://build.nvidia.com/explore/discover).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export \`NVIDIA\_API\_KEY\`

    export NVIDIA_API_KEY=xxx
    

4

Run Nvidia Agent

    python cookbook/providers/nvidia/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/nvidia/basic.py)</content>
</page>

<page>
  <title>Sambanova - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/sambanova</url>
  <content>1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export \`SAMBANOVA\_API\_KEY\`

    export SAMBANOVA_API_KEY=***
    

4

Run Sambanova Agent

    python cookbook/providers/sambanova/basic.py</content>
</page>

<page>
  <title>xAI - Phidata</title>
  <url>https://docs.phidata.com/examples/provider/xai</url>
  <content>[​](#example)

Example
------------------------

[​](#usage)

Usage
--------------------

Get your API key [from xAI here](https://console.x.ai/).

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

2

Install libraries

    pip install -U openai phidata
    

3

Export \`XAI\_API\_KEY\`

    export XAI_API_KEY=***
    

4

Run xAI Agent

    python cookbook/providers/xai/basic.py
    

[​](#information)

Information
--------------------------------

*   View on [Github](https://github.com/phidatahq/phidata/tree/main/cookbook/providers/xai/basic.py)</content>
</page>

<page>
  <title>Setup workspace for new users - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/new-users</url>
  <content>Manage Workspace

Follow these steps to setup an existing workspace:

1

Clone git repository

Clone the git repo and `cd` into the workspace directory

2

Create and activate a virtual env

3

Install phidata

4

Setup workspace

5

Copy secrets

Copy `workspace/example_secrets` to `workspace/secrets`

6

Start workspace

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) if needed.

7

Stop workspace

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/templates/how-to/new-users.mdx)

[Create Git Repo](https://docs.phidata.com/templates/how-to/git-repo)[Format & Validate](https://docs.phidata.com/templates/how-to/format-and-validate)</content>
</page>

<page>
  <title>Composio - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/composio</url>
  <content>[**ComposioTools**](https://docs.composio.dev/framework/phidata) enables an Agent to work with sofware tools like Gmail, Salesforce, Github, etc.

Example
-------

The following agent will use Github Tool from Composio Toolkit to star a repo.

Run the following commands to setup the agent

The following parameters are used when calling the GitHub star repository action:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `owner` | `str` | \- | The owner of the repository to star. |
| `repo` | `str` | \- | The name of the repository to star. |

Composio Toolkit provides 1000+ functions to connect to different software tools. Open this [link](https://composio.dev/tools) to view the complete list of functions.

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)</content>
</page>

<page>
  <title>SingleStore - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/singlestore</url>
  <content>Integrations

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/integrations/singlestore.mdx)

[PgVector](https://docs.phidata.com/examples/integrations/pgvector)[LanceDB](https://docs.phidata.com/examples/integrations/lancedb)</content>
</page>

<page>
  <title>LanceDB Integration - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/lancedb</url>
  <content>    import typer
    from typing import Optional
    from rich.prompt import Prompt
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.lancedb import LanceDb
    from phi.vectordb.search import SearchType
    
    # LanceDB Vector DB
    vector_db = LanceDb(
        table_name="recipes",
        uri="/tmp/lancedb",
        search_type=SearchType.keyword,
    )
    
    # Knowledge Base
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=True)
    
    
    def lancedb_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge=knowledge_base,
            show_tool_calls=True,
            debug_mode=True,
        )
    
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(lancedb_agent)</content>
</page>

<page>
  <title>Pinecone Integration - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/pinecone</url>
  <content>    import os
    import typer
    from typing import Optional
    from rich.prompt import Prompt
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pineconedb import PineconeDB
    
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = "thai-recipe-hybrid-search"
    
    vector_db = PineconeDB(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
        api_key=api_key,
        use_hybrid_search=True,
        hybrid_alpha=0.5,
    )
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=True, upsert=True)
    
    
    def pinecone_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge=knowledge_base,
            show_tool_calls=True,
            debug_mode=True,
        )
    
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(pinecone_agent)</content>
</page>

<page>
  <title>Qdrant Integration - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/qdrant</url>
  <content>    import os
    import typer
    from typing import Optional
    from rich.prompt import Prompt
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.qdrant import Qdrant
    
    api_key = os.getenv("QDRANT_API_KEY")
    qdrant_url = os.getenv("QDRANT_URL")
    collection_name = "thai-recipe-index"
    
    vector_db = Qdrant(
        collection=collection_name,
        url=qdrant_url,
        api_key=api_key,
    )
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=True, upsert=True)
    
    
    def qdrant_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge_base=knowledge_base,
            tool_calls=True,
            use_tools=True,
            show_tool_calls=True,
            debug_mode=True,
            # Uncomment the following line to use traditional RAG
            # add_references_to_prompt=True,
        )
    
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(qdrant_agent)</content>
</page>

<page>
  <title>ChromaDB Integration - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/chroma</url>
  <content>    import typer
    from rich.prompt import Prompt
    from typing import Optional
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.chroma import ChromaDb
    
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=ChromaDb(collection="recipes"),
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=False)
    
    
    def pdf_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge_base=knowledge_base,
            use_tools=True,
            show_tool_calls=True,
            debug_mode=True,
        )
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(pdf_agent)</content>
</page>

<page>
  <title>Portkey - Phidata</title>
  <url>https://docs.phidata.com/examples/integrations/portkey</url>
  <content>Portkey Integration with Phidata
--------------------------------

[Portkey](https://portkey.ai/) is a 2-line upgrade to make your Phidata agents reliable, cost-efficient, and fast.

Portkey adds 4 core production capabilities to any Phidata agent:

1.  Routing to 200+ LLMs
2.  Making each LLM call more robust
3.  Full-stack tracing & cost, performance analytics
4.  Real-time guardrails to enforce behavior

Getting Started
---------------

1.  **Install Required Packages:**

2.  **Configure Phidata with Portkey:**

Generate your API key in the [Portkey Dashboard](https://app.portkey.ai/).

And, that’s it! With just this, you can start logging all of your Phidata requests and make them reliable.

3.  **Let’s Run your Agent**

Here’s the output from your Agent’s run on Portkey’s dashboard.

Key Features
------------

Portkey offers a range of advanced features to enhance your Phidata agents. Here’s an overview:

| Feature | Description |
| --- | --- |
| 🌐 [Multi-LLM Integration](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#interoperability) | Access 200+ LLMs with simple configuration changes |
| 🛡️ [Enhanced Reliability](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#reliability) | Implement fallbacks, load balancing, retries, and much more |
| 📊 [Advanced Metrics](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#metrics) | Track costs, tokens, latency, and 40+ custom metrics effortlessly |
| 🔍 [Detailed Traces and Logs](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#comprehensive-logging) | Gain insights into every agent action and decision |
| 🚧 [Guardrails](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#guardrails) | Enforce agent behavior with real-time checks on inputs and outputs |
| 🔄 [Continuous Optimization](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#continuous-improvement) | Capture user feedback for ongoing agent improvements |
| 💾 [Smart Caching](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#caching) | Reduce costs and latency with built-in caching mechanisms |
| 🔐 [Enterprise-Grade Security](https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#security-and-compliance) | Set budget limits and implement fine-grained access controls |

Colab Notebook
--------------

For a hands-on example of integrating Portkey with Phidata, check out our notebook:

Advanced Features
-----------------

### Interoperability

Easily switch between **200+ LLMs** by changing the `provider` and API key in your configuration.

#### Example: Switching from OpenAI to Azure OpenAI

### Reliability

Implement fallbacks, load balancing, and automatic retries to make your agents more resilient.

### Metrics

Agent runs are complex. Portkey automatically logs **40+ comprehensive metrics** for your AI agents, including cost, tokens used, latency, etc. Whether you need a broad overview or granular insights into your agent runs, Portkey’s customizable filters provide the metrics you need.

### Comprehensive Logging

Access detailed logs and traces of agent activities, function calls, and errors. Filter logs based on multiple parameters for in-depth analysis.

### Guardrails

Phidata agents, while powerful, can sometimes produce unexpected or undesired outputs. Portkey’s Guardrails feature helps enforce agent behavior in real-time, ensuring your Phidata agents operate within specified parameters. Verify both the **inputs** to and _outputs_ from your agents to ensure they adhere to specified formats and content guidelines.

### Continuous Improvement

Capture qualitative and quantitative user feedback on your requests to continuously enhance your agent performance.

### Caching

Reduce costs and latency with Portkey’s built-in caching system.

### Security and Compliance

Set budget limits on provider API keys and implement fine-grained user roles and permissions for both your application and the Portkey APIs.

Additional Resources
--------------------

*   [📘 Portkey Documentation](https://docs.portkey.ai/)
*   [🐦 Twitter](https://twitter.com/portkeyai)
*   [💬 Discord Community](https://discord.gg/DD7vgKK299)
*   [📊 Portkey App](https://app.portkey.ai/)

For more information on using these features and setting up your Config, please refer to the [Portkey documentation](https://docs.portkey.ai/).</content>
</page>

<page>
  <title>Container - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/docker/container</url>
  <content>[Phidata home page](https://docs.phidata.com/)

*   [Discord](https://phidata.link/discord)
*   [Community](https://community.phidata.com/)
*   [Log In](https://phidata.app/)
*   [
    
    phidatahq/phidata
    
    
    
    ](https://github.com/phidatahq/phidata)
*   [
    
    phidatahq/phidata
    
    
    
    ](https://github.com/phidatahq/phidata)

Docker

Container

[Documentation](https://docs.phidata.com/introduction)[Examples](https://docs.phidata.com/examples/introduction)[Templates](https://docs.phidata.com/templates/introduction)[Changelog](https://docs.phidata.com/changelog/overview)[Reference](https://docs.phidata.com/reference/agent)[FAQs](https://docs.phidata.com/faq/could-not-connect-to-docker)

[Phidata home page](https://docs.phidata.com/)

##### Templates

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/introduction)
*   Agent App
    
*   Agent API
    

##### How to

*   Manage Application
    
*   Manage Workspace
    

##### Workspace

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/workspace/introduction)
*   [
    
    Settings
    
    
    
    ](https://docs.phidata.com/templates/workspace/settings)
*   [
    
    Resources
    
    
    
    ](https://docs.phidata.com/templates/workspace/resources)

##### Apps

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/apps/introduction)
*   [
    
    Examples
    
    
    
    ](https://docs.phidata.com/templates/apps/examples)
*   [
    
    Features
    
    
    
    ](https://docs.phidata.com/templates/apps/features)

##### Resources

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/resources/introduction)
*   Docker
    
    *   [
        
        Docker
        
        
        
        ](https://docs.phidata.com/templates/resources/docker/introduction)
    *   [
        
        Container
        
        
        
        ](https://docs.phidata.com/templates/resources/docker/container)
*   AWS
    

Docker

This guide is in the works

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/templates/resources/docker/container.mdx)

[Docker](https://docs.phidata.com/templates/resources/docker/introduction)[AWS](https://docs.phidata.com/templates/resources/aws/introduction)</content>
</page>

<page>
  <title>ECS - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/aws/ecs</url>
  <content>[Phidata home page](https://docs.phidata.com/)

*   [Discord](https://phidata.link/discord)
*   [Community](https://community.phidata.com/)
*   [Log In](https://phidata.app/)
*   [
    
    phidatahq/phidata
    
    
    
    ](https://github.com/phidatahq/phidata)
*   [
    
    phidatahq/phidata
    
    
    
    ](https://github.com/phidatahq/phidata)

AWS

ECS

[Documentation](https://docs.phidata.com/introduction)[Examples](https://docs.phidata.com/examples/introduction)[Templates](https://docs.phidata.com/templates/introduction)[Changelog](https://docs.phidata.com/changelog/overview)[Reference](https://docs.phidata.com/reference/agent)[FAQs](https://docs.phidata.com/faq/could-not-connect-to-docker)

[Phidata home page](https://docs.phidata.com/)

##### Templates

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/introduction)
*   Agent App
    
*   Agent API
    

##### How to

*   Manage Application
    
*   Manage Workspace
    

##### Workspace

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/workspace/introduction)
*   [
    
    Settings
    
    
    
    ](https://docs.phidata.com/templates/workspace/settings)
*   [
    
    Resources
    
    
    
    ](https://docs.phidata.com/templates/workspace/resources)

##### Apps

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/apps/introduction)
*   [
    
    Examples
    
    
    
    ](https://docs.phidata.com/templates/apps/examples)
*   [
    
    Features
    
    
    
    ](https://docs.phidata.com/templates/apps/features)

##### Resources

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/resources/introduction)
*   Docker
    
*   AWS
    
    *   [
        
        AWS
        
        
        
        ](https://docs.phidata.com/templates/resources/aws/introduction)
    *   [
        
        ECS
        
        
        
        ](https://docs.phidata.com/templates/resources/aws/ecs)
    *   [
        
        RDS
        
        
        
        ](https://docs.phidata.com/templates/resources/aws/rds)

AWS

This guide is in the works

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/templates/resources/aws/ecs.mdx)

[AWS](https://docs.phidata.com/templates/resources/aws/introduction)[RDS](https://docs.phidata.com/templates/resources/aws/rds)</content>
</page>

<page>
  <title>RDS - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/aws/rds</url>
  <content>[Phidata home page](https://docs.phidata.com/)

*   [Discord](https://phidata.link/discord)
*   [Community](https://community.phidata.com/)
*   [Log In](https://phidata.app/)
*   [
    
    phidatahq/phidata
    
    
    
    ](https://github.com/phidatahq/phidata)
*   [
    
    phidatahq/phidata
    
    
    
    ](https://github.com/phidatahq/phidata)

AWS

RDS

[Documentation](https://docs.phidata.com/introduction)[Examples](https://docs.phidata.com/examples/introduction)[Templates](https://docs.phidata.com/templates/introduction)[Changelog](https://docs.phidata.com/changelog/overview)[Reference](https://docs.phidata.com/reference/agent)[FAQs](https://docs.phidata.com/faq/could-not-connect-to-docker)

[Phidata home page](https://docs.phidata.com/)

##### Templates

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/introduction)
*   Agent App
    
*   Agent API
    

##### How to

*   Manage Application
    
*   Manage Workspace
    

##### Workspace

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/workspace/introduction)
*   [
    
    Settings
    
    
    
    ](https://docs.phidata.com/templates/workspace/settings)
*   [
    
    Resources
    
    
    
    ](https://docs.phidata.com/templates/workspace/resources)

##### Apps

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/apps/introduction)
*   [
    
    Examples
    
    
    
    ](https://docs.phidata.com/templates/apps/examples)
*   [
    
    Features
    
    
    
    ](https://docs.phidata.com/templates/apps/features)

##### Resources

*   [
    
    Introduction
    
    
    
    ](https://docs.phidata.com/templates/resources/introduction)
*   Docker
    
*   AWS
    
    *   [
        
        AWS
        
        
        
        ](https://docs.phidata.com/templates/resources/aws/introduction)
    *   [
        
        ECS
        
        
        
        ](https://docs.phidata.com/templates/resources/aws/ecs)
    *   [
        
        RDS
        
        
        
        ](https://docs.phidata.com/templates/resources/aws/rds)

AWS

This guide is in the works

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/templates/resources/aws/rds.mdx)

[ECS](https://docs.phidata.com/templates/resources/aws/ecs)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/resources/docker/templates/apps/introduction</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Production Application - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/production-app#build-your-production-image</url>
  <content>Your production application runs on AWS and its resources are defined in the `workspace/prd_resources.py` file. This guide shows how to:

1.  [Build a production image](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/production-app#build-your-production-image)
2.  [Update ECS Task Definitions](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/production-app#ecs-task-definition)
3.  [Update ECS Services](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/production-app#ecs-service)

Workspace Settings
------------------

The `WorkspaceSettings` object in the `workspace/settings.py` file defines common settings used by your workspace apps and resources.

Build your production image
---------------------------

Your application uses the `phidata` images by default. To use your own image:

*   Create a Repository in `ECR` and authenticate or use `Dockerhub`.
*   Open `workspace/settings.py` file
*   Update the `image_repo` to your image repository
*   Set `build_images=True` and `push_images=True`
*   Optional - Set `build_images=False` and `push_images=False` to use an existing image in the repository

### Create an ECR Repository

To use ECR, **create the image repo and authenticate with ECR** before pushing images.

**1\. Create the image repository in ECR**

The repo name should match the `ws_name`. Meaning if you’re using the default workspace name, the repo name would be `ai`.

**2\. Authenticate with ECR**

You can also use a helper script to avoid running the full command

### Update the `WorkspaceSettings`

### Build a new image

Build the production image using:

To `force` rebuild images, use the `--force` or `-f` flag

Because the only docker resources in the production env are docker images, you can also use:

ECS Task Definition
-------------------

If you updated the Image, CPU, Memory or Environment Variables, update the Task Definition using:

ECS Service
-----------

To redeploy the production application, update the ECS Service using:</content>
</page>

<page>
  <title>SSH Access - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/ssh-access</url>
  <content>SSH Access is an important part of the developer workflow.

Dev SSH Access
--------------

SSH into the dev containers using the `docker exec` command

    docker exec -it ai-api zsh
    

Production SSH Access
---------------------

Your ECS tasks are already enabled with SSH access. SSH into the production containers using:

    ECS_CLUSTER=ai-app-prd-cluster
    TASK_ARN=$(aws ecs list-tasks --cluster ai-app-prd-cluster --query "taskArns[0]" --output text)
    CONTAINER_NAME=ai-api-prd
    
    aws ecs execute-command --cluster $ECS_CLUSTER \
        --task $TASK_ARN \
        --container $CONTAINER_NAME \
        --interactive \
        --command "zsh"</content>
</page>

<page>
  <title>Use Custom Domain and HTTPS - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/domain-https</url>
  <content>1.  Register your domain with [Route 53](https://us-east-1.console.aws.amazon.com/route53/).
2.  Point the domain to the loadbalancer DNS.

### Custom domain for your Streamlit App

Create a record in the Route53 console to point `app.[YOUR_DOMAIN]` to the Streamlit App.

You can visit the app at [http://app.aidev.run](http://app.aidev.run/)

### Custom domain for your FastApi App

Create a record in the Route53 console to point `api.[YOUR_DOMAIN]` to the FastApi App.

You can access the api at [http://api.aidev.run](http://api.aidev.run/)

Add HTTPS
---------

To add HTTPS:

1.  Create a certificate using [AWS ACM](https://us-east-1.console.aws.amazon.com/acm). Request a certificat for `*.[YOUR_DOMAIN]`

2.  Creating records in Route 53.

3.  Add the certificate ARN to Apps

Update the `llm-app/workspace/prd_resources.py` file and add the `load_balancer_certificate_arn` to the `FastApi` and `Streamlit` Apps.

workspace/prd\_resources.py

4.  Create new Loadbalancer Listeners

Create new listeners for the loadbalancer to pickup the HTTPs configuration.

After this, `https` should be working on your custom domain.

5.  Update existing listeners to redirect HTTP to HTTPS

After this, all HTTP requests should redirect to HTTPS automatically.

*   [Use a custom domain](#use-a-custom-domain)
*   [Custom domain for your Streamlit App](#custom-domain-for-your-streamlit-app)
*   [Custom domain for your FastApi App](#custom-domain-for-your-fastapi-app)
*   [Add HTTPS](#add-https)</content>
</page>

<page>
  <title>CI/CD - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/ci-cd</url>
  <content>Phidata templates come pre-configured with [Github Actions](https://docs.github.com/en/actions) for CI/CD. We can

1.  [Test and Validate on every PR](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/ci-cd#test-and-validate-on-every-pr)
2.  [Build Docker Images with Github Releases](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/ci-cd#build-docker-images-with-github-releases)
3.  [Build ECR Images with Github Releases](https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/ci-cd#build-ecr-images-with-github-releases)

Test and Validate on every PR
-----------------------------

Whenever a PR is opened against the `main` branch, a validate script runs that ensures

1.  The changes are formatted using ruff
2.  All unit-tests pass
3.  The changes don’t have any typing or linting errors.

Checkout the `.github/workflows/validate.yml` file for more information.

Build Docker Images with Github Releases
----------------------------------------

If you’re using [Dockerhub](https://hub.docker.com/) for images, you can buld and push the images throug a Github Release. This action is defined in the `.github/workflows/docker-images.yml` file.

1.  Create a [Docker Access Token](https://hub.docker.com/settings/security) for Github Actions

2.  Create secret variables `DOCKERHUB_REPO`, `DOCKERHUB_TOKEN` and `DOCKERHUB_USERNAME` in your github repo. These variables are used by the action in `.github/workflows/docker-images.yml`

3.  Run workflow using a Github Release

This workflow is configured to run when a release is created. Create a new release using:

Build ECR Images with Github Releases
-------------------------------------

If you’re using ECR for images, you can buld and push the images through a Github Release. This action is defined in the `.github/workflows/ecr-images.yml` file and uses the new OpenID Connect (OIDC) approach to request the access token, without using IAM access keys.

We will follow this [guide](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/) to create an IAM role which will be used by the github action.

1.  Open the IAM console.
2.  In the left navigation menu, choose Identity providers.
3.  In the Identity providers pane, choose Add provider.
4.  For Provider type, choose OpenID Connect.
5.  For Provider URL, enter the URL of the GitHub OIDC IdP: [https://token.actions.githubusercontent.com](https://token.actions.githubusercontent.com/)
6.  Get thumbprint to verify the server certificate
7.  For Audience, enter sts.amazonaws.com.

Verify the information matches the screenshot below and Add provider

8.  Assign a Role to the provider.

9.  Create a new role.

10.  Confirm that Web identity is already selected as the trusted entity and the Identity provider field is populated with the IdP. In the Audience list, select sts.amazonaws.com, and then select Next.

11.  Add the `AmazonEC2ContainerRegistryPowerUser` permission to this role.
    
12.  Create the role with the name `GithubActionsRole`.
    
13.  Find the role `GithubActionsRole` and copy the ARN.
    

14.  Create the ECR Repositories: `llm` and `jupyter-llm` which are built by the workflow.

15.  Update the workflow with the `GithubActionsRole` ARN and ECR Repository.

.github/workflows/ecr-images.yml

16.  Update the `docker-images` workflow to **NOT** run on a release

.github/workflows/docker-images.yml

17.  Run workflow using a Github Release</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/agent-api/templates/how-to/production-app</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Add Secrets - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/secrets</url>
  <content>Secret management is a critical part of your application security and should be taken seriously.

Local secrets are defined in the `worspace/secrets` directory which is excluded from version control (see `.gitignore`). Its contents should be handled with the same security as passwords.

Production secrets are managed by [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

Development Secrets
-------------------

Apps running locally can read secrets using a `yaml` file, for example:

Production Secrets
------------------

`AWS Secrets` are used to manage production secrets, which are read by the production apps.

Read the secret in production apps using:

Production resources can also read secrets using yaml files but we highly recommend using [AWS Secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

*   [Development Secrets](#development-secrets)
*   [Production Secrets](#production-secrets)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/templates/how-to/new-users</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Environment variables - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/env-vars</url>
  <content>Environment variables can be added to resources using the `env_vars` parameter or the `env_file` parameter pointing to a `yaml` file. Examples

    dev_fastapi = FastApi(
        ...
        env_vars={
            "RUNTIME_ENV": "dev",
            # Get the OpenAI API key from the local environment
            "OPENAI_API_KEY": getenv("OPENAI_API_KEY"),
            # Database configuration
            "DB_HOST": dev_db.get_db_host(),
            "DB_PORT": dev_db.get_db_port(),
            "DB_USER": dev_db.get_db_user(),
            "DB_PASS": dev_db.get_db_password(),
            "DB_DATABASE": dev_db.get_db_database(),
            # Wait for database to be available before starting the application
            "WAIT_FOR_DB": ws_settings.dev_db_enabled,
            # Migrate database on startup using alembic
            # "MIGRATE_DB": ws_settings.prd_db_enabled,
        },
        ...
    )
    

    prd_fastapi = FastApi(
        ...
        env_vars={
            "RUNTIME_ENV": "prd",
            # Get the OpenAI API key from the local environment
            "OPENAI_API_KEY": getenv("OPENAI_API_KEY"),
            # Database configuration
            "DB_HOST": AwsReference(prd_db.get_db_endpoint),
            "DB_PORT": AwsReference(prd_db.get_db_port),
            "DB_USER": AwsReference(prd_db.get_master_username),
            "DB_PASS": AwsReference(prd_db.get_master_user_password),
            "DB_DATABASE": AwsReference(prd_db.get_db_name),
            # Wait for database to be available before starting the application
            "WAIT_FOR_DB": ws_settings.prd_db_enabled,
            # Migrate database on startup using alembic
            # "MIGRATE_DB": ws_settings.prd_db_enabled,
        },
        ...
    )
    

The apps in your templates are already configured to read environment variables.</content>
</page>

<page>
  <title>Database Tables - Phidata</title>
  <url>https://docs.phidata.com/templates/how-to/database-tables</url>
  <content>Phidata templates come pre-configured with [SqlAlchemy](https://www.sqlalchemy.org/) and [alembic](https://alembic.sqlalchemy.org/en/latest/) to manage databases. The general workflow to add a table is:

1.  Add table definition to the `db/tables` directory.
2.  Import the table class in the `db/tables/__init__.py` file.
3.  Create a database migration.
4.  Run database migration.

Table Definition
----------------

Let’s create a `UsersTable`, copy the following code to `db/tables/user.py`

Update the `db/tables/__init__.py` file:

Creat a database revision
-------------------------

Run the alembic command to create a database migration in the dev container:

Migrate dev database
--------------------

Run the alembic command to migrate the dev database:

### Optional: Add test user

Now lets’s add a test user. Copy the following code to `db/tables/test_add_user.py`

db/tables/test\_add\_user.py

Run the script to add a test adding a user:

Migrate production database
---------------------------

We recommended migrating the production database by setting the environment variable `MIGRATE_DB = True` and restarting the production service. This runs `alembic -c db/alembic.ini upgrade head` from the entrypoint script at container startup.

### Update the `workspace/prd_resources.py` file

workspace/prd\_resources.py

### Update the ECS Task Definition

Because we updated the Environment Variables, we need to update the Task Definition:

### Update the ECS Service

After updating the task definition, redeploy the production application:

Manually migrate prodution database
-----------------------------------

Another approach is to SSH into the production container to run the migration manually. Your ECS tasks are already enabled with SSH access. Run the alembic command to migrate the production database:

* * *

How the migrations directory was created
----------------------------------------

The migrations directory was created using:

*   After running the above command, the `db/migrations` directory should be created.
*   Update `alembic.ini`
    *   set `script_location = db/migrations`
    *   uncomment `black` hook in `[post_write_hooks]`
*   Update `db/migrations/env.py` file following [this link](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
*   Add the following function to `configure` to only include tables in the target\_metadata</content>
</page>

<page>
  <title>Model Base - Phidata</title>
  <url>https://docs.phidata.com/reference/model/base</url>
  <content>Base Params
-----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | \- | ID of the model to use. Alias: "model" |
| `name` | `Optional[str]` | `None` | Name for this Model. Not sent to the Model API. |
| `provider` | `Optional[str]` | `None` | Provider for this Model. Not sent to the Model API. |
| `metrics` | `Dict[str, Any]` | `{}` | Metrics collected for this Model. Not sent to the Model API. |
| `response_format` | `Optional[Any]` | `None` | Format of the response. |
| `tools` | `Optional[List[Union[Tool, Dict]]]` | `None` | A list of tools provided to the Model. |
| `tool_choice` | `Optional[Union[str, Dict[str, Any]]]` | `None` | Controls which (if any) function is called by the model. |
| `run_tools` | `bool` | `True` | If True, runs the tool before sending back the response content. |
| `show_tool_calls` | `Optional[bool]` | `None` | If True, shows function calls in the response. |
| `tool_call_limit` | `Optional[int]` | `None` | Maximum number of tool calls allowed. |
| `functions` | `Optional[Dict[str, Function]]` | `None` | Functions extracted from the tools. Not sent to the Model API. |
| `function_call_stack` | `Optional[List[FunctionCall]]` | `None` | Function call stack. |
| `system_prompt` | `Optional[str]` | `None` | System prompt from the model added to the Agent. |
| `instructions` | `Optional[List[str]]` | `None` | Instructions from the model added to the Agent. |
| `session_id` | `Optional[str]` | `None` | Session ID of the calling Agent or Workflow. |
| `structured_outputs` | `Optional[bool]` | `None` | Whether to use the structured outputs with this Model. |
| `supports_structured_outputs` | `bool` | `False` | Whether the Model supports structured outputs. |
| `add_images_to_message_content` | `bool` | `False` | Whether to add images to the message content. |</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/development-app#build-your-development-image</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/templates/agent-app/templates/how-to/production-app</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>YAML Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/yaml</url>
  <content>Phidata supports using local YAML files as a storage backend for Agents using the `YamlFileAgentStorage` class.

Usage
-----

    from phi.agent import Agent
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.storage.agent.yaml import YamlFileAgentStorage
    
    agent = Agent(
        storage=YamlFileAgentStorage(path="tmp/agent_sessions_yaml"),
        tools=[DuckDuckGo()],
        add_history_to_messages=True,
    )
    
    agent.print_response("How many people live in Canada?")
    agent.print_response("What is their national anthem called?")
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dir_path` | `str` | \- | Path to the folder to be used to store the YAML files. |</content>
</page>

<page>
  <title>Toolkits - Phidata</title>
  <url>https://docs.phidata.com/tools/toolkits</url>
  <content>A **Toolkit** is a collection of functions that can be added to an Agent. The functions in a Toolkit are designed to work together, share internal state and provide a better development experience.

The following **Toolkits** are available to use

[

Apify
-----

Tools to use Apify Actors.



](https://docs.phidata.com/tools/apify)[

Arxiv
-----

Tools to read arXiv papers.



](https://docs.phidata.com/tools/arxiv)[

Calculator
----------

Tools to perform calculations.



](https://docs.phidata.com/tools/calculator)[

CalCom
------

Tools to interact with the Cal.com API.



](https://docs.phidata.com/tools/calcom)[

Composio
--------

Tools to compose complex workflows.



](https://docs.phidata.com/tools/composio)[

Crawl4AI
--------

Tools to crawl web data.



](https://docs.phidata.com/tools/crawl4ai)[

CSV
---

Tools to work with CSV files.



](https://docs.phidata.com/tools/csv)[

DuckDb
------

Tools to run SQL using DuckDb.



](https://docs.phidata.com/tools/duckdb)[

DuckDuckGo
----------

Tools to search the web using DuckDuckGo.



](https://docs.phidata.com/tools/duckduckgo)[

Dalle
-----

Tools to interact with Dalle.



](https://docs.phidata.com/tools/dalle)[

Email
-----

Tools to send emails.



](https://docs.phidata.com/tools/email)[

Exa
---

Tools to search the web using Exa.



](https://docs.phidata.com/tools/exa)[

File
----

Tools to read and write files.



](https://docs.phidata.com/tools/file)[

Firecrawl
---------

Tools to crawl the web using Firecrawl.



](https://docs.phidata.com/tools/firecrawl)[

GitHub
------

Tools to interact with GitHub.



](https://docs.phidata.com/tools/github)[

Google Search
-------------

Tools to search Google.



](https://docs.phidata.com/tools/googlesearch)[

HackerNews
----------

Tools to read Hacker News articles.



](https://docs.phidata.com/tools/hackernews)[

Jina Reader
-----------

Tools for neural search and AI services using Jina.



](https://docs.phidata.com/tools/jina_reader)[

Jira
----

Tools to interact with Jira.



](https://docs.phidata.com/tools/jira)[

MLX Transcribe
--------------

Tools to transcribe audio using MLX.



](https://docs.phidata.com/tools/mlx_transcribe)[

ModelsLabs
----------

Tools to generate videos using ModelsLabs.



](https://docs.phidata.com/tools/models_labs)[

Newspaper
---------

Tools to read news articles.



](https://docs.phidata.com/tools/newspaper)[

Newspaper4k
-----------

Tools to read articles using Newspaper4k.



](https://docs.phidata.com/tools/newspaper4k)[

OpenBB
------

Tools to search for stock data using OpenBB.



](https://docs.phidata.com/tools/openbb)[

Pandas
------

Tools to manipulate data using Pandas.



](https://docs.phidata.com/tools/pandas)[

Postgres
--------

Tools to interact with PostgreSQL databases.



](https://docs.phidata.com/tools/postgres)[

Pubmed
------

Tools to search Pubmed.



](https://docs.phidata.com/tools/pubmed)[

Python
------

Tools to write and run Python code.



](https://docs.phidata.com/tools/python)[

Resend
------

Tools to send emails using Resend.



](https://docs.phidata.com/tools/resend)[

SearxNG
-------

Tools to search the web using SearxNG.



](https://docs.phidata.com/tools/searxng)[

Serpapi
-------

Tools to search Google, YouTube, and more using Serpapi.



](https://docs.phidata.com/tools/serpapi)[

Slack
-----

Tools to interact with Slack.



](https://docs.phidata.com/tools/slack)[

Shell
-----

Tools to run shell commands.



](https://docs.phidata.com/tools/shell)[

Sleep
-----

Tools to pause execution for a given number of seconds.



](https://docs.phidata.com/tools/sleep)[

Spider
------

Tools to crawl websites.



](https://docs.phidata.com/tools/spider)[

SQL
---

Tools to run SQL queries.



](https://docs.phidata.com/tools/sql)[

Twitter
-------

Tools to interact with Twitter.



](https://docs.phidata.com/tools/twitter)[

Tavily
------

Tools to search the web using Tavily.



](https://docs.phidata.com/tools/tavily)[

Website
-------

Tools to scrape websites.



](https://docs.phidata.com/tools/website)[

Wikipedia
---------

Tools to search Wikipedia.



](https://docs.phidata.com/tools/wikipedia)[

YFinance
--------

Tools to search Yahoo Finance.



](https://docs.phidata.com/tools/yfinance)[

YouTube
-------

Tools to search YouTube.



](https://docs.phidata.com/tools/youtube)[

Zendesk
-------

Tools to search Zendesk.



](https://docs.phidata.com/tools/zendesk)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/models/introduction</url>
  <content>Language Models are machine-learning programs that are trained to understand natural language and code. They provide reasoning and planning capabilities to Agents.

Use any `model` with an Agent like:

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        description="Share 15 minute healthy recipes.",
        markdown=True,
    )
    agent.print_response("Share a breakfast recipe.", stream=True)
    

Phidata supports the following model providers:

*   [OpenAI](https://docs.phidata.com/models/openai)
*   [Anthropic](https://docs.phidata.com/models/anthropic)
*   [AWS Bedrock](https://docs.phidata.com/models/aws-bedrock)
*   [Azure](https://docs.phidata.com/models/azure)
*   [Cohere](https://docs.phidata.com/models/cohere)
*   [DeepSeek](https://docs.phidata.com/models/deepseek)
*   [Fireworks](https://docs.phidata.com/models/fireworks)
*   [Google](https://docs.phidata.com/models/google)
*   [Groq](https://docs.phidata.com/models/groq)
*   [Mistral](https://docs.phidata.com/models/mistral)
*   [Ollama](https://docs.phidata.com/models/ollama)
*   [OpenAI Like](https://docs.phidata.com/models/openai-like)
*   [OpenRouter](https://docs.phidata.com/models/openrouter)
*   [Sambanova](https://docs.phidata.com/models/sambanova)
*   [Together](https://docs.phidata.com/models/together)
*   [VertexAI](https://docs.phidata.com/models/vertexai)</content>
</page>

<page>
  <title>Functions - Phidata</title>
  <url>https://docs.phidata.com/tools/functions</url>
  <content>Any python function can be used as a tool by an Agent. **We highly recommend** creating functions specific to your workflow and adding them to your Agents.

For example, here’s how to use a `get_top_hackernews_stories` function as a tool:

    import json
    import httpx
    
    from phi.agent import Agent
    
    
    def get_top_hackernews_stories(num_stories: int = 10) -> str:
        """Use this function to get top stories from Hacker News.
    
        Args:
            num_stories (int): Number of stories to return. Defaults to 10.
    
        Returns:
            str: JSON string of top stories.
        """
    
        # Fetch top story IDs
        response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        story_ids = response.json()
    
        # Fetch story details
        stories = []
        for story_id in story_ids[:num_stories]:
            story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
            story = story_response.json()
            if "text" in story:
                story.pop("text", None)
            stories.append(story)
        return json.dumps(stories)
    
    agent = Agent(tools=[get_top_hackernews_stories], show_tool_calls=True, markdown=True)
    agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)</content>
</page>

<page>
  <title>Hackernews Team - Phidata</title>
  <url>https://docs.phidata.com/examples/teams/hackernews</url>
  <content>Agent Teams

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/teams/hackernews.mdx)

[Investment Team](https://docs.phidata.com/examples/teams/investment)[Sql Agent](https://docs.phidata.com/examples/use-case/sql)</content>
</page>

<page>
  <title>Research Team - Phidata</title>
  <url>https://docs.phidata.com/examples/teams/research</url>
  <content>Agent Teams

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/teams/research.mdx)

[Portkey](https://docs.phidata.com/examples/integrations/portkey)[Journalist Team](https://docs.phidata.com/examples/teams/journalist)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/_sites/docs.phidata.com/examples/integrations/portkey#interoperability</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/production-app#build-your-production-image</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>OpenAI - Phidata</title>
  <url>https://docs.phidata.com/reference/model/openai</url>
  <content>Example
-------

OpenAI Params
-------------

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o"` | The id of the OpenAI model to use. |
| `name` | `str` | `"OpenAIChat"` | The name of this chat model instance. |
| `provider` | `str` | `"OpenAI " + id` | The provider of the model. |
| `store` | `Optional[bool]` | `None` | Whether or not to store the output of this chat completion request for use in the model distillation or evals products. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | `None` | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | `None` | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | `None` | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | `None` | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | `None` | How many log probability results to return per token. |
| `user` | `Optional[str]` | `None` | A unique identifier representing your end-user. |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling. |
| `extra_headers` | `Optional[Any]` | `None` | Additional headers to send with the request. |
| `extra_query` | `Optional[Any]` | `None` | Additional query parameters to send with the request. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with OpenAI. |
| `organization` | `Optional[str]` | `None` | The organization to use for API requests. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for API requests. |
| `timeout` | `Optional[float]` | `None` | The timeout for API requests. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[OpenAIClient]` | `None` | The OpenAI client instance. |
| `async_client` | `Optional[AsyncOpenAIClient]` | `None` | The asynchronous OpenAI client instance. |
| `structured_outputs` | `bool` | `False` | Whether to use the structured outputs from the Model. |
| `supports_structured_outputs` | `bool` | `True` | Whether the Model supports structured outputs. |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content. |

For more information, please refer to the [OpenAI docs](https://platform.openai.com/docs/api-reference/chat/create) as well.

`OpenAIChat` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/_sites/docs.phidata.com/templates/how-to/ci-cd#test-and-validate-on-every-pr</url>
  <content>    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.tools.yfinance import YFinanceTools
    
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
        instructions=["Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
    )
    
    agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)</content>
</page>

<page>
  <title>OpenAILike - Phidata</title>
  <url>https://docs.phidata.com/reference/model/openai-like</url>
  <content>[​](#example)

Example
------------------------

[​](#openai-params)

OpenAI Params
------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | \- | The name of the model to be used for generating responses. |
| `api_key` | `str` | \- | The API key for authenticating requests to the service. |
| `base_url` | `str` | \- | The base URL for making API requests to the service. |

For more information, please refer to the [OpenAI docs](https://platform.openai.com/docs/api-reference/chat/create) as well.

`OpenAILike` is a subclass of the [OpenAI](https://docs.phidata.com/reference/model/openai) class and has access to the same params.</content>
</page>

<page>
  <title>Aws Bedrock - Phidata</title>
  <url>https://docs.phidata.com/reference/model/aws</url>
  <content>AWS Bedrock Params
------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"anthropic.claude-3-sonnet-20240229-v1:0"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AwsBedrockAnthropicClaude"` | The name identifier for the Claude agent. |
| `provider` | `str` | `"AwsBedrock"` | The provider of the model. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_p` | `Optional[float]` | \- | The nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `top_k` | `Optional[int]` | \- | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `stop_sequences` | `Optional[List[str]]` | \- | A list of sequences where the API will stop generating further tokens. |
| `anthropic_version` | `str` | `"bedrock-2023-05-31"` | The version of the Anthropic API to use. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for the request, provided as a dictionary. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional client parameters for initializing the `AwsBedrock` client, provided as a dictionary. |

`AwsBedrock` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Azure - Phidata</title>
  <url>https://docs.phidata.com/reference/model/azure</url>
  <content>Example
-------

Azure Params
------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | \- | The specific model ID used for generating responses. This field is required. |
| `name` | `str` | `"AzureOpenAIChat"` | The name identifier for the agent. |
| `provider` | `str` | `"Azure"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Azure OpenAI service. |
| `api_version` | `str` | `"2024-02-01"` | The version of the Azure OpenAI API to use. |
| `azure_endpoint` | `Optional[str]` | \- | The endpoint URL for the Azure OpenAI service. |
| `azure_deployment` | `Optional[str]` | \- | The deployment name or ID in Azure. |
| `base_url` | `Optional[str]` | \- | The base URL for making API requests to the Azure OpenAI service. |
| `azure_ad_token` | `Optional[str]` | \- | The Azure Active Directory token for authenticating requests. |
| `azure_ad_token_provider` | `Optional[Any]` | \- | The provider for obtaining Azure Active Directory tokens. |
| `organization` | `Optional[str]` | \- | The organization associated with the API requests. |
| `openai_client` | `Optional[AzureOpenAIClient]` | \- | An instance of AzureOpenAIClient provided for making API requests. |

`Azure` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Anthropic Claude - Phidata</title>
  <url>https://docs.phidata.com/reference/model/claude</url>
  <content>Example
-------

Claude Params
-------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"claude-3-5-sonnet-20240620"` | The id of the Anthropic Claude model to use |
| `name` | `str` | `"Claude"` | The name of the model |
| `provider` | `str` | `"Anthropic"` | The provider of the model |
| `max_tokens` | `Optional[int]` | `1024` | Maximum number of tokens to generate in the chat completion |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output |
| `stop_sequences` | `Optional[List[str]]` | `None` | A list of strings that the model should stop generating text at |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling |
| `top_k` | `Optional[int]` | `None` | Controls diversity via top-k sampling |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Anthropic |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration |
| `client` | `Optional[AnthropicClient]` | `None` | A pre-configured instance of the Anthropic client |

`Claude` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>DeepSeek - Phidata</title>
  <url>https://docs.phidata.com/reference/model/deepseek</url>
  <content>Example
-------

DeepSeek Params
---------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"deepseek-chat"` | The specific model ID used for generating responses. |
| `name` | `str` | `"DeepSeekChat"` | The name identifier for the DeepSeek model. |
| `provider` | `str` | `"DeepSeek"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key used for authenticating requests to the DeepSeek service. Retrieved from the environment variable `DEEPSEEK_API_KEY`. |
| `base_url` | `str` | `"https://api.deepseek.com"` | The base URL for making API requests to the DeepSeek service. |

Model Params
------------

`DeepSeek` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Cohere - Phidata</title>
  <url>https://docs.phidata.com/reference/model/cohere</url>
  <content>Example
-------

Cohere Params
-------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"command-r-08-2024"` | The specific model ID used for generating responses. |
| `name` | `str` | `"CohereChat"` | The name identifier for the agent. |
| `provider` | `str` | `"Cohere"` | The provider of the model. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `max_tokens` | `Optional[int]` | \- | The maximum number of tokens to generate in the response. |
| `top_k` | `Optional[int]` | \- | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `top_p` | `Optional[float]` | \- | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `frequency_penalty` | `Optional[float]` | \- | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `presence_penalty` | `Optional[float]` | \- | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `add_chat_history` | `bool` | `False` | Whether to add chat history to the Cohere messages instead of using the conversation\_id. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Cohere service. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `cohere_client` | `Optional[CohereClient]` | \- | A pre-configured instance of the Cohere client. |

`Cohere` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Gemini - Google AI Studio - Phidata</title>
  <url>https://docs.phidata.com/reference/model/gemini</url>
  <content>Example
-------

Gemini Params
-------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gemini-1.5-flash"` | The specific Gemini model ID to use. |
| `name` | `str` | `"Gemini"` | The name of this Gemini model instance. |
| `provider` | `str` | `"Google"` | The provider of the model. |
| `function_declarations` | `Optional[List[FunctionDeclaration]]` | `None` | List of function declarations for the model. |
| `generation_config` | `Optional[Any]` | `None` | Configuration for text generation. |
| `safety_settings` | `Optional[Any]` | `None` | Safety settings for the model. |
| `generative_model_kwargs` | `Optional[Dict[str, Any]]` | `None` | Additional keyword arguments for the generative model. |
| `api_key` | `Optional[str]` | `None` | API key for authentication. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for the client. |
| `client` | `Optional[GenerativeModel]` | `None` | The underlying generative model client. |

`Gemini` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Fireworks - Phidata</title>
  <url>https://docs.phidata.com/reference/model/fireworks</url>
  <content>Example
-------

Fireworks Params
----------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"accounts/fireworks/models/firefunction-v2"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Fireworks: {id}"` | The name identifier for the agent. Defaults to "Fireworks: " followed by the model ID. |
| `provider` | `str` | `"Fireworks"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the service. Retrieved from the environment variable FIREWORKS\_API\_KEY. |
| `base_url` | `str` | `"https://api.fireworks.ai/inference/v1"` | The base URL for making API requests to the Fireworks service. |

`Fireworks` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Gemini - VertexAI - Phidata</title>
  <url>https://docs.phidata.com/reference/model/vertexai</url>
  <content>Example
-------

Gemini Params
-------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gemini-1.5-flash"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Gemini"` | The name identifier for the agent. |
| `provider` | `str` | `"VertexAI"` | The provider of the model. |
| `function_declarations` | `Optional[List[FunctionDeclaration]]` | \- | A list of function declarations that the model can utilize during the response generation process. |
| `generation_config` | `Optional[Any]` | \- | Configuration settings for the generation process, such as parameters for controlling output behavior. |
| `safety_settings` | `Optional[Any]` | \- | Settings related to safety measures, ensuring the generation of appropriate and safe content. |
| `generative_model_kwargs` | `Optional[Dict[str, Any]]` | \- | Additional keyword arguments for the generative model. |
| `client` | `Optional[GenerativeModel]` | \- | A pre-configured instance of the Gemini client. |

`VertexAI` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Groq - Phidata</title>
  <url>https://docs.phidata.com/reference/model/groq</url>
  <content>Example
-------

Groq Params
-----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama3-groq-70b-8192-tool-use-preview"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Groq"` | The name identifier for the agent. |
| `provider` | `str` | `"Groq"` | The provider of the model. |
| `frequency_penalty` | `Optional[float]` | \- | A number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `logit_bias` | `Optional[Any]` | \- | A JSON object that modifies the likelihood of specified tokens appearing in the completion by mapping token IDs to bias values between -100 and 100. |
| `logprobs` | `Optional[bool]` | \- | Whether to return log probabilities of the output tokens. |
| `max_tokens` | `Optional[int]` | \- | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | \- | A number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `response_format` | `Optional[Dict[str, Any]]` | \- | Specifies the format that the model must output. Setting to `{ "type": "json_object" }` enables JSON mode, ensuring the message generated is valid JSON. |
| `seed` | `Optional[int]` | \- | A seed value for deterministic sampling, ensuring repeated requests with the same seed and parameters return the same result. |
| `stop` | `Optional[Union[str, List[str]]]` | \- | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_logprobs` | `Optional[int]` | \- | The number of top log probabilities to return for each generated token. |
| `top_p` | `Optional[float]` | \- | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `user` | `Optional[str]` | \- | A unique identifier representing your end-user, helping to monitor and detect abuse. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the service. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | \- | The base URL for making API requests to the service. |
| `timeout` | `Optional[int]` | \- | The timeout duration for requests, specified in seconds. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retry attempts for failed requests. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `groq_client` | `Optional[GroqClient]` | \- | An instance of GroqClient provided for making API requests. |

`Groq` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>HuggingFace - Phidata</title>
  <url>https://docs.phidata.com/reference/model/huggingface</url>
  <content>Example
-------

HuggingFace Params
------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"meta-llama/Meta-Llama-3-8B-Instruct"` | The id of the HuggingFace model to use. |
| `name` | `str` | `"HuggingFaceChat"` | The name of this chat model instance. |
| `provider` | `str` | `"HuggingFace"` | The provider of the model. |
| `store` | `Optional[bool]` | \- | Whether or not to store the output of this chat completion request. |
| `frequency_penalty` | `Optional[float]` | \- | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | \- | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | \- | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | \- | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | \- | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | \- | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | \- | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | \- | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | \- | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | \- | How many log probability results to return per token. |
| `top_p` | `Optional[float]` | \- | Controls diversity via nucleus sampling. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | \- | The Access Token for authenticating with HuggingFace. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | \- | The base URL for API requests. |
| `timeout` | `Optional[float]` | \- | The timeout for API requests. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | \- | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | \- | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | \- | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `client` | `Optional[InferenceClient]` | \- | The HuggingFace Hub Inference client instance. |
| `async_client` | `Optional[AsyncInferenceClient]` | \- | The asynchronous HuggingFace Hub client instance. |

`HuggingFaceChat` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Mistral - Phidata</title>
  <url>https://docs.phidata.com/reference/model/mistral</url>
  <content>Example
-------

Mistral Params
--------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistral-large-latest"` | The ID of the model. |
| `name` | `str` | `"MistralChat"` | The name of the model. |
| `provider` | `str` | `"Mistral"` | The provider of the model. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in output generation. |
| `max_tokens` | `Optional[int]` | `None` | Maximum number of tokens to generate. |
| `top_p` | `Optional[float]` | `None` | Controls diversity of output generation. |
| `random_seed` | `Optional[int]` | `None` | Seed for random number generation. |
| `safe_mode` | `bool` | `False` | Enables content filtering. |
| `safe_prompt` | `bool` | `False` | Applies content filtering to prompts. |
| `response_format` | `Optional[Union[Dict[str, Any], ChatCompletionResponse]]` | `None` | Specifies the desired response format. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional request parameters. |
| `api_key` | `Optional[str]` | `None` | Your Mistral API key. |
| `endpoint` | `Optional[str]` | `None` | Custom API endpoint URL. |
| `max_retries` | `Optional[int]` | `None` | Maximum number of API call retries. |
| `timeout` | `Optional[int]` | `None` | Timeout for API calls in seconds. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional client parameters. |
| `mistral_client` | `Optional[Mistral]` | `None` | Custom Mistral client instance. |

`MistralChat` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>Nvidia - Phidata</title>
  <url>https://docs.phidata.com/reference/model/nvidia</url>
  <content>Example
-------

Nvidia Params
-------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"nvidia/llama-3.1-nemotron-70b-instruct"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Nvidia"` | The name identifier for the Nvidia agent. |
| `provider` | `str` | \- | The provider of the model, combining "Nvidia" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Nvidia service. Retrieved from the environment variable `NVIDIA_API_KEY`. |
| `base_url` | `str` | `"https://integrate.api.nvidia.com/v1"` | The base URL for making API requests to the Nvidia service. |

`Nvidia` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Ollama - Phidata</title>
  <url>https://docs.phidata.com/reference/model/ollama</url>
  <content>Example
-------

Ollama Params
-------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama3.2"` | The ID of the model to use. |
| `name` | `str` | `"Ollama"` | The name of the model. |
| `provider` | `str` | `"Ollama llama3.2"` | The provider of the model. |
| `format` | `Optional[str]` | `None` | The format of the response. |
| `options` | `Optional[Any]` | `None` | Additional options to pass to the model. |
| `keep_alive` | `Optional[Union[float, str]]` | `None` | The keep alive time for the model. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass to the request. |
| `host` | `Optional[str]` | `None` | The host to connect to. |
| `timeout` | `Optional[Any]` | `None` | The timeout for the connection. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass to the client. |
| `client` | `Optional[OllamaClient]` | `None` | A pre-configured instance of the Ollama client. |
| `async_client` | `Optional[AsyncOllamaClient]` | `None` | A pre-configured instance of the asynchronous Ollama client. |

`Ollama` is a subclass of the [Model](https://docs.phidata.com/reference/model/base) class and has access to the same params.</content>
</page>

<page>
  <title>OpenRouter - Phidata</title>
  <url>https://docs.phidata.com/reference/model/openrouter</url>
  <content>Example
-------

OpenRouter Params
-----------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o"` | The specific model ID used for generating responses. |
| `name` | `str` | `"OpenRouter"` | The name identifier for the OpenRouter agent. |
| `provider` | `str` | \- | The provider of the model, combining "OpenRouter" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the OpenRouter service. Retrieved from the environment variable `OPENROUTER_API_KEY`. |
| `base_url` | `str` | `"https://openrouter.ai/api/v1"` | The base URL for making API requests to the OpenRouter service. |
| `max_tokens` | `int` | `1024` | The maximum number of tokens to generate in the response. |

`OpenRouter` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Sambanova - Phidata</title>
  <url>https://docs.phidata.com/reference/model/sambanova</url>
  <content>Example
-------

Sambanova Params
----------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"Meta-Llama-3.1-8B-Instruct"` | The id of the Sambanova model to use |
| `name` | `str` | `"Sambanova"` | The name of this chat model instance |
| `provider` | `str` | `"Sambanova"` | The provider of the model |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Sambanova (defaults to environment variable SAMBANOVA\_API\_KEY) |
| `base_url` | `str` | `"https://api.sambanova.ai/v1"` | The base URL for API requests |

`Sambanova` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Together - Phidata</title>
  <url>https://docs.phidata.com/reference/model/together</url>
  <content>Example
-------

Together Params
---------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistralai/Mixtral-8x7B-Instruct-v0.1"` | The id of the Together model to use. |
| `name` | `str` | `"Together"` | The name of this chat model instance. |
| `provider` | `str` | `"Together " + id` | The provider of the model. |
| `api_key` | `Optional[str]` | `None` | The API key to authorize requests to Together. Defaults to environment variable TOGETHER\_API\_KEY. |
| `base_url` | `str` | `"https://api.together.xyz/v1"` | The base URL for API requests. |
| `monkey_patch` | `bool` | `False` | Whether to apply monkey patching. |

`Together` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>xAI - Phidata</title>
  <url>https://docs.phidata.com/reference/model/xai</url>
  <content>Example
-------

xAI Params
----------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"grok-beta"` | The specific model ID used for generating responses. |
| `name` | `str` | `"xAI"` | The name identifier for the xAI agent. |
| `provider` | `str` | `"xAI"` | The provider of the model, combining "xAI" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the xAI service. Retrieved from the environment variable `XAI_API_KEY`. |
| `base_url` | `str` | `"https://api.xai.xyz/v1"` | The base URL for making API requests to the xAI service. |

`xAI` is a subclass of the [OpenAILike](https://docs.phidata.com/reference/model/openai-like) class and has access to the same params.</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/storage/introduction</url>
  <content>Agents come with built-in memory but it only lasts while the session is active. To continue conversations across sessions, we store Agent sessions in a database like PostgreSQL.

Storage is a necessary component when building user facing AI products as any production application will require users to be able to “continue” their conversation with the Agent.

The general syntax for adding storage to an Agent looks like:

The following databases are supported as a storage backend:

*   [PostgreSQL](https://docs.phidata.com/storage/postgres)
*   [Sqlite](https://docs.phidata.com/storage/sqlite)
*   [SingleStore](https://docs.phidata.com/storage/singlestore)
*   [DynamoDB](https://docs.phidata.com/storage/dynamodb)
*   [MongoDB](https://docs.phidata.com/storage/mongodb)</content>
</page>

<page>
  <title>Postgres Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/postgres</url>
  <content>Phidata supports using PostgreSQL as a storage backend for Agents using the `PgAgentStorage` class.

Usage
-----

Run PgVector
------------

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **PgVector** on port **5532** using:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `schema` | `Optional[str]` | `"ai"` | Schema name, default is "ai". |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_engine` | `Optional[Engine]` | `None` | Database engine to be used. |
| `schema_version` | `int` | `1` | Version of the schema, default is 1. |
| `auto_upgrade_schema` | `bool` | `False` | If true, automatically upgrades the schema when necessary. |</content>
</page>

<page>
  <title>Sqlite Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/sqlite</url>
  <content>Phidata supports using Sqlite as a storage backend for Agents using the `SqlAgentStorage` class.

Usage
-----

You need to provide either `db_url`, `db_file` or `db_engine`. The following example uses `db_file`.

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `schema` | `Optional[str]` | `"ai"` | Schema name, default is "ai". |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_engine` | `Optional[Engine]` | `None` | Database engine to be used. |
| `schema_version` | `int` | `1` | Version of the schema, default is 1. |
| `auto_upgrade_schema` | `bool` | `False` | If true, automatically upgrades the schema when necessary. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Singlestore Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/singlestore</url>
  <content>Phidata supports using Singlestore as a storage backend for Agents using the `S2AgentStorage` class.

Usage
-----

Obtain the credentials for Singlestore from [here](https://portal.singlestore.com/)

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `schema` | `Optional[str]` | `"ai"` | Schema name. |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_engine` | `Optional[Engine]` | `None` | Database engine to be used. |
| `schema_version` | `int` | `1` | Version of the schema. |
| `auto_upgrade_schema` | `bool` | `False` | If `true`, automatically upgrades the schema when necessary. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>DynamoDB Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/dynamodb</url>
  <content>Phidata supports using DynamoDB as a storage backend for Agents using the `DynamoDbAgentStorage` class.

Usage
-----

You need to provide `aws_access_key_id` and `aws_secret_access_key` parameters to the `DynamoDbAgentStorage` class.

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `region_name` | `Optional[str]` | `None` | Region name of the DynamoDB table. |
| `aws_access_key_id` | `Optional[str]` | `None` | AWS access key id, if provided. |
| `aws_secret_access_key` | `Optional[str]` | `None` | AWS secret access key, if provided. |
| `endpoint_url` | `Optional[str]` | `None` | Endpoint URL, if provided. |
| `create_table_if_not_exists` | `bool` | `True` | If true, creates the table if it does not exist. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>JSON Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/json</url>
  <content>Phidata supports using local JSON files as a storage backend for Agents using the `JsonFileAgentStorage` class.

Usage
-----

    from phi.agent import Agent
    from phi.tools.duckduckgo import DuckDuckGo
    from phi.storage.agent.json import JsonFileAgentStorage
    
    agent = Agent(
        storage=JsonFileAgentStorage(path="tmp/agent_sessions_json"),
        tools=[DuckDuckGo()],
        add_history_to_messages=True,
    )
    
    agent.print_response("How many people live in Canada?")
    agent.print_response("What is their national anthem called?")
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dir_path` | `str` | \- | Path to the folder to be used to store the JSON files. |</content>
</page>

<page>
  <title>Writing your own Toolkit - Phidata</title>
  <url>https://docs.phidata.com/tools/custom-toolkits</url>
  <content>Many advanced use-cases will require writing custom Toolkits. Here’s the general flow:

1.  Create a class inheriting the `phi.tools.Toolkit` class.
2.  Add your functions to the class.
3.  **Important:** Register the functions using `self.register(function_name)`

Now your Toolkit is ready to use with an Agent. For example:

    from typing import List
    
    from phi.tools import Toolkit
    from phi.utils.log import logger
    
    
    class ShellTools(Toolkit):
        def __init__(self):
            super().__init__(name="shell_tools")
            self.register(self.run_shell_command)
    
        def run_shell_command(self, args: List[str], tail: int = 100) -> str:
            """Runs a shell command and returns the output or error.
    
            Args:
                args (List[str]): The command to run as a list of strings.
                tail (int): The number of lines to return from the output.
            Returns:
                str: The output of the command.
            """
            import subprocess
    
            logger.info(f"Running shell command: {args}")
            try:
                logger.info(f"Running shell command: {args}")
                result = subprocess.run(args, capture_output=True, text=True)
                logger.debug(f"Result: {result}")
                logger.debug(f"Return code: {result.returncode}")
                if result.returncode != 0:
                    return f"Error: {result.stderr}"
                # return only the last n lines of the output
                return "\n".join(result.stdout.split("\n")[-tail:])
            except Exception as e:
                logger.warning(f"Failed to run shell command: {e}")
                return f"Error: {e}"</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/tools/introduction</url>
  <content>Tools are **functions** that an Agent can run like searching the web, running SQL, sending an email or calling APIs. Use tools integrate Agents with external systems. You can use any python function as a tool or use a pre-built **toolkit**. The general syntax is:

    from phi.agent import Agent
    
    agent = Agent(
        # Add functions or Toolkits
        tools=[...],
        # Show tool calls in the Agent response
        show_tool_calls=True
    )
    

Read more about:

*   [Available Toolkits](https://docs.phidata.com/tools/toolkits)
*   [Using functions as tools](https://docs.phidata.com/tools/functions)</content>
</page>

<page>
  <title>Airflow - Phidata</title>
  <url>https://docs.phidata.com/tools/airflow</url>
  <content>    from phi.agent import Agent
    from phi.tools.airflow import AirflowToolkit
    
    agent = Agent(
        tools=[AirflowToolkit(dags_dir="dags", save_dag=True, read_dag=True)], show_tool_calls=True, markdown=True
    )
    
    
    dag_content = """
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime, timedelta
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024, 1, 1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }
    # Using 'schedule' instead of deprecated 'schedule_interval'
    with DAG(
        'example_dag',
        default_args=default_args,
        description='A simple example DAG',
        schedule='@daily',  # Changed from schedule_interval
        catchup=False
    ) as dag:
        def print_hello():
            print("Hello from Airflow!")
            return "Hello task completed"
        task = PythonOperator(
            task_id='hello_task',
            python_callable=print_hello,
            dag=dag,
        )
    """
    
    agent.run(f"Save this DAG file as 'example_dag.py': {dag_content}")
    
    
    agent.print_response("Read the contents of 'example_dag.py'")</content>
</page>

<page>
  <title>Apify - Phidata</title>
  <url>https://docs.phidata.com/tools/apify</url>
  <content>**ApifyTools** enable an Agent to access the Apify API and run actors.

Prerequisites
-------------

The following example requires the `apify-client` library and an API token which can be obtained from [Apify](https://apify.com/).

Example
-------

The following agent will use Apify to crawl the webpage: [https://docs.phidata.com/introduction](https://docs.phidata.com/introduction) and summarize it.

cookbook/tools/apify\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | \- | API key for authentication purposes. |
| `website_content_crawler` | `bool` | `True` | Enables the functionality to crawl a website using website-content-crawler actor. |
| `web_scraper` | `bool` | `False` | Enables the functionality to crawl a website using web\_scraper actor. |

| Function | Description |
| --- | --- |
| `website_content_crawler` | Crawls a website using Apify’s website-content-crawler actor. |
| `web_scrapper` | Scrapes a website using Apify’s web-scraper actor. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/apify.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Arxiv - Phidata</title>
  <url>https://docs.phidata.com/tools/arxiv</url>
  <content>**ArxivTools** enable an Agent to search for publications on Arxiv.

Prerequisites
-------------

The following example requires the `arxiv` and `pypdf` libraries.

Example
-------

The following agent will run seach arXiv for “language models” and print the response.

cookbook/tools/arxiv\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `search_arxiv` | `bool` | `True` | Enables the functionality to search the arXiv database. |
| `read_arxiv_papers` | `bool` | `True` | Allows reading of arXiv papers directly. |
| `download_dir` | `Path` | \- | Specifies the directory path where downloaded files will be saved. |

| Function | Description |
| --- | --- |
| `search_arxiv_and_update_knowledge_base` | This function searches arXiv for a topic, adds the results to the knowledge base and returns them. |
| `search_arxiv` | Searches arXiv for a query. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/arxiv_toolkit.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>BaiduSearch - Phidata</title>
  <url>https://docs.phidata.com/tools/baidusearch</url>
  <content>**BaiduSearch** enables an Agent to search the web for information using the Baidu search engine.

Prerequisites
-------------

The following example requires the `baidusearch` library. To install BaiduSearch, run the following command:

Example
-------

cookbook/tools/baidusearch\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `fixed_max_results` | `int` | \- | Sets a fixed number of maximum results to return. No default is provided, must be specified if used. |
| `fixed_language` | `str` | \- | Set the fixed language for the results. |
| `headers` | `Any` | \- | Headers to be used in the search request. |
| `proxy` | `str` | \- | Specifies a single proxy address as a string to be used for the HTTP requests. |
| `timeout` | `int` | `10` | Sets the timeout for HTTP requests, in seconds. |

| Function | Description |
| --- | --- |
| `baidu_search` | Use this function to search Baidu for a query. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/baidusearch.py)</content>
</page>

<page>
  <title>AWS Lambda - Phidata</title>
  <url>https://docs.phidata.com/tools/aws_lambda</url>
  <content>Prerequisites
-------------

The following example requires the `boto3` library.

Example
-------

The following agent will use AWS Lambda to list all Lambda functions in our AWS account and invoke a specific Lambda function.

cookbook/tools/aws\_lambda\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `region_name` | `str` | `"us-east-1"` | AWS region name where Lambda functions are located. |

| Function | Description |
| --- | --- |
| `list_functions` | Lists all Lambda functions available in the AWS account. |
| `invoke_function` | Invokes a specific Lambda function with an optional payload. Takes `function_name` and optional `payload` parameters. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/aws_lambda.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Calculator - Phidata</title>
  <url>https://docs.phidata.com/tools/calculator</url>
  <content>**Calculator** enables an Agent to perform mathematical calculations.

Example
-------

The following agent will calculate the result of `10*5` and then raise it to the power of `2`:

cookbook/tools/calculator\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `add` | `bool` | `True` | Enables the functionality to perform addition. |
| `subtract` | `bool` | `True` | Enables the functionality to perform subtraction. |
| `multiply` | `bool` | `True` | Enables the functionality to perform multiplication. |
| `divide` | `bool` | `True` | Enables the functionality to perform division. |
| `exponentiate` | `bool` | `False` | Enables the functionality to perform exponentiation. |
| `factorial` | `bool` | `False` | Enables the functionality to calculate the factorial of a number. |
| `is_prime` | `bool` | `False` | Enables the functionality to check if a number is prime. |
| `square_root` | `bool` | `False` | Enables the functionality to calculate the square root of a number. |

| Function | Description |
| --- | --- |
| `add` | Adds two numbers and returns the result. |
| `subtract` | Subtracts the second number from the first and returns the result. |
| `multiply` | Multiplies two numbers and returns the result. |
| `divide` | Divides the first number by the second and returns the result. Handles division by zero. |
| `exponentiate` | Raises the first number to the power of the second number and returns the result. |
| `factorial` | Calculates the factorial of a number and returns the result. Handles negative numbers. |
| `is_prime` | Checks if a number is prime and returns the result. |
| `square_root` | Calculates the square root of a number and returns the result. Handles negative numbers. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/calculator.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Cal.com - Phidata</title>
  <url>https://docs.phidata.com/tools/calcom</url>
  <content>Prerequisites
-------------

The following example requires the `pytz` and `requests` libraries.

Example
-------

The following agent will use Cal.com to list all events in your Cal.com account for tomorrow.

cookbook/tools/calcom\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | Cal.com API key |
| `event_type_id` | `int` | `None` | Event type ID for scheduling |
| `user_timezone` | `str` | `None` | User’s timezone (e.g. “America/New\_York”) |
| `get_available_slots` | `bool` | `True` | Enable getting available time slots |
| `create_booking` | `bool` | `True` | Enable creating new bookings |
| `get_upcoming_bookings` | `bool` | `True` | Enable getting upcoming bookings |
| `reschedule_booking` | `bool` | `True` | Enable rescheduling bookings |
| `cancel_booking` | `bool` | `True` | Enable canceling bookings |

| Function | Description |
| --- | --- |
| `get_available_slots` | Gets available time slots for a given date range |
| `create_booking` | Creates a new booking with provided details |
| `get_upcoming_bookings` | Gets list of upcoming bookings |
| `get_booking_details` | Gets details for a specific booking |
| `reschedule_booking` | Reschedules an existing booking |
| `cancel_booking` | Cancels an existing booking |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/calcom.py)</content>
</page>

<page>
  <title>Composio - Phidata</title>
  <url>https://docs.phidata.com/tools/composio</url>
  <content>[**ComposioTools**](https://docs.composio.dev/framework/phidata) enable an Agent to work with tools like Gmail, Salesforce, Github, etc.

Prerequisites
-------------

The following example requires the `composio-phidata` library.

Example
-------

The following agent will use Github Tool from Composio Toolkit to star a repo.

cookbook/tools/composio\_tools.py

The following parameters are used when calling the GitHub star repository action:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `owner` | `str` | \- | The owner of the repository to star. |
| `repo` | `str` | \- | The name of the repository to star. |

Composio Toolkit provides 1000+ functions to connect to different software tools. Open this [link](https://composio.dev/tools) to view the complete list of functions.

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)</content>
</page>

<page>
  <title>Crawl4AI - Phidata</title>
  <url>https://docs.phidata.com/tools/crawl4ai</url>
  <content>**Crawl4aiTools** enable an Agent to perform web crawling and scraping tasks using the Crawl4ai library.

Prerequisites
-------------

The following example requires the `crawl4ai` library.

Example
-------

The following agent will scrape the content from the [https://github.com/phidatahq/phidata](https://github.com/phidatahq/phidata) webpage:

cookbook/tools/crawl4ai\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `max_length` | `int` | `1000` | Specifies the maximum length of the text from the webpage to be returned. |

| Function | Description |
| --- | --- |
| `web_crawler` | Crawls a website using crawl4ai’s WebCrawler. Parameters include ‘url’ for the URL to crawl and an optional ‘max\_length’ to limit the length of extracted content. The default value for ‘max\_length’ is 1000. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/crawl4ai_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>CSV - Phidata</title>
  <url>https://docs.phidata.com/tools/csv</url>
  <content>**CsvTools** enable an Agent to read and write CSV files.

Example
-------

The following agent will download the IMDB csv file and allow the user to query it using a CLI app.

cookbook/tools/csv\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `csvs` | `List[Union[str, Path]]` | \- | A list of CSV files or paths to be processed or read. |
| `row_limit` | `int` | \- | The maximum number of rows to process from each CSV file. |
| `read_csvs` | `bool` | `True` | Enables the functionality to read data from specified CSV files. |
| `list_csvs` | `bool` | `True` | Enables the functionality to list all available CSV files. |
| `query_csvs` | `bool` | `True` | Enables the functionality to execute queries on data within CSV files. |
| `read_column_names` | `bool` | `True` | Enables the functionality to read the column names from the CSV files. |
| `duckdb_connection` | `Any` | \- | Specifies a connection instance for DuckDB database operations. |
| `duckdb_kwargs` | `Dict[str, Any]` | \- | A dictionary of keyword arguments for configuring DuckDB operations. |

| Function | Description |
| --- | --- |
| `list_csv_files` | Lists all available CSV files. |
| `read_csv_file` | This function reads the contents of a csv file |
| `get_columns` | This function returns the columns of a csv file |
| `query_csv_file` | This function queries the contents of a csv file |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/csv_tools.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Dalle - Phidata</title>
  <url>https://docs.phidata.com/tools/dalle</url>
  <content>Prerequisites
-------------

You need to install the `openai` library.

Set the `OPENAI_API_KEY` environment variable.

Example
-------

The following agent will use DALL-E to generate an image based on a text prompt.

cookbook/tools/dalle\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `str` | `"dall-e-3"` | The DALL-E model to use |
| `n` | `int` | `1` | Number of images to generate |
| `size` | `str` | `"1024x1024"` | Image size (256x256, 512x512, 1024x1024, 1792x1024, or 1024x1792) |
| `quality` | `str` | `"standard"` | Image quality (standard or hd) |
| `style` | `str` | `"vivid"` | Image style (vivid or natural) |
| `api_key` | `str` | `None` | The OpenAI API key for authentication |

| Function | Description |
| --- | --- |
| `generate_image` | Generates an image based on a text prompt |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/dalle.py)</content>
</page>

<page>
  <title>DuckDuckGo - Phidata</title>
  <url>https://docs.phidata.com/tools/duckduckgo</url>
  <content>**DuckDuckGo** enables an Agent to search the web for information.

Prerequisites
-------------

The following example requires the `duckduckgo-search` library. To install DuckDuckGo, run the following command:

Example
-------

cookbook/tools/duckduckgo.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `search` | `bool` | `True` | Enables the use of the `duckduckgo_search` function to search DuckDuckGo for a query. |
| `news` | `bool` | `True` | Enables the use of the `duckduckgo_news` function to fetch the latest news via DuckDuckGo. |
| `fixed_max_results` | `int` | \- | Sets a fixed number of maximum results to return. No default is provided, must be specified if used. |
| `headers` | `Any` | \- | Accepts any type of header values to be sent with HTTP requests. |
| `proxy` | `str` | \- | Specifies a single proxy address as a string to be used for the HTTP requests. |
| `proxies` | `Any` | \- | Accepts a dictionary of proxies to be used for HTTP requests. |
| `timeout` | `int` | `10` | Sets the timeout for HTTP requests, in seconds. |

| Function | Description |
| --- | --- |
| `duckduckgo_search` | Use this function to search DuckDuckGo for a query. |
| `duckduckgo_news` | Use this function to get the latest news from DuckDuckGo. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/duckduckgo.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Email - Phidata</title>
  <url>https://docs.phidata.com/tools/email</url>
  <content>**EmailTools** enable an Agent to send an email to a user. The Agent can send an email to a user with a specific subject and body.

Example
-------

cookbook/tools/email\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `receiver_email` | `str` | \- | The email address of the receiver. |
| `sender_name` | `str` | \- | The name of the sender. |
| `sender_email` | `str` | \- | The email address of the sender. |
| `sender_passkey` | `str` | \- | The passkey for the sender’s email. |

| Function | Description |
| --- | --- |
| `email_user` | Emails the user with the given subject and body. Currently works with Gmail. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/email.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Exa - Phidata</title>
  <url>https://docs.phidata.com/tools/exa</url>
  <content>**ExaTools** enable an Agent to search the web using Exa.

Prerequisites
-------------

The following examples requires the `exa-client` library and an API key which can be obtained from [Exa](https://exa.ai/).

Example
-------

The following agent will run seach exa for AAPL news and print the response.

cookbook/tools/exa\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | \- | API key for authentication purposes. |
| `search` | `bool` | `False` | Determines whether to enable search functionality. |
| `search_with_contents` | `bool` | `True` | Indicates whether to include contents in the search results. |
| `show_results` | `bool` | `False` | Controls whether to display search results directly. |

| Function | Description |
| --- | --- |
| `search_exa` | Searches Exa for a query. |
| `search_exa_with_contents` | Searches Exa for a query and returns the contents from the search results. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/exa.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Fal - Phidata</title>
  <url>https://docs.phidata.com/tools/fal</url>
  <content>**FalTools** enable an Agent to perform media generation tasks.

Prerequisites
-------------

The following example requires the `fal_client` library and an API key which can be obtained from [Fal](https://fal.ai/).

Example
-------

The following agent will use FAL to generate any video requested by the user.

cookbook/tools/fal\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | API key for authentication purposes. |
| `model` | `str` | `None` | The model to use for the media generation. |

| Function | Description |
| --- | --- |
| `generate_media` | Generate either images or videos depending on the user prompt. |
| `image_to_image` | Transform an input image based on a text prompt. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/fal_tools.py)</content>
</page>

<page>
  <title>DuckDb - Phidata</title>
  <url>https://docs.phidata.com/tools/duckdb</url>
  <content>**DuckDbTools** enable an Agent to run SQL and analyze data using DuckDb.

Prerequisites
-------------

The following example requires DuckDB library. To install DuckDB, run the following command:

For more installation options, please refer to [DuckDB documentation](https://duckdb.org/docs/installation).

Example
-------

The following agent will analyze the movies file using SQL and return the result.

cookbook/tools/duckdb\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `db_path` | `str` | \- | Specifies the path to the database file. |
| `connection` | `DuckDBPyConnection` | \- | Provides an existing DuckDB connection object. |
| `init_commands` | `List` | \- | A list of initial SQL commands to run on database connection. |
| `read_only` | `bool` | `False` | Configures the database connection to be read-only. |
| `config` | `dict` | \- | Configuration options for the database connection. |
| `run_queries` | `bool` | `True` | Determines whether to run SQL queries during the operation. |
| `inspect_queries` | `bool` | `False` | Enables inspection of SQL queries without executing them. |
| `create_tables` | `bool` | `True` | Allows creation of tables in the database during the operation. |
| `summarize_tables` | `bool` | `True` | Enables summarization of table data during the operation. |
| `export_tables` | `bool` | `False` | Allows exporting tables to external formats during the operation. |

| Function | Description |
| --- | --- |
| `show_tables` | Function to show tables in the database |
| `describe_table` | Function to describe a table |
| `inspect_query` | Function to inspect a query and return the query plan. Always inspect your query before running them. |
| `run_query` | Function that runs a query and returns the result. |
| `summarize_table` | Function to compute a number of aggregates over a table. The function launches a query that computes a number of aggregates over all columns, including min, max, avg, std and approx\_unique. |
| `get_table_name_from_path` | Get the table name from a path |
| `create_table_from_path` | Creates a table from a path |
| `export_table_to_path` | Save a table in a desired format (default: parquet). If the path is provided, the table will be saved under that path. Eg: If path is /tmp, the table will be saved as /tmp/table.parquet. Otherwise it will be saved in the current directory |
| `load_local_path_to_table` | Load a local file into duckdb |
| `load_local_csv_to_table` | Load a local CSV file into duckdb |
| `load_s3_path_to_table` | Load a file from S3 into duckdb |
| `load_s3_csv_to_table` | Load a CSV file from S3 into duckdb |
| `create_fts_index` | Create a full text search index on a table |
| `full_text_search` | Full text Search in a table column for a specific text/keyword |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/duckdb.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>File - Phidata</title>
  <url>https://docs.phidata.com/tools/file</url>
  <content>**FileTools** enable an Agent to read and write files on the local file system.

Example
-------

The following agent will generate an answer and save it in a file.

cookbook/tools/file\_tools.py

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `base_dir` | `Path` | \- | Specifies the base directory path for file operations. |
| `save_files` | `bool` | `True` | Determines whether files should be saved during the operation. |
| `read_files` | `bool` | `True` | Allows reading from files during the operation. |
| `list_files` | `bool` | `True` | Enables listing of files in the specified directory. |

| Name | Description |
| --- | --- |
| `save_file` | Saves the contents to a file called `file_name` and returns the file name if successful. |
| `read_file` | Reads the contents of the file `file_name` and returns the contents if successful. |
| `list_files` | Returns a list of files in the base directory |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/file.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Firecrawl - Phidata</title>
  <url>https://docs.phidata.com/tools/firecrawl</url>
  <content>**FirecrawlTools** enable an Agent to perform web crawling and scraping tasks.

Prerequisites
-------------

The following example requires the `firecrawl-py` library and an API key which can be obtained from [Firecrawl](https://firecrawl.dev/).

Example
-------

The following agent will scrape the content from [https://finance.yahoo.com/](https://finance.yahoo.com/) and return a summary of the content:

cookbook/tools/firecrawl\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | Optional API key for authentication purposes. |
| `formats` | `List[str]` | `None` | Optional list of formats to be used for the operation. |
| `limit` | `int` | `10` | Maximum number of items to retrieve. The default value is 10. |
| `scrape` | `bool` | `True` | Enables the scraping functionality. Default is True. |
| `crawl` | `bool` | `False` | Enables the crawling functionality. Default is False. |

| Function | Description |
| --- | --- |
| `scrape_website` | Scrapes a website using Firecrawl. Parameters include `url` to specify the URL to scrape. The function supports optional formats if specified. Returns the results of the scraping in JSON format. |
| `crawl_website` | Crawls a website using Firecrawl. Parameters include `url` to specify the URL to crawl, and an optional `limit` to define the maximum number of pages to crawl. The function supports optional formats and returns the crawling results in JSON format. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/firecrawl.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Github - Phidata</title>
  <url>https://docs.phidata.com/tools/github</url>
  <content>**GithubTools** enables an Agent to access Github repositories and perform tasks such as listing open pull requests, issues and more.

Prerequisites
-------------

The following examples requires the `PyGithub` library and a Github access token which can be obtained from [here](https://github.com/settings/tokens).

Example
-------

The following agent will search Google for the latest news about “Mistral AI”:

cookbook/tools/github\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `access_token` | `str` | `None` | Github access token for authentication. If not provided, will use GITHUB\_ACCESS\_TOKEN environment variable. |
| `base_url` | `str` | `None` | Optional base URL for Github Enterprise installations. |
| `search_repositories` | `bool` | `True` | Enable searching Github repositories. |
| `list_repositories` | `bool` | `True` | Enable listing repositories for a user/organization. |
| `get_repository` | `bool` | `True` | Enable getting repository details. |
| `list_pull_requests` | `bool` | `True` | Enable listing pull requests for a repository. |
| `get_pull_request` | `bool` | `True` | Enable getting pull request details. |
| `get_pull_request_changes` | `bool` | `True` | Enable getting pull request file changes. |
| `create_issue` | `bool` | `True` | Enable creating issues in repositories. |

| Function | Description |
| --- | --- |
| `search_repositories` | Searches Github repositories based on a query. |
| `list_repositories` | Lists repositories for a given user or organization. |
| `get_repository` | Gets details about a specific repository. |
| `list_pull_requests` | Lists pull requests for a repository. |
| `get_pull_request` | Gets details about a specific pull request. |
| `get_pull_request_changes` | Gets the file changes in a pull request. |
| `create_issue` | Creates a new issue in a repository. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/github.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Giphy - Phidata</title>
  <url>https://docs.phidata.com/tools/giphy</url>
  <content>**GiphyTools** enables an Agent to search for GIFs on GIPHY.

Prerequisites
-------------

Example
-------

The following agent will search GIPHY for a GIF appropriate for a birthday message.

    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.giphy import GiphyTools
    
    
    gif_agent = Agent(
        name="Gif Generator Agent",
        model=OpenAIChat(id="gpt-4o"),
        tools=[GiphyTools()],
        description="You are an AI agent that can generate gifs using Giphy.",
    )
    
    gif_agent.print_response("I want a gif to send to a friend for their birthday.")
    

Toolkit Params
--------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | If you want to manually supply the GIPHY API key. |
| `limit` | `int` | `1` | The number of GIFs to return in a search. |

Toolkit Functions
-----------------

| Function | Description |
| --- | --- |
| `search_gifs` | Searches GIPHY for a GIF based on the query string. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/giphy.py)</content>
</page>

<page>
  <title>Google Calendar - Phidata</title>
  <url>https://docs.phidata.com/tools/googlecalendar</url>
  <content>Enable an Agent to work with Google Calendar to view and schedule meetings.

Prerequisites
-------------

### Install dependencies

### Setup Google Project and OAuth

Reference: [https://developers.google.com/calendar/api/quickstart/python](https://developers.google.com/calendar/api/quickstart/python)

1.  Enable Google Calender API
    
    *   Go to [Google Cloud Console](https://console.cloud.google.com/apis/enableflow?apiid=calendar-json.googleapis.com).
    *   Select Project and Enable.
2.  Go To API & Service -> OAuth Consent Screen
    
3.  Select User Type
    
    *   If you are a Google Workspace user, select Internal.
    *   Otherwise, select External.
4.  Fill in the app details (App name, logo, support email, etc).
    
5.  Select Scope
    
    *   Click on Add or Remove Scope.
    *   Search for Google Calender API (Make sure you’ve enabled Google calender API otherwise scopes wont be visible).
    *   Select scopes accordingly
        *   From the dropdown check on `/auth/calendar` scope
    *   Save and continue.
6.  Adding Test User
    
    *   Click Add Users and enter the email addresses of the users you want to allow during testing.
    *   NOTE : Only these users can access the app’s OAuth functionality when the app is in “Testing” mode. Any other users will receive access denied errors.
    *   To make the app available to all users, you’ll need to move the app’s status to “In Production”. Before doing so, ensure the app is fully verified by Google if it uses sensitive or restricted scopes.
    *   Click on Go back to Dashboard.
7.  Generate OAuth 2.0 Client ID
    
    *   Go to Credentials.
    *   Click on Create Credentials -> OAuth Client ID
    *   Select Application Type as Desktop app.
    *   Download JSON.
8.  Using Google Calender Tool
    
    *   Pass the path of downloaded credentials as credentials\_path to Google Calender tool.
    *   Optional: Set the `token_path` parameter to specify where the tool should create the `token.json` file.
    *   The `token.json` file is used to store the user’s access and refresh tokens and is automatically created during the authorization flow if it doesn’t already exist.
    *   If `token_path` is not explicitly provided, the file will be created in the default location which is your current working directory.
    *   If you choose to specify `token_path`, please ensure that the directory you provide has write access, as the application needs to create or update this file during the authentication process.

Example
-------

The following agent will use GoogleCalendarTools to find today’s events.

cookbook/tools/googlecalendar\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `credentials_path` | `str` | `None` | Path of the file credentials.json file which contains OAuth 2.0 Client ID. |
| `token_path` | `str` | `None` | Path of the file token.json which stores the user’s access and refresh tokens. |

| Function | Description |
| --- | --- |
| `list_events` | List events from the user’s primary calendar. |
| `create_event` | Create a new event in the user’s primary calendar. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/googlecalendar.py)

*   [Prerequisites](#prerequisites)
*   [Install dependencies](#install-dependencies)
*   [Setup Google Project and OAuth](#setup-google-project-and-oauth)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Google Search - Phidata</title>
  <url>https://docs.phidata.com/tools/googlesearch</url>
  <content>**GoogleSearch** enables an Agent to perform web crawling and scraping tasks.

Prerequisites
-------------

The following examples requires the `googlesearch` and `pycountry` libraries.

Example
-------

The following agent will search Google for the latest news about “Mistral AI”:

cookbook/tools/googlesearch\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `fixed_max_results` | `int` | `None` | Optional fixed maximum number of results to return. |
| `fixed_language` | `str` | `None` | Optional fixed language for the requests. |
| `headers` | `Any` | `None` | Optional headers to include in the requests. |
| `proxy` | `str` | `None` | Optional proxy to be used for the requests. |
| `timeout` | `int` | `None` | Optional timeout for the requests, in seconds. |

| Function | Description |
| --- | --- |
| `google_search` | Searches Google for a specified query. Parameters include `query` for the search term, `max_results` for the maximum number of results (default is 5), and `language` for the language of the search results (default is “en”). Returns the search results as a JSON formatted string. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/googlesearch.py)</content>
</page>

<page>
  <title>Hacker News - Phidata</title>
  <url>https://docs.phidata.com/tools/hackernews</url>
  <content>**HackerNews** enables an Agent to search Hacker News website.

Example
-------

The following agent will write an engaging summary of the users with the top 2 stories on hackernews along with the stories.

cookbook/tools/hackernews.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `get_top_stories` | `bool` | `True` | Enables fetching top stories. |
| `get_user_details` | `bool` | `True` | Enables fetching user details. |

| Function | Description |
| --- | --- |
| `get_top_hackernews_stories` | Retrieves the top stories from Hacker News. Parameters include `num_stories` to specify the number of stories to return (default is 10). Returns the top stories in JSON format. |
| `get_user_details` | Retrieves the details of a Hacker News user by their username. Parameters include `username` to specify the user. Returns the user details in JSON format. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/hackernews.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Jina Reader - Phidata</title>
  <url>https://docs.phidata.com/tools/jina_reader</url>
  <content>**JinaReaderTools** enable an Agent to perform web search tasks using Jina.

Prerequisites
-------------

The following example requires the `jina` library.

Example
-------

The following agent will use Jina API to summarize the content of [https://github.com/phidatahq](https://github.com/phidatahq)

cookbook/tools/jinareader\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | \- | The API key for authentication purposes, retrieved from the configuration. |
| `base_url` | `str` | \- | The base URL of the API, retrieved from the configuration. |
| `search_url` | `str` | \- | The URL used for search queries, retrieved from the configuration. |
| `max_content_length` | `int` | \- | The maximum length of content allowed, retrieved from the configuration. |

| Function | Description |
| --- | --- |
| `read_url` | Reads the content of a specified URL using Jina Reader API. Parameters include `url` for the URL to read. Returns the truncated content or an error message if the request fails. |
| `search_query` | Performs a web search using Jina Reader API based on a specified query. Parameters include `query` for the search term. Returns the truncated search results or an error message if the request fails. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/jina_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Jira - Phidata</title>
  <url>https://docs.phidata.com/tools/jira</url>
  <content>**JiraTools** enable an Agent to perform Jira tasks.

Prerequisites
-------------

The following example requires the `jira` library and auth credentials.

Example
-------

The following agent will use Jira API to search for issues in a project.

cookbook/tools/jira\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `server_url` | `str` | `""` | The URL of the JIRA server, retrieved from the environment variable `JIRA_SERVER_URL`. Default is an empty string if not set. |
| `username` | `str` | `None` | The JIRA username for authentication, retrieved from the environment variable `JIRA_USERNAME`. Default is None if not set. |
| `password` | `str` | `None` | The JIRA password for authentication, retrieved from the environment variable `JIRA_PASSWORD`. Default is None if not set. |
| `token` | `str` | `None` | The JIRA API token for authentication, retrieved from the environment variable `JIRA_TOKEN`. Default is None if not set. |

| Function | Description |
| --- | --- |
| `get_issue` | Retrieves issue details from JIRA. Parameters include:  
\- `issue_key`: the key of the issue to retrieve  
Returns a JSON string containing issue details or an error message. |
| `create_issue` | Creates a new issue in JIRA. Parameters include:  
\- `project_key`: the project in which to create the issue  
\- `summary`: the issue summary  
\- `description`: the issue description  
\- `issuetype`: the type of issue (default is “Task”)  
Returns a JSON string with the new issue’s key and URL or an error message. |
| `search_issues` | Searches for issues using a JQL query in JIRA. Parameters include:  
\- `jql_str`: the JQL query string  
\- `max_results`: the maximum number of results to return (default is 50)  
Returns a JSON string containing a list of dictionaries with issue details or an error message. |
| `add_comment` | Adds a comment to an issue in JIRA. Parameters include:  
\- `issue_key`: the key of the issue  
\- `comment`: the comment text  
Returns a JSON string indicating success or an error message. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/jira_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Lumalabs - Phidata</title>
  <url>https://docs.phidata.com/tools/lumalabs</url>
  <content>**LumaLabTools** enables an Agent to generate media using the [Lumalabs platform](https://lumalabs.ai/dream-machine).

Prerequisites
-------------

The following example requires the `lumaai` library. To install the Lumalabs client, run the following command:

Example
-------

The following agent will use Lumalabs to generate any video requested by the user.

cookbook/tools/lumalabs\_tool.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | If you want to manually supply the Lumalabs API key. |

| Function | Description |
| --- | --- |
| `generate_video` | Generate a video from a prompt. |
| `image_to_video` | Generate a video from a prompt, a starting image and an ending image. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/lumalab.py)</content>
</page>

<page>
  <title>Linear - Phidata</title>
  <url>https://docs.phidata.com/tools/linear</url>
  <content>**LinearTool** enable an Agent to perform [Linear](https://linear.app/) tasks.

Prerequisites
-------------

Example
-------

The following agent will use Linear API to search for issues in a project for a specific user.

cookbook/tools/linear\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `get_user_details` | `bool` | `True` | Enable `get_user_details` tool. |
| `get_issue_details` | `bool` | `True` | Enable `get_issue_details` tool. |
| `create_issue` | `bool` | `True` | Enable `create_issue` tool. |
| `update_issue` | `bool` | `True` | Enable `update_issue` tool. |
| `get_user_assigned_issues` | `bool` | `True` | Enable `get_user_assigned_issues` tool. |
| `get_workflow_issues` | `bool` | `True` | Enable `get_workflow_issues` tool. |
| `get_high_priority_issues` | `bool` | `True` | Enable `get_high_priority_issues` tool. |

| Function | Description |
| --- | --- |
| `get_user_details` | Fetch authenticated user details. |
| `get_issue_details` | Retrieve details of a specific issue by issue ID. |
| `create_issue` | Create a new issue within a specific project and team. |
| `update_issue` | Update the title or state of a specific issue by issue ID. |
| `get_user_assigned_issues` | Retrieve issues assigned to a specific user by user ID. |
| `get_workflow_issues` | Retrieve issues within a specific workflow state by workflow ID. |
| `get_high_priority_issues` | Retrieve issues with a high priority (priority `<=` 2). |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/linear_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>MLX Transcribe - Phidata</title>
  <url>https://docs.phidata.com/tools/mlx_transcribe</url>
  <content>**MLX Transcribe** is a tool for transcribing audio files using MLX Whisper.

Prerequisites
-------------

1.  **Install ffmpeg**
    
    *   macOS: `brew install ffmpeg`
    *   Ubuntu: `sudo apt-get install ffmpeg`
    *   Windows: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2.  **Install mlx-whisper library**
    
3.  **Prepare audio files**
    
    *   Create a ‘storage/audio’ directory
    *   Place your audio files in this directory
    *   Supported formats: mp3, mp4, wav, etc.
4.  **Download sample audio** (optional)
    
    *   Visit: [https://www.ted.com/talks/reid\_hoffman\_and\_kevin\_scott\_the\_evolution\_of\_ai\_and\_how\_it\_will\_impact\_human\_creativity](https://www.ted.com/talks/reid_hoffman_and_kevin_scott_the_evolution_of_ai_and_how_it_will_impact_human_creativity)
    *   Save the audio file to ‘storage/audio’ directory

Example
-------

The following agent will use MLX Transcribe to transcribe audio files.

cookbook/tools/mlx\_transcribe\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `base_dir` | `Path` | `Path.cwd()` | Base directory for audio files |
| `read_files_in_base_dir` | `bool` | `True` | Whether to register the read\_files function |
| `path_or_hf_repo` | `str` | `"mlx-community/whisper-large-v3-turbo"` | Path or HuggingFace repo for the model |
| `verbose` | `bool` | `None` | Enable verbose output |
| `temperature` | `float` or `Tuple[float, ...]` | `None` | Temperature for sampling |
| `compression_ratio_threshold` | `float` | `None` | Compression ratio threshold |
| `logprob_threshold` | `float` | `None` | Log probability threshold |
| `no_speech_threshold` | `float` | `None` | No speech threshold |
| `condition_on_previous_text` | `bool` | `None` | Whether to condition on previous text |
| `initial_prompt` | `str` | `None` | Initial prompt for transcription |
| `word_timestamps` | `bool` | `None` | Enable word-level timestamps |
| `prepend_punctuations` | `str` | `None` | Punctuations to prepend |
| `append_punctuations` | `str` | `None` | Punctuations to append |
| `clip_timestamps` | `str` or `List[float]` | `None` | Clip timestamps |
| `hallucination_silence_threshold` | `float` | `None` | Hallucination silence threshold |
| `decode_options` | `dict` | `None` | Additional decoding options |

| Function | Description |
| --- | --- |
| `transcribe` | Transcribes an audio file using MLX Whisper |
| `read_files` | Lists all audio files in the base directory |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/mlx_transcribe.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>ModelsLabs - Phidata</title>
  <url>https://docs.phidata.com/tools/models_labs</url>
  <content>Prerequisites
-------------

You need to install the `requests` library.

Set the `MODELS_LAB_API_KEY` environment variable.

Example
-------

The following agent will use ModelsLabs to generate a video based on a text prompt.

cookbook/tools/models\_labs\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | The ModelsLab API key for authentication |
| `url` | `str` | `"https://modelslab.com/api/v6/video/text2video"` | The API endpoint URL |
| `fetch_url` | `str` | `https://modelslab.com/api/v6/video/fetch` | The URL to fetch the video status from |
| `wait_for_completion` | `bool` | `False` | Whether to wait for the video to be ready |
| `add_to_eta` | `int` | `15` | Time to add to the ETA to account for the time it takes to fetch the video |
| `max_wait_time` | `int` | `60` | Maximum time to wait for the video to be ready |
| `file_type` | `str` | `"mp4"` | The type of file to generate |

| Function | Description |
| --- | --- |
| `generate_media` | Generates a video or gif based on a text prompt |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/models_labs.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Newspaper - Phidata</title>
  <url>https://docs.phidata.com/tools/newspaper</url>
  <content>**NewspaperTools** enable an Agent to read news articles using the Newspaper4k library.

Prerequisites
-------------

The following example requires the `newspaper3k` library.

Example
-------

The following agent will summarize the wikipedia article on language models.

cookbook/tools/newspaper\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `get_article_text` | `bool` | `True` | Enables the functionality to retrieve the text of an article. |

| Function | Description |
| --- | --- |
| `get_article_text` | Retrieves the text of an article from a specified URL. Parameters include `url` for the URL of the article. Returns the text of the article or an error message if the retrieval fails. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/newspaper_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>OpenBB - Phidata</title>
  <url>https://docs.phidata.com/tools/openbb</url>
  <content>**OpenBBTools** enable an Agent to provide information about stocks and companies.

cookbook/tools/openbb\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `read_article` | `bool` | `True` | Enables the functionality to read the full content of an article. |
| `include_summary` | `bool` | `False` | Specifies whether to include a summary of the article along with the full content. |
| `article_length` | `int` | \- | The maximum length of the article or its summary to be processed or returned. |

| Function | Description |
| --- | --- |
| `get_stock_price` | This function gets the current stock price for a stock symbol or list of symbols. |
| `search_company_symbol` | This function searches for the stock symbol of a company. |
| `get_price_targets` | This function gets the price targets for a stock symbol or list of symbols. |
| `get_company_news` | This function gets the latest news for a stock symbol or list of symbols. |
| `get_company_profile` | This function gets the company profile for a stock symbol or list of symbols. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/openbb_tools.py)

*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Newspaper4k - Phidata</title>
  <url>https://docs.phidata.com/tools/newspaper4k</url>
  <content>**Newspaper4k** enables an Agent to read news articles using the Newspaper4k library.

Prerequisites
-------------

The following example requires the `newspaper4k` and `lxml_html_clean` libraries.

Example
-------

The following agent will summarize the article: [https://www.rockymountaineer.com/blog/experience-icefields-parkway-scenic-drive-lifetime](https://www.rockymountaineer.com/blog/experience-icefields-parkway-scenic-drive-lifetime).

cookbook/tools/newspaper4k\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `read_article` | `bool` | `True` | Enables the functionality to read the full content of an article. |
| `include_summary` | `bool` | `False` | Specifies whether to include a summary of the article along with the full content. |
| `article_length` | `int` | \- | The maximum length of the article or its summary to be processed or returned. |

| Function | Description |
| --- | --- |
| `get_article_data` | This function reads the full content and data of an article. |
| `read_article` | This function reads the full content of an article. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/newspaper4k.py)</content>
</page>

<page>
  <title>Pandas - Phidata</title>
  <url>https://docs.phidata.com/tools/pandas</url>
  <content>**PandasTools** enable an Agent to perform data manipulation tasks using the Pandas library.

cookbook/tools/pandas\_tool.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dataframes` | `Dict[str, pd.DataFrame]` | `{}` | A dictionary to store Pandas DataFrames, keyed by their names. |
| `create_pandas_dataframe` | `function` | \- | Registers a function to create a Pandas DataFrame. |
| `run_dataframe_operation` | `function` | \- | Registers a function to run operations on a Pandas DataFrame. |

| Function | Description |
| --- | --- |
| `create_pandas_dataframe` | Creates a Pandas DataFrame named `dataframe_name` by using the specified function `create_using_function` with parameters `function_parameters`. Parameters include ‘dataframe\_name’ for the name of the DataFrame, ‘create\_using\_function’ for the function to create it (e.g., ‘read\_csv’), and ‘function\_parameters’ for the arguments required by the function. Returns the name of the created DataFrame if successful, otherwise returns an error message. |
| `run_dataframe_operation` | Runs a specified operation `operation` on a DataFrame `dataframe_name` with the parameters `operation_parameters`. Parameters include ‘dataframe\_name’ for the DataFrame to operate on, ‘operation’ for the operation to perform (e.g., ‘head’, ‘tail’), and ‘operation\_parameters’ for the arguments required by the operation. Returns the result of the operation if successful, otherwise returns an error message. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/pandas.py)

*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Phi - Phidata</title>
  <url>https://docs.phidata.com/tools/phi</url>
  <content>Example
-------

The following agent will use the Phi toolkit to create and manage phidata workspaces. It can create new applications from templates like llm-app, api-app, django-app, and streamlit-app. It can also start existing workspaces and validate that Phi is ready to run commands.

cookbook/tools/phi\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `str` | `"phi_tools"` | The name of the tool |

| Function | Description |
| --- | --- |
| `validate_phi_is_ready` | Validates that Phi is ready to run commands |
| `create_new_app` | Creates a new phidata workspace for a given application template |
| `start_user_workspace` | Starts the workspace for a user |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/phi.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Postgres - Phidata</title>
  <url>https://docs.phidata.com/tools/postgres</url>
  <content>**PostgresTools** enable an Agent to interact with a PostgreSQL database.

Prerequisites
-------------

The following example requires the `psycopg2` library.

You will also need a database. The following example uses a Postgres database running in a Docker container.

Example
-------

The following agent will list all tables in the database.

cookbook/tools/postgres.py

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `connection` | `psycopg2.extensions.connection` | `None` | Optional database connection object. |
| `db_name` | `str` | `None` | Optional name of the database to connect to. |
| `user` | `str` | `None` | Optional username for database authentication. |
| `password` | `str` | `None` | Optional password for database authentication. |
| `host` | `str` | `None` | Optional host for the database connection. |
| `port` | `int` | `None` | Optional port for the database connection. |
| `run_queries` | `bool` | `True` | Enables running SQL queries. |
| `inspect_queries` | `bool` | `False` | Enables inspecting SQL queries before execution. |
| `summarize_tables` | `bool` | `True` | Enables summarizing table structures. |
| `export_tables` | `bool` | `False` | Enables exporting tables from the database. |

| Function | Description |
| --- | --- |
| `show_tables` | Retrieves and displays a list of tables in the database. Returns the list of tables. |
| `describe_table` | Describes the structure of a specified table by returning its columns, data types, and maximum character length. Parameters include ‘table’ to specify the table name. Returns the table description. |
| `summarize_table` | Summarizes a table by computing aggregates such as min, max, average, standard deviation, and non-null counts for numeric columns. Parameters include ‘table’ to specify the table name, and an optional ‘table\_schema’ to specify the schema (default is “public”). Returns the summary of the table. |
| `inspect_query` | Inspects an SQL query by returning the query plan. Parameters include ‘query’ to specify the SQL query. Returns the query plan. |
| `export_table_to_path` | Exports a specified table in CSV format to a given path. Parameters include ‘table’ to specify the table name and an optional ‘path’ to specify where to save the file (default is the current directory). Returns the result of the export operation. |
| `run_query` | Executes an SQL query and returns the result. Parameters include ‘query’ to specify the SQL query. Returns the result of the query execution. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/postgres.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Pubmed - Phidata</title>
  <url>https://docs.phidata.com/tools/pubmed</url>
  <content>**PubmedTools** enable an Agent to search for Pubmed for articles.

Example
-------

The following agent will search Pubmed for articles related to “ulcerative colitis”.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `email` | `str` | `"your_email@example.com"` | Specifies the email address to use. |
| `max_results` | `int` | `None` | Optional parameter to specify the maximum number of results to return. |

| Function | Description |
| --- | --- |
| `search_pubmed` | Searches PubMed for articles based on a specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results to return (default is 10). Returns a JSON string containing the search results, including publication date, title, and summary. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/pubmed.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Python - Phidata</title>
  <url>https://docs.phidata.com/tools/python</url>
  <content>**PythonTools** enable an Agent to write and run python code.

Example
-------

The following agent will write a python script that creates the fibonacci series, save it to a file, run it and return the result.

cookbook/tools/python\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `base_dir` | `Path` | `None` | Specifies the base directory for operations. Default is None, indicating the current working directory. |
| `save_and_run` | `bool` | `True` | If True, saves and runs the code. Useful for execution of scripts after saving. |
| `pip_install` | `bool` | `False` | Enables pip installation of required packages before running the code. |
| `run_code` | `bool` | `False` | Determines whether the code should be executed. |
| `list_files` | `bool` | `False` | If True, lists all files in the specified base directory. |
| `run_files` | `bool` | `False` | If True, runs the Python files found in the specified directory. |
| `read_files` | `bool` | `False` | If True, reads the contents of the files in the specified directory. |
| `safe_globals` | `dict` | \- | Specifies a dictionary of global variables that are considered safe to use during the execution. |
| `safe_locals` | `dict` | \- | Specifies a dictionary of local variables that are considered safe to use during the execution. |

| Function | Description |
| --- | --- |
| `save_to_file_and_run` | This function saves Python code to a file called `file_name` and then runs it. If successful, returns the value of `variable_to_return` if provided otherwise returns a success message. If failed, returns an error message. Make sure the file\_name ends with `.py` |
| `run_python_file_return_variable` | This function runs code in a Python file. If successful, returns the value of `variable_to_return` if provided otherwise returns a success message. If failed, returns an error message. |
| `read_file` | Reads the contents of the file `file_name` and returns the contents if successful. |
| `list_files` | Returns a list of files in the base directory |
| `run_python_code` | This function runs Python code in the current environment. If successful, returns the value of `variable_to_return` if provided otherwise returns a success message. If failed, returns an error message. |
| `pip_install_package` | This function installs a package using pip in the current environment. If successful, returns a success message. If failed, returns an error message. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/python.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Resend - Phidata</title>
  <url>https://docs.phidata.com/tools/resend</url>
  <content>**ResendTools** enable an Agent to send emails using Resend

Prerequisites
-------------

The following example requires the `resend` library and an API key from [Resend](https://resend.com/).

    export RESEND_API_KEY=***
    

Example
-------

The following agent will send an email using Resend

cookbook/tools/resend\_tools.py

    from phi.agent import Agent
    from phi.tools.resend_tools import ResendTools
    
    from_email = "<enter_from_email>"
    to_email = "<enter_to_email>"
    
    agent = Agent(tools=[ResendTools(from_email=from_email)], show_tool_calls=True)
    agent.print_response(f"Send an email to {to_email} greeting them with hello world")
    

Toolkit Params
--------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | \- | API key for authentication purposes. |
| `from_email` | `str` | \- | The email address used as the sender in email communications. |

Toolkit Functions
-----------------

| Function | Description |
| --- | --- |
| `send_email` | Send an email using the Resend API. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/resend_tools.py)</content>
</page>

<page>
  <title>Replicate - Phidata</title>
  <url>https://docs.phidata.com/tools/replicate</url>
  <content>**ReplicateTools** enables an Agent to generate media using the [Replicate platform](https://replicate.com/).

Prerequisites
-------------

The following example requires the `replicate` library. To install the Replicate client, run the following command:

Example
-------

The following agent will use Replicate to generate images or videos requested by the user.

cookbook/tools/replicate\_tool.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | `None` | If you want to manually supply the Replicate API key. |
| `model` | `str` | `minimax/video-01` | The replicate model to use. Find out more on the Replicate platform. |

| Function | Description |
| --- | --- |
| `generate_media` | Generate either an image or a video from a prompt. The output depends on the model. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/replicate.py)</content>
</page>

<page>
  <title>Searxng - Phidata</title>
  <url>https://docs.phidata.com/tools/searxng</url>
  <content>Example
-------

**Searxng** enables an Agent to search the web for a query, scrape a website, or crawl a website.

cookbook/tools/searxng\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `host` | `str` | \- | The host for the connection. |
| `engines` | `List[str]` | `[]` | A list of search engines to use. |
| `fixed_max_results` | `int` | `None` | Optional parameter to specify the fixed maximum number of results. |
| `images` | `bool` | `False` | Enables searching for images. |
| `it` | `bool` | `False` | Enables searching for IT-related content. |
| `map` | `bool` | `False` | Enables searching for maps. |
| `music` | `bool` | `False` | Enables searching for music. |
| `news` | `bool` | `False` | Enables searching for news. |
| `science` | `bool` | `False` | Enables searching for science-related content. |
| `videos` | `bool` | `False` | Enables searching for videos. |

| Function | Description |
| --- | --- |
| `search` | Performs a general web search using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the search results. |
| `image_search` | Performs an image search using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the image search results. |
| `it_search` | Performs a search for IT-related information using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the IT-related search results. |
| `map_search` | Performs a search for maps using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the map search results. |
| `music_search` | Performs a search for music-related information using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the music search results. |
| `news_search` | Performs a search for news using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the news search results. |
| `science_search` | Performs a search for science-related information using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the science search results. |
| `video_search` | Performs a search for videos using the specified query. Parameters include `query` for the search term and `max_results` for the maximum number of results (default is 5). Returns the video search results. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/searxng.py)

*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Serpapi - Phidata</title>
  <url>https://docs.phidata.com/tools/serpapi</url>
  <content>**SerpApiTools** enable an Agent to search Google and YouTube for a query.

Prerequisites
-------------

The following example requires the `google-search-results` library and an API key from [SerpApi](https://serpapi.com/).

Example
-------

The following agent will search Google for the query: “Whats happening in the USA” and share results.

cookbook/tools/serpapi\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | \- | API key for authentication purposes. |
| `search_youtube` | `bool` | `False` | Enables the functionality to search for content on YouTube. |

| Function | Description |
| --- | --- |
| `search_google` | This function searches Google for a query. |
| `search_youtube` | Searches YouTube for a query. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/serpapi_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Shell - Phidata</title>
  <url>https://docs.phidata.com/tools/shell</url>
  <content>**ShellTools** enable an Agent to interact with the shell to run commands.

Example
-------

The following agent will run a shell command and show contents of the current directory.

Mention your OS to the agent to make sure it runs the correct command.

cookbook/tools/shell\_tools.py

    from phi.agent import Agent
    from phi.tools.shell import ShellTools
    
    agent = Agent(tools=[ShellTools()], show_tool_calls=True)
    agent.print_response("Show me the contents of the current directory", markdown=True)
    

Functions in Toolkit
--------------------

| Function | Description |
| --- | --- |
| `run_shell_command` | Runs a shell command and returns the output or error. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/shell.py)</content>
</page>

<page>
  <title>Sleep - Phidata</title>
  <url>https://docs.phidata.com/tools/sleep</url>
  <content>Example
-------

The following agent will use the `sleep` tool to pause execution for a given number of seconds.

cookbook/tools/sleep\_tools.py

    from phi.agent import Agent
    from phi.tools.sleep import Sleep
    
    # Create an Agent with the Sleep tool
    agent = Agent(tools=[Sleep()], name="Sleep Agent")
    
    # Example 1: Sleep for 2 seconds
    agent.print_response("Sleep for 2 seconds")
    
    # Example 2: Sleep for a longer duration
    agent.print_response("Sleep for 5 seconds")
    

Toolkit Params
--------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `str` | `"sleep"` | The name of the tool |

Toolkit Functions
-----------------

| Function | Description |
| --- | --- |
| `sleep` | Pauses execution for a specified number of seconds |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/sleep.py)</content>
</page>

<page>
  <title>Slack - Phidata</title>
  <url>https://docs.phidata.com/tools/slack</url>
  <content>Prerequisites
-------------

The following example requires the `slack-sdk` library.

Get a Slack token from [here](https://api.slack.com/tutorials/tracks/getting-a-token).

Example
-------

The following agent will use Slack to send a message to a channel, list all channels, and get the message history of a specific channel.

cookbook/tools/slack\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `token` | `str` | \- | Slack API token for authentication |
| `send_message` | `bool` | `True` | Enables the functionality to send messages to Slack channels |
| `list_channels` | `bool` | `True` | Enables the functionality to list available Slack channels |
| `get_channel_history` | `bool` | `True` | Enables the functionality to retrieve message history from channels |

| Function | Description |
| --- | --- |
| `send_message` | Sends a message to a specified Slack channel |
| `list_channels` | Lists all available channels in the Slack workspace |
| `get_channel_history` | Retrieves message history from a specified channel |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/slack.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Spider - Phidata</title>
  <url>https://docs.phidata.com/tools/spider</url>
  <content>**SpiderTools** is an open source web Scraper & Crawler that returns LLM-ready data. To start using Spider, you need an API key from the [Spider dashboard](https://spider.cloud/).

Prerequisites
-------------

The following example requires the `spider-client` library.

Example
-------

The following agent will run a search query to get the latest news in USA and scrape the first search result. The agent will return the scraped data in markdown format.

cookbook/tools/spider\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `max_results` | `int` | \- | The maximum number of search results to return |
| `url` | `str` | \- | The url to be scraped or crawled |

| Function | Description |
| --- | --- |
| `search` | Searches the web for the given query. |
| `scrape` | Scrapes the given url. |
| `crawl` | Crawls the given url. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/spider.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Tavily - Phidata</title>
  <url>https://docs.phidata.com/tools/tavily</url>
  <content>**TavilyTools** enable an Agent to search the web using the Tavily API.

Prerequisites
-------------

The following examples requires the `tavily-python` library and an API key from [Tavily](https://tavily.com/).

Example
-------

The following agent will run a search on Tavily for “language models” and print the response.

cookbook/tools/tavily\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | \- | API key for authentication. If not provided, will check TAVILY\_API\_KEY environment variable. |
| `search` | `bool` | `True` | Enables search functionality. |
| `max_tokens` | `int` | `6000` | Maximum number of tokens to use in search results. |
| `include_answer` | `bool` | `True` | Whether to include an AI-generated answer summary in the response. |
| `search_depth` | `Literal['basic', 'advanced']` | `'advanced'` | Depth of search - ‘basic’ for faster results or ‘advanced’ for more comprehensive search. |
| `format` | `Literal['json', 'markdown']` | `'markdown'` | Output format - ‘json’ for raw data or ‘markdown’ for formatted text. |
| `use_search_context` | `bool` | `False` | Whether to use Tavily’s search context API instead of regular search. |

| Function | Description |
| --- | --- |
| `web_search_using_tavily` | Searches the web for a query using Tavily API. Takes a query string and optional max\_results parameter (default 5). Returns results in specified format with titles, URLs, content and relevance scores. |
| `web_search_with_tavily` | Alternative search function that uses Tavily’s search context API. Takes a query string and returns contextualized search results. Only available if use\_search\_context is True. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/tavily.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>SQL - Phidata</title>
  <url>https://docs.phidata.com/tools/sql</url>
  <content>**SQLTools** enable an Agent to run SQL queries and interact with databases.

Prerequisites
-------------

The following example requires the `sqlalchemy` library and a database URL.

You will also need a database. The following example uses a Postgres database running in a Docker container.

Example
-------

The following agent will run a SQL query to list all tables in the database and describe the contents of one of the tables.

cookbook/tools/sql\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `db_url` | `str` | \- | The URL for connecting to the database. |
| `db_engine` | `Engine` | \- | The database engine used for connections and operations. |
| `user` | `str` | \- | The username for database authentication. |
| `password` | `str` | \- | The password for database authentication. |
| `host` | `str` | \- | The hostname or IP address of the database server. |
| `port` | `int` | \- | The port number on which the database server is listening. |
| `schema` | `str` | \- | The specific schema within the database to use. |
| `dialect` | `str` | \- | The SQL dialect used by the database. |
| `tables` | `Dict[str, Any]` | \- | A dictionary mapping table names to their respective metadata or structure. |
| `list_tables` | `bool` | `True` | Enables the functionality to list all tables in the database. |
| `describe_table` | `bool` | `True` | Enables the functionality to describe the schema of a specific table. |
| `run_sql_query` | `bool` | `True` | Enables the functionality to execute SQL queries directly. |

| Function | Description |
| --- | --- |
| `list_tables` | Lists all tables in the database. |
| `describe_table` | Describes the schema of a specific table. |
| `run_sql_query` | Executes SQL queries directly. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/sql.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Twitter - Phidata</title>
  <url>https://docs.phidata.com/tools/twitter</url>
  <content>Prerequisites
-------------

The following example requires the `tweepy` library.

Get a Twitter API key and secret from [here](https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret).

Example
-------

The following agent will use Twitter to get information about a user, send a message to a user, and create a new tweet.

cookbook/tools/twitter\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_token` | `str` | `None` | The bearer token for Twitter API authentication |
| `consumer_key` | `str` | `None` | The consumer key for Twitter API authentication |
| `consumer_secret` | `str` | `None` | The consumer secret for Twitter API authentication |
| `access_token` | `str` | `None` | The access token for Twitter API authentication |
| `access_token_secret` | `str` | `None` | The access token secret for Twitter API authentication |

| Function | Description |
| --- | --- |
| `create_tweet` | Creates and posts a new tweet |
| `reply_to_tweet` | Replies to an existing tweet |
| `send_dm` | Sends a direct message to a Twitter user |
| `get_user_info` | Retrieves information about a Twitter user |
| `get_home_timeline` | Gets the authenticated user’s home timeline |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/twitter.py)</content>
</page>

<page>
  <title>Website - Phidata</title>
  <url>https://docs.phidata.com/tools/website</url>
  <content>**WebsiteTools** enable an Agent to parse a website and add its contents to the knowledge base.

Prerequisites
-------------

The following example requires the `beautifulsoup4` library.

Example
-------

The following agent will read the contents of a website and add it to the knowledge base.

cookbook/tools/website\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `knowledge_base` | `WebsiteKnowledgeBase` | \- | The knowledge base associated with the website, containing various data and resources linked to the website’s content. |

| Function | Description |
| --- | --- |
| `add_website_to_knowledge_base` | This function adds a website’s content to the knowledge base. **NOTE:** The website must start with `https://` and should be a valid website. Use this function to get information about products from the internet. |
| `read_url` | This function reads a URL and returns the contents. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/website.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Wikipedia - Phidata</title>
  <url>https://docs.phidata.com/tools/wikipedia</url>
  <content>**WikipediaTools** enable an Agent to search wikipedia a website and add its contents to the knowledge base.

Prerequisites
-------------

The following example requires the `wikipedia` library.

Example
-------

The following agent will run seach wikipedia for “ai” and print the response.

cookbook/tools/wikipedia\_tools.py

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `knowledge_base` | `WikipediaKnowledgeBase` | \- | The knowledge base associated with Wikipedia, containing various data and resources linked to Wikipedia’s content. |

| Function Name | Description |
| --- | --- |
| `search_wikipedia_and_update_knowledge_base` | This function searches wikipedia for a topic, adds the results to the knowledge base and returns them. |
| `search_wikipedia` | Searches Wikipedia for a query. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/wikipedia.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Yfinance - Phidata</title>
  <url>https://docs.phidata.com/tools/yfinance</url>
  <content>**YFinanceTools** enable an Agent to access stock data, financial information and more from Yahoo Finance.

Prerequisites
-------------

The following example requires the `yfinance` library.

Example
-------

The following agent will provide information about the stock price and analyst recommendations for NVDA (Nvidia Corporation).

cookbook/tools/yfinance\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `stock_price` | bool | `True` | Enables the functionality to retrieve current stock price information. |
| `company_info` | bool | `False` | Enables the functionality to retrieve detailed company information. |
| `stock_fundamentals` | bool | `False` | Enables the functionality to retrieve fundamental data about a stock. |
| `income_statements` | bool | `False` | Enables the functionality to retrieve income statements of a company. |
| `key_financial_ratios` | bool | `False` | Enables the functionality to retrieve key financial ratios for a company. |
| `analyst_recommendations` | bool | `False` | Enables the functionality to retrieve analyst recommendations for a stock. |
| `company_news` | bool | `False` | Enables the functionality to retrieve the latest news related to a company. |
| `technical_indicators` | bool | `False` | Enables the functionality to retrieve technical indicators for stock analysis. |
| `historical_prices` | bool | `False` | Enables the functionality to retrieve historical price data for a stock. |

| Function | Description |
| --- | --- |
| `get_current_stock_price` | This function retrieves the current stock price of a company. |
| `get_company_info` | This function retrieves detailed information about a company. |
| `get_historical_stock_prices` | This function retrieves historical stock prices for a company. |
| `get_stock_fundamentals` | This function retrieves fundamental data about a stock. |
| `get_income_statements` | This function retrieves income statements of a company. |
| `get_key_financial_ratios` | This function retrieves key financial ratios for a company. |
| `get_analyst_recommendations` | This function retrieves analyst recommendations for a stock. |
| `get_company_news` | This function retrieves the latest news related to a company. |
| `get_technical_indicators` | This function retrieves technical indicators for stock analysis. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/yfinance.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Youtube - Phidata</title>
  <url>https://docs.phidata.com/tools/youtube</url>
  <content>**YouTubeTools** enable an Agent to access captions and metadata of YouTube videos, when provided with a video URL.

Prerequisites
-------------

The following example requires the `youtube_transcript_api` library.

Example
-------

The following agent will provide a summary of a YouTube video.

cookbook/tools/youtube\_tools.py

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| `get_video_captions` | `bool` | `True` | Enables the functionality to retrieve video captions. |
| `get_video_data` | `bool` | `True` | Enables the functionality to retrieve video metadata and other related data. |
| `languages` | `List[str]` | \- | Specifies the list of languages for which data should be retrieved, if applicable. |

| Function | Description |
| --- | --- |
| `get_youtube_video_captions` | This function retrieves the captions of a YouTube video. |
| `get_youtube_video_data` | This function retrieves the metadata of a YouTube video. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/youtube_tools.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Zendesk - Phidata</title>
  <url>https://docs.phidata.com/tools/zendesk</url>
  <content>**ZendeskTools** enable an Agent to access Zendesk API to search for articles.

Prerequisites
-------------

The following example requires the `requests` library and auth credentials.

Example
-------

The following agent will run seach Zendesk for “How do I login?” and print the response.

cookbook/tools/zendesk\_tools.py

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `username` | `str` | \- | The username used for authentication or identification purposes. |
| `password` | `str` | \- | The password associated with the username for authentication purposes. |
| `company_name` | `str` | \- | The name of the company related to the user or the data being accessed. |

| Function | Description |
| --- | --- |
| `search_zendesk` | This function searches for articles in Zendesk Help Center that match the given search string. |

Information
-----------

*   View on [Github](https://github.com/phidatahq/phidata/blob/main/phi/tools/zendesk.py)

*   [Prerequisites](#prerequisites)
*   [Example](#example)
*   [Toolkit Params](#toolkit-params)
*   [Toolkit Functions](#toolkit-functions)
*   [Information](#information)</content>
</page>

<page>
  <title>Zoom - Phidata</title>
  <url>https://docs.phidata.com/tools/zoom</url>
  <content>    import os
    import time
    import requests
    from typing import Optional
    
    from phi.utils.log import logger
    from phi.agent import Agent
    from phi.model.openai import OpenAIChat
    from phi.tools.zoom import ZoomTool
    
    # Get environment variables
    ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
    CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
    CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")
    
    
    class CustomZoomTool(ZoomTool):
        def __init__(
            self,
            account_id: Optional[str] = None,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            name: str = "zoom_tool",
        ):
            super().__init__(account_id=account_id, client_id=client_id, client_secret=client_secret, name=name)
            self.token_url = "https://zoom.us/oauth/token"
            self.access_token = None
            self.token_expires_at = 0
    
        def get_access_token(self) -> str:
            """
            Obtain or refresh the access token for Zoom API.
            Returns:
                A string containing the access token or an empty string if token retrieval fails.
            """
            if self.access_token and time.time() < self.token_expires_at:
                return str(self.access_token)
    
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {"grant_type": "account_credentials", "account_id": self.account_id}
    
            try:
                response = requests.post(
                    self.token_url, headers=headers, data=data, auth=(self.client_id, self.client_secret)
                )
                response.raise_for_status()
    
                token_info = response.json()
                self.access_token = token_info["access_token"]
                expires_in = token_info["expires_in"]
                self.token_expires_at = time.time() + expires_in - 60
    
                self._set_parent_token(str(self.access_token))
                return str(self.access_token)
            except requests.RequestException as e:
                logger.error(f"Error fetching access token: {e}")
                return ""
    
        def _set_parent_token(self, token: str) -> None:
            """Helper method to set the token in the parent ZoomTool class"""
            if token:
                self._ZoomTool__access_token = token
    
    
    zoom_tools = CustomZoomTool(account_id=ACCOUNT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    
    
    agent = Agent(
        name="Zoom Meeting Manager",
        agent_id="zoom-meeting-manager",
        model=OpenAIChat(model="gpt-4"),
        tools=[zoom_tools],
        markdown=True,
        debug_mode=True,
        show_tool_calls=True,
        instructions=[
            "You are an expert at managing Zoom meetings using the Zoom API.",
            "You can:",
            "1. Schedule new meetings (schedule_meeting)",
            "2. Get meeting details (get_meeting)",
            "3. List all meetings (list_meetings)",
            "4. Get upcoming meetings (get_upcoming_meetings)",
            "5. Delete meetings (delete_meeting)",
            "6. Get meeting recordings (get_meeting_recordings)",
            "",
            "For recordings, you can:",
            "- Retrieve recordings for any past meeting using the meeting ID",
            "- Include download tokens if needed",
            "- Get recording details like duration, size, download link and file types",
            "",
            "Guidelines:",
            "- Use ISO 8601 format for dates (e.g., '2024-12-28T10:00:00Z')",
            "- Ensure meeting times are in the future",
            "- Provide meeting details after scheduling (ID, URL, time)",
            "- Handle errors gracefully",
            "- Confirm successful operations",
        ],
    )
    
    
    agent.print_response("Schedule a meeting titled 'Team Sync' 8th december at 2 PM UTC for 45 minutes")
    agent.print_response("delete a meeting titled 'Team Sync' which scheduled tomorrow at 2 PM UTC for 45 minutes")
    agent.print_response("List all my scheduled meetings")</content>
</page>

<page>
  <title>OpenAI Like - Phidata</title>
  <url>https://docs.phidata.com/models/openai-like</url>
  <content>Many providers like Together, Groq, Sambanova, etc support the OpenAI API format. Use the `OpenAILike` model to access them by replacing the `base_url`.

[​](#example)

Example
------------------------

[​](#params)

Params
----------------------

`OpenAILike` also support all the params of [OpenAIChat](https://docs.phidata.com/models/openai)</content>
</page>

<page>
  <title>OpenAI - Phidata</title>
  <url>https://docs.phidata.com/models/openai</url>
  <content>The GPT models are the best in class LLMs and used as the default LLM by **Agents**.

Authentication
--------------

Set your `OPENAI_API_KEY` environment variable. You can get one [from OpenAI here](https://platform.openai.com/account/api-keys).

Example
-------

Use `OpenAIChat` with your `Agent`:

Params
------

For more information, please refer to the [OpenAI docs](https://platform.openai.com/docs/api-reference/chat/create) as well.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o"` | The id of the OpenAI model to use. |
| `name` | `str` | `"OpenAIChat"` | The name of this chat model instance. |
| `provider` | `str` | `"OpenAI " + id` | The provider of the model. |
| `store` | `Optional[bool]` | `None` | Whether or not to store the output of this chat completion request for use in the model distillation or evals products. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | `None` | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | `None` | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | `None` | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | `None` | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | `None` | How many log probability results to return per token. |
| `user` | `Optional[str]` | `None` | A unique identifier representing your end-user. |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling. |
| `extra_headers` | `Optional[Any]` | `None` | Additional headers to send with the request. |
| `extra_query` | `Optional[Any]` | `None` | Additional query parameters to send with the request. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with OpenAI. |
| `organization` | `Optional[str]` | `None` | The organization to use for API requests. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for API requests. |
| `timeout` | `Optional[float]` | `None` | The timeout for API requests. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[OpenAIClient]` | `None` | The OpenAI client instance. |
| `async_client` | `Optional[AsyncOpenAIClient]` | `None` | The asynchronous OpenAI client instance. |
| `structured_outputs` | `bool` | `False` | Whether to use the structured outputs from the Model. |
| `supports_structured_outputs` | `bool` | `True` | Whether the Model supports structured outputs. |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content. |</content>
</page>

<page>
  <title>AWS Bedrock Claude - Phidata</title>
  <url>https://docs.phidata.com/models/aws-bedrock</url>
  <content>Use AWS Bedrock to access the Claude models.

Authentication
--------------

Set your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_DEFAULT_REGION` environment variables. Get your keys from [here](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/models).

Example
-------

Use `AWS BedrockClaude` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"anthropic.claude-3-sonnet-20240229-v1:0"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AwsBedrockAnthropicClaude"` | The name identifier for the Claude agent. |
| `provider` | `str` | `"AwsBedrock"` | The provider of the model. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_p` | `Optional[float]` | \- | The nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `top_k` | `Optional[int]` | \- | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `stop_sequences` | `Optional[List[str]]` | \- | A list of sequences where the API will stop generating further tokens. |
| `anthropic_version` | `str` | `"bedrock-2023-05-31"` | The version of the Anthropic API to use. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for the request, provided as a dictionary. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional client parameters for initializing the `AwsBedrock` client, provided as a dictionary. |</content>
</page>

<page>
  <title>Anthropic Claude - Phidata</title>
  <url>https://docs.phidata.com/models/anthropic</url>
  <content>Claude is a family of foundational AI models by Anthropic that can be used in a variety of applications.

Authentication
--------------

Set your `ANTHROPIC_API_KEY` environment. You can get one [from Anthropic here](https://anthropic.com/).

Example
-------

Use `Claude` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"claude-3-5-sonnet-20240620"` | The id of the Anthropic Claude model to use |
| `name` | `str` | `"Claude"` | The name of the model |
| `provider` | `str` | `"Anthropic"` | The provider of the model |
| `max_tokens` | `Optional[int]` | `1024` | Maximum number of tokens to generate in the chat completion |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output |
| `stop_sequences` | `Optional[List[str]]` | `None` | A list of strings that the model should stop generating text at |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling |
| `top_k` | `Optional[int]` | `None` | Controls diversity via top-k sampling |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Anthropic |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration |
| `client` | `Optional[AnthropicClient]` | `None` | A pre-configured instance of the Anthropic client |</content>
</page>

<page>
  <title>Azure - Phidata</title>
  <url>https://docs.phidata.com/models/azure</url>
  <content>Use the best in class GPT models using Azure’s OpenAI API.

Authentication
--------------

Set your environment variables.

Example
-------

Use `AzureOpenAIChat` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | \- | The specific model ID used for generating responses. This field is required. |
| `name` | `str` | `"AzureOpenAIChat"` | The name identifier for the agent. |
| `provider` | `str` | `"Azure"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Azure OpenAI service. |
| `api_version` | `str` | `"2024-02-01"` | The version of the Azure OpenAI API to use. |
| `azure_endpoint` | `Optional[str]` | \- | The endpoint URL for the Azure OpenAI service. |
| `azure_deployment` | `Optional[str]` | \- | The deployment name or ID in Azure. |
| `base_url` | `Optional[str]` | \- | The base URL for making API requests to the Azure OpenAI service. |
| `azure_ad_token` | `Optional[str]` | \- | The Azure Active Directory token for authenticating requests. |
| `azure_ad_token_provider` | `Optional[Any]` | \- | The provider for obtaining Azure Active Directory tokens. |
| `organization` | `Optional[str]` | \- | The organization associated with the API requests. |
| `openai_client` | `Optional[AzureOpenAIClient]` | \- | An instance of AzureOpenAIClient provided for making API requests. |

Azure also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>DeepSeek - Phidata</title>
  <url>https://docs.phidata.com/models/deepseek</url>
  <content>DeepSeek is a platform for providing endpoints for Large Language models.

Authentication
--------------

Set your `DEEPSEEK_API_KEY` environment variable. Get your key from [here](https://platform.deepseek.com/api_keys).

Example
-------

Use `DeepSeek` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"deepseek-chat"` | The specific model ID used for generating responses. |
| `name` | `str` | `"DeepSeekChat"` | The name identifier for the DeepSeek model. |
| `provider` | `str` | `"DeepSeek"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key used for authenticating requests to the DeepSeek service. Retrieved from the environment variable `DEEPSEEK_API_KEY`. |
| `base_url` | `str` | `"https://api.deepseek.com"` | The base URL for making API requests to the DeepSeek service. |

DeepSeek also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>Fireworks - Phidata</title>
  <url>https://docs.phidata.com/models/fireworks</url>
  <content>Fireworks is a platform for providing endpoints for Large Language models.

Authentication
--------------

Set your `FIREWORKS_API_KEY` environment variable. Get your key from [here](https://fireworks.ai/account/api-keys).

Example
-------

Use `Fireworks` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"accounts/fireworks/models/firefunction-v2"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Fireworks: {id}"` | The name identifier for the agent. Defaults to "Fireworks: " followed by the model ID. |
| `provider` | `str` | `"Fireworks"` | The provider of the model. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the service. Retrieved from the environment variable FIREWORKS\_API\_KEY. |
| `base_url` | `str` | `"https://api.fireworks.ai/inference/v1"` | The base URL for making API requests to the Fireworks service. |

Fireworks also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>Cohere - Phidata</title>
  <url>https://docs.phidata.com/models/cohere</url>
  <content>Leverage Cohere’s powerful command models and more.

Authentication
--------------

Set your `CO_API_KEY` environment variable. Get your key from [here](https://dashboard.cohere.com/api-keys).

Example
-------

Use `CohereChat` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"command-r-08-2024"` | The specific model ID used for generating responses. |
| `name` | `str` | `"CohereChat"` | The name identifier for the agent. |
| `provider` | `str` | `"Cohere"` | The provider of the model. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `max_tokens` | `Optional[int]` | \- | The maximum number of tokens to generate in the response. |
| `top_k` | `Optional[int]` | \- | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `top_p` | `Optional[float]` | \- | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `frequency_penalty` | `Optional[float]` | \- | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `presence_penalty` | `Optional[float]` | \- | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `add_chat_history` | `bool` | `False` | Whether to add chat history to the Cohere messages instead of using the conversation\_id. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Cohere service. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `cohere_client` | `Optional[CohereClient]` | \- | A pre-configured instance of the Cohere client. |</content>
</page>

<page>
  <title>Gemini - AI Studio - Phidata</title>
  <url>https://docs.phidata.com/models/google</url>
  <content>Use Google’s AI Studio to access the Gemini and Gemma models.

Authentication
--------------

Set your `GOOGLE_API_KEY` environment variable. You can get one [from Google here](https://ai.google.dev/aistudio).

Example
-------

Use `Gemini` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gemini-1.5-flash"` | The specific Gemini model ID to use. |
| `name` | `str` | `"Gemini"` | The name of this Gemini model instance. |
| `provider` | `str` | `"Google"` | The provider of the model. |
| `function_declarations` | `Optional[List[FunctionDeclaration]]` | `None` | List of function declarations for the model. |
| `generation_config` | `Optional[Any]` | `None` | Configuration for text generation. |
| `safety_settings` | `Optional[Any]` | `None` | Safety settings for the model. |
| `generative_model_kwargs` | `Optional[Dict[str, Any]]` | `None` | Additional keyword arguments for the generative model. |
| `api_key` | `Optional[str]` | `None` | API key for authentication. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for the client. |
| `client` | `Optional[GenerativeModel]` | `None` | The underlying generative model client. |</content>
</page>

<page>
  <title>Gemini - VertexAI - Phidata</title>
  <url>https://docs.phidata.com/models/vertexai</url>
  <content>`VertexAI` is Google’s cloud platform for building, training, and deploying machine learning models.

Authentication
--------------

[Authenticate with Gcloud](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal)

Example
-------

Use `Gemini` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"claude-3-5-sonnet-20240620"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Claude"` | The name identifier for the agent. |
| `provider` | `str` | `"Anthropic"` | The provider of the model. |
| `max_tokens` | `Optional[int]` | `1024` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `stop_sequences` | `Optional[List[str]]` | \- | A list of sequences where the API will stop generating further tokens. |
| `top_p` | `Optional[float]` | \- | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `top_k` | `Optional[int]` | \- | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the service. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `client` | `Optional[AnthropicClient]` | \- | A pre-configured instance of the Anthropic client. |</content>
</page>

<page>
  <title>Groq - Phidata</title>
  <url>https://docs.phidata.com/models/groq</url>
  <content>Groq offers blazing-fast API endpoints for large language models

Authentication
--------------

Set your `GROQ_API_KEY` environment variable. Get your key from [here](https://console.groq.com/keys).

Example
-------

Use `Groq` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama3-groq-70b-8192-tool-use-preview"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Groq"` | The name identifier for the agent. |
| `provider` | `str` | `"Groq"` | The provider of the model. |
| `frequency_penalty` | `Optional[float]` | \- | A number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `logit_bias` | `Optional[Any]` | \- | A JSON object that modifies the likelihood of specified tokens appearing in the completion by mapping token IDs to bias values between -100 and 100. |
| `logprobs` | `Optional[bool]` | \- | Whether to return log probabilities of the output tokens. |
| `max_tokens` | `Optional[int]` | \- | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | \- | A number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `response_format` | `Optional[Dict[str, Any]]` | \- | Specifies the format that the model must output. Setting to `{ "type": "json_object" }` enables JSON mode, ensuring the message generated is valid JSON. |
| `seed` | `Optional[int]` | \- | A seed value for deterministic sampling, ensuring repeated requests with the same seed and parameters return the same result. |
| `stop` | `Optional[Union[str, List[str]]]` | \- | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | \- | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_logprobs` | `Optional[int]` | \- | The number of top log probabilities to return for each generated token. |
| `top_p` | `Optional[float]` | \- | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `user` | `Optional[str]` | \- | A unique identifier representing your end-user, helping to monitor and detect abuse. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the service. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | \- | The base URL for making API requests to the service. |
| `timeout` | `Optional[int]` | \- | The timeout duration for requests, specified in seconds. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retry attempts for failed requests. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `groq_client` | `Optional[GroqClient]` | \- | An instance of GroqClient provided for making API requests. |</content>
</page>

<page>
  <title>HuggingFace - Phidata</title>
  <url>https://docs.phidata.com/models/huggingface</url>
  <content>Authentication
--------------

Set your `HF_TOKEN` environment. You can get one [from HuggingFace here](https://huggingface.co/settings/tokens).

Example
-------

Use `HuggingFace` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"meta-llama/Meta-Llama-3-8B-Instruct"` | The id of the HuggingFace model to use. |
| `name` | `str` | `"HuggingFaceChat"` | The name of this chat model instance. |
| `provider` | `str` | `"HuggingFace"` | The provider of the model. |
| `store` | `Optional[bool]` | \- | Whether or not to store the output of this chat completion request. |
| `frequency_penalty` | `Optional[float]` | \- | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | \- | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | \- | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | \- | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | \- | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | \- | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | \- | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | \- | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | \- | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | \- | How many log probability results to return per token. |
| `top_p` | `Optional[float]` | \- | Controls diversity via nucleus sampling. |
| `request_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | \- | The Access Token for authenticating with HuggingFace. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | \- | The base URL for API requests. |
| `timeout` | `Optional[float]` | \- | The timeout for API requests. |
| `max_retries` | `Optional[int]` | \- | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | \- | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | \- | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | \- | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | \- | Additional parameters for client configuration. |
| `client` | `Optional[InferenceClient]` | \- | The HuggingFace Hub Inference client instance. |
| `async_client` | `Optional[AsyncInferenceClient]` | \- | The asynchronous HuggingFace Hub client instance. |</content>
</page>

<page>
  <title>Mistral - Phidata</title>
  <url>https://docs.phidata.com/models/mistral</url>
  <content>Mistral is a platform for providing endpoints for Large Language models.

Authentication
--------------

Set your `MISTRAL_API_KEY` environment variable. Get your key from [here](https://console.mistral.ai/api-keys/).

Example
-------

Use `Mistral` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistral-large-latest"` | The ID of the model. |
| `name` | `str` | `"MistralChat"` | The name of the model. |
| `provider` | `str` | `"Mistral"` | The provider of the model. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in output generation. |
| `max_tokens` | `Optional[int]` | `None` | Maximum number of tokens to generate. |
| `top_p` | `Optional[float]` | `None` | Controls diversity of output generation. |
| `random_seed` | `Optional[int]` | `None` | Seed for random number generation. |
| `safe_mode` | `bool` | `False` | Enables content filtering. |
| `safe_prompt` | `bool` | `False` | Applies content filtering to prompts. |
| `response_format` | `Optional[Union[Dict[str, Any], ChatCompletionResponse]]` | `None` | Specifies the desired response format. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional request parameters. |
| `api_key` | `Optional[str]` | `None` | Your Mistral API key. |
| `endpoint` | `Optional[str]` | `None` | Custom API endpoint URL. |
| `max_retries` | `Optional[int]` | `None` | Maximum number of API call retries. |
| `timeout` | `Optional[int]` | `None` | Timeout for API calls in seconds. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional client parameters. |
| `mistral_client` | `Optional[Mistral]` | `None` | Custom Mistral client instance. |</content>
</page>

<page>
  <title>Nvidia - Phidata</title>
  <url>https://docs.phidata.com/models/nvidia</url>
  <content>Authentication
--------------

Set your `NVIDIA_API_KEY` environment variable. Get your key [from Nvidia here](https://build.nvidia.com/explore/discover).

Example
-------

Use `Nvidia` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"nvidia/llama-3.1-nemotron-70b-instruct"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Nvidia"` | The name identifier for the Nvidia agent. |
| `provider` | `str` | \- | The provider of the model, combining "Nvidia" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the Nvidia service. Retrieved from the environment variable `NVIDIA_API_KEY`. |
| `base_url` | `str` | `"https://integrate.api.nvidia.com/v1"` | The base URL for making API requests to the Nvidia service. |

Nvidia also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>Ollama - Phidata</title>
  <url>https://docs.phidata.com/models/ollama</url>
  <content>Run Large Language Models locally with Ollama

[Ollama](https://ollama.com/) is a fantastic tool for running models locally. Install [ollama](https://ollama.com/) and run a model using

After you have the local model running, use the `Ollama` model to access them

Example
-------

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama3.2"` | The ID of the model to use. |
| `name` | `str` | `"Ollama"` | The name of the model. |
| `provider` | `str` | `"Ollama llama3.2"` | The provider of the model. |
| `format` | `Optional[str]` | `None` | The format of the response. |
| `options` | `Optional[Any]` | `None` | Additional options to pass to the model. |
| `keep_alive` | `Optional[Union[float, str]]` | `None` | The keep alive time for the model. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass to the request. |
| `host` | `Optional[str]` | `None` | The host to connect to. |
| `timeout` | `Optional[Any]` | `None` | The timeout for the connection. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass to the client. |
| `client` | `Optional[OllamaClient]` | `None` | A pre-configured instance of the Ollama client. |
| `async_client` | `Optional[AsyncOllamaClient]` | `None` | A pre-configured instance of the asynchronous Ollama client. |</content>
</page>

<page>
  <title>OpenRouter - Phidata</title>
  <url>https://docs.phidata.com/models/openrouter</url>
  <content>OpenRouter is a platform for providing endpoints for Large Language models.

Authentication
--------------

Set your `OPENROUTER_API_KEY` environment variable. Get your key from [here](https://openrouter.ai/settings/keys).

Example
-------

Use `OpenRouter` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o"` | The specific model ID used for generating responses. |
| `name` | `str` | `"OpenRouter"` | The name identifier for the OpenRouter agent. |
| `provider` | `str` | \- | The provider of the model, combining "OpenRouter" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the OpenRouter service. Retrieved from the environment variable `OPENROUTER_API_KEY`. |
| `base_url` | `str` | `"https://openrouter.ai/api/v1"` | The base URL for making API requests to the OpenRouter service. |
| `max_tokens` | `int` | `1024` | The maximum number of tokens to generate in the response. |

OpenRouter also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>Sambanova - Phidata</title>
  <url>https://docs.phidata.com/models/sambanova</url>
  <content>Sambanova is a platform for providing endpoints for Large Language models. Note that Sambanova currently does not support function calling.

Authentication
--------------

Set your `SAMBANOVA_API_KEY` environment variable. Get your key from [here](https://cloud.sambanova.ai/apis).

Example
-------

Use `Sambanova` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"Meta-Llama-3.1-8B-Instruct"` | The id of the Sambanova model to use |
| `name` | `str` | `"Sambanova"` | The name of this chat model instance |
| `provider` | `str` | `"Sambanova"` | The provider of the model |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Sambanova (defaults to environment variable SAMBANOVA\_API\_KEY) |
| `base_url` | `str` | `"https://api.sambanova.ai/v1"` | The base URL for API requests |

Sambanova also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>Together - Phidata</title>
  <url>https://docs.phidata.com/models/together</url>
  <content>Together is a platform for providing endpoints for Large Language models.

Authentication
--------------

Set your `TOGETHER_API_KEY` environment variable. Get your key [from Together here](https://api.together.xyz/settings/api-keys).

Example
-------

Use `Together` with your `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistralai/Mixtral-8x7B-Instruct-v0.1"` | The id of the Together model to use. |
| `name` | `str` | `"Together"` | The name of this chat model instance. |
| `provider` | `str` | `"Together " + id` | The provider of the model. |
| `api_key` | `Optional[str]` | `None` | The API key to authorize requests to Together. Defaults to environment variable TOGETHER\_API\_KEY. |
| `base_url` | `str` | `"https://api.together.xyz/v1"` | The base URL for API requests. |
| `monkey_patch` | `bool` | `False` | Whether to apply monkey patching. |

Together also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>xAI - Phidata</title>
  <url>https://docs.phidata.com/models/xai</url>
  <content>xAI is a platform for providing endpoints for Large Language models.

Authentication
--------------

Set your `XAI_API_KEY` environment variable. You can get one [from xAI here](https://console.x.ai/).

Example
-------

Use `xAI` with your `Agent`:

Params
------

For more information, please refer to the [xAI docs](https://docs.x.ai/docs) as well.

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"grok-beta"` | The specific model ID used for generating responses. |
| `name` | `str` | `"xAI"` | The name identifier for the xAI agent. |
| `provider` | `str` | `"xAI"` | The provider of the model, combining "xAI" with the model ID. |
| `api_key` | `Optional[str]` | \- | The API key for authenticating requests to the xAI service. Retrieved from the environment variable `XAI_API_KEY`. |
| `base_url` | `str` | `"https://api.xai.xyz/v1"` | The base URL for making API requests to the xAI service. |

xAI also supports the params of [OpenAI](https://docs.phidata.com/models/openai).</content>
</page>

<page>
  <title>Investment Team - Phidata</title>
  <url>https://docs.phidata.com/examples/teams/investment</url>
  <content>Agent Teams

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/teams/investment.mdx)

[Journalist Team](https://docs.phidata.com/examples/teams/journalist)[Hackernews Team](https://docs.phidata.com/examples/teams/hackernews)</content>
</page>

<page>
  <title>Journalist Team - Phidata</title>
  <url>https://docs.phidata.com/examples/teams/journalist</url>
  <content>Agent Teams

This guide is in the works

Message us on [discord](https://discord.gg/4MtYHHrgA8) if you need help.

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/examples/teams/journalist.mdx)

[Research Team](https://docs.phidata.com/examples/teams/research)[Investment Team](https://docs.phidata.com/examples/teams/investment)</content>
</page>

<page>
  <title>PostgreSQL Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/reference/storage/postgres</url>
  <content>Example
-------

    from phi.storage.agent.postgres import PgAgentStorage
    
    # Create a storage backend using the Postgres database
    storage = PgAgentStorage(
        # store sessions in the ai.sessions table
        table_name="agent_sessions",
        # db_url: Postgres database URL
        db_url=db_url,
    )
    
    # Add storage to the Agent
    agent = Agent(storage=storage)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `schema` | `Optional[str]` | `"ai"` | Schema name, default is "ai". |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_engine` | `Optional[Engine]` | `None` | Database engine to be used. |
| `schema_version` | `int` | `1` | Version of the schema, default is 1. |
| `auto_upgrade_schema` | `bool` | `False` | If true, automatically upgrades the schema when necessary. |</content>
</page>

<page>
  <title>Mongo Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/storage/mongodb</url>
  <content>Phidata supports using Mongo as a storage backend for Agents using the `MongoAgentStorage` class.

Usage
-----

You need to provide either `db_url` or `client`. The following example uses `db_url`.

    from phi.storage.agent.mongodb import MongoAgentStorage
    
    db_url = "mongodb://ai:ai@localhost:27017/phi"
    
    # Create a storage backend using the Mongo database
    storage = MongoAgentStorage(
        # store sessions in the agent_sessions collection
        collection_name="agent_sessions",
        db_url=db_url,
    )
    
    # Add storage to the Agent
    agent = Agent(storage=storage)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `collection_name` | `str` | \- | Name of the collection to be used. |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_name` | `str` | `"phi"` | Database Name. |
| `client` | `Optional[MongoClient]` | `None` | MongoDB client, if provided. |</content>
</page>

<page>
  <title>SingleStore Agent Knowledge - Phidata</title>
  <url>https://docs.phidata.com/vectordb/singlestore</url>
  <content>Setup
-----

Follow the instructions in the [SingleStore Setup Guide](https://docs.singlestore.com/cloud/connect-to-singlestore/connect-with-mysql/connect-with-mysql-client/connect-to-singlestore-helios-using-tls-ssl/) to install SingleStore locally.

Example
-------

SingleStore Params
------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | The name of the collection to use. |
| `schema` | `Optional[str]` | `"ai"` | The database schema to use. |
| `db_url` | `Optional[str]` | `None` | The database connection URL. |
| `db_engine` | `Optional[Engine]` | `None` | SQLAlchemy engine instance. |
| `embedder` | `Embedder` | `OpenAIEmbedder()` | The embedder to use for creating vector embeddings. |
| `distance` | `Distance` | `Distance.cosine` | The distance metric to use for similarity search. |

*   [Setup](#setup)
*   [Example](#example)
*   [SingleStore Params](#singlestore-params)</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/knowledge/introduction</url>
  <content>A **knowledge base** is a database of information that an agent can search to improve its responses. This information is stored in a vector database and provides agents with business context, helping them respond in a context-aware manner. The general syntax is:

Vector Databases
----------------

While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly. Here’s how vector databases are used with Agents:

Loading the Knowledge Base
--------------------------

Before you can use a knowledge base, it needs to be loaded with embeddings that will be used for retrieval. Use one of the following knowledge bases to simplify the chunking, loading, searching and optimization process:

*   [ArXiv knowledge base](https://docs.phidata.com/knowledge/arxiv): Load ArXiv papers to a knowledge base
*   [Combined knowledge base](https://docs.phidata.com/knowledge/combined): Combine multiple knowledge bases into 1
*   [CSV knowledge base](https://docs.phidata.com/knowledge/csv): Load CSV files to a knowledge base
*   [Document knowledge base](https://docs.phidata.com/knowledge/document): Load local docx files to a knowledge base
*   [JSON knowledge base](https://docs.phidata.com/knowledge/json): Load JSON files to a knowledge base
*   [LangChain knowledge base](https://docs.phidata.com/knowledge/langchain): Use a Langchain retriever as a knowledge base
*   [PDF knowledge base](https://docs.phidata.com/knowledge/pdf): Load local PDF files to a knowledge base
*   [PDF URL knowledge base](https://docs.phidata.com/knowledge/pdf-url): Load PDF files from a URL to a knowledge base
*   [S3 PDF knowledge base](https://docs.phidata.com/knowledge/s3_pdf): Load PDF files from S3 to a knowledge base
*   [S3 Text knowledge base](https://docs.phidata.com/knowledge/s3_text): Load text files from S3 to a knowledge base
*   [Text knowledge base](https://docs.phidata.com/knowledge/text): Load text/docx files to a knowledge base
*   [Website knowledge base](https://docs.phidata.com/knowledge/website): Load website data to a knowledge base
*   [Wikipedia knowledge base](https://docs.phidata.com/knowledge/wikipedia): Load wikipedia articles to a knowledge base

*   [Vector Databases](#vector-databases)
*   [Loading the Knowledge Base](#loading-the-knowledge-base)</content>
</page>

<page>
  <title>Sqlite Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/reference/storage/sqlite</url>
  <content>Example
-------

    from phi.storage.agent.sqlite import SqlAgentStorage
    
    # Create a storage backend using the Sqlite database
    storage = SqlAgentStorage(
        # store sessions in the ai.sessions table
        table_name="agent_sessions",
        # db_file: Sqlite database file
        db_file=db_file,
    )
    
    # Add storage to the Agent
    agent = Agent(storage=storage)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `schema` | `Optional[str]` | `"ai"` | Schema name, default is "ai". |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_engine` | `Optional[Engine]` | `None` | Database engine to be used. |
| `schema_version` | `int` | `1` | Version of the schema, default is 1. |
| `auto_upgrade_schema` | `bool` | `False` | If true, automatically upgrades the schema when necessary. |</content>
</page>

<page>
  <title>Single Store Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/reference/storage/singlestore</url>
  <content>Example
-------

    from phi.storage.agent.singlestore import S2AgentStorage
    
    # Create a storage backend using the SingleStore database
    storage = S2AgentStorage(
        # store sessions in the ai.sessions table
        table_name="agent_sessions",
        # db_engine: SingleStore database engine
        db_engine=db_engine,
        # schema: SingleStore schema
        schema="ai",
    )
    
    # Add storage to the Agent
    agent = Agent(storage=storage)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `schema` | `Optional[str]` | `"ai"` | Schema name. |
| `db_url` | `Optional[str]` | `None` | Database URL, if provided. |
| `db_engine` | `Optional[Engine]` | `None` | Database engine to be used. |
| `schema_version` | `int` | `1` | Version of the schema. |
| `auto_upgrade_schema` | `bool` | `False` | If `true`, automatically upgrades the schema when necessary. |</content>
</page>

<page>
  <title>DynamoDB Agent Storage - Phidata</title>
  <url>https://docs.phidata.com/reference/storage/dynamodb</url>
  <content>Example
-------

    from phi.storage.agent.dynamodb import DynamoDbAgentStorage
    
    # Create a storage backend using the DynamoDB database
    storage = DynamoDbAgentStorage(
        # store sessions in the ai.sessions table
        table_name="agent_sessions",
        # region_name: AWS region name
        region_name="us-east-1",
    )
    
    # Add storage to the Agent
    agent = Agent(storage=storage)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | Name of the table to be used. |
| `region_name` | `Optional[str]` | `None` | Region name of the DynamoDB table. |
| `aws_access_key_id` | `Optional[str]` | `None` | AWS access key id, if provided. |
| `aws_secret_access_key` | `Optional[str]` | `None` | AWS secret access key, if provided. |
| `endpoint_url` | `Optional[str]` | `None` | Endpoint URL, if provided. |
| `create_table_if_not_exists` | `bool` | `True` | If true, creates the table if it does not exist. |</content>
</page>

<page>
  <title>Introduction - Phidata</title>
  <url>https://docs.phidata.com/vectordb/introduction</url>
  <content>Vector databases enable us to store information as embeddings and search for “results similar” to our input query using cosine similarity or full text search. These results are then provided to the Agent as context so it can respond in a context-aware manner using Retrieval Augmented Generation (**RAG**).

Here’s how vector databases are used with Agents:

Many vector databases also support hybrid search, which combines the power of vector similarity search with traditional keyword-based search. This approach can significantly improve the relevance and accuracy of search results, especially for complex queries or when dealing with diverse types of data.

Hybrid search typically works by:

1.  Performing a vector similarity search to find semantically similar content.
2.  Conducting a keyword-based search to identify exact or close matches.
3.  Combining the results using a weighted approach to provide the most relevant information.

This capability allows for more flexible and powerful querying, often yielding better results than either method alone.

The following VectorDb are currently supported:

*   [PgVector](https://docs.phidata.com/vectordb/pgvector)\*
*   [LanceDb](https://docs.phidata.com/vectordb/lancedb)\*
*   [Pinecone](https://docs.phidata.com/vectordb/pinecone)\*
*   [Qdrant](https://docs.phidata.com/vectordb/qdrant)

\*hybrid search supported

Each of these databases has its own strengths and features, including varying levels of support for hybrid search. Be sure to check the specific documentation for each to understand how to best leverage their capabilities in your projects.</content>
</page>

<page>
  <title>PgVector Agent Knowledge - Phidata</title>
  <url>https://docs.phidata.com/vectordb/pgvector</url>
  <content>Setup
-----

Example
-------

PgVector Params
---------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | The name of the table to use. |
| `schema` | `str` | \- | The schema to use. |
| `db_url` | `str` | \- | The database URL to connect to. |
| `db_engine` | `Engine` | \- | The database engine to use. |
| `embedder` | `Embedder` | \- | The embedder to use. |
| `search_type` | `SearchType` | vector | The search type to use. |
| `vector_index` | `Union[Ivfflat, HNSW]` | \- | The vector index to use. |
| `distance` | `Distance` | cosine | The distance to use. |
| `prefix_match` | `bool` | \- | Whether to use prefix matching. |
| `vector_score_weight` | `float` | 0.5 | Weight for vector similarity in hybrid search. Must be between 0 and 1. |
| `content_language` | `str` | \- | The content language to use. |
| `schema_version` | `int` | \- | The schema version to use. |
| `auto_upgrade_schema` | `bool` | \- | Whether to auto upgrade the schema. |</content>
</page>

<page>
  <title>Qdrant Agent Knowledge - Phidata</title>
  <url>https://docs.phidata.com/vectordb/qdrant</url>
  <content>Setup
-----

Follow the instructions in the [Qdrant Setup Guide](https://qdrant.tech/documentation/guides/installation/) to install Qdrant locally. Here is a guide to get API keys: [Qdrant API Keys](https://qdrant.tech/documentation/cloud/authentication/).

Example
-------

    import os
    import typer
    from typing import Optional
    from rich.prompt import Prompt
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.qdrant import Qdrant
    
    api_key = os.getenv("QDRANT_API_KEY")
    qdrant_url = os.getenv("QDRANT_URL")
    collection_name = "thai-recipe-index"
    
    vector_db = Qdrant(
        collection=collection_name,
        url=qdrant_url,
        api_key=api_key,
    )
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=True, upsert=True)
    
    
    def qdrant_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge=knowledge_base,
            tool_calls=True,
            use_tools=True,
            show_tool_calls=True,
            debug_mode=True,
        )
    
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(qdrant_agent)
    
    

Qdrant Params
-------------

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | Name of the Qdrant collection |
| `embedder` | `Embedder` | `OpenAIEmbedder()` | Embedder for embedding the document contents |
| `distance` | `Distance` | `Distance.cosine` | Distance metric for similarity search |
| `location` | `Optional[str]` | `None` | Location of the Qdrant database |
| `url` | `Optional[str]` | `None` | URL of the Qdrant server |
| `port` | `Optional[int]` | `6333` | Port number for the Qdrant server |
| `grpc_port` | `int` | `6334` | gRPC port number for the Qdrant server |
| `prefer_grpc` | `bool` | `False` | Whether to prefer gRPC over HTTP |
| `https` | `Optional[bool]` | `None` | Whether to use HTTPS |
| `api_key` | `Optional[str]` | `None` | API key for authentication |
| `prefix` | `Optional[str]` | `None` | Prefix for the Qdrant API |
| `timeout` | `Optional[float]` | `None` | Timeout for Qdrant operations |
| `host` | `Optional[str]` | `None` | Host address for the Qdrant server |
| `path` | `Optional[str]` | `None` | Path to the Qdrant database |</content>
</page>

<page>
  <title>Pinecone Agent Knowledge - Phidata</title>
  <url>https://docs.phidata.com/vectordb/pinecone</url>
  <content>    import os
    import typer
    from typing import Optional
    from rich.prompt import Prompt
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pineconedb import PineconeDB
    
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = "thai-recipe-hybrid-search"
    
    vector_db = PineconeDB(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
        api_key=api_key,
        use_hybrid_search=True,
        hybrid_alpha=0.5,
    )
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=True, upsert=True)
    
    
    def pinecone_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge=knowledge_base,
            show_tool_calls=True,
            debug_mode=True,
        )
    
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(pinecone_agent)</content>
</page>

<page>
  <title>LanceDB Agent Knowledge - Phidata</title>
  <url>https://docs.phidata.com/vectordb/lancedb</url>
  <content>    import typer
    from typing import Optional
    from rich.prompt import Prompt
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.lancedb import LanceDb
    from phi.vectordb.search import SearchType
    
    # LanceDB Vector DB
    vector_db = LanceDb(
        table_name="recipes",
        uri="/tmp/lancedb",
        search_type=SearchType.keyword,
    )
    
    # Knowledge Base
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=True)
    
    
    def lancedb_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge=knowledge_base,
            show_tool_calls=True,
            debug_mode=True,
        )
    
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(lancedb_agent)</content>
</page>

<page>
  <title>ChromaDB Agent Knowledge - Phidata</title>
  <url>https://docs.phidata.com/vectordb/chroma</url>
  <content>Setup
-----

Example
-------

    import typer
    from rich.prompt import Prompt
    from typing import Optional
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.chroma import ChromaDb
    
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=ChromaDb(collection="recipes"),
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=False)
    
    
    def pdf_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge_base=knowledge_base,
            use_tools=True,
            show_tool_calls=True,
            debug_mode=True,
        )
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(pdf_agent)
    
    

ChromaDb Params
---------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | The name of the collection to use. |
| `embedder` | `Embedder` | OpenAIEmbedder() | The embedder to use for embedding document contents. |
| `distance` | `Distance` | cosine | The distance metric to use. |
| `path` | `str` | "tmp/chromadb" | The path where ChromaDB data will be stored. |
| `persistent_client` | `bool` | False | Whether to use a persistent ChromaDB client. |</content>
</page>

<page>
  <title>Combined KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/knowledge/combined</url>
  <content>The **CombinedKnowledgeBase** combines multiple knowledge bases into 1 and is used when your app needs information using multiple sources.

Usage
-----

Then use the `knowledge_base` with an Agent:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `sources` | `List[AgentKnowledge]` | \- | List of Agent knowledge bases. |
| `reader` | `Reader` | \- | A `Reader` that converts the content of the documents into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>ArXiv Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/arxiv</url>
  <content>The **ArxivKnowledgeBase** reads Arxiv articles, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `queries` | `List[str]` | \- | Queries to search |
| `reader` | `ArxivReader` | `ArxivReader()` | A `ArxivReader` that reads the articles and converts them into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |</content>
</page>

<page>
  <title>CSV Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/csv</url>
  <content>The **CSVKnowledgeBase** reads **local CSV** files, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to docx files. Can point to a single docx file or a directory of docx files. |
| `reader` | `CSVReader` | `CSVReader()` | A `CSVReader` that converts the CSV files into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>CSV URL Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/csv-url</url>
  <content>The **CSVUrlKnowledgeBase** reads **CSVs from urls**, converts them into vector embeddings and loads them to a vector database.

Usage
-----

Then use the `knowledge_base` with an Agent:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `urls` | `List[str]` | \- | URLs for `PDF` files. |
| `reader` | `CSVUrlReader` | `CSVUrlReader()` | A `CSVUrlReader` that converts the `CSVs` into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Docx Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/docx</url>
  <content>The **DocxKnowledgeBase** reads **local docx** files, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to docx files. Can point to a single docx file or a directory of docx files. |
| `formats` | `List[str]` | `[".doc", ".docx"]` | Formats accepted by this knowledge base. |
| `reader` | `DocxReader` | `DocxReader()` | A `DocxReader` that converts the docx files into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Document Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/document</url>
  <content>The **DocumentKnowledgeBase** reads **local docs** files, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `documents` | `List[Document]` | \- | List of documents to load into the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `reader` | `Reader` | \- | A `Reader` that converts the content of the documents into `Documents` for the vector database. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>JSON Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/json</url>
  <content>The **JSONKnowledgeBase** reads **local JSON** files, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to `JSON` files. Can point to a single JSON file or a directory of JSON files. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `reader` | `JSONReader` | `JSONReader()` | A `JSONReader` that converts the `JSON` files into `Documents` for the vector database. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>LangChain Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/langchain</url>
  <content>The **LangchainKnowledgeBase** allows us to use a LangChain retriever or vector store as a knowledge base.

Usage
-----

    from phi.agent import Agent
    from phi.knowledge.langchain import LangChainKnowledgeBase
    
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import Chroma
    
    chroma_db_dir = "./chroma_db"
    
    
    def load_vector_store():
        state_of_the_union = ws_settings.ws_root.joinpath("data/demo/state_of_the_union.txt")
        # -*- Load the document
        raw_documents = TextLoader(str(state_of_the_union)).load()
        # -*- Split it into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        documents = text_splitter.split_documents(raw_documents)
        # -*- Embed each chunk and load it into the vector store
        Chroma.from_documents(documents, OpenAIEmbeddings(), persist_directory=str(chroma_db_dir))
    
    
    # -*- Get the vectordb
    db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory=str(chroma_db_dir))
    # -*- Create a retriever from the vector store
    retriever = db.as_retriever()
    
    # -*- Create a knowledge base from the vector store
    knowledge_base = LangChainKnowledgeBase(retriever=retriever)
    
    agent = Agent(knowledge_base=knowledge_base, add_references_to_prompt=True)
    conv.print_response("What did the president say about technology?")
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `retriever` | `Any` | `None` | LangChain retriever. |
| `vectorstore` | `Any` | `None` | LangChain vector store used to create a retriever. |
| `search_kwargs` | `dict` | `None` | Search kwargs when creating a retriever using the langchain vector store. |</content>
</page>

<page>
  <title>LlamaIndex Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/llamaindex</url>
  <content>The **LlamaIndexKnowledgeBase** allows us to use a LlamaIndex retriever or vector store as a knowledge base.

Usage
-----

    pip install llama-index-core llama-index-readers-file llama-index-embeddings-openai
    

    
    from pathlib import Path
    from shutil import rmtree
    
    import httpx
    from phi.agent import Agent
    from phi.knowledge.llamaindex import LlamaIndexKnowledgeBase
    from llama_index.core import (
        SimpleDirectoryReader,
        StorageContext,
        VectorStoreIndex,
    )
    from llama_index.core.retrievers import VectorIndexRetriever
    from llama_index.core.node_parser import SentenceSplitter
    
    
    data_dir = Path(__file__).parent.parent.parent.joinpath("wip", "data", "paul_graham")
    if data_dir.is_dir():
        rmtree(path=data_dir, ignore_errors=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    
    url = "https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt"
    file_path = data_dir.joinpath("paul_graham_essay.txt")
    response = httpx.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"File downloaded and saved as {file_path}")
    else:
        print("Failed to download the file")
    
    
    documents = SimpleDirectoryReader(str(data_dir)).load_data()
    
    splitter = SentenceSplitter(chunk_size=1024)
    
    nodes = splitter.get_nodes_from_documents(documents)
    
    storage_context = StorageContext.from_defaults()
    
    index = VectorStoreIndex(nodes=nodes, storage_context=storage_context)
    
    retriever = VectorIndexRetriever(index)
    
    # Create a knowledge base from the vector store
    knowledge_base = LlamaIndexKnowledgeBase(retriever=retriever)
    
    # Create an agent with the knowledge base
    agent = Agent(knowledge_base=knowledge_base, search_knowledge=True, debug_mode=True, show_tool_calls=True)
    
    # Use the agent to ask a question and print a response.
    agent.print_response("Explain what this text means: low end eats the high end", markdown=True)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `retriever` | `BaseRetriever` | `None` | LlamaIndex retriever used for querying the knowledge base. |
| `loader` | `Optional[Callable]` | `None` | Optional callable function to load documents into the knowledge base. |</content>
</page>

<page>
  <title>PDF Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/pdf</url>
  <content>The **PDFKnowledgeBase** reads **local PDF** files, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an Agent:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to `PDF` files. Can point to a single PDF file or a directory of PDF files. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. Example: `PgVector` |
| `reader` | `Union[PDFReader, PDFImageReader]` | `PDFReader()` | A `PDFReader` that converts the `PDFs` into `Documents` for the vector database. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. For Example: Create an index for `PgVector`. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |</content>
</page>

<page>
  <title>PDF URL Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/pdf-url</url>
  <content>The **PDFUrlKnowledgeBase** reads **PDFs from urls**, converts them into vector embeddings and loads them to a vector database.

Usage
-----

Then use the `knowledge_base` with an Agent:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `urls` | `List[str]` | \- | URLs for `PDF` files. |
| `reader` | `Union[PDFUrlReader, PDFUrlImageReader]` | `PDFUrlReader()` | A `PDFUrlReader` that converts the `PDFs` into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>S3 PDF Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/s3_pdf</url>
  <content>The **S3PDFKnowledgeBase** reads **PDF** files from an S3 bucket, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `S3PDFReader` | `S3PDFReader()` | A `S3PDFReader` that converts the `PDFs` into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |</content>
</page>

<page>
  <title>S3 Text Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/s3_text</url>
  <content>The **S3TextKnowledgeBase** reads **text** files from an S3 bucket, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `formats` | `List[str]` | `[".doc", ".docx"]` | Formats accepted by this knowledge base. |
| `reader` | `S3TextReader` | `S3TextReader()` | A `S3TextReader` that converts the `Text` files into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |</content>
</page>

<page>
  <title>Text Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/text</url>
  <content>The **TextKnowledgeBase** reads **local txt** files, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an Agent:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to text files. Can point to a single txt file or a directory of txt files. |
| `formats` | `List[str]` | `[".txt"]` | Formats accepted by this knowledge base. |
| `reader` | `TextReader` | `TextReader()` | A `TextReader` that converts the text files into `Documents` for the vector database. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |

*   [Usage](#usage)
*   [Params](#params)</content>
</page>

<page>
  <title>Website Knowledge Base - Phidata</title>
  <url>https://docs.phidata.com/knowledge/website</url>
  <content>The **WebsiteKnowledgeBase** reads websites, converts them into vector embeddings and loads them to a `vector_db`.

Usage
-----

Then use the `knowledge_base` with an `Agent`:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `urls` | `List[str]` | \- | URLs to read |
| `reader` | `WebsiteReader` | \- | A `WebsiteReader` that reads the urls and converts them into `Documents` for the vector database. |
| `max_depth` | `int` | `3` | Maximum depth to crawl. |
| `max_links` | `int` | `10` | Number of links to crawl. |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |</content>
</page>

<page>
  <title>Wikipedia KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/knowledge/wikipedia</url>
  <content>The **WikipediaKnowledgeBase** reads wikipedia topics, converts them into vector embeddings and loads them to a vector databse.

Usage
-----

Then use the `knowledge_base` with an Agent:

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `topics` | `List[str]` | \- | Topics to read |
| `vector_db` | `VectorDb` | \- | Vector Database for the Knowledge Base. |
| `reader` | `Reader` | \- | A `Reader` that reads the topics and converts them into `Documents` for the vector database. |
| `num_documents` | `int` | `5` | Number of documents to return on search. |
| `optimize_on` | `int` | \- | Number of documents to optimize the vector db on. |
| `chunking_strategy` | `ChunkingStrategy` | `FixedSizeChunking` | The chunking strategy to use. |</content>
</page>

<page>
  <title>AgentKnowledge - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/base</url>
  <content>[​](#agentknowledge-params)

AgentKnowledge Params
----------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |</content>
</page>

<page>
  <title>Fixed Size Chunking - Phidata</title>
  <url>https://docs.phidata.com/chunking/fixed-size-chunking</url>
  <content>Fixed size chunking is a method of splitting documents into smaller chunks of a specified size, with optional overlap between chunks. This is useful when you want to process large documents in smaller, manageable pieces.

Usage
-----

    from phi.agent import Agent
    from phi.document.chunking.fixed import FixedSizeChunking
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(table_name="recipes_fixed_size_chunking", db_url=db_url),
        chunking_strategy=FixedSizeChunking(),
    )
    knowledge_base.load(recreate=False)  # Comment out after first run
    
    agent = Agent(
        knowledge_base=knowledge_base,
        search_knowledge=True,
    )
    
    agent.print_response("How to make Thai curry?", markdown=True)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chunk_size` | `int` | `5000` | The maximum size of each chunk. |
| `overlap` | `int` | `0` | The number of characters to overlap between chunks. |</content>
</page>

<page>
  <title>Arxiv KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/arxiv</url>
  <content>Example
-------

ArxivKnowledgeBase Params
-------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `queries` | `List[str]` | `[]` | Queries to search |
| `reader` | `ArxivReader` | `ArxivReader()` | A `ArxivReader` that reads the articles and converts them into `Documents` for the vector database |

AgentKnowledge Params
---------------------

`ArxivKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [ArxivKnowledgeBase Params](#arxivknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>Document Chunking - Phidata</title>
  <url>https://docs.phidata.com/chunking/document-chunking</url>
  <content>Document chunking is a method of splitting documents into smaller chunks based on document structure like paragraphs and sections. It analyzes natural document boundaries rather than splitting at fixed character counts. This is useful when you want to process large documents while preserving semantic meaning and context.

Usage
-----

    from phi.agent import Agent
    from phi.document.chunking.document import DocumentChunking
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(table_name="recipes_document_chunking", db_url=db_url),
        chunking_strategy=DocumentChunking(),
    )
    knowledge_base.load(recreate=False)  # Comment out after first run
    
    agent = Agent(
        knowledge_base=knowledge_base,
        search_knowledge=True,
    )
    
    agent.print_response("How to make Thai curry?", markdown=True)
    
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chunk_size` | `int` | `5000` | The maximum size of each chunk. |
| `overlap` | `int` | `0` | The number of characters to overlap between chunks. |</content>
</page>

<page>
  <title>Combined KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/combined</url>
  <content>Example
-------

CombinedKnowledgeBase Params
----------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `sources` | `List[AgentKnowledge]` | `[]` | List of knowledge bases. |

AgentKnowledge Params
---------------------

`CombinedKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [CombinedKnowledgeBase Params](#combinedknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>CSV KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/csv</url>
  <content>CSVKnowledgeBase Params
-----------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to the CSV file |
| `reader` | `CSVReader` | `CSVReader()` | A `CSVReader` that reads the CSV file and converts it into `Documents` for the vector database |

AgentKnowledge Params
---------------------

`CSVKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |</content>
</page>

<page>
  <title>Document KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/document</url>
  <content>DocumentKnowledgeBase Params
----------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `documents` | `List[Document]` | \- | List of Document objects to be used as the knowledge base |

AgentKnowledge Params
---------------------

`DocumentKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |</content>
</page>

<page>
  <title>JSON KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/json</url>
  <content>Example
-------

JSONKnowledgeBase Params
------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to `JSON` files.  
Can point to a single JSON file or a directory of JSON files. |
| `reader` | `JSONReader` | `JSONReader()` | A `JSONReader` that converts the `JSON` files into `Documents` for the vector database. |

AgentKnowledge Params
---------------------

`JSONKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [JSONKnowledgeBase Params](#jsonknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>Docx KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/docx</url>
  <content>Example
-------

DocxKnowledgeBase Params
------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to text files. Can point to a single docx file or a directory of docx files. |
| `formats` | `List[str]` | `[".doc", ".docx"]` | Formats accepted by this knowledge base. |
| `reader` | `DocxReader` | `DocxReader()` | A `DocxReader` that converts the docx files into `Documents` for the vector database. |

AgentKnowledge Params
---------------------

`DocxKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [DocxKnowledgeBase Params](#docxknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>LangChain KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/langchain</url>
  <content>Example
-------

LangChainKnowledgeBase Params
-----------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `loader` | `Optional[Callable]` | `None` | LangChain loader. |
| `vectorstore` | `Optional[Any]` | `None` | LangChain vector store used to create a retriever. |
| `search_kwargs` | `Optional[dict]` | `None` | Search kwargs when creating a retriever using the langchain vector store. |
| `retriever` | `Optional[Any]` | `None` | LangChain retriever. |

AgentKnowledge Params
---------------------

`LangChainKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [LangChainKnowledgeBase Params](#langchainknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>LlamaIndex KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/llamaindex</url>
  <content>LlamaIndexKnowledgeBase Params
------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `retriever` | `BaseRetriever` | \- | LlamaIndex retriever used for querying the knowledge base |
| `loader` | `Optional[Callable]` | `None` | Optional loader function to load documents into the knowledge base |

AgentKnowledge Params
---------------------

`LlamaIndexKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |</content>
</page>

<page>
  <title>PDF KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/pdf</url>
  <content>Example
-------

PDFKnowledgeBase Params
-----------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to `PDF` files. Can point to a single PDF file or a directory of PDF files. |
| `reader` | `Union[PDFReader, PDFImageReader]` | `PDFReader()` | A `PDFReader` or `PDFImageReader` that converts the `PDFs` into `Documents` for the vector database. |

AgentKnowledge Params
---------------------

`PDFKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [PDFKnowledgeBase Params](#pdfknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>PDF Url KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/pdf-url</url>
  <content>Example
-------

PDFUrlKnowledgeBase Params
--------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `urls` | `List[str]` | \- | URLs for `PDF` files. |
| `reader` | `PDFUrlReader` | \- | A `PDFUrlReader` that converts the `PDFs` into `Documents` for the vector database. |

AgentKnowledge Params
---------------------

`PDFUrlKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [PDFUrlKnowledgeBase Params](#pdfurlknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>Text KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/text</url>
  <content>Example
-------

TextKnowledgeBase Params
------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `path` | `Union[str, Path]` | \- | Path to text files. Can point to a single text file or a directory of text files. |
| `formats` | `List[str]` | `[".txt"]` | Formats accepted by this knowledge base. |
| `reader` | `TextReader` | `TextReader()` | A `TextReader` that converts the text files into `Documents` for the vector database. |

AgentKnowledge Params
---------------------

`TextKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [TextKnowledgeBase Params](#textknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>Website KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/website</url>
  <content>Example
-------

WebsiteKnowledgeBase Params
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `urls` | `List[str]` | `[]` | URLs to read |
| `reader` | `Optional[WebsiteReader]` | `None` | A `WebsiteReader` that reads the urls and converts them into `Documents` for the vector database. |
| `max_depth` | `int` | `3` | Maximum depth to crawl. |
| `max_links` | `int` | `10` | Number of links to crawl. |

AgentKnowledge Params
---------------------

`WebsiteKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [WebsiteKnowledgeBase Params](#websiteknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>Wikipedia KnowledgeBase - Phidata</title>
  <url>https://docs.phidata.com/reference/kb/wikipedia</url>
  <content>Example
-------

WikipediaKnowledgeBase Params
-----------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `topics` | `List[str]` | \[\] | Topics to read |

AgentKnowledge Params
---------------------

`WikipediaKnowledgeBase` is a subclass of the `AgentKnowledge` class and has access to the same params

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `reader` | `Optional[Reader]` | `None` | Reader to read the documents |
| `vector_db` | `Optional[VectorDb]` | `None` | Vector db to store the knowledge base |
| `num_documents` | `int` | `2` | Number of relevant documents to return on search |
| `optimize_on` | `Optional[int]` | `1000` | Number of documents to optimize the vector db on |
| `driver` | `str` | `"knowledge"` | Driver for the Assistant knowledge |

*   [Example](#example)
*   [WikipediaKnowledgeBase Params](#wikipediaknowledgebase-params)
*   [AgentKnowledge Params](#agentknowledge-params)</content>
</page>

<page>
  <title>Agentic Chunking - Phidata</title>
  <url>https://docs.phidata.com/chunking/agentic-chunking</url>
  <content>Agentic chunking is an intelligent method of splitting documents into smaller chunks by using an LLM to determine natural breakpoints in the text. Rather than splitting text at fixed character counts, it analyzes the content to find semantically meaningful boundaries like paragraph breaks and topic transitions.

Usage
-----

    from phi.agent import Agent
    from phi.document.chunking.agentic import AgenticChunking
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(table_name="recipes_agentic_chunking", db_url=db_url),
        chunking_strategy=AgenticChunking(),
    )
    knowledge_base.load(recreate=False)  # Comment out after first run
    
    agent = Agent(
        knowledge_base=knowledge_base,
        search_knowledge=True,
    )
    
    agent.print_response("How to make Thai curry?", markdown=True)
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `Model` | `OpenAIChat` | The model to use for chunking. |
| `max_chunk_size` | `int` | `5000` | The maximum size of each chunk. |</content>
</page>

<page>
  <title>Semantic Chunking - Phidata</title>
  <url>https://docs.phidata.com/chunking/semantic-chunking</url>
  <content>Semantic chunking is a method of splitting documents into smaller chunks by analyzing semantic similarity between text segments using embeddings. It uses the chonkie library to identify natural breakpoints where the semantic meaning changes significantly, based on a configurable similarity threshold. This helps preserve context and meaning better than fixed-size chunking by ensuring semantically related content stays together in the same chunk, while splitting occurs at meaningful topic transitions.

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `embedder` | `Embedder` | `OpenAIEmbedder` | The embedder to use for semantic chunking. |
| `chunk_size` | `int` | `5000` | The maximum size of each chunk. |
| `similarity_threshold` | `float` | `0.5` | The similarity threshold for determining chunk boundaries. |

*   [Params](#params)</content>
</page>

<page>
  <title>Recursive Chunking - Phidata</title>
  <url>https://docs.phidata.com/chunking/recursive-chunking</url>
  <content>Recursive chunking is a method of splitting documents into smaller chunks by recursively applying a chunking strategy. This is useful when you want to process large documents in smaller, manageable pieces.

    from phi.agent import Agent
    from phi.document.chunking.recursive import RecursiveChunking
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.pgvector import PgVector
    
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(table_name="recipes_recursive_chunking", db_url=db_url),
        chunking_strategy=RecursiveChunking(),
    )
    knowledge_base.load(recreate=False)  # Comment out after first run
    
    agent = Agent(
        knowledge_base=knowledge_base,
        search_knowledge=True,
    )
    
    agent.print_response("How to make Thai curry?", markdown=True)
    
    

Params
------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `chunk_size` | `int` | `5000` | The maximum size of each chunk. |
| `overlap` | `int` | `0` | The number of characters to overlap between chunks. |</content>
</page>

<page>
  <title>PgVector - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/pgvector</url>
  <content>PgVectorDb Params
-----------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `table_name` | `str` | \- | The name of the table to use. |
| `schema` | `str` | \- | The schema to use. |
| `db_url` | `str` | \- | The database URL to connect to. |
| `db_engine` | `Engine` | \- | The database engine to use. |
| `embedder` | `Embedder` | \- | The embedder to use. |
| `search_type` | `SearchType` | vector | The search type to use. |
| `vector_index` | `Union[Ivfflat, HNSW]` | \- | The vector index to use. |
| `distance` | `Distance` | cosine | The distance to use. |
| `prefix_match` | `bool` | \- | Whether to use prefix matching. |
| `vector_score_weight` | `float` | 0.5 | Weight for vector similarity in hybrid search. Must be between 0 and 1. |
| `content_language` | `str` | \- | The content language to use. |
| `schema_version` | `int` | \- | The schema version to use. |
| `auto_upgrade_schema` | `bool` | \- | Whether to auto upgrade the schema. |</content>
</page>

<page>
  <title>Single Store - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/singlestore</url>
  <content>[​](#single-store-params)

Single Store Params
------------------------------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | The name of the collection to use. |
| `schema` | `Optional[str]` | `"ai"` | The database schema to use. |
| `db_url` | `Optional[str]` | `None` | The database connection URL. |
| `db_engine` | `Optional[Engine]` | `None` | SQLAlchemy engine instance. |
| `embedder` | `Embedder` | `OpenAIEmbedder()` | The embedder to use for creating vector embeddings. |
| `distance` | `Distance` | `Distance.cosine` | The distance metric to use for similarity search. |</content>
</page>

<page>
  <title>PgVector - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/pgvector2</url>
  <content>PgVectorDb Params
-----------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | Name of the collection to store vector data |
| `schema` | `Optional[str]` | `"ai"` | Database schema name |
| `db_url` | `Optional[str]` | `None` | Database connection URL |
| `db_engine` | `Optional[Engine]` | `None` | SQLAlchemy database engine |
| `embedder` | `Optional[Embedder]` | `None` | Embedder instance for creating embeddings (defaults to OpenAIEmbedder if not provided) |
| `distance` | `Distance` | `Distance.cosine` | Distance metric for vector comparisons |
| `index` | `Optional[Union[Ivfflat, HNSW]]` | `HNSW()` | Vector index configuration |</content>
</page>

<page>
  <title>Qdrant - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/qdrant</url>
  <content>Qdrant Params
-------------

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | Name of the Qdrant collection |
| `embedder` | `Embedder` | `OpenAIEmbedder()` | Embedder for embedding the document contents |
| `distance` | `Distance` | `Distance.cosine` | Distance metric for similarity search |
| `location` | `Optional[str]` | `None` | Location of the Qdrant database |
| `url` | `Optional[str]` | `None` | URL of the Qdrant server |
| `port` | `Optional[int]` | `6333` | Port number for the Qdrant server |
| `grpc_port` | `int` | `6334` | gRPC port number for the Qdrant server |
| `prefer_grpc` | `bool` | `False` | Whether to prefer gRPC over HTTP |
| `https` | `Optional[bool]` | `None` | Whether to use HTTPS |
| `api_key` | `Optional[str]` | `None` | API key for authentication |
| `prefix` | `Optional[str]` | `None` | Prefix for the Qdrant API |
| `timeout` | `Optional[float]` | `None` | Timeout for Qdrant operations |
| `host` | `Optional[str]` | `None` | Host address for the Qdrant server |
| `path` | `Optional[str]` | `None` | Path to the Qdrant database |</content>
</page>

<page>
  <title>ChromaDb - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/chromadb</url>
  <content>    import typer
    from rich.prompt import Prompt
    from typing import Optional
    
    from phi.agent import Agent
    from phi.knowledge.pdf import PDFUrlKnowledgeBase
    from phi.vectordb.chroma import ChromaDb
    
    
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=ChromaDb(collection="recipes"),
    )
    
    # Comment out after first run
    knowledge_base.load(recreate=False)
    
    
    def pdf_agent(user: str = "user"):
        run_id: Optional[str] = None
    
        agent = Agent(
            run_id=run_id,
            user_id=user,
            knowledge_base=knowledge_base,
            use_tools=True,
            show_tool_calls=True,
            debug_mode=True,
        )
        if run_id is None:
            run_id = agent.run_id
            print(f"Started Run: {run_id}\n")
        else:
            print(f"Continuing Run: {run_id}\n")
    
        while True:
            message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            if message in ("exit", "bye"):
                break
            agent.print_response(message)
    
    
    if __name__ == "__main__":
        typer.run(pdf_agent)
    
    

ChromaDb Params
---------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `collection` | `str` | \- | The name of the collection to use. |
| `embedder` | `Embedder` | OpenAIEmbedder() | The embedder to use for embedding document contents. |
| `distance` | `Distance` | cosine | The distance metric to use. |
| `path` | `str` | "tmp/chromadb" | The path where ChromaDB data will be stored. |
| `persistent_client` | `bool` | False | Whether to use a persistent ChromaDB client. |</content>
</page>

<page>
  <title>LanceDb - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/lancedb</url>
  <content>LanceDb Params
--------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `uri` | `str` | \- | The URI to connect to. |
| `table` | `LanceTable` | \- | The Lance table to use. |
| `table_name` | `str` | \- | The name of the table to use. |
| `connection` | `DBConnection` | \- | The database connection to use. |
| `api_key` | `str` | \- | The API key to use. |
| `embedder` | `Embedder` | \- | The embedder to use. |
| `search_type` | `SearchType` | vector | The search type to use. |
| `distance` | `Distance` | cosine | The distance to use. |
| `nprobes` | `int` | \- | The number of probes to use. [More Info](https://lancedb.github.io/lancedb/ann_indexes/#use-gpu-to-build-vector-index) |
| `reranker` | `Reranker` | \- | The reranker to use. [More Info](https://lancedb.github.io/lancedb/hybrid_search/eval/) |
| `use_tantivy` | `bool` | \- | Whether to use tantivy. |</content>
</page>

<page>
  <title>PineconeDB - Phidata</title>
  <url>https://docs.phidata.com/reference/vectordb/pineconedb</url>
  <content>PineconeDB Params
-----------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `str` | \- | The name of the Pinecone index |
| `dimension` | `int` | \- | The dimension of the embeddings |
| `spec` | `Union[Dict, ServerlessSpec, PodSpec]` | \- | The index spec |
| `embedder` | `Optional[Embedder]` | `None` | Embedder instance for creating embeddings (defaults to OpenAIEmbedder if not provided) |
| `metric` | `Optional[str]` | `"cosine"` | The metric used for similarity search |
| `additional_headers` | `Optional[Dict[str, str]]` | `None` | Additional headers to pass to the Pinecone client |
| `pool_threads` | `Optional[int]` | `1` | The number of threads to use for the Pinecone client |
| `namespace` | `Optional[str]` | `None` | The namespace for the Pinecone index |
| `timeout` | `Optional[int]` | `None` | The timeout for Pinecone operations |
| `index_api` | `Optional[Any]` | `None` | The Index API object |
| `api_key` | `Optional[str]` | `None` | The Pinecone API key |
| `host` | `Optional[str]` | `None` | The Pinecone host |
| `config` | `Optional[Config]` | `None` | The Pinecone config |
| `use_hybrid_search` | `bool` | `False` | Whether to use hybrid search |
| `hybrid_alpha` | `float` | `0.5` | The alpha value for hybrid search |</content>
</page>

<page>
  <title>phi init - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/init</url>
  <content>Initialize phidata, use -r to reset

[​](#params)

Params
----------------------

[​](#param-reset)

reset

bool

Reset phidata `--reset` `-r`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-login)

login

bool

Login with phidata.com `--login` `-l`</content>
</page>

<page>
  <title>phi start - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/start</url>
  <content>Start resources defined in a resources.py file

[​](#params)

Params
----------------------

[​](#param-resources-file)

resources\_file

str

Path to workspace file.

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`</content>
</page>

<page>
  <title>phi auth - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/auth</url>
  <content>Authenticate with phidata.com

[​](#params)

Params
----------------------

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`</content>
</page>

<page>
  <title>phi stop - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/stop</url>
  <content>Stop resources defined in a resources.py file

[​](#params)

Params
----------------------

[​](#param-resources-file)

resources\_file

str

Path to workspace file.

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`</content>
</page>

<page>
  <title>phi patch - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/patch</url>
  <content>Update resources defined in a resources.py file

[​](#params)

Params
----------------------

[​](#param-resources-file)

resources\_file

str

Path to workspace file.

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`</content>
</page>

<page>
  <title>phi restart - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/restart</url>
  <content>Restart resources defined in a resources.py file

[​](#params)

Params
----------------------

[​](#param-resources-file)

resources\_file

str

Path to workspace file.

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`</content>
</page>

<page>
  <title>phi config - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/config</url>
  <content>Print phi config

Params
------

Print debug logs. `--debug` `-d`

Show all workspaces `--all` `-a`

*   [Params](#params)</content>
</page>

<page>
  <title>phi set - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/set</url>
  <content>Set current directory as active workspace

[​](#params)

Params
----------------------

[​](#param-ws-name)

ws\_name

bool

Active workspace name `--ws`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`</content>
</page>

<page>
  <title>phi reset - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/phi/reset</url>
  <content>phi

Reset phi installation

[​](#params)

Params
----------------------

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/reference/cli/phi/reset.mdx)

[phi set](https://docs.phidata.com/reference/cli/phi/set)[phi ws create](https://docs.phidata.com/reference/cli/ws/create)

On this page

*   [Params](#params)</content>
</page>

<page>
  <title>phi ws create - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/create</url>
  <content>Create a new workspace in the current directory.

[​](#params)

Params
----------------------

[​](#param-name)

name

str

Name of the new workspace. `--name` `-n`

[​](#param-template)

template

str

Starter template for the workspace. `--template` `-t`

[​](#param-url)

url

str

URL of the starter template. `--url` `-u`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`</content>
</page>

<page>
  <title>phi ws down - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/down</url>
  <content>Delete resources for active workspace

[​](#params)

Params
----------------------

[​](#param-resources-filter)

resources\_filter

str

Resource filter. Format - ENV:INFRA:GROUP:NAME:TYPE

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`</content>
</page>

<page>
  <title>phi ws up - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/up</url>
  <content>Create resources for the active workspace

[​](#params)

Params
----------------------

[​](#param-resources-filter)

resources\_filter

str

Resource filter. Format - ENV:INFRA:GROUP:NAME:TYPE

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`

[​](#param-pull)

pull

bool

Pull `--pull` `-p`</content>
</page>

<page>
  <title>phi ws patch - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/patch</url>
  <content>Update resources for active workspace

[​](#params)

Params
----------------------

[​](#param-resources-filter)

resources\_filter

str

Resource filter. Format - ENV:INFRA:GROUP:NAME:TYPE

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`

[​](#param-pull)

pull

bool

Pull `--pull` `-p`</content>
</page>

<page>
  <title>phi ws restart - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/restart</url>
  <content>Restart resources for active workspace

[​](#params)

Params
----------------------

[​](#param-resources-filter)

resources\_filter

str

Resource filter. Format - ENV:INFRA:GROUP:NAME:TYPE

[​](#param-env-filter)

env\_filter

str

Filter the environment to deploy `--env` `-e`

[​](#param-infra-filter)

infra\_filter

str

Filter the infra to deploy. `--infra` `-i`

[​](#param-config-filter)

config\_filter

str

Filter the config to deploy. `--config` `-c`

[​](#param-group-filter)

group\_filter

str

Filter resources using group name. `--group` `-g`

[​](#param-name-filter)

name\_filter

str

Filter resource using name. `--name` `-n`

[​](#param-type-filter)

type\_filter

str

Filter resource using type `--type` `-t`

[​](#param-dry-run)

dry\_run

bool

Print resources and exit. `--dry-run` `-dr`

[​](#param-auto-confirm)

auto\_confirm

bool

Skip the confirmation before deploying resources. `--yes` `-y`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

[​](#param-force)

force

bool

Force `--force` `-f`

[​](#param-pull)

pull

bool

Pull `--pull` `-p`</content>
</page>

<page>
  <title>phi ws config - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/config</url>
  <content>Prints active workspace config

[​](#params)

Params
----------------------

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`</content>
</page>

<page>
  <title>phi ws delete - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/delete</url>
  <content>phi ws

Delete workspace record

[​](#params)

Params
----------------------

[​](#param-ws-name)

ws\_name

str

Name of the workspace to delete `-ws`

[​](#param-all-workspaces)

all\_workspaces

str

Delete all workspaces from phidata `--all` `-a`

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`

Was this page helpful?

[Suggest edits](https://github.com/phidatahq/phidata-docs/edit/main/reference/cli/ws/delete.mdx)

[phi ws config](https://docs.phidata.com/reference/cli/ws/config)[phi ws setup](https://docs.phidata.com/reference/cli/ws/setup)</content>
</page>

<page>
  <title>phi ws setup - Phidata</title>
  <url>https://docs.phidata.com/reference/cli/ws/setup</url>
  <content>Setup workspace from the current directory

[​](#params)

Params
----------------------

[​](#param-path)

path

str

Path to workspace \[default: current directory\]

[​](#param-print-debug-log)

print\_debug\_log

bool

Print debug logs. `--debug` `-d`</content>
</page>