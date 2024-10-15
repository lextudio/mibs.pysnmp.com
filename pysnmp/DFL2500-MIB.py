# SNMP MIB module (DFL2500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL2500-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:16 2024
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

dfl2500_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 1, 2)
)
dfl2500_MIB.setRevisions(
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
_Dfl2500_ObjectIdentity = ObjectIdentity
dfl2500 = _Dfl2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5)
)
_Dfl2500OS_ObjectIdentity = ObjectIdentity
dfl2500OS = _Dfl2500OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1)
)
_Dfl2500OSStats_ObjectIdentity = ObjectIdentity
dfl2500OSStats = _Dfl2500OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2)
)
_Dfl2500System_ObjectIdentity = ObjectIdentity
dfl2500System = _Dfl2500System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1)
)
_Dfl2500SysCpuLoad_Type = Gauge32
_Dfl2500SysCpuLoad_Object = MibScalar
dfl2500SysCpuLoad = _Dfl2500SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 1),
    _Dfl2500SysCpuLoad_Type()
)
dfl2500SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysCpuLoad.setStatus("current")
_Dfl2500SysForwardedBits_Type = Counter32
_Dfl2500SysForwardedBits_Object = MibScalar
dfl2500SysForwardedBits = _Dfl2500SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 2),
    _Dfl2500SysForwardedBits_Type()
)
dfl2500SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysForwardedBits.setStatus("current")
_Dfl2500SysForwardedPackets_Type = Counter32
_Dfl2500SysForwardedPackets_Object = MibScalar
dfl2500SysForwardedPackets = _Dfl2500SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 3),
    _Dfl2500SysForwardedPackets_Type()
)
dfl2500SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysForwardedPackets.setStatus("current")
_Dfl2500SysBuffUse_Type = Gauge32
_Dfl2500SysBuffUse_Object = MibScalar
dfl2500SysBuffUse = _Dfl2500SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 4),
    _Dfl2500SysBuffUse_Type()
)
dfl2500SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysBuffUse.setStatus("current")
_Dfl2500SysConns_Type = Gauge32
_Dfl2500SysConns_Object = MibScalar
dfl2500SysConns = _Dfl2500SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 5),
    _Dfl2500SysConns_Type()
)
dfl2500SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysConns.setStatus("current")
_Dfl2500SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl2500SysPerStateCounters = _Dfl2500SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6)
)
_Dfl2500SysPscTcpSyn_Type = Gauge32
_Dfl2500SysPscTcpSyn_Object = MibScalar
dfl2500SysPscTcpSyn = _Dfl2500SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6, 1),
    _Dfl2500SysPscTcpSyn_Type()
)
dfl2500SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysPscTcpSyn.setStatus("current")
_Dfl2500SysPscTcpOpen_Type = Gauge32
_Dfl2500SysPscTcpOpen_Object = MibScalar
dfl2500SysPscTcpOpen = _Dfl2500SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6, 2),
    _Dfl2500SysPscTcpOpen_Type()
)
dfl2500SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysPscTcpOpen.setStatus("current")
_Dfl2500SysPscTcpFin_Type = Gauge32
_Dfl2500SysPscTcpFin_Object = MibScalar
dfl2500SysPscTcpFin = _Dfl2500SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6, 3),
    _Dfl2500SysPscTcpFin_Type()
)
dfl2500SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysPscTcpFin.setStatus("current")
_Dfl2500SysPscUdp_Type = Gauge32
_Dfl2500SysPscUdp_Object = MibScalar
dfl2500SysPscUdp = _Dfl2500SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6, 4),
    _Dfl2500SysPscUdp_Type()
)
dfl2500SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysPscUdp.setStatus("current")
_Dfl2500SysPscIcmp_Type = Gauge32
_Dfl2500SysPscIcmp_Object = MibScalar
dfl2500SysPscIcmp = _Dfl2500SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6, 5),
    _Dfl2500SysPscIcmp_Type()
)
dfl2500SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysPscIcmp.setStatus("current")
_Dfl2500SysPscOther_Type = Gauge32
_Dfl2500SysPscOther_Object = MibScalar
dfl2500SysPscOther = _Dfl2500SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 6, 6),
    _Dfl2500SysPscOther_Type()
)
dfl2500SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysPscOther.setStatus("current")
_Dfl2500IfStatsTable_Object = MibTable
dfl2500IfStatsTable = _Dfl2500IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl2500IfStatsTable.setStatus("current")
_Dfl2500IfStatsEntry_Object = MibTableRow
dfl2500IfStatsEntry = _Dfl2500IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1)
)
dfl2500IfStatsEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl2500IfStatsEntry.setStatus("current")


class _Dfl2500IfStatsIndex_Type(Integer32):
    """Custom type dfl2500IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500IfStatsIndex_Type.__name__ = "Integer32"
_Dfl2500IfStatsIndex_Object = MibTableColumn
dfl2500IfStatsIndex = _Dfl2500IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 1),
    _Dfl2500IfStatsIndex_Type()
)
dfl2500IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500IfStatsIndex.setStatus("current")
_Dfl2500IfName_Type = DisplayString
_Dfl2500IfName_Object = MibTableColumn
dfl2500IfName = _Dfl2500IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 2),
    _Dfl2500IfName_Type()
)
dfl2500IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfName.setStatus("current")
_Dfl2500IfFragsIn_Type = Counter32
_Dfl2500IfFragsIn_Object = MibTableColumn
dfl2500IfFragsIn = _Dfl2500IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 3),
    _Dfl2500IfFragsIn_Type()
)
dfl2500IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfFragsIn.setStatus("current")
_Dfl2500IfFragReassOk_Type = Counter32
_Dfl2500IfFragReassOk_Object = MibTableColumn
dfl2500IfFragReassOk = _Dfl2500IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 4),
    _Dfl2500IfFragReassOk_Type()
)
dfl2500IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfFragReassOk.setStatus("current")
_Dfl2500IfFragReassFail_Type = Counter32
_Dfl2500IfFragReassFail_Object = MibTableColumn
dfl2500IfFragReassFail = _Dfl2500IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 5),
    _Dfl2500IfFragReassFail_Type()
)
dfl2500IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfFragReassFail.setStatus("current")
_Dfl2500IfPktsInCnt_Type = Counter32
_Dfl2500IfPktsInCnt_Object = MibTableColumn
dfl2500IfPktsInCnt = _Dfl2500IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 6),
    _Dfl2500IfPktsInCnt_Type()
)
dfl2500IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfPktsInCnt.setStatus("current")
_Dfl2500IfPktsOutCnt_Type = Counter32
_Dfl2500IfPktsOutCnt_Object = MibTableColumn
dfl2500IfPktsOutCnt = _Dfl2500IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 7),
    _Dfl2500IfPktsOutCnt_Type()
)
dfl2500IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfPktsOutCnt.setStatus("current")
_Dfl2500IfBitsInCnt_Type = Counter32
_Dfl2500IfBitsInCnt_Object = MibTableColumn
dfl2500IfBitsInCnt = _Dfl2500IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 8),
    _Dfl2500IfBitsInCnt_Type()
)
dfl2500IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfBitsInCnt.setStatus("current")
_Dfl2500IfBitsOutCnt_Type = Counter32
_Dfl2500IfBitsOutCnt_Object = MibTableColumn
dfl2500IfBitsOutCnt = _Dfl2500IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 9),
    _Dfl2500IfBitsOutCnt_Type()
)
dfl2500IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfBitsOutCnt.setStatus("current")
_Dfl2500IfPktsTotCnt_Type = Counter32
_Dfl2500IfPktsTotCnt_Object = MibTableColumn
dfl2500IfPktsTotCnt = _Dfl2500IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 10),
    _Dfl2500IfPktsTotCnt_Type()
)
dfl2500IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfPktsTotCnt.setStatus("current")
_Dfl2500IfBitsTotCnt_Type = Counter32
_Dfl2500IfBitsTotCnt_Object = MibTableColumn
dfl2500IfBitsTotCnt = _Dfl2500IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 11),
    _Dfl2500IfBitsTotCnt_Type()
)
dfl2500IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfBitsTotCnt.setStatus("current")
_Dfl2500IfHCPktsInCnt_Type = Counter64
_Dfl2500IfHCPktsInCnt_Object = MibTableColumn
dfl2500IfHCPktsInCnt = _Dfl2500IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 12),
    _Dfl2500IfHCPktsInCnt_Type()
)
dfl2500IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfHCPktsInCnt.setStatus("current")
_Dfl2500IfHCPktsOutCnt_Type = Counter64
_Dfl2500IfHCPktsOutCnt_Object = MibTableColumn
dfl2500IfHCPktsOutCnt = _Dfl2500IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 13),
    _Dfl2500IfHCPktsOutCnt_Type()
)
dfl2500IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfHCPktsOutCnt.setStatus("current")
_Dfl2500IfHCBitsInCnt_Type = Counter64
_Dfl2500IfHCBitsInCnt_Object = MibTableColumn
dfl2500IfHCBitsInCnt = _Dfl2500IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 14),
    _Dfl2500IfHCBitsInCnt_Type()
)
dfl2500IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfHCBitsInCnt.setStatus("current")
_Dfl2500IfHCBitsOutCnt_Type = Counter64
_Dfl2500IfHCBitsOutCnt_Object = MibTableColumn
dfl2500IfHCBitsOutCnt = _Dfl2500IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 15),
    _Dfl2500IfHCBitsOutCnt_Type()
)
dfl2500IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfHCBitsOutCnt.setStatus("current")
_Dfl2500IfHCPktsTotCnt_Type = Counter64
_Dfl2500IfHCPktsTotCnt_Object = MibTableColumn
dfl2500IfHCPktsTotCnt = _Dfl2500IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 16),
    _Dfl2500IfHCPktsTotCnt_Type()
)
dfl2500IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfHCPktsTotCnt.setStatus("current")
_Dfl2500IfHCBitsTotCnt_Type = Counter64
_Dfl2500IfHCBitsTotCnt_Object = MibTableColumn
dfl2500IfHCBitsTotCnt = _Dfl2500IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 7, 1, 17),
    _Dfl2500IfHCBitsTotCnt_Type()
)
dfl2500IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfHCBitsTotCnt.setStatus("current")
_Dfl2500IfRxRingTable_Object = MibTable
dfl2500IfRxRingTable = _Dfl2500IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl2500IfRxRingTable.setStatus("current")
_Dfl2500IfRxRingEntry_Object = MibTableRow
dfl2500IfRxRingEntry = _Dfl2500IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1)
)
dfl2500IfRxRingEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl2500IfRxRingEntry.setStatus("current")


class _Dfl2500IfRxRingIndex_Type(Integer32):
    """Custom type dfl2500IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl2500IfRxRingIndex_Object = MibTableColumn
dfl2500IfRxRingIndex = _Dfl2500IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1, 1),
    _Dfl2500IfRxRingIndex_Type()
)
dfl2500IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500IfRxRingIndex.setStatus("current")
_Dfl2500IfRxRingFifoErrors_Type = Counter32
_Dfl2500IfRxRingFifoErrors_Object = MibTableColumn
dfl2500IfRxRingFifoErrors = _Dfl2500IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1, 2),
    _Dfl2500IfRxRingFifoErrors_Type()
)
dfl2500IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfRxRingFifoErrors.setStatus("current")
_Dfl2500IfRxDespools_Type = Gauge32
_Dfl2500IfRxDespools_Object = MibTableColumn
dfl2500IfRxDespools = _Dfl2500IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1, 3),
    _Dfl2500IfRxDespools_Type()
)
dfl2500IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfRxDespools.setStatus("current")
_Dfl2500IfRxAvgUse_Type = Gauge32
_Dfl2500IfRxAvgUse_Object = MibTableColumn
dfl2500IfRxAvgUse = _Dfl2500IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1, 4),
    _Dfl2500IfRxAvgUse_Type()
)
dfl2500IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfRxAvgUse.setStatus("current")
_Dfl2500IfRxRingSaturation_Type = Gauge32
_Dfl2500IfRxRingSaturation_Object = MibTableColumn
dfl2500IfRxRingSaturation = _Dfl2500IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1, 5),
    _Dfl2500IfRxRingSaturation_Type()
)
dfl2500IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfRxRingSaturation.setStatus("current")
_Dfl2500RxRingFlooded_Type = Gauge32
_Dfl2500RxRingFlooded_Object = MibTableColumn
dfl2500RxRingFlooded = _Dfl2500RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 8, 1, 6),
    _Dfl2500RxRingFlooded_Type()
)
dfl2500RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500RxRingFlooded.setStatus("current")
_Dfl2500IfTxRingTable_Object = MibTable
dfl2500IfTxRingTable = _Dfl2500IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl2500IfTxRingTable.setStatus("current")
_Dfl2500IfTxRingEntry_Object = MibTableRow
dfl2500IfTxRingEntry = _Dfl2500IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9, 1)
)
dfl2500IfTxRingEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl2500IfTxRingEntry.setStatus("current")


class _Dfl2500IfTxRingIndex_Type(Integer32):
    """Custom type dfl2500IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl2500IfTxRingIndex_Object = MibTableColumn
dfl2500IfTxRingIndex = _Dfl2500IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9, 1, 1),
    _Dfl2500IfTxRingIndex_Type()
)
dfl2500IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500IfTxRingIndex.setStatus("current")
_Dfl2500IfTxDespools_Type = Gauge32
_Dfl2500IfTxDespools_Object = MibTableColumn
dfl2500IfTxDespools = _Dfl2500IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9, 1, 2),
    _Dfl2500IfTxDespools_Type()
)
dfl2500IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfTxDespools.setStatus("current")
_Dfl2500IfTxAvgUse_Type = Gauge32
_Dfl2500IfTxAvgUse_Object = MibTableColumn
dfl2500IfTxAvgUse = _Dfl2500IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9, 1, 3),
    _Dfl2500IfTxAvgUse_Type()
)
dfl2500IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfTxAvgUse.setStatus("current")
_Dfl2500IfTxRingSaturation_Type = Gauge32
_Dfl2500IfTxRingSaturation_Object = MibTableColumn
dfl2500IfTxRingSaturation = _Dfl2500IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9, 1, 4),
    _Dfl2500IfTxRingSaturation_Type()
)
dfl2500IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfTxRingSaturation.setStatus("current")
_Dfl2500RxTingFlooded_Type = Gauge32
_Dfl2500RxTingFlooded_Object = MibTableColumn
dfl2500RxTingFlooded = _Dfl2500RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 9, 1, 5),
    _Dfl2500RxTingFlooded_Type()
)
dfl2500RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500RxTingFlooded.setStatus("current")
_Dfl2500IfVlanStatsTable_Object = MibTable
dfl2500IfVlanStatsTable = _Dfl2500IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl2500IfVlanStatsTable.setStatus("current")
_Dfl2500IfVlanStatsEntry_Object = MibTableRow
dfl2500IfVlanStatsEntry = _Dfl2500IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1)
)
dfl2500IfVlanStatsEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl2500IfVlanStatsEntry.setStatus("current")


class _Dfl2500IfVlanIndex_Type(Integer32):
    """Custom type dfl2500IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500IfVlanIndex_Type.__name__ = "Integer32"
_Dfl2500IfVlanIndex_Object = MibTableColumn
dfl2500IfVlanIndex = _Dfl2500IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 1),
    _Dfl2500IfVlanIndex_Type()
)
dfl2500IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500IfVlanIndex.setStatus("current")
_Dfl2500IfVlanUntaggedInPkts_Type = Counter32
_Dfl2500IfVlanUntaggedInPkts_Object = MibTableColumn
dfl2500IfVlanUntaggedInPkts = _Dfl2500IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 2),
    _Dfl2500IfVlanUntaggedInPkts_Type()
)
dfl2500IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfVlanUntaggedInPkts.setStatus("current")
_Dfl2500IfVlanUntaggedOutPkts_Type = Counter32
_Dfl2500IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl2500IfVlanUntaggedOutPkts = _Dfl2500IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 3),
    _Dfl2500IfVlanUntaggedOutPkts_Type()
)
dfl2500IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfVlanUntaggedOutPkts.setStatus("current")
_Dfl2500IfVlanUntaggedTotPkts_Type = Counter32
_Dfl2500IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl2500IfVlanUntaggedTotPkts = _Dfl2500IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 4),
    _Dfl2500IfVlanUntaggedTotPkts_Type()
)
dfl2500IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfVlanUntaggedTotPkts.setStatus("current")
_Dfl2500IfVlanUntaggedInOctets_Type = Counter32
_Dfl2500IfVlanUntaggedInOctets_Object = MibTableColumn
dfl2500IfVlanUntaggedInOctets = _Dfl2500IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 5),
    _Dfl2500IfVlanUntaggedInOctets_Type()
)
dfl2500IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfVlanUntaggedInOctets.setStatus("current")
_Dfl2500IfVlanUntaggedOutOctets_Type = Counter32
_Dfl2500IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl2500IfVlanUntaggedOutOctets = _Dfl2500IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 6),
    _Dfl2500IfVlanUntaggedOutOctets_Type()
)
dfl2500IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfVlanUntaggedOutOctets.setStatus("current")
_Dfl2500IfVlanUntaggedTotOctets_Type = Counter32
_Dfl2500IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl2500IfVlanUntaggedTotOctets = _Dfl2500IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 10, 1, 7),
    _Dfl2500IfVlanUntaggedTotOctets_Type()
)
dfl2500IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IfVlanUntaggedTotOctets.setStatus("current")
_Dfl2500HWSensorTable_Object = MibTable
dfl2500HWSensorTable = _Dfl2500HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl2500HWSensorTable.setStatus("current")
_Dfl2500HWSensorEntry_Object = MibTableRow
dfl2500HWSensorEntry = _Dfl2500HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 11, 1)
)
dfl2500HWSensorEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl2500HWSensorEntry.setStatus("current")


class _Dfl2500HWSensorIndex_Type(Integer32):
    """Custom type dfl2500HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500HWSensorIndex_Type.__name__ = "Integer32"
_Dfl2500HWSensorIndex_Object = MibTableColumn
dfl2500HWSensorIndex = _Dfl2500HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 11, 1, 1),
    _Dfl2500HWSensorIndex_Type()
)
dfl2500HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500HWSensorIndex.setStatus("current")
_Dfl2500HWSensorName_Type = DisplayString
_Dfl2500HWSensorName_Object = MibTableColumn
dfl2500HWSensorName = _Dfl2500HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 11, 1, 2),
    _Dfl2500HWSensorName_Type()
)
dfl2500HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HWSensorName.setStatus("current")
_Dfl2500HWSensorValue_Type = Gauge32
_Dfl2500HWSensorValue_Object = MibTableColumn
dfl2500HWSensorValue = _Dfl2500HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 11, 1, 3),
    _Dfl2500HWSensorValue_Type()
)
dfl2500HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HWSensorValue.setStatus("current")
_Dfl2500HWSensorUnit_Type = DisplayString
_Dfl2500HWSensorUnit_Object = MibTableColumn
dfl2500HWSensorUnit = _Dfl2500HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 11, 1, 4),
    _Dfl2500HWSensorUnit_Type()
)
dfl2500HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HWSensorUnit.setStatus("current")
_Dfl2500SysMemUsage_Type = Gauge32
_Dfl2500SysMemUsage_Object = MibScalar
dfl2500SysMemUsage = _Dfl2500SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 12),
    _Dfl2500SysMemUsage_Type()
)
dfl2500SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysMemUsage.setStatus("current")
_Dfl2500SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl2500SysTCPUsage = _Dfl2500SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 13)
)
_Dfl2500SysTCPRecvSmall_Type = Gauge32
_Dfl2500SysTCPRecvSmall_Object = MibScalar
dfl2500SysTCPRecvSmall = _Dfl2500SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 13, 1),
    _Dfl2500SysTCPRecvSmall_Type()
)
dfl2500SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysTCPRecvSmall.setStatus("current")
_Dfl2500SysTCPRecvLarge_Type = Gauge32
_Dfl2500SysTCPRecvLarge_Object = MibScalar
dfl2500SysTCPRecvLarge = _Dfl2500SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 13, 2),
    _Dfl2500SysTCPRecvLarge_Type()
)
dfl2500SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysTCPRecvLarge.setStatus("current")
_Dfl2500SysTCPSendSmall_Type = Gauge32
_Dfl2500SysTCPSendSmall_Object = MibScalar
dfl2500SysTCPSendSmall = _Dfl2500SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 13, 3),
    _Dfl2500SysTCPSendSmall_Type()
)
dfl2500SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysTCPSendSmall.setStatus("current")
_Dfl2500SysTCPSendLarge_Type = Gauge32
_Dfl2500SysTCPSendLarge_Object = MibScalar
dfl2500SysTCPSendLarge = _Dfl2500SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 13, 4),
    _Dfl2500SysTCPSendLarge_Type()
)
dfl2500SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysTCPSendLarge.setStatus("current")
_Dfl2500SysTimerUsage_Type = Gauge32
_Dfl2500SysTimerUsage_Object = MibScalar
dfl2500SysTimerUsage = _Dfl2500SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 14),
    _Dfl2500SysTimerUsage_Type()
)
dfl2500SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysTimerUsage.setStatus("current")
_Dfl2500SysConnOPS_Type = Gauge32
_Dfl2500SysConnOPS_Object = MibScalar
dfl2500SysConnOPS = _Dfl2500SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 15),
    _Dfl2500SysConnOPS_Type()
)
dfl2500SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysConnOPS.setStatus("current")
_Dfl2500SysConnCPS_Type = Gauge32
_Dfl2500SysConnCPS_Object = MibScalar
dfl2500SysConnCPS = _Dfl2500SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 16),
    _Dfl2500SysConnCPS_Type()
)
dfl2500SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysConnCPS.setStatus("current")
_Dfl2500SysHCForwardedBits_Type = Counter64
_Dfl2500SysHCForwardedBits_Object = MibScalar
dfl2500SysHCForwardedBits = _Dfl2500SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 1, 17),
    _Dfl2500SysHCForwardedBits_Type()
)
dfl2500SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SysHCForwardedBits.setStatus("current")
_Dfl2500VPN_ObjectIdentity = ObjectIdentity
dfl2500VPN = _Dfl2500VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2)
)
_Dfl2500IPsec_ObjectIdentity = ObjectIdentity
dfl2500IPsec = _Dfl2500IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1)
)
_Dfl2500IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl2500IPsecGlobal = _Dfl2500IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1)
)
_Dfl2500IPsecPhaseOneActive_Type = Gauge32
_Dfl2500IPsecPhaseOneActive_Object = MibScalar
dfl2500IPsecPhaseOneActive = _Dfl2500IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 1),
    _Dfl2500IPsecPhaseOneActive_Type()
)
dfl2500IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecPhaseOneActive.setStatus("current")
_Dfl2500IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl2500IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl2500IPsecPhaseOneAggrModeDone = _Dfl2500IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 2),
    _Dfl2500IPsecPhaseOneAggrModeDone_Type()
)
dfl2500IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl2500IPsecQuickModeActive_Type = Gauge32
_Dfl2500IPsecQuickModeActive_Object = MibScalar
dfl2500IPsecQuickModeActive = _Dfl2500IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 3),
    _Dfl2500IPsecQuickModeActive_Type()
)
dfl2500IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecQuickModeActive.setStatus("current")
_Dfl2500IPsecPhaseOneDone_Type = Counter32
_Dfl2500IPsecPhaseOneDone_Object = MibScalar
dfl2500IPsecPhaseOneDone = _Dfl2500IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 4),
    _Dfl2500IPsecPhaseOneDone_Type()
)
dfl2500IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecPhaseOneDone.setStatus("current")
_Dfl2500IPsecPhaseOneFailed_Type = Counter32
_Dfl2500IPsecPhaseOneFailed_Object = MibScalar
dfl2500IPsecPhaseOneFailed = _Dfl2500IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 5),
    _Dfl2500IPsecPhaseOneFailed_Type()
)
dfl2500IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecPhaseOneFailed.setStatus("current")
_Dfl2500IPsecPhaseOneRekeyed_Type = Counter32
_Dfl2500IPsecPhaseOneRekeyed_Object = MibScalar
dfl2500IPsecPhaseOneRekeyed = _Dfl2500IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 6),
    _Dfl2500IPsecPhaseOneRekeyed_Type()
)
dfl2500IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecPhaseOneRekeyed.setStatus("current")
_Dfl2500IPsecQuickModeDone_Type = Counter32
_Dfl2500IPsecQuickModeDone_Object = MibScalar
dfl2500IPsecQuickModeDone = _Dfl2500IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 7),
    _Dfl2500IPsecQuickModeDone_Type()
)
dfl2500IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecQuickModeDone.setStatus("current")
_Dfl2500IPsecQuickModeFailed_Type = Counter32
_Dfl2500IPsecQuickModeFailed_Object = MibScalar
dfl2500IPsecQuickModeFailed = _Dfl2500IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 8),
    _Dfl2500IPsecQuickModeFailed_Type()
)
dfl2500IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecQuickModeFailed.setStatus("current")
_Dfl2500IPsecInfoDone_Type = Counter32
_Dfl2500IPsecInfoDone_Object = MibScalar
dfl2500IPsecInfoDone = _Dfl2500IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 9),
    _Dfl2500IPsecInfoDone_Type()
)
dfl2500IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecInfoDone.setStatus("current")
_Dfl2500IPsecInfoFailed_Type = Counter32
_Dfl2500IPsecInfoFailed_Object = MibScalar
dfl2500IPsecInfoFailed = _Dfl2500IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 10),
    _Dfl2500IPsecInfoFailed_Type()
)
dfl2500IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecInfoFailed.setStatus("current")
_Dfl2500IPsecInOctetsComp_Type = Counter64
_Dfl2500IPsecInOctetsComp_Object = MibScalar
dfl2500IPsecInOctetsComp = _Dfl2500IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 11),
    _Dfl2500IPsecInOctetsComp_Type()
)
dfl2500IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecInOctetsComp.setStatus("current")
_Dfl2500IPsecInOctetsUncomp_Type = Counter64
_Dfl2500IPsecInOctetsUncomp_Object = MibScalar
dfl2500IPsecInOctetsUncomp = _Dfl2500IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 12),
    _Dfl2500IPsecInOctetsUncomp_Type()
)
dfl2500IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecInOctetsUncomp.setStatus("current")
_Dfl2500IPsecOutOctetsComp_Type = Counter64
_Dfl2500IPsecOutOctetsComp_Object = MibScalar
dfl2500IPsecOutOctetsComp = _Dfl2500IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 13),
    _Dfl2500IPsecOutOctetsComp_Type()
)
dfl2500IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecOutOctetsComp.setStatus("current")
_Dfl2500IPsecOutOctetsUncomp_Type = Counter64
_Dfl2500IPsecOutOctetsUncomp_Object = MibScalar
dfl2500IPsecOutOctetsUncomp = _Dfl2500IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 14),
    _Dfl2500IPsecOutOctetsUncomp_Type()
)
dfl2500IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecOutOctetsUncomp.setStatus("current")
_Dfl2500IPsecForwardedOctetsComp_Type = Counter64
_Dfl2500IPsecForwardedOctetsComp_Object = MibScalar
dfl2500IPsecForwardedOctetsComp = _Dfl2500IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 15),
    _Dfl2500IPsecForwardedOctetsComp_Type()
)
dfl2500IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecForwardedOctetsComp.setStatus("current")
_Dfl2500IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl2500IPsecForwardedOctetsUcomp_Object = MibScalar
dfl2500IPsecForwardedOctetsUcomp = _Dfl2500IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 16),
    _Dfl2500IPsecForwardedOctetsUcomp_Type()
)
dfl2500IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl2500IPsecInPackets_Type = Counter64
_Dfl2500IPsecInPackets_Object = MibScalar
dfl2500IPsecInPackets = _Dfl2500IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 17),
    _Dfl2500IPsecInPackets_Type()
)
dfl2500IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecInPackets.setStatus("current")
_Dfl2500IPsecOutPackets_Type = Counter64
_Dfl2500IPsecOutPackets_Object = MibScalar
dfl2500IPsecOutPackets = _Dfl2500IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 18),
    _Dfl2500IPsecOutPackets_Type()
)
dfl2500IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecOutPackets.setStatus("current")
_Dfl2500IPsecForwardedPackets_Type = Counter64
_Dfl2500IPsecForwardedPackets_Object = MibScalar
dfl2500IPsecForwardedPackets = _Dfl2500IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 19),
    _Dfl2500IPsecForwardedPackets_Type()
)
dfl2500IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecForwardedPackets.setStatus("current")
_Dfl2500IPsecActiveTransforms_Type = Gauge32
_Dfl2500IPsecActiveTransforms_Object = MibScalar
dfl2500IPsecActiveTransforms = _Dfl2500IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 20),
    _Dfl2500IPsecActiveTransforms_Type()
)
dfl2500IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecActiveTransforms.setStatus("current")
_Dfl2500IPsecTotalTransforms_Type = Counter32
_Dfl2500IPsecTotalTransforms_Object = MibScalar
dfl2500IPsecTotalTransforms = _Dfl2500IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 21),
    _Dfl2500IPsecTotalTransforms_Type()
)
dfl2500IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecTotalTransforms.setStatus("current")
_Dfl2500IPsecOutOfTransforms_Type = Counter32
_Dfl2500IPsecOutOfTransforms_Object = MibScalar
dfl2500IPsecOutOfTransforms = _Dfl2500IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 22),
    _Dfl2500IPsecOutOfTransforms_Type()
)
dfl2500IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecOutOfTransforms.setStatus("current")
_Dfl2500IPsecTotalRekeys_Type = Counter32
_Dfl2500IPsecTotalRekeys_Object = MibScalar
dfl2500IPsecTotalRekeys = _Dfl2500IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 2, 1, 1, 23),
    _Dfl2500IPsecTotalRekeys_Type()
)
dfl2500IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPsecTotalRekeys.setStatus("current")
_Dfl2500Rules_ObjectIdentity = ObjectIdentity
dfl2500Rules = _Dfl2500Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 3)
)
_Dfl2500RuleUseTable_Object = MibTable
dfl2500RuleUseTable = _Dfl2500RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl2500RuleUseTable.setStatus("current")
_Dfl2500RuleUseEntry_Object = MibTableRow
dfl2500RuleUseEntry = _Dfl2500RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 3, 2, 1)
)
dfl2500RuleUseEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2500RuleUseEntry.setStatus("current")


class _Dfl2500RuleIndex_Type(Integer32):
    """Custom type dfl2500RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500RuleIndex_Type.__name__ = "Integer32"
_Dfl2500RuleIndex_Object = MibTableColumn
dfl2500RuleIndex = _Dfl2500RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 3, 2, 1, 1),
    _Dfl2500RuleIndex_Type()
)
dfl2500RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500RuleIndex.setStatus("current")
_Dfl2500RuleName_Type = DisplayString
_Dfl2500RuleName_Object = MibTableColumn
dfl2500RuleName = _Dfl2500RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 3, 2, 1, 2),
    _Dfl2500RuleName_Type()
)
dfl2500RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500RuleName.setStatus("current")
_Dfl2500RuleUse_Type = Counter32
_Dfl2500RuleUse_Object = MibTableColumn
dfl2500RuleUse = _Dfl2500RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 3, 2, 1, 3),
    _Dfl2500RuleUse_Type()
)
dfl2500RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500RuleUse.setStatus("current")
_Dfl2500IPPools_ObjectIdentity = ObjectIdentity
dfl2500IPPools = _Dfl2500IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4)
)
_Dfl2500IPPoolsNumber_Type = Integer32
_Dfl2500IPPoolsNumber_Object = MibScalar
dfl2500IPPoolsNumber = _Dfl2500IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 1),
    _Dfl2500IPPoolsNumber_Type()
)
dfl2500IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolsNumber.setStatus("current")
_Dfl2500IPPoolTable_Object = MibTable
dfl2500IPPoolTable = _Dfl2500IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl2500IPPoolTable.setStatus("current")
_Dfl2500IPPoolEntry_Object = MibTableRow
dfl2500IPPoolEntry = _Dfl2500IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1)
)
dfl2500IPPoolEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl2500IPPoolEntry.setStatus("current")


class _Dfl2500IPPoolIndex_Type(Integer32):
    """Custom type dfl2500IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500IPPoolIndex_Type.__name__ = "Integer32"
_Dfl2500IPPoolIndex_Object = MibTableColumn
dfl2500IPPoolIndex = _Dfl2500IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 1),
    _Dfl2500IPPoolIndex_Type()
)
dfl2500IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500IPPoolIndex.setStatus("current")
_Dfl2500IPPoolName_Type = DisplayString
_Dfl2500IPPoolName_Object = MibTableColumn
dfl2500IPPoolName = _Dfl2500IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 2),
    _Dfl2500IPPoolName_Type()
)
dfl2500IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolName.setStatus("current")
_Dfl2500IPPoolPrepare_Type = Gauge32
_Dfl2500IPPoolPrepare_Object = MibTableColumn
dfl2500IPPoolPrepare = _Dfl2500IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 3),
    _Dfl2500IPPoolPrepare_Type()
)
dfl2500IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolPrepare.setStatus("current")
_Dfl2500IPPoolFree_Type = Gauge32
_Dfl2500IPPoolFree_Object = MibTableColumn
dfl2500IPPoolFree = _Dfl2500IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 4),
    _Dfl2500IPPoolFree_Type()
)
dfl2500IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolFree.setStatus("current")
_Dfl2500IPPoolMisses_Type = Gauge32
_Dfl2500IPPoolMisses_Object = MibTableColumn
dfl2500IPPoolMisses = _Dfl2500IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 5),
    _Dfl2500IPPoolMisses_Type()
)
dfl2500IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolMisses.setStatus("current")
_Dfl2500IPPoolClientFails_Type = Gauge32
_Dfl2500IPPoolClientFails_Object = MibTableColumn
dfl2500IPPoolClientFails = _Dfl2500IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 6),
    _Dfl2500IPPoolClientFails_Type()
)
dfl2500IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolClientFails.setStatus("current")
_Dfl2500IPPoolUsed_Type = Gauge32
_Dfl2500IPPoolUsed_Object = MibTableColumn
dfl2500IPPoolUsed = _Dfl2500IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 4, 2, 1, 7),
    _Dfl2500IPPoolUsed_Type()
)
dfl2500IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500IPPoolUsed.setStatus("current")
_Dfl2500DHCPServer_ObjectIdentity = ObjectIdentity
dfl2500DHCPServer = _Dfl2500DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5)
)
_Dfl2500DHCPTotalRejected_Type = Gauge32
_Dfl2500DHCPTotalRejected_Object = MibScalar
dfl2500DHCPTotalRejected = _Dfl2500DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 1),
    _Dfl2500DHCPTotalRejected_Type()
)
dfl2500DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPTotalRejected.setStatus("current")
_Dfl2500DHCPRuleTable_Object = MibTable
dfl2500DHCPRuleTable = _Dfl2500DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl2500DHCPRuleTable.setStatus("current")
_Dfl2500DHCPRuleEntry_Object = MibTableRow
dfl2500DHCPRuleEntry = _Dfl2500DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1)
)
dfl2500DHCPRuleEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2500DHCPRuleEntry.setStatus("current")


class _Dfl2500DHCPRuleIndex_Type(Integer32):
    """Custom type dfl2500DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl2500DHCPRuleIndex_Object = MibTableColumn
dfl2500DHCPRuleIndex = _Dfl2500DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 1),
    _Dfl2500DHCPRuleIndex_Type()
)
dfl2500DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500DHCPRuleIndex.setStatus("current")
_Dfl2500DHCPRuleName_Type = DisplayString
_Dfl2500DHCPRuleName_Object = MibTableColumn
dfl2500DHCPRuleName = _Dfl2500DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 2),
    _Dfl2500DHCPRuleName_Type()
)
dfl2500DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRuleName.setStatus("current")
_Dfl2500DHCPRuleUsage_Type = Gauge32
_Dfl2500DHCPRuleUsage_Object = MibTableColumn
dfl2500DHCPRuleUsage = _Dfl2500DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 3),
    _Dfl2500DHCPRuleUsage_Type()
)
dfl2500DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRuleUsage.setStatus("current")
_Dfl2500DHCPRuleUsagePercent_Type = Gauge32
_Dfl2500DHCPRuleUsagePercent_Object = MibTableColumn
dfl2500DHCPRuleUsagePercent = _Dfl2500DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 4),
    _Dfl2500DHCPRuleUsagePercent_Type()
)
dfl2500DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRuleUsagePercent.setStatus("current")
_Dfl2500DHCPActiveClients_Type = Gauge32
_Dfl2500DHCPActiveClients_Object = MibTableColumn
dfl2500DHCPActiveClients = _Dfl2500DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 5),
    _Dfl2500DHCPActiveClients_Type()
)
dfl2500DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPActiveClients.setStatus("current")
_Dfl2500DHCPActiveClientsPercent_Type = Gauge32
_Dfl2500DHCPActiveClientsPercent_Object = MibTableColumn
dfl2500DHCPActiveClientsPercent = _Dfl2500DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 6),
    _Dfl2500DHCPActiveClientsPercent_Type()
)
dfl2500DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPActiveClientsPercent.setStatus("current")
_Dfl2500DHCPRejectedRequests_Type = Gauge32
_Dfl2500DHCPRejectedRequests_Object = MibTableColumn
dfl2500DHCPRejectedRequests = _Dfl2500DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 7),
    _Dfl2500DHCPRejectedRequests_Type()
)
dfl2500DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRejectedRequests.setStatus("current")
_Dfl2500DHCPTotalLeases_Type = Gauge32
_Dfl2500DHCPTotalLeases_Object = MibTableColumn
dfl2500DHCPTotalLeases = _Dfl2500DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 5, 2, 1, 8),
    _Dfl2500DHCPTotalLeases_Type()
)
dfl2500DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPTotalLeases.setStatus("current")
_Dfl2500UserAuth_ObjectIdentity = ObjectIdentity
dfl2500UserAuth = _Dfl2500UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6)
)
_Dfl2500UserAuthHTTPUsers_Type = Gauge32
_Dfl2500UserAuthHTTPUsers_Object = MibScalar
dfl2500UserAuthHTTPUsers = _Dfl2500UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 1),
    _Dfl2500UserAuthHTTPUsers_Type()
)
dfl2500UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthHTTPUsers.setStatus("current")
_Dfl2500UserAuthXAUTHUsers_Type = Gauge32
_Dfl2500UserAuthXAUTHUsers_Object = MibScalar
dfl2500UserAuthXAUTHUsers = _Dfl2500UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 2),
    _Dfl2500UserAuthXAUTHUsers_Type()
)
dfl2500UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthXAUTHUsers.setStatus("current")
_Dfl2500UserAuthHTTPSUsers_Type = Gauge32
_Dfl2500UserAuthHTTPSUsers_Object = MibScalar
dfl2500UserAuthHTTPSUsers = _Dfl2500UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 3),
    _Dfl2500UserAuthHTTPSUsers_Type()
)
dfl2500UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthHTTPSUsers.setStatus("current")
_Dfl2500UserAuthPPPUsers_Type = Gauge32
_Dfl2500UserAuthPPPUsers_Object = MibScalar
dfl2500UserAuthPPPUsers = _Dfl2500UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 4),
    _Dfl2500UserAuthPPPUsers_Type()
)
dfl2500UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthPPPUsers.setStatus("current")
_Dfl2500UserAuthEAPUsers_Type = Gauge32
_Dfl2500UserAuthEAPUsers_Object = MibScalar
dfl2500UserAuthEAPUsers = _Dfl2500UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 5),
    _Dfl2500UserAuthEAPUsers_Type()
)
dfl2500UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthEAPUsers.setStatus("current")
_Dfl2500UserAuthRuleUseTable_Object = MibTable
dfl2500UserAuthRuleUseTable = _Dfl2500UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl2500UserAuthRuleUseTable.setStatus("current")
_Dfl2500UserAuthRuleUseEntry_Object = MibTableRow
dfl2500UserAuthRuleUseEntry = _Dfl2500UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 6, 1)
)
dfl2500UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2500UserAuthRuleUseEntry.setStatus("current")


class _Dfl2500UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl2500UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl2500UserAuthRuleIndex_Object = MibTableColumn
dfl2500UserAuthRuleIndex = _Dfl2500UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 6, 1, 1),
    _Dfl2500UserAuthRuleIndex_Type()
)
dfl2500UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500UserAuthRuleIndex.setStatus("current")
_Dfl2500UserAuthRuleName_Type = DisplayString
_Dfl2500UserAuthRuleName_Object = MibTableColumn
dfl2500UserAuthRuleName = _Dfl2500UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 6, 1, 2),
    _Dfl2500UserAuthRuleName_Type()
)
dfl2500UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthRuleName.setStatus("current")
_Dfl2500UserAuthRuleUse_Type = Counter32
_Dfl2500UserAuthRuleUse_Object = MibTableColumn
dfl2500UserAuthRuleUse = _Dfl2500UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 6, 6, 1, 3),
    _Dfl2500UserAuthRuleUse_Type()
)
dfl2500UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500UserAuthRuleUse.setStatus("current")
_Dfl2500LinkMonitor_ObjectIdentity = ObjectIdentity
dfl2500LinkMonitor = _Dfl2500LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7)
)
_Dfl2500LinkMonGrp_Type = Integer32
_Dfl2500LinkMonGrp_Object = MibScalar
dfl2500LinkMonGrp = _Dfl2500LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 1),
    _Dfl2500LinkMonGrp_Type()
)
dfl2500LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500LinkMonGrp.setStatus("current")
_Dfl2500LinkMonGrpTable_Object = MibTable
dfl2500LinkMonGrpTable = _Dfl2500LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl2500LinkMonGrpTable.setStatus("current")
_Dfl2500LinkMonGrpEntry_Object = MibTableRow
dfl2500LinkMonGrpEntry = _Dfl2500LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 2, 1)
)
dfl2500LinkMonGrpEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl2500LinkMonGrpEntry.setStatus("current")


class _Dfl2500LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl2500LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl2500LinkMonGrpIndex_Object = MibTableColumn
dfl2500LinkMonGrpIndex = _Dfl2500LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 2, 1, 1),
    _Dfl2500LinkMonGrpIndex_Type()
)
dfl2500LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500LinkMonGrpIndex.setStatus("current")
_Dfl2500LinkMonGrpName_Type = DisplayString
_Dfl2500LinkMonGrpName_Object = MibTableColumn
dfl2500LinkMonGrpName = _Dfl2500LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 2, 1, 2),
    _Dfl2500LinkMonGrpName_Type()
)
dfl2500LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500LinkMonGrpName.setStatus("current")
_Dfl2500LinkMonGrpHostsUp_Type = Gauge32
_Dfl2500LinkMonGrpHostsUp_Object = MibTableColumn
dfl2500LinkMonGrpHostsUp = _Dfl2500LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 2, 1, 3),
    _Dfl2500LinkMonGrpHostsUp_Type()
)
dfl2500LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500LinkMonGrpHostsUp.setStatus("current")
_Dfl2500LinkMonHostTable_Object = MibTable
dfl2500LinkMonHostTable = _Dfl2500LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl2500LinkMonHostTable.setStatus("current")
_Dfl2500LinkMonHostEntry_Object = MibTableRow
dfl2500LinkMonHostEntry = _Dfl2500LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 3, 1)
)
dfl2500LinkMonHostEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500LinkMonGrpIndex"),
    (0, "DFL2500-MIB", "dfl2500LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl2500LinkMonHostEntry.setStatus("current")


class _Dfl2500LinkMonHostIndex_Type(Integer32):
    """Custom type dfl2500LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl2500LinkMonHostIndex_Object = MibTableColumn
dfl2500LinkMonHostIndex = _Dfl2500LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 3, 1, 1),
    _Dfl2500LinkMonHostIndex_Type()
)
dfl2500LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500LinkMonHostIndex.setStatus("current")
_Dfl2500LinkMonHostId_Type = DisplayString
_Dfl2500LinkMonHostId_Object = MibTableColumn
dfl2500LinkMonHostId = _Dfl2500LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 3, 1, 2),
    _Dfl2500LinkMonHostId_Type()
)
dfl2500LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500LinkMonHostId.setStatus("current")
_Dfl2500LinkMonHostShortTermLoss_Type = Gauge32
_Dfl2500LinkMonHostShortTermLoss_Object = MibTableColumn
dfl2500LinkMonHostShortTermLoss = _Dfl2500LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 3, 1, 3),
    _Dfl2500LinkMonHostShortTermLoss_Type()
)
dfl2500LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500LinkMonHostShortTermLoss.setStatus("current")
_Dfl2500LinkMonHostPacketsLost_Type = Counter32
_Dfl2500LinkMonHostPacketsLost_Object = MibTableColumn
dfl2500LinkMonHostPacketsLost = _Dfl2500LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 7, 3, 1, 4),
    _Dfl2500LinkMonHostPacketsLost_Type()
)
dfl2500LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500LinkMonHostPacketsLost.setStatus("current")
_Dfl2500Pipes_ObjectIdentity = ObjectIdentity
dfl2500Pipes = _Dfl2500Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8)
)
_Dfl2500PipeUsers_Type = Gauge32
_Dfl2500PipeUsers_Object = MibScalar
dfl2500PipeUsers = _Dfl2500PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 1),
    _Dfl2500PipeUsers_Type()
)
dfl2500PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeUsers.setStatus("current")
_Dfl2500PipeTable_Object = MibTable
dfl2500PipeTable = _Dfl2500PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl2500PipeTable.setStatus("current")
_Dfl2500PipeEntry_Object = MibTableRow
dfl2500PipeEntry = _Dfl2500PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1)
)
dfl2500PipeEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl2500PipeEntry.setStatus("current")


class _Dfl2500PipeIndex_Type(Integer32):
    """Custom type dfl2500PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500PipeIndex_Type.__name__ = "Integer32"
_Dfl2500PipeIndex_Object = MibTableColumn
dfl2500PipeIndex = _Dfl2500PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 1),
    _Dfl2500PipeIndex_Type()
)
dfl2500PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500PipeIndex.setStatus("current")
_Dfl2500PipeName_Type = DisplayString
_Dfl2500PipeName_Object = MibTableColumn
dfl2500PipeName = _Dfl2500PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 2),
    _Dfl2500PipeName_Type()
)
dfl2500PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeName.setStatus("current")
_Dfl2500PipeMinPrec_Type = Integer32
_Dfl2500PipeMinPrec_Object = MibTableColumn
dfl2500PipeMinPrec = _Dfl2500PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 3),
    _Dfl2500PipeMinPrec_Type()
)
dfl2500PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeMinPrec.setStatus("current")
_Dfl2500PipeMaxPrec_Type = Integer32
_Dfl2500PipeMaxPrec_Object = MibTableColumn
dfl2500PipeMaxPrec = _Dfl2500PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 4),
    _Dfl2500PipeMaxPrec_Type()
)
dfl2500PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeMaxPrec.setStatus("current")
_Dfl2500PipeDefPrec_Type = Integer32
_Dfl2500PipeDefPrec_Object = MibTableColumn
dfl2500PipeDefPrec = _Dfl2500PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 5),
    _Dfl2500PipeDefPrec_Type()
)
dfl2500PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeDefPrec.setStatus("current")
_Dfl2500PipeNumPrec_Type = Integer32
_Dfl2500PipeNumPrec_Object = MibTableColumn
dfl2500PipeNumPrec = _Dfl2500PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 6),
    _Dfl2500PipeNumPrec_Type()
)
dfl2500PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeNumPrec.setStatus("current")
_Dfl2500PipeNumUsers_Type = Gauge32
_Dfl2500PipeNumUsers_Object = MibTableColumn
dfl2500PipeNumUsers = _Dfl2500PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 7),
    _Dfl2500PipeNumUsers_Type()
)
dfl2500PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeNumUsers.setStatus("current")
_Dfl2500PipeCurrentBps_Type = Gauge32
_Dfl2500PipeCurrentBps_Object = MibTableColumn
dfl2500PipeCurrentBps = _Dfl2500PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 8),
    _Dfl2500PipeCurrentBps_Type()
)
dfl2500PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeCurrentBps.setStatus("current")
_Dfl2500PipeCurrentPps_Type = Gauge32
_Dfl2500PipeCurrentPps_Object = MibTableColumn
dfl2500PipeCurrentPps = _Dfl2500PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 9),
    _Dfl2500PipeCurrentPps_Type()
)
dfl2500PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeCurrentPps.setStatus("current")
_Dfl2500PipeDelayedPackets_Type = Counter32
_Dfl2500PipeDelayedPackets_Object = MibTableColumn
dfl2500PipeDelayedPackets = _Dfl2500PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 10),
    _Dfl2500PipeDelayedPackets_Type()
)
dfl2500PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeDelayedPackets.setStatus("current")
_Dfl2500PipeDropedPackets_Type = Counter32
_Dfl2500PipeDropedPackets_Object = MibTableColumn
dfl2500PipeDropedPackets = _Dfl2500PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 2, 1, 11),
    _Dfl2500PipeDropedPackets_Type()
)
dfl2500PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipeDropedPackets.setStatus("current")
_Dfl2500PipePrecTable_Object = MibTable
dfl2500PipePrecTable = _Dfl2500PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl2500PipePrecTable.setStatus("current")
_Dfl2500PipePrecEntry_Object = MibTableRow
dfl2500PipePrecEntry = _Dfl2500PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1)
)
dfl2500PipePrecEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500PipeIndex"),
    (0, "DFL2500-MIB", "dfl2500PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl2500PipePrecEntry.setStatus("current")


class _Dfl2500PipePrecIndex_Type(Integer32):
    """Custom type dfl2500PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500PipePrecIndex_Type.__name__ = "Integer32"
_Dfl2500PipePrecIndex_Object = MibTableColumn
dfl2500PipePrecIndex = _Dfl2500PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 1),
    _Dfl2500PipePrecIndex_Type()
)
dfl2500PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500PipePrecIndex.setStatus("current")
_Dfl2500PipePrec_Type = Integer32
_Dfl2500PipePrec_Object = MibTableColumn
dfl2500PipePrec = _Dfl2500PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 2),
    _Dfl2500PipePrec_Type()
)
dfl2500PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrec.setStatus("current")
_Dfl2500PipePrecBps_Type = Gauge32
_Dfl2500PipePrecBps_Object = MibTableColumn
dfl2500PipePrecBps = _Dfl2500PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 3),
    _Dfl2500PipePrecBps_Type()
)
dfl2500PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecBps.setStatus("current")
_Dfl2500PipePrecTotalPps_Type = Gauge32
_Dfl2500PipePrecTotalPps_Object = MibTableColumn
dfl2500PipePrecTotalPps = _Dfl2500PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 4),
    _Dfl2500PipePrecTotalPps_Type()
)
dfl2500PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecTotalPps.setStatus("current")
_Dfl2500PipePrecReservedBps_Type = Gauge32
_Dfl2500PipePrecReservedBps_Object = MibTableColumn
dfl2500PipePrecReservedBps = _Dfl2500PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 5),
    _Dfl2500PipePrecReservedBps_Type()
)
dfl2500PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecReservedBps.setStatus("current")
_Dfl2500PipePrecDynLimBps_Type = Gauge32
_Dfl2500PipePrecDynLimBps_Object = MibTableColumn
dfl2500PipePrecDynLimBps = _Dfl2500PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 6),
    _Dfl2500PipePrecDynLimBps_Type()
)
dfl2500PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecDynLimBps.setStatus("current")
_Dfl2500PipePrecDynUsrLimBps_Type = Gauge32
_Dfl2500PipePrecDynUsrLimBps_Object = MibTableColumn
dfl2500PipePrecDynUsrLimBps = _Dfl2500PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 7),
    _Dfl2500PipePrecDynUsrLimBps_Type()
)
dfl2500PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecDynUsrLimBps.setStatus("current")
_Dfl2500PipePrecDelayedPackets_Type = Counter32
_Dfl2500PipePrecDelayedPackets_Object = MibTableColumn
dfl2500PipePrecDelayedPackets = _Dfl2500PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 8),
    _Dfl2500PipePrecDelayedPackets_Type()
)
dfl2500PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecDelayedPackets.setStatus("current")
_Dfl2500PipePrecDropedPackets_Type = Counter32
_Dfl2500PipePrecDropedPackets_Object = MibTableColumn
dfl2500PipePrecDropedPackets = _Dfl2500PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 8, 3, 1, 9),
    _Dfl2500PipePrecDropedPackets_Type()
)
dfl2500PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500PipePrecDropedPackets.setStatus("current")
_Dfl2500ALG_ObjectIdentity = ObjectIdentity
dfl2500ALG = _Dfl2500ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9)
)
_Dfl2500AlgSessions_Type = Gauge32
_Dfl2500AlgSessions_Object = MibScalar
dfl2500AlgSessions = _Dfl2500AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 1),
    _Dfl2500AlgSessions_Type()
)
dfl2500AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500AlgSessions.setStatus("current")
_Dfl2500AlgConnections_Type = Gauge32
_Dfl2500AlgConnections_Object = MibScalar
dfl2500AlgConnections = _Dfl2500AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 2),
    _Dfl2500AlgConnections_Type()
)
dfl2500AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500AlgConnections.setStatus("current")
_Dfl2500AlgTCPStreams_Type = Gauge32
_Dfl2500AlgTCPStreams_Object = MibScalar
dfl2500AlgTCPStreams = _Dfl2500AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 3),
    _Dfl2500AlgTCPStreams_Type()
)
dfl2500AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500AlgTCPStreams.setStatus("current")
_Dfl2500HttpAlg_ObjectIdentity = ObjectIdentity
dfl2500HttpAlg = _Dfl2500HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4)
)
_Dfl2500HttpAlgTable_Object = MibTable
dfl2500HttpAlgTable = _Dfl2500HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl2500HttpAlgTable.setStatus("current")
_Dfl2500HttpAlgEntry_Object = MibTableRow
dfl2500HttpAlgEntry = _Dfl2500HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1, 1)
)
dfl2500HttpAlgEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl2500HttpAlgEntry.setStatus("current")


class _Dfl2500HttpAlgIndex_Type(Integer32):
    """Custom type dfl2500HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl2500HttpAlgIndex_Object = MibTableColumn
dfl2500HttpAlgIndex = _Dfl2500HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1, 1, 1),
    _Dfl2500HttpAlgIndex_Type()
)
dfl2500HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500HttpAlgIndex.setStatus("current")
_Dfl2500HttpAlgName_Type = DisplayString
_Dfl2500HttpAlgName_Object = MibTableColumn
dfl2500HttpAlgName = _Dfl2500HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1, 1, 2),
    _Dfl2500HttpAlgName_Type()
)
dfl2500HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgName.setStatus("current")
_Dfl2500HttpAlgTotalRequested_Type = Gauge32
_Dfl2500HttpAlgTotalRequested_Object = MibTableColumn
dfl2500HttpAlgTotalRequested = _Dfl2500HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1, 1, 3),
    _Dfl2500HttpAlgTotalRequested_Type()
)
dfl2500HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgTotalRequested.setStatus("current")
_Dfl2500HttpAlgTotalAllowed_Type = Gauge32
_Dfl2500HttpAlgTotalAllowed_Object = MibTableColumn
dfl2500HttpAlgTotalAllowed = _Dfl2500HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1, 1, 4),
    _Dfl2500HttpAlgTotalAllowed_Type()
)
dfl2500HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgTotalAllowed.setStatus("current")
_Dfl2500HttpAlgTotalBlocked_Type = Gauge32
_Dfl2500HttpAlgTotalBlocked_Object = MibTableColumn
dfl2500HttpAlgTotalBlocked = _Dfl2500HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 1, 1, 5),
    _Dfl2500HttpAlgTotalBlocked_Type()
)
dfl2500HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgTotalBlocked.setStatus("current")
_Dfl2500HttpAlgCntFltTable_Object = MibTable
dfl2500HttpAlgCntFltTable = _Dfl2500HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltTable.setStatus("current")
_Dfl2500HttpAlgCntFltEntry_Object = MibTableRow
dfl2500HttpAlgCntFltEntry = _Dfl2500HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2, 1)
)
dfl2500HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500HttpAlgIndex"),
    (0, "DFL2500-MIB", "dfl2500HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltEntry.setStatus("current")


class _Dfl2500HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl2500HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl2500HttpAlgCntFltIndex_Object = MibTableColumn
dfl2500HttpAlgCntFltIndex = _Dfl2500HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2, 1, 1),
    _Dfl2500HttpAlgCntFltIndex_Type()
)
dfl2500HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltIndex.setStatus("current")
_Dfl2500HttpAlgCntFltName_Type = DisplayString
_Dfl2500HttpAlgCntFltName_Object = MibTableColumn
dfl2500HttpAlgCntFltName = _Dfl2500HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2, 1, 2),
    _Dfl2500HttpAlgCntFltName_Type()
)
dfl2500HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltName.setStatus("current")
_Dfl2500HttpAlgCntFltRequests_Type = Gauge32
_Dfl2500HttpAlgCntFltRequests_Object = MibTableColumn
dfl2500HttpAlgCntFltRequests = _Dfl2500HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2, 1, 3),
    _Dfl2500HttpAlgCntFltRequests_Type()
)
dfl2500HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltRequests.setStatus("current")
_Dfl2500HttpAlgCntFltAllowed_Type = Gauge32
_Dfl2500HttpAlgCntFltAllowed_Object = MibTableColumn
dfl2500HttpAlgCntFltAllowed = _Dfl2500HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2, 1, 4),
    _Dfl2500HttpAlgCntFltAllowed_Type()
)
dfl2500HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltAllowed.setStatus("current")
_Dfl2500HttpAlgCntFltBlocked_Type = Gauge32
_Dfl2500HttpAlgCntFltBlocked_Object = MibTableColumn
dfl2500HttpAlgCntFltBlocked = _Dfl2500HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 4, 2, 1, 5),
    _Dfl2500HttpAlgCntFltBlocked_Type()
)
dfl2500HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HttpAlgCntFltBlocked.setStatus("current")
_Dfl2500SmtpAlg_ObjectIdentity = ObjectIdentity
dfl2500SmtpAlg = _Dfl2500SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5)
)
_Dfl2500SmtpAlgTable_Object = MibTable
dfl2500SmtpAlgTable = _Dfl2500SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl2500SmtpAlgTable.setStatus("current")
_Dfl2500SmtpAlgEntry_Object = MibTableRow
dfl2500SmtpAlgEntry = _Dfl2500SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1, 1)
)
dfl2500SmtpAlgEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl2500SmtpAlgEntry.setStatus("current")


class _Dfl2500SmtpAlgIndex_Type(Integer32):
    """Custom type dfl2500SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl2500SmtpAlgIndex_Object = MibTableColumn
dfl2500SmtpAlgIndex = _Dfl2500SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1, 1, 1),
    _Dfl2500SmtpAlgIndex_Type()
)
dfl2500SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgIndex.setStatus("current")
_Dfl2500SmtpAlgName_Type = DisplayString
_Dfl2500SmtpAlgName_Object = MibTableColumn
dfl2500SmtpAlgName = _Dfl2500SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1, 1, 2),
    _Dfl2500SmtpAlgName_Type()
)
dfl2500SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgName.setStatus("current")
_Dfl2500SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl2500SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl2500SmtpAlgTotCheckedSes = _Dfl2500SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1, 1, 3),
    _Dfl2500SmtpAlgTotCheckedSes_Type()
)
dfl2500SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgTotCheckedSes.setStatus("current")
_Dfl2500SmtpAlgTotSpamSes_Type = Gauge32
_Dfl2500SmtpAlgTotSpamSes_Object = MibTableColumn
dfl2500SmtpAlgTotSpamSes = _Dfl2500SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1, 1, 4),
    _Dfl2500SmtpAlgTotSpamSes_Type()
)
dfl2500SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgTotSpamSes.setStatus("current")
_Dfl2500SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl2500SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl2500SmtpAlgTotDroppedSes = _Dfl2500SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 1, 1, 5),
    _Dfl2500SmtpAlgTotDroppedSes_Type()
)
dfl2500SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgTotDroppedSes.setStatus("current")
_Dfl2500SmtpAlgDnsBlTable_Object = MibTable
dfl2500SmtpAlgDnsBlTable = _Dfl2500SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlTable.setStatus("current")
_Dfl2500SmtpAlgDnsBlEntry_Object = MibTableRow
dfl2500SmtpAlgDnsBlEntry = _Dfl2500SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2, 1)
)
dfl2500SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500SmtpAlgIndex"),
    (0, "DFL2500-MIB", "dfl2500SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl2500SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl2500SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl2500SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl2500SmtpAlgDnsBlIndex = _Dfl2500SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2, 1, 1),
    _Dfl2500SmtpAlgDnsBlIndex_Type()
)
dfl2500SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlIndex.setStatus("current")
_Dfl2500SmtpAlgDnsBlName_Type = DisplayString
_Dfl2500SmtpAlgDnsBlName_Object = MibTableColumn
dfl2500SmtpAlgDnsBlName = _Dfl2500SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2, 1, 2),
    _Dfl2500SmtpAlgDnsBlName_Type()
)
dfl2500SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlName.setStatus("current")
_Dfl2500SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl2500SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl2500SmtpAlgDnsBlChecked = _Dfl2500SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2, 1, 3),
    _Dfl2500SmtpAlgDnsBlChecked_Type()
)
dfl2500SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlChecked.setStatus("current")
_Dfl2500SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl2500SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl2500SmtpAlgDnsBlMatched = _Dfl2500SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2, 1, 4),
    _Dfl2500SmtpAlgDnsBlMatched_Type()
)
dfl2500SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlMatched.setStatus("current")
_Dfl2500SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl2500SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl2500SmtpAlgDnsBlFailChecks = _Dfl2500SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 9, 5, 2, 1, 5),
    _Dfl2500SmtpAlgDnsBlFailChecks_Type()
)
dfl2500SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl2500DHCPRelay_ObjectIdentity = ObjectIdentity
dfl2500DHCPRelay = _Dfl2500DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11)
)
_Dfl2500DHCPRelayCurClients_Type = Gauge32
_Dfl2500DHCPRelayCurClients_Object = MibScalar
dfl2500DHCPRelayCurClients = _Dfl2500DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 1),
    _Dfl2500DHCPRelayCurClients_Type()
)
dfl2500DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayCurClients.setStatus("current")
_Dfl2500DHCPRelayCurTrans_Type = Gauge32
_Dfl2500DHCPRelayCurTrans_Object = MibScalar
dfl2500DHCPRelayCurTrans = _Dfl2500DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 2),
    _Dfl2500DHCPRelayCurTrans_Type()
)
dfl2500DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayCurTrans.setStatus("current")
_Dfl2500DHCPRelayRejected_Type = Gauge32
_Dfl2500DHCPRelayRejected_Object = MibScalar
dfl2500DHCPRelayRejected = _Dfl2500DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 3),
    _Dfl2500DHCPRelayRejected_Type()
)
dfl2500DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRejected.setStatus("current")
_Dfl2500DHCPRelayRuleTable_Object = MibTable
dfl2500DHCPRelayRuleTable = _Dfl2500DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleTable.setStatus("current")
_Dfl2500DHCPRelayRuleEntry_Object = MibTableRow
dfl2500DHCPRelayRuleEntry = _Dfl2500DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1)
)
dfl2500DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL2500-MIB", "dfl2500DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleEntry.setStatus("current")


class _Dfl2500DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl2500DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2500DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl2500DHCPRelayRuleIndex_Object = MibTableColumn
dfl2500DHCPRelayRuleIndex = _Dfl2500DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1, 1),
    _Dfl2500DHCPRelayRuleIndex_Type()
)
dfl2500DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleIndex.setStatus("current")
_Dfl2500DHCPRelayRuleName_Type = DisplayString
_Dfl2500DHCPRelayRuleName_Object = MibTableColumn
dfl2500DHCPRelayRuleName = _Dfl2500DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1, 2),
    _Dfl2500DHCPRelayRuleName_Type()
)
dfl2500DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleName.setStatus("current")
_Dfl2500DHCPRelayRuleHits_Type = Gauge32
_Dfl2500DHCPRelayRuleHits_Object = MibTableColumn
dfl2500DHCPRelayRuleHits = _Dfl2500DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1, 3),
    _Dfl2500DHCPRelayRuleHits_Type()
)
dfl2500DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleHits.setStatus("current")
_Dfl2500DHCPRelayRuleCurClients_Type = Gauge32
_Dfl2500DHCPRelayRuleCurClients_Object = MibTableColumn
dfl2500DHCPRelayRuleCurClients = _Dfl2500DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1, 4),
    _Dfl2500DHCPRelayRuleCurClients_Type()
)
dfl2500DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleCurClients.setStatus("current")
_Dfl2500DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl2500DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl2500DHCPRelayRuleRejCliPkts = _Dfl2500DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1, 5),
    _Dfl2500DHCPRelayRuleRejCliPkts_Type()
)
dfl2500DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl2500DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl2500DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl2500DHCPRelayRuleRejSrvPkts = _Dfl2500DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 11, 4, 1, 6),
    _Dfl2500DHCPRelayRuleRejSrvPkts_Type()
)
dfl2500DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl2500HA_ObjectIdentity = ObjectIdentity
dfl2500HA = _Dfl2500HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 12)
)
_Dfl2500HASyncSendQueueLength_Type = Gauge32
_Dfl2500HASyncSendQueueLength_Object = MibScalar
dfl2500HASyncSendQueueLength = _Dfl2500HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 12, 1),
    _Dfl2500HASyncSendQueueLength_Type()
)
dfl2500HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HASyncSendQueueLength.setStatus("current")
_Dfl2500HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl2500HASyncSendQueueUsagePkt_Object = MibScalar
dfl2500HASyncSendQueueUsagePkt = _Dfl2500HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 12, 2),
    _Dfl2500HASyncSendQueueUsagePkt_Type()
)
dfl2500HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HASyncSendQueueUsagePkt.setStatus("current")
_Dfl2500HASyncSendQueueUsageOct_Type = Gauge32
_Dfl2500HASyncSendQueueUsageOct_Object = MibScalar
dfl2500HASyncSendQueueUsageOct = _Dfl2500HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 12, 3),
    _Dfl2500HASyncSendQueueUsageOct_Type()
)
dfl2500HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HASyncSendQueueUsageOct.setStatus("current")
_Dfl2500HASyncSentPackets_Type = Counter32
_Dfl2500HASyncSentPackets_Object = MibScalar
dfl2500HASyncSentPackets = _Dfl2500HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 12, 4),
    _Dfl2500HASyncSentPackets_Type()
)
dfl2500HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HASyncSentPackets.setStatus("current")
_Dfl2500HASyncSendResentPackets_Type = Counter32
_Dfl2500HASyncSendResentPackets_Object = MibScalar
dfl2500HASyncSendResentPackets = _Dfl2500HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 1, 2, 12, 5),
    _Dfl2500HASyncSendResentPackets_Type()
)
dfl2500HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2500HASyncSendResentPackets.setStatus("current")
_Dfl2500reg_ObjectIdentity = ObjectIdentity
dfl2500reg = _Dfl2500reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2)
)
_Dfl2500MibModules_ObjectIdentity = ObjectIdentity
dfl2500MibModules = _Dfl2500MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 1)
)
_Dfl2500MibConfs_ObjectIdentity = ObjectIdentity
dfl2500MibConfs = _Dfl2500MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 2)
)
_Dfl2500StatsConformance_ObjectIdentity = ObjectIdentity
dfl2500StatsConformance = _Dfl2500StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 2, 1)
)
_Dfl2500MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl2500MibObjectGroups = _Dfl2500MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3)
)
_Dfl2500StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl2500StatsRegGroups = _Dfl2500StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1)
)

# Managed Objects groups

dfl2500SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 1)
)
dfl2500SystemObjectGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500SysCpuLoad"),
        ("DFL2500-MIB", "dfl2500SysForwardedBits"),
        ("DFL2500-MIB", "dfl2500SysForwardedPackets"),
        ("DFL2500-MIB", "dfl2500SysBuffUse"),
        ("DFL2500-MIB", "dfl2500SysConns"),
        ("DFL2500-MIB", "dfl2500HWSensorName"),
        ("DFL2500-MIB", "dfl2500HWSensorValue"),
        ("DFL2500-MIB", "dfl2500HWSensorUnit"),
        ("DFL2500-MIB", "dfl2500SysMemUsage"),
        ("DFL2500-MIB", "dfl2500SysTimerUsage"),
        ("DFL2500-MIB", "dfl2500SysConnOPS"),
        ("DFL2500-MIB", "dfl2500SysConnCPS"),
        ("DFL2500-MIB", "dfl2500SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl2500SystemObjectGroup.setStatus("current")

dfl2500IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 2)
)
dfl2500IPsecObjectGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500IPsecPhaseOneActive"),
        ("DFL2500-MIB", "dfl2500IPsecPhaseOneAggrModeDone"),
        ("DFL2500-MIB", "dfl2500IPsecQuickModeActive"),
        ("DFL2500-MIB", "dfl2500IPsecPhaseOneDone"),
        ("DFL2500-MIB", "dfl2500IPsecPhaseOneFailed"),
        ("DFL2500-MIB", "dfl2500IPsecPhaseOneRekeyed"),
        ("DFL2500-MIB", "dfl2500IPsecQuickModeDone"),
        ("DFL2500-MIB", "dfl2500IPsecQuickModeFailed"),
        ("DFL2500-MIB", "dfl2500IPsecInfoDone"),
        ("DFL2500-MIB", "dfl2500IPsecInfoFailed"),
        ("DFL2500-MIB", "dfl2500IPsecInOctetsComp"),
        ("DFL2500-MIB", "dfl2500IPsecInOctetsUncomp"),
        ("DFL2500-MIB", "dfl2500IPsecOutOctetsComp"),
        ("DFL2500-MIB", "dfl2500IPsecOutOctetsUncomp"),
        ("DFL2500-MIB", "dfl2500IPsecForwardedOctetsComp"),
        ("DFL2500-MIB", "dfl2500IPsecForwardedOctetsUcomp"),
        ("DFL2500-MIB", "dfl2500IPsecInPackets"),
        ("DFL2500-MIB", "dfl2500IPsecOutPackets"),
        ("DFL2500-MIB", "dfl2500IPsecForwardedPackets"),
        ("DFL2500-MIB", "dfl2500IPsecActiveTransforms"),
        ("DFL2500-MIB", "dfl2500IPsecTotalTransforms"),
        ("DFL2500-MIB", "dfl2500IPsecOutOfTransforms"),
        ("DFL2500-MIB", "dfl2500IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl2500IPsecObjectGroup.setStatus("current")

dfl2500StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 3)
)
dfl2500StateCountersGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500SysPscTcpSyn"),
        ("DFL2500-MIB", "dfl2500SysPscTcpOpen"),
        ("DFL2500-MIB", "dfl2500SysPscTcpFin"),
        ("DFL2500-MIB", "dfl2500SysPscUdp"),
        ("DFL2500-MIB", "dfl2500SysPscIcmp"),
        ("DFL2500-MIB", "dfl2500SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl2500StateCountersGroup.setStatus("current")

dfl2500IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 4)
)
dfl2500IPPoolGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500IPPoolsNumber"),
        ("DFL2500-MIB", "dfl2500IPPoolName"),
        ("DFL2500-MIB", "dfl2500IPPoolPrepare"),
        ("DFL2500-MIB", "dfl2500IPPoolFree"),
        ("DFL2500-MIB", "dfl2500IPPoolMisses"),
        ("DFL2500-MIB", "dfl2500IPPoolClientFails"),
        ("DFL2500-MIB", "dfl2500IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl2500IPPoolGroup.setStatus("current")

dfl2500DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 5)
)
dfl2500DHCPServerGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500DHCPTotalRejected"),
        ("DFL2500-MIB", "dfl2500DHCPRuleName"),
        ("DFL2500-MIB", "dfl2500DHCPRuleUsage"),
        ("DFL2500-MIB", "dfl2500DHCPRuleUsagePercent"),
        ("DFL2500-MIB", "dfl2500DHCPActiveClients"),
        ("DFL2500-MIB", "dfl2500DHCPActiveClientsPercent"),
        ("DFL2500-MIB", "dfl2500DHCPRejectedRequests"),
        ("DFL2500-MIB", "dfl2500DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl2500DHCPServerGroup.setStatus("current")

dfl2500RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 6)
)
dfl2500RuleUseGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500RuleName"),
        ("DFL2500-MIB", "dfl2500RuleUse"))
)
if mibBuilder.loadTexts:
    dfl2500RuleUseGroup.setStatus("current")

dfl2500UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 7)
)
dfl2500UserAuthGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500UserAuthHTTPUsers"),
        ("DFL2500-MIB", "dfl2500UserAuthXAUTHUsers"),
        ("DFL2500-MIB", "dfl2500UserAuthHTTPSUsers"),
        ("DFL2500-MIB", "dfl2500UserAuthPPPUsers"),
        ("DFL2500-MIB", "dfl2500UserAuthEAPUsers"),
        ("DFL2500-MIB", "dfl2500UserAuthRuleName"),
        ("DFL2500-MIB", "dfl2500UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl2500UserAuthGroup.setStatus("current")

dfl2500IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 8)
)
dfl2500IfStatsGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500IfName"),
        ("DFL2500-MIB", "dfl2500IfFragsIn"),
        ("DFL2500-MIB", "dfl2500IfFragReassOk"),
        ("DFL2500-MIB", "dfl2500IfFragReassFail"),
        ("DFL2500-MIB", "dfl2500IfPktsInCnt"),
        ("DFL2500-MIB", "dfl2500IfPktsOutCnt"),
        ("DFL2500-MIB", "dfl2500IfBitsInCnt"),
        ("DFL2500-MIB", "dfl2500IfBitsOutCnt"),
        ("DFL2500-MIB", "dfl2500IfPktsTotCnt"),
        ("DFL2500-MIB", "dfl2500IfBitsTotCnt"),
        ("DFL2500-MIB", "dfl2500IfHCPktsInCnt"),
        ("DFL2500-MIB", "dfl2500IfHCPktsOutCnt"),
        ("DFL2500-MIB", "dfl2500IfHCBitsInCnt"),
        ("DFL2500-MIB", "dfl2500IfHCBitsOutCnt"),
        ("DFL2500-MIB", "dfl2500IfHCPktsTotCnt"),
        ("DFL2500-MIB", "dfl2500IfHCBitsTotCnt"),
        ("DFL2500-MIB", "dfl2500IfRxRingFifoErrors"),
        ("DFL2500-MIB", "dfl2500IfRxDespools"),
        ("DFL2500-MIB", "dfl2500IfRxAvgUse"),
        ("DFL2500-MIB", "dfl2500IfRxRingSaturation"),
        ("DFL2500-MIB", "dfl2500RxRingFlooded"),
        ("DFL2500-MIB", "dfl2500IfTxDespools"),
        ("DFL2500-MIB", "dfl2500IfTxAvgUse"),
        ("DFL2500-MIB", "dfl2500IfTxRingSaturation"),
        ("DFL2500-MIB", "dfl2500RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl2500IfStatsGroup.setStatus("current")

dfl2500LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 9)
)
dfl2500LinkMonitorGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500LinkMonGrp"),
        ("DFL2500-MIB", "dfl2500LinkMonGrpName"),
        ("DFL2500-MIB", "dfl2500LinkMonGrpHostsUp"),
        ("DFL2500-MIB", "dfl2500LinkMonHostId"),
        ("DFL2500-MIB", "dfl2500LinkMonHostShortTermLoss"),
        ("DFL2500-MIB", "dfl2500LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl2500LinkMonitorGroup.setStatus("current")

dfl2500PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 10)
)
dfl2500PipesObjectGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500PipeUsers"),
        ("DFL2500-MIB", "dfl2500PipeName"),
        ("DFL2500-MIB", "dfl2500PipeMinPrec"),
        ("DFL2500-MIB", "dfl2500PipeMaxPrec"),
        ("DFL2500-MIB", "dfl2500PipeDefPrec"),
        ("DFL2500-MIB", "dfl2500PipeNumPrec"),
        ("DFL2500-MIB", "dfl2500PipeNumUsers"),
        ("DFL2500-MIB", "dfl2500PipeCurrentBps"),
        ("DFL2500-MIB", "dfl2500PipeCurrentPps"),
        ("DFL2500-MIB", "dfl2500PipeDelayedPackets"),
        ("DFL2500-MIB", "dfl2500PipeDropedPackets"),
        ("DFL2500-MIB", "dfl2500PipePrec"),
        ("DFL2500-MIB", "dfl2500PipePrecBps"),
        ("DFL2500-MIB", "dfl2500PipePrecTotalPps"),
        ("DFL2500-MIB", "dfl2500PipePrecReservedBps"),
        ("DFL2500-MIB", "dfl2500PipePrecDynLimBps"),
        ("DFL2500-MIB", "dfl2500PipePrecDynUsrLimBps"),
        ("DFL2500-MIB", "dfl2500PipePrecDelayedPackets"),
        ("DFL2500-MIB", "dfl2500PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl2500PipesObjectGroup.setStatus("current")

dfl2500DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 12)
)
dfl2500DHCPRelayObjectGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500DHCPRelayCurClients"),
        ("DFL2500-MIB", "dfl2500DHCPRelayCurTrans"),
        ("DFL2500-MIB", "dfl2500DHCPRelayRejected"),
        ("DFL2500-MIB", "dfl2500DHCPRelayRuleName"),
        ("DFL2500-MIB", "dfl2500DHCPRelayRuleHits"),
        ("DFL2500-MIB", "dfl2500DHCPRelayRuleCurClients"),
        ("DFL2500-MIB", "dfl2500DHCPRelayRuleRejCliPkts"),
        ("DFL2500-MIB", "dfl2500DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl2500DHCPRelayObjectGroup.setStatus("current")

dfl2500AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 13)
)
dfl2500AlgGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500AlgSessions"),
        ("DFL2500-MIB", "dfl2500AlgConnections"),
        ("DFL2500-MIB", "dfl2500AlgTCPStreams"),
        ("DFL2500-MIB", "dfl2500HttpAlgName"),
        ("DFL2500-MIB", "dfl2500HttpAlgTotalRequested"),
        ("DFL2500-MIB", "dfl2500HttpAlgTotalAllowed"),
        ("DFL2500-MIB", "dfl2500HttpAlgTotalBlocked"),
        ("DFL2500-MIB", "dfl2500HttpAlgCntFltName"),
        ("DFL2500-MIB", "dfl2500HttpAlgCntFltRequests"),
        ("DFL2500-MIB", "dfl2500HttpAlgCntFltAllowed"),
        ("DFL2500-MIB", "dfl2500HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl2500AlgGroup.setStatus("current")

dfl2500HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 14)
)
dfl2500HAGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500HASyncSendQueueLength"),
        ("DFL2500-MIB", "dfl2500HASyncSendQueueUsagePkt"),
        ("DFL2500-MIB", "dfl2500HASyncSendQueueUsageOct"),
        ("DFL2500-MIB", "dfl2500HASyncSentPackets"),
        ("DFL2500-MIB", "dfl2500HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl2500HAGroup.setStatus("current")

dfl2500IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 15)
)
dfl2500IfVlanGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500IfVlanUntaggedInPkts"),
        ("DFL2500-MIB", "dfl2500IfVlanUntaggedOutPkts"),
        ("DFL2500-MIB", "dfl2500IfVlanUntaggedTotPkts"),
        ("DFL2500-MIB", "dfl2500IfVlanUntaggedInOctets"),
        ("DFL2500-MIB", "dfl2500IfVlanUntaggedOutOctets"),
        ("DFL2500-MIB", "dfl2500IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl2500IfVlanGroup.setStatus("current")

dfl2500SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 16)
)
dfl2500SmtpAlgGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500SmtpAlgName"),
        ("DFL2500-MIB", "dfl2500SmtpAlgTotCheckedSes"),
        ("DFL2500-MIB", "dfl2500SmtpAlgTotSpamSes"),
        ("DFL2500-MIB", "dfl2500SmtpAlgTotDroppedSes"),
        ("DFL2500-MIB", "dfl2500SmtpAlgDnsBlName"),
        ("DFL2500-MIB", "dfl2500SmtpAlgDnsBlChecked"),
        ("DFL2500-MIB", "dfl2500SmtpAlgDnsBlMatched"),
        ("DFL2500-MIB", "dfl2500SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl2500SmtpAlgGroup.setStatus("current")

dfl2500SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 3, 1, 17)
)
dfl2500SysTCPGroup.setObjects(
      *(("DFL2500-MIB", "dfl2500SysTCPRecvSmall"),
        ("DFL2500-MIB", "dfl2500SysTCPRecvLarge"),
        ("DFL2500-MIB", "dfl2500SysTCPSendSmall"),
        ("DFL2500-MIB", "dfl2500SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl2500SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl2500StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 1, 5, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl2500StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL2500-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "ipsFirewall": ipsFirewall,
       "dfl2500": dfl2500,
       "dfl2500OS": dfl2500OS,
       "dfl2500OSStats": dfl2500OSStats,
       "dfl2500System": dfl2500System,
       "dfl2500SysCpuLoad": dfl2500SysCpuLoad,
       "dfl2500SysForwardedBits": dfl2500SysForwardedBits,
       "dfl2500SysForwardedPackets": dfl2500SysForwardedPackets,
       "dfl2500SysBuffUse": dfl2500SysBuffUse,
       "dfl2500SysConns": dfl2500SysConns,
       "dfl2500SysPerStateCounters": dfl2500SysPerStateCounters,
       "dfl2500SysPscTcpSyn": dfl2500SysPscTcpSyn,
       "dfl2500SysPscTcpOpen": dfl2500SysPscTcpOpen,
       "dfl2500SysPscTcpFin": dfl2500SysPscTcpFin,
       "dfl2500SysPscUdp": dfl2500SysPscUdp,
       "dfl2500SysPscIcmp": dfl2500SysPscIcmp,
       "dfl2500SysPscOther": dfl2500SysPscOther,
       "dfl2500IfStatsTable": dfl2500IfStatsTable,
       "dfl2500IfStatsEntry": dfl2500IfStatsEntry,
       "dfl2500IfStatsIndex": dfl2500IfStatsIndex,
       "dfl2500IfName": dfl2500IfName,
       "dfl2500IfFragsIn": dfl2500IfFragsIn,
       "dfl2500IfFragReassOk": dfl2500IfFragReassOk,
       "dfl2500IfFragReassFail": dfl2500IfFragReassFail,
       "dfl2500IfPktsInCnt": dfl2500IfPktsInCnt,
       "dfl2500IfPktsOutCnt": dfl2500IfPktsOutCnt,
       "dfl2500IfBitsInCnt": dfl2500IfBitsInCnt,
       "dfl2500IfBitsOutCnt": dfl2500IfBitsOutCnt,
       "dfl2500IfPktsTotCnt": dfl2500IfPktsTotCnt,
       "dfl2500IfBitsTotCnt": dfl2500IfBitsTotCnt,
       "dfl2500IfHCPktsInCnt": dfl2500IfHCPktsInCnt,
       "dfl2500IfHCPktsOutCnt": dfl2500IfHCPktsOutCnt,
       "dfl2500IfHCBitsInCnt": dfl2500IfHCBitsInCnt,
       "dfl2500IfHCBitsOutCnt": dfl2500IfHCBitsOutCnt,
       "dfl2500IfHCPktsTotCnt": dfl2500IfHCPktsTotCnt,
       "dfl2500IfHCBitsTotCnt": dfl2500IfHCBitsTotCnt,
       "dfl2500IfRxRingTable": dfl2500IfRxRingTable,
       "dfl2500IfRxRingEntry": dfl2500IfRxRingEntry,
       "dfl2500IfRxRingIndex": dfl2500IfRxRingIndex,
       "dfl2500IfRxRingFifoErrors": dfl2500IfRxRingFifoErrors,
       "dfl2500IfRxDespools": dfl2500IfRxDespools,
       "dfl2500IfRxAvgUse": dfl2500IfRxAvgUse,
       "dfl2500IfRxRingSaturation": dfl2500IfRxRingSaturation,
       "dfl2500RxRingFlooded": dfl2500RxRingFlooded,
       "dfl2500IfTxRingTable": dfl2500IfTxRingTable,
       "dfl2500IfTxRingEntry": dfl2500IfTxRingEntry,
       "dfl2500IfTxRingIndex": dfl2500IfTxRingIndex,
       "dfl2500IfTxDespools": dfl2500IfTxDespools,
       "dfl2500IfTxAvgUse": dfl2500IfTxAvgUse,
       "dfl2500IfTxRingSaturation": dfl2500IfTxRingSaturation,
       "dfl2500RxTingFlooded": dfl2500RxTingFlooded,
       "dfl2500IfVlanStatsTable": dfl2500IfVlanStatsTable,
       "dfl2500IfVlanStatsEntry": dfl2500IfVlanStatsEntry,
       "dfl2500IfVlanIndex": dfl2500IfVlanIndex,
       "dfl2500IfVlanUntaggedInPkts": dfl2500IfVlanUntaggedInPkts,
       "dfl2500IfVlanUntaggedOutPkts": dfl2500IfVlanUntaggedOutPkts,
       "dfl2500IfVlanUntaggedTotPkts": dfl2500IfVlanUntaggedTotPkts,
       "dfl2500IfVlanUntaggedInOctets": dfl2500IfVlanUntaggedInOctets,
       "dfl2500IfVlanUntaggedOutOctets": dfl2500IfVlanUntaggedOutOctets,
       "dfl2500IfVlanUntaggedTotOctets": dfl2500IfVlanUntaggedTotOctets,
       "dfl2500HWSensorTable": dfl2500HWSensorTable,
       "dfl2500HWSensorEntry": dfl2500HWSensorEntry,
       "dfl2500HWSensorIndex": dfl2500HWSensorIndex,
       "dfl2500HWSensorName": dfl2500HWSensorName,
       "dfl2500HWSensorValue": dfl2500HWSensorValue,
       "dfl2500HWSensorUnit": dfl2500HWSensorUnit,
       "dfl2500SysMemUsage": dfl2500SysMemUsage,
       "dfl2500SysTCPUsage": dfl2500SysTCPUsage,
       "dfl2500SysTCPRecvSmall": dfl2500SysTCPRecvSmall,
       "dfl2500SysTCPRecvLarge": dfl2500SysTCPRecvLarge,
       "dfl2500SysTCPSendSmall": dfl2500SysTCPSendSmall,
       "dfl2500SysTCPSendLarge": dfl2500SysTCPSendLarge,
       "dfl2500SysTimerUsage": dfl2500SysTimerUsage,
       "dfl2500SysConnOPS": dfl2500SysConnOPS,
       "dfl2500SysConnCPS": dfl2500SysConnCPS,
       "dfl2500SysHCForwardedBits": dfl2500SysHCForwardedBits,
       "dfl2500VPN": dfl2500VPN,
       "dfl2500IPsec": dfl2500IPsec,
       "dfl2500IPsecGlobal": dfl2500IPsecGlobal,
       "dfl2500IPsecPhaseOneActive": dfl2500IPsecPhaseOneActive,
       "dfl2500IPsecPhaseOneAggrModeDone": dfl2500IPsecPhaseOneAggrModeDone,
       "dfl2500IPsecQuickModeActive": dfl2500IPsecQuickModeActive,
       "dfl2500IPsecPhaseOneDone": dfl2500IPsecPhaseOneDone,
       "dfl2500IPsecPhaseOneFailed": dfl2500IPsecPhaseOneFailed,
       "dfl2500IPsecPhaseOneRekeyed": dfl2500IPsecPhaseOneRekeyed,
       "dfl2500IPsecQuickModeDone": dfl2500IPsecQuickModeDone,
       "dfl2500IPsecQuickModeFailed": dfl2500IPsecQuickModeFailed,
       "dfl2500IPsecInfoDone": dfl2500IPsecInfoDone,
       "dfl2500IPsecInfoFailed": dfl2500IPsecInfoFailed,
       "dfl2500IPsecInOctetsComp": dfl2500IPsecInOctetsComp,
       "dfl2500IPsecInOctetsUncomp": dfl2500IPsecInOctetsUncomp,
       "dfl2500IPsecOutOctetsComp": dfl2500IPsecOutOctetsComp,
       "dfl2500IPsecOutOctetsUncomp": dfl2500IPsecOutOctetsUncomp,
       "dfl2500IPsecForwardedOctetsComp": dfl2500IPsecForwardedOctetsComp,
       "dfl2500IPsecForwardedOctetsUcomp": dfl2500IPsecForwardedOctetsUcomp,
       "dfl2500IPsecInPackets": dfl2500IPsecInPackets,
       "dfl2500IPsecOutPackets": dfl2500IPsecOutPackets,
       "dfl2500IPsecForwardedPackets": dfl2500IPsecForwardedPackets,
       "dfl2500IPsecActiveTransforms": dfl2500IPsecActiveTransforms,
       "dfl2500IPsecTotalTransforms": dfl2500IPsecTotalTransforms,
       "dfl2500IPsecOutOfTransforms": dfl2500IPsecOutOfTransforms,
       "dfl2500IPsecTotalRekeys": dfl2500IPsecTotalRekeys,
       "dfl2500Rules": dfl2500Rules,
       "dfl2500RuleUseTable": dfl2500RuleUseTable,
       "dfl2500RuleUseEntry": dfl2500RuleUseEntry,
       "dfl2500RuleIndex": dfl2500RuleIndex,
       "dfl2500RuleName": dfl2500RuleName,
       "dfl2500RuleUse": dfl2500RuleUse,
       "dfl2500IPPools": dfl2500IPPools,
       "dfl2500IPPoolsNumber": dfl2500IPPoolsNumber,
       "dfl2500IPPoolTable": dfl2500IPPoolTable,
       "dfl2500IPPoolEntry": dfl2500IPPoolEntry,
       "dfl2500IPPoolIndex": dfl2500IPPoolIndex,
       "dfl2500IPPoolName": dfl2500IPPoolName,
       "dfl2500IPPoolPrepare": dfl2500IPPoolPrepare,
       "dfl2500IPPoolFree": dfl2500IPPoolFree,
       "dfl2500IPPoolMisses": dfl2500IPPoolMisses,
       "dfl2500IPPoolClientFails": dfl2500IPPoolClientFails,
       "dfl2500IPPoolUsed": dfl2500IPPoolUsed,
       "dfl2500DHCPServer": dfl2500DHCPServer,
       "dfl2500DHCPTotalRejected": dfl2500DHCPTotalRejected,
       "dfl2500DHCPRuleTable": dfl2500DHCPRuleTable,
       "dfl2500DHCPRuleEntry": dfl2500DHCPRuleEntry,
       "dfl2500DHCPRuleIndex": dfl2500DHCPRuleIndex,
       "dfl2500DHCPRuleName": dfl2500DHCPRuleName,
       "dfl2500DHCPRuleUsage": dfl2500DHCPRuleUsage,
       "dfl2500DHCPRuleUsagePercent": dfl2500DHCPRuleUsagePercent,
       "dfl2500DHCPActiveClients": dfl2500DHCPActiveClients,
       "dfl2500DHCPActiveClientsPercent": dfl2500DHCPActiveClientsPercent,
       "dfl2500DHCPRejectedRequests": dfl2500DHCPRejectedRequests,
       "dfl2500DHCPTotalLeases": dfl2500DHCPTotalLeases,
       "dfl2500UserAuth": dfl2500UserAuth,
       "dfl2500UserAuthHTTPUsers": dfl2500UserAuthHTTPUsers,
       "dfl2500UserAuthXAUTHUsers": dfl2500UserAuthXAUTHUsers,
       "dfl2500UserAuthHTTPSUsers": dfl2500UserAuthHTTPSUsers,
       "dfl2500UserAuthPPPUsers": dfl2500UserAuthPPPUsers,
       "dfl2500UserAuthEAPUsers": dfl2500UserAuthEAPUsers,
       "dfl2500UserAuthRuleUseTable": dfl2500UserAuthRuleUseTable,
       "dfl2500UserAuthRuleUseEntry": dfl2500UserAuthRuleUseEntry,
       "dfl2500UserAuthRuleIndex": dfl2500UserAuthRuleIndex,
       "dfl2500UserAuthRuleName": dfl2500UserAuthRuleName,
       "dfl2500UserAuthRuleUse": dfl2500UserAuthRuleUse,
       "dfl2500LinkMonitor": dfl2500LinkMonitor,
       "dfl2500LinkMonGrp": dfl2500LinkMonGrp,
       "dfl2500LinkMonGrpTable": dfl2500LinkMonGrpTable,
       "dfl2500LinkMonGrpEntry": dfl2500LinkMonGrpEntry,
       "dfl2500LinkMonGrpIndex": dfl2500LinkMonGrpIndex,
       "dfl2500LinkMonGrpName": dfl2500LinkMonGrpName,
       "dfl2500LinkMonGrpHostsUp": dfl2500LinkMonGrpHostsUp,
       "dfl2500LinkMonHostTable": dfl2500LinkMonHostTable,
       "dfl2500LinkMonHostEntry": dfl2500LinkMonHostEntry,
       "dfl2500LinkMonHostIndex": dfl2500LinkMonHostIndex,
       "dfl2500LinkMonHostId": dfl2500LinkMonHostId,
       "dfl2500LinkMonHostShortTermLoss": dfl2500LinkMonHostShortTermLoss,
       "dfl2500LinkMonHostPacketsLost": dfl2500LinkMonHostPacketsLost,
       "dfl2500Pipes": dfl2500Pipes,
       "dfl2500PipeUsers": dfl2500PipeUsers,
       "dfl2500PipeTable": dfl2500PipeTable,
       "dfl2500PipeEntry": dfl2500PipeEntry,
       "dfl2500PipeIndex": dfl2500PipeIndex,
       "dfl2500PipeName": dfl2500PipeName,
       "dfl2500PipeMinPrec": dfl2500PipeMinPrec,
       "dfl2500PipeMaxPrec": dfl2500PipeMaxPrec,
       "dfl2500PipeDefPrec": dfl2500PipeDefPrec,
       "dfl2500PipeNumPrec": dfl2500PipeNumPrec,
       "dfl2500PipeNumUsers": dfl2500PipeNumUsers,
       "dfl2500PipeCurrentBps": dfl2500PipeCurrentBps,
       "dfl2500PipeCurrentPps": dfl2500PipeCurrentPps,
       "dfl2500PipeDelayedPackets": dfl2500PipeDelayedPackets,
       "dfl2500PipeDropedPackets": dfl2500PipeDropedPackets,
       "dfl2500PipePrecTable": dfl2500PipePrecTable,
       "dfl2500PipePrecEntry": dfl2500PipePrecEntry,
       "dfl2500PipePrecIndex": dfl2500PipePrecIndex,
       "dfl2500PipePrec": dfl2500PipePrec,
       "dfl2500PipePrecBps": dfl2500PipePrecBps,
       "dfl2500PipePrecTotalPps": dfl2500PipePrecTotalPps,
       "dfl2500PipePrecReservedBps": dfl2500PipePrecReservedBps,
       "dfl2500PipePrecDynLimBps": dfl2500PipePrecDynLimBps,
       "dfl2500PipePrecDynUsrLimBps": dfl2500PipePrecDynUsrLimBps,
       "dfl2500PipePrecDelayedPackets": dfl2500PipePrecDelayedPackets,
       "dfl2500PipePrecDropedPackets": dfl2500PipePrecDropedPackets,
       "dfl2500ALG": dfl2500ALG,
       "dfl2500AlgSessions": dfl2500AlgSessions,
       "dfl2500AlgConnections": dfl2500AlgConnections,
       "dfl2500AlgTCPStreams": dfl2500AlgTCPStreams,
       "dfl2500HttpAlg": dfl2500HttpAlg,
       "dfl2500HttpAlgTable": dfl2500HttpAlgTable,
       "dfl2500HttpAlgEntry": dfl2500HttpAlgEntry,
       "dfl2500HttpAlgIndex": dfl2500HttpAlgIndex,
       "dfl2500HttpAlgName": dfl2500HttpAlgName,
       "dfl2500HttpAlgTotalRequested": dfl2500HttpAlgTotalRequested,
       "dfl2500HttpAlgTotalAllowed": dfl2500HttpAlgTotalAllowed,
       "dfl2500HttpAlgTotalBlocked": dfl2500HttpAlgTotalBlocked,
       "dfl2500HttpAlgCntFltTable": dfl2500HttpAlgCntFltTable,
       "dfl2500HttpAlgCntFltEntry": dfl2500HttpAlgCntFltEntry,
       "dfl2500HttpAlgCntFltIndex": dfl2500HttpAlgCntFltIndex,
       "dfl2500HttpAlgCntFltName": dfl2500HttpAlgCntFltName,
       "dfl2500HttpAlgCntFltRequests": dfl2500HttpAlgCntFltRequests,
       "dfl2500HttpAlgCntFltAllowed": dfl2500HttpAlgCntFltAllowed,
       "dfl2500HttpAlgCntFltBlocked": dfl2500HttpAlgCntFltBlocked,
       "dfl2500SmtpAlg": dfl2500SmtpAlg,
       "dfl2500SmtpAlgTable": dfl2500SmtpAlgTable,
       "dfl2500SmtpAlgEntry": dfl2500SmtpAlgEntry,
       "dfl2500SmtpAlgIndex": dfl2500SmtpAlgIndex,
       "dfl2500SmtpAlgName": dfl2500SmtpAlgName,
       "dfl2500SmtpAlgTotCheckedSes": dfl2500SmtpAlgTotCheckedSes,
       "dfl2500SmtpAlgTotSpamSes": dfl2500SmtpAlgTotSpamSes,
       "dfl2500SmtpAlgTotDroppedSes": dfl2500SmtpAlgTotDroppedSes,
       "dfl2500SmtpAlgDnsBlTable": dfl2500SmtpAlgDnsBlTable,
       "dfl2500SmtpAlgDnsBlEntry": dfl2500SmtpAlgDnsBlEntry,
       "dfl2500SmtpAlgDnsBlIndex": dfl2500SmtpAlgDnsBlIndex,
       "dfl2500SmtpAlgDnsBlName": dfl2500SmtpAlgDnsBlName,
       "dfl2500SmtpAlgDnsBlChecked": dfl2500SmtpAlgDnsBlChecked,
       "dfl2500SmtpAlgDnsBlMatched": dfl2500SmtpAlgDnsBlMatched,
       "dfl2500SmtpAlgDnsBlFailChecks": dfl2500SmtpAlgDnsBlFailChecks,
       "dfl2500DHCPRelay": dfl2500DHCPRelay,
       "dfl2500DHCPRelayCurClients": dfl2500DHCPRelayCurClients,
       "dfl2500DHCPRelayCurTrans": dfl2500DHCPRelayCurTrans,
       "dfl2500DHCPRelayRejected": dfl2500DHCPRelayRejected,
       "dfl2500DHCPRelayRuleTable": dfl2500DHCPRelayRuleTable,
       "dfl2500DHCPRelayRuleEntry": dfl2500DHCPRelayRuleEntry,
       "dfl2500DHCPRelayRuleIndex": dfl2500DHCPRelayRuleIndex,
       "dfl2500DHCPRelayRuleName": dfl2500DHCPRelayRuleName,
       "dfl2500DHCPRelayRuleHits": dfl2500DHCPRelayRuleHits,
       "dfl2500DHCPRelayRuleCurClients": dfl2500DHCPRelayRuleCurClients,
       "dfl2500DHCPRelayRuleRejCliPkts": dfl2500DHCPRelayRuleRejCliPkts,
       "dfl2500DHCPRelayRuleRejSrvPkts": dfl2500DHCPRelayRuleRejSrvPkts,
       "dfl2500HA": dfl2500HA,
       "dfl2500HASyncSendQueueLength": dfl2500HASyncSendQueueLength,
       "dfl2500HASyncSendQueueUsagePkt": dfl2500HASyncSendQueueUsagePkt,
       "dfl2500HASyncSendQueueUsageOct": dfl2500HASyncSendQueueUsageOct,
       "dfl2500HASyncSentPackets": dfl2500HASyncSentPackets,
       "dfl2500HASyncSendResentPackets": dfl2500HASyncSendResentPackets,
       "dfl2500reg": dfl2500reg,
       "dfl2500MibModules": dfl2500MibModules,
       "dfl2500-MIB": dfl2500_MIB,
       "dfl2500MibConfs": dfl2500MibConfs,
       "dfl2500StatsConformance": dfl2500StatsConformance,
       "dfl2500StatsCompliance": dfl2500StatsCompliance,
       "dfl2500MibObjectGroups": dfl2500MibObjectGroups,
       "dfl2500StatsRegGroups": dfl2500StatsRegGroups,
       "dfl2500SystemObjectGroup": dfl2500SystemObjectGroup,
       "dfl2500IPsecObjectGroup": dfl2500IPsecObjectGroup,
       "dfl2500StateCountersGroup": dfl2500StateCountersGroup,
       "dfl2500IPPoolGroup": dfl2500IPPoolGroup,
       "dfl2500DHCPServerGroup": dfl2500DHCPServerGroup,
       "dfl2500RuleUseGroup": dfl2500RuleUseGroup,
       "dfl2500UserAuthGroup": dfl2500UserAuthGroup,
       "dfl2500IfStatsGroup": dfl2500IfStatsGroup,
       "dfl2500LinkMonitorGroup": dfl2500LinkMonitorGroup,
       "dfl2500PipesObjectGroup": dfl2500PipesObjectGroup,
       "dfl2500DHCPRelayObjectGroup": dfl2500DHCPRelayObjectGroup,
       "dfl2500AlgGroup": dfl2500AlgGroup,
       "dfl2500HAGroup": dfl2500HAGroup,
       "dfl2500IfVlanGroup": dfl2500IfVlanGroup,
       "dfl2500SmtpAlgGroup": dfl2500SmtpAlgGroup,
       "dfl2500SysTCPGroup": dfl2500SysTCPGroup}
)
