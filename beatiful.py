html="""
<html>
    <head>
        <title>test web</title>
    </head>
    <body>
        <p align="center">text contents</p>
        <img src="c:\python34\koaja.jpg" width="500" height="300">
    </body>
</html>"""


from bs4 import Be
bs=BeautifulSoup(html)
print(bs.find("title"))
