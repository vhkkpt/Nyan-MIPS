import mido, sys
from math import ceil


# --------- Note ---------
# Note that the converter can not correctly recognize two tones
# being played at the same time. So make sure the track you choose
# is "linear". (I'm not a musician so I don't know how to describe
# it, but you know what I mean.)
# --------- Input 1 ---------
# python3 music.py input_music.midi
# --------- Output 1 ---------
# In this case, the converter will print out the tracks' information,
# including track names and the number of notes in them. Choose the
# correct track name according to number of notes.
# --------- Input 2 ---------
# python3 music.py input_music.midi track_name
# --------- Output 2 ---------
# In this case, the converter will convert the notes into an array,
# in the following format:
# music: .word pitch[0] duration[0] pitch[1] duration[1] ... -1
# In another word, all words with even indexes are pitches, and all
# words with odd indexes are durations (in millisecond). If a pitch
# is 128, then it represents a delay (no sound need to be played),
# and the array ends with word -1.
# --------- Input 3 ---------
# python3 music.py input_music.midi track_name scaler
# --------- Output 3 ---------
# This case is similar with case 2, but the converter will multiply
# every duration by the scaler, so you can control the speed of the
# music.


if len(sys.argv) < 2:
    exit()
mid = mido.MidiFile(sys.argv[1])

if len(sys.argv) == 2:
    for track in mid.tracks:
        print("Track name:", track.name, "[" + str(len(track)) + "]")
    exit()

res = []

for track in mid.tracks:
    if track.name != sys.argv[2]:
        continue
    for msg in track:
        if msg.type == "note_on":
            if msg.time > 0:
                res.append([128, msg.time]) # Delay
        elif msg.type == "note_off":
            if msg.time > 0:
                res.append([msg.note, msg.time])

if len(sys.argv) == 4:
    p = float(sys.argv[3])
    for i in range(len(res)):
        res[i][1] = ceil(res[i][1] * p)

print("music: .word ", end = "")

for i in res:
    print(i[0], i[1], sep = ", ", end = ", ")

print(-1)
