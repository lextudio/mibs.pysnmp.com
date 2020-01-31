#
# PySNMP MIB module TERAWAVE-teraCon-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-teraCon-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Counter64, ModuleIdentity, MibIdentifier, enterprises, IpAddress, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "ModuleIdentity", "MibIdentifier", "enterprises", "IpAddress", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
connections = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 2))
conTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 1), )
if mibBuilder.loadTexts: conTable.setStatus('mandatory')
if mibBuilder.loadTexts: conTable.setDescription(' table conTable')
nextConTableEntryIndex = MibScalar((1, 3, 6, 1, 4, 1, 4513, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextConTableEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nextConTableEntryIndex.setDescription(' Next index to the table.')
conTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "circuitCONID"))
if mibBuilder.loadTexts: conTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: conTableEntry.setDescription(' table entry conTableEntry ')
circuitCONID = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitCONID.setStatus('mandatory')
if mibBuilder.loadTexts: circuitCONID.setDescription('')
circuitCONName = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: circuitCONName.setStatus('mandatory')
if mibBuilder.loadTexts: circuitCONName.setDescription('')
serviceCONType = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("tdm-tdm", 1), ("tdm-pvc", 2), ("pvc-pvc", 3), ("lan-pvc", 4), ("lan-lan", 5), ("lan2pvc", 6), ("vlan-trunk", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serviceCONType.setStatus('mandatory')
if mibBuilder.loadTexts: serviceCONType.setDescription('')
firstCONIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firstCONIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: firstCONIfIndex.setDescription('')
secondCONIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondCONIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: secondCONIfIndex.setDescription('')
firstCONVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firstCONVPI.setStatus('mandatory')
if mibBuilder.loadTexts: firstCONVPI.setDescription('')
firstCONVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firstCONVCI.setStatus('mandatory')
if mibBuilder.loadTexts: firstCONVCI.setDescription('')
secondCONVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondCONVPI.setStatus('mandatory')
if mibBuilder.loadTexts: secondCONVPI.setDescription('')
secondCONVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondCONVCI.setStatus('mandatory')
if mibBuilder.loadTexts: secondCONVCI.setDescription('')
conVLANNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: conVLANNumber.setStatus('mandatory')
if mibBuilder.loadTexts: conVLANNumber.setDescription('')
requestedCONBW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("atm", 1), ("vlan-c", 2), ("t1", 3), ("e1", 4), ("ds3", 5), ("e3", 6), ("oc3", 7), ("stm1", 8), ("atm-vpi", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: requestedCONBW.setStatus('mandatory')
if mibBuilder.loadTexts: requestedCONBW.setDescription('')
firstInternalVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firstInternalVPI.setStatus('mandatory')
if mibBuilder.loadTexts: firstInternalVPI.setDescription('')
firstInternalVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firstInternalVCI.setStatus('mandatory')
if mibBuilder.loadTexts: firstInternalVCI.setDescription('')
secondInternalVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secondInternalVPI.setStatus('mandatory')
if mibBuilder.loadTexts: secondInternalVPI.setDescription('')
secondInternalVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secondInternalVCI.setStatus('mandatory')
if mibBuilder.loadTexts: secondInternalVCI.setDescription('')
rowCONTableAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rowCONTableAction.setStatus('mandatory')
if mibBuilder.loadTexts: rowCONTableAction.setDescription('')
conStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: conStatus.setStatus('mandatory')
if mibBuilder.loadTexts: conStatus.setDescription('')
conUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: conUserId.setStatus('mandatory')
if mibBuilder.loadTexts: conUserId.setDescription('')
conUserConId = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: conUserConId.setStatus('mandatory')
if mibBuilder.loadTexts: conUserConId.setDescription('')
circTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 2), )
if mibBuilder.loadTexts: circTable.setStatus('mandatory')
if mibBuilder.loadTexts: circTable.setDescription(' table circTable')
circTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 2, 1), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "circuitCONID"))
if mibBuilder.loadTexts: circTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: circTableEntry.setDescription(' table entry circTableEntry ')
cmFirstInternalVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmFirstInternalVPI.setStatus('mandatory')
if mibBuilder.loadTexts: cmFirstInternalVPI.setDescription('')
cmFirstInternalVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmFirstInternalVCI.setStatus('mandatory')
if mibBuilder.loadTexts: cmFirstInternalVCI.setDescription('')
cmSecondInternalVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmSecondInternalVPI.setStatus('mandatory')
if mibBuilder.loadTexts: cmSecondInternalVPI.setDescription('')
cmSecondInternalVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmSecondInternalVCI.setStatus('mandatory')
if mibBuilder.loadTexts: cmSecondInternalVCI.setDescription('')
bandwidthGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 2, 3))
bwGroupTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1), )
if mibBuilder.loadTexts: bwGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupTable.setDescription(' table bwGroupTable')
bwGroupTableNextId = MibScalar((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwGroupTableNextId.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupTableNextId.setDescription(' Next index to the table.')
bwGroupTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "bwGroupId"))
if mibBuilder.loadTexts: bwGroupTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupTableEntry.setDescription(' table entry bwGroupTableEntry ')
bwGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupId.setDescription('')
bwGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGroupName.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupName.setDescription('')
requestedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: requestedBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: requestedBandwidth.setDescription('')
maxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: maxBandwidth.setDescription('')
bwGroupPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGroupPorts.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupPorts.setDescription('')
bwGroupTableAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGroupTableAction.setStatus('mandatory')
if mibBuilder.loadTexts: bwGroupTableAction.setDescription('')
teraStaticBWTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 4), )
if mibBuilder.loadTexts: teraStaticBWTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticBWTable.setDescription(' table teraStaticBWTable')
teraStaticBWTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 4, 1), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "teraInstallSlotNumber"))
if mibBuilder.loadTexts: teraStaticBWTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticBWTableEntry.setDescription(' table entry teraStaticBWTableEntry ')
teraStaticBWTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticBWTotal.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticBWTotal.setDescription('')
teraStaticBWcbr = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticBWcbr.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticBWcbr.setDescription('')
teraStaticBWaux = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticBWaux.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticBWaux.setDescription('')
teraStaticBWvbr = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticBWvbr.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticBWvbr.setDescription('')
teraStaticAllocBWvbr = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticAllocBWvbr.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticAllocBWvbr.setDescription('')
teraStaticSplitBWTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 5), )
if mibBuilder.loadTexts: teraStaticSplitBWTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWTable.setDescription(' table teraStaticSplitBWTable')
teraStaticSplitBWTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "teraInstallSlotNumber"), (0, "TERAWAVE-teraCon-MIB", "teraNEIDxSlotLevel1"))
if mibBuilder.loadTexts: teraStaticSplitBWTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWTableEntry.setDescription(' table entry teraStaticSplitBWTableEntry ')
teraStaticSplitBWVBRConn = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticSplitBWVBRConn.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWVBRConn.setDescription('')
teraStaticSplitBWCBRConn = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticSplitBWCBRConn.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWCBRConn.setDescription('')
teraStaticSplitBWEffective = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticSplitBWEffective.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWEffective.setDescription('')
teraStaticSplitBWUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticSplitBWUnits.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWUnits.setDescription('')
teraStaticSplitBWUnitsBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticSplitBWUnitsBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWUnitsBandwidth.setDescription('')
teraStaticSplitBWAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraStaticSplitBWAllocated.setStatus('mandatory')
if mibBuilder.loadTexts: teraStaticSplitBWAllocated.setDescription('')
teraCraftCMTable = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 2, 6))
teraCraftCMAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4513, 2, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("granted", 1), ("notgranted", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraCraftCMAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraCraftCMAdminStatus.setDescription('')
teraCraftCMOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 4513, 2, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("wait4ack", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCraftCMOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraCraftCMOperStatus.setDescription('')
teraManagementPVCTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 7), )
if mibBuilder.loadTexts: teraManagementPVCTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCTable.setDescription(' table teraManagementPVCTable')
teraManagementPVCTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "teraManagementPVCNumber"))
if mibBuilder.loadTexts: teraManagementPVCTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCTableEntry.setDescription(' table entry teraManagementPVCTableEntry ')
teraManagementPVCNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraManagementPVCNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCNumber.setDescription('')
teraManagementPVCAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCAdminStatus.setDescription('')
teraManagementPVCPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCPortIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCPortIfIndex.setDescription('')
teraManagementPVCVclVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCVclVpi.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCVclVpi.setDescription('')
teraManagementPVCVclVci = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCVclVci.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCVclVci.setDescription('')
teraManagementPVCIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCIPAddress.setDescription('')
teraManagementPVCIPNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCIPNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCIPNetMask.setDescription('')
teraManagementPVCIPGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCIPGateway.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCIPGateway.setDescription('')
teraManagementPVCIPMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCIPMtu.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCIPMtu.setDescription('')
teraManagementPVCIPEncapsType = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("llcNone", 1), ("llcRoutedIPv4", 2), ("llcRoutedIPv4AtmArp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraManagementPVCIPEncapsType.setStatus('mandatory')
if mibBuilder.loadTexts: teraManagementPVCIPEncapsType.setDescription('')
teraONTconTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 2, 8), )
if mibBuilder.loadTexts: teraONTconTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTconTable.setDescription(' table teraONTconTable')
teraONTconTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1), ).setIndexNames((0, "TERAWAVE-teraCon-MIB", "teraONTconID"))
if mibBuilder.loadTexts: teraONTconTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTconTableEntry.setDescription(' table entry teraONTconTableEntry ')
teraONTconID = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTconID.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTconID.setDescription('')
teraONTfirstCONIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTfirstCONIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTfirstCONIfIndex.setDescription('')
teraONTsecondCONIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTsecondCONIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTsecondCONIfIndex.setDescription('')
teraONTfirstCONVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTfirstCONVPI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTfirstCONVPI.setDescription('')
teraONTfirstCONVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTfirstCONVCI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTfirstCONVCI.setDescription('')
teraONTsecondCONVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTsecondCONVPI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTsecondCONVPI.setDescription('')
teraONTsecondCONVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTsecondCONVCI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTsecondCONVCI.setDescription('')
teraONTconVLANNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTconVLANNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTconVLANNumber.setDescription('')
teraONTrequestedCONBW = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("atm", 1), ("vlan-c", 2), ("t1", 3), ("e1", 4), ("ds3", 5), ("e3", 6), ("oc3", 7), ("stm1", 8), ("atm-vpi", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTrequestedCONBW.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTrequestedCONBW.setDescription('')
teraONTfirstInternalVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTfirstInternalVPI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTfirstInternalVPI.setDescription('')
teraONTfirstInternalVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTfirstInternalVCI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTfirstInternalVCI.setDescription('')
teraONTsecondInternalVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTsecondInternalVPI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTsecondInternalVPI.setDescription('')
teraONTsecondInternalVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTsecondInternalVCI.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTsecondInternalVCI.setDescription('')
teraONTconStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraONTconStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraONTconStatus.setDescription('')
mibBuilder.exportSymbols("TERAWAVE-teraCon-MIB", cmFirstInternalVPI=cmFirstInternalVPI, teraONTsecondCONIfIndex=teraONTsecondCONIfIndex, teraONTconVLANNumber=teraONTconVLANNumber, connections=connections, serviceCONType=serviceCONType, teraManagementPVCVclVci=teraManagementPVCVclVci, bwGroupTableEntry=bwGroupTableEntry, bwGroupTableNextId=bwGroupTableNextId, teraStaticSplitBWTableEntry=teraStaticSplitBWTableEntry, requestedBandwidth=requestedBandwidth, conTableEntry=conTableEntry, conTable=conTable, teraStaticSplitBWUnitsBandwidth=teraStaticSplitBWUnitsBandwidth, teraManagementPVCIPAddress=teraManagementPVCIPAddress, teraManagementPVCTableEntry=teraManagementPVCTableEntry, teraStaticAllocBWvbr=teraStaticAllocBWvbr, teraCraftCMTable=teraCraftCMTable, teraONTrequestedCONBW=teraONTrequestedCONBW, teraManagementPVCIPGateway=teraManagementPVCIPGateway, bwGroupPorts=bwGroupPorts, teraONTfirstCONIfIndex=teraONTfirstCONIfIndex, teraManagementPVCAdminStatus=teraManagementPVCAdminStatus, teraManagementPVCIPMtu=teraManagementPVCIPMtu, circuitCONName=circuitCONName, terawave=terawave, teraStaticSplitBWCBRConn=teraStaticSplitBWCBRConn, bwGroupTable=bwGroupTable, teraONTfirstInternalVCI=teraONTfirstInternalVCI, nextConTableEntryIndex=nextConTableEntryIndex, teraONTconID=teraONTconID, teraONTfirstCONVCI=teraONTfirstCONVCI, secondCONVCI=secondCONVCI, teraONTsecondCONVPI=teraONTsecondCONVPI, circTable=circTable, teraONTsecondCONVCI=teraONTsecondCONVCI, teraONTfirstCONVPI=teraONTfirstCONVPI, secondCONVPI=secondCONVPI, requestedCONBW=requestedCONBW, teraStaticSplitBWUnits=teraStaticSplitBWUnits, cmSecondInternalVPI=cmSecondInternalVPI, teraStaticBWvbr=teraStaticBWvbr, cmSecondInternalVCI=cmSecondInternalVCI, circuitCONID=circuitCONID, firstInternalVCI=firstInternalVCI, conUserConId=conUserConId, secondInternalVCI=secondInternalVCI, bwGroupName=bwGroupName, rowCONTableAction=rowCONTableAction, teraStaticSplitBWVBRConn=teraStaticSplitBWVBRConn, teraONTfirstInternalVPI=teraONTfirstInternalVPI, teraStaticBWaux=teraStaticBWaux, teraManagementPVCPortIfIndex=teraManagementPVCPortIfIndex, teraONTsecondInternalVCI=teraONTsecondInternalVCI, maxBandwidth=maxBandwidth, secondInternalVPI=secondInternalVPI, firstCONVCI=firstCONVCI, conUserId=conUserId, teraManagementPVCIPNetMask=teraManagementPVCIPNetMask, teraManagementPVCTable=teraManagementPVCTable, bandwidthGroup=bandwidthGroup, teraManagementPVCIPEncapsType=teraManagementPVCIPEncapsType, circTableEntry=circTableEntry, teraONTconTable=teraONTconTable, teraCraftCMOperStatus=teraCraftCMOperStatus, teraStaticSplitBWTable=teraStaticSplitBWTable, conVLANNumber=conVLANNumber, bwGroupId=bwGroupId, teraStaticBWcbr=teraStaticBWcbr, teraONTsecondInternalVPI=teraONTsecondInternalVPI, teraStaticBWTableEntry=teraStaticBWTableEntry, firstInternalVPI=firstInternalVPI, teraCraftCMAdminStatus=teraCraftCMAdminStatus, teraStaticSplitBWAllocated=teraStaticSplitBWAllocated, teraONTconTableEntry=teraONTconTableEntry, teraManagementPVCNumber=teraManagementPVCNumber, cmFirstInternalVCI=cmFirstInternalVCI, firstCONVPI=firstCONVPI, secondCONIfIndex=secondCONIfIndex, teraStaticBWTotal=teraStaticBWTotal, teraONTconStatus=teraONTconStatus, conStatus=conStatus, teraStaticSplitBWEffective=teraStaticSplitBWEffective, firstCONIfIndex=firstCONIfIndex, bwGroupTableAction=bwGroupTableAction, teraStaticBWTable=teraStaticBWTable, teraManagementPVCVclVpi=teraManagementPVCVclVpi)