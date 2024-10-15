# SNMP MIB module (HH3C-LswIGSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswIGSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:55 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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

hh3cLswIgmpsnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7)
)
hh3cLswIgmpsnoopingMib.setRevisions(
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

_Hh3cLswIgmpsnoopingMibObject_ObjectIdentity = ObjectIdentity
hh3cLswIgmpsnoopingMibObject = _Hh3cLswIgmpsnoopingMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1)
)
_Hh3cIgmpSnoopingStatus_Type = EnabledStatus
_Hh3cIgmpSnoopingStatus_Object = MibScalar
hh3cIgmpSnoopingStatus = _Hh3cIgmpSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 1),
    _Hh3cIgmpSnoopingStatus_Type()
)
hh3cIgmpSnoopingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingStatus.setStatus("current")


class _Hh3cIgmpSnoopingRouterPortAge_Type(Integer32):
    """Custom type hh3cIgmpSnoopingRouterPortAge based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Hh3cIgmpSnoopingRouterPortAge_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingRouterPortAge_Object = MibScalar
hh3cIgmpSnoopingRouterPortAge = _Hh3cIgmpSnoopingRouterPortAge_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 2),
    _Hh3cIgmpSnoopingRouterPortAge_Type()
)
hh3cIgmpSnoopingRouterPortAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingRouterPortAge.setStatus("current")


class _Hh3cIgmpSnoopingResponseTime_Type(Integer32):
    """Custom type hh3cIgmpSnoopingResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Hh3cIgmpSnoopingResponseTime_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingResponseTime_Object = MibScalar
hh3cIgmpSnoopingResponseTime = _Hh3cIgmpSnoopingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 3),
    _Hh3cIgmpSnoopingResponseTime_Type()
)
hh3cIgmpSnoopingResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingResponseTime.setStatus("current")


class _Hh3cIgmpSnoopingHostTime_Type(Integer32):
    """Custom type hh3cIgmpSnoopingHostTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Hh3cIgmpSnoopingHostTime_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingHostTime_Object = MibScalar
hh3cIgmpSnoopingHostTime = _Hh3cIgmpSnoopingHostTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 4),
    _Hh3cIgmpSnoopingHostTime_Type()
)
hh3cIgmpSnoopingHostTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingHostTime.setStatus("current")
_Hh3cIgmpSnoopingGroupLimitTable_Object = MibTable
hh3cIgmpSnoopingGroupLimitTable = _Hh3cIgmpSnoopingGroupLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupLimitTable.setStatus("current")
_Hh3cIgmpSnoopingGroupLimitEntry_Object = MibTableRow
hh3cIgmpSnoopingGroupLimitEntry = _Hh3cIgmpSnoopingGroupLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5, 1)
)
hh3cIgmpSnoopingGroupLimitEntry.setIndexNames(
    (0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingGroupIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupLimitEntry.setStatus("current")
_Hh3cIgmpSnoopingGroupIfIndex_Type = InterfaceIndex
_Hh3cIgmpSnoopingGroupIfIndex_Object = MibTableColumn
hh3cIgmpSnoopingGroupIfIndex = _Hh3cIgmpSnoopingGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5, 1, 1),
    _Hh3cIgmpSnoopingGroupIfIndex_Type()
)
hh3cIgmpSnoopingGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupIfIndex.setStatus("current")


class _Hh3cIgmpSnoopingGroupLimitNumber_Type(Unsigned32):
    """Custom type hh3cIgmpSnoopingGroupLimitNumber based on Unsigned32"""
    defaultValue = 4294967295


_Hh3cIgmpSnoopingGroupLimitNumber_Object = MibTableColumn
hh3cIgmpSnoopingGroupLimitNumber = _Hh3cIgmpSnoopingGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5, 1, 2),
    _Hh3cIgmpSnoopingGroupLimitNumber_Type()
)
hh3cIgmpSnoopingGroupLimitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupLimitNumber.setStatus("current")
_Hh3cIgmpSnoopingFastLeaveTable_Object = MibTable
hh3cIgmpSnoopingFastLeaveTable = _Hh3cIgmpSnoopingFastLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingFastLeaveTable.setStatus("current")
_Hh3cIgmpSnoopingFastLeaveEntry_Object = MibTableRow
hh3cIgmpSnoopingFastLeaveEntry = _Hh3cIgmpSnoopingFastLeaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6, 1)
)
hh3cIgmpSnoopingFastLeaveEntry.setIndexNames(
    (0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingFastLeaveIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingFastLeaveEntry.setStatus("current")
_Hh3cIgmpSnoopingFastLeaveIfIndex_Type = InterfaceIndex
_Hh3cIgmpSnoopingFastLeaveIfIndex_Object = MibTableColumn
hh3cIgmpSnoopingFastLeaveIfIndex = _Hh3cIgmpSnoopingFastLeaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6, 1, 1),
    _Hh3cIgmpSnoopingFastLeaveIfIndex_Type()
)
hh3cIgmpSnoopingFastLeaveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingFastLeaveIfIndex.setStatus("current")


class _Hh3cIgmpSnoopingFastLeaveStatus_Type(EnabledStatus):
    """Custom type hh3cIgmpSnoopingFastLeaveStatus based on EnabledStatus"""
    defaultValue = 2


_Hh3cIgmpSnoopingFastLeaveStatus_Object = MibTableColumn
hh3cIgmpSnoopingFastLeaveStatus = _Hh3cIgmpSnoopingFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6, 1, 2),
    _Hh3cIgmpSnoopingFastLeaveStatus_Type()
)
hh3cIgmpSnoopingFastLeaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingFastLeaveStatus.setStatus("current")
_Hh3cIgmpSnoopingGroupPolicyTable_Object = MibTable
hh3cIgmpSnoopingGroupPolicyTable = _Hh3cIgmpSnoopingGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupPolicyTable.setStatus("current")
_Hh3cIgmpSnoopingGroupPolicyEntry_Object = MibTableRow
hh3cIgmpSnoopingGroupPolicyEntry = _Hh3cIgmpSnoopingGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1)
)
hh3cIgmpSnoopingGroupPolicyEntry.setIndexNames(
    (0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingGroupPolicyIfIndex"),
    (0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingGroupPolicyVlanID"),
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupPolicyEntry.setStatus("current")
_Hh3cIgmpSnoopingGroupPolicyIfIndex_Type = InterfaceIndex
_Hh3cIgmpSnoopingGroupPolicyIfIndex_Object = MibTableColumn
hh3cIgmpSnoopingGroupPolicyIfIndex = _Hh3cIgmpSnoopingGroupPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 1),
    _Hh3cIgmpSnoopingGroupPolicyIfIndex_Type()
)
hh3cIgmpSnoopingGroupPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupPolicyIfIndex.setStatus("current")


class _Hh3cIgmpSnoopingGroupPolicyVlanID_Type(Integer32):
    """Custom type hh3cIgmpSnoopingGroupPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cIgmpSnoopingGroupPolicyVlanID_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingGroupPolicyVlanID_Object = MibTableColumn
