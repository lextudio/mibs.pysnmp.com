# SNMP MIB module (CISCO-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PRIVATE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:12 2024
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

(vtpVlanEditEntry,
 vtpVlanEntry) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "vtpVlanEditEntry",
    "vtpVlanEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173)
)
ciscoPrivateVlanMIB.setRevisions(
        ("2005-09-08 00:00",
         "2002-07-24 00:00",
         "2001-05-23 00:00",
         "2001-04-17 00:00")
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("community", 4),
          ("isolated", 3),
          ("normal", 1),
          ("primary", 2),
          ("twoWayCommunity", 5))
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

_CpvlanMIBObjects_ObjectIdentity = ObjectIdentity
cpvlanMIBObjects = _CpvlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1)
)
_CpvlanVlanObjects_ObjectIdentity = ObjectIdentity
cpvlanVlanObjects = _CpvlanVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1)
)
_CpvlanVlanTable_Object = MibTable
cpvlanVlanTable = _CpvlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpvlanVlanTable.setStatus("current")
_CpvlanVlanEntry_Object = MibTableRow
cpvlanVlanEntry = _CpvlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpvlanVlanEntry.setStatus("current")
_CpvlanVlanPrivateVlanType_Type = PrivateVlanType
_CpvlanVlanPrivateVlanType_Object = MibTableColumn
cpvlanVlanPrivateVlanType = _CpvlanVlanPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1, 1, 1),
    _CpvlanVlanPrivateVlanType_Type()
)
cpvlanVlanPrivateVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvlanVlanPrivateVlanType.setStatus("current")
_CpvlanVlanAssociatedPrimaryVlan_Type = VlanIndexOrZero
_CpvlanVlanAssociatedPrimaryVlan_Object = MibTableColumn
cpvlanVlanAssociatedPrimaryVlan = _CpvlanVlanAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 1, 1, 2),
    _CpvlanVlanAssociatedPrimaryVlan_Type()
)
cpvlanVlanAssociatedPrimaryVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvlanVlanAssociatedPrimaryVlan.setStatus("current")
_CpvlanVlanEditTable_Object = MibTable
cpvlanVlanEditTable = _CpvlanVlanEditTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpvlanVlanEditTable.setStatus("current")
_CpvlanVlanEditEntry_Object = MibTableRow
cpvlanVlanEditEntry = _CpvlanVlanEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpvlanVlanEditEntry.setStatus("current")


class _CpvlanVlanEditPrivateVlanType_Type(PrivateVlanType):
    """Custom type cpvlanVlanEditPrivateVlanType based on PrivateVlanType"""


_CpvlanVlanEditPrivateVlanType_Object = MibTableColumn
cpvlanVlanEditPrivateVlanType = _CpvlanVlanEditPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2, 1, 1),
    _CpvlanVlanEditPrivateVlanType_Type()
)
cpvlanVlanEditPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanVlanEditPrivateVlanType.setStatus("current")


class _CpvlanVlanEditAssocPrimaryVlan_Type(VlanIndexOrZero):
    """Custom type cpvlanVlanEditAssocPrimaryVlan based on VlanIndexOrZero"""
    defaultValue = 0


_CpvlanVlanEditAssocPrimaryVlan_Object = MibTableColumn
cpvlanVlanEditAssocPrimaryVlan = _CpvlanVlanEditAssocPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 1, 2, 1, 2),
    _CpvlanVlanEditAssocPrimaryVlan_Type()
)
cpvlanVlanEditAssocPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanVlanEditAssocPrimaryVlan.setStatus("current")
_CpvlanPortObjects_ObjectIdentity = ObjectIdentity
cpvlanPortObjects = _CpvlanPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2)
)
_CpvlanPrivatePortTable_Object = MibTable
cpvlanPrivatePortTable = _CpvlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpvlanPrivatePortTable.setStatus("current")
_CpvlanPrivatePortEntry_Object = MibTableRow
cpvlanPrivatePortEntry = _CpvlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 1, 1)
)
cpvlanPrivatePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpvlanPrivatePortEntry.setStatus("current")


class _CpvlanPrivatePortSecondaryVlan_Type(VlanIndexOrZero):
    """Custom type cpvlanPrivatePortSecondaryVlan based on VlanIndexOrZero"""
    defaultValue = 0


_CpvlanPrivatePortSecondaryVlan_Object = MibTableColumn
cpvlanPrivatePortSecondaryVlan = _CpvlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 1, 1, 1),
    _CpvlanPrivatePortSecondaryVlan_Type()
)
cpvlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanPrivatePortSecondaryVlan.setStatus("current")
_CpvlanPromPortTable_Object = MibTable
cpvlanPromPortTable = _CpvlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpvlanPromPortTable.setStatus("current")
_CpvlanPromPortEntry_Object = MibTableRow
cpvlanPromPortEntry = _CpvlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1)
)
cpvlanPromPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpvlanPromPortEntry.setStatus("current")
_CpvlanPromPortMultiPrimaryVlan_Type = TruthValue
_CpvlanPromPortMultiPrimaryVlan_Object = MibTableColumn
cpvlanPromPortMultiPrimaryVlan = _CpvlanPromPortMultiPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 1),
    _CpvlanPromPortMultiPrimaryVlan_Type()
)
cpvlanPromPortMultiPrimaryVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvlanPromPortMultiPrimaryVlan.setStatus("current")


class _CpvlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type cpvlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpvlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_CpvlanPromPortSecondaryRemap_Object = MibTableColumn
cpvlanPromPortSecondaryRemap = _CpvlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 2),
    _CpvlanPromPortSecondaryRemap_Type()
)
cpvlanPromPortSecondaryRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanPromPortSecondaryRemap.setStatus("current")


class _CpvlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type cpvlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpvlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_CpvlanPromPortSecondaryRemap2k_Object = MibTableColumn
cpvlanPromPortSecondaryRemap2k = _CpvlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 3),
    _CpvlanPromPortSecondaryRemap2k_Type()
)
cpvlanPromPortSecondaryRemap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanPromPortSecondaryRemap2k.setStatus("current")


class _CpvlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type cpvlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpvlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_CpvlanPromPortSecondaryRemap3k_Object = MibTableColumn
cpvlanPromPortSecondaryRemap3k = _CpvlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 4),
    _CpvlanPromPortSecondaryRemap3k_Type()
)
cpvlanPromPortSecondaryRemap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanPromPortSecondaryRemap3k.setStatus("current")


class _CpvlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type cpvlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpvlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_CpvlanPromPortSecondaryRemap4k_Object = MibTableColumn
cpvlanPromPortSecondaryRemap4k = _CpvlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 5),
    _CpvlanPromPortSecondaryRemap4k_Type()
)
cpvlanPromPortSecondaryRemap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanPromPortSecondaryRemap4k.setStatus("current")
_CpvlanPromPortTwoWayRemapCapable_Type = TruthValue
_CpvlanPromPortTwoWayRemapCapable_Object = MibTableColumn
cpvlanPromPortTwoWayRemapCapable = _CpvlanPromPortTwoWayRemapCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 2, 1, 6),
    _CpvlanPromPortTwoWayRemapCapable_Type()
)
cpvlanPromPortTwoWayRemapCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvlanPromPortTwoWayRemapCapable.setStatus("current")
_CpvlanPortModeTable_Object = MibTable
cpvlanPortModeTable = _CpvlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpvlanPortModeTable.setStatus("current")
_CpvlanPortModeEntry_Object = MibTableRow
cpvlanPortModeEntry = _CpvlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 3, 1)
)
cpvlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpvlanPortModeEntry.setStatus("current")


class _CpvlanPortMode_Type(Integer32):
    """Custom type cpvlanPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("nonPrivateVlan", 1),
          ("promiscuous", 3),
          ("promiscuousTrunk", 5),
          ("secondaryTrunk", 4))
    )


_CpvlanPortMode_Type.__name__ = "Integer32"
_CpvlanPortMode_Object = MibTableColumn
cpvlanPortMode = _CpvlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 3, 1, 1),
    _CpvlanPortMode_Type()
)
cpvlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanPortMode.setStatus("current")
_CpvlanTrunkPortTable_Object = MibTable
cpvlanTrunkPortTable = _CpvlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cpvlanTrunkPortTable.setStatus("current")
_CpvlanTrunkPortEntry_Object = MibTableRow
cpvlanTrunkPortEntry = _CpvlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1)
)
cpvlanTrunkPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpvlanTrunkPortEntry.setStatus("current")


class _CpvlanTrunkPortDynamicState_Type(Integer32):
    """Custom type cpvlanTrunkPortDynamicState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("onNoNegotiate", 2))
    )


_CpvlanTrunkPortDynamicState_Type.__name__ = "Integer32"
_CpvlanTrunkPortDynamicState_Object = MibTableColumn
cpvlanTrunkPortDynamicState = _CpvlanTrunkPortDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 1),
    _CpvlanTrunkPortDynamicState_Type()
)
cpvlanTrunkPortDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortDynamicState.setStatus("current")


class _CpvlanTrunkPortEncapType_Type(Integer32):
    """Custom type cpvlanTrunkPortEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 1),
          ("isl", 2),
          ("negotiate", 3))
    )


_CpvlanTrunkPortEncapType_Type.__name__ = "Integer32"
_CpvlanTrunkPortEncapType_Object = MibTableColumn
cpvlanTrunkPortEncapType = _CpvlanTrunkPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 2),
    _CpvlanTrunkPortEncapType_Type()
)
cpvlanTrunkPortEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortEncapType.setStatus("current")
_CpvlanTrunkPortNativeVlan_Type = VlanIndexOrZero
_CpvlanTrunkPortNativeVlan_Object = MibTableColumn
cpvlanTrunkPortNativeVlan = _CpvlanTrunkPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 3),
    _CpvlanTrunkPortNativeVlan_Type()
)
cpvlanTrunkPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortNativeVlan.setStatus("current")
_CpvlanTrunkPortSecondaryVlans_Type = VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans_Object = MibTableColumn
cpvlanTrunkPortSecondaryVlans = _CpvlanTrunkPortSecondaryVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 4),
    _CpvlanTrunkPortSecondaryVlans_Type()
)
cpvlanTrunkPortSecondaryVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortSecondaryVlans.setStatus("current")
_CpvlanTrunkPortSecondaryVlans2k_Type = VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans2k_Object = MibTableColumn
cpvlanTrunkPortSecondaryVlans2k = _CpvlanTrunkPortSecondaryVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 5),
    _CpvlanTrunkPortSecondaryVlans2k_Type()
)
cpvlanTrunkPortSecondaryVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortSecondaryVlans2k.setStatus("current")
_CpvlanTrunkPortSecondaryVlans3k_Type = VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans3k_Object = MibTableColumn
cpvlanTrunkPortSecondaryVlans3k = _CpvlanTrunkPortSecondaryVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 6),
    _CpvlanTrunkPortSecondaryVlans3k_Type()
)
cpvlanTrunkPortSecondaryVlans3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortSecondaryVlans3k.setStatus("current")
_CpvlanTrunkPortSecondaryVlans4k_Type = VlanIndexBitmap
_CpvlanTrunkPortSecondaryVlans4k_Object = MibTableColumn
cpvlanTrunkPortSecondaryVlans4k = _CpvlanTrunkPortSecondaryVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 7),
    _CpvlanTrunkPortSecondaryVlans4k_Type()
)
cpvlanTrunkPortSecondaryVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortSecondaryVlans4k.setStatus("current")
_CpvlanTrunkPortNormalVlans_Type = VlanIndexBitmap
_CpvlanTrunkPortNormalVlans_Object = MibTableColumn
cpvlanTrunkPortNormalVlans = _CpvlanTrunkPortNormalVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 8),
    _CpvlanTrunkPortNormalVlans_Type()
)
cpvlanTrunkPortNormalVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortNormalVlans.setStatus("current")
_CpvlanTrunkPortNormalVlans2k_Type = VlanIndexBitmap
_CpvlanTrunkPortNormalVlans2k_Object = MibTableColumn
cpvlanTrunkPortNormalVlans2k = _CpvlanTrunkPortNormalVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 9),
    _CpvlanTrunkPortNormalVlans2k_Type()
)
cpvlanTrunkPortNormalVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortNormalVlans2k.setStatus("current")
_CpvlanTrunkPortNormalVlans3k_Type = VlanIndexBitmap
_CpvlanTrunkPortNormalVlans3k_Object = MibTableColumn
cpvlanTrunkPortNormalVlans3k = _CpvlanTrunkPortNormalVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 10),
    _CpvlanTrunkPortNormalVlans3k_Type()
)
cpvlanTrunkPortNormalVlans3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortNormalVlans3k.setStatus("current")
_CpvlanTrunkPortNormalVlans4k_Type = VlanIndexBitmap
_CpvlanTrunkPortNormalVlans4k_Object = MibTableColumn
cpvlanTrunkPortNormalVlans4k = _CpvlanTrunkPortNormalVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 11),
    _CpvlanTrunkPortNormalVlans4k_Type()
)
cpvlanTrunkPortNormalVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanTrunkPortNormalVlans4k.setStatus("current")


class _CpvlanTrunkPortDynamicStatus_Type(Integer32):
    """Custom type cpvlanTrunkPortDynamicStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTrunking", 2),
          ("trunking", 1))
    )


_CpvlanTrunkPortDynamicStatus_Type.__name__ = "Integer32"
_CpvlanTrunkPortDynamicStatus_Object = MibTableColumn
cpvlanTrunkPortDynamicStatus = _CpvlanTrunkPortDynamicStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 12),
    _CpvlanTrunkPortDynamicStatus_Type()
)
cpvlanTrunkPortDynamicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvlanTrunkPortDynamicStatus.setStatus("current")


class _CpvlanTrunkPortEncapOperType_Type(Integer32):
    """Custom type cpvlanTrunkPortEncapOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 1),
          ("isl", 2),
          ("notApplicable", 3))
    )


_CpvlanTrunkPortEncapOperType_Type.__name__ = "Integer32"
_CpvlanTrunkPortEncapOperType_Object = MibTableColumn
cpvlanTrunkPortEncapOperType = _CpvlanTrunkPortEncapOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 2, 4, 1, 13),
    _CpvlanTrunkPortEncapOperType_Type()
)
cpvlanTrunkPortEncapOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvlanTrunkPortEncapOperType.setStatus("current")
_CpvlanSVIObjects_ObjectIdentity = ObjectIdentity
cpvlanSVIObjects = _CpvlanSVIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3)
)
_CpvlanSVIMappingTable_Object = MibTable
cpvlanSVIMappingTable = _CpvlanSVIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cpvlanSVIMappingTable.setStatus("current")
_CpvlanSVIMappingEntry_Object = MibTableRow
cpvlanSVIMappingEntry = _CpvlanSVIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1, 1)
)
cpvlanSVIMappingEntry.setIndexNames(
    (0, "CISCO-PRIVATE-VLAN-MIB", "cpvlanSVIMappingVlanIndex"),
)
if mibBuilder.loadTexts:
    cpvlanSVIMappingEntry.setStatus("current")
_CpvlanSVIMappingVlanIndex_Type = VlanIndexOrZero
_CpvlanSVIMappingVlanIndex_Object = MibTableColumn
cpvlanSVIMappingVlanIndex = _CpvlanSVIMappingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1, 1, 1),
    _CpvlanSVIMappingVlanIndex_Type()
)
cpvlanSVIMappingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpvlanSVIMappingVlanIndex.setStatus("current")


class _CpvlanSVIMappingPrimarySVI_Type(VlanIndexOrZero):
    """Custom type cpvlanSVIMappingPrimarySVI based on VlanIndexOrZero"""
    defaultValue = 0


_CpvlanSVIMappingPrimarySVI_Object = MibTableColumn
cpvlanSVIMappingPrimarySVI = _CpvlanSVIMappingPrimarySVI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 1, 3, 1, 1, 2),
    _CpvlanSVIMappingPrimarySVI_Type()
)
cpvlanSVIMappingPrimarySVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpvlanSVIMappingPrimarySVI.setStatus("current")
_CpvlanMIBConformance_ObjectIdentity = ObjectIdentity
cpvlanMIBConformance = _CpvlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2)
)
_CpvlanMIBCompliances_ObjectIdentity = ObjectIdentity
cpvlanMIBCompliances = _CpvlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 1)
)
_CpvlanMIBGroups_ObjectIdentity = ObjectIdentity
cpvlanMIBGroups = _CpvlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2)
)
vtpVlanEntry.registerAugmentions(
    ("CISCO-PRIVATE-VLAN-MIB",
     "cpvlanVlanEntry")
)
cpvlanVlanEntry.setIndexNames(*vtpVlanEntry.getIndexNames())
vtpVlanEditEntry.registerAugmentions(
    ("CISCO-PRIVATE-VLAN-MIB",
     "cpvlanVlanEditEntry")
)
cpvlanVlanEditEntry.setIndexNames(*vtpVlanEditEntry.getIndexNames())

# Managed Objects groups

cpvlanVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 1)
)
cpvlanVlanGroup.setObjects(
      *(("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanPrivateVlanType"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanAssociatedPrimaryVlan"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanEditPrivateVlanType"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanVlanEditAssocPrimaryVlan"))
)
if mibBuilder.loadTexts:
    cpvlanVlanGroup.setStatus("current")

cpvlanPrivatePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 2)
)
cpvlanPrivatePortGroup.setObjects(
    ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPrivatePortSecondaryVlan")
)
if mibBuilder.loadTexts:
    cpvlanPrivatePortGroup.setStatus("current")

cpvlanPromPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 3)
)
cpvlanPromPortGroup.setObjects(
      *(("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortMultiPrimaryVlan"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortTwoWayRemapCapable"))
)
if mibBuilder.loadTexts:
    cpvlanPromPortGroup.setStatus("current")

cpvlanPromPort4kGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 4)
)
cpvlanPromPort4kGroup.setObjects(
      *(("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap2k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap3k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPromPortSecondaryRemap4k"))
)
if mibBuilder.loadTexts:
    cpvlanPromPort4kGroup.setStatus("current")

cpvlanPortModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 5)
)
cpvlanPortModeGroup.setObjects(
    ("CISCO-PRIVATE-VLAN-MIB", "cpvlanPortMode")
)
if mibBuilder.loadTexts:
    cpvlanPortModeGroup.setStatus("current")

cpvlanSVIMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 6)
)
cpvlanSVIMappingGroup.setObjects(
    ("CISCO-PRIVATE-VLAN-MIB", "cpvlanSVIMappingPrimarySVI")
)
if mibBuilder.loadTexts:
    cpvlanSVIMappingGroup.setStatus("current")

cpvlanTrunkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 2, 7)
)
cpvlanTrunkPortGroup.setObjects(
      *(("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortDynamicState"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortEncapType"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNativeVlan"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans2k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans3k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortSecondaryVlans4k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans2k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans3k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortNormalVlans4k"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortDynamicStatus"),
        ("CISCO-PRIVATE-VLAN-MIB", "cpvlanTrunkPortEncapOperType"))
)
if mibBuilder.loadTexts:
    cpvlanTrunkPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpvlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 173, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpvlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PRIVATE-VLAN-MIB",
    **{"PrivateVlanType": PrivateVlanType,
       "VlanIndexOrZero": VlanIndexOrZero,
       "VlanIndexBitmap": VlanIndexBitmap,
       "ciscoPrivateVlanMIB": ciscoPrivateVlanMIB,
       "cpvlanMIBObjects": cpvlanMIBObjects,
       "cpvlanVlanObjects": cpvlanVlanObjects,
       "cpvlanVlanTable": cpvlanVlanTable,
       "cpvlanVlanEntry": cpvlanVlanEntry,
       "cpvlanVlanPrivateVlanType": cpvlanVlanPrivateVlanType,
       "cpvlanVlanAssociatedPrimaryVlan": cpvlanVlanAssociatedPrimaryVlan,
       "cpvlanVlanEditTable": cpvlanVlanEditTable,
       "cpvlanVlanEditEntry": cpvlanVlanEditEntry,
       "cpvlanVlanEditPrivateVlanType": cpvlanVlanEditPrivateVlanType,
       "cpvlanVlanEditAssocPrimaryVlan": cpvlanVlanEditAssocPrimaryVlan,
       "cpvlanPortObjects": cpvlanPortObjects,
       "cpvlanPrivatePortTable": cpvlanPrivatePortTable,
       "cpvlanPrivatePortEntry": cpvlanPrivatePortEntry,
       "cpvlanPrivatePortSecondaryVlan": cpvlanPrivatePortSecondaryVlan,
       "cpvlanPromPortTable": cpvlanPromPortTable,
       "cpvlanPromPortEntry": cpvlanPromPortEntry,
       "cpvlanPromPortMultiPrimaryVlan": cpvlanPromPortMultiPrimaryVlan,
       "cpvlanPromPortSecondaryRemap": cpvlanPromPortSecondaryRemap,
       "cpvlanPromPortSecondaryRemap2k": cpvlanPromPortSecondaryRemap2k,
       "cpvlanPromPortSecondaryRemap3k": cpvlanPromPortSecondaryRemap3k,
       "cpvlanPromPortSecondaryRemap4k": cpvlanPromPortSecondaryRemap4k,
       "cpvlanPromPortTwoWayRemapCapable": cpvlanPromPortTwoWayRemapCapable,
       "cpvlanPortModeTable": cpvlanPortModeTable,
       "cpvlanPortModeEntry": cpvlanPortModeEntry,
       "cpvlanPortMode": cpvlanPortMode,
       "cpvlanTrunkPortTable": cpvlanTrunkPortTable,
       "cpvlanTrunkPortEntry": cpvlanTrunkPortEntry,
       "cpvlanTrunkPortDynamicState": cpvlanTrunkPortDynamicState,
       "cpvlanTrunkPortEncapType": cpvlanTrunkPortEncapType,
       "cpvlanTrunkPortNativeVlan": cpvlanTrunkPortNativeVlan,
       "cpvlanTrunkPortSecondaryVlans": cpvlanTrunkPortSecondaryVlans,
       "cpvlanTrunkPortSecondaryVlans2k": cpvlanTrunkPortSecondaryVlans2k,
       "cpvlanTrunkPortSecondaryVlans3k": cpvlanTrunkPortSecondaryVlans3k,
       "cpvlanTrunkPortSecondaryVlans4k": cpvlanTrunkPortSecondaryVlans4k,
       "cpvlanTrunkPortNormalVlans": cpvlanTrunkPortNormalVlans,
       "cpvlanTrunkPortNormalVlans2k": cpvlanTrunkPortNormalVlans2k,
       "cpvlanTrunkPortNormalVlans3k": cpvlanTrunkPortNormalVlans3k,
       "cpvlanTrunkPortNormalVlans4k": cpvlanTrunkPortNormalVlans4k,
       "cpvlanTrunkPortDynamicStatus": cpvlanTrunkPortDynamicStatus,
       "cpvlanTrunkPortEncapOperType": cpvlanTrunkPortEncapOperType,
       "cpvlanSVIObjects": cpvlanSVIObjects,
       "cpvlanSVIMappingTable": cpvlanSVIMappingTable,
       "cpvlanSVIMappingEntry": cpvlanSVIMappingEntry,
       "cpvlanSVIMappingVlanIndex": cpvlanSVIMappingVlanIndex,
       "cpvlanSVIMappingPrimarySVI": cpvlanSVIMappingPrimarySVI,
       "cpvlanMIBConformance": cpvlanMIBConformance,
       "cpvlanMIBCompliances": cpvlanMIBCompliances,
       "cpvlanMIBCompliance": cpvlanMIBCompliance,
       "cpvlanMIBGroups": cpvlanMIBGroups,
       "cpvlanVlanGroup": cpvlanVlanGroup,
       "cpvlanPrivatePortGroup": cpvlanPrivatePortGroup,
       "cpvlanPromPortGroup": cpvlanPromPortGroup,
       "cpvlanPromPort4kGroup": cpvlanPromPort4kGroup,
       "cpvlanPortModeGroup": cpvlanPortModeGroup,
       "cpvlanSVIMappingGroup": cpvlanSVIMappingGroup,
       "cpvlanTrunkPortGroup": cpvlanTrunkPortGroup}
)
