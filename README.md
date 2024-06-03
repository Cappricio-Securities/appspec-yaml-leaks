
<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/appspec-yaml-leaks-tool.png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/appspec-yaml-leaks)
![PyPI - Downloads](https://img.shields.io/pypi/dm/appspec-yaml-leaks)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/appspec-yaml-leaks/total)
<a href="https://github.com/Cappricio-Securities/appspec-yaml-leaks/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/appspec-yaml-leaks"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install appspec-yaml-leaks 
        ```
   - Run bellow command to check
     - `appspec-yaml-leaks -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          appspec-yaml-leaks --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          appspec-yaml-leaks -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          appspec-yaml-leaks -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          appspec-yaml-leaks -i urls.txt -o out.txt
        ```
   - Want to Learn about [`appspec-yaml-leaks`](https://blogs.cappriciosec.com/blog/180/appspec-yaml-leaks)? Then Type Below command
      - ```bash
          appspec-yaml-leaks -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-06-03%20at%204.55.49%20PM.png)](https://asciinema.org/a/UbNJ6Svl6FTypJ3a3KJmQSd3X)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                                                                v1.0
                                                                      __      __           __
  ____ _____  ____  _________  ___  _____      __  ______ _____ ___  / /     / /__  ____ _/ /_______
 / __ `/ __ \/ __ \/ ___/ __ \/ _ \/ ___/_____/ / / / __ `/ __ `__ \/ /_____/ / _ \/ __ `/ //_/ ___/
/ /_/ / /_/ / /_/ (__  ) /_/ /  __/ /__/_____/ /_/ / /_/ / / / / / / /_____/ /  __/ /_/ / ,< (__  )
\__,_/ .___/ .___/____/ .___/\___/\___/      \__, /\__,_/_/ /_/ /_/_/     /_/\___/\__,_/_/|_/____/
    /_/   /_/        /_/                    /____/

                                                 Developed By https://cappriciosec.com

appspec-yaml-leaks : Bug scanner for WebPentesters and Bugbounty Hunters 

$ appspec-yaml-leaks [option]

Usage: appspec-yaml-leaks [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | appspec-yaml-leaks -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | appspec-yaml-leaks -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | appspec-yaml-leaks -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | appspec-yaml-leaks --chatid yourid |
| `-b` | `--blog` | To Read about appspec-yaml-leaks Bug | appspec-yaml-leaks -b |
| `-h` | `--help` | Help Menu | appspec-yaml-leaks -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com
