# SNMP MIB module (HUAWEI-TRANSPARENTBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TRANSPARENTBRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:15 2024
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

(hwBaseTrapEventType,
 hwBaseTrapProbableCause,
 hwBaseTrapSeverity) = mibBuilder.importSymbols(
    "HUAWEI-BASE-TRAP-MIB",
    "hwBaseTrapEventType",
    "hwBaseTrapProbableCause",
    "hwBaseTrapSeverity")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwTransparentBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1)
)
hwTransparentBridge.setRevisions(
        ("2015-05-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTransparentBridgeMIB_ObjectIdentity = ObjectIdentity
hwTransparentBridgeMIB = _HwTransparentBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242)
)
_HwTPBridgeMngObjects_ObjectIdentity = ObjectIdentity
hwTPBridgeMngObjects = _HwTPBridgeMngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1)
)
_HwTPBridgeBase_ObjectIdentity = ObjectIdentity
hwTPBridgeBase = _HwTPBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1)
)
_HwTPBridgeMIBTable_Object = MibTable
hwTPBridgeMIBTable = _HwTPBridgeMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwTPBridgeMIBTable.setStatus("current")
_HwTPBridgeMIBEntry_Object = MibTableRow
hwTPBridgeMIBEntry = _HwTPBridgeMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1)
)
hwTPBridgeMIBEntry.setIndexNames(
    (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeId"),
)
if mibBuilder.loadTexts:
    hwTPBridgeMIBEntry.setStatus("current")


class _HwTPBridgeId_Type(Integer32):
    """Custom type hwTPBridgeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwTPBridgeId_Type.__name__ = "Integer32"
_HwTPBridgeId_Object = MibTableColumn
hwTPBridgeId = _HwTPBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 1),
    _HwTPBridgeId_Type()
)
hwTPBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTPBridgeId.setStatus("current")
_HwTPBridgeMacLearn_Type = EnabledStatus
_HwTPBridgeMacLearn_Object = MibTableColumn
hwTPBridgeMacLearn = _HwTPBridgeMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 2),
    _HwTPBridgeMacLearn_Type()
)
hwTPBridgeMacLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeMacLearn.setStatus("current")
_HwTPBridgeRoutingIp_Type = EnabledStatus
_HwTPBridgeRoutingIp_Object = MibTableColumn
hwTPBridgeRoutingIp = _HwTPBridgeRoutingIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 3),
    _HwTPBridgeRoutingIp_Type()
)
hwTPBridgeRoutingIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeRoutingIp.setStatus("current")
_HwTPBridgeBridgingIp_Type = EnabledStatus
_HwTPBridgeBridgingIp_Object = MibTableColumn
hwTPBridgeBridgingIp = _HwTPBridgeBridgingIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 4),
    _HwTPBridgeBridgingIp_Type()
)
hwTPBridgeBridgingIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeBridgingIp.setStatus("current")
_HwTPBridgeBridgingOther_Type = EnabledStatus
_HwTPBridgeBridgingOther_Object = MibTableColumn
hwTPBridgeBridgingOther = _HwTPBridgeBridgingOther_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 5),
    _HwTPBridgeBridgingOther_Type()
)
hwTPBridgeBridgingOther.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeBridgingOther.setStatus("current")


class _HwTPBridgeAdminStatus_Type(EnabledStatus):
    """Custom type hwTPBridgeAdminStatus based on EnabledStatus"""
    defaultValue = 1


_HwTPBridgeAdminStatus_Object = MibTableColumn
hwTPBridgeAdminStatus = _HwTPBridgeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 6),
    _HwTPBridgeAdminStatus_Type()
)
hwTPBridgeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeAdminStatus.setStatus("current")
_HwTPBridgeRowStatus_Type = RowStatus
_HwTPBridgeRowStatus_Object = MibTableColumn
hwTPBridgeRowStatus = _HwTPBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 7),
    _HwTPBridgeRowStatus_Type()
)
hwTPBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeRowStatus.setStatus("current")
_HwTPBridgeMemberMIBTable_Object = MibTable
hwTPBridgeMemberMIBTable = _HwTPBridgeMemberMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwTPBridgeMemberMIBTable.setStatus("current")
_HwTPBridgeMemberMIBEntry_Object = MibTableRow
hwTPBridgeMemberMIBEntry = _HwTPBridgeMemberMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1)
)
hwTPBridgeMemberMIBEntry.setIndexNames(
    (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeId"),
    (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberIfIndex"),
)
if mibBuilder.loadTexts:
    hwTPBridgeMemberMIBEntry.setStatus("current")
_HwTPBridgeMemberIfIndex_Type = InterfaceIndex
_HwTPBridgeMemberIfIndex_Object = MibTableColumn
hwTPBridgeMemberIfIndex = _HwTPBridgeMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 1),
    _HwTPBridgeMemberIfIndex_Type()
)
hwTPBridgeMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTPBridgeMemberIfIndex.setStatus("current")
_HwTPBridgeMemberVlanTransparent_Type = EnabledStatus
_HwTPBridgeMemberVlanTransparent_Object = MibTableColumn
hwTPBridgeMemberVlanTransparent = _HwTPBridgeMemberVlanTransparent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 2),
    _HwTPBridgeMemberVlanTransparent_Type()
)
hwTPBridgeMemberVlanTransparent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeMemberVlanTransparent.setStatus("current")
_HwTPBridgeMemberRowStatus_Type = RowStatus
_HwTPBridgeMemberRowStatus_Object = MibTableColumn
hwTPBridgeMemberRowStatus = _HwTPBridgeMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 3),
    _HwTPBridgeMemberRowStatus_Type()
)
hwTPBridgeMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTPBridgeMemberRowStatus.setStatus("current")
_HwTPBridgeApply_ObjectIdentity = ObjectIdentity
hwTPBridgeApply = _HwTPBridgeApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2)
)
_HwTPBridgeStatTable_Object = MibTable
hwTPBridgeStatTable = _HwTPBridgeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwTPBridgeStatTable.setStatus("current")
_HwTPBridgeStatEntry_Object = MibTableRow
hwTPBridgeStatEntry = _HwTPBridgeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1)
)
hwTPBridgeStatEntry.setIndexNames(
    (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatBridgeId"),
)
if mibBuilder.loadTexts:
    hwTPBridgeStatEntry.setStatus("current")


class _HwTPBridgeStatBridgeId_Type(Integer32):
    """Custom type hwTPBridgeStatBridgeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwTPBridgeStatBridgeId_Type.__name__ = "Integer32"
_HwTPBridgeStatBridgeId_Object = MibTableColumn
hwTPBridgeStatBridgeId = _HwTPBridgeStatBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 1),
    _HwTPBridgeStatBridgeId_Type()
)
hwTPBridgeStatBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTPBridgeStatBridgeId.setStatus("current")
_HwTPBridgeStatInTotalPkts_Type = Counter64
_HwTPBridgeStatInTotalPkts_Object = MibTableColumn
hwTPBridgeStatInTotalPkts = _HwTPBridgeStatInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 2),
    _HwTPBridgeStatInTotalPkts_Type()
)
hwTPBridgeStatInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatInTotalPkts.setStatus("current")
_HwTPBridgeStatInBPDUPkts_Type = Counter64
_HwTPBridgeStatInBPDUPkts_Object = MibTableColumn
hwTPBridgeStatInBPDUPkts = _HwTPBridgeStatInBPDUPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 3),
    _HwTPBridgeStatInBPDUPkts_Type()
)
hwTPBridgeStatInBPDUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatInBPDUPkts.setStatus("current")
_HwTPBridgeStatInUcastkts_Type = Counter64
_HwTPBridgeStatInUcastkts_Object = MibTableColumn
hwTPBridgeStatInUcastkts = _HwTPBridgeStatInUcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 4),
    _HwTPBridgeStatInUcastkts_Type()
)
hwTPBridgeStatInUcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatInUcastkts.setStatus("current")
_HwTPBridgeStatInMcastkts_Type = Counter64
_HwTPBridgeStatInMcastkts_Object = MibTableColumn
hwTPBridgeStatInMcastkts = _HwTPBridgeStatInMcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 5),
    _HwTPBridgeStatInMcastkts_Type()
)
hwTPBridgeStatInMcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatInMcastkts.setStatus("current")
_HwTPBridgeStatInBcastkts_Type = Counter64
_HwTPBridgeStatInBcastkts_Object = MibTableColumn
hwTPBridgeStatInBcastkts = _HwTPBridgeStatInBcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 6),
    _HwTPBridgeStatInBcastkts_Type()
)
hwTPBridgeStatInBcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatInBcastkts.setStatus("current")
_HwTPBridgeStatOutTotalPkts_Type = Counter64
_HwTPBridgeStatOutTotalPkts_Object = MibTableColumn
hwTPBridgeStatOutTotalPkts = _HwTPBridgeStatOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 7),
    _HwTPBridgeStatOutTotalPkts_Type()
)
hwTPBridgeStatOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatOutTotalPkts.setStatus("current")
_HwTPBridgeStatOutBPDUPkts_Type = Counter64
_HwTPBridgeStatOutBPDUPkts_Object = MibTableColumn
hwTPBridgeStatOutBPDUPkts = _HwTPBridgeStatOutBPDUPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 8),
    _HwTPBridgeStatOutBPDUPkts_Type()
)
hwTPBridgeStatOutBPDUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatOutBPDUPkts.setStatus("current")
_HwTPBridgeStatOutUcastkts_Type = Counter64
_HwTPBridgeStatOutUcastkts_Object = MibTableColumn
hwTPBridgeStatOutUcastkts = _HwTPBridgeStatOutUcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 9),
    _HwTPBridgeStatOutUcastkts_Type()
)
hwTPBridgeStatOutUcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatOutUcastkts.setStatus("current")
_HwTPBridgeStatOutMcastkts_Type = Counter64
_HwTPBridgeStatOutMcastkts_Object = MibTableColumn
hwTPBridgeStatOutMcastkts = _HwTPBridgeStatOutMcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 10),
    _HwTPBridgeStatOutMcastkts_Type()
)
hwTPBridgeStatOutMcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatOutMcastkts.setStatus("current")
_HwTPBridgeStatOutBcastkts_Type = Counter64
_HwTPBridgeStatOutBcastkts_Object = MibTableColumn
hwTPBridgeStatOutBcastkts = _HwTPBridgeStatOutBcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 11),
    _HwTPBridgeStatOutBcastkts_Type()
)
hwTPBridgeStatOutBcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeStatOutBcastkts.setStatus("current")
_HwTPBridgeStatResetFlag_Type = EnabledStatus
_HwTPBridgeStatResetFlag_Object = MibTableColumn
hwTPBridgeStatResetFlag = _HwTPBridgeStatResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 12),
    _HwTPBridgeStatResetFlag_Type()
)
hwTPBridgeStatResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTPBridgeStatResetFlag.setStatus("current")
_HwTPBridgeMemberStatTable_Object = MibTable
hwTPBridgeMemberStatTable = _HwTPBridgeMemberStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatTable.setStatus("current")
_HwTPBridgeMemberStatEntry_Object = MibTableRow
hwTPBridgeMemberStatEntry = _HwTPBridgeMemberStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1)
)
hwTPBridgeMemberStatEntry.setIndexNames(
    (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatIfIndex"),
)
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatEntry.setStatus("current")
_HwTPBridgeMemberStatIfIndex_Type = InterfaceIndex
_HwTPBridgeMemberStatIfIndex_Object = MibTableColumn
hwTPBridgeMemberStatIfIndex = _HwTPBridgeMemberStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 1),
    _HwTPBridgeMemberStatIfIndex_Type()
)
hwTPBridgeMemberStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatIfIndex.setStatus("current")
_HwTPBridgeMemberStatInTotalPkts_Type = Counter64
_HwTPBridgeMemberStatInTotalPkts_Object = MibTableColumn
hwTPBridgeMemberStatInTotalPkts = _HwTPBridgeMemberStatInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 2),
    _HwTPBridgeMemberStatInTotalPkts_Type()
)
hwTPBridgeMemberStatInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatInTotalPkts.setStatus("current")
_HwTPBridgeMemberStatInBPDUPkts_Type = Counter64
_HwTPBridgeMemberStatInBPDUPkts_Object = MibTableColumn
hwTPBridgeMemberStatInBPDUPkts = _HwTPBridgeMemberStatInBPDUPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 3),
    _HwTPBridgeMemberStatInBPDUPkts_Type()
)
hwTPBridgeMemberStatInBPDUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatInBPDUPkts.setStatus("current")
_HwTPBridgeMemberStatInUcastkts_Type = Counter64
_HwTPBridgeMemberStatInUcastkts_Object = MibTableColumn
hwTPBridgeMemberStatInUcastkts = _HwTPBridgeMemberStatInUcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 4),
    _HwTPBridgeMemberStatInUcastkts_Type()
)
hwTPBridgeMemberStatInUcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatInUcastkts.setStatus("current")
_HwTPBridgeMemberStatInMcastkts_Type = Counter64
_HwTPBridgeMemberStatInMcastkts_Object = MibTableColumn
hwTPBridgeMemberStatInMcastkts = _HwTPBridgeMemberStatInMcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 5),
    _HwTPBridgeMemberStatInMcastkts_Type()
)
hwTPBridgeMemberStatInMcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatInMcastkts.setStatus("current")
_HwTPBridgeMemberStatInBcastkts_Type = Counter64
_HwTPBridgeMemberStatInBcastkts_Object = MibTableColumn
hwTPBridgeMemberStatInBcastkts = _HwTPBridgeMemberStatInBcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 6),
    _HwTPBridgeMemberStatInBcastkts_Type()
)
hwTPBridgeMemberStatInBcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatInBcastkts.setStatus("current")
_HwTPBridgeMemberStatOutTotalPkts_Type = Counter64
_HwTPBridgeMemberStatOutTotalPkts_Object = MibTableColumn
hwTPBridgeMemberStatOutTotalPkts = _HwTPBridgeMemberStatOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 7),
    _HwTPBridgeMemberStatOutTotalPkts_Type()
)
hwTPBridgeMemberStatOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatOutTotalPkts.setStatus("current")
_HwTPBridgeMemberStatOutBPDUPkts_Type = Counter64
_HwTPBridgeMemberStatOutBPDUPkts_Object = MibTableColumn
hwTPBridgeMemberStatOutBPDUPkts = _HwTPBridgeMemberStatOutBPDUPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 8),
    _HwTPBridgeMemberStatOutBPDUPkts_Type()
)
hwTPBridgeMemberStatOutBPDUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatOutBPDUPkts.setStatus("current")
_HwTPBridgeMemberStatOutUcastkts_Type = Counter64
_HwTPBridgeMemberStatOutUcastkts_Object = MibTableColumn
hwTPBridgeMemberStatOutUcastkts = _HwTPBridgeMemberStatOutUcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 9),
    _HwTPBridgeMemberStatOutUcastkts_Type()
)
hwTPBridgeMemberStatOutUcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatOutUcastkts.setStatus("current")
_HwTPBridgeMemberStatOutMcastkts_Type = Counter64
_HwTPBridgeMemberStatOutMcastkts_Object = MibTableColumn
hwTPBridgeMemberStatOutMcastkts = _HwTPBridgeMemberStatOutMcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 10),
    _HwTPBridgeMemberStatOutMcastkts_Type()
)
hwTPBridgeMemberStatOutMcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatOutMcastkts.setStatus("current")
_HwTPBridgeMemberStatOutBcastkts_Type = Counter64
_HwTPBridgeMemberStatOutBcastkts_Object = MibTableColumn
hwTPBridgeMemberStatOutBcastkts = _HwTPBridgeMemberStatOutBcastkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 11),
    _HwTPBridgeMemberStatOutBcastkts_Type()
)
hwTPBridgeMemberStatOutBcastkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatOutBcastkts.setStatus("current")
_HwTPBridgeConformance_ObjectIdentity = ObjectIdentity
hwTPBridgeConformance = _HwTPBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2)
)
_HwTPBridgeCompliances_ObjectIdentity = ObjectIdentity
hwTPBridgeCompliances = _HwTPBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 1)
)
_HwTPBridgeGroups_ObjectIdentity = ObjectIdentity
hwTPBridgeGroups = _HwTPBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2)
)

