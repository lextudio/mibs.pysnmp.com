# SNMP MIB module (CISCO-UNIFIED-COMPUTING-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:00 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsEquipmentEvacState,
 CucsEquipmentSensorThresholdStatus,
 CucsMgmtAdminState,
 CucsNetworkElementOperability,
 CucsNetworkIfStatsType,
 CucsNetworkIfStatsUnits,
 CucsNetworkInventoryStatus,
 CucsNetworkSwitchId,
 CucsNetworkVlanCountStatus) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsEquipmentEvacState",
    "CucsEquipmentSensorThresholdStatus",
    "CucsMgmtAdminState",
    "CucsNetworkElementOperability",
    "CucsNetworkIfStatsType",
    "CucsNetworkIfStatsUnits",
    "CucsNetworkInventoryStatus",
    "CucsNetworkSwitchId",
    "CucsNetworkVlanCountStatus")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsNetworkObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsNetworkElementTable_Object = MibTable
cucsNetworkElementTable = _CucsNetworkElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1)
)
if mibBuilder.loadTexts:
    cucsNetworkElementTable.setStatus("current")
_CucsNetworkElementEntry_Object = MibTableRow
cucsNetworkElementEntry = _CucsNetworkElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1)
)
cucsNetworkElementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkElementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkElementEntry.setStatus("current")
_CucsNetworkElementInstanceId_Type = CucsManagedObjectId
_CucsNetworkElementInstanceId_Object = MibTableColumn
cucsNetworkElementInstanceId = _CucsNetworkElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 1),
    _CucsNetworkElementInstanceId_Type()
)
cucsNetworkElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkElementInstanceId.setStatus("current")
_CucsNetworkElementDn_Type = CucsManagedObjectDn
_CucsNetworkElementDn_Object = MibTableColumn
cucsNetworkElementDn = _CucsNetworkElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 2),
    _CucsNetworkElementDn_Type()
)
cucsNetworkElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementDn.setStatus("current")
_CucsNetworkElementRn_Type = SnmpAdminString
_CucsNetworkElementRn_Object = MibTableColumn
cucsNetworkElementRn = _CucsNetworkElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 3),
    _CucsNetworkElementRn_Type()
)
cucsNetworkElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementRn.setStatus("current")
_CucsNetworkElementAdminInbandIfState_Type = CucsMgmtAdminState
_CucsNetworkElementAdminInbandIfState_Object = MibTableColumn
cucsNetworkElementAdminInbandIfState = _CucsNetworkElementAdminInbandIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 4),
    _CucsNetworkElementAdminInbandIfState_Type()
)
cucsNetworkElementAdminInbandIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementAdminInbandIfState.setStatus("current")
_CucsNetworkElementFltAggr_Type = Unsigned64
_CucsNetworkElementFltAggr_Object = MibTableColumn
cucsNetworkElementFltAggr = _CucsNetworkElementFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 5),
    _CucsNetworkElementFltAggr_Type()
)
cucsNetworkElementFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementFltAggr.setStatus("current")
_CucsNetworkElementId_Type = CucsNetworkSwitchId
_CucsNetworkElementId_Object = MibTableColumn
cucsNetworkElementId = _CucsNetworkElementId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 6),
    _CucsNetworkElementId_Type()
)
cucsNetworkElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementId.setStatus("current")
_CucsNetworkElementInbandIfGw_Type = InetAddressIPv4
_CucsNetworkElementInbandIfGw_Object = MibTableColumn
cucsNetworkElementInbandIfGw = _CucsNetworkElementInbandIfGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 7),
    _CucsNetworkElementInbandIfGw_Type()
)
cucsNetworkElementInbandIfGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementInbandIfGw.setStatus("current")
_CucsNetworkElementInbandIfIp_Type = InetAddressIPv4
_CucsNetworkElementInbandIfIp_Object = MibTableColumn
cucsNetworkElementInbandIfIp = _CucsNetworkElementInbandIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 8),
    _CucsNetworkElementInbandIfIp_Type()
)
cucsNetworkElementInbandIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementInbandIfIp.setStatus("current")
_CucsNetworkElementInbandIfMask_Type = InetAddressIPv4
_CucsNetworkElementInbandIfMask_Object = MibTableColumn
cucsNetworkElementInbandIfMask = _CucsNetworkElementInbandIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 9),
    _CucsNetworkElementInbandIfMask_Type()
)
cucsNetworkElementInbandIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementInbandIfMask.setStatus("current")
_CucsNetworkElementInbandIfVnet_Type = Gauge32
_CucsNetworkElementInbandIfVnet_Object = MibTableColumn
cucsNetworkElementInbandIfVnet = _CucsNetworkElementInbandIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 10),
    _CucsNetworkElementInbandIfVnet_Type()
)
cucsNetworkElementInbandIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementInbandIfVnet.setStatus("current")
_CucsNetworkElementModel_Type = SnmpAdminString
_CucsNetworkElementModel_Object = MibTableColumn
cucsNetworkElementModel = _CucsNetworkElementModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 11),
    _CucsNetworkElementModel_Type()
)
cucsNetworkElementModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementModel.setStatus("current")
_CucsNetworkElementOobIfGw_Type = InetAddressIPv4
_CucsNetworkElementOobIfGw_Object = MibTableColumn
cucsNetworkElementOobIfGw = _CucsNetworkElementOobIfGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 12),
    _CucsNetworkElementOobIfGw_Type()
)
cucsNetworkElementOobIfGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementOobIfGw.setStatus("current")
_CucsNetworkElementOobIfIp_Type = InetAddressIPv4
_CucsNetworkElementOobIfIp_Object = MibTableColumn
cucsNetworkElementOobIfIp = _CucsNetworkElementOobIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 13),
    _CucsNetworkElementOobIfIp_Type()
)
cucsNetworkElementOobIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementOobIfIp.setStatus("current")
_CucsNetworkElementOobIfMask_Type = InetAddressIPv4
_CucsNetworkElementOobIfMask_Object = MibTableColumn
cucsNetworkElementOobIfMask = _CucsNetworkElementOobIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 14),
    _CucsNetworkElementOobIfMask_Type()
)
cucsNetworkElementOobIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementOobIfMask.setStatus("current")
_CucsNetworkElementOperability_Type = CucsNetworkElementOperability
_CucsNetworkElementOperability_Object = MibTableColumn
cucsNetworkElementOperability = _CucsNetworkElementOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 15),
    _CucsNetworkElementOperability_Type()
)
cucsNetworkElementOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementOperability.setStatus("current")
_CucsNetworkElementRevision_Type = SnmpAdminString
_CucsNetworkElementRevision_Object = MibTableColumn
cucsNetworkElementRevision = _CucsNetworkElementRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 16),
    _CucsNetworkElementRevision_Type()
)
cucsNetworkElementRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementRevision.setStatus("current")
_CucsNetworkElementSerial_Type = SnmpAdminString
_CucsNetworkElementSerial_Object = MibTableColumn
cucsNetworkElementSerial = _CucsNetworkElementSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 17),
    _CucsNetworkElementSerial_Type()
)
cucsNetworkElementSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementSerial.setStatus("current")
_CucsNetworkElementTotalMemory_Type = Gauge32
_CucsNetworkElementTotalMemory_Object = MibTableColumn
cucsNetworkElementTotalMemory = _CucsNetworkElementTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 18),
    _CucsNetworkElementTotalMemory_Type()
)
cucsNetworkElementTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementTotalMemory.setStatus("current")
_CucsNetworkElementVendor_Type = SnmpAdminString
_CucsNetworkElementVendor_Object = MibTableColumn
cucsNetworkElementVendor = _CucsNetworkElementVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 19),
    _CucsNetworkElementVendor_Type()
)
cucsNetworkElementVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementVendor.setStatus("current")
_CucsNetworkElementInventoryStatus_Type = CucsNetworkInventoryStatus
_CucsNetworkElementInventoryStatus_Object = MibTableColumn
cucsNetworkElementInventoryStatus = _CucsNetworkElementInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 20),
    _CucsNetworkElementInventoryStatus_Type()
)
cucsNetworkElementInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementInventoryStatus.setStatus("current")
_CucsNetworkElementThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsNetworkElementThermal_Object = MibTableColumn
cucsNetworkElementThermal = _CucsNetworkElementThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 21),
    _CucsNetworkElementThermal_Type()
)
cucsNetworkElementThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementThermal.setStatus("current")
_CucsNetworkElementDiffMemory_Type = Gauge32
_CucsNetworkElementDiffMemory_Object = MibTableColumn
cucsNetworkElementDiffMemory = _CucsNetworkElementDiffMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 22),
    _CucsNetworkElementDiffMemory_Type()
)
cucsNetworkElementDiffMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementDiffMemory.setStatus("current")
_CucsNetworkElementExpectedMemory_Type = Gauge32
_CucsNetworkElementExpectedMemory_Object = MibTableColumn
cucsNetworkElementExpectedMemory = _CucsNetworkElementExpectedMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 23),
    _CucsNetworkElementExpectedMemory_Type()
)
cucsNetworkElementExpectedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementExpectedMemory.setStatus("current")
_CucsNetworkElementAdminEvacState_Type = CucsEquipmentEvacState
_CucsNetworkElementAdminEvacState_Object = MibTableColumn
cucsNetworkElementAdminEvacState = _CucsNetworkElementAdminEvacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 24),
    _CucsNetworkElementAdminEvacState_Type()
)
cucsNetworkElementAdminEvacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementAdminEvacState.setStatus("current")
_CucsNetworkElementForceEvac_Type = TruthValue
_CucsNetworkElementForceEvac_Object = MibTableColumn
cucsNetworkElementForceEvac = _CucsNetworkElementForceEvac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 25),
    _CucsNetworkElementForceEvac_Type()
)
cucsNetworkElementForceEvac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementForceEvac.setStatus("current")
_CucsNetworkElementOperEvacState_Type = CucsEquipmentEvacState
_CucsNetworkElementOperEvacState_Object = MibTableColumn
cucsNetworkElementOperEvacState = _CucsNetworkElementOperEvacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 26),
    _CucsNetworkElementOperEvacState_Type()
)
cucsNetworkElementOperEvacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementOperEvacState.setStatus("current")
_CucsNetworkElementOobIfMac_Type = MacAddress
_CucsNetworkElementOobIfMac_Object = MibTableColumn
cucsNetworkElementOobIfMac = _CucsNetworkElementOobIfMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 27),
    _CucsNetworkElementOobIfMac_Type()
)
cucsNetworkElementOobIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementOobIfMac.setStatus("current")
_CucsNetworkElementMinActiveFan_Type = Gauge32
_CucsNetworkElementMinActiveFan_Object = MibTableColumn
cucsNetworkElementMinActiveFan = _CucsNetworkElementMinActiveFan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 40),
    _CucsNetworkElementMinActiveFan_Type()
)
cucsNetworkElementMinActiveFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementMinActiveFan.setStatus("current")
_CucsNetworkElementShutdownFanRemoveal_Type = TruthValue
_CucsNetworkElementShutdownFanRemoveal_Object = MibTableColumn
cucsNetworkElementShutdownFanRemoveal = _CucsNetworkElementShutdownFanRemoveal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 1, 1, 41),
    _CucsNetworkElementShutdownFanRemoveal_Type()
)
cucsNetworkElementShutdownFanRemoveal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkElementShutdownFanRemoveal.setStatus("current")
_CucsNetworkIfStatsTable_Object = MibTable
cucsNetworkIfStatsTable = _CucsNetworkIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2)
)
if mibBuilder.loadTexts:
    cucsNetworkIfStatsTable.setStatus("current")
