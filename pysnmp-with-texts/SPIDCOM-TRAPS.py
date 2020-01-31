#
# PySNMP MIB module SPIDCOM-TRAPS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPIDCOM-TRAPS
# Produced by pysmi-0.3.4 at Wed May  1 15:10:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Integer32, Counter32, iso, IpAddress, NotificationType, MibIdentifier, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Counter32", "iso", "IpAddress", "NotificationType", "MibIdentifier", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Unsigned32", "Gauge32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
plcBasePortIndex, = mibBuilder.importSymbols("SPC200", "plcBasePortIndex")
ItuAlarmType, neAlarmActivePhoto, ItuAlarmProbableCause = mibBuilder.importSymbols("SPIDCOM-ALARM-MIB", "ItuAlarmType", "neAlarmActivePhoto", "ItuAlarmProbableCause")
specificSpidcomTrap, = mibBuilder.importSymbols("SPIDCOM-NOTIFICATION-MIB", "specificSpidcomTrap")
trapsDefinition = ModuleIdentity((1, 3, 6, 1, 4, 1, 22764, 4, 1))
if mibBuilder.loadTexts: trapsDefinition.setLastUpdated('200207151330Z')
if mibBuilder.loadTexts: trapsDefinition.setOrganization('SPiDCOM')
if mibBuilder.loadTexts: trapsDefinition.setContactInfo(' TO BE SPECIFIED BY SPiDCOM ')
if mibBuilder.loadTexts: trapsDefinition.setDescription('Definition of the MIB tree structure to manage the Alarm Monitoring.')
deviceDown = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 1))
if mibBuilder.loadTexts: deviceDown.setStatus('current')
if mibBuilder.loadTexts: deviceDown.setDescription('This trap is sent when a the connection with a distant node is down')
deviceUp = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 2))
if mibBuilder.loadTexts: deviceUp.setStatus('current')
if mibBuilder.loadTexts: deviceUp.setDescription('This trap is sent when a the connection with a distant node is down')
maxAttenuation = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 3))
if mibBuilder.loadTexts: maxAttenuation.setStatus('current')
if mibBuilder.loadTexts: maxAttenuation.setDescription('This trap is sent when some value is reached for attenuation')
maxNoise = NotificationType((1, 3, 6, 1, 4, 1, 22764, 4, 1, 4))
if mibBuilder.loadTexts: maxNoise.setStatus('current')
if mibBuilder.loadTexts: maxNoise.setDescription('This trap is sent when some value is reached for noise')
linkUpDownNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22764, 4, 1, 11)).setObjects(("SPIDCOM-TRAPS", "deviceUp"), ("SPIDCOM-TRAPS", "deviceDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linkUpDownNotificationsGroup = linkUpDownNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: linkUpDownNotificationsGroup.setDescription('The notifications which indicates connection with a distant node is up/down')
maxAttenuationNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22764, 4, 1, 12)).setObjects(("SPIDCOM-TRAPS", "maxAttenuation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxAttenuationNotificationsGroup = maxAttenuationNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: maxAttenuationNotificationsGroup.setDescription('The notification which indicates attenuation change')
maxNoiseNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22764, 4, 1, 13)).setObjects(("SPIDCOM-TRAPS", "maxNoise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxNoiseNotificationsGroup = maxNoiseNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: maxNoiseNotificationsGroup.setDescription('The notification which indicates noise change')
mibBuilder.exportSymbols("SPIDCOM-TRAPS", deviceDown=deviceDown, maxNoiseNotificationsGroup=maxNoiseNotificationsGroup, deviceUp=deviceUp, maxAttenuation=maxAttenuation, maxNoise=maxNoise, linkUpDownNotificationsGroup=linkUpDownNotificationsGroup, trapsDefinition=trapsDefinition, PYSNMP_MODULE_ID=trapsDefinition, maxAttenuationNotificationsGroup=maxAttenuationNotificationsGroup)