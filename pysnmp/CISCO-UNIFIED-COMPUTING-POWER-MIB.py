# SNMP MIB module (CISCO-UNIFIED-COMPUTING-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:12 2024
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

(CucsPolicyPolicyOwner,
 CucsPowerBudgetFanSpeed,
 CucsPowerCapAction,
 CucsPowerChThrAction,
 CucsPowerGroupState,
 CucsPowerGroupStatsHistThresholded,
 CucsPowerGroupStatsThresholded,
 CucsPowerLockState,
 CucsPowerMemberState,
 CucsPowerMgmtStyle,
 CucsPowerOperState,
 CucsPowerPolicyFanSpeed,
 CucsPowerPowerAvailState,
 CucsPowerPowerDeployState,
 CucsPowerPrioritySharing,
 CucsPowerProfilingMethod,
 CucsPowerPsuLineMode,
 CucsPowerPsuState,
 CucsPowerReallocation,
 CucsPowerReqConflict) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsPolicyPolicyOwner",
    "CucsPowerBudgetFanSpeed",
    "CucsPowerCapAction",
    "CucsPowerChThrAction",
    "CucsPowerGroupState",
    "CucsPowerGroupStatsHistThresholded",
    "CucsPowerGroupStatsThresholded",
    "CucsPowerLockState",
    "CucsPowerMemberState",
    "CucsPowerMgmtStyle",
    "CucsPowerOperState",
    "CucsPowerPolicyFanSpeed",
    "CucsPowerPowerAvailState",
    "CucsPowerPowerDeployState",
    "CucsPowerPrioritySharing",
    "CucsPowerProfilingMethod",
    "CucsPowerPsuLineMode",
    "CucsPowerPsuState",
    "CucsPowerReallocation",
    "CucsPowerReqConflict")

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

cucsPowerObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsPowerBudgetTable_Object = MibTable
cucsPowerBudgetTable = _CucsPowerBudgetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1)
)
if mibBuilder.loadTexts:
    cucsPowerBudgetTable.setStatus("current")
_CucsPowerBudgetEntry_Object = MibTableRow
cucsPowerBudgetEntry = _CucsPowerBudgetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1)
)
cucsPowerBudgetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerBudgetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerBudgetEntry.setStatus("current")
_CucsPowerBudgetInstanceId_Type = CucsManagedObjectId
_CucsPowerBudgetInstanceId_Object = MibTableColumn
cucsPowerBudgetInstanceId = _CucsPowerBudgetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 1),
    _CucsPowerBudgetInstanceId_Type()
)
cucsPowerBudgetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerBudgetInstanceId.setStatus("current")
_CucsPowerBudgetDn_Type = CucsManagedObjectDn
_CucsPowerBudgetDn_Object = MibTableColumn
cucsPowerBudgetDn = _CucsPowerBudgetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 2),
    _CucsPowerBudgetDn_Type()
)
cucsPowerBudgetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetDn.setStatus("current")
_CucsPowerBudgetRn_Type = SnmpAdminString
_CucsPowerBudgetRn_Object = MibTableColumn
cucsPowerBudgetRn = _CucsPowerBudgetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 3),
    _CucsPowerBudgetRn_Type()
)
cucsPowerBudgetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetRn.setStatus("current")
_CucsPowerBudgetAdminCommitted_Type = Gauge32
_CucsPowerBudgetAdminCommitted_Object = MibTableColumn
cucsPowerBudgetAdminCommitted = _CucsPowerBudgetAdminCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 4),
    _CucsPowerBudgetAdminCommitted_Type()
)
cucsPowerBudgetAdminCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetAdminCommitted.setStatus("current")
_CucsPowerBudgetAdminPeak_Type = Gauge32
_CucsPowerBudgetAdminPeak_Object = MibTableColumn
cucsPowerBudgetAdminPeak = _CucsPowerBudgetAdminPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 5),
    _CucsPowerBudgetAdminPeak_Type()
)
cucsPowerBudgetAdminPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetAdminPeak.setStatus("current")
_CucsPowerBudgetCurrentPower_Type = Gauge32
_CucsPowerBudgetCurrentPower_Object = MibTableColumn
cucsPowerBudgetCurrentPower = _CucsPowerBudgetCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 6),
    _CucsPowerBudgetCurrentPower_Type()
)
cucsPowerBudgetCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetCurrentPower.setStatus("current")
_CucsPowerBudgetGroupName_Type = SnmpAdminString
_CucsPowerBudgetGroupName_Object = MibTableColumn
cucsPowerBudgetGroupName = _CucsPowerBudgetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 7),
    _CucsPowerBudgetGroupName_Type()
)
cucsPowerBudgetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetGroupName.setStatus("current")
_CucsPowerBudgetIdlePower_Type = Gauge32
_CucsPowerBudgetIdlePower_Object = MibTableColumn
cucsPowerBudgetIdlePower = _CucsPowerBudgetIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 8),
    _CucsPowerBudgetIdlePower_Type()
)
cucsPowerBudgetIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetIdlePower.setStatus("current")
_CucsPowerBudgetMaxPower_Type = Gauge32
_CucsPowerBudgetMaxPower_Object = MibTableColumn
cucsPowerBudgetMaxPower = _CucsPowerBudgetMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 9),
    _CucsPowerBudgetMaxPower_Type()
)
cucsPowerBudgetMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetMaxPower.setStatus("current")
_CucsPowerBudgetMinPower_Type = Gauge32
_CucsPowerBudgetMinPower_Object = MibTableColumn
cucsPowerBudgetMinPower = _CucsPowerBudgetMinPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 10),
    _CucsPowerBudgetMinPower_Type()
)
cucsPowerBudgetMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetMinPower.setStatus("current")
_CucsPowerBudgetOperCommitted_Type = Gauge32
_CucsPowerBudgetOperCommitted_Object = MibTableColumn
cucsPowerBudgetOperCommitted = _CucsPowerBudgetOperCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 11),
    _CucsPowerBudgetOperCommitted_Type()
)
cucsPowerBudgetOperCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetOperCommitted.setStatus("current")
_CucsPowerBudgetOperMin_Type = Gauge32
_CucsPowerBudgetOperMin_Object = MibTableColumn
cucsPowerBudgetOperMin = _CucsPowerBudgetOperMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 12),
    _CucsPowerBudgetOperMin_Type()
)
cucsPowerBudgetOperMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetOperMin.setStatus("current")
_CucsPowerBudgetOperPeak_Type = Gauge32
_CucsPowerBudgetOperPeak_Object = MibTableColumn
cucsPowerBudgetOperPeak = _CucsPowerBudgetOperPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 13),
    _CucsPowerBudgetOperPeak_Type()
)
cucsPowerBudgetOperPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetOperPeak.setStatus("current")
_CucsPowerBudgetScaledWt_Type = Gauge32
_CucsPowerBudgetScaledWt_Object = MibTableColumn
cucsPowerBudgetScaledWt = _CucsPowerBudgetScaledWt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 14),
    _CucsPowerBudgetScaledWt_Type()
)
cucsPowerBudgetScaledWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetScaledWt.setStatus("current")
_CucsPowerBudgetOperState_Type = CucsPowerOperState
_CucsPowerBudgetOperState_Object = MibTableColumn
cucsPowerBudgetOperState = _CucsPowerBudgetOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 15),
    _CucsPowerBudgetOperState_Type()
)
cucsPowerBudgetOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetOperState.setStatus("current")
_CucsPowerBudgetDynRealloc_Type = CucsPowerReallocation
_CucsPowerBudgetDynRealloc_Object = MibTableColumn
cucsPowerBudgetDynRealloc = _CucsPowerBudgetDynRealloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 16),
    _CucsPowerBudgetDynRealloc_Type()
)
cucsPowerBudgetDynRealloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetDynRealloc.setStatus("current")
_CucsPowerBudgetPrio_Type = Gauge32
_CucsPowerBudgetPrio_Object = MibTableColumn
cucsPowerBudgetPrio = _CucsPowerBudgetPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 17),
    _CucsPowerBudgetPrio_Type()
)
cucsPowerBudgetPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPrio.setStatus("current")
_CucsPowerBudgetCatalogPower_Type = Gauge32
_CucsPowerBudgetCatalogPower_Object = MibTableColumn
cucsPowerBudgetCatalogPower = _CucsPowerBudgetCatalogPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 18),
    _CucsPowerBudgetCatalogPower_Type()
)
cucsPowerBudgetCatalogPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetCatalogPower.setStatus("current")
_CucsPowerBudgetUpdateTime_Type = DateAndTime
_CucsPowerBudgetUpdateTime_Object = MibTableColumn
cucsPowerBudgetUpdateTime = _CucsPowerBudgetUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 19),
    _CucsPowerBudgetUpdateTime_Type()
)
cucsPowerBudgetUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetUpdateTime.setStatus("current")
_CucsPowerBudgetCapAction_Type = CucsPowerCapAction
_CucsPowerBudgetCapAction_Object = MibTableColumn
cucsPowerBudgetCapAction = _CucsPowerBudgetCapAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 20),
    _CucsPowerBudgetCapAction_Type()
)
cucsPowerBudgetCapAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetCapAction.setStatus("current")
_CucsPowerBudgetWeight_Type = Gauge32
_CucsPowerBudgetWeight_Object = MibTableColumn
cucsPowerBudgetWeight = _CucsPowerBudgetWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 21),
    _CucsPowerBudgetWeight_Type()
)
cucsPowerBudgetWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetWeight.setStatus("current")
_CucsPowerBudgetPsuCapacity_Type = Gauge32
_CucsPowerBudgetPsuCapacity_Object = MibTableColumn
cucsPowerBudgetPsuCapacity = _CucsPowerBudgetPsuCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 22),
    _CucsPowerBudgetPsuCapacity_Type()
)
cucsPowerBudgetPsuCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPsuCapacity.setStatus("current")
_CucsPowerBudgetPsuState_Type = CucsPowerPsuState
_CucsPowerBudgetPsuState_Object = MibTableColumn
cucsPowerBudgetPsuState = _CucsPowerBudgetPsuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 23),
    _CucsPowerBudgetPsuState_Type()
)
cucsPowerBudgetPsuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPsuState.setStatus("current")
_CucsPowerBudgetStyle_Type = CucsPowerMgmtStyle
_CucsPowerBudgetStyle_Object = MibTableColumn
cucsPowerBudgetStyle = _CucsPowerBudgetStyle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 24),
    _CucsPowerBudgetStyle_Type()
)
cucsPowerBudgetStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetStyle.setStatus("current")
_CucsPowerBudgetAdminFPLockState_Type = CucsPowerLockState
_CucsPowerBudgetAdminFPLockState_Object = MibTableColumn
cucsPowerBudgetAdminFPLockState = _CucsPowerBudgetAdminFPLockState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 25),
    _CucsPowerBudgetAdminFPLockState_Type()
)
cucsPowerBudgetAdminFPLockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetAdminFPLockState.setStatus("current")
_CucsPowerBudgetAdminPeakNew_Type = Gauge32
_CucsPowerBudgetAdminPeakNew_Object = MibTableColumn
cucsPowerBudgetAdminPeakNew = _CucsPowerBudgetAdminPeakNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 26),
    _CucsPowerBudgetAdminPeakNew_Type()
)
cucsPowerBudgetAdminPeakNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetAdminPeakNew.setStatus("current")
_CucsPowerBudgetBootPower_Type = Gauge32
_CucsPowerBudgetBootPower_Object = MibTableColumn
cucsPowerBudgetBootPower = _CucsPowerBudgetBootPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 27),
    _CucsPowerBudgetBootPower_Type()
)
cucsPowerBudgetBootPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetBootPower.setStatus("current")
_CucsPowerBudgetChRsrvdPower_Type = Gauge32
_CucsPowerBudgetChRsrvdPower_Object = MibTableColumn
cucsPowerBudgetChRsrvdPower = _CucsPowerBudgetChRsrvdPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 28),
    _CucsPowerBudgetChRsrvdPower_Type()
)
cucsPowerBudgetChRsrvdPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetChRsrvdPower.setStatus("current")
_CucsPowerBudgetOperFPLockState_Type = CucsPowerLockState
_CucsPowerBudgetOperFPLockState_Object = MibTableColumn
cucsPowerBudgetOperFPLockState = _CucsPowerBudgetOperFPLockState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 29),
    _CucsPowerBudgetOperFPLockState_Type()
)
cucsPowerBudgetOperFPLockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetOperFPLockState.setStatus("current")
_CucsPowerBudgetOperProfMethod_Type = CucsPowerProfilingMethod
_CucsPowerBudgetOperProfMethod_Object = MibTableColumn
cucsPowerBudgetOperProfMethod = _CucsPowerBudgetOperProfMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 30),
    _CucsPowerBudgetOperProfMethod_Type()
)
cucsPowerBudgetOperProfMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetOperProfMethod.setStatus("current")
_CucsPowerBudgetProfMethod_Type = CucsPowerProfilingMethod
_CucsPowerBudgetProfMethod_Object = MibTableColumn
cucsPowerBudgetProfMethod = _CucsPowerBudgetProfMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 31),
    _CucsPowerBudgetProfMethod_Type()
)
cucsPowerBudgetProfMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetProfMethod.setStatus("current")
_CucsPowerBudgetProfiling_Type = TruthValue
_CucsPowerBudgetProfiling_Object = MibTableColumn
cucsPowerBudgetProfiling = _CucsPowerBudgetProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 32),
    _CucsPowerBudgetProfiling_Type()
)
cucsPowerBudgetProfiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetProfiling.setStatus("current")
_CucsPowerBudgetPsuLineMode_Type = CucsPowerPsuLineMode
_CucsPowerBudgetPsuLineMode_Object = MibTableColumn
cucsPowerBudgetPsuLineMode = _CucsPowerBudgetPsuLineMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 33),
    _CucsPowerBudgetPsuLineMode_Type()
)
cucsPowerBudgetPsuLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPsuLineMode.setStatus("current")
_CucsPowerBudgetPowerAvailState_Type = CucsPowerPowerAvailState
_CucsPowerBudgetPowerAvailState_Object = MibTableColumn
cucsPowerBudgetPowerAvailState = _CucsPowerBudgetPowerAvailState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 34),
    _CucsPowerBudgetPowerAvailState_Type()
)
cucsPowerBudgetPowerAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPowerAvailState.setStatus("current")
_CucsPowerBudgetPowerDeployState_Type = CucsPowerPowerDeployState
_CucsPowerBudgetPowerDeployState_Object = MibTableColumn
cucsPowerBudgetPowerDeployState = _CucsPowerBudgetPowerDeployState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 35),
    _CucsPowerBudgetPowerDeployState_Type()
)
cucsPowerBudgetPowerDeployState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPowerDeployState.setStatus("current")
_CucsPowerBudgetPowerOnDeploy_Type = TruthValue
_CucsPowerBudgetPowerOnDeploy_Object = MibTableColumn
cucsPowerBudgetPowerOnDeploy = _CucsPowerBudgetPowerOnDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 36),
    _CucsPowerBudgetPowerOnDeploy_Type()
)
cucsPowerBudgetPowerOnDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetPowerOnDeploy.setStatus("current")
_CucsPowerBudgetFanSpeed_Type = CucsPowerBudgetFanSpeed
_CucsPowerBudgetFanSpeed_Object = MibTableColumn
cucsPowerBudgetFanSpeed = _CucsPowerBudgetFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 1, 1, 37),
    _CucsPowerBudgetFanSpeed_Type()
)
cucsPowerBudgetFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerBudgetFanSpeed.setStatus("current")
_CucsPowerChassisMemberTable_Object = MibTable
cucsPowerChassisMemberTable = _CucsPowerChassisMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2)
)
if mibBuilder.loadTexts:
    cucsPowerChassisMemberTable.setStatus("current")
