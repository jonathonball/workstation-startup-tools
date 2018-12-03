# Prepare The System

    sudo apt update
    sudo apt upgrade

# If you want you can get bleeding edge video drivers from intel:

    sudo add-apt-repository ppa:ubuntu-x-swat/updates
    sudo apt dist-upgrade

# Copy in SSH keys

# Copy in keepass key file 

# Install from repos:
  - exfat-fuse    
  - exfat-utils
  - vim
  - curl
  - zsh
  - terminator
  - redshift
  - xdotool
  - wmctrl
  - mplayer
  - ack
  - tree
  - python-pip
  - vlc
  - network-manager-openvpn
  - openvpn
  - build-essential
  - libusb-dev
  - libudev-dev
  - gimp
  - xscreensaver
  - xscreensaver-data
  - xscreensaver-data-extra
  - xscreensaver-gl
  - xscreensaver-gl-extra
  - htop
  - vlc
  - whois
  - figlet
  - lolcat
  - usb-creator-gtk
  - zenmap
  - xbacklight
  - jq
  - html-xml-utils

# Laptop Specific
  - acpi

# XFCE Specific
  - xfce4-goodies
  - xfce4-popup-clipman
    - add keyboard shortcut to call `xfce4-popup-clipman` 
  - network-manager-openvpn-gnome
  - pavucontrol
  - guake

# Download and install from external sources:
  - Google Chrome - https://www.google.com/chrome/
  - Keeweb - https://keeweb.info/
  - Dropbox - https://www.dropbox.com/install-linux
  - Slack - https://slack.com/downloads/linux
  - Atom - https://atom.io/
    - activate-power-mode
    - atom-beautify
    - atom-jinja2
    - chocomint-ui
    - chocula-syntax
    - pigments
    - remote-ftp
  - Hack font - https://sourcefoundry.org/hack/
  - oh-my-zsh - https://github.com/robbyrussell/oh-my-zsh
    - `ZSH_THEME="gnzh"`
    - `alias gtfo="sudo shutdown -h now"`
    - `alias ll="ls -lah"`
  - nvm - https://github.com/creationix/nvm
  - node
    - `nvm install 8.12.0`
    - `nvm use 8.12.0`
  - yarn - https://yarnpkg.com/en/
    - Add global install to PATH `/home/jonathanb/.yarn/bin`
  - docker - https://docs.docker.com/install/linux/docker-ce/ubuntu/
    - Add the following to `/etc/docker/daemon.json`

```
    {
        "bip": "192.168.2.1/24"
    }
```

# Browser Setup
- Login to sync for Google Chrome
- Login to sync for Firefox

## Add userChrome.css to Firefire
File path is `/home/${USER}/.mozilla/firefox/########.default/chrome/userChrome.css`

    @namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

    /* to hide the native tabs */
    #TabsToolbar {
        visibility: collapse;
    }

    /* to hide the sidebar header */
    #sidebar-header {
        visibility: collapse;
    }

## Add custom css to Atom
File path is `~/.atom/styles.less`

    @remote-ftp-font-size: 11px;

    // Set remote-ftp's tree view font size
    li.file.entry.list-item {
        font-size: @remote-ftp-font-size;
    }
    div.header.list-item {
        font-size: @remote-ftp-font-size;
    }

    // Set remote-ftp's tree view indent size
    .list-tree.has-collapsable-children .list-nested-item > .list-tree > li,
    .list-tree.has-collapsable-children .list-nested-item > .list-group > li {
        padding-left: 8px;
    }

    // Add in super-annoying whitespace highlighting
    .trailing-whitespace {
        text-decoration: line-through;
        text-decoration-color: #cc6666 !important;
        opacity: 0.7;
    }

# Bring in https://github.com/jonathonball/workstation-startup-tools
  - Add keyboard shortcut for `move-to-next-monitor`

# Add these search domains to your networking to make life easier
  - `inmotionhosting.com, webhostinghub.com, servconfig.com`

