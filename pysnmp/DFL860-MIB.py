# SNMP MIB module (DFL860-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL860-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:19 2024
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

dfl860_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 1, 2)
)
dfl860_MIB.setRevisions(
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
_Dfl860_ObjectIdentity = ObjectIdentity
dfl860 = _Dfl860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2)
)
_Dfl860OS_ObjectIdentity = ObjectIdentity
dfl860OS = _Dfl860OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1)
)
_Dfl860OSStats_ObjectIdentity = ObjectIdentity
dfl860OSStats = _Dfl860OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2)
)
_Dfl860System_ObjectIdentity = ObjectIdentity
dfl860System = _Dfl860System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1)
)
_Dfl860SysCpuLoad_Type = Gauge32
_Dfl860SysCpuLoad_Object = MibScalar
dfl860SysCpuLoad = _Dfl860SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 1),
    _Dfl860SysCpuLoad_Type()
)
dfl860SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysCpuLoad.setStatus("current")
_Dfl860SysForwardedBits_Type = Counter32
_Dfl860SysForwardedBits_Object = MibScalar
dfl860SysForwardedBits = _Dfl860SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 2),
    _Dfl860SysForwardedBits_Type()
)
dfl860SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysForwardedBits.setStatus("current")
_Dfl860SysForwardedPackets_Type = Counter32
_Dfl860SysForwardedPackets_Object = MibScalar
dfl860SysForwardedPackets = _Dfl860SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 3),
    _Dfl860SysForwardedPackets_Type()
)
dfl860SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysForwardedPackets.setStatus("current")
_Dfl860SysBuffUse_Type = Gauge32
_Dfl860SysBuffUse_Object = MibScalar
dfl860SysBuffUse = _Dfl860SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 4),
    _Dfl860SysBuffUse_Type()
)
dfl860SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysBuffUse.setStatus("current")
_Dfl860SysConns_Type = Gauge32
_Dfl860SysConns_Object = MibScalar
dfl860SysConns = _Dfl860SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 5),
    _Dfl860SysConns_Type()
)
dfl860SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysConns.setStatus("current")
_Dfl860SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl860SysPerStateCounters = _Dfl860SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6)
)
_Dfl860SysPscTcpSyn_Type = Gauge32
_Dfl860SysPscTcpSyn_Object = MibScalar
dfl860SysPscTcpSyn = _Dfl860SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6, 1),
    _Dfl860SysPscTcpSyn_Type()
)
dfl860SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysPscTcpSyn.setStatus("current")
_Dfl860SysPscTcpOpen_Type = Gauge32
_Dfl860SysPscTcpOpen_Object = MibScalar
dfl860SysPscTcpOpen = _Dfl860SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6, 2),
    _Dfl860SysPscTcpOpen_Type()
)
dfl860SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysPscTcpOpen.setStatus("current")
_Dfl860SysPscTcpFin_Type = Gauge32
_Dfl860SysPscTcpFin_Object = MibScalar
dfl860SysPscTcpFin = _Dfl860SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6, 3),
    _Dfl860SysPscTcpFin_Type()
)
dfl860SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysPscTcpFin.setStatus("current")
_Dfl860SysPscUdp_Type = Gauge32
_Dfl860SysPscUdp_Object = MibScalar
dfl860SysPscUdp = _Dfl860SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6, 4),
    _Dfl860SysPscUdp_Type()
)
dfl860SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysPscUdp.setStatus("current")
_Dfl860SysPscIcmp_Type = Gauge32
_Dfl860SysPscIcmp_Object = MibScalar
dfl860SysPscIcmp = _Dfl860SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6, 5),
    _Dfl860SysPscIcmp_Type()
)
dfl860SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysPscIcmp.setStatus("current")
_Dfl860SysPscOther_Type = Gauge32
_Dfl860SysPscOther_Object = MibScalar
dfl860SysPscOther = _Dfl860SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 6, 6),
    _Dfl860SysPscOther_Type()
)
dfl860SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysPscOther.setStatus("current")
_Dfl860IfStatsTable_Object = MibTable
dfl860IfStatsTable = _Dfl860IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl860IfStatsTable.setStatus("current")
_Dfl860IfStatsEntry_Object = MibTableRow
dfl860IfStatsEntry = _Dfl860IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1)
)
dfl860IfStatsEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl860IfStatsEntry.setStatus("current")


class _Dfl860IfStatsIndex_Type(Integer32):
    """Custom type dfl860IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860IfStatsIndex_Type.__name__ = "Integer32"
_Dfl860IfStatsIndex_Object = MibTableColumn
dfl860IfStatsIndex = _Dfl860IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 1),
    _Dfl860IfStatsIndex_Type()
)
dfl860IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860IfStatsIndex.setStatus("current")
_Dfl860IfName_Type = DisplayString
_Dfl860IfName_Object = MibTableColumn
dfl860IfName = _Dfl860IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 2),
    _Dfl860IfName_Type()
)
dfl860IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfName.setStatus("current")
_Dfl860IfFragsIn_Type = Counter32
_Dfl860IfFragsIn_Object = MibTableColumn
dfl860IfFragsIn = _Dfl860IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 3),
    _Dfl860IfFragsIn_Type()
)
dfl860IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfFragsIn.setStatus("current")
_Dfl860IfFragReassOk_Type = Counter32
_Dfl860IfFragReassOk_Object = MibTableColumn
dfl860IfFragReassOk = _Dfl860IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 4),
    _Dfl860IfFragReassOk_Type()
)
dfl860IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfFragReassOk.setStatus("current")
_Dfl860IfFragReassFail_Type = Counter32
_Dfl860IfFragReassFail_Object = MibTableColumn
dfl860IfFragReassFail = _Dfl860IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 5),
    _Dfl860IfFragReassFail_Type()
)
dfl860IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfFragReassFail.setStatus("current")
_Dfl860IfPktsInCnt_Type = Counter32
_Dfl860IfPktsInCnt_Object = MibTableColumn
dfl860IfPktsInCnt = _Dfl860IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 6),
    _Dfl860IfPktsInCnt_Type()
)
dfl860IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfPktsInCnt.setStatus("current")
_Dfl860IfPktsOutCnt_Type = Counter32
_Dfl860IfPktsOutCnt_Object = MibTableColumn
dfl860IfPktsOutCnt = _Dfl860IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 7),
    _Dfl860IfPktsOutCnt_Type()
)
dfl860IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfPktsOutCnt.setStatus("current")
_Dfl860IfBitsInCnt_Type = Counter32
_Dfl860IfBitsInCnt_Object = MibTableColumn
dfl860IfBitsInCnt = _Dfl860IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 8),
    _Dfl860IfBitsInCnt_Type()
)
dfl860IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfBitsInCnt.setStatus("current")
_Dfl860IfBitsOutCnt_Type = Counter32
_Dfl860IfBitsOutCnt_Object = MibTableColumn
dfl860IfBitsOutCnt = _Dfl860IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 9),
    _Dfl860IfBitsOutCnt_Type()
)
dfl860IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfBitsOutCnt.setStatus("current")
_Dfl860IfPktsTotCnt_Type = Counter32
_Dfl860IfPktsTotCnt_Object = MibTableColumn
dfl860IfPktsTotCnt = _Dfl860IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 10),
    _Dfl860IfPktsTotCnt_Type()
)
dfl860IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfPktsTotCnt.setStatus("current")
_Dfl860IfBitsTotCnt_Type = Counter32
_Dfl860IfBitsTotCnt_Object = MibTableColumn
dfl860IfBitsTotCnt = _Dfl860IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 11),
    _Dfl860IfBitsTotCnt_Type()
)
dfl860IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfBitsTotCnt.setStatus("current")
_Dfl860IfHCPktsInCnt_Type = Counter64
_Dfl860IfHCPktsInCnt_Object = MibTableColumn
dfl860IfHCPktsInCnt = _Dfl860IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 12),
    _Dfl860IfHCPktsInCnt_Type()
)
dfl860IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfHCPktsInCnt.setStatus("current")
_Dfl860IfHCPktsOutCnt_Type = Counter64
_Dfl860IfHCPktsOutCnt_Object = MibTableColumn
dfl860IfHCPktsOutCnt = _Dfl860IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 13),
    _Dfl860IfHCPktsOutCnt_Type()
)
dfl860IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfHCPktsOutCnt.setStatus("current")
_Dfl860IfHCBitsInCnt_Type = Counter64
_Dfl860IfHCBitsInCnt_Object = MibTableColumn
dfl860IfHCBitsInCnt = _Dfl860IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 14),
    _Dfl860IfHCBitsInCnt_Type()
)
dfl860IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfHCBitsInCnt.setStatus("current")
_Dfl860IfHCBitsOutCnt_Type = Counter64
_Dfl860IfHCBitsOutCnt_Object = MibTableColumn
dfl860IfHCBitsOutCnt = _Dfl860IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 15),
    _Dfl860IfHCBitsOutCnt_Type()
)
dfl860IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfHCBitsOutCnt.setStatus("current")
_Dfl860IfHCPktsTotCnt_Type = Counter64
_Dfl860IfHCPktsTotCnt_Object = MibTableColumn
dfl860IfHCPktsTotCnt = _Dfl860IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 16),
    _Dfl860IfHCPktsTotCnt_Type()
)
dfl860IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfHCPktsTotCnt.setStatus("current")
_Dfl860IfHCBitsTotCnt_Type = Counter64
_Dfl860IfHCBitsTotCnt_Object = MibTableColumn
dfl860IfHCBitsTotCnt = _Dfl860IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 7, 1, 17),
    _Dfl860IfHCBitsTotCnt_Type()
)
dfl860IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfHCBitsTotCnt.setStatus("current")
_Dfl860IfRxRingTable_Object = MibTable
dfl860IfRxRingTable = _Dfl860IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl860IfRxRingTable.setStatus("current")
_Dfl860IfRxRingEntry_Object = MibTableRow
dfl860IfRxRingEntry = _Dfl860IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1)
)
dfl860IfRxRingEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl860IfRxRingEntry.setStatus("current")


class _Dfl860IfRxRingIndex_Type(Integer32):
    """Custom type dfl860IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl860IfRxRingIndex_Object = MibTableColumn
dfl860IfRxRingIndex = _Dfl860IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1, 1),
    _Dfl860IfRxRingIndex_Type()
)
dfl860IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860IfRxRingIndex.setStatus("current")
_Dfl860IfRxRingFifoErrors_Type = Counter32
_Dfl860IfRxRingFifoErrors_Object = MibTableColumn
dfl860IfRxRingFifoErrors = _Dfl860IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1, 2),
    _Dfl860IfRxRingFifoErrors_Type()
)
dfl860IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfRxRingFifoErrors.setStatus("current")
_Dfl860IfRxDespools_Type = Gauge32
_Dfl860IfRxDespools_Object = MibTableColumn
dfl860IfRxDespools = _Dfl860IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1, 3),
    _Dfl860IfRxDespools_Type()
)
dfl860IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfRxDespools.setStatus("current")
_Dfl860IfRxAvgUse_Type = Gauge32
_Dfl860IfRxAvgUse_Object = MibTableColumn
dfl860IfRxAvgUse = _Dfl860IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1, 4),
    _Dfl860IfRxAvgUse_Type()
)
dfl860IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfRxAvgUse.setStatus("current")
_Dfl860IfRxRingSaturation_Type = Gauge32
_Dfl860IfRxRingSaturation_Object = MibTableColumn
dfl860IfRxRingSaturation = _Dfl860IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1, 5),
    _Dfl860IfRxRingSaturation_Type()
)
dfl860IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfRxRingSaturation.setStatus("current")
_Dfl860RxRingFlooded_Type = Gauge32
_Dfl860RxRingFlooded_Object = MibTableColumn
dfl860RxRingFlooded = _Dfl860RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 8, 1, 6),
    _Dfl860RxRingFlooded_Type()
)
dfl860RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860RxRingFlooded.setStatus("current")
_Dfl860IfTxRingTable_Object = MibTable
dfl860IfTxRingTable = _Dfl860IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl860IfTxRingTable.setStatus("current")
_Dfl860IfTxRingEntry_Object = MibTableRow
dfl860IfTxRingEntry = _Dfl860IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9, 1)
)
dfl860IfTxRingEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl860IfTxRingEntry.setStatus("current")


