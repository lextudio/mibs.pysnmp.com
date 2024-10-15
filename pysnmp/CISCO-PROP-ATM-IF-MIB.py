# SNMP MIB module (CISCO-PROP-ATM-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PROP-ATM-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:10 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoPropAtmIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319)
)
ciscoPropAtmIfMIB.setRevisions(
        ("2002-12-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPropAtmIfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPropAtmIfMIBNotifs = _CiscoPropAtmIfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 0)
)
_CiscoPropAtmIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPropAtmIfMIBObjects = _CiscoPropAtmIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1)
)
_CpAtmIfConfig_ObjectIdentity = ObjectIdentity
cpAtmIfConfig = _CpAtmIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1)
)
_CpAtmIfConfigTable_Object = MibTable
cpAtmIfConfigTable = _CpAtmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpAtmIfConfigTable.setStatus("current")
_CpAtmIfConfigEntry_Object = MibTableRow
cpAtmIfConfigEntry = _CpAtmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1, 1, 1)
)
cpAtmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpAtmIfConfigEntry.setStatus("current")


class _CpAtmIfMaxBandwidth_Type(Unsigned32):
    """Custom type cpAtmIfMaxBandwidth based on Unsigned32"""
    defaultValue = 7000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpAtmIfMaxBandwidth_Type.__name__ = "Unsigned32"
_CpAtmIfMaxBandwidth_Object = MibTableColumn
cpAtmIfMaxBandwidth = _CpAtmIfMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1, 1, 1, 1),
    _CpAtmIfMaxBandwidth_Type()
)
cpAtmIfMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpAtmIfMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cpAtmIfMaxBandwidth.setUnits("cells-per-second")
_CpAtmIfVirtualPortStats_ObjectIdentity = ObjectIdentity
cpAtmIfVirtualPortStats = _CpAtmIfVirtualPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2)
)
_CpAtmIfStatsEgressTable_Object = MibTable
cpAtmIfStatsEgressTable = _CpAtmIfStatsEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpAtmIfStatsEgressTable.setStatus("current")
_CpAtmIfStatsEgressEntry_Object = MibTableRow
cpAtmIfStatsEgressEntry = _CpAtmIfStatsEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1)
)
cpAtmIfStatsEgressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpAtmIfStatsEgressEntry.setStatus("current")
_CpAtmIfEgrRcvClp0Cells_Type = Counter32
_CpAtmIfEgrRcvClp0Cells_Object = MibTableColumn
cpAtmIfEgrRcvClp0Cells = _CpAtmIfEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 1),
    _CpAtmIfEgrRcvClp0Cells_Type()
)
cpAtmIfEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfEgrRcvClp0Cells.setStatus("current")
_CpAtmIfEgrRcvClp1Cells_Type = Counter32
_CpAtmIfEgrRcvClp1Cells_Object = MibTableColumn
cpAtmIfEgrRcvClp1Cells = _CpAtmIfEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 2),
    _CpAtmIfEgrRcvClp1Cells_Type()
)
cpAtmIfEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfEgrRcvClp1Cells.setStatus("current")
_CpAtmIfEgrClp0DiscCells_Type = Counter32
_CpAtmIfEgrClp0DiscCells_Object = MibTableColumn
cpAtmIfEgrClp0DiscCells = _CpAtmIfEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 3),
    _CpAtmIfEgrClp0DiscCells_Type()
)
cpAtmIfEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfEgrClp0DiscCells.setStatus("current")
_CpAtmIfEgrClp1DiscCells_Type = Counter32
_CpAtmIfEgrClp1DiscCells_Object = MibTableColumn
cpAtmIfEgrClp1DiscCells = _CpAtmIfEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 4),
    _CpAtmIfEgrClp1DiscCells_Type()
)
cpAtmIfEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfEgrClp1DiscCells.setStatus("current")
_CpAtmIfEgrRcvOAMCells_Type = Counter32
_CpAtmIfEgrRcvOAMCells_Object = MibTableColumn
cpAtmIfEgrRcvOAMCells = _CpAtmIfEgrRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 5),
    _CpAtmIfEgrRcvOAMCells_Type()
)
cpAtmIfEgrRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfEgrRcvOAMCells.setStatus("current")
_CpAtmIfEgrRcvEFCICells_Type = Counter32
_CpAtmIfEgrRcvEFCICells_Object = MibTableColumn
cpAtmIfEgrRcvEFCICells = _CpAtmIfEgrRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 6),
    _CpAtmIfEgrRcvEFCICells_Type()
)
cpAtmIfEgrRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfEgrRcvEFCICells.setStatus("current")
_CpAtmIfHCEgrRcvClp0Cells_Type = Counter64
_CpAtmIfHCEgrRcvClp0Cells_Object = MibTableColumn
cpAtmIfHCEgrRcvClp0Cells = _CpAtmIfHCEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 7),
    _CpAtmIfHCEgrRcvClp0Cells_Type()
)
cpAtmIfHCEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCEgrRcvClp0Cells.setStatus("current")
_CpAtmIfHCEgrRcvClp1Cells_Type = Counter64
_CpAtmIfHCEgrRcvClp1Cells_Object = MibTableColumn
cpAtmIfHCEgrRcvClp1Cells = _CpAtmIfHCEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 8),
    _CpAtmIfHCEgrRcvClp1Cells_Type()
)
cpAtmIfHCEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCEgrRcvClp1Cells.setStatus("current")
_CpAtmIfHCEgrClp0DiscCells_Type = Counter64
_CpAtmIfHCEgrClp0DiscCells_Object = MibTableColumn
cpAtmIfHCEgrClp0DiscCells = _CpAtmIfHCEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 9),
    _CpAtmIfHCEgrClp0DiscCells_Type()
)
cpAtmIfHCEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCEgrClp0DiscCells.setStatus("current")
_CpAtmIfHCEgrClp1DiscCells_Type = Counter64
_CpAtmIfHCEgrClp1DiscCells_Object = MibTableColumn
cpAtmIfHCEgrClp1DiscCells = _CpAtmIfHCEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 10),
    _CpAtmIfHCEgrClp1DiscCells_Type()
)
cpAtmIfHCEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCEgrClp1DiscCells.setStatus("current")
_CpAtmIfHCEgrRcvOAMCells_Type = Counter64
_CpAtmIfHCEgrRcvOAMCells_Object = MibTableColumn
cpAtmIfHCEgrRcvOAMCells = _CpAtmIfHCEgrRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 11),
    _CpAtmIfHCEgrRcvOAMCells_Type()
)
cpAtmIfHCEgrRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCEgrRcvOAMCells.setStatus("current")
_CpAtmIfHCEgrRcvEFCICells_Type = Counter64
_CpAtmIfHCEgrRcvEFCICells_Object = MibTableColumn
cpAtmIfHCEgrRcvEFCICells = _CpAtmIfHCEgrRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 12),
    _CpAtmIfHCEgrRcvEFCICells_Type()
)
cpAtmIfHCEgrRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCEgrRcvEFCICells.setStatus("current")
_CpAtmIfEgressIntervalTable_Object = MibTable
cpAtmIfEgressIntervalTable = _CpAtmIfEgressIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpAtmIfEgressIntervalTable.setStatus("current")
_CpAtmIfEgressIntervalEntry_Object = MibTableRow
cpAtmIfEgressIntervalEntry = _CpAtmIfEgressIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1)
)
cpAtmIfEgressIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgressIntervalNumber"),
)
if mibBuilder.loadTexts:
    cpAtmIfEgressIntervalEntry.setStatus("current")


class _CpAtmIfEgressIntervalNumber_Type(Integer32):
    """Custom type cpAtmIfEgressIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CpAtmIfEgressIntervalNumber_Type.__name__ = "Integer32"
_CpAtmIfEgressIntervalNumber_Object = MibTableColumn
cpAtmIfEgressIntervalNumber = _CpAtmIfEgressIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 1),
    _CpAtmIfEgressIntervalNumber_Type()
)
cpAtmIfEgressIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpAtmIfEgressIntervalNumber.setStatus("current")
_CpAtmIfIntEgrRcvClp0Cells_Type = Counter32
_CpAtmIfIntEgrRcvClp0Cells_Object = MibTableColumn
cpAtmIfIntEgrRcvClp0Cells = _CpAtmIfIntEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 2),
    _CpAtmIfIntEgrRcvClp0Cells_Type()
)
cpAtmIfIntEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIntEgrRcvClp0Cells.setStatus("current")
_CpAtmIfIntEgrRcvClp1Cells_Type = Counter32
_CpAtmIfIntEgrRcvClp1Cells_Object = MibTableColumn
cpAtmIfIntEgrRcvClp1Cells = _CpAtmIfIntEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 3),
    _CpAtmIfIntEgrRcvClp1Cells_Type()
)
cpAtmIfIntEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIntEgrRcvClp1Cells.setStatus("current")
_CpAtmIfIntEgrClp0DiscCells_Type = Counter32
_CpAtmIfIntEgrClp0DiscCells_Object = MibTableColumn
cpAtmIfIntEgrClp0DiscCells = _CpAtmIfIntEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 4),
    _CpAtmIfIntEgrClp0DiscCells_Type()
)
cpAtmIfIntEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIntEgrClp0DiscCells.setStatus("current")
_CpAtmIfIntEgrClp1DiscCells_Type = Counter32
_CpAtmIfIntEgrClp1DiscCells_Object = MibTableColumn
cpAtmIfIntEgrClp1DiscCells = _CpAtmIfIntEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 5),
    _CpAtmIfIntEgrClp1DiscCells_Type()
)
cpAtmIfIntEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIntEgrClp1DiscCells.setStatus("current")
_CpAtmIfIntEgrRcvOAMCells_Type = Counter32
_CpAtmIfIntEgrRcvOAMCells_Object = MibTableColumn
cpAtmIfIntEgrRcvOAMCells = _CpAtmIfIntEgrRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 6),
    _CpAtmIfIntEgrRcvOAMCells_Type()
)
cpAtmIfIntEgrRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIntEgrRcvOAMCells.setStatus("current")
_CpAtmIfIntEgrRcvEFCICells_Type = Counter32
_CpAtmIfIntEgrRcvEFCICells_Object = MibTableColumn
cpAtmIfIntEgrRcvEFCICells = _CpAtmIfIntEgrRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 7),
    _CpAtmIfIntEgrRcvEFCICells_Type()
)
cpAtmIfIntEgrRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIntEgrRcvEFCICells.setStatus("current")
_CpAtmIfHCIntEgrRcvClp0Cells_Type = Counter64
_CpAtmIfHCIntEgrRcvClp0Cells_Object = MibTableColumn
cpAtmIfHCIntEgrRcvClp0Cells = _CpAtmIfHCIntEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 8),
    _CpAtmIfHCIntEgrRcvClp0Cells_Type()
)
cpAtmIfHCIntEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIntEgrRcvClp0Cells.setStatus("current")
_CpAtmIfHCIntEgrRcvClp1Cells_Type = Counter64
_CpAtmIfHCIntEgrRcvClp1Cells_Object = MibTableColumn
cpAtmIfHCIntEgrRcvClp1Cells = _CpAtmIfHCIntEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 9),
    _CpAtmIfHCIntEgrRcvClp1Cells_Type()
)
cpAtmIfHCIntEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIntEgrRcvClp1Cells.setStatus("current")
_CpAtmIfHCIntEgrClp0DiscCells_Type = Counter64
_CpAtmIfHCIntEgrClp0DiscCells_Object = MibTableColumn
cpAtmIfHCIntEgrClp0DiscCells = _CpAtmIfHCIntEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 10),
    _CpAtmIfHCIntEgrClp0DiscCells_Type()
)
cpAtmIfHCIntEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIntEgrClp0DiscCells.setStatus("current")
_CpAtmIfHCIntEgrClp1DiscCells_Type = Counter64
_CpAtmIfHCIntEgrClp1DiscCells_Object = MibTableColumn
cpAtmIfHCIntEgrClp1DiscCells = _CpAtmIfHCIntEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 11),
    _CpAtmIfHCIntEgrClp1DiscCells_Type()
)
cpAtmIfHCIntEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIntEgrClp1DiscCells.setStatus("current")
_CpAtmIfHCIntEgrRcvOAMCells_Type = Counter64
_CpAtmIfHCIntEgrRcvOAMCells_Object = MibTableColumn
cpAtmIfHCIntEgrRcvOAMCells = _CpAtmIfHCIntEgrRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 12),
    _CpAtmIfHCIntEgrRcvOAMCells_Type()
)
cpAtmIfHCIntEgrRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIntEgrRcvOAMCells.setStatus("current")
_CpAtmIfHCIntEgrRcvEFCICells_Type = Counter64
_CpAtmIfHCIntEgrRcvEFCICells_Object = MibTableColumn
cpAtmIfHCIntEgrRcvEFCICells = _CpAtmIfHCIntEgrRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 13),
    _CpAtmIfHCIntEgrRcvEFCICells_Type()
)
cpAtmIfHCIntEgrRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIntEgrRcvEFCICells.setStatus("current")
_CpAtmIfStatsIngressTable_Object = MibTable
cpAtmIfStatsIngressTable = _CpAtmIfStatsIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpAtmIfStatsIngressTable.setStatus("current")
_CpAtmIfStatsIngressEntry_Object = MibTableRow
cpAtmIfStatsIngressEntry = _CpAtmIfStatsIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1)
)
cpAtmIfStatsIngressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpAtmIfStatsIngressEntry.setStatus("current")
_CpAtmIfIngXmtClp0Cells_Type = Counter32
_CpAtmIfIngXmtClp0Cells_Object = MibTableColumn
cpAtmIfIngXmtClp0Cells = _CpAtmIfIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 1),
    _CpAtmIfIngXmtClp0Cells_Type()
)
cpAtmIfIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIngXmtClp0Cells.setStatus("current")
_CpAtmIfIngXmtClp1Cells_Type = Counter32
_CpAtmIfIngXmtClp1Cells_Object = MibTableColumn
cpAtmIfIngXmtClp1Cells = _CpAtmIfIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 2),
    _CpAtmIfIngXmtClp1Cells_Type()
)
cpAtmIfIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIngXmtClp1Cells.setStatus("current")
_CpAtmIfIngXmtEFCICells_Type = Counter32
_CpAtmIfIngXmtEFCICells_Object = MibTableColumn
cpAtmIfIngXmtEFCICells = _CpAtmIfIngXmtEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 3),
    _CpAtmIfIngXmtEFCICells_Type()
)
cpAtmIfIngXmtEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIngXmtEFCICells.setStatus("current")
_CpAtmIfIngXmtOAMCells_Type = Counter32
_CpAtmIfIngXmtOAMCells_Object = MibTableColumn
cpAtmIfIngXmtOAMCells = _CpAtmIfIngXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 4),
    _CpAtmIfIngXmtOAMCells_Type()
)
cpAtmIfIngXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfIngXmtOAMCells.setStatus("current")
_CpAtmIfHCIngXmtClp0Cells_Type = Counter64
_CpAtmIfHCIngXmtClp0Cells_Object = MibTableColumn
cpAtmIfHCIngXmtClp0Cells = _CpAtmIfHCIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 5),
    _CpAtmIfHCIngXmtClp0Cells_Type()
)
cpAtmIfHCIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIngXmtClp0Cells.setStatus("current")
_CpAtmIfHCIngXmtClp1Cells_Type = Counter64
_CpAtmIfHCIngXmtClp1Cells_Object = MibTableColumn
cpAtmIfHCIngXmtClp1Cells = _CpAtmIfHCIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 6),
    _CpAtmIfHCIngXmtClp1Cells_Type()
)
cpAtmIfHCIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIngXmtClp1Cells.setStatus("current")
_CpAtmIfHCIngXmtEFCICells_Type = Counter64
_CpAtmIfHCIngXmtEFCICells_Object = MibTableColumn
cpAtmIfHCIngXmtEFCICells = _CpAtmIfHCIngXmtEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 7),
    _CpAtmIfHCIngXmtEFCICells_Type()
)
cpAtmIfHCIngXmtEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIngXmtEFCICells.setStatus("current")
_CpAtmIfHCIngXmtOAMCells_Type = Counter64
_CpAtmIfHCIngXmtOAMCells_Object = MibTableColumn
cpAtmIfHCIngXmtOAMCells = _CpAtmIfHCIngXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 8),
    _CpAtmIfHCIngXmtOAMCells_Type()
)
cpAtmIfHCIngXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpAtmIfHCIngXmtOAMCells.setStatus("current")
_CpAtmIfMIBConformance_ObjectIdentity = ObjectIdentity
cpAtmIfMIBConformance = _CpAtmIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2)
)
_CpAtmIfMIBCompliances_ObjectIdentity = ObjectIdentity
cpAtmIfMIBCompliances = _CpAtmIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 1)
)
_CpAtmIfMIBGroups_ObjectIdentity = ObjectIdentity
cpAtmIfMIBGroups = _CpAtmIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2)
)

# Managed Objects groups

cpAtmIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 1)
)
cpAtmIfConfigGroup.setObjects(
    ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfMaxBandwidth")
)
if mibBuilder.loadTexts:
    cpAtmIfConfigGroup.setStatus("current")

cpAtmIfEgressStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 2)
)
cpAtmIfEgressStatMIBGroup.setObjects(
      *(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvClp0Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvClp1Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrClp0DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrClp1DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvOAMCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvEFCICells"))
)
if mibBuilder.loadTexts:
    cpAtmIfEgressStatMIBGroup.setStatus("current")

cpAtmIfEgressIntervalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 3)
)
cpAtmIfEgressIntervalMIBGroup.setObjects(
      *(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvClp0Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvClp1Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrClp0DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrClp1DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvOAMCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvEFCICells"))
)
if mibBuilder.loadTexts:
    cpAtmIfEgressIntervalMIBGroup.setStatus("current")

cpAtmIfIngressStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 4)
)
cpAtmIfIngressStatMIBGroup.setObjects(
      *(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtClp0Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtClp1Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtEFCICells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtOAMCells"))
)
if mibBuilder.loadTexts:
    cpAtmIfIngressStatMIBGroup.setStatus("current")

cpAtmIfHCEgressStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 5)
)
cpAtmIfHCEgressStatMIBGroup.setObjects(
      *(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvClp0Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvClp1Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrClp0DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrClp1DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvOAMCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvEFCICells"))
)
if mibBuilder.loadTexts:
    cpAtmIfHCEgressStatMIBGroup.setStatus("current")

cpAtmIfHCEgressIntervalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 6)
)
cpAtmIfHCEgressIntervalMIBGroup.setObjects(
      *(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvClp0Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvClp1Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrClp0DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrClp1DiscCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvOAMCells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvEFCICells"))
)
if mibBuilder.loadTexts:
    cpAtmIfHCEgressIntervalMIBGroup.setStatus("current")

cpAtmIfHCIngressStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 7)
)
cpAtmIfHCIngressStatMIBGroup.setObjects(
      *(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtClp0Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtClp1Cells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtEFCICells"),
        ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtOAMCells"))
)
if mibBuilder.loadTexts:
    cpAtmIfHCIngressStatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpAtmIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpAtmIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PROP-ATM-IF-MIB",
    **{"ciscoPropAtmIfMIB": ciscoPropAtmIfMIB,
       "ciscoPropAtmIfMIBNotifs": ciscoPropAtmIfMIBNotifs,
       "ciscoPropAtmIfMIBObjects": ciscoPropAtmIfMIBObjects,
       "cpAtmIfConfig": cpAtmIfConfig,
       "cpAtmIfConfigTable": cpAtmIfConfigTable,
       "cpAtmIfConfigEntry": cpAtmIfConfigEntry,
       "cpAtmIfMaxBandwidth": cpAtmIfMaxBandwidth,
       "cpAtmIfVirtualPortStats": cpAtmIfVirtualPortStats,
       "cpAtmIfStatsEgressTable": cpAtmIfStatsEgressTable,
       "cpAtmIfStatsEgressEntry": cpAtmIfStatsEgressEntry,
       "cpAtmIfEgrRcvClp0Cells": cpAtmIfEgrRcvClp0Cells,
       "cpAtmIfEgrRcvClp1Cells": cpAtmIfEgrRcvClp1Cells,
       "cpAtmIfEgrClp0DiscCells": cpAtmIfEgrClp0DiscCells,
       "cpAtmIfEgrClp1DiscCells": cpAtmIfEgrClp1DiscCells,
       "cpAtmIfEgrRcvOAMCells": cpAtmIfEgrRcvOAMCells,
       "cpAtmIfEgrRcvEFCICells": cpAtmIfEgrRcvEFCICells,
       "cpAtmIfHCEgrRcvClp0Cells": cpAtmIfHCEgrRcvClp0Cells,
       "cpAtmIfHCEgrRcvClp1Cells": cpAtmIfHCEgrRcvClp1Cells,
       "cpAtmIfHCEgrClp0DiscCells": cpAtmIfHCEgrClp0DiscCells,
       "cpAtmIfHCEgrClp1DiscCells": cpAtmIfHCEgrClp1DiscCells,
       "cpAtmIfHCEgrRcvOAMCells": cpAtmIfHCEgrRcvOAMCells,
       "cpAtmIfHCEgrRcvEFCICells": cpAtmIfHCEgrRcvEFCICells,
       "cpAtmIfEgressIntervalTable": cpAtmIfEgressIntervalTable,
       "cpAtmIfEgressIntervalEntry": cpAtmIfEgressIntervalEntry,
       "cpAtmIfEgressIntervalNumber": cpAtmIfEgressIntervalNumber,
       "cpAtmIfIntEgrRcvClp0Cells": cpAtmIfIntEgrRcvClp0Cells,
       "cpAtmIfIntEgrRcvClp1Cells": cpAtmIfIntEgrRcvClp1Cells,
       "cpAtmIfIntEgrClp0DiscCells": cpAtmIfIntEgrClp0DiscCells,
       "cpAtmIfIntEgrClp1DiscCells": cpAtmIfIntEgrClp1DiscCells,
       "cpAtmIfIntEgrRcvOAMCells": cpAtmIfIntEgrRcvOAMCells,
       "cpAtmIfIntEgrRcvEFCICells": cpAtmIfIntEgrRcvEFCICells,
       "cpAtmIfHCIntEgrRcvClp0Cells": cpAtmIfHCIntEgrRcvClp0Cells,
       "cpAtmIfHCIntEgrRcvClp1Cells": cpAtmIfHCIntEgrRcvClp1Cells,
       "cpAtmIfHCIntEgrClp0DiscCells": cpAtmIfHCIntEgrClp0DiscCells,
       "cpAtmIfHCIntEgrClp1DiscCells": cpAtmIfHCIntEgrClp1DiscCells,
       "cpAtmIfHCIntEgrRcvOAMCells": cpAtmIfHCIntEgrRcvOAMCells,
       "cpAtmIfHCIntEgrRcvEFCICells": cpAtmIfHCIntEgrRcvEFCICells,
       "cpAtmIfStatsIngressTable": cpAtmIfStatsIngressTable,
       "cpAtmIfStatsIngressEntry": cpAtmIfStatsIngressEntry,
       "cpAtmIfIngXmtClp0Cells": cpAtmIfIngXmtClp0Cells,
       "cpAtmIfIngXmtClp1Cells": cpAtmIfIngXmtClp1Cells,
       "cpAtmIfIngXmtEFCICells": cpAtmIfIngXmtEFCICells,
       "cpAtmIfIngXmtOAMCells": cpAtmIfIngXmtOAMCells,
       "cpAtmIfHCIngXmtClp0Cells": cpAtmIfHCIngXmtClp0Cells,
       "cpAtmIfHCIngXmtClp1Cells": cpAtmIfHCIngXmtClp1Cells,
       "cpAtmIfHCIngXmtEFCICells": cpAtmIfHCIngXmtEFCICells,
       "cpAtmIfHCIngXmtOAMCells": cpAtmIfHCIngXmtOAMCells,
       "cpAtmIfMIBConformance": cpAtmIfMIBConformance,
       "cpAtmIfMIBCompliances": cpAtmIfMIBCompliances,
       "cpAtmIfMIBCompliance": cpAtmIfMIBCompliance,
       "cpAtmIfMIBGroups": cpAtmIfMIBGroups,
       "cpAtmIfConfigGroup": cpAtmIfConfigGroup,
       "cpAtmIfEgressStatMIBGroup": cpAtmIfEgressStatMIBGroup,
       "cpAtmIfEgressIntervalMIBGroup": cpAtmIfEgressIntervalMIBGroup,
       "cpAtmIfIngressStatMIBGroup": cpAtmIfIngressStatMIBGroup,
       "cpAtmIfHCEgressStatMIBGroup": cpAtmIfHCEgressStatMIBGroup,
       "cpAtmIfHCEgressIntervalMIBGroup": cpAtmIfHCEgressIntervalMIBGroup,
       "cpAtmIfHCIngressStatMIBGroup": cpAtmIfHCIngressStatMIBGroup}
)