_CucsPowerChassisMemberEntry_Object = MibTableRow
cucsPowerChassisMemberEntry = _CucsPowerChassisMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2, 1)
)
cucsPowerChassisMemberEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerChassisMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerChassisMemberEntry.setStatus("current")
_CucsPowerChassisMemberInstanceId_Type = CucsManagedObjectId
_CucsPowerChassisMemberInstanceId_Object = MibTableColumn
cucsPowerChassisMemberInstanceId = _CucsPowerChassisMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2, 1, 1),
    _CucsPowerChassisMemberInstanceId_Type()
)
cucsPowerChassisMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerChassisMemberInstanceId.setStatus("current")
_CucsPowerChassisMemberDn_Type = CucsManagedObjectDn
_CucsPowerChassisMemberDn_Object = MibTableColumn
cucsPowerChassisMemberDn = _CucsPowerChassisMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2, 1, 2),
    _CucsPowerChassisMemberDn_Type()
)
cucsPowerChassisMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerChassisMemberDn.setStatus("current")
_CucsPowerChassisMemberRn_Type = SnmpAdminString
_CucsPowerChassisMemberRn_Object = MibTableColumn
cucsPowerChassisMemberRn = _CucsPowerChassisMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2, 1, 3),
    _CucsPowerChassisMemberRn_Type()
)
cucsPowerChassisMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerChassisMemberRn.setStatus("current")
_CucsPowerChassisMemberId_Type = Gauge32
_CucsPowerChassisMemberId_Object = MibTableColumn
cucsPowerChassisMemberId = _CucsPowerChassisMemberId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2, 1, 4),
    _CucsPowerChassisMemberId_Type()
)
cucsPowerChassisMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerChassisMemberId.setStatus("current")
_CucsPowerChassisMemberOperState_Type = CucsPowerMemberState
_CucsPowerChassisMemberOperState_Object = MibTableColumn
cucsPowerChassisMemberOperState = _CucsPowerChassisMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 2, 1, 5),
    _CucsPowerChassisMemberOperState_Type()
)
cucsPowerChassisMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerChassisMemberOperState.setStatus("current")
_CucsPowerEpTable_Object = MibTable
cucsPowerEpTable = _CucsPowerEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 3)
)
if mibBuilder.loadTexts:
    cucsPowerEpTable.setStatus("current")
_CucsPowerEpEntry_Object = MibTableRow
cucsPowerEpEntry = _CucsPowerEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 3, 1)
)
cucsPowerEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerEpEntry.setStatus("current")
_CucsPowerEpInstanceId_Type = CucsManagedObjectId
_CucsPowerEpInstanceId_Object = MibTableColumn
cucsPowerEpInstanceId = _CucsPowerEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 3, 1, 1),
    _CucsPowerEpInstanceId_Type()
)
cucsPowerEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerEpInstanceId.setStatus("current")
_CucsPowerEpDn_Type = CucsManagedObjectDn
_CucsPowerEpDn_Object = MibTableColumn
cucsPowerEpDn = _CucsPowerEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 3, 1, 2),
    _CucsPowerEpDn_Type()
)
cucsPowerEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerEpDn.setStatus("current")
_CucsPowerEpRn_Type = SnmpAdminString
_CucsPowerEpRn_Object = MibTableColumn
cucsPowerEpRn = _CucsPowerEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 3, 1, 3),
    _CucsPowerEpRn_Type()
)
cucsPowerEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerEpRn.setStatus("current")
_CucsPowerGroupTable_Object = MibTable
cucsPowerGroupTable = _CucsPowerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4)
)
if mibBuilder.loadTexts:
    cucsPowerGroupTable.setStatus("current")
