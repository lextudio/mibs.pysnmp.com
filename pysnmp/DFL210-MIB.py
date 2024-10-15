# SNMP MIB module (DFL210-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL210-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:15 2024
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

dfl210_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 1, 2)
)
dfl210_MIB.setRevisions(
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
_IpsFirewall_ObjectIdentity = ObjectIdentity
ipsFirewall = _IpsFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1)
)
_Dfl210_ObjectIdentity = ObjectIdentity
dfl210 = _Dfl210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1)
)
_Dfl210OS_ObjectIdentity = ObjectIdentity
dfl210OS = _Dfl210OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1)
)
_Dfl210OSStats_ObjectIdentity = ObjectIdentity
dfl210OSStats = _Dfl210OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2)
)
_Dfl210System_ObjectIdentity = ObjectIdentity
dfl210System = _Dfl210System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1)
)
_Dfl210SysCpuLoad_Type = Gauge32
_Dfl210SysCpuLoad_Object = MibScalar
dfl210SysCpuLoad = _Dfl210SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 1),
    _Dfl210SysCpuLoad_Type()
)
dfl210SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysCpuLoad.setStatus("current")
_Dfl210SysForwardedBits_Type = Counter32
_Dfl210SysForwardedBits_Object = MibScalar
dfl210SysForwardedBits = _Dfl210SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 2),
    _Dfl210SysForwardedBits_Type()
)
dfl210SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysForwardedBits.setStatus("current")
_Dfl210SysForwardedPackets_Type = Counter32
_Dfl210SysForwardedPackets_Object = MibScalar
dfl210SysForwardedPackets = _Dfl210SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 3),
    _Dfl210SysForwardedPackets_Type()
)
dfl210SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysForwardedPackets.setStatus("current")
_Dfl210SysBuffUse_Type = Gauge32
_Dfl210SysBuffUse_Object = MibScalar
dfl210SysBuffUse = _Dfl210SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 4),
    _Dfl210SysBuffUse_Type()
)
dfl210SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysBuffUse.setStatus("current")
_Dfl210SysConns_Type = Gauge32
_Dfl210SysConns_Object = MibScalar
dfl210SysConns = _Dfl210SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 5),
    _Dfl210SysConns_Type()
)
dfl210SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysConns.setStatus("current")
_Dfl210SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl210SysPerStateCounters = _Dfl210SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6)
)
_Dfl210SysPscTcpSyn_Type = Gauge32
_Dfl210SysPscTcpSyn_Object = MibScalar
dfl210SysPscTcpSyn = _Dfl210SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6, 1),
    _Dfl210SysPscTcpSyn_Type()
)
dfl210SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysPscTcpSyn.setStatus("current")
_Dfl210SysPscTcpOpen_Type = Gauge32
_Dfl210SysPscTcpOpen_Object = MibScalar
dfl210SysPscTcpOpen = _Dfl210SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6, 2),
    _Dfl210SysPscTcpOpen_Type()
)
dfl210SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysPscTcpOpen.setStatus("current")
_Dfl210SysPscTcpFin_Type = Gauge32
_Dfl210SysPscTcpFin_Object = MibScalar
dfl210SysPscTcpFin = _Dfl210SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6, 3),
    _Dfl210SysPscTcpFin_Type()
)
dfl210SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysPscTcpFin.setStatus("current")
_Dfl210SysPscUdp_Type = Gauge32
_Dfl210SysPscUdp_Object = MibScalar
dfl210SysPscUdp = _Dfl210SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6, 4),
    _Dfl210SysPscUdp_Type()
)
dfl210SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysPscUdp.setStatus("current")
_Dfl210SysPscIcmp_Type = Gauge32
_Dfl210SysPscIcmp_Object = MibScalar
dfl210SysPscIcmp = _Dfl210SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6, 5),
    _Dfl210SysPscIcmp_Type()
)
dfl210SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysPscIcmp.setStatus("current")
_Dfl210SysPscOther_Type = Gauge32
_Dfl210SysPscOther_Object = MibScalar
dfl210SysPscOther = _Dfl210SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 6, 6),
    _Dfl210SysPscOther_Type()
)
dfl210SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysPscOther.setStatus("current")
_Dfl210IfStatsTable_Object = MibTable
dfl210IfStatsTable = _Dfl210IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl210IfStatsTable.setStatus("current")
_Dfl210IfStatsEntry_Object = MibTableRow
dfl210IfStatsEntry = _Dfl210IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1)
)
dfl210IfStatsEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl210IfStatsEntry.setStatus("current")


class _Dfl210IfStatsIndex_Type(Integer32):
    """Custom type dfl210IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210IfStatsIndex_Type.__name__ = "Integer32"
_Dfl210IfStatsIndex_Object = MibTableColumn
dfl210IfStatsIndex = _Dfl210IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 1),
    _Dfl210IfStatsIndex_Type()
)
dfl210IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210IfStatsIndex.setStatus("current")
_Dfl210IfName_Type = DisplayString
_Dfl210IfName_Object = MibTableColumn
dfl210IfName = _Dfl210IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 2),
    _Dfl210IfName_Type()
)
dfl210IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfName.setStatus("current")
_Dfl210IfFragsIn_Type = Counter32
_Dfl210IfFragsIn_Object = MibTableColumn
dfl210IfFragsIn = _Dfl210IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 3),
    _Dfl210IfFragsIn_Type()
)
dfl210IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfFragsIn.setStatus("current")
_Dfl210IfFragReassOk_Type = Counter32
_Dfl210IfFragReassOk_Object = MibTableColumn
dfl210IfFragReassOk = _Dfl210IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 4),
    _Dfl210IfFragReassOk_Type()
)
dfl210IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfFragReassOk.setStatus("current")
_Dfl210IfFragReassFail_Type = Counter32
_Dfl210IfFragReassFail_Object = MibTableColumn
dfl210IfFragReassFail = _Dfl210IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 5),
    _Dfl210IfFragReassFail_Type()
)
dfl210IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfFragReassFail.setStatus("current")
_Dfl210IfPktsInCnt_Type = Counter32
_Dfl210IfPktsInCnt_Object = MibTableColumn
dfl210IfPktsInCnt = _Dfl210IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 6),
    _Dfl210IfPktsInCnt_Type()
)
dfl210IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfPktsInCnt.setStatus("current")
_Dfl210IfPktsOutCnt_Type = Counter32
_Dfl210IfPktsOutCnt_Object = MibTableColumn
dfl210IfPktsOutCnt = _Dfl210IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 7),
    _Dfl210IfPktsOutCnt_Type()
)
dfl210IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfPktsOutCnt.setStatus("current")
_Dfl210IfBitsInCnt_Type = Counter32
_Dfl210IfBitsInCnt_Object = MibTableColumn
dfl210IfBitsInCnt = _Dfl210IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 8),
    _Dfl210IfBitsInCnt_Type()
)
dfl210IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfBitsInCnt.setStatus("current")
_Dfl210IfBitsOutCnt_Type = Counter32
_Dfl210IfBitsOutCnt_Object = MibTableColumn
dfl210IfBitsOutCnt = _Dfl210IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 9),
    _Dfl210IfBitsOutCnt_Type()
)
dfl210IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfBitsOutCnt.setStatus("current")
_Dfl210IfPktsTotCnt_Type = Counter32
_Dfl210IfPktsTotCnt_Object = MibTableColumn
dfl210IfPktsTotCnt = _Dfl210IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 10),
    _Dfl210IfPktsTotCnt_Type()
)
dfl210IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfPktsTotCnt.setStatus("current")
_Dfl210IfBitsTotCnt_Type = Counter32
_Dfl210IfBitsTotCnt_Object = MibTableColumn
dfl210IfBitsTotCnt = _Dfl210IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 11),
    _Dfl210IfBitsTotCnt_Type()
)
dfl210IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfBitsTotCnt.setStatus("current")
_Dfl210IfHCPktsInCnt_Type = Counter64
_Dfl210IfHCPktsInCnt_Object = MibTableColumn
dfl210IfHCPktsInCnt = _Dfl210IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 12),
    _Dfl210IfHCPktsInCnt_Type()
)
dfl210IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfHCPktsInCnt.setStatus("current")
_Dfl210IfHCPktsOutCnt_Type = Counter64
_Dfl210IfHCPktsOutCnt_Object = MibTableColumn
dfl210IfHCPktsOutCnt = _Dfl210IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 13),
    _Dfl210IfHCPktsOutCnt_Type()
)
dfl210IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfHCPktsOutCnt.setStatus("current")
_Dfl210IfHCBitsInCnt_Type = Counter64
_Dfl210IfHCBitsInCnt_Object = MibTableColumn
dfl210IfHCBitsInCnt = _Dfl210IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 14),
    _Dfl210IfHCBitsInCnt_Type()
)
dfl210IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfHCBitsInCnt.setStatus("current")
_Dfl210IfHCBitsOutCnt_Type = Counter64
_Dfl210IfHCBitsOutCnt_Object = MibTableColumn
dfl210IfHCBitsOutCnt = _Dfl210IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 15),
    _Dfl210IfHCBitsOutCnt_Type()
)
dfl210IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfHCBitsOutCnt.setStatus("current")
_Dfl210IfHCPktsTotCnt_Type = Counter64
_Dfl210IfHCPktsTotCnt_Object = MibTableColumn
dfl210IfHCPktsTotCnt = _Dfl210IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 16),
    _Dfl210IfHCPktsTotCnt_Type()
)
dfl210IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfHCPktsTotCnt.setStatus("current")
_Dfl210IfHCBitsTotCnt_Type = Counter64
_Dfl210IfHCBitsTotCnt_Object = MibTableColumn
dfl210IfHCBitsTotCnt = _Dfl210IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 7, 1, 17),
    _Dfl210IfHCBitsTotCnt_Type()
)
dfl210IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfHCBitsTotCnt.setStatus("current")
_Dfl210IfRxRingTable_Object = MibTable
dfl210IfRxRingTable = _Dfl210IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl210IfRxRingTable.setStatus("current")
_Dfl210IfRxRingEntry_Object = MibTableRow
dfl210IfRxRingEntry = _Dfl210IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1)
)
dfl210IfRxRingEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl210IfRxRingEntry.setStatus("current")


class _Dfl210IfRxRingIndex_Type(Integer32):
    """Custom type dfl210IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl210IfRxRingIndex_Object = MibTableColumn
dfl210IfRxRingIndex = _Dfl210IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1, 1),
    _Dfl210IfRxRingIndex_Type()
)
dfl210IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210IfRxRingIndex.setStatus("current")
_Dfl210IfRxRingFifoErrors_Type = Counter32
_Dfl210IfRxRingFifoErrors_Object = MibTableColumn
dfl210IfRxRingFifoErrors = _Dfl210IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1, 2),
    _Dfl210IfRxRingFifoErrors_Type()
)
dfl210IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfRxRingFifoErrors.setStatus("current")
_Dfl210IfRxDespools_Type = Gauge32
_Dfl210IfRxDespools_Object = MibTableColumn
dfl210IfRxDespools = _Dfl210IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1, 3),
    _Dfl210IfRxDespools_Type()
)
dfl210IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfRxDespools.setStatus("current")
_Dfl210IfRxAvgUse_Type = Gauge32
_Dfl210IfRxAvgUse_Object = MibTableColumn
dfl210IfRxAvgUse = _Dfl210IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1, 4),
    _Dfl210IfRxAvgUse_Type()
)
dfl210IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfRxAvgUse.setStatus("current")
_Dfl210IfRxRingSaturation_Type = Gauge32
_Dfl210IfRxRingSaturation_Object = MibTableColumn
dfl210IfRxRingSaturation = _Dfl210IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1, 5),
    _Dfl210IfRxRingSaturation_Type()
)
dfl210IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfRxRingSaturation.setStatus("current")
_Dfl210RxRingFlooded_Type = Gauge32
_Dfl210RxRingFlooded_Object = MibTableColumn
dfl210RxRingFlooded = _Dfl210RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 8, 1, 6),
    _Dfl210RxRingFlooded_Type()
)
dfl210RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210RxRingFlooded.setStatus("current")
_Dfl210IfTxRingTable_Object = MibTable
dfl210IfTxRingTable = _Dfl210IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl210IfTxRingTable.setStatus("current")
_Dfl210IfTxRingEntry_Object = MibTableRow
dfl210IfTxRingEntry = _Dfl210IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9, 1)
)
dfl210IfTxRingEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl210IfTxRingEntry.setStatus("current")


class _Dfl210IfTxRingIndex_Type(Integer32):
    """Custom type dfl210IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl210IfTxRingIndex_Object = MibTableColumn
dfl210IfTxRingIndex = _Dfl210IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9, 1, 1),
    _Dfl210IfTxRingIndex_Type()
)
dfl210IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210IfTxRingIndex.setStatus("current")
_Dfl210IfTxDespools_Type = Gauge32
_Dfl210IfTxDespools_Object = MibTableColumn
dfl210IfTxDespools = _Dfl210IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9, 1, 2),
    _Dfl210IfTxDespools_Type()
)
dfl210IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfTxDespools.setStatus("current")
_Dfl210IfTxAvgUse_Type = Gauge32
_Dfl210IfTxAvgUse_Object = MibTableColumn
dfl210IfTxAvgUse = _Dfl210IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9, 1, 3),
    _Dfl210IfTxAvgUse_Type()
)
dfl210IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfTxAvgUse.setStatus("current")
_Dfl210IfTxRingSaturation_Type = Gauge32
_Dfl210IfTxRingSaturation_Object = MibTableColumn
dfl210IfTxRingSaturation = _Dfl210IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9, 1, 4),
    _Dfl210IfTxRingSaturation_Type()
)
dfl210IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfTxRingSaturation.setStatus("current")
_Dfl210RxTingFlooded_Type = Gauge32
_Dfl210RxTingFlooded_Object = MibTableColumn
dfl210RxTingFlooded = _Dfl210RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 9, 1, 5),
    _Dfl210RxTingFlooded_Type()
)
dfl210RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210RxTingFlooded.setStatus("current")
_Dfl210IfVlanStatsTable_Object = MibTable
dfl210IfVlanStatsTable = _Dfl210IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl210IfVlanStatsTable.setStatus("current")
_Dfl210IfVlanStatsEntry_Object = MibTableRow
dfl210IfVlanStatsEntry = _Dfl210IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1)
)
dfl210IfVlanStatsEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl210IfVlanStatsEntry.setStatus("current")


class _Dfl210IfVlanIndex_Type(Integer32):
    """Custom type dfl210IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210IfVlanIndex_Type.__name__ = "Integer32"
_Dfl210IfVlanIndex_Object = MibTableColumn
dfl210IfVlanIndex = _Dfl210IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 1),
    _Dfl210IfVlanIndex_Type()
)
dfl210IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210IfVlanIndex.setStatus("current")
_Dfl210IfVlanUntaggedInPkts_Type = Counter32
_Dfl210IfVlanUntaggedInPkts_Object = MibTableColumn
dfl210IfVlanUntaggedInPkts = _Dfl210IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 2),
    _Dfl210IfVlanUntaggedInPkts_Type()
)
dfl210IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfVlanUntaggedInPkts.setStatus("current")
_Dfl210IfVlanUntaggedOutPkts_Type = Counter32
_Dfl210IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl210IfVlanUntaggedOutPkts = _Dfl210IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 3),
    _Dfl210IfVlanUntaggedOutPkts_Type()
)
dfl210IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfVlanUntaggedOutPkts.setStatus("current")
_Dfl210IfVlanUntaggedTotPkts_Type = Counter32
_Dfl210IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl210IfVlanUntaggedTotPkts = _Dfl210IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 4),
    _Dfl210IfVlanUntaggedTotPkts_Type()
)
dfl210IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfVlanUntaggedTotPkts.setStatus("current")
_Dfl210IfVlanUntaggedInOctets_Type = Counter32
_Dfl210IfVlanUntaggedInOctets_Object = MibTableColumn
dfl210IfVlanUntaggedInOctets = _Dfl210IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 5),
    _Dfl210IfVlanUntaggedInOctets_Type()
)
dfl210IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfVlanUntaggedInOctets.setStatus("current")
_Dfl210IfVlanUntaggedOutOctets_Type = Counter32
_Dfl210IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl210IfVlanUntaggedOutOctets = _Dfl210IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 6),
    _Dfl210IfVlanUntaggedOutOctets_Type()
)
dfl210IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfVlanUntaggedOutOctets.setStatus("current")
_Dfl210IfVlanUntaggedTotOctets_Type = Counter32
_Dfl210IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl210IfVlanUntaggedTotOctets = _Dfl210IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 10, 1, 7),
    _Dfl210IfVlanUntaggedTotOctets_Type()
)
dfl210IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IfVlanUntaggedTotOctets.setStatus("current")
_Dfl210HWSensorTable_Object = MibTable
dfl210HWSensorTable = _Dfl210HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl210HWSensorTable.setStatus("current")
_Dfl210HWSensorEntry_Object = MibTableRow
dfl210HWSensorEntry = _Dfl210HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 11, 1)
)
dfl210HWSensorEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl210HWSensorEntry.setStatus("current")


class _Dfl210HWSensorIndex_Type(Integer32):
    """Custom type dfl210HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210HWSensorIndex_Type.__name__ = "Integer32"
_Dfl210HWSensorIndex_Object = MibTableColumn
dfl210HWSensorIndex = _Dfl210HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 11, 1, 1),
    _Dfl210HWSensorIndex_Type()
)
dfl210HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210HWSensorIndex.setStatus("current")
_Dfl210HWSensorName_Type = DisplayString
_Dfl210HWSensorName_Object = MibTableColumn
dfl210HWSensorName = _Dfl210HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 11, 1, 2),
    _Dfl210HWSensorName_Type()
)
dfl210HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HWSensorName.setStatus("current")
_Dfl210HWSensorValue_Type = Gauge32
_Dfl210HWSensorValue_Object = MibTableColumn
dfl210HWSensorValue = _Dfl210HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 11, 1, 3),
    _Dfl210HWSensorValue_Type()
)
dfl210HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HWSensorValue.setStatus("current")
_Dfl210HWSensorUnit_Type = DisplayString
_Dfl210HWSensorUnit_Object = MibTableColumn
dfl210HWSensorUnit = _Dfl210HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 11, 1, 4),
    _Dfl210HWSensorUnit_Type()
)
dfl210HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HWSensorUnit.setStatus("current")
_Dfl210SysMemUsage_Type = Gauge32
_Dfl210SysMemUsage_Object = MibScalar
dfl210SysMemUsage = _Dfl210SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 12),
    _Dfl210SysMemUsage_Type()
)
dfl210SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysMemUsage.setStatus("current")
_Dfl210SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl210SysTCPUsage = _Dfl210SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 13)
)
_Dfl210SysTCPRecvSmall_Type = Gauge32
_Dfl210SysTCPRecvSmall_Object = MibScalar
dfl210SysTCPRecvSmall = _Dfl210SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 13, 1),
    _Dfl210SysTCPRecvSmall_Type()
)
dfl210SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysTCPRecvSmall.setStatus("current")
_Dfl210SysTCPRecvLarge_Type = Gauge32
_Dfl210SysTCPRecvLarge_Object = MibScalar
dfl210SysTCPRecvLarge = _Dfl210SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 13, 2),
    _Dfl210SysTCPRecvLarge_Type()
)
dfl210SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysTCPRecvLarge.setStatus("current")
_Dfl210SysTCPSendSmall_Type = Gauge32
_Dfl210SysTCPSendSmall_Object = MibScalar
dfl210SysTCPSendSmall = _Dfl210SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 13, 3),
    _Dfl210SysTCPSendSmall_Type()
)
dfl210SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysTCPSendSmall.setStatus("current")
_Dfl210SysTCPSendLarge_Type = Gauge32
_Dfl210SysTCPSendLarge_Object = MibScalar
dfl210SysTCPSendLarge = _Dfl210SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 13, 4),
    _Dfl210SysTCPSendLarge_Type()
)
dfl210SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysTCPSendLarge.setStatus("current")
_Dfl210SysTimerUsage_Type = Gauge32
_Dfl210SysTimerUsage_Object = MibScalar
dfl210SysTimerUsage = _Dfl210SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 14),
    _Dfl210SysTimerUsage_Type()
)
dfl210SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysTimerUsage.setStatus("current")
_Dfl210SysConnOPS_Type = Gauge32
_Dfl210SysConnOPS_Object = MibScalar
dfl210SysConnOPS = _Dfl210SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 15),
    _Dfl210SysConnOPS_Type()
)
dfl210SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysConnOPS.setStatus("current")
_Dfl210SysConnCPS_Type = Gauge32
_Dfl210SysConnCPS_Object = MibScalar
dfl210SysConnCPS = _Dfl210SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 16),
    _Dfl210SysConnCPS_Type()
)
dfl210SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysConnCPS.setStatus("current")
_Dfl210SysHCForwardedBits_Type = Counter64
_Dfl210SysHCForwardedBits_Object = MibScalar
dfl210SysHCForwardedBits = _Dfl210SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 1, 17),
    _Dfl210SysHCForwardedBits_Type()
)
dfl210SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SysHCForwardedBits.setStatus("current")
_Dfl210VPN_ObjectIdentity = ObjectIdentity
dfl210VPN = _Dfl210VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2)
)
_Dfl210IPsec_ObjectIdentity = ObjectIdentity
dfl210IPsec = _Dfl210IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1)
)
_Dfl210IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl210IPsecGlobal = _Dfl210IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1)
)
_Dfl210IPsecPhaseOneActive_Type = Gauge32
_Dfl210IPsecPhaseOneActive_Object = MibScalar
dfl210IPsecPhaseOneActive = _Dfl210IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 1),
    _Dfl210IPsecPhaseOneActive_Type()
)
dfl210IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecPhaseOneActive.setStatus("current")
_Dfl210IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl210IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl210IPsecPhaseOneAggrModeDone = _Dfl210IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 2),
    _Dfl210IPsecPhaseOneAggrModeDone_Type()
)
dfl210IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl210IPsecQuickModeActive_Type = Gauge32
_Dfl210IPsecQuickModeActive_Object = MibScalar
dfl210IPsecQuickModeActive = _Dfl210IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 3),
    _Dfl210IPsecQuickModeActive_Type()
)
dfl210IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecQuickModeActive.setStatus("current")
_Dfl210IPsecPhaseOneDone_Type = Counter32
_Dfl210IPsecPhaseOneDone_Object = MibScalar
dfl210IPsecPhaseOneDone = _Dfl210IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 4),
    _Dfl210IPsecPhaseOneDone_Type()
)
dfl210IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecPhaseOneDone.setStatus("current")
_Dfl210IPsecPhaseOneFailed_Type = Counter32
_Dfl210IPsecPhaseOneFailed_Object = MibScalar
dfl210IPsecPhaseOneFailed = _Dfl210IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 5),
    _Dfl210IPsecPhaseOneFailed_Type()
)
dfl210IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecPhaseOneFailed.setStatus("current")
_Dfl210IPsecPhaseOneRekeyed_Type = Counter32
_Dfl210IPsecPhaseOneRekeyed_Object = MibScalar
dfl210IPsecPhaseOneRekeyed = _Dfl210IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 6),
    _Dfl210IPsecPhaseOneRekeyed_Type()
)
dfl210IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecPhaseOneRekeyed.setStatus("current")
_Dfl210IPsecQuickModeDone_Type = Counter32
_Dfl210IPsecQuickModeDone_Object = MibScalar
dfl210IPsecQuickModeDone = _Dfl210IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 7),
    _Dfl210IPsecQuickModeDone_Type()
)
dfl210IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecQuickModeDone.setStatus("current")
_Dfl210IPsecQuickModeFailed_Type = Counter32
_Dfl210IPsecQuickModeFailed_Object = MibScalar
dfl210IPsecQuickModeFailed = _Dfl210IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 8),
    _Dfl210IPsecQuickModeFailed_Type()
)
dfl210IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecQuickModeFailed.setStatus("current")
_Dfl210IPsecInfoDone_Type = Counter32
_Dfl210IPsecInfoDone_Object = MibScalar
dfl210IPsecInfoDone = _Dfl210IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 9),
    _Dfl210IPsecInfoDone_Type()
)
dfl210IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecInfoDone.setStatus("current")
_Dfl210IPsecInfoFailed_Type = Counter32
_Dfl210IPsecInfoFailed_Object = MibScalar
dfl210IPsecInfoFailed = _Dfl210IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 10),
    _Dfl210IPsecInfoFailed_Type()
)
dfl210IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecInfoFailed.setStatus("current")
_Dfl210IPsecInOctetsComp_Type = Counter64
_Dfl210IPsecInOctetsComp_Object = MibScalar
dfl210IPsecInOctetsComp = _Dfl210IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 11),
    _Dfl210IPsecInOctetsComp_Type()
)
dfl210IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecInOctetsComp.setStatus("current")
_Dfl210IPsecInOctetsUncomp_Type = Counter64
_Dfl210IPsecInOctetsUncomp_Object = MibScalar
dfl210IPsecInOctetsUncomp = _Dfl210IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 12),
    _Dfl210IPsecInOctetsUncomp_Type()
)
dfl210IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecInOctetsUncomp.setStatus("current")
_Dfl210IPsecOutOctetsComp_Type = Counter64
_Dfl210IPsecOutOctetsComp_Object = MibScalar
dfl210IPsecOutOctetsComp = _Dfl210IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 13),
    _Dfl210IPsecOutOctetsComp_Type()
)
dfl210IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecOutOctetsComp.setStatus("current")
_Dfl210IPsecOutOctetsUncomp_Type = Counter64
_Dfl210IPsecOutOctetsUncomp_Object = MibScalar
dfl210IPsecOutOctetsUncomp = _Dfl210IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 14),
    _Dfl210IPsecOutOctetsUncomp_Type()
)
dfl210IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecOutOctetsUncomp.setStatus("current")
_Dfl210IPsecForwardedOctetsComp_Type = Counter64
_Dfl210IPsecForwardedOctetsComp_Object = MibScalar
dfl210IPsecForwardedOctetsComp = _Dfl210IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 15),
    _Dfl210IPsecForwardedOctetsComp_Type()
)
dfl210IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecForwardedOctetsComp.setStatus("current")
_Dfl210IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl210IPsecForwardedOctetsUcomp_Object = MibScalar
dfl210IPsecForwardedOctetsUcomp = _Dfl210IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 16),
    _Dfl210IPsecForwardedOctetsUcomp_Type()
)
dfl210IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl210IPsecInPackets_Type = Counter64
_Dfl210IPsecInPackets_Object = MibScalar
dfl210IPsecInPackets = _Dfl210IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 17),
    _Dfl210IPsecInPackets_Type()
)
dfl210IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecInPackets.setStatus("current")
_Dfl210IPsecOutPackets_Type = Counter64
_Dfl210IPsecOutPackets_Object = MibScalar
dfl210IPsecOutPackets = _Dfl210IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 18),
    _Dfl210IPsecOutPackets_Type()
)
dfl210IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecOutPackets.setStatus("current")
_Dfl210IPsecForwardedPackets_Type = Counter64
_Dfl210IPsecForwardedPackets_Object = MibScalar
dfl210IPsecForwardedPackets = _Dfl210IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 19),
    _Dfl210IPsecForwardedPackets_Type()
)
dfl210IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecForwardedPackets.setStatus("current")
_Dfl210IPsecActiveTransforms_Type = Gauge32
_Dfl210IPsecActiveTransforms_Object = MibScalar
dfl210IPsecActiveTransforms = _Dfl210IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 20),
    _Dfl210IPsecActiveTransforms_Type()
)
dfl210IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecActiveTransforms.setStatus("current")
_Dfl210IPsecTotalTransforms_Type = Counter32
_Dfl210IPsecTotalTransforms_Object = MibScalar
dfl210IPsecTotalTransforms = _Dfl210IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 21),
    _Dfl210IPsecTotalTransforms_Type()
)
dfl210IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecTotalTransforms.setStatus("current")
_Dfl210IPsecOutOfTransforms_Type = Counter32
_Dfl210IPsecOutOfTransforms_Object = MibScalar
dfl210IPsecOutOfTransforms = _Dfl210IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 22),
    _Dfl210IPsecOutOfTransforms_Type()
)
dfl210IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecOutOfTransforms.setStatus("current")
_Dfl210IPsecTotalRekeys_Type = Counter32
_Dfl210IPsecTotalRekeys_Object = MibScalar
dfl210IPsecTotalRekeys = _Dfl210IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 2, 1, 1, 23),
    _Dfl210IPsecTotalRekeys_Type()
)
dfl210IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPsecTotalRekeys.setStatus("current")
_Dfl210Rules_ObjectIdentity = ObjectIdentity
dfl210Rules = _Dfl210Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 3)
)
_Dfl210RuleUseTable_Object = MibTable
dfl210RuleUseTable = _Dfl210RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl210RuleUseTable.setStatus("current")
_Dfl210RuleUseEntry_Object = MibTableRow
dfl210RuleUseEntry = _Dfl210RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 3, 2, 1)
)
dfl210RuleUseEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl210RuleUseEntry.setStatus("current")


class _Dfl210RuleIndex_Type(Integer32):
    """Custom type dfl210RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210RuleIndex_Type.__name__ = "Integer32"
_Dfl210RuleIndex_Object = MibTableColumn
dfl210RuleIndex = _Dfl210RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 3, 2, 1, 1),
    _Dfl210RuleIndex_Type()
)
dfl210RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210RuleIndex.setStatus("current")
_Dfl210RuleName_Type = DisplayString
_Dfl210RuleName_Object = MibTableColumn
dfl210RuleName = _Dfl210RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 3, 2, 1, 2),
    _Dfl210RuleName_Type()
)
dfl210RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210RuleName.setStatus("current")
_Dfl210RuleUse_Type = Counter32
_Dfl210RuleUse_Object = MibTableColumn
dfl210RuleUse = _Dfl210RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 3, 2, 1, 3),
    _Dfl210RuleUse_Type()
)
dfl210RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210RuleUse.setStatus("current")
_Dfl210IPPools_ObjectIdentity = ObjectIdentity
dfl210IPPools = _Dfl210IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4)
)
_Dfl210IPPoolsNumber_Type = Integer32
_Dfl210IPPoolsNumber_Object = MibScalar
dfl210IPPoolsNumber = _Dfl210IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 1),
    _Dfl210IPPoolsNumber_Type()
)
dfl210IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolsNumber.setStatus("current")
_Dfl210IPPoolTable_Object = MibTable
dfl210IPPoolTable = _Dfl210IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl210IPPoolTable.setStatus("current")
_Dfl210IPPoolEntry_Object = MibTableRow
dfl210IPPoolEntry = _Dfl210IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1)
)
dfl210IPPoolEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl210IPPoolEntry.setStatus("current")


class _Dfl210IPPoolIndex_Type(Integer32):
    """Custom type dfl210IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210IPPoolIndex_Type.__name__ = "Integer32"
_Dfl210IPPoolIndex_Object = MibTableColumn
dfl210IPPoolIndex = _Dfl210IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 1),
    _Dfl210IPPoolIndex_Type()
)
dfl210IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210IPPoolIndex.setStatus("current")
_Dfl210IPPoolName_Type = DisplayString
_Dfl210IPPoolName_Object = MibTableColumn
dfl210IPPoolName = _Dfl210IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 2),
    _Dfl210IPPoolName_Type()
)
dfl210IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolName.setStatus("current")
_Dfl210IPPoolPrepare_Type = Gauge32
_Dfl210IPPoolPrepare_Object = MibTableColumn
dfl210IPPoolPrepare = _Dfl210IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 3),
    _Dfl210IPPoolPrepare_Type()
)
dfl210IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolPrepare.setStatus("current")
_Dfl210IPPoolFree_Type = Gauge32
_Dfl210IPPoolFree_Object = MibTableColumn
dfl210IPPoolFree = _Dfl210IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 4),
    _Dfl210IPPoolFree_Type()
)
dfl210IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolFree.setStatus("current")
_Dfl210IPPoolMisses_Type = Gauge32
_Dfl210IPPoolMisses_Object = MibTableColumn
dfl210IPPoolMisses = _Dfl210IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 5),
    _Dfl210IPPoolMisses_Type()
)
dfl210IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolMisses.setStatus("current")
_Dfl210IPPoolClientFails_Type = Gauge32
_Dfl210IPPoolClientFails_Object = MibTableColumn
dfl210IPPoolClientFails = _Dfl210IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 6),
    _Dfl210IPPoolClientFails_Type()
)
dfl210IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolClientFails.setStatus("current")
_Dfl210IPPoolUsed_Type = Gauge32
_Dfl210IPPoolUsed_Object = MibTableColumn
dfl210IPPoolUsed = _Dfl210IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 4, 2, 1, 7),
    _Dfl210IPPoolUsed_Type()
)
dfl210IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210IPPoolUsed.setStatus("current")
_Dfl210DHCPServer_ObjectIdentity = ObjectIdentity
dfl210DHCPServer = _Dfl210DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5)
)
_Dfl210DHCPTotalRejected_Type = Gauge32
_Dfl210DHCPTotalRejected_Object = MibScalar
dfl210DHCPTotalRejected = _Dfl210DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 1),
    _Dfl210DHCPTotalRejected_Type()
)
dfl210DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPTotalRejected.setStatus("current")
_Dfl210DHCPRuleTable_Object = MibTable
dfl210DHCPRuleTable = _Dfl210DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl210DHCPRuleTable.setStatus("current")
_Dfl210DHCPRuleEntry_Object = MibTableRow
dfl210DHCPRuleEntry = _Dfl210DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1)
)
dfl210DHCPRuleEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl210DHCPRuleEntry.setStatus("current")


class _Dfl210DHCPRuleIndex_Type(Integer32):
    """Custom type dfl210DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl210DHCPRuleIndex_Object = MibTableColumn
dfl210DHCPRuleIndex = _Dfl210DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 1),
    _Dfl210DHCPRuleIndex_Type()
)
dfl210DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210DHCPRuleIndex.setStatus("current")
_Dfl210DHCPRuleName_Type = DisplayString
_Dfl210DHCPRuleName_Object = MibTableColumn
dfl210DHCPRuleName = _Dfl210DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 2),
    _Dfl210DHCPRuleName_Type()
)
dfl210DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRuleName.setStatus("current")
_Dfl210DHCPRuleUsage_Type = Gauge32
_Dfl210DHCPRuleUsage_Object = MibTableColumn
dfl210DHCPRuleUsage = _Dfl210DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 3),
    _Dfl210DHCPRuleUsage_Type()
)
dfl210DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRuleUsage.setStatus("current")
_Dfl210DHCPRuleUsagePercent_Type = Gauge32
_Dfl210DHCPRuleUsagePercent_Object = MibTableColumn
dfl210DHCPRuleUsagePercent = _Dfl210DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 4),
    _Dfl210DHCPRuleUsagePercent_Type()
)
dfl210DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRuleUsagePercent.setStatus("current")
_Dfl210DHCPActiveClients_Type = Gauge32
_Dfl210DHCPActiveClients_Object = MibTableColumn
dfl210DHCPActiveClients = _Dfl210DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 5),
    _Dfl210DHCPActiveClients_Type()
)
dfl210DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPActiveClients.setStatus("current")
_Dfl210DHCPActiveClientsPercent_Type = Gauge32
_Dfl210DHCPActiveClientsPercent_Object = MibTableColumn
dfl210DHCPActiveClientsPercent = _Dfl210DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 6),
    _Dfl210DHCPActiveClientsPercent_Type()
)
dfl210DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPActiveClientsPercent.setStatus("current")
_Dfl210DHCPRejectedRequests_Type = Gauge32
_Dfl210DHCPRejectedRequests_Object = MibTableColumn
dfl210DHCPRejectedRequests = _Dfl210DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 7),
    _Dfl210DHCPRejectedRequests_Type()
)
dfl210DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRejectedRequests.setStatus("current")
_Dfl210DHCPTotalLeases_Type = Gauge32
_Dfl210DHCPTotalLeases_Object = MibTableColumn
dfl210DHCPTotalLeases = _Dfl210DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 5, 2, 1, 8),
    _Dfl210DHCPTotalLeases_Type()
)
dfl210DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPTotalLeases.setStatus("current")
_Dfl210UserAuth_ObjectIdentity = ObjectIdentity
dfl210UserAuth = _Dfl210UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6)
)
_Dfl210UserAuthHTTPUsers_Type = Gauge32
_Dfl210UserAuthHTTPUsers_Object = MibScalar
dfl210UserAuthHTTPUsers = _Dfl210UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 1),
    _Dfl210UserAuthHTTPUsers_Type()
)
dfl210UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthHTTPUsers.setStatus("current")
_Dfl210UserAuthXAUTHUsers_Type = Gauge32
_Dfl210UserAuthXAUTHUsers_Object = MibScalar
dfl210UserAuthXAUTHUsers = _Dfl210UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 2),
    _Dfl210UserAuthXAUTHUsers_Type()
)
dfl210UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthXAUTHUsers.setStatus("current")
_Dfl210UserAuthHTTPSUsers_Type = Gauge32
_Dfl210UserAuthHTTPSUsers_Object = MibScalar
dfl210UserAuthHTTPSUsers = _Dfl210UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 3),
    _Dfl210UserAuthHTTPSUsers_Type()
)
dfl210UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthHTTPSUsers.setStatus("current")
_Dfl210UserAuthPPPUsers_Type = Gauge32
_Dfl210UserAuthPPPUsers_Object = MibScalar
dfl210UserAuthPPPUsers = _Dfl210UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 4),
    _Dfl210UserAuthPPPUsers_Type()
)
dfl210UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthPPPUsers.setStatus("current")
_Dfl210UserAuthEAPUsers_Type = Gauge32
_Dfl210UserAuthEAPUsers_Object = MibScalar
dfl210UserAuthEAPUsers = _Dfl210UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 5),
    _Dfl210UserAuthEAPUsers_Type()
)
dfl210UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthEAPUsers.setStatus("current")
_Dfl210UserAuthRuleUseTable_Object = MibTable
dfl210UserAuthRuleUseTable = _Dfl210UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl210UserAuthRuleUseTable.setStatus("current")
_Dfl210UserAuthRuleUseEntry_Object = MibTableRow
dfl210UserAuthRuleUseEntry = _Dfl210UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 6, 1)
)
dfl210UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl210UserAuthRuleUseEntry.setStatus("current")


class _Dfl210UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl210UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl210UserAuthRuleIndex_Object = MibTableColumn
dfl210UserAuthRuleIndex = _Dfl210UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 6, 1, 1),
    _Dfl210UserAuthRuleIndex_Type()
)
dfl210UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210UserAuthRuleIndex.setStatus("current")
_Dfl210UserAuthRuleName_Type = DisplayString
_Dfl210UserAuthRuleName_Object = MibTableColumn
dfl210UserAuthRuleName = _Dfl210UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 6, 1, 2),
    _Dfl210UserAuthRuleName_Type()
)
dfl210UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthRuleName.setStatus("current")
_Dfl210UserAuthRuleUse_Type = Counter32
_Dfl210UserAuthRuleUse_Object = MibTableColumn
dfl210UserAuthRuleUse = _Dfl210UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 6, 6, 1, 3),
    _Dfl210UserAuthRuleUse_Type()
)
dfl210UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210UserAuthRuleUse.setStatus("current")
_Dfl210LinkMonitor_ObjectIdentity = ObjectIdentity
dfl210LinkMonitor = _Dfl210LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7)
)
_Dfl210LinkMonGrp_Type = Integer32
_Dfl210LinkMonGrp_Object = MibScalar
dfl210LinkMonGrp = _Dfl210LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 1),
    _Dfl210LinkMonGrp_Type()
)
dfl210LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210LinkMonGrp.setStatus("current")
_Dfl210LinkMonGrpTable_Object = MibTable
dfl210LinkMonGrpTable = _Dfl210LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl210LinkMonGrpTable.setStatus("current")
_Dfl210LinkMonGrpEntry_Object = MibTableRow
dfl210LinkMonGrpEntry = _Dfl210LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 2, 1)
)
dfl210LinkMonGrpEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl210LinkMonGrpEntry.setStatus("current")


class _Dfl210LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl210LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl210LinkMonGrpIndex_Object = MibTableColumn
dfl210LinkMonGrpIndex = _Dfl210LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 2, 1, 1),
    _Dfl210LinkMonGrpIndex_Type()
)
dfl210LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210LinkMonGrpIndex.setStatus("current")
_Dfl210LinkMonGrpName_Type = DisplayString
_Dfl210LinkMonGrpName_Object = MibTableColumn
dfl210LinkMonGrpName = _Dfl210LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 2, 1, 2),
    _Dfl210LinkMonGrpName_Type()
)
dfl210LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210LinkMonGrpName.setStatus("current")
_Dfl210LinkMonGrpHostsUp_Type = Gauge32
_Dfl210LinkMonGrpHostsUp_Object = MibTableColumn
dfl210LinkMonGrpHostsUp = _Dfl210LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 2, 1, 3),
    _Dfl210LinkMonGrpHostsUp_Type()
)
dfl210LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210LinkMonGrpHostsUp.setStatus("current")
_Dfl210LinkMonHostTable_Object = MibTable
dfl210LinkMonHostTable = _Dfl210LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl210LinkMonHostTable.setStatus("current")
_Dfl210LinkMonHostEntry_Object = MibTableRow
dfl210LinkMonHostEntry = _Dfl210LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 3, 1)
)
dfl210LinkMonHostEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210LinkMonGrpIndex"),
    (0, "DFL210-MIB", "dfl210LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl210LinkMonHostEntry.setStatus("current")


class _Dfl210LinkMonHostIndex_Type(Integer32):
    """Custom type dfl210LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl210LinkMonHostIndex_Object = MibTableColumn
dfl210LinkMonHostIndex = _Dfl210LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 3, 1, 1),
    _Dfl210LinkMonHostIndex_Type()
)
dfl210LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210LinkMonHostIndex.setStatus("current")
_Dfl210LinkMonHostId_Type = DisplayString
_Dfl210LinkMonHostId_Object = MibTableColumn
dfl210LinkMonHostId = _Dfl210LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 3, 1, 2),
    _Dfl210LinkMonHostId_Type()
)
dfl210LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210LinkMonHostId.setStatus("current")
_Dfl210LinkMonHostShortTermLoss_Type = Gauge32
_Dfl210LinkMonHostShortTermLoss_Object = MibTableColumn
dfl210LinkMonHostShortTermLoss = _Dfl210LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 3, 1, 3),
    _Dfl210LinkMonHostShortTermLoss_Type()
)
dfl210LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210LinkMonHostShortTermLoss.setStatus("current")
_Dfl210LinkMonHostPacketsLost_Type = Counter32
_Dfl210LinkMonHostPacketsLost_Object = MibTableColumn
dfl210LinkMonHostPacketsLost = _Dfl210LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 7, 3, 1, 4),
    _Dfl210LinkMonHostPacketsLost_Type()
)
dfl210LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210LinkMonHostPacketsLost.setStatus("current")
_Dfl210Pipes_ObjectIdentity = ObjectIdentity
dfl210Pipes = _Dfl210Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8)
)
_Dfl210PipeUsers_Type = Gauge32
_Dfl210PipeUsers_Object = MibScalar
dfl210PipeUsers = _Dfl210PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 1),
    _Dfl210PipeUsers_Type()
)
dfl210PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeUsers.setStatus("current")
_Dfl210PipeTable_Object = MibTable
dfl210PipeTable = _Dfl210PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl210PipeTable.setStatus("current")
_Dfl210PipeEntry_Object = MibTableRow
dfl210PipeEntry = _Dfl210PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1)
)
dfl210PipeEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl210PipeEntry.setStatus("current")


class _Dfl210PipeIndex_Type(Integer32):
    """Custom type dfl210PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210PipeIndex_Type.__name__ = "Integer32"
_Dfl210PipeIndex_Object = MibTableColumn
dfl210PipeIndex = _Dfl210PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 1),
    _Dfl210PipeIndex_Type()
)
dfl210PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210PipeIndex.setStatus("current")
_Dfl210PipeName_Type = DisplayString
_Dfl210PipeName_Object = MibTableColumn
dfl210PipeName = _Dfl210PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 2),
    _Dfl210PipeName_Type()
)
dfl210PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeName.setStatus("current")
_Dfl210PipeMinPrec_Type = Integer32
_Dfl210PipeMinPrec_Object = MibTableColumn
dfl210PipeMinPrec = _Dfl210PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 3),
    _Dfl210PipeMinPrec_Type()
)
dfl210PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeMinPrec.setStatus("current")
_Dfl210PipeMaxPrec_Type = Integer32
_Dfl210PipeMaxPrec_Object = MibTableColumn
dfl210PipeMaxPrec = _Dfl210PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 4),
    _Dfl210PipeMaxPrec_Type()
)
dfl210PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeMaxPrec.setStatus("current")
_Dfl210PipeDefPrec_Type = Integer32
_Dfl210PipeDefPrec_Object = MibTableColumn
dfl210PipeDefPrec = _Dfl210PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 5),
    _Dfl210PipeDefPrec_Type()
)
dfl210PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeDefPrec.setStatus("current")
_Dfl210PipeNumPrec_Type = Integer32
_Dfl210PipeNumPrec_Object = MibTableColumn
dfl210PipeNumPrec = _Dfl210PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 6),
    _Dfl210PipeNumPrec_Type()
)
dfl210PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeNumPrec.setStatus("current")
_Dfl210PipeNumUsers_Type = Gauge32
_Dfl210PipeNumUsers_Object = MibTableColumn
dfl210PipeNumUsers = _Dfl210PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 7),
    _Dfl210PipeNumUsers_Type()
)
dfl210PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeNumUsers.setStatus("current")
_Dfl210PipeCurrentBps_Type = Gauge32
_Dfl210PipeCurrentBps_Object = MibTableColumn
dfl210PipeCurrentBps = _Dfl210PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 8),
    _Dfl210PipeCurrentBps_Type()
)
dfl210PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeCurrentBps.setStatus("current")
_Dfl210PipeCurrentPps_Type = Gauge32
_Dfl210PipeCurrentPps_Object = MibTableColumn
dfl210PipeCurrentPps = _Dfl210PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 9),
    _Dfl210PipeCurrentPps_Type()
)
dfl210PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeCurrentPps.setStatus("current")
_Dfl210PipeDelayedPackets_Type = Counter32
_Dfl210PipeDelayedPackets_Object = MibTableColumn
dfl210PipeDelayedPackets = _Dfl210PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 10),
    _Dfl210PipeDelayedPackets_Type()
)
dfl210PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeDelayedPackets.setStatus("current")
_Dfl210PipeDropedPackets_Type = Counter32
_Dfl210PipeDropedPackets_Object = MibTableColumn
dfl210PipeDropedPackets = _Dfl210PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 2, 1, 11),
    _Dfl210PipeDropedPackets_Type()
)
dfl210PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipeDropedPackets.setStatus("current")
_Dfl210PipePrecTable_Object = MibTable
dfl210PipePrecTable = _Dfl210PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl210PipePrecTable.setStatus("current")
_Dfl210PipePrecEntry_Object = MibTableRow
dfl210PipePrecEntry = _Dfl210PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1)
)
dfl210PipePrecEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210PipeIndex"),
    (0, "DFL210-MIB", "dfl210PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl210PipePrecEntry.setStatus("current")


class _Dfl210PipePrecIndex_Type(Integer32):
    """Custom type dfl210PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210PipePrecIndex_Type.__name__ = "Integer32"
_Dfl210PipePrecIndex_Object = MibTableColumn
dfl210PipePrecIndex = _Dfl210PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 1),
    _Dfl210PipePrecIndex_Type()
)
dfl210PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210PipePrecIndex.setStatus("current")
_Dfl210PipePrec_Type = Integer32
_Dfl210PipePrec_Object = MibTableColumn
dfl210PipePrec = _Dfl210PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 2),
    _Dfl210PipePrec_Type()
)
dfl210PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrec.setStatus("current")
_Dfl210PipePrecBps_Type = Gauge32
_Dfl210PipePrecBps_Object = MibTableColumn
dfl210PipePrecBps = _Dfl210PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 3),
    _Dfl210PipePrecBps_Type()
)
dfl210PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecBps.setStatus("current")
_Dfl210PipePrecTotalPps_Type = Gauge32
_Dfl210PipePrecTotalPps_Object = MibTableColumn
dfl210PipePrecTotalPps = _Dfl210PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 4),
    _Dfl210PipePrecTotalPps_Type()
)
dfl210PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecTotalPps.setStatus("current")
_Dfl210PipePrecReservedBps_Type = Gauge32
_Dfl210PipePrecReservedBps_Object = MibTableColumn
dfl210PipePrecReservedBps = _Dfl210PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 5),
    _Dfl210PipePrecReservedBps_Type()
)
dfl210PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecReservedBps.setStatus("current")
_Dfl210PipePrecDynLimBps_Type = Gauge32
_Dfl210PipePrecDynLimBps_Object = MibTableColumn
dfl210PipePrecDynLimBps = _Dfl210PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 6),
    _Dfl210PipePrecDynLimBps_Type()
)
dfl210PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecDynLimBps.setStatus("current")
_Dfl210PipePrecDynUsrLimBps_Type = Gauge32
_Dfl210PipePrecDynUsrLimBps_Object = MibTableColumn
dfl210PipePrecDynUsrLimBps = _Dfl210PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 7),
    _Dfl210PipePrecDynUsrLimBps_Type()
)
dfl210PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecDynUsrLimBps.setStatus("current")
_Dfl210PipePrecDelayedPackets_Type = Counter32
_Dfl210PipePrecDelayedPackets_Object = MibTableColumn
dfl210PipePrecDelayedPackets = _Dfl210PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 8),
    _Dfl210PipePrecDelayedPackets_Type()
)
dfl210PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecDelayedPackets.setStatus("current")
_Dfl210PipePrecDropedPackets_Type = Counter32
_Dfl210PipePrecDropedPackets_Object = MibTableColumn
dfl210PipePrecDropedPackets = _Dfl210PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 8, 3, 1, 9),
    _Dfl210PipePrecDropedPackets_Type()
)
dfl210PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210PipePrecDropedPackets.setStatus("current")
_Dfl210ALG_ObjectIdentity = ObjectIdentity
dfl210ALG = _Dfl210ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9)
)
_Dfl210AlgSessions_Type = Gauge32
_Dfl210AlgSessions_Object = MibScalar
dfl210AlgSessions = _Dfl210AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 1),
    _Dfl210AlgSessions_Type()
)
dfl210AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210AlgSessions.setStatus("current")
_Dfl210AlgConnections_Type = Gauge32
_Dfl210AlgConnections_Object = MibScalar
dfl210AlgConnections = _Dfl210AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 2),
    _Dfl210AlgConnections_Type()
)
dfl210AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210AlgConnections.setStatus("current")
_Dfl210AlgTCPStreams_Type = Gauge32
_Dfl210AlgTCPStreams_Object = MibScalar
dfl210AlgTCPStreams = _Dfl210AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 3),
    _Dfl210AlgTCPStreams_Type()
)
dfl210AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210AlgTCPStreams.setStatus("current")
_Dfl210HttpAlg_ObjectIdentity = ObjectIdentity
dfl210HttpAlg = _Dfl210HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4)
)
_Dfl210HttpAlgTable_Object = MibTable
dfl210HttpAlgTable = _Dfl210HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl210HttpAlgTable.setStatus("current")
_Dfl210HttpAlgEntry_Object = MibTableRow
dfl210HttpAlgEntry = _Dfl210HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1, 1)
)
dfl210HttpAlgEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl210HttpAlgEntry.setStatus("current")


class _Dfl210HttpAlgIndex_Type(Integer32):
    """Custom type dfl210HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl210HttpAlgIndex_Object = MibTableColumn
dfl210HttpAlgIndex = _Dfl210HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1, 1, 1),
    _Dfl210HttpAlgIndex_Type()
)
dfl210HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210HttpAlgIndex.setStatus("current")
_Dfl210HttpAlgName_Type = DisplayString
_Dfl210HttpAlgName_Object = MibTableColumn
dfl210HttpAlgName = _Dfl210HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1, 1, 2),
    _Dfl210HttpAlgName_Type()
)
dfl210HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgName.setStatus("current")
_Dfl210HttpAlgTotalRequested_Type = Gauge32
_Dfl210HttpAlgTotalRequested_Object = MibTableColumn
dfl210HttpAlgTotalRequested = _Dfl210HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1, 1, 3),
    _Dfl210HttpAlgTotalRequested_Type()
)
dfl210HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgTotalRequested.setStatus("current")
_Dfl210HttpAlgTotalAllowed_Type = Gauge32
_Dfl210HttpAlgTotalAllowed_Object = MibTableColumn
dfl210HttpAlgTotalAllowed = _Dfl210HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1, 1, 4),
    _Dfl210HttpAlgTotalAllowed_Type()
)
dfl210HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgTotalAllowed.setStatus("current")
_Dfl210HttpAlgTotalBlocked_Type = Gauge32
_Dfl210HttpAlgTotalBlocked_Object = MibTableColumn
dfl210HttpAlgTotalBlocked = _Dfl210HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 1, 1, 5),
    _Dfl210HttpAlgTotalBlocked_Type()
)
dfl210HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgTotalBlocked.setStatus("current")
_Dfl210HttpAlgCntFltTable_Object = MibTable
dfl210HttpAlgCntFltTable = _Dfl210HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltTable.setStatus("current")
_Dfl210HttpAlgCntFltEntry_Object = MibTableRow
dfl210HttpAlgCntFltEntry = _Dfl210HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2, 1)
)
dfl210HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210HttpAlgIndex"),
    (0, "DFL210-MIB", "dfl210HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltEntry.setStatus("current")


class _Dfl210HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl210HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl210HttpAlgCntFltIndex_Object = MibTableColumn
dfl210HttpAlgCntFltIndex = _Dfl210HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2, 1, 1),
    _Dfl210HttpAlgCntFltIndex_Type()
)
dfl210HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltIndex.setStatus("current")
_Dfl210HttpAlgCntFltName_Type = DisplayString
_Dfl210HttpAlgCntFltName_Object = MibTableColumn
dfl210HttpAlgCntFltName = _Dfl210HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2, 1, 2),
    _Dfl210HttpAlgCntFltName_Type()
)
dfl210HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltName.setStatus("current")
_Dfl210HttpAlgCntFltRequests_Type = Gauge32
_Dfl210HttpAlgCntFltRequests_Object = MibTableColumn
dfl210HttpAlgCntFltRequests = _Dfl210HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2, 1, 3),
    _Dfl210HttpAlgCntFltRequests_Type()
)
dfl210HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltRequests.setStatus("current")
_Dfl210HttpAlgCntFltAllowed_Type = Gauge32
_Dfl210HttpAlgCntFltAllowed_Object = MibTableColumn
dfl210HttpAlgCntFltAllowed = _Dfl210HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2, 1, 4),
    _Dfl210HttpAlgCntFltAllowed_Type()
)
dfl210HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltAllowed.setStatus("current")
_Dfl210HttpAlgCntFltBlocked_Type = Gauge32
_Dfl210HttpAlgCntFltBlocked_Object = MibTableColumn
dfl210HttpAlgCntFltBlocked = _Dfl210HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 4, 2, 1, 5),
    _Dfl210HttpAlgCntFltBlocked_Type()
)
dfl210HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HttpAlgCntFltBlocked.setStatus("current")
_Dfl210SmtpAlg_ObjectIdentity = ObjectIdentity
dfl210SmtpAlg = _Dfl210SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5)
)
_Dfl210SmtpAlgTable_Object = MibTable
dfl210SmtpAlgTable = _Dfl210SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl210SmtpAlgTable.setStatus("current")
_Dfl210SmtpAlgEntry_Object = MibTableRow
dfl210SmtpAlgEntry = _Dfl210SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1, 1)
)
dfl210SmtpAlgEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl210SmtpAlgEntry.setStatus("current")


class _Dfl210SmtpAlgIndex_Type(Integer32):
    """Custom type dfl210SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl210SmtpAlgIndex_Object = MibTableColumn
dfl210SmtpAlgIndex = _Dfl210SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1, 1, 1),
    _Dfl210SmtpAlgIndex_Type()
)
dfl210SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210SmtpAlgIndex.setStatus("current")
_Dfl210SmtpAlgName_Type = DisplayString
_Dfl210SmtpAlgName_Object = MibTableColumn
dfl210SmtpAlgName = _Dfl210SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1, 1, 2),
    _Dfl210SmtpAlgName_Type()
)
dfl210SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgName.setStatus("current")
_Dfl210SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl210SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl210SmtpAlgTotCheckedSes = _Dfl210SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1, 1, 3),
    _Dfl210SmtpAlgTotCheckedSes_Type()
)
dfl210SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgTotCheckedSes.setStatus("current")
_Dfl210SmtpAlgTotSpamSes_Type = Gauge32
_Dfl210SmtpAlgTotSpamSes_Object = MibTableColumn
dfl210SmtpAlgTotSpamSes = _Dfl210SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1, 1, 4),
    _Dfl210SmtpAlgTotSpamSes_Type()
)
dfl210SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgTotSpamSes.setStatus("current")
_Dfl210SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl210SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl210SmtpAlgTotDroppedSes = _Dfl210SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 1, 1, 5),
    _Dfl210SmtpAlgTotDroppedSes_Type()
)
dfl210SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgTotDroppedSes.setStatus("current")
_Dfl210SmtpAlgDnsBlTable_Object = MibTable
dfl210SmtpAlgDnsBlTable = _Dfl210SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlTable.setStatus("current")
_Dfl210SmtpAlgDnsBlEntry_Object = MibTableRow
dfl210SmtpAlgDnsBlEntry = _Dfl210SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2, 1)
)
dfl210SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210SmtpAlgIndex"),
    (0, "DFL210-MIB", "dfl210SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl210SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl210SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl210SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl210SmtpAlgDnsBlIndex = _Dfl210SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2, 1, 1),
    _Dfl210SmtpAlgDnsBlIndex_Type()
)
dfl210SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlIndex.setStatus("current")
_Dfl210SmtpAlgDnsBlName_Type = DisplayString
_Dfl210SmtpAlgDnsBlName_Object = MibTableColumn
dfl210SmtpAlgDnsBlName = _Dfl210SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2, 1, 2),
    _Dfl210SmtpAlgDnsBlName_Type()
)
dfl210SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlName.setStatus("current")
_Dfl210SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl210SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl210SmtpAlgDnsBlChecked = _Dfl210SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2, 1, 3),
    _Dfl210SmtpAlgDnsBlChecked_Type()
)
dfl210SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlChecked.setStatus("current")
_Dfl210SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl210SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl210SmtpAlgDnsBlMatched = _Dfl210SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2, 1, 4),
    _Dfl210SmtpAlgDnsBlMatched_Type()
)
dfl210SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlMatched.setStatus("current")
_Dfl210SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl210SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl210SmtpAlgDnsBlFailChecks = _Dfl210SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 9, 5, 2, 1, 5),
    _Dfl210SmtpAlgDnsBlFailChecks_Type()
)
dfl210SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl210DHCPRelay_ObjectIdentity = ObjectIdentity
dfl210DHCPRelay = _Dfl210DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11)
)
_Dfl210DHCPRelayCurClients_Type = Gauge32
_Dfl210DHCPRelayCurClients_Object = MibScalar
dfl210DHCPRelayCurClients = _Dfl210DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 1),
    _Dfl210DHCPRelayCurClients_Type()
)
dfl210DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayCurClients.setStatus("current")
_Dfl210DHCPRelayCurTrans_Type = Gauge32
_Dfl210DHCPRelayCurTrans_Object = MibScalar
dfl210DHCPRelayCurTrans = _Dfl210DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 2),
    _Dfl210DHCPRelayCurTrans_Type()
)
dfl210DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayCurTrans.setStatus("current")
_Dfl210DHCPRelayRejected_Type = Gauge32
_Dfl210DHCPRelayRejected_Object = MibScalar
dfl210DHCPRelayRejected = _Dfl210DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 3),
    _Dfl210DHCPRelayRejected_Type()
)
dfl210DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRejected.setStatus("current")
_Dfl210DHCPRelayRuleTable_Object = MibTable
dfl210DHCPRelayRuleTable = _Dfl210DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleTable.setStatus("current")
_Dfl210DHCPRelayRuleEntry_Object = MibTableRow
dfl210DHCPRelayRuleEntry = _Dfl210DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1)
)
dfl210DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL210-MIB", "dfl210DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleEntry.setStatus("current")


class _Dfl210DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl210DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl210DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl210DHCPRelayRuleIndex_Object = MibTableColumn
dfl210DHCPRelayRuleIndex = _Dfl210DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1, 1),
    _Dfl210DHCPRelayRuleIndex_Type()
)
dfl210DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleIndex.setStatus("current")
_Dfl210DHCPRelayRuleName_Type = DisplayString
_Dfl210DHCPRelayRuleName_Object = MibTableColumn
dfl210DHCPRelayRuleName = _Dfl210DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1, 2),
    _Dfl210DHCPRelayRuleName_Type()
)
dfl210DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleName.setStatus("current")
_Dfl210DHCPRelayRuleHits_Type = Gauge32
_Dfl210DHCPRelayRuleHits_Object = MibTableColumn
dfl210DHCPRelayRuleHits = _Dfl210DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1, 3),
    _Dfl210DHCPRelayRuleHits_Type()
)
dfl210DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleHits.setStatus("current")
_Dfl210DHCPRelayRuleCurClients_Type = Gauge32
_Dfl210DHCPRelayRuleCurClients_Object = MibTableColumn
dfl210DHCPRelayRuleCurClients = _Dfl210DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1, 4),
    _Dfl210DHCPRelayRuleCurClients_Type()
)
dfl210DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleCurClients.setStatus("current")
_Dfl210DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl210DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl210DHCPRelayRuleRejCliPkts = _Dfl210DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1, 5),
    _Dfl210DHCPRelayRuleRejCliPkts_Type()
)
dfl210DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl210DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl210DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl210DHCPRelayRuleRejSrvPkts = _Dfl210DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 11, 4, 1, 6),
    _Dfl210DHCPRelayRuleRejSrvPkts_Type()
)
dfl210DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl210HA_ObjectIdentity = ObjectIdentity
dfl210HA = _Dfl210HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 12)
)
_Dfl210HASyncSendQueueLength_Type = Gauge32
_Dfl210HASyncSendQueueLength_Object = MibScalar
dfl210HASyncSendQueueLength = _Dfl210HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 12, 1),
    _Dfl210HASyncSendQueueLength_Type()
)
dfl210HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HASyncSendQueueLength.setStatus("current")
_Dfl210HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl210HASyncSendQueueUsagePkt_Object = MibScalar
dfl210HASyncSendQueueUsagePkt = _Dfl210HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 12, 2),
    _Dfl210HASyncSendQueueUsagePkt_Type()
)
dfl210HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HASyncSendQueueUsagePkt.setStatus("current")
_Dfl210HASyncSendQueueUsageOct_Type = Gauge32
_Dfl210HASyncSendQueueUsageOct_Object = MibScalar
dfl210HASyncSendQueueUsageOct = _Dfl210HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 12, 3),
    _Dfl210HASyncSendQueueUsageOct_Type()
)
dfl210HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HASyncSendQueueUsageOct.setStatus("current")
_Dfl210HASyncSentPackets_Type = Counter32
_Dfl210HASyncSentPackets_Object = MibScalar
dfl210HASyncSentPackets = _Dfl210HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 12, 4),
    _Dfl210HASyncSentPackets_Type()
)
dfl210HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HASyncSentPackets.setStatus("current")
_Dfl210HASyncSendResentPackets_Type = Counter32
_Dfl210HASyncSendResentPackets_Object = MibScalar
dfl210HASyncSendResentPackets = _Dfl210HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 1, 2, 12, 5),
    _Dfl210HASyncSendResentPackets_Type()
)
dfl210HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl210HASyncSendResentPackets.setStatus("current")
_Dfl210reg_ObjectIdentity = ObjectIdentity
dfl210reg = _Dfl210reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2)
)
_Dfl210MibModules_ObjectIdentity = ObjectIdentity
dfl210MibModules = _Dfl210MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 1)
)
_Dfl210MibConfs_ObjectIdentity = ObjectIdentity
dfl210MibConfs = _Dfl210MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 2)
)
_Dfl210StatsConformance_ObjectIdentity = ObjectIdentity
dfl210StatsConformance = _Dfl210StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 2, 1)
)
_Dfl210MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl210MibObjectGroups = _Dfl210MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3)
)
_Dfl210StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl210StatsRegGroups = _Dfl210StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1)
)

# Managed Objects groups

dfl210SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 1)
)
dfl210SystemObjectGroup.setObjects(
      *(("DFL210-MIB", "dfl210SysCpuLoad"),
        ("DFL210-MIB", "dfl210SysForwardedBits"),
        ("DFL210-MIB", "dfl210SysForwardedPackets"),
        ("DFL210-MIB", "dfl210SysBuffUse"),
        ("DFL210-MIB", "dfl210SysConns"),
        ("DFL210-MIB", "dfl210HWSensorName"),
        ("DFL210-MIB", "dfl210HWSensorValue"),
        ("DFL210-MIB", "dfl210HWSensorUnit"),
        ("DFL210-MIB", "dfl210SysMemUsage"),
        ("DFL210-MIB", "dfl210SysTimerUsage"),
        ("DFL210-MIB", "dfl210SysConnOPS"),
        ("DFL210-MIB", "dfl210SysConnCPS"),
        ("DFL210-MIB", "dfl210SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl210SystemObjectGroup.setStatus("current")

dfl210IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 2)
)
dfl210IPsecObjectGroup.setObjects(
      *(("DFL210-MIB", "dfl210IPsecPhaseOneActive"),
        ("DFL210-MIB", "dfl210IPsecPhaseOneAggrModeDone"),
        ("DFL210-MIB", "dfl210IPsecQuickModeActive"),
        ("DFL210-MIB", "dfl210IPsecPhaseOneDone"),
        ("DFL210-MIB", "dfl210IPsecPhaseOneFailed"),
        ("DFL210-MIB", "dfl210IPsecPhaseOneRekeyed"),
        ("DFL210-MIB", "dfl210IPsecQuickModeDone"),
        ("DFL210-MIB", "dfl210IPsecQuickModeFailed"),
        ("DFL210-MIB", "dfl210IPsecInfoDone"),
        ("DFL210-MIB", "dfl210IPsecInfoFailed"),
        ("DFL210-MIB", "dfl210IPsecInOctetsComp"),
        ("DFL210-MIB", "dfl210IPsecInOctetsUncomp"),
        ("DFL210-MIB", "dfl210IPsecOutOctetsComp"),
        ("DFL210-MIB", "dfl210IPsecOutOctetsUncomp"),
        ("DFL210-MIB", "dfl210IPsecForwardedOctetsComp"),
        ("DFL210-MIB", "dfl210IPsecForwardedOctetsUcomp"),
        ("DFL210-MIB", "dfl210IPsecInPackets"),
        ("DFL210-MIB", "dfl210IPsecOutPackets"),
        ("DFL210-MIB", "dfl210IPsecForwardedPackets"),
        ("DFL210-MIB", "dfl210IPsecActiveTransforms"),
        ("DFL210-MIB", "dfl210IPsecTotalTransforms"),
        ("DFL210-MIB", "dfl210IPsecOutOfTransforms"),
        ("DFL210-MIB", "dfl210IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl210IPsecObjectGroup.setStatus("current")

dfl210StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 3)
)
dfl210StateCountersGroup.setObjects(
      *(("DFL210-MIB", "dfl210SysPscTcpSyn"),
        ("DFL210-MIB", "dfl210SysPscTcpOpen"),
        ("DFL210-MIB", "dfl210SysPscTcpFin"),
        ("DFL210-MIB", "dfl210SysPscUdp"),
        ("DFL210-MIB", "dfl210SysPscIcmp"),
        ("DFL210-MIB", "dfl210SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl210StateCountersGroup.setStatus("current")

dfl210IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 4)
)
dfl210IPPoolGroup.setObjects(
      *(("DFL210-MIB", "dfl210IPPoolsNumber"),
        ("DFL210-MIB", "dfl210IPPoolName"),
        ("DFL210-MIB", "dfl210IPPoolPrepare"),
        ("DFL210-MIB", "dfl210IPPoolFree"),
        ("DFL210-MIB", "dfl210IPPoolMisses"),
        ("DFL210-MIB", "dfl210IPPoolClientFails"),
        ("DFL210-MIB", "dfl210IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl210IPPoolGroup.setStatus("current")

dfl210DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 5)
)
dfl210DHCPServerGroup.setObjects(
      *(("DFL210-MIB", "dfl210DHCPTotalRejected"),
        ("DFL210-MIB", "dfl210DHCPRuleName"),
        ("DFL210-MIB", "dfl210DHCPRuleUsage"),
        ("DFL210-MIB", "dfl210DHCPRuleUsagePercent"),
        ("DFL210-MIB", "dfl210DHCPActiveClients"),
        ("DFL210-MIB", "dfl210DHCPActiveClientsPercent"),
        ("DFL210-MIB", "dfl210DHCPRejectedRequests"),
        ("DFL210-MIB", "dfl210DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl210DHCPServerGroup.setStatus("current")

dfl210RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 6)
)
dfl210RuleUseGroup.setObjects(
      *(("DFL210-MIB", "dfl210RuleName"),
        ("DFL210-MIB", "dfl210RuleUse"))
)
if mibBuilder.loadTexts:
    dfl210RuleUseGroup.setStatus("current")

dfl210UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 7)
)
dfl210UserAuthGroup.setObjects(
      *(("DFL210-MIB", "dfl210UserAuthHTTPUsers"),
        ("DFL210-MIB", "dfl210UserAuthXAUTHUsers"),
        ("DFL210-MIB", "dfl210UserAuthHTTPSUsers"),
        ("DFL210-MIB", "dfl210UserAuthPPPUsers"),
        ("DFL210-MIB", "dfl210UserAuthEAPUsers"),
        ("DFL210-MIB", "dfl210UserAuthRuleName"),
        ("DFL210-MIB", "dfl210UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl210UserAuthGroup.setStatus("current")

dfl210IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 8)
)
dfl210IfStatsGroup.setObjects(
      *(("DFL210-MIB", "dfl210IfName"),
        ("DFL210-MIB", "dfl210IfFragsIn"),
        ("DFL210-MIB", "dfl210IfFragReassOk"),
        ("DFL210-MIB", "dfl210IfFragReassFail"),
        ("DFL210-MIB", "dfl210IfPktsInCnt"),
        ("DFL210-MIB", "dfl210IfPktsOutCnt"),
        ("DFL210-MIB", "dfl210IfBitsInCnt"),
        ("DFL210-MIB", "dfl210IfBitsOutCnt"),
        ("DFL210-MIB", "dfl210IfPktsTotCnt"),
        ("DFL210-MIB", "dfl210IfBitsTotCnt"),
        ("DFL210-MIB", "dfl210IfHCPktsInCnt"),
        ("DFL210-MIB", "dfl210IfHCPktsOutCnt"),
        ("DFL210-MIB", "dfl210IfHCBitsInCnt"),
        ("DFL210-MIB", "dfl210IfHCBitsOutCnt"),
        ("DFL210-MIB", "dfl210IfHCPktsTotCnt"),
        ("DFL210-MIB", "dfl210IfHCBitsTotCnt"),
        ("DFL210-MIB", "dfl210IfRxRingFifoErrors"),
        ("DFL210-MIB", "dfl210IfRxDespools"),
        ("DFL210-MIB", "dfl210IfRxAvgUse"),
        ("DFL210-MIB", "dfl210IfRxRingSaturation"),
        ("DFL210-MIB", "dfl210RxRingFlooded"),
        ("DFL210-MIB", "dfl210IfTxDespools"),
        ("DFL210-MIB", "dfl210IfTxAvgUse"),
        ("DFL210-MIB", "dfl210IfTxRingSaturation"),
        ("DFL210-MIB", "dfl210RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl210IfStatsGroup.setStatus("current")

dfl210LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 9)
)
dfl210LinkMonitorGroup.setObjects(
      *(("DFL210-MIB", "dfl210LinkMonGrp"),
        ("DFL210-MIB", "dfl210LinkMonGrpName"),
        ("DFL210-MIB", "dfl210LinkMonGrpHostsUp"),
        ("DFL210-MIB", "dfl210LinkMonHostId"),
        ("DFL210-MIB", "dfl210LinkMonHostShortTermLoss"),
        ("DFL210-MIB", "dfl210LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl210LinkMonitorGroup.setStatus("current")

dfl210PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 10)
)
dfl210PipesObjectGroup.setObjects(
      *(("DFL210-MIB", "dfl210PipeUsers"),
        ("DFL210-MIB", "dfl210PipeName"),
        ("DFL210-MIB", "dfl210PipeMinPrec"),
        ("DFL210-MIB", "dfl210PipeMaxPrec"),
        ("DFL210-MIB", "dfl210PipeDefPrec"),
        ("DFL210-MIB", "dfl210PipeNumPrec"),
        ("DFL210-MIB", "dfl210PipeNumUsers"),
        ("DFL210-MIB", "dfl210PipeCurrentBps"),
        ("DFL210-MIB", "dfl210PipeCurrentPps"),
        ("DFL210-MIB", "dfl210PipeDelayedPackets"),
        ("DFL210-MIB", "dfl210PipeDropedPackets"),
        ("DFL210-MIB", "dfl210PipePrec"),
        ("DFL210-MIB", "dfl210PipePrecBps"),
        ("DFL210-MIB", "dfl210PipePrecTotalPps"),
        ("DFL210-MIB", "dfl210PipePrecReservedBps"),
        ("DFL210-MIB", "dfl210PipePrecDynLimBps"),
        ("DFL210-MIB", "dfl210PipePrecDynUsrLimBps"),
        ("DFL210-MIB", "dfl210PipePrecDelayedPackets"),
        ("DFL210-MIB", "dfl210PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl210PipesObjectGroup.setStatus("current")

dfl210DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 12)
)
dfl210DHCPRelayObjectGroup.setObjects(
      *(("DFL210-MIB", "dfl210DHCPRelayCurClients"),
        ("DFL210-MIB", "dfl210DHCPRelayCurTrans"),
        ("DFL210-MIB", "dfl210DHCPRelayRejected"),
        ("DFL210-MIB", "dfl210DHCPRelayRuleName"),
        ("DFL210-MIB", "dfl210DHCPRelayRuleHits"),
        ("DFL210-MIB", "dfl210DHCPRelayRuleCurClients"),
        ("DFL210-MIB", "dfl210DHCPRelayRuleRejCliPkts"),
        ("DFL210-MIB", "dfl210DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl210DHCPRelayObjectGroup.setStatus("current")

dfl210AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 13)
)
dfl210AlgGroup.setObjects(
      *(("DFL210-MIB", "dfl210AlgSessions"),
        ("DFL210-MIB", "dfl210AlgConnections"),
        ("DFL210-MIB", "dfl210AlgTCPStreams"),
        ("DFL210-MIB", "dfl210HttpAlgName"),
        ("DFL210-MIB", "dfl210HttpAlgTotalRequested"),
        ("DFL210-MIB", "dfl210HttpAlgTotalAllowed"),
        ("DFL210-MIB", "dfl210HttpAlgTotalBlocked"),
        ("DFL210-MIB", "dfl210HttpAlgCntFltName"),
        ("DFL210-MIB", "dfl210HttpAlgCntFltRequests"),
        ("DFL210-MIB", "dfl210HttpAlgCntFltAllowed"),
        ("DFL210-MIB", "dfl210HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl210AlgGroup.setStatus("current")

dfl210HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 14)
)
dfl210HAGroup.setObjects(
      *(("DFL210-MIB", "dfl210HASyncSendQueueLength"),
        ("DFL210-MIB", "dfl210HASyncSendQueueUsagePkt"),
        ("DFL210-MIB", "dfl210HASyncSendQueueUsageOct"),
        ("DFL210-MIB", "dfl210HASyncSentPackets"),
        ("DFL210-MIB", "dfl210HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl210HAGroup.setStatus("current")

dfl210IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 15)
)
dfl210IfVlanGroup.setObjects(
      *(("DFL210-MIB", "dfl210IfVlanUntaggedInPkts"),
        ("DFL210-MIB", "dfl210IfVlanUntaggedOutPkts"),
        ("DFL210-MIB", "dfl210IfVlanUntaggedTotPkts"),
        ("DFL210-MIB", "dfl210IfVlanUntaggedInOctets"),
        ("DFL210-MIB", "dfl210IfVlanUntaggedOutOctets"),
        ("DFL210-MIB", "dfl210IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl210IfVlanGroup.setStatus("current")

dfl210SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 16)
)
dfl210SmtpAlgGroup.setObjects(
      *(("DFL210-MIB", "dfl210SmtpAlgName"),
        ("DFL210-MIB", "dfl210SmtpAlgTotCheckedSes"),
        ("DFL210-MIB", "dfl210SmtpAlgTotSpamSes"),
        ("DFL210-MIB", "dfl210SmtpAlgTotDroppedSes"),
        ("DFL210-MIB", "dfl210SmtpAlgDnsBlName"),
        ("DFL210-MIB", "dfl210SmtpAlgDnsBlChecked"),
        ("DFL210-MIB", "dfl210SmtpAlgDnsBlMatched"),
        ("DFL210-MIB", "dfl210SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl210SmtpAlgGroup.setStatus("current")

dfl210SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 3, 1, 17)
)
dfl210SysTCPGroup.setObjects(
      *(("DFL210-MIB", "dfl210SysTCPRecvSmall"),
        ("DFL210-MIB", "dfl210SysTCPRecvLarge"),
        ("DFL210-MIB", "dfl210SysTCPSendSmall"),
        ("DFL210-MIB", "dfl210SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl210SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl210StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl210StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL210-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "ipsFirewall": ipsFirewall,
       "dfl210": dfl210,
       "dfl210OS": dfl210OS,
       "dfl210OSStats": dfl210OSStats,
       "dfl210System": dfl210System,
       "dfl210SysCpuLoad": dfl210SysCpuLoad,
       "dfl210SysForwardedBits": dfl210SysForwardedBits,
       "dfl210SysForwardedPackets": dfl210SysForwardedPackets,
       "dfl210SysBuffUse": dfl210SysBuffUse,
       "dfl210SysConns": dfl210SysConns,
       "dfl210SysPerStateCounters": dfl210SysPerStateCounters,
       "dfl210SysPscTcpSyn": dfl210SysPscTcpSyn,
       "dfl210SysPscTcpOpen": dfl210SysPscTcpOpen,
       "dfl210SysPscTcpFin": dfl210SysPscTcpFin,
       "dfl210SysPscUdp": dfl210SysPscUdp,
       "dfl210SysPscIcmp": dfl210SysPscIcmp,
       "dfl210SysPscOther": dfl210SysPscOther,
       "dfl210IfStatsTable": dfl210IfStatsTable,
       "dfl210IfStatsEntry": dfl210IfStatsEntry,
       "dfl210IfStatsIndex": dfl210IfStatsIndex,
       "dfl210IfName": dfl210IfName,
       "dfl210IfFragsIn": dfl210IfFragsIn,
       "dfl210IfFragReassOk": dfl210IfFragReassOk,
       "dfl210IfFragReassFail": dfl210IfFragReassFail,
       "dfl210IfPktsInCnt": dfl210IfPktsInCnt,
       "dfl210IfPktsOutCnt": dfl210IfPktsOutCnt,
       "dfl210IfBitsInCnt": dfl210IfBitsInCnt,
       "dfl210IfBitsOutCnt": dfl210IfBitsOutCnt,
       "dfl210IfPktsTotCnt": dfl210IfPktsTotCnt,
       "dfl210IfBitsTotCnt": dfl210IfBitsTotCnt,
       "dfl210IfHCPktsInCnt": dfl210IfHCPktsInCnt,
       "dfl210IfHCPktsOutCnt": dfl210IfHCPktsOutCnt,
       "dfl210IfHCBitsInCnt": dfl210IfHCBitsInCnt,
       "dfl210IfHCBitsOutCnt": dfl210IfHCBitsOutCnt,
       "dfl210IfHCPktsTotCnt": dfl210IfHCPktsTotCnt,
       "dfl210IfHCBitsTotCnt": dfl210IfHCBitsTotCnt,
       "dfl210IfRxRingTable": dfl210IfRxRingTable,
       "dfl210IfRxRingEntry": dfl210IfRxRingEntry,
       "dfl210IfRxRingIndex": dfl210IfRxRingIndex,
       "dfl210IfRxRingFifoErrors": dfl210IfRxRingFifoErrors,
       "dfl210IfRxDespools": dfl210IfRxDespools,
       "dfl210IfRxAvgUse": dfl210IfRxAvgUse,
       "dfl210IfRxRingSaturation": dfl210IfRxRingSaturation,
       "dfl210RxRingFlooded": dfl210RxRingFlooded,
       "dfl210IfTxRingTable": dfl210IfTxRingTable,
       "dfl210IfTxRingEntry": dfl210IfTxRingEntry,
       "dfl210IfTxRingIndex": dfl210IfTxRingIndex,
       "dfl210IfTxDespools": dfl210IfTxDespools,
       "dfl210IfTxAvgUse": dfl210IfTxAvgUse,
       "dfl210IfTxRingSaturation": dfl210IfTxRingSaturation,
       "dfl210RxTingFlooded": dfl210RxTingFlooded,
       "dfl210IfVlanStatsTable": dfl210IfVlanStatsTable,
       "dfl210IfVlanStatsEntry": dfl210IfVlanStatsEntry,
       "dfl210IfVlanIndex": dfl210IfVlanIndex,
       "dfl210IfVlanUntaggedInPkts": dfl210IfVlanUntaggedInPkts,
       "dfl210IfVlanUntaggedOutPkts": dfl210IfVlanUntaggedOutPkts,
       "dfl210IfVlanUntaggedTotPkts": dfl210IfVlanUntaggedTotPkts,
       "dfl210IfVlanUntaggedInOctets": dfl210IfVlanUntaggedInOctets,
       "dfl210IfVlanUntaggedOutOctets": dfl210IfVlanUntaggedOutOctets,
       "dfl210IfVlanUntaggedTotOctets": dfl210IfVlanUntaggedTotOctets,
       "dfl210HWSensorTable": dfl210HWSensorTable,
       "dfl210HWSensorEntry": dfl210HWSensorEntry,
       "dfl210HWSensorIndex": dfl210HWSensorIndex,
       "dfl210HWSensorName": dfl210HWSensorName,
       "dfl210HWSensorValue": dfl210HWSensorValue,
       "dfl210HWSensorUnit": dfl210HWSensorUnit,
       "dfl210SysMemUsage": dfl210SysMemUsage,
       "dfl210SysTCPUsage": dfl210SysTCPUsage,
       "dfl210SysTCPRecvSmall": dfl210SysTCPRecvSmall,
       "dfl210SysTCPRecvLarge": dfl210SysTCPRecvLarge,
       "dfl210SysTCPSendSmall": dfl210SysTCPSendSmall,
       "dfl210SysTCPSendLarge": dfl210SysTCPSendLarge,
       "dfl210SysTimerUsage": dfl210SysTimerUsage,
       "dfl210SysConnOPS": dfl210SysConnOPS,
       "dfl210SysConnCPS": dfl210SysConnCPS,
       "dfl210SysHCForwardedBits": dfl210SysHCForwardedBits,
       "dfl210VPN": dfl210VPN,
       "dfl210IPsec": dfl210IPsec,
       "dfl210IPsecGlobal": dfl210IPsecGlobal,
       "dfl210IPsecPhaseOneActive": dfl210IPsecPhaseOneActive,
       "dfl210IPsecPhaseOneAggrModeDone": dfl210IPsecPhaseOneAggrModeDone,
       "dfl210IPsecQuickModeActive": dfl210IPsecQuickModeActive,
       "dfl210IPsecPhaseOneDone": dfl210IPsecPhaseOneDone,
       "dfl210IPsecPhaseOneFailed": dfl210IPsecPhaseOneFailed,
       "dfl210IPsecPhaseOneRekeyed": dfl210IPsecPhaseOneRekeyed,
       "dfl210IPsecQuickModeDone": dfl210IPsecQuickModeDone,
       "dfl210IPsecQuickModeFailed": dfl210IPsecQuickModeFailed,
       "dfl210IPsecInfoDone": dfl210IPsecInfoDone,
       "dfl210IPsecInfoFailed": dfl210IPsecInfoFailed,
       "dfl210IPsecInOctetsComp": dfl210IPsecInOctetsComp,
       "dfl210IPsecInOctetsUncomp": dfl210IPsecInOctetsUncomp,
       "dfl210IPsecOutOctetsComp": dfl210IPsecOutOctetsComp,
       "dfl210IPsecOutOctetsUncomp": dfl210IPsecOutOctetsUncomp,
       "dfl210IPsecForwardedOctetsComp": dfl210IPsecForwardedOctetsComp,
       "dfl210IPsecForwardedOctetsUcomp": dfl210IPsecForwardedOctetsUcomp,
       "dfl210IPsecInPackets": dfl210IPsecInPackets,
       "dfl210IPsecOutPackets": dfl210IPsecOutPackets,
       "dfl210IPsecForwardedPackets": dfl210IPsecForwardedPackets,
       "dfl210IPsecActiveTransforms": dfl210IPsecActiveTransforms,
       "dfl210IPsecTotalTransforms": dfl210IPsecTotalTransforms,
       "dfl210IPsecOutOfTransforms": dfl210IPsecOutOfTransforms,
       "dfl210IPsecTotalRekeys": dfl210IPsecTotalRekeys,
       "dfl210Rules": dfl210Rules,
       "dfl210RuleUseTable": dfl210RuleUseTable,
       "dfl210RuleUseEntry": dfl210RuleUseEntry,
       "dfl210RuleIndex": dfl210RuleIndex,
       "dfl210RuleName": dfl210RuleName,
       "dfl210RuleUse": dfl210RuleUse,
       "dfl210IPPools": dfl210IPPools,
       "dfl210IPPoolsNumber": dfl210IPPoolsNumber,
       "dfl210IPPoolTable": dfl210IPPoolTable,
       "dfl210IPPoolEntry": dfl210IPPoolEntry,
       "dfl210IPPoolIndex": dfl210IPPoolIndex,
       "dfl210IPPoolName": dfl210IPPoolName,
       "dfl210IPPoolPrepare": dfl210IPPoolPrepare,
       "dfl210IPPoolFree": dfl210IPPoolFree,
       "dfl210IPPoolMisses": dfl210IPPoolMisses,
       "dfl210IPPoolClientFails": dfl210IPPoolClientFails,
       "dfl210IPPoolUsed": dfl210IPPoolUsed,
       "dfl210DHCPServer": dfl210DHCPServer,
       "dfl210DHCPTotalRejected": dfl210DHCPTotalRejected,
       "dfl210DHCPRuleTable": dfl210DHCPRuleTable,
       "dfl210DHCPRuleEntry": dfl210DHCPRuleEntry,
       "dfl210DHCPRuleIndex": dfl210DHCPRuleIndex,
       "dfl210DHCPRuleName": dfl210DHCPRuleName,
       "dfl210DHCPRuleUsage": dfl210DHCPRuleUsage,
       "dfl210DHCPRuleUsagePercent": dfl210DHCPRuleUsagePercent,
       "dfl210DHCPActiveClients": dfl210DHCPActiveClients,
       "dfl210DHCPActiveClientsPercent": dfl210DHCPActiveClientsPercent,
       "dfl210DHCPRejectedRequests": dfl210DHCPRejectedRequests,
       "dfl210DHCPTotalLeases": dfl210DHCPTotalLeases,
       "dfl210UserAuth": dfl210UserAuth,
       "dfl210UserAuthHTTPUsers": dfl210UserAuthHTTPUsers,
       "dfl210UserAuthXAUTHUsers": dfl210UserAuthXAUTHUsers,
       "dfl210UserAuthHTTPSUsers": dfl210UserAuthHTTPSUsers,
       "dfl210UserAuthPPPUsers": dfl210UserAuthPPPUsers,
       "dfl210UserAuthEAPUsers": dfl210UserAuthEAPUsers,
       "dfl210UserAuthRuleUseTable": dfl210UserAuthRuleUseTable,
       "dfl210UserAuthRuleUseEntry": dfl210UserAuthRuleUseEntry,
       "dfl210UserAuthRuleIndex": dfl210UserAuthRuleIndex,
       "dfl210UserAuthRuleName": dfl210UserAuthRuleName,
       "dfl210UserAuthRuleUse": dfl210UserAuthRuleUse,
       "dfl210LinkMonitor": dfl210LinkMonitor,
       "dfl210LinkMonGrp": dfl210LinkMonGrp,
       "dfl210LinkMonGrpTable": dfl210LinkMonGrpTable,
       "dfl210LinkMonGrpEntry": dfl210LinkMonGrpEntry,
       "dfl210LinkMonGrpIndex": dfl210LinkMonGrpIndex,
       "dfl210LinkMonGrpName": dfl210LinkMonGrpName,
       "dfl210LinkMonGrpHostsUp": dfl210LinkMonGrpHostsUp,
       "dfl210LinkMonHostTable": dfl210LinkMonHostTable,
       "dfl210LinkMonHostEntry": dfl210LinkMonHostEntry,
       "dfl210LinkMonHostIndex": dfl210LinkMonHostIndex,
       "dfl210LinkMonHostId": dfl210LinkMonHostId,
       "dfl210LinkMonHostShortTermLoss": dfl210LinkMonHostShortTermLoss,
       "dfl210LinkMonHostPacketsLost": dfl210LinkMonHostPacketsLost,
       "dfl210Pipes": dfl210Pipes,
       "dfl210PipeUsers": dfl210PipeUsers,
       "dfl210PipeTable": dfl210PipeTable,
       "dfl210PipeEntry": dfl210PipeEntry,
       "dfl210PipeIndex": dfl210PipeIndex,
       "dfl210PipeName": dfl210PipeName,
       "dfl210PipeMinPrec": dfl210PipeMinPrec,
       "dfl210PipeMaxPrec": dfl210PipeMaxPrec,
       "dfl210PipeDefPrec": dfl210PipeDefPrec,
       "dfl210PipeNumPrec": dfl210PipeNumPrec,
       "dfl210PipeNumUsers": dfl210PipeNumUsers,
       "dfl210PipeCurrentBps": dfl210PipeCurrentBps,
       "dfl210PipeCurrentPps": dfl210PipeCurrentPps,
       "dfl210PipeDelayedPackets": dfl210PipeDelayedPackets,
       "dfl210PipeDropedPackets": dfl210PipeDropedPackets,
       "dfl210PipePrecTable": dfl210PipePrecTable,
       "dfl210PipePrecEntry": dfl210PipePrecEntry,
       "dfl210PipePrecIndex": dfl210PipePrecIndex,
       "dfl210PipePrec": dfl210PipePrec,
       "dfl210PipePrecBps": dfl210PipePrecBps,
       "dfl210PipePrecTotalPps": dfl210PipePrecTotalPps,
       "dfl210PipePrecReservedBps": dfl210PipePrecReservedBps,
       "dfl210PipePrecDynLimBps": dfl210PipePrecDynLimBps,
       "dfl210PipePrecDynUsrLimBps": dfl210PipePrecDynUsrLimBps,
       "dfl210PipePrecDelayedPackets": dfl210PipePrecDelayedPackets,
       "dfl210PipePrecDropedPackets": dfl210PipePrecDropedPackets,
       "dfl210ALG": dfl210ALG,
       "dfl210AlgSessions": dfl210AlgSessions,
       "dfl210AlgConnections": dfl210AlgConnections,
       "dfl210AlgTCPStreams": dfl210AlgTCPStreams,
       "dfl210HttpAlg": dfl210HttpAlg,
       "dfl210HttpAlgTable": dfl210HttpAlgTable,
       "dfl210HttpAlgEntry": dfl210HttpAlgEntry,
       "dfl210HttpAlgIndex": dfl210HttpAlgIndex,
       "dfl210HttpAlgName": dfl210HttpAlgName,
       "dfl210HttpAlgTotalRequested": dfl210HttpAlgTotalRequested,
       "dfl210HttpAlgTotalAllowed": dfl210HttpAlgTotalAllowed,
       "dfl210HttpAlgTotalBlocked": dfl210HttpAlgTotalBlocked,
       "dfl210HttpAlgCntFltTable": dfl210HttpAlgCntFltTable,
       "dfl210HttpAlgCntFltEntry": dfl210HttpAlgCntFltEntry,
       "dfl210HttpAlgCntFltIndex": dfl210HttpAlgCntFltIndex,
       "dfl210HttpAlgCntFltName": dfl210HttpAlgCntFltName,
       "dfl210HttpAlgCntFltRequests": dfl210HttpAlgCntFltRequests,
       "dfl210HttpAlgCntFltAllowed": dfl210HttpAlgCntFltAllowed,
       "dfl210HttpAlgCntFltBlocked": dfl210HttpAlgCntFltBlocked,
       "dfl210SmtpAlg": dfl210SmtpAlg,
       "dfl210SmtpAlgTable": dfl210SmtpAlgTable,
       "dfl210SmtpAlgEntry": dfl210SmtpAlgEntry,
       "dfl210SmtpAlgIndex": dfl210SmtpAlgIndex,
       "dfl210SmtpAlgName": dfl210SmtpAlgName,
       "dfl210SmtpAlgTotCheckedSes": dfl210SmtpAlgTotCheckedSes,
       "dfl210SmtpAlgTotSpamSes": dfl210SmtpAlgTotSpamSes,
       "dfl210SmtpAlgTotDroppedSes": dfl210SmtpAlgTotDroppedSes,
       "dfl210SmtpAlgDnsBlTable": dfl210SmtpAlgDnsBlTable,
       "dfl210SmtpAlgDnsBlEntry": dfl210SmtpAlgDnsBlEntry,
       "dfl210SmtpAlgDnsBlIndex": dfl210SmtpAlgDnsBlIndex,
       "dfl210SmtpAlgDnsBlName": dfl210SmtpAlgDnsBlName,
       "dfl210SmtpAlgDnsBlChecked": dfl210SmtpAlgDnsBlChecked,
       "dfl210SmtpAlgDnsBlMatched": dfl210SmtpAlgDnsBlMatched,
       "dfl210SmtpAlgDnsBlFailChecks": dfl210SmtpAlgDnsBlFailChecks,
       "dfl210DHCPRelay": dfl210DHCPRelay,
       "dfl210DHCPRelayCurClients": dfl210DHCPRelayCurClients,
       "dfl210DHCPRelayCurTrans": dfl210DHCPRelayCurTrans,
       "dfl210DHCPRelayRejected": dfl210DHCPRelayRejected,
       "dfl210DHCPRelayRuleTable": dfl210DHCPRelayRuleTable,
       "dfl210DHCPRelayRuleEntry": dfl210DHCPRelayRuleEntry,
       "dfl210DHCPRelayRuleIndex": dfl210DHCPRelayRuleIndex,
       "dfl210DHCPRelayRuleName": dfl210DHCPRelayRuleName,
       "dfl210DHCPRelayRuleHits": dfl210DHCPRelayRuleHits,
       "dfl210DHCPRelayRuleCurClients": dfl210DHCPRelayRuleCurClients,
       "dfl210DHCPRelayRuleRejCliPkts": dfl210DHCPRelayRuleRejCliPkts,
       "dfl210DHCPRelayRuleRejSrvPkts": dfl210DHCPRelayRuleRejSrvPkts,
       "dfl210HA": dfl210HA,
       "dfl210HASyncSendQueueLength": dfl210HASyncSendQueueLength,
       "dfl210HASyncSendQueueUsagePkt": dfl210HASyncSendQueueUsagePkt,
       "dfl210HASyncSendQueueUsageOct": dfl210HASyncSendQueueUsageOct,
       "dfl210HASyncSentPackets": dfl210HASyncSentPackets,
       "dfl210HASyncSendResentPackets": dfl210HASyncSendResentPackets,
       "dfl210reg": dfl210reg,
       "dfl210MibModules": dfl210MibModules,
       "dfl210-MIB": dfl210_MIB,
       "dfl210MibConfs": dfl210MibConfs,
       "dfl210StatsConformance": dfl210StatsConformance,
       "dfl210StatsCompliance": dfl210StatsCompliance,
       "dfl210MibObjectGroups": dfl210MibObjectGroups,
       "dfl210StatsRegGroups": dfl210StatsRegGroups,
       "dfl210SystemObjectGroup": dfl210SystemObjectGroup,
       "dfl210IPsecObjectGroup": dfl210IPsecObjectGroup,
       "dfl210StateCountersGroup": dfl210StateCountersGroup,
       "dfl210IPPoolGroup": dfl210IPPoolGroup,
       "dfl210DHCPServerGroup": dfl210DHCPServerGroup,
       "dfl210RuleUseGroup": dfl210RuleUseGroup,
       "dfl210UserAuthGroup": dfl210UserAuthGroup,
       "dfl210IfStatsGroup": dfl210IfStatsGroup,
       "dfl210LinkMonitorGroup": dfl210LinkMonitorGroup,
       "dfl210PipesObjectGroup": dfl210PipesObjectGroup,
       "dfl210DHCPRelayObjectGroup": dfl210DHCPRelayObjectGroup,
       "dfl210AlgGroup": dfl210AlgGroup,
       "dfl210HAGroup": dfl210HAGroup,
       "dfl210IfVlanGroup": dfl210IfVlanGroup,
       "dfl210SmtpAlgGroup": dfl210SmtpAlgGroup,
       "dfl210SysTCPGroup": dfl210SysTCPGroup}
)
