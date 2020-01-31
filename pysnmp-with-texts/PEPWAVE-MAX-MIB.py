#
# PySNMP MIB module PEPWAVE-MAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PEPWAVE-MAX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:40:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, NotificationType, Counter64, MibIdentifier, Bits, Integer32, iso, ObjectIdentity, Gauge32, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "NotificationType", "Counter64", "MibIdentifier", "Bits", "Integer32", "iso", "ObjectIdentity", "Gauge32", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pepwaveMAX = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 1))
pepwaveMAX.setRevisions(('2012-06-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pepwaveMAX.setRevisionsDescriptions(('Initial release.',))
if mibBuilder.loadTexts: pepwaveMAX.setLastUpdated('201206060000Z')
if mibBuilder.loadTexts: pepwaveMAX.setOrganization('Pepwave')
if mibBuilder.loadTexts: pepwaveMAX.setContactInfo('Pepwave http://www.pepwave.com Support: http://www.pepwave.com/contact/support/ Email: info@pepwave.com ')
if mibBuilder.loadTexts: pepwaveMAX.setDescription('MIB module for Pepwave MAX.')
class TableIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ConnectionNum(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each WAN connection number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NameString(TextualConvention, OctetString):
    description = 'MAX name string.'
    status = 'current'
    displayHint = '80a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

class PortSpeedType(TextualConvention, Integer32):
    description = 'Describe the port speed and type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

maxStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1))
maxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1))
maxFirmware = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxFirmware.setStatus('current')
if mibBuilder.loadTexts: maxFirmware.setDescription('MAX firmware version.')
maxSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxSerialNumber.setStatus('current')
if mibBuilder.loadTexts: maxSerialNumber.setDescription('MAX serial number.')
maxTime = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxTime.setStatus('current')
if mibBuilder.loadTexts: maxTime.setDescription('MAX system time.')
maxUpTime = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxUpTime.setStatus('current')
if mibBuilder.loadTexts: maxUpTime.setDescription('MAX up time (in hundredths of a second) since the system was last re-initialized.')
maxLan = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6))
maxLanStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanStatus.setStatus('current')
if mibBuilder.loadTexts: maxLanStatus.setDescription('MAX LAN status (up/down).')
maxLanIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanIp.setStatus('current')
if mibBuilder.loadTexts: maxLanIp.setDescription('MAX LAN IP address.')
maxLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanSubnetMask.setStatus('current')
if mibBuilder.loadTexts: maxLanSubnetMask.setDescription('MAX LAN sub-net mask.')
maxLinkStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2))
maxLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLinkNumber.setStatus('current')
if mibBuilder.loadTexts: maxLinkNumber.setDescription('The number of network interfaces (regardless of their current state) present on this system.')
linkTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2), )
if mibBuilder.loadTexts: linkTable.setStatus('current')
if mibBuilder.loadTexts: linkTable.setDescription('A list of link status.')
linkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "linkConnNum"))
if mibBuilder.loadTexts: linkEntry.setStatus('current')
if mibBuilder.loadTexts: linkEntry.setDescription('An entry containing management information applicable to a particular interface.')
linkConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkConnNum.setStatus('current')
if mibBuilder.loadTexts: linkConnNum.setDescription('Virtual WAN index number (1-based, unique).')
linkName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkName.setStatus('current')
if mibBuilder.loadTexts: linkName.setDescription('MAX link status (connecting/connected/link down).')
linkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkStatus.setStatus('current')
if mibBuilder.loadTexts: linkStatus.setDescription('MAX link status (connecting/connected/link down).')
linkThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputIn.setStatus('current')
if mibBuilder.loadTexts: linkThroughputIn.setDescription('The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of maxWanCounterDiscontinuityTime.')
linkThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputOut.setStatus('current')
if mibBuilder.loadTexts: linkThroughputOut.setDescription('The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of maxWanCounterDiscontinuityTime.')
linkDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDataTransferred.setStatus('current')
if mibBuilder.loadTexts: linkDataTransferred.setDescription('The numbe of bytes transferred through.')
linkIpTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3), )
if mibBuilder.loadTexts: linkIpTable.setStatus('current')
if mibBuilder.loadTexts: linkIpTable.setDescription('A list of link status.')
linkIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "linkIpConnNum"), (0, "PEPWAVE-MAX-MIB", "linkIpIndex"))
if mibBuilder.loadTexts: linkIpEntry.setStatus('current')
if mibBuilder.loadTexts: linkIpEntry.setDescription('An entry containing management information applicable to a particular interface.')
linkIpConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkIpConnNum.setStatus('current')
if mibBuilder.loadTexts: linkIpConnNum.setDescription('Virtual WAN index number.')
linkIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 2), TableIndex())
if mibBuilder.loadTexts: linkIpIndex.setStatus('current')
if mibBuilder.loadTexts: linkIpIndex.setDescription('Virtual WAN index number.')
linkIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkIp.setStatus('current')
if mibBuilder.loadTexts: linkIp.setDescription('MAX link IP address list.')
wanUsageTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3), )
if mibBuilder.loadTexts: wanUsageTable.setStatus('current')
if mibBuilder.loadTexts: wanUsageTable.setDescription('A list of interface entries.')
wanUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "wanUsageIndex"))
if mibBuilder.loadTexts: wanUsageEntry.setStatus('current')
if mibBuilder.loadTexts: wanUsageEntry.setDescription('An entry containing management information applicable to a particular interface.')
wanUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 1), TableIndex())
if mibBuilder.loadTexts: wanUsageIndex.setStatus('current')
if mibBuilder.loadTexts: wanUsageIndex.setDescription('Physical WAN index number.')
wanUsageThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputIn.setStatus('current')
if mibBuilder.loadTexts: wanUsageThroughputIn.setDescription('The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of maxWanCounterDiscontinuityTime.')
wanUsageThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputOut.setStatus('current')
if mibBuilder.loadTexts: wanUsageThroughputOut.setDescription('The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of maxWanCounterDiscontinuityTime.')
wanUsageDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageDataTransferred.setStatus('current')
if mibBuilder.loadTexts: wanUsageDataTransferred.setDescription('The numbe of bytes transferred through.')
maxMaintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 2))
maxReboot = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 2, 1), NameString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxReboot.setStatus('current')
if mibBuilder.loadTexts: maxReboot.setDescription("Reboot the device. Write 'enable' to take effect.")
maxLanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 3))
portLanSpeedConfig = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 1), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLanSpeedConfig.setStatus('current')
if mibBuilder.loadTexts: portLanSpeedConfig.setDescription("Set device's LAN port speed (Auto/10baseT-FD/ 10baseT-HD/100baseTx-FD/100baseTx-HD/1000baseTx-FD/ 1000baseTx-HD.")
portWanSpeedConfigTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2), )
if mibBuilder.loadTexts: portWanSpeedConfigTable.setStatus('current')
if mibBuilder.loadTexts: portWanSpeedConfigTable.setDescription('A list of interface entries.')
portWanSpeedConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "portWanSpeedConfigIndex"))
if mibBuilder.loadTexts: portWanSpeedConfigEntry.setStatus('current')
if mibBuilder.loadTexts: portWanSpeedConfigEntry.setDescription('An entry containing management information applicable to a particular interface.')
portWanSpeedConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 1), TableIndex())
if mibBuilder.loadTexts: portWanSpeedConfigIndex.setStatus('current')
if mibBuilder.loadTexts: portWanSpeedConfigIndex.setDescription('Physical LAN/WAN port name.')
portWanSpeedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 2), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portWanSpeedConfig.setStatus('current')
if mibBuilder.loadTexts: portWanSpeedConfig.setDescription("Set device's WAN port speed (Auto/10baseT-FD/ 10baseT-HD/100baseTx-FD/100baseTx-HD/1000baseTx-FD/ 1000baseTx-HD.")
lanConfigIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigIp.setStatus('current')
if mibBuilder.loadTexts: lanConfigIp.setDescription("Set device's LAN IP address.")
lanConfigSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigSubnetMask.setStatus('current')
if mibBuilder.loadTexts: lanConfigSubnetMask.setDescription("Set device's LAN sub-net mask.")
maxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50))
maxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50, 1))
maxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2))
maxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27662, 1, 50, 1, 1)).setObjects(("PEPWAVE-MAX-MIB", "maxSystemGroup"), ("PEPWAVE-MAX-MIB", "maxLinkGroup"), ("PEPWAVE-MAX-MIB", "maxWanGroup"), ("PEPWAVE-MAX-MIB", "maxSetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxCompliance = maxCompliance.setStatus('current')
if mibBuilder.loadTexts: maxCompliance.setDescription('MAX compliance groups.')
maxSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 1)).setObjects(("PEPWAVE-MAX-MIB", "maxFirmware"), ("PEPWAVE-MAX-MIB", "maxSerialNumber"), ("PEPWAVE-MAX-MIB", "maxTime"), ("PEPWAVE-MAX-MIB", "maxUpTime"), ("PEPWAVE-MAX-MIB", "maxLanStatus"), ("PEPWAVE-MAX-MIB", "maxLanIp"), ("PEPWAVE-MAX-MIB", "maxLanSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxSystemGroup = maxSystemGroup.setStatus('current')
if mibBuilder.loadTexts: maxSystemGroup.setDescription("MAX's system status group.")
maxLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 2)).setObjects(("PEPWAVE-MAX-MIB", "maxLinkNumber"), ("PEPWAVE-MAX-MIB", "linkName"), ("PEPWAVE-MAX-MIB", "linkStatus"), ("PEPWAVE-MAX-MIB", "linkIp"), ("PEPWAVE-MAX-MIB", "linkThroughputIn"), ("PEPWAVE-MAX-MIB", "linkThroughputOut"), ("PEPWAVE-MAX-MIB", "linkDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxLinkGroup = maxLinkGroup.setStatus('current')
if mibBuilder.loadTexts: maxLinkGroup.setDescription("MAX's system status group.")
maxWanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 3)).setObjects(("PEPWAVE-MAX-MIB", "wanUsageThroughputIn"), ("PEPWAVE-MAX-MIB", "wanUsageThroughputOut"), ("PEPWAVE-MAX-MIB", "wanUsageDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxWanGroup = maxWanGroup.setStatus('current')
if mibBuilder.loadTexts: maxWanGroup.setDescription("MAX's system status group.")
maxSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 4)).setObjects(("PEPWAVE-MAX-MIB", "maxReboot"), ("PEPWAVE-MAX-MIB", "portWanSpeedConfig"), ("PEPWAVE-MAX-MIB", "portLanSpeedConfig"), ("PEPWAVE-MAX-MIB", "lanConfigIp"), ("PEPWAVE-MAX-MIB", "lanConfigSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxSetGroup = maxSetGroup.setStatus('current')
if mibBuilder.loadTexts: maxSetGroup.setDescription("MAX's system status group.")
mibBuilder.exportSymbols("PEPWAVE-MAX-MIB", linkThroughputOut=linkThroughputOut, wanUsageThroughputIn=wanUsageThroughputIn, wanUsageEntry=wanUsageEntry, maxLinkStatus=maxLinkStatus, maxReboot=maxReboot, portLanSpeedConfig=portLanSpeedConfig, TableIndex=TableIndex, ConnectionNum=ConnectionNum, maxFirmware=maxFirmware, maxLinkNumber=maxLinkNumber, linkIpEntry=linkIpEntry, maxMaintenance=maxMaintenance, maxWanGroup=maxWanGroup, wanUsageTable=wanUsageTable, portWanSpeedConfigEntry=portWanSpeedConfigEntry, lanConfigSubnetMask=lanConfigSubnetMask, maxLinkGroup=maxLinkGroup, linkIpConnNum=linkIpConnNum, maxSystem=maxSystem, PortSpeedType=PortSpeedType, maxStatus=maxStatus, maxSerialNumber=maxSerialNumber, maxUpTime=maxUpTime, maxLanIp=maxLanIp, maxLanConfig=maxLanConfig, portWanSpeedConfig=portWanSpeedConfig, maxSystemGroup=maxSystemGroup, linkConnNum=linkConnNum, wanUsageThroughputOut=wanUsageThroughputOut, linkName=linkName, maxCompliance=maxCompliance, linkThroughputIn=linkThroughputIn, maxCompliances=maxCompliances, wanUsageIndex=wanUsageIndex, lanConfigIp=lanConfigIp, wanUsageDataTransferred=wanUsageDataTransferred, maxLan=maxLan, linkDataTransferred=linkDataTransferred, maxLanSubnetMask=maxLanSubnetMask, linkIp=linkIp, maxConformance=maxConformance, linkTable=linkTable, pepwaveMAX=pepwaveMAX, PYSNMP_MODULE_ID=pepwaveMAX, maxSetGroup=maxSetGroup, maxGroups=maxGroups, portWanSpeedConfigIndex=portWanSpeedConfigIndex, maxLanStatus=maxLanStatus, linkIpIndex=linkIpIndex, linkIpTable=linkIpTable, maxTime=maxTime, linkEntry=linkEntry, linkStatus=linkStatus, NameString=NameString, portWanSpeedConfigTable=portWanSpeedConfigTable)