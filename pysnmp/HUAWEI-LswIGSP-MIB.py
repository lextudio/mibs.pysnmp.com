# SNMP MIB module (HUAWEI-LswIGSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LswIGSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:40 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwLswIgmpsnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7)
)
hwLswIgmpsnoopingMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwLswIgmpsnoopingMibObject_ObjectIdentity = ObjectIdentity
hwLswIgmpsnoopingMibObject = _HwLswIgmpsnoopingMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1)
)
_HwIgmpSnoopingStatus_Type = EnabledStatus
_HwIgmpSnoopingStatus_Object = MibScalar
hwIgmpSnoopingStatus = _HwIgmpSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 1),
    _HwIgmpSnoopingStatus_Type()
)
hwIgmpSnoopingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingStatus.setStatus("current")


class _HwIgmpSnoopingRouterPortAge_Type(Integer32):
    """Custom type hwIgmpSnoopingRouterPortAge based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwIgmpSnoopingRouterPortAge_Type.__name__ = "Integer32"
_HwIgmpSnoopingRouterPortAge_Object = MibScalar
hwIgmpSnoopingRouterPortAge = _HwIgmpSnoopingRouterPortAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 2),
    _HwIgmpSnoopingRouterPortAge_Type()
)
hwIgmpSnoopingRouterPortAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingRouterPortAge.setStatus("current")


class _HwIgmpSnoopingResponseTime_Type(Integer32):
    """Custom type hwIgmpSnoopingResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HwIgmpSnoopingResponseTime_Type.__name__ = "Integer32"
_HwIgmpSnoopingResponseTime_Object = MibScalar
hwIgmpSnoopingResponseTime = _HwIgmpSnoopingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 3),
    _HwIgmpSnoopingResponseTime_Type()
)
hwIgmpSnoopingResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingResponseTime.setStatus("current")


