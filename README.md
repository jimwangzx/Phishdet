<img src="https://github.com/whoamisec75/Phishdet/blob/main/static/IMG_20211129_194107.jpg"/>
<p align="center"><b><i>Heuristic phishing link scanner</b></i></p>

## File Structure

* phishdet/
  * main.py
  * init.py
  * core/
    * scanner.py
    * init.py
    * colors.py
  * db/
    * db.py
    * init.py
* setup.py
* .gitignore
* LICENCE
* README.md
* static/
  * IMG_20211129_194107.jpg

## Installation

```
▶ git clone https://github.com/whoamisec75/Phishdet.git
▶ cd Phishdet
▶ sudo python3 setup.py install
▶ phishdet -h
```

## Usage

<img src="https://github.com/whoamisec75/Phishdet/blob/main/static/phishdet.png" height="500px"  width="500px"/>

```
usage: phishdet [-h] -u URL [-ls]

optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url URL  Specify the URL for scanning
  -ls, --login-scan  Scan for login keyords
```

Scan any URL/Link:
```
▶ phishdet -u http://phishing.ngrok.io
```


