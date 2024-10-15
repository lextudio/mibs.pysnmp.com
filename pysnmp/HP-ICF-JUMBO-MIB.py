# SNMP MIB module (HP-ICF-JUMBO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-JUMBO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:41 2024
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

(hpicfObjectModules,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfObjectModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hpicfJumboMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13)
)
hpicfJumboMIB.setRevisions(
        ("2004-08-22 10:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfJumboObjects_ObjectIdentity = ObjectIdentity
hpicfJumboObjects = _HpicfJumboObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1)
)
_HpJumboStats_ObjectIdentity = ObjectIdentity
hpJumboStats = _HpJumboStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1)
)
_HpJumboStatsTable_Object = MibTable
hpJumboStatsTable = _HpJumboStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpJumboStatsTable.setStatus("current")
_HpJumboStatsEntry_Object = MibTableRow
hpJumboStatsEntry = _HpJumboStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1)
)
hpJumboStatsEntry.setIndexNames(
    (0, "HP-ICF-JUMBO-MIB", "hpJumboStatsIndex"),
)
if mibBuilder.loadTexts:
    hpJumboStatsEntry.setStatus("current")
_HpJumboStatsIndex_Type = InterfaceIndex
_HpJumboStatsIndex_Object = MibTableColumn
hpJumboStatsIndex = _HpJumboStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 1),
    _HpJumboStatsIndex_Type()
)
hpJumboStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpJumboStatsIndex.setStatus("current")
_HpJumboStatsPkts1523to2047Octets_Type = Counter32
_HpJumboStatsPkts1523to2047Octets_Object = MibTableColumn
hpJumboStatsPkts1523to2047Octets = _HpJumboStatsPkts1523to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 2),
    _HpJumboStatsPkts1523to2047Octets_Type()
)
hpJumboStatsPkts1523to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpJumboStatsPkts1523to2047Octets.setStatus("current")
_HpJumboStatsPkts2048to4095Octets_Type = Counter32
_HpJumboStatsPkts2048to4095Octets_Object = MibTableColumn
hpJumboStatsPkts2048to4095Octets = _HpJumboStatsPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 3),
    _HpJumboStatsPkts2048to4095Octets_Type()
)
hpJumboStatsPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpJumboStatsPkts2048to4095Octets.setStatus("current")
_HpJumboStatsPkts4096to9216Octets_Type = Counter32
_HpJumboStatsPkts4096to9216Octets_Object = MibTableColumn
hpJumboStatsPkts4096to9216Octets = _HpJumboStatsPkts4096to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 4),
    _HpJumboStatsPkts4096to9216Octets_Type()
)
hpJumboStatsPkts4096to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpJumboStatsPkts4096to9216Octets.setStatus("current")
_HpicfJumboConformance_ObjectIdentity = ObjectIdentity
hpicfJumboConformance = _HpicfJumboConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2)
)
_HpicfJumboGroups_ObjectIdentity = ObjectIdentity
hpicfJumboGroups = _HpicfJumboGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 1)
)
_HpicfJumboCompliances_ObjectIdentity = ObjectIdentity
hpicfJumboCompliances = _HpicfJumboCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 2)
)

# Managed Objects groups

hpicfJumboStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 1, 1)
)
hpicfJumboStatsGroup.setObjects(
      *(("HP-ICF-JUMBO-MIB", "hpJumboStatsIndex"),
        ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts1523to2047Octets"),
        ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts2048to4095Octets"),
        ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts4096to9216Octets"))
)
if mibBuilder.loadTexts:
    hpicfJumboStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfJumboCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfJumboCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-JUMBO-MIB",
    **{"hpicfJumboMIB": hpicfJumboMIB,
       "hpicfJumboObjects": hpicfJumboObjects,
       "hpJumboStats": hpJumboStats,
       "hpJumboStatsTable": hpJumboStatsTable,
       "hpJumboStatsEntry": hpJumboStatsEntry,
       "hpJumboStatsIndex": hpJumboStatsIndex,
       "hpJumboStatsPkts1523to2047Octets": hpJumboStatsPkts1523to2047Octets,
       "hpJumboStatsPkts2048to4095Octets": hpJumboStatsPkts2048to4095Octets,
       "hpJumboStatsPkts4096to9216Octets": hpJumboStatsPkts4096to9216Octets,
       "hpicfJumboConformance": hpicfJumboConformance,
       "hpicfJumboGroups": hpicfJumboGroups,
       "hpicfJumboStatsGroup": hpicfJumboStatsGroup,
       "hpicfJumboCompliances": hpicfJumboCompliances,
       "hpicfJumboCompliance": hpicfJumboCompliance}
)
