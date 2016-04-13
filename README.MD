## Synopsis
This python script automates uploading emoji icons to a slack team. 
It uses selenium automation libraries and the firefox browser to upload images in a folder. 

Useful when there is a large number of emoji to upload when customizing a slack team.
## Code Example

Users must edit the script to tailor each enviroment and set the path to the images.



```python
binaryPath = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
profilePath = "/Users/[Username]/Library/Application Support/Firefox/Profiles/20wd5tda.default"
sourcepath = "/Users/[Username]/Downloads/hubot-ingress-master/badges/"
team_url = "https://[teamname].slack.com/customize/emoji"
```

The name of the image is used as the name of the emoji:
```python 
fname = os.path.splitext(fileinfo)[0] 
```
##Testing
Passes on OS X 10.11.4, Python 2.7.10

Untested in Windows OS.

## Motivation

I got tired of uploading icons to serveral slack teams for work and hobbies. So, it's automated now.

##Requirements
- *There should only be images files in the source directory*
- FireFox 45.0.1 
- *Login to your slack team and have firefox remember login credentials*
- Selnium automation libraries for python ```pip install selenium ```
(Don't have pip? ([OS X](http://docs.python-guide.org/en/latest/starting/install/osx/))

## Installation & Usage

* Download the [project](https://github.com/iloreto/emoji-slack-uploader) 
* open and edit the main.py script in the src directory
* Set FireFox binary path
* Set FirefFox Profile path
* Set image source directory path
* Set team url 
* Run ```python main.py``` from src directory
* Sitback and sip on your drink of choice

##Issues

- Lacks robust error handling.
- Lacks validation of file types.
- Lacks login methods, user needs to be logged in to slack team.
- Lacks input params for user defined variables.
- Lacks comments for now.

## Collaboration
If you like this project, support the dev @ [iLoreto Development](https://www.paypal.me/iLoretoDevelopment) ;-)

Want to jump in and help, make a git pull and push your changes! 

## License
Licensed under [MIT License](https://github.com/iloreto/emoji-slack-uploader/LICENSE)
