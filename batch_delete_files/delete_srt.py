# Delete all files ending with .*srt from 'mypath' and all of its subfolders
# Can be in use for any batch-deletion of similar-extension-files

import os, re, os.path

pattern = ".*srt"
mypath = "/Volumes/MyPassport/Courses/"

for root, dirs, files in os.walk(mypath):
    for file in filter(lambda x: re.match(pattern, x), files):
        os.remove(os.path.join(root, file))
