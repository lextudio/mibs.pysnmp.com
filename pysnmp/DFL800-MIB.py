# SNMP MIB module (DFL800-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL800-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:18 2024
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

dfl800_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 1, 2)
)
dfl800_MIB.setRevisions(
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
_Dfl800_ObjectIdentity = ObjectIdentity
dfl800 = _Dfl800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2)
)
_Dfl800OS_ObjectIdentity = ObjectIdentity
dfl800OS = _Dfl800OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1)
)
_Dfl800OSStats_ObjectIdentity = ObjectIdentity
dfl800OSStats = _Dfl800OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2)
)
_Dfl800System_ObjectIdentity = ObjectIdentity
dfl800System = _Dfl800System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1)
)
_Dfl800SysCpuLoad_Type = Gauge32
_Dfl800SysCpuLoad_Object = MibScalar
dfl800SysCpuLoad = _Dfl800SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 1),
    _Dfl800SysCpuLoad_Type()
)
dfl800SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysCpuLoad.setStatus("current")
_Dfl800SysForwardedBits_Type = Counter32
_Dfl800SysForwardedBits_Object = MibScalar
dfl800SysForwardedBits = _Dfl800SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 2),
    _Dfl800SysForwardedBits_Type()
)
dfl800SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysForwardedBits.setStatus("current")
_Dfl800SysForwardedPackets_Type = Counter32
_Dfl800SysForwardedPackets_Object = MibScalar
dfl800SysForwardedPackets = _Dfl800SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 3),
    _Dfl800SysForwardedPackets_Type()
)
dfl800SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysForwardedPackets.setStatus("current")
_Dfl800SysBuffUse_Type = Gauge32
_Dfl800SysBuffUse_Object = MibScalar
dfl800SysBuffUse = _Dfl800SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 4),
    _Dfl800SysBuffUse_Type()
)
dfl800SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysBuffUse.setStatus("current")
_Dfl800SysConns_Type = Gauge32
_Dfl800SysConns_Object = MibScalar
dfl800SysConns = _Dfl800SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 5),
    _Dfl800SysConns_Type()
)
dfl800SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysConns.setStatus("current")
_Dfl800SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl800SysPerStateCounters = _Dfl800SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6)
)
_Dfl800SysPscTcpSyn_Type = Gauge32
_Dfl800SysPscTcpSyn_Object = MibScalar
dfl800SysPscTcpSyn = _Dfl800SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6, 1),
    _Dfl800SysPscTcpSyn_Type()
)
dfl800SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysPscTcpSyn.setStatus("current")
_Dfl800SysPscTcpOpen_Type = Gauge32
_Dfl800SysPscTcpOpen_Object = MibScalar
dfl800SysPscTcpOpen = _Dfl800SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6, 2),
    _Dfl800SysPscTcpOpen_Type()
)
dfl800SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysPscTcpOpen.setStatus("current")
_Dfl800SysPscTcpFin_Type = Gauge32
_Dfl800SysPscTcpFin_Object = MibScalar
dfl800SysPscTcpFin = _Dfl800SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6, 3),
    _Dfl800SysPscTcpFin_Type()
)
dfl800SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysPscTcpFin.setStatus("current")
_Dfl800SysPscUdp_Type = Gauge32
_Dfl800SysPscUdp_Object = MibScalar
dfl800SysPscUdp = _Dfl800SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6, 4),
    _Dfl800SysPscUdp_Type()
)
dfl800SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysPscUdp.setStatus("current")
_Dfl800SysPscIcmp_Type = Gauge32
_Dfl800SysPscIcmp_Object = MibScalar
dfl800SysPscIcmp = _Dfl800SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6, 5),
    _Dfl800SysPscIcmp_Type()
)
dfl800SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysPscIcmp.setStatus("current")
_Dfl800SysPscOther_Type = Gauge32
_Dfl800SysPscOther_Object = MibScalar
dfl800SysPscOther = _Dfl800SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 6, 6),
    _Dfl800SysPscOther_Type()
)
dfl800SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysPscOther.setStatus("current")
_Dfl800IfStatsTable_Object = MibTable
dfl800IfStatsTable = _Dfl800IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl800IfStatsTable.setStatus("current")
_Dfl800IfStatsEntry_Object = MibTableRow
dfl800IfStatsEntry = _Dfl800IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1)
)
dfl800IfStatsEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl800IfStatsEntry.setStatus("current")


class _Dfl800IfStatsIndex_Type(Integer32):
    """Custom type dfl800IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800IfStatsIndex_Type.__name__ = "Integer32"
_Dfl800IfStatsIndex_Object = MibTableColumn
dfl800IfStatsIndex = _Dfl800IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 1),
    _Dfl800IfStatsIndex_Type()
)
dfl800IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800IfStatsIndex.setStatus("current")
_Dfl800IfName_Type = DisplayString
_Dfl800IfName_Object = MibTableColumn
dfl800IfName = _Dfl800IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 2),
    _Dfl800IfName_Type()
)
dfl800IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfName.setStatus("current")
_Dfl800IfFragsIn_Type = Counter32
_Dfl800IfFragsIn_Object = MibTableColumn
dfl800IfFragsIn = _Dfl800IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 3),
    _Dfl800IfFragsIn_Type()
)
dfl800IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfFragsIn.setStatus("current")
_Dfl800IfFragReassOk_Type = Counter32
_Dfl800IfFragReassOk_Object = MibTableColumn
dfl800IfFragReassOk = _Dfl800IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 4),
    _Dfl800IfFragReassOk_Type()
)
dfl800IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfFragReassOk.setStatus("current")
_Dfl800IfFragReassFail_Type = Counter32
_Dfl800IfFragReassFail_Object = MibTableColumn
dfl800IfFragReassFail = _Dfl800IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 5),
    _Dfl800IfFragReassFail_Type()
)
dfl800IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfFragReassFail.setStatus("current")
_Dfl800IfPktsInCnt_Type = Counter32
_Dfl800IfPktsInCnt_Object = MibTableColumn
dfl800IfPktsInCnt = _Dfl800IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 6),
    _Dfl800IfPktsInCnt_Type()
)
dfl800IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfPktsInCnt.setStatus("current")
_Dfl800IfPktsOutCnt_Type = Counter32
_Dfl800IfPktsOutCnt_Object = MibTableColumn
dfl800IfPktsOutCnt = _Dfl800IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 7),
    _Dfl800IfPktsOutCnt_Type()
)
dfl800IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfPktsOutCnt.setStatus("current")
_Dfl800IfBitsInCnt_Type = Counter32
_Dfl800IfBitsInCnt_Object = MibTableColumn
dfl800IfBitsInCnt = _Dfl800IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 8),
    _Dfl800IfBitsInCnt_Type()
)
dfl800IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfBitsInCnt.setStatus("current")
_Dfl800IfBitsOutCnt_Type = Counter32
_Dfl800IfBitsOutCnt_Object = MibTableColumn
dfl800IfBitsOutCnt = _Dfl800IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 9),
    _Dfl800IfBitsOutCnt_Type()
)
dfl800IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfBitsOutCnt.setStatus("current")
_Dfl800IfPktsTotCnt_Type = Counter32
_Dfl800IfPktsTotCnt_Object = MibTableColumn
dfl800IfPktsTotCnt = _Dfl800IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 10),
    _Dfl800IfPktsTotCnt_Type()
)
dfl800IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfPktsTotCnt.setStatus("current")
_Dfl800IfBitsTotCnt_Type = Counter32
_Dfl800IfBitsTotCnt_Object = MibTableColumn
dfl800IfBitsTotCnt = _Dfl800IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 11),
    _Dfl800IfBitsTotCnt_Type()
)
dfl800IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfBitsTotCnt.setStatus("current")
_Dfl800IfHCPktsInCnt_Type = Counter64
_Dfl800IfHCPktsInCnt_Object = MibTableColumn
dfl800IfHCPktsInCnt = _Dfl800IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 12),
    _Dfl800IfHCPktsInCnt_Type()
)
dfl800IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfHCPktsInCnt.setStatus("current")
_Dfl800IfHCPktsOutCnt_Type = Counter64
_Dfl800IfHCPktsOutCnt_Object = MibTableColumn
dfl800IfHCPktsOutCnt = _Dfl800IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 13),
    _Dfl800IfHCPktsOutCnt_Type()
)
dfl800IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfHCPktsOutCnt.setStatus("current")
_Dfl800IfHCBitsInCnt_Type = Counter64
_Dfl800IfHCBitsInCnt_Object = MibTableColumn
dfl800IfHCBitsInCnt = _Dfl800IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 14),
    _Dfl800IfHCBitsInCnt_Type()
)
dfl800IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfHCBitsInCnt.setStatus("current")
_Dfl800IfHCBitsOutCnt_Type = Counter64
_Dfl800IfHCBitsOutCnt_Object = MibTableColumn
dfl800IfHCBitsOutCnt = _Dfl800IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 15),
    _Dfl800IfHCBitsOutCnt_Type()
)
dfl800IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfHCBitsOutCnt.setStatus("current")
_Dfl800IfHCPktsTotCnt_Type = Counter64
_Dfl800IfHCPktsTotCnt_Object = MibTableColumn
dfl800IfHCPktsTotCnt = _Dfl800IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 16),
    _Dfl800IfHCPktsTotCnt_Type()
)
dfl800IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfHCPktsTotCnt.setStatus("current")
_Dfl800IfHCBitsTotCnt_Type = Counter64
_Dfl800IfHCBitsTotCnt_Object = MibTableColumn
dfl800IfHCBitsTotCnt = _Dfl800IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 7, 1, 17),
    _Dfl800IfHCBitsTotCnt_Type()
)
dfl800IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfHCBitsTotCnt.setStatus("current")
_Dfl800IfRxRingTable_Object = MibTable
dfl800IfRxRingTable = _Dfl800IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl800IfRxRingTable.setStatus("current")
_Dfl800IfRxRingEntry_Object = MibTableRow
dfl800IfRxRingEntry = _Dfl800IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1)
)
dfl800IfRxRingEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl800IfRxRingEntry.setStatus("current")


class _Dfl800IfRxRingIndex_Type(Integer32):
    """Custom type dfl800IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl800IfRxRingIndex_Object = MibTableColumn
dfl800IfRxRingIndex = _Dfl800IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1, 1),
    _Dfl800IfRxRingIndex_Type()
)
dfl800IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800IfRxRingIndex.setStatus("current")
_Dfl800IfRxRingFifoErrors_Type = Counter32
_Dfl800IfRxRingFifoErrors_Object = MibTableColumn
dfl800IfRxRingFifoErrors = _Dfl800IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1, 2),
    _Dfl800IfRxRingFifoErrors_Type()
)
dfl800IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfRxRingFifoErrors.setStatus("current")
_Dfl800IfRxDespools_Type = Gauge32
_Dfl800IfRxDespools_Object = MibTableColumn
dfl800IfRxDespools = _Dfl800IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1, 3),
    _Dfl800IfRxDespools_Type()
)
dfl800IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfRxDespools.setStatus("current")
_Dfl800IfRxAvgUse_Type = Gauge32
_Dfl800IfRxAvgUse_Object = MibTableColumn
dfl800IfRxAvgUse = _Dfl800IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1, 4),
    _Dfl800IfRxAvgUse_Type()
)
dfl800IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfRxAvgUse.setStatus("current")
_Dfl800IfRxRingSaturation_Type = Gauge32
_Dfl800IfRxRingSaturation_Object = MibTableColumn
dfl800IfRxRingSaturation = _Dfl800IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1, 5),
    _Dfl800IfRxRingSaturation_Type()
)
dfl800IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfRxRingSaturation.setStatus("current")
_Dfl800RxRingFlooded_Type = Gauge32
_Dfl800RxRingFlooded_Object = MibTableColumn
dfl800RxRingFlooded = _Dfl800RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 8, 1, 6),
    _Dfl800RxRingFlooded_Type()
)
dfl800RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800RxRingFlooded.setStatus("current")
_Dfl800IfTxRingTable_Object = MibTable
dfl800IfTxRingTable = _Dfl800IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl800IfTxRingTable.setStatus("current")
_Dfl800IfTxRingEntry_Object = MibTableRow
dfl800IfTxRingEntry = _Dfl800IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9, 1)
)
dfl800IfTxRingEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl800IfTxRingEntry.setStatus("current")


class _Dfl800IfTxRingIndex_Type(Integer32):
    """Custom type dfl800IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl800IfTxRingIndex_Object = MibTableColumn
dfl800IfTxRingIndex = _Dfl800IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9, 1, 1),
    _Dfl800IfTxRingIndex_Type()
)
dfl800IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800IfTxRingIndex.setStatus("current")
_Dfl800IfTxDespools_Type = Gauge32
_Dfl800IfTxDespools_Object = MibTableColumn
dfl800IfTxDespools = _Dfl800IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9, 1, 2),
    _Dfl800IfTxDespools_Type()
)
dfl800IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfTxDespools.setStatus("current")
_Dfl800IfTxAvgUse_Type = Gauge32
_Dfl800IfTxAvgUse_Object = MibTableColumn
dfl800IfTxAvgUse = _Dfl800IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9, 1, 3),
    _Dfl800IfTxAvgUse_Type()
)
dfl800IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfTxAvgUse.setStatus("current")
_Dfl800IfTxRingSaturation_Type = Gauge32
_Dfl800IfTxRingSaturation_Object = MibTableColumn
dfl800IfTxRingSaturation = _Dfl800IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9, 1, 4),
    _Dfl800IfTxRingSaturation_Type()
)
dfl800IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfTxRingSaturation.setStatus("current")
_Dfl800RxTingFlooded_Type = Gauge32
_Dfl800RxTingFlooded_Object = MibTableColumn
dfl800RxTingFlooded = _Dfl800RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 9, 1, 5),
    _Dfl800RxTingFlooded_Type()
)
dfl800RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800RxTingFlooded.setStatus("current")
_Dfl800IfVlanStatsTable_Object = MibTable
dfl800IfVlanStatsTable = _Dfl800IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl800IfVlanStatsTable.setStatus("current")
_Dfl800IfVlanStatsEntry_Object = MibTableRow
dfl800IfVlanStatsEntry = _Dfl800IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1)
)
dfl800IfVlanStatsEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl800IfVlanStatsEntry.setStatus("current")


class _Dfl800IfVlanIndex_Type(Integer32):
    """Custom type dfl800IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800IfVlanIndex_Type.__name__ = "Integer32"
_Dfl800IfVlanIndex_Object = MibTableColumn
dfl800IfVlanIndex = _Dfl800IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 1),
    _Dfl800IfVlanIndex_Type()
)
dfl800IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800IfVlanIndex.setStatus("current")
_Dfl800IfVlanUntaggedInPkts_Type = Counter32
_Dfl800IfVlanUntaggedInPkts_Object = MibTableColumn
dfl800IfVlanUntaggedInPkts = _Dfl800IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 2),
    _Dfl800IfVlanUntaggedInPkts_Type()
)
dfl800IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfVlanUntaggedInPkts.setStatus("current")
_Dfl800IfVlanUntaggedOutPkts_Type = Counter32
_Dfl800IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl800IfVlanUntaggedOutPkts = _Dfl800IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 3),
    _Dfl800IfVlanUntaggedOutPkts_Type()
)
dfl800IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfVlanUntaggedOutPkts.setStatus("current")
_Dfl800IfVlanUntaggedTotPkts_Type = Counter32
_Dfl800IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl800IfVlanUntaggedTotPkts = _Dfl800IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 4),
    _Dfl800IfVlanUntaggedTotPkts_Type()
)
dfl800IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfVlanUntaggedTotPkts.setStatus("current")
_Dfl800IfVlanUntaggedInOctets_Type = Counter32
_Dfl800IfVlanUntaggedInOctets_Object = MibTableColumn
dfl800IfVlanUntaggedInOctets = _Dfl800IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 5),
    _Dfl800IfVlanUntaggedInOctets_Type()
)
dfl800IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfVlanUntaggedInOctets.setStatus("current")
_Dfl800IfVlanUntaggedOutOctets_Type = Counter32
_Dfl800IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl800IfVlanUntaggedOutOctets = _Dfl800IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 6),
    _Dfl800IfVlanUntaggedOutOctets_Type()
)
dfl800IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfVlanUntaggedOutOctets.setStatus("current")
_Dfl800IfVlanUntaggedTotOctets_Type = Counter32
_Dfl800IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl800IfVlanUntaggedTotOctets = _Dfl800IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 10, 1, 7),
    _Dfl800IfVlanUntaggedTotOctets_Type()
)
dfl800IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IfVlanUntaggedTotOctets.setStatus("current")
_Dfl800HWSensorTable_Object = MibTable
dfl800HWSensorTable = _Dfl800HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl800HWSensorTable.setStatus("current")
_Dfl800HWSensorEntry_Object = MibTableRow
dfl800HWSensorEntry = _Dfl800HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 11, 1)
)
dfl800HWSensorEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl800HWSensorEntry.setStatus("current")


class _Dfl800HWSensorIndex_Type(Integer32):
    """Custom type dfl800HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800HWSensorIndex_Type.__name__ = "Integer32"
_Dfl800HWSensorIndex_Object = MibTableColumn
dfl800HWSensorIndex = _Dfl800HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 11, 1, 1),
    _Dfl800HWSensorIndex_Type()
)
dfl800HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800HWSensorIndex.setStatus("current")
_Dfl800HWSensorName_Type = DisplayString
_Dfl800HWSensorName_Object = MibTableColumn
dfl800HWSensorName = _Dfl800HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 11, 1, 2),
    _Dfl800HWSensorName_Type()
)
dfl800HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HWSensorName.setStatus("current")
_Dfl800HWSensorValue_Type = Gauge32
_Dfl800HWSensorValue_Object = MibTableColumn
dfl800HWSensorValue = _Dfl800HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 11, 1, 3),
    _Dfl800HWSensorValue_Type()
)
dfl800HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HWSensorValue.setStatus("current")
_Dfl800HWSensorUnit_Type = DisplayString
_Dfl800HWSensorUnit_Object = MibTableColumn
dfl800HWSensorUnit = _Dfl800HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 11, 1, 4),
    _Dfl800HWSensorUnit_Type()
)
dfl800HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HWSensorUnit.setStatus("current")
_Dfl800SysMemUsage_Type = Gauge32
_Dfl800SysMemUsage_Object = MibScalar
dfl800SysMemUsage = _Dfl800SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 12),
    _Dfl800SysMemUsage_Type()
)
dfl800SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysMemUsage.setStatus("current")
_Dfl800SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl800SysTCPUsage = _Dfl800SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 13)
)
_Dfl800SysTCPRecvSmall_Type = Gauge32
_Dfl800SysTCPRecvSmall_Object = MibScalar
dfl800SysTCPRecvSmall = _Dfl800SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 13, 1),
    _Dfl800SysTCPRecvSmall_Type()
)
dfl800SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysTCPRecvSmall.setStatus("current")
_Dfl800SysTCPRecvLarge_Type = Gauge32
_Dfl800SysTCPRecvLarge_Object = MibScalar
dfl800SysTCPRecvLarge = _Dfl800SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 13, 2),
    _Dfl800SysTCPRecvLarge_Type()
)
dfl800SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysTCPRecvLarge.setStatus("current")
_Dfl800SysTCPSendSmall_Type = Gauge32
_Dfl800SysTCPSendSmall_Object = MibScalar
dfl800SysTCPSendSmall = _Dfl800SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 13, 3),
    _Dfl800SysTCPSendSmall_Type()
)
dfl800SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysTCPSendSmall.setStatus("current")
_Dfl800SysTCPSendLarge_Type = Gauge32
_Dfl800SysTCPSendLarge_Object = MibScalar
dfl800SysTCPSendLarge = _Dfl800SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 13, 4),
    _Dfl800SysTCPSendLarge_Type()
)
dfl800SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysTCPSendLarge.setStatus("current")
_Dfl800SysTimerUsage_Type = Gauge32
_Dfl800SysTimerUsage_Object = MibScalar
dfl800SysTimerUsage = _Dfl800SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 14),
    _Dfl800SysTimerUsage_Type()
)
dfl800SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysTimerUsage.setStatus("current")
_Dfl800SysConnOPS_Type = Gauge32
_Dfl800SysConnOPS_Object = MibScalar
dfl800SysConnOPS = _Dfl800SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 15),
    _Dfl800SysConnOPS_Type()
)
dfl800SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysConnOPS.setStatus("current")
_Dfl800SysConnCPS_Type = Gauge32
_Dfl800SysConnCPS_Object = MibScalar
dfl800SysConnCPS = _Dfl800SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 16),
    _Dfl800SysConnCPS_Type()
)
dfl800SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysConnCPS.setStatus("current")
_Dfl800SysHCForwardedBits_Type = Counter64
_Dfl800SysHCForwardedBits_Object = MibScalar
dfl800SysHCForwardedBits = _Dfl800SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 1, 17),
    _Dfl800SysHCForwardedBits_Type()
)
dfl800SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SysHCForwardedBits.setStatus("current")
_Dfl800VPN_ObjectIdentity = ObjectIdentity
dfl800VPN = _Dfl800VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2)
)
_Dfl800IPsec_ObjectIdentity = ObjectIdentity
dfl800IPsec = _Dfl800IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1)
)
_Dfl800IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl800IPsecGlobal = _Dfl800IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1)
)
_Dfl800IPsecPhaseOneActive_Type = Gauge32
_Dfl800IPsecPhaseOneActive_Object = MibScalar
dfl800IPsecPhaseOneActive = _Dfl800IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 1),
    _Dfl800IPsecPhaseOneActive_Type()
)
dfl800IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecPhaseOneActive.setStatus("current")
_Dfl800IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl800IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl800IPsecPhaseOneAggrModeDone = _Dfl800IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 2),
    _Dfl800IPsecPhaseOneAggrModeDone_Type()
)
dfl800IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl800IPsecQuickModeActive_Type = Gauge32
_Dfl800IPsecQuickModeActive_Object = MibScalar
dfl800IPsecQuickModeActive = _Dfl800IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 3),
    _Dfl800IPsecQuickModeActive_Type()
)
dfl800IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecQuickModeActive.setStatus("current")
_Dfl800IPsecPhaseOneDone_Type = Counter32
_Dfl800IPsecPhaseOneDone_Object = MibScalar
dfl800IPsecPhaseOneDone = _Dfl800IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 4),
    _Dfl800IPsecPhaseOneDone_Type()
)
dfl800IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecPhaseOneDone.setStatus("current")
_Dfl800IPsecPhaseOneFailed_Type = Counter32
_Dfl800IPsecPhaseOneFailed_Object = MibScalar
dfl800IPsecPhaseOneFailed = _Dfl800IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 5),
    _Dfl800IPsecPhaseOneFailed_Type()
)
dfl800IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecPhaseOneFailed.setStatus("current")
_Dfl800IPsecPhaseOneRekeyed_Type = Counter32
_Dfl800IPsecPhaseOneRekeyed_Object = MibScalar
dfl800IPsecPhaseOneRekeyed = _Dfl800IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 6),
    _Dfl800IPsecPhaseOneRekeyed_Type()
)
dfl800IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecPhaseOneRekeyed.setStatus("current")
_Dfl800IPsecQuickModeDone_Type = Counter32
_Dfl800IPsecQuickModeDone_Object = MibScalar
dfl800IPsecQuickModeDone = _Dfl800IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 7),
    _Dfl800IPsecQuickModeDone_Type()
)
dfl800IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecQuickModeDone.setStatus("current")
_Dfl800IPsecQuickModeFailed_Type = Counter32
_Dfl800IPsecQuickModeFailed_Object = MibScalar
dfl800IPsecQuickModeFailed = _Dfl800IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 8),
    _Dfl800IPsecQuickModeFailed_Type()
)
dfl800IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecQuickModeFailed.setStatus("current")
_Dfl800IPsecInfoDone_Type = Counter32
_Dfl800IPsecInfoDone_Object = MibScalar
dfl800IPsecInfoDone = _Dfl800IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 9),
    _Dfl800IPsecInfoDone_Type()
)
dfl800IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecInfoDone.setStatus("current")
_Dfl800IPsecInfoFailed_Type = Counter32
_Dfl800IPsecInfoFailed_Object = MibScalar
dfl800IPsecInfoFailed = _Dfl800IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 10),
    _Dfl800IPsecInfoFailed_Type()
)
dfl800IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecInfoFailed.setStatus("current")
_Dfl800IPsecInOctetsComp_Type = Counter64
_Dfl800IPsecInOctetsComp_Object = MibScalar
dfl800IPsecInOctetsComp = _Dfl800IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 11),
    _Dfl800IPsecInOctetsComp_Type()
)
dfl800IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecInOctetsComp.setStatus("current")
_Dfl800IPsecInOctetsUncomp_Type = Counter64
_Dfl800IPsecInOctetsUncomp_Object = MibScalar
dfl800IPsecInOctetsUncomp = _Dfl800IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 12),
    _Dfl800IPsecInOctetsUncomp_Type()
)
dfl800IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecInOctetsUncomp.setStatus("current")
_Dfl800IPsecOutOctetsComp_Type = Counter64
_Dfl800IPsecOutOctetsComp_Object = MibScalar
dfl800IPsecOutOctetsComp = _Dfl800IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 13),
    _Dfl800IPsecOutOctetsComp_Type()
)
dfl800IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecOutOctetsComp.setStatus("current")
_Dfl800IPsecOutOctetsUncomp_Type = Counter64
_Dfl800IPsecOutOctetsUncomp_Object = MibScalar
dfl800IPsecOutOctetsUncomp = _Dfl800IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 14),
    _Dfl800IPsecOutOctetsUncomp_Type()
)
dfl800IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecOutOctetsUncomp.setStatus("current")
_Dfl800IPsecForwardedOctetsComp_Type = Counter64
_Dfl800IPsecForwardedOctetsComp_Object = MibScalar
dfl800IPsecForwardedOctetsComp = _Dfl800IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 15),
    _Dfl800IPsecForwardedOctetsComp_Type()
)
dfl800IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecForwardedOctetsComp.setStatus("current")
_Dfl800IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl800IPsecForwardedOctetsUcomp_Object = MibScalar
dfl800IPsecForwardedOctetsUcomp = _Dfl800IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 16),
    _Dfl800IPsecForwardedOctetsUcomp_Type()
)
dfl800IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl800IPsecInPackets_Type = Counter64
_Dfl800IPsecInPackets_Object = MibScalar
dfl800IPsecInPackets = _Dfl800IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 17),
    _Dfl800IPsecInPackets_Type()
)
dfl800IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecInPackets.setStatus("current")
_Dfl800IPsecOutPackets_Type = Counter64
_Dfl800IPsecOutPackets_Object = MibScalar
dfl800IPsecOutPackets = _Dfl800IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 18),
    _Dfl800IPsecOutPackets_Type()
)
dfl800IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecOutPackets.setStatus("current")
_Dfl800IPsecForwardedPackets_Type = Counter64
_Dfl800IPsecForwardedPackets_Object = MibScalar
dfl800IPsecForwardedPackets = _Dfl800IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 19),
    _Dfl800IPsecForwardedPackets_Type()
)
dfl800IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecForwardedPackets.setStatus("current")
_Dfl800IPsecActiveTransforms_Type = Gauge32
_Dfl800IPsecActiveTransforms_Object = MibScalar
dfl800IPsecActiveTransforms = _Dfl800IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 20),
    _Dfl800IPsecActiveTransforms_Type()
)
dfl800IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecActiveTransforms.setStatus("current")
_Dfl800IPsecTotalTransforms_Type = Counter32
_Dfl800IPsecTotalTransforms_Object = MibScalar
dfl800IPsecTotalTransforms = _Dfl800IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 21),
    _Dfl800IPsecTotalTransforms_Type()
)
dfl800IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecTotalTransforms.setStatus("current")
_Dfl800IPsecOutOfTransforms_Type = Counter32
_Dfl800IPsecOutOfTransforms_Object = MibScalar
dfl800IPsecOutOfTransforms = _Dfl800IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 22),
    _Dfl800IPsecOutOfTransforms_Type()
)
dfl800IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecOutOfTransforms.setStatus("current")
_Dfl800IPsecTotalRekeys_Type = Counter32
_Dfl800IPsecTotalRekeys_Object = MibScalar
dfl800IPsecTotalRekeys = _Dfl800IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 2, 1, 1, 23),
    _Dfl800IPsecTotalRekeys_Type()
)
dfl800IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPsecTotalRekeys.setStatus("current")
_Dfl800Rules_ObjectIdentity = ObjectIdentity
dfl800Rules = _Dfl800Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 3)
)
_Dfl800RuleUseTable_Object = MibTable
dfl800RuleUseTable = _Dfl800RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl800RuleUseTable.setStatus("current")
_Dfl800RuleUseEntry_Object = MibTableRow
dfl800RuleUseEntry = _Dfl800RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 3, 2, 1)
)
dfl800RuleUseEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl800RuleUseEntry.setStatus("current")


class _Dfl800RuleIndex_Type(Integer32):
    """Custom type dfl800RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800RuleIndex_Type.__name__ = "Integer32"
_Dfl800RuleIndex_Object = MibTableColumn
dfl800RuleIndex = _Dfl800RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 3, 2, 1, 1),
    _Dfl800RuleIndex_Type()
)
dfl800RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800RuleIndex.setStatus("current")
_Dfl800RuleName_Type = DisplayString
_Dfl800RuleName_Object = MibTableColumn
dfl800RuleName = _Dfl800RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 3, 2, 1, 2),
    _Dfl800RuleName_Type()
)
dfl800RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800RuleName.setStatus("current")
_Dfl800RuleUse_Type = Counter32
_Dfl800RuleUse_Object = MibTableColumn
dfl800RuleUse = _Dfl800RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 3, 2, 1, 3),
    _Dfl800RuleUse_Type()
)
dfl800RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800RuleUse.setStatus("current")
_Dfl800IPPools_ObjectIdentity = ObjectIdentity
dfl800IPPools = _Dfl800IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4)
)
_Dfl800IPPoolsNumber_Type = Integer32
_Dfl800IPPoolsNumber_Object = MibScalar
dfl800IPPoolsNumber = _Dfl800IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 1),
    _Dfl800IPPoolsNumber_Type()
)
dfl800IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolsNumber.setStatus("current")
_Dfl800IPPoolTable_Object = MibTable
dfl800IPPoolTable = _Dfl800IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl800IPPoolTable.setStatus("current")
_Dfl800IPPoolEntry_Object = MibTableRow
dfl800IPPoolEntry = _Dfl800IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1)
)
dfl800IPPoolEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl800IPPoolEntry.setStatus("current")


class _Dfl800IPPoolIndex_Type(Integer32):
    """Custom type dfl800IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800IPPoolIndex_Type.__name__ = "Integer32"
_Dfl800IPPoolIndex_Object = MibTableColumn
dfl800IPPoolIndex = _Dfl800IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 1),
    _Dfl800IPPoolIndex_Type()
)
dfl800IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800IPPoolIndex.setStatus("current")
_Dfl800IPPoolName_Type = DisplayString
_Dfl800IPPoolName_Object = MibTableColumn
dfl800IPPoolName = _Dfl800IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 2),
    _Dfl800IPPoolName_Type()
)
dfl800IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolName.setStatus("current")
_Dfl800IPPoolPrepare_Type = Gauge32
_Dfl800IPPoolPrepare_Object = MibTableColumn
dfl800IPPoolPrepare = _Dfl800IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 3),
    _Dfl800IPPoolPrepare_Type()
)
dfl800IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolPrepare.setStatus("current")
_Dfl800IPPoolFree_Type = Gauge32
_Dfl800IPPoolFree_Object = MibTableColumn
dfl800IPPoolFree = _Dfl800IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 4),
    _Dfl800IPPoolFree_Type()
)
dfl800IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolFree.setStatus("current")
_Dfl800IPPoolMisses_Type = Gauge32
_Dfl800IPPoolMisses_Object = MibTableColumn
dfl800IPPoolMisses = _Dfl800IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 5),
    _Dfl800IPPoolMisses_Type()
)
dfl800IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolMisses.setStatus("current")
_Dfl800IPPoolClientFails_Type = Gauge32
_Dfl800IPPoolClientFails_Object = MibTableColumn
dfl800IPPoolClientFails = _Dfl800IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 6),
    _Dfl800IPPoolClientFails_Type()
)
dfl800IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolClientFails.setStatus("current")
_Dfl800IPPoolUsed_Type = Gauge32
_Dfl800IPPoolUsed_Object = MibTableColumn
dfl800IPPoolUsed = _Dfl800IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 4, 2, 1, 7),
    _Dfl800IPPoolUsed_Type()
)
dfl800IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800IPPoolUsed.setStatus("current")
_Dfl800DHCPServer_ObjectIdentity = ObjectIdentity
dfl800DHCPServer = _Dfl800DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5)
)
_Dfl800DHCPTotalRejected_Type = Gauge32
_Dfl800DHCPTotalRejected_Object = MibScalar
dfl800DHCPTotalRejected = _Dfl800DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 1),
    _Dfl800DHCPTotalRejected_Type()
)
dfl800DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPTotalRejected.setStatus("current")
_Dfl800DHCPRuleTable_Object = MibTable
dfl800DHCPRuleTable = _Dfl800DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl800DHCPRuleTable.setStatus("current")
_Dfl800DHCPRuleEntry_Object = MibTableRow
dfl800DHCPRuleEntry = _Dfl800DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1)
)
dfl800DHCPRuleEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl800DHCPRuleEntry.setStatus("current")


class _Dfl800DHCPRuleIndex_Type(Integer32):
    """Custom type dfl800DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl800DHCPRuleIndex_Object = MibTableColumn
dfl800DHCPRuleIndex = _Dfl800DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 1),
    _Dfl800DHCPRuleIndex_Type()
)
dfl800DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800DHCPRuleIndex.setStatus("current")
_Dfl800DHCPRuleName_Type = DisplayString
_Dfl800DHCPRuleName_Object = MibTableColumn
dfl800DHCPRuleName = _Dfl800DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 2),
    _Dfl800DHCPRuleName_Type()
)
dfl800DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRuleName.setStatus("current")
_Dfl800DHCPRuleUsage_Type = Gauge32
_Dfl800DHCPRuleUsage_Object = MibTableColumn
dfl800DHCPRuleUsage = _Dfl800DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 3),
    _Dfl800DHCPRuleUsage_Type()
)
dfl800DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRuleUsage.setStatus("current")
_Dfl800DHCPRuleUsagePercent_Type = Gauge32
_Dfl800DHCPRuleUsagePercent_Object = MibTableColumn
dfl800DHCPRuleUsagePercent = _Dfl800DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 4),
    _Dfl800DHCPRuleUsagePercent_Type()
)
dfl800DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRuleUsagePercent.setStatus("current")
_Dfl800DHCPActiveClients_Type = Gauge32
_Dfl800DHCPActiveClients_Object = MibTableColumn
dfl800DHCPActiveClients = _Dfl800DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 5),
    _Dfl800DHCPActiveClients_Type()
)
dfl800DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPActiveClients.setStatus("current")
_Dfl800DHCPActiveClientsPercent_Type = Gauge32
_Dfl800DHCPActiveClientsPercent_Object = MibTableColumn
dfl800DHCPActiveClientsPercent = _Dfl800DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 6),
    _Dfl800DHCPActiveClientsPercent_Type()
)
dfl800DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPActiveClientsPercent.setStatus("current")
_Dfl800DHCPRejectedRequests_Type = Gauge32
_Dfl800DHCPRejectedRequests_Object = MibTableColumn
dfl800DHCPRejectedRequests = _Dfl800DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 7),
    _Dfl800DHCPRejectedRequests_Type()
)
dfl800DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRejectedRequests.setStatus("current")
_Dfl800DHCPTotalLeases_Type = Gauge32
_Dfl800DHCPTotalLeases_Object = MibTableColumn
dfl800DHCPTotalLeases = _Dfl800DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 5, 2, 1, 8),
    _Dfl800DHCPTotalLeases_Type()
)
dfl800DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPTotalLeases.setStatus("current")
_Dfl800UserAuth_ObjectIdentity = ObjectIdentity
dfl800UserAuth = _Dfl800UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6)
)
_Dfl800UserAuthHTTPUsers_Type = Gauge32
_Dfl800UserAuthHTTPUsers_Object = MibScalar
dfl800UserAuthHTTPUsers = _Dfl800UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 1),
    _Dfl800UserAuthHTTPUsers_Type()
)
dfl800UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthHTTPUsers.setStatus("current")
_Dfl800UserAuthXAUTHUsers_Type = Gauge32
_Dfl800UserAuthXAUTHUsers_Object = MibScalar
dfl800UserAuthXAUTHUsers = _Dfl800UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 2),
    _Dfl800UserAuthXAUTHUsers_Type()
)
dfl800UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthXAUTHUsers.setStatus("current")
_Dfl800UserAuthHTTPSUsers_Type = Gauge32
_Dfl800UserAuthHTTPSUsers_Object = MibScalar
dfl800UserAuthHTTPSUsers = _Dfl800UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 3),
    _Dfl800UserAuthHTTPSUsers_Type()
)
dfl800UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthHTTPSUsers.setStatus("current")
_Dfl800UserAuthPPPUsers_Type = Gauge32
_Dfl800UserAuthPPPUsers_Object = MibScalar
dfl800UserAuthPPPUsers = _Dfl800UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 4),
    _Dfl800UserAuthPPPUsers_Type()
)
dfl800UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthPPPUsers.setStatus("current")
_Dfl800UserAuthEAPUsers_Type = Gauge32
_Dfl800UserAuthEAPUsers_Object = MibScalar
dfl800UserAuthEAPUsers = _Dfl800UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 5),
    _Dfl800UserAuthEAPUsers_Type()
)
dfl800UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthEAPUsers.setStatus("current")
_Dfl800UserAuthRuleUseTable_Object = MibTable
dfl800UserAuthRuleUseTable = _Dfl800UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl800UserAuthRuleUseTable.setStatus("current")
_Dfl800UserAuthRuleUseEntry_Object = MibTableRow
dfl800UserAuthRuleUseEntry = _Dfl800UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 6, 1)
)
dfl800UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl800UserAuthRuleUseEntry.setStatus("current")


class _Dfl800UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl800UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl800UserAuthRuleIndex_Object = MibTableColumn
dfl800UserAuthRuleIndex = _Dfl800UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 6, 1, 1),
    _Dfl800UserAuthRuleIndex_Type()
)
dfl800UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800UserAuthRuleIndex.setStatus("current")
_Dfl800UserAuthRuleName_Type = DisplayString
_Dfl800UserAuthRuleName_Object = MibTableColumn
dfl800UserAuthRuleName = _Dfl800UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 6, 1, 2),
    _Dfl800UserAuthRuleName_Type()
)
dfl800UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthRuleName.setStatus("current")
_Dfl800UserAuthRuleUse_Type = Counter32
_Dfl800UserAuthRuleUse_Object = MibTableColumn
dfl800UserAuthRuleUse = _Dfl800UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 6, 6, 1, 3),
    _Dfl800UserAuthRuleUse_Type()
)
dfl800UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800UserAuthRuleUse.setStatus("current")
_Dfl800LinkMonitor_ObjectIdentity = ObjectIdentity
dfl800LinkMonitor = _Dfl800LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7)
)
_Dfl800LinkMonGrp_Type = Integer32
_Dfl800LinkMonGrp_Object = MibScalar
dfl800LinkMonGrp = _Dfl800LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 1),
    _Dfl800LinkMonGrp_Type()
)
dfl800LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800LinkMonGrp.setStatus("current")
_Dfl800LinkMonGrpTable_Object = MibTable
dfl800LinkMonGrpTable = _Dfl800LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl800LinkMonGrpTable.setStatus("current")
_Dfl800LinkMonGrpEntry_Object = MibTableRow
dfl800LinkMonGrpEntry = _Dfl800LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 2, 1)
)
dfl800LinkMonGrpEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl800LinkMonGrpEntry.setStatus("current")


class _Dfl800LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl800LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl800LinkMonGrpIndex_Object = MibTableColumn
dfl800LinkMonGrpIndex = _Dfl800LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 2, 1, 1),
    _Dfl800LinkMonGrpIndex_Type()
)
dfl800LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800LinkMonGrpIndex.setStatus("current")
_Dfl800LinkMonGrpName_Type = DisplayString
_Dfl800LinkMonGrpName_Object = MibTableColumn
dfl800LinkMonGrpName = _Dfl800LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 2, 1, 2),
    _Dfl800LinkMonGrpName_Type()
)
dfl800LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800LinkMonGrpName.setStatus("current")
_Dfl800LinkMonGrpHostsUp_Type = Gauge32
_Dfl800LinkMonGrpHostsUp_Object = MibTableColumn
dfl800LinkMonGrpHostsUp = _Dfl800LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 2, 1, 3),
    _Dfl800LinkMonGrpHostsUp_Type()
)
dfl800LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800LinkMonGrpHostsUp.setStatus("current")
_Dfl800LinkMonHostTable_Object = MibTable
dfl800LinkMonHostTable = _Dfl800LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl800LinkMonHostTable.setStatus("current")
_Dfl800LinkMonHostEntry_Object = MibTableRow
dfl800LinkMonHostEntry = _Dfl800LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 3, 1)
)
dfl800LinkMonHostEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800LinkMonGrpIndex"),
    (0, "DFL800-MIB", "dfl800LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl800LinkMonHostEntry.setStatus("current")


class _Dfl800LinkMonHostIndex_Type(Integer32):
    """Custom type dfl800LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl800LinkMonHostIndex_Object = MibTableColumn
dfl800LinkMonHostIndex = _Dfl800LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 3, 1, 1),
    _Dfl800LinkMonHostIndex_Type()
)
dfl800LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800LinkMonHostIndex.setStatus("current")
_Dfl800LinkMonHostId_Type = DisplayString
_Dfl800LinkMonHostId_Object = MibTableColumn
dfl800LinkMonHostId = _Dfl800LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 3, 1, 2),
    _Dfl800LinkMonHostId_Type()
)
dfl800LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800LinkMonHostId.setStatus("current")
_Dfl800LinkMonHostShortTermLoss_Type = Gauge32
_Dfl800LinkMonHostShortTermLoss_Object = MibTableColumn
dfl800LinkMonHostShortTermLoss = _Dfl800LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 3, 1, 3),
    _Dfl800LinkMonHostShortTermLoss_Type()
)
dfl800LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800LinkMonHostShortTermLoss.setStatus("current")
_Dfl800LinkMonHostPacketsLost_Type = Counter32
_Dfl800LinkMonHostPacketsLost_Object = MibTableColumn
dfl800LinkMonHostPacketsLost = _Dfl800LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 7, 3, 1, 4),
    _Dfl800LinkMonHostPacketsLost_Type()
)
dfl800LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800LinkMonHostPacketsLost.setStatus("current")
_Dfl800Pipes_ObjectIdentity = ObjectIdentity
dfl800Pipes = _Dfl800Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8)
)
_Dfl800PipeUsers_Type = Gauge32
_Dfl800PipeUsers_Object = MibScalar
dfl800PipeUsers = _Dfl800PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 1),
    _Dfl800PipeUsers_Type()
)
dfl800PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeUsers.setStatus("current")
_Dfl800PipeTable_Object = MibTable
dfl800PipeTable = _Dfl800PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl800PipeTable.setStatus("current")
_Dfl800PipeEntry_Object = MibTableRow
dfl800PipeEntry = _Dfl800PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1)
)
dfl800PipeEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl800PipeEntry.setStatus("current")


class _Dfl800PipeIndex_Type(Integer32):
    """Custom type dfl800PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800PipeIndex_Type.__name__ = "Integer32"
_Dfl800PipeIndex_Object = MibTableColumn
dfl800PipeIndex = _Dfl800PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 1),
    _Dfl800PipeIndex_Type()
)
dfl800PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800PipeIndex.setStatus("current")
_Dfl800PipeName_Type = DisplayString
_Dfl800PipeName_Object = MibTableColumn
dfl800PipeName = _Dfl800PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 2),
    _Dfl800PipeName_Type()
)
dfl800PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeName.setStatus("current")
_Dfl800PipeMinPrec_Type = Integer32
_Dfl800PipeMinPrec_Object = MibTableColumn
dfl800PipeMinPrec = _Dfl800PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 3),
    _Dfl800PipeMinPrec_Type()
)
dfl800PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeMinPrec.setStatus("current")
_Dfl800PipeMaxPrec_Type = Integer32
_Dfl800PipeMaxPrec_Object = MibTableColumn
dfl800PipeMaxPrec = _Dfl800PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 4),
    _Dfl800PipeMaxPrec_Type()
)
dfl800PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeMaxPrec.setStatus("current")
_Dfl800PipeDefPrec_Type = Integer32
_Dfl800PipeDefPrec_Object = MibTableColumn
dfl800PipeDefPrec = _Dfl800PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 5),
    _Dfl800PipeDefPrec_Type()
)
dfl800PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeDefPrec.setStatus("current")
_Dfl800PipeNumPrec_Type = Integer32
_Dfl800PipeNumPrec_Object = MibTableColumn
dfl800PipeNumPrec = _Dfl800PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 6),
    _Dfl800PipeNumPrec_Type()
)
dfl800PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeNumPrec.setStatus("current")
_Dfl800PipeNumUsers_Type = Gauge32
_Dfl800PipeNumUsers_Object = MibTableColumn
dfl800PipeNumUsers = _Dfl800PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 7),
    _Dfl800PipeNumUsers_Type()
)
dfl800PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeNumUsers.setStatus("current")
_Dfl800PipeCurrentBps_Type = Gauge32
_Dfl800PipeCurrentBps_Object = MibTableColumn
dfl800PipeCurrentBps = _Dfl800PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 8),
    _Dfl800PipeCurrentBps_Type()
)
dfl800PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeCurrentBps.setStatus("current")
_Dfl800PipeCurrentPps_Type = Gauge32
_Dfl800PipeCurrentPps_Object = MibTableColumn
dfl800PipeCurrentPps = _Dfl800PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 9),
    _Dfl800PipeCurrentPps_Type()
)
dfl800PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeCurrentPps.setStatus("current")
_Dfl800PipeDelayedPackets_Type = Counter32
_Dfl800PipeDelayedPackets_Object = MibTableColumn
dfl800PipeDelayedPackets = _Dfl800PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 10),
    _Dfl800PipeDelayedPackets_Type()
)
dfl800PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeDelayedPackets.setStatus("current")
_Dfl800PipeDropedPackets_Type = Counter32
_Dfl800PipeDropedPackets_Object = MibTableColumn
dfl800PipeDropedPackets = _Dfl800PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 2, 1, 11),
    _Dfl800PipeDropedPackets_Type()
)
dfl800PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipeDropedPackets.setStatus("current")
_Dfl800PipePrecTable_Object = MibTable
dfl800PipePrecTable = _Dfl800PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl800PipePrecTable.setStatus("current")
_Dfl800PipePrecEntry_Object = MibTableRow
dfl800PipePrecEntry = _Dfl800PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1)
)
dfl800PipePrecEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800PipeIndex"),
    (0, "DFL800-MIB", "dfl800PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl800PipePrecEntry.setStatus("current")


class _Dfl800PipePrecIndex_Type(Integer32):
    """Custom type dfl800PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800PipePrecIndex_Type.__name__ = "Integer32"
_Dfl800PipePrecIndex_Object = MibTableColumn
dfl800PipePrecIndex = _Dfl800PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 1),
    _Dfl800PipePrecIndex_Type()
)
dfl800PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800PipePrecIndex.setStatus("current")
_Dfl800PipePrec_Type = Integer32
_Dfl800PipePrec_Object = MibTableColumn
dfl800PipePrec = _Dfl800PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 2),
    _Dfl800PipePrec_Type()
)
dfl800PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrec.setStatus("current")
_Dfl800PipePrecBps_Type = Gauge32
_Dfl800PipePrecBps_Object = MibTableColumn
dfl800PipePrecBps = _Dfl800PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 3),
    _Dfl800PipePrecBps_Type()
)
dfl800PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecBps.setStatus("current")
_Dfl800PipePrecTotalPps_Type = Gauge32
_Dfl800PipePrecTotalPps_Object = MibTableColumn
dfl800PipePrecTotalPps = _Dfl800PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 4),
    _Dfl800PipePrecTotalPps_Type()
)
dfl800PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecTotalPps.setStatus("current")
_Dfl800PipePrecReservedBps_Type = Gauge32
_Dfl800PipePrecReservedBps_Object = MibTableColumn
dfl800PipePrecReservedBps = _Dfl800PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 5),
    _Dfl800PipePrecReservedBps_Type()
)
dfl800PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecReservedBps.setStatus("current")
_Dfl800PipePrecDynLimBps_Type = Gauge32
_Dfl800PipePrecDynLimBps_Object = MibTableColumn
dfl800PipePrecDynLimBps = _Dfl800PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 6),
    _Dfl800PipePrecDynLimBps_Type()
)
dfl800PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecDynLimBps.setStatus("current")
_Dfl800PipePrecDynUsrLimBps_Type = Gauge32
_Dfl800PipePrecDynUsrLimBps_Object = MibTableColumn
dfl800PipePrecDynUsrLimBps = _Dfl800PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 7),
    _Dfl800PipePrecDynUsrLimBps_Type()
)
dfl800PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecDynUsrLimBps.setStatus("current")
_Dfl800PipePrecDelayedPackets_Type = Counter32
_Dfl800PipePrecDelayedPackets_Object = MibTableColumn
dfl800PipePrecDelayedPackets = _Dfl800PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 8),
    _Dfl800PipePrecDelayedPackets_Type()
)
dfl800PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecDelayedPackets.setStatus("current")
_Dfl800PipePrecDropedPackets_Type = Counter32
_Dfl800PipePrecDropedPackets_Object = MibTableColumn
dfl800PipePrecDropedPackets = _Dfl800PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 8, 3, 1, 9),
    _Dfl800PipePrecDropedPackets_Type()
)
dfl800PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800PipePrecDropedPackets.setStatus("current")
_Dfl800ALG_ObjectIdentity = ObjectIdentity
dfl800ALG = _Dfl800ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9)
)
_Dfl800AlgSessions_Type = Gauge32
_Dfl800AlgSessions_Object = MibScalar
dfl800AlgSessions = _Dfl800AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 1),
    _Dfl800AlgSessions_Type()
)
dfl800AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800AlgSessions.setStatus("current")
_Dfl800AlgConnections_Type = Gauge32
_Dfl800AlgConnections_Object = MibScalar
dfl800AlgConnections = _Dfl800AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 2),
    _Dfl800AlgConnections_Type()
)
dfl800AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800AlgConnections.setStatus("current")
_Dfl800AlgTCPStreams_Type = Gauge32
_Dfl800AlgTCPStreams_Object = MibScalar
dfl800AlgTCPStreams = _Dfl800AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 3),
    _Dfl800AlgTCPStreams_Type()
)
dfl800AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800AlgTCPStreams.setStatus("current")
_Dfl800HttpAlg_ObjectIdentity = ObjectIdentity
dfl800HttpAlg = _Dfl800HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4)
)
_Dfl800HttpAlgTable_Object = MibTable
dfl800HttpAlgTable = _Dfl800HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl800HttpAlgTable.setStatus("current")
_Dfl800HttpAlgEntry_Object = MibTableRow
dfl800HttpAlgEntry = _Dfl800HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1, 1)
)
dfl800HttpAlgEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl800HttpAlgEntry.setStatus("current")


class _Dfl800HttpAlgIndex_Type(Integer32):
    """Custom type dfl800HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl800HttpAlgIndex_Object = MibTableColumn
dfl800HttpAlgIndex = _Dfl800HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1, 1, 1),
    _Dfl800HttpAlgIndex_Type()
)
dfl800HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800HttpAlgIndex.setStatus("current")
_Dfl800HttpAlgName_Type = DisplayString
_Dfl800HttpAlgName_Object = MibTableColumn
dfl800HttpAlgName = _Dfl800HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1, 1, 2),
    _Dfl800HttpAlgName_Type()
)
dfl800HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgName.setStatus("current")
_Dfl800HttpAlgTotalRequested_Type = Gauge32
_Dfl800HttpAlgTotalRequested_Object = MibTableColumn
dfl800HttpAlgTotalRequested = _Dfl800HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1, 1, 3),
    _Dfl800HttpAlgTotalRequested_Type()
)
dfl800HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgTotalRequested.setStatus("current")
_Dfl800HttpAlgTotalAllowed_Type = Gauge32
_Dfl800HttpAlgTotalAllowed_Object = MibTableColumn
dfl800HttpAlgTotalAllowed = _Dfl800HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1, 1, 4),
    _Dfl800HttpAlgTotalAllowed_Type()
)
dfl800HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgTotalAllowed.setStatus("current")
_Dfl800HttpAlgTotalBlocked_Type = Gauge32
_Dfl800HttpAlgTotalBlocked_Object = MibTableColumn
dfl800HttpAlgTotalBlocked = _Dfl800HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 1, 1, 5),
    _Dfl800HttpAlgTotalBlocked_Type()
)
dfl800HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgTotalBlocked.setStatus("current")
_Dfl800HttpAlgCntFltTable_Object = MibTable
dfl800HttpAlgCntFltTable = _Dfl800HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltTable.setStatus("current")
_Dfl800HttpAlgCntFltEntry_Object = MibTableRow
dfl800HttpAlgCntFltEntry = _Dfl800HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2, 1)
)
dfl800HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800HttpAlgIndex"),
    (0, "DFL800-MIB", "dfl800HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltEntry.setStatus("current")


class _Dfl800HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl800HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl800HttpAlgCntFltIndex_Object = MibTableColumn
dfl800HttpAlgCntFltIndex = _Dfl800HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2, 1, 1),
    _Dfl800HttpAlgCntFltIndex_Type()
)
dfl800HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltIndex.setStatus("current")
_Dfl800HttpAlgCntFltName_Type = DisplayString
_Dfl800HttpAlgCntFltName_Object = MibTableColumn
dfl800HttpAlgCntFltName = _Dfl800HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2, 1, 2),
    _Dfl800HttpAlgCntFltName_Type()
)
dfl800HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltName.setStatus("current")
_Dfl800HttpAlgCntFltRequests_Type = Gauge32
_Dfl800HttpAlgCntFltRequests_Object = MibTableColumn
dfl800HttpAlgCntFltRequests = _Dfl800HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2, 1, 3),
    _Dfl800HttpAlgCntFltRequests_Type()
)
dfl800HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltRequests.setStatus("current")
_Dfl800HttpAlgCntFltAllowed_Type = Gauge32
_Dfl800HttpAlgCntFltAllowed_Object = MibTableColumn
dfl800HttpAlgCntFltAllowed = _Dfl800HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2, 1, 4),
    _Dfl800HttpAlgCntFltAllowed_Type()
)
dfl800HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltAllowed.setStatus("current")
_Dfl800HttpAlgCntFltBlocked_Type = Gauge32
_Dfl800HttpAlgCntFltBlocked_Object = MibTableColumn
dfl800HttpAlgCntFltBlocked = _Dfl800HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 4, 2, 1, 5),
    _Dfl800HttpAlgCntFltBlocked_Type()
)
dfl800HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HttpAlgCntFltBlocked.setStatus("current")
_Dfl800SmtpAlg_ObjectIdentity = ObjectIdentity
dfl800SmtpAlg = _Dfl800SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5)
)
_Dfl800SmtpAlgTable_Object = MibTable
dfl800SmtpAlgTable = _Dfl800SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl800SmtpAlgTable.setStatus("current")
_Dfl800SmtpAlgEntry_Object = MibTableRow
dfl800SmtpAlgEntry = _Dfl800SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1, 1)
)
dfl800SmtpAlgEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl800SmtpAlgEntry.setStatus("current")


class _Dfl800SmtpAlgIndex_Type(Integer32):
    """Custom type dfl800SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl800SmtpAlgIndex_Object = MibTableColumn
dfl800SmtpAlgIndex = _Dfl800SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1, 1, 1),
    _Dfl800SmtpAlgIndex_Type()
)
dfl800SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800SmtpAlgIndex.setStatus("current")
_Dfl800SmtpAlgName_Type = DisplayString
_Dfl800SmtpAlgName_Object = MibTableColumn
dfl800SmtpAlgName = _Dfl800SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1, 1, 2),
    _Dfl800SmtpAlgName_Type()
)
dfl800SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgName.setStatus("current")
_Dfl800SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl800SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl800SmtpAlgTotCheckedSes = _Dfl800SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1, 1, 3),
    _Dfl800SmtpAlgTotCheckedSes_Type()
)
dfl800SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgTotCheckedSes.setStatus("current")
_Dfl800SmtpAlgTotSpamSes_Type = Gauge32
_Dfl800SmtpAlgTotSpamSes_Object = MibTableColumn
dfl800SmtpAlgTotSpamSes = _Dfl800SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1, 1, 4),
    _Dfl800SmtpAlgTotSpamSes_Type()
)
dfl800SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgTotSpamSes.setStatus("current")
_Dfl800SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl800SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl800SmtpAlgTotDroppedSes = _Dfl800SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 1, 1, 5),
    _Dfl800SmtpAlgTotDroppedSes_Type()
)
dfl800SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgTotDroppedSes.setStatus("current")
_Dfl800SmtpAlgDnsBlTable_Object = MibTable
dfl800SmtpAlgDnsBlTable = _Dfl800SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlTable.setStatus("current")
_Dfl800SmtpAlgDnsBlEntry_Object = MibTableRow
dfl800SmtpAlgDnsBlEntry = _Dfl800SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2, 1)
)
dfl800SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800SmtpAlgIndex"),
    (0, "DFL800-MIB", "dfl800SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl800SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl800SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl800SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl800SmtpAlgDnsBlIndex = _Dfl800SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2, 1, 1),
    _Dfl800SmtpAlgDnsBlIndex_Type()
)
dfl800SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlIndex.setStatus("current")
_Dfl800SmtpAlgDnsBlName_Type = DisplayString
_Dfl800SmtpAlgDnsBlName_Object = MibTableColumn
dfl800SmtpAlgDnsBlName = _Dfl800SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2, 1, 2),
    _Dfl800SmtpAlgDnsBlName_Type()
)
dfl800SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlName.setStatus("current")
_Dfl800SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl800SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl800SmtpAlgDnsBlChecked = _Dfl800SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2, 1, 3),
    _Dfl800SmtpAlgDnsBlChecked_Type()
)
dfl800SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlChecked.setStatus("current")
_Dfl800SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl800SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl800SmtpAlgDnsBlMatched = _Dfl800SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2, 1, 4),
    _Dfl800SmtpAlgDnsBlMatched_Type()
)
dfl800SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlMatched.setStatus("current")
_Dfl800SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl800SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl800SmtpAlgDnsBlFailChecks = _Dfl800SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 9, 5, 2, 1, 5),
    _Dfl800SmtpAlgDnsBlFailChecks_Type()
)
dfl800SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl800DHCPRelay_ObjectIdentity = ObjectIdentity
dfl800DHCPRelay = _Dfl800DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11)
)
_Dfl800DHCPRelayCurClients_Type = Gauge32
_Dfl800DHCPRelayCurClients_Object = MibScalar
dfl800DHCPRelayCurClients = _Dfl800DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 1),
    _Dfl800DHCPRelayCurClients_Type()
)
dfl800DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayCurClients.setStatus("current")
_Dfl800DHCPRelayCurTrans_Type = Gauge32
_Dfl800DHCPRelayCurTrans_Object = MibScalar
dfl800DHCPRelayCurTrans = _Dfl800DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 2),
    _Dfl800DHCPRelayCurTrans_Type()
)
dfl800DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayCurTrans.setStatus("current")
_Dfl800DHCPRelayRejected_Type = Gauge32
_Dfl800DHCPRelayRejected_Object = MibScalar
dfl800DHCPRelayRejected = _Dfl800DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 3),
    _Dfl800DHCPRelayRejected_Type()
)
dfl800DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRejected.setStatus("current")
_Dfl800DHCPRelayRuleTable_Object = MibTable
dfl800DHCPRelayRuleTable = _Dfl800DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleTable.setStatus("current")
_Dfl800DHCPRelayRuleEntry_Object = MibTableRow
dfl800DHCPRelayRuleEntry = _Dfl800DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1)
)
dfl800DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL800-MIB", "dfl800DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleEntry.setStatus("current")


class _Dfl800DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl800DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl800DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl800DHCPRelayRuleIndex_Object = MibTableColumn
dfl800DHCPRelayRuleIndex = _Dfl800DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1, 1),
    _Dfl800DHCPRelayRuleIndex_Type()
)
dfl800DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleIndex.setStatus("current")
_Dfl800DHCPRelayRuleName_Type = DisplayString
_Dfl800DHCPRelayRuleName_Object = MibTableColumn
dfl800DHCPRelayRuleName = _Dfl800DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1, 2),
    _Dfl800DHCPRelayRuleName_Type()
)
dfl800DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleName.setStatus("current")
_Dfl800DHCPRelayRuleHits_Type = Gauge32
_Dfl800DHCPRelayRuleHits_Object = MibTableColumn
dfl800DHCPRelayRuleHits = _Dfl800DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1, 3),
    _Dfl800DHCPRelayRuleHits_Type()
)
dfl800DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleHits.setStatus("current")
_Dfl800DHCPRelayRuleCurClients_Type = Gauge32
_Dfl800DHCPRelayRuleCurClients_Object = MibTableColumn
dfl800DHCPRelayRuleCurClients = _Dfl800DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1, 4),
    _Dfl800DHCPRelayRuleCurClients_Type()
)
dfl800DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleCurClients.setStatus("current")
_Dfl800DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl800DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl800DHCPRelayRuleRejCliPkts = _Dfl800DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1, 5),
    _Dfl800DHCPRelayRuleRejCliPkts_Type()
)
dfl800DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl800DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl800DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl800DHCPRelayRuleRejSrvPkts = _Dfl800DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 11, 4, 1, 6),
    _Dfl800DHCPRelayRuleRejSrvPkts_Type()
)
dfl800DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl800HA_ObjectIdentity = ObjectIdentity
dfl800HA = _Dfl800HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 12)
)
_Dfl800HASyncSendQueueLength_Type = Gauge32
_Dfl800HASyncSendQueueLength_Object = MibScalar
dfl800HASyncSendQueueLength = _Dfl800HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 12, 1),
    _Dfl800HASyncSendQueueLength_Type()
)
dfl800HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HASyncSendQueueLength.setStatus("current")
_Dfl800HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl800HASyncSendQueueUsagePkt_Object = MibScalar
dfl800HASyncSendQueueUsagePkt = _Dfl800HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 12, 2),
    _Dfl800HASyncSendQueueUsagePkt_Type()
)
dfl800HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HASyncSendQueueUsagePkt.setStatus("current")
_Dfl800HASyncSendQueueUsageOct_Type = Gauge32
_Dfl800HASyncSendQueueUsageOct_Object = MibScalar
dfl800HASyncSendQueueUsageOct = _Dfl800HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 12, 3),
    _Dfl800HASyncSendQueueUsageOct_Type()
)
dfl800HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HASyncSendQueueUsageOct.setStatus("current")
_Dfl800HASyncSentPackets_Type = Counter32
_Dfl800HASyncSentPackets_Object = MibScalar
dfl800HASyncSentPackets = _Dfl800HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 12, 4),
    _Dfl800HASyncSentPackets_Type()
)
dfl800HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HASyncSentPackets.setStatus("current")
_Dfl800HASyncSendResentPackets_Type = Counter32
_Dfl800HASyncSendResentPackets_Object = MibScalar
dfl800HASyncSendResentPackets = _Dfl800HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 1, 2, 12, 5),
    _Dfl800HASyncSendResentPackets_Type()
)
dfl800HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl800HASyncSendResentPackets.setStatus("current")
_Dfl800reg_ObjectIdentity = ObjectIdentity
dfl800reg = _Dfl800reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2)
)
_Dfl800MibModules_ObjectIdentity = ObjectIdentity
dfl800MibModules = _Dfl800MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 1)
)
_Dfl800MibConfs_ObjectIdentity = ObjectIdentity
dfl800MibConfs = _Dfl800MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 2)
)
_Dfl800StatsConformance_ObjectIdentity = ObjectIdentity
dfl800StatsConformance = _Dfl800StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 2, 1)
)
_Dfl800MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl800MibObjectGroups = _Dfl800MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3)
)
_Dfl800StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl800StatsRegGroups = _Dfl800StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1)
)

# Managed Objects groups

dfl800SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 1)
)
dfl800SystemObjectGroup.setObjects(
      *(("DFL800-MIB", "dfl800SysCpuLoad"),
        ("DFL800-MIB", "dfl800SysForwardedBits"),
        ("DFL800-MIB", "dfl800SysForwardedPackets"),
        ("DFL800-MIB", "dfl800SysBuffUse"),
        ("DFL800-MIB", "dfl800SysConns"),
        ("DFL800-MIB", "dfl800HWSensorName"),
        ("DFL800-MIB", "dfl800HWSensorValue"),
        ("DFL800-MIB", "dfl800HWSensorUnit"),
        ("DFL800-MIB", "dfl800SysMemUsage"),
        ("DFL800-MIB", "dfl800SysTimerUsage"),
        ("DFL800-MIB", "dfl800SysConnOPS"),
        ("DFL800-MIB", "dfl800SysConnCPS"),
        ("DFL800-MIB", "dfl800SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl800SystemObjectGroup.setStatus("current")

dfl800IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 2)
)
dfl800IPsecObjectGroup.setObjects(
      *(("DFL800-MIB", "dfl800IPsecPhaseOneActive"),
        ("DFL800-MIB", "dfl800IPsecPhaseOneAggrModeDone"),
        ("DFL800-MIB", "dfl800IPsecQuickModeActive"),
        ("DFL800-MIB", "dfl800IPsecPhaseOneDone"),
        ("DFL800-MIB", "dfl800IPsecPhaseOneFailed"),
        ("DFL800-MIB", "dfl800IPsecPhaseOneRekeyed"),
        ("DFL800-MIB", "dfl800IPsecQuickModeDone"),
        ("DFL800-MIB", "dfl800IPsecQuickModeFailed"),
        ("DFL800-MIB", "dfl800IPsecInfoDone"),
        ("DFL800-MIB", "dfl800IPsecInfoFailed"),
        ("DFL800-MIB", "dfl800IPsecInOctetsComp"),
        ("DFL800-MIB", "dfl800IPsecInOctetsUncomp"),
        ("DFL800-MIB", "dfl800IPsecOutOctetsComp"),
        ("DFL800-MIB", "dfl800IPsecOutOctetsUncomp"),
        ("DFL800-MIB", "dfl800IPsecForwardedOctetsComp"),
        ("DFL800-MIB", "dfl800IPsecForwardedOctetsUcomp"),
        ("DFL800-MIB", "dfl800IPsecInPackets"),
        ("DFL800-MIB", "dfl800IPsecOutPackets"),
        ("DFL800-MIB", "dfl800IPsecForwardedPackets"),
        ("DFL800-MIB", "dfl800IPsecActiveTransforms"),
        ("DFL800-MIB", "dfl800IPsecTotalTransforms"),
        ("DFL800-MIB", "dfl800IPsecOutOfTransforms"),
        ("DFL800-MIB", "dfl800IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl800IPsecObjectGroup.setStatus("current")

dfl800StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 3)
)
dfl800StateCountersGroup.setObjects(
      *(("DFL800-MIB", "dfl800SysPscTcpSyn"),
        ("DFL800-MIB", "dfl800SysPscTcpOpen"),
        ("DFL800-MIB", "dfl800SysPscTcpFin"),
        ("DFL800-MIB", "dfl800SysPscUdp"),
        ("DFL800-MIB", "dfl800SysPscIcmp"),
        ("DFL800-MIB", "dfl800SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl800StateCountersGroup.setStatus("current")

dfl800IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 4)
)
dfl800IPPoolGroup.setObjects(
      *(("DFL800-MIB", "dfl800IPPoolsNumber"),
        ("DFL800-MIB", "dfl800IPPoolName"),
        ("DFL800-MIB", "dfl800IPPoolPrepare"),
        ("DFL800-MIB", "dfl800IPPoolFree"),
        ("DFL800-MIB", "dfl800IPPoolMisses"),
        ("DFL800-MIB", "dfl800IPPoolClientFails"),
        ("DFL800-MIB", "dfl800IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl800IPPoolGroup.setStatus("current")

dfl800DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 5)
)
dfl800DHCPServerGroup.setObjects(
      *(("DFL800-MIB", "dfl800DHCPTotalRejected"),
        ("DFL800-MIB", "dfl800DHCPRuleName"),
        ("DFL800-MIB", "dfl800DHCPRuleUsage"),
        ("DFL800-MIB", "dfl800DHCPRuleUsagePercent"),
        ("DFL800-MIB", "dfl800DHCPActiveClients"),
        ("DFL800-MIB", "dfl800DHCPActiveClientsPercent"),
        ("DFL800-MIB", "dfl800DHCPRejectedRequests"),
        ("DFL800-MIB", "dfl800DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl800DHCPServerGroup.setStatus("current")

dfl800RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 6)
)
dfl800RuleUseGroup.setObjects(
      *(("DFL800-MIB", "dfl800RuleName"),
        ("DFL800-MIB", "dfl800RuleUse"))
)
if mibBuilder.loadTexts:
    dfl800RuleUseGroup.setStatus("current")

dfl800UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 7)
)
dfl800UserAuthGroup.setObjects(
      *(("DFL800-MIB", "dfl800UserAuthHTTPUsers"),
        ("DFL800-MIB", "dfl800UserAuthXAUTHUsers"),
        ("DFL800-MIB", "dfl800UserAuthHTTPSUsers"),
        ("DFL800-MIB", "dfl800UserAuthPPPUsers"),
        ("DFL800-MIB", "dfl800UserAuthEAPUsers"),
        ("DFL800-MIB", "dfl800UserAuthRuleName"),
        ("DFL800-MIB", "dfl800UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl800UserAuthGroup.setStatus("current")

dfl800IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 8)
)
dfl800IfStatsGroup.setObjects(
      *(("DFL800-MIB", "dfl800IfName"),
        ("DFL800-MIB", "dfl800IfFragsIn"),
        ("DFL800-MIB", "dfl800IfFragReassOk"),
        ("DFL800-MIB", "dfl800IfFragReassFail"),
        ("DFL800-MIB", "dfl800IfPktsInCnt"),
        ("DFL800-MIB", "dfl800IfPktsOutCnt"),
        ("DFL800-MIB", "dfl800IfBitsInCnt"),
        ("DFL800-MIB", "dfl800IfBitsOutCnt"),
        ("DFL800-MIB", "dfl800IfPktsTotCnt"),
        ("DFL800-MIB", "dfl800IfBitsTotCnt"),
        ("DFL800-MIB", "dfl800IfHCPktsInCnt"),
        ("DFL800-MIB", "dfl800IfHCPktsOutCnt"),
        ("DFL800-MIB", "dfl800IfHCBitsInCnt"),
        ("DFL800-MIB", "dfl800IfHCBitsOutCnt"),
        ("DFL800-MIB", "dfl800IfHCPktsTotCnt"),
        ("DFL800-MIB", "dfl800IfHCBitsTotCnt"),
        ("DFL800-MIB", "dfl800IfRxRingFifoErrors"),
        ("DFL800-MIB", "dfl800IfRxDespools"),
        ("DFL800-MIB", "dfl800IfRxAvgUse"),
        ("DFL800-MIB", "dfl800IfRxRingSaturation"),
        ("DFL800-MIB", "dfl800RxRingFlooded"),
        ("DFL800-MIB", "dfl800IfTxDespools"),
        ("DFL800-MIB", "dfl800IfTxAvgUse"),
        ("DFL800-MIB", "dfl800IfTxRingSaturation"),
        ("DFL800-MIB", "dfl800RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl800IfStatsGroup.setStatus("current")

dfl800LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 9)
)
dfl800LinkMonitorGroup.setObjects(
      *(("DFL800-MIB", "dfl800LinkMonGrp"),
        ("DFL800-MIB", "dfl800LinkMonGrpName"),
        ("DFL800-MIB", "dfl800LinkMonGrpHostsUp"),
        ("DFL800-MIB", "dfl800LinkMonHostId"),
        ("DFL800-MIB", "dfl800LinkMonHostShortTermLoss"),
        ("DFL800-MIB", "dfl800LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl800LinkMonitorGroup.setStatus("current")

dfl800PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 10)
)
dfl800PipesObjectGroup.setObjects(
      *(("DFL800-MIB", "dfl800PipeUsers"),
        ("DFL800-MIB", "dfl800PipeName"),
        ("DFL800-MIB", "dfl800PipeMinPrec"),
        ("DFL800-MIB", "dfl800PipeMaxPrec"),
        ("DFL800-MIB", "dfl800PipeDefPrec"),
        ("DFL800-MIB", "dfl800PipeNumPrec"),
        ("DFL800-MIB", "dfl800PipeNumUsers"),
        ("DFL800-MIB", "dfl800PipeCurrentBps"),
        ("DFL800-MIB", "dfl800PipeCurrentPps"),
        ("DFL800-MIB", "dfl800PipeDelayedPackets"),
        ("DFL800-MIB", "dfl800PipeDropedPackets"),
        ("DFL800-MIB", "dfl800PipePrec"),
        ("DFL800-MIB", "dfl800PipePrecBps"),
        ("DFL800-MIB", "dfl800PipePrecTotalPps"),
        ("DFL800-MIB", "dfl800PipePrecReservedBps"),
        ("DFL800-MIB", "dfl800PipePrecDynLimBps"),
        ("DFL800-MIB", "dfl800PipePrecDynUsrLimBps"),
        ("DFL800-MIB", "dfl800PipePrecDelayedPackets"),
        ("DFL800-MIB", "dfl800PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl800PipesObjectGroup.setStatus("current")

dfl800DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 12)
)
dfl800DHCPRelayObjectGroup.setObjects(
      *(("DFL800-MIB", "dfl800DHCPRelayCurClients"),
        ("DFL800-MIB", "dfl800DHCPRelayCurTrans"),
        ("DFL800-MIB", "dfl800DHCPRelayRejected"),
        ("DFL800-MIB", "dfl800DHCPRelayRuleName"),
        ("DFL800-MIB", "dfl800DHCPRelayRuleHits"),
        ("DFL800-MIB", "dfl800DHCPRelayRuleCurClients"),
        ("DFL800-MIB", "dfl800DHCPRelayRuleRejCliPkts"),
        ("DFL800-MIB", "dfl800DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl800DHCPRelayObjectGroup.setStatus("current")

dfl800AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 13)
)
dfl800AlgGroup.setObjects(
      *(("DFL800-MIB", "dfl800AlgSessions"),
        ("DFL800-MIB", "dfl800AlgConnections"),
        ("DFL800-MIB", "dfl800AlgTCPStreams"),
        ("DFL800-MIB", "dfl800HttpAlgName"),
        ("DFL800-MIB", "dfl800HttpAlgTotalRequested"),
        ("DFL800-MIB", "dfl800HttpAlgTotalAllowed"),
        ("DFL800-MIB", "dfl800HttpAlgTotalBlocked"),
        ("DFL800-MIB", "dfl800HttpAlgCntFltName"),
        ("DFL800-MIB", "dfl800HttpAlgCntFltRequests"),
        ("DFL800-MIB", "dfl800HttpAlgCntFltAllowed"),
        ("DFL800-MIB", "dfl800HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl800AlgGroup.setStatus("current")

dfl800HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 14)
)
dfl800HAGroup.setObjects(
      *(("DFL800-MIB", "dfl800HASyncSendQueueLength"),
        ("DFL800-MIB", "dfl800HASyncSendQueueUsagePkt"),
        ("DFL800-MIB", "dfl800HASyncSendQueueUsageOct"),
        ("DFL800-MIB", "dfl800HASyncSentPackets"),
        ("DFL800-MIB", "dfl800HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl800HAGroup.setStatus("current")

dfl800IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 15)
)
dfl800IfVlanGroup.setObjects(
      *(("DFL800-MIB", "dfl800IfVlanUntaggedInPkts"),
        ("DFL800-MIB", "dfl800IfVlanUntaggedOutPkts"),
        ("DFL800-MIB", "dfl800IfVlanUntaggedTotPkts"),
        ("DFL800-MIB", "dfl800IfVlanUntaggedInOctets"),
        ("DFL800-MIB", "dfl800IfVlanUntaggedOutOctets"),
        ("DFL800-MIB", "dfl800IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl800IfVlanGroup.setStatus("current")

dfl800SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 16)
)
dfl800SmtpAlgGroup.setObjects(
      *(("DFL800-MIB", "dfl800SmtpAlgName"),
        ("DFL800-MIB", "dfl800SmtpAlgTotCheckedSes"),
        ("DFL800-MIB", "dfl800SmtpAlgTotSpamSes"),
        ("DFL800-MIB", "dfl800SmtpAlgTotDroppedSes"),
        ("DFL800-MIB", "dfl800SmtpAlgDnsBlName"),
        ("DFL800-MIB", "dfl800SmtpAlgDnsBlChecked"),
        ("DFL800-MIB", "dfl800SmtpAlgDnsBlMatched"),
        ("DFL800-MIB", "dfl800SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl800SmtpAlgGroup.setStatus("current")

dfl800SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 3, 1, 17)
)
dfl800SysTCPGroup.setObjects(
      *(("DFL800-MIB", "dfl800SysTCPRecvSmall"),
        ("DFL800-MIB", "dfl800SysTCPRecvLarge"),
        ("DFL800-MIB", "dfl800SysTCPSendSmall"),
        ("DFL800-MIB", "dfl800SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl800SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl800StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl800StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL800-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "ipsFirewall": ipsFirewall,
       "dfl800": dfl800,
       "dfl800OS": dfl800OS,
       "dfl800OSStats": dfl800OSStats,
       "dfl800System": dfl800System,
       "dfl800SysCpuLoad": dfl800SysCpuLoad,
       "dfl800SysForwardedBits": dfl800SysForwardedBits,
       "dfl800SysForwardedPackets": dfl800SysForwardedPackets,
       "dfl800SysBuffUse": dfl800SysBuffUse,
       "dfl800SysConns": dfl800SysConns,
       "dfl800SysPerStateCounters": dfl800SysPerStateCounters,
       "dfl800SysPscTcpSyn": dfl800SysPscTcpSyn,
       "dfl800SysPscTcpOpen": dfl800SysPscTcpOpen,
       "dfl800SysPscTcpFin": dfl800SysPscTcpFin,
       "dfl800SysPscUdp": dfl800SysPscUdp,
       "dfl800SysPscIcmp": dfl800SysPscIcmp,
       "dfl800SysPscOther": dfl800SysPscOther,
       "dfl800IfStatsTable": dfl800IfStatsTable,
       "dfl800IfStatsEntry": dfl800IfStatsEntry,
       "dfl800IfStatsIndex": dfl800IfStatsIndex,
       "dfl800IfName": dfl800IfName,
       "dfl800IfFragsIn": dfl800IfFragsIn,
       "dfl800IfFragReassOk": dfl800IfFragReassOk,
       "dfl800IfFragReassFail": dfl800IfFragReassFail,
       "dfl800IfPktsInCnt": dfl800IfPktsInCnt,
       "dfl800IfPktsOutCnt": dfl800IfPktsOutCnt,
       "dfl800IfBitsInCnt": dfl800IfBitsInCnt,
       "dfl800IfBitsOutCnt": dfl800IfBitsOutCnt,
       "dfl800IfPktsTotCnt": dfl800IfPktsTotCnt,
       "dfl800IfBitsTotCnt": dfl800IfBitsTotCnt,
       "dfl800IfHCPktsInCnt": dfl800IfHCPktsInCnt,
       "dfl800IfHCPktsOutCnt": dfl800IfHCPktsOutCnt,
       "dfl800IfHCBitsInCnt": dfl800IfHCBitsInCnt,
       "dfl800IfHCBitsOutCnt": dfl800IfHCBitsOutCnt,
       "dfl800IfHCPktsTotCnt": dfl800IfHCPktsTotCnt,
       "dfl800IfHCBitsTotCnt": dfl800IfHCBitsTotCnt,
       "dfl800IfRxRingTable": dfl800IfRxRingTable,
       "dfl800IfRxRingEntry": dfl800IfRxRingEntry,
       "dfl800IfRxRingIndex": dfl800IfRxRingIndex,
       "dfl800IfRxRingFifoErrors": dfl800IfRxRingFifoErrors,
       "dfl800IfRxDespools": dfl800IfRxDespools,
       "dfl800IfRxAvgUse": dfl800IfRxAvgUse,
       "dfl800IfRxRingSaturation": dfl800IfRxRingSaturation,
       "dfl800RxRingFlooded": dfl800RxRingFlooded,
       "dfl800IfTxRingTable": dfl800IfTxRingTable,
       "dfl800IfTxRingEntry": dfl800IfTxRingEntry,
       "dfl800IfTxRingIndex": dfl800IfTxRingIndex,
       "dfl800IfTxDespools": dfl800IfTxDespools,
       "dfl800IfTxAvgUse": dfl800IfTxAvgUse,
       "dfl800IfTxRingSaturation": dfl800IfTxRingSaturation,
       "dfl800RxTingFlooded": dfl800RxTingFlooded,
       "dfl800IfVlanStatsTable": dfl800IfVlanStatsTable,
       "dfl800IfVlanStatsEntry": dfl800IfVlanStatsEntry,
       "dfl800IfVlanIndex": dfl800IfVlanIndex,
       "dfl800IfVlanUntaggedInPkts": dfl800IfVlanUntaggedInPkts,
       "dfl800IfVlanUntaggedOutPkts": dfl800IfVlanUntaggedOutPkts,
       "dfl800IfVlanUntaggedTotPkts": dfl800IfVlanUntaggedTotPkts,
       "dfl800IfVlanUntaggedInOctets": dfl800IfVlanUntaggedInOctets,
       "dfl800IfVlanUntaggedOutOctets": dfl800IfVlanUntaggedOutOctets,
       "dfl800IfVlanUntaggedTotOctets": dfl800IfVlanUntaggedTotOctets,
       "dfl800HWSensorTable": dfl800HWSensorTable,
       "dfl800HWSensorEntry": dfl800HWSensorEntry,
       "dfl800HWSensorIndex": dfl800HWSensorIndex,
       "dfl800HWSensorName": dfl800HWSensorName,
       "dfl800HWSensorValue": dfl800HWSensorValue,
       "dfl800HWSensorUnit": dfl800HWSensorUnit,
       "dfl800SysMemUsage": dfl800SysMemUsage,
       "dfl800SysTCPUsage": dfl800SysTCPUsage,
       "dfl800SysTCPRecvSmall": dfl800SysTCPRecvSmall,
       "dfl800SysTCPRecvLarge": dfl800SysTCPRecvLarge,
       "dfl800SysTCPSendSmall": dfl800SysTCPSendSmall,
       "dfl800SysTCPSendLarge": dfl800SysTCPSendLarge,
       "dfl800SysTimerUsage": dfl800SysTimerUsage,
       "dfl800SysConnOPS": dfl800SysConnOPS,
       "dfl800SysConnCPS": dfl800SysConnCPS,
       "dfl800SysHCForwardedBits": dfl800SysHCForwardedBits,
       "dfl800VPN": dfl800VPN,
       "dfl800IPsec": dfl800IPsec,
       "dfl800IPsecGlobal": dfl800IPsecGlobal,
       "dfl800IPsecPhaseOneActive": dfl800IPsecPhaseOneActive,
       "dfl800IPsecPhaseOneAggrModeDone": dfl800IPsecPhaseOneAggrModeDone,
       "dfl800IPsecQuickModeActive": dfl800IPsecQuickModeActive,
       "dfl800IPsecPhaseOneDone": dfl800IPsecPhaseOneDone,
       "dfl800IPsecPhaseOneFailed": dfl800IPsecPhaseOneFailed,
       "dfl800IPsecPhaseOneRekeyed": dfl800IPsecPhaseOneRekeyed,
       "dfl800IPsecQuickModeDone": dfl800IPsecQuickModeDone,
       "dfl800IPsecQuickModeFailed": dfl800IPsecQuickModeFailed,
       "dfl800IPsecInfoDone": dfl800IPsecInfoDone,
       "dfl800IPsecInfoFailed": dfl800IPsecInfoFailed,
       "dfl800IPsecInOctetsComp": dfl800IPsecInOctetsComp,
       "dfl800IPsecInOctetsUncomp": dfl800IPsecInOctetsUncomp,
       "dfl800IPsecOutOctetsComp": dfl800IPsecOutOctetsComp,
       "dfl800IPsecOutOctetsUncomp": dfl800IPsecOutOctetsUncomp,
       "dfl800IPsecForwardedOctetsComp": dfl800IPsecForwardedOctetsComp,
       "dfl800IPsecForwardedOctetsUcomp": dfl800IPsecForwardedOctetsUcomp,
       "dfl800IPsecInPackets": dfl800IPsecInPackets,
       "dfl800IPsecOutPackets": dfl800IPsecOutPackets,
       "dfl800IPsecForwardedPackets": dfl800IPsecForwardedPackets,
       "dfl800IPsecActiveTransforms": dfl800IPsecActiveTransforms,
       "dfl800IPsecTotalTransforms": dfl800IPsecTotalTransforms,
       "dfl800IPsecOutOfTransforms": dfl800IPsecOutOfTransforms,
       "dfl800IPsecTotalRekeys": dfl800IPsecTotalRekeys,
       "dfl800Rules": dfl800Rules,
       "dfl800RuleUseTable": dfl800RuleUseTable,
       "dfl800RuleUseEntry": dfl800RuleUseEntry,
       "dfl800RuleIndex": dfl800RuleIndex,
       "dfl800RuleName": dfl800RuleName,
       "dfl800RuleUse": dfl800RuleUse,
       "dfl800IPPools": dfl800IPPools,
       "dfl800IPPoolsNumber": dfl800IPPoolsNumber,
       "dfl800IPPoolTable": dfl800IPPoolTable,
       "dfl800IPPoolEntry": dfl800IPPoolEntry,
       "dfl800IPPoolIndex": dfl800IPPoolIndex,
       "dfl800IPPoolName": dfl800IPPoolName,
       "dfl800IPPoolPrepare": dfl800IPPoolPrepare,
       "dfl800IPPoolFree": dfl800IPPoolFree,
       "dfl800IPPoolMisses": dfl800IPPoolMisses,
       "dfl800IPPoolClientFails": dfl800IPPoolClientFails,
       "dfl800IPPoolUsed": dfl800IPPoolUsed,
       "dfl800DHCPServer": dfl800DHCPServer,
       "dfl800DHCPTotalRejected": dfl800DHCPTotalRejected,
       "dfl800DHCPRuleTable": dfl800DHCPRuleTable,
       "dfl800DHCPRuleEntry": dfl800DHCPRuleEntry,
       "dfl800DHCPRuleIndex": dfl800DHCPRuleIndex,
       "dfl800DHCPRuleName": dfl800DHCPRuleName,
       "dfl800DHCPRuleUsage": dfl800DHCPRuleUsage,
       "dfl800DHCPRuleUsagePercent": dfl800DHCPRuleUsagePercent,
       "dfl800DHCPActiveClients": dfl800DHCPActiveClients,
       "dfl800DHCPActiveClientsPercent": dfl800DHCPActiveClientsPercent,
       "dfl800DHCPRejectedRequests": dfl800DHCPRejectedRequests,
       "dfl800DHCPTotalLeases": dfl800DHCPTotalLeases,
       "dfl800UserAuth": dfl800UserAuth,
       "dfl800UserAuthHTTPUsers": dfl800UserAuthHTTPUsers,
       "dfl800UserAuthXAUTHUsers": dfl800UserAuthXAUTHUsers,
       "dfl800UserAuthHTTPSUsers": dfl800UserAuthHTTPSUsers,
       "dfl800UserAuthPPPUsers": dfl800UserAuthPPPUsers,
       "dfl800UserAuthEAPUsers": dfl800UserAuthEAPUsers,
       "dfl800UserAuthRuleUseTable": dfl800UserAuthRuleUseTable,
       "dfl800UserAuthRuleUseEntry": dfl800UserAuthRuleUseEntry,
       "dfl800UserAuthRuleIndex": dfl800UserAuthRuleIndex,
       "dfl800UserAuthRuleName": dfl800UserAuthRuleName,
       "dfl800UserAuthRuleUse": dfl800UserAuthRuleUse,
       "dfl800LinkMonitor": dfl800LinkMonitor,
       "dfl800LinkMonGrp": dfl800LinkMonGrp,
       "dfl800LinkMonGrpTable": dfl800LinkMonGrpTable,
       "dfl800LinkMonGrpEntry": dfl800LinkMonGrpEntry,
       "dfl800LinkMonGrpIndex": dfl800LinkMonGrpIndex,
       "dfl800LinkMonGrpName": dfl800LinkMonGrpName,
       "dfl800LinkMonGrpHostsUp": dfl800LinkMonGrpHostsUp,
       "dfl800LinkMonHostTable": dfl800LinkMonHostTable,
       "dfl800LinkMonHostEntry": dfl800LinkMonHostEntry,
       "dfl800LinkMonHostIndex": dfl800LinkMonHostIndex,
       "dfl800LinkMonHostId": dfl800LinkMonHostId,
       "dfl800LinkMonHostShortTermLoss": dfl800LinkMonHostShortTermLoss,
       "dfl800LinkMonHostPacketsLost": dfl800LinkMonHostPacketsLost,
       "dfl800Pipes": dfl800Pipes,
       "dfl800PipeUsers": dfl800PipeUsers,
       "dfl800PipeTable": dfl800PipeTable,
       "dfl800PipeEntry": dfl800PipeEntry,
       "dfl800PipeIndex": dfl800PipeIndex,
       "dfl800PipeName": dfl800PipeName,
       "dfl800PipeMinPrec": dfl800PipeMinPrec,
       "dfl800PipeMaxPrec": dfl800PipeMaxPrec,
       "dfl800PipeDefPrec": dfl800PipeDefPrec,
       "dfl800PipeNumPrec": dfl800PipeNumPrec,
       "dfl800PipeNumUsers": dfl800PipeNumUsers,
       "dfl800PipeCurrentBps": dfl800PipeCurrentBps,
       "dfl800PipeCurrentPps": dfl800PipeCurrentPps,
       "dfl800PipeDelayedPackets": dfl800PipeDelayedPackets,
       "dfl800PipeDropedPackets": dfl800PipeDropedPackets,
       "dfl800PipePrecTable": dfl800PipePrecTable,
       "dfl800PipePrecEntry": dfl800PipePrecEntry,
       "dfl800PipePrecIndex": dfl800PipePrecIndex,
       "dfl800PipePrec": dfl800PipePrec,
       "dfl800PipePrecBps": dfl800PipePrecBps,
       "dfl800PipePrecTotalPps": dfl800PipePrecTotalPps,
       "dfl800PipePrecReservedBps": dfl800PipePrecReservedBps,
       "dfl800PipePrecDynLimBps": dfl800PipePrecDynLimBps,
       "dfl800PipePrecDynUsrLimBps": dfl800PipePrecDynUsrLimBps,
       "dfl800PipePrecDelayedPackets": dfl800PipePrecDelayedPackets,
       "dfl800PipePrecDropedPackets": dfl800PipePrecDropedPackets,
       "dfl800ALG": dfl800ALG,
       "dfl800AlgSessions": dfl800AlgSessions,
       "dfl800AlgConnections": dfl800AlgConnections,
       "dfl800AlgTCPStreams": dfl800AlgTCPStreams,
       "dfl800HttpAlg": dfl800HttpAlg,
       "dfl800HttpAlgTable": dfl800HttpAlgTable,
       "dfl800HttpAlgEntry": dfl800HttpAlgEntry,
       "dfl800HttpAlgIndex": dfl800HttpAlgIndex,
       "dfl800HttpAlgName": dfl800HttpAlgName,
       "dfl800HttpAlgTotalRequested": dfl800HttpAlgTotalRequested,
       "dfl800HttpAlgTotalAllowed": dfl800HttpAlgTotalAllowed,
       "dfl800HttpAlgTotalBlocked": dfl800HttpAlgTotalBlocked,
       "dfl800HttpAlgCntFltTable": dfl800HttpAlgCntFltTable,
       "dfl800HttpAlgCntFltEntry": dfl800HttpAlgCntFltEntry,
       "dfl800HttpAlgCntFltIndex": dfl800HttpAlgCntFltIndex,
       "dfl800HttpAlgCntFltName": dfl800HttpAlgCntFltName,
       "dfl800HttpAlgCntFltRequests": dfl800HttpAlgCntFltRequests,
       "dfl800HttpAlgCntFltAllowed": dfl800HttpAlgCntFltAllowed,
       "dfl800HttpAlgCntFltBlocked": dfl800HttpAlgCntFltBlocked,
       "dfl800SmtpAlg": dfl800SmtpAlg,
       "dfl800SmtpAlgTable": dfl800SmtpAlgTable,
       "dfl800SmtpAlgEntry": dfl800SmtpAlgEntry,
       "dfl800SmtpAlgIndex": dfl800SmtpAlgIndex,
       "dfl800SmtpAlgName": dfl800SmtpAlgName,
       "dfl800SmtpAlgTotCheckedSes": dfl800SmtpAlgTotCheckedSes,
       "dfl800SmtpAlgTotSpamSes": dfl800SmtpAlgTotSpamSes,
       "dfl800SmtpAlgTotDroppedSes": dfl800SmtpAlgTotDroppedSes,
       "dfl800SmtpAlgDnsBlTable": dfl800SmtpAlgDnsBlTable,
       "dfl800SmtpAlgDnsBlEntry": dfl800SmtpAlgDnsBlEntry,
       "dfl800SmtpAlgDnsBlIndex": dfl800SmtpAlgDnsBlIndex,
       "dfl800SmtpAlgDnsBlName": dfl800SmtpAlgDnsBlName,
       "dfl800SmtpAlgDnsBlChecked": dfl800SmtpAlgDnsBlChecked,
       "dfl800SmtpAlgDnsBlMatched": dfl800SmtpAlgDnsBlMatched,
       "dfl800SmtpAlgDnsBlFailChecks": dfl800SmtpAlgDnsBlFailChecks,
       "dfl800DHCPRelay": dfl800DHCPRelay,
       "dfl800DHCPRelayCurClients": dfl800DHCPRelayCurClients,
       "dfl800DHCPRelayCurTrans": dfl800DHCPRelayCurTrans,
       "dfl800DHCPRelayRejected": dfl800DHCPRelayRejected,
       "dfl800DHCPRelayRuleTable": dfl800DHCPRelayRuleTable,
       "dfl800DHCPRelayRuleEntry": dfl800DHCPRelayRuleEntry,
       "dfl800DHCPRelayRuleIndex": dfl800DHCPRelayRuleIndex,
       "dfl800DHCPRelayRuleName": dfl800DHCPRelayRuleName,
       "dfl800DHCPRelayRuleHits": dfl800DHCPRelayRuleHits,
       "dfl800DHCPRelayRuleCurClients": dfl800DHCPRelayRuleCurClients,
       "dfl800DHCPRelayRuleRejCliPkts": dfl800DHCPRelayRuleRejCliPkts,
       "dfl800DHCPRelayRuleRejSrvPkts": dfl800DHCPRelayRuleRejSrvPkts,
       "dfl800HA": dfl800HA,
       "dfl800HASyncSendQueueLength": dfl800HASyncSendQueueLength,
       "dfl800HASyncSendQueueUsagePkt": dfl800HASyncSendQueueUsagePkt,
       "dfl800HASyncSendQueueUsageOct": dfl800HASyncSendQueueUsageOct,
       "dfl800HASyncSentPackets": dfl800HASyncSentPackets,
       "dfl800HASyncSendResentPackets": dfl800HASyncSendResentPackets,
       "dfl800reg": dfl800reg,
       "dfl800MibModules": dfl800MibModules,
       "dfl800-MIB": dfl800_MIB,
       "dfl800MibConfs": dfl800MibConfs,
       "dfl800StatsConformance": dfl800StatsConformance,
       "dfl800StatsCompliance": dfl800StatsCompliance,
       "dfl800MibObjectGroups": dfl800MibObjectGroups,
       "dfl800StatsRegGroups": dfl800StatsRegGroups,
       "dfl800SystemObjectGroup": dfl800SystemObjectGroup,
       "dfl800IPsecObjectGroup": dfl800IPsecObjectGroup,
       "dfl800StateCountersGroup": dfl800StateCountersGroup,
       "dfl800IPPoolGroup": dfl800IPPoolGroup,
       "dfl800DHCPServerGroup": dfl800DHCPServerGroup,
       "dfl800RuleUseGroup": dfl800RuleUseGroup,
       "dfl800UserAuthGroup": dfl800UserAuthGroup,
       "dfl800IfStatsGroup": dfl800IfStatsGroup,
       "dfl800LinkMonitorGroup": dfl800LinkMonitorGroup,
       "dfl800PipesObjectGroup": dfl800PipesObjectGroup,
       "dfl800DHCPRelayObjectGroup": dfl800DHCPRelayObjectGroup,
       "dfl800AlgGroup": dfl800AlgGroup,
       "dfl800HAGroup": dfl800HAGroup,
       "dfl800IfVlanGroup": dfl800IfVlanGroup,
       "dfl800SmtpAlgGroup": dfl800SmtpAlgGroup,
       "dfl800SysTCPGroup": dfl800SysTCPGroup}
)
