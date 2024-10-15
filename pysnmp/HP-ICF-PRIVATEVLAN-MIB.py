# SNMP MIB module (HP-ICF-PRIVATEVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-PRIVATEVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:00 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "VidList")

(VlanId,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "dot1qVlanStaticEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfPrivateVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114)
)
hpicfPrivateVlan.setRevisions(
        ("2015-04-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PrivateVlanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("community", 4),
          ("isolated", 3),
          ("notAPrivateVLAN", 1),
          ("primary", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfPrivateVlanObjects_ObjectIdentity = ObjectIdentity
hpicfPrivateVlanObjects = _HpicfPrivateVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1)
)
_HpicfPrivateVlanConfig_ObjectIdentity = ObjectIdentity
hpicfPrivateVlanConfig = _HpicfPrivateVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1)
)
_HpicfPrivateVlanTable_Object = MibTable
hpicfPrivateVlanTable = _HpicfPrivateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPrivateVlanTable.setStatus("current")
_HpicfPrivateVlanEntry_Object = MibTableRow
hpicfPrivateVlanEntry = _HpicfPrivateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPrivateVlanEntry.setStatus("current")


class _HpicfPrivateVlanType_Type(PrivateVlanType):
    """Custom type hpicfPrivateVlanType based on PrivateVlanType"""


_HpicfPrivateVlanType_Object = MibTableColumn
hpicfPrivateVlanType = _HpicfPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1, 1),
    _HpicfPrivateVlanType_Type()
)
hpicfPrivateVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPrivateVlanType.setStatus("current")
_HpicfPrivateVlanMappingTable_Object = MibTable
hpicfPrivateVlanMappingTable = _HpicfPrivateVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfPrivateVlanMappingTable.setStatus("current")
_HpicfPrivateVlanMappingEntry_Object = MibTableRow
hpicfPrivateVlanMappingEntry = _HpicfPrivateVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1)
)
hpicfPrivateVlanMappingEntry.setIndexNames(
    (0, "HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanPrimary"),
)
if mibBuilder.loadTexts:
    hpicfPrivateVlanMappingEntry.setStatus("current")
_HpicfPrivateVlanPrimary_Type = VlanId
_HpicfPrivateVlanPrimary_Object = MibTableColumn
hpicfPrivateVlanPrimary = _HpicfPrivateVlanPrimary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 1),
    _HpicfPrivateVlanPrimary_Type()
)
hpicfPrivateVlanPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPrivateVlanPrimary.setStatus("current")


class _HpicfPrivateVlanIsolated_Type(Integer32):
    """Custom type hpicfPrivateVlanIsolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfPrivateVlanIsolated_Type.__name__ = "Integer32"
_HpicfPrivateVlanIsolated_Object = MibTableColumn
hpicfPrivateVlanIsolated = _HpicfPrivateVlanIsolated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 2),
    _HpicfPrivateVlanIsolated_Type()
)
hpicfPrivateVlanIsolated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPrivateVlanIsolated.setStatus("current")
_HpicfPrivateVlanCommunity_Type = VidList
_HpicfPrivateVlanCommunity_Object = MibTableColumn
hpicfPrivateVlanCommunity = _HpicfPrivateVlanCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 3),
    _HpicfPrivateVlanCommunity_Type()
)
hpicfPrivateVlanCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPrivateVlanCommunity.setStatus("current")
_HpicfPrivateVlanMappingRowStatus_Type = RowStatus
_HpicfPrivateVlanMappingRowStatus_Object = MibTableColumn
hpicfPrivateVlanMappingRowStatus = _HpicfPrivateVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 4),
    _HpicfPrivateVlanMappingRowStatus_Type()
)
hpicfPrivateVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPrivateVlanMappingRowStatus.setStatus("current")
_HpicfPrivateVlanConformance_ObjectIdentity = ObjectIdentity
hpicfPrivateVlanConformance = _HpicfPrivateVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2)
)
_HpicfPrivateVlanCompliances_ObjectIdentity = ObjectIdentity
hpicfPrivateVlanCompliances = _HpicfPrivateVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1)
)
_HpicfPrivateVlanGroup_ObjectIdentity = ObjectIdentity
hpicfPrivateVlanGroup = _HpicfPrivateVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2)
)
dot1qVlanStaticEntry.registerAugmentions(
    ("HP-ICF-PRIVATEVLAN-MIB",
     "hpicfPrivateVlanEntry")
)
hpicfPrivateVlanEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

hpicfPrivateVlanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 1)
)
hpicfPrivateVlanTableGroup.setObjects(
    ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanType")
)
if mibBuilder.loadTexts:
    hpicfPrivateVlanTableGroup.setStatus("current")

hpicfPVlanMappingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 2)
)
hpicfPVlanMappingTableGroup.setObjects(
      *(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanIsolated"),
        ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanCommunity"),
        ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfPVlanMappingTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfPVlanTableCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPVlanTableCompliance.setStatus(
        "current"
    )

hpicfPVlanMappingTblCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfPVlanMappingTblCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-PRIVATEVLAN-MIB",
    **{"PrivateVlanType": PrivateVlanType,
       "hpicfPrivateVlan": hpicfPrivateVlan,
       "hpicfPrivateVlanObjects": hpicfPrivateVlanObjects,
       "hpicfPrivateVlanConfig": hpicfPrivateVlanConfig,
       "hpicfPrivateVlanTable": hpicfPrivateVlanTable,
       "hpicfPrivateVlanEntry": hpicfPrivateVlanEntry,
       "hpicfPrivateVlanType": hpicfPrivateVlanType,
       "hpicfPrivateVlanMappingTable": hpicfPrivateVlanMappingTable,
       "hpicfPrivateVlanMappingEntry": hpicfPrivateVlanMappingEntry,
       "hpicfPrivateVlanPrimary": hpicfPrivateVlanPrimary,
       "hpicfPrivateVlanIsolated": hpicfPrivateVlanIsolated,
       "hpicfPrivateVlanCommunity": hpicfPrivateVlanCommunity,
       "hpicfPrivateVlanMappingRowStatus": hpicfPrivateVlanMappingRowStatus,
       "hpicfPrivateVlanConformance": hpicfPrivateVlanConformance,
       "hpicfPrivateVlanCompliances": hpicfPrivateVlanCompliances,
       "hpicfPVlanTableCompliance": hpicfPVlanTableCompliance,
       "hpicfPVlanMappingTblCompliance": hpicfPVlanMappingTblCompliance,
       "hpicfPrivateVlanGroup": hpicfPrivateVlanGroup,
       "hpicfPrivateVlanTableGroup": hpicfPrivateVlanTableGroup,
       "hpicfPVlanMappingTableGroup": hpicfPVlanMappingTableGroup}
)
