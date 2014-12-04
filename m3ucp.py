
# takes two arguments
# 1. relative m3u playlist
# 2. destination

# on execution:
# copies music files referenced in playlist to destination

import sys, os, shutil

#m3u, dest = sys.argv[1:3]

cwd = os.getcwd()

#process m3u playlist
mp3s = []
with open(os.path.join(cwd,sys.argv[1]), "rb") as m3u:

    m3u_path = os.path.join(cwd, os.path.split(sys.argv[1])[0])        

    for line in m3u.readlines():
        if not line.startswith("#"):            
            path = os.path.normpath(os.path.join(m3u_path, line.strip()))
            mp3s.append(path)

dest_path = os.path.join(cwd, sys.argv[2])
if not os.path.exists(dest_path):
    os.makedirs(dest_path)

for mp3 in mp3s:
    shutil.copy(mp3, dest_path)


