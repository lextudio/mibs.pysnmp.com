# SNMP MIB module (A3COM-HUAWEI-USERLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-USERLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:16 2024
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

(huawei,
 huaweiDatacomm,
 huaweiMgmt) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huawei",
    "huaweiDatacomm",
    "huaweiMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwUserLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwUserlogObjects_ObjectIdentity = ObjectIdentity
hwUserlogObjects = _HwUserlogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1)
)
_HwUserlogNatObjects_ObjectIdentity = ObjectIdentity
hwUserlogNatObjects = _HwUserlogNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1)
)
_HwUserlogNatVersion_Type = Integer32
_HwUserlogNatVersion_Object = MibScalar
hwUserlogNatVersion = _HwUserlogNatVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 1),
    _HwUserlogNatVersion_Type()
)
hwUserlogNatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatVersion.setStatus("current")
_HwUserlogNatSyslog_Type = Integer32
_HwUserlogNatSyslog_Object = MibScalar
hwUserlogNatSyslog = _HwUserlogNatSyslog_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 2),
    _HwUserlogNatSyslog_Type()
)
hwUserlogNatSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatSyslog.setStatus("current")
_HwUserlogNatSourceIP_Type = IpAddress
_HwUserlogNatSourceIP_Object = MibScalar
hwUserlogNatSourceIP = _HwUserlogNatSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 3),
    _HwUserlogNatSourceIP_Type()
)
hwUserlogNatSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatSourceIP.setStatus("current")
_HwUserlogNatFlowBegin_Type = Integer32
_HwUserlogNatFlowBegin_Object = MibScalar
hwUserlogNatFlowBegin = _HwUserlogNatFlowBegin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 4),
    _HwUserlogNatFlowBegin_Type()
)
hwUserlogNatFlowBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatFlowBegin.setStatus("current")
_HwUserlogNatActiveTime_Type = Integer32
_HwUserlogNatActiveTime_Object = MibScalar
hwUserlogNatActiveTime = _HwUserlogNatActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 5),
    _HwUserlogNatActiveTime_Type()
)
hwUserlogNatActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatActiveTime.setStatus("current")
_HwUserlogNatSlotCfgInfoTable_Object = MibTable
hwUserlogNatSlotCfgInfoTable = _HwUserlogNatSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwUserlogNatSlotCfgInfoTable.setStatus("current")
_HwUserlogNatSlotCfgInfoEntry_Object = MibTableRow
hwUserlogNatSlotCfgInfoEntry = _HwUserlogNatSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1)
)
hwUserlogNatSlotCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hwUserlogNatSlotCfgInfoEntry.setStatus("current")


class _HwUserlogNatCfgSlotNumber_Type(Integer32):
    """Custom type hwUserlogNatCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwUserlogNatCfgSlotNumber_Type.__name__ = "Integer32"
_HwUserlogNatCfgSlotNumber_Object = MibTableColumn
hwUserlogNatCfgSlotNumber = _HwUserlogNatCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 1),
    _HwUserlogNatCfgSlotNumber_Type()
)
hwUserlogNatCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatCfgSlotNumber.setStatus("current")
_HwUserlogNatEnable_Type = Integer32
_HwUserlogNatEnable_Object = MibTableColumn
hwUserlogNatEnable = _HwUserlogNatEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 2),
    _HwUserlogNatEnable_Type()
)
hwUserlogNatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatEnable.setStatus("current")
_HwUserlogNatAclNumber_Type = Integer32
_HwUserlogNatAclNumber_Object = MibTableColumn
hwUserlogNatAclNumber = _HwUserlogNatAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 3),
    _HwUserlogNatAclNumber_Type()
)
hwUserlogNatAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatAclNumber.setStatus("current")
_HwUserlogNatHostAddress_Type = IpAddress
_HwUserlogNatHostAddress_Object = MibTableColumn
hwUserlogNatHostAddress = _HwUserlogNatHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 4),
    _HwUserlogNatHostAddress_Type()
)
hwUserlogNatHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatHostAddress.setStatus("current")


class _HwUserlogNatUdpPort_Type(Integer32):
    """Custom type hwUserlogNatUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwUserlogNatUdpPort_Type.__name__ = "Integer32"
