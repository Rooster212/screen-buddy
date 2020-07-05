# Screen Buddy

Little project to show certain things on (initially) the ssd1322 OLED display.

I bought [this one][1] and I soldered on the included pins for prototyping, as well as changing a jumper to allow running in 4 pin SPI mode. It was delivered in 8080 mode which I'm not familiar with, and I found a great example [of using this screen in a project from Balena Labs][2] in SPI mode which helped, as the datasheet seems hard to find for this screen.

[1]: https://www.aliexpress.com/item/32988174566.html
[2]: https://github.com/balenalabs/uk-train-departure-display#configuration

## References

[OLED Driver (Luma.oled)](https://luma-oled.readthedocs.io/en/latest/intro.html)
[luma.examples](https://github.com/rm-hull/luma.examples)