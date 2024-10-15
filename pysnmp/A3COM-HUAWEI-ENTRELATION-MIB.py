# SNMP MIB module (A3COM-HUAWEI-ENTRELATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-ENTRELATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:52 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

h3cEntityRelation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cEntRelationType(Integer32, TextualConvention):
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

_H3cEntRelationObjects_ObjectIdentity = ObjectIdentity
h3cEntRelationObjects = _H3cEntRelationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1)
)
_H3cEntRelation_ObjectIdentity = ObjectIdentity
h3cEntRelation = _H3cEntRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1)
)
_H3cEntRelationTable_Object = MibTable
h3cEntRelationTable = _H3cEntRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEntRelationTable.setStatus("current")
_H3cEntRelationEntry_Object = MibTableRow
h3cEntRelationEntry = _H3cEntRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1)
)
h3cEntRelationEntry.setIndexNames(
    (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntRelationType"),
    (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntityIndex"),
    (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cRelatedEntityIndex"),
)
if mibBuilder.loadTexts:
    h3cEntRelationEntry.setStatus("current")
_H3cEntRelationType_Type = H3cEntRelationType
_H3cEntRelationType_Object = MibTableColumn
h3cEntRelationType = _H3cEntRelationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 1),
    _H3cEntRelationType_Type()
)
h3cEntRelationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEntRelationType.setStatus("current")
_H3cEntityIndex_Type = PhysicalIndex
_H3cEntityIndex_Object = MibTableColumn
h3cEntityIndex = _H3cEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 2),
    _H3cEntityIndex_Type()
)
h3cEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEntityIndex.setStatus("current")
_H3cRelatedEntityIndex_Type = PhysicalIndex
_H3cRelatedEntityIndex_Object = MibTableColumn
h3cRelatedEntityIndex = _H3cRelatedEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 3),
    _H3cRelatedEntityIndex_Type()
)
h3cRelatedEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRelatedEntityIndex.setStatus("current")
_H3cEntRelationConformance_ObjectIdentity = ObjectIdentity
h3cEntRelationConformance = _H3cEntRelationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2)
)
_H3cEntRelationCompliances_ObjectIdentity = ObjectIdentity
h3cEntRelationCompliances = _H3cEntRelationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 1)
)
_H3cEntRelationGroups_ObjectIdentity = ObjectIdentity
h3cEntRelationGroups = _H3cEntRelationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 2)
)

# Managed Objects groups

h3cEntRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 2, 1)
)
h3cEntRelationGroup.setObjects(
    ("A3COM-HUAWEI-ENTRELATION-MIB", "h3cRelatedEntityIndex")
)
if mibBuilder.loadTexts:
    h3cEntRelationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cEntRelationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEntRelationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-ENTRELATION-MIB",
    **{"H3cEntRelationType": H3cEntRelationType,
       "h3cEntityRelation": h3cEntityRelation,
       "h3cEntRelationObjects": h3cEntRelationObjects,
       "h3cEntRelation": h3cEntRelation,
       "h3cEntRelationTable": h3cEntRelationTable,
       "h3cEntRelationEntry": h3cEntRelationEntry,
       "h3cEntRelationType": h3cEntRelationType,
       "h3cEntityIndex": h3cEntityIndex,
       "h3cRelatedEntityIndex": h3cRelatedEntityIndex,
       "h3cEntRelationConformance": h3cEntRelationConformance,
       "h3cEntRelationCompliances": h3cEntRelationCompliances,
       "h3cEntRelationCompliance": h3cEntRelationCompliance,
       "h3cEntRelationGroups": h3cEntRelationGroups,
       "h3cEntRelationGroup": h3cEntRelationGroup}
)