_CucsPowerGroupEntry_Object = MibTableRow
cucsPowerGroupEntry = _CucsPowerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1)
)
cucsPowerGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerGroupEntry.setStatus("current")
_CucsPowerGroupInstanceId_Type = CucsManagedObjectId
_CucsPowerGroupInstanceId_Object = MibTableColumn
cucsPowerGroupInstanceId = _CucsPowerGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 1),
    _CucsPowerGroupInstanceId_Type()
)
cucsPowerGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerGroupInstanceId.setStatus("current")
_CucsPowerGroupDn_Type = CucsManagedObjectDn
_CucsPowerGroupDn_Object = MibTableColumn
cucsPowerGroupDn = _CucsPowerGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 2),
    _CucsPowerGroupDn_Type()
)
cucsPowerGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupDn.setStatus("current")
_CucsPowerGroupRn_Type = SnmpAdminString
_CucsPowerGroupRn_Object = MibTableColumn
cucsPowerGroupRn = _CucsPowerGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 3),
    _CucsPowerGroupRn_Type()
)
cucsPowerGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupRn.setStatus("current")
_CucsPowerGroupRealloc_Type = CucsPowerReallocation
_CucsPowerGroupRealloc_Object = MibTableColumn
cucsPowerGroupRealloc = _CucsPowerGroupRealloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 4),
    _CucsPowerGroupRealloc_Type()
)
cucsPowerGroupRealloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupRealloc.setStatus("current")
_CucsPowerGroupAdminCommitted_Type = Gauge32
_CucsPowerGroupAdminCommitted_Object = MibTableColumn
cucsPowerGroupAdminCommitted = _CucsPowerGroupAdminCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 5),
    _CucsPowerGroupAdminCommitted_Type()
)
cucsPowerGroupAdminCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdminCommitted.setStatus("current")
_CucsPowerGroupAdminPeak_Type = Gauge32
_CucsPowerGroupAdminPeak_Object = MibTableColumn
cucsPowerGroupAdminPeak = _CucsPowerGroupAdminPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 6),
    _CucsPowerGroupAdminPeak_Type()
)
cucsPowerGroupAdminPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdminPeak.setStatus("current")
_CucsPowerGroupCurrentPower_Type = Gauge32
_CucsPowerGroupCurrentPower_Object = MibTableColumn
cucsPowerGroupCurrentPower = _CucsPowerGroupCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 7),
    _CucsPowerGroupCurrentPower_Type()
)
cucsPowerGroupCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupCurrentPower.setStatus("current")
_CucsPowerGroupDescr_Type = SnmpAdminString
_CucsPowerGroupDescr_Object = MibTableColumn
cucsPowerGroupDescr = _CucsPowerGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 8),
    _CucsPowerGroupDescr_Type()
)
cucsPowerGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupDescr.setStatus("current")
_CucsPowerGroupFltAggr_Type = Unsigned64
_CucsPowerGroupFltAggr_Object = MibTableColumn
cucsPowerGroupFltAggr = _CucsPowerGroupFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 9),
    _CucsPowerGroupFltAggr_Type()
)
cucsPowerGroupFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupFltAggr.setStatus("current")
_CucsPowerGroupCurReqPower_Type = Gauge32
_CucsPowerGroupCurReqPower_Object = MibTableColumn
cucsPowerGroupCurReqPower = _CucsPowerGroupCurReqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 10),
    _CucsPowerGroupCurReqPower_Type()
)
cucsPowerGroupCurReqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupCurReqPower.setStatus("current")
_CucsPowerGroupMinReqPower_Type = Gauge32
_CucsPowerGroupMinReqPower_Object = MibTableColumn
cucsPowerGroupMinReqPower = _CucsPowerGroupMinReqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 11),
    _CucsPowerGroupMinReqPower_Type()
)
cucsPowerGroupMinReqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupMinReqPower.setStatus("current")
_CucsPowerGroupIntId_Type = SnmpAdminString
_CucsPowerGroupIntId_Object = MibTableColumn
cucsPowerGroupIntId = _CucsPowerGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 12),
    _CucsPowerGroupIntId_Type()
)
cucsPowerGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupIntId.setStatus("current")
_CucsPowerGroupName_Type = SnmpAdminString
_CucsPowerGroupName_Object = MibTableColumn
cucsPowerGroupName = _CucsPowerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 13),
    _CucsPowerGroupName_Type()
)
cucsPowerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupName.setStatus("current")
_CucsPowerGroupQualifier_Type = SnmpAdminString
_CucsPowerGroupQualifier_Object = MibTableColumn
cucsPowerGroupQualifier = _CucsPowerGroupQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 14),
    _CucsPowerGroupQualifier_Type()
)
cucsPowerGroupQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupQualifier.setStatus("current")
_CucsPowerGroupOperCommitted_Type = Gauge32
_CucsPowerGroupOperCommitted_Object = MibTableColumn
cucsPowerGroupOperCommitted = _CucsPowerGroupOperCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 15),
    _CucsPowerGroupOperCommitted_Type()
)
cucsPowerGroupOperCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupOperCommitted.setStatus("current")
_CucsPowerGroupOperPeak_Type = Gauge32
_CucsPowerGroupOperPeak_Object = MibTableColumn
cucsPowerGroupOperPeak = _CucsPowerGroupOperPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 16),
    _CucsPowerGroupOperPeak_Type()
)
cucsPowerGroupOperPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupOperPeak.setStatus("current")
_CucsPowerGroupOperState_Type = CucsPowerGroupState
_CucsPowerGroupOperState_Object = MibTableColumn
cucsPowerGroupOperState = _CucsPowerGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 17),
    _CucsPowerGroupOperState_Type()
)
cucsPowerGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupOperState.setStatus("current")
_CucsPowerGroupPolicyLevel_Type = Gauge32
_CucsPowerGroupPolicyLevel_Object = MibTableColumn
cucsPowerGroupPolicyLevel = _CucsPowerGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 18),
    _CucsPowerGroupPolicyLevel_Type()
)
cucsPowerGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupPolicyLevel.setStatus("current")
_CucsPowerGroupPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPowerGroupPolicyOwner_Object = MibTableColumn
cucsPowerGroupPolicyOwner = _CucsPowerGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 4, 1, 19),
    _CucsPowerGroupPolicyOwner_Type()
)
cucsPowerGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupPolicyOwner.setStatus("current")
_CucsPowerGroupAdditionPolicyTable_Object = MibTable
cucsPowerGroupAdditionPolicyTable = _CucsPowerGroupAdditionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5)
)
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyTable.setStatus("current")
_CucsPowerGroupAdditionPolicyEntry_Object = MibTableRow
cucsPowerGroupAdditionPolicyEntry = _CucsPowerGroupAdditionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1)
)
cucsPowerGroupAdditionPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerGroupAdditionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyEntry.setStatus("current")
_CucsPowerGroupAdditionPolicyInstanceId_Type = CucsManagedObjectId
_CucsPowerGroupAdditionPolicyInstanceId_Object = MibTableColumn
cucsPowerGroupAdditionPolicyInstanceId = _CucsPowerGroupAdditionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 1),
    _CucsPowerGroupAdditionPolicyInstanceId_Type()
)
cucsPowerGroupAdditionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyInstanceId.setStatus("current")
_CucsPowerGroupAdditionPolicyDn_Type = CucsManagedObjectDn
_CucsPowerGroupAdditionPolicyDn_Object = MibTableColumn
cucsPowerGroupAdditionPolicyDn = _CucsPowerGroupAdditionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 2),
    _CucsPowerGroupAdditionPolicyDn_Type()
)
cucsPowerGroupAdditionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyDn.setStatus("current")
_CucsPowerGroupAdditionPolicyRn_Type = SnmpAdminString
_CucsPowerGroupAdditionPolicyRn_Object = MibTableColumn
cucsPowerGroupAdditionPolicyRn = _CucsPowerGroupAdditionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 3),
    _CucsPowerGroupAdditionPolicyRn_Type()
)
cucsPowerGroupAdditionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyRn.setStatus("current")
_CucsPowerGroupAdditionPolicyAction_Type = CucsPowerChThrAction
_CucsPowerGroupAdditionPolicyAction_Object = MibTableColumn
cucsPowerGroupAdditionPolicyAction = _CucsPowerGroupAdditionPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 4),
    _CucsPowerGroupAdditionPolicyAction_Type()
)
cucsPowerGroupAdditionPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyAction.setStatus("current")
_CucsPowerGroupAdditionPolicyDescr_Type = SnmpAdminString
_CucsPowerGroupAdditionPolicyDescr_Object = MibTableColumn
cucsPowerGroupAdditionPolicyDescr = _CucsPowerGroupAdditionPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 5),
    _CucsPowerGroupAdditionPolicyDescr_Type()
)
cucsPowerGroupAdditionPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyDescr.setStatus("current")
_CucsPowerGroupAdditionPolicyIntId_Type = SnmpAdminString
_CucsPowerGroupAdditionPolicyIntId_Object = MibTableColumn
cucsPowerGroupAdditionPolicyIntId = _CucsPowerGroupAdditionPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 6),
    _CucsPowerGroupAdditionPolicyIntId_Type()
)
cucsPowerGroupAdditionPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyIntId.setStatus("current")
_CucsPowerGroupAdditionPolicyName_Type = SnmpAdminString
_CucsPowerGroupAdditionPolicyName_Object = MibTableColumn
cucsPowerGroupAdditionPolicyName = _CucsPowerGroupAdditionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 7),
    _CucsPowerGroupAdditionPolicyName_Type()
)
cucsPowerGroupAdditionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyName.setStatus("current")
_CucsPowerGroupAdditionPolicyPolicyLevel_Type = Gauge32
_CucsPowerGroupAdditionPolicyPolicyLevel_Object = MibTableColumn
cucsPowerGroupAdditionPolicyPolicyLevel = _CucsPowerGroupAdditionPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 8),
    _CucsPowerGroupAdditionPolicyPolicyLevel_Type()
)
cucsPowerGroupAdditionPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyPolicyLevel.setStatus("current")
_CucsPowerGroupAdditionPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPowerGroupAdditionPolicyPolicyOwner_Object = MibTableColumn
cucsPowerGroupAdditionPolicyPolicyOwner = _CucsPowerGroupAdditionPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 5, 1, 9),
    _CucsPowerGroupAdditionPolicyPolicyOwner_Type()
)
cucsPowerGroupAdditionPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupAdditionPolicyPolicyOwner.setStatus("current")
_CucsPowerGroupQualTable_Object = MibTable
cucsPowerGroupQualTable = _CucsPowerGroupQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 6)
)
if mibBuilder.loadTexts:
    cucsPowerGroupQualTable.setStatus("current")
_CucsPowerGroupQualEntry_Object = MibTableRow
cucsPowerGroupQualEntry = _CucsPowerGroupQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 6, 1)
)
cucsPowerGroupQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerGroupQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerGroupQualEntry.setStatus("current")
_CucsPowerGroupQualInstanceId_Type = CucsManagedObjectId
_CucsPowerGroupQualInstanceId_Object = MibTableColumn
cucsPowerGroupQualInstanceId = _CucsPowerGroupQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 6, 1, 1),
    _CucsPowerGroupQualInstanceId_Type()
)
cucsPowerGroupQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerGroupQualInstanceId.setStatus("current")
_CucsPowerGroupQualDn_Type = CucsManagedObjectDn
_CucsPowerGroupQualDn_Object = MibTableColumn
cucsPowerGroupQualDn = _CucsPowerGroupQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 6, 1, 2),
    _CucsPowerGroupQualDn_Type()
)
cucsPowerGroupQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupQualDn.setStatus("current")
_CucsPowerGroupQualRn_Type = SnmpAdminString
_CucsPowerGroupQualRn_Object = MibTableColumn
cucsPowerGroupQualRn = _CucsPowerGroupQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 6, 1, 3),
    _CucsPowerGroupQualRn_Type()
)
cucsPowerGroupQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupQualRn.setStatus("current")
_CucsPowerGroupQualGroupName_Type = SnmpAdminString
_CucsPowerGroupQualGroupName_Object = MibTableColumn
cucsPowerGroupQualGroupName = _CucsPowerGroupQualGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 6, 1, 4),
    _CucsPowerGroupQualGroupName_Type()
)
cucsPowerGroupQualGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupQualGroupName.setStatus("current")
_CucsPowerGroupStatsTable_Object = MibTable
cucsPowerGroupStatsTable = _CucsPowerGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7)
)
if mibBuilder.loadTexts:
    cucsPowerGroupStatsTable.setStatus("current")
