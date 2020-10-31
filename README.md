# Haas-ToolBox

## Installation on Linux (Debian/Ubuntu)

```
apt-install python3 python3-pip -y
pip3 install -r requirements.txt
chmod +x *.py
```

## Configuration

1. Edit HTS/Settings/MailSettings.xml set these lines (changing unique_token for a random password):
  ```
  <LocalAPIAdres>127.0.0.1</LocalAPIAdres>
  <LocalAPIPort>8095</LocalAPIPort>
  <LocalAPIToken/>unique_token<LocalAPIToken>
  ```
2. Restart HTS (kill mono and relaunch) or reboot your system.

3. Set the same token in config.ini.

## First run

```
python3 BaseHaas.py
```