class _Dfl860IfTxRingIndex_Type(Integer32):
    """Custom type dfl860IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl860IfTxRingIndex_Object = MibTableColumn
dfl860IfTxRingIndex = _Dfl860IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9, 1, 1),
    _Dfl860IfTxRingIndex_Type()
)
dfl860IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860IfTxRingIndex.setStatus("current")
_Dfl860IfTxDespools_Type = Gauge32
_Dfl860IfTxDespools_Object = MibTableColumn
dfl860IfTxDespools = _Dfl860IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9, 1, 2),
    _Dfl860IfTxDespools_Type()
)
dfl860IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfTxDespools.setStatus("current")
_Dfl860IfTxAvgUse_Type = Gauge32
_Dfl860IfTxAvgUse_Object = MibTableColumn
dfl860IfTxAvgUse = _Dfl860IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9, 1, 3),
    _Dfl860IfTxAvgUse_Type()
)
dfl860IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfTxAvgUse.setStatus("current")
_Dfl860IfTxRingSaturation_Type = Gauge32
_Dfl860IfTxRingSaturation_Object = MibTableColumn
dfl860IfTxRingSaturation = _Dfl860IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9, 1, 4),
    _Dfl860IfTxRingSaturation_Type()
)
dfl860IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfTxRingSaturation.setStatus("current")
_Dfl860RxTingFlooded_Type = Gauge32
_Dfl860RxTingFlooded_Object = MibTableColumn
dfl860RxTingFlooded = _Dfl860RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 9, 1, 5),
    _Dfl860RxTingFlooded_Type()
)
dfl860RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860RxTingFlooded.setStatus("current")
_Dfl860IfVlanStatsTable_Object = MibTable
dfl860IfVlanStatsTable = _Dfl860IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl860IfVlanStatsTable.setStatus("current")
_Dfl860IfVlanStatsEntry_Object = MibTableRow
dfl860IfVlanStatsEntry = _Dfl860IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1)
)
dfl860IfVlanStatsEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl860IfVlanStatsEntry.setStatus("current")


class _Dfl860IfVlanIndex_Type(Integer32):
    """Custom type dfl860IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860IfVlanIndex_Type.__name__ = "Integer32"
_Dfl860IfVlanIndex_Object = MibTableColumn
dfl860IfVlanIndex = _Dfl860IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 1),
    _Dfl860IfVlanIndex_Type()
)
dfl860IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860IfVlanIndex.setStatus("current")
_Dfl860IfVlanUntaggedInPkts_Type = Counter32
_Dfl860IfVlanUntaggedInPkts_Object = MibTableColumn
dfl860IfVlanUntaggedInPkts = _Dfl860IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 2),
    _Dfl860IfVlanUntaggedInPkts_Type()
)
dfl860IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfVlanUntaggedInPkts.setStatus("current")
_Dfl860IfVlanUntaggedOutPkts_Type = Counter32
_Dfl860IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl860IfVlanUntaggedOutPkts = _Dfl860IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 3),
    _Dfl860IfVlanUntaggedOutPkts_Type()
)
dfl860IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfVlanUntaggedOutPkts.setStatus("current")
_Dfl860IfVlanUntaggedTotPkts_Type = Counter32
_Dfl860IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl860IfVlanUntaggedTotPkts = _Dfl860IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 4),
    _Dfl860IfVlanUntaggedTotPkts_Type()
)
dfl860IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfVlanUntaggedTotPkts.setStatus("current")
_Dfl860IfVlanUntaggedInOctets_Type = Counter32
_Dfl860IfVlanUntaggedInOctets_Object = MibTableColumn
dfl860IfVlanUntaggedInOctets = _Dfl860IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 5),
    _Dfl860IfVlanUntaggedInOctets_Type()
)
dfl860IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfVlanUntaggedInOctets.setStatus("current")
_Dfl860IfVlanUntaggedOutOctets_Type = Counter32
_Dfl860IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl860IfVlanUntaggedOutOctets = _Dfl860IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 6),
    _Dfl860IfVlanUntaggedOutOctets_Type()
)
dfl860IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfVlanUntaggedOutOctets.setStatus("current")
_Dfl860IfVlanUntaggedTotOctets_Type = Counter32
_Dfl860IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl860IfVlanUntaggedTotOctets = _Dfl860IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 10, 1, 7),
    _Dfl860IfVlanUntaggedTotOctets_Type()
)
dfl860IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IfVlanUntaggedTotOctets.setStatus("current")
_Dfl860HWSensorTable_Object = MibTable
dfl860HWSensorTable = _Dfl860HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl860HWSensorTable.setStatus("current")
_Dfl860HWSensorEntry_Object = MibTableRow
dfl860HWSensorEntry = _Dfl860HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 11, 1)
)
dfl860HWSensorEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl860HWSensorEntry.setStatus("current")


class _Dfl860HWSensorIndex_Type(Integer32):
    """Custom type dfl860HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860HWSensorIndex_Type.__name__ = "Integer32"
_Dfl860HWSensorIndex_Object = MibTableColumn
dfl860HWSensorIndex = _Dfl860HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 11, 1, 1),
    _Dfl860HWSensorIndex_Type()
)
dfl860HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860HWSensorIndex.setStatus("current")
_Dfl860HWSensorName_Type = DisplayString
_Dfl860HWSensorName_Object = MibTableColumn
dfl860HWSensorName = _Dfl860HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 11, 1, 2),
    _Dfl860HWSensorName_Type()
)
dfl860HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HWSensorName.setStatus("current")
_Dfl860HWSensorValue_Type = Gauge32
_Dfl860HWSensorValue_Object = MibTableColumn
dfl860HWSensorValue = _Dfl860HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 11, 1, 3),
    _Dfl860HWSensorValue_Type()
)
dfl860HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HWSensorValue.setStatus("current")
_Dfl860HWSensorUnit_Type = DisplayString
_Dfl860HWSensorUnit_Object = MibTableColumn
dfl860HWSensorUnit = _Dfl860HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 11, 1, 4),
    _Dfl860HWSensorUnit_Type()
)
dfl860HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HWSensorUnit.setStatus("current")
_Dfl860SysMemUsage_Type = Gauge32
_Dfl860SysMemUsage_Object = MibScalar
dfl860SysMemUsage = _Dfl860SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 12),
    _Dfl860SysMemUsage_Type()
)
dfl860SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysMemUsage.setStatus("current")
_Dfl860SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl860SysTCPUsage = _Dfl860SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 13)
)
_Dfl860SysTCPRecvSmall_Type = Gauge32
_Dfl860SysTCPRecvSmall_Object = MibScalar
dfl860SysTCPRecvSmall = _Dfl860SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 13, 1),
    _Dfl860SysTCPRecvSmall_Type()
)
dfl860SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysTCPRecvSmall.setStatus("current")
_Dfl860SysTCPRecvLarge_Type = Gauge32
_Dfl860SysTCPRecvLarge_Object = MibScalar
dfl860SysTCPRecvLarge = _Dfl860SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 13, 2),
    _Dfl860SysTCPRecvLarge_Type()
)
dfl860SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysTCPRecvLarge.setStatus("current")
_Dfl860SysTCPSendSmall_Type = Gauge32
_Dfl860SysTCPSendSmall_Object = MibScalar
dfl860SysTCPSendSmall = _Dfl860SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 13, 3),
    _Dfl860SysTCPSendSmall_Type()
)
dfl860SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysTCPSendSmall.setStatus("current")
_Dfl860SysTCPSendLarge_Type = Gauge32
_Dfl860SysTCPSendLarge_Object = MibScalar
dfl860SysTCPSendLarge = _Dfl860SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 13, 4),
    _Dfl860SysTCPSendLarge_Type()
)
dfl860SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysTCPSendLarge.setStatus("current")
_Dfl860SysTimerUsage_Type = Gauge32
_Dfl860SysTimerUsage_Object = MibScalar
dfl860SysTimerUsage = _Dfl860SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 14),
    _Dfl860SysTimerUsage_Type()
)
dfl860SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysTimerUsage.setStatus("current")
_Dfl860SysConnOPS_Type = Gauge32
_Dfl860SysConnOPS_Object = MibScalar
dfl860SysConnOPS = _Dfl860SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 15),
    _Dfl860SysConnOPS_Type()
)
dfl860SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysConnOPS.setStatus("current")
_Dfl860SysConnCPS_Type = Gauge32
_Dfl860SysConnCPS_Object = MibScalar
dfl860SysConnCPS = _Dfl860SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 16),
    _Dfl860SysConnCPS_Type()
)
dfl860SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysConnCPS.setStatus("current")
_Dfl860SysHCForwardedBits_Type = Counter64
_Dfl860SysHCForwardedBits_Object = MibScalar
dfl860SysHCForwardedBits = _Dfl860SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 1, 17),
    _Dfl860SysHCForwardedBits_Type()
)
dfl860SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SysHCForwardedBits.setStatus("current")
_Dfl860VPN_ObjectIdentity = ObjectIdentity
dfl860VPN = _Dfl860VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2)
)
_Dfl860IPsec_ObjectIdentity = ObjectIdentity
dfl860IPsec = _Dfl860IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1)
)
_Dfl860IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl860IPsecGlobal = _Dfl860IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1)
)
_Dfl860IPsecPhaseOneActive_Type = Gauge32
_Dfl860IPsecPhaseOneActive_Object = MibScalar
dfl860IPsecPhaseOneActive = _Dfl860IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 1),
    _Dfl860IPsecPhaseOneActive_Type()
)
dfl860IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecPhaseOneActive.setStatus("current")
_Dfl860IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl860IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl860IPsecPhaseOneAggrModeDone = _Dfl860IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 2),
    _Dfl860IPsecPhaseOneAggrModeDone_Type()
)
dfl860IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl860IPsecQuickModeActive_Type = Gauge32
_Dfl860IPsecQuickModeActive_Object = MibScalar
dfl860IPsecQuickModeActive = _Dfl860IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 3),
    _Dfl860IPsecQuickModeActive_Type()
)
dfl860IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecQuickModeActive.setStatus("current")
_Dfl860IPsecPhaseOneDone_Type = Counter32
_Dfl860IPsecPhaseOneDone_Object = MibScalar
dfl860IPsecPhaseOneDone = _Dfl860IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 4),
    _Dfl860IPsecPhaseOneDone_Type()
)
dfl860IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecPhaseOneDone.setStatus("current")
_Dfl860IPsecPhaseOneFailed_Type = Counter32
_Dfl860IPsecPhaseOneFailed_Object = MibScalar
dfl860IPsecPhaseOneFailed = _Dfl860IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 5),
    _Dfl860IPsecPhaseOneFailed_Type()
)
dfl860IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecPhaseOneFailed.setStatus("current")
_Dfl860IPsecPhaseOneRekeyed_Type = Counter32
_Dfl860IPsecPhaseOneRekeyed_Object = MibScalar
dfl860IPsecPhaseOneRekeyed = _Dfl860IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 6),
    _Dfl860IPsecPhaseOneRekeyed_Type()
)
dfl860IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecPhaseOneRekeyed.setStatus("current")
_Dfl860IPsecQuickModeDone_Type = Counter32
_Dfl860IPsecQuickModeDone_Object = MibScalar
dfl860IPsecQuickModeDone = _Dfl860IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 7),
    _Dfl860IPsecQuickModeDone_Type()
)
dfl860IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecQuickModeDone.setStatus("current")
_Dfl860IPsecQuickModeFailed_Type = Counter32
_Dfl860IPsecQuickModeFailed_Object = MibScalar
dfl860IPsecQuickModeFailed = _Dfl860IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 8),
    _Dfl860IPsecQuickModeFailed_Type()
)
dfl860IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecQuickModeFailed.setStatus("current")
_Dfl860IPsecInfoDone_Type = Counter32
_Dfl860IPsecInfoDone_Object = MibScalar
dfl860IPsecInfoDone = _Dfl860IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 9),
    _Dfl860IPsecInfoDone_Type()
)
dfl860IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecInfoDone.setStatus("current")
_Dfl860IPsecInfoFailed_Type = Counter32
_Dfl860IPsecInfoFailed_Object = MibScalar
dfl860IPsecInfoFailed = _Dfl860IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 10),
    _Dfl860IPsecInfoFailed_Type()
)
dfl860IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecInfoFailed.setStatus("current")
_Dfl860IPsecInOctetsComp_Type = Counter64
_Dfl860IPsecInOctetsComp_Object = MibScalar
dfl860IPsecInOctetsComp = _Dfl860IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 11),
    _Dfl860IPsecInOctetsComp_Type()
)
dfl860IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecInOctetsComp.setStatus("current")
_Dfl860IPsecInOctetsUncomp_Type = Counter64
_Dfl860IPsecInOctetsUncomp_Object = MibScalar
dfl860IPsecInOctetsUncomp = _Dfl860IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 12),
    _Dfl860IPsecInOctetsUncomp_Type()
)
dfl860IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecInOctetsUncomp.setStatus("current")
_Dfl860IPsecOutOctetsComp_Type = Counter64
_Dfl860IPsecOutOctetsComp_Object = MibScalar
dfl860IPsecOutOctetsComp = _Dfl860IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 13),
    _Dfl860IPsecOutOctetsComp_Type()
)
dfl860IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecOutOctetsComp.setStatus("current")
_Dfl860IPsecOutOctetsUncomp_Type = Counter64
_Dfl860IPsecOutOctetsUncomp_Object = MibScalar
dfl860IPsecOutOctetsUncomp = _Dfl860IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 14),
    _Dfl860IPsecOutOctetsUncomp_Type()
)
dfl860IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecOutOctetsUncomp.setStatus("current")
_Dfl860IPsecForwardedOctetsComp_Type = Counter64
_Dfl860IPsecForwardedOctetsComp_Object = MibScalar
dfl860IPsecForwardedOctetsComp = _Dfl860IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 15),
    _Dfl860IPsecForwardedOctetsComp_Type()
)
dfl860IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecForwardedOctetsComp.setStatus("current")
_Dfl860IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl860IPsecForwardedOctetsUcomp_Object = MibScalar
dfl860IPsecForwardedOctetsUcomp = _Dfl860IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 16),
    _Dfl860IPsecForwardedOctetsUcomp_Type()
)
dfl860IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl860IPsecInPackets_Type = Counter64
_Dfl860IPsecInPackets_Object = MibScalar
dfl860IPsecInPackets = _Dfl860IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 17),
    _Dfl860IPsecInPackets_Type()
)
dfl860IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecInPackets.setStatus("current")
_Dfl860IPsecOutPackets_Type = Counter64
_Dfl860IPsecOutPackets_Object = MibScalar
dfl860IPsecOutPackets = _Dfl860IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 18),
    _Dfl860IPsecOutPackets_Type()
)
dfl860IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecOutPackets.setStatus("current")
_Dfl860IPsecForwardedPackets_Type = Counter64
_Dfl860IPsecForwardedPackets_Object = MibScalar
dfl860IPsecForwardedPackets = _Dfl860IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 19),
    _Dfl860IPsecForwardedPackets_Type()
)
dfl860IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecForwardedPackets.setStatus("current")
_Dfl860IPsecActiveTransforms_Type = Gauge32
_Dfl860IPsecActiveTransforms_Object = MibScalar
dfl860IPsecActiveTransforms = _Dfl860IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 20),
    _Dfl860IPsecActiveTransforms_Type()
)
dfl860IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecActiveTransforms.setStatus("current")
_Dfl860IPsecTotalTransforms_Type = Counter32
_Dfl860IPsecTotalTransforms_Object = MibScalar
dfl860IPsecTotalTransforms = _Dfl860IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 21),
    _Dfl860IPsecTotalTransforms_Type()
)
dfl860IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecTotalTransforms.setStatus("current")
_Dfl860IPsecOutOfTransforms_Type = Counter32
_Dfl860IPsecOutOfTransforms_Object = MibScalar
dfl860IPsecOutOfTransforms = _Dfl860IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 22),
    _Dfl860IPsecOutOfTransforms_Type()
)
dfl860IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecOutOfTransforms.setStatus("current")
_Dfl860IPsecTotalRekeys_Type = Counter32
_Dfl860IPsecTotalRekeys_Object = MibScalar
dfl860IPsecTotalRekeys = _Dfl860IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 2, 1, 1, 23),
    _Dfl860IPsecTotalRekeys_Type()
)
dfl860IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPsecTotalRekeys.setStatus("current")
_Dfl860Rules_ObjectIdentity = ObjectIdentity
dfl860Rules = _Dfl860Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 3)
)
_Dfl860RuleUseTable_Object = MibTable
dfl860RuleUseTable = _Dfl860RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl860RuleUseTable.setStatus("current")
_Dfl860RuleUseEntry_Object = MibTableRow
dfl860RuleUseEntry = _Dfl860RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 3, 2, 1)
)
dfl860RuleUseEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860RuleUseEntry.setStatus("current")


class _Dfl860RuleIndex_Type(Integer32):
    """Custom type dfl860RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860RuleIndex_Type.__name__ = "Integer32"
_Dfl860RuleIndex_Object = MibTableColumn
dfl860RuleIndex = _Dfl860RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 3, 2, 1, 1),
    _Dfl860RuleIndex_Type()
)
dfl860RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860RuleIndex.setStatus("current")
_Dfl860RuleName_Type = DisplayString
_Dfl860RuleName_Object = MibTableColumn
dfl860RuleName = _Dfl860RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 3, 2, 1, 2),
    _Dfl860RuleName_Type()
)
dfl860RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860RuleName.setStatus("current")
_Dfl860RuleUse_Type = Counter32
_Dfl860RuleUse_Object = MibTableColumn
dfl860RuleUse = _Dfl860RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 3, 2, 1, 3),
    _Dfl860RuleUse_Type()
)
dfl860RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860RuleUse.setStatus("current")
_Dfl860IPPools_ObjectIdentity = ObjectIdentity
dfl860IPPools = _Dfl860IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4)
)
_Dfl860IPPoolsNumber_Type = Integer32
_Dfl860IPPoolsNumber_Object = MibScalar
dfl860IPPoolsNumber = _Dfl860IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 1),
    _Dfl860IPPoolsNumber_Type()
)
dfl860IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolsNumber.setStatus("current")
_Dfl860IPPoolTable_Object = MibTable
dfl860IPPoolTable = _Dfl860IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl860IPPoolTable.setStatus("current")
_Dfl860IPPoolEntry_Object = MibTableRow
dfl860IPPoolEntry = _Dfl860IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1)
)
dfl860IPPoolEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl860IPPoolEntry.setStatus("current")


class _Dfl860IPPoolIndex_Type(Integer32):
    """Custom type dfl860IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860IPPoolIndex_Type.__name__ = "Integer32"
_Dfl860IPPoolIndex_Object = MibTableColumn
dfl860IPPoolIndex = _Dfl860IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 1),
    _Dfl860IPPoolIndex_Type()
)
dfl860IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860IPPoolIndex.setStatus("current")
_Dfl860IPPoolName_Type = DisplayString
_Dfl860IPPoolName_Object = MibTableColumn
dfl860IPPoolName = _Dfl860IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 2),
    _Dfl860IPPoolName_Type()
)
dfl860IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolName.setStatus("current")
_Dfl860IPPoolPrepare_Type = Gauge32
_Dfl860IPPoolPrepare_Object = MibTableColumn
dfl860IPPoolPrepare = _Dfl860IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 3),
    _Dfl860IPPoolPrepare_Type()
)
dfl860IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolPrepare.setStatus("current")
_Dfl860IPPoolFree_Type = Gauge32
_Dfl860IPPoolFree_Object = MibTableColumn
dfl860IPPoolFree = _Dfl860IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 4),
    _Dfl860IPPoolFree_Type()
)
dfl860IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolFree.setStatus("current")
_Dfl860IPPoolMisses_Type = Gauge32
_Dfl860IPPoolMisses_Object = MibTableColumn
dfl860IPPoolMisses = _Dfl860IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 5),
    _Dfl860IPPoolMisses_Type()
)
dfl860IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolMisses.setStatus("current")
_Dfl860IPPoolClientFails_Type = Gauge32
_Dfl860IPPoolClientFails_Object = MibTableColumn
dfl860IPPoolClientFails = _Dfl860IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 6),
    _Dfl860IPPoolClientFails_Type()
)
dfl860IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolClientFails.setStatus("current")
_Dfl860IPPoolUsed_Type = Gauge32
_Dfl860IPPoolUsed_Object = MibTableColumn
dfl860IPPoolUsed = _Dfl860IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 4, 2, 1, 7),
    _Dfl860IPPoolUsed_Type()
)
dfl860IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860IPPoolUsed.setStatus("current")
_Dfl860DHCPServer_ObjectIdentity = ObjectIdentity
dfl860DHCPServer = _Dfl860DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5)
)
_Dfl860DHCPTotalRejected_Type = Gauge32
_Dfl860DHCPTotalRejected_Object = MibScalar
dfl860DHCPTotalRejected = _Dfl860DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 1),
    _Dfl860DHCPTotalRejected_Type()
)
dfl860DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPTotalRejected.setStatus("current")
_Dfl860DHCPRuleTable_Object = MibTable
dfl860DHCPRuleTable = _Dfl860DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl860DHCPRuleTable.setStatus("current")
_Dfl860DHCPRuleEntry_Object = MibTableRow
dfl860DHCPRuleEntry = _Dfl860DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1)
)
dfl860DHCPRuleEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860DHCPRuleEntry.setStatus("current")


class _Dfl860DHCPRuleIndex_Type(Integer32):
    """Custom type dfl860DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl860DHCPRuleIndex_Object = MibTableColumn
dfl860DHCPRuleIndex = _Dfl860DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 1),
    _Dfl860DHCPRuleIndex_Type()
)
dfl860DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860DHCPRuleIndex.setStatus("current")
_Dfl860DHCPRuleName_Type = DisplayString
_Dfl860DHCPRuleName_Object = MibTableColumn
dfl860DHCPRuleName = _Dfl860DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 2),
    _Dfl860DHCPRuleName_Type()
)
dfl860DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRuleName.setStatus("current")
_Dfl860DHCPRuleUsage_Type = Gauge32
_Dfl860DHCPRuleUsage_Object = MibTableColumn
dfl860DHCPRuleUsage = _Dfl860DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 3),
    _Dfl860DHCPRuleUsage_Type()
)
dfl860DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRuleUsage.setStatus("current")
_Dfl860DHCPRuleUsagePercent_Type = Gauge32
_Dfl860DHCPRuleUsagePercent_Object = MibTableColumn
dfl860DHCPRuleUsagePercent = _Dfl860DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 4),
    _Dfl860DHCPRuleUsagePercent_Type()
)
dfl860DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRuleUsagePercent.setStatus("current")
_Dfl860DHCPActiveClients_Type = Gauge32
_Dfl860DHCPActiveClients_Object = MibTableColumn
dfl860DHCPActiveClients = _Dfl860DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 5),
    _Dfl860DHCPActiveClients_Type()
)
dfl860DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPActiveClients.setStatus("current")
_Dfl860DHCPActiveClientsPercent_Type = Gauge32
_Dfl860DHCPActiveClientsPercent_Object = MibTableColumn
dfl860DHCPActiveClientsPercent = _Dfl860DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 6),
    _Dfl860DHCPActiveClientsPercent_Type()
)
dfl860DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPActiveClientsPercent.setStatus("current")
_Dfl860DHCPRejectedRequests_Type = Gauge32
_Dfl860DHCPRejectedRequests_Object = MibTableColumn
dfl860DHCPRejectedRequests = _Dfl860DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 7),
    _Dfl860DHCPRejectedRequests_Type()
)
dfl860DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRejectedRequests.setStatus("current")
_Dfl860DHCPTotalLeases_Type = Gauge32
_Dfl860DHCPTotalLeases_Object = MibTableColumn
dfl860DHCPTotalLeases = _Dfl860DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 5, 2, 1, 8),
    _Dfl860DHCPTotalLeases_Type()
)
dfl860DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPTotalLeases.setStatus("current")
_Dfl860UserAuth_ObjectIdentity = ObjectIdentity
dfl860UserAuth = _Dfl860UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6)
)
_Dfl860UserAuthHTTPUsers_Type = Gauge32
_Dfl860UserAuthHTTPUsers_Object = MibScalar
dfl860UserAuthHTTPUsers = _Dfl860UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 1),
    _Dfl860UserAuthHTTPUsers_Type()
)
dfl860UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthHTTPUsers.setStatus("current")
_Dfl860UserAuthXAUTHUsers_Type = Gauge32
_Dfl860UserAuthXAUTHUsers_Object = MibScalar
dfl860UserAuthXAUTHUsers = _Dfl860UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 2),
    _Dfl860UserAuthXAUTHUsers_Type()
)
dfl860UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthXAUTHUsers.setStatus("current")
_Dfl860UserAuthHTTPSUsers_Type = Gauge32
_Dfl860UserAuthHTTPSUsers_Object = MibScalar
dfl860UserAuthHTTPSUsers = _Dfl860UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 3),
    _Dfl860UserAuthHTTPSUsers_Type()
)
dfl860UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthHTTPSUsers.setStatus("current")
_Dfl860UserAuthPPPUsers_Type = Gauge32
_Dfl860UserAuthPPPUsers_Object = MibScalar
dfl860UserAuthPPPUsers = _Dfl860UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 4),
    _Dfl860UserAuthPPPUsers_Type()
)
dfl860UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthPPPUsers.setStatus("current")
_Dfl860UserAuthEAPUsers_Type = Gauge32
_Dfl860UserAuthEAPUsers_Object = MibScalar
dfl860UserAuthEAPUsers = _Dfl860UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 5),
    _Dfl860UserAuthEAPUsers_Type()
)
dfl860UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthEAPUsers.setStatus("current")
_Dfl860UserAuthRuleUseTable_Object = MibTable
dfl860UserAuthRuleUseTable = _Dfl860UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl860UserAuthRuleUseTable.setStatus("current")
_Dfl860UserAuthRuleUseEntry_Object = MibTableRow
dfl860UserAuthRuleUseEntry = _Dfl860UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 6, 1)
)
dfl860UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860UserAuthRuleUseEntry.setStatus("current")