_CucsPowerGroupStatsEntry_Object = MibTableRow
cucsPowerGroupStatsEntry = _CucsPowerGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1)
)
cucsPowerGroupStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerGroupStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerGroupStatsEntry.setStatus("current")
_CucsPowerGroupStatsInstanceId_Type = CucsManagedObjectId
_CucsPowerGroupStatsInstanceId_Object = MibTableColumn
cucsPowerGroupStatsInstanceId = _CucsPowerGroupStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 1),
    _CucsPowerGroupStatsInstanceId_Type()
)
cucsPowerGroupStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsInstanceId.setStatus("current")
_CucsPowerGroupStatsDn_Type = CucsManagedObjectDn
_CucsPowerGroupStatsDn_Object = MibTableColumn
cucsPowerGroupStatsDn = _CucsPowerGroupStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 2),
    _CucsPowerGroupStatsDn_Type()
)
cucsPowerGroupStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsDn.setStatus("current")
_CucsPowerGroupStatsRn_Type = SnmpAdminString
_CucsPowerGroupStatsRn_Object = MibTableColumn
cucsPowerGroupStatsRn = _CucsPowerGroupStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 3),
    _CucsPowerGroupStatsRn_Type()
)
cucsPowerGroupStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsRn.setStatus("current")
_CucsPowerGroupStatsIntervals_Type = Gauge32
_CucsPowerGroupStatsIntervals_Object = MibTableColumn
cucsPowerGroupStatsIntervals = _CucsPowerGroupStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 4),
    _CucsPowerGroupStatsIntervals_Type()
)
cucsPowerGroupStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsIntervals.setStatus("current")
_CucsPowerGroupStatsPower_Type = Integer32
_CucsPowerGroupStatsPower_Object = MibTableColumn
cucsPowerGroupStatsPower = _CucsPowerGroupStatsPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 5),
    _CucsPowerGroupStatsPower_Type()
)
cucsPowerGroupStatsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsPower.setStatus("current")
_CucsPowerGroupStatsPowerAvg_Type = Integer32
_CucsPowerGroupStatsPowerAvg_Object = MibTableColumn
cucsPowerGroupStatsPowerAvg = _CucsPowerGroupStatsPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 6),
    _CucsPowerGroupStatsPowerAvg_Type()
)
cucsPowerGroupStatsPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsPowerAvg.setStatus("current")
_CucsPowerGroupStatsPowerMax_Type = Integer32
_CucsPowerGroupStatsPowerMax_Object = MibTableColumn
cucsPowerGroupStatsPowerMax = _CucsPowerGroupStatsPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 7),
    _CucsPowerGroupStatsPowerMax_Type()
)
cucsPowerGroupStatsPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsPowerMax.setStatus("current")
_CucsPowerGroupStatsPowerMin_Type = Integer32
_CucsPowerGroupStatsPowerMin_Object = MibTableColumn
cucsPowerGroupStatsPowerMin = _CucsPowerGroupStatsPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 8),
    _CucsPowerGroupStatsPowerMin_Type()
)
cucsPowerGroupStatsPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsPowerMin.setStatus("current")
_CucsPowerGroupStatsSuspect_Type = TruthValue
_CucsPowerGroupStatsSuspect_Object = MibTableColumn
cucsPowerGroupStatsSuspect = _CucsPowerGroupStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 9),
    _CucsPowerGroupStatsSuspect_Type()
)
cucsPowerGroupStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsSuspect.setStatus("current")
_CucsPowerGroupStatsThresholded_Type = CucsPowerGroupStatsThresholded
_CucsPowerGroupStatsThresholded_Object = MibTableColumn
cucsPowerGroupStatsThresholded = _CucsPowerGroupStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 10),
    _CucsPowerGroupStatsThresholded_Type()
)
cucsPowerGroupStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsThresholded.setStatus("current")
_CucsPowerGroupStatsTimeCollected_Type = DateAndTime
_CucsPowerGroupStatsTimeCollected_Object = MibTableColumn
cucsPowerGroupStatsTimeCollected = _CucsPowerGroupStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 11),
    _CucsPowerGroupStatsTimeCollected_Type()
)
cucsPowerGroupStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsTimeCollected.setStatus("current")
_CucsPowerGroupStatsUpdate_Type = Gauge32
_CucsPowerGroupStatsUpdate_Object = MibTableColumn
cucsPowerGroupStatsUpdate = _CucsPowerGroupStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 7, 1, 12),
    _CucsPowerGroupStatsUpdate_Type()
)
cucsPowerGroupStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsUpdate.setStatus("current")
_CucsPowerGroupStatsHistTable_Object = MibTable
cucsPowerGroupStatsHistTable = _CucsPowerGroupStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8)
)
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistTable.setStatus("current")
_CucsPowerGroupStatsHistEntry_Object = MibTableRow
cucsPowerGroupStatsHistEntry = _CucsPowerGroupStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1)
)
cucsPowerGroupStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerGroupStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistEntry.setStatus("current")
_CucsPowerGroupStatsHistInstanceId_Type = CucsManagedObjectId
_CucsPowerGroupStatsHistInstanceId_Object = MibTableColumn
cucsPowerGroupStatsHistInstanceId = _CucsPowerGroupStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 1),
    _CucsPowerGroupStatsHistInstanceId_Type()
)
cucsPowerGroupStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistInstanceId.setStatus("current")
_CucsPowerGroupStatsHistDn_Type = CucsManagedObjectDn
_CucsPowerGroupStatsHistDn_Object = MibTableColumn
cucsPowerGroupStatsHistDn = _CucsPowerGroupStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 2),
    _CucsPowerGroupStatsHistDn_Type()
)
cucsPowerGroupStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistDn.setStatus("current")
_CucsPowerGroupStatsHistRn_Type = SnmpAdminString
_CucsPowerGroupStatsHistRn_Object = MibTableColumn
cucsPowerGroupStatsHistRn = _CucsPowerGroupStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 3),
    _CucsPowerGroupStatsHistRn_Type()
)
cucsPowerGroupStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistRn.setStatus("current")
_CucsPowerGroupStatsHistId_Type = Unsigned64
_CucsPowerGroupStatsHistId_Object = MibTableColumn
cucsPowerGroupStatsHistId = _CucsPowerGroupStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 4),
    _CucsPowerGroupStatsHistId_Type()
)
cucsPowerGroupStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistId.setStatus("current")
_CucsPowerGroupStatsHistMostRecent_Type = TruthValue
_CucsPowerGroupStatsHistMostRecent_Object = MibTableColumn
cucsPowerGroupStatsHistMostRecent = _CucsPowerGroupStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 5),
    _CucsPowerGroupStatsHistMostRecent_Type()
)
cucsPowerGroupStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistMostRecent.setStatus("current")
_CucsPowerGroupStatsHistPower_Type = Integer32
_CucsPowerGroupStatsHistPower_Object = MibTableColumn
cucsPowerGroupStatsHistPower = _CucsPowerGroupStatsHistPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 6),
    _CucsPowerGroupStatsHistPower_Type()
)
cucsPowerGroupStatsHistPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistPower.setStatus("current")
_CucsPowerGroupStatsHistPowerAvg_Type = Integer32
_CucsPowerGroupStatsHistPowerAvg_Object = MibTableColumn
cucsPowerGroupStatsHistPowerAvg = _CucsPowerGroupStatsHistPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 7),
    _CucsPowerGroupStatsHistPowerAvg_Type()
)
cucsPowerGroupStatsHistPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistPowerAvg.setStatus("current")
_CucsPowerGroupStatsHistPowerMax_Type = Integer32
_CucsPowerGroupStatsHistPowerMax_Object = MibTableColumn
cucsPowerGroupStatsHistPowerMax = _CucsPowerGroupStatsHistPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 8),
    _CucsPowerGroupStatsHistPowerMax_Type()
)
cucsPowerGroupStatsHistPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistPowerMax.setStatus("current")
_CucsPowerGroupStatsHistPowerMin_Type = Integer32
_CucsPowerGroupStatsHistPowerMin_Object = MibTableColumn
cucsPowerGroupStatsHistPowerMin = _CucsPowerGroupStatsHistPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 9),
    _CucsPowerGroupStatsHistPowerMin_Type()
)
cucsPowerGroupStatsHistPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistPowerMin.setStatus("current")
_CucsPowerGroupStatsHistSuspect_Type = TruthValue
_CucsPowerGroupStatsHistSuspect_Object = MibTableColumn
cucsPowerGroupStatsHistSuspect = _CucsPowerGroupStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 10),
    _CucsPowerGroupStatsHistSuspect_Type()
)
cucsPowerGroupStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistSuspect.setStatus("current")
_CucsPowerGroupStatsHistThresholded_Type = CucsPowerGroupStatsHistThresholded
_CucsPowerGroupStatsHistThresholded_Object = MibTableColumn
cucsPowerGroupStatsHistThresholded = _CucsPowerGroupStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 11),
    _CucsPowerGroupStatsHistThresholded_Type()
)
cucsPowerGroupStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistThresholded.setStatus("current")
_CucsPowerGroupStatsHistTimeCollected_Type = DateAndTime
_CucsPowerGroupStatsHistTimeCollected_Object = MibTableColumn
cucsPowerGroupStatsHistTimeCollected = _CucsPowerGroupStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 8, 1, 12),
    _CucsPowerGroupStatsHistTimeCollected_Type()
)
cucsPowerGroupStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerGroupStatsHistTimeCollected.setStatus("current")
_CucsPowerPlacementTable_Object = MibTable
cucsPowerPlacementTable = _CucsPowerPlacementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9)
)
if mibBuilder.loadTexts:
    cucsPowerPlacementTable.setStatus("current")
