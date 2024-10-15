# SNMP MIB module (DFL260e-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFL260e-MIB
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

dfl260e_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 1, 2)
)
dfl260e_MIB.setRevisions(
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
_Dfl260e_ObjectIdentity = ObjectIdentity
dfl260e = _Dfl260e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6)
)
_Dfl260eOS_ObjectIdentity = ObjectIdentity
dfl260eOS = _Dfl260eOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1)
)
_Dfl260eOSStats_ObjectIdentity = ObjectIdentity
dfl260eOSStats = _Dfl260eOSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2)
)
_Dfl260eSystem_ObjectIdentity = ObjectIdentity
dfl260eSystem = _Dfl260eSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1)
)
_Dfl260eSysCpuLoad_Type = Gauge32
_Dfl260eSysCpuLoad_Object = MibScalar
dfl260eSysCpuLoad = _Dfl260eSysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 1),
    _Dfl260eSysCpuLoad_Type()
)
dfl260eSysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysCpuLoad.setStatus("current")
_Dfl260eSysForwardedBits_Type = Counter32
_Dfl260eSysForwardedBits_Object = MibScalar
dfl260eSysForwardedBits = _Dfl260eSysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 2),
    _Dfl260eSysForwardedBits_Type()
)
dfl260eSysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysForwardedBits.setStatus("current")
_Dfl260eSysForwardedPackets_Type = Counter32
_Dfl260eSysForwardedPackets_Object = MibScalar
dfl260eSysForwardedPackets = _Dfl260eSysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 3),
    _Dfl260eSysForwardedPackets_Type()
)
dfl260eSysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysForwardedPackets.setStatus("current")
_Dfl260eSysBuffUse_Type = Gauge32
_Dfl260eSysBuffUse_Object = MibScalar
dfl260eSysBuffUse = _Dfl260eSysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 4),
    _Dfl260eSysBuffUse_Type()
)
dfl260eSysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysBuffUse.setStatus("current")
_Dfl260eSysConns_Type = Gauge32
_Dfl260eSysConns_Object = MibScalar
dfl260eSysConns = _Dfl260eSysConns_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 5),
    _Dfl260eSysConns_Type()
)
dfl260eSysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysConns.setStatus("current")
_Dfl260eSysPerStateCounters_ObjectIdentity = ObjectIdentity
dfl260eSysPerStateCounters = _Dfl260eSysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6)
)
_Dfl260eSysPscTcpSyn_Type = Gauge32
_Dfl260eSysPscTcpSyn_Object = MibScalar
dfl260eSysPscTcpSyn = _Dfl260eSysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6, 1),
    _Dfl260eSysPscTcpSyn_Type()
)
dfl260eSysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysPscTcpSyn.setStatus("current")
_Dfl260eSysPscTcpOpen_Type = Gauge32
_Dfl260eSysPscTcpOpen_Object = MibScalar
dfl260eSysPscTcpOpen = _Dfl260eSysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6, 2),
    _Dfl260eSysPscTcpOpen_Type()
)
dfl260eSysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysPscTcpOpen.setStatus("current")
_Dfl260eSysPscTcpFin_Type = Gauge32
_Dfl260eSysPscTcpFin_Object = MibScalar
dfl260eSysPscTcpFin = _Dfl260eSysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6, 3),
    _Dfl260eSysPscTcpFin_Type()
)
dfl260eSysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysPscTcpFin.setStatus("current")
_Dfl260eSysPscUdp_Type = Gauge32
_Dfl260eSysPscUdp_Object = MibScalar
dfl260eSysPscUdp = _Dfl260eSysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6, 4),
    _Dfl260eSysPscUdp_Type()
)
dfl260eSysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysPscUdp.setStatus("current")
_Dfl260eSysPscIcmp_Type = Gauge32
_Dfl260eSysPscIcmp_Object = MibScalar
dfl260eSysPscIcmp = _Dfl260eSysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6, 5),
    _Dfl260eSysPscIcmp_Type()
)
dfl260eSysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysPscIcmp.setStatus("current")
_Dfl260eSysPscOther_Type = Gauge32
_Dfl260eSysPscOther_Object = MibScalar
dfl260eSysPscOther = _Dfl260eSysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 6, 6),
    _Dfl260eSysPscOther_Type()
)
dfl260eSysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysPscOther.setStatus("current")
_Dfl260eIfStatsTable_Object = MibTable
dfl260eIfStatsTable = _Dfl260eIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    dfl260eIfStatsTable.setStatus("current")
_Dfl260eIfStatsEntry_Object = MibTableRow
dfl260eIfStatsEntry = _Dfl260eIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1)
)
dfl260eIfStatsEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eIfStatsIndex"),
)
if mibBuilder.loadTexts:
    dfl260eIfStatsEntry.setStatus("current")


class _Dfl260eIfStatsIndex_Type(Integer32):
    """Custom type dfl260eIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eIfStatsIndex_Type.__name__ = "Integer32"
_Dfl260eIfStatsIndex_Object = MibTableColumn
dfl260eIfStatsIndex = _Dfl260eIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 1),
    _Dfl260eIfStatsIndex_Type()
)
dfl260eIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eIfStatsIndex.setStatus("current")
_Dfl260eIfName_Type = DisplayString
_Dfl260eIfName_Object = MibTableColumn
dfl260eIfName = _Dfl260eIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 2),
    _Dfl260eIfName_Type()
)
dfl260eIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfName.setStatus("current")
_Dfl260eIfFragsIn_Type = Counter32
_Dfl260eIfFragsIn_Object = MibTableColumn
dfl260eIfFragsIn = _Dfl260eIfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 3),
    _Dfl260eIfFragsIn_Type()
)
dfl260eIfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfFragsIn.setStatus("current")
_Dfl260eIfFragReassOk_Type = Counter32
_Dfl260eIfFragReassOk_Object = MibTableColumn
dfl260eIfFragReassOk = _Dfl260eIfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 4),
    _Dfl260eIfFragReassOk_Type()
)
dfl260eIfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfFragReassOk.setStatus("current")
_Dfl260eIfFragReassFail_Type = Counter32
_Dfl260eIfFragReassFail_Object = MibTableColumn
dfl260eIfFragReassFail = _Dfl260eIfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 5),
    _Dfl260eIfFragReassFail_Type()
)
dfl260eIfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfFragReassFail.setStatus("current")
_Dfl260eIfPktsInCnt_Type = Counter32
_Dfl260eIfPktsInCnt_Object = MibTableColumn
dfl260eIfPktsInCnt = _Dfl260eIfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 6),
    _Dfl260eIfPktsInCnt_Type()
)
dfl260eIfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfPktsInCnt.setStatus("current")
_Dfl260eIfPktsOutCnt_Type = Counter32
_Dfl260eIfPktsOutCnt_Object = MibTableColumn
dfl260eIfPktsOutCnt = _Dfl260eIfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 7),
    _Dfl260eIfPktsOutCnt_Type()
)
dfl260eIfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfPktsOutCnt.setStatus("current")
_Dfl260eIfBitsInCnt_Type = Counter32
_Dfl260eIfBitsInCnt_Object = MibTableColumn
dfl260eIfBitsInCnt = _Dfl260eIfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 8),
    _Dfl260eIfBitsInCnt_Type()
)
dfl260eIfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfBitsInCnt.setStatus("current")
_Dfl260eIfBitsOutCnt_Type = Counter32
_Dfl260eIfBitsOutCnt_Object = MibTableColumn
dfl260eIfBitsOutCnt = _Dfl260eIfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 9),
    _Dfl260eIfBitsOutCnt_Type()
)
dfl260eIfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfBitsOutCnt.setStatus("current")
_Dfl260eIfPktsTotCnt_Type = Counter32
_Dfl260eIfPktsTotCnt_Object = MibTableColumn
dfl260eIfPktsTotCnt = _Dfl260eIfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 10),
    _Dfl260eIfPktsTotCnt_Type()
)
dfl260eIfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfPktsTotCnt.setStatus("current")
_Dfl260eIfBitsTotCnt_Type = Counter32
_Dfl260eIfBitsTotCnt_Object = MibTableColumn
dfl260eIfBitsTotCnt = _Dfl260eIfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 11),
    _Dfl260eIfBitsTotCnt_Type()
)
dfl260eIfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfBitsTotCnt.setStatus("current")
_Dfl260eIfHCPktsInCnt_Type = Counter64
_Dfl260eIfHCPktsInCnt_Object = MibTableColumn
dfl260eIfHCPktsInCnt = _Dfl260eIfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 12),
    _Dfl260eIfHCPktsInCnt_Type()
)
dfl260eIfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfHCPktsInCnt.setStatus("current")
_Dfl260eIfHCPktsOutCnt_Type = Counter64
_Dfl260eIfHCPktsOutCnt_Object = MibTableColumn
dfl260eIfHCPktsOutCnt = _Dfl260eIfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 13),
    _Dfl260eIfHCPktsOutCnt_Type()
)
dfl260eIfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfHCPktsOutCnt.setStatus("current")
_Dfl260eIfHCBitsInCnt_Type = Counter64
_Dfl260eIfHCBitsInCnt_Object = MibTableColumn
dfl260eIfHCBitsInCnt = _Dfl260eIfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 14),
    _Dfl260eIfHCBitsInCnt_Type()
)
dfl260eIfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfHCBitsInCnt.setStatus("current")
_Dfl260eIfHCBitsOutCnt_Type = Counter64
_Dfl260eIfHCBitsOutCnt_Object = MibTableColumn
dfl260eIfHCBitsOutCnt = _Dfl260eIfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 15),
    _Dfl260eIfHCBitsOutCnt_Type()
)
dfl260eIfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfHCBitsOutCnt.setStatus("current")
_Dfl260eIfHCPktsTotCnt_Type = Counter64
_Dfl260eIfHCPktsTotCnt_Object = MibTableColumn
dfl260eIfHCPktsTotCnt = _Dfl260eIfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 16),
    _Dfl260eIfHCPktsTotCnt_Type()
)
dfl260eIfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfHCPktsTotCnt.setStatus("current")
_Dfl260eIfHCBitsTotCnt_Type = Counter64
_Dfl260eIfHCBitsTotCnt_Object = MibTableColumn
dfl260eIfHCBitsTotCnt = _Dfl260eIfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 7, 1, 17),
    _Dfl260eIfHCBitsTotCnt_Type()
)
dfl260eIfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfHCBitsTotCnt.setStatus("current")
_Dfl260eIfRxRingTable_Object = MibTable
dfl260eIfRxRingTable = _Dfl260eIfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    dfl260eIfRxRingTable.setStatus("current")
_Dfl260eIfRxRingEntry_Object = MibTableRow
dfl260eIfRxRingEntry = _Dfl260eIfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1)
)
dfl260eIfRxRingEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eIfRxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl260eIfRxRingEntry.setStatus("current")


class _Dfl260eIfRxRingIndex_Type(Integer32):
    """Custom type dfl260eIfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eIfRxRingIndex_Type.__name__ = "Integer32"
_Dfl260eIfRxRingIndex_Object = MibTableColumn
dfl260eIfRxRingIndex = _Dfl260eIfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1, 1),
    _Dfl260eIfRxRingIndex_Type()
)
dfl260eIfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eIfRxRingIndex.setStatus("current")
_Dfl260eIfRxRingFifoErrors_Type = Counter32
_Dfl260eIfRxRingFifoErrors_Object = MibTableColumn
dfl260eIfRxRingFifoErrors = _Dfl260eIfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1, 2),
    _Dfl260eIfRxRingFifoErrors_Type()
)
dfl260eIfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfRxRingFifoErrors.setStatus("current")
_Dfl260eIfRxDespools_Type = Gauge32
_Dfl260eIfRxDespools_Object = MibTableColumn
dfl260eIfRxDespools = _Dfl260eIfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1, 3),
    _Dfl260eIfRxDespools_Type()
)
dfl260eIfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfRxDespools.setStatus("current")
_Dfl260eIfRxAvgUse_Type = Gauge32
_Dfl260eIfRxAvgUse_Object = MibTableColumn
dfl260eIfRxAvgUse = _Dfl260eIfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1, 4),
    _Dfl260eIfRxAvgUse_Type()
)
dfl260eIfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfRxAvgUse.setStatus("current")
_Dfl260eIfRxRingSaturation_Type = Gauge32
_Dfl260eIfRxRingSaturation_Object = MibTableColumn
dfl260eIfRxRingSaturation = _Dfl260eIfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1, 5),
    _Dfl260eIfRxRingSaturation_Type()
)
dfl260eIfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfRxRingSaturation.setStatus("current")
_Dfl260eRxRingFlooded_Type = Gauge32
_Dfl260eRxRingFlooded_Object = MibTableColumn
dfl260eRxRingFlooded = _Dfl260eRxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 8, 1, 6),
    _Dfl260eRxRingFlooded_Type()
)
dfl260eRxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eRxRingFlooded.setStatus("current")
_Dfl260eIfTxRingTable_Object = MibTable
dfl260eIfTxRingTable = _Dfl260eIfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    dfl260eIfTxRingTable.setStatus("current")
_Dfl260eIfTxRingEntry_Object = MibTableRow
dfl260eIfTxRingEntry = _Dfl260eIfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9, 1)
)
dfl260eIfTxRingEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eIfTxRingIndex"),
)
if mibBuilder.loadTexts:
    dfl260eIfTxRingEntry.setStatus("current")


class _Dfl260eIfTxRingIndex_Type(Integer32):
    """Custom type dfl260eIfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eIfTxRingIndex_Type.__name__ = "Integer32"
_Dfl260eIfTxRingIndex_Object = MibTableColumn
dfl260eIfTxRingIndex = _Dfl260eIfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9, 1, 1),
    _Dfl260eIfTxRingIndex_Type()
)
dfl260eIfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eIfTxRingIndex.setStatus("current")
_Dfl260eIfTxDespools_Type = Gauge32
_Dfl260eIfTxDespools_Object = MibTableColumn
dfl260eIfTxDespools = _Dfl260eIfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9, 1, 2),
    _Dfl260eIfTxDespools_Type()
)
dfl260eIfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfTxDespools.setStatus("current")
_Dfl260eIfTxAvgUse_Type = Gauge32
_Dfl260eIfTxAvgUse_Object = MibTableColumn
dfl260eIfTxAvgUse = _Dfl260eIfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9, 1, 3),
    _Dfl260eIfTxAvgUse_Type()
)
dfl260eIfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfTxAvgUse.setStatus("current")
_Dfl260eIfTxRingSaturation_Type = Gauge32
_Dfl260eIfTxRingSaturation_Object = MibTableColumn
dfl260eIfTxRingSaturation = _Dfl260eIfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9, 1, 4),
    _Dfl260eIfTxRingSaturation_Type()
)
dfl260eIfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfTxRingSaturation.setStatus("current")
_Dfl260eRxTingFlooded_Type = Gauge32
_Dfl260eRxTingFlooded_Object = MibTableColumn
dfl260eRxTingFlooded = _Dfl260eRxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 9, 1, 5),
    _Dfl260eRxTingFlooded_Type()
)
dfl260eRxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eRxTingFlooded.setStatus("current")
_Dfl260eIfVlanStatsTable_Object = MibTable
dfl260eIfVlanStatsTable = _Dfl260eIfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dfl260eIfVlanStatsTable.setStatus("current")
_Dfl260eIfVlanStatsEntry_Object = MibTableRow
dfl260eIfVlanStatsEntry = _Dfl260eIfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1)
)
dfl260eIfVlanStatsEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eIfVlanIndex"),
)
if mibBuilder.loadTexts:
    dfl260eIfVlanStatsEntry.setStatus("current")


class _Dfl260eIfVlanIndex_Type(Integer32):
    """Custom type dfl260eIfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eIfVlanIndex_Type.__name__ = "Integer32"
_Dfl260eIfVlanIndex_Object = MibTableColumn
dfl260eIfVlanIndex = _Dfl260eIfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 1),
    _Dfl260eIfVlanIndex_Type()
)
dfl260eIfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eIfVlanIndex.setStatus("current")
_Dfl260eIfVlanUntaggedInPkts_Type = Counter32
_Dfl260eIfVlanUntaggedInPkts_Object = MibTableColumn
dfl260eIfVlanUntaggedInPkts = _Dfl260eIfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 2),
    _Dfl260eIfVlanUntaggedInPkts_Type()
)
dfl260eIfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfVlanUntaggedInPkts.setStatus("current")
_Dfl260eIfVlanUntaggedOutPkts_Type = Counter32
_Dfl260eIfVlanUntaggedOutPkts_Object = MibTableColumn
dfl260eIfVlanUntaggedOutPkts = _Dfl260eIfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 3),
    _Dfl260eIfVlanUntaggedOutPkts_Type()
)
dfl260eIfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfVlanUntaggedOutPkts.setStatus("current")
_Dfl260eIfVlanUntaggedTotPkts_Type = Counter32
_Dfl260eIfVlanUntaggedTotPkts_Object = MibTableColumn
dfl260eIfVlanUntaggedTotPkts = _Dfl260eIfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 4),
    _Dfl260eIfVlanUntaggedTotPkts_Type()
)
dfl260eIfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfVlanUntaggedTotPkts.setStatus("current")
_Dfl260eIfVlanUntaggedInOctets_Type = Counter32
_Dfl260eIfVlanUntaggedInOctets_Object = MibTableColumn
dfl260eIfVlanUntaggedInOctets = _Dfl260eIfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 5),
    _Dfl260eIfVlanUntaggedInOctets_Type()
)
dfl260eIfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfVlanUntaggedInOctets.setStatus("current")
_Dfl260eIfVlanUntaggedOutOctets_Type = Counter32
_Dfl260eIfVlanUntaggedOutOctets_Object = MibTableColumn
dfl260eIfVlanUntaggedOutOctets = _Dfl260eIfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 6),
    _Dfl260eIfVlanUntaggedOutOctets_Type()
)
dfl260eIfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfVlanUntaggedOutOctets.setStatus("current")
_Dfl260eIfVlanUntaggedTotOctets_Type = Counter32
_Dfl260eIfVlanUntaggedTotOctets_Object = MibTableColumn
dfl260eIfVlanUntaggedTotOctets = _Dfl260eIfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 10, 1, 7),
    _Dfl260eIfVlanUntaggedTotOctets_Type()
)
dfl260eIfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIfVlanUntaggedTotOctets.setStatus("current")
_Dfl260eHWSensorTable_Object = MibTable
dfl260eHWSensorTable = _Dfl260eHWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    dfl260eHWSensorTable.setStatus("current")
_Dfl260eHWSensorEntry_Object = MibTableRow
dfl260eHWSensorEntry = _Dfl260eHWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 11, 1)
)
dfl260eHWSensorEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eHWSensorIndex"),
)
if mibBuilder.loadTexts:
    dfl260eHWSensorEntry.setStatus("current")


class _Dfl260eHWSensorIndex_Type(Integer32):
    """Custom type dfl260eHWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eHWSensorIndex_Type.__name__ = "Integer32"
_Dfl260eHWSensorIndex_Object = MibTableColumn
dfl260eHWSensorIndex = _Dfl260eHWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 11, 1, 1),
    _Dfl260eHWSensorIndex_Type()
)
dfl260eHWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eHWSensorIndex.setStatus("current")
_Dfl260eHWSensorName_Type = DisplayString
_Dfl260eHWSensorName_Object = MibTableColumn
dfl260eHWSensorName = _Dfl260eHWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 11, 1, 2),
    _Dfl260eHWSensorName_Type()
)
dfl260eHWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHWSensorName.setStatus("current")
_Dfl260eHWSensorValue_Type = Gauge32
_Dfl260eHWSensorValue_Object = MibTableColumn
dfl260eHWSensorValue = _Dfl260eHWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 11, 1, 3),
    _Dfl260eHWSensorValue_Type()
)
dfl260eHWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHWSensorValue.setStatus("current")
_Dfl260eHWSensorUnit_Type = DisplayString
_Dfl260eHWSensorUnit_Object = MibTableColumn
dfl260eHWSensorUnit = _Dfl260eHWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 11, 1, 4),
    _Dfl260eHWSensorUnit_Type()
)
dfl260eHWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHWSensorUnit.setStatus("current")
_Dfl260eSysMemUsage_Type = Gauge32
_Dfl260eSysMemUsage_Object = MibScalar
dfl260eSysMemUsage = _Dfl260eSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 12),
    _Dfl260eSysMemUsage_Type()
)
dfl260eSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysMemUsage.setStatus("current")
_Dfl260eSysTCPUsage_ObjectIdentity = ObjectIdentity
dfl260eSysTCPUsage = _Dfl260eSysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 13)
)
_Dfl260eSysTCPRecvSmall_Type = Gauge32
_Dfl260eSysTCPRecvSmall_Object = MibScalar
dfl260eSysTCPRecvSmall = _Dfl260eSysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 13, 1),
    _Dfl260eSysTCPRecvSmall_Type()
)
dfl260eSysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysTCPRecvSmall.setStatus("current")
_Dfl260eSysTCPRecvLarge_Type = Gauge32
_Dfl260eSysTCPRecvLarge_Object = MibScalar
dfl260eSysTCPRecvLarge = _Dfl260eSysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 13, 2),
    _Dfl260eSysTCPRecvLarge_Type()
)
dfl260eSysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysTCPRecvLarge.setStatus("current")
_Dfl260eSysTCPSendSmall_Type = Gauge32
_Dfl260eSysTCPSendSmall_Object = MibScalar
dfl260eSysTCPSendSmall = _Dfl260eSysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 13, 3),
    _Dfl260eSysTCPSendSmall_Type()
)
dfl260eSysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysTCPSendSmall.setStatus("current")
_Dfl260eSysTCPSendLarge_Type = Gauge32
_Dfl260eSysTCPSendLarge_Object = MibScalar
dfl260eSysTCPSendLarge = _Dfl260eSysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 13, 4),
    _Dfl260eSysTCPSendLarge_Type()
)
dfl260eSysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysTCPSendLarge.setStatus("current")
_Dfl260eSysTimerUsage_Type = Gauge32
_Dfl260eSysTimerUsage_Object = MibScalar
dfl260eSysTimerUsage = _Dfl260eSysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 14),
    _Dfl260eSysTimerUsage_Type()
)
dfl260eSysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysTimerUsage.setStatus("current")
_Dfl260eSysConnOPS_Type = Gauge32
_Dfl260eSysConnOPS_Object = MibScalar
dfl260eSysConnOPS = _Dfl260eSysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 15),
    _Dfl260eSysConnOPS_Type()
)
dfl260eSysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysConnOPS.setStatus("current")
_Dfl260eSysConnCPS_Type = Gauge32
_Dfl260eSysConnCPS_Object = MibScalar
dfl260eSysConnCPS = _Dfl260eSysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 16),
    _Dfl260eSysConnCPS_Type()
)
dfl260eSysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysConnCPS.setStatus("current")
_Dfl260eSysHCForwardedBits_Type = Counter64
_Dfl260eSysHCForwardedBits_Object = MibScalar
dfl260eSysHCForwardedBits = _Dfl260eSysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 1, 17),
    _Dfl260eSysHCForwardedBits_Type()
)
dfl260eSysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSysHCForwardedBits.setStatus("current")
_Dfl260eVPN_ObjectIdentity = ObjectIdentity
dfl260eVPN = _Dfl260eVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2)
)
_Dfl260eIPsec_ObjectIdentity = ObjectIdentity
dfl260eIPsec = _Dfl260eIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1)
)
_Dfl260eIPsecGlobal_ObjectIdentity = ObjectIdentity
dfl260eIPsecGlobal = _Dfl260eIPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1)
)
_Dfl260eIPsecPhaseOneActive_Type = Gauge32
_Dfl260eIPsecPhaseOneActive_Object = MibScalar
dfl260eIPsecPhaseOneActive = _Dfl260eIPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 1),
    _Dfl260eIPsecPhaseOneActive_Type()
)
dfl260eIPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecPhaseOneActive.setStatus("current")
_Dfl260eIPsecPhaseOneAggrModeDone_Type = Gauge32
_Dfl260eIPsecPhaseOneAggrModeDone_Object = MibScalar
dfl260eIPsecPhaseOneAggrModeDone = _Dfl260eIPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 2),
    _Dfl260eIPsecPhaseOneAggrModeDone_Type()
)
dfl260eIPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecPhaseOneAggrModeDone.setStatus("current")
_Dfl260eIPsecQuickModeActive_Type = Gauge32
_Dfl260eIPsecQuickModeActive_Object = MibScalar
dfl260eIPsecQuickModeActive = _Dfl260eIPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 3),
    _Dfl260eIPsecQuickModeActive_Type()
)
dfl260eIPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecQuickModeActive.setStatus("current")
_Dfl260eIPsecPhaseOneDone_Type = Counter32
_Dfl260eIPsecPhaseOneDone_Object = MibScalar
dfl260eIPsecPhaseOneDone = _Dfl260eIPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 4),
    _Dfl260eIPsecPhaseOneDone_Type()
)
dfl260eIPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecPhaseOneDone.setStatus("current")
_Dfl260eIPsecPhaseOneFailed_Type = Counter32
_Dfl260eIPsecPhaseOneFailed_Object = MibScalar
dfl260eIPsecPhaseOneFailed = _Dfl260eIPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 5),
    _Dfl260eIPsecPhaseOneFailed_Type()
)
dfl260eIPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecPhaseOneFailed.setStatus("current")
_Dfl260eIPsecPhaseOneRekeyed_Type = Counter32
_Dfl260eIPsecPhaseOneRekeyed_Object = MibScalar
dfl260eIPsecPhaseOneRekeyed = _Dfl260eIPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 6),
    _Dfl260eIPsecPhaseOneRekeyed_Type()
)
dfl260eIPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecPhaseOneRekeyed.setStatus("current")
_Dfl260eIPsecQuickModeDone_Type = Counter32
_Dfl260eIPsecQuickModeDone_Object = MibScalar
dfl260eIPsecQuickModeDone = _Dfl260eIPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 7),
    _Dfl260eIPsecQuickModeDone_Type()
)
dfl260eIPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecQuickModeDone.setStatus("current")
_Dfl260eIPsecQuickModeFailed_Type = Counter32
_Dfl260eIPsecQuickModeFailed_Object = MibScalar
dfl260eIPsecQuickModeFailed = _Dfl260eIPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 8),
    _Dfl260eIPsecQuickModeFailed_Type()
)
dfl260eIPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecQuickModeFailed.setStatus("current")
_Dfl260eIPsecInfoDone_Type = Counter32
_Dfl260eIPsecInfoDone_Object = MibScalar
dfl260eIPsecInfoDone = _Dfl260eIPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 9),
    _Dfl260eIPsecInfoDone_Type()
)
dfl260eIPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecInfoDone.setStatus("current")
_Dfl260eIPsecInfoFailed_Type = Counter32
_Dfl260eIPsecInfoFailed_Object = MibScalar
dfl260eIPsecInfoFailed = _Dfl260eIPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 10),
    _Dfl260eIPsecInfoFailed_Type()
)
dfl260eIPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecInfoFailed.setStatus("current")
_Dfl260eIPsecInOctetsComp_Type = Counter64
_Dfl260eIPsecInOctetsComp_Object = MibScalar
dfl260eIPsecInOctetsComp = _Dfl260eIPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 11),
    _Dfl260eIPsecInOctetsComp_Type()
)
dfl260eIPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecInOctetsComp.setStatus("current")
_Dfl260eIPsecInOctetsUncomp_Type = Counter64
_Dfl260eIPsecInOctetsUncomp_Object = MibScalar
dfl260eIPsecInOctetsUncomp = _Dfl260eIPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 12),
    _Dfl260eIPsecInOctetsUncomp_Type()
)
dfl260eIPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecInOctetsUncomp.setStatus("current")
_Dfl260eIPsecOutOctetsComp_Type = Counter64
_Dfl260eIPsecOutOctetsComp_Object = MibScalar
dfl260eIPsecOutOctetsComp = _Dfl260eIPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 13),
    _Dfl260eIPsecOutOctetsComp_Type()
)
dfl260eIPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecOutOctetsComp.setStatus("current")
_Dfl260eIPsecOutOctetsUncomp_Type = Counter64
_Dfl260eIPsecOutOctetsUncomp_Object = MibScalar
dfl260eIPsecOutOctetsUncomp = _Dfl260eIPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 14),
    _Dfl260eIPsecOutOctetsUncomp_Type()
)
dfl260eIPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecOutOctetsUncomp.setStatus("current")
_Dfl260eIPsecForwardedOctetsComp_Type = Counter64
_Dfl260eIPsecForwardedOctetsComp_Object = MibScalar
dfl260eIPsecForwardedOctetsComp = _Dfl260eIPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 15),
    _Dfl260eIPsecForwardedOctetsComp_Type()
)
dfl260eIPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecForwardedOctetsComp.setStatus("current")
_Dfl260eIPsecForwardedOctetsUcomp_Type = Counter64
_Dfl260eIPsecForwardedOctetsUcomp_Object = MibScalar
dfl260eIPsecForwardedOctetsUcomp = _Dfl260eIPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 16),
    _Dfl260eIPsecForwardedOctetsUcomp_Type()
)
dfl260eIPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecForwardedOctetsUcomp.setStatus("current")
_Dfl260eIPsecInPackets_Type = Counter64
_Dfl260eIPsecInPackets_Object = MibScalar
dfl260eIPsecInPackets = _Dfl260eIPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 17),
    _Dfl260eIPsecInPackets_Type()
)
dfl260eIPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecInPackets.setStatus("current")
_Dfl260eIPsecOutPackets_Type = Counter64
_Dfl260eIPsecOutPackets_Object = MibScalar
dfl260eIPsecOutPackets = _Dfl260eIPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 18),
    _Dfl260eIPsecOutPackets_Type()
)
dfl260eIPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecOutPackets.setStatus("current")
_Dfl260eIPsecForwardedPackets_Type = Counter64
_Dfl260eIPsecForwardedPackets_Object = MibScalar
dfl260eIPsecForwardedPackets = _Dfl260eIPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 19),
    _Dfl260eIPsecForwardedPackets_Type()
)
dfl260eIPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecForwardedPackets.setStatus("current")
_Dfl260eIPsecActiveTransforms_Type = Gauge32
_Dfl260eIPsecActiveTransforms_Object = MibScalar
dfl260eIPsecActiveTransforms = _Dfl260eIPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 20),
    _Dfl260eIPsecActiveTransforms_Type()
)
dfl260eIPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecActiveTransforms.setStatus("current")
_Dfl260eIPsecTotalTransforms_Type = Counter32
_Dfl260eIPsecTotalTransforms_Object = MibScalar
dfl260eIPsecTotalTransforms = _Dfl260eIPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 21),
    _Dfl260eIPsecTotalTransforms_Type()
)
dfl260eIPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecTotalTransforms.setStatus("current")
_Dfl260eIPsecOutOfTransforms_Type = Counter32
_Dfl260eIPsecOutOfTransforms_Object = MibScalar
dfl260eIPsecOutOfTransforms = _Dfl260eIPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 22),
    _Dfl260eIPsecOutOfTransforms_Type()
)
dfl260eIPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecOutOfTransforms.setStatus("current")
_Dfl260eIPsecTotalRekeys_Type = Counter32
_Dfl260eIPsecTotalRekeys_Object = MibScalar
dfl260eIPsecTotalRekeys = _Dfl260eIPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 2, 1, 1, 23),
    _Dfl260eIPsecTotalRekeys_Type()
)
dfl260eIPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPsecTotalRekeys.setStatus("current")
_Dfl260eRules_ObjectIdentity = ObjectIdentity
dfl260eRules = _Dfl260eRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 3)
)
_Dfl260eRuleUseTable_Object = MibTable
dfl260eRuleUseTable = _Dfl260eRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dfl260eRuleUseTable.setStatus("current")
_Dfl260eRuleUseEntry_Object = MibTableRow
dfl260eRuleUseEntry = _Dfl260eRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 3, 2, 1)
)
dfl260eRuleUseEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260eRuleUseEntry.setStatus("current")


class _Dfl260eRuleIndex_Type(Integer32):
    """Custom type dfl260eRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eRuleIndex_Type.__name__ = "Integer32"
_Dfl260eRuleIndex_Object = MibTableColumn
dfl260eRuleIndex = _Dfl260eRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 3, 2, 1, 1),
    _Dfl260eRuleIndex_Type()
)
dfl260eRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eRuleIndex.setStatus("current")
_Dfl260eRuleName_Type = DisplayString
_Dfl260eRuleName_Object = MibTableColumn
dfl260eRuleName = _Dfl260eRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 3, 2, 1, 2),
    _Dfl260eRuleName_Type()
)
dfl260eRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eRuleName.setStatus("current")
_Dfl260eRuleUse_Type = Counter32
_Dfl260eRuleUse_Object = MibTableColumn
dfl260eRuleUse = _Dfl260eRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 3, 2, 1, 3),
    _Dfl260eRuleUse_Type()
)
dfl260eRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eRuleUse.setStatus("current")
_Dfl260eIPPools_ObjectIdentity = ObjectIdentity
dfl260eIPPools = _Dfl260eIPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4)
)
_Dfl260eIPPoolsNumber_Type = Integer32
_Dfl260eIPPoolsNumber_Object = MibScalar
dfl260eIPPoolsNumber = _Dfl260eIPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 1),
    _Dfl260eIPPoolsNumber_Type()
)
dfl260eIPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolsNumber.setStatus("current")
_Dfl260eIPPoolTable_Object = MibTable
dfl260eIPPoolTable = _Dfl260eIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dfl260eIPPoolTable.setStatus("current")
_Dfl260eIPPoolEntry_Object = MibTableRow
dfl260eIPPoolEntry = _Dfl260eIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1)
)
dfl260eIPPoolEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eIPPoolIndex"),
)
if mibBuilder.loadTexts:
    dfl260eIPPoolEntry.setStatus("current")


class _Dfl260eIPPoolIndex_Type(Integer32):
    """Custom type dfl260eIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eIPPoolIndex_Type.__name__ = "Integer32"
_Dfl260eIPPoolIndex_Object = MibTableColumn
dfl260eIPPoolIndex = _Dfl260eIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 1),
    _Dfl260eIPPoolIndex_Type()
)
dfl260eIPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eIPPoolIndex.setStatus("current")
_Dfl260eIPPoolName_Type = DisplayString
_Dfl260eIPPoolName_Object = MibTableColumn
dfl260eIPPoolName = _Dfl260eIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 2),
    _Dfl260eIPPoolName_Type()
)
dfl260eIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolName.setStatus("current")
_Dfl260eIPPoolPrepare_Type = Gauge32
_Dfl260eIPPoolPrepare_Object = MibTableColumn
dfl260eIPPoolPrepare = _Dfl260eIPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 3),
    _Dfl260eIPPoolPrepare_Type()
)
dfl260eIPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolPrepare.setStatus("current")
_Dfl260eIPPoolFree_Type = Gauge32
_Dfl260eIPPoolFree_Object = MibTableColumn
dfl260eIPPoolFree = _Dfl260eIPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 4),
    _Dfl260eIPPoolFree_Type()
)
dfl260eIPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolFree.setStatus("current")
_Dfl260eIPPoolMisses_Type = Gauge32
_Dfl260eIPPoolMisses_Object = MibTableColumn
dfl260eIPPoolMisses = _Dfl260eIPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 5),
    _Dfl260eIPPoolMisses_Type()
)
dfl260eIPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolMisses.setStatus("current")
_Dfl260eIPPoolClientFails_Type = Gauge32
_Dfl260eIPPoolClientFails_Object = MibTableColumn
dfl260eIPPoolClientFails = _Dfl260eIPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 6),
    _Dfl260eIPPoolClientFails_Type()
)
dfl260eIPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolClientFails.setStatus("current")
_Dfl260eIPPoolUsed_Type = Gauge32
_Dfl260eIPPoolUsed_Object = MibTableColumn
dfl260eIPPoolUsed = _Dfl260eIPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 4, 2, 1, 7),
    _Dfl260eIPPoolUsed_Type()
)
dfl260eIPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eIPPoolUsed.setStatus("current")
_Dfl260eDHCPServer_ObjectIdentity = ObjectIdentity
dfl260eDHCPServer = _Dfl260eDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5)
)
_Dfl260eDHCPTotalRejected_Type = Gauge32
_Dfl260eDHCPTotalRejected_Object = MibScalar
dfl260eDHCPTotalRejected = _Dfl260eDHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 1),
    _Dfl260eDHCPTotalRejected_Type()
)
dfl260eDHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPTotalRejected.setStatus("current")
_Dfl260eDHCPRuleTable_Object = MibTable
dfl260eDHCPRuleTable = _Dfl260eDHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    dfl260eDHCPRuleTable.setStatus("current")
_Dfl260eDHCPRuleEntry_Object = MibTableRow
dfl260eDHCPRuleEntry = _Dfl260eDHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1)
)
dfl260eDHCPRuleEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eDHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260eDHCPRuleEntry.setStatus("current")


class _Dfl260eDHCPRuleIndex_Type(Integer32):
    """Custom type dfl260eDHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eDHCPRuleIndex_Type.__name__ = "Integer32"
_Dfl260eDHCPRuleIndex_Object = MibTableColumn
dfl260eDHCPRuleIndex = _Dfl260eDHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 1),
    _Dfl260eDHCPRuleIndex_Type()
)
dfl260eDHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eDHCPRuleIndex.setStatus("current")
_Dfl260eDHCPRuleName_Type = DisplayString
_Dfl260eDHCPRuleName_Object = MibTableColumn
dfl260eDHCPRuleName = _Dfl260eDHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 2),
    _Dfl260eDHCPRuleName_Type()
)
dfl260eDHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRuleName.setStatus("current")
_Dfl260eDHCPRuleUsage_Type = Gauge32
_Dfl260eDHCPRuleUsage_Object = MibTableColumn
dfl260eDHCPRuleUsage = _Dfl260eDHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 3),
    _Dfl260eDHCPRuleUsage_Type()
)
dfl260eDHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRuleUsage.setStatus("current")
_Dfl260eDHCPRuleUsagePercent_Type = Gauge32
_Dfl260eDHCPRuleUsagePercent_Object = MibTableColumn
dfl260eDHCPRuleUsagePercent = _Dfl260eDHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 4),
    _Dfl260eDHCPRuleUsagePercent_Type()
)
dfl260eDHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRuleUsagePercent.setStatus("current")
_Dfl260eDHCPActiveClients_Type = Gauge32
_Dfl260eDHCPActiveClients_Object = MibTableColumn
dfl260eDHCPActiveClients = _Dfl260eDHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 5),
    _Dfl260eDHCPActiveClients_Type()
)
dfl260eDHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPActiveClients.setStatus("current")
_Dfl260eDHCPActiveClientsPercent_Type = Gauge32
_Dfl260eDHCPActiveClientsPercent_Object = MibTableColumn
dfl260eDHCPActiveClientsPercent = _Dfl260eDHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 6),
    _Dfl260eDHCPActiveClientsPercent_Type()
)
dfl260eDHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPActiveClientsPercent.setStatus("current")
_Dfl260eDHCPRejectedRequests_Type = Gauge32
_Dfl260eDHCPRejectedRequests_Object = MibTableColumn
dfl260eDHCPRejectedRequests = _Dfl260eDHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 7),
    _Dfl260eDHCPRejectedRequests_Type()
)
dfl260eDHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRejectedRequests.setStatus("current")
_Dfl260eDHCPTotalLeases_Type = Gauge32
_Dfl260eDHCPTotalLeases_Object = MibTableColumn
dfl260eDHCPTotalLeases = _Dfl260eDHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 5, 2, 1, 8),
    _Dfl260eDHCPTotalLeases_Type()
)
dfl260eDHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPTotalLeases.setStatus("current")
_Dfl260eUserAuth_ObjectIdentity = ObjectIdentity
dfl260eUserAuth = _Dfl260eUserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6)
)
_Dfl260eUserAuthHTTPUsers_Type = Gauge32
_Dfl260eUserAuthHTTPUsers_Object = MibScalar
dfl260eUserAuthHTTPUsers = _Dfl260eUserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 1),
    _Dfl260eUserAuthHTTPUsers_Type()
)
dfl260eUserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthHTTPUsers.setStatus("current")
_Dfl260eUserAuthXAUTHUsers_Type = Gauge32
_Dfl260eUserAuthXAUTHUsers_Object = MibScalar
dfl260eUserAuthXAUTHUsers = _Dfl260eUserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 2),
    _Dfl260eUserAuthXAUTHUsers_Type()
)
dfl260eUserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthXAUTHUsers.setStatus("current")
_Dfl260eUserAuthHTTPSUsers_Type = Gauge32
_Dfl260eUserAuthHTTPSUsers_Object = MibScalar
dfl260eUserAuthHTTPSUsers = _Dfl260eUserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 3),
    _Dfl260eUserAuthHTTPSUsers_Type()
)
dfl260eUserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthHTTPSUsers.setStatus("current")
_Dfl260eUserAuthPPPUsers_Type = Gauge32
_Dfl260eUserAuthPPPUsers_Object = MibScalar
dfl260eUserAuthPPPUsers = _Dfl260eUserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 4),
    _Dfl260eUserAuthPPPUsers_Type()
)
dfl260eUserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthPPPUsers.setStatus("current")
_Dfl260eUserAuthEAPUsers_Type = Gauge32
_Dfl260eUserAuthEAPUsers_Object = MibScalar
dfl260eUserAuthEAPUsers = _Dfl260eUserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 5),
    _Dfl260eUserAuthEAPUsers_Type()
)
dfl260eUserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthEAPUsers.setStatus("current")
_Dfl260eUserAuthRuleUseTable_Object = MibTable
dfl260eUserAuthRuleUseTable = _Dfl260eUserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    dfl260eUserAuthRuleUseTable.setStatus("current")
_Dfl260eUserAuthRuleUseEntry_Object = MibTableRow
dfl260eUserAuthRuleUseEntry = _Dfl260eUserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 6, 1)
)
dfl260eUserAuthRuleUseEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eUserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260eUserAuthRuleUseEntry.setStatus("current")


class _Dfl260eUserAuthRuleIndex_Type(Integer32):
    """Custom type dfl260eUserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eUserAuthRuleIndex_Type.__name__ = "Integer32"
_Dfl260eUserAuthRuleIndex_Object = MibTableColumn
dfl260eUserAuthRuleIndex = _Dfl260eUserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 6, 1, 1),
    _Dfl260eUserAuthRuleIndex_Type()
)
dfl260eUserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eUserAuthRuleIndex.setStatus("current")
_Dfl260eUserAuthRuleName_Type = DisplayString
_Dfl260eUserAuthRuleName_Object = MibTableColumn
dfl260eUserAuthRuleName = _Dfl260eUserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 6, 1, 2),
    _Dfl260eUserAuthRuleName_Type()
)
dfl260eUserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthRuleName.setStatus("current")
_Dfl260eUserAuthRuleUse_Type = Counter32
_Dfl260eUserAuthRuleUse_Object = MibTableColumn
dfl260eUserAuthRuleUse = _Dfl260eUserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 6, 6, 1, 3),
    _Dfl260eUserAuthRuleUse_Type()
)
dfl260eUserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eUserAuthRuleUse.setStatus("current")
_Dfl260eLinkMonitor_ObjectIdentity = ObjectIdentity
dfl260eLinkMonitor = _Dfl260eLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7)
)
_Dfl260eLinkMonGrp_Type = Integer32
_Dfl260eLinkMonGrp_Object = MibScalar
dfl260eLinkMonGrp = _Dfl260eLinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 1),
    _Dfl260eLinkMonGrp_Type()
)
dfl260eLinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eLinkMonGrp.setStatus("current")
_Dfl260eLinkMonGrpTable_Object = MibTable
dfl260eLinkMonGrpTable = _Dfl260eLinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dfl260eLinkMonGrpTable.setStatus("current")
_Dfl260eLinkMonGrpEntry_Object = MibTableRow
dfl260eLinkMonGrpEntry = _Dfl260eLinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 2, 1)
)
dfl260eLinkMonGrpEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eLinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    dfl260eLinkMonGrpEntry.setStatus("current")


class _Dfl260eLinkMonGrpIndex_Type(Integer32):
    """Custom type dfl260eLinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eLinkMonGrpIndex_Type.__name__ = "Integer32"
_Dfl260eLinkMonGrpIndex_Object = MibTableColumn
dfl260eLinkMonGrpIndex = _Dfl260eLinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 2, 1, 1),
    _Dfl260eLinkMonGrpIndex_Type()
)
dfl260eLinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eLinkMonGrpIndex.setStatus("current")
_Dfl260eLinkMonGrpName_Type = DisplayString
_Dfl260eLinkMonGrpName_Object = MibTableColumn
dfl260eLinkMonGrpName = _Dfl260eLinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 2, 1, 2),
    _Dfl260eLinkMonGrpName_Type()
)
dfl260eLinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eLinkMonGrpName.setStatus("current")
_Dfl260eLinkMonGrpHostsUp_Type = Gauge32
_Dfl260eLinkMonGrpHostsUp_Object = MibTableColumn
dfl260eLinkMonGrpHostsUp = _Dfl260eLinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 2, 1, 3),
    _Dfl260eLinkMonGrpHostsUp_Type()
)
dfl260eLinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eLinkMonGrpHostsUp.setStatus("current")
_Dfl260eLinkMonHostTable_Object = MibTable
dfl260eLinkMonHostTable = _Dfl260eLinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    dfl260eLinkMonHostTable.setStatus("current")
_Dfl260eLinkMonHostEntry_Object = MibTableRow
dfl260eLinkMonHostEntry = _Dfl260eLinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 3, 1)
)
dfl260eLinkMonHostEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eLinkMonGrpIndex"),
    (0, "DFL260e-MIB", "dfl260eLinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    dfl260eLinkMonHostEntry.setStatus("current")


class _Dfl260eLinkMonHostIndex_Type(Integer32):
    """Custom type dfl260eLinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eLinkMonHostIndex_Type.__name__ = "Integer32"
_Dfl260eLinkMonHostIndex_Object = MibTableColumn
dfl260eLinkMonHostIndex = _Dfl260eLinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 3, 1, 1),
    _Dfl260eLinkMonHostIndex_Type()
)
dfl260eLinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eLinkMonHostIndex.setStatus("current")
_Dfl260eLinkMonHostId_Type = DisplayString
_Dfl260eLinkMonHostId_Object = MibTableColumn
dfl260eLinkMonHostId = _Dfl260eLinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 3, 1, 2),
    _Dfl260eLinkMonHostId_Type()
)
dfl260eLinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eLinkMonHostId.setStatus("current")
_Dfl260eLinkMonHostShortTermLoss_Type = Gauge32
_Dfl260eLinkMonHostShortTermLoss_Object = MibTableColumn
dfl260eLinkMonHostShortTermLoss = _Dfl260eLinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 3, 1, 3),
    _Dfl260eLinkMonHostShortTermLoss_Type()
)
dfl260eLinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eLinkMonHostShortTermLoss.setStatus("current")
_Dfl260eLinkMonHostPacketsLost_Type = Counter32
_Dfl260eLinkMonHostPacketsLost_Object = MibTableColumn
dfl260eLinkMonHostPacketsLost = _Dfl260eLinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 7, 3, 1, 4),
    _Dfl260eLinkMonHostPacketsLost_Type()
)
dfl260eLinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eLinkMonHostPacketsLost.setStatus("current")
_Dfl260ePipes_ObjectIdentity = ObjectIdentity
dfl260ePipes = _Dfl260ePipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8)
)
_Dfl260ePipeUsers_Type = Gauge32
_Dfl260ePipeUsers_Object = MibScalar
dfl260ePipeUsers = _Dfl260ePipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 1),
    _Dfl260ePipeUsers_Type()
)
dfl260ePipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeUsers.setStatus("current")
_Dfl260ePipeTable_Object = MibTable
dfl260ePipeTable = _Dfl260ePipeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dfl260ePipeTable.setStatus("current")
_Dfl260ePipeEntry_Object = MibTableRow
dfl260ePipeEntry = _Dfl260ePipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1)
)
dfl260ePipeEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260ePipeIndex"),
)
if mibBuilder.loadTexts:
    dfl260ePipeEntry.setStatus("current")


class _Dfl260ePipeIndex_Type(Integer32):
    """Custom type dfl260ePipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260ePipeIndex_Type.__name__ = "Integer32"
_Dfl260ePipeIndex_Object = MibTableColumn
dfl260ePipeIndex = _Dfl260ePipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 1),
    _Dfl260ePipeIndex_Type()
)
dfl260ePipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260ePipeIndex.setStatus("current")
_Dfl260ePipeName_Type = DisplayString
_Dfl260ePipeName_Object = MibTableColumn
dfl260ePipeName = _Dfl260ePipeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 2),
    _Dfl260ePipeName_Type()
)
dfl260ePipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeName.setStatus("current")
_Dfl260ePipeMinPrec_Type = Integer32
_Dfl260ePipeMinPrec_Object = MibTableColumn
dfl260ePipeMinPrec = _Dfl260ePipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 3),
    _Dfl260ePipeMinPrec_Type()
)
dfl260ePipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeMinPrec.setStatus("current")
_Dfl260ePipeMaxPrec_Type = Integer32
_Dfl260ePipeMaxPrec_Object = MibTableColumn
dfl260ePipeMaxPrec = _Dfl260ePipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 4),
    _Dfl260ePipeMaxPrec_Type()
)
dfl260ePipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeMaxPrec.setStatus("current")
_Dfl260ePipeDefPrec_Type = Integer32
_Dfl260ePipeDefPrec_Object = MibTableColumn
dfl260ePipeDefPrec = _Dfl260ePipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 5),
    _Dfl260ePipeDefPrec_Type()
)
dfl260ePipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeDefPrec.setStatus("current")
_Dfl260ePipeNumPrec_Type = Integer32
_Dfl260ePipeNumPrec_Object = MibTableColumn
dfl260ePipeNumPrec = _Dfl260ePipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 6),
    _Dfl260ePipeNumPrec_Type()
)
dfl260ePipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeNumPrec.setStatus("current")
_Dfl260ePipeNumUsers_Type = Gauge32
_Dfl260ePipeNumUsers_Object = MibTableColumn
dfl260ePipeNumUsers = _Dfl260ePipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 7),
    _Dfl260ePipeNumUsers_Type()
)
dfl260ePipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeNumUsers.setStatus("current")
_Dfl260ePipeCurrentBps_Type = Gauge32
_Dfl260ePipeCurrentBps_Object = MibTableColumn
dfl260ePipeCurrentBps = _Dfl260ePipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 8),
    _Dfl260ePipeCurrentBps_Type()
)
dfl260ePipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeCurrentBps.setStatus("current")
_Dfl260ePipeCurrentPps_Type = Gauge32
_Dfl260ePipeCurrentPps_Object = MibTableColumn
dfl260ePipeCurrentPps = _Dfl260ePipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 9),
    _Dfl260ePipeCurrentPps_Type()
)
dfl260ePipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeCurrentPps.setStatus("current")
_Dfl260ePipeDelayedPackets_Type = Counter32
_Dfl260ePipeDelayedPackets_Object = MibTableColumn
dfl260ePipeDelayedPackets = _Dfl260ePipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 10),
    _Dfl260ePipeDelayedPackets_Type()
)
dfl260ePipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeDelayedPackets.setStatus("current")
_Dfl260ePipeDropedPackets_Type = Counter32
_Dfl260ePipeDropedPackets_Object = MibTableColumn
dfl260ePipeDropedPackets = _Dfl260ePipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 2, 1, 11),
    _Dfl260ePipeDropedPackets_Type()
)
dfl260ePipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipeDropedPackets.setStatus("current")
_Dfl260ePipePrecTable_Object = MibTable
dfl260ePipePrecTable = _Dfl260ePipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dfl260ePipePrecTable.setStatus("current")
_Dfl260ePipePrecEntry_Object = MibTableRow
dfl260ePipePrecEntry = _Dfl260ePipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1)
)
dfl260ePipePrecEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260ePipeIndex"),
    (0, "DFL260e-MIB", "dfl260ePipePrecIndex"),
)
if mibBuilder.loadTexts:
    dfl260ePipePrecEntry.setStatus("current")


class _Dfl260ePipePrecIndex_Type(Integer32):
    """Custom type dfl260ePipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260ePipePrecIndex_Type.__name__ = "Integer32"
_Dfl260ePipePrecIndex_Object = MibTableColumn
dfl260ePipePrecIndex = _Dfl260ePipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 1),
    _Dfl260ePipePrecIndex_Type()
)
dfl260ePipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260ePipePrecIndex.setStatus("current")
_Dfl260ePipePrec_Type = Integer32
_Dfl260ePipePrec_Object = MibTableColumn
dfl260ePipePrec = _Dfl260ePipePrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 2),
    _Dfl260ePipePrec_Type()
)
dfl260ePipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrec.setStatus("current")
_Dfl260ePipePrecBps_Type = Gauge32
_Dfl260ePipePrecBps_Object = MibTableColumn
dfl260ePipePrecBps = _Dfl260ePipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 3),
    _Dfl260ePipePrecBps_Type()
)
dfl260ePipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecBps.setStatus("current")
_Dfl260ePipePrecTotalPps_Type = Gauge32
_Dfl260ePipePrecTotalPps_Object = MibTableColumn
dfl260ePipePrecTotalPps = _Dfl260ePipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 4),
    _Dfl260ePipePrecTotalPps_Type()
)
dfl260ePipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecTotalPps.setStatus("current")
_Dfl260ePipePrecReservedBps_Type = Gauge32
_Dfl260ePipePrecReservedBps_Object = MibTableColumn
dfl260ePipePrecReservedBps = _Dfl260ePipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 5),
    _Dfl260ePipePrecReservedBps_Type()
)
dfl260ePipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecReservedBps.setStatus("current")
_Dfl260ePipePrecDynLimBps_Type = Gauge32
_Dfl260ePipePrecDynLimBps_Object = MibTableColumn
dfl260ePipePrecDynLimBps = _Dfl260ePipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 6),
    _Dfl260ePipePrecDynLimBps_Type()
)
dfl260ePipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecDynLimBps.setStatus("current")
_Dfl260ePipePrecDynUsrLimBps_Type = Gauge32
_Dfl260ePipePrecDynUsrLimBps_Object = MibTableColumn
dfl260ePipePrecDynUsrLimBps = _Dfl260ePipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 7),
    _Dfl260ePipePrecDynUsrLimBps_Type()
)
dfl260ePipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecDynUsrLimBps.setStatus("current")
_Dfl260ePipePrecDelayedPackets_Type = Counter32
_Dfl260ePipePrecDelayedPackets_Object = MibTableColumn
dfl260ePipePrecDelayedPackets = _Dfl260ePipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 8),
    _Dfl260ePipePrecDelayedPackets_Type()
)
dfl260ePipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecDelayedPackets.setStatus("current")
_Dfl260ePipePrecDropedPackets_Type = Counter32
_Dfl260ePipePrecDropedPackets_Object = MibTableColumn
dfl260ePipePrecDropedPackets = _Dfl260ePipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 8, 3, 1, 9),
    _Dfl260ePipePrecDropedPackets_Type()
)
dfl260ePipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260ePipePrecDropedPackets.setStatus("current")
_Dfl260eALG_ObjectIdentity = ObjectIdentity
dfl260eALG = _Dfl260eALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9)
)
_Dfl260eAlgSessions_Type = Gauge32
_Dfl260eAlgSessions_Object = MibScalar
dfl260eAlgSessions = _Dfl260eAlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 1),
    _Dfl260eAlgSessions_Type()
)
dfl260eAlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eAlgSessions.setStatus("current")
_Dfl260eAlgConnections_Type = Gauge32
_Dfl260eAlgConnections_Object = MibScalar
dfl260eAlgConnections = _Dfl260eAlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 2),
    _Dfl260eAlgConnections_Type()
)
dfl260eAlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eAlgConnections.setStatus("current")
_Dfl260eAlgTCPStreams_Type = Gauge32
_Dfl260eAlgTCPStreams_Object = MibScalar
dfl260eAlgTCPStreams = _Dfl260eAlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 3),
    _Dfl260eAlgTCPStreams_Type()
)
dfl260eAlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eAlgTCPStreams.setStatus("current")
_Dfl260eHttpAlg_ObjectIdentity = ObjectIdentity
dfl260eHttpAlg = _Dfl260eHttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4)
)
_Dfl260eHttpAlgTable_Object = MibTable
dfl260eHttpAlgTable = _Dfl260eHttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dfl260eHttpAlgTable.setStatus("current")
_Dfl260eHttpAlgEntry_Object = MibTableRow
dfl260eHttpAlgEntry = _Dfl260eHttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1, 1)
)
dfl260eHttpAlgEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eHttpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl260eHttpAlgEntry.setStatus("current")


class _Dfl260eHttpAlgIndex_Type(Integer32):
    """Custom type dfl260eHttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eHttpAlgIndex_Type.__name__ = "Integer32"
_Dfl260eHttpAlgIndex_Object = MibTableColumn
dfl260eHttpAlgIndex = _Dfl260eHttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1, 1, 1),
    _Dfl260eHttpAlgIndex_Type()
)
dfl260eHttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eHttpAlgIndex.setStatus("current")
_Dfl260eHttpAlgName_Type = DisplayString
_Dfl260eHttpAlgName_Object = MibTableColumn
dfl260eHttpAlgName = _Dfl260eHttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1, 1, 2),
    _Dfl260eHttpAlgName_Type()
)
dfl260eHttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgName.setStatus("current")
_Dfl260eHttpAlgTotalRequested_Type = Gauge32
_Dfl260eHttpAlgTotalRequested_Object = MibTableColumn
dfl260eHttpAlgTotalRequested = _Dfl260eHttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1, 1, 3),
    _Dfl260eHttpAlgTotalRequested_Type()
)
dfl260eHttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgTotalRequested.setStatus("current")
_Dfl260eHttpAlgTotalAllowed_Type = Gauge32
_Dfl260eHttpAlgTotalAllowed_Object = MibTableColumn
dfl260eHttpAlgTotalAllowed = _Dfl260eHttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1, 1, 4),
    _Dfl260eHttpAlgTotalAllowed_Type()
)
dfl260eHttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgTotalAllowed.setStatus("current")
_Dfl260eHttpAlgTotalBlocked_Type = Gauge32
_Dfl260eHttpAlgTotalBlocked_Object = MibTableColumn
dfl260eHttpAlgTotalBlocked = _Dfl260eHttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 1, 1, 5),
    _Dfl260eHttpAlgTotalBlocked_Type()
)
dfl260eHttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgTotalBlocked.setStatus("current")
_Dfl260eHttpAlgCntFltTable_Object = MibTable
dfl260eHttpAlgCntFltTable = _Dfl260eHttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltTable.setStatus("current")
_Dfl260eHttpAlgCntFltEntry_Object = MibTableRow
dfl260eHttpAlgCntFltEntry = _Dfl260eHttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2, 1)
)
dfl260eHttpAlgCntFltEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eHttpAlgIndex"),
    (0, "DFL260e-MIB", "dfl260eHttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltEntry.setStatus("current")


class _Dfl260eHttpAlgCntFltIndex_Type(Integer32):
    """Custom type dfl260eHttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eHttpAlgCntFltIndex_Type.__name__ = "Integer32"
_Dfl260eHttpAlgCntFltIndex_Object = MibTableColumn
dfl260eHttpAlgCntFltIndex = _Dfl260eHttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2, 1, 1),
    _Dfl260eHttpAlgCntFltIndex_Type()
)
dfl260eHttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltIndex.setStatus("current")
_Dfl260eHttpAlgCntFltName_Type = DisplayString
_Dfl260eHttpAlgCntFltName_Object = MibTableColumn
dfl260eHttpAlgCntFltName = _Dfl260eHttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2, 1, 2),
    _Dfl260eHttpAlgCntFltName_Type()
)
dfl260eHttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltName.setStatus("current")
_Dfl260eHttpAlgCntFltRequests_Type = Gauge32
_Dfl260eHttpAlgCntFltRequests_Object = MibTableColumn
dfl260eHttpAlgCntFltRequests = _Dfl260eHttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2, 1, 3),
    _Dfl260eHttpAlgCntFltRequests_Type()
)
dfl260eHttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltRequests.setStatus("current")
_Dfl260eHttpAlgCntFltAllowed_Type = Gauge32
_Dfl260eHttpAlgCntFltAllowed_Object = MibTableColumn
dfl260eHttpAlgCntFltAllowed = _Dfl260eHttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2, 1, 4),
    _Dfl260eHttpAlgCntFltAllowed_Type()
)
dfl260eHttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltAllowed.setStatus("current")
_Dfl260eHttpAlgCntFltBlocked_Type = Gauge32
_Dfl260eHttpAlgCntFltBlocked_Object = MibTableColumn
dfl260eHttpAlgCntFltBlocked = _Dfl260eHttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 4, 2, 1, 5),
    _Dfl260eHttpAlgCntFltBlocked_Type()
)
dfl260eHttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHttpAlgCntFltBlocked.setStatus("current")
_Dfl260eSmtpAlg_ObjectIdentity = ObjectIdentity
dfl260eSmtpAlg = _Dfl260eSmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5)
)
_Dfl260eSmtpAlgTable_Object = MibTable
dfl260eSmtpAlgTable = _Dfl260eSmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    dfl260eSmtpAlgTable.setStatus("current")
_Dfl260eSmtpAlgEntry_Object = MibTableRow
dfl260eSmtpAlgEntry = _Dfl260eSmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1, 1)
)
dfl260eSmtpAlgEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eSmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    dfl260eSmtpAlgEntry.setStatus("current")


class _Dfl260eSmtpAlgIndex_Type(Integer32):
    """Custom type dfl260eSmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eSmtpAlgIndex_Type.__name__ = "Integer32"
_Dfl260eSmtpAlgIndex_Object = MibTableColumn
dfl260eSmtpAlgIndex = _Dfl260eSmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1, 1, 1),
    _Dfl260eSmtpAlgIndex_Type()
)
dfl260eSmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgIndex.setStatus("current")
_Dfl260eSmtpAlgName_Type = DisplayString
_Dfl260eSmtpAlgName_Object = MibTableColumn
dfl260eSmtpAlgName = _Dfl260eSmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1, 1, 2),
    _Dfl260eSmtpAlgName_Type()
)
dfl260eSmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgName.setStatus("current")
_Dfl260eSmtpAlgTotCheckedSes_Type = Gauge32
_Dfl260eSmtpAlgTotCheckedSes_Object = MibTableColumn
dfl260eSmtpAlgTotCheckedSes = _Dfl260eSmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1, 1, 3),
    _Dfl260eSmtpAlgTotCheckedSes_Type()
)
dfl260eSmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgTotCheckedSes.setStatus("current")
_Dfl260eSmtpAlgTotSpamSes_Type = Gauge32
_Dfl260eSmtpAlgTotSpamSes_Object = MibTableColumn
dfl260eSmtpAlgTotSpamSes = _Dfl260eSmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1, 1, 4),
    _Dfl260eSmtpAlgTotSpamSes_Type()
)
dfl260eSmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgTotSpamSes.setStatus("current")
_Dfl260eSmtpAlgTotDroppedSes_Type = Gauge32
_Dfl260eSmtpAlgTotDroppedSes_Object = MibTableColumn
dfl260eSmtpAlgTotDroppedSes = _Dfl260eSmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 1, 1, 5),
    _Dfl260eSmtpAlgTotDroppedSes_Type()
)
dfl260eSmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgTotDroppedSes.setStatus("current")
_Dfl260eSmtpAlgDnsBlTable_Object = MibTable
dfl260eSmtpAlgDnsBlTable = _Dfl260eSmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlTable.setStatus("current")
_Dfl260eSmtpAlgDnsBlEntry_Object = MibTableRow
dfl260eSmtpAlgDnsBlEntry = _Dfl260eSmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2, 1)
)
dfl260eSmtpAlgDnsBlEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eSmtpAlgIndex"),
    (0, "DFL260e-MIB", "dfl260eSmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlEntry.setStatus("current")


class _Dfl260eSmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type dfl260eSmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eSmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_Dfl260eSmtpAlgDnsBlIndex_Object = MibTableColumn
dfl260eSmtpAlgDnsBlIndex = _Dfl260eSmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2, 1, 1),
    _Dfl260eSmtpAlgDnsBlIndex_Type()
)
dfl260eSmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlIndex.setStatus("current")
_Dfl260eSmtpAlgDnsBlName_Type = DisplayString
_Dfl260eSmtpAlgDnsBlName_Object = MibTableColumn
dfl260eSmtpAlgDnsBlName = _Dfl260eSmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2, 1, 2),
    _Dfl260eSmtpAlgDnsBlName_Type()
)
dfl260eSmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlName.setStatus("current")
_Dfl260eSmtpAlgDnsBlChecked_Type = Gauge32
_Dfl260eSmtpAlgDnsBlChecked_Object = MibTableColumn
dfl260eSmtpAlgDnsBlChecked = _Dfl260eSmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2, 1, 3),
    _Dfl260eSmtpAlgDnsBlChecked_Type()
)
dfl260eSmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlChecked.setStatus("current")
_Dfl260eSmtpAlgDnsBlMatched_Type = Gauge32
_Dfl260eSmtpAlgDnsBlMatched_Object = MibTableColumn
dfl260eSmtpAlgDnsBlMatched = _Dfl260eSmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2, 1, 4),
    _Dfl260eSmtpAlgDnsBlMatched_Type()
)
dfl260eSmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlMatched.setStatus("current")
_Dfl260eSmtpAlgDnsBlFailChecks_Type = Gauge32
_Dfl260eSmtpAlgDnsBlFailChecks_Object = MibTableColumn
dfl260eSmtpAlgDnsBlFailChecks = _Dfl260eSmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 9, 5, 2, 1, 5),
    _Dfl260eSmtpAlgDnsBlFailChecks_Type()
)
dfl260eSmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eSmtpAlgDnsBlFailChecks.setStatus("current")
_Dfl260eDHCPRelay_ObjectIdentity = ObjectIdentity
dfl260eDHCPRelay = _Dfl260eDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11)
)
_Dfl260eDHCPRelayCurClients_Type = Gauge32
_Dfl260eDHCPRelayCurClients_Object = MibScalar
dfl260eDHCPRelayCurClients = _Dfl260eDHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 1),
    _Dfl260eDHCPRelayCurClients_Type()
)
dfl260eDHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayCurClients.setStatus("current")
_Dfl260eDHCPRelayCurTrans_Type = Gauge32
_Dfl260eDHCPRelayCurTrans_Object = MibScalar
dfl260eDHCPRelayCurTrans = _Dfl260eDHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 2),
    _Dfl260eDHCPRelayCurTrans_Type()
)
dfl260eDHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayCurTrans.setStatus("current")
_Dfl260eDHCPRelayRejected_Type = Gauge32
_Dfl260eDHCPRelayRejected_Object = MibScalar
dfl260eDHCPRelayRejected = _Dfl260eDHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 3),
    _Dfl260eDHCPRelayRejected_Type()
)
dfl260eDHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRejected.setStatus("current")
_Dfl260eDHCPRelayRuleTable_Object = MibTable
dfl260eDHCPRelayRuleTable = _Dfl260eDHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleTable.setStatus("current")
_Dfl260eDHCPRelayRuleEntry_Object = MibTableRow
dfl260eDHCPRelayRuleEntry = _Dfl260eDHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1)
)
dfl260eDHCPRelayRuleEntry.setIndexNames(
    (0, "DFL260e-MIB", "dfl260eDHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleEntry.setStatus("current")


class _Dfl260eDHCPRelayRuleIndex_Type(Integer32):
    """Custom type dfl260eDHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dfl260eDHCPRelayRuleIndex_Type.__name__ = "Integer32"
_Dfl260eDHCPRelayRuleIndex_Object = MibTableColumn
dfl260eDHCPRelayRuleIndex = _Dfl260eDHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1, 1),
    _Dfl260eDHCPRelayRuleIndex_Type()
)
dfl260eDHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleIndex.setStatus("current")
_Dfl260eDHCPRelayRuleName_Type = DisplayString
_Dfl260eDHCPRelayRuleName_Object = MibTableColumn
dfl260eDHCPRelayRuleName = _Dfl260eDHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1, 2),
    _Dfl260eDHCPRelayRuleName_Type()
)
dfl260eDHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleName.setStatus("current")
_Dfl260eDHCPRelayRuleHits_Type = Gauge32
_Dfl260eDHCPRelayRuleHits_Object = MibTableColumn
dfl260eDHCPRelayRuleHits = _Dfl260eDHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1, 3),
    _Dfl260eDHCPRelayRuleHits_Type()
)
dfl260eDHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleHits.setStatus("current")
_Dfl260eDHCPRelayRuleCurClients_Type = Gauge32
_Dfl260eDHCPRelayRuleCurClients_Object = MibTableColumn
dfl260eDHCPRelayRuleCurClients = _Dfl260eDHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1, 4),
    _Dfl260eDHCPRelayRuleCurClients_Type()
)
dfl260eDHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleCurClients.setStatus("current")
_Dfl260eDHCPRelayRuleRejCliPkts_Type = Gauge32
_Dfl260eDHCPRelayRuleRejCliPkts_Object = MibTableColumn
dfl260eDHCPRelayRuleRejCliPkts = _Dfl260eDHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1, 5),
    _Dfl260eDHCPRelayRuleRejCliPkts_Type()
)
dfl260eDHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleRejCliPkts.setStatus("current")
_Dfl260eDHCPRelayRuleRejSrvPkts_Type = Gauge32
_Dfl260eDHCPRelayRuleRejSrvPkts_Object = MibTableColumn
dfl260eDHCPRelayRuleRejSrvPkts = _Dfl260eDHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 11, 4, 1, 6),
    _Dfl260eDHCPRelayRuleRejSrvPkts_Type()
)
dfl260eDHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eDHCPRelayRuleRejSrvPkts.setStatus("current")
_Dfl260eHA_ObjectIdentity = ObjectIdentity
dfl260eHA = _Dfl260eHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 12)
)
_Dfl260eHASyncSendQueueLength_Type = Gauge32
_Dfl260eHASyncSendQueueLength_Object = MibScalar
dfl260eHASyncSendQueueLength = _Dfl260eHASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 12, 1),
    _Dfl260eHASyncSendQueueLength_Type()
)
dfl260eHASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHASyncSendQueueLength.setStatus("current")
_Dfl260eHASyncSendQueueUsagePkt_Type = Gauge32
_Dfl260eHASyncSendQueueUsagePkt_Object = MibScalar
dfl260eHASyncSendQueueUsagePkt = _Dfl260eHASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 12, 2),
    _Dfl260eHASyncSendQueueUsagePkt_Type()
)
dfl260eHASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHASyncSendQueueUsagePkt.setStatus("current")
_Dfl260eHASyncSendQueueUsageOct_Type = Gauge32
_Dfl260eHASyncSendQueueUsageOct_Object = MibScalar
dfl260eHASyncSendQueueUsageOct = _Dfl260eHASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 12, 3),
    _Dfl260eHASyncSendQueueUsageOct_Type()
)
dfl260eHASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHASyncSendQueueUsageOct.setStatus("current")
_Dfl260eHASyncSentPackets_Type = Counter32
_Dfl260eHASyncSentPackets_Object = MibScalar
dfl260eHASyncSentPackets = _Dfl260eHASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 12, 4),
    _Dfl260eHASyncSentPackets_Type()
)
dfl260eHASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHASyncSentPackets.setStatus("current")
_Dfl260eHASyncSendResentPackets_Type = Counter32
_Dfl260eHASyncSendResentPackets_Object = MibScalar
dfl260eHASyncSendResentPackets = _Dfl260eHASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 1, 2, 12, 5),
    _Dfl260eHASyncSendResentPackets_Type()
)
dfl260eHASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfl260eHASyncSendResentPackets.setStatus("current")
_Dfl260ereg_ObjectIdentity = ObjectIdentity
dfl260ereg = _Dfl260ereg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2)
)
_Dfl260eMibModules_ObjectIdentity = ObjectIdentity
dfl260eMibModules = _Dfl260eMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 1)
)
_Dfl260eMibConfs_ObjectIdentity = ObjectIdentity
dfl260eMibConfs = _Dfl260eMibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 2)
)
_Dfl260eStatsConformance_ObjectIdentity = ObjectIdentity
dfl260eStatsConformance = _Dfl260eStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 2, 1)
)
_Dfl260eMibObjectGroups_ObjectIdentity = ObjectIdentity
dfl260eMibObjectGroups = _Dfl260eMibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3)
)
_Dfl260eStatsRegGroups_ObjectIdentity = ObjectIdentity
dfl260eStatsRegGroups = _Dfl260eStatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1)
)

# Managed Objects groups

dfl260eSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 1)
)
dfl260eSystemObjectGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eSysCpuLoad"),
        ("DFL260e-MIB", "dfl260eSysForwardedBits"),
        ("DFL260e-MIB", "dfl260eSysForwardedPackets"),
        ("DFL260e-MIB", "dfl260eSysBuffUse"),
        ("DFL260e-MIB", "dfl260eSysConns"),
        ("DFL260e-MIB", "dfl260eHWSensorName"),
        ("DFL260e-MIB", "dfl260eHWSensorValue"),
        ("DFL260e-MIB", "dfl260eHWSensorUnit"),
        ("DFL260e-MIB", "dfl260eSysMemUsage"),
        ("DFL260e-MIB", "dfl260eSysTimerUsage"),
        ("DFL260e-MIB", "dfl260eSysConnOPS"),
        ("DFL260e-MIB", "dfl260eSysConnCPS"),
        ("DFL260e-MIB", "dfl260eSysHCForwardedBits"))
)
if mibBuilder.loadTexts:
    dfl260eSystemObjectGroup.setStatus("current")

dfl260eIPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 2)
)
dfl260eIPsecObjectGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eIPsecPhaseOneActive"),
        ("DFL260e-MIB", "dfl260eIPsecPhaseOneAggrModeDone"),
        ("DFL260e-MIB", "dfl260eIPsecQuickModeActive"),
        ("DFL260e-MIB", "dfl260eIPsecPhaseOneDone"),
        ("DFL260e-MIB", "dfl260eIPsecPhaseOneFailed"),
        ("DFL260e-MIB", "dfl260eIPsecPhaseOneRekeyed"),
        ("DFL260e-MIB", "dfl260eIPsecQuickModeDone"),
        ("DFL260e-MIB", "dfl260eIPsecQuickModeFailed"),
        ("DFL260e-MIB", "dfl260eIPsecInfoDone"),
        ("DFL260e-MIB", "dfl260eIPsecInfoFailed"),
        ("DFL260e-MIB", "dfl260eIPsecInOctetsComp"),
        ("DFL260e-MIB", "dfl260eIPsecInOctetsUncomp"),
        ("DFL260e-MIB", "dfl260eIPsecOutOctetsComp"),
        ("DFL260e-MIB", "dfl260eIPsecOutOctetsUncomp"),
        ("DFL260e-MIB", "dfl260eIPsecForwardedOctetsComp"),
        ("DFL260e-MIB", "dfl260eIPsecForwardedOctetsUcomp"),
        ("DFL260e-MIB", "dfl260eIPsecInPackets"),
        ("DFL260e-MIB", "dfl260eIPsecOutPackets"),
        ("DFL260e-MIB", "dfl260eIPsecForwardedPackets"),
        ("DFL260e-MIB", "dfl260eIPsecActiveTransforms"),
        ("DFL260e-MIB", "dfl260eIPsecTotalTransforms"),
        ("DFL260e-MIB", "dfl260eIPsecOutOfTransforms"),
        ("DFL260e-MIB", "dfl260eIPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    dfl260eIPsecObjectGroup.setStatus("current")

dfl260eStateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 3)
)
dfl260eStateCountersGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eSysPscTcpSyn"),
        ("DFL260e-MIB", "dfl260eSysPscTcpOpen"),
        ("DFL260e-MIB", "dfl260eSysPscTcpFin"),
        ("DFL260e-MIB", "dfl260eSysPscUdp"),
        ("DFL260e-MIB", "dfl260eSysPscIcmp"),
        ("DFL260e-MIB", "dfl260eSysPscOther"))
)
if mibBuilder.loadTexts:
    dfl260eStateCountersGroup.setStatus("current")

dfl260eIPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 4)
)
dfl260eIPPoolGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eIPPoolsNumber"),
        ("DFL260e-MIB", "dfl260eIPPoolName"),
        ("DFL260e-MIB", "dfl260eIPPoolPrepare"),
        ("DFL260e-MIB", "dfl260eIPPoolFree"),
        ("DFL260e-MIB", "dfl260eIPPoolMisses"),
        ("DFL260e-MIB", "dfl260eIPPoolClientFails"),
        ("DFL260e-MIB", "dfl260eIPPoolUsed"))
)
if mibBuilder.loadTexts:
    dfl260eIPPoolGroup.setStatus("current")

dfl260eDHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 5)
)
dfl260eDHCPServerGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eDHCPTotalRejected"),
        ("DFL260e-MIB", "dfl260eDHCPRuleName"),
        ("DFL260e-MIB", "dfl260eDHCPRuleUsage"),
        ("DFL260e-MIB", "dfl260eDHCPRuleUsagePercent"),
        ("DFL260e-MIB", "dfl260eDHCPActiveClients"),
        ("DFL260e-MIB", "dfl260eDHCPActiveClientsPercent"),
        ("DFL260e-MIB", "dfl260eDHCPRejectedRequests"),
        ("DFL260e-MIB", "dfl260eDHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    dfl260eDHCPServerGroup.setStatus("current")

dfl260eRuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 6)
)
dfl260eRuleUseGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eRuleName"),
        ("DFL260e-MIB", "dfl260eRuleUse"))
)
if mibBuilder.loadTexts:
    dfl260eRuleUseGroup.setStatus("current")

dfl260eUserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 7)
)
dfl260eUserAuthGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eUserAuthHTTPUsers"),
        ("DFL260e-MIB", "dfl260eUserAuthXAUTHUsers"),
        ("DFL260e-MIB", "dfl260eUserAuthHTTPSUsers"),
        ("DFL260e-MIB", "dfl260eUserAuthPPPUsers"),
        ("DFL260e-MIB", "dfl260eUserAuthEAPUsers"),
        ("DFL260e-MIB", "dfl260eUserAuthRuleName"),
        ("DFL260e-MIB", "dfl260eUserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    dfl260eUserAuthGroup.setStatus("current")

dfl260eIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 8)
)
dfl260eIfStatsGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eIfName"),
        ("DFL260e-MIB", "dfl260eIfFragsIn"),
        ("DFL260e-MIB", "dfl260eIfFragReassOk"),
        ("DFL260e-MIB", "dfl260eIfFragReassFail"),
        ("DFL260e-MIB", "dfl260eIfPktsInCnt"),
        ("DFL260e-MIB", "dfl260eIfPktsOutCnt"),
        ("DFL260e-MIB", "dfl260eIfBitsInCnt"),
        ("DFL260e-MIB", "dfl260eIfBitsOutCnt"),
        ("DFL260e-MIB", "dfl260eIfPktsTotCnt"),
        ("DFL260e-MIB", "dfl260eIfBitsTotCnt"),
        ("DFL260e-MIB", "dfl260eIfHCPktsInCnt"),
        ("DFL260e-MIB", "dfl260eIfHCPktsOutCnt"),
        ("DFL260e-MIB", "dfl260eIfHCBitsInCnt"),
        ("DFL260e-MIB", "dfl260eIfHCBitsOutCnt"),
        ("DFL260e-MIB", "dfl260eIfHCPktsTotCnt"),
        ("DFL260e-MIB", "dfl260eIfHCBitsTotCnt"),
        ("DFL260e-MIB", "dfl260eIfRxRingFifoErrors"),
        ("DFL260e-MIB", "dfl260eIfRxDespools"),
        ("DFL260e-MIB", "dfl260eIfRxAvgUse"),
        ("DFL260e-MIB", "dfl260eIfRxRingSaturation"),
        ("DFL260e-MIB", "dfl260eRxRingFlooded"),
        ("DFL260e-MIB", "dfl260eIfTxDespools"),
        ("DFL260e-MIB", "dfl260eIfTxAvgUse"),
        ("DFL260e-MIB", "dfl260eIfTxRingSaturation"),
        ("DFL260e-MIB", "dfl260eRxTingFlooded"))
)
if mibBuilder.loadTexts:
    dfl260eIfStatsGroup.setStatus("current")

dfl260eLinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 9)
)
dfl260eLinkMonitorGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eLinkMonGrp"),
        ("DFL260e-MIB", "dfl260eLinkMonGrpName"),
        ("DFL260e-MIB", "dfl260eLinkMonGrpHostsUp"),
        ("DFL260e-MIB", "dfl260eLinkMonHostId"),
        ("DFL260e-MIB", "dfl260eLinkMonHostShortTermLoss"),
        ("DFL260e-MIB", "dfl260eLinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    dfl260eLinkMonitorGroup.setStatus("current")

dfl260ePipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 10)
)
dfl260ePipesObjectGroup.setObjects(
      *(("DFL260e-MIB", "dfl260ePipeUsers"),
        ("DFL260e-MIB", "dfl260ePipeName"),
        ("DFL260e-MIB", "dfl260ePipeMinPrec"),
        ("DFL260e-MIB", "dfl260ePipeMaxPrec"),
        ("DFL260e-MIB", "dfl260ePipeDefPrec"),
        ("DFL260e-MIB", "dfl260ePipeNumPrec"),
        ("DFL260e-MIB", "dfl260ePipeNumUsers"),
        ("DFL260e-MIB", "dfl260ePipeCurrentBps"),
        ("DFL260e-MIB", "dfl260ePipeCurrentPps"),
        ("DFL260e-MIB", "dfl260ePipeDelayedPackets"),
        ("DFL260e-MIB", "dfl260ePipeDropedPackets"),
        ("DFL260e-MIB", "dfl260ePipePrec"),
        ("DFL260e-MIB", "dfl260ePipePrecBps"),
        ("DFL260e-MIB", "dfl260ePipePrecTotalPps"),
        ("DFL260e-MIB", "dfl260ePipePrecReservedBps"),
        ("DFL260e-MIB", "dfl260ePipePrecDynLimBps"),
        ("DFL260e-MIB", "dfl260ePipePrecDynUsrLimBps"),
        ("DFL260e-MIB", "dfl260ePipePrecDelayedPackets"),
        ("DFL260e-MIB", "dfl260ePipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    dfl260ePipesObjectGroup.setStatus("current")

dfl260eDHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 12)
)
dfl260eDHCPRelayObjectGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eDHCPRelayCurClients"),
        ("DFL260e-MIB", "dfl260eDHCPRelayCurTrans"),
        ("DFL260e-MIB", "dfl260eDHCPRelayRejected"),
        ("DFL260e-MIB", "dfl260eDHCPRelayRuleName"),
        ("DFL260e-MIB", "dfl260eDHCPRelayRuleHits"),
        ("DFL260e-MIB", "dfl260eDHCPRelayRuleCurClients"),
        ("DFL260e-MIB", "dfl260eDHCPRelayRuleRejCliPkts"),
        ("DFL260e-MIB", "dfl260eDHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    dfl260eDHCPRelayObjectGroup.setStatus("current")

dfl260eAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 13)
)
dfl260eAlgGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eAlgSessions"),
        ("DFL260e-MIB", "dfl260eAlgConnections"),
        ("DFL260e-MIB", "dfl260eAlgTCPStreams"),
        ("DFL260e-MIB", "dfl260eHttpAlgName"),
        ("DFL260e-MIB", "dfl260eHttpAlgTotalRequested"),
        ("DFL260e-MIB", "dfl260eHttpAlgTotalAllowed"),
        ("DFL260e-MIB", "dfl260eHttpAlgTotalBlocked"),
        ("DFL260e-MIB", "dfl260eHttpAlgCntFltName"),
        ("DFL260e-MIB", "dfl260eHttpAlgCntFltRequests"),
        ("DFL260e-MIB", "dfl260eHttpAlgCntFltAllowed"),
        ("DFL260e-MIB", "dfl260eHttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    dfl260eAlgGroup.setStatus("current")

dfl260eHAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 14)
)
dfl260eHAGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eHASyncSendQueueLength"),
        ("DFL260e-MIB", "dfl260eHASyncSendQueueUsagePkt"),
        ("DFL260e-MIB", "dfl260eHASyncSendQueueUsageOct"),
        ("DFL260e-MIB", "dfl260eHASyncSentPackets"),
        ("DFL260e-MIB", "dfl260eHASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    dfl260eHAGroup.setStatus("current")

dfl260eIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 15)
)
dfl260eIfVlanGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eIfVlanUntaggedInPkts"),
        ("DFL260e-MIB", "dfl260eIfVlanUntaggedOutPkts"),
        ("DFL260e-MIB", "dfl260eIfVlanUntaggedTotPkts"),
        ("DFL260e-MIB", "dfl260eIfVlanUntaggedInOctets"),
        ("DFL260e-MIB", "dfl260eIfVlanUntaggedOutOctets"),
        ("DFL260e-MIB", "dfl260eIfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    dfl260eIfVlanGroup.setStatus("current")

dfl260eSmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 16)
)
dfl260eSmtpAlgGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eSmtpAlgName"),
        ("DFL260e-MIB", "dfl260eSmtpAlgTotCheckedSes"),
        ("DFL260e-MIB", "dfl260eSmtpAlgTotSpamSes"),
        ("DFL260e-MIB", "dfl260eSmtpAlgTotDroppedSes"),
        ("DFL260e-MIB", "dfl260eSmtpAlgDnsBlName"),
        ("DFL260e-MIB", "dfl260eSmtpAlgDnsBlChecked"),
        ("DFL260e-MIB", "dfl260eSmtpAlgDnsBlMatched"),
        ("DFL260e-MIB", "dfl260eSmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    dfl260eSmtpAlgGroup.setStatus("current")

dfl260eSysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 3, 1, 17)
)
dfl260eSysTCPGroup.setObjects(
      *(("DFL260e-MIB", "dfl260eSysTCPRecvSmall"),
        ("DFL260e-MIB", "dfl260eSysTCPRecvLarge"),
        ("DFL260e-MIB", "dfl260eSysTCPSendSmall"),
        ("DFL260e-MIB", "dfl260eSysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    dfl260eSysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dfl260eStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 20, 2, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dfl260eStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFL260e-MIB",
    **{"dlink": dlink,
       "netdefendMgmt": netdefendMgmt,
       "utmFirewall": utmFirewall,
       "dfl260e": dfl260e,
       "dfl260eOS": dfl260eOS,
       "dfl260eOSStats": dfl260eOSStats,
       "dfl260eSystem": dfl260eSystem,
       "dfl260eSysCpuLoad": dfl260eSysCpuLoad,
       "dfl260eSysForwardedBits": dfl260eSysForwardedBits,
       "dfl260eSysForwardedPackets": dfl260eSysForwardedPackets,
       "dfl260eSysBuffUse": dfl260eSysBuffUse,
       "dfl260eSysConns": dfl260eSysConns,
       "dfl260eSysPerStateCounters": dfl260eSysPerStateCounters,
       "dfl260eSysPscTcpSyn": dfl260eSysPscTcpSyn,
       "dfl260eSysPscTcpOpen": dfl260eSysPscTcpOpen,
       "dfl260eSysPscTcpFin": dfl260eSysPscTcpFin,
       "dfl260eSysPscUdp": dfl260eSysPscUdp,
       "dfl260eSysPscIcmp": dfl260eSysPscIcmp,
       "dfl260eSysPscOther": dfl260eSysPscOther,
       "dfl260eIfStatsTable": dfl260eIfStatsTable,
       "dfl260eIfStatsEntry": dfl260eIfStatsEntry,
       "dfl260eIfStatsIndex": dfl260eIfStatsIndex,
       "dfl260eIfName": dfl260eIfName,
       "dfl260eIfFragsIn": dfl260eIfFragsIn,
       "dfl260eIfFragReassOk": dfl260eIfFragReassOk,
       "dfl260eIfFragReassFail": dfl260eIfFragReassFail,
       "dfl260eIfPktsInCnt": dfl260eIfPktsInCnt,
       "dfl260eIfPktsOutCnt": dfl260eIfPktsOutCnt,
       "dfl260eIfBitsInCnt": dfl260eIfBitsInCnt,
       "dfl260eIfBitsOutCnt": dfl260eIfBitsOutCnt,
       "dfl260eIfPktsTotCnt": dfl260eIfPktsTotCnt,
       "dfl260eIfBitsTotCnt": dfl260eIfBitsTotCnt,
       "dfl260eIfHCPktsInCnt": dfl260eIfHCPktsInCnt,
       "dfl260eIfHCPktsOutCnt": dfl260eIfHCPktsOutCnt,
       "dfl260eIfHCBitsInCnt": dfl260eIfHCBitsInCnt,
       "dfl260eIfHCBitsOutCnt": dfl260eIfHCBitsOutCnt,
       "dfl260eIfHCPktsTotCnt": dfl260eIfHCPktsTotCnt,
       "dfl260eIfHCBitsTotCnt": dfl260eIfHCBitsTotCnt,
       "dfl260eIfRxRingTable": dfl260eIfRxRingTable,
       "dfl260eIfRxRingEntry": dfl260eIfRxRingEntry,
       "dfl260eIfRxRingIndex": dfl260eIfRxRingIndex,
       "dfl260eIfRxRingFifoErrors": dfl260eIfRxRingFifoErrors,
       "dfl260eIfRxDespools": dfl260eIfRxDespools,
       "dfl260eIfRxAvgUse": dfl260eIfRxAvgUse,
       "dfl260eIfRxRingSaturation": dfl260eIfRxRingSaturation,
       "dfl260eRxRingFlooded": dfl260eRxRingFlooded,
       "dfl260eIfTxRingTable": dfl260eIfTxRingTable,
       "dfl260eIfTxRingEntry": dfl260eIfTxRingEntry,
       "dfl260eIfTxRingIndex": dfl260eIfTxRingIndex,
       "dfl260eIfTxDespools": dfl260eIfTxDespools,
       "dfl260eIfTxAvgUse": dfl260eIfTxAvgUse,
       "dfl260eIfTxRingSaturation": dfl260eIfTxRingSaturation,
       "dfl260eRxTingFlooded": dfl260eRxTingFlooded,
       "dfl260eIfVlanStatsTable": dfl260eIfVlanStatsTable,
       "dfl260eIfVlanStatsEntry": dfl260eIfVlanStatsEntry,
       "dfl260eIfVlanIndex": dfl260eIfVlanIndex,
       "dfl260eIfVlanUntaggedInPkts": dfl260eIfVlanUntaggedInPkts,
       "dfl260eIfVlanUntaggedOutPkts": dfl260eIfVlanUntaggedOutPkts,
       "dfl260eIfVlanUntaggedTotPkts": dfl260eIfVlanUntaggedTotPkts,
       "dfl260eIfVlanUntaggedInOctets": dfl260eIfVlanUntaggedInOctets,
       "dfl260eIfVlanUntaggedOutOctets": dfl260eIfVlanUntaggedOutOctets,
       "dfl260eIfVlanUntaggedTotOctets": dfl260eIfVlanUntaggedTotOctets,
       "dfl260eHWSensorTable": dfl260eHWSensorTable,
       "dfl260eHWSensorEntry": dfl260eHWSensorEntry,
       "dfl260eHWSensorIndex": dfl260eHWSensorIndex,
       "dfl260eHWSensorName": dfl260eHWSensorName,
       "dfl260eHWSensorValue": dfl260eHWSensorValue,
       "dfl260eHWSensorUnit": dfl260eHWSensorUnit,
       "dfl260eSysMemUsage": dfl260eSysMemUsage,
       "dfl260eSysTCPUsage": dfl260eSysTCPUsage,
       "dfl260eSysTCPRecvSmall": dfl260eSysTCPRecvSmall,
       "dfl260eSysTCPRecvLarge": dfl260eSysTCPRecvLarge,
       "dfl260eSysTCPSendSmall": dfl260eSysTCPSendSmall,
       "dfl260eSysTCPSendLarge": dfl260eSysTCPSendLarge,
       "dfl260eSysTimerUsage": dfl260eSysTimerUsage,
       "dfl260eSysConnOPS": dfl260eSysConnOPS,
       "dfl260eSysConnCPS": dfl260eSysConnCPS,
       "dfl260eSysHCForwardedBits": dfl260eSysHCForwardedBits,
       "dfl260eVPN": dfl260eVPN,
       "dfl260eIPsec": dfl260eIPsec,
       "dfl260eIPsecGlobal": dfl260eIPsecGlobal,
       "dfl260eIPsecPhaseOneActive": dfl260eIPsecPhaseOneActive,
       "dfl260eIPsecPhaseOneAggrModeDone": dfl260eIPsecPhaseOneAggrModeDone,
       "dfl260eIPsecQuickModeActive": dfl260eIPsecQuickModeActive,
       "dfl260eIPsecPhaseOneDone": dfl260eIPsecPhaseOneDone,
       "dfl260eIPsecPhaseOneFailed": dfl260eIPsecPhaseOneFailed,
       "dfl260eIPsecPhaseOneRekeyed": dfl260eIPsecPhaseOneRekeyed,
       "dfl260eIPsecQuickModeDone": dfl260eIPsecQuickModeDone,
       "dfl260eIPsecQuickModeFailed": dfl260eIPsecQuickModeFailed,
       "dfl260eIPsecInfoDone": dfl260eIPsecInfoDone,
       "dfl260eIPsecInfoFailed": dfl260eIPsecInfoFailed,
       "dfl260eIPsecInOctetsComp": dfl260eIPsecInOctetsComp,
       "dfl260eIPsecInOctetsUncomp": dfl260eIPsecInOctetsUncomp,
       "dfl260eIPsecOutOctetsComp": dfl260eIPsecOutOctetsComp,
       "dfl260eIPsecOutOctetsUncomp": dfl260eIPsecOutOctetsUncomp,
       "dfl260eIPsecForwardedOctetsComp": dfl260eIPsecForwardedOctetsComp,
       "dfl260eIPsecForwardedOctetsUcomp": dfl260eIPsecForwardedOctetsUcomp,
       "dfl260eIPsecInPackets": dfl260eIPsecInPackets,
       "dfl260eIPsecOutPackets": dfl260eIPsecOutPackets,
       "dfl260eIPsecForwardedPackets": dfl260eIPsecForwardedPackets,
       "dfl260eIPsecActiveTransforms": dfl260eIPsecActiveTransforms,
       "dfl260eIPsecTotalTransforms": dfl260eIPsecTotalTransforms,
       "dfl260eIPsecOutOfTransforms": dfl260eIPsecOutOfTransforms,
       "dfl260eIPsecTotalRekeys": dfl260eIPsecTotalRekeys,
       "dfl260eRules": dfl260eRules,
       "dfl260eRuleUseTable": dfl260eRuleUseTable,
       "dfl260eRuleUseEntry": dfl260eRuleUseEntry,
       "dfl260eRuleIndex": dfl260eRuleIndex,
       "dfl260eRuleName": dfl260eRuleName,
       "dfl260eRuleUse": dfl260eRuleUse,
       "dfl260eIPPools": dfl260eIPPools,
       "dfl260eIPPoolsNumber": dfl260eIPPoolsNumber,
       "dfl260eIPPoolTable": dfl260eIPPoolTable,
       "dfl260eIPPoolEntry": dfl260eIPPoolEntry,
       "dfl260eIPPoolIndex": dfl260eIPPoolIndex,
       "dfl260eIPPoolName": dfl260eIPPoolName,
       "dfl260eIPPoolPrepare": dfl260eIPPoolPrepare,
       "dfl260eIPPoolFree": dfl260eIPPoolFree,
       "dfl260eIPPoolMisses": dfl260eIPPoolMisses,
       "dfl260eIPPoolClientFails": dfl260eIPPoolClientFails,
       "dfl260eIPPoolUsed": dfl260eIPPoolUsed,
       "dfl260eDHCPServer": dfl260eDHCPServer,
       "dfl260eDHCPTotalRejected": dfl260eDHCPTotalRejected,
       "dfl260eDHCPRuleTable": dfl260eDHCPRuleTable,
       "dfl260eDHCPRuleEntry": dfl260eDHCPRuleEntry,
       "dfl260eDHCPRuleIndex": dfl260eDHCPRuleIndex,
       "dfl260eDHCPRuleName": dfl260eDHCPRuleName,
       "dfl260eDHCPRuleUsage": dfl260eDHCPRuleUsage,
       "dfl260eDHCPRuleUsagePercent": dfl260eDHCPRuleUsagePercent,
       "dfl260eDHCPActiveClients": dfl260eDHCPActiveClients,
       "dfl260eDHCPActiveClientsPercent": dfl260eDHCPActiveClientsPercent,
       "dfl260eDHCPRejectedRequests": dfl260eDHCPRejectedRequests,
       "dfl260eDHCPTotalLeases": dfl260eDHCPTotalLeases,
       "dfl260eUserAuth": dfl260eUserAuth,
       "dfl260eUserAuthHTTPUsers": dfl260eUserAuthHTTPUsers,
       "dfl260eUserAuthXAUTHUsers": dfl260eUserAuthXAUTHUsers,
       "dfl260eUserAuthHTTPSUsers": dfl260eUserAuthHTTPSUsers,
       "dfl260eUserAuthPPPUsers": dfl260eUserAuthPPPUsers,
       "dfl260eUserAuthEAPUsers": dfl260eUserAuthEAPUsers,
       "dfl260eUserAuthRuleUseTable": dfl260eUserAuthRuleUseTable,
       "dfl260eUserAuthRuleUseEntry": dfl260eUserAuthRuleUseEntry,
       "dfl260eUserAuthRuleIndex": dfl260eUserAuthRuleIndex,
       "dfl260eUserAuthRuleName": dfl260eUserAuthRuleName,
       "dfl260eUserAuthRuleUse": dfl260eUserAuthRuleUse,
       "dfl260eLinkMonitor": dfl260eLinkMonitor,
       "dfl260eLinkMonGrp": dfl260eLinkMonGrp,
       "dfl260eLinkMonGrpTable": dfl260eLinkMonGrpTable,
       "dfl260eLinkMonGrpEntry": dfl260eLinkMonGrpEntry,
       "dfl260eLinkMonGrpIndex": dfl260eLinkMonGrpIndex,
       "dfl260eLinkMonGrpName": dfl260eLinkMonGrpName,
       "dfl260eLinkMonGrpHostsUp": dfl260eLinkMonGrpHostsUp,
       "dfl260eLinkMonHostTable": dfl260eLinkMonHostTable,
       "dfl260eLinkMonHostEntry": dfl260eLinkMonHostEntry,
       "dfl260eLinkMonHostIndex": dfl260eLinkMonHostIndex,
       "dfl260eLinkMonHostId": dfl260eLinkMonHostId,
       "dfl260eLinkMonHostShortTermLoss": dfl260eLinkMonHostShortTermLoss,
       "dfl260eLinkMonHostPacketsLost": dfl260eLinkMonHostPacketsLost,
       "dfl260ePipes": dfl260ePipes,
       "dfl260ePipeUsers": dfl260ePipeUsers,
       "dfl260ePipeTable": dfl260ePipeTable,
       "dfl260ePipeEntry": dfl260ePipeEntry,
       "dfl260ePipeIndex": dfl260ePipeIndex,
       "dfl260ePipeName": dfl260ePipeName,
       "dfl260ePipeMinPrec": dfl260ePipeMinPrec,
       "dfl260ePipeMaxPrec": dfl260ePipeMaxPrec,
       "dfl260ePipeDefPrec": dfl260ePipeDefPrec,
       "dfl260ePipeNumPrec": dfl260ePipeNumPrec,
       "dfl260ePipeNumUsers": dfl260ePipeNumUsers,
       "dfl260ePipeCurrentBps": dfl260ePipeCurrentBps,
       "dfl260ePipeCurrentPps": dfl260ePipeCurrentPps,
       "dfl260ePipeDelayedPackets": dfl260ePipeDelayedPackets,
       "dfl260ePipeDropedPackets": dfl260ePipeDropedPackets,
       "dfl260ePipePrecTable": dfl260ePipePrecTable,
       "dfl260ePipePrecEntry": dfl260ePipePrecEntry,
       "dfl260ePipePrecIndex": dfl260ePipePrecIndex,
       "dfl260ePipePrec": dfl260ePipePrec,
       "dfl260ePipePrecBps": dfl260ePipePrecBps,
       "dfl260ePipePrecTotalPps": dfl260ePipePrecTotalPps,
       "dfl260ePipePrecReservedBps": dfl260ePipePrecReservedBps,
       "dfl260ePipePrecDynLimBps": dfl260ePipePrecDynLimBps,
       "dfl260ePipePrecDynUsrLimBps": dfl260ePipePrecDynUsrLimBps,
       "dfl260ePipePrecDelayedPackets": dfl260ePipePrecDelayedPackets,
       "dfl260ePipePrecDropedPackets": dfl260ePipePrecDropedPackets,
       "dfl260eALG": dfl260eALG,
       "dfl260eAlgSessions": dfl260eAlgSessions,
       "dfl260eAlgConnections": dfl260eAlgConnections,
       "dfl260eAlgTCPStreams": dfl260eAlgTCPStreams,
       "dfl260eHttpAlg": dfl260eHttpAlg,
       "dfl260eHttpAlgTable": dfl260eHttpAlgTable,
       "dfl260eHttpAlgEntry": dfl260eHttpAlgEntry,
       "dfl260eHttpAlgIndex": dfl260eHttpAlgIndex,
       "dfl260eHttpAlgName": dfl260eHttpAlgName,
       "dfl260eHttpAlgTotalRequested": dfl260eHttpAlgTotalRequested,
       "dfl260eHttpAlgTotalAllowed": dfl260eHttpAlgTotalAllowed,
       "dfl260eHttpAlgTotalBlocked": dfl260eHttpAlgTotalBlocked,
       "dfl260eHttpAlgCntFltTable": dfl260eHttpAlgCntFltTable,
       "dfl260eHttpAlgCntFltEntry": dfl260eHttpAlgCntFltEntry,
       "dfl260eHttpAlgCntFltIndex": dfl260eHttpAlgCntFltIndex,
       "dfl260eHttpAlgCntFltName": dfl260eHttpAlgCntFltName,
       "dfl260eHttpAlgCntFltRequests": dfl260eHttpAlgCntFltRequests,
       "dfl260eHttpAlgCntFltAllowed": dfl260eHttpAlgCntFltAllowed,
       "dfl260eHttpAlgCntFltBlocked": dfl260eHttpAlgCntFltBlocked,
       "dfl260eSmtpAlg": dfl260eSmtpAlg,
       "dfl260eSmtpAlgTable": dfl260eSmtpAlgTable,
       "dfl260eSmtpAlgEntry": dfl260eSmtpAlgEntry,
       "dfl260eSmtpAlgIndex": dfl260eSmtpAlgIndex,
       "dfl260eSmtpAlgName": dfl260eSmtpAlgName,
       "dfl260eSmtpAlgTotCheckedSes": dfl260eSmtpAlgTotCheckedSes,
       "dfl260eSmtpAlgTotSpamSes": dfl260eSmtpAlgTotSpamSes,
       "dfl260eSmtpAlgTotDroppedSes": dfl260eSmtpAlgTotDroppedSes,
       "dfl260eSmtpAlgDnsBlTable": dfl260eSmtpAlgDnsBlTable,
       "dfl260eSmtpAlgDnsBlEntry": dfl260eSmtpAlgDnsBlEntry,
       "dfl260eSmtpAlgDnsBlIndex": dfl260eSmtpAlgDnsBlIndex,
       "dfl260eSmtpAlgDnsBlName": dfl260eSmtpAlgDnsBlName,
       "dfl260eSmtpAlgDnsBlChecked": dfl260eSmtpAlgDnsBlChecked,
       "dfl260eSmtpAlgDnsBlMatched": dfl260eSmtpAlgDnsBlMatched,
       "dfl260eSmtpAlgDnsBlFailChecks": dfl260eSmtpAlgDnsBlFailChecks,
       "dfl260eDHCPRelay": dfl260eDHCPRelay,
       "dfl260eDHCPRelayCurClients": dfl260eDHCPRelayCurClients,
       "dfl260eDHCPRelayCurTrans": dfl260eDHCPRelayCurTrans,
       "dfl260eDHCPRelayRejected": dfl260eDHCPRelayRejected,
       "dfl260eDHCPRelayRuleTable": dfl260eDHCPRelayRuleTable,
       "dfl260eDHCPRelayRuleEntry": dfl260eDHCPRelayRuleEntry,
       "dfl260eDHCPRelayRuleIndex": dfl260eDHCPRelayRuleIndex,
       "dfl260eDHCPRelayRuleName": dfl260eDHCPRelayRuleName,
       "dfl260eDHCPRelayRuleHits": dfl260eDHCPRelayRuleHits,
       "dfl260eDHCPRelayRuleCurClients": dfl260eDHCPRelayRuleCurClients,
       "dfl260eDHCPRelayRuleRejCliPkts": dfl260eDHCPRelayRuleRejCliPkts,
       "dfl260eDHCPRelayRuleRejSrvPkts": dfl260eDHCPRelayRuleRejSrvPkts,
       "dfl260eHA": dfl260eHA,
       "dfl260eHASyncSendQueueLength": dfl260eHASyncSendQueueLength,
       "dfl260eHASyncSendQueueUsagePkt": dfl260eHASyncSendQueueUsagePkt,
       "dfl260eHASyncSendQueueUsageOct": dfl260eHASyncSendQueueUsageOct,
       "dfl260eHASyncSentPackets": dfl260eHASyncSentPackets,
       "dfl260eHASyncSendResentPackets": dfl260eHASyncSendResentPackets,
       "dfl260ereg": dfl260ereg,
       "dfl260eMibModules": dfl260eMibModules,
       "dfl260e-MIB": dfl260e_MIB,
       "dfl260eMibConfs": dfl260eMibConfs,
       "dfl260eStatsConformance": dfl260eStatsConformance,
       "dfl260eStatsCompliance": dfl260eStatsCompliance,
       "dfl260eMibObjectGroups": dfl260eMibObjectGroups,
       "dfl260eStatsRegGroups": dfl260eStatsRegGroups,
       "dfl260eSystemObjectGroup": dfl260eSystemObjectGroup,
       "dfl260eIPsecObjectGroup": dfl260eIPsecObjectGroup,
       "dfl260eStateCountersGroup": dfl260eStateCountersGroup,
       "dfl260eIPPoolGroup": dfl260eIPPoolGroup,
       "dfl260eDHCPServerGroup": dfl260eDHCPServerGroup,
       "dfl260eRuleUseGroup": dfl260eRuleUseGroup,
       "dfl260eUserAuthGroup": dfl260eUserAuthGroup,
       "dfl260eIfStatsGroup": dfl260eIfStatsGroup,
       "dfl260eLinkMonitorGroup": dfl260eLinkMonitorGroup,
       "dfl260ePipesObjectGroup": dfl260ePipesObjectGroup,
       "dfl260eDHCPRelayObjectGroup": dfl260eDHCPRelayObjectGroup,
       "dfl260eAlgGroup": dfl260eAlgGroup,
       "dfl260eHAGroup": dfl260eHAGroup,
       "dfl260eIfVlanGroup": dfl260eIfVlanGroup,
       "dfl260eSmtpAlgGroup": dfl260eSmtpAlgGroup,
       "dfl260eSysTCPGroup": dfl260eSysTCPGroup}
)
