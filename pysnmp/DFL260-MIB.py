# SNMP MIB module (DFL260-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL260-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:17 2024
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

dfl260_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 1, 2)
)
dfl260_MIB.setRevisions(
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
_Dfl260_ObjectIdentity = ObjectIdentity
dfl260 = _Dfl260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1)
)
_Dfl260OS_ObjectIdentity = ObjectIdentity
dfl260OS = _Dfl260OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1)
)
_Dfl260OSStats_ObjectIdentity = ObjectIdentity
dfl260OSStats = _Dfl260OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2)
)
_Dfl260System_ObjectIdentity = ObjectIdentity
dfl260System = _Dfl260System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1)
)
_Dfl260SysCpuLoad_Type = Gauge32
_Dfl260SysCpuLoad_Object = MibScalar
dfl260SysCpuLoad = _Dfl260SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 1),
    _Dfl260SysCpuLoad_Type()
)
dfl260SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysCpuLoad.setStatus("current")
_Dfl260SysForwardedBits_Type = Counter32
_Dfl260SysForwardedBits_Object = MibScalar
dfl260SysForwardedBits = _Dfl260SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 2),
    _Dfl260SysForwardedBits_Type()
)
dfl260SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysForwardedBits.setStatus("current")
_Dfl260SysForwardedPackets_Type = Counter32
_Dfl260SysForwardedPackets_Object = MibScalar
dfl260SysForwardedPackets = _Dfl260SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 3),
    _Dfl260SysForwardedPackets_Type()
)
dfl260SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysForwardedPackets.setStatus("current")
_Dfl260SysBuffUse_Type = Gauge32
_Dfl260SysBuffUse_Object = MibScalar
dfl260SysBuffUse = _Dfl260SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 4),
    _Dfl260SysBuffUse_Type()
)
dfl260SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysBuffUse.setStatus("current")
_Dfl260SysConns_Type = Gauge32
_Dfl260SysConns_Object = MibScalar
dfl260SysConns = _Dfl260SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 5),
    _Dfl260SysConns_Type()
)
dfl260SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysConns.setStatus("current")
_Dfl260SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl260SysPerStateCounters = _Dfl260SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6)
)
_Dfl260SysPscTcpSyn_Type = Gauge32
_Dfl260SysPscTcpSyn_Object = MibScalar
dfl260SysPscTcpSyn = _Dfl260SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6, 1),
    _Dfl260SysPscTcpSyn_Type()
)
dfl260SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysPscTcpSyn.setStatus("current")
_Dfl260SysPscTcpOpen_Type = Gauge32
_Dfl260SysPscTcpOpen_Object = MibScalar
dfl260SysPscTcpOpen = _Dfl260SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6, 2),
    _Dfl260SysPscTcpOpen_Type()
)
dfl260SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysPscTcpOpen.setStatus("current")
_Dfl260SysPscTcpFin_Type = Gauge32
_Dfl260SysPscTcpFin_Object = MibScalar
dfl260SysPscTcpFin = _Dfl260SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6, 3),
    _Dfl260SysPscTcpFin_Type()
)
dfl260SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysPscTcpFin.setStatus("current")
_Dfl260SysPscUdp_Type = Gauge32
_Dfl260SysPscUdp_Object = MibScalar
dfl260SysPscUdp = _Dfl260SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6, 4),
    _Dfl260SysPscUdp_Type()
)
dfl260SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysPscUdp.setStatus("current")
_Dfl260SysPscIcmp_Type = Gauge32
_Dfl260SysPscIcmp_Object = MibScalar
dfl260SysPscIcmp = _Dfl260SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6, 5),
    _Dfl260SysPscIcmp_Type()
)
dfl260SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysPscIcmp.setStatus("current")
_Dfl260SysPscOther_Type = Gauge32
_Dfl260SysPscOther_Object = MibScalar
dfl260SysPscOther = _Dfl260SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 6, 6),
    _Dfl260SysPscOther_Type()
)
dfl260SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysPscOther.setStatus("current")
_Dfl260IfStatsTable_Object = MibTable
dfl260IfStatsTable = _Dfl260IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl260IfStatsTable.setStatus("current")
_Dfl260IfStatsEntry_Object = MibTableRow
dfl260IfStatsEntry = _Dfl260IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1)
)
dfl260IfStatsEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl260IfStatsEntry.setStatus("current")


class _Dfl260IfStatsIndex_Type(Integer32):
    """Custom type dfl260IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260IfStatsIndex_Type.__name__ = "Integer32"
_Dfl260IfStatsIndex_Object = MibTableColumn
dfl260IfStatsIndex = _Dfl260IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 1),
    _Dfl260IfStatsIndex_Type()
)
dfl260IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260IfStatsIndex.setStatus("current")
_Dfl260IfName_Type = DisplayString
_Dfl260IfName_Object = MibTableColumn
dfl260IfName = _Dfl260IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 2),
    _Dfl260IfName_Type()
)
dfl260IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfName.setStatus("current")
_Dfl260IfFragsIn_Type = Counter32
_Dfl260IfFragsIn_Object = MibTableColumn
dfl260IfFragsIn = _Dfl260IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 3),
    _Dfl260IfFragsIn_Type()
)
dfl260IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfFragsIn.setStatus("current")
_Dfl260IfFragReassOk_Type = Counter32
_Dfl260IfFragReassOk_Object = MibTableColumn
dfl260IfFragReassOk = _Dfl260IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 4),
    _Dfl260IfFragReassOk_Type()
)
dfl260IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfFragReassOk.setStatus("current")
_Dfl260IfFragReassFail_Type = Counter32
_Dfl260IfFragReassFail_Object = MibTableColumn
dfl260IfFragReassFail = _Dfl260IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 5),
    _Dfl260IfFragReassFail_Type()
)
dfl260IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfFragReassFail.setStatus("current")
_Dfl260IfPktsInCnt_Type = Counter32
_Dfl260IfPktsInCnt_Object = MibTableColumn
dfl260IfPktsInCnt = _Dfl260IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 6),
    _Dfl260IfPktsInCnt_Type()
)
dfl260IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfPktsInCnt.setStatus("current")
_Dfl260IfPktsOutCnt_Type = Counter32
_Dfl260IfPktsOutCnt_Object = MibTableColumn
dfl260IfPktsOutCnt = _Dfl260IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 7),
    _Dfl260IfPktsOutCnt_Type()
)
dfl260IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfPktsOutCnt.setStatus("current")
_Dfl260IfBitsInCnt_Type = Counter32
_Dfl260IfBitsInCnt_Object = MibTableColumn
dfl260IfBitsInCnt = _Dfl260IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 8),
    _Dfl260IfBitsInCnt_Type()
)
dfl260IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfBitsInCnt.setStatus("current")
_Dfl260IfBitsOutCnt_Type = Counter32
_Dfl260IfBitsOutCnt_Object = MibTableColumn
dfl260IfBitsOutCnt = _Dfl260IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 9),
    _Dfl260IfBitsOutCnt_Type()
)
dfl260IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfBitsOutCnt.setStatus("current")
_Dfl260IfPktsTotCnt_Type = Counter32
_Dfl260IfPktsTotCnt_Object = MibTableColumn
dfl260IfPktsTotCnt = _Dfl260IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 10),
    _Dfl260IfPktsTotCnt_Type()
)
dfl260IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfPktsTotCnt.setStatus("current")
_Dfl260IfBitsTotCnt_Type = Counter32
_Dfl260IfBitsTotCnt_Object = MibTableColumn
dfl260IfBitsTotCnt = _Dfl260IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 11),
    _Dfl260IfBitsTotCnt_Type()
)
dfl260IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfBitsTotCnt.setStatus("current")
_Dfl260IfHCPktsInCnt_Type = Counter64
_Dfl260IfHCPktsInCnt_Object = MibTableColumn
dfl260IfHCPktsInCnt = _Dfl260IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 12),
    _Dfl260IfHCPktsInCnt_Type()
)
dfl260IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfHCPktsInCnt.setStatus("current")
_Dfl260IfHCPktsOutCnt_Type = Counter64
_Dfl260IfHCPktsOutCnt_Object = MibTableColumn
dfl260IfHCPktsOutCnt = _Dfl260IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 13),
    _Dfl260IfHCPktsOutCnt_Type()
)
dfl260IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfHCPktsOutCnt.setStatus("current")
_Dfl260IfHCBitsInCnt_Type = Counter64
_Dfl260IfHCBitsInCnt_Object = MibTableColumn
dfl260IfHCBitsInCnt = _Dfl260IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 14),
    _Dfl260IfHCBitsInCnt_Type()
)
dfl260IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfHCBitsInCnt.setStatus("current")
_Dfl260IfHCBitsOutCnt_Type = Counter64
_Dfl260IfHCBitsOutCnt_Object = MibTableColumn
dfl260IfHCBitsOutCnt = _Dfl260IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 15),
    _Dfl260IfHCBitsOutCnt_Type()
)
dfl260IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfHCBitsOutCnt.setStatus("current")
_Dfl260IfHCPktsTotCnt_Type = Counter64
_Dfl260IfHCPktsTotCnt_Object = MibTableColumn
dfl260IfHCPktsTotCnt = _Dfl260IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 16),
    _Dfl260IfHCPktsTotCnt_Type()
)
dfl260IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfHCPktsTotCnt.setStatus("current")
_Dfl260IfHCBitsTotCnt_Type = Counter64
_Dfl260IfHCBitsTotCnt_Object = MibTableColumn
dfl260IfHCBitsTotCnt = _Dfl260IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 7, 1, 17),
    _Dfl260IfHCBitsTotCnt_Type()
)
dfl260IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfHCBitsTotCnt.setStatus("current")
_Dfl260IfRxRingTable_Object = MibTable
dfl260IfRxRingTable = _Dfl260IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl260IfRxRingTable.setStatus("current")
_Dfl260IfRxRingEntry_Object = MibTableRow
dfl260IfRxRingEntry = _Dfl260IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1)
)
dfl260IfRxRingEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl260IfRxRingEntry.setStatus("current")


class _Dfl260IfRxRingIndex_Type(Integer32):
    """Custom type dfl260IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl260IfRxRingIndex_Object = MibTableColumn
dfl260IfRxRingIndex = _Dfl260IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1, 1),
    _Dfl260IfRxRingIndex_Type()
)
dfl260IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260IfRxRingIndex.setStatus("current")
_Dfl260IfRxRingFifoErrors_Type = Counter32
_Dfl260IfRxRingFifoErrors_Object = MibTableColumn
dfl260IfRxRingFifoErrors = _Dfl260IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1, 2),
    _Dfl260IfRxRingFifoErrors_Type()
)
dfl260IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfRxRingFifoErrors.setStatus("current")
_Dfl260IfRxDespools_Type = Gauge32
_Dfl260IfRxDespools_Object = MibTableColumn
dfl260IfRxDespools = _Dfl260IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1, 3),
    _Dfl260IfRxDespools_Type()
)
dfl260IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfRxDespools.setStatus("current")
_Dfl260IfRxAvgUse_Type = Gauge32
_Dfl260IfRxAvgUse_Object = MibTableColumn
dfl260IfRxAvgUse = _Dfl260IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1, 4),
    _Dfl260IfRxAvgUse_Type()
)
dfl260IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfRxAvgUse.setStatus("current")
_Dfl260IfRxRingSaturation_Type = Gauge32
_Dfl260IfRxRingSaturation_Object = MibTableColumn
dfl260IfRxRingSaturation = _Dfl260IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1, 5),
    _Dfl260IfRxRingSaturation_Type()
)
dfl260IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfRxRingSaturation.setStatus("current")
_Dfl260RxRingFlooded_Type = Gauge32
_Dfl260RxRingFlooded_Object = MibTableColumn
dfl260RxRingFlooded = _Dfl260RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 8, 1, 6),
    _Dfl260RxRingFlooded_Type()
)
dfl260RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260RxRingFlooded.setStatus("current")
_Dfl260IfTxRingTable_Object = MibTable
dfl260IfTxRingTable = _Dfl260IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl260IfTxRingTable.setStatus("current")
_Dfl260IfTxRingEntry_Object = MibTableRow
dfl260IfTxRingEntry = _Dfl260IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9, 1)
)
dfl260IfTxRingEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl260IfTxRingEntry.setStatus("current")


