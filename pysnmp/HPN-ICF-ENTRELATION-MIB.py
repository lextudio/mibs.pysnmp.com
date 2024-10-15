# SNMP MIB module (HPN-ICF-ENTRELATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-ENTRELATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:05 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfEntityRelation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfEntRelationType(Integer32, TextualConvention):
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

_HpnicfEntRelationObjects_ObjectIdentity = ObjectIdentity
hpnicfEntRelationObjects = _HpnicfEntRelationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1)
)
_HpnicfEntRelation_ObjectIdentity = ObjectIdentity
hpnicfEntRelation = _HpnicfEntRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1)
)
_HpnicfEntRelationTable_Object = MibTable
hpnicfEntRelationTable = _HpnicfEntRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntRelationTable.setStatus("current")
_HpnicfEntRelationEntry_Object = MibTableRow
hpnicfEntRelationEntry = _HpnicfEntRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1)
)
hpnicfEntRelationEntry.setIndexNames(
    (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationType"),
    (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntityIndex"),
    (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEntRelationEntry.setStatus("current")
_HpnicfEntRelationType_Type = HpnicfEntRelationType
_HpnicfEntRelationType_Object = MibTableColumn
hpnicfEntRelationType = _HpnicfEntRelationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 1),
    _HpnicfEntRelationType_Type()
)
hpnicfEntRelationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEntRelationType.setStatus("current")
_HpnicfEntityIndex_Type = PhysicalIndex
_HpnicfEntityIndex_Object = MibTableColumn
hpnicfEntityIndex = _HpnicfEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 2),
    _HpnicfEntityIndex_Type()
)
hpnicfEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEntityIndex.setStatus("current")
_HpnicfRelatedEntityIndex_Type = PhysicalIndex
_HpnicfRelatedEntityIndex_Object = MibTableColumn
hpnicfRelatedEntityIndex = _HpnicfRelatedEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 3),
    _HpnicfRelatedEntityIndex_Type()
)
hpnicfRelatedEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRelatedEntityIndex.setStatus("current")
_HpnicfEntRelationConformance_ObjectIdentity = ObjectIdentity
hpnicfEntRelationConformance = _HpnicfEntRelationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2)
)
_HpnicfEntRelationCompliances_ObjectIdentity = ObjectIdentity
hpnicfEntRelationCompliances = _HpnicfEntRelationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1)
)
_HpnicfEntRelationGroups_ObjectIdentity = ObjectIdentity
hpnicfEntRelationGroups = _HpnicfEntRelationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2)
)

# Managed Objects groups

hpnicfEntRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2, 1)
)
hpnicfEntRelationGroup.setObjects(
    ("HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex")
)
if mibBuilder.loadTexts:
    hpnicfEntRelationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfEntRelationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEntRelationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ENTRELATION-MIB",
    **{"HpnicfEntRelationType": HpnicfEntRelationType,
       "hpnicfEntityRelation": hpnicfEntityRelation,
       "hpnicfEntRelationObjects": hpnicfEntRelationObjects,
       "hpnicfEntRelation": hpnicfEntRelation,
       "hpnicfEntRelationTable": hpnicfEntRelationTable,
       "hpnicfEntRelationEntry": hpnicfEntRelationEntry,
       "hpnicfEntRelationType": hpnicfEntRelationType,
       "hpnicfEntityIndex": hpnicfEntityIndex,
       "hpnicfRelatedEntityIndex": hpnicfRelatedEntityIndex,
       "hpnicfEntRelationConformance": hpnicfEntRelationConformance,
       "hpnicfEntRelationCompliances": hpnicfEntRelationCompliances,
       "hpnicfEntRelationCompliance": hpnicfEntRelationCompliance,
       "hpnicfEntRelationGroups": hpnicfEntRelationGroups,
       "hpnicfEntRelationGroup": hpnicfEntRelationGroup}
)
