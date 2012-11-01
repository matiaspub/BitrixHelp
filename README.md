# BitrixHelp ([Sublime] Text 2 plugin for some helps in work with [Bitrix] CMS)

Feauters:

* BitrixAPI.sublime-complations(complations for Bitrix API) - all modules included.
* List links whith names of Bitrix Dev API Help (links to http://dev.1c-bitrix.ru/api_help/) [ctrl+alt+b, ctrl+alt+b].
* List links whith names of Bitrix Components (links to http://dev.1c-bitrix.ru/api_help/) [ctrl+alt+b, ctrl+alt+c].


## Instalation
Recommended way is using [PackageControll] package.

### Using Sublime Package Control

It is preferred and simplest way for most users. 

- Install Package Control http://wbond.net/sublime_packages/package_control
- Open Package Control
- Select 'Install Package'
- Find and select 'BitrixHelp'

### Using Git

If you like work with HEAD you can locate BitrixHelp in your packages directory.

- Go to your Packages directory, you can locate to your Packages directory by using the menu item 
  Preferences ->   Browse Packages...
- Inside the Packages directory, clone the BitrixHelp repository using the command below: 
  git clone https://github.com/matiaspub/BitrixHelp.git BitrixHelp

### Download Manually

- Download the files using the GitHub .zip download option.
- Unzip the files and rename the folder to something like BitrixHelp.
- Copy the folder to your Sublime Text 2 Packages directory.

## Configuration
You can add self links in BitrixHelp.sublime-settings
````
{
	"pages": {
		// items in list Bitrix Components [ctrl+alt+b, ctrl+alt+c]
		"bitrixComponents":[ list of links ],
		// items in list Bitrix API [ctrl+alt+b, ctrl+alt+b]
		"bitrixAPI": [ list of links ]
	}
}
````

## Key Map
It contains redefine standart keys as ctrl++(encrease font size), but you can change it.
````
[
	{ "keys": ["ctrl+alt+b", "ctrl+alt+b"], "command": "bitrix_help"},
	{ "keys": ["ctrl+alt+b", "ctrl+alt+c"], "command": "bitrix_help", "args": {"it": "bitrixComponents"}}
]
````

## Use

### Complations

For complation in $APPLICATION->IncludeComponent($componentName, $componentName, $arParams = array(), $arParams = array(), $arFunctionParams = array())
Type APPincom + Tab, or choose complation in drop-down select + Enter
Its work for objects $APPLICATION, $USER and $DB

For complation in CIBlockElement::GetList($arOrder=array('SORT'=>'ASC'), $arFilter=array(), $arGroupBy=false, $arNavStartParams=false, $arSelectFields=array())
Type CIblElGetli + Tab, or choose complation in drop-down select + Enter

### API Help

To speed choose API help page of Bitrix API Help - press __[ctrl+alt+b, ctrl+alt+b]__, and type some characters to find what you need and press Enter.
You will see opened tab in browser with choosen page of Bitrix Api Help.

### Components Help

To speed choose component help page of Bitrix API Help - press __[ctrl+alt+b, ctrl+alt+c]__, and type some characters to find what you need and press Enter.
You will see opened tab in browser with choosen page of Bitrix Api Help.


[Sublime]: http://www.sublimetext.com/
[PackageControll]: http://wbond.net/sublime_packages/package_control/installation
[Bitrix]: http://1c-bitrix.ru
