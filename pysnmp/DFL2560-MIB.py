# SNMP MIB module (DFL2560-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL2560-MIB
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

dfl2560_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 1, 2)
)
dfl2560_MIB.setRevisions(
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
_Dfl2560_ObjectIdentity = ObjectIdentity
dfl2560 = _Dfl2560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4)
)
_Dfl2560OS_ObjectIdentity = ObjectIdentity
dfl2560OS = _Dfl2560OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1)
)
_Dfl2560OSStats_ObjectIdentity = ObjectIdentity
dfl2560OSStats = _Dfl2560OSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2)
)
_Dfl2560System_ObjectIdentity = ObjectIdentity
dfl2560System = _Dfl2560System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1)
)
_Dfl2560SysCpuLoad_Type = Gauge32
_Dfl2560SysCpuLoad_Object = MibScalar
dfl2560SysCpuLoad = _Dfl2560SysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 1),
    _Dfl2560SysCpuLoad_Type()
)
dfl2560SysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysCpuLoad.setStatus("current")
_Dfl2560SysForwardedBits_Type = Counter32
_Dfl2560SysForwardedBits_Object = MibScalar
dfl2560SysForwardedBits = _Dfl2560SysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 2),
    _Dfl2560SysForwardedBits_Type()
)
dfl2560SysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysForwardedBits.setStatus("current")
_Dfl2560SysForwardedPackets_Type = Counter32
_Dfl2560SysForwardedPackets_Object = MibScalar
dfl2560SysForwardedPackets = _Dfl2560SysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 3),
    _Dfl2560SysForwardedPackets_Type()
)
dfl2560SysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysForwardedPackets.setStatus("current")
_Dfl2560SysBuffUse_Type = Gauge32
_Dfl2560SysBuffUse_Object = MibScalar
dfl2560SysBuffUse = _Dfl2560SysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 4),
    _Dfl2560SysBuffUse_Type()
)
dfl2560SysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysBuffUse.setStatus("current")
_Dfl2560SysConns_Type = Gauge32
_Dfl2560SysConns_Object = MibScalar
dfl2560SysConns = _Dfl2560SysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 5),
    _Dfl2560SysConns_Type()
)
dfl2560SysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysConns.setStatus("current")
_Dfl2560SysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl2560SysPerStateCounters = _Dfl2560SysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6)
)
_Dfl2560SysPscTcpSyn_Type = Gauge32
_Dfl2560SysPscTcpSyn_Object = MibScalar
dfl2560SysPscTcpSyn = _Dfl2560SysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6, 1),
    _Dfl2560SysPscTcpSyn_Type()
)
dfl2560SysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysPscTcpSyn.setStatus("current")
_Dfl2560SysPscTcpOpen_Type = Gauge32
_Dfl2560SysPscTcpOpen_Object = MibScalar
dfl2560SysPscTcpOpen = _Dfl2560SysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6, 2),
    _Dfl2560SysPscTcpOpen_Type()
)
dfl2560SysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysPscTcpOpen.setStatus("current")
_Dfl2560SysPscTcpFin_Type = Gauge32
_Dfl2560SysPscTcpFin_Object = MibScalar
dfl2560SysPscTcpFin = _Dfl2560SysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6, 3),
    _Dfl2560SysPscTcpFin_Type()
)
dfl2560SysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysPscTcpFin.setStatus("current")
_Dfl2560SysPscUdp_Type = Gauge32
_Dfl2560SysPscUdp_Object = MibScalar
dfl2560SysPscUdp = _Dfl2560SysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6, 4),
    _Dfl2560SysPscUdp_Type()
)
dfl2560SysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysPscUdp.setStatus("current")
_Dfl2560SysPscIcmp_Type = Gauge32
_Dfl2560SysPscIcmp_Object = MibScalar
dfl2560SysPscIcmp = _Dfl2560SysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6, 5),
    _Dfl2560SysPscIcmp_Type()
)
dfl2560SysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysPscIcmp.setStatus("current")
_Dfl2560SysPscOther_Type = Gauge32
_Dfl2560SysPscOther_Object = MibScalar
dfl2560SysPscOther = _Dfl2560SysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 6, 6),
    _Dfl2560SysPscOther_Type()
)
dfl2560SysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysPscOther.setStatus("current")
_Dfl2560IfStatsTable_Object = MibTable
dfl2560IfStatsTable = _Dfl2560IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl2560IfStatsTable.setStatus("current")
_Dfl2560IfStatsEntry_Object = MibTableRow
dfl2560IfStatsEntry = _Dfl2560IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1)
)
dfl2560IfStatsEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560IfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl2560IfStatsEntry.setStatus("current")


class _Dfl2560IfStatsIndex_Type(Integer32):
    """Custom type dfl2560IfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560IfStatsIndex_Type.__name__ = "Integer32"
_Dfl2560IfStatsIndex_Object = MibTableColumn
dfl2560IfStatsIndex = _Dfl2560IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 1),
    _Dfl2560IfStatsIndex_Type()
)
dfl2560IfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560IfStatsIndex.setStatus("current")
_Dfl2560IfName_Type = DisplayString
_Dfl2560IfName_Object = MibTableColumn
dfl2560IfName = _Dfl2560IfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 2),
    _Dfl2560IfName_Type()
)
dfl2560IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfName.setStatus("current")
_Dfl2560IfFragsIn_Type = Counter32
_Dfl2560IfFragsIn_Object = MibTableColumn
dfl2560IfFragsIn = _Dfl2560IfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 3),
    _Dfl2560IfFragsIn_Type()
)
dfl2560IfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfFragsIn.setStatus("current")
_Dfl2560IfFragReassOk_Type = Counter32
_Dfl2560IfFragReassOk_Object = MibTableColumn
dfl2560IfFragReassOk = _Dfl2560IfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 4),
    _Dfl2560IfFragReassOk_Type()
)
dfl2560IfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfFragReassOk.setStatus("current")
_Dfl2560IfFragReassFail_Type = Counter32
_Dfl2560IfFragReassFail_Object = MibTableColumn
dfl2560IfFragReassFail = _Dfl2560IfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 5),
    _Dfl2560IfFragReassFail_Type()
)
dfl2560IfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfFragReassFail.setStatus("current")
_Dfl2560IfPktsInCnt_Type = Counter32
_Dfl2560IfPktsInCnt_Object = MibTableColumn
dfl2560IfPktsInCnt = _Dfl2560IfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 6),
    _Dfl2560IfPktsInCnt_Type()
)
dfl2560IfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfPktsInCnt.setStatus("current")
_Dfl2560IfPktsOutCnt_Type = Counter32
_Dfl2560IfPktsOutCnt_Object = MibTableColumn
dfl2560IfPktsOutCnt = _Dfl2560IfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 7),
    _Dfl2560IfPktsOutCnt_Type()
)
dfl2560IfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfPktsOutCnt.setStatus("current")
_Dfl2560IfBitsInCnt_Type = Counter32
_Dfl2560IfBitsInCnt_Object = MibTableColumn
dfl2560IfBitsInCnt = _Dfl2560IfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 8),
    _Dfl2560IfBitsInCnt_Type()
)
dfl2560IfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfBitsInCnt.setStatus("current")
_Dfl2560IfBitsOutCnt_Type = Counter32
_Dfl2560IfBitsOutCnt_Object = MibTableColumn
dfl2560IfBitsOutCnt = _Dfl2560IfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 9),
    _Dfl2560IfBitsOutCnt_Type()
)
dfl2560IfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfBitsOutCnt.setStatus("current")
_Dfl2560IfPktsTotCnt_Type = Counter32
_Dfl2560IfPktsTotCnt_Object = MibTableColumn
dfl2560IfPktsTotCnt = _Dfl2560IfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 10),
    _Dfl2560IfPktsTotCnt_Type()
)
dfl2560IfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfPktsTotCnt.setStatus("current")
_Dfl2560IfBitsTotCnt_Type = Counter32
_Dfl2560IfBitsTotCnt_Object = MibTableColumn
dfl2560IfBitsTotCnt = _Dfl2560IfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 11),
    _Dfl2560IfBitsTotCnt_Type()
)
dfl2560IfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfBitsTotCnt.setStatus("current")
_Dfl2560IfHCPktsInCnt_Type = Counter64
_Dfl2560IfHCPktsInCnt_Object = MibTableColumn
dfl2560IfHCPktsInCnt = _Dfl2560IfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 12),
    _Dfl2560IfHCPktsInCnt_Type()
)
dfl2560IfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfHCPktsInCnt.setStatus("current")
_Dfl2560IfHCPktsOutCnt_Type = Counter64
_Dfl2560IfHCPktsOutCnt_Object = MibTableColumn
dfl2560IfHCPktsOutCnt = _Dfl2560IfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 13),
    _Dfl2560IfHCPktsOutCnt_Type()
)
dfl2560IfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfHCPktsOutCnt.setStatus("current")
_Dfl2560IfHCBitsInCnt_Type = Counter64
_Dfl2560IfHCBitsInCnt_Object = MibTableColumn
dfl2560IfHCBitsInCnt = _Dfl2560IfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 14),
    _Dfl2560IfHCBitsInCnt_Type()
)
dfl2560IfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfHCBitsInCnt.setStatus("current")
_Dfl2560IfHCBitsOutCnt_Type = Counter64
_Dfl2560IfHCBitsOutCnt_Object = MibTableColumn
dfl2560IfHCBitsOutCnt = _Dfl2560IfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 15),
    _Dfl2560IfHCBitsOutCnt_Type()
)
dfl2560IfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfHCBitsOutCnt.setStatus("current")
_Dfl2560IfHCPktsTotCnt_Type = Counter64
_Dfl2560IfHCPktsTotCnt_Object = MibTableColumn
dfl2560IfHCPktsTotCnt = _Dfl2560IfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 16),
    _Dfl2560IfHCPktsTotCnt_Type()
)
dfl2560IfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfHCPktsTotCnt.setStatus("current")
_Dfl2560IfHCBitsTotCnt_Type = Counter64
_Dfl2560IfHCBitsTotCnt_Object = MibTableColumn
dfl2560IfHCBitsTotCnt = _Dfl2560IfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 7, 1, 17),
    _Dfl2560IfHCBitsTotCnt_Type()
)
dfl2560IfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfHCBitsTotCnt.setStatus("current")
_Dfl2560IfRxRingTable_Object = MibTable
dfl2560IfRxRingTable = _Dfl2560IfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl2560IfRxRingTable.setStatus("current")
_Dfl2560IfRxRingEntry_Object = MibTableRow
dfl2560IfRxRingEntry = _Dfl2560IfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1)
)
dfl2560IfRxRingEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560IfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl2560IfRxRingEntry.setStatus("current")


class _Dfl2560IfRxRingIndex_Type(Integer32):
    """Custom type dfl2560IfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560IfRxRingIndex_Type.__name__ = "Integer32"
_Dfl2560IfRxRingIndex_Object = MibTableColumn
dfl2560IfRxRingIndex = _Dfl2560IfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1, 1),
    _Dfl2560IfRxRingIndex_Type()
)
dfl2560IfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560IfRxRingIndex.setStatus("current")
_Dfl2560IfRxRingFifoErrors_Type = Counter32
_Dfl2560IfRxRingFifoErrors_Object = MibTableColumn
dfl2560IfRxRingFifoErrors = _Dfl2560IfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1, 2),
    _Dfl2560IfRxRingFifoErrors_Type()
)
dfl2560IfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfRxRingFifoErrors.setStatus("current")
_Dfl2560IfRxDespools_Type = Gauge32
_Dfl2560IfRxDespools_Object = MibTableColumn
dfl2560IfRxDespools = _Dfl2560IfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1, 3),
    _Dfl2560IfRxDespools_Type()
)
dfl2560IfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfRxDespools.setStatus("current")
_Dfl2560IfRxAvgUse_Type = Gauge32
_Dfl2560IfRxAvgUse_Object = MibTableColumn
dfl2560IfRxAvgUse = _Dfl2560IfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1, 4),
    _Dfl2560IfRxAvgUse_Type()
)
dfl2560IfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfRxAvgUse.setStatus("current")
_Dfl2560IfRxRingSaturation_Type = Gauge32
_Dfl2560IfRxRingSaturation_Object = MibTableColumn
dfl2560IfRxRingSaturation = _Dfl2560IfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1, 5),
    _Dfl2560IfRxRingSaturation_Type()
)
dfl2560IfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfRxRingSaturation.setStatus("current")
_Dfl2560RxRingFlooded_Type = Gauge32
_Dfl2560RxRingFlooded_Object = MibTableColumn
dfl2560RxRingFlooded = _Dfl2560RxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 8, 1, 6),
    _Dfl2560RxRingFlooded_Type()
)
dfl2560RxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560RxRingFlooded.setStatus("current")
_Dfl2560IfTxRingTable_Object = MibTable
dfl2560IfTxRingTable = _Dfl2560IfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl2560IfTxRingTable.setStatus("current")
_Dfl2560IfTxRingEntry_Object = MibTableRow
dfl2560IfTxRingEntry = _Dfl2560IfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9, 1)
)
dfl2560IfTxRingEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560IfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl2560IfTxRingEntry.setStatus("current")


class _Dfl2560IfTxRingIndex_Type(Integer32):
    """Custom type dfl2560IfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560IfTxRingIndex_Type.__name__ = "Integer32"
_Dfl2560IfTxRingIndex_Object = MibTableColumn
dfl2560IfTxRingIndex = _Dfl2560IfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9, 1, 1),
    _Dfl2560IfTxRingIndex_Type()
)
dfl2560IfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560IfTxRingIndex.setStatus("current")
_Dfl2560IfTxDespools_Type = Gauge32
_Dfl2560IfTxDespools_Object = MibTableColumn
dfl2560IfTxDespools = _Dfl2560IfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9, 1, 2),
    _Dfl2560IfTxDespools_Type()
)
dfl2560IfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfTxDespools.setStatus("current")
_Dfl2560IfTxAvgUse_Type = Gauge32
_Dfl2560IfTxAvgUse_Object = MibTableColumn
dfl2560IfTxAvgUse = _Dfl2560IfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9, 1, 3),
    _Dfl2560IfTxAvgUse_Type()
)
dfl2560IfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfTxAvgUse.setStatus("current")
_Dfl2560IfTxRingSaturation_Type = Gauge32
_Dfl2560IfTxRingSaturation_Object = MibTableColumn
dfl2560IfTxRingSaturation = _Dfl2560IfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9, 1, 4),
    _Dfl2560IfTxRingSaturation_Type()
)
dfl2560IfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfTxRingSaturation.setStatus("current")
_Dfl2560RxTingFlooded_Type = Gauge32
_Dfl2560RxTingFlooded_Object = MibTableColumn
dfl2560RxTingFlooded = _Dfl2560RxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 9, 1, 5),
    _Dfl2560RxTingFlooded_Type()
)
dfl2560RxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560RxTingFlooded.setStatus("current")
_Dfl2560IfVlanStatsTable_Object = MibTable
dfl2560IfVlanStatsTable = _Dfl2560IfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl2560IfVlanStatsTable.setStatus("current")
_Dfl2560IfVlanStatsEntry_Object = MibTableRow
dfl2560IfVlanStatsEntry = _Dfl2560IfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1)
)
dfl2560IfVlanStatsEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560IfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl2560IfVlanStatsEntry.setStatus("current")


class _Dfl2560IfVlanIndex_Type(Integer32):
    """Custom type dfl2560IfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560IfVlanIndex_Type.__name__ = "Integer32"
_Dfl2560IfVlanIndex_Object = MibTableColumn
dfl2560IfVlanIndex = _Dfl2560IfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 1),
    _Dfl2560IfVlanIndex_Type()
)
dfl2560IfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560IfVlanIndex.setStatus("current")
_Dfl2560IfVlanUntaggedInPkts_Type = Counter32
_Dfl2560IfVlanUntaggedInPkts_Object = MibTableColumn
dfl2560IfVlanUntaggedInPkts = _Dfl2560IfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 2),
    _Dfl2560IfVlanUntaggedInPkts_Type()
)
dfl2560IfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfVlanUntaggedInPkts.setStatus("current")
_Dfl2560IfVlanUntaggedOutPkts_Type = Counter32
_Dfl2560IfVlanUntaggedOutPkts_Object = MibTableColumn
dfl2560IfVlanUntaggedOutPkts = _Dfl2560IfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 3),
    _Dfl2560IfVlanUntaggedOutPkts_Type()
)
dfl2560IfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfVlanUntaggedOutPkts.setStatus("current")
_Dfl2560IfVlanUntaggedTotPkts_Type = Counter32
_Dfl2560IfVlanUntaggedTotPkts_Object = MibTableColumn
dfl2560IfVlanUntaggedTotPkts = _Dfl2560IfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 4),
    _Dfl2560IfVlanUntaggedTotPkts_Type()
)
dfl2560IfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfVlanUntaggedTotPkts.setStatus("current")
_Dfl2560IfVlanUntaggedInOctets_Type = Counter32
_Dfl2560IfVlanUntaggedInOctets_Object = MibTableColumn
dfl2560IfVlanUntaggedInOctets = _Dfl2560IfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 5),
    _Dfl2560IfVlanUntaggedInOctets_Type()
)
dfl2560IfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfVlanUntaggedInOctets.setStatus("current")
_Dfl2560IfVlanUntaggedOutOctets_Type = Counter32
_Dfl2560IfVlanUntaggedOutOctets_Object = MibTableColumn
dfl2560IfVlanUntaggedOutOctets = _Dfl2560IfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 6),
    _Dfl2560IfVlanUntaggedOutOctets_Type()
)
dfl2560IfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfVlanUntaggedOutOctets.setStatus("current")
_Dfl2560IfVlanUntaggedTotOctets_Type = Counter32
_Dfl2560IfVlanUntaggedTotOctets_Object = MibTableColumn
dfl2560IfVlanUntaggedTotOctets = _Dfl2560IfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 10, 1, 7),
    _Dfl2560IfVlanUntaggedTotOctets_Type()
)
dfl2560IfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IfVlanUntaggedTotOctets.setStatus("current")
_Dfl2560HWSensorTable_Object = MibTable
dfl2560HWSensorTable = _Dfl2560HWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl2560HWSensorTable.setStatus("current")
_Dfl2560HWSensorEntry_Object = MibTableRow
dfl2560HWSensorEntry = _Dfl2560HWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 11, 1)
)
dfl2560HWSensorEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560HWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl2560HWSensorEntry.setStatus("current")


class _Dfl2560HWSensorIndex_Type(Integer32):
    """Custom type dfl2560HWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560HWSensorIndex_Type.__name__ = "Integer32"
_Dfl2560HWSensorIndex_Object = MibTableColumn
dfl2560HWSensorIndex = _Dfl2560HWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 11, 1, 1),
    _Dfl2560HWSensorIndex_Type()
)
dfl2560HWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560HWSensorIndex.setStatus("current")
_Dfl2560HWSensorName_Type = DisplayString
_Dfl2560HWSensorName_Object = MibTableColumn
dfl2560HWSensorName = _Dfl2560HWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 11, 1, 2),
    _Dfl2560HWSensorName_Type()
)
dfl2560HWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HWSensorName.setStatus("current")
_Dfl2560HWSensorValue_Type = Gauge32
_Dfl2560HWSensorValue_Object = MibTableColumn
dfl2560HWSensorValue = _Dfl2560HWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 11, 1, 3),
    _Dfl2560HWSensorValue_Type()
)
dfl2560HWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HWSensorValue.setStatus("current")
_Dfl2560HWSensorUnit_Type = DisplayString
_Dfl2560HWSensorUnit_Object = MibTableColumn
dfl2560HWSensorUnit = _Dfl2560HWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 11, 1, 4),
    _Dfl2560HWSensorUnit_Type()
)
dfl2560HWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HWSensorUnit.setStatus("current")
_Dfl2560SysMemUsage_Type = Gauge32
_Dfl2560SysMemUsage_Object = MibScalar
dfl2560SysMemUsage = _Dfl2560SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 12),
    _Dfl2560SysMemUsage_Type()
)
dfl2560SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysMemUsage.setStatus("current")
_Dfl2560SysTCPUsage_ObjectIdentity = ObjectIdentity
dfl2560SysTCPUsage = _Dfl2560SysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 13)
)
_Dfl2560SysTCPRecvSmall_Type = Gauge32
_Dfl2560SysTCPRecvSmall_Object = MibScalar
dfl2560SysTCPRecvSmall = _Dfl2560SysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 13, 1),
    _Dfl2560SysTCPRecvSmall_Type()
)
dfl2560SysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysTCPRecvSmall.setStatus("current")
_Dfl2560SysTCPRecvLarge_Type = Gauge32
_Dfl2560SysTCPRecvLarge_Object = MibScalar
dfl2560SysTCPRecvLarge = _Dfl2560SysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 13, 2),
    _Dfl2560SysTCPRecvLarge_Type()
)
dfl2560SysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysTCPRecvLarge.setStatus("current")
_Dfl2560SysTCPSendSmall_Type = Gauge32
_Dfl2560SysTCPSendSmall_Object = MibScalar
dfl2560SysTCPSendSmall = _Dfl2560SysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 13, 3),
    _Dfl2560SysTCPSendSmall_Type()
)
dfl2560SysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysTCPSendSmall.setStatus("current")
_Dfl2560SysTCPSendLarge_Type = Gauge32
_Dfl2560SysTCPSendLarge_Object = MibScalar
dfl2560SysTCPSendLarge = _Dfl2560SysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 13, 4),
    _Dfl2560SysTCPSendLarge_Type()
)
dfl2560SysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysTCPSendLarge.setStatus("current")
_Dfl2560SysTimerUsage_Type = Gauge32
_Dfl2560SysTimerUsage_Object = MibScalar
dfl2560SysTimerUsage = _Dfl2560SysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 14),
    _Dfl2560SysTimerUsage_Type()
)
dfl2560SysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysTimerUsage.setStatus("current")
_Dfl2560SysConnOPS_Type = Gauge32
_Dfl2560SysConnOPS_Object = MibScalar
dfl2560SysConnOPS = _Dfl2560SysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 15),
    _Dfl2560SysConnOPS_Type()
)
dfl2560SysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysConnOPS.setStatus("current")
_Dfl2560SysConnCPS_Type = Gauge32
_Dfl2560SysConnCPS_Object = MibScalar
dfl2560SysConnCPS = _Dfl2560SysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 16),
    _Dfl2560SysConnCPS_Type()
)
dfl2560SysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysConnCPS.setStatus("current")
_Dfl2560SysHCForwardedBits_Type = Counter64
_Dfl2560SysHCForwardedBits_Object = MibScalar
dfl2560SysHCForwardedBits = _Dfl2560SysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 1, 17),
    _Dfl2560SysHCForwardedBits_Type()
)
dfl2560SysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SysHCForwardedBits.setStatus("current")
_Dfl2560VPN_ObjectIdentity = ObjectIdentity
dfl2560VPN = _Dfl2560VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2)
)
_Dfl2560IPsec_ObjectIdentity = ObjectIdentity
dfl2560IPsec = _Dfl2560IPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1)
)
_Dfl2560IPsecGlobal_ObjectIdentity = ObjectIdentity
dfl2560IPsecGlobal = _Dfl2560IPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1)
)
_Dfl2560IPsecPhaseOneActive_Type = Gauge32
_Dfl2560IPsecPhaseOneActive_Object = MibScalar
dfl2560IPsecPhaseOneActive = _Dfl2560IPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 1),
    _Dfl2560IPsecPhaseOneActive_Type()
)
dfl2560IPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecPhaseOneActive.setStatus("current")
_Dfl2560IPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl2560IPsecPhaseOneAggrModeDone_Object = MibScalar
dfl2560IPsecPhaseOneAggrModeDone = _Dfl2560IPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 2),
    _Dfl2560IPsecPhaseOneAggrModeDone_Type()
)
dfl2560IPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl2560IPsecQuickModeActive_Type = Gauge32
_Dfl2560IPsecQuickModeActive_Object = MibScalar
dfl2560IPsecQuickModeActive = _Dfl2560IPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 3),
    _Dfl2560IPsecQuickModeActive_Type()
)
dfl2560IPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecQuickModeActive.setStatus("current")
_Dfl2560IPsecPhaseOneDone_Type = Counter32
_Dfl2560IPsecPhaseOneDone_Object = MibScalar
dfl2560IPsecPhaseOneDone = _Dfl2560IPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 4),
    _Dfl2560IPsecPhaseOneDone_Type()
)
dfl2560IPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecPhaseOneDone.setStatus("current")
_Dfl2560IPsecPhaseOneFailed_Type = Counter32
_Dfl2560IPsecPhaseOneFailed_Object = MibScalar
dfl2560IPsecPhaseOneFailed = _Dfl2560IPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 5),
    _Dfl2560IPsecPhaseOneFailed_Type()
)
dfl2560IPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecPhaseOneFailed.setStatus("current")
_Dfl2560IPsecPhaseOneRekeyed_Type = Counter32
_Dfl2560IPsecPhaseOneRekeyed_Object = MibScalar
dfl2560IPsecPhaseOneRekeyed = _Dfl2560IPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 6),
    _Dfl2560IPsecPhaseOneRekeyed_Type()
)
dfl2560IPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecPhaseOneRekeyed.setStatus("current")
_Dfl2560IPsecQuickModeDone_Type = Counter32
_Dfl2560IPsecQuickModeDone_Object = MibScalar
dfl2560IPsecQuickModeDone = _Dfl2560IPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 7),
    _Dfl2560IPsecQuickModeDone_Type()
)
dfl2560IPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecQuickModeDone.setStatus("current")
_Dfl2560IPsecQuickModeFailed_Type = Counter32
_Dfl2560IPsecQuickModeFailed_Object = MibScalar
dfl2560IPsecQuickModeFailed = _Dfl2560IPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 8),
    _Dfl2560IPsecQuickModeFailed_Type()
)
dfl2560IPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecQuickModeFailed.setStatus("current")
_Dfl2560IPsecInfoDone_Type = Counter32
_Dfl2560IPsecInfoDone_Object = MibScalar
dfl2560IPsecInfoDone = _Dfl2560IPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 9),
    _Dfl2560IPsecInfoDone_Type()
)
dfl2560IPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecInfoDone.setStatus("current")
_Dfl2560IPsecInfoFailed_Type = Counter32
_Dfl2560IPsecInfoFailed_Object = MibScalar
dfl2560IPsecInfoFailed = _Dfl2560IPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 10),
    _Dfl2560IPsecInfoFailed_Type()
)
dfl2560IPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecInfoFailed.setStatus("current")
_Dfl2560IPsecInOctetsComp_Type = Counter64
_Dfl2560IPsecInOctetsComp_Object = MibScalar
dfl2560IPsecInOctetsComp = _Dfl2560IPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 11),
    _Dfl2560IPsecInOctetsComp_Type()
)
dfl2560IPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecInOctetsComp.setStatus("current")
_Dfl2560IPsecInOctetsUncomp_Type = Counter64
_Dfl2560IPsecInOctetsUncomp_Object = MibScalar
dfl2560IPsecInOctetsUncomp = _Dfl2560IPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 12),
    _Dfl2560IPsecInOctetsUncomp_Type()
)
dfl2560IPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecInOctetsUncomp.setStatus("current")
_Dfl2560IPsecOutOctetsComp_Type = Counter64
_Dfl2560IPsecOutOctetsComp_Object = MibScalar
dfl2560IPsecOutOctetsComp = _Dfl2560IPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 13),
    _Dfl2560IPsecOutOctetsComp_Type()
)
dfl2560IPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecOutOctetsComp.setStatus("current")
_Dfl2560IPsecOutOctetsUncomp_Type = Counter64
_Dfl2560IPsecOutOctetsUncomp_Object = MibScalar
dfl2560IPsecOutOctetsUncomp = _Dfl2560IPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 14),
    _Dfl2560IPsecOutOctetsUncomp_Type()
)
dfl2560IPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecOutOctetsUncomp.setStatus("current")
_Dfl2560IPsecForwardedOctetsComp_Type = Counter64
_Dfl2560IPsecForwardedOctetsComp_Object = MibScalar
dfl2560IPsecForwardedOctetsComp = _Dfl2560IPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 15),
    _Dfl2560IPsecForwardedOctetsComp_Type()
)
dfl2560IPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecForwardedOctetsComp.setStatus("current")
_Dfl2560IPsecForwardedOctetsUcomp_Type = Counter64
_Dfl2560IPsecForwardedOctetsUcomp_Object = MibScalar
dfl2560IPsecForwardedOctetsUcomp = _Dfl2560IPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 16),
    _Dfl2560IPsecForwardedOctetsUcomp_Type()
)
dfl2560IPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecForwardedOctetsUcomp.setStatus("current")
_Dfl2560IPsecInPackets_Type = Counter64
_Dfl2560IPsecInPackets_Object = MibScalar
dfl2560IPsecInPackets = _Dfl2560IPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 17),
    _Dfl2560IPsecInPackets_Type()
)
dfl2560IPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecInPackets.setStatus("current")
_Dfl2560IPsecOutPackets_Type = Counter64
_Dfl2560IPsecOutPackets_Object = MibScalar
dfl2560IPsecOutPackets = _Dfl2560IPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 18),
    _Dfl2560IPsecOutPackets_Type()
)
dfl2560IPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecOutPackets.setStatus("current")
_Dfl2560IPsecForwardedPackets_Type = Counter64
_Dfl2560IPsecForwardedPackets_Object = MibScalar
dfl2560IPsecForwardedPackets = _Dfl2560IPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 19),
    _Dfl2560IPsecForwardedPackets_Type()
)
dfl2560IPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecForwardedPackets.setStatus("current")
_Dfl2560IPsecActiveTransforms_Type = Gauge32
_Dfl2560IPsecActiveTransforms_Object = MibScalar
dfl2560IPsecActiveTransforms = _Dfl2560IPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 20),
    _Dfl2560IPsecActiveTransforms_Type()
)
dfl2560IPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecActiveTransforms.setStatus("current")
_Dfl2560IPsecTotalTransforms_Type = Counter32
_Dfl2560IPsecTotalTransforms_Object = MibScalar
dfl2560IPsecTotalTransforms = _Dfl2560IPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 21),
    _Dfl2560IPsecTotalTransforms_Type()
)
dfl2560IPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecTotalTransforms.setStatus("current")
_Dfl2560IPsecOutOfTransforms_Type = Counter32
_Dfl2560IPsecOutOfTransforms_Object = MibScalar
dfl2560IPsecOutOfTransforms = _Dfl2560IPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 22),
    _Dfl2560IPsecOutOfTransforms_Type()
)
dfl2560IPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecOutOfTransforms.setStatus("current")
_Dfl2560IPsecTotalRekeys_Type = Counter32
_Dfl2560IPsecTotalRekeys_Object = MibScalar
dfl2560IPsecTotalRekeys = _Dfl2560IPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 2, 1, 1, 23),
    _Dfl2560IPsecTotalRekeys_Type()
)
dfl2560IPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPsecTotalRekeys.setStatus("current")
_Dfl2560Rules_ObjectIdentity = ObjectIdentity
dfl2560Rules = _Dfl2560Rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 3)
)
_Dfl2560RuleUseTable_Object = MibTable
dfl2560RuleUseTable = _Dfl2560RuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl2560RuleUseTable.setStatus("current")
_Dfl2560RuleUseEntry_Object = MibTableRow
dfl2560RuleUseEntry = _Dfl2560RuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 3, 2, 1)
)
dfl2560RuleUseEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560RuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2560RuleUseEntry.setStatus("current")


class _Dfl2560RuleIndex_Type(Integer32):
    """Custom type dfl2560RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560RuleIndex_Type.__name__ = "Integer32"
_Dfl2560RuleIndex_Object = MibTableColumn
dfl2560RuleIndex = _Dfl2560RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 3, 2, 1, 1),
    _Dfl2560RuleIndex_Type()
)
dfl2560RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560RuleIndex.setStatus("current")
_Dfl2560RuleName_Type = DisplayString
_Dfl2560RuleName_Object = MibTableColumn
dfl2560RuleName = _Dfl2560RuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 3, 2, 1, 2),
    _Dfl2560RuleName_Type()
)
dfl2560RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560RuleName.setStatus("current")
_Dfl2560RuleUse_Type = Counter32
_Dfl2560RuleUse_Object = MibTableColumn
dfl2560RuleUse = _Dfl2560RuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 3, 2, 1, 3),
    _Dfl2560RuleUse_Type()
)
dfl2560RuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560RuleUse.setStatus("current")
_Dfl2560IPPools_ObjectIdentity = ObjectIdentity
dfl2560IPPools = _Dfl2560IPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4)
)
_Dfl2560IPPoolsNumber_Type = Integer32
_Dfl2560IPPoolsNumber_Object = MibScalar
dfl2560IPPoolsNumber = _Dfl2560IPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 1),
    _Dfl2560IPPoolsNumber_Type()
)
dfl2560IPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolsNumber.setStatus("current")
_Dfl2560IPPoolTable_Object = MibTable
dfl2560IPPoolTable = _Dfl2560IPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl2560IPPoolTable.setStatus("current")
_Dfl2560IPPoolEntry_Object = MibTableRow
dfl2560IPPoolEntry = _Dfl2560IPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1)
)
dfl2560IPPoolEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560IPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl2560IPPoolEntry.setStatus("current")


class _Dfl2560IPPoolIndex_Type(Integer32):
    """Custom type dfl2560IPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560IPPoolIndex_Type.__name__ = "Integer32"
_Dfl2560IPPoolIndex_Object = MibTableColumn
dfl2560IPPoolIndex = _Dfl2560IPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 1),
    _Dfl2560IPPoolIndex_Type()
)
dfl2560IPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560IPPoolIndex.setStatus("current")
_Dfl2560IPPoolName_Type = DisplayString
_Dfl2560IPPoolName_Object = MibTableColumn
dfl2560IPPoolName = _Dfl2560IPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 2),
    _Dfl2560IPPoolName_Type()
)
dfl2560IPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolName.setStatus("current")
_Dfl2560IPPoolPrepare_Type = Gauge32
_Dfl2560IPPoolPrepare_Object = MibTableColumn
dfl2560IPPoolPrepare = _Dfl2560IPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 3),
    _Dfl2560IPPoolPrepare_Type()
)
dfl2560IPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolPrepare.setStatus("current")
_Dfl2560IPPoolFree_Type = Gauge32
_Dfl2560IPPoolFree_Object = MibTableColumn
dfl2560IPPoolFree = _Dfl2560IPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 4),
    _Dfl2560IPPoolFree_Type()
)
dfl2560IPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolFree.setStatus("current")
_Dfl2560IPPoolMisses_Type = Gauge32
_Dfl2560IPPoolMisses_Object = MibTableColumn
dfl2560IPPoolMisses = _Dfl2560IPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 5),
    _Dfl2560IPPoolMisses_Type()
)
dfl2560IPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolMisses.setStatus("current")
_Dfl2560IPPoolClientFails_Type = Gauge32
_Dfl2560IPPoolClientFails_Object = MibTableColumn
dfl2560IPPoolClientFails = _Dfl2560IPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 6),
    _Dfl2560IPPoolClientFails_Type()
)
dfl2560IPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolClientFails.setStatus("current")
_Dfl2560IPPoolUsed_Type = Gauge32
_Dfl2560IPPoolUsed_Object = MibTableColumn
dfl2560IPPoolUsed = _Dfl2560IPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 4, 2, 1, 7),
    _Dfl2560IPPoolUsed_Type()
)
dfl2560IPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560IPPoolUsed.setStatus("current")
_Dfl2560DHCPServer_ObjectIdentity = ObjectIdentity
dfl2560DHCPServer = _Dfl2560DHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5)
)
_Dfl2560DHCPTotalRejected_Type = Gauge32
_Dfl2560DHCPTotalRejected_Object = MibScalar
dfl2560DHCPTotalRejected = _Dfl2560DHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 1),
    _Dfl2560DHCPTotalRejected_Type()
)
dfl2560DHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPTotalRejected.setStatus("current")
_Dfl2560DHCPRuleTable_Object = MibTable
dfl2560DHCPRuleTable = _Dfl2560DHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl2560DHCPRuleTable.setStatus("current")
_Dfl2560DHCPRuleEntry_Object = MibTableRow
dfl2560DHCPRuleEntry = _Dfl2560DHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1)
)
dfl2560DHCPRuleEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560DHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2560DHCPRuleEntry.setStatus("current")


class _Dfl2560DHCPRuleIndex_Type(Integer32):
    """Custom type dfl2560DHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560DHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl2560DHCPRuleIndex_Object = MibTableColumn
dfl2560DHCPRuleIndex = _Dfl2560DHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 1),
    _Dfl2560DHCPRuleIndex_Type()
)
dfl2560DHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560DHCPRuleIndex.setStatus("current")
_Dfl2560DHCPRuleName_Type = DisplayString
_Dfl2560DHCPRuleName_Object = MibTableColumn
dfl2560DHCPRuleName = _Dfl2560DHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 2),
    _Dfl2560DHCPRuleName_Type()
)
dfl2560DHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRuleName.setStatus("current")
_Dfl2560DHCPRuleUsage_Type = Gauge32
_Dfl2560DHCPRuleUsage_Object = MibTableColumn
dfl2560DHCPRuleUsage = _Dfl2560DHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 3),
    _Dfl2560DHCPRuleUsage_Type()
)
dfl2560DHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRuleUsage.setStatus("current")
_Dfl2560DHCPRuleUsagePercent_Type = Gauge32
_Dfl2560DHCPRuleUsagePercent_Object = MibTableColumn
dfl2560DHCPRuleUsagePercent = _Dfl2560DHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 4),
    _Dfl2560DHCPRuleUsagePercent_Type()
)
dfl2560DHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRuleUsagePercent.setStatus("current")
_Dfl2560DHCPActiveClients_Type = Gauge32
_Dfl2560DHCPActiveClients_Object = MibTableColumn
dfl2560DHCPActiveClients = _Dfl2560DHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 5),
    _Dfl2560DHCPActiveClients_Type()
)
dfl2560DHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPActiveClients.setStatus("current")
_Dfl2560DHCPActiveClientsPercent_Type = Gauge32
_Dfl2560DHCPActiveClientsPercent_Object = MibTableColumn
dfl2560DHCPActiveClientsPercent = _Dfl2560DHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 6),
    _Dfl2560DHCPActiveClientsPercent_Type()
)
dfl2560DHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPActiveClientsPercent.setStatus("current")
_Dfl2560DHCPRejectedRequests_Type = Gauge32
_Dfl2560DHCPRejectedRequests_Object = MibTableColumn
dfl2560DHCPRejectedRequests = _Dfl2560DHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 7),
    _Dfl2560DHCPRejectedRequests_Type()
)
dfl2560DHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRejectedRequests.setStatus("current")
_Dfl2560DHCPTotalLeases_Type = Gauge32
_Dfl2560DHCPTotalLeases_Object = MibTableColumn
dfl2560DHCPTotalLeases = _Dfl2560DHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 5, 2, 1, 8),
    _Dfl2560DHCPTotalLeases_Type()
)
dfl2560DHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPTotalLeases.setStatus("current")
_Dfl2560UserAuth_ObjectIdentity = ObjectIdentity
dfl2560UserAuth = _Dfl2560UserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6)
)
_Dfl2560UserAuthHTTPUsers_Type = Gauge32
_Dfl2560UserAuthHTTPUsers_Object = MibScalar
dfl2560UserAuthHTTPUsers = _Dfl2560UserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 1),
    _Dfl2560UserAuthHTTPUsers_Type()
)
dfl2560UserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthHTTPUsers.setStatus("current")
_Dfl2560UserAuthXAUTHUsers_Type = Gauge32
_Dfl2560UserAuthXAUTHUsers_Object = MibScalar
dfl2560UserAuthXAUTHUsers = _Dfl2560UserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 2),
    _Dfl2560UserAuthXAUTHUsers_Type()
)
dfl2560UserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthXAUTHUsers.setStatus("current")
_Dfl2560UserAuthHTTPSUsers_Type = Gauge32
_Dfl2560UserAuthHTTPSUsers_Object = MibScalar
dfl2560UserAuthHTTPSUsers = _Dfl2560UserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 3),
    _Dfl2560UserAuthHTTPSUsers_Type()
)
dfl2560UserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthHTTPSUsers.setStatus("current")
_Dfl2560UserAuthPPPUsers_Type = Gauge32
_Dfl2560UserAuthPPPUsers_Object = MibScalar
dfl2560UserAuthPPPUsers = _Dfl2560UserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 4),
    _Dfl2560UserAuthPPPUsers_Type()
)
dfl2560UserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthPPPUsers.setStatus("current")
_Dfl2560UserAuthEAPUsers_Type = Gauge32
_Dfl2560UserAuthEAPUsers_Object = MibScalar
dfl2560UserAuthEAPUsers = _Dfl2560UserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 5),
    _Dfl2560UserAuthEAPUsers_Type()
)
dfl2560UserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthEAPUsers.setStatus("current")
_Dfl2560UserAuthRuleUseTable_Object = MibTable
dfl2560UserAuthRuleUseTable = _Dfl2560UserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl2560UserAuthRuleUseTable.setStatus("current")
_Dfl2560UserAuthRuleUseEntry_Object = MibTableRow
dfl2560UserAuthRuleUseEntry = _Dfl2560UserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 6, 1)
)
dfl2560UserAuthRuleUseEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560UserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2560UserAuthRuleUseEntry.setStatus("current")


class _Dfl2560UserAuthRuleIndex_Type(Integer32):
    """Custom type dfl2560UserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560UserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl2560UserAuthRuleIndex_Object = MibTableColumn
dfl2560UserAuthRuleIndex = _Dfl2560UserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 6, 1, 1),
    _Dfl2560UserAuthRuleIndex_Type()
)
dfl2560UserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560UserAuthRuleIndex.setStatus("current")
_Dfl2560UserAuthRuleName_Type = DisplayString
_Dfl2560UserAuthRuleName_Object = MibTableColumn
dfl2560UserAuthRuleName = _Dfl2560UserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 6, 1, 2),
    _Dfl2560UserAuthRuleName_Type()
)
dfl2560UserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthRuleName.setStatus("current")
_Dfl2560UserAuthRuleUse_Type = Counter32
_Dfl2560UserAuthRuleUse_Object = MibTableColumn
dfl2560UserAuthRuleUse = _Dfl2560UserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 6, 6, 1, 3),
    _Dfl2560UserAuthRuleUse_Type()
)
dfl2560UserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560UserAuthRuleUse.setStatus("current")
_Dfl2560LinkMonitor_ObjectIdentity = ObjectIdentity
dfl2560LinkMonitor = _Dfl2560LinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7)
)
_Dfl2560LinkMonGrp_Type = Integer32
_Dfl2560LinkMonGrp_Object = MibScalar
dfl2560LinkMonGrp = _Dfl2560LinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 1),
    _Dfl2560LinkMonGrp_Type()
)
dfl2560LinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560LinkMonGrp.setStatus("current")
_Dfl2560LinkMonGrpTable_Object = MibTable
dfl2560LinkMonGrpTable = _Dfl2560LinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl2560LinkMonGrpTable.setStatus("current")
_Dfl2560LinkMonGrpEntry_Object = MibTableRow
dfl2560LinkMonGrpEntry = _Dfl2560LinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 2, 1)
)
dfl2560LinkMonGrpEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560LinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl2560LinkMonGrpEntry.setStatus("current")


class _Dfl2560LinkMonGrpIndex_Type(Integer32):
    """Custom type dfl2560LinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560LinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl2560LinkMonGrpIndex_Object = MibTableColumn
dfl2560LinkMonGrpIndex = _Dfl2560LinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 2, 1, 1),
    _Dfl2560LinkMonGrpIndex_Type()
)
dfl2560LinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560LinkMonGrpIndex.setStatus("current")
_Dfl2560LinkMonGrpName_Type = DisplayString
_Dfl2560LinkMonGrpName_Object = MibTableColumn
dfl2560LinkMonGrpName = _Dfl2560LinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 2, 1, 2),
    _Dfl2560LinkMonGrpName_Type()
)
dfl2560LinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560LinkMonGrpName.setStatus("current")
_Dfl2560LinkMonGrpHostsUp_Type = Gauge32
_Dfl2560LinkMonGrpHostsUp_Object = MibTableColumn
dfl2560LinkMonGrpHostsUp = _Dfl2560LinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 2, 1, 3),
    _Dfl2560LinkMonGrpHostsUp_Type()
)
dfl2560LinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560LinkMonGrpHostsUp.setStatus("current")
_Dfl2560LinkMonHostTable_Object = MibTable
dfl2560LinkMonHostTable = _Dfl2560LinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl2560LinkMonHostTable.setStatus("current")
_Dfl2560LinkMonHostEntry_Object = MibTableRow
dfl2560LinkMonHostEntry = _Dfl2560LinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 3, 1)
)
dfl2560LinkMonHostEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560LinkMonGrpIndex"),
    (0, "DFL2560-MIB", "dfl2560LinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl2560LinkMonHostEntry.setStatus("current")


class _Dfl2560LinkMonHostIndex_Type(Integer32):
    """Custom type dfl2560LinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560LinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl2560LinkMonHostIndex_Object = MibTableColumn
dfl2560LinkMonHostIndex = _Dfl2560LinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 3, 1, 1),
    _Dfl2560LinkMonHostIndex_Type()
)
dfl2560LinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560LinkMonHostIndex.setStatus("current")
_Dfl2560LinkMonHostId_Type = DisplayString
_Dfl2560LinkMonHostId_Object = MibTableColumn
dfl2560LinkMonHostId = _Dfl2560LinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 3, 1, 2),
    _Dfl2560LinkMonHostId_Type()
)
dfl2560LinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560LinkMonHostId.setStatus("current")
_Dfl2560LinkMonHostShortTermLoss_Type = Gauge32
_Dfl2560LinkMonHostShortTermLoss_Object = MibTableColumn
dfl2560LinkMonHostShortTermLoss = _Dfl2560LinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 3, 1, 3),
    _Dfl2560LinkMonHostShortTermLoss_Type()
)
dfl2560LinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560LinkMonHostShortTermLoss.setStatus("current")
_Dfl2560LinkMonHostPacketsLost_Type = Counter32
_Dfl2560LinkMonHostPacketsLost_Object = MibTableColumn
dfl2560LinkMonHostPacketsLost = _Dfl2560LinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 7, 3, 1, 4),
    _Dfl2560LinkMonHostPacketsLost_Type()
)
dfl2560LinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560LinkMonHostPacketsLost.setStatus("current")
_Dfl2560Pipes_ObjectIdentity = ObjectIdentity
dfl2560Pipes = _Dfl2560Pipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8)
)
_Dfl2560PipeUsers_Type = Gauge32
_Dfl2560PipeUsers_Object = MibScalar
dfl2560PipeUsers = _Dfl2560PipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 1),
    _Dfl2560PipeUsers_Type()
)
dfl2560PipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeUsers.setStatus("current")
_Dfl2560PipeTable_Object = MibTable
dfl2560PipeTable = _Dfl2560PipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl2560PipeTable.setStatus("current")
_Dfl2560PipeEntry_Object = MibTableRow
dfl2560PipeEntry = _Dfl2560PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1)
)
dfl2560PipeEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560PipeIndex"),
)
if mibBuilder.loadTexts:
    dfl2560PipeEntry.setStatus("current")


class _Dfl2560PipeIndex_Type(Integer32):
    """Custom type dfl2560PipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560PipeIndex_Type.__name__ = "Integer32"
_Dfl2560PipeIndex_Object = MibTableColumn
dfl2560PipeIndex = _Dfl2560PipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 1),
    _Dfl2560PipeIndex_Type()
)
dfl2560PipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560PipeIndex.setStatus("current")
_Dfl2560PipeName_Type = DisplayString
_Dfl2560PipeName_Object = MibTableColumn
dfl2560PipeName = _Dfl2560PipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 2),
    _Dfl2560PipeName_Type()
)
dfl2560PipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeName.setStatus("current")
_Dfl2560PipeMinPrec_Type = Integer32
_Dfl2560PipeMinPrec_Object = MibTableColumn
dfl2560PipeMinPrec = _Dfl2560PipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 3),
    _Dfl2560PipeMinPrec_Type()
)
dfl2560PipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeMinPrec.setStatus("current")
_Dfl2560PipeMaxPrec_Type = Integer32
_Dfl2560PipeMaxPrec_Object = MibTableColumn
dfl2560PipeMaxPrec = _Dfl2560PipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 4),
    _Dfl2560PipeMaxPrec_Type()
)
dfl2560PipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeMaxPrec.setStatus("current")
_Dfl2560PipeDefPrec_Type = Integer32
_Dfl2560PipeDefPrec_Object = MibTableColumn
dfl2560PipeDefPrec = _Dfl2560PipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 5),
    _Dfl2560PipeDefPrec_Type()
)
dfl2560PipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeDefPrec.setStatus("current")
_Dfl2560PipeNumPrec_Type = Integer32
_Dfl2560PipeNumPrec_Object = MibTableColumn
dfl2560PipeNumPrec = _Dfl2560PipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 6),
    _Dfl2560PipeNumPrec_Type()
)
dfl2560PipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeNumPrec.setStatus("current")
_Dfl2560PipeNumUsers_Type = Gauge32
_Dfl2560PipeNumUsers_Object = MibTableColumn
dfl2560PipeNumUsers = _Dfl2560PipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 7),
    _Dfl2560PipeNumUsers_Type()
)
dfl2560PipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeNumUsers.setStatus("current")
_Dfl2560PipeCurrentBps_Type = Gauge32
_Dfl2560PipeCurrentBps_Object = MibTableColumn
dfl2560PipeCurrentBps = _Dfl2560PipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 8),
    _Dfl2560PipeCurrentBps_Type()
)
dfl2560PipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeCurrentBps.setStatus("current")
_Dfl2560PipeCurrentPps_Type = Gauge32
_Dfl2560PipeCurrentPps_Object = MibTableColumn
dfl2560PipeCurrentPps = _Dfl2560PipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 9),
    _Dfl2560PipeCurrentPps_Type()
)
dfl2560PipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeCurrentPps.setStatus("current")
_Dfl2560PipeDelayedPackets_Type = Counter32
_Dfl2560PipeDelayedPackets_Object = MibTableColumn
dfl2560PipeDelayedPackets = _Dfl2560PipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 10),
    _Dfl2560PipeDelayedPackets_Type()
)
dfl2560PipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeDelayedPackets.setStatus("current")
_Dfl2560PipeDropedPackets_Type = Counter32
_Dfl2560PipeDropedPackets_Object = MibTableColumn
dfl2560PipeDropedPackets = _Dfl2560PipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 2, 1, 11),
    _Dfl2560PipeDropedPackets_Type()
)
dfl2560PipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipeDropedPackets.setStatus("current")
_Dfl2560PipePrecTable_Object = MibTable
dfl2560PipePrecTable = _Dfl2560PipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl2560PipePrecTable.setStatus("current")
_Dfl2560PipePrecEntry_Object = MibTableRow
dfl2560PipePrecEntry = _Dfl2560PipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1)
)
dfl2560PipePrecEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560PipeIndex"),
    (0, "DFL2560-MIB", "dfl2560PipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl2560PipePrecEntry.setStatus("current")


class _Dfl2560PipePrecIndex_Type(Integer32):
    """Custom type dfl2560PipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560PipePrecIndex_Type.__name__ = "Integer32"
_Dfl2560PipePrecIndex_Object = MibTableColumn
dfl2560PipePrecIndex = _Dfl2560PipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 1),
    _Dfl2560PipePrecIndex_Type()
)
dfl2560PipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560PipePrecIndex.setStatus("current")
_Dfl2560PipePrec_Type = Integer32
_Dfl2560PipePrec_Object = MibTableColumn
dfl2560PipePrec = _Dfl2560PipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 2),
    _Dfl2560PipePrec_Type()
)
dfl2560PipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrec.setStatus("current")
_Dfl2560PipePrecBps_Type = Gauge32
_Dfl2560PipePrecBps_Object = MibTableColumn
dfl2560PipePrecBps = _Dfl2560PipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 3),
    _Dfl2560PipePrecBps_Type()
)
dfl2560PipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecBps.setStatus("current")
_Dfl2560PipePrecTotalPps_Type = Gauge32
_Dfl2560PipePrecTotalPps_Object = MibTableColumn
dfl2560PipePrecTotalPps = _Dfl2560PipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 4),
    _Dfl2560PipePrecTotalPps_Type()
)
dfl2560PipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecTotalPps.setStatus("current")
_Dfl2560PipePrecReservedBps_Type = Gauge32
_Dfl2560PipePrecReservedBps_Object = MibTableColumn
dfl2560PipePrecReservedBps = _Dfl2560PipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 5),
    _Dfl2560PipePrecReservedBps_Type()
)
dfl2560PipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecReservedBps.setStatus("current")
_Dfl2560PipePrecDynLimBps_Type = Gauge32
_Dfl2560PipePrecDynLimBps_Object = MibTableColumn
dfl2560PipePrecDynLimBps = _Dfl2560PipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 6),
    _Dfl2560PipePrecDynLimBps_Type()
)
dfl2560PipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecDynLimBps.setStatus("current")
_Dfl2560PipePrecDynUsrLimBps_Type = Gauge32
_Dfl2560PipePrecDynUsrLimBps_Object = MibTableColumn
dfl2560PipePrecDynUsrLimBps = _Dfl2560PipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 7),
    _Dfl2560PipePrecDynUsrLimBps_Type()
)
dfl2560PipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecDynUsrLimBps.setStatus("current")
_Dfl2560PipePrecDelayedPackets_Type = Counter32
_Dfl2560PipePrecDelayedPackets_Object = MibTableColumn
dfl2560PipePrecDelayedPackets = _Dfl2560PipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 8),
    _Dfl2560PipePrecDelayedPackets_Type()
)
dfl2560PipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecDelayedPackets.setStatus("current")
_Dfl2560PipePrecDropedPackets_Type = Counter32
_Dfl2560PipePrecDropedPackets_Object = MibTableColumn
dfl2560PipePrecDropedPackets = _Dfl2560PipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 8, 3, 1, 9),
    _Dfl2560PipePrecDropedPackets_Type()
)
dfl2560PipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560PipePrecDropedPackets.setStatus("current")
_Dfl2560ALG_ObjectIdentity = ObjectIdentity
dfl2560ALG = _Dfl2560ALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9)
)
_Dfl2560AlgSessions_Type = Gauge32
_Dfl2560AlgSessions_Object = MibScalar
dfl2560AlgSessions = _Dfl2560AlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 1),
    _Dfl2560AlgSessions_Type()
)
dfl2560AlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560AlgSessions.setStatus("current")
_Dfl2560AlgConnections_Type = Gauge32
_Dfl2560AlgConnections_Object = MibScalar
dfl2560AlgConnections = _Dfl2560AlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 2),
    _Dfl2560AlgConnections_Type()
)
dfl2560AlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560AlgConnections.setStatus("current")
_Dfl2560AlgTCPStreams_Type = Gauge32
_Dfl2560AlgTCPStreams_Object = MibScalar
dfl2560AlgTCPStreams = _Dfl2560AlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 3),
    _Dfl2560AlgTCPStreams_Type()
)
dfl2560AlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560AlgTCPStreams.setStatus("current")
_Dfl2560HttpAlg_ObjectIdentity = ObjectIdentity
dfl2560HttpAlg = _Dfl2560HttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4)
)
_Dfl2560HttpAlgTable_Object = MibTable
dfl2560HttpAlgTable = _Dfl2560HttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl2560HttpAlgTable.setStatus("current")
_Dfl2560HttpAlgEntry_Object = MibTableRow
dfl2560HttpAlgEntry = _Dfl2560HttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1, 1)
)
dfl2560HttpAlgEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560HttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl2560HttpAlgEntry.setStatus("current")


class _Dfl2560HttpAlgIndex_Type(Integer32):
    """Custom type dfl2560HttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560HttpAlgIndex_Type.__name__ = "Integer32"
_Dfl2560HttpAlgIndex_Object = MibTableColumn
dfl2560HttpAlgIndex = _Dfl2560HttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1, 1, 1),
    _Dfl2560HttpAlgIndex_Type()
)
dfl2560HttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560HttpAlgIndex.setStatus("current")
_Dfl2560HttpAlgName_Type = DisplayString
_Dfl2560HttpAlgName_Object = MibTableColumn
dfl2560HttpAlgName = _Dfl2560HttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1, 1, 2),
    _Dfl2560HttpAlgName_Type()
)
dfl2560HttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgName.setStatus("current")
_Dfl2560HttpAlgTotalRequested_Type = Gauge32
_Dfl2560HttpAlgTotalRequested_Object = MibTableColumn
dfl2560HttpAlgTotalRequested = _Dfl2560HttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1, 1, 3),
    _Dfl2560HttpAlgTotalRequested_Type()
)
dfl2560HttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgTotalRequested.setStatus("current")
_Dfl2560HttpAlgTotalAllowed_Type = Gauge32
_Dfl2560HttpAlgTotalAllowed_Object = MibTableColumn
dfl2560HttpAlgTotalAllowed = _Dfl2560HttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1, 1, 4),
    _Dfl2560HttpAlgTotalAllowed_Type()
)
dfl2560HttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgTotalAllowed.setStatus("current")
_Dfl2560HttpAlgTotalBlocked_Type = Gauge32
_Dfl2560HttpAlgTotalBlocked_Object = MibTableColumn
dfl2560HttpAlgTotalBlocked = _Dfl2560HttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 1, 1, 5),
    _Dfl2560HttpAlgTotalBlocked_Type()
)
dfl2560HttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgTotalBlocked.setStatus("current")
_Dfl2560HttpAlgCntFltTable_Object = MibTable
dfl2560HttpAlgCntFltTable = _Dfl2560HttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltTable.setStatus("current")
_Dfl2560HttpAlgCntFltEntry_Object = MibTableRow
dfl2560HttpAlgCntFltEntry = _Dfl2560HttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2, 1)
)
dfl2560HttpAlgCntFltEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560HttpAlgIndex"),
    (0, "DFL2560-MIB", "dfl2560HttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltEntry.setStatus("current")


class _Dfl2560HttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl2560HttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560HttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl2560HttpAlgCntFltIndex_Object = MibTableColumn
dfl2560HttpAlgCntFltIndex = _Dfl2560HttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2, 1, 1),
    _Dfl2560HttpAlgCntFltIndex_Type()
)
dfl2560HttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltIndex.setStatus("current")
_Dfl2560HttpAlgCntFltName_Type = DisplayString
_Dfl2560HttpAlgCntFltName_Object = MibTableColumn
dfl2560HttpAlgCntFltName = _Dfl2560HttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2, 1, 2),
    _Dfl2560HttpAlgCntFltName_Type()
)
dfl2560HttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltName.setStatus("current")
_Dfl2560HttpAlgCntFltRequests_Type = Gauge32
_Dfl2560HttpAlgCntFltRequests_Object = MibTableColumn
dfl2560HttpAlgCntFltRequests = _Dfl2560HttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2, 1, 3),
    _Dfl2560HttpAlgCntFltRequests_Type()
)
dfl2560HttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltRequests.setStatus("current")
_Dfl2560HttpAlgCntFltAllowed_Type = Gauge32
_Dfl2560HttpAlgCntFltAllowed_Object = MibTableColumn
dfl2560HttpAlgCntFltAllowed = _Dfl2560HttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2, 1, 4),
    _Dfl2560HttpAlgCntFltAllowed_Type()
)
dfl2560HttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltAllowed.setStatus("current")
_Dfl2560HttpAlgCntFltBlocked_Type = Gauge32
_Dfl2560HttpAlgCntFltBlocked_Object = MibTableColumn
dfl2560HttpAlgCntFltBlocked = _Dfl2560HttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 4, 2, 1, 5),
    _Dfl2560HttpAlgCntFltBlocked_Type()
)
dfl2560HttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HttpAlgCntFltBlocked.setStatus("current")
_Dfl2560SmtpAlg_ObjectIdentity = ObjectIdentity
dfl2560SmtpAlg = _Dfl2560SmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5)
)
_Dfl2560SmtpAlgTable_Object = MibTable
dfl2560SmtpAlgTable = _Dfl2560SmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl2560SmtpAlgTable.setStatus("current")
_Dfl2560SmtpAlgEntry_Object = MibTableRow
dfl2560SmtpAlgEntry = _Dfl2560SmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1, 1)
)
dfl2560SmtpAlgEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560SmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl2560SmtpAlgEntry.setStatus("current")


class _Dfl2560SmtpAlgIndex_Type(Integer32):
    """Custom type dfl2560SmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560SmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl2560SmtpAlgIndex_Object = MibTableColumn
dfl2560SmtpAlgIndex = _Dfl2560SmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1, 1, 1),
    _Dfl2560SmtpAlgIndex_Type()
)
dfl2560SmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgIndex.setStatus("current")
_Dfl2560SmtpAlgName_Type = DisplayString
_Dfl2560SmtpAlgName_Object = MibTableColumn
dfl2560SmtpAlgName = _Dfl2560SmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1, 1, 2),
    _Dfl2560SmtpAlgName_Type()
)
dfl2560SmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgName.setStatus("current")
_Dfl2560SmtpAlgTotCheckedSes_Type = Gauge32
_Dfl2560SmtpAlgTotCheckedSes_Object = MibTableColumn
dfl2560SmtpAlgTotCheckedSes = _Dfl2560SmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1, 1, 3),
    _Dfl2560SmtpAlgTotCheckedSes_Type()
)
dfl2560SmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgTotCheckedSes.setStatus("current")
_Dfl2560SmtpAlgTotSpamSes_Type = Gauge32
_Dfl2560SmtpAlgTotSpamSes_Object = MibTableColumn
dfl2560SmtpAlgTotSpamSes = _Dfl2560SmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1, 1, 4),
    _Dfl2560SmtpAlgTotSpamSes_Type()
)
dfl2560SmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgTotSpamSes.setStatus("current")
_Dfl2560SmtpAlgTotDroppedSes_Type = Gauge32
_Dfl2560SmtpAlgTotDroppedSes_Object = MibTableColumn
dfl2560SmtpAlgTotDroppedSes = _Dfl2560SmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 1, 1, 5),
    _Dfl2560SmtpAlgTotDroppedSes_Type()
)
dfl2560SmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgTotDroppedSes.setStatus("current")
_Dfl2560SmtpAlgDnsBlTable_Object = MibTable
dfl2560SmtpAlgDnsBlTable = _Dfl2560SmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlTable.setStatus("current")
_Dfl2560SmtpAlgDnsBlEntry_Object = MibTableRow
dfl2560SmtpAlgDnsBlEntry = _Dfl2560SmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2, 1)
)
dfl2560SmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560SmtpAlgIndex"),
    (0, "DFL2560-MIB", "dfl2560SmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlEntry.setStatus("current")


class _Dfl2560SmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl2560SmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560SmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl2560SmtpAlgDnsBlIndex_Object = MibTableColumn
dfl2560SmtpAlgDnsBlIndex = _Dfl2560SmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2, 1, 1),
    _Dfl2560SmtpAlgDnsBlIndex_Type()
)
dfl2560SmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlIndex.setStatus("current")
_Dfl2560SmtpAlgDnsBlName_Type = DisplayString
_Dfl2560SmtpAlgDnsBlName_Object = MibTableColumn
dfl2560SmtpAlgDnsBlName = _Dfl2560SmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2, 1, 2),
    _Dfl2560SmtpAlgDnsBlName_Type()
)
dfl2560SmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlName.setStatus("current")
_Dfl2560SmtpAlgDnsBlChecked_Type = Gauge32
_Dfl2560SmtpAlgDnsBlChecked_Object = MibTableColumn
dfl2560SmtpAlgDnsBlChecked = _Dfl2560SmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2, 1, 3),
    _Dfl2560SmtpAlgDnsBlChecked_Type()
)
dfl2560SmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlChecked.setStatus("current")
_Dfl2560SmtpAlgDnsBlMatched_Type = Gauge32
_Dfl2560SmtpAlgDnsBlMatched_Object = MibTableColumn
dfl2560SmtpAlgDnsBlMatched = _Dfl2560SmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2, 1, 4),
    _Dfl2560SmtpAlgDnsBlMatched_Type()
)
dfl2560SmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlMatched.setStatus("current")
_Dfl2560SmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl2560SmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl2560SmtpAlgDnsBlFailChecks = _Dfl2560SmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 9, 5, 2, 1, 5),
    _Dfl2560SmtpAlgDnsBlFailChecks_Type()
)
dfl2560SmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560SmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl2560DHCPRelay_ObjectIdentity = ObjectIdentity
dfl2560DHCPRelay = _Dfl2560DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11)
)
_Dfl2560DHCPRelayCurClients_Type = Gauge32
_Dfl2560DHCPRelayCurClients_Object = MibScalar
dfl2560DHCPRelayCurClients = _Dfl2560DHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 1),
    _Dfl2560DHCPRelayCurClients_Type()
)
dfl2560DHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayCurClients.setStatus("current")
_Dfl2560DHCPRelayCurTrans_Type = Gauge32
_Dfl2560DHCPRelayCurTrans_Object = MibScalar
dfl2560DHCPRelayCurTrans = _Dfl2560DHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 2),
    _Dfl2560DHCPRelayCurTrans_Type()
)
dfl2560DHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayCurTrans.setStatus("current")
_Dfl2560DHCPRelayRejected_Type = Gauge32
_Dfl2560DHCPRelayRejected_Object = MibScalar
dfl2560DHCPRelayRejected = _Dfl2560DHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 3),
    _Dfl2560DHCPRelayRejected_Type()
)
dfl2560DHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRejected.setStatus("current")
_Dfl2560DHCPRelayRuleTable_Object = MibTable
dfl2560DHCPRelayRuleTable = _Dfl2560DHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleTable.setStatus("current")
_Dfl2560DHCPRelayRuleEntry_Object = MibTableRow
dfl2560DHCPRelayRuleEntry = _Dfl2560DHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1)
)
dfl2560DHCPRelayRuleEntry.setIndexNames(
    (0, "DFL2560-MIB", "dfl2560DHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleEntry.setStatus("current")


class _Dfl2560DHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl2560DHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl2560DHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl2560DHCPRelayRuleIndex_Object = MibTableColumn
dfl2560DHCPRelayRuleIndex = _Dfl2560DHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1, 1),
    _Dfl2560DHCPRelayRuleIndex_Type()
)
dfl2560DHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleIndex.setStatus("current")
_Dfl2560DHCPRelayRuleName_Type = DisplayString
_Dfl2560DHCPRelayRuleName_Object = MibTableColumn
dfl2560DHCPRelayRuleName = _Dfl2560DHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1, 2),
    _Dfl2560DHCPRelayRuleName_Type()
)
dfl2560DHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleName.setStatus("current")
_Dfl2560DHCPRelayRuleHits_Type = Gauge32
_Dfl2560DHCPRelayRuleHits_Object = MibTableColumn
dfl2560DHCPRelayRuleHits = _Dfl2560DHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1, 3),
    _Dfl2560DHCPRelayRuleHits_Type()
)
dfl2560DHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleHits.setStatus("current")
_Dfl2560DHCPRelayRuleCurClients_Type = Gauge32
_Dfl2560DHCPRelayRuleCurClients_Object = MibTableColumn
dfl2560DHCPRelayRuleCurClients = _Dfl2560DHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1, 4),
    _Dfl2560DHCPRelayRuleCurClients_Type()
)
dfl2560DHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleCurClients.setStatus("current")
_Dfl2560DHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl2560DHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl2560DHCPRelayRuleRejCliPkts = _Dfl2560DHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1, 5),
    _Dfl2560DHCPRelayRuleRejCliPkts_Type()
)
dfl2560DHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl2560DHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl2560DHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl2560DHCPRelayRuleRejSrvPkts = _Dfl2560DHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 11, 4, 1, 6),
    _Dfl2560DHCPRelayRuleRejSrvPkts_Type()
)
dfl2560DHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560DHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl2560HA_ObjectIdentity = ObjectIdentity
dfl2560HA = _Dfl2560HA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 12)
)
_Dfl2560HASyncSendQueueLength_Type = Gauge32
_Dfl2560HASyncSendQueueLength_Object = MibScalar
dfl2560HASyncSendQueueLength = _Dfl2560HASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 12, 1),
    _Dfl2560HASyncSendQueueLength_Type()
)
dfl2560HASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HASyncSendQueueLength.setStatus("current")
_Dfl2560HASyncSendQueueUsagePkt_Type = Gauge32
_Dfl2560HASyncSendQueueUsagePkt_Object = MibScalar
dfl2560HASyncSendQueueUsagePkt = _Dfl2560HASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 12, 2),
    _Dfl2560HASyncSendQueueUsagePkt_Type()
)
dfl2560HASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HASyncSendQueueUsagePkt.setStatus("current")
_Dfl2560HASyncSendQueueUsageOct_Type = Gauge32
_Dfl2560HASyncSendQueueUsageOct_Object = MibScalar
dfl2560HASyncSendQueueUsageOct = _Dfl2560HASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 12, 3),
    _Dfl2560HASyncSendQueueUsageOct_Type()
)
dfl2560HASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HASyncSendQueueUsageOct.setStatus("current")
_Dfl2560HASyncSentPackets_Type = Counter32
_Dfl2560HASyncSentPackets_Object = MibScalar
dfl2560HASyncSentPackets = _Dfl2560HASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 12, 4),
    _Dfl2560HASyncSentPackets_Type()
)
dfl2560HASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HASyncSentPackets.setStatus("current")
_Dfl2560HASyncSendResentPackets_Type = Counter32
_Dfl2560HASyncSendResentPackets_Object = MibScalar
dfl2560HASyncSendResentPackets = _Dfl2560HASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 1, 2, 12, 5),
    _Dfl2560HASyncSendResentPackets_Type()
)
dfl2560HASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl2560HASyncSendResentPackets.setStatus("current")
_Dfl2560reg_ObjectIdentity = ObjectIdentity
dfl2560reg = _Dfl2560reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2)
)
_Dfl2560MibModules_ObjectIdentity = ObjectIdentity
dfl2560MibModules = _Dfl2560MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 1)
)
_Dfl2560MibConfs_ObjectIdentity = ObjectIdentity
dfl2560MibConfs = _Dfl2560MibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 2)
)
_Dfl2560StatsConformance_ObjectIdentity = ObjectIdentity
dfl2560StatsConformance = _Dfl2560StatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 2, 1)
)
_Dfl2560MibObjectGroups_ObjectIdentity = ObjectIdentity
dfl2560MibObjectGroups = _Dfl2560MibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3)
)
_Dfl2560StatsRegGroups_ObjectIdentity = ObjectIdentity
dfl2560StatsRegGroups = _Dfl2560StatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1)
)

# Managed Objects groups

dfl2560SystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 1)
)
dfl2560SystemObjectGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560SysCpuLoad"),
        ("DFL2560-MIB", "dfl2560SysForwardedBits"),
        ("DFL2560-MIB", "dfl2560SysForwardedPackets"),
        ("DFL2560-MIB", "dfl2560SysBuffUse"),
        ("DFL2560-MIB", "dfl2560SysConns"),
        ("DFL2560-MIB", "dfl2560HWSensorName"),
        ("DFL2560-MIB", "dfl2560HWSensorValue"),
        ("DFL2560-MIB", "dfl2560HWSensorUnit"),
        ("DFL2560-MIB", "dfl2560SysMemUsage"),
        ("DFL2560-MIB", "dfl2560SysTimerUsage"),
        ("DFL2560-MIB", "dfl2560SysConnOPS"),
        ("DFL2560-MIB", "dfl2560SysConnCPS"),
        ("DFL2560-MIB", "dfl2560SysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl2560SystemObjectGroup.setStatus("current")

dfl2560IPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 2)
)
dfl2560IPsecObjectGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560IPsecPhaseOneActive"),
        ("DFL2560-MIB", "dfl2560IPsecPhaseOneAggrModeDone"),
        ("DFL2560-MIB", "dfl2560IPsecQuickModeActive"),
        ("DFL2560-MIB", "dfl2560IPsecPhaseOneDone"),
        ("DFL2560-MIB", "dfl2560IPsecPhaseOneFailed"),
        ("DFL2560-MIB", "dfl2560IPsecPhaseOneRekeyed"),
        ("DFL2560-MIB", "dfl2560IPsecQuickModeDone"),
        ("DFL2560-MIB", "dfl2560IPsecQuickModeFailed"),
        ("DFL2560-MIB", "dfl2560IPsecInfoDone"),
        ("DFL2560-MIB", "dfl2560IPsecInfoFailed"),
        ("DFL2560-MIB", "dfl2560IPsecInOctetsComp"),
        ("DFL2560-MIB", "dfl2560IPsecInOctetsUncomp"),
        ("DFL2560-MIB", "dfl2560IPsecOutOctetsComp"),
        ("DFL2560-MIB", "dfl2560IPsecOutOctetsUncomp"),
        ("DFL2560-MIB", "dfl2560IPsecForwardedOctetsComp"),
        ("DFL2560-MIB", "dfl2560IPsecForwardedOctetsUcomp"),
        ("DFL2560-MIB", "dfl2560IPsecInPackets"),
        ("DFL2560-MIB", "dfl2560IPsecOutPackets"),
        ("DFL2560-MIB", "dfl2560IPsecForwardedPackets"),
        ("DFL2560-MIB", "dfl2560IPsecActiveTransforms"),
        ("DFL2560-MIB", "dfl2560IPsecTotalTransforms"),
        ("DFL2560-MIB", "dfl2560IPsecOutOfTransforms"),
        ("DFL2560-MIB", "dfl2560IPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl2560IPsecObjectGroup.setStatus("current")

dfl2560StateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 3)
)
dfl2560StateCountersGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560SysPscTcpSyn"),
        ("DFL2560-MIB", "dfl2560SysPscTcpOpen"),
        ("DFL2560-MIB", "dfl2560SysPscTcpFin"),
        ("DFL2560-MIB", "dfl2560SysPscUdp"),
        ("DFL2560-MIB", "dfl2560SysPscIcmp"),
        ("DFL2560-MIB", "dfl2560SysPscOther"))
)
if mibBuilder.loadTexts:
    dfl2560StateCountersGroup.setStatus("current")

dfl2560IPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 4)
)
dfl2560IPPoolGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560IPPoolsNumber"),
        ("DFL2560-MIB", "dfl2560IPPoolName"),
        ("DFL2560-MIB", "dfl2560IPPoolPrepare"),
        ("DFL2560-MIB", "dfl2560IPPoolFree"),
        ("DFL2560-MIB", "dfl2560IPPoolMisses"),
        ("DFL2560-MIB", "dfl2560IPPoolClientFails"),
        ("DFL2560-MIB", "dfl2560IPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl2560IPPoolGroup.setStatus("current")

dfl2560DHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 5)
)
dfl2560DHCPServerGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560DHCPTotalRejected"),
        ("DFL2560-MIB", "dfl2560DHCPRuleName"),
        ("DFL2560-MIB", "dfl2560DHCPRuleUsage"),
        ("DFL2560-MIB", "dfl2560DHCPRuleUsagePercent"),
        ("DFL2560-MIB", "dfl2560DHCPActiveClients"),
        ("DFL2560-MIB", "dfl2560DHCPActiveClientsPercent"),
        ("DFL2560-MIB", "dfl2560DHCPRejectedRequests"),
        ("DFL2560-MIB", "dfl2560DHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl2560DHCPServerGroup.setStatus("current")

dfl2560RuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 6)
)
dfl2560RuleUseGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560RuleName"),
        ("DFL2560-MIB", "dfl2560RuleUse"))
)
if mibBuilder.loadTexts:
    dfl2560RuleUseGroup.setStatus("current")

dfl2560UserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 7)
)
dfl2560UserAuthGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560UserAuthHTTPUsers"),
        ("DFL2560-MIB", "dfl2560UserAuthXAUTHUsers"),
        ("DFL2560-MIB", "dfl2560UserAuthHTTPSUsers"),
        ("DFL2560-MIB", "dfl2560UserAuthPPPUsers"),
        ("DFL2560-MIB", "dfl2560UserAuthEAPUsers"),
        ("DFL2560-MIB", "dfl2560UserAuthRuleName"),
        ("DFL2560-MIB", "dfl2560UserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl2560UserAuthGroup.setStatus("current")

dfl2560IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 8)
)
dfl2560IfStatsGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560IfName"),
        ("DFL2560-MIB", "dfl2560IfFragsIn"),
        ("DFL2560-MIB", "dfl2560IfFragReassOk"),
        ("DFL2560-MIB", "dfl2560IfFragReassFail"),
        ("DFL2560-MIB", "dfl2560IfPktsInCnt"),
        ("DFL2560-MIB", "dfl2560IfPktsOutCnt"),
        ("DFL2560-MIB", "dfl2560IfBitsInCnt"),
        ("DFL2560-MIB", "dfl2560IfBitsOutCnt"),
        ("DFL2560-MIB", "dfl2560IfPktsTotCnt"),
        ("DFL2560-MIB", "dfl2560IfBitsTotCnt"),
        ("DFL2560-MIB", "dfl2560IfHCPktsInCnt"),
        ("DFL2560-MIB", "dfl2560IfHCPktsOutCnt"),
        ("DFL2560-MIB", "dfl2560IfHCBitsInCnt"),
        ("DFL2560-MIB", "dfl2560IfHCBitsOutCnt"),
        ("DFL2560-MIB", "dfl2560IfHCPktsTotCnt"),
        ("DFL2560-MIB", "dfl2560IfHCBitsTotCnt"),
        ("DFL2560-MIB", "dfl2560IfRxRingFifoErrors"),
        ("DFL2560-MIB", "dfl2560IfRxDespools"),
        ("DFL2560-MIB", "dfl2560IfRxAvgUse"),
        ("DFL2560-MIB", "dfl2560IfRxRingSaturation"),
        ("DFL2560-MIB", "dfl2560RxRingFlooded"),
        ("DFL2560-MIB", "dfl2560IfTxDespools"),
        ("DFL2560-MIB", "dfl2560IfTxAvgUse"),
        ("DFL2560-MIB", "dfl2560IfTxRingSaturation"),
        ("DFL2560-MIB", "dfl2560RxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl2560IfStatsGroup.setStatus("current")

dfl2560LinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 9)
)
dfl2560LinkMonitorGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560LinkMonGrp"),
        ("DFL2560-MIB", "dfl2560LinkMonGrpName"),
        ("DFL2560-MIB", "dfl2560LinkMonGrpHostsUp"),
        ("DFL2560-MIB", "dfl2560LinkMonHostId"),
        ("DFL2560-MIB", "dfl2560LinkMonHostShortTermLoss"),
        ("DFL2560-MIB", "dfl2560LinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl2560LinkMonitorGroup.setStatus("current")

dfl2560PipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 10)
)
dfl2560PipesObjectGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560PipeUsers"),
        ("DFL2560-MIB", "dfl2560PipeName"),
        ("DFL2560-MIB", "dfl2560PipeMinPrec"),
        ("DFL2560-MIB", "dfl2560PipeMaxPrec"),
        ("DFL2560-MIB", "dfl2560PipeDefPrec"),
        ("DFL2560-MIB", "dfl2560PipeNumPrec"),
        ("DFL2560-MIB", "dfl2560PipeNumUsers"),
        ("DFL2560-MIB", "dfl2560PipeCurrentBps"),
        ("DFL2560-MIB", "dfl2560PipeCurrentPps"),
        ("DFL2560-MIB", "dfl2560PipeDelayedPackets"),
        ("DFL2560-MIB", "dfl2560PipeDropedPackets"),
        ("DFL2560-MIB", "dfl2560PipePrec"),
        ("DFL2560-MIB", "dfl2560PipePrecBps"),
        ("DFL2560-MIB", "dfl2560PipePrecTotalPps"),
        ("DFL2560-MIB", "dfl2560PipePrecReservedBps"),
        ("DFL2560-MIB", "dfl2560PipePrecDynLimBps"),
        ("DFL2560-MIB", "dfl2560PipePrecDynUsrLimBps"),
        ("DFL2560-MIB", "dfl2560PipePrecDelayedPackets"),
        ("DFL2560-MIB", "dfl2560PipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl2560PipesObjectGroup.setStatus("current")

dfl2560DHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 12)
)
dfl2560DHCPRelayObjectGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560DHCPRelayCurClients"),
        ("DFL2560-MIB", "dfl2560DHCPRelayCurTrans"),
        ("DFL2560-MIB", "dfl2560DHCPRelayRejected"),
        ("DFL2560-MIB", "dfl2560DHCPRelayRuleName"),
        ("DFL2560-MIB", "dfl2560DHCPRelayRuleHits"),
        ("DFL2560-MIB", "dfl2560DHCPRelayRuleCurClients"),
        ("DFL2560-MIB", "dfl2560DHCPRelayRuleRejCliPkts"),
        ("DFL2560-MIB", "dfl2560DHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl2560DHCPRelayObjectGroup.setStatus("current")

dfl2560AlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 13)
)
dfl2560AlgGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560AlgSessions"),
        ("DFL2560-MIB", "dfl2560AlgConnections"),
        ("DFL2560-MIB", "dfl2560AlgTCPStreams"),
        ("DFL2560-MIB", "dfl2560HttpAlgName"),
        ("DFL2560-MIB", "dfl2560HttpAlgTotalRequested"),
        ("DFL2560-MIB", "dfl2560HttpAlgTotalAllowed"),
        ("DFL2560-MIB", "dfl2560HttpAlgTotalBlocked"),
        ("DFL2560-MIB", "dfl2560HttpAlgCntFltName"),
        ("DFL2560-MIB", "dfl2560HttpAlgCntFltRequests"),
        ("DFL2560-MIB", "dfl2560HttpAlgCntFltAllowed"),
        ("DFL2560-MIB", "dfl2560HttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl2560AlgGroup.setStatus("current")

dfl2560HAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 14)
)
dfl2560HAGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560HASyncSendQueueLength"),
        ("DFL2560-MIB", "dfl2560HASyncSendQueueUsagePkt"),
        ("DFL2560-MIB", "dfl2560HASyncSendQueueUsageOct"),
        ("DFL2560-MIB", "dfl2560HASyncSentPackets"),
        ("DFL2560-MIB", "dfl2560HASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl2560HAGroup.setStatus("current")

dfl2560IfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 15)
)
dfl2560IfVlanGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560IfVlanUntaggedInPkts"),
        ("DFL2560-MIB", "dfl2560IfVlanUntaggedOutPkts"),
        ("DFL2560-MIB", "dfl2560IfVlanUntaggedTotPkts"),
        ("DFL2560-MIB", "dfl2560IfVlanUntaggedInOctets"),
        ("DFL2560-MIB", "dfl2560IfVlanUntaggedOutOctets"),
        ("DFL2560-MIB", "dfl2560IfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl2560IfVlanGroup.setStatus("current")

dfl2560SmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 16)
)
dfl2560SmtpAlgGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560SmtpAlgName"),
        ("DFL2560-MIB", "dfl2560SmtpAlgTotCheckedSes"),
        ("DFL2560-MIB", "dfl2560SmtpAlgTotSpamSes"),
        ("DFL2560-MIB", "dfl2560SmtpAlgTotDroppedSes"),
        ("DFL2560-MIB", "dfl2560SmtpAlgDnsBlName"),
        ("DFL2560-MIB", "dfl2560SmtpAlgDnsBlChecked"),
        ("DFL2560-MIB", "dfl2560SmtpAlgDnsBlMatched"),
        ("DFL2560-MIB", "dfl2560SmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl2560SmtpAlgGroup.setStatus("current")

dfl2560SysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 3, 1, 17)
)
dfl2560SysTCPGroup.setObjects(
      *(("DFL2560-MIB", "dfl2560SysTCPRecvSmall"),
        ("DFL2560-MIB", "dfl2560SysTCPRecvLarge"),
        ("DFL2560-MIB", "dfl2560SysTCPSendSmall"),
        ("DFL2560-MIB", "dfl2560SysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl2560SysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl2560StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl2560StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL2560-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "utmFirewall": utmFirewall,
       "dfl2560": dfl2560,
       "dfl2560OS": dfl2560OS,
       "dfl2560OSStats": dfl2560OSStats,
       "dfl2560System": dfl2560System,
       "dfl2560SysCpuLoad": dfl2560SysCpuLoad,
       "dfl2560SysForwardedBits": dfl2560SysForwardedBits,
       "dfl2560SysForwardedPackets": dfl2560SysForwardedPackets,
       "dfl2560SysBuffUse": dfl2560SysBuffUse,
       "dfl2560SysConns": dfl2560SysConns,
       "dfl2560SysPerStateCounters": dfl2560SysPerStateCounters,
       "dfl2560SysPscTcpSyn": dfl2560SysPscTcpSyn,
       "dfl2560SysPscTcpOpen": dfl2560SysPscTcpOpen,
       "dfl2560SysPscTcpFin": dfl2560SysPscTcpFin,
       "dfl2560SysPscUdp": dfl2560SysPscUdp,
       "dfl2560SysPscIcmp": dfl2560SysPscIcmp,
       "dfl2560SysPscOther": dfl2560SysPscOther,
       "dfl2560IfStatsTable": dfl2560IfStatsTable,
       "dfl2560IfStatsEntry": dfl2560IfStatsEntry,
       "dfl2560IfStatsIndex": dfl2560IfStatsIndex,
       "dfl2560IfName": dfl2560IfName,
       "dfl2560IfFragsIn": dfl2560IfFragsIn,
       "dfl2560IfFragReassOk": dfl2560IfFragReassOk,
       "dfl2560IfFragReassFail": dfl2560IfFragReassFail,
       "dfl2560IfPktsInCnt": dfl2560IfPktsInCnt,
       "dfl2560IfPktsOutCnt": dfl2560IfPktsOutCnt,
       "dfl2560IfBitsInCnt": dfl2560IfBitsInCnt,
       "dfl2560IfBitsOutCnt": dfl2560IfBitsOutCnt,
       "dfl2560IfPktsTotCnt": dfl2560IfPktsTotCnt,
       "dfl2560IfBitsTotCnt": dfl2560IfBitsTotCnt,
       "dfl2560IfHCPktsInCnt": dfl2560IfHCPktsInCnt,
       "dfl2560IfHCPktsOutCnt": dfl2560IfHCPktsOutCnt,
       "dfl2560IfHCBitsInCnt": dfl2560IfHCBitsInCnt,
       "dfl2560IfHCBitsOutCnt": dfl2560IfHCBitsOutCnt,
       "dfl2560IfHCPktsTotCnt": dfl2560IfHCPktsTotCnt,
       "dfl2560IfHCBitsTotCnt": dfl2560IfHCBitsTotCnt,
       "dfl2560IfRxRingTable": dfl2560IfRxRingTable,
       "dfl2560IfRxRingEntry": dfl2560IfRxRingEntry,
       "dfl2560IfRxRingIndex": dfl2560IfRxRingIndex,
       "dfl2560IfRxRingFifoErrors": dfl2560IfRxRingFifoErrors,
       "dfl2560IfRxDespools": dfl2560IfRxDespools,
       "dfl2560IfRxAvgUse": dfl2560IfRxAvgUse,
       "dfl2560IfRxRingSaturation": dfl2560IfRxRingSaturation,
       "dfl2560RxRingFlooded": dfl2560RxRingFlooded,
       "dfl2560IfTxRingTable": dfl2560IfTxRingTable,
       "dfl2560IfTxRingEntry": dfl2560IfTxRingEntry,
       "dfl2560IfTxRingIndex": dfl2560IfTxRingIndex,
       "dfl2560IfTxDespools": dfl2560IfTxDespools,
       "dfl2560IfTxAvgUse": dfl2560IfTxAvgUse,
       "dfl2560IfTxRingSaturation": dfl2560IfTxRingSaturation,
       "dfl2560RxTingFlooded": dfl2560RxTingFlooded,
       "dfl2560IfVlanStatsTable": dfl2560IfVlanStatsTable,
       "dfl2560IfVlanStatsEntry": dfl2560IfVlanStatsEntry,
       "dfl2560IfVlanIndex": dfl2560IfVlanIndex,
       "dfl2560IfVlanUntaggedInPkts": dfl2560IfVlanUntaggedInPkts,
       "dfl2560IfVlanUntaggedOutPkts": dfl2560IfVlanUntaggedOutPkts,
       "dfl2560IfVlanUntaggedTotPkts": dfl2560IfVlanUntaggedTotPkts,
       "dfl2560IfVlanUntaggedInOctets": dfl2560IfVlanUntaggedInOctets,
       "dfl2560IfVlanUntaggedOutOctets": dfl2560IfVlanUntaggedOutOctets,
       "dfl2560IfVlanUntaggedTotOctets": dfl2560IfVlanUntaggedTotOctets,
       "dfl2560HWSensorTable": dfl2560HWSensorTable,
       "dfl2560HWSensorEntry": dfl2560HWSensorEntry,
       "dfl2560HWSensorIndex": dfl2560HWSensorIndex,
       "dfl2560HWSensorName": dfl2560HWSensorName,
       "dfl2560HWSensorValue": dfl2560HWSensorValue,
       "dfl2560HWSensorUnit": dfl2560HWSensorUnit,
       "dfl2560SysMemUsage": dfl2560SysMemUsage,
       "dfl2560SysTCPUsage": dfl2560SysTCPUsage,
       "dfl2560SysTCPRecvSmall": dfl2560SysTCPRecvSmall,
       "dfl2560SysTCPRecvLarge": dfl2560SysTCPRecvLarge,
       "dfl2560SysTCPSendSmall": dfl2560SysTCPSendSmall,
       "dfl2560SysTCPSendLarge": dfl2560SysTCPSendLarge,
       "dfl2560SysTimerUsage": dfl2560SysTimerUsage,
       "dfl2560SysConnOPS": dfl2560SysConnOPS,
       "dfl2560SysConnCPS": dfl2560SysConnCPS,
       "dfl2560SysHCForwardedBits": dfl2560SysHCForwardedBits,
       "dfl2560VPN": dfl2560VPN,
       "dfl2560IPsec": dfl2560IPsec,
       "dfl2560IPsecGlobal": dfl2560IPsecGlobal,
       "dfl2560IPsecPhaseOneActive": dfl2560IPsecPhaseOneActive,
       "dfl2560IPsecPhaseOneAggrModeDone": dfl2560IPsecPhaseOneAggrModeDone,
       "dfl2560IPsecQuickModeActive": dfl2560IPsecQuickModeActive,
       "dfl2560IPsecPhaseOneDone": dfl2560IPsecPhaseOneDone,
       "dfl2560IPsecPhaseOneFailed": dfl2560IPsecPhaseOneFailed,
       "dfl2560IPsecPhaseOneRekeyed": dfl2560IPsecPhaseOneRekeyed,
       "dfl2560IPsecQuickModeDone": dfl2560IPsecQuickModeDone,
       "dfl2560IPsecQuickModeFailed": dfl2560IPsecQuickModeFailed,
       "dfl2560IPsecInfoDone": dfl2560IPsecInfoDone,
       "dfl2560IPsecInfoFailed": dfl2560IPsecInfoFailed,
       "dfl2560IPsecInOctetsComp": dfl2560IPsecInOctetsComp,
       "dfl2560IPsecInOctetsUncomp": dfl2560IPsecInOctetsUncomp,
       "dfl2560IPsecOutOctetsComp": dfl2560IPsecOutOctetsComp,
       "dfl2560IPsecOutOctetsUncomp": dfl2560IPsecOutOctetsUncomp,
       "dfl2560IPsecForwardedOctetsComp": dfl2560IPsecForwardedOctetsComp,
       "dfl2560IPsecForwardedOctetsUcomp": dfl2560IPsecForwardedOctetsUcomp,
       "dfl2560IPsecInPackets": dfl2560IPsecInPackets,
       "dfl2560IPsecOutPackets": dfl2560IPsecOutPackets,
       "dfl2560IPsecForwardedPackets": dfl2560IPsecForwardedPackets,
       "dfl2560IPsecActiveTransforms": dfl2560IPsecActiveTransforms,
       "dfl2560IPsecTotalTransforms": dfl2560IPsecTotalTransforms,
       "dfl2560IPsecOutOfTransforms": dfl2560IPsecOutOfTransforms,
       "dfl2560IPsecTotalRekeys": dfl2560IPsecTotalRekeys,
       "dfl2560Rules": dfl2560Rules,
       "dfl2560RuleUseTable": dfl2560RuleUseTable,
       "dfl2560RuleUseEntry": dfl2560RuleUseEntry,
       "dfl2560RuleIndex": dfl2560RuleIndex,
       "dfl2560RuleName": dfl2560RuleName,
       "dfl2560RuleUse": dfl2560RuleUse,
       "dfl2560IPPools": dfl2560IPPools,
       "dfl2560IPPoolsNumber": dfl2560IPPoolsNumber,
       "dfl2560IPPoolTable": dfl2560IPPoolTable,
       "dfl2560IPPoolEntry": dfl2560IPPoolEntry,
       "dfl2560IPPoolIndex": dfl2560IPPoolIndex,
       "dfl2560IPPoolName": dfl2560IPPoolName,
       "dfl2560IPPoolPrepare": dfl2560IPPoolPrepare,
       "dfl2560IPPoolFree": dfl2560IPPoolFree,
       "dfl2560IPPoolMisses": dfl2560IPPoolMisses,
       "dfl2560IPPoolClientFails": dfl2560IPPoolClientFails,
       "dfl2560IPPoolUsed": dfl2560IPPoolUsed,
       "dfl2560DHCPServer": dfl2560DHCPServer,
       "dfl2560DHCPTotalRejected": dfl2560DHCPTotalRejected,
       "dfl2560DHCPRuleTable": dfl2560DHCPRuleTable,
       "dfl2560DHCPRuleEntry": dfl2560DHCPRuleEntry,
       "dfl2560DHCPRuleIndex": dfl2560DHCPRuleIndex,
       "dfl2560DHCPRuleName": dfl2560DHCPRuleName,
       "dfl2560DHCPRuleUsage": dfl2560DHCPRuleUsage,
       "dfl2560DHCPRuleUsagePercent": dfl2560DHCPRuleUsagePercent,
       "dfl2560DHCPActiveClients": dfl2560DHCPActiveClients,
       "dfl2560DHCPActiveClientsPercent": dfl2560DHCPActiveClientsPercent,
       "dfl2560DHCPRejectedRequests": dfl2560DHCPRejectedRequests,
       "dfl2560DHCPTotalLeases": dfl2560DHCPTotalLeases,
       "dfl2560UserAuth": dfl2560UserAuth,
       "dfl2560UserAuthHTTPUsers": dfl2560UserAuthHTTPUsers,
       "dfl2560UserAuthXAUTHUsers": dfl2560UserAuthXAUTHUsers,
       "dfl2560UserAuthHTTPSUsers": dfl2560UserAuthHTTPSUsers,
       "dfl2560UserAuthPPPUsers": dfl2560UserAuthPPPUsers,
       "dfl2560UserAuthEAPUsers": dfl2560UserAuthEAPUsers,
       "dfl2560UserAuthRuleUseTable": dfl2560UserAuthRuleUseTable,
       "dfl2560UserAuthRuleUseEntry": dfl2560UserAuthRuleUseEntry,
       "dfl2560UserAuthRuleIndex": dfl2560UserAuthRuleIndex,
       "dfl2560UserAuthRuleName": dfl2560UserAuthRuleName,
       "dfl2560UserAuthRuleUse": dfl2560UserAuthRuleUse,
       "dfl2560LinkMonitor": dfl2560LinkMonitor,
       "dfl2560LinkMonGrp": dfl2560LinkMonGrp,
       "dfl2560LinkMonGrpTable": dfl2560LinkMonGrpTable,
       "dfl2560LinkMonGrpEntry": dfl2560LinkMonGrpEntry,
       "dfl2560LinkMonGrpIndex": dfl2560LinkMonGrpIndex,
       "dfl2560LinkMonGrpName": dfl2560LinkMonGrpName,
       "dfl2560LinkMonGrpHostsUp": dfl2560LinkMonGrpHostsUp,
       "dfl2560LinkMonHostTable": dfl2560LinkMonHostTable,
       "dfl2560LinkMonHostEntry": dfl2560LinkMonHostEntry,
       "dfl2560LinkMonHostIndex": dfl2560LinkMonHostIndex,
       "dfl2560LinkMonHostId": dfl2560LinkMonHostId,
       "dfl2560LinkMonHostShortTermLoss": dfl2560LinkMonHostShortTermLoss,
       "dfl2560LinkMonHostPacketsLost": dfl2560LinkMonHostPacketsLost,
       "dfl2560Pipes": dfl2560Pipes,
       "dfl2560PipeUsers": dfl2560PipeUsers,
       "dfl2560PipeTable": dfl2560PipeTable,
       "dfl2560PipeEntry": dfl2560PipeEntry,
       "dfl2560PipeIndex": dfl2560PipeIndex,
       "dfl2560PipeName": dfl2560PipeName,
       "dfl2560PipeMinPrec": dfl2560PipeMinPrec,
       "dfl2560PipeMaxPrec": dfl2560PipeMaxPrec,
       "dfl2560PipeDefPrec": dfl2560PipeDefPrec,
       "dfl2560PipeNumPrec": dfl2560PipeNumPrec,
       "dfl2560PipeNumUsers": dfl2560PipeNumUsers,
       "dfl2560PipeCurrentBps": dfl2560PipeCurrentBps,
       "dfl2560PipeCurrentPps": dfl2560PipeCurrentPps,
       "dfl2560PipeDelayedPackets": dfl2560PipeDelayedPackets,
       "dfl2560PipeDropedPackets": dfl2560PipeDropedPackets,
       "dfl2560PipePrecTable": dfl2560PipePrecTable,
       "dfl2560PipePrecEntry": dfl2560PipePrecEntry,
       "dfl2560PipePrecIndex": dfl2560PipePrecIndex,
       "dfl2560PipePrec": dfl2560PipePrec,
       "dfl2560PipePrecBps": dfl2560PipePrecBps,
       "dfl2560PipePrecTotalPps": dfl2560PipePrecTotalPps,
       "dfl2560PipePrecReservedBps": dfl2560PipePrecReservedBps,
       "dfl2560PipePrecDynLimBps": dfl2560PipePrecDynLimBps,
       "dfl2560PipePrecDynUsrLimBps": dfl2560PipePrecDynUsrLimBps,
       "dfl2560PipePrecDelayedPackets": dfl2560PipePrecDelayedPackets,
       "dfl2560PipePrecDropedPackets": dfl2560PipePrecDropedPackets,
       "dfl2560ALG": dfl2560ALG,
       "dfl2560AlgSessions": dfl2560AlgSessions,
       "dfl2560AlgConnections": dfl2560AlgConnections,
       "dfl2560AlgTCPStreams": dfl2560AlgTCPStreams,
       "dfl2560HttpAlg": dfl2560HttpAlg,
       "dfl2560HttpAlgTable": dfl2560HttpAlgTable,
       "dfl2560HttpAlgEntry": dfl2560HttpAlgEntry,
       "dfl2560HttpAlgIndex": dfl2560HttpAlgIndex,
       "dfl2560HttpAlgName": dfl2560HttpAlgName,
       "dfl2560HttpAlgTotalRequested": dfl2560HttpAlgTotalRequested,
       "dfl2560HttpAlgTotalAllowed": dfl2560HttpAlgTotalAllowed,
       "dfl2560HttpAlgTotalBlocked": dfl2560HttpAlgTotalBlocked,
       "dfl2560HttpAlgCntFltTable": dfl2560HttpAlgCntFltTable,
       "dfl2560HttpAlgCntFltEntry": dfl2560HttpAlgCntFltEntry,
       "dfl2560HttpAlgCntFltIndex": dfl2560HttpAlgCntFltIndex,
       "dfl2560HttpAlgCntFltName": dfl2560HttpAlgCntFltName,
       "dfl2560HttpAlgCntFltRequests": dfl2560HttpAlgCntFltRequests,
       "dfl2560HttpAlgCntFltAllowed": dfl2560HttpAlgCntFltAllowed,
       "dfl2560HttpAlgCntFltBlocked": dfl2560HttpAlgCntFltBlocked,
       "dfl2560SmtpAlg": dfl2560SmtpAlg,
       "dfl2560SmtpAlgTable": dfl2560SmtpAlgTable,
       "dfl2560SmtpAlgEntry": dfl2560SmtpAlgEntry,
       "dfl2560SmtpAlgIndex": dfl2560SmtpAlgIndex,
       "dfl2560SmtpAlgName": dfl2560SmtpAlgName,
       "dfl2560SmtpAlgTotCheckedSes": dfl2560SmtpAlgTotCheckedSes,
       "dfl2560SmtpAlgTotSpamSes": dfl2560SmtpAlgTotSpamSes,
       "dfl2560SmtpAlgTotDroppedSes": dfl2560SmtpAlgTotDroppedSes,
       "dfl2560SmtpAlgDnsBlTable": dfl2560SmtpAlgDnsBlTable,
       "dfl2560SmtpAlgDnsBlEntry": dfl2560SmtpAlgDnsBlEntry,
       "dfl2560SmtpAlgDnsBlIndex": dfl2560SmtpAlgDnsBlIndex,
       "dfl2560SmtpAlgDnsBlName": dfl2560SmtpAlgDnsBlName,
       "dfl2560SmtpAlgDnsBlChecked": dfl2560SmtpAlgDnsBlChecked,
       "dfl2560SmtpAlgDnsBlMatched": dfl2560SmtpAlgDnsBlMatched,
       "dfl2560SmtpAlgDnsBlFailChecks": dfl2560SmtpAlgDnsBlFailChecks,
       "dfl2560DHCPRelay": dfl2560DHCPRelay,
       "dfl2560DHCPRelayCurClients": dfl2560DHCPRelayCurClients,
       "dfl2560DHCPRelayCurTrans": dfl2560DHCPRelayCurTrans,
       "dfl2560DHCPRelayRejected": dfl2560DHCPRelayRejected,
       "dfl2560DHCPRelayRuleTable": dfl2560DHCPRelayRuleTable,
       "dfl2560DHCPRelayRuleEntry": dfl2560DHCPRelayRuleEntry,
       "dfl2560DHCPRelayRuleIndex": dfl2560DHCPRelayRuleIndex,
       "dfl2560DHCPRelayRuleName": dfl2560DHCPRelayRuleName,
       "dfl2560DHCPRelayRuleHits": dfl2560DHCPRelayRuleHits,
       "dfl2560DHCPRelayRuleCurClients": dfl2560DHCPRelayRuleCurClients,
       "dfl2560DHCPRelayRuleRejCliPkts": dfl2560DHCPRelayRuleRejCliPkts,
       "dfl2560DHCPRelayRuleRejSrvPkts": dfl2560DHCPRelayRuleRejSrvPkts,
       "dfl2560HA": dfl2560HA,
       "dfl2560HASyncSendQueueLength": dfl2560HASyncSendQueueLength,
       "dfl2560HASyncSendQueueUsagePkt": dfl2560HASyncSendQueueUsagePkt,
       "dfl2560HASyncSendQueueUsageOct": dfl2560HASyncSendQueueUsageOct,
       "dfl2560HASyncSentPackets": dfl2560HASyncSentPackets,
       "dfl2560HASyncSendResentPackets": dfl2560HASyncSendResentPackets,
       "dfl2560reg": dfl2560reg,
       "dfl2560MibModules": dfl2560MibModules,
       "dfl2560-MIB": dfl2560_MIB,
       "dfl2560MibConfs": dfl2560MibConfs,
       "dfl2560StatsConformance": dfl2560StatsConformance,
       "dfl2560StatsCompliance": dfl2560StatsCompliance,
       "dfl2560MibObjectGroups": dfl2560MibObjectGroups,
       "dfl2560StatsRegGroups": dfl2560StatsRegGroups,
       "dfl2560SystemObjectGroup": dfl2560SystemObjectGroup,
       "dfl2560IPsecObjectGroup": dfl2560IPsecObjectGroup,
       "dfl2560StateCountersGroup": dfl2560StateCountersGroup,
       "dfl2560IPPoolGroup": dfl2560IPPoolGroup,
       "dfl2560DHCPServerGroup": dfl2560DHCPServerGroup,
       "dfl2560RuleUseGroup": dfl2560RuleUseGroup,
       "dfl2560UserAuthGroup": dfl2560UserAuthGroup,
       "dfl2560IfStatsGroup": dfl2560IfStatsGroup,
       "dfl2560LinkMonitorGroup": dfl2560LinkMonitorGroup,
       "dfl2560PipesObjectGroup": dfl2560PipesObjectGroup,
       "dfl2560DHCPRelayObjectGroup": dfl2560DHCPRelayObjectGroup,
       "dfl2560AlgGroup": dfl2560AlgGroup,
       "dfl2560HAGroup": dfl2560HAGroup,
       "dfl2560IfVlanGroup": dfl2560IfVlanGroup,
       "dfl2560SmtpAlgGroup": dfl2560SmtpAlgGroup,
       "dfl2560SysTCPGroup": dfl2560SysTCPGroup}
)
