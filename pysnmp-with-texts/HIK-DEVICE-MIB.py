#
# PySNMP MIB module HIK-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HIK-DEVICE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:30:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Bits, Counter32, ModuleIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso, IpAddress, Unsigned32, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "Counter32", "ModuleIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
test = MibIdentifier((1, 3, 6, 1, 4, 1, 39165))
devicemib = MibIdentifier((1, 3, 6, 1, 4, 1, 39165, 1))
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('current')
if mibBuilder.loadTexts: deviceType.setDescription('The type of device.')
hardwVersion = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwVersion.setStatus('current')
if mibBuilder.loadTexts: hardwVersion.setDescription('The version of hardware in this device.')
softwVersion = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwVersion.setStatus('current')
if mibBuilder.loadTexts: softwVersion.setDescription('The version of software in this device')
macAddr = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddr.setStatus('current')
if mibBuilder.loadTexts: macAddr.setDescription('The MAC address of the device.')
deviceID = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceID.setStatus('current')
if mibBuilder.loadTexts: deviceID.setDescription('The code name of manufacturer of this device.')
manufacturer = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: manufacturer.setStatus('current')
if mibBuilder.loadTexts: manufacturer.setDescription('The manufacturer of this device.')
cpuPercent = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuPercent.setStatus('current')
if mibBuilder.loadTexts: cpuPercent.setDescription('Percentage of cpu used on the device.')
diskSize = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSize.setStatus('current')
if mibBuilder.loadTexts: diskSize.setDescription('The tatol size of the disk.')
diskPercent = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPercent.setStatus('current')
if mibBuilder.loadTexts: diskPercent.setDescription('Percentage of space used on disk.')
memSize = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memSize.setStatus('current')
if mibBuilder.loadTexts: memSize.setDescription('The memory size on the device.')
memUsed = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memUsed.setStatus('current')
if mibBuilder.loadTexts: memUsed.setDescription('The memory used on the device.')
restartDev = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartDev.setStatus('current')
if mibBuilder.loadTexts: restartDev.setDescription('The support of restarting the device.')
dynIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dynIpAddr.setStatus('current')
if mibBuilder.loadTexts: dynIpAddr.setDescription('The dynamic IP address.')
dynNetMask = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dynNetMask.setStatus('current')
if mibBuilder.loadTexts: dynNetMask.setDescription('The dynamic subnet mask associated with the IP address.')
dynGateway = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dynGateway.setStatus('current')
if mibBuilder.loadTexts: dynGateway.setDescription('The dynamic gateway address.')
staticIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpAddr.setStatus('current')
if mibBuilder.loadTexts: staticIpAddr.setDescription('The static IP address.')
staticNetMask = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticNetMask.setStatus('current')
if mibBuilder.loadTexts: staticNetMask.setDescription('The static subnet mask associated with the IP address.')
staticGateway = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticGateway.setStatus('current')
if mibBuilder.loadTexts: staticGateway.setDescription('The static Gateway.')
sysTime = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTime.setStatus('current')
if mibBuilder.loadTexts: sysTime.setDescription("The host's notion of the local date and time of day.")
videoInChanNum = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoInChanNum.setStatus('current')
if mibBuilder.loadTexts: videoInChanNum.setDescription('The number of video input channels.')
videoEncode = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoEncode.setStatus('current')
if mibBuilder.loadTexts: videoEncode.setDescription('The type of video coding.')
videoNetTrans = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoNetTrans.setStatus('current')
if mibBuilder.loadTexts: videoNetTrans.setDescription('The type of video network transmission.')
audioAbility = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioAbility.setStatus('current')
if mibBuilder.loadTexts: audioAbility.setDescription('The ability of audio.')
audioInNum = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioInNum.setStatus('current')
if mibBuilder.loadTexts: audioInNum.setDescription('The number of audio input.')
videoOutNum = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoOutNum.setStatus('current')
if mibBuilder.loadTexts: videoOutNum.setDescription('The number of video output.')
clarityChanNum = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clarityChanNum.setStatus('current')
if mibBuilder.loadTexts: clarityChanNum.setDescription('The number of clarity channels.')
localStorage = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: localStorage.setStatus('current')
if mibBuilder.loadTexts: localStorage.setDescription('The support of local storage.')
rtspPlayBack = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtspPlayBack.setStatus('current')
if mibBuilder.loadTexts: rtspPlayBack.setDescription('The support of RTSP lookback.')
netAccessType = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 29), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: netAccessType.setStatus('current')
if mibBuilder.loadTexts: netAccessType.setDescription('The type of network access supported.')
alarmInChanNum = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmInChanNum.setStatus('current')
if mibBuilder.loadTexts: alarmInChanNum.setDescription('The num of input channel for alarming.')
alarmOutChanNum = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOutChanNum.setStatus('current')
if mibBuilder.loadTexts: alarmOutChanNum.setDescription('The num of output channel for alarming.')
manageServAddr = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 32), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manageServAddr.setStatus('current')
if mibBuilder.loadTexts: manageServAddr.setDescription('The address of network manage host.')
managePort = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 34), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managePort.setStatus('current')
if mibBuilder.loadTexts: managePort.setDescription('The port of network manage host.')
ntpServIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 39165, 1, 33), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpServIpAddr.setStatus('current')
if mibBuilder.loadTexts: ntpServIpAddr.setDescription('The IP address of NTP server.')
mibBuilder.exportSymbols("HIK-DEVICE-MIB", manageServAddr=manageServAddr, localStorage=localStorage, softwVersion=softwVersion, dynGateway=dynGateway, videoEncode=videoEncode, devicemib=devicemib, diskPercent=diskPercent, videoNetTrans=videoNetTrans, clarityChanNum=clarityChanNum, alarmOutChanNum=alarmOutChanNum, dynIpAddr=dynIpAddr, staticGateway=staticGateway, videoInChanNum=videoInChanNum, sysTime=sysTime, manufacturer=manufacturer, diskSize=diskSize, deviceType=deviceType, memSize=memSize, macAddr=macAddr, audioInNum=audioInNum, netAccessType=netAccessType, staticNetMask=staticNetMask, alarmInChanNum=alarmInChanNum, hardwVersion=hardwVersion, memUsed=memUsed, ntpServIpAddr=ntpServIpAddr, rtspPlayBack=rtspPlayBack, videoOutNum=videoOutNum, managePort=managePort, dynNetMask=dynNetMask, cpuPercent=cpuPercent, restartDev=restartDev, staticIpAddr=staticIpAddr, test=test, deviceID=deviceID, audioAbility=audioAbility)