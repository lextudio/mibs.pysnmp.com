#
# PySNMP MIB module ZYXEL-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, Integer32, IpAddress, Gauge32, ObjectIdentity, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "Integer32", "IpAddress", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelSysLog = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81))
if mibBuilder.loadTexts: zyxelSysLog.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelSysLog.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelSysLog.setContactInfo('')
if mibBuilder.loadTexts: zyxelSysLog.setDescription('The subtree for syslog')
zyxelSysLogSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1))
zySysLogState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysLogState.setStatus('current')
if mibBuilder.loadTexts: zySysLogState.setDescription('Enable/Disable sysLog for the switch. The syslog feature sends logs to an external syslog server.')
zyxelSysLogTypeTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2), )
if mibBuilder.loadTexts: zyxelSysLogTypeTable.setStatus('current')
if mibBuilder.loadTexts: zyxelSysLogTypeTable.setDescription('The table contains system logs type configuration.')
zyxelSysLogTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1), ).setIndexNames((0, "ZYXEL-SYSLOG-MIB", "zySysLogTypeIndex"))
if mibBuilder.loadTexts: zyxelSysLogTypeEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelSysLogTypeEntry.setDescription('An entry contains system logs type configuration.')
zySysLogTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zySysLogTypeIndex.setStatus('current')
if mibBuilder.loadTexts: zySysLogTypeIndex.setDescription('The index of syslog type categories.')
zySysLogTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysLogTypeName.setStatus('current')
if mibBuilder.loadTexts: zySysLogTypeName.setDescription('The names of syslog categories that the device can generate.')
zySysLogTypeState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysLogTypeState.setStatus('current')
if mibBuilder.loadTexts: zySysLogTypeState.setDescription('Enable/Disable the device to generate logs for the corresponding category.')
zySysLogTypeFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("localUser0", 0), ("localUser1", 1), ("localUser2", 2), ("localUser3", 3), ("localUser4", 4), ("localUser5", 5), ("localUser6", 6), ("localUser7", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysLogTypeFacility.setStatus('current')
if mibBuilder.loadTexts: zySysLogTypeFacility.setDescription('Enter the log facility that allows you to send logs to different files in the syslog server.')
zySysLogMaxNumberOfServers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysLogMaxNumberOfServers.setStatus('current')
if mibBuilder.loadTexts: zySysLogMaxNumberOfServers.setDescription('The maximum number of sys log servers that can be created.')
zyxelSysLogServerTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4), )
if mibBuilder.loadTexts: zyxelSysLogServerTable.setStatus('current')
if mibBuilder.loadTexts: zyxelSysLogServerTable.setDescription('The table contains system logs server configuration.')
zyxelSysLogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1), ).setIndexNames((0, "ZYXEL-SYSLOG-MIB", "zySysLogServerIpAddress"))
if mibBuilder.loadTexts: zyxelSysLogServerEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelSysLogServerEntry.setDescription('An entry contains system logs server configuration.')
zySysLogServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: zySysLogServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: zySysLogServerIpAddress.setDescription('The IP address of the syslog server.')
zySysLogServerLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("level0", 0), ("level0To1", 1), ("level0To2", 2), ("level0To3", 3), ("level0To4", 4), ("level0To5", 5), ("level0To6", 6), ("level0To7", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysLogServerLogLevel.setStatus('current')
if mibBuilder.loadTexts: zySysLogServerLogLevel.setDescription('Enter the severity level(s) of the logs that you want the device to send to this syslog server. The lower the number, the more critical the logs are.')
zySysLogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 81, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zySysLogServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: zySysLogServerRowStatus.setDescription('This object allows entry to be created and deleted syslog servers configuration.')
mibBuilder.exportSymbols("ZYXEL-SYSLOG-MIB", zyxelSysLog=zyxelSysLog, PYSNMP_MODULE_ID=zyxelSysLog, zySysLogServerRowStatus=zySysLogServerRowStatus, zyxelSysLogServerEntry=zyxelSysLogServerEntry, zySysLogServerIpAddress=zySysLogServerIpAddress, zyxelSysLogSetup=zyxelSysLogSetup, zySysLogState=zySysLogState, zySysLogMaxNumberOfServers=zySysLogMaxNumberOfServers, zySysLogServerLogLevel=zySysLogServerLogLevel, zySysLogTypeFacility=zySysLogTypeFacility, zyxelSysLogTypeTable=zyxelSysLogTypeTable, zyxelSysLogServerTable=zyxelSysLogServerTable, zySysLogTypeName=zySysLogTypeName, zyxelSysLogTypeEntry=zyxelSysLogTypeEntry, zySysLogTypeIndex=zySysLogTypeIndex, zySysLogTypeState=zySysLogTypeState)