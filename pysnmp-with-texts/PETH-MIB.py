#
# PySNMP MIB module PETH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PETH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:40:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
dot3, = mibBuilder.importSymbols("EtherLike-MIB", "dot3")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, IpAddress, Counter64, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, MibIdentifier, Unsigned32, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "Counter64", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "MibIdentifier", "Unsigned32", "Bits", "iso", "Gauge32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 7, 20))
if mibBuilder.loadTexts: powerEthernetMIB.setLastUpdated('200106200000Z')
if mibBuilder.loadTexts: powerEthernetMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
if mibBuilder.loadTexts: powerEthernetMIB.setContactInfo(' Chair: Dan Romascanu Avaya Inc. Tel: +972-3-645-8414 Email: dromasca@avaya.com Editor: Avi Berger PowerDsine Inc. Tel: 972-9-7755100 Ext 307 Fax: 972-9-7755120 E-mail: avib@PowerDsine.com ')
if mibBuilder.loadTexts: powerEthernetMIB.setDescription('The MIB module for for managing Powered Devices (PD) or Power Source Equipment (PSE) working according to the IEEE 802.af Powere Ethernet (DTE Power via MDI) standard.')
pethObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 1))
pethNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 2))
pethConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 3))
pethPsePortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1), )
if mibBuilder.loadTexts: pethPsePortTable.setStatus('current')
if mibBuilder.loadTexts: pethPsePortTable.setDescription('A table of objects that display and control the power characteristics power Ethernet ports on a Power Source Entity (PSE) device. This group will be implemented in managed power Ethernet switches and mid-span devices.')
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1), ).setIndexNames((0, "PETH-MIB", "pethPsePortGroupIndex"), (0, "PETH-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: pethPsePortEntry.setStatus('current')
if mibBuilder.loadTexts: pethPsePortEntry.setDescription('A set of objects that display and control the power characteristics of a power Ethernet PSE port.')
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortGroupIndex.setStatus('current')
if mibBuilder.loadTexts: pethPsePortGroupIndex.setDescription('This variable uniquely identifies the group containing the port to which power Ethernet PSE is connected. Group means a box in the stack, or a module in a rack. For non-modular devices the value 1 is recommended.')
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortIndex.setStatus('current')
if mibBuilder.loadTexts: pethPsePortIndex.setDescription('This variable uniquely identifies the power Ethernet PSE port within group pethPseGroupIndex to which the power Ethernet PSE entry is connected.')
pethPsePortPowerEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerEnable.setStatus('current')
if mibBuilder.loadTexts: pethPsePortPowerEnable.setDescription('Enables power supply on this port. Setting this object at a value auto(1) enables power and detection mechanism for this port. Setting this object at a value off(2) disables power and detection mechanism for this port.')
pethPsePortPowerIdPairsControl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerIdPairsControl.setStatus('current')
if mibBuilder.loadTexts: pethPsePortPowerIdPairsControl.setDescription('Describes the capability of controlling the power pairs functionality to switch pins for sourcing power.')
pethPsePortPowerIdPairs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("signal", 1), ("spare", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerIdPairs.setStatus('current')
if mibBuilder.loadTexts: pethPsePortPowerIdPairs.setDescription('Describes or controls the pairs in use. If the value of pethPsePortPowerIdpairsControl is true, thisobject is writable. A value of signal(1) menas that the signal pairs only are in use. A value of spare(2) means that the spare pairs only are in use. A value of both(3) means that both the signal and the spare pairs are in use.')
pethPsePortPowerDetectionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("off", 2), ("test", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerDetectionStatus.setStatus('current')
if mibBuilder.loadTexts: pethPsePortPowerDetectionStatus.setDescription('Controls the power detection mechanism of the port. Setting the value auto(1) enables the power detection mechanism of the port. Setting the value off(2) disables the power detection mechanism of the port. Setting the value test(3) puts the port in a test mode forcing continuous discovery without applying power regardless of whether PD detected.')
pethPsePortDetectionOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("deliveringPower", 1), ("off", 2), ("searching", 3), ("fault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDetectionOperStatus.setStatus('current')
if mibBuilder.loadTexts: pethPsePortDetectionOperStatus.setDescription('Describes the operational status of the port detection. A value of deliveringPower(1) indicates that the port executed the detection algorithm, found a PD connection and is currently delivering power. A value of off(2) indicates that the port did not find a PD connection and is not in serching mode. A value of searching(3) indicates that the detection algorithm is in work, and did not detect a valid PD. No power is currently provided. A value of fault(4) indicates that a fault was detected on the port . ')
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPriority.setStatus('current')
if mibBuilder.loadTexts: pethPsePortPowerPriority.setDescription('This object controls the priority of the port from the point of view of a power management algorithm. The priority that is set by this variable could be used by a control mechanism that prevents over current situations by disconnecting first ports with lower power priority. Ports that connect devices critical to the operation of the network - like the E911 telephones ports - should be set to higher priority.')
pethPsePortDenyError = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("lowPriority", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDenyError.setStatus('current')
if mibBuilder.loadTexts: pethPsePortDenyError.setDescription('This object describes an error resulted from an action of the power management mechanism. The value lowPriority(2) indicates that the port was disabled by the power management system, in order to keep active higher priority ports.')
pethPsePortStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 1), ("underCurrent", 2), ("overCurrent", 3), ("both", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortStatus.setStatus('current')
if mibBuilder.loadTexts: pethPsePortStatus.setDescription('Describes a current port status related to the power generation The value underCurrent(2) indicates that the port current is below the minimal value. The value overCurrent(3) indicates that the port current exceeds the maximal value. The value both(4) indicates that both underCurrent and overCurrent status happend from the lase Clear.')
pethPsePortStatusClear = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortStatusClear.setStatus('current')
if mibBuilder.loadTexts: pethPsePortStatusClear.setDescription('Setting the value of this object to clear(1) clears the value of the pethPsePortStatus to none(1).')
pethPsePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("telephone", 2), ("webcam", 3), ("wireless", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortType.setStatus('current')
if mibBuilder.loadTexts: pethPsePortType.setDescription('A manager will set the value of this variable to a value that indicates the type of the device that is connected to theport. This value can be the result of the mapping the address of the station connected to the port and of the value of the pethPdPortType of the respective PD port.')
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5), ("class5", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setStatus('current')
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setDescription('Classification is a way to tag different terminals on the power over LAN network according to their power consumption. Devices such as IP telephones, WLAN access points and others, will be classified according to their power requirements. Class Usage Maximum Power 0 Default 0.5 - 15.0 W 1 Optional 0.5 - 4.0 W 2 Optional 4.0 - 7.0 W 3 Optional 7.0 - 15.0 W 4 Optional Future Use 5 Optional Future Use ')
pethPdPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 2), )
if mibBuilder.loadTexts: pethPdPortTable.setStatus('current')
if mibBuilder.loadTexts: pethPdPortTable.setDescription('A table of objects that display and control the power characteristics power Ethernet ports on a Powered Device(PD) device. This group will be implemented in managed powered and mid-span devices.')
pethPdPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 2, 1), ).setIndexNames((0, "PETH-MIB", "pethPdPortIndex"))
if mibBuilder.loadTexts: pethPdPortEntry.setStatus('current')
if mibBuilder.loadTexts: pethPdPortEntry.setDescription('A set of objects that display and control the power characteristics of a Powered Device port.')
pethPdPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: pethPdPortIndex.setStatus('current')
if mibBuilder.loadTexts: pethPdPortIndex.setDescription('An index value that uniquely identifies an interface to a PD device. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex. The mapping between the ifIndex values and the numbering of the port on the device is an implementation issue.')
pethPdPortPowerPairs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("signal", 1), ("spare", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPdPortPowerPairs.setStatus('current')
if mibBuilder.loadTexts: pethPdPortPowerPairs.setDescription('Describes the pairs in use. A value of signal(1) menas that the signal pairs only are in use. A value of spare(2) means that the spare pairs only are in use. A value of both(3) means that both the signal and the spare pairs are inuse.')
pethPdPortDetectionOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("receivingPower", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPdPortDetectionOperStatus.setStatus('current')
if mibBuilder.loadTexts: pethPdPortDetectionOperStatus.setDescription('Describes the operational status of the port detection. The value off(1) means that the port does not receive power and the detection algorithm might still be operating. The value receivingPower(2) means that the port is receiving power. ')
pethPdPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("telephone", 2), ("webcam", 3), ("wireless", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPdPortType.setStatus('current')
if mibBuilder.loadTexts: pethPdPortType.setDescription('The type of the device. A management application may read the value of this variable and use it for setting the corresponding value of pethPsePortType of the port that connects the device.')
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1), )
if mibBuilder.loadTexts: pethMainPseTable.setStatus('current')
if mibBuilder.loadTexts: pethMainPseTable.setDescription('A table of objects that display and control the Main power on a PSE device.')
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1), ).setIndexNames((0, "PETH-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: pethMainPseEntry.setStatus('current')
if mibBuilder.loadTexts: pethMainPseEntry.setDescription('A set of objects that display and control the Main power of a PSE.')
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: pethMainPseGroupIndex.setStatus('current')
if mibBuilder.loadTexts: pethMainPseGroupIndex.setDescription('This variable uniquely identifies the group to which power Ethernet PSE is connected. Group means box in the stack, module in a rack. It is recommended that the value 1 be used for non-modular devices ')
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPsePower.setStatus('current')
if mibBuilder.loadTexts: pethMainPsePower.setDescription('The nominal power of the PSE expressed in Watts.')
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseOperStatus.setStatus('current')
if mibBuilder.loadTexts: pethMainPseOperStatus.setDescription('The operational status of the main PSE.')
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setStatus('current')
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setDescription('Measured usage power expressed in Watts.')
pethMainPseBackupPresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("present", 1), ("notPresent", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseBackupPresent.setStatus('current')
if mibBuilder.loadTexts: pethMainPseBackupPresent.setDescription('This value reflects the presence and status of a backup PSE .')
pethMainPseBackupActivated = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activated", 1), ("notActivated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseBackupActivated.setStatus('current')
if mibBuilder.loadTexts: pethMainPseBackupActivated.setDescription('This variable reflects the activation status of the backup PSE')
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setStatus('current')
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setDescription('The usage threshold expressed in percents for comparing the measured power and initiating an alarm if the threshold is exceeded.')
pethTrapsControl = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 4))
pethTrapsControlTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 4, 1), )
if mibBuilder.loadTexts: pethTrapsControlTable.setStatus('current')
if mibBuilder.loadTexts: pethTrapsControlTable.setDescription('A table of objects that display and control the Main power on a PSE device.')
pethTrapsControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 4, 1, 1), ).setIndexNames((0, "PETH-MIB", "pethTrapsControlGroupIndex"))
if mibBuilder.loadTexts: pethTrapsControlEntry.setStatus('current')
if mibBuilder.loadTexts: pethTrapsControlEntry.setDescription('A set of objects that control the Trap events.')
pethTrapsControlGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: pethTrapsControlGroupIndex.setStatus('current')
if mibBuilder.loadTexts: pethTrapsControlGroupIndex.setDescription('This variable uniquely identifies the group. Group means box in the stack, or module in a rack. It is recommended that the value 1 is used for non-modular devices.')
pethTrapsControlEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 20, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethTrapsControlEnable.setStatus('current')
if mibBuilder.loadTexts: pethTrapsControlEnable.setDescription('Enable Traps from Agent')
pethPsePortOnOffTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 7, 20, 2, 1)).setObjects(("PETH-MIB", "pethPsePortGroupIndex"), ("PETH-MIB", "pethPsePortIndex"), ("PETH-MIB", "pethPsePortDetectionOperStatus"))
if mibBuilder.loadTexts: pethPsePortOnOffTrap.setStatus('current')
if mibBuilder.loadTexts: pethPsePortOnOffTrap.setDescription(' This trap indicate if Pse Port is delivering or not power to the PD.')
pethPsePortDenyTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 7, 20, 2, 2)).setObjects(("PETH-MIB", "pethPsePortGroupIndex"), ("PETH-MIB", "pethPsePortIndex"), ("PETH-MIB", "pethPsePortDenyError"))
if mibBuilder.loadTexts: pethPsePortDenyTrap.setStatus('current')
if mibBuilder.loadTexts: pethPsePortDenyTrap.setDescription(' This trap indicate Port Deny service.')
pethPsePortStatusTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 7, 20, 2, 3)).setObjects(("PETH-MIB", "pethPsePortGroupIndex"), ("PETH-MIB", "pethPsePortIndex"), ("PETH-MIB", "pethPsePortStatus"))
if mibBuilder.loadTexts: pethPsePortStatusTrap.setStatus('current')
if mibBuilder.loadTexts: pethPsePortStatusTrap.setDescription(' This trap indicate Port Change Status.')
pethMainPseBackUpActivatedTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 7, 20, 2, 4)).setObjects(("PETH-MIB", "pethPsePortGroupIndex"), ("PETH-MIB", "pethMainPseBackupActivated"))
if mibBuilder.loadTexts: pethMainPseBackUpActivatedTrap.setStatus('current')
if mibBuilder.loadTexts: pethMainPseBackUpActivatedTrap.setDescription(' This trap indicates that BackUp PSE is Activated .')
pethMainPowerUsageTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 7, 20, 2, 5)).setObjects(("PETH-MIB", "pethPsePortGroupIndex"))
if mibBuilder.loadTexts: pethMainPowerUsageTrap.setStatus('current')
if mibBuilder.loadTexts: pethMainPowerUsageTrap.setDescription(' This trap indicate PSE Threshold usage indication .')
pethCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 2))
pethCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 1, 1)).setObjects(("PETH-MIB", "pethPsePortGroup"), ("PETH-MIB", "pethPdPortGroup"), ("PETH-MIB", "pethMainPseGroup"), ("PETH-MIB", "pethTrapsControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethCompliance = pethCompliance.setStatus('current')
if mibBuilder.loadTexts: pethCompliance.setDescription('Describes the requirements for conformance to the Power Ethernet MIB.')
pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 2, 1)).setObjects(("PETH-MIB", "pethPsePortPowerEnable"), ("PETH-MIB", "pethPsePortPowerIdPairsControl"), ("PETH-MIB", "pethPsePortPowerIdPairs"), ("PETH-MIB", "pethPsePortPowerDetectionStatus"), ("PETH-MIB", "pethPsePortDetectionOperStatus"), ("PETH-MIB", "pethPsePortPowerPriority"), ("PETH-MIB", "pethPsePortDenyError"), ("PETH-MIB", "pethPsePortStatus"), ("PETH-MIB", "pethPsePortStatusClear"), ("PETH-MIB", "pethPsePortType"), ("PETH-MIB", "pethPsePortPowerClassifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortGroup = pethPsePortGroup.setStatus('current')
if mibBuilder.loadTexts: pethPsePortGroup.setDescription('PSE Port Objects.')
pethPdPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 2, 2)).setObjects(("PETH-MIB", "pethPdPortPowerPairs"), ("PETH-MIB", "pethPdPortDetectionOperStatus"), ("PETH-MIB", "pethPdPortType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPdPortGroup = pethPdPortGroup.setStatus('current')
if mibBuilder.loadTexts: pethPdPortGroup.setDescription('PD Port Objects.')
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 2, 3)).setObjects(("PETH-MIB", "pethMainPsePower"), ("PETH-MIB", "pethMainPseOperStatus"), ("PETH-MIB", "pethMainPseConsumptionPower"), ("PETH-MIB", "pethMainPseBackupPresent"), ("PETH-MIB", "pethMainPseBackupActivated"), ("PETH-MIB", "pethMainPseUsageThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPseGroup = pethMainPseGroup.setStatus('current')
if mibBuilder.loadTexts: pethMainPseGroup.setDescription('Main PSE Objects. ')
pethTrapsControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 7, 20, 3, 2, 4)).setObjects(("PETH-MIB", "pethTrapsControlEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethTrapsControlGroup = pethTrapsControlGroup.setStatus('current')
if mibBuilder.loadTexts: pethTrapsControlGroup.setDescription('Trap Control Objects. ')
mibBuilder.exportSymbols("PETH-MIB", pethMainPseOperStatus=pethMainPseOperStatus, pethPsePortType=pethPsePortType, pethPdPortDetectionOperStatus=pethPdPortDetectionOperStatus, pethTrapsControlGroupIndex=pethTrapsControlGroupIndex, pethPsePortOnOffTrap=pethPsePortOnOffTrap, pethPsePortPowerDetectionStatus=pethPsePortPowerDetectionStatus, pethNotifications=pethNotifications, pethMainPseBackUpActivatedTrap=pethMainPseBackUpActivatedTrap, powerEthernetMIB=powerEthernetMIB, pethCompliances=pethCompliances, pethMainPseGroupIndex=pethMainPseGroupIndex, pethMainPsePower=pethMainPsePower, pethMainPseObjects=pethMainPseObjects, pethPsePortDetectionOperStatus=pethPsePortDetectionOperStatus, pethPsePortPowerIdPairsControl=pethPsePortPowerIdPairsControl, pethTrapsControlTable=pethTrapsControlTable, pethGroups=pethGroups, pethConformance=pethConformance, pethPsePortEntry=pethPsePortEntry, pethPsePortStatusClear=pethPsePortStatusClear, pethMainPseGroup=pethMainPseGroup, pethPdPortPowerPairs=pethPdPortPowerPairs, PYSNMP_MODULE_ID=powerEthernetMIB, pethPsePortTable=pethPsePortTable, pethPsePortPowerPriority=pethPsePortPowerPriority, pethPdPortIndex=pethPdPortIndex, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethPsePortDenyTrap=pethPsePortDenyTrap, pethTrapsControl=pethTrapsControl, pethMainPseBackupPresent=pethMainPseBackupPresent, pethPdPortTable=pethPdPortTable, pethMainPowerUsageTrap=pethMainPowerUsageTrap, pethMainPseTable=pethMainPseTable, pethPsePortPowerEnable=pethPsePortPowerEnable, pethPdPortGroup=pethPdPortGroup, pethMainPseBackupActivated=pethMainPseBackupActivated, pethObjects=pethObjects, pethPsePortDenyError=pethPsePortDenyError, pethPsePortPowerIdPairs=pethPsePortPowerIdPairs, pethPsePortGroupIndex=pethPsePortGroupIndex, pethPdPortEntry=pethPdPortEntry, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethCompliance=pethCompliance, pethPsePortStatus=pethPsePortStatus, pethTrapsControlEntry=pethTrapsControlEntry, pethPsePortStatusTrap=pethPsePortStatusTrap, pethTrapsControlGroup=pethTrapsControlGroup, pethPsePortIndex=pethPsePortIndex, pethPdPortType=pethPdPortType, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethTrapsControlEnable=pethTrapsControlEnable, pethPsePortGroup=pethPsePortGroup, pethMainPseEntry=pethMainPseEntry)
