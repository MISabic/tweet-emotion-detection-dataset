from tweepy import OAuthHandler, API
from excelWrite import *
from decouple import config
from tqdm import tqdm
import sys, os

try:
    CONSUMER_KEY = config('CONSUMER_KEY')
    CONSUMER_SECRET = config('CONSUMER_SECRET')
    ACCESS_TOKEN = config('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = API(auth)

except:
    print('API key missing!')
    quit()

def writeFile(excelFileName, tweetsListWithEmotion) :
    
    print(len(tweetsListWithEmotion))

    # for i in range(len(tweetsListWithEmotion)):
    #    print(tweetsListWithEmotion[i][0],'  ',tweetsListWithEmotion[i][1])

    xWrite = excelWrite(excelFileName)
    xWrite.writeText(tweetsListWithEmotion)

def run(numberOfTweetsInAFile) :
    numberOfTweetsInAFile = int(numberOfTweetsInAFile)

    directory = os.path.dirname(os.path.abspath(__file__))
    srcFileName = os.path.join(directory, 'Dataset/test.txt')

    if not os.path.exists(directory + '/Tweets'):
        os.makedirs(directory + '/Tweets')

    file = open(srcFileName, "r", encoding="utf-8" ).readlines()

    tweetIdEmotion = []
    tweetsListWithEmotion = []

    fileNum = 1
    numberOfCheckedTweets = 0
    numberOfTweetsFound = 0

    for line in tqdm(file) :

        tweetIdEmotion = line.split('\t')
        
        numberOfCheckedTweets += 1

        # print("Number Of Tweets Found :: ", numberOfTweetsFound)
        
        try:
            tweet = api.get_status(tweetIdEmotion[0])
            tweetText = str(tweet.text)
            record = (tweetText.strip(), tweetIdEmotion[1].strip())
            tweetsListWithEmotion.append(record)
            numberOfTweetsFound += 1

            if (numberOfTweetsFound % numberOfTweetsInAFile) == 0 :
                
                dstFileName = os.path.join(directory, 'Tweets/')

                xWrite = excelWrite(dstFileName + str(fileNum) + '.xlsx')
                xWrite.writeText(tweetsListWithEmotion)

                keepRecord = open(directory + "/Record.txt", "a")
                keepRecord.write("Number Of Checked Tweets IDs :: " + str(numberOfCheckedTweets) + "\n")
                keepRecord.write("Number Of Tweets Found :: " + str(numberOfTweetsFound) + "\n\n")
                keepRecord.close()
                
                fileNum += 1
                tweetIdEmotion = []
                tweetsListWithEmotion = []

        except:
            pass
    
    file.close()
    

if __name__ == "__main__":
    run(sys.argv[1])