_CucsPowerPlacementEntry_Object = MibTableRow
cucsPowerPlacementEntry = _CucsPowerPlacementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1)
)
cucsPowerPlacementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerPlacementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerPlacementEntry.setStatus("current")
_CucsPowerPlacementInstanceId_Type = CucsManagedObjectId
_CucsPowerPlacementInstanceId_Object = MibTableColumn
cucsPowerPlacementInstanceId = _CucsPowerPlacementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 1),
    _CucsPowerPlacementInstanceId_Type()
)
cucsPowerPlacementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerPlacementInstanceId.setStatus("current")
_CucsPowerPlacementDn_Type = CucsManagedObjectDn
_CucsPowerPlacementDn_Object = MibTableColumn
cucsPowerPlacementDn = _CucsPowerPlacementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 2),
    _CucsPowerPlacementDn_Type()
)
cucsPowerPlacementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementDn.setStatus("current")
_CucsPowerPlacementRn_Type = SnmpAdminString
_CucsPowerPlacementRn_Object = MibTableColumn
cucsPowerPlacementRn = _CucsPowerPlacementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 3),
    _CucsPowerPlacementRn_Type()
)
cucsPowerPlacementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementRn.setStatus("current")
_CucsPowerPlacementDescr_Type = SnmpAdminString
_CucsPowerPlacementDescr_Object = MibTableColumn
cucsPowerPlacementDescr = _CucsPowerPlacementDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 4),
    _CucsPowerPlacementDescr_Type()
)
cucsPowerPlacementDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementDescr.setStatus("current")
_CucsPowerPlacementIntId_Type = SnmpAdminString
_CucsPowerPlacementIntId_Object = MibTableColumn
cucsPowerPlacementIntId = _CucsPowerPlacementIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 5),
    _CucsPowerPlacementIntId_Type()
)
cucsPowerPlacementIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementIntId.setStatus("current")
_CucsPowerPlacementName_Type = SnmpAdminString
_CucsPowerPlacementName_Object = MibTableColumn
cucsPowerPlacementName = _CucsPowerPlacementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 6),
    _CucsPowerPlacementName_Type()
)
cucsPowerPlacementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementName.setStatus("current")
_CucsPowerPlacementPeerReqConflict_Type = CucsPowerReqConflict
_CucsPowerPlacementPeerReqConflict_Object = MibTableColumn
cucsPowerPlacementPeerReqConflict = _CucsPowerPlacementPeerReqConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 7),
    _CucsPowerPlacementPeerReqConflict_Type()
)
cucsPowerPlacementPeerReqConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementPeerReqConflict.setStatus("current")
_CucsPowerPlacementPgName_Type = SnmpAdminString
_CucsPowerPlacementPgName_Object = MibTableColumn
cucsPowerPlacementPgName = _CucsPowerPlacementPgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 8),
    _CucsPowerPlacementPgName_Type()
)
cucsPowerPlacementPgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementPgName.setStatus("current")
_CucsPowerPlacementPrioShare_Type = CucsPowerPrioritySharing
_CucsPowerPlacementPrioShare_Object = MibTableColumn
cucsPowerPlacementPrioShare = _CucsPowerPlacementPrioShare_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 9),
    _CucsPowerPlacementPrioShare_Type()
)
cucsPowerPlacementPrioShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementPrioShare.setStatus("current")
_CucsPowerPlacementSelfReqConflict_Type = CucsPowerReqConflict
_CucsPowerPlacementSelfReqConflict_Object = MibTableColumn
cucsPowerPlacementSelfReqConflict = _CucsPowerPlacementSelfReqConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 10),
    _CucsPowerPlacementSelfReqConflict_Type()
)
cucsPowerPlacementSelfReqConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementSelfReqConflict.setStatus("current")
_CucsPowerPlacementPolicyLevel_Type = Gauge32
_CucsPowerPlacementPolicyLevel_Object = MibTableColumn
cucsPowerPlacementPolicyLevel = _CucsPowerPlacementPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 11),
    _CucsPowerPlacementPolicyLevel_Type()
)
cucsPowerPlacementPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementPolicyLevel.setStatus("current")
_CucsPowerPlacementPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPowerPlacementPolicyOwner_Object = MibTableColumn
cucsPowerPlacementPolicyOwner = _CucsPowerPlacementPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 9, 1, 12),
    _CucsPowerPlacementPolicyOwner_Type()
)
cucsPowerPlacementPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPlacementPolicyOwner.setStatus("current")
_CucsPowerPolicyTable_Object = MibTable
cucsPowerPolicyTable = _CucsPowerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10)
)
if mibBuilder.loadTexts:
    cucsPowerPolicyTable.setStatus("current")
_CucsPowerPolicyEntry_Object = MibTableRow
cucsPowerPolicyEntry = _CucsPowerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1)
)
cucsPowerPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerPolicyEntry.setStatus("current")
_CucsPowerPolicyInstanceId_Type = CucsManagedObjectId
_CucsPowerPolicyInstanceId_Object = MibTableColumn
cucsPowerPolicyInstanceId = _CucsPowerPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 1),
    _CucsPowerPolicyInstanceId_Type()
)
cucsPowerPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerPolicyInstanceId.setStatus("current")
_CucsPowerPolicyDn_Type = CucsManagedObjectDn
_CucsPowerPolicyDn_Object = MibTableColumn
cucsPowerPolicyDn = _CucsPowerPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 2),
    _CucsPowerPolicyDn_Type()
)
cucsPowerPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyDn.setStatus("current")
_CucsPowerPolicyRn_Type = SnmpAdminString
_CucsPowerPolicyRn_Object = MibTableColumn
cucsPowerPolicyRn = _CucsPowerPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 3),
    _CucsPowerPolicyRn_Type()
)
cucsPowerPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyRn.setStatus("current")
_CucsPowerPolicyDescr_Type = SnmpAdminString
_CucsPowerPolicyDescr_Object = MibTableColumn
cucsPowerPolicyDescr = _CucsPowerPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 4),
    _CucsPowerPolicyDescr_Type()
)
cucsPowerPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyDescr.setStatus("current")
_CucsPowerPolicyIntId_Type = SnmpAdminString
_CucsPowerPolicyIntId_Object = MibTableColumn
cucsPowerPolicyIntId = _CucsPowerPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 5),
    _CucsPowerPolicyIntId_Type()
)
cucsPowerPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyIntId.setStatus("current")
_CucsPowerPolicyName_Type = SnmpAdminString
_CucsPowerPolicyName_Object = MibTableColumn
cucsPowerPolicyName = _CucsPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 6),
    _CucsPowerPolicyName_Type()
)
cucsPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyName.setStatus("current")
_CucsPowerPolicyOperPrio_Type = Gauge32
_CucsPowerPolicyOperPrio_Object = MibTableColumn
cucsPowerPolicyOperPrio = _CucsPowerPolicyOperPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 7),
    _CucsPowerPolicyOperPrio_Type()
)
cucsPowerPolicyOperPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyOperPrio.setStatus("current")
_CucsPowerPolicyPrio_Type = Gauge32
_CucsPowerPolicyPrio_Object = MibTableColumn
cucsPowerPolicyPrio = _CucsPowerPolicyPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 8),
    _CucsPowerPolicyPrio_Type()
)
cucsPowerPolicyPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyPrio.setStatus("current")
_CucsPowerPolicyPolicyLevel_Type = Gauge32
_CucsPowerPolicyPolicyLevel_Object = MibTableColumn
cucsPowerPolicyPolicyLevel = _CucsPowerPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 9),
    _CucsPowerPolicyPolicyLevel_Type()
)
cucsPowerPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyPolicyLevel.setStatus("current")
_CucsPowerPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPowerPolicyPolicyOwner_Object = MibTableColumn
cucsPowerPolicyPolicyOwner = _CucsPowerPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 10),
    _CucsPowerPolicyPolicyOwner_Type()
)
cucsPowerPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyPolicyOwner.setStatus("current")
_CucsPowerPolicyPropAcl_Type = Unsigned64
_CucsPowerPolicyPropAcl_Object = MibTableColumn
cucsPowerPolicyPropAcl = _CucsPowerPolicyPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 11),
    _CucsPowerPolicyPropAcl_Type()
)
cucsPowerPolicyPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyPropAcl.setStatus("current")
_CucsPowerPolicyFanSpeed_Type = CucsPowerPolicyFanSpeed
_CucsPowerPolicyFanSpeed_Object = MibTableColumn
cucsPowerPolicyFanSpeed = _CucsPowerPolicyFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 10, 1, 12),
    _CucsPowerPolicyFanSpeed_Type()
)
cucsPowerPolicyFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPolicyFanSpeed.setStatus("current")
_CucsPowerPrioWghtTable_Object = MibTable
cucsPowerPrioWghtTable = _CucsPowerPrioWghtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11)
)
if mibBuilder.loadTexts:
    cucsPowerPrioWghtTable.setStatus("current")
