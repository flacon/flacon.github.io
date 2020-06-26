---
layout: page
title: Download
description: Flacon available for Windows and Linux.
menuItem: download
---


<div class="download-block _flex">
    <div class="button big "><a href="{% include url.apple %}">Download APP for Mac</a></div>
    <div class="button big" ><a target="_blank" href="https://flathub.org/apps/details/com.github.Flacon">Download Flatpak for Linux</a></div>
</div>



## Apple macOS
_Mac OS_ users can download program from the our site.<br>
[Flacon_{% include version.apple %}.dmg]({% include url.apple %})

If you are using old versions of _Mac OS_ and have problems with running the Flacon. Try the version for the legacy MacOS.<br>
[Flacon_{% include version.apple_legacy %}-LegacyOS.dmg]({% include url.apple_legacy %})



## Flatpack for Linux
Flatpak is a modern method of distributing Linux applications. The applications run inside a sandbox environment and don't rely on packages or environment provided by your Linux distributions.
Flatpak is the recommended way to install the Flacon under Linux.

Flatpak builds of Flacon are now provided on [Flathub](https://flathub.org/apps/details/com.github.Flacon) (direct link to [download flcon](https://flathub.org/repo/appstream/com.github.Flacon.flatpakref)).


{% for post in site.categories.download reversed %}
{{ post.content }}
{% endfor %}


## FreeBSD
_FreeBSD_ users can install it from the official repositories.

    pkg install flacon

Alternatively, users can install it from ports (build from source):

    cd /usr/ports/audio/flacon && make install clean


## Source code

Flacon is a free and open source application. Patches, suggestions and comments are welcome. The source code is hosted on [GitHub](https://github.com/flacon/flacon).

If you are having troubles compiling the program, you might want to read "[Build Instuctions](https://github.com/flacon/flacon/wiki/How-to-build)" on the [WIKI section](https://github.com/flacon/flacon/wiki). Also, this section is useful when you want to learn more details about a development or translation process.