class _HwIgmpSnoopingHostTime_Type(Integer32):
    """Custom type hwIgmpSnoopingHostTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_HwIgmpSnoopingHostTime_Type.__name__ = "Integer32"
_HwIgmpSnoopingHostTime_Object = MibScalar
hwIgmpSnoopingHostTime = _HwIgmpSnoopingHostTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 4),
    _HwIgmpSnoopingHostTime_Type()
)
hwIgmpSnoopingHostTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingHostTime.setStatus("current")
_HwIgmpSnoopingGroupLimitTable_Object = MibTable
hwIgmpSnoopingGroupLimitTable = _HwIgmpSnoopingGroupLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 5)
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupLimitTable.setStatus("current")
_HwIgmpSnoopingGroupLimitEntry_Object = MibTableRow
hwIgmpSnoopingGroupLimitEntry = _HwIgmpSnoopingGroupLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 5, 1)
)
hwIgmpSnoopingGroupLimitEntry.setIndexNames(
    (0, "HUAWEI-LswIGSP-MIB", "hwIgmpSnoopingGroupIfIndex"),
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupLimitEntry.setStatus("current")
_HwIgmpSnoopingGroupIfIndex_Type = InterfaceIndex
_HwIgmpSnoopingGroupIfIndex_Object = MibTableColumn
hwIgmpSnoopingGroupIfIndex = _HwIgmpSnoopingGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 5, 1, 1),
    _HwIgmpSnoopingGroupIfIndex_Type()
)
hwIgmpSnoopingGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupIfIndex.setStatus("current")


class _HwIgmpSnoopingGroupLimitNumber_Type(Unsigned32):
    """Custom type hwIgmpSnoopingGroupLimitNumber based on Unsigned32"""
    defaultValue = 4294967295


_HwIgmpSnoopingGroupLimitNumber_Object = MibTableColumn
hwIgmpSnoopingGroupLimitNumber = _HwIgmpSnoopingGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 5, 1, 2),
    _HwIgmpSnoopingGroupLimitNumber_Type()
)
hwIgmpSnoopingGroupLimitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupLimitNumber.setStatus("current")
_HwIgmpSnoopingFastLeaveTable_Object = MibTable
hwIgmpSnoopingFastLeaveTable = _HwIgmpSnoopingFastLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 6)
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingFastLeaveTable.setStatus("current")
_HwIgmpSnoopingFastLeaveEntry_Object = MibTableRow
hwIgmpSnoopingFastLeaveEntry = _HwIgmpSnoopingFastLeaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 6, 1)
)
hwIgmpSnoopingFastLeaveEntry.setIndexNames(
    (0, "HUAWEI-LswIGSP-MIB", "hwIgmpSnoopingFastLeaveIfIndex"),
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingFastLeaveEntry.setStatus("current")
_HwIgmpSnoopingFastLeaveIfIndex_Type = InterfaceIndex
_HwIgmpSnoopingFastLeaveIfIndex_Object = MibTableColumn
hwIgmpSnoopingFastLeaveIfIndex = _HwIgmpSnoopingFastLeaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 6, 1, 1),
    _HwIgmpSnoopingFastLeaveIfIndex_Type()
)
hwIgmpSnoopingFastLeaveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIgmpSnoopingFastLeaveIfIndex.setStatus("current")


class _HwIgmpSnoopingFastLeaveStatus_Type(EnabledStatus):
    """Custom type hwIgmpSnoopingFastLeaveStatus based on EnabledStatus"""
    defaultValue = 2


_HwIgmpSnoopingFastLeaveStatus_Object = MibTableColumn
hwIgmpSnoopingFastLeaveStatus = _HwIgmpSnoopingFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 6, 1, 2),
    _HwIgmpSnoopingFastLeaveStatus_Type()
)
hwIgmpSnoopingFastLeaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingFastLeaveStatus.setStatus("current")
_HwIgmpSnoopingGroupPolicyTable_Object = MibTable
hwIgmpSnoopingGroupPolicyTable = _HwIgmpSnoopingGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 7)
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupPolicyTable.setStatus("current")
_HwIgmpSnoopingGroupPolicyEntry_Object = MibTableRow
hwIgmpSnoopingGroupPolicyEntry = _HwIgmpSnoopingGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 7, 1)
)
hwIgmpSnoopingGroupPolicyEntry.setIndexNames(
    (0, "HUAWEI-LswIGSP-MIB", "hwIgmpSnoopingGroupPolicyIfIndex"),
    (0, "HUAWEI-LswIGSP-MIB", "hwIgmpSnoopingGroupPolicyVlanID"),
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupPolicyEntry.setStatus("current")
_HwIgmpSnoopingGroupPolicyIfIndex_Type = InterfaceIndex
_HwIgmpSnoopingGroupPolicyIfIndex_Object = MibTableColumn
hwIgmpSnoopingGroupPolicyIfIndex = _HwIgmpSnoopingGroupPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 7, 1, 1),
    _HwIgmpSnoopingGroupPolicyIfIndex_Type()
)
hwIgmpSnoopingGroupPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupPolicyIfIndex.setStatus("current")


class _HwIgmpSnoopingGroupPolicyVlanID_Type(Integer32):
    """Custom type hwIgmpSnoopingGroupPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwIgmpSnoopingGroupPolicyVlanID_Type.__name__ = "Integer32"
_HwIgmpSnoopingGroupPolicyVlanID_Object = MibTableColumn
hwIgmpSnoopingGroupPolicyVlanID = _HwIgmpSnoopingGroupPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 7, 1, 2),
    _HwIgmpSnoopingGroupPolicyVlanID_Type()
)
hwIgmpSnoopingGroupPolicyVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupPolicyVlanID.setStatus("current")


class _HwIgmpSnoopingGroupPolicyParameter_Type(Integer32):
    """Custom type hwIgmpSnoopingGroupPolicyParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2999),
    )


_HwIgmpSnoopingGroupPolicyParameter_Type.__name__ = "Integer32"
_HwIgmpSnoopingGroupPolicyParameter_Object = MibTableColumn
hwIgmpSnoopingGroupPolicyParameter = _HwIgmpSnoopingGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 7, 1, 3),
    _HwIgmpSnoopingGroupPolicyParameter_Type()
)
hwIgmpSnoopingGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupPolicyParameter.setStatus("current")
_HwIgmpSnoopingGroupPolicyStatus_Type = RowStatus
_HwIgmpSnoopingGroupPolicyStatus_Object = MibTableColumn
hwIgmpSnoopingGroupPolicyStatus = _HwIgmpSnoopingGroupPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 7, 1, 4),
    _HwIgmpSnoopingGroupPolicyStatus_Type()
)
hwIgmpSnoopingGroupPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIgmpSnoopingGroupPolicyStatus.setStatus("current")
_HwIgmpSnoopingNonFloodingStatus_Type = EnabledStatus
_HwIgmpSnoopingNonFloodingStatus_Object = MibScalar
hwIgmpSnoopingNonFloodingStatus = _HwIgmpSnoopingNonFloodingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 8),
    _HwIgmpSnoopingNonFloodingStatus_Type()
)
hwIgmpSnoopingNonFloodingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingNonFloodingStatus.setStatus("current")
_HwIgmpSnoopingVlanStatusTable_Object = MibTable
hwIgmpSnoopingVlanStatusTable = _HwIgmpSnoopingVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 9)
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingVlanStatusTable.setStatus("current")
_HwIgmpSnoopingVlanStatusEntry_Object = MibTableRow
hwIgmpSnoopingVlanStatusEntry = _HwIgmpSnoopingVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 9, 1)
)
hwIgmpSnoopingVlanStatusEntry.setIndexNames(
    (0, "HUAWEI-LswIGSP-MIB", "hwIgmpSnoopingVlanID"),
)
if mibBuilder.loadTexts:
    hwIgmpSnoopingVlanStatusEntry.setStatus("current")


class _HwIgmpSnoopingVlanID_Type(Integer32):
    """Custom type hwIgmpSnoopingVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwIgmpSnoopingVlanID_Type.__name__ = "Integer32"
