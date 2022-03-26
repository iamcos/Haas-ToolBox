# Haas-ToolBox

## Configuration

1. Edit HTS/Settings/MailSettings.xml set these lines (changing unique_token for a random password):
  ```
  <LocalAPIAdres>127.0.0.1</LocalAPIAdres>
  <LocalAPIPort>8095</LocalAPIPort>
  <LocalAPIToken/>unique_token<LocalAPIToken>
  ```
2. Restart HTS (kill mono and relaunch) or reboot your system.

3. Set the same token in ./api/config/config.ini.

## Dependencies

Only Python3.10 must be installed by hands

### Debian based
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
```

### Arch based
```
sudo pacman -s python
```

### Fedora/CentOs
```
sudo dnf update && sudo dnf upgrade -y
sudo dnf install --enablerepo=updates-testing python3.10
sudo dnf install python3.10
```

## First run
```
./run.sh
```