class _Dfl860UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl860UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl860UserAuthRuleIndex_Object = MibTableColumn
dfl860UserAuthRuleIndex = _Dfl860UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 6, 1, 1),
    _Dfl860UserAuthRuleIndex_Type()
)
dfl860UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860UserAuthRuleIndex.setStatus("current")
_Dfl860UserAuthRuleName_Type = DisplayString
_Dfl860UserAuthRuleName_Object = MibTableColumn
dfl860UserAuthRuleName = _Dfl860UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 6, 1, 2),
    _Dfl860UserAuthRuleName_Type()
)
dfl860UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthRuleName.setStatus("current")
_Dfl860UserAuthRuleUse_Type = Counter32
_Dfl860UserAuthRuleUse_Object = MibTableColumn
dfl860UserAuthRuleUse = _Dfl860UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 6, 6, 1, 3),
    _Dfl860UserAuthRuleUse_Type()
)
dfl860UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860UserAuthRuleUse.setStatus("current")
_Dfl860LinkMonitor_ObjectIdentity = ObjectIdentity
dfl860LinkMonitor = _Dfl860LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7)
)
_Dfl860LinkMonGrp_Type = Integer32
_Dfl860LinkMonGrp_Object = MibScalar
dfl860LinkMonGrp = _Dfl860LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 1),
    _Dfl860LinkMonGrp_Type()
)
dfl860LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860LinkMonGrp.setStatus("current")
_Dfl860LinkMonGrpTable_Object = MibTable
dfl860LinkMonGrpTable = _Dfl860LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl860LinkMonGrpTable.setStatus("current")
_Dfl860LinkMonGrpEntry_Object = MibTableRow
dfl860LinkMonGrpEntry = _Dfl860LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 2, 1)
)
dfl860LinkMonGrpEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl860LinkMonGrpEntry.setStatus("current")


class _Dfl860LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl860LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl860LinkMonGrpIndex_Object = MibTableColumn
dfl860LinkMonGrpIndex = _Dfl860LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 2, 1, 1),
    _Dfl860LinkMonGrpIndex_Type()
)
dfl860LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860LinkMonGrpIndex.setStatus("current")
_Dfl860LinkMonGrpName_Type = DisplayString
_Dfl860LinkMonGrpName_Object = MibTableColumn
dfl860LinkMonGrpName = _Dfl860LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 2, 1, 2),
    _Dfl860LinkMonGrpName_Type()
)
dfl860LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860LinkMonGrpName.setStatus("current")
_Dfl860LinkMonGrpHostsUp_Type = Gauge32
_Dfl860LinkMonGrpHostsUp_Object = MibTableColumn
dfl860LinkMonGrpHostsUp = _Dfl860LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 2, 1, 3),
    _Dfl860LinkMonGrpHostsUp_Type()
)
dfl860LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860LinkMonGrpHostsUp.setStatus("current")
_Dfl860LinkMonHostTable_Object = MibTable
dfl860LinkMonHostTable = _Dfl860LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl860LinkMonHostTable.setStatus("current")
_Dfl860LinkMonHostEntry_Object = MibTableRow
dfl860LinkMonHostEntry = _Dfl860LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 3, 1)
)
dfl860LinkMonHostEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860LinkMonGrpIndex"),
    (0, "DFL860-MIB", "dfl860LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl860LinkMonHostEntry.setStatus("current")


class _Dfl860LinkMonHostIndex_Type(Integer32):
    """Custom type dfl860LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl860LinkMonHostIndex_Object = MibTableColumn
dfl860LinkMonHostIndex = _Dfl860LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 3, 1, 1),
    _Dfl860LinkMonHostIndex_Type()
)
dfl860LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860LinkMonHostIndex.setStatus("current")
_Dfl860LinkMonHostId_Type = DisplayString
_Dfl860LinkMonHostId_Object = MibTableColumn
dfl860LinkMonHostId = _Dfl860LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 3, 1, 2),
    _Dfl860LinkMonHostId_Type()
)
dfl860LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860LinkMonHostId.setStatus("current")
_Dfl860LinkMonHostShortTermLoss_Type = Gauge32
_Dfl860LinkMonHostShortTermLoss_Object = MibTableColumn
dfl860LinkMonHostShortTermLoss = _Dfl860LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 3, 1, 3),
    _Dfl860LinkMonHostShortTermLoss_Type()
)
dfl860LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860LinkMonHostShortTermLoss.setStatus("current")
_Dfl860LinkMonHostPacketsLost_Type = Counter32
_Dfl860LinkMonHostPacketsLost_Object = MibTableColumn
dfl860LinkMonHostPacketsLost = _Dfl860LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 7, 3, 1, 4),
    _Dfl860LinkMonHostPacketsLost_Type()
)
dfl860LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860LinkMonHostPacketsLost.setStatus("current")
_Dfl860Pipes_ObjectIdentity = ObjectIdentity
dfl860Pipes = _Dfl860Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8)
)
_Dfl860PipeUsers_Type = Gauge32
_Dfl860PipeUsers_Object = MibScalar
dfl860PipeUsers = _Dfl860PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 1),
    _Dfl860PipeUsers_Type()
)
dfl860PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeUsers.setStatus("current")
_Dfl860PipeTable_Object = MibTable
dfl860PipeTable = _Dfl860PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl860PipeTable.setStatus("current")
_Dfl860PipeEntry_Object = MibTableRow
dfl860PipeEntry = _Dfl860PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1)
)
dfl860PipeEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl860PipeEntry.setStatus("current")


class _Dfl860PipeIndex_Type(Integer32):
    """Custom type dfl860PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860PipeIndex_Type.__name__ = "Integer32"
_Dfl860PipeIndex_Object = MibTableColumn
dfl860PipeIndex = _Dfl860PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 1),
    _Dfl860PipeIndex_Type()
)
dfl860PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860PipeIndex.setStatus("current")
_Dfl860PipeName_Type = DisplayString
_Dfl860PipeName_Object = MibTableColumn
dfl860PipeName = _Dfl860PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 2),
    _Dfl860PipeName_Type()
)
dfl860PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeName.setStatus("current")
_Dfl860PipeMinPrec_Type = Integer32
_Dfl860PipeMinPrec_Object = MibTableColumn
dfl860PipeMinPrec = _Dfl860PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 3),
    _Dfl860PipeMinPrec_Type()
)
dfl860PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeMinPrec.setStatus("current")
_Dfl860PipeMaxPrec_Type = Integer32
_Dfl860PipeMaxPrec_Object = MibTableColumn
dfl860PipeMaxPrec = _Dfl860PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 4),
    _Dfl860PipeMaxPrec_Type()
)
dfl860PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeMaxPrec.setStatus("current")
_Dfl860PipeDefPrec_Type = Integer32
_Dfl860PipeDefPrec_Object = MibTableColumn
dfl860PipeDefPrec = _Dfl860PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 5),
    _Dfl860PipeDefPrec_Type()
)
dfl860PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeDefPrec.setStatus("current")
_Dfl860PipeNumPrec_Type = Integer32
_Dfl860PipeNumPrec_Object = MibTableColumn
dfl860PipeNumPrec = _Dfl860PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 6),
    _Dfl860PipeNumPrec_Type()
)
dfl860PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeNumPrec.setStatus("current")
_Dfl860PipeNumUsers_Type = Gauge32
_Dfl860PipeNumUsers_Object = MibTableColumn
dfl860PipeNumUsers = _Dfl860PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 7),
    _Dfl860PipeNumUsers_Type()
)
dfl860PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeNumUsers.setStatus("current")
_Dfl860PipeCurrentBps_Type = Gauge32
_Dfl860PipeCurrentBps_Object = MibTableColumn
dfl860PipeCurrentBps = _Dfl860PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 8),
    _Dfl860PipeCurrentBps_Type()
)
dfl860PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeCurrentBps.setStatus("current")
_Dfl860PipeCurrentPps_Type = Gauge32
_Dfl860PipeCurrentPps_Object = MibTableColumn
dfl860PipeCurrentPps = _Dfl860PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 9),
    _Dfl860PipeCurrentPps_Type()
)
dfl860PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeCurrentPps.setStatus("current")
_Dfl860PipeDelayedPackets_Type = Counter32
_Dfl860PipeDelayedPackets_Object = MibTableColumn
dfl860PipeDelayedPackets = _Dfl860PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 10),
    _Dfl860PipeDelayedPackets_Type()
)
dfl860PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeDelayedPackets.setStatus("current")
_Dfl860PipeDropedPackets_Type = Counter32
_Dfl860PipeDropedPackets_Object = MibTableColumn
dfl860PipeDropedPackets = _Dfl860PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 2, 1, 11),
    _Dfl860PipeDropedPackets_Type()
)
dfl860PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipeDropedPackets.setStatus("current")
_Dfl860PipePrecTable_Object = MibTable
dfl860PipePrecTable = _Dfl860PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl860PipePrecTable.setStatus("current")
_Dfl860PipePrecEntry_Object = MibTableRow
dfl860PipePrecEntry = _Dfl860PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1)
)
dfl860PipePrecEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860PipeIndex"),
    (0, "DFL860-MIB", "dfl860PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl860PipePrecEntry.setStatus("current")


class _Dfl860PipePrecIndex_Type(Integer32):
    """Custom type dfl860PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860PipePrecIndex_Type.__name__ = "Integer32"
_Dfl860PipePrecIndex_Object = MibTableColumn
dfl860PipePrecIndex = _Dfl860PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 1),
    _Dfl860PipePrecIndex_Type()
)
dfl860PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860PipePrecIndex.setStatus("current")
_Dfl860PipePrec_Type = Integer32
_Dfl860PipePrec_Object = MibTableColumn
dfl860PipePrec = _Dfl860PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 2),
    _Dfl860PipePrec_Type()
)
dfl860PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrec.setStatus("current")
_Dfl860PipePrecBps_Type = Gauge32
_Dfl860PipePrecBps_Object = MibTableColumn
dfl860PipePrecBps = _Dfl860PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 3),
    _Dfl860PipePrecBps_Type()
)
dfl860PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecBps.setStatus("current")
_Dfl860PipePrecTotalPps_Type = Gauge32
_Dfl860PipePrecTotalPps_Object = MibTableColumn
dfl860PipePrecTotalPps = _Dfl860PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 4),
    _Dfl860PipePrecTotalPps_Type()
)
dfl860PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecTotalPps.setStatus("current")
_Dfl860PipePrecReservedBps_Type = Gauge32
_Dfl860PipePrecReservedBps_Object = MibTableColumn
dfl860PipePrecReservedBps = _Dfl860PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 5),
    _Dfl860PipePrecReservedBps_Type()
)
dfl860PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecReservedBps.setStatus("current")
_Dfl860PipePrecDynLimBps_Type = Gauge32
_Dfl860PipePrecDynLimBps_Object = MibTableColumn
dfl860PipePrecDynLimBps = _Dfl860PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 6),
    _Dfl860PipePrecDynLimBps_Type()
)
dfl860PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecDynLimBps.setStatus("current")
_Dfl860PipePrecDynUsrLimBps_Type = Gauge32
_Dfl860PipePrecDynUsrLimBps_Object = MibTableColumn
dfl860PipePrecDynUsrLimBps = _Dfl860PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 7),
    _Dfl860PipePrecDynUsrLimBps_Type()
)
dfl860PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecDynUsrLimBps.setStatus("current")
_Dfl860PipePrecDelayedPackets_Type = Counter32
_Dfl860PipePrecDelayedPackets_Object = MibTableColumn
dfl860PipePrecDelayedPackets = _Dfl860PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 8),
    _Dfl860PipePrecDelayedPackets_Type()
)
dfl860PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecDelayedPackets.setStatus("current")
_Dfl860PipePrecDropedPackets_Type = Counter32
_Dfl860PipePrecDropedPackets_Object = MibTableColumn
dfl860PipePrecDropedPackets = _Dfl860PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 8, 3, 1, 9),
    _Dfl860PipePrecDropedPackets_Type()
)
dfl860PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860PipePrecDropedPackets.setStatus("current")
_Dfl860ALG_ObjectIdentity = ObjectIdentity
dfl860ALG = _Dfl860ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9)
)
_Dfl860AlgSessions_Type = Gauge32
_Dfl860AlgSessions_Object = MibScalar
dfl860AlgSessions = _Dfl860AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 1),
    _Dfl860AlgSessions_Type()
)
dfl860AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860AlgSessions.setStatus("current")
_Dfl860AlgConnections_Type = Gauge32
_Dfl860AlgConnections_Object = MibScalar
dfl860AlgConnections = _Dfl860AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 2),
    _Dfl860AlgConnections_Type()
)
dfl860AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860AlgConnections.setStatus("current")
_Dfl860AlgTCPStreams_Type = Gauge32
_Dfl860AlgTCPStreams_Object = MibScalar
dfl860AlgTCPStreams = _Dfl860AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 3),
    _Dfl860AlgTCPStreams_Type()
)
dfl860AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860AlgTCPStreams.setStatus("current")
_Dfl860HttpAlg_ObjectIdentity = ObjectIdentity
dfl860HttpAlg = _Dfl860HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4)
)
_Dfl860HttpAlgTable_Object = MibTable
dfl860HttpAlgTable = _Dfl860HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl860HttpAlgTable.setStatus("current")
_Dfl860HttpAlgEntry_Object = MibTableRow
dfl860HttpAlgEntry = _Dfl860HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1, 1)
)
dfl860HttpAlgEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl860HttpAlgEntry.setStatus("current")


class _Dfl860HttpAlgIndex_Type(Integer32):
    """Custom type dfl860HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl860HttpAlgIndex_Object = MibTableColumn
dfl860HttpAlgIndex = _Dfl860HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1, 1, 1),
    _Dfl860HttpAlgIndex_Type()
)
dfl860HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860HttpAlgIndex.setStatus("current")
_Dfl860HttpAlgName_Type = DisplayString
_Dfl860HttpAlgName_Object = MibTableColumn
dfl860HttpAlgName = _Dfl860HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1, 1, 2),
    _Dfl860HttpAlgName_Type()
)
dfl860HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgName.setStatus("current")
_Dfl860HttpAlgTotalRequested_Type = Gauge32
_Dfl860HttpAlgTotalRequested_Object = MibTableColumn
dfl860HttpAlgTotalRequested = _Dfl860HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1, 1, 3),
    _Dfl860HttpAlgTotalRequested_Type()
)
dfl860HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgTotalRequested.setStatus("current")
_Dfl860HttpAlgTotalAllowed_Type = Gauge32
_Dfl860HttpAlgTotalAllowed_Object = MibTableColumn
dfl860HttpAlgTotalAllowed = _Dfl860HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1, 1, 4),
    _Dfl860HttpAlgTotalAllowed_Type()
)
dfl860HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgTotalAllowed.setStatus("current")
_Dfl860HttpAlgTotalBlocked_Type = Gauge32
_Dfl860HttpAlgTotalBlocked_Object = MibTableColumn
dfl860HttpAlgTotalBlocked = _Dfl860HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 1, 1, 5),
    _Dfl860HttpAlgTotalBlocked_Type()
)
dfl860HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgTotalBlocked.setStatus("current")
_Dfl860HttpAlgCntFltTable_Object = MibTable
dfl860HttpAlgCntFltTable = _Dfl860HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltTable.setStatus("current")
_Dfl860HttpAlgCntFltEntry_Object = MibTableRow
dfl860HttpAlgCntFltEntry = _Dfl860HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2, 1)
)
dfl860HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860HttpAlgIndex"),
    (0, "DFL860-MIB", "dfl860HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltEntry.setStatus("current")


class _Dfl860HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl860HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl860HttpAlgCntFltIndex_Object = MibTableColumn
dfl860HttpAlgCntFltIndex = _Dfl860HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2, 1, 1),
    _Dfl860HttpAlgCntFltIndex_Type()
)
dfl860HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltIndex.setStatus("current")
_Dfl860HttpAlgCntFltName_Type = DisplayString
_Dfl860HttpAlgCntFltName_Object = MibTableColumn
dfl860HttpAlgCntFltName = _Dfl860HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2, 1, 2),
    _Dfl860HttpAlgCntFltName_Type()
)
dfl860HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltName.setStatus("current")
_Dfl860HttpAlgCntFltRequests_Type = Gauge32
_Dfl860HttpAlgCntFltRequests_Object = MibTableColumn
dfl860HttpAlgCntFltRequests = _Dfl860HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2, 1, 3),
    _Dfl860HttpAlgCntFltRequests_Type()
)
dfl860HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltRequests.setStatus("current")
_Dfl860HttpAlgCntFltAllowed_Type = Gauge32
_Dfl860HttpAlgCntFltAllowed_Object = MibTableColumn
dfl860HttpAlgCntFltAllowed = _Dfl860HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2, 1, 4),
    _Dfl860HttpAlgCntFltAllowed_Type()
)
dfl860HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltAllowed.setStatus("current")
_Dfl860HttpAlgCntFltBlocked_Type = Gauge32
_Dfl860HttpAlgCntFltBlocked_Object = MibTableColumn
dfl860HttpAlgCntFltBlocked = _Dfl860HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 4, 2, 1, 5),
    _Dfl860HttpAlgCntFltBlocked_Type()
)
dfl860HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HttpAlgCntFltBlocked.setStatus("current")
_Dfl860SmtpAlg_ObjectIdentity = ObjectIdentity
dfl860SmtpAlg = _Dfl860SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5)
)
_Dfl860SmtpAlgTable_Object = MibTable
dfl860SmtpAlgTable = _Dfl860SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl860SmtpAlgTable.setStatus("current")
_Dfl860SmtpAlgEntry_Object = MibTableRow
dfl860SmtpAlgEntry = _Dfl860SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1, 1)
)
dfl860SmtpAlgEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl860SmtpAlgEntry.setStatus("current")


class _Dfl860SmtpAlgIndex_Type(Integer32):
    """Custom type dfl860SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl860SmtpAlgIndex_Object = MibTableColumn
dfl860SmtpAlgIndex = _Dfl860SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1, 1, 1),
    _Dfl860SmtpAlgIndex_Type()
)
dfl860SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860SmtpAlgIndex.setStatus("current")
_Dfl860SmtpAlgName_Type = DisplayString
_Dfl860SmtpAlgName_Object = MibTableColumn
dfl860SmtpAlgName = _Dfl860SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1, 1, 2),
    _Dfl860SmtpAlgName_Type()
)
dfl860SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgName.setStatus("current")
_Dfl860SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl860SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl860SmtpAlgTotCheckedSes = _Dfl860SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1, 1, 3),
    _Dfl860SmtpAlgTotCheckedSes_Type()
)
dfl860SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgTotCheckedSes.setStatus("current")
_Dfl860SmtpAlgTotSpamSes_Type = Gauge32
_Dfl860SmtpAlgTotSpamSes_Object = MibTableColumn
dfl860SmtpAlgTotSpamSes = _Dfl860SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1, 1, 4),
    _Dfl860SmtpAlgTotSpamSes_Type()
)
dfl860SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgTotSpamSes.setStatus("current")
_Dfl860SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl860SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl860SmtpAlgTotDroppedSes = _Dfl860SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 1, 1, 5),
    _Dfl860SmtpAlgTotDroppedSes_Type()
)
dfl860SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgTotDroppedSes.setStatus("current")
_Dfl860SmtpAlgDnsBlTable_Object = MibTable
dfl860SmtpAlgDnsBlTable = _Dfl860SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlTable.setStatus("current")
_Dfl860SmtpAlgDnsBlEntry_Object = MibTableRow
dfl860SmtpAlgDnsBlEntry = _Dfl860SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2, 1)
)
dfl860SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860SmtpAlgIndex"),
    (0, "DFL860-MIB", "dfl860SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl860SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl860SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl860SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl860SmtpAlgDnsBlIndex = _Dfl860SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2, 1, 1),
    _Dfl860SmtpAlgDnsBlIndex_Type()
)
dfl860SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlIndex.setStatus("current")
_Dfl860SmtpAlgDnsBlName_Type = DisplayString
_Dfl860SmtpAlgDnsBlName_Object = MibTableColumn
dfl860SmtpAlgDnsBlName = _Dfl860SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2, 1, 2),
    _Dfl860SmtpAlgDnsBlName_Type()
)
dfl860SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlName.setStatus("current")
_Dfl860SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl860SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl860SmtpAlgDnsBlChecked = _Dfl860SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2, 1, 3),
    _Dfl860SmtpAlgDnsBlChecked_Type()
)
dfl860SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlChecked.setStatus("current")
_Dfl860SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl860SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl860SmtpAlgDnsBlMatched = _Dfl860SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2, 1, 4),
    _Dfl860SmtpAlgDnsBlMatched_Type()
)
dfl860SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlMatched.setStatus("current")
_Dfl860SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl860SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl860SmtpAlgDnsBlFailChecks = _Dfl860SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 9, 5, 2, 1, 5),
    _Dfl860SmtpAlgDnsBlFailChecks_Type()
)
dfl860SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl860DHCPRelay_ObjectIdentity = ObjectIdentity
dfl860DHCPRelay = _Dfl860DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11)
)
_Dfl860DHCPRelayCurClients_Type = Gauge32
_Dfl860DHCPRelayCurClients_Object = MibScalar
dfl860DHCPRelayCurClients = _Dfl860DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 1),
    _Dfl860DHCPRelayCurClients_Type()
)
dfl860DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayCurClients.setStatus("current")
_Dfl860DHCPRelayCurTrans_Type = Gauge32
_Dfl860DHCPRelayCurTrans_Object = MibScalar
dfl860DHCPRelayCurTrans = _Dfl860DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 2),
    _Dfl860DHCPRelayCurTrans_Type()
)
dfl860DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayCurTrans.setStatus("current")
_Dfl860DHCPRelayRejected_Type = Gauge32
_Dfl860DHCPRelayRejected_Object = MibScalar
dfl860DHCPRelayRejected = _Dfl860DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 3),
    _Dfl860DHCPRelayRejected_Type()
)
dfl860DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRejected.setStatus("current")
_Dfl860DHCPRelayRuleTable_Object = MibTable
dfl860DHCPRelayRuleTable = _Dfl860DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleTable.setStatus("current")
_Dfl860DHCPRelayRuleEntry_Object = MibTableRow
dfl860DHCPRelayRuleEntry = _Dfl860DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1)
)
dfl860DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL860-MIB", "dfl860DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleEntry.setStatus("current")


class _Dfl860DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl860DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl860DHCPRelayRuleIndex_Object = MibTableColumn
dfl860DHCPRelayRuleIndex = _Dfl860DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1, 1),
    _Dfl860DHCPRelayRuleIndex_Type()
)
dfl860DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleIndex.setStatus("current")
_Dfl860DHCPRelayRuleName_Type = DisplayString
_Dfl860DHCPRelayRuleName_Object = MibTableColumn
dfl860DHCPRelayRuleName = _Dfl860DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1, 2),
    _Dfl860DHCPRelayRuleName_Type()
)
dfl860DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleName.setStatus("current")
_Dfl860DHCPRelayRuleHits_Type = Gauge32
_Dfl860DHCPRelayRuleHits_Object = MibTableColumn
dfl860DHCPRelayRuleHits = _Dfl860DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1, 3),
    _Dfl860DHCPRelayRuleHits_Type()
)
dfl860DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleHits.setStatus("current")
_Dfl860DHCPRelayRuleCurClients_Type = Gauge32
_Dfl860DHCPRelayRuleCurClients_Object = MibTableColumn
dfl860DHCPRelayRuleCurClients = _Dfl860DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1, 4),
    _Dfl860DHCPRelayRuleCurClients_Type()
)
dfl860DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleCurClients.setStatus("current")
_Dfl860DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl860DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl860DHCPRelayRuleRejCliPkts = _Dfl860DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1, 5),
    _Dfl860DHCPRelayRuleRejCliPkts_Type()
)
dfl860DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl860DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl860DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl860DHCPRelayRuleRejSrvPkts = _Dfl860DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 11, 4, 1, 6),
    _Dfl860DHCPRelayRuleRejSrvPkts_Type()
)
dfl860DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl860HA_ObjectIdentity = ObjectIdentity
dfl860HA = _Dfl860HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 12)
)
_Dfl860HASyncSendQueueLength_Type = Gauge32
_Dfl860HASyncSendQueueLength_Object = MibScalar
dfl860HASyncSendQueueLength = _Dfl860HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 12, 1),
    _Dfl860HASyncSendQueueLength_Type()
)
dfl860HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HASyncSendQueueLength.setStatus("current")
_Dfl860HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl860HASyncSendQueueUsagePkt_Object = MibScalar
dfl860HASyncSendQueueUsagePkt = _Dfl860HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 12, 2),
    _Dfl860HASyncSendQueueUsagePkt_Type()
)
dfl860HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HASyncSendQueueUsagePkt.setStatus("current")
_Dfl860HASyncSendQueueUsageOct_Type = Gauge32
_Dfl860HASyncSendQueueUsageOct_Object = MibScalar
dfl860HASyncSendQueueUsageOct = _Dfl860HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 12, 3),
    _Dfl860HASyncSendQueueUsageOct_Type()
)
dfl860HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HASyncSendQueueUsageOct.setStatus("current")
_Dfl860HASyncSentPackets_Type = Counter32
_Dfl860HASyncSentPackets_Object = MibScalar
dfl860HASyncSentPackets = _Dfl860HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 12, 4),
    _Dfl860HASyncSentPackets_Type()
)
dfl860HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HASyncSentPackets.setStatus("current")
_Dfl860HASyncSendResentPackets_Type = Counter32
_Dfl860HASyncSendResentPackets_Object = MibScalar
dfl860HASyncSendResentPackets = _Dfl860HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 1, 2, 12, 5),
    _Dfl860HASyncSendResentPackets_Type()
)
dfl860HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860HASyncSendResentPackets.setStatus("current")
_Dfl860reg_ObjectIdentity = ObjectIdentity
dfl860reg = _Dfl860reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2)
)
_Dfl860MibModules_ObjectIdentity = ObjectIdentity
dfl860MibModules = _Dfl860MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 1)
)
_Dfl860MibConfs_ObjectIdentity = ObjectIdentity
dfl860MibConfs = _Dfl860MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 2)
)
_Dfl860StatsConformance_ObjectIdentity = ObjectIdentity
dfl860StatsConformance = _Dfl860StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 2, 1)
)
_Dfl860MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl860MibObjectGroups = _Dfl860MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3)
)
_Dfl860StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl860StatsRegGroups = _Dfl860StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1)
)

# Managed Objects groups

dfl860SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 1)
)
dfl860SystemObjectGroup.setObjects(
      *(("DFL860-MIB", "dfl860SysCpuLoad"),
        ("DFL860-MIB", "dfl860SysForwardedBits"),
        ("DFL860-MIB", "dfl860SysForwardedPackets"),
        ("DFL860-MIB", "dfl860SysBuffUse"),
        ("DFL860-MIB", "dfl860SysConns"),
        ("DFL860-MIB", "dfl860HWSensorName"),
        ("DFL860-MIB", "dfl860HWSensorValue"),
        ("DFL860-MIB", "dfl860HWSensorUnit"),
        ("DFL860-MIB", "dfl860SysMemUsage"),
        ("DFL860-MIB", "dfl860SysTimerUsage"),
        ("DFL860-MIB", "dfl860SysConnOPS"),
        ("DFL860-MIB", "dfl860SysConnCPS"),
        ("DFL860-MIB", "dfl860SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl860SystemObjectGroup.setStatus("current")

dfl860IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 2)
)
dfl860IPsecObjectGroup.setObjects(
      *(("DFL860-MIB", "dfl860IPsecPhaseOneActive"),
        ("DFL860-MIB", "dfl860IPsecPhaseOneAggrModeDone"),
        ("DFL860-MIB", "dfl860IPsecQuickModeActive"),
        ("DFL860-MIB", "dfl860IPsecPhaseOneDone"),
        ("DFL860-MIB", "dfl860IPsecPhaseOneFailed"),
        ("DFL860-MIB", "dfl860IPsecPhaseOneRekeyed"),
        ("DFL860-MIB", "dfl860IPsecQuickModeDone"),
        ("DFL860-MIB", "dfl860IPsecQuickModeFailed"),
        ("DFL860-MIB", "dfl860IPsecInfoDone"),
        ("DFL860-MIB", "dfl860IPsecInfoFailed"),
        ("DFL860-MIB", "dfl860IPsecInOctetsComp"),
        ("DFL860-MIB", "dfl860IPsecInOctetsUncomp"),
        ("DFL860-MIB", "dfl860IPsecOutOctetsComp"),
        ("DFL860-MIB", "dfl860IPsecOutOctetsUncomp"),
        ("DFL860-MIB", "dfl860IPsecForwardedOctetsComp"),
        ("DFL860-MIB", "dfl860IPsecForwardedOctetsUcomp"),
        ("DFL860-MIB", "dfl860IPsecInPackets"),
        ("DFL860-MIB", "dfl860IPsecOutPackets"),
        ("DFL860-MIB", "dfl860IPsecForwardedPackets"),
        ("DFL860-MIB", "dfl860IPsecActiveTransforms"),
        ("DFL860-MIB", "dfl860IPsecTotalTransforms"),
        ("DFL860-MIB", "dfl860IPsecOutOfTransforms"),
        ("DFL860-MIB", "dfl860IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl860IPsecObjectGroup.setStatus("current")

dfl860StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 3)
)
dfl860StateCountersGroup.setObjects(
      *(("DFL860-MIB", "dfl860SysPscTcpSyn"),
        ("DFL860-MIB", "dfl860SysPscTcpOpen"),
        ("DFL860-MIB", "dfl860SysPscTcpFin"),
        ("DFL860-MIB", "dfl860SysPscUdp"),
        ("DFL860-MIB", "dfl860SysPscIcmp"),
        ("DFL860-MIB", "dfl860SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl860StateCountersGroup.setStatus("current")

dfl860IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 4)
)
dfl860IPPoolGroup.setObjects(
      *(("DFL860-MIB", "dfl860IPPoolsNumber"),
        ("DFL860-MIB", "dfl860IPPoolName"),
        ("DFL860-MIB", "dfl860IPPoolPrepare"),
        ("DFL860-MIB", "dfl860IPPoolFree"),
        ("DFL860-MIB", "dfl860IPPoolMisses"),
        ("DFL860-MIB", "dfl860IPPoolClientFails"),
        ("DFL860-MIB", "dfl860IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl860IPPoolGroup.setStatus("current")

dfl860DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 5)
)
dfl860DHCPServerGroup.setObjects(
      *(("DFL860-MIB", "dfl860DHCPTotalRejected"),
        ("DFL860-MIB", "dfl860DHCPRuleName"),
        ("DFL860-MIB", "dfl860DHCPRuleUsage"),
        ("DFL860-MIB", "dfl860DHCPRuleUsagePercent"),
        ("DFL860-MIB", "dfl860DHCPActiveClients"),
        ("DFL860-MIB", "dfl860DHCPActiveClientsPercent"),
        ("DFL860-MIB", "dfl860DHCPRejectedRequests"),
        ("DFL860-MIB", "dfl860DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl860DHCPServerGroup.setStatus("current")

dfl860RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 6)
)
dfl860RuleUseGroup.setObjects(
      *(("DFL860-MIB", "dfl860RuleName"),
        ("DFL860-MIB", "dfl860RuleUse"))
)
if mibBuilder.loadTexts:
    dfl860RuleUseGroup.setStatus("current")

dfl860UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 7)
)
dfl860UserAuthGroup.setObjects(
      *(("DFL860-MIB", "dfl860UserAuthHTTPUsers"),
        ("DFL860-MIB", "dfl860UserAuthXAUTHUsers"),
        ("DFL860-MIB", "dfl860UserAuthHTTPSUsers"),
        ("DFL860-MIB", "dfl860UserAuthPPPUsers"),
        ("DFL860-MIB", "dfl860UserAuthEAPUsers"),
        ("DFL860-MIB", "dfl860UserAuthRuleName"),
        ("DFL860-MIB", "dfl860UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl860UserAuthGroup.setStatus("current")

dfl860IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 8)
)
dfl860IfStatsGroup.setObjects(
      *(("DFL860-MIB", "dfl860IfName"),
        ("DFL860-MIB", "dfl860IfFragsIn"),
        ("DFL860-MIB", "dfl860IfFragReassOk"),
        ("DFL860-MIB", "dfl860IfFragReassFail"),
        ("DFL860-MIB", "dfl860IfPktsInCnt"),
        ("DFL860-MIB", "dfl860IfPktsOutCnt"),
        ("DFL860-MIB", "dfl860IfBitsInCnt"),
        ("DFL860-MIB", "dfl860IfBitsOutCnt"),
        ("DFL860-MIB", "dfl860IfPktsTotCnt"),
        ("DFL860-MIB", "dfl860IfBitsTotCnt"),
        ("DFL860-MIB", "dfl860IfHCPktsInCnt"),
        ("DFL860-MIB", "dfl860IfHCPktsOutCnt"),
        ("DFL860-MIB", "dfl860IfHCBitsInCnt"),
        ("DFL860-MIB", "dfl860IfHCBitsOutCnt"),
        ("DFL860-MIB", "dfl860IfHCPktsTotCnt"),
        ("DFL860-MIB", "dfl860IfHCBitsTotCnt"),
        ("DFL860-MIB", "dfl860IfRxRingFifoErrors"),
        ("DFL860-MIB", "dfl860IfRxDespools"),
        ("DFL860-MIB", "dfl860IfRxAvgUse"),
        ("DFL860-MIB", "dfl860IfRxRingSaturation"),
        ("DFL860-MIB", "dfl860RxRingFlooded"),
        ("DFL860-MIB", "dfl860IfTxDespools"),
        ("DFL860-MIB", "dfl860IfTxAvgUse"),
        ("DFL860-MIB", "dfl860IfTxRingSaturation"),
        ("DFL860-MIB", "dfl860RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl860IfStatsGroup.setStatus("current")

dfl860LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 9)
)
dfl860LinkMonitorGroup.setObjects(
      *(("DFL860-MIB", "dfl860LinkMonGrp"),
        ("DFL860-MIB", "dfl860LinkMonGrpName"),
        ("DFL860-MIB", "dfl860LinkMonGrpHostsUp"),
        ("DFL860-MIB", "dfl860LinkMonHostId"),
        ("DFL860-MIB", "dfl860LinkMonHostShortTermLoss"),
        ("DFL860-MIB", "dfl860LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl860LinkMonitorGroup.setStatus("current")

dfl860PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 10)
)
dfl860PipesObjectGroup.setObjects(
      *(("DFL860-MIB", "dfl860PipeUsers"),
        ("DFL860-MIB", "dfl860PipeName"),
        ("DFL860-MIB", "dfl860PipeMinPrec"),
        ("DFL860-MIB", "dfl860PipeMaxPrec"),
        ("DFL860-MIB", "dfl860PipeDefPrec"),
        ("DFL860-MIB", "dfl860PipeNumPrec"),
        ("DFL860-MIB", "dfl860PipeNumUsers"),
        ("DFL860-MIB", "dfl860PipeCurrentBps"),
        ("DFL860-MIB", "dfl860PipeCurrentPps"),
        ("DFL860-MIB", "dfl860PipeDelayedPackets"),
        ("DFL860-MIB", "dfl860PipeDropedPackets"),
        ("DFL860-MIB", "dfl860PipePrec"),
        ("DFL860-MIB", "dfl860PipePrecBps"),
        ("DFL860-MIB", "dfl860PipePrecTotalPps"),
        ("DFL860-MIB", "dfl860PipePrecReservedBps"),
        ("DFL860-MIB", "dfl860PipePrecDynLimBps"),
        ("DFL860-MIB", "dfl860PipePrecDynUsrLimBps"),
        ("DFL860-MIB", "dfl860PipePrecDelayedPackets"),
        ("DFL860-MIB", "dfl860PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl860PipesObjectGroup.setStatus("current")

dfl860DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 12)
)
dfl860DHCPRelayObjectGroup.setObjects(
      *(("DFL860-MIB", "dfl860DHCPRelayCurClients"),
        ("DFL860-MIB", "dfl860DHCPRelayCurTrans"),
        ("DFL860-MIB", "dfl860DHCPRelayRejected"),
        ("DFL860-MIB", "dfl860DHCPRelayRuleName"),
        ("DFL860-MIB", "dfl860DHCPRelayRuleHits"),
        ("DFL860-MIB", "dfl860DHCPRelayRuleCurClients"),
        ("DFL860-MIB", "dfl860DHCPRelayRuleRejCliPkts"),
        ("DFL860-MIB", "dfl860DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl860DHCPRelayObjectGroup.setStatus("current")

dfl860AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 13)
)
dfl860AlgGroup.setObjects(
      *(("DFL860-MIB", "dfl860AlgSessions"),
        ("DFL860-MIB", "dfl860AlgConnections"),
        ("DFL860-MIB", "dfl860AlgTCPStreams"),
        ("DFL860-MIB", "dfl860HttpAlgName"),
        ("DFL860-MIB", "dfl860HttpAlgTotalRequested"),
        ("DFL860-MIB", "dfl860HttpAlgTotalAllowed"),
        ("DFL860-MIB", "dfl860HttpAlgTotalBlocked"),
        ("DFL860-MIB", "dfl860HttpAlgCntFltName"),
        ("DFL860-MIB", "dfl860HttpAlgCntFltRequests"),
        ("DFL860-MIB", "dfl860HttpAlgCntFltAllowed"),
        ("DFL860-MIB", "dfl860HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl860AlgGroup.setStatus("current")

dfl860HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 14)
)
dfl860HAGroup.setObjects(
      *(("DFL860-MIB", "dfl860HASyncSendQueueLength"),
        ("DFL860-MIB", "dfl860HASyncSendQueueUsagePkt"),
        ("DFL860-MIB", "dfl860HASyncSendQueueUsageOct"),
        ("DFL860-MIB", "dfl860HASyncSentPackets"),
        ("DFL860-MIB", "dfl860HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl860HAGroup.setStatus("current")

dfl860IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 15)
)
dfl860IfVlanGroup.setObjects(
      *(("DFL860-MIB", "dfl860IfVlanUntaggedInPkts"),
        ("DFL860-MIB", "dfl860IfVlanUntaggedOutPkts"),
        ("DFL860-MIB", "dfl860IfVlanUntaggedTotPkts"),
        ("DFL860-MIB", "dfl860IfVlanUntaggedInOctets"),
        ("DFL860-MIB", "dfl860IfVlanUntaggedOutOctets"),
        ("DFL860-MIB", "dfl860IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl860IfVlanGroup.setStatus("current")

dfl860SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 16)
)
dfl860SmtpAlgGroup.setObjects(
      *(("DFL860-MIB", "dfl860SmtpAlgName"),
        ("DFL860-MIB", "dfl860SmtpAlgTotCheckedSes"),
        ("DFL860-MIB", "dfl860SmtpAlgTotSpamSes"),
        ("DFL860-MIB", "dfl860SmtpAlgTotDroppedSes"),
        ("DFL860-MIB", "dfl860SmtpAlgDnsBlName"),
        ("DFL860-MIB", "dfl860SmtpAlgDnsBlChecked"),
        ("DFL860-MIB", "dfl860SmtpAlgDnsBlMatched"),
        ("DFL860-MIB", "dfl860SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl860SmtpAlgGroup.setStatus("current")

dfl860SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 3, 1, 17)
)
dfl860SysTCPGroup.setObjects(
      *(("DFL860-MIB", "dfl860SysTCPRecvSmall"),
        ("DFL860-MIB", "dfl860SysTCPRecvLarge"),
        ("DFL860-MIB", "dfl860SysTCPSendSmall"),
        ("DFL860-MIB", "dfl860SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl860SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl860StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl860StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL860-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "utmFirewall": utmFirewall,
       "dfl860": dfl860,
       "dfl860OS": dfl860OS,
       "dfl860OSStats": dfl860OSStats,
       "dfl860System": dfl860System,
       "dfl860SysCpuLoad": dfl860SysCpuLoad,
       "dfl860SysForwardedBits": dfl860SysForwardedBits,
       "dfl860SysForwardedPackets": dfl860SysForwardedPackets,
       "dfl860SysBuffUse": dfl860SysBuffUse,
       "dfl860SysConns": dfl860SysConns,
       "dfl860SysPerStateCounters": dfl860SysPerStateCounters,
       "dfl860SysPscTcpSyn": dfl860SysPscTcpSyn,
       "dfl860SysPscTcpOpen": dfl860SysPscTcpOpen,
       "dfl860SysPscTcpFin": dfl860SysPscTcpFin,
       "dfl860SysPscUdp": dfl860SysPscUdp,
       "dfl860SysPscIcmp": dfl860SysPscIcmp,
       "dfl860SysPscOther": dfl860SysPscOther,
       "dfl860IfStatsTable": dfl860IfStatsTable,
       "dfl860IfStatsEntry": dfl860IfStatsEntry,
       "dfl860IfStatsIndex": dfl860IfStatsIndex,
       "dfl860IfName": dfl860IfName,
       "dfl860IfFragsIn": dfl860IfFragsIn,
       "dfl860IfFragReassOk": dfl860IfFragReassOk,
       "dfl860IfFragReassFail": dfl860IfFragReassFail,
       "dfl860IfPktsInCnt": dfl860IfPktsInCnt,
       "dfl860IfPktsOutCnt": dfl860IfPktsOutCnt,
       "dfl860IfBitsInCnt": dfl860IfBitsInCnt,
       "dfl860IfBitsOutCnt": dfl860IfBitsOutCnt,
       "dfl860IfPktsTotCnt": dfl860IfPktsTotCnt,
       "dfl860IfBitsTotCnt": dfl860IfBitsTotCnt,
       "dfl860IfHCPktsInCnt": dfl860IfHCPktsInCnt,
       "dfl860IfHCPktsOutCnt": dfl860IfHCPktsOutCnt,
       "dfl860IfHCBitsInCnt": dfl860IfHCBitsInCnt,
       "dfl860IfHCBitsOutCnt": dfl860IfHCBitsOutCnt,
       "dfl860IfHCPktsTotCnt": dfl860IfHCPktsTotCnt,
       "dfl860IfHCBitsTotCnt": dfl860IfHCBitsTotCnt,
       "dfl860IfRxRingTable": dfl860IfRxRingTable,
       "dfl860IfRxRingEntry": dfl860IfRxRingEntry,
       "dfl860IfRxRingIndex": dfl860IfRxRingIndex,
       "dfl860IfRxRingFifoErrors": dfl860IfRxRingFifoErrors,
       "dfl860IfRxDespools": dfl860IfRxDespools,
       "dfl860IfRxAvgUse": dfl860IfRxAvgUse,
       "dfl860IfRxRingSaturation": dfl860IfRxRingSaturation,
       "dfl860RxRingFlooded": dfl860RxRingFlooded,
       "dfl860IfTxRingTable": dfl860IfTxRingTable,
       "dfl860IfTxRingEntry": dfl860IfTxRingEntry,
       "dfl860IfTxRingIndex": dfl860IfTxRingIndex,
       "dfl860IfTxDespools": dfl860IfTxDespools,
       "dfl860IfTxAvgUse": dfl860IfTxAvgUse,
       "dfl860IfTxRingSaturation": dfl860IfTxRingSaturation,
       "dfl860RxTingFlooded": dfl860RxTingFlooded,
       "dfl860IfVlanStatsTable": dfl860IfVlanStatsTable,
       "dfl860IfVlanStatsEntry": dfl860IfVlanStatsEntry,
       "dfl860IfVlanIndex": dfl860IfVlanIndex,
       "dfl860IfVlanUntaggedInPkts": dfl860IfVlanUntaggedInPkts,
       "dfl860IfVlanUntaggedOutPkts": dfl860IfVlanUntaggedOutPkts,
       "dfl860IfVlanUntaggedTotPkts": dfl860IfVlanUntaggedTotPkts,
       "dfl860IfVlanUntaggedInOctets": dfl860IfVlanUntaggedInOctets,
       "dfl860IfVlanUntaggedOutOctets": dfl860IfVlanUntaggedOutOctets,
       "dfl860IfVlanUntaggedTotOctets": dfl860IfVlanUntaggedTotOctets,
       "dfl860HWSensorTable": dfl860HWSensorTable,
       "dfl860HWSensorEntry": dfl860HWSensorEntry,
       "dfl860HWSensorIndex": dfl860HWSensorIndex,
       "dfl860HWSensorName": dfl860HWSensorName,
       "dfl860HWSensorValue": dfl860HWSensorValue,
       "dfl860HWSensorUnit": dfl860HWSensorUnit,
       "dfl860SysMemUsage": dfl860SysMemUsage,
       "dfl860SysTCPUsage": dfl860SysTCPUsage,
       "dfl860SysTCPRecvSmall": dfl860SysTCPRecvSmall,
       "dfl860SysTCPRecvLarge": dfl860SysTCPRecvLarge,
       "dfl860SysTCPSendSmall": dfl860SysTCPSendSmall,
       "dfl860SysTCPSendLarge": dfl860SysTCPSendLarge,
       "dfl860SysTimerUsage": dfl860SysTimerUsage,
       "dfl860SysConnOPS": dfl860SysConnOPS,
       "dfl860SysConnCPS": dfl860SysConnCPS,
       "dfl860SysHCForwardedBits": dfl860SysHCForwardedBits,
       "dfl860VPN": dfl860VPN,
       "dfl860IPsec": dfl860IPsec,
       "dfl860IPsecGlobal": dfl860IPsecGlobal,
       "dfl860IPsecPhaseOneActive": dfl860IPsecPhaseOneActive,
       "dfl860IPsecPhaseOneAggrModeDone": dfl860IPsecPhaseOneAggrModeDone,
       "dfl860IPsecQuickModeActive": dfl860IPsecQuickModeActive,
       "dfl860IPsecPhaseOneDone": dfl860IPsecPhaseOneDone,
       "dfl860IPsecPhaseOneFailed": dfl860IPsecPhaseOneFailed,
       "dfl860IPsecPhaseOneRekeyed": dfl860IPsecPhaseOneRekeyed,
       "dfl860IPsecQuickModeDone": dfl860IPsecQuickModeDone,
       "dfl860IPsecQuickModeFailed": dfl860IPsecQuickModeFailed,
       "dfl860IPsecInfoDone": dfl860IPsecInfoDone,
       "dfl860IPsecInfoFailed": dfl860IPsecInfoFailed,
       "dfl860IPsecInOctetsComp": dfl860IPsecInOctetsComp,
       "dfl860IPsecInOctetsUncomp": dfl860IPsecInOctetsUncomp,
       "dfl860IPsecOutOctetsComp": dfl860IPsecOutOctetsComp,
       "dfl860IPsecOutOctetsUncomp": dfl860IPsecOutOctetsUncomp,
       "dfl860IPsecForwardedOctetsComp": dfl860IPsecForwardedOctetsComp,
       "dfl860IPsecForwardedOctetsUcomp": dfl860IPsecForwardedOctetsUcomp,
       "dfl860IPsecInPackets": dfl860IPsecInPackets,
       "dfl860IPsecOutPackets": dfl860IPsecOutPackets,
       "dfl860IPsecForwardedPackets": dfl860IPsecForwardedPackets,
       "dfl860IPsecActiveTransforms": dfl860IPsecActiveTransforms,
       "dfl860IPsecTotalTransforms": dfl860IPsecTotalTransforms,
       "dfl860IPsecOutOfTransforms": dfl860IPsecOutOfTransforms,
       "dfl860IPsecTotalRekeys": dfl860IPsecTotalRekeys,
       "dfl860Rules": dfl860Rules,
       "dfl860RuleUseTable": dfl860RuleUseTable,
       "dfl860RuleUseEntry": dfl860RuleUseEntry,
       "dfl860RuleIndex": dfl860RuleIndex,
       "dfl860RuleName": dfl860RuleName,
       "dfl860RuleUse": dfl860RuleUse,
       "dfl860IPPools": dfl860IPPools,
       "dfl860IPPoolsNumber": dfl860IPPoolsNumber,
       "dfl860IPPoolTable": dfl860IPPoolTable,
       "dfl860IPPoolEntry": dfl860IPPoolEntry,
       "dfl860IPPoolIndex": dfl860IPPoolIndex,
       "dfl860IPPoolName": dfl860IPPoolName,
       "dfl860IPPoolPrepare": dfl860IPPoolPrepare,
       "dfl860IPPoolFree": dfl860IPPoolFree,
       "dfl860IPPoolMisses": dfl860IPPoolMisses,
       "dfl860IPPoolClientFails": dfl860IPPoolClientFails,
       "dfl860IPPoolUsed": dfl860IPPoolUsed,
       "dfl860DHCPServer": dfl860DHCPServer,
       "dfl860DHCPTotalRejected": dfl860DHCPTotalRejected,
       "dfl860DHCPRuleTable": dfl860DHCPRuleTable,
       "dfl860DHCPRuleEntry": dfl860DHCPRuleEntry,
       "dfl860DHCPRuleIndex": dfl860DHCPRuleIndex,
       "dfl860DHCPRuleName": dfl860DHCPRuleName,
       "dfl860DHCPRuleUsage": dfl860DHCPRuleUsage,
       "dfl860DHCPRuleUsagePercent": dfl860DHCPRuleUsagePercent,
       "dfl860DHCPActiveClients": dfl860DHCPActiveClients,
       "dfl860DHCPActiveClientsPercent": dfl860DHCPActiveClientsPercent,
       "dfl860DHCPRejectedRequests": dfl860DHCPRejectedRequests,
       "dfl860DHCPTotalLeases": dfl860DHCPTotalLeases,
       "dfl860UserAuth": dfl860UserAuth,
       "dfl860UserAuthHTTPUsers": dfl860UserAuthHTTPUsers,
       "dfl860UserAuthXAUTHUsers": dfl860UserAuthXAUTHUsers,
       "dfl860UserAuthHTTPSUsers": dfl860UserAuthHTTPSUsers,
       "dfl860UserAuthPPPUsers": dfl860UserAuthPPPUsers,
       "dfl860UserAuthEAPUsers": dfl860UserAuthEAPUsers,
       "dfl860UserAuthRuleUseTable": dfl860UserAuthRuleUseTable,
       "dfl860UserAuthRuleUseEntry": dfl860UserAuthRuleUseEntry,
       "dfl860UserAuthRuleIndex": dfl860UserAuthRuleIndex,
       "dfl860UserAuthRuleName": dfl860UserAuthRuleName,
       "dfl860UserAuthRuleUse": dfl860UserAuthRuleUse,
       "dfl860LinkMonitor": dfl860LinkMonitor,
       "dfl860LinkMonGrp": dfl860LinkMonGrp,
       "dfl860LinkMonGrpTable": dfl860LinkMonGrpTable,
       "dfl860LinkMonGrpEntry": dfl860LinkMonGrpEntry,
       "dfl860LinkMonGrpIndex": dfl860LinkMonGrpIndex,
       "dfl860LinkMonGrpName": dfl860LinkMonGrpName,
       "dfl860LinkMonGrpHostsUp": dfl860LinkMonGrpHostsUp,
       "dfl860LinkMonHostTable": dfl860LinkMonHostTable,
       "dfl860LinkMonHostEntry": dfl860LinkMonHostEntry,
       "dfl860LinkMonHostIndex": dfl860LinkMonHostIndex,
       "dfl860LinkMonHostId": dfl860LinkMonHostId,
       "dfl860LinkMonHostShortTermLoss": dfl860LinkMonHostShortTermLoss,
       "dfl860LinkMonHostPacketsLost": dfl860LinkMonHostPacketsLost,
       "dfl860Pipes": dfl860Pipes,
       "dfl860PipeUsers": dfl860PipeUsers,
       "dfl860PipeTable": dfl860PipeTable,
       "dfl860PipeEntry": dfl860PipeEntry,
       "dfl860PipeIndex": dfl860PipeIndex,
       "dfl860PipeName": dfl860PipeName,
       "dfl860PipeMinPrec": dfl860PipeMinPrec,
       "dfl860PipeMaxPrec": dfl860PipeMaxPrec,
       "dfl860PipeDefPrec": dfl860PipeDefPrec,
       "dfl860PipeNumPrec": dfl860PipeNumPrec,
       "dfl860PipeNumUsers": dfl860PipeNumUsers,
       "dfl860PipeCurrentBps": dfl860PipeCurrentBps,
       "dfl860PipeCurrentPps": dfl860PipeCurrentPps,
       "dfl860PipeDelayedPackets": dfl860PipeDelayedPackets,
       "dfl860PipeDropedPackets": dfl860PipeDropedPackets,
       "dfl860PipePrecTable": dfl860PipePrecTable,
       "dfl860PipePrecEntry": dfl860PipePrecEntry,
       "dfl860PipePrecIndex": dfl860PipePrecIndex,
       "dfl860PipePrec": dfl860PipePrec,
       "dfl860PipePrecBps": dfl860PipePrecBps,
       "dfl860PipePrecTotalPps": dfl860PipePrecTotalPps,
       "dfl860PipePrecReservedBps": dfl860PipePrecReservedBps,
       "dfl860PipePrecDynLimBps": dfl860PipePrecDynLimBps,
       "dfl860PipePrecDynUsrLimBps": dfl860PipePrecDynUsrLimBps,
       "dfl860PipePrecDelayedPackets": dfl860PipePrecDelayedPackets,
       "dfl860PipePrecDropedPackets": dfl860PipePrecDropedPackets,
       "dfl860ALG": dfl860ALG,
       "dfl860AlgSessions": dfl860AlgSessions,
       "dfl860AlgConnections": dfl860AlgConnections,
       "dfl860AlgTCPStreams": dfl860AlgTCPStreams,
       "dfl860HttpAlg": dfl860HttpAlg,
       "dfl860HttpAlgTable": dfl860HttpAlgTable,
       "dfl860HttpAlgEntry": dfl860HttpAlgEntry,
       "dfl860HttpAlgIndex": dfl860HttpAlgIndex,
       "dfl860HttpAlgName": dfl860HttpAlgName,
       "dfl860HttpAlgTotalRequested": dfl860HttpAlgTotalRequested,
       "dfl860HttpAlgTotalAllowed": dfl860HttpAlgTotalAllowed,
       "dfl860HttpAlgTotalBlocked": dfl860HttpAlgTotalBlocked,
       "dfl860HttpAlgCntFltTable": dfl860HttpAlgCntFltTable,
       "dfl860HttpAlgCntFltEntry": dfl860HttpAlgCntFltEntry,
       "dfl860HttpAlgCntFltIndex": dfl860HttpAlgCntFltIndex,
       "dfl860HttpAlgCntFltName": dfl860HttpAlgCntFltName,
       "dfl860HttpAlgCntFltRequests": dfl860HttpAlgCntFltRequests,
       "dfl860HttpAlgCntFltAllowed": dfl860HttpAlgCntFltAllowed,
       "dfl860HttpAlgCntFltBlocked": dfl860HttpAlgCntFltBlocked,
       "dfl860SmtpAlg": dfl860SmtpAlg,
       "dfl860SmtpAlgTable": dfl860SmtpAlgTable,
       "dfl860SmtpAlgEntry": dfl860SmtpAlgEntry,
       "dfl860SmtpAlgIndex": dfl860SmtpAlgIndex,
       "dfl860SmtpAlgName": dfl860SmtpAlgName,
       "dfl860SmtpAlgTotCheckedSes": dfl860SmtpAlgTotCheckedSes,
       "dfl860SmtpAlgTotSpamSes": dfl860SmtpAlgTotSpamSes,
       "dfl860SmtpAlgTotDroppedSes": dfl860SmtpAlgTotDroppedSes,
       "dfl860SmtpAlgDnsBlTable": dfl860SmtpAlgDnsBlTable,
       "dfl860SmtpAlgDnsBlEntry": dfl860SmtpAlgDnsBlEntry,
       "dfl860SmtpAlgDnsBlIndex": dfl860SmtpAlgDnsBlIndex,
       "dfl860SmtpAlgDnsBlName": dfl860SmtpAlgDnsBlName,
       "dfl860SmtpAlgDnsBlChecked": dfl860SmtpAlgDnsBlChecked,
       "dfl860SmtpAlgDnsBlMatched": dfl860SmtpAlgDnsBlMatched,
       "dfl860SmtpAlgDnsBlFailChecks": dfl860SmtpAlgDnsBlFailChecks,
       "dfl860DHCPRelay": dfl860DHCPRelay,
       "dfl860DHCPRelayCurClients": dfl860DHCPRelayCurClients,
       "dfl860DHCPRelayCurTrans": dfl860DHCPRelayCurTrans,
       "dfl860DHCPRelayRejected": dfl860DHCPRelayRejected,
       "dfl860DHCPRelayRuleTable": dfl860DHCPRelayRuleTable,
       "dfl860DHCPRelayRuleEntry": dfl860DHCPRelayRuleEntry,
       "dfl860DHCPRelayRuleIndex": dfl860DHCPRelayRuleIndex,
       "dfl860DHCPRelayRuleName": dfl860DHCPRelayRuleName,
       "dfl860DHCPRelayRuleHits": dfl860DHCPRelayRuleHits,
       "dfl860DHCPRelayRuleCurClients": dfl860DHCPRelayRuleCurClients,
       "dfl860DHCPRelayRuleRejCliPkts": dfl860DHCPRelayRuleRejCliPkts,
       "dfl860DHCPRelayRuleRejSrvPkts": dfl860DHCPRelayRuleRejSrvPkts,
       "dfl860HA": dfl860HA,
       "dfl860HASyncSendQueueLength": dfl860HASyncSendQueueLength,
       "dfl860HASyncSendQueueUsagePkt": dfl860HASyncSendQueueUsagePkt,
       "dfl860HASyncSendQueueUsageOct": dfl860HASyncSendQueueUsageOct,
       "dfl860HASyncSentPackets": dfl860HASyncSentPackets,
       "dfl860HASyncSendResentPackets": dfl860HASyncSendResentPackets,
       "dfl860reg": dfl860reg,
       "dfl860MibModules": dfl860MibModules,
       "dfl860-MIB": dfl860_MIB,
       "dfl860MibConfs": dfl860MibConfs,
       "dfl860StatsConformance": dfl860StatsConformance,
       "dfl860StatsCompliance": dfl860StatsCompliance,
       "dfl860MibObjectGroups": dfl860MibObjectGroups,
       "dfl860StatsRegGroups": dfl860StatsRegGroups,
       "dfl860SystemObjectGroup": dfl860SystemObjectGroup,
       "dfl860IPsecObjectGroup": dfl860IPsecObjectGroup,
       "dfl860StateCountersGroup": dfl860StateCountersGroup,
       "dfl860IPPoolGroup": dfl860IPPoolGroup,
       "dfl860DHCPServerGroup": dfl860DHCPServerGroup,
       "dfl860RuleUseGroup": dfl860RuleUseGroup,
       "dfl860UserAuthGroup": dfl860UserAuthGroup,
       "dfl860IfStatsGroup": dfl860IfStatsGroup,
       "dfl860LinkMonitorGroup": dfl860LinkMonitorGroup,
       "dfl860PipesObjectGroup": dfl860PipesObjectGroup,
       "dfl860DHCPRelayObjectGroup": dfl860DHCPRelayObjectGroup,
       "dfl860AlgGroup": dfl860AlgGroup,
       "dfl860HAGroup": dfl860HAGroup,
       "dfl860IfVlanGroup": dfl860IfVlanGroup,
       "dfl860SmtpAlgGroup": dfl860SmtpAlgGroup,
       "dfl860SysTCPGroup": dfl860SysTCPGroup}
)
