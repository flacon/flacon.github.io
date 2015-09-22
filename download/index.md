---
layout: default
title: Flacon - Download
menuItem: download
---

## Ubuntu
_Ubuntu_ users can use repository at [launchpad](https://launchpad.net/~flacon/+archive/ppa). Open up a terminal and input these commands:

    sudo add-apt-repository ppa:flacon
    sudo apt-get update
    sudo apt-get install flacon

## Debian
### Stable, Unstable and Testing
_Debian stable, unstable and testing_ and _Linux Mint "Debian"_ users can use repository at [OpenSUSE Build Service] (http://download.opensuse.org/repositories/home:/Sokoloff/Debian_7.0/).
Open up a terminal and input these commands as root:

    echo "deb http://download.opensuse.org/repositories/home:/Sokoloff/Debian_7.0 ./" > /etc/apt/sources.list.d/flacon.list
    wget http://download.opensuse.org/repositories/home:/Sokoloff/Debian_7.0/Release.key -O- | apt-key add -
    apt-get update
    apt-get install flacon


### OldStable
_Debian old stable_ users can use repository at [OpenSUSE Build Service] (http://download.opensuse.org/repositories/home:/Sokoloff/Debian_6.0/).
Open up a terminal and input these commands as root:

    echo "deb http://download.opensuse.org/repositories/home:/Sokoloff/Debian_6.0 ./" > /etc/apt/sources.list.d/flacon.list
    wget http://download.opensuse.org/repositories/home:/Sokoloff/Debian_6.0/Release.key -O- | apt-key add -
    apt-get update
    apt-get install flacon


## Fedora
_Fedora_ users can use repository at [copr.fedoraproject.org](https://copr.fedoraproject.org/coprs/region51/flacon/). Open up a terminal and input these commands:

    sudo dnf copr enable region51/flacon
    sudo dnf install flacon


## Rosa
_Rosa_ users can install it from the official repositories.

    urpmi flacon

## FreeBSD
_FreeBSD_ users can install it from the official repositories.

    pkg install flacon

Alternatively, users can install it from ports (build from source):

    cd /usr/ports/audio/flacon && make install clean


## Other distribution
_Please let me know about packages for your distribution._

## Source code
###Stable release {{ site.flacon.release.version }}
The current stable release of Flacon is [{{ site.flacon.release.version }}]({{ site.flacon.release.link }}/v{{ site.flacon.release.version }}.tar.gz). See the [changelog](/changelog) for what has changed.


### Development version
You can checkout the latest source code of Flacon from the [git repository](https://github.com/flacon/flacon). This is the prefered way to get Flacon if you want to benefit from the latest improvements and be able to upgrade easily.

    git clone https://github.com/flacon/flacon.git

Alternatively, you can download sourses as [tarball](https://github.com/flacon/flacon/archive/master.tar.gz)

[Full build instructions and list of dependencies](https://github.com/flacon/flacon/wiki/How-to-build)


<br><br><br><br><br><br><br>
