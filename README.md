# Download Feeds CSIRTAmericas

This script was made in **python 3** in order to download the feeds provided by CSIRTAmericas.


## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install pytz.

```bash
pip3 install pytz
```

## Usage

```bash
$ git clone https://github.com/Nelsonwgc/downloadFeeds.git
$ cd downloadFeeds
# Modify downloadFeed.py, specifically for:
# 1) FTPUSER, FTPPASS, FTPSERVER: This data is provided by CSIRTAmericas.
# 2) DSTFOLDER: Destination folder for feeds. Ex: /home/user/python || D:\\python
$ python3 downloadFeeds.py
```
## Automation

We recommend that you use a crontab to automate this download.
With the following example you will be able to place the crontab every 30 minutes from 7 am to 6 pm Monday through Sunday.
```python
$ sudo crontab -e
# If you have not used crontab before, it will ask you with which text editor to open the document.
# Now you must place the following code at the bottom of the page 
*/30 7-18 1-7 * * timeout 180 /path/to/script/downloadFeed.py
```

## Help/Questions/Comments:
For help or more info, feel free to contact Nelson Guanilo: nguanilo@csirtamericas.org

## License
[MIT](https://choosealicense.com/licenses/mit/)
