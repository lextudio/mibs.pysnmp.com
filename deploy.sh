#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root (administrator)." 1>&2
   exit 1
fi

cd /var/www/mibs.pysnmp.com/html
git pull

cd /home/lextudio/sharpsnmplib-samples
git pull

killall snmpd
cd /home/lextudio/sharpsnmplib-samples/Samples/CSharpCore/snmpd
dotnet publish --framework net6.0 -c Release
nohup ./bin/Release/net6.0/publish/snmpd >/dev/null 2>&1 &
ps aux | grep snmpd

killall snmptrapd
cd /home/lextudio/sharpsnmplib-samples/Samples/CSharpCore/snmptrapd
dotnet publish -c Release --framework net6.0
nohup ./bin/Release/net6.0/publish/snmptrapd >/dev/null 2>&1 &
ps aux | grep snmptrapd
