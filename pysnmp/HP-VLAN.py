# SNMP MIB module (HP-VLAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-VLAN
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:11 2024
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

(ConfigStatus,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "ConfigStatus")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpVlanLevelOne = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1)
)
hpVlanLevelOne.setRevisions(
        ("2000-11-03 04:17",
         "1995-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanID(Integer32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_HpVLAN_ObjectIdentity = ObjectIdentity
hpVLAN = _HpVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3)
)
_HpVlanObjects_ObjectIdentity = ObjectIdentity
hpVlanObjects = _HpVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1)
)
_HpVlanNumber_Type = Integer32
_HpVlanNumber_Object = MibScalar
hpVlanNumber = _HpVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 1),
    _HpVlanNumber_Type()
)
hpVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVlanNumber.setStatus("deprecated")
_HpVlanIdentTable_Object = MibTable
hpVlanIdentTable = _HpVlanIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpVlanIdentTable.setStatus("deprecated")
_HpVlanIdentEntry_Object = MibTableRow
hpVlanIdentEntry = _HpVlanIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1)
)
hpVlanIdentEntry.setIndexNames(
    (0, "HP-VLAN", "hpVlanIdentIndex"),
)
if mibBuilder.loadTexts:
    hpVlanIdentEntry.setStatus("deprecated")
_HpVlanIdentIndex_Type = VlanID
_HpVlanIdentIndex_Object = MibTableColumn
hpVlanIdentIndex = _HpVlanIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 1),
    _HpVlanIdentIndex_Type()
)
hpVlanIdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVlanIdentIndex.setStatus("deprecated")
_HpVlanIdentName_Type = DisplayString
_HpVlanIdentName_Object = MibTableColumn
hpVlanIdentName = _HpVlanIdentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 2),
    _HpVlanIdentName_Type()
)
hpVlanIdentName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpVlanIdentName.setStatus("deprecated")


class _HpVlanIdentMode_Type(Integer32):
    """Custom type hpVlanIdentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 2),
          ("port", 1))
    )


_HpVlanIdentMode_Type.__name__ = "Integer32"
_HpVlanIdentMode_Object = MibTableColumn
hpVlanIdentMode = _HpVlanIdentMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 3),
    _HpVlanIdentMode_Type()
)
hpVlanIdentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVlanIdentMode.setStatus("deprecated")
_HpVlanIdentStatus_Type = RowStatus
_HpVlanIdentStatus_Object = MibTableColumn
hpVlanIdentStatus = _HpVlanIdentStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 4),
    _HpVlanIdentStatus_Type()
)
hpVlanIdentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpVlanIdentStatus.setStatus("deprecated")


class _HpVlanDot1QID_Type(Integer32):
    """Custom type hpVlanDot1QID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HpVlanDot1QID_Type.__name__ = "Integer32"
_HpVlanDot1QID_Object = MibTableColumn
hpVlanDot1QID = _HpVlanDot1QID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 5),
    _HpVlanDot1QID_Type()
)
hpVlanDot1QID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpVlanDot1QID.setStatus("deprecated")


class _HpVlanIdentState_Type(Integer32):
    """Custom type hpVlanIdentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HpVlanIdentState_Type.__name__ = "Integer32"
_HpVlanIdentState_Object = MibTableColumn
hpVlanIdentState = _HpVlanIdentState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 6),
    _HpVlanIdentState_Type()
)
hpVlanIdentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVlanIdentState.setStatus("deprecated")


class _HpVlanIdentType_Type(Integer32):
    """Custom type hpVlanIdentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_HpVlanIdentType_Type.__name__ = "Integer32"
_HpVlanIdentType_Object = MibTableColumn
hpVlanIdentType = _HpVlanIdentType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 4, 1, 7),
    _HpVlanIdentType_Type()
)
hpVlanIdentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpVlanIdentType.setStatus("deprecated")
_HpVlanMemberTable_Object = MibTable
hpVlanMemberTable = _HpVlanMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpVlanMemberTable.setStatus("deprecated")
_HpVlanMemberEntry_Object = MibTableRow
hpVlanMemberEntry = _HpVlanMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 5, 1)
)
hpVlanMemberEntry.setIndexNames(
    (0, "HP-VLAN", "hpVlanMemberIfIndex"),
)
if mibBuilder.loadTexts:
    hpVlanMemberEntry.setStatus("deprecated")
_HpVlanMemberIfIndex_Type = InterfaceIndex
_HpVlanMemberIfIndex_Object = MibTableColumn
hpVlanMemberIfIndex = _HpVlanMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 5, 1, 1),
    _HpVlanMemberIfIndex_Type()
)
hpVlanMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVlanMemberIfIndex.setStatus("deprecated")
_HpVlanMemberIndex_Type = VlanID
_HpVlanMemberIndex_Object = MibTableColumn
hpVlanMemberIndex = _HpVlanMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 5, 1, 2),
    _HpVlanMemberIndex_Type()
)
hpVlanMemberIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpVlanMemberIndex.setStatus("deprecated")
_HpVlanAddrTable_Object = MibTable
hpVlanAddrTable = _HpVlanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpVlanAddrTable.setStatus("deprecated")
_HpVlanAddrEntry_Object = MibTableRow
hpVlanAddrEntry = _HpVlanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 6, 1)
)
hpVlanAddrEntry.setIndexNames(
    (0, "HP-VLAN", "hpVlanAddrIndex"),
)
if mibBuilder.loadTexts:
    hpVlanAddrEntry.setStatus("deprecated")
_HpVlanAddrIndex_Type = VlanID
_HpVlanAddrIndex_Object = MibTableColumn
hpVlanAddrIndex = _HpVlanAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 6, 1, 1),
    _HpVlanAddrIndex_Type()
)
hpVlanAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVlanAddrIndex.setStatus("deprecated")
_HpVlanAddrPhysAddress_Type = PhysAddress
_HpVlanAddrPhysAddress_Object = MibTableColumn
hpVlanAddrPhysAddress = _HpVlanAddrPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 6, 1, 2),
    _HpVlanAddrPhysAddress_Type()
)
hpVlanAddrPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVlanAddrPhysAddress.setStatus("deprecated")
_HpVlanIdentConfigStatus_Type = ConfigStatus
_HpVlanIdentConfigStatus_Object = MibScalar
hpVlanIdentConfigStatus = _HpVlanIdentConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 7),
    _HpVlanIdentConfigStatus_Type()
)
hpVlanIdentConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVlanIdentConfigStatus.setStatus("deprecated")
_HpVlanMemberTable2_Object = MibTable
hpVlanMemberTable2 = _HpVlanMemberTable2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hpVlanMemberTable2.setStatus("deprecated")
_HpVlanMemberEntry2_Object = MibTableRow
hpVlanMemberEntry2 = _HpVlanMemberEntry2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 8, 1)
)
hpVlanMemberEntry2.setIndexNames(
    (0, "HP-VLAN", "hpVlanIdentIndex"),
    (0, "HP-VLAN", "hpVlanMemberIfIndex"),
)
if mibBuilder.loadTexts:
    hpVlanMemberEntry2.setStatus("deprecated")


class _HpVlanMemberTagged2_Type(Integer32):
    """Custom type hpVlanMemberTagged2 based on Integer32"""
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
        *(("auto", 4),
          ("no", 3),
          ("tagged", 1),
          ("untagged", 2))
    )


_HpVlanMemberTagged2_Type.__name__ = "Integer32"
_HpVlanMemberTagged2_Object = MibTableColumn
hpVlanMemberTagged2 = _HpVlanMemberTagged2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 1, 8, 1, 1),
    _HpVlanMemberTagged2_Type()
)
hpVlanMemberTagged2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpVlanMemberTagged2.setStatus("deprecated")
_HpVlanTraps_ObjectIdentity = ObjectIdentity
hpVlanTraps = _HpVlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 2)
)
_HpVlanConformance_ObjectIdentity = ObjectIdentity
hpVlanConformance = _HpVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3)
)
_HpVlanGroups_ObjectIdentity = ObjectIdentity
hpVlanGroups = _HpVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 1)
)
_HpVlanCompliances_ObjectIdentity = ObjectIdentity
hpVlanCompliances = _HpVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 2)
)

# Managed Objects groups

hpVlanGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 1, 1)
)
hpVlanGeneralGroup.setObjects(
      *(("HP-VLAN", "hpVlanNumber"),
        ("HP-VLAN", "hpVlanIdentMode"),
        ("HP-VLAN", "hpVlanIdentName"),
        ("HP-VLAN", "hpVlanIdentStatus"))
)
if mibBuilder.loadTexts:
    hpVlanGeneralGroup.setStatus("deprecated")

hpVlanAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 1, 2)
)
hpVlanAddressGroup.setObjects(
    ("HP-VLAN", "hpVlanAddrPhysAddress")
)
if mibBuilder.loadTexts:
    hpVlanAddressGroup.setStatus("deprecated")

hpVlanMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 1, 3)
)
hpVlanMemberGroup.setObjects(
    ("HP-VLAN", "hpVlanMemberIndex")
)
if mibBuilder.loadTexts:
    hpVlanMemberGroup.setStatus("deprecated")

hpVlanTaggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 1, 4)
)
hpVlanTaggingGroup.setObjects(
      *(("HP-VLAN", "hpVlanDot1QID"),
        ("HP-VLAN", "hpVlanIdentState"),
        ("HP-VLAN", "hpVlanIdentType"),
        ("HP-VLAN", "hpVlanIdentConfigStatus"),
        ("HP-VLAN", "hpVlanMemberTagged2"))
)
if mibBuilder.loadTexts:
    hpVlanTaggingGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpVlanCompliance.setStatus(
        "deprecated"
    )

hpVlanCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hpVlanCompliance1.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-VLAN",
    **{"VlanID": VlanID,
       "hpVLAN": hpVLAN,
       "hpVlanLevelOne": hpVlanLevelOne,
       "hpVlanObjects": hpVlanObjects,
       "hpVlanNumber": hpVlanNumber,
       "hpVlanIdentTable": hpVlanIdentTable,
       "hpVlanIdentEntry": hpVlanIdentEntry,
       "hpVlanIdentIndex": hpVlanIdentIndex,
       "hpVlanIdentName": hpVlanIdentName,
       "hpVlanIdentMode": hpVlanIdentMode,
       "hpVlanIdentStatus": hpVlanIdentStatus,
       "hpVlanDot1QID": hpVlanDot1QID,
       "hpVlanIdentState": hpVlanIdentState,
       "hpVlanIdentType": hpVlanIdentType,
       "hpVlanMemberTable": hpVlanMemberTable,
       "hpVlanMemberEntry": hpVlanMemberEntry,
       "hpVlanMemberIfIndex": hpVlanMemberIfIndex,
       "hpVlanMemberIndex": hpVlanMemberIndex,
       "hpVlanAddrTable": hpVlanAddrTable,
       "hpVlanAddrEntry": hpVlanAddrEntry,
       "hpVlanAddrIndex": hpVlanAddrIndex,
       "hpVlanAddrPhysAddress": hpVlanAddrPhysAddress,
       "hpVlanIdentConfigStatus": hpVlanIdentConfigStatus,
       "hpVlanMemberTable2": hpVlanMemberTable2,
       "hpVlanMemberEntry2": hpVlanMemberEntry2,
       "hpVlanMemberTagged2": hpVlanMemberTagged2,
       "hpVlanTraps": hpVlanTraps,
       "hpVlanConformance": hpVlanConformance,
       "hpVlanGroups": hpVlanGroups,
       "hpVlanGeneralGroup": hpVlanGeneralGroup,
       "hpVlanAddressGroup": hpVlanAddressGroup,
       "hpVlanMemberGroup": hpVlanMemberGroup,
       "hpVlanTaggingGroup": hpVlanTaggingGroup,
       "hpVlanCompliances": hpVlanCompliances,
       "hpVlanCompliance": hpVlanCompliance,
       "hpVlanCompliance1": hpVlanCompliance1}
)
