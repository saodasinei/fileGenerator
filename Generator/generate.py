import re
import random
from DB import models


def getfile(file_ids):
    files = []
    for file_id in file_ids:
        file = models.File.objects.filter(id=file_id)
        files.append(file)
    return files


def getprofile(profile_ids):
    profiles = []
    for profile_id in profile_ids:
        profile = models.Profile.objects.filter(id=profile_id)
        profiles.append(profile)
    return profiles


def generate(files, profiles):
    newfilearr = []
    for file in files:
        for f in file:
            for profile in profiles:
                newfile = {}
                newfile["file_template"] = f.title
                content = f.content

                for p in profile:
                    newfile["profile_template"] = p.series
                    greeting = p.greeting
                    end = p.end

                    # 替换常用词
                    pat = '今天我们来讲一讲'
                    newpat = p.question
                    news1 = re.sub(pat, newpat, content)

                    pat = '下一期，带你详细了解'
                    newpat = p.next
                    news2 = re.sub(pat, newpat, news1)

                    pat = '我'
                    newpat = p.self
                    news3 = re.sub(pat, newpat, news2)

                    pat = '好'
                    newpat = p.praise
                    news4 = re.sub(pat, newpat, news3)

                    pat = '粉丝'
                    newpat = p.fans
                    news = re.sub(pat, newpat, news4)

                    new = greeting + news + end

                    print(new)

                    newfile["newfile_content"] = new
                    newfilearr.append(newfile)

    return newfilearr

    # rowrandom = random.randint(2, len(arr)-2)
    # koupirandom = random.randint(0, 1)
    # print(rowrandom)
    # print(koupirandom)
    # arr[rowrandom] = arr[rowrandom]+","+koupi1[koupirandom]
    # print(arr)
    #
    # str = '\n'.join(arr)
    # print(str)
    #
    # newfile.template = f.id
