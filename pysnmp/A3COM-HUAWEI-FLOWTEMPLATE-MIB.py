# SNMP MIB module (A3COM-HUAWEI-FLOWTEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-FLOWTEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:01 2024
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

h3cFlowTemplate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFlowTemplateMibObject_ObjectIdentity = ObjectIdentity
h3cFlowTemplateMibObject = _H3cFlowTemplateMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1)
)
_H3cFTConfigGroup_ObjectIdentity = ObjectIdentity
h3cFTConfigGroup = _H3cFTConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1)
)
_H3cFTGroupNextIndex_Type = Integer32
_H3cFTGroupNextIndex_Object = MibScalar
h3cFTGroupNextIndex = _H3cFTGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 1),
    _H3cFTGroupNextIndex_Type()
)
h3cFTGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFTGroupNextIndex.setStatus("current")
_H3cFTGroupTable_Object = MibTable
h3cFTGroupTable = _H3cFTGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cFTGroupTable.setStatus("current")
_H3cFTGroupEntry_Object = MibTableRow
h3cFTGroupEntry = _H3cFTGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 2, 1)
)
h3cFTGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-FLOWTEMPLATE-MIB", "h3cFTGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cFTGroupEntry.setStatus("current")
_H3cFTGroupIndex_Type = Integer32
_H3cFTGroupIndex_Object = MibTableColumn
h3cFTGroupIndex = _H3cFTGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 2, 1, 1),
    _H3cFTGroupIndex_Type()
)
h3cFTGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFTGroupIndex.setStatus("current")


class _H3cFTGroupName_Type(OctetString):
    """Custom type h3cFTGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cFTGroupName_Type.__name__ = "OctetString"
_H3cFTGroupName_Object = MibTableColumn
h3cFTGroupName = _H3cFTGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 2, 1, 2),
    _H3cFTGroupName_Type()
)
h3cFTGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTGroupName.setStatus("current")


class _H3cFTGroupType_Type(Integer32):
    """Custom type h3cFTGroupType based on Integer32"""
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


_H3cFTGroupType_Type.__name__ = "Integer32"
_H3cFTGroupType_Object = MibTableColumn
h3cFTGroupType = _H3cFTGroupType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 2, 1, 3),
    _H3cFTGroupType_Type()
)
h3cFTGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTGroupType.setStatus("current")
_H3cFTGroupRowStatus_Type = RowStatus
_H3cFTGroupRowStatus_Object = MibTableColumn
h3cFTGroupRowStatus = _H3cFTGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 2, 1, 4),
    _H3cFTGroupRowStatus_Type()
)
h3cFTGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTGroupRowStatus.setStatus("current")
_H3cFTBasicGroupTable_Object = MibTable
h3cFTBasicGroupTable = _H3cFTBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cFTBasicGroupTable.setStatus("current")
_H3cFTBasicGroupEntry_Object = MibTableRow
h3cFTBasicGroupEntry = _H3cFTBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1)
)
h3cFTBasicGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-FLOWTEMPLATE-MIB", "h3cFTGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cFTBasicGroupEntry.setStatus("current")


class _H3cFTBasicGroupAddressType_Type(Bits):
    """Custom type h3cFTBasicGroupAddressType based on Bits"""
    namedValues = NamedValues(
        *(("destIPv4Address", 1),
          ("destIPv6Address", 3),
          ("destMacAddress", 5),
          ("sourceIPv6Address", 2),
          ("sourceIpv4Address", 0),
          ("sourceMacAddress", 4))
    )

_H3cFTBasicGroupAddressType_Type.__name__ = "Bits"
_H3cFTBasicGroupAddressType_Object = MibTableColumn
h3cFTBasicGroupAddressType = _H3cFTBasicGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1, 1),
    _H3cFTBasicGroupAddressType_Type()
)
h3cFTBasicGroupAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTBasicGroupAddressType.setStatus("current")


class _H3cFTBasicGroupPriorityType_Type(Bits):
    """Custom type h3cFTBasicGroupPriorityType based on Bits"""
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

_H3cFTBasicGroupPriorityType_Type.__name__ = "Bits"
_H3cFTBasicGroupPriorityType_Object = MibTableColumn
h3cFTBasicGroupPriorityType = _H3cFTBasicGroupPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1, 2),
    _H3cFTBasicGroupPriorityType_Type()
)
h3cFTBasicGroupPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTBasicGroupPriorityType.setStatus("current")


class _H3cFTBasicGroupProtocolType_Type(Bits):
    """Custom type h3cFTBasicGroupProtocolType based on Bits"""
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

_H3cFTBasicGroupProtocolType_Type.__name__ = "Bits"
_H3cFTBasicGroupProtocolType_Object = MibTableColumn
h3cFTBasicGroupProtocolType = _H3cFTBasicGroupProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1, 3),
    _H3cFTBasicGroupProtocolType_Type()
)
h3cFTBasicGroupProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTBasicGroupProtocolType.setStatus("current")
_H3cFTBasicGroupSMacWildCard_Type = MacAddress
_H3cFTBasicGroupSMacWildCard_Object = MibTableColumn
h3cFTBasicGroupSMacWildCard = _H3cFTBasicGroupSMacWildCard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1, 4),
    _H3cFTBasicGroupSMacWildCard_Type()
)
h3cFTBasicGroupSMacWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTBasicGroupSMacWildCard.setStatus("current")
_H3cFTBasicGroupDMacWildCard_Type = MacAddress
_H3cFTBasicGroupDMacWildCard_Object = MibTableColumn
h3cFTBasicGroupDMacWildCard = _H3cFTBasicGroupDMacWildCard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1, 5),
    _H3cFTBasicGroupDMacWildCard_Type()
)
h3cFTBasicGroupDMacWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTBasicGroupDMacWildCard.setStatus("current")
_H3cFTBasicGroupRowStatus_Type = RowStatus
_H3cFTBasicGroupRowStatus_Object = MibTableColumn
h3cFTBasicGroupRowStatus = _H3cFTBasicGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 3, 1, 6),
    _H3cFTBasicGroupRowStatus_Type()
)
h3cFTBasicGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTBasicGroupRowStatus.setStatus("current")
_H3cFTExtendGroupTable_Object = MibTable
h3cFTExtendGroupTable = _H3cFTExtendGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3cFTExtendGroupTable.setStatus("current")
_H3cFTExtendGroupEntry_Object = MibTableRow
h3cFTExtendGroupEntry = _H3cFTExtendGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 4, 1)
)
h3cFTExtendGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-FLOWTEMPLATE-MIB", "h3cFTGroupIndex"),
    (0, "A3COM-HUAWEI-FLOWTEMPLATE-MIB", "h3cFTExtendGroupOffsetType"),
)
if mibBuilder.loadTexts:
    h3cFTExtendGroupEntry.setStatus("current")


class _H3cFTExtendGroupOffsetType_Type(Integer32):
    """Custom type h3cFTExtendGroupOffsetType based on Integer32"""
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


_H3cFTExtendGroupOffsetType_Type.__name__ = "Integer32"
_H3cFTExtendGroupOffsetType_Object = MibTableColumn
h3cFTExtendGroupOffsetType = _H3cFTExtendGroupOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 4, 1, 1),
    _H3cFTExtendGroupOffsetType_Type()
)
h3cFTExtendGroupOffsetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFTExtendGroupOffsetType.setStatus("current")
_H3cFTExtendGroupOffsetMaxValue_Type = Integer32
_H3cFTExtendGroupOffsetMaxValue_Object = MibTableColumn
h3cFTExtendGroupOffsetMaxValue = _H3cFTExtendGroupOffsetMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 4, 1, 2),
    _H3cFTExtendGroupOffsetMaxValue_Type()
)
h3cFTExtendGroupOffsetMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTExtendGroupOffsetMaxValue.setStatus("current")
_H3cFTExtendGroupLengthMaxValue_Type = Integer32
_H3cFTExtendGroupLengthMaxValue_Object = MibTableColumn
h3cFTExtendGroupLengthMaxValue = _H3cFTExtendGroupLengthMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 4, 1, 3),
    _H3cFTExtendGroupLengthMaxValue_Type()
)
h3cFTExtendGroupLengthMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTExtendGroupLengthMaxValue.setStatus("current")
_H3cFTExtendGroupRowStatus_Type = RowStatus
_H3cFTExtendGroupRowStatus_Object = MibTableColumn
h3cFTExtendGroupRowStatus = _H3cFTExtendGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 1, 4, 1, 4),
    _H3cFTExtendGroupRowStatus_Type()
)
h3cFTExtendGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTExtendGroupRowStatus.setStatus("current")
_H3cFTApplyGroup_ObjectIdentity = ObjectIdentity
h3cFTApplyGroup = _H3cFTApplyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 2)
)
_H3cFTIfApplyTable_Object = MibTable
h3cFTIfApplyTable = _H3cFTIfApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFTIfApplyTable.setStatus("current")
_H3cFTIfApplyEntry_Object = MibTableRow
h3cFTIfApplyEntry = _H3cFTIfApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 2, 1, 1)
)
h3cFTIfApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-FLOWTEMPLATE-MIB", "h3cFTGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cFTIfApplyEntry.setStatus("current")
_H3cFTIfApplyGroupName_Type = OctetString
_H3cFTIfApplyGroupName_Object = MibTableColumn
h3cFTIfApplyGroupName = _H3cFTIfApplyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 2, 1, 1, 1),
    _H3cFTIfApplyGroupName_Type()
)
h3cFTIfApplyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFTIfApplyGroupName.setStatus("current")
_H3cFTIfApplyRowStatus_Type = RowStatus
_H3cFTIfApplyRowStatus_Object = MibTableColumn
h3cFTIfApplyRowStatus = _H3cFTIfApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 64, 1, 2, 1, 1, 2),
    _H3cFTIfApplyRowStatus_Type()
)
h3cFTIfApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFTIfApplyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-FLOWTEMPLATE-MIB",
    **{"h3cFlowTemplate": h3cFlowTemplate,
       "h3cFlowTemplateMibObject": h3cFlowTemplateMibObject,
       "h3cFTConfigGroup": h3cFTConfigGroup,
       "h3cFTGroupNextIndex": h3cFTGroupNextIndex,
       "h3cFTGroupTable": h3cFTGroupTable,
       "h3cFTGroupEntry": h3cFTGroupEntry,
       "h3cFTGroupIndex": h3cFTGroupIndex,
       "h3cFTGroupName": h3cFTGroupName,
       "h3cFTGroupType": h3cFTGroupType,
       "h3cFTGroupRowStatus": h3cFTGroupRowStatus,
       "h3cFTBasicGroupTable": h3cFTBasicGroupTable,
       "h3cFTBasicGroupEntry": h3cFTBasicGroupEntry,
       "h3cFTBasicGroupAddressType": h3cFTBasicGroupAddressType,
       "h3cFTBasicGroupPriorityType": h3cFTBasicGroupPriorityType,
       "h3cFTBasicGroupProtocolType": h3cFTBasicGroupProtocolType,
       "h3cFTBasicGroupSMacWildCard": h3cFTBasicGroupSMacWildCard,
       "h3cFTBasicGroupDMacWildCard": h3cFTBasicGroupDMacWildCard,
       "h3cFTBasicGroupRowStatus": h3cFTBasicGroupRowStatus,
       "h3cFTExtendGroupTable": h3cFTExtendGroupTable,
       "h3cFTExtendGroupEntry": h3cFTExtendGroupEntry,
       "h3cFTExtendGroupOffsetType": h3cFTExtendGroupOffsetType,
       "h3cFTExtendGroupOffsetMaxValue": h3cFTExtendGroupOffsetMaxValue,
       "h3cFTExtendGroupLengthMaxValue": h3cFTExtendGroupLengthMaxValue,
       "h3cFTExtendGroupRowStatus": h3cFTExtendGroupRowStatus,
       "h3cFTApplyGroup": h3cFTApplyGroup,
       "h3cFTIfApplyTable": h3cFTIfApplyTable,
       "h3cFTIfApplyEntry": h3cFTIfApplyEntry,
       "h3cFTIfApplyGroupName": h3cFTIfApplyGroupName,
       "h3cFTIfApplyRowStatus": h3cFTIfApplyRowStatus}
)