class _Dfl260IfTxRingIndex_Type(Integer32):
    """Custom type dfl260IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl260IfTxRingIndex_Object = MibTableColumn
dfl260IfTxRingIndex = _Dfl260IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9, 1, 1),
    _Dfl260IfTxRingIndex_Type()
)
dfl260IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260IfTxRingIndex.setStatus("current")
_Dfl260IfTxDespools_Type = Gauge32
_Dfl260IfTxDespools_Object = MibTableColumn
dfl260IfTxDespools = _Dfl260IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9, 1, 2),
    _Dfl260IfTxDespools_Type()
)
dfl260IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfTxDespools.setStatus("current")
_Dfl260IfTxAvgUse_Type = Gauge32
_Dfl260IfTxAvgUse_Object = MibTableColumn
dfl260IfTxAvgUse = _Dfl260IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9, 1, 3),
    _Dfl260IfTxAvgUse_Type()
)
dfl260IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfTxAvgUse.setStatus("current")
_Dfl260IfTxRingSaturation_Type = Gauge32
_Dfl260IfTxRingSaturation_Object = MibTableColumn
dfl260IfTxRingSaturation = _Dfl260IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9, 1, 4),
    _Dfl260IfTxRingSaturation_Type()
)
dfl260IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfTxRingSaturation.setStatus("current")
_Dfl260RxTingFlooded_Type = Gauge32
_Dfl260RxTingFlooded_Object = MibTableColumn
dfl260RxTingFlooded = _Dfl260RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 9, 1, 5),
    _Dfl260RxTingFlooded_Type()
)
dfl260RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260RxTingFlooded.setStatus("current")
_Dfl260IfVlanStatsTable_Object = MibTable
dfl260IfVlanStatsTable = _Dfl260IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl260IfVlanStatsTable.setStatus("current")
_Dfl260IfVlanStatsEntry_Object = MibTableRow
dfl260IfVlanStatsEntry = _Dfl260IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1)
)
dfl260IfVlanStatsEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl260IfVlanStatsEntry.setStatus("current")


class _Dfl260IfVlanIndex_Type(Integer32):
    """Custom type dfl260IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260IfVlanIndex_Type.__name__ = "Integer32"
_Dfl260IfVlanIndex_Object = MibTableColumn
dfl260IfVlanIndex = _Dfl260IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 1),
    _Dfl260IfVlanIndex_Type()
)
dfl260IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260IfVlanIndex.setStatus("current")
_Dfl260IfVlanUntaggedInPkts_Type = Counter32
_Dfl260IfVlanUntaggedInPkts_Object = MibTableColumn
dfl260IfVlanUntaggedInPkts = _Dfl260IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 2),
    _Dfl260IfVlanUntaggedInPkts_Type()
)
dfl260IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfVlanUntaggedInPkts.setStatus("current")
_Dfl260IfVlanUntaggedOutPkts_Type = Counter32
_Dfl260IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl260IfVlanUntaggedOutPkts = _Dfl260IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 3),
    _Dfl260IfVlanUntaggedOutPkts_Type()
)
dfl260IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfVlanUntaggedOutPkts.setStatus("current")
_Dfl260IfVlanUntaggedTotPkts_Type = Counter32
_Dfl260IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl260IfVlanUntaggedTotPkts = _Dfl260IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 4),
    _Dfl260IfVlanUntaggedTotPkts_Type()
)
dfl260IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfVlanUntaggedTotPkts.setStatus("current")
_Dfl260IfVlanUntaggedInOctets_Type = Counter32
_Dfl260IfVlanUntaggedInOctets_Object = MibTableColumn
dfl260IfVlanUntaggedInOctets = _Dfl260IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 5),
    _Dfl260IfVlanUntaggedInOctets_Type()
)
dfl260IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfVlanUntaggedInOctets.setStatus("current")
_Dfl260IfVlanUntaggedOutOctets_Type = Counter32
_Dfl260IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl260IfVlanUntaggedOutOctets = _Dfl260IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 6),
    _Dfl260IfVlanUntaggedOutOctets_Type()
)
dfl260IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfVlanUntaggedOutOctets.setStatus("current")
_Dfl260IfVlanUntaggedTotOctets_Type = Counter32
_Dfl260IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl260IfVlanUntaggedTotOctets = _Dfl260IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 10, 1, 7),
    _Dfl260IfVlanUntaggedTotOctets_Type()
)
dfl260IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IfVlanUntaggedTotOctets.setStatus("current")
_Dfl260HWSensorTable_Object = MibTable
dfl260HWSensorTable = _Dfl260HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl260HWSensorTable.setStatus("current")
_Dfl260HWSensorEntry_Object = MibTableRow
dfl260HWSensorEntry = _Dfl260HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 11, 1)
)
dfl260HWSensorEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl260HWSensorEntry.setStatus("current")


class _Dfl260HWSensorIndex_Type(Integer32):
    """Custom type dfl260HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260HWSensorIndex_Type.__name__ = "Integer32"
_Dfl260HWSensorIndex_Object = MibTableColumn
dfl260HWSensorIndex = _Dfl260HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 11, 1, 1),
    _Dfl260HWSensorIndex_Type()
)
dfl260HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260HWSensorIndex.setStatus("current")
_Dfl260HWSensorName_Type = DisplayString
_Dfl260HWSensorName_Object = MibTableColumn
dfl260HWSensorName = _Dfl260HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 11, 1, 2),
    _Dfl260HWSensorName_Type()
)
dfl260HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HWSensorName.setStatus("current")
_Dfl260HWSensorValue_Type = Gauge32
_Dfl260HWSensorValue_Object = MibTableColumn
dfl260HWSensorValue = _Dfl260HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 11, 1, 3),
    _Dfl260HWSensorValue_Type()
)
dfl260HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HWSensorValue.setStatus("current")
_Dfl260HWSensorUnit_Type = DisplayString
_Dfl260HWSensorUnit_Object = MibTableColumn
dfl260HWSensorUnit = _Dfl260HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 11, 1, 4),
    _Dfl260HWSensorUnit_Type()
)
dfl260HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HWSensorUnit.setStatus("current")
_Dfl260SysMemUsage_Type = Gauge32
_Dfl260SysMemUsage_Object = MibScalar
dfl260SysMemUsage = _Dfl260SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 12),
    _Dfl260SysMemUsage_Type()
)
dfl260SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysMemUsage.setStatus("current")
_Dfl260SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl260SysTCPUsage = _Dfl260SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 13)
)
_Dfl260SysTCPRecvSmall_Type = Gauge32
_Dfl260SysTCPRecvSmall_Object = MibScalar
dfl260SysTCPRecvSmall = _Dfl260SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 13, 1),
    _Dfl260SysTCPRecvSmall_Type()
)
dfl260SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysTCPRecvSmall.setStatus("current")
_Dfl260SysTCPRecvLarge_Type = Gauge32
_Dfl260SysTCPRecvLarge_Object = MibScalar
dfl260SysTCPRecvLarge = _Dfl260SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 13, 2),
    _Dfl260SysTCPRecvLarge_Type()
)
dfl260SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysTCPRecvLarge.setStatus("current")
_Dfl260SysTCPSendSmall_Type = Gauge32
_Dfl260SysTCPSendSmall_Object = MibScalar
dfl260SysTCPSendSmall = _Dfl260SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 13, 3),
    _Dfl260SysTCPSendSmall_Type()
)
dfl260SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysTCPSendSmall.setStatus("current")
_Dfl260SysTCPSendLarge_Type = Gauge32
_Dfl260SysTCPSendLarge_Object = MibScalar
dfl260SysTCPSendLarge = _Dfl260SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 13, 4),
    _Dfl260SysTCPSendLarge_Type()
)
dfl260SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysTCPSendLarge.setStatus("current")
_Dfl260SysTimerUsage_Type = Gauge32
_Dfl260SysTimerUsage_Object = MibScalar
dfl260SysTimerUsage = _Dfl260SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 14),
    _Dfl260SysTimerUsage_Type()
)
dfl260SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysTimerUsage.setStatus("current")
_Dfl260SysConnOPS_Type = Gauge32
_Dfl260SysConnOPS_Object = MibScalar
dfl260SysConnOPS = _Dfl260SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 15),
    _Dfl260SysConnOPS_Type()
)
dfl260SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysConnOPS.setStatus("current")
_Dfl260SysConnCPS_Type = Gauge32
_Dfl260SysConnCPS_Object = MibScalar
dfl260SysConnCPS = _Dfl260SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 16),
    _Dfl260SysConnCPS_Type()
)
dfl260SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysConnCPS.setStatus("current")
_Dfl260SysHCForwardedBits_Type = Counter64
_Dfl260SysHCForwardedBits_Object = MibScalar
dfl260SysHCForwardedBits = _Dfl260SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 1, 17),
    _Dfl260SysHCForwardedBits_Type()
)
dfl260SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SysHCForwardedBits.setStatus("current")
_Dfl260VPN_ObjectIdentity = ObjectIdentity
dfl260VPN = _Dfl260VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2)
)
_Dfl260IPsec_ObjectIdentity = ObjectIdentity
dfl260IPsec = _Dfl260IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1)
)
_Dfl260IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl260IPsecGlobal = _Dfl260IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1)
)
_Dfl260IPsecPhaseOneActive_Type = Gauge32
_Dfl260IPsecPhaseOneActive_Object = MibScalar
dfl260IPsecPhaseOneActive = _Dfl260IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 1),
    _Dfl260IPsecPhaseOneActive_Type()
)
dfl260IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecPhaseOneActive.setStatus("current")
_Dfl260IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl260IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl260IPsecPhaseOneAggrModeDone = _Dfl260IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 2),
    _Dfl260IPsecPhaseOneAggrModeDone_Type()
)
dfl260IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl260IPsecQuickModeActive_Type = Gauge32
_Dfl260IPsecQuickModeActive_Object = MibScalar
dfl260IPsecQuickModeActive = _Dfl260IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 3),
    _Dfl260IPsecQuickModeActive_Type()
)
dfl260IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecQuickModeActive.setStatus("current")
_Dfl260IPsecPhaseOneDone_Type = Counter32
_Dfl260IPsecPhaseOneDone_Object = MibScalar
dfl260IPsecPhaseOneDone = _Dfl260IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 4),
    _Dfl260IPsecPhaseOneDone_Type()
)
dfl260IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecPhaseOneDone.setStatus("current")
_Dfl260IPsecPhaseOneFailed_Type = Counter32
_Dfl260IPsecPhaseOneFailed_Object = MibScalar
dfl260IPsecPhaseOneFailed = _Dfl260IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 5),
    _Dfl260IPsecPhaseOneFailed_Type()
)
dfl260IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecPhaseOneFailed.setStatus("current")
_Dfl260IPsecPhaseOneRekeyed_Type = Counter32
_Dfl260IPsecPhaseOneRekeyed_Object = MibScalar
dfl260IPsecPhaseOneRekeyed = _Dfl260IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 6),
    _Dfl260IPsecPhaseOneRekeyed_Type()
)
dfl260IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecPhaseOneRekeyed.setStatus("current")
_Dfl260IPsecQuickModeDone_Type = Counter32
_Dfl260IPsecQuickModeDone_Object = MibScalar
dfl260IPsecQuickModeDone = _Dfl260IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 7),
    _Dfl260IPsecQuickModeDone_Type()
)
dfl260IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecQuickModeDone.setStatus("current")
_Dfl260IPsecQuickModeFailed_Type = Counter32
_Dfl260IPsecQuickModeFailed_Object = MibScalar
dfl260IPsecQuickModeFailed = _Dfl260IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 8),
    _Dfl260IPsecQuickModeFailed_Type()
)
dfl260IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecQuickModeFailed.setStatus("current")
_Dfl260IPsecInfoDone_Type = Counter32
_Dfl260IPsecInfoDone_Object = MibScalar
dfl260IPsecInfoDone = _Dfl260IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 9),
    _Dfl260IPsecInfoDone_Type()
)
dfl260IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecInfoDone.setStatus("current")
_Dfl260IPsecInfoFailed_Type = Counter32
_Dfl260IPsecInfoFailed_Object = MibScalar
dfl260IPsecInfoFailed = _Dfl260IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 10),
    _Dfl260IPsecInfoFailed_Type()
)
dfl260IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecInfoFailed.setStatus("current")
_Dfl260IPsecInOctetsComp_Type = Counter64
_Dfl260IPsecInOctetsComp_Object = MibScalar
dfl260IPsecInOctetsComp = _Dfl260IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 11),
    _Dfl260IPsecInOctetsComp_Type()
)
dfl260IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecInOctetsComp.setStatus("current")
_Dfl260IPsecInOctetsUncomp_Type = Counter64
_Dfl260IPsecInOctetsUncomp_Object = MibScalar
dfl260IPsecInOctetsUncomp = _Dfl260IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 12),
    _Dfl260IPsecInOctetsUncomp_Type()
)
dfl260IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecInOctetsUncomp.setStatus("current")
_Dfl260IPsecOutOctetsComp_Type = Counter64
_Dfl260IPsecOutOctetsComp_Object = MibScalar
dfl260IPsecOutOctetsComp = _Dfl260IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 13),
    _Dfl260IPsecOutOctetsComp_Type()
)
dfl260IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecOutOctetsComp.setStatus("current")
_Dfl260IPsecOutOctetsUncomp_Type = Counter64
_Dfl260IPsecOutOctetsUncomp_Object = MibScalar
dfl260IPsecOutOctetsUncomp = _Dfl260IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 14),
    _Dfl260IPsecOutOctetsUncomp_Type()
)
dfl260IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecOutOctetsUncomp.setStatus("current")
_Dfl260IPsecForwardedOctetsComp_Type = Counter64
_Dfl260IPsecForwardedOctetsComp_Object = MibScalar
dfl260IPsecForwardedOctetsComp = _Dfl260IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 15),
    _Dfl260IPsecForwardedOctetsComp_Type()
)
dfl260IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecForwardedOctetsComp.setStatus("current")
_Dfl260IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl260IPsecForwardedOctetsUcomp_Object = MibScalar
dfl260IPsecForwardedOctetsUcomp = _Dfl260IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 16),
    _Dfl260IPsecForwardedOctetsUcomp_Type()
)
dfl260IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl260IPsecInPackets_Type = Counter64
_Dfl260IPsecInPackets_Object = MibScalar
dfl260IPsecInPackets = _Dfl260IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 17),
    _Dfl260IPsecInPackets_Type()
)
dfl260IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecInPackets.setStatus("current")
_Dfl260IPsecOutPackets_Type = Counter64
_Dfl260IPsecOutPackets_Object = MibScalar
dfl260IPsecOutPackets = _Dfl260IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 18),
    _Dfl260IPsecOutPackets_Type()
)
dfl260IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecOutPackets.setStatus("current")
_Dfl260IPsecForwardedPackets_Type = Counter64
_Dfl260IPsecForwardedPackets_Object = MibScalar
dfl260IPsecForwardedPackets = _Dfl260IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 19),
    _Dfl260IPsecForwardedPackets_Type()
)
dfl260IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecForwardedPackets.setStatus("current")
_Dfl260IPsecActiveTransforms_Type = Gauge32
_Dfl260IPsecActiveTransforms_Object = MibScalar
dfl260IPsecActiveTransforms = _Dfl260IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 20),
    _Dfl260IPsecActiveTransforms_Type()
)
dfl260IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecActiveTransforms.setStatus("current")
_Dfl260IPsecTotalTransforms_Type = Counter32
_Dfl260IPsecTotalTransforms_Object = MibScalar
dfl260IPsecTotalTransforms = _Dfl260IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 21),
    _Dfl260IPsecTotalTransforms_Type()
)
dfl260IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecTotalTransforms.setStatus("current")
_Dfl260IPsecOutOfTransforms_Type = Counter32
_Dfl260IPsecOutOfTransforms_Object = MibScalar
dfl260IPsecOutOfTransforms = _Dfl260IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 22),
    _Dfl260IPsecOutOfTransforms_Type()
)
dfl260IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecOutOfTransforms.setStatus("current")
_Dfl260IPsecTotalRekeys_Type = Counter32
_Dfl260IPsecTotalRekeys_Object = MibScalar
dfl260IPsecTotalRekeys = _Dfl260IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 2, 1, 1, 23),
    _Dfl260IPsecTotalRekeys_Type()
)
dfl260IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPsecTotalRekeys.setStatus("current")
_Dfl260Rules_ObjectIdentity = ObjectIdentity
dfl260Rules = _Dfl260Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 3)
)
_Dfl260RuleUseTable_Object = MibTable
dfl260RuleUseTable = _Dfl260RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl260RuleUseTable.setStatus("current")
_Dfl260RuleUseEntry_Object = MibTableRow
dfl260RuleUseEntry = _Dfl260RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 3, 2, 1)
)
dfl260RuleUseEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260RuleUseEntry.setStatus("current")


class _Dfl260RuleIndex_Type(Integer32):
    """Custom type dfl260RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260RuleIndex_Type.__name__ = "Integer32"
