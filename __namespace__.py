NAME: str = "rtalign"
AUTHOR: str = "C. Lucas, S. Dubois",
AUTHOR_EMAIL: str = "siegfried.dubois@inria.fr",
LICENCE: str = "LICENCE"
DESCRIPTION: str = "Random-tubed alignment of sequences"
REQUIRED_PYTHON: tuple = (3, 10)
WORKSPACE: str = "rtalign"
MAIN_MODULE: str = "main"
MAIN_FUNC: str = "main"

# Change this to ovveride default version number
OVERRIDE_VN: bool = True
VN: str = "0.0.1"

# Fill this part if your tool features command-line interface
HAS_COMMAND_LINE: bool = True
COMMAND: dict = {'console_scripts': [
    f'{NAME}={WORKSPACE}.{MAIN_MODULE}:{MAIN_FUNC}']}
