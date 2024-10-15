# SNMP MIB module (HH3C-ENTRELATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ENTRELATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:06 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cEntityRelation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cEntRelationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("comboport", 2),
          ("stackport", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cEntRelationObjects_ObjectIdentity = ObjectIdentity
hh3cEntRelationObjects = _Hh3cEntRelationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1)
)
_Hh3cEntRelation_ObjectIdentity = ObjectIdentity
hh3cEntRelation = _Hh3cEntRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1)
)
_Hh3cEntRelationTable_Object = MibTable
hh3cEntRelationTable = _Hh3cEntRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEntRelationTable.setStatus("current")
_Hh3cEntRelationEntry_Object = MibTableRow
hh3cEntRelationEntry = _Hh3cEntRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1)
)
hh3cEntRelationEntry.setIndexNames(
    (0, "HH3C-ENTRELATION-MIB", "hh3cEntRelationType"),
    (0, "HH3C-ENTRELATION-MIB", "hh3cEntityIndex"),
    (0, "HH3C-ENTRELATION-MIB", "hh3cRelatedEntityIndex"),
)
if mibBuilder.loadTexts:
    hh3cEntRelationEntry.setStatus("current")
_Hh3cEntRelationType_Type = Hh3cEntRelationType
_Hh3cEntRelationType_Object = MibTableColumn
hh3cEntRelationType = _Hh3cEntRelationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 1),
    _Hh3cEntRelationType_Type()
)
hh3cEntRelationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEntRelationType.setStatus("current")
_Hh3cEntityIndex_Type = PhysicalIndex
_Hh3cEntityIndex_Object = MibTableColumn
hh3cEntityIndex = _Hh3cEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 2),
    _Hh3cEntityIndex_Type()
)
hh3cEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEntityIndex.setStatus("current")
_Hh3cRelatedEntityIndex_Type = PhysicalIndex
_Hh3cRelatedEntityIndex_Object = MibTableColumn
hh3cRelatedEntityIndex = _Hh3cRelatedEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 3),
    _Hh3cRelatedEntityIndex_Type()
)
hh3cRelatedEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRelatedEntityIndex.setStatus("current")
_Hh3cEntRelationConformance_ObjectIdentity = ObjectIdentity
hh3cEntRelationConformance = _Hh3cEntRelationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 2)
)
_Hh3cEntRelationCompliances_ObjectIdentity = ObjectIdentity
hh3cEntRelationCompliances = _Hh3cEntRelationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 1)
)
_Hh3cEntRelationGroups_ObjectIdentity = ObjectIdentity
hh3cEntRelationGroups = _Hh3cEntRelationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 2)
)

# Managed Objects groups

hh3cEntRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 2, 1)
)
hh3cEntRelationGroup.setObjects(
    ("HH3C-ENTRELATION-MIB", "hh3cRelatedEntityIndex")
)
if mibBuilder.loadTexts:
    hh3cEntRelationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cEntRelationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEntRelationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ENTRELATION-MIB",
    **{"Hh3cEntRelationType": Hh3cEntRelationType,
       "hh3cEntityRelation": hh3cEntityRelation,
       "hh3cEntRelationObjects": hh3cEntRelationObjects,
       "hh3cEntRelation": hh3cEntRelation,
       "hh3cEntRelationTable": hh3cEntRelationTable,
       "hh3cEntRelationEntry": hh3cEntRelationEntry,
       "hh3cEntRelationType": hh3cEntRelationType,
       "hh3cEntityIndex": hh3cEntityIndex,
       "hh3cRelatedEntityIndex": hh3cRelatedEntityIndex,
       "hh3cEntRelationConformance": hh3cEntRelationConformance,
       "hh3cEntRelationCompliances": hh3cEntRelationCompliances,
       "hh3cEntRelationCompliance": hh3cEntRelationCompliance,
       "hh3cEntRelationGroups": hh3cEntRelationGroups,
       "hh3cEntRelationGroup": hh3cEntRelationGroup}
)
