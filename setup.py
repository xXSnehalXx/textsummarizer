import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_descrption= f.read()

__version__ = "0.0.1"
REPO_NAME= "textsummarizer"
AUTHOR_USER_NAME= "xXSnehalXx"
SRC_REPO= "textsummarizer"
AUTHOR_EMAIL= "snehalmachan@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python project for NLP App",
    long_description= long_descrption,
    long_description_content_type= "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls= {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues"
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(),
)

