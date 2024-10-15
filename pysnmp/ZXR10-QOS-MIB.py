# SNMP MIB module (ZXR10-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:05 2024
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


# MODULE-IDENTITY

zxr10qos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class QosCirMatchType(Integer32):
    """Custom type QosCirMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("match-802dot1p", 8),
          ("match-acl", 4),
          ("match-address-MAc", 37),
          ("match-dscp", 6),
          ("match-localport", 3),
          ("match-mpls-exp", 7),
          ("match-precedence", 5),
          ("match-qos-group", 36),
          ("match-vlanId", 9))
    )





class QosCirAction(Integer32):
    """Custom type QosCirAction based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 0),
          ("set-dscp-continue", 5),
          ("set-dscp-transmit", 6),
          ("set-exp-continue", 9),
          ("set-exp-transmit", 10),
          ("set-prec-continue", 3),
          ("set-prec-transmit", 4),
          ("transmit", 2))
    )





class QosCBQCarAction(Integer32):
    """Custom type QosCBQCarAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("set-dscp-transmit", 6),
          ("set-exp-transmit", 10),
          ("set-prec-transmit", 4),
          ("transmit", 2))
    )





class QosPQMatchType(Integer32):
    """Custom type QosPQMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("match-802dot1p", 8),
          ("match-acl", 4),
          ("match-address-MAc", 37),
          ("match-default", 1),
          ("match-dscp", 6),
          ("match-interface", 3),
          ("match-mpls-exp", 7),
          ("match-precedence", 5),
          ("match-qos-group", 36),
          ("match-vlanId", 9))
    )





class QosPQQueueType(Integer32):
    """Custom type QosPQQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("low", 3),
          ("medium", 1),
          ("normal", 2))
    )





class QosCMAPMatchType(Integer32):
    """Custom type QosCMAPMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8,
              9,
              19,
              21,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("match-802dot1p", 8),
          ("match-acl", 4),
          ("match-address-MAc", 37),
          ("match-any", 19),
          ("match-classmap", 21),
          ("match-dscp", 6),
          ("match-mpls-exp", 7),
          ("match-not", 1),
          ("match-precedence", 5),
          ("match-qos-group", 36),
          ("match-vlanId", 9))
    )





class TrafficDirection(Integer32):
    """Custom type TrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("output", 2)
    )





class QueueingBandwidthUnits(Integer32):
    """Custom type QueueingBandwidthUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("percentage", 1))
    )




# TEXTUAL-CONVENTIONS



class EntryStatus(Integer32, TextualConvention):
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10protocol_ObjectIdentity = ObjectIdentity
zxr10protocol = _Zxr10protocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101)
)
_QosModuleStart_Type = Integer32
_QosModuleStart_Object = MibScalar
qosModuleStart = _QosModuleStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 1),
    _QosModuleStart_Type()
)
qosModuleStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosModuleStart.setStatus("current")
_QosPQconfig_ObjectIdentity = ObjectIdentity
qosPQconfig = _QosPQconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2)
)
_QosPriorityQueueCfgTable_Object = MibTable
qosPriorityQueueCfgTable = _QosPriorityQueueCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1)
)
if mibBuilder.loadTexts:
    qosPriorityQueueCfgTable.setStatus("current")
_QosPriorityQueueCfgEntry_Object = MibTableRow
qosPriorityQueueCfgEntry = _QosPriorityQueueCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1)
)
qosPriorityQueueCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qosPriorityQueueIndex"),
)
if mibBuilder.loadTexts:
    qosPriorityQueueCfgEntry.setStatus("current")
_QosPriorityQueueIndex_Type = Integer32
_QosPriorityQueueIndex_Object = MibTableColumn
qosPriorityQueueIndex = _QosPriorityQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 1),
    _QosPriorityQueueIndex_Type()
)
qosPriorityQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPriorityQueueIndex.setStatus("current")


class _QosPriorityQueueItemTotal_Type(Integer32):
    """Custom type qosPriorityQueueItemTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosPriorityQueueItemTotal_Type.__name__ = "Integer32"
_QosPriorityQueueItemTotal_Object = MibTableColumn
qosPriorityQueueItemTotal = _QosPriorityQueueItemTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 2),
    _QosPriorityQueueItemTotal_Type()
)
qosPriorityQueueItemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPriorityQueueItemTotal.setStatus("current")
_QosPriorityQueueDefault_Type = QosPQQueueType
_QosPriorityQueueDefault_Object = MibTableColumn
qosPriorityQueueDefault = _QosPriorityQueueDefault_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 3),
    _QosPriorityQueueDefault_Type()
)
qosPriorityQueueDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityQueueDefault.setStatus("current")
_QosPriorityQueueLimitHigh_Type = Integer32
_QosPriorityQueueLimitHigh_Object = MibTableColumn
qosPriorityQueueLimitHigh = _QosPriorityQueueLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 4),
    _QosPriorityQueueLimitHigh_Type()
)
qosPriorityQueueLimitHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityQueueLimitHigh.setStatus("current")
_QosPriorityQueueLimitMedium_Type = Integer32
_QosPriorityQueueLimitMedium_Object = MibTableColumn
qosPriorityQueueLimitMedium = _QosPriorityQueueLimitMedium_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 5),
    _QosPriorityQueueLimitMedium_Type()
)
qosPriorityQueueLimitMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityQueueLimitMedium.setStatus("current")
_QosPriorityQueueLimitNormal_Type = Integer32
_QosPriorityQueueLimitNormal_Object = MibTableColumn
qosPriorityQueueLimitNormal = _QosPriorityQueueLimitNormal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 6),
    _QosPriorityQueueLimitNormal_Type()
)
qosPriorityQueueLimitNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityQueueLimitNormal.setStatus("current")
_QosPriorityQueueLimitLow_Type = Integer32
_QosPriorityQueueLimitLow_Object = MibTableColumn
qosPriorityQueueLimitLow = _QosPriorityQueueLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 7),
    _QosPriorityQueueLimitLow_Type()
)
qosPriorityQueueLimitLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityQueueLimitLow.setStatus("current")
_QosPriorityQueueRowStatus_Type = EntryStatus
_QosPriorityQueueRowStatus_Object = MibTableColumn
qosPriorityQueueRowStatus = _QosPriorityQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 1, 1, 8),
    _QosPriorityQueueRowStatus_Type()
)
qosPriorityQueueRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityQueueRowStatus.setStatus("current")
_QosPriorityQueueCfgTableLastchange_Type = TimeTicks
_QosPriorityQueueCfgTableLastchange_Object = MibScalar
qosPriorityQueueCfgTableLastchange = _QosPriorityQueueCfgTableLastchange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 2),
    _QosPriorityQueueCfgTableLastchange_Type()
)
qosPriorityQueueCfgTableLastchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPriorityQueueCfgTableLastchange.setStatus("current")
_QosPriorityQueueItemTable_Object = MibTable
qosPriorityQueueItemTable = _QosPriorityQueueItemTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3)
)
if mibBuilder.loadTexts:
    qosPriorityQueueItemTable.setStatus("current")
_QosPriorityQueueItemEntry_Object = MibTableRow
qosPriorityQueueItemEntry = _QosPriorityQueueItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1)
)
qosPriorityQueueItemEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qosPriorityQueueIndex"),
    (0, "ZXR10-QOS-MIB", "qosPriorityQueueItemIndex"),
)
if mibBuilder.loadTexts:
    qosPriorityQueueItemEntry.setStatus("current")
_QosPriorityQueueItemIndex_Type = Integer32
_QosPriorityQueueItemIndex_Object = MibTableColumn
qosPriorityQueueItemIndex = _QosPriorityQueueItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1, 1),
    _QosPriorityQueueItemIndex_Type()
)
qosPriorityQueueItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPriorityQueueItemIndex.setStatus("current")
_QosPriorityQueueItemMatchType_Type = QosPQMatchType
_QosPriorityQueueItemMatchType_Object = MibTableColumn
qosPriorityQueueItemMatchType = _QosPriorityQueueItemMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1, 2),
    _QosPriorityQueueItemMatchType_Type()
)
qosPriorityQueueItemMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityQueueItemMatchType.setStatus("current")
_QosPriorityQueueItemMatchValue_Type = DisplayString
_QosPriorityQueueItemMatchValue_Object = MibTableColumn
qosPriorityQueueItemMatchValue = _QosPriorityQueueItemMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1, 3),
    _QosPriorityQueueItemMatchValue_Type()
)
qosPriorityQueueItemMatchValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityQueueItemMatchValue.setStatus("current")
_QosPriorityQueueItemQueueNum_Type = QosPQQueueType
_QosPriorityQueueItemQueueNum_Object = MibTableColumn
qosPriorityQueueItemQueueNum = _QosPriorityQueueItemQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1, 4),
    _QosPriorityQueueItemQueueNum_Type()
)
qosPriorityQueueItemQueueNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityQueueItemQueueNum.setStatus("current")
_QosPriorityQueueItemRowStatus_Type = EntryStatus
_QosPriorityQueueItemRowStatus_Object = MibTableColumn
qosPriorityQueueItemRowStatus = _QosPriorityQueueItemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1, 5),
    _QosPriorityQueueItemRowStatus_Type()
)
qosPriorityQueueItemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityQueueItemRowStatus.setStatus("current")
_QosPriorityQueueItemDescription_Type = DisplayString
_QosPriorityQueueItemDescription_Object = MibTableColumn
qosPriorityQueueItemDescription = _QosPriorityQueueItemDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 3, 1, 6),
    _QosPriorityQueueItemDescription_Type()
)
qosPriorityQueueItemDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityQueueItemDescription.setStatus("current")
_QosPriorityGroupTable_Object = MibTable
qosPriorityGroupTable = _QosPriorityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 4)
)
if mibBuilder.loadTexts:
    qosPriorityGroupTable.setStatus("current")
_QosPriorityGroupEntry_Object = MibTableRow
qosPriorityGroupEntry = _QosPriorityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 4, 1)
)
qosPriorityGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosPriorityGroupEntry.setStatus("current")
_QosPriorityGroupifname_Type = DisplayString
_QosPriorityGroupifname_Object = MibTableColumn
qosPriorityGroupifname = _QosPriorityGroupifname_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 4, 1, 1),
    _QosPriorityGroupifname_Type()
)
qosPriorityGroupifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPriorityGroupifname.setStatus("current")
_QosPriorityGroupNum_Type = Integer32
_QosPriorityGroupNum_Object = MibTableColumn
qosPriorityGroupNum = _QosPriorityGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 4, 1, 2),
    _QosPriorityGroupNum_Type()
)
qosPriorityGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityGroupNum.setStatus("current")
_QosPriorityGroupRowStatus_Type = EntryStatus
_QosPriorityGroupRowStatus_Object = MibTableColumn
qosPriorityGroupRowStatus = _QosPriorityGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 2, 4, 1, 3),
    _QosPriorityGroupRowStatus_Type()
)
qosPriorityGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPriorityGroupRowStatus.setStatus("current")
_QosCQconfig_ObjectIdentity = ObjectIdentity
qosCQconfig = _QosCQconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 3)
)
_QosCBQconfig_ObjectIdentity = ObjectIdentity
qosCBQconfig = _QosCBQconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4)
)
_QosCBQosServicePolicyTable_Object = MibTable
qosCBQosServicePolicyTable = _QosCBQosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 1)
)
if mibBuilder.loadTexts:
    qosCBQosServicePolicyTable.setStatus("current")
_QosCBQosServicePolicyEntry_Object = MibTableRow
qosCBQosServicePolicyEntry = _QosCBQosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 1, 1)
)
qosCBQosServicePolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosCBQosServicePolicyEntry.setStatus("current")
_QosCbQosPolicyifname_Type = DisplayString
_QosCbQosPolicyifname_Object = MibTableColumn
qosCbQosPolicyifname = _QosCbQosPolicyifname_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 1, 1, 1),
    _QosCbQosPolicyifname_Type()
)
qosCbQosPolicyifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCbQosPolicyifname.setStatus("current")
_QosCbQosPolicyDirection_Type = TrafficDirection
_QosCbQosPolicyDirection_Object = MibTableColumn
qosCbQosPolicyDirection = _QosCbQosPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 1, 1, 2),
    _QosCbQosPolicyDirection_Type()
)
qosCbQosPolicyDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPolicyDirection.setStatus("current")
_QosCbQosServicePolicyName_Type = DisplayString
_QosCbQosServicePolicyName_Object = MibTableColumn
qosCbQosServicePolicyName = _QosCbQosServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 1, 1, 3),
    _QosCbQosServicePolicyName_Type()
)
qosCbQosServicePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosServicePolicyName.setStatus("current")
_QosCbQosServicePolicyRowStatus_Type = EntryStatus
_QosCbQosServicePolicyRowStatus_Object = MibTableColumn
qosCbQosServicePolicyRowStatus = _QosCbQosServicePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 1, 1, 4),
    _QosCbQosServicePolicyRowStatus_Type()
)
qosCbQosServicePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosServicePolicyRowStatus.setStatus("current")
_QosCbQosPolicyMapCfgTable_Object = MibTable
qosCbQosPolicyMapCfgTable = _QosCbQosPolicyMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 2)
)
if mibBuilder.loadTexts:
    qosCbQosPolicyMapCfgTable.setStatus("current")
_QosCbQosPolicyMapCfgEntry_Object = MibTableRow
qosCbQosPolicyMapCfgEntry = _QosCbQosPolicyMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 2, 1)
)
qosCbQosPolicyMapCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosPMapIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosPolicyMapCfgEntry.setStatus("current")
_QoscbQosPMapIndex_Type = Integer32
_QoscbQosPMapIndex_Object = MibTableColumn
qoscbQosPMapIndex = _QoscbQosPMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 2, 1, 1),
    _QoscbQosPMapIndex_Type()
)
qoscbQosPMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoscbQosPMapIndex.setStatus("current")
_QoscbQosPolicyMapName_Type = DisplayString
_QoscbQosPolicyMapName_Object = MibTableColumn
qoscbQosPolicyMapName = _QoscbQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 2, 1, 2),
    _QoscbQosPolicyMapName_Type()
)
qoscbQosPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qoscbQosPolicyMapName.setStatus("current")
_QosCbQosPolicyMapRowStatus_Type = EntryStatus
_QosCbQosPolicyMapRowStatus_Object = MibTableColumn
qosCbQosPolicyMapRowStatus = _QosCbQosPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 2, 1, 3),
    _QosCbQosPolicyMapRowStatus_Type()
)
qosCbQosPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPolicyMapRowStatus.setStatus("current")
_QoscbQosPolicyMapDescription_Type = DisplayString
_QoscbQosPolicyMapDescription_Object = MibTableColumn
qoscbQosPolicyMapDescription = _QoscbQosPolicyMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 2, 1, 4),
    _QoscbQosPolicyMapDescription_Type()
)
qoscbQosPolicyMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qoscbQosPolicyMapDescription.setStatus("current")
_QosCbQosClassMapCfgTable_Object = MibTable
qosCbQosClassMapCfgTable = _QosCbQosClassMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 3)
)
if mibBuilder.loadTexts:
    qosCbQosClassMapCfgTable.setStatus("current")
_QosCbQosClassMapCfgEntry_Object = MibTableRow
qosCbQosClassMapCfgEntry = _QosCbQosClassMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 3, 1)
)
qosCbQosClassMapCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosCMapIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosClassMapCfgEntry.setStatus("current")
_QoscbQosCMapIndex_Type = Integer32
_QoscbQosCMapIndex_Object = MibTableColumn
qoscbQosCMapIndex = _QoscbQosCMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 3, 1, 1),
    _QoscbQosCMapIndex_Type()
)
qoscbQosCMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qoscbQosCMapIndex.setStatus("current")
_QosCbQosClassMapName_Type = DisplayString
_QosCbQosClassMapName_Object = MibTableColumn
qosCbQosClassMapName = _QosCbQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 3, 1, 2),
    _QosCbQosClassMapName_Type()
)
qosCbQosClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosClassMapName.setStatus("current")
_QosCbQosClassMapRowStatus_Type = EntryStatus
_QosCbQosClassMapRowStatus_Object = MibTableColumn
qosCbQosClassMapRowStatus = _QosCbQosClassMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 3, 1, 3),
    _QosCbQosClassMapRowStatus_Type()
)
qosCbQosClassMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosClassMapRowStatus.setStatus("current")
_QoscbQosClassMapDescription_Type = DisplayString
_QoscbQosClassMapDescription_Object = MibTableColumn
qoscbQosClassMapDescription = _QoscbQosClassMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 3, 1, 4),
    _QoscbQosClassMapDescription_Type()
)
qoscbQosClassMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qoscbQosClassMapDescription.setStatus("current")
_QosCbQosCMAPMatchCfgTable_Object = MibTable
qosCbQosCMAPMatchCfgTable = _QosCbQosCMAPMatchCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 4)
)
if mibBuilder.loadTexts:
    qosCbQosCMAPMatchCfgTable.setStatus("current")
_QosCbQosCMAPMatchCfgEntry_Object = MibTableRow
qosCbQosCMAPMatchCfgEntry = _QosCbQosCMAPMatchCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 4, 1)
)
qosCbQosCMAPMatchCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosCMapIndex"),
    (0, "ZXR10-QOS-MIB", "qosCbQosCMAPMatchIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosCMAPMatchCfgEntry.setStatus("current")
_QosCbQosCMAPMatchIndex_Type = Integer32
_QosCbQosCMAPMatchIndex_Object = MibTableColumn
qosCbQosCMAPMatchIndex = _QosCbQosCMAPMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 4, 1, 1),
    _QosCbQosCMAPMatchIndex_Type()
)
qosCbQosCMAPMatchIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosCMAPMatchIndex.setStatus("current")
_QosCbQosCMAPMatchType_Type = QosCMAPMatchType
_QosCbQosCMAPMatchType_Object = MibTableColumn
qosCbQosCMAPMatchType = _QosCbQosCMAPMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 4, 1, 2),
    _QosCbQosCMAPMatchType_Type()
)
qosCbQosCMAPMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosCMAPMatchType.setStatus("current")
_QosCbQosCMAPMatchValue_Type = DisplayString
_QosCbQosCMAPMatchValue_Object = MibTableColumn
qosCbQosCMAPMatchValue = _QosCbQosCMAPMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 4, 1, 3),
    _QosCbQosCMAPMatchValue_Type()
)
qosCbQosCMAPMatchValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosCMAPMatchValue.setStatus("current")
_QosCbQosCMAPMatchRowStatus_Type = EntryStatus
_QosCbQosCMAPMatchRowStatus_Object = MibTableColumn
qosCbQosCMAPMatchRowStatus = _QosCbQosCMAPMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 4, 1, 4),
    _QosCbQosCMAPMatchRowStatus_Type()
)
qosCbQosCMAPMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosCMAPMatchRowStatus.setStatus("current")
_QosCbQosPolicyClassCfgTable_Object = MibTable
qosCbQosPolicyClassCfgTable = _QosCbQosPolicyClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 5)
)
if mibBuilder.loadTexts:
    qosCbQosPolicyClassCfgTable.setStatus("current")
_QosCbQosPolicyClassCfgEntry_Object = MibTableRow
qosCbQosPolicyClassCfgEntry = _QosCbQosPolicyClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 5, 1)
)
qosCbQosPolicyClassCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosPMapIndex"),
    (0, "ZXR10-QOS-MIB", "qoscbQosCMapIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosPolicyClassCfgEntry.setStatus("current")
_QosCbQosPolicyClassName_Type = DisplayString
_QosCbQosPolicyClassName_Object = MibTableColumn
qosCbQosPolicyClassName = _QosCbQosPolicyClassName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 5, 1, 1),
    _QosCbQosPolicyClassName_Type()
)
qosCbQosPolicyClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPolicyClassName.setStatus("current")
_QosCbQosPolicyClassRowStatus_Type = EntryStatus
_QosCbQosPolicyClassRowStatus_Object = MibTableColumn
qosCbQosPolicyClassRowStatus = _QosCbQosPolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 5, 1, 2),
    _QosCbQosPolicyClassRowStatus_Type()
)
qosCbQosPolicyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPolicyClassRowStatus.setStatus("current")
_QosCbQosqueueCfgTable_Object = MibTable
qosCbQosqueueCfgTable = _QosCbQosqueueCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 6)
)
if mibBuilder.loadTexts:
    qosCbQosqueueCfgTable.setStatus("current")
_QosCbQosqueueCfgEntry_Object = MibTableRow
qosCbQosqueueCfgEntry = _QosCbQosqueueCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 6, 1)
)
qosCbQosqueueCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosPMapIndex"),
    (0, "ZXR10-QOS-MIB", "qoscbQosCMapIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosqueueCfgEntry.setStatus("current")
_QosCbQosQueueingCfgPriorityQueueNo_Type = QosPQQueueType
_QosCbQosQueueingCfgPriorityQueueNo_Object = MibTableColumn
qosCbQosQueueingCfgPriorityQueueNo = _QosCbQosQueueingCfgPriorityQueueNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 6, 1, 1),
    _QosCbQosQueueingCfgPriorityQueueNo_Type()
)
qosCbQosQueueingCfgPriorityQueueNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosQueueingCfgPriorityQueueNo.setStatus("current")
_QosCbQosqueueRowStatus_Type = EntryStatus
_QosCbQosqueueRowStatus_Object = MibTableColumn
qosCbQosqueueRowStatus = _QosCbQosqueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 6, 1, 2),
    _QosCbQosqueueRowStatus_Type()
)
qosCbQosqueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosqueueRowStatus.setStatus("current")
_QosCbQosbandwidthCfgTable_Object = MibTable
qosCbQosbandwidthCfgTable = _QosCbQosbandwidthCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 7)
)
if mibBuilder.loadTexts:
    qosCbQosbandwidthCfgTable.setStatus("current")
_QosCbQosbindwidthCfgEntry_Object = MibTableRow
qosCbQosbindwidthCfgEntry = _QosCbQosbindwidthCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 7, 1)
)
qosCbQosbindwidthCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosPMapIndex"),
    (0, "ZXR10-QOS-MIB", "qoscbQosCMapIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosbindwidthCfgEntry.setStatus("current")
_QosCbQosQueueingCfgBandwidth_Type = Integer32
_QosCbQosQueueingCfgBandwidth_Object = MibTableColumn
qosCbQosQueueingCfgBandwidth = _QosCbQosQueueingCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 7, 1, 1),
    _QosCbQosQueueingCfgBandwidth_Type()
)
qosCbQosQueueingCfgBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosQueueingCfgBandwidth.setStatus("current")
_QosCbQosQueueingCfgBandwidthUnits_Type = QueueingBandwidthUnits
_QosCbQosQueueingCfgBandwidthUnits_Object = MibTableColumn
qosCbQosQueueingCfgBandwidthUnits = _QosCbQosQueueingCfgBandwidthUnits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 7, 1, 2),
    _QosCbQosQueueingCfgBandwidthUnits_Type()
)
qosCbQosQueueingCfgBandwidthUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosQueueingCfgBandwidthUnits.setStatus("current")
_QosCbQosActionRowStatus_Type = EntryStatus
_QosCbQosActionRowStatus_Object = MibTableColumn
qosCbQosActionRowStatus = _QosCbQosActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 7, 1, 3),
    _QosCbQosActionRowStatus_Type()
)
qosCbQosActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosActionRowStatus.setStatus("current")
_QosCbQosPoliceCfgTable_Object = MibTable
qosCbQosPoliceCfgTable = _QosCbQosPoliceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8)
)
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgTable.setStatus("current")
_QosCbQosPoliceCfgEntry_Object = MibTableRow
qosCbQosPoliceCfgEntry = _QosCbQosPoliceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1)
)
qosCbQosPoliceCfgEntry.setIndexNames(
    (0, "ZXR10-QOS-MIB", "qoscbQosPMapIndex"),
    (0, "ZXR10-QOS-MIB", "qoscbQosCMapIndex"),
)
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgEntry.setStatus("current")


class _QosCbQosPoliceCfgCir_Type(Integer32):
    """Custom type qosCbQosPoliceCfgCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2000000),
    )


_QosCbQosPoliceCfgCir_Type.__name__ = "Integer32"
_QosCbQosPoliceCfgCir_Object = MibTableColumn
qosCbQosPoliceCfgCir = _QosCbQosPoliceCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 1),
    _QosCbQosPoliceCfgCir_Type()
)
qosCbQosPoliceCfgCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgCir.setStatus("current")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgCir.setUnits("Kilobits/second")


class _QosCbQosPoliceCfgBurstSize_Type(Integer32):
    """Custom type qosCbQosPoliceCfgBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 512000000),
    )


_QosCbQosPoliceCfgBurstSize_Type.__name__ = "Integer32"
_QosCbQosPoliceCfgBurstSize_Object = MibTableColumn
qosCbQosPoliceCfgBurstSize = _QosCbQosPoliceCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 2),
    _QosCbQosPoliceCfgBurstSize_Type()
)
qosCbQosPoliceCfgBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgBurstSize.setUnits("bytes")


class _QosCbQosPoliceCfgPir_Type(Integer32):
    """Custom type qosCbQosPoliceCfgPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2000000),
    )


_QosCbQosPoliceCfgPir_Type.__name__ = "Integer32"
_QosCbQosPoliceCfgPir_Object = MibTableColumn
qosCbQosPoliceCfgPir = _QosCbQosPoliceCfgPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 3),
    _QosCbQosPoliceCfgPir_Type()
)
qosCbQosPoliceCfgPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgPir.setStatus("current")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgPir.setUnits("Kilobits/second")


class _QosCbQosPoliceCfgExtBurstSize_Type(Integer32):
    """Custom type qosCbQosPoliceCfgExtBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 512000000),
    )


_QosCbQosPoliceCfgExtBurstSize_Type.__name__ = "Integer32"
_QosCbQosPoliceCfgExtBurstSize_Object = MibTableColumn
qosCbQosPoliceCfgExtBurstSize = _QosCbQosPoliceCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 4),
    _QosCbQosPoliceCfgExtBurstSize_Type()
)
qosCbQosPoliceCfgExtBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgExtBurstSize.setUnits("bytes")
_QosCbQosPoliceCfgConformAction_Type = QosCBQCarAction
_QosCbQosPoliceCfgConformAction_Object = MibTableColumn
qosCbQosPoliceCfgConformAction = _QosCbQosPoliceCfgConformAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 5),
    _QosCbQosPoliceCfgConformAction_Type()
)
qosCbQosPoliceCfgConformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgConformAction.setStatus("current")
_QosCbQosPoliceCfgConformSetValue_Type = Gauge32
_QosCbQosPoliceCfgConformSetValue_Object = MibTableColumn
qosCbQosPoliceCfgConformSetValue = _QosCbQosPoliceCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 6),
    _QosCbQosPoliceCfgConformSetValue_Type()
)
qosCbQosPoliceCfgConformSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgConformSetValue.setStatus("current")
_QosCbQosPoliceCfgExceedAction_Type = QosCBQCarAction
_QosCbQosPoliceCfgExceedAction_Object = MibTableColumn
qosCbQosPoliceCfgExceedAction = _QosCbQosPoliceCfgExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 7),
    _QosCbQosPoliceCfgExceedAction_Type()
)
qosCbQosPoliceCfgExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgExceedAction.setStatus("current")
_QosCbQosPoliceCfgExceedSetValue_Type = Gauge32
_QosCbQosPoliceCfgExceedSetValue_Object = MibTableColumn
qosCbQosPoliceCfgExceedSetValue = _QosCbQosPoliceCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 8),
    _QosCbQosPoliceCfgExceedSetValue_Type()
)
qosCbQosPoliceCfgExceedSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgExceedSetValue.setStatus("current")
_QosCbQosPoliceCfgViolateAction_Type = QosCBQCarAction
_QosCbQosPoliceCfgViolateAction_Object = MibTableColumn
qosCbQosPoliceCfgViolateAction = _QosCbQosPoliceCfgViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 9),
    _QosCbQosPoliceCfgViolateAction_Type()
)
qosCbQosPoliceCfgViolateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgViolateAction.setStatus("current")
_QosCbQosPoliceCfgViolateSetValue_Type = Gauge32
_QosCbQosPoliceCfgViolateSetValue_Object = MibTableColumn
qosCbQosPoliceCfgViolateSetValue = _QosCbQosPoliceCfgViolateSetValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 10),
    _QosCbQosPoliceCfgViolateSetValue_Type()
)
qosCbQosPoliceCfgViolateSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgViolateSetValue.setStatus("current")
_QosCbQosPoliceCfgRowStatus_Type = EntryStatus
_QosCbQosPoliceCfgRowStatus_Object = MibTableColumn
qosCbQosPoliceCfgRowStatus = _QosCbQosPoliceCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 4, 8, 1, 11),
    _QosCbQosPoliceCfgRowStatus_Type()
)
qosCbQosPoliceCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCbQosPoliceCfgRowStatus.setStatus("current")
_QosWREDconfig_ObjectIdentity = ObjectIdentity
qosWREDconfig = _QosWREDconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5)
)
_QosWREDprecedenceCfgTable_Object = MibTable
qosWREDprecedenceCfgTable = _QosWREDprecedenceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1)
)
if mibBuilder.loadTexts:
    qosWREDprecedenceCfgTable.setStatus("current")
_QosWREDprecedenceCfgEntry_Object = MibTableRow
qosWREDprecedenceCfgEntry = _QosWREDprecedenceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1, 1)
)
qosWREDprecedenceCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-QOS-MIB", "qosREDCfgPreValue"),
)
if mibBuilder.loadTexts:
    qosWREDprecedenceCfgEntry.setStatus("current")
_QosREDCfgPreValue_Type = Integer32
_QosREDCfgPreValue_Object = MibTableColumn
qosREDCfgPreValue = _QosREDCfgPreValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1, 1, 1),
    _QosREDCfgPreValue_Type()
)
qosREDCfgPreValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDCfgPreValue.setStatus("current")
_QosREDprecedenceCfgMinThreshold_Type = Integer32
_QosREDprecedenceCfgMinThreshold_Object = MibTableColumn
qosREDprecedenceCfgMinThreshold = _QosREDprecedenceCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1, 1, 2),
    _QosREDprecedenceCfgMinThreshold_Type()
)
qosREDprecedenceCfgMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDprecedenceCfgMinThreshold.setStatus("current")
_QosREDprecedenceCfgMaxThreshold_Type = Integer32
_QosREDprecedenceCfgMaxThreshold_Object = MibTableColumn
qosREDprecedenceCfgMaxThreshold = _QosREDprecedenceCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1, 1, 3),
    _QosREDprecedenceCfgMaxThreshold_Type()
)
qosREDprecedenceCfgMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDprecedenceCfgMaxThreshold.setStatus("current")
_QosREDprecedenceCfgPktDropProb_Type = Integer32
_QosREDprecedenceCfgPktDropProb_Object = MibTableColumn
qosREDprecedenceCfgPktDropProb = _QosREDprecedenceCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1, 1, 4),
    _QosREDprecedenceCfgPktDropProb_Type()
)
qosREDprecedenceCfgPktDropProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDprecedenceCfgPktDropProb.setStatus("current")
_QosREDCfgprecedenceRowStatus_Type = EntryStatus
_QosREDCfgprecedenceRowStatus_Object = MibTableColumn
qosREDCfgprecedenceRowStatus = _QosREDCfgprecedenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 1, 1, 5),
    _QosREDCfgprecedenceRowStatus_Type()
)
qosREDCfgprecedenceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDCfgprecedenceRowStatus.setStatus("current")
_QosWREDweightCfgTable_Object = MibTable
qosWREDweightCfgTable = _QosWREDweightCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 2)
)
if mibBuilder.loadTexts:
    qosWREDweightCfgTable.setStatus("current")
_QosWREDweightCfgEntry_Object = MibTableRow
qosWREDweightCfgEntry = _QosWREDweightCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 2, 1)
)
qosWREDweightCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosWREDweightCfgEntry.setStatus("current")
_QosREDCfgweightValue_Type = Integer32
_QosREDCfgweightValue_Object = MibTableColumn
qosREDCfgweightValue = _QosREDCfgweightValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 2, 1, 1),
    _QosREDCfgweightValue_Type()
)
qosREDCfgweightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDCfgweightValue.setStatus("current")
_QosREDCfgweightRowStatus_Type = EntryStatus
_QosREDCfgweightRowStatus_Object = MibTableColumn
qosREDCfgweightRowStatus = _QosREDCfgweightRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 5, 2, 1, 2),
    _QosREDCfgweightRowStatus_Type()
)
qosREDCfgweightRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosREDCfgweightRowStatus.setStatus("current")
_QosWFQconfig_ObjectIdentity = ObjectIdentity
qosWFQconfig = _QosWFQconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 6)
)
_QosWFQCfgTable_Object = MibTable
qosWFQCfgTable = _QosWFQCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 6, 1)
)
if mibBuilder.loadTexts:
    qosWFQCfgTable.setStatus("current")
_QosWFQCfgEntry_Object = MibTableRow
qosWFQCfgEntry = _QosWFQCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 6, 1, 1)
)
qosWFQCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosWFQCfgEntry.setStatus("current")
_QosWFQCfgTotalQueueNum_Type = Integer32
_QosWFQCfgTotalQueueNum_Object = MibTableColumn
qosWFQCfgTotalQueueNum = _QosWFQCfgTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 6, 1, 1, 1),
    _QosWFQCfgTotalQueueNum_Type()
)
qosWFQCfgTotalQueueNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWFQCfgTotalQueueNum.setStatus("current")
_QosWFQCfgQueueLimit_Type = Integer32
_QosWFQCfgQueueLimit_Object = MibTableColumn
qosWFQCfgQueueLimit = _QosWFQCfgQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 6, 1, 1, 2),
    _QosWFQCfgQueueLimit_Type()
)
qosWFQCfgQueueLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWFQCfgQueueLimit.setStatus("current")
_QosWFQCfgRowStatus_Type = EntryStatus
_QosWFQCfgRowStatus_Object = MibTableColumn
qosWFQCfgRowStatus = _QosWFQCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 6, 1, 1, 3),
    _QosWFQCfgRowStatus_Type()
)
qosWFQCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosWFQCfgRowStatus.setStatus("current")
_QosCARconfig_ObjectIdentity = ObjectIdentity
qosCARconfig = _QosCARconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7)
)
_QosFreeCirIndex_Type = Integer32
_QosFreeCirIndex_Object = MibScalar
qosFreeCirIndex = _QosFreeCirIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 1),
    _QosFreeCirIndex_Type()
)
qosFreeCirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosFreeCirIndex.setStatus("current")
_QosInputCirIfTable_Object = MibTable
qosInputCirIfTable = _QosInputCirIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2)
)
if mibBuilder.loadTexts:
    qosInputCirIfTable.setStatus("current")
_QosInputCirIfEntry_Object = MibTableRow
qosInputCirIfEntry = _QosInputCirIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1)
)
qosInputCirIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-QOS-MIB", "qosInputCirIndex"),
)
if mibBuilder.loadTexts:
    qosInputCirIfEntry.setStatus("current")
_QosInputCirIndex_Type = Integer32
_QosInputCirIndex_Object = MibTableColumn
qosInputCirIndex = _QosInputCirIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 1),
    _QosInputCirIndex_Type()
)
qosInputCirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosInputCirIndex.setStatus("current")
_QosInputCirMatchType_Type = QosCirMatchType
_QosInputCirMatchType_Object = MibTableColumn
qosInputCirMatchType = _QosInputCirMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 2),
    _QosInputCirMatchType_Type()
)
qosInputCirMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirMatchType.setStatus("current")
_QosInputCirMatchValue_Type = DisplayString
_QosInputCirMatchValue_Object = MibTableColumn
qosInputCirMatchValue = _QosInputCirMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 3),
    _QosInputCirMatchValue_Type()
)
qosInputCirMatchValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirMatchValue.setStatus("current")


class _QosInputCirCir_Type(Gauge32):
    """Custom type qosInputCirCir based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2000000),
    )


_QosInputCirCir_Type.__name__ = "Gauge32"
_QosInputCirCir_Object = MibTableColumn
qosInputCirCir = _QosInputCirCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 4),
    _QosInputCirCir_Type()
)
qosInputCirCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirCir.setStatus("current")


class _QosInputCirNormalBurstRate_Type(Gauge32):
    """Custom type qosInputCirNormalBurstRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 512000000),
    )


_QosInputCirNormalBurstRate_Type.__name__ = "Gauge32"
_QosInputCirNormalBurstRate_Object = MibTableColumn
qosInputCirNormalBurstRate = _QosInputCirNormalBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 5),
    _QosInputCirNormalBurstRate_Type()
)
qosInputCirNormalBurstRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirNormalBurstRate.setStatus("current")


class _QosInputCirPir_Type(Gauge32):
    """Custom type qosInputCirPir based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2000000),
    )


_QosInputCirPir_Type.__name__ = "Gauge32"
_QosInputCirPir_Object = MibTableColumn
qosInputCirPir = _QosInputCirPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 6),
    _QosInputCirPir_Type()
)
qosInputCirPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirPir.setStatus("current")


class _QosInputCirMaxBurstRate_Type(Gauge32):
    """Custom type qosInputCirMaxBurstRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 512000000),
    )


_QosInputCirMaxBurstRate_Type.__name__ = "Gauge32"
_QosInputCirMaxBurstRate_Object = MibTableColumn
qosInputCirMaxBurstRate = _QosInputCirMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 7),
    _QosInputCirMaxBurstRate_Type()
)
qosInputCirMaxBurstRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirMaxBurstRate.setStatus("current")
_QosInputCirConformAction_Type = QosCirAction
_QosInputCirConformAction_Object = MibTableColumn
qosInputCirConformAction = _QosInputCirConformAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 8),
    _QosInputCirConformAction_Type()
)
qosInputCirConformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirConformAction.setStatus("current")
_QosInputCirConformValue_Type = Gauge32
_QosInputCirConformValue_Object = MibTableColumn
qosInputCirConformValue = _QosInputCirConformValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 9),
    _QosInputCirConformValue_Type()
)
qosInputCirConformValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirConformValue.setStatus("current")
_QosInputCirExceedAction_Type = QosCirAction
_QosInputCirExceedAction_Object = MibTableColumn
qosInputCirExceedAction = _QosInputCirExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 10),
    _QosInputCirExceedAction_Type()
)
qosInputCirExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirExceedAction.setStatus("current")
_QosInputCirExceedValue_Type = Gauge32
_QosInputCirExceedValue_Object = MibTableColumn
qosInputCirExceedValue = _QosInputCirExceedValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 11),
    _QosInputCirExceedValue_Type()
)
qosInputCirExceedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirExceedValue.setStatus("current")
_QosInputCirViolateAction_Type = QosCirAction
_QosInputCirViolateAction_Object = MibTableColumn
qosInputCirViolateAction = _QosInputCirViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 12),
    _QosInputCirViolateAction_Type()
)
qosInputCirViolateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirViolateAction.setStatus("current")
_QosInputCirViolateValue_Type = Gauge32
_QosInputCirViolateValue_Object = MibTableColumn
qosInputCirViolateValue = _QosInputCirViolateValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 13),
    _QosInputCirViolateValue_Type()
)
qosInputCirViolateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirViolateValue.setStatus("current")
_QosInputCirRowStatus_Type = EntryStatus
_QosInputCirRowStatus_Object = MibTableColumn
qosInputCirRowStatus = _QosInputCirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 14),
    _QosInputCirRowStatus_Type()
)
qosInputCirRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirRowStatus.setStatus("current")
_QosInputCirDescription_Type = DisplayString
_QosInputCirDescription_Object = MibTableColumn
qosInputCirDescription = _QosInputCirDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 2, 1, 15),
    _QosInputCirDescription_Type()
)
qosInputCirDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInputCirDescription.setStatus("current")
_QosInputCirIfTableLastchange_Type = TimeTicks
_QosInputCirIfTableLastchange_Object = MibScalar
qosInputCirIfTableLastchange = _QosInputCirIfTableLastchange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 3),
    _QosInputCirIfTableLastchange_Type()
)
qosInputCirIfTableLastchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosInputCirIfTableLastchange.setStatus("current")
_QosOutputCirIfTable_Object = MibTable
qosOutputCirIfTable = _QosOutputCirIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4)
)
if mibBuilder.loadTexts:
    qosOutputCirIfTable.setStatus("current")
_QosOutputCirIfEntry_Object = MibTableRow
qosOutputCirIfEntry = _QosOutputCirIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1)
)
qosOutputCirIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-QOS-MIB", "qosOutputCirIndex"),
)
if mibBuilder.loadTexts:
    qosOutputCirIfEntry.setStatus("current")
_QosOutputCirIndex_Type = Integer32
_QosOutputCirIndex_Object = MibTableColumn
qosOutputCirIndex = _QosOutputCirIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 1),
    _QosOutputCirIndex_Type()
)
qosOutputCirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosOutputCirIndex.setStatus("current")
_QosOutputCirMatchType_Type = QosCirMatchType
_QosOutputCirMatchType_Object = MibTableColumn
qosOutputCirMatchType = _QosOutputCirMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 2),
    _QosOutputCirMatchType_Type()
)
qosOutputCirMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirMatchType.setStatus("current")
_QosOutputCirMatchValue_Type = DisplayString
_QosOutputCirMatchValue_Object = MibTableColumn
qosOutputCirMatchValue = _QosOutputCirMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 3),
    _QosOutputCirMatchValue_Type()
)
qosOutputCirMatchValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirMatchValue.setStatus("current")


class _QosOutputCirCir_Type(Gauge32):
    """Custom type qosOutputCirCir based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2000000),
    )


_QosOutputCirCir_Type.__name__ = "Gauge32"
_QosOutputCirCir_Object = MibTableColumn
qosOutputCirCir = _QosOutputCirCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 4),
    _QosOutputCirCir_Type()
)
qosOutputCirCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirCir.setStatus("current")


class _QosOutputCirNormalBurstRate_Type(Gauge32):
    """Custom type qosOutputCirNormalBurstRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 512000000),
    )


_QosOutputCirNormalBurstRate_Type.__name__ = "Gauge32"
_QosOutputCirNormalBurstRate_Object = MibTableColumn
qosOutputCirNormalBurstRate = _QosOutputCirNormalBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 5),
    _QosOutputCirNormalBurstRate_Type()
)
qosOutputCirNormalBurstRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirNormalBurstRate.setStatus("current")


class _QosOutputCirPir_Type(Gauge32):
    """Custom type qosOutputCirPir based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2000000),
    )


_QosOutputCirPir_Type.__name__ = "Gauge32"
_QosOutputCirPir_Object = MibTableColumn
qosOutputCirPir = _QosOutputCirPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 6),
    _QosOutputCirPir_Type()
)
qosOutputCirPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirPir.setStatus("current")


class _QosOutputCirMaxBurstRate_Type(Gauge32):
    """Custom type qosOutputCirMaxBurstRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 512000000),
    )


_QosOutputCirMaxBurstRate_Type.__name__ = "Gauge32"
_QosOutputCirMaxBurstRate_Object = MibTableColumn
qosOutputCirMaxBurstRate = _QosOutputCirMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 7),
    _QosOutputCirMaxBurstRate_Type()
)
qosOutputCirMaxBurstRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirMaxBurstRate.setStatus("current")
_QosOutputCirConformAction_Type = QosCirAction
_QosOutputCirConformAction_Object = MibTableColumn
qosOutputCirConformAction = _QosOutputCirConformAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 8),
    _QosOutputCirConformAction_Type()
)
qosOutputCirConformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirConformAction.setStatus("current")
_QosOutputCirConformValue_Type = Gauge32
_QosOutputCirConformValue_Object = MibTableColumn
qosOutputCirConformValue = _QosOutputCirConformValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 9),
    _QosOutputCirConformValue_Type()
)
qosOutputCirConformValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirConformValue.setStatus("current")
_QosOutputCirExceedAction_Type = QosCirAction
_QosOutputCirExceedAction_Object = MibTableColumn
qosOutputCirExceedAction = _QosOutputCirExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 10),
    _QosOutputCirExceedAction_Type()
)
qosOutputCirExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirExceedAction.setStatus("current")
_QosOutputCirExceedValue_Type = Gauge32
_QosOutputCirExceedValue_Object = MibTableColumn
qosOutputCirExceedValue = _QosOutputCirExceedValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 11),
    _QosOutputCirExceedValue_Type()
)
qosOutputCirExceedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirExceedValue.setStatus("current")
_QosOutputCirViolateAction_Type = QosCirAction
_QosOutputCirViolateAction_Object = MibTableColumn
qosOutputCirViolateAction = _QosOutputCirViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 12),
    _QosOutputCirViolateAction_Type()
)
qosOutputCirViolateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirViolateAction.setStatus("current")
_QosOutputCirViolateValue_Type = Gauge32
_QosOutputCirViolateValue_Object = MibTableColumn
qosOutputCirViolateValue = _QosOutputCirViolateValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 13),
    _QosOutputCirViolateValue_Type()
)
qosOutputCirViolateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirViolateValue.setStatus("current")
_QosOutputCirRowStatus_Type = EntryStatus
_QosOutputCirRowStatus_Object = MibTableColumn
qosOutputCirRowStatus = _QosOutputCirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 14),
    _QosOutputCirRowStatus_Type()
)
qosOutputCirRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirRowStatus.setStatus("current")
_QosOutputCirDescription_Type = DisplayString
_QosOutputCirDescription_Object = MibTableColumn
qosOutputCirDescription = _QosOutputCirDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 4, 1, 15),
    _QosOutputCirDescription_Type()
)
qosOutputCirDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosOutputCirDescription.setStatus("current")
_QosOutputCirIfTableLastchange_Type = TimeTicks
_QosOutputCirIfTableLastchange_Object = MibScalar
qosOutputCirIfTableLastchange = _QosOutputCirIfTableLastchange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 7, 5),
    _QosOutputCirIfTableLastchange_Type()
)
qosOutputCirIfTableLastchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosOutputCirIfTableLastchange.setStatus("current")
_QosIntfCarStat_ObjectIdentity = ObjectIdentity
qosIntfCarStat = _QosIntfCarStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8)
)
_QosIfTraffStatInfoTable_Object = MibTable
qosIfTraffStatInfoTable = _QosIfTraffStatInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1)
)
if mibBuilder.loadTexts:
    qosIfTraffStatInfoTable.setStatus("current")
_QosIfTraffStatInfoEntry_Object = MibTableRow
qosIfTraffStatInfoEntry = _QosIfTraffStatInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1)
)
qosIfTraffStatInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosIfTraffStatInfoEntry.setStatus("current")
_QosIntfName_Type = DisplayString
_QosIntfName_Object = MibTableColumn
qosIntfName = _QosIntfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 1),
    _QosIntfName_Type()
)
qosIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfName.setStatus("current")
_QosIntfInUtilization_Type = DisplayString
_QosIntfInUtilization_Object = MibTableColumn
qosIntfInUtilization = _QosIntfInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 2),
    _QosIntfInUtilization_Type()
)
qosIntfInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInUtilization.setStatus("current")
_QosIntfInCarTotalPackets_Type = DisplayString
_QosIntfInCarTotalPackets_Object = MibTableColumn
qosIntfInCarTotalPackets = _QosIntfInCarTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 3),
    _QosIntfInCarTotalPackets_Type()
)
qosIntfInCarTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInCarTotalPackets.setStatus("current")
_QosIntfInCarTranPackets_Type = DisplayString
_QosIntfInCarTranPackets_Object = MibTableColumn
qosIntfInCarTranPackets = _QosIntfInCarTranPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 4),
    _QosIntfInCarTranPackets_Type()
)
qosIntfInCarTranPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInCarTranPackets.setStatus("current")
_QosIntfInCarDropPackets_Type = DisplayString
_QosIntfInCarDropPackets_Object = MibTableColumn
qosIntfInCarDropPackets = _QosIntfInCarDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 5),
    _QosIntfInCarDropPackets_Type()
)
qosIntfInCarDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInCarDropPackets.setStatus("current")
_QosIntfInCarTotalBytes_Type = DisplayString
_QosIntfInCarTotalBytes_Object = MibTableColumn
qosIntfInCarTotalBytes = _QosIntfInCarTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 6),
    _QosIntfInCarTotalBytes_Type()
)
qosIntfInCarTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInCarTotalBytes.setStatus("current")
_QosIntfInCarTranBytes_Type = DisplayString
_QosIntfInCarTranBytes_Object = MibTableColumn
qosIntfInCarTranBytes = _QosIntfInCarTranBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 7),
    _QosIntfInCarTranBytes_Type()
)
qosIntfInCarTranBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInCarTranBytes.setStatus("current")
_QosIntfInCarDropBytes_Type = DisplayString
_QosIntfInCarDropBytes_Object = MibTableColumn
qosIntfInCarDropBytes = _QosIntfInCarDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 8),
    _QosIntfInCarDropBytes_Type()
)
qosIntfInCarDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfInCarDropBytes.setStatus("current")
_QosIntfOutUtilization_Type = DisplayString
_QosIntfOutUtilization_Object = MibTableColumn
qosIntfOutUtilization = _QosIntfOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 9),
    _QosIntfOutUtilization_Type()
)
qosIntfOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutUtilization.setStatus("current")
_QosIntfOutCarTotalPackets_Type = DisplayString
_QosIntfOutCarTotalPackets_Object = MibTableColumn
qosIntfOutCarTotalPackets = _QosIntfOutCarTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 10),
    _QosIntfOutCarTotalPackets_Type()
)
qosIntfOutCarTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutCarTotalPackets.setStatus("current")
_QosIntfOutCarTranPackets_Type = DisplayString
_QosIntfOutCarTranPackets_Object = MibTableColumn
qosIntfOutCarTranPackets = _QosIntfOutCarTranPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 11),
    _QosIntfOutCarTranPackets_Type()
)
qosIntfOutCarTranPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutCarTranPackets.setStatus("current")
_QosIntfOutCarDropPackets_Type = DisplayString
_QosIntfOutCarDropPackets_Object = MibTableColumn
qosIntfOutCarDropPackets = _QosIntfOutCarDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 12),
    _QosIntfOutCarDropPackets_Type()
)
qosIntfOutCarDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutCarDropPackets.setStatus("current")
_QosIntfOutCarTotalBytes_Type = DisplayString
_QosIntfOutCarTotalBytes_Object = MibTableColumn
qosIntfOutCarTotalBytes = _QosIntfOutCarTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 13),
    _QosIntfOutCarTotalBytes_Type()
)
qosIntfOutCarTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutCarTotalBytes.setStatus("current")
_QosIntfOutCarTranBytes_Type = DisplayString
_QosIntfOutCarTranBytes_Object = MibTableColumn
qosIntfOutCarTranBytes = _QosIntfOutCarTranBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 14),
    _QosIntfOutCarTranBytes_Type()
)
qosIntfOutCarTranBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutCarTranBytes.setStatus("current")
_QosIntfOutCarDropBytes_Type = DisplayString
_QosIntfOutCarDropBytes_Object = MibTableColumn
qosIntfOutCarDropBytes = _QosIntfOutCarDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 6, 8, 1, 1, 15),
    _QosIntfOutCarDropBytes_Type()
)
qosIntfOutCarDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIntfOutCarDropBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-QOS-MIB",
    **{"DisplayString": DisplayString,
       "QosCirMatchType": QosCirMatchType,
       "QosCirAction": QosCirAction,
       "QosCBQCarAction": QosCBQCarAction,
       "QosPQMatchType": QosPQMatchType,
       "QosPQQueueType": QosPQQueueType,
       "QosCMAPMatchType": QosCMAPMatchType,
       "TrafficDirection": TrafficDirection,
       "QueueingBandwidthUnits": QueueingBandwidthUnits,
       "EntryStatus": EntryStatus,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10protocol": zxr10protocol,
       "zxr10qos": zxr10qos,
       "qosModuleStart": qosModuleStart,
       "qosPQconfig": qosPQconfig,
       "qosPriorityQueueCfgTable": qosPriorityQueueCfgTable,
       "qosPriorityQueueCfgEntry": qosPriorityQueueCfgEntry,
       "qosPriorityQueueIndex": qosPriorityQueueIndex,
       "qosPriorityQueueItemTotal": qosPriorityQueueItemTotal,
       "qosPriorityQueueDefault": qosPriorityQueueDefault,
       "qosPriorityQueueLimitHigh": qosPriorityQueueLimitHigh,
       "qosPriorityQueueLimitMedium": qosPriorityQueueLimitMedium,
       "qosPriorityQueueLimitNormal": qosPriorityQueueLimitNormal,
       "qosPriorityQueueLimitLow": qosPriorityQueueLimitLow,
       "qosPriorityQueueRowStatus": qosPriorityQueueRowStatus,
       "qosPriorityQueueCfgTableLastchange": qosPriorityQueueCfgTableLastchange,
       "qosPriorityQueueItemTable": qosPriorityQueueItemTable,
       "qosPriorityQueueItemEntry": qosPriorityQueueItemEntry,
       "qosPriorityQueueItemIndex": qosPriorityQueueItemIndex,
       "qosPriorityQueueItemMatchType": qosPriorityQueueItemMatchType,
       "qosPriorityQueueItemMatchValue": qosPriorityQueueItemMatchValue,
       "qosPriorityQueueItemQueueNum": qosPriorityQueueItemQueueNum,
       "qosPriorityQueueItemRowStatus": qosPriorityQueueItemRowStatus,
       "qosPriorityQueueItemDescription": qosPriorityQueueItemDescription,
       "qosPriorityGroupTable": qosPriorityGroupTable,
       "qosPriorityGroupEntry": qosPriorityGroupEntry,
       "qosPriorityGroupifname": qosPriorityGroupifname,
       "qosPriorityGroupNum": qosPriorityGroupNum,
       "qosPriorityGroupRowStatus": qosPriorityGroupRowStatus,
       "qosCQconfig": qosCQconfig,
       "qosCBQconfig": qosCBQconfig,
       "qosCBQosServicePolicyTable": qosCBQosServicePolicyTable,
       "qosCBQosServicePolicyEntry": qosCBQosServicePolicyEntry,
       "qosCbQosPolicyifname": qosCbQosPolicyifname,
       "qosCbQosPolicyDirection": qosCbQosPolicyDirection,
       "qosCbQosServicePolicyName": qosCbQosServicePolicyName,
       "qosCbQosServicePolicyRowStatus": qosCbQosServicePolicyRowStatus,
       "qosCbQosPolicyMapCfgTable": qosCbQosPolicyMapCfgTable,
       "qosCbQosPolicyMapCfgEntry": qosCbQosPolicyMapCfgEntry,
       "qoscbQosPMapIndex": qoscbQosPMapIndex,
       "qoscbQosPolicyMapName": qoscbQosPolicyMapName,
       "qosCbQosPolicyMapRowStatus": qosCbQosPolicyMapRowStatus,
       "qoscbQosPolicyMapDescription": qoscbQosPolicyMapDescription,
       "qosCbQosClassMapCfgTable": qosCbQosClassMapCfgTable,
       "qosCbQosClassMapCfgEntry": qosCbQosClassMapCfgEntry,
       "qoscbQosCMapIndex": qoscbQosCMapIndex,
       "qosCbQosClassMapName": qosCbQosClassMapName,
       "qosCbQosClassMapRowStatus": qosCbQosClassMapRowStatus,
       "qoscbQosClassMapDescription": qoscbQosClassMapDescription,
       "qosCbQosCMAPMatchCfgTable": qosCbQosCMAPMatchCfgTable,
       "qosCbQosCMAPMatchCfgEntry": qosCbQosCMAPMatchCfgEntry,
       "qosCbQosCMAPMatchIndex": qosCbQosCMAPMatchIndex,
       "qosCbQosCMAPMatchType": qosCbQosCMAPMatchType,
       "qosCbQosCMAPMatchValue": qosCbQosCMAPMatchValue,
       "qosCbQosCMAPMatchRowStatus": qosCbQosCMAPMatchRowStatus,
       "qosCbQosPolicyClassCfgTable": qosCbQosPolicyClassCfgTable,
       "qosCbQosPolicyClassCfgEntry": qosCbQosPolicyClassCfgEntry,
       "qosCbQosPolicyClassName": qosCbQosPolicyClassName,
       "qosCbQosPolicyClassRowStatus": qosCbQosPolicyClassRowStatus,
       "qosCbQosqueueCfgTable": qosCbQosqueueCfgTable,
       "qosCbQosqueueCfgEntry": qosCbQosqueueCfgEntry,
       "qosCbQosQueueingCfgPriorityQueueNo": qosCbQosQueueingCfgPriorityQueueNo,
       "qosCbQosqueueRowStatus": qosCbQosqueueRowStatus,
       "qosCbQosbandwidthCfgTable": qosCbQosbandwidthCfgTable,
       "qosCbQosbindwidthCfgEntry": qosCbQosbindwidthCfgEntry,
       "qosCbQosQueueingCfgBandwidth": qosCbQosQueueingCfgBandwidth,
       "qosCbQosQueueingCfgBandwidthUnits": qosCbQosQueueingCfgBandwidthUnits,
       "qosCbQosActionRowStatus": qosCbQosActionRowStatus,
       "qosCbQosPoliceCfgTable": qosCbQosPoliceCfgTable,
       "qosCbQosPoliceCfgEntry": qosCbQosPoliceCfgEntry,
       "qosCbQosPoliceCfgCir": qosCbQosPoliceCfgCir,
       "qosCbQosPoliceCfgBurstSize": qosCbQosPoliceCfgBurstSize,
       "qosCbQosPoliceCfgPir": qosCbQosPoliceCfgPir,
       "qosCbQosPoliceCfgExtBurstSize": qosCbQosPoliceCfgExtBurstSize,
       "qosCbQosPoliceCfgConformAction": qosCbQosPoliceCfgConformAction,
       "qosCbQosPoliceCfgConformSetValue": qosCbQosPoliceCfgConformSetValue,
       "qosCbQosPoliceCfgExceedAction": qosCbQosPoliceCfgExceedAction,
       "qosCbQosPoliceCfgExceedSetValue": qosCbQosPoliceCfgExceedSetValue,
       "qosCbQosPoliceCfgViolateAction": qosCbQosPoliceCfgViolateAction,
       "qosCbQosPoliceCfgViolateSetValue": qosCbQosPoliceCfgViolateSetValue,
       "qosCbQosPoliceCfgRowStatus": qosCbQosPoliceCfgRowStatus,
       "qosWREDconfig": qosWREDconfig,
       "qosWREDprecedenceCfgTable": qosWREDprecedenceCfgTable,
       "qosWREDprecedenceCfgEntry": qosWREDprecedenceCfgEntry,
       "qosREDCfgPreValue": qosREDCfgPreValue,
       "qosREDprecedenceCfgMinThreshold": qosREDprecedenceCfgMinThreshold,
       "qosREDprecedenceCfgMaxThreshold": qosREDprecedenceCfgMaxThreshold,
       "qosREDprecedenceCfgPktDropProb": qosREDprecedenceCfgPktDropProb,
       "qosREDCfgprecedenceRowStatus": qosREDCfgprecedenceRowStatus,
       "qosWREDweightCfgTable": qosWREDweightCfgTable,
       "qosWREDweightCfgEntry": qosWREDweightCfgEntry,
       "qosREDCfgweightValue": qosREDCfgweightValue,
       "qosREDCfgweightRowStatus": qosREDCfgweightRowStatus,
       "qosWFQconfig": qosWFQconfig,
       "qosWFQCfgTable": qosWFQCfgTable,
       "qosWFQCfgEntry": qosWFQCfgEntry,
       "qosWFQCfgTotalQueueNum": qosWFQCfgTotalQueueNum,
       "qosWFQCfgQueueLimit": qosWFQCfgQueueLimit,
       "qosWFQCfgRowStatus": qosWFQCfgRowStatus,
       "qosCARconfig": qosCARconfig,
       "qosFreeCirIndex": qosFreeCirIndex,
       "qosInputCirIfTable": qosInputCirIfTable,
       "qosInputCirIfEntry": qosInputCirIfEntry,
       "qosInputCirIndex": qosInputCirIndex,
       "qosInputCirMatchType": qosInputCirMatchType,
       "qosInputCirMatchValue": qosInputCirMatchValue,
       "qosInputCirCir": qosInputCirCir,
       "qosInputCirNormalBurstRate": qosInputCirNormalBurstRate,
       "qosInputCirPir": qosInputCirPir,
       "qosInputCirMaxBurstRate": qosInputCirMaxBurstRate,
       "qosInputCirConformAction": qosInputCirConformAction,
       "qosInputCirConformValue": qosInputCirConformValue,
       "qosInputCirExceedAction": qosInputCirExceedAction,
       "qosInputCirExceedValue": qosInputCirExceedValue,
       "qosInputCirViolateAction": qosInputCirViolateAction,
       "qosInputCirViolateValue": qosInputCirViolateValue,
       "qosInputCirRowStatus": qosInputCirRowStatus,
       "qosInputCirDescription": qosInputCirDescription,
       "qosInputCirIfTableLastchange": qosInputCirIfTableLastchange,
       "qosOutputCirIfTable": qosOutputCirIfTable,
       "qosOutputCirIfEntry": qosOutputCirIfEntry,
       "qosOutputCirIndex": qosOutputCirIndex,
       "qosOutputCirMatchType": qosOutputCirMatchType,
       "qosOutputCirMatchValue": qosOutputCirMatchValue,
       "qosOutputCirCir": qosOutputCirCir,
       "qosOutputCirNormalBurstRate": qosOutputCirNormalBurstRate,
       "qosOutputCirPir": qosOutputCirPir,
       "qosOutputCirMaxBurstRate": qosOutputCirMaxBurstRate,
       "qosOutputCirConformAction": qosOutputCirConformAction,
       "qosOutputCirConformValue": qosOutputCirConformValue,
       "qosOutputCirExceedAction": qosOutputCirExceedAction,
       "qosOutputCirExceedValue": qosOutputCirExceedValue,
       "qosOutputCirViolateAction": qosOutputCirViolateAction,
       "qosOutputCirViolateValue": qosOutputCirViolateValue,
       "qosOutputCirRowStatus": qosOutputCirRowStatus,
       "qosOutputCirDescription": qosOutputCirDescription,
       "qosOutputCirIfTableLastchange": qosOutputCirIfTableLastchange,
       "qosIntfCarStat": qosIntfCarStat,
       "qosIfTraffStatInfoTable": qosIfTraffStatInfoTable,
       "qosIfTraffStatInfoEntry": qosIfTraffStatInfoEntry,
       "qosIntfName": qosIntfName,
       "qosIntfInUtilization": qosIntfInUtilization,
       "qosIntfInCarTotalPackets": qosIntfInCarTotalPackets,
       "qosIntfInCarTranPackets": qosIntfInCarTranPackets,
       "qosIntfInCarDropPackets": qosIntfInCarDropPackets,
       "qosIntfInCarTotalBytes": qosIntfInCarTotalBytes,
       "qosIntfInCarTranBytes": qosIntfInCarTranBytes,
       "qosIntfInCarDropBytes": qosIntfInCarDropBytes,
       "qosIntfOutUtilization": qosIntfOutUtilization,
       "qosIntfOutCarTotalPackets": qosIntfOutCarTotalPackets,
       "qosIntfOutCarTranPackets": qosIntfOutCarTranPackets,
       "qosIntfOutCarDropPackets": qosIntfOutCarDropPackets,
       "qosIntfOutCarTotalBytes": qosIntfOutCarTotalBytes,
       "qosIntfOutCarTranBytes": qosIntfOutCarTranBytes,
       "qosIntfOutCarDropBytes": qosIntfOutCarDropBytes}
)
