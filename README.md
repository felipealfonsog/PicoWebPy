# Webserver Raspberry Pi Pico W 2

[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![Vim](https://img.shields.io/badge/--019733?logo=vim)](https://www.vim.org/)
[![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/)
[![Python 3.6 | 3.7 | 3.8](https://img.shields.io/badge/python-3.6%20|%20%203.7%20|%203.8-yellowgreen)](https://www.python.org/downloads/release/python-385/)

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

If you like my project, give it a :star: or support me by buying me a coffee :coffee::grinning:

<a href="https://www.buymeacoffee.com/felipealfonsog" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 27px !important;width: 114px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

Web Server written in micropython for a Raspberry Pi Pico W 2 - Wifi - BT
#
By Engineer: Felipe A. Gonzalez <f.alfonso@res-ear.ch>
#




# Web Server written in micropython for a Raspberry Pi Pico W

![Version 1.0.0](https://img.shields.io/badge/version-v1.0.0-blue)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![Python 3.6 | 3.7 | 3.8](https://img.shields.io/badge/python-3.6%20|%20%203.7%20|%203.8-yellowgreen)](https://www.python.org/downloads/release/python-385/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![Vim](https://img.shields.io/badge/--019733?logo=vim)](https://www.vim.org/)
[![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/)

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

Web Server written in micropython for a Raspberry Pi Pico W 2 - Wifi - BT

By Engineer: Felipe A. Gonzalez <f.alfonso@res-ear.ch>

If you like my project, give it a :star: or support me by buying me a coffee :coffee::grinning:

<a href="https://www.buymeacoffee.com/felipealfonsog" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 27px !important;width: 114px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


### Important Notice
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Starting February 9, we will no longer support free access to the Twitter API, both v2 and v1.1. A paid basic tier will be available instead 🧵</p>&mdash; Twitter Dev (<a href="https://twitter.com/TwitterDev/status/1621026986784337922?ref_src=twsrc%5Etfw">@TwitterDev</a>) February 2, 2023</blockquote>

---

### Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [To Run it](#to-run)
    - [To Host](#to-host)
- [Instructions](#instructions)
  - [File Structure](#file-structure)
- [Deployment](#deployment)
  - [PythonAnywhere](#pythonanywhere)
  - [Amazon Web Services](#amazon-web-services)
- [Contributing](#contributing)
- [Creator / Maintainer](#creator--maintainer)
- [Additional Information](#additional-information)

---

## Getting Started

Get a raspberry pi pico w 2 - wifi. Get a project usb - micro-c cable and get thonny.

### Prerequisites

#### To Run it

- [Python 3](https://www.python.org/downloads/)
- [Thonny](https://thonny.org) - a micropython IDE

#### To Host

You can host it locally, or directly when it's connected via USB, but that implementation is not yet properly working fine.

It can be used to host a site 24/7. Also has a implementation for a 404 file not find, like most webservers. 

---

## Instructions

1. Get thony IDE and modify the network connectivity. 

2. Run the file setting up Thonny to run the code as a raspberry pi pico

![Keys and Secrets](resources-for-readme/keys-secrets.png)

- Make sure the app settings has _Read and Write_ permissions.

![App Permissions](resources-for-readme/app-permissions.png)

3. Create a file named `credentials.py` to hold the private information using the format below.
   - See [File Structure](#file-structure) for where the file should be placed.

```
TWITTER_API_KEY="xxxx"
TWITTER_API_KEY_SECRET="xxxx"
TWITTER_ACCESS_TOKEN="xxxx"
TWITTER_ACCESS_TOKEN_SECRET="xxxx"
```

4. Adjustments you can make in `config.py` to tweak the bot to your liking. _(Keep in mind the TwitterAPI search index has a 7-day limit, no tweets will be found for a date older than one week.)_

   - **search_keywords** - Keyword(s) and/or hashtag(s) that you want to retweet
   - **delay** - Time to wait between processing requests in seconds
     - Please be aware of the [TwitterAPI rate limits](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits)
   - **result_type** - Specify what type of search results you want to get
     - "recent", "popular", or "mixed"
   - **number_of_tweets** - Specify the number of tweets you want the bot to iterate through
   - **run_continuously** - Set True if you want the bot to run continuously
     - Also set True if you will be deploying the script
   - **retweet_tweets**, **like_tweets** - Adjust booleans for whether you want to only retweet, only like, or do both

5. Run the script. Enjoy your Twitter bot!

```
python twitter-bot.py
```

### File Structure

```
Twitter-Retweet-Bot
 |-- config.py
 |-- credentials.py
 |-- requirements.txt
 |-- twitter-bot.py
```

---

## Deployment

Here is a tutorial on how to deploy / host the bot on a server.

### PythonAnywhere

1. Create a free Beginner [PythonAnywhere](https://www.pythonanywhere.com/pricing/) account.

![Create Account](resources-for-readme/create-account.png)

2. Go to Files, create a new Directory, upload the three `.py` files.

![Upload Files](https://media.giphy.com/media/ggzrVLXPx3UYA9aWKM/giphy.gif)

3. Create a new bash console on your Dashboard and run pip with your python version to install tweepy

![Bash Console](resources-for-readme/new-bash.png)

```
pip3.8 install --user tweepy
```

4. Copy the file path, go to Tasks, enter the [UTC](https://www.worldtimeserver.com/current_time_in_UTC.aspx) time you want the script to run at, and enter the python version and file path with `twitter-bot.py` at the end.

```
python3.8 /home/account-name/directory-name/twitter-bot.py
```

![Schedule Task](https://media.giphy.com/media/RfLrY3SZU5Zugca5Sz/giphy.gif)

5. After the task runs as the scheduled time, you can check the task log to see the bot running

![Check Logs](resources-for-readme/check-logs.png)

### Amazon Web Services

1. Launch an EC2 instance on Amazon Web Services.
   - See [Additional Information](#additional-information) for more details.

![Launch EC2 Instance](https://media.giphy.com/media/RIBJvH1dyXCl4WGrNl/giphy.gif)

2. Load the key-pair file (.pem) into PuTTYgen (which was downloaded when you installed [PuTTY](https://www.putty.org/)) and save the private key as a private key file (.ppk).

![Generate PPK](https://media.giphy.com/media/iIGG5Pgf338zjaAHMr/giphy.gif)

3. Connect to your instance on [WinSCP](https://winscp.net/eng/download.php).
   - The host name is ubuntu@[public DNS here].
   - Click Advanced, go to Authentication under SSH, and load the previously generated private key file (.ppk).
   - Login to the session.

![Conenct to WinSCP](https://media.giphy.com/media/XDpwQS1KQA5ZyqmKaN/giphy.gif)

4. Use [WinSCP](https://winscp.net/eng/download.php) to transfer the project's .py files to the server.

![WinSCP File Transfer](https://media.giphy.com/media/cltoUcOEABkI7h1seu/giphy.gif)

5. Connect to your instance on a bash command line using one of the following ways.
   - Use a bash shell with the example ssh command (I use [Git Bash](https://gitforwindows.org/)).
     - Make sure you are in the directory with the key-pair file (.pem).
   - Use [PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html?icmpid=docs_ec2_console) with the public DNS and private key file (.ppk).

![Connect to Bash](https://media.giphy.com/media/JTDsQkn9CG0bkQTv7T/giphy.gif)

6. Install python and pip to the server on the bash command line.

```
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
pip3 install update pip
```

7. Check if python and pip have been installed correctly.

```
python3 --version
pip3 --version
```

8. Install tweepy to the server.

```
pip3 install tweepy
```

9. Run the script. Enjoy!.

```
python3 twitter-bot.py
```

10. See [Additional Information](#additional-information) for details on running the script continuously.
    - I used the _screen_ option.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

### How To Contribute

1. Fork the repository to your own Github account.
2. Clone the project to your machine.
3. Create a branch locally with a succinct but descriptive name.
4. Commit changes to the branch.
5. Following any formatting and testing guidelines specific to this repo.
6. Push changes to your fork.
7. Open a Pull Request in my repository.

---

### Creator / Maintainer

Annie Wu ([anniedotexe](https://github.com/anniedotexe))

If you have any questions, comments, or concerns, feel free to contact me below.

<p align="left">
  <a href="mailto:anniewu2303@gmail.com"> 
    <img alt="Connect via Email" src="https://img.shields.io/badge/Gmail-c14438?style=flat&logo=Gmail&logoColor=white" />
  </a>
</p>

This project was created for educational purposes of learning development, documentation, and deployment and for personal and open-source use.

Default values of the project are used to run [@ac_celeste_bot](https://twitter.com/ac_celeste_bot).

If you like my content or find this code useful, give it a :star: or support me by buying me a coffee :coffee::grinning:

<a href="https://www.buymeacoffee.com/anniedotexe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

---

## Additional Information

- [Getting Started with Amazon EC2](https://aws.amazon.com/ec2/getting-started/)
- [How to Continuously Run a Python Script on an EC2 Server](https://intellipaat.com/community/9361/how-to-continuously-run-a-python-script-on-an-ec2-server)