hh3cIgmpSnoopingGroupPolicyVlanID = _Hh3cIgmpSnoopingGroupPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 2),
    _Hh3cIgmpSnoopingGroupPolicyVlanID_Type()
)
hh3cIgmpSnoopingGroupPolicyVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupPolicyVlanID.setStatus("current")


class _Hh3cIgmpSnoopingGroupPolicyParameter_Type(Integer32):
    """Custom type hh3cIgmpSnoopingGroupPolicyParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2999),
    )


_Hh3cIgmpSnoopingGroupPolicyParameter_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingGroupPolicyParameter_Object = MibTableColumn
hh3cIgmpSnoopingGroupPolicyParameter = _Hh3cIgmpSnoopingGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 3),
    _Hh3cIgmpSnoopingGroupPolicyParameter_Type()
)
hh3cIgmpSnoopingGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupPolicyParameter.setStatus("current")
_Hh3cIgmpSnoopingGroupPolicyStatus_Type = RowStatus
_Hh3cIgmpSnoopingGroupPolicyStatus_Object = MibTableColumn
hh3cIgmpSnoopingGroupPolicyStatus = _Hh3cIgmpSnoopingGroupPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 4),
    _Hh3cIgmpSnoopingGroupPolicyStatus_Type()
)
hh3cIgmpSnoopingGroupPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingGroupPolicyStatus.setStatus("current")
_Hh3cIgmpSnoopingNonFloodingStatus_Type = EnabledStatus
_Hh3cIgmpSnoopingNonFloodingStatus_Object = MibScalar
hh3cIgmpSnoopingNonFloodingStatus = _Hh3cIgmpSnoopingNonFloodingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 8),
    _Hh3cIgmpSnoopingNonFloodingStatus_Type()
)
hh3cIgmpSnoopingNonFloodingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingNonFloodingStatus.setStatus("current")
_Hh3cIgmpSnoopingVlanStatusTable_Object = MibTable
hh3cIgmpSnoopingVlanStatusTable = _Hh3cIgmpSnoopingVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingVlanStatusTable.setStatus("current")
_Hh3cIgmpSnoopingVlanStatusEntry_Object = MibTableRow
hh3cIgmpSnoopingVlanStatusEntry = _Hh3cIgmpSnoopingVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9, 1)
)
hh3cIgmpSnoopingVlanStatusEntry.setIndexNames(
    (0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingVlanID"),
)
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingVlanStatusEntry.setStatus("current")


class _Hh3cIgmpSnoopingVlanID_Type(Integer32):
    """Custom type hh3cIgmpSnoopingVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cIgmpSnoopingVlanID_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingVlanID_Object = MibTableColumn
