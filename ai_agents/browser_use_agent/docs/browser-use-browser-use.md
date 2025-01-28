Directory structure:
└── browser-use-browser-use/
    ├── README.md
    ├── LICENSE
    ├── SECURITY.md
    ├── conftest.py
    ├── pyproject.toml
    ├── pytest.ini
    ├── .env.example
    ├── .pre-commit-config.yaml
    ├── .python-version
    ├── browser_use/
    │   ├── README.md
    │   ├── __init__.py
    │   ├── logging_config.py
    │   ├── utils.py
    │   ├── agent/
    │   │   ├── prompts.py
    │   │   ├── service.py
    │   │   ├── tests.py
    │   │   ├── views.py
    │   │   └── message_manager/
    │   │       ├── service.py
    │   │       ├── tests.py
    │   │       └── views.py
    │   ├── browser/
    │   │   ├── browser.py
    │   │   ├── context.py
    │   │   ├── views.py
    │   │   └── tests/
    │   │       ├── screenshot_test.py
    │   │       └── test_clicks.py
    │   ├── controller/
    │   │   ├── service.py
    │   │   ├── views.py
    │   │   └── registry/
    │   │       ├── service.py
    │   │       └── views.py
    │   ├── dom/
    │   │   ├── __init__.py
    │   │   ├── buildDomTree.js
    │   │   ├── service.py
    │   │   ├── views.py
    │   │   ├── history_tree_processor/
    │   │   │   ├── service.py
    │   │   │   └── view.py
    │   │   └── tests/
    │   │       ├── extraction_test.py
    │   │       └── process_dom_test.py
    │   └── telemetry/
    │       ├── service.py
    │       └── views.py
    ├── docs/
    │   ├── README.md
    │   ├── development.mdx
    │   ├── introduction.mdx
    │   ├── mint.json
    │   ├── quickstart.mdx
    │   ├── customize/
    │   │   ├── agent-settings.mdx
    │   │   ├── browser-settings.mdx
    │   │   ├── custom-functions.mdx
    │   │   ├── output-format.mdx
    │   │   ├── real-browser.mdx
    │   │   ├── supported-models.mdx
    │   │   └── system-prompt.mdx
    │   ├── development/
    │   │   ├── contribution-guide.mdx
    │   │   ├── local-setup.mdx
    │   │   ├── roadmap.mdx
    │   │   └── telemetry.mdx
    │   ├── images/
    │   └── logo/
    ├── examples/
    │   ├── simple.py
    │   ├── browser/
    │   │   ├── real_browser.py
    │   │   └── using_cdp.py
    │   ├── custom-functions/
    │   │   ├── clipboard.py
    │   │   ├── file_upload.py
    │   │   ├── notification.py
    │   │   └── save_to_file_hugging_face.py
    │   ├── features/
    │   │   ├── custom_output.py
    │   │   ├── custom_system_prompt.py
    │   │   ├── custom_user_agent.py
    │   │   ├── follow_up_tasks.py
    │   │   ├── initial_actions.py
    │   │   ├── multi-tab_handling.py
    │   │   ├── multiple_agents_same_browser.py
    │   │   ├── parallel_agents.py
    │   │   ├── pause_agent.py
    │   │   ├── restrict_urls.py
    │   │   ├── result_processing.py
    │   │   ├── save_trace.py
    │   │   └── validate_output.py
    │   ├── integrations/
    │   │   ├── discord_api.py
    │   │   └── discord_example.py
    │   ├── models/
    │   │   ├── bedrock_claude.py
    │   │   ├── deepseek-r1.py
    │   │   ├── deepseek.py
    │   │   ├── gemini.py
    │   │   ├── gpt-4o.py
    │   │   ├── ollama.py
    │   │   └── qwen.py
    │   ├── notebook/
    │   │   └── agent_browsing.ipynb
    │   ├── ui/
    │   │   ├── command_line.py
    │   │   └── gradio_demo.py
    │   └── use-cases/
    │       ├── captcha.py
    │       ├── check_appointment.py
    │       ├── find_and_apply_to_jobs.py
    │       ├── online_coding_agent.py
    │       ├── post-twitter.py
    │       ├── scrolling_page.py
    │       ├── test_cv.txt
    │       ├── twitter_cookies.txt
    │       ├── twitter_post_using_cookies.py
    │       └── web_voyager_agent.py
    ├── static/
    ├── tests/
    │   ├── test_agent_actions.py
    │   ├── test_attach_chrome.py
    │   ├── test_core_functionality.py
    │   ├── test_dropdown.py
    │   ├── test_dropdown_complex.py
    │   ├── test_dropdown_error.py
    │   ├── test_excluded_actions.py
    │   ├── test_full_screen.py
    │   ├── test_gif_path.py
    │   ├── test_mind2web.py
    │   ├── test_models.py
    │   ├── test_qwen.py
    │   ├── test_react_dropdown.py
    │   ├── test_self_registered_actions.py
    │   ├── test_service.py
    │   ├── test_stress.py
    │   ├── test_vision.py
    │   └── mind2web_data/
    │       └── processed.json
    └── .github/
        ├── ISSUE_TEMPLATE/
        │   ├── bug_report.yml
        │   ├── config.yml
        │   ├── docs_issue.yml
        │   └── feature_request.yml
        └── workflows/
            └── publish.yml

================================================
File: README.md
================================================
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./static/browser-use-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./static/browser-use.png">
  <img alt="Shows a black Browser Use Logo in light color mode and a white one in dark color mode." src="./static/browser-use.png"  width="full">
</picture>

<br/>

