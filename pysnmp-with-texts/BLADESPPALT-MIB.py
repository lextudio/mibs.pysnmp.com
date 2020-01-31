#
# PySNMP MIB module BLADESPPALT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLADESPPALT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Bits, enterprises, Gauge32, ModuleIdentity, Integer32, TimeTicks, NotificationType, NotificationType, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Bits", "enterprises", "Gauge32", "ModuleIdentity", "Integer32", "TimeTicks", "NotificationType", "NotificationType", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
supportProcessor = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158))
mmRemoteSupTrapMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158, 3))
remoteSupTrapMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1))
spTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1))
spTrapDateTime = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapDateTime.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapDateTime.setDescription('Timestamp of Local Date and Time when alert was generated')
spTrapAppId = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapAppId.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapAppId.setDescription("Application ID, always 'BladeCenter Management Module'")
spTrapSpTxtId = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapSpTxtId.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapSpTxtId.setDescription('SP System Identification - Text Identification')
spTrapSysUuid = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapSysUuid.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapSysUuid.setDescription('Host System UUID(Universal Unique ID)')
spTrapSysSern = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapSysSern.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapSysSern.setDescription('Host System Serial Number')
spTrapAppType = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapAppType.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapAppType.setDescription('Application Alert Type - Event Number ID')
spTrapPriority = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapPriority.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapPriority.setDescription('Alert Severity Value - Critical Alert(0) - Non-Critical Alert(2) - System Alert(4) - Recovery Alert(8) - Informational Only Alert(255)')
spTrapMsgText = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapMsgText.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapMsgText.setDescription('Alert Message Text')
spTrapHostContact = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapHostContact.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapHostContact.setDescription('Host Contact')
spTrapHostLocation = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapHostLocation.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapHostLocation.setDescription('Host Location')
spTrapBladeName = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapBladeName.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapBladeName.setDescription('Blade Name')
spTrapBladeSern = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapBladeSern.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapBladeSern.setDescription('Blade Serial Number')
spTrapBladeUuid = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spTrapBladeUuid.setStatus('mandatory')
if mibBuilder.loadTexts: spTrapBladeUuid.setDescription('Blade UUID(Universal Unique ID)')
mmTrapTempC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,0)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapTempC.setDescription('Critical Alert: Temperature threshold exceeded.')
mmTrapVoltC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,1)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapVoltC.setDescription('Critical Alert: Voltage threshold exceeded.')
mmTrapTampC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,2)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapTampC.setDescription('Critical Alert: Physical intrusion of system has occurred.')
mmTrapMffC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,3)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapMffC.setDescription('Critical Alert: Multiple fan failure.')
mmTrapPsC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,4)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapPsC.setDescription('Critical Alert: Power supply failure.')
mTrapHdC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,5)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mTrapHdC.setDescription('Critical Alert: Hard disk drive failure.')
mmTrapVrmC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,6)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapVrmC.setDescription('Critical Alert: Voltage Regulator Module(VRM) failure.')
mmTrapSffC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,11)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapSffC.setDescription('Critical Alert: Single Fan failure.')
mmTrapMsC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,31)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapMsC.setDescription('Critical Alert: Multiple switch module failure.')
mmTrapIhcC = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,36)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapIhcC.setDescription('Critical Alert: Incompatible hardware configuration.')
mmTrapRdpsN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,10)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapRdpsN.setDescription('Non-Critical Alert: Redundant Power Supply failure.')
mmTrapTempN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,12)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapTempN.setDescription('Non-Critical Alert: Temperature threshold exceeded.')
mmTrapVoltN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,13)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapVoltN.setDescription('Non-Critical Alert: Voltage threshold exceeded.')
mmTrapRmN = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,32)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapRmN.setDescription('Non-Critical Alert: Redundant module.')
mmTrapSecDvS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,15)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapSecDvS.setDescription('System Alert: Secondary Device warning.')
mmTrapPostToS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,20)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapPostToS.setDescription('System Alert: Post Timeout value exceeded.')
mmTrapOsToS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,21)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapOsToS.setDescription('System Alert: OS Timeout value exceeded.')
mmTrapAppS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,22)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapAppS.setDescription('System Alert: Application Alert.')
mmTrapPoffS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,23)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapPoffS.setDescription('System Alert: Power Off.')
mmTrapPonS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,24)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapPonS.setDescription('System Alert: Power On.')
mmTrapBootS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,25)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapBootS.setDescription('System Alert: System Boot Failure.')
mmTrapLdrToS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,26)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapLdrToS.setDescription('System Alert: OS Loader Timeout.')
mmTrapPFAS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,27)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapPFAS.setDescription('System Alert: Predictive Failure Analysis(PFA) information.')
mmTrapKVMSwitchS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,33)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapKVMSwitchS.setDescription('System Alert: Keyboard/Video/Mouse(KVM) or Medial Tray(MT) switching failure.')
mmTrapSysInvS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,34)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapSysInvS.setDescription('System Alert: Inventory.')
mmTrapSysLogS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,35)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapSysLogS.setDescription('System Alert: System Log 75% full.')
mmTrapNwChangeS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,37)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapNwChangeS.setDescription('System Alert: Network change notification.')
mmTrapBlThrS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,39)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapBlThrS.setDescription('System Alert: Blade Throttle')
mmTrapPwrMgntS = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 158, 3) + (0,40)).setObjects(("BLADESPPALT-MIB", "spTrapDateTime"), ("BLADESPPALT-MIB", "spTrapAppId"), ("BLADESPPALT-MIB", "spTrapSpTxtId"), ("BLADESPPALT-MIB", "spTrapSysUuid"), ("BLADESPPALT-MIB", "spTrapSysSern"), ("BLADESPPALT-MIB", "spTrapAppType"), ("BLADESPPALT-MIB", "spTrapPriority"), ("BLADESPPALT-MIB", "spTrapMsgText"), ("BLADESPPALT-MIB", "spTrapHostContact"), ("BLADESPPALT-MIB", "spTrapHostLocation"), ("BLADESPPALT-MIB", "spTrapBladeName"), ("BLADESPPALT-MIB", "spTrapBladeSern"), ("BLADESPPALT-MIB", "spTrapBladeUuid"))
if mibBuilder.loadTexts: mmTrapPwrMgntS.setDescription('System Alert: Power Management')
mibBuilder.exportSymbols("BLADESPPALT-MIB", spTrapHostContact=spTrapHostContact, mmTrapVrmC=mmTrapVrmC, mmTrapOsToS=mmTrapOsToS, mmTrapPostToS=mmTrapPostToS, mmTrapSysInvS=mmTrapSysInvS, mmTrapNwChangeS=mmTrapNwChangeS, mmTrapTempN=mmTrapTempN, mmTrapKVMSwitchS=mmTrapKVMSwitchS, mmRemoteSupTrapMIB=mmRemoteSupTrapMIB, mmTrapVoltN=mmTrapVoltN, spTrapInfo=spTrapInfo, spTrapSpTxtId=spTrapSpTxtId, mmTrapBlThrS=mmTrapBlThrS, mmTrapBootS=mmTrapBootS, remoteSupTrapMibObjects=remoteSupTrapMibObjects, mmTrapLdrToS=mmTrapLdrToS, spTrapSysSern=spTrapSysSern, spTrapHostLocation=spTrapHostLocation, supportProcessor=supportProcessor, mmTrapTempC=mmTrapTempC, mmTrapAppS=mmTrapAppS, spTrapAppType=spTrapAppType, mmTrapMsC=mmTrapMsC, mmTrapRmN=mmTrapRmN, spTrapAppId=spTrapAppId, mmTrapSecDvS=mmTrapSecDvS, ibm=ibm, mmTrapPFAS=mmTrapPFAS, mmTrapRdpsN=mmTrapRdpsN, mmTrapSffC=mmTrapSffC, ibmProd=ibmProd, spTrapMsgText=spTrapMsgText, mmTrapPonS=mmTrapPonS, mmTrapIhcC=mmTrapIhcC, mmTrapPoffS=mmTrapPoffS, spTrapBladeName=spTrapBladeName, spTrapDateTime=spTrapDateTime, mmTrapPwrMgntS=mmTrapPwrMgntS, mmTrapTampC=mmTrapTampC, mmTrapSysLogS=mmTrapSysLogS, mmTrapPsC=mmTrapPsC, mmTrapVoltC=mmTrapVoltC, spTrapPriority=spTrapPriority, mTrapHdC=mTrapHdC, spTrapBladeSern=spTrapBladeSern, spTrapBladeUuid=spTrapBladeUuid, spTrapSysUuid=spTrapSysUuid, mmTrapMffC=mmTrapMffC)