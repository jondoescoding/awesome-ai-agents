from setuptools import setup, find_packages

setup(
    name="curve_api_agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "llama-index>=0.9.8",
        "python-dotenv>=1.0.0",
        "openai>=1.3.0",
        "aiohttp>=3.9.1"
    ],
) 