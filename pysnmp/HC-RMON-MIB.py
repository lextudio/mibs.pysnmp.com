# SNMP MIB module (HC-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HC-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:25 2024
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

(CounterBasedGauge64,
 ZeroBasedCounter64) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64",
    "ZeroBasedCounter64")

(OwnerString,
 capture,
 captureBufferControlIndex,
 captureBufferIndex,
 etherHistoryIndex,
 etherHistorySampleIndex,
 etherStatsIndex,
 history,
 hostAddress,
 hostIndex,
 hostTimeCreationOrder,
 hostTimeIndex,
 hostTopN,
 hostTopNIndex,
 hostTopNReport,
 hosts,
 matrix,
 matrixDSDestAddress,
 matrixDSIndex,
 matrixDSSourceAddress,
 matrixSDDestAddress,
 matrixSDIndex,
 matrixSDSourceAddress,
 rmon,
 statistics) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "capture",
    "captureBufferControlIndex",
    "captureBufferIndex",
    "etherHistoryIndex",
    "etherHistorySampleIndex",
    "etherStatsIndex",
    "history",
    "hostAddress",
    "hostIndex",
    "hostTimeCreationOrder",
    "hostTimeIndex",
    "hostTopN",
    "hostTopNIndex",
    "hostTopNReport",
    "hosts",
    "matrix",
    "matrixDSDestAddress",
    "matrixDSIndex",
    "matrixDSSourceAddress",
    "matrixSDDestAddress",
    "matrixSDIndex",
    "matrixSDSourceAddress",
    "rmon",
    "statistics")

(rmonConformance,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "rmonConformance")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hcRMON = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 5)
)
hcRMON.setRevisions(
        ("2002-05-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtherStatsHighCapacityTable_Object = MibTable
etherStatsHighCapacityTable = _EtherStatsHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7)
)
if mibBuilder.loadTexts:
    etherStatsHighCapacityTable.setStatus("current")
_EtherStatsHighCapacityEntry_Object = MibTableRow
etherStatsHighCapacityEntry = _EtherStatsHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1)
)
etherStatsHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    etherStatsHighCapacityEntry.setStatus("current")
_EtherStatsHighCapacityOverflowPkts_Type = Counter32
_EtherStatsHighCapacityOverflowPkts_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts = _EtherStatsHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 1),
    _EtherStatsHighCapacityOverflowPkts_Type()
)
etherStatsHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts.setUnits("Packets")
_EtherStatsHighCapacityPkts_Type = Counter64
_EtherStatsHighCapacityPkts_Object = MibTableColumn
etherStatsHighCapacityPkts = _EtherStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 2),
    _EtherStatsHighCapacityPkts_Type()
)
etherStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts.setUnits("Packets")
_EtherStatsHighCapacityOverflowOctets_Type = Counter32
_EtherStatsHighCapacityOverflowOctets_Object = MibTableColumn
etherStatsHighCapacityOverflowOctets = _EtherStatsHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 3),
    _EtherStatsHighCapacityOverflowOctets_Type()
)
etherStatsHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowOctets.setUnits("Octets")
_EtherStatsHighCapacityOctets_Type = Counter64
_EtherStatsHighCapacityOctets_Object = MibTableColumn
etherStatsHighCapacityOctets = _EtherStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 4),
    _EtherStatsHighCapacityOctets_Type()
)
etherStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOctets.setUnits("Octets")
_EtherStatsHighCapacityOverflowPkts64Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts64Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts64Octets = _EtherStatsHighCapacityOverflowPkts64Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 5),
    _EtherStatsHighCapacityOverflowPkts64Octets_Type()
)
etherStatsHighCapacityOverflowPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts64Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts64Octets_Type = Counter64
_EtherStatsHighCapacityPkts64Octets_Object = MibTableColumn
etherStatsHighCapacityPkts64Octets = _EtherStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 6),
    _EtherStatsHighCapacityPkts64Octets_Type()
)
etherStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts64Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts65to127Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts65to127Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts65to127Octets = _EtherStatsHighCapacityOverflowPkts65to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 7),
    _EtherStatsHighCapacityOverflowPkts65to127Octets_Type()
)
etherStatsHighCapacityOverflowPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts65to127Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts65to127Octets_Type = Counter64
_EtherStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
etherStatsHighCapacityPkts65to127Octets = _EtherStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 8),
    _EtherStatsHighCapacityPkts65to127Octets_Type()
)
etherStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts65to127Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts128to255Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts128to255Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts128to255Octets = _EtherStatsHighCapacityOverflowPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 9),
    _EtherStatsHighCapacityOverflowPkts128to255Octets_Type()
)
etherStatsHighCapacityOverflowPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts128to255Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts128to255Octets_Type = Counter64
_EtherStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
etherStatsHighCapacityPkts128to255Octets = _EtherStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 10),
    _EtherStatsHighCapacityPkts128to255Octets_Type()
)
etherStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts128to255Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts256to511Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts256to511Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts256to511Octets = _EtherStatsHighCapacityOverflowPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 11),
    _EtherStatsHighCapacityOverflowPkts256to511Octets_Type()
)
etherStatsHighCapacityOverflowPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts256to511Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts256to511Octets_Type = Counter64
_EtherStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
etherStatsHighCapacityPkts256to511Octets = _EtherStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 12),
    _EtherStatsHighCapacityPkts256to511Octets_Type()
)
etherStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts256to511Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts512to1023Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts512to1023Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts512to1023Octets = _EtherStatsHighCapacityOverflowPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 13),
    _EtherStatsHighCapacityOverflowPkts512to1023Octets_Type()
)
etherStatsHighCapacityOverflowPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts512to1023Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts512to1023Octets_Type = Counter64
_EtherStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
etherStatsHighCapacityPkts512to1023Octets = _EtherStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 14),
    _EtherStatsHighCapacityPkts512to1023Octets_Type()
)
etherStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts512to1023Octets.setUnits("Packets")
_EtherStatsHighCapacityOverflowPkts1024to1518Octets_Type = Counter32
_EtherStatsHighCapacityOverflowPkts1024to1518Octets_Object = MibTableColumn
etherStatsHighCapacityOverflowPkts1024to1518Octets = _EtherStatsHighCapacityOverflowPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 15),
    _EtherStatsHighCapacityOverflowPkts1024to1518Octets_Type()
)
etherStatsHighCapacityOverflowPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityOverflowPkts1024to1518Octets.setUnits("Packets")
_EtherStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_EtherStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
etherStatsHighCapacityPkts1024to1518Octets = _EtherStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 7, 1, 16),
    _EtherStatsHighCapacityPkts1024to1518Octets_Type()
)
etherStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsHighCapacityPkts1024to1518Octets.setUnits("Packets")
_EtherHistoryHighCapacityTable_Object = MibTable
etherHistoryHighCapacityTable = _EtherHistoryHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6)
)
if mibBuilder.loadTexts:
    etherHistoryHighCapacityTable.setStatus("current")
_EtherHistoryHighCapacityEntry_Object = MibTableRow
etherHistoryHighCapacityEntry = _EtherHistoryHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1)
)
etherHistoryHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "etherHistoryIndex"),
    (0, "RMON-MIB", "etherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    etherHistoryHighCapacityEntry.setStatus("current")
_EtherHistoryHighCapacityOverflowPkts_Type = Gauge32
_EtherHistoryHighCapacityOverflowPkts_Object = MibTableColumn
etherHistoryHighCapacityOverflowPkts = _EtherHistoryHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 1),
    _EtherHistoryHighCapacityOverflowPkts_Type()
)
etherHistoryHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowPkts.setUnits("Packets")
_EtherHistoryHighCapacityPkts_Type = CounterBasedGauge64
_EtherHistoryHighCapacityPkts_Object = MibTableColumn
etherHistoryHighCapacityPkts = _EtherHistoryHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 2),
    _EtherHistoryHighCapacityPkts_Type()
)
etherHistoryHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityPkts.setUnits("Packets")
_EtherHistoryHighCapacityOverflowOctets_Type = Gauge32
_EtherHistoryHighCapacityOverflowOctets_Object = MibTableColumn
etherHistoryHighCapacityOverflowOctets = _EtherHistoryHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 3),
    _EtherHistoryHighCapacityOverflowOctets_Type()
)
etherHistoryHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOverflowOctets.setUnits("Octets")
_EtherHistoryHighCapacityOctets_Type = CounterBasedGauge64
_EtherHistoryHighCapacityOctets_Object = MibTableColumn
etherHistoryHighCapacityOctets = _EtherHistoryHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 6, 1, 4),
    _EtherHistoryHighCapacityOctets_Type()
)
etherHistoryHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryHighCapacityOctets.setUnits("Octets")
_HostHighCapacityTable_Object = MibTable
hostHighCapacityTable = _HostHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5)
)
if mibBuilder.loadTexts:
    hostHighCapacityTable.setStatus("current")
_HostHighCapacityEntry_Object = MibTableRow
hostHighCapacityEntry = _HostHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1)
)
hostHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "hostIndex"),
    (0, "RMON-MIB", "hostAddress"),
)
if mibBuilder.loadTexts:
    hostHighCapacityEntry.setStatus("current")
_HostHighCapacityInOverflowPkts_Type = Counter32
_HostHighCapacityInOverflowPkts_Object = MibTableColumn
hostHighCapacityInOverflowPkts = _HostHighCapacityInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 1),
    _HostHighCapacityInOverflowPkts_Type()
)
hostHighCapacityInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowPkts.setUnits("Packets")
_HostHighCapacityInPkts_Type = Counter64
_HostHighCapacityInPkts_Object = MibTableColumn
hostHighCapacityInPkts = _HostHighCapacityInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 2),
    _HostHighCapacityInPkts_Type()
)
hostHighCapacityInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInPkts.setUnits("Packets")
_HostHighCapacityOutOverflowPkts_Type = Counter32
_HostHighCapacityOutOverflowPkts_Object = MibTableColumn
hostHighCapacityOutOverflowPkts = _HostHighCapacityOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 3),
    _HostHighCapacityOutOverflowPkts_Type()
)
hostHighCapacityOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowPkts.setUnits("Packets")
_HostHighCapacityOutPkts_Type = Counter64
_HostHighCapacityOutPkts_Object = MibTableColumn
hostHighCapacityOutPkts = _HostHighCapacityOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 4),
    _HostHighCapacityOutPkts_Type()
)
hostHighCapacityOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutPkts.setUnits("Packets")
_HostHighCapacityInOverflowOctets_Type = Counter32
_HostHighCapacityInOverflowOctets_Object = MibTableColumn
hostHighCapacityInOverflowOctets = _HostHighCapacityInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 5),
    _HostHighCapacityInOverflowOctets_Type()
)
hostHighCapacityInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInOverflowOctets.setUnits("Octets")
_HostHighCapacityInOctets_Type = Counter64
_HostHighCapacityInOctets_Object = MibTableColumn
hostHighCapacityInOctets = _HostHighCapacityInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 6),
    _HostHighCapacityInOctets_Type()
)
hostHighCapacityInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityInOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityInOctets.setUnits("Octets")
_HostHighCapacityOutOverflowOctets_Type = Counter32
_HostHighCapacityOutOverflowOctets_Object = MibTableColumn
hostHighCapacityOutOverflowOctets = _HostHighCapacityOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 7),
    _HostHighCapacityOutOverflowOctets_Type()
)
hostHighCapacityOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutOverflowOctets.setUnits("Octets")
_HostHighCapacityOutOctets_Type = Counter64
_HostHighCapacityOutOctets_Object = MibTableColumn
hostHighCapacityOutOctets = _HostHighCapacityOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 5, 1, 8),
    _HostHighCapacityOutOctets_Type()
)
hostHighCapacityOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostHighCapacityOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostHighCapacityOutOctets.setUnits("Octets")
_HostTimeHighCapacityTable_Object = MibTable
hostTimeHighCapacityTable = _HostTimeHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6)
)
if mibBuilder.loadTexts:
    hostTimeHighCapacityTable.setStatus("current")
_HostTimeHighCapacityEntry_Object = MibTableRow
hostTimeHighCapacityEntry = _HostTimeHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1)
)
hostTimeHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "hostTimeIndex"),
    (0, "RMON-MIB", "hostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    hostTimeHighCapacityEntry.setStatus("current")
_HostTimeHighCapacityInOverflowPkts_Type = Counter32
_HostTimeHighCapacityInOverflowPkts_Object = MibTableColumn
hostTimeHighCapacityInOverflowPkts = _HostTimeHighCapacityInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 1),
    _HostTimeHighCapacityInOverflowPkts_Type()
)
hostTimeHighCapacityInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowPkts.setUnits("Packets")
_HostTimeHighCapacityInPkts_Type = Counter64
_HostTimeHighCapacityInPkts_Object = MibTableColumn
hostTimeHighCapacityInPkts = _HostTimeHighCapacityInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 2),
    _HostTimeHighCapacityInPkts_Type()
)
hostTimeHighCapacityInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInPkts.setUnits("Packets")
_HostTimeHighCapacityOutOverflowPkts_Type = Counter32
_HostTimeHighCapacityOutOverflowPkts_Object = MibTableColumn
hostTimeHighCapacityOutOverflowPkts = _HostTimeHighCapacityOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 3),
    _HostTimeHighCapacityOutOverflowPkts_Type()
)
hostTimeHighCapacityOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowPkts.setUnits("Packets")
_HostTimeHighCapacityOutPkts_Type = Counter64
_HostTimeHighCapacityOutPkts_Object = MibTableColumn
hostTimeHighCapacityOutPkts = _HostTimeHighCapacityOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 4),
    _HostTimeHighCapacityOutPkts_Type()
)
hostTimeHighCapacityOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutPkts.setUnits("Packets")
_HostTimeHighCapacityInOverflowOctets_Type = Counter32
_HostTimeHighCapacityInOverflowOctets_Object = MibTableColumn
hostTimeHighCapacityInOverflowOctets = _HostTimeHighCapacityInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 5),
    _HostTimeHighCapacityInOverflowOctets_Type()
)
hostTimeHighCapacityInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOverflowOctets.setUnits("Octets")
_HostTimeHighCapacityInOctets_Type = Counter64
_HostTimeHighCapacityInOctets_Object = MibTableColumn
hostTimeHighCapacityInOctets = _HostTimeHighCapacityInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 6),
    _HostTimeHighCapacityInOctets_Type()
)
hostTimeHighCapacityInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityInOctets.setUnits("Octets")
_HostTimeHighCapacityOutOverflowOctets_Type = Counter32
_HostTimeHighCapacityOutOverflowOctets_Object = MibTableColumn
hostTimeHighCapacityOutOverflowOctets = _HostTimeHighCapacityOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 7),
    _HostTimeHighCapacityOutOverflowOctets_Type()
)
hostTimeHighCapacityOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOverflowOctets.setUnits("Octets")
_HostTimeHighCapacityOutOctets_Type = Counter64
_HostTimeHighCapacityOutOctets_Object = MibTableColumn
hostTimeHighCapacityOutOctets = _HostTimeHighCapacityOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 6, 1, 8),
    _HostTimeHighCapacityOutOctets_Type()
)
hostTimeHighCapacityOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeHighCapacityOutOctets.setUnits("Octets")
_HostTopNHighCapacityTable_Object = MibTable
hostTopNHighCapacityTable = _HostTopNHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3)
)
if mibBuilder.loadTexts:
    hostTopNHighCapacityTable.setStatus("current")
_HostTopNHighCapacityEntry_Object = MibTableRow
hostTopNHighCapacityEntry = _HostTopNHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1)
)
hostTopNHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "hostTopNReport"),
    (0, "RMON-MIB", "hostTopNIndex"),
)
if mibBuilder.loadTexts:
    hostTopNHighCapacityEntry.setStatus("current")
_HostTopNHighCapacityAddress_Type = OctetString
_HostTopNHighCapacityAddress_Object = MibTableColumn
hostTopNHighCapacityAddress = _HostTopNHighCapacityAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 1),
    _HostTopNHighCapacityAddress_Type()
)
hostTopNHighCapacityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityAddress.setStatus("current")
_HostTopNHighCapacityBaseRate_Type = Gauge32
_HostTopNHighCapacityBaseRate_Object = MibTableColumn
hostTopNHighCapacityBaseRate = _HostTopNHighCapacityBaseRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 2),
    _HostTopNHighCapacityBaseRate_Type()
)
hostTopNHighCapacityBaseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityBaseRate.setStatus("current")
_HostTopNHighCapacityOverflowRate_Type = Gauge32
_HostTopNHighCapacityOverflowRate_Object = MibTableColumn
hostTopNHighCapacityOverflowRate = _HostTopNHighCapacityOverflowRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 3),
    _HostTopNHighCapacityOverflowRate_Type()
)
hostTopNHighCapacityOverflowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityOverflowRate.setStatus("current")
_HostTopNHighCapacityRate_Type = CounterBasedGauge64
_HostTopNHighCapacityRate_Object = MibTableColumn
hostTopNHighCapacityRate = _HostTopNHighCapacityRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 3, 1, 4),
    _HostTopNHighCapacityRate_Type()
)
hostTopNHighCapacityRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNHighCapacityRate.setStatus("current")
_MatrixSDHighCapacityTable_Object = MibTable
matrixSDHighCapacityTable = _MatrixSDHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5)
)
if mibBuilder.loadTexts:
    matrixSDHighCapacityTable.setStatus("current")
_MatrixSDHighCapacityEntry_Object = MibTableRow
matrixSDHighCapacityEntry = _MatrixSDHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1)
)
matrixSDHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "matrixSDIndex"),
    (0, "RMON-MIB", "matrixSDSourceAddress"),
    (0, "RMON-MIB", "matrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    matrixSDHighCapacityEntry.setStatus("current")
_MatrixSDHighCapacityOverflowPkts_Type = Counter32
_MatrixSDHighCapacityOverflowPkts_Object = MibTableColumn
matrixSDHighCapacityOverflowPkts = _MatrixSDHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 1),
    _MatrixSDHighCapacityOverflowPkts_Type()
)
matrixSDHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowPkts.setUnits("Packets")
_MatrixSDHighCapacityPkts_Type = Counter64
_MatrixSDHighCapacityPkts_Object = MibTableColumn
matrixSDHighCapacityPkts = _MatrixSDHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 2),
    _MatrixSDHighCapacityPkts_Type()
)
matrixSDHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityPkts.setUnits("Packets")
_MatrixSDHighCapacityOverflowOctets_Type = Counter32
_MatrixSDHighCapacityOverflowOctets_Object = MibTableColumn
matrixSDHighCapacityOverflowOctets = _MatrixSDHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 3),
    _MatrixSDHighCapacityOverflowOctets_Type()
)
matrixSDHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOverflowOctets.setUnits("Octets")
_MatrixSDHighCapacityOctets_Type = Counter64
_MatrixSDHighCapacityOctets_Object = MibTableColumn
matrixSDHighCapacityOctets = _MatrixSDHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 5, 1, 4),
    _MatrixSDHighCapacityOctets_Type()
)
matrixSDHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDHighCapacityOctets.setUnits("Octets")
_MatrixDSHighCapacityTable_Object = MibTable
matrixDSHighCapacityTable = _MatrixDSHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6)
)
if mibBuilder.loadTexts:
    matrixDSHighCapacityTable.setStatus("current")
_MatrixDSHighCapacityEntry_Object = MibTableRow
matrixDSHighCapacityEntry = _MatrixDSHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1)
)
matrixDSHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "matrixDSIndex"),
    (0, "RMON-MIB", "matrixDSDestAddress"),
    (0, "RMON-MIB", "matrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    matrixDSHighCapacityEntry.setStatus("current")
_MatrixDSHighCapacityOverflowPkts_Type = Counter32
_MatrixDSHighCapacityOverflowPkts_Object = MibTableColumn
matrixDSHighCapacityOverflowPkts = _MatrixDSHighCapacityOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 1),
    _MatrixDSHighCapacityOverflowPkts_Type()
)
matrixDSHighCapacityOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowPkts.setUnits("Packets")
_MatrixDSHighCapacityPkts_Type = Counter64
_MatrixDSHighCapacityPkts_Object = MibTableColumn
matrixDSHighCapacityPkts = _MatrixDSHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 2),
    _MatrixDSHighCapacityPkts_Type()
)
matrixDSHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityPkts.setUnits("Packets")
_MatrixDSHighCapacityOverflowOctets_Type = Counter32
_MatrixDSHighCapacityOverflowOctets_Object = MibTableColumn
matrixDSHighCapacityOverflowOctets = _MatrixDSHighCapacityOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 3),
    _MatrixDSHighCapacityOverflowOctets_Type()
)
matrixDSHighCapacityOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOverflowOctets.setUnits("Octets")
_MatrixDSHighCapacityOctets_Type = Counter64
_MatrixDSHighCapacityOctets_Object = MibTableColumn
matrixDSHighCapacityOctets = _MatrixDSHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 6, 1, 4),
    _MatrixDSHighCapacityOctets_Type()
)
matrixDSHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSHighCapacityOctets.setUnits("Octets")
_CaptureBufferHighCapacityTable_Object = MibTable
captureBufferHighCapacityTable = _CaptureBufferHighCapacityTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 3)
)
if mibBuilder.loadTexts:
    captureBufferHighCapacityTable.setStatus("current")
_CaptureBufferHighCapacityEntry_Object = MibTableRow
captureBufferHighCapacityEntry = _CaptureBufferHighCapacityEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 3, 1)
)
captureBufferHighCapacityEntry.setIndexNames(
    (0, "RMON-MIB", "captureBufferControlIndex"),
    (0, "RMON-MIB", "captureBufferIndex"),
)
if mibBuilder.loadTexts:
    captureBufferHighCapacityEntry.setStatus("current")


class _CaptureBufferPacketHighCapacityTime_Type(Integer32):
    """Custom type captureBufferPacketHighCapacityTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_CaptureBufferPacketHighCapacityTime_Type.__name__ = "Integer32"
_CaptureBufferPacketHighCapacityTime_Object = MibTableColumn
captureBufferPacketHighCapacityTime = _CaptureBufferPacketHighCapacityTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 3, 1, 1),
    _CaptureBufferPacketHighCapacityTime_Type()
)
captureBufferPacketHighCapacityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketHighCapacityTime.setStatus("current")
if mibBuilder.loadTexts:
    captureBufferPacketHighCapacityTime.setUnits("nanoseconds")
_HcRmonMIBCompliances_ObjectIdentity = ObjectIdentity
hcRmonMIBCompliances = _HcRmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 6)
)
_HcRmonMIBGroups_ObjectIdentity = ObjectIdentity
hcRmonMIBGroups = _HcRmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 7)
)
_MediaIndependentStats_ObjectIdentity = ObjectIdentity
mediaIndependentStats = _MediaIndependentStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 21)
)
_MediaIndependentTable_Object = MibTable
mediaIndependentTable = _MediaIndependentTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1)
)
if mibBuilder.loadTexts:
    mediaIndependentTable.setStatus("current")
_MediaIndependentEntry_Object = MibTableRow
mediaIndependentEntry = _MediaIndependentEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1)
)
mediaIndependentEntry.setIndexNames(
    (0, "HC-RMON-MIB", "mediaIndependentIndex"),
)
if mibBuilder.loadTexts:
    mediaIndependentEntry.setStatus("current")


class _MediaIndependentIndex_Type(Integer32):
    """Custom type mediaIndependentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MediaIndependentIndex_Type.__name__ = "Integer32"
_MediaIndependentIndex_Object = MibTableColumn
mediaIndependentIndex = _MediaIndependentIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 1),
    _MediaIndependentIndex_Type()
)
mediaIndependentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mediaIndependentIndex.setStatus("current")
_MediaIndependentDataSource_Type = ObjectIdentifier
_MediaIndependentDataSource_Object = MibTableColumn
mediaIndependentDataSource = _MediaIndependentDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 2),
    _MediaIndependentDataSource_Type()
)
mediaIndependentDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mediaIndependentDataSource.setStatus("current")
_MediaIndependentDropEvents_Type = Counter32
_MediaIndependentDropEvents_Object = MibTableColumn
mediaIndependentDropEvents = _MediaIndependentDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 3),
    _MediaIndependentDropEvents_Type()
)
mediaIndependentDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDropEvents.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentDropEvents.setUnits("Events")
_MediaIndependentDroppedFrames_Type = Counter32
_MediaIndependentDroppedFrames_Object = MibTableColumn
mediaIndependentDroppedFrames = _MediaIndependentDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 4),
    _MediaIndependentDroppedFrames_Type()
)
mediaIndependentDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentDroppedFrames.setUnits("Packets")
_MediaIndependentInPkts_Type = Counter32
_MediaIndependentInPkts_Object = MibTableColumn
mediaIndependentInPkts = _MediaIndependentInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 5),
    _MediaIndependentInPkts_Type()
)
mediaIndependentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInPkts.setUnits("Packets")
_MediaIndependentInOverflowPkts_Type = Counter32
_MediaIndependentInOverflowPkts_Object = MibTableColumn
mediaIndependentInOverflowPkts = _MediaIndependentInOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 6),
    _MediaIndependentInOverflowPkts_Type()
)
mediaIndependentInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowPkts.setUnits("Packets")
_MediaIndependentInHighCapacityPkts_Type = Counter64
_MediaIndependentInHighCapacityPkts_Object = MibTableColumn
mediaIndependentInHighCapacityPkts = _MediaIndependentInHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 7),
    _MediaIndependentInHighCapacityPkts_Type()
)
mediaIndependentInHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityPkts.setUnits("Packets")
_MediaIndependentOutPkts_Type = Counter32
_MediaIndependentOutPkts_Object = MibTableColumn
mediaIndependentOutPkts = _MediaIndependentOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 8),
    _MediaIndependentOutPkts_Type()
)
mediaIndependentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutPkts.setUnits("Packets")
_MediaIndependentOutOverflowPkts_Type = Counter32
_MediaIndependentOutOverflowPkts_Object = MibTableColumn
mediaIndependentOutOverflowPkts = _MediaIndependentOutOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 9),
    _MediaIndependentOutOverflowPkts_Type()
)
mediaIndependentOutOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowPkts.setUnits("Packets")
_MediaIndependentOutHighCapacityPkts_Type = Counter64
_MediaIndependentOutHighCapacityPkts_Object = MibTableColumn
mediaIndependentOutHighCapacityPkts = _MediaIndependentOutHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 10),
    _MediaIndependentOutHighCapacityPkts_Type()
)
mediaIndependentOutHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityPkts.setUnits("Packets")
_MediaIndependentInOctets_Type = Counter32
_MediaIndependentInOctets_Object = MibTableColumn
mediaIndependentInOctets = _MediaIndependentInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 11),
    _MediaIndependentInOctets_Type()
)
mediaIndependentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInOctets.setUnits("Octets")
_MediaIndependentInOverflowOctets_Type = Counter32
_MediaIndependentInOverflowOctets_Object = MibTableColumn
mediaIndependentInOverflowOctets = _MediaIndependentInOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 12),
    _MediaIndependentInOverflowOctets_Type()
)
mediaIndependentInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInOverflowOctets.setUnits("Octets")
_MediaIndependentInHighCapacityOctets_Type = Counter64
_MediaIndependentInHighCapacityOctets_Object = MibTableColumn
mediaIndependentInHighCapacityOctets = _MediaIndependentInHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 13),
    _MediaIndependentInHighCapacityOctets_Type()
)
mediaIndependentInHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInHighCapacityOctets.setUnits("Octets")
_MediaIndependentOutOctets_Type = Counter32
_MediaIndependentOutOctets_Object = MibTableColumn
mediaIndependentOutOctets = _MediaIndependentOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 14),
    _MediaIndependentOutOctets_Type()
)
mediaIndependentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutOctets.setUnits("Octets")
_MediaIndependentOutOverflowOctets_Type = Counter32
_MediaIndependentOutOverflowOctets_Object = MibTableColumn
mediaIndependentOutOverflowOctets = _MediaIndependentOutOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 15),
    _MediaIndependentOutOverflowOctets_Type()
)
mediaIndependentOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutOverflowOctets.setUnits("Octets")
_MediaIndependentOutHighCapacityOctets_Type = Counter64
_MediaIndependentOutHighCapacityOctets_Object = MibTableColumn
mediaIndependentOutHighCapacityOctets = _MediaIndependentOutHighCapacityOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 16),
    _MediaIndependentOutHighCapacityOctets_Type()
)
mediaIndependentOutHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityOctets.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutHighCapacityOctets.setUnits("Octets")
_MediaIndependentInNUCastPkts_Type = Counter32
_MediaIndependentInNUCastPkts_Object = MibTableColumn
mediaIndependentInNUCastPkts = _MediaIndependentInNUCastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 17),
    _MediaIndependentInNUCastPkts_Type()
)
mediaIndependentInNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastPkts.setUnits("Packets")
_MediaIndependentInNUCastOverflowPkts_Type = Counter32
_MediaIndependentInNUCastOverflowPkts_Object = MibTableColumn
mediaIndependentInNUCastOverflowPkts = _MediaIndependentInNUCastOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 18),
    _MediaIndependentInNUCastOverflowPkts_Type()
)
mediaIndependentInNUCastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastOverflowPkts.setUnits("Packets")
_MediaIndependentInNUCastHighCapacityPkts_Type = Counter64
_MediaIndependentInNUCastHighCapacityPkts_Object = MibTableColumn
mediaIndependentInNUCastHighCapacityPkts = _MediaIndependentInNUCastHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 19),
    _MediaIndependentInNUCastHighCapacityPkts_Type()
)
mediaIndependentInNUCastHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInNUCastHighCapacityPkts.setUnits("Packets")
_MediaIndependentOutNUCastPkts_Type = Counter32
_MediaIndependentOutNUCastPkts_Object = MibTableColumn
mediaIndependentOutNUCastPkts = _MediaIndependentOutNUCastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 20),
    _MediaIndependentOutNUCastPkts_Type()
)
mediaIndependentOutNUCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastPkts.setUnits("Packets")
_MediaIndependentOutNUCastOverflowPkts_Type = Counter32
_MediaIndependentOutNUCastOverflowPkts_Object = MibTableColumn
mediaIndependentOutNUCastOverflowPkts = _MediaIndependentOutNUCastOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 21),
    _MediaIndependentOutNUCastOverflowPkts_Type()
)
mediaIndependentOutNUCastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastOverflowPkts.setUnits("Packets")
_MediaIndependentOutNUCastHighCapacityPkts_Type = Counter64
_MediaIndependentOutNUCastHighCapacityPkts_Object = MibTableColumn
mediaIndependentOutNUCastHighCapacityPkts = _MediaIndependentOutNUCastHighCapacityPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 22),
    _MediaIndependentOutNUCastHighCapacityPkts_Type()
)
mediaIndependentOutNUCastHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastHighCapacityPkts.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutNUCastHighCapacityPkts.setUnits("Packets")
_MediaIndependentInErrors_Type = Counter32
_MediaIndependentInErrors_Object = MibTableColumn
mediaIndependentInErrors = _MediaIndependentInErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 23),
    _MediaIndependentInErrors_Type()
)
mediaIndependentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInErrors.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInErrors.setUnits("Packets")
_MediaIndependentOutErrors_Type = Counter32
_MediaIndependentOutErrors_Object = MibTableColumn
mediaIndependentOutErrors = _MediaIndependentOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 24),
    _MediaIndependentOutErrors_Type()
)
mediaIndependentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutErrors.setUnits("Packets")
_MediaIndependentInputSpeed_Type = Gauge32
_MediaIndependentInputSpeed_Object = MibTableColumn
mediaIndependentInputSpeed = _MediaIndependentInputSpeed_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 25),
    _MediaIndependentInputSpeed_Type()
)
mediaIndependentInputSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentInputSpeed.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentInputSpeed.setUnits("Kilobits per Second")
_MediaIndependentOutputSpeed_Type = Gauge32
_MediaIndependentOutputSpeed_Object = MibTableColumn
mediaIndependentOutputSpeed = _MediaIndependentOutputSpeed_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 26),
    _MediaIndependentOutputSpeed_Type()
)
mediaIndependentOutputSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentOutputSpeed.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentOutputSpeed.setUnits("Kilobits per Second")


class _MediaIndependentDuplexMode_Type(Integer32):
    """Custom type mediaIndependentDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 2),
          ("halfduplex", 1))
    )


_MediaIndependentDuplexMode_Type.__name__ = "Integer32"
_MediaIndependentDuplexMode_Object = MibTableColumn
mediaIndependentDuplexMode = _MediaIndependentDuplexMode_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 27),
    _MediaIndependentDuplexMode_Type()
)
mediaIndependentDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDuplexMode.setStatus("current")
_MediaIndependentDuplexChanges_Type = Counter32
_MediaIndependentDuplexChanges_Object = MibTableColumn
mediaIndependentDuplexChanges = _MediaIndependentDuplexChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 28),
    _MediaIndependentDuplexChanges_Type()
)
mediaIndependentDuplexChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDuplexChanges.setStatus("current")
if mibBuilder.loadTexts:
    mediaIndependentDuplexChanges.setUnits("Events")
_MediaIndependentDuplexLastChange_Type = TimeStamp
_MediaIndependentDuplexLastChange_Object = MibTableColumn
mediaIndependentDuplexLastChange = _MediaIndependentDuplexLastChange_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 29),
    _MediaIndependentDuplexLastChange_Type()
)
mediaIndependentDuplexLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaIndependentDuplexLastChange.setStatus("current")
_MediaIndependentOwner_Type = OwnerString
_MediaIndependentOwner_Object = MibTableColumn
mediaIndependentOwner = _MediaIndependentOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 30),
    _MediaIndependentOwner_Type()
)
mediaIndependentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mediaIndependentOwner.setStatus("current")
_MediaIndependentStatus_Type = RowStatus
_MediaIndependentStatus_Object = MibTableColumn
mediaIndependentStatus = _MediaIndependentStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 21, 1, 1, 31),
    _MediaIndependentStatus_Type()
)
mediaIndependentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mediaIndependentStatus.setStatus("current")

# Managed Objects groups

mediaIndependentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 1)
)
mediaIndependentGroup.setObjects(
      *(("HC-RMON-MIB", "mediaIndependentDataSource"),
        ("HC-RMON-MIB", "mediaIndependentDropEvents"),
        ("HC-RMON-MIB", "mediaIndependentDroppedFrames"),
        ("HC-RMON-MIB", "mediaIndependentInPkts"),
        ("HC-RMON-MIB", "mediaIndependentInOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentInHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentInOctets"),
        ("HC-RMON-MIB", "mediaIndependentInOverflowOctets"),
        ("HC-RMON-MIB", "mediaIndependentInHighCapacityOctets"),
        ("HC-RMON-MIB", "mediaIndependentOutOctets"),
        ("HC-RMON-MIB", "mediaIndependentOutOverflowOctets"),
        ("HC-RMON-MIB", "mediaIndependentOutHighCapacityOctets"),
        ("HC-RMON-MIB", "mediaIndependentInNUCastPkts"),
        ("HC-RMON-MIB", "mediaIndependentInNUCastOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentInNUCastHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutNUCastPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutNUCastOverflowPkts"),
        ("HC-RMON-MIB", "mediaIndependentOutNUCastHighCapacityPkts"),
        ("HC-RMON-MIB", "mediaIndependentInErrors"),
        ("HC-RMON-MIB", "mediaIndependentOutErrors"),
        ("HC-RMON-MIB", "mediaIndependentInputSpeed"),
        ("HC-RMON-MIB", "mediaIndependentOutputSpeed"),
        ("HC-RMON-MIB", "mediaIndependentDuplexMode"),
        ("HC-RMON-MIB", "mediaIndependentDuplexChanges"),
        ("HC-RMON-MIB", "mediaIndependentDuplexLastChange"),
        ("HC-RMON-MIB", "mediaIndependentOwner"),
        ("HC-RMON-MIB", "mediaIndependentStatus"))
)
if mibBuilder.loadTexts:
    mediaIndependentGroup.setStatus("current")

etherStatsHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 2)
)
etherStatsHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOctets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts64Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts64Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts65to127Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts65to127Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts128to255Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts128to255Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts256to511Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts256to511Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts512to1023Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts512to1023Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityOverflowPkts1024to1518Octets"),
        ("HC-RMON-MIB", "etherStatsHighCapacityPkts1024to1518Octets"))
)
if mibBuilder.loadTexts:
    etherStatsHighCapacityGroup.setStatus("current")

etherHistoryHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 3)
)
etherHistoryHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "etherHistoryHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityPkts"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "etherHistoryHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    etherHistoryHighCapacityGroup.setStatus("current")

hostHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 4)
)
hostHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "hostHighCapacityInOverflowPkts"),
        ("HC-RMON-MIB", "hostHighCapacityInPkts"),
        ("HC-RMON-MIB", "hostHighCapacityOutOverflowPkts"),
        ("HC-RMON-MIB", "hostHighCapacityOutPkts"),
        ("HC-RMON-MIB", "hostHighCapacityInOverflowOctets"),
        ("HC-RMON-MIB", "hostHighCapacityInOctets"),
        ("HC-RMON-MIB", "hostHighCapacityOutOverflowOctets"),
        ("HC-RMON-MIB", "hostHighCapacityOutOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInOverflowPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutOverflowPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutPkts"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInOverflowOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityInOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutOverflowOctets"),
        ("HC-RMON-MIB", "hostTimeHighCapacityOutOctets"))
)
if mibBuilder.loadTexts:
    hostHighCapacityGroup.setStatus("current")

hostTopNHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 5)
)
hostTopNHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "hostTopNHighCapacityAddress"),
        ("HC-RMON-MIB", "hostTopNHighCapacityBaseRate"),
        ("HC-RMON-MIB", "hostTopNHighCapacityOverflowRate"),
        ("HC-RMON-MIB", "hostTopNHighCapacityRate"))
)
if mibBuilder.loadTexts:
    hostTopNHighCapacityGroup.setStatus("current")

matrixHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 6)
)
matrixHighCapacityGroup.setObjects(
      *(("HC-RMON-MIB", "matrixSDHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "matrixSDHighCapacityPkts"),
        ("HC-RMON-MIB", "matrixSDHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "matrixSDHighCapacityOctets"),
        ("HC-RMON-MIB", "matrixDSHighCapacityOverflowPkts"),
        ("HC-RMON-MIB", "matrixDSHighCapacityPkts"),
        ("HC-RMON-MIB", "matrixDSHighCapacityOverflowOctets"),
        ("HC-RMON-MIB", "matrixDSHighCapacityOctets"))
)
if mibBuilder.loadTexts:
    matrixHighCapacityGroup.setStatus("current")

captureBufferHighCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 7, 7)
)
captureBufferHighCapacityGroup.setObjects(
    ("HC-RMON-MIB", "captureBufferPacketHighCapacityTime")
)
if mibBuilder.loadTexts:
    captureBufferHighCapacityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hcMediaIndependentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 6, 1)
)
if mibBuilder.loadTexts:
    hcMediaIndependentCompliance.setStatus(
        "current"
    )

hcRmon1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 6, 2)
)
if mibBuilder.loadTexts:
    hcRmon1MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HC-RMON-MIB",
    **{"etherStatsHighCapacityTable": etherStatsHighCapacityTable,
       "etherStatsHighCapacityEntry": etherStatsHighCapacityEntry,
       "etherStatsHighCapacityOverflowPkts": etherStatsHighCapacityOverflowPkts,
       "etherStatsHighCapacityPkts": etherStatsHighCapacityPkts,
       "etherStatsHighCapacityOverflowOctets": etherStatsHighCapacityOverflowOctets,
       "etherStatsHighCapacityOctets": etherStatsHighCapacityOctets,
       "etherStatsHighCapacityOverflowPkts64Octets": etherStatsHighCapacityOverflowPkts64Octets,
       "etherStatsHighCapacityPkts64Octets": etherStatsHighCapacityPkts64Octets,
       "etherStatsHighCapacityOverflowPkts65to127Octets": etherStatsHighCapacityOverflowPkts65to127Octets,
       "etherStatsHighCapacityPkts65to127Octets": etherStatsHighCapacityPkts65to127Octets,
       "etherStatsHighCapacityOverflowPkts128to255Octets": etherStatsHighCapacityOverflowPkts128to255Octets,
       "etherStatsHighCapacityPkts128to255Octets": etherStatsHighCapacityPkts128to255Octets,
       "etherStatsHighCapacityOverflowPkts256to511Octets": etherStatsHighCapacityOverflowPkts256to511Octets,
       "etherStatsHighCapacityPkts256to511Octets": etherStatsHighCapacityPkts256to511Octets,
       "etherStatsHighCapacityOverflowPkts512to1023Octets": etherStatsHighCapacityOverflowPkts512to1023Octets,
       "etherStatsHighCapacityPkts512to1023Octets": etherStatsHighCapacityPkts512to1023Octets,
       "etherStatsHighCapacityOverflowPkts1024to1518Octets": etherStatsHighCapacityOverflowPkts1024to1518Octets,
       "etherStatsHighCapacityPkts1024to1518Octets": etherStatsHighCapacityPkts1024to1518Octets,
       "etherHistoryHighCapacityTable": etherHistoryHighCapacityTable,
       "etherHistoryHighCapacityEntry": etherHistoryHighCapacityEntry,
       "etherHistoryHighCapacityOverflowPkts": etherHistoryHighCapacityOverflowPkts,
       "etherHistoryHighCapacityPkts": etherHistoryHighCapacityPkts,
       "etherHistoryHighCapacityOverflowOctets": etherHistoryHighCapacityOverflowOctets,
       "etherHistoryHighCapacityOctets": etherHistoryHighCapacityOctets,
       "hostHighCapacityTable": hostHighCapacityTable,
       "hostHighCapacityEntry": hostHighCapacityEntry,
       "hostHighCapacityInOverflowPkts": hostHighCapacityInOverflowPkts,
       "hostHighCapacityInPkts": hostHighCapacityInPkts,
       "hostHighCapacityOutOverflowPkts": hostHighCapacityOutOverflowPkts,
       "hostHighCapacityOutPkts": hostHighCapacityOutPkts,
       "hostHighCapacityInOverflowOctets": hostHighCapacityInOverflowOctets,
       "hostHighCapacityInOctets": hostHighCapacityInOctets,
       "hostHighCapacityOutOverflowOctets": hostHighCapacityOutOverflowOctets,
       "hostHighCapacityOutOctets": hostHighCapacityOutOctets,
       "hostTimeHighCapacityTable": hostTimeHighCapacityTable,
       "hostTimeHighCapacityEntry": hostTimeHighCapacityEntry,
       "hostTimeHighCapacityInOverflowPkts": hostTimeHighCapacityInOverflowPkts,
       "hostTimeHighCapacityInPkts": hostTimeHighCapacityInPkts,
       "hostTimeHighCapacityOutOverflowPkts": hostTimeHighCapacityOutOverflowPkts,
       "hostTimeHighCapacityOutPkts": hostTimeHighCapacityOutPkts,
       "hostTimeHighCapacityInOverflowOctets": hostTimeHighCapacityInOverflowOctets,
       "hostTimeHighCapacityInOctets": hostTimeHighCapacityInOctets,
       "hostTimeHighCapacityOutOverflowOctets": hostTimeHighCapacityOutOverflowOctets,
       "hostTimeHighCapacityOutOctets": hostTimeHighCapacityOutOctets,
       "hostTopNHighCapacityTable": hostTopNHighCapacityTable,
       "hostTopNHighCapacityEntry": hostTopNHighCapacityEntry,
       "hostTopNHighCapacityAddress": hostTopNHighCapacityAddress,
       "hostTopNHighCapacityBaseRate": hostTopNHighCapacityBaseRate,
       "hostTopNHighCapacityOverflowRate": hostTopNHighCapacityOverflowRate,
       "hostTopNHighCapacityRate": hostTopNHighCapacityRate,
       "matrixSDHighCapacityTable": matrixSDHighCapacityTable,
       "matrixSDHighCapacityEntry": matrixSDHighCapacityEntry,
       "matrixSDHighCapacityOverflowPkts": matrixSDHighCapacityOverflowPkts,
       "matrixSDHighCapacityPkts": matrixSDHighCapacityPkts,
       "matrixSDHighCapacityOverflowOctets": matrixSDHighCapacityOverflowOctets,
       "matrixSDHighCapacityOctets": matrixSDHighCapacityOctets,
       "matrixDSHighCapacityTable": matrixDSHighCapacityTable,
       "matrixDSHighCapacityEntry": matrixDSHighCapacityEntry,
       "matrixDSHighCapacityOverflowPkts": matrixDSHighCapacityOverflowPkts,
       "matrixDSHighCapacityPkts": matrixDSHighCapacityPkts,
       "matrixDSHighCapacityOverflowOctets": matrixDSHighCapacityOverflowOctets,
       "matrixDSHighCapacityOctets": matrixDSHighCapacityOctets,
       "captureBufferHighCapacityTable": captureBufferHighCapacityTable,
       "captureBufferHighCapacityEntry": captureBufferHighCapacityEntry,
       "captureBufferPacketHighCapacityTime": captureBufferPacketHighCapacityTime,
       "hcRMON": hcRMON,
       "hcRmonMIBCompliances": hcRmonMIBCompliances,
       "hcMediaIndependentCompliance": hcMediaIndependentCompliance,
       "hcRmon1MIBCompliance": hcRmon1MIBCompliance,
       "hcRmonMIBGroups": hcRmonMIBGroups,
       "mediaIndependentGroup": mediaIndependentGroup,
       "etherStatsHighCapacityGroup": etherStatsHighCapacityGroup,
       "etherHistoryHighCapacityGroup": etherHistoryHighCapacityGroup,
       "hostHighCapacityGroup": hostHighCapacityGroup,
       "hostTopNHighCapacityGroup": hostTopNHighCapacityGroup,
       "matrixHighCapacityGroup": matrixHighCapacityGroup,
       "captureBufferHighCapacityGroup": captureBufferHighCapacityGroup,
       "mediaIndependentStats": mediaIndependentStats,
       "mediaIndependentTable": mediaIndependentTable,
       "mediaIndependentEntry": mediaIndependentEntry,
       "mediaIndependentIndex": mediaIndependentIndex,
       "mediaIndependentDataSource": mediaIndependentDataSource,
       "mediaIndependentDropEvents": mediaIndependentDropEvents,
       "mediaIndependentDroppedFrames": mediaIndependentDroppedFrames,
       "mediaIndependentInPkts": mediaIndependentInPkts,
       "mediaIndependentInOverflowPkts": mediaIndependentInOverflowPkts,
       "mediaIndependentInHighCapacityPkts": mediaIndependentInHighCapacityPkts,
       "mediaIndependentOutPkts": mediaIndependentOutPkts,
       "mediaIndependentOutOverflowPkts": mediaIndependentOutOverflowPkts,
       "mediaIndependentOutHighCapacityPkts": mediaIndependentOutHighCapacityPkts,
       "mediaIndependentInOctets": mediaIndependentInOctets,
       "mediaIndependentInOverflowOctets": mediaIndependentInOverflowOctets,
       "mediaIndependentInHighCapacityOctets": mediaIndependentInHighCapacityOctets,
       "mediaIndependentOutOctets": mediaIndependentOutOctets,
       "mediaIndependentOutOverflowOctets": mediaIndependentOutOverflowOctets,
       "mediaIndependentOutHighCapacityOctets": mediaIndependentOutHighCapacityOctets,
       "mediaIndependentInNUCastPkts": mediaIndependentInNUCastPkts,
       "mediaIndependentInNUCastOverflowPkts": mediaIndependentInNUCastOverflowPkts,
       "mediaIndependentInNUCastHighCapacityPkts": mediaIndependentInNUCastHighCapacityPkts,
       "mediaIndependentOutNUCastPkts": mediaIndependentOutNUCastPkts,
       "mediaIndependentOutNUCastOverflowPkts": mediaIndependentOutNUCastOverflowPkts,
       "mediaIndependentOutNUCastHighCapacityPkts": mediaIndependentOutNUCastHighCapacityPkts,
       "mediaIndependentInErrors": mediaIndependentInErrors,
       "mediaIndependentOutErrors": mediaIndependentOutErrors,
       "mediaIndependentInputSpeed": mediaIndependentInputSpeed,
       "mediaIndependentOutputSpeed": mediaIndependentOutputSpeed,
       "mediaIndependentDuplexMode": mediaIndependentDuplexMode,
       "mediaIndependentDuplexChanges": mediaIndependentDuplexChanges,
       "mediaIndependentDuplexLastChange": mediaIndependentDuplexLastChange,
       "mediaIndependentOwner": mediaIndependentOwner,
       "mediaIndependentStatus": mediaIndependentStatus}
)