hh3cIgmpSnoopingVlanID = _Hh3cIgmpSnoopingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9, 1, 1),
    _Hh3cIgmpSnoopingVlanID_Type()
)
hh3cIgmpSnoopingVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingVlanID.setStatus("current")


class _Hh3cIgmpSnoopingVlanEnabled_Type(EnabledStatus):
    """Custom type hh3cIgmpSnoopingVlanEnabled based on EnabledStatus"""


_Hh3cIgmpSnoopingVlanEnabled_Object = MibTableColumn
hh3cIgmpSnoopingVlanEnabled = _Hh3cIgmpSnoopingVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9, 1, 2),
    _Hh3cIgmpSnoopingVlanEnabled_Type()
)
hh3cIgmpSnoopingVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingVlanEnabled.setStatus("current")
_Hh3cIgmpSnoopingStatsObjects_ObjectIdentity = ObjectIdentity
hh3cIgmpSnoopingStatsObjects = _Hh3cIgmpSnoopingStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10)
)
_Hh3cRecvIGMPGQueryNum_Type = Counter32
_Hh3cRecvIGMPGQueryNum_Object = MibScalar
hh3cRecvIGMPGQueryNum = _Hh3cRecvIGMPGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 1),
    _Hh3cRecvIGMPGQueryNum_Type()
)
hh3cRecvIGMPGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRecvIGMPGQueryNum.setStatus("current")
_Hh3cRecvIGMPSQueryNum_Type = Counter32
_Hh3cRecvIGMPSQueryNum_Object = MibScalar
hh3cRecvIGMPSQueryNum = _Hh3cRecvIGMPSQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 2),
    _Hh3cRecvIGMPSQueryNum_Type()
)
hh3cRecvIGMPSQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRecvIGMPSQueryNum.setStatus("current")
_Hh3cRecvIGMPV1ReportNum_Type = Counter32
_Hh3cRecvIGMPV1ReportNum_Object = MibScalar
hh3cRecvIGMPV1ReportNum = _Hh3cRecvIGMPV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 3),
    _Hh3cRecvIGMPV1ReportNum_Type()
)
hh3cRecvIGMPV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRecvIGMPV1ReportNum.setStatus("current")
_Hh3cRecvIGMPV2ReportNum_Type = Counter32
_Hh3cRecvIGMPV2ReportNum_Object = MibScalar
hh3cRecvIGMPV2ReportNum = _Hh3cRecvIGMPV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 4),
    _Hh3cRecvIGMPV2ReportNum_Type()
)
hh3cRecvIGMPV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRecvIGMPV2ReportNum.setStatus("current")
_Hh3cRecvIGMPLeaveNum_Type = Counter32
_Hh3cRecvIGMPLeaveNum_Object = MibScalar
hh3cRecvIGMPLeaveNum = _Hh3cRecvIGMPLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 5),
    _Hh3cRecvIGMPLeaveNum_Type()
)
hh3cRecvIGMPLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRecvIGMPLeaveNum.setStatus("current")
_Hh3cRecvErrorIGMPPacketNum_Type = Counter32
_Hh3cRecvErrorIGMPPacketNum_Object = MibScalar
hh3cRecvErrorIGMPPacketNum = _Hh3cRecvErrorIGMPPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 6),
    _Hh3cRecvErrorIGMPPacketNum_Type()
)
hh3cRecvErrorIGMPPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRecvErrorIGMPPacketNum.setStatus("current")
_Hh3cSentIGMPSQueryNum_Type = Counter32
_Hh3cSentIGMPSQueryNum_Object = MibScalar
hh3cSentIGMPSQueryNum = _Hh3cSentIGMPSQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 7),
    _Hh3cSentIGMPSQueryNum_Type()
)
hh3cSentIGMPSQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSentIGMPSQueryNum.setStatus("current")


