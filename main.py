import urllib.request
import scratchattach as scratch3
import time
from PIL import Image

session = scratch3.login("CoolBotABC123AWESOME", "#")


conn = session.connect_cloud("983994522")



while True:
    try:
        if scratch3.get_var(983994522, "start") == "1":
            time.sleep(0.1)
            i = 0
            print("debug")

            user = scratch3.get_user(scratch3.Encoding.decode(scratch3.get_var(983994522, "user"))).id
            url = "https://uploads.scratch.mit.edu/get_image/user/"+str(user)+"_30x30.png"

            urllib.request.urlretrieve(url, "avatar.png")

            time.sleep(0.1)
            
            img = Image.open("avatar.png").convert("RGB")
            img = img.resize((15, 15))
            width, height = img.size
            pixels = img.load()

            for y in range(height):
                for x in range(width):
                    time.sleep(0.1)
                    r, g, b = pixels[x, y]
                    color = r * 65536 + g * 256 + b
                    i += 1
                    time.sleep(0.2)
                    conn.set_var("i", i)
                    print(i)
                    conn.set_var("color", color)
            conn.set_var("start", 0)
    except scratch3.exceptions.UserNotFound:
        conn.set_var("i", 255)
        conn.set_var("start", 0)
        


