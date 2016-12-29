# PiRadio
PiRadio is a small and lightweight Python3 radio script that is based on PiFM project

## Requirements:
There is only one dependency that is not a part of the standard Python3 library, and 
that is **configparser**.

You can get config parser by running `sudo pip3 install configparser`.


## How to use:

**1. Step one**

Create a `music` folder inside of PiRadio folder and place your music there.

Songs can be in whichever format you prefer, if *mpg123* supports it.
&nbsp;

*Hint:* mpg123 supports a whole lot of music formats, including **mp3**.

--
**2. Step two**

Edit the settings in `config.ini` file to suit your interest.

The `BROADCAST_FREQUENCY` sets the radio emmiter frequency, in MHz.

The `RANDOM` tells PiRadio to shuffle the songs (play them in a random order).

--
**3. Step three**

Connect any kind of wire (20 cm will do) to **GPIO Pin 4** on your Raspberry Pi.

--
**4. Step four**

Run PiRadio.py **as super user (*sudo*)** and enjoy your radio!

--
### DISCLAIMER: In my country, It is legal to broadcast on unassigned FM frequencies if the source is less powerful than 0.3 W.
### Before broadcasting, you must check your (local, or state) laws.
### I am NOT responsible for any trouble you do if you violate your laws.
