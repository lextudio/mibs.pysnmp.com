# SNMP MIB module (DFL1660-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL1660-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:14 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

dfl1660_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 1, 2)
)
dfl1660_MIB.setRevisions(
        ("2010-09-02 11:39",
         "2010-03-30 09:00",
         "2009-11-10 09:16",
         "2008-11-18 16:05",
         "2008-10-14 12:27",
         "2007-10-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_NetdefendMgmt_ObjectIdentity = ObjectIdentity
netdefendMgmt = _NetdefendMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20)
)
_UtmFirewall_ObjectIdentity = ObjectIdentity
utmFirewall = _UtmFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2)
)
_Dfl1660_ObjectIdentity = ObjectIdentity
dfl1660 = _Dfl1660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3)
)
_Dfl1660OS_ObjectIdentity = ObjectIdentity
dfl1660OS = _Dfl1660OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1)
)
_Dfl1660OSStats_ObjectIdentity = ObjectIdentity
dfl1660OSStats = _Dfl1660OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2)
)
_Dfl1660System_ObjectIdentity = ObjectIdentity
dfl1660System = _Dfl1660System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1)
)
_Dfl1660SysCpuLoad_Type = Gauge32
_Dfl1660SysCpuLoad_Object = MibScalar
dfl1660SysCpuLoad = _Dfl1660SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 1),
    _Dfl1660SysCpuLoad_Type()
)
dfl1660SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysCpuLoad.setStatus("current")
_Dfl1660SysForwardedBits_Type = Counter32
_Dfl1660SysForwardedBits_Object = MibScalar
dfl1660SysForwardedBits = _Dfl1660SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 2),
    _Dfl1660SysForwardedBits_Type()
)
dfl1660SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysForwardedBits.setStatus("current")
_Dfl1660SysForwardedPackets_Type = Counter32
_Dfl1660SysForwardedPackets_Object = MibScalar
dfl1660SysForwardedPackets = _Dfl1660SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 3),
    _Dfl1660SysForwardedPackets_Type()
)
dfl1660SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysForwardedPackets.setStatus("current")
_Dfl1660SysBuffUse_Type = Gauge32
_Dfl1660SysBuffUse_Object = MibScalar
dfl1660SysBuffUse = _Dfl1660SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 4),
    _Dfl1660SysBuffUse_Type()
)
dfl1660SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysBuffUse.setStatus("current")
_Dfl1660SysConns_Type = Gauge32
_Dfl1660SysConns_Object = MibScalar
dfl1660SysConns = _Dfl1660SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 5),
    _Dfl1660SysConns_Type()
)
dfl1660SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysConns.setStatus("current")
_Dfl1660SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl1660SysPerStateCounters = _Dfl1660SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6)
)
_Dfl1660SysPscTcpSyn_Type = Gauge32
_Dfl1660SysPscTcpSyn_Object = MibScalar
dfl1660SysPscTcpSyn = _Dfl1660SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6, 1),
    _Dfl1660SysPscTcpSyn_Type()
)
dfl1660SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysPscTcpSyn.setStatus("current")
_Dfl1660SysPscTcpOpen_Type = Gauge32
_Dfl1660SysPscTcpOpen_Object = MibScalar
dfl1660SysPscTcpOpen = _Dfl1660SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6, 2),
    _Dfl1660SysPscTcpOpen_Type()
)
dfl1660SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysPscTcpOpen.setStatus("current")
_Dfl1660SysPscTcpFin_Type = Gauge32
_Dfl1660SysPscTcpFin_Object = MibScalar
dfl1660SysPscTcpFin = _Dfl1660SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6, 3),
    _Dfl1660SysPscTcpFin_Type()
)
dfl1660SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysPscTcpFin.setStatus("current")
_Dfl1660SysPscUdp_Type = Gauge32
_Dfl1660SysPscUdp_Object = MibScalar
dfl1660SysPscUdp = _Dfl1660SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6, 4),
    _Dfl1660SysPscUdp_Type()
)
dfl1660SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysPscUdp.setStatus("current")
_Dfl1660SysPscIcmp_Type = Gauge32
_Dfl1660SysPscIcmp_Object = MibScalar
dfl1660SysPscIcmp = _Dfl1660SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6, 5),
    _Dfl1660SysPscIcmp_Type()
)
dfl1660SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysPscIcmp.setStatus("current")
_Dfl1660SysPscOther_Type = Gauge32
_Dfl1660SysPscOther_Object = MibScalar
dfl1660SysPscOther = _Dfl1660SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 6, 6),
    _Dfl1660SysPscOther_Type()
)
dfl1660SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysPscOther.setStatus("current")
_Dfl1660IfStatsTable_Object = MibTable
dfl1660IfStatsTable = _Dfl1660IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl1660IfStatsTable.setStatus("current")
_Dfl1660IfStatsEntry_Object = MibTableRow
dfl1660IfStatsEntry = _Dfl1660IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1)
)
dfl1660IfStatsEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl1660IfStatsEntry.setStatus("current")


class _Dfl1660IfStatsIndex_Type(Integer32):
    """Custom type dfl1660IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660IfStatsIndex_Type.__name__ = "Integer32"
_Dfl1660IfStatsIndex_Object = MibTableColumn
dfl1660IfStatsIndex = _Dfl1660IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 1),
    _Dfl1660IfStatsIndex_Type()
)
dfl1660IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660IfStatsIndex.setStatus("current")
_Dfl1660IfName_Type = DisplayString
_Dfl1660IfName_Object = MibTableColumn
dfl1660IfName = _Dfl1660IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 2),
    _Dfl1660IfName_Type()
)
dfl1660IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfName.setStatus("current")
_Dfl1660IfFragsIn_Type = Counter32
_Dfl1660IfFragsIn_Object = MibTableColumn
dfl1660IfFragsIn = _Dfl1660IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 3),
    _Dfl1660IfFragsIn_Type()
)
dfl1660IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfFragsIn.setStatus("current")
_Dfl1660IfFragReassOk_Type = Counter32
_Dfl1660IfFragReassOk_Object = MibTableColumn
dfl1660IfFragReassOk = _Dfl1660IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 4),
    _Dfl1660IfFragReassOk_Type()
)
dfl1660IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfFragReassOk.setStatus("current")
_Dfl1660IfFragReassFail_Type = Counter32
_Dfl1660IfFragReassFail_Object = MibTableColumn
dfl1660IfFragReassFail = _Dfl1660IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 5),
    _Dfl1660IfFragReassFail_Type()
)
dfl1660IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfFragReassFail.setStatus("current")
_Dfl1660IfPktsInCnt_Type = Counter32
_Dfl1660IfPktsInCnt_Object = MibTableColumn
dfl1660IfPktsInCnt = _Dfl1660IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 6),
    _Dfl1660IfPktsInCnt_Type()
)
dfl1660IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfPktsInCnt.setStatus("current")
_Dfl1660IfPktsOutCnt_Type = Counter32
_Dfl1660IfPktsOutCnt_Object = MibTableColumn
dfl1660IfPktsOutCnt = _Dfl1660IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 7),
    _Dfl1660IfPktsOutCnt_Type()
)
dfl1660IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfPktsOutCnt.setStatus("current")
_Dfl1660IfBitsInCnt_Type = Counter32
_Dfl1660IfBitsInCnt_Object = MibTableColumn
dfl1660IfBitsInCnt = _Dfl1660IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 8),
    _Dfl1660IfBitsInCnt_Type()
)
dfl1660IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfBitsInCnt.setStatus("current")
_Dfl1660IfBitsOutCnt_Type = Counter32
_Dfl1660IfBitsOutCnt_Object = MibTableColumn
dfl1660IfBitsOutCnt = _Dfl1660IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 9),
    _Dfl1660IfBitsOutCnt_Type()
)
dfl1660IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfBitsOutCnt.setStatus("current")
_Dfl1660IfPktsTotCnt_Type = Counter32
_Dfl1660IfPktsTotCnt_Object = MibTableColumn
dfl1660IfPktsTotCnt = _Dfl1660IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 10),
    _Dfl1660IfPktsTotCnt_Type()
)
dfl1660IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfPktsTotCnt.setStatus("current")
_Dfl1660IfBitsTotCnt_Type = Counter32
_Dfl1660IfBitsTotCnt_Object = MibTableColumn
dfl1660IfBitsTotCnt = _Dfl1660IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 11),
    _Dfl1660IfBitsTotCnt_Type()
)
dfl1660IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfBitsTotCnt.setStatus("current")
_Dfl1660IfHCPktsInCnt_Type = Counter64
_Dfl1660IfHCPktsInCnt_Object = MibTableColumn
dfl1660IfHCPktsInCnt = _Dfl1660IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 12),
    _Dfl1660IfHCPktsInCnt_Type()
)
dfl1660IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfHCPktsInCnt.setStatus("current")
_Dfl1660IfHCPktsOutCnt_Type = Counter64
_Dfl1660IfHCPktsOutCnt_Object = MibTableColumn
dfl1660IfHCPktsOutCnt = _Dfl1660IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 13),
    _Dfl1660IfHCPktsOutCnt_Type()
)
dfl1660IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfHCPktsOutCnt.setStatus("current")
_Dfl1660IfHCBitsInCnt_Type = Counter64
_Dfl1660IfHCBitsInCnt_Object = MibTableColumn
dfl1660IfHCBitsInCnt = _Dfl1660IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 14),
    _Dfl1660IfHCBitsInCnt_Type()
)
dfl1660IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfHCBitsInCnt.setStatus("current")
_Dfl1660IfHCBitsOutCnt_Type = Counter64
_Dfl1660IfHCBitsOutCnt_Object = MibTableColumn
dfl1660IfHCBitsOutCnt = _Dfl1660IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 15),
    _Dfl1660IfHCBitsOutCnt_Type()
)
dfl1660IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfHCBitsOutCnt.setStatus("current")
_Dfl1660IfHCPktsTotCnt_Type = Counter64
_Dfl1660IfHCPktsTotCnt_Object = MibTableColumn
dfl1660IfHCPktsTotCnt = _Dfl1660IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 16),
    _Dfl1660IfHCPktsTotCnt_Type()
)
dfl1660IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfHCPktsTotCnt.setStatus("current")
_Dfl1660IfHCBitsTotCnt_Type = Counter64
_Dfl1660IfHCBitsTotCnt_Object = MibTableColumn
dfl1660IfHCBitsTotCnt = _Dfl1660IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 7, 1, 17),
    _Dfl1660IfHCBitsTotCnt_Type()
)
dfl1660IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfHCBitsTotCnt.setStatus("current")
_Dfl1660IfRxRingTable_Object = MibTable
dfl1660IfRxRingTable = _Dfl1660IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl1660IfRxRingTable.setStatus("current")
_Dfl1660IfRxRingEntry_Object = MibTableRow
dfl1660IfRxRingEntry = _Dfl1660IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1)
)
dfl1660IfRxRingEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl1660IfRxRingEntry.setStatus("current")


class _Dfl1660IfRxRingIndex_Type(Integer32):
    """Custom type dfl1660IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl1660IfRxRingIndex_Object = MibTableColumn
dfl1660IfRxRingIndex = _Dfl1660IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1, 1),
    _Dfl1660IfRxRingIndex_Type()
)
dfl1660IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660IfRxRingIndex.setStatus("current")
_Dfl1660IfRxRingFifoErrors_Type = Counter32
_Dfl1660IfRxRingFifoErrors_Object = MibTableColumn
dfl1660IfRxRingFifoErrors = _Dfl1660IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1, 2),
    _Dfl1660IfRxRingFifoErrors_Type()
)
dfl1660IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfRxRingFifoErrors.setStatus("current")
_Dfl1660IfRxDespools_Type = Gauge32
_Dfl1660IfRxDespools_Object = MibTableColumn
dfl1660IfRxDespools = _Dfl1660IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1, 3),
    _Dfl1660IfRxDespools_Type()
)
dfl1660IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfRxDespools.setStatus("current")
_Dfl1660IfRxAvgUse_Type = Gauge32
_Dfl1660IfRxAvgUse_Object = MibTableColumn
dfl1660IfRxAvgUse = _Dfl1660IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1, 4),
    _Dfl1660IfRxAvgUse_Type()
)
dfl1660IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfRxAvgUse.setStatus("current")
_Dfl1660IfRxRingSaturation_Type = Gauge32
_Dfl1660IfRxRingSaturation_Object = MibTableColumn
dfl1660IfRxRingSaturation = _Dfl1660IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1, 5),
    _Dfl1660IfRxRingSaturation_Type()
)
dfl1660IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfRxRingSaturation.setStatus("current")
_Dfl1660RxRingFlooded_Type = Gauge32
_Dfl1660RxRingFlooded_Object = MibTableColumn
dfl1660RxRingFlooded = _Dfl1660RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 8, 1, 6),
    _Dfl1660RxRingFlooded_Type()
)
dfl1660RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660RxRingFlooded.setStatus("current")
_Dfl1660IfTxRingTable_Object = MibTable
dfl1660IfTxRingTable = _Dfl1660IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl1660IfTxRingTable.setStatus("current")
_Dfl1660IfTxRingEntry_Object = MibTableRow
dfl1660IfTxRingEntry = _Dfl1660IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9, 1)
)
dfl1660IfTxRingEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl1660IfTxRingEntry.setStatus("current")


