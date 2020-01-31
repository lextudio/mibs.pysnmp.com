#
# PySNMP MIB module CTRON-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-ENTITY-STATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:29:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
EntityStandbyStatus, EntityAlarmStatus, EntityUsageState, EntityOperState, EntityAdminState = mibBuilder.importSymbols("CTRON-ENTITY-STATE-TC-MIB", "EntityStandbyStatus", "EntityAlarmStatus", "EntityUsageState", "EntityOperState", "EntityAdminState")
ctEntityStateMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateMib")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, NotificationType, Integer32, ModuleIdentity, iso, TimeTicks, Unsigned32, ObjectIdentity, Counter32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "iso", "TimeTicks", "Unsigned32", "ObjectIdentity", "Counter32", "Bits", "mib-2", "IpAddress")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ctEntityStateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1))
ctEntityStateMIB.setRevisions(('2005-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ctEntityStateMIB.setRevisionsDescriptions(('Initial version, published as RFC YYYY.',))
if mibBuilder.loadTexts: ctEntityStateMIB.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateMIB.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: ctEntityStateMIB.setContactInfo(' General Discussion: entmib@ietf.org To Subscribe: http://www.ietf.org/mailman/listinfo/entmib http://www.ietf.org/html.charters/entmib-charter.html Sharon Chisholm Nortel Networks PO Box 3511 Station C Ottawa, Ont. K1Y 4H7 Canada schishol@nortelnetworks.com David T. Perkins 548 Qualbrook Ct San Jose, CA 95110 USA Phone: 408 394-8702 dperkins@snmpinfo.com ')
if mibBuilder.loadTexts: ctEntityStateMIB.setDescription('This MIB defines a state extension to the Entity MIB. Copyright (C) The Internet Society 2005. This version of this MIB module is part of RFC yyyy; see the RFC itself for full legal notices.')
ctEntStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1))
ctEntStateTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1), )
if mibBuilder.loadTexts: ctEntStateTable.setStatus('current')
if mibBuilder.loadTexts: ctEntStateTable.setDescription('A table of information about state/status of entities. This is a sparse augment of the entPhysicalTable. Entries appear in this table for values of entPhysicalClass [RFC2737] that in this implementation are able to report any of the state or status stored in this table. ')
ctEntStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ctEntStateEntry.setStatus('current')
if mibBuilder.loadTexts: ctEntStateEntry.setDescription('State information about this physical entity.')
ctEntStateLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateLastChanged.setStatus('current')
if mibBuilder.loadTexts: ctEntStateLastChanged.setDescription('The value of this object is the date and time when the value of any of ctEntStateAdmin, ctEntStateOper, ctEntStateUsage, ctEntStateAlarm, or ctEntStateStandby changed for this entity. If there has been no change since the last re-initialization of the local system, this object contains the date and time of local system initialization. If there has been no change since the entity was added to the local system, this object contains the date and time of the insertion.')
ctEntStateAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEntStateAdmin.setStatus('current')
if mibBuilder.loadTexts: ctEntStateAdmin.setDescription("The administrative state for this entity. This object refers to an entities administrative permission to service both other entities within its containment hierarchy as well other users of its services defined by means outside the scope of this MIB. Setting this object to 'notSupported' will result in an 'inconsistentValue' error. For entities that do not support administrative state, all set operations will result in an 'inconsistentValue' error. Some physical entities exhibit only a subset of the remaining administrative state values. Some entities cannot be locked, and hence this object exhibits only the 'unlocked' state. Other entities can not be shutdown gracefully, and hence this object does not exhibit the 'shuttingDown' state. A value of 'inconsistentValue' will be returned if attempts are made to set this object to values not supported by its administrative model.")
ctEntStateOper = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateOper.setStatus('current')
if mibBuilder.loadTexts: ctEntStateOper.setDescription("The operational state for this entity. Note that unlike the state model used within the Interfaces MIB [RFC2863], this object does not follow the administrative state. An administrative state of down does not predict an operational state of disabled. A value of 'testing' means that entity currently being tested and cannot there fore report whether it is operational or not. A value of 'disabled' means that an entity is totally inoperable and unable to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB. A value of 'enabled' means that an entity is fully or partially operable and able to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB. Note that some implementations may not be able to accurately report ctEntStateOper while the ctEntStateAdmin object has a value other than 'unlocked'. In these cases, this object MUST have a value of 'unknown'.")
ctEntStateUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateUsage.setStatus('current')
if mibBuilder.loadTexts: ctEntStateUsage.setDescription("The usage state for this entity. This object refers to an entity's ability to service more physical entities in a containment hierarchy. A value of 'idle' means this entity is able to contain other entities but that no other entity is currently contained within this entity. A value of 'active' means that at least one entity is contained within this entity, but that it could handle more. A value of 'busy' means that the entity is unable to handle any additional entities being contained in it. Some entities will exhibit only a subset of the usage state values. Entities that are unable to ever service any entities within a containment hierarchy will always have a usage state of 'busy'. Some entities will only ever be able to support one entity within its containment hierarchy and will therefore only exhibit values of 'idle' and 'busy'.")
ctEntStateAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateAlarm.setStatus('current')
if mibBuilder.loadTexts: ctEntStateAlarm.setDescription("The alarm status for this entity. It does not include the alarms raised on child components within its containment hierarchy. A value of 'unknown' means that this entity is unable to report alarm state. Note that this differs from 'indeterminate' which means that that alarm state is supported and there are alarms against this entity, but the severity of some of the alarms is not known If no bits are set, then this entity supports reporting of alarms, but there are currently no active alarms against this entity. ")
ctEntStateStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateStandby.setStatus('current')
if mibBuilder.loadTexts: ctEntStateStandby.setDescription("The standby status for this entity. Some entities will exhibit only a subset of the remaining standby state values. If this entity cannot operate in a standby role, the value of this object will always be 'providingService'.")
ctEntStateNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0))
ctEntStateOperEnabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperEnabled.setStatus('current')
if mibBuilder.loadTexts: ctEntStateOperEnabled.setDescription("An ctEntStateOperEnabled notification signifies that the SNMP entity, acting in an agent role, has detected that the ctEntStateOper object for one of its entities has transitioned into the 'enabled' state. The entity this notification refers can be identified by extracting the entPhysicalIndex from one of the variable bindings. The ctEntStateAdmin and ctEntStateAlarm varbinds may be examined to find out additional information on the administrative state at the time of the operation state change as well to find out whether there were any known alarms against the entity at that time that may explain why the physical entity has become operationally disabled.")
ctEntStateOperDisabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperDisabled.setStatus('current')
if mibBuilder.loadTexts: ctEntStateOperDisabled.setDescription("An ctEntStateOperDisabled notification signifies that the SNMP entity, acting in an agent role, has detected that the ctEntStateOper object for one of its entities has transitioned into the 'disabled' state. The entity this notification refers can be identified by extracting the entPhysicalIndex from one of the variable bindings. The ctEntStateAdmin and ctEntStateAlarm varbinds may be examined to find out additional information on the administrative state at the time of the operation state change as well to find out whether there were any known alarms against the entity at that time that may have affect on the physical entity's ability to stay operationally enabled.")
ctEntStateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2))
ctEntStateCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1))
ctEntStateCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateGroup"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateCompliance = ctEntStateCompliance.setStatus('current')
if mibBuilder.loadTexts: ctEntStateCompliance.setDescription('The compliance statement for systems supporting the Entity State MIB.')
ctEntStateGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2))
ctEntStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateLastChanged"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOper"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateUsage"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateGroup = ctEntStateGroup.setStatus('current')
if mibBuilder.loadTexts: ctEntStateGroup.setDescription('Standard Entity State group.')
ctEntStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateOperEnabled"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateNotificationsGroup = ctEntStateNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ctEntStateNotificationsGroup.setDescription('Standard Entity State Notification group.')
mibBuilder.exportSymbols("CTRON-ENTITY-STATE-MIB", ctEntStateOper=ctEntStateOper, ctEntStateOperEnabled=ctEntStateOperEnabled, ctEntStateStandby=ctEntStateStandby, ctEntStateAlarm=ctEntStateAlarm, ctEntStateOperDisabled=ctEntStateOperDisabled, ctEntStateConformance=ctEntStateConformance, ctEntStateGroups=ctEntStateGroups, ctEntStateEntry=ctEntStateEntry, ctEntityStateMIB=ctEntityStateMIB, PYSNMP_MODULE_ID=ctEntityStateMIB, ctEntStateNotifications=ctEntStateNotifications, ctEntStateCompliance=ctEntStateCompliance, ctEntStateAdmin=ctEntStateAdmin, ctEntStateUsage=ctEntStateUsage, ctEntStateCompliances=ctEntStateCompliances, ctEntStateGroup=ctEntStateGroup, ctEntStateLastChanged=ctEntStateLastChanged, ctEntStateTable=ctEntStateTable, ctEntStateObjects=ctEntStateObjects, ctEntStateNotificationsGroup=ctEntStateNotificationsGroup)