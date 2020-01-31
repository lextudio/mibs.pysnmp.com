#
# PySNMP MIB module DFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DFM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:42:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Counter64, Integer32, iso, Gauge32, MibIdentifier, enterprises, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Counter64", "Integer32", "iso", "Gauge32", "MibIdentifier", "enterprises", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 733))
if mibBuilder.loadTexts: dfmMIB.setLastUpdated('9909232300Z')
if mibBuilder.loadTexts: dfmMIB.setOrganization('Cisco Systems')
if mibBuilder.loadTexts: dfmMIB.setContactInfo('Support Postal:Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 US Phone:+1 408 526-4000 E-mail:tac@cisco.com')
if mibBuilder.loadTexts: dfmMIB.setDescription('The CiscoWorks2000 Device Fault Manager MIB module for entities defined by Cisco Systems, Inc.')
smNotificationTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 733, 0))
smNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 733, 2))
smGenericNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 733, 2, 1))
smNotifTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 1), Counter32())
if mibBuilder.loadTexts: smNotifTimestamp.setStatus('current')
if mibBuilder.loadTexts: smNotifTimestamp.setDescription('The timestamp of the notification.')
smNotifServer = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 2), OctetString())
if mibBuilder.loadTexts: smNotifServer.setStatus('current')
if mibBuilder.loadTexts: smNotifServer.setDescription('The name of the server that is sending the notification.')
smNotifClass = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 3), OctetString())
if mibBuilder.loadTexts: smNotifClass.setStatus('current')
if mibBuilder.loadTexts: smNotifClass.setDescription('The class of the object associated with the notification.')
smNotifInstance = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 4), OctetString())
if mibBuilder.loadTexts: smNotifInstance.setStatus('current')
if mibBuilder.loadTexts: smNotifInstance.setDescription('The instance name of the object associated with the notification.')
smNotifEventName = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 5), OctetString())
if mibBuilder.loadTexts: smNotifEventName.setStatus('current')
if mibBuilder.loadTexts: smNotifEventName.setDescription('The name of the event causing the notification.')
smNotifInstanceID = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 6), OctetString())
if mibBuilder.loadTexts: smNotifInstanceID.setStatus('current')
if mibBuilder.loadTexts: smNotifInstanceID.setDescription('The unique DFM inventory identification for the object associated with the notification .')
smNotifDescription = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 7), OctetString())
if mibBuilder.loadTexts: smNotifDescription.setStatus('current')
if mibBuilder.loadTexts: smNotifDescription.setDescription('A complete description of the event.')
smNotifCertainty = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 8), OctetString())
if mibBuilder.loadTexts: smNotifCertainty.setStatus('current')
if mibBuilder.loadTexts: smNotifCertainty.setDescription('The certainty of the event. Floating-point number in the range 0-100, stored as a string.')
smNotifSeverity = MibScalar((1, 3, 6, 1, 4, 1, 733, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("informational", 2), ("warning", 3), ("minor", 4), ("major", 5), ("severe", 6))))
if mibBuilder.loadTexts: smNotifSeverity.setStatus('current')
if mibBuilder.loadTexts: smNotifSeverity.setDescription('The severity of the event. Integer number in the range 1-6.')
smTrapNotification = NotificationType((1, 3, 6, 1, 4, 1, 733, 0, 4)).setObjects(("DFM-MIB", "smNotifTimestamp"), ("DFM-MIB", "smNotifServer"), ("DFM-MIB", "smNotifClass"), ("DFM-MIB", "smNotifInstance"), ("DFM-MIB", "smNotifEventName"), ("DFM-MIB", "smNotifInstanceID"), ("DFM-MIB", "smNotifDescription"), ("DFM-MIB", "smNotifCertainty"), ("DFM-MIB", "smNotifSeverity"))
if mibBuilder.loadTexts: smTrapNotification.setStatus('current')
if mibBuilder.loadTexts: smTrapNotification.setDescription('A trap describing a DFM root cause notification. The text in smNotifDescription indicates the nature of the problem.')
smTrapCertaintyChange = NotificationType((1, 3, 6, 1, 4, 1, 733, 0, 2)).setObjects(("DFM-MIB", "smNotifTimestamp"), ("DFM-MIB", "smNotifServer"), ("DFM-MIB", "smNotifClass"), ("DFM-MIB", "smNotifInstance"), ("DFM-MIB", "smNotifEventName"), ("DFM-MIB", "smNotifInstanceID"), ("DFM-MIB", "smNotifDescription"), ("DFM-MIB", "smNotifCertainty"), ("DFM-MIB", "smNotifSeverity"))
if mibBuilder.loadTexts: smTrapCertaintyChange.setStatus('current')
if mibBuilder.loadTexts: smTrapCertaintyChange.setDescription('A trap indicating a certainty change of a DFM notification. The text in smNotifDescription indicates the nature of the problem.')
smTrapSeverityChange = NotificationType((1, 3, 6, 1, 4, 1, 733, 0, 3)).setObjects(("DFM-MIB", "smNotifTimestamp"), ("DFM-MIB", "smNotifServer"), ("DFM-MIB", "smNotifClass"), ("DFM-MIB", "smNotifInstance"), ("DFM-MIB", "smNotifEventName"), ("DFM-MIB", "smNotifInstanceID"), ("DFM-MIB", "smNotifDescription"), ("DFM-MIB", "smNotifCertainty"), ("DFM-MIB", "smNotifSeverity"))
if mibBuilder.loadTexts: smTrapSeverityChange.setStatus('current')
if mibBuilder.loadTexts: smTrapSeverityChange.setDescription('A trap indicating a severity change of a DFM notification. The text in smNotifDescription indicates the nature of the notification.')
smTrapNotificationClear = NotificationType((1, 3, 6, 1, 4, 1, 733, 0, 7)).setObjects(("DFM-MIB", "smNotifTimestamp"), ("DFM-MIB", "smNotifServer"), ("DFM-MIB", "smNotifClass"), ("DFM-MIB", "smNotifInstance"), ("DFM-MIB", "smNotifEventName"), ("DFM-MIB", "smNotifInstanceID"), ("DFM-MIB", "smNotifDescription"), ("DFM-MIB", "smNotifCertainty"), ("DFM-MIB", "smNotifSeverity"))
if mibBuilder.loadTexts: smTrapNotificationClear.setStatus('current')
if mibBuilder.loadTexts: smTrapNotificationClear.setDescription('A trap indicating the clear of a DFM notification.')
mibBuilder.exportSymbols("DFM-MIB", smTrapNotificationClear=smTrapNotificationClear, smNotifClass=smNotifClass, PYSNMP_MODULE_ID=dfmMIB, smTrapNotification=smTrapNotification, smNotifTimestamp=smNotifTimestamp, smNotificationTrap=smNotificationTrap, smNotificationData=smNotificationData, smNotifInstanceID=smNotifInstanceID, smNotifDescription=smNotifDescription, smNotifCertainty=smNotifCertainty, smTrapSeverityChange=smTrapSeverityChange, smNotifEventName=smNotifEventName, smTrapCertaintyChange=smTrapCertaintyChange, smGenericNotify=smGenericNotify, smNotifInstance=smNotifInstance, smNotifSeverity=smNotifSeverity, smNotifServer=smNotifServer, dfmMIB=dfmMIB)