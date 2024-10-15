# SNMP MIB module (HH3C-USERLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-USERLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:13 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cUserLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cUserlogObjects_ObjectIdentity = ObjectIdentity
hh3cUserlogObjects = _Hh3cUserlogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1)
)
_Hh3cUserlogNatObjects_ObjectIdentity = ObjectIdentity
hh3cUserlogNatObjects = _Hh3cUserlogNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1)
)
_Hh3cUserlogNatVersion_Type = Integer32
_Hh3cUserlogNatVersion_Object = MibScalar
hh3cUserlogNatVersion = _Hh3cUserlogNatVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 1),
    _Hh3cUserlogNatVersion_Type()
)
hh3cUserlogNatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatVersion.setStatus("current")
_Hh3cUserlogNatSyslog_Type = Integer32
_Hh3cUserlogNatSyslog_Object = MibScalar
hh3cUserlogNatSyslog = _Hh3cUserlogNatSyslog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 2),
    _Hh3cUserlogNatSyslog_Type()
)
hh3cUserlogNatSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatSyslog.setStatus("current")
_Hh3cUserlogNatSourceIP_Type = IpAddress
_Hh3cUserlogNatSourceIP_Object = MibScalar
hh3cUserlogNatSourceIP = _Hh3cUserlogNatSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 3),
    _Hh3cUserlogNatSourceIP_Type()
)
hh3cUserlogNatSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatSourceIP.setStatus("current")
_Hh3cUserlogNatFlowBegin_Type = Integer32
_Hh3cUserlogNatFlowBegin_Object = MibScalar
hh3cUserlogNatFlowBegin = _Hh3cUserlogNatFlowBegin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 4),
    _Hh3cUserlogNatFlowBegin_Type()
)
hh3cUserlogNatFlowBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatFlowBegin.setStatus("current")
_Hh3cUserlogNatActiveTime_Type = Integer32
_Hh3cUserlogNatActiveTime_Object = MibScalar
hh3cUserlogNatActiveTime = _Hh3cUserlogNatActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 5),
    _Hh3cUserlogNatActiveTime_Type()
)
hh3cUserlogNatActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatActiveTime.setStatus("current")
_Hh3cUserlogNatSlotCfgInfoTable_Object = MibTable
hh3cUserlogNatSlotCfgInfoTable = _Hh3cUserlogNatSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cUserlogNatSlotCfgInfoTable.setStatus("current")
_Hh3cUserlogNatSlotCfgInfoEntry_Object = MibTableRow
hh3cUserlogNatSlotCfgInfoEntry = _Hh3cUserlogNatSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1)
)
hh3cUserlogNatSlotCfgInfoEntry.setIndexNames(
    (0, "HH3C-USERLOG-MIB", "hh3cUserlogNatCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hh3cUserlogNatSlotCfgInfoEntry.setStatus("current")


class _Hh3cUserlogNatCfgSlotNumber_Type(Integer32):
    """Custom type hh3cUserlogNatCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cUserlogNatCfgSlotNumber_Type.__name__ = "Integer32"
_Hh3cUserlogNatCfgSlotNumber_Object = MibTableColumn
hh3cUserlogNatCfgSlotNumber = _Hh3cUserlogNatCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 1),
    _Hh3cUserlogNatCfgSlotNumber_Type()
)
hh3cUserlogNatCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatCfgSlotNumber.setStatus("current")
_Hh3cUserlogNatEnable_Type = Integer32
_Hh3cUserlogNatEnable_Object = MibTableColumn
hh3cUserlogNatEnable = _Hh3cUserlogNatEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 2),
    _Hh3cUserlogNatEnable_Type()
)
hh3cUserlogNatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatEnable.setStatus("current")
_Hh3cUserlogNatAclNumber_Type = Integer32
_Hh3cUserlogNatAclNumber_Object = MibTableColumn
hh3cUserlogNatAclNumber = _Hh3cUserlogNatAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 3),
    _Hh3cUserlogNatAclNumber_Type()
)
hh3cUserlogNatAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatAclNumber.setStatus("current")
_Hh3cUserlogNatHostAddress_Type = IpAddress
_Hh3cUserlogNatHostAddress_Object = MibTableColumn
hh3cUserlogNatHostAddress = _Hh3cUserlogNatHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 4),
    _Hh3cUserlogNatHostAddress_Type()
)
hh3cUserlogNatHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatHostAddress.setStatus("current")


class _Hh3cUserlogNatUdpPort_Type(Integer32):
    """Custom type hh3cUserlogNatUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cUserlogNatUdpPort_Type.__name__ = "Integer32"
_Hh3cUserlogNatUdpPort_Object = MibTableColumn
hh3cUserlogNatUdpPort = _Hh3cUserlogNatUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 5),
    _Hh3cUserlogNatUdpPort_Type()
)
hh3cUserlogNatUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatUdpPort.setStatus("current")
_Hh3cUserlogNatSlotRunInfoTable_Object = MibTable
hh3cUserlogNatSlotRunInfoTable = _Hh3cUserlogNatSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cUserlogNatSlotRunInfoTable.setStatus("current")
_Hh3cUserlogNatSlotRunInfoEntry_Object = MibTableRow
hh3cUserlogNatSlotRunInfoEntry = _Hh3cUserlogNatSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1)
)
hh3cUserlogNatSlotRunInfoEntry.setIndexNames(
    (0, "HH3C-USERLOG-MIB", "hh3cUserlogNatRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hh3cUserlogNatSlotRunInfoEntry.setStatus("current")


class _Hh3cUserlogNatRunSlotNumber_Type(Integer32):
    """Custom type hh3cUserlogNatRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cUserlogNatRunSlotNumber_Type.__name__ = "Integer32"
_Hh3cUserlogNatRunSlotNumber_Object = MibTableColumn
hh3cUserlogNatRunSlotNumber = _Hh3cUserlogNatRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 1),
    _Hh3cUserlogNatRunSlotNumber_Type()
)
hh3cUserlogNatRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatRunSlotNumber.setStatus("current")
_Hh3cUserlogNatTotalEntries_Type = Counter32
_Hh3cUserlogNatTotalEntries_Object = MibTableColumn
hh3cUserlogNatTotalEntries = _Hh3cUserlogNatTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 2),
    _Hh3cUserlogNatTotalEntries_Type()
)
hh3cUserlogNatTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatTotalEntries.setStatus("current")
_Hh3cUserlogNatTotalPackets_Type = Counter32
_Hh3cUserlogNatTotalPackets_Object = MibTableColumn
hh3cUserlogNatTotalPackets = _Hh3cUserlogNatTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 3),
    _Hh3cUserlogNatTotalPackets_Type()
)
hh3cUserlogNatTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatTotalPackets.setStatus("current")
_Hh3cUserlogNatFailedEntries_Type = Counter32
_Hh3cUserlogNatFailedEntries_Object = MibTableColumn
hh3cUserlogNatFailedEntries = _Hh3cUserlogNatFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 4),
    _Hh3cUserlogNatFailedEntries_Type()
)
hh3cUserlogNatFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatFailedEntries.setStatus("current")
_Hh3cUserlogNatFailedPackets_Type = Counter32
_Hh3cUserlogNatFailedPackets_Object = MibTableColumn
hh3cUserlogNatFailedPackets = _Hh3cUserlogNatFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 5),
    _Hh3cUserlogNatFailedPackets_Type()
)
hh3cUserlogNatFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogNatFailedPackets.setStatus("current")
_Hh3cUserlogNatClearRunStat_Type = Integer32
_Hh3cUserlogNatClearRunStat_Object = MibTableColumn
hh3cUserlogNatClearRunStat = _Hh3cUserlogNatClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 6),
    _Hh3cUserlogNatClearRunStat_Type()
)
hh3cUserlogNatClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogNatClearRunStat.setStatus("current")
_Hh3cUserlogFlowObjects_ObjectIdentity = ObjectIdentity
hh3cUserlogFlowObjects = _Hh3cUserlogFlowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2)
)
_Hh3cUserlogFlowVersion_Type = Integer32
_Hh3cUserlogFlowVersion_Object = MibScalar
hh3cUserlogFlowVersion = _Hh3cUserlogFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 1),
    _Hh3cUserlogFlowVersion_Type()
)
hh3cUserlogFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowVersion.setStatus("current")
_Hh3cUserlogFlowSyslog_Type = Integer32
_Hh3cUserlogFlowSyslog_Object = MibScalar
hh3cUserlogFlowSyslog = _Hh3cUserlogFlowSyslog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 2),
    _Hh3cUserlogFlowSyslog_Type()
)
hh3cUserlogFlowSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowSyslog.setStatus("current")
_Hh3cUserlogFlowSourceIP_Type = IpAddress
_Hh3cUserlogFlowSourceIP_Object = MibScalar
hh3cUserlogFlowSourceIP = _Hh3cUserlogFlowSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 3),
    _Hh3cUserlogFlowSourceIP_Type()
)
hh3cUserlogFlowSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowSourceIP.setStatus("current")
_Hh3cUserlogFlowFlowBegin_Type = Integer32
_Hh3cUserlogFlowFlowBegin_Object = MibScalar
hh3cUserlogFlowFlowBegin = _Hh3cUserlogFlowFlowBegin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 4),
    _Hh3cUserlogFlowFlowBegin_Type()
)
hh3cUserlogFlowFlowBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowFlowBegin.setStatus("current")
_Hh3cUserlogFlowActiveTime_Type = Integer32
_Hh3cUserlogFlowActiveTime_Object = MibScalar
hh3cUserlogFlowActiveTime = _Hh3cUserlogFlowActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 5),
    _Hh3cUserlogFlowActiveTime_Type()
)
hh3cUserlogFlowActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowActiveTime.setStatus("current")
_Hh3cUserlogFlowSlotCfgInfoTable_Object = MibTable
hh3cUserlogFlowSlotCfgInfoTable = _Hh3cUserlogFlowSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cUserlogFlowSlotCfgInfoTable.setStatus("current")
_Hh3cUserlogFlowSlotCfgInfoEntry_Object = MibTableRow
hh3cUserlogFlowSlotCfgInfoEntry = _Hh3cUserlogFlowSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1)
)
hh3cUserlogFlowSlotCfgInfoEntry.setIndexNames(
    (0, "HH3C-USERLOG-MIB", "hh3cUserlogFlowCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hh3cUserlogFlowSlotCfgInfoEntry.setStatus("current")


class _Hh3cUserlogFlowCfgSlotNumber_Type(Integer32):
    """Custom type hh3cUserlogFlowCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cUserlogFlowCfgSlotNumber_Type.__name__ = "Integer32"
_Hh3cUserlogFlowCfgSlotNumber_Object = MibTableColumn
hh3cUserlogFlowCfgSlotNumber = _Hh3cUserlogFlowCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 1),
    _Hh3cUserlogFlowCfgSlotNumber_Type()
)
hh3cUserlogFlowCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowCfgSlotNumber.setStatus("current")
_Hh3cUserlogFlowEnable_Type = Integer32
_Hh3cUserlogFlowEnable_Object = MibTableColumn
hh3cUserlogFlowEnable = _Hh3cUserlogFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 2),
    _Hh3cUserlogFlowEnable_Type()
)
hh3cUserlogFlowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowEnable.setStatus("current")
_Hh3cUserlogFlowAclNumber_Type = Integer32
_Hh3cUserlogFlowAclNumber_Object = MibTableColumn
hh3cUserlogFlowAclNumber = _Hh3cUserlogFlowAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 3),
    _Hh3cUserlogFlowAclNumber_Type()
)
hh3cUserlogFlowAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowAclNumber.setStatus("current")
_Hh3cUserlogFlowHostAddress_Type = IpAddress
_Hh3cUserlogFlowHostAddress_Object = MibTableColumn
hh3cUserlogFlowHostAddress = _Hh3cUserlogFlowHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 4),
    _Hh3cUserlogFlowHostAddress_Type()
)
hh3cUserlogFlowHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowHostAddress.setStatus("current")


class _Hh3cUserlogFlowUdpPort_Type(Integer32):
    """Custom type hh3cUserlogFlowUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cUserlogFlowUdpPort_Type.__name__ = "Integer32"
_Hh3cUserlogFlowUdpPort_Object = MibTableColumn
hh3cUserlogFlowUdpPort = _Hh3cUserlogFlowUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 5),
    _Hh3cUserlogFlowUdpPort_Type()
)
hh3cUserlogFlowUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowUdpPort.setStatus("current")
_Hh3cUserlogFlowSlotRunInfoTable_Object = MibTable
hh3cUserlogFlowSlotRunInfoTable = _Hh3cUserlogFlowSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cUserlogFlowSlotRunInfoTable.setStatus("current")
_Hh3cUserlogFlowSlotRunInfoEntry_Object = MibTableRow
hh3cUserlogFlowSlotRunInfoEntry = _Hh3cUserlogFlowSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1)
)
hh3cUserlogFlowSlotRunInfoEntry.setIndexNames(
    (0, "HH3C-USERLOG-MIB", "hh3cUserlogFlowRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hh3cUserlogFlowSlotRunInfoEntry.setStatus("current")


class _Hh3cUserlogFlowRunSlotNumber_Type(Integer32):
    """Custom type hh3cUserlogFlowRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cUserlogFlowRunSlotNumber_Type.__name__ = "Integer32"
_Hh3cUserlogFlowRunSlotNumber_Object = MibTableColumn
hh3cUserlogFlowRunSlotNumber = _Hh3cUserlogFlowRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 1),
    _Hh3cUserlogFlowRunSlotNumber_Type()
)
hh3cUserlogFlowRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowRunSlotNumber.setStatus("current")
_Hh3cUserlogFlowTotalEntries_Type = Counter32
_Hh3cUserlogFlowTotalEntries_Object = MibTableColumn
hh3cUserlogFlowTotalEntries = _Hh3cUserlogFlowTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 2),
    _Hh3cUserlogFlowTotalEntries_Type()
)
hh3cUserlogFlowTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowTotalEntries.setStatus("current")
_Hh3cUserlogFlowTotalPackets_Type = Counter32
_Hh3cUserlogFlowTotalPackets_Object = MibTableColumn
hh3cUserlogFlowTotalPackets = _Hh3cUserlogFlowTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 3),
    _Hh3cUserlogFlowTotalPackets_Type()
)
hh3cUserlogFlowTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowTotalPackets.setStatus("current")
_Hh3cUserlogFlowFailedEntries_Type = Counter32
_Hh3cUserlogFlowFailedEntries_Object = MibTableColumn
hh3cUserlogFlowFailedEntries = _Hh3cUserlogFlowFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 4),
    _Hh3cUserlogFlowFailedEntries_Type()
)
hh3cUserlogFlowFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowFailedEntries.setStatus("current")
_Hh3cUserlogFlowFailedPackets_Type = Counter32
_Hh3cUserlogFlowFailedPackets_Object = MibTableColumn
hh3cUserlogFlowFailedPackets = _Hh3cUserlogFlowFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 5),
    _Hh3cUserlogFlowFailedPackets_Type()
)
hh3cUserlogFlowFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogFlowFailedPackets.setStatus("current")
_Hh3cUserlogFlowClearRunStat_Type = Integer32
_Hh3cUserlogFlowClearRunStat_Object = MibTableColumn
hh3cUserlogFlowClearRunStat = _Hh3cUserlogFlowClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 6),
    _Hh3cUserlogFlowClearRunStat_Type()
)
hh3cUserlogFlowClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogFlowClearRunStat.setStatus("current")
_Hh3cUserlogAccessObjects_ObjectIdentity = ObjectIdentity
hh3cUserlogAccessObjects = _Hh3cUserlogAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3)
)
_Hh3cUserlogAccessVersion_Type = Integer32
_Hh3cUserlogAccessVersion_Object = MibScalar
hh3cUserlogAccessVersion = _Hh3cUserlogAccessVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 1),
    _Hh3cUserlogAccessVersion_Type()
)
hh3cUserlogAccessVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessVersion.setStatus("current")
_Hh3cUserlogAccessSyslog_Type = Integer32
_Hh3cUserlogAccessSyslog_Object = MibScalar
hh3cUserlogAccessSyslog = _Hh3cUserlogAccessSyslog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 2),
    _Hh3cUserlogAccessSyslog_Type()
)
hh3cUserlogAccessSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogAccessSyslog.setStatus("current")
_Hh3cUserlogAccessSourceIP_Type = IpAddress
_Hh3cUserlogAccessSourceIP_Object = MibScalar
hh3cUserlogAccessSourceIP = _Hh3cUserlogAccessSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 3),
    _Hh3cUserlogAccessSourceIP_Type()
)
hh3cUserlogAccessSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogAccessSourceIP.setStatus("current")
_Hh3cUserlogAccessSlotCfgInfoTable_Object = MibTable
hh3cUserlogAccessSlotCfgInfoTable = _Hh3cUserlogAccessSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cUserlogAccessSlotCfgInfoTable.setStatus("current")
_Hh3cUserlogAccessSlotCfgInfoEntry_Object = MibTableRow
hh3cUserlogAccessSlotCfgInfoEntry = _Hh3cUserlogAccessSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1)
)
hh3cUserlogAccessSlotCfgInfoEntry.setIndexNames(
    (0, "HH3C-USERLOG-MIB", "hh3cUserlogAccessCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hh3cUserlogAccessSlotCfgInfoEntry.setStatus("current")


class _Hh3cUserlogAccessCfgSlotNumber_Type(Integer32):
    """Custom type hh3cUserlogAccessCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cUserlogAccessCfgSlotNumber_Type.__name__ = "Integer32"
_Hh3cUserlogAccessCfgSlotNumber_Object = MibTableColumn
hh3cUserlogAccessCfgSlotNumber = _Hh3cUserlogAccessCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 1),
    _Hh3cUserlogAccessCfgSlotNumber_Type()
)
hh3cUserlogAccessCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessCfgSlotNumber.setStatus("current")
_Hh3cUserlogAccessEnable_Type = Integer32
_Hh3cUserlogAccessEnable_Object = MibTableColumn
hh3cUserlogAccessEnable = _Hh3cUserlogAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 2),
    _Hh3cUserlogAccessEnable_Type()
)
hh3cUserlogAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogAccessEnable.setStatus("current")
_Hh3cUserlogAccessHostAddress_Type = IpAddress
_Hh3cUserlogAccessHostAddress_Object = MibTableColumn
hh3cUserlogAccessHostAddress = _Hh3cUserlogAccessHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 3),
    _Hh3cUserlogAccessHostAddress_Type()
)
hh3cUserlogAccessHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogAccessHostAddress.setStatus("current")


class _Hh3cUserlogAccessUdpPort_Type(Integer32):
    """Custom type hh3cUserlogAccessUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cUserlogAccessUdpPort_Type.__name__ = "Integer32"
_Hh3cUserlogAccessUdpPort_Object = MibTableColumn
hh3cUserlogAccessUdpPort = _Hh3cUserlogAccessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 4),
    _Hh3cUserlogAccessUdpPort_Type()
)
hh3cUserlogAccessUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogAccessUdpPort.setStatus("current")
_Hh3cUserlogAccessSlotRunInfoTable_Object = MibTable
hh3cUserlogAccessSlotRunInfoTable = _Hh3cUserlogAccessSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cUserlogAccessSlotRunInfoTable.setStatus("current")
_Hh3cUserlogAccessSlotRunInfoEntry_Object = MibTableRow
hh3cUserlogAccessSlotRunInfoEntry = _Hh3cUserlogAccessSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1)
)
hh3cUserlogAccessSlotRunInfoEntry.setIndexNames(
    (0, "HH3C-USERLOG-MIB", "hh3cUserlogAccessRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hh3cUserlogAccessSlotRunInfoEntry.setStatus("current")


class _Hh3cUserlogAccessRunSlotNumber_Type(Integer32):
    """Custom type hh3cUserlogAccessRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cUserlogAccessRunSlotNumber_Type.__name__ = "Integer32"
_Hh3cUserlogAccessRunSlotNumber_Object = MibTableColumn
hh3cUserlogAccessRunSlotNumber = _Hh3cUserlogAccessRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 1),
    _Hh3cUserlogAccessRunSlotNumber_Type()
)
hh3cUserlogAccessRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessRunSlotNumber.setStatus("current")
_Hh3cUserlogAccessTotalEntries_Type = Counter32
_Hh3cUserlogAccessTotalEntries_Object = MibTableColumn
hh3cUserlogAccessTotalEntries = _Hh3cUserlogAccessTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 2),
    _Hh3cUserlogAccessTotalEntries_Type()
)
hh3cUserlogAccessTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessTotalEntries.setStatus("current")
_Hh3cUserlogAccessTotalPackets_Type = Counter32
_Hh3cUserlogAccessTotalPackets_Object = MibTableColumn
hh3cUserlogAccessTotalPackets = _Hh3cUserlogAccessTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 3),
    _Hh3cUserlogAccessTotalPackets_Type()
)
hh3cUserlogAccessTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessTotalPackets.setStatus("current")
_Hh3cUserlogAccessFailedEntries_Type = Counter32
_Hh3cUserlogAccessFailedEntries_Object = MibTableColumn
hh3cUserlogAccessFailedEntries = _Hh3cUserlogAccessFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 4),
    _Hh3cUserlogAccessFailedEntries_Type()
)
hh3cUserlogAccessFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessFailedEntries.setStatus("current")
_Hh3cUserlogAccessFailedPackets_Type = Counter32
_Hh3cUserlogAccessFailedPackets_Object = MibTableColumn
hh3cUserlogAccessFailedPackets = _Hh3cUserlogAccessFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 5),
    _Hh3cUserlogAccessFailedPackets_Type()
)
hh3cUserlogAccessFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUserlogAccessFailedPackets.setStatus("current")
_Hh3cUserlogAccessClearRunStat_Type = Integer32
_Hh3cUserlogAccessClearRunStat_Object = MibTableColumn
hh3cUserlogAccessClearRunStat = _Hh3cUserlogAccessClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 6),
    _Hh3cUserlogAccessClearRunStat_Type()
)
hh3cUserlogAccessClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUserlogAccessClearRunStat.setStatus("current")
_Hh3cUserlogNotifications_ObjectIdentity = ObjectIdentity
hh3cUserlogNotifications = _Hh3cUserlogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 2)
)
_Hh3cUserlogConformance_ObjectIdentity = ObjectIdentity
hh3cUserlogConformance = _Hh3cUserlogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3)
)
_Hh3cUserlogCompliances_ObjectIdentity = ObjectIdentity
hh3cUserlogCompliances = _Hh3cUserlogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 1)
)
_Hh3cUserlogGroups_ObjectIdentity = ObjectIdentity
hh3cUserlogGroups = _Hh3cUserlogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2)
)

# Managed Objects groups

hh3cUserlogMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 1)
)
hh3cUserlogMandatoryGroup.setObjects(
      *(("HH3C-USERLOG-MIB", "hh3cUserlogNatEnable"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatHostAddress"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatUdpPort"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowEnable"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowHostAddress"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowUdpPort"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessEnable"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessHostAddress"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessUdpPort"))
)
if mibBuilder.loadTexts:
    hh3cUserlogMandatoryGroup.setStatus("current")

hh3cUserlogConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 2)
)
hh3cUserlogConfigGroup.setObjects(
      *(("HH3C-USERLOG-MIB", "hh3cUserlogNatVersion"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatSyslog"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatSourceIP"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatFlowBegin"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatActiveTime"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatCfgSlotNumber"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatEnable"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatAclNumber"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatHostAddress"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatUdpPort"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowVersion"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowSyslog"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowSourceIP"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFlowBegin"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowActiveTime"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowCfgSlotNumber"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowEnable"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowAclNumber"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowHostAddress"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowUdpPort"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessVersion"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessSyslog"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessSourceIP"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessCfgSlotNumber"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessEnable"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessHostAddress"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessUdpPort"))
)
if mibBuilder.loadTexts:
    hh3cUserlogConfigGroup.setStatus("current")

hh3cUserlogInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 3)
)
hh3cUserlogInfoGroup.setObjects(
      *(("HH3C-USERLOG-MIB", "hh3cUserlogNatTotalEntries"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatTotalPackets"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatFailedEntries"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogNatFailedPackets"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowTotalEntries"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowTotalPackets"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFailedEntries"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFailedPackets"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessTotalEntries"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessTotalPackets"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessFailedEntries"),
        ("HH3C-USERLOG-MIB", "hh3cUserlogAccessFailedPackets"))
)
if mibBuilder.loadTexts:
    hh3cUserlogInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cUserlogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cUserlogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-USERLOG-MIB",
    **{"hh3cUserLogMIB": hh3cUserLogMIB,
       "hh3cUserlogObjects": hh3cUserlogObjects,
       "hh3cUserlogNatObjects": hh3cUserlogNatObjects,
       "hh3cUserlogNatVersion": hh3cUserlogNatVersion,
       "hh3cUserlogNatSyslog": hh3cUserlogNatSyslog,
       "hh3cUserlogNatSourceIP": hh3cUserlogNatSourceIP,
       "hh3cUserlogNatFlowBegin": hh3cUserlogNatFlowBegin,
       "hh3cUserlogNatActiveTime": hh3cUserlogNatActiveTime,
       "hh3cUserlogNatSlotCfgInfoTable": hh3cUserlogNatSlotCfgInfoTable,
       "hh3cUserlogNatSlotCfgInfoEntry": hh3cUserlogNatSlotCfgInfoEntry,
       "hh3cUserlogNatCfgSlotNumber": hh3cUserlogNatCfgSlotNumber,
       "hh3cUserlogNatEnable": hh3cUserlogNatEnable,
       "hh3cUserlogNatAclNumber": hh3cUserlogNatAclNumber,
       "hh3cUserlogNatHostAddress": hh3cUserlogNatHostAddress,
       "hh3cUserlogNatUdpPort": hh3cUserlogNatUdpPort,
       "hh3cUserlogNatSlotRunInfoTable": hh3cUserlogNatSlotRunInfoTable,
       "hh3cUserlogNatSlotRunInfoEntry": hh3cUserlogNatSlotRunInfoEntry,
       "hh3cUserlogNatRunSlotNumber": hh3cUserlogNatRunSlotNumber,
       "hh3cUserlogNatTotalEntries": hh3cUserlogNatTotalEntries,
       "hh3cUserlogNatTotalPackets": hh3cUserlogNatTotalPackets,
       "hh3cUserlogNatFailedEntries": hh3cUserlogNatFailedEntries,
       "hh3cUserlogNatFailedPackets": hh3cUserlogNatFailedPackets,
       "hh3cUserlogNatClearRunStat": hh3cUserlogNatClearRunStat,
       "hh3cUserlogFlowObjects": hh3cUserlogFlowObjects,
       "hh3cUserlogFlowVersion": hh3cUserlogFlowVersion,
       "hh3cUserlogFlowSyslog": hh3cUserlogFlowSyslog,
       "hh3cUserlogFlowSourceIP": hh3cUserlogFlowSourceIP,
       "hh3cUserlogFlowFlowBegin": hh3cUserlogFlowFlowBegin,
       "hh3cUserlogFlowActiveTime": hh3cUserlogFlowActiveTime,
       "hh3cUserlogFlowSlotCfgInfoTable": hh3cUserlogFlowSlotCfgInfoTable,
       "hh3cUserlogFlowSlotCfgInfoEntry": hh3cUserlogFlowSlotCfgInfoEntry,
       "hh3cUserlogFlowCfgSlotNumber": hh3cUserlogFlowCfgSlotNumber,
       "hh3cUserlogFlowEnable": hh3cUserlogFlowEnable,
       "hh3cUserlogFlowAclNumber": hh3cUserlogFlowAclNumber,
       "hh3cUserlogFlowHostAddress": hh3cUserlogFlowHostAddress,
       "hh3cUserlogFlowUdpPort": hh3cUserlogFlowUdpPort,
       "hh3cUserlogFlowSlotRunInfoTable": hh3cUserlogFlowSlotRunInfoTable,
       "hh3cUserlogFlowSlotRunInfoEntry": hh3cUserlogFlowSlotRunInfoEntry,
       "hh3cUserlogFlowRunSlotNumber": hh3cUserlogFlowRunSlotNumber,
       "hh3cUserlogFlowTotalEntries": hh3cUserlogFlowTotalEntries,
       "hh3cUserlogFlowTotalPackets": hh3cUserlogFlowTotalPackets,
       "hh3cUserlogFlowFailedEntries": hh3cUserlogFlowFailedEntries,
       "hh3cUserlogFlowFailedPackets": hh3cUserlogFlowFailedPackets,
       "hh3cUserlogFlowClearRunStat": hh3cUserlogFlowClearRunStat,
       "hh3cUserlogAccessObjects": hh3cUserlogAccessObjects,
       "hh3cUserlogAccessVersion": hh3cUserlogAccessVersion,
       "hh3cUserlogAccessSyslog": hh3cUserlogAccessSyslog,
       "hh3cUserlogAccessSourceIP": hh3cUserlogAccessSourceIP,
       "hh3cUserlogAccessSlotCfgInfoTable": hh3cUserlogAccessSlotCfgInfoTable,
       "hh3cUserlogAccessSlotCfgInfoEntry": hh3cUserlogAccessSlotCfgInfoEntry,
       "hh3cUserlogAccessCfgSlotNumber": hh3cUserlogAccessCfgSlotNumber,
       "hh3cUserlogAccessEnable": hh3cUserlogAccessEnable,
       "hh3cUserlogAccessHostAddress": hh3cUserlogAccessHostAddress,
       "hh3cUserlogAccessUdpPort": hh3cUserlogAccessUdpPort,
       "hh3cUserlogAccessSlotRunInfoTable": hh3cUserlogAccessSlotRunInfoTable,
       "hh3cUserlogAccessSlotRunInfoEntry": hh3cUserlogAccessSlotRunInfoEntry,
       "hh3cUserlogAccessRunSlotNumber": hh3cUserlogAccessRunSlotNumber,
       "hh3cUserlogAccessTotalEntries": hh3cUserlogAccessTotalEntries,
       "hh3cUserlogAccessTotalPackets": hh3cUserlogAccessTotalPackets,
       "hh3cUserlogAccessFailedEntries": hh3cUserlogAccessFailedEntries,
       "hh3cUserlogAccessFailedPackets": hh3cUserlogAccessFailedPackets,
       "hh3cUserlogAccessClearRunStat": hh3cUserlogAccessClearRunStat,
       "hh3cUserlogNotifications": hh3cUserlogNotifications,
       "hh3cUserlogConformance": hh3cUserlogConformance,
       "hh3cUserlogCompliances": hh3cUserlogCompliances,
       "hh3cUserlogCompliance": hh3cUserlogCompliance,
       "hh3cUserlogGroups": hh3cUserlogGroups,
       "hh3cUserlogMandatoryGroup": hh3cUserlogMandatoryGroup,
       "hh3cUserlogConfigGroup": hh3cUserlogConfigGroup,
       "hh3cUserlogInfoGroup": hh3cUserlogInfoGroup}
)
