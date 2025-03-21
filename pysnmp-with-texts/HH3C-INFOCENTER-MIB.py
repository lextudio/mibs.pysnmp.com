#
# PySNMP MIB module HH3C-INFOCENTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-INFOCENTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, Unsigned32, NotificationType, Counter64, ObjectIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, IpAddress, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "Counter64", "ObjectIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "IpAddress", "Integer32", "Gauge32")
TruthValue, DisplayString, TAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TAddress", "RowStatus", "TextualConvention")
hh3cInfoCenter = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 119))
hh3cInfoCenter.setRevisions(('2012-03-07 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cInfoCenter.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: hh3cInfoCenter.setLastUpdated('201203071900Z')
if mibBuilder.loadTexts: hh3cInfoCenter.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cInfoCenter.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cInfoCenter.setDescription('All the configuration of the info center can be managed by info center MIB.')
class ICMessageLevelType(TextualConvention, Integer32):
    description = 'Specify severity level of message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("informational", 6), ("debug", 7), ("invalid", 8))

class ICFacilityType(TextualConvention, Integer32):
    description = 'Specify loghost facility which generates messages.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("userLevel", 1), ("mailSystem", 2), ("systemDaemons", 3), ("securityAuthorization", 4), ("internallyMessages", 5), ("linePrinter", 6), ("networkNews", 7), ("uucp", 8), ("clockDaemon", 9), ("securityAuthorization2", 10), ("ftpDaemon", 11), ("ntp", 12), ("logAudit", 13), ("logAlert", 14), ("clockDaemon2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class ICTimeStampType(TextualConvention, Integer32):
    description = 'Specify operation types on time stamp of message. date: the time stamp type of message is date. boot: the time stamp type of message is the time from uptime of system. iso: the time stamp type of message is ISO date with format YYYY-MM-ddThh:mm:ss. dateWithoutYear: the time stamp type of message is date without year information. none: no time stamp information in message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("date", 0), ("boot", 1), ("iso", 2), ("dateWithoutYear", 3), ("none", 4))

hh3cICLogbuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1))
hh3cICLogbufferObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1))
hh3cICMaxLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICMaxLogbufferSize.setStatus('current')
if mibBuilder.loadTexts: hh3cICMaxLogbufferSize.setDescription('The maximum number of messages that can be stored in logbuffer.')
hh3cICLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 2), Unsigned32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cICLogbufferSize.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferSize.setDescription('The capacity of logbuffer which can be customized by users. The valid range is from 0 to hh3cICMaxLogbufferSize.')
hh3cICLogbufferCurrentMessages = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICLogbufferCurrentMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferCurrentMessages.setDescription('The number of log messages stored in logbuffer.')
hh3cICLogbufferOverwrittenMessages = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICLogbufferOverwrittenMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferOverwrittenMessages.setDescription('The number of log messages overwritten in logbuffer.')
hh3cICLogbufferDroppedMessages = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICLogbufferDroppedMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferDroppedMessages.setDescription('The number of log messages dropped in logbuffer.')
hh3cICLogbufferContTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2), )
if mibBuilder.loadTexts: hh3cICLogbufferContTable.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferContTable.setDescription('The table of logbuffer contents.')
hh3cICLogbufferContEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2, 1), ).setIndexNames((0, "HH3C-INFOCENTER-MIB", "hh3cICLogbufferContIndex"))
if mibBuilder.loadTexts: hh3cICLogbufferContEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferContEntry.setDescription('The contents entry of logbuffer.')
hh3cICLogbufferContIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cICLogbufferContIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferContIndex.setDescription('The index of this table.')
hh3cICLogbufferContDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICLogbufferContDescription.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogbufferContDescription.setDescription('The contents of logbuffer.')
hh3cICLoghost = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2))
hh3cICLoghostObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1))
hh3cICMaxLoghost = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICMaxLoghost.setStatus('current')
if mibBuilder.loadTexts: hh3cICMaxLoghost.setDescription('The object shows the maximum number of rows in hh3cLoghostTable.')
hh3cICLoghostSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cICLoghostSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostSourceInterface.setDescription('The source interface which sends message to loghost. All loghosts use the same source interface. Zero is invalid.')
hh3cICLoghostTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 1, 3), ICTimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cICLoghostTimestampType.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostTimestampType.setDescription('Time stamp type of message sent to loghost.')
hh3cICLoghostTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2), )
if mibBuilder.loadTexts: hh3cICLoghostTable.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostTable.setDescription('The table of loghost.')
hh3cICLoghostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1), ).setIndexNames((0, "HH3C-INFOCENTER-MIB", "hh3cICLoghostIndex"))
if mibBuilder.loadTexts: hh3cICLoghostEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostEntry.setDescription('The loghost entry of syslog.')
hh3cICLoghostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hh3cICLoghostIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostIndex.setDescription('The index of this table.')
hh3cICLoghostIpaddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostIpaddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostIpaddressType.setDescription('The IP address type of loghost.')
hh3cICLoghostIpaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostIpaddress.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostIpaddress.setDescription('The IP address of loghost.')
hh3cICLoghostVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostVPNName.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostVPNName.setDescription('The VPN instance of loghost.')
hh3cICLoghostFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 5), ICFacilityType().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostFacility.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostFacility.setDescription('The operations staff can selectively filter the messages with priority which consists of facility that generates the message and severity of the message. ')
hh3cICLoghostOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostOperateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostOperateRowStatus.setDescription('The status of this table entry.')
hh3cICLoghostIpaddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostIpaddressPort.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostIpaddressPort.setDescription('The loghost server port.')
hh3cICLoghostTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 2, 2, 1, 8), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLoghostTAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cICLoghostTAddress.setDescription("The loghost server transport address. Consist of hh3cICLoghostIpaddress(ipv4) and hh3cICLoghostIpaddressPort. This node can't be bound with hh3cICLoghostIpaddress, hh3cICLoghostIpaddressPort and hh3cICLoghostIpaddressType at the same time.")
hh3cICDirection = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 3))
hh3cICDirectionTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1), )
if mibBuilder.loadTexts: hh3cICDirectionTable.setStatus('current')
if mibBuilder.loadTexts: hh3cICDirectionTable.setDescription('A table of syslog output direction.')
hh3cICDirectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1), ).setIndexNames((0, "HH3C-INFOCENTER-MIB", "hh3cICDirectionIndex"))
if mibBuilder.loadTexts: hh3cICDirectionEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cICDirectionEntry.setDescription('The output direction entry of syslog.')
hh3cICDirectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cICDirectionIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cICDirectionIndex.setDescription('The index of this table.')
hh3cICDirectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICDirectionName.setStatus('current')
if mibBuilder.loadTexts: hh3cICDirectionName.setDescription('The name of output direction.')
hh3cICDirectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 3, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cICDirectionState.setStatus('current')
if mibBuilder.loadTexts: hh3cICDirectionState.setDescription('The state of syslog: true(1):enable. false(2):disable.')
hh3cICModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 4))
hh3cICModuleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 119, 4, 1), )
if mibBuilder.loadTexts: hh3cICModuleTable.setStatus('current')
if mibBuilder.loadTexts: hh3cICModuleTable.setDescription('A table of syslog module.')
hh3cICModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 119, 4, 1, 1), ).setIndexNames((1, "HH3C-INFOCENTER-MIB", "hh3cICModuleName"))
if mibBuilder.loadTexts: hh3cICModuleEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cICModuleEntry.setDescription('The module entry of syslog.')
hh3cICModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cICModuleName.setStatus('current')
if mibBuilder.loadTexts: hh3cICModuleName.setDescription('The name of module.')
hh3cICLog = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5))
hh3cICLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 1))
hh3cICLogGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cICLogGlobalState.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogGlobalState.setDescription('The global state of syslog: true(1):enable. false(2):disable.')
hh3cICLogTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 1, 2), ICTimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cICLogTimestampType.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogTimestampType.setDescription('Time stamp type of log message.')
hh3cICLogTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2), )
if mibBuilder.loadTexts: hh3cICLogTable.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogTable.setDescription('A table of syslog module.')
hh3cICLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2, 1), ).setIndexNames((0, "HH3C-INFOCENTER-MIB", "hh3cICDirectionIndex"), (1, "HH3C-INFOCENTER-MIB", "hh3cICModuleName"))
if mibBuilder.loadTexts: hh3cICLogEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogEntry.setDescription('The log entry of syslog.')
hh3cICLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2, 1, 1), ICMessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLogLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogLevel.setDescription('The level of log message, invalid is for deny any log.')
hh3cICLogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 119, 5, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cICLogRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cICLogRowStatus.setDescription('The status of this table entry.')
mibBuilder.exportSymbols("HH3C-INFOCENTER-MIB", hh3cICMaxLoghost=hh3cICMaxLoghost, hh3cICLogbufferContTable=hh3cICLogbufferContTable, hh3cICLogEntry=hh3cICLogEntry, hh3cICDirectionIndex=hh3cICDirectionIndex, hh3cICLogbufferDroppedMessages=hh3cICLogbufferDroppedMessages, hh3cICDirectionState=hh3cICDirectionState, hh3cICModuleName=hh3cICModuleName, ICTimeStampType=ICTimeStampType, hh3cICDirectionEntry=hh3cICDirectionEntry, hh3cICDirectionTable=hh3cICDirectionTable, hh3cICLogbufferContDescription=hh3cICLogbufferContDescription, hh3cICLogGlobalState=hh3cICLogGlobalState, hh3cICMaxLogbufferSize=hh3cICMaxLogbufferSize, hh3cICLoghostEntry=hh3cICLoghostEntry, hh3cICDirectionName=hh3cICDirectionName, ICFacilityType=ICFacilityType, hh3cICLoghostSourceInterface=hh3cICLoghostSourceInterface, hh3cICLoghostIndex=hh3cICLoghostIndex, ICMessageLevelType=ICMessageLevelType, hh3cICModuleEntry=hh3cICModuleEntry, hh3cICLogbuffer=hh3cICLogbuffer, hh3cICLoghostObjects=hh3cICLoghostObjects, hh3cICLoghostVPNName=hh3cICLoghostVPNName, hh3cICModuleTable=hh3cICModuleTable, hh3cICLogbufferContEntry=hh3cICLogbufferContEntry, hh3cICModule=hh3cICModule, hh3cICLogTimestampType=hh3cICLogTimestampType, hh3cICLoghostTimestampType=hh3cICLoghostTimestampType, hh3cInfoCenter=hh3cInfoCenter, hh3cICLogTable=hh3cICLogTable, hh3cICLogbufferSize=hh3cICLogbufferSize, hh3cICLoghost=hh3cICLoghost, hh3cICLoghostIpaddress=hh3cICLoghostIpaddress, hh3cICLogbufferContIndex=hh3cICLogbufferContIndex, hh3cICLogLevel=hh3cICLogLevel, hh3cICLogbufferOverwrittenMessages=hh3cICLogbufferOverwrittenMessages, hh3cICLogObjects=hh3cICLogObjects, hh3cICLoghostOperateRowStatus=hh3cICLoghostOperateRowStatus, hh3cICLogRowStatus=hh3cICLogRowStatus, hh3cICLoghostIpaddressPort=hh3cICLoghostIpaddressPort, hh3cICDirection=hh3cICDirection, hh3cICLoghostTAddress=hh3cICLoghostTAddress, hh3cICLog=hh3cICLog, hh3cICLogbufferObjects=hh3cICLogbufferObjects, hh3cICLoghostTable=hh3cICLoghostTable, hh3cICLogbufferCurrentMessages=hh3cICLogbufferCurrentMessages, hh3cICLoghostFacility=hh3cICLoghostFacility, hh3cICLoghostIpaddressType=hh3cICLoghostIpaddressType, PYSNMP_MODULE_ID=hh3cInfoCenter)