class _Dfl1660IfTxRingIndex_Type(Integer32):
    """Custom type dfl1660IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl1660IfTxRingIndex_Object = MibTableColumn
dfl1660IfTxRingIndex = _Dfl1660IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9, 1, 1),
    _Dfl1660IfTxRingIndex_Type()
)
dfl1660IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660IfTxRingIndex.setStatus("current")
_Dfl1660IfTxDespools_Type = Gauge32
_Dfl1660IfTxDespools_Object = MibTableColumn
dfl1660IfTxDespools = _Dfl1660IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9, 1, 2),
    _Dfl1660IfTxDespools_Type()
)
dfl1660IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfTxDespools.setStatus("current")
_Dfl1660IfTxAvgUse_Type = Gauge32
_Dfl1660IfTxAvgUse_Object = MibTableColumn
dfl1660IfTxAvgUse = _Dfl1660IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9, 1, 3),
    _Dfl1660IfTxAvgUse_Type()
)
dfl1660IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfTxAvgUse.setStatus("current")
_Dfl1660IfTxRingSaturation_Type = Gauge32
_Dfl1660IfTxRingSaturation_Object = MibTableColumn
dfl1660IfTxRingSaturation = _Dfl1660IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9, 1, 4),
    _Dfl1660IfTxRingSaturation_Type()
)
dfl1660IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfTxRingSaturation.setStatus("current")
_Dfl1660RxTingFlooded_Type = Gauge32
_Dfl1660RxTingFlooded_Object = MibTableColumn
dfl1660RxTingFlooded = _Dfl1660RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 9, 1, 5),
    _Dfl1660RxTingFlooded_Type()
)
dfl1660RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660RxTingFlooded.setStatus("current")
_Dfl1660IfVlanStatsTable_Object = MibTable
dfl1660IfVlanStatsTable = _Dfl1660IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl1660IfVlanStatsTable.setStatus("current")
_Dfl1660IfVlanStatsEntry_Object = MibTableRow
dfl1660IfVlanStatsEntry = _Dfl1660IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1)
)
dfl1660IfVlanStatsEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl1660IfVlanStatsEntry.setStatus("current")


class _Dfl1660IfVlanIndex_Type(Integer32):
    """Custom type dfl1660IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660IfVlanIndex_Type.__name__ = "Integer32"
_Dfl1660IfVlanIndex_Object = MibTableColumn
dfl1660IfVlanIndex = _Dfl1660IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 1),
    _Dfl1660IfVlanIndex_Type()
)
dfl1660IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660IfVlanIndex.setStatus("current")
_Dfl1660IfVlanUntaggedInPkts_Type = Counter32
_Dfl1660IfVlanUntaggedInPkts_Object = MibTableColumn
dfl1660IfVlanUntaggedInPkts = _Dfl1660IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 2),
    _Dfl1660IfVlanUntaggedInPkts_Type()
)
dfl1660IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfVlanUntaggedInPkts.setStatus("current")
_Dfl1660IfVlanUntaggedOutPkts_Type = Counter32
_Dfl1660IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl1660IfVlanUntaggedOutPkts = _Dfl1660IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 3),
    _Dfl1660IfVlanUntaggedOutPkts_Type()
)
dfl1660IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfVlanUntaggedOutPkts.setStatus("current")
_Dfl1660IfVlanUntaggedTotPkts_Type = Counter32
_Dfl1660IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl1660IfVlanUntaggedTotPkts = _Dfl1660IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 4),
    _Dfl1660IfVlanUntaggedTotPkts_Type()
)
dfl1660IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfVlanUntaggedTotPkts.setStatus("current")
_Dfl1660IfVlanUntaggedInOctets_Type = Counter32
_Dfl1660IfVlanUntaggedInOctets_Object = MibTableColumn
dfl1660IfVlanUntaggedInOctets = _Dfl1660IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 5),
    _Dfl1660IfVlanUntaggedInOctets_Type()
)
dfl1660IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfVlanUntaggedInOctets.setStatus("current")
_Dfl1660IfVlanUntaggedOutOctets_Type = Counter32
_Dfl1660IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl1660IfVlanUntaggedOutOctets = _Dfl1660IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 6),
    _Dfl1660IfVlanUntaggedOutOctets_Type()
)
dfl1660IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfVlanUntaggedOutOctets.setStatus("current")
_Dfl1660IfVlanUntaggedTotOctets_Type = Counter32
_Dfl1660IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl1660IfVlanUntaggedTotOctets = _Dfl1660IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 10, 1, 7),
    _Dfl1660IfVlanUntaggedTotOctets_Type()
)
dfl1660IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IfVlanUntaggedTotOctets.setStatus("current")
_Dfl1660HWSensorTable_Object = MibTable
dfl1660HWSensorTable = _Dfl1660HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl1660HWSensorTable.setStatus("current")
_Dfl1660HWSensorEntry_Object = MibTableRow
dfl1660HWSensorEntry = _Dfl1660HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 11, 1)
)
dfl1660HWSensorEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl1660HWSensorEntry.setStatus("current")


class _Dfl1660HWSensorIndex_Type(Integer32):
    """Custom type dfl1660HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660HWSensorIndex_Type.__name__ = "Integer32"
_Dfl1660HWSensorIndex_Object = MibTableColumn
dfl1660HWSensorIndex = _Dfl1660HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 11, 1, 1),
    _Dfl1660HWSensorIndex_Type()
)
dfl1660HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660HWSensorIndex.setStatus("current")
_Dfl1660HWSensorName_Type = DisplayString
_Dfl1660HWSensorName_Object = MibTableColumn
dfl1660HWSensorName = _Dfl1660HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 11, 1, 2),
    _Dfl1660HWSensorName_Type()
)
dfl1660HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HWSensorName.setStatus("current")
_Dfl1660HWSensorValue_Type = Gauge32
_Dfl1660HWSensorValue_Object = MibTableColumn
dfl1660HWSensorValue = _Dfl1660HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 11, 1, 3),
    _Dfl1660HWSensorValue_Type()
)
dfl1660HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HWSensorValue.setStatus("current")
_Dfl1660HWSensorUnit_Type = DisplayString
_Dfl1660HWSensorUnit_Object = MibTableColumn
dfl1660HWSensorUnit = _Dfl1660HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 11, 1, 4),
    _Dfl1660HWSensorUnit_Type()
)
dfl1660HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HWSensorUnit.setStatus("current")
_Dfl1660SysMemUsage_Type = Gauge32
_Dfl1660SysMemUsage_Object = MibScalar
dfl1660SysMemUsage = _Dfl1660SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 12),
    _Dfl1660SysMemUsage_Type()
)
dfl1660SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysMemUsage.setStatus("current")
_Dfl1660SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl1660SysTCPUsage = _Dfl1660SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 13)
)
_Dfl1660SysTCPRecvSmall_Type = Gauge32
_Dfl1660SysTCPRecvSmall_Object = MibScalar
dfl1660SysTCPRecvSmall = _Dfl1660SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 13, 1),
    _Dfl1660SysTCPRecvSmall_Type()
)
dfl1660SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysTCPRecvSmall.setStatus("current")
_Dfl1660SysTCPRecvLarge_Type = Gauge32
_Dfl1660SysTCPRecvLarge_Object = MibScalar
dfl1660SysTCPRecvLarge = _Dfl1660SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 13, 2),
    _Dfl1660SysTCPRecvLarge_Type()
)
dfl1660SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysTCPRecvLarge.setStatus("current")
_Dfl1660SysTCPSendSmall_Type = Gauge32
_Dfl1660SysTCPSendSmall_Object = MibScalar
dfl1660SysTCPSendSmall = _Dfl1660SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 13, 3),
    _Dfl1660SysTCPSendSmall_Type()
)
dfl1660SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysTCPSendSmall.setStatus("current")
_Dfl1660SysTCPSendLarge_Type = Gauge32
_Dfl1660SysTCPSendLarge_Object = MibScalar
dfl1660SysTCPSendLarge = _Dfl1660SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 13, 4),
    _Dfl1660SysTCPSendLarge_Type()
)
dfl1660SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysTCPSendLarge.setStatus("current")
_Dfl1660SysTimerUsage_Type = Gauge32
_Dfl1660SysTimerUsage_Object = MibScalar
dfl1660SysTimerUsage = _Dfl1660SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 14),
    _Dfl1660SysTimerUsage_Type()
)
dfl1660SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysTimerUsage.setStatus("current")
_Dfl1660SysConnOPS_Type = Gauge32
_Dfl1660SysConnOPS_Object = MibScalar
dfl1660SysConnOPS = _Dfl1660SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 15),
    _Dfl1660SysConnOPS_Type()
)
dfl1660SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysConnOPS.setStatus("current")
_Dfl1660SysConnCPS_Type = Gauge32
_Dfl1660SysConnCPS_Object = MibScalar
dfl1660SysConnCPS = _Dfl1660SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 16),
    _Dfl1660SysConnCPS_Type()
)
dfl1660SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysConnCPS.setStatus("current")
_Dfl1660SysHCForwardedBits_Type = Counter64
_Dfl1660SysHCForwardedBits_Object = MibScalar
dfl1660SysHCForwardedBits = _Dfl1660SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 1, 17),
    _Dfl1660SysHCForwardedBits_Type()
)
dfl1660SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SysHCForwardedBits.setStatus("current")
_Dfl1660VPN_ObjectIdentity = ObjectIdentity
dfl1660VPN = _Dfl1660VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2)
)
_Dfl1660IPsec_ObjectIdentity = ObjectIdentity
dfl1660IPsec = _Dfl1660IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1)
)
_Dfl1660IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl1660IPsecGlobal = _Dfl1660IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1)
)
_Dfl1660IPsecPhaseOneActive_Type = Gauge32
_Dfl1660IPsecPhaseOneActive_Object = MibScalar
dfl1660IPsecPhaseOneActive = _Dfl1660IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 1),
    _Dfl1660IPsecPhaseOneActive_Type()
)
dfl1660IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecPhaseOneActive.setStatus("current")
_Dfl1660IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl1660IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl1660IPsecPhaseOneAggrModeDone = _Dfl1660IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 2),
    _Dfl1660IPsecPhaseOneAggrModeDone_Type()
)
dfl1660IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl1660IPsecQuickModeActive_Type = Gauge32
_Dfl1660IPsecQuickModeActive_Object = MibScalar
dfl1660IPsecQuickModeActive = _Dfl1660IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 3),
    _Dfl1660IPsecQuickModeActive_Type()
)
dfl1660IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecQuickModeActive.setStatus("current")
_Dfl1660IPsecPhaseOneDone_Type = Counter32
_Dfl1660IPsecPhaseOneDone_Object = MibScalar
dfl1660IPsecPhaseOneDone = _Dfl1660IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 4),
    _Dfl1660IPsecPhaseOneDone_Type()
)
dfl1660IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecPhaseOneDone.setStatus("current")
_Dfl1660IPsecPhaseOneFailed_Type = Counter32
_Dfl1660IPsecPhaseOneFailed_Object = MibScalar
dfl1660IPsecPhaseOneFailed = _Dfl1660IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 5),
    _Dfl1660IPsecPhaseOneFailed_Type()
)
dfl1660IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecPhaseOneFailed.setStatus("current")
_Dfl1660IPsecPhaseOneRekeyed_Type = Counter32
_Dfl1660IPsecPhaseOneRekeyed_Object = MibScalar
dfl1660IPsecPhaseOneRekeyed = _Dfl1660IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 6),
    _Dfl1660IPsecPhaseOneRekeyed_Type()
)
dfl1660IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecPhaseOneRekeyed.setStatus("current")
_Dfl1660IPsecQuickModeDone_Type = Counter32
_Dfl1660IPsecQuickModeDone_Object = MibScalar
dfl1660IPsecQuickModeDone = _Dfl1660IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 7),
    _Dfl1660IPsecQuickModeDone_Type()
)
dfl1660IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecQuickModeDone.setStatus("current")
_Dfl1660IPsecQuickModeFailed_Type = Counter32
_Dfl1660IPsecQuickModeFailed_Object = MibScalar
dfl1660IPsecQuickModeFailed = _Dfl1660IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 8),
    _Dfl1660IPsecQuickModeFailed_Type()
)
dfl1660IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecQuickModeFailed.setStatus("current")
_Dfl1660IPsecInfoDone_Type = Counter32
_Dfl1660IPsecInfoDone_Object = MibScalar
dfl1660IPsecInfoDone = _Dfl1660IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 9),
    _Dfl1660IPsecInfoDone_Type()
)
dfl1660IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecInfoDone.setStatus("current")
_Dfl1660IPsecInfoFailed_Type = Counter32
_Dfl1660IPsecInfoFailed_Object = MibScalar
dfl1660IPsecInfoFailed = _Dfl1660IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 10),
    _Dfl1660IPsecInfoFailed_Type()
)
dfl1660IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecInfoFailed.setStatus("current")
_Dfl1660IPsecInOctetsComp_Type = Counter64
_Dfl1660IPsecInOctetsComp_Object = MibScalar
dfl1660IPsecInOctetsComp = _Dfl1660IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 11),
    _Dfl1660IPsecInOctetsComp_Type()
)
dfl1660IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecInOctetsComp.setStatus("current")
_Dfl1660IPsecInOctetsUncomp_Type = Counter64
_Dfl1660IPsecInOctetsUncomp_Object = MibScalar
dfl1660IPsecInOctetsUncomp = _Dfl1660IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 12),
    _Dfl1660IPsecInOctetsUncomp_Type()
)
dfl1660IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecInOctetsUncomp.setStatus("current")
_Dfl1660IPsecOutOctetsComp_Type = Counter64
_Dfl1660IPsecOutOctetsComp_Object = MibScalar
dfl1660IPsecOutOctetsComp = _Dfl1660IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 13),
    _Dfl1660IPsecOutOctetsComp_Type()
)
dfl1660IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecOutOctetsComp.setStatus("current")
_Dfl1660IPsecOutOctetsUncomp_Type = Counter64
_Dfl1660IPsecOutOctetsUncomp_Object = MibScalar
dfl1660IPsecOutOctetsUncomp = _Dfl1660IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 14),
    _Dfl1660IPsecOutOctetsUncomp_Type()
)
dfl1660IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecOutOctetsUncomp.setStatus("current")
_Dfl1660IPsecForwardedOctetsComp_Type = Counter64
_Dfl1660IPsecForwardedOctetsComp_Object = MibScalar
dfl1660IPsecForwardedOctetsComp = _Dfl1660IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 15),
    _Dfl1660IPsecForwardedOctetsComp_Type()
)
dfl1660IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecForwardedOctetsComp.setStatus("current")
_Dfl1660IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl1660IPsecForwardedOctetsUcomp_Object = MibScalar
dfl1660IPsecForwardedOctetsUcomp = _Dfl1660IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 16),
    _Dfl1660IPsecForwardedOctetsUcomp_Type()
)
dfl1660IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl1660IPsecInPackets_Type = Counter64
_Dfl1660IPsecInPackets_Object = MibScalar
dfl1660IPsecInPackets = _Dfl1660IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 17),
    _Dfl1660IPsecInPackets_Type()
)
dfl1660IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecInPackets.setStatus("current")
_Dfl1660IPsecOutPackets_Type = Counter64
_Dfl1660IPsecOutPackets_Object = MibScalar
dfl1660IPsecOutPackets = _Dfl1660IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 18),
    _Dfl1660IPsecOutPackets_Type()
)
dfl1660IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecOutPackets.setStatus("current")
_Dfl1660IPsecForwardedPackets_Type = Counter64
_Dfl1660IPsecForwardedPackets_Object = MibScalar
dfl1660IPsecForwardedPackets = _Dfl1660IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 19),
    _Dfl1660IPsecForwardedPackets_Type()
)
dfl1660IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecForwardedPackets.setStatus("current")
_Dfl1660IPsecActiveTransforms_Type = Gauge32
_Dfl1660IPsecActiveTransforms_Object = MibScalar
dfl1660IPsecActiveTransforms = _Dfl1660IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 20),
    _Dfl1660IPsecActiveTransforms_Type()
)
dfl1660IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecActiveTransforms.setStatus("current")
_Dfl1660IPsecTotalTransforms_Type = Counter32
_Dfl1660IPsecTotalTransforms_Object = MibScalar
dfl1660IPsecTotalTransforms = _Dfl1660IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 21),
    _Dfl1660IPsecTotalTransforms_Type()
)
dfl1660IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecTotalTransforms.setStatus("current")
_Dfl1660IPsecOutOfTransforms_Type = Counter32
_Dfl1660IPsecOutOfTransforms_Object = MibScalar
dfl1660IPsecOutOfTransforms = _Dfl1660IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 22),
    _Dfl1660IPsecOutOfTransforms_Type()
)
dfl1660IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecOutOfTransforms.setStatus("current")
_Dfl1660IPsecTotalRekeys_Type = Counter32
_Dfl1660IPsecTotalRekeys_Object = MibScalar
dfl1660IPsecTotalRekeys = _Dfl1660IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 2, 1, 1, 23),
    _Dfl1660IPsecTotalRekeys_Type()
)
dfl1660IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPsecTotalRekeys.setStatus("current")
_Dfl1660Rules_ObjectIdentity = ObjectIdentity
dfl1660Rules = _Dfl1660Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 3)
)
_Dfl1660RuleUseTable_Object = MibTable
dfl1660RuleUseTable = _Dfl1660RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl1660RuleUseTable.setStatus("current")
_Dfl1660RuleUseEntry_Object = MibTableRow
dfl1660RuleUseEntry = _Dfl1660RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 3, 2, 1)
)
dfl1660RuleUseEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl1660RuleUseEntry.setStatus("current")


class _Dfl1660RuleIndex_Type(Integer32):
    """Custom type dfl1660RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660RuleIndex_Type.__name__ = "Integer32"