_CucsNetworkIfStatsEntry_Object = MibTableRow
cucsNetworkIfStatsEntry = _CucsNetworkIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1)
)
cucsNetworkIfStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkIfStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkIfStatsEntry.setStatus("current")
_CucsNetworkIfStatsInstanceId_Type = CucsManagedObjectId
_CucsNetworkIfStatsInstanceId_Object = MibTableColumn
cucsNetworkIfStatsInstanceId = _CucsNetworkIfStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 1),
    _CucsNetworkIfStatsInstanceId_Type()
)
cucsNetworkIfStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsInstanceId.setStatus("current")
_CucsNetworkIfStatsDn_Type = CucsManagedObjectDn
_CucsNetworkIfStatsDn_Object = MibTableColumn
cucsNetworkIfStatsDn = _CucsNetworkIfStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 2),
    _CucsNetworkIfStatsDn_Type()
)
cucsNetworkIfStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsDn.setStatus("current")
_CucsNetworkIfStatsRn_Type = SnmpAdminString
_CucsNetworkIfStatsRn_Object = MibTableColumn
cucsNetworkIfStatsRn = _CucsNetworkIfStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 3),
    _CucsNetworkIfStatsRn_Type()
)
cucsNetworkIfStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsRn.setStatus("current")
_CucsNetworkIfStatsOut_Type = Unsigned64
_CucsNetworkIfStatsOut_Object = MibTableColumn
cucsNetworkIfStatsOut = _CucsNetworkIfStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 5),
    _CucsNetworkIfStatsOut_Type()
)
cucsNetworkIfStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsOut.setStatus("current")
_CucsNetworkIfStatsType_Type = CucsNetworkIfStatsType
_CucsNetworkIfStatsType_Object = MibTableColumn
cucsNetworkIfStatsType = _CucsNetworkIfStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 6),
    _CucsNetworkIfStatsType_Type()
)
cucsNetworkIfStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsType.setStatus("current")
_CucsNetworkIfStatsUnits_Type = CucsNetworkIfStatsUnits
_CucsNetworkIfStatsUnits_Object = MibTableColumn
cucsNetworkIfStatsUnits = _CucsNetworkIfStatsUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 7),
    _CucsNetworkIfStatsUnits_Type()
)
cucsNetworkIfStatsUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsUnits.setStatus("current")
_CucsNetworkIfStatsRin_Type = Unsigned64
_CucsNetworkIfStatsRin_Object = MibTableColumn
cucsNetworkIfStatsRin = _CucsNetworkIfStatsRin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 2, 1, 8),
    _CucsNetworkIfStatsRin_Type()
)
cucsNetworkIfStatsRin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkIfStatsRin.setStatus("current")
_CucsNetworkOperLevelTable_Object = MibTable
cucsNetworkOperLevelTable = _CucsNetworkOperLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3)
)
if mibBuilder.loadTexts:
    cucsNetworkOperLevelTable.setStatus("current")
