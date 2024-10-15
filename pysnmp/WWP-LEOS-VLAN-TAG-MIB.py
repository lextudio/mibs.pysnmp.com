# SNMP MIB module (WWP-LEOS-VLAN-TAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-VLAN-TAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:15 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5)
)
wwpLeosVlanMIB.setRevisions(
        ("2007-09-29 17:00",
         "2003-01-15 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )



class VlanTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosVlanMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosVlanMIBObjects = _WwpLeosVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1)
)
_WwpLeosVlan_ObjectIdentity = ObjectIdentity
wwpLeosVlan = _WwpLeosVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1)
)
_WwpLeosMaxVlans_Type = Unsigned32
_WwpLeosMaxVlans_Object = MibScalar
wwpLeosMaxVlans = _WwpLeosMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 1),
    _WwpLeosMaxVlans_Type()
)
wwpLeosMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMaxVlans.setStatus("current")
_WwpLeosMaxSupportedVlanTagId_Type = Unsigned32
_WwpLeosMaxSupportedVlanTagId_Object = MibScalar
wwpLeosMaxSupportedVlanTagId = _WwpLeosMaxSupportedVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 2),
    _WwpLeosMaxSupportedVlanTagId_Type()
)
wwpLeosMaxSupportedVlanTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMaxSupportedVlanTagId.setStatus("current")
_WwpLeosNumVlans_Type = Unsigned32
_WwpLeosNumVlans_Object = MibScalar
wwpLeosNumVlans = _WwpLeosNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 3),
    _WwpLeosNumVlans_Type()
)
wwpLeosNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNumVlans.setStatus("current")
_WwpLeosVlanTable_Object = MibTable
wwpLeosVlanTable = _WwpLeosVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosVlanTable.setStatus("current")
_WwpLeosVlanEntry_Object = MibTableRow
wwpLeosVlanEntry = _WwpLeosVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1)
)
wwpLeosVlanEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanEntry.setStatus("current")
_WwpLeosVlanId_Type = VlanId
_WwpLeosVlanId_Object = MibTableColumn
wwpLeosVlanId = _WwpLeosVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 1),
    _WwpLeosVlanId_Type()
)
wwpLeosVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanId.setStatus("current")


class _WwpLeosVlanName_Type(OctetString):
    """Custom type wwpLeosVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosVlanName_Type.__name__ = "OctetString"
_WwpLeosVlanName_Object = MibTableColumn
wwpLeosVlanName = _WwpLeosVlanName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 2),
    _WwpLeosVlanName_Type()
)
wwpLeosVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanName.setStatus("current")
_WwpLeosVlanStatus_Type = RowStatus
_WwpLeosVlanStatus_Object = MibTableColumn
wwpLeosVlanStatus = _WwpLeosVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 4),
    _WwpLeosVlanStatus_Type()
)
wwpLeosVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanStatus.setStatus("current")


class _WwpLeosVlanMacLrnState_Type(Integer32):
    """Custom type wwpLeosVlanMacLrnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVlanMacLrnState_Type.__name__ = "Integer32"
_WwpLeosVlanMacLrnState_Object = MibTableColumn
wwpLeosVlanMacLrnState = _WwpLeosVlanMacLrnState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 5),
    _WwpLeosVlanMacLrnState_Type()
)
wwpLeosVlanMacLrnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanMacLrnState.setStatus("current")


class _WwpLeosVlanMacLrnOperState_Type(Integer32):
    """Custom type wwpLeosVlanMacLrnOperState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("vsOverride", 3))
    )


_WwpLeosVlanMacLrnOperState_Type.__name__ = "Integer32"
_WwpLeosVlanMacLrnOperState_Object = MibTableColumn
wwpLeosVlanMacLrnOperState = _WwpLeosVlanMacLrnOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 6),
    _WwpLeosVlanMacLrnOperState_Type()
)
wwpLeosVlanMacLrnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanMacLrnOperState.setStatus("current")


class _WwpLeosVlanTranslationVlan_Type(Integer32):
    """Custom type wwpLeosVlanTranslationVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosVlanTranslationVlan_Type.__name__ = "Integer32"
_WwpLeosVlanTranslationVlan_Object = MibTableColumn
wwpLeosVlanTranslationVlan = _WwpLeosVlanTranslationVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 7),
    _WwpLeosVlanTranslationVlan_Type()
)
wwpLeosVlanTranslationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationVlan.setStatus("current")


class _WwpLeosVlanEgressTpid_Type(Integer32):
    """Custom type wwpLeosVlanEgressTpid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tpid8100", 1),
          ("tpid88A8", 3),
          ("tpid9100", 2))
    )


_WwpLeosVlanEgressTpid_Type.__name__ = "Integer32"
_WwpLeosVlanEgressTpid_Object = MibTableColumn
wwpLeosVlanEgressTpid = _WwpLeosVlanEgressTpid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 4, 1, 8),
    _WwpLeosVlanEgressTpid_Type()
)
wwpLeosVlanEgressTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanEgressTpid.setStatus("current")
_WwpLeosVlanTagMemberTable_Object = MibTable
wwpLeosVlanTagMemberTable = _WwpLeosVlanTagMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosVlanTagMemberTable.setStatus("current")
_WwpLeosVlanTagMemberEntry_Object = MibTableRow
wwpLeosVlanTagMemberEntry = _WwpLeosVlanTagMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1)
)
wwpLeosVlanTagMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberPortId"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberTagId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanTagMemberEntry.setStatus("current")


class _WwpLeosVlanMemberPortId_Type(Integer32):
    """Custom type wwpLeosVlanMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVlanMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVlanMemberPortId_Object = MibTableColumn
wwpLeosVlanMemberPortId = _WwpLeosVlanMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1, 1),
    _WwpLeosVlanMemberPortId_Type()
)
wwpLeosVlanMemberPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanMemberPortId.setStatus("current")
_WwpLeosVlanMemberTagId_Type = VlanTag
_WwpLeosVlanMemberTagId_Object = MibTableColumn
wwpLeosVlanMemberTagId = _WwpLeosVlanMemberTagId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1, 2),
    _WwpLeosVlanMemberTagId_Type()
)
wwpLeosVlanMemberTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanMemberTagId.setStatus("current")
_WwpLeosVlanMemberStatus_Type = RowStatus
_WwpLeosVlanMemberStatus_Object = MibTableColumn
wwpLeosVlanMemberStatus = _WwpLeosVlanMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 5, 1, 4),
    _WwpLeosVlanMemberStatus_Type()
)
wwpLeosVlanMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanMemberStatus.setStatus("current")
_WwpLeosVlanCircuitTable_Object = MibTable
wwpLeosVlanCircuitTable = _WwpLeosVlanCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitTable.setStatus("deprecated")
_WwpLeosVlanCircuitEntry_Object = MibTableRow
wwpLeosVlanCircuitEntry = _WwpLeosVlanCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1)
)
wwpLeosVlanCircuitEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitEntry.setStatus("deprecated")


class _WwpLeosCircuitIndex_Type(Integer32):
    """Custom type wwpLeosCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCircuitIndex_Type.__name__ = "Integer32"
_WwpLeosCircuitIndex_Object = MibTableColumn
wwpLeosCircuitIndex = _WwpLeosCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 1),
    _WwpLeosCircuitIndex_Type()
)
wwpLeosCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCircuitIndex.setStatus("deprecated")
_WwpLeosCircuitVlanId_Type = VlanId
_WwpLeosCircuitVlanId_Object = MibTableColumn
wwpLeosCircuitVlanId = _WwpLeosCircuitVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 2),
    _WwpLeosCircuitVlanId_Type()
)
wwpLeosCircuitVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCircuitVlanId.setStatus("deprecated")


class _WwpLeosCircuitType_Type(Integer32):
    """Custom type wwpLeosCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosCircuitType_Type.__name__ = "Integer32"
_WwpLeosCircuitType_Object = MibTableColumn
wwpLeosCircuitType = _WwpLeosCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 3),
    _WwpLeosCircuitType_Type()
)
wwpLeosCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCircuitType.setStatus("deprecated")


class _WwpLeosCircuitName_Type(OctetString):
    """Custom type wwpLeosCircuitName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosCircuitName_Type.__name__ = "OctetString"
_WwpLeosCircuitName_Object = MibTableColumn
wwpLeosCircuitName = _WwpLeosCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 4),
    _WwpLeosCircuitName_Type()
)
wwpLeosCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCircuitName.setStatus("deprecated")


class _WwpLeosCircuitPriority_Type(Integer32):
    """Custom type wwpLeosCircuitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCircuitPriority_Type.__name__ = "Integer32"
_WwpLeosCircuitPriority_Object = MibTableColumn
wwpLeosCircuitPriority = _WwpLeosCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 5),
    _WwpLeosCircuitPriority_Type()
)
wwpLeosCircuitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCircuitPriority.setStatus("deprecated")


class _WwpLeosCircuitDataTunnelState_Type(Integer32):
    """Custom type wwpLeosCircuitDataTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosCircuitDataTunnelState_Type.__name__ = "Integer32"
_WwpLeosCircuitDataTunnelState_Object = MibTableColumn
wwpLeosCircuitDataTunnelState = _WwpLeosCircuitDataTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 6),
    _WwpLeosCircuitDataTunnelState_Type()
)
wwpLeosCircuitDataTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCircuitDataTunnelState.setStatus("deprecated")


class _WwpLeosCircuitCtrlProtocolTunnelState_Type(Integer32):
    """Custom type wwpLeosCircuitCtrlProtocolTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosCircuitCtrlProtocolTunnelState_Type.__name__ = "Integer32"
_WwpLeosCircuitCtrlProtocolTunnelState_Object = MibTableColumn
wwpLeosCircuitCtrlProtocolTunnelState = _WwpLeosCircuitCtrlProtocolTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 7),
    _WwpLeosCircuitCtrlProtocolTunnelState_Type()
)
wwpLeosCircuitCtrlProtocolTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCircuitCtrlProtocolTunnelState.setStatus("deprecated")


class _WwpLeosCircuitNumEndPoints_Type(Integer32):
    """Custom type wwpLeosCircuitNumEndPoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosCircuitNumEndPoints_Type.__name__ = "Integer32"
_WwpLeosCircuitNumEndPoints_Object = MibTableColumn
wwpLeosCircuitNumEndPoints = _WwpLeosCircuitNumEndPoints_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 8),
    _WwpLeosCircuitNumEndPoints_Type()
)
wwpLeosCircuitNumEndPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCircuitNumEndPoints.setStatus("deprecated")
_WwpLeosCircuitStatus_Type = RowStatus
_WwpLeosCircuitStatus_Object = MibTableColumn
wwpLeosCircuitStatus = _WwpLeosCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 6, 1, 9),
    _WwpLeosCircuitStatus_Type()
)
wwpLeosCircuitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCircuitStatus.setStatus("deprecated")
_WwpLeosVlanCircuitPortExclusiveTable_Object = MibTable
wwpLeosVlanCircuitPortExclusiveTable = _WwpLeosVlanCircuitPortExclusiveTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitPortExclusiveTable.setStatus("deprecated")
_WwpLeosVlanCircuitPortExclusiveEntry_Object = MibTableRow
wwpLeosVlanCircuitPortExclusiveEntry = _WwpLeosVlanCircuitPortExclusiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7, 1)
)
wwpLeosVlanCircuitPortExclusiveEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitPortExclusiveEntry.setStatus("deprecated")


class _WwpLeosPortId_Type(Integer32):
    """Custom type wwpLeosPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPortId_Type.__name__ = "Integer32"
_WwpLeosPortId_Object = MibTableColumn
wwpLeosPortId = _WwpLeosPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7, 1, 1),
    _WwpLeosPortId_Type()
)
wwpLeosPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPortId.setStatus("deprecated")
_WwpLeosPortExclusiveStatus_Type = RowStatus
_WwpLeosPortExclusiveStatus_Object = MibTableColumn
wwpLeosPortExclusiveStatus = _WwpLeosPortExclusiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 7, 1, 2),
    _WwpLeosPortExclusiveStatus_Type()
)
wwpLeosPortExclusiveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPortExclusiveStatus.setStatus("deprecated")
_WwpLeosVlanCircuitCtrlProtocolTable_Object = MibTable
wwpLeosVlanCircuitCtrlProtocolTable = _WwpLeosVlanCircuitCtrlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitCtrlProtocolTable.setStatus("deprecated")
_WwpLeosVlanCircuitCtrlProtocolEntry_Object = MibTableRow
wwpLeosVlanCircuitCtrlProtocolEntry = _WwpLeosVlanCircuitCtrlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8, 1)
)
wwpLeosVlanCircuitCtrlProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanl2ProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitCtrlProtocolEntry.setStatus("deprecated")


class _WwpLeosVlanl2ProtocolNum_Type(Integer32):
    """Custom type wwpLeosVlanl2ProtocolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUdlp", 8),
          ("ciscoUplinkFast", 7),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("l28021x", 1),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("lldp", 13),
          ("oam", 14),
          ("rstp", 2),
          ("vlanBridge", 15))
    )


_WwpLeosVlanl2ProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVlanl2ProtocolNum_Object = MibTableColumn
wwpLeosVlanl2ProtocolNum = _WwpLeosVlanl2ProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8, 1, 1),
    _WwpLeosVlanl2ProtocolNum_Type()
)
wwpLeosVlanl2ProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2ProtocolNum.setStatus("deprecated")


class _WwpLeosVlanl2Type_Type(Integer32):
    """Custom type wwpLeosVlanl2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )


_WwpLeosVlanl2Type_Type.__name__ = "Integer32"
_WwpLeosVlanl2Type_Object = MibTableColumn
wwpLeosVlanl2Type = _WwpLeosVlanl2Type_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 8, 1, 2),
    _WwpLeosVlanl2Type_Type()
)
wwpLeosVlanl2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanl2Type.setStatus("deprecated")
_WwpLeosVlanCircuitStats_ObjectIdentity = ObjectIdentity
wwpLeosVlanCircuitStats = _WwpLeosVlanCircuitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9)
)
_WwpLeosVlanl2AllRxPkts_Type = Counter32
_WwpLeosVlanl2AllRxPkts_Object = MibScalar
wwpLeosVlanl2AllRxPkts = _WwpLeosVlanl2AllRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 1),
    _WwpLeosVlanl2AllRxPkts_Type()
)
wwpLeosVlanl2AllRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllRxPkts.setStatus("deprecated")
_WwpLeosVlanl2AllTunneledPkts_Type = Counter32
_WwpLeosVlanl2AllTunneledPkts_Object = MibScalar
wwpLeosVlanl2AllTunneledPkts = _WwpLeosVlanl2AllTunneledPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 2),
    _WwpLeosVlanl2AllTunneledPkts_Type()
)
wwpLeosVlanl2AllTunneledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllTunneledPkts.setStatus("deprecated")
_WwpLeosVlanl2AllPeerPkts_Type = Counter32
_WwpLeosVlanl2AllPeerPkts_Object = MibScalar
wwpLeosVlanl2AllPeerPkts = _WwpLeosVlanl2AllPeerPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 3),
    _WwpLeosVlanl2AllPeerPkts_Type()
)
wwpLeosVlanl2AllPeerPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllPeerPkts.setStatus("deprecated")
_WwpLeosVlanl2AllDiscardedPkts_Type = Counter32
_WwpLeosVlanl2AllDiscardedPkts_Object = MibScalar
wwpLeosVlanl2AllDiscardedPkts = _WwpLeosVlanl2AllDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 4),
    _WwpLeosVlanl2AllDiscardedPkts_Type()
)
wwpLeosVlanl2AllDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllDiscardedPkts.setStatus("deprecated")
_WwpLeosVlanl2AllDecodedPkts_Type = Counter32
_WwpLeosVlanl2AllDecodedPkts_Object = MibScalar
wwpLeosVlanl2AllDecodedPkts = _WwpLeosVlanl2AllDecodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 5),
    _WwpLeosVlanl2AllDecodedPkts_Type()
)
wwpLeosVlanl2AllDecodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllDecodedPkts.setStatus("deprecated")
_WwpLeosVlanl2AllDecodedFailures_Type = Counter32
_WwpLeosVlanl2AllDecodedFailures_Object = MibScalar
wwpLeosVlanl2AllDecodedFailures = _WwpLeosVlanl2AllDecodedFailures_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 6),
    _WwpLeosVlanl2AllDecodedFailures_Type()
)
wwpLeosVlanl2AllDecodedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllDecodedFailures.setStatus("deprecated")
_WwpLeosVlanl2AllTunneledSubcriberPortPkts_Type = Counter32
_WwpLeosVlanl2AllTunneledSubcriberPortPkts_Object = MibScalar
wwpLeosVlanl2AllTunneledSubcriberPortPkts = _WwpLeosVlanl2AllTunneledSubcriberPortPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 9, 7),
    _WwpLeosVlanl2AllTunneledSubcriberPortPkts_Type()
)
wwpLeosVlanl2AllTunneledSubcriberPortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2AllTunneledSubcriberPortPkts.setStatus("deprecated")
_WwpLeosVlanCircuitProtocolStatsTable_Object = MibTable
wwpLeosVlanCircuitProtocolStatsTable = _WwpLeosVlanCircuitProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitProtocolStatsTable.setStatus("deprecated")
_WwpLeosVlanCircuitProtocolStatsEntry_Object = MibTableRow
wwpLeosVlanCircuitProtocolStatsEntry = _WwpLeosVlanCircuitProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1)
)
wwpLeosVlanCircuitProtocolStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosCircuitIndex"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanl2ProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanCircuitProtocolStatsEntry.setStatus("deprecated")
_WwpLeosVlanl2RxPkts_Type = Counter32
_WwpLeosVlanl2RxPkts_Object = MibTableColumn
wwpLeosVlanl2RxPkts = _WwpLeosVlanl2RxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 1),
    _WwpLeosVlanl2RxPkts_Type()
)
wwpLeosVlanl2RxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2RxPkts.setStatus("deprecated")
_WwpLeosVlanl2TunneledPkts_Type = Counter32
_WwpLeosVlanl2TunneledPkts_Object = MibTableColumn
wwpLeosVlanl2TunneledPkts = _WwpLeosVlanl2TunneledPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 2),
    _WwpLeosVlanl2TunneledPkts_Type()
)
wwpLeosVlanl2TunneledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2TunneledPkts.setStatus("deprecated")
_WwpLeosVlanl2PeerPkts_Type = Counter32
_WwpLeosVlanl2PeerPkts_Object = MibTableColumn
wwpLeosVlanl2PeerPkts = _WwpLeosVlanl2PeerPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 3),
    _WwpLeosVlanl2PeerPkts_Type()
)
wwpLeosVlanl2PeerPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2PeerPkts.setStatus("deprecated")
_WwpLeosVlanl2DiscardedPkts_Type = Counter32
_WwpLeosVlanl2DiscardedPkts_Object = MibTableColumn
wwpLeosVlanl2DiscardedPkts = _WwpLeosVlanl2DiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 4),
    _WwpLeosVlanl2DiscardedPkts_Type()
)
wwpLeosVlanl2DiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2DiscardedPkts.setStatus("deprecated")
_WwpLeosVlanl2DecodedPkts_Type = Counter32
_WwpLeosVlanl2DecodedPkts_Object = MibTableColumn
wwpLeosVlanl2DecodedPkts = _WwpLeosVlanl2DecodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 5),
    _WwpLeosVlanl2DecodedPkts_Type()
)
wwpLeosVlanl2DecodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2DecodedPkts.setStatus("deprecated")
_WwpLeosVlanl2DecodedFailures_Type = Counter32
_WwpLeosVlanl2DecodedFailures_Object = MibTableColumn
wwpLeosVlanl2DecodedFailures = _WwpLeosVlanl2DecodedFailures_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 6),
    _WwpLeosVlanl2DecodedFailures_Type()
)
wwpLeosVlanl2DecodedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2DecodedFailures.setStatus("deprecated")
_WwpLeosVlanl2TunneledSubcriberPortPkts_Type = Counter32
_WwpLeosVlanl2TunneledSubcriberPortPkts_Object = MibTableColumn
wwpLeosVlanl2TunneledSubcriberPortPkts = _WwpLeosVlanl2TunneledSubcriberPortPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 10, 1, 7),
    _WwpLeosVlanl2TunneledSubcriberPortPkts_Type()
)
wwpLeosVlanl2TunneledSubcriberPortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanl2TunneledSubcriberPortPkts.setStatus("deprecated")
_WwpLeosVlanStatsTable_Object = MibTable
wwpLeosVlanStatsTable = _WwpLeosVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wwpLeosVlanStatsTable.setStatus("current")
_WwpLeosVlanStatsEntry_Object = MibTableRow
wwpLeosVlanStatsEntry = _WwpLeosVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1)
)
wwpLeosVlanStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanStatsVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanStatsEntry.setStatus("current")
_WwpLeosVlanStatsVlanId_Type = VlanTag
_WwpLeosVlanStatsVlanId_Object = MibTableColumn
wwpLeosVlanStatsVlanId = _WwpLeosVlanStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 1),
    _WwpLeosVlanStatsVlanId_Type()
)
wwpLeosVlanStatsVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsVlanId.setStatus("current")
_WwpLeosVlanStatsCreateTime_Type = TimeStamp
_WwpLeosVlanStatsCreateTime_Object = MibTableColumn
wwpLeosVlanStatsCreateTime = _WwpLeosVlanStatsCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 2),
    _WwpLeosVlanStatsCreateTime_Type()
)
wwpLeosVlanStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsCreateTime.setStatus("current")
_WwpLeosVlanStatsUniOctets_Type = Counter64
_WwpLeosVlanStatsUniOctets_Object = MibTableColumn
wwpLeosVlanStatsUniOctets = _WwpLeosVlanStatsUniOctets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 3),
    _WwpLeosVlanStatsUniOctets_Type()
)
wwpLeosVlanStatsUniOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsUniOctets.setStatus("current")
_WwpLeosVlanStatsUniPkts_Type = Counter32
_WwpLeosVlanStatsUniPkts_Object = MibTableColumn
wwpLeosVlanStatsUniPkts = _WwpLeosVlanStatsUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 4),
    _WwpLeosVlanStatsUniPkts_Type()
)
wwpLeosVlanStatsUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsUniPkts.setStatus("current")
_WwpLeosVlanStatsNonUniOctets_Type = Counter64
_WwpLeosVlanStatsNonUniOctets_Object = MibTableColumn
wwpLeosVlanStatsNonUniOctets = _WwpLeosVlanStatsNonUniOctets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 5),
    _WwpLeosVlanStatsNonUniOctets_Type()
)
wwpLeosVlanStatsNonUniOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsNonUniOctets.setStatus("current")
_WwpLeosVlanStatsNonUniPkts_Type = Counter32
_WwpLeosVlanStatsNonUniPkts_Object = MibTableColumn
wwpLeosVlanStatsNonUniPkts = _WwpLeosVlanStatsNonUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 6),
    _WwpLeosVlanStatsNonUniPkts_Type()
)
wwpLeosVlanStatsNonUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsNonUniPkts.setStatus("current")
_WwpLeosVlanStatsStatus_Type = RowStatus
_WwpLeosVlanStatsStatus_Object = MibTableColumn
wwpLeosVlanStatsStatus = _WwpLeosVlanStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 7),
    _WwpLeosVlanStatsStatus_Type()
)
wwpLeosVlanStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsStatus.setStatus("current")


class _WwpLeosVlanStatsClear_Type(TruthValue):
    """Custom type wwpLeosVlanStatsClear based on TruthValue"""


_WwpLeosVlanStatsClear_Object = MibTableColumn
wwpLeosVlanStatsClear = _WwpLeosVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 8),
    _WwpLeosVlanStatsClear_Type()
)
wwpLeosVlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsClear.setStatus("current")


class _WwpLeosVlanStatsPortId_Type(Integer32):
    """Custom type wwpLeosVlanStatsPortId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVlanStatsPortId_Type.__name__ = "Integer32"
_WwpLeosVlanStatsPortId_Object = MibTableColumn
wwpLeosVlanStatsPortId = _WwpLeosVlanStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 11, 1, 9),
    _WwpLeosVlanStatsPortId_Type()
)
wwpLeosVlanStatsPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanStatsPortId.setStatus("current")
_WwpLeosVlanTotalStatsTable_Object = MibTable
wwpLeosVlanTotalStatsTable = _WwpLeosVlanTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsTable.setStatus("current")
_WwpLeosVlanTotalStatsEntry_Object = MibTableRow
wwpLeosVlanTotalStatsEntry = _WwpLeosVlanTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1)
)
wwpLeosVlanTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanTotalStatsVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsEntry.setStatus("current")
_WwpLeosVlanTotalStatsVlanId_Type = VlanTag
_WwpLeosVlanTotalStatsVlanId_Object = MibTableColumn
wwpLeosVlanTotalStatsVlanId = _WwpLeosVlanTotalStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 1),
    _WwpLeosVlanTotalStatsVlanId_Type()
)
wwpLeosVlanTotalStatsVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsVlanId.setStatus("current")
_WwpLeosVlanTotalStatsCreateTime_Type = TimeStamp
_WwpLeosVlanTotalStatsCreateTime_Object = MibTableColumn
wwpLeosVlanTotalStatsCreateTime = _WwpLeosVlanTotalStatsCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 2),
    _WwpLeosVlanTotalStatsCreateTime_Type()
)
wwpLeosVlanTotalStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsCreateTime.setStatus("current")
_WwpLeosVlanTotalStatsUniOctets_Type = Counter64
_WwpLeosVlanTotalStatsUniOctets_Object = MibTableColumn
wwpLeosVlanTotalStatsUniOctets = _WwpLeosVlanTotalStatsUniOctets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 3),
    _WwpLeosVlanTotalStatsUniOctets_Type()
)
wwpLeosVlanTotalStatsUniOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsUniOctets.setStatus("current")
_WwpLeosVlanTotalStatsUniPkts_Type = Counter32
_WwpLeosVlanTotalStatsUniPkts_Object = MibTableColumn
wwpLeosVlanTotalStatsUniPkts = _WwpLeosVlanTotalStatsUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 4),
    _WwpLeosVlanTotalStatsUniPkts_Type()
)
wwpLeosVlanTotalStatsUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsUniPkts.setStatus("current")
_WwpLeosVlanTotalStatsNonUniOctets_Type = Counter64
_WwpLeosVlanTotalStatsNonUniOctets_Object = MibTableColumn
wwpLeosVlanTotalStatsNonUniOctets = _WwpLeosVlanTotalStatsNonUniOctets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 5),
    _WwpLeosVlanTotalStatsNonUniOctets_Type()
)
wwpLeosVlanTotalStatsNonUniOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsNonUniOctets.setStatus("current")
_WwpLeosVlanTotalStatsNonUniPkts_Type = Counter32
_WwpLeosVlanTotalStatsNonUniPkts_Object = MibTableColumn
wwpLeosVlanTotalStatsNonUniPkts = _WwpLeosVlanTotalStatsNonUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 6),
    _WwpLeosVlanTotalStatsNonUniPkts_Type()
)
wwpLeosVlanTotalStatsNonUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsNonUniPkts.setStatus("current")
_WwpLeosVlanTotalStatsStatus_Type = RowStatus
_WwpLeosVlanTotalStatsStatus_Object = MibTableColumn
wwpLeosVlanTotalStatsStatus = _WwpLeosVlanTotalStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 7),
    _WwpLeosVlanTotalStatsStatus_Type()
)
wwpLeosVlanTotalStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsStatus.setStatus("current")


class _WwpLeosVlanTotalStatsClear_Type(TruthValue):
    """Custom type wwpLeosVlanTotalStatsClear based on TruthValue"""


_WwpLeosVlanTotalStatsClear_Object = MibTableColumn
wwpLeosVlanTotalStatsClear = _WwpLeosVlanTotalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 8),
    _WwpLeosVlanTotalStatsClear_Type()
)
wwpLeosVlanTotalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsClear.setStatus("current")


class _WwpLeosVlanTotalStatsPortId_Type(Integer32):
    """Custom type wwpLeosVlanTotalStatsPortId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVlanTotalStatsPortId_Type.__name__ = "Integer32"
_WwpLeosVlanTotalStatsPortId_Object = MibTableColumn
wwpLeosVlanTotalStatsPortId = _WwpLeosVlanTotalStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 12, 1, 9),
    _WwpLeosVlanTotalStatsPortId_Type()
)
wwpLeosVlanTotalStatsPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanTotalStatsPortId.setStatus("current")
_WwpLeosVlanTranslationTable_Object = MibTable
wwpLeosVlanTranslationTable = _WwpLeosVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationTable.setStatus("current")
_WwpLeosVlanTranslationEntry_Object = MibTableRow
wwpLeosVlanTranslationEntry = _WwpLeosVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1)
)
wwpLeosVlanTranslationEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanTranslationPgId"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanTranslationFrameVid"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationEntry.setStatus("current")


class _WwpLeosVlanTranslationPgId_Type(Integer32):
    """Custom type wwpLeosVlanTranslationPgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVlanTranslationPgId_Type.__name__ = "Integer32"
_WwpLeosVlanTranslationPgId_Object = MibTableColumn
wwpLeosVlanTranslationPgId = _WwpLeosVlanTranslationPgId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 1),
    _WwpLeosVlanTranslationPgId_Type()
)
wwpLeosVlanTranslationPgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationPgId.setStatus("current")
_WwpLeosVlanTranslationFrameVid_Type = VlanTag
_WwpLeosVlanTranslationFrameVid_Object = MibTableColumn
wwpLeosVlanTranslationFrameVid = _WwpLeosVlanTranslationFrameVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 2),
    _WwpLeosVlanTranslationFrameVid_Type()
)
wwpLeosVlanTranslationFrameVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationFrameVid.setStatus("current")
_WwpLeosVlanTranslationVlanId_Type = VlanTag
_WwpLeosVlanTranslationVlanId_Object = MibTableColumn
wwpLeosVlanTranslationVlanId = _WwpLeosVlanTranslationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 3),
    _WwpLeosVlanTranslationVlanId_Type()
)
wwpLeosVlanTranslationVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationVlanId.setStatus("current")
_WwpLeosVlanTranslationStatus_Type = RowStatus
_WwpLeosVlanTranslationStatus_Object = MibTableColumn
wwpLeosVlanTranslationStatus = _WwpLeosVlanTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 1, 13, 1, 4),
    _WwpLeosVlanTranslationStatus_Type()
)
wwpLeosVlanTranslationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVlanTranslationStatus.setStatus("current")
_WwpLeosVlanEPR_ObjectIdentity = ObjectIdentity
wwpLeosVlanEPR = _WwpLeosVlanEPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2)
)
_WwpLeosVlanEPRTable_Object = MibTable
wwpLeosVlanEPRTable = _WwpLeosVlanEPRTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosVlanEPRTable.setStatus("current")
_WwpLeosVlanEPREntry_Object = MibTableRow
wwpLeosVlanEPREntry = _WwpLeosVlanEPREntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 1, 1)
)
wwpLeosVlanEPREntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanEPREntry.setStatus("current")


class _WwpLeosVlanEPRState_Type(Integer32):
    """Custom type wwpLeosVlanEPRState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosVlanEPRState_Type.__name__ = "Integer32"
_WwpLeosVlanEPRState_Object = MibTableColumn
wwpLeosVlanEPRState = _WwpLeosVlanEPRState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 1, 1, 1),
    _WwpLeosVlanEPRState_Type()
)
wwpLeosVlanEPRState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanEPRState.setStatus("current")
_WwpLeosVlanEPRGrpMemTable_Object = MibTable
wwpLeosVlanEPRGrpMemTable = _WwpLeosVlanEPRGrpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpMemTable.setStatus("current")
_WwpLeosVlanEPRGrpMemEntry_Object = MibTableRow
wwpLeosVlanEPRGrpMemEntry = _WwpLeosVlanEPRGrpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 2, 1)
)
wwpLeosVlanEPRGrpMemEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberPortId"),
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanMemberTagId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpMemEntry.setStatus("current")


class _WwpLeosVlanEPRGrpName_Type(Integer32):
    """Custom type wwpLeosVlanEPRGrpName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groupA", 1),
          ("groupB", 2))
    )


_WwpLeosVlanEPRGrpName_Type.__name__ = "Integer32"
_WwpLeosVlanEPRGrpName_Object = MibTableColumn
wwpLeosVlanEPRGrpName = _WwpLeosVlanEPRGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 2, 1, 1),
    _WwpLeosVlanEPRGrpName_Type()
)
wwpLeosVlanEPRGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpName.setStatus("current")
_WwpLeosVlanEPRGrpAccessTable_Object = MibTable
wwpLeosVlanEPRGrpAccessTable = _WwpLeosVlanEPRGrpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpAccessTable.setStatus("current")
_WwpLeosVlanEPRGrpAccessEntry_Object = MibTableRow
wwpLeosVlanEPRGrpAccessEntry = _WwpLeosVlanEPRGrpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3, 1)
)
wwpLeosVlanEPRGrpAccessEntry.setIndexNames(
    (0, "WWP-LEOS-VLAN-TAG-MIB", "wwpLeosVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpAccessEntry.setStatus("current")


class _WwpLeosVlanEPRGrpAAccess_Type(Integer32):
    """Custom type wwpLeosVlanEPRGrpAAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("groupA", 1),
          ("groupAB", 3),
          ("groupB", 2))
    )


_WwpLeosVlanEPRGrpAAccess_Type.__name__ = "Integer32"
_WwpLeosVlanEPRGrpAAccess_Object = MibTableColumn
wwpLeosVlanEPRGrpAAccess = _WwpLeosVlanEPRGrpAAccess_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3, 1, 1),
    _WwpLeosVlanEPRGrpAAccess_Type()
)
wwpLeosVlanEPRGrpAAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpAAccess.setStatus("current")


class _WwpLeosVlanEPRGrpBAccess_Type(Integer32):
    """Custom type wwpLeosVlanEPRGrpBAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("groupA", 1),
          ("groupAB", 3),
          ("groupB", 2))
    )


_WwpLeosVlanEPRGrpBAccess_Type.__name__ = "Integer32"
_WwpLeosVlanEPRGrpBAccess_Object = MibTableColumn
wwpLeosVlanEPRGrpBAccess = _WwpLeosVlanEPRGrpBAccess_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 1, 2, 3, 1, 2),
    _WwpLeosVlanEPRGrpBAccess_Type()
)
wwpLeosVlanEPRGrpBAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVlanEPRGrpBAccess.setStatus("current")
_WwpLeosVlanMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosVlanMIBNotificationPrefix = _WwpLeosVlanMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 2)
)
_WwpLeosVlanMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosVlanMIBNotifications = _WwpLeosVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 2, 0)
)
_WwpLeosVlanMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosVlanMIBConformance = _WwpLeosVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 3)
)
_WwpLeosVlanMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosVlanMIBCompliances = _WwpLeosVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 3, 1)
)
_WwpLeosVlanMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosVlanMIBGroups = _WwpLeosVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 5, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-VLAN-TAG-MIB",
    **{"VlanId": VlanId,
       "VlanTag": VlanTag,
       "wwpLeosVlanMIB": wwpLeosVlanMIB,
       "wwpLeosVlanMIBObjects": wwpLeosVlanMIBObjects,
       "wwpLeosVlan": wwpLeosVlan,
       "wwpLeosMaxVlans": wwpLeosMaxVlans,
       "wwpLeosMaxSupportedVlanTagId": wwpLeosMaxSupportedVlanTagId,
       "wwpLeosNumVlans": wwpLeosNumVlans,
       "wwpLeosVlanTable": wwpLeosVlanTable,
       "wwpLeosVlanEntry": wwpLeosVlanEntry,
       "wwpLeosVlanId": wwpLeosVlanId,
       "wwpLeosVlanName": wwpLeosVlanName,
       "wwpLeosVlanStatus": wwpLeosVlanStatus,
       "wwpLeosVlanMacLrnState": wwpLeosVlanMacLrnState,
       "wwpLeosVlanMacLrnOperState": wwpLeosVlanMacLrnOperState,
       "wwpLeosVlanTranslationVlan": wwpLeosVlanTranslationVlan,
       "wwpLeosVlanEgressTpid": wwpLeosVlanEgressTpid,
       "wwpLeosVlanTagMemberTable": wwpLeosVlanTagMemberTable,
       "wwpLeosVlanTagMemberEntry": wwpLeosVlanTagMemberEntry,
       "wwpLeosVlanMemberPortId": wwpLeosVlanMemberPortId,
       "wwpLeosVlanMemberTagId": wwpLeosVlanMemberTagId,
       "wwpLeosVlanMemberStatus": wwpLeosVlanMemberStatus,
       "wwpLeosVlanCircuitTable": wwpLeosVlanCircuitTable,
       "wwpLeosVlanCircuitEntry": wwpLeosVlanCircuitEntry,
       "wwpLeosCircuitIndex": wwpLeosCircuitIndex,
       "wwpLeosCircuitVlanId": wwpLeosCircuitVlanId,
       "wwpLeosCircuitType": wwpLeosCircuitType,
       "wwpLeosCircuitName": wwpLeosCircuitName,
       "wwpLeosCircuitPriority": wwpLeosCircuitPriority,
       "wwpLeosCircuitDataTunnelState": wwpLeosCircuitDataTunnelState,
       "wwpLeosCircuitCtrlProtocolTunnelState": wwpLeosCircuitCtrlProtocolTunnelState,
       "wwpLeosCircuitNumEndPoints": wwpLeosCircuitNumEndPoints,
       "wwpLeosCircuitStatus": wwpLeosCircuitStatus,
       "wwpLeosVlanCircuitPortExclusiveTable": wwpLeosVlanCircuitPortExclusiveTable,
       "wwpLeosVlanCircuitPortExclusiveEntry": wwpLeosVlanCircuitPortExclusiveEntry,
       "wwpLeosPortId": wwpLeosPortId,
       "wwpLeosPortExclusiveStatus": wwpLeosPortExclusiveStatus,
       "wwpLeosVlanCircuitCtrlProtocolTable": wwpLeosVlanCircuitCtrlProtocolTable,
       "wwpLeosVlanCircuitCtrlProtocolEntry": wwpLeosVlanCircuitCtrlProtocolEntry,
       "wwpLeosVlanl2ProtocolNum": wwpLeosVlanl2ProtocolNum,
       "wwpLeosVlanl2Type": wwpLeosVlanl2Type,
       "wwpLeosVlanCircuitStats": wwpLeosVlanCircuitStats,
       "wwpLeosVlanl2AllRxPkts": wwpLeosVlanl2AllRxPkts,
       "wwpLeosVlanl2AllTunneledPkts": wwpLeosVlanl2AllTunneledPkts,
       "wwpLeosVlanl2AllPeerPkts": wwpLeosVlanl2AllPeerPkts,
       "wwpLeosVlanl2AllDiscardedPkts": wwpLeosVlanl2AllDiscardedPkts,
       "wwpLeosVlanl2AllDecodedPkts": wwpLeosVlanl2AllDecodedPkts,
       "wwpLeosVlanl2AllDecodedFailures": wwpLeosVlanl2AllDecodedFailures,
       "wwpLeosVlanl2AllTunneledSubcriberPortPkts": wwpLeosVlanl2AllTunneledSubcriberPortPkts,
       "wwpLeosVlanCircuitProtocolStatsTable": wwpLeosVlanCircuitProtocolStatsTable,
       "wwpLeosVlanCircuitProtocolStatsEntry": wwpLeosVlanCircuitProtocolStatsEntry,
       "wwpLeosVlanl2RxPkts": wwpLeosVlanl2RxPkts,
       "wwpLeosVlanl2TunneledPkts": wwpLeosVlanl2TunneledPkts,
       "wwpLeosVlanl2PeerPkts": wwpLeosVlanl2PeerPkts,
       "wwpLeosVlanl2DiscardedPkts": wwpLeosVlanl2DiscardedPkts,
       "wwpLeosVlanl2DecodedPkts": wwpLeosVlanl2DecodedPkts,
       "wwpLeosVlanl2DecodedFailures": wwpLeosVlanl2DecodedFailures,
       "wwpLeosVlanl2TunneledSubcriberPortPkts": wwpLeosVlanl2TunneledSubcriberPortPkts,
       "wwpLeosVlanStatsTable": wwpLeosVlanStatsTable,
       "wwpLeosVlanStatsEntry": wwpLeosVlanStatsEntry,
       "wwpLeosVlanStatsVlanId": wwpLeosVlanStatsVlanId,
       "wwpLeosVlanStatsCreateTime": wwpLeosVlanStatsCreateTime,
       "wwpLeosVlanStatsUniOctets": wwpLeosVlanStatsUniOctets,
       "wwpLeosVlanStatsUniPkts": wwpLeosVlanStatsUniPkts,
       "wwpLeosVlanStatsNonUniOctets": wwpLeosVlanStatsNonUniOctets,
       "wwpLeosVlanStatsNonUniPkts": wwpLeosVlanStatsNonUniPkts,
       "wwpLeosVlanStatsStatus": wwpLeosVlanStatsStatus,
       "wwpLeosVlanStatsClear": wwpLeosVlanStatsClear,
       "wwpLeosVlanStatsPortId": wwpLeosVlanStatsPortId,
       "wwpLeosVlanTotalStatsTable": wwpLeosVlanTotalStatsTable,
       "wwpLeosVlanTotalStatsEntry": wwpLeosVlanTotalStatsEntry,
       "wwpLeosVlanTotalStatsVlanId": wwpLeosVlanTotalStatsVlanId,
       "wwpLeosVlanTotalStatsCreateTime": wwpLeosVlanTotalStatsCreateTime,
       "wwpLeosVlanTotalStatsUniOctets": wwpLeosVlanTotalStatsUniOctets,
       "wwpLeosVlanTotalStatsUniPkts": wwpLeosVlanTotalStatsUniPkts,
       "wwpLeosVlanTotalStatsNonUniOctets": wwpLeosVlanTotalStatsNonUniOctets,
       "wwpLeosVlanTotalStatsNonUniPkts": wwpLeosVlanTotalStatsNonUniPkts,
       "wwpLeosVlanTotalStatsStatus": wwpLeosVlanTotalStatsStatus,
       "wwpLeosVlanTotalStatsClear": wwpLeosVlanTotalStatsClear,
       "wwpLeosVlanTotalStatsPortId": wwpLeosVlanTotalStatsPortId,
       "wwpLeosVlanTranslationTable": wwpLeosVlanTranslationTable,
       "wwpLeosVlanTranslationEntry": wwpLeosVlanTranslationEntry,
       "wwpLeosVlanTranslationPgId": wwpLeosVlanTranslationPgId,
       "wwpLeosVlanTranslationFrameVid": wwpLeosVlanTranslationFrameVid,
       "wwpLeosVlanTranslationVlanId": wwpLeosVlanTranslationVlanId,
       "wwpLeosVlanTranslationStatus": wwpLeosVlanTranslationStatus,
       "wwpLeosVlanEPR": wwpLeosVlanEPR,
       "wwpLeosVlanEPRTable": wwpLeosVlanEPRTable,
       "wwpLeosVlanEPREntry": wwpLeosVlanEPREntry,
       "wwpLeosVlanEPRState": wwpLeosVlanEPRState,
       "wwpLeosVlanEPRGrpMemTable": wwpLeosVlanEPRGrpMemTable,
       "wwpLeosVlanEPRGrpMemEntry": wwpLeosVlanEPRGrpMemEntry,
       "wwpLeosVlanEPRGrpName": wwpLeosVlanEPRGrpName,
       "wwpLeosVlanEPRGrpAccessTable": wwpLeosVlanEPRGrpAccessTable,
       "wwpLeosVlanEPRGrpAccessEntry": wwpLeosVlanEPRGrpAccessEntry,
       "wwpLeosVlanEPRGrpAAccess": wwpLeosVlanEPRGrpAAccess,
       "wwpLeosVlanEPRGrpBAccess": wwpLeosVlanEPRGrpBAccess,
       "wwpLeosVlanMIBNotificationPrefix": wwpLeosVlanMIBNotificationPrefix,
       "wwpLeosVlanMIBNotifications": wwpLeosVlanMIBNotifications,
       "wwpLeosVlanMIBConformance": wwpLeosVlanMIBConformance,
       "wwpLeosVlanMIBCompliances": wwpLeosVlanMIBCompliances,
       "wwpLeosVlanMIBGroups": wwpLeosVlanMIBGroups}
)
