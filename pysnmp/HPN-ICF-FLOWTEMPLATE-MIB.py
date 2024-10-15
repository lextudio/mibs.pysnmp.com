# SNMP MIB module (HPN-ICF-FLOWTEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FLOWTEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:26 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfFlowTemplate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFlowTemplateMibObject_ObjectIdentity = ObjectIdentity
hpnicfFlowTemplateMibObject = _HpnicfFlowTemplateMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1)
)
_HpnicfFTConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfFTConfigGroup = _HpnicfFTConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1)
)
_HpnicfFTGroupNextIndex_Type = Integer32
_HpnicfFTGroupNextIndex_Object = MibScalar
hpnicfFTGroupNextIndex = _HpnicfFTGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 1),
    _HpnicfFTGroupNextIndex_Type()
)
hpnicfFTGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFTGroupNextIndex.setStatus("current")
_HpnicfFTGroupTable_Object = MibTable
hpnicfFTGroupTable = _HpnicfFTGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfFTGroupTable.setStatus("current")
_HpnicfFTGroupEntry_Object = MibTableRow
hpnicfFTGroupEntry = _HpnicfFTGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1)
)
hpnicfFTGroupEntry.setIndexNames(
    (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFTGroupEntry.setStatus("current")
_HpnicfFTGroupIndex_Type = Integer32
_HpnicfFTGroupIndex_Object = MibTableColumn
hpnicfFTGroupIndex = _HpnicfFTGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 1),
    _HpnicfFTGroupIndex_Type()
)
hpnicfFTGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFTGroupIndex.setStatus("current")


class _HpnicfFTGroupName_Type(OctetString):
    """Custom type hpnicfFTGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfFTGroupName_Type.__name__ = "OctetString"
_HpnicfFTGroupName_Object = MibTableColumn
hpnicfFTGroupName = _HpnicfFTGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 2),
    _HpnicfFTGroupName_Type()
)
hpnicfFTGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTGroupName.setStatus("current")


class _HpnicfFTGroupType_Type(Integer32):
    """Custom type hpnicfFTGroupType based on Integer32"""
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


_HpnicfFTGroupType_Type.__name__ = "Integer32"
_HpnicfFTGroupType_Object = MibTableColumn
hpnicfFTGroupType = _HpnicfFTGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 3),
    _HpnicfFTGroupType_Type()
)
hpnicfFTGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTGroupType.setStatus("current")
_HpnicfFTGroupRowStatus_Type = RowStatus
_HpnicfFTGroupRowStatus_Object = MibTableColumn
hpnicfFTGroupRowStatus = _HpnicfFTGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 4),
    _HpnicfFTGroupRowStatus_Type()
)
hpnicfFTGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTGroupRowStatus.setStatus("current")
_HpnicfFTBasicGroupTable_Object = MibTable
hpnicfFTBasicGroupTable = _HpnicfFTBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupTable.setStatus("current")
_HpnicfFTBasicGroupEntry_Object = MibTableRow
hpnicfFTBasicGroupEntry = _HpnicfFTBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1)
)
hpnicfFTBasicGroupEntry.setIndexNames(
    (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupEntry.setStatus("current")


class _HpnicfFTBasicGroupAddressType_Type(Bits):
    """Custom type hpnicfFTBasicGroupAddressType based on Bits"""
    namedValues = NamedValues(
        *(("destIPv4Address", 1),
          ("destIPv6Address", 3),
          ("destMacAddress", 5),
          ("sourceIPv6Address", 2),
          ("sourceIpv4Address", 0),
          ("sourceMacAddress", 4))
    )

_HpnicfFTBasicGroupAddressType_Type.__name__ = "Bits"
_HpnicfFTBasicGroupAddressType_Object = MibTableColumn
hpnicfFTBasicGroupAddressType = _HpnicfFTBasicGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 1),
    _HpnicfFTBasicGroupAddressType_Type()
)
hpnicfFTBasicGroupAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupAddressType.setStatus("current")


class _HpnicfFTBasicGroupPriorityType_Type(Bits):
    """Custom type hpnicfFTBasicGroupPriorityType based on Bits"""
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

_HpnicfFTBasicGroupPriorityType_Type.__name__ = "Bits"
_HpnicfFTBasicGroupPriorityType_Object = MibTableColumn
hpnicfFTBasicGroupPriorityType = _HpnicfFTBasicGroupPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 2),
    _HpnicfFTBasicGroupPriorityType_Type()
)
hpnicfFTBasicGroupPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupPriorityType.setStatus("current")


class _HpnicfFTBasicGroupProtocolType_Type(Bits):
    """Custom type hpnicfFTBasicGroupProtocolType based on Bits"""
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

_HpnicfFTBasicGroupProtocolType_Type.__name__ = "Bits"
_HpnicfFTBasicGroupProtocolType_Object = MibTableColumn
hpnicfFTBasicGroupProtocolType = _HpnicfFTBasicGroupProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 3),
    _HpnicfFTBasicGroupProtocolType_Type()
)
hpnicfFTBasicGroupProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupProtocolType.setStatus("current")
_HpnicfFTBasicGroupSMacWildCard_Type = MacAddress
_HpnicfFTBasicGroupSMacWildCard_Object = MibTableColumn
hpnicfFTBasicGroupSMacWildCard = _HpnicfFTBasicGroupSMacWildCard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 4),
    _HpnicfFTBasicGroupSMacWildCard_Type()
)
hpnicfFTBasicGroupSMacWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupSMacWildCard.setStatus("current")
_HpnicfFTBasicGroupDMacWildCard_Type = MacAddress
_HpnicfFTBasicGroupDMacWildCard_Object = MibTableColumn
hpnicfFTBasicGroupDMacWildCard = _HpnicfFTBasicGroupDMacWildCard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 5),
    _HpnicfFTBasicGroupDMacWildCard_Type()
)
hpnicfFTBasicGroupDMacWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupDMacWildCard.setStatus("current")
_HpnicfFTBasicGroupRowStatus_Type = RowStatus
_HpnicfFTBasicGroupRowStatus_Object = MibTableColumn
hpnicfFTBasicGroupRowStatus = _HpnicfFTBasicGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 6),
    _HpnicfFTBasicGroupRowStatus_Type()
)
hpnicfFTBasicGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTBasicGroupRowStatus.setStatus("current")
_HpnicfFTExtendGroupTable_Object = MibTable
hpnicfFTExtendGroupTable = _HpnicfFTExtendGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfFTExtendGroupTable.setStatus("current")
_HpnicfFTExtendGroupEntry_Object = MibTableRow
hpnicfFTExtendGroupEntry = _HpnicfFTExtendGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1)
)
hpnicfFTExtendGroupEntry.setIndexNames(
    (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"),
    (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTExtendGroupOffsetType"),
)
if mibBuilder.loadTexts:
    hpnicfFTExtendGroupEntry.setStatus("current")


class _HpnicfFTExtendGroupOffsetType_Type(Integer32):
    """Custom type hpnicfFTExtendGroupOffsetType based on Integer32"""
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


_HpnicfFTExtendGroupOffsetType_Type.__name__ = "Integer32"
_HpnicfFTExtendGroupOffsetType_Object = MibTableColumn
hpnicfFTExtendGroupOffsetType = _HpnicfFTExtendGroupOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 1),
    _HpnicfFTExtendGroupOffsetType_Type()
)
hpnicfFTExtendGroupOffsetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFTExtendGroupOffsetType.setStatus("current")
_HpnicfFTExtendGroupOffsetMaxValue_Type = Integer32
_HpnicfFTExtendGroupOffsetMaxValue_Object = MibTableColumn
hpnicfFTExtendGroupOffsetMaxValue = _HpnicfFTExtendGroupOffsetMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 2),
    _HpnicfFTExtendGroupOffsetMaxValue_Type()
)
hpnicfFTExtendGroupOffsetMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTExtendGroupOffsetMaxValue.setStatus("current")
_HpnicfFTExtendGroupLengthMaxValue_Type = Integer32
_HpnicfFTExtendGroupLengthMaxValue_Object = MibTableColumn
hpnicfFTExtendGroupLengthMaxValue = _HpnicfFTExtendGroupLengthMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 3),
    _HpnicfFTExtendGroupLengthMaxValue_Type()
)
hpnicfFTExtendGroupLengthMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTExtendGroupLengthMaxValue.setStatus("current")
_HpnicfFTExtendGroupRowStatus_Type = RowStatus
_HpnicfFTExtendGroupRowStatus_Object = MibTableColumn
hpnicfFTExtendGroupRowStatus = _HpnicfFTExtendGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 4),
    _HpnicfFTExtendGroupRowStatus_Type()
)
hpnicfFTExtendGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTExtendGroupRowStatus.setStatus("current")
_HpnicfFTApplyGroup_ObjectIdentity = ObjectIdentity
hpnicfFTApplyGroup = _HpnicfFTApplyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2)
)
_HpnicfFTIfApplyTable_Object = MibTable
hpnicfFTIfApplyTable = _HpnicfFTIfApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFTIfApplyTable.setStatus("current")
_HpnicfFTIfApplyEntry_Object = MibTableRow
hpnicfFTIfApplyEntry = _HpnicfFTIfApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1, 1)
)
hpnicfFTIfApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFTIfApplyEntry.setStatus("current")
_HpnicfFTIfApplyGroupName_Type = OctetString
_HpnicfFTIfApplyGroupName_Object = MibTableColumn
hpnicfFTIfApplyGroupName = _HpnicfFTIfApplyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1, 1, 1),
    _HpnicfFTIfApplyGroupName_Type()
)
hpnicfFTIfApplyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFTIfApplyGroupName.setStatus("current")
_HpnicfFTIfApplyRowStatus_Type = RowStatus
_HpnicfFTIfApplyRowStatus_Object = MibTableColumn
hpnicfFTIfApplyRowStatus = _HpnicfFTIfApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1, 1, 2),
    _HpnicfFTIfApplyRowStatus_Type()
)
hpnicfFTIfApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFTIfApplyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FLOWTEMPLATE-MIB",
    **{"hpnicfFlowTemplate": hpnicfFlowTemplate,
       "hpnicfFlowTemplateMibObject": hpnicfFlowTemplateMibObject,
       "hpnicfFTConfigGroup": hpnicfFTConfigGroup,
       "hpnicfFTGroupNextIndex": hpnicfFTGroupNextIndex,
       "hpnicfFTGroupTable": hpnicfFTGroupTable,
       "hpnicfFTGroupEntry": hpnicfFTGroupEntry,
       "hpnicfFTGroupIndex": hpnicfFTGroupIndex,
       "hpnicfFTGroupName": hpnicfFTGroupName,
       "hpnicfFTGroupType": hpnicfFTGroupType,
       "hpnicfFTGroupRowStatus": hpnicfFTGroupRowStatus,
       "hpnicfFTBasicGroupTable": hpnicfFTBasicGroupTable,
       "hpnicfFTBasicGroupEntry": hpnicfFTBasicGroupEntry,
       "hpnicfFTBasicGroupAddressType": hpnicfFTBasicGroupAddressType,
       "hpnicfFTBasicGroupPriorityType": hpnicfFTBasicGroupPriorityType,
       "hpnicfFTBasicGroupProtocolType": hpnicfFTBasicGroupProtocolType,
       "hpnicfFTBasicGroupSMacWildCard": hpnicfFTBasicGroupSMacWildCard,
       "hpnicfFTBasicGroupDMacWildCard": hpnicfFTBasicGroupDMacWildCard,
       "hpnicfFTBasicGroupRowStatus": hpnicfFTBasicGroupRowStatus,
       "hpnicfFTExtendGroupTable": hpnicfFTExtendGroupTable,
       "hpnicfFTExtendGroupEntry": hpnicfFTExtendGroupEntry,
       "hpnicfFTExtendGroupOffsetType": hpnicfFTExtendGroupOffsetType,
       "hpnicfFTExtendGroupOffsetMaxValue": hpnicfFTExtendGroupOffsetMaxValue,
       "hpnicfFTExtendGroupLengthMaxValue": hpnicfFTExtendGroupLengthMaxValue,
       "hpnicfFTExtendGroupRowStatus": hpnicfFTExtendGroupRowStatus,
       "hpnicfFTApplyGroup": hpnicfFTApplyGroup,
       "hpnicfFTIfApplyTable": hpnicfFTIfApplyTable,
       "hpnicfFTIfApplyEntry": hpnicfFTIfApplyEntry,
       "hpnicfFTIfApplyGroupName": hpnicfFTIfApplyGroupName,
       "hpnicfFTIfApplyRowStatus": hpnicfFTIfApplyRowStatus}
)
