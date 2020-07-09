# Screen Buddy

Little project to show certain things on (initially) the ssd1322 OLED display.

I bought [this one][1] and I soldered on the included pins for prototyping, as well as changing a jumper to allow running in 4 pin SPI mode. It was delivered in 8080 mode which I'm not familiar with, and I found a great example [of using this screen in a project from Balena Labs][2] in SPI mode which helped, as the datasheet seems hard to find for this screen.

[1]: https://www.aliexpress.com/item/32988174566.html
[2]: https://github.com/balenalabs/uk-train-departure-display#configuration

## Getting started

```bash
sudo -H pip3 install -r requirements.txt
```

For the font, I've been using this [Dot Matrix typeface](https://github.com/DanielHartUK/Dot-Matrix-Typeface) (great especially for the larger ssd1322 display), I've just copied the typeface `Dot Matrix Regular.ttf` to the root of this repo for now - these examples will work with that.

Then I can go into the relevant folder (`cd ssd1322`) and run `./run.sh` to run it on the screen for testing purposes.

## Screens

### `ssd1306`
A little tiny screen - not sure where I got it from (Wish perhaps?). From the label, it's a 0.96" `IIC OLED SSD1306`, the top 20ish lines are yellow in colour and below that is all blue. The dimensions of it are 128x64.


#### Pin connections

[Pinout.xyz SPI](https://pinout.xyz/pinout/i2c#).

Display pin | Connection    | Raspberry Pi pin
------------|---------------|-----------------
1           | V+ (3.3v)     | 1 (`3.3V`)
2           | Ground        | 9 (`GND`)
3           | Clock         | 5 (`BCM2 / SCL`)
4           | Data          | 3 (`BCM3 / SDA`)

### `ssd1322`

A OLED screen, the dimensions are 256x64. I bought it [from AliExpress a while ago from this listing](https://www.aliexpress.com/item/32988174566.html) (in yellow). It came supplied in 8080 mode, I changed it using the jumpers on the back into 4-pin SPI mode (as that was what the Balenalabs example was in, which allowed me to follow the pinout!)

#### Pin connections

[Pinout.xyz I2C example](https://pinout.xyz/pinout/spi#).

Display pin   | Connection                    | Raspberry Pi pin
--------------|-------------------------------|-------------------
1             | Ground                        | 25 (`GND`)
2             | V+ (3.3V)                     | 17 (`3.3V`)
4             | `D0/SCLK`                     | 23 (`BCM11 SCLK`)
5             | `D1/SDIN`                     | 19 (`BCM10 MOSI`)
14            | `DC` (data/command select)    | 18 (`BCM24`)
15            | `RST` (reset)                 | 22 (`BCM25`)
16            | `CS` (chip select)            | 24 (`BCM8 CE0`)

## References

* [OLED Driver (Luma.oled)](https://luma-oled.readthedocs.io/en/latest/intro.html) - Driver used for the screen
* [luma.examples](https://github.com/rm-hull/luma.examples) - Great examples and inspiration
* [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - For drawing on the screen itself
* [Dot Matrix Typeface](https://github.com/DanielHartUK/Dot-Matrix-Typeface) - Great font for this display
* [balenalabs - Train Departure display](https://github.com/balenalabs/uk-train-departure-display) - An inspiration for this project!