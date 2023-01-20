#!/usr/bin/env python3
# v 0.2

GITHUB_USER = "Flacon"
GITHUB_REPO = "flacon"

MIN_VERSION = "10.0.0"

#######################################
URL_TEMPLATE = "https://api.github.com/repos/%s/%s/releases"

import sys
import os
import urllib.request
import json
import re
from xml.dom import minidom
import datetime
import markdown


class Error(Exception):
    pass

def Version(str):
    return tuple(map(int, (str.split("."))))

def versiontuple(str):
    return tuple(map(int, (str.split("."))))

class Release:
    def __init__(self, data):
        self.tag = data["tag_name"]
        self.version = self.extractVersion(self.tag)
        self.prerelease = data["prerelease"]
        self.url = self.getUrl(data)
        self.changeLog = data["body"]
        self.date = datetime.datetime.strptime(data["published_at"], '%Y-%m-%dT%H:%M:%SZ')
        self.dmg_exist = self.hasAsset(data, ".dmg")
        self.appImage_exist = self.hasAsset(data, ".AppImage")

    def extractVersion(self, tag):
        s = tag

        res = re.search("-beta\d+", s)
        if res:
            s = s[:res.start()]

        PREFIXES = [
            "v",
            "v.",
            f"{GITHUB_REPO}-",
        ]

        for p in sorted(PREFIXES, key=len, reverse = True):
            if s.startswith(p):
                s = s[len(p):]
                break

        if (re.match("[\d\.]+$", s)):
            return s

        raise Error(f"Can't extract version from '{tag}' tag")

    def hasAsset(self, data, ext):
        for asset in data["assets"]:
            if asset["name"].endswith(ext):
                return True

        return False

    def getUrl(self, data):
        for asset in data["assets"]:
            if asset["browser_download_url"].endswith(".dmg"):
                return asset["browser_download_url"]

        return None


def download(url):
    print(url)
    try:
        response = urllib.request.urlopen(url)
        res = response.read().decode('utf-8')
        return json.loads(res)

    except urllib.error.HTTPError as err:
        raise Error("Can't download from %s: %s" % (url, err))


def parse(data):
    min_version = Version(MIN_VERSION)

    releases = []
    for d in data:
        release = Release(d)

        if  Version(release.version) < min_version:
            continue

        if release.prerelease:
            continue

        releases.append(release)


    return releases


def dump(releases):
    for r in releases:
        print("*************************************")
        print(f"{r.version} {r.date}")
        print(f"DMG:{r.dmg_exist}, AppImage:  {r.appImage_exist}")
        print(".....................................")
        print(r.changeLog)
        print()


def write(release):
    file_name="%s-Flacon-%s.md" % (release.date.strftime("%Y-%m-%d"), release.version)

    def boolToStr(v):
        return "true" if v else "false"

    lines = []

    lines.append("---")
    lines.append(f"layout: default")
    lines.append(f"version: {release.version}")
    lines.append(f"apple: {boolToStr(release.dmg_exist)}")
    lines.append(f"appimage: {boolToStr(release.appImage_exist)}")
    lines.append("")
    lines.append("---")
    lines.append("")


    changeLog = release.changeLog.replace("\r", "")
    lines.append(changeLog)

    if not changeLog.endswith("\n"):
        lines.append("")

    print("=================================================================")
    print("\n".join(lines))


    f =  open(file_name, "wb")
    f.write("\n".join(lines).encode("UTF-8"))
    f.close()




if __name__ == "__main__":

    try:
        data = download(URL_TEMPLATE % (GITHUB_USER, GITHUB_REPO))
        releases = parse(data)
        #dump(releases)

        for r in releases:
            write(r)

    except Error as err:
        print("Error: %s" % err, file=sys.stderr)