# Managed Objects groups

hwTPBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 1)
)
hwTPBridgeGroup.setObjects(
      *(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMacLearn"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeRoutingIp"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeBridgingIp"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeBridgingOther"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeAdminStatus"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeRowStatus"))
)
if mibBuilder.loadTexts:
    hwTPBridgeGroup.setStatus("current")

hwTPBridgeMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 2)
)
hwTPBridgeMemberGroup.setObjects(
      *(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberVlanTransparent"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwTPBridgeMemberGroup.setStatus("current")

hhwTPBridgeStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 3)
)
hhwTPBridgeStatGroup.setObjects(
      *(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInTotalPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInBPDUPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInUcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInMcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInBcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutTotalPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutBPDUPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutUcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutMcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutBcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatResetFlag"))
)
if mibBuilder.loadTexts:
    hhwTPBridgeStatGroup.setStatus("current")

hwTPBridgeMemberStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 4)
)
hwTPBridgeMemberStatGroup.setObjects(
      *(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInTotalPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInBPDUPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInUcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInMcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInBcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutTotalPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutBPDUPkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutUcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutMcastkts"),
        ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutBcastkts"))
)
if mibBuilder.loadTexts:
    hwTPBridgeMemberStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwTPBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwTPBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TRANSPARENTBRIDGE-MIB",
    **{"hwTransparentBridgeMIB": hwTransparentBridgeMIB,
       "hwTransparentBridge": hwTransparentBridge,
       "hwTPBridgeMngObjects": hwTPBridgeMngObjects,
       "hwTPBridgeBase": hwTPBridgeBase,
       "hwTPBridgeMIBTable": hwTPBridgeMIBTable,
       "hwTPBridgeMIBEntry": hwTPBridgeMIBEntry,
       "hwTPBridgeId": hwTPBridgeId,
       "hwTPBridgeMacLearn": hwTPBridgeMacLearn,
       "hwTPBridgeRoutingIp": hwTPBridgeRoutingIp,
       "hwTPBridgeBridgingIp": hwTPBridgeBridgingIp,
       "hwTPBridgeBridgingOther": hwTPBridgeBridgingOther,
       "hwTPBridgeAdminStatus": hwTPBridgeAdminStatus,
       "hwTPBridgeRowStatus": hwTPBridgeRowStatus,
       "hwTPBridgeMemberMIBTable": hwTPBridgeMemberMIBTable,
       "hwTPBridgeMemberMIBEntry": hwTPBridgeMemberMIBEntry,
       "hwTPBridgeMemberIfIndex": hwTPBridgeMemberIfIndex,
       "hwTPBridgeMemberVlanTransparent": hwTPBridgeMemberVlanTransparent,
       "hwTPBridgeMemberRowStatus": hwTPBridgeMemberRowStatus,
       "hwTPBridgeApply": hwTPBridgeApply,
       "hwTPBridgeStatTable": hwTPBridgeStatTable,
       "hwTPBridgeStatEntry": hwTPBridgeStatEntry,
       "hwTPBridgeStatBridgeId": hwTPBridgeStatBridgeId,
       "hwTPBridgeStatInTotalPkts": hwTPBridgeStatInTotalPkts,
       "hwTPBridgeStatInBPDUPkts": hwTPBridgeStatInBPDUPkts,
       "hwTPBridgeStatInUcastkts": hwTPBridgeStatInUcastkts,
       "hwTPBridgeStatInMcastkts": hwTPBridgeStatInMcastkts,
       "hwTPBridgeStatInBcastkts": hwTPBridgeStatInBcastkts,
       "hwTPBridgeStatOutTotalPkts": hwTPBridgeStatOutTotalPkts,
       "hwTPBridgeStatOutBPDUPkts": hwTPBridgeStatOutBPDUPkts,
       "hwTPBridgeStatOutUcastkts": hwTPBridgeStatOutUcastkts,
       "hwTPBridgeStatOutMcastkts": hwTPBridgeStatOutMcastkts,
       "hwTPBridgeStatOutBcastkts": hwTPBridgeStatOutBcastkts,
       "hwTPBridgeStatResetFlag": hwTPBridgeStatResetFlag,
       "hwTPBridgeMemberStatTable": hwTPBridgeMemberStatTable,
       "hwTPBridgeMemberStatEntry": hwTPBridgeMemberStatEntry,
       "hwTPBridgeMemberStatIfIndex": hwTPBridgeMemberStatIfIndex,
       "hwTPBridgeMemberStatInTotalPkts": hwTPBridgeMemberStatInTotalPkts,
       "hwTPBridgeMemberStatInBPDUPkts": hwTPBridgeMemberStatInBPDUPkts,
       "hwTPBridgeMemberStatInUcastkts": hwTPBridgeMemberStatInUcastkts,
       "hwTPBridgeMemberStatInMcastkts": hwTPBridgeMemberStatInMcastkts,
       "hwTPBridgeMemberStatInBcastkts": hwTPBridgeMemberStatInBcastkts,
       "hwTPBridgeMemberStatOutTotalPkts": hwTPBridgeMemberStatOutTotalPkts,
       "hwTPBridgeMemberStatOutBPDUPkts": hwTPBridgeMemberStatOutBPDUPkts,
       "hwTPBridgeMemberStatOutUcastkts": hwTPBridgeMemberStatOutUcastkts,
       "hwTPBridgeMemberStatOutMcastkts": hwTPBridgeMemberStatOutMcastkts,
       "hwTPBridgeMemberStatOutBcastkts": hwTPBridgeMemberStatOutBcastkts,
       "hwTPBridgeConformance": hwTPBridgeConformance,
       "hwTPBridgeCompliances": hwTPBridgeCompliances,
       "hwTPBridgeCompliance": hwTPBridgeCompliance,
       "hwTPBridgeGroups": hwTPBridgeGroups,
       "hwTPBridgeGroup": hwTPBridgeGroup,
       "hwTPBridgeMemberGroup": hwTPBridgeMemberGroup,
       "hhwTPBridgeStatGroup": hhwTPBridgeStatGroup,
       "hwTPBridgeMemberStatGroup": hwTPBridgeMemberStatGroup}
)