_HwIgmpSnoopingVlanID_Object = MibTableColumn
hwIgmpSnoopingVlanID = _HwIgmpSnoopingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 9, 1, 1),
    _HwIgmpSnoopingVlanID_Type()
)
hwIgmpSnoopingVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIgmpSnoopingVlanID.setStatus("current")


class _HwIgmpSnoopingVlanEnabled_Type(EnabledStatus):
    """Custom type hwIgmpSnoopingVlanEnabled based on EnabledStatus"""


_HwIgmpSnoopingVlanEnabled_Object = MibTableColumn
hwIgmpSnoopingVlanEnabled = _HwIgmpSnoopingVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 9, 1, 2),
    _HwIgmpSnoopingVlanEnabled_Type()
)
hwIgmpSnoopingVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingVlanEnabled.setStatus("current")
_HwIgmpSnoopingStatsObjects_ObjectIdentity = ObjectIdentity
hwIgmpSnoopingStatsObjects = _HwIgmpSnoopingStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10)
)
_HwRecvIGMPGQueryNum_Type = Counter32
_HwRecvIGMPGQueryNum_Object = MibScalar
hwRecvIGMPGQueryNum = _HwRecvIGMPGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 1),
    _HwRecvIGMPGQueryNum_Type()
)
hwRecvIGMPGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecvIGMPGQueryNum.setStatus("current")
_HwRecvIGMPSQueryNum_Type = Counter32
_HwRecvIGMPSQueryNum_Object = MibScalar
hwRecvIGMPSQueryNum = _HwRecvIGMPSQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 2),
    _HwRecvIGMPSQueryNum_Type()
)
hwRecvIGMPSQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecvIGMPSQueryNum.setStatus("current")
_HwRecvIGMPV1ReportNum_Type = Counter32
_HwRecvIGMPV1ReportNum_Object = MibScalar
hwRecvIGMPV1ReportNum = _HwRecvIGMPV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 3),
    _HwRecvIGMPV1ReportNum_Type()
)
hwRecvIGMPV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecvIGMPV1ReportNum.setStatus("current")
_HwRecvIGMPV2ReportNum_Type = Counter32
_HwRecvIGMPV2ReportNum_Object = MibScalar
hwRecvIGMPV2ReportNum = _HwRecvIGMPV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 4),
    _HwRecvIGMPV2ReportNum_Type()
)
hwRecvIGMPV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecvIGMPV2ReportNum.setStatus("current")
_HwRecvIGMPLeaveNum_Type = Counter32
_HwRecvIGMPLeaveNum_Object = MibScalar
hwRecvIGMPLeaveNum = _HwRecvIGMPLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 5),
    _HwRecvIGMPLeaveNum_Type()
)
hwRecvIGMPLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecvIGMPLeaveNum.setStatus("current")
_HwRecvErrorIGMPPacketNum_Type = Counter32
_HwRecvErrorIGMPPacketNum_Object = MibScalar
hwRecvErrorIGMPPacketNum = _HwRecvErrorIGMPPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 6),
    _HwRecvErrorIGMPPacketNum_Type()
)
hwRecvErrorIGMPPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecvErrorIGMPPacketNum.setStatus("current")
_HwSentIGMPSQueryNum_Type = Counter32
_HwSentIGMPSQueryNum_Object = MibScalar
hwSentIGMPSQueryNum = _HwSentIGMPSQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 7),
    _HwSentIGMPSQueryNum_Type()
)
hwSentIGMPSQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSentIGMPSQueryNum.setStatus("current")


