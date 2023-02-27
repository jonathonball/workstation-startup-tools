# Prepare The System

    sudo apt update
    sudo apt upgrade

# Copy in SSH keys

# Copy in keepass key file

# Install from repos:
  - vim
  - curl
  - zsh
  - terminator
  - redshift
  - xdotool
  - ack
  - tree
  - vlc
  - network-manager-openvpn
  - network-manager-openvpn-gnome
  - openvpn
  - build-essential
  - xscreensaver
  - xscreensaver-data
  - xscreensaver-data-extra
  - xscreensaver-gl
  - xscreensaver-gl-extra
  - whois
  - figlet
  - lolcat
  - jq
  - acpi
  - xfce4-goodies
  - pavucontrol

# Download and install from external sources:
  - Google Chrome - https://www.google.com/chrome/
  - Keeweb - https://keeweb.info/
  - Slack - https://slack.com/downloads/linux
  - git
  - guake
  - vs-code
  - Hack font - https://sourcefoundry.org/hack/
  - oh-my-zsh - https://github.com/robbyrussell/oh-my-zsh
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
First enable `toolkit.legacyUserProfileCustomizations.stylesheets` in `about:confg`.
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

# Bring in https://github.com/jonathonball/workstation-startup-tools
  - Add keyboard shortcut for `move-to-next-monitor`

# Disable gnome-keyring's control over ssh keys

    cp /etc/xdg/autostart/gnome-keyring-ssh.desktop ~/.config/autostart
    echo "Hidden=true" >> ~/.config/autostart/gnome-keyring-ssh.desktop
    xfce4-session-logout --logout
