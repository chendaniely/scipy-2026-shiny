# run this script with
# python code/demos/ai-03-tools.py
from dotenv import load_dotenv
from chatlas import ChatGithub, ChatAnthropic

 # this is the path to the .env file relative to working directory
load_dotenv('.env')

def scipy_locations(year: int) -> str:
    """Looks up the location SciPy is held given a year.

    Parameters
    ----------
    year : int
        The year of the SciPy conference.

    Returns
    -------
    str
        The city and region where SciPy is held that year, or a message
        indicating the location is unknown.
    """
    match year:
        case 2027:
            return "The Moon"
        case 2026:
            return "Tacoma, WA"
        case 2025:
            return "Tacoma, WA"

chat = ChatGithub(model="gpt-5")
#chat = ChatAnthropic()

chat.register_tool(scipy_locations)

chat.chat("Where is SciPy 2027 being held?")
