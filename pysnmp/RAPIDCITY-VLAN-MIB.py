# SNMP MIB module (RAPIDCITY-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPIDCITY-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:42 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,
 MacAddress,
 RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rapidcity_ObjectIdentity = ObjectIdentity
rapidcity = _Rapidcity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272)
)
_Rapidcityfoo_ObjectIdentity = ObjectIdentity
rapidcityfoo = _Rapidcityfoo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1)
)
_RcVlan_ObjectIdentity = ObjectIdentity
rcVlan = _RcVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3)
)


class _RcVlanNumVlans_Type(Integer32):
    """Custom type rcVlanNumVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RcVlanNumVlans_Type.__name__ = "Integer32"
_RcVlanNumVlans_Object = MibScalar
rcVlanNumVlans = _RcVlanNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 1),
    _RcVlanNumVlans_Type()
)
rcVlanNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcVlanNumVlans.setStatus("mandatory")
_RcVlanTable_Object = MibTable
rcVlanTable = _RcVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rcVlanTable.setStatus("mandatory")
_RcVlanEntry_Object = MibTableRow
rcVlanEntry = _RcVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1)
)
rcVlanEntry.setIndexNames(
    (0, "RAPIDCITY-VLAN-MIB", "rcVlanId"),
)
if mibBuilder.loadTexts:
    rcVlanEntry.setStatus("mandatory")


class _RcVlanId_Type(Integer32):
    """Custom type rcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RcVlanId_Type.__name__ = "Integer32"
_RcVlanId_Object = MibTableColumn
rcVlanId = _RcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 1),
    _RcVlanId_Type()
)
rcVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcVlanId.setStatus("mandatory")


class _RcVlanName_Type(DisplayString):
    """Custom type rcVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcVlanName_Type.__name__ = "DisplayString"
_RcVlanName_Object = MibTableColumn
rcVlanName = _RcVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 2),
    _RcVlanName_Type()
)
rcVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanName.setStatus("mandatory")


class _RcVlanColor_Type(Integer32):
    """Custom type rcVlanColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RcVlanColor_Type.__name__ = "Integer32"
_RcVlanColor_Object = MibTableColumn
rcVlanColor = _RcVlanColor_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 3),
    _RcVlanColor_Type()
)
rcVlanColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanColor.setStatus("mandatory")


class _RcVlanHighPriority_Type(TruthValue):
    """Custom type rcVlanHighPriority based on TruthValue"""


_RcVlanHighPriority_Object = MibTableColumn
rcVlanHighPriority = _RcVlanHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 4),
    _RcVlanHighPriority_Type()
)
rcVlanHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanHighPriority.setStatus("mandatory")


class _RcVlanRoutingEnable_Type(TruthValue):
    """Custom type rcVlanRoutingEnable based on TruthValue"""


_RcVlanRoutingEnable_Object = MibTableColumn
rcVlanRoutingEnable = _RcVlanRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 5),
    _RcVlanRoutingEnable_Type()
)
rcVlanRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanRoutingEnable.setStatus("mandatory")
_RcVlanIfIndex_Type = InterfaceIndex
_RcVlanIfIndex_Object = MibTableColumn
rcVlanIfIndex = _RcVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 6),
    _RcVlanIfIndex_Type()
)
rcVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcVlanIfIndex.setStatus("mandatory")


class _RcVlanAction_Type(Integer32):
    """Custom type rcVlanAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 6),
          ("flushArp", 3),
          ("flushDynMemb", 5),
          ("flushIp", 4),
          ("flushMacFdb", 2),
          ("none", 1))
    )


_RcVlanAction_Type.__name__ = "Integer32"
_RcVlanAction_Object = MibTableColumn
rcVlanAction = _RcVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 7),
    _RcVlanAction_Type()
)
rcVlanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanAction.setStatus("mandatory")


class _RcVlanResult_Type(Integer32):
    """Custom type rcVlanResult based on Integer32"""
    defaultValue = 1

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
        *(("fail", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_RcVlanResult_Type.__name__ = "Integer32"
_RcVlanResult_Object = MibTableColumn
rcVlanResult = _RcVlanResult_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 8),
    _RcVlanResult_Type()
)
rcVlanResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcVlanResult.setStatus("mandatory")


class _RcVlanStgId_Type(Integer32):
    """Custom type rcVlanStgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RcVlanStgId_Type.__name__ = "Integer32"
_RcVlanStgId_Object = MibTableColumn
rcVlanStgId = _RcVlanStgId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 9),
    _RcVlanStgId_Type()
)
rcVlanStgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanStgId.setStatus("mandatory")


class _RcVlanType_Type(Integer32):
    """Custom type rcVlanType based on Integer32"""
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
        *(("byDstMcast", 5),
          ("byIpSubnet", 2),
          ("byPort", 1),
          ("byProtocolId", 3),
          ("bySrcMac", 4))
    )


_RcVlanType_Type.__name__ = "Integer32"
_RcVlanType_Object = MibTableColumn
rcVlanType = _RcVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 10),
    _RcVlanType_Type()
)
rcVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanType.setStatus("mandatory")


class _RcVlanPortMembers_Type(OctetString):
    """Custom type rcVlanPortMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RcVlanPortMembers_Type.__name__ = "OctetString"
_RcVlanPortMembers_Object = MibTableColumn
rcVlanPortMembers = _RcVlanPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 11),
    _RcVlanPortMembers_Type()
)
rcVlanPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanPortMembers.setStatus("mandatory")


class _RcVlanPotentialMembers_Type(OctetString):
    """Custom type rcVlanPotentialMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RcVlanPotentialMembers_Type.__name__ = "OctetString"
_RcVlanPotentialMembers_Object = MibTableColumn
rcVlanPotentialMembers = _RcVlanPotentialMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 12),
    _RcVlanPotentialMembers_Type()
)
rcVlanPotentialMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanPotentialMembers.setStatus("mandatory")


class _RcVlanStaticMembers_Type(OctetString):
    """Custom type rcVlanStaticMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RcVlanStaticMembers_Type.__name__ = "OctetString"
_RcVlanStaticMembers_Object = MibTableColumn
rcVlanStaticMembers = _RcVlanStaticMembers_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 13),
    _RcVlanStaticMembers_Type()
)
rcVlanStaticMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanStaticMembers.setStatus("mandatory")


class _RcVlanNotAllowToJoin_Type(OctetString):
    """Custom type rcVlanNotAllowToJoin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RcVlanNotAllowToJoin_Type.__name__ = "OctetString"
_RcVlanNotAllowToJoin_Object = MibTableColumn
rcVlanNotAllowToJoin = _RcVlanNotAllowToJoin_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 14),
    _RcVlanNotAllowToJoin_Type()
)
rcVlanNotAllowToJoin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanNotAllowToJoin.setStatus("mandatory")


class _RcVlanProtocolId_Type(Integer32):
    """Custom type rcVlanProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 6),
          ("decLat", 7),
          ("decOther", 8),
          ("ip", 1),
          ("ipx802dot2", 3),
          ("ipx802dot3", 2),
          ("ipxEthernet2", 5),
          ("ipxSnap", 4),
          ("netBios", 11),
          ("none", 0),
          ("sna802dot2", 9),
          ("snaEthernet2", 10),
          ("xns", 12))
    )


_RcVlanProtocolId_Type.__name__ = "Integer32"
_RcVlanProtocolId_Object = MibTableColumn
rcVlanProtocolId = _RcVlanProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 15),
    _RcVlanProtocolId_Type()
)
rcVlanProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanProtocolId.setStatus("mandatory")
_RcVlanSubnetAddr_Type = IpAddress
_RcVlanSubnetAddr_Object = MibTableColumn
rcVlanSubnetAddr = _RcVlanSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 16),
    _RcVlanSubnetAddr_Type()
)
rcVlanSubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanSubnetAddr.setStatus("mandatory")
_RcVlanSubnetMask_Type = IpAddress
_RcVlanSubnetMask_Object = MibTableColumn
rcVlanSubnetMask = _RcVlanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 17),
    _RcVlanSubnetMask_Type()
)
rcVlanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanSubnetMask.setStatus("mandatory")


class _RcVlanAgingTime_Type(Integer32):
    """Custom type rcVlanAgingTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_RcVlanAgingTime_Type.__name__ = "Integer32"
_RcVlanAgingTime_Object = MibTableColumn
rcVlanAgingTime = _RcVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 18),
    _RcVlanAgingTime_Type()
)
rcVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanAgingTime.setStatus("mandatory")
_RcVlanMacAddress_Type = MacAddress
_RcVlanMacAddress_Object = MibTableColumn
rcVlanMacAddress = _RcVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 19),
    _RcVlanMacAddress_Type()
)
rcVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcVlanMacAddress.setStatus("mandatory")
_RcVlanRowStatus_Type = RowStatus
_RcVlanRowStatus_Object = MibTableColumn
rcVlanRowStatus = _RcVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 3, 2, 1, 20),
    _RcVlanRowStatus_Type()
)
rcVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPIDCITY-VLAN-MIB",
    **{"rapidcity": rapidcity,
       "rapidcityfoo": rapidcityfoo,
       "rcVlan": rcVlan,
       "rcVlanNumVlans": rcVlanNumVlans,
       "rcVlanTable": rcVlanTable,
       "rcVlanEntry": rcVlanEntry,
       "rcVlanId": rcVlanId,
       "rcVlanName": rcVlanName,
       "rcVlanColor": rcVlanColor,
       "rcVlanHighPriority": rcVlanHighPriority,
       "rcVlanRoutingEnable": rcVlanRoutingEnable,
       "rcVlanIfIndex": rcVlanIfIndex,
       "rcVlanAction": rcVlanAction,
       "rcVlanResult": rcVlanResult,
       "rcVlanStgId": rcVlanStgId,
       "rcVlanType": rcVlanType,
       "rcVlanPortMembers": rcVlanPortMembers,
       "rcVlanPotentialMembers": rcVlanPotentialMembers,
       "rcVlanStaticMembers": rcVlanStaticMembers,
       "rcVlanNotAllowToJoin": rcVlanNotAllowToJoin,
       "rcVlanProtocolId": rcVlanProtocolId,
       "rcVlanSubnetAddr": rcVlanSubnetAddr,
       "rcVlanSubnetMask": rcVlanSubnetMask,
       "rcVlanAgingTime": rcVlanAgingTime,
       "rcVlanMacAddress": rcVlanMacAddress,
       "rcVlanRowStatus": rcVlanRowStatus}
)