_Dfl1660RuleIndex_Object = MibTableColumn
dfl1660RuleIndex = _Dfl1660RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 3, 2, 1, 1),
    _Dfl1660RuleIndex_Type()
)
dfl1660RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660RuleIndex.setStatus("current")
_Dfl1660RuleName_Type = DisplayString
_Dfl1660RuleName_Object = MibTableColumn
dfl1660RuleName = _Dfl1660RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 3, 2, 1, 2),
    _Dfl1660RuleName_Type()
)
dfl1660RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660RuleName.setStatus("current")
_Dfl1660RuleUse_Type = Counter32
_Dfl1660RuleUse_Object = MibTableColumn
dfl1660RuleUse = _Dfl1660RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 3, 2, 1, 3),
    _Dfl1660RuleUse_Type()
)
dfl1660RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660RuleUse.setStatus("current")
_Dfl1660IPPools_ObjectIdentity = ObjectIdentity
dfl1660IPPools = _Dfl1660IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4)
)
_Dfl1660IPPoolsNumber_Type = Integer32
_Dfl1660IPPoolsNumber_Object = MibScalar
dfl1660IPPoolsNumber = _Dfl1660IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 1),
    _Dfl1660IPPoolsNumber_Type()
)
dfl1660IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolsNumber.setStatus("current")
_Dfl1660IPPoolTable_Object = MibTable
dfl1660IPPoolTable = _Dfl1660IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl1660IPPoolTable.setStatus("current")
_Dfl1660IPPoolEntry_Object = MibTableRow
dfl1660IPPoolEntry = _Dfl1660IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1)
)
dfl1660IPPoolEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl1660IPPoolEntry.setStatus("current")


class _Dfl1660IPPoolIndex_Type(Integer32):
    """Custom type dfl1660IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660IPPoolIndex_Type.__name__ = "Integer32"
_Dfl1660IPPoolIndex_Object = MibTableColumn
dfl1660IPPoolIndex = _Dfl1660IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 1),
    _Dfl1660IPPoolIndex_Type()
)
dfl1660IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660IPPoolIndex.setStatus("current")
_Dfl1660IPPoolName_Type = DisplayString
_Dfl1660IPPoolName_Object = MibTableColumn
dfl1660IPPoolName = _Dfl1660IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 2),
    _Dfl1660IPPoolName_Type()
)
dfl1660IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolName.setStatus("current")
_Dfl1660IPPoolPrepare_Type = Gauge32
_Dfl1660IPPoolPrepare_Object = MibTableColumn
dfl1660IPPoolPrepare = _Dfl1660IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 3),
    _Dfl1660IPPoolPrepare_Type()
)
dfl1660IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolPrepare.setStatus("current")
_Dfl1660IPPoolFree_Type = Gauge32
_Dfl1660IPPoolFree_Object = MibTableColumn
dfl1660IPPoolFree = _Dfl1660IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 4),
    _Dfl1660IPPoolFree_Type()
)
dfl1660IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolFree.setStatus("current")
_Dfl1660IPPoolMisses_Type = Gauge32
_Dfl1660IPPoolMisses_Object = MibTableColumn
dfl1660IPPoolMisses = _Dfl1660IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 5),
    _Dfl1660IPPoolMisses_Type()
)
dfl1660IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolMisses.setStatus("current")
_Dfl1660IPPoolClientFails_Type = Gauge32
_Dfl1660IPPoolClientFails_Object = MibTableColumn
dfl1660IPPoolClientFails = _Dfl1660IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 6),
    _Dfl1660IPPoolClientFails_Type()
)
dfl1660IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolClientFails.setStatus("current")
_Dfl1660IPPoolUsed_Type = Gauge32
_Dfl1660IPPoolUsed_Object = MibTableColumn
dfl1660IPPoolUsed = _Dfl1660IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 4, 2, 1, 7),
    _Dfl1660IPPoolUsed_Type()
)
dfl1660IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660IPPoolUsed.setStatus("current")
_Dfl1660DHCPServer_ObjectIdentity = ObjectIdentity
dfl1660DHCPServer = _Dfl1660DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5)
)
_Dfl1660DHCPTotalRejected_Type = Gauge32
_Dfl1660DHCPTotalRejected_Object = MibScalar
dfl1660DHCPTotalRejected = _Dfl1660DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 1),
    _Dfl1660DHCPTotalRejected_Type()
)
dfl1660DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPTotalRejected.setStatus("current")
_Dfl1660DHCPRuleTable_Object = MibTable
dfl1660DHCPRuleTable = _Dfl1660DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl1660DHCPRuleTable.setStatus("current")
_Dfl1660DHCPRuleEntry_Object = MibTableRow
dfl1660DHCPRuleEntry = _Dfl1660DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1)
)
dfl1660DHCPRuleEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl1660DHCPRuleEntry.setStatus("current")


class _Dfl1660DHCPRuleIndex_Type(Integer32):
    """Custom type dfl1660DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl1660DHCPRuleIndex_Object = MibTableColumn
dfl1660DHCPRuleIndex = _Dfl1660DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 1),
    _Dfl1660DHCPRuleIndex_Type()
)
dfl1660DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660DHCPRuleIndex.setStatus("current")
_Dfl1660DHCPRuleName_Type = DisplayString
_Dfl1660DHCPRuleName_Object = MibTableColumn
dfl1660DHCPRuleName = _Dfl1660DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 2),
    _Dfl1660DHCPRuleName_Type()
)
dfl1660DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRuleName.setStatus("current")
_Dfl1660DHCPRuleUsage_Type = Gauge32
_Dfl1660DHCPRuleUsage_Object = MibTableColumn
dfl1660DHCPRuleUsage = _Dfl1660DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 3),
    _Dfl1660DHCPRuleUsage_Type()
)
dfl1660DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRuleUsage.setStatus("current")
_Dfl1660DHCPRuleUsagePercent_Type = Gauge32
_Dfl1660DHCPRuleUsagePercent_Object = MibTableColumn
dfl1660DHCPRuleUsagePercent = _Dfl1660DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 4),
    _Dfl1660DHCPRuleUsagePercent_Type()
)
dfl1660DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRuleUsagePercent.setStatus("current")
_Dfl1660DHCPActiveClients_Type = Gauge32
_Dfl1660DHCPActiveClients_Object = MibTableColumn
dfl1660DHCPActiveClients = _Dfl1660DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 5),
    _Dfl1660DHCPActiveClients_Type()
)
dfl1660DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPActiveClients.setStatus("current")
_Dfl1660DHCPActiveClientsPercent_Type = Gauge32
_Dfl1660DHCPActiveClientsPercent_Object = MibTableColumn
dfl1660DHCPActiveClientsPercent = _Dfl1660DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 6),
    _Dfl1660DHCPActiveClientsPercent_Type()
)
dfl1660DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPActiveClientsPercent.setStatus("current")
_Dfl1660DHCPRejectedRequests_Type = Gauge32
_Dfl1660DHCPRejectedRequests_Object = MibTableColumn
dfl1660DHCPRejectedRequests = _Dfl1660DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 7),
    _Dfl1660DHCPRejectedRequests_Type()
)
dfl1660DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRejectedRequests.setStatus("current")
_Dfl1660DHCPTotalLeases_Type = Gauge32
_Dfl1660DHCPTotalLeases_Object = MibTableColumn
dfl1660DHCPTotalLeases = _Dfl1660DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 5, 2, 1, 8),
    _Dfl1660DHCPTotalLeases_Type()
)
dfl1660DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPTotalLeases.setStatus("current")
_Dfl1660UserAuth_ObjectIdentity = ObjectIdentity
dfl1660UserAuth = _Dfl1660UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6)
)
_Dfl1660UserAuthHTTPUsers_Type = Gauge32
_Dfl1660UserAuthHTTPUsers_Object = MibScalar
dfl1660UserAuthHTTPUsers = _Dfl1660UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 1),
    _Dfl1660UserAuthHTTPUsers_Type()
)
dfl1660UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthHTTPUsers.setStatus("current")
_Dfl1660UserAuthXAUTHUsers_Type = Gauge32
_Dfl1660UserAuthXAUTHUsers_Object = MibScalar
dfl1660UserAuthXAUTHUsers = _Dfl1660UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 2),
    _Dfl1660UserAuthXAUTHUsers_Type()
)
dfl1660UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthXAUTHUsers.setStatus("current")
_Dfl1660UserAuthHTTPSUsers_Type = Gauge32
_Dfl1660UserAuthHTTPSUsers_Object = MibScalar
dfl1660UserAuthHTTPSUsers = _Dfl1660UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 3),
    _Dfl1660UserAuthHTTPSUsers_Type()
)
dfl1660UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthHTTPSUsers.setStatus("current")
_Dfl1660UserAuthPPPUsers_Type = Gauge32
_Dfl1660UserAuthPPPUsers_Object = MibScalar
dfl1660UserAuthPPPUsers = _Dfl1660UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 4),
    _Dfl1660UserAuthPPPUsers_Type()
)
dfl1660UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthPPPUsers.setStatus("current")
_Dfl1660UserAuthEAPUsers_Type = Gauge32
_Dfl1660UserAuthEAPUsers_Object = MibScalar
dfl1660UserAuthEAPUsers = _Dfl1660UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 5),
    _Dfl1660UserAuthEAPUsers_Type()
)
dfl1660UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthEAPUsers.setStatus("current")
_Dfl1660UserAuthRuleUseTable_Object = MibTable
dfl1660UserAuthRuleUseTable = _Dfl1660UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl1660UserAuthRuleUseTable.setStatus("current")
_Dfl1660UserAuthRuleUseEntry_Object = MibTableRow
dfl1660UserAuthRuleUseEntry = _Dfl1660UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 6, 1)
)
dfl1660UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl1660UserAuthRuleUseEntry.setStatus("current")