class _HwIgmpSnoopingClearStats_Type(Integer32):
    """Custom type hwIgmpSnoopingClearStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("counting", 2))
    )


_HwIgmpSnoopingClearStats_Type.__name__ = "Integer32"
_HwIgmpSnoopingClearStats_Object = MibScalar
hwIgmpSnoopingClearStats = _HwIgmpSnoopingClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 7, 1, 10, 8),
    _HwIgmpSnoopingClearStats_Type()
)
hwIgmpSnoopingClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingClearStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswIGSP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hwLswIgmpsnoopingMib": hwLswIgmpsnoopingMib,
       "hwLswIgmpsnoopingMibObject": hwLswIgmpsnoopingMibObject,
       "hwIgmpSnoopingStatus": hwIgmpSnoopingStatus,
       "hwIgmpSnoopingRouterPortAge": hwIgmpSnoopingRouterPortAge,
       "hwIgmpSnoopingResponseTime": hwIgmpSnoopingResponseTime,
       "hwIgmpSnoopingHostTime": hwIgmpSnoopingHostTime,
       "hwIgmpSnoopingGroupLimitTable": hwIgmpSnoopingGroupLimitTable,
       "hwIgmpSnoopingGroupLimitEntry": hwIgmpSnoopingGroupLimitEntry,
       "hwIgmpSnoopingGroupIfIndex": hwIgmpSnoopingGroupIfIndex,
       "hwIgmpSnoopingGroupLimitNumber": hwIgmpSnoopingGroupLimitNumber,
       "hwIgmpSnoopingFastLeaveTable": hwIgmpSnoopingFastLeaveTable,
       "hwIgmpSnoopingFastLeaveEntry": hwIgmpSnoopingFastLeaveEntry,
       "hwIgmpSnoopingFastLeaveIfIndex": hwIgmpSnoopingFastLeaveIfIndex,
       "hwIgmpSnoopingFastLeaveStatus": hwIgmpSnoopingFastLeaveStatus,
       "hwIgmpSnoopingGroupPolicyTable": hwIgmpSnoopingGroupPolicyTable,
       "hwIgmpSnoopingGroupPolicyEntry": hwIgmpSnoopingGroupPolicyEntry,
       "hwIgmpSnoopingGroupPolicyIfIndex": hwIgmpSnoopingGroupPolicyIfIndex,
       "hwIgmpSnoopingGroupPolicyVlanID": hwIgmpSnoopingGroupPolicyVlanID,
       "hwIgmpSnoopingGroupPolicyParameter": hwIgmpSnoopingGroupPolicyParameter,
       "hwIgmpSnoopingGroupPolicyStatus": hwIgmpSnoopingGroupPolicyStatus,
       "hwIgmpSnoopingNonFloodingStatus": hwIgmpSnoopingNonFloodingStatus,
       "hwIgmpSnoopingVlanStatusTable": hwIgmpSnoopingVlanStatusTable,
       "hwIgmpSnoopingVlanStatusEntry": hwIgmpSnoopingVlanStatusEntry,
       "hwIgmpSnoopingVlanID": hwIgmpSnoopingVlanID,
       "hwIgmpSnoopingVlanEnabled": hwIgmpSnoopingVlanEnabled,
       "hwIgmpSnoopingStatsObjects": hwIgmpSnoopingStatsObjects,
       "hwRecvIGMPGQueryNum": hwRecvIGMPGQueryNum,
       "hwRecvIGMPSQueryNum": hwRecvIGMPSQueryNum,
       "hwRecvIGMPV1ReportNum": hwRecvIGMPV1ReportNum,
       "hwRecvIGMPV2ReportNum": hwRecvIGMPV2ReportNum,
       "hwRecvIGMPLeaveNum": hwRecvIGMPLeaveNum,
       "hwRecvErrorIGMPPacketNum": hwRecvErrorIGMPPacketNum,
       "hwSentIGMPSQueryNum": hwSentIGMPSQueryNum,
       "hwIgmpSnoopingClearStats": hwIgmpSnoopingClearStats}
)
