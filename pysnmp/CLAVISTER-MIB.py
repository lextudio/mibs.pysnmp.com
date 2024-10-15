# SNMP MIB module (CLAVISTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAVISTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:43 2024
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

(clavisterMibConfs,
 clavisterMibModules,
 clavisterMibObjectGroups,
 clavisterOSStats) = mibBuilder.importSymbols(
    "CLAVISTER-SMI",
    "clavisterMibConfs",
    "clavisterMibModules",
    "clavisterMibObjectGroups",
    "clavisterOSStats")

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

clavisterStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 1, 1)
)
clavisterStatsMibModule.setRevisions(
        ("2008-11-18 16:05",
         "2008-10-14 12:27",
         "2008-03-06 10:18",
         "2007-08-16 10:19",
         "2007-05-28 08:00",
         "2007-02-13 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClvSystem_ObjectIdentity = ObjectIdentity
clvSystem = _ClvSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1)
)
_ClvSysCpuLoad_Type = Gauge32
_ClvSysCpuLoad_Object = MibScalar
clvSysCpuLoad = _ClvSysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 1),
    _ClvSysCpuLoad_Type()
)
clvSysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysCpuLoad.setStatus("current")
_ClvSysForwardedBits_Type = Counter32
_ClvSysForwardedBits_Object = MibScalar
clvSysForwardedBits = _ClvSysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 2),
    _ClvSysForwardedBits_Type()
)
clvSysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysForwardedBits.setStatus("current")
_ClvSysForwardedPackets_Type = Counter32
_ClvSysForwardedPackets_Object = MibScalar
clvSysForwardedPackets = _ClvSysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 3),
    _ClvSysForwardedPackets_Type()
)
clvSysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysForwardedPackets.setStatus("current")
_ClvSysBuffUse_Type = Gauge32
_ClvSysBuffUse_Object = MibScalar
clvSysBuffUse = _ClvSysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 4),
    _ClvSysBuffUse_Type()
)
clvSysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysBuffUse.setStatus("current")
_ClvSysConns_Type = Gauge32
_ClvSysConns_Object = MibScalar
clvSysConns = _ClvSysConns_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 5),
    _ClvSysConns_Type()
)
clvSysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysConns.setStatus("current")
_ClvSysPerStateCounters_ObjectIdentity = ObjectIdentity
clvSysPerStateCounters = _ClvSysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6)
)
_ClvSysPscTcpSyn_Type = Gauge32
_ClvSysPscTcpSyn_Object = MibScalar
clvSysPscTcpSyn = _ClvSysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 1),
    _ClvSysPscTcpSyn_Type()
)
clvSysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscTcpSyn.setStatus("current")
_ClvSysPscTcpOpen_Type = Gauge32
_ClvSysPscTcpOpen_Object = MibScalar
clvSysPscTcpOpen = _ClvSysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 2),
    _ClvSysPscTcpOpen_Type()
)
clvSysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscTcpOpen.setStatus("current")
_ClvSysPscTcpFin_Type = Gauge32
_ClvSysPscTcpFin_Object = MibScalar
clvSysPscTcpFin = _ClvSysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 3),
    _ClvSysPscTcpFin_Type()
)
clvSysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscTcpFin.setStatus("current")
_ClvSysPscUdp_Type = Gauge32
_ClvSysPscUdp_Object = MibScalar
clvSysPscUdp = _ClvSysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 4),
    _ClvSysPscUdp_Type()
)
clvSysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscUdp.setStatus("current")
_ClvSysPscIcmp_Type = Gauge32
_ClvSysPscIcmp_Object = MibScalar
clvSysPscIcmp = _ClvSysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 5),
    _ClvSysPscIcmp_Type()
)
clvSysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscIcmp.setStatus("current")
_ClvSysPscOther_Type = Gauge32
_ClvSysPscOther_Object = MibScalar
clvSysPscOther = _ClvSysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 6),
    _ClvSysPscOther_Type()
)
clvSysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscOther.setStatus("current")
_ClvIfStatsTable_Object = MibTable
clvIfStatsTable = _ClvIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    clvIfStatsTable.setStatus("current")
_ClvIfStatsEntry_Object = MibTableRow
clvIfStatsEntry = _ClvIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1)
)
clvIfStatsEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfStatsIndex"),
)
if mibBuilder.loadTexts:
    clvIfStatsEntry.setStatus("current")


class _ClvIfStatsIndex_Type(Integer32):
    """Custom type clvIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfStatsIndex_Type.__name__ = "Integer32"
_ClvIfStatsIndex_Object = MibTableColumn
clvIfStatsIndex = _ClvIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 1),
    _ClvIfStatsIndex_Type()
)
clvIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfStatsIndex.setStatus("current")
_ClvIfName_Type = DisplayString
_ClvIfName_Object = MibTableColumn
clvIfName = _ClvIfName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 2),
    _ClvIfName_Type()
)
clvIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfName.setStatus("current")
_ClvIfFragsIn_Type = Counter32
_ClvIfFragsIn_Object = MibTableColumn
clvIfFragsIn = _ClvIfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 3),
    _ClvIfFragsIn_Type()
)
clvIfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfFragsIn.setStatus("current")
_ClvIfFragReassOk_Type = Counter32
_ClvIfFragReassOk_Object = MibTableColumn
clvIfFragReassOk = _ClvIfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 4),
    _ClvIfFragReassOk_Type()
)
clvIfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfFragReassOk.setStatus("current")
_ClvIfFragReassFail_Type = Counter32
_ClvIfFragReassFail_Object = MibTableColumn
clvIfFragReassFail = _ClvIfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 5),
    _ClvIfFragReassFail_Type()
)
clvIfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfFragReassFail.setStatus("current")
_ClvIfPktsInCnt_Type = Counter32
_ClvIfPktsInCnt_Object = MibTableColumn
clvIfPktsInCnt = _ClvIfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 6),
    _ClvIfPktsInCnt_Type()
)
clvIfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfPktsInCnt.setStatus("current")
_ClvIfPktsOutCnt_Type = Counter32
_ClvIfPktsOutCnt_Object = MibTableColumn
clvIfPktsOutCnt = _ClvIfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 7),
    _ClvIfPktsOutCnt_Type()
)
clvIfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfPktsOutCnt.setStatus("current")
_ClvIfBitsInCnt_Type = Counter32
_ClvIfBitsInCnt_Object = MibTableColumn
clvIfBitsInCnt = _ClvIfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 8),
    _ClvIfBitsInCnt_Type()
)
clvIfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfBitsInCnt.setStatus("current")
_ClvIfBitsOutCnt_Type = Counter32
_ClvIfBitsOutCnt_Object = MibTableColumn
clvIfBitsOutCnt = _ClvIfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 9),
    _ClvIfBitsOutCnt_Type()
)
clvIfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfBitsOutCnt.setStatus("current")
_ClvIfPktsTotCnt_Type = Counter32
_ClvIfPktsTotCnt_Object = MibTableColumn
clvIfPktsTotCnt = _ClvIfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 10),
    _ClvIfPktsTotCnt_Type()
)
clvIfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfPktsTotCnt.setStatus("current")
_ClvIfBitsTotCnt_Type = Counter32
_ClvIfBitsTotCnt_Object = MibTableColumn
clvIfBitsTotCnt = _ClvIfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 11),
    _ClvIfBitsTotCnt_Type()
)
clvIfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfBitsTotCnt.setStatus("current")
_ClvIfRxRingTable_Object = MibTable
clvIfRxRingTable = _ClvIfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    clvIfRxRingTable.setStatus("current")
_ClvIfRxRingEntry_Object = MibTableRow
clvIfRxRingEntry = _ClvIfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1)
)
clvIfRxRingEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfRxRingIndex"),
)
if mibBuilder.loadTexts:
    clvIfRxRingEntry.setStatus("current")


class _ClvIfRxRingIndex_Type(Integer32):
    """Custom type clvIfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfRxRingIndex_Type.__name__ = "Integer32"
_ClvIfRxRingIndex_Object = MibTableColumn
clvIfRxRingIndex = _ClvIfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 1),
    _ClvIfRxRingIndex_Type()
)
clvIfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfRxRingIndex.setStatus("current")
_ClvIfRxRingFifoErrors_Type = Counter32
_ClvIfRxRingFifoErrors_Object = MibTableColumn
clvIfRxRingFifoErrors = _ClvIfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 2),
    _ClvIfRxRingFifoErrors_Type()
)
clvIfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxRingFifoErrors.setStatus("current")
_ClvIfRxDespools_Type = Gauge32
_ClvIfRxDespools_Object = MibTableColumn
clvIfRxDespools = _ClvIfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 3),
    _ClvIfRxDespools_Type()
)
clvIfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxDespools.setStatus("current")
_ClvIfRxAvgUse_Type = Gauge32
_ClvIfRxAvgUse_Object = MibTableColumn
clvIfRxAvgUse = _ClvIfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 4),
    _ClvIfRxAvgUse_Type()
)
clvIfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxAvgUse.setStatus("current")
_ClvIfRxRingSaturation_Type = Gauge32
_ClvIfRxRingSaturation_Object = MibTableColumn
clvIfRxRingSaturation = _ClvIfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 5),
    _ClvIfRxRingSaturation_Type()
)
clvIfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxRingSaturation.setStatus("current")
_ClvRxRingFlooded_Type = Gauge32
_ClvRxRingFlooded_Object = MibTableColumn
clvRxRingFlooded = _ClvRxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 6),
    _ClvRxRingFlooded_Type()
)
clvRxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRxRingFlooded.setStatus("current")
_ClvIfTxRingTable_Object = MibTable
clvIfTxRingTable = _ClvIfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    clvIfTxRingTable.setStatus("current")
_ClvIfTxRingEntry_Object = MibTableRow
clvIfTxRingEntry = _ClvIfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1)
)
clvIfTxRingEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfTxRingIndex"),
)
if mibBuilder.loadTexts:
    clvIfTxRingEntry.setStatus("current")


class _ClvIfTxRingIndex_Type(Integer32):
    """Custom type clvIfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfTxRingIndex_Type.__name__ = "Integer32"
_ClvIfTxRingIndex_Object = MibTableColumn
clvIfTxRingIndex = _ClvIfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 1),
    _ClvIfTxRingIndex_Type()
)
clvIfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfTxRingIndex.setStatus("current")
_ClvIfTxDespools_Type = Gauge32
_ClvIfTxDespools_Object = MibTableColumn
clvIfTxDespools = _ClvIfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 2),
    _ClvIfTxDespools_Type()
)
clvIfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfTxDespools.setStatus("current")
_ClvIfTxAvgUse_Type = Gauge32
_ClvIfTxAvgUse_Object = MibTableColumn
clvIfTxAvgUse = _ClvIfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 3),
    _ClvIfTxAvgUse_Type()
)
clvIfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfTxAvgUse.setStatus("current")
_ClvIfTxRingSaturation_Type = Gauge32
_ClvIfTxRingSaturation_Object = MibTableColumn
clvIfTxRingSaturation = _ClvIfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 4),
    _ClvIfTxRingSaturation_Type()
)
clvIfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfTxRingSaturation.setStatus("current")
_ClvRxTingFlooded_Type = Gauge32
_ClvRxTingFlooded_Object = MibTableColumn
clvRxTingFlooded = _ClvRxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 5),
    _ClvRxTingFlooded_Type()
)
clvRxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRxTingFlooded.setStatus("current")
_ClvIfVlanStatsTable_Object = MibTable
clvIfVlanStatsTable = _ClvIfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    clvIfVlanStatsTable.setStatus("current")
_ClvIfVlanStatsEntry_Object = MibTableRow
clvIfVlanStatsEntry = _ClvIfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1)
)
clvIfVlanStatsEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfVlanIndex"),
)
if mibBuilder.loadTexts:
    clvIfVlanStatsEntry.setStatus("current")


class _ClvIfVlanIndex_Type(Integer32):
    """Custom type clvIfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfVlanIndex_Type.__name__ = "Integer32"
_ClvIfVlanIndex_Object = MibTableColumn
clvIfVlanIndex = _ClvIfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 1),
    _ClvIfVlanIndex_Type()
)
clvIfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfVlanIndex.setStatus("current")
_ClvIfVlanUntaggedInPkts_Type = Counter32
_ClvIfVlanUntaggedInPkts_Object = MibTableColumn
clvIfVlanUntaggedInPkts = _ClvIfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 2),
    _ClvIfVlanUntaggedInPkts_Type()
)
clvIfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedInPkts.setStatus("current")
_ClvIfVlanUntaggedOutPkts_Type = Counter32
_ClvIfVlanUntaggedOutPkts_Object = MibTableColumn
clvIfVlanUntaggedOutPkts = _ClvIfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 3),
    _ClvIfVlanUntaggedOutPkts_Type()
)
clvIfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedOutPkts.setStatus("current")
_ClvIfVlanUntaggedTotPkts_Type = Counter32
_ClvIfVlanUntaggedTotPkts_Object = MibTableColumn
clvIfVlanUntaggedTotPkts = _ClvIfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 4),
    _ClvIfVlanUntaggedTotPkts_Type()
)
clvIfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedTotPkts.setStatus("current")
_ClvIfVlanUntaggedInOctets_Type = Counter32
_ClvIfVlanUntaggedInOctets_Object = MibTableColumn
clvIfVlanUntaggedInOctets = _ClvIfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 5),
    _ClvIfVlanUntaggedInOctets_Type()
)
clvIfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedInOctets.setStatus("current")
_ClvIfVlanUntaggedOutOctets_Type = Counter32
_ClvIfVlanUntaggedOutOctets_Object = MibTableColumn
clvIfVlanUntaggedOutOctets = _ClvIfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 6),
    _ClvIfVlanUntaggedOutOctets_Type()
)
clvIfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedOutOctets.setStatus("current")
_ClvIfVlanUntaggedTotOctets_Type = Counter32
_ClvIfVlanUntaggedTotOctets_Object = MibTableColumn
clvIfVlanUntaggedTotOctets = _ClvIfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 7),
    _ClvIfVlanUntaggedTotOctets_Type()
)
clvIfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedTotOctets.setStatus("current")
_ClvHWSensorTable_Object = MibTable
clvHWSensorTable = _ClvHWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    clvHWSensorTable.setStatus("current")
_ClvHWSensorEntry_Object = MibTableRow
clvHWSensorEntry = _ClvHWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1)
)
clvHWSensorEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvHWSensorIndex"),
)
if mibBuilder.loadTexts:
    clvHWSensorEntry.setStatus("current")


class _ClvHWSensorIndex_Type(Integer32):
    """Custom type clvHWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvHWSensorIndex_Type.__name__ = "Integer32"
_ClvHWSensorIndex_Object = MibTableColumn
clvHWSensorIndex = _ClvHWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 1),
    _ClvHWSensorIndex_Type()
)
clvHWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvHWSensorIndex.setStatus("current")
_ClvHWSensorName_Type = DisplayString
_ClvHWSensorName_Object = MibTableColumn
clvHWSensorName = _ClvHWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 2),
    _ClvHWSensorName_Type()
)
clvHWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHWSensorName.setStatus("current")
_ClvHWSensorValue_Type = Gauge32
_ClvHWSensorValue_Object = MibTableColumn
clvHWSensorValue = _ClvHWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 3),
    _ClvHWSensorValue_Type()
)
clvHWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHWSensorValue.setStatus("current")
_ClvHWSensorUnit_Type = DisplayString
_ClvHWSensorUnit_Object = MibTableColumn
clvHWSensorUnit = _ClvHWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 4),
    _ClvHWSensorUnit_Type()
)
clvHWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHWSensorUnit.setStatus("current")
_ClvSysMemUsage_Type = Gauge32
_ClvSysMemUsage_Object = MibScalar
clvSysMemUsage = _ClvSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 12),
    _ClvSysMemUsage_Type()
)
clvSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysMemUsage.setStatus("current")
_ClvSysTCPUsage_ObjectIdentity = ObjectIdentity
clvSysTCPUsage = _ClvSysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13)
)
_ClvSysTCPRecvSmall_Type = Gauge32
_ClvSysTCPRecvSmall_Object = MibScalar
clvSysTCPRecvSmall = _ClvSysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 1),
    _ClvSysTCPRecvSmall_Type()
)
clvSysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPRecvSmall.setStatus("current")
_ClvSysTCPRecvLarge_Type = Gauge32
_ClvSysTCPRecvLarge_Object = MibScalar
clvSysTCPRecvLarge = _ClvSysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 2),
    _ClvSysTCPRecvLarge_Type()
)
clvSysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPRecvLarge.setStatus("current")
_ClvSysTCPSendSmall_Type = Gauge32
_ClvSysTCPSendSmall_Object = MibScalar
clvSysTCPSendSmall = _ClvSysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 3),
    _ClvSysTCPSendSmall_Type()
)
clvSysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPSendSmall.setStatus("current")
_ClvSysTCPSendLarge_Type = Gauge32
_ClvSysTCPSendLarge_Object = MibScalar
clvSysTCPSendLarge = _ClvSysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 4),
    _ClvSysTCPSendLarge_Type()
)
clvSysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPSendLarge.setStatus("current")
_ClvSysTimerUsage_Type = Gauge32
_ClvSysTimerUsage_Object = MibScalar
clvSysTimerUsage = _ClvSysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 14),
    _ClvSysTimerUsage_Type()
)
clvSysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTimerUsage.setStatus("current")
_ClvVPN_ObjectIdentity = ObjectIdentity
clvVPN = _ClvVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2)
)
_ClvIPsec_ObjectIdentity = ObjectIdentity
clvIPsec = _ClvIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1)
)
_ClvIPsecGlobal_ObjectIdentity = ObjectIdentity
clvIPsecGlobal = _ClvIPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1)
)
_ClvIPsecPhaseOneActive_Type = Gauge32
_ClvIPsecPhaseOneActive_Object = MibScalar
clvIPsecPhaseOneActive = _ClvIPsecPhaseOneActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 1),
    _ClvIPsecPhaseOneActive_Type()
)
clvIPsecPhaseOneActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecPhaseOneActive.setStatus("current")
_ClvIPsecPhaseOneAggrModeDone_Type = Gauge32
_ClvIPsecPhaseOneAggrModeDone_Object = MibScalar
clvIPsecPhaseOneAggrModeDone = _ClvIPsecPhaseOneAggrModeDone_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 2),
    _ClvIPsecPhaseOneAggrModeDone_Type()
)
clvIPsecPhaseOneAggrModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecPhaseOneAggrModeDone.setStatus("current")
_ClvIPsecQuickModeActive_Type = Gauge32
_ClvIPsecQuickModeActive_Object = MibScalar
clvIPsecQuickModeActive = _ClvIPsecQuickModeActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 3),
    _ClvIPsecQuickModeActive_Type()
)
clvIPsecQuickModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecQuickModeActive.setStatus("current")
_ClvIPsecPhaseOneDone_Type = Counter32
_ClvIPsecPhaseOneDone_Object = MibScalar
clvIPsecPhaseOneDone = _ClvIPsecPhaseOneDone_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 4),
    _ClvIPsecPhaseOneDone_Type()
)
clvIPsecPhaseOneDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecPhaseOneDone.setStatus("current")
_ClvIPsecPhaseOneFailed_Type = Counter32
_ClvIPsecPhaseOneFailed_Object = MibScalar
clvIPsecPhaseOneFailed = _ClvIPsecPhaseOneFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 5),
    _ClvIPsecPhaseOneFailed_Type()
)
clvIPsecPhaseOneFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecPhaseOneFailed.setStatus("current")
_ClvIPsecPhaseOneRekeyed_Type = Counter32
_ClvIPsecPhaseOneRekeyed_Object = MibScalar
clvIPsecPhaseOneRekeyed = _ClvIPsecPhaseOneRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 6),
    _ClvIPsecPhaseOneRekeyed_Type()
)
clvIPsecPhaseOneRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecPhaseOneRekeyed.setStatus("current")
_ClvIPsecQuickModeDone_Type = Counter32
_ClvIPsecQuickModeDone_Object = MibScalar
clvIPsecQuickModeDone = _ClvIPsecQuickModeDone_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 7),
    _ClvIPsecQuickModeDone_Type()
)
clvIPsecQuickModeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecQuickModeDone.setStatus("current")
_ClvIPsecQuickModeFailed_Type = Counter32
_ClvIPsecQuickModeFailed_Object = MibScalar
clvIPsecQuickModeFailed = _ClvIPsecQuickModeFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 8),
    _ClvIPsecQuickModeFailed_Type()
)
clvIPsecQuickModeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecQuickModeFailed.setStatus("current")
_ClvIPsecInfoDone_Type = Counter32
_ClvIPsecInfoDone_Object = MibScalar
clvIPsecInfoDone = _ClvIPsecInfoDone_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 9),
    _ClvIPsecInfoDone_Type()
)
clvIPsecInfoDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInfoDone.setStatus("current")
_ClvIPsecInfoFailed_Type = Counter32
_ClvIPsecInfoFailed_Object = MibScalar
clvIPsecInfoFailed = _ClvIPsecInfoFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 10),
    _ClvIPsecInfoFailed_Type()
)
clvIPsecInfoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInfoFailed.setStatus("current")
_ClvIPsecInOctetsComp_Type = Counter64
_ClvIPsecInOctetsComp_Object = MibScalar
clvIPsecInOctetsComp = _ClvIPsecInOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 11),
    _ClvIPsecInOctetsComp_Type()
)
clvIPsecInOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInOctetsComp.setStatus("current")
_ClvIPsecInOctetsUncomp_Type = Counter64
_ClvIPsecInOctetsUncomp_Object = MibScalar
clvIPsecInOctetsUncomp = _ClvIPsecInOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 12),
    _ClvIPsecInOctetsUncomp_Type()
)
clvIPsecInOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInOctetsUncomp.setStatus("current")
_ClvIPsecOutOctetsComp_Type = Counter64
_ClvIPsecOutOctetsComp_Object = MibScalar
clvIPsecOutOctetsComp = _ClvIPsecOutOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 13),
    _ClvIPsecOutOctetsComp_Type()
)
clvIPsecOutOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutOctetsComp.setStatus("current")
_ClvIPsecOutOctetsUncomp_Type = Counter64
_ClvIPsecOutOctetsUncomp_Object = MibScalar
clvIPsecOutOctetsUncomp = _ClvIPsecOutOctetsUncomp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 14),
    _ClvIPsecOutOctetsUncomp_Type()
)
clvIPsecOutOctetsUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutOctetsUncomp.setStatus("current")
_ClvIPsecForwardedOctetsComp_Type = Counter64
_ClvIPsecForwardedOctetsComp_Object = MibScalar
clvIPsecForwardedOctetsComp = _ClvIPsecForwardedOctetsComp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 15),
    _ClvIPsecForwardedOctetsComp_Type()
)
clvIPsecForwardedOctetsComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecForwardedOctetsComp.setStatus("current")
_ClvIPsecForwardedOctetsUcomp_Type = Counter64
_ClvIPsecForwardedOctetsUcomp_Object = MibScalar
clvIPsecForwardedOctetsUcomp = _ClvIPsecForwardedOctetsUcomp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 16),
    _ClvIPsecForwardedOctetsUcomp_Type()
)
clvIPsecForwardedOctetsUcomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecForwardedOctetsUcomp.setStatus("current")
_ClvIPsecInPackets_Type = Counter64
_ClvIPsecInPackets_Object = MibScalar
clvIPsecInPackets = _ClvIPsecInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 17),
    _ClvIPsecInPackets_Type()
)
clvIPsecInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInPackets.setStatus("current")
_ClvIPsecOutPackets_Type = Counter64
_ClvIPsecOutPackets_Object = MibScalar
clvIPsecOutPackets = _ClvIPsecOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 18),
    _ClvIPsecOutPackets_Type()
)
clvIPsecOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutPackets.setStatus("current")
_ClvIPsecForwardedPackets_Type = Counter64
_ClvIPsecForwardedPackets_Object = MibScalar
clvIPsecForwardedPackets = _ClvIPsecForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 19),
    _ClvIPsecForwardedPackets_Type()
)
clvIPsecForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecForwardedPackets.setStatus("current")
_ClvIPsecActiveTransforms_Type = Gauge32
_ClvIPsecActiveTransforms_Object = MibScalar
clvIPsecActiveTransforms = _ClvIPsecActiveTransforms_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 20),
    _ClvIPsecActiveTransforms_Type()
)
clvIPsecActiveTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecActiveTransforms.setStatus("current")
_ClvIPsecTotalTransforms_Type = Counter32
_ClvIPsecTotalTransforms_Object = MibScalar
clvIPsecTotalTransforms = _ClvIPsecTotalTransforms_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 21),
    _ClvIPsecTotalTransforms_Type()
)
clvIPsecTotalTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecTotalTransforms.setStatus("current")
_ClvIPsecOutOfTransforms_Type = Counter32
_ClvIPsecOutOfTransforms_Object = MibScalar
clvIPsecOutOfTransforms = _ClvIPsecOutOfTransforms_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 22),
    _ClvIPsecOutOfTransforms_Type()
)
clvIPsecOutOfTransforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutOfTransforms.setStatus("current")
_ClvIPsecTotalRekeys_Type = Counter32
_ClvIPsecTotalRekeys_Object = MibScalar
clvIPsecTotalRekeys = _ClvIPsecTotalRekeys_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 23),
    _ClvIPsecTotalRekeys_Type()
)
clvIPsecTotalRekeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecTotalRekeys.setStatus("current")
_ClvRules_ObjectIdentity = ObjectIdentity
clvRules = _ClvRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3)
)
_ClvRuleUseTable_Object = MibTable
clvRuleUseTable = _ClvRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    clvRuleUseTable.setStatus("current")
_ClvRuleUseEntry_Object = MibTableRow
clvRuleUseEntry = _ClvRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1)
)
clvRuleUseEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvRuleIndex"),
)
if mibBuilder.loadTexts:
    clvRuleUseEntry.setStatus("current")


class _ClvRuleIndex_Type(Integer32):
    """Custom type clvRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvRuleIndex_Type.__name__ = "Integer32"
_ClvRuleIndex_Object = MibTableColumn
clvRuleIndex = _ClvRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1, 1),
    _ClvRuleIndex_Type()
)
clvRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvRuleIndex.setStatus("current")
_ClvRuleName_Type = DisplayString
_ClvRuleName_Object = MibTableColumn
clvRuleName = _ClvRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1, 2),
    _ClvRuleName_Type()
)
clvRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRuleName.setStatus("current")
_ClvRuleUse_Type = Counter32
_ClvRuleUse_Object = MibTableColumn
clvRuleUse = _ClvRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1, 3),
    _ClvRuleUse_Type()
)
clvRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRuleUse.setStatus("current")
_ClvIPPools_ObjectIdentity = ObjectIdentity
clvIPPools = _ClvIPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4)
)
_ClvIPPoolsNumber_Type = Integer32
_ClvIPPoolsNumber_Object = MibScalar
clvIPPoolsNumber = _ClvIPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 1),
    _ClvIPPoolsNumber_Type()
)
clvIPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolsNumber.setStatus("current")
_ClvIPPoolTable_Object = MibTable
clvIPPoolTable = _ClvIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    clvIPPoolTable.setStatus("current")
_ClvIPPoolEntry_Object = MibTableRow
clvIPPoolEntry = _ClvIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1)
)
clvIPPoolEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIPPoolIndex"),
)
if mibBuilder.loadTexts:
    clvIPPoolEntry.setStatus("current")


class _ClvIPPoolIndex_Type(Integer32):
    """Custom type clvIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIPPoolIndex_Type.__name__ = "Integer32"
_ClvIPPoolIndex_Object = MibTableColumn
clvIPPoolIndex = _ClvIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 1),
    _ClvIPPoolIndex_Type()
)
clvIPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIPPoolIndex.setStatus("current")
_ClvIPPoolName_Type = DisplayString
_ClvIPPoolName_Object = MibTableColumn
clvIPPoolName = _ClvIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 2),
    _ClvIPPoolName_Type()
)
clvIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolName.setStatus("current")
_ClvIPPoolPrepare_Type = Gauge32
_ClvIPPoolPrepare_Object = MibTableColumn
clvIPPoolPrepare = _ClvIPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 3),
    _ClvIPPoolPrepare_Type()
)
clvIPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolPrepare.setStatus("current")
_ClvIPPoolFree_Type = Gauge32
_ClvIPPoolFree_Object = MibTableColumn
clvIPPoolFree = _ClvIPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 4),
    _ClvIPPoolFree_Type()
)
clvIPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolFree.setStatus("current")
_ClvIPPoolMisses_Type = Gauge32
_ClvIPPoolMisses_Object = MibTableColumn
clvIPPoolMisses = _ClvIPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 5),
    _ClvIPPoolMisses_Type()
)
clvIPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolMisses.setStatus("current")
_ClvIPPoolClientFails_Type = Gauge32
_ClvIPPoolClientFails_Object = MibTableColumn
clvIPPoolClientFails = _ClvIPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 6),
    _ClvIPPoolClientFails_Type()
)
clvIPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolClientFails.setStatus("current")
_ClvIPPoolUsed_Type = Gauge32
_ClvIPPoolUsed_Object = MibTableColumn
clvIPPoolUsed = _ClvIPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 7),
    _ClvIPPoolUsed_Type()
)
clvIPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolUsed.setStatus("current")
_ClvDHCPServer_ObjectIdentity = ObjectIdentity
clvDHCPServer = _ClvDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5)
)
_ClvDHCPTotalRejected_Type = Gauge32
_ClvDHCPTotalRejected_Object = MibScalar
clvDHCPTotalRejected = _ClvDHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 1),
    _ClvDHCPTotalRejected_Type()
)
clvDHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPTotalRejected.setStatus("current")
_ClvDHCPRuleTable_Object = MibTable
clvDHCPRuleTable = _ClvDHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    clvDHCPRuleTable.setStatus("current")
_ClvDHCPRuleEntry_Object = MibTableRow
clvDHCPRuleEntry = _ClvDHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1)
)
clvDHCPRuleEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvDHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    clvDHCPRuleEntry.setStatus("current")


class _ClvDHCPRuleIndex_Type(Integer32):
    """Custom type clvDHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvDHCPRuleIndex_Type.__name__ = "Integer32"
_ClvDHCPRuleIndex_Object = MibTableColumn
clvDHCPRuleIndex = _ClvDHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 1),
    _ClvDHCPRuleIndex_Type()
)
clvDHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvDHCPRuleIndex.setStatus("current")
_ClvDHCPRuleName_Type = DisplayString
_ClvDHCPRuleName_Object = MibTableColumn
clvDHCPRuleName = _ClvDHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 2),
    _ClvDHCPRuleName_Type()
)
clvDHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRuleName.setStatus("current")
_ClvDHCPRuleUsage_Type = Gauge32
_ClvDHCPRuleUsage_Object = MibTableColumn
clvDHCPRuleUsage = _ClvDHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 3),
    _ClvDHCPRuleUsage_Type()
)
clvDHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRuleUsage.setStatus("current")
_ClvDHCPRuleUsagePercent_Type = Gauge32
_ClvDHCPRuleUsagePercent_Object = MibTableColumn
clvDHCPRuleUsagePercent = _ClvDHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 4),
    _ClvDHCPRuleUsagePercent_Type()
)
clvDHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRuleUsagePercent.setStatus("current")
_ClvDHCPActiveClients_Type = Gauge32
_ClvDHCPActiveClients_Object = MibTableColumn
clvDHCPActiveClients = _ClvDHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 5),
    _ClvDHCPActiveClients_Type()
)
clvDHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPActiveClients.setStatus("current")
_ClvDHCPActiveClientsPercent_Type = Gauge32
_ClvDHCPActiveClientsPercent_Object = MibTableColumn
clvDHCPActiveClientsPercent = _ClvDHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 6),
    _ClvDHCPActiveClientsPercent_Type()
)
clvDHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPActiveClientsPercent.setStatus("current")
_ClvDHCPRejectedRequests_Type = Gauge32
_ClvDHCPRejectedRequests_Object = MibTableColumn
clvDHCPRejectedRequests = _ClvDHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 7),
    _ClvDHCPRejectedRequests_Type()
)
clvDHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRejectedRequests.setStatus("current")
_ClvDHCPTotalLeases_Type = Gauge32
_ClvDHCPTotalLeases_Object = MibTableColumn
clvDHCPTotalLeases = _ClvDHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 8),
    _ClvDHCPTotalLeases_Type()
)
clvDHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPTotalLeases.setStatus("current")
_ClvUserAuth_ObjectIdentity = ObjectIdentity
clvUserAuth = _ClvUserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6)
)
_ClvUserAuthHTTPUsers_Type = Gauge32
_ClvUserAuthHTTPUsers_Object = MibScalar
clvUserAuthHTTPUsers = _ClvUserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 1),
    _ClvUserAuthHTTPUsers_Type()
)
clvUserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthHTTPUsers.setStatus("current")
_ClvUserAuthXAUTHUsers_Type = Gauge32
_ClvUserAuthXAUTHUsers_Object = MibScalar
clvUserAuthXAUTHUsers = _ClvUserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 2),
    _ClvUserAuthXAUTHUsers_Type()
)
clvUserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthXAUTHUsers.setStatus("current")
_ClvUserAuthHTTPSUsers_Type = Gauge32
_ClvUserAuthHTTPSUsers_Object = MibScalar
clvUserAuthHTTPSUsers = _ClvUserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 3),
    _ClvUserAuthHTTPSUsers_Type()
)
clvUserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthHTTPSUsers.setStatus("current")
_ClvUserAuthPPPUsers_Type = Gauge32
_ClvUserAuthPPPUsers_Object = MibScalar
clvUserAuthPPPUsers = _ClvUserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 4),
    _ClvUserAuthPPPUsers_Type()
)
clvUserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthPPPUsers.setStatus("current")
_ClvUserAuthEAPUsers_Type = Gauge32
_ClvUserAuthEAPUsers_Object = MibScalar
clvUserAuthEAPUsers = _ClvUserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 5),
    _ClvUserAuthEAPUsers_Type()
)
clvUserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthEAPUsers.setStatus("current")
_ClvUserAuthRuleUseTable_Object = MibTable
clvUserAuthRuleUseTable = _ClvUserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    clvUserAuthRuleUseTable.setStatus("current")
_ClvUserAuthRuleUseEntry_Object = MibTableRow
clvUserAuthRuleUseEntry = _ClvUserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1)
)
clvUserAuthRuleUseEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvUserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    clvUserAuthRuleUseEntry.setStatus("current")


class _ClvUserAuthRuleIndex_Type(Integer32):
    """Custom type clvUserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvUserAuthRuleIndex_Type.__name__ = "Integer32"
_ClvUserAuthRuleIndex_Object = MibTableColumn
clvUserAuthRuleIndex = _ClvUserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1, 1),
    _ClvUserAuthRuleIndex_Type()
)
clvUserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvUserAuthRuleIndex.setStatus("current")
_ClvUserAuthRuleName_Type = DisplayString
_ClvUserAuthRuleName_Object = MibTableColumn
clvUserAuthRuleName = _ClvUserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1, 2),
    _ClvUserAuthRuleName_Type()
)
clvUserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthRuleName.setStatus("current")
_ClvUserAuthRuleUse_Type = Counter32
_ClvUserAuthRuleUse_Object = MibTableColumn
clvUserAuthRuleUse = _ClvUserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1, 3),
    _ClvUserAuthRuleUse_Type()
)
clvUserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthRuleUse.setStatus("current")
_ClvLinkMonitor_ObjectIdentity = ObjectIdentity
clvLinkMonitor = _ClvLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7)
)
_ClvLinkMonGrp_Type = Integer32
_ClvLinkMonGrp_Object = MibScalar
clvLinkMonGrp = _ClvLinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 1),
    _ClvLinkMonGrp_Type()
)
clvLinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonGrp.setStatus("current")
_ClvLinkMonGrpTable_Object = MibTable
clvLinkMonGrpTable = _ClvLinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    clvLinkMonGrpTable.setStatus("current")
_ClvLinkMonGrpEntry_Object = MibTableRow
clvLinkMonGrpEntry = _ClvLinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1)
)
clvLinkMonGrpEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvLinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    clvLinkMonGrpEntry.setStatus("current")


class _ClvLinkMonGrpIndex_Type(Integer32):
    """Custom type clvLinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvLinkMonGrpIndex_Type.__name__ = "Integer32"
_ClvLinkMonGrpIndex_Object = MibTableColumn
clvLinkMonGrpIndex = _ClvLinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1, 1),
    _ClvLinkMonGrpIndex_Type()
)
clvLinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvLinkMonGrpIndex.setStatus("current")
_ClvLinkMonGrpName_Type = DisplayString
_ClvLinkMonGrpName_Object = MibTableColumn
clvLinkMonGrpName = _ClvLinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1, 2),
    _ClvLinkMonGrpName_Type()
)
clvLinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonGrpName.setStatus("current")
_ClvLinkMonGrpHostsUp_Type = Gauge32
_ClvLinkMonGrpHostsUp_Object = MibTableColumn
clvLinkMonGrpHostsUp = _ClvLinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1, 3),
    _ClvLinkMonGrpHostsUp_Type()
)
clvLinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonGrpHostsUp.setStatus("current")
_ClvLinkMonHostTable_Object = MibTable
clvLinkMonHostTable = _ClvLinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    clvLinkMonHostTable.setStatus("current")
_ClvLinkMonHostEntry_Object = MibTableRow
clvLinkMonHostEntry = _ClvLinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1)
)
clvLinkMonHostEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvLinkMonGrpIndex"),
    (0, "CLAVISTER-MIB", "clvLinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    clvLinkMonHostEntry.setStatus("current")


class _ClvLinkMonHostIndex_Type(Integer32):
    """Custom type clvLinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvLinkMonHostIndex_Type.__name__ = "Integer32"
_ClvLinkMonHostIndex_Object = MibTableColumn
clvLinkMonHostIndex = _ClvLinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 1),
    _ClvLinkMonHostIndex_Type()
)
clvLinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvLinkMonHostIndex.setStatus("current")
_ClvLinkMonHostId_Type = DisplayString
_ClvLinkMonHostId_Object = MibTableColumn
clvLinkMonHostId = _ClvLinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 2),
    _ClvLinkMonHostId_Type()
)
clvLinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonHostId.setStatus("current")
_ClvLinkMonHostShortTermLoss_Type = Gauge32
_ClvLinkMonHostShortTermLoss_Object = MibTableColumn
clvLinkMonHostShortTermLoss = _ClvLinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 3),
    _ClvLinkMonHostShortTermLoss_Type()
)
clvLinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonHostShortTermLoss.setStatus("current")
_ClvLinkMonHostPacketsLost_Type = Counter32
_ClvLinkMonHostPacketsLost_Object = MibTableColumn
clvLinkMonHostPacketsLost = _ClvLinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 4),
    _ClvLinkMonHostPacketsLost_Type()
)
clvLinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonHostPacketsLost.setStatus("current")
_ClvPipes_ObjectIdentity = ObjectIdentity
clvPipes = _ClvPipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8)
)
_ClvPipeUsers_Type = Gauge32
_ClvPipeUsers_Object = MibScalar
clvPipeUsers = _ClvPipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 1),
    _ClvPipeUsers_Type()
)
clvPipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeUsers.setStatus("current")
_ClvPipeTable_Object = MibTable
clvPipeTable = _ClvPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    clvPipeTable.setStatus("current")
_ClvPipeEntry_Object = MibTableRow
clvPipeEntry = _ClvPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1)
)
clvPipeEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvPipeIndex"),
)
if mibBuilder.loadTexts:
    clvPipeEntry.setStatus("current")


class _ClvPipeIndex_Type(Integer32):
    """Custom type clvPipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvPipeIndex_Type.__name__ = "Integer32"
_ClvPipeIndex_Object = MibTableColumn
clvPipeIndex = _ClvPipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 1),
    _ClvPipeIndex_Type()
)
clvPipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvPipeIndex.setStatus("current")
_ClvPipeName_Type = DisplayString
_ClvPipeName_Object = MibTableColumn
clvPipeName = _ClvPipeName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 2),
    _ClvPipeName_Type()
)
clvPipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeName.setStatus("current")
_ClvPipeMinPrec_Type = Integer32
_ClvPipeMinPrec_Object = MibTableColumn
clvPipeMinPrec = _ClvPipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 3),
    _ClvPipeMinPrec_Type()
)
clvPipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeMinPrec.setStatus("current")
_ClvPipeMaxPrec_Type = Integer32
_ClvPipeMaxPrec_Object = MibTableColumn
clvPipeMaxPrec = _ClvPipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 4),
    _ClvPipeMaxPrec_Type()
)
clvPipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeMaxPrec.setStatus("current")
_ClvPipeDefPrec_Type = Integer32
_ClvPipeDefPrec_Object = MibTableColumn
clvPipeDefPrec = _ClvPipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 5),
    _ClvPipeDefPrec_Type()
)
clvPipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeDefPrec.setStatus("current")
_ClvPipeNumPrec_Type = Integer32
_ClvPipeNumPrec_Object = MibTableColumn
clvPipeNumPrec = _ClvPipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 6),
    _ClvPipeNumPrec_Type()
)
clvPipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeNumPrec.setStatus("current")
_ClvPipeNumUsers_Type = Gauge32
_ClvPipeNumUsers_Object = MibTableColumn
clvPipeNumUsers = _ClvPipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 7),
    _ClvPipeNumUsers_Type()
)
clvPipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeNumUsers.setStatus("current")
_ClvPipeCurrentBps_Type = Gauge32
_ClvPipeCurrentBps_Object = MibTableColumn
clvPipeCurrentBps = _ClvPipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 8),
    _ClvPipeCurrentBps_Type()
)
clvPipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeCurrentBps.setStatus("current")
_ClvPipeCurrentPps_Type = Gauge32
_ClvPipeCurrentPps_Object = MibTableColumn
clvPipeCurrentPps = _ClvPipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 9),
    _ClvPipeCurrentPps_Type()
)
clvPipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeCurrentPps.setStatus("current")
_ClvPipeDelayedPackets_Type = Counter32
_ClvPipeDelayedPackets_Object = MibTableColumn
clvPipeDelayedPackets = _ClvPipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 10),
    _ClvPipeDelayedPackets_Type()
)
clvPipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeDelayedPackets.setStatus("current")
_ClvPipeDropedPackets_Type = Counter32
_ClvPipeDropedPackets_Object = MibTableColumn
clvPipeDropedPackets = _ClvPipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 11),
    _ClvPipeDropedPackets_Type()
)
clvPipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeDropedPackets.setStatus("current")
_ClvPipePrecTable_Object = MibTable
clvPipePrecTable = _ClvPipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    clvPipePrecTable.setStatus("current")
_ClvPipePrecEntry_Object = MibTableRow
clvPipePrecEntry = _ClvPipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1)
)
clvPipePrecEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvPipeIndex"),
    (0, "CLAVISTER-MIB", "clvPipePrecIndex"),
)
if mibBuilder.loadTexts:
    clvPipePrecEntry.setStatus("current")


class _ClvPipePrecIndex_Type(Integer32):
    """Custom type clvPipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvPipePrecIndex_Type.__name__ = "Integer32"
_ClvPipePrecIndex_Object = MibTableColumn
clvPipePrecIndex = _ClvPipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 1),
    _ClvPipePrecIndex_Type()
)
clvPipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvPipePrecIndex.setStatus("current")
_ClvPipePrec_Type = Integer32
_ClvPipePrec_Object = MibTableColumn
clvPipePrec = _ClvPipePrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 2),
    _ClvPipePrec_Type()
)
clvPipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrec.setStatus("current")
_ClvPipePrecBps_Type = Gauge32
_ClvPipePrecBps_Object = MibTableColumn
clvPipePrecBps = _ClvPipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 3),
    _ClvPipePrecBps_Type()
)
clvPipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecBps.setStatus("current")
_ClvPipePrecTotalPps_Type = Gauge32
_ClvPipePrecTotalPps_Object = MibTableColumn
clvPipePrecTotalPps = _ClvPipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 4),
    _ClvPipePrecTotalPps_Type()
)
clvPipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecTotalPps.setStatus("current")
_ClvPipePrecReservedBps_Type = Gauge32
_ClvPipePrecReservedBps_Object = MibTableColumn
clvPipePrecReservedBps = _ClvPipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 5),
    _ClvPipePrecReservedBps_Type()
)
clvPipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecReservedBps.setStatus("current")
_ClvPipePrecDynLimBps_Type = Gauge32
_ClvPipePrecDynLimBps_Object = MibTableColumn
clvPipePrecDynLimBps = _ClvPipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 6),
    _ClvPipePrecDynLimBps_Type()
)
clvPipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDynLimBps.setStatus("current")
_ClvPipePrecDynUsrLimBps_Type = Gauge32
_ClvPipePrecDynUsrLimBps_Object = MibTableColumn
clvPipePrecDynUsrLimBps = _ClvPipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 7),
    _ClvPipePrecDynUsrLimBps_Type()
)
clvPipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDynUsrLimBps.setStatus("current")
_ClvPipePrecDelayedPackets_Type = Counter32
_ClvPipePrecDelayedPackets_Object = MibTableColumn
clvPipePrecDelayedPackets = _ClvPipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 8),
    _ClvPipePrecDelayedPackets_Type()
)
clvPipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDelayedPackets.setStatus("current")
_ClvPipePrecDropedPackets_Type = Counter32
_ClvPipePrecDropedPackets_Object = MibTableColumn
clvPipePrecDropedPackets = _ClvPipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 9),
    _ClvPipePrecDropedPackets_Type()
)
clvPipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDropedPackets.setStatus("current")
_ClvALG_ObjectIdentity = ObjectIdentity
clvALG = _ClvALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9)
)
_ClvAlgSessions_Type = Gauge32
_ClvAlgSessions_Object = MibScalar
clvAlgSessions = _ClvAlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 1),
    _ClvAlgSessions_Type()
)
clvAlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAlgSessions.setStatus("current")
_ClvAlgConnections_Type = Gauge32
_ClvAlgConnections_Object = MibScalar
clvAlgConnections = _ClvAlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 2),
    _ClvAlgConnections_Type()
)
clvAlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAlgConnections.setStatus("current")
_ClvAlgTCPStreams_Type = Gauge32
_ClvAlgTCPStreams_Object = MibScalar
clvAlgTCPStreams = _ClvAlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 3),
    _ClvAlgTCPStreams_Type()
)
clvAlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAlgTCPStreams.setStatus("current")
_ClvHttpAlg_ObjectIdentity = ObjectIdentity
clvHttpAlg = _ClvHttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4)
)
_ClvHttpAlgTable_Object = MibTable
clvHttpAlgTable = _ClvHttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    clvHttpAlgTable.setStatus("current")
_ClvHttpAlgEntry_Object = MibTableRow
clvHttpAlgEntry = _ClvHttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1)
)
clvHttpAlgEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvHttpAlgIndex"),
)
if mibBuilder.loadTexts:
    clvHttpAlgEntry.setStatus("current")


class _ClvHttpAlgIndex_Type(Integer32):
    """Custom type clvHttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvHttpAlgIndex_Type.__name__ = "Integer32"
_ClvHttpAlgIndex_Object = MibTableColumn
clvHttpAlgIndex = _ClvHttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 1),
    _ClvHttpAlgIndex_Type()
)
clvHttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvHttpAlgIndex.setStatus("current")
_ClvHttpAlgName_Type = DisplayString
_ClvHttpAlgName_Object = MibTableColumn
clvHttpAlgName = _ClvHttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 2),
    _ClvHttpAlgName_Type()
)
clvHttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgName.setStatus("current")
_ClvHttpAlgTotalRequested_Type = Gauge32
_ClvHttpAlgTotalRequested_Object = MibTableColumn
clvHttpAlgTotalRequested = _ClvHttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 3),
    _ClvHttpAlgTotalRequested_Type()
)
clvHttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgTotalRequested.setStatus("current")
_ClvHttpAlgTotalAllowed_Type = Gauge32
_ClvHttpAlgTotalAllowed_Object = MibTableColumn
clvHttpAlgTotalAllowed = _ClvHttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 4),
    _ClvHttpAlgTotalAllowed_Type()
)
clvHttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgTotalAllowed.setStatus("current")
_ClvHttpAlgTotalBlocked_Type = Gauge32
_ClvHttpAlgTotalBlocked_Object = MibTableColumn
clvHttpAlgTotalBlocked = _ClvHttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 5),
    _ClvHttpAlgTotalBlocked_Type()
)
clvHttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgTotalBlocked.setStatus("current")
_ClvHttpAlgCntFltTable_Object = MibTable
clvHttpAlgCntFltTable = _ClvHttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    clvHttpAlgCntFltTable.setStatus("current")
_ClvHttpAlgCntFltEntry_Object = MibTableRow
clvHttpAlgCntFltEntry = _ClvHttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1)
)
clvHttpAlgCntFltEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvHttpAlgIndex"),
    (0, "CLAVISTER-MIB", "clvHttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    clvHttpAlgCntFltEntry.setStatus("current")


class _ClvHttpAlgCntFltIndex_Type(Integer32):
    """Custom type clvHttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvHttpAlgCntFltIndex_Type.__name__ = "Integer32"
_ClvHttpAlgCntFltIndex_Object = MibTableColumn
clvHttpAlgCntFltIndex = _ClvHttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 1),
    _ClvHttpAlgCntFltIndex_Type()
)
clvHttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltIndex.setStatus("current")
_ClvHttpAlgCntFltName_Type = DisplayString
_ClvHttpAlgCntFltName_Object = MibTableColumn
clvHttpAlgCntFltName = _ClvHttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 2),
    _ClvHttpAlgCntFltName_Type()
)
clvHttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltName.setStatus("current")
_ClvHttpAlgCntFltRequests_Type = Gauge32
_ClvHttpAlgCntFltRequests_Object = MibTableColumn
clvHttpAlgCntFltRequests = _ClvHttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 3),
    _ClvHttpAlgCntFltRequests_Type()
)
clvHttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltRequests.setStatus("current")
_ClvHttpAlgCntFltAllowed_Type = Gauge32
_ClvHttpAlgCntFltAllowed_Object = MibTableColumn
clvHttpAlgCntFltAllowed = _ClvHttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 4),
    _ClvHttpAlgCntFltAllowed_Type()
)
clvHttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltAllowed.setStatus("current")
_ClvHttpAlgCntFltBlocked_Type = Gauge32
_ClvHttpAlgCntFltBlocked_Object = MibTableColumn
clvHttpAlgCntFltBlocked = _ClvHttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 5),
    _ClvHttpAlgCntFltBlocked_Type()
)
clvHttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltBlocked.setStatus("current")
_ClvSmtpAlg_ObjectIdentity = ObjectIdentity
clvSmtpAlg = _ClvSmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5)
)
_ClvSmtpAlgTable_Object = MibTable
clvSmtpAlgTable = _ClvSmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    clvSmtpAlgTable.setStatus("current")
_ClvSmtpAlgEntry_Object = MibTableRow
clvSmtpAlgEntry = _ClvSmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1)
)
clvSmtpAlgEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    clvSmtpAlgEntry.setStatus("current")


class _ClvSmtpAlgIndex_Type(Integer32):
    """Custom type clvSmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSmtpAlgIndex_Type.__name__ = "Integer32"
_ClvSmtpAlgIndex_Object = MibTableColumn
clvSmtpAlgIndex = _ClvSmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 1),
    _ClvSmtpAlgIndex_Type()
)
clvSmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSmtpAlgIndex.setStatus("current")
_ClvSmtpAlgName_Type = DisplayString
_ClvSmtpAlgName_Object = MibTableColumn
clvSmtpAlgName = _ClvSmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 2),
    _ClvSmtpAlgName_Type()
)
clvSmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgName.setStatus("current")
_ClvSmtpAlgTotCheckedSes_Type = Gauge32
_ClvSmtpAlgTotCheckedSes_Object = MibTableColumn
clvSmtpAlgTotCheckedSes = _ClvSmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 3),
    _ClvSmtpAlgTotCheckedSes_Type()
)
clvSmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgTotCheckedSes.setStatus("current")
_ClvSmtpAlgTotSpamSes_Type = Gauge32
_ClvSmtpAlgTotSpamSes_Object = MibTableColumn
clvSmtpAlgTotSpamSes = _ClvSmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 4),
    _ClvSmtpAlgTotSpamSes_Type()
)
clvSmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgTotSpamSes.setStatus("current")
_ClvSmtpAlgTotDroppedSes_Type = Gauge32
_ClvSmtpAlgTotDroppedSes_Object = MibTableColumn
clvSmtpAlgTotDroppedSes = _ClvSmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 5),
    _ClvSmtpAlgTotDroppedSes_Type()
)
clvSmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgTotDroppedSes.setStatus("current")
_ClvSmtpAlgDnsBlTable_Object = MibTable
clvSmtpAlgDnsBlTable = _ClvSmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlTable.setStatus("current")
_ClvSmtpAlgDnsBlEntry_Object = MibTableRow
clvSmtpAlgDnsBlEntry = _ClvSmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1)
)
clvSmtpAlgDnsBlEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSmtpAlgIndex"),
    (0, "CLAVISTER-MIB", "clvSmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlEntry.setStatus("current")


class _ClvSmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type clvSmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_ClvSmtpAlgDnsBlIndex_Object = MibTableColumn
clvSmtpAlgDnsBlIndex = _ClvSmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 1),
    _ClvSmtpAlgDnsBlIndex_Type()
)
clvSmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlIndex.setStatus("current")
_ClvSmtpAlgDnsBlName_Type = DisplayString
_ClvSmtpAlgDnsBlName_Object = MibTableColumn
clvSmtpAlgDnsBlName = _ClvSmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 2),
    _ClvSmtpAlgDnsBlName_Type()
)
clvSmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlName.setStatus("current")
_ClvSmtpAlgDnsBlChecked_Type = Gauge32
_ClvSmtpAlgDnsBlChecked_Object = MibTableColumn
clvSmtpAlgDnsBlChecked = _ClvSmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 3),
    _ClvSmtpAlgDnsBlChecked_Type()
)
clvSmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlChecked.setStatus("current")
_ClvSmtpAlgDnsBlMatched_Type = Gauge32
_ClvSmtpAlgDnsBlMatched_Object = MibTableColumn
clvSmtpAlgDnsBlMatched = _ClvSmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 4),
    _ClvSmtpAlgDnsBlMatched_Type()
)
clvSmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlMatched.setStatus("current")
_ClvSmtpAlgDnsBlFailChecks_Type = Gauge32
_ClvSmtpAlgDnsBlFailChecks_Object = MibTableColumn
clvSmtpAlgDnsBlFailChecks = _ClvSmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 5),
    _ClvSmtpAlgDnsBlFailChecks_Type()
)
clvSmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlFailChecks.setStatus("current")
_ClvDHCPRelay_ObjectIdentity = ObjectIdentity
clvDHCPRelay = _ClvDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11)
)
_ClvDHCPRelayCurClients_Type = Gauge32
_ClvDHCPRelayCurClients_Object = MibScalar
clvDHCPRelayCurClients = _ClvDHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 1),
    _ClvDHCPRelayCurClients_Type()
)
clvDHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayCurClients.setStatus("current")
_ClvDHCPRelayCurTrans_Type = Gauge32
_ClvDHCPRelayCurTrans_Object = MibScalar
clvDHCPRelayCurTrans = _ClvDHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 2),
    _ClvDHCPRelayCurTrans_Type()
)
clvDHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayCurTrans.setStatus("current")
_ClvDHCPRelayRejected_Type = Gauge32
_ClvDHCPRelayRejected_Object = MibScalar
clvDHCPRelayRejected = _ClvDHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 3),
    _ClvDHCPRelayRejected_Type()
)
clvDHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRejected.setStatus("current")
_ClvDHCPRelayRuleTable_Object = MibTable
clvDHCPRelayRuleTable = _ClvDHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    clvDHCPRelayRuleTable.setStatus("current")
_ClvDHCPRelayRuleEntry_Object = MibTableRow
clvDHCPRelayRuleEntry = _ClvDHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1)
)
clvDHCPRelayRuleEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvDHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    clvDHCPRelayRuleEntry.setStatus("current")


class _ClvDHCPRelayRuleIndex_Type(Integer32):
    """Custom type clvDHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvDHCPRelayRuleIndex_Type.__name__ = "Integer32"
_ClvDHCPRelayRuleIndex_Object = MibTableColumn
clvDHCPRelayRuleIndex = _ClvDHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 1),
    _ClvDHCPRelayRuleIndex_Type()
)
clvDHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleIndex.setStatus("current")
_ClvDHCPRelayRuleName_Type = DisplayString
_ClvDHCPRelayRuleName_Object = MibTableColumn
clvDHCPRelayRuleName = _ClvDHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 2),
    _ClvDHCPRelayRuleName_Type()
)
clvDHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleName.setStatus("current")
_ClvDHCPRelayRuleHits_Type = Gauge32
_ClvDHCPRelayRuleHits_Object = MibTableColumn
clvDHCPRelayRuleHits = _ClvDHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 3),
    _ClvDHCPRelayRuleHits_Type()
)
clvDHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleHits.setStatus("current")
_ClvDHCPRelayRuleCurClients_Type = Gauge32
_ClvDHCPRelayRuleCurClients_Object = MibTableColumn
clvDHCPRelayRuleCurClients = _ClvDHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 4),
    _ClvDHCPRelayRuleCurClients_Type()
)
clvDHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleCurClients.setStatus("current")
_ClvDHCPRelayRuleRejCliPkts_Type = Gauge32
_ClvDHCPRelayRuleRejCliPkts_Object = MibTableColumn
clvDHCPRelayRuleRejCliPkts = _ClvDHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 5),
    _ClvDHCPRelayRuleRejCliPkts_Type()
)
clvDHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleRejCliPkts.setStatus("current")
_ClvDHCPRelayRuleRejSrvPkts_Type = Gauge32
_ClvDHCPRelayRuleRejSrvPkts_Object = MibTableColumn
clvDHCPRelayRuleRejSrvPkts = _ClvDHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 6),
    _ClvDHCPRelayRuleRejSrvPkts_Type()
)
clvDHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleRejSrvPkts.setStatus("current")
_ClvHA_ObjectIdentity = ObjectIdentity
clvHA = _ClvHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12)
)
_ClvHASyncSendQueueLength_Type = Gauge32
_ClvHASyncSendQueueLength_Object = MibScalar
clvHASyncSendQueueLength = _ClvHASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 1),
    _ClvHASyncSendQueueLength_Type()
)
clvHASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendQueueLength.setStatus("current")
_ClvHASyncSendQueueUsagePackets_Type = Gauge32
_ClvHASyncSendQueueUsagePackets_Object = MibScalar
clvHASyncSendQueueUsagePackets = _ClvHASyncSendQueueUsagePackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 2),
    _ClvHASyncSendQueueUsagePackets_Type()
)
clvHASyncSendQueueUsagePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendQueueUsagePackets.setStatus("current")
_ClvHASyncSendQueueUsageOctects_Type = Gauge32
_ClvHASyncSendQueueUsageOctects_Object = MibScalar
clvHASyncSendQueueUsageOctects = _ClvHASyncSendQueueUsageOctects_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 3),
    _ClvHASyncSendQueueUsageOctects_Type()
)
clvHASyncSendQueueUsageOctects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendQueueUsageOctects.setStatus("current")
_ClvHASyncSentPackets_Type = Counter32
_ClvHASyncSentPackets_Object = MibScalar
clvHASyncSentPackets = _ClvHASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 4),
    _ClvHASyncSentPackets_Type()
)
clvHASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSentPackets.setStatus("current")
_ClvHASyncSendResentPackets_Type = Counter32
_ClvHASyncSendResentPackets_Object = MibScalar
clvHASyncSendResentPackets = _ClvHASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 5),
    _ClvHASyncSendResentPackets_Type()
)
clvHASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendResentPackets.setStatus("current")
_ClavisterStatsConformance_ObjectIdentity = ObjectIdentity
clavisterStatsConformance = _ClavisterStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 2, 1)
)
_ClavisterStatsRegGroups_ObjectIdentity = ObjectIdentity
clavisterStatsRegGroups = _ClavisterStatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1)
)

# Managed Objects groups

clvSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 1)
)
clvSystemObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSysCpuLoad"),
        ("CLAVISTER-MIB", "clvSysForwardedBits"),
        ("CLAVISTER-MIB", "clvSysForwardedPackets"),
        ("CLAVISTER-MIB", "clvSysBuffUse"),
        ("CLAVISTER-MIB", "clvSysConns"),
        ("CLAVISTER-MIB", "clvHWSensorName"),
        ("CLAVISTER-MIB", "clvHWSensorValue"),
        ("CLAVISTER-MIB", "clvHWSensorUnit"),
        ("CLAVISTER-MIB", "clvSysMemUsage"),
        ("CLAVISTER-MIB", "clvSysTimerUsage"))
)
if mibBuilder.loadTexts:
    clvSystemObjectGroup.setStatus("current")

clvIPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 2)
)
clvIPsecObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIPsecPhaseOneActive"),
        ("CLAVISTER-MIB", "clvIPsecPhaseOneAggrModeDone"),
        ("CLAVISTER-MIB", "clvIPsecQuickModeActive"),
        ("CLAVISTER-MIB", "clvIPsecPhaseOneDone"),
        ("CLAVISTER-MIB", "clvIPsecPhaseOneFailed"),
        ("CLAVISTER-MIB", "clvIPsecPhaseOneRekeyed"),
        ("CLAVISTER-MIB", "clvIPsecQuickModeDone"),
        ("CLAVISTER-MIB", "clvIPsecQuickModeFailed"),
        ("CLAVISTER-MIB", "clvIPsecInfoDone"),
        ("CLAVISTER-MIB", "clvIPsecInfoFailed"),
        ("CLAVISTER-MIB", "clvIPsecInOctetsComp"),
        ("CLAVISTER-MIB", "clvIPsecInOctetsUncomp"),
        ("CLAVISTER-MIB", "clvIPsecOutOctetsComp"),
        ("CLAVISTER-MIB", "clvIPsecOutOctetsUncomp"),
        ("CLAVISTER-MIB", "clvIPsecForwardedOctetsComp"),
        ("CLAVISTER-MIB", "clvIPsecForwardedOctetsUcomp"),
        ("CLAVISTER-MIB", "clvIPsecInPackets"),
        ("CLAVISTER-MIB", "clvIPsecOutPackets"),
        ("CLAVISTER-MIB", "clvIPsecForwardedPackets"),
        ("CLAVISTER-MIB", "clvIPsecActiveTransforms"),
        ("CLAVISTER-MIB", "clvIPsecTotalTransforms"),
        ("CLAVISTER-MIB", "clvIPsecOutOfTransforms"),
        ("CLAVISTER-MIB", "clvIPsecTotalRekeys"))
)
if mibBuilder.loadTexts:
    clvIPsecObjectGroup.setStatus("current")

clvStateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 3)
)
clvStateCountersGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSysPscTcpSyn"),
        ("CLAVISTER-MIB", "clvSysPscTcpOpen"),
        ("CLAVISTER-MIB", "clvSysPscTcpFin"),
        ("CLAVISTER-MIB", "clvSysPscUdp"),
        ("CLAVISTER-MIB", "clvSysPscIcmp"),
        ("CLAVISTER-MIB", "clvSysPscOther"))
)
if mibBuilder.loadTexts:
    clvStateCountersGroup.setStatus("current")

clvIPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 4)
)
clvIPPoolGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIPPoolsNumber"),
        ("CLAVISTER-MIB", "clvIPPoolName"),
        ("CLAVISTER-MIB", "clvIPPoolPrepare"),
        ("CLAVISTER-MIB", "clvIPPoolFree"),
        ("CLAVISTER-MIB", "clvIPPoolMisses"),
        ("CLAVISTER-MIB", "clvIPPoolClientFails"),
        ("CLAVISTER-MIB", "clvIPPoolUsed"))
)
if mibBuilder.loadTexts:
    clvIPPoolGroup.setStatus("current")

clvDHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 5)
)
clvDHCPServerGroup.setObjects(
      *(("CLAVISTER-MIB", "clvDHCPTotalRejected"),
        ("CLAVISTER-MIB", "clvDHCPRuleName"),
        ("CLAVISTER-MIB", "clvDHCPRuleUsage"),
        ("CLAVISTER-MIB", "clvDHCPRuleUsagePercent"),
        ("CLAVISTER-MIB", "clvDHCPActiveClients"),
        ("CLAVISTER-MIB", "clvDHCPActiveClientsPercent"),
        ("CLAVISTER-MIB", "clvDHCPRejectedRequests"),
        ("CLAVISTER-MIB", "clvDHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    clvDHCPServerGroup.setStatus("current")

clvRuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 6)
)
clvRuleUseGroup.setObjects(
      *(("CLAVISTER-MIB", "clvRuleName"),
        ("CLAVISTER-MIB", "clvRuleUse"))
)
if mibBuilder.loadTexts:
    clvRuleUseGroup.setStatus("current")

clvUserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 7)
)
clvUserAuthGroup.setObjects(
      *(("CLAVISTER-MIB", "clvUserAuthHTTPUsers"),
        ("CLAVISTER-MIB", "clvUserAuthXAUTHUsers"),
        ("CLAVISTER-MIB", "clvUserAuthHTTPSUsers"),
        ("CLAVISTER-MIB", "clvUserAuthPPPUsers"),
        ("CLAVISTER-MIB", "clvUserAuthEAPUsers"),
        ("CLAVISTER-MIB", "clvUserAuthRuleName"),
        ("CLAVISTER-MIB", "clvUserAuthRuleUse"))
)
if mibBuilder.loadTexts:
    clvUserAuthGroup.setStatus("current")

clvIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 8)
)
clvIfStatsGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIfName"),
        ("CLAVISTER-MIB", "clvIfFragsIn"),
        ("CLAVISTER-MIB", "clvIfFragReassOk"),
        ("CLAVISTER-MIB", "clvIfFragReassFail"),
        ("CLAVISTER-MIB", "clvIfPktsInCnt"),
        ("CLAVISTER-MIB", "clvIfPktsOutCnt"),
        ("CLAVISTER-MIB", "clvIfBitsInCnt"),
        ("CLAVISTER-MIB", "clvIfBitsOutCnt"),
        ("CLAVISTER-MIB", "clvIfPktsTotCnt"),
        ("CLAVISTER-MIB", "clvIfBitsTotCnt"),
        ("CLAVISTER-MIB", "clvIfRxRingFifoErrors"),
        ("CLAVISTER-MIB", "clvIfRxDespools"),
        ("CLAVISTER-MIB", "clvIfRxAvgUse"),
        ("CLAVISTER-MIB", "clvIfRxRingSaturation"),
        ("CLAVISTER-MIB", "clvRxRingFlooded"),
        ("CLAVISTER-MIB", "clvIfTxDespools"),
        ("CLAVISTER-MIB", "clvIfTxAvgUse"),
        ("CLAVISTER-MIB", "clvIfTxRingSaturation"),
        ("CLAVISTER-MIB", "clvRxTingFlooded"))
)
if mibBuilder.loadTexts:
    clvIfStatsGroup.setStatus("current")

clvLinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 9)
)
clvLinkMonitorGroup.setObjects(
      *(("CLAVISTER-MIB", "clvLinkMonGrp"),
        ("CLAVISTER-MIB", "clvLinkMonGrpName"),
        ("CLAVISTER-MIB", "clvLinkMonGrpHostsUp"),
        ("CLAVISTER-MIB", "clvLinkMonHostId"),
        ("CLAVISTER-MIB", "clvLinkMonHostShortTermLoss"),
        ("CLAVISTER-MIB", "clvLinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    clvLinkMonitorGroup.setStatus("current")

clvPipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 10)
)
clvPipesObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvPipeUsers"),
        ("CLAVISTER-MIB", "clvPipeName"),
        ("CLAVISTER-MIB", "clvPipeMinPrec"),
        ("CLAVISTER-MIB", "clvPipeMaxPrec"),
        ("CLAVISTER-MIB", "clvPipeDefPrec"),
        ("CLAVISTER-MIB", "clvPipeNumPrec"),
        ("CLAVISTER-MIB", "clvPipeNumUsers"),
        ("CLAVISTER-MIB", "clvPipeCurrentBps"),
        ("CLAVISTER-MIB", "clvPipeCurrentPps"),
        ("CLAVISTER-MIB", "clvPipeDelayedPackets"),
        ("CLAVISTER-MIB", "clvPipeDropedPackets"),
        ("CLAVISTER-MIB", "clvPipePrec"),
        ("CLAVISTER-MIB", "clvPipePrecBps"),
        ("CLAVISTER-MIB", "clvPipePrecTotalPps"),
        ("CLAVISTER-MIB", "clvPipePrecReservedBps"),
        ("CLAVISTER-MIB", "clvPipePrecDynLimBps"),
        ("CLAVISTER-MIB", "clvPipePrecDynUsrLimBps"),
        ("CLAVISTER-MIB", "clvPipePrecDelayedPackets"),
        ("CLAVISTER-MIB", "clvPipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    clvPipesObjectGroup.setStatus("current")

clvDHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 12)
)
clvDHCPRelayObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvDHCPRelayCurClients"),
        ("CLAVISTER-MIB", "clvDHCPRelayCurTrans"),
        ("CLAVISTER-MIB", "clvDHCPRelayRejected"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleName"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleHits"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleCurClients"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleRejCliPkts"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    clvDHCPRelayObjectGroup.setStatus("current")

clvAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 13)
)
clvAlgGroup.setObjects(
      *(("CLAVISTER-MIB", "clvAlgSessions"),
        ("CLAVISTER-MIB", "clvAlgConnections"),
        ("CLAVISTER-MIB", "clvAlgTCPStreams"),
        ("CLAVISTER-MIB", "clvHttpAlgName"),
        ("CLAVISTER-MIB", "clvHttpAlgTotalRequested"),
        ("CLAVISTER-MIB", "clvHttpAlgTotalAllowed"),
        ("CLAVISTER-MIB", "clvHttpAlgTotalBlocked"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltName"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltRequests"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltAllowed"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    clvAlgGroup.setStatus("current")

clvHAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 14)
)
clvHAGroup.setObjects(
      *(("CLAVISTER-MIB", "clvHASyncSendQueueLength"),
        ("CLAVISTER-MIB", "clvHASyncSendQueueUsagePackets"),
        ("CLAVISTER-MIB", "clvHASyncSendQueueUsageOctects"),
        ("CLAVISTER-MIB", "clvHASyncSentPackets"),
        ("CLAVISTER-MIB", "clvHASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    clvHAGroup.setStatus("current")

clvIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 15)
)
clvIfVlanGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIfVlanUntaggedInPkts"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedOutPkts"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedTotPkts"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedInOctets"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedOutOctets"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    clvIfVlanGroup.setStatus("current")

clvSmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 16)
)
clvSmtpAlgGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSmtpAlgName"),
        ("CLAVISTER-MIB", "clvSmtpAlgTotCheckedSes"),
        ("CLAVISTER-MIB", "clvSmtpAlgTotSpamSes"),
        ("CLAVISTER-MIB", "clvSmtpAlgTotDroppedSes"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlName"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlChecked"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlMatched"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    clvSmtpAlgGroup.setStatus("current")

clvSysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 17)
)
clvSysTCPGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSysTCPRecvSmall"),
        ("CLAVISTER-MIB", "clvSysTCPRecvLarge"),
        ("CLAVISTER-MIB", "clvSysTCPSendSmall"),
        ("CLAVISTER-MIB", "clvSysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    clvSysTCPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clavisterStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5089, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clavisterStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAVISTER-MIB",
    **{"clvSystem": clvSystem,
       "clvSysCpuLoad": clvSysCpuLoad,
       "clvSysForwardedBits": clvSysForwardedBits,
       "clvSysForwardedPackets": clvSysForwardedPackets,
       "clvSysBuffUse": clvSysBuffUse,
       "clvSysConns": clvSysConns,
       "clvSysPerStateCounters": clvSysPerStateCounters,
       "clvSysPscTcpSyn": clvSysPscTcpSyn,
       "clvSysPscTcpOpen": clvSysPscTcpOpen,
       "clvSysPscTcpFin": clvSysPscTcpFin,
       "clvSysPscUdp": clvSysPscUdp,
       "clvSysPscIcmp": clvSysPscIcmp,
       "clvSysPscOther": clvSysPscOther,
       "clvIfStatsTable": clvIfStatsTable,
       "clvIfStatsEntry": clvIfStatsEntry,
       "clvIfStatsIndex": clvIfStatsIndex,
       "clvIfName": clvIfName,
       "clvIfFragsIn": clvIfFragsIn,
       "clvIfFragReassOk": clvIfFragReassOk,
       "clvIfFragReassFail": clvIfFragReassFail,
       "clvIfPktsInCnt": clvIfPktsInCnt,
       "clvIfPktsOutCnt": clvIfPktsOutCnt,
       "clvIfBitsInCnt": clvIfBitsInCnt,
       "clvIfBitsOutCnt": clvIfBitsOutCnt,
       "clvIfPktsTotCnt": clvIfPktsTotCnt,
       "clvIfBitsTotCnt": clvIfBitsTotCnt,
       "clvIfRxRingTable": clvIfRxRingTable,
       "clvIfRxRingEntry": clvIfRxRingEntry,
       "clvIfRxRingIndex": clvIfRxRingIndex,
       "clvIfRxRingFifoErrors": clvIfRxRingFifoErrors,
       "clvIfRxDespools": clvIfRxDespools,
       "clvIfRxAvgUse": clvIfRxAvgUse,
       "clvIfRxRingSaturation": clvIfRxRingSaturation,
       "clvRxRingFlooded": clvRxRingFlooded,
       "clvIfTxRingTable": clvIfTxRingTable,
       "clvIfTxRingEntry": clvIfTxRingEntry,
       "clvIfTxRingIndex": clvIfTxRingIndex,
       "clvIfTxDespools": clvIfTxDespools,
       "clvIfTxAvgUse": clvIfTxAvgUse,
       "clvIfTxRingSaturation": clvIfTxRingSaturation,
       "clvRxTingFlooded": clvRxTingFlooded,
       "clvIfVlanStatsTable": clvIfVlanStatsTable,
       "clvIfVlanStatsEntry": clvIfVlanStatsEntry,
       "clvIfVlanIndex": clvIfVlanIndex,
       "clvIfVlanUntaggedInPkts": clvIfVlanUntaggedInPkts,
       "clvIfVlanUntaggedOutPkts": clvIfVlanUntaggedOutPkts,
       "clvIfVlanUntaggedTotPkts": clvIfVlanUntaggedTotPkts,
       "clvIfVlanUntaggedInOctets": clvIfVlanUntaggedInOctets,
       "clvIfVlanUntaggedOutOctets": clvIfVlanUntaggedOutOctets,
       "clvIfVlanUntaggedTotOctets": clvIfVlanUntaggedTotOctets,
       "clvHWSensorTable": clvHWSensorTable,
       "clvHWSensorEntry": clvHWSensorEntry,
       "clvHWSensorIndex": clvHWSensorIndex,
       "clvHWSensorName": clvHWSensorName,
       "clvHWSensorValue": clvHWSensorValue,
       "clvHWSensorUnit": clvHWSensorUnit,
       "clvSysMemUsage": clvSysMemUsage,
       "clvSysTCPUsage": clvSysTCPUsage,
       "clvSysTCPRecvSmall": clvSysTCPRecvSmall,
       "clvSysTCPRecvLarge": clvSysTCPRecvLarge,
       "clvSysTCPSendSmall": clvSysTCPSendSmall,
       "clvSysTCPSendLarge": clvSysTCPSendLarge,
       "clvSysTimerUsage": clvSysTimerUsage,
       "clvVPN": clvVPN,
       "clvIPsec": clvIPsec,
       "clvIPsecGlobal": clvIPsecGlobal,
       "clvIPsecPhaseOneActive": clvIPsecPhaseOneActive,
       "clvIPsecPhaseOneAggrModeDone": clvIPsecPhaseOneAggrModeDone,
       "clvIPsecQuickModeActive": clvIPsecQuickModeActive,
       "clvIPsecPhaseOneDone": clvIPsecPhaseOneDone,
       "clvIPsecPhaseOneFailed": clvIPsecPhaseOneFailed,
       "clvIPsecPhaseOneRekeyed": clvIPsecPhaseOneRekeyed,
       "clvIPsecQuickModeDone": clvIPsecQuickModeDone,
       "clvIPsecQuickModeFailed": clvIPsecQuickModeFailed,
       "clvIPsecInfoDone": clvIPsecInfoDone,
       "clvIPsecInfoFailed": clvIPsecInfoFailed,
       "clvIPsecInOctetsComp": clvIPsecInOctetsComp,
       "clvIPsecInOctetsUncomp": clvIPsecInOctetsUncomp,
       "clvIPsecOutOctetsComp": clvIPsecOutOctetsComp,
       "clvIPsecOutOctetsUncomp": clvIPsecOutOctetsUncomp,
       "clvIPsecForwardedOctetsComp": clvIPsecForwardedOctetsComp,
       "clvIPsecForwardedOctetsUcomp": clvIPsecForwardedOctetsUcomp,
       "clvIPsecInPackets": clvIPsecInPackets,
       "clvIPsecOutPackets": clvIPsecOutPackets,
       "clvIPsecForwardedPackets": clvIPsecForwardedPackets,
       "clvIPsecActiveTransforms": clvIPsecActiveTransforms,
       "clvIPsecTotalTransforms": clvIPsecTotalTransforms,
       "clvIPsecOutOfTransforms": clvIPsecOutOfTransforms,
       "clvIPsecTotalRekeys": clvIPsecTotalRekeys,
       "clvRules": clvRules,
       "clvRuleUseTable": clvRuleUseTable,
       "clvRuleUseEntry": clvRuleUseEntry,
       "clvRuleIndex": clvRuleIndex,
       "clvRuleName": clvRuleName,
       "clvRuleUse": clvRuleUse,
       "clvIPPools": clvIPPools,
       "clvIPPoolsNumber": clvIPPoolsNumber,
       "clvIPPoolTable": clvIPPoolTable,
       "clvIPPoolEntry": clvIPPoolEntry,
       "clvIPPoolIndex": clvIPPoolIndex,
       "clvIPPoolName": clvIPPoolName,
       "clvIPPoolPrepare": clvIPPoolPrepare,
       "clvIPPoolFree": clvIPPoolFree,
       "clvIPPoolMisses": clvIPPoolMisses,
       "clvIPPoolClientFails": clvIPPoolClientFails,
       "clvIPPoolUsed": clvIPPoolUsed,
       "clvDHCPServer": clvDHCPServer,
       "clvDHCPTotalRejected": clvDHCPTotalRejected,
       "clvDHCPRuleTable": clvDHCPRuleTable,
       "clvDHCPRuleEntry": clvDHCPRuleEntry,
       "clvDHCPRuleIndex": clvDHCPRuleIndex,
       "clvDHCPRuleName": clvDHCPRuleName,
       "clvDHCPRuleUsage": clvDHCPRuleUsage,
       "clvDHCPRuleUsagePercent": clvDHCPRuleUsagePercent,
       "clvDHCPActiveClients": clvDHCPActiveClients,
       "clvDHCPActiveClientsPercent": clvDHCPActiveClientsPercent,
       "clvDHCPRejectedRequests": clvDHCPRejectedRequests,
       "clvDHCPTotalLeases": clvDHCPTotalLeases,
       "clvUserAuth": clvUserAuth,
       "clvUserAuthHTTPUsers": clvUserAuthHTTPUsers,
       "clvUserAuthXAUTHUsers": clvUserAuthXAUTHUsers,
       "clvUserAuthHTTPSUsers": clvUserAuthHTTPSUsers,
       "clvUserAuthPPPUsers": clvUserAuthPPPUsers,
       "clvUserAuthEAPUsers": clvUserAuthEAPUsers,
       "clvUserAuthRuleUseTable": clvUserAuthRuleUseTable,
       "clvUserAuthRuleUseEntry": clvUserAuthRuleUseEntry,
       "clvUserAuthRuleIndex": clvUserAuthRuleIndex,
       "clvUserAuthRuleName": clvUserAuthRuleName,
       "clvUserAuthRuleUse": clvUserAuthRuleUse,
       "clvLinkMonitor": clvLinkMonitor,
       "clvLinkMonGrp": clvLinkMonGrp,
       "clvLinkMonGrpTable": clvLinkMonGrpTable,
       "clvLinkMonGrpEntry": clvLinkMonGrpEntry,
       "clvLinkMonGrpIndex": clvLinkMonGrpIndex,
       "clvLinkMonGrpName": clvLinkMonGrpName,
       "clvLinkMonGrpHostsUp": clvLinkMonGrpHostsUp,
       "clvLinkMonHostTable": clvLinkMonHostTable,
       "clvLinkMonHostEntry": clvLinkMonHostEntry,
       "clvLinkMonHostIndex": clvLinkMonHostIndex,
       "clvLinkMonHostId": clvLinkMonHostId,
       "clvLinkMonHostShortTermLoss": clvLinkMonHostShortTermLoss,
       "clvLinkMonHostPacketsLost": clvLinkMonHostPacketsLost,
       "clvPipes": clvPipes,
       "clvPipeUsers": clvPipeUsers,
       "clvPipeTable": clvPipeTable,
       "clvPipeEntry": clvPipeEntry,
       "clvPipeIndex": clvPipeIndex,
       "clvPipeName": clvPipeName,
       "clvPipeMinPrec": clvPipeMinPrec,
       "clvPipeMaxPrec": clvPipeMaxPrec,
       "clvPipeDefPrec": clvPipeDefPrec,
       "clvPipeNumPrec": clvPipeNumPrec,
       "clvPipeNumUsers": clvPipeNumUsers,
       "clvPipeCurrentBps": clvPipeCurrentBps,
       "clvPipeCurrentPps": clvPipeCurrentPps,
       "clvPipeDelayedPackets": clvPipeDelayedPackets,
       "clvPipeDropedPackets": clvPipeDropedPackets,
       "clvPipePrecTable": clvPipePrecTable,
       "clvPipePrecEntry": clvPipePrecEntry,
       "clvPipePrecIndex": clvPipePrecIndex,
       "clvPipePrec": clvPipePrec,
       "clvPipePrecBps": clvPipePrecBps,
       "clvPipePrecTotalPps": clvPipePrecTotalPps,
       "clvPipePrecReservedBps": clvPipePrecReservedBps,
       "clvPipePrecDynLimBps": clvPipePrecDynLimBps,
       "clvPipePrecDynUsrLimBps": clvPipePrecDynUsrLimBps,
       "clvPipePrecDelayedPackets": clvPipePrecDelayedPackets,
       "clvPipePrecDropedPackets": clvPipePrecDropedPackets,
       "clvALG": clvALG,
       "clvAlgSessions": clvAlgSessions,
       "clvAlgConnections": clvAlgConnections,
       "clvAlgTCPStreams": clvAlgTCPStreams,
       "clvHttpAlg": clvHttpAlg,
       "clvHttpAlgTable": clvHttpAlgTable,
       "clvHttpAlgEntry": clvHttpAlgEntry,
       "clvHttpAlgIndex": clvHttpAlgIndex,
       "clvHttpAlgName": clvHttpAlgName,
       "clvHttpAlgTotalRequested": clvHttpAlgTotalRequested,
       "clvHttpAlgTotalAllowed": clvHttpAlgTotalAllowed,
       "clvHttpAlgTotalBlocked": clvHttpAlgTotalBlocked,
       "clvHttpAlgCntFltTable": clvHttpAlgCntFltTable,
       "clvHttpAlgCntFltEntry": clvHttpAlgCntFltEntry,
       "clvHttpAlgCntFltIndex": clvHttpAlgCntFltIndex,
       "clvHttpAlgCntFltName": clvHttpAlgCntFltName,
       "clvHttpAlgCntFltRequests": clvHttpAlgCntFltRequests,
       "clvHttpAlgCntFltAllowed": clvHttpAlgCntFltAllowed,
       "clvHttpAlgCntFltBlocked": clvHttpAlgCntFltBlocked,
       "clvSmtpAlg": clvSmtpAlg,
       "clvSmtpAlgTable": clvSmtpAlgTable,
       "clvSmtpAlgEntry": clvSmtpAlgEntry,
       "clvSmtpAlgIndex": clvSmtpAlgIndex,
       "clvSmtpAlgName": clvSmtpAlgName,
       "clvSmtpAlgTotCheckedSes": clvSmtpAlgTotCheckedSes,
       "clvSmtpAlgTotSpamSes": clvSmtpAlgTotSpamSes,
       "clvSmtpAlgTotDroppedSes": clvSmtpAlgTotDroppedSes,
       "clvSmtpAlgDnsBlTable": clvSmtpAlgDnsBlTable,
       "clvSmtpAlgDnsBlEntry": clvSmtpAlgDnsBlEntry,
       "clvSmtpAlgDnsBlIndex": clvSmtpAlgDnsBlIndex,
       "clvSmtpAlgDnsBlName": clvSmtpAlgDnsBlName,
       "clvSmtpAlgDnsBlChecked": clvSmtpAlgDnsBlChecked,
       "clvSmtpAlgDnsBlMatched": clvSmtpAlgDnsBlMatched,
       "clvSmtpAlgDnsBlFailChecks": clvSmtpAlgDnsBlFailChecks,
       "clvDHCPRelay": clvDHCPRelay,
       "clvDHCPRelayCurClients": clvDHCPRelayCurClients,
       "clvDHCPRelayCurTrans": clvDHCPRelayCurTrans,
       "clvDHCPRelayRejected": clvDHCPRelayRejected,
       "clvDHCPRelayRuleTable": clvDHCPRelayRuleTable,
       "clvDHCPRelayRuleEntry": clvDHCPRelayRuleEntry,
       "clvDHCPRelayRuleIndex": clvDHCPRelayRuleIndex,
       "clvDHCPRelayRuleName": clvDHCPRelayRuleName,
       "clvDHCPRelayRuleHits": clvDHCPRelayRuleHits,
       "clvDHCPRelayRuleCurClients": clvDHCPRelayRuleCurClients,
       "clvDHCPRelayRuleRejCliPkts": clvDHCPRelayRuleRejCliPkts,
       "clvDHCPRelayRuleRejSrvPkts": clvDHCPRelayRuleRejSrvPkts,
       "clvHA": clvHA,
       "clvHASyncSendQueueLength": clvHASyncSendQueueLength,
       "clvHASyncSendQueueUsagePackets": clvHASyncSendQueueUsagePackets,
       "clvHASyncSendQueueUsageOctects": clvHASyncSendQueueUsageOctects,
       "clvHASyncSentPackets": clvHASyncSentPackets,
       "clvHASyncSendResentPackets": clvHASyncSendResentPackets,
       "clavisterStatsMibModule": clavisterStatsMibModule,
       "clavisterStatsConformance": clavisterStatsConformance,
       "clavisterStatsCompliance": clavisterStatsCompliance,
       "clavisterStatsRegGroups": clavisterStatsRegGroups,
       "clvSystemObjectGroup": clvSystemObjectGroup,
       "clvIPsecObjectGroup": clvIPsecObjectGroup,
       "clvStateCountersGroup": clvStateCountersGroup,
       "clvIPPoolGroup": clvIPPoolGroup,
       "clvDHCPServerGroup": clvDHCPServerGroup,
       "clvRuleUseGroup": clvRuleUseGroup,
       "clvUserAuthGroup": clvUserAuthGroup,
       "clvIfStatsGroup": clvIfStatsGroup,
       "clvLinkMonitorGroup": clvLinkMonitorGroup,
       "clvPipesObjectGroup": clvPipesObjectGroup,
       "clvDHCPRelayObjectGroup": clvDHCPRelayObjectGroup,
       "clvAlgGroup": clvAlgGroup,
       "clvHAGroup": clvHAGroup,
       "clvIfVlanGroup": clvIfVlanGroup,
       "clvSmtpAlgGroup": clvSmtpAlgGroup,
       "clvSysTCPGroup": clvSysTCPGroup}
)
