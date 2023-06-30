# regToZero

regToZero is a Python Solution utilizing Selenium framework tools to interact with the webpage DOM. [regToZero features](#usage) located on mini window are clear registers[0 - 13] and clear memory. Additionally, sets webpage layout to auto align layout size to byte, and set memory display to the right stack.

## Installation

Additional Step for Mac users
: Use [Chrome Driver](https://sites.google.com/chromium.org/driver/) to install chromedriver on your local mac machine.

```
// in terminal to set chromediver to system path
$mv chromedriver /usr/local/bin
```

Then
: Verify successful chromedriver by going to System Preferences, then press "allow and open anyway" for chrome driver.

For All OS
: Required dependencies for this project to work

```
// required dependencies
pip install selenium
pip install pyside2
pip install darkdetect
pip install qdarktheme
pip install pyqtdarktheme
```

## Usage

<div align="center">
    <div style="display: flex; align-items: center;">
        <img src="https://github.com/yycorcino/regToZero/blob/media/mini-window.png">
    </div>
</div>

Opens [CPUlator](https://cpulator.01xz.net/?sys=arm) on Chrome and automatically setup website. With small window popup, commands:

| Button Commands | Description                                         |
| --------------- | --------------------------------------------------- |
| Reset Registers | Reset registers to 0 from 0 - 13                    |
| Clear Memory    | Clear memory addresses from 0x00000000 - 0x000000f0 |
| Quit            | Closes Chrome and Window Popup                      |

## License

Distributed under the MIT License. See LICENSE for more information.
