
import math
import time
import datetime
from demo_opts import get_device
from luma.core.render import canvas

def main():
    today_last_time = "Unknown"
    margin = 4
    cx = 30
    cy = min(device.height, 64) / 2
    left = cx - cy
    right = cx + cy

    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")

        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                draw.text((2 * (cx + margin), cy - 8), today_date, fill="yellow")
                draw.text((2 * (cx + margin), cy), today_time, fill="yellow")

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