[![GitHub stars](https://img.shields.io/github/stars/gregpr07/browser-use?style=social)](https://github.com/gregpr07/browser-use/stargazers)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)

Enable AI to control your browser 🤖.

Browser use is the easiest way to connect your AI agents with the browser. If you have used Browser Use for your project feel free to show it off in our [Discord](https://link.browser-use.com/discord).

To learn more about the library, check out the [documentation 📕](https://docs.browser-use.com).

# Quick start

With pip:

```bash
pip install browser-use
```

install playwright:

```bash
playwright install
```

Spin up your agent:

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use' in the search bar, click on the first post and return the first comment.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

And don't forget to add your API keys to your `.env` file.

```bash
OPENAI_API_KEY=
```

For other settings, models, and more, check out the [documentation 📕](https://docs.browser-use.com).

### Test with UI

You can test [browser-use with a UI repository](https://github.com/browser-use/web-ui)

Or simply run the gradio example:

```
uv pip install gradio
```

```bash
python examples/gradio_demo.py
```

# Demos

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py): Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.

![Letter to Papa](https://github.com/user-attachments/assets/242ade3e-15bc-41c2-988f-cbc5415a66aa)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/find_and_apply_to_jobs.py): Read my CV & find ML jobs, save them to a file, and then start applying for them in new tabs, if you need help, ask me.'

https://github.com/user-attachments/assets/171fb4d6-0355-46f2-863e-edb04a828d04

<br/><br/>

Prompt: Find flights on kayak.com from Zurich to Beijing from 25.12.2024 to 02.02.2025.

![flight search 8x 10fps](https://github.com/user-attachments/assets/ea605d4a-90e6-481e-a569-f0e0db7e6390)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/custom-functions/save_to_file_hugging_face.py): Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file.

https://github.com/user-attachments/assets/de73ee39-432c-4b97-b4e8-939fd7f323b3

## More examples

For more examples see the [examples](examples) folder or join the [Discord](https://link.browser-use.com/discord) and show off your project.

# Vision

Tell your computer what to do, and it gets it done.

## Roadmap

- [ ] Improve memory management
- [ ] Enhance planning capabilities
- [ ] Improve self-correction
- [ ] Fine-tune the model for better performance
- [ ] Create datasets for complex tasks
- [ ] Sandbox browser-use for specific websites
- [ ] Implement deterministic script rerun with LLM fallback
- [ ] Cloud-hosted version
- [ ] Add stop/pause functionality
- [ ] Improve authentication handling
- [ ] Reduce token consumption
- [ ] Implement long-term memory
- [ ] Handle repetitive tasks reliably
- [ ] Third-party integrations (Slack, etc.)
- [ ] Include more interactive elements
- [ ] Human-in-the-loop execution
- [ ] Benchmark various models against each other
- [ ] Let the user record a workflow and browser-use will execute it
- [ ] Improve the generated GIF quality
- [ ] Create various demos for tutorial execution, job application, QA testing, social media, etc.

## Contributing

We love contributions! Feel free to open issues for bugs or feature requests. To contribute to the docs, check out the `/docs` folder.

## Local Setup

To learn more about the library, check out the [local setup 📕](https://docs.browser-use.com/development/local-setup).

## Cooperations

We are forming a commission to define best practices for UI/UX design for browser agents.
Together, we're exploring how software redesign improves the performance of AI agents and gives these companies a competitive advantage by designing their existing software to be at the forefront of the agent age.

Email [Toby](mailto:tbiddle@loop11.com?subject=I%20want%20to%20join%20the%20UI/UX%20commission%20for%20AI%20agents&body=Hi%20Toby%2C%0A%0AI%20found%20you%20in%20the%20browser-use%20GitHub%20README.%0A%0A) to apply for a seat on the committee.

## Citation

If you use Browser Use in your research or project, please cite:

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```

---

<div align="center">
  Made with ❤️ in Zurich and San Francisco
</div>




================================================
File: LICENSE
================================================
MIT License

Copyright (c) 2024 Gregor Zunic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


================================================
File: SECURITY.md
================================================
## Reporting Security Issues

If you believe you have found a security vulnerability in browser-use, please report it through coordinated disclosure.

**Please do not report security vulnerabilities through the repository issues, discussions, or pull requests.**

Instead, please open a new [Github security advisory](https://github.com/browser-use/browser-use/security/advisories/new).

Please include as much of the information listed below as you can to help me better understand and resolve the issue:

* The type of issue (e.g., buffer overflow, SQL injection, or cross-site scripting)
* Full paths of source file(s) related to the manifestation of the issue
* The location of the affected source code (tag/branch/commit or direct URL)
* Any special configuration required to reproduce the issue
* Step-by-step instructions to reproduce the issue
* Proof-of-concept or exploit code (if possible)
* Impact of the issue, including how an attacker might exploit the issue

This information will help me triage your report more quickly.



================================================
File: conftest.py
================================================
import os
import sys

from browser_use.logging_config import setup_logging

# Get the absolute path to the project root
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

setup_logging()


================================================
File: pyproject.toml
================================================
[project]
name = "browser-use"
description = "Make websites accessible for AI agents"
authors = [
    { name = "Gregor Zunic" }
]
version = "0.1.29"
readme = "README.md"
requires-python = ">=3.11"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "MainContentExtractor>=0.0.4",
    "beautifulsoup4>=4.12.3",
    "httpx>=0.27.2",
    "langchain==0.3.14",
    "langchain-openai==0.3.1",
    "langchain-anthropic==0.3.3",
    "langchain-ollama==0.2.2",
    "langchain-fireworks>=0.2.6",
    "langchain-aws>=0.2.11",
    "langchain-google-genai==2.0.8",
    "pydantic>=2.10.4",
    "python-dotenv>=1.0.1",
    "requests>=2.32.3",
    "posthog>=3.7.0",
    "playwright>=1.49.0",
    "setuptools>=75.8.0",
    "lmnr[langchain]>=0.4.53"
]

[project.optional-dependencies]
dev = [
    "tokencost>=0.1.16",
    "hatch>=1.13.0",
    "build>=1.2.2",
    "pytest>=8.3.3",
    "pytest-asyncio>=0.24.0"
]

[tool.ruff]
line-length = 130
select = ["E", "F", "I"]
fix = true

[tool.ruff.format]
quote-style = "single"
indent-style = "tab"
docstring-code-format = true

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"


================================================
File: pytest.ini
================================================
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests

testpaths =
    tests

python_files =
    test_*.py
    *_test.py

addopts =
    -v
    --strict-markers
    --tb=short

asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
log_cli = true
; log_cli_level = DEBUG
log_cli_format = %(levelname)-8s [%(name)s] %(message)s
filterwarnings =
    ignore::pytest.PytestDeprecationWarning
    ignore::DeprecationWarning

log_level = INFO


================================================
File: .env.example
================================================
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

# Set to false to disable anonymized telemetry
ANONYMIZED_TELEMETRY=true

# LogLevel: Set to debug to enable verbose logging, set to result to get results only. Available: result | debug | info
BROWSER_USE_LOGGING_LEVEL=info


================================================
File: .pre-commit-config.yaml
================================================
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [
            --line-length=130,
            --select=E,F,I,
            --fix,
        ]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml


================================================
File: .python-version
================================================
3.11


================================================
File: browser_use/README.md
================================================
# Codebase Structure

> The code structure inspired by https://github.com/Netflix/dispatch.

Very good structure on how to make a scalable codebase is also in [this repo](https://github.com/zhanymkanov/fastapi-best-practices).

Just a brief document about how we should structure our backend codebase.

## Code Structure

```markdown
src/
/<service name>/
models.py
services.py
prompts.py
views.py
utils.py
routers.py

    	/_<subservice name>/
```

### Service.py

Always a single file, except if it becomes too long - more than ~500 lines, split it into \_subservices

### Views.py

Always split the views into two parts

```python
# All
...

# Requests
...

# Responses
...
```

If too long → split into multiple files

### Prompts.py

Single file; if too long → split into multiple files (one prompt per file or so)

### Routers.py

Never split into more than one file


================================================
File: browser_use/__init__.py
================================================
from browser_use.logging_config import setup_logging

setup_logging()

from browser_use.agent.prompts import SystemPrompt as SystemPrompt
from browser_use.agent.service import Agent as Agent
from browser_use.agent.views import ActionModel as ActionModel
from browser_use.agent.views import ActionResult as ActionResult
from browser_use.agent.views import AgentHistoryList as AgentHistoryList
from browser_use.browser.browser import Browser as Browser
from browser_use.browser.browser import BrowserConfig as BrowserConfig
from browser_use.controller.service import Controller as Controller
from browser_use.dom.service import DomService as DomService

__all__ = [
	'Agent',
	'Browser',
	'BrowserConfig',
	'Controller',
	'DomService',
	'SystemPrompt',
	'ActionResult',
	'ActionModel',
	'AgentHistoryList',
]


================================================
File: browser_use/logging_config.py
================================================
import logging
import os
import sys

from dotenv import load_dotenv

load_dotenv()


def addLoggingLevel(levelName, levelNum, methodName=None):
	"""
	Comprehensively adds a new logging level to the `logging` module and the
	currently configured logging class.

	`levelName` becomes an attribute of the `logging` module with the value
	`levelNum`. `methodName` becomes a convenience method for both `logging`
	itself and the class returned by `logging.getLoggerClass()` (usually just
	`logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
	used.

	To avoid accidental clobberings of existing attributes, this method will
	raise an `AttributeError` if the level name is already an attribute of the
	`logging` module or if the method name is already present

	Example
	-------
	>>> addLoggingLevel('TRACE', logging.DEBUG - 5)
	>>> logging.getLogger(__name__).setLevel('TRACE')
	>>> logging.getLogger(__name__).trace('that worked')
	>>> logging.trace('so did this')
	>>> logging.TRACE
	5

	"""
	if not methodName:
		methodName = levelName.lower()

	if hasattr(logging, levelName):
		raise AttributeError('{} already defined in logging module'.format(levelName))
	if hasattr(logging, methodName):
		raise AttributeError('{} already defined in logging module'.format(methodName))
	if hasattr(logging.getLoggerClass(), methodName):
		raise AttributeError('{} already defined in logger class'.format(methodName))

	# This method was inspired by the answers to Stack Overflow post
	# http://stackoverflow.com/q/2183233/2988730, especially
	# http://stackoverflow.com/a/13638084/2988730
	def logForLevel(self, message, *args, **kwargs):
		if self.isEnabledFor(levelNum):
			self._log(levelNum, message, args, **kwargs)

	def logToRoot(message, *args, **kwargs):
		logging.log(levelNum, message, *args, **kwargs)

	logging.addLevelName(levelNum, levelName)
	setattr(logging, levelName, levelNum)
	setattr(logging.getLoggerClass(), methodName, logForLevel)
	setattr(logging, methodName, logToRoot)


def setup_logging():
	# Try to add RESULT level, but ignore if it already exists
	try:
		addLoggingLevel('RESULT', 35)  # This allows ERROR, FATAL and CRITICAL
	except AttributeError:
		pass  # Level already exists, which is fine

	log_type = os.getenv('BROWSER_USE_LOGGING_LEVEL', 'info').lower()

	# Check if handlers are already set up
	if logging.getLogger().hasHandlers():
		return

	# Clear existing handlers
	root = logging.getLogger()
	root.handlers = []

	class BrowserUseFormatter(logging.Formatter):
		def format(self, record):
			if record.name.startswith('browser_use.'):
				record.name = record.name.split('.')[-2]
			return super().format(record)

	# Setup single handler for all loggers
	console = logging.StreamHandler(sys.stdout)

	# adittional setLevel here to filter logs
	if log_type == 'result':
		console.setLevel('RESULT')
		console.setFormatter(BrowserUseFormatter('%(message)s'))
	else:
		console.setFormatter(BrowserUseFormatter('%(levelname)-8s [%(name)s] %(message)s'))

	# Configure root logger only
	root.addHandler(console)

	# switch cases for log_type
	if log_type == 'result':
		root.setLevel('RESULT')  # string usage to avoid syntax error
	elif log_type == 'debug':
		root.setLevel(logging.DEBUG)
	else:
		root.setLevel(logging.INFO)

	# Configure browser_use logger
	browser_use_logger = logging.getLogger('browser_use')
	browser_use_logger.propagate = False  # Don't propagate to root logger
	browser_use_logger.addHandler(console)
	browser_use_logger.setLevel(root.level)  # Set same level as root logger

	logger = logging.getLogger('browser_use')
	logger.info('BrowserUse logging setup complete with level %s', log_type)
	# Silence third-party loggers
	for logger in [
		'WDM',
		'httpx',
		'selenium',
		'playwright',
		'urllib3',
		'asyncio',
		'langchain',
		'openai',
		'httpcore',
		'charset_normalizer',
		'anthropic._base_client',
		'PIL.PngImagePlugin',
		'trafilatura.htmlprocessing',
		'trafilatura',
	]:
		third_party = logging.getLogger(logger)
		third_party.setLevel(logging.ERROR)
		third_party.propagate = False


================================================
File: browser_use/utils.py
================================================
import logging
import time
from functools import wraps
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

logger = logging.getLogger(__name__)


# Define generic type variables for return type and parameters
R = TypeVar('R')
P = ParamSpec('P')


def time_execution_sync(additional_text: str = '') -> Callable[[Callable[P, R]], Callable[P, R]]:
	def decorator(func: Callable[P, R]) -> Callable[P, R]:
		@wraps(func)
		def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
			start_time = time.time()
			result = func(*args, **kwargs)
			execution_time = time.time() - start_time
			logger.debug(f'{additional_text} Execution time: {execution_time:.2f} seconds')
			return result

		return wrapper

	return decorator


def time_execution_async(
	additional_text: str = '',
) -> Callable[[Callable[P, Coroutine[Any, Any, R]]], Callable[P, Coroutine[Any, Any, R]]]:
	def decorator(func: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
		@wraps(func)
		async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
			start_time = time.time()
			result = await func(*args, **kwargs)
			execution_time = time.time() - start_time
			logger.debug(f'{additional_text} Execution time: {execution_time:.2f} seconds')
			return result

		return wrapper

	return decorator


def singleton(cls):
	instance = [None]

	def wrapper(*args, **kwargs):
		if instance[0] is None:
			instance[0] = cls(*args, **kwargs)
		return instance[0]

	return wrapper


================================================
File: browser_use/agent/prompts.py
================================================
from datetime import datetime
from typing import List, Optional

from langchain_core.messages import HumanMessage, SystemMessage

from browser_use.agent.views import ActionResult, AgentStepInfo
from browser_use.browser.views import BrowserState


class SystemPrompt:
	def __init__(self, action_description: str, current_date: datetime, max_actions_per_step: int = 10):
		self.default_action_description = action_description
		self.current_date = current_date
		self.max_actions_per_step = max_actions_per_step

	def important_rules(self) -> str:
		"""
		Returns the important rules for the agent.
		"""
		text = """
1. RESPONSE FORMAT: You must ALWAYS respond with valid JSON in this exact format:
   {
     "current_state": {
       "evaluation_previous_goal": "Success|Failed|Unknown - Analyze the current elements and the image to check if the previous goals/actions are successful like intended by the task. Ignore the action result. The website is the ground truth. Also mention if something unexpected happened like new suggestions in an input field. Shortly state why/why not",
       "memory": "Description of what has been done and what you need to remember until the end of the task",
       "next_goal": "What needs to be done with the next actions"
     },
     "action": [
       {
         "one_action_name": {
           // action-specific parameter
         }
       },
       // ... more actions in sequence
     ]
   }

2. ACTIONS: You can specify multiple actions in the list to be executed in sequence. But always specify only one action name per item.

   Common action sequences:
   - Form filling: [
       {"input_text": {"index": 1, "text": "username"}},
       {"input_text": {"index": 2, "text": "password"}},
       {"click_element": {"index": 3}}
     ]
   - Navigation and extraction: [
       {"open_new_tab": {}},
       {"go_to_url": {"url": "https://example.com"}},
       {"extract_page_content": {}}
     ]


3. ELEMENT INTERACTION:
   - Only use indexes that exist in the provided element list
   - Each element has a unique index number (e.g., "33[:]<button>")
   - Elements marked with "_[:]" are non-interactive (for context only)

4. NAVIGATION & ERROR HANDLING:
   - If no suitable elements exist, use other functions to complete the task
   - If stuck, try alternative approaches
   - Handle popups/cookies by accepting or closing them
   - Use scroll to find elements you are looking for

5. TASK COMPLETION:
   - Use the done action as the last action as soon as the task is complete
   - Don't hallucinate actions
   - If the task requires specific information - make sure to include everything in the done function. This is what the user will see.
   - If you are running out of steps (current step), think about speeding it up, and ALWAYS use the done action as the last action.

6. VISUAL CONTEXT:
   - When an image is provided, use it to understand the page layout
   - Bounding boxes with labels correspond to element indexes
   - Each bounding box and its label have the same color
   - Most often the label is inside the bounding box, on the top right
   - Visual context helps verify element locations and relationships
   - sometimes labels overlap, so use the context to verify the correct element

7. Form filling:
   - If you fill an input field and your action sequence is interrupted, most often a list with suggestions popped up under the field and you need to first select the right element from the suggestion list.

8. ACTION SEQUENCING:
   - Actions are executed in the order they appear in the list
   - Each action should logically follow from the previous one
   - If the page changes after an action, the sequence is interrupted and you get the new state.
   - If content only disappears the sequence continues.
   - Only provide the action sequence until you think the page will change.
   - Try to be efficient, e.g. fill forms at once, or chain actions where nothing changes on the page like saving, extracting, checkboxes...
   - only use multiple actions if it makes sense.


"""
		text += f'   - use maximum {self.max_actions_per_step} actions per sequence'
		return text

	def input_format(self) -> str:
		return """
INPUT STRUCTURE:
1. Current URL: The webpage you're currently on
2. Available Tabs: List of open browser tabs
3. Interactive Elements: List in the format:
   index[:]<element_type>element_text</element_type>
   - index: Numeric identifier for interaction
   - element_type: HTML element type (button, input, etc.)
   - element_text: Visible text or element description

Example:
33[:]<button>Submit Form</button>
_[:] Non-interactive text


Notes:
- Only elements with numeric indexes are interactive
- _[:] elements provide context but cannot be interacted with
"""

	def get_system_message(self) -> SystemMessage:
		"""
		Get the system prompt for the agent.

		Returns:
		    str: Formatted system prompt
		"""
		time_str = self.current_date.strftime('%Y-%m-%d %H:%M')

		AGENT_PROMPT = f"""You are a precise browser automation agent that interacts with websites through structured commands. Your role is to:
1. Analyze the provided webpage elements and structure
2. Plan a sequence of actions to accomplish the given task
3. Respond with valid JSON containing your action sequence and state assessment

Current date and time: {time_str}

{self.input_format()}

{self.important_rules()}

Functions:
{self.default_action_description}

Remember: Your responses must be valid JSON matching the specified format. Each action in the sequence must be valid."""
		return SystemMessage(content=AGENT_PROMPT)


# Example:
# {self.example_response()}
# Your AVAILABLE ACTIONS:
# {self.default_action_description}


class AgentMessagePrompt:
	def __init__(
		self,
		state: BrowserState,
		result: Optional[List[ActionResult]] = None,
		include_attributes: list[str] = [],
		max_error_length: int = 400,
		step_info: Optional[AgentStepInfo] = None,
	):
		self.state = state
		self.result = result
		self.max_error_length = max_error_length
		self.include_attributes = include_attributes
		self.step_info = step_info

	def get_user_message(self) -> HumanMessage:
		if self.step_info:
			step_info_description = f'Current step: {self.step_info.step_number + 1}/{self.step_info.max_steps}'
		else:
			step_info_description = ''

		elements_text = self.state.element_tree.clickable_elements_to_string(include_attributes=self.include_attributes)

		has_content_above = (self.state.pixels_above or 0) > 0
		has_content_below = (self.state.pixels_below or 0) > 0

		if elements_text != '':
			if has_content_above:
				elements_text = (
					f'... {self.state.pixels_above} pixels above - scroll or extract content to see more ...\n{elements_text}'
				)
			else:
				elements_text = f'[Start of page]\n{elements_text}'
			if has_content_below:
				elements_text = (
					f'{elements_text}\n... {self.state.pixels_below} pixels below - scroll or extract content to see more ...'
				)
			else:
				elements_text = f'{elements_text}\n[End of page]'
		else:
			elements_text = 'empty page'

		state_description = f"""
{step_info_description}
Current url: {self.state.url}
Available tabs:
{self.state.tabs}
Interactive elements from current page view:
{elements_text}
"""

		if self.result:
			for i, result in enumerate(self.result):
				if result.extracted_content:
					state_description += f'\nAction result {i + 1}/{len(self.result)}: {result.extracted_content}'
				if result.error:
					# only use last 300 characters of error
					error = result.error[-self.max_error_length :]
					state_description += f'\nAction error {i + 1}/{len(self.result)}: ...{error}'

		if self.state.screenshot:
			# Format message for vision model
			return HumanMessage(
				content=[
					{'type': 'text', 'text': state_description},
					{
						'type': 'image_url',
						'image_url': {'url': f'data:image/png;base64,{self.state.screenshot}'},
					},
				]
			)

		return HumanMessage(content=state_description)


================================================
File: browser_use/agent/service.py
================================================
from __future__ import annotations

import asyncio
import base64
import io
import json
import logging
import os
import platform
import textwrap
import uuid
from io import BytesIO
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
	BaseMessage,
	SystemMessage,
)
from lmnr import observe
from openai import RateLimitError
from PIL import Image, ImageDraw, ImageFont
from pydantic import BaseModel, ValidationError

from browser_use.agent.message_manager.service import MessageManager
from browser_use.agent.prompts import AgentMessagePrompt, SystemPrompt
from browser_use.agent.views import (
	ActionResult,
	AgentError,
	AgentHistory,
	AgentHistoryList,
	AgentOutput,
	AgentStepInfo,
)
from browser_use.browser.browser import Browser
from browser_use.browser.context import BrowserContext
from browser_use.browser.views import BrowserState, BrowserStateHistory
from browser_use.controller.registry.views import ActionModel
from browser_use.controller.service import Controller
from browser_use.dom.history_tree_processor.service import (
	DOMHistoryElement,
	HistoryTreeProcessor,
)
from browser_use.telemetry.service import ProductTelemetry
from browser_use.telemetry.views import (
	AgentEndTelemetryEvent,
	AgentRunTelemetryEvent,
	AgentStepTelemetryEvent,
)
from browser_use.utils import time_execution_async

load_dotenv()
logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)


class Agent:
	def __init__(
		self,
		task: str,
		llm: BaseChatModel,
		browser: Browser | None = None,
		browser_context: BrowserContext | None = None,
		controller: Controller = Controller(),
		use_vision: bool = True,
		save_conversation_path: Optional[str] = None,
		save_conversation_path_encoding: Optional[str] = 'utf-8',
		max_failures: int = 3,
		retry_delay: int = 10,
		system_prompt_class: Type[SystemPrompt] = SystemPrompt,
		max_input_tokens: int = 128000,
		validate_output: bool = False,
		message_context: Optional[str] = None,
		generate_gif: bool | str = True,
		include_attributes: list[str] = [
			'title',
			'type',
			'name',
			'role',
			'tabindex',
			'aria-label',
			'placeholder',
			'value',
			'alt',
			'aria-expanded',
		],
		max_error_length: int = 400,
		max_actions_per_step: int = 10,
		tool_call_in_content: bool = True,
		initial_actions: Optional[List[Dict[str, Dict[str, Any]]]] = None,
		# Cloud Callbacks
		register_new_step_callback: Callable[['BrowserState', 'AgentOutput', int], None] | None = None,
		register_done_callback: Callable[['AgentHistoryList'], None] | None = None,
		tool_calling_method: Optional[str] = 'auto',
	):
		self.agent_id = str(uuid.uuid4())  # unique identifier for the agent

		self.task = task
		self.use_vision = use_vision
		self.llm = llm
		self.save_conversation_path = save_conversation_path
		self.save_conversation_path_encoding = save_conversation_path_encoding
		self._last_result = None
		self.include_attributes = include_attributes
		self.max_error_length = max_error_length
		self.generate_gif = generate_gif

		# Controller setup
		self.controller = controller
		self.max_actions_per_step = max_actions_per_step

		# Browser setup
		self.injected_browser = browser is not None
		self.injected_browser_context = browser_context is not None
		self.message_context = message_context

		# Initialize browser first if needed
		self.browser = browser if browser is not None else (None if browser_context else Browser())

		# Initialize browser context
		if browser_context:
			self.browser_context = browser_context
		elif self.browser:
			self.browser_context = BrowserContext(browser=self.browser, config=self.browser.config.new_context_config)
		else:
			# If neither is provided, create both new
			self.browser = Browser()
			self.browser_context = BrowserContext(browser=self.browser)

		self.system_prompt_class = system_prompt_class

		# Telemetry setup
		self.telemetry = ProductTelemetry()

		# Action and output models setup
		self._setup_action_models()
		self._set_version_and_source()
		self.max_input_tokens = max_input_tokens

		self._set_model_names()

		self.tool_calling_method = self.set_tool_calling_method(tool_calling_method)

		self.message_manager = MessageManager(
			llm=self.llm,
			task=self.task,
			action_descriptions=self.controller.registry.get_prompt_description(),
			system_prompt_class=self.system_prompt_class,
			max_input_tokens=self.max_input_tokens,
			include_attributes=self.include_attributes,
			max_error_length=self.max_error_length,
			max_actions_per_step=self.max_actions_per_step,
			message_context=self.message_context,
		)

		# Step callback
		self.register_new_step_callback = register_new_step_callback
		self.register_done_callback = register_done_callback

		# Tracking variables
		self.history: AgentHistoryList = AgentHistoryList(history=[])
		self.n_steps = 1
		self.consecutive_failures = 0
		self.max_failures = max_failures
		self.retry_delay = retry_delay
		self.validate_output = validate_output
		self.initial_actions = self._convert_initial_actions(initial_actions) if initial_actions else None
		if save_conversation_path:
			logger.info(f'Saving conversation to {save_conversation_path}')

		self._paused = False
		self._stopped = False

	def _set_version_and_source(self) -> None:
		try:
			import pkg_resources

			version = pkg_resources.get_distribution('browser-use').version
			source = 'pip'
		except Exception:
			try:
				import subprocess

				version = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()
				source = 'git'
			except Exception:
				version = 'unknown'
				source = 'unknown'
		logger.debug(f'Version: {version}, Source: {source}')
		self.version = version
		self.source = source

	def _set_model_names(self) -> None:
		self.chat_model_library = self.llm.__class__.__name__
		if hasattr(self.llm, 'model_name'):
			self.model_name = self.llm.model_name  # type: ignore
		elif hasattr(self.llm, 'model'):
			self.model_name = self.llm.model  # type: ignore
		else:
			self.model_name = 'Unknown'

	def _setup_action_models(self) -> None:
		"""Setup dynamic action models from controller's registry"""
		# Get the dynamic action model from controller's registry
		self.ActionModel = self.controller.registry.create_action_model()
		# Create output model with the dynamic actions
		self.AgentOutput = AgentOutput.type_with_custom_actions(self.ActionModel)

	def set_tool_calling_method(self, tool_calling_method: Optional[str]) -> Optional[str]:
		if tool_calling_method == 'auto':
			if self.chat_model_library == 'ChatGoogleGenerativeAI':
				return None
			elif self.chat_model_library == 'ChatOpenAI':
				return 'function_calling'
			elif self.chat_model_library == 'AzureChatOpenAI':
				return 'function_calling'
			else:
				return None
		else:
			return tool_calling_method

	def add_new_task(self, new_task: str) -> None:
		self.message_manager.add_new_task(new_task)

	@time_execution_async('--step')
	async def step(self, step_info: Optional[AgentStepInfo] = None) -> None:
		"""Execute one step of the task"""
		logger.info(f'📍 Step {self.n_steps}')
		state = None
		model_output = None
		result: list[ActionResult] = []

		try:
			state = await self.browser_context.get_state(use_vision=self.use_vision)

			if self._stopped or self._paused:
				logger.debug('Agent paused after getting state')
				raise InterruptedError

			self.message_manager.add_state_message(state, self._last_result, step_info)
			input_messages = self.message_manager.get_messages()

			try:
				model_output = await self.get_next_action(input_messages)

				if self.register_new_step_callback:
					self.register_new_step_callback(state, model_output, self.n_steps)

				self._save_conversation(input_messages, model_output)
				self.message_manager._remove_last_state_message()  # we dont want the whole state in the chat history

				if self._stopped or self._paused:
					logger.debug('Agent paused after getting next action')
					raise InterruptedError

				self.message_manager.add_model_output(model_output)
			except Exception as e:
				# model call failed, remove last state message from history
				self.message_manager._remove_last_state_message()
				raise e

			result: list[ActionResult] = await self.controller.multi_act(model_output.action, self.browser_context)
			self._last_result = result

			if len(result) > 0 and result[-1].is_done:
				logger.info(f'📄 Result: {result[-1].extracted_content}')

			self.consecutive_failures = 0

		except InterruptedError:
			logger.debug('Agent paused')
			return
		except Exception as e:
			result = await self._handle_step_error(e)
			self._last_result = result

		finally:
			actions = [a.model_dump(exclude_unset=True) for a in model_output.action] if model_output else []
			self.telemetry.capture(
				AgentStepTelemetryEvent(
					agent_id=self.agent_id,
					step=self.n_steps,
					actions=actions,
					consecutive_failures=self.consecutive_failures,
					step_error=[r.error for r in result if r.error] if result else ['No result'],
				)
			)
			if not result:
				return

			if state:
				self._make_history_item(model_output, state, result)

	async def _handle_step_error(self, error: Exception) -> list[ActionResult]:
		"""Handle all types of errors that can occur during a step"""
		include_trace = logger.isEnabledFor(logging.DEBUG)
		error_msg = AgentError.format_error(error, include_trace=include_trace)
		prefix = f'❌ Result failed {self.consecutive_failures + 1}/{self.max_failures} times:\n '

		if isinstance(error, (ValidationError, ValueError)):
			logger.error(f'{prefix}{error_msg}')
			if 'Max token limit reached' in error_msg:
				# cut tokens from history
				self.message_manager.max_input_tokens = self.max_input_tokens - 500
				logger.info(f'Cutting tokens from history - new max input tokens: {self.message_manager.max_input_tokens}')
				self.message_manager.cut_messages()
			elif 'Could not parse response' in error_msg:
				# give model a hint how output should look like
				error_msg += '\n\nReturn a valid JSON object with the required fields.'

			self.consecutive_failures += 1
		elif isinstance(error, RateLimitError):
			logger.warning(f'{prefix}{error_msg}')
			await asyncio.sleep(self.retry_delay)
			self.consecutive_failures += 1
		else:
			logger.error(f'{prefix}{error_msg}')
			self.consecutive_failures += 1

		return [ActionResult(error=error_msg, include_in_memory=True)]

	def _make_history_item(
		self,
		model_output: AgentOutput | None,
		state: BrowserState,
		result: list[ActionResult],
	) -> None:
		"""Create and store history item"""
		interacted_element = None
		len_result = len(result)

		if model_output:
			interacted_elements = AgentHistory.get_interacted_element(model_output, state.selector_map)
		else:
			interacted_elements = [None]

		state_history = BrowserStateHistory(
			url=state.url,
			title=state.title,
			tabs=state.tabs,
			interacted_element=interacted_elements,
			screenshot=state.screenshot,
		)

		history_item = AgentHistory(model_output=model_output, result=result, state=state_history)

		self.history.history.append(history_item)

	@time_execution_async('--get_next_action')
	async def get_next_action(self, input_messages: list[BaseMessage]) -> AgentOutput:
		"""Get next action from LLM based on current state"""

		if self.model_name == 'deepseek-reasoner':
			converted_input_messages = self.message_manager.convert_messages_for_non_function_calling_models(input_messages)
			merged_input_messages = self.message_manager.merge_successive_human_messages(converted_input_messages)
			output = self.llm.invoke(merged_input_messages)
			# TODO: currently invoke does not return reasoning_content, we should override invoke
			try:
				parsed_json = self.message_manager.extract_json_from_model_output(output.content)
				parsed = self.AgentOutput(**parsed_json)
			except (ValueError, ValidationError) as e:
				logger.warning(f'Failed to parse model output: {str(e)}')
				raise ValueError('Could not parse response.')
		elif self.tool_calling_method is None:
			structured_llm = self.llm.with_structured_output(self.AgentOutput, include_raw=True)
			response: dict[str, Any] = await structured_llm.ainvoke(input_messages)  # type: ignore
			parsed: AgentOutput | None = response['parsed']
		else:
			structured_llm = self.llm.with_structured_output(self.AgentOutput, include_raw=True, method=self.tool_calling_method)
			response: dict[str, Any] = await structured_llm.ainvoke(input_messages)  # type: ignore
			parsed: AgentOutput | None = response['parsed']

		if parsed is None:
			raise ValueError('Could not parse response.')

		# cut the number of actions to max_actions_per_step
		parsed.action = parsed.action[: self.max_actions_per_step]
		self._log_response(parsed)
		self.n_steps += 1

		return parsed

	def _log_response(self, response: AgentOutput) -> None:
		"""Log the model's response"""
		if 'Success' in response.current_state.evaluation_previous_goal:
			emoji = '👍'
		elif 'Failed' in response.current_state.evaluation_previous_goal:
			emoji = '⚠'
		else:
			emoji = '🤷'

		logger.info(f'{emoji} Eval: {response.current_state.evaluation_previous_goal}')
		logger.info(f'🧠 Memory: {response.current_state.memory}')
		logger.info(f'🎯 Next goal: {response.current_state.next_goal}')
		for i, action in enumerate(response.action):
			logger.info(f'🛠️  Action {i + 1}/{len(response.action)}: {action.model_dump_json(exclude_unset=True)}')

	def _save_conversation(self, input_messages: list[BaseMessage], response: Any) -> None:
		"""Save conversation history to file if path is specified"""
		if not self.save_conversation_path:
			return

		# create folders if not exists
		os.makedirs(os.path.dirname(self.save_conversation_path), exist_ok=True)

		with open(
			self.save_conversation_path + f'_{self.n_steps}.txt',
			'w',
			encoding=self.save_conversation_path_encoding,
		) as f:
			self._write_messages_to_file(f, input_messages)
			self._write_response_to_file(f, response)

	def _write_messages_to_file(self, f: Any, messages: list[BaseMessage]) -> None:
		"""Write messages to conversation file"""
		for message in messages:
			f.write(f' {message.__class__.__name__} \n')

			if isinstance(message.content, list):
				for item in message.content:
					if isinstance(item, dict) and item.get('type') == 'text':
						f.write(item['text'].strip() + '\n')
			elif isinstance(message.content, str):
				try:
					content = json.loads(message.content)
					f.write(json.dumps(content, indent=2) + '\n')
				except json.JSONDecodeError:
					f.write(message.content.strip() + '\n')

			f.write('\n')

	def _write_response_to_file(self, f: Any, response: Any) -> None:
		"""Write model response to conversation file"""
		f.write(' RESPONSE\n')
		f.write(json.dumps(json.loads(response.model_dump_json(exclude_unset=True)), indent=2))

	def _log_agent_run(self) -> None:
		"""Log the agent run"""
		logger.info(f'🚀 Starting task: {self.task}')

		logger.debug(f'Version: {self.version}, Source: {self.source}')
		self.telemetry.capture(
			AgentRunTelemetryEvent(
				agent_id=self.agent_id,
				use_vision=self.use_vision,
				task=self.task,
				model_name=self.model_name,
				chat_model_library=self.chat_model_library,
				version=self.version,
				source=self.source,
			)
		)

	@observe(name='agent.run')
	async def run(self, max_steps: int = 100) -> AgentHistoryList:
		"""Execute the task with maximum number of steps"""
		try:
			self._log_agent_run()

			# Execute initial actions if provided
			if self.initial_actions:
				result = await self.controller.multi_act(self.initial_actions, self.browser_context, check_for_new_elements=False)
				self._last_result = result

			for step in range(max_steps):
				if self._too_many_failures():
					break

				# Check control flags before each step
				if not await self._handle_control_flags():
					break

				await self.step()

				if self.history.is_done():
					if self.validate_output and step < max_steps - 1:
						if not await self._validate_output():
							continue

					logger.info('✅ Task completed successfully')
					if self.register_done_callback:
						self.register_done_callback(self.history)
					break
			else:
				logger.info('❌ Failed to complete task in maximum steps')

			return self.history
		finally:
			self.telemetry.capture(
				AgentEndTelemetryEvent(
					agent_id=self.agent_id,
					success=self.history.is_done(),
					steps=self.n_steps,
					max_steps_reached=self.n_steps >= max_steps,
					errors=self.history.errors(),
				)
			)

			if not self.injected_browser_context:
				await self.browser_context.close()

			if not self.injected_browser and self.browser:
				await self.browser.close()

			if self.generate_gif:
				output_path: str = 'agent_history.gif'
				if isinstance(self.generate_gif, str):
					output_path = self.generate_gif

				self.create_history_gif(output_path=output_path)

	def _too_many_failures(self) -> bool:
		"""Check if we should stop due to too many failures"""
		if self.consecutive_failures >= self.max_failures:
			logger.error(f'❌ Stopping due to {self.max_failures} consecutive failures')
			return True
		return False

	async def _handle_control_flags(self) -> bool:
		"""Handle pause and stop flags. Returns True if execution should continue."""
		if self._stopped:
			logger.info('Agent stopped')
			return False

		while self._paused:
			await asyncio.sleep(0.2)  # Small delay to prevent CPU spinning
			if self._stopped:  # Allow stopping while paused
				return False
		return True

	async def _validate_output(self) -> bool:
		"""Validate the output of the last action is what the user wanted"""
		system_msg = (
			f'You are a validator of an agent who interacts with a browser. '
			f'Validate if the output of last action is what the user wanted and if the task is completed. '
			f'If the task is unclear defined, you can let it pass. But if something is missing or the image does not show what was requested dont let it pass. '
			f'Try to understand the page and help the model with suggestions like scroll, do x, ... to get the solution right. '
			f'Task to validate: {self.task}. Return a JSON object with 2 keys: is_valid and reason. '
			f'is_valid is a boolean that indicates if the output is correct. '
			f'reason is a string that explains why it is valid or not.'
			f' example: {{"is_valid": false, "reason": "The user wanted to search for "cat photos", but the agent searched for "dog photos" instead."}}'
		)

		if self.browser_context.session:
			state = await self.browser_context.get_state(use_vision=self.use_vision)
			content = AgentMessagePrompt(
				state=state,
				result=self._last_result,
				include_attributes=self.include_attributes,
				max_error_length=self.max_error_length,
			)
			msg = [SystemMessage(content=system_msg), content.get_user_message()]
		else:
			# if no browser session, we can't validate the output
			return True

		class ValidationResult(BaseModel):
			is_valid: bool
			reason: str

		validator = self.llm.with_structured_output(ValidationResult, include_raw=True)
		response: dict[str, Any] = await validator.ainvoke(msg)  # type: ignore
		parsed: ValidationResult = response['parsed']
		is_valid = parsed.is_valid
		if not is_valid:
			logger.info(f'❌ Validator decision: {parsed.reason}')
			msg = f'The output is not yet correct. {parsed.reason}.'
			self._last_result = [ActionResult(extracted_content=msg, include_in_memory=True)]
		else:
			logger.info(f'✅ Validator decision: {parsed.reason}')
		return is_valid

	async def rerun_history(
		self,
		history: AgentHistoryList,
		max_retries: int = 3,
		skip_failures: bool = True,
		delay_between_actions: float = 2.0,
	) -> list[ActionResult]:
		"""
		Rerun a saved history of actions with error handling and retry logic.

		Args:
		        history: The history to replay
		        max_retries: Maximum number of retries per action
		        skip_failures: Whether to skip failed actions or stop execution
		        delay_between_actions: Delay between actions in seconds

		Returns:
		        List of action results
		"""
		results = []

		for i, history_item in enumerate(history.history):
			goal = history_item.model_output.current_state.next_goal if history_item.model_output else ''
			logger.info(f'Replaying step {i + 1}/{len(history.history)}: goal: {goal}')

			if (
				not history_item.model_output
				or not history_item.model_output.action
				or history_item.model_output.action == [None]
			):
				logger.warning(f'Step {i + 1}: No action to replay, skipping')
				results.append(ActionResult(error='No action to replay'))
				continue

			retry_count = 0
			while retry_count < max_retries:
				try:
					result = await self._execute_history_step(history_item, delay_between_actions)
					results.extend(result)
					break

				except Exception as e:
					retry_count += 1
					if retry_count == max_retries:
						error_msg = f'Step {i + 1} failed after {max_retries} attempts: {str(e)}'
						logger.error(error_msg)
						if not skip_failures:
							results.append(ActionResult(error=error_msg))
							raise RuntimeError(error_msg)
					else:
						logger.warning(f'Step {i + 1} failed (attempt {retry_count}/{max_retries}), retrying...')
						await asyncio.sleep(delay_between_actions)

		return results

	async def _execute_history_step(self, history_item: AgentHistory, delay: float) -> list[ActionResult]:
		"""Execute a single step from history with element validation"""

		state = await self.browser_context.get_state()
		if not state or not history_item.model_output:
			raise ValueError('Invalid state or model output')
		updated_actions = []
		for i, action in enumerate(history_item.model_output.action):
			updated_action = await self._update_action_indices(
				history_item.state.interacted_element[i],
				action,
				state,
			)
			updated_actions.append(updated_action)

			if updated_action is None:
				raise ValueError(f'Could not find matching element {i} in current page')

		result = await self.controller.multi_act(updated_actions, self.browser_context)

		await asyncio.sleep(delay)
		return result

	async def _update_action_indices(
		self,
		historical_element: Optional[DOMHistoryElement],
		action: ActionModel,  # Type this properly based on your action model
		current_state: BrowserState,
	) -> Optional[ActionModel]:
		"""
		Update action indices based on current page state.
		Returns updated action or None if element cannot be found.
		"""
		if not historical_element or not current_state.element_tree:
			return action

		current_element = HistoryTreeProcessor.find_history_element_in_tree(historical_element, current_state.element_tree)

		if not current_element or current_element.highlight_index is None:
			return None

		old_index = action.get_index()
		if old_index != current_element.highlight_index:
			action.set_index(current_element.highlight_index)
			logger.info(f'Element moved in DOM, updated index from {old_index} to {current_element.highlight_index}')

		return action

	async def load_and_rerun(self, history_file: Optional[str | Path] = None, **kwargs) -> list[ActionResult]:
		"""
		Load history from file and rerun it.

		Args:
		        history_file: Path to the history file
		        **kwargs: Additional arguments passed to rerun_history
		"""
		if not history_file:
			history_file = 'AgentHistory.json'
		history = AgentHistoryList.load_from_file(history_file, self.AgentOutput)
		return await self.rerun_history(history, **kwargs)

	def save_history(self, file_path: Optional[str | Path] = None) -> None:
		"""Save the history to a file"""
		if not file_path:
			file_path = 'AgentHistory.json'
		self.history.save_to_file(file_path)

	def create_history_gif(
		self,
		output_path: str = 'agent_history.gif',
		duration: int = 3000,
		show_goals: bool = True,
		show_task: bool = True,
		show_logo: bool = False,
		font_size: int = 40,
		title_font_size: int = 56,
		goal_font_size: int = 44,
		margin: int = 40,
		line_spacing: float = 1.5,
	) -> None:
		"""Create a GIF from the agent's history with overlaid task and goal text."""
		if not self.history.history:
			logger.warning('No history to create GIF from')
			return

		images = []
		# if history is empty or first screenshot is None, we can't create a gif
		if not self.history.history or not self.history.history[0].state.screenshot:
			logger.warning('No history or first screenshot to create GIF from')
			return

		# Try to load nicer fonts
		try:
			# Try different font options in order of preference
			font_options = ['Helvetica', 'Arial', 'DejaVuSans', 'Verdana']
			font_loaded = False

			for font_name in font_options:
				try:
					if platform.system() == 'Windows':
						# Need to specify the abs font path on Windows
						font_name = os.path.join(os.getenv('WIN_FONT_DIR', 'C:\\Windows\\Fonts'), font_name + '.ttf')
					regular_font = ImageFont.truetype(font_name, font_size)
					title_font = ImageFont.truetype(font_name, title_font_size)
					goal_font = ImageFont.truetype(font_name, goal_font_size)
					font_loaded = True
					break
				except OSError:
					continue

			if not font_loaded:
				raise OSError('No preferred fonts found')

		except OSError:
			regular_font = ImageFont.load_default()
			title_font = ImageFont.load_default()

			goal_font = regular_font

		# Load logo if requested
		logo = None
		if show_logo:
			try:
				logo = Image.open('./static/browser-use.png')
				# Resize logo to be small (e.g., 40px height)
				logo_height = 150
				aspect_ratio = logo.width / logo.height
				logo_width = int(logo_height * aspect_ratio)
				logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
			except Exception as e:
				logger.warning(f'Could not load logo: {e}')

		# Create task frame if requested
		if show_task and self.task:
			task_frame = self._create_task_frame(
				self.task,
				self.history.history[0].state.screenshot,
				title_font,
				regular_font,
				logo,
				line_spacing,
			)
			images.append(task_frame)

		# Process each history item
		for i, item in enumerate(self.history.history, 1):
			if not item.state.screenshot:
				continue

			# Convert base64 screenshot to PIL Image
			img_data = base64.b64decode(item.state.screenshot)
			image = Image.open(io.BytesIO(img_data))

			if show_goals and item.model_output:
				image = self._add_overlay_to_image(
					image=image,
					step_number=i,
					goal_text=item.model_output.current_state.next_goal,
					regular_font=regular_font,
					title_font=title_font,
					margin=margin,
					logo=logo,
				)

			images.append(image)

		if images:
			# Save the GIF
			images[0].save(
				output_path,
				save_all=True,
				append_images=images[1:],
				duration=duration,
				loop=0,
				optimize=False,
			)
			logger.info(f'Created GIF at {output_path}')
		else:
			logger.warning('No images found in history to create GIF')

	def _create_task_frame(
		self,
		task: str,
		first_screenshot: str,
		title_font: ImageFont.FreeTypeFont,
		regular_font: ImageFont.FreeTypeFont,
		logo: Optional[Image.Image] = None,
		line_spacing: float = 1.5,
	) -> Image.Image:
		"""Create initial frame showing the task."""
		img_data = base64.b64decode(first_screenshot)
		template = Image.open(io.BytesIO(img_data))
		image = Image.new('RGB', template.size, (0, 0, 0))
		draw = ImageDraw.Draw(image)

		# Calculate vertical center of image
		center_y = image.height // 2

		# Draw task text with increased font size
		margin = 140  # Increased margin
		max_width = image.width - (2 * margin)
		larger_font = ImageFont.truetype(regular_font.path, regular_font.size + 16)  # Increase font size more
		wrapped_text = self._wrap_text(task, larger_font, max_width)

		# Calculate line height with spacing
		line_height = larger_font.size * line_spacing

		# Split text into lines and draw with custom spacing
		lines = wrapped_text.split('\n')
		total_height = line_height * len(lines)

		# Start position for first line
		text_y = center_y - (total_height / 2) + 50  # Shifted down slightly

		for line in lines:
			# Get line width for centering
			line_bbox = draw.textbbox((0, 0), line, font=larger_font)
			text_x = (image.width - (line_bbox[2] - line_bbox[0])) // 2

			draw.text(
				(text_x, text_y),
				line,
				font=larger_font,
				fill=(255, 255, 255),
			)
			text_y += line_height

		# Add logo if provided (top right corner)
		if logo:
			logo_margin = 20
			logo_x = image.width - logo.width - logo_margin
			image.paste(logo, (logo_x, logo_margin), logo if logo.mode == 'RGBA' else None)

		return image

	def _add_overlay_to_image(
		self,
		image: Image.Image,
		step_number: int,
		goal_text: str,
		regular_font: ImageFont.FreeTypeFont,
		title_font: ImageFont.FreeTypeFont,
		margin: int,
		logo: Optional[Image.Image] = None,
		display_step: bool = True,
		text_color: tuple[int, int, int, int] = (255, 255, 255, 255),
		text_box_color: tuple[int, int, int, int] = (0, 0, 0, 255),
	) -> Image.Image:
		"""Add step number and goal overlay to an image."""
		image = image.convert('RGBA')
		txt_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
		draw = ImageDraw.Draw(txt_layer)
		if display_step:
			# Add step number (bottom left)
			step_text = str(step_number)
			step_bbox = draw.textbbox((0, 0), step_text, font=title_font)
			step_width = step_bbox[2] - step_bbox[0]
			step_height = step_bbox[3] - step_bbox[1]

			# Position step number in bottom left
			x_step = margin + 10  # Slight additional offset from edge
			y_step = image.height - margin - step_height - 10  # Slight offset from bottom

			# Draw rounded rectangle background for step number
			padding = 20  # Increased padding
			step_bg_bbox = (
				x_step - padding,
				y_step - padding,
				x_step + step_width + padding,
				y_step + step_height + padding,
			)
			draw.rounded_rectangle(
				step_bg_bbox,
				radius=15,  # Add rounded corners
				fill=text_box_color,
			)

			# Draw step number
			draw.text(
				(x_step, y_step),
				step_text,
				font=title_font,
				fill=text_color,
			)

		# Draw goal text (centered, bottom)
		max_width = image.width - (4 * margin)
		wrapped_goal = self._wrap_text(goal_text, title_font, max_width)
		goal_bbox = draw.multiline_textbbox((0, 0), wrapped_goal, font=title_font)
		goal_width = goal_bbox[2] - goal_bbox[0]
		goal_height = goal_bbox[3] - goal_bbox[1]

		# Center goal text horizontally, place above step number
		x_goal = (image.width - goal_width) // 2
		y_goal = y_step - goal_height - padding * 4  # More space between step and goal

		# Draw rounded rectangle background for goal
		padding_goal = 25  # Increased padding for goal
		goal_bg_bbox = (
			x_goal - padding_goal,  # Remove extra space for logo
			y_goal - padding_goal,
			x_goal + goal_width + padding_goal,
			y_goal + goal_height + padding_goal,
		)
		draw.rounded_rectangle(
			goal_bg_bbox,
			radius=15,  # Add rounded corners
			fill=text_box_color,
		)

		# Draw goal text
		draw.multiline_text(
			(x_goal, y_goal),
			wrapped_goal,
			font=title_font,
			fill=text_color,
			align='center',
		)

		# Add logo if provided (top right corner)
		if logo:
			logo_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
			logo_margin = 20
			logo_x = image.width - logo.width - logo_margin
			logo_layer.paste(logo, (logo_x, logo_margin), logo if logo.mode == 'RGBA' else None)
			txt_layer = Image.alpha_composite(logo_layer, txt_layer)

		# Composite and convert
		result = Image.alpha_composite(image, txt_layer)
		return result.convert('RGB')

	def _wrap_text(self, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> str:
		"""
		Wrap text to fit within a given width.

		Args:
			text: Text to wrap
			font: Font to use for text
			max_width: Maximum width in pixels

		Returns:
			Wrapped text with newlines
		"""
		words = text.split()
		lines = []
		current_line = []

		for word in words:
			current_line.append(word)
			line = ' '.join(current_line)
			bbox = font.getbbox(line)
			if bbox[2] > max_width:
				if len(current_line) == 1:
					lines.append(current_line.pop())
				else:
					current_line.pop()
					lines.append(' '.join(current_line))
					current_line = [word]

		if current_line:
			lines.append(' '.join(current_line))

		return '\n'.join(lines)

	def _create_frame(self, screenshot: str, text: str, step_number: int, width: int = 1200, height: int = 800) -> Image.Image:
		"""Create a frame for the GIF with improved styling"""

		# Create base image
		frame = Image.new('RGB', (width, height), 'white')

		# Load and resize screenshot
		screenshot_img = Image.open(BytesIO(base64.b64decode(screenshot)))
		screenshot_img.thumbnail((width - 40, height - 160))  # Leave space for text

		# Calculate positions
		screenshot_x = (width - screenshot_img.width) // 2
		screenshot_y = 120  # Leave space for header

		# Draw screenshot
		frame.paste(screenshot_img, (screenshot_x, screenshot_y))

		# Load browser-use logo
		logo_size = 100  # Increased size for browser-use logo
		logo_path = os.path.join(os.path.dirname(__file__), 'assets/browser-use-logo.png')
		if os.path.exists(logo_path):
			logo = Image.open(logo_path)
			logo.thumbnail((logo_size, logo_size))
			frame.paste(logo, (width - logo_size - 20, 20), logo if 'A' in logo.getbands() else None)

		# Create drawing context
		draw = ImageDraw.Draw(frame)

		# Load fonts
		try:
			title_font = ImageFont.truetype('Arial.ttf', 36)  # Increased font size
			text_font = ImageFont.truetype('Arial.ttf', 24)  # Increased font size
			number_font = ImageFont.truetype('Arial.ttf', 48)  # Increased font size for step number
		except:
			title_font = ImageFont.load_default()
			text_font = ImageFont.load_default()
			number_font = ImageFont.load_default()

		# Draw task text with increased spacing
		margin = 80  # Increased margin
		max_text_width = width - (2 * margin)

		# Create rounded rectangle for goal text
		text_padding = 20
		text_lines = textwrap.wrap(text, width=60)
		text_height = sum(draw.textsize(line, font=text_font)[1] for line in text_lines)
		text_box_height = text_height + (2 * text_padding)

		# Draw rounded rectangle background for goal
		goal_bg_coords = [
			margin - text_padding,
			40,  # Top position
			width - margin + text_padding,
			40 + text_box_height,
		]
		draw.rounded_rectangle(
			goal_bg_coords,
			radius=15,  # Increased radius for more rounded corners
			fill='#f0f0f0',
		)

		# Draw browser-use small logo in top left of goal box
		small_logo_size = 30
		if os.path.exists(logo_path):
			small_logo = Image.open(logo_path)
			small_logo.thumbnail((small_logo_size, small_logo_size))
			frame.paste(
				small_logo,
				(margin - text_padding + 10, 45),  # Positioned inside goal box
				small_logo if 'A' in small_logo.getbands() else None,
			)

		# Draw text with proper wrapping
		y = 50  # Starting y position for text
		for line in text_lines:
			draw.text((margin + small_logo_size + 20, y), line, font=text_font, fill='black')
			y += draw.textsize(line, font=text_font)[1] + 5

		# Draw step number with rounded background
		number_text = str(step_number)
		number_size = draw.textsize(number_text, font=number_font)
		number_padding = 20
		number_box_width = number_size[0] + (2 * number_padding)
		number_box_height = number_size[1] + (2 * number_padding)

		# Draw rounded rectangle for step number
		number_bg_coords = [
			20,  # Left position
			height - number_box_height - 20,  # Bottom position
			20 + number_box_width,
			height - 20,
		]
		draw.rounded_rectangle(
			number_bg_coords,
			radius=15,
			fill='#007AFF',  # Blue background
		)

		# Center number in its background
		number_x = number_bg_coords[0] + ((number_box_width - number_size[0]) // 2)
		number_y = number_bg_coords[1] + ((number_box_height - number_size[1]) // 2)
		draw.text((number_x, number_y), number_text, font=number_font, fill='white')

		return frame

	def pause(self) -> None:
		"""Pause the agent before the next step"""
		logger.info('🔄 pausing Agent ')
		self._paused = True

	def resume(self) -> None:
		"""Resume the agent"""
		logger.info('▶️ Agent resuming')
		self._paused = False

	def stop(self) -> None:
		"""Stop the agent"""
		logger.info('⏹️ Agent stopping')
		self._stopped = True

	def _convert_initial_actions(self, actions: List[Dict[str, Dict[str, Any]]]) -> List[ActionModel]:
		"""Convert dictionary-based actions to ActionModel instances"""
		converted_actions = []
		action_model = self.ActionModel
		for action_dict in actions:
			# Each action_dict should have a single key-value pair
			action_name = next(iter(action_dict))
			params = action_dict[action_name]

			# Get the parameter model for this action from registry
			action_info = self.controller.registry.registry.actions[action_name]
			param_model = action_info.param_model

			# Create validated parameters using the appropriate param model
			validated_params = param_model(**params)

			# Create ActionModel instance with the validated parameters
			action_model = self.ActionModel(**{action_name: validated_params})
			converted_actions.append(action_model)

		return converted_actions


================================================
File: browser_use/agent/tests.py
================================================
import pytest

from browser_use.agent.views import (
	ActionResult,
	AgentBrain,
	AgentHistory,
	AgentHistoryList,
	AgentOutput,
)
from browser_use.browser.views import BrowserState, BrowserStateHistory, TabInfo
from browser_use.controller.registry.service import Registry
from browser_use.controller.views import ClickElementAction, DoneAction, ExtractPageContentAction
from browser_use.dom.views import DOMElementNode


@pytest.fixture
def sample_browser_state():
	return BrowserState(
		url='https://example.com',
		title='Example Page',
		tabs=[TabInfo(url='https://example.com', title='Example Page', page_id=1)],
		screenshot='screenshot1.png',
		element_tree=DOMElementNode(
			tag_name='root',
			is_visible=True,
			parent=None,
			xpath='',
			attributes={},
			children=[],
		),
		selector_map={},
	)


@pytest.fixture
def action_registry():
	registry = Registry()

	# Register the actions we need for testing
	@registry.action(
		description='Click an element', requires_browser=True, param_model=ClickElementAction
	)
	def click_element(params: ClickElementAction, browser=None):
		pass

	@registry.action(
		description='Extract page content',
		requires_browser=True,
		param_model=ExtractPageContentAction,
	)
	def extract_page_content(params: ExtractPageContentAction, browser=None):
		pass

	@registry.action(description='Mark task as done', param_model=DoneAction)
	def done(params: DoneAction):
		pass

	# Create the dynamic ActionModel with all registered actions
	return registry.create_action_model()


@pytest.fixture
def sample_history(action_registry):
	# Create actions with nested params structure
	click_action = action_registry(click_element={'index': 1})

	extract_action = action_registry(extract_page_content={'value': 'text'})

	done_action = action_registry(done={'text': 'Task completed'})

	histories = [
		AgentHistory(
			model_output=AgentOutput(
				current_state=AgentBrain(
					evaluation_previous_goal='None', memory='Started task', next_goal='Click button'
				),
				action=[click_action],
			),
			result=[ActionResult(is_done=False)],
			state=BrowserStateHistory(
				url='https://example.com',
				title='Page 1',
				tabs=[TabInfo(url='https://example.com', title='Page 1', page_id=1)],
				screenshot='screenshot1.png',
				interacted_element=[],
			),
		),
		AgentHistory(
			model_output=AgentOutput(
				current_state=AgentBrain(
					evaluation_previous_goal='Clicked button',
					memory='Button clicked',
					next_goal='Extract content',
				),
				action=[extract_action],
			),
			result=[
				ActionResult(
					is_done=False,
					extracted_content='Extracted text',
					error='Failed to extract completely',
				)
			],
			state=BrowserStateHistory(
				url='https://example.com/page2',
				title='Page 2',
				tabs=[TabInfo(url='https://example.com/page2', title='Page 2', page_id=2)],
				screenshot='screenshot2.png',
				interacted_element=[],
			),
		),
		AgentHistory(
			model_output=AgentOutput(
				current_state=AgentBrain(
					evaluation_previous_goal='Extracted content',
					memory='Content extracted',
					next_goal='Finish task',
				),
				action=[done_action],
			),
			result=[ActionResult(is_done=True, extracted_content='Task completed', error=None)],
			state=BrowserStateHistory(
				url='https://example.com/page2',
				title='Page 2',
				tabs=[TabInfo(url='https://example.com/page2', title='Page 2', page_id=2)],
				screenshot='screenshot3.png',
				interacted_element=[],
			),
		),
	]
	return AgentHistoryList(history=histories)


def test_last_model_output(sample_history: AgentHistoryList):
	last_output = sample_history.last_action()
	print(last_output)
	assert last_output == {'done': {'text': 'Task completed'}}


def test_get_errors(sample_history: AgentHistoryList):
	errors = sample_history.errors()
	assert len(errors) == 1
	assert errors[0] == 'Failed to extract completely'


def test_final_result(sample_history: AgentHistoryList):
	assert sample_history.final_result() == 'Task completed'


def test_is_done(sample_history: AgentHistoryList):
	assert sample_history.is_done() == True


def test_urls(sample_history: AgentHistoryList):
	urls = sample_history.urls()
	assert 'https://example.com' in urls
	assert 'https://example.com/page2' in urls


def test_all_screenshots(sample_history: AgentHistoryList):
	screenshots = sample_history.screenshots()
	assert len(screenshots) == 3
	assert screenshots == ['screenshot1.png', 'screenshot2.png', 'screenshot3.png']


def test_all_model_outputs(sample_history: AgentHistoryList):
	outputs = sample_history.model_actions()
	assert len(outputs) == 3
	assert outputs[0] == {'click_element': {'index': 1, 'xpath': '//button[1]'}}
	assert outputs[1] == {'extract_page_content': {'value': 'text'}}
	assert outputs[2] == {'done': {'text': 'Task completed'}}


def test_all_model_outputs_filtered(sample_history: AgentHistoryList):
	filtered = sample_history.model_actions_filtered(include=['click_element'])
	assert len(filtered) == 1
	assert filtered[0]['click_element']['index'] == 1


def test_empty_history():
	empty_history = AgentHistoryList(history=[])
	assert empty_history.last_action() is None
	assert empty_history.final_result() is None
	assert empty_history.is_done() == False
	assert len(empty_history.urls()) == 0


# Add a test to verify action creation
def test_action_creation(action_registry):
	click_action = action_registry(click_element={'index': 1})

	assert click_action.model_dump(exclude_none=True) == {'click_element': {'index': 1}}


# run this with:
# pytest browser_use/agent/tests.py


================================================
File: browser_use/agent/views.py
================================================
from __future__ import annotations

import json
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Type

from openai import RateLimitError
from pydantic import BaseModel, ConfigDict, Field, ValidationError, create_model

from browser_use.browser.views import BrowserStateHistory
from browser_use.controller.registry.views import ActionModel
from browser_use.dom.history_tree_processor.service import (
	DOMElementNode,
	DOMHistoryElement,
	HistoryTreeProcessor,
)
from browser_use.dom.views import SelectorMap


@dataclass
class AgentStepInfo:
	step_number: int
	max_steps: int


class ActionResult(BaseModel):
	"""Result of executing an action"""

	is_done: Optional[bool] = False
	extracted_content: Optional[str] = None
	error: Optional[str] = None
	include_in_memory: bool = False  # whether to include in past messages as context or not


class AgentBrain(BaseModel):
	"""Current state of the agent"""

	evaluation_previous_goal: str
	memory: str
	next_goal: str


class AgentOutput(BaseModel):
	"""Output model for agent

	@dev note: this model is extended with custom actions in AgentService. You can also use some fields that are not in this model as provided by the linter, as long as they are registered in the DynamicActions model.
	"""

	model_config = ConfigDict(arbitrary_types_allowed=True)

	current_state: AgentBrain
	action: list[ActionModel]

	@staticmethod
	def type_with_custom_actions(custom_actions: Type[ActionModel]) -> Type['AgentOutput']:
		"""Extend actions with custom actions"""
		return create_model(
			'AgentOutput',
			__base__=AgentOutput,
			action=(list[custom_actions], Field(...)),  # Properly annotated field with no default
			__module__=AgentOutput.__module__,
		)


class AgentHistory(BaseModel):
	"""History item for agent actions"""

	model_output: AgentOutput | None
	result: list[ActionResult]
	state: BrowserStateHistory

	model_config = ConfigDict(arbitrary_types_allowed=True, protected_namespaces=())

	@staticmethod
	def get_interacted_element(
		model_output: AgentOutput, selector_map: SelectorMap
	) -> list[DOMHistoryElement | None]:
		elements = []
		for action in model_output.action:
			index = action.get_index()
			if index and index in selector_map:
				el: DOMElementNode = selector_map[index]
				elements.append(HistoryTreeProcessor.convert_dom_element_to_history_element(el))
			else:
				elements.append(None)
		return elements

	def model_dump(self, **kwargs) -> Dict[str, Any]:
		"""Custom serialization handling circular references"""

		# Handle action serialization
		model_output_dump = None
		if self.model_output:
			action_dump = [
				action.model_dump(exclude_none=True) for action in self.model_output.action
			]
			model_output_dump = {
				'current_state': self.model_output.current_state.model_dump(),
				'action': action_dump,  # This preserves the actual action data
			}

		return {
			'model_output': model_output_dump,
			'result': [r.model_dump(exclude_none=True) for r in self.result],
			'state': self.state.to_dict(),
		}


class AgentHistoryList(BaseModel):
	"""List of agent history items"""

	history: list[AgentHistory]

	def __str__(self) -> str:
		"""Representation of the AgentHistoryList object"""
		return f'AgentHistoryList(all_results={self.action_results()}, all_model_outputs={self.model_actions()})'

	def __repr__(self) -> str:
		"""Representation of the AgentHistoryList object"""
		return self.__str__()

	def save_to_file(self, filepath: str | Path) -> None:
		"""Save history to JSON file with proper serialization"""
		try:
			Path(filepath).parent.mkdir(parents=True, exist_ok=True)
			data = self.model_dump()
			with open(filepath, 'w', encoding='utf-8') as f:
				json.dump(data, f, indent=2)
		except Exception as e:
			raise e

	def model_dump(self, **kwargs) -> Dict[str, Any]:
		"""Custom serialization that properly uses AgentHistory's model_dump"""
		return {
			'history': [h.model_dump(**kwargs) for h in self.history],
		}

	@classmethod
	def load_from_file(
		cls, filepath: str | Path, output_model: Type[AgentOutput]
	) -> 'AgentHistoryList':
		"""Load history from JSON file"""
		with open(filepath, 'r', encoding='utf-8') as f:
			data = json.load(f)
		# loop through history and validate output_model actions to enrich with custom actions
		for h in data['history']:
			if h['model_output']:
				if isinstance(h['model_output'], dict):
					h['model_output'] = output_model.model_validate(h['model_output'])
				else:
					h['model_output'] = None
			if 'interacted_element' not in h['state']:
				h['state']['interacted_element'] = None
		history = cls.model_validate(data)
		return history

	def last_action(self) -> None | dict:
		"""Last action in history"""
		if self.history and self.history[-1].model_output:
			return self.history[-1].model_output.action[-1].model_dump(exclude_none=True)
		return None

	def errors(self) -> list[str]:
		"""Get all errors from history"""
		errors = []
		for h in self.history:
			errors.extend([r.error for r in h.result if r.error])
		return errors

	def final_result(self) -> None | str:
		"""Final result from history"""
		if self.history and self.history[-1].result[-1].extracted_content:
			return self.history[-1].result[-1].extracted_content
		return None

	def is_done(self) -> bool:
		"""Check if the agent is done"""
		if (
			self.history
			and len(self.history[-1].result) > 0
			and self.history[-1].result[-1].is_done
		):
			return self.history[-1].result[-1].is_done
		return False

	def has_errors(self) -> bool:
		"""Check if the agent has any errors"""
		return len(self.errors()) > 0

	def urls(self) -> list[str]:
		"""Get all unique URLs from history"""
		return [h.state.url for h in self.history if h.state.url]

	def screenshots(self) -> list[str]:
		"""Get all screenshots from history"""
		return [h.state.screenshot for h in self.history if h.state.screenshot]

	def action_names(self) -> list[str]:
		"""Get all action names from history"""
		action_names = []
		for action in self.model_actions():
			actions = list(action.keys())
			if actions:
				action_names.append(actions[0])
		return action_names

	def model_thoughts(self) -> list[AgentBrain]:
		"""Get all thoughts from history"""
		return [h.model_output.current_state for h in self.history if h.model_output]

	def model_outputs(self) -> list[AgentOutput]:
		"""Get all model outputs from history"""
		return [h.model_output for h in self.history if h.model_output]

	# get all actions with params
	def model_actions(self) -> list[dict]:
		"""Get all actions from history"""
		outputs = []

		for h in self.history:
			if h.model_output:
				for action in h.model_output.action:
					output = action.model_dump(exclude_none=True)
					outputs.append(output)
		return outputs

	def action_results(self) -> list[ActionResult]:
		"""Get all results from history"""
		results = []
		for h in self.history:
			results.extend([r for r in h.result if r])
		return results

	def extracted_content(self) -> list[str]:
		"""Get all extracted content from history"""
		content = []
		for h in self.history:
			content.extend([r.extracted_content for r in h.result if r.extracted_content])
		return content

	def model_actions_filtered(self, include: list[str] = []) -> list[dict]:
		"""Get all model actions from history as JSON"""
		outputs = self.model_actions()
		result = []
		for o in outputs:
			for i in include:
				if i == list(o.keys())[0]:
					result.append(o)
		return result


class AgentError:
	"""Container for agent error handling"""

	VALIDATION_ERROR = 'Invalid model output format. Please follow the correct schema.'
	RATE_LIMIT_ERROR = 'Rate limit reached. Waiting before retry.'
	NO_VALID_ACTION = 'No valid action found'

	@staticmethod
	def format_error(error: Exception, include_trace: bool = False) -> str:
		"""Format error message based on error type and optionally include trace"""
		message = ''
		if isinstance(error, ValidationError):
			return f'{AgentError.VALIDATION_ERROR}\nDetails: {str(error)}'
		if isinstance(error, RateLimitError):
			return AgentError.RATE_LIMIT_ERROR
		if include_trace:
			return f'{str(error)}\nStacktrace:\n{traceback.format_exc()}'
		return f'{str(error)}'


================================================
File: browser_use/agent/message_manager/service.py
================================================
from __future__ import annotations

import json
import logging
from datetime import datetime
from typing import List, Optional, Type

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import (
	AIMessage,
	BaseMessage,
	HumanMessage,
	SystemMessage,
	ToolMessage,
)
from langchain_openai import ChatOpenAI

from browser_use.agent.message_manager.views import MessageHistory, MessageMetadata
from browser_use.agent.prompts import AgentMessagePrompt, SystemPrompt
from browser_use.agent.views import ActionResult, AgentOutput, AgentStepInfo
from browser_use.browser.views import BrowserState

logger = logging.getLogger(__name__)


class MessageManager:
	def __init__(
		self,
		llm: BaseChatModel,
		task: str,
		action_descriptions: str,
		system_prompt_class: Type[SystemPrompt],
		max_input_tokens: int = 128000,
		estimated_characters_per_token: int = 3,
		image_tokens: int = 800,
		include_attributes: list[str] = [],
		max_error_length: int = 400,
		max_actions_per_step: int = 10,
		message_context: Optional[str] = None,
	):
		self.llm = llm
		self.system_prompt_class = system_prompt_class
		self.max_input_tokens = max_input_tokens
		self.history = MessageHistory()
		self.task = task
		self.action_descriptions = action_descriptions
		self.estimated_characters_per_token = estimated_characters_per_token
		self.IMG_TOKENS = image_tokens
		self.include_attributes = include_attributes
		self.max_error_length = max_error_length
		self.message_context = message_context

		system_message = self.system_prompt_class(
			self.action_descriptions,
			current_date=datetime.now(),
			max_actions_per_step=max_actions_per_step,
		).get_system_message()

		self._add_message_with_tokens(system_message)
		self.system_prompt = system_message

		if self.message_context:
			context_message = HumanMessage(content=self.message_context)
			self._add_message_with_tokens(context_message)

		task_message = self.task_instructions(task)
		self._add_message_with_tokens(task_message)
		self.tool_id = 1
		tool_calls = [
			{
				'name': 'AgentOutput',
				'args': {
					'current_state': {
						'evaluation_previous_goal': 'Unknown - No previous actions to evaluate.',
						'memory': '',
						'next_goal': 'Start browser',
					},
					'action': [],
				},
				'id': str(self.tool_id),
				'type': 'tool_call',
			}
		]

		example_tool_call = AIMessage(
			content=f'',
			tool_calls=tool_calls,
		)
		self._add_message_with_tokens(example_tool_call)
		tool_message = ToolMessage(
			content=f'Browser started',
			tool_call_id=str(self.tool_id),
		)
		self._add_message_with_tokens(tool_message)
		self.tool_id += 1

	@staticmethod
	def task_instructions(task: str) -> HumanMessage:
		content = f'Your ultimate task is: {task}. If you achieved your ultimate task, stop everything and use the done action in the next step to complete the task. If not, continue as usual.'
		return HumanMessage(content=content)

	def add_new_task(self, new_task: str) -> None:
		content = (
			f'Your new ultimate task is: {new_task}. Take the previous context into account and finish your new ultimate task. '
		)
		msg = HumanMessage(content=content)
		self._add_message_with_tokens(msg)

	def add_state_message(
		self,
		state: BrowserState,
		result: Optional[List[ActionResult]] = None,
		step_info: Optional[AgentStepInfo] = None,
	) -> None:
		"""Add browser state as human message"""

		# if keep in memory, add to directly to history and add state without result
		if result:
			for r in result:
				if r.include_in_memory:
					if r.extracted_content:
						msg = HumanMessage(content='Action result: ' + str(r.extracted_content))
						self._add_message_with_tokens(msg)
					if r.error:
						msg = HumanMessage(content='Action error: ' + str(r.error)[-self.max_error_length :])
						self._add_message_with_tokens(msg)
					result = None  # if result in history, we dont want to add it again

		# otherwise add state message and result to next message (which will not stay in memory)
		state_message = AgentMessagePrompt(
			state,
			result,
			include_attributes=self.include_attributes,
			max_error_length=self.max_error_length,
			step_info=step_info,
		).get_user_message()
		self._add_message_with_tokens(state_message)

	def _remove_last_state_message(self) -> None:
		"""Remove last state message from history"""
		if len(self.history.messages) > 2 and isinstance(self.history.messages[-1].message, HumanMessage):
			self.history.remove_message()

	def add_model_output(self, model_output: AgentOutput) -> None:
		"""Add model output as AI message"""
		tool_calls = [
			{
				'name': 'AgentOutput',
				'args': model_output.model_dump(mode='json', exclude_unset=True),
				'id': str(self.tool_id),
				'type': 'tool_call',
			}
		]

		msg = AIMessage(
			content='',
			tool_calls=tool_calls,
		)

		self._add_message_with_tokens(msg)
		# empty tool response
		tool_message = ToolMessage(
			content='',
			tool_call_id=str(self.tool_id),
		)
		self._add_message_with_tokens(tool_message)
		self.tool_id += 1

	def get_messages(self) -> List[BaseMessage]:
		"""Get current message list, potentially trimmed to max tokens"""

		msg = [m.message for m in self.history.messages]
		# debug which messages are in history with token count # log
		total_input_tokens = 0
		logger.debug(f'Messages in history: {len(self.history.messages)}:')
		for m in self.history.messages:
			total_input_tokens += m.metadata.input_tokens
			logger.debug(f'{m.message.__class__.__name__} - Token count: {m.metadata.input_tokens}')
		logger.debug(f'Total input tokens: {total_input_tokens}')

		return msg

	def _add_message_with_tokens(self, message: BaseMessage) -> None:
		"""Add message with token count metadata"""
		token_count = self._count_tokens(message)
		metadata = MessageMetadata(input_tokens=token_count)
		self.history.add_message(message, metadata)

	def _count_tokens(self, message: BaseMessage) -> int:
		"""Count tokens in a message using the model's tokenizer"""
		tokens = 0
		if isinstance(message.content, list):
			for item in message.content:
				if 'image_url' in item:
					tokens += self.IMG_TOKENS
				elif isinstance(item, dict) and 'text' in item:
					tokens += self._count_text_tokens(item['text'])
		else:
			msg = message.content
			if hasattr(message, 'tool_calls'):
				msg += str(message.tool_calls)  # type: ignore
			tokens += self._count_text_tokens(msg)
		return tokens

	def _count_text_tokens(self, text: str) -> int:
		"""Count tokens in a text string"""

		tokens = len(text) // self.estimated_characters_per_token  # Rough estimate if no tokenizer available
		return tokens

	def cut_messages(self):
		"""Get current message list, potentially trimmed to max tokens"""
		diff = self.history.total_tokens - self.max_input_tokens
		if diff <= 0:
			return None

		msg = self.history.messages[-1]

		# if list with image remove image
		if isinstance(msg.message.content, list):
			text = ''
			for item in msg.message.content:
				if 'image_url' in item:
					msg.message.content.remove(item)
					diff -= self.IMG_TOKENS
					msg.metadata.input_tokens -= self.IMG_TOKENS
					self.history.total_tokens -= self.IMG_TOKENS
					logger.debug(
						f'Removed image with {self.IMG_TOKENS} tokens - total tokens now: {self.history.total_tokens}/{self.max_input_tokens}'
					)
				elif 'text' in item and isinstance(item, dict):
					text += item['text']
			msg.message.content = text
			self.history.messages[-1] = msg

		if diff <= 0:
			return None

		# if still over, remove text from state message proportionally to the number of tokens needed with buffer
		# Calculate the proportion of content to remove
		proportion_to_remove = diff / msg.metadata.input_tokens
		if proportion_to_remove > 0.99:
			raise ValueError(
				f'Max token limit reached - history is too long - reduce the system prompt or task. '
				f'proportion_to_remove: {proportion_to_remove}'
			)
		logger.debug(
			f'Removing {proportion_to_remove * 100:.2f}% of the last message  {proportion_to_remove * msg.metadata.input_tokens:.2f} / {msg.metadata.input_tokens:.2f} tokens)'
		)

		content = msg.message.content
		characters_to_remove = int(len(content) * proportion_to_remove)
		content = content[:-characters_to_remove]

		# remove tokens and old long message
		self.history.remove_message(index=-1)

		# new message with updated content
		msg = HumanMessage(content=content)
		self._add_message_with_tokens(msg)

		last_msg = self.history.messages[-1]

		logger.debug(
			f'Added message with {last_msg.metadata.input_tokens} tokens - total tokens now: {self.history.total_tokens}/{self.max_input_tokens} - total messages: {len(self.history.messages)}'
		)

	def convert_messages_for_non_function_calling_models(self, input_messages: list[BaseMessage]) -> list[BaseMessage]:
		"""Convert messages for non-function-calling models"""
		output_messages = []
		for message in input_messages:
			if isinstance(message, HumanMessage):
				output_messages.append(message)
			elif isinstance(message, SystemMessage):
				output_messages.append(message)
			elif isinstance(message, ToolMessage):
				output_messages.append(HumanMessage(content=message.content))
			elif isinstance(message, AIMessage):
				# check if tool_calls is a valid JSON object
				if message.tool_calls:
					tool_calls = json.dumps(message.tool_calls)
					output_messages.append(AIMessage(content=tool_calls))
				else:
					output_messages.append(message)
			else:
				raise ValueError(f'Unknown message type: {type(message)}')
		return output_messages

	def merge_successive_human_messages(self, messages: list[BaseMessage]) -> list[BaseMessage]:
		"""Some models like deepseek-reasoner dont allow multiple human messages in a row. This function merges them into one."""
		merged_messages = []
		streak = 0
		for message in messages:
			if isinstance(message, HumanMessage):
				streak += 1
				if streak > 1:
					merged_messages[-1].content += message.content
				else:
					merged_messages.append(message)
			else:
				merged_messages.append(message)
				streak = 0
		return merged_messages

	def extract_json_from_model_output(self, content: str) -> dict:
		"""Extract JSON from model output, handling both plain JSON and code-block-wrapped JSON."""
		try:
			# If content is wrapped in code blocks, extract just the JSON part
			if content.startswith('```'):
				# Find the JSON content between code blocks
				content = content.split('```')[1]
				# Remove language identifier if present (e.g., 'json\n')
				if '\n' in content:
					content = content.split('\n', 1)[1]
			# Parse the cleaned content
			return json.loads(content)
		except json.JSONDecodeError as e:
			logger.warning(f'Failed to parse model output: {str(e)}')
			raise ValueError('Could not parse response.')


================================================
File: browser_use/agent/message_manager/tests.py
================================================
import pytest
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI, ChatOpenAI

from browser_use.agent.message_manager.service import MessageManager
from browser_use.agent.prompts import SystemPrompt
from browser_use.agent.views import ActionResult
from browser_use.browser.views import BrowserState, TabInfo
from browser_use.dom.views import DOMElementNode, DOMTextNode


@pytest.fixture(
	params=[
		ChatOpenAI(model='gpt-4o-mini'),
		AzureChatOpenAI(model='gpt-4o', api_version='2024-02-15-preview'),
		ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=100, temperature=0.0, stop=None),
	],
	ids=['gpt-4o-mini', 'gpt-4o', 'claude-3-5-sonnet'],
)
def message_manager(request: pytest.FixtureRequest):
	llm = request.param
	task = 'Test task'
	action_descriptions = 'Test actions'
	return MessageManager(
		llm=llm,
		task=task,
		action_descriptions=action_descriptions,
		system_prompt_class=SystemPrompt,
		max_input_tokens=1000,
		estimated_characters_per_token=3,
		image_tokens=800,
	)


def test_initial_messages(message_manager: MessageManager):
	"""Test that message manager initializes with system and task messages"""
	messages = message_manager.get_messages()
	assert len(messages) == 2
	assert isinstance(messages[0], SystemMessage)
	assert isinstance(messages[1], HumanMessage)
	assert 'Test task' in messages[1].content


def test_add_state_message(message_manager: MessageManager):
	"""Test adding browser state message"""
	state = BrowserState(
		url='https://test.com',
		title='Test Page',
		element_tree=DOMElementNode(
			tag_name='div',
			attributes={},
			children=[],
			is_visible=True,
			parent=None,
			xpath='//div',
		),
		selector_map={},
		tabs=[TabInfo(page_id=1, url='https://test.com', title='Test Page')],
	)
	message_manager.add_state_message(state)

	messages = message_manager.get_messages()
	assert len(messages) == 3
	assert isinstance(messages[2], HumanMessage)
	assert 'https://test.com' in messages[2].content


def test_add_state_with_memory_result(message_manager: MessageManager):
	"""Test adding state with result that should be included in memory"""
	state = BrowserState(
		url='https://test.com',
		title='Test Page',
		element_tree=DOMElementNode(
			tag_name='div',
			attributes={},
			children=[],
			is_visible=True,
			parent=None,
			xpath='//div',
		),
		selector_map={},
		tabs=[TabInfo(page_id=1, url='https://test.com', title='Test Page')],
	)
	result = ActionResult(extracted_content='Important content', include_in_memory=True)

	message_manager.add_state_message(state, result)
	messages = message_manager.get_messages()

	# Should have system, task, extracted content, and state messages
	assert len(messages) == 4
	assert 'Important content' in messages[2].content
	assert isinstance(messages[2], HumanMessage)
	assert isinstance(messages[3], HumanMessage)
	assert 'Important content' not in messages[3].content


def test_add_state_with_non_memory_result(message_manager: MessageManager):
	"""Test adding state with result that should not be included in memory"""
	state = BrowserState(
		url='https://test.com',
		title='Test Page',
		element_tree=DOMElementNode(
			tag_name='div',
			attributes={},
			children=[],
			is_visible=True,
			parent=None,
			xpath='//div',
		),
		selector_map={},
		tabs=[TabInfo(page_id=1, url='https://test.com', title='Test Page')],
	)
	result = ActionResult(extracted_content='Temporary content', include_in_memory=False)

	message_manager.add_state_message(state, result)
	messages = message_manager.get_messages()

	# Should have system, task, and combined state+result message
	assert len(messages) == 3
	assert 'Temporary content' in messages[2].content
	assert isinstance(messages[2], HumanMessage)


@pytest.mark.skip('not sure how to fix this')
@pytest.mark.parametrize('max_tokens', [100000, 10000, 5000])
def test_token_overflow_handling_with_real_flow(message_manager: MessageManager, max_tokens):
	"""Test handling of token overflow in a realistic message flow"""
	# Set more realistic token limit
	message_manager.max_input_tokens = max_tokens

	# Create a long sequence of interactions
	for i in range(200):  # Simulate 40 steps of interaction
		# Create state with varying content length
		state = BrowserState(
			url=f'https://test{i}.com',
			title=f'Test Page {i}',
			element_tree=DOMElementNode(
				tag_name='div',
				attributes={},
				children=[
					DOMTextNode(
						text=f'Content {j} ' * (10 + i),  # Increasing content length
						is_visible=True,
						parent=None,
					)
					for j in range(5)  # Multiple DOM items
				],
				is_visible=True,
				parent=None,
				xpath='//div',
			),
			selector_map={j: f'//div[{j}]' for j in range(5)},
			tabs=[TabInfo(page_id=1, url=f'https://test{i}.com', title=f'Test Page {i}')],
		)

		# Alternate between different types of results
		result = None
		if i % 2 == 0:  # Every other iteration
			result = ActionResult(
				extracted_content=f'Important content from step {i}' * 5,
				include_in_memory=i % 4 == 0,  # Include in memory every 4th message
			)

		# Add state message
		message_manager.add_state_message(state, result)

		try:
			messages = message_manager.get_messages()
		except ValueError as e:
			if 'Max token limit reached - history is too long' in str(e):
				return  # If error occurs, end the test
			else:
				raise e

		assert message_manager.history.total_tokens <= message_manager.max_input_tokens + 100

		last_msg = messages[-1]
		assert isinstance(last_msg, HumanMessage)

		if i % 4 == 0:
			assert isinstance(message_manager.history.messages[-2].message, HumanMessage)
		if i % 2 == 0 and not i % 4 == 0:
			if isinstance(last_msg.content, list):
				assert 'Current url: https://test' in last_msg.content[0]['text']
			else:
				assert 'Current url: https://test' in last_msg.content

		# Add model output every time
		from browser_use.agent.views import AgentBrain, AgentOutput
		from browser_use.controller.registry.views import ActionModel

		output = AgentOutput(
			current_state=AgentBrain(
				evaluation_previous_goal=f'Success in step {i}',
				memory=f'Memory from step {i}',
				next_goal=f'Goal for step {i + 1}',
			),
			action=[ActionModel()],
		)
		message_manager._remove_last_state_message()
		message_manager.add_model_output(output)

		# Get messages and verify after each addition
		messages = [m.message for m in message_manager.history.messages]

		# Verify token limit is respected

		# Verify essential messages are preserved
		assert isinstance(messages[0], SystemMessage)  # System prompt always first
		assert isinstance(messages[1], HumanMessage)  # Task always second
		assert 'Test task' in messages[1].content

		# Verify structure of latest messages
		assert isinstance(messages[-1], AIMessage)  # Last message should be model output
		assert f'step {i}' in messages[-1].content  # Should contain current step info

		# Log token usage for debugging
		token_usage = message_manager.history.total_tokens
		token_limit = message_manager.max_input_tokens
		# print(f'Step {i}: Using {token_usage}/{token_limit} tokens')

		# go through all messages and verify that the token count and total tokens is correct
		total_tokens = 0
		real_tokens = []
		stored_tokens = []
		for msg in message_manager.history.messages:
			total_tokens += msg.metadata.input_tokens
			stored_tokens.append(msg.metadata.input_tokens)
			real_tokens.append(message_manager._count_tokens(msg.message))
		assert total_tokens == sum(real_tokens)
		assert stored_tokens == real_tokens
		assert message_manager.history.total_tokens == total_tokens


# pytest -s browser_use/agent/message_manager/tests.py


================================================
File: browser_use/agent/message_manager/views.py
================================================
from __future__ import annotations

from typing import List, Optional

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from pydantic import BaseModel, Field


class MessageMetadata(BaseModel):
	"""Metadata for a message including token counts"""

	input_tokens: int = 0


class ManagedMessage(BaseModel):
	"""A message with its metadata"""

	message: BaseMessage
	metadata: MessageMetadata = Field(default_factory=MessageMetadata)


class MessageHistory(BaseModel):
	"""Container for message history with metadata"""

	messages: List[ManagedMessage] = Field(default_factory=list)
	total_tokens: int = 0

	def add_message(self, message: BaseMessage, metadata: MessageMetadata) -> None:
		"""Add a message with metadata"""
		self.messages.append(ManagedMessage(message=message, metadata=metadata))
		self.total_tokens += metadata.input_tokens

	def remove_message(self, index: int = -1) -> None:
		"""Remove last message from history"""
		if self.messages:
			msg = self.messages.pop(index)
			self.total_tokens -= msg.metadata.input_tokens


================================================
File: browser_use/browser/browser.py
================================================
"""
Playwright browser on steroids.
"""

import asyncio
import logging
from dataclasses import dataclass, field

from playwright._impl._api_structures import ProxySettings
from playwright.async_api import Browser as PlaywrightBrowser
from playwright.async_api import (
	Playwright,
	async_playwright,
)

from browser_use.browser.context import BrowserContext, BrowserContextConfig

logger = logging.getLogger(__name__)


@dataclass
class BrowserConfig:
	"""
	Configuration for the Browser.

	Default values:
		headless: True
			Whether to run browser in headless mode

		disable_security: False
			Disable browser security features

		extra_chromium_args: []
			Extra arguments to pass to the browser

		wss_url: None
			Connect to a browser instance via WebSocket

		cdp_url: None
			Connect to a browser instance via CDP

		chrome_instance_path: None
			Path to a Chrome instance to use to connect to your normal browser
			e.g. '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
	"""

	headless: bool = False
	disable_security: bool = True
	extra_chromium_args: list[str] = field(default_factory=list)
	chrome_instance_path: str | None = None
	wss_url: str | None = None
	cdp_url: str | None = None

	proxy: ProxySettings | None = field(default=None)
	new_context_config: BrowserContextConfig = field(default_factory=BrowserContextConfig)


# @singleton: TODO - think about id singleton makes sense here
# @dev By default this is a singleton, but you can create multiple instances if you need to.
class Browser:
	"""
	Playwright browser on steroids.

	This is persistant browser factory that can spawn multiple browser contexts.
	It is recommended to use only one instance of Browser per your application (RAM usage will grow otherwise).
	"""

	def __init__(
		self,
		config: BrowserConfig = BrowserConfig(),
	):
		logger.debug('Initializing new browser')
		self.config = config
		self.playwright: Playwright | None = None
		self.playwright_browser: PlaywrightBrowser | None = None

		self.disable_security_args = []
		if self.config.disable_security:
			self.disable_security_args = [
				'--disable-web-security',
				'--disable-site-isolation-trials',
				'--disable-features=IsolateOrigins,site-per-process',
			]

	async def new_context(
		self, config: BrowserContextConfig = BrowserContextConfig()
	) -> BrowserContext:
		"""Create a browser context"""
		return BrowserContext(config=config, browser=self)

	async def get_playwright_browser(self) -> PlaywrightBrowser:
		"""Get a browser context"""
		if self.playwright_browser is None:
			return await self._init()

		return self.playwright_browser

	async def _init(self):
		"""Initialize the browser session"""
		playwright = await async_playwright().start()
		browser = await self._setup_browser(playwright)

		self.playwright = playwright
		self.playwright_browser = browser

		return self.playwright_browser

	async def _setup_cdp(self, playwright: Playwright) -> PlaywrightBrowser:
		"""Sets up and returns a Playwright Browser instance with anti-detection measures."""
		if not self.config.cdp_url:
			raise ValueError('CDP URL is required')
		logger.info(f'Connecting to remote browser via CDP {self.config.cdp_url}')
		browser = await playwright.chromium.connect_over_cdp(self.config.cdp_url)
		return browser

	async def _setup_wss(self, playwright: Playwright) -> PlaywrightBrowser:
		"""Sets up and returns a Playwright Browser instance with anti-detection measures."""
		if not self.config.wss_url:
			raise ValueError('WSS URL is required')
		logger.info(f'Connecting to remote browser via WSS {self.config.wss_url}')
		browser = await playwright.chromium.connect(self.config.wss_url)
		return browser

	async def _setup_browser_with_instance(self, playwright: Playwright) -> PlaywrightBrowser:
		"""Sets up and returns a Playwright Browser instance with anti-detection measures."""
		if not self.config.chrome_instance_path:
			raise ValueError('Chrome instance path is required')
		import subprocess

		import requests

		try:
			# Check if browser is already running
			response = requests.get('http://localhost:9222/json/version', timeout=2)
			if response.status_code == 200:
				logger.info('Reusing existing Chrome instance')
				browser = await playwright.chromium.connect_over_cdp(
					endpoint_url='http://localhost:9222',
					timeout=20000,  # 20 second timeout for connection
				)
				return browser
		except requests.ConnectionError:
			logger.debug('No existing Chrome instance found, starting a new one')

		# Start a new Chrome instance
		subprocess.Popen(
			[
				self.config.chrome_instance_path,
				'--remote-debugging-port=9222',
			],
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL,
		)
    
		# Attempt to connect again after starting a new instance
		for _ in range(10):
			try:
				response = requests.get('http://localhost:9222/json/version', timeout=2)
				if response.status_code == 200:
					break
			except requests.ConnectionError:
				pass
			await asyncio.sleep(1)

		# Attempt to connect again after starting a new instance
		try:
			browser = await playwright.chromium.connect_over_cdp(
				endpoint_url='http://localhost:9222',
				timeout=20000,  # 20 second timeout for connection
			)
			return browser
		except Exception as e:
			logger.error(f'Failed to start a new Chrome instance.: {str(e)}')
			raise RuntimeError(
				' To start chrome in Debug mode, you need to close all existing Chrome instances and try again otherwise we can not connect to the instance.'
			)

	async def _setup_standard_browser(self, playwright: Playwright) -> PlaywrightBrowser:
		"""Sets up and returns a Playwright Browser instance with anti-detection measures."""
		browser = await playwright.chromium.launch(
			headless=self.config.headless,
			args=[
				'--no-sandbox',
				'--disable-blink-features=AutomationControlled',
				'--disable-infobars',
				'--disable-background-timer-throttling',
				'--disable-popup-blocking',
				'--disable-backgrounding-occluded-windows',
				'--disable-renderer-backgrounding',
				'--disable-window-activation',
				'--disable-focus-on-load',
				'--no-first-run',
				'--no-default-browser-check',
				'--no-startup-window',
				'--window-position=0,0',
				# '--window-size=1280,1000',
			]
			+ self.disable_security_args
			+ self.config.extra_chromium_args,
			proxy=self.config.proxy,
		)
		# convert to Browser
		return browser

	async def _setup_browser(self, playwright: Playwright) -> PlaywrightBrowser:
		"""Sets up and returns a Playwright Browser instance with anti-detection measures."""
		try:
			if self.config.cdp_url:
				return await self._setup_cdp(playwright)
			if self.config.wss_url:
				return await self._setup_wss(playwright)
			elif self.config.chrome_instance_path:
				return await self._setup_browser_with_instance(playwright)
			else:
				return await self._setup_standard_browser(playwright)
		except Exception as e:
			logger.error(f'Failed to initialize Playwright browser: {str(e)}')
			raise

	async def close(self):
		"""Close the browser instance"""
		try:
			if self.playwright_browser:
				await self.playwright_browser.close()
			if self.playwright:
				await self.playwright.stop()
		except Exception as e:
			logger.debug(f'Failed to close browser properly: {e}')
		finally:
			self.playwright_browser = None
			self.playwright = None

	def __del__(self):
		"""Async cleanup when object is destroyed"""
		try:
			if self.playwright_browser or self.playwright:
				loop = asyncio.get_running_loop()
				if loop.is_running():
					loop.create_task(self.close())
				else:
					asyncio.run(self.close())
		except Exception as e:
			logger.debug(f'Failed to cleanup browser in destructor: {e}')


================================================
File: browser_use/browser/context.py
================================================
"""
Playwright browser on steroids.
"""

import asyncio
import base64
import json
import logging
import os
import re
import time
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, TypedDict

from playwright.async_api import Browser as PlaywrightBrowser
from playwright.async_api import (
	BrowserContext as PlaywrightBrowserContext,
)
from playwright.async_api import (
	ElementHandle,
	FrameLocator,
	Page,
)

from browser_use.browser.views import BrowserError, BrowserState, TabInfo, URLNotAllowedError
from browser_use.dom.service import DomService
from browser_use.dom.views import DOMElementNode, SelectorMap
from browser_use.utils import time_execution_sync

if TYPE_CHECKING:
	from browser_use.browser.browser import Browser

logger = logging.getLogger(__name__)


class BrowserContextWindowSize(TypedDict):
	width: int
	height: int


@dataclass
class BrowserContextConfig:
	"""
	Configuration for the BrowserContext.

	Default values:
		cookies_file: None
			Path to cookies file for persistence

	        disable_security: False
	                Disable browser security features

		minimum_wait_page_load_time: 0.5
			Minimum time to wait before getting page state for LLM input

	        wait_for_network_idle_page_load_time: 1.0
	                Time to wait for network requests to finish before getting page state.
	                Lower values may result in incomplete page loads.

		maximum_wait_page_load_time: 5.0
			Maximum time to wait for page load before proceeding anyway

		wait_between_actions: 1.0
			Time to wait between multiple per step actions

		browser_window_size: {
				'width': 1280,
				'height': 1100,
			}
			Default browser window size

		no_viewport: False
			Disable viewport

		save_recording_path: None
			Path to save video recordings

		trace_path: None
			Path to save trace files. It will auto name the file with the TRACE_PATH/{context_id}.zip

		locale: None
			Specify user locale, for example en-GB, de-DE, etc. Locale will affect navigator.language value, Accept-Language request header value as well as number and date formatting rules. If not provided, defaults to the system default locale.

		user_agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
			custom user agent to use.

		highlight_elements: True
			Highlight elements in the DOM on the screen

		viewport_expansion: 500
			Viewport expansion in pixels. This amount will increase the number of elements which are included in the state what the LLM will see. If set to -1, all elements will be included (this leads to high token usage). If set to 0, only the elements which are visible in the viewport will be included.

		allowed_domains: None
			List of allowed domains that can be accessed. If None, all domains are allowed.
			Example: ['example.com', 'api.example.com']
	"""

	cookies_file: str | None = None
	minimum_wait_page_load_time: float = 0.5
	wait_for_network_idle_page_load_time: float = 1
	maximum_wait_page_load_time: float = 5
	wait_between_actions: float = 1

	disable_security: bool = False

	browser_window_size: BrowserContextWindowSize = field(default_factory=lambda: {'width': 1280, 'height': 1100})
	no_viewport: Optional[bool] = None

	save_recording_path: str | None = None
	trace_path: str | None = None
	locale: str | None = None
	user_agent: str = (
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
	)

	highlight_elements: bool = True
	viewport_expansion: int = 500
	allowed_domains: list[str] | None = None


@dataclass
class BrowserSession:
	context: PlaywrightBrowserContext
	current_page: Page
	cached_state: BrowserState


class BrowserContext:
	def __init__(
		self,
		browser: 'Browser',
		config: BrowserContextConfig = BrowserContextConfig(),
	):
		self.context_id = str(uuid.uuid4())
		logger.debug(f'Initializing new browser context with id: {self.context_id}')

		self.config = config
		self.browser = browser

		# Initialize these as None - they'll be set up when needed
		self.session: BrowserSession | None = None

	async def __aenter__(self):
		"""Async context manager entry"""
		await self._initialize_session()
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		"""Async context manager exit"""
		await self.close()

	async def close(self):
		"""Close the browser instance"""
		logger.debug('Closing browser context')

		try:
			# check if already closed
			if self.session is None:
				return

			await self.save_cookies()

			if self.config.trace_path:
				try:
					await self.session.context.tracing.stop(path=os.path.join(self.config.trace_path, f'{self.context_id}.zip'))
				except Exception as e:
					logger.debug(f'Failed to stop tracing: {e}')

			try:
				await self.session.context.close()
			except Exception as e:
				logger.debug(f'Failed to close context: {e}')
		finally:
			self.session = None

	def __del__(self):
		"""Cleanup when object is destroyed"""
		if self.session is not None:
			logger.debug('BrowserContext was not properly closed before destruction')
			try:
				# Use sync Playwright method for force cleanup
				if hasattr(self.session.context, '_impl_obj'):
					asyncio.run(self.session.context._impl_obj.close())
				self.session = None
			except Exception as e:
				logger.warning(f'Failed to force close browser context: {e}')

	async def _initialize_session(self):
		"""Initialize the browser session"""
		logger.debug('Initializing browser context')

		playwright_browser = await self.browser.get_playwright_browser()

		context = await self._create_context(playwright_browser)
		self._add_new_page_listener(context)
		page = await context.new_page()

		# Instead of calling _update_state(), create an empty initial state
		initial_state = BrowserState(
			element_tree=DOMElementNode(
				tag_name='root',
				is_visible=True,
				parent=None,
				xpath='',
				attributes={},
				children=[],
			),
			selector_map={},
			url=page.url,
			title='',
			screenshot=None,
			tabs=[],
			pixels_above=0,
			pixels_below=0,
		)

		self.session = BrowserSession(
			context=context,
			current_page=page,
			cached_state=initial_state,
		)
		return self.session

	def _add_new_page_listener(self, context: PlaywrightBrowserContext):
		async def on_page(page: Page):
			await page.wait_for_load_state()
			logger.debug(f'New page opened: {page.url}')
			if self.session is not None:
				self.session.current_page = page

		context.on('page', on_page)

	async def get_session(self) -> BrowserSession:
		"""Lazy initialization of the browser and related components"""
		if self.session is None:
			return await self._initialize_session()
		return self.session

	async def get_current_page(self) -> Page:
		"""Get the current page"""
		session = await self.get_session()
		return session.current_page

	async def _create_context(self, browser: PlaywrightBrowser):
		"""Creates a new browser context with anti-detection measures and loads cookies if available."""
		if self.browser.config.cdp_url and len(browser.contexts) > 0:
			context = browser.contexts[0]
		elif self.browser.config.chrome_instance_path and len(browser.contexts) > 0:
			# Connect to existing Chrome instance instead of creating new one
			context = browser.contexts[0]
		else:
			# Original code for creating new context
			context = await browser.new_context(
				viewport=self.config.browser_window_size,
				no_viewport=False,
				user_agent=self.config.user_agent,
				java_script_enabled=True,
				bypass_csp=self.config.disable_security,
				ignore_https_errors=self.config.disable_security,
				record_video_dir=self.config.save_recording_path,
				record_video_size=self.config.browser_window_size,
				locale=self.config.locale,
			)

		if self.config.trace_path:
			await context.tracing.start(screenshots=True, snapshots=True, sources=True)

		# Load cookies if they exist
		if self.config.cookies_file and os.path.exists(self.config.cookies_file):
			with open(self.config.cookies_file, 'r') as f:
				cookies = json.load(f)
				logger.info(f'Loaded {len(cookies)} cookies from {self.config.cookies_file}')
				await context.add_cookies(cookies)

		# Expose anti-detection scripts
		await context.add_init_script(
			"""
			// Webdriver property
			Object.defineProperty(navigator, 'webdriver', {
				get: () => undefined
			});

			// Languages
			Object.defineProperty(navigator, 'languages', {
				get: () => ['en-US']
			});

			// Plugins
			Object.defineProperty(navigator, 'plugins', {
				get: () => [1, 2, 3, 4, 5]
			});

			// Chrome runtime
			window.chrome = { runtime: {} };

			// Permissions
			const originalQuery = window.navigator.permissions.query;
			window.navigator.permissions.query = (parameters) => (
				parameters.name === 'notifications' ?
					Promise.resolve({ state: Notification.permission }) :
					originalQuery(parameters)
			);
			(function () {
				const originalAttachShadow = Element.prototype.attachShadow;
				Element.prototype.attachShadow = function attachShadow(options) {
					return originalAttachShadow.call(this, { ...options, mode: "open" });
				};
			})();
			"""
		)

		return context

	async def _wait_for_stable_network(self):
		page = await self.get_current_page()

		pending_requests = set()
		last_activity = asyncio.get_event_loop().time()

		# Define relevant resource types and content types
		RELEVANT_RESOURCE_TYPES = {
			'document',
			'stylesheet',
			'image',
			'font',
			'script',
			'iframe',
		}

		RELEVANT_CONTENT_TYPES = {
			'text/html',
			'text/css',
			'application/javascript',
			'image/',
			'font/',
			'application/json',
		}

		# Additional patterns to filter out
		IGNORED_URL_PATTERNS = {
			# Analytics and tracking
			'analytics',
			'tracking',
			'telemetry',
			'beacon',
			'metrics',
			# Ad-related
			'doubleclick',
			'adsystem',
			'adserver',
			'advertising',
			# Social media widgets
			'facebook.com/plugins',
			'platform.twitter',
			'linkedin.com/embed',
			# Live chat and support
			'livechat',
			'zendesk',
			'intercom',
			'crisp.chat',
			'hotjar',
			# Push notifications
			'push-notifications',
			'onesignal',
			'pushwoosh',
			# Background sync/heartbeat
			'heartbeat',
			'ping',
			'alive',
			# WebRTC and streaming
			'webrtc',
			'rtmp://',
			'wss://',
			# Common CDNs for dynamic content
			'cloudfront.net',
			'fastly.net',
		}

		async def on_request(request):
			# Filter by resource type
			if request.resource_type not in RELEVANT_RESOURCE_TYPES:
				return

			# Filter out streaming, websocket, and other real-time requests
			if request.resource_type in {
				'websocket',
				'media',
				'eventsource',
				'manifest',
				'other',
			}:
				return

			# Filter out by URL patterns
			url = request.url.lower()
			if any(pattern in url for pattern in IGNORED_URL_PATTERNS):
				return

			# Filter out data URLs and blob URLs
			if url.startswith(('data:', 'blob:')):
				return

			# Filter out requests with certain headers
			headers = request.headers
			if headers.get('purpose') == 'prefetch' or headers.get('sec-fetch-dest') in [
				'video',
				'audio',
			]:
				return

			nonlocal last_activity
			pending_requests.add(request)
			last_activity = asyncio.get_event_loop().time()
			# logger.debug(f'Request started: {request.url} ({request.resource_type})')

		async def on_response(response):
			request = response.request
			if request not in pending_requests:
				return

			# Filter by content type if available
			content_type = response.headers.get('content-type', '').lower()

			# Skip if content type indicates streaming or real-time data
			if any(
				t in content_type
				for t in [
					'streaming',
					'video',
					'audio',
					'webm',
					'mp4',
					'event-stream',
					'websocket',
					'protobuf',
				]
			):
				pending_requests.remove(request)
				return

			# Only process relevant content types
			if not any(ct in content_type for ct in RELEVANT_CONTENT_TYPES):
				pending_requests.remove(request)
				return

			# Skip if response is too large (likely not essential for page load)
			content_length = response.headers.get('content-length')
			if content_length and int(content_length) > 5 * 1024 * 1024:  # 5MB
				pending_requests.remove(request)
				return

			nonlocal last_activity
			pending_requests.remove(request)
			last_activity = asyncio.get_event_loop().time()
			# logger.debug(f'Request resolved: {request.url} ({content_type})')

		# Attach event listeners
		page.on('request', on_request)
		page.on('response', on_response)

		try:
			# Wait for idle time
			start_time = asyncio.get_event_loop().time()
			while True:
				await asyncio.sleep(0.1)
				now = asyncio.get_event_loop().time()
				if len(pending_requests) == 0 and (now - last_activity) >= self.config.wait_for_network_idle_page_load_time:
					break
				if now - start_time > self.config.maximum_wait_page_load_time:
					logger.debug(
						f'Network timeout after {self.config.maximum_wait_page_load_time}s with {len(pending_requests)} '
						f'pending requests: {[r.url for r in pending_requests]}'
					)
					break

		finally:
			# Clean up event listeners
			page.remove_listener('request', on_request)
			page.remove_listener('response', on_response)

		logger.debug(f'Network stabilized for {self.config.wait_for_network_idle_page_load_time} seconds')

	async def _wait_for_page_and_frames_load(self, timeout_overwrite: float | None = None):
		"""
		Ensures page is fully loaded before continuing.
		Waits for either network to be idle or minimum WAIT_TIME, whichever is longer.
		Also checks if the loaded URL is allowed.
		"""
		# Start timing
		start_time = time.time()

		# Wait for page load
		try:
			await self._wait_for_stable_network()

			# Check if the loaded URL is allowed
			page = await self.get_current_page()
			await self._check_and_handle_navigation(page)
		except URLNotAllowedError as e:
			raise e
		except Exception:
			logger.warning('Page load failed, continuing...')
			pass

		# Calculate remaining time to meet minimum WAIT_TIME
		elapsed = time.time() - start_time
		remaining = max((timeout_overwrite or self.config.minimum_wait_page_load_time) - elapsed, 0)

		logger.debug(f'--Page loaded in {elapsed:.2f} seconds, waiting for additional {remaining:.2f} seconds')

		# Sleep remaining time if needed
		if remaining > 0:
			await asyncio.sleep(remaining)

	def _is_url_allowed(self, url: str) -> bool:
		"""Check if a URL is allowed based on the whitelist configuration."""
		if not self.config.allowed_domains:
			return True

		try:
			from urllib.parse import urlparse

			parsed_url = urlparse(url)
			domain = parsed_url.netloc.lower()

			# Remove port number if present
			if ':' in domain:
				domain = domain.split(':')[0]

			# Check if domain matches any allowed domain pattern
			return any(
				domain == allowed_domain.lower() or domain.endswith('.' + allowed_domain.lower())
				for allowed_domain in self.config.allowed_domains
			)
		except Exception as e:
			logger.error(f'Error checking URL allowlist: {str(e)}')
			return False

	async def _check_and_handle_navigation(self, page: Page) -> None:
		"""Check if current page URL is allowed and handle if not."""
		if not self._is_url_allowed(page.url):
			logger.warning(f'Navigation to non-allowed URL detected: {page.url}')
			try:
				await self.go_back()
			except Exception as e:
				logger.error(f'Failed to go back after detecting non-allowed URL: {str(e)}')
			raise URLNotAllowedError(f'Navigation to non-allowed URL: {page.url}')

	async def navigate_to(self, url: str):
		"""Navigate to a URL"""
		if not self._is_url_allowed(url):
			raise BrowserError(f'Navigation to non-allowed URL: {url}')

		page = await self.get_current_page()
		await page.goto(url)
		await page.wait_for_load_state()

	async def refresh_page(self):
		"""Refresh the current page"""
		page = await self.get_current_page()
		await page.reload()
		await page.wait_for_load_state()

	async def go_back(self):
		"""Navigate back in history"""
		page = await self.get_current_page()
		try:
			# 10 ms timeout
			await page.go_back(timeout=10, wait_until='domcontentloaded')
			# await self._wait_for_page_and_frames_load(timeout_overwrite=1.0)
		except Exception as e:
			# Continue even if its not fully loaded, because we wait later for the page to load
			logger.debug(f'During go_back: {e}')

	async def go_forward(self):
		"""Navigate forward in history"""
		page = await self.get_current_page()
		try:
			await page.go_forward(timeout=10, wait_until='domcontentloaded')
		except Exception as e:
			# Continue even if its not fully loaded, because we wait later for the page to load
			logger.debug(f'During go_forward: {e}')

	async def close_current_tab(self):
		"""Close the current tab"""
		session = await self.get_session()
		page = session.current_page
		await page.close()

		# Switch to the first available tab if any exist
		if session.context.pages:
			await self.switch_to_tab(0)

		# otherwise the browser will be closed

	async def get_page_html(self) -> str:
		"""Get the current page HTML content"""
		page = await self.get_current_page()
		return await page.content()

	async def execute_javascript(self, script: str):
		"""Execute JavaScript code on the page"""
		page = await self.get_current_page()
		return await page.evaluate(script)

	@time_execution_sync('--get_state')  # This decorator might need to be updated to handle async
	async def get_state(self, use_vision: bool = False) -> BrowserState:
		"""Get the current state of the browser"""
		await self._wait_for_page_and_frames_load()
		session = await self.get_session()
		session.cached_state = await self._update_state(use_vision=use_vision)

		# Save cookies if a file is specified
		if self.config.cookies_file:
			asyncio.create_task(self.save_cookies())

		return session.cached_state

	async def _update_state(self, use_vision: bool = False, focus_element: int = -1) -> BrowserState:
		"""Update and return state."""
		session = await self.get_session()

		# Check if current page is still valid, if not switch to another available page
		try:
			page = await self.get_current_page()
			# Test if page is still accessible
			await page.evaluate('1')
		except Exception as e:
			logger.debug(f'Current page is no longer accessible: {str(e)}')
			# Get all available pages
			pages = session.context.pages
			if pages:
				session.current_page = pages[-1]
				page = session.current_page
				logger.debug(f'Switched to page: {await page.title()}')
			else:
				raise BrowserError('Browser closed: no valid pages available')

		try:
			await self.remove_highlights()
			dom_service = DomService(page)
			content = await dom_service.get_clickable_elements(
				focus_element=focus_element,
				viewport_expansion=self.config.viewport_expansion,
				highlight_elements=self.config.highlight_elements,
			)

			screenshot_b64 = None
			if use_vision:
				screenshot_b64 = await self.take_screenshot()
			pixels_above, pixels_below = await self.get_scroll_info(page)

			self.current_state = BrowserState(
				element_tree=content.element_tree,
				selector_map=content.selector_map,
				url=page.url,
				title=await page.title(),
				tabs=await self.get_tabs_info(),
				screenshot=screenshot_b64,
				pixels_above=pixels_above,
				pixels_below=pixels_below,
			)

			return self.current_state
		except Exception as e:
			logger.error(f'Failed to update state: {str(e)}')
			# Return last known good state if available
			if hasattr(self, 'current_state'):
				return self.current_state
			raise

	# region - Browser Actions

	async def take_screenshot(self, full_page: bool = False) -> str:
		"""
		Returns a base64 encoded screenshot of the current page.
		"""
		page = await self.get_current_page()

		screenshot = await page.screenshot(
			full_page=full_page,
			animations='disabled',
		)

		screenshot_b64 = base64.b64encode(screenshot).decode('utf-8')

		# await self.remove_highlights()

		return screenshot_b64

	async def remove_highlights(self):
		"""
		Removes all highlight overlays and labels created by the highlightElement function.
		Handles cases where the page might be closed or inaccessible.
		"""
		try:
			page = await self.get_current_page()
			await page.evaluate(
				"""
                try {
                    // Remove the highlight container and all its contents
                    const container = document.getElementById('playwright-highlight-container');
                    if (container) {
                        container.remove();
                    }

                    // Remove highlight attributes from elements
                    const highlightedElements = document.querySelectorAll('[browser-user-highlight-id^="playwright-highlight-"]');
                    highlightedElements.forEach(el => {
                        el.removeAttribute('browser-user-highlight-id');
                    });
                } catch (e) {
                    console.error('Failed to remove highlights:', e);
                }
                """
			)
		except Exception as e:
			logger.debug(f'Failed to remove highlights (this is usually ok): {str(e)}')
			# Don't raise the error since this is not critical functionality
			pass

	# endregion

	# region - User Actions
	def _convert_simple_xpath_to_css_selector(self, xpath: str) -> str:
		"""Converts simple XPath expressions to CSS selectors."""
		if not xpath:
			return ''

		# Remove leading slash if present
		xpath = xpath.lstrip('/')

		# Split into parts
		parts = xpath.split('/')
		css_parts = []

		for part in parts:
			if not part:
				continue

			# Handle index notation [n]
			if '[' in part:
				base_part = part[: part.find('[')]
				index_part = part[part.find('[') :]

				# Handle multiple indices
				indices = [i.strip('[]') for i in index_part.split(']')[:-1]]

				for idx in indices:
					try:
						# Handle numeric indices
						if idx.isdigit():
							index = int(idx) - 1
							base_part += f':nth-of-type({index + 1})'
						# Handle last() function
						elif idx == 'last()':
							base_part += ':last-of-type'
						# Handle position() functions
						elif 'position()' in idx:
							if '>1' in idx:
								base_part += ':nth-of-type(n+2)'
					except ValueError:
						continue

				css_parts.append(base_part)
			else:
				css_parts.append(part)

		base_selector = ' > '.join(css_parts)
		return base_selector

	def _enhanced_css_selector_for_element(self, element: DOMElementNode) -> str:
		"""
		Creates a CSS selector for a DOM element, handling various edge cases and special characters.

		Args:
		        element: The DOM element to create a selector for

		Returns:
		        A valid CSS selector string
		"""
		try:
			# Get base selector from XPath
			css_selector = self._convert_simple_xpath_to_css_selector(element.xpath)

			# Handle class attributes
			if 'class' in element.attributes and element.attributes['class']:
				# Define a regex pattern for valid class names in CSS
				valid_class_name_pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_-]*$')

				# Iterate through the class attribute values
				classes = element.attributes['class'].split()
				for class_name in classes:
					# Skip empty class names
					if not class_name.strip():
						continue

					# Check if the class name is valid
					if valid_class_name_pattern.match(class_name):
						# Append the valid class name to the CSS selector
						css_selector += f'.{class_name}'
					else:
						# Skip invalid class names
						continue

			# Expanded set of safe attributes that are stable and useful for selection
			SAFE_ATTRIBUTES = {
				# Standard HTML attributes
				'id',
				'name',
				'type',
				'value',
				'placeholder',
				# Accessibility attributes
				'aria-label',
				'aria-labelledby',
				'aria-describedby',
				'role',
				# Common form attributes
				'for',
				'autocomplete',
				'required',
				'readonly',
				# Media attributes
				'alt',
				'title',
				'src',
				# Data attributes (if they're stable in your application)
				'data-testid',
				'data-id',
				'data-qa',
				'data-cy',
				# Custom stable attributes (add any application-specific ones)
				'href',
				'target',
			}

			# Handle other attributes
			for attribute, value in element.attributes.items():
				if attribute == 'class':
					continue

				# Skip invalid attribute names
				if not attribute.strip():
					continue

				if attribute not in SAFE_ATTRIBUTES:
					continue

				# Escape special characters in attribute names
				safe_attribute = attribute.replace(':', r'\:')

				# Handle different value cases
				if value == '':
					css_selector += f'[{safe_attribute}]'
				elif any(char in value for char in '"\'<>`\n\r\t'):
					# Use contains for values with special characters
					# Regex-substitute *any* whitespace with a single space, then strip.
					collapsed_value = re.sub(r'\s+', ' ', value).strip()
					# Escape embedded double-quotes.
					safe_value = collapsed_value.replace('"', '\\"')
					css_selector += f'[{safe_attribute}*="{safe_value}"]'
				else:
					css_selector += f'[{safe_attribute}="{value}"]'

			return css_selector

		except Exception:
			# Fallback to a more basic selector if something goes wrong
			tag_name = element.tag_name or '*'
			return f"{tag_name}[highlight_index='{element.highlight_index}']"

	async def get_locate_element(self, element: DOMElementNode) -> ElementHandle | None:
		current_frame = await self.get_current_page()

		# Start with the target element and collect all parents
		parents: list[DOMElementNode] = []
		current = element
		while current.parent is not None:
			parent = current.parent
			parents.append(parent)
			current = parent

		# Reverse the parents list to process from top to bottom
		parents.reverse()

		# Process all iframe parents in sequence
		iframes = [item for item in parents if item.tag_name == 'iframe']
		for parent in iframes:
			css_selector = self._enhanced_css_selector_for_element(parent)
			current_frame = current_frame.frame_locator(css_selector)

		css_selector = self._enhanced_css_selector_for_element(element)

		try:
			if isinstance(current_frame, FrameLocator):
				return await current_frame.locator(css_selector).element_handle()
			else:
				# Try to scroll into view if hidden
				element_handle = await current_frame.query_selector(css_selector)
				if element_handle:
					await element_handle.scroll_into_view_if_needed()
					return element_handle
		except Exception as e:
			logger.error(f'Failed to locate element: {str(e)}')
			return None

	async def _input_text_element_node(self, element_node: DOMElementNode, text: str):
		try:
			# Highlight before typing
			if element_node.highlight_index is not None:
				await self._update_state(focus_element=element_node.highlight_index)

			page = await self.get_current_page()
			element = await self.get_locate_element(element_node)

			if element is None:
				raise Exception(f'Element: {repr(element_node)} not found')

			await element.scroll_into_view_if_needed(timeout=2500)
			await element.fill('')
			await element.type(text)
			await page.wait_for_load_state()

		except Exception as e:
			raise Exception(f'Failed to input text into element: {repr(element_node)}. Error: {str(e)}')

	async def _click_element_node(self, element_node: DOMElementNode):
		"""
		Optimized method to click an element using xpath.
		"""
		page = await self.get_current_page()

		try:
			# Highlight before clicking
			if element_node.highlight_index is not None:
				await self._update_state(focus_element=element_node.highlight_index)

			element = await self.get_locate_element(element_node)

			if element is None:
				raise Exception(f'Element: {repr(element_node)} not found')

			# await element.scroll_into_view_if_needed()

			try:
				await element.click(timeout=1500)
				await page.wait_for_load_state()
				# Check if navigation occurred and if the new URL is allowed
				await self._check_and_handle_navigation(page)
			except URLNotAllowedError as e:
				raise e
			except Exception:
				try:
					await page.evaluate('(el) => el.click()', element)
					await page.wait_for_load_state()
					# Check if navigation occurred and if the new URL is allowed
					await self._check_and_handle_navigation(page)
				except URLNotAllowedError as e:
					raise e
				except Exception as e:
					raise Exception(f'Failed to click element: {str(e)}')

		except URLNotAllowedError as e:
			raise e
		except Exception as e:
			raise Exception(f'Failed to click element: {repr(element_node)}. Error: {str(e)}')

	async def get_tabs_info(self) -> list[TabInfo]:
		"""Get information about all tabs"""
		session = await self.get_session()

		tabs_info = []
		for page_id, page in enumerate(session.context.pages):
			tab_info = TabInfo(page_id=page_id, url=page.url, title=await page.title())
			tabs_info.append(tab_info)

		return tabs_info

	async def switch_to_tab(self, page_id: int) -> None:
		"""Switch to a specific tab by its page_id

		@You can also use negative indices to switch to tabs from the end (Pure pythonic way)
		"""
		session = await self.get_session()
		pages = session.context.pages

		if page_id >= len(pages):
			raise BrowserError(f'No tab found with page_id: {page_id}')

		page = pages[page_id]

		# Check if the tab's URL is allowed before switching
		if not self._is_url_allowed(page.url):
			raise BrowserError(f'Cannot switch to tab with non-allowed URL: {page.url}')

		session.current_page = page

		await page.bring_to_front()
		await page.wait_for_load_state()

	async def create_new_tab(self, url: str | None = None) -> None:
		"""Create a new tab and optionally navigate to a URL"""
		if url and not self._is_url_allowed(url):
			raise BrowserError(f'Cannot create new tab with non-allowed URL: {url}')

		session = await self.get_session()
		new_page = await session.context.new_page()
		session.current_page = new_page

		await new_page.wait_for_load_state()

		page = await self.get_current_page()

		if url:
			await page.goto(url)
			await self._wait_for_page_and_frames_load(timeout_overwrite=1)

	# endregion

	# region - Helper methods for easier access to the DOM
	async def get_selector_map(self) -> SelectorMap:
		session = await self.get_session()
		return session.cached_state.selector_map

	async def get_element_by_index(self, index: int) -> ElementHandle | None:
		selector_map = await self.get_selector_map()
		return await self.get_locate_element(selector_map[index])

	async def get_dom_element_by_index(self, index: int) -> DOMElementNode | None:
		selector_map = await self.get_selector_map()
		return selector_map[index]

	async def save_cookies(self):
		"""Save current cookies to file"""
		if self.session and self.session.context and self.config.cookies_file:
			try:
				cookies = await self.session.context.cookies()
				logger.info(f'Saving {len(cookies)} cookies to {self.config.cookies_file}')

				# Check if the path is a directory and create it if necessary
				dirname = os.path.dirname(self.config.cookies_file)
				if dirname:
					os.makedirs(dirname, exist_ok=True)

				with open(self.config.cookies_file, 'w') as f:
					json.dump(cookies, f)
			except Exception as e:
				logger.warning(f'Failed to save cookies: {str(e)}')

	async def is_file_uploader(self, element_node: DOMElementNode, max_depth: int = 3, current_depth: int = 0) -> bool:
		"""Check if element or its children are file uploaders"""
		if current_depth > max_depth:
			return False

		# Check current element
		is_uploader = False

		if not isinstance(element_node, DOMElementNode):
			return False

		# Check for file input attributes
		if element_node.tag_name == 'input':
			is_uploader = element_node.attributes.get('type') == 'file' or element_node.attributes.get('accept') is not None

		if is_uploader:
			return True

		# Recursively check children
		if element_node.children and current_depth < max_depth:
			for child in element_node.children:
				if isinstance(child, DOMElementNode):
					if await self.is_file_uploader(child, max_depth, current_depth + 1):
						return True

		return False

	async def get_scroll_info(self, page: Page) -> tuple[int, int]:
		"""Get scroll position information for the current page."""
		scroll_y = await page.evaluate('window.scrollY')
		viewport_height = await page.evaluate('window.innerHeight')
		total_height = await page.evaluate('document.documentElement.scrollHeight')
		pixels_above = scroll_y
		pixels_below = total_height - (scroll_y + viewport_height)
		return pixels_above, pixels_below


================================================
File: browser_use/browser/views.py
================================================
from dataclasses import dataclass, field
from typing import Any, Optional

from pydantic import BaseModel

from browser_use.dom.history_tree_processor.service import DOMHistoryElement
from browser_use.dom.views import DOMState


# Pydantic
class TabInfo(BaseModel):
	"""Represents information about a browser tab"""

	page_id: int
	url: str
	title: str


@dataclass
class BrowserState(DOMState):
	url: str
	title: str
	tabs: list[TabInfo]
	screenshot: Optional[str] = None
	pixels_above: int = 0
	pixels_below: int = 0
	browser_errors: list[str] = field(default_factory=list)


@dataclass
class BrowserStateHistory:
	url: str
	title: str
	tabs: list[TabInfo]
	interacted_element: list[DOMHistoryElement | None] | list[None]
	screenshot: Optional[str] = None

	def to_dict(self) -> dict[str, Any]:
		data = {}
		data['tabs'] = [tab.model_dump() for tab in self.tabs]
		data['screenshot'] = self.screenshot
		data['interacted_element'] = [el.to_dict() if el else None for el in self.interacted_element]
		data['url'] = self.url
		data['title'] = self.title
		return data


class BrowserError(Exception):
	"""Base class for all browser errors"""


class URLNotAllowedError(BrowserError):
	"""Error raised when a URL is not allowed"""


================================================
File: browser_use/browser/tests/screenshot_test.py
================================================
import base64

import pytest

from browser_use.browser.browser import Browser, BrowserConfig


@pytest.fixture
async def browser():
	browser_service = Browser(config=BrowserConfig(headless=True))
	yield browser_service

	await browser_service.close()


# @pytest.mark.skip(reason='takes too long')
def test_take_full_page_screenshot(browser):
	# Go to a test page
	browser.go_to_url('https://example.com')

	# Take full page screenshot
	screenshot_b64 = browser.take_screenshot(full_page=True)

	# Verify screenshot is not empty and is valid base64
	assert screenshot_b64 is not None
	assert isinstance(screenshot_b64, str)
	assert len(screenshot_b64) > 0

	# Test we can decode the base64 string
	try:
		base64.b64decode(screenshot_b64)
	except Exception as e:
		pytest.fail(f'Failed to decode base64 screenshot: {str(e)}')


if __name__ == '__main__':
	test_take_full_page_screenshot(Browser(config=BrowserConfig(headless=False)))


================================================
File: browser_use/browser/tests/test_clicks.py
================================================
import asyncio
import json

import pytest

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.dom.views import ElementTreeSerializer
from browser_use.utils import time_execution_sync


# run with: pytest browser_use/browser/tests/test_clicks.py
@pytest.mark.asyncio
async def test_highlight_elements():
	browser = Browser(config=BrowserConfig(headless=False, disable_security=True))

	async with await browser.new_context() as context:
		page = await context.get_current_page()
		# await page.goto('https://immobilienscout24.de')
		# await page.goto('https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/service-plans')
		# await page.goto('https://google.com/search?q=elon+musk')
		# await page.goto('https://kayak.com')
		# await page.goto('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')
		# await page.goto('https://dictionary.cambridge.org')
		# await page.goto('https://github.com')
		await page.goto('https://huggingface.co/')

		await asyncio.sleep(1)

		while True:
			try:
				# await asyncio.sleep(10)
				state = await context.get_state()

				with open('./tmp/page.json', 'w') as f:
					json.dump(
						ElementTreeSerializer.dom_element_node_to_json(state.element_tree),
						f,
						indent=1,
					)

				# await time_execution_sync('highlight_selector_map_elements')(
				# 	browser.highlight_selector_map_elements
				# )(state.selector_map)

				# Find and print duplicate XPaths
				xpath_counts = {}
				if not state.selector_map:
					continue
				for selector in state.selector_map.values():
					xpath = selector.xpath
					if xpath in xpath_counts:
						xpath_counts[xpath] += 1
					else:
						xpath_counts[xpath] = 1

				print('\nDuplicate XPaths found:')
				for xpath, count in xpath_counts.items():
					if count > 1:
						print(f'XPath: {xpath}')
						print(f'Count: {count}\n')

				print(list(state.selector_map.keys()), 'Selector map keys')
				print(state.element_tree.clickable_elements_to_string())
				action = input('Select next action: ')

				await time_execution_sync('remove_highlight_elements')(context.remove_highlights)()

				node_element = state.selector_map[int(action)]

				# check if index of selector map are the same as index of items in dom_items

				await context._click_element_node(node_element)

			except Exception as e:
				print(e)


================================================
File: browser_use/controller/service.py
================================================
import asyncio
import json
import logging
from typing import Optional, Type

from main_content_extractor import MainContentExtractor
from pydantic import BaseModel

from browser_use.agent.views import ActionModel, ActionResult
from browser_use.browser.context import BrowserContext
from browser_use.controller.registry.service import Registry
from browser_use.controller.views import (
	ClickElementAction,
	DoneAction,
	ExtractPageContentAction,
	GoToUrlAction,
	InputTextAction,
	NoParamsAction,
	OpenTabAction,
	ScrollAction,
	SearchGoogleAction,
	SendKeysAction,
	SwitchTabAction,
)
from browser_use.utils import time_execution_async, time_execution_sync

logger = logging.getLogger(__name__)


class Controller:
	def __init__(
		self,
		exclude_actions: list[str] = [],
		output_model: Optional[Type[BaseModel]] = None,
	):
		self.exclude_actions = exclude_actions
		self.output_model = output_model
		self.registry = Registry(exclude_actions)
		self._register_default_actions()

	def _register_default_actions(self):
		"""Register all default browser actions"""

		if self.output_model is not None:

			@self.registry.action('Complete task', param_model=self.output_model)
			async def done(params: BaseModel):
				return ActionResult(is_done=True, extracted_content=params.model_dump_json())
		else:

			@self.registry.action('Complete task', param_model=DoneAction)
			async def done(params: DoneAction):
				return ActionResult(is_done=True, extracted_content=params.text)

		# Basic Navigation Actions
		@self.registry.action(
			'Search Google in the current tab',
			param_model=SearchGoogleAction,
			requires_browser=True,
		)
		async def search_google(params: SearchGoogleAction, browser: BrowserContext):
			page = await browser.get_current_page()
			await page.goto(f'https://www.google.com/search?q={params.query}&udm=14')
			await page.wait_for_load_state()
			msg = f'🔍  Searched for "{params.query}" in Google'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action('Navigate to URL in the current tab', param_model=GoToUrlAction, requires_browser=True)
		async def go_to_url(params: GoToUrlAction, browser: BrowserContext):
			page = await browser.get_current_page()
			await page.goto(params.url)
			await page.wait_for_load_state()
			msg = f'🔗  Navigated to {params.url}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action('Go back', param_model=NoParamsAction, requires_browser=True)
		async def go_back(_: NoParamsAction, browser: BrowserContext):
			await browser.go_back()
			msg = '🔙  Navigated back'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		# Element Interaction Actions
		@self.registry.action('Click element', param_model=ClickElementAction, requires_browser=True)
		async def click_element(params: ClickElementAction, browser: BrowserContext):
			session = await browser.get_session()
			state = session.cached_state

			if params.index not in state.selector_map:
				raise Exception(f'Element with index {params.index} does not exist - retry or use alternative actions')

			element_node = state.selector_map[params.index]
			initial_pages = len(session.context.pages)

			# if element has file uploader then dont click
			if await browser.is_file_uploader(element_node):
				msg = f'Index {params.index} - has an element which opens file upload dialog. To upload files please use a specific function to upload files '
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

			msg = None

			try:
				await browser._click_element_node(element_node)
				msg = f'🖱️  Clicked button with index {params.index}: {element_node.get_all_text_till_next_clickable_element(max_depth=2)}'

				logger.info(msg)
				logger.debug(f'Element xpath: {element_node.xpath}')
				if len(session.context.pages) > initial_pages:
					new_tab_msg = 'New tab opened - switching to it'
					msg += f' - {new_tab_msg}'
					logger.info(new_tab_msg)
					await browser.switch_to_tab(-1)
				return ActionResult(extracted_content=msg, include_in_memory=True)
			except Exception as e:
				logger.warning(f'Element not clickable with index {params.index} - most likely the page changed')
				return ActionResult(error=str(e))

		@self.registry.action(
			'Input text into a input interactive element',
			param_model=InputTextAction,
			requires_browser=True,
		)
		async def input_text(params: InputTextAction, browser: BrowserContext):
			session = await browser.get_session()
			state = session.cached_state

			if params.index not in state.selector_map:
				raise Exception(f'Element index {params.index} does not exist - retry or use alternative actions')

			element_node = state.selector_map[params.index]
			await browser._input_text_element_node(element_node, params.text)
			msg = f'⌨️  Input "{params.text}" into index {params.index}'
			logger.info(msg)
			logger.debug(f'Element xpath: {element_node.xpath}')
			return ActionResult(extracted_content=msg, include_in_memory=True)

		# Tab Management Actions
		@self.registry.action('Switch tab', param_model=SwitchTabAction, requires_browser=True)
		async def switch_tab(params: SwitchTabAction, browser: BrowserContext):
			await browser.switch_to_tab(params.page_id)
			# Wait for tab to be ready
			page = await browser.get_current_page()
			await page.wait_for_load_state()
			msg = f'🔄  Switched to tab {params.page_id}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action('Open url in new tab', param_model=OpenTabAction, requires_browser=True)
		async def open_tab(params: OpenTabAction, browser: BrowserContext):
			await browser.create_new_tab(params.url)
			msg = f'🔗  Opened new tab with {params.url}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		# Content Actions
		@self.registry.action(
			'Extract page content to get the pure text or markdown with links if include_links is set to true',
			param_model=ExtractPageContentAction,
			requires_browser=True,
		)
		async def extract_content(params: ExtractPageContentAction, browser: BrowserContext):
			page = await browser.get_current_page()
			output_format = 'markdown' if params.include_links else 'text'
			content = MainContentExtractor.extract(  # type: ignore
				html=await page.content(),
				output_format=output_format,
			)
			msg = f'📄  Extracted page as {output_format}\n: {content}\n'
			logger.info(msg)
			return ActionResult(extracted_content=msg)

		@self.registry.action(
			'Scroll down the page by pixel amount - if no amount is specified, scroll down one page',
			param_model=ScrollAction,
			requires_browser=True,
		)
		async def scroll_down(params: ScrollAction, browser: BrowserContext):
			page = await browser.get_current_page()
			if params.amount is not None:
				await page.evaluate(f'window.scrollBy(0, {params.amount});')
			else:
				await page.keyboard.press('PageDown')

			amount = f'{params.amount} pixels' if params.amount is not None else 'one page'
			msg = f'🔍  Scrolled down the page by {amount}'
			logger.info(msg)
			return ActionResult(
				extracted_content=msg,
				include_in_memory=True,
			)

		# scroll up
		@self.registry.action(
			'Scroll up the page by pixel amount - if no amount is specified, scroll up one page',
			param_model=ScrollAction,
			requires_browser=True,
		)
		async def scroll_up(params: ScrollAction, browser: BrowserContext):
			page = await browser.get_current_page()
			if params.amount is not None:
				await page.evaluate(f'window.scrollBy(0, -{params.amount});')
			else:
				await page.keyboard.press('PageUp')

			amount = f'{params.amount} pixels' if params.amount is not None else 'one page'
			msg = f'🔍  Scrolled up the page by {amount}'
			logger.info(msg)
			return ActionResult(
				extracted_content=msg,
				include_in_memory=True,
			)

		# send keys
		@self.registry.action(
			'Send strings of special keys like Backspace, Insert, PageDown, Delete, Enter, Shortcuts such as `Control+o`, `Control+Shift+T` are supported as well. This gets used in keyboard.press. Be aware of different operating systems and their shortcuts',
			param_model=SendKeysAction,
			requires_browser=True,
		)
		async def send_keys(params: SendKeysAction, browser: BrowserContext):
			page = await browser.get_current_page()

			await page.keyboard.press(params.keys)
			msg = f'⌨️  Sent keys: {params.keys}'
			logger.info(msg)
			return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action(
			description='If you dont find something which you want to interact with, scroll to it',
			requires_browser=True,
		)
		async def scroll_to_text(text: str, browser: BrowserContext):  # type: ignore
			page = await browser.get_current_page()
			try:
				# Try different locator strategies
				locators = [
					page.get_by_text(text, exact=False),
					page.locator(f'text={text}'),
					page.locator(f"//*[contains(text(), '{text}')]"),
				]

				for locator in locators:
					try:
						# First check if element exists and is visible
						if await locator.count() > 0 and await locator.first.is_visible():
							await locator.first.scroll_into_view_if_needed()
							await asyncio.sleep(0.5)  # Wait for scroll to complete
							msg = f'🔍  Scrolled to text: {text}'
							logger.info(msg)
							return ActionResult(extracted_content=msg, include_in_memory=True)
					except Exception as e:
						logger.debug(f'Locator attempt failed: {str(e)}')
						continue

				msg = f"Text '{text}' not found or not visible on page"
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

			except Exception as e:
				msg = f"Failed to scroll to text '{text}': {str(e)}"
				logger.error(msg)
				return ActionResult(error=msg, include_in_memory=True)

		@self.registry.action(
			description='Get all options from a native dropdown',
			requires_browser=True,
		)
		async def get_dropdown_options(index: int, browser: BrowserContext) -> ActionResult:
			"""Get all options from a native dropdown"""
			page = await browser.get_current_page()
			selector_map = await browser.get_selector_map()
			dom_element = selector_map[index]

			try:
				# Frame-aware approach since we know it works
				all_options = []
				frame_index = 0

				for frame in page.frames:
					try:
						options = await frame.evaluate(
							"""
							(xpath) => {
								const select = document.evaluate(xpath, document, null,
									XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
								if (!select) return null;

								return {
									options: Array.from(select.options).map(opt => ({
										text: opt.text, //do not trim, because we are doing exact match in select_dropdown_option
										value: opt.value,
										index: opt.index
									})),
									id: select.id,
									name: select.name
								};
							}
						""",
							dom_element.xpath,
						)

						if options:
							logger.debug(f'Found dropdown in frame {frame_index}')
							logger.debug(f'Dropdown ID: {options["id"]}, Name: {options["name"]}')

							formatted_options = []
							for opt in options['options']:
								# encoding ensures AI uses the exact string in select_dropdown_option
								encoded_text = json.dumps(opt['text'])
								formatted_options.append(f'{opt["index"]}: text={encoded_text}')

							all_options.extend(formatted_options)

					except Exception as frame_e:
						logger.debug(f'Frame {frame_index} evaluation failed: {str(frame_e)}')

					frame_index += 1

				if all_options:
					msg = '\n'.join(all_options)
					msg += '\nUse the exact text string in select_dropdown_option'
					logger.info(msg)
					return ActionResult(extracted_content=msg, include_in_memory=True)
				else:
					msg = 'No options found in any frame for dropdown'
					logger.info(msg)
					return ActionResult(extracted_content=msg, include_in_memory=True)

			except Exception as e:
				logger.error(f'Failed to get dropdown options: {str(e)}')
				msg = f'Error getting options: {str(e)}'
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

		@self.registry.action(
			description='Select dropdown option for interactive element index by the text of the option you want to select',
			requires_browser=True,
		)
		async def select_dropdown_option(
			index: int,
			text: str,
			browser: BrowserContext,
		) -> ActionResult:
			"""Select dropdown option by the text of the option you want to select"""
			page = await browser.get_current_page()
			selector_map = await browser.get_selector_map()
			dom_element = selector_map[index]

			# Validate that we're working with a select element
			if dom_element.tag_name != 'select':
				logger.error(f'Element is not a select! Tag: {dom_element.tag_name}, Attributes: {dom_element.attributes}')
				msg = f'Cannot select option: Element with index {index} is a {dom_element.tag_name}, not a select'
				return ActionResult(extracted_content=msg, include_in_memory=True)

			logger.debug(f"Attempting to select '{text}' using xpath: {dom_element.xpath}")
			logger.debug(f'Element attributes: {dom_element.attributes}')
			logger.debug(f'Element tag: {dom_element.tag_name}')

			xpath = '//' + dom_element.xpath

			try:
				frame_index = 0
				for frame in page.frames:
					try:
						logger.debug(f'Trying frame {frame_index} URL: {frame.url}')

						# First verify we can find the dropdown in this frame
						find_dropdown_js = """
							(xpath) => {
								try {
									const select = document.evaluate(xpath, document, null,
										XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
									if (!select) return null;
									if (select.tagName.toLowerCase() !== 'select') {
										return {
											error: `Found element but it's a ${select.tagName}, not a SELECT`,
											found: false
										};
									}
									return {
										id: select.id,
										name: select.name,
										found: true,
										tagName: select.tagName,
										optionCount: select.options.length,
										currentValue: select.value,
										availableOptions: Array.from(select.options).map(o => o.text.trim())
									};
								} catch (e) {
									return {error: e.toString(), found: false};
								}
							}
						"""

						dropdown_info = await frame.evaluate(find_dropdown_js, dom_element.xpath)

						if dropdown_info:
							if not dropdown_info.get('found'):
								logger.error(f'Frame {frame_index} error: {dropdown_info.get("error")}')
								continue

							logger.debug(f'Found dropdown in frame {frame_index}: {dropdown_info}')

							# "label" because we are selecting by text
							# nth(0) to disable error thrown by strict mode
							# timeout=1000 because we are already waiting for all network events, therefore ideally we don't need to wait a lot here (default 30s)
							selected_option_values = (
								await frame.locator('//' + dom_element.xpath).nth(0).select_option(label=text, timeout=1000)
							)

							msg = f'selected option {text} with value {selected_option_values}'
							logger.info(msg + f' in frame {frame_index}')

							return ActionResult(extracted_content=msg, include_in_memory=True)

					except Exception as frame_e:
						logger.error(f'Frame {frame_index} attempt failed: {str(frame_e)}')
						logger.error(f'Frame type: {type(frame)}')
						logger.error(f'Frame URL: {frame.url}')

					frame_index += 1

				msg = f"Could not select option '{text}' in any frame"
				logger.info(msg)
				return ActionResult(extracted_content=msg, include_in_memory=True)

			except Exception as e:
				msg = f'Selection failed: {str(e)}'
				logger.error(msg)
				return ActionResult(error=msg, include_in_memory=True)

	def action(self, description: str, **kwargs):
		"""Decorator for registering custom actions

		@param description: Describe the LLM what the function does (better description == better function calling)
		"""
		return self.registry.action(description, **kwargs)

	@time_execution_async('--multi-act')
	async def multi_act(
		self, actions: list[ActionModel], browser_context: BrowserContext, check_for_new_elements: bool = True
	) -> list[ActionResult]:
		"""Execute multiple actions"""
		results = []

		session = await browser_context.get_session()
		cached_selector_map = session.cached_state.selector_map
		cached_path_hashes = set(e.hash.branch_path_hash for e in cached_selector_map.values())
		await browser_context.remove_highlights()

		for i, action in enumerate(actions):
			if action.get_index() is not None and i != 0:
				new_state = await browser_context.get_state()
				new_path_hashes = set(e.hash.branch_path_hash for e in new_state.selector_map.values())
				if check_for_new_elements and not new_path_hashes.issubset(cached_path_hashes):
					# next action requires index but there are new elements on the page
					logger.info(f'Something new appeared after action {i} / {len(actions)}')
					break

			results.append(await self.act(action, browser_context))

			logger.debug(f'Executed action {i + 1} / {len(actions)}')
			if results[-1].is_done or results[-1].error or i == len(actions) - 1:
				break

			await asyncio.sleep(browser_context.config.wait_between_actions)
			# hash all elements. if it is a subset of cached_state its fine - else break (new elements on page)

		return results

	@time_execution_sync('--act')
	async def act(self, action: ActionModel, browser_context: BrowserContext) -> ActionResult:
		"""Execute an action"""
		try:
			for action_name, params in action.model_dump(exclude_unset=True).items():
				if params is not None:
					# remove highlights
					result = await self.registry.execute_action(action_name, params, browser=browser_context)
					if isinstance(result, str):
						return ActionResult(extracted_content=result)
					elif isinstance(result, ActionResult):
						return result
					elif result is None:
						return ActionResult()
					else:
						raise ValueError(f'Invalid action result type: {type(result)} of {result}')
			return ActionResult()
		except Exception as e:
			raise e


================================================
File: browser_use/controller/views.py
================================================
from typing import Optional

from pydantic import BaseModel, model_validator


# Action Input Models
class SearchGoogleAction(BaseModel):
	query: str


class GoToUrlAction(BaseModel):
	url: str


class ClickElementAction(BaseModel):
	index: int
	xpath: Optional[str] = None


class InputTextAction(BaseModel):
	index: int
	text: str
	xpath: Optional[str] = None


class DoneAction(BaseModel):
	text: str


class SwitchTabAction(BaseModel):
	page_id: int


class OpenTabAction(BaseModel):
	url: str


class ExtractPageContentAction(BaseModel):
	include_links: bool


class ScrollAction(BaseModel):
	amount: Optional[int] = None  # The number of pixels to scroll. If None, scroll down/up one page


class SendKeysAction(BaseModel):
	keys: str


class NoParamsAction(BaseModel):
	"""
	Accepts absolutely anything in the incoming data
	and discards it, so the final parsed model is empty.
	"""

	@model_validator(mode='before')
	def ignore_all_inputs(cls, values):
		# No matter what the user sends, discard it and return empty.
		return {}

	class Config:
		# If you want to silently allow unknown fields at top-level,
		# set extra = 'allow' as well:
		extra = 'allow'


================================================
File: browser_use/controller/registry/service.py
================================================
import asyncio
from inspect import iscoroutinefunction, signature
from typing import Any, Callable, Optional, Type

from pydantic import BaseModel, Field, create_model

from browser_use.browser.context import BrowserContext
from browser_use.controller.registry.views import (
	ActionModel,
	ActionRegistry,
	RegisteredAction,
)
from browser_use.telemetry.service import ProductTelemetry
from browser_use.telemetry.views import (
	ControllerRegisteredFunctionsTelemetryEvent,
	RegisteredFunction,
)


class Registry:
	"""Service for registering and managing actions"""

	def __init__(self, exclude_actions: list[str] = []):
		self.registry = ActionRegistry()
		self.telemetry = ProductTelemetry()
		self.exclude_actions = exclude_actions

	def _create_param_model(self, function: Callable) -> Type[BaseModel]:
		"""Creates a Pydantic model from function signature"""
		sig = signature(function)
		params = {
			name: (param.annotation, ... if param.default == param.empty else param.default)
			for name, param in sig.parameters.items()
			if name != 'browser'
		}
		# TODO: make the types here work
		return create_model(
			f'{function.__name__}_parameters',
			__base__=ActionModel,
			**params,  # type: ignore
		)

	def action(
		self,
		description: str,
		param_model: Optional[Type[BaseModel]] = None,
		requires_browser: bool = False,
	):
		"""Decorator for registering actions"""

		def decorator(func: Callable):
			# Skip registration if action is in exclude_actions
			if func.__name__ in self.exclude_actions:
				return func

			# Create param model from function if not provided
			actual_param_model = param_model or self._create_param_model(func)

			# Wrap sync functions to make them async
			if not iscoroutinefunction(func):

				async def async_wrapper(*args, **kwargs):
					return await asyncio.to_thread(func, *args, **kwargs)

				# Copy the signature and other metadata from the original function
				async_wrapper.__signature__ = signature(func)
				async_wrapper.__name__ = func.__name__
				async_wrapper.__annotations__ = func.__annotations__
				wrapped_func = async_wrapper
			else:
				wrapped_func = func

			action = RegisteredAction(
				name=func.__name__,
				description=description,
				function=wrapped_func,
				param_model=actual_param_model,
				requires_browser=requires_browser,
			)
			self.registry.actions[func.__name__] = action
			return func

		return decorator

	async def execute_action(self, action_name: str, params: dict, browser: Optional[BrowserContext] = None) -> Any:
		"""Execute a registered action"""
		if action_name not in self.registry.actions:
			raise ValueError(f'Action {action_name} not found')

		action = self.registry.actions[action_name]
		try:
			# Create the validated Pydantic model
			validated_params = action.param_model(**params)

			# Check if the first parameter is a Pydantic model
			sig = signature(action.function)
			parameters = list(sig.parameters.values())
			is_pydantic = parameters and issubclass(parameters[0].annotation, BaseModel)

			# Prepare arguments based on parameter type
			if action.requires_browser:
				if not browser:
					raise ValueError(
						f'Action {action_name} requires browser but none provided. This has to be used in combination of `requires_browser=True` when registering the action.'
					)
				if is_pydantic:
					return await action.function(validated_params, browser=browser)
				return await action.function(**validated_params.model_dump(), browser=browser)

			if is_pydantic:
				return await action.function(validated_params)
			return await action.function(**validated_params.model_dump())

		except Exception as e:
			raise RuntimeError(f'Error executing action {action_name}: {str(e)}') from e

	def create_action_model(self) -> Type[ActionModel]:
		"""Creates a Pydantic model from registered actions"""
		fields = {
			name: (
				Optional[action.param_model],
				Field(default=None, description=action.description),
			)
			for name, action in self.registry.actions.items()
		}

		self.telemetry.capture(
			ControllerRegisteredFunctionsTelemetryEvent(
				registered_functions=[
					RegisteredFunction(name=name, params=action.param_model.model_json_schema())
					for name, action in self.registry.actions.items()
				]
			)
		)

		return create_model('ActionModel', __base__=ActionModel, **fields)  # type:ignore

	def get_prompt_description(self) -> str:
		"""Get a description of all actions for the prompt"""
		return self.registry.get_prompt_description()


================================================
File: browser_use/controller/registry/views.py
================================================
from typing import Callable, Dict, Type

from pydantic import BaseModel, ConfigDict


class RegisteredAction(BaseModel):
	"""Model for a registered action"""

	name: str
	description: str
	function: Callable
	param_model: Type[BaseModel]
	requires_browser: bool = False

	model_config = ConfigDict(arbitrary_types_allowed=True)

	def prompt_description(self) -> str:
		"""Get a description of the action for the prompt"""
		skip_keys = ['title']
		s = f'{self.description}: \n'
		s += '{' + str(self.name) + ': '
		s += str(
			{
				k: {sub_k: sub_v for sub_k, sub_v in v.items() if sub_k not in skip_keys}
				for k, v in self.param_model.schema()['properties'].items()
			}
		)
		s += '}'
		return s


class ActionModel(BaseModel):
	"""Base model for dynamically created action models"""

	# this will have all the registered actions, e.g.
	# click_element = param_model = ClickElementParams
	# done = param_model = None
	#
	model_config = ConfigDict(arbitrary_types_allowed=True)

	def get_index(self) -> int | None:
		"""Get the index of the action"""
		# {'clicked_element': {'index':5}}
		params = self.model_dump(exclude_unset=True).values()
		if not params:
			return None
		for param in params:
			if param is not None and 'index' in param:
				return param['index']
		return None

	def set_index(self, index: int):
		"""Overwrite the index of the action"""
		# Get the action name and params
		action_data = self.model_dump(exclude_unset=True)
		action_name = next(iter(action_data.keys()))
		action_params = getattr(self, action_name)

		# Update the index directly on the model
		if hasattr(action_params, 'index'):
			action_params.index = index


class ActionRegistry(BaseModel):
	"""Model representing the action registry"""

	actions: Dict[str, RegisteredAction] = {}

	def get_prompt_description(self) -> str:
		"""Get a description of all actions for the prompt"""
		return '\n'.join([action.prompt_description() for action in self.actions.values()])


================================================
File: browser_use/dom/buildDomTree.js
================================================
(
    args = { doHighlightElements: true, focusHighlightIndex: -1, viewportExpansion: 0 }
) => {
    const { doHighlightElements, focusHighlightIndex, viewportExpansion } = args;
    let highlightIndex = 0; // Reset highlight index

    // Quick check to confirm the script receives focusHighlightIndex
    console.log('focusHighlightIndex:', focusHighlightIndex);

    function highlightElement(element, index, parentIframe = null) {
        // Create or get highlight container
        let container = document.getElementById('playwright-highlight-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'playwright-highlight-container';
            container.style.position = 'absolute';
            container.style.pointerEvents = 'none';
            container.style.top = '0';
            container.style.left = '0';
            container.style.width = '100%';
            container.style.height = '100%';
            container.style.zIndex = '2147483647'; // Maximum z-index value
            document.body.appendChild(container);        }

        // Generate a color based on the index
        const colors = [
            '#FF0000', '#00FF00', '#0000FF', '#FFA500',
            '#800080', '#008080', '#FF69B4', '#4B0082',
            '#FF4500', '#2E8B57', '#DC143C', '#4682B4'
        ];
        const colorIndex = index % colors.length;
        const baseColor = colors[colorIndex];
        const backgroundColor = `${baseColor}1A`; // 10% opacity version of the color

        // Create highlight overlay
        const overlay = document.createElement('div');
        overlay.style.position = 'absolute';
        overlay.style.border = `2px solid ${baseColor}`;
        overlay.style.backgroundColor = backgroundColor;
        overlay.style.pointerEvents = 'none';
        overlay.style.boxSizing = 'border-box';

        // Position overlay based on element, including scroll position
        const rect = element.getBoundingClientRect();
        let top = rect.top + window.scrollY;
        let left = rect.left + window.scrollX;

        // Adjust position if element is inside an iframe
        if (parentIframe) {
            const iframeRect = parentIframe.getBoundingClientRect();
            top += iframeRect.top;
            left += iframeRect.left;
        }

        overlay.style.top = `${top}px`;
        overlay.style.left = `${left}px`;
        overlay.style.width = `${rect.width}px`;
        overlay.style.height = `${rect.height}px`;

        // Create label
        const label = document.createElement('div');
        label.className = 'playwright-highlight-label';
        label.style.position = 'absolute';
        label.style.background = baseColor;
        label.style.color = 'white';
        label.style.padding = '1px 4px';
        label.style.borderRadius = '4px';
        label.style.fontSize = `${Math.min(12, Math.max(8, rect.height / 2))}px`; // Responsive font size
        label.textContent = index;

        // Calculate label position
        const labelWidth = 20; // Approximate width
        const labelHeight = 16; // Approximate height

        // Default position (top-right corner inside the box)
        let labelTop = top + 2;
        let labelLeft = left + rect.width - labelWidth - 2;

        // Adjust if box is too small
        if (rect.width < labelWidth + 4 || rect.height < labelHeight + 4) {
            // Position outside the box if it's too small
            labelTop = top - labelHeight - 2;
            labelLeft = left + rect.width - labelWidth;
        }


        label.style.top = `${labelTop}px`;
        label.style.left = `${labelLeft}px`;

        // Add to container
        container.appendChild(overlay);
        container.appendChild(label);

        // Store reference for cleanup
        element.setAttribute('browser-user-highlight-id', `playwright-highlight-${index}`);

        return index + 1;
    }


    // Helper function to generate XPath as a tree
    function getXPathTree(element, stopAtBoundary = true) {
        const segments = [];
        let currentElement = element;

        while (currentElement && currentElement.nodeType === Node.ELEMENT_NODE) {
            // Stop if we hit a shadow root or iframe
            if (stopAtBoundary && (currentElement.parentNode instanceof ShadowRoot || currentElement.parentNode instanceof HTMLIFrameElement)) {
                break;
            }

            let index = 0;
            let sibling = currentElement.previousSibling;
            while (sibling) {
                if (sibling.nodeType === Node.ELEMENT_NODE &&
                    sibling.nodeName === currentElement.nodeName) {
                    index++;
                }
                sibling = sibling.previousSibling;
            }

            const tagName = currentElement.nodeName.toLowerCase();
            const xpathIndex = index > 0 ? `[${index + 1}]` : '';
            segments.unshift(`${tagName}${xpathIndex}`);

            currentElement = currentElement.parentNode;
        }

        return segments.join('/');
    }

    // Helper function to check if element is accepted
    function isElementAccepted(element) {
        const leafElementDenyList = new Set(['svg', 'script', 'style', 'link', 'meta']);
        return !leafElementDenyList.has(element.tagName.toLowerCase());
    }

    // Helper function to check if element is interactive
    function isInteractiveElement(element) {
        // Base interactive elements and roles
        const interactiveElements = new Set([
            'a', 'button', 'details', 'embed', 'input', 'label',
            'menu', 'menuitem', 'object', 'select', 'textarea', 'summary'
        ]);

        const interactiveRoles = new Set([
            'button', 'menu', 'menuitem', 'link', 'checkbox', 'radio',
            'slider', 'tab', 'tabpanel', 'textbox', 'combobox', 'grid',
            'listbox', 'option', 'progressbar', 'scrollbar', 'searchbox',
            'switch', 'tree', 'treeitem', 'spinbutton', 'tooltip', 'a-button-inner', 'a-dropdown-button', 'click', 
            'menuitemcheckbox', 'menuitemradio', 'a-button-text', 'button-text', 'button-icon', 'button-icon-only', 'button-text-icon-only', 'dropdown', 'combobox'
        ]);

        const tagName = element.tagName.toLowerCase();
        const role = element.getAttribute('role');
        const ariaRole = element.getAttribute('aria-role');
        const tabIndex = element.getAttribute('tabindex');

        // Add check for specific class
        const hasAddressInputClass = element.classList.contains('address-input__container__input');

        // Basic role/attribute checks
        const hasInteractiveRole = hasAddressInputClass ||
            interactiveElements.has(tagName) ||
            interactiveRoles.has(role) ||
            interactiveRoles.has(ariaRole) ||
            (tabIndex !== null && tabIndex !== '-1') ||
            element.getAttribute('data-action') === 'a-dropdown-select' ||
            element.getAttribute('data-action') === 'a-dropdown-button';

        if (hasInteractiveRole) return true;

        // Get computed style
        const style = window.getComputedStyle(element);

        // Check if element has click-like styling
        // const hasClickStyling = style.cursor === 'pointer' ||
        //     element.style.cursor === 'pointer' ||
        //     style.pointerEvents !== 'none';

        // Check for event listeners
        const hasClickHandler = element.onclick !== null ||
            element.getAttribute('onclick') !== null ||
            element.hasAttribute('ng-click') ||
            element.hasAttribute('@click') ||
            element.hasAttribute('v-on:click');

        // Helper function to safely get event listeners
        function getEventListeners(el) {
            try {
                // Try to get listeners using Chrome DevTools API
                return window.getEventListeners?.(el) || {};
            } catch (e) {
                // Fallback: check for common event properties
                const listeners = {};

                // List of common event types to check
                const eventTypes = [
                    'click', 'mousedown', 'mouseup',
                    'touchstart', 'touchend',
                    'keydown', 'keyup', 'focus', 'blur'
                ];

                for (const type of eventTypes) {
                    const handler = el[`on${type}`];
                    if (handler) {
                        listeners[type] = [{
                            listener: handler,
                            useCapture: false
                        }];
                    }
                }

                return listeners;
            }
        }

        // Check for click-related events on the element itself
        const listeners = getEventListeners(element);
        const hasClickListeners = listeners && (
            listeners.click?.length > 0 ||
            listeners.mousedown?.length > 0 ||
            listeners.mouseup?.length > 0 ||
            listeners.touchstart?.length > 0 ||
            listeners.touchend?.length > 0
        );

        // Check for ARIA properties that suggest interactivity
        const hasAriaProps = element.hasAttribute('aria-expanded') ||
            element.hasAttribute('aria-pressed') ||
            element.hasAttribute('aria-selected') ||
            element.hasAttribute('aria-checked');

        // Check for form-related functionality
        const isFormRelated = element.form !== undefined ||
            element.hasAttribute('contenteditable') ||
            style.userSelect !== 'none';

        // Check if element is draggable
        const isDraggable = element.draggable ||
            element.getAttribute('draggable') === 'true';

        return hasAriaProps ||
            // hasClickStyling ||
            hasClickHandler ||
            hasClickListeners ||
            // isFormRelated ||
            isDraggable;

    }

    // Helper function to check if element is visible
    function isElementVisible(element) {
        const style = window.getComputedStyle(element);
        return element.offsetWidth > 0 &&
            element.offsetHeight > 0 &&
            style.visibility !== 'hidden' &&
            style.display !== 'none';
    }

    // Helper function to check if element is the top element at its position
    function isTopElement(element) {
        // Find the correct document context and root element
        let doc = element.ownerDocument;

        // If we're in an iframe, elements are considered top by default
        if (doc !== window.document) {
            return true;
        }

        // For shadow DOM, we need to check within its own root context
        const shadowRoot = element.getRootNode();
        if (shadowRoot instanceof ShadowRoot) {
            const rect = element.getBoundingClientRect();
            const point = { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };

            try {
                // Use shadow root's elementFromPoint to check within shadow DOM context
                const topEl = shadowRoot.elementFromPoint(point.x, point.y);
                if (!topEl) return false;

                // Check if the element or any of its parents match our target element
                let current = topEl;
                while (current && current !== shadowRoot) {
                    if (current === element) return true;
                    current = current.parentElement;
                }
                return false;
            } catch (e) {
                return true; // If we can't determine, consider it visible
            }
        }

        // Regular DOM elements
        const rect = element.getBoundingClientRect();

        // If viewportExpansion is -1, check if element is the top one at its position
        if (viewportExpansion === -1) {
            return true; // Consider all elements as top elements when expansion is -1
        }

        // Calculate expanded viewport boundaries including scroll position
        const scrollX = window.scrollX;
        const scrollY = window.scrollY;
        const viewportTop = -viewportExpansion + scrollY;
        const viewportLeft = -viewportExpansion + scrollX;
        const viewportBottom = window.innerHeight + viewportExpansion + scrollY;
        const viewportRight = window.innerWidth + viewportExpansion + scrollX;

        // Get absolute element position
        const absTop = rect.top + scrollY;
        const absLeft = rect.left + scrollX;
        const absBottom = rect.bottom + scrollY;
        const absRight = rect.right + scrollX;

        // Skip if element is completely outside expanded viewport
        if (absBottom < viewportTop || 
            absTop > viewportBottom || 
            absRight < viewportLeft || 
            absLeft > viewportRight) {
            return false;
        }

        // For elements within expanded viewport, check if they're the top element
        try {
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            
            // Only clamp the point if it's outside the actual document
            const point = {
                x: centerX,
                y: centerY
            };
            
            if (point.x < 0 || point.x >= window.innerWidth || 
                point.y < 0 || point.y >= window.innerHeight) {
                return true; // Consider elements with center outside viewport as visible
            }

            const topEl = document.elementFromPoint(point.x, point.y);
            if (!topEl) return false;

            let current = topEl;
            while (current && current !== document.documentElement) {
                if (current === element) return true;
                current = current.parentElement;
            }
            return false;
        } catch (e) {
            return true;
        }
    }

    // Helper function to check if text node is visible
    function isTextNodeVisible(textNode) {
        const range = document.createRange();
        range.selectNodeContents(textNode);
        const rect = range.getBoundingClientRect();

        return rect.width !== 0 &&
            rect.height !== 0 &&
            rect.top >= 0 &&
            rect.top <= window.innerHeight &&
            textNode.parentElement?.checkVisibility({
                checkOpacity: true,
                checkVisibilityCSS: true
            });
    }


    // Function to traverse the DOM and create nested JSON
    function buildDomTree(node, parentIframe = null) {
        if (!node) return null;

        // Special case for text nodes
        if (node.nodeType === Node.TEXT_NODE) {
            const textContent = node.textContent.trim();
            if (textContent && isTextNodeVisible(node)) {
                return {
                    type: "TEXT_NODE",
                    text: textContent,
                    isVisible: true,
                };
            }
            return null;
        }

        // Check if element is accepted
        if (node.nodeType === Node.ELEMENT_NODE && !isElementAccepted(node)) {
            return null;
        }

        const nodeData = {
            tagName: node.tagName ? node.tagName.toLowerCase() : null,
            attributes: {},
            xpath: node.nodeType === Node.ELEMENT_NODE ? getXPathTree(node, true) : null,
            children: [],
        };

        // Copy all attributes if the node is an element
        if (node.nodeType === Node.ELEMENT_NODE && node.attributes) {
            // Use getAttributeNames() instead of directly iterating attributes
            const attributeNames = node.getAttributeNames?.() || [];
            for (const name of attributeNames) {
                nodeData.attributes[name] = node.getAttribute(name);
            }
        }

        if (node.nodeType === Node.ELEMENT_NODE) {
            const isInteractive = isInteractiveElement(node);
            const isVisible = isElementVisible(node);
            const isTop = isTopElement(node);

            nodeData.isInteractive = isInteractive;
            nodeData.isVisible = isVisible;
            nodeData.isTopElement = isTop;

            // Highlight if element meets all criteria and highlighting is enabled
            if (isInteractive && isVisible && isTop) {
                nodeData.highlightIndex = highlightIndex++;
                if (doHighlightElements) {
                    if(focusHighlightIndex >= 0){
                        if(focusHighlightIndex === nodeData.highlightIndex){
                            highlightElement(node, nodeData.highlightIndex, parentIframe);
                        }
                    } else {
                        highlightElement(node, nodeData.highlightIndex, parentIframe);
                    }
                }
            }
        }

        // Only add iframeContext if we're inside an iframe
        // if (parentIframe) {
        //     nodeData.iframeContext = `iframe[src="${parentIframe.src || ''}"]`;
        // }

        // Only add shadowRoot field if it exists
        if (node.shadowRoot) {
            nodeData.shadowRoot = true;
        }

        // Handle shadow DOM
        if (node.shadowRoot) {
            const shadowChildren = Array.from(node.shadowRoot.childNodes).map(child =>
                buildDomTree(child, parentIframe)
            );
            nodeData.children.push(...shadowChildren);
        }

        // Handle iframes
        if (node.tagName === 'IFRAME') {
            try {
                const iframeDoc = node.contentDocument || node.contentWindow.document;
                if (iframeDoc) {
                    const iframeChildren = Array.from(iframeDoc.body.childNodes).map(child =>
                        buildDomTree(child, node)
                    );
                    nodeData.children.push(...iframeChildren);
                }
            } catch (e) {
                console.warn('Unable to access iframe:', node);
            }
        } else {
            const children = Array.from(node.childNodes).map(child =>
                buildDomTree(child, parentIframe)
            );
            nodeData.children.push(...children);
        }

        return nodeData;
    }


    return buildDomTree(document.body);
}


================================================
File: browser_use/dom/service.py
================================================
import logging
from importlib import resources
from typing import Optional

from playwright.async_api import Page

from browser_use.dom.views import (
	DOMBaseNode,
	DOMElementNode,
	DOMState,
	DOMTextNode,
	SelectorMap,
)

logger = logging.getLogger(__name__)


class DomService:
	def __init__(self, page: Page):
		self.page = page
		self.xpath_cache = {}

	# region - Clickable elements
	async def get_clickable_elements(
		self,
		highlight_elements: bool = True,
		focus_element: int = -1,
		viewport_expansion: int = 0,
	) -> DOMState:
		element_tree = await self._build_dom_tree(highlight_elements, focus_element, viewport_expansion)
		selector_map = self._create_selector_map(element_tree)

		return DOMState(element_tree=element_tree, selector_map=selector_map)

	async def _build_dom_tree(
		self,
		highlight_elements: bool,
		focus_element: int,
		viewport_expansion: int,
	) -> DOMElementNode:
		js_code = resources.read_text('browser_use.dom', 'buildDomTree.js')

		args = {
			'doHighlightElements': highlight_elements,
			'focusHighlightIndex': focus_element,
			'viewportExpansion': viewport_expansion,
		}

		eval_page = await self.page.evaluate(js_code, args)  # This is quite big, so be careful
		html_to_dict = self._parse_node(eval_page)

		if html_to_dict is None or not isinstance(html_to_dict, DOMElementNode):
			raise ValueError('Failed to parse HTML to dictionary')

		return html_to_dict

	def _create_selector_map(self, element_tree: DOMElementNode) -> SelectorMap:
		selector_map = {}

		def process_node(node: DOMBaseNode):
			if isinstance(node, DOMElementNode):
				if node.highlight_index is not None:
					selector_map[node.highlight_index] = node

				for child in node.children:
					process_node(child)

		process_node(element_tree)
		return selector_map

	def _parse_node(
		self,
		node_data: dict,
		parent: Optional[DOMElementNode] = None,
	) -> Optional[DOMBaseNode]:
		if not node_data:
			return None

		if node_data.get('type') == 'TEXT_NODE':
			text_node = DOMTextNode(
				text=node_data['text'],
				is_visible=node_data['isVisible'],
				parent=parent,
			)

			return text_node

		tag_name = node_data['tagName']

		element_node = DOMElementNode(
			tag_name=tag_name,
			xpath=node_data['xpath'],
			attributes=node_data.get('attributes', {}),
			children=[],  # Initialize empty, will fill later
			is_visible=node_data.get('isVisible', False),
			is_interactive=node_data.get('isInteractive', False),
			is_top_element=node_data.get('isTopElement', False),
			highlight_index=node_data.get('highlightIndex'),
			shadow_root=node_data.get('shadowRoot', False),
			parent=parent,
		)

		children: list[DOMBaseNode] = []
		for child in node_data.get('children', []):
			if child is not None:
				child_node = self._parse_node(child, parent=element_node)
				if child_node is not None:
					children.append(child_node)

		element_node.children = children

		return element_node

	# endregion


================================================
File: browser_use/dom/views.py
================================================
from dataclasses import dataclass
from functools import cached_property
from typing import TYPE_CHECKING, Dict, List, Optional

from browser_use.dom.history_tree_processor.view import HashedDomElement

# Avoid circular import issues
if TYPE_CHECKING:
	from .views import DOMElementNode


@dataclass(frozen=False)
class DOMBaseNode:
	is_visible: bool
	# Use None as default and set parent later to avoid circular reference issues
	parent: Optional['DOMElementNode']


@dataclass(frozen=False)
class DOMTextNode(DOMBaseNode):
	text: str
	type: str = 'TEXT_NODE'

	def has_parent_with_highlight_index(self) -> bool:
		current = self.parent
		while current is not None:
			if current.highlight_index is not None:
				return True
			current = current.parent
		return False


@dataclass(frozen=False)
class DOMElementNode(DOMBaseNode):
	"""
	xpath: the xpath of the element from the last root node (shadow root or iframe OR document if no shadow root or iframe).
	To properly reference the element we need to recursively switch the root node until we find the element (work you way up the tree with `.parent`)
	"""

	tag_name: str
	xpath: str
	attributes: Dict[str, str]
	children: List[DOMBaseNode]
	is_interactive: bool = False
	is_top_element: bool = False
	shadow_root: bool = False
	highlight_index: Optional[int] = None

	def __repr__(self) -> str:
		tag_str = f'<{self.tag_name}'

		# Add attributes
		for key, value in self.attributes.items():
			tag_str += f' {key}="{value}"'
		tag_str += '>'

		# Add extra info
		extras = []
		if self.is_interactive:
			extras.append('interactive')
		if self.is_top_element:
			extras.append('top')
		if self.shadow_root:
			extras.append('shadow-root')
		if self.highlight_index is not None:
			extras.append(f'highlight:{self.highlight_index}')

		if extras:
			tag_str += f' [{", ".join(extras)}]'

		return tag_str

	@cached_property
	def hash(self) -> HashedDomElement:
		from browser_use.dom.history_tree_processor.service import (
			HistoryTreeProcessor,
		)

		return HistoryTreeProcessor._hash_dom_element(self)

	def get_all_text_till_next_clickable_element(self, max_depth: int = -1) -> str:
		text_parts = []

		def collect_text(node: DOMBaseNode, current_depth: int) -> None:
			if max_depth != -1 and current_depth > max_depth:
				return

			# Skip this branch if we hit a highlighted element (except for the current node)
			if (
				isinstance(node, DOMElementNode)
				and node != self
				and node.highlight_index is not None
			):
				return

			if isinstance(node, DOMTextNode):
				text_parts.append(node.text)
			elif isinstance(node, DOMElementNode):
				for child in node.children:
					collect_text(child, current_depth + 1)

		collect_text(self, 0)
		return '\n'.join(text_parts).strip()

	def clickable_elements_to_string(self, include_attributes: list[str] = []) -> str:
		"""Convert the processed DOM content to HTML."""
		formatted_text = []

		def process_node(node: DOMBaseNode, depth: int) -> None:
			if isinstance(node, DOMElementNode):
				# Add element with highlight_index
				if node.highlight_index is not None:
					attributes_str = ''
					if include_attributes:
						attributes_str = ' ' + ' '.join(
							f'{key}="{value}"'
							for key, value in node.attributes.items()
							if key in include_attributes
						)
					formatted_text.append(
						f'{node.highlight_index}[:]<{node.tag_name}{attributes_str}>{node.get_all_text_till_next_clickable_element()}</{node.tag_name}>'
					)

				# Process children regardless
				for child in node.children:
					process_node(child, depth + 1)

			elif isinstance(node, DOMTextNode):
				# Add text only if it doesn't have a highlighted parent
				if not node.has_parent_with_highlight_index():
					formatted_text.append(f'_[:]{node.text}')

		process_node(self, 0)
		return '\n'.join(formatted_text)

	def get_file_upload_element(self, check_siblings: bool = True) -> Optional['DOMElementNode']:
		# Check if current element is a file input
		if self.tag_name == 'input' and self.attributes.get('type') == 'file':
			return self

		# Check children
		for child in self.children:
			if isinstance(child, DOMElementNode):
				result = child.get_file_upload_element(check_siblings=False)
				if result:
					return result

		# Check siblings only for the initial call
		if check_siblings and self.parent:
			for sibling in self.parent.children:
				if sibling is not self and isinstance(sibling, DOMElementNode):
					result = sibling.get_file_upload_element(check_siblings=False)
					if result:
						return result

		return None


class ElementTreeSerializer:
	@staticmethod
	def serialize_clickable_elements(element_tree: DOMElementNode) -> str:
		return element_tree.clickable_elements_to_string()

	@staticmethod
	def dom_element_node_to_json(element_tree: DOMElementNode) -> dict:
		def node_to_dict(node: DOMBaseNode) -> dict:
			if isinstance(node, DOMTextNode):
				return {'type': 'text', 'text': node.text}
			elif isinstance(node, DOMElementNode):
				return {
					'type': 'element',
					'tag_name': node.tag_name,
					'attributes': node.attributes,
					'highlight_index': node.highlight_index,
					'children': [node_to_dict(child) for child in node.children],
				}
			return {}

		return node_to_dict(element_tree)


SelectorMap = dict[int, DOMElementNode]


@dataclass
class DOMState:
	element_tree: DOMElementNode
	selector_map: SelectorMap


================================================
File: browser_use/dom/history_tree_processor/service.py
================================================
import hashlib
from dataclasses import dataclass
from typing import Optional

from browser_use.dom.history_tree_processor.view import DOMHistoryElement, HashedDomElement
from browser_use.dom.views import DOMElementNode


class HistoryTreeProcessor:
	""" "
	Operations on the DOM elements

	@dev be careful - text nodes can change even if elements stay the same
	"""

	@staticmethod
	def convert_dom_element_to_history_element(dom_element: DOMElementNode) -> DOMHistoryElement:
		parent_branch_path = HistoryTreeProcessor._get_parent_branch_path(dom_element)
		return DOMHistoryElement(
			dom_element.tag_name,
			dom_element.xpath,
			dom_element.highlight_index,
			parent_branch_path,
			dom_element.attributes,
			dom_element.shadow_root,
		)

	@staticmethod
	def find_history_element_in_tree(
		dom_history_element: DOMHistoryElement, tree: DOMElementNode
	) -> Optional[DOMElementNode]:
		hashed_dom_history_element = HistoryTreeProcessor._hash_dom_history_element(
			dom_history_element
		)

		def process_node(node: DOMElementNode):
			if node.highlight_index is not None:
				hashed_node = HistoryTreeProcessor._hash_dom_element(node)
				if hashed_node == hashed_dom_history_element:
					return node
			for child in node.children:
				if isinstance(child, DOMElementNode):
					result = process_node(child)
					if result is not None:
						return result
			return None

		return process_node(tree)

	@staticmethod
	def compare_history_element_and_dom_element(
		dom_history_element: DOMHistoryElement, dom_element: DOMElementNode
	) -> bool:
		hashed_dom_history_element = HistoryTreeProcessor._hash_dom_history_element(
			dom_history_element
		)
		hashed_dom_element = HistoryTreeProcessor._hash_dom_element(dom_element)

		return hashed_dom_history_element == hashed_dom_element

	@staticmethod
	def _hash_dom_history_element(dom_history_element: DOMHistoryElement) -> HashedDomElement:
		branch_path_hash = HistoryTreeProcessor._parent_branch_path_hash(
			dom_history_element.entire_parent_branch_path
		)
		attributes_hash = HistoryTreeProcessor._attributes_hash(dom_history_element.attributes)

		return HashedDomElement(branch_path_hash, attributes_hash)

	@staticmethod
	def _hash_dom_element(dom_element: DOMElementNode) -> HashedDomElement:
		parent_branch_path = HistoryTreeProcessor._get_parent_branch_path(dom_element)
		branch_path_hash = HistoryTreeProcessor._parent_branch_path_hash(parent_branch_path)
		attributes_hash = HistoryTreeProcessor._attributes_hash(dom_element.attributes)
		# text_hash = DomTreeProcessor._text_hash(dom_element)

		return HashedDomElement(branch_path_hash, attributes_hash)

	@staticmethod
	def _get_parent_branch_path(dom_element: DOMElementNode) -> list[str]:
		parents: list[DOMElementNode] = []
		current_element: DOMElementNode = dom_element
		while current_element.parent is not None:
			parents.append(current_element)
			current_element = current_element.parent

		parents.reverse()

		return [parent.tag_name for parent in parents]

	@staticmethod
	def _parent_branch_path_hash(parent_branch_path: list[str]) -> str:
		parent_branch_path_string = '/'.join(parent_branch_path)
		return hashlib.sha256(parent_branch_path_string.encode()).hexdigest()

	@staticmethod
	def _attributes_hash(attributes: dict[str, str]) -> str:
		attributes_string = ''.join(f'{key}={value}' for key, value in attributes.items())
		return hashlib.sha256(attributes_string.encode()).hexdigest()

	@staticmethod
	def _text_hash(dom_element: DOMElementNode) -> str:
		""" """
		text_string = dom_element.get_all_text_till_next_clickable_element()
		return hashlib.sha256(text_string.encode()).hexdigest()


================================================
File: browser_use/dom/history_tree_processor/view.py
================================================
from dataclasses import dataclass
from typing import Optional


@dataclass
class HashedDomElement:
	"""
	Hash of the dom element to be used as a unique identifier
	"""

	branch_path_hash: str
	attributes_hash: str
	# text_hash: str


@dataclass
class DOMHistoryElement:
	tag_name: str
	xpath: str
	highlight_index: Optional[int]
	entire_parent_branch_path: list[str]
	attributes: dict[str, str]
	shadow_root: bool = False

	def to_dict(self) -> dict:
		return {
			'tag_name': self.tag_name,
			'xpath': self.xpath,
			'highlight_index': self.highlight_index,
			'entire_parent_branch_path': self.entire_parent_branch_path,
			'attributes': self.attributes,
			'shadow_root': self.shadow_root,
		}


================================================
File: browser_use/dom/tests/extraction_test.py
================================================
import asyncio
import time

from tokencost import count_string_tokens

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.dom.service import DomService
from browser_use.utils import time_execution_sync


async def test_process_html_file():
	browser = Browser(config=BrowserConfig(headless=False))

	websites = [
		'https://kayak.com/flights',
		'https://immobilienscout24.de',
		'https://google.com',
		'https://amazon.com',
		'https://github.com',
	]

	async with await browser.new_context() as context:
		page = await context.get_current_page()
		dom_service = DomService(page)

		for website in websites:
			print(f'\n{"=" * 50}\nTesting {website}\n{"=" * 50}')
			await page.goto(website)
			time.sleep(2)  # Additional wait for dynamic content

			async def test_viewport(expansion: int, description: str):
				print(f'\n{description}:')
				dom_state = await time_execution_sync(f'get_clickable_elements ({description})')(
					dom_service.get_clickable_elements
				)(highlight_elements=True, viewport_expansion=expansion)

				elements = dom_state.element_tree
				selector_map = dom_state.selector_map
				element_count = len(selector_map.keys())
				token_count = count_string_tokens(elements.clickable_elements_to_string(), model='gpt-4o')

				print(f'Number of elements: {element_count}')
				print(f'Token count: {token_count}')
				return element_count, token_count

			expansions = [0, 100, 200, 300, 400, 500, 600, 1000, -1, -200]
			results = []

			for i, expansion in enumerate(expansions):
				description = (
					f'{i + 1}. Expansion {expansion}px' if expansion >= 0 else f'{i + 1}. All elements ({expansion} expansion)'
				)
				count, tokens = await test_viewport(expansion, description)
				results.append((count, tokens))
				input('Press Enter to continue...')
				await page.evaluate('document.getElementById("playwright-highlight-container")?.remove()')

			# Print comparison summary
			print('\nComparison Summary:')
			for i, (count, tokens) in enumerate(results):
				expansion = expansions[i]
				description = f'Expansion {expansion}px' if expansion >= 0 else 'All elements (-1)'
				initial_count, initial_tokens = results[0]
				print(f'{description}: {count} elements (+{count - initial_count}), {tokens} tokens')

			input('\nPress Enter to continue to next website...')

			# Clear highlights before next website
			await page.evaluate('document.getElementById("playwright-highlight-container")?.remove()')


async def test_focus_vs_all_elements():
	browser = Browser(config=BrowserConfig(headless=False))

	websites = [
		'https://google.com',  # Simple UI
		'https://amazon.com',  # Complex UI
	]

	async with await browser.new_context() as context:
		page = await context.get_current_page()
		dom_service = DomService(page)

		for website in websites:
			print(f'\n{"=" * 50}\nTesting {website}\n{"=" * 50}')
			await page.goto(website)
			time.sleep(2)  # Additional wait for dynamic content

			# First get all elements
			print('\nGetting all elements:')
			all_elements_state = await time_execution_sync('get_all_elements')(dom_service.get_clickable_elements)(
				highlight_elements=True, viewport_expansion=0
			)

			selector_map = all_elements_state.selector_map
			total_elements = len(selector_map.keys())
			print(f'Total number of elements: {total_elements}')

			answer = input('Which element do you want to focus on? (Enter index): ')
			await page.evaluate('document.getElementById("playwright-highlight-container")?.remove()')

			focus_element = int(answer)
			focus_state = await time_execution_sync('get_focused_element')(dom_service.get_clickable_elements)(
				highlight_elements=True, focus_element=focus_element, viewport_expansion=0
			)
			focus_selector_map = focus_state.selector_map
			focus_element_count = len(focus_selector_map.keys())
			print(f'Number of highlighted elements when focused: {focus_element_count}')

			input('Press Enter to clear highlights and continue...')
			await page.evaluate('document.getElementById("playwright-highlight-container")?.remove()')


if __name__ == '__main__':
	asyncio.run(test_focus_vs_all_elements())
	asyncio.run(test_process_html_file())


================================================
File: browser_use/dom/tests/process_dom_test.py
================================================
import json
import os
import time

from browser_use.browser.browser import Browser, BrowserConfig


async def test_process_dom():
	browser = Browser(config=BrowserConfig(headless=False))

	async with await browser.new_context() as context:
		page = await context.get_current_page()
		await page.goto('https://kayak.com/flights')
		# await page.goto('https://google.com/flights')
		# await page.goto('https://immobilienscout24.de')
		# await page.goto('https://seleniumbase.io/w3schools/iframes')

		time.sleep(3)

		with open('browser_use/dom/buildDomTree.js', 'r') as f:
			js_code = f.read()

		start = time.time()
		dom_tree = await page.evaluate(js_code)
		end = time.time()

		# print(dom_tree)
		print(f'Time: {end - start:.2f}s')

		os.makedirs('./tmp', exist_ok=True)
		with open('./tmp/dom.json', 'w') as f:
			json.dump(dom_tree, f, indent=1)

		# both of these work for immobilienscout24.de
		# await page.click('.sc-dcJsrY.ezjNCe')
		# await page.click(
		# 	'div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > button:nth-of-type(2)'
		# )

		input('Press Enter to continue...')


================================================
File: browser_use/telemetry/service.py
================================================
import logging
import os
import uuid
from pathlib import Path

from dotenv import load_dotenv
from posthog import Posthog

from browser_use.telemetry.views import BaseTelemetryEvent
from browser_use.utils import singleton

load_dotenv()


logger = logging.getLogger(__name__)


POSTHOG_EVENT_SETTINGS = {
	'process_person_profile': True,
}


@singleton
class ProductTelemetry:
	"""
	Service for capturing anonymized telemetry data.

	If the environment variable `ANONYMIZED_TELEMETRY=False`, anonymized telemetry will be disabled.
	"""

	USER_ID_PATH = str(Path.home() / '.cache' / 'browser_use' / 'telemetry_user_id')
	PROJECT_API_KEY = 'phc_F8JMNjW1i2KbGUTaW1unnDdLSPCoyc52SGRU0JecaUh'
	HOST = 'https://eu.i.posthog.com'
	UNKNOWN_USER_ID = 'UNKNOWN'

	_curr_user_id = None

	def __init__(self) -> None:
		telemetry_disabled = os.getenv('ANONYMIZED_TELEMETRY', 'true').lower() == 'false'
		self.debug_logging = os.getenv('BROWSER_USE_LOGGING_LEVEL', 'info').lower() == 'debug'

		if telemetry_disabled:
			self._posthog_client = None
		else:
			logging.info(
				'Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.'
			)
			self._posthog_client = Posthog(
				project_api_key=self.PROJECT_API_KEY,
				host=self.HOST,
				disable_geoip=False,
			)

			# Silence posthog's logging
			if not self.debug_logging:
				posthog_logger = logging.getLogger('posthog')
				posthog_logger.disabled = True

		if self._posthog_client is None:
			logger.debug('Telemetry disabled')

	def capture(self, event: BaseTelemetryEvent) -> None:
		if self._posthog_client is None:
			return

		if self.debug_logging:
			logger.debug(f'Telemetry event: {event.name} {event.properties}')
		self._direct_capture(event)

	def _direct_capture(self, event: BaseTelemetryEvent) -> None:
		"""
		Should not be thread blocking because posthog magically handles it
		"""
		if self._posthog_client is None:
			return

		try:
			self._posthog_client.capture(
				self.user_id,
				event.name,
				{**event.properties, **POSTHOG_EVENT_SETTINGS},
			)
		except Exception as e:
			logger.error(f'Failed to send telemetry event {event.name}: {e}')

	@property
	def user_id(self) -> str:
		if self._curr_user_id:
			return self._curr_user_id

		# File access may fail due to permissions or other reasons. We don't want to
		# crash so we catch all exceptions.
		try:
			if not os.path.exists(self.USER_ID_PATH):
				os.makedirs(os.path.dirname(self.USER_ID_PATH), exist_ok=True)
				with open(self.USER_ID_PATH, 'w') as f:
					new_user_id = str(uuid.uuid4())
					f.write(new_user_id)
				self._curr_user_id = new_user_id
			else:
				with open(self.USER_ID_PATH, 'r') as f:
					self._curr_user_id = f.read()
		except Exception:
			self._curr_user_id = 'UNKNOWN_USER_ID'
		return self._curr_user_id


================================================
File: browser_use/telemetry/views.py
================================================
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional

from browser_use.controller.registry.views import ActionModel


@dataclass
class BaseTelemetryEvent(ABC):
	@property
	@abstractmethod
	def name(self) -> str:
		pass

	@property
	def properties(self) -> Dict[str, Any]:
		return {k: v for k, v in asdict(self).items() if k != 'name'}


@dataclass
class RegisteredFunction:
	name: str
	params: dict[str, Any]


@dataclass
class ControllerRegisteredFunctionsTelemetryEvent(BaseTelemetryEvent):
	registered_functions: list[RegisteredFunction]
	name: str = 'controller_registered_functions'


@dataclass
class AgentStepTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	step: int
	step_error: list[str]
	consecutive_failures: int
	actions: list[dict]
	name: str = 'agent_step'


@dataclass
class AgentRunTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	use_vision: bool
	task: str
	model_name: str
	chat_model_library: str
	version: str
	source: str
	name: str = 'agent_run'


@dataclass
class AgentEndTelemetryEvent(BaseTelemetryEvent):
	agent_id: str
	steps: int
	max_steps_reached: bool
	success: bool
	errors: list[str]
	name: str = 'agent_end'


================================================
File: docs/README.md
================================================
# Docs

The official documentation for Browser Use. The docs are published to [Browser Use Docs](https://docs.browser-use.com).

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where mint.json is)

```
mintlify dev
```


================================================
File: docs/development.mdx
================================================
---
title: 'Development'
description: 'Preview changes locally to update your docs'
---

<Info>
  **Prerequisite**: Please install Node.js (version 19 or higher) before proceeding.
</Info>

Follow these steps to install and run Mintlify on your operating system:

**Step 1**: Install Mintlify:

<CodeGroup>

  ```bash npm
  npm i -g mintlify
  ```

```bash yarn
yarn global add mintlify
```

</CodeGroup>

**Step 2**: Navigate to the docs directory (where the `mint.json` file is located) and execute the following command:

```bash
mintlify dev
```

A local preview of your documentation will be available at `http://localhost:3000`.

### Custom Ports

By default, Mintlify uses port 3000. You can customize the port Mintlify runs on by using the `--port` flag. To run Mintlify on port 3333, for instance, use this command:

```bash
mintlify dev --port 3333
```

If you attempt to run Mintlify on a port that's already in use, it will use the next available port:

```md
Port 3000 is already in use. Trying 3001 instead.
```

## Mintlify Versions

Please note that each CLI release is associated with a specific version of Mintlify. If your local website doesn't align with the production version, please update the CLI:

<CodeGroup>

```bash npm
npm i -g mintlify@latest
```

```bash yarn
yarn global upgrade mintlify
```

</CodeGroup>

## Validating Links

The CLI can assist with validating reference links made in your documentation. To identify any broken links, use the following command:

```bash
mintlify broken-links
```

## Deployment

<Tip>
  Unlimited editors available under the [Pro
  Plan](https://mintlify.com/pricing) and above.
</Tip>

If the deployment is successful, you should see the following:

<Frame>
  <img src="/images/checks-passed.png" style={{ borderRadius: '0.5rem' }} />
</Frame>

## Code Formatting

We suggest using extensions on your IDE to recognize and format MDX. If you're a VSCode user, consider the [MDX VSCode extension](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx) for syntax highlighting, and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) for code formatting.

## Troubleshooting

<AccordionGroup>
  <Accordion title='Error: Could not load the "sharp" module using the darwin-arm64 runtime'>

    This may be due to an outdated version of node. Try the following:
    1. Remove the currently-installed version of mintlify: `npm remove -g mintlify`
    2. Upgrade to Node v19 or higher.
    3. Reinstall mintlify: `npm install -g mintlify`
  </Accordion>

  <Accordion title="Issue: Encountering an unknown error">
  
    Solution: Go to the root of your device and delete the \~/.mintlify folder. Afterwards, run `mintlify dev` again.
  </Accordion>
</AccordionGroup>

Curious about what changed in the CLI version? [Check out the CLI changelog.](https://www.npmjs.com/package/mintlify?activeTab=versions)


================================================
File: docs/introduction.mdx
================================================
---
title: "Introduction"
description: "Welcome to Browser Use - We enable AI to control your browser"
icon: "book-open"
---

<img className="block" src="/images/browser-use.png" alt="Browser Use" />

## Overview

Browser Use is the easiest way to connect your AI agents with the browser. It makes websites accessible for AI agents by providing a powerful, yet simple interface for browser automation.

<Note>
  If you have used Browser Use for your project, feel free to show it off in our
  [Discord community](https://link.browser-use.com/discord)!
</Note>

## Getting Started

<CardGroup cols={2}>
  <Card title="Quick Start" icon="rocket" href="/quickstart">
    Get up and running with Browser Use in minutes
  </Card>
  <Card
    title="Supported Models"
    icon="robot"
    href="/customize/supported-models"
  >
    Configure different LLMs for your agents
  </Card>
  <Card title="Agent Settings" icon="gear" href="/customize/agent-settings">
    Learn how to configure and customize your agents
  </Card>
  <Card title="Custom Functions" icon="code" href="/customize/custom-functions">
    Extend functionality with custom actions
  </Card>
</CardGroup>

## Fancy Demos

### Writing in Google Docs

Task: Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.

<Frame>
  <img src="https://github.com/user-attachments/assets/242ade3e-15bc-41c2-988f-cbc5415a66aa" />
</Frame>

### Job Applications

Task: Read my CV & find ML jobs, save them to a file, and then start applying for them in new tabs.

<Frame>
  <video
    controls
    src="https://github.com/user-attachments/assets/171fb4d6-0355-46f2-863e-edb04a828d04"
  />
</Frame>

### Flight Search

Task: Find flights on kayak.com from Zurich to Beijing.

<Frame>
  <img src="https://github.com/user-attachments/assets/ea605d4a-90e6-481e-a569-f0e0db7e6390" />
</Frame>

### Data Collection

Task: Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging Face, save top 5 to file.

<Frame>
  <video
    controls
    src="https://github.com/user-attachments/assets/de73ee39-432c-4b97-b4e8-939fd7f323b3"
  />
</Frame>

## Community & Support

<CardGroup cols={2}>
  <Card
    title="Join Discord"
    icon="discord"
    href="https://link.browser-use.com/discord"
  >
    Join our community for support and showcases
  </Card>
  <Card
    title="GitHub"
    icon="github"
    href="https://github.com/browser-use/browser-use"
  >
    Star us on GitHub and contribute to development
  </Card>
</CardGroup>

<Note>
  Browser Use is MIT licensed and actively maintained. We welcome contributions
  and feedback from the community!
</Note>


================================================
File: docs/mint.json
================================================
{
  "$schema": "https://mintlify.com/schema.json",
  "name": "Browser Use",
  "logo": {
    "dark": "/logo/dark.svg",
    "light": "/logo/light.svg",
    "href": "https://browser-use.com"
  },
  "favicon": "/favicon.svg",
  "colors": {
    "primary": "#F97316",
    "light": "#FFF7ED",
    "dark": "#C2410C",
    "anchors": {
      "from": "#F97316",
      "to": "#FB923C"
    }
  },
  "feedback": {
    "thumbsRating": true,
    "raiseIssue": true,
    "suggestEdit": true
  },
  "topbarLinks": [
    {
      "name": "Github",
      "url": "https://github.com/browser-use/browser-use"
    },
    {
      "name": "Twitter",
      "url": "https://x.com/gregpr07"
    }
  ],
  "topbarCtaButton": {
    "name": "Join Discord",
    "url": "https://link.browser-use.com/discord"
  },
  "navigation": [
    {
      "group": "Get Started",
      "pages": [
        "introduction",
        "quickstart"
      ]
    },
    {
      "group": "Customize",
      "pages": [
        "customize/supported-models",
        "customize/agent-settings",
        "customize/browser-settings",
        "customize/real-browser",
        "customize/output-format",
        "customize/system-prompt",
        "customize/custom-functions"
      ]
    },
    {
      "group": "Development",
      "pages": [
        "development/local-setup",
        "development/telemetry",
        "development/roadmap"
      ]
    }
  ],
  "footerSocials": {
    "x": "https://x.com/gregpr07",
    "github": "https://github.com/browser-use/browser-use",
    "linkedin": "https://linkedin.com/company/browser-use"
  }
}

================================================
File: docs/quickstart.mdx
================================================
---
title: "Quickstart"
description: "Start using Browser Use with this quickstart guide"
icon: "rocket"
---

{/* You can install Browser Use from PyPI or clone it from Github. */}

## Prepare the environment

Browser Use requires Python 3.11 or higher.

First, we recommend using [uv](https://docs.astral.sh/uv/) to setup the Python environment.

```bash
uv venv --python 3.11
```

and activate it with:

```bash
# For Mac/Linux:
source .venv/bin/activate

# For Windows:
.venv\Scripts\activate
```

Install the dependencies:

```bash
uv pip install browser-use
```

Then install playwright:

```bash
playwright install
```

## Create an agent

Then you can use the agent as follows:

```python agent.py
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

## Set up your LLM API keys

`ChatOpenAI` and other Langchain chat models require API keys. You should store these in your `.env` file. For example, for OpenAI and Anthropic, you can set the API keys in your `.env` file, such as:


```bash .env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

For other LLM models you can refer to the [Langchain documentation](https://python.langchain.com/docs/integrations/chat/) to find how to set them up with their specific API keys.


================================================
File: docs/customize/agent-settings.mdx
================================================
---
title: "Agent Settings"
description: "Learn how to configure the agent"
icon: "gear"
---

## Overview

The `Agent` class is the core component of Browser Use that handles browser automation. Here are the main configuration options you can use when initializing an agent.

## Basic Settings

```python
from browser_use import Agent
from langchain_openai import ChatOpenAI

agent = Agent(
    task="Search for latest news about AI",
    llm=ChatOpenAI(model="gpt-4o"),
)
```

### Required Parameters

- `task`: The instruction for the agent to execute
- `llm`: A LangChain chat model instance. See <a href="/customize/langchain-models">LangChain Models</a> for supported models.

## Agent Behavior

Control how the agent operates:

```python
agent = Agent(
    task="your task",
    llm=llm,
    controller=custom_controller,  # For custom tool calling
    use_vision=True,              # Enable vision capabilities
    save_conversation_path="logs/conversation.json"  # Save chat logs
)
```

### Behavior Parameters

- `controller`: Registry of functions the agent can call. Defaults to base Controller. See <a href="/customize/custom-functions">Custom Functions</a> for details.
- `use_vision`: Enable/disable vision capabilities. Defaults to `True`.
  - When enabled, the model processes visual information from web pages
  - Disable to reduce costs or use models without vision support
  - For GPT-4o, image processing costs approximately 800-1000 tokens (~$0.002 USD) per image (but this depends on the defined screen size)
- `save_conversation_path`: Path to save the complete conversation history. Useful for debugging.
- `system_prompt_class`: Custom system prompt class. See <a href="/customize/system-prompt">System Prompt</a> for customization options.

<Note>
  Vision capabilities are recommended for better web interaction understanding,
  but can be disabled to reduce costs or when using models without vision
  support.
</Note>

## (Reuse) Browser Configuration

You can configure how the agent interacts with the browser. To see more `Browser` options refer to the <a href="/customize/browser-settings">Browser Settings</a> documentation.

### Reuse Existing Browser

`browser`: A Browser Use Browser instance. When provided, the agent will reuse this browser instance and automatically create new contexts for each `run()`.

```python
from browser_use import Agent, Browser
from playwright.async_api import BrowserContext

# Reuse existing browser
browser = Browser()
agent = Agent(
    task=task1,
    llm=llm,
    browser=browser  # Browser instance will be reused
)

await agent.run()

# Manually close the browser
await browser.close()
```

<Note>
  Remember: in this scenario the `Browser` will not be closed automatically.
</Note>

### Reuse Existing Browser Context

`browser_context`: A Playwright browser context. Useful for maintaining persistent sessions. See <a href="/customize/persistent-browser">Persistent Browser</a> for more details.

```python
from browser_use import Agent, Browser
from playwright.async_api import BrowserContext

# Use specific browser context (preferred method)
async with await browser.new_context() as context:
    agent = Agent(
        task=task2,
        llm=llm,
        browser_context=context  # Use persistent context
    )

    # Run the agent
    await agent.run()

    # Pass the context to the next agent
    next_agent = Agent(
        task=task2,
        llm=llm,
        browser_context=context
    )

    ...

await browser.close()
```

For more information about how browser context works, refer to the [Playwright
documentation](https://playwright.dev/docs/api/class-browsercontext).

<Note>
  You can reuse the same context for multiple agents. If you do nothing, the
  browser will be automatically created and closed on `run()` completion.
</Note>

## Running the Agent

The agent is executed using the async `run()` method:

- `max_steps` (default: `100`)  
  Maximum number of steps the agent can take during execution. This prevents infinite loops and helps control execution time.

## Agent History

The method returns an `AgentHistoryList` object containing the complete execution history. This history is invaluable for debugging, analysis, and creating reproducible scripts.

```python
# Example of accessing history
history = await agent.run()

# Access (some) useful information
history.urls()              # List of visited URLs
history.screenshots()       # List of screenshot paths
history.action_names()      # Names of executed actions
history.extracted_content() # Content extracted during execution
history.errors()           # Any errors that occurred
history.model_actions()     # All actions with their parameters
```

The `AgentHistoryList` provides many helper methods to analyze the execution:

- `final_result()`: Get the final extracted content
- `is_done()`: Check if the agent completed successfully
- `has_errors()`: Check if any errors occurred
- `model_thoughts()`: Get the agent's reasoning process
- `action_results()`: Get results of all actions

<Note>
  For a complete list of helper methods and detailed history analysis
  capabilities, refer to the [AgentHistoryList source
  code](https://github.com/browser-use/browser-use/blob/main/browser_use/agent/views.py#L111).
</Note>



## Run initial actions without LLM
With [this example](https://github.com/browser-use/browser-use/blob/main/examples/features/initial_actions.py) you can run initial actions without the LLM.
Specify the action as a dictionary where the key is the action name and the value is the action parameters. You can find all our actions in the [Controller](https://github.com/browser-use/browser-use/blob/main/browser_use/controller/service.py) source code.
```python

initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
	{'scroll_down': {'amount': 1000}},
	{'extract_content': {'include_links': False}},
]
agent = Agent(
	task='What theories are displayed on the page?',
	initial_actions=initial_actions,
	llm=llm,
)
```



================================================
File: docs/customize/browser-settings.mdx
================================================
---
title: "Browser Settings"
description: "Configure browser behavior and context settings"
icon: "globe"
---

Browser Use allows you to customize how the browser behaves through two main configuration classes: `BrowserConfig` and `BrowserContextConfig`. These settings control everything from headless mode to proxy settings and page load behavior.

<Note>
  We are currently working on improving how browser contexts are managed. The
  system will soon transition to a "1 agent, 1 browser, 1 context" model for
  better stability and developer experience.
</Note>

# Browser Configuration

The `BrowserConfig` class controls the core browser behavior and connection settings.

```python
from browser_use import BrowserConfig

# Basic configuration
config = BrowserConfig(
    headless=False,
    disable_security=True
)
```

## Core Settings

- **headless** (default: `False`)  
  Runs the browser without a visible UI. Note that some websites may detect headless mode.

- **disable_security** (default: `True`)  
  Disables browser security features. While this can fix certain functionality issues (like cross-site iFrames), it should be used cautiously, especially when visiting untrusted websites.

### Additional Settings

- **extra_chromium_args** (default: `[]`)  
  Additional arguments passed to the browser at launch. See the [full list of available arguments](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L154).

- **proxy** (default: `None`)  
  Standard Playwright proxy settings for using external proxy services.

- **new_context_config** (default: `BrowserContextConfig()`)  
  Default settings for new browser contexts. See Context Configuration below.

<Note>
  For web scraping tasks on sites that restrict automated access, we recommend
  using external browser or proxy providers for better reliability.
</Note>

## Alternative Initialization

These settings allow you to connect to external browser providers or use a local Chrome instance.

### External Browser Provider (wss)

Connect to cloud-based browser services for enhanced reliability and proxy capabilities.

```python
config = BrowserConfig(
    wss_url="wss://your-browser-provider.com/ws"
)
```

- **wss_url** (default: `None`)  
  WebSocket URL for connecting to external browser providers (e.g., anchorbrowser.com, steel.dev, browserbase.com, browserless.io).

<Note>
  This overrides local browser settings and uses the provider's configuration.
  Refer to their documentation for settings.
</Note>

### External Browser Provider (cdp)

Connect to cloud or local Chrome instances using Chrome DevTools Protocol (CDP) for use with tools like `headless-shell` or `browserless`.

```python
config = BrowserConfig(
    cdp_url="http://localhost:9222"
)
```

- **cdp_url** (default: `None`)  
  URL for connecting to a Chrome instance via CDP. Commonly used for debugging or connecting to locally running Chrome instances.

### Local Chrome Instance (binary)

Connect to your existing Chrome installation to access saved states and cookies.

```python
config = BrowserConfig(
    chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
```

- **chrome_instance_path** (default: `None`)  
  Path to connect to an existing Chrome installation. Particularly useful for workflows requiring existing login states or browser preferences.

<Note>This will overwrite other browser settings.</Note>

# Context Configuration

The `BrowserContextConfig` class controls settings for individual browser contexts.

```python
from browser_use.browser.context import BrowserContextConfig

config = BrowserContextConfig(
    cookies_file="path/to/cookies.json",
    wait_for_network_idle_page_load_time=3.0,
    browser_window_size={'width': 1280, 'height': 1100},
    locale='en-US',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    highlight_elements=True,
    viewport_expansion=500,
    allowed_domains=['google.com', 'wikipedia.org'],
)

browser = Browser()
context = BrowserContext(browser=browser, config=config)


async def run_search():
	agent = Agent(
		browser_context=context,
		task='Your task',
		llm=llm)
```

## Configuration Options

### Page Load Settings

- **minimum_wait_page_load_time** (default: `0.5`)  
  Minimum time to wait before capturing page state for LLM input.

- **wait_for_network_idle_page_load_time** (default: `1.0`)  
  Time to wait for network activity to cease. Increase to 3-5s for slower websites. This tracks essential content loading, not dynamic elements like videos.

- **maximum_wait_page_load_time** (default: `5.0`)  
  Maximum time to wait for page load before proceeding.

### Display Settings

- **browser_window_size** (default: `{'width': 1280, 'height': 1100}`)  
  Browser window dimensions. The default size is optimized for general use cases and interaction with common UI elements like cookie banners.

- **locale** (default: `None`)  
  Specify user locale, for example en-GB, de-DE, etc. Locale will affect navigator.language value, Accept-Language request header value as well as number and date formatting rules. If not provided, defaults to the system default locale.

- **highlight_elements** (default: `True`)  
  Highlight interactive elements on the screen with colorfull bounding boxes.

- **viewport_expansion** (default: `500`)  
  Viewport expansion in pixels. With this you can controll how much of the page is included in the context of the LLM. If set to -1, all elements from the entire page will be included (this leads to high token usage). If set to 0, only the elements which are visible in the viewport will be included.
  Default is 500 pixels, that means that we inlcude a little bit more than the visible viewport inside the context.

### Restrict URLs 

- **allowed_domains** (default: `None`)  
  List of allowed domains that the agent can access. If None, all domains are allowed. 
  Example: ['google.com', 'wikipedia.org'] - Here the agent will only be able to access google and wikipedia.

### Debug and Recording

- **save_recording_path** (default: `None`)  
  Directory path for saving video recordings.

- **trace_path** (default: `None`)  
  Directory path for saving trace files. Files are automatically named as `{trace_path}/{context_id}.zip`.


================================================
File: docs/customize/custom-functions.mdx
================================================
---
title: "Custom Functions"
description: "Extend default agent and write custom function calls"
icon: "function"
---

## Basic Function Registration

Functions can be either `sync` or `async`. Keep them focused and single-purpose.

```python
from browser_use import Controller, ActionResult
# Initialize the controller
controller = Controller()

@controller.action('Ask user for information')
def ask_human(question: str) -> str:
    answer = input(f'\n{question}\nInput: ')
    return ActionResult(extracted_content=answer)
```

<Note>
  Basic `Controller` has all basic functionality you might need to interact with
  the browser already implemented.
</Note>

```python
# ... then pass controller to the agent
agent = Agent(
    task=task,
    llm=llm,
    controller=controller
)
```

<Note>
  Keep the function name and description short and concise. The Agent use the
  function solely based on the name and description. The stringified output of
  the action is passed to the Agent.
</Note>

## Browser-Aware Functions

For actions that need browser access, use the `requires_browser=True` parameter:

```python
from browser_use import Browser, Controller, ActionResult

controller = Controller()
@controller.action('Open website', requires_browser=True)
async def open_website(url: str, browser: Browser):
    page = browser.get_current_page()
    await page.goto(url)
    return ActionResult(extracted_content='Website opened')
```

## Structured Parameters with Pydantic

For complex actions, you can define parameter schemas using Pydantic models:

```python
from pydantic import BaseModel
from typing import Optional
from browser_use import Controller, ActionResult, Browser

controller = Controller()

class JobDetails(BaseModel):
    title: str
    company: str
    job_link: str
    salary: Optional[str] = None

@controller.action(
    'Save job details which you found on page',
    param_model=JobDetails,
    requires_browser=True
)
async def save_job(params: JobDetails, browser: Browser):
    print(f"Saving job: {params.title} at {params.company}")

    # Access browser if needed
    page = browser.get_current_page()
    await page.goto(params.job_link)
```

## Using Custom Actions with multiple agents

You can use the same controller for multiple agents.

```python
controller = Controller()

# ... register actions to the controller

agent = Agent(
    task="Go to website X and find the latest news",
    llm=llm,
    controller=controller
)

# Run the agent
await agent.run()

agent2 = Agent(
    task="Go to website Y and find the latest news",
    llm=llm,
    controller=controller
)

await agent2.run()
```

<Note>
  The controller is stateless and can be used to register multiple actions and
  multiple agents.
</Note>



## Exclude functions
If you want less actions to be used by the agent, you can exclude them from the controller.
```python
controller = Controller(exclude_actions=['open_tab', 'google_search'])
```


For more examples like file upload or notifications, visit [examples/custom-functions](https://github.com/browser-use/browser-use/tree/main/examples/custom-functions).



================================================
File: docs/customize/output-format.mdx
================================================
---
title: "Output Format"
description: "The default is text. But you can define a structured output format to make post-processing easier."
icon: "code"
---

## Custom output format
With [this example](https://github.com/browser-use/browser-use/blob/main/examples/features/custom_output.py) you can define what output format the agent should return to you.

```python
from pydantic import BaseModel
# Define the output format as a Pydantic model
class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int


class Posts(BaseModel):
	posts: List[Post]


controller = Controller(output_model=Posts)


async def main():
	task = 'Go to hackernews show hn and give me the first  5 posts'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)

	history = await agent.run()

	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)

		for post in parsed.posts:
			print('\n--------------------------------')
			print(f'Title:            {post.post_title}')
			print(f'URL:              {post.post_url}')
			print(f'Comments:         {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
	else:
		print('No result')


if __name__ == '__main__':
	asyncio.run(main())
```

================================================
File: docs/customize/real-browser.mdx
================================================
---
title: "Connect to your Browser"
description: "With this you can connect to your real browser, where you are logged in with all your accounts."
icon: "computer"
---

## Overview

You can connect the agent to your real Chrome browser instance, allowing it to access your existing browser profile with all your logged-in accounts and settings. This is particularly useful when you want the agent to interact with services where you're already authenticated.

<Note>
  First make sure to close all running Chrome instances.
</Note>

## Basic Configuration

To connect to your real Chrome browser, you'll need to specify the path to your Chrome executable when creating the Browser instance:

```python
from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import asyncio
# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

# Create the agent with your configured browser
agent = Agent(
    task="Your task here",
    llm=ChatOpenAI(model='gpt-4o'),
    browser=browser,
)

async def main():
    await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
```


<Note>
  When using your real browser, the agent will have access to all your logged-in sessions. Make sure to review the task you're giving to the agent and ensure it aligns with your security requirements.
</Note>


================================================
File: docs/customize/supported-models.mdx
================================================
---
title: "Supported Models"
description: "Guide to using different LangChain chat models with Browser Use"
icon: "robot"
---

## Overview

Browser Use supports various LangChain chat models. Here's how to configure and use the most popular ones. The full list is available in the [LangChain documentation](https://python.langchain.com/docs/integrations/chat/).

## Model Recommendations

We have yet to test performance across all models. Currently, we achieve the best results using GPT-4o with an 89% accuracy on the [WebVoyager Dataset](https://browser-use.com/posts/sota-technical-report). DeepSeek-V3 is 30 times cheaper than GPT-4o. Gemini-2.0-exp is also gaining popularity in the community because it is currently free.
We also support local models, like Qwen 2.5, but be aware that small models often return the wrong output structure-which lead to parsing errors. We believe that local models will improve significantly this year.


<Note>
  All models require their respective API keys. Make sure to set them in your
  environment variables before running the agent.
</Note>

## Supported Models

All LangChain chat models, which support tool-calling are available. We will document the most popular ones here.

### OpenAI

OpenAI's GPT-4o models are recommended for best performance.

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Initialize the model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
```

Required environment variables:

```bash .env
OPENAI_API_KEY=
```

### Anthropic


```python
from langchain_anthropic import ChatAnthropic
from browser_use import Agent

# Initialize the model
llm = ChatAnthropic(
    model_name="claude-3-sonnet-20240229",
    temperature=0.0,
    timeout=100, # Increase for complex tasks
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
```

And add the variable:

```bash .env
ANTHROPIC_API_KEY=
```

### Azure OpenAI

```python
from langchain_openai import AzureChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
import os

# Initialize the model
llm = AzureChatOpenAI(
    model="gpt-4o",
    api_version='2024-10-21',
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
    api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
```

Required environment variables:

```bash .env
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_KEY=
```


### Gemini

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
```

Required environment variables:

```bash .env
GEMINI_API_KEY=
```


### DeepSeek-V3
The community likes DeepSeek-V3 for its low price, no rate limits, open-source nature, and good performance. 
The example is available [here](https://github.com/browser-use/browser-use/blob/main/examples/models/deepseek.py).

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr


# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm,
    use_vision=False
)
```

Required environment variables:

```bash .env
DEEPSEEK_API_KEY=
```

### DeepSeek-R1
We support DeepSeek-R1. Its not fully tested yet, more and more functionality will be added, like e.g. the output of it'sreasoning content.
The example is available [here](https://github.com/browser-use/browser-use/blob/main/examples/models/deepseek-r1.py).
It does not support vision. The model is open-source so you could also use it with Ollama, but we have not tested it.
```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr


# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-reasoner', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm,
    use_vision=False
)
```

Required environment variables:

```bash .env
DEEPSEEK_API_KEY=
```

### Ollama
Many users asked for local models. Here they are. 

1. Download Ollama from [here](https://ollama.ai/download)
2. Run `ollama pull model_name`. Pick a model which supports tool-calling from [here](https://ollama.com/search?c=tools)
3. Run `ollama start`

```python
from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr


# Initialize the model
llm=ChatOllama(model="qwen2.5", num_ctx=32000)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
```

Required environment variables: None!

## Coming soon
(We are working on it)
- Groq
- Github
- Fine-tuned models


================================================
File: docs/customize/system-prompt.mdx
================================================
---
title: "System Prompt"
description: "Customize the system prompt to control agent behavior and capabilities"
icon: "message"
---

## Overview

You can customize the system prompt by extending the `SystemPrompt` class. Internally, this adds extra instructions to the default system prompt.

<Note>
  Custom system prompts allow you to modify the agent's behavior at a
  fundamental level. Use this feature carefully as it can significantly impact
  the agent's performance and reliability.
</Note>

## Basic Customization

Create a custom system prompt by inheriting from the base class.

```python
from browser_use import Agent, SystemPrompt

class MySystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        # Get existing rules from parent class
        existing_rules = super().important_rules()

        # Add your custom rules
        new_rules = """
9. MOST IMPORTANT RULE:
- ALWAYS open first a new tab and go to wikipedia.com no matter the task!!!
"""

        # Make sure to use this pattern otherwise the exiting rules will be lost
        return f'{existing_rules}\n{new_rules}'
```

## Using Custom System Prompt

Apply your custom system prompt when creating an agent:

```python
from langchain_openai import ChatOpenAI

# Initialize the model
model = ChatOpenAI(model='gpt-4o')

# Create agent with custom system prompt
agent = Agent(
    task="Your task here",
    llm=model,
    system_prompt_class=MySystemPrompt
)
```


================================================
File: docs/development/contribution-guide.mdx
================================================
---
title: "Contribution Guide"
description: "Learn how to contribute to Browser Use"
icon: "code-pull-request"
---

Working on it!


================================================
File: docs/development/local-setup.mdx
================================================
---
title: "Local Setup"
description: "Set up Browser Use development environment locally"
icon: "laptop-code"
---

## Prerequisites

Browser Use requires Python 3.11 or higher. We recommend using [uv](https://docs.astral.sh/uv/) for Python environment management.

## Clone the Repository

First, clone the Browser Use repository:

```bash
git clone https://github.com/browser-use/browser-use
cd browser-use
```

## Environment Setup

1. Create a virtual environment:

```bash
uv venv --python 3.11
```

2. Install dependencies:

```bash
# Install all dependencies including dev packages
uv pip install . ."[dev]"
```

## Configuration

Set up your environment variables:

```bash
# Copy the example environment file
cp .env.example .env
```

Or manually create a `.env` file with your API keys:

```bash .env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

<Note>
  You can use any LLM model supported by LangChain. See [LangChain
  Models](/customize/langchain-models) for available options and their specific
  API key requirements.
</Note>

## Development

After setup, you can:

- Run tests with `pytest`
- Build the package with `hatch build`
- Try the examples in the `examples/` directory

## Getting Help

If you run into any issues:

1. Check our [GitHub Issues](https://github.com/browser-use/browser-use/issues)
2. Join our [Discord community](https://link.browser-use.com/discord) for support

<Note>
  We welcome contributions! See our [Contribution
  Guide](/development/contribution-guide) for guidelines on how to help improve
  Browser Use.
</Note>


================================================
File: docs/development/roadmap.mdx
================================================
---
title: "Roadmap"
description: "Future plans and upcoming features for Browser Use"
icon: "road"
---

Big things coming soon!


================================================
File: docs/development/telemetry.mdx
================================================
---
title: "Telemetry"
description: "Understanding Browser Use's telemetry and privacy settings"
icon: "chart-mixed"
---

## Overview

Browser Use collects anonymous usage data to help us understand how the library is being used and to improve the user experience. It also helps us fix bugs faster and prioritize feature development.

## Data Collection

We use [PostHog](https://posthog.com) for telemetry collection. The data is completely anonymized and contains no personally identifiable information.

<Note>
  We never collect personal information, credentials, or specific content from
  your browser automation tasks.
</Note>

## Opting Out

You can disable telemetry by setting an environment variable:

```bash .env
ANONYMIZED_TELEMETRY=false
```

Or in your Python code:

```python
import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"
```

<Note>
  Even when enabled, telemetry has zero impact on the library's performance or
  functionality. Code is available in [Telemetry
  Service](https://github.com/browser-use/browser-use/tree/main/browser_use/telemetry).
</Note>


================================================
File: examples/simple.py
================================================
import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
task = 'Find the founders of browser-use and draft them a short personalized message'

agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/browser/real_browser.py
================================================
import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

browser = Browser(
	config=BrowserConfig(
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)


async def main():
	agent = Agent(
		task='In docs.google.com write my Papa a quick letter',
		llm=ChatOpenAI(model='gpt-4o'),
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/browser/using_cdp.py
================================================
"""
Simple demonstration of the CDP feature.

To test this locally, follow these steps:
1. Create a shortcut for the executable Chrome file.
2. Add the following argument to the shortcut:
   - On Windows: `--remote-debugging-port=9222`
3. Open a web browser and navigate to `http://localhost:9222/json/version` to verify that the Remote Debugging Protocol (CDP) is running.
4. Launch this example.

@dev You need to set the `GEMINI_API_KEY` environment variable before proceeding.
"""



import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from pydantic import SecretStr

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

browser = Browser(
	config=BrowserConfig(
		headless=False,
		cdp_url="http://localhost:9222",
	)
)
controller = Controller()


async def main():
	task = f'In docs.google.com write my Papa a quick thank you for everything letter \n - Magnus'
	task += f' and save the document as pdf'
	model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=SecretStr(api_key))
	agent = Agent(
		task=task,
		llm=model,
		controller=controller,
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/custom-functions/clipboard.py
================================================
import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

import pyperclip
from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

browser = Browser(
	config=BrowserConfig(
		headless=False,
	)
)
controller = Controller()


@controller.registry.action('Copy text to clipboard')
def copy_to_clipboard(text: str):
	pyperclip.copy(text)
	return ActionResult(extracted_content=text)


@controller.registry.action('Paste text from clipboard', requires_browser=True)
async def paste_from_clipboard(browser: BrowserContext):
	text = pyperclip.paste()
	# send text to browser
	page = await browser.get_current_page()
	await page.keyboard.type(text)

	return ActionResult(extracted_content=text)


async def main():
	task = (
		f'Copy the text "Hello, world!" to the clipboard, then go to google.com and paste the text'
	)
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(
		task=task,
		llm=model,
		controller=controller,
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/custom-functions/file_upload.py
================================================
import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

CV = Path.cwd() / 'examples/test_cv.txt'
import logging

logger = logging.getLogger(__name__)

# Initialize controller first
browser = Browser(
	config=BrowserConfig(
		headless=False,
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)
controller = Controller()


@controller.action(
	'Upload file to element ',
	requires_browser=True,
)
async def upload_file(index: int, browser: BrowserContext):
	path = str(CV.absolute())
	dom_el = await browser.get_dom_element_by_index(index)

	if dom_el is None:
		return ActionResult(error=f'No element found at index {index}')

	file_upload_dom_el = dom_el.get_file_upload_element()

	if file_upload_dom_el is None:
		logger.info(f'No file upload element found at index {index}')
		return ActionResult(error=f'No file upload element found at index {index}')

	file_upload_el = await browser.get_locate_element(file_upload_dom_el)

	if file_upload_el is None:
		logger.info(f'No file upload element found at index {index}')
		return ActionResult(error=f'No file upload element found at index {index}')

	try:
		await file_upload_el.set_input_files(path)
		msg = f'Successfully uploaded file to index {index}'
		logger.info(msg)
		return ActionResult(extracted_content=msg)
	except Exception as e:
		logger.debug(f'Error in set_input_files: {str(e)}')
		return ActionResult(error=f'Failed to upload file to index {index}')


@controller.action('Close file dialog', requires_browser=True)
async def close_file_dialog(browser: BrowserContext):
	page = await browser.get_current_page()
	await page.keyboard.press('Escape')


async def main():
	task = (
		f'go to https://kzmpmkh2zfk1ojnpxfn1.lite.vusercontent.net/'
		f' and upload to each upload field my file'
	)

	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(
		task=task,
		llm=model,
		controller=controller,
		browser=browser,
	)

	await agent.run()

	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/custom-functions/notification.py
================================================
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from browser_use import ActionResult, Agent, Controller

load_dotenv()

controller = Controller()


@controller.registry.action('Done with task ')
async def done(text: str):
	import yagmail

	# To send emails use
	# STEP 1: go to https://support.google.com/accounts/answer/185833
	# STEP 2: Create an app password (you cant use here your normal gmail password)
	# STEP 3: Use the app password in the code below for the password
	yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')
	yag.send(
		to='recipient@example.com',
		subject='Test Email',
		contents=f'result\n: {text}',
	)

	return ActionResult(is_done=True, extracted_content='Email sent!')


async def main():
	task = 'go to brower-use.com and then done'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/custom-functions/save_to_file_hugging_face.py
================================================
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from typing import List, Optional

from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller

# Initialize controller first
controller = Controller()


class Model(BaseModel):
	title: str
	url: str
	likes: int
	license: str


class Models(BaseModel):
	models: List[Model]


@controller.action('Save models', param_model=Models)
def save_models(params: Models):
	with open('models.txt', 'a') as f:
		for model in params.models:
			f.write(f'{model.title} ({model.url}): {model.likes} likes, {model.license}\n')


# video: https://preview.screen.studio/share/EtOhIk0P
async def main():
	task = f'Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file.'

	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/features/custom_output.py
================================================
"""
Show how to use custom outputs.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from browser_use import ActionResult, Agent, Controller

load_dotenv()


class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int


class Posts(BaseModel):
	posts: List[Post]


controller = Controller(output_model=Posts)


async def main():
	task = 'Go to hackernews show hn and give me the first  5 posts'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)

	history = await agent.run()

	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)

		for post in parsed.posts:
			print('\n--------------------------------')
			print(f'Title:            {post.post_title}')
			print(f'URL:              {post.post_url}')
			print(f'Comments:         {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
	else:
		print('No result')


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/features/custom_system_prompt.py
================================================
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, SystemPrompt


class MySystemPrompt(SystemPrompt):
	def important_rules(self) -> str:
		existing_rules = super().important_rules()
		new_rules = 'REMEMBER the most important RULE: ALWAYS open first a new tab and go first to url wikipedia.com no matter the task!!!'
		return f'{existing_rules}\n{new_rules}'

		# other methods can be overridden as well (not recommended)


async def main():
	task = "do google search to find images of Elon Musk's wife"
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, system_prompt_class=MySystemPrompt)

	print(
		json.dumps(
			agent.message_manager.system_prompt.model_dump(exclude_unset=True),
			indent=4,
		)
	)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/features/custom_user_agent.py
================================================
import os
import sys

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from browser_use.browser.context import BrowserContext, BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import asyncio

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller


def get_llm(provider: str):
	if provider == 'anthropic':
		return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0)
	elif provider == 'openai':
		return ChatOpenAI(model='gpt-4o', temperature=0.0)

	else:
		raise ValueError(f'Unsupported provider: {provider}')


# NOTE: This example is to find your current user agent string to use it in the browser_context
task = 'go to https://whatismyuseragent.com and find the current user agent string '


controller = Controller()


parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, help='The query to process', default=task)
parser.add_argument(
	'--provider',
	type=str,
	choices=['openai', 'anthropic'],
	default='openai',
	help='The model provider to use (default: openai)',
)

args = parser.parse_args()

llm = get_llm(args.provider)


browser = Browser(
	config=BrowserConfig(
		# chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

browser_context = BrowserContext(config=BrowserContextConfig(user_agent='foobarfoo'), browser=browser)

agent = Agent(
	task=args.query,
	llm=llm,
	controller=controller,
	# browser=browser,
	browser_context=browser_context,
	use_vision=True,
	max_actions_per_step=1,
)


async def main():
	await agent.run(max_steps=25)

	input('Press Enter to close the browser...')
	await browser_context.close()


asyncio.run(main())


================================================
File: examples/features/follow_up_tasks.py
================================================
import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent
from browser_use.agent.views import ActionResult
from browser_use.controller.service import Controller

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
controller = Controller()


task = 'Find the founders of browser-use and draft them a short personalized message'

agent = Agent(task=task, llm=llm, controller=controller)


async def main():
	await agent.run()

	# new_task = input('Type in a new task: ')
	new_task = 'Find an image of the founders'

	agent.add_new_task(new_task)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/features/initial_actions.py
================================================
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()
llm = ChatOpenAI(model='gpt-4o')

initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
	{'scroll_down': {'amount': 1000}},
	{'extract_content': {'include_links': False}},
]
agent = Agent(
	task='What theories are displayed on the page?',
	initial_actions=initial_actions,
	llm=llm,
)


async def main():
	await agent.run(max_steps=10)


if __name__ == '__main__':
	import asyncio

	asyncio.run(main())


================================================
File: examples/features/multi-tab_handling.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

# video: https://preview.screen.studio/share/clenCmS6
llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='open 3 tabs with elon musk, trump, and steve jobs, then go back to the first and stop',
	llm=llm,
)


async def main():
	await agent.run()


asyncio.run(main())


================================================
File: examples/features/multiple_agents_same_browser.py
================================================
import os
import sys

from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from browser_use import Agent, Browser, Controller


# Video: https://preview.screen.studio/share/8Elaq9sm
async def main():
	# Persist the browser state across agents

	browser = Browser()
	async with await browser.new_context() as context:
		model = ChatOpenAI(model='gpt-4o')
		current_agent = None

		async def get_input():
			return await asyncio.get_event_loop().run_in_executor(
				None, lambda: input('Enter task (p: pause current agent, r: resume, b: break): ')
			)

		while True:
			task = await get_input()

			if task.lower() == 'p':
				# Pause the current agent if one exists
				if current_agent:
					current_agent.pause()
				continue
			elif task.lower() == 'r':
				# Resume the current agent if one exists
				if current_agent:
					current_agent.resume()
				continue
			elif task.lower() == 'b':
				# Break the current agent's execution if one exists
				if current_agent:
					current_agent.stop()
					current_agent = None
				continue

			# If there's a current agent running, pause it before starting new one
			if current_agent:
				current_agent.pause()

			# Create and run new agent with the task
			current_agent = Agent(
				task=task,
				llm=model,
				browser_context=context,
			)

			# Run the agent asynchronously without blocking
			asyncio.create_task(current_agent.run())


asyncio.run(main())

# Now aad the cheapest to the cart


================================================
File: examples/features/parallel_agents.py
================================================
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig

browser = Browser(
	config=BrowserConfig(
		disable_security=True,
		headless=False,
		new_context_config=BrowserContextConfig(save_recording_path='./tmp/recordings'),
	)
)
llm = ChatOpenAI(model='gpt-4o')


async def main():
	agents = [
		Agent(task=task, llm=llm, browser=browser)
		for task in [
			'Search Google for weather in Tokyo',
			'Check Reddit front page title',
			'Look up Bitcoin price on Coinbase',
			'Find NASA image of the day',
			# 'Check top story on CNN',
			# 'Search latest SpaceX launch date',
			# 'Look up population of Paris',
			# 'Find current time in Sydney',
			# 'Check who won last Super Bowl',
			# 'Search trending topics on Twitter',
		]
	]

	await asyncio.gather(*[agent.run() for agent in agents])

	# async with await browser.new_context() as context:
	agentX = Agent(
		task='Go to apple.com and return the title of the page',
		llm=llm,
		browser=browser,
		# browser_context=context,
	)
	await agentX.run()

	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/features/pause_agent.py
================================================
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import threading
import time

from langchain_openai import ChatOpenAI

from browser_use import Agent


class AgentController:
	def __init__(self):
		llm = ChatOpenAI(model='gpt-4o')
		self.agent = Agent(
			task="Go to wikipedia.org and search for 'Python programming language', then read the first paragraph", llm=llm
		)
		self.running = False

	async def run_agent(self):
		"""Run the agent"""
		self.running = True
		await self.agent.run()

	def start(self):
		"""Start the agent in a separate thread"""
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		loop.run_until_complete(self.run_agent())

	def pause(self):
		"""Pause the agent"""
		self.agent.pause()

	def resume(self):
		"""Resume the agent"""
		self.agent.resume()

	def stop(self):
		"""Stop the agent"""
		self.agent.stop()
		self.running = False


def print_menu():
	print('\nAgent Control Menu:')
	print('1. Start')
	print('2. Pause')
	print('3. Resume')
	print('4. Stop')
	print('5. Exit')


def main():
	controller = AgentController()
	agent_thread = None

	while True:
		print_menu()
		choice = input('Enter your choice (1-5): ')

		if choice == '1' and not agent_thread:
			print('Starting agent...')
			agent_thread = threading.Thread(target=controller.start)
			agent_thread.start()

		elif choice == '2':
			print('Pausing agent...')
			controller.pause()

		elif choice == '3':
			print('Resuming agent...')
			controller.resume()

		elif choice == '4':
			print('Stopping agent...')
			controller.stop()
			if agent_thread:
				agent_thread.join()
				agent_thread = None

		elif choice == '5':
			print('Exiting...')
			if controller.running:
				controller.stop()
				if agent_thread:
					agent_thread.join()
			break

		time.sleep(0.1)  # Small delay to prevent CPU spinning


if __name__ == '__main__':
	main()


================================================
File: examples/features/restrict_urls.py
================================================
import os
import sys

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from browser_use.browser.context import BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import asyncio

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller

llm = ChatOpenAI(model='gpt-4o', temperature=0.0)
task = (
	'go to google.com and search for openai.com and click on the first link then extract content and scroll down - whats there?'
)

allowed_domains = ['google.com']

browser = Browser(
	config=BrowserConfig(
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
		new_context_config=BrowserContextConfig(
			allowed_domains=allowed_domains,
		),
	),
)

agent = Agent(
	task=task,
	llm=llm,
	browser=browser,
)


async def main():
	await agent.run(max_steps=25)

	input('Press Enter to close the browser...')
	await browser.close()


asyncio.run(main())


================================================
File: examples/features/result_processing.py
================================================
import os
import sys
from pprint import pprint

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import (
	BrowserContext,
	BrowserContextConfig,
	BrowserContextWindowSize,
)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.controller.service import Controller

llm = ChatOpenAI(model='gpt-4o')
browser = Browser(
	config=BrowserConfig(
		headless=False,
		disable_security=True,
		extra_chromium_args=['--window-size=2000,2000'],
	)
)


async def main():
	async with await browser.new_context(
		config=BrowserContextConfig(
			trace_path='./tmp/result_processing',
			no_viewport=False,
			browser_window_size=BrowserContextWindowSize(width=1280, height=1000),
		)
	) as browser_context:
		agent = Agent(
			task="go to google.com and type 'OpenAI' click search and give me the first url",
			llm=llm,
			browser_context=browser_context,
		)
		history: AgentHistoryList = await agent.run(max_steps=3)

		print('Final Result:')
		pprint(history.final_result(), indent=4)

		print('\nErrors:')
		pprint(history.errors(), indent=4)

		# e.g. xPaths the model clicked on
		print('\nModel Outputs:')
		pprint(history.model_actions(), indent=4)

		print('\nThoughts:')
		pprint(history.model_thoughts(), indent=4)
	# close browser
	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/features/save_trace.py
================================================
import os
import sys

from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser
from browser_use.browser.context import BrowserContextConfig

llm = ChatOpenAI(model='gpt-4o', temperature=0.0)


async def main():
	browser = Browser()

	async with await browser.new_context(
		config=BrowserContextConfig(trace_path='./tmp/traces/')
	) as context:
		agent = Agent(
			task='Go to hackernews, then go to apple.com and return all titles of open tabs',
			llm=llm,
			browser_context=context,
		)
		await agent.run()

	await browser.close()


asyncio.run(main())


================================================
File: examples/features/validate_output.py
================================================
"""
Demostrate output validator.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from browser_use import ActionResult, Agent, Controller

load_dotenv()

controller = Controller()


class DoneResult(BaseModel):
	title: str
	comments: str
	hours_since_start: int


# we overwrite done() in this example to demonstrate the validator
@controller.registry.action('Done with task', param_model=DoneResult)
async def done(params: DoneResult):
	result = ActionResult(is_done=True, extracted_content=params.model_dump_json())
	print(result)
	# NOTE: this is clearly wrong - to demonstrate the validator
	return 'blablabla'


async def main():
	task = 'Go to hackernews hn and give me the top 1 post'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller, validate_output=True)
	# NOTE: this should fail to demonstrate the validator
	await agent.run(max_steps=5)


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/integrations/discord_api.py
================================================
import discord
from discord.ext import commands
from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel

from browser_use import BrowserConfig
from browser_use.agent.service import Agent, Browser

load_dotenv()


class DiscordBot(commands.Bot):
	"""Discord bot implementation for Browser-Use tasks.

	This bot allows users to run browser automation tasks through Discord messages.
	Processes tasks asynchronously and sends the result back to the user in response to the message.
	Messages must start with the configured prefix (default: "$bu") followed by the task description.

	Args:
	    llm (BaseChatModel): Language model instance to use for task processing
	    prefix (str, optional): Command prefix for triggering browser tasks. Defaults to "$bu"
	    ack (bool, optional): Whether to acknowledge task receipt with a message. Defaults to False
	    browser_config (BrowserConfig, optional): Browser configuration settings.
	        Defaults to headless mode

	Usage:
	    ```python
	    from langchain_openai import ChatOpenAI

	    llm = ChatOpenAI()
	    bot = DiscordBot(llm=llm, prefix='$bu', ack=True)
	    bot.run('YOUR_DISCORD_TOKEN')
	    ```

	Discord Usage:
	    Send messages starting with the prefix:
	    "$bu search for python tutorials"
	"""

	def __init__(
		self,
		llm: BaseChatModel,
		prefix: str = '$bu',
		ack: bool = False,
		browser_config: BrowserConfig = BrowserConfig(headless=True),
	):
		self.llm = llm
		self.prefix = prefix.strip()
		self.ack = ack
		self.browser_config = browser_config

		# Define intents.
		intents = discord.Intents.default()
		intents.message_content = True  # Enable message content intent
		intents.members = True  # Enable members intent for user info

		# Initialize the bot with a command prefix and intents.
		super().__init__(command_prefix='!', intents=intents)  # You may not need prefix, just here for flexibility

		# self.tree = app_commands.CommandTree(self) # Initialize command tree for slash commands.

	async def on_ready(self):
		"""Called when the bot is ready."""
		try:
			print(f'We have logged in as {self.user}')
			cmds = await self.tree.sync()  # Sync the command tree with discord

		except Exception as e:
			print(f'Error during bot startup: {e}')

	async def on_message(self, message):
		"""Called when a message is received."""
		try:
			if message.author == self.user:  # Ignore the bot's messages
				return
			if message.content.strip().startswith(f'{self.prefix} '):
				if self.ack:
					try:
						await message.reply(
							'Starting browser use task...',
							mention_author=True,  # Don't ping the user
						)
					except Exception as e:
						print(f'Error sending start message: {e}')

				try:
					agent_message = await self.run_agent(message.content.replace(f'{self.prefix} ', '').strip())
					await message.channel.send(content=f'{agent_message}', reference=message, mention_author=True)
				except Exception as e:
					await message.channel.send(
						content=f'Error during task execution: {str(e)}',
						reference=message,
						mention_author=True,
					)

		except Exception as e:
			print(f'Error in message handling: {e}')

	#    await self.process_commands(message)  # Needed to process bot commands

	async def run_agent(self, task: str) -> str:
		try:
			browser = Browser(config=self.browser_config)
			agent = Agent(task=(task), llm=self.llm, browser=browser)
			result = await agent.run()

			agent_message = None
			if result.is_done():
				agent_message = result.history[-1].result[0].extracted_content

			if agent_message is None:
				agent_message = 'Oops! Something went wrong while running Browser-Use.'

			return agent_message

		except Exception as e:
			raise Exception(f'Browser-use task failed: {str(e)}')


================================================
File: examples/integrations/discord_example.py
================================================
"""
This examples requires you to have a Discord bot token and the bot already added to a server.

Five Steps to create and invite a Discord bot:

1. Create a Discord Application:
    *   Go to the Discord Developer Portal: https://discord.com/developers/applications
    *   Log in to the Discord website.
    *   Click on "New Application".
    *   Give the application a name and click "Create".
2. Configure the Bot:
    *   Navigate to the "Bot" tab on the left side of the screen.
    *   Make sure "Public Bot" is ticked if you want others to invite your bot.
	*	Generate your bot token by clicking on "Reset Token", Copy the token and save it securely.
        *   Do not share the bot token. Treat it like a password. If the token is leaked, regenerate it.
3. Enable Privileged Intents:
    *   Scroll down to the "Privileged Gateway Intents" section.
    *   Enable the necessary intents (e.g., "Server Members Intent" and "Message Content Intent").
   -->  Note: Enabling privileged intents for bots in over 100 guilds requires bot verification. You may need to contact Discord support to enable privileged intents for verified bots.
4. Generate Invite URL:
    *   Go to "OAuth2" tab and "OAuth2 URL Generator" section.
    *   Under "scopes", tick the "bot" checkbox.
    *   Tick the permissions required for your bot to function under “Bot Permissions”.
		*	e.g. "Send Messages", "Send Messages in Threads", "Read Message History",  "Mention Everyone".
    *   Copy the generated URL under the "GENERATED URL" section at the bottom.
5. Invite the Bot:
    *   Paste the URL into your browser.
    *   Choose a server to invite the bot to.
    *   Click “Authorize”.
   -->  Note: The person adding the bot needs "Manage Server" permissions.
6. Run the code below to start the bot with your bot token.
7. Write e.g. "/bu whats the weather in Tokyo?" to start a browser-use task and get a response inside the Discord channel.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import BrowserConfig
from browser_use.agent.service import Agent
from examples.integrations.discord_api import DiscordBot

load_dotenv()

# load credentials from environment variables
bot_token = os.getenv('DISCORD_BOT_TOKEN')
if not bot_token:
	raise ValueError('Discord bot token not found in .env file.')

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

bot = DiscordBot(
	llm=llm,  # required; instance of BaseChatModel
	prefix='$bu',  # optional; prefix of messages to trigger browser-use, defaults to "$bu"
	ack=True,  # optional; whether to acknowledge task receipt with a message, defaults to False
	browser_config=BrowserConfig(
		headless=False
	),  # optional; useful for changing headless mode or other browser configs, defaults to headless mode
)

bot.run(
	token=bot_token,  # required; Discord bot token
)


================================================
File: examples/models/bedrock_claude.py
================================================
"""
Automated news analysis and sentiment scoring using Bedrock.

@dev Ensure AWS environment variables are set correctly for Bedrock access.
"""

import os
import sys

from langchain_aws import ChatBedrock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import asyncio

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller


def get_llm():
    return ChatBedrock(
        model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        temperature=0.0,
        max_tokens=None,
    )


# Define the task for the agent
task = (
    "Visit cnn.com, navigate to the 'World News' section, and identify the latest headline. "
    "Open the first article and summarize its content in 3-4 sentences. "
    "Additionally, analyze the sentiment of the article (positive, neutral, or negative) "
    "and provide a confidence score for the sentiment. Present the result in a tabular format."
)

parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, help='The query for the agent to execute', default=task)
args = parser.parse_args()

llm = get_llm()

browser = Browser(
    config=BrowserConfig(
        # chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    )
)

agent = Agent(
    task=args.query, llm=llm, controller=Controller(), browser=browser, validate_output=True,
)


async def main():
    await agent.run(max_steps=30)
    await browser.close()


asyncio.run(main())


================================================
File: examples/models/deepseek-r1.py
================================================
import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent

# dotenv
load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY', '')
if not api_key:
	raise ValueError('DEEPSEEK_API_KEY is not set')


async def run_search():
	agent = Agent(
		task=('go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result'),
		llm=ChatOpenAI(
			base_url='https://api.deepseek.com/v1',
			model='deepseek-reasoner',
			api_key=SecretStr(api_key),
		),
		use_vision=False,
		max_failures=2,
		max_actions_per_step=1,
	)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(run_search())


================================================
File: examples/models/deepseek.py
================================================
import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent

# dotenv
load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY', '')
if not api_key:
	raise ValueError('DEEPSEEK_API_KEY is not set')


async def run_search():
	agent = Agent(
		task=(
			'1. Go to https://www.reddit.com/r/LocalLLaMA '
			"2. Search for 'browser use' in the search bar"
			'3. Click on first result'
			'4. Return the first comment'
		),
		llm=ChatOpenAI(
			base_url='https://api.deepseek.com/v1',
			model='deepseek-chat',
			api_key=SecretStr(api_key),
		),
		use_vision=False,
	)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(run_search())


================================================
File: examples/models/gemini.py
================================================
import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))


async def run_search():
	agent = Agent(
		task=(
			'Go to url r/LocalLLaMA subreddit and search for "browser use" in the search bar and click on the first post and find the funniest comment'
		),
		llm=llm,
		max_actions_per_step=4,
	)

	await agent.run(max_steps=25)


if __name__ == '__main__':
	asyncio.run(run_search())


================================================
File: examples/models/gpt-4o.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
	llm=llm,
)


async def main():
	await agent.run(max_steps=10)
	input('Press Enter to continue...')


asyncio.run(main())


================================================
File: examples/models/ollama.py
================================================
# import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

import asyncio
from browser_use import Agent
from browser_use.agent.views import AgentHistoryList
from langchain_ollama import ChatOllama


async def run_search() -> AgentHistoryList:
    agent = Agent(
        task="Search for a 'browser use' post on the r/LocalLLaMA subreddit and open it.",
        llm=ChatOllama(
            model="qwen2.5:32b-instruct-q4_K_M",
            num_ctx=32000,
        ),
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())


================================================
File: examples/models/qwen.py
================================================
import asyncio
import os

from langchain_ollama import ChatOllama

from browser_use import Agent


async def run_search():
	agent = Agent(
		task=(
			'1. Go to https://www.reddit.com/r/LocalLLaMA'
			"2. Search for 'browser use' in the search bar"
			'3. Click search'
			'4. Call done'
		),
		llm=ChatOllama(
			# model='qwen2.5:32b-instruct-q4_K_M',
			# model='qwen2.5:14b',
			model='qwen2.5:latest',
			num_ctx=128000,
		),
		max_actions_per_step=1,
	)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(run_search())


================================================
File: examples/ui/command_line.py
================================================
import os
import sys

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import asyncio

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller


def get_llm(provider: str):
	if provider == 'anthropic':
		return ChatAnthropic(
			model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0
		)
	elif provider == 'openai':
		return ChatOpenAI(model='gpt-4o', temperature=0.0)

	else:
		raise ValueError(f'Unsupported provider: {provider}')


task = 'go to reddit and search for post about brower-use '


controller = Controller()


parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, help='The query to process', default=task)
parser.add_argument(
	'--provider',
	type=str,
	choices=['openai', 'anthropic'],
	default='openai',
	help='The model provider to use (default: openai)',
)

args = parser.parse_args()

llm = get_llm(args.provider)


browser = Browser(
	config=BrowserConfig(
		# chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

agent = Agent(
	task=args.query,
	llm=llm,
	controller=controller,
	browser=browser,
	use_vision=True,
	max_actions_per_step=1,
)


async def main():
	await agent.run(max_steps=25)

	input('Press Enter to close the browser...')
	await browser.close()


asyncio.run(main())


================================================
File: examples/ui/gradio_demo.py
================================================
import asyncio
import os
from dataclasses import dataclass
from typing import List, Optional

import gradio as gr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from browser_use import Agent

load_dotenv()


@dataclass
class ActionResult:
	is_done: bool
	extracted_content: Optional[str]
	error: Optional[str]
	include_in_memory: bool


@dataclass
class AgentHistoryList:
	all_results: List[ActionResult]
	all_model_outputs: List[dict]


def parse_agent_history(history_str: str) -> None:
	console = Console()

	# Split the content into sections based on ActionResult entries
	sections = history_str.split('ActionResult(')

	for i, section in enumerate(sections[1:], 1):  # Skip first empty section
		# Extract relevant information
		content = ''
		if 'extracted_content=' in section:
			content = section.split('extracted_content=')[1].split(',')[0].strip("'")

		if content:
			header = Text(f'Step {i}', style='bold blue')
			panel = Panel(content, title=header, border_style='blue')
			console.print(panel)
			console.print()


async def run_browser_task(
	task: str,
	api_key: str,
	model: str = 'gpt-4o',
	headless: bool = True,
) -> str:
	if not api_key.strip():
		return 'Please provide an API key'

	os.environ['OPENAI_API_KEY'] = api_key

	try:
		agent = Agent(
			task=task,
			llm=ChatOpenAI(model='gpt-4o'),
		)
		result = await agent.run()
		#  TODO: The result cloud be parsed better
		return result
	except Exception as e:
		return f'Error: {str(e)}'


def create_ui():
	with gr.Blocks(title='Browser Use GUI') as interface:
		gr.Markdown('# Browser Use Task Automation')

		with gr.Row():
			with gr.Column():
				api_key = gr.Textbox(label='OpenAI API Key', placeholder='sk-...', type='password')
				task = gr.Textbox(
					label='Task Description',
					placeholder='E.g., Find flights from New York to London for next week',
					lines=3,
				)
				model = gr.Dropdown(
					choices=['gpt-4', 'gpt-3.5-turbo'], label='Model', value='gpt-4'
				)
				headless = gr.Checkbox(label='Run Headless', value=True)
				submit_btn = gr.Button('Run Task')

			with gr.Column():
				output = gr.Textbox(label='Output', lines=10, interactive=False)

		submit_btn.click(
			fn=lambda *args: asyncio.run(run_browser_task(*args)),
			inputs=[task, api_key, model, headless],
			outputs=output,
		)

	return interface


if __name__ == '__main__':
	demo = create_ui()
	demo.launch()


================================================
File: examples/use-cases/captcha.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

# NOTE: captchas are hard. For this example it works. But e.g. for iframes it does not.
# for this example it helps to zoom in.
llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='go to https://captcha.com/demos/features/captcha-demo.aspx and solve the captcha',
	llm=llm,
)


async def main():
	await agent.run()
	input('Press Enter to exit')


asyncio.run(main())


================================================
File: examples/use-cases/check_appointment.py
================================================
import asyncio
import os

import dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller

dotenv.load_dotenv()


controller = Controller()


class WebpageInfo(BaseModel):
	link: str = 'https://appointment.mfa.gr/en/reservations/aero/ireland-grcon-dub/'


@controller.action('Go to the webpage', param_model=WebpageInfo)
def go_to_webpage(webpage_info: WebpageInfo):
	return webpage_info.link


async def main():
	task = (
		'Go to the Greece MFA webpage via the link I provided you.'
		'Check the visa appointment dates. If there is no available date in this month, check the next month.'
		'If there is no available date in both months, tell me there is no available date.'
	)

	model = ChatOpenAI(model='gpt-4o-mini', api_key=SecretStr(os.getenv('OPENAI_API_KEY', '')))
	agent = Agent(task, model, controller=controller, use_vision=True)

	result = await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/use-cases/find_and_apply_to_jobs.py
================================================
"""
Find and apply to jobs.

@dev You need to add OPENAI_API_KEY to your environment variables.

Also you have to install PyPDF2 to read pdf files: pip install PyPDF2
"""

import csv
import os
import re
import sys
from pathlib import Path

from PyPDF2 import PdfReader

from browser_use.browser.browser import Browser, BrowserConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
from typing import List, Optional

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use import ActionResult, Agent, Controller
from browser_use.browser.context import BrowserContext

load_dotenv()
import logging

logger = logging.getLogger(__name__)
# full screen mode
controller = Controller()

# NOTE: This is the path to your cv file
CV = Path.cwd() / 'cv_04_24.pdf'

if not CV.exists():
	raise FileNotFoundError(f'You need to set the path to your cv file in the CV variable. CV file not found at {CV}')


class Job(BaseModel):
	title: str
	link: str
	company: str
	fit_score: float
	location: Optional[str] = None
	salary: Optional[str] = None


@controller.action('Save jobs to file - with a score how well it fits to my profile', param_model=Job)
def save_jobs(job: Job):
	with open('jobs.csv', 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow([job.title, job.company, job.link, job.salary, job.location])

	return 'Saved job to file'


@controller.action('Read jobs from file')
def read_jobs():
	with open('jobs.csv', 'r') as f:
		return f.read()


@controller.action('Read my cv for context to fill forms')
def read_cv():
	pdf = PdfReader(CV)
	text = ''
	for page in pdf.pages:
		text += page.extract_text() or ''
	logger.info(f'Read cv with {len(text)} characters')
	return ActionResult(extracted_content=text, include_in_memory=True)


@controller.action(
	'Upload cv to element - call this function to upload if element is not found, try with different index of the same upload element',
	requires_browser=True,
)
async def upload_cv(index: int, browser: BrowserContext):
	path = str(CV.absolute())
	dom_el = await browser.get_dom_element_by_index(index)

	if dom_el is None:
		return ActionResult(error=f'No element found at index {index}')

	file_upload_dom_el = dom_el.get_file_upload_element()

	if file_upload_dom_el is None:
		logger.info(f'No file upload element found at index {index}')
		return ActionResult(error=f'No file upload element found at index {index}')

	file_upload_el = await browser.get_locate_element(file_upload_dom_el)

	if file_upload_el is None:
		logger.info(f'No file upload element found at index {index}')
		return ActionResult(error=f'No file upload element found at index {index}')

	try:
		await file_upload_el.set_input_files(path)
		msg = f'Successfully uploaded file to index {index}'
		logger.info(msg)
		return ActionResult(extracted_content=msg)
	except Exception as e:
		logger.debug(f'Error in set_input_files: {str(e)}')
		return ActionResult(error=f'Failed to upload file to index {index}')


browser = Browser(
	config=BrowserConfig(
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
		disable_security=True,
	)
)


async def main():
	# ground_task = (
	# 	'You are a professional job finder. '
	# 	'1. Read my cv with read_cv'
	# 	'2. Read the saved jobs file '
	# 	'3. start applying to the first link of Amazon '
	# 	'You can navigate through pages e.g. by scrolling '
	# 	'Make sure to be on the english version of the page'
	# )
	ground_task = (
		'You are a professional job finder. '
		'1. Read my cv with read_cv'
		'find ml internships in and save them to a file'
		'search at company:'
	)
	tasks = [
		ground_task + '\n' + 'Google',
		# ground_task + '\n' + 'Amazon',
		# ground_task + '\n' + 'Apple',
		# ground_task + '\n' + 'Microsoft',
		# ground_task
		# + '\n'
		# + 'go to https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Taiwan%2C-Remote/Fulfillment-Analyst---New-College-Graduate-2025_JR1988949/apply/autofillWithResume?workerSubType=0c40f6bd1d8f10adf6dae42e46d44a17&workerSubType=ab40a98049581037a3ada55b087049b7 NVIDIA',
		# ground_task + '\n' + 'Meta',
	]
	model = AzureChatOpenAI(
		model='gpt-4o',
		api_version='2024-10-21',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)

	agents = []
	for task in tasks:
		agent = Agent(task=task, llm=model, controller=controller, browser=browser)
		agents.append(agent)

	await asyncio.gather(*[agent.run() for agent in agents])


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/use-cases/online_coding_agent.py
================================================
import os
import sys

from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from browser_use import Agent, Browser, Controller

async def main():
    browser = Browser()
    async with await browser.new_context() as context:
        model = ChatOpenAI(model='gpt-4o')

        # Initialize browser agent
        agent1 = Agent(
            task='Open an online code editor programiz.',
            llm=model,
            browser_context=context,
        )
        executor = Agent(
            task='Executor. Execute the code written by the coder and suggest some updates if there are errors.',
            llm=model,
            browser_context=context,
        )

        coder = Agent(
            task='Coder. Your job is to write and complete code. You are an expert coder. Code a simple calculator. Write the code on the coding interface after agent1 has opened the link.',
            llm=model,
            browser_context=context,
        )
        await agent1.run()
        await executor.run()
        await coder.run()

asyncio.run(main())


================================================
File: examples/use-cases/post-twitter.py
================================================
"""
X Posting Template using browser-use
----------------------------------------

This template allows you to automate posting on X using browser-use.
It supports:
- Posting new tweets
- Tagging users
- Replying to tweets

Add your target user and message in the config section.

target_user="XXXXX"
message="XXXXX"
reply_url="XXXXX"

Any issues, contact me on X @defichemist95
"""

import os
import sys
from typing import Optional
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from langchain_openai import ChatOpenAI
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use import Agent, Controller


# ============ Configuration Section ============
@dataclass
class TwitterConfig:
    """Configuration for Twitter posting"""

    openai_api_key: str
    chrome_path: str
    target_user: str  # Twitter handle without @
    message: str
    reply_url: str
    headless: bool = False
    model: str = "gpt-4o-mini"
    base_url: str = "https://x.com/home"


# Customize these settings
config = TwitterConfig(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    chrome_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", # This is for MacOS (Chrome)
    target_user="XXXXX",
    message="XXXXX",
    reply_url="XXXXX",
    headless=False,
)


def create_twitter_agent(config: TwitterConfig) -> Agent:

    llm = ChatOpenAI(model=config.model, api_key=config.openai_api_key)

    browser = Browser(
        config=BrowserConfig(
            headless=config.headless,
            chrome_instance_path=config.chrome_path,
        )
    )

    controller = Controller()

    # Construct the full message with tag
    full_message = f"@{config.target_user} {config.message}"

    # Create the agent with detailed instructions
    return Agent(
        task=f"""Navigate to Twitter and create a post and reply to a tweet.

        Here are the specific steps:

        1. Go to {config.base_url}. See the text input field at the top of the page that says "What's happening?"
        2. Look for the text input field at the top of the page that says "What's happening?"
        3. Click the input field and type exactly this message:
        "{full_message}"
        4. Find and click the "Post" button (look for attributes: 'button' and 'data-testid="tweetButton"')
        5. Do not click on the '+' button which will add another tweet.

        6. Navigate to {config.reply_url}
        7. Before replying, understand the context of the tweet by scrolling down and reading the comments.
        8. Reply to the tweet under 50 characters.

        Important:
        - Wait for each element to load before interacting
        - Make sure the message is typed exactly as shown
        - Verify the post button is clickable before clicking
        - Do not click on the '+' button which will add another tweet
        """,
        llm=llm,
        controller=controller,
        browser=browser,
    )


async def post_tweet(agent: Agent):

    try:
        await agent.run(max_steps=100)
        agent.create_history_gif()
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {str(e)}")


def main():
    agent = create_twitter_agent(config)
    asyncio.run(post_tweet(agent))

if __name__ == "__main__":
    main()


================================================
File: examples/use-cases/scrolling_page.py
================================================
import os
import sys

from browser_use.browser.browser import Browser, BrowserConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

"""
Example: Using the 'Scroll down' action.

This script demonstrates how the agent can navigate to a webpage and scroll down the content.
If no amount is specified, the agent will scroll down by one page height.
"""

llm = ChatOpenAI(model='gpt-4o')

agent = Agent(
	# task="Navigate to 'https://en.wikipedia.org/wiki/Internet' and scroll down by one page - then scroll up by 100 pixels - then scroll down by 100 pixels - then scroll down by 10000 pixels.",
	task="Navigate to 'https://en.wikipedia.org/wiki/Internet' and scroll to the string 'The vast majority of computer'",
	llm=llm,
	browser=Browser(config=BrowserConfig(headless=False)),
)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: examples/use-cases/test_cv.txt
================================================
123


================================================
File: examples/use-cases/twitter_cookies.txt
================================================
[{
    "name": "auth_token",
    "value": "auth_token_cookie_value",
    "domain": ".x.com",
    "path": "/"
  },
{
    "name": "ct0",
    "value": "ct0_cookie_value",
    "domain": ".x.com",
    "path": "/"
}]


================================================
File: examples/use-cases/twitter_post_using_cookies.py
================================================
import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from browser_use.controller.service import Controller

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))


browser = Browser(
	config=BrowserConfig(
		# chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)
file_path = os.path.join(os.path.dirname(__file__), 'twitter_cookies.txt')
context = BrowserContext(browser=browser, config=BrowserContextConfig(cookies_file=file_path))


async def run_search():
	agent = Agent(
		browser_context=context,
		task=('go to https://x.com. write a new post with the text "browser-use ftw", and submit it'),
		llm=llm,
		max_actions_per_step=4,
	)
	await agent.run(max_steps=25)
	input('Press Enter to close the browser...')


if __name__ == '__main__':
	asyncio.run(run_search())


================================================
File: examples/use-cases/web_voyager_agent.py
================================================
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import os

from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig

browser = Browser(
	config=BrowserConfig(
		headless=False,  # This is True in production
		disable_security=True,
		new_context_config=BrowserContextConfig(
			disable_security=True,
			minimum_wait_page_load_time=1,  # 3 on prod
			maximum_wait_page_load_time=10,  # 20 on prod
			# no_viewport=True,
			browser_window_size={
				'width': 1280,
				'height': 1100,
			},
			# trace_path='./tmp/web_voyager_agent',
		),
	)
)
llm = AzureChatOpenAI(
	model='gpt-4o',
	api_version='2024-10-21',
	azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
	api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
)

# TASK = """
# Find the lowest-priced one-way flight from Cairo to Montreal on February 21, 2025, including the total travel time and number of stops. on https://www.google.com/travel/flights/
# """
# TASK = """
# Browse Coursera, which universities offer Master of Advanced Study in Engineering degrees? Tell me what is the latest application deadline for this degree? on https://www.coursera.org/"""
TASK = """
Find and book a hotel in Paris with suitable accommodations for a family of four (two adults and two children) offering free cancellation for the dates of February 14-21, 2025. on https://www.booking.com/
"""


async def main():
	agent = Agent(
		task=TASK,
		llm=llm,
		browser=browser,
		validate_output=True,
	)
	history = await agent.run(max_steps=50)
	history.save_to_file('./tmp/history.json')


if __name__ == '__main__':
	asyncio.run(main())


================================================
File: tests/test_agent_actions.py
================================================
import asyncio
import os

import pytest
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use.agent.service import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.views import BrowserState


@pytest.fixture
def llm():
	"""Initialize language model for testing"""

	# return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None)
	return AzureChatOpenAI(
		model='gpt-4o',
		api_version='2024-10-21',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)
	# return ChatOpenAI(model='gpt-4o-mini')


@pytest.fixture(scope='session')
def event_loop():
	"""Create an instance of the default event loop for each test case."""
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='session')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context
		# Clean up automatically happens with __aexit__


# pytest tests/test_agent_actions.py -v -k "test_ecommerce_interaction" --capture=no
# @pytest.mark.asyncio
@pytest.mark.skip(reason='Kinda expensive to run')
async def test_ecommerce_interaction(llm, context):
	"""Test complex ecommerce interaction sequence"""
	agent = Agent(
		task="Go to amazon.com, search for 'laptop', filter by 4+ stars, and find the price of the first result",
		llm=llm,
		browser_context=context,
		save_conversation_path='tmp/test_ecommerce_interaction/conversation',
	)

	history: AgentHistoryList = await agent.run(max_steps=20)

	# Verify sequence of actions
	action_sequence = []
	for action in history.model_actions():
		action_name = list(action.keys())[0]
		if action_name in ['go_to_url', 'open_tab']:
			action_sequence.append('navigate')
		elif action_name == 'input_text':
			action_sequence.append('input')
			# Check that the input is 'laptop'
			inp = action['input_text']['text'].lower()  # type: ignore
			if inp == 'laptop':
				action_sequence.append('input_exact_correct')
			elif 'laptop' in inp:
				action_sequence.append('correct_in_input')
			else:
				action_sequence.append('incorrect_input')
		elif action_name == 'click_element':
			action_sequence.append('click')

	# Verify essential steps were performed
	assert 'navigate' in action_sequence  # Navigated to Amazon
	assert 'input' in action_sequence  # Entered search term
	assert 'click' in action_sequence  # Clicked search/filter
	assert 'input_exact_correct' in action_sequence or 'correct_in_input' in action_sequence


# @pytest.mark.asyncio
async def test_error_recovery(llm, context):
	"""Test agent's ability to recover from errors"""
	agent = Agent(
		task='Navigate to nonexistent-site.com and then recover by going to google.com ',
		llm=llm,
		browser_context=context,
	)

	history: AgentHistoryList = await agent.run(max_steps=10)

	actions_names = history.action_names()
	actions = history.model_actions()
	assert (
		'go_to_url' in actions_names or 'open_tab' in actions_names
	), f'{actions_names} does not contain go_to_url or open_tab'
	for action in actions:
		if 'go_to_url' in action:
			assert 'url' in action['go_to_url'], 'url is not in go_to_url'
			assert action['go_to_url']['url'].endswith(
				'google.com'
			), 'url does not end with google.com'
			break


# @pytest.mark.asyncio
async def test_find_contact_email(llm, context):
	"""Test agent's ability to find contact email on a website"""
	agent = Agent(
		task='Go to https://browser-use.com/ and find out the contact email',
		llm=llm,
		browser_context=context,
	)

	history: AgentHistoryList = await agent.run(max_steps=10)

	# Verify the agent found the contact email
	extracted_content = history.extracted_content()
	email = 'info@browser-use.com'
	for content in extracted_content:
		if email in content:
			break
	else:
		pytest.fail(f'{extracted_content} does not contain {email}')


# @pytest.mark.asyncio
async def test_agent_finds_installation_command(llm, context):
	"""Test agent's ability to find the pip installation command for browser-use on the web"""
	agent = Agent(
		task='Find the pip installation command for the browser-use repo',
		llm=llm,
		browser_context=context,
	)

	history: AgentHistoryList = await agent.run(max_steps=10)

	# Verify the agent found the correct installation command
	extracted_content = history.extracted_content()
	install_command = 'pip install browser-use'
	for content in extracted_content:
		if install_command in content:
			break
	else:
		pytest.fail(f'{extracted_content} does not contain {install_command}')


class CaptchaTest(BaseModel):
	name: str
	url: str
	success_text: str
	additional_text: str | None = None


# run 3 test: python -m pytest tests/test_agent_actions.py -v -k "test_captcha_solver" --capture=no --log-cli-level=INFO
# pytest tests/test_agent_actions.py -v -k "test_captcha_solver" --capture=no --log-cli-level=INFO
@pytest.mark.asyncio
@pytest.mark.parametrize(
	'captcha',
	[
		CaptchaTest(
			name='Text Captcha',
			url='https://2captcha.com/demo/text',
			success_text='Captcha is passed successfully!',
		),
		CaptchaTest(
			name='Basic Captcha',
			url='https://captcha.com/demos/features/captcha-demo.aspx',
			success_text='Correct!',
		),
		CaptchaTest(
			name='Rotate Captcha',
			url='https://2captcha.com/demo/rotatecaptcha',
			success_text='Captcha is passed successfully',
			additional_text='Use multiple clicks at once. click done when image is exact correct position.',
		),
		CaptchaTest(
			name='MT Captcha',
			url='https://2captcha.com/demo/mtcaptcha',
			success_text='Verified Successfully',
			additional_text='Stop when you solved it successfully.',
		),
	],
)
async def test_captcha_solver(llm, context, captcha: CaptchaTest):
	"""Test agent's ability to solve different types of captchas"""
	agent = Agent(
		task=f'Go to {captcha.url} and solve the captcha. {captcha.additional_text}',
		llm=llm,
		browser_context=context,
	)
	from browser_use.agent.views import AgentHistoryList

	history: AgentHistoryList = await agent.run(max_steps=7)

	state: BrowserState = await context.get_state()

	all_text = state.element_tree.get_all_text_till_next_clickable_element()

	if not all_text:
		all_text = ''

	if not isinstance(all_text, str):
		all_text = str(all_text)

	solved = captcha.success_text in all_text
	assert solved, f'Failed to solve {captcha.name}'

	# python -m pytest tests/test_agent_actions.py -v --capture=no

	# pytest tests/test_agent_actions.py -v -k "test_captcha_solver" --capture=no --log-cli-level=INFO


================================================
File: tests/test_attach_chrome.py
================================================
import argparse
import asyncio

from playwright.async_api import async_playwright


async def test_full_screen(start_fullscreen: bool, maximize: bool):
	async with async_playwright() as p:
		try:
			print('Attempting to connect to Chrome...')
			# run in terminal: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run
			browser = await p.chromium.connect_over_cdp(
				'http://localhost:9222',
				timeout=20000,  # 20 second timeout for connection
			)
			print('Connected to Chrome successfully')

			# Get the first context and page, or create new ones if needed
			if len(browser.contexts) == 0:
				context = await browser.new_context(ignore_https_errors=True)
			else:
				context = browser.contexts[0]

			if len(context.pages) == 0:
				page = await context.new_page()
			else:
				page = context.pages[0]

			print('Attempting to navigate to Gmail...')
			try:
				# First try with a shorter timeout
				await page.goto(
					'https://mail.google.com',
					wait_until='load',  # Changed from domcontentloaded
					timeout=10000,
				)
			except Exception as e:
				print(f'First navigation attempt failed: {e}')
				print('Trying again with different settings...')
				# If that fails, try again with different settings
				await page.goto(
					'https://mail.google.com',
					wait_until='commit',  # Less strict wait condition
					timeout=30000,
				)

			# Wait for the page to stabilize
			await asyncio.sleep(2)

			print(f'Current page title: {await page.title()}')

			# Optional: wait for specific Gmail elements
			try:
				await page.wait_for_selector('div[role="main"]', timeout=5000)
				print('Gmail interface detected')
			except Exception as e:
				print(f'Note: Gmail interface not detected: {e}')

			await asyncio.sleep(30)
		except Exception as e:
			print(f'An error occurred: {e}')
			import traceback

			traceback.print_exc()
		finally:
			await browser.close()


if __name__ == '__main__':
	asyncio.run(test_full_screen(False, False))


================================================
File: tests/test_core_functionality.py
================================================
import asyncio
import os

import pytest
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.browser.browser import Browser, BrowserConfig


@pytest.fixture(scope='function')
def event_loop():
	"""Create an instance of the default event loop for each test case."""
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='function')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context


@pytest.fixture
def llm():
	"""Initialize language model for testing"""
	return AzureChatOpenAI(
		model='gpt-4o',
		api_version='2024-10-21',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)


# pytest -s -k test_search_google
@pytest.mark.asyncio
async def test_search_google(llm, context):
	"""Test 'Search Google' action"""
	agent = Agent(
		task="Search Google for 'OpenAI'.",
		llm=llm,
		browser_context=context,
	)
	history: AgentHistoryList = await agent.run(max_steps=2)
	action_names = history.action_names()
	assert 'search_google' in action_names


@pytest.mark.asyncio
async def test_go_to_url(llm, context):
	"""Test 'Navigate to URL' action"""
	agent = Agent(
		task="Navigate to 'https://www.python.org'.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=2)
	action_names = history.action_names()
	assert 'go_to_url' in action_names


@pytest.mark.asyncio
async def test_go_back(llm, context):
	"""Test 'Go back' action"""
	agent = Agent(
		task="Go to 'https://www.example.com', then go back.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=3)
	action_names = history.action_names()
	assert 'go_to_url' in action_names
	assert 'go_back' in action_names


@pytest.mark.asyncio
async def test_click_element(llm, context):
	"""Test 'Click element' action"""
	agent = Agent(
		task="Go to 'https://www.python.org' and click on the first link.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=4)
	action_names = history.action_names()
	assert 'go_to_url' in action_names or 'open_tab' in action_names
	assert 'click_element' in action_names


@pytest.mark.asyncio
async def test_input_text(llm, context):
	"""Test 'Input text' action"""
	agent = Agent(
		task="Go to 'https://www.google.com' and input 'OpenAI' into the search box.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=4)
	action_names = history.action_names()
	assert 'go_to_url' in action_names
	assert 'input_text' in action_names


@pytest.mark.asyncio
async def test_switch_tab(llm, context):
	"""Test 'Switch tab' action"""
	agent = Agent(
		task="Open new tabs with 'https://www.google.com' and 'https://www.wikipedia.org', then switch to the first tab.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=6)
	action_names = history.action_names()
	open_tab_count = action_names.count('open_tab')
	assert open_tab_count >= 2
	assert 'switch_tab' in action_names


@pytest.mark.asyncio
async def test_open_new_tab(llm, context):
	"""Test 'Open new tab' action"""
	agent = Agent(
		task="Open a new tab and go to 'https://www.example.com'.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=3)
	action_names = history.action_names()
	assert 'open_tab' in action_names


@pytest.mark.asyncio
async def test_extract_page_content(llm, context):
	"""Test 'Extract page content' action"""
	agent = Agent(
		task="Go to 'https://www.example.com' and extract the page content.",
		llm=llm,
		browser_context=context,
	)
	history = await agent.run(max_steps=3)
	action_names = history.action_names()
	assert 'go_to_url' in action_names
	assert 'extract_content' in action_names


# pytest -k test_done_action
@pytest.mark.asyncio
async def test_done_action(llm, context):
	"""Test 'Complete task' action"""
	agent = Agent(
		task="Navigate to 'https://www.example.com' and signal that the task is done.",
		llm=llm,
		browser_context=context,
	)

	history = await agent.run(max_steps=3)
	action_names = history.action_names()
	assert 'go_to_url' in action_names
	assert 'done' in action_names


# run with: pytest -k test_scroll_down
@pytest.mark.asyncio
async def test_scroll_down(llm, context):
	"""Test 'Scroll down' action and validate that the page actually scrolled"""
	agent = Agent(
		task="Go to 'https://en.wikipedia.org/wiki/Internet' and scroll down the page.",
		llm=llm,
		browser_context=context,
	)
	# Get the browser instance
	page = await context.get_current_page()

	# Navigate to the page and get initial scroll position
	await agent.run(max_steps=1)
	initial_scroll_position = await page.evaluate('window.scrollY;')

	# Perform the scroll down action
	await agent.run(max_steps=2)
	final_scroll_position = await page.evaluate('window.scrollY;')

	# Validate that the scroll position has changed
	assert final_scroll_position > initial_scroll_position, 'Page did not scroll down'

	# Validate that the 'scroll_down' action was executed
	history = agent.history
	action_names = history.action_names()
	assert 'scroll_down' in action_names


================================================
File: tests/test_dropdown.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, AgentHistoryList, Controller

llm = ChatOpenAI(model='gpt-4o')
# browser = Browser(config=BrowserConfig(headless=False))

agent = Agent(
	task=(
		'go to https://codepen.io/geheimschriftstift/pen/mPLvQz and first get all options for the dropdown and then select the 5th option'
	),
	llm=llm,
	browser_context=BrowserContext(
		browser=Browser(config=BrowserConfig(headless=False, disable_security=True)),
	),
)


async def test_dropdown():
	history: AgentHistoryList = await agent.run(20)
	# await controller.browser.close(force=True)

	result = history.final_result()
	assert result is not None
	assert 'Duck' in result
	# await browser.close()


================================================
File: tests/test_dropdown_complex.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, AgentHistoryList, Controller

llm = ChatOpenAI(model='gpt-4o')
# browser = Browser(config=BrowserConfig(headless=False))

agent = Agent(
	task=(
		'go to https://codepen.io/shyam-king/pen/pvzpByJ and first get all options for the dropdown and then select the json option'
	),
	llm=llm,
	browser_context=BrowserContext(
		browser=Browser(config=BrowserConfig(headless=False, disable_security=True)),
	),
)


async def test_dropdown():
	history: AgentHistoryList = await agent.run(20)
	# await controller.browser.close(force=True)

	result = history.final_result()
	assert result is not None
	# await browser.close()


if __name__ == '__main__':
	asyncio.run(test_dropdown())


================================================
File: tests/test_dropdown_error.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, AgentHistoryList, Controller

llm = ChatOpenAI(model='gpt-4o')
# browser = Browser(config=BrowserConfig(headless=False))

agent = Agent(
	task=(
		'go to https://codepen.io/shyam-king/pen/emOyjKm and select number "4" and return the output of "selected value"'
	),
	llm=llm,
	browser_context=BrowserContext(
		browser=Browser(config=BrowserConfig(headless=False, disable_security=True)),
	),
)


async def test_dropdown():
	history: AgentHistoryList = await agent.run(20)
	# await controller.browser.close(force=True)

	result = history.final_result()
	assert result is not None
	assert '4' in result
	print(result)

	# await browser.close()


================================================
File: tests/test_excluded_actions.py
================================================
import asyncio
import os

import pytest
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller

# run with:
# python -m pytest tests/test_excluded_actions.py -v -k "test_only_open_tab_allowed" --capture=no


@pytest.fixture(scope='session')
def event_loop():
	"""Create an instance of the default event loop for each test case."""
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='session')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context


@pytest.fixture
def llm():
	"""Initialize language model for testing"""
	return AzureChatOpenAI(
		model='gpt-4o',
		api_version='2024-10-21',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)


# pytest tests/test_excluded_actions.py -v -k "test_only_open_tab_allowed" --capture=no
@pytest.mark.asyncio
async def test_only_open_tab_allowed(llm, context):
	"""Test that only open_tab action is available while others are excluded"""

	# Create list of all default actions except open_tab
	excluded_actions = [
		'search_google',
		'go_to_url',
		'go_back',
		'click_element',
		'input_text',
		'switch_tab',
		'extract_content',
		'done',
		'scroll_down',
		'scroll_up',
		'send_keys',
		'scroll_to_text',
		'get_dropdown_options',
		'select_dropdown_option',
	]

	# Initialize controller with excluded actions
	controller = Controller(exclude_actions=excluded_actions)

	# Create agent with a task that would normally use other actions
	agent = Agent(
		task="Go to google.com and search for 'python programming'",
		llm=llm,
		browser_context=context,
		controller=controller,
	)

	history: AgentHistoryList = await agent.run(max_steps=2)

	# Verify that only open_tab was used
	action_names = history.action_names()

	# Only open_tab should be in the actions
	assert all(action == 'open_tab' for action in action_names), (
		f'Found unexpected actions: {[a for a in action_names if a != "open_tab"]}'
	)

	# open_tab should be used at least once
	assert 'open_tab' in action_names, 'open_tab action was not used'


================================================
File: tests/test_full_screen.py
================================================
import argparse
import asyncio

from playwright.async_api import async_playwright


async def test_full_screen(start_fullscreen: bool, maximize: bool):
	async with async_playwright() as p:
		browser = await p.chromium.launch(
			headless=False,
			args=['--start-maximized'],
		)
		context = await browser.new_context(no_viewport=True, viewport=None)
		page = await context.new_page()
		await page.goto('https://google.com')

		await asyncio.sleep(10)
		await browser.close()


if __name__ == '__main__':
	asyncio.run(test_full_screen(False, False))


================================================
File: tests/test_gif_path.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_openai import ChatOpenAI

from browser_use import Agent, AgentHistoryList, Controller

llm = ChatOpenAI(model='gpt-4o')

agent = Agent(
	task=(
		'go to google.com and search for text "hi there"'
	),
	llm=llm,
	browser_context=BrowserContext(
		browser=Browser(config=BrowserConfig(headless=False, disable_security=True)),
	),
	generate_gif="./google.gif"
)


async def test_gif_path():
	if os.path.exists("./google.gif"):
		os.unlink("./google.gif")

	history: AgentHistoryList = await agent.run(20)

	result = history.final_result()
	assert result is not None

	assert os.path.exists("./google.gif"), "google.gif was not created"



================================================
File: tests/test_mind2web.py
================================================
"""
Test browser automation using Mind2Web dataset tasks with pytest framework.
"""

import asyncio
import json
import os
from typing import Any, Dict, List

import pytest
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.utils import logger

# Constants
MAX_STEPS = 50
TEST_SUBSET_SIZE = 10


@pytest.fixture(scope='session')
def event_loop():
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='session')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as new_context:
		yield new_context


@pytest.fixture(scope='session')
def test_cases() -> List[Dict[str, Any]]:
	"""Load test cases from Mind2Web dataset"""
	file_path = os.path.join(os.path.dirname(__file__), 'mind2web_data/processed.json')
	logger.info(f'Loading test cases from {file_path}')

	with open(file_path, 'r') as f:
		data = json.load(f)

	subset = data[:TEST_SUBSET_SIZE]
	logger.info(f'Loaded {len(subset)}/{len(data)} test cases')
	return subset


@pytest.fixture
def llm():
	"""Initialize language model for testing"""

	# return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None)
	return AzureChatOpenAI(
		model='gpt-4o',
		api_version='2024-10-21',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)


# run with: pytest -s -v tests/test_mind2web.py:test_random_samples
@pytest.mark.asyncio
async def test_random_samples(test_cases: List[Dict[str, Any]], llm, context, validator):
	"""Test a random sampling of tasks across different websites"""
	import random

	logger.info('=== Testing Random Samples ===')

	# Take random samples
	samples = random.sample(test_cases, 1)

	for i, case in enumerate(samples, 1):
		task = f"Go to {case['website']}.com and {case['confirmed_task']}"
		logger.info(f'--- Random Sample {i}/{len(samples)} ---')
		logger.info(f'Task: {task}\n')

		agent = Agent(task, llm, browser_context=context)

		await agent.run()

		logger.info('Validating random sample task...')

		# TODO: Validate the task


def test_dataset_integrity(test_cases):
	"""Test the integrity of the test dataset"""
	logger.info('\n=== Testing Dataset Integrity ===')

	required_fields = ['website', 'confirmed_task', 'action_reprs']
	missing_fields = []

	logger.info(f'Checking {len(test_cases)} test cases for required fields')

	for i, case in enumerate(test_cases, 1):
		logger.debug(f'Checking case {i}/{len(test_cases)}')

		for field in required_fields:
			if field not in case:
				missing_fields.append(f'Case {i}: {field}')
				logger.warning(f"Missing field '{field}' in case {i}")

		# Type checks
		if not isinstance(case.get('confirmed_task'), str):
			logger.error(f"Case {i}: 'confirmed_task' must be string")
			assert False, 'Task must be string'

		if not isinstance(case.get('action_reprs'), list):
			logger.error(f"Case {i}: 'action_reprs' must be list")
			assert False, 'Actions must be list'

		if len(case.get('action_reprs', [])) == 0:
			logger.error(f"Case {i}: 'action_reprs' must not be empty")
			assert False, 'Must have at least one action'

	if missing_fields:
		logger.error('Dataset integrity check failed')
		assert False, f'Missing fields: {missing_fields}'
	else:
		logger.info('✅ Dataset integrity check passed')


if __name__ == '__main__':
	pytest.main([__file__, '-v'])


================================================
File: tests/test_models.py
================================================
import asyncio
import os

import pytest
import requests
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult, AgentHistoryList
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.views import BrowserState, TabInfo
from browser_use.dom.views import DOMElementNode, DOMTextNode


@pytest.fixture(scope='function')
def event_loop():
	"""Create an instance of the default event loop for each test case."""
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='function')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context


api_key_gemini = SecretStr(os.getenv('GEMINI_API_KEY') or '')
api_key_deepseek = SecretStr(os.getenv('DEEPSEEK_API_KEY') or '')
api_key_anthropic = SecretStr(os.getenv('ANTHROPIC_API_KEY') or '')


# pytest -s -v tests/test_models.py
@pytest.fixture(
	params=[
		# run: ollama start
		ChatOpenAI(
			base_url='https://api.deepseek.com/v1',
			model='deepseek-reasoner',
			api_key=api_key_deepseek,
		),
		ChatOllama(
			model='qwen2.5:latest',
			num_ctx=128000,
		),
		AzureChatOpenAI(
			model='gpt-4o-mini',
			api_version='2024-10-21',
			azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
			api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
		),
		ChatAnthropic(
			model_name='claude-3-5-sonnet-20240620',
			timeout=100,
			temperature=0.0,
			stop=None,
			api_key=api_key_anthropic,
		),
		ChatOpenAI(model='gpt-4o'),
		ChatOpenAI(model='gpt-4o-mini'),
		AzureChatOpenAI(
			model='gpt-4o',
			api_version='2024-10-21',
			azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
			api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
		),
		ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=api_key_gemini),
		ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=api_key_gemini),
		ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', api_key=api_key_gemini),
		ChatOpenAI(
			base_url='https://api.deepseek.com/v1',
			model='deepseek-chat',
			api_key=api_key_deepseek,
		),
	],
	ids=[
		'deepseek-reasoner',
		'qwen2.5:latest',
		'azure-gpt-4o-mini',
		'claude-3-5-sonnet',
		'gpt-4o',
		'gpt-4o-mini',
		'azure-gpt-4o',
		'gemini-2.0-flash-exp',
		'gemini-1.5-pro',
		'gemini-1.5-flash-latest',
		'deepseek-chat',
	],
)
async def llm(request):
	return request.param


@pytest.mark.asyncio
async def test_model_search(llm, context):
	"""Test 'Search Google' action"""
	model_name = llm.model if hasattr(llm, 'model') else llm.model_name
	print(f'\nTesting model: {model_name}')

	use_vision = True
	models_without_vision = ['deepseek-chat', 'deepseek-reasoner']
	if hasattr(llm, 'model') and llm.model in models_without_vision:
		use_vision = False
	elif hasattr(llm, 'model_name') and llm.model_name in models_without_vision:
		use_vision = False

	# require ollama run
	local_models = ['qwen2.5:latest']
	if model_name in local_models:
		# check if ollama is running
		# ping ollama http://127.0.0.1
		try:
			response = requests.get('http://127.0.0.1:11434/')
			if response.status_code != 200:
				raise
		except Exception as e:
			raise Exception('Ollama is not running - start with `ollama start`')

	agent = Agent(
		task="Search Google for 'elon musk' then click on the first result and scroll down.",
		llm=llm,
		browser_context=context,
		max_failures=2,
		use_vision=use_vision,
	)
	history: AgentHistoryList = await agent.run(max_steps=2)
	action_names = history.action_names()
	print(f'Actions performed: {action_names}')
	errors = history.errors()
	errors = '\n'.join(errors)
	passed = False
	if 'search_google' in action_names:
		passed = True
	elif 'go_to_url' in action_names:
		passed = True
	elif 'open_tab' in action_names:
		passed = True

	else:
		passed = False
	print(f'Model {model_name}: {"✅ PASSED" if passed else "❌ FAILED"}')

	assert passed, f'Model {model_name} not working\nActions performed: {action_names}\nErrors: {errors}'


================================================
File: tests/test_qwen.py
================================================
import asyncio
import os

import pytest
from langchain_ollama import ChatOllama
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use.agent.service import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.views import BrowserState


@pytest.fixture
def llm():
	"""Initialize language model for testing"""

	# return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None)
	# NOTE: Make sure to run ollama server with `ollama start'
	return ChatOllama(
		model='qwen2.5:latest',
		num_ctx=128000,
	)


@pytest.fixture(scope='session')
def event_loop():
	"""Create an instance of the default event loop for each test case."""
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='session')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context


# pytest tests/test_qwen.py -v -k "test_qwen_url" --capture=no
# @pytest.mark.asyncio
async def test_qwen_url(llm, context):
	"""Test complex ecommerce interaction sequence"""
	agent = Agent(
		task='go_to_url amazon.com',
		llm=llm,
	)

	history: AgentHistoryList = await agent.run(max_steps=3)

	# Verify sequence of actions
	action_sequence = []
	for action in history.model_actions():
		action_name = list(action.keys())[0]
		if action_name in ['go_to_url', 'open_tab']:
			action_sequence.append('navigate')

	assert 'navigate' in action_sequence  # Navigated to Amazon


================================================
File: tests/test_react_dropdown.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent, AgentHistoryList, Controller

llm = ChatOpenAI(model='gpt-4o')
# browser = Browser(config=BrowserConfig(headless=False))

agent = Agent(
	task=(
		'go to https://codepen.io/shyam-king/pen/ByBJoOv and select "Tiger" dropdown and read the text given in "Selected Animal" box (it can be empty as well)'
	),
	llm=llm,
	browser_context=BrowserContext(
		browser=Browser(config=BrowserConfig(headless=False, disable_security=True)),
	),
)


async def test_dropdown():
	history: AgentHistoryList = await agent.run(10)
	# await controller.browser.close(force=True)

	result = history.final_result()
	assert result is not None
	print('result: ', result)
	# await browser.close()


if __name__ == '__main__':
	asyncio.run(test_dropdown())


================================================
File: tests/test_self_registered_actions.py
================================================
import asyncio
import os

import pytest
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use.agent.service import Agent
from browser_use.agent.views import AgentHistoryList
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller


@pytest.fixture(scope='session')
def event_loop():
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='session')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context


@pytest.fixture
async def controller():
	"""Initialize the controller with self-registered actions"""
	controller = Controller()

	# Define custom actions without Pydantic models
	@controller.action('Print a message')
	def print_message(message: str):
		print(f'Message: {message}')
		return f'Printed message: {message}'

	@controller.action('Add two numbers')
	def add_numbers(a: int, b: int):
		result = a + b
		return f'The sum is {result}'

	@controller.action('Concatenate strings')
	def concatenate_strings(str1: str, str2: str):
		result = str1 + str2
		return f'Concatenated string: {result}'

	# Define Pydantic models
	class SimpleModel(BaseModel):
		name: str
		age: int

	class Address(BaseModel):
		street: str
		city: str

	class NestedModel(BaseModel):
		user: SimpleModel
		address: Address

	# Add actions with Pydantic model arguments
	@controller.action('Process simple model', param_model=SimpleModel)
	def process_simple_model(model: SimpleModel):
		return f'Processed {model.name}, age {model.age}'

	@controller.action('Process nested model', param_model=NestedModel)
	def process_nested_model(model: NestedModel):
		user_info = f'{model.user.name}, age {model.user.age}'
		address_info = f'{model.address.street}, {model.address.city}'
		return f'Processed user {user_info} at address {address_info}'

	@controller.action('Process multiple models')
	def process_multiple_models(model1: SimpleModel, model2: Address):
		return f'Processed {model1.name} living at {model2.street}, {model2.city}'

	yield controller


@pytest.fixture
def llm():
	"""Initialize language model for testing"""

	# return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None)
	return AzureChatOpenAI(
		model='gpt-4o',
		api_version='2024-10-21',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)


# @pytest.mark.skip(reason="Skipping test for now")
@pytest.mark.asyncio
async def test_self_registered_actions_no_pydantic(llm, controller):
	"""Test self-registered actions with individual arguments"""
	agent = Agent(
		task="First, print the message 'Hello, World!'. Then, add 10 and 20. Next, concatenate 'foo' and 'bar'.",
		llm=llm,
		controller=controller,
	)
	history: AgentHistoryList = await agent.run(max_steps=10)
	# Check that custom actions were executed
	action_names = history.action_names()

	assert 'print_message' in action_names
	assert 'add_numbers' in action_names
	assert 'concatenate_strings' in action_names


# @pytest.mark.skip(reason="Skipping test for now")
@pytest.mark.asyncio
async def test_mixed_arguments_actions(llm, controller):
	"""Test actions with mixed argument types"""

	# Define another action during the test
	# Test for async actions
	@controller.action('Calculate the area of a rectangle')
	async def calculate_area(length: float, width: float):
		area = length * width
		return f'The area is {area}'

	agent = Agent(
		task='Calculate the area of a rectangle with length 5.5 and width 3.2.',
		llm=llm,
		controller=controller,
	)
	history = await agent.run(max_steps=5)

	# Check that the action was executed
	action_names = history.action_names()

	assert 'calculate_area' in action_names
	# check result
	correct = 'The area is 17.6'
	for content in history.extracted_content():
		if correct in content:
			break
	else:
		pytest.fail(f'{correct} not found in extracted content')


@pytest.mark.asyncio
async def test_pydantic_simple_model(llm, controller):
	"""Test action with a simple Pydantic model argument"""
	agent = Agent(
		task="Process a simple model with name 'Alice' and age 30.",
		llm=llm,
		controller=controller,
	)
	history = await agent.run(max_steps=5)

	# Check that the action was executed
	action_names = history.action_names()

	assert 'process_simple_model' in action_names
	correct = 'Processed Alice, age 30'
	for content in history.extracted_content():
		if correct in content:
			break
	else:
		pytest.fail(f'{correct} not found in extracted content')


@pytest.mark.asyncio
async def test_pydantic_nested_model(llm, controller):
	"""Test action with a nested Pydantic model argument"""
	agent = Agent(
		task="Process a nested model with user name 'Bob', age 25, living at '123 Maple St', 'Springfield'.",
		llm=llm,
		controller=controller,
	)
	history = await agent.run(max_steps=5)

	# Check that the action was executed
	action_names = history.action_names()

	assert 'process_nested_model' in action_names
	correct = 'Processed user Bob, age 25 at address 123 Maple St, Springfield'
	for content in history.extracted_content():
		if correct in content:
			break
	else:
		pytest.fail(f'{correct} not found in extracted content')


# run this file with:
# pytest tests/test_self_registered_actions.py --capture=no


================================================
File: tests/test_service.py
================================================
import os
import pytest
import sys

from browser_use.agent.message_manager.service import MessageManager
from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult, AgentOutput
from browser_use.browser.browser import Browser
from browser_use.browser.context import BrowserContext
from browser_use.browser.views import BrowserState
from browser_use.controller.registry.service import Registry
from browser_use.controller.registry.views import ActionModel
from browser_use.controller.service import Controller
from langchain_core.language_models.chat_models import BaseChatModel
from pydantic import BaseModel
from unittest.mock import AsyncMock, MagicMock, Mock, patch

# run with python -m pytest tests/test_service.py

# run test with:
# python -m pytest tests/test_service.py
class TestAgent:
	@pytest.fixture
	def mock_controller(self):
		controller = Mock(spec=Controller)
		registry = Mock(spec=Registry)
		registry.registry = MagicMock()
		registry.registry.actions = {'test_action': MagicMock(param_model=MagicMock())}  # type: ignore
		controller.registry = registry
		return controller

	@pytest.fixture
	def mock_llm(self):
		return Mock(spec=BaseChatModel)

	@pytest.fixture
	def mock_browser(self):
		return Mock(spec=Browser)

	@pytest.fixture
	def mock_browser_context(self):
		return Mock(spec=BrowserContext)

	def test_convert_initial_actions(self, mock_controller, mock_llm, mock_browser, mock_browser_context):  # type: ignore
		"""
		Test that the _convert_initial_actions method correctly converts
		dictionary-based actions to ActionModel instances.

		This test ensures that:
		1. The method processes the initial actions correctly.
		2. The correct param_model is called with the right parameters.
		3. The ActionModel is created with the validated parameters.
		4. The method returns a list of ActionModel instances.
		"""
		# Arrange
		agent = Agent(
			task='Test task', llm=mock_llm, controller=mock_controller, browser=mock_browser, browser_context=mock_browser_context
		)
		initial_actions = [{'test_action': {'param1': 'value1', 'param2': 'value2'}}]

		# Mock the ActionModel
		mock_action_model = MagicMock(spec=ActionModel)
		mock_action_model_instance = MagicMock()
		mock_action_model.return_value = mock_action_model_instance
		agent.ActionModel = mock_action_model  # type: ignore

		# Act
		result = agent._convert_initial_actions(initial_actions)

		# Assert
		assert len(result) == 1
		mock_controller.registry.registry.actions['test_action'].param_model.assert_called_once_with(  # type: ignore
			param1='value1', param2='value2'
		)
		mock_action_model.assert_called_once()
		assert isinstance(result[0], MagicMock)
		assert result[0] == mock_action_model_instance

		# Check that the ActionModel was called with the correct parameters
		call_args = mock_action_model.call_args[1]
		assert 'test_action' in call_args
		assert call_args['test_action'] == mock_controller.registry.registry.actions['test_action'].param_model.return_value  # type: ignore

	@pytest.mark.asyncio
	async def test_step_error_handling(self):
		"""
		Test the error handling in the step method of the Agent class.
		This test simulates a failure in the get_next_action method and
		checks if the error is properly handled and recorded.
		"""
		# Mock the LLM
		mock_llm = MagicMock(spec=BaseChatModel)

		# Mock the MessageManager
		with patch('browser_use.agent.service.MessageManager') as mock_message_manager:
			# Create an Agent instance with mocked dependencies
			agent = Agent(task='Test task', llm=mock_llm)

			# Mock the get_next_action method to raise an exception
			agent.get_next_action = AsyncMock(side_effect=ValueError('Test error'))

			# Mock the browser_context
			agent.browser_context = AsyncMock()
			agent.browser_context.get_state = AsyncMock(
				return_value=BrowserState(
					url='https://example.com',
					title='Example',
					element_tree=MagicMock(),  # Mocked element tree
					tabs=[],
					selector_map={},
					screenshot='',
				)
			)

			# Mock the controller
			agent.controller = AsyncMock()

			# Call the step method
			await agent.step()

			# Assert that the error was handled and recorded
			assert agent.consecutive_failures == 1
			assert len(agent._last_result) == 1
			assert isinstance(agent._last_result[0], ActionResult)
			assert 'Test error' in agent._last_result[0].error
			assert agent._last_result[0].include_in_memory == True

class TestRegistry:
    @pytest.fixture
    def registry_with_excludes(self):
        return Registry(exclude_actions=['excluded_action'])

    def test_action_decorator_with_excluded_action(self, registry_with_excludes):
        """
        Test that the action decorator does not register an action
        if it's in the exclude_actions list.
        """
        # Define a function to be decorated
        def excluded_action():
            pass

        # Apply the action decorator
        decorated_func = registry_with_excludes.action(description="This should be excluded")(excluded_action)

        # Assert that the decorated function is the same as the original
        assert decorated_func == excluded_action

        # Assert that the action was not added to the registry
        assert 'excluded_action' not in registry_with_excludes.registry.actions

        # Define another function that should be included
        def included_action():
            pass

        # Apply the action decorator to an included action
        registry_with_excludes.action(description="This should be included")(included_action)

        # Assert that the included action was added to the registry
        assert 'included_action' in registry_with_excludes.registry.actions

    @pytest.mark.asyncio
    async def test_execute_action_with_and_without_browser_context(self):
        """
        Test that the execute_action method correctly handles actions with and without a browser context.
        This test ensures that:
        1. An action requiring a browser context is executed correctly.
        2. An action not requiring a browser context is executed correctly.
        3. The browser context is passed to the action function when required.
        4. The action function receives the correct parameters.
        5. The method raises an error when a browser context is required but not provided.
        """
        registry = Registry()

        # Define a mock action model
        class TestActionModel(BaseModel):
            param1: str

        # Define mock action functions
        async def test_action_with_browser(param1: str, browser):
            return f"Action executed with {param1} and browser"

        async def test_action_without_browser(param1: str):
            return f"Action executed with {param1}"

        # Register the actions
        registry.registry.actions['test_action_with_browser'] = MagicMock(
            requires_browser=True,
            function=AsyncMock(side_effect=test_action_with_browser),
            param_model=TestActionModel,
            description="Test action with browser"
        )

        registry.registry.actions['test_action_without_browser'] = MagicMock(
            requires_browser=False,
            function=AsyncMock(side_effect=test_action_without_browser),
            param_model=TestActionModel,
            description="Test action without browser"
        )

        # Mock BrowserContext
        mock_browser = MagicMock()

        # Execute the action with a browser context
        result_with_browser = await registry.execute_action('test_action_with_browser', {'param1': 'test_value'}, browser=mock_browser)
        assert result_with_browser == "Action executed with test_value and browser"

        # Execute the action without a browser context
        result_without_browser = await registry.execute_action('test_action_without_browser', {'param1': 'test_value'})
        assert result_without_browser == "Action executed with test_value"

        # Test error when browser is required but not provided
        with pytest.raises(RuntimeError, match="Action test_action_with_browser requires browser but none provided"):
            await registry.execute_action('test_action_with_browser', {'param1': 'test_value'})

        # Verify that the action functions were called with correct parameters
        registry.registry.actions['test_action_with_browser'].function.assert_called_once_with(param1='test_value', browser=mock_browser)
        registry.registry.actions['test_action_without_browser'].function.assert_called_once_with(param1='test_value')

================================================
File: tests/test_stress.py
================================================
import asyncio
import os
import random
import string
import time

import pytest
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller


@pytest.fixture(scope='session')
def event_loop():
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope='session')
async def browser(event_loop):
	browser_instance = Browser(
		config=BrowserConfig(
			headless=True,
		)
	)
	yield browser_instance
	await browser_instance.close()


@pytest.fixture
async def context(browser):
	async with await browser.new_context() as context:
		yield context


@pytest.fixture
def llm():
	"""Initialize the language model"""
	model = AzureChatOpenAI(
		api_version='2024-10-21',
		model='gpt-4o',
		azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
		api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
	)
	return model


def generate_random_text(length: int) -> str:
	"""Generate random text of specified length"""
	return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))


@pytest.fixture
async def controller():
	"""Initialize the controller"""
	controller = Controller()
	large_text = generate_random_text(10000)

	@controller.action('call this magical function to get very special text')
	def get_very_special_text():
		return large_text

	yield controller


@pytest.mark.asyncio
async def test_token_limit_with_multiple_extractions(llm, controller, context):
	"""Test handling of multiple smaller extractions accumulating tokens"""
	agent = Agent(
		task='Call the magical function to get very special text 5 times',
		llm=llm,
		controller=controller,
		browser_context=context,
		max_input_tokens=2000,
		save_conversation_path='tmp/stress_test/test_token_limit_with_multiple_extractions.json',
	)

	history = await agent.run(max_steps=5)

	# check if 5 times called get_special_text
	calls = [a for a in history.action_names() if a == 'get_very_special_text']
	assert len(calls) == 5
	# check the message history should be max 3 messages
	assert len(agent.message_manager.history.messages) > 3


@pytest.mark.slow
@pytest.mark.parametrize('max_tokens', [4000])  # 8000 20000
@pytest.mark.asyncio
async def test_open_3_tabs_and_extract_content(llm, controller, context, max_tokens):
	"""Stress test: Open 3 tabs with urls and extract content"""
	agent = Agent(
		task='Open 3 tabs with https://en.wikipedia.org/wiki/Internet and extract the content from each.',
		llm=llm,
		controller=controller,
		browser_context=context,
		max_input_tokens=max_tokens,
		save_conversation_path='tmp/stress_test/test_open_3_tabs_and_extract_content.json',
	)
	start_time = time.time()
	history = await agent.run(max_steps=7)
	end_time = time.time()

	total_time = end_time - start_time

	print(f'Total time: {total_time:.2f} seconds')
	# Check for errors
	errors = history.errors()
	assert len(errors) == 0, 'Errors occurred during the test'
	# check if 3 tabs were opened
	assert len(context.current_state.tabs) >= 3, '3 tabs were not opened'


================================================
File: tests/test_vision.py
================================================
"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import json
import os
import sys
from doctest import OutputChecker
from pprint import pprint

import pytest

from browser_use.browser.browser import Browser, BrowserConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI

from browser_use import ActionModel, Agent, AgentHistoryList, Controller
from browser_use.agent.views import AgentOutput

llm = ChatOpenAI(model='gpt-4o')
controller = Controller()

# use this test to ask the model questions about the page like
# which color do you see for bbox labels, list all with their label
# whats the smallest bboxes with labels and


@controller.registry.action(description='explain what you see on the screen and ask user for input')
async def explain_screen(text: str) -> str:
	pprint(text)
	answer = input('\nuser input next question: \n')
	return answer


@controller.registry.action(description='done')
async def done(text: str) -> str:
	# pprint(text)
	return 'call explain_screen'


agent = Agent(
	task='call explain_screen all the time the user asks you questions e.g. about the page like bbox which you see are labels  - your task is to expalin it and get the next question',
	llm=llm,
	controller=controller,
	browser=Browser(config=BrowserConfig(disable_security=True, headless=False)),
)


@pytest.mark.skip(reason='this is for local testing only')
async def test_vision():
	history: AgentHistoryList = await agent.run(20)


================================================
File: .github/ISSUE_TEMPLATE/bug_report.yml
================================================
name: 🐛 Bug Report
description: Report a bug in browser-use
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report! Please fill out the form below to help us reproduce and fix the issue.

  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: A clear and concise description of what the bug is.
      placeholder: When I try to... the library...
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction Steps
      description: Steps to reproduce the behavior
      placeholder: |
        1. Install browser-use...
        2. Run the following task...
        3. See error...
    validations:
      required: true

  - type: textarea
    id: code
    attributes:
      label: Code Sample
      description: Include a minimal code sample that reproduces the issue
      render: python
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: Version
      description: What version of browser-use are you using? (Run `uv pip show browser-use` to find out)
      placeholder: "e.g., pip 0.1.26, or git main branch"
    validations:
      required: true

  - type: dropdown
    id: model
    attributes:
      label: LLM Model
      description: Which LLM model(s) are you using?
      multiple: true
      options:
        - GPT-4o
        - GPT-4
        - Claude 3.5 Sonnet
        - Claude 3.5 Opus
        - Claude 3.5 Haiku
        - Gemini 1.5 Pro
        - Gemini 1.5 Ultra
        - Fireworks Mixtral
        - DeepSeek Coder
        - Local Model (Specify model in description)
        - Other (specify in description)
    validations:
      required: true

  - type: input
    id: os
    attributes:
      label: Operating System
      description: What operating system are you using?
      placeholder: "e.g., macOS 13.1, Windows 11, Ubuntu 22.04"
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Relevant Log Output
      description: Please copy and paste any relevant log output. This will be automatically formatted into code.
      render: shell

================================================
File: .github/ISSUE_TEMPLATE/config.yml
================================================
blank_issues_enabled: false  # Set to true if you want to allow blank issues
contact_links:
  - name: 🤔 Quickstart Guide
    url: https://docs.browser-use.com/quickstart
    about: Most common issues can be resolved by following our quickstart guide
  - name: 🤔 Questions and Help
    url: https://link.browser-use.com/discord
    about: Please ask questions in our Discord community
  - name: 📖 Documentation
    url: https://docs.browser-use.com
    about: Check our documentation for answers first 

================================================
File: .github/ISSUE_TEMPLATE/docs_issue.yml
================================================
name: 📚 Documentation Issue
description: Report an issue in the browser-use documentation
labels: ["documentation"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to improve our documentation! Please fill out the form below to help us understand the issue.

  - type: dropdown
    id: type
    attributes:
      label: Type of Documentation Issue
      description: What type of documentation issue is this?
      options:
        - Missing documentation
        - Incorrect documentation
        - Unclear documentation
        - Broken link
        - Other (specify in description)
    validations:
      required: true

  - type: input
    id: page
    attributes:
      label: Documentation Page
      description: Which page or section of the documentation is this about?
      placeholder: "e.g., https://docs.browser-use.com/getting-started or Installation Guide"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Issue Description
      description: Describe what's wrong or missing in the documentation
      placeholder: The documentation should...
    validations:
      required: true

  - type: textarea
    id: suggestion
    attributes:
      label: Suggested Changes
      description: If you have specific suggestions for how to improve the documentation, please share them
      placeholder: |
        The documentation could be improved by...
        
        Example:
        ```python
        # Your suggested code example or text here
        ```
    validations:
      required: true

================================================
File: .github/ISSUE_TEMPLATE/feature_request.yml
================================================
name: 💡 Feature Request
description: Suggest a new feature for browser-use
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to suggest a new feature! Please fill out the form below to help us understand your suggestion.

  - type: textarea
    id: problem
    attributes:
      label: Problem Description
      description: Is your feature request related to a problem? Please describe.
      placeholder: I'm always frustrated when...
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: Proposed Solution
      description: Describe the solution you'd like to see
      placeholder: It would be great if...
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Alternative Solutions
      description: Describe any alternative solutions or features you've considered
      placeholder: I've also thought about...

  - type: textarea
    id: context
    attributes:
      label: Additional Context
      description: Add any other context or examples about the feature request here
      placeholder: |
        - Example use cases
        - Screenshots or mockups
        - Related issues or discussions 

================================================
File: .github/workflows/publish.yml
================================================
# This workflow will upload a Python Package using Twine when a release is created
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#publishing-to-package-registries

# This workflow uses actions that are not certified by GitHub.
# They are provided by a third-party and are governed by
# separate terms of service, privacy policy, and support
# documentation.

name: Upload Python Package

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build hatch
      - name: Build package
        run: python -m build
      - name: Publish package
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}


