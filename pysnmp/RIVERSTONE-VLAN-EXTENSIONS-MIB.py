# SNMP MIB module (RIVERSTONE-VLAN-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-VLAN-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:58 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(dot1qVlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rsVlanExtensionsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65)
)
rsVlanExtensionsMIB.setRevisions(
        ("2004-12-06 00:00",
         "2002-08-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsVlanObjects_ObjectIdentity = ObjectIdentity
rsVlanObjects = _RsVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1)
)
_RsVlanStats_ObjectIdentity = ObjectIdentity
rsVlanStats = _RsVlanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10)
)
_RsPortVlanStatsTable_Object = MibTable
rsPortVlanStatsTable = _RsPortVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1)
)
if mibBuilder.loadTexts:
    rsPortVlanStatsTable.setStatus("current")
_RsPortVlanStatsEntry_Object = MibTableRow
rsPortVlanStatsEntry = _RsPortVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1)
)
rsPortVlanStatsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rsPortVlanStatsEntry.setStatus("current")
_RsPortVlanInOctets_Type = Counter32
_RsPortVlanInOctets_Object = MibTableColumn
rsPortVlanInOctets = _RsPortVlanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 101),
    _RsPortVlanInOctets_Type()
)
rsPortVlanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortVlanInOctets.setStatus("current")
_RsPortVlanOutOctets_Type = Counter32
_RsPortVlanOutOctets_Object = MibTableColumn
rsPortVlanOutOctets = _RsPortVlanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 102),
    _RsPortVlanOutOctets_Type()
)
rsPortVlanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortVlanOutOctets.setStatus("current")
_RsPortVlanInOverflowOctets_Type = Counter32
_RsPortVlanInOverflowOctets_Object = MibTableColumn
rsPortVlanInOverflowOctets = _RsPortVlanInOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 103),
    _RsPortVlanInOverflowOctets_Type()
)
rsPortVlanInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortVlanInOverflowOctets.setStatus("current")
_RsPortVlanOutOverflowOctets_Type = Counter32
_RsPortVlanOutOverflowOctets_Object = MibTableColumn
rsPortVlanOutOverflowOctets = _RsPortVlanOutOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 104),
    _RsPortVlanOutOverflowOctets_Type()
)
rsPortVlanOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortVlanOutOverflowOctets.setStatus("current")
_RsPortVlanHCStatsTable_Object = MibTable
rsPortVlanHCStatsTable = _RsPortVlanHCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2)
)
if mibBuilder.loadTexts:
    rsPortVlanHCStatsTable.setStatus("current")
_RsPortVlanHCStatsEntry_Object = MibTableRow
rsPortVlanHCStatsEntry = _RsPortVlanHCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1)
)
rsPortVlanHCStatsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rsPortVlanHCStatsEntry.setStatus("current")
_RsPortVlanHCInOctets_Type = Counter64
_RsPortVlanHCInOctets_Object = MibTableColumn
rsPortVlanHCInOctets = _RsPortVlanHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1, 101),
    _RsPortVlanHCInOctets_Type()
)
rsPortVlanHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortVlanHCInOctets.setStatus("current")
_RsPortVlanHCOutOctets_Type = Counter64
_RsPortVlanHCOutOctets_Object = MibTableColumn
rsPortVlanHCOutOctets = _RsPortVlanHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1, 102),
    _RsPortVlanHCOutOctets_Type()
)
rsPortVlanHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortVlanHCOutOctets.setStatus("current")
_RsPortCustomerVlanStatsTable_Object = MibTable
rsPortCustomerVlanStatsTable = _RsPortCustomerVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3)
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanStatsTable.setStatus("current")
_RsPortCustomerVlanStatsEntry_Object = MibTableRow
rsPortCustomerVlanStatsEntry = _RsPortCustomerVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1)
)
rsPortCustomerVlanStatsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanStatsEntry.setStatus("current")


class _RsPortCustomerIndex_Type(Integer32):
    """Custom type rsPortCustomerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsPortCustomerIndex_Type.__name__ = "Integer32"
_RsPortCustomerIndex_Object = MibTableColumn
rsPortCustomerIndex = _RsPortCustomerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 1),
    _RsPortCustomerIndex_Type()
)
rsPortCustomerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsPortCustomerIndex.setStatus("current")
_RsPortCustomerVlanInFrames_Type = Counter32
_RsPortCustomerVlanInFrames_Object = MibTableColumn
rsPortCustomerVlanInFrames = _RsPortCustomerVlanInFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 2),
    _RsPortCustomerVlanInFrames_Type()
)
rsPortCustomerVlanInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanInFrames.setStatus("current")
_RsPortCustomerVlanOutFrames_Type = Counter32
_RsPortCustomerVlanOutFrames_Object = MibTableColumn
rsPortCustomerVlanOutFrames = _RsPortCustomerVlanOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 3),
    _RsPortCustomerVlanOutFrames_Type()
)
rsPortCustomerVlanOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanOutFrames.setStatus("current")
_RsPortCustomerVlanInDiscards_Type = Counter32
_RsPortCustomerVlanInDiscards_Object = MibTableColumn
rsPortCustomerVlanInDiscards = _RsPortCustomerVlanInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 4),
    _RsPortCustomerVlanInDiscards_Type()
)
rsPortCustomerVlanInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanInDiscards.setStatus("current")
_RsPortCustomerVlanInOverflowFrames_Type = Counter32
_RsPortCustomerVlanInOverflowFrames_Object = MibTableColumn
rsPortCustomerVlanInOverflowFrames = _RsPortCustomerVlanInOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 5),
    _RsPortCustomerVlanInOverflowFrames_Type()
)
rsPortCustomerVlanInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanInOverflowFrames.setStatus("current")
_RsPortCustomerVlanOutOverflowFrames_Type = Counter32
_RsPortCustomerVlanOutOverflowFrames_Object = MibTableColumn
rsPortCustomerVlanOutOverflowFrames = _RsPortCustomerVlanOutOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 6),
    _RsPortCustomerVlanOutOverflowFrames_Type()
)
rsPortCustomerVlanOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanOutOverflowFrames.setStatus("current")
_RsPortCustomerVlanInOverflowDiscards_Type = Counter32
_RsPortCustomerVlanInOverflowDiscards_Object = MibTableColumn
rsPortCustomerVlanInOverflowDiscards = _RsPortCustomerVlanInOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 7),
    _RsPortCustomerVlanInOverflowDiscards_Type()
)
rsPortCustomerVlanInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanInOverflowDiscards.setStatus("current")
_RsPortCustomerVlanInOctets_Type = Counter32
_RsPortCustomerVlanInOctets_Object = MibTableColumn
rsPortCustomerVlanInOctets = _RsPortCustomerVlanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 8),
    _RsPortCustomerVlanInOctets_Type()
)
rsPortCustomerVlanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanInOctets.setStatus("current")
_RsPortCustomerVlanOutOctets_Type = Counter32
_RsPortCustomerVlanOutOctets_Object = MibTableColumn
rsPortCustomerVlanOutOctets = _RsPortCustomerVlanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 9),
    _RsPortCustomerVlanOutOctets_Type()
)
rsPortCustomerVlanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanOutOctets.setStatus("current")
_RsPortCustomerVlanInOverflowOctets_Type = Counter32
_RsPortCustomerVlanInOverflowOctets_Object = MibTableColumn
rsPortCustomerVlanInOverflowOctets = _RsPortCustomerVlanInOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 10),
    _RsPortCustomerVlanInOverflowOctets_Type()
)
rsPortCustomerVlanInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanInOverflowOctets.setStatus("current")
_RsPortCustomerVlanOutOverflowOctets_Type = Counter32
_RsPortCustomerVlanOutOverflowOctets_Object = MibTableColumn
rsPortCustomerVlanOutOverflowOctets = _RsPortCustomerVlanOutOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 11),
    _RsPortCustomerVlanOutOverflowOctets_Type()
)
rsPortCustomerVlanOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanOutOverflowOctets.setStatus("current")
_RsPortCustomerVlanHCStatsTable_Object = MibTable
rsPortCustomerVlanHCStatsTable = _RsPortCustomerVlanHCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4)
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCStatsTable.setStatus("current")
_RsPortCustomerVlanHCStatsEntry_Object = MibTableRow
rsPortCustomerVlanHCStatsEntry = _RsPortCustomerVlanHCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1)
)
rsPortCustomerVlanHCStatsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCStatsEntry.setStatus("current")
_RsPortCustomerVlanHCInFrames_Type = Counter64
_RsPortCustomerVlanHCInFrames_Object = MibTableColumn
rsPortCustomerVlanHCInFrames = _RsPortCustomerVlanHCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 1),
    _RsPortCustomerVlanHCInFrames_Type()
)
rsPortCustomerVlanHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCInFrames.setStatus("current")
_RsPortCustomerVlanHCOutFrames_Type = Counter64
_RsPortCustomerVlanHCOutFrames_Object = MibTableColumn
rsPortCustomerVlanHCOutFrames = _RsPortCustomerVlanHCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 2),
    _RsPortCustomerVlanHCOutFrames_Type()
)
rsPortCustomerVlanHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCOutFrames.setStatus("current")
_RsPortCustomerVlanHCInDiscards_Type = Counter64
_RsPortCustomerVlanHCInDiscards_Object = MibTableColumn
rsPortCustomerVlanHCInDiscards = _RsPortCustomerVlanHCInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 3),
    _RsPortCustomerVlanHCInDiscards_Type()
)
rsPortCustomerVlanHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCInDiscards.setStatus("current")
_RsPortCustomerVlanHCInOctets_Type = Counter64
_RsPortCustomerVlanHCInOctets_Object = MibTableColumn
rsPortCustomerVlanHCInOctets = _RsPortCustomerVlanHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 4),
    _RsPortCustomerVlanHCInOctets_Type()
)
rsPortCustomerVlanHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCInOctets.setStatus("current")
_RsPortCustomerVlanHCOutOctets_Type = Counter64
_RsPortCustomerVlanHCOutOctets_Object = MibTableColumn
rsPortCustomerVlanHCOutOctets = _RsPortCustomerVlanHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 5),
    _RsPortCustomerVlanHCOutOctets_Type()
)
rsPortCustomerVlanHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCOutOctets.setStatus("current")
_RsCustomerVlanStatsTable_Object = MibTable
rsCustomerVlanStatsTable = _RsCustomerVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5)
)
if mibBuilder.loadTexts:
    rsCustomerVlanStatsTable.setStatus("current")
_RsCustomerVlanStatsEntry_Object = MibTableRow
rsCustomerVlanStatsEntry = _RsCustomerVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1)
)
rsCustomerVlanStatsEntry.setIndexNames(
    (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rsCustomerVlanStatsEntry.setStatus("current")
_RsCustomerVlanInFrames_Type = Counter32
_RsCustomerVlanInFrames_Object = MibTableColumn
rsCustomerVlanInFrames = _RsCustomerVlanInFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 1),
    _RsCustomerVlanInFrames_Type()
)
rsCustomerVlanInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanInFrames.setStatus("current")
_RsCustomerVlanOutFrames_Type = Counter32
_RsCustomerVlanOutFrames_Object = MibTableColumn
rsCustomerVlanOutFrames = _RsCustomerVlanOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 2),
    _RsCustomerVlanOutFrames_Type()
)
rsCustomerVlanOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanOutFrames.setStatus("current")
_RsCustomerVlanInDiscards_Type = Counter32
_RsCustomerVlanInDiscards_Object = MibTableColumn
rsCustomerVlanInDiscards = _RsCustomerVlanInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 3),
    _RsCustomerVlanInDiscards_Type()
)
rsCustomerVlanInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanInDiscards.setStatus("current")
_RsCustomerVlanInOverflowFrames_Type = Counter32
_RsCustomerVlanInOverflowFrames_Object = MibTableColumn
rsCustomerVlanInOverflowFrames = _RsCustomerVlanInOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 4),
    _RsCustomerVlanInOverflowFrames_Type()
)
rsCustomerVlanInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanInOverflowFrames.setStatus("current")
_RsCustomerVlanOutOverflowFrames_Type = Counter32
_RsCustomerVlanOutOverflowFrames_Object = MibTableColumn
rsCustomerVlanOutOverflowFrames = _RsCustomerVlanOutOverflowFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 5),
    _RsCustomerVlanOutOverflowFrames_Type()
)
rsCustomerVlanOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanOutOverflowFrames.setStatus("current")
_RsCustomerVlanInOverflowDiscards_Type = Counter32
_RsCustomerVlanInOverflowDiscards_Object = MibTableColumn
rsCustomerVlanInOverflowDiscards = _RsCustomerVlanInOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 6),
    _RsCustomerVlanInOverflowDiscards_Type()
)
rsCustomerVlanInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanInOverflowDiscards.setStatus("current")
_RsCustomerVlanInOctets_Type = Counter32
_RsCustomerVlanInOctets_Object = MibTableColumn
rsCustomerVlanInOctets = _RsCustomerVlanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 7),
    _RsCustomerVlanInOctets_Type()
)
rsCustomerVlanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanInOctets.setStatus("current")
_RsCustomerVlanOutOctets_Type = Counter32
_RsCustomerVlanOutOctets_Object = MibTableColumn
rsCustomerVlanOutOctets = _RsCustomerVlanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 8),
    _RsCustomerVlanOutOctets_Type()
)
rsCustomerVlanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanOutOctets.setStatus("current")
_RsCustomerVlanInOverflowOctets_Type = Counter32
_RsCustomerVlanInOverflowOctets_Object = MibTableColumn
rsCustomerVlanInOverflowOctets = _RsCustomerVlanInOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 9),
    _RsCustomerVlanInOverflowOctets_Type()
)
rsCustomerVlanInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanInOverflowOctets.setStatus("current")
_RsCustomerVlanOutOverflowOctets_Type = Counter32
_RsCustomerVlanOutOverflowOctets_Object = MibTableColumn
rsCustomerVlanOutOverflowOctets = _RsCustomerVlanOutOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 10),
    _RsCustomerVlanOutOverflowOctets_Type()
)
rsCustomerVlanOutOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanOutOverflowOctets.setStatus("current")
_RsCustomerVlanHCStatsTable_Object = MibTable
rsCustomerVlanHCStatsTable = _RsCustomerVlanHCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6)
)
if mibBuilder.loadTexts:
    rsCustomerVlanHCStatsTable.setStatus("current")
_RsCustomerVlanHCStatsEntry_Object = MibTableRow
rsCustomerVlanHCStatsEntry = _RsCustomerVlanHCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1)
)
rsCustomerVlanHCStatsEntry.setIndexNames(
    (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rsCustomerVlanHCStatsEntry.setStatus("current")
_RsCustomerVlanHCInFrames_Type = Counter64
_RsCustomerVlanHCInFrames_Object = MibTableColumn
rsCustomerVlanHCInFrames = _RsCustomerVlanHCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 1),
    _RsCustomerVlanHCInFrames_Type()
)
rsCustomerVlanHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanHCInFrames.setStatus("current")
_RsCustomerVlanHCOutFrames_Type = Counter64
_RsCustomerVlanHCOutFrames_Object = MibTableColumn
rsCustomerVlanHCOutFrames = _RsCustomerVlanHCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 2),
    _RsCustomerVlanHCOutFrames_Type()
)
rsCustomerVlanHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanHCOutFrames.setStatus("current")
_RsCustomerVlanHCInDiscards_Type = Counter64
_RsCustomerVlanHCInDiscards_Object = MibTableColumn
rsCustomerVlanHCInDiscards = _RsCustomerVlanHCInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 3),
    _RsCustomerVlanHCInDiscards_Type()
)
rsCustomerVlanHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanHCInDiscards.setStatus("current")
_RsCustomerVlanHCInOctets_Type = Counter64
_RsCustomerVlanHCInOctets_Object = MibTableColumn
rsCustomerVlanHCInOctets = _RsCustomerVlanHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 4),
    _RsCustomerVlanHCInOctets_Type()
)
rsCustomerVlanHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanHCInOctets.setStatus("current")
_RsCustomerVlanHCOutOctets_Type = Counter64
_RsCustomerVlanHCOutOctets_Object = MibTableColumn
rsCustomerVlanHCOutOctets = _RsCustomerVlanHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 5),
    _RsCustomerVlanHCOutOctets_Type()
)
rsCustomerVlanHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCustomerVlanHCOutOctets.setStatus("current")
_RsVlanConformance_ObjectIdentity = ObjectIdentity
rsVlanConformance = _RsVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2)
)
_RsVlanCompliances_ObjectIdentity = ObjectIdentity
rsVlanCompliances = _RsVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 1)
)
_RsVlanGroups_ObjectIdentity = ObjectIdentity
rsVlanGroups = _RsVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2)
)

# Managed Objects groups

rsPortVlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 1)
)
rsPortVlanStatsGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanInOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanOutOctets"))
)
if mibBuilder.loadTexts:
    rsPortVlanStatsGroup.setStatus("current")

rsPortVlanStatsOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 2)
)
rsPortVlanStatsOverflowGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanInOverflowOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanOutOverflowOctets"))
)
if mibBuilder.loadTexts:
    rsPortVlanStatsOverflowGroup.setStatus("current")

rsPortVlanHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 3)
)
rsPortVlanHCStatsGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCInOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCOutOctets"))
)
if mibBuilder.loadTexts:
    rsPortVlanHCStatsGroup.setStatus("current")

rsPortCustomerVlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 4)
)
rsPortCustomerVlanStatsGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanInOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanOutOctets"))
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanStatsGroup.setStatus("current")

rsPortCustomerVlanStatsOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 5)
)
rsPortCustomerVlanStatsOverflowGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanInOverflowOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanOutOverflowOctets"))
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanStatsOverflowGroup.setStatus("current")

rsPortCustomerVlanHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 6)
)
rsPortCustomerVlanHCStatsGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCInOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCOutOctets"))
)
if mibBuilder.loadTexts:
    rsPortCustomerVlanHCStatsGroup.setStatus("current")

rsCustomerVlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 7)
)
rsCustomerVlanStatsGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanInOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanOutOctets"))
)
if mibBuilder.loadTexts:
    rsCustomerVlanStatsGroup.setStatus("current")

rsCustomerVlanStatsOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 8)
)
rsCustomerVlanStatsOverflowGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanInOverflowOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanOutOverflowOctets"))
)
if mibBuilder.loadTexts:
    rsCustomerVlanStatsOverflowGroup.setStatus("current")

rsCustomerVlanHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 9)
)
rsCustomerVlanHCStatsGroup.setObjects(
      *(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCInOctets"),
        ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCOutOctets"))
)
if mibBuilder.loadTexts:
    rsCustomerVlanHCStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-VLAN-EXTENSIONS-MIB",
    **{"rsVlanExtensionsMIB": rsVlanExtensionsMIB,
       "rsVlanObjects": rsVlanObjects,
       "rsVlanStats": rsVlanStats,
       "rsPortVlanStatsTable": rsPortVlanStatsTable,
       "rsPortVlanStatsEntry": rsPortVlanStatsEntry,
       "rsPortVlanInOctets": rsPortVlanInOctets,
       "rsPortVlanOutOctets": rsPortVlanOutOctets,
       "rsPortVlanInOverflowOctets": rsPortVlanInOverflowOctets,
       "rsPortVlanOutOverflowOctets": rsPortVlanOutOverflowOctets,
       "rsPortVlanHCStatsTable": rsPortVlanHCStatsTable,
       "rsPortVlanHCStatsEntry": rsPortVlanHCStatsEntry,
       "rsPortVlanHCInOctets": rsPortVlanHCInOctets,
       "rsPortVlanHCOutOctets": rsPortVlanHCOutOctets,
       "rsPortCustomerVlanStatsTable": rsPortCustomerVlanStatsTable,
       "rsPortCustomerVlanStatsEntry": rsPortCustomerVlanStatsEntry,
       "rsPortCustomerIndex": rsPortCustomerIndex,
       "rsPortCustomerVlanInFrames": rsPortCustomerVlanInFrames,
       "rsPortCustomerVlanOutFrames": rsPortCustomerVlanOutFrames,
       "rsPortCustomerVlanInDiscards": rsPortCustomerVlanInDiscards,
       "rsPortCustomerVlanInOverflowFrames": rsPortCustomerVlanInOverflowFrames,
       "rsPortCustomerVlanOutOverflowFrames": rsPortCustomerVlanOutOverflowFrames,
       "rsPortCustomerVlanInOverflowDiscards": rsPortCustomerVlanInOverflowDiscards,
       "rsPortCustomerVlanInOctets": rsPortCustomerVlanInOctets,
       "rsPortCustomerVlanOutOctets": rsPortCustomerVlanOutOctets,
       "rsPortCustomerVlanInOverflowOctets": rsPortCustomerVlanInOverflowOctets,
       "rsPortCustomerVlanOutOverflowOctets": rsPortCustomerVlanOutOverflowOctets,
       "rsPortCustomerVlanHCStatsTable": rsPortCustomerVlanHCStatsTable,
       "rsPortCustomerVlanHCStatsEntry": rsPortCustomerVlanHCStatsEntry,
       "rsPortCustomerVlanHCInFrames": rsPortCustomerVlanHCInFrames,
       "rsPortCustomerVlanHCOutFrames": rsPortCustomerVlanHCOutFrames,
       "rsPortCustomerVlanHCInDiscards": rsPortCustomerVlanHCInDiscards,
       "rsPortCustomerVlanHCInOctets": rsPortCustomerVlanHCInOctets,
       "rsPortCustomerVlanHCOutOctets": rsPortCustomerVlanHCOutOctets,
       "rsCustomerVlanStatsTable": rsCustomerVlanStatsTable,
       "rsCustomerVlanStatsEntry": rsCustomerVlanStatsEntry,
       "rsCustomerVlanInFrames": rsCustomerVlanInFrames,
       "rsCustomerVlanOutFrames": rsCustomerVlanOutFrames,
       "rsCustomerVlanInDiscards": rsCustomerVlanInDiscards,
       "rsCustomerVlanInOverflowFrames": rsCustomerVlanInOverflowFrames,
       "rsCustomerVlanOutOverflowFrames": rsCustomerVlanOutOverflowFrames,
       "rsCustomerVlanInOverflowDiscards": rsCustomerVlanInOverflowDiscards,
       "rsCustomerVlanInOctets": rsCustomerVlanInOctets,
       "rsCustomerVlanOutOctets": rsCustomerVlanOutOctets,
       "rsCustomerVlanInOverflowOctets": rsCustomerVlanInOverflowOctets,
       "rsCustomerVlanOutOverflowOctets": rsCustomerVlanOutOverflowOctets,
       "rsCustomerVlanHCStatsTable": rsCustomerVlanHCStatsTable,
       "rsCustomerVlanHCStatsEntry": rsCustomerVlanHCStatsEntry,
       "rsCustomerVlanHCInFrames": rsCustomerVlanHCInFrames,
       "rsCustomerVlanHCOutFrames": rsCustomerVlanHCOutFrames,
       "rsCustomerVlanHCInDiscards": rsCustomerVlanHCInDiscards,
       "rsCustomerVlanHCInOctets": rsCustomerVlanHCInOctets,
       "rsCustomerVlanHCOutOctets": rsCustomerVlanHCOutOctets,
       "rsVlanConformance": rsVlanConformance,
       "rsVlanCompliances": rsVlanCompliances,
       "rsVlanCompliance": rsVlanCompliance,
       "rsVlanGroups": rsVlanGroups,
       "rsPortVlanStatsGroup": rsPortVlanStatsGroup,
       "rsPortVlanStatsOverflowGroup": rsPortVlanStatsOverflowGroup,
       "rsPortVlanHCStatsGroup": rsPortVlanHCStatsGroup,
       "rsPortCustomerVlanStatsGroup": rsPortCustomerVlanStatsGroup,
       "rsPortCustomerVlanStatsOverflowGroup": rsPortCustomerVlanStatsOverflowGroup,
       "rsPortCustomerVlanHCStatsGroup": rsPortCustomerVlanHCStatsGroup,
       "rsCustomerVlanStatsGroup": rsCustomerVlanStatsGroup,
       "rsCustomerVlanStatsOverflowGroup": rsCustomerVlanStatsOverflowGroup,
       "rsCustomerVlanHCStatsGroup": rsCustomerVlanHCStatsGroup}
)