class _Dfl1660UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl1660UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl1660UserAuthRuleIndex_Object = MibTableColumn
dfl1660UserAuthRuleIndex = _Dfl1660UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 6, 1, 1),
    _Dfl1660UserAuthRuleIndex_Type()
)
dfl1660UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660UserAuthRuleIndex.setStatus("current")
_Dfl1660UserAuthRuleName_Type = DisplayString
_Dfl1660UserAuthRuleName_Object = MibTableColumn
dfl1660UserAuthRuleName = _Dfl1660UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 6, 1, 2),
    _Dfl1660UserAuthRuleName_Type()
)
dfl1660UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthRuleName.setStatus("current")
_Dfl1660UserAuthRuleUse_Type = Counter32
_Dfl1660UserAuthRuleUse_Object = MibTableColumn
dfl1660UserAuthRuleUse = _Dfl1660UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 6, 6, 1, 3),
    _Dfl1660UserAuthRuleUse_Type()
)
dfl1660UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660UserAuthRuleUse.setStatus("current")
_Dfl1660LinkMonitor_ObjectIdentity = ObjectIdentity
dfl1660LinkMonitor = _Dfl1660LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7)
)
_Dfl1660LinkMonGrp_Type = Integer32
_Dfl1660LinkMonGrp_Object = MibScalar
dfl1660LinkMonGrp = _Dfl1660LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 1),
    _Dfl1660LinkMonGrp_Type()
)
dfl1660LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660LinkMonGrp.setStatus("current")
_Dfl1660LinkMonGrpTable_Object = MibTable
dfl1660LinkMonGrpTable = _Dfl1660LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl1660LinkMonGrpTable.setStatus("current")
_Dfl1660LinkMonGrpEntry_Object = MibTableRow
dfl1660LinkMonGrpEntry = _Dfl1660LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 2, 1)
)
dfl1660LinkMonGrpEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl1660LinkMonGrpEntry.setStatus("current")


class _Dfl1660LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl1660LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl1660LinkMonGrpIndex_Object = MibTableColumn
dfl1660LinkMonGrpIndex = _Dfl1660LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 2, 1, 1),
    _Dfl1660LinkMonGrpIndex_Type()
)
dfl1660LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660LinkMonGrpIndex.setStatus("current")
_Dfl1660LinkMonGrpName_Type = DisplayString
_Dfl1660LinkMonGrpName_Object = MibTableColumn
dfl1660LinkMonGrpName = _Dfl1660LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 2, 1, 2),
    _Dfl1660LinkMonGrpName_Type()
)
dfl1660LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660LinkMonGrpName.setStatus("current")
_Dfl1660LinkMonGrpHostsUp_Type = Gauge32
_Dfl1660LinkMonGrpHostsUp_Object = MibTableColumn
dfl1660LinkMonGrpHostsUp = _Dfl1660LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 2, 1, 3),
    _Dfl1660LinkMonGrpHostsUp_Type()
)
dfl1660LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660LinkMonGrpHostsUp.setStatus("current")
_Dfl1660LinkMonHostTable_Object = MibTable
dfl1660LinkMonHostTable = _Dfl1660LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl1660LinkMonHostTable.setStatus("current")
_Dfl1660LinkMonHostEntry_Object = MibTableRow
dfl1660LinkMonHostEntry = _Dfl1660LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 3, 1)
)
dfl1660LinkMonHostEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660LinkMonGrpIndex"),
    (0, "DFL1660-MIB", "dfl1660LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl1660LinkMonHostEntry.setStatus("current")


class _Dfl1660LinkMonHostIndex_Type(Integer32):
    """Custom type dfl1660LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl1660LinkMonHostIndex_Object = MibTableColumn
dfl1660LinkMonHostIndex = _Dfl1660LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 3, 1, 1),
    _Dfl1660LinkMonHostIndex_Type()
)
dfl1660LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660LinkMonHostIndex.setStatus("current")
_Dfl1660LinkMonHostId_Type = DisplayString
_Dfl1660LinkMonHostId_Object = MibTableColumn
dfl1660LinkMonHostId = _Dfl1660LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 3, 1, 2),
    _Dfl1660LinkMonHostId_Type()
)
dfl1660LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660LinkMonHostId.setStatus("current")
_Dfl1660LinkMonHostShortTermLoss_Type = Gauge32
_Dfl1660LinkMonHostShortTermLoss_Object = MibTableColumn
dfl1660LinkMonHostShortTermLoss = _Dfl1660LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 3, 1, 3),
    _Dfl1660LinkMonHostShortTermLoss_Type()
)
dfl1660LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660LinkMonHostShortTermLoss.setStatus("current")
_Dfl1660LinkMonHostPacketsLost_Type = Counter32
_Dfl1660LinkMonHostPacketsLost_Object = MibTableColumn
dfl1660LinkMonHostPacketsLost = _Dfl1660LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 7, 3, 1, 4),
    _Dfl1660LinkMonHostPacketsLost_Type()
)
dfl1660LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660LinkMonHostPacketsLost.setStatus("current")
_Dfl1660Pipes_ObjectIdentity = ObjectIdentity
dfl1660Pipes = _Dfl1660Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8)
)
_Dfl1660PipeUsers_Type = Gauge32
_Dfl1660PipeUsers_Object = MibScalar
dfl1660PipeUsers = _Dfl1660PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 1),
    _Dfl1660PipeUsers_Type()
)
dfl1660PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeUsers.setStatus("current")
_Dfl1660PipeTable_Object = MibTable
dfl1660PipeTable = _Dfl1660PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl1660PipeTable.setStatus("current")
_Dfl1660PipeEntry_Object = MibTableRow
dfl1660PipeEntry = _Dfl1660PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1)
)
dfl1660PipeEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl1660PipeEntry.setStatus("current")


class _Dfl1660PipeIndex_Type(Integer32):
    """Custom type dfl1660PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660PipeIndex_Type.__name__ = "Integer32"
_Dfl1660PipeIndex_Object = MibTableColumn
dfl1660PipeIndex = _Dfl1660PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 1),
    _Dfl1660PipeIndex_Type()
)
dfl1660PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660PipeIndex.setStatus("current")
_Dfl1660PipeName_Type = DisplayString
_Dfl1660PipeName_Object = MibTableColumn
dfl1660PipeName = _Dfl1660PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 2),
    _Dfl1660PipeName_Type()
)
dfl1660PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeName.setStatus("current")
_Dfl1660PipeMinPrec_Type = Integer32
_Dfl1660PipeMinPrec_Object = MibTableColumn
dfl1660PipeMinPrec = _Dfl1660PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 3),
    _Dfl1660PipeMinPrec_Type()
)
dfl1660PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeMinPrec.setStatus("current")
_Dfl1660PipeMaxPrec_Type = Integer32
_Dfl1660PipeMaxPrec_Object = MibTableColumn
dfl1660PipeMaxPrec = _Dfl1660PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 4),
    _Dfl1660PipeMaxPrec_Type()
)
dfl1660PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeMaxPrec.setStatus("current")
_Dfl1660PipeDefPrec_Type = Integer32
_Dfl1660PipeDefPrec_Object = MibTableColumn
dfl1660PipeDefPrec = _Dfl1660PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 5),
    _Dfl1660PipeDefPrec_Type()
)
dfl1660PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeDefPrec.setStatus("current")
_Dfl1660PipeNumPrec_Type = Integer32
_Dfl1660PipeNumPrec_Object = MibTableColumn
dfl1660PipeNumPrec = _Dfl1660PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 6),
    _Dfl1660PipeNumPrec_Type()
)
dfl1660PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeNumPrec.setStatus("current")
_Dfl1660PipeNumUsers_Type = Gauge32
_Dfl1660PipeNumUsers_Object = MibTableColumn
dfl1660PipeNumUsers = _Dfl1660PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 7),
    _Dfl1660PipeNumUsers_Type()
)
dfl1660PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeNumUsers.setStatus("current")
_Dfl1660PipeCurrentBps_Type = Gauge32
_Dfl1660PipeCurrentBps_Object = MibTableColumn
dfl1660PipeCurrentBps = _Dfl1660PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 8),
    _Dfl1660PipeCurrentBps_Type()
)
dfl1660PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeCurrentBps.setStatus("current")
_Dfl1660PipeCurrentPps_Type = Gauge32
_Dfl1660PipeCurrentPps_Object = MibTableColumn
dfl1660PipeCurrentPps = _Dfl1660PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 9),
    _Dfl1660PipeCurrentPps_Type()
)
dfl1660PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeCurrentPps.setStatus("current")
_Dfl1660PipeDelayedPackets_Type = Counter32
_Dfl1660PipeDelayedPackets_Object = MibTableColumn
dfl1660PipeDelayedPackets = _Dfl1660PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 10),
    _Dfl1660PipeDelayedPackets_Type()
)
dfl1660PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeDelayedPackets.setStatus("current")
_Dfl1660PipeDropedPackets_Type = Counter32
_Dfl1660PipeDropedPackets_Object = MibTableColumn
dfl1660PipeDropedPackets = _Dfl1660PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 2, 1, 11),
    _Dfl1660PipeDropedPackets_Type()
)
dfl1660PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipeDropedPackets.setStatus("current")
_Dfl1660PipePrecTable_Object = MibTable
dfl1660PipePrecTable = _Dfl1660PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl1660PipePrecTable.setStatus("current")
_Dfl1660PipePrecEntry_Object = MibTableRow
dfl1660PipePrecEntry = _Dfl1660PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1)
)
dfl1660PipePrecEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660PipeIndex"),
    (0, "DFL1660-MIB", "dfl1660PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl1660PipePrecEntry.setStatus("current")


class _Dfl1660PipePrecIndex_Type(Integer32):
    """Custom type dfl1660PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660PipePrecIndex_Type.__name__ = "Integer32"
_Dfl1660PipePrecIndex_Object = MibTableColumn
dfl1660PipePrecIndex = _Dfl1660PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 1),
    _Dfl1660PipePrecIndex_Type()
)
dfl1660PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660PipePrecIndex.setStatus("current")
_Dfl1660PipePrec_Type = Integer32
_Dfl1660PipePrec_Object = MibTableColumn
dfl1660PipePrec = _Dfl1660PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 2),
    _Dfl1660PipePrec_Type()
)
dfl1660PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrec.setStatus("current")
_Dfl1660PipePrecBps_Type = Gauge32
_Dfl1660PipePrecBps_Object = MibTableColumn
dfl1660PipePrecBps = _Dfl1660PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 3),
    _Dfl1660PipePrecBps_Type()
)
dfl1660PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecBps.setStatus("current")
_Dfl1660PipePrecTotalPps_Type = Gauge32
_Dfl1660PipePrecTotalPps_Object = MibTableColumn
dfl1660PipePrecTotalPps = _Dfl1660PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 4),
    _Dfl1660PipePrecTotalPps_Type()
)
dfl1660PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecTotalPps.setStatus("current")
_Dfl1660PipePrecReservedBps_Type = Gauge32
_Dfl1660PipePrecReservedBps_Object = MibTableColumn
dfl1660PipePrecReservedBps = _Dfl1660PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 5),
    _Dfl1660PipePrecReservedBps_Type()
)
dfl1660PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecReservedBps.setStatus("current")
_Dfl1660PipePrecDynLimBps_Type = Gauge32
_Dfl1660PipePrecDynLimBps_Object = MibTableColumn
dfl1660PipePrecDynLimBps = _Dfl1660PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 6),
    _Dfl1660PipePrecDynLimBps_Type()
)
dfl1660PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecDynLimBps.setStatus("current")
_Dfl1660PipePrecDynUsrLimBps_Type = Gauge32
_Dfl1660PipePrecDynUsrLimBps_Object = MibTableColumn
dfl1660PipePrecDynUsrLimBps = _Dfl1660PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 7),
    _Dfl1660PipePrecDynUsrLimBps_Type()
)
dfl1660PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecDynUsrLimBps.setStatus("current")
_Dfl1660PipePrecDelayedPackets_Type = Counter32
_Dfl1660PipePrecDelayedPackets_Object = MibTableColumn
dfl1660PipePrecDelayedPackets = _Dfl1660PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 8),
    _Dfl1660PipePrecDelayedPackets_Type()
)
dfl1660PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecDelayedPackets.setStatus("current")
_Dfl1660PipePrecDropedPackets_Type = Counter32
_Dfl1660PipePrecDropedPackets_Object = MibTableColumn
dfl1660PipePrecDropedPackets = _Dfl1660PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 8, 3, 1, 9),
    _Dfl1660PipePrecDropedPackets_Type()
)
dfl1660PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660PipePrecDropedPackets.setStatus("current")
_Dfl1660ALG_ObjectIdentity = ObjectIdentity
dfl1660ALG = _Dfl1660ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9)
)
_Dfl1660AlgSessions_Type = Gauge32
_Dfl1660AlgSessions_Object = MibScalar
dfl1660AlgSessions = _Dfl1660AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 1),
    _Dfl1660AlgSessions_Type()
)
dfl1660AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660AlgSessions.setStatus("current")
_Dfl1660AlgConnections_Type = Gauge32
_Dfl1660AlgConnections_Object = MibScalar
dfl1660AlgConnections = _Dfl1660AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 2),
    _Dfl1660AlgConnections_Type()
)
dfl1660AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660AlgConnections.setStatus("current")
_Dfl1660AlgTCPStreams_Type = Gauge32
_Dfl1660AlgTCPStreams_Object = MibScalar
dfl1660AlgTCPStreams = _Dfl1660AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 3),
    _Dfl1660AlgTCPStreams_Type()
)
dfl1660AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660AlgTCPStreams.setStatus("current")
_Dfl1660HttpAlg_ObjectIdentity = ObjectIdentity
dfl1660HttpAlg = _Dfl1660HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4)
)
_Dfl1660HttpAlgTable_Object = MibTable
dfl1660HttpAlgTable = _Dfl1660HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl1660HttpAlgTable.setStatus("current")
_Dfl1660HttpAlgEntry_Object = MibTableRow
dfl1660HttpAlgEntry = _Dfl1660HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1, 1)
)
dfl1660HttpAlgEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl1660HttpAlgEntry.setStatus("current")


class _Dfl1660HttpAlgIndex_Type(Integer32):
    """Custom type dfl1660HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl1660HttpAlgIndex_Object = MibTableColumn
dfl1660HttpAlgIndex = _Dfl1660HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1, 1, 1),
    _Dfl1660HttpAlgIndex_Type()
)
dfl1660HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660HttpAlgIndex.setStatus("current")
_Dfl1660HttpAlgName_Type = DisplayString
_Dfl1660HttpAlgName_Object = MibTableColumn
dfl1660HttpAlgName = _Dfl1660HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1, 1, 2),
    _Dfl1660HttpAlgName_Type()
)
dfl1660HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgName.setStatus("current")
_Dfl1660HttpAlgTotalRequested_Type = Gauge32
_Dfl1660HttpAlgTotalRequested_Object = MibTableColumn
dfl1660HttpAlgTotalRequested = _Dfl1660HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1, 1, 3),
    _Dfl1660HttpAlgTotalRequested_Type()
)
dfl1660HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgTotalRequested.setStatus("current")
_Dfl1660HttpAlgTotalAllowed_Type = Gauge32
_Dfl1660HttpAlgTotalAllowed_Object = MibTableColumn
dfl1660HttpAlgTotalAllowed = _Dfl1660HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1, 1, 4),
    _Dfl1660HttpAlgTotalAllowed_Type()
)
dfl1660HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgTotalAllowed.setStatus("current")
_Dfl1660HttpAlgTotalBlocked_Type = Gauge32
_Dfl1660HttpAlgTotalBlocked_Object = MibTableColumn
dfl1660HttpAlgTotalBlocked = _Dfl1660HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 1, 1, 5),
    _Dfl1660HttpAlgTotalBlocked_Type()
)
dfl1660HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgTotalBlocked.setStatus("current")
_Dfl1660HttpAlgCntFltTable_Object = MibTable
dfl1660HttpAlgCntFltTable = _Dfl1660HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltTable.setStatus("current")
_Dfl1660HttpAlgCntFltEntry_Object = MibTableRow
dfl1660HttpAlgCntFltEntry = _Dfl1660HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2, 1)
)
dfl1660HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660HttpAlgIndex"),
    (0, "DFL1660-MIB", "dfl1660HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltEntry.setStatus("current")


class _Dfl1660HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl1660HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl1660HttpAlgCntFltIndex_Object = MibTableColumn
dfl1660HttpAlgCntFltIndex = _Dfl1660HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2, 1, 1),
    _Dfl1660HttpAlgCntFltIndex_Type()
)
dfl1660HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltIndex.setStatus("current")
_Dfl1660HttpAlgCntFltName_Type = DisplayString
_Dfl1660HttpAlgCntFltName_Object = MibTableColumn
dfl1660HttpAlgCntFltName = _Dfl1660HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2, 1, 2),
    _Dfl1660HttpAlgCntFltName_Type()
)
dfl1660HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltName.setStatus("current")
_Dfl1660HttpAlgCntFltRequests_Type = Gauge32
_Dfl1660HttpAlgCntFltRequests_Object = MibTableColumn
dfl1660HttpAlgCntFltRequests = _Dfl1660HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2, 1, 3),
    _Dfl1660HttpAlgCntFltRequests_Type()
)
dfl1660HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltRequests.setStatus("current")
_Dfl1660HttpAlgCntFltAllowed_Type = Gauge32
_Dfl1660HttpAlgCntFltAllowed_Object = MibTableColumn
dfl1660HttpAlgCntFltAllowed = _Dfl1660HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2, 1, 4),
    _Dfl1660HttpAlgCntFltAllowed_Type()
)
dfl1660HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltAllowed.setStatus("current")
_Dfl1660HttpAlgCntFltBlocked_Type = Gauge32
_Dfl1660HttpAlgCntFltBlocked_Object = MibTableColumn
dfl1660HttpAlgCntFltBlocked = _Dfl1660HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 4, 2, 1, 5),
    _Dfl1660HttpAlgCntFltBlocked_Type()
)
dfl1660HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HttpAlgCntFltBlocked.setStatus("current")
_Dfl1660SmtpAlg_ObjectIdentity = ObjectIdentity
dfl1660SmtpAlg = _Dfl1660SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5)
)
_Dfl1660SmtpAlgTable_Object = MibTable
dfl1660SmtpAlgTable = _Dfl1660SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl1660SmtpAlgTable.setStatus("current")
_Dfl1660SmtpAlgEntry_Object = MibTableRow
dfl1660SmtpAlgEntry = _Dfl1660SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1, 1)
)
dfl1660SmtpAlgEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl1660SmtpAlgEntry.setStatus("current")


