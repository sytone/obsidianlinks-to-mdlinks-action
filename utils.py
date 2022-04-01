import os
import re


def getAllDocumentPaths(source_directory):
    allpaths = list()

    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        dirnames.sort()
        filenames.sort()
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            # path.replace(source_directory, "")
            allpaths.append(path)
    allpaths.sort(reverse=True)

    return allpaths


def getFileFullText(path):
    with open(path) as f:
        fulltext = f.read()

    return fulltext


def replaceLinks(text, allpaths):
    foundmatches = re.findall(
        r'(?P<fullwikilink>\[\[(?P<linkpage>.*?)\]\]?)', text)
    outputtext = text
    for item in foundmatches:
        fullwikilink = item[0]
        linkpage = item[1]

        pageurl = list(filter(lambda x: x.split(
            "/")[-1] == linkpage + ".md", allpaths))

        outputtext.replace(fullwikilink, "[" + pageurl + "]("+pageurl+")")
    return outputtext


def replaceurl(path, allpaths):
    fulltext = getFileFullText(path)
    replacedtext = replaceLinks(fulltext, allpaths)
    print(replacedtext)
    with open(path, "w") as f:
        f.write(replacedtext)
