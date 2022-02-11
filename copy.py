import time
from apiclient.discovery import build
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from pytz import timezone
import time


DEVELOPER_KEY = "ここにAPIキーを入れる"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

ytcurrentviewersarray =[]
datesArray=[]

for i in range (0, 20, 1):
  time.sleep(30)
  response = youtube.videos().list(part="liveStreamingDetails",id = "ここにyoutubeの動画IDを入れる").execute() 
  liveinfo = (response["items"][0]["liveStreamingDetails"])
  ytcurrentviewers = (liveinfo["concurrentViewers"])
  ytcurrentviewersarray.append(ytcurrentviewers)
  datesArray.append(datetime.now(timezone('Asia/Tokyo')))


plt.plot_date(datesArray, ytcurrentviewersarray)