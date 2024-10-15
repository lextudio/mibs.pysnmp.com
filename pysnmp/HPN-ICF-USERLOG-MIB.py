# SNMP MIB module (HPN-ICF-USERLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-USERLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:07 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfUserLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfUserlogObjects_ObjectIdentity = ObjectIdentity
hpnicfUserlogObjects = _HpnicfUserlogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1)
)
_HpnicfUserlogNatObjects_ObjectIdentity = ObjectIdentity
hpnicfUserlogNatObjects = _HpnicfUserlogNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1)
)
_HpnicfUserlogNatVersion_Type = Integer32
_HpnicfUserlogNatVersion_Object = MibScalar
hpnicfUserlogNatVersion = _HpnicfUserlogNatVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 1),
    _HpnicfUserlogNatVersion_Type()
)
hpnicfUserlogNatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatVersion.setStatus("current")
_HpnicfUserlogNatSyslog_Type = Integer32
_HpnicfUserlogNatSyslog_Object = MibScalar
hpnicfUserlogNatSyslog = _HpnicfUserlogNatSyslog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 2),
    _HpnicfUserlogNatSyslog_Type()
)
hpnicfUserlogNatSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatSyslog.setStatus("current")
_HpnicfUserlogNatSourceIP_Type = IpAddress
_HpnicfUserlogNatSourceIP_Object = MibScalar
hpnicfUserlogNatSourceIP = _HpnicfUserlogNatSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 3),
    _HpnicfUserlogNatSourceIP_Type()
)
hpnicfUserlogNatSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatSourceIP.setStatus("current")
_HpnicfUserlogNatFlowBegin_Type = Integer32
_HpnicfUserlogNatFlowBegin_Object = MibScalar
hpnicfUserlogNatFlowBegin = _HpnicfUserlogNatFlowBegin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 4),
    _HpnicfUserlogNatFlowBegin_Type()
)
hpnicfUserlogNatFlowBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatFlowBegin.setStatus("current")
_HpnicfUserlogNatActiveTime_Type = Integer32
_HpnicfUserlogNatActiveTime_Object = MibScalar
hpnicfUserlogNatActiveTime = _HpnicfUserlogNatActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 5),
    _HpnicfUserlogNatActiveTime_Type()
)
hpnicfUserlogNatActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatActiveTime.setStatus("current")
_HpnicfUserlogNatSlotCfgInfoTable_Object = MibTable
hpnicfUserlogNatSlotCfgInfoTable = _HpnicfUserlogNatSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfUserlogNatSlotCfgInfoTable.setStatus("current")
_HpnicfUserlogNatSlotCfgInfoEntry_Object = MibTableRow
hpnicfUserlogNatSlotCfgInfoEntry = _HpnicfUserlogNatSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6, 1)
)
hpnicfUserlogNatSlotCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hpnicfUserlogNatSlotCfgInfoEntry.setStatus("current")


class _HpnicfUserlogNatCfgSlotNumber_Type(Integer32):
    """Custom type hpnicfUserlogNatCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfUserlogNatCfgSlotNumber_Type.__name__ = "Integer32"
_HpnicfUserlogNatCfgSlotNumber_Object = MibTableColumn
hpnicfUserlogNatCfgSlotNumber = _HpnicfUserlogNatCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6, 1, 1),
    _HpnicfUserlogNatCfgSlotNumber_Type()
)
hpnicfUserlogNatCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatCfgSlotNumber.setStatus("current")
_HpnicfUserlogNatEnable_Type = Integer32
_HpnicfUserlogNatEnable_Object = MibTableColumn
hpnicfUserlogNatEnable = _HpnicfUserlogNatEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6, 1, 2),
    _HpnicfUserlogNatEnable_Type()
)
hpnicfUserlogNatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatEnable.setStatus("current")
_HpnicfUserlogNatAclNumber_Type = Integer32
_HpnicfUserlogNatAclNumber_Object = MibTableColumn
hpnicfUserlogNatAclNumber = _HpnicfUserlogNatAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6, 1, 3),
    _HpnicfUserlogNatAclNumber_Type()
)
hpnicfUserlogNatAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatAclNumber.setStatus("current")
_HpnicfUserlogNatHostAddress_Type = IpAddress
_HpnicfUserlogNatHostAddress_Object = MibTableColumn
hpnicfUserlogNatHostAddress = _HpnicfUserlogNatHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6, 1, 4),
    _HpnicfUserlogNatHostAddress_Type()
)
hpnicfUserlogNatHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatHostAddress.setStatus("current")


class _HpnicfUserlogNatUdpPort_Type(Integer32):
    """Custom type hpnicfUserlogNatUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfUserlogNatUdpPort_Type.__name__ = "Integer32"
_HpnicfUserlogNatUdpPort_Object = MibTableColumn
hpnicfUserlogNatUdpPort = _HpnicfUserlogNatUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 6, 1, 5),
    _HpnicfUserlogNatUdpPort_Type()
)
hpnicfUserlogNatUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatUdpPort.setStatus("current")
_HpnicfUserlogNatSlotRunInfoTable_Object = MibTable
hpnicfUserlogNatSlotRunInfoTable = _HpnicfUserlogNatSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfUserlogNatSlotRunInfoTable.setStatus("current")
_HpnicfUserlogNatSlotRunInfoEntry_Object = MibTableRow
hpnicfUserlogNatSlotRunInfoEntry = _HpnicfUserlogNatSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1)
)
hpnicfUserlogNatSlotRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hpnicfUserlogNatSlotRunInfoEntry.setStatus("current")


class _HpnicfUserlogNatRunSlotNumber_Type(Integer32):
    """Custom type hpnicfUserlogNatRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfUserlogNatRunSlotNumber_Type.__name__ = "Integer32"
_HpnicfUserlogNatRunSlotNumber_Object = MibTableColumn
hpnicfUserlogNatRunSlotNumber = _HpnicfUserlogNatRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1, 1),
    _HpnicfUserlogNatRunSlotNumber_Type()
)
hpnicfUserlogNatRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatRunSlotNumber.setStatus("current")
_HpnicfUserlogNatTotalEntries_Type = Counter32
_HpnicfUserlogNatTotalEntries_Object = MibTableColumn
hpnicfUserlogNatTotalEntries = _HpnicfUserlogNatTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1, 2),
    _HpnicfUserlogNatTotalEntries_Type()
)
hpnicfUserlogNatTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatTotalEntries.setStatus("current")
_HpnicfUserlogNatTotalPackets_Type = Counter32
_HpnicfUserlogNatTotalPackets_Object = MibTableColumn
hpnicfUserlogNatTotalPackets = _HpnicfUserlogNatTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1, 3),
    _HpnicfUserlogNatTotalPackets_Type()
)
hpnicfUserlogNatTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatTotalPackets.setStatus("current")
_HpnicfUserlogNatFailedEntries_Type = Counter32
_HpnicfUserlogNatFailedEntries_Object = MibTableColumn
hpnicfUserlogNatFailedEntries = _HpnicfUserlogNatFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1, 4),
    _HpnicfUserlogNatFailedEntries_Type()
)
hpnicfUserlogNatFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatFailedEntries.setStatus("current")
_HpnicfUserlogNatFailedPackets_Type = Counter32
_HpnicfUserlogNatFailedPackets_Object = MibTableColumn
hpnicfUserlogNatFailedPackets = _HpnicfUserlogNatFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1, 5),
    _HpnicfUserlogNatFailedPackets_Type()
)
hpnicfUserlogNatFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogNatFailedPackets.setStatus("current")
_HpnicfUserlogNatClearRunStat_Type = Integer32
_HpnicfUserlogNatClearRunStat_Object = MibTableColumn
hpnicfUserlogNatClearRunStat = _HpnicfUserlogNatClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 1, 7, 1, 6),
    _HpnicfUserlogNatClearRunStat_Type()
)
hpnicfUserlogNatClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogNatClearRunStat.setStatus("current")
_HpnicfUserlogFlowObjects_ObjectIdentity = ObjectIdentity
hpnicfUserlogFlowObjects = _HpnicfUserlogFlowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2)
)
_HpnicfUserlogFlowVersion_Type = Integer32
_HpnicfUserlogFlowVersion_Object = MibScalar
hpnicfUserlogFlowVersion = _HpnicfUserlogFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 1),
    _HpnicfUserlogFlowVersion_Type()
)
hpnicfUserlogFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowVersion.setStatus("current")
_HpnicfUserlogFlowSyslog_Type = Integer32
_HpnicfUserlogFlowSyslog_Object = MibScalar
hpnicfUserlogFlowSyslog = _HpnicfUserlogFlowSyslog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 2),
    _HpnicfUserlogFlowSyslog_Type()
)
hpnicfUserlogFlowSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowSyslog.setStatus("current")
_HpnicfUserlogFlowSourceIP_Type = IpAddress
_HpnicfUserlogFlowSourceIP_Object = MibScalar
hpnicfUserlogFlowSourceIP = _HpnicfUserlogFlowSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 3),
    _HpnicfUserlogFlowSourceIP_Type()
)
hpnicfUserlogFlowSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowSourceIP.setStatus("current")
_HpnicfUserlogFlowFlowBegin_Type = Integer32
_HpnicfUserlogFlowFlowBegin_Object = MibScalar
hpnicfUserlogFlowFlowBegin = _HpnicfUserlogFlowFlowBegin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 4),
    _HpnicfUserlogFlowFlowBegin_Type()
)
hpnicfUserlogFlowFlowBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowFlowBegin.setStatus("current")
_HpnicfUserlogFlowActiveTime_Type = Integer32
_HpnicfUserlogFlowActiveTime_Object = MibScalar
hpnicfUserlogFlowActiveTime = _HpnicfUserlogFlowActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 5),
    _HpnicfUserlogFlowActiveTime_Type()
)
hpnicfUserlogFlowActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowActiveTime.setStatus("current")
_HpnicfUserlogFlowSlotCfgInfoTable_Object = MibTable
hpnicfUserlogFlowSlotCfgInfoTable = _HpnicfUserlogFlowSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfUserlogFlowSlotCfgInfoTable.setStatus("current")
_HpnicfUserlogFlowSlotCfgInfoEntry_Object = MibTableRow
hpnicfUserlogFlowSlotCfgInfoEntry = _HpnicfUserlogFlowSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6, 1)
)
hpnicfUserlogFlowSlotCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hpnicfUserlogFlowSlotCfgInfoEntry.setStatus("current")


class _HpnicfUserlogFlowCfgSlotNumber_Type(Integer32):
    """Custom type hpnicfUserlogFlowCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfUserlogFlowCfgSlotNumber_Type.__name__ = "Integer32"
_HpnicfUserlogFlowCfgSlotNumber_Object = MibTableColumn
hpnicfUserlogFlowCfgSlotNumber = _HpnicfUserlogFlowCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6, 1, 1),
    _HpnicfUserlogFlowCfgSlotNumber_Type()
)
hpnicfUserlogFlowCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowCfgSlotNumber.setStatus("current")
_HpnicfUserlogFlowEnable_Type = Integer32
_HpnicfUserlogFlowEnable_Object = MibTableColumn
hpnicfUserlogFlowEnable = _HpnicfUserlogFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6, 1, 2),
    _HpnicfUserlogFlowEnable_Type()
)
hpnicfUserlogFlowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowEnable.setStatus("current")
_HpnicfUserlogFlowAclNumber_Type = Integer32
_HpnicfUserlogFlowAclNumber_Object = MibTableColumn
hpnicfUserlogFlowAclNumber = _HpnicfUserlogFlowAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6, 1, 3),
    _HpnicfUserlogFlowAclNumber_Type()
)
hpnicfUserlogFlowAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowAclNumber.setStatus("current")
_HpnicfUserlogFlowHostAddress_Type = IpAddress
_HpnicfUserlogFlowHostAddress_Object = MibTableColumn
hpnicfUserlogFlowHostAddress = _HpnicfUserlogFlowHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6, 1, 4),
    _HpnicfUserlogFlowHostAddress_Type()
)
hpnicfUserlogFlowHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowHostAddress.setStatus("current")


class _HpnicfUserlogFlowUdpPort_Type(Integer32):
    """Custom type hpnicfUserlogFlowUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfUserlogFlowUdpPort_Type.__name__ = "Integer32"
_HpnicfUserlogFlowUdpPort_Object = MibTableColumn
hpnicfUserlogFlowUdpPort = _HpnicfUserlogFlowUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 6, 1, 5),
    _HpnicfUserlogFlowUdpPort_Type()
)
hpnicfUserlogFlowUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowUdpPort.setStatus("current")
_HpnicfUserlogFlowSlotRunInfoTable_Object = MibTable
hpnicfUserlogFlowSlotRunInfoTable = _HpnicfUserlogFlowSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfUserlogFlowSlotRunInfoTable.setStatus("current")
_HpnicfUserlogFlowSlotRunInfoEntry_Object = MibTableRow
hpnicfUserlogFlowSlotRunInfoEntry = _HpnicfUserlogFlowSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1)
)
hpnicfUserlogFlowSlotRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hpnicfUserlogFlowSlotRunInfoEntry.setStatus("current")


class _HpnicfUserlogFlowRunSlotNumber_Type(Integer32):
    """Custom type hpnicfUserlogFlowRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfUserlogFlowRunSlotNumber_Type.__name__ = "Integer32"
_HpnicfUserlogFlowRunSlotNumber_Object = MibTableColumn
hpnicfUserlogFlowRunSlotNumber = _HpnicfUserlogFlowRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1, 1),
    _HpnicfUserlogFlowRunSlotNumber_Type()
)
hpnicfUserlogFlowRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowRunSlotNumber.setStatus("current")
_HpnicfUserlogFlowTotalEntries_Type = Counter32
_HpnicfUserlogFlowTotalEntries_Object = MibTableColumn
hpnicfUserlogFlowTotalEntries = _HpnicfUserlogFlowTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1, 2),
    _HpnicfUserlogFlowTotalEntries_Type()
)
hpnicfUserlogFlowTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowTotalEntries.setStatus("current")
_HpnicfUserlogFlowTotalPackets_Type = Counter32
_HpnicfUserlogFlowTotalPackets_Object = MibTableColumn
hpnicfUserlogFlowTotalPackets = _HpnicfUserlogFlowTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1, 3),
    _HpnicfUserlogFlowTotalPackets_Type()
)
hpnicfUserlogFlowTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowTotalPackets.setStatus("current")
_HpnicfUserlogFlowFailedEntries_Type = Counter32
_HpnicfUserlogFlowFailedEntries_Object = MibTableColumn
hpnicfUserlogFlowFailedEntries = _HpnicfUserlogFlowFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1, 4),
    _HpnicfUserlogFlowFailedEntries_Type()
)
hpnicfUserlogFlowFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowFailedEntries.setStatus("current")
_HpnicfUserlogFlowFailedPackets_Type = Counter32
_HpnicfUserlogFlowFailedPackets_Object = MibTableColumn
hpnicfUserlogFlowFailedPackets = _HpnicfUserlogFlowFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1, 5),
    _HpnicfUserlogFlowFailedPackets_Type()
)
hpnicfUserlogFlowFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowFailedPackets.setStatus("current")
_HpnicfUserlogFlowClearRunStat_Type = Integer32
_HpnicfUserlogFlowClearRunStat_Object = MibTableColumn
hpnicfUserlogFlowClearRunStat = _HpnicfUserlogFlowClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 2, 7, 1, 6),
    _HpnicfUserlogFlowClearRunStat_Type()
)
hpnicfUserlogFlowClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogFlowClearRunStat.setStatus("current")
_HpnicfUserlogAccessObjects_ObjectIdentity = ObjectIdentity
hpnicfUserlogAccessObjects = _HpnicfUserlogAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3)
)
_HpnicfUserlogAccessVersion_Type = Integer32
_HpnicfUserlogAccessVersion_Object = MibScalar
hpnicfUserlogAccessVersion = _HpnicfUserlogAccessVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 1),
    _HpnicfUserlogAccessVersion_Type()
)
hpnicfUserlogAccessVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessVersion.setStatus("current")
_HpnicfUserlogAccessSyslog_Type = Integer32
_HpnicfUserlogAccessSyslog_Object = MibScalar
hpnicfUserlogAccessSyslog = _HpnicfUserlogAccessSyslog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 2),
    _HpnicfUserlogAccessSyslog_Type()
)
hpnicfUserlogAccessSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessSyslog.setStatus("current")
_HpnicfUserlogAccessSourceIP_Type = IpAddress
_HpnicfUserlogAccessSourceIP_Object = MibScalar
hpnicfUserlogAccessSourceIP = _HpnicfUserlogAccessSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 3),
    _HpnicfUserlogAccessSourceIP_Type()
)
hpnicfUserlogAccessSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessSourceIP.setStatus("current")
_HpnicfUserlogAccessSlotCfgInfoTable_Object = MibTable
hpnicfUserlogAccessSlotCfgInfoTable = _HpnicfUserlogAccessSlotCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfUserlogAccessSlotCfgInfoTable.setStatus("current")
_HpnicfUserlogAccessSlotCfgInfoEntry_Object = MibTableRow
hpnicfUserlogAccessSlotCfgInfoEntry = _HpnicfUserlogAccessSlotCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 4, 1)
)
hpnicfUserlogAccessSlotCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessCfgSlotNumber"),
)
if mibBuilder.loadTexts:
    hpnicfUserlogAccessSlotCfgInfoEntry.setStatus("current")


class _HpnicfUserlogAccessCfgSlotNumber_Type(Integer32):
    """Custom type hpnicfUserlogAccessCfgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfUserlogAccessCfgSlotNumber_Type.__name__ = "Integer32"
_HpnicfUserlogAccessCfgSlotNumber_Object = MibTableColumn
hpnicfUserlogAccessCfgSlotNumber = _HpnicfUserlogAccessCfgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 4, 1, 1),
    _HpnicfUserlogAccessCfgSlotNumber_Type()
)
hpnicfUserlogAccessCfgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessCfgSlotNumber.setStatus("current")
_HpnicfUserlogAccessEnable_Type = Integer32
_HpnicfUserlogAccessEnable_Object = MibTableColumn
hpnicfUserlogAccessEnable = _HpnicfUserlogAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 4, 1, 2),
    _HpnicfUserlogAccessEnable_Type()
)
hpnicfUserlogAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessEnable.setStatus("current")
_HpnicfUserlogAccessHostAddress_Type = IpAddress
_HpnicfUserlogAccessHostAddress_Object = MibTableColumn
hpnicfUserlogAccessHostAddress = _HpnicfUserlogAccessHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 4, 1, 3),
    _HpnicfUserlogAccessHostAddress_Type()
)
hpnicfUserlogAccessHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessHostAddress.setStatus("current")


class _HpnicfUserlogAccessUdpPort_Type(Integer32):
    """Custom type hpnicfUserlogAccessUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfUserlogAccessUdpPort_Type.__name__ = "Integer32"
_HpnicfUserlogAccessUdpPort_Object = MibTableColumn
hpnicfUserlogAccessUdpPort = _HpnicfUserlogAccessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 4, 1, 4),
    _HpnicfUserlogAccessUdpPort_Type()
)
hpnicfUserlogAccessUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessUdpPort.setStatus("current")
_HpnicfUserlogAccessSlotRunInfoTable_Object = MibTable
hpnicfUserlogAccessSlotRunInfoTable = _HpnicfUserlogAccessSlotRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hpnicfUserlogAccessSlotRunInfoTable.setStatus("current")
_HpnicfUserlogAccessSlotRunInfoEntry_Object = MibTableRow
hpnicfUserlogAccessSlotRunInfoEntry = _HpnicfUserlogAccessSlotRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1)
)
hpnicfUserlogAccessSlotRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessRunSlotNumber"),
)
if mibBuilder.loadTexts:
    hpnicfUserlogAccessSlotRunInfoEntry.setStatus("current")