_Dfl260RuleIndex_Object = MibTableColumn
dfl260RuleIndex = _Dfl260RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 3, 2, 1, 1),
    _Dfl260RuleIndex_Type()
)
dfl260RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260RuleIndex.setStatus("current")
_Dfl260RuleName_Type = DisplayString
_Dfl260RuleName_Object = MibTableColumn
dfl260RuleName = _Dfl260RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 3, 2, 1, 2),
    _Dfl260RuleName_Type()
)
dfl260RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260RuleName.setStatus("current")
_Dfl260RuleUse_Type = Counter32
_Dfl260RuleUse_Object = MibTableColumn
dfl260RuleUse = _Dfl260RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 3, 2, 1, 3),
    _Dfl260RuleUse_Type()
)
dfl260RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260RuleUse.setStatus("current")
_Dfl260IPPools_ObjectIdentity = ObjectIdentity
dfl260IPPools = _Dfl260IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4)
)
_Dfl260IPPoolsNumber_Type = Integer32
_Dfl260IPPoolsNumber_Object = MibScalar
dfl260IPPoolsNumber = _Dfl260IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 1),
    _Dfl260IPPoolsNumber_Type()
)
dfl260IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolsNumber.setStatus("current")
_Dfl260IPPoolTable_Object = MibTable
dfl260IPPoolTable = _Dfl260IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl260IPPoolTable.setStatus("current")
_Dfl260IPPoolEntry_Object = MibTableRow
dfl260IPPoolEntry = _Dfl260IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1)
)
dfl260IPPoolEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl260IPPoolEntry.setStatus("current")


class _Dfl260IPPoolIndex_Type(Integer32):
    """Custom type dfl260IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260IPPoolIndex_Type.__name__ = "Integer32"
_Dfl260IPPoolIndex_Object = MibTableColumn
dfl260IPPoolIndex = _Dfl260IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 1),
    _Dfl260IPPoolIndex_Type()
)
dfl260IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260IPPoolIndex.setStatus("current")
_Dfl260IPPoolName_Type = DisplayString
_Dfl260IPPoolName_Object = MibTableColumn
dfl260IPPoolName = _Dfl260IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 2),
    _Dfl260IPPoolName_Type()
)
dfl260IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolName.setStatus("current")
_Dfl260IPPoolPrepare_Type = Gauge32
_Dfl260IPPoolPrepare_Object = MibTableColumn
dfl260IPPoolPrepare = _Dfl260IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 3),
    _Dfl260IPPoolPrepare_Type()
)
dfl260IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolPrepare.setStatus("current")
_Dfl260IPPoolFree_Type = Gauge32
_Dfl260IPPoolFree_Object = MibTableColumn
dfl260IPPoolFree = _Dfl260IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 4),
    _Dfl260IPPoolFree_Type()
)
dfl260IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolFree.setStatus("current")
_Dfl260IPPoolMisses_Type = Gauge32
_Dfl260IPPoolMisses_Object = MibTableColumn
dfl260IPPoolMisses = _Dfl260IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 5),
    _Dfl260IPPoolMisses_Type()
)
dfl260IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolMisses.setStatus("current")
_Dfl260IPPoolClientFails_Type = Gauge32
_Dfl260IPPoolClientFails_Object = MibTableColumn
dfl260IPPoolClientFails = _Dfl260IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 6),
    _Dfl260IPPoolClientFails_Type()
)
dfl260IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolClientFails.setStatus("current")
_Dfl260IPPoolUsed_Type = Gauge32
_Dfl260IPPoolUsed_Object = MibTableColumn
dfl260IPPoolUsed = _Dfl260IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 4, 2, 1, 7),
    _Dfl260IPPoolUsed_Type()
)
dfl260IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260IPPoolUsed.setStatus("current")
_Dfl260DHCPServer_ObjectIdentity = ObjectIdentity
dfl260DHCPServer = _Dfl260DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5)
)
_Dfl260DHCPTotalRejected_Type = Gauge32
_Dfl260DHCPTotalRejected_Object = MibScalar
dfl260DHCPTotalRejected = _Dfl260DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 1),
    _Dfl260DHCPTotalRejected_Type()
)
dfl260DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPTotalRejected.setStatus("current")
_Dfl260DHCPRuleTable_Object = MibTable
dfl260DHCPRuleTable = _Dfl260DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl260DHCPRuleTable.setStatus("current")
_Dfl260DHCPRuleEntry_Object = MibTableRow
dfl260DHCPRuleEntry = _Dfl260DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1)
)
dfl260DHCPRuleEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260DHCPRuleEntry.setStatus("current")


class _Dfl260DHCPRuleIndex_Type(Integer32):
    """Custom type dfl260DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl260DHCPRuleIndex_Object = MibTableColumn
dfl260DHCPRuleIndex = _Dfl260DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 1),
    _Dfl260DHCPRuleIndex_Type()
)
dfl260DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260DHCPRuleIndex.setStatus("current")
_Dfl260DHCPRuleName_Type = DisplayString
_Dfl260DHCPRuleName_Object = MibTableColumn
dfl260DHCPRuleName = _Dfl260DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 2),
    _Dfl260DHCPRuleName_Type()
)
dfl260DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRuleName.setStatus("current")
_Dfl260DHCPRuleUsage_Type = Gauge32
_Dfl260DHCPRuleUsage_Object = MibTableColumn
dfl260DHCPRuleUsage = _Dfl260DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 3),
    _Dfl260DHCPRuleUsage_Type()
)
dfl260DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRuleUsage.setStatus("current")
_Dfl260DHCPRuleUsagePercent_Type = Gauge32
_Dfl260DHCPRuleUsagePercent_Object = MibTableColumn
dfl260DHCPRuleUsagePercent = _Dfl260DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 4),
    _Dfl260DHCPRuleUsagePercent_Type()
)
dfl260DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRuleUsagePercent.setStatus("current")
_Dfl260DHCPActiveClients_Type = Gauge32
_Dfl260DHCPActiveClients_Object = MibTableColumn
dfl260DHCPActiveClients = _Dfl260DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 5),
    _Dfl260DHCPActiveClients_Type()
)
dfl260DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPActiveClients.setStatus("current")
_Dfl260DHCPActiveClientsPercent_Type = Gauge32
_Dfl260DHCPActiveClientsPercent_Object = MibTableColumn
dfl260DHCPActiveClientsPercent = _Dfl260DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 6),
    _Dfl260DHCPActiveClientsPercent_Type()
)
dfl260DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPActiveClientsPercent.setStatus("current")
_Dfl260DHCPRejectedRequests_Type = Gauge32
_Dfl260DHCPRejectedRequests_Object = MibTableColumn
dfl260DHCPRejectedRequests = _Dfl260DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 7),
    _Dfl260DHCPRejectedRequests_Type()
)
dfl260DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRejectedRequests.setStatus("current")
_Dfl260DHCPTotalLeases_Type = Gauge32
_Dfl260DHCPTotalLeases_Object = MibTableColumn
dfl260DHCPTotalLeases = _Dfl260DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 5, 2, 1, 8),
    _Dfl260DHCPTotalLeases_Type()
)
dfl260DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPTotalLeases.setStatus("current")
_Dfl260UserAuth_ObjectIdentity = ObjectIdentity
dfl260UserAuth = _Dfl260UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6)
)
_Dfl260UserAuthHTTPUsers_Type = Gauge32
_Dfl260UserAuthHTTPUsers_Object = MibScalar
dfl260UserAuthHTTPUsers = _Dfl260UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 1),
    _Dfl260UserAuthHTTPUsers_Type()
)
dfl260UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthHTTPUsers.setStatus("current")
_Dfl260UserAuthXAUTHUsers_Type = Gauge32
_Dfl260UserAuthXAUTHUsers_Object = MibScalar
dfl260UserAuthXAUTHUsers = _Dfl260UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 2),
    _Dfl260UserAuthXAUTHUsers_Type()
)
dfl260UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthXAUTHUsers.setStatus("current")
_Dfl260UserAuthHTTPSUsers_Type = Gauge32
_Dfl260UserAuthHTTPSUsers_Object = MibScalar
dfl260UserAuthHTTPSUsers = _Dfl260UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 3),
    _Dfl260UserAuthHTTPSUsers_Type()
)
dfl260UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthHTTPSUsers.setStatus("current")
_Dfl260UserAuthPPPUsers_Type = Gauge32
_Dfl260UserAuthPPPUsers_Object = MibScalar
dfl260UserAuthPPPUsers = _Dfl260UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 4),
    _Dfl260UserAuthPPPUsers_Type()
)
dfl260UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthPPPUsers.setStatus("current")
_Dfl260UserAuthEAPUsers_Type = Gauge32
_Dfl260UserAuthEAPUsers_Object = MibScalar
dfl260UserAuthEAPUsers = _Dfl260UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 5),
    _Dfl260UserAuthEAPUsers_Type()
)
dfl260UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthEAPUsers.setStatus("current")
_Dfl260UserAuthRuleUseTable_Object = MibTable
dfl260UserAuthRuleUseTable = _Dfl260UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl260UserAuthRuleUseTable.setStatus("current")
_Dfl260UserAuthRuleUseEntry_Object = MibTableRow
dfl260UserAuthRuleUseEntry = _Dfl260UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 6, 1)
)
dfl260UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260UserAuthRuleUseEntry.setStatus("current")


