# regToZero

regToZero is a Python solution utilizing Selenium that sets registers[0 - 13] to 0 without manual inputs. Additionally, auto align layout size to byte, and set memory display to the right stack.

## Usage

Opens https://cpulator.01xz.net/?sys=arm in Chrome and automatically setup website. With small window popup, commands:

Commands  | Description
------------- | -------------
Reset Registers  | Reset all registers to 0 from 0 - 13
Clear Memory  | Clear memory addresses from 0x00000000 - 0x000000f0
Quit  | Closes Chrome and Window Popup

## Installation

For Mac: Use https://sites.google.com/chromium.org/driver/ to install chromedriver.

```
// in terminal to set chromediver to system path
$mv chromedriver /usr/local/bin
```

Verify chromedriver by going to System Preferences, then presss "allow and open anyway" for chrome driver.

```
// required dependencies
pip install selenium
pip install pyside2
pip install darkdetect
pip install qdarktheme
```

## License

Distributed under the MIT License. See LICENSE for more information.
