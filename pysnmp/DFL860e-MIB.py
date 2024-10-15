# SNMP MIB module (DFL860e-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL860e-MIB
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

dfl860e_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 1, 2)
)
dfl860e_MIB.setRevisions(
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
_Dfl860e_ObjectIdentity = ObjectIdentity
dfl860e = _Dfl860e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7)
)
_Dfl860eOS_ObjectIdentity = ObjectIdentity
dfl860eOS = _Dfl860eOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1)
)
_Dfl860eOSStats_ObjectIdentity = ObjectIdentity
dfl860eOSStats = _Dfl860eOSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2)
)
_Dfl860eSystem_ObjectIdentity = ObjectIdentity
dfl860eSystem = _Dfl860eSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1)
)
_Dfl860eSysCpuLoad_Type = Gauge32
_Dfl860eSysCpuLoad_Object = MibScalar
dfl860eSysCpuLoad = _Dfl860eSysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 1),
    _Dfl860eSysCpuLoad_Type()
)
dfl860eSysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysCpuLoad.setStatus("current")
_Dfl860eSysForwardedBits_Type = Counter32
_Dfl860eSysForwardedBits_Object = MibScalar
dfl860eSysForwardedBits = _Dfl860eSysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 2),
    _Dfl860eSysForwardedBits_Type()
)
dfl860eSysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysForwardedBits.setStatus("current")
_Dfl860eSysForwardedPackets_Type = Counter32
_Dfl860eSysForwardedPackets_Object = MibScalar
dfl860eSysForwardedPackets = _Dfl860eSysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 3),
    _Dfl860eSysForwardedPackets_Type()
)
dfl860eSysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysForwardedPackets.setStatus("current")
_Dfl860eSysBuffUse_Type = Gauge32
_Dfl860eSysBuffUse_Object = MibScalar
dfl860eSysBuffUse = _Dfl860eSysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 4),
    _Dfl860eSysBuffUse_Type()
)
dfl860eSysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysBuffUse.setStatus("current")
_Dfl860eSysConns_Type = Gauge32
_Dfl860eSysConns_Object = MibScalar
dfl860eSysConns = _Dfl860eSysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 5),
    _Dfl860eSysConns_Type()
)
dfl860eSysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysConns.setStatus("current")
_Dfl860eSysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl860eSysPerStateCounters = _Dfl860eSysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6)
)
_Dfl860eSysPscTcpSyn_Type = Gauge32
_Dfl860eSysPscTcpSyn_Object = MibScalar
dfl860eSysPscTcpSyn = _Dfl860eSysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6, 1),
    _Dfl860eSysPscTcpSyn_Type()
)
dfl860eSysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysPscTcpSyn.setStatus("current")
_Dfl860eSysPscTcpOpen_Type = Gauge32
_Dfl860eSysPscTcpOpen_Object = MibScalar
dfl860eSysPscTcpOpen = _Dfl860eSysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6, 2),
    _Dfl860eSysPscTcpOpen_Type()
)
dfl860eSysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysPscTcpOpen.setStatus("current")
_Dfl860eSysPscTcpFin_Type = Gauge32
_Dfl860eSysPscTcpFin_Object = MibScalar
dfl860eSysPscTcpFin = _Dfl860eSysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6, 3),
    _Dfl860eSysPscTcpFin_Type()
)
dfl860eSysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysPscTcpFin.setStatus("current")
_Dfl860eSysPscUdp_Type = Gauge32
_Dfl860eSysPscUdp_Object = MibScalar
dfl860eSysPscUdp = _Dfl860eSysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6, 4),
    _Dfl860eSysPscUdp_Type()
)
dfl860eSysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysPscUdp.setStatus("current")
_Dfl860eSysPscIcmp_Type = Gauge32
_Dfl860eSysPscIcmp_Object = MibScalar
dfl860eSysPscIcmp = _Dfl860eSysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6, 5),
    _Dfl860eSysPscIcmp_Type()
)
dfl860eSysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysPscIcmp.setStatus("current")
_Dfl860eSysPscOther_Type = Gauge32
_Dfl860eSysPscOther_Object = MibScalar
dfl860eSysPscOther = _Dfl860eSysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 6, 6),
    _Dfl860eSysPscOther_Type()
)
dfl860eSysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysPscOther.setStatus("current")
_Dfl860eIfStatsTable_Object = MibTable
dfl860eIfStatsTable = _Dfl860eIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl860eIfStatsTable.setStatus("current")
_Dfl860eIfStatsEntry_Object = MibTableRow
dfl860eIfStatsEntry = _Dfl860eIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1)
)
dfl860eIfStatsEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eIfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl860eIfStatsEntry.setStatus("current")


class _Dfl860eIfStatsIndex_Type(Integer32):
    """Custom type dfl860eIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eIfStatsIndex_Type.__name__ = "Integer32"
_Dfl860eIfStatsIndex_Object = MibTableColumn
dfl860eIfStatsIndex = _Dfl860eIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 1),
    _Dfl860eIfStatsIndex_Type()
)
dfl860eIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eIfStatsIndex.setStatus("current")
_Dfl860eIfName_Type = DisplayString
_Dfl860eIfName_Object = MibTableColumn
dfl860eIfName = _Dfl860eIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 2),
    _Dfl860eIfName_Type()
)
dfl860eIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfName.setStatus("current")
_Dfl860eIfFragsIn_Type = Counter32
_Dfl860eIfFragsIn_Object = MibTableColumn
dfl860eIfFragsIn = _Dfl860eIfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 3),
    _Dfl860eIfFragsIn_Type()
)
dfl860eIfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfFragsIn.setStatus("current")
_Dfl860eIfFragReassOk_Type = Counter32
_Dfl860eIfFragReassOk_Object = MibTableColumn
dfl860eIfFragReassOk = _Dfl860eIfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 4),
    _Dfl860eIfFragReassOk_Type()
)
dfl860eIfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfFragReassOk.setStatus("current")
_Dfl860eIfFragReassFail_Type = Counter32
_Dfl860eIfFragReassFail_Object = MibTableColumn
dfl860eIfFragReassFail = _Dfl860eIfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 5),
    _Dfl860eIfFragReassFail_Type()
)
dfl860eIfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfFragReassFail.setStatus("current")
_Dfl860eIfPktsInCnt_Type = Counter32
_Dfl860eIfPktsInCnt_Object = MibTableColumn
dfl860eIfPktsInCnt = _Dfl860eIfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 6),
    _Dfl860eIfPktsInCnt_Type()
)
dfl860eIfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfPktsInCnt.setStatus("current")
_Dfl860eIfPktsOutCnt_Type = Counter32
_Dfl860eIfPktsOutCnt_Object = MibTableColumn
dfl860eIfPktsOutCnt = _Dfl860eIfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 7),
    _Dfl860eIfPktsOutCnt_Type()
)
dfl860eIfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfPktsOutCnt.setStatus("current")
_Dfl860eIfBitsInCnt_Type = Counter32
_Dfl860eIfBitsInCnt_Object = MibTableColumn
dfl860eIfBitsInCnt = _Dfl860eIfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 8),
    _Dfl860eIfBitsInCnt_Type()
)
dfl860eIfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfBitsInCnt.setStatus("current")
_Dfl860eIfBitsOutCnt_Type = Counter32
_Dfl860eIfBitsOutCnt_Object = MibTableColumn
dfl860eIfBitsOutCnt = _Dfl860eIfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 9),
    _Dfl860eIfBitsOutCnt_Type()
)
dfl860eIfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfBitsOutCnt.setStatus("current")
_Dfl860eIfPktsTotCnt_Type = Counter32
_Dfl860eIfPktsTotCnt_Object = MibTableColumn
dfl860eIfPktsTotCnt = _Dfl860eIfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 10),
    _Dfl860eIfPktsTotCnt_Type()
)
dfl860eIfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfPktsTotCnt.setStatus("current")
_Dfl860eIfBitsTotCnt_Type = Counter32
_Dfl860eIfBitsTotCnt_Object = MibTableColumn
dfl860eIfBitsTotCnt = _Dfl860eIfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 11),
    _Dfl860eIfBitsTotCnt_Type()
)
dfl860eIfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfBitsTotCnt.setStatus("current")
_Dfl860eIfHCPktsInCnt_Type = Counter64
_Dfl860eIfHCPktsInCnt_Object = MibTableColumn
dfl860eIfHCPktsInCnt = _Dfl860eIfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 12),
    _Dfl860eIfHCPktsInCnt_Type()
)
dfl860eIfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfHCPktsInCnt.setStatus("current")
_Dfl860eIfHCPktsOutCnt_Type = Counter64
_Dfl860eIfHCPktsOutCnt_Object = MibTableColumn
dfl860eIfHCPktsOutCnt = _Dfl860eIfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 13),
    _Dfl860eIfHCPktsOutCnt_Type()
)
dfl860eIfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfHCPktsOutCnt.setStatus("current")
_Dfl860eIfHCBitsInCnt_Type = Counter64
_Dfl860eIfHCBitsInCnt_Object = MibTableColumn
dfl860eIfHCBitsInCnt = _Dfl860eIfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 14),
    _Dfl860eIfHCBitsInCnt_Type()
)
dfl860eIfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfHCBitsInCnt.setStatus("current")
_Dfl860eIfHCBitsOutCnt_Type = Counter64
_Dfl860eIfHCBitsOutCnt_Object = MibTableColumn
dfl860eIfHCBitsOutCnt = _Dfl860eIfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 15),
    _Dfl860eIfHCBitsOutCnt_Type()
)
dfl860eIfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfHCBitsOutCnt.setStatus("current")
_Dfl860eIfHCPktsTotCnt_Type = Counter64
_Dfl860eIfHCPktsTotCnt_Object = MibTableColumn
dfl860eIfHCPktsTotCnt = _Dfl860eIfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 16),
    _Dfl860eIfHCPktsTotCnt_Type()
)
dfl860eIfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfHCPktsTotCnt.setStatus("current")
_Dfl860eIfHCBitsTotCnt_Type = Counter64
_Dfl860eIfHCBitsTotCnt_Object = MibTableColumn
dfl860eIfHCBitsTotCnt = _Dfl860eIfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 7, 1, 17),
    _Dfl860eIfHCBitsTotCnt_Type()
)
dfl860eIfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfHCBitsTotCnt.setStatus("current")
_Dfl860eIfRxRingTable_Object = MibTable
dfl860eIfRxRingTable = _Dfl860eIfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl860eIfRxRingTable.setStatus("current")
_Dfl860eIfRxRingEntry_Object = MibTableRow
dfl860eIfRxRingEntry = _Dfl860eIfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1)
)
dfl860eIfRxRingEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eIfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl860eIfRxRingEntry.setStatus("current")


class _Dfl860eIfRxRingIndex_Type(Integer32):
    """Custom type dfl860eIfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eIfRxRingIndex_Type.__name__ = "Integer32"
_Dfl860eIfRxRingIndex_Object = MibTableColumn
dfl860eIfRxRingIndex = _Dfl860eIfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1, 1),
    _Dfl860eIfRxRingIndex_Type()
)
dfl860eIfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eIfRxRingIndex.setStatus("current")
_Dfl860eIfRxRingFifoErrors_Type = Counter32
_Dfl860eIfRxRingFifoErrors_Object = MibTableColumn
dfl860eIfRxRingFifoErrors = _Dfl860eIfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1, 2),
    _Dfl860eIfRxRingFifoErrors_Type()
)
dfl860eIfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfRxRingFifoErrors.setStatus("current")
_Dfl860eIfRxDespools_Type = Gauge32
_Dfl860eIfRxDespools_Object = MibTableColumn
dfl860eIfRxDespools = _Dfl860eIfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1, 3),
    _Dfl860eIfRxDespools_Type()
)
dfl860eIfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfRxDespools.setStatus("current")
_Dfl860eIfRxAvgUse_Type = Gauge32
_Dfl860eIfRxAvgUse_Object = MibTableColumn
dfl860eIfRxAvgUse = _Dfl860eIfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1, 4),
    _Dfl860eIfRxAvgUse_Type()
)
dfl860eIfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfRxAvgUse.setStatus("current")
_Dfl860eIfRxRingSaturation_Type = Gauge32
_Dfl860eIfRxRingSaturation_Object = MibTableColumn
dfl860eIfRxRingSaturation = _Dfl860eIfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1, 5),
    _Dfl860eIfRxRingSaturation_Type()
)
dfl860eIfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfRxRingSaturation.setStatus("current")
_Dfl860eRxRingFlooded_Type = Gauge32
_Dfl860eRxRingFlooded_Object = MibTableColumn
dfl860eRxRingFlooded = _Dfl860eRxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 8, 1, 6),
    _Dfl860eRxRingFlooded_Type()
)
dfl860eRxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eRxRingFlooded.setStatus("current")
_Dfl860eIfTxRingTable_Object = MibTable
dfl860eIfTxRingTable = _Dfl860eIfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl860eIfTxRingTable.setStatus("current")
_Dfl860eIfTxRingEntry_Object = MibTableRow
dfl860eIfTxRingEntry = _Dfl860eIfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9, 1)
)
dfl860eIfTxRingEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eIfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl860eIfTxRingEntry.setStatus("current")


class _Dfl860eIfTxRingIndex_Type(Integer32):
    """Custom type dfl860eIfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eIfTxRingIndex_Type.__name__ = "Integer32"
_Dfl860eIfTxRingIndex_Object = MibTableColumn
dfl860eIfTxRingIndex = _Dfl860eIfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9, 1, 1),
    _Dfl860eIfTxRingIndex_Type()
)
dfl860eIfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eIfTxRingIndex.setStatus("current")
_Dfl860eIfTxDespools_Type = Gauge32
_Dfl860eIfTxDespools_Object = MibTableColumn
dfl860eIfTxDespools = _Dfl860eIfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9, 1, 2),
    _Dfl860eIfTxDespools_Type()
)
dfl860eIfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfTxDespools.setStatus("current")
_Dfl860eIfTxAvgUse_Type = Gauge32
_Dfl860eIfTxAvgUse_Object = MibTableColumn
dfl860eIfTxAvgUse = _Dfl860eIfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9, 1, 3),
    _Dfl860eIfTxAvgUse_Type()
)
dfl860eIfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfTxAvgUse.setStatus("current")
_Dfl860eIfTxRingSaturation_Type = Gauge32
_Dfl860eIfTxRingSaturation_Object = MibTableColumn
dfl860eIfTxRingSaturation = _Dfl860eIfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9, 1, 4),
    _Dfl860eIfTxRingSaturation_Type()
)
dfl860eIfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfTxRingSaturation.setStatus("current")
_Dfl860eRxTingFlooded_Type = Gauge32
_Dfl860eRxTingFlooded_Object = MibTableColumn
dfl860eRxTingFlooded = _Dfl860eRxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 9, 1, 5),
    _Dfl860eRxTingFlooded_Type()
)
dfl860eRxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eRxTingFlooded.setStatus("current")
_Dfl860eIfVlanStatsTable_Object = MibTable
dfl860eIfVlanStatsTable = _Dfl860eIfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl860eIfVlanStatsTable.setStatus("current")
_Dfl860eIfVlanStatsEntry_Object = MibTableRow
dfl860eIfVlanStatsEntry = _Dfl860eIfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1)
)
dfl860eIfVlanStatsEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eIfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl860eIfVlanStatsEntry.setStatus("current")


class _Dfl860eIfVlanIndex_Type(Integer32):
    """Custom type dfl860eIfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eIfVlanIndex_Type.__name__ = "Integer32"
_Dfl860eIfVlanIndex_Object = MibTableColumn
dfl860eIfVlanIndex = _Dfl860eIfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 1),
    _Dfl860eIfVlanIndex_Type()
)
dfl860eIfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eIfVlanIndex.setStatus("current")
_Dfl860eIfVlanUntaggedInPkts_Type = Counter32
_Dfl860eIfVlanUntaggedInPkts_Object = MibTableColumn
dfl860eIfVlanUntaggedInPkts = _Dfl860eIfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 2),
    _Dfl860eIfVlanUntaggedInPkts_Type()
)
dfl860eIfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfVlanUntaggedInPkts.setStatus("current")
_Dfl860eIfVlanUntaggedOutPkts_Type = Counter32
_Dfl860eIfVlanUntaggedOutPkts_Object = MibTableColumn
dfl860eIfVlanUntaggedOutPkts = _Dfl860eIfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 3),
    _Dfl860eIfVlanUntaggedOutPkts_Type()
)
dfl860eIfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfVlanUntaggedOutPkts.setStatus("current")
_Dfl860eIfVlanUntaggedTotPkts_Type = Counter32
_Dfl860eIfVlanUntaggedTotPkts_Object = MibTableColumn
dfl860eIfVlanUntaggedTotPkts = _Dfl860eIfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 4),
    _Dfl860eIfVlanUntaggedTotPkts_Type()
)
dfl860eIfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfVlanUntaggedTotPkts.setStatus("current")
_Dfl860eIfVlanUntaggedInOctets_Type = Counter32
_Dfl860eIfVlanUntaggedInOctets_Object = MibTableColumn
dfl860eIfVlanUntaggedInOctets = _Dfl860eIfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 5),
    _Dfl860eIfVlanUntaggedInOctets_Type()
)
dfl860eIfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfVlanUntaggedInOctets.setStatus("current")
_Dfl860eIfVlanUntaggedOutOctets_Type = Counter32
_Dfl860eIfVlanUntaggedOutOctets_Object = MibTableColumn
dfl860eIfVlanUntaggedOutOctets = _Dfl860eIfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 6),
    _Dfl860eIfVlanUntaggedOutOctets_Type()
)
dfl860eIfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfVlanUntaggedOutOctets.setStatus("current")
_Dfl860eIfVlanUntaggedTotOctets_Type = Counter32
_Dfl860eIfVlanUntaggedTotOctets_Object = MibTableColumn
dfl860eIfVlanUntaggedTotOctets = _Dfl860eIfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 10, 1, 7),
    _Dfl860eIfVlanUntaggedTotOctets_Type()
)
dfl860eIfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIfVlanUntaggedTotOctets.setStatus("current")
_Dfl860eHWSensorTable_Object = MibTable
dfl860eHWSensorTable = _Dfl860eHWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl860eHWSensorTable.setStatus("current")
_Dfl860eHWSensorEntry_Object = MibTableRow
dfl860eHWSensorEntry = _Dfl860eHWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 11, 1)
)
dfl860eHWSensorEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eHWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl860eHWSensorEntry.setStatus("current")


class _Dfl860eHWSensorIndex_Type(Integer32):
    """Custom type dfl860eHWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eHWSensorIndex_Type.__name__ = "Integer32"
_Dfl860eHWSensorIndex_Object = MibTableColumn
dfl860eHWSensorIndex = _Dfl860eHWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 11, 1, 1),
    _Dfl860eHWSensorIndex_Type()
)
dfl860eHWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eHWSensorIndex.setStatus("current")
_Dfl860eHWSensorName_Type = DisplayString
_Dfl860eHWSensorName_Object = MibTableColumn
dfl860eHWSensorName = _Dfl860eHWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 11, 1, 2),
    _Dfl860eHWSensorName_Type()
)
dfl860eHWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHWSensorName.setStatus("current")
_Dfl860eHWSensorValue_Type = Gauge32
_Dfl860eHWSensorValue_Object = MibTableColumn
dfl860eHWSensorValue = _Dfl860eHWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 11, 1, 3),
    _Dfl860eHWSensorValue_Type()
)
dfl860eHWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHWSensorValue.setStatus("current")
_Dfl860eHWSensorUnit_Type = DisplayString
_Dfl860eHWSensorUnit_Object = MibTableColumn
dfl860eHWSensorUnit = _Dfl860eHWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 11, 1, 4),
    _Dfl860eHWSensorUnit_Type()
)
dfl860eHWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHWSensorUnit.setStatus("current")
_Dfl860eSysMemUsage_Type = Gauge32
_Dfl860eSysMemUsage_Object = MibScalar
dfl860eSysMemUsage = _Dfl860eSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 12),
    _Dfl860eSysMemUsage_Type()
)
dfl860eSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysMemUsage.setStatus("current")
_Dfl860eSysTCPUsage_ObjectIdentity = ObjectIdentity
dfl860eSysTCPUsage = _Dfl860eSysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 13)
)
_Dfl860eSysTCPRecvSmall_Type = Gauge32
_Dfl860eSysTCPRecvSmall_Object = MibScalar
dfl860eSysTCPRecvSmall = _Dfl860eSysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 13, 1),
    _Dfl860eSysTCPRecvSmall_Type()
)
dfl860eSysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysTCPRecvSmall.setStatus("current")
_Dfl860eSysTCPRecvLarge_Type = Gauge32
_Dfl860eSysTCPRecvLarge_Object = MibScalar
dfl860eSysTCPRecvLarge = _Dfl860eSysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 13, 2),
    _Dfl860eSysTCPRecvLarge_Type()
)
dfl860eSysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysTCPRecvLarge.setStatus("current")
_Dfl860eSysTCPSendSmall_Type = Gauge32
_Dfl860eSysTCPSendSmall_Object = MibScalar
dfl860eSysTCPSendSmall = _Dfl860eSysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 13, 3),
    _Dfl860eSysTCPSendSmall_Type()
)
dfl860eSysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysTCPSendSmall.setStatus("current")
_Dfl860eSysTCPSendLarge_Type = Gauge32
_Dfl860eSysTCPSendLarge_Object = MibScalar
dfl860eSysTCPSendLarge = _Dfl860eSysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 13, 4),
    _Dfl860eSysTCPSendLarge_Type()
)
dfl860eSysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysTCPSendLarge.setStatus("current")
_Dfl860eSysTimerUsage_Type = Gauge32
_Dfl860eSysTimerUsage_Object = MibScalar
dfl860eSysTimerUsage = _Dfl860eSysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 14),
    _Dfl860eSysTimerUsage_Type()
)
dfl860eSysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysTimerUsage.setStatus("current")
_Dfl860eSysConnOPS_Type = Gauge32
_Dfl860eSysConnOPS_Object = MibScalar
dfl860eSysConnOPS = _Dfl860eSysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 15),
    _Dfl860eSysConnOPS_Type()
)
dfl860eSysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysConnOPS.setStatus("current")
_Dfl860eSysConnCPS_Type = Gauge32
_Dfl860eSysConnCPS_Object = MibScalar
dfl860eSysConnCPS = _Dfl860eSysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 16),
    _Dfl860eSysConnCPS_Type()
)
dfl860eSysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysConnCPS.setStatus("current")
_Dfl860eSysHCForwardedBits_Type = Counter64
_Dfl860eSysHCForwardedBits_Object = MibScalar
dfl860eSysHCForwardedBits = _Dfl860eSysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 1, 17),
    _Dfl860eSysHCForwardedBits_Type()
)
dfl860eSysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSysHCForwardedBits.setStatus("current")
_Dfl860eVPN_ObjectIdentity = ObjectIdentity
dfl860eVPN = _Dfl860eVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2)
)
_Dfl860eIPsec_ObjectIdentity = ObjectIdentity
dfl860eIPsec = _Dfl860eIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1)
)
_Dfl860eIPsecGlobal_ObjectIdentity = ObjectIdentity
dfl860eIPsecGlobal = _Dfl860eIPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1)
)
_Dfl860eIPsecPhaseOneActive_Type = Gauge32
_Dfl860eIPsecPhaseOneActive_Object = MibScalar
dfl860eIPsecPhaseOneActive = _Dfl860eIPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 1),
    _Dfl860eIPsecPhaseOneActive_Type()
)
dfl860eIPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecPhaseOneActive.setStatus("current")
_Dfl860eIPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl860eIPsecPhaseOneAggrModeDone_Object = MibScalar
dfl860eIPsecPhaseOneAggrModeDone = _Dfl860eIPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 2),
    _Dfl860eIPsecPhaseOneAggrModeDone_Type()
)
dfl860eIPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl860eIPsecQuickModeActive_Type = Gauge32
_Dfl860eIPsecQuickModeActive_Object = MibScalar
dfl860eIPsecQuickModeActive = _Dfl860eIPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 3),
    _Dfl860eIPsecQuickModeActive_Type()
)
dfl860eIPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecQuickModeActive.setStatus("current")
_Dfl860eIPsecPhaseOneDone_Type = Counter32
_Dfl860eIPsecPhaseOneDone_Object = MibScalar
dfl860eIPsecPhaseOneDone = _Dfl860eIPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 4),
    _Dfl860eIPsecPhaseOneDone_Type()
)
dfl860eIPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecPhaseOneDone.setStatus("current")
_Dfl860eIPsecPhaseOneFailed_Type = Counter32
_Dfl860eIPsecPhaseOneFailed_Object = MibScalar
dfl860eIPsecPhaseOneFailed = _Dfl860eIPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 5),
    _Dfl860eIPsecPhaseOneFailed_Type()
)
dfl860eIPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecPhaseOneFailed.setStatus("current")
_Dfl860eIPsecPhaseOneRekeyed_Type = Counter32
_Dfl860eIPsecPhaseOneRekeyed_Object = MibScalar
dfl860eIPsecPhaseOneRekeyed = _Dfl860eIPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 6),
    _Dfl860eIPsecPhaseOneRekeyed_Type()
)
dfl860eIPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecPhaseOneRekeyed.setStatus("current")
_Dfl860eIPsecQuickModeDone_Type = Counter32
_Dfl860eIPsecQuickModeDone_Object = MibScalar
dfl860eIPsecQuickModeDone = _Dfl860eIPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 7),
    _Dfl860eIPsecQuickModeDone_Type()
)
dfl860eIPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecQuickModeDone.setStatus("current")
_Dfl860eIPsecQuickModeFailed_Type = Counter32
_Dfl860eIPsecQuickModeFailed_Object = MibScalar
dfl860eIPsecQuickModeFailed = _Dfl860eIPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 8),
    _Dfl860eIPsecQuickModeFailed_Type()
)
dfl860eIPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecQuickModeFailed.setStatus("current")
_Dfl860eIPsecInfoDone_Type = Counter32
_Dfl860eIPsecInfoDone_Object = MibScalar
dfl860eIPsecInfoDone = _Dfl860eIPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 9),
    _Dfl860eIPsecInfoDone_Type()
)
dfl860eIPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecInfoDone.setStatus("current")
_Dfl860eIPsecInfoFailed_Type = Counter32
_Dfl860eIPsecInfoFailed_Object = MibScalar
dfl860eIPsecInfoFailed = _Dfl860eIPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 10),
    _Dfl860eIPsecInfoFailed_Type()
)
dfl860eIPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecInfoFailed.setStatus("current")
_Dfl860eIPsecInOctetsComp_Type = Counter64
_Dfl860eIPsecInOctetsComp_Object = MibScalar
dfl860eIPsecInOctetsComp = _Dfl860eIPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 11),
    _Dfl860eIPsecInOctetsComp_Type()
)
dfl860eIPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecInOctetsComp.setStatus("current")
_Dfl860eIPsecInOctetsUncomp_Type = Counter64
_Dfl860eIPsecInOctetsUncomp_Object = MibScalar
dfl860eIPsecInOctetsUncomp = _Dfl860eIPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 12),
    _Dfl860eIPsecInOctetsUncomp_Type()
)
dfl860eIPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecInOctetsUncomp.setStatus("current")
_Dfl860eIPsecOutOctetsComp_Type = Counter64
_Dfl860eIPsecOutOctetsComp_Object = MibScalar
dfl860eIPsecOutOctetsComp = _Dfl860eIPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 13),
    _Dfl860eIPsecOutOctetsComp_Type()
)
dfl860eIPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecOutOctetsComp.setStatus("current")
_Dfl860eIPsecOutOctetsUncomp_Type = Counter64
_Dfl860eIPsecOutOctetsUncomp_Object = MibScalar
dfl860eIPsecOutOctetsUncomp = _Dfl860eIPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 14),
    _Dfl860eIPsecOutOctetsUncomp_Type()
)
dfl860eIPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecOutOctetsUncomp.setStatus("current")
_Dfl860eIPsecForwardedOctetsComp_Type = Counter64
_Dfl860eIPsecForwardedOctetsComp_Object = MibScalar
dfl860eIPsecForwardedOctetsComp = _Dfl860eIPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 15),
    _Dfl860eIPsecForwardedOctetsComp_Type()
)
dfl860eIPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecForwardedOctetsComp.setStatus("current")
_Dfl860eIPsecForwardedOctetsUcomp_Type = Counter64
_Dfl860eIPsecForwardedOctetsUcomp_Object = MibScalar
dfl860eIPsecForwardedOctetsUcomp = _Dfl860eIPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 16),
    _Dfl860eIPsecForwardedOctetsUcomp_Type()
)
dfl860eIPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecForwardedOctetsUcomp.setStatus("current")
_Dfl860eIPsecInPackets_Type = Counter64
_Dfl860eIPsecInPackets_Object = MibScalar
dfl860eIPsecInPackets = _Dfl860eIPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 17),
    _Dfl860eIPsecInPackets_Type()
)
dfl860eIPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecInPackets.setStatus("current")
_Dfl860eIPsecOutPackets_Type = Counter64
_Dfl860eIPsecOutPackets_Object = MibScalar
dfl860eIPsecOutPackets = _Dfl860eIPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 18),
    _Dfl860eIPsecOutPackets_Type()
)
dfl860eIPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecOutPackets.setStatus("current")
_Dfl860eIPsecForwardedPackets_Type = Counter64
_Dfl860eIPsecForwardedPackets_Object = MibScalar
dfl860eIPsecForwardedPackets = _Dfl860eIPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 19),
    _Dfl860eIPsecForwardedPackets_Type()
)
dfl860eIPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecForwardedPackets.setStatus("current")
_Dfl860eIPsecActiveTransforms_Type = Gauge32
_Dfl860eIPsecActiveTransforms_Object = MibScalar
dfl860eIPsecActiveTransforms = _Dfl860eIPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 20),
    _Dfl860eIPsecActiveTransforms_Type()
)
dfl860eIPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecActiveTransforms.setStatus("current")
_Dfl860eIPsecTotalTransforms_Type = Counter32
_Dfl860eIPsecTotalTransforms_Object = MibScalar
dfl860eIPsecTotalTransforms = _Dfl860eIPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 21),
    _Dfl860eIPsecTotalTransforms_Type()
)
dfl860eIPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecTotalTransforms.setStatus("current")
_Dfl860eIPsecOutOfTransforms_Type = Counter32
_Dfl860eIPsecOutOfTransforms_Object = MibScalar
dfl860eIPsecOutOfTransforms = _Dfl860eIPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 22),
    _Dfl860eIPsecOutOfTransforms_Type()
)
dfl860eIPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecOutOfTransforms.setStatus("current")
_Dfl860eIPsecTotalRekeys_Type = Counter32
_Dfl860eIPsecTotalRekeys_Object = MibScalar
dfl860eIPsecTotalRekeys = _Dfl860eIPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 2, 1, 1, 23),
    _Dfl860eIPsecTotalRekeys_Type()
)
dfl860eIPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPsecTotalRekeys.setStatus("current")
_Dfl860eRules_ObjectIdentity = ObjectIdentity
dfl860eRules = _Dfl860eRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 3)
)
_Dfl860eRuleUseTable_Object = MibTable
dfl860eRuleUseTable = _Dfl860eRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl860eRuleUseTable.setStatus("current")
_Dfl860eRuleUseEntry_Object = MibTableRow
dfl860eRuleUseEntry = _Dfl860eRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 3, 2, 1)
)
dfl860eRuleUseEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860eRuleUseEntry.setStatus("current")


class _Dfl860eRuleIndex_Type(Integer32):
    """Custom type dfl860eRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eRuleIndex_Type.__name__ = "Integer32"
_Dfl860eRuleIndex_Object = MibTableColumn
dfl860eRuleIndex = _Dfl860eRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 3, 2, 1, 1),
    _Dfl860eRuleIndex_Type()
)
dfl860eRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eRuleIndex.setStatus("current")
_Dfl860eRuleName_Type = DisplayString
_Dfl860eRuleName_Object = MibTableColumn
dfl860eRuleName = _Dfl860eRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 3, 2, 1, 2),
    _Dfl860eRuleName_Type()
)
dfl860eRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eRuleName.setStatus("current")
_Dfl860eRuleUse_Type = Counter32
_Dfl860eRuleUse_Object = MibTableColumn
dfl860eRuleUse = _Dfl860eRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 3, 2, 1, 3),
    _Dfl860eRuleUse_Type()
)
dfl860eRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eRuleUse.setStatus("current")
_Dfl860eIPPools_ObjectIdentity = ObjectIdentity
dfl860eIPPools = _Dfl860eIPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4)
)
_Dfl860eIPPoolsNumber_Type = Integer32
_Dfl860eIPPoolsNumber_Object = MibScalar
dfl860eIPPoolsNumber = _Dfl860eIPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 1),
    _Dfl860eIPPoolsNumber_Type()
)
dfl860eIPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolsNumber.setStatus("current")
_Dfl860eIPPoolTable_Object = MibTable
dfl860eIPPoolTable = _Dfl860eIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl860eIPPoolTable.setStatus("current")
_Dfl860eIPPoolEntry_Object = MibTableRow
dfl860eIPPoolEntry = _Dfl860eIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1)
)
dfl860eIPPoolEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eIPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl860eIPPoolEntry.setStatus("current")


class _Dfl860eIPPoolIndex_Type(Integer32):
    """Custom type dfl860eIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eIPPoolIndex_Type.__name__ = "Integer32"
_Dfl860eIPPoolIndex_Object = MibTableColumn
dfl860eIPPoolIndex = _Dfl860eIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 1),
    _Dfl860eIPPoolIndex_Type()
)
dfl860eIPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eIPPoolIndex.setStatus("current")
_Dfl860eIPPoolName_Type = DisplayString
_Dfl860eIPPoolName_Object = MibTableColumn
dfl860eIPPoolName = _Dfl860eIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 2),
    _Dfl860eIPPoolName_Type()
)
dfl860eIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolName.setStatus("current")
_Dfl860eIPPoolPrepare_Type = Gauge32
_Dfl860eIPPoolPrepare_Object = MibTableColumn
dfl860eIPPoolPrepare = _Dfl860eIPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 3),
    _Dfl860eIPPoolPrepare_Type()
)
dfl860eIPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolPrepare.setStatus("current")
_Dfl860eIPPoolFree_Type = Gauge32
_Dfl860eIPPoolFree_Object = MibTableColumn
dfl860eIPPoolFree = _Dfl860eIPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 4),
    _Dfl860eIPPoolFree_Type()
)
dfl860eIPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolFree.setStatus("current")
_Dfl860eIPPoolMisses_Type = Gauge32
_Dfl860eIPPoolMisses_Object = MibTableColumn
dfl860eIPPoolMisses = _Dfl860eIPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 5),
    _Dfl860eIPPoolMisses_Type()
)
dfl860eIPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolMisses.setStatus("current")
_Dfl860eIPPoolClientFails_Type = Gauge32
_Dfl860eIPPoolClientFails_Object = MibTableColumn
dfl860eIPPoolClientFails = _Dfl860eIPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 6),
    _Dfl860eIPPoolClientFails_Type()
)
dfl860eIPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolClientFails.setStatus("current")
_Dfl860eIPPoolUsed_Type = Gauge32
_Dfl860eIPPoolUsed_Object = MibTableColumn
dfl860eIPPoolUsed = _Dfl860eIPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 4, 2, 1, 7),
    _Dfl860eIPPoolUsed_Type()
)
dfl860eIPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eIPPoolUsed.setStatus("current")
_Dfl860eDHCPServer_ObjectIdentity = ObjectIdentity
dfl860eDHCPServer = _Dfl860eDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5)
)
_Dfl860eDHCPTotalRejected_Type = Gauge32
_Dfl860eDHCPTotalRejected_Object = MibScalar
dfl860eDHCPTotalRejected = _Dfl860eDHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 1),
    _Dfl860eDHCPTotalRejected_Type()
)
dfl860eDHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPTotalRejected.setStatus("current")
_Dfl860eDHCPRuleTable_Object = MibTable
dfl860eDHCPRuleTable = _Dfl860eDHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl860eDHCPRuleTable.setStatus("current")
_Dfl860eDHCPRuleEntry_Object = MibTableRow
dfl860eDHCPRuleEntry = _Dfl860eDHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1)
)
dfl860eDHCPRuleEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eDHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860eDHCPRuleEntry.setStatus("current")


class _Dfl860eDHCPRuleIndex_Type(Integer32):
    """Custom type dfl860eDHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eDHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl860eDHCPRuleIndex_Object = MibTableColumn
dfl860eDHCPRuleIndex = _Dfl860eDHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 1),
    _Dfl860eDHCPRuleIndex_Type()
)
dfl860eDHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eDHCPRuleIndex.setStatus("current")
_Dfl860eDHCPRuleName_Type = DisplayString
_Dfl860eDHCPRuleName_Object = MibTableColumn
dfl860eDHCPRuleName = _Dfl860eDHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 2),
    _Dfl860eDHCPRuleName_Type()
)
dfl860eDHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRuleName.setStatus("current")
_Dfl860eDHCPRuleUsage_Type = Gauge32
_Dfl860eDHCPRuleUsage_Object = MibTableColumn
dfl860eDHCPRuleUsage = _Dfl860eDHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 3),
    _Dfl860eDHCPRuleUsage_Type()
)
dfl860eDHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRuleUsage.setStatus("current")
_Dfl860eDHCPRuleUsagePercent_Type = Gauge32
_Dfl860eDHCPRuleUsagePercent_Object = MibTableColumn
dfl860eDHCPRuleUsagePercent = _Dfl860eDHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 4),
    _Dfl860eDHCPRuleUsagePercent_Type()
)
dfl860eDHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRuleUsagePercent.setStatus("current")
_Dfl860eDHCPActiveClients_Type = Gauge32
_Dfl860eDHCPActiveClients_Object = MibTableColumn
dfl860eDHCPActiveClients = _Dfl860eDHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 5),
    _Dfl860eDHCPActiveClients_Type()
)
dfl860eDHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPActiveClients.setStatus("current")
_Dfl860eDHCPActiveClientsPercent_Type = Gauge32
_Dfl860eDHCPActiveClientsPercent_Object = MibTableColumn
dfl860eDHCPActiveClientsPercent = _Dfl860eDHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 6),
    _Dfl860eDHCPActiveClientsPercent_Type()
)
dfl860eDHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPActiveClientsPercent.setStatus("current")
_Dfl860eDHCPRejectedRequests_Type = Gauge32
_Dfl860eDHCPRejectedRequests_Object = MibTableColumn
dfl860eDHCPRejectedRequests = _Dfl860eDHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 7),
    _Dfl860eDHCPRejectedRequests_Type()
)
dfl860eDHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRejectedRequests.setStatus("current")
_Dfl860eDHCPTotalLeases_Type = Gauge32
_Dfl860eDHCPTotalLeases_Object = MibTableColumn
dfl860eDHCPTotalLeases = _Dfl860eDHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 5, 2, 1, 8),
    _Dfl860eDHCPTotalLeases_Type()
)
dfl860eDHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPTotalLeases.setStatus("current")
_Dfl860eUserAuth_ObjectIdentity = ObjectIdentity
dfl860eUserAuth = _Dfl860eUserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6)
)
_Dfl860eUserAuthHTTPUsers_Type = Gauge32
_Dfl860eUserAuthHTTPUsers_Object = MibScalar
dfl860eUserAuthHTTPUsers = _Dfl860eUserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 1),
    _Dfl860eUserAuthHTTPUsers_Type()
)
dfl860eUserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthHTTPUsers.setStatus("current")
_Dfl860eUserAuthXAUTHUsers_Type = Gauge32
_Dfl860eUserAuthXAUTHUsers_Object = MibScalar
dfl860eUserAuthXAUTHUsers = _Dfl860eUserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 2),
    _Dfl860eUserAuthXAUTHUsers_Type()
)
dfl860eUserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthXAUTHUsers.setStatus("current")
_Dfl860eUserAuthHTTPSUsers_Type = Gauge32
_Dfl860eUserAuthHTTPSUsers_Object = MibScalar
dfl860eUserAuthHTTPSUsers = _Dfl860eUserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 3),
    _Dfl860eUserAuthHTTPSUsers_Type()
)
dfl860eUserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthHTTPSUsers.setStatus("current")
_Dfl860eUserAuthPPPUsers_Type = Gauge32
_Dfl860eUserAuthPPPUsers_Object = MibScalar
dfl860eUserAuthPPPUsers = _Dfl860eUserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 4),
    _Dfl860eUserAuthPPPUsers_Type()
)
dfl860eUserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthPPPUsers.setStatus("current")
_Dfl860eUserAuthEAPUsers_Type = Gauge32
_Dfl860eUserAuthEAPUsers_Object = MibScalar
dfl860eUserAuthEAPUsers = _Dfl860eUserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 5),
    _Dfl860eUserAuthEAPUsers_Type()
)
dfl860eUserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthEAPUsers.setStatus("current")
_Dfl860eUserAuthRuleUseTable_Object = MibTable
dfl860eUserAuthRuleUseTable = _Dfl860eUserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl860eUserAuthRuleUseTable.setStatus("current")
_Dfl860eUserAuthRuleUseEntry_Object = MibTableRow
dfl860eUserAuthRuleUseEntry = _Dfl860eUserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 6, 1)
)
dfl860eUserAuthRuleUseEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eUserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860eUserAuthRuleUseEntry.setStatus("current")


class _Dfl860eUserAuthRuleIndex_Type(Integer32):
    """Custom type dfl860eUserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eUserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl860eUserAuthRuleIndex_Object = MibTableColumn
dfl860eUserAuthRuleIndex = _Dfl860eUserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 6, 1, 1),
    _Dfl860eUserAuthRuleIndex_Type()
)
dfl860eUserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eUserAuthRuleIndex.setStatus("current")
_Dfl860eUserAuthRuleName_Type = DisplayString
_Dfl860eUserAuthRuleName_Object = MibTableColumn
dfl860eUserAuthRuleName = _Dfl860eUserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 6, 1, 2),
    _Dfl860eUserAuthRuleName_Type()
)
dfl860eUserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthRuleName.setStatus("current")
_Dfl860eUserAuthRuleUse_Type = Counter32
_Dfl860eUserAuthRuleUse_Object = MibTableColumn
dfl860eUserAuthRuleUse = _Dfl860eUserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 6, 6, 1, 3),
    _Dfl860eUserAuthRuleUse_Type()
)
dfl860eUserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eUserAuthRuleUse.setStatus("current")
_Dfl860eLinkMonitor_ObjectIdentity = ObjectIdentity
dfl860eLinkMonitor = _Dfl860eLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7)
)
_Dfl860eLinkMonGrp_Type = Integer32
_Dfl860eLinkMonGrp_Object = MibScalar
dfl860eLinkMonGrp = _Dfl860eLinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 1),
    _Dfl860eLinkMonGrp_Type()
)
dfl860eLinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eLinkMonGrp.setStatus("current")
_Dfl860eLinkMonGrpTable_Object = MibTable
dfl860eLinkMonGrpTable = _Dfl860eLinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl860eLinkMonGrpTable.setStatus("current")
_Dfl860eLinkMonGrpEntry_Object = MibTableRow
dfl860eLinkMonGrpEntry = _Dfl860eLinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 2, 1)
)
dfl860eLinkMonGrpEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eLinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl860eLinkMonGrpEntry.setStatus("current")


class _Dfl860eLinkMonGrpIndex_Type(Integer32):
    """Custom type dfl860eLinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eLinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl860eLinkMonGrpIndex_Object = MibTableColumn
dfl860eLinkMonGrpIndex = _Dfl860eLinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 2, 1, 1),
    _Dfl860eLinkMonGrpIndex_Type()
)
dfl860eLinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eLinkMonGrpIndex.setStatus("current")
_Dfl860eLinkMonGrpName_Type = DisplayString
_Dfl860eLinkMonGrpName_Object = MibTableColumn
dfl860eLinkMonGrpName = _Dfl860eLinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 2, 1, 2),
    _Dfl860eLinkMonGrpName_Type()
)
dfl860eLinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eLinkMonGrpName.setStatus("current")
_Dfl860eLinkMonGrpHostsUp_Type = Gauge32
_Dfl860eLinkMonGrpHostsUp_Object = MibTableColumn
dfl860eLinkMonGrpHostsUp = _Dfl860eLinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 2, 1, 3),
    _Dfl860eLinkMonGrpHostsUp_Type()
)
dfl860eLinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eLinkMonGrpHostsUp.setStatus("current")
_Dfl860eLinkMonHostTable_Object = MibTable
dfl860eLinkMonHostTable = _Dfl860eLinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl860eLinkMonHostTable.setStatus("current")
_Dfl860eLinkMonHostEntry_Object = MibTableRow
dfl860eLinkMonHostEntry = _Dfl860eLinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 3, 1)
)
dfl860eLinkMonHostEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eLinkMonGrpIndex"),
    (0, "DFL860e-MIB", "dfl860eLinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl860eLinkMonHostEntry.setStatus("current")


class _Dfl860eLinkMonHostIndex_Type(Integer32):
    """Custom type dfl860eLinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eLinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl860eLinkMonHostIndex_Object = MibTableColumn
dfl860eLinkMonHostIndex = _Dfl860eLinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 3, 1, 1),
    _Dfl860eLinkMonHostIndex_Type()
)
dfl860eLinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eLinkMonHostIndex.setStatus("current")
_Dfl860eLinkMonHostId_Type = DisplayString
_Dfl860eLinkMonHostId_Object = MibTableColumn
dfl860eLinkMonHostId = _Dfl860eLinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 3, 1, 2),
    _Dfl860eLinkMonHostId_Type()
)
dfl860eLinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eLinkMonHostId.setStatus("current")
_Dfl860eLinkMonHostShortTermLoss_Type = Gauge32
_Dfl860eLinkMonHostShortTermLoss_Object = MibTableColumn
dfl860eLinkMonHostShortTermLoss = _Dfl860eLinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 3, 1, 3),
    _Dfl860eLinkMonHostShortTermLoss_Type()
)
dfl860eLinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eLinkMonHostShortTermLoss.setStatus("current")
_Dfl860eLinkMonHostPacketsLost_Type = Counter32
_Dfl860eLinkMonHostPacketsLost_Object = MibTableColumn
dfl860eLinkMonHostPacketsLost = _Dfl860eLinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 7, 3, 1, 4),
    _Dfl860eLinkMonHostPacketsLost_Type()
)
dfl860eLinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eLinkMonHostPacketsLost.setStatus("current")
_Dfl860ePipes_ObjectIdentity = ObjectIdentity
dfl860ePipes = _Dfl860ePipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8)
)
_Dfl860ePipeUsers_Type = Gauge32
_Dfl860ePipeUsers_Object = MibScalar
dfl860ePipeUsers = _Dfl860ePipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 1),
    _Dfl860ePipeUsers_Type()
)
dfl860ePipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeUsers.setStatus("current")
_Dfl860ePipeTable_Object = MibTable
dfl860ePipeTable = _Dfl860ePipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl860ePipeTable.setStatus("current")
_Dfl860ePipeEntry_Object = MibTableRow
dfl860ePipeEntry = _Dfl860ePipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1)
)
dfl860ePipeEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860ePipeIndex"),
)
if mibBuilder.loadTexts:
    dfl860ePipeEntry.setStatus("current")


class _Dfl860ePipeIndex_Type(Integer32):
    """Custom type dfl860ePipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860ePipeIndex_Type.__name__ = "Integer32"
_Dfl860ePipeIndex_Object = MibTableColumn
dfl860ePipeIndex = _Dfl860ePipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 1),
    _Dfl860ePipeIndex_Type()
)
dfl860ePipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860ePipeIndex.setStatus("current")
_Dfl860ePipeName_Type = DisplayString
_Dfl860ePipeName_Object = MibTableColumn
dfl860ePipeName = _Dfl860ePipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 2),
    _Dfl860ePipeName_Type()
)
dfl860ePipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeName.setStatus("current")
_Dfl860ePipeMinPrec_Type = Integer32
_Dfl860ePipeMinPrec_Object = MibTableColumn
dfl860ePipeMinPrec = _Dfl860ePipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 3),
    _Dfl860ePipeMinPrec_Type()
)
dfl860ePipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeMinPrec.setStatus("current")
_Dfl860ePipeMaxPrec_Type = Integer32
_Dfl860ePipeMaxPrec_Object = MibTableColumn
dfl860ePipeMaxPrec = _Dfl860ePipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 4),
    _Dfl860ePipeMaxPrec_Type()
)
dfl860ePipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeMaxPrec.setStatus("current")
_Dfl860ePipeDefPrec_Type = Integer32
_Dfl860ePipeDefPrec_Object = MibTableColumn
dfl860ePipeDefPrec = _Dfl860ePipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 5),
    _Dfl860ePipeDefPrec_Type()
)
dfl860ePipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeDefPrec.setStatus("current")
_Dfl860ePipeNumPrec_Type = Integer32
_Dfl860ePipeNumPrec_Object = MibTableColumn
dfl860ePipeNumPrec = _Dfl860ePipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 6),
    _Dfl860ePipeNumPrec_Type()
)
dfl860ePipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeNumPrec.setStatus("current")
_Dfl860ePipeNumUsers_Type = Gauge32
_Dfl860ePipeNumUsers_Object = MibTableColumn
dfl860ePipeNumUsers = _Dfl860ePipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 7),
    _Dfl860ePipeNumUsers_Type()
)
dfl860ePipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeNumUsers.setStatus("current")
_Dfl860ePipeCurrentBps_Type = Gauge32
_Dfl860ePipeCurrentBps_Object = MibTableColumn
dfl860ePipeCurrentBps = _Dfl860ePipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 8),
    _Dfl860ePipeCurrentBps_Type()
)
dfl860ePipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeCurrentBps.setStatus("current")
_Dfl860ePipeCurrentPps_Type = Gauge32
_Dfl860ePipeCurrentPps_Object = MibTableColumn
dfl860ePipeCurrentPps = _Dfl860ePipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 9),
    _Dfl860ePipeCurrentPps_Type()
)
dfl860ePipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeCurrentPps.setStatus("current")
_Dfl860ePipeDelayedPackets_Type = Counter32
_Dfl860ePipeDelayedPackets_Object = MibTableColumn
dfl860ePipeDelayedPackets = _Dfl860ePipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 10),
    _Dfl860ePipeDelayedPackets_Type()
)
dfl860ePipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeDelayedPackets.setStatus("current")
_Dfl860ePipeDropedPackets_Type = Counter32
_Dfl860ePipeDropedPackets_Object = MibTableColumn
dfl860ePipeDropedPackets = _Dfl860ePipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 2, 1, 11),
    _Dfl860ePipeDropedPackets_Type()
)
dfl860ePipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipeDropedPackets.setStatus("current")
_Dfl860ePipePrecTable_Object = MibTable
dfl860ePipePrecTable = _Dfl860ePipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl860ePipePrecTable.setStatus("current")
_Dfl860ePipePrecEntry_Object = MibTableRow
dfl860ePipePrecEntry = _Dfl860ePipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1)
)
dfl860ePipePrecEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860ePipeIndex"),
    (0, "DFL860e-MIB", "dfl860ePipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl860ePipePrecEntry.setStatus("current")


class _Dfl860ePipePrecIndex_Type(Integer32):
    """Custom type dfl860ePipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860ePipePrecIndex_Type.__name__ = "Integer32"
_Dfl860ePipePrecIndex_Object = MibTableColumn
dfl860ePipePrecIndex = _Dfl860ePipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 1),
    _Dfl860ePipePrecIndex_Type()
)
dfl860ePipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860ePipePrecIndex.setStatus("current")
_Dfl860ePipePrec_Type = Integer32
_Dfl860ePipePrec_Object = MibTableColumn
dfl860ePipePrec = _Dfl860ePipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 2),
    _Dfl860ePipePrec_Type()
)
dfl860ePipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrec.setStatus("current")
_Dfl860ePipePrecBps_Type = Gauge32
_Dfl860ePipePrecBps_Object = MibTableColumn
dfl860ePipePrecBps = _Dfl860ePipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 3),
    _Dfl860ePipePrecBps_Type()
)
dfl860ePipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecBps.setStatus("current")
_Dfl860ePipePrecTotalPps_Type = Gauge32
_Dfl860ePipePrecTotalPps_Object = MibTableColumn
dfl860ePipePrecTotalPps = _Dfl860ePipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 4),
    _Dfl860ePipePrecTotalPps_Type()
)
dfl860ePipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecTotalPps.setStatus("current")
_Dfl860ePipePrecReservedBps_Type = Gauge32
_Dfl860ePipePrecReservedBps_Object = MibTableColumn
dfl860ePipePrecReservedBps = _Dfl860ePipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 5),
    _Dfl860ePipePrecReservedBps_Type()
)
dfl860ePipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecReservedBps.setStatus("current")
_Dfl860ePipePrecDynLimBps_Type = Gauge32
_Dfl860ePipePrecDynLimBps_Object = MibTableColumn
dfl860ePipePrecDynLimBps = _Dfl860ePipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 6),
    _Dfl860ePipePrecDynLimBps_Type()
)
dfl860ePipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecDynLimBps.setStatus("current")
_Dfl860ePipePrecDynUsrLimBps_Type = Gauge32
_Dfl860ePipePrecDynUsrLimBps_Object = MibTableColumn
dfl860ePipePrecDynUsrLimBps = _Dfl860ePipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 7),
    _Dfl860ePipePrecDynUsrLimBps_Type()
)
dfl860ePipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecDynUsrLimBps.setStatus("current")
_Dfl860ePipePrecDelayedPackets_Type = Counter32
_Dfl860ePipePrecDelayedPackets_Object = MibTableColumn
dfl860ePipePrecDelayedPackets = _Dfl860ePipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 8),
    _Dfl860ePipePrecDelayedPackets_Type()
)
dfl860ePipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecDelayedPackets.setStatus("current")
_Dfl860ePipePrecDropedPackets_Type = Counter32
_Dfl860ePipePrecDropedPackets_Object = MibTableColumn
dfl860ePipePrecDropedPackets = _Dfl860ePipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 8, 3, 1, 9),
    _Dfl860ePipePrecDropedPackets_Type()
)
dfl860ePipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860ePipePrecDropedPackets.setStatus("current")
_Dfl860eALG_ObjectIdentity = ObjectIdentity
dfl860eALG = _Dfl860eALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9)
)
_Dfl860eAlgSessions_Type = Gauge32
_Dfl860eAlgSessions_Object = MibScalar
dfl860eAlgSessions = _Dfl860eAlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 1),
    _Dfl860eAlgSessions_Type()
)
dfl860eAlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eAlgSessions.setStatus("current")
_Dfl860eAlgConnections_Type = Gauge32
_Dfl860eAlgConnections_Object = MibScalar
dfl860eAlgConnections = _Dfl860eAlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 2),
    _Dfl860eAlgConnections_Type()
)
dfl860eAlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eAlgConnections.setStatus("current")
_Dfl860eAlgTCPStreams_Type = Gauge32
_Dfl860eAlgTCPStreams_Object = MibScalar
dfl860eAlgTCPStreams = _Dfl860eAlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 3),
    _Dfl860eAlgTCPStreams_Type()
)
dfl860eAlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eAlgTCPStreams.setStatus("current")
_Dfl860eHttpAlg_ObjectIdentity = ObjectIdentity
dfl860eHttpAlg = _Dfl860eHttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4)
)
_Dfl860eHttpAlgTable_Object = MibTable
dfl860eHttpAlgTable = _Dfl860eHttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl860eHttpAlgTable.setStatus("current")
_Dfl860eHttpAlgEntry_Object = MibTableRow
dfl860eHttpAlgEntry = _Dfl860eHttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1, 1)
)
dfl860eHttpAlgEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eHttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl860eHttpAlgEntry.setStatus("current")


class _Dfl860eHttpAlgIndex_Type(Integer32):
    """Custom type dfl860eHttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eHttpAlgIndex_Type.__name__ = "Integer32"
_Dfl860eHttpAlgIndex_Object = MibTableColumn
dfl860eHttpAlgIndex = _Dfl860eHttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1, 1, 1),
    _Dfl860eHttpAlgIndex_Type()
)
dfl860eHttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eHttpAlgIndex.setStatus("current")
_Dfl860eHttpAlgName_Type = DisplayString
_Dfl860eHttpAlgName_Object = MibTableColumn
dfl860eHttpAlgName = _Dfl860eHttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1, 1, 2),
    _Dfl860eHttpAlgName_Type()
)
dfl860eHttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgName.setStatus("current")
_Dfl860eHttpAlgTotalRequested_Type = Gauge32
_Dfl860eHttpAlgTotalRequested_Object = MibTableColumn
dfl860eHttpAlgTotalRequested = _Dfl860eHttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1, 1, 3),
    _Dfl860eHttpAlgTotalRequested_Type()
)
dfl860eHttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgTotalRequested.setStatus("current")
_Dfl860eHttpAlgTotalAllowed_Type = Gauge32
_Dfl860eHttpAlgTotalAllowed_Object = MibTableColumn
dfl860eHttpAlgTotalAllowed = _Dfl860eHttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1, 1, 4),
    _Dfl860eHttpAlgTotalAllowed_Type()
)
dfl860eHttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgTotalAllowed.setStatus("current")
_Dfl860eHttpAlgTotalBlocked_Type = Gauge32
_Dfl860eHttpAlgTotalBlocked_Object = MibTableColumn
dfl860eHttpAlgTotalBlocked = _Dfl860eHttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 1, 1, 5),
    _Dfl860eHttpAlgTotalBlocked_Type()
)
dfl860eHttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgTotalBlocked.setStatus("current")
_Dfl860eHttpAlgCntFltTable_Object = MibTable
dfl860eHttpAlgCntFltTable = _Dfl860eHttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltTable.setStatus("current")
_Dfl860eHttpAlgCntFltEntry_Object = MibTableRow
dfl860eHttpAlgCntFltEntry = _Dfl860eHttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2, 1)
)
dfl860eHttpAlgCntFltEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eHttpAlgIndex"),
    (0, "DFL860e-MIB", "dfl860eHttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltEntry.setStatus("current")


class _Dfl860eHttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl860eHttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eHttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl860eHttpAlgCntFltIndex_Object = MibTableColumn
dfl860eHttpAlgCntFltIndex = _Dfl860eHttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2, 1, 1),
    _Dfl860eHttpAlgCntFltIndex_Type()
)
dfl860eHttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltIndex.setStatus("current")
_Dfl860eHttpAlgCntFltName_Type = DisplayString
_Dfl860eHttpAlgCntFltName_Object = MibTableColumn
dfl860eHttpAlgCntFltName = _Dfl860eHttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2, 1, 2),
    _Dfl860eHttpAlgCntFltName_Type()
)
dfl860eHttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltName.setStatus("current")
_Dfl860eHttpAlgCntFltRequests_Type = Gauge32
_Dfl860eHttpAlgCntFltRequests_Object = MibTableColumn
dfl860eHttpAlgCntFltRequests = _Dfl860eHttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2, 1, 3),
    _Dfl860eHttpAlgCntFltRequests_Type()
)
dfl860eHttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltRequests.setStatus("current")
_Dfl860eHttpAlgCntFltAllowed_Type = Gauge32
_Dfl860eHttpAlgCntFltAllowed_Object = MibTableColumn
dfl860eHttpAlgCntFltAllowed = _Dfl860eHttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2, 1, 4),
    _Dfl860eHttpAlgCntFltAllowed_Type()
)
dfl860eHttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltAllowed.setStatus("current")
_Dfl860eHttpAlgCntFltBlocked_Type = Gauge32
_Dfl860eHttpAlgCntFltBlocked_Object = MibTableColumn
dfl860eHttpAlgCntFltBlocked = _Dfl860eHttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 4, 2, 1, 5),
    _Dfl860eHttpAlgCntFltBlocked_Type()
)
dfl860eHttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHttpAlgCntFltBlocked.setStatus("current")
_Dfl860eSmtpAlg_ObjectIdentity = ObjectIdentity
dfl860eSmtpAlg = _Dfl860eSmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5)
)
_Dfl860eSmtpAlgTable_Object = MibTable
dfl860eSmtpAlgTable = _Dfl860eSmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl860eSmtpAlgTable.setStatus("current")
_Dfl860eSmtpAlgEntry_Object = MibTableRow
dfl860eSmtpAlgEntry = _Dfl860eSmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1, 1)
)
dfl860eSmtpAlgEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eSmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl860eSmtpAlgEntry.setStatus("current")


class _Dfl860eSmtpAlgIndex_Type(Integer32):
    """Custom type dfl860eSmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eSmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl860eSmtpAlgIndex_Object = MibTableColumn
dfl860eSmtpAlgIndex = _Dfl860eSmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1, 1, 1),
    _Dfl860eSmtpAlgIndex_Type()
)
dfl860eSmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgIndex.setStatus("current")
_Dfl860eSmtpAlgName_Type = DisplayString
_Dfl860eSmtpAlgName_Object = MibTableColumn
dfl860eSmtpAlgName = _Dfl860eSmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1, 1, 2),
    _Dfl860eSmtpAlgName_Type()
)
dfl860eSmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgName.setStatus("current")
_Dfl860eSmtpAlgTotCheckedSes_Type = Gauge32
_Dfl860eSmtpAlgTotCheckedSes_Object = MibTableColumn
dfl860eSmtpAlgTotCheckedSes = _Dfl860eSmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1, 1, 3),
    _Dfl860eSmtpAlgTotCheckedSes_Type()
)
dfl860eSmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgTotCheckedSes.setStatus("current")
_Dfl860eSmtpAlgTotSpamSes_Type = Gauge32
_Dfl860eSmtpAlgTotSpamSes_Object = MibTableColumn
dfl860eSmtpAlgTotSpamSes = _Dfl860eSmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1, 1, 4),
    _Dfl860eSmtpAlgTotSpamSes_Type()
)
dfl860eSmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgTotSpamSes.setStatus("current")
_Dfl860eSmtpAlgTotDroppedSes_Type = Gauge32
_Dfl860eSmtpAlgTotDroppedSes_Object = MibTableColumn
dfl860eSmtpAlgTotDroppedSes = _Dfl860eSmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 1, 1, 5),
    _Dfl860eSmtpAlgTotDroppedSes_Type()
)
dfl860eSmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgTotDroppedSes.setStatus("current")
_Dfl860eSmtpAlgDnsBlTable_Object = MibTable
dfl860eSmtpAlgDnsBlTable = _Dfl860eSmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlTable.setStatus("current")
_Dfl860eSmtpAlgDnsBlEntry_Object = MibTableRow
dfl860eSmtpAlgDnsBlEntry = _Dfl860eSmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2, 1)
)
dfl860eSmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eSmtpAlgIndex"),
    (0, "DFL860e-MIB", "dfl860eSmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlEntry.setStatus("current")


class _Dfl860eSmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl860eSmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eSmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl860eSmtpAlgDnsBlIndex_Object = MibTableColumn
dfl860eSmtpAlgDnsBlIndex = _Dfl860eSmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2, 1, 1),
    _Dfl860eSmtpAlgDnsBlIndex_Type()
)
dfl860eSmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlIndex.setStatus("current")
_Dfl860eSmtpAlgDnsBlName_Type = DisplayString
_Dfl860eSmtpAlgDnsBlName_Object = MibTableColumn
dfl860eSmtpAlgDnsBlName = _Dfl860eSmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2, 1, 2),
    _Dfl860eSmtpAlgDnsBlName_Type()
)
dfl860eSmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlName.setStatus("current")
_Dfl860eSmtpAlgDnsBlChecked_Type = Gauge32
_Dfl860eSmtpAlgDnsBlChecked_Object = MibTableColumn
dfl860eSmtpAlgDnsBlChecked = _Dfl860eSmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2, 1, 3),
    _Dfl860eSmtpAlgDnsBlChecked_Type()
)
dfl860eSmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlChecked.setStatus("current")
_Dfl860eSmtpAlgDnsBlMatched_Type = Gauge32
_Dfl860eSmtpAlgDnsBlMatched_Object = MibTableColumn
dfl860eSmtpAlgDnsBlMatched = _Dfl860eSmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2, 1, 4),
    _Dfl860eSmtpAlgDnsBlMatched_Type()
)
dfl860eSmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlMatched.setStatus("current")
_Dfl860eSmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl860eSmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl860eSmtpAlgDnsBlFailChecks = _Dfl860eSmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 9, 5, 2, 1, 5),
    _Dfl860eSmtpAlgDnsBlFailChecks_Type()
)
dfl860eSmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eSmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl860eDHCPRelay_ObjectIdentity = ObjectIdentity
dfl860eDHCPRelay = _Dfl860eDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11)
)
_Dfl860eDHCPRelayCurClients_Type = Gauge32
_Dfl860eDHCPRelayCurClients_Object = MibScalar
dfl860eDHCPRelayCurClients = _Dfl860eDHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 1),
    _Dfl860eDHCPRelayCurClients_Type()
)
dfl860eDHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayCurClients.setStatus("current")
_Dfl860eDHCPRelayCurTrans_Type = Gauge32
_Dfl860eDHCPRelayCurTrans_Object = MibScalar
dfl860eDHCPRelayCurTrans = _Dfl860eDHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 2),
    _Dfl860eDHCPRelayCurTrans_Type()
)
dfl860eDHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayCurTrans.setStatus("current")
_Dfl860eDHCPRelayRejected_Type = Gauge32
_Dfl860eDHCPRelayRejected_Object = MibScalar
dfl860eDHCPRelayRejected = _Dfl860eDHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 3),
    _Dfl860eDHCPRelayRejected_Type()
)
dfl860eDHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRejected.setStatus("current")
_Dfl860eDHCPRelayRuleTable_Object = MibTable
dfl860eDHCPRelayRuleTable = _Dfl860eDHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleTable.setStatus("current")
_Dfl860eDHCPRelayRuleEntry_Object = MibTableRow
dfl860eDHCPRelayRuleEntry = _Dfl860eDHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1)
)
dfl860eDHCPRelayRuleEntry.setIndexNames(
    (0, "DFL860e-MIB", "dfl860eDHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleEntry.setStatus("current")


class _Dfl860eDHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl860eDHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl860eDHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl860eDHCPRelayRuleIndex_Object = MibTableColumn
dfl860eDHCPRelayRuleIndex = _Dfl860eDHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1, 1),
    _Dfl860eDHCPRelayRuleIndex_Type()
)
dfl860eDHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleIndex.setStatus("current")
_Dfl860eDHCPRelayRuleName_Type = DisplayString
_Dfl860eDHCPRelayRuleName_Object = MibTableColumn
dfl860eDHCPRelayRuleName = _Dfl860eDHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1, 2),
    _Dfl860eDHCPRelayRuleName_Type()
)
dfl860eDHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleName.setStatus("current")
_Dfl860eDHCPRelayRuleHits_Type = Gauge32
_Dfl860eDHCPRelayRuleHits_Object = MibTableColumn
dfl860eDHCPRelayRuleHits = _Dfl860eDHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1, 3),
    _Dfl860eDHCPRelayRuleHits_Type()
)
dfl860eDHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleHits.setStatus("current")
_Dfl860eDHCPRelayRuleCurClients_Type = Gauge32
_Dfl860eDHCPRelayRuleCurClients_Object = MibTableColumn
dfl860eDHCPRelayRuleCurClients = _Dfl860eDHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1, 4),
    _Dfl860eDHCPRelayRuleCurClients_Type()
)
dfl860eDHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleCurClients.setStatus("current")
_Dfl860eDHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl860eDHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl860eDHCPRelayRuleRejCliPkts = _Dfl860eDHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1, 5),
    _Dfl860eDHCPRelayRuleRejCliPkts_Type()
)
dfl860eDHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl860eDHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl860eDHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl860eDHCPRelayRuleRejSrvPkts = _Dfl860eDHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 11, 4, 1, 6),
    _Dfl860eDHCPRelayRuleRejSrvPkts_Type()
)
dfl860eDHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eDHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl860eHA_ObjectIdentity = ObjectIdentity
dfl860eHA = _Dfl860eHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 12)
)
_Dfl860eHASyncSendQueueLength_Type = Gauge32
_Dfl860eHASyncSendQueueLength_Object = MibScalar
dfl860eHASyncSendQueueLength = _Dfl860eHASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 12, 1),
    _Dfl860eHASyncSendQueueLength_Type()
)
dfl860eHASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHASyncSendQueueLength.setStatus("current")
_Dfl860eHASyncSendQueueUsagePkt_Type = Gauge32
_Dfl860eHASyncSendQueueUsagePkt_Object = MibScalar
dfl860eHASyncSendQueueUsagePkt = _Dfl860eHASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 12, 2),
    _Dfl860eHASyncSendQueueUsagePkt_Type()
)
dfl860eHASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHASyncSendQueueUsagePkt.setStatus("current")
_Dfl860eHASyncSendQueueUsageOct_Type = Gauge32
_Dfl860eHASyncSendQueueUsageOct_Object = MibScalar
dfl860eHASyncSendQueueUsageOct = _Dfl860eHASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 12, 3),
    _Dfl860eHASyncSendQueueUsageOct_Type()
)
dfl860eHASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHASyncSendQueueUsageOct.setStatus("current")
_Dfl860eHASyncSentPackets_Type = Counter32
_Dfl860eHASyncSentPackets_Object = MibScalar
dfl860eHASyncSentPackets = _Dfl860eHASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 12, 4),
    _Dfl860eHASyncSentPackets_Type()
)
dfl860eHASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHASyncSentPackets.setStatus("current")
_Dfl860eHASyncSendResentPackets_Type = Counter32
_Dfl860eHASyncSendResentPackets_Object = MibScalar
dfl860eHASyncSendResentPackets = _Dfl860eHASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 1, 2, 12, 5),
    _Dfl860eHASyncSendResentPackets_Type()
)
dfl860eHASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl860eHASyncSendResentPackets.setStatus("current")
_Dfl860ereg_ObjectIdentity = ObjectIdentity
dfl860ereg = _Dfl860ereg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2)
)
_Dfl860eMibModules_ObjectIdentity = ObjectIdentity
dfl860eMibModules = _Dfl860eMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 1)
)
_Dfl860eMibConfs_ObjectIdentity = ObjectIdentity
dfl860eMibConfs = _Dfl860eMibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 2)
)
_Dfl860eStatsConformance_ObjectIdentity = ObjectIdentity
dfl860eStatsConformance = _Dfl860eStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 2, 1)
)
_Dfl860eMibObjectGroups_ObjectIdentity = ObjectIdentity
dfl860eMibObjectGroups = _Dfl860eMibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3)
)
_Dfl860eStatsRegGroups_ObjectIdentity = ObjectIdentity
dfl860eStatsRegGroups = _Dfl860eStatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1)
)

# Managed Objects groups

dfl860eSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 1)
)
dfl860eSystemObjectGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eSysCpuLoad"),
        ("DFL860e-MIB", "dfl860eSysForwardedBits"),
        ("DFL860e-MIB", "dfl860eSysForwardedPackets"),
        ("DFL860e-MIB", "dfl860eSysBuffUse"),
        ("DFL860e-MIB", "dfl860eSysConns"),
        ("DFL860e-MIB", "dfl860eHWSensorName"),
        ("DFL860e-MIB", "dfl860eHWSensorValue"),
        ("DFL860e-MIB", "dfl860eHWSensorUnit"),
        ("DFL860e-MIB", "dfl860eSysMemUsage"),
        ("DFL860e-MIB", "dfl860eSysTimerUsage"),
        ("DFL860e-MIB", "dfl860eSysConnOPS"),
        ("DFL860e-MIB", "dfl860eSysConnCPS"),
        ("DFL860e-MIB", "dfl860eSysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl860eSystemObjectGroup.setStatus("current")

dfl860eIPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 2)
)
dfl860eIPsecObjectGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eIPsecPhaseOneActive"),
        ("DFL860e-MIB", "dfl860eIPsecPhaseOneAggrModeDone"),
        ("DFL860e-MIB", "dfl860eIPsecQuickModeActive"),
        ("DFL860e-MIB", "dfl860eIPsecPhaseOneDone"),
        ("DFL860e-MIB", "dfl860eIPsecPhaseOneFailed"),
        ("DFL860e-MIB", "dfl860eIPsecPhaseOneRekeyed"),
        ("DFL860e-MIB", "dfl860eIPsecQuickModeDone"),
        ("DFL860e-MIB", "dfl860eIPsecQuickModeFailed"),
        ("DFL860e-MIB", "dfl860eIPsecInfoDone"),
        ("DFL860e-MIB", "dfl860eIPsecInfoFailed"),
        ("DFL860e-MIB", "dfl860eIPsecInOctetsComp"),
        ("DFL860e-MIB", "dfl860eIPsecInOctetsUncomp"),
        ("DFL860e-MIB", "dfl860eIPsecOutOctetsComp"),
        ("DFL860e-MIB", "dfl860eIPsecOutOctetsUncomp"),
        ("DFL860e-MIB", "dfl860eIPsecForwardedOctetsComp"),
        ("DFL860e-MIB", "dfl860eIPsecForwardedOctetsUcomp"),
        ("DFL860e-MIB", "dfl860eIPsecInPackets"),
        ("DFL860e-MIB", "dfl860eIPsecOutPackets"),
        ("DFL860e-MIB", "dfl860eIPsecForwardedPackets"),
        ("DFL860e-MIB", "dfl860eIPsecActiveTransforms"),
        ("DFL860e-MIB", "dfl860eIPsecTotalTransforms"),
        ("DFL860e-MIB", "dfl860eIPsecOutOfTransforms"),
        ("DFL860e-MIB", "dfl860eIPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl860eIPsecObjectGroup.setStatus("current")

dfl860eStateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 3)
)
dfl860eStateCountersGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eSysPscTcpSyn"),
        ("DFL860e-MIB", "dfl860eSysPscTcpOpen"),
        ("DFL860e-MIB", "dfl860eSysPscTcpFin"),
        ("DFL860e-MIB", "dfl860eSysPscUdp"),
        ("DFL860e-MIB", "dfl860eSysPscIcmp"),
        ("DFL860e-MIB", "dfl860eSysPscOther"))
)
if mibBuilder.loadTexts:
    dfl860eStateCountersGroup.setStatus("current")

dfl860eIPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 4)
)
dfl860eIPPoolGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eIPPoolsNumber"),
        ("DFL860e-MIB", "dfl860eIPPoolName"),
        ("DFL860e-MIB", "dfl860eIPPoolPrepare"),
        ("DFL860e-MIB", "dfl860eIPPoolFree"),
        ("DFL860e-MIB", "dfl860eIPPoolMisses"),
        ("DFL860e-MIB", "dfl860eIPPoolClientFails"),
        ("DFL860e-MIB", "dfl860eIPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl860eIPPoolGroup.setStatus("current")

dfl860eDHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 5)
)
dfl860eDHCPServerGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eDHCPTotalRejected"),
        ("DFL860e-MIB", "dfl860eDHCPRuleName"),
        ("DFL860e-MIB", "dfl860eDHCPRuleUsage"),
        ("DFL860e-MIB", "dfl860eDHCPRuleUsagePercent"),
        ("DFL860e-MIB", "dfl860eDHCPActiveClients"),
        ("DFL860e-MIB", "dfl860eDHCPActiveClientsPercent"),
        ("DFL860e-MIB", "dfl860eDHCPRejectedRequests"),
        ("DFL860e-MIB", "dfl860eDHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl860eDHCPServerGroup.setStatus("current")

dfl860eRuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 6)
)
dfl860eRuleUseGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eRuleName"),
        ("DFL860e-MIB", "dfl860eRuleUse"))
)
if mibBuilder.loadTexts:
    dfl860eRuleUseGroup.setStatus("current")

dfl860eUserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 7)
)
dfl860eUserAuthGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eUserAuthHTTPUsers"),
        ("DFL860e-MIB", "dfl860eUserAuthXAUTHUsers"),
        ("DFL860e-MIB", "dfl860eUserAuthHTTPSUsers"),
        ("DFL860e-MIB", "dfl860eUserAuthPPPUsers"),
        ("DFL860e-MIB", "dfl860eUserAuthEAPUsers"),
        ("DFL860e-MIB", "dfl860eUserAuthRuleName"),
        ("DFL860e-MIB", "dfl860eUserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl860eUserAuthGroup.setStatus("current")

dfl860eIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 8)
)
dfl860eIfStatsGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eIfName"),
        ("DFL860e-MIB", "dfl860eIfFragsIn"),
        ("DFL860e-MIB", "dfl860eIfFragReassOk"),
        ("DFL860e-MIB", "dfl860eIfFragReassFail"),
        ("DFL860e-MIB", "dfl860eIfPktsInCnt"),
        ("DFL860e-MIB", "dfl860eIfPktsOutCnt"),
        ("DFL860e-MIB", "dfl860eIfBitsInCnt"),
        ("DFL860e-MIB", "dfl860eIfBitsOutCnt"),
        ("DFL860e-MIB", "dfl860eIfPktsTotCnt"),
        ("DFL860e-MIB", "dfl860eIfBitsTotCnt"),
        ("DFL860e-MIB", "dfl860eIfHCPktsInCnt"),
        ("DFL860e-MIB", "dfl860eIfHCPktsOutCnt"),
        ("DFL860e-MIB", "dfl860eIfHCBitsInCnt"),
        ("DFL860e-MIB", "dfl860eIfHCBitsOutCnt"),
        ("DFL860e-MIB", "dfl860eIfHCPktsTotCnt"),
        ("DFL860e-MIB", "dfl860eIfHCBitsTotCnt"),
        ("DFL860e-MIB", "dfl860eIfRxRingFifoErrors"),
        ("DFL860e-MIB", "dfl860eIfRxDespools"),
        ("DFL860e-MIB", "dfl860eIfRxAvgUse"),
        ("DFL860e-MIB", "dfl860eIfRxRingSaturation"),
        ("DFL860e-MIB", "dfl860eRxRingFlooded"),
        ("DFL860e-MIB", "dfl860eIfTxDespools"),
        ("DFL860e-MIB", "dfl860eIfTxAvgUse"),
        ("DFL860e-MIB", "dfl860eIfTxRingSaturation"),
        ("DFL860e-MIB", "dfl860eRxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl860eIfStatsGroup.setStatus("current")

dfl860eLinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 9)
)
dfl860eLinkMonitorGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eLinkMonGrp"),
        ("DFL860e-MIB", "dfl860eLinkMonGrpName"),
        ("DFL860e-MIB", "dfl860eLinkMonGrpHostsUp"),
        ("DFL860e-MIB", "dfl860eLinkMonHostId"),
        ("DFL860e-MIB", "dfl860eLinkMonHostShortTermLoss"),
        ("DFL860e-MIB", "dfl860eLinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl860eLinkMonitorGroup.setStatus("current")

dfl860ePipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 10)
)
dfl860ePipesObjectGroup.setObjects(
      *(("DFL860e-MIB", "dfl860ePipeUsers"),
        ("DFL860e-MIB", "dfl860ePipeName"),
        ("DFL860e-MIB", "dfl860ePipeMinPrec"),
        ("DFL860e-MIB", "dfl860ePipeMaxPrec"),
        ("DFL860e-MIB", "dfl860ePipeDefPrec"),
        ("DFL860e-MIB", "dfl860ePipeNumPrec"),
        ("DFL860e-MIB", "dfl860ePipeNumUsers"),
        ("DFL860e-MIB", "dfl860ePipeCurrentBps"),
        ("DFL860e-MIB", "dfl860ePipeCurrentPps"),
        ("DFL860e-MIB", "dfl860ePipeDelayedPackets"),
        ("DFL860e-MIB", "dfl860ePipeDropedPackets"),
        ("DFL860e-MIB", "dfl860ePipePrec"),
        ("DFL860e-MIB", "dfl860ePipePrecBps"),
        ("DFL860e-MIB", "dfl860ePipePrecTotalPps"),
        ("DFL860e-MIB", "dfl860ePipePrecReservedBps"),
        ("DFL860e-MIB", "dfl860ePipePrecDynLimBps"),
        ("DFL860e-MIB", "dfl860ePipePrecDynUsrLimBps"),
        ("DFL860e-MIB", "dfl860ePipePrecDelayedPackets"),
        ("DFL860e-MIB", "dfl860ePipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl860ePipesObjectGroup.setStatus("current")

dfl860eDHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 12)
)
dfl860eDHCPRelayObjectGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eDHCPRelayCurClients"),
        ("DFL860e-MIB", "dfl860eDHCPRelayCurTrans"),
        ("DFL860e-MIB", "dfl860eDHCPRelayRejected"),
        ("DFL860e-MIB", "dfl860eDHCPRelayRuleName"),
        ("DFL860e-MIB", "dfl860eDHCPRelayRuleHits"),
        ("DFL860e-MIB", "dfl860eDHCPRelayRuleCurClients"),
        ("DFL860e-MIB", "dfl860eDHCPRelayRuleRejCliPkts"),
        ("DFL860e-MIB", "dfl860eDHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl860eDHCPRelayObjectGroup.setStatus("current")

dfl860eAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 13)
)
dfl860eAlgGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eAlgSessions"),
        ("DFL860e-MIB", "dfl860eAlgConnections"),
        ("DFL860e-MIB", "dfl860eAlgTCPStreams"),
        ("DFL860e-MIB", "dfl860eHttpAlgName"),
        ("DFL860e-MIB", "dfl860eHttpAlgTotalRequested"),
        ("DFL860e-MIB", "dfl860eHttpAlgTotalAllowed"),
        ("DFL860e-MIB", "dfl860eHttpAlgTotalBlocked"),
        ("DFL860e-MIB", "dfl860eHttpAlgCntFltName"),
        ("DFL860e-MIB", "dfl860eHttpAlgCntFltRequests"),
        ("DFL860e-MIB", "dfl860eHttpAlgCntFltAllowed"),
        ("DFL860e-MIB", "dfl860eHttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl860eAlgGroup.setStatus("current")

dfl860eHAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 14)
)
dfl860eHAGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eHASyncSendQueueLength"),
        ("DFL860e-MIB", "dfl860eHASyncSendQueueUsagePkt"),
        ("DFL860e-MIB", "dfl860eHASyncSendQueueUsageOct"),
        ("DFL860e-MIB", "dfl860eHASyncSentPackets"),
        ("DFL860e-MIB", "dfl860eHASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl860eHAGroup.setStatus("current")

dfl860eIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 15)
)
dfl860eIfVlanGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eIfVlanUntaggedInPkts"),
        ("DFL860e-MIB", "dfl860eIfVlanUntaggedOutPkts"),
        ("DFL860e-MIB", "dfl860eIfVlanUntaggedTotPkts"),
        ("DFL860e-MIB", "dfl860eIfVlanUntaggedInOctets"),
        ("DFL860e-MIB", "dfl860eIfVlanUntaggedOutOctets"),
        ("DFL860e-MIB", "dfl860eIfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl860eIfVlanGroup.setStatus("current")

dfl860eSmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 16)
)
dfl860eSmtpAlgGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eSmtpAlgName"),
        ("DFL860e-MIB", "dfl860eSmtpAlgTotCheckedSes"),
        ("DFL860e-MIB", "dfl860eSmtpAlgTotSpamSes"),
        ("DFL860e-MIB", "dfl860eSmtpAlgTotDroppedSes"),
        ("DFL860e-MIB", "dfl860eSmtpAlgDnsBlName"),
        ("DFL860e-MIB", "dfl860eSmtpAlgDnsBlChecked"),
        ("DFL860e-MIB", "dfl860eSmtpAlgDnsBlMatched"),
        ("DFL860e-MIB", "dfl860eSmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl860eSmtpAlgGroup.setStatus("current")

dfl860eSysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 3, 1, 17)
)
dfl860eSysTCPGroup.setObjects(
      *(("DFL860e-MIB", "dfl860eSysTCPRecvSmall"),
        ("DFL860e-MIB", "dfl860eSysTCPRecvLarge"),
        ("DFL860e-MIB", "dfl860eSysTCPSendSmall"),
        ("DFL860e-MIB", "dfl860eSysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl860eSysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl860eStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 7, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl860eStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL860e-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "utmFirewall": utmFirewall,
       "dfl860e": dfl860e,
       "dfl860eOS": dfl860eOS,
       "dfl860eOSStats": dfl860eOSStats,
       "dfl860eSystem": dfl860eSystem,
       "dfl860eSysCpuLoad": dfl860eSysCpuLoad,
       "dfl860eSysForwardedBits": dfl860eSysForwardedBits,
       "dfl860eSysForwardedPackets": dfl860eSysForwardedPackets,
       "dfl860eSysBuffUse": dfl860eSysBuffUse,
       "dfl860eSysConns": dfl860eSysConns,
       "dfl860eSysPerStateCounters": dfl860eSysPerStateCounters,
       "dfl860eSysPscTcpSyn": dfl860eSysPscTcpSyn,
       "dfl860eSysPscTcpOpen": dfl860eSysPscTcpOpen,
       "dfl860eSysPscTcpFin": dfl860eSysPscTcpFin,
       "dfl860eSysPscUdp": dfl860eSysPscUdp,
       "dfl860eSysPscIcmp": dfl860eSysPscIcmp,
       "dfl860eSysPscOther": dfl860eSysPscOther,
       "dfl860eIfStatsTable": dfl860eIfStatsTable,
       "dfl860eIfStatsEntry": dfl860eIfStatsEntry,
       "dfl860eIfStatsIndex": dfl860eIfStatsIndex,
       "dfl860eIfName": dfl860eIfName,
       "dfl860eIfFragsIn": dfl860eIfFragsIn,
       "dfl860eIfFragReassOk": dfl860eIfFragReassOk,
       "dfl860eIfFragReassFail": dfl860eIfFragReassFail,
       "dfl860eIfPktsInCnt": dfl860eIfPktsInCnt,
       "dfl860eIfPktsOutCnt": dfl860eIfPktsOutCnt,
       "dfl860eIfBitsInCnt": dfl860eIfBitsInCnt,
       "dfl860eIfBitsOutCnt": dfl860eIfBitsOutCnt,
       "dfl860eIfPktsTotCnt": dfl860eIfPktsTotCnt,
       "dfl860eIfBitsTotCnt": dfl860eIfBitsTotCnt,
       "dfl860eIfHCPktsInCnt": dfl860eIfHCPktsInCnt,
       "dfl860eIfHCPktsOutCnt": dfl860eIfHCPktsOutCnt,
       "dfl860eIfHCBitsInCnt": dfl860eIfHCBitsInCnt,
       "dfl860eIfHCBitsOutCnt": dfl860eIfHCBitsOutCnt,
       "dfl860eIfHCPktsTotCnt": dfl860eIfHCPktsTotCnt,
       "dfl860eIfHCBitsTotCnt": dfl860eIfHCBitsTotCnt,
       "dfl860eIfRxRingTable": dfl860eIfRxRingTable,
       "dfl860eIfRxRingEntry": dfl860eIfRxRingEntry,
       "dfl860eIfRxRingIndex": dfl860eIfRxRingIndex,
       "dfl860eIfRxRingFifoErrors": dfl860eIfRxRingFifoErrors,
       "dfl860eIfRxDespools": dfl860eIfRxDespools,
       "dfl860eIfRxAvgUse": dfl860eIfRxAvgUse,
       "dfl860eIfRxRingSaturation": dfl860eIfRxRingSaturation,
       "dfl860eRxRingFlooded": dfl860eRxRingFlooded,
       "dfl860eIfTxRingTable": dfl860eIfTxRingTable,
       "dfl860eIfTxRingEntry": dfl860eIfTxRingEntry,
       "dfl860eIfTxRingIndex": dfl860eIfTxRingIndex,
       "dfl860eIfTxDespools": dfl860eIfTxDespools,
       "dfl860eIfTxAvgUse": dfl860eIfTxAvgUse,
       "dfl860eIfTxRingSaturation": dfl860eIfTxRingSaturation,
       "dfl860eRxTingFlooded": dfl860eRxTingFlooded,
       "dfl860eIfVlanStatsTable": dfl860eIfVlanStatsTable,
       "dfl860eIfVlanStatsEntry": dfl860eIfVlanStatsEntry,
       "dfl860eIfVlanIndex": dfl860eIfVlanIndex,
       "dfl860eIfVlanUntaggedInPkts": dfl860eIfVlanUntaggedInPkts,
       "dfl860eIfVlanUntaggedOutPkts": dfl860eIfVlanUntaggedOutPkts,
       "dfl860eIfVlanUntaggedTotPkts": dfl860eIfVlanUntaggedTotPkts,
       "dfl860eIfVlanUntaggedInOctets": dfl860eIfVlanUntaggedInOctets,
       "dfl860eIfVlanUntaggedOutOctets": dfl860eIfVlanUntaggedOutOctets,
       "dfl860eIfVlanUntaggedTotOctets": dfl860eIfVlanUntaggedTotOctets,
       "dfl860eHWSensorTable": dfl860eHWSensorTable,
       "dfl860eHWSensorEntry": dfl860eHWSensorEntry,
       "dfl860eHWSensorIndex": dfl860eHWSensorIndex,
       "dfl860eHWSensorName": dfl860eHWSensorName,
       "dfl860eHWSensorValue": dfl860eHWSensorValue,
       "dfl860eHWSensorUnit": dfl860eHWSensorUnit,
       "dfl860eSysMemUsage": dfl860eSysMemUsage,
       "dfl860eSysTCPUsage": dfl860eSysTCPUsage,
       "dfl860eSysTCPRecvSmall": dfl860eSysTCPRecvSmall,
       "dfl860eSysTCPRecvLarge": dfl860eSysTCPRecvLarge,
       "dfl860eSysTCPSendSmall": dfl860eSysTCPSendSmall,
       "dfl860eSysTCPSendLarge": dfl860eSysTCPSendLarge,
       "dfl860eSysTimerUsage": dfl860eSysTimerUsage,
       "dfl860eSysConnOPS": dfl860eSysConnOPS,
       "dfl860eSysConnCPS": dfl860eSysConnCPS,
       "dfl860eSysHCForwardedBits": dfl860eSysHCForwardedBits,
       "dfl860eVPN": dfl860eVPN,
       "dfl860eIPsec": dfl860eIPsec,
       "dfl860eIPsecGlobal": dfl860eIPsecGlobal,
       "dfl860eIPsecPhaseOneActive": dfl860eIPsecPhaseOneActive,
       "dfl860eIPsecPhaseOneAggrModeDone": dfl860eIPsecPhaseOneAggrModeDone,
       "dfl860eIPsecQuickModeActive": dfl860eIPsecQuickModeActive,
       "dfl860eIPsecPhaseOneDone": dfl860eIPsecPhaseOneDone,
       "dfl860eIPsecPhaseOneFailed": dfl860eIPsecPhaseOneFailed,
       "dfl860eIPsecPhaseOneRekeyed": dfl860eIPsecPhaseOneRekeyed,
       "dfl860eIPsecQuickModeDone": dfl860eIPsecQuickModeDone,
       "dfl860eIPsecQuickModeFailed": dfl860eIPsecQuickModeFailed,
       "dfl860eIPsecInfoDone": dfl860eIPsecInfoDone,
       "dfl860eIPsecInfoFailed": dfl860eIPsecInfoFailed,
       "dfl860eIPsecInOctetsComp": dfl860eIPsecInOctetsComp,
       "dfl860eIPsecInOctetsUncomp": dfl860eIPsecInOctetsUncomp,
       "dfl860eIPsecOutOctetsComp": dfl860eIPsecOutOctetsComp,
       "dfl860eIPsecOutOctetsUncomp": dfl860eIPsecOutOctetsUncomp,
       "dfl860eIPsecForwardedOctetsComp": dfl860eIPsecForwardedOctetsComp,
       "dfl860eIPsecForwardedOctetsUcomp": dfl860eIPsecForwardedOctetsUcomp,
       "dfl860eIPsecInPackets": dfl860eIPsecInPackets,
       "dfl860eIPsecOutPackets": dfl860eIPsecOutPackets,
       "dfl860eIPsecForwardedPackets": dfl860eIPsecForwardedPackets,
       "dfl860eIPsecActiveTransforms": dfl860eIPsecActiveTransforms,
       "dfl860eIPsecTotalTransforms": dfl860eIPsecTotalTransforms,
       "dfl860eIPsecOutOfTransforms": dfl860eIPsecOutOfTransforms,
       "dfl860eIPsecTotalRekeys": dfl860eIPsecTotalRekeys,
       "dfl860eRules": dfl860eRules,
       "dfl860eRuleUseTable": dfl860eRuleUseTable,
       "dfl860eRuleUseEntry": dfl860eRuleUseEntry,
       "dfl860eRuleIndex": dfl860eRuleIndex,
       "dfl860eRuleName": dfl860eRuleName,
       "dfl860eRuleUse": dfl860eRuleUse,
       "dfl860eIPPools": dfl860eIPPools,
       "dfl860eIPPoolsNumber": dfl860eIPPoolsNumber,
       "dfl860eIPPoolTable": dfl860eIPPoolTable,
       "dfl860eIPPoolEntry": dfl860eIPPoolEntry,
       "dfl860eIPPoolIndex": dfl860eIPPoolIndex,
       "dfl860eIPPoolName": dfl860eIPPoolName,
       "dfl860eIPPoolPrepare": dfl860eIPPoolPrepare,
       "dfl860eIPPoolFree": dfl860eIPPoolFree,
       "dfl860eIPPoolMisses": dfl860eIPPoolMisses,
       "dfl860eIPPoolClientFails": dfl860eIPPoolClientFails,
       "dfl860eIPPoolUsed": dfl860eIPPoolUsed,
       "dfl860eDHCPServer": dfl860eDHCPServer,
       "dfl860eDHCPTotalRejected": dfl860eDHCPTotalRejected,
       "dfl860eDHCPRuleTable": dfl860eDHCPRuleTable,
       "dfl860eDHCPRuleEntry": dfl860eDHCPRuleEntry,
       "dfl860eDHCPRuleIndex": dfl860eDHCPRuleIndex,
       "dfl860eDHCPRuleName": dfl860eDHCPRuleName,
       "dfl860eDHCPRuleUsage": dfl860eDHCPRuleUsage,
       "dfl860eDHCPRuleUsagePercent": dfl860eDHCPRuleUsagePercent,
       "dfl860eDHCPActiveClients": dfl860eDHCPActiveClients,
       "dfl860eDHCPActiveClientsPercent": dfl860eDHCPActiveClientsPercent,
       "dfl860eDHCPRejectedRequests": dfl860eDHCPRejectedRequests,
       "dfl860eDHCPTotalLeases": dfl860eDHCPTotalLeases,
       "dfl860eUserAuth": dfl860eUserAuth,
       "dfl860eUserAuthHTTPUsers": dfl860eUserAuthHTTPUsers,
       "dfl860eUserAuthXAUTHUsers": dfl860eUserAuthXAUTHUsers,
       "dfl860eUserAuthHTTPSUsers": dfl860eUserAuthHTTPSUsers,
       "dfl860eUserAuthPPPUsers": dfl860eUserAuthPPPUsers,
       "dfl860eUserAuthEAPUsers": dfl860eUserAuthEAPUsers,
       "dfl860eUserAuthRuleUseTable": dfl860eUserAuthRuleUseTable,
       "dfl860eUserAuthRuleUseEntry": dfl860eUserAuthRuleUseEntry,
       "dfl860eUserAuthRuleIndex": dfl860eUserAuthRuleIndex,
       "dfl860eUserAuthRuleName": dfl860eUserAuthRuleName,
       "dfl860eUserAuthRuleUse": dfl860eUserAuthRuleUse,
       "dfl860eLinkMonitor": dfl860eLinkMonitor,
       "dfl860eLinkMonGrp": dfl860eLinkMonGrp,
       "dfl860eLinkMonGrpTable": dfl860eLinkMonGrpTable,
       "dfl860eLinkMonGrpEntry": dfl860eLinkMonGrpEntry,
       "dfl860eLinkMonGrpIndex": dfl860eLinkMonGrpIndex,
       "dfl860eLinkMonGrpName": dfl860eLinkMonGrpName,
       "dfl860eLinkMonGrpHostsUp": dfl860eLinkMonGrpHostsUp,
       "dfl860eLinkMonHostTable": dfl860eLinkMonHostTable,
       "dfl860eLinkMonHostEntry": dfl860eLinkMonHostEntry,
       "dfl860eLinkMonHostIndex": dfl860eLinkMonHostIndex,
       "dfl860eLinkMonHostId": dfl860eLinkMonHostId,
       "dfl860eLinkMonHostShortTermLoss": dfl860eLinkMonHostShortTermLoss,
       "dfl860eLinkMonHostPacketsLost": dfl860eLinkMonHostPacketsLost,
       "dfl860ePipes": dfl860ePipes,
       "dfl860ePipeUsers": dfl860ePipeUsers,
       "dfl860ePipeTable": dfl860ePipeTable,
       "dfl860ePipeEntry": dfl860ePipeEntry,
       "dfl860ePipeIndex": dfl860ePipeIndex,
       "dfl860ePipeName": dfl860ePipeName,
       "dfl860ePipeMinPrec": dfl860ePipeMinPrec,
       "dfl860ePipeMaxPrec": dfl860ePipeMaxPrec,
       "dfl860ePipeDefPrec": dfl860ePipeDefPrec,
       "dfl860ePipeNumPrec": dfl860ePipeNumPrec,
       "dfl860ePipeNumUsers": dfl860ePipeNumUsers,
       "dfl860ePipeCurrentBps": dfl860ePipeCurrentBps,
       "dfl860ePipeCurrentPps": dfl860ePipeCurrentPps,
       "dfl860ePipeDelayedPackets": dfl860ePipeDelayedPackets,
       "dfl860ePipeDropedPackets": dfl860ePipeDropedPackets,
       "dfl860ePipePrecTable": dfl860ePipePrecTable,
       "dfl860ePipePrecEntry": dfl860ePipePrecEntry,
       "dfl860ePipePrecIndex": dfl860ePipePrecIndex,
       "dfl860ePipePrec": dfl860ePipePrec,
       "dfl860ePipePrecBps": dfl860ePipePrecBps,
       "dfl860ePipePrecTotalPps": dfl860ePipePrecTotalPps,
       "dfl860ePipePrecReservedBps": dfl860ePipePrecReservedBps,
       "dfl860ePipePrecDynLimBps": dfl860ePipePrecDynLimBps,
       "dfl860ePipePrecDynUsrLimBps": dfl860ePipePrecDynUsrLimBps,
       "dfl860ePipePrecDelayedPackets": dfl860ePipePrecDelayedPackets,
       "dfl860ePipePrecDropedPackets": dfl860ePipePrecDropedPackets,
       "dfl860eALG": dfl860eALG,
       "dfl860eAlgSessions": dfl860eAlgSessions,
       "dfl860eAlgConnections": dfl860eAlgConnections,
       "dfl860eAlgTCPStreams": dfl860eAlgTCPStreams,
       "dfl860eHttpAlg": dfl860eHttpAlg,
       "dfl860eHttpAlgTable": dfl860eHttpAlgTable,
       "dfl860eHttpAlgEntry": dfl860eHttpAlgEntry,
       "dfl860eHttpAlgIndex": dfl860eHttpAlgIndex,
       "dfl860eHttpAlgName": dfl860eHttpAlgName,
       "dfl860eHttpAlgTotalRequested": dfl860eHttpAlgTotalRequested,
       "dfl860eHttpAlgTotalAllowed": dfl860eHttpAlgTotalAllowed,
       "dfl860eHttpAlgTotalBlocked": dfl860eHttpAlgTotalBlocked,
       "dfl860eHttpAlgCntFltTable": dfl860eHttpAlgCntFltTable,
       "dfl860eHttpAlgCntFltEntry": dfl860eHttpAlgCntFltEntry,
       "dfl860eHttpAlgCntFltIndex": dfl860eHttpAlgCntFltIndex,
       "dfl860eHttpAlgCntFltName": dfl860eHttpAlgCntFltName,
       "dfl860eHttpAlgCntFltRequests": dfl860eHttpAlgCntFltRequests,
       "dfl860eHttpAlgCntFltAllowed": dfl860eHttpAlgCntFltAllowed,
       "dfl860eHttpAlgCntFltBlocked": dfl860eHttpAlgCntFltBlocked,
       "dfl860eSmtpAlg": dfl860eSmtpAlg,
       "dfl860eSmtpAlgTable": dfl860eSmtpAlgTable,
       "dfl860eSmtpAlgEntry": dfl860eSmtpAlgEntry,
       "dfl860eSmtpAlgIndex": dfl860eSmtpAlgIndex,
       "dfl860eSmtpAlgName": dfl860eSmtpAlgName,
       "dfl860eSmtpAlgTotCheckedSes": dfl860eSmtpAlgTotCheckedSes,
       "dfl860eSmtpAlgTotSpamSes": dfl860eSmtpAlgTotSpamSes,
       "dfl860eSmtpAlgTotDroppedSes": dfl860eSmtpAlgTotDroppedSes,
       "dfl860eSmtpAlgDnsBlTable": dfl860eSmtpAlgDnsBlTable,
       "dfl860eSmtpAlgDnsBlEntry": dfl860eSmtpAlgDnsBlEntry,
       "dfl860eSmtpAlgDnsBlIndex": dfl860eSmtpAlgDnsBlIndex,
       "dfl860eSmtpAlgDnsBlName": dfl860eSmtpAlgDnsBlName,
       "dfl860eSmtpAlgDnsBlChecked": dfl860eSmtpAlgDnsBlChecked,
       "dfl860eSmtpAlgDnsBlMatched": dfl860eSmtpAlgDnsBlMatched,
       "dfl860eSmtpAlgDnsBlFailChecks": dfl860eSmtpAlgDnsBlFailChecks,
       "dfl860eDHCPRelay": dfl860eDHCPRelay,
       "dfl860eDHCPRelayCurClients": dfl860eDHCPRelayCurClients,
       "dfl860eDHCPRelayCurTrans": dfl860eDHCPRelayCurTrans,
       "dfl860eDHCPRelayRejected": dfl860eDHCPRelayRejected,
       "dfl860eDHCPRelayRuleTable": dfl860eDHCPRelayRuleTable,
       "dfl860eDHCPRelayRuleEntry": dfl860eDHCPRelayRuleEntry,
       "dfl860eDHCPRelayRuleIndex": dfl860eDHCPRelayRuleIndex,
       "dfl860eDHCPRelayRuleName": dfl860eDHCPRelayRuleName,
       "dfl860eDHCPRelayRuleHits": dfl860eDHCPRelayRuleHits,
       "dfl860eDHCPRelayRuleCurClients": dfl860eDHCPRelayRuleCurClients,
       "dfl860eDHCPRelayRuleRejCliPkts": dfl860eDHCPRelayRuleRejCliPkts,
       "dfl860eDHCPRelayRuleRejSrvPkts": dfl860eDHCPRelayRuleRejSrvPkts,
       "dfl860eHA": dfl860eHA,
       "dfl860eHASyncSendQueueLength": dfl860eHASyncSendQueueLength,
       "dfl860eHASyncSendQueueUsagePkt": dfl860eHASyncSendQueueUsagePkt,
       "dfl860eHASyncSendQueueUsageOct": dfl860eHASyncSendQueueUsageOct,
       "dfl860eHASyncSentPackets": dfl860eHASyncSentPackets,
       "dfl860eHASyncSendResentPackets": dfl860eHASyncSendResentPackets,
       "dfl860ereg": dfl860ereg,
       "dfl860eMibModules": dfl860eMibModules,
       "dfl860e-MIB": dfl860e_MIB,
       "dfl860eMibConfs": dfl860eMibConfs,
       "dfl860eStatsConformance": dfl860eStatsConformance,
       "dfl860eStatsCompliance": dfl860eStatsCompliance,
       "dfl860eMibObjectGroups": dfl860eMibObjectGroups,
       "dfl860eStatsRegGroups": dfl860eStatsRegGroups,
       "dfl860eSystemObjectGroup": dfl860eSystemObjectGroup,
       "dfl860eIPsecObjectGroup": dfl860eIPsecObjectGroup,
       "dfl860eStateCountersGroup": dfl860eStateCountersGroup,
       "dfl860eIPPoolGroup": dfl860eIPPoolGroup,
       "dfl860eDHCPServerGroup": dfl860eDHCPServerGroup,
       "dfl860eRuleUseGroup": dfl860eRuleUseGroup,
       "dfl860eUserAuthGroup": dfl860eUserAuthGroup,
       "dfl860eIfStatsGroup": dfl860eIfStatsGroup,
       "dfl860eLinkMonitorGroup": dfl860eLinkMonitorGroup,
       "dfl860ePipesObjectGroup": dfl860ePipesObjectGroup,
       "dfl860eDHCPRelayObjectGroup": dfl860eDHCPRelayObjectGroup,
       "dfl860eAlgGroup": dfl860eAlgGroup,
       "dfl860eHAGroup": dfl860eHAGroup,
       "dfl860eIfVlanGroup": dfl860eIfVlanGroup,
       "dfl860eSmtpAlgGroup": dfl860eSmtpAlgGroup,
       "dfl860eSysTCPGroup": dfl860eSysTCPGroup}
)
