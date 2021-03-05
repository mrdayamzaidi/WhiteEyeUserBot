from rotten_tomatoes_client import RottenTomatoesClient

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd, sudo_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern="rt (.*)"))
@WhiteEye.on(sudo_cmd(pattern="rt (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    result = RottenTomatoesClient.search(term=input_str, limit=1)

    l = result.get("movies")[0]
    name = l.get("name")
    year = l.get("year")
    l.get("image")
    Classe = l.get("meterClass")
    Meter = l.get("meterScore")
    ullu = l.get("url")
    url = f"http://rottentomatoes.com{ullu}"
    Ceset = l.get("castItems")
    cast = ""
    for Hitler in Ceset:
        cast += Hitler.get("name") + "\n"
    caption = f"""Name : {name}
Year Of Release : {year}
Link : {url}
Meter Class : {Classe}
Meter Score : {Meter}
Cast : 
{cast}"""
    await borg.send_message(
        event.chat_id,
        caption,
    )


CMD_HELP.update(
    {
        "rottentomatoes": "**Rotten Tomatoes**\
\n\n**Syntax : **`.rt <Movie name>`\
\n**Usage :** Gives Rating and cast Of The Movie.\
\n\n**Example : **`.rt tenet`\
\nThis above syntax Gives Rating and cast of tenet"
    }
)