import json
import matplotlib.pyplot as plt

timesPlayed = {}
playTime = {}
minPlaytimeThreshold = 0
font = {'size': 7}
plt.rc('font', **font)

for i in range(0,4):
    with open(f"StreamingHistory_music_{i}.json", "r", encoding="utf8") as f:
        f = json.load(f)

        for line in f:
            artist = line["artistName"]
            playtime = line["msPlayed"]/60000

            if playtime > minPlaytimeThreshold:
                if len(timesPlayed) < 1:
                    timesPlayed[artist] = 1
                    playTime[artist] = playtime

                for key, value in timesPlayed.items():
                    if artist not in timesPlayed:
                        timesPlayed.update({artist: int(1)})
                        break
                    elif artist == key:
                        timesPlayed.update({key: value + 1})

                for key, value in playTime.items():
                    if artist not in playTime:
                        playTime.update({artist: playtime})
                        break
                    elif artist == key:
                        playTime.update({key: value+playtime})

for key, value in playTime.items():
    newValue = str(value).split(".")
    newValue[1] = round(float(f"0.{newValue[1]}")*60, 2)
    playTime[key] = f"{newValue[0]} minutes, {newValue[1]} seconds"

timesPlayed = dict(sorted(timesPlayed.items(), reverse=True, key=lambda kv: (kv[1], kv[0])))


artists = []
timesPlay = []

for key, value in timesPlayed.items():
    if value > 200:
        artists.append(key)
        timesPlay.append(value)


fig = plt.figure(figsize=(10, 8))
# creating the bar plot
plt.bar(artists, timesPlay, color='green',
        width=0.4)
plt.xticks(rotation=90)
plt.title("Artist/Number of listens")
plt.show()

print(timesPlayed)
