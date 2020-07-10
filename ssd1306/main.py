import math
import time
import datetime
import sys

from luma.core.render import canvas
from luma.core import cmdline, error

from PIL import ImageFont

def get_device(actual_args=None):
    """
    Create device from command-line arguments and return it.
    """
    if actual_args is None:
        actual_args = sys.argv[1:]
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)

    if args.config:
        # load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
    except error.Error as e:
        parser.error(e)

    return device

def main():
    today_last_time = "Unknown"
    margin = 4
    cx = 0
    cy = min(device.height, 64) / 2
    left = cx - cy
    right = cx + cy
    fontSize=10
    dotMatrixFont = ImageFont.truetype("../Dot Matrix Regular.ttf", fontSize)
    print("Displaying on screen now")

    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")

        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                draw.text((0 + margin, 2), today_date, fill="yellow", font=dotMatrixFont)
                draw.text((device.width - (3.5*10), 2), today_time, fill="yellow", font=dotMatrixFont)

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
