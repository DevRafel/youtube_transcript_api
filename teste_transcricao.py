from youtube_transcript_api import YouTubeTranscriptApi as yta

import re

# https://www.youtube.com/watch?v=FM6kHcXpw98

vid_id = '2p4dHBKPj3M'

data = yta.get_transcript(vid_id, languages=['pt', 'en'], preserve_formatting=True)

transcript = ''

for value in data:
    for key, val in value.items():
        if key == 'text':
            transcript += val

l = transcript.splitlines()
final_tra = " ".join(l)

file = open("Guruji.text", 'w')
file.write(final_tra)
file.close()