class _HpnicfUserlogAccessRunSlotNumber_Type(Integer32):
    """Custom type hpnicfUserlogAccessRunSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfUserlogAccessRunSlotNumber_Type.__name__ = "Integer32"
_HpnicfUserlogAccessRunSlotNumber_Object = MibTableColumn
hpnicfUserlogAccessRunSlotNumber = _HpnicfUserlogAccessRunSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1, 1),
    _HpnicfUserlogAccessRunSlotNumber_Type()
)
hpnicfUserlogAccessRunSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessRunSlotNumber.setStatus("current")
_HpnicfUserlogAccessTotalEntries_Type = Counter32
_HpnicfUserlogAccessTotalEntries_Object = MibTableColumn
hpnicfUserlogAccessTotalEntries = _HpnicfUserlogAccessTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1, 2),
    _HpnicfUserlogAccessTotalEntries_Type()
)
hpnicfUserlogAccessTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessTotalEntries.setStatus("current")
_HpnicfUserlogAccessTotalPackets_Type = Counter32
_HpnicfUserlogAccessTotalPackets_Object = MibTableColumn
hpnicfUserlogAccessTotalPackets = _HpnicfUserlogAccessTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1, 3),
    _HpnicfUserlogAccessTotalPackets_Type()
)
hpnicfUserlogAccessTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessTotalPackets.setStatus("current")
_HpnicfUserlogAccessFailedEntries_Type = Counter32
_HpnicfUserlogAccessFailedEntries_Object = MibTableColumn
hpnicfUserlogAccessFailedEntries = _HpnicfUserlogAccessFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1, 4),
    _HpnicfUserlogAccessFailedEntries_Type()
)
hpnicfUserlogAccessFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessFailedEntries.setStatus("current")
_HpnicfUserlogAccessFailedPackets_Type = Counter32
_HpnicfUserlogAccessFailedPackets_Object = MibTableColumn
hpnicfUserlogAccessFailedPackets = _HpnicfUserlogAccessFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1, 5),
    _HpnicfUserlogAccessFailedPackets_Type()
)
hpnicfUserlogAccessFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessFailedPackets.setStatus("current")
_HpnicfUserlogAccessClearRunStat_Type = Integer32
_HpnicfUserlogAccessClearRunStat_Object = MibTableColumn
hpnicfUserlogAccessClearRunStat = _HpnicfUserlogAccessClearRunStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 1, 3, 5, 1, 6),
    _HpnicfUserlogAccessClearRunStat_Type()
)
hpnicfUserlogAccessClearRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfUserlogAccessClearRunStat.setStatus("current")
_HpnicfUserlogNotifications_ObjectIdentity = ObjectIdentity
hpnicfUserlogNotifications = _HpnicfUserlogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 2)
)
_HpnicfUserlogConformance_ObjectIdentity = ObjectIdentity
hpnicfUserlogConformance = _HpnicfUserlogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3)
)
_HpnicfUserlogCompliances_ObjectIdentity = ObjectIdentity
hpnicfUserlogCompliances = _HpnicfUserlogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3, 1)
)
_HpnicfUserlogGroups_ObjectIdentity = ObjectIdentity
hpnicfUserlogGroups = _HpnicfUserlogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3, 2)
)

# Managed Objects groups

hpnicfUserlogMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3, 2, 1)
)
hpnicfUserlogMandatoryGroup.setObjects(
      *(("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatEnable"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatHostAddress"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatUdpPort"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowEnable"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowHostAddress"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowUdpPort"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessEnable"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessHostAddress"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessUdpPort"))
)
if mibBuilder.loadTexts:
    hpnicfUserlogMandatoryGroup.setStatus("current")

hpnicfUserlogConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3, 2, 2)
)
hpnicfUserlogConfigGroup.setObjects(
      *(("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatVersion"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatSyslog"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatSourceIP"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatFlowBegin"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatActiveTime"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatCfgSlotNumber"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatEnable"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatAclNumber"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatHostAddress"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatUdpPort"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowVersion"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowSyslog"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowSourceIP"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowFlowBegin"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowActiveTime"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowCfgSlotNumber"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowEnable"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowAclNumber"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowHostAddress"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowUdpPort"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessVersion"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessSyslog"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessSourceIP"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessCfgSlotNumber"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessEnable"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessHostAddress"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessUdpPort"))
)
if mibBuilder.loadTexts:
    hpnicfUserlogConfigGroup.setStatus("current")

hpnicfUserlogInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3, 2, 3)
)
hpnicfUserlogInfoGroup.setObjects(
      *(("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatTotalEntries"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatTotalPackets"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatFailedEntries"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogNatFailedPackets"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowTotalEntries"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowTotalPackets"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowFailedEntries"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogFlowFailedPackets"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessTotalEntries"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessTotalPackets"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessFailedEntries"),
        ("HPN-ICF-USERLOG-MIB", "hpnicfUserlogAccessFailedPackets"))
)
if mibBuilder.loadTexts:
    hpnicfUserlogInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfUserlogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfUserlogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-USERLOG-MIB",
    **{"hpnicfUserLogMIB": hpnicfUserLogMIB,
       "hpnicfUserlogObjects": hpnicfUserlogObjects,
       "hpnicfUserlogNatObjects": hpnicfUserlogNatObjects,
       "hpnicfUserlogNatVersion": hpnicfUserlogNatVersion,
       "hpnicfUserlogNatSyslog": hpnicfUserlogNatSyslog,
       "hpnicfUserlogNatSourceIP": hpnicfUserlogNatSourceIP,
       "hpnicfUserlogNatFlowBegin": hpnicfUserlogNatFlowBegin,
       "hpnicfUserlogNatActiveTime": hpnicfUserlogNatActiveTime,
       "hpnicfUserlogNatSlotCfgInfoTable": hpnicfUserlogNatSlotCfgInfoTable,
       "hpnicfUserlogNatSlotCfgInfoEntry": hpnicfUserlogNatSlotCfgInfoEntry,
       "hpnicfUserlogNatCfgSlotNumber": hpnicfUserlogNatCfgSlotNumber,
       "hpnicfUserlogNatEnable": hpnicfUserlogNatEnable,
       "hpnicfUserlogNatAclNumber": hpnicfUserlogNatAclNumber,
       "hpnicfUserlogNatHostAddress": hpnicfUserlogNatHostAddress,
       "hpnicfUserlogNatUdpPort": hpnicfUserlogNatUdpPort,
       "hpnicfUserlogNatSlotRunInfoTable": hpnicfUserlogNatSlotRunInfoTable,
       "hpnicfUserlogNatSlotRunInfoEntry": hpnicfUserlogNatSlotRunInfoEntry,
       "hpnicfUserlogNatRunSlotNumber": hpnicfUserlogNatRunSlotNumber,
       "hpnicfUserlogNatTotalEntries": hpnicfUserlogNatTotalEntries,
       "hpnicfUserlogNatTotalPackets": hpnicfUserlogNatTotalPackets,
       "hpnicfUserlogNatFailedEntries": hpnicfUserlogNatFailedEntries,
       "hpnicfUserlogNatFailedPackets": hpnicfUserlogNatFailedPackets,
       "hpnicfUserlogNatClearRunStat": hpnicfUserlogNatClearRunStat,
       "hpnicfUserlogFlowObjects": hpnicfUserlogFlowObjects,
       "hpnicfUserlogFlowVersion": hpnicfUserlogFlowVersion,
       "hpnicfUserlogFlowSyslog": hpnicfUserlogFlowSyslog,
       "hpnicfUserlogFlowSourceIP": hpnicfUserlogFlowSourceIP,
       "hpnicfUserlogFlowFlowBegin": hpnicfUserlogFlowFlowBegin,
       "hpnicfUserlogFlowActiveTime": hpnicfUserlogFlowActiveTime,
       "hpnicfUserlogFlowSlotCfgInfoTable": hpnicfUserlogFlowSlotCfgInfoTable,
       "hpnicfUserlogFlowSlotCfgInfoEntry": hpnicfUserlogFlowSlotCfgInfoEntry,
       "hpnicfUserlogFlowCfgSlotNumber": hpnicfUserlogFlowCfgSlotNumber,
       "hpnicfUserlogFlowEnable": hpnicfUserlogFlowEnable,
       "hpnicfUserlogFlowAclNumber": hpnicfUserlogFlowAclNumber,
       "hpnicfUserlogFlowHostAddress": hpnicfUserlogFlowHostAddress,
       "hpnicfUserlogFlowUdpPort": hpnicfUserlogFlowUdpPort,
       "hpnicfUserlogFlowSlotRunInfoTable": hpnicfUserlogFlowSlotRunInfoTable,
       "hpnicfUserlogFlowSlotRunInfoEntry": hpnicfUserlogFlowSlotRunInfoEntry,
       "hpnicfUserlogFlowRunSlotNumber": hpnicfUserlogFlowRunSlotNumber,
       "hpnicfUserlogFlowTotalEntries": hpnicfUserlogFlowTotalEntries,
       "hpnicfUserlogFlowTotalPackets": hpnicfUserlogFlowTotalPackets,
       "hpnicfUserlogFlowFailedEntries": hpnicfUserlogFlowFailedEntries,
       "hpnicfUserlogFlowFailedPackets": hpnicfUserlogFlowFailedPackets,
       "hpnicfUserlogFlowClearRunStat": hpnicfUserlogFlowClearRunStat,
       "hpnicfUserlogAccessObjects": hpnicfUserlogAccessObjects,
       "hpnicfUserlogAccessVersion": hpnicfUserlogAccessVersion,
       "hpnicfUserlogAccessSyslog": hpnicfUserlogAccessSyslog,
       "hpnicfUserlogAccessSourceIP": hpnicfUserlogAccessSourceIP,
       "hpnicfUserlogAccessSlotCfgInfoTable": hpnicfUserlogAccessSlotCfgInfoTable,
       "hpnicfUserlogAccessSlotCfgInfoEntry": hpnicfUserlogAccessSlotCfgInfoEntry,
       "hpnicfUserlogAccessCfgSlotNumber": hpnicfUserlogAccessCfgSlotNumber,
       "hpnicfUserlogAccessEnable": hpnicfUserlogAccessEnable,
       "hpnicfUserlogAccessHostAddress": hpnicfUserlogAccessHostAddress,
       "hpnicfUserlogAccessUdpPort": hpnicfUserlogAccessUdpPort,
       "hpnicfUserlogAccessSlotRunInfoTable": hpnicfUserlogAccessSlotRunInfoTable,
       "hpnicfUserlogAccessSlotRunInfoEntry": hpnicfUserlogAccessSlotRunInfoEntry,
       "hpnicfUserlogAccessRunSlotNumber": hpnicfUserlogAccessRunSlotNumber,
       "hpnicfUserlogAccessTotalEntries": hpnicfUserlogAccessTotalEntries,
       "hpnicfUserlogAccessTotalPackets": hpnicfUserlogAccessTotalPackets,
       "hpnicfUserlogAccessFailedEntries": hpnicfUserlogAccessFailedEntries,
       "hpnicfUserlogAccessFailedPackets": hpnicfUserlogAccessFailedPackets,
       "hpnicfUserlogAccessClearRunStat": hpnicfUserlogAccessClearRunStat,
       "hpnicfUserlogNotifications": hpnicfUserlogNotifications,
       "hpnicfUserlogConformance": hpnicfUserlogConformance,
       "hpnicfUserlogCompliances": hpnicfUserlogCompliances,
       "hpnicfUserlogCompliance": hpnicfUserlogCompliance,
       "hpnicfUserlogGroups": hpnicfUserlogGroups,
       "hpnicfUserlogMandatoryGroup": hpnicfUserlogMandatoryGroup,
       "hpnicfUserlogConfigGroup": hpnicfUserlogConfigGroup,
       "hpnicfUserlogInfoGroup": hpnicfUserlogInfoGroup}
)