class _Hh3cIgmpSnoopingClearStats_Type(Integer32):
    """Custom type hh3cIgmpSnoopingClearStats based on Integer32"""
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


_Hh3cIgmpSnoopingClearStats_Type.__name__ = "Integer32"
_Hh3cIgmpSnoopingClearStats_Object = MibScalar
hh3cIgmpSnoopingClearStats = _Hh3cIgmpSnoopingClearStats_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 8),
    _Hh3cIgmpSnoopingClearStats_Type()
)
hh3cIgmpSnoopingClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIgmpSnoopingClearStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswIGSP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cLswIgmpsnoopingMib": hh3cLswIgmpsnoopingMib,
       "hh3cLswIgmpsnoopingMibObject": hh3cLswIgmpsnoopingMibObject,
       "hh3cIgmpSnoopingStatus": hh3cIgmpSnoopingStatus,
       "hh3cIgmpSnoopingRouterPortAge": hh3cIgmpSnoopingRouterPortAge,
       "hh3cIgmpSnoopingResponseTime": hh3cIgmpSnoopingResponseTime,
       "hh3cIgmpSnoopingHostTime": hh3cIgmpSnoopingHostTime,
       "hh3cIgmpSnoopingGroupLimitTable": hh3cIgmpSnoopingGroupLimitTable,
       "hh3cIgmpSnoopingGroupLimitEntry": hh3cIgmpSnoopingGroupLimitEntry,
       "hh3cIgmpSnoopingGroupIfIndex": hh3cIgmpSnoopingGroupIfIndex,
       "hh3cIgmpSnoopingGroupLimitNumber": hh3cIgmpSnoopingGroupLimitNumber,
       "hh3cIgmpSnoopingFastLeaveTable": hh3cIgmpSnoopingFastLeaveTable,
       "hh3cIgmpSnoopingFastLeaveEntry": hh3cIgmpSnoopingFastLeaveEntry,
       "hh3cIgmpSnoopingFastLeaveIfIndex": hh3cIgmpSnoopingFastLeaveIfIndex,
       "hh3cIgmpSnoopingFastLeaveStatus": hh3cIgmpSnoopingFastLeaveStatus,
       "hh3cIgmpSnoopingGroupPolicyTable": hh3cIgmpSnoopingGroupPolicyTable,
       "hh3cIgmpSnoopingGroupPolicyEntry": hh3cIgmpSnoopingGroupPolicyEntry,
       "hh3cIgmpSnoopingGroupPolicyIfIndex": hh3cIgmpSnoopingGroupPolicyIfIndex,
       "hh3cIgmpSnoopingGroupPolicyVlanID": hh3cIgmpSnoopingGroupPolicyVlanID,
       "hh3cIgmpSnoopingGroupPolicyParameter": hh3cIgmpSnoopingGroupPolicyParameter,
       "hh3cIgmpSnoopingGroupPolicyStatus": hh3cIgmpSnoopingGroupPolicyStatus,
       "hh3cIgmpSnoopingNonFloodingStatus": hh3cIgmpSnoopingNonFloodingStatus,
       "hh3cIgmpSnoopingVlanStatusTable": hh3cIgmpSnoopingVlanStatusTable,
       "hh3cIgmpSnoopingVlanStatusEntry": hh3cIgmpSnoopingVlanStatusEntry,
       "hh3cIgmpSnoopingVlanID": hh3cIgmpSnoopingVlanID,
       "hh3cIgmpSnoopingVlanEnabled": hh3cIgmpSnoopingVlanEnabled,
       "hh3cIgmpSnoopingStatsObjects": hh3cIgmpSnoopingStatsObjects,
       "hh3cRecvIGMPGQueryNum": hh3cRecvIGMPGQueryNum,
       "hh3cRecvIGMPSQueryNum": hh3cRecvIGMPSQueryNum,
       "hh3cRecvIGMPV1ReportNum": hh3cRecvIGMPV1ReportNum,
       "hh3cRecvIGMPV2ReportNum": hh3cRecvIGMPV2ReportNum,
       "hh3cRecvIGMPLeaveNum": hh3cRecvIGMPLeaveNum,
       "hh3cRecvErrorIGMPPacketNum": hh3cRecvErrorIGMPPacketNum,
       "hh3cSentIGMPSQueryNum": hh3cSentIGMPSQueryNum,
       "hh3cIgmpSnoopingClearStats": hh3cIgmpSnoopingClearStats}
)
