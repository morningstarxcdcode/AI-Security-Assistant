from setuptools import setup, find_packages

setup(
    name='ai_security_assistant',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'requests',
        'pytest',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'ai-security-assistant=main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Next-generation AI-assisted security assistant with black box AI orchestration',
    url='https://github.com/yourusername/ai_security_assistant',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