class _Dfl260UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl260UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl260UserAuthRuleIndex_Object = MibTableColumn
dfl260UserAuthRuleIndex = _Dfl260UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 6, 1, 1),
    _Dfl260UserAuthRuleIndex_Type()
)
dfl260UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260UserAuthRuleIndex.setStatus("current")
_Dfl260UserAuthRuleName_Type = DisplayString
_Dfl260UserAuthRuleName_Object = MibTableColumn
dfl260UserAuthRuleName = _Dfl260UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 6, 1, 2),
    _Dfl260UserAuthRuleName_Type()
)
dfl260UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthRuleName.setStatus("current")
_Dfl260UserAuthRuleUse_Type = Counter32
_Dfl260UserAuthRuleUse_Object = MibTableColumn
dfl260UserAuthRuleUse = _Dfl260UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 6, 6, 1, 3),
    _Dfl260UserAuthRuleUse_Type()
)
dfl260UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260UserAuthRuleUse.setStatus("current")
_Dfl260LinkMonitor_ObjectIdentity = ObjectIdentity
dfl260LinkMonitor = _Dfl260LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7)
)
_Dfl260LinkMonGrp_Type = Integer32
_Dfl260LinkMonGrp_Object = MibScalar
dfl260LinkMonGrp = _Dfl260LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 1),
    _Dfl260LinkMonGrp_Type()
)
dfl260LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260LinkMonGrp.setStatus("current")
_Dfl260LinkMonGrpTable_Object = MibTable
dfl260LinkMonGrpTable = _Dfl260LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl260LinkMonGrpTable.setStatus("current")
_Dfl260LinkMonGrpEntry_Object = MibTableRow
dfl260LinkMonGrpEntry = _Dfl260LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 2, 1)
)
dfl260LinkMonGrpEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl260LinkMonGrpEntry.setStatus("current")


class _Dfl260LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl260LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl260LinkMonGrpIndex_Object = MibTableColumn
dfl260LinkMonGrpIndex = _Dfl260LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 2, 1, 1),
    _Dfl260LinkMonGrpIndex_Type()
)
dfl260LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260LinkMonGrpIndex.setStatus("current")
_Dfl260LinkMonGrpName_Type = DisplayString
_Dfl260LinkMonGrpName_Object = MibTableColumn
dfl260LinkMonGrpName = _Dfl260LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 2, 1, 2),
    _Dfl260LinkMonGrpName_Type()
)
dfl260LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260LinkMonGrpName.setStatus("current")
_Dfl260LinkMonGrpHostsUp_Type = Gauge32
_Dfl260LinkMonGrpHostsUp_Object = MibTableColumn
dfl260LinkMonGrpHostsUp = _Dfl260LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 2, 1, 3),
    _Dfl260LinkMonGrpHostsUp_Type()
)
dfl260LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260LinkMonGrpHostsUp.setStatus("current")
_Dfl260LinkMonHostTable_Object = MibTable
dfl260LinkMonHostTable = _Dfl260LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl260LinkMonHostTable.setStatus("current")
_Dfl260LinkMonHostEntry_Object = MibTableRow
dfl260LinkMonHostEntry = _Dfl260LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 3, 1)
)
dfl260LinkMonHostEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260LinkMonGrpIndex"),
    (0, "DFL260-MIB", "dfl260LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl260LinkMonHostEntry.setStatus("current")


class _Dfl260LinkMonHostIndex_Type(Integer32):
    """Custom type dfl260LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl260LinkMonHostIndex_Object = MibTableColumn
dfl260LinkMonHostIndex = _Dfl260LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 3, 1, 1),
    _Dfl260LinkMonHostIndex_Type()
)
dfl260LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260LinkMonHostIndex.setStatus("current")
_Dfl260LinkMonHostId_Type = DisplayString
_Dfl260LinkMonHostId_Object = MibTableColumn
dfl260LinkMonHostId = _Dfl260LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 3, 1, 2),
    _Dfl260LinkMonHostId_Type()
)
dfl260LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260LinkMonHostId.setStatus("current")
_Dfl260LinkMonHostShortTermLoss_Type = Gauge32
_Dfl260LinkMonHostShortTermLoss_Object = MibTableColumn
dfl260LinkMonHostShortTermLoss = _Dfl260LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 3, 1, 3),
    _Dfl260LinkMonHostShortTermLoss_Type()
)
dfl260LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260LinkMonHostShortTermLoss.setStatus("current")
_Dfl260LinkMonHostPacketsLost_Type = Counter32
_Dfl260LinkMonHostPacketsLost_Object = MibTableColumn
dfl260LinkMonHostPacketsLost = _Dfl260LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 7, 3, 1, 4),
    _Dfl260LinkMonHostPacketsLost_Type()
)
dfl260LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260LinkMonHostPacketsLost.setStatus("current")
_Dfl260Pipes_ObjectIdentity = ObjectIdentity
dfl260Pipes = _Dfl260Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8)
)
_Dfl260PipeUsers_Type = Gauge32
_Dfl260PipeUsers_Object = MibScalar
dfl260PipeUsers = _Dfl260PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 1),
    _Dfl260PipeUsers_Type()
)
dfl260PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeUsers.setStatus("current")
_Dfl260PipeTable_Object = MibTable
dfl260PipeTable = _Dfl260PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl260PipeTable.setStatus("current")
_Dfl260PipeEntry_Object = MibTableRow
dfl260PipeEntry = _Dfl260PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1)
)
dfl260PipeEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl260PipeEntry.setStatus("current")


class _Dfl260PipeIndex_Type(Integer32):
    """Custom type dfl260PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260PipeIndex_Type.__name__ = "Integer32"
_Dfl260PipeIndex_Object = MibTableColumn
dfl260PipeIndex = _Dfl260PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 1),
    _Dfl260PipeIndex_Type()
)
dfl260PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260PipeIndex.setStatus("current")
_Dfl260PipeName_Type = DisplayString
_Dfl260PipeName_Object = MibTableColumn
dfl260PipeName = _Dfl260PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 2),
    _Dfl260PipeName_Type()
)
dfl260PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeName.setStatus("current")
_Dfl260PipeMinPrec_Type = Integer32
_Dfl260PipeMinPrec_Object = MibTableColumn
dfl260PipeMinPrec = _Dfl260PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 3),
    _Dfl260PipeMinPrec_Type()
)
dfl260PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeMinPrec.setStatus("current")
_Dfl260PipeMaxPrec_Type = Integer32
_Dfl260PipeMaxPrec_Object = MibTableColumn
dfl260PipeMaxPrec = _Dfl260PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 4),
    _Dfl260PipeMaxPrec_Type()
)
dfl260PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeMaxPrec.setStatus("current")
_Dfl260PipeDefPrec_Type = Integer32
_Dfl260PipeDefPrec_Object = MibTableColumn
dfl260PipeDefPrec = _Dfl260PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 5),
    _Dfl260PipeDefPrec_Type()
)
dfl260PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeDefPrec.setStatus("current")
_Dfl260PipeNumPrec_Type = Integer32
_Dfl260PipeNumPrec_Object = MibTableColumn
dfl260PipeNumPrec = _Dfl260PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 6),
    _Dfl260PipeNumPrec_Type()
)
dfl260PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeNumPrec.setStatus("current")
_Dfl260PipeNumUsers_Type = Gauge32
_Dfl260PipeNumUsers_Object = MibTableColumn
dfl260PipeNumUsers = _Dfl260PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 7),
    _Dfl260PipeNumUsers_Type()
)
dfl260PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeNumUsers.setStatus("current")
_Dfl260PipeCurrentBps_Type = Gauge32
_Dfl260PipeCurrentBps_Object = MibTableColumn
dfl260PipeCurrentBps = _Dfl260PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 8),
    _Dfl260PipeCurrentBps_Type()
)
dfl260PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeCurrentBps.setStatus("current")
_Dfl260PipeCurrentPps_Type = Gauge32
_Dfl260PipeCurrentPps_Object = MibTableColumn
dfl260PipeCurrentPps = _Dfl260PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 9),
    _Dfl260PipeCurrentPps_Type()
)
dfl260PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeCurrentPps.setStatus("current")
_Dfl260PipeDelayedPackets_Type = Counter32
_Dfl260PipeDelayedPackets_Object = MibTableColumn
dfl260PipeDelayedPackets = _Dfl260PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 10),
    _Dfl260PipeDelayedPackets_Type()
)
dfl260PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeDelayedPackets.setStatus("current")
_Dfl260PipeDropedPackets_Type = Counter32
_Dfl260PipeDropedPackets_Object = MibTableColumn
dfl260PipeDropedPackets = _Dfl260PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 2, 1, 11),
    _Dfl260PipeDropedPackets_Type()
)
dfl260PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipeDropedPackets.setStatus("current")
_Dfl260PipePrecTable_Object = MibTable
dfl260PipePrecTable = _Dfl260PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl260PipePrecTable.setStatus("current")
_Dfl260PipePrecEntry_Object = MibTableRow
dfl260PipePrecEntry = _Dfl260PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1)
)
dfl260PipePrecEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260PipeIndex"),
    (0, "DFL260-MIB", "dfl260PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl260PipePrecEntry.setStatus("current")


class _Dfl260PipePrecIndex_Type(Integer32):
    """Custom type dfl260PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260PipePrecIndex_Type.__name__ = "Integer32"
_Dfl260PipePrecIndex_Object = MibTableColumn
dfl260PipePrecIndex = _Dfl260PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 1),
    _Dfl260PipePrecIndex_Type()
)
dfl260PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260PipePrecIndex.setStatus("current")
_Dfl260PipePrec_Type = Integer32
_Dfl260PipePrec_Object = MibTableColumn
dfl260PipePrec = _Dfl260PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 2),
    _Dfl260PipePrec_Type()
)
dfl260PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrec.setStatus("current")
_Dfl260PipePrecBps_Type = Gauge32
_Dfl260PipePrecBps_Object = MibTableColumn
dfl260PipePrecBps = _Dfl260PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 3),
    _Dfl260PipePrecBps_Type()
)
dfl260PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecBps.setStatus("current")
_Dfl260PipePrecTotalPps_Type = Gauge32
_Dfl260PipePrecTotalPps_Object = MibTableColumn
dfl260PipePrecTotalPps = _Dfl260PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 4),
    _Dfl260PipePrecTotalPps_Type()
)
dfl260PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecTotalPps.setStatus("current")
_Dfl260PipePrecReservedBps_Type = Gauge32
_Dfl260PipePrecReservedBps_Object = MibTableColumn
dfl260PipePrecReservedBps = _Dfl260PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 5),
    _Dfl260PipePrecReservedBps_Type()
)
dfl260PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecReservedBps.setStatus("current")
_Dfl260PipePrecDynLimBps_Type = Gauge32
_Dfl260PipePrecDynLimBps_Object = MibTableColumn
dfl260PipePrecDynLimBps = _Dfl260PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 6),
    _Dfl260PipePrecDynLimBps_Type()
)
dfl260PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecDynLimBps.setStatus("current")
_Dfl260PipePrecDynUsrLimBps_Type = Gauge32
_Dfl260PipePrecDynUsrLimBps_Object = MibTableColumn
dfl260PipePrecDynUsrLimBps = _Dfl260PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 7),
    _Dfl260PipePrecDynUsrLimBps_Type()
)
dfl260PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecDynUsrLimBps.setStatus("current")
_Dfl260PipePrecDelayedPackets_Type = Counter32
_Dfl260PipePrecDelayedPackets_Object = MibTableColumn
dfl260PipePrecDelayedPackets = _Dfl260PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 8),
    _Dfl260PipePrecDelayedPackets_Type()
)
dfl260PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecDelayedPackets.setStatus("current")
_Dfl260PipePrecDropedPackets_Type = Counter32
_Dfl260PipePrecDropedPackets_Object = MibTableColumn
dfl260PipePrecDropedPackets = _Dfl260PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 8, 3, 1, 9),
    _Dfl260PipePrecDropedPackets_Type()
)
dfl260PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260PipePrecDropedPackets.setStatus("current")
_Dfl260ALG_ObjectIdentity = ObjectIdentity
dfl260ALG = _Dfl260ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9)
)
_Dfl260AlgSessions_Type = Gauge32
_Dfl260AlgSessions_Object = MibScalar
dfl260AlgSessions = _Dfl260AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 1),
    _Dfl260AlgSessions_Type()
)
dfl260AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260AlgSessions.setStatus("current")
_Dfl260AlgConnections_Type = Gauge32
_Dfl260AlgConnections_Object = MibScalar
dfl260AlgConnections = _Dfl260AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 2),
    _Dfl260AlgConnections_Type()
)
dfl260AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260AlgConnections.setStatus("current")
_Dfl260AlgTCPStreams_Type = Gauge32
_Dfl260AlgTCPStreams_Object = MibScalar
dfl260AlgTCPStreams = _Dfl260AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 3),
    _Dfl260AlgTCPStreams_Type()
)
dfl260AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260AlgTCPStreams.setStatus("current")
_Dfl260HttpAlg_ObjectIdentity = ObjectIdentity
dfl260HttpAlg = _Dfl260HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4)
)
_Dfl260HttpAlgTable_Object = MibTable
dfl260HttpAlgTable = _Dfl260HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl260HttpAlgTable.setStatus("current")
_Dfl260HttpAlgEntry_Object = MibTableRow
dfl260HttpAlgEntry = _Dfl260HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1, 1)
)
dfl260HttpAlgEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl260HttpAlgEntry.setStatus("current")


class _Dfl260HttpAlgIndex_Type(Integer32):
    """Custom type dfl260HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl260HttpAlgIndex_Object = MibTableColumn
dfl260HttpAlgIndex = _Dfl260HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1, 1, 1),
    _Dfl260HttpAlgIndex_Type()
)
dfl260HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260HttpAlgIndex.setStatus("current")
_Dfl260HttpAlgName_Type = DisplayString
_Dfl260HttpAlgName_Object = MibTableColumn
dfl260HttpAlgName = _Dfl260HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1, 1, 2),
    _Dfl260HttpAlgName_Type()
)
dfl260HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgName.setStatus("current")
_Dfl260HttpAlgTotalRequested_Type = Gauge32
_Dfl260HttpAlgTotalRequested_Object = MibTableColumn
dfl260HttpAlgTotalRequested = _Dfl260HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1, 1, 3),
    _Dfl260HttpAlgTotalRequested_Type()
)
dfl260HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgTotalRequested.setStatus("current")
_Dfl260HttpAlgTotalAllowed_Type = Gauge32
_Dfl260HttpAlgTotalAllowed_Object = MibTableColumn
dfl260HttpAlgTotalAllowed = _Dfl260HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1, 1, 4),
    _Dfl260HttpAlgTotalAllowed_Type()
)
dfl260HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgTotalAllowed.setStatus("current")
_Dfl260HttpAlgTotalBlocked_Type = Gauge32
_Dfl260HttpAlgTotalBlocked_Object = MibTableColumn
dfl260HttpAlgTotalBlocked = _Dfl260HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 1, 1, 5),
    _Dfl260HttpAlgTotalBlocked_Type()
)
dfl260HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgTotalBlocked.setStatus("current")
_Dfl260HttpAlgCntFltTable_Object = MibTable
dfl260HttpAlgCntFltTable = _Dfl260HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltTable.setStatus("current")
_Dfl260HttpAlgCntFltEntry_Object = MibTableRow
dfl260HttpAlgCntFltEntry = _Dfl260HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2, 1)
)
dfl260HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260HttpAlgIndex"),
    (0, "DFL260-MIB", "dfl260HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltEntry.setStatus("current")


class _Dfl260HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl260HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl260HttpAlgCntFltIndex_Object = MibTableColumn
dfl260HttpAlgCntFltIndex = _Dfl260HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2, 1, 1),
    _Dfl260HttpAlgCntFltIndex_Type()
)
dfl260HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltIndex.setStatus("current")
_Dfl260HttpAlgCntFltName_Type = DisplayString
_Dfl260HttpAlgCntFltName_Object = MibTableColumn
dfl260HttpAlgCntFltName = _Dfl260HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2, 1, 2),
    _Dfl260HttpAlgCntFltName_Type()
)
dfl260HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltName.setStatus("current")
_Dfl260HttpAlgCntFltRequests_Type = Gauge32
_Dfl260HttpAlgCntFltRequests_Object = MibTableColumn
dfl260HttpAlgCntFltRequests = _Dfl260HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2, 1, 3),
    _Dfl260HttpAlgCntFltRequests_Type()
)
dfl260HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltRequests.setStatus("current")
_Dfl260HttpAlgCntFltAllowed_Type = Gauge32
_Dfl260HttpAlgCntFltAllowed_Object = MibTableColumn
dfl260HttpAlgCntFltAllowed = _Dfl260HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2, 1, 4),
    _Dfl260HttpAlgCntFltAllowed_Type()
)
dfl260HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltAllowed.setStatus("current")
_Dfl260HttpAlgCntFltBlocked_Type = Gauge32
_Dfl260HttpAlgCntFltBlocked_Object = MibTableColumn
dfl260HttpAlgCntFltBlocked = _Dfl260HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 4, 2, 1, 5),
    _Dfl260HttpAlgCntFltBlocked_Type()
)
dfl260HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HttpAlgCntFltBlocked.setStatus("current")
_Dfl260SmtpAlg_ObjectIdentity = ObjectIdentity
dfl260SmtpAlg = _Dfl260SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5)
)
_Dfl260SmtpAlgTable_Object = MibTable
dfl260SmtpAlgTable = _Dfl260SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl260SmtpAlgTable.setStatus("current")
_Dfl260SmtpAlgEntry_Object = MibTableRow
dfl260SmtpAlgEntry = _Dfl260SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1, 1)
)
dfl260SmtpAlgEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl260SmtpAlgEntry.setStatus("current")


