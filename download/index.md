---
layout: default
title: Flacon - Download
menuItem: download
---

# Apple macOS
_Mac OS_ users can download program from the our site.<br>
{% for post in site.categories.changelog %}{% if post.apple %}[Flacon_{{post.version}}.dmg](https://github.com/flacon/flacon/releases/download/v{{post.version}}/Flacon_{{post.version}}.dmg)
{% break %}
{%endif%}{% endfor %}

If you are using old versions of _Mac OS_ and have problems with running the Flacon. Try the version for the legacy MacOS.<br>
{% for post in site.categories.changelog %}{% if post.apple_legacy %}[Flacon_{{post.version}}-LegacyOS.dmg](https://github.com/flacon/flacon/releases/download/v{{post.version}}/Flacon_{{post.version}}-LegacyOS.dmg)
{% break %}
{%endif%}{% endfor %}

# Linux
Flatpak is a modern method of distributing Linux applications. The applications run inside a sandbox environment and don't rely on packages or environment provided by your Linux distributions.
Flatpak is the recommended way to install the Flacon under Linux.

Flatpak builds of Flacon are now provided on [Flathub](https://flathub.org/apps/details/com.github.Flacon) (direct link to [download flcon](https://flathub.org/repo/appstream/com.github.Flacon.flatpakref)).


# Other packages
Flacon is available for a variety of distributions.

{% for post in site.categories.download reversed %}
{{ post.content }}
{% endfor %}


# FreeBSD
_FreeBSD_ users can install it from the official repositories.

    pkg install flacon

Alternatively, users can install it from ports (build from source):

    cd /usr/ports/audio/flacon && make install clean


# Source code

### Stable release {{ site.flacon.release.version }}
The current stable release of Flacon is [{{ site.flacon.release.version }}]({{ site.flacon.release.link }}/v{{ site.flacon.release.version }}.tar.gz). See the [changelog](/changelog) for what has changed.


### Development version
You can checkout the latest source code of Flacon from the [git repository](https://github.com/flacon/flacon). This is the prefered way to get Flacon if you want to benefit from the latest improvements and be able to upgrade easily.

    git clone https://github.com/flacon/flacon.git

Alternatively, you can download sourses as [tarball](https://github.com/flacon/flacon/archive/master.tar.gz)

[Full build instructions and list of dependencies](https://github.com/flacon/flacon/wiki/How-to-build)


<br><br><br><br><br><br><br>
