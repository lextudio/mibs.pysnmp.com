# SNMP MIB module (MY-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-PRIVATE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:23 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myPrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44)
)
myPrivateVlanMIB.setRevisions(
        ("2009-03-01 00:00",)
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
          ("normal", 1),
          ("primary", 2))
    )



class VlanIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class VlanIndexBitmap(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs

_MypvlanMIBObjects_ObjectIdentity = ObjectIdentity
mypvlanMIBObjects = _MypvlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1)
)
_MypvlanVlanObjects_ObjectIdentity = ObjectIdentity
mypvlanVlanObjects = _MypvlanVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1)
)
_MypvlanVlanTable_Object = MibTable
mypvlanVlanTable = _MypvlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mypvlanVlanTable.setStatus("current")
_MypvlanVlanEntry_Object = MibTableRow
mypvlanVlanEntry = _MypvlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1)
)
mypvlanVlanEntry.setIndexNames(
    (0, "MY-PRIVATE-VLAN-MIB", "mypvlanVlanIndex"),
)
if mibBuilder.loadTexts:
    mypvlanVlanEntry.setStatus("current")
_MypvlanVlanIndex_Type = VlanIndexOrZero
_MypvlanVlanIndex_Object = MibTableColumn
mypvlanVlanIndex = _MypvlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 1),
    _MypvlanVlanIndex_Type()
)
mypvlanVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mypvlanVlanIndex.setStatus("current")
_MypvlanVlanPrivateVlanType_Type = PrivateVlanType
_MypvlanVlanPrivateVlanType_Object = MibTableColumn
mypvlanVlanPrivateVlanType = _MypvlanVlanPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 2),
    _MypvlanVlanPrivateVlanType_Type()
)
mypvlanVlanPrivateVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mypvlanVlanPrivateVlanType.setStatus("current")
_MypvlanVlanAssociatedPrimaryVlan_Type = VlanIndexOrZero
_MypvlanVlanAssociatedPrimaryVlan_Object = MibTableColumn
mypvlanVlanAssociatedPrimaryVlan = _MypvlanVlanAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 3),
    _MypvlanVlanAssociatedPrimaryVlan_Type()
)
mypvlanVlanAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mypvlanVlanAssociatedPrimaryVlan.setStatus("current")
_MypvlanIfAssociatedPrimaryVlan_Type = TruthValue
_MypvlanIfAssociatedPrimaryVlan_Object = MibTableColumn
mypvlanIfAssociatedPrimaryVlan = _MypvlanIfAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 4),
    _MypvlanIfAssociatedPrimaryVlan_Type()
)
mypvlanIfAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mypvlanIfAssociatedPrimaryVlan.setStatus("current")
_MypvlanPortObjects_ObjectIdentity = ObjectIdentity
mypvlanPortObjects = _MypvlanPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2)
)
_MypvlanPrivatePortTable_Object = MibTable
mypvlanPrivatePortTable = _MypvlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mypvlanPrivatePortTable.setStatus("current")
_MypvlanPrivatePortEntry_Object = MibTableRow
mypvlanPrivatePortEntry = _MypvlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1)
)
mypvlanPrivatePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mypvlanPrivatePortEntry.setStatus("current")
_MypvlanPrivatePortPrimaryVlan_Type = VlanIndexOrZero
_MypvlanPrivatePortPrimaryVlan_Object = MibTableColumn
mypvlanPrivatePortPrimaryVlan = _MypvlanPrivatePortPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1, 1),
    _MypvlanPrivatePortPrimaryVlan_Type()
)
mypvlanPrivatePortPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPrivatePortPrimaryVlan.setStatus("current")
_MypvlanPrivatePortSecondaryVlan_Type = VlanIndexOrZero
_MypvlanPrivatePortSecondaryVlan_Object = MibTableColumn
mypvlanPrivatePortSecondaryVlan = _MypvlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1, 2),
    _MypvlanPrivatePortSecondaryVlan_Type()
)
mypvlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPrivatePortSecondaryVlan.setStatus("current")
_MypvlanPromPortTable_Object = MibTable
mypvlanPromPortTable = _MypvlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mypvlanPromPortTable.setStatus("current")
_MypvlanPromPortEntry_Object = MibTableRow
mypvlanPromPortEntry = _MypvlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1)
)
mypvlanPromPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mypvlanPromPortEntry.setStatus("current")
_MypvlanPrivatePortPrimaryVlanId_Type = VlanIndexOrZero
_MypvlanPrivatePortPrimaryVlanId_Object = MibTableColumn
mypvlanPrivatePortPrimaryVlanId = _MypvlanPrivatePortPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 1),
    _MypvlanPrivatePortPrimaryVlanId_Type()
)
mypvlanPrivatePortPrimaryVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPrivatePortPrimaryVlanId.setStatus("current")


class _MypvlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type mypvlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MypvlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_MypvlanPromPortSecondaryRemap_Object = MibTableColumn
mypvlanPromPortSecondaryRemap = _MypvlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 2),
    _MypvlanPromPortSecondaryRemap_Type()
)
mypvlanPromPortSecondaryRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPromPortSecondaryRemap.setStatus("current")


class _MypvlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type mypvlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MypvlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_MypvlanPromPortSecondaryRemap2k_Object = MibTableColumn
mypvlanPromPortSecondaryRemap2k = _MypvlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 3),
    _MypvlanPromPortSecondaryRemap2k_Type()
)
mypvlanPromPortSecondaryRemap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPromPortSecondaryRemap2k.setStatus("current")


class _MypvlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type mypvlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MypvlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_MypvlanPromPortSecondaryRemap3k_Object = MibTableColumn
mypvlanPromPortSecondaryRemap3k = _MypvlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 4),
    _MypvlanPromPortSecondaryRemap3k_Type()
)
mypvlanPromPortSecondaryRemap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPromPortSecondaryRemap3k.setStatus("current")


class _MypvlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type mypvlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MypvlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_MypvlanPromPortSecondaryRemap4k_Object = MibTableColumn
mypvlanPromPortSecondaryRemap4k = _MypvlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 5),
    _MypvlanPromPortSecondaryRemap4k_Type()
)
mypvlanPromPortSecondaryRemap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPromPortSecondaryRemap4k.setStatus("current")
_MypvlanPortModeTable_Object = MibTable
mypvlanPortModeTable = _MypvlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mypvlanPortModeTable.setStatus("current")
_MypvlanPortModeEntry_Object = MibTableRow
mypvlanPortModeEntry = _MypvlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3, 1)
)
mypvlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mypvlanPortModeEntry.setStatus("current")


class _MypvlanPortMode_Type(Integer32):
    """Custom type mypvlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("nonPrivateVlan", 1),
          ("promiscuous", 3))
    )


_MypvlanPortMode_Type.__name__ = "Integer32"
_MypvlanPortMode_Object = MibTableColumn
mypvlanPortMode = _MypvlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3, 1, 1),
    _MypvlanPortMode_Type()
)
mypvlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanPortMode.setStatus("current")
_MypvlanSVIObjects_ObjectIdentity = ObjectIdentity
mypvlanSVIObjects = _MypvlanSVIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3)
)
_MypvlanSVIMappingTable_Object = MibTable
mypvlanSVIMappingTable = _MypvlanSVIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mypvlanSVIMappingTable.setStatus("current")
_MypvlanSVIMappingEntry_Object = MibTableRow
mypvlanSVIMappingEntry = _MypvlanSVIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1)
)
mypvlanSVIMappingEntry.setIndexNames(
    (0, "MY-PRIVATE-VLAN-MIB", "mypvlanSVIMappingVlanIndex"),
)
if mibBuilder.loadTexts:
    mypvlanSVIMappingEntry.setStatus("current")
_MypvlanSVIMappingVlanIndex_Type = VlanIndexOrZero
_MypvlanSVIMappingVlanIndex_Object = MibTableColumn
mypvlanSVIMappingVlanIndex = _MypvlanSVIMappingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1, 1),
    _MypvlanSVIMappingVlanIndex_Type()
)
mypvlanSVIMappingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mypvlanSVIMappingVlanIndex.setStatus("current")
_MypvlanSVIMappingPrimarySVI_Type = VlanIndexOrZero
_MypvlanSVIMappingPrimarySVI_Object = MibTableColumn
mypvlanSVIMappingPrimarySVI = _MypvlanSVIMappingPrimarySVI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1, 2),
    _MypvlanSVIMappingPrimarySVI_Type()
)
mypvlanSVIMappingPrimarySVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mypvlanSVIMappingPrimarySVI.setStatus("current")
_MypvlanMIBConformance_ObjectIdentity = ObjectIdentity
mypvlanMIBConformance = _MypvlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2)
)
_MypvlanMIBCompliances_ObjectIdentity = ObjectIdentity
mypvlanMIBCompliances = _MypvlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 1)
)
_MypvlanMIBGroups_ObjectIdentity = ObjectIdentity
mypvlanMIBGroups = _MypvlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2)
)

# Managed Objects groups

mypvlanVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 1)
)
mypvlanVlanGroup.setObjects(
      *(("MY-PRIVATE-VLAN-MIB", "mypvlanVlanIndex"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanVlanPrivateVlanType"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanVlanAssociatedPrimaryVlan"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanIfAssociatedPrimaryVlan"))
)
if mibBuilder.loadTexts:
    mypvlanVlanGroup.setStatus("current")

mypvlanPrivatePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 2)
)
mypvlanPrivatePortGroup.setObjects(
      *(("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortPrimaryVlan"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortSecondaryVlan"))
)
if mibBuilder.loadTexts:
    mypvlanPrivatePortGroup.setStatus("current")

mypvlanPromPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 3)
)
mypvlanPromPortGroup.setObjects(
      *(("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortPrimaryVlan"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap2k"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap3k"),
        ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap4k"))
)
if mibBuilder.loadTexts:
    mypvlanPromPortGroup.setStatus("current")

mypvlanPortModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 4)
)
mypvlanPortModeGroup.setObjects(
    ("MY-PRIVATE-VLAN-MIB", "mypvlanPortMode")
)
if mibBuilder.loadTexts:
    mypvlanPortModeGroup.setStatus("current")

mypvlanSVIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 5)
)
mypvlanSVIGroup.setObjects(
    ("MY-PRIVATE-VLAN-MIB", "mypvlanSVIMappingPrimarySVI")
)
if mibBuilder.loadTexts:
    mypvlanSVIGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mypvlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mypvlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-PRIVATE-VLAN-MIB",
    **{"PrivateVlanType": PrivateVlanType,
       "VlanIndexOrZero": VlanIndexOrZero,
       "VlanIndexBitmap": VlanIndexBitmap,
       "myPrivateVlanMIB": myPrivateVlanMIB,
       "mypvlanMIBObjects": mypvlanMIBObjects,
       "mypvlanVlanObjects": mypvlanVlanObjects,
       "mypvlanVlanTable": mypvlanVlanTable,
       "mypvlanVlanEntry": mypvlanVlanEntry,
       "mypvlanVlanIndex": mypvlanVlanIndex,
       "mypvlanVlanPrivateVlanType": mypvlanVlanPrivateVlanType,
       "mypvlanVlanAssociatedPrimaryVlan": mypvlanVlanAssociatedPrimaryVlan,
       "mypvlanIfAssociatedPrimaryVlan": mypvlanIfAssociatedPrimaryVlan,
       "mypvlanPortObjects": mypvlanPortObjects,
       "mypvlanPrivatePortTable": mypvlanPrivatePortTable,
       "mypvlanPrivatePortEntry": mypvlanPrivatePortEntry,
       "mypvlanPrivatePortPrimaryVlan": mypvlanPrivatePortPrimaryVlan,
       "mypvlanPrivatePortSecondaryVlan": mypvlanPrivatePortSecondaryVlan,
       "mypvlanPromPortTable": mypvlanPromPortTable,
       "mypvlanPromPortEntry": mypvlanPromPortEntry,
       "mypvlanPrivatePortPrimaryVlanId": mypvlanPrivatePortPrimaryVlanId,
       "mypvlanPromPortSecondaryRemap": mypvlanPromPortSecondaryRemap,
       "mypvlanPromPortSecondaryRemap2k": mypvlanPromPortSecondaryRemap2k,
       "mypvlanPromPortSecondaryRemap3k": mypvlanPromPortSecondaryRemap3k,
       "mypvlanPromPortSecondaryRemap4k": mypvlanPromPortSecondaryRemap4k,
       "mypvlanPortModeTable": mypvlanPortModeTable,
       "mypvlanPortModeEntry": mypvlanPortModeEntry,
       "mypvlanPortMode": mypvlanPortMode,
       "mypvlanSVIObjects": mypvlanSVIObjects,
       "mypvlanSVIMappingTable": mypvlanSVIMappingTable,
       "mypvlanSVIMappingEntry": mypvlanSVIMappingEntry,
       "mypvlanSVIMappingVlanIndex": mypvlanSVIMappingVlanIndex,
       "mypvlanSVIMappingPrimarySVI": mypvlanSVIMappingPrimarySVI,
       "mypvlanMIBConformance": mypvlanMIBConformance,
       "mypvlanMIBCompliances": mypvlanMIBCompliances,
       "mypvlanMIBCompliance": mypvlanMIBCompliance,
       "mypvlanMIBGroups": mypvlanMIBGroups,
       "mypvlanVlanGroup": mypvlanVlanGroup,
       "mypvlanPrivatePortGroup": mypvlanPrivatePortGroup,
       "mypvlanPromPortGroup": mypvlanPromPortGroup,
       "mypvlanPortModeGroup": mypvlanPortModeGroup,
       "mypvlanSVIGroup": mypvlanSVIGroup}
)