_CucsPowerPrioWghtEntry_Object = MibTableRow
cucsPowerPrioWghtEntry = _CucsPowerPrioWghtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11, 1)
)
cucsPowerPrioWghtEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerPrioWghtInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerPrioWghtEntry.setStatus("current")
_CucsPowerPrioWghtInstanceId_Type = CucsManagedObjectId
_CucsPowerPrioWghtInstanceId_Object = MibTableColumn
cucsPowerPrioWghtInstanceId = _CucsPowerPrioWghtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11, 1, 1),
    _CucsPowerPrioWghtInstanceId_Type()
)
cucsPowerPrioWghtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerPrioWghtInstanceId.setStatus("current")
_CucsPowerPrioWghtDn_Type = CucsManagedObjectDn
_CucsPowerPrioWghtDn_Object = MibTableColumn
cucsPowerPrioWghtDn = _CucsPowerPrioWghtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11, 1, 2),
    _CucsPowerPrioWghtDn_Type()
)
cucsPowerPrioWghtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPrioWghtDn.setStatus("current")
_CucsPowerPrioWghtRn_Type = SnmpAdminString
_CucsPowerPrioWghtRn_Object = MibTableColumn
cucsPowerPrioWghtRn = _CucsPowerPrioWghtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11, 1, 3),
    _CucsPowerPrioWghtRn_Type()
)
cucsPowerPrioWghtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPrioWghtRn.setStatus("current")
_CucsPowerPrioWghtPrio_Type = Gauge32
_CucsPowerPrioWghtPrio_Object = MibTableColumn
cucsPowerPrioWghtPrio = _CucsPowerPrioWghtPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11, 1, 4),
    _CucsPowerPrioWghtPrio_Type()
)
cucsPowerPrioWghtPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPrioWghtPrio.setStatus("current")
_CucsPowerPrioWghtWeight_Type = Gauge32
_CucsPowerPrioWghtWeight_Object = MibTableColumn
cucsPowerPrioWghtWeight = _CucsPowerPrioWghtWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 11, 1, 5),
    _CucsPowerPrioWghtWeight_Type()
)
cucsPowerPrioWghtWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerPrioWghtWeight.setStatus("current")
_CucsPowerRackUnitMemberTable_Object = MibTable
cucsPowerRackUnitMemberTable = _CucsPowerRackUnitMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12)
)
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberTable.setStatus("current")
_CucsPowerRackUnitMemberEntry_Object = MibTableRow
cucsPowerRackUnitMemberEntry = _CucsPowerRackUnitMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12, 1)
)
cucsPowerRackUnitMemberEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerRackUnitMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberEntry.setStatus("current")
_CucsPowerRackUnitMemberInstanceId_Type = CucsManagedObjectId
_CucsPowerRackUnitMemberInstanceId_Object = MibTableColumn
cucsPowerRackUnitMemberInstanceId = _CucsPowerRackUnitMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12, 1, 1),
    _CucsPowerRackUnitMemberInstanceId_Type()
)
cucsPowerRackUnitMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberInstanceId.setStatus("current")
_CucsPowerRackUnitMemberDn_Type = CucsManagedObjectDn
_CucsPowerRackUnitMemberDn_Object = MibTableColumn
cucsPowerRackUnitMemberDn = _CucsPowerRackUnitMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12, 1, 2),
    _CucsPowerRackUnitMemberDn_Type()
)
cucsPowerRackUnitMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberDn.setStatus("current")
_CucsPowerRackUnitMemberRn_Type = SnmpAdminString
_CucsPowerRackUnitMemberRn_Object = MibTableColumn
cucsPowerRackUnitMemberRn = _CucsPowerRackUnitMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12, 1, 3),
    _CucsPowerRackUnitMemberRn_Type()
)
cucsPowerRackUnitMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberRn.setStatus("current")
_CucsPowerRackUnitMemberId_Type = Gauge32
_CucsPowerRackUnitMemberId_Object = MibTableColumn
cucsPowerRackUnitMemberId = _CucsPowerRackUnitMemberId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12, 1, 4),
    _CucsPowerRackUnitMemberId_Type()
)
cucsPowerRackUnitMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberId.setStatus("current")
_CucsPowerRackUnitMemberOperState_Type = CucsPowerMemberState
_CucsPowerRackUnitMemberOperState_Object = MibTableColumn
cucsPowerRackUnitMemberOperState = _CucsPowerRackUnitMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 12, 1, 5),
    _CucsPowerRackUnitMemberOperState_Type()
)
cucsPowerRackUnitMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerRackUnitMemberOperState.setStatus("current")
_CucsPowerMgmtPolicyTable_Object = MibTable
cucsPowerMgmtPolicyTable = _CucsPowerMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13)
)
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyTable.setStatus("current")
_CucsPowerMgmtPolicyEntry_Object = MibTableRow
cucsPowerMgmtPolicyEntry = _CucsPowerMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1)
)
cucsPowerMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyEntry.setStatus("current")
_CucsPowerMgmtPolicyInstanceId_Type = CucsManagedObjectId
_CucsPowerMgmtPolicyInstanceId_Object = MibTableColumn
cucsPowerMgmtPolicyInstanceId = _CucsPowerMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 1),
    _CucsPowerMgmtPolicyInstanceId_Type()
)
cucsPowerMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyInstanceId.setStatus("current")
_CucsPowerMgmtPolicyDn_Type = CucsManagedObjectDn
_CucsPowerMgmtPolicyDn_Object = MibTableColumn
cucsPowerMgmtPolicyDn = _CucsPowerMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 2),
    _CucsPowerMgmtPolicyDn_Type()
)
cucsPowerMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyDn.setStatus("current")
_CucsPowerMgmtPolicyRn_Type = SnmpAdminString
_CucsPowerMgmtPolicyRn_Object = MibTableColumn
cucsPowerMgmtPolicyRn = _CucsPowerMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 3),
    _CucsPowerMgmtPolicyRn_Type()
)
cucsPowerMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyRn.setStatus("current")
_CucsPowerMgmtPolicyDescr_Type = SnmpAdminString
_CucsPowerMgmtPolicyDescr_Object = MibTableColumn
cucsPowerMgmtPolicyDescr = _CucsPowerMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 4),
    _CucsPowerMgmtPolicyDescr_Type()
)
cucsPowerMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyDescr.setStatus("current")
_CucsPowerMgmtPolicyIntId_Type = SnmpAdminString
_CucsPowerMgmtPolicyIntId_Object = MibTableColumn
cucsPowerMgmtPolicyIntId = _CucsPowerMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 5),
    _CucsPowerMgmtPolicyIntId_Type()
)
cucsPowerMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyIntId.setStatus("current")
_CucsPowerMgmtPolicyName_Type = SnmpAdminString
_CucsPowerMgmtPolicyName_Object = MibTableColumn
cucsPowerMgmtPolicyName = _CucsPowerMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 6),
    _CucsPowerMgmtPolicyName_Type()
)
cucsPowerMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyName.setStatus("current")
_CucsPowerMgmtPolicyStyle_Type = CucsPowerMgmtStyle
_CucsPowerMgmtPolicyStyle_Object = MibTableColumn
cucsPowerMgmtPolicyStyle = _CucsPowerMgmtPolicyStyle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 7),
    _CucsPowerMgmtPolicyStyle_Type()
)
cucsPowerMgmtPolicyStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyStyle.setStatus("current")
_CucsPowerMgmtPolicyPolicyLevel_Type = Gauge32
_CucsPowerMgmtPolicyPolicyLevel_Object = MibTableColumn
cucsPowerMgmtPolicyPolicyLevel = _CucsPowerMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 8),
    _CucsPowerMgmtPolicyPolicyLevel_Type()
)
cucsPowerMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyPolicyLevel.setStatus("current")
_CucsPowerMgmtPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPowerMgmtPolicyPolicyOwner_Object = MibTableColumn
cucsPowerMgmtPolicyPolicyOwner = _CucsPowerMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 9),
    _CucsPowerMgmtPolicyPolicyOwner_Type()
)
cucsPowerMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyPolicyOwner.setStatus("current")
_CucsPowerMgmtPolicyProfiling_Type = TruthValue
_CucsPowerMgmtPolicyProfiling_Object = MibTableColumn
cucsPowerMgmtPolicyProfiling = _CucsPowerMgmtPolicyProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 10),
    _CucsPowerMgmtPolicyProfiling_Type()
)
cucsPowerMgmtPolicyProfiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicyProfiling.setStatus("current")
_CucsPowerMgmtPolicySkipPowerCheck_Type = TruthValue
_CucsPowerMgmtPolicySkipPowerCheck_Object = MibTableColumn
cucsPowerMgmtPolicySkipPowerCheck = _CucsPowerMgmtPolicySkipPowerCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 11),
    _CucsPowerMgmtPolicySkipPowerCheck_Type()
)
cucsPowerMgmtPolicySkipPowerCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicySkipPowerCheck.setStatus("current")
_CucsPowerMgmtPolicySkipPowerDeployCheck_Type = TruthValue
_CucsPowerMgmtPolicySkipPowerDeployCheck_Object = MibTableColumn
cucsPowerMgmtPolicySkipPowerDeployCheck = _CucsPowerMgmtPolicySkipPowerDeployCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 13, 1, 12),
    _CucsPowerMgmtPolicySkipPowerDeployCheck_Type()
)
cucsPowerMgmtPolicySkipPowerDeployCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerMgmtPolicySkipPowerDeployCheck.setStatus("current")
_CucsPowerProfiledPowerTable_Object = MibTable
cucsPowerProfiledPowerTable = _CucsPowerProfiledPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14)
)
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerTable.setStatus("current")
_CucsPowerProfiledPowerEntry_Object = MibTableRow
cucsPowerProfiledPowerEntry = _CucsPowerProfiledPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1)
)
cucsPowerProfiledPowerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POWER-MIB", "cucsPowerProfiledPowerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerEntry.setStatus("current")
_CucsPowerProfiledPowerInstanceId_Type = CucsManagedObjectId
_CucsPowerProfiledPowerInstanceId_Object = MibTableColumn
cucsPowerProfiledPowerInstanceId = _CucsPowerProfiledPowerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 1),
    _CucsPowerProfiledPowerInstanceId_Type()
)
cucsPowerProfiledPowerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerInstanceId.setStatus("current")
_CucsPowerProfiledPowerDn_Type = CucsManagedObjectDn
_CucsPowerProfiledPowerDn_Object = MibTableColumn
cucsPowerProfiledPowerDn = _CucsPowerProfiledPowerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 2),
    _CucsPowerProfiledPowerDn_Type()
)
cucsPowerProfiledPowerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerDn.setStatus("current")
_CucsPowerProfiledPowerRn_Type = SnmpAdminString
_CucsPowerProfiledPowerRn_Object = MibTableColumn
cucsPowerProfiledPowerRn = _CucsPowerProfiledPowerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 3),
    _CucsPowerProfiledPowerRn_Type()
)
cucsPowerProfiledPowerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerRn.setStatus("current")
_CucsPowerProfiledPowerAbsMinPostPower_Type = Gauge32
_CucsPowerProfiledPowerAbsMinPostPower_Object = MibTableColumn
cucsPowerProfiledPowerAbsMinPostPower = _CucsPowerProfiledPowerAbsMinPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 4),
    _CucsPowerProfiledPowerAbsMinPostPower_Type()
)
cucsPowerProfiledPowerAbsMinPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerAbsMinPostPower.setStatus("current")
_CucsPowerProfiledPowerMaxAppPower_Type = Gauge32
_CucsPowerProfiledPowerMaxAppPower_Object = MibTableColumn
cucsPowerProfiledPowerMaxAppPower = _CucsPowerProfiledPowerMaxAppPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 5),
    _CucsPowerProfiledPowerMaxAppPower_Type()
)
cucsPowerProfiledPowerMaxAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerMaxAppPower.setStatus("current")
_CucsPowerProfiledPowerMaxPostPower_Type = Gauge32
_CucsPowerProfiledPowerMaxPostPower_Object = MibTableColumn
cucsPowerProfiledPowerMaxPostPower = _CucsPowerProfiledPowerMaxPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 6),
    _CucsPowerProfiledPowerMaxPostPower_Type()
)
cucsPowerProfiledPowerMaxPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerMaxPostPower.setStatus("current")
_CucsPowerProfiledPowerMinAppPower_Type = Gauge32
_CucsPowerProfiledPowerMinAppPower_Object = MibTableColumn
cucsPowerProfiledPowerMinAppPower = _CucsPowerProfiledPowerMinAppPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 7),
    _CucsPowerProfiledPowerMinAppPower_Type()
)
cucsPowerProfiledPowerMinAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerMinAppPower.setStatus("current")
_CucsPowerProfiledPowerMinNormPostPower_Type = Gauge32
_CucsPowerProfiledPowerMinNormPostPower_Object = MibTableColumn
cucsPowerProfiledPowerMinNormPostPower = _CucsPowerProfiledPowerMinNormPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 8),
    _CucsPowerProfiledPowerMinNormPostPower_Type()
)
cucsPowerProfiledPowerMinNormPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerMinNormPostPower.setStatus("current")
_CucsPowerProfiledPowerMinPostPower_Type = Gauge32
_CucsPowerProfiledPowerMinPostPower_Object = MibTableColumn
cucsPowerProfiledPowerMinPostPower = _CucsPowerProfiledPowerMinPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 9),
    _CucsPowerProfiledPowerMinPostPower_Type()
)
cucsPowerProfiledPowerMinPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerMinPostPower.setStatus("current")
_CucsPowerProfiledPowerPreDiscoveryPower_Type = Gauge32
_CucsPowerProfiledPowerPreDiscoveryPower_Object = MibTableColumn
cucsPowerProfiledPowerPreDiscoveryPower = _CucsPowerProfiledPowerPreDiscoveryPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 10),
    _CucsPowerProfiledPowerPreDiscoveryPower_Type()
)
cucsPowerProfiledPowerPreDiscoveryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerPreDiscoveryPower.setStatus("current")
_CucsPowerProfiledPowerProfileRunTime_Type = Gauge32
_CucsPowerProfiledPowerProfileRunTime_Object = MibTableColumn
cucsPowerProfiledPowerProfileRunTime = _CucsPowerProfiledPowerProfileRunTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 11),
    _CucsPowerProfiledPowerProfileRunTime_Type()
)
cucsPowerProfiledPowerProfileRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerProfileRunTime.setStatus("current")
_CucsPowerProfiledPowerProfiledBoot_Type = Gauge32
_CucsPowerProfiledPowerProfiledBoot_Object = MibTableColumn
cucsPowerProfiledPowerProfiledBoot = _CucsPowerProfiledPowerProfiledBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 12),
    _CucsPowerProfiledPowerProfiledBoot_Type()
)
cucsPowerProfiledPowerProfiledBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerProfiledBoot.setStatus("current")
_CucsPowerProfiledPowerProfiledMax_Type = Gauge32
_CucsPowerProfiledPowerProfiledMax_Object = MibTableColumn
cucsPowerProfiledPowerProfiledMax = _CucsPowerProfiledPowerProfiledMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 13),
    _CucsPowerProfiledPowerProfiledMax_Type()
)
cucsPowerProfiledPowerProfiledMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerProfiledMax.setStatus("current")
_CucsPowerProfiledPowerProfiledMin_Type = Gauge32
_CucsPowerProfiledPowerProfiledMin_Object = MibTableColumn
cucsPowerProfiledPowerProfiledMin = _CucsPowerProfiledPowerProfiledMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 14),
    _CucsPowerProfiledPowerProfiledMin_Type()
)
cucsPowerProfiledPowerProfiledMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerProfiledMin.setStatus("current")
_CucsPowerProfiledPowerSkipProfiling_Type = TruthValue
_CucsPowerProfiledPowerSkipProfiling_Object = MibTableColumn
cucsPowerProfiledPowerSkipProfiling = _CucsPowerProfiledPowerSkipProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 39, 14, 1, 15),
    _CucsPowerProfiledPowerSkipProfiling_Type()
)
cucsPowerProfiledPowerSkipProfiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPowerProfiledPowerSkipProfiling.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-POWER-MIB",
    **{"cucsPowerObjects": cucsPowerObjects,
       "cucsPowerBudgetTable": cucsPowerBudgetTable,
       "cucsPowerBudgetEntry": cucsPowerBudgetEntry,
       "cucsPowerBudgetInstanceId": cucsPowerBudgetInstanceId,
       "cucsPowerBudgetDn": cucsPowerBudgetDn,
       "cucsPowerBudgetRn": cucsPowerBudgetRn,
       "cucsPowerBudgetAdminCommitted": cucsPowerBudgetAdminCommitted,
       "cucsPowerBudgetAdminPeak": cucsPowerBudgetAdminPeak,
       "cucsPowerBudgetCurrentPower": cucsPowerBudgetCurrentPower,
       "cucsPowerBudgetGroupName": cucsPowerBudgetGroupName,
       "cucsPowerBudgetIdlePower": cucsPowerBudgetIdlePower,
       "cucsPowerBudgetMaxPower": cucsPowerBudgetMaxPower,
       "cucsPowerBudgetMinPower": cucsPowerBudgetMinPower,
       "cucsPowerBudgetOperCommitted": cucsPowerBudgetOperCommitted,
       "cucsPowerBudgetOperMin": cucsPowerBudgetOperMin,
       "cucsPowerBudgetOperPeak": cucsPowerBudgetOperPeak,
       "cucsPowerBudgetScaledWt": cucsPowerBudgetScaledWt,
       "cucsPowerBudgetOperState": cucsPowerBudgetOperState,
       "cucsPowerBudgetDynRealloc": cucsPowerBudgetDynRealloc,
       "cucsPowerBudgetPrio": cucsPowerBudgetPrio,
       "cucsPowerBudgetCatalogPower": cucsPowerBudgetCatalogPower,
       "cucsPowerBudgetUpdateTime": cucsPowerBudgetUpdateTime,
       "cucsPowerBudgetCapAction": cucsPowerBudgetCapAction,
       "cucsPowerBudgetWeight": cucsPowerBudgetWeight,
       "cucsPowerBudgetPsuCapacity": cucsPowerBudgetPsuCapacity,
       "cucsPowerBudgetPsuState": cucsPowerBudgetPsuState,
       "cucsPowerBudgetStyle": cucsPowerBudgetStyle,
       "cucsPowerBudgetAdminFPLockState": cucsPowerBudgetAdminFPLockState,
       "cucsPowerBudgetAdminPeakNew": cucsPowerBudgetAdminPeakNew,
       "cucsPowerBudgetBootPower": cucsPowerBudgetBootPower,
       "cucsPowerBudgetChRsrvdPower": cucsPowerBudgetChRsrvdPower,
       "cucsPowerBudgetOperFPLockState": cucsPowerBudgetOperFPLockState,
       "cucsPowerBudgetOperProfMethod": cucsPowerBudgetOperProfMethod,
       "cucsPowerBudgetProfMethod": cucsPowerBudgetProfMethod,
       "cucsPowerBudgetProfiling": cucsPowerBudgetProfiling,
       "cucsPowerBudgetPsuLineMode": cucsPowerBudgetPsuLineMode,
       "cucsPowerBudgetPowerAvailState": cucsPowerBudgetPowerAvailState,
       "cucsPowerBudgetPowerDeployState": cucsPowerBudgetPowerDeployState,
       "cucsPowerBudgetPowerOnDeploy": cucsPowerBudgetPowerOnDeploy,
       "cucsPowerBudgetFanSpeed": cucsPowerBudgetFanSpeed,
       "cucsPowerChassisMemberTable": cucsPowerChassisMemberTable,
       "cucsPowerChassisMemberEntry": cucsPowerChassisMemberEntry,
       "cucsPowerChassisMemberInstanceId": cucsPowerChassisMemberInstanceId,
       "cucsPowerChassisMemberDn": cucsPowerChassisMemberDn,
       "cucsPowerChassisMemberRn": cucsPowerChassisMemberRn,
       "cucsPowerChassisMemberId": cucsPowerChassisMemberId,
       "cucsPowerChassisMemberOperState": cucsPowerChassisMemberOperState,
       "cucsPowerEpTable": cucsPowerEpTable,
       "cucsPowerEpEntry": cucsPowerEpEntry,
       "cucsPowerEpInstanceId": cucsPowerEpInstanceId,
       "cucsPowerEpDn": cucsPowerEpDn,
       "cucsPowerEpRn": cucsPowerEpRn,
       "cucsPowerGroupTable": cucsPowerGroupTable,
       "cucsPowerGroupEntry": cucsPowerGroupEntry,
       "cucsPowerGroupInstanceId": cucsPowerGroupInstanceId,
       "cucsPowerGroupDn": cucsPowerGroupDn,
       "cucsPowerGroupRn": cucsPowerGroupRn,
       "cucsPowerGroupRealloc": cucsPowerGroupRealloc,
       "cucsPowerGroupAdminCommitted": cucsPowerGroupAdminCommitted,
       "cucsPowerGroupAdminPeak": cucsPowerGroupAdminPeak,
       "cucsPowerGroupCurrentPower": cucsPowerGroupCurrentPower,
       "cucsPowerGroupDescr": cucsPowerGroupDescr,
       "cucsPowerGroupFltAggr": cucsPowerGroupFltAggr,
       "cucsPowerGroupCurReqPower": cucsPowerGroupCurReqPower,
       "cucsPowerGroupMinReqPower": cucsPowerGroupMinReqPower,
       "cucsPowerGroupIntId": cucsPowerGroupIntId,
       "cucsPowerGroupName": cucsPowerGroupName,
       "cucsPowerGroupQualifier": cucsPowerGroupQualifier,
       "cucsPowerGroupOperCommitted": cucsPowerGroupOperCommitted,
       "cucsPowerGroupOperPeak": cucsPowerGroupOperPeak,
       "cucsPowerGroupOperState": cucsPowerGroupOperState,
       "cucsPowerGroupPolicyLevel": cucsPowerGroupPolicyLevel,
       "cucsPowerGroupPolicyOwner": cucsPowerGroupPolicyOwner,
       "cucsPowerGroupAdditionPolicyTable": cucsPowerGroupAdditionPolicyTable,
       "cucsPowerGroupAdditionPolicyEntry": cucsPowerGroupAdditionPolicyEntry,
       "cucsPowerGroupAdditionPolicyInstanceId": cucsPowerGroupAdditionPolicyInstanceId,
       "cucsPowerGroupAdditionPolicyDn": cucsPowerGroupAdditionPolicyDn,
       "cucsPowerGroupAdditionPolicyRn": cucsPowerGroupAdditionPolicyRn,
       "cucsPowerGroupAdditionPolicyAction": cucsPowerGroupAdditionPolicyAction,
       "cucsPowerGroupAdditionPolicyDescr": cucsPowerGroupAdditionPolicyDescr,
       "cucsPowerGroupAdditionPolicyIntId": cucsPowerGroupAdditionPolicyIntId,
       "cucsPowerGroupAdditionPolicyName": cucsPowerGroupAdditionPolicyName,
       "cucsPowerGroupAdditionPolicyPolicyLevel": cucsPowerGroupAdditionPolicyPolicyLevel,
       "cucsPowerGroupAdditionPolicyPolicyOwner": cucsPowerGroupAdditionPolicyPolicyOwner,
       "cucsPowerGroupQualTable": cucsPowerGroupQualTable,
       "cucsPowerGroupQualEntry": cucsPowerGroupQualEntry,
       "cucsPowerGroupQualInstanceId": cucsPowerGroupQualInstanceId,
       "cucsPowerGroupQualDn": cucsPowerGroupQualDn,
       "cucsPowerGroupQualRn": cucsPowerGroupQualRn,
       "cucsPowerGroupQualGroupName": cucsPowerGroupQualGroupName,
       "cucsPowerGroupStatsTable": cucsPowerGroupStatsTable,
       "cucsPowerGroupStatsEntry": cucsPowerGroupStatsEntry,
       "cucsPowerGroupStatsInstanceId": cucsPowerGroupStatsInstanceId,
       "cucsPowerGroupStatsDn": cucsPowerGroupStatsDn,
       "cucsPowerGroupStatsRn": cucsPowerGroupStatsRn,
       "cucsPowerGroupStatsIntervals": cucsPowerGroupStatsIntervals,
       "cucsPowerGroupStatsPower": cucsPowerGroupStatsPower,
       "cucsPowerGroupStatsPowerAvg": cucsPowerGroupStatsPowerAvg,
       "cucsPowerGroupStatsPowerMax": cucsPowerGroupStatsPowerMax,
       "cucsPowerGroupStatsPowerMin": cucsPowerGroupStatsPowerMin,
       "cucsPowerGroupStatsSuspect": cucsPowerGroupStatsSuspect,
       "cucsPowerGroupStatsThresholded": cucsPowerGroupStatsThresholded,
       "cucsPowerGroupStatsTimeCollected": cucsPowerGroupStatsTimeCollected,
       "cucsPowerGroupStatsUpdate": cucsPowerGroupStatsUpdate,
       "cucsPowerGroupStatsHistTable": cucsPowerGroupStatsHistTable,
       "cucsPowerGroupStatsHistEntry": cucsPowerGroupStatsHistEntry,
       "cucsPowerGroupStatsHistInstanceId": cucsPowerGroupStatsHistInstanceId,
       "cucsPowerGroupStatsHistDn": cucsPowerGroupStatsHistDn,
       "cucsPowerGroupStatsHistRn": cucsPowerGroupStatsHistRn,
       "cucsPowerGroupStatsHistId": cucsPowerGroupStatsHistId,
       "cucsPowerGroupStatsHistMostRecent": cucsPowerGroupStatsHistMostRecent,
       "cucsPowerGroupStatsHistPower": cucsPowerGroupStatsHistPower,
       "cucsPowerGroupStatsHistPowerAvg": cucsPowerGroupStatsHistPowerAvg,
       "cucsPowerGroupStatsHistPowerMax": cucsPowerGroupStatsHistPowerMax,
       "cucsPowerGroupStatsHistPowerMin": cucsPowerGroupStatsHistPowerMin,
       "cucsPowerGroupStatsHistSuspect": cucsPowerGroupStatsHistSuspect,
       "cucsPowerGroupStatsHistThresholded": cucsPowerGroupStatsHistThresholded,
       "cucsPowerGroupStatsHistTimeCollected": cucsPowerGroupStatsHistTimeCollected,
       "cucsPowerPlacementTable": cucsPowerPlacementTable,
       "cucsPowerPlacementEntry": cucsPowerPlacementEntry,
       "cucsPowerPlacementInstanceId": cucsPowerPlacementInstanceId,
       "cucsPowerPlacementDn": cucsPowerPlacementDn,
       "cucsPowerPlacementRn": cucsPowerPlacementRn,
       "cucsPowerPlacementDescr": cucsPowerPlacementDescr,
       "cucsPowerPlacementIntId": cucsPowerPlacementIntId,
       "cucsPowerPlacementName": cucsPowerPlacementName,
       "cucsPowerPlacementPeerReqConflict": cucsPowerPlacementPeerReqConflict,
       "cucsPowerPlacementPgName": cucsPowerPlacementPgName,
       "cucsPowerPlacementPrioShare": cucsPowerPlacementPrioShare,
       "cucsPowerPlacementSelfReqConflict": cucsPowerPlacementSelfReqConflict,
       "cucsPowerPlacementPolicyLevel": cucsPowerPlacementPolicyLevel,
       "cucsPowerPlacementPolicyOwner": cucsPowerPlacementPolicyOwner,
       "cucsPowerPolicyTable": cucsPowerPolicyTable,
       "cucsPowerPolicyEntry": cucsPowerPolicyEntry,
       "cucsPowerPolicyInstanceId": cucsPowerPolicyInstanceId,
       "cucsPowerPolicyDn": cucsPowerPolicyDn,
       "cucsPowerPolicyRn": cucsPowerPolicyRn,
       "cucsPowerPolicyDescr": cucsPowerPolicyDescr,
       "cucsPowerPolicyIntId": cucsPowerPolicyIntId,
       "cucsPowerPolicyName": cucsPowerPolicyName,
       "cucsPowerPolicyOperPrio": cucsPowerPolicyOperPrio,
       "cucsPowerPolicyPrio": cucsPowerPolicyPrio,
       "cucsPowerPolicyPolicyLevel": cucsPowerPolicyPolicyLevel,
       "cucsPowerPolicyPolicyOwner": cucsPowerPolicyPolicyOwner,
       "cucsPowerPolicyPropAcl": cucsPowerPolicyPropAcl,
       "cucsPowerPolicyFanSpeed": cucsPowerPolicyFanSpeed,
       "cucsPowerPrioWghtTable": cucsPowerPrioWghtTable,
       "cucsPowerPrioWghtEntry": cucsPowerPrioWghtEntry,
       "cucsPowerPrioWghtInstanceId": cucsPowerPrioWghtInstanceId,
       "cucsPowerPrioWghtDn": cucsPowerPrioWghtDn,
       "cucsPowerPrioWghtRn": cucsPowerPrioWghtRn,
       "cucsPowerPrioWghtPrio": cucsPowerPrioWghtPrio,
       "cucsPowerPrioWghtWeight": cucsPowerPrioWghtWeight,
       "cucsPowerRackUnitMemberTable": cucsPowerRackUnitMemberTable,
       "cucsPowerRackUnitMemberEntry": cucsPowerRackUnitMemberEntry,
       "cucsPowerRackUnitMemberInstanceId": cucsPowerRackUnitMemberInstanceId,
       "cucsPowerRackUnitMemberDn": cucsPowerRackUnitMemberDn,
       "cucsPowerRackUnitMemberRn": cucsPowerRackUnitMemberRn,
       "cucsPowerRackUnitMemberId": cucsPowerRackUnitMemberId,
       "cucsPowerRackUnitMemberOperState": cucsPowerRackUnitMemberOperState,
       "cucsPowerMgmtPolicyTable": cucsPowerMgmtPolicyTable,
       "cucsPowerMgmtPolicyEntry": cucsPowerMgmtPolicyEntry,
       "cucsPowerMgmtPolicyInstanceId": cucsPowerMgmtPolicyInstanceId,
       "cucsPowerMgmtPolicyDn": cucsPowerMgmtPolicyDn,
       "cucsPowerMgmtPolicyRn": cucsPowerMgmtPolicyRn,
       "cucsPowerMgmtPolicyDescr": cucsPowerMgmtPolicyDescr,
       "cucsPowerMgmtPolicyIntId": cucsPowerMgmtPolicyIntId,
       "cucsPowerMgmtPolicyName": cucsPowerMgmtPolicyName,
       "cucsPowerMgmtPolicyStyle": cucsPowerMgmtPolicyStyle,
       "cucsPowerMgmtPolicyPolicyLevel": cucsPowerMgmtPolicyPolicyLevel,
       "cucsPowerMgmtPolicyPolicyOwner": cucsPowerMgmtPolicyPolicyOwner,
       "cucsPowerMgmtPolicyProfiling": cucsPowerMgmtPolicyProfiling,
       "cucsPowerMgmtPolicySkipPowerCheck": cucsPowerMgmtPolicySkipPowerCheck,
       "cucsPowerMgmtPolicySkipPowerDeployCheck": cucsPowerMgmtPolicySkipPowerDeployCheck,
       "cucsPowerProfiledPowerTable": cucsPowerProfiledPowerTable,
       "cucsPowerProfiledPowerEntry": cucsPowerProfiledPowerEntry,
       "cucsPowerProfiledPowerInstanceId": cucsPowerProfiledPowerInstanceId,
       "cucsPowerProfiledPowerDn": cucsPowerProfiledPowerDn,
       "cucsPowerProfiledPowerRn": cucsPowerProfiledPowerRn,
       "cucsPowerProfiledPowerAbsMinPostPower": cucsPowerProfiledPowerAbsMinPostPower,
       "cucsPowerProfiledPowerMaxAppPower": cucsPowerProfiledPowerMaxAppPower,
       "cucsPowerProfiledPowerMaxPostPower": cucsPowerProfiledPowerMaxPostPower,
       "cucsPowerProfiledPowerMinAppPower": cucsPowerProfiledPowerMinAppPower,
       "cucsPowerProfiledPowerMinNormPostPower": cucsPowerProfiledPowerMinNormPostPower,
       "cucsPowerProfiledPowerMinPostPower": cucsPowerProfiledPowerMinPostPower,
       "cucsPowerProfiledPowerPreDiscoveryPower": cucsPowerProfiledPowerPreDiscoveryPower,
       "cucsPowerProfiledPowerProfileRunTime": cucsPowerProfiledPowerProfileRunTime,
       "cucsPowerProfiledPowerProfiledBoot": cucsPowerProfiledPowerProfiledBoot,
       "cucsPowerProfiledPowerProfiledMax": cucsPowerProfiledPowerProfiledMax,
       "cucsPowerProfiledPowerProfiledMin": cucsPowerProfiledPowerProfiledMin,
       "cucsPowerProfiledPowerSkipProfiling": cucsPowerProfiledPowerSkipProfiling}
)
