# SNMP MIB module (HP-ENTITY-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ENTITY-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:00 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpEntityPowerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71)
)
hpEntityPowerMIB.setRevisions(
        ("2010-04-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpEntPowerObjects_ObjectIdentity = ObjectIdentity
hpEntPowerObjects = _HpEntPowerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1)
)
_HpEntPowerTable_Object = MibTable
hpEntPowerTable = _HpEntPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1)
)
if mibBuilder.loadTexts:
    hpEntPowerTable.setStatus("current")
_HpEntPowerEntry_Object = MibTableRow
hpEntPowerEntry = _HpEntPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1)
)
hpEntPowerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpEntPowerEntry.setStatus("current")
_HpEntPowerMaxPowerUsage_Type = Unsigned32
_HpEntPowerMaxPowerUsage_Object = MibTableColumn
hpEntPowerMaxPowerUsage = _HpEntPowerMaxPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 1),
    _HpEntPowerMaxPowerUsage_Type()
)
hpEntPowerMaxPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPowerMaxPowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpEntPowerMaxPowerUsage.setUnits("Watts")
_HpEntPowerMinPowerUsage_Type = Unsigned32
_HpEntPowerMinPowerUsage_Object = MibTableColumn
hpEntPowerMinPowerUsage = _HpEntPowerMinPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 2),
    _HpEntPowerMinPowerUsage_Type()
)
hpEntPowerMinPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPowerMinPowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpEntPowerMinPowerUsage.setUnits("Watts")
_HpEntPowerCurrentPowerUsage_Type = Unsigned32
_HpEntPowerCurrentPowerUsage_Object = MibTableColumn
hpEntPowerCurrentPowerUsage = _HpEntPowerCurrentPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 3),
    _HpEntPowerCurrentPowerUsage_Type()
)
hpEntPowerCurrentPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPowerCurrentPowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpEntPowerCurrentPowerUsage.setUnits("Watts")
_HpEntPowerConformance_ObjectIdentity = ObjectIdentity
hpEntPowerConformance = _HpEntPowerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2)
)
_HpEntPowerCompliances_ObjectIdentity = ObjectIdentity
hpEntPowerCompliances = _HpEntPowerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1)
)
_HpEntPowerGroups_ObjectIdentity = ObjectIdentity
hpEntPowerGroups = _HpEntPowerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2)
)

# Managed Objects groups

hpEntPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2, 1)
)
hpEntPowerGroup.setObjects(
      *(("HP-ENTITY-POWER-MIB", "hpEntPowerMaxPowerUsage"),
        ("HP-ENTITY-POWER-MIB", "hpEntPowerMinPowerUsage"),
        ("HP-ENTITY-POWER-MIB", "hpEntPowerCurrentPowerUsage"))
)
if mibBuilder.loadTexts:
    hpEntPowerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpEntPowerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpEntPowerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ENTITY-POWER-MIB",
    **{"hpEntityPowerMIB": hpEntityPowerMIB,
       "hpEntPowerObjects": hpEntPowerObjects,
       "hpEntPowerTable": hpEntPowerTable,
       "hpEntPowerEntry": hpEntPowerEntry,
       "hpEntPowerMaxPowerUsage": hpEntPowerMaxPowerUsage,
       "hpEntPowerMinPowerUsage": hpEntPowerMinPowerUsage,
       "hpEntPowerCurrentPowerUsage": hpEntPowerCurrentPowerUsage,
       "hpEntPowerConformance": hpEntPowerConformance,
       "hpEntPowerCompliances": hpEntPowerCompliances,
       "hpEntPowerCompliance": hpEntPowerCompliance,
       "hpEntPowerGroups": hpEntPowerGroups,
       "hpEntPowerGroup": hpEntPowerGroup}
)
