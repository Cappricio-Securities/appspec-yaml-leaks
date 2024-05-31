#!/usr/bin/env python

"""
 * appspec-yaml-leaks
 * appspec-yaml-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */

"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                                          v1.0
                                                                      __      __           __
  ____ _____  ____  _________  ___  _____      __  ______ _____ ___  / /     / /__  ____ _/ /_______
 / __ `/ __ \/ __ \/ ___/ __ \/ _ \/ ___/_____/ / / / __ `/ __ `__ \/ /_____/ / _ \/ __ `/ //_/ ___/
/ /_/ / /_/ / /_/ (__  ) /_/ /  __/ /__/_____/ /_/ / /_/ / / / / / / /_____/ /  __/ /_/ / ,< (__  )
\__,_/ .___/ .___/____/ .___/\___/\___/      \__, /\__,_/_/ /_/ /_/_/     /_/\___/\__,_/_/|_/____/
    /_/   /_/        /_/                    /____/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mappspec-yaml-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mappspec-yaml-leaks\033[0m [option]

Usage: \033[92mappspec-yaml-leaks\033[0m [options]

Options:
  -u, --url     URL to scan                                appspec-yaml-leaks -u https://target.com
  -i, --input   <filename> Read input from txt             appspec-yaml-leaks -i target.txt
  -o, --output  <filename> Write output in txt file        appspec-yaml-leaks -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             appspec-yaml-leaks --chatid yourid
  -b, --blog    To Read about appspec-yaml-leaks Bug       appspec-yaml-leaks -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                                      v1.0
                                                                      __      __           __
  ____ _____  ____  _________  ___  _____      __  ______ _____ ___  / /     / /__  ____ _/ /_______
 / __ `/ __ \/ __ \/ ___/ __ \/ _ \/ ___/_____/ / / / __ `/ __ `__ \/ /_____/ / _ \/ __ `/ //_/ ___/
/ /_/ / /_/ / /_/ (__  ) /_/ /  __/ /__/_____/ /_/ / /_/ / / / / / / /_____/ /  __/ /_/ / ,< (__  )
\__,_/ .___/ .___/____/ .___/\___/\___/      \__, /\__,_/_/ /_/ /_/_/     /_/\___/\__,_/_/|_/____/
    /_/   /_/        /_/                    /____/
    
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mappspec-yaml-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