_HwUserlogNatUdpPort_Object = MibTableColumn
hwUserlogNatUdpPort = _HwUserlogNatUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 5),
    _HwUserlogNatUdpPort_Type()
)
hwUserlogNatUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatUdpPort.setStatus("current")
_HwUserlogNatSlotRunInfoTable_Object = MibTable
hwUserlogNatSlotRunInfoTable = _HwUserlogNatSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwUserlogNatSlotRunInfoTable.setStatus("current")
_HwUserlogNatSlotRunInfoEntry_Object = MibTableRow
hwUserlogNatSlotRunInfoEntry = _HwUserlogNatSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1)
)
hwUserlogNatSlotRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hwUserlogNatSlotRunInfoEntry.setStatus("current")


class _HwUserlogNatRunSlotNumber_Type(Integer32):
    """Custom type hwUserlogNatRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwUserlogNatRunSlotNumber_Type.__name__ = "Integer32"
_HwUserlogNatRunSlotNumber_Object = MibTableColumn
hwUserlogNatRunSlotNumber = _HwUserlogNatRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 1),
    _HwUserlogNatRunSlotNumber_Type()
)
hwUserlogNatRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatRunSlotNumber.setStatus("current")
_HwUserlogNatTotalEntries_Type = Counter32
_HwUserlogNatTotalEntries_Object = MibTableColumn
hwUserlogNatTotalEntries = _HwUserlogNatTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 2),
    _HwUserlogNatTotalEntries_Type()
)
hwUserlogNatTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatTotalEntries.setStatus("current")
_HwUserlogNatTotalPackets_Type = Counter32
_HwUserlogNatTotalPackets_Object = MibTableColumn
hwUserlogNatTotalPackets = _HwUserlogNatTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 3),
    _HwUserlogNatTotalPackets_Type()
)
hwUserlogNatTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatTotalPackets.setStatus("current")
_HwUserlogNatFailedEntries_Type = Counter32
_HwUserlogNatFailedEntries_Object = MibTableColumn
hwUserlogNatFailedEntries = _HwUserlogNatFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 4),
    _HwUserlogNatFailedEntries_Type()
)
hwUserlogNatFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatFailedEntries.setStatus("current")
_HwUserlogNatFailedPackets_Type = Counter32
_HwUserlogNatFailedPackets_Object = MibTableColumn
hwUserlogNatFailedPackets = _HwUserlogNatFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 5),
    _HwUserlogNatFailedPackets_Type()
)
hwUserlogNatFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogNatFailedPackets.setStatus("current")
_HwUserlogNatClearRunStat_Type = Integer32
_HwUserlogNatClearRunStat_Object = MibTableColumn
hwUserlogNatClearRunStat = _HwUserlogNatClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 6),
    _HwUserlogNatClearRunStat_Type()
)
hwUserlogNatClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogNatClearRunStat.setStatus("current")
_HwUserlogFlowObjects_ObjectIdentity = ObjectIdentity
hwUserlogFlowObjects = _HwUserlogFlowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2)
)
_HwUserlogFlowVersion_Type = Integer32
_HwUserlogFlowVersion_Object = MibScalar
hwUserlogFlowVersion = _HwUserlogFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 1),
    _HwUserlogFlowVersion_Type()
)
hwUserlogFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowVersion.setStatus("current")
_HwUserlogFlowSyslog_Type = Integer32
_HwUserlogFlowSyslog_Object = MibScalar
hwUserlogFlowSyslog = _HwUserlogFlowSyslog_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 2),
    _HwUserlogFlowSyslog_Type()
)
hwUserlogFlowSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowSyslog.setStatus("current")
_HwUserlogFlowSourceIP_Type = IpAddress
_HwUserlogFlowSourceIP_Object = MibScalar
hwUserlogFlowSourceIP = _HwUserlogFlowSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 3),
    _HwUserlogFlowSourceIP_Type()
)
hwUserlogFlowSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowSourceIP.setStatus("current")
_HwUserlogFlowFlowBegin_Type = Integer32
_HwUserlogFlowFlowBegin_Object = MibScalar
hwUserlogFlowFlowBegin = _HwUserlogFlowFlowBegin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 4),
    _HwUserlogFlowFlowBegin_Type()
)
hwUserlogFlowFlowBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowFlowBegin.setStatus("current")
_HwUserlogFlowActiveTime_Type = Integer32
_HwUserlogFlowActiveTime_Object = MibScalar
hwUserlogFlowActiveTime = _HwUserlogFlowActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 5),
    _HwUserlogFlowActiveTime_Type()
)
hwUserlogFlowActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowActiveTime.setStatus("current")
_HwUserlogFlowSlotCfgInfoTable_Object = MibTable
hwUserlogFlowSlotCfgInfoTable = _HwUserlogFlowSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwUserlogFlowSlotCfgInfoTable.setStatus("current")
_HwUserlogFlowSlotCfgInfoEntry_Object = MibTableRow
hwUserlogFlowSlotCfgInfoEntry = _HwUserlogFlowSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1)
)
hwUserlogFlowSlotCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hwUserlogFlowSlotCfgInfoEntry.setStatus("current")


class _HwUserlogFlowCfgSlotNumber_Type(Integer32):
    """Custom type hwUserlogFlowCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwUserlogFlowCfgSlotNumber_Type.__name__ = "Integer32"
_HwUserlogFlowCfgSlotNumber_Object = MibTableColumn
hwUserlogFlowCfgSlotNumber = _HwUserlogFlowCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 1),
    _HwUserlogFlowCfgSlotNumber_Type()
)
hwUserlogFlowCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowCfgSlotNumber.setStatus("current")
_HwUserlogFlowEnable_Type = Integer32
_HwUserlogFlowEnable_Object = MibTableColumn
hwUserlogFlowEnable = _HwUserlogFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 2),
    _HwUserlogFlowEnable_Type()
)
hwUserlogFlowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowEnable.setStatus("current")
_HwUserlogFlowAclNumber_Type = Integer32
_HwUserlogFlowAclNumber_Object = MibTableColumn
hwUserlogFlowAclNumber = _HwUserlogFlowAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 3),
    _HwUserlogFlowAclNumber_Type()
)
hwUserlogFlowAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowAclNumber.setStatus("current")
_HwUserlogFlowHostAddress_Type = IpAddress
_HwUserlogFlowHostAddress_Object = MibTableColumn
hwUserlogFlowHostAddress = _HwUserlogFlowHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 4),
    _HwUserlogFlowHostAddress_Type()
)
hwUserlogFlowHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowHostAddress.setStatus("current")


class _HwUserlogFlowUdpPort_Type(Integer32):
    """Custom type hwUserlogFlowUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwUserlogFlowUdpPort_Type.__name__ = "Integer32"
_HwUserlogFlowUdpPort_Object = MibTableColumn
hwUserlogFlowUdpPort = _HwUserlogFlowUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 5),
    _HwUserlogFlowUdpPort_Type()
)
hwUserlogFlowUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowUdpPort.setStatus("current")
_HwUserlogFlowSlotRunInfoTable_Object = MibTable
hwUserlogFlowSlotRunInfoTable = _HwUserlogFlowSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwUserlogFlowSlotRunInfoTable.setStatus("current")
_HwUserlogFlowSlotRunInfoEntry_Object = MibTableRow
hwUserlogFlowSlotRunInfoEntry = _HwUserlogFlowSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1)
)
hwUserlogFlowSlotRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hwUserlogFlowSlotRunInfoEntry.setStatus("current")


class _HwUserlogFlowRunSlotNumber_Type(Integer32):
    """Custom type hwUserlogFlowRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwUserlogFlowRunSlotNumber_Type.__name__ = "Integer32"
_HwUserlogFlowRunSlotNumber_Object = MibTableColumn
hwUserlogFlowRunSlotNumber = _HwUserlogFlowRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 1),
    _HwUserlogFlowRunSlotNumber_Type()
)
hwUserlogFlowRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowRunSlotNumber.setStatus("current")
_HwUserlogFlowTotalEntries_Type = Counter32
_HwUserlogFlowTotalEntries_Object = MibTableColumn
hwUserlogFlowTotalEntries = _HwUserlogFlowTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 2),
    _HwUserlogFlowTotalEntries_Type()
)
hwUserlogFlowTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowTotalEntries.setStatus("current")
_HwUserlogFlowTotalPackets_Type = Counter32
_HwUserlogFlowTotalPackets_Object = MibTableColumn
hwUserlogFlowTotalPackets = _HwUserlogFlowTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 3),
    _HwUserlogFlowTotalPackets_Type()
)
hwUserlogFlowTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowTotalPackets.setStatus("current")
_HwUserlogFlowFailedEntries_Type = Counter32
_HwUserlogFlowFailedEntries_Object = MibTableColumn
hwUserlogFlowFailedEntries = _HwUserlogFlowFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 4),
    _HwUserlogFlowFailedEntries_Type()
)
hwUserlogFlowFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowFailedEntries.setStatus("current")
_HwUserlogFlowFailedPackets_Type = Counter32
_HwUserlogFlowFailedPackets_Object = MibTableColumn
hwUserlogFlowFailedPackets = _HwUserlogFlowFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 5),
    _HwUserlogFlowFailedPackets_Type()
)
hwUserlogFlowFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogFlowFailedPackets.setStatus("current")
_HwUserlogFlowClearRunStat_Type = Integer32
_HwUserlogFlowClearRunStat_Object = MibTableColumn
hwUserlogFlowClearRunStat = _HwUserlogFlowClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 6),
    _HwUserlogFlowClearRunStat_Type()
)
hwUserlogFlowClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogFlowClearRunStat.setStatus("current")
_HwUserlogAccessObjects_ObjectIdentity = ObjectIdentity
hwUserlogAccessObjects = _HwUserlogAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3)
)
_HwUserlogAccessVersion_Type = Integer32
_HwUserlogAccessVersion_Object = MibScalar
hwUserlogAccessVersion = _HwUserlogAccessVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 1),
    _HwUserlogAccessVersion_Type()
)
hwUserlogAccessVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessVersion.setStatus("current")
_HwUserlogAccessSyslog_Type = Integer32
_HwUserlogAccessSyslog_Object = MibScalar
hwUserlogAccessSyslog = _HwUserlogAccessSyslog_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 2),
    _HwUserlogAccessSyslog_Type()
)
hwUserlogAccessSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogAccessSyslog.setStatus("current")
_HwUserlogAccessSourceIP_Type = IpAddress
_HwUserlogAccessSourceIP_Object = MibScalar
hwUserlogAccessSourceIP = _HwUserlogAccessSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 3),
    _HwUserlogAccessSourceIP_Type()
)
hwUserlogAccessSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogAccessSourceIP.setStatus("current")
_HwUserlogAccessSlotCfgInfoTable_Object = MibTable
hwUserlogAccessSlotCfgInfoTable = _HwUserlogAccessSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwUserlogAccessSlotCfgInfoTable.setStatus("current")
_HwUserlogAccessSlotCfgInfoEntry_Object = MibTableRow
hwUserlogAccessSlotCfgInfoEntry = _HwUserlogAccessSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1)
)
hwUserlogAccessSlotCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hwUserlogAccessSlotCfgInfoEntry.setStatus("current")


class _HwUserlogAccessCfgSlotNumber_Type(Integer32):
    """Custom type hwUserlogAccessCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwUserlogAccessCfgSlotNumber_Type.__name__ = "Integer32"
_HwUserlogAccessCfgSlotNumber_Object = MibTableColumn
hwUserlogAccessCfgSlotNumber = _HwUserlogAccessCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 1),
    _HwUserlogAccessCfgSlotNumber_Type()
)
hwUserlogAccessCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessCfgSlotNumber.setStatus("current")
_HwUserlogAccessEnable_Type = Integer32
_HwUserlogAccessEnable_Object = MibTableColumn
hwUserlogAccessEnable = _HwUserlogAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 2),
    _HwUserlogAccessEnable_Type()
)
hwUserlogAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogAccessEnable.setStatus("current")
_HwUserlogAccessHostAddress_Type = IpAddress
_HwUserlogAccessHostAddress_Object = MibTableColumn
hwUserlogAccessHostAddress = _HwUserlogAccessHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 3),
    _HwUserlogAccessHostAddress_Type()
)
hwUserlogAccessHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogAccessHostAddress.setStatus("current")


class _HwUserlogAccessUdpPort_Type(Integer32):
    """Custom type hwUserlogAccessUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwUserlogAccessUdpPort_Type.__name__ = "Integer32"
_HwUserlogAccessUdpPort_Object = MibTableColumn
hwUserlogAccessUdpPort = _HwUserlogAccessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 4),
    _HwUserlogAccessUdpPort_Type()
)
hwUserlogAccessUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogAccessUdpPort.setStatus("current")
_HwUserlogAccessSlotRunInfoTable_Object = MibTable
hwUserlogAccessSlotRunInfoTable = _HwUserlogAccessSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hwUserlogAccessSlotRunInfoTable.setStatus("current")
_HwUserlogAccessSlotRunInfoEntry_Object = MibTableRow
hwUserlogAccessSlotRunInfoEntry = _HwUserlogAccessSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1)
)
hwUserlogAccessSlotRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hwUserlogAccessSlotRunInfoEntry.setStatus("current")


class _HwUserlogAccessRunSlotNumber_Type(Integer32):
    """Custom type hwUserlogAccessRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwUserlogAccessRunSlotNumber_Type.__name__ = "Integer32"
_HwUserlogAccessRunSlotNumber_Object = MibTableColumn
hwUserlogAccessRunSlotNumber = _HwUserlogAccessRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 1),
    _HwUserlogAccessRunSlotNumber_Type()
)
hwUserlogAccessRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessRunSlotNumber.setStatus("current")
_HwUserlogAccessTotalEntries_Type = Counter32
_HwUserlogAccessTotalEntries_Object = MibTableColumn
hwUserlogAccessTotalEntries = _HwUserlogAccessTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 2),
    _HwUserlogAccessTotalEntries_Type()
)
hwUserlogAccessTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessTotalEntries.setStatus("current")
_HwUserlogAccessTotalPackets_Type = Counter32
_HwUserlogAccessTotalPackets_Object = MibTableColumn
hwUserlogAccessTotalPackets = _HwUserlogAccessTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 3),
    _HwUserlogAccessTotalPackets_Type()
)
hwUserlogAccessTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessTotalPackets.setStatus("current")
_HwUserlogAccessFailedEntries_Type = Counter32
_HwUserlogAccessFailedEntries_Object = MibTableColumn
hwUserlogAccessFailedEntries = _HwUserlogAccessFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 4),
    _HwUserlogAccessFailedEntries_Type()
)
hwUserlogAccessFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessFailedEntries.setStatus("current")
_HwUserlogAccessFailedPackets_Type = Counter32
_HwUserlogAccessFailedPackets_Object = MibTableColumn
hwUserlogAccessFailedPackets = _HwUserlogAccessFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 5),
    _HwUserlogAccessFailedPackets_Type()
)
hwUserlogAccessFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserlogAccessFailedPackets.setStatus("current")
_HwUserlogAccessClearRunStat_Type = Integer32
_HwUserlogAccessClearRunStat_Object = MibTableColumn
hwUserlogAccessClearRunStat = _HwUserlogAccessClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 6),
    _HwUserlogAccessClearRunStat_Type()
)
hwUserlogAccessClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserlogAccessClearRunStat.setStatus("current")
_HwUserlogNotifications_ObjectIdentity = ObjectIdentity
hwUserlogNotifications = _HwUserlogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 2)
)
_HwUserlogConformance_ObjectIdentity = ObjectIdentity
hwUserlogConformance = _HwUserlogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3)
)
_HwUserlogCompliances_ObjectIdentity = ObjectIdentity
hwUserlogCompliances = _HwUserlogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 1)
)
_HwUserlogGroups_ObjectIdentity = ObjectIdentity
hwUserlogGroups = _HwUserlogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2)
)

# Managed Objects groups

hwUserlogMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2, 1)
)
hwUserlogMandatoryGroup.setObjects(
      *(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
)
if mibBuilder.loadTexts:
    hwUserlogMandatoryGroup.setStatus("current")

hwUserlogConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2, 2)
)
hwUserlogConfigGroup.setObjects(
      *(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatVersion"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatSyslog"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatSourceIP"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatFlowBegin"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatActiveTime"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatAclNumber"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowVersion"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowSyslog"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowSourceIP"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowFlowBegin"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowActiveTime"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowAclNumber"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessVersion"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessSyslog"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessSourceIP"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
)
if mibBuilder.loadTexts:
    hwUserlogConfigGroup.setStatus("current")

hwUserlogInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2, 3)
)
hwUserlogInfoGroup.setObjects(
      *(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatTotalEntries"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatTotalPackets"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatFailedEntries"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatFailedPackets"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalEntries"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalPackets"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedEntries"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedPackets"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalEntries"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalPackets"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedEntries"),
        ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedPackets"))
)
if mibBuilder.loadTexts:
    hwUserlogInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwUserlogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwUserlogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-USERLOG-MIB",
    **{"hwUserLogMIB": hwUserLogMIB,
       "hwUserlogObjects": hwUserlogObjects,
       "hwUserlogNatObjects": hwUserlogNatObjects,
       "hwUserlogNatVersion": hwUserlogNatVersion,
       "hwUserlogNatSyslog": hwUserlogNatSyslog,
       "hwUserlogNatSourceIP": hwUserlogNatSourceIP,
       "hwUserlogNatFlowBegin": hwUserlogNatFlowBegin,
       "hwUserlogNatActiveTime": hwUserlogNatActiveTime,
       "hwUserlogNatSlotCfgInfoTable": hwUserlogNatSlotCfgInfoTable,
       "hwUserlogNatSlotCfgInfoEntry": hwUserlogNatSlotCfgInfoEntry,
       "hwUserlogNatCfgSlotNumber": hwUserlogNatCfgSlotNumber,
       "hwUserlogNatEnable": hwUserlogNatEnable,
       "hwUserlogNatAclNumber": hwUserlogNatAclNumber,
       "hwUserlogNatHostAddress": hwUserlogNatHostAddress,
       "hwUserlogNatUdpPort": hwUserlogNatUdpPort,
       "hwUserlogNatSlotRunInfoTable": hwUserlogNatSlotRunInfoTable,
       "hwUserlogNatSlotRunInfoEntry": hwUserlogNatSlotRunInfoEntry,
       "hwUserlogNatRunSlotNumber": hwUserlogNatRunSlotNumber,
       "hwUserlogNatTotalEntries": hwUserlogNatTotalEntries,
       "hwUserlogNatTotalPackets": hwUserlogNatTotalPackets,
       "hwUserlogNatFailedEntries": hwUserlogNatFailedEntries,
       "hwUserlogNatFailedPackets": hwUserlogNatFailedPackets,
       "hwUserlogNatClearRunStat": hwUserlogNatClearRunStat,
       "hwUserlogFlowObjects": hwUserlogFlowObjects,
       "hwUserlogFlowVersion": hwUserlogFlowVersion,
       "hwUserlogFlowSyslog": hwUserlogFlowSyslog,
       "hwUserlogFlowSourceIP": hwUserlogFlowSourceIP,
       "hwUserlogFlowFlowBegin": hwUserlogFlowFlowBegin,
       "hwUserlogFlowActiveTime": hwUserlogFlowActiveTime,
       "hwUserlogFlowSlotCfgInfoTable": hwUserlogFlowSlotCfgInfoTable,
       "hwUserlogFlowSlotCfgInfoEntry": hwUserlogFlowSlotCfgInfoEntry,
       "hwUserlogFlowCfgSlotNumber": hwUserlogFlowCfgSlotNumber,
       "hwUserlogFlowEnable": hwUserlogFlowEnable,
       "hwUserlogFlowAclNumber": hwUserlogFlowAclNumber,
       "hwUserlogFlowHostAddress": hwUserlogFlowHostAddress,
       "hwUserlogFlowUdpPort": hwUserlogFlowUdpPort,
       "hwUserlogFlowSlotRunInfoTable": hwUserlogFlowSlotRunInfoTable,
       "hwUserlogFlowSlotRunInfoEntry": hwUserlogFlowSlotRunInfoEntry,
       "hwUserlogFlowRunSlotNumber": hwUserlogFlowRunSlotNumber,
       "hwUserlogFlowTotalEntries": hwUserlogFlowTotalEntries,
       "hwUserlogFlowTotalPackets": hwUserlogFlowTotalPackets,
       "hwUserlogFlowFailedEntries": hwUserlogFlowFailedEntries,
       "hwUserlogFlowFailedPackets": hwUserlogFlowFailedPackets,
       "hwUserlogFlowClearRunStat": hwUserlogFlowClearRunStat,
       "hwUserlogAccessObjects": hwUserlogAccessObjects,
       "hwUserlogAccessVersion": hwUserlogAccessVersion,
       "hwUserlogAccessSyslog": hwUserlogAccessSyslog,
       "hwUserlogAccessSourceIP": hwUserlogAccessSourceIP,
       "hwUserlogAccessSlotCfgInfoTable": hwUserlogAccessSlotCfgInfoTable,
       "hwUserlogAccessSlotCfgInfoEntry": hwUserlogAccessSlotCfgInfoEntry,
       "hwUserlogAccessCfgSlotNumber": hwUserlogAccessCfgSlotNumber,
       "hwUserlogAccessEnable": hwUserlogAccessEnable,
       "hwUserlogAccessHostAddress": hwUserlogAccessHostAddress,
       "hwUserlogAccessUdpPort": hwUserlogAccessUdpPort,
       "hwUserlogAccessSlotRunInfoTable": hwUserlogAccessSlotRunInfoTable,
       "hwUserlogAccessSlotRunInfoEntry": hwUserlogAccessSlotRunInfoEntry,
       "hwUserlogAccessRunSlotNumber": hwUserlogAccessRunSlotNumber,
       "hwUserlogAccessTotalEntries": hwUserlogAccessTotalEntries,
       "hwUserlogAccessTotalPackets": hwUserlogAccessTotalPackets,
       "hwUserlogAccessFailedEntries": hwUserlogAccessFailedEntries,
       "hwUserlogAccessFailedPackets": hwUserlogAccessFailedPackets,
       "hwUserlogAccessClearRunStat": hwUserlogAccessClearRunStat,
       "hwUserlogNotifications": hwUserlogNotifications,
       "hwUserlogConformance": hwUserlogConformance,
       "hwUserlogCompliances": hwUserlogCompliances,
       "hwUserlogCompliance": hwUserlogCompliance,
       "hwUserlogGroups": hwUserlogGroups,
       "hwUserlogMandatoryGroup": hwUserlogMandatoryGroup,
       "hwUserlogConfigGroup": hwUserlogConfigGroup,
       "hwUserlogInfoGroup": hwUserlogInfoGroup}
)
