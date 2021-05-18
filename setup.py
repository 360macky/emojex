from setuptools import setup, find_packages

VERSION = '0.0.9'
DESCRIPTION = 'Smart converter of popular culture texts to emoji'
LONG_DESCRIPTION = 'Converter of popular culture texts such as series or movies to emoji using OpenAI GPT-3'

setup(
    name="emojex",
    version=VERSION,
    author="360macky (Marcelo Arias)",
    author_email="<mail.marcelo.as@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['openai'],
    keywords=['python', 'emoji', 'openai', 'gpt-3', 'converter', 'text'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
