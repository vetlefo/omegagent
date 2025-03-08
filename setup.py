from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    # Filter out comments and empty lines
    install_requires = [
        line.split('#')[0].strip() for line in f
        if line.strip() and not line.strip().startswith('#')
    ]

# Read dev requirements if available
dev_requires = []
if os.path.exists('dev-requirements.txt'):
    with open('dev-requirements.txt') as f:
        dev_requires = [
            line.split('#')[0].strip() for line in f
            if line.strip() and not line.strip().startswith('#')
        ]

setup(
    name="agentic_research",
    version="0.1.0",
    description="Framework for agentic reasoning and collaborative problem solving",
    packages=find_packages() + ['scripts', 'scripts.tools', 'tests', 'tests.utils', 'tests.unit', 'tests.integration'],
    package_data={
        'tests': ['*'],  # Include all files in tests directory
    },
    python_requires='>=3.11.0',
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'graph': ['nano-graphrag>=0.0.8.2', 'gensim>=4.3.0'],
        'qdrant': ['qdrant-client>=1.13.0', 'langchain-qdrant>=0.2.0'],
        'search': ['duckduckgo-search>=7.3.0', 'bing-search>=1.0.0', 'jina>=3.0.0'],
    }
)