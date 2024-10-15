# SNMP MIB module (HH3C-FLOWTEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FLOWTEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:26 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cFlowTemplate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFlowTemplateMibObject_ObjectIdentity = ObjectIdentity
hh3cFlowTemplateMibObject = _Hh3cFlowTemplateMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1)
)
_Hh3cFTConfigGroup_ObjectIdentity = ObjectIdentity
hh3cFTConfigGroup = _Hh3cFTConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1)
)
_Hh3cFTGroupNextIndex_Type = Integer32
_Hh3cFTGroupNextIndex_Object = MibScalar
hh3cFTGroupNextIndex = _Hh3cFTGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 1),
    _Hh3cFTGroupNextIndex_Type()
)
hh3cFTGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFTGroupNextIndex.setStatus("current")
_Hh3cFTGroupTable_Object = MibTable
hh3cFTGroupTable = _Hh3cFTGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFTGroupTable.setStatus("current")
_Hh3cFTGroupEntry_Object = MibTableRow
hh3cFTGroupEntry = _Hh3cFTGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1)
)
hh3cFTGroupEntry.setIndexNames(
    (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cFTGroupEntry.setStatus("current")
_Hh3cFTGroupIndex_Type = Integer32
_Hh3cFTGroupIndex_Object = MibTableColumn
hh3cFTGroupIndex = _Hh3cFTGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 1),
    _Hh3cFTGroupIndex_Type()
)
hh3cFTGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFTGroupIndex.setStatus("current")


class _Hh3cFTGroupName_Type(OctetString):
    """Custom type hh3cFTGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cFTGroupName_Type.__name__ = "OctetString"
_Hh3cFTGroupName_Object = MibTableColumn
hh3cFTGroupName = _Hh3cFTGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 2),
    _Hh3cFTGroupName_Type()
)
hh3cFTGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTGroupName.setStatus("current")


class _Hh3cFTGroupType_Type(Integer32):
    """Custom type hh3cFTGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("extend", 2))
    )


_Hh3cFTGroupType_Type.__name__ = "Integer32"
_Hh3cFTGroupType_Object = MibTableColumn
hh3cFTGroupType = _Hh3cFTGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 3),
    _Hh3cFTGroupType_Type()
)
hh3cFTGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTGroupType.setStatus("current")
_Hh3cFTGroupRowStatus_Type = RowStatus
_Hh3cFTGroupRowStatus_Object = MibTableColumn
hh3cFTGroupRowStatus = _Hh3cFTGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 4),
    _Hh3cFTGroupRowStatus_Type()
)
hh3cFTGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTGroupRowStatus.setStatus("current")
_Hh3cFTBasicGroupTable_Object = MibTable
hh3cFTBasicGroupTable = _Hh3cFTBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cFTBasicGroupTable.setStatus("current")
_Hh3cFTBasicGroupEntry_Object = MibTableRow
hh3cFTBasicGroupEntry = _Hh3cFTBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1)
)
hh3cFTBasicGroupEntry.setIndexNames(
    (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cFTBasicGroupEntry.setStatus("current")


class _Hh3cFTBasicGroupAddressType_Type(Bits):
    """Custom type hh3cFTBasicGroupAddressType based on Bits"""
    namedValues = NamedValues(
        *(("destIPv4Address", 1),
          ("destIPv6Address", 3),
          ("destMacAddress", 5),
          ("sourceIPv6Address", 2),
          ("sourceIpv4Address", 0),
          ("sourceMacAddress", 4))
    )

_Hh3cFTBasicGroupAddressType_Type.__name__ = "Bits"
_Hh3cFTBasicGroupAddressType_Object = MibTableColumn
hh3cFTBasicGroupAddressType = _Hh3cFTBasicGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 1),
    _Hh3cFTBasicGroupAddressType_Type()
)
hh3cFTBasicGroupAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTBasicGroupAddressType.setStatus("current")


class _Hh3cFTBasicGroupPriorityType_Type(Bits):
    """Custom type hh3cFTBasicGroupPriorityType based on Bits"""
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 7),
          ("fragment", 4),
          ("ipprecedence", 8),
          ("tcpFlag", 5),
          ("topCos", 3),
          ("topVlanID", 2),
          ("tos", 6),
          ("vlanID", 0))
    )

_Hh3cFTBasicGroupPriorityType_Type.__name__ = "Bits"
_Hh3cFTBasicGroupPriorityType_Object = MibTableColumn
hh3cFTBasicGroupPriorityType = _Hh3cFTBasicGroupPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 2),
    _Hh3cFTBasicGroupPriorityType_Type()
)
hh3cFTBasicGroupPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTBasicGroupPriorityType.setStatus("current")


class _Hh3cFTBasicGroupProtocolType_Type(Bits):
    """Custom type hh3cFTBasicGroupProtocolType based on Bits"""
    namedValues = NamedValues(
        *(("destL4Port", 8),
          ("icmpProtocolCode", 4),
          ("icmpProtocolType", 3),
          ("icmpv6ProtocolCode", 6),
          ("icmpv6ProtocolType", 5),
          ("ipv4L3Protocol", 1),
          ("ipv6L3Protocol", 2),
          ("l2Potocol", 0),
          ("sourceL4Port", 7))
    )

_Hh3cFTBasicGroupProtocolType_Type.__name__ = "Bits"
_Hh3cFTBasicGroupProtocolType_Object = MibTableColumn
hh3cFTBasicGroupProtocolType = _Hh3cFTBasicGroupProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 3),
    _Hh3cFTBasicGroupProtocolType_Type()
)
hh3cFTBasicGroupProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTBasicGroupProtocolType.setStatus("current")
_Hh3cFTBasicGroupSMacWildCard_Type = MacAddress
_Hh3cFTBasicGroupSMacWildCard_Object = MibTableColumn
hh3cFTBasicGroupSMacWildCard = _Hh3cFTBasicGroupSMacWildCard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 4),
    _Hh3cFTBasicGroupSMacWildCard_Type()
)
hh3cFTBasicGroupSMacWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTBasicGroupSMacWildCard.setStatus("current")
_Hh3cFTBasicGroupDMacWildCard_Type = MacAddress
_Hh3cFTBasicGroupDMacWildCard_Object = MibTableColumn
hh3cFTBasicGroupDMacWildCard = _Hh3cFTBasicGroupDMacWildCard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 5),
    _Hh3cFTBasicGroupDMacWildCard_Type()
)
hh3cFTBasicGroupDMacWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTBasicGroupDMacWildCard.setStatus("current")
_Hh3cFTBasicGroupRowStatus_Type = RowStatus
_Hh3cFTBasicGroupRowStatus_Object = MibTableColumn
hh3cFTBasicGroupRowStatus = _Hh3cFTBasicGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 6),
    _Hh3cFTBasicGroupRowStatus_Type()
)
hh3cFTBasicGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTBasicGroupRowStatus.setStatus("current")
_Hh3cFTExtendGroupTable_Object = MibTable
hh3cFTExtendGroupTable = _Hh3cFTExtendGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cFTExtendGroupTable.setStatus("current")
_Hh3cFTExtendGroupEntry_Object = MibTableRow
hh3cFTExtendGroupEntry = _Hh3cFTExtendGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1)
)
hh3cFTExtendGroupEntry.setIndexNames(
    (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"),
    (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTExtendGroupOffsetType"),
)
if mibBuilder.loadTexts:
    hh3cFTExtendGroupEntry.setStatus("current")


class _Hh3cFTExtendGroupOffsetType_Type(Integer32):
    """Custom type hh3cFTExtendGroupOffsetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 6),
          ("ipv6", 7),
          ("l2", 3),
          ("l4", 4),
          ("l5", 5),
          ("mpls", 2),
          ("start", 1))
    )


_Hh3cFTExtendGroupOffsetType_Type.__name__ = "Integer32"
_Hh3cFTExtendGroupOffsetType_Object = MibTableColumn
hh3cFTExtendGroupOffsetType = _Hh3cFTExtendGroupOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 1),
    _Hh3cFTExtendGroupOffsetType_Type()
)
hh3cFTExtendGroupOffsetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFTExtendGroupOffsetType.setStatus("current")
_Hh3cFTExtendGroupOffsetMaxValue_Type = Integer32
_Hh3cFTExtendGroupOffsetMaxValue_Object = MibTableColumn
hh3cFTExtendGroupOffsetMaxValue = _Hh3cFTExtendGroupOffsetMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 2),
    _Hh3cFTExtendGroupOffsetMaxValue_Type()
)
hh3cFTExtendGroupOffsetMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTExtendGroupOffsetMaxValue.setStatus("current")
_Hh3cFTExtendGroupLengthMaxValue_Type = Integer32
_Hh3cFTExtendGroupLengthMaxValue_Object = MibTableColumn
hh3cFTExtendGroupLengthMaxValue = _Hh3cFTExtendGroupLengthMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 3),
    _Hh3cFTExtendGroupLengthMaxValue_Type()
)
hh3cFTExtendGroupLengthMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTExtendGroupLengthMaxValue.setStatus("current")
_Hh3cFTExtendGroupRowStatus_Type = RowStatus
_Hh3cFTExtendGroupRowStatus_Object = MibTableColumn
hh3cFTExtendGroupRowStatus = _Hh3cFTExtendGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 4),
    _Hh3cFTExtendGroupRowStatus_Type()
)
hh3cFTExtendGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTExtendGroupRowStatus.setStatus("current")
_Hh3cFTApplyGroup_ObjectIdentity = ObjectIdentity
hh3cFTApplyGroup = _Hh3cFTApplyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2)
)
_Hh3cFTIfApplyTable_Object = MibTable
hh3cFTIfApplyTable = _Hh3cFTIfApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFTIfApplyTable.setStatus("current")
_Hh3cFTIfApplyEntry_Object = MibTableRow
hh3cFTIfApplyEntry = _Hh3cFTIfApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1, 1)
)
hh3cFTIfApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cFTIfApplyEntry.setStatus("current")
_Hh3cFTIfApplyGroupName_Type = OctetString
_Hh3cFTIfApplyGroupName_Object = MibTableColumn
hh3cFTIfApplyGroupName = _Hh3cFTIfApplyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1, 1, 1),
    _Hh3cFTIfApplyGroupName_Type()
)
hh3cFTIfApplyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFTIfApplyGroupName.setStatus("current")
_Hh3cFTIfApplyRowStatus_Type = RowStatus
_Hh3cFTIfApplyRowStatus_Object = MibTableColumn
hh3cFTIfApplyRowStatus = _Hh3cFTIfApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1, 1, 2),
    _Hh3cFTIfApplyRowStatus_Type()
)
hh3cFTIfApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFTIfApplyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FLOWTEMPLATE-MIB",
    **{"hh3cFlowTemplate": hh3cFlowTemplate,
       "hh3cFlowTemplateMibObject": hh3cFlowTemplateMibObject,
       "hh3cFTConfigGroup": hh3cFTConfigGroup,
       "hh3cFTGroupNextIndex": hh3cFTGroupNextIndex,
       "hh3cFTGroupTable": hh3cFTGroupTable,
       "hh3cFTGroupEntry": hh3cFTGroupEntry,
       "hh3cFTGroupIndex": hh3cFTGroupIndex,
       "hh3cFTGroupName": hh3cFTGroupName,
       "hh3cFTGroupType": hh3cFTGroupType,
       "hh3cFTGroupRowStatus": hh3cFTGroupRowStatus,
       "hh3cFTBasicGroupTable": hh3cFTBasicGroupTable,
       "hh3cFTBasicGroupEntry": hh3cFTBasicGroupEntry,
       "hh3cFTBasicGroupAddressType": hh3cFTBasicGroupAddressType,
       "hh3cFTBasicGroupPriorityType": hh3cFTBasicGroupPriorityType,
       "hh3cFTBasicGroupProtocolType": hh3cFTBasicGroupProtocolType,
       "hh3cFTBasicGroupSMacWildCard": hh3cFTBasicGroupSMacWildCard,
       "hh3cFTBasicGroupDMacWildCard": hh3cFTBasicGroupDMacWildCard,
       "hh3cFTBasicGroupRowStatus": hh3cFTBasicGroupRowStatus,
       "hh3cFTExtendGroupTable": hh3cFTExtendGroupTable,
       "hh3cFTExtendGroupEntry": hh3cFTExtendGroupEntry,
       "hh3cFTExtendGroupOffsetType": hh3cFTExtendGroupOffsetType,
       "hh3cFTExtendGroupOffsetMaxValue": hh3cFTExtendGroupOffsetMaxValue,
       "hh3cFTExtendGroupLengthMaxValue": hh3cFTExtendGroupLengthMaxValue,
       "hh3cFTExtendGroupRowStatus": hh3cFTExtendGroupRowStatus,
       "hh3cFTApplyGroup": hh3cFTApplyGroup,
       "hh3cFTIfApplyTable": hh3cFTIfApplyTable,
       "hh3cFTIfApplyEntry": hh3cFTIfApplyEntry,
       "hh3cFTIfApplyGroupName": hh3cFTIfApplyGroupName,
       "hh3cFTIfApplyRowStatus": hh3cFTIfApplyRowStatus}
)
