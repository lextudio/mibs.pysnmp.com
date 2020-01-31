#
# PySNMP MIB module CDR-DS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CDR-DS2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectName, enterprises, TimeTicks, IpAddress, snmpModules, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, NotificationType, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, ObjectIdentity, Counter64, iso, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectName", "enterprises", "TimeTicks", "IpAddress", "snmpModules", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "NotificationType", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter64", "iso", "Counter32", "Bits")
DisplayString, TextualConvention, TimeStamp, TestAndIncr, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TestAndIncr", "TruthValue", "RowStatus")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
cdrDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7))
cdrDS2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2))
if mibBuilder.loadTexts: cdrDS2.setLastUpdated('240701')
if mibBuilder.loadTexts: cdrDS2.setOrganization('Lucent Technologies')
if mibBuilder.loadTexts: cdrDS2.setContactInfo('')
if mibBuilder.loadTexts: cdrDS2.setDescription('The MIB module for entities implementing the xxxx protocol.')
cdrSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1))
cdrClient = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cdrClient.setStatus('current')
if mibBuilder.loadTexts: cdrClient.setDescription('A newClient name.')
callState = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: callState.setStatus('current')
if mibBuilder.loadTexts: callState.setDescription('Call state.')
fCAppID = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fCAppID.setStatus('current')
if mibBuilder.loadTexts: fCAppID.setDescription("FullCircle Server' Application ID.")
fCAppInstance = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fCAppInstance.setStatus('current')
if mibBuilder.loadTexts: fCAppInstance.setDescription("FullCircle Server' Application ID.")
severity = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: severity.setStatus('current')
if mibBuilder.loadTexts: severity.setDescription('Severity of a Long Duration Call (LDC) alarm. This is configurable, thus had to be a variable.')
originationNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: originationNumber.setStatus('current')
if mibBuilder.loadTexts: originationNumber.setDescription('Originator of the LDC.')
destinationNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: destinationNumber.setStatus('current')
if mibBuilder.loadTexts: destinationNumber.setDescription('Destination of the LDC.')
callAnswerTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: callAnswerTime.setStatus('current')
if mibBuilder.loadTexts: callAnswerTime.setDescription("Call AnswerTime of the LDC, start of billing. Formatted as YYYYMMDD:hhmmssms (example '20010506:172335100' means may/06/2000 05:23PM, 35 seconds, 1000milliseconds).")
switchId = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: switchId.setStatus('current')
if mibBuilder.loadTexts: switchId.setDescription('SwitchId.')
callId = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: callId.setStatus('current')
if mibBuilder.loadTexts: callId.setDescription('CallId, internal call handle may be used for debugging.')
fullPercent = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fullPercent.setStatus('current')
if mibBuilder.loadTexts: fullPercent.setDescription('FullPercent, the DiskFull percent value.')
fileSystem = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fileSystem.setStatus('current')
if mibBuilder.loadTexts: fileSystem.setDescription('FileSystem, File System.')
mibBuilder.exportSymbols("CDR-DS2-MIB", cdrDS2=cdrDS2, callState=callState, callId=callId, lucent=lucent, cdrClient=cdrClient, cdrSystem=cdrSystem, PYSNMP_MODULE_ID=cdrDS2, fCAppInstance=fCAppInstance, fileSystem=fileSystem, callAnswerTime=callAnswerTime, originationNumber=originationNumber, destinationNumber=destinationNumber, fullPercent=fullPercent, severity=severity, cdrDeviceServer=cdrDeviceServer, softSwitch=softSwitch, switchId=switchId, products=products, fCAppID=fCAppID)