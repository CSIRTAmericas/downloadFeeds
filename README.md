# Download Feeds CSIRTAmericas

This script was made in **python 3** in order to download the feeds provided by CSIRTAmericas.


## Installation
In order to use the script you must have python3 installed, in case you do not have it installed, you can check this [link](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server-es) 

The first step is to install **pip3**

```bash
sudo apt install python3-pip
```
![downloadpip3](https://user-images.githubusercontent.com/29242324/113663885-6b8f7780-9670-11eb-9e5f-4764ac27dd7b.gif)

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install pytz.

```bash
pip3 install pytz
```
![pytz](https://user-images.githubusercontent.com/29242324/113663905-76e2a300-9670-11eb-89a2-f8994b93ad60.gif)

## Usage

```bash
$ git clone https://github.com/CSIRTAmericas/downloadFeeds.git
$ cd downloadFeeds
# Modify downloadFeed.py, specifically for:
# 1) FTPUSER, FTPPASS, FTPSERVER: This data is provided by CSIRTAmericas.
# 2) DSTFOLDER: Destination folder for feeds. Ex: /home/user/python || D:\\python
$ python3 downloadFeeds.py
```

![downFeedsCsir](https://user-images.githubusercontent.com/29242324/113663930-7fd37480-9670-11eb-93f5-c68907a305df.gif)

## Automation

We recommend that you use a crontab to automate this download.
With the following example you will be able to place the crontab every 30 minutes from 7 am to 6 pm Monday through Sunday.
```python
$ sudo crontab -e
# If you have not used crontab before, it will ask you with which text editor to open the document.
# Now you must place the following code at the bottom of the page 
*/30 7-18 1-7 * * timeout 180 /path/to/script/downloadFeed.py
```
![auto](https://user-images.githubusercontent.com/29242324/113741787-9bb63500-96c7-11eb-94d3-515db276ba14.gif)

## Help/Questions/Comments:
For help or more info, feel free to contact Nelson Guanilo: nguanilo@csirtamericas.org

## License
[MIT](https://choosealicense.com/licenses/mit/)