_CucsNetworkOperLevelEntry_Object = MibTableRow
cucsNetworkOperLevelEntry = _CucsNetworkOperLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1)
)
cucsNetworkOperLevelEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkOperLevelInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkOperLevelEntry.setStatus("current")
_CucsNetworkOperLevelInstanceId_Type = CucsManagedObjectId
_CucsNetworkOperLevelInstanceId_Object = MibTableColumn
cucsNetworkOperLevelInstanceId = _CucsNetworkOperLevelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 1),
    _CucsNetworkOperLevelInstanceId_Type()
)
cucsNetworkOperLevelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelInstanceId.setStatus("current")
_CucsNetworkOperLevelDn_Type = CucsManagedObjectDn
_CucsNetworkOperLevelDn_Object = MibTableColumn
cucsNetworkOperLevelDn = _CucsNetworkOperLevelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 2),
    _CucsNetworkOperLevelDn_Type()
)
cucsNetworkOperLevelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelDn.setStatus("current")
_CucsNetworkOperLevelRn_Type = SnmpAdminString
_CucsNetworkOperLevelRn_Object = MibTableColumn
cucsNetworkOperLevelRn = _CucsNetworkOperLevelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 3),
    _CucsNetworkOperLevelRn_Type()
)
cucsNetworkOperLevelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelRn.setStatus("current")
_CucsNetworkOperLevelId_Type = CucsNetworkSwitchId
_CucsNetworkOperLevelId_Object = MibTableColumn
cucsNetworkOperLevelId = _CucsNetworkOperLevelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 4),
    _CucsNetworkOperLevelId_Type()
)
cucsNetworkOperLevelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelId.setStatus("current")
_CucsNetworkOperLevelMaxPrimaryVlanCount_Type = Gauge32
_CucsNetworkOperLevelMaxPrimaryVlanCount_Object = MibTableColumn
cucsNetworkOperLevelMaxPrimaryVlanCount = _CucsNetworkOperLevelMaxPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 8),
    _CucsNetworkOperLevelMaxPrimaryVlanCount_Type()
)
cucsNetworkOperLevelMaxPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelMaxPrimaryVlanCount.setStatus("current")
_CucsNetworkOperLevelPrimaryVlanCount_Type = Gauge32
_CucsNetworkOperLevelPrimaryVlanCount_Object = MibTableColumn
cucsNetworkOperLevelPrimaryVlanCount = _CucsNetworkOperLevelPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 9),
    _CucsNetworkOperLevelPrimaryVlanCount_Type()
)
cucsNetworkOperLevelPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelPrimaryVlanCount.setStatus("current")
_CucsNetworkOperLevelPrimaryVlanCountStatus_Type = CucsNetworkVlanCountStatus
_CucsNetworkOperLevelPrimaryVlanCountStatus_Object = MibTableColumn
cucsNetworkOperLevelPrimaryVlanCountStatus = _CucsNetworkOperLevelPrimaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 10),
    _CucsNetworkOperLevelPrimaryVlanCountStatus_Type()
)
cucsNetworkOperLevelPrimaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelPrimaryVlanCountStatus.setStatus("current")
_CucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type = Gauge32
_CucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object = MibTableColumn
cucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount = _CucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 11),
    _CucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type()
)
cucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setStatus("current")
_CucsNetworkOperLevelMaxSecondaryVlanCount_Type = Gauge32
_CucsNetworkOperLevelMaxSecondaryVlanCount_Object = MibTableColumn
cucsNetworkOperLevelMaxSecondaryVlanCount = _CucsNetworkOperLevelMaxSecondaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 12),
    _CucsNetworkOperLevelMaxSecondaryVlanCount_Type()
)
cucsNetworkOperLevelMaxSecondaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelMaxSecondaryVlanCount.setStatus("current")
_CucsNetworkOperLevelSecondaryVlanCount_Type = Gauge32
_CucsNetworkOperLevelSecondaryVlanCount_Object = MibTableColumn
cucsNetworkOperLevelSecondaryVlanCount = _CucsNetworkOperLevelSecondaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 13),
    _CucsNetworkOperLevelSecondaryVlanCount_Type()
)
cucsNetworkOperLevelSecondaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelSecondaryVlanCount.setStatus("current")
_CucsNetworkOperLevelSecondaryVlanCountStatus_Type = CucsNetworkVlanCountStatus
_CucsNetworkOperLevelSecondaryVlanCountStatus_Object = MibTableColumn
cucsNetworkOperLevelSecondaryVlanCountStatus = _CucsNetworkOperLevelSecondaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 14),
    _CucsNetworkOperLevelSecondaryVlanCountStatus_Type()
)
cucsNetworkOperLevelSecondaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelSecondaryVlanCountStatus.setStatus("current")
_CucsNetworkOperLevelMaxVifCount_Type = Gauge32
_CucsNetworkOperLevelMaxVifCount_Object = MibTableColumn
cucsNetworkOperLevelMaxVifCount = _CucsNetworkOperLevelMaxVifCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 15),
    _CucsNetworkOperLevelMaxVifCount_Type()
)
cucsNetworkOperLevelMaxVifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelMaxVifCount.setStatus("current")
_CucsNetworkOperLevelVifCount_Type = Gauge32
_CucsNetworkOperLevelVifCount_Object = MibTableColumn
cucsNetworkOperLevelVifCount = _CucsNetworkOperLevelVifCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 16),
    _CucsNetworkOperLevelVifCount_Type()
)
cucsNetworkOperLevelVifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelVifCount.setStatus("current")
_CucsNetworkOperLevelVifCountStatus_Type = CucsNetworkVlanCountStatus
_CucsNetworkOperLevelVifCountStatus_Object = MibTableColumn
cucsNetworkOperLevelVifCountStatus = _CucsNetworkOperLevelVifCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 3, 1, 17),
    _CucsNetworkOperLevelVifCountStatus_Type()
)
cucsNetworkOperLevelVifCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkOperLevelVifCountStatus.setStatus("current")
_CucsNetworkLanNeighborEntryTable_Object = MibTable
cucsNetworkLanNeighborEntryTable = _CucsNetworkLanNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4)
)
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryTable.setStatus("current")
_CucsNetworkLanNeighborEntryEntry_Object = MibTableRow
cucsNetworkLanNeighborEntryEntry = _CucsNetworkLanNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1)
)
cucsNetworkLanNeighborEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkLanNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryEntry.setStatus("current")
_CucsNetworkLanNeighborEntryInstanceId_Type = CucsManagedObjectId
_CucsNetworkLanNeighborEntryInstanceId_Object = MibTableColumn
cucsNetworkLanNeighborEntryInstanceId = _CucsNetworkLanNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 1),
    _CucsNetworkLanNeighborEntryInstanceId_Type()
)
cucsNetworkLanNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryInstanceId.setStatus("current")
_CucsNetworkLanNeighborEntryDn_Type = CucsManagedObjectDn
_CucsNetworkLanNeighborEntryDn_Object = MibTableColumn
cucsNetworkLanNeighborEntryDn = _CucsNetworkLanNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 2),
    _CucsNetworkLanNeighborEntryDn_Type()
)
cucsNetworkLanNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryDn.setStatus("current")
_CucsNetworkLanNeighborEntryRn_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryRn_Object = MibTableColumn
cucsNetworkLanNeighborEntryRn = _CucsNetworkLanNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 3),
    _CucsNetworkLanNeighborEntryRn_Type()
)
cucsNetworkLanNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryRn.setStatus("current")
_CucsNetworkLanNeighborEntryCapabilities_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryCapabilities_Object = MibTableColumn
cucsNetworkLanNeighborEntryCapabilities = _CucsNetworkLanNeighborEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 4),
    _CucsNetworkLanNeighborEntryCapabilities_Type()
)
cucsNetworkLanNeighborEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryCapabilities.setStatus("current")
_CucsNetworkLanNeighborEntryDeviceId_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryDeviceId_Object = MibTableColumn
cucsNetworkLanNeighborEntryDeviceId = _CucsNetworkLanNeighborEntryDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 5),
    _CucsNetworkLanNeighborEntryDeviceId_Type()
)
cucsNetworkLanNeighborEntryDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryDeviceId.setStatus("current")
_CucsNetworkLanNeighborEntryFiPortDn_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryFiPortDn_Object = MibTableColumn
cucsNetworkLanNeighborEntryFiPortDn = _CucsNetworkLanNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 6),
    _CucsNetworkLanNeighborEntryFiPortDn_Type()
)
cucsNetworkLanNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryFiPortDn.setStatus("current")
_CucsNetworkLanNeighborEntryIpV4Address_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryIpV4Address_Object = MibTableColumn
cucsNetworkLanNeighborEntryIpV4Address = _CucsNetworkLanNeighborEntryIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 7),
    _CucsNetworkLanNeighborEntryIpV4Address_Type()
)
cucsNetworkLanNeighborEntryIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryIpV4Address.setStatus("current")
_CucsNetworkLanNeighborEntryIpV4MgmtAddress_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryIpV4MgmtAddress_Object = MibTableColumn
cucsNetworkLanNeighborEntryIpV4MgmtAddress = _CucsNetworkLanNeighborEntryIpV4MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 8),
    _CucsNetworkLanNeighborEntryIpV4MgmtAddress_Type()
)
cucsNetworkLanNeighborEntryIpV4MgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryIpV4MgmtAddress.setStatus("current")
_CucsNetworkLanNeighborEntryLocalInterface_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryLocalInterface_Object = MibTableColumn
cucsNetworkLanNeighborEntryLocalInterface = _CucsNetworkLanNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 9),
    _CucsNetworkLanNeighborEntryLocalInterface_Type()
)
cucsNetworkLanNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryLocalInterface.setStatus("current")
_CucsNetworkLanNeighborEntryNativeVlan_Type = Gauge32
_CucsNetworkLanNeighborEntryNativeVlan_Object = MibTableColumn
cucsNetworkLanNeighborEntryNativeVlan = _CucsNetworkLanNeighborEntryNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 10),
    _CucsNetworkLanNeighborEntryNativeVlan_Type()
)
cucsNetworkLanNeighborEntryNativeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryNativeVlan.setStatus("current")
_CucsNetworkLanNeighborEntryPlatform_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryPlatform_Object = MibTableColumn
cucsNetworkLanNeighborEntryPlatform = _CucsNetworkLanNeighborEntryPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 11),
    _CucsNetworkLanNeighborEntryPlatform_Type()
)
cucsNetworkLanNeighborEntryPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryPlatform.setStatus("current")
_CucsNetworkLanNeighborEntryRemoteInterface_Type = SnmpAdminString
_CucsNetworkLanNeighborEntryRemoteInterface_Object = MibTableColumn
cucsNetworkLanNeighborEntryRemoteInterface = _CucsNetworkLanNeighborEntryRemoteInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 12),
    _CucsNetworkLanNeighborEntryRemoteInterface_Type()
)
cucsNetworkLanNeighborEntryRemoteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntryRemoteInterface.setStatus("current")
_CucsNetworkLanNeighborEntrySerialNumber_Type = SnmpAdminString
_CucsNetworkLanNeighborEntrySerialNumber_Object = MibTableColumn
cucsNetworkLanNeighborEntrySerialNumber = _CucsNetworkLanNeighborEntrySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 13),
    _CucsNetworkLanNeighborEntrySerialNumber_Type()
)
cucsNetworkLanNeighborEntrySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntrySerialNumber.setStatus("current")
_CucsNetworkLanNeighborEntrySystemName_Type = SnmpAdminString
_CucsNetworkLanNeighborEntrySystemName_Object = MibTableColumn
cucsNetworkLanNeighborEntrySystemName = _CucsNetworkLanNeighborEntrySystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 4, 1, 14),
    _CucsNetworkLanNeighborEntrySystemName_Type()
)
cucsNetworkLanNeighborEntrySystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborEntrySystemName.setStatus("current")
_CucsNetworkLanNeighborsTable_Object = MibTable
cucsNetworkLanNeighborsTable = _CucsNetworkLanNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 5)
)
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborsTable.setStatus("current")
_CucsNetworkLanNeighborsEntry_Object = MibTableRow
cucsNetworkLanNeighborsEntry = _CucsNetworkLanNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 5, 1)
)
cucsNetworkLanNeighborsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkLanNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborsEntry.setStatus("current")
_CucsNetworkLanNeighborsInstanceId_Type = CucsManagedObjectId
_CucsNetworkLanNeighborsInstanceId_Object = MibTableColumn
cucsNetworkLanNeighborsInstanceId = _CucsNetworkLanNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 5, 1, 1),
    _CucsNetworkLanNeighborsInstanceId_Type()
)
cucsNetworkLanNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborsInstanceId.setStatus("current")
_CucsNetworkLanNeighborsDn_Type = CucsManagedObjectDn
_CucsNetworkLanNeighborsDn_Object = MibTableColumn
cucsNetworkLanNeighborsDn = _CucsNetworkLanNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 5, 1, 2),
    _CucsNetworkLanNeighborsDn_Type()
)
cucsNetworkLanNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborsDn.setStatus("current")
_CucsNetworkLanNeighborsRn_Type = SnmpAdminString
_CucsNetworkLanNeighborsRn_Object = MibTableColumn
cucsNetworkLanNeighborsRn = _CucsNetworkLanNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 5, 1, 3),
    _CucsNetworkLanNeighborsRn_Type()
)
cucsNetworkLanNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLanNeighborsRn.setStatus("current")
_CucsNetworkSanNeighborEntryTable_Object = MibTable
cucsNetworkSanNeighborEntryTable = _CucsNetworkSanNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6)
)
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryTable.setStatus("current")
_CucsNetworkSanNeighborEntryEntry_Object = MibTableRow
cucsNetworkSanNeighborEntryEntry = _CucsNetworkSanNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1)
)
cucsNetworkSanNeighborEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkSanNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryEntry.setStatus("current")
_CucsNetworkSanNeighborEntryInstanceId_Type = CucsManagedObjectId
_CucsNetworkSanNeighborEntryInstanceId_Object = MibTableColumn
cucsNetworkSanNeighborEntryInstanceId = _CucsNetworkSanNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 1),
    _CucsNetworkSanNeighborEntryInstanceId_Type()
)
cucsNetworkSanNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryInstanceId.setStatus("current")
_CucsNetworkSanNeighborEntryDn_Type = CucsManagedObjectDn
_CucsNetworkSanNeighborEntryDn_Object = MibTableColumn
cucsNetworkSanNeighborEntryDn = _CucsNetworkSanNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 2),
    _CucsNetworkSanNeighborEntryDn_Type()
)
cucsNetworkSanNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryDn.setStatus("current")
_CucsNetworkSanNeighborEntryRn_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryRn_Object = MibTableColumn
cucsNetworkSanNeighborEntryRn = _CucsNetworkSanNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 3),
    _CucsNetworkSanNeighborEntryRn_Type()
)
cucsNetworkSanNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryRn.setStatus("current")
_CucsNetworkSanNeighborEntryFabricMgmtAddr_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryFabricMgmtAddr_Object = MibTableColumn
cucsNetworkSanNeighborEntryFabricMgmtAddr = _CucsNetworkSanNeighborEntryFabricMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 4),
    _CucsNetworkSanNeighborEntryFabricMgmtAddr_Type()
)
cucsNetworkSanNeighborEntryFabricMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryFabricMgmtAddr.setStatus("current")
_CucsNetworkSanNeighborEntryFabricNwwn_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryFabricNwwn_Object = MibTableColumn
cucsNetworkSanNeighborEntryFabricNwwn = _CucsNetworkSanNeighborEntryFabricNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 5),
    _CucsNetworkSanNeighborEntryFabricNwwn_Type()
)
cucsNetworkSanNeighborEntryFabricNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryFabricNwwn.setStatus("current")
_CucsNetworkSanNeighborEntryFabricPwwn_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryFabricPwwn_Object = MibTableColumn
cucsNetworkSanNeighborEntryFabricPwwn = _CucsNetworkSanNeighborEntryFabricPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 6),
    _CucsNetworkSanNeighborEntryFabricPwwn_Type()
)
cucsNetworkSanNeighborEntryFabricPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryFabricPwwn.setStatus("current")
_CucsNetworkSanNeighborEntryFiPortDn_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryFiPortDn_Object = MibTableColumn
cucsNetworkSanNeighborEntryFiPortDn = _CucsNetworkSanNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 7),
    _CucsNetworkSanNeighborEntryFiPortDn_Type()
)
cucsNetworkSanNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryFiPortDn.setStatus("current")
_CucsNetworkSanNeighborEntryLocalInterface_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryLocalInterface_Object = MibTableColumn
cucsNetworkSanNeighborEntryLocalInterface = _CucsNetworkSanNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 8),
    _CucsNetworkSanNeighborEntryLocalInterface_Type()
)
cucsNetworkSanNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryLocalInterface.setStatus("current")
_CucsNetworkSanNeighborEntryMyNwwn_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryMyNwwn_Object = MibTableColumn
cucsNetworkSanNeighborEntryMyNwwn = _CucsNetworkSanNeighborEntryMyNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 9),
    _CucsNetworkSanNeighborEntryMyNwwn_Type()
)
cucsNetworkSanNeighborEntryMyNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryMyNwwn.setStatus("current")
_CucsNetworkSanNeighborEntryMyPwwn_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryMyPwwn_Object = MibTableColumn
cucsNetworkSanNeighborEntryMyPwwn = _CucsNetworkSanNeighborEntryMyPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 10),
    _CucsNetworkSanNeighborEntryMyPwwn_Type()
)
cucsNetworkSanNeighborEntryMyPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryMyPwwn.setStatus("current")
_CucsNetworkSanNeighborEntryPortVsan_Type = SnmpAdminString
_CucsNetworkSanNeighborEntryPortVsan_Object = MibTableColumn
cucsNetworkSanNeighborEntryPortVsan = _CucsNetworkSanNeighborEntryPortVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 6, 1, 11),
    _CucsNetworkSanNeighborEntryPortVsan_Type()
)
cucsNetworkSanNeighborEntryPortVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborEntryPortVsan.setStatus("current")
_CucsNetworkSanNeighborsTable_Object = MibTable
cucsNetworkSanNeighborsTable = _CucsNetworkSanNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 7)
)
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborsTable.setStatus("current")
_CucsNetworkSanNeighborsEntry_Object = MibTableRow
cucsNetworkSanNeighborsEntry = _CucsNetworkSanNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 7, 1)
)
cucsNetworkSanNeighborsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkSanNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborsEntry.setStatus("current")
_CucsNetworkSanNeighborsInstanceId_Type = CucsManagedObjectId
_CucsNetworkSanNeighborsInstanceId_Object = MibTableColumn
cucsNetworkSanNeighborsInstanceId = _CucsNetworkSanNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 7, 1, 1),
    _CucsNetworkSanNeighborsInstanceId_Type()
)
cucsNetworkSanNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborsInstanceId.setStatus("current")
_CucsNetworkSanNeighborsDn_Type = CucsManagedObjectDn
_CucsNetworkSanNeighborsDn_Object = MibTableColumn
cucsNetworkSanNeighborsDn = _CucsNetworkSanNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 7, 1, 2),
    _CucsNetworkSanNeighborsDn_Type()
)
cucsNetworkSanNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborsDn.setStatus("current")
_CucsNetworkSanNeighborsRn_Type = SnmpAdminString
_CucsNetworkSanNeighborsRn_Object = MibTableColumn
cucsNetworkSanNeighborsRn = _CucsNetworkSanNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 7, 1, 3),
    _CucsNetworkSanNeighborsRn_Type()
)
cucsNetworkSanNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkSanNeighborsRn.setStatus("current")
_CucsNetworkLldpNeighborEntryTable_Object = MibTable
cucsNetworkLldpNeighborEntryTable = _CucsNetworkLldpNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8)
)
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryTable.setStatus("current")
_CucsNetworkLldpNeighborEntryEntry_Object = MibTableRow
cucsNetworkLldpNeighborEntryEntry = _CucsNetworkLldpNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1)
)
cucsNetworkLldpNeighborEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkLldpNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryEntry.setStatus("current")
_CucsNetworkLldpNeighborEntryInstanceId_Type = CucsManagedObjectId
_CucsNetworkLldpNeighborEntryInstanceId_Object = MibTableColumn
cucsNetworkLldpNeighborEntryInstanceId = _CucsNetworkLldpNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 1),
    _CucsNetworkLldpNeighborEntryInstanceId_Type()
)
cucsNetworkLldpNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryInstanceId.setStatus("current")
_CucsNetworkLldpNeighborEntryDn_Type = CucsManagedObjectDn
_CucsNetworkLldpNeighborEntryDn_Object = MibTableColumn
cucsNetworkLldpNeighborEntryDn = _CucsNetworkLldpNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 2),
    _CucsNetworkLldpNeighborEntryDn_Type()
)
cucsNetworkLldpNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryDn.setStatus("current")
_CucsNetworkLldpNeighborEntryRn_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryRn_Object = MibTableColumn
cucsNetworkLldpNeighborEntryRn = _CucsNetworkLldpNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 3),
    _CucsNetworkLldpNeighborEntryRn_Type()
)
cucsNetworkLldpNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryRn.setStatus("current")
_CucsNetworkLldpNeighborEntryCapabilities_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryCapabilities_Object = MibTableColumn
cucsNetworkLldpNeighborEntryCapabilities = _CucsNetworkLldpNeighborEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 4),
    _CucsNetworkLldpNeighborEntryCapabilities_Type()
)
cucsNetworkLldpNeighborEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryCapabilities.setStatus("current")
_CucsNetworkLldpNeighborEntryChassisId_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryChassisId_Object = MibTableColumn
cucsNetworkLldpNeighborEntryChassisId = _CucsNetworkLldpNeighborEntryChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 5),
    _CucsNetworkLldpNeighborEntryChassisId_Type()
)
cucsNetworkLldpNeighborEntryChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryChassisId.setStatus("current")
_CucsNetworkLldpNeighborEntryEnabledCapabilities_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryEnabledCapabilities_Object = MibTableColumn
cucsNetworkLldpNeighborEntryEnabledCapabilities = _CucsNetworkLldpNeighborEntryEnabledCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 6),
    _CucsNetworkLldpNeighborEntryEnabledCapabilities_Type()
)
cucsNetworkLldpNeighborEntryEnabledCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryEnabledCapabilities.setStatus("current")
_CucsNetworkLldpNeighborEntryFiPortDn_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryFiPortDn_Object = MibTableColumn
cucsNetworkLldpNeighborEntryFiPortDn = _CucsNetworkLldpNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 7),
    _CucsNetworkLldpNeighborEntryFiPortDn_Type()
)
cucsNetworkLldpNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryFiPortDn.setStatus("current")
_CucsNetworkLldpNeighborEntryIpV4MgmtAddress_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryIpV4MgmtAddress_Object = MibTableColumn
cucsNetworkLldpNeighborEntryIpV4MgmtAddress = _CucsNetworkLldpNeighborEntryIpV4MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 8),
    _CucsNetworkLldpNeighborEntryIpV4MgmtAddress_Type()
)
cucsNetworkLldpNeighborEntryIpV4MgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryIpV4MgmtAddress.setStatus("current")
_CucsNetworkLldpNeighborEntryLocalInterface_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryLocalInterface_Object = MibTableColumn
cucsNetworkLldpNeighborEntryLocalInterface = _CucsNetworkLldpNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 9),
    _CucsNetworkLldpNeighborEntryLocalInterface_Type()
)
cucsNetworkLldpNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryLocalInterface.setStatus("current")
_CucsNetworkLldpNeighborEntryNativeVlan_Type = Gauge32
_CucsNetworkLldpNeighborEntryNativeVlan_Object = MibTableColumn
cucsNetworkLldpNeighborEntryNativeVlan = _CucsNetworkLldpNeighborEntryNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 10),
    _CucsNetworkLldpNeighborEntryNativeVlan_Type()
)
cucsNetworkLldpNeighborEntryNativeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryNativeVlan.setStatus("current")
_CucsNetworkLldpNeighborEntryRemoteIfDesc_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryRemoteIfDesc_Object = MibTableColumn
cucsNetworkLldpNeighborEntryRemoteIfDesc = _CucsNetworkLldpNeighborEntryRemoteIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 11),
    _CucsNetworkLldpNeighborEntryRemoteIfDesc_Type()
)
cucsNetworkLldpNeighborEntryRemoteIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryRemoteIfDesc.setStatus("current")
_CucsNetworkLldpNeighborEntryRemoteInterface_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntryRemoteInterface_Object = MibTableColumn
cucsNetworkLldpNeighborEntryRemoteInterface = _CucsNetworkLldpNeighborEntryRemoteInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 12),
    _CucsNetworkLldpNeighborEntryRemoteInterface_Type()
)
cucsNetworkLldpNeighborEntryRemoteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntryRemoteInterface.setStatus("current")
_CucsNetworkLldpNeighborEntrySystemDesc_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntrySystemDesc_Object = MibTableColumn
cucsNetworkLldpNeighborEntrySystemDesc = _CucsNetworkLldpNeighborEntrySystemDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 13),
    _CucsNetworkLldpNeighborEntrySystemDesc_Type()
)
cucsNetworkLldpNeighborEntrySystemDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntrySystemDesc.setStatus("current")
_CucsNetworkLldpNeighborEntrySystemName_Type = SnmpAdminString
_CucsNetworkLldpNeighborEntrySystemName_Object = MibTableColumn
cucsNetworkLldpNeighborEntrySystemName = _CucsNetworkLldpNeighborEntrySystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 8, 1, 14),
    _CucsNetworkLldpNeighborEntrySystemName_Type()
)
cucsNetworkLldpNeighborEntrySystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborEntrySystemName.setStatus("current")
_CucsNetworkLldpNeighborsTable_Object = MibTable
cucsNetworkLldpNeighborsTable = _CucsNetworkLldpNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 9)
)
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborsTable.setStatus("current")
_CucsNetworkLldpNeighborsEntry_Object = MibTableRow
cucsNetworkLldpNeighborsEntry = _CucsNetworkLldpNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 9, 1)
)
cucsNetworkLldpNeighborsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NETWORK-MIB", "cucsNetworkLldpNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborsEntry.setStatus("current")
_CucsNetworkLldpNeighborsInstanceId_Type = CucsManagedObjectId
_CucsNetworkLldpNeighborsInstanceId_Object = MibTableColumn
cucsNetworkLldpNeighborsInstanceId = _CucsNetworkLldpNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 9, 1, 1),
    _CucsNetworkLldpNeighborsInstanceId_Type()
)
cucsNetworkLldpNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborsInstanceId.setStatus("current")
_CucsNetworkLldpNeighborsDn_Type = CucsManagedObjectDn
_CucsNetworkLldpNeighborsDn_Object = MibTableColumn
cucsNetworkLldpNeighborsDn = _CucsNetworkLldpNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 9, 1, 2),
    _CucsNetworkLldpNeighborsDn_Type()
)
cucsNetworkLldpNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborsDn.setStatus("current")
_CucsNetworkLldpNeighborsRn_Type = SnmpAdminString
_CucsNetworkLldpNeighborsRn_Object = MibTableColumn
cucsNetworkLldpNeighborsRn = _CucsNetworkLldpNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 32, 9, 1, 3),
    _CucsNetworkLldpNeighborsRn_Type()
)
cucsNetworkLldpNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNetworkLldpNeighborsRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-NETWORK-MIB",
    **{"cucsNetworkObjects": cucsNetworkObjects,
       "cucsNetworkElementTable": cucsNetworkElementTable,
       "cucsNetworkElementEntry": cucsNetworkElementEntry,
       "cucsNetworkElementInstanceId": cucsNetworkElementInstanceId,
       "cucsNetworkElementDn": cucsNetworkElementDn,
       "cucsNetworkElementRn": cucsNetworkElementRn,
       "cucsNetworkElementAdminInbandIfState": cucsNetworkElementAdminInbandIfState,
       "cucsNetworkElementFltAggr": cucsNetworkElementFltAggr,
       "cucsNetworkElementId": cucsNetworkElementId,
       "cucsNetworkElementInbandIfGw": cucsNetworkElementInbandIfGw,
       "cucsNetworkElementInbandIfIp": cucsNetworkElementInbandIfIp,
       "cucsNetworkElementInbandIfMask": cucsNetworkElementInbandIfMask,
       "cucsNetworkElementInbandIfVnet": cucsNetworkElementInbandIfVnet,
       "cucsNetworkElementModel": cucsNetworkElementModel,
       "cucsNetworkElementOobIfGw": cucsNetworkElementOobIfGw,
       "cucsNetworkElementOobIfIp": cucsNetworkElementOobIfIp,
       "cucsNetworkElementOobIfMask": cucsNetworkElementOobIfMask,
       "cucsNetworkElementOperability": cucsNetworkElementOperability,
       "cucsNetworkElementRevision": cucsNetworkElementRevision,
       "cucsNetworkElementSerial": cucsNetworkElementSerial,
       "cucsNetworkElementTotalMemory": cucsNetworkElementTotalMemory,
       "cucsNetworkElementVendor": cucsNetworkElementVendor,
       "cucsNetworkElementInventoryStatus": cucsNetworkElementInventoryStatus,
       "cucsNetworkElementThermal": cucsNetworkElementThermal,
       "cucsNetworkElementDiffMemory": cucsNetworkElementDiffMemory,
       "cucsNetworkElementExpectedMemory": cucsNetworkElementExpectedMemory,
       "cucsNetworkElementAdminEvacState": cucsNetworkElementAdminEvacState,
       "cucsNetworkElementForceEvac": cucsNetworkElementForceEvac,
       "cucsNetworkElementOperEvacState": cucsNetworkElementOperEvacState,
       "cucsNetworkElementOobIfMac": cucsNetworkElementOobIfMac,
       "cucsNetworkElementMinActiveFan": cucsNetworkElementMinActiveFan,
       "cucsNetworkElementShutdownFanRemoveal": cucsNetworkElementShutdownFanRemoveal,
       "cucsNetworkIfStatsTable": cucsNetworkIfStatsTable,
       "cucsNetworkIfStatsEntry": cucsNetworkIfStatsEntry,
       "cucsNetworkIfStatsInstanceId": cucsNetworkIfStatsInstanceId,
       "cucsNetworkIfStatsDn": cucsNetworkIfStatsDn,
       "cucsNetworkIfStatsRn": cucsNetworkIfStatsRn,
       "cucsNetworkIfStatsOut": cucsNetworkIfStatsOut,
       "cucsNetworkIfStatsType": cucsNetworkIfStatsType,
       "cucsNetworkIfStatsUnits": cucsNetworkIfStatsUnits,
       "cucsNetworkIfStatsRin": cucsNetworkIfStatsRin,
       "cucsNetworkOperLevelTable": cucsNetworkOperLevelTable,
       "cucsNetworkOperLevelEntry": cucsNetworkOperLevelEntry,
       "cucsNetworkOperLevelInstanceId": cucsNetworkOperLevelInstanceId,
       "cucsNetworkOperLevelDn": cucsNetworkOperLevelDn,
       "cucsNetworkOperLevelRn": cucsNetworkOperLevelRn,
       "cucsNetworkOperLevelId": cucsNetworkOperLevelId,
       "cucsNetworkOperLevelMaxPrimaryVlanCount": cucsNetworkOperLevelMaxPrimaryVlanCount,
       "cucsNetworkOperLevelPrimaryVlanCount": cucsNetworkOperLevelPrimaryVlanCount,
       "cucsNetworkOperLevelPrimaryVlanCountStatus": cucsNetworkOperLevelPrimaryVlanCountStatus,
       "cucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount": cucsNetworkOperLevelMaxSecVlanPerPrimaryVlanCount,
       "cucsNetworkOperLevelMaxSecondaryVlanCount": cucsNetworkOperLevelMaxSecondaryVlanCount,
       "cucsNetworkOperLevelSecondaryVlanCount": cucsNetworkOperLevelSecondaryVlanCount,
       "cucsNetworkOperLevelSecondaryVlanCountStatus": cucsNetworkOperLevelSecondaryVlanCountStatus,
       "cucsNetworkOperLevelMaxVifCount": cucsNetworkOperLevelMaxVifCount,
       "cucsNetworkOperLevelVifCount": cucsNetworkOperLevelVifCount,
       "cucsNetworkOperLevelVifCountStatus": cucsNetworkOperLevelVifCountStatus,
       "cucsNetworkLanNeighborEntryTable": cucsNetworkLanNeighborEntryTable,
       "cucsNetworkLanNeighborEntryEntry": cucsNetworkLanNeighborEntryEntry,
       "cucsNetworkLanNeighborEntryInstanceId": cucsNetworkLanNeighborEntryInstanceId,
       "cucsNetworkLanNeighborEntryDn": cucsNetworkLanNeighborEntryDn,
       "cucsNetworkLanNeighborEntryRn": cucsNetworkLanNeighborEntryRn,
       "cucsNetworkLanNeighborEntryCapabilities": cucsNetworkLanNeighborEntryCapabilities,
       "cucsNetworkLanNeighborEntryDeviceId": cucsNetworkLanNeighborEntryDeviceId,
       "cucsNetworkLanNeighborEntryFiPortDn": cucsNetworkLanNeighborEntryFiPortDn,
       "cucsNetworkLanNeighborEntryIpV4Address": cucsNetworkLanNeighborEntryIpV4Address,
       "cucsNetworkLanNeighborEntryIpV4MgmtAddress": cucsNetworkLanNeighborEntryIpV4MgmtAddress,
       "cucsNetworkLanNeighborEntryLocalInterface": cucsNetworkLanNeighborEntryLocalInterface,
       "cucsNetworkLanNeighborEntryNativeVlan": cucsNetworkLanNeighborEntryNativeVlan,
       "cucsNetworkLanNeighborEntryPlatform": cucsNetworkLanNeighborEntryPlatform,
       "cucsNetworkLanNeighborEntryRemoteInterface": cucsNetworkLanNeighborEntryRemoteInterface,
       "cucsNetworkLanNeighborEntrySerialNumber": cucsNetworkLanNeighborEntrySerialNumber,
       "cucsNetworkLanNeighborEntrySystemName": cucsNetworkLanNeighborEntrySystemName,
       "cucsNetworkLanNeighborsTable": cucsNetworkLanNeighborsTable,
       "cucsNetworkLanNeighborsEntry": cucsNetworkLanNeighborsEntry,
       "cucsNetworkLanNeighborsInstanceId": cucsNetworkLanNeighborsInstanceId,
       "cucsNetworkLanNeighborsDn": cucsNetworkLanNeighborsDn,
       "cucsNetworkLanNeighborsRn": cucsNetworkLanNeighborsRn,
       "cucsNetworkSanNeighborEntryTable": cucsNetworkSanNeighborEntryTable,
       "cucsNetworkSanNeighborEntryEntry": cucsNetworkSanNeighborEntryEntry,
       "cucsNetworkSanNeighborEntryInstanceId": cucsNetworkSanNeighborEntryInstanceId,
       "cucsNetworkSanNeighborEntryDn": cucsNetworkSanNeighborEntryDn,
       "cucsNetworkSanNeighborEntryRn": cucsNetworkSanNeighborEntryRn,
       "cucsNetworkSanNeighborEntryFabricMgmtAddr": cucsNetworkSanNeighborEntryFabricMgmtAddr,
       "cucsNetworkSanNeighborEntryFabricNwwn": cucsNetworkSanNeighborEntryFabricNwwn,
       "cucsNetworkSanNeighborEntryFabricPwwn": cucsNetworkSanNeighborEntryFabricPwwn,
       "cucsNetworkSanNeighborEntryFiPortDn": cucsNetworkSanNeighborEntryFiPortDn,
       "cucsNetworkSanNeighborEntryLocalInterface": cucsNetworkSanNeighborEntryLocalInterface,
       "cucsNetworkSanNeighborEntryMyNwwn": cucsNetworkSanNeighborEntryMyNwwn,
       "cucsNetworkSanNeighborEntryMyPwwn": cucsNetworkSanNeighborEntryMyPwwn,
       "cucsNetworkSanNeighborEntryPortVsan": cucsNetworkSanNeighborEntryPortVsan,
       "cucsNetworkSanNeighborsTable": cucsNetworkSanNeighborsTable,
       "cucsNetworkSanNeighborsEntry": cucsNetworkSanNeighborsEntry,
       "cucsNetworkSanNeighborsInstanceId": cucsNetworkSanNeighborsInstanceId,
       "cucsNetworkSanNeighborsDn": cucsNetworkSanNeighborsDn,
       "cucsNetworkSanNeighborsRn": cucsNetworkSanNeighborsRn,
       "cucsNetworkLldpNeighborEntryTable": cucsNetworkLldpNeighborEntryTable,
       "cucsNetworkLldpNeighborEntryEntry": cucsNetworkLldpNeighborEntryEntry,
       "cucsNetworkLldpNeighborEntryInstanceId": cucsNetworkLldpNeighborEntryInstanceId,
       "cucsNetworkLldpNeighborEntryDn": cucsNetworkLldpNeighborEntryDn,
       "cucsNetworkLldpNeighborEntryRn": cucsNetworkLldpNeighborEntryRn,
       "cucsNetworkLldpNeighborEntryCapabilities": cucsNetworkLldpNeighborEntryCapabilities,
       "cucsNetworkLldpNeighborEntryChassisId": cucsNetworkLldpNeighborEntryChassisId,
       "cucsNetworkLldpNeighborEntryEnabledCapabilities": cucsNetworkLldpNeighborEntryEnabledCapabilities,
       "cucsNetworkLldpNeighborEntryFiPortDn": cucsNetworkLldpNeighborEntryFiPortDn,
       "cucsNetworkLldpNeighborEntryIpV4MgmtAddress": cucsNetworkLldpNeighborEntryIpV4MgmtAddress,
       "cucsNetworkLldpNeighborEntryLocalInterface": cucsNetworkLldpNeighborEntryLocalInterface,
       "cucsNetworkLldpNeighborEntryNativeVlan": cucsNetworkLldpNeighborEntryNativeVlan,
       "cucsNetworkLldpNeighborEntryRemoteIfDesc": cucsNetworkLldpNeighborEntryRemoteIfDesc,
       "cucsNetworkLldpNeighborEntryRemoteInterface": cucsNetworkLldpNeighborEntryRemoteInterface,
       "cucsNetworkLldpNeighborEntrySystemDesc": cucsNetworkLldpNeighborEntrySystemDesc,
       "cucsNetworkLldpNeighborEntrySystemName": cucsNetworkLldpNeighborEntrySystemName,
       "cucsNetworkLldpNeighborsTable": cucsNetworkLldpNeighborsTable,
       "cucsNetworkLldpNeighborsEntry": cucsNetworkLldpNeighborsEntry,
       "cucsNetworkLldpNeighborsInstanceId": cucsNetworkLldpNeighborsInstanceId,
       "cucsNetworkLldpNeighborsDn": cucsNetworkLldpNeighborsDn,
       "cucsNetworkLldpNeighborsRn": cucsNetworkLldpNeighborsRn}
)
