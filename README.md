# Tweet Emotion Detection Dataset

### The dataset used here is the result of a research work. If you use the dataset, please cite the following paper.

### Citation Info

Wenbo Wang, Lu Chen, Krishnaprasad Thirunarayan, Amit P. Sheth. Harnessing Twitter ‘Big Data’ for Automatic Emotion Identification. IEEE fourth conference on social computing, 2012
http://knoesis.org/library/resource.php?id=1749


### Due to the restrictions on redistributing Twitter data, the dataset only has the tweet ids and emotions. The script was written to get the tweets without any unnecessary work. 
### Since the dataset is relatively old, some tweets do not exist anymore. This script will only get the available tweets.

## To run the scripts on Windows

- First, you will need Twitter API keys. Follow this answer to get the API keys - https://stackoverflow.com/a/6875024/4757055
- Rename example.env to .env and add your credentials.
- Run the following commands in the terminal.

```bash
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python tweepy_streamer.py 10   # 10 means the number of tweets you want in a single file
```
