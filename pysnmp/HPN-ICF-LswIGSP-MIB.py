# SNMP MIB module (HPN-ICF-LswIGSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswIGSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:54 2024
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

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfLswIgmpsnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7)
)
hpnicfLswIgmpsnoopingMib.setRevisions(
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

_HpnicfLswIgmpsnoopingMibObject_ObjectIdentity = ObjectIdentity
hpnicfLswIgmpsnoopingMibObject = _HpnicfLswIgmpsnoopingMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1)
)
_HpnicfIgmpSnoopingStatus_Type = EnabledStatus
_HpnicfIgmpSnoopingStatus_Object = MibScalar
hpnicfIgmpSnoopingStatus = _HpnicfIgmpSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 1),
    _HpnicfIgmpSnoopingStatus_Type()
)
hpnicfIgmpSnoopingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingStatus.setStatus("current")


class _HpnicfIgmpSnoopingRouterPortAge_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingRouterPortAge based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HpnicfIgmpSnoopingRouterPortAge_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingRouterPortAge_Object = MibScalar
hpnicfIgmpSnoopingRouterPortAge = _HpnicfIgmpSnoopingRouterPortAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 2),
    _HpnicfIgmpSnoopingRouterPortAge_Type()
)
hpnicfIgmpSnoopingRouterPortAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingRouterPortAge.setStatus("current")


class _HpnicfIgmpSnoopingResponseTime_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HpnicfIgmpSnoopingResponseTime_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingResponseTime_Object = MibScalar
hpnicfIgmpSnoopingResponseTime = _HpnicfIgmpSnoopingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 3),
    _HpnicfIgmpSnoopingResponseTime_Type()
)
hpnicfIgmpSnoopingResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingResponseTime.setStatus("current")


class _HpnicfIgmpSnoopingHostTime_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingHostTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_HpnicfIgmpSnoopingHostTime_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingHostTime_Object = MibScalar
hpnicfIgmpSnoopingHostTime = _HpnicfIgmpSnoopingHostTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 4),
    _HpnicfIgmpSnoopingHostTime_Type()
)
hpnicfIgmpSnoopingHostTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingHostTime.setStatus("current")
_HpnicfIgmpSnoopingGroupLimitTable_Object = MibTable
hpnicfIgmpSnoopingGroupLimitTable = _HpnicfIgmpSnoopingGroupLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupLimitTable.setStatus("current")
_HpnicfIgmpSnoopingGroupLimitEntry_Object = MibTableRow
hpnicfIgmpSnoopingGroupLimitEntry = _HpnicfIgmpSnoopingGroupLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5, 1)
)
hpnicfIgmpSnoopingGroupLimitEntry.setIndexNames(
    (0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingGroupIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupLimitEntry.setStatus("current")
_HpnicfIgmpSnoopingGroupIfIndex_Type = InterfaceIndex
_HpnicfIgmpSnoopingGroupIfIndex_Object = MibTableColumn
hpnicfIgmpSnoopingGroupIfIndex = _HpnicfIgmpSnoopingGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5, 1, 1),
    _HpnicfIgmpSnoopingGroupIfIndex_Type()
)
hpnicfIgmpSnoopingGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupIfIndex.setStatus("current")


class _HpnicfIgmpSnoopingGroupLimitNumber_Type(Unsigned32):
    """Custom type hpnicfIgmpSnoopingGroupLimitNumber based on Unsigned32"""
    defaultValue = 4294967295


_HpnicfIgmpSnoopingGroupLimitNumber_Object = MibTableColumn
hpnicfIgmpSnoopingGroupLimitNumber = _HpnicfIgmpSnoopingGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5, 1, 2),
    _HpnicfIgmpSnoopingGroupLimitNumber_Type()
)
hpnicfIgmpSnoopingGroupLimitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupLimitNumber.setStatus("current")
_HpnicfIgmpSnoopingFastLeaveTable_Object = MibTable
hpnicfIgmpSnoopingFastLeaveTable = _HpnicfIgmpSnoopingFastLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingFastLeaveTable.setStatus("current")
_HpnicfIgmpSnoopingFastLeaveEntry_Object = MibTableRow
hpnicfIgmpSnoopingFastLeaveEntry = _HpnicfIgmpSnoopingFastLeaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6, 1)
)
hpnicfIgmpSnoopingFastLeaveEntry.setIndexNames(
    (0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingFastLeaveIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingFastLeaveEntry.setStatus("current")
_HpnicfIgmpSnoopingFastLeaveIfIndex_Type = InterfaceIndex
_HpnicfIgmpSnoopingFastLeaveIfIndex_Object = MibTableColumn
hpnicfIgmpSnoopingFastLeaveIfIndex = _HpnicfIgmpSnoopingFastLeaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6, 1, 1),
    _HpnicfIgmpSnoopingFastLeaveIfIndex_Type()
)
hpnicfIgmpSnoopingFastLeaveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingFastLeaveIfIndex.setStatus("current")


class _HpnicfIgmpSnoopingFastLeaveStatus_Type(EnabledStatus):
    """Custom type hpnicfIgmpSnoopingFastLeaveStatus based on EnabledStatus"""
    defaultValue = 2


_HpnicfIgmpSnoopingFastLeaveStatus_Object = MibTableColumn
hpnicfIgmpSnoopingFastLeaveStatus = _HpnicfIgmpSnoopingFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6, 1, 2),
    _HpnicfIgmpSnoopingFastLeaveStatus_Type()
)
hpnicfIgmpSnoopingFastLeaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingFastLeaveStatus.setStatus("current")
_HpnicfIgmpSnoopingGroupPolicyTable_Object = MibTable
hpnicfIgmpSnoopingGroupPolicyTable = _HpnicfIgmpSnoopingGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupPolicyTable.setStatus("current")
_HpnicfIgmpSnoopingGroupPolicyEntry_Object = MibTableRow
hpnicfIgmpSnoopingGroupPolicyEntry = _HpnicfIgmpSnoopingGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1)
)
hpnicfIgmpSnoopingGroupPolicyEntry.setIndexNames(
    (0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingGroupPolicyIfIndex"),
    (0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingGroupPolicyVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupPolicyEntry.setStatus("current")
_HpnicfIgmpSnoopingGroupPolicyIfIndex_Type = InterfaceIndex
_HpnicfIgmpSnoopingGroupPolicyIfIndex_Object = MibTableColumn
hpnicfIgmpSnoopingGroupPolicyIfIndex = _HpnicfIgmpSnoopingGroupPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 1),
    _HpnicfIgmpSnoopingGroupPolicyIfIndex_Type()
)
hpnicfIgmpSnoopingGroupPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupPolicyIfIndex.setStatus("current")


class _HpnicfIgmpSnoopingGroupPolicyVlanID_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingGroupPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfIgmpSnoopingGroupPolicyVlanID_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingGroupPolicyVlanID_Object = MibTableColumn
hpnicfIgmpSnoopingGroupPolicyVlanID = _HpnicfIgmpSnoopingGroupPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 2),
    _HpnicfIgmpSnoopingGroupPolicyVlanID_Type()
)
hpnicfIgmpSnoopingGroupPolicyVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupPolicyVlanID.setStatus("current")


class _HpnicfIgmpSnoopingGroupPolicyParameter_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingGroupPolicyParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2999),
    )


_HpnicfIgmpSnoopingGroupPolicyParameter_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingGroupPolicyParameter_Object = MibTableColumn
hpnicfIgmpSnoopingGroupPolicyParameter = _HpnicfIgmpSnoopingGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 3),
    _HpnicfIgmpSnoopingGroupPolicyParameter_Type()
)
hpnicfIgmpSnoopingGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupPolicyParameter.setStatus("current")
_HpnicfIgmpSnoopingGroupPolicyStatus_Type = RowStatus
_HpnicfIgmpSnoopingGroupPolicyStatus_Object = MibTableColumn
hpnicfIgmpSnoopingGroupPolicyStatus = _HpnicfIgmpSnoopingGroupPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 4),
    _HpnicfIgmpSnoopingGroupPolicyStatus_Type()
)
hpnicfIgmpSnoopingGroupPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingGroupPolicyStatus.setStatus("current")
_HpnicfIgmpSnoopingNonFloodingStatus_Type = EnabledStatus
_HpnicfIgmpSnoopingNonFloodingStatus_Object = MibScalar
hpnicfIgmpSnoopingNonFloodingStatus = _HpnicfIgmpSnoopingNonFloodingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 8),
    _HpnicfIgmpSnoopingNonFloodingStatus_Type()
)
hpnicfIgmpSnoopingNonFloodingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingNonFloodingStatus.setStatus("current")
_HpnicfIgmpSnoopingVlanStatusTable_Object = MibTable
hpnicfIgmpSnoopingVlanStatusTable = _HpnicfIgmpSnoopingVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingVlanStatusTable.setStatus("current")
_HpnicfIgmpSnoopingVlanStatusEntry_Object = MibTableRow
hpnicfIgmpSnoopingVlanStatusEntry = _HpnicfIgmpSnoopingVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9, 1)
)
hpnicfIgmpSnoopingVlanStatusEntry.setIndexNames(
    (0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingVlanStatusEntry.setStatus("current")


class _HpnicfIgmpSnoopingVlanID_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfIgmpSnoopingVlanID_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingVlanID_Object = MibTableColumn
hpnicfIgmpSnoopingVlanID = _HpnicfIgmpSnoopingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9, 1, 1),
    _HpnicfIgmpSnoopingVlanID_Type()
)
hpnicfIgmpSnoopingVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingVlanID.setStatus("current")


class _HpnicfIgmpSnoopingVlanEnabled_Type(EnabledStatus):
    """Custom type hpnicfIgmpSnoopingVlanEnabled based on EnabledStatus"""


_HpnicfIgmpSnoopingVlanEnabled_Object = MibTableColumn
hpnicfIgmpSnoopingVlanEnabled = _HpnicfIgmpSnoopingVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9, 1, 2),
    _HpnicfIgmpSnoopingVlanEnabled_Type()
)
hpnicfIgmpSnoopingVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingVlanEnabled.setStatus("current")
_HpnicfIgmpSnoopingStatsObjects_ObjectIdentity = ObjectIdentity
hpnicfIgmpSnoopingStatsObjects = _HpnicfIgmpSnoopingStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10)
)
_HpnicfRecvIGMPGQueryNum_Type = Counter32
_HpnicfRecvIGMPGQueryNum_Object = MibScalar
hpnicfRecvIGMPGQueryNum = _HpnicfRecvIGMPGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 1),
    _HpnicfRecvIGMPGQueryNum_Type()
)
hpnicfRecvIGMPGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRecvIGMPGQueryNum.setStatus("current")
_HpnicfRecvIGMPSQueryNum_Type = Counter32
_HpnicfRecvIGMPSQueryNum_Object = MibScalar
hpnicfRecvIGMPSQueryNum = _HpnicfRecvIGMPSQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 2),
    _HpnicfRecvIGMPSQueryNum_Type()
)
hpnicfRecvIGMPSQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRecvIGMPSQueryNum.setStatus("current")
_HpnicfRecvIGMPV1ReportNum_Type = Counter32
_HpnicfRecvIGMPV1ReportNum_Object = MibScalar
hpnicfRecvIGMPV1ReportNum = _HpnicfRecvIGMPV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 3),
    _HpnicfRecvIGMPV1ReportNum_Type()
)
hpnicfRecvIGMPV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRecvIGMPV1ReportNum.setStatus("current")
_HpnicfRecvIGMPV2ReportNum_Type = Counter32
_HpnicfRecvIGMPV2ReportNum_Object = MibScalar
hpnicfRecvIGMPV2ReportNum = _HpnicfRecvIGMPV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 4),
    _HpnicfRecvIGMPV2ReportNum_Type()
)
hpnicfRecvIGMPV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRecvIGMPV2ReportNum.setStatus("current")
_HpnicfRecvIGMPLeaveNum_Type = Counter32
_HpnicfRecvIGMPLeaveNum_Object = MibScalar
hpnicfRecvIGMPLeaveNum = _HpnicfRecvIGMPLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 5),
    _HpnicfRecvIGMPLeaveNum_Type()
)
hpnicfRecvIGMPLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRecvIGMPLeaveNum.setStatus("current")
_HpnicfRecvErrorIGMPPacketNum_Type = Counter32
_HpnicfRecvErrorIGMPPacketNum_Object = MibScalar
hpnicfRecvErrorIGMPPacketNum = _HpnicfRecvErrorIGMPPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 6),
    _HpnicfRecvErrorIGMPPacketNum_Type()
)
hpnicfRecvErrorIGMPPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRecvErrorIGMPPacketNum.setStatus("current")
_HpnicfSentIGMPSQueryNum_Type = Counter32
_HpnicfSentIGMPSQueryNum_Object = MibScalar
hpnicfSentIGMPSQueryNum = _HpnicfSentIGMPSQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 7),
    _HpnicfSentIGMPSQueryNum_Type()
)
hpnicfSentIGMPSQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSentIGMPSQueryNum.setStatus("current")


class _HpnicfIgmpSnoopingClearStats_Type(Integer32):
    """Custom type hpnicfIgmpSnoopingClearStats based on Integer32"""
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


_HpnicfIgmpSnoopingClearStats_Type.__name__ = "Integer32"
_HpnicfIgmpSnoopingClearStats_Object = MibScalar
hpnicfIgmpSnoopingClearStats = _HpnicfIgmpSnoopingClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 8),
    _HpnicfIgmpSnoopingClearStats_Type()
)
hpnicfIgmpSnoopingClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIgmpSnoopingClearStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswIGSP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hpnicfLswIgmpsnoopingMib": hpnicfLswIgmpsnoopingMib,
       "hpnicfLswIgmpsnoopingMibObject": hpnicfLswIgmpsnoopingMibObject,
       "hpnicfIgmpSnoopingStatus": hpnicfIgmpSnoopingStatus,
       "hpnicfIgmpSnoopingRouterPortAge": hpnicfIgmpSnoopingRouterPortAge,
       "hpnicfIgmpSnoopingResponseTime": hpnicfIgmpSnoopingResponseTime,
       "hpnicfIgmpSnoopingHostTime": hpnicfIgmpSnoopingHostTime,
       "hpnicfIgmpSnoopingGroupLimitTable": hpnicfIgmpSnoopingGroupLimitTable,
       "hpnicfIgmpSnoopingGroupLimitEntry": hpnicfIgmpSnoopingGroupLimitEntry,
       "hpnicfIgmpSnoopingGroupIfIndex": hpnicfIgmpSnoopingGroupIfIndex,
       "hpnicfIgmpSnoopingGroupLimitNumber": hpnicfIgmpSnoopingGroupLimitNumber,
       "hpnicfIgmpSnoopingFastLeaveTable": hpnicfIgmpSnoopingFastLeaveTable,
       "hpnicfIgmpSnoopingFastLeaveEntry": hpnicfIgmpSnoopingFastLeaveEntry,
       "hpnicfIgmpSnoopingFastLeaveIfIndex": hpnicfIgmpSnoopingFastLeaveIfIndex,
       "hpnicfIgmpSnoopingFastLeaveStatus": hpnicfIgmpSnoopingFastLeaveStatus,
       "hpnicfIgmpSnoopingGroupPolicyTable": hpnicfIgmpSnoopingGroupPolicyTable,
       "hpnicfIgmpSnoopingGroupPolicyEntry": hpnicfIgmpSnoopingGroupPolicyEntry,
       "hpnicfIgmpSnoopingGroupPolicyIfIndex": hpnicfIgmpSnoopingGroupPolicyIfIndex,
       "hpnicfIgmpSnoopingGroupPolicyVlanID": hpnicfIgmpSnoopingGroupPolicyVlanID,
       "hpnicfIgmpSnoopingGroupPolicyParameter": hpnicfIgmpSnoopingGroupPolicyParameter,
       "hpnicfIgmpSnoopingGroupPolicyStatus": hpnicfIgmpSnoopingGroupPolicyStatus,
       "hpnicfIgmpSnoopingNonFloodingStatus": hpnicfIgmpSnoopingNonFloodingStatus,
       "hpnicfIgmpSnoopingVlanStatusTable": hpnicfIgmpSnoopingVlanStatusTable,
       "hpnicfIgmpSnoopingVlanStatusEntry": hpnicfIgmpSnoopingVlanStatusEntry,
       "hpnicfIgmpSnoopingVlanID": hpnicfIgmpSnoopingVlanID,
       "hpnicfIgmpSnoopingVlanEnabled": hpnicfIgmpSnoopingVlanEnabled,
       "hpnicfIgmpSnoopingStatsObjects": hpnicfIgmpSnoopingStatsObjects,
       "hpnicfRecvIGMPGQueryNum": hpnicfRecvIGMPGQueryNum,
       "hpnicfRecvIGMPSQueryNum": hpnicfRecvIGMPSQueryNum,
       "hpnicfRecvIGMPV1ReportNum": hpnicfRecvIGMPV1ReportNum,
       "hpnicfRecvIGMPV2ReportNum": hpnicfRecvIGMPV2ReportNum,
       "hpnicfRecvIGMPLeaveNum": hpnicfRecvIGMPLeaveNum,
       "hpnicfRecvErrorIGMPPacketNum": hpnicfRecvErrorIGMPPacketNum,
       "hpnicfSentIGMPSQueryNum": hpnicfSentIGMPSQueryNum,
       "hpnicfIgmpSnoopingClearStats": hpnicfIgmpSnoopingClearStats}
)