class _Dfl1660SmtpAlgIndex_Type(Integer32):
    """Custom type dfl1660SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl1660SmtpAlgIndex_Object = MibTableColumn
dfl1660SmtpAlgIndex = _Dfl1660SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1, 1, 1),
    _Dfl1660SmtpAlgIndex_Type()
)
dfl1660SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgIndex.setStatus("current")
_Dfl1660SmtpAlgName_Type = DisplayString
_Dfl1660SmtpAlgName_Object = MibTableColumn
dfl1660SmtpAlgName = _Dfl1660SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1, 1, 2),
    _Dfl1660SmtpAlgName_Type()
)
dfl1660SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgName.setStatus("current")
_Dfl1660SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl1660SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl1660SmtpAlgTotCheckedSes = _Dfl1660SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1, 1, 3),
    _Dfl1660SmtpAlgTotCheckedSes_Type()
)
dfl1660SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgTotCheckedSes.setStatus("current")
_Dfl1660SmtpAlgTotSpamSes_Type = Gauge32
_Dfl1660SmtpAlgTotSpamSes_Object = MibTableColumn
dfl1660SmtpAlgTotSpamSes = _Dfl1660SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1, 1, 4),
    _Dfl1660SmtpAlgTotSpamSes_Type()
)
dfl1660SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgTotSpamSes.setStatus("current")
_Dfl1660SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl1660SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl1660SmtpAlgTotDroppedSes = _Dfl1660SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 1, 1, 5),
    _Dfl1660SmtpAlgTotDroppedSes_Type()
)
dfl1660SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgTotDroppedSes.setStatus("current")
_Dfl1660SmtpAlgDnsBlTable_Object = MibTable
dfl1660SmtpAlgDnsBlTable = _Dfl1660SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlTable.setStatus("current")
_Dfl1660SmtpAlgDnsBlEntry_Object = MibTableRow
dfl1660SmtpAlgDnsBlEntry = _Dfl1660SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2, 1)
)
dfl1660SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660SmtpAlgIndex"),
    (0, "DFL1660-MIB", "dfl1660SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl1660SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl1660SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl1660SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl1660SmtpAlgDnsBlIndex = _Dfl1660SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2, 1, 1),
    _Dfl1660SmtpAlgDnsBlIndex_Type()
)
dfl1660SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlIndex.setStatus("current")
_Dfl1660SmtpAlgDnsBlName_Type = DisplayString
_Dfl1660SmtpAlgDnsBlName_Object = MibTableColumn
dfl1660SmtpAlgDnsBlName = _Dfl1660SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2, 1, 2),
    _Dfl1660SmtpAlgDnsBlName_Type()
)
dfl1660SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlName.setStatus("current")
_Dfl1660SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl1660SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl1660SmtpAlgDnsBlChecked = _Dfl1660SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2, 1, 3),
    _Dfl1660SmtpAlgDnsBlChecked_Type()
)
dfl1660SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlChecked.setStatus("current")
_Dfl1660SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl1660SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl1660SmtpAlgDnsBlMatched = _Dfl1660SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2, 1, 4),
    _Dfl1660SmtpAlgDnsBlMatched_Type()
)
dfl1660SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlMatched.setStatus("current")
_Dfl1660SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl1660SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl1660SmtpAlgDnsBlFailChecks = _Dfl1660SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 9, 5, 2, 1, 5),
    _Dfl1660SmtpAlgDnsBlFailChecks_Type()
)
dfl1660SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl1660DHCPRelay_ObjectIdentity = ObjectIdentity
dfl1660DHCPRelay = _Dfl1660DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11)
)
_Dfl1660DHCPRelayCurClients_Type = Gauge32
_Dfl1660DHCPRelayCurClients_Object = MibScalar
dfl1660DHCPRelayCurClients = _Dfl1660DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 1),
    _Dfl1660DHCPRelayCurClients_Type()
)
dfl1660DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayCurClients.setStatus("current")
_Dfl1660DHCPRelayCurTrans_Type = Gauge32
_Dfl1660DHCPRelayCurTrans_Object = MibScalar
dfl1660DHCPRelayCurTrans = _Dfl1660DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 2),
    _Dfl1660DHCPRelayCurTrans_Type()
)
dfl1660DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayCurTrans.setStatus("current")
_Dfl1660DHCPRelayRejected_Type = Gauge32
_Dfl1660DHCPRelayRejected_Object = MibScalar
dfl1660DHCPRelayRejected = _Dfl1660DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 3),
    _Dfl1660DHCPRelayRejected_Type()
)
dfl1660DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRejected.setStatus("current")
_Dfl1660DHCPRelayRuleTable_Object = MibTable
dfl1660DHCPRelayRuleTable = _Dfl1660DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleTable.setStatus("current")
_Dfl1660DHCPRelayRuleEntry_Object = MibTableRow
dfl1660DHCPRelayRuleEntry = _Dfl1660DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1)
)
dfl1660DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL1660-MIB", "dfl1660DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleEntry.setStatus("current")


class _Dfl1660DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl1660DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl1660DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl1660DHCPRelayRuleIndex_Object = MibTableColumn
dfl1660DHCPRelayRuleIndex = _Dfl1660DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1, 1),
    _Dfl1660DHCPRelayRuleIndex_Type()
)
dfl1660DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleIndex.setStatus("current")
_Dfl1660DHCPRelayRuleName_Type = DisplayString
_Dfl1660DHCPRelayRuleName_Object = MibTableColumn
dfl1660DHCPRelayRuleName = _Dfl1660DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1, 2),
    _Dfl1660DHCPRelayRuleName_Type()
)
dfl1660DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleName.setStatus("current")
_Dfl1660DHCPRelayRuleHits_Type = Gauge32
_Dfl1660DHCPRelayRuleHits_Object = MibTableColumn
dfl1660DHCPRelayRuleHits = _Dfl1660DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1, 3),
    _Dfl1660DHCPRelayRuleHits_Type()
)
dfl1660DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleHits.setStatus("current")
_Dfl1660DHCPRelayRuleCurClients_Type = Gauge32
_Dfl1660DHCPRelayRuleCurClients_Object = MibTableColumn
dfl1660DHCPRelayRuleCurClients = _Dfl1660DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1, 4),
    _Dfl1660DHCPRelayRuleCurClients_Type()
)
dfl1660DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleCurClients.setStatus("current")
_Dfl1660DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl1660DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl1660DHCPRelayRuleRejCliPkts = _Dfl1660DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1, 5),
    _Dfl1660DHCPRelayRuleRejCliPkts_Type()
)
dfl1660DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl1660DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl1660DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl1660DHCPRelayRuleRejSrvPkts = _Dfl1660DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 11, 4, 1, 6),
    _Dfl1660DHCPRelayRuleRejSrvPkts_Type()
)
dfl1660DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl1660HA_ObjectIdentity = ObjectIdentity
dfl1660HA = _Dfl1660HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 12)
)
_Dfl1660HASyncSendQueueLength_Type = Gauge32
_Dfl1660HASyncSendQueueLength_Object = MibScalar
dfl1660HASyncSendQueueLength = _Dfl1660HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 12, 1),
    _Dfl1660HASyncSendQueueLength_Type()
)
dfl1660HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HASyncSendQueueLength.setStatus("current")
_Dfl1660HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl1660HASyncSendQueueUsagePkt_Object = MibScalar
dfl1660HASyncSendQueueUsagePkt = _Dfl1660HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 12, 2),
    _Dfl1660HASyncSendQueueUsagePkt_Type()
)
dfl1660HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HASyncSendQueueUsagePkt.setStatus("current")
_Dfl1660HASyncSendQueueUsageOct_Type = Gauge32
_Dfl1660HASyncSendQueueUsageOct_Object = MibScalar
dfl1660HASyncSendQueueUsageOct = _Dfl1660HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 12, 3),
    _Dfl1660HASyncSendQueueUsageOct_Type()
)
dfl1660HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HASyncSendQueueUsageOct.setStatus("current")
_Dfl1660HASyncSentPackets_Type = Counter32
_Dfl1660HASyncSentPackets_Object = MibScalar
dfl1660HASyncSentPackets = _Dfl1660HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 12, 4),
    _Dfl1660HASyncSentPackets_Type()
)
dfl1660HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HASyncSentPackets.setStatus("current")
_Dfl1660HASyncSendResentPackets_Type = Counter32
_Dfl1660HASyncSendResentPackets_Object = MibScalar
dfl1660HASyncSendResentPackets = _Dfl1660HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 1, 2, 12, 5),
    _Dfl1660HASyncSendResentPackets_Type()
)
dfl1660HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl1660HASyncSendResentPackets.setStatus("current")
_Dfl1660reg_ObjectIdentity = ObjectIdentity
dfl1660reg = _Dfl1660reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2)
)
_Dfl1660MibModules_ObjectIdentity = ObjectIdentity
dfl1660MibModules = _Dfl1660MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 1)
)
_Dfl1660MibConfs_ObjectIdentity = ObjectIdentity
dfl1660MibConfs = _Dfl1660MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 2)
)
_Dfl1660StatsConformance_ObjectIdentity = ObjectIdentity
dfl1660StatsConformance = _Dfl1660StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 2, 1)
)
_Dfl1660MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl1660MibObjectGroups = _Dfl1660MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3)
)
_Dfl1660StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl1660StatsRegGroups = _Dfl1660StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1)
)

# Managed Objects groups

dfl1660SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 1)
)
dfl1660SystemObjectGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660SysCpuLoad"),
        ("DFL1660-MIB", "dfl1660SysForwardedBits"),
        ("DFL1660-MIB", "dfl1660SysForwardedPackets"),
        ("DFL1660-MIB", "dfl1660SysBuffUse"),
        ("DFL1660-MIB", "dfl1660SysConns"),
        ("DFL1660-MIB", "dfl1660HWSensorName"),
        ("DFL1660-MIB", "dfl1660HWSensorValue"),
        ("DFL1660-MIB", "dfl1660HWSensorUnit"),
        ("DFL1660-MIB", "dfl1660SysMemUsage"),
        ("DFL1660-MIB", "dfl1660SysTimerUsage"),
        ("DFL1660-MIB", "dfl1660SysConnOPS"),
        ("DFL1660-MIB", "dfl1660SysConnCPS"),
        ("DFL1660-MIB", "dfl1660SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl1660SystemObjectGroup.setStatus("current")

dfl1660IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 2)
)
dfl1660IPsecObjectGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660IPsecPhaseOneActive"),
        ("DFL1660-MIB", "dfl1660IPsecPhaseOneAggrModeDone"),
        ("DFL1660-MIB", "dfl1660IPsecQuickModeActive"),
        ("DFL1660-MIB", "dfl1660IPsecPhaseOneDone"),
        ("DFL1660-MIB", "dfl1660IPsecPhaseOneFailed"),
        ("DFL1660-MIB", "dfl1660IPsecPhaseOneRekeyed"),
        ("DFL1660-MIB", "dfl1660IPsecQuickModeDone"),
        ("DFL1660-MIB", "dfl1660IPsecQuickModeFailed"),
        ("DFL1660-MIB", "dfl1660IPsecInfoDone"),
        ("DFL1660-MIB", "dfl1660IPsecInfoFailed"),
        ("DFL1660-MIB", "dfl1660IPsecInOctetsComp"),
        ("DFL1660-MIB", "dfl1660IPsecInOctetsUncomp"),
        ("DFL1660-MIB", "dfl1660IPsecOutOctetsComp"),
        ("DFL1660-MIB", "dfl1660IPsecOutOctetsUncomp"),
        ("DFL1660-MIB", "dfl1660IPsecForwardedOctetsComp"),
        ("DFL1660-MIB", "dfl1660IPsecForwardedOctetsUcomp"),
        ("DFL1660-MIB", "dfl1660IPsecInPackets"),
        ("DFL1660-MIB", "dfl1660IPsecOutPackets"),
        ("DFL1660-MIB", "dfl1660IPsecForwardedPackets"),
        ("DFL1660-MIB", "dfl1660IPsecActiveTransforms"),
        ("DFL1660-MIB", "dfl1660IPsecTotalTransforms"),
        ("DFL1660-MIB", "dfl1660IPsecOutOfTransforms"),
        ("DFL1660-MIB", "dfl1660IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl1660IPsecObjectGroup.setStatus("current")

dfl1660StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 3)
)
dfl1660StateCountersGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660SysPscTcpSyn"),
        ("DFL1660-MIB", "dfl1660SysPscTcpOpen"),
        ("DFL1660-MIB", "dfl1660SysPscTcpFin"),
        ("DFL1660-MIB", "dfl1660SysPscUdp"),
        ("DFL1660-MIB", "dfl1660SysPscIcmp"),
        ("DFL1660-MIB", "dfl1660SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl1660StateCountersGroup.setStatus("current")

dfl1660IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 4)
)
dfl1660IPPoolGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660IPPoolsNumber"),
        ("DFL1660-MIB", "dfl1660IPPoolName"),
        ("DFL1660-MIB", "dfl1660IPPoolPrepare"),
        ("DFL1660-MIB", "dfl1660IPPoolFree"),
        ("DFL1660-MIB", "dfl1660IPPoolMisses"),
        ("DFL1660-MIB", "dfl1660IPPoolClientFails"),
        ("DFL1660-MIB", "dfl1660IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl1660IPPoolGroup.setStatus("current")

dfl1660DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 5)
)
dfl1660DHCPServerGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660DHCPTotalRejected"),
        ("DFL1660-MIB", "dfl1660DHCPRuleName"),
        ("DFL1660-MIB", "dfl1660DHCPRuleUsage"),
        ("DFL1660-MIB", "dfl1660DHCPRuleUsagePercent"),
        ("DFL1660-MIB", "dfl1660DHCPActiveClients"),
        ("DFL1660-MIB", "dfl1660DHCPActiveClientsPercent"),
        ("DFL1660-MIB", "dfl1660DHCPRejectedRequests"),
        ("DFL1660-MIB", "dfl1660DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl1660DHCPServerGroup.setStatus("current")

dfl1660RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 6)
)
dfl1660RuleUseGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660RuleName"),
        ("DFL1660-MIB", "dfl1660RuleUse"))
)
if mibBuilder.loadTexts:
    dfl1660RuleUseGroup.setStatus("current")

dfl1660UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 7)
)
dfl1660UserAuthGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660UserAuthHTTPUsers"),
        ("DFL1660-MIB", "dfl1660UserAuthXAUTHUsers"),
        ("DFL1660-MIB", "dfl1660UserAuthHTTPSUsers"),
        ("DFL1660-MIB", "dfl1660UserAuthPPPUsers"),
        ("DFL1660-MIB", "dfl1660UserAuthEAPUsers"),
        ("DFL1660-MIB", "dfl1660UserAuthRuleName"),
        ("DFL1660-MIB", "dfl1660UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl1660UserAuthGroup.setStatus("current")

dfl1660IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 8)
)
dfl1660IfStatsGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660IfName"),
        ("DFL1660-MIB", "dfl1660IfFragsIn"),
        ("DFL1660-MIB", "dfl1660IfFragReassOk"),
        ("DFL1660-MIB", "dfl1660IfFragReassFail"),
        ("DFL1660-MIB", "dfl1660IfPktsInCnt"),
        ("DFL1660-MIB", "dfl1660IfPktsOutCnt"),
        ("DFL1660-MIB", "dfl1660IfBitsInCnt"),
        ("DFL1660-MIB", "dfl1660IfBitsOutCnt"),
        ("DFL1660-MIB", "dfl1660IfPktsTotCnt"),
        ("DFL1660-MIB", "dfl1660IfBitsTotCnt"),
        ("DFL1660-MIB", "dfl1660IfHCPktsInCnt"),
        ("DFL1660-MIB", "dfl1660IfHCPktsOutCnt"),
        ("DFL1660-MIB", "dfl1660IfHCBitsInCnt"),
        ("DFL1660-MIB", "dfl1660IfHCBitsOutCnt"),
        ("DFL1660-MIB", "dfl1660IfHCPktsTotCnt"),
        ("DFL1660-MIB", "dfl1660IfHCBitsTotCnt"),
        ("DFL1660-MIB", "dfl1660IfRxRingFifoErrors"),
        ("DFL1660-MIB", "dfl1660IfRxDespools"),
        ("DFL1660-MIB", "dfl1660IfRxAvgUse"),
        ("DFL1660-MIB", "dfl1660IfRxRingSaturation"),
        ("DFL1660-MIB", "dfl1660RxRingFlooded"),
        ("DFL1660-MIB", "dfl1660IfTxDespools"),
        ("DFL1660-MIB", "dfl1660IfTxAvgUse"),
        ("DFL1660-MIB", "dfl1660IfTxRingSaturation"),
        ("DFL1660-MIB", "dfl1660RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl1660IfStatsGroup.setStatus("current")

dfl1660LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 9)
)
dfl1660LinkMonitorGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660LinkMonGrp"),
        ("DFL1660-MIB", "dfl1660LinkMonGrpName"),
        ("DFL1660-MIB", "dfl1660LinkMonGrpHostsUp"),
        ("DFL1660-MIB", "dfl1660LinkMonHostId"),
        ("DFL1660-MIB", "dfl1660LinkMonHostShortTermLoss"),
        ("DFL1660-MIB", "dfl1660LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl1660LinkMonitorGroup.setStatus("current")

dfl1660PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 10)
)
dfl1660PipesObjectGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660PipeUsers"),
        ("DFL1660-MIB", "dfl1660PipeName"),
        ("DFL1660-MIB", "dfl1660PipeMinPrec"),
        ("DFL1660-MIB", "dfl1660PipeMaxPrec"),
        ("DFL1660-MIB", "dfl1660PipeDefPrec"),
        ("DFL1660-MIB", "dfl1660PipeNumPrec"),
        ("DFL1660-MIB", "dfl1660PipeNumUsers"),
        ("DFL1660-MIB", "dfl1660PipeCurrentBps"),
        ("DFL1660-MIB", "dfl1660PipeCurrentPps"),
        ("DFL1660-MIB", "dfl1660PipeDelayedPackets"),
        ("DFL1660-MIB", "dfl1660PipeDropedPackets"),
        ("DFL1660-MIB", "dfl1660PipePrec"),
        ("DFL1660-MIB", "dfl1660PipePrecBps"),
        ("DFL1660-MIB", "dfl1660PipePrecTotalPps"),
        ("DFL1660-MIB", "dfl1660PipePrecReservedBps"),
        ("DFL1660-MIB", "dfl1660PipePrecDynLimBps"),
        ("DFL1660-MIB", "dfl1660PipePrecDynUsrLimBps"),
        ("DFL1660-MIB", "dfl1660PipePrecDelayedPackets"),
        ("DFL1660-MIB", "dfl1660PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl1660PipesObjectGroup.setStatus("current")

dfl1660DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 12)
)
dfl1660DHCPRelayObjectGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660DHCPRelayCurClients"),
        ("DFL1660-MIB", "dfl1660DHCPRelayCurTrans"),
        ("DFL1660-MIB", "dfl1660DHCPRelayRejected"),
        ("DFL1660-MIB", "dfl1660DHCPRelayRuleName"),
        ("DFL1660-MIB", "dfl1660DHCPRelayRuleHits"),
        ("DFL1660-MIB", "dfl1660DHCPRelayRuleCurClients"),
        ("DFL1660-MIB", "dfl1660DHCPRelayRuleRejCliPkts"),
        ("DFL1660-MIB", "dfl1660DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl1660DHCPRelayObjectGroup.setStatus("current")

dfl1660AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 13)
)
dfl1660AlgGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660AlgSessions"),
        ("DFL1660-MIB", "dfl1660AlgConnections"),
        ("DFL1660-MIB", "dfl1660AlgTCPStreams"),
        ("DFL1660-MIB", "dfl1660HttpAlgName"),
        ("DFL1660-MIB", "dfl1660HttpAlgTotalRequested"),
        ("DFL1660-MIB", "dfl1660HttpAlgTotalAllowed"),
        ("DFL1660-MIB", "dfl1660HttpAlgTotalBlocked"),
        ("DFL1660-MIB", "dfl1660HttpAlgCntFltName"),
        ("DFL1660-MIB", "dfl1660HttpAlgCntFltRequests"),
        ("DFL1660-MIB", "dfl1660HttpAlgCntFltAllowed"),
        ("DFL1660-MIB", "dfl1660HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl1660AlgGroup.setStatus("current")

dfl1660HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 14)
)
dfl1660HAGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660HASyncSendQueueLength"),
        ("DFL1660-MIB", "dfl1660HASyncSendQueueUsagePkt"),
        ("DFL1660-MIB", "dfl1660HASyncSendQueueUsageOct"),
        ("DFL1660-MIB", "dfl1660HASyncSentPackets"),
        ("DFL1660-MIB", "dfl1660HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl1660HAGroup.setStatus("current")

dfl1660IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 15)
)
dfl1660IfVlanGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660IfVlanUntaggedInPkts"),
        ("DFL1660-MIB", "dfl1660IfVlanUntaggedOutPkts"),
        ("DFL1660-MIB", "dfl1660IfVlanUntaggedTotPkts"),
        ("DFL1660-MIB", "dfl1660IfVlanUntaggedInOctets"),
        ("DFL1660-MIB", "dfl1660IfVlanUntaggedOutOctets"),
        ("DFL1660-MIB", "dfl1660IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl1660IfVlanGroup.setStatus("current")

dfl1660SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 16)
)
dfl1660SmtpAlgGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660SmtpAlgName"),
        ("DFL1660-MIB", "dfl1660SmtpAlgTotCheckedSes"),
        ("DFL1660-MIB", "dfl1660SmtpAlgTotSpamSes"),
        ("DFL1660-MIB", "dfl1660SmtpAlgTotDroppedSes"),
        ("DFL1660-MIB", "dfl1660SmtpAlgDnsBlName"),
        ("DFL1660-MIB", "dfl1660SmtpAlgDnsBlChecked"),
        ("DFL1660-MIB", "dfl1660SmtpAlgDnsBlMatched"),
        ("DFL1660-MIB", "dfl1660SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl1660SmtpAlgGroup.setStatus("current")

dfl1660SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 3, 1, 17)
)
dfl1660SysTCPGroup.setObjects(
      *(("DFL1660-MIB", "dfl1660SysTCPRecvSmall"),
        ("DFL1660-MIB", "dfl1660SysTCPRecvLarge"),
        ("DFL1660-MIB", "dfl1660SysTCPSendSmall"),
        ("DFL1660-MIB", "dfl1660SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl1660SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl1660StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 3, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl1660StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL1660-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "utmFirewall": utmFirewall,
       "dfl1660": dfl1660,
       "dfl1660OS": dfl1660OS,
       "dfl1660OSStats": dfl1660OSStats,
       "dfl1660System": dfl1660System,
       "dfl1660SysCpuLoad": dfl1660SysCpuLoad,
       "dfl1660SysForwardedBits": dfl1660SysForwardedBits,
       "dfl1660SysForwardedPackets": dfl1660SysForwardedPackets,
       "dfl1660SysBuffUse": dfl1660SysBuffUse,
       "dfl1660SysConns": dfl1660SysConns,
       "dfl1660SysPerStateCounters": dfl1660SysPerStateCounters,
       "dfl1660SysPscTcpSyn": dfl1660SysPscTcpSyn,
       "dfl1660SysPscTcpOpen": dfl1660SysPscTcpOpen,
       "dfl1660SysPscTcpFin": dfl1660SysPscTcpFin,
       "dfl1660SysPscUdp": dfl1660SysPscUdp,
       "dfl1660SysPscIcmp": dfl1660SysPscIcmp,
       "dfl1660SysPscOther": dfl1660SysPscOther,
       "dfl1660IfStatsTable": dfl1660IfStatsTable,
       "dfl1660IfStatsEntry": dfl1660IfStatsEntry,
       "dfl1660IfStatsIndex": dfl1660IfStatsIndex,
       "dfl1660IfName": dfl1660IfName,
       "dfl1660IfFragsIn": dfl1660IfFragsIn,
       "dfl1660IfFragReassOk": dfl1660IfFragReassOk,
       "dfl1660IfFragReassFail": dfl1660IfFragReassFail,
       "dfl1660IfPktsInCnt": dfl1660IfPktsInCnt,
       "dfl1660IfPktsOutCnt": dfl1660IfPktsOutCnt,
       "dfl1660IfBitsInCnt": dfl1660IfBitsInCnt,
       "dfl1660IfBitsOutCnt": dfl1660IfBitsOutCnt,
       "dfl1660IfPktsTotCnt": dfl1660IfPktsTotCnt,
       "dfl1660IfBitsTotCnt": dfl1660IfBitsTotCnt,
       "dfl1660IfHCPktsInCnt": dfl1660IfHCPktsInCnt,
       "dfl1660IfHCPktsOutCnt": dfl1660IfHCPktsOutCnt,
       "dfl1660IfHCBitsInCnt": dfl1660IfHCBitsInCnt,
       "dfl1660IfHCBitsOutCnt": dfl1660IfHCBitsOutCnt,
       "dfl1660IfHCPktsTotCnt": dfl1660IfHCPktsTotCnt,
       "dfl1660IfHCBitsTotCnt": dfl1660IfHCBitsTotCnt,
       "dfl1660IfRxRingTable": dfl1660IfRxRingTable,
       "dfl1660IfRxRingEntry": dfl1660IfRxRingEntry,
       "dfl1660IfRxRingIndex": dfl1660IfRxRingIndex,
       "dfl1660IfRxRingFifoErrors": dfl1660IfRxRingFifoErrors,
       "dfl1660IfRxDespools": dfl1660IfRxDespools,
       "dfl1660IfRxAvgUse": dfl1660IfRxAvgUse,
       "dfl1660IfRxRingSaturation": dfl1660IfRxRingSaturation,
       "dfl1660RxRingFlooded": dfl1660RxRingFlooded,
       "dfl1660IfTxRingTable": dfl1660IfTxRingTable,
       "dfl1660IfTxRingEntry": dfl1660IfTxRingEntry,
       "dfl1660IfTxRingIndex": dfl1660IfTxRingIndex,
       "dfl1660IfTxDespools": dfl1660IfTxDespools,
       "dfl1660IfTxAvgUse": dfl1660IfTxAvgUse,
       "dfl1660IfTxRingSaturation": dfl1660IfTxRingSaturation,
       "dfl1660RxTingFlooded": dfl1660RxTingFlooded,
       "dfl1660IfVlanStatsTable": dfl1660IfVlanStatsTable,
       "dfl1660IfVlanStatsEntry": dfl1660IfVlanStatsEntry,
       "dfl1660IfVlanIndex": dfl1660IfVlanIndex,
       "dfl1660IfVlanUntaggedInPkts": dfl1660IfVlanUntaggedInPkts,
       "dfl1660IfVlanUntaggedOutPkts": dfl1660IfVlanUntaggedOutPkts,
       "dfl1660IfVlanUntaggedTotPkts": dfl1660IfVlanUntaggedTotPkts,
       "dfl1660IfVlanUntaggedInOctets": dfl1660IfVlanUntaggedInOctets,
       "dfl1660IfVlanUntaggedOutOctets": dfl1660IfVlanUntaggedOutOctets,
       "dfl1660IfVlanUntaggedTotOctets": dfl1660IfVlanUntaggedTotOctets,
       "dfl1660HWSensorTable": dfl1660HWSensorTable,
       "dfl1660HWSensorEntry": dfl1660HWSensorEntry,
       "dfl1660HWSensorIndex": dfl1660HWSensorIndex,
       "dfl1660HWSensorName": dfl1660HWSensorName,
       "dfl1660HWSensorValue": dfl1660HWSensorValue,
       "dfl1660HWSensorUnit": dfl1660HWSensorUnit,
       "dfl1660SysMemUsage": dfl1660SysMemUsage,
       "dfl1660SysTCPUsage": dfl1660SysTCPUsage,
       "dfl1660SysTCPRecvSmall": dfl1660SysTCPRecvSmall,
       "dfl1660SysTCPRecvLarge": dfl1660SysTCPRecvLarge,
       "dfl1660SysTCPSendSmall": dfl1660SysTCPSendSmall,
       "dfl1660SysTCPSendLarge": dfl1660SysTCPSendLarge,
       "dfl1660SysTimerUsage": dfl1660SysTimerUsage,
       "dfl1660SysConnOPS": dfl1660SysConnOPS,
       "dfl1660SysConnCPS": dfl1660SysConnCPS,
       "dfl1660SysHCForwardedBits": dfl1660SysHCForwardedBits,
       "dfl1660VPN": dfl1660VPN,
       "dfl1660IPsec": dfl1660IPsec,
       "dfl1660IPsecGlobal": dfl1660IPsecGlobal,
       "dfl1660IPsecPhaseOneActive": dfl1660IPsecPhaseOneActive,
       "dfl1660IPsecPhaseOneAggrModeDone": dfl1660IPsecPhaseOneAggrModeDone,
       "dfl1660IPsecQuickModeActive": dfl1660IPsecQuickModeActive,
       "dfl1660IPsecPhaseOneDone": dfl1660IPsecPhaseOneDone,
       "dfl1660IPsecPhaseOneFailed": dfl1660IPsecPhaseOneFailed,
       "dfl1660IPsecPhaseOneRekeyed": dfl1660IPsecPhaseOneRekeyed,
       "dfl1660IPsecQuickModeDone": dfl1660IPsecQuickModeDone,
       "dfl1660IPsecQuickModeFailed": dfl1660IPsecQuickModeFailed,
       "dfl1660IPsecInfoDone": dfl1660IPsecInfoDone,
       "dfl1660IPsecInfoFailed": dfl1660IPsecInfoFailed,
       "dfl1660IPsecInOctetsComp": dfl1660IPsecInOctetsComp,
       "dfl1660IPsecInOctetsUncomp": dfl1660IPsecInOctetsUncomp,
       "dfl1660IPsecOutOctetsComp": dfl1660IPsecOutOctetsComp,
       "dfl1660IPsecOutOctetsUncomp": dfl1660IPsecOutOctetsUncomp,
       "dfl1660IPsecForwardedOctetsComp": dfl1660IPsecForwardedOctetsComp,
       "dfl1660IPsecForwardedOctetsUcomp": dfl1660IPsecForwardedOctetsUcomp,
       "dfl1660IPsecInPackets": dfl1660IPsecInPackets,
       "dfl1660IPsecOutPackets": dfl1660IPsecOutPackets,
       "dfl1660IPsecForwardedPackets": dfl1660IPsecForwardedPackets,
       "dfl1660IPsecActiveTransforms": dfl1660IPsecActiveTransforms,
       "dfl1660IPsecTotalTransforms": dfl1660IPsecTotalTransforms,
       "dfl1660IPsecOutOfTransforms": dfl1660IPsecOutOfTransforms,
       "dfl1660IPsecTotalRekeys": dfl1660IPsecTotalRekeys,
       "dfl1660Rules": dfl1660Rules,
       "dfl1660RuleUseTable": dfl1660RuleUseTable,
       "dfl1660RuleUseEntry": dfl1660RuleUseEntry,
       "dfl1660RuleIndex": dfl1660RuleIndex,
       "dfl1660RuleName": dfl1660RuleName,
       "dfl1660RuleUse": dfl1660RuleUse,
       "dfl1660IPPools": dfl1660IPPools,
       "dfl1660IPPoolsNumber": dfl1660IPPoolsNumber,
       "dfl1660IPPoolTable": dfl1660IPPoolTable,
       "dfl1660IPPoolEntry": dfl1660IPPoolEntry,
       "dfl1660IPPoolIndex": dfl1660IPPoolIndex,
       "dfl1660IPPoolName": dfl1660IPPoolName,
       "dfl1660IPPoolPrepare": dfl1660IPPoolPrepare,
       "dfl1660IPPoolFree": dfl1660IPPoolFree,
       "dfl1660IPPoolMisses": dfl1660IPPoolMisses,
       "dfl1660IPPoolClientFails": dfl1660IPPoolClientFails,
       "dfl1660IPPoolUsed": dfl1660IPPoolUsed,
       "dfl1660DHCPServer": dfl1660DHCPServer,
       "dfl1660DHCPTotalRejected": dfl1660DHCPTotalRejected,
       "dfl1660DHCPRuleTable": dfl1660DHCPRuleTable,
       "dfl1660DHCPRuleEntry": dfl1660DHCPRuleEntry,
       "dfl1660DHCPRuleIndex": dfl1660DHCPRuleIndex,
       "dfl1660DHCPRuleName": dfl1660DHCPRuleName,
       "dfl1660DHCPRuleUsage": dfl1660DHCPRuleUsage,
       "dfl1660DHCPRuleUsagePercent": dfl1660DHCPRuleUsagePercent,
       "dfl1660DHCPActiveClients": dfl1660DHCPActiveClients,
       "dfl1660DHCPActiveClientsPercent": dfl1660DHCPActiveClientsPercent,
       "dfl1660DHCPRejectedRequests": dfl1660DHCPRejectedRequests,
       "dfl1660DHCPTotalLeases": dfl1660DHCPTotalLeases,
       "dfl1660UserAuth": dfl1660UserAuth,
       "dfl1660UserAuthHTTPUsers": dfl1660UserAuthHTTPUsers,
       "dfl1660UserAuthXAUTHUsers": dfl1660UserAuthXAUTHUsers,
       "dfl1660UserAuthHTTPSUsers": dfl1660UserAuthHTTPSUsers,
       "dfl1660UserAuthPPPUsers": dfl1660UserAuthPPPUsers,
       "dfl1660UserAuthEAPUsers": dfl1660UserAuthEAPUsers,
       "dfl1660UserAuthRuleUseTable": dfl1660UserAuthRuleUseTable,
       "dfl1660UserAuthRuleUseEntry": dfl1660UserAuthRuleUseEntry,
       "dfl1660UserAuthRuleIndex": dfl1660UserAuthRuleIndex,
       "dfl1660UserAuthRuleName": dfl1660UserAuthRuleName,
       "dfl1660UserAuthRuleUse": dfl1660UserAuthRuleUse,
       "dfl1660LinkMonitor": dfl1660LinkMonitor,
       "dfl1660LinkMonGrp": dfl1660LinkMonGrp,
       "dfl1660LinkMonGrpTable": dfl1660LinkMonGrpTable,
       "dfl1660LinkMonGrpEntry": dfl1660LinkMonGrpEntry,
       "dfl1660LinkMonGrpIndex": dfl1660LinkMonGrpIndex,
       "dfl1660LinkMonGrpName": dfl1660LinkMonGrpName,
       "dfl1660LinkMonGrpHostsUp": dfl1660LinkMonGrpHostsUp,
       "dfl1660LinkMonHostTable": dfl1660LinkMonHostTable,
       "dfl1660LinkMonHostEntry": dfl1660LinkMonHostEntry,
       "dfl1660LinkMonHostIndex": dfl1660LinkMonHostIndex,
       "dfl1660LinkMonHostId": dfl1660LinkMonHostId,
       "dfl1660LinkMonHostShortTermLoss": dfl1660LinkMonHostShortTermLoss,
       "dfl1660LinkMonHostPacketsLost": dfl1660LinkMonHostPacketsLost,
       "dfl1660Pipes": dfl1660Pipes,
       "dfl1660PipeUsers": dfl1660PipeUsers,
       "dfl1660PipeTable": dfl1660PipeTable,
       "dfl1660PipeEntry": dfl1660PipeEntry,
       "dfl1660PipeIndex": dfl1660PipeIndex,
       "dfl1660PipeName": dfl1660PipeName,
       "dfl1660PipeMinPrec": dfl1660PipeMinPrec,
       "dfl1660PipeMaxPrec": dfl1660PipeMaxPrec,
       "dfl1660PipeDefPrec": dfl1660PipeDefPrec,
       "dfl1660PipeNumPrec": dfl1660PipeNumPrec,
       "dfl1660PipeNumUsers": dfl1660PipeNumUsers,
       "dfl1660PipeCurrentBps": dfl1660PipeCurrentBps,
       "dfl1660PipeCurrentPps": dfl1660PipeCurrentPps,
       "dfl1660PipeDelayedPackets": dfl1660PipeDelayedPackets,
       "dfl1660PipeDropedPackets": dfl1660PipeDropedPackets,
       "dfl1660PipePrecTable": dfl1660PipePrecTable,
       "dfl1660PipePrecEntry": dfl1660PipePrecEntry,
       "dfl1660PipePrecIndex": dfl1660PipePrecIndex,
       "dfl1660PipePrec": dfl1660PipePrec,
       "dfl1660PipePrecBps": dfl1660PipePrecBps,
       "dfl1660PipePrecTotalPps": dfl1660PipePrecTotalPps,
       "dfl1660PipePrecReservedBps": dfl1660PipePrecReservedBps,
       "dfl1660PipePrecDynLimBps": dfl1660PipePrecDynLimBps,
       "dfl1660PipePrecDynUsrLimBps": dfl1660PipePrecDynUsrLimBps,
       "dfl1660PipePrecDelayedPackets": dfl1660PipePrecDelayedPackets,
       "dfl1660PipePrecDropedPackets": dfl1660PipePrecDropedPackets,
       "dfl1660ALG": dfl1660ALG,
       "dfl1660AlgSessions": dfl1660AlgSessions,
       "dfl1660AlgConnections": dfl1660AlgConnections,
       "dfl1660AlgTCPStreams": dfl1660AlgTCPStreams,
       "dfl1660HttpAlg": dfl1660HttpAlg,
       "dfl1660HttpAlgTable": dfl1660HttpAlgTable,
       "dfl1660HttpAlgEntry": dfl1660HttpAlgEntry,
       "dfl1660HttpAlgIndex": dfl1660HttpAlgIndex,
       "dfl1660HttpAlgName": dfl1660HttpAlgName,
       "dfl1660HttpAlgTotalRequested": dfl1660HttpAlgTotalRequested,
       "dfl1660HttpAlgTotalAllowed": dfl1660HttpAlgTotalAllowed,
       "dfl1660HttpAlgTotalBlocked": dfl1660HttpAlgTotalBlocked,
       "dfl1660HttpAlgCntFltTable": dfl1660HttpAlgCntFltTable,
       "dfl1660HttpAlgCntFltEntry": dfl1660HttpAlgCntFltEntry,
       "dfl1660HttpAlgCntFltIndex": dfl1660HttpAlgCntFltIndex,
       "dfl1660HttpAlgCntFltName": dfl1660HttpAlgCntFltName,
       "dfl1660HttpAlgCntFltRequests": dfl1660HttpAlgCntFltRequests,
       "dfl1660HttpAlgCntFltAllowed": dfl1660HttpAlgCntFltAllowed,
       "dfl1660HttpAlgCntFltBlocked": dfl1660HttpAlgCntFltBlocked,
       "dfl1660SmtpAlg": dfl1660SmtpAlg,
       "dfl1660SmtpAlgTable": dfl1660SmtpAlgTable,
       "dfl1660SmtpAlgEntry": dfl1660SmtpAlgEntry,
       "dfl1660SmtpAlgIndex": dfl1660SmtpAlgIndex,
       "dfl1660SmtpAlgName": dfl1660SmtpAlgName,
       "dfl1660SmtpAlgTotCheckedSes": dfl1660SmtpAlgTotCheckedSes,
       "dfl1660SmtpAlgTotSpamSes": dfl1660SmtpAlgTotSpamSes,
       "dfl1660SmtpAlgTotDroppedSes": dfl1660SmtpAlgTotDroppedSes,
       "dfl1660SmtpAlgDnsBlTable": dfl1660SmtpAlgDnsBlTable,
       "dfl1660SmtpAlgDnsBlEntry": dfl1660SmtpAlgDnsBlEntry,
       "dfl1660SmtpAlgDnsBlIndex": dfl1660SmtpAlgDnsBlIndex,
       "dfl1660SmtpAlgDnsBlName": dfl1660SmtpAlgDnsBlName,
       "dfl1660SmtpAlgDnsBlChecked": dfl1660SmtpAlgDnsBlChecked,
       "dfl1660SmtpAlgDnsBlMatched": dfl1660SmtpAlgDnsBlMatched,
       "dfl1660SmtpAlgDnsBlFailChecks": dfl1660SmtpAlgDnsBlFailChecks,
       "dfl1660DHCPRelay": dfl1660DHCPRelay,
       "dfl1660DHCPRelayCurClients": dfl1660DHCPRelayCurClients,
       "dfl1660DHCPRelayCurTrans": dfl1660DHCPRelayCurTrans,
       "dfl1660DHCPRelayRejected": dfl1660DHCPRelayRejected,
       "dfl1660DHCPRelayRuleTable": dfl1660DHCPRelayRuleTable,
       "dfl1660DHCPRelayRuleEntry": dfl1660DHCPRelayRuleEntry,
       "dfl1660DHCPRelayRuleIndex": dfl1660DHCPRelayRuleIndex,
       "dfl1660DHCPRelayRuleName": dfl1660DHCPRelayRuleName,
       "dfl1660DHCPRelayRuleHits": dfl1660DHCPRelayRuleHits,
       "dfl1660DHCPRelayRuleCurClients": dfl1660DHCPRelayRuleCurClients,
       "dfl1660DHCPRelayRuleRejCliPkts": dfl1660DHCPRelayRuleRejCliPkts,
       "dfl1660DHCPRelayRuleRejSrvPkts": dfl1660DHCPRelayRuleRejSrvPkts,
       "dfl1660HA": dfl1660HA,
       "dfl1660HASyncSendQueueLength": dfl1660HASyncSendQueueLength,
       "dfl1660HASyncSendQueueUsagePkt": dfl1660HASyncSendQueueUsagePkt,
       "dfl1660HASyncSendQueueUsageOct": dfl1660HASyncSendQueueUsageOct,
       "dfl1660HASyncSentPackets": dfl1660HASyncSentPackets,
       "dfl1660HASyncSendResentPackets": dfl1660HASyncSendResentPackets,
       "dfl1660reg": dfl1660reg,
       "dfl1660MibModules": dfl1660MibModules,
       "dfl1660-MIB": dfl1660_MIB,
       "dfl1660MibConfs": dfl1660MibConfs,
       "dfl1660StatsConformance": dfl1660StatsConformance,
       "dfl1660StatsCompliance": dfl1660StatsCompliance,
       "dfl1660MibObjectGroups": dfl1660MibObjectGroups,
       "dfl1660StatsRegGroups": dfl1660StatsRegGroups,
       "dfl1660SystemObjectGroup": dfl1660SystemObjectGroup,
       "dfl1660IPsecObjectGroup": dfl1660IPsecObjectGroup,
       "dfl1660StateCountersGroup": dfl1660StateCountersGroup,
       "dfl1660IPPoolGroup": dfl1660IPPoolGroup,
       "dfl1660DHCPServerGroup": dfl1660DHCPServerGroup,
       "dfl1660RuleUseGroup": dfl1660RuleUseGroup,
       "dfl1660UserAuthGroup": dfl1660UserAuthGroup,
       "dfl1660IfStatsGroup": dfl1660IfStatsGroup,
       "dfl1660LinkMonitorGroup": dfl1660LinkMonitorGroup,
       "dfl1660PipesObjectGroup": dfl1660PipesObjectGroup,
       "dfl1660DHCPRelayObjectGroup": dfl1660DHCPRelayObjectGroup,
       "dfl1660AlgGroup": dfl1660AlgGroup,
       "dfl1660HAGroup": dfl1660HAGroup,
       "dfl1660IfVlanGroup": dfl1660IfVlanGroup,
       "dfl1660SmtpAlgGroup": dfl1660SmtpAlgGroup,
       "dfl1660SysTCPGroup": dfl1660SysTCPGroup}
)