class _Dfl260SmtpAlgIndex_Type(Integer32):
    """Custom type dfl260SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl260SmtpAlgIndex_Object = MibTableColumn
dfl260SmtpAlgIndex = _Dfl260SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1, 1, 1),
    _Dfl260SmtpAlgIndex_Type()
)
dfl260SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260SmtpAlgIndex.setStatus("current")
_Dfl260SmtpAlgName_Type = DisplayString
_Dfl260SmtpAlgName_Object = MibTableColumn
dfl260SmtpAlgName = _Dfl260SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1, 1, 2),
    _Dfl260SmtpAlgName_Type()
)
dfl260SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgName.setStatus("current")
_Dfl260SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl260SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl260SmtpAlgTotCheckedSes = _Dfl260SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1, 1, 3),
    _Dfl260SmtpAlgTotCheckedSes_Type()
)
dfl260SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgTotCheckedSes.setStatus("current")
_Dfl260SmtpAlgTotSpamSes_Type = Gauge32
_Dfl260SmtpAlgTotSpamSes_Object = MibTableColumn
dfl260SmtpAlgTotSpamSes = _Dfl260SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1, 1, 4),
    _Dfl260SmtpAlgTotSpamSes_Type()
)
dfl260SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgTotSpamSes.setStatus("current")
_Dfl260SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl260SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl260SmtpAlgTotDroppedSes = _Dfl260SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 1, 1, 5),
    _Dfl260SmtpAlgTotDroppedSes_Type()
)
dfl260SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgTotDroppedSes.setStatus("current")
_Dfl260SmtpAlgDnsBlTable_Object = MibTable
dfl260SmtpAlgDnsBlTable = _Dfl260SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlTable.setStatus("current")
_Dfl260SmtpAlgDnsBlEntry_Object = MibTableRow
dfl260SmtpAlgDnsBlEntry = _Dfl260SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2, 1)
)
dfl260SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260SmtpAlgIndex"),
    (0, "DFL260-MIB", "dfl260SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl260SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl260SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl260SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl260SmtpAlgDnsBlIndex = _Dfl260SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2, 1, 1),
    _Dfl260SmtpAlgDnsBlIndex_Type()
)
dfl260SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlIndex.setStatus("current")
_Dfl260SmtpAlgDnsBlName_Type = DisplayString
_Dfl260SmtpAlgDnsBlName_Object = MibTableColumn
dfl260SmtpAlgDnsBlName = _Dfl260SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2, 1, 2),
    _Dfl260SmtpAlgDnsBlName_Type()
)
dfl260SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlName.setStatus("current")
_Dfl260SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl260SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl260SmtpAlgDnsBlChecked = _Dfl260SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2, 1, 3),
    _Dfl260SmtpAlgDnsBlChecked_Type()
)
dfl260SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlChecked.setStatus("current")
_Dfl260SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl260SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl260SmtpAlgDnsBlMatched = _Dfl260SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2, 1, 4),
    _Dfl260SmtpAlgDnsBlMatched_Type()
)
dfl260SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlMatched.setStatus("current")
_Dfl260SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl260SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl260SmtpAlgDnsBlFailChecks = _Dfl260SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 9, 5, 2, 1, 5),
    _Dfl260SmtpAlgDnsBlFailChecks_Type()
)
dfl260SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl260DHCPRelay_ObjectIdentity = ObjectIdentity
dfl260DHCPRelay = _Dfl260DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11)
)
_Dfl260DHCPRelayCurClients_Type = Gauge32
_Dfl260DHCPRelayCurClients_Object = MibScalar
dfl260DHCPRelayCurClients = _Dfl260DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 1),
    _Dfl260DHCPRelayCurClients_Type()
)
dfl260DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayCurClients.setStatus("current")
_Dfl260DHCPRelayCurTrans_Type = Gauge32
_Dfl260DHCPRelayCurTrans_Object = MibScalar
dfl260DHCPRelayCurTrans = _Dfl260DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 2),
    _Dfl260DHCPRelayCurTrans_Type()
)
dfl260DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayCurTrans.setStatus("current")
_Dfl260DHCPRelayRejected_Type = Gauge32
_Dfl260DHCPRelayRejected_Object = MibScalar
dfl260DHCPRelayRejected = _Dfl260DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 3),
    _Dfl260DHCPRelayRejected_Type()
)
dfl260DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRejected.setStatus("current")
_Dfl260DHCPRelayRuleTable_Object = MibTable
dfl260DHCPRelayRuleTable = _Dfl260DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleTable.setStatus("current")
_Dfl260DHCPRelayRuleEntry_Object = MibTableRow
dfl260DHCPRelayRuleEntry = _Dfl260DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1)
)
dfl260DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL260-MIB", "dfl260DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleEntry.setStatus("current")


class _Dfl260DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl260DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl260DHCPRelayRuleIndex_Object = MibTableColumn
dfl260DHCPRelayRuleIndex = _Dfl260DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1, 1),
    _Dfl260DHCPRelayRuleIndex_Type()
)
dfl260DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleIndex.setStatus("current")
_Dfl260DHCPRelayRuleName_Type = DisplayString
_Dfl260DHCPRelayRuleName_Object = MibTableColumn
dfl260DHCPRelayRuleName = _Dfl260DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1, 2),
    _Dfl260DHCPRelayRuleName_Type()
)
dfl260DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleName.setStatus("current")
_Dfl260DHCPRelayRuleHits_Type = Gauge32
_Dfl260DHCPRelayRuleHits_Object = MibTableColumn
dfl260DHCPRelayRuleHits = _Dfl260DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1, 3),
    _Dfl260DHCPRelayRuleHits_Type()
)
dfl260DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleHits.setStatus("current")
_Dfl260DHCPRelayRuleCurClients_Type = Gauge32
_Dfl260DHCPRelayRuleCurClients_Object = MibTableColumn
dfl260DHCPRelayRuleCurClients = _Dfl260DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1, 4),
    _Dfl260DHCPRelayRuleCurClients_Type()
)
dfl260DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleCurClients.setStatus("current")
_Dfl260DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl260DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl260DHCPRelayRuleRejCliPkts = _Dfl260DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1, 5),
    _Dfl260DHCPRelayRuleRejCliPkts_Type()
)
dfl260DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl260DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl260DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl260DHCPRelayRuleRejSrvPkts = _Dfl260DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 11, 4, 1, 6),
    _Dfl260DHCPRelayRuleRejSrvPkts_Type()
)
dfl260DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl260HA_ObjectIdentity = ObjectIdentity
dfl260HA = _Dfl260HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 12)
)
_Dfl260HASyncSendQueueLength_Type = Gauge32
_Dfl260HASyncSendQueueLength_Object = MibScalar
dfl260HASyncSendQueueLength = _Dfl260HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 12, 1),
    _Dfl260HASyncSendQueueLength_Type()
)
dfl260HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HASyncSendQueueLength.setStatus("current")
_Dfl260HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl260HASyncSendQueueUsagePkt_Object = MibScalar
dfl260HASyncSendQueueUsagePkt = _Dfl260HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 12, 2),
    _Dfl260HASyncSendQueueUsagePkt_Type()
)
dfl260HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HASyncSendQueueUsagePkt.setStatus("current")
_Dfl260HASyncSendQueueUsageOct_Type = Gauge32
_Dfl260HASyncSendQueueUsageOct_Object = MibScalar
dfl260HASyncSendQueueUsageOct = _Dfl260HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 12, 3),
    _Dfl260HASyncSendQueueUsageOct_Type()
)
dfl260HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HASyncSendQueueUsageOct.setStatus("current")
_Dfl260HASyncSentPackets_Type = Counter32
_Dfl260HASyncSentPackets_Object = MibScalar
dfl260HASyncSentPackets = _Dfl260HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 12, 4),
    _Dfl260HASyncSentPackets_Type()
)
dfl260HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HASyncSentPackets.setStatus("current")
_Dfl260HASyncSendResentPackets_Type = Counter32
_Dfl260HASyncSendResentPackets_Object = MibScalar
dfl260HASyncSendResentPackets = _Dfl260HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 1, 2, 12, 5),
    _Dfl260HASyncSendResentPackets_Type()
)
dfl260HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260HASyncSendResentPackets.setStatus("current")
_Dfl260reg_ObjectIdentity = ObjectIdentity
dfl260reg = _Dfl260reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2)
)
_Dfl260MibModules_ObjectIdentity = ObjectIdentity
dfl260MibModules = _Dfl260MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 1)
)
_Dfl260MibConfs_ObjectIdentity = ObjectIdentity
dfl260MibConfs = _Dfl260MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 2)
)
_Dfl260StatsConformance_ObjectIdentity = ObjectIdentity
dfl260StatsConformance = _Dfl260StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 2, 1)
)
_Dfl260MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl260MibObjectGroups = _Dfl260MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3)
)
_Dfl260StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl260StatsRegGroups = _Dfl260StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1)
)

# Managed Objects groups

dfl260SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 1)
)
dfl260SystemObjectGroup.setObjects(
      *(("DFL260-MIB", "dfl260SysCpuLoad"),
        ("DFL260-MIB", "dfl260SysForwardedBits"),
        ("DFL260-MIB", "dfl260SysForwardedPackets"),
        ("DFL260-MIB", "dfl260SysBuffUse"),
        ("DFL260-MIB", "dfl260SysConns"),
        ("DFL260-MIB", "dfl260HWSensorName"),
        ("DFL260-MIB", "dfl260HWSensorValue"),
        ("DFL260-MIB", "dfl260HWSensorUnit"),
        ("DFL260-MIB", "dfl260SysMemUsage"),
        ("DFL260-MIB", "dfl260SysTimerUsage"),
        ("DFL260-MIB", "dfl260SysConnOPS"),
        ("DFL260-MIB", "dfl260SysConnCPS"),
        ("DFL260-MIB", "dfl260SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl260SystemObjectGroup.setStatus("current")

dfl260IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 2)
)
dfl260IPsecObjectGroup.setObjects(
      *(("DFL260-MIB", "dfl260IPsecPhaseOneActive"),
        ("DFL260-MIB", "dfl260IPsecPhaseOneAggrModeDone"),
        ("DFL260-MIB", "dfl260IPsecQuickModeActive"),
        ("DFL260-MIB", "dfl260IPsecPhaseOneDone"),
        ("DFL260-MIB", "dfl260IPsecPhaseOneFailed"),
        ("DFL260-MIB", "dfl260IPsecPhaseOneRekeyed"),
        ("DFL260-MIB", "dfl260IPsecQuickModeDone"),
        ("DFL260-MIB", "dfl260IPsecQuickModeFailed"),
        ("DFL260-MIB", "dfl260IPsecInfoDone"),
        ("DFL260-MIB", "dfl260IPsecInfoFailed"),
        ("DFL260-MIB", "dfl260IPsecInOctetsComp"),
        ("DFL260-MIB", "dfl260IPsecInOctetsUncomp"),
        ("DFL260-MIB", "dfl260IPsecOutOctetsComp"),
        ("DFL260-MIB", "dfl260IPsecOutOctetsUncomp"),
        ("DFL260-MIB", "dfl260IPsecForwardedOctetsComp"),
        ("DFL260-MIB", "dfl260IPsecForwardedOctetsUcomp"),
        ("DFL260-MIB", "dfl260IPsecInPackets"),
        ("DFL260-MIB", "dfl260IPsecOutPackets"),
        ("DFL260-MIB", "dfl260IPsecForwardedPackets"),
        ("DFL260-MIB", "dfl260IPsecActiveTransforms"),
        ("DFL260-MIB", "dfl260IPsecTotalTransforms"),
        ("DFL260-MIB", "dfl260IPsecOutOfTransforms"),
        ("DFL260-MIB", "dfl260IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl260IPsecObjectGroup.setStatus("current")

dfl260StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 3)
)
dfl260StateCountersGroup.setObjects(
      *(("DFL260-MIB", "dfl260SysPscTcpSyn"),
        ("DFL260-MIB", "dfl260SysPscTcpOpen"),
        ("DFL260-MIB", "dfl260SysPscTcpFin"),
        ("DFL260-MIB", "dfl260SysPscUdp"),
        ("DFL260-MIB", "dfl260SysPscIcmp"),
        ("DFL260-MIB", "dfl260SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl260StateCountersGroup.setStatus("current")

dfl260IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 4)
)
dfl260IPPoolGroup.setObjects(
      *(("DFL260-MIB", "dfl260IPPoolsNumber"),
        ("DFL260-MIB", "dfl260IPPoolName"),
        ("DFL260-MIB", "dfl260IPPoolPrepare"),
        ("DFL260-MIB", "dfl260IPPoolFree"),
        ("DFL260-MIB", "dfl260IPPoolMisses"),
        ("DFL260-MIB", "dfl260IPPoolClientFails"),
        ("DFL260-MIB", "dfl260IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl260IPPoolGroup.setStatus("current")

dfl260DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 5)
)
dfl260DHCPServerGroup.setObjects(
      *(("DFL260-MIB", "dfl260DHCPTotalRejected"),
        ("DFL260-MIB", "dfl260DHCPRuleName"),
        ("DFL260-MIB", "dfl260DHCPRuleUsage"),
        ("DFL260-MIB", "dfl260DHCPRuleUsagePercent"),
        ("DFL260-MIB", "dfl260DHCPActiveClients"),
        ("DFL260-MIB", "dfl260DHCPActiveClientsPercent"),
        ("DFL260-MIB", "dfl260DHCPRejectedRequests"),
        ("DFL260-MIB", "dfl260DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl260DHCPServerGroup.setStatus("current")

dfl260RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 6)
)
dfl260RuleUseGroup.setObjects(
      *(("DFL260-MIB", "dfl260RuleName"),
        ("DFL260-MIB", "dfl260RuleUse"))
)
if mibBuilder.loadTexts:
    dfl260RuleUseGroup.setStatus("current")

dfl260UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 7)
)
dfl260UserAuthGroup.setObjects(
      *(("DFL260-MIB", "dfl260UserAuthHTTPUsers"),
        ("DFL260-MIB", "dfl260UserAuthXAUTHUsers"),
        ("DFL260-MIB", "dfl260UserAuthHTTPSUsers"),
        ("DFL260-MIB", "dfl260UserAuthPPPUsers"),
        ("DFL260-MIB", "dfl260UserAuthEAPUsers"),
        ("DFL260-MIB", "dfl260UserAuthRuleName"),
        ("DFL260-MIB", "dfl260UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl260UserAuthGroup.setStatus("current")

dfl260IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 8)
)
dfl260IfStatsGroup.setObjects(
      *(("DFL260-MIB", "dfl260IfName"),
        ("DFL260-MIB", "dfl260IfFragsIn"),
        ("DFL260-MIB", "dfl260IfFragReassOk"),
        ("DFL260-MIB", "dfl260IfFragReassFail"),
        ("DFL260-MIB", "dfl260IfPktsInCnt"),
        ("DFL260-MIB", "dfl260IfPktsOutCnt"),
        ("DFL260-MIB", "dfl260IfBitsInCnt"),
        ("DFL260-MIB", "dfl260IfBitsOutCnt"),
        ("DFL260-MIB", "dfl260IfPktsTotCnt"),
        ("DFL260-MIB", "dfl260IfBitsTotCnt"),
        ("DFL260-MIB", "dfl260IfHCPktsInCnt"),
        ("DFL260-MIB", "dfl260IfHCPktsOutCnt"),
        ("DFL260-MIB", "dfl260IfHCBitsInCnt"),
        ("DFL260-MIB", "dfl260IfHCBitsOutCnt"),
        ("DFL260-MIB", "dfl260IfHCPktsTotCnt"),
        ("DFL260-MIB", "dfl260IfHCBitsTotCnt"),
        ("DFL260-MIB", "dfl260IfRxRingFifoErrors"),
        ("DFL260-MIB", "dfl260IfRxDespools"),
        ("DFL260-MIB", "dfl260IfRxAvgUse"),
        ("DFL260-MIB", "dfl260IfRxRingSaturation"),
        ("DFL260-MIB", "dfl260RxRingFlooded"),
        ("DFL260-MIB", "dfl260IfTxDespools"),
        ("DFL260-MIB", "dfl260IfTxAvgUse"),
        ("DFL260-MIB", "dfl260IfTxRingSaturation"),
        ("DFL260-MIB", "dfl260RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl260IfStatsGroup.setStatus("current")

dfl260LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 9)
)
dfl260LinkMonitorGroup.setObjects(
      *(("DFL260-MIB", "dfl260LinkMonGrp"),
        ("DFL260-MIB", "dfl260LinkMonGrpName"),
        ("DFL260-MIB", "dfl260LinkMonGrpHostsUp"),
        ("DFL260-MIB", "dfl260LinkMonHostId"),
        ("DFL260-MIB", "dfl260LinkMonHostShortTermLoss"),
        ("DFL260-MIB", "dfl260LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl260LinkMonitorGroup.setStatus("current")

dfl260PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 10)
)
dfl260PipesObjectGroup.setObjects(
      *(("DFL260-MIB", "dfl260PipeUsers"),
        ("DFL260-MIB", "dfl260PipeName"),
        ("DFL260-MIB", "dfl260PipeMinPrec"),
        ("DFL260-MIB", "dfl260PipeMaxPrec"),
        ("DFL260-MIB", "dfl260PipeDefPrec"),
        ("DFL260-MIB", "dfl260PipeNumPrec"),
        ("DFL260-MIB", "dfl260PipeNumUsers"),
        ("DFL260-MIB", "dfl260PipeCurrentBps"),
        ("DFL260-MIB", "dfl260PipeCurrentPps"),
        ("DFL260-MIB", "dfl260PipeDelayedPackets"),
        ("DFL260-MIB", "dfl260PipeDropedPackets"),
        ("DFL260-MIB", "dfl260PipePrec"),
        ("DFL260-MIB", "dfl260PipePrecBps"),
        ("DFL260-MIB", "dfl260PipePrecTotalPps"),
        ("DFL260-MIB", "dfl260PipePrecReservedBps"),
        ("DFL260-MIB", "dfl260PipePrecDynLimBps"),
        ("DFL260-MIB", "dfl260PipePrecDynUsrLimBps"),
        ("DFL260-MIB", "dfl260PipePrecDelayedPackets"),
        ("DFL260-MIB", "dfl260PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl260PipesObjectGroup.setStatus("current")

dfl260DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 12)
)
dfl260DHCPRelayObjectGroup.setObjects(
      *(("DFL260-MIB", "dfl260DHCPRelayCurClients"),
        ("DFL260-MIB", "dfl260DHCPRelayCurTrans"),
        ("DFL260-MIB", "dfl260DHCPRelayRejected"),
        ("DFL260-MIB", "dfl260DHCPRelayRuleName"),
        ("DFL260-MIB", "dfl260DHCPRelayRuleHits"),
        ("DFL260-MIB", "dfl260DHCPRelayRuleCurClients"),
        ("DFL260-MIB", "dfl260DHCPRelayRuleRejCliPkts"),
        ("DFL260-MIB", "dfl260DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl260DHCPRelayObjectGroup.setStatus("current")

dfl260AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 13)
)
dfl260AlgGroup.setObjects(
      *(("DFL260-MIB", "dfl260AlgSessions"),
        ("DFL260-MIB", "dfl260AlgConnections"),
        ("DFL260-MIB", "dfl260AlgTCPStreams"),
        ("DFL260-MIB", "dfl260HttpAlgName"),
        ("DFL260-MIB", "dfl260HttpAlgTotalRequested"),
        ("DFL260-MIB", "dfl260HttpAlgTotalAllowed"),
        ("DFL260-MIB", "dfl260HttpAlgTotalBlocked"),
        ("DFL260-MIB", "dfl260HttpAlgCntFltName"),
        ("DFL260-MIB", "dfl260HttpAlgCntFltRequests"),
        ("DFL260-MIB", "dfl260HttpAlgCntFltAllowed"),
        ("DFL260-MIB", "dfl260HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl260AlgGroup.setStatus("current")

dfl260HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 14)
)
dfl260HAGroup.setObjects(
      *(("DFL260-MIB", "dfl260HASyncSendQueueLength"),
        ("DFL260-MIB", "dfl260HASyncSendQueueUsagePkt"),
        ("DFL260-MIB", "dfl260HASyncSendQueueUsageOct"),
        ("DFL260-MIB", "dfl260HASyncSentPackets"),
        ("DFL260-MIB", "dfl260HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl260HAGroup.setStatus("current")

dfl260IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 15)
)
dfl260IfVlanGroup.setObjects(
      *(("DFL260-MIB", "dfl260IfVlanUntaggedInPkts"),
        ("DFL260-MIB", "dfl260IfVlanUntaggedOutPkts"),
        ("DFL260-MIB", "dfl260IfVlanUntaggedTotPkts"),
        ("DFL260-MIB", "dfl260IfVlanUntaggedInOctets"),
        ("DFL260-MIB", "dfl260IfVlanUntaggedOutOctets"),
        ("DFL260-MIB", "dfl260IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl260IfVlanGroup.setStatus("current")

dfl260SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 16)
)
dfl260SmtpAlgGroup.setObjects(
      *(("DFL260-MIB", "dfl260SmtpAlgName"),
        ("DFL260-MIB", "dfl260SmtpAlgTotCheckedSes"),
        ("DFL260-MIB", "dfl260SmtpAlgTotSpamSes"),
        ("DFL260-MIB", "dfl260SmtpAlgTotDroppedSes"),
        ("DFL260-MIB", "dfl260SmtpAlgDnsBlName"),
        ("DFL260-MIB", "dfl260SmtpAlgDnsBlChecked"),
        ("DFL260-MIB", "dfl260SmtpAlgDnsBlMatched"),
        ("DFL260-MIB", "dfl260SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl260SmtpAlgGroup.setStatus("current")

dfl260SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 3, 1, 17)
)
dfl260SysTCPGroup.setObjects(
      *(("DFL260-MIB", "dfl260SysTCPRecvSmall"),
        ("DFL260-MIB", "dfl260SysTCPRecvLarge"),
        ("DFL260-MIB", "dfl260SysTCPSendSmall"),
        ("DFL260-MIB", "dfl260SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl260SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl260StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl260StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL260-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "utmFirewall": utmFirewall,
       "dfl260": dfl260,
       "dfl260OS": dfl260OS,
       "dfl260OSStats": dfl260OSStats,
       "dfl260System": dfl260System,
       "dfl260SysCpuLoad": dfl260SysCpuLoad,
       "dfl260SysForwardedBits": dfl260SysForwardedBits,
       "dfl260SysForwardedPackets": dfl260SysForwardedPackets,
       "dfl260SysBuffUse": dfl260SysBuffUse,
       "dfl260SysConns": dfl260SysConns,
       "dfl260SysPerStateCounters": dfl260SysPerStateCounters,
       "dfl260SysPscTcpSyn": dfl260SysPscTcpSyn,
       "dfl260SysPscTcpOpen": dfl260SysPscTcpOpen,
       "dfl260SysPscTcpFin": dfl260SysPscTcpFin,
       "dfl260SysPscUdp": dfl260SysPscUdp,
       "dfl260SysPscIcmp": dfl260SysPscIcmp,
       "dfl260SysPscOther": dfl260SysPscOther,
       "dfl260IfStatsTable": dfl260IfStatsTable,
       "dfl260IfStatsEntry": dfl260IfStatsEntry,
       "dfl260IfStatsIndex": dfl260IfStatsIndex,
       "dfl260IfName": dfl260IfName,
       "dfl260IfFragsIn": dfl260IfFragsIn,
       "dfl260IfFragReassOk": dfl260IfFragReassOk,
       "dfl260IfFragReassFail": dfl260IfFragReassFail,
       "dfl260IfPktsInCnt": dfl260IfPktsInCnt,
       "dfl260IfPktsOutCnt": dfl260IfPktsOutCnt,
       "dfl260IfBitsInCnt": dfl260IfBitsInCnt,
       "dfl260IfBitsOutCnt": dfl260IfBitsOutCnt,
       "dfl260IfPktsTotCnt": dfl260IfPktsTotCnt,
       "dfl260IfBitsTotCnt": dfl260IfBitsTotCnt,
       "dfl260IfHCPktsInCnt": dfl260IfHCPktsInCnt,
       "dfl260IfHCPktsOutCnt": dfl260IfHCPktsOutCnt,
       "dfl260IfHCBitsInCnt": dfl260IfHCBitsInCnt,
       "dfl260IfHCBitsOutCnt": dfl260IfHCBitsOutCnt,
       "dfl260IfHCPktsTotCnt": dfl260IfHCPktsTotCnt,
       "dfl260IfHCBitsTotCnt": dfl260IfHCBitsTotCnt,
       "dfl260IfRxRingTable": dfl260IfRxRingTable,
       "dfl260IfRxRingEntry": dfl260IfRxRingEntry,
       "dfl260IfRxRingIndex": dfl260IfRxRingIndex,
       "dfl260IfRxRingFifoErrors": dfl260IfRxRingFifoErrors,
       "dfl260IfRxDespools": dfl260IfRxDespools,
       "dfl260IfRxAvgUse": dfl260IfRxAvgUse,
       "dfl260IfRxRingSaturation": dfl260IfRxRingSaturation,
       "dfl260RxRingFlooded": dfl260RxRingFlooded,
       "dfl260IfTxRingTable": dfl260IfTxRingTable,
       "dfl260IfTxRingEntry": dfl260IfTxRingEntry,
       "dfl260IfTxRingIndex": dfl260IfTxRingIndex,
       "dfl260IfTxDespools": dfl260IfTxDespools,
       "dfl260IfTxAvgUse": dfl260IfTxAvgUse,
       "dfl260IfTxRingSaturation": dfl260IfTxRingSaturation,
       "dfl260RxTingFlooded": dfl260RxTingFlooded,
       "dfl260IfVlanStatsTable": dfl260IfVlanStatsTable,
       "dfl260IfVlanStatsEntry": dfl260IfVlanStatsEntry,
       "dfl260IfVlanIndex": dfl260IfVlanIndex,
       "dfl260IfVlanUntaggedInPkts": dfl260IfVlanUntaggedInPkts,
       "dfl260IfVlanUntaggedOutPkts": dfl260IfVlanUntaggedOutPkts,
       "dfl260IfVlanUntaggedTotPkts": dfl260IfVlanUntaggedTotPkts,
       "dfl260IfVlanUntaggedInOctets": dfl260IfVlanUntaggedInOctets,
       "dfl260IfVlanUntaggedOutOctets": dfl260IfVlanUntaggedOutOctets,
       "dfl260IfVlanUntaggedTotOctets": dfl260IfVlanUntaggedTotOctets,
       "dfl260HWSensorTable": dfl260HWSensorTable,
       "dfl260HWSensorEntry": dfl260HWSensorEntry,
       "dfl260HWSensorIndex": dfl260HWSensorIndex,
       "dfl260HWSensorName": dfl260HWSensorName,
       "dfl260HWSensorValue": dfl260HWSensorValue,
       "dfl260HWSensorUnit": dfl260HWSensorUnit,
       "dfl260SysMemUsage": dfl260SysMemUsage,
       "dfl260SysTCPUsage": dfl260SysTCPUsage,
       "dfl260SysTCPRecvSmall": dfl260SysTCPRecvSmall,
       "dfl260SysTCPRecvLarge": dfl260SysTCPRecvLarge,
       "dfl260SysTCPSendSmall": dfl260SysTCPSendSmall,
       "dfl260SysTCPSendLarge": dfl260SysTCPSendLarge,
       "dfl260SysTimerUsage": dfl260SysTimerUsage,
       "dfl260SysConnOPS": dfl260SysConnOPS,
       "dfl260SysConnCPS": dfl260SysConnCPS,
       "dfl260SysHCForwardedBits": dfl260SysHCForwardedBits,
       "dfl260VPN": dfl260VPN,
       "dfl260IPsec": dfl260IPsec,
       "dfl260IPsecGlobal": dfl260IPsecGlobal,
       "dfl260IPsecPhaseOneActive": dfl260IPsecPhaseOneActive,
       "dfl260IPsecPhaseOneAggrModeDone": dfl260IPsecPhaseOneAggrModeDone,
       "dfl260IPsecQuickModeActive": dfl260IPsecQuickModeActive,
       "dfl260IPsecPhaseOneDone": dfl260IPsecPhaseOneDone,
       "dfl260IPsecPhaseOneFailed": dfl260IPsecPhaseOneFailed,
       "dfl260IPsecPhaseOneRekeyed": dfl260IPsecPhaseOneRekeyed,
       "dfl260IPsecQuickModeDone": dfl260IPsecQuickModeDone,
       "dfl260IPsecQuickModeFailed": dfl260IPsecQuickModeFailed,
       "dfl260IPsecInfoDone": dfl260IPsecInfoDone,
       "dfl260IPsecInfoFailed": dfl260IPsecInfoFailed,
       "dfl260IPsecInOctetsComp": dfl260IPsecInOctetsComp,
       "dfl260IPsecInOctetsUncomp": dfl260IPsecInOctetsUncomp,
       "dfl260IPsecOutOctetsComp": dfl260IPsecOutOctetsComp,
       "dfl260IPsecOutOctetsUncomp": dfl260IPsecOutOctetsUncomp,
       "dfl260IPsecForwardedOctetsComp": dfl260IPsecForwardedOctetsComp,
       "dfl260IPsecForwardedOctetsUcomp": dfl260IPsecForwardedOctetsUcomp,
       "dfl260IPsecInPackets": dfl260IPsecInPackets,
       "dfl260IPsecOutPackets": dfl260IPsecOutPackets,
       "dfl260IPsecForwardedPackets": dfl260IPsecForwardedPackets,
       "dfl260IPsecActiveTransforms": dfl260IPsecActiveTransforms,
       "dfl260IPsecTotalTransforms": dfl260IPsecTotalTransforms,
       "dfl260IPsecOutOfTransforms": dfl260IPsecOutOfTransforms,
       "dfl260IPsecTotalRekeys": dfl260IPsecTotalRekeys,
       "dfl260Rules": dfl260Rules,
       "dfl260RuleUseTable": dfl260RuleUseTable,
       "dfl260RuleUseEntry": dfl260RuleUseEntry,
       "dfl260RuleIndex": dfl260RuleIndex,
       "dfl260RuleName": dfl260RuleName,
       "dfl260RuleUse": dfl260RuleUse,
       "dfl260IPPools": dfl260IPPools,
       "dfl260IPPoolsNumber": dfl260IPPoolsNumber,
       "dfl260IPPoolTable": dfl260IPPoolTable,
       "dfl260IPPoolEntry": dfl260IPPoolEntry,
       "dfl260IPPoolIndex": dfl260IPPoolIndex,
       "dfl260IPPoolName": dfl260IPPoolName,
       "dfl260IPPoolPrepare": dfl260IPPoolPrepare,
       "dfl260IPPoolFree": dfl260IPPoolFree,
       "dfl260IPPoolMisses": dfl260IPPoolMisses,
       "dfl260IPPoolClientFails": dfl260IPPoolClientFails,
       "dfl260IPPoolUsed": dfl260IPPoolUsed,
       "dfl260DHCPServer": dfl260DHCPServer,
       "dfl260DHCPTotalRejected": dfl260DHCPTotalRejected,
       "dfl260DHCPRuleTable": dfl260DHCPRuleTable,
       "dfl260DHCPRuleEntry": dfl260DHCPRuleEntry,
       "dfl260DHCPRuleIndex": dfl260DHCPRuleIndex,
       "dfl260DHCPRuleName": dfl260DHCPRuleName,
       "dfl260DHCPRuleUsage": dfl260DHCPRuleUsage,
       "dfl260DHCPRuleUsagePercent": dfl260DHCPRuleUsagePercent,
       "dfl260DHCPActiveClients": dfl260DHCPActiveClients,
       "dfl260DHCPActiveClientsPercent": dfl260DHCPActiveClientsPercent,
       "dfl260DHCPRejectedRequests": dfl260DHCPRejectedRequests,
       "dfl260DHCPTotalLeases": dfl260DHCPTotalLeases,
       "dfl260UserAuth": dfl260UserAuth,
       "dfl260UserAuthHTTPUsers": dfl260UserAuthHTTPUsers,
       "dfl260UserAuthXAUTHUsers": dfl260UserAuthXAUTHUsers,
       "dfl260UserAuthHTTPSUsers": dfl260UserAuthHTTPSUsers,
       "dfl260UserAuthPPPUsers": dfl260UserAuthPPPUsers,
       "dfl260UserAuthEAPUsers": dfl260UserAuthEAPUsers,
       "dfl260UserAuthRuleUseTable": dfl260UserAuthRuleUseTable,
       "dfl260UserAuthRuleUseEntry": dfl260UserAuthRuleUseEntry,
       "dfl260UserAuthRuleIndex": dfl260UserAuthRuleIndex,
       "dfl260UserAuthRuleName": dfl260UserAuthRuleName,
       "dfl260UserAuthRuleUse": dfl260UserAuthRuleUse,
       "dfl260LinkMonitor": dfl260LinkMonitor,
       "dfl260LinkMonGrp": dfl260LinkMonGrp,
       "dfl260LinkMonGrpTable": dfl260LinkMonGrpTable,
       "dfl260LinkMonGrpEntry": dfl260LinkMonGrpEntry,
       "dfl260LinkMonGrpIndex": dfl260LinkMonGrpIndex,
       "dfl260LinkMonGrpName": dfl260LinkMonGrpName,
       "dfl260LinkMonGrpHostsUp": dfl260LinkMonGrpHostsUp,
       "dfl260LinkMonHostTable": dfl260LinkMonHostTable,
       "dfl260LinkMonHostEntry": dfl260LinkMonHostEntry,
       "dfl260LinkMonHostIndex": dfl260LinkMonHostIndex,
       "dfl260LinkMonHostId": dfl260LinkMonHostId,
       "dfl260LinkMonHostShortTermLoss": dfl260LinkMonHostShortTermLoss,
       "dfl260LinkMonHostPacketsLost": dfl260LinkMonHostPacketsLost,
       "dfl260Pipes": dfl260Pipes,
       "dfl260PipeUsers": dfl260PipeUsers,
       "dfl260PipeTable": dfl260PipeTable,
       "dfl260PipeEntry": dfl260PipeEntry,
       "dfl260PipeIndex": dfl260PipeIndex,
       "dfl260PipeName": dfl260PipeName,
       "dfl260PipeMinPrec": dfl260PipeMinPrec,
       "dfl260PipeMaxPrec": dfl260PipeMaxPrec,
       "dfl260PipeDefPrec": dfl260PipeDefPrec,
       "dfl260PipeNumPrec": dfl260PipeNumPrec,
       "dfl260PipeNumUsers": dfl260PipeNumUsers,
       "dfl260PipeCurrentBps": dfl260PipeCurrentBps,
       "dfl260PipeCurrentPps": dfl260PipeCurrentPps,
       "dfl260PipeDelayedPackets": dfl260PipeDelayedPackets,
       "dfl260PipeDropedPackets": dfl260PipeDropedPackets,
       "dfl260PipePrecTable": dfl260PipePrecTable,
       "dfl260PipePrecEntry": dfl260PipePrecEntry,
       "dfl260PipePrecIndex": dfl260PipePrecIndex,
       "dfl260PipePrec": dfl260PipePrec,
       "dfl260PipePrecBps": dfl260PipePrecBps,
       "dfl260PipePrecTotalPps": dfl260PipePrecTotalPps,
       "dfl260PipePrecReservedBps": dfl260PipePrecReservedBps,
       "dfl260PipePrecDynLimBps": dfl260PipePrecDynLimBps,
       "dfl260PipePrecDynUsrLimBps": dfl260PipePrecDynUsrLimBps,
       "dfl260PipePrecDelayedPackets": dfl260PipePrecDelayedPackets,
       "dfl260PipePrecDropedPackets": dfl260PipePrecDropedPackets,
       "dfl260ALG": dfl260ALG,
       "dfl260AlgSessions": dfl260AlgSessions,
       "dfl260AlgConnections": dfl260AlgConnections,
       "dfl260AlgTCPStreams": dfl260AlgTCPStreams,
       "dfl260HttpAlg": dfl260HttpAlg,
       "dfl260HttpAlgTable": dfl260HttpAlgTable,
       "dfl260HttpAlgEntry": dfl260HttpAlgEntry,
       "dfl260HttpAlgIndex": dfl260HttpAlgIndex,
       "dfl260HttpAlgName": dfl260HttpAlgName,
       "dfl260HttpAlgTotalRequested": dfl260HttpAlgTotalRequested,
       "dfl260HttpAlgTotalAllowed": dfl260HttpAlgTotalAllowed,
       "dfl260HttpAlgTotalBlocked": dfl260HttpAlgTotalBlocked,
       "dfl260HttpAlgCntFltTable": dfl260HttpAlgCntFltTable,
       "dfl260HttpAlgCntFltEntry": dfl260HttpAlgCntFltEntry,
       "dfl260HttpAlgCntFltIndex": dfl260HttpAlgCntFltIndex,
       "dfl260HttpAlgCntFltName": dfl260HttpAlgCntFltName,
       "dfl260HttpAlgCntFltRequests": dfl260HttpAlgCntFltRequests,
       "dfl260HttpAlgCntFltAllowed": dfl260HttpAlgCntFltAllowed,
       "dfl260HttpAlgCntFltBlocked": dfl260HttpAlgCntFltBlocked,
       "dfl260SmtpAlg": dfl260SmtpAlg,
       "dfl260SmtpAlgTable": dfl260SmtpAlgTable,
       "dfl260SmtpAlgEntry": dfl260SmtpAlgEntry,
       "dfl260SmtpAlgIndex": dfl260SmtpAlgIndex,
       "dfl260SmtpAlgName": dfl260SmtpAlgName,
       "dfl260SmtpAlgTotCheckedSes": dfl260SmtpAlgTotCheckedSes,
       "dfl260SmtpAlgTotSpamSes": dfl260SmtpAlgTotSpamSes,
       "dfl260SmtpAlgTotDroppedSes": dfl260SmtpAlgTotDroppedSes,
       "dfl260SmtpAlgDnsBlTable": dfl260SmtpAlgDnsBlTable,
       "dfl260SmtpAlgDnsBlEntry": dfl260SmtpAlgDnsBlEntry,
       "dfl260SmtpAlgDnsBlIndex": dfl260SmtpAlgDnsBlIndex,
       "dfl260SmtpAlgDnsBlName": dfl260SmtpAlgDnsBlName,
       "dfl260SmtpAlgDnsBlChecked": dfl260SmtpAlgDnsBlChecked,
       "dfl260SmtpAlgDnsBlMatched": dfl260SmtpAlgDnsBlMatched,
       "dfl260SmtpAlgDnsBlFailChecks": dfl260SmtpAlgDnsBlFailChecks,
       "dfl260DHCPRelay": dfl260DHCPRelay,
       "dfl260DHCPRelayCurClients": dfl260DHCPRelayCurClients,
       "dfl260DHCPRelayCurTrans": dfl260DHCPRelayCurTrans,
       "dfl260DHCPRelayRejected": dfl260DHCPRelayRejected,
       "dfl260DHCPRelayRuleTable": dfl260DHCPRelayRuleTable,
       "dfl260DHCPRelayRuleEntry": dfl260DHCPRelayRuleEntry,
       "dfl260DHCPRelayRuleIndex": dfl260DHCPRelayRuleIndex,
       "dfl260DHCPRelayRuleName": dfl260DHCPRelayRuleName,
       "dfl260DHCPRelayRuleHits": dfl260DHCPRelayRuleHits,
       "dfl260DHCPRelayRuleCurClients": dfl260DHCPRelayRuleCurClients,
       "dfl260DHCPRelayRuleRejCliPkts": dfl260DHCPRelayRuleRejCliPkts,
       "dfl260DHCPRelayRuleRejSrvPkts": dfl260DHCPRelayRuleRejSrvPkts,
       "dfl260HA": dfl260HA,
       "dfl260HASyncSendQueueLength": dfl260HASyncSendQueueLength,
       "dfl260HASyncSendQueueUsagePkt": dfl260HASyncSendQueueUsagePkt,
       "dfl260HASyncSendQueueUsageOct": dfl260HASyncSendQueueUsageOct,
       "dfl260HASyncSentPackets": dfl260HASyncSentPackets,
       "dfl260HASyncSendResentPackets": dfl260HASyncSendResentPackets,
       "dfl260reg": dfl260reg,
       "dfl260MibModules": dfl260MibModules,
       "dfl260-MIB": dfl260_MIB,
       "dfl260MibConfs": dfl260MibConfs,
       "dfl260StatsConformance": dfl260StatsConformance,
       "dfl260StatsCompliance": dfl260StatsCompliance,
       "dfl260MibObjectGroups": dfl260MibObjectGroups,
       "dfl260StatsRegGroups": dfl260StatsRegGroups,
       "dfl260SystemObjectGroup": dfl260SystemObjectGroup,
       "dfl260IPsecObjectGroup": dfl260IPsecObjectGroup,
       "dfl260StateCountersGroup": dfl260StateCountersGroup,
       "dfl260IPPoolGroup": dfl260IPPoolGroup,
       "dfl260DHCPServerGroup": dfl260DHCPServerGroup,
       "dfl260RuleUseGroup": dfl260RuleUseGroup,
       "dfl260UserAuthGroup": dfl260UserAuthGroup,
       "dfl260IfStatsGroup": dfl260IfStatsGroup,
       "dfl260LinkMonitorGroup": dfl260LinkMonitorGroup,
       "dfl260PipesObjectGroup": dfl260PipesObjectGroup,
       "dfl260DHCPRelayObjectGroup": dfl260DHCPRelayObjectGroup,
       "dfl260AlgGroup": dfl260AlgGroup,
       "dfl260HAGroup": dfl260HAGroup,
       "dfl260IfVlanGroup": dfl260IfVlanGroup,
       "dfl260SmtpAlgGroup": dfl260SmtpAlgGroup,
       "dfl260SysTCPGroup": dfl260SysTCPGroup}
)
