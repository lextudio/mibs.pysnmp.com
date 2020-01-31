#
# PySNMP MIB module CISCO-MAC-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAC-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:06:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, MibIdentifier, IpAddress, Bits, Counter64, ObjectIdentity, Gauge32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "Bits", "Counter64", "ObjectIdentity", "Gauge32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ModuleIdentity")
DisplayString, TruthValue, TimeStamp, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeStamp", "MacAddress", "TextualConvention")
ciscoMacNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 215))
ciscoMacNotificationMIB.setRevisions(('2007-06-11 00:00', '2003-03-21 00:00', '2001-10-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMacNotificationMIB.setRevisionsDescriptions(('Fixed typo and made changes to the description of cmnMACMoveObjects, cmnMACThresholdNotifEnabled and cmnMacThresholdExceedNotif.', 'Added cmnMACMoveObjects, cmnMACThresholdObjects.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMacNotificationMIB.setLastUpdated('200706110000Z')
if mibBuilder.loadTexts: ciscoMacNotificationMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMacNotificationMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wbu@cisco.com')
if mibBuilder.loadTexts: ciscoMacNotificationMIB.setDescription('This MIB module is for configuration of the MAC notification feature. MAC notification is a mechanism to inform monitoring devices when there are MAC addresses learnt or removed from the forwarding database of the monitored devices.')
ciscoMacNotificationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 1))
cmnGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1))
cmnInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2))
cmnMACMoveObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3))
cmnMACThresholdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4))
cmnGlobalFeatureEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnGlobalFeatureEnabled.setStatus('current')
if mibBuilder.loadTexts: cmnGlobalFeatureEnabled.setDescription('Indicates whether the MAC notification feature is currently running in the device. Setting this object to false(2) disables the MAC notification feature globally thus disabling the feature at each interface. Setting this object to true(1) will start the MAC notification feature running in the device. If the feature is already running, setting to true(1) has no effect. Once the MAC notification is enabled, whether the feature is running at each interface is controlled by the cmnIfConfigTable.')
cmnNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnNotificationInterval.setStatus('current')
if mibBuilder.loadTexts: cmnNotificationInterval.setDescription('This object specifies the maximum interval of time between cmnMacChangedNotifications being generated by the device. If the value of cmnNotificationsEnabled is true(1), the device will send out the generated cmnMacChangedNotifications and archive the MAC change notification events in the cmnHistoryTable. If the value of cmnNotificationEnabled is false(2), the device will not send out the generated cmnMacChangedNotifications but it will archive these events in the cmnHistoryTable. If the value of this object is equal to 0, the device will generate cmnMacChangedNotifications and archive the MAC change notification events in the cmnHistoryTable as soon as there is MAC address learnt or removed by the device. If the value of this object is greater than 0, the device will wait for a period of time equal to the value of this object before generate the cmnMacChangedNotifications and archive the MAC change notification events in the cmnHistoryTable.')
cmnMacAddressesLearnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMacAddressesLearnt.setStatus('current')
if mibBuilder.loadTexts: cmnMacAddressesLearnt.setDescription('Indicates the number of MAC addresses learnt by the device.')
cmnMacAddressesRemoved = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMacAddressesRemoved.setStatus('current')
if mibBuilder.loadTexts: cmnMacAddressesRemoved.setDescription('Indicates the number of MAC addresses removed from the forwarding database.')
cmnNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnNotificationsEnabled.setStatus('current')
if mibBuilder.loadTexts: cmnNotificationsEnabled.setDescription("Indicates whether cmnMacChangedNotification notifications will or will not be sent when there are MAC addresses learnt or removed from the device's forwarding database. Disabling notifications does not prevent the MAC address info from being added to the cmnHistoryTable.")
cmnNotificationsSent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnNotificationsSent.setStatus('current')
if mibBuilder.loadTexts: cmnNotificationsSent.setDescription('Indicates the number of cmnMacChangedNotifications sent out by the device.')
cmnHistTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 500)).clone(1)).setUnits('entries').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnHistTableMaxLength.setStatus('current')
if mibBuilder.loadTexts: cmnHistTableMaxLength.setDescription('The upper limit on the number of entries that the cmnHistoryTable may contain. A value of 0 will prevent any history from being retained. When this table is full, the oldest entry will be deleted and a new one will be created.')
cmnHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8), )
if mibBuilder.loadTexts: cmnHistoryTable.setStatus('current')
if mibBuilder.loadTexts: cmnHistoryTable.setDescription('This table will archive the MAC change notification events generated by this device. The MAC change notification events are archived here even if cmnMacChangesNotifications are not actually sent.')
cmnHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1), ).setIndexNames((0, "CISCO-MAC-NOTIFICATION-MIB", "cmnHistIndex"))
if mibBuilder.loadTexts: cmnHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: cmnHistoryEntry.setDescription('A MAC change notification message that was previously generated by this device. Each entry is indexed by a message index.')
cmnHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cmnHistIndex.setStatus('current')
if mibBuilder.loadTexts: cmnHistIndex.setDescription('An index that uniquely identifies a MAC change notification event previously generated by the device. This index starts at 1 and increases by one when a MAC change notification is generated. When it reaches the maximum value, the agent wraps the value back to 1.')
cmnHistMacChangedMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnHistMacChangedMsg.setStatus('current')
if mibBuilder.loadTexts: cmnHistMacChangedMsg.setDescription("This object contains the information of a MAC change notification event. It consists of several tuples packed together in the format of '<tuple1><tuple2>...'. Each tuple consist of 11 octets in the format of '<operation><VLAN><MAC><dot1dBasePort>' where <operation> is of size 1 octet and supports the following values 0 - End of MIB object. 1 - MAC learnt. 2 - MAC removed. <VLAN> is VLAN number of the VLAN which the MAC address is belonged to and has size of 2 octet. <MAC> is the Layer2 Mac Address and has size of 6 octets. <dot1dBasePort> is the value of dot1dBasePort for the interface from which the MAC address is learnt and has size of 2 octets.")
cmnHistTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnHistTimestamp.setStatus('current')
if mibBuilder.loadTexts: cmnHistTimestamp.setDescription('The value of sysUpTime when the cmnMacChangedNotification containing the information denoted by the cmnHistMacChangedMsg object in this entry was generated.')
cmnIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1), )
if mibBuilder.loadTexts: cmnIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: cmnIfConfigTable.setDescription('This table enables or disables the generation of notification at each interface when MAC address is learnt or removed.')
cmnIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmnIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cmnIfConfigEntry.setDescription('Each entry contains the configuration for enabling the MAC notification at each interface that supports this feature.')
cmnMacAddrLearntEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMacAddrLearntEnable.setStatus('current')
if mibBuilder.loadTexts: cmnMacAddrLearntEnable.setDescription('Indicates whether this interface is enabled to send cmnMacChangedNotification when it learns a new MAC address. This variable has no effect when the value of cmnGlobalFeatureEnabled object is false(2). Setting this object to true(1) enables the sending of cmnMacChangedNotification when this interface learns a new MAC address. Setting this object to false(2) disables the sending of cmnMacChangedNotification when this interface learns a new MAC address.')
cmnMacAddrRemovedEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMacAddrRemovedEnable.setStatus('current')
if mibBuilder.loadTexts: cmnMacAddrRemovedEnable.setDescription('Indicates whether this interface is enabled to send cmnMacChangedNotification when a MAC address which it learnt previously is removed from the forwarding table. This variable has no effect when the value of cmnGlobalFeatureEnabled object is false(2). Setting this object to true(1) enables the sending of cmnMacChangedNotification when a MAC address which this interface learnt previously is removed from the forwarding table. Setting this object to false(2) disables the sending of cmnMacChangedNotification when a MAC address which this interface learnt previously is removed from the forwarding table.')
cmnMACMoveFeatureEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMACMoveFeatureEnabled.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveFeatureEnabled.setDescription('Specifies whether the MAC Move notification feature is currently running in the device. Setting this object to false(2) disables the MAC Move notification feature globally. Setting this object to true(1) will start the MAC Move notification feature running in the device.')
cmnMACMoveNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMACMoveNotificationsEnabled.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveNotificationsEnabled.setDescription('Specifies whether cmnMacMoveNotification notifications will or will not be sent when a MAC move is detected by the MAC move notification feature. Setting this object to false(2) will not send the cmnMacMoveNotification notifications. Setting this object to true(1) will send the cmnMacMoveNotification notifications.')
cmnMACMoveAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMACMoveAddress.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveAddress.setDescription('Indicates the MAC address that is moved between cmnMACMoveFromPortId and cmnMACMoveToPortId on cmnMACMoveVlanNumber. This object is instantiated only when cmnMACMoveFeatureEnabled value is set to true(1) and a MAC move is detected by the MAC move notification feature.')
cmnMACMoveVlanNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 4), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMACMoveVlanNumber.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveVlanNumber.setDescription('Indicates the VLAN on which the cmnMACMoveAddress is moved from cmnMACMoveFromPortId to cmnMACMoveToPortId. This object is instantiated only when cmnMACMoveFeatureEnabled value is set to true(1) and a MAC move is detected by the MAC move notification feature.')
cmnMACMoveFromPortId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMACMoveFromPortId.setReference('dot1dBasePort is defined in RFC1493.')
if mibBuilder.loadTexts: cmnMACMoveFromPortId.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveFromPortId.setDescription('The value of dot1dBasePort for the bridge port from which the cmnMACMoveAddress is moved to cmnMACMoveToPortId on cmnMACMoveVlanNumber. This object is instantiated only when cmnMACMoveFeatureEnabled value is set to true(1) and a MAC move is detected by the MAC move notification feature.')
cmnMACMoveToPortId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMACMoveToPortId.setReference('dot1dBasePort is defined in RFC1493.')
if mibBuilder.loadTexts: cmnMACMoveToPortId.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveToPortId.setDescription('The value of dot1dBasePort for the bridge port to which the cmnMACMoveAddress is moved from cmnMACMoveFromPortId on cmnMACMoveVlanNumber. This object is instantiated only when cmnMACMoveFeatureEnabled value is set to true(1) and a MAC move is detected by the MAC move notification feature.')
cmnMACMoveTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnMACMoveTime.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveTime.setDescription('The value of sysUpTime when a cmnMACMoveAddress is moved between cmnMACMoveFromPortId and cmnMACMACMoveToPortId. This object is instantiated only when cmnMACMoveFeatureEnabled value is set to true(1) and a MAC move is detected by the MAC move notification feature.')
cmnMACThresholdFeatureEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMACThresholdFeatureEnabled.setStatus('current')
if mibBuilder.loadTexts: cmnMACThresholdFeatureEnabled.setDescription('Specifies whether the MAC Threshold notification feature is currently running in the device. Setting this object to false(2) disables the MAC Threshold notification feature globally. Setting this object to true(1) will start the MAC Threshold notification feature running in the device.')
cmnMACThresholdLimit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 2), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMACThresholdLimit.setStatus('current')
if mibBuilder.loadTexts: cmnMACThresholdLimit.setDescription('Indicate the threshold limit of the forwarding table utilization.')
cmnMACThresholdInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 3), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMACThresholdInterval.setStatus('current')
if mibBuilder.loadTexts: cmnMACThresholdInterval.setDescription('Interval at which forwarding table utilization is compared against cmnMACThresholdLimit.')
cmnMACThresholdNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmnMACThresholdNotifEnabled.setStatus('current')
if mibBuilder.loadTexts: cmnMACThresholdNotifEnabled.setDescription('Specifies whether cmnMacThresholdExceedNotif notifications will or will not be sent when the forwarding table utilization exceeds or equals to cmnMACThresholdLimit value. cmnMacThresholdExceedNotif notification is not sent when cmnMACThresholdLimit is set to zero.')
cmnUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5), )
if mibBuilder.loadTexts: cmnUtilizationTable.setStatus('current')
if mibBuilder.loadTexts: cmnUtilizationTable.setDescription('cmnUtilizationTable specifies the forwarding table utilization information. This table is instantiated only when cmnMACThresholdFeatureEnabled value is set to true(1). Entries in this table are updated at the end of every cmnMACThresholdInterval.')
cmnUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cmnUtilizationEntry.setStatus('current')
if mibBuilder.loadTexts: cmnUtilizationEntry.setDescription('A conceptual row containing forwarding table utilization maintained by switching engine (identified by entPhysicalIndex). Each switching engine managed by this MIB module can have at least one entry in this table.')
cmnUtilizationEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnUtilizationEntries.setStatus('current')
if mibBuilder.loadTexts: cmnUtilizationEntries.setDescription('Indicates the number of entries present in the forwarding table for the given entPhysicalIndex calculated at the end of cmnMACThresholdInterval.')
cmnUtilizationUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnUtilizationUtilization.setStatus('current')
if mibBuilder.loadTexts: cmnUtilizationUtilization.setDescription('Indicates the utilization of the forwarding table for the given entPhysicalIndex calculated at the end of cmnMACThresholdInterval.')
cmnUtilizationTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmnUtilizationTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cmnUtilizationTimeStamp.setDescription('Indicates the sysUptime at which the cmnUtilizationUtilization is updated.')
cmnMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 2))
cmnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0))
cmnMacChangedNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0, 1)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnHistMacChangedMsg"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistTimestamp"))
if mibBuilder.loadTexts: cmnMacChangedNotification.setStatus('current')
if mibBuilder.loadTexts: cmnMacChangedNotification.setDescription('This notification is generated when there is enough MAC address information to fully occupy a maximum size SNMP trap message. This notification is also generated when there is at least one MAC address changed or removed and the amount of time elapsed from the previous notification is greater than the maximum wait time denoted by cmnNotificationInterval object. If there are more MAC addresses information than can fit into one cmmHistTrapContent object, then multiple notifications will be generated.')
cmnMacMoveNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0, 2)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveAddress"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveVlanNumber"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveFromPortId"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveToPortId"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveTime"))
if mibBuilder.loadTexts: cmnMacMoveNotification.setStatus('current')
if mibBuilder.loadTexts: cmnMacMoveNotification.setDescription('cmnMacMoveNotification is generated when a MAC address is moved between two interfaces.')
cmnMacThresholdExceedNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0, 3)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationUtilization"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdLimit"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationTimeStamp"))
if mibBuilder.loadTexts: cmnMacThresholdExceedNotif.setStatus('current')
if mibBuilder.loadTexts: cmnMacThresholdExceedNotif.setDescription('cmnMacThresholdExceedNotif is sent when cmnUtilizationUtilization exceeds or equals to the cmnMACThresholdLimit for a given entPhysicalIndex. cmnMacThresholdExceedNotif is not sent when cmnMACThresholdLimit is set to zero')
cmnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 3))
cmnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 1))
cmnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2))
cmnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 1, 1)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnGlobalGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnInterfaceGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnMIBCompliance = cmnMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cmnMIBCompliance.setDescription('The compliance statement for the CISCO-MAC-NOTIFICATION-MIB.')
cmnMIBComplianceVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 1, 2)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnGlobalGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnInterfaceGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveNotifGroup"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnMIBComplianceVer1 = cmnMIBComplianceVer1.setStatus('current')
if mibBuilder.loadTexts: cmnMIBComplianceVer1.setDescription('The compliance statement for the CISCO-MAC-NOTIFICATION-MIB.')
cmnGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 1)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnGlobalFeatureEnabled"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationInterval"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddressesLearnt"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddressesRemoved"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationsEnabled"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistTableMaxLength"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistMacChangedMsg"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistTimestamp"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnGlobalGroup = cmnGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: cmnGlobalGroup.setDescription('A collection of objects providing the global configuration and information for MAC notification.')
cmnInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 2)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddrLearntEnable"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddrRemovedEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnInterfaceGroup = cmnInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: cmnInterfaceGroup.setDescription('A collection of objects providing the configuration information for MAC notification at each interface.')
cmnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 3)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMacChangedNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnNotificationGroup = cmnNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cmnNotificationGroup.setDescription('The notification generated by the CISCO-MAC-NOTIFICATION-MIB.')
cmnMACMoveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 5)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveFeatureEnabled"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveNotificationsEnabled"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveAddress"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveVlanNumber"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveFromPortId"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveToPortId"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnMACMoveGroup = cmnMACMoveGroup.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveGroup.setDescription('A collection of objects providing the global configuration and information for MAC Move notification feature.')
cmnMACThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 6)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdFeatureEnabled"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdLimit"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdInterval"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdNotifEnabled"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationEntries"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationUtilization"), ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnMACThresholdGroup = cmnMACThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: cmnMACThresholdGroup.setDescription('A collection of objects providing the global configuration and information for MAC Threshold notification feature.')
cmnMACMoveNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 7)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMacMoveNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnMACMoveNotifGroup = cmnMACMoveNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cmnMACMoveNotifGroup.setDescription('A collection of objects providing the notification information for MAC Move notification feature.')
cmnMACThresholdNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 8)).setObjects(("CISCO-MAC-NOTIFICATION-MIB", "cmnMacThresholdExceedNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnMACThresholdNotifGroup = cmnMACThresholdNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cmnMACThresholdNotifGroup.setDescription('A collection of objects providing the notification information for MAC Threshold notification feature.')
mibBuilder.exportSymbols("CISCO-MAC-NOTIFICATION-MIB", cmnMACMoveVlanNumber=cmnMACMoveVlanNumber, cmnHistoryTable=cmnHistoryTable, cmnInterfaceGroup=cmnInterfaceGroup, cmnGlobalGroup=cmnGlobalGroup, cmnMacChangedNotification=cmnMacChangedNotification, cmnMIBCompliances=cmnMIBCompliances, cmnNotificationsEnabled=cmnNotificationsEnabled, cmnMacAddrRemovedEnable=cmnMacAddrRemovedEnable, cmnGlobalObjects=cmnGlobalObjects, cmnMIBConformance=cmnMIBConformance, cmnHistTableMaxLength=cmnHistTableMaxLength, cmnMacAddressesRemoved=cmnMacAddressesRemoved, cmnInterfaceObjects=cmnInterfaceObjects, cmnMACMoveGroup=cmnMACMoveGroup, cmnGlobalFeatureEnabled=cmnGlobalFeatureEnabled, cmnUtilizationTable=cmnUtilizationTable, cmnMACMoveFeatureEnabled=cmnMACMoveFeatureEnabled, cmnMACThresholdInterval=cmnMACThresholdInterval, cmnMIBCompliance=cmnMIBCompliance, cmnMacAddressesLearnt=cmnMacAddressesLearnt, cmnMACThresholdFeatureEnabled=cmnMACThresholdFeatureEnabled, ciscoMacNotificationMIBObjects=ciscoMacNotificationMIBObjects, cmnMACThresholdObjects=cmnMACThresholdObjects, cmnMACMoveToPortId=cmnMACMoveToPortId, cmnMACMoveAddress=cmnMACMoveAddress, cmnMIBGroups=cmnMIBGroups, cmnMACThresholdLimit=cmnMACThresholdLimit, cmnNotificationGroup=cmnNotificationGroup, cmnIfConfigTable=cmnIfConfigTable, cmnUtilizationTimeStamp=cmnUtilizationTimeStamp, cmnMACThresholdGroup=cmnMACThresholdGroup, cmnMACMoveNotifGroup=cmnMACMoveNotifGroup, cmnUtilizationEntry=cmnUtilizationEntry, cmnUtilizationUtilization=cmnUtilizationUtilization, cmnMIBNotifications=cmnMIBNotifications, cmnMACThresholdNotifGroup=cmnMACThresholdNotifGroup, cmnMACMoveObjects=cmnMACMoveObjects, PYSNMP_MODULE_ID=ciscoMacNotificationMIB, cmnMacMoveNotification=cmnMacMoveNotification, cmnIfConfigEntry=cmnIfConfigEntry, cmnHistTimestamp=cmnHistTimestamp, cmnHistMacChangedMsg=cmnHistMacChangedMsg, cmnMACMoveNotificationsEnabled=cmnMACMoveNotificationsEnabled, cmnMACMoveTime=cmnMACMoveTime, cmnMACThresholdNotifEnabled=cmnMACThresholdNotifEnabled, cmnUtilizationEntries=cmnUtilizationEntries, ciscoMacNotificationMIB=ciscoMacNotificationMIB, cmnMIBNotificationPrefix=cmnMIBNotificationPrefix, cmnNotificationInterval=cmnNotificationInterval, cmnMIBComplianceVer1=cmnMIBComplianceVer1, cmnNotificationsSent=cmnNotificationsSent, cmnMacThresholdExceedNotif=cmnMacThresholdExceedNotif, cmnHistoryEntry=cmnHistoryEntry, cmnHistIndex=cmnHistIndex, cmnMACMoveFromPortId=cmnMACMoveFromPortId, cmnMacAddrLearntEnable=cmnMacAddrLearntEnable)