# SNMP MIB module (HUAWEI-CBQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CBQOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:17 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

hwCBQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1)
)
hwCBQoSMIB.setRevisions(
        ("2015-09-01 17:37",
         "2014-02-19 17:37",
         "2013-07-20 16:00",
         "2013-06-04 16:00",
         "2014-02-19 17:37",
         "2015-03-28 18:08",
         "2015-09-17 18:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MatchRuleType(Integer32, TextualConvention):
    status = "current"
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("app-protocol", 35),
          ("atmClp", 17),
          ("classifier", 11),
          ("cvlan8021p", 32),
          ("cvlanId", 29),
          ("destinationMac", 10),
          ("discard", 33),
          ("dlci", 34),
          ("doubleTag", 30),
          ("dscp", 6),
          ("frDe", 16),
          ("inboundInterface", 12),
          ("ipPrec", 5),
          ("ipv4Acl", 2),
          ("ipv6Acl", 14),
          ("ipv6Any", 20),
          ("ipv6Dscp", 18),
          ("ipv6DstIp", 21),
          ("ipv6NextHeader", 19),
          ("ipv6SrcIp", 22),
          ("l2Acl", 27),
          ("l2Protocol", 26),
          ("macGroup", 13),
          ("mplsExp", 8),
          ("outboundInterface", 25),
          ("protocol", 4),
          ("protocol-group", 36),
          ("qosLocalId", 15),
          ("rtpPort", 3),
          ("ruleString", 23),
          ("sourceMac", 9),
          ("sourceQosLocalId", 31),
          ("tagged-vxlan", 38),
          ("tcpFlag", 28),
          ("untagged-vxlan", 39),
          ("vlan8021p", 7),
          ("vlanId", 24),
          ("vlanid-cvlanid", 37))
    )



class CarAction(Integer32, TextualConvention):
    status = "current"
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
        *(("discard", 2),
          ("pass", 1),
          ("remark", 6),
          ("remark8021p", 7),
          ("remarkDscp", 4),
          ("remarkIpPrec", 3),
          ("remarkMplsExp", 5))
    )



class RemarkType(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("atmClp", 5),
          ("destinationMac", 10),
          ("dscp", 2),
          ("frDe", 6),
          ("ipPrec", 1),
          ("ipv6Dscp", 8),
          ("localPrec", 9),
          ("mplsExp", 3),
          ("qosLocalId", 7),
          ("vlan8021p", 4),
          ("vlanId", 11),
          ("vlanProtocol", 12))
    )



class CBQueueType(Integer32, TextualConvention):
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
        *(("af", 2),
          ("ef", 1),
          ("llq", 4),
          ("wfq", 3))
    )



class QueueBandwidthUnit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteUnitKbps", 1),
          ("percentUnit", 2),
          ("unavailable", -1))
    )



class WredType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscpbased", 2),
          ("ipPrecbased", 1))
    )



class SamplingType(Integer32, TextualConvention):
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
        *(("fixPackets", 1),
          ("fixTime", 2),
          ("randomPackets", 3),
          ("randomTime", 4))
    )



class LrCirUnit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteUnitBps", 1),
          ("percentUnit", 2))
    )



class RedirectType(Integer32, TextualConvention):
    status = "current"
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
        *(("cp", 1),
          ("ipNexthop", 2),
          ("ipv6Cp", 4),
          ("ipv6Nexthop", 5),
          ("lspLabel", 3),
          ("lspPath", 6))
    )



class RedirectCtrlType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )



class UrpfCtrlType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )



class DirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class CosType(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )



# MIB Managed Objects in the order of their OIDs

_HwQoS_ObjectIdentity = ObjectIdentity
hwQoS = _HwQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32)
)
_HwCBQoSObjects_ObjectIdentity = ObjectIdentity
hwCBQoSObjects = _HwCBQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1)
)
_HwCBQoSClassifierObjects_ObjectIdentity = ObjectIdentity
hwCBQoSClassifierObjects = _HwCBQoSClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1)
)
_HwCBQoSClassifierIndexNext_Type = Integer32
_HwCBQoSClassifierIndexNext_Object = MibScalar
hwCBQoSClassifierIndexNext = _HwCBQoSClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 1),
    _HwCBQoSClassifierIndexNext_Type()
)
hwCBQoSClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierIndexNext.setStatus("current")
_HwCBQoSClassifierCfgInfoTable_Object = MibTable
hwCBQoSClassifierCfgInfoTable = _HwCBQoSClassifierCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierCfgInfoTable.setStatus("current")
_HwCBQoSClassifierCfgInfoEntry_Object = MibTableRow
hwCBQoSClassifierCfgInfoEntry = _HwCBQoSClassifierCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1)
)
hwCBQoSClassifierCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSClassifierIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierCfgInfoEntry.setStatus("current")
_HwCBQoSClassifierIndex_Type = Integer32
_HwCBQoSClassifierIndex_Object = MibTableColumn
hwCBQoSClassifierIndex = _HwCBQoSClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1, 1),
    _HwCBQoSClassifierIndex_Type()
)
hwCBQoSClassifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierIndex.setStatus("current")


class _HwCBQoSClassifierName_Type(OctetString):
    """Custom type hwCBQoSClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSClassifierName_Type.__name__ = "OctetString"
_HwCBQoSClassifierName_Object = MibTableColumn
hwCBQoSClassifierName = _HwCBQoSClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1, 2),
    _HwCBQoSClassifierName_Type()
)
hwCBQoSClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierName.setStatus("current")
_HwCBQoSClassifierRuleCount_Type = Integer32
_HwCBQoSClassifierRuleCount_Object = MibTableColumn
hwCBQoSClassifierRuleCount = _HwCBQoSClassifierRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1, 3),
    _HwCBQoSClassifierRuleCount_Type()
)
hwCBQoSClassifierRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierRuleCount.setStatus("current")


class _HwCBQoSClassifierOperator_Type(Integer32):
    """Custom type hwCBQoSClassifierOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2))
    )


_HwCBQoSClassifierOperator_Type.__name__ = "Integer32"
_HwCBQoSClassifierOperator_Object = MibTableColumn
hwCBQoSClassifierOperator = _HwCBQoSClassifierOperator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1, 4),
    _HwCBQoSClassifierOperator_Type()
)
hwCBQoSClassifierOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierOperator.setStatus("current")


class _HwCBQoSClassifierLayer_Type(Integer32):
    """Custom type hwCBQoSClassifierLayer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("l2", 1),
          ("l3", 2),
          ("unavailable", -1))
    )


_HwCBQoSClassifierLayer_Type.__name__ = "Integer32"
_HwCBQoSClassifierLayer_Object = MibTableColumn
hwCBQoSClassifierLayer = _HwCBQoSClassifierLayer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1, 5),
    _HwCBQoSClassifierLayer_Type()
)
hwCBQoSClassifierLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierLayer.setStatus("current")
_HwCBQoSClassifierRowStatus_Type = RowStatus
_HwCBQoSClassifierRowStatus_Object = MibTableColumn
hwCBQoSClassifierRowStatus = _HwCBQoSClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 2, 1, 6),
    _HwCBQoSClassifierRowStatus_Type()
)
hwCBQoSClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierRowStatus.setStatus("current")
_HwCBQoSMatchRuleCfgInfoTable_Object = MibTable
hwCBQoSMatchRuleCfgInfoTable = _HwCBQoSMatchRuleCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleCfgInfoTable.setStatus("current")
_HwCBQoSMatchRuleCfgInfoEntry_Object = MibTableRow
hwCBQoSMatchRuleCfgInfoEntry = _HwCBQoSMatchRuleCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1)
)
hwCBQoSMatchRuleCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSClassifierIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSMatchVlanBeginId"),
)
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleCfgInfoEntry.setStatus("current")
_HwCBQoSMatchRuleIndex_Type = Integer32
_HwCBQoSMatchRuleIndex_Object = MibTableColumn
hwCBQoSMatchRuleIndex = _HwCBQoSMatchRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 1),
    _HwCBQoSMatchRuleIndex_Type()
)
hwCBQoSMatchRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIndex.setStatus("current")


class _HwCBQoSMatchRuleIfNot_Type(Integer32):
    """Custom type hwCBQoSMatchRuleIfNot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match", 1),
          ("notMatch", 2))
    )


_HwCBQoSMatchRuleIfNot_Type.__name__ = "Integer32"
_HwCBQoSMatchRuleIfNot_Object = MibTableColumn
hwCBQoSMatchRuleIfNot = _HwCBQoSMatchRuleIfNot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 2),
    _HwCBQoSMatchRuleIfNot_Type()
)
hwCBQoSMatchRuleIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIfNot.setStatus("current")
_HwCBQoSMatchRuleType_Type = MatchRuleType
_HwCBQoSMatchRuleType_Object = MibTableColumn
hwCBQoSMatchRuleType = _HwCBQoSMatchRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 3),
    _HwCBQoSMatchRuleType_Type()
)
hwCBQoSMatchRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleType.setStatus("current")


class _HwCBQoSMatchRuleStringValue_Type(OctetString):
    """Custom type hwCBQoSMatchRuleStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwCBQoSMatchRuleStringValue_Type.__name__ = "OctetString"
_HwCBQoSMatchRuleStringValue_Object = MibTableColumn
hwCBQoSMatchRuleStringValue = _HwCBQoSMatchRuleStringValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 4),
    _HwCBQoSMatchRuleStringValue_Type()
)
hwCBQoSMatchRuleStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleStringValue.setStatus("current")
_HwCBQoSMatchRuleIntValue1_Type = Unsigned32
_HwCBQoSMatchRuleIntValue1_Object = MibTableColumn
hwCBQoSMatchRuleIntValue1 = _HwCBQoSMatchRuleIntValue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 5),
    _HwCBQoSMatchRuleIntValue1_Type()
)
hwCBQoSMatchRuleIntValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIntValue1.setStatus("current")
_HwCBQoSMatchRuleIntValue2_Type = Unsigned32
_HwCBQoSMatchRuleIntValue2_Object = MibTableColumn
hwCBQoSMatchRuleIntValue2 = _HwCBQoSMatchRuleIntValue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 6),
    _HwCBQoSMatchRuleIntValue2_Type()
)
hwCBQoSMatchRuleIntValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIntValue2.setStatus("current")
_HwCBQoSMatchRuleRowStatus_Type = RowStatus
_HwCBQoSMatchRuleRowStatus_Object = MibTableColumn
hwCBQoSMatchRuleRowStatus = _HwCBQoSMatchRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 7),
    _HwCBQoSMatchRuleRowStatus_Type()
)
hwCBQoSMatchRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleRowStatus.setStatus("current")


class _HwCBQoSMatchMacMask_Type(OctetString):
    """Custom type hwCBQoSMatchMacMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HwCBQoSMatchMacMask_Type.__name__ = "OctetString"
_HwCBQoSMatchMacMask_Object = MibTableColumn
hwCBQoSMatchMacMask = _HwCBQoSMatchMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 8),
    _HwCBQoSMatchMacMask_Type()
)
hwCBQoSMatchMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchMacMask.setStatus("current")
_HwCBQoSMatchVlanBeginId_Type = Unsigned32
_HwCBQoSMatchVlanBeginId_Object = MibTableColumn
hwCBQoSMatchVlanBeginId = _HwCBQoSMatchVlanBeginId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 9),
    _HwCBQoSMatchVlanBeginId_Type()
)
hwCBQoSMatchVlanBeginId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSMatchVlanBeginId.setStatus("current")
_HwCBQoSMatchVlanEndId_Type = Unsigned32
_HwCBQoSMatchVlanEndId_Object = MibTableColumn
hwCBQoSMatchVlanEndId = _HwCBQoSMatchVlanEndId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 10),
    _HwCBQoSMatchVlanEndId_Type()
)
hwCBQoSMatchVlanEndId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchVlanEndId.setStatus("current")
_HwCBQoSMatchInnerSrcIp_Type = IpAddress
_HwCBQoSMatchInnerSrcIp_Object = MibTableColumn
hwCBQoSMatchInnerSrcIp = _HwCBQoSMatchInnerSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 11),
    _HwCBQoSMatchInnerSrcIp_Type()
)
hwCBQoSMatchInnerSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerSrcIp.setStatus("current")


class _HwCBQoSMatchInnerSrcIpMask_Type(Unsigned32):
    """Custom type hwCBQoSMatchInnerSrcIpMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwCBQoSMatchInnerSrcIpMask_Type.__name__ = "Unsigned32"
_HwCBQoSMatchInnerSrcIpMask_Object = MibTableColumn
hwCBQoSMatchInnerSrcIpMask = _HwCBQoSMatchInnerSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 12),
    _HwCBQoSMatchInnerSrcIpMask_Type()
)
hwCBQoSMatchInnerSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerSrcIpMask.setStatus("current")
_HwCBQoSMatchInnerDstIp_Type = IpAddress
_HwCBQoSMatchInnerDstIp_Object = MibTableColumn
hwCBQoSMatchInnerDstIp = _HwCBQoSMatchInnerDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 13),
    _HwCBQoSMatchInnerDstIp_Type()
)
hwCBQoSMatchInnerDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerDstIp.setStatus("current")


class _HwCBQoSMatchInnerDstIpMask_Type(Unsigned32):
    """Custom type hwCBQoSMatchInnerDstIpMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwCBQoSMatchInnerDstIpMask_Type.__name__ = "Unsigned32"
_HwCBQoSMatchInnerDstIpMask_Object = MibTableColumn
hwCBQoSMatchInnerDstIpMask = _HwCBQoSMatchInnerDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 14),
    _HwCBQoSMatchInnerDstIpMask_Type()
)
hwCBQoSMatchInnerDstIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerDstIpMask.setStatus("current")


class _HwCBQoSMatchInnerSrcPort_Type(Unsigned32):
    """Custom type hwCBQoSMatchInnerSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(65536, 65536),
    )


_HwCBQoSMatchInnerSrcPort_Type.__name__ = "Unsigned32"
_HwCBQoSMatchInnerSrcPort_Object = MibTableColumn
hwCBQoSMatchInnerSrcPort = _HwCBQoSMatchInnerSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 15),
    _HwCBQoSMatchInnerSrcPort_Type()
)
hwCBQoSMatchInnerSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerSrcPort.setStatus("current")


class _HwCBQoSMatchInnerDstPort_Type(Unsigned32):
    """Custom type hwCBQoSMatchInnerDstPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(65536, 65536),
    )


_HwCBQoSMatchInnerDstPort_Type.__name__ = "Unsigned32"
_HwCBQoSMatchInnerDstPort_Object = MibTableColumn
hwCBQoSMatchInnerDstPort = _HwCBQoSMatchInnerDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 16),
    _HwCBQoSMatchInnerDstPort_Type()
)
hwCBQoSMatchInnerDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerDstPort.setStatus("current")


class _HwCBQoSMatchInnerProtocol_Type(Unsigned32):
    """Custom type hwCBQoSMatchInnerProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65536, 65536),
    )


_HwCBQoSMatchInnerProtocol_Type.__name__ = "Unsigned32"
_HwCBQoSMatchInnerProtocol_Object = MibTableColumn
hwCBQoSMatchInnerProtocol = _HwCBQoSMatchInnerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 1, 3, 1, 17),
    _HwCBQoSMatchInnerProtocol_Type()
)
hwCBQoSMatchInnerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchInnerProtocol.setStatus("current")
_HwCBQoSBehaviorObjects_ObjectIdentity = ObjectIdentity
hwCBQoSBehaviorObjects = _HwCBQoSBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2)
)
_HwCBQoSBehaviorIndexNext_Type = Integer32
_HwCBQoSBehaviorIndexNext_Object = MibScalar
hwCBQoSBehaviorIndexNext = _HwCBQoSBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 1),
    _HwCBQoSBehaviorIndexNext_Type()
)
hwCBQoSBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorIndexNext.setStatus("current")
_HwCBQoSBehaviorCfgInfoTable_Object = MibTable
hwCBQoSBehaviorCfgInfoTable = _HwCBQoSBehaviorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSBehaviorCfgInfoTable.setStatus("current")
_HwCBQoSBehaviorCfgInfoEntry_Object = MibTableRow
hwCBQoSBehaviorCfgInfoEntry = _HwCBQoSBehaviorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 2, 1)
)
hwCBQoSBehaviorCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSBehaviorCfgInfoEntry.setStatus("current")
_HwCBQoSBehaviorIndex_Type = Integer32
_HwCBQoSBehaviorIndex_Object = MibTableColumn
hwCBQoSBehaviorIndex = _HwCBQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 2, 1, 1),
    _HwCBQoSBehaviorIndex_Type()
)
hwCBQoSBehaviorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorIndex.setStatus("current")


class _HwCBQoSBehaviorName_Type(OctetString):
    """Custom type hwCBQoSBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSBehaviorName_Type.__name__ = "OctetString"
_HwCBQoSBehaviorName_Object = MibTableColumn
hwCBQoSBehaviorName = _HwCBQoSBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 2, 1, 2),
    _HwCBQoSBehaviorName_Type()
)
hwCBQoSBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorName.setStatus("current")
_HwCBQoSBehaviorRowStatus_Type = RowStatus
_HwCBQoSBehaviorRowStatus_Object = MibTableColumn
hwCBQoSBehaviorRowStatus = _HwCBQoSBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 2, 1, 3),
    _HwCBQoSBehaviorRowStatus_Type()
)
hwCBQoSBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorRowStatus.setStatus("current")
_HwCBQoSCarCfgInfoTable_Object = MibTable
hwCBQoSCarCfgInfoTable = _HwCBQoSCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSCarCfgInfoTable.setStatus("current")
_HwCBQoSCarCfgInfoEntry_Object = MibTableRow
hwCBQoSCarCfgInfoEntry = _HwCBQoSCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1)
)
hwCBQoSCarCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSCarCfgInfoEntry.setStatus("current")
_HwCBQoSCarCir_Type = Unsigned32
_HwCBQoSCarCir_Object = MibTableColumn
hwCBQoSCarCir = _HwCBQoSCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 1),
    _HwCBQoSCarCir_Type()
)
hwCBQoSCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarCir.setStatus("current")
_HwCBQoSCarCbs_Type = Unsigned32
_HwCBQoSCarCbs_Object = MibTableColumn
hwCBQoSCarCbs = _HwCBQoSCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 2),
    _HwCBQoSCarCbs_Type()
)
hwCBQoSCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarCbs.setStatus("current")


class _HwCBQoSCarEbs_Type(Unsigned32):
    """Custom type hwCBQoSCarEbs based on Unsigned32"""
    defaultValue = 0


_HwCBQoSCarEbs_Object = MibTableColumn
hwCBQoSCarEbs = _HwCBQoSCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 3),
    _HwCBQoSCarEbs_Type()
)
hwCBQoSCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarEbs.setStatus("current")
_HwCBQoSCarPir_Type = Unsigned32
_HwCBQoSCarPir_Object = MibTableColumn
hwCBQoSCarPir = _HwCBQoSCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 4),
    _HwCBQoSCarPir_Type()
)
hwCBQoSCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarPir.setStatus("current")
_HwCBQoSCarPbs_Type = Unsigned32
_HwCBQoSCarPbs_Object = MibTableColumn
hwCBQoSCarPbs = _HwCBQoSCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 5),
    _HwCBQoSCarPbs_Type()
)
hwCBQoSCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarPbs.setStatus("current")


class _HwCBQoSCarGreenAction_Type(CarAction):
    """Custom type hwCBQoSCarGreenAction based on CarAction"""


_HwCBQoSCarGreenAction_Object = MibTableColumn
hwCBQoSCarGreenAction = _HwCBQoSCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 6),
    _HwCBQoSCarGreenAction_Type()
)
hwCBQoSCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarGreenAction.setStatus("current")


class _HwCBQoSCarGreenRemarkValue_Type(Integer32):
    """Custom type hwCBQoSCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(11, 81),
    )


_HwCBQoSCarGreenRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSCarGreenRemarkValue_Object = MibTableColumn
hwCBQoSCarGreenRemarkValue = _HwCBQoSCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 7),
    _HwCBQoSCarGreenRemarkValue_Type()
)
hwCBQoSCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarGreenRemarkValue.setStatus("current")


class _HwCBQoSCarYellowAction_Type(CarAction):
    """Custom type hwCBQoSCarYellowAction based on CarAction"""


_HwCBQoSCarYellowAction_Object = MibTableColumn
hwCBQoSCarYellowAction = _HwCBQoSCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 8),
    _HwCBQoSCarYellowAction_Type()
)
hwCBQoSCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarYellowAction.setStatus("current")


class _HwCBQoSCarYellowRemarkValue_Type(Integer32):
    """Custom type hwCBQoSCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(11, 81),
    )


_HwCBQoSCarYellowRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSCarYellowRemarkValue_Object = MibTableColumn
hwCBQoSCarYellowRemarkValue = _HwCBQoSCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 9),
    _HwCBQoSCarYellowRemarkValue_Type()
)
hwCBQoSCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarYellowRemarkValue.setStatus("current")


class _HwCBQoSCarRedAction_Type(CarAction):
    """Custom type hwCBQoSCarRedAction based on CarAction"""


_HwCBQoSCarRedAction_Object = MibTableColumn
hwCBQoSCarRedAction = _HwCBQoSCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 10),
    _HwCBQoSCarRedAction_Type()
)
hwCBQoSCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarRedAction.setStatus("current")


class _HwCBQoSCarRedRemarkValue_Type(Integer32):
    """Custom type hwCBQoSCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(11, 81),
    )


_HwCBQoSCarRedRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSCarRedRemarkValue_Object = MibTableColumn
hwCBQoSCarRedRemarkValue = _HwCBQoSCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 11),
    _HwCBQoSCarRedRemarkValue_Type()
)
hwCBQoSCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarRedRemarkValue.setStatus("current")
_HwCBQoSCarRowStatus_Type = RowStatus
_HwCBQoSCarRowStatus_Object = MibTableColumn
hwCBQoSCarRowStatus = _HwCBQoSCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 12),
    _HwCBQoSCarRowStatus_Type()
)
hwCBQoSCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarRowStatus.setStatus("current")


class _HwCBQosCarAggregation_Type(Integer32):
    """Custom type hwCBQosCarAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregationCar", 1),
          ("noneAggregationCar", 2))
    )


_HwCBQosCarAggregation_Type.__name__ = "Integer32"
_HwCBQosCarAggregation_Object = MibTableColumn
hwCBQosCarAggregation = _HwCBQosCarAggregation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 3, 1, 13),
    _HwCBQosCarAggregation_Type()
)
hwCBQosCarAggregation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQosCarAggregation.setStatus("current")
_HwCBQoSGtsCfgInfoTable_Object = MibTable
hwCBQoSGtsCfgInfoTable = _HwCBQoSGtsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSGtsCfgInfoTable.setStatus("current")
_HwCBQoSGtsCfgInfoEntry_Object = MibTableRow
hwCBQoSGtsCfgInfoEntry = _HwCBQoSGtsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1)
)
hwCBQoSGtsCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSGtsCfgInfoEntry.setStatus("current")
_HwCBQoSGtsCir_Type = Integer32
_HwCBQoSGtsCir_Object = MibTableColumn
hwCBQoSGtsCir = _HwCBQoSGtsCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1, 1),
    _HwCBQoSGtsCir_Type()
)
hwCBQoSGtsCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsCir.setStatus("current")


class _HwCBQoSGtsCbs_Type(Integer32):
    """Custom type hwCBQoSGtsCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_HwCBQoSGtsCbs_Type.__name__ = "Integer32"
_HwCBQoSGtsCbs_Object = MibTableColumn
hwCBQoSGtsCbs = _HwCBQoSGtsCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1, 2),
    _HwCBQoSGtsCbs_Type()
)
hwCBQoSGtsCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsCbs.setStatus("current")


class _HwCBQoSGtsEbs_Type(Integer32):
    """Custom type hwCBQoSGtsEbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_HwCBQoSGtsEbs_Type.__name__ = "Integer32"
_HwCBQoSGtsEbs_Object = MibTableColumn
hwCBQoSGtsEbs = _HwCBQoSGtsEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1, 3),
    _HwCBQoSGtsEbs_Type()
)
hwCBQoSGtsEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsEbs.setStatus("current")


class _HwCBQoSGtsQueueLength_Type(Integer32):
    """Custom type hwCBQoSGtsQueueLength based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwCBQoSGtsQueueLength_Type.__name__ = "Integer32"
_HwCBQoSGtsQueueLength_Object = MibTableColumn
hwCBQoSGtsQueueLength = _HwCBQoSGtsQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1, 4),
    _HwCBQoSGtsQueueLength_Type()
)
hwCBQoSGtsQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsQueueLength.setStatus("current")
_HwCBQoSGtsRowStatus_Type = RowStatus
_HwCBQoSGtsRowStatus_Object = MibTableColumn
hwCBQoSGtsRowStatus = _HwCBQoSGtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1, 5),
    _HwCBQoSGtsRowStatus_Type()
)
hwCBQoSGtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsRowStatus.setStatus("current")


class _HwCBQoSGtsPir_Type(Integer32):
    """Custom type hwCBQoSGtsPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_HwCBQoSGtsPir_Type.__name__ = "Integer32"
_HwCBQoSGtsPir_Object = MibTableColumn
hwCBQoSGtsPir = _HwCBQoSGtsPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 4, 1, 6),
    _HwCBQoSGtsPir_Type()
)
hwCBQoSGtsPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsPir.setStatus("current")
_HwCBQoSRemarkCfgInfoTable_Object = MibTable
hwCBQoSRemarkCfgInfoTable = _HwCBQoSRemarkCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkCfgInfoTable.setStatus("current")
_HwCBQoSRemarkCfgInfoEntry_Object = MibTableRow
hwCBQoSRemarkCfgInfoEntry = _HwCBQoSRemarkCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 5, 1)
)
hwCBQoSRemarkCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSRemarkType"),
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkCfgInfoEntry.setStatus("current")
_HwCBQoSRemarkType_Type = RemarkType
_HwCBQoSRemarkType_Object = MibTableColumn
hwCBQoSRemarkType = _HwCBQoSRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 5, 1, 1),
    _HwCBQoSRemarkType_Type()
)
hwCBQoSRemarkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSRemarkType.setStatus("current")


class _HwCBQoSRemarkValue_Type(Integer32):
    """Custom type hwCBQoSRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwCBQoSRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSRemarkValue_Object = MibTableColumn
hwCBQoSRemarkValue = _HwCBQoSRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 5, 1, 2),
    _HwCBQoSRemarkValue_Type()
)
hwCBQoSRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkValue.setStatus("current")


class _HwCBQoSRemarkStringValue_Type(OctetString):
    """Custom type hwCBQoSRemarkStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwCBQoSRemarkStringValue_Type.__name__ = "OctetString"
_HwCBQoSRemarkStringValue_Object = MibTableColumn
hwCBQoSRemarkStringValue = _HwCBQoSRemarkStringValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 5, 1, 3),
    _HwCBQoSRemarkStringValue_Type()
)
hwCBQoSRemarkStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkStringValue.setStatus("current")
_HwCBQoSRemarkRowStatus_Type = RowStatus
_HwCBQoSRemarkRowStatus_Object = MibTableColumn
hwCBQoSRemarkRowStatus = _HwCBQoSRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 5, 1, 4),
    _HwCBQoSRemarkRowStatus_Type()
)
hwCBQoSRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkRowStatus.setStatus("current")
_HwCBQoSQueueCfgInfoTable_Object = MibTable
hwCBQoSQueueCfgInfoTable = _HwCBQoSQueueCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSQueueCfgInfoTable.setStatus("current")
_HwCBQoSQueueCfgInfoEntry_Object = MibTableRow
hwCBQoSQueueCfgInfoEntry = _HwCBQoSQueueCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1)
)
hwCBQoSQueueCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSQueueCfgInfoEntry.setStatus("current")
_HwCBQoSQueueType_Type = CBQueueType
_HwCBQoSQueueType_Object = MibTableColumn
hwCBQoSQueueType = _HwCBQoSQueueType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 1),
    _HwCBQoSQueueType_Type()
)
hwCBQoSQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueType.setStatus("current")


class _HwCBQoSQueueDropType_Type(Integer32):
    """Custom type hwCBQoSQueueDropType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tailDrop", 1),
          ("unavailable", -1),
          ("wred", 2))
    )


_HwCBQoSQueueDropType_Type.__name__ = "Integer32"
_HwCBQoSQueueDropType_Object = MibTableColumn
hwCBQoSQueueDropType = _HwCBQoSQueueDropType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 2),
    _HwCBQoSQueueDropType_Type()
)
hwCBQoSQueueDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueDropType.setStatus("current")


class _HwCBQoSQueueLength_Type(Integer32):
    """Custom type hwCBQoSQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1024),
    )


_HwCBQoSQueueLength_Type.__name__ = "Integer32"
_HwCBQoSQueueLength_Object = MibTableColumn
hwCBQoSQueueLength = _HwCBQoSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 3),
    _HwCBQoSQueueLength_Type()
)
hwCBQoSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueLength.setStatus("current")
_HwCBQoSQueueBandwidthUnit_Type = QueueBandwidthUnit
_HwCBQoSQueueBandwidthUnit_Object = MibTableColumn
hwCBQoSQueueBandwidthUnit = _HwCBQoSQueueBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 4),
    _HwCBQoSQueueBandwidthUnit_Type()
)
hwCBQoSQueueBandwidthUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueBandwidthUnit.setStatus("current")


class _HwCBQoSQueueBandwidthValue_Type(Integer32):
    """Custom type hwCBQoSQueueBandwidthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000000),
    )


_HwCBQoSQueueBandwidthValue_Type.__name__ = "Integer32"
_HwCBQoSQueueBandwidthValue_Object = MibTableColumn
hwCBQoSQueueBandwidthValue = _HwCBQoSQueueBandwidthValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 5),
    _HwCBQoSQueueBandwidthValue_Type()
)
hwCBQoSQueueBandwidthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueBandwidthValue.setStatus("current")


class _HwCBQoSQueueCbs_Type(Integer32):
    """Custom type hwCBQoSQueueCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(32, 2000000),
    )


_HwCBQoSQueueCbs_Type.__name__ = "Integer32"
_HwCBQoSQueueCbs_Object = MibTableColumn
hwCBQoSQueueCbs = _HwCBQoSQueueCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 6),
    _HwCBQoSQueueCbs_Type()
)
hwCBQoSQueueCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueCbs.setStatus("current")


class _HwCBQoSQueueQueueNumber_Type(Integer32):
    """Custom type hwCBQoSQueueQueueNumber based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("a1", 1),
          ("a1024", 1024),
          ("a128", 128),
          ("a16", 16),
          ("a2048", 2048),
          ("a256", 256),
          ("a32", 32),
          ("a4096", 4096),
          ("a512", 512),
          ("a64", 64),
          ("a8", 8),
          ("unavailable", -1))
    )


_HwCBQoSQueueQueueNumber_Type.__name__ = "Integer32"
_HwCBQoSQueueQueueNumber_Object = MibTableColumn
hwCBQoSQueueQueueNumber = _HwCBQoSQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 7),
    _HwCBQoSQueueQueueNumber_Type()
)
hwCBQoSQueueQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueQueueNumber.setStatus("current")
_HwCBQoSQueueRowStatus_Type = RowStatus
_HwCBQoSQueueRowStatus_Object = MibTableColumn
hwCBQoSQueueRowStatus = _HwCBQoSQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 8),
    _HwCBQoSQueueRowStatus_Type()
)
hwCBQoSQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueRowStatus.setStatus("current")


class _HwCBQoSQueueCbsRatio_Type(Integer32):
    """Custom type hwCBQoSQueueCbsRatio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(25, 500),
    )


_HwCBQoSQueueCbsRatio_Type.__name__ = "Integer32"
_HwCBQoSQueueCbsRatio_Object = MibTableColumn
hwCBQoSQueueCbsRatio = _HwCBQoSQueueCbsRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 6, 1, 9),
    _HwCBQoSQueueCbsRatio_Type()
)
hwCBQoSQueueCbsRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueCbsRatio.setStatus("current")
_HwCBQoSWredCfgInfoTable_Object = MibTable
hwCBQoSWredCfgInfoTable = _HwCBQoSWredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSWredCfgInfoTable.setStatus("current")
_HwCBQoSWredCfgInfoEntry_Object = MibTableRow
hwCBQoSWredCfgInfoEntry = _HwCBQoSWredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 7, 1)
)
hwCBQoSWredCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSWredCfgInfoEntry.setStatus("current")


class _HwCBQoSWredType_Type(WredType):
    """Custom type hwCBQoSWredType based on WredType"""


_HwCBQoSWredType_Object = MibTableColumn
hwCBQoSWredType = _HwCBQoSWredType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 7, 1, 1),
    _HwCBQoSWredType_Type()
)
hwCBQoSWredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredType.setStatus("current")


class _HwCBQoSWredWeightConst_Type(Integer32):
    """Custom type hwCBQoSWredWeightConst based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwCBQoSWredWeightConst_Type.__name__ = "Integer32"
_HwCBQoSWredWeightConst_Object = MibTableColumn
hwCBQoSWredWeightConst = _HwCBQoSWredWeightConst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 7, 1, 2),
    _HwCBQoSWredWeightConst_Type()
)
hwCBQoSWredWeightConst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredWeightConst.setStatus("current")
_HwCBQoSWredDropProfileIndex_Type = Integer32
_HwCBQoSWredDropProfileIndex_Object = MibTableColumn
hwCBQoSWredDropProfileIndex = _HwCBQoSWredDropProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 7, 1, 3),
    _HwCBQoSWredDropProfileIndex_Type()
)
hwCBQoSWredDropProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredDropProfileIndex.setStatus("current")
_HwCBQoSWredCfgRowStatus_Type = RowStatus
_HwCBQoSWredCfgRowStatus_Object = MibTableColumn
hwCBQoSWredCfgRowStatus = _HwCBQoSWredCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 7, 1, 4),
    _HwCBQoSWredCfgRowStatus_Type()
)
hwCBQoSWredCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSWredCfgRowStatus.setStatus("current")
_HwCBQoSWredClassCfgInfoTable_Object = MibTable
hwCBQoSWredClassCfgInfoTable = _HwCBQoSWredClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSWredClassCfgInfoTable.setStatus("current")
_HwCBQoSWredClassCfgInfoEntry_Object = MibTableRow
hwCBQoSWredClassCfgInfoEntry = _HwCBQoSWredClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 8, 1)
)
hwCBQoSWredClassCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSWredClassCfgInfoEntry.setStatus("current")


class _HwCBQoSWredClassValue_Type(Integer32):
    """Custom type hwCBQoSWredClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwCBQoSWredClassValue_Type.__name__ = "Integer32"
_HwCBQoSWredClassValue_Object = MibTableColumn
hwCBQoSWredClassValue = _HwCBQoSWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 8, 1, 1),
    _HwCBQoSWredClassValue_Type()
)
hwCBQoSWredClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSWredClassValue.setStatus("current")


class _HwCBQoSWredClassLowLimit_Type(Integer32):
    """Custom type hwCBQoSWredClassLowLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwCBQoSWredClassLowLimit_Type.__name__ = "Integer32"
_HwCBQoSWredClassLowLimit_Object = MibTableColumn
hwCBQoSWredClassLowLimit = _HwCBQoSWredClassLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 8, 1, 2),
    _HwCBQoSWredClassLowLimit_Type()
)
hwCBQoSWredClassLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredClassLowLimit.setStatus("current")


class _HwCBQoSWredClassHighLimit_Type(Integer32):
    """Custom type hwCBQoSWredClassHighLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwCBQoSWredClassHighLimit_Type.__name__ = "Integer32"
_HwCBQoSWredClassHighLimit_Object = MibTableColumn
hwCBQoSWredClassHighLimit = _HwCBQoSWredClassHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 8, 1, 3),
    _HwCBQoSWredClassHighLimit_Type()
)
hwCBQoSWredClassHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredClassHighLimit.setStatus("current")


class _HwCBQoSWredClassDiscardProb_Type(Integer32):
    """Custom type hwCBQoSWredClassDiscardProb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCBQoSWredClassDiscardProb_Type.__name__ = "Integer32"
_HwCBQoSWredClassDiscardProb_Object = MibTableColumn
hwCBQoSWredClassDiscardProb = _HwCBQoSWredClassDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 8, 1, 4),
    _HwCBQoSWredClassDiscardProb_Type()
)
hwCBQoSWredClassDiscardProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredClassDiscardProb.setStatus("current")
_HwCBQoSNatCfgInfoTable_Object = MibTable
hwCBQoSNatCfgInfoTable = _HwCBQoSNatCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hwCBQoSNatCfgInfoTable.setStatus("current")
_HwCBQoSNatCfgInfoEntry_Object = MibTableRow
hwCBQoSNatCfgInfoEntry = _HwCBQoSNatCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 10, 1)
)
hwCBQoSNatCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSNatCfgInfoEntry.setStatus("current")


class _HwCBQoSNatAddressGroup_Type(OctetString):
    """Custom type hwCBQoSNatAddressGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSNatAddressGroup_Type.__name__ = "OctetString"
_HwCBQoSNatAddressGroup_Object = MibTableColumn
hwCBQoSNatAddressGroup = _HwCBQoSNatAddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 10, 1, 1),
    _HwCBQoSNatAddressGroup_Type()
)
hwCBQoSNatAddressGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatAddressGroup.setStatus("current")


class _HwCBQoSNatNoPat_Type(Integer32):
    """Custom type hwCBQoSNatNoPat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nopat", 1),
          ("pat", 2))
    )


_HwCBQoSNatNoPat_Type.__name__ = "Integer32"
_HwCBQoSNatNoPat_Object = MibTableColumn
hwCBQoSNatNoPat = _HwCBQoSNatNoPat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 10, 1, 2),
    _HwCBQoSNatNoPat_Type()
)
hwCBQoSNatNoPat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatNoPat.setStatus("current")


class _HwCBQoSNatServiceClass_Type(Integer32):
    """Custom type hwCBQoSNatServiceClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwCBQoSNatServiceClass_Type.__name__ = "Integer32"
_HwCBQoSNatServiceClass_Object = MibTableColumn
hwCBQoSNatServiceClass = _HwCBQoSNatServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 10, 1, 3),
    _HwCBQoSNatServiceClass_Type()
)
hwCBQoSNatServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatServiceClass.setStatus("current")
_HwCBQoSNatRowStatus_Type = RowStatus
_HwCBQoSNatRowStatus_Object = MibTableColumn
hwCBQoSNatRowStatus = _HwCBQoSNatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 10, 1, 4),
    _HwCBQoSNatRowStatus_Type()
)
hwCBQoSNatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatRowStatus.setStatus("current")
_HwCBQoSFirewallCfgInfoTable_Object = MibTable
hwCBQoSFirewallCfgInfoTable = _HwCBQoSFirewallCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hwCBQoSFirewallCfgInfoTable.setStatus("current")
_HwCBQoSFirewallCfgInfoEntry_Object = MibTableRow
hwCBQoSFirewallCfgInfoEntry = _HwCBQoSFirewallCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 11, 1)
)
hwCBQoSFirewallCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFirewallCfgInfoEntry.setStatus("current")


class _HwCBQoSFirewallAction_Type(Integer32):
    """Custom type hwCBQoSFirewallAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwCBQoSFirewallAction_Type.__name__ = "Integer32"
_HwCBQoSFirewallAction_Object = MibTableColumn
hwCBQoSFirewallAction = _HwCBQoSFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 11, 1, 1),
    _HwCBQoSFirewallAction_Type()
)
hwCBQoSFirewallAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFirewallAction.setStatus("current")
_HwCBQoSFirewallRowStatus_Type = RowStatus
_HwCBQoSFirewallRowStatus_Object = MibTableColumn
hwCBQoSFirewallRowStatus = _HwCBQoSFirewallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 11, 1, 2),
    _HwCBQoSFirewallRowStatus_Type()
)
hwCBQoSFirewallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFirewallRowStatus.setStatus("current")
_HwCBQoSSamplingCfgInfoTable_Object = MibTable
hwCBQoSSamplingCfgInfoTable = _HwCBQoSSamplingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hwCBQoSSamplingCfgInfoTable.setStatus("current")
_HwCBQoSSamplingCfgInfoEntry_Object = MibTableRow
hwCBQoSSamplingCfgInfoEntry = _HwCBQoSSamplingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 12, 1)
)
hwCBQoSSamplingCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSSamplingCfgInfoEntry.setStatus("current")
_HwCBQoSIfSamplingType_Type = SamplingType
_HwCBQoSIfSamplingType_Object = MibTableColumn
hwCBQoSIfSamplingType = _HwCBQoSIfSamplingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 12, 1, 1),
    _HwCBQoSIfSamplingType_Type()
)
hwCBQoSIfSamplingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfSamplingType.setStatus("current")


class _HwCBQoSSamplingNum_Type(Integer32):
    """Custom type hwCBQoSSamplingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwCBQoSSamplingNum_Type.__name__ = "Integer32"
_HwCBQoSSamplingNum_Object = MibTableColumn
hwCBQoSSamplingNum = _HwCBQoSSamplingNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 12, 1, 2),
    _HwCBQoSSamplingNum_Type()
)
hwCBQoSSamplingNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSamplingNum.setStatus("current")
_HwCBQoSSamplingRowStatus_Type = RowStatus
_HwCBQoSSamplingRowStatus_Object = MibTableColumn
hwCBQoSSamplingRowStatus = _HwCBQoSSamplingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 12, 1, 3),
    _HwCBQoSSamplingRowStatus_Type()
)
hwCBQoSSamplingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSamplingRowStatus.setStatus("current")
_HwCBQoSLrCfgInfoTable_Object = MibTable
hwCBQoSLrCfgInfoTable = _HwCBQoSLrCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hwCBQoSLrCfgInfoTable.setStatus("current")
_HwCBQoSLrCfgInfoEntry_Object = MibTableRow
hwCBQoSLrCfgInfoEntry = _HwCBQoSLrCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13, 1)
)
hwCBQoSLrCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSLrCfgInfoEntry.setStatus("current")
_HwCBQoSLrUnit_Type = LrCirUnit
_HwCBQoSLrUnit_Object = MibTableColumn
hwCBQoSLrUnit = _HwCBQoSLrUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13, 1, 1),
    _HwCBQoSLrUnit_Type()
)
hwCBQoSLrUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrUnit.setStatus("current")


class _HwCBQoSLrCir_Type(Integer32):
    """Custom type hwCBQoSLrCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000000),
    )


_HwCBQoSLrCir_Type.__name__ = "Integer32"
_HwCBQoSLrCir_Object = MibTableColumn
hwCBQoSLrCir = _HwCBQoSLrCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13, 1, 2),
    _HwCBQoSLrCir_Type()
)
hwCBQoSLrCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrCir.setStatus("current")


class _HwCBQoSLrCbs_Type(Integer32):
    """Custom type hwCBQoSLrCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 155000000),
    )


_HwCBQoSLrCbs_Type.__name__ = "Integer32"
_HwCBQoSLrCbs_Object = MibTableColumn
hwCBQoSLrCbs = _HwCBQoSLrCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13, 1, 3),
    _HwCBQoSLrCbs_Type()
)
hwCBQoSLrCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrCbs.setStatus("current")


class _HwCBQoSLrEbs_Type(Integer32):
    """Custom type hwCBQoSLrEbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_HwCBQoSLrEbs_Type.__name__ = "Integer32"
_HwCBQoSLrEbs_Object = MibTableColumn
hwCBQoSLrEbs = _HwCBQoSLrEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13, 1, 4),
    _HwCBQoSLrEbs_Type()
)
hwCBQoSLrEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrEbs.setStatus("current")
_HwCBQoSLrRowStatus_Type = RowStatus
_HwCBQoSLrRowStatus_Object = MibTableColumn
hwCBQoSLrRowStatus = _HwCBQoSLrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 13, 1, 5),
    _HwCBQoSLrRowStatus_Type()
)
hwCBQoSLrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrRowStatus.setStatus("current")
_HwCBQoSNestPolicyCfgInfoTable_Object = MibTable
hwCBQoSNestPolicyCfgInfoTable = _HwCBQoSNestPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyCfgInfoTable.setStatus("current")
_HwCBQoSNestPolicyCfgInfoEntry_Object = MibTableRow
hwCBQoSNestPolicyCfgInfoEntry = _HwCBQoSNestPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 14, 1)
)
hwCBQoSNestPolicyCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyCfgInfoEntry.setStatus("current")


class _HwCBQoSNestPolicyName_Type(OctetString):
    """Custom type hwCBQoSNestPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSNestPolicyName_Type.__name__ = "OctetString"
_HwCBQoSNestPolicyName_Object = MibTableColumn
hwCBQoSNestPolicyName = _HwCBQoSNestPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 14, 1, 1),
    _HwCBQoSNestPolicyName_Type()
)
hwCBQoSNestPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyName.setStatus("current")
_HwCBQoSNestPolicyRowStatus_Type = RowStatus
_HwCBQoSNestPolicyRowStatus_Object = MibTableColumn
hwCBQoSNestPolicyRowStatus = _HwCBQoSNestPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 14, 1, 2),
    _HwCBQoSNestPolicyRowStatus_Type()
)
hwCBQoSNestPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyRowStatus.setStatus("current")
_HwCBQoSRedirectCfgInfoTable_Object = MibTable
hwCBQoSRedirectCfgInfoTable = _HwCBQoSRedirectCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectCfgInfoTable.setStatus("current")
_HwCBQoSRedirectCfgInfoEntry_Object = MibTableRow
hwCBQoSRedirectCfgInfoEntry = _HwCBQoSRedirectCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1)
)
hwCBQoSRedirectCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSRedirectType"),
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectCfgInfoEntry.setStatus("current")
_HwCBQoSRedirectType_Type = RedirectType
_HwCBQoSRedirectType_Object = MibTableColumn
hwCBQoSRedirectType = _HwCBQoSRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 1),
    _HwCBQoSRedirectType_Type()
)
hwCBQoSRedirectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSRedirectType.setStatus("current")


class _HwCBQoSRedirectIpAddress_Type(OctetString):
    """Custom type hwCBQoSRedirectIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCBQoSRedirectIpAddress_Type.__name__ = "OctetString"
_HwCBQoSRedirectIpAddress_Object = MibTableColumn
hwCBQoSRedirectIpAddress = _HwCBQoSRedirectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 2),
    _HwCBQoSRedirectIpAddress_Type()
)
hwCBQoSRedirectIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectIpAddress.setStatus("current")
_HwCBQoSRedirectIfIndex_Type = Integer32
_HwCBQoSRedirectIfIndex_Object = MibTableColumn
hwCBQoSRedirectIfIndex = _HwCBQoSRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 3),
    _HwCBQoSRedirectIfIndex_Type()
)
hwCBQoSRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectIfIndex.setStatus("current")


class _HwCBQoSRedirectVlanId_Type(Integer32):
    """Custom type hwCBQoSRedirectVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_HwCBQoSRedirectVlanId_Type.__name__ = "Integer32"
_HwCBQoSRedirectVlanId_Object = MibTableColumn
hwCBQoSRedirectVlanId = _HwCBQoSRedirectVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 4),
    _HwCBQoSRedirectVlanId_Type()
)
hwCBQoSRedirectVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectVlanId.setStatus("current")
_HwCBQoSRedirectCtrlType_Type = RedirectCtrlType
_HwCBQoSRedirectCtrlType_Object = MibTableColumn
hwCBQoSRedirectCtrlType = _HwCBQoSRedirectCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 5),
    _HwCBQoSRedirectCtrlType_Type()
)
hwCBQoSRedirectCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectCtrlType.setStatus("current")
_HwCBQoSRedirectRowStatus_Type = RowStatus
_HwCBQoSRedirectRowStatus_Object = MibTableColumn
hwCBQoSRedirectRowStatus = _HwCBQoSRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 6),
    _HwCBQoSRedirectRowStatus_Type()
)
hwCBQoSRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectRowStatus.setStatus("current")


class _HwCBQoSRedirectLSPDstIpAddress_Type(OctetString):
    """Custom type hwCBQoSRedirectLSPDstIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCBQoSRedirectLSPDstIpAddress_Type.__name__ = "OctetString"
_HwCBQoSRedirectLSPDstIpAddress_Object = MibTableColumn
hwCBQoSRedirectLSPDstIpAddress = _HwCBQoSRedirectLSPDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 7),
    _HwCBQoSRedirectLSPDstIpAddress_Type()
)
hwCBQoSRedirectLSPDstIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectLSPDstIpAddress.setStatus("current")


class _HwCBQoSRedirectLSPSecondary_Type(Integer32):
    """Custom type hwCBQoSRedirectLSPSecondary based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupLSPPath", 2),
          ("mainLSPPath", 1),
          ("notConfigLSP", -1))
    )


_HwCBQoSRedirectLSPSecondary_Type.__name__ = "Integer32"
_HwCBQoSRedirectLSPSecondary_Object = MibTableColumn
hwCBQoSRedirectLSPSecondary = _HwCBQoSRedirectLSPSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 15, 1, 8),
    _HwCBQoSRedirectLSPSecondary_Type()
)
hwCBQoSRedirectLSPSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectLSPSecondary.setStatus("current")
_HwCBQoSMirrorCfgInfoTable_Object = MibTable
hwCBQoSMirrorCfgInfoTable = _HwCBQoSMirrorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    hwCBQoSMirrorCfgInfoTable.setStatus("current")
_HwCBQoSMirrorCfgInfoEntry_Object = MibTableRow
hwCBQoSMirrorCfgInfoEntry = _HwCBQoSMirrorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 16, 1)
)
hwCBQoSMirrorCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSMirrorCfgInfoEntry.setStatus("current")


class _HwCBQoSMirrorObserveIndex_Type(Integer32):
    """Custom type hwCBQoSMirrorObserveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwCBQoSMirrorObserveIndex_Type.__name__ = "Integer32"
_HwCBQoSMirrorObserveIndex_Object = MibTableColumn
hwCBQoSMirrorObserveIndex = _HwCBQoSMirrorObserveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 16, 1, 1),
    _HwCBQoSMirrorObserveIndex_Type()
)
hwCBQoSMirrorObserveIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMirrorObserveIndex.setStatus("current")
_HwCBQoSMirrorRowStatus_Type = RowStatus
_HwCBQoSMirrorRowStatus_Object = MibTableColumn
hwCBQoSMirrorRowStatus = _HwCBQoSMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 16, 1, 2),
    _HwCBQoSMirrorRowStatus_Type()
)
hwCBQoSMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMirrorRowStatus.setStatus("current")
_HwCBQoSUrpfCfgInfoTable_Object = MibTable
hwCBQoSUrpfCfgInfoTable = _HwCBQoSUrpfCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 17)
)
if mibBuilder.loadTexts:
    hwCBQoSUrpfCfgInfoTable.setStatus("current")
_HwCBQoSUrpfCfgInfoEntry_Object = MibTableRow
hwCBQoSUrpfCfgInfoEntry = _HwCBQoSUrpfCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 17, 1)
)
hwCBQoSUrpfCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSUrpfCfgInfoEntry.setStatus("current")
_HwCBQoSUrpfCtrlType_Type = UrpfCtrlType
_HwCBQoSUrpfCtrlType_Object = MibTableColumn
hwCBQoSUrpfCtrlType = _HwCBQoSUrpfCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 17, 1, 1),
    _HwCBQoSUrpfCtrlType_Type()
)
hwCBQoSUrpfCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSUrpfCtrlType.setStatus("current")


class _HwCBQoSUrpfAllowDefault_Type(Integer32):
    """Custom type hwCBQoSUrpfAllowDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwCBQoSUrpfAllowDefault_Type.__name__ = "Integer32"
_HwCBQoSUrpfAllowDefault_Object = MibTableColumn
hwCBQoSUrpfAllowDefault = _HwCBQoSUrpfAllowDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 17, 1, 2),
    _HwCBQoSUrpfAllowDefault_Type()
)
hwCBQoSUrpfAllowDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSUrpfAllowDefault.setStatus("current")
_HwCBQoSUrpfRowStatus_Type = RowStatus
_HwCBQoSUrpfRowStatus_Object = MibTableColumn
hwCBQoSUrpfRowStatus = _HwCBQoSUrpfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 17, 1, 3),
    _HwCBQoSUrpfRowStatus_Type()
)
hwCBQoSUrpfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSUrpfRowStatus.setStatus("current")
_HwCBQoSCountCfgInfoTable_Object = MibTable
hwCBQoSCountCfgInfoTable = _HwCBQoSCountCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 18)
)
if mibBuilder.loadTexts:
    hwCBQoSCountCfgInfoTable.setStatus("current")
_HwCBQoSCountCfgInfoEntry_Object = MibTableRow
hwCBQoSCountCfgInfoEntry = _HwCBQoSCountCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 18, 1)
)
hwCBQoSCountCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSCountCfgInfoEntry.setStatus("current")


class _HwCBQoSCountAction_Type(Integer32):
    """Custom type hwCBQoSCountAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("count", 1)
    )


_HwCBQoSCountAction_Type.__name__ = "Integer32"
_HwCBQoSCountAction_Object = MibTableColumn
hwCBQoSCountAction = _HwCBQoSCountAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 18, 1, 1),
    _HwCBQoSCountAction_Type()
)
hwCBQoSCountAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCountAction.setStatus("current")
_HwCBQoSCountRowStatus_Type = RowStatus
_HwCBQoSCountRowStatus_Object = MibTableColumn
hwCBQoSCountRowStatus = _HwCBQoSCountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 18, 1, 2),
    _HwCBQoSCountRowStatus_Type()
)
hwCBQoSCountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCountRowStatus.setStatus("current")
_HwCBQoSHighDropCfgInfoTable_Object = MibTable
hwCBQoSHighDropCfgInfoTable = _HwCBQoSHighDropCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 19)
)
if mibBuilder.loadTexts:
    hwCBQoSHighDropCfgInfoTable.setStatus("current")
_HwCBQoSHighDropCfgInfoEntry_Object = MibTableRow
hwCBQoSHighDropCfgInfoEntry = _HwCBQoSHighDropCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 19, 1)
)
hwCBQoSHighDropCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSHighDropCfgInfoEntry.setStatus("current")


class _HwCBQoSHighDropPrecedence_Type(Integer32):
    """Custom type hwCBQoSHighDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("high", 1)
    )


_HwCBQoSHighDropPrecedence_Type.__name__ = "Integer32"
_HwCBQoSHighDropPrecedence_Object = MibTableColumn
hwCBQoSHighDropPrecedence = _HwCBQoSHighDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 19, 1, 1),
    _HwCBQoSHighDropPrecedence_Type()
)
hwCBQoSHighDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSHighDropPrecedence.setStatus("current")
_HwCBQoSHighDropRowStatus_Type = RowStatus
_HwCBQoSHighDropRowStatus_Object = MibTableColumn
hwCBQoSHighDropRowStatus = _HwCBQoSHighDropRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 19, 1, 2),
    _HwCBQoSHighDropRowStatus_Type()
)
hwCBQoSHighDropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSHighDropRowStatus.setStatus("current")
_HwCBQoSLoadBalanceCfgInfoTable_Object = MibTable
hwCBQoSLoadBalanceCfgInfoTable = _HwCBQoSLoadBalanceCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 20)
)
if mibBuilder.loadTexts:
    hwCBQoSLoadBalanceCfgInfoTable.setStatus("current")
_HwCBQoSLoadBalanceCfgInfoEntry_Object = MibTableRow
hwCBQoSLoadBalanceCfgInfoEntry = _HwCBQoSLoadBalanceCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 20, 1)
)
hwCBQoSLoadBalanceCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSLoadBalanceCfgInfoEntry.setStatus("current")


class _HwCBQoSLoadBalanceType_Type(Integer32):
    """Custom type hwCBQoSLoadBalanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flow", 1),
          ("packet", 2))
    )


_HwCBQoSLoadBalanceType_Type.__name__ = "Integer32"
_HwCBQoSLoadBalanceType_Object = MibTableColumn
hwCBQoSLoadBalanceType = _HwCBQoSLoadBalanceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 20, 1, 1),
    _HwCBQoSLoadBalanceType_Type()
)
hwCBQoSLoadBalanceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLoadBalanceType.setStatus("current")
_HwCBQoSLoadBalanceRowStatus_Type = RowStatus
_HwCBQoSLoadBalanceRowStatus_Object = MibTableColumn
hwCBQoSLoadBalanceRowStatus = _HwCBQoSLoadBalanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 20, 1, 2),
    _HwCBQoSLoadBalanceRowStatus_Type()
)
hwCBQoSLoadBalanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLoadBalanceRowStatus.setStatus("current")
_HwCBQoSEgressGtsCfgInfoTable_Object = MibTable
hwCBQoSEgressGtsCfgInfoTable = _HwCBQoSEgressGtsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 21)
)
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsCfgInfoTable.setStatus("current")
_HwCBQoSEgressGtsCfgInfoEntry_Object = MibTableRow
hwCBQoSEgressGtsCfgInfoEntry = _HwCBQoSEgressGtsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 21, 1)
)
hwCBQoSEgressGtsCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSEgressGtsIfIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsCfgInfoEntry.setStatus("current")
_HwCBQoSEgressGtsIfIndex_Type = InterfaceIndex
_HwCBQoSEgressGtsIfIndex_Object = MibTableColumn
hwCBQoSEgressGtsIfIndex = _HwCBQoSEgressGtsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 21, 1, 1),
    _HwCBQoSEgressGtsIfIndex_Type()
)
hwCBQoSEgressGtsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsIfIndex.setStatus("current")
_HwCBQoSEgressGtsCir_Type = Integer32
_HwCBQoSEgressGtsCir_Object = MibTableColumn
hwCBQoSEgressGtsCir = _HwCBQoSEgressGtsCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 21, 1, 2),
    _HwCBQoSEgressGtsCir_Type()
)
hwCBQoSEgressGtsCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsCir.setStatus("current")
_HwCBQoSEgressGtsPir_Type = Integer32
_HwCBQoSEgressGtsPir_Object = MibTableColumn
hwCBQoSEgressGtsPir = _HwCBQoSEgressGtsPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 21, 1, 3),
    _HwCBQoSEgressGtsPir_Type()
)
hwCBQoSEgressGtsPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsPir.setStatus("current")
_HwCBQoSEgressGtsRowStatus_Type = RowStatus
_HwCBQoSEgressGtsRowStatus_Object = MibTableColumn
hwCBQoSEgressGtsRowStatus = _HwCBQoSEgressGtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 21, 1, 4),
    _HwCBQoSEgressGtsRowStatus_Type()
)
hwCBQoSEgressGtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsRowStatus.setStatus("current")
_HwCBQoSServiceClassCfgInfoTable_Object = MibTable
hwCBQoSServiceClassCfgInfoTable = _HwCBQoSServiceClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 22)
)
if mibBuilder.loadTexts:
    hwCBQoSServiceClassCfgInfoTable.setStatus("current")
_HwCBQoSServiceClassCfgInfoEntry_Object = MibTableRow
hwCBQoSServiceClassCfgInfoEntry = _HwCBQoSServiceClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 22, 1)
)
hwCBQoSServiceClassCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSServiceClassCfgInfoEntry.setStatus("current")
_HwCBQoSServiceClassQueueId_Type = CosType
_HwCBQoSServiceClassQueueId_Object = MibTableColumn
hwCBQoSServiceClassQueueId = _HwCBQoSServiceClassQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 22, 1, 1),
    _HwCBQoSServiceClassQueueId_Type()
)
hwCBQoSServiceClassQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSServiceClassQueueId.setStatus("current")


class _HwCBQoSServiceClassColor_Type(Integer32):
    """Custom type hwCBQoSServiceClassColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwCBQoSServiceClassColor_Type.__name__ = "Integer32"
_HwCBQoSServiceClassColor_Object = MibTableColumn
hwCBQoSServiceClassColor = _HwCBQoSServiceClassColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 22, 1, 2),
    _HwCBQoSServiceClassColor_Type()
)
hwCBQoSServiceClassColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSServiceClassColor.setStatus("current")
_HwCBQoSServiceClassRowStatus_Type = RowStatus
_HwCBQoSServiceClassRowStatus_Object = MibTableColumn
hwCBQoSServiceClassRowStatus = _HwCBQoSServiceClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 22, 1, 3),
    _HwCBQoSServiceClassRowStatus_Type()
)
hwCBQoSServiceClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSServiceClassRowStatus.setStatus("current")
_HwCBQoSServiceClassNoremarkflag_Type = Integer32
_HwCBQoSServiceClassNoremarkflag_Object = MibTableColumn
hwCBQoSServiceClassNoremarkflag = _HwCBQoSServiceClassNoremarkflag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 22, 1, 4),
    _HwCBQoSServiceClassNoremarkflag_Type()
)
hwCBQoSServiceClassNoremarkflag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSServiceClassNoremarkflag.setStatus("current")
_HwCBQoSRedirectMULCfgInfoTable_Object = MibTable
hwCBQoSRedirectMULCfgInfoTable = _HwCBQoSRedirectMULCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23)
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULCfgInfoTable.setStatus("current")
_HwCBQoSRedirectMULCfgInfoEntry_Object = MibTableRow
hwCBQoSRedirectMULCfgInfoEntry = _HwCBQoSRedirectMULCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1)
)
hwCBQoSRedirectMULCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULCfgInfoEntry.setStatus("current")


class _HwCBQoSRedirectMULIpAddress1_Type(OctetString):
    """Custom type hwCBQoSRedirectMULIpAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCBQoSRedirectMULIpAddress1_Type.__name__ = "OctetString"
_HwCBQoSRedirectMULIpAddress1_Object = MibTableColumn
hwCBQoSRedirectMULIpAddress1 = _HwCBQoSRedirectMULIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 1),
    _HwCBQoSRedirectMULIpAddress1_Type()
)
hwCBQoSRedirectMULIpAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIpAddress1.setStatus("current")
_HwCBQoSRedirectMULIfIndex1_Type = Integer32
_HwCBQoSRedirectMULIfIndex1_Object = MibTableColumn
hwCBQoSRedirectMULIfIndex1 = _HwCBQoSRedirectMULIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 2),
    _HwCBQoSRedirectMULIfIndex1_Type()
)
hwCBQoSRedirectMULIfIndex1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIfIndex1.setStatus("current")


class _HwCBQoSRedirectMULIpAddress2_Type(OctetString):
    """Custom type hwCBQoSRedirectMULIpAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCBQoSRedirectMULIpAddress2_Type.__name__ = "OctetString"
_HwCBQoSRedirectMULIpAddress2_Object = MibTableColumn
hwCBQoSRedirectMULIpAddress2 = _HwCBQoSRedirectMULIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 3),
    _HwCBQoSRedirectMULIpAddress2_Type()
)
hwCBQoSRedirectMULIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIpAddress2.setStatus("current")
_HwCBQoSRedirectMULIfIndex2_Type = Integer32
_HwCBQoSRedirectMULIfIndex2_Object = MibTableColumn
hwCBQoSRedirectMULIfIndex2 = _HwCBQoSRedirectMULIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 4),
    _HwCBQoSRedirectMULIfIndex2_Type()
)
hwCBQoSRedirectMULIfIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIfIndex2.setStatus("current")


class _HwCBQoSRedirectMULIpAddress3_Type(OctetString):
    """Custom type hwCBQoSRedirectMULIpAddress3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCBQoSRedirectMULIpAddress3_Type.__name__ = "OctetString"
_HwCBQoSRedirectMULIpAddress3_Object = MibTableColumn
hwCBQoSRedirectMULIpAddress3 = _HwCBQoSRedirectMULIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 5),
    _HwCBQoSRedirectMULIpAddress3_Type()
)
hwCBQoSRedirectMULIpAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIpAddress3.setStatus("current")
_HwCBQoSRedirectMULIfIndex3_Type = Integer32
_HwCBQoSRedirectMULIfIndex3_Object = MibTableColumn
hwCBQoSRedirectMULIfIndex3 = _HwCBQoSRedirectMULIfIndex3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 6),
    _HwCBQoSRedirectMULIfIndex3_Type()
)
hwCBQoSRedirectMULIfIndex3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIfIndex3.setStatus("current")


class _HwCBQoSRedirectMULIpAddress4_Type(OctetString):
    """Custom type hwCBQoSRedirectMULIpAddress4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCBQoSRedirectMULIpAddress4_Type.__name__ = "OctetString"
_HwCBQoSRedirectMULIpAddress4_Object = MibTableColumn
hwCBQoSRedirectMULIpAddress4 = _HwCBQoSRedirectMULIpAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 7),
    _HwCBQoSRedirectMULIpAddress4_Type()
)
hwCBQoSRedirectMULIpAddress4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIpAddress4.setStatus("current")
_HwCBQoSRedirectMULIfIndex4_Type = Integer32
_HwCBQoSRedirectMULIfIndex4_Object = MibTableColumn
hwCBQoSRedirectMULIfIndex4 = _HwCBQoSRedirectMULIfIndex4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 8),
    _HwCBQoSRedirectMULIfIndex4_Type()
)
hwCBQoSRedirectMULIfIndex4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULIfIndex4.setStatus("current")
_HwCBQoSRedirectMULCtrlType_Type = RedirectCtrlType
_HwCBQoSRedirectMULCtrlType_Object = MibTableColumn
hwCBQoSRedirectMULCtrlType = _HwCBQoSRedirectMULCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 9),
    _HwCBQoSRedirectMULCtrlType_Type()
)
hwCBQoSRedirectMULCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULCtrlType.setStatus("current")
_HwCBQoSRedirectMULRowStatus_Type = RowStatus
_HwCBQoSRedirectMULRowStatus_Object = MibTableColumn
hwCBQoSRedirectMULRowStatus = _HwCBQoSRedirectMULRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 23, 1, 10),
    _HwCBQoSRedirectMULRowStatus_Type()
)
hwCBQoSRedirectMULRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectMULRowStatus.setStatus("current")
_HwCBQoSRandomDiscardCfgInfoTable_Object = MibTable
hwCBQoSRandomDiscardCfgInfoTable = _HwCBQoSRandomDiscardCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 24)
)
if mibBuilder.loadTexts:
    hwCBQoSRandomDiscardCfgInfoTable.setStatus("current")
_HwCBQoSRandomDiscardCfgInfoEntry_Object = MibTableRow
hwCBQoSRandomDiscardCfgInfoEntry = _HwCBQoSRandomDiscardCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 24, 1)
)
hwCBQoSRandomDiscardCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSRandomDiscardCfgInfoEntry.setStatus("current")


class _HwCBQoSRandomPercent_Type(Integer32):
    """Custom type hwCBQoSRandomPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_HwCBQoSRandomPercent_Type.__name__ = "Integer32"
_HwCBQoSRandomPercent_Object = MibTableColumn
hwCBQoSRandomPercent = _HwCBQoSRandomPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 24, 1, 1),
    _HwCBQoSRandomPercent_Type()
)
hwCBQoSRandomPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRandomPercent.setStatus("current")
_HwCBQoSRandomDiscardRowStatus_Type = RowStatus
_HwCBQoSRandomDiscardRowStatus_Object = MibTableColumn
hwCBQoSRandomDiscardRowStatus = _HwCBQoSRandomDiscardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 24, 1, 50),
    _HwCBQoSRandomDiscardRowStatus_Type()
)
hwCBQoSRandomDiscardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRandomDiscardRowStatus.setStatus("current")
_HwCBQoSDenyPacketLengthCfgInfoTable_Object = MibTable
hwCBQoSDenyPacketLengthCfgInfoTable = _HwCBQoSDenyPacketLengthCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25)
)
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthCfgInfoTable.setStatus("current")
_HwCBQoSDenyPacketLengthCfgInfoEntry_Object = MibTableRow
hwCBQoSDenyPacketLengthCfgInfoEntry = _HwCBQoSDenyPacketLengthCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25, 1)
)
hwCBQoSDenyPacketLengthCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthCfgInfoEntry.setStatus("current")


class _HwCBQoSDenyPacketLengthOptype_Type(Integer32):
    """Custom type hwCBQoSDenyPacketLengthOptype based on Integer32"""
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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("range", 1))
    )


_HwCBQoSDenyPacketLengthOptype_Type.__name__ = "Integer32"
_HwCBQoSDenyPacketLengthOptype_Object = MibTableColumn
hwCBQoSDenyPacketLengthOptype = _HwCBQoSDenyPacketLengthOptype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25, 1, 1),
    _HwCBQoSDenyPacketLengthOptype_Type()
)
hwCBQoSDenyPacketLengthOptype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthOptype.setStatus("current")


class _HwCBQoSDenyPacketLengthMin_Type(Integer32):
    """Custom type hwCBQoSDenyPacketLengthMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwCBQoSDenyPacketLengthMin_Type.__name__ = "Integer32"
_HwCBQoSDenyPacketLengthMin_Object = MibTableColumn
hwCBQoSDenyPacketLengthMin = _HwCBQoSDenyPacketLengthMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25, 1, 2),
    _HwCBQoSDenyPacketLengthMin_Type()
)
hwCBQoSDenyPacketLengthMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthMin.setStatus("current")


class _HwCBQoSDenyPacketLengthMax_Type(Integer32):
    """Custom type hwCBQoSDenyPacketLengthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwCBQoSDenyPacketLengthMax_Type.__name__ = "Integer32"
_HwCBQoSDenyPacketLengthMax_Object = MibTableColumn
hwCBQoSDenyPacketLengthMax = _HwCBQoSDenyPacketLengthMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25, 1, 3),
    _HwCBQoSDenyPacketLengthMax_Type()
)
hwCBQoSDenyPacketLengthMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthMax.setStatus("current")


class _HwCBQoSDenyPacketLength_Type(Integer32):
    """Custom type hwCBQoSDenyPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwCBQoSDenyPacketLength_Type.__name__ = "Integer32"
_HwCBQoSDenyPacketLength_Object = MibTableColumn
hwCBQoSDenyPacketLength = _HwCBQoSDenyPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25, 1, 4),
    _HwCBQoSDenyPacketLength_Type()
)
hwCBQoSDenyPacketLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLength.setStatus("current")
_HwCBQoSDenyPacketLengthRowStatus_Type = RowStatus
_HwCBQoSDenyPacketLengthRowStatus_Object = MibTableColumn
hwCBQoSDenyPacketLengthRowStatus = _HwCBQoSDenyPacketLengthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 25, 1, 50),
    _HwCBQoSDenyPacketLengthRowStatus_Type()
)
hwCBQoSDenyPacketLengthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthRowStatus.setStatus("current")
_HwCBQoSDAAStatisticsCfgInfoTable_Object = MibTable
hwCBQoSDAAStatisticsCfgInfoTable = _HwCBQoSDAAStatisticsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 26)
)
if mibBuilder.loadTexts:
    hwCBQoSDAAStatisticsCfgInfoTable.setStatus("current")
_HwCBQoSDAAStatisticsCfgInfoEntry_Object = MibTableRow
hwCBQoSDAAStatisticsCfgInfoEntry = _HwCBQoSDAAStatisticsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 26, 1)
)
hwCBQoSDAAStatisticsCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSDAAStatisticsCfgInfoEntry.setStatus("current")


class _HwCBQoSDAAStatisticsSummary_Type(Integer32):
    """Custom type hwCBQoSDAAStatisticsSummary based on Integer32"""
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


_HwCBQoSDAAStatisticsSummary_Type.__name__ = "Integer32"
_HwCBQoSDAAStatisticsSummary_Object = MibTableColumn
hwCBQoSDAAStatisticsSummary = _HwCBQoSDAAStatisticsSummary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 26, 1, 1),
    _HwCBQoSDAAStatisticsSummary_Type()
)
hwCBQoSDAAStatisticsSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDAAStatisticsSummary.setStatus("current")
_HwCBQoSDAAStatisticsRowStatus_Type = RowStatus
_HwCBQoSDAAStatisticsRowStatus_Object = MibTableColumn
hwCBQoSDAAStatisticsRowStatus = _HwCBQoSDAAStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 26, 1, 50),
    _HwCBQoSDAAStatisticsRowStatus_Type()
)
hwCBQoSDAAStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDAAStatisticsRowStatus.setStatus("current")
_HwCBQoSDAATariffLevelCfgInfoTable_Object = MibTable
hwCBQoSDAATariffLevelCfgInfoTable = _HwCBQoSDAATariffLevelCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 27)
)
if mibBuilder.loadTexts:
    hwCBQoSDAATariffLevelCfgInfoTable.setStatus("current")
_HwCBQoSDAATariffLevelCfgInfoEntry_Object = MibTableRow
hwCBQoSDAATariffLevelCfgInfoEntry = _HwCBQoSDAATariffLevelCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 27, 1)
)
hwCBQoSDAATariffLevelCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSDAATariffLevelCfgInfoEntry.setStatus("current")


class _HwCBQoSDAATariffLevelValue_Type(Integer32):
    """Custom type hwCBQoSDAATariffLevelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCBQoSDAATariffLevelValue_Type.__name__ = "Integer32"
_HwCBQoSDAATariffLevelValue_Object = MibTableColumn
hwCBQoSDAATariffLevelValue = _HwCBQoSDAATariffLevelValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 27, 1, 1),
    _HwCBQoSDAATariffLevelValue_Type()
)
hwCBQoSDAATariffLevelValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDAATariffLevelValue.setStatus("current")
_HwCBQoSDAATariffLevelRowStatus_Type = RowStatus
_HwCBQoSDAATariffLevelRowStatus_Object = MibTableColumn
hwCBQoSDAATariffLevelRowStatus = _HwCBQoSDAATariffLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 27, 1, 50),
    _HwCBQoSDAATariffLevelRowStatus_Type()
)
hwCBQoSDAATariffLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDAATariffLevelRowStatus.setStatus("current")
_HwCBQoSRemarkIpDfCfgInfoTable_Object = MibTable
hwCBQoSRemarkIpDfCfgInfoTable = _HwCBQoSRemarkIpDfCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 28)
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkIpDfCfgInfoTable.setStatus("current")
_HwCBQoSRemarkIpDfCfgInfoEntry_Object = MibTableRow
hwCBQoSRemarkIpDfCfgInfoEntry = _HwCBQoSRemarkIpDfCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 28, 1)
)
hwCBQoSRemarkIpDfCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkIpDfCfgInfoEntry.setStatus("current")


class _HwCBQoSRemarkIpDf_Type(Integer32):
    """Custom type hwCBQoSRemarkIpDf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwCBQoSRemarkIpDf_Type.__name__ = "Integer32"
_HwCBQoSRemarkIpDf_Object = MibTableColumn
hwCBQoSRemarkIpDf = _HwCBQoSRemarkIpDf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 28, 1, 1),
    _HwCBQoSRemarkIpDf_Type()
)
hwCBQoSRemarkIpDf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkIpDf.setStatus("current")
_HwCBQoSRemarkIpDfRowStatus_Type = RowStatus
_HwCBQoSRemarkIpDfRowStatus_Object = MibTableColumn
hwCBQoSRemarkIpDfRowStatus = _HwCBQoSRemarkIpDfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 28, 1, 2),
    _HwCBQoSRemarkIpDfRowStatus_Type()
)
hwCBQoSRemarkIpDfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkIpDfRowStatus.setStatus("current")
_HwCBQoSDropProfileCfgInfoTable_Object = MibTable
hwCBQoSDropProfileCfgInfoTable = _HwCBQoSDropProfileCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 29)
)
if mibBuilder.loadTexts:
    hwCBQoSDropProfileCfgInfoTable.setStatus("current")
_HwCBQoSDropProfileCfgInfoEntry_Object = MibTableRow
hwCBQoSDropProfileCfgInfoEntry = _HwCBQoSDropProfileCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 29, 1)
)
hwCBQoSDropProfileCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSDropProfileIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSDropProfileCfgInfoEntry.setStatus("current")
_HwCBQoSDropProfileIndex_Type = Integer32
_HwCBQoSDropProfileIndex_Object = MibTableColumn
hwCBQoSDropProfileIndex = _HwCBQoSDropProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 29, 1, 1),
    _HwCBQoSDropProfileIndex_Type()
)
hwCBQoSDropProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileIndex.setStatus("current")


class _HwCBQoSDropProfileName_Type(OctetString):
    """Custom type hwCBQoSDropProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSDropProfileName_Type.__name__ = "OctetString"
_HwCBQoSDropProfileName_Object = MibTableColumn
hwCBQoSDropProfileName = _HwCBQoSDropProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 29, 1, 2),
    _HwCBQoSDropProfileName_Type()
)
hwCBQoSDropProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileName.setStatus("current")


class _HwCBQoSDropProfileType_Type(Integer32):
    """Custom type hwCBQoSDropProfileType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwCBQoSDropProfileType_Type.__name__ = "Integer32"
_HwCBQoSDropProfileType_Object = MibTableColumn
hwCBQoSDropProfileType = _HwCBQoSDropProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 29, 1, 3),
    _HwCBQoSDropProfileType_Type()
)
hwCBQoSDropProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileType.setStatus("current")
_HwCBQoSDropProfileRowStatus_Type = RowStatus
_HwCBQoSDropProfileRowStatus_Object = MibTableColumn
hwCBQoSDropProfileRowStatus = _HwCBQoSDropProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 29, 1, 4),
    _HwCBQoSDropProfileRowStatus_Type()
)
hwCBQoSDropProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileRowStatus.setStatus("current")
_HwCBQoSDropProfileClassCfgInfoTable_Object = MibTable
hwCBQoSDropProfileClassCfgInfoTable = _HwCBQoSDropProfileClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 30)
)
if mibBuilder.loadTexts:
    hwCBQoSDropProfileClassCfgInfoTable.setStatus("current")
_HwCBQoSDropProfileClassCfgInfoEntry_Object = MibTableRow
hwCBQoSDropProfileClassCfgInfoEntry = _HwCBQoSDropProfileClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 30, 1)
)
hwCBQoSDropProfileClassCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSDropProfileIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSDropProfileClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSDropProfileClassCfgInfoEntry.setStatus("current")


class _HwCBQoSDropProfileClassValue_Type(Integer32):
    """Custom type hwCBQoSDropProfileClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwCBQoSDropProfileClassValue_Type.__name__ = "Integer32"
_HwCBQoSDropProfileClassValue_Object = MibTableColumn
hwCBQoSDropProfileClassValue = _HwCBQoSDropProfileClassValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 30, 1, 1),
    _HwCBQoSDropProfileClassValue_Type()
)
hwCBQoSDropProfileClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileClassValue.setStatus("current")


class _HwCBQoSDropProfileLowLimit_Type(Integer32):
    """Custom type hwCBQoSDropProfileLowLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCBQoSDropProfileLowLimit_Type.__name__ = "Integer32"
_HwCBQoSDropProfileLowLimit_Object = MibTableColumn
hwCBQoSDropProfileLowLimit = _HwCBQoSDropProfileLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 30, 1, 2),
    _HwCBQoSDropProfileLowLimit_Type()
)
hwCBQoSDropProfileLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileLowLimit.setStatus("current")


class _HwCBQoSDropProfileHighLimit_Type(Integer32):
    """Custom type hwCBQoSDropProfileHighLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCBQoSDropProfileHighLimit_Type.__name__ = "Integer32"
_HwCBQoSDropProfileHighLimit_Object = MibTableColumn
hwCBQoSDropProfileHighLimit = _HwCBQoSDropProfileHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 30, 1, 3),
    _HwCBQoSDropProfileHighLimit_Type()
)
hwCBQoSDropProfileHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileHighLimit.setStatus("current")


class _HwCBQoSDropProfileDiscardProb_Type(Integer32):
    """Custom type hwCBQoSDropProfileDiscardProb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCBQoSDropProfileDiscardProb_Type.__name__ = "Integer32"
_HwCBQoSDropProfileDiscardProb_Object = MibTableColumn
hwCBQoSDropProfileDiscardProb = _HwCBQoSDropProfileDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 30, 1, 4),
    _HwCBQoSDropProfileDiscardProb_Type()
)
hwCBQoSDropProfileDiscardProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSDropProfileDiscardProb.setStatus("current")
_HwCBQoSRedirectVsiTable_Object = MibTable
hwCBQoSRedirectVsiTable = _HwCBQoSRedirectVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 31)
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectVsiTable.setStatus("current")
_HwCBQoSRedirectVsiEntry_Object = MibTableRow
hwCBQoSRedirectVsiEntry = _HwCBQoSRedirectVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 31, 1)
)
hwCBQoSRedirectVsiEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectVsiEntry.setStatus("current")


class _HwCBQoSRedirectVsiName_Type(OctetString):
    """Custom type hwCBQoSRedirectVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSRedirectVsiName_Type.__name__ = "OctetString"
_HwCBQoSRedirectVsiName_Object = MibTableColumn
hwCBQoSRedirectVsiName = _HwCBQoSRedirectVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 31, 1, 1),
    _HwCBQoSRedirectVsiName_Type()
)
hwCBQoSRedirectVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectVsiName.setStatus("current")
_HwCBQoSRedirectVsiRowStatus_Type = RowStatus
_HwCBQoSRedirectVsiRowStatus_Object = MibTableColumn
hwCBQoSRedirectVsiRowStatus = _HwCBQoSRedirectVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 31, 1, 2),
    _HwCBQoSRedirectVsiRowStatus_Type()
)
hwCBQoSRedirectVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRedirectVsiRowStatus.setStatus("current")
_HwCBQoSSuppressionCfgInfoTable_Object = MibTable
hwCBQoSSuppressionCfgInfoTable = _HwCBQoSSuppressionCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32)
)
if mibBuilder.loadTexts:
    hwCBQoSSuppressionCfgInfoTable.setStatus("current")
_HwCBQoSSuppressionCfgInfoEntry_Object = MibTableRow
hwCBQoSSuppressionCfgInfoEntry = _HwCBQoSSuppressionCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1)
)
hwCBQoSSuppressionCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSSuppressionCfgInfoEntry.setStatus("current")


class _HwCBQoSSuppressionType_Type(Integer32):
    """Custom type hwCBQoSSuppressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unkonwnunicast", 3))
    )


_HwCBQoSSuppressionType_Type.__name__ = "Integer32"
_HwCBQoSSuppressionType_Object = MibTableColumn
hwCBQoSSuppressionType = _HwCBQoSSuppressionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 1),
    _HwCBQoSSuppressionType_Type()
)
hwCBQoSSuppressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionType.setStatus("current")
_HwCBQoSSuppressionCir_Type = Integer32
_HwCBQoSSuppressionCir_Object = MibTableColumn
hwCBQoSSuppressionCir = _HwCBQoSSuppressionCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 2),
    _HwCBQoSSuppressionCir_Type()
)
hwCBQoSSuppressionCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionCir.setStatus("current")
_HwCBQoSSuppressionCbs_Type = Integer32
_HwCBQoSSuppressionCbs_Object = MibTableColumn
hwCBQoSSuppressionCbs = _HwCBQoSSuppressionCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 3),
    _HwCBQoSSuppressionCbs_Type()
)
hwCBQoSSuppressionCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionCbs.setStatus("current")


class _HwCBQoSSuppressionGreenAction_Type(CarAction):
    """Custom type hwCBQoSSuppressionGreenAction based on CarAction"""


_HwCBQoSSuppressionGreenAction_Object = MibTableColumn
hwCBQoSSuppressionGreenAction = _HwCBQoSSuppressionGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 4),
    _HwCBQoSSuppressionGreenAction_Type()
)
hwCBQoSSuppressionGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionGreenAction.setStatus("current")


class _HwCBQoSSuppressionGreenRemarkValue_Type(Integer32):
    """Custom type hwCBQoSSuppressionGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(11, 81),
    )


_HwCBQoSSuppressionGreenRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSSuppressionGreenRemarkValue_Object = MibTableColumn
hwCBQoSSuppressionGreenRemarkValue = _HwCBQoSSuppressionGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 5),
    _HwCBQoSSuppressionGreenRemarkValue_Type()
)
hwCBQoSSuppressionGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionGreenRemarkValue.setStatus("current")


class _HwCBQoSSuppressionRedAction_Type(CarAction):
    """Custom type hwCBQoSSuppressionRedAction based on CarAction"""


_HwCBQoSSuppressionRedAction_Object = MibTableColumn
hwCBQoSSuppressionRedAction = _HwCBQoSSuppressionRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 6),
    _HwCBQoSSuppressionRedAction_Type()
)
hwCBQoSSuppressionRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionRedAction.setStatus("current")


class _HwCBQoSSuppressionRedRemarkValue_Type(Integer32):
    """Custom type hwCBQoSSuppressionRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(11, 81),
    )


_HwCBQoSSuppressionRedRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSSuppressionRedRemarkValue_Object = MibTableColumn
hwCBQoSSuppressionRedRemarkValue = _HwCBQoSSuppressionRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 7),
    _HwCBQoSSuppressionRedRemarkValue_Type()
)
hwCBQoSSuppressionRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionRedRemarkValue.setStatus("current")
_HwCBQoSSuppressionRowStatus_Type = RowStatus
_HwCBQoSSuppressionRowStatus_Object = MibTableColumn
hwCBQoSSuppressionRowStatus = _HwCBQoSSuppressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 2, 32, 1, 8),
    _HwCBQoSSuppressionRowStatus_Type()
)
hwCBQoSSuppressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSuppressionRowStatus.setStatus("current")
_HwCBQoSPolicyObjects_ObjectIdentity = ObjectIdentity
hwCBQoSPolicyObjects = _HwCBQoSPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3)
)
_HwCBQoSPolicyIndexNext_Type = Integer32
_HwCBQoSPolicyIndexNext_Object = MibScalar
hwCBQoSPolicyIndexNext = _HwCBQoSPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 1),
    _HwCBQoSPolicyIndexNext_Type()
)
hwCBQoSPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyIndexNext.setStatus("current")
_HwCBQoSPolicyCfgInfoTable_Object = MibTable
hwCBQoSPolicyCfgInfoTable = _HwCBQoSPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyCfgInfoTable.setStatus("current")
_HwCBQoSPolicyCfgInfoEntry_Object = MibTableRow
hwCBQoSPolicyCfgInfoEntry = _HwCBQoSPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1)
)
hwCBQoSPolicyCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyCfgInfoEntry.setStatus("current")
_HwCBQoSPolicyIndex_Type = Integer32
_HwCBQoSPolicyIndex_Object = MibTableColumn
hwCBQoSPolicyIndex = _HwCBQoSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 1),
    _HwCBQoSPolicyIndex_Type()
)
hwCBQoSPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyIndex.setStatus("current")


class _HwCBQoSPolicyName_Type(OctetString):
    """Custom type hwCBQoSPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSPolicyName_Type.__name__ = "OctetString"
_HwCBQoSPolicyName_Object = MibTableColumn
hwCBQoSPolicyName = _HwCBQoSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 2),
    _HwCBQoSPolicyName_Type()
)
hwCBQoSPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyName.setStatus("current")
_HwCBQoSPolicyClassCount_Type = Integer32
_HwCBQoSPolicyClassCount_Object = MibTableColumn
hwCBQoSPolicyClassCount = _HwCBQoSPolicyClassCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 3),
    _HwCBQoSPolicyClassCount_Type()
)
hwCBQoSPolicyClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassCount.setStatus("current")


class _HwCBQoSPolicyConfigMode_Type(Integer32):
    """Custom type hwCBQoSPolicyConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1),
          ("unavailable", -1))
    )


_HwCBQoSPolicyConfigMode_Type.__name__ = "Integer32"
_HwCBQoSPolicyConfigMode_Object = MibTableColumn
hwCBQoSPolicyConfigMode = _HwCBQoSPolicyConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 4),
    _HwCBQoSPolicyConfigMode_Type()
)
hwCBQoSPolicyConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyConfigMode.setStatus("current")
_HwCBQoSPolicyRowStatus_Type = RowStatus
_HwCBQoSPolicyRowStatus_Object = MibTableColumn
hwCBQoSPolicyRowStatus = _HwCBQoSPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 5),
    _HwCBQoSPolicyRowStatus_Type()
)
hwCBQoSPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyRowStatus.setStatus("current")


class _HwCBQoSPolicyShareFlag_Type(Integer32):
    """Custom type hwCBQoSPolicyShareFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 1),
          ("single", 2))
    )


_HwCBQoSPolicyShareFlag_Type.__name__ = "Integer32"
_HwCBQoSPolicyShareFlag_Object = MibTableColumn
hwCBQoSPolicyShareFlag = _HwCBQoSPolicyShareFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 6),
    _HwCBQoSPolicyShareFlag_Type()
)
hwCBQoSPolicyShareFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyShareFlag.setStatus("current")


class _HwCBQoSPolicyStatisticsFlag_Type(EnabledStatus):
    """Custom type hwCBQoSPolicyStatisticsFlag based on EnabledStatus"""


_HwCBQoSPolicyStatisticsFlag_Object = MibTableColumn
hwCBQoSPolicyStatisticsFlag = _HwCBQoSPolicyStatisticsFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 2, 1, 7),
    _HwCBQoSPolicyStatisticsFlag_Type()
)
hwCBQoSPolicyStatisticsFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsFlag.setStatus("current")
_HwCBQoSPolicyClassCfgInfoTable_Object = MibTable
hwCBQoSPolicyClassCfgInfoTable = _HwCBQoSPolicyClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassCfgInfoTable.setStatus("current")
_HwCBQoSPolicyClassCfgInfoEntry_Object = MibTableRow
hwCBQoSPolicyClassCfgInfoEntry = _HwCBQoSPolicyClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1)
)
hwCBQoSPolicyClassCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassCfgInfoEntry.setStatus("current")
_HwCBQoSPolicyClassIndex_Type = Integer32
_HwCBQoSPolicyClassIndex_Object = MibTableColumn
hwCBQoSPolicyClassIndex = _HwCBQoSPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 1),
    _HwCBQoSPolicyClassIndex_Type()
)
hwCBQoSPolicyClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassIndex.setStatus("current")
_HwCBQoSPolicyClassClassifierIndex_Type = Integer32
_HwCBQoSPolicyClassClassifierIndex_Object = MibTableColumn
hwCBQoSPolicyClassClassifierIndex = _HwCBQoSPolicyClassClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 2),
    _HwCBQoSPolicyClassClassifierIndex_Type()
)
hwCBQoSPolicyClassClassifierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassClassifierIndex.setStatus("current")


class _HwCBQoSPolicyClassClassifierName_Type(OctetString):
    """Custom type hwCBQoSPolicyClassClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSPolicyClassClassifierName_Type.__name__ = "OctetString"
_HwCBQoSPolicyClassClassifierName_Object = MibTableColumn
hwCBQoSPolicyClassClassifierName = _HwCBQoSPolicyClassClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 3),
    _HwCBQoSPolicyClassClassifierName_Type()
)
hwCBQoSPolicyClassClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassClassifierName.setStatus("current")
_HwCBQoSPolicyClassBehaviorIndex_Type = Integer32
_HwCBQoSPolicyClassBehaviorIndex_Object = MibTableColumn
hwCBQoSPolicyClassBehaviorIndex = _HwCBQoSPolicyClassBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 4),
    _HwCBQoSPolicyClassBehaviorIndex_Type()
)
hwCBQoSPolicyClassBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassBehaviorIndex.setStatus("current")


class _HwCBQoSPolicyClassBehaviorName_Type(OctetString):
    """Custom type hwCBQoSPolicyClassBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSPolicyClassBehaviorName_Type.__name__ = "OctetString"
_HwCBQoSPolicyClassBehaviorName_Object = MibTableColumn
hwCBQoSPolicyClassBehaviorName = _HwCBQoSPolicyClassBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 5),
    _HwCBQoSPolicyClassBehaviorName_Type()
)
hwCBQoSPolicyClassBehaviorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassBehaviorName.setStatus("current")


class _HwCBQoSPolicyClassPrecedence_Type(Integer32):
    """Custom type hwCBQoSPolicyClassPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_HwCBQoSPolicyClassPrecedence_Type.__name__ = "Integer32"
_HwCBQoSPolicyClassPrecedence_Object = MibTableColumn
hwCBQoSPolicyClassPrecedence = _HwCBQoSPolicyClassPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 6),
    _HwCBQoSPolicyClassPrecedence_Type()
)
hwCBQoSPolicyClassPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassPrecedence.setStatus("current")
_HwCBQoSPolicyClassRowStatus_Type = RowStatus
_HwCBQoSPolicyClassRowStatus_Object = MibTableColumn
hwCBQoSPolicyClassRowStatus = _HwCBQoSPolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 3, 1, 7),
    _HwCBQoSPolicyClassRowStatus_Type()
)
hwCBQoSPolicyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassRowStatus.setStatus("current")
_HwCBQoSPolicyShareModeCfgInfoTable_Object = MibTable
hwCBQoSPolicyShareModeCfgInfoTable = _HwCBQoSPolicyShareModeCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyShareModeCfgInfoTable.setStatus("current")
_HwCBQoSPolicyShareModeCfgInfoEntry_Object = MibTableRow
hwCBQoSPolicyShareModeCfgInfoEntry = _HwCBQoSPolicyShareModeCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 4, 1)
)
hwCBQoSPolicyShareModeCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyShareModeCfgInfoEntry.setStatus("current")


class _HwCBQoSPolicyShareModeFlag_Type(EnabledStatus):
    """Custom type hwCBQoSPolicyShareModeFlag based on EnabledStatus"""


_HwCBQoSPolicyShareModeFlag_Object = MibTableColumn
hwCBQoSPolicyShareModeFlag = _HwCBQoSPolicyShareModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 4, 1, 1),
    _HwCBQoSPolicyShareModeFlag_Type()
)
hwCBQoSPolicyShareModeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyShareModeFlag.setStatus("current")
_HwCBQoSPolicyShareModeRowStatus_Type = RowStatus
_HwCBQoSPolicyShareModeRowStatus_Object = MibTableColumn
hwCBQoSPolicyShareModeRowStatus = _HwCBQoSPolicyShareModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 3, 4, 1, 2),
    _HwCBQoSPolicyShareModeRowStatus_Type()
)
hwCBQoSPolicyShareModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyShareModeRowStatus.setStatus("current")
_HwCBQoSApplyPolicyObjects_ObjectIdentity = ObjectIdentity
hwCBQoSApplyPolicyObjects = _HwCBQoSApplyPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4)
)
_HwCBQoSIfApplyPolicyTable_Object = MibTable
hwCBQoSIfApplyPolicyTable = _HwCBQoSIfApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyTable.setStatus("current")
_HwCBQoSIfApplyPolicyEntry_Object = MibTableRow
hwCBQoSIfApplyPolicyEntry = _HwCBQoSIfApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1, 1)
)
hwCBQoSIfApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyEntry.setStatus("current")
_HwCBQoSIfApplyPolicyIfIndex_Type = Integer32
_HwCBQoSIfApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSIfApplyPolicyIfIndex = _HwCBQoSIfApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1, 1, 1),
    _HwCBQoSIfApplyPolicyIfIndex_Type()
)
hwCBQoSIfApplyPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyIfIndex.setStatus("current")
_HwCBQoSIfApplyPolicyDirection_Type = DirectionType
_HwCBQoSIfApplyPolicyDirection_Object = MibTableColumn
hwCBQoSIfApplyPolicyDirection = _HwCBQoSIfApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1, 1, 2),
    _HwCBQoSIfApplyPolicyDirection_Type()
)
hwCBQoSIfApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyDirection.setStatus("current")


class _HwCBQoSIfApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSIfApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSIfApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSIfApplyPolicyName_Object = MibTableColumn
hwCBQoSIfApplyPolicyName = _HwCBQoSIfApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1, 1, 3),
    _HwCBQoSIfApplyPolicyName_Type()
)
hwCBQoSIfApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyName.setStatus("current")
_HwCBQoSIfApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSIfApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSIfApplyPolicyRowStatus = _HwCBQoSIfApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1, 1, 4),
    _HwCBQoSIfApplyPolicyRowStatus_Type()
)
hwCBQoSIfApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyRowStatus.setStatus("current")


class _HwCBQoSIfApplyPolicyLinkLayer_Type(Integer32):
    """Custom type hwCBQoSIfApplyPolicyLinkLayer based on Integer32"""
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
        *(("alllayer", 2),
          ("iplayer", 3),
          ("linklayer", 1),
          ("mplslayer", 4))
    )


_HwCBQoSIfApplyPolicyLinkLayer_Type.__name__ = "Integer32"
_HwCBQoSIfApplyPolicyLinkLayer_Object = MibTableColumn
hwCBQoSIfApplyPolicyLinkLayer = _HwCBQoSIfApplyPolicyLinkLayer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 1, 1, 5),
    _HwCBQoSIfApplyPolicyLinkLayer_Type()
)
hwCBQoSIfApplyPolicyLinkLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyLinkLayer.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyTable_Object = MibTable
hwCBQoSAtmPvcApplyPolicyTable = _HwCBQoSAtmPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyTable.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyEntry_Object = MibTableRow
hwCBQoSAtmPvcApplyPolicyEntry = _HwCBQoSAtmPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1)
)
hwCBQoSAtmPvcApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyEntry.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyIfIndex_Type = Integer32
_HwCBQoSAtmPvcApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyIfIndex = _HwCBQoSAtmPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1, 1),
    _HwCBQoSAtmPvcApplyPolicyIfIndex_Type()
)
hwCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyIfIndex.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyVPI_Type = Integer32
_HwCBQoSAtmPvcApplyPolicyVPI_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyVPI = _HwCBQoSAtmPvcApplyPolicyVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1, 2),
    _HwCBQoSAtmPvcApplyPolicyVPI_Type()
)
hwCBQoSAtmPvcApplyPolicyVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyVPI.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyVCI_Type = Integer32
_HwCBQoSAtmPvcApplyPolicyVCI_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyVCI = _HwCBQoSAtmPvcApplyPolicyVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1, 3),
    _HwCBQoSAtmPvcApplyPolicyVCI_Type()
)
hwCBQoSAtmPvcApplyPolicyVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyVCI.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyDirection_Type = DirectionType
_HwCBQoSAtmPvcApplyPolicyDirection_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyDirection = _HwCBQoSAtmPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1, 4),
    _HwCBQoSAtmPvcApplyPolicyDirection_Type()
)
hwCBQoSAtmPvcApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyDirection.setStatus("current")


class _HwCBQoSAtmPvcApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSAtmPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSAtmPvcApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSAtmPvcApplyPolicyName_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyName = _HwCBQoSAtmPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1, 5),
    _HwCBQoSAtmPvcApplyPolicyName_Type()
)
hwCBQoSAtmPvcApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyName.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSAtmPvcApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyRowStatus = _HwCBQoSAtmPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 2, 1, 6),
    _HwCBQoSAtmPvcApplyPolicyRowStatus_Type()
)
hwCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyRowStatus.setStatus("current")
_HwCBQoSIfVlanApplyPolicyTable_Object = MibTable
hwCBQoSIfVlanApplyPolicyTable = _HwCBQoSIfVlanApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyTable.setStatus("current")
_HwCBQoSIfVlanApplyPolicyEntry_Object = MibTableRow
hwCBQoSIfVlanApplyPolicyEntry = _HwCBQoSIfVlanApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1)
)
hwCBQoSIfVlanApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid2"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyEntry.setStatus("current")
_HwCBQoSIfVlanApplyPolicyIfIndex_Type = Integer32
_HwCBQoSIfVlanApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyIfIndex = _HwCBQoSIfVlanApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 1),
    _HwCBQoSIfVlanApplyPolicyIfIndex_Type()
)
hwCBQoSIfVlanApplyPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyIfIndex.setStatus("current")
_HwCBQoSIfVlanApplyPolicyDirection_Type = DirectionType
_HwCBQoSIfVlanApplyPolicyDirection_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyDirection = _HwCBQoSIfVlanApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 2),
    _HwCBQoSIfVlanApplyPolicyDirection_Type()
)
hwCBQoSIfVlanApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyDirection.setStatus("current")
_HwCBQoSIfVlanApplyPolicyVlanid1_Type = Integer32
_HwCBQoSIfVlanApplyPolicyVlanid1_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyVlanid1 = _HwCBQoSIfVlanApplyPolicyVlanid1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 3),
    _HwCBQoSIfVlanApplyPolicyVlanid1_Type()
)
hwCBQoSIfVlanApplyPolicyVlanid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyVlanid1.setStatus("current")
_HwCBQoSIfVlanApplyPolicyVlanid2_Type = Integer32
_HwCBQoSIfVlanApplyPolicyVlanid2_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyVlanid2 = _HwCBQoSIfVlanApplyPolicyVlanid2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 4),
    _HwCBQoSIfVlanApplyPolicyVlanid2_Type()
)
hwCBQoSIfVlanApplyPolicyVlanid2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyVlanid2.setStatus("current")
_HwCBQoSIfVlanApplyPolicyCeVidEnd_Type = Integer32
_HwCBQoSIfVlanApplyPolicyCeVidEnd_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyCeVidEnd = _HwCBQoSIfVlanApplyPolicyCeVidEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 5),
    _HwCBQoSIfVlanApplyPolicyCeVidEnd_Type()
)
hwCBQoSIfVlanApplyPolicyCeVidEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyCeVidEnd.setStatus("current")


class _HwCBQoSIfVlanApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSIfVlanApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSIfVlanApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSIfVlanApplyPolicyName_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyName = _HwCBQoSIfVlanApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 6),
    _HwCBQoSIfVlanApplyPolicyName_Type()
)
hwCBQoSIfVlanApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyName.setStatus("current")
_HwCBQoSIfVlanApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSIfVlanApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyRowStatus = _HwCBQoSIfVlanApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 7),
    _HwCBQoSIfVlanApplyPolicyRowStatus_Type()
)
hwCBQoSIfVlanApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyRowStatus.setStatus("current")


class _HwCBQoSIfVlanApplyPolicyLinkLayer_Type(Integer32):
    """Custom type hwCBQoSIfVlanApplyPolicyLinkLayer based on Integer32"""
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
        *(("alllayer", 2),
          ("iplayer", 3),
          ("linklayer", 1),
          ("mplslayer", 4))
    )


_HwCBQoSIfVlanApplyPolicyLinkLayer_Type.__name__ = "Integer32"
_HwCBQoSIfVlanApplyPolicyLinkLayer_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyLinkLayer = _HwCBQoSIfVlanApplyPolicyLinkLayer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 3, 1, 8),
    _HwCBQoSIfVlanApplyPolicyLinkLayer_Type()
)
hwCBQoSIfVlanApplyPolicyLinkLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyLinkLayer.setStatus("current")
_HwCBQoSFrClassApplyPolicyTable_Object = MibTable
hwCBQoSFrClassApplyPolicyTable = _HwCBQoSFrClassApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyTable.setStatus("current")
_HwCBQoSFrClassApplyPolicyEntry_Object = MibTableRow
hwCBQoSFrClassApplyPolicyEntry = _HwCBQoSFrClassApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 4, 1)
)
hwCBQoSFrClassApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyFrClassName"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyEntry.setStatus("current")


class _HwCBQoSFrClassApplyPolicyFrClassName_Type(OctetString):
    """Custom type hwCBQoSFrClassApplyPolicyFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSFrClassApplyPolicyFrClassName_Type.__name__ = "OctetString"
_HwCBQoSFrClassApplyPolicyFrClassName_Object = MibTableColumn
hwCBQoSFrClassApplyPolicyFrClassName = _HwCBQoSFrClassApplyPolicyFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 4, 1, 1),
    _HwCBQoSFrClassApplyPolicyFrClassName_Type()
)
hwCBQoSFrClassApplyPolicyFrClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyFrClassName.setStatus("current")
_HwCBQoSFrClassApplyPolicyDirection_Type = DirectionType
_HwCBQoSFrClassApplyPolicyDirection_Object = MibTableColumn
hwCBQoSFrClassApplyPolicyDirection = _HwCBQoSFrClassApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 4, 1, 2),
    _HwCBQoSFrClassApplyPolicyDirection_Type()
)
hwCBQoSFrClassApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyDirection.setStatus("current")


class _HwCBQoSFrClassApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSFrClassApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSFrClassApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSFrClassApplyPolicyName_Object = MibTableColumn
hwCBQoSFrClassApplyPolicyName = _HwCBQoSFrClassApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 4, 1, 3),
    _HwCBQoSFrClassApplyPolicyName_Type()
)
hwCBQoSFrClassApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyName.setStatus("current")
_HwCBQoSFrClassApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSFrClassApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSFrClassApplyPolicyRowStatus = _HwCBQoSFrClassApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 4, 1, 4),
    _HwCBQoSFrClassApplyPolicyRowStatus_Type()
)
hwCBQoSFrClassApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyRowStatus.setStatus("current")
_HwCBQoSFrPvcApplyPolicyTable_Object = MibTable
hwCBQoSFrPvcApplyPolicyTable = _HwCBQoSFrPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyTable.setStatus("current")
_HwCBQoSFrPvcApplyPolicyEntry_Object = MibTableRow
hwCBQoSFrPvcApplyPolicyEntry = _HwCBQoSFrPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 5, 1)
)
hwCBQoSFrPvcApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyEntry.setStatus("current")
_HwCBQoSFrPvcApplyPolicyIfIndex_Type = Integer32
_HwCBQoSFrPvcApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSFrPvcApplyPolicyIfIndex = _HwCBQoSFrPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 5, 1, 1),
    _HwCBQoSFrPvcApplyPolicyIfIndex_Type()
)
hwCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyIfIndex.setStatus("current")


class _HwCBQoSFrPvcApplyPolicyDlciNum_Type(Integer32):
    """Custom type hwCBQoSFrPvcApplyPolicyDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_HwCBQoSFrPvcApplyPolicyDlciNum_Type.__name__ = "Integer32"
_HwCBQoSFrPvcApplyPolicyDlciNum_Object = MibTableColumn
hwCBQoSFrPvcApplyPolicyDlciNum = _HwCBQoSFrPvcApplyPolicyDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 5, 1, 2),
    _HwCBQoSFrPvcApplyPolicyDlciNum_Type()
)
hwCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyDlciNum.setStatus("current")
_HwCBQoSFrPvcApplyPolicyDirection_Type = DirectionType
_HwCBQoSFrPvcApplyPolicyDirection_Object = MibTableColumn
hwCBQoSFrPvcApplyPolicyDirection = _HwCBQoSFrPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 5, 1, 3),
    _HwCBQoSFrPvcApplyPolicyDirection_Type()
)
hwCBQoSFrPvcApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyDirection.setStatus("current")


class _HwCBQoSFrPvcApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSFrPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSFrPvcApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSFrPvcApplyPolicyName_Object = MibTableColumn
hwCBQoSFrPvcApplyPolicyName = _HwCBQoSFrPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 5, 1, 4),
    _HwCBQoSFrPvcApplyPolicyName_Type()
)
hwCBQoSFrPvcApplyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyName.setStatus("current")
_HwCBQoSVsiApplyPolicyTable_Object = MibTable
hwCBQoSVsiApplyPolicyTable = _HwCBQoSVsiApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSVsiApplyPolicyTable.setStatus("current")
_HwCBQoSVsiApplyPolicyEntry_Object = MibTableRow
hwCBQoSVsiApplyPolicyEntry = _HwCBQoSVsiApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6, 1)
)
hwCBQoSVsiApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVsiApplyPolicyVsiIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVsiApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSVsiApplyPolicyEntry.setStatus("current")
_HwCBQoSVsiApplyPolicyVsiIndex_Type = Integer32
_HwCBQoSVsiApplyPolicyVsiIndex_Object = MibTableColumn
hwCBQoSVsiApplyPolicyVsiIndex = _HwCBQoSVsiApplyPolicyVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6, 1, 1),
    _HwCBQoSVsiApplyPolicyVsiIndex_Type()
)
hwCBQoSVsiApplyPolicyVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVsiApplyPolicyVsiIndex.setStatus("current")


class _HwCBQoSVsiName_Type(OctetString):
    """Custom type hwCBQoSVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSVsiName_Type.__name__ = "OctetString"
_HwCBQoSVsiName_Object = MibTableColumn
hwCBQoSVsiName = _HwCBQoSVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6, 1, 2),
    _HwCBQoSVsiName_Type()
)
hwCBQoSVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSVsiName.setStatus("current")
_HwCBQoSVsiApplyPolicyDirection_Type = DirectionType
_HwCBQoSVsiApplyPolicyDirection_Object = MibTableColumn
hwCBQoSVsiApplyPolicyDirection = _HwCBQoSVsiApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6, 1, 3),
    _HwCBQoSVsiApplyPolicyDirection_Type()
)
hwCBQoSVsiApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVsiApplyPolicyDirection.setStatus("current")


class _HwCBQoSVsiApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSVsiApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSVsiApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSVsiApplyPolicyName_Object = MibTableColumn
hwCBQoSVsiApplyPolicyName = _HwCBQoSVsiApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6, 1, 4),
    _HwCBQoSVsiApplyPolicyName_Type()
)
hwCBQoSVsiApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSVsiApplyPolicyName.setStatus("current")
_HwCBQoSVsiApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSVsiApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSVsiApplyPolicyRowStatus = _HwCBQoSVsiApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 6, 1, 5),
    _HwCBQoSVsiApplyPolicyRowStatus_Type()
)
hwCBQoSVsiApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSVsiApplyPolicyRowStatus.setStatus("current")
_HwCBQoSVlanApplyPolicyTable_Object = MibTable
hwCBQoSVlanApplyPolicyTable = _HwCBQoSVlanApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyTable.setStatus("current")
_HwCBQoSVlanApplyPolicyEntry_Object = MibTableRow
hwCBQoSVlanApplyPolicyEntry = _HwCBQoSVlanApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 7, 1)
)
hwCBQoSVlanApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyVlanId"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyEntry.setStatus("current")


class _HwCBQoSVlanApplyPolicyVlanId_Type(Integer32):
    """Custom type hwCBQoSVlanApplyPolicyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwCBQoSVlanApplyPolicyVlanId_Type.__name__ = "Integer32"
_HwCBQoSVlanApplyPolicyVlanId_Object = MibTableColumn
hwCBQoSVlanApplyPolicyVlanId = _HwCBQoSVlanApplyPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 7, 1, 1),
    _HwCBQoSVlanApplyPolicyVlanId_Type()
)
hwCBQoSVlanApplyPolicyVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyVlanId.setStatus("current")


class _HwCBQoSVlanApplyPolicyDirection_Type(Integer32):
    """Custom type hwCBQoSVlanApplyPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwCBQoSVlanApplyPolicyDirection_Type.__name__ = "Integer32"
_HwCBQoSVlanApplyPolicyDirection_Object = MibTableColumn
hwCBQoSVlanApplyPolicyDirection = _HwCBQoSVlanApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 7, 1, 2),
    _HwCBQoSVlanApplyPolicyDirection_Type()
)
hwCBQoSVlanApplyPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyDirection.setStatus("current")


class _HwCBQoSVlanApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSVlanApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSVlanApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSVlanApplyPolicyName_Object = MibTableColumn
hwCBQoSVlanApplyPolicyName = _HwCBQoSVlanApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 7, 1, 3),
    _HwCBQoSVlanApplyPolicyName_Type()
)
hwCBQoSVlanApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyName.setStatus("current")
_HwCBQoSVlanApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSVlanApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSVlanApplyPolicyRowStatus = _HwCBQoSVlanApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 7, 1, 4),
    _HwCBQoSVlanApplyPolicyRowStatus_Type()
)
hwCBQoSVlanApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyRowStatus.setStatus("current")
_HwCBQoSRuleNotSupportAlarmTable_Object = MibTable
hwCBQoSRuleNotSupportAlarmTable = _HwCBQoSRuleNotSupportAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSRuleNotSupportAlarmTable.setStatus("current")
_HwCBQoSRuleNotSupportAlarmEntry_Object = MibTableRow
hwCBQoSRuleNotSupportAlarmEntry = _HwCBQoSRuleNotSupportAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 8, 1)
)
hwCBQoSRuleNotSupportAlarmEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSRuleDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSRuleSlotID"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSRuleInfo"),
)
if mibBuilder.loadTexts:
    hwCBQoSRuleNotSupportAlarmEntry.setStatus("current")


class _HwCBQoSRuleDirection_Type(OctetString):
    """Custom type hwCBQoSRuleDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSRuleDirection_Type.__name__ = "OctetString"
_HwCBQoSRuleDirection_Object = MibTableColumn
hwCBQoSRuleDirection = _HwCBQoSRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 8, 1, 1),
    _HwCBQoSRuleDirection_Type()
)
hwCBQoSRuleDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSRuleDirection.setStatus("current")


class _HwCBQoSRuleSlotID_Type(Integer32):
    """Custom type hwCBQoSRuleSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwCBQoSRuleSlotID_Type.__name__ = "Integer32"
_HwCBQoSRuleSlotID_Object = MibTableColumn
hwCBQoSRuleSlotID = _HwCBQoSRuleSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 8, 1, 2),
    _HwCBQoSRuleSlotID_Type()
)
hwCBQoSRuleSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSRuleSlotID.setStatus("current")


class _HwCBQoSRuleInfo_Type(OctetString):
    """Custom type hwCBQoSRuleInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwCBQoSRuleInfo_Type.__name__ = "OctetString"
_HwCBQoSRuleInfo_Object = MibTableColumn
hwCBQoSRuleInfo = _HwCBQoSRuleInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 8, 1, 3),
    _HwCBQoSRuleInfo_Type()
)
hwCBQoSRuleInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSRuleInfo.setStatus("current")
_HwCBQoSActionNotSupportAlarmTable_Object = MibTable
hwCBQoSActionNotSupportAlarmTable = _HwCBQoSActionNotSupportAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    hwCBQoSActionNotSupportAlarmTable.setStatus("current")
_HwCBQoSActionNotSupportAlarmEntry_Object = MibTableRow
hwCBQoSActionNotSupportAlarmEntry = _HwCBQoSActionNotSupportAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 9, 1)
)
hwCBQoSActionNotSupportAlarmEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSActionDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSActionSlotID"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSActionInfo"),
)
if mibBuilder.loadTexts:
    hwCBQoSActionNotSupportAlarmEntry.setStatus("current")


class _HwCBQoSActionDirection_Type(OctetString):
    """Custom type hwCBQoSActionDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSActionDirection_Type.__name__ = "OctetString"
_HwCBQoSActionDirection_Object = MibTableColumn
hwCBQoSActionDirection = _HwCBQoSActionDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 9, 1, 1),
    _HwCBQoSActionDirection_Type()
)
hwCBQoSActionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSActionDirection.setStatus("current")


class _HwCBQoSActionSlotID_Type(Integer32):
    """Custom type hwCBQoSActionSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwCBQoSActionSlotID_Type.__name__ = "Integer32"
_HwCBQoSActionSlotID_Object = MibTableColumn
hwCBQoSActionSlotID = _HwCBQoSActionSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 9, 1, 2),
    _HwCBQoSActionSlotID_Type()
)
hwCBQoSActionSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSActionSlotID.setStatus("current")


class _HwCBQoSActionInfo_Type(OctetString):
    """Custom type hwCBQoSActionInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwCBQoSActionInfo_Type.__name__ = "OctetString"
_HwCBQoSActionInfo_Object = MibTableColumn
hwCBQoSActionInfo = _HwCBQoSActionInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 9, 1, 3),
    _HwCBQoSActionInfo_Type()
)
hwCBQoSActionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSActionInfo.setStatus("current")
_HwCBQoSIfApplyMultiPolicyTable_Object = MibTable
hwCBQoSIfApplyMultiPolicyTable = _HwCBQoSIfApplyMultiPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyTable.setStatus("current")
_HwCBQoSIfApplyMultiPolicyEntry_Object = MibTableRow
hwCBQoSIfApplyMultiPolicyEntry = _HwCBQoSIfApplyMultiPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10, 1)
)
hwCBQoSIfApplyMultiPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyEntry.setStatus("current")
_HwCBQoSIfApplyMultiPolicyIfIndex_Type = Integer32
_HwCBQoSIfApplyMultiPolicyIfIndex_Object = MibTableColumn
hwCBQoSIfApplyMultiPolicyIfIndex = _HwCBQoSIfApplyMultiPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10, 1, 1),
    _HwCBQoSIfApplyMultiPolicyIfIndex_Type()
)
hwCBQoSIfApplyMultiPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyIfIndex.setStatus("current")
_HwCBQoSIfApplyMultiPolicyDirection_Type = DirectionType
_HwCBQoSIfApplyMultiPolicyDirection_Object = MibTableColumn
hwCBQoSIfApplyMultiPolicyDirection = _HwCBQoSIfApplyMultiPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10, 1, 2),
    _HwCBQoSIfApplyMultiPolicyDirection_Type()
)
hwCBQoSIfApplyMultiPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyDirection.setStatus("current")
_HwCBQoSIfApplyMultiPolicyIndex_Type = Integer32
_HwCBQoSIfApplyMultiPolicyIndex_Object = MibTableColumn
hwCBQoSIfApplyMultiPolicyIndex = _HwCBQoSIfApplyMultiPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10, 1, 3),
    _HwCBQoSIfApplyMultiPolicyIndex_Type()
)
hwCBQoSIfApplyMultiPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyIndex.setStatus("current")


class _HwCBQoSIfApplyMultiPolicyName_Type(OctetString):
    """Custom type hwCBQoSIfApplyMultiPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSIfApplyMultiPolicyName_Type.__name__ = "OctetString"
_HwCBQoSIfApplyMultiPolicyName_Object = MibTableColumn
hwCBQoSIfApplyMultiPolicyName = _HwCBQoSIfApplyMultiPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10, 1, 4),
    _HwCBQoSIfApplyMultiPolicyName_Type()
)
hwCBQoSIfApplyMultiPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyName.setStatus("current")
_HwCBQoSIfApplyMultiPolicyRowStatus_Type = RowStatus
_HwCBQoSIfApplyMultiPolicyRowStatus_Object = MibTableColumn
hwCBQoSIfApplyMultiPolicyRowStatus = _HwCBQoSIfApplyMultiPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 10, 1, 5),
    _HwCBQoSIfApplyMultiPolicyRowStatus_Type()
)
hwCBQoSIfApplyMultiPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyMultiPolicyRowStatus.setStatus("current")
_HwCBQoSVlanApplyMultiPolicyTable_Object = MibTable
hwCBQoSVlanApplyMultiPolicyTable = _HwCBQoSVlanApplyMultiPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyTable.setStatus("current")
_HwCBQoSVlanApplyMultiPolicyEntry_Object = MibTableRow
hwCBQoSVlanApplyMultiPolicyEntry = _HwCBQoSVlanApplyMultiPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11, 1)
)
hwCBQoSVlanApplyMultiPolicyEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyMultiPolicyVlanId"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyMultiPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyMultiPolicyIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyEntry.setStatus("current")


class _HwCBQoSVlanApplyMultiPolicyVlanId_Type(Integer32):
    """Custom type hwCBQoSVlanApplyMultiPolicyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwCBQoSVlanApplyMultiPolicyVlanId_Type.__name__ = "Integer32"
_HwCBQoSVlanApplyMultiPolicyVlanId_Object = MibTableColumn
hwCBQoSVlanApplyMultiPolicyVlanId = _HwCBQoSVlanApplyMultiPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11, 1, 1),
    _HwCBQoSVlanApplyMultiPolicyVlanId_Type()
)
hwCBQoSVlanApplyMultiPolicyVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyVlanId.setStatus("current")


class _HwCBQoSVlanApplyMultiPolicyDirection_Type(Integer32):
    """Custom type hwCBQoSVlanApplyMultiPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwCBQoSVlanApplyMultiPolicyDirection_Type.__name__ = "Integer32"
_HwCBQoSVlanApplyMultiPolicyDirection_Object = MibTableColumn
hwCBQoSVlanApplyMultiPolicyDirection = _HwCBQoSVlanApplyMultiPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11, 1, 2),
    _HwCBQoSVlanApplyMultiPolicyDirection_Type()
)
hwCBQoSVlanApplyMultiPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyDirection.setStatus("current")
_HwCBQoSVlanApplyMultiPolicyIndex_Type = Integer32
_HwCBQoSVlanApplyMultiPolicyIndex_Object = MibTableColumn
hwCBQoSVlanApplyMultiPolicyIndex = _HwCBQoSVlanApplyMultiPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11, 1, 3),
    _HwCBQoSVlanApplyMultiPolicyIndex_Type()
)
hwCBQoSVlanApplyMultiPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyIndex.setStatus("current")


class _HwCBQoSVlanApplyMultiPolicyName_Type(OctetString):
    """Custom type hwCBQoSVlanApplyMultiPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSVlanApplyMultiPolicyName_Type.__name__ = "OctetString"
_HwCBQoSVlanApplyMultiPolicyName_Object = MibTableColumn
hwCBQoSVlanApplyMultiPolicyName = _HwCBQoSVlanApplyMultiPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11, 1, 4),
    _HwCBQoSVlanApplyMultiPolicyName_Type()
)
hwCBQoSVlanApplyMultiPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyName.setStatus("current")
_HwCBQoSVlanApplyMultiPolicyRowStatus_Type = RowStatus
_HwCBQoSVlanApplyMultiPolicyRowStatus_Object = MibTableColumn
hwCBQoSVlanApplyMultiPolicyRowStatus = _HwCBQoSVlanApplyMultiPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 4, 11, 1, 5),
    _HwCBQoSVlanApplyMultiPolicyRowStatus_Type()
)
hwCBQoSVlanApplyMultiPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyMultiPolicyRowStatus.setStatus("current")
_HwCBQoSApplyPolicyStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSApplyPolicyStaticsObjects = _HwCBQoSApplyPolicyStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5)
)
_HwCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSIfStaticsObjects = _HwCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1)
)
_HwCBQoSIfCbqRunInfoTable_Object = MibTable
hwCBQoSIfCbqRunInfoTable = _HwCBQoSIfCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSIfCbqRunInfoTable.setStatus("current")
_HwCBQoSIfCbqRunInfoEntry_Object = MibTableRow
hwCBQoSIfCbqRunInfoEntry = _HwCBQoSIfCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1)
)
hwCBQoSIfCbqRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfCbqRunInfoEntry.setStatus("current")
_HwCBQoSIfCbqQueueSize_Type = Integer32
_HwCBQoSIfCbqQueueSize_Object = MibTableColumn
hwCBQoSIfCbqQueueSize = _HwCBQoSIfCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 1),
    _HwCBQoSIfCbqQueueSize_Type()
)
hwCBQoSIfCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqQueueSize.setStatus("current")
_HwCBQoSIfCbqDiscard_Type = Counter64
_HwCBQoSIfCbqDiscard_Object = MibTableColumn
hwCBQoSIfCbqDiscard = _HwCBQoSIfCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 2),
    _HwCBQoSIfCbqDiscard_Type()
)
hwCBQoSIfCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqDiscard.setStatus("current")
_HwCBQoSIfCbqEfQueueSize_Type = Integer32
_HwCBQoSIfCbqEfQueueSize_Object = MibTableColumn
hwCBQoSIfCbqEfQueueSize = _HwCBQoSIfCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 3),
    _HwCBQoSIfCbqEfQueueSize_Type()
)
hwCBQoSIfCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqEfQueueSize.setStatus("current")
_HwCBQoSIfCbqAfQueueSize_Type = Integer32
_HwCBQoSIfCbqAfQueueSize_Object = MibTableColumn
hwCBQoSIfCbqAfQueueSize = _HwCBQoSIfCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 4),
    _HwCBQoSIfCbqAfQueueSize_Type()
)
hwCBQoSIfCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqAfQueueSize.setStatus("current")
_HwCBQoSIfCbqBeQueueSize_Type = Integer32
_HwCBQoSIfCbqBeQueueSize_Object = MibTableColumn
hwCBQoSIfCbqBeQueueSize = _HwCBQoSIfCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 5),
    _HwCBQoSIfCbqBeQueueSize_Type()
)
hwCBQoSIfCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeQueueSize.setStatus("current")
_HwCBQoSIfCbqBeActiveQueueNum_Type = Integer32
_HwCBQoSIfCbqBeActiveQueueNum_Object = MibTableColumn
hwCBQoSIfCbqBeActiveQueueNum = _HwCBQoSIfCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 6),
    _HwCBQoSIfCbqBeActiveQueueNum_Type()
)
hwCBQoSIfCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeActiveQueueNum.setStatus("current")
_HwCBQoSIfCbqBeMaxActiveQueueNum_Type = Integer32
_HwCBQoSIfCbqBeMaxActiveQueueNum_Object = MibTableColumn
hwCBQoSIfCbqBeMaxActiveQueueNum = _HwCBQoSIfCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 7),
    _HwCBQoSIfCbqBeMaxActiveQueueNum_Type()
)
hwCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeMaxActiveQueueNum.setStatus("current")
_HwCBQoSIfCbqBeTotalQueueNum_Type = Integer32
_HwCBQoSIfCbqBeTotalQueueNum_Object = MibTableColumn
hwCBQoSIfCbqBeTotalQueueNum = _HwCBQoSIfCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 8),
    _HwCBQoSIfCbqBeTotalQueueNum_Type()
)
hwCBQoSIfCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeTotalQueueNum.setStatus("current")
_HwCBQoSIfCbqAfAllocatedQueueNum_Type = Integer32
_HwCBQoSIfCbqAfAllocatedQueueNum_Object = MibTableColumn
hwCBQoSIfCbqAfAllocatedQueueNum = _HwCBQoSIfCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 1, 1, 9),
    _HwCBQoSIfCbqAfAllocatedQueueNum_Type()
)
hwCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqAfAllocatedQueueNum.setStatus("current")
_HwCBQoSIfClassMatchRunInfoTable_Object = MibTable
hwCBQoSIfClassMatchRunInfoTable = _HwCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchRunInfoTable.setStatus("current")
_HwCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSIfClassMatchRunInfoEntry = _HwCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2, 1)
)
hwCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSIfClassMatchedPackets_Type = Counter64
_HwCBQoSIfClassMatchedPackets_Object = MibTableColumn
hwCBQoSIfClassMatchedPackets = _HwCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2, 1, 1),
    _HwCBQoSIfClassMatchedPackets_Type()
)
hwCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchedPackets.setStatus("current")
_HwCBQoSIfClassMatchedBytes_Type = Counter64
_HwCBQoSIfClassMatchedBytes_Object = MibTableColumn
hwCBQoSIfClassMatchedBytes = _HwCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2, 1, 2),
    _HwCBQoSIfClassMatchedBytes_Type()
)
hwCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchedBytes.setStatus("current")
_HwCBQoSIfClassAverageRate_Type = Counter64
_HwCBQoSIfClassAverageRate_Object = MibTableColumn
hwCBQoSIfClassAverageRate = _HwCBQoSIfClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2, 1, 3),
    _HwCBQoSIfClassAverageRate_Type()
)
hwCBQoSIfClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfClassAverageRate.setStatus("current")
_HwCBQosIfClassPassedPackets_Type = Counter64
_HwCBQosIfClassPassedPackets_Object = MibTableColumn
hwCBQosIfClassPassedPackets = _HwCBQosIfClassPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2, 1, 4),
    _HwCBQosIfClassPassedPackets_Type()
)
hwCBQosIfClassPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQosIfClassPassedPackets.setStatus("current")
_HwCBQosIfClassDroppedPackets_Type = Counter64
_HwCBQosIfClassDroppedPackets_Object = MibTableColumn
hwCBQosIfClassDroppedPackets = _HwCBQosIfClassDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 2, 1, 5),
    _HwCBQosIfClassDroppedPackets_Type()
)
hwCBQosIfClassDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQosIfClassDroppedPackets.setStatus("current")
_HwCBQoSIfCarRunInfoTable_Object = MibTable
hwCBQoSIfCarRunInfoTable = _HwCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSIfCarRunInfoTable.setStatus("current")
_HwCBQoSIfCarRunInfoEntry_Object = MibTableRow
hwCBQoSIfCarRunInfoEntry = _HwCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1)
)
hwCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfCarRunInfoEntry.setStatus("current")
_HwCBQoSIfCarGreenPassedPackets_Type = Counter64
_HwCBQoSIfCarGreenPassedPackets_Object = MibTableColumn
hwCBQoSIfCarGreenPassedPackets = _HwCBQoSIfCarGreenPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 1),
    _HwCBQoSIfCarGreenPassedPackets_Type()
)
hwCBQoSIfCarGreenPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenPassedPackets.setStatus("current")
_HwCBQoSIfCarGreenPassedBytes_Type = Counter64
_HwCBQoSIfCarGreenPassedBytes_Object = MibTableColumn
hwCBQoSIfCarGreenPassedBytes = _HwCBQoSIfCarGreenPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 2),
    _HwCBQoSIfCarGreenPassedBytes_Type()
)
hwCBQoSIfCarGreenPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenPassedBytes.setStatus("current")
_HwCBQoSIfCarGreenRemarkedPackets_Type = Counter64
_HwCBQoSIfCarGreenRemarkedPackets_Object = MibTableColumn
hwCBQoSIfCarGreenRemarkedPackets = _HwCBQoSIfCarGreenRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 3),
    _HwCBQoSIfCarGreenRemarkedPackets_Type()
)
hwCBQoSIfCarGreenRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenRemarkedPackets.setStatus("current")
_HwCBQoSIfCarGreenRemarkedBytes_Type = Counter64
_HwCBQoSIfCarGreenRemarkedBytes_Object = MibTableColumn
hwCBQoSIfCarGreenRemarkedBytes = _HwCBQoSIfCarGreenRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 4),
    _HwCBQoSIfCarGreenRemarkedBytes_Type()
)
hwCBQoSIfCarGreenRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenRemarkedBytes.setStatus("current")
_HwCBQoSIfCarGreenDiscardedPackets_Type = Counter64
_HwCBQoSIfCarGreenDiscardedPackets_Object = MibTableColumn
hwCBQoSIfCarGreenDiscardedPackets = _HwCBQoSIfCarGreenDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 5),
    _HwCBQoSIfCarGreenDiscardedPackets_Type()
)
hwCBQoSIfCarGreenDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenDiscardedPackets.setStatus("current")
_HwCBQoSIfCarGreenDiscardedBytes_Type = Counter64
_HwCBQoSIfCarGreenDiscardedBytes_Object = MibTableColumn
hwCBQoSIfCarGreenDiscardedBytes = _HwCBQoSIfCarGreenDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 6),
    _HwCBQoSIfCarGreenDiscardedBytes_Type()
)
hwCBQoSIfCarGreenDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenDiscardedBytes.setStatus("current")
_HwCBQoSIfCarYellowPassedPackets_Type = Counter64
_HwCBQoSIfCarYellowPassedPackets_Object = MibTableColumn
hwCBQoSIfCarYellowPassedPackets = _HwCBQoSIfCarYellowPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 7),
    _HwCBQoSIfCarYellowPassedPackets_Type()
)
hwCBQoSIfCarYellowPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowPassedPackets.setStatus("current")
_HwCBQoSIfCarYellowPassedBytes_Type = Counter64
_HwCBQoSIfCarYellowPassedBytes_Object = MibTableColumn
hwCBQoSIfCarYellowPassedBytes = _HwCBQoSIfCarYellowPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 8),
    _HwCBQoSIfCarYellowPassedBytes_Type()
)
hwCBQoSIfCarYellowPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowPassedBytes.setStatus("current")
_HwCBQoSIfCarYellowRemarkedPackets_Type = Counter64
_HwCBQoSIfCarYellowRemarkedPackets_Object = MibTableColumn
hwCBQoSIfCarYellowRemarkedPackets = _HwCBQoSIfCarYellowRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 9),
    _HwCBQoSIfCarYellowRemarkedPackets_Type()
)
hwCBQoSIfCarYellowRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowRemarkedPackets.setStatus("current")
_HwCBQoSIfCarYellowRemarkedBytes_Type = Counter64
_HwCBQoSIfCarYellowRemarkedBytes_Object = MibTableColumn
hwCBQoSIfCarYellowRemarkedBytes = _HwCBQoSIfCarYellowRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 10),
    _HwCBQoSIfCarYellowRemarkedBytes_Type()
)
hwCBQoSIfCarYellowRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowRemarkedBytes.setStatus("current")
_HwCBQoSIfCarYellowDiscardedPackets_Type = Counter64
_HwCBQoSIfCarYellowDiscardedPackets_Object = MibTableColumn
hwCBQoSIfCarYellowDiscardedPackets = _HwCBQoSIfCarYellowDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 11),
    _HwCBQoSIfCarYellowDiscardedPackets_Type()
)
hwCBQoSIfCarYellowDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowDiscardedPackets.setStatus("current")
_HwCBQoSIfCarYellowDiscardedBytes_Type = Counter64
_HwCBQoSIfCarYellowDiscardedBytes_Object = MibTableColumn
hwCBQoSIfCarYellowDiscardedBytes = _HwCBQoSIfCarYellowDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 12),
    _HwCBQoSIfCarYellowDiscardedBytes_Type()
)
hwCBQoSIfCarYellowDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowDiscardedBytes.setStatus("current")
_HwCBQoSIfCarRedPassedPackets_Type = Counter64
_HwCBQoSIfCarRedPassedPackets_Object = MibTableColumn
hwCBQoSIfCarRedPassedPackets = _HwCBQoSIfCarRedPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 13),
    _HwCBQoSIfCarRedPassedPackets_Type()
)
hwCBQoSIfCarRedPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedPassedPackets.setStatus("current")
_HwCBQoSIfCarRedPassedBytes_Type = Counter64
_HwCBQoSIfCarRedPassedBytes_Object = MibTableColumn
hwCBQoSIfCarRedPassedBytes = _HwCBQoSIfCarRedPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 14),
    _HwCBQoSIfCarRedPassedBytes_Type()
)
hwCBQoSIfCarRedPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedPassedBytes.setStatus("current")
_HwCBQoSIfCarRedRemarkedPackets_Type = Counter64
_HwCBQoSIfCarRedRemarkedPackets_Object = MibTableColumn
hwCBQoSIfCarRedRemarkedPackets = _HwCBQoSIfCarRedRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 15),
    _HwCBQoSIfCarRedRemarkedPackets_Type()
)
hwCBQoSIfCarRedRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedRemarkedPackets.setStatus("current")
_HwCBQoSIfCarRedRemarkedBytes_Type = Counter64
_HwCBQoSIfCarRedRemarkedBytes_Object = MibTableColumn
hwCBQoSIfCarRedRemarkedBytes = _HwCBQoSIfCarRedRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 16),
    _HwCBQoSIfCarRedRemarkedBytes_Type()
)
hwCBQoSIfCarRedRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedRemarkedBytes.setStatus("current")
_HwCBQoSIfCarRedDiscardedPackets_Type = Counter64
_HwCBQoSIfCarRedDiscardedPackets_Object = MibTableColumn
hwCBQoSIfCarRedDiscardedPackets = _HwCBQoSIfCarRedDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 17),
    _HwCBQoSIfCarRedDiscardedPackets_Type()
)
hwCBQoSIfCarRedDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedDiscardedPackets.setStatus("current")
_HwCBQoSIfCarRedDiscardedBytes_Type = Counter64
_HwCBQoSIfCarRedDiscardedBytes_Object = MibTableColumn
hwCBQoSIfCarRedDiscardedBytes = _HwCBQoSIfCarRedDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 18),
    _HwCBQoSIfCarRedDiscardedBytes_Type()
)
hwCBQoSIfCarRedDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedDiscardedBytes.setStatus("current")
_HwCBQoSIfCarGreenPassedPacketsRate_Type = Counter64
_HwCBQoSIfCarGreenPassedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarGreenPassedPacketsRate = _HwCBQoSIfCarGreenPassedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 19),
    _HwCBQoSIfCarGreenPassedPacketsRate_Type()
)
hwCBQoSIfCarGreenPassedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenPassedPacketsRate.setStatus("current")
_HwCBQoSIfCarGreenPassedBytesRate_Type = Counter64
_HwCBQoSIfCarGreenPassedBytesRate_Object = MibTableColumn
hwCBQoSIfCarGreenPassedBytesRate = _HwCBQoSIfCarGreenPassedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 20),
    _HwCBQoSIfCarGreenPassedBytesRate_Type()
)
hwCBQoSIfCarGreenPassedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenPassedBytesRate.setStatus("current")
_HwCBQoSIfCarGreenRemarkedPacketsRate_Type = Counter64
_HwCBQoSIfCarGreenRemarkedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarGreenRemarkedPacketsRate = _HwCBQoSIfCarGreenRemarkedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 21),
    _HwCBQoSIfCarGreenRemarkedPacketsRate_Type()
)
hwCBQoSIfCarGreenRemarkedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenRemarkedPacketsRate.setStatus("current")
_HwCBQoSIfCarGreenRemarkedBytesRate_Type = Counter64
_HwCBQoSIfCarGreenRemarkedBytesRate_Object = MibTableColumn
hwCBQoSIfCarGreenRemarkedBytesRate = _HwCBQoSIfCarGreenRemarkedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 22),
    _HwCBQoSIfCarGreenRemarkedBytesRate_Type()
)
hwCBQoSIfCarGreenRemarkedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenRemarkedBytesRate.setStatus("current")
_HwCBQoSIfCarGreenDiscardedPacketsRate_Type = Counter64
_HwCBQoSIfCarGreenDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarGreenDiscardedPacketsRate = _HwCBQoSIfCarGreenDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 23),
    _HwCBQoSIfCarGreenDiscardedPacketsRate_Type()
)
hwCBQoSIfCarGreenDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenDiscardedPacketsRate.setStatus("current")
_HwCBQoSIfCarGreenDiscardedBytesRate_Type = Counter64
_HwCBQoSIfCarGreenDiscardedBytesRate_Object = MibTableColumn
hwCBQoSIfCarGreenDiscardedBytesRate = _HwCBQoSIfCarGreenDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 24),
    _HwCBQoSIfCarGreenDiscardedBytesRate_Type()
)
hwCBQoSIfCarGreenDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenDiscardedBytesRate.setStatus("current")
_HwCBQoSIfCarYellowPassedPacketsRate_Type = Counter64
_HwCBQoSIfCarYellowPassedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarYellowPassedPacketsRate = _HwCBQoSIfCarYellowPassedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 25),
    _HwCBQoSIfCarYellowPassedPacketsRate_Type()
)
hwCBQoSIfCarYellowPassedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowPassedPacketsRate.setStatus("current")
_HwCBQoSIfCarYellowPassedBytesRate_Type = Counter64
_HwCBQoSIfCarYellowPassedBytesRate_Object = MibTableColumn
hwCBQoSIfCarYellowPassedBytesRate = _HwCBQoSIfCarYellowPassedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 26),
    _HwCBQoSIfCarYellowPassedBytesRate_Type()
)
hwCBQoSIfCarYellowPassedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowPassedBytesRate.setStatus("current")
_HwCBQoSIfCarYellowRemarkedPacketsRate_Type = Counter64
_HwCBQoSIfCarYellowRemarkedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarYellowRemarkedPacketsRate = _HwCBQoSIfCarYellowRemarkedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 27),
    _HwCBQoSIfCarYellowRemarkedPacketsRate_Type()
)
hwCBQoSIfCarYellowRemarkedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowRemarkedPacketsRate.setStatus("current")
_HwCBQoSIfCarYellowRemarkedBytesRate_Type = Counter64
_HwCBQoSIfCarYellowRemarkedBytesRate_Object = MibTableColumn
hwCBQoSIfCarYellowRemarkedBytesRate = _HwCBQoSIfCarYellowRemarkedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 28),
    _HwCBQoSIfCarYellowRemarkedBytesRate_Type()
)
hwCBQoSIfCarYellowRemarkedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowRemarkedBytesRate.setStatus("current")
_HwCBQoSIfCarYellowDiscardedPacketsRate_Type = Counter64
_HwCBQoSIfCarYellowDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarYellowDiscardedPacketsRate = _HwCBQoSIfCarYellowDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 29),
    _HwCBQoSIfCarYellowDiscardedPacketsRate_Type()
)
hwCBQoSIfCarYellowDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowDiscardedPacketsRate.setStatus("current")
_HwCBQoSIfCarYellowDiscardedBytesRate_Type = Counter64
_HwCBQoSIfCarYellowDiscardedBytesRate_Object = MibTableColumn
hwCBQoSIfCarYellowDiscardedBytesRate = _HwCBQoSIfCarYellowDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 30),
    _HwCBQoSIfCarYellowDiscardedBytesRate_Type()
)
hwCBQoSIfCarYellowDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarYellowDiscardedBytesRate.setStatus("current")
_HwCBQoSIfCarRedPassedPacketsRate_Type = Counter64
_HwCBQoSIfCarRedPassedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarRedPassedPacketsRate = _HwCBQoSIfCarRedPassedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 31),
    _HwCBQoSIfCarRedPassedPacketsRate_Type()
)
hwCBQoSIfCarRedPassedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedPassedPacketsRate.setStatus("current")
_HwCBQoSIfCarRedPassedBytesRate_Type = Counter64
_HwCBQoSIfCarRedPassedBytesRate_Object = MibTableColumn
hwCBQoSIfCarRedPassedBytesRate = _HwCBQoSIfCarRedPassedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 32),
    _HwCBQoSIfCarRedPassedBytesRate_Type()
)
hwCBQoSIfCarRedPassedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedPassedBytesRate.setStatus("current")
_HwCBQoSIfCarRedRemarkedPacketsRate_Type = Counter64
_HwCBQoSIfCarRedRemarkedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarRedRemarkedPacketsRate = _HwCBQoSIfCarRedRemarkedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 33),
    _HwCBQoSIfCarRedRemarkedPacketsRate_Type()
)
hwCBQoSIfCarRedRemarkedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedRemarkedPacketsRate.setStatus("current")
_HwCBQoSIfCarRedRemarkedBytesRate_Type = Counter64
_HwCBQoSIfCarRedRemarkedBytesRate_Object = MibTableColumn
hwCBQoSIfCarRedRemarkedBytesRate = _HwCBQoSIfCarRedRemarkedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 34),
    _HwCBQoSIfCarRedRemarkedBytesRate_Type()
)
hwCBQoSIfCarRedRemarkedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedRemarkedBytesRate.setStatus("current")
_HwCBQoSIfCarRedDiscardedPacketsRate_Type = Counter64
_HwCBQoSIfCarRedDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSIfCarRedDiscardedPacketsRate = _HwCBQoSIfCarRedDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 35),
    _HwCBQoSIfCarRedDiscardedPacketsRate_Type()
)
hwCBQoSIfCarRedDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedDiscardedPacketsRate.setStatus("current")
_HwCBQoSIfCarRedDiscardedBytesRate_Type = Counter64
_HwCBQoSIfCarRedDiscardedBytesRate_Object = MibTableColumn
hwCBQoSIfCarRedDiscardedBytesRate = _HwCBQoSIfCarRedDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 3, 1, 36),
    _HwCBQoSIfCarRedDiscardedBytesRate_Type()
)
hwCBQoSIfCarRedDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedDiscardedBytesRate.setStatus("current")
_HwCBQoSIfGtsRunInfoTable_Object = MibTable
hwCBQoSIfGtsRunInfoTable = _HwCBQoSIfGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSIfGtsRunInfoTable.setStatus("current")
_HwCBQoSIfGtsRunInfoEntry_Object = MibTableRow
hwCBQoSIfGtsRunInfoEntry = _HwCBQoSIfGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1)
)
hwCBQoSIfGtsRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfGtsRunInfoEntry.setStatus("current")
_HwCBQoSIfGtsPassedPackets_Type = Counter64
_HwCBQoSIfGtsPassedPackets_Object = MibTableColumn
hwCBQoSIfGtsPassedPackets = _HwCBQoSIfGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 1),
    _HwCBQoSIfGtsPassedPackets_Type()
)
hwCBQoSIfGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsPassedPackets.setStatus("current")
_HwCBQoSIfGtsPassedBytes_Type = Counter64
_HwCBQoSIfGtsPassedBytes_Object = MibTableColumn
hwCBQoSIfGtsPassedBytes = _HwCBQoSIfGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 2),
    _HwCBQoSIfGtsPassedBytes_Type()
)
hwCBQoSIfGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsPassedBytes.setStatus("current")
_HwCBQoSIfGtsDiscardedPackets_Type = Counter64
_HwCBQoSIfGtsDiscardedPackets_Object = MibTableColumn
hwCBQoSIfGtsDiscardedPackets = _HwCBQoSIfGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 3),
    _HwCBQoSIfGtsDiscardedPackets_Type()
)
hwCBQoSIfGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDiscardedPackets.setStatus("current")
_HwCBQoSIfGtsDiscardedBytes_Type = Counter64
_HwCBQoSIfGtsDiscardedBytes_Object = MibTableColumn
hwCBQoSIfGtsDiscardedBytes = _HwCBQoSIfGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 4),
    _HwCBQoSIfGtsDiscardedBytes_Type()
)
hwCBQoSIfGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDiscardedBytes.setStatus("current")
_HwCBQoSIfGtsDelayedPackets_Type = Counter64
_HwCBQoSIfGtsDelayedPackets_Object = MibTableColumn
hwCBQoSIfGtsDelayedPackets = _HwCBQoSIfGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 5),
    _HwCBQoSIfGtsDelayedPackets_Type()
)
hwCBQoSIfGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDelayedPackets.setStatus("current")
_HwCBQoSIfGtsDelayedBytes_Type = Counter64
_HwCBQoSIfGtsDelayedBytes_Object = MibTableColumn
hwCBQoSIfGtsDelayedBytes = _HwCBQoSIfGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 6),
    _HwCBQoSIfGtsDelayedBytes_Type()
)
hwCBQoSIfGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDelayedBytes.setStatus("current")
_HwCBQoSIfGtsQueueSize_Type = Integer32
_HwCBQoSIfGtsQueueSize_Object = MibTableColumn
hwCBQoSIfGtsQueueSize = _HwCBQoSIfGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 4, 1, 7),
    _HwCBQoSIfGtsQueueSize_Type()
)
hwCBQoSIfGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsQueueSize.setStatus("current")
_HwCBQoSIfRemarkRunInfoTable_Object = MibTable
hwCBQoSIfRemarkRunInfoTable = _HwCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkRunInfoTable.setStatus("current")
_HwCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
hwCBQoSIfRemarkRunInfoEntry = _HwCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 5, 1)
)
hwCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkRunInfoEntry.setStatus("current")
_HwCBQoSIfRemarkedPackets_Type = Counter64
_HwCBQoSIfRemarkedPackets_Object = MibTableColumn
hwCBQoSIfRemarkedPackets = _HwCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 5, 1, 1),
    _HwCBQoSIfRemarkedPackets_Type()
)
hwCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkedPackets.setStatus("current")
_HwCBQoSIfRemarkedBytes_Type = Counter64
_HwCBQoSIfRemarkedBytes_Object = MibTableColumn
hwCBQoSIfRemarkedBytes = _HwCBQoSIfRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 5, 1, 2),
    _HwCBQoSIfRemarkedBytes_Type()
)
hwCBQoSIfRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkedBytes.setStatus("current")
_HwCBQoSIfQueueRunInfoTable_Object = MibTable
hwCBQoSIfQueueRunInfoTable = _HwCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSIfQueueRunInfoTable.setStatus("current")
_HwCBQoSIfQueueRunInfoEntry_Object = MibTableRow
hwCBQoSIfQueueRunInfoEntry = _HwCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1)
)
hwCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfQueueRunInfoEntry.setStatus("current")
_HwCBQoSIfQueueMatchedPackets_Type = Counter64
_HwCBQoSIfQueueMatchedPackets_Object = MibTableColumn
hwCBQoSIfQueueMatchedPackets = _HwCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 1),
    _HwCBQoSIfQueueMatchedPackets_Type()
)
hwCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueMatchedPackets.setStatus("current")
_HwCBQoSIfQueueMatchedBytes_Type = Counter64
_HwCBQoSIfQueueMatchedBytes_Object = MibTableColumn
hwCBQoSIfQueueMatchedBytes = _HwCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 2),
    _HwCBQoSIfQueueMatchedBytes_Type()
)
hwCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueMatchedBytes.setStatus("current")
_HwCBQoSIfQueueEnqueuedPackets_Type = Counter64
_HwCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSIfQueueEnqueuedPackets = _HwCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 3),
    _HwCBQoSIfQueueEnqueuedPackets_Type()
)
hwCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueEnqueuedPackets.setStatus("current")
_HwCBQoSIfQueueEnqueuedBytes_Type = Counter64
_HwCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSIfQueueEnqueuedBytes = _HwCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 4),
    _HwCBQoSIfQueueEnqueuedBytes_Type()
)
hwCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueEnqueuedBytes.setStatus("current")
_HwCBQoSIfQueueDiscardedPackets_Type = Counter64
_HwCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSIfQueueDiscardedPackets = _HwCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 5),
    _HwCBQoSIfQueueDiscardedPackets_Type()
)
hwCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueDiscardedPackets.setStatus("current")
_HwCBQoSIfQueueDiscardedBytes_Type = Counter64
_HwCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSIfQueueDiscardedBytes = _HwCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 6),
    _HwCBQoSIfQueueDiscardedBytes_Type()
)
hwCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueDiscardedBytes.setStatus("current")
_HwCBQoSIfQueueMatchedPacketsRate_Type = Counter64
_HwCBQoSIfQueueMatchedPacketsRate_Object = MibTableColumn
hwCBQoSIfQueueMatchedPacketsRate = _HwCBQoSIfQueueMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 7),
    _HwCBQoSIfQueueMatchedPacketsRate_Type()
)
hwCBQoSIfQueueMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueMatchedPacketsRate.setStatus("current")
_HwCBQoSIfQueueMatchedBytesRate_Type = Counter64
_HwCBQoSIfQueueMatchedBytesRate_Object = MibTableColumn
hwCBQoSIfQueueMatchedBytesRate = _HwCBQoSIfQueueMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 8),
    _HwCBQoSIfQueueMatchedBytesRate_Type()
)
hwCBQoSIfQueueMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueMatchedBytesRate.setStatus("current")
_HwCBQoSIfQueueEnqueuedPacketsRate_Type = Counter64
_HwCBQoSIfQueueEnqueuedPacketsRate_Object = MibTableColumn
hwCBQoSIfQueueEnqueuedPacketsRate = _HwCBQoSIfQueueEnqueuedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 9),
    _HwCBQoSIfQueueEnqueuedPacketsRate_Type()
)
hwCBQoSIfQueueEnqueuedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueEnqueuedPacketsRate.setStatus("current")
_HwCBQoSIfQueueEnqueuedBytesRate_Type = Counter64
_HwCBQoSIfQueueEnqueuedBytesRate_Object = MibTableColumn
hwCBQoSIfQueueEnqueuedBytesRate = _HwCBQoSIfQueueEnqueuedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 10),
    _HwCBQoSIfQueueEnqueuedBytesRate_Type()
)
hwCBQoSIfQueueEnqueuedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueEnqueuedBytesRate.setStatus("current")
_HwCBQoSIfQueueDiscardedPacketsRate_Type = Counter64
_HwCBQoSIfQueueDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSIfQueueDiscardedPacketsRate = _HwCBQoSIfQueueDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 11),
    _HwCBQoSIfQueueDiscardedPacketsRate_Type()
)
hwCBQoSIfQueueDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueDiscardedPacketsRate.setStatus("current")
_HwCBQoSIfQueueDiscardedBytesRate_Type = Counter64
_HwCBQoSIfQueueDiscardedBytesRate_Object = MibTableColumn
hwCBQoSIfQueueDiscardedBytesRate = _HwCBQoSIfQueueDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 6, 1, 12),
    _HwCBQoSIfQueueDiscardedBytesRate_Type()
)
hwCBQoSIfQueueDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueDiscardedBytesRate.setStatus("current")
_HwCBQoSIfWredRunInfoTable_Object = MibTable
hwCBQoSIfWredRunInfoTable = _HwCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSIfWredRunInfoTable.setStatus("current")
_HwCBQoSIfWredRunInfoEntry_Object = MibTableRow
hwCBQoSIfWredRunInfoEntry = _HwCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 7, 1)
)
hwCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfWredRunInfoEntry.setStatus("current")
_HwCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_HwCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
hwCBQoSIfWredRandomDiscardedPackets = _HwCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 7, 1, 1),
    _HwCBQoSIfWredRandomDiscardedPackets_Type()
)
hwCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_HwCBQoSIfWredTailDiscardedPackets_Type = Counter64
_HwCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
hwCBQoSIfWredTailDiscardedPackets = _HwCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 7, 1, 2),
    _HwCBQoSIfWredTailDiscardedPackets_Type()
)
hwCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfWredTailDiscardedPackets.setStatus("current")
_HwCBQoSIfLrRunInfoTable_Object = MibTable
hwCBQoSIfLrRunInfoTable = _HwCBQoSIfLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSIfLrRunInfoTable.setStatus("current")
_HwCBQoSIfLrRunInfoEntry_Object = MibTableRow
hwCBQoSIfLrRunInfoEntry = _HwCBQoSIfLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1)
)
hwCBQoSIfLrRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfLrRunInfoEntry.setStatus("current")
_HwCBQoSIfLrPassedPackets_Type = Counter64
_HwCBQoSIfLrPassedPackets_Object = MibTableColumn
hwCBQoSIfLrPassedPackets = _HwCBQoSIfLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1, 1),
    _HwCBQoSIfLrPassedPackets_Type()
)
hwCBQoSIfLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrPassedPackets.setStatus("current")
_HwCBQoSIfLrPassedBytes_Type = Counter64
_HwCBQoSIfLrPassedBytes_Object = MibTableColumn
hwCBQoSIfLrPassedBytes = _HwCBQoSIfLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1, 2),
    _HwCBQoSIfLrPassedBytes_Type()
)
hwCBQoSIfLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrPassedBytes.setStatus("current")
_HwCBQoSIfLrDiscardedPackets_Type = Counter64
_HwCBQoSIfLrDiscardedPackets_Object = MibTableColumn
hwCBQoSIfLrDiscardedPackets = _HwCBQoSIfLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1, 3),
    _HwCBQoSIfLrDiscardedPackets_Type()
)
hwCBQoSIfLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDiscardedPackets.setStatus("current")
_HwCBQoSIfLrDiscardedBytes_Type = Counter64
_HwCBQoSIfLrDiscardedBytes_Object = MibTableColumn
hwCBQoSIfLrDiscardedBytes = _HwCBQoSIfLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1, 4),
    _HwCBQoSIfLrDiscardedBytes_Type()
)
hwCBQoSIfLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDiscardedBytes.setStatus("current")
_HwCBQoSIfLrDelayedPackets_Type = Counter64
_HwCBQoSIfLrDelayedPackets_Object = MibTableColumn
hwCBQoSIfLrDelayedPackets = _HwCBQoSIfLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1, 5),
    _HwCBQoSIfLrDelayedPackets_Type()
)
hwCBQoSIfLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDelayedPackets.setStatus("current")
_HwCBQoSIfLrDelayedBytes_Type = Counter64
_HwCBQoSIfLrDelayedBytes_Object = MibTableColumn
hwCBQoSIfLrDelayedBytes = _HwCBQoSIfLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 8, 1, 6),
    _HwCBQoSIfLrDelayedBytes_Type()
)
hwCBQoSIfLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDelayedBytes.setStatus("current")
_HwCBQoSIfRedirectRunInfoTable_Object = MibTable
hwCBQoSIfRedirectRunInfoTable = _HwCBQoSIfRedirectRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 9)
)
if mibBuilder.loadTexts:
    hwCBQoSIfRedirectRunInfoTable.setStatus("current")
_HwCBQoSIfRedirectRunInfoEntry_Object = MibTableRow
hwCBQoSIfRedirectRunInfoEntry = _HwCBQoSIfRedirectRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 9, 1)
)
hwCBQoSIfRedirectRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfRedirectRunInfoEntry.setStatus("current")
_HwCBQoSIfRedirectedPackets_Type = Counter64
_HwCBQoSIfRedirectedPackets_Object = MibTableColumn
hwCBQoSIfRedirectedPackets = _HwCBQoSIfRedirectedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 9, 1, 1),
    _HwCBQoSIfRedirectedPackets_Type()
)
hwCBQoSIfRedirectedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfRedirectedPackets.setStatus("current")
_HwCBQoSIfRedirectedBytes_Type = Counter64
_HwCBQoSIfRedirectedBytes_Object = MibTableColumn
hwCBQoSIfRedirectedBytes = _HwCBQoSIfRedirectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 9, 1, 2),
    _HwCBQoSIfRedirectedBytes_Type()
)
hwCBQoSIfRedirectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfRedirectedBytes.setStatus("current")
_HwCBQoSIfFirewallRunInfoTable_Object = MibTable
hwCBQoSIfFirewallRunInfoTable = _HwCBQoSIfFirewallRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hwCBQoSIfFirewallRunInfoTable.setStatus("current")
_HwCBQoSIfFirewallRunInfoEntry_Object = MibTableRow
hwCBQoSIfFirewallRunInfoEntry = _HwCBQoSIfFirewallRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 10, 1)
)
hwCBQoSIfFirewallRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfFirewallRunInfoEntry.setStatus("current")
_HwCBQoSIfFilteredPackets_Type = Counter64
_HwCBQoSIfFilteredPackets_Object = MibTableColumn
hwCBQoSIfFilteredPackets = _HwCBQoSIfFilteredPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 10, 1, 1),
    _HwCBQoSIfFilteredPackets_Type()
)
hwCBQoSIfFilteredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfFilteredPackets.setStatus("current")
_HwCBQoSIfFilteredBytes_Type = Counter64
_HwCBQoSIfFilteredBytes_Object = MibTableColumn
hwCBQoSIfFilteredBytes = _HwCBQoSIfFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 10, 1, 2),
    _HwCBQoSIfFilteredBytes_Type()
)
hwCBQoSIfFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfFilteredBytes.setStatus("current")
_HwCBQoSIfMirrorRunInfoTable_Object = MibTable
hwCBQoSIfMirrorRunInfoTable = _HwCBQoSIfMirrorRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hwCBQoSIfMirrorRunInfoTable.setStatus("current")
_HwCBQoSIfMirrorRunInfoEntry_Object = MibTableRow
hwCBQoSIfMirrorRunInfoEntry = _HwCBQoSIfMirrorRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 11, 1)
)
hwCBQoSIfMirrorRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfMirrorRunInfoEntry.setStatus("current")
_HwCBQoSIfMirroredPackets_Type = Counter64
_HwCBQoSIfMirroredPackets_Object = MibTableColumn
hwCBQoSIfMirroredPackets = _HwCBQoSIfMirroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 11, 1, 1),
    _HwCBQoSIfMirroredPackets_Type()
)
hwCBQoSIfMirroredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfMirroredPackets.setStatus("current")
_HwCBQoSIfMirroredBytes_Type = Counter64
_HwCBQoSIfMirroredBytes_Object = MibTableColumn
hwCBQoSIfMirroredBytes = _HwCBQoSIfMirroredBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 11, 1, 2),
    _HwCBQoSIfMirroredBytes_Type()
)
hwCBQoSIfMirroredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfMirroredBytes.setStatus("current")
_HwCBQoSIfUrpfRunInfoTable_Object = MibTable
hwCBQoSIfUrpfRunInfoTable = _HwCBQoSIfUrpfRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 12)
)
if mibBuilder.loadTexts:
    hwCBQoSIfUrpfRunInfoTable.setStatus("current")
_HwCBQoSIfUrpfRunInfoEntry_Object = MibTableRow
hwCBQoSIfUrpfRunInfoEntry = _HwCBQoSIfUrpfRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 12, 1)
)
hwCBQoSIfUrpfRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfUrpfRunInfoEntry.setStatus("current")
_HwCBQoSIfUrpfPassedPackets_Type = Counter64
_HwCBQoSIfUrpfPassedPackets_Object = MibTableColumn
hwCBQoSIfUrpfPassedPackets = _HwCBQoSIfUrpfPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 12, 1, 1),
    _HwCBQoSIfUrpfPassedPackets_Type()
)
hwCBQoSIfUrpfPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfUrpfPassedPackets.setStatus("current")
_HwCBQoSIfUrpfPassedBytes_Type = Counter64
_HwCBQoSIfUrpfPassedBytes_Object = MibTableColumn
hwCBQoSIfUrpfPassedBytes = _HwCBQoSIfUrpfPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 12, 1, 2),
    _HwCBQoSIfUrpfPassedBytes_Type()
)
hwCBQoSIfUrpfPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfUrpfPassedBytes.setStatus("current")
_HwCBQoSIfUrpfDroppedPackets_Type = Counter64
_HwCBQoSIfUrpfDroppedPackets_Object = MibTableColumn
hwCBQoSIfUrpfDroppedPackets = _HwCBQoSIfUrpfDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 12, 1, 3),
    _HwCBQoSIfUrpfDroppedPackets_Type()
)
hwCBQoSIfUrpfDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfUrpfDroppedPackets.setStatus("current")
_HwCBQoSIfUrpfDroppedBytes_Type = Counter64
_HwCBQoSIfUrpfDroppedBytes_Object = MibTableColumn
hwCBQoSIfUrpfDroppedBytes = _HwCBQoSIfUrpfDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 12, 1, 4),
    _HwCBQoSIfUrpfDroppedBytes_Type()
)
hwCBQoSIfUrpfDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfUrpfDroppedBytes.setStatus("current")
_HwCBQoSIfSampleRunInfoTable_Object = MibTable
hwCBQoSIfSampleRunInfoTable = _HwCBQoSIfSampleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hwCBQoSIfSampleRunInfoTable.setStatus("current")
_HwCBQoSIfSampleRunInfoEntry_Object = MibTableRow
hwCBQoSIfSampleRunInfoEntry = _HwCBQoSIfSampleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 13, 1)
)
hwCBQoSIfSampleRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfSampleRunInfoEntry.setStatus("current")
_HwCBQoSIfSampledPackets_Type = Counter64
_HwCBQoSIfSampledPackets_Object = MibTableColumn
hwCBQoSIfSampledPackets = _HwCBQoSIfSampledPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 13, 1, 1),
    _HwCBQoSIfSampledPackets_Type()
)
hwCBQoSIfSampledPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfSampledPackets.setStatus("current")
_HwCBQoSIfSampledBytes_Type = Counter64
_HwCBQoSIfSampledBytes_Object = MibTableColumn
hwCBQoSIfSampledBytes = _HwCBQoSIfSampledBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 1, 13, 1, 2),
    _HwCBQoSIfSampledBytes_Type()
)
hwCBQoSIfSampledBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfSampledBytes.setStatus("current")
_HwCBQoSAtmPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSAtmPvcStaticsObjects = _HwCBQoSAtmPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2)
)
_HwCBQoSAtmPvcCbqRunInfoTable_Object = MibTable
hwCBQoSAtmPvcCbqRunInfoTable = _HwCBQoSAtmPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcCbqRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcCbqRunInfoEntry = _HwCBQoSAtmPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1)
)
hwCBQoSAtmPvcCbqRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcCbqQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqQueueSize = _HwCBQoSAtmPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 1),
    _HwCBQoSAtmPvcCbqQueueSize_Type()
)
hwCBQoSAtmPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqDiscard_Type = Counter64
_HwCBQoSAtmPvcCbqDiscard_Object = MibTableColumn
hwCBQoSAtmPvcCbqDiscard = _HwCBQoSAtmPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 2),
    _HwCBQoSAtmPvcCbqDiscard_Type()
)
hwCBQoSAtmPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqDiscard.setStatus("current")
_HwCBQoSAtmPvcCbqEfQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqEfQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqEfQueueSize = _HwCBQoSAtmPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 3),
    _HwCBQoSAtmPvcCbqEfQueueSize_Type()
)
hwCBQoSAtmPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqEfQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqAfQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqAfQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqAfQueueSize = _HwCBQoSAtmPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 4),
    _HwCBQoSAtmPvcCbqAfQueueSize_Type()
)
hwCBQoSAtmPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqAfQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqBeQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqBeQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeQueueSize = _HwCBQoSAtmPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 5),
    _HwCBQoSAtmPvcCbqBeQueueSize_Type()
)
hwCBQoSAtmPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqBeActiveQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqBeActiveQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeActiveQueueNum = _HwCBQoSAtmPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 6),
    _HwCBQoSAtmPvcCbqBeActiveQueueNum_Type()
)
hwCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeActiveQueueNum.setStatus("current")
_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeMaxActiveQueueNum = _HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 7),
    _HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type()
)
hwCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus("current")
_HwCBQoSAtmPvcCbqBeTotalQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqBeTotalQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeTotalQueueNum = _HwCBQoSAtmPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 8),
    _HwCBQoSAtmPvcCbqBeTotalQueueNum_Type()
)
hwCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeTotalQueueNum.setStatus("current")
_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqAfAllocatedQueueNum = _HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 1, 1, 9),
    _HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Type()
)
hwCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus("current")
_HwCBQoSAtmPvcClassMatchRunInfoTable_Object = MibTable
hwCBQoSAtmPvcClassMatchRunInfoTable = _HwCBQoSAtmPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcClassMatchRunInfoEntry = _HwCBQoSAtmPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 2, 1)
)
hwCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcClassMatchPackets_Type = Counter64
_HwCBQoSAtmPvcClassMatchPackets_Object = MibTableColumn
hwCBQoSAtmPvcClassMatchPackets = _HwCBQoSAtmPvcClassMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 2, 1, 1),
    _HwCBQoSAtmPvcClassMatchPackets_Type()
)
hwCBQoSAtmPvcClassMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchPackets.setStatus("current")
_HwCBQoSAtmPvcClassMatchBytes_Type = Counter64
_HwCBQoSAtmPvcClassMatchBytes_Object = MibTableColumn
hwCBQoSAtmPvcClassMatchBytes = _HwCBQoSAtmPvcClassMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 2, 1, 2),
    _HwCBQoSAtmPvcClassMatchBytes_Type()
)
hwCBQoSAtmPvcClassMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchBytes.setStatus("current")
_HwCBQoSAtmPvcClassAverageRate_Type = Counter64
_HwCBQoSAtmPvcClassAverageRate_Object = MibTableColumn
hwCBQoSAtmPvcClassAverageRate = _HwCBQoSAtmPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 2, 1, 3),
    _HwCBQoSAtmPvcClassAverageRate_Type()
)
hwCBQoSAtmPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassAverageRate.setStatus("current")
_HwCBQoSAtmPvcCarRunInfoTable_Object = MibTable
hwCBQoSAtmPvcCarRunInfoTable = _HwCBQoSAtmPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcCarRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcCarRunInfoEntry = _HwCBQoSAtmPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1)
)
hwCBQoSAtmPvcCarRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcCarConformPackets_Type = Counter64
_HwCBQoSAtmPvcCarConformPackets_Object = MibTableColumn
hwCBQoSAtmPvcCarConformPackets = _HwCBQoSAtmPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 1),
    _HwCBQoSAtmPvcCarConformPackets_Type()
)
hwCBQoSAtmPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarConformPackets.setStatus("current")
_HwCBQoSAtmPvcCarConformBytes_Type = Counter64
_HwCBQoSAtmPvcCarConformBytes_Object = MibTableColumn
hwCBQoSAtmPvcCarConformBytes = _HwCBQoSAtmPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 2),
    _HwCBQoSAtmPvcCarConformBytes_Type()
)
hwCBQoSAtmPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarConformBytes.setStatus("current")
_HwCBQoSAtmPvcCarExceedPackets_Type = Counter64
_HwCBQoSAtmPvcCarExceedPackets_Object = MibTableColumn
hwCBQoSAtmPvcCarExceedPackets = _HwCBQoSAtmPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 3),
    _HwCBQoSAtmPvcCarExceedPackets_Type()
)
hwCBQoSAtmPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarExceedPackets.setStatus("current")
_HwCBQoSAtmPvcCarExceedBytes_Type = Counter64
_HwCBQoSAtmPvcCarExceedBytes_Object = MibTableColumn
hwCBQoSAtmPvcCarExceedBytes = _HwCBQoSAtmPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 4),
    _HwCBQoSAtmPvcCarExceedBytes_Type()
)
hwCBQoSAtmPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarExceedBytes.setStatus("current")
_HwCBQoSAtmPvcCarConformPacketsRate_Type = Counter64
_HwCBQoSAtmPvcCarConformPacketsRate_Object = MibTableColumn
hwCBQoSAtmPvcCarConformPacketsRate = _HwCBQoSAtmPvcCarConformPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 5),
    _HwCBQoSAtmPvcCarConformPacketsRate_Type()
)
hwCBQoSAtmPvcCarConformPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarConformPacketsRate.setStatus("current")
_HwCBQoSAtmPvcCarConformBytesRate_Type = Counter64
_HwCBQoSAtmPvcCarConformBytesRate_Object = MibTableColumn
hwCBQoSAtmPvcCarConformBytesRate = _HwCBQoSAtmPvcCarConformBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 6),
    _HwCBQoSAtmPvcCarConformBytesRate_Type()
)
hwCBQoSAtmPvcCarConformBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarConformBytesRate.setStatus("current")
_HwCBQoSAtmPvcCarExceedPacketsRate_Type = Counter64
_HwCBQoSAtmPvcCarExceedPacketsRate_Object = MibTableColumn
hwCBQoSAtmPvcCarExceedPacketsRate = _HwCBQoSAtmPvcCarExceedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 7),
    _HwCBQoSAtmPvcCarExceedPacketsRate_Type()
)
hwCBQoSAtmPvcCarExceedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarExceedPacketsRate.setStatus("current")
_HwCBQoSAtmPvcCarExceedBytesRate_Type = Counter64
_HwCBQoSAtmPvcCarExceedBytesRate_Object = MibTableColumn
hwCBQoSAtmPvcCarExceedBytesRate = _HwCBQoSAtmPvcCarExceedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 3, 1, 8),
    _HwCBQoSAtmPvcCarExceedBytesRate_Type()
)
hwCBQoSAtmPvcCarExceedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarExceedBytesRate.setStatus("current")
_HwCBQoSAtmPvcGtsRunInfoTable_Object = MibTable
hwCBQoSAtmPvcGtsRunInfoTable = _HwCBQoSAtmPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcGtsRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcGtsRunInfoEntry = _HwCBQoSAtmPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1)
)
hwCBQoSAtmPvcGtsRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcGtsPassedPackets_Type = Counter64
_HwCBQoSAtmPvcGtsPassedPackets_Object = MibTableColumn
hwCBQoSAtmPvcGtsPassedPackets = _HwCBQoSAtmPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 1),
    _HwCBQoSAtmPvcGtsPassedPackets_Type()
)
hwCBQoSAtmPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsPassedPackets.setStatus("current")
_HwCBQoSAtmPvcGtsPassedBytes_Type = Counter64
_HwCBQoSAtmPvcGtsPassedBytes_Object = MibTableColumn
hwCBQoSAtmPvcGtsPassedBytes = _HwCBQoSAtmPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 2),
    _HwCBQoSAtmPvcGtsPassedBytes_Type()
)
hwCBQoSAtmPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsPassedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsDiscardedPackets_Type = Counter64
_HwCBQoSAtmPvcGtsDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcGtsDiscardedPackets = _HwCBQoSAtmPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 3),
    _HwCBQoSAtmPvcGtsDiscardedPackets_Type()
)
hwCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcGtsDiscardedBytes_Type = Counter64
_HwCBQoSAtmPvcGtsDiscardedBytes_Object = MibTableColumn
hwCBQoSAtmPvcGtsDiscardedBytes = _HwCBQoSAtmPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 4),
    _HwCBQoSAtmPvcGtsDiscardedBytes_Type()
)
hwCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDiscardedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsDelayedPackets_Type = Counter64
_HwCBQoSAtmPvcGtsDelayedPackets_Object = MibTableColumn
hwCBQoSAtmPvcGtsDelayedPackets = _HwCBQoSAtmPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 5),
    _HwCBQoSAtmPvcGtsDelayedPackets_Type()
)
hwCBQoSAtmPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDelayedPackets.setStatus("current")
_HwCBQoSAtmPvcGtsDelayedBytes_Type = Counter64
_HwCBQoSAtmPvcGtsDelayedBytes_Object = MibTableColumn
hwCBQoSAtmPvcGtsDelayedBytes = _HwCBQoSAtmPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 6),
    _HwCBQoSAtmPvcGtsDelayedBytes_Type()
)
hwCBQoSAtmPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDelayedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsQueueSize_Type = Integer32
_HwCBQoSAtmPvcGtsQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcGtsQueueSize = _HwCBQoSAtmPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 4, 1, 7),
    _HwCBQoSAtmPvcGtsQueueSize_Type()
)
hwCBQoSAtmPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsQueueSize.setStatus("current")
_HwCBQoSAtmPvcRemarkRunInfoTable_Object = MibTable
hwCBQoSAtmPvcRemarkRunInfoTable = _HwCBQoSAtmPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcRemarkRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcRemarkRunInfoEntry = _HwCBQoSAtmPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 5, 1)
)
hwCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcRemarkedPackets_Type = Counter64
_HwCBQoSAtmPvcRemarkedPackets_Object = MibTableColumn
hwCBQoSAtmPvcRemarkedPackets = _HwCBQoSAtmPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 5, 1, 1),
    _HwCBQoSAtmPvcRemarkedPackets_Type()
)
hwCBQoSAtmPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueRunInfoTable_Object = MibTable
hwCBQoSAtmPvcQueueRunInfoTable = _HwCBQoSAtmPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcQueueRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcQueueRunInfoEntry = _HwCBQoSAtmPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1)
)
hwCBQoSAtmPvcQueueRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcQueueMatchedPackets_Type = Counter64
_HwCBQoSAtmPvcQueueMatchedPackets_Object = MibTableColumn
hwCBQoSAtmPvcQueueMatchedPackets = _HwCBQoSAtmPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 1),
    _HwCBQoSAtmPvcQueueMatchedPackets_Type()
)
hwCBQoSAtmPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueMatchedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueMatchedBytes_Type = Counter64
_HwCBQoSAtmPvcQueueMatchedBytes_Object = MibTableColumn
hwCBQoSAtmPvcQueueMatchedBytes = _HwCBQoSAtmPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 2),
    _HwCBQoSAtmPvcQueueMatchedBytes_Type()
)
hwCBQoSAtmPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueMatchedBytes.setStatus("current")
_HwCBQoSAtmPvcQueueEnqueuedPackets_Type = Counter64
_HwCBQoSAtmPvcQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedPackets = _HwCBQoSAtmPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 3),
    _HwCBQoSAtmPvcQueueEnqueuedPackets_Type()
)
hwCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueEnqueuedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueEnqueuedBytes_Type = Counter64
_HwCBQoSAtmPvcQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedBytes = _HwCBQoSAtmPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 4),
    _HwCBQoSAtmPvcQueueEnqueuedBytes_Type()
)
hwCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueEnqueuedBytes.setStatus("current")
_HwCBQoSAtmPvcQueueDiscardedPackets_Type = Counter64
_HwCBQoSAtmPvcQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcQueueDiscardedPackets = _HwCBQoSAtmPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 5),
    _HwCBQoSAtmPvcQueueDiscardedPackets_Type()
)
hwCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueDiscardedBytes_Type = Counter64
_HwCBQoSAtmPvcQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSAtmPvcQueueDiscardedBytes = _HwCBQoSAtmPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 6),
    _HwCBQoSAtmPvcQueueDiscardedBytes_Type()
)
hwCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueDiscardedBytes.setStatus("current")
_HwCBQoSAtmPvcQueueMatchedPacketsRate_Type = Counter64
_HwCBQoSAtmPvcQueueMatchedPacketsRate_Object = MibTableColumn
hwCBQoSAtmPvcQueueMatchedPacketsRate = _HwCBQoSAtmPvcQueueMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 7),
    _HwCBQoSAtmPvcQueueMatchedPacketsRate_Type()
)
hwCBQoSAtmPvcQueueMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueMatchedPacketsRate.setStatus("current")
_HwCBQoSAtmPvcQueueMatchedBytesRate_Type = Counter64
_HwCBQoSAtmPvcQueueMatchedBytesRate_Object = MibTableColumn
hwCBQoSAtmPvcQueueMatchedBytesRate = _HwCBQoSAtmPvcQueueMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 8),
    _HwCBQoSAtmPvcQueueMatchedBytesRate_Type()
)
hwCBQoSAtmPvcQueueMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueMatchedBytesRate.setStatus("current")
_HwCBQoSAtmPvcQueueEnqueuedPacketsRate_Type = Counter64
_HwCBQoSAtmPvcQueueEnqueuedPacketsRate_Object = MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedPacketsRate = _HwCBQoSAtmPvcQueueEnqueuedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 9),
    _HwCBQoSAtmPvcQueueEnqueuedPacketsRate_Type()
)
hwCBQoSAtmPvcQueueEnqueuedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueEnqueuedPacketsRate.setStatus("current")
_HwCBQoSAtmPvcQueueEnqueuedBytesRate_Type = Counter64
_HwCBQoSAtmPvcQueueEnqueuedBytesRate_Object = MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedBytesRate = _HwCBQoSAtmPvcQueueEnqueuedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 10),
    _HwCBQoSAtmPvcQueueEnqueuedBytesRate_Type()
)
hwCBQoSAtmPvcQueueEnqueuedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueEnqueuedBytesRate.setStatus("current")
_HwCBQoSAtmPvcQueueDiscardedPacketsRate_Type = Counter64
_HwCBQoSAtmPvcQueueDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSAtmPvcQueueDiscardedPacketsRate = _HwCBQoSAtmPvcQueueDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 11),
    _HwCBQoSAtmPvcQueueDiscardedPacketsRate_Type()
)
hwCBQoSAtmPvcQueueDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueDiscardedPacketsRate.setStatus("current")
_HwCBQoSAtmPvcQueueDiscardedBytesRate_Type = Counter64
_HwCBQoSAtmPvcQueueDiscardedBytesRate_Object = MibTableColumn
hwCBQoSAtmPvcQueueDiscardedBytesRate = _HwCBQoSAtmPvcQueueDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 6, 1, 12),
    _HwCBQoSAtmPvcQueueDiscardedBytesRate_Type()
)
hwCBQoSAtmPvcQueueDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueDiscardedBytesRate.setStatus("current")
_HwCBQoSAtmPvcWredRunInfoTable_Object = MibTable
hwCBQoSAtmPvcWredRunInfoTable = _HwCBQoSAtmPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcWredRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcWredRunInfoEntry = _HwCBQoSAtmPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 7, 1)
)
hwCBQoSAtmPvcWredRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcWredRandomDiscardedPackets_Type = Counter64
_HwCBQoSAtmPvcWredRandomDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcWredRandomDiscardedPackets = _HwCBQoSAtmPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 7, 1, 1),
    _HwCBQoSAtmPvcWredRandomDiscardedPackets_Type()
)
hwCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRandomDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcWredTailDiscardedPackets_Type = Counter64
_HwCBQoSAtmPvcWredTailDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcWredTailDiscardedPackets = _HwCBQoSAtmPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 7, 1, 2),
    _HwCBQoSAtmPvcWredTailDiscardedPackets_Type()
)
hwCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredTailDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcLrRunInfoTable_Object = MibTable
hwCBQoSAtmPvcLrRunInfoTable = _HwCBQoSAtmPvcLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcLrRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcLrRunInfoEntry = _HwCBQoSAtmPvcLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1)
)
hwCBQoSAtmPvcLrRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcLrPassedPackets_Type = Counter64
_HwCBQoSAtmPvcLrPassedPackets_Object = MibTableColumn
hwCBQoSAtmPvcLrPassedPackets = _HwCBQoSAtmPvcLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1, 1),
    _HwCBQoSAtmPvcLrPassedPackets_Type()
)
hwCBQoSAtmPvcLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrPassedPackets.setStatus("current")
_HwCBQoSAtmPvcLrPassedBytes_Type = Counter64
_HwCBQoSAtmPvcLrPassedBytes_Object = MibTableColumn
hwCBQoSAtmPvcLrPassedBytes = _HwCBQoSAtmPvcLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1, 2),
    _HwCBQoSAtmPvcLrPassedBytes_Type()
)
hwCBQoSAtmPvcLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrPassedBytes.setStatus("current")
_HwCBQoSAtmPvcLrDiscardedPackets_Type = Counter64
_HwCBQoSAtmPvcLrDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcLrDiscardedPackets = _HwCBQoSAtmPvcLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1, 3),
    _HwCBQoSAtmPvcLrDiscardedPackets_Type()
)
hwCBQoSAtmPvcLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcLrDiscardedBytes_Type = Counter64
_HwCBQoSAtmPvcLrDiscardedBytes_Object = MibTableColumn
hwCBQoSAtmPvcLrDiscardedBytes = _HwCBQoSAtmPvcLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1, 4),
    _HwCBQoSAtmPvcLrDiscardedBytes_Type()
)
hwCBQoSAtmPvcLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDiscardedBytes.setStatus("current")
_HwCBQoSAtmPvcLrDelayedPackets_Type = Counter64
_HwCBQoSAtmPvcLrDelayedPackets_Object = MibTableColumn
hwCBQoSAtmPvcLrDelayedPackets = _HwCBQoSAtmPvcLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1, 5),
    _HwCBQoSAtmPvcLrDelayedPackets_Type()
)
hwCBQoSAtmPvcLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDelayedPackets.setStatus("current")
_HwCBQoSAtmPvcLrDelayedBytes_Type = Counter64
_HwCBQoSAtmPvcLrDelayedBytes_Object = MibTableColumn
hwCBQoSAtmPvcLrDelayedBytes = _HwCBQoSAtmPvcLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 2, 8, 1, 6),
    _HwCBQoSAtmPvcLrDelayedBytes_Type()
)
hwCBQoSAtmPvcLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDelayedBytes.setStatus("current")
_HwCBQoSFrPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSFrPvcStaticsObjects = _HwCBQoSFrPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3)
)
_HwCBQoSFrPvcCbqRunInfoTable_Object = MibTable
hwCBQoSFrPvcCbqRunInfoTable = _HwCBQoSFrPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqRunInfoTable.setStatus("current")
_HwCBQoSFrPvcCbqRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcCbqRunInfoEntry = _HwCBQoSFrPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1)
)
hwCBQoSFrPvcCbqRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcCbqQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqQueueSize = _HwCBQoSFrPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 1),
    _HwCBQoSFrPvcCbqQueueSize_Type()
)
hwCBQoSFrPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqDiscard_Type = Counter64
_HwCBQoSFrPvcCbqDiscard_Object = MibTableColumn
hwCBQoSFrPvcCbqDiscard = _HwCBQoSFrPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 2),
    _HwCBQoSFrPvcCbqDiscard_Type()
)
hwCBQoSFrPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqDiscard.setStatus("current")
_HwCBQoSFrPvcCbqEfQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqEfQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqEfQueueSize = _HwCBQoSFrPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 3),
    _HwCBQoSFrPvcCbqEfQueueSize_Type()
)
hwCBQoSFrPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqEfQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqAfQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqAfQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqAfQueueSize = _HwCBQoSFrPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 4),
    _HwCBQoSFrPvcCbqAfQueueSize_Type()
)
hwCBQoSFrPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqAfQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqBeQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqBeQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqBeQueueSize = _HwCBQoSFrPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 5),
    _HwCBQoSFrPvcCbqBeQueueSize_Type()
)
hwCBQoSFrPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqBeActiveQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqBeActiveQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqBeActiveQueueNum = _HwCBQoSFrPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 6),
    _HwCBQoSFrPvcCbqBeActiveQueueNum_Type()
)
hwCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeActiveQueueNum.setStatus("current")
_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqBeMaxActiveQueueNum = _HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 7),
    _HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Type()
)
hwCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus("current")
_HwCBQoSFrPvcCbqBeTotalQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqBeTotalQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqBeTotalQueueNum = _HwCBQoSFrPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 8),
    _HwCBQoSFrPvcCbqBeTotalQueueNum_Type()
)
hwCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeTotalQueueNum.setStatus("current")
_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqAfAllocatedQueueNum = _HwCBQoSFrPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 1, 1, 9),
    _HwCBQoSFrPvcCbqAfAllocatedQueueNum_Type()
)
hwCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus("current")
_HwCBQoSFrPvcClassMatchRunInfoTable_Object = MibTable
hwCBQoSFrPvcClassMatchRunInfoTable = _HwCBQoSFrPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchRunInfoTable.setStatus("current")
_HwCBQoSFrPvcClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcClassMatchRunInfoEntry = _HwCBQoSFrPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 2, 1)
)
hwCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcClassMatchedPackets_Type = Counter64
_HwCBQoSFrPvcClassMatchedPackets_Object = MibTableColumn
hwCBQoSFrPvcClassMatchedPackets = _HwCBQoSFrPvcClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 2, 1, 1),
    _HwCBQoSFrPvcClassMatchedPackets_Type()
)
hwCBQoSFrPvcClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchedPackets.setStatus("current")
_HwCBQoSFrPvcClassMatchedBytes_Type = Counter64
_HwCBQoSFrPvcClassMatchedBytes_Object = MibTableColumn
hwCBQoSFrPvcClassMatchedBytes = _HwCBQoSFrPvcClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 2, 1, 2),
    _HwCBQoSFrPvcClassMatchedBytes_Type()
)
hwCBQoSFrPvcClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchedBytes.setStatus("current")
_HwCBQoSFrPvcClassAverageRate_Type = Counter64
_HwCBQoSFrPvcClassAverageRate_Object = MibTableColumn
hwCBQoSFrPvcClassAverageRate = _HwCBQoSFrPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 2, 1, 3),
    _HwCBQoSFrPvcClassAverageRate_Type()
)
hwCBQoSFrPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassAverageRate.setStatus("current")
_HwCBQoSFrPvcCarRunInfoTable_Object = MibTable
hwCBQoSFrPvcCarRunInfoTable = _HwCBQoSFrPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarRunInfoTable.setStatus("current")
_HwCBQoSFrPvcCarRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcCarRunInfoEntry = _HwCBQoSFrPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1)
)
hwCBQoSFrPvcCarRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcCarConformPackets_Type = Counter64
_HwCBQoSFrPvcCarConformPackets_Object = MibTableColumn
hwCBQoSFrPvcCarConformPackets = _HwCBQoSFrPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 1),
    _HwCBQoSFrPvcCarConformPackets_Type()
)
hwCBQoSFrPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarConformPackets.setStatus("current")
_HwCBQoSFrPvcCarConformBytes_Type = Counter64
_HwCBQoSFrPvcCarConformBytes_Object = MibTableColumn
hwCBQoSFrPvcCarConformBytes = _HwCBQoSFrPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 2),
    _HwCBQoSFrPvcCarConformBytes_Type()
)
hwCBQoSFrPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarConformBytes.setStatus("current")
_HwCBQoSFrPvcCarExceedPackets_Type = Counter64
_HwCBQoSFrPvcCarExceedPackets_Object = MibTableColumn
hwCBQoSFrPvcCarExceedPackets = _HwCBQoSFrPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 3),
    _HwCBQoSFrPvcCarExceedPackets_Type()
)
hwCBQoSFrPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarExceedPackets.setStatus("current")
_HwCBQoSFrPvcCarExceedBytes_Type = Counter64
_HwCBQoSFrPvcCarExceedBytes_Object = MibTableColumn
hwCBQoSFrPvcCarExceedBytes = _HwCBQoSFrPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 4),
    _HwCBQoSFrPvcCarExceedBytes_Type()
)
hwCBQoSFrPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarExceedBytes.setStatus("current")
_HwCBQoSFrPvcCarConformPacketsRate_Type = Counter64
_HwCBQoSFrPvcCarConformPacketsRate_Object = MibTableColumn
hwCBQoSFrPvcCarConformPacketsRate = _HwCBQoSFrPvcCarConformPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 5),
    _HwCBQoSFrPvcCarConformPacketsRate_Type()
)
hwCBQoSFrPvcCarConformPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarConformPacketsRate.setStatus("current")
_HwCBQoSFrPvcCarConformBytesRate_Type = Counter64
_HwCBQoSFrPvcCarConformBytesRate_Object = MibTableColumn
hwCBQoSFrPvcCarConformBytesRate = _HwCBQoSFrPvcCarConformBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 6),
    _HwCBQoSFrPvcCarConformBytesRate_Type()
)
hwCBQoSFrPvcCarConformBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarConformBytesRate.setStatus("current")
_HwCBQoSFrPvcCarExceedPacketsRate_Type = Counter64
_HwCBQoSFrPvcCarExceedPacketsRate_Object = MibTableColumn
hwCBQoSFrPvcCarExceedPacketsRate = _HwCBQoSFrPvcCarExceedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 7),
    _HwCBQoSFrPvcCarExceedPacketsRate_Type()
)
hwCBQoSFrPvcCarExceedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarExceedPacketsRate.setStatus("current")
_HwCBQoSFrPvcCarExceedBytesRate_Type = Counter64
_HwCBQoSFrPvcCarExceedBytesRate_Object = MibTableColumn
hwCBQoSFrPvcCarExceedBytesRate = _HwCBQoSFrPvcCarExceedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 3, 1, 8),
    _HwCBQoSFrPvcCarExceedBytesRate_Type()
)
hwCBQoSFrPvcCarExceedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarExceedBytesRate.setStatus("current")
_HwCBQoSFrPvcGtsRunInfoTable_Object = MibTable
hwCBQoSFrPvcGtsRunInfoTable = _HwCBQoSFrPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsRunInfoTable.setStatus("current")
_HwCBQoSFrPvcGtsRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcGtsRunInfoEntry = _HwCBQoSFrPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1)
)
hwCBQoSFrPvcGtsRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcGtsPassedPackets_Type = Counter64
_HwCBQoSFrPvcGtsPassedPackets_Object = MibTableColumn
hwCBQoSFrPvcGtsPassedPackets = _HwCBQoSFrPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 1),
    _HwCBQoSFrPvcGtsPassedPackets_Type()
)
hwCBQoSFrPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsPassedPackets.setStatus("current")
_HwCBQoSFrPvcGtsPassedBytes_Type = Counter64
_HwCBQoSFrPvcGtsPassedBytes_Object = MibTableColumn
hwCBQoSFrPvcGtsPassedBytes = _HwCBQoSFrPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 2),
    _HwCBQoSFrPvcGtsPassedBytes_Type()
)
hwCBQoSFrPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsPassedBytes.setStatus("current")
_HwCBQoSFrPvcGtsDiscardedPackets_Type = Counter64
_HwCBQoSFrPvcGtsDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcGtsDiscardedPackets = _HwCBQoSFrPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 3),
    _HwCBQoSFrPvcGtsDiscardedPackets_Type()
)
hwCBQoSFrPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcGtsDiscardedBytes_Type = Counter64
_HwCBQoSFrPvcGtsDiscardedBytes_Object = MibTableColumn
hwCBQoSFrPvcGtsDiscardedBytes = _HwCBQoSFrPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 4),
    _HwCBQoSFrPvcGtsDiscardedBytes_Type()
)
hwCBQoSFrPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDiscardedBytes.setStatus("current")
_HwCBQoSFrPvcGtsDelayedPackets_Type = Counter64
_HwCBQoSFrPvcGtsDelayedPackets_Object = MibTableColumn
hwCBQoSFrPvcGtsDelayedPackets = _HwCBQoSFrPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 5),
    _HwCBQoSFrPvcGtsDelayedPackets_Type()
)
hwCBQoSFrPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDelayedPackets.setStatus("current")
_HwCBQoSFrPvcGtsDelayedBytes_Type = Counter64
_HwCBQoSFrPvcGtsDelayedBytes_Object = MibTableColumn
hwCBQoSFrPvcGtsDelayedBytes = _HwCBQoSFrPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 6),
    _HwCBQoSFrPvcGtsDelayedBytes_Type()
)
hwCBQoSFrPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDelayedBytes.setStatus("current")
_HwCBQoSFrPvcGtsQueueSize_Type = Integer32
_HwCBQoSFrPvcGtsQueueSize_Object = MibTableColumn
hwCBQoSFrPvcGtsQueueSize = _HwCBQoSFrPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 4, 1, 7),
    _HwCBQoSFrPvcGtsQueueSize_Type()
)
hwCBQoSFrPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsQueueSize.setStatus("current")
_HwCBQoSFrPvcRemarkRunInfoTable_Object = MibTable
hwCBQoSFrPvcRemarkRunInfoTable = _HwCBQoSFrPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkRunInfoTable.setStatus("current")
_HwCBQoSFrPvcRemarkRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcRemarkRunInfoEntry = _HwCBQoSFrPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 5, 1)
)
hwCBQoSFrPvcRemarkRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcRemarkedPackets_Type = Counter64
_HwCBQoSFrPvcRemarkedPackets_Object = MibTableColumn
hwCBQoSFrPvcRemarkedPackets = _HwCBQoSFrPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 5, 1, 1),
    _HwCBQoSFrPvcRemarkedPackets_Type()
)
hwCBQoSFrPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkedPackets.setStatus("current")
_HwCBQoSFrPvcQueueRunInfoTable_Object = MibTable
hwCBQoSFrPvcQueueRunInfoTable = _HwCBQoSFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueRunInfoTable.setStatus("current")
_HwCBQoSFrPvcQueueRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcQueueRunInfoEntry = _HwCBQoSFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1)
)
hwCBQoSFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcQueueMatchedPackets_Type = Counter64
_HwCBQoSFrPvcQueueMatchedPackets_Object = MibTableColumn
hwCBQoSFrPvcQueueMatchedPackets = _HwCBQoSFrPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 1),
    _HwCBQoSFrPvcQueueMatchedPackets_Type()
)
hwCBQoSFrPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueMatchedPackets.setStatus("current")
_HwCBQoSFrPvcQueueMatchedBytes_Type = Counter64
_HwCBQoSFrPvcQueueMatchedBytes_Object = MibTableColumn
hwCBQoSFrPvcQueueMatchedBytes = _HwCBQoSFrPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 2),
    _HwCBQoSFrPvcQueueMatchedBytes_Type()
)
hwCBQoSFrPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueMatchedBytes.setStatus("current")
_HwCBQoSFrPvcQueueEnqueuedPackets_Type = Counter64
_HwCBQoSFrPvcQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSFrPvcQueueEnqueuedPackets = _HwCBQoSFrPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 3),
    _HwCBQoSFrPvcQueueEnqueuedPackets_Type()
)
hwCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueEnqueuedPackets.setStatus("current")
_HwCBQoSFrPvcQueueEnqueuedBytes_Type = Counter64
_HwCBQoSFrPvcQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSFrPvcQueueEnqueuedBytes = _HwCBQoSFrPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 4),
    _HwCBQoSFrPvcQueueEnqueuedBytes_Type()
)
hwCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueEnqueuedBytes.setStatus("current")
_HwCBQoSFrPvcQueueDiscardedPackets_Type = Counter64
_HwCBQoSFrPvcQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcQueueDiscardedPackets = _HwCBQoSFrPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 5),
    _HwCBQoSFrPvcQueueDiscardedPackets_Type()
)
hwCBQoSFrPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcQueueDiscardedBytes_Type = Counter64
_HwCBQoSFrPvcQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSFrPvcQueueDiscardedBytes = _HwCBQoSFrPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 6),
    _HwCBQoSFrPvcQueueDiscardedBytes_Type()
)
hwCBQoSFrPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueDiscardedBytes.setStatus("current")
_HwCBQoSFrPvcQueueMatchedPacketsRate_Type = Counter64
_HwCBQoSFrPvcQueueMatchedPacketsRate_Object = MibTableColumn
hwCBQoSFrPvcQueueMatchedPacketsRate = _HwCBQoSFrPvcQueueMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 7),
    _HwCBQoSFrPvcQueueMatchedPacketsRate_Type()
)
hwCBQoSFrPvcQueueMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueMatchedPacketsRate.setStatus("current")
_HwCBQoSFrPvcQueueMatchedBytesRate_Type = Counter64
_HwCBQoSFrPvcQueueMatchedBytesRate_Object = MibTableColumn
hwCBQoSFrPvcQueueMatchedBytesRate = _HwCBQoSFrPvcQueueMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 8),
    _HwCBQoSFrPvcQueueMatchedBytesRate_Type()
)
hwCBQoSFrPvcQueueMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueMatchedBytesRate.setStatus("current")
_HwCBQoSFrPvcQueueEnqueuedPacketsRate_Type = Counter64
_HwCBQoSFrPvcQueueEnqueuedPacketsRate_Object = MibTableColumn
hwCBQoSFrPvcQueueEnqueuedPacketsRate = _HwCBQoSFrPvcQueueEnqueuedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 9),
    _HwCBQoSFrPvcQueueEnqueuedPacketsRate_Type()
)
hwCBQoSFrPvcQueueEnqueuedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueEnqueuedPacketsRate.setStatus("current")
_HwCBQoSFrPvcQueueEnqueuedBytesRate_Type = Counter64
_HwCBQoSFrPvcQueueEnqueuedBytesRate_Object = MibTableColumn
hwCBQoSFrPvcQueueEnqueuedBytesRate = _HwCBQoSFrPvcQueueEnqueuedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 10),
    _HwCBQoSFrPvcQueueEnqueuedBytesRate_Type()
)
hwCBQoSFrPvcQueueEnqueuedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueEnqueuedBytesRate.setStatus("current")
_HwCBQoSFrPvcQueueDiscardedPacketsRate_Type = Counter64
_HwCBQoSFrPvcQueueDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSFrPvcQueueDiscardedPacketsRate = _HwCBQoSFrPvcQueueDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 11),
    _HwCBQoSFrPvcQueueDiscardedPacketsRate_Type()
)
hwCBQoSFrPvcQueueDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueDiscardedPacketsRate.setStatus("current")
_HwCBQoSFrPvcQueueDiscardedBytesRate_Type = Counter64
_HwCBQoSFrPvcQueueDiscardedBytesRate_Object = MibTableColumn
hwCBQoSFrPvcQueueDiscardedBytesRate = _HwCBQoSFrPvcQueueDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 6, 1, 12),
    _HwCBQoSFrPvcQueueDiscardedBytesRate_Type()
)
hwCBQoSFrPvcQueueDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueDiscardedBytesRate.setStatus("current")
_HwCBQoSFrPvcWredRunInfoTable_Object = MibTable
hwCBQoSFrPvcWredRunInfoTable = _HwCBQoSFrPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRunInfoTable.setStatus("current")
_HwCBQoSFrPvcWredRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcWredRunInfoEntry = _HwCBQoSFrPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 7, 1)
)
hwCBQoSFrPvcWredRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcWredRandomDiscardedPackets_Type = Counter64
_HwCBQoSFrPvcWredRandomDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcWredRandomDiscardedPackets = _HwCBQoSFrPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 7, 1, 1),
    _HwCBQoSFrPvcWredRandomDiscardedPackets_Type()
)
hwCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRandomDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcWredTailDiscardedPackets_Type = Counter64
_HwCBQoSFrPvcWredTailDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcWredTailDiscardedPackets = _HwCBQoSFrPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 7, 1, 2),
    _HwCBQoSFrPvcWredTailDiscardedPackets_Type()
)
hwCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredTailDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcLrRunInfoTable_Object = MibTable
hwCBQoSFrPvcLrRunInfoTable = _HwCBQoSFrPvcLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrRunInfoTable.setStatus("current")
_HwCBQoSFrPvcLrRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcLrRunInfoEntry = _HwCBQoSFrPvcLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1)
)
hwCBQoSFrPvcLrRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcLrPassedPackets_Type = Counter64
_HwCBQoSFrPvcLrPassedPackets_Object = MibTableColumn
hwCBQoSFrPvcLrPassedPackets = _HwCBQoSFrPvcLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1, 1),
    _HwCBQoSFrPvcLrPassedPackets_Type()
)
hwCBQoSFrPvcLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrPassedPackets.setStatus("current")
_HwCBQoSFrPvcLrPassedBytes_Type = Counter64
_HwCBQoSFrPvcLrPassedBytes_Object = MibTableColumn
hwCBQoSFrPvcLrPassedBytes = _HwCBQoSFrPvcLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1, 2),
    _HwCBQoSFrPvcLrPassedBytes_Type()
)
hwCBQoSFrPvcLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrPassedBytes.setStatus("current")
_HwCBQoSFrPvcLrDiscardedPackets_Type = Counter64
_HwCBQoSFrPvcLrDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcLrDiscardedPackets = _HwCBQoSFrPvcLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1, 3),
    _HwCBQoSFrPvcLrDiscardedPackets_Type()
)
hwCBQoSFrPvcLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcLrDiscardedBytes_Type = Counter64
_HwCBQoSFrPvcLrDiscardedBytes_Object = MibTableColumn
hwCBQoSFrPvcLrDiscardedBytes = _HwCBQoSFrPvcLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1, 4),
    _HwCBQoSFrPvcLrDiscardedBytes_Type()
)
hwCBQoSFrPvcLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDiscardedBytes.setStatus("current")
_HwCBQoSFrPvcLrDelayedPackets_Type = Counter64
_HwCBQoSFrPvcLrDelayedPackets_Object = MibTableColumn
hwCBQoSFrPvcLrDelayedPackets = _HwCBQoSFrPvcLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1, 5),
    _HwCBQoSFrPvcLrDelayedPackets_Type()
)
hwCBQoSFrPvcLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDelayedPackets.setStatus("current")
_HwCBQoSFrPvcLrDelayedBytes_Type = Counter64
_HwCBQoSFrPvcLrDelayedBytes_Object = MibTableColumn
hwCBQoSFrPvcLrDelayedBytes = _HwCBQoSFrPvcLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 3, 8, 1, 6),
    _HwCBQoSFrPvcLrDelayedBytes_Type()
)
hwCBQoSFrPvcLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDelayedBytes.setStatus("current")
_HwCBQoSIfVlanStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSIfVlanStaticsObjects = _HwCBQoSIfVlanStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 4)
)
_HwCBQoSIfVlanClassMatchRunInfoTable_Object = MibTable
hwCBQoSIfVlanClassMatchRunInfoTable = _HwCBQoSIfVlanClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchRunInfoTable.setStatus("current")
_HwCBQoSIfVlanClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSIfVlanClassMatchRunInfoEntry = _HwCBQoSIfVlanClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 4, 1, 1)
)
hwCBQoSIfVlanClassMatchRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSIfVlanClassMatchedPackets_Type = Counter64
_HwCBQoSIfVlanClassMatchedPackets_Object = MibTableColumn
hwCBQoSIfVlanClassMatchedPackets = _HwCBQoSIfVlanClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 4, 1, 1, 1),
    _HwCBQoSIfVlanClassMatchedPackets_Type()
)
hwCBQoSIfVlanClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchedPackets.setStatus("current")
_HwCBQoSIfVlanClassMatchedBytes_Type = Counter64
_HwCBQoSIfVlanClassMatchedBytes_Object = MibTableColumn
hwCBQoSIfVlanClassMatchedBytes = _HwCBQoSIfVlanClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 4, 1, 1, 2),
    _HwCBQoSIfVlanClassMatchedBytes_Type()
)
hwCBQoSIfVlanClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchedBytes.setStatus("current")
_HwCBQoSVsiStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSVsiStaticsObjects = _HwCBQoSVsiStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 5)
)
_HwCBQoSVsiClassMatchRunInfoTable_Object = MibTable
hwCBQoSVsiClassMatchRunInfoTable = _HwCBQoSVsiClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSVsiClassMatchRunInfoTable.setStatus("current")
_HwCBQoSVsiClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSVsiClassMatchRunInfoEntry = _HwCBQoSVsiClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 5, 1, 1)
)
hwCBQoSVsiClassMatchRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVsiApplyPolicyVsiIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVsiApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSVsiClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSVsiClassMatchedPackets_Type = Counter64
_HwCBQoSVsiClassMatchedPackets_Object = MibTableColumn
hwCBQoSVsiClassMatchedPackets = _HwCBQoSVsiClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 5, 1, 1, 1),
    _HwCBQoSVsiClassMatchedPackets_Type()
)
hwCBQoSVsiClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVsiClassMatchedPackets.setStatus("current")
_HwCBQoSVsiClassMatchedBytes_Type = Counter64
_HwCBQoSVsiClassMatchedBytes_Object = MibTableColumn
hwCBQoSVsiClassMatchedBytes = _HwCBQoSVsiClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 5, 1, 1, 2),
    _HwCBQoSVsiClassMatchedBytes_Type()
)
hwCBQoSVsiClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVsiClassMatchedBytes.setStatus("current")
_HwCBQoSPolicyStatisticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSPolicyStatisticsObjects = _HwCBQoSPolicyStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6)
)
_HwCBQoSCarStatisticsTable_Object = MibTable
hwCBQoSCarStatisticsTable = _HwCBQoSCarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSCarStatisticsTable.setStatus("current")
_HwCBQoSCarStatisticsEntry_Object = MibTableRow
hwCBQoSCarStatisticsEntry = _HwCBQoSCarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1)
)
hwCBQoSCarStatisticsEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid2"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSCarStatisticsEntry.setStatus("current")
_HwCBQoSCarConformedPackets_Type = Counter64
_HwCBQoSCarConformedPackets_Object = MibTableColumn
hwCBQoSCarConformedPackets = _HwCBQoSCarConformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 11),
    _HwCBQoSCarConformedPackets_Type()
)
hwCBQoSCarConformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarConformedPackets.setStatus("current")
_HwCBQoSCarConformedBytes_Type = Counter64
_HwCBQoSCarConformedBytes_Object = MibTableColumn
hwCBQoSCarConformedBytes = _HwCBQoSCarConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 12),
    _HwCBQoSCarConformedBytes_Type()
)
hwCBQoSCarConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarConformedBytes.setStatus("current")
_HwCBQoSCarConformedPacketRate_Type = Counter64
_HwCBQoSCarConformedPacketRate_Object = MibTableColumn
hwCBQoSCarConformedPacketRate = _HwCBQoSCarConformedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 13),
    _HwCBQoSCarConformedPacketRate_Type()
)
hwCBQoSCarConformedPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarConformedPacketRate.setStatus("current")
_HwCBQoSCarConformedByteRate_Type = Counter64
_HwCBQoSCarConformedByteRate_Object = MibTableColumn
hwCBQoSCarConformedByteRate = _HwCBQoSCarConformedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 14),
    _HwCBQoSCarConformedByteRate_Type()
)
hwCBQoSCarConformedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarConformedByteRate.setStatus("current")
_HwCBQoSCarExceededPackets_Type = Counter64
_HwCBQoSCarExceededPackets_Object = MibTableColumn
hwCBQoSCarExceededPackets = _HwCBQoSCarExceededPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 15),
    _HwCBQoSCarExceededPackets_Type()
)
hwCBQoSCarExceededPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarExceededPackets.setStatus("current")
_HwCBQoSCarExceededBytes_Type = Counter64
_HwCBQoSCarExceededBytes_Object = MibTableColumn
hwCBQoSCarExceededBytes = _HwCBQoSCarExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 16),
    _HwCBQoSCarExceededBytes_Type()
)
hwCBQoSCarExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarExceededBytes.setStatus("current")
_HwCBQoSCarExceededPacketRate_Type = Counter64
_HwCBQoSCarExceededPacketRate_Object = MibTableColumn
hwCBQoSCarExceededPacketRate = _HwCBQoSCarExceededPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 17),
    _HwCBQoSCarExceededPacketRate_Type()
)
hwCBQoSCarExceededPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarExceededPacketRate.setStatus("current")
_HwCBQoSCarExceededByteRate_Type = Counter64
_HwCBQoSCarExceededByteRate_Object = MibTableColumn
hwCBQoSCarExceededByteRate = _HwCBQoSCarExceededByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 18),
    _HwCBQoSCarExceededByteRate_Type()
)
hwCBQoSCarExceededByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarExceededByteRate.setStatus("current")
_HwCBQoSCarOverflowPackets_Type = Counter64
_HwCBQoSCarOverflowPackets_Object = MibTableColumn
hwCBQoSCarOverflowPackets = _HwCBQoSCarOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 19),
    _HwCBQoSCarOverflowPackets_Type()
)
hwCBQoSCarOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarOverflowPackets.setStatus("current")
_HwCBQoSCarOverflowBytes_Type = Counter64
_HwCBQoSCarOverflowBytes_Object = MibTableColumn
hwCBQoSCarOverflowBytes = _HwCBQoSCarOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 20),
    _HwCBQoSCarOverflowBytes_Type()
)
hwCBQoSCarOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarOverflowBytes.setStatus("current")
_HwCBQoSCarOverflowPacketRate_Type = Counter64
_HwCBQoSCarOverflowPacketRate_Object = MibTableColumn
hwCBQoSCarOverflowPacketRate = _HwCBQoSCarOverflowPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 21),
    _HwCBQoSCarOverflowPacketRate_Type()
)
hwCBQoSCarOverflowPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarOverflowPacketRate.setStatus("current")
_HwCBQoSCarOverflowByteRate_Type = Counter64
_HwCBQoSCarOverflowByteRate_Object = MibTableColumn
hwCBQoSCarOverflowByteRate = _HwCBQoSCarOverflowByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 22),
    _HwCBQoSCarOverflowByteRate_Type()
)
hwCBQoSCarOverflowByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarOverflowByteRate.setStatus("current")
_HwCBQoSCarPassedPackets_Type = Counter64
_HwCBQoSCarPassedPackets_Object = MibTableColumn
hwCBQoSCarPassedPackets = _HwCBQoSCarPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 23),
    _HwCBQoSCarPassedPackets_Type()
)
hwCBQoSCarPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarPassedPackets.setStatus("current")
_HwCBQoSCarPassedBytes_Type = Counter64
_HwCBQoSCarPassedBytes_Object = MibTableColumn
hwCBQoSCarPassedBytes = _HwCBQoSCarPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 24),
    _HwCBQoSCarPassedBytes_Type()
)
hwCBQoSCarPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarPassedBytes.setStatus("current")
_HwCBQoSCarDroppedPackets_Type = Counter64
_HwCBQoSCarDroppedPackets_Object = MibTableColumn
hwCBQoSCarDroppedPackets = _HwCBQoSCarDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 25),
    _HwCBQoSCarDroppedPackets_Type()
)
hwCBQoSCarDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarDroppedPackets.setStatus("current")
_HwCBQoSCarDroppedBytes_Type = Counter64
_HwCBQoSCarDroppedBytes_Object = MibTableColumn
hwCBQoSCarDroppedBytes = _HwCBQoSCarDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 1, 1, 26),
    _HwCBQoSCarDroppedBytes_Type()
)
hwCBQoSCarDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSCarDroppedBytes.setStatus("current")
_HwCBQoSPolicyStatisticsTable_Object = MibTable
hwCBQoSPolicyStatisticsTable = _HwCBQoSPolicyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsTable.setStatus("current")
_HwCBQoSPolicyStatisticsEntry_Object = MibTableRow
hwCBQoSPolicyStatisticsEntry = _HwCBQoSPolicyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1)
)
hwCBQoSPolicyStatisticsEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid2"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsEntry.setStatus("current")
_HwCBQoSPolicyMatchedPackets_Type = Counter64
_HwCBQoSPolicyMatchedPackets_Object = MibTableColumn
hwCBQoSPolicyMatchedPackets = _HwCBQoSPolicyMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 11),
    _HwCBQoSPolicyMatchedPackets_Type()
)
hwCBQoSPolicyMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedPackets.setStatus("current")
_HwCBQoSPolicyMatchedBytes_Type = Counter64
_HwCBQoSPolicyMatchedBytes_Object = MibTableColumn
hwCBQoSPolicyMatchedBytes = _HwCBQoSPolicyMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 12),
    _HwCBQoSPolicyMatchedBytes_Type()
)
hwCBQoSPolicyMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedBytes.setStatus("current")
_HwCBQoSPolicyUnmatchedPackets_Type = Counter64
_HwCBQoSPolicyUnmatchedPackets_Object = MibTableColumn
hwCBQoSPolicyUnmatchedPackets = _HwCBQoSPolicyUnmatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 13),
    _HwCBQoSPolicyUnmatchedPackets_Type()
)
hwCBQoSPolicyUnmatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyUnmatchedPackets.setStatus("current")
_HwCBQoSPolicyUnmatchedBytes_Type = Counter64
_HwCBQoSPolicyUnmatchedBytes_Object = MibTableColumn
hwCBQoSPolicyUnmatchedBytes = _HwCBQoSPolicyUnmatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 14),
    _HwCBQoSPolicyUnmatchedBytes_Type()
)
hwCBQoSPolicyUnmatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyUnmatchedBytes.setStatus("current")
_HwCBQoSPolicyMatchedPassPackets_Type = Counter64
_HwCBQoSPolicyMatchedPassPackets_Object = MibTableColumn
hwCBQoSPolicyMatchedPassPackets = _HwCBQoSPolicyMatchedPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 15),
    _HwCBQoSPolicyMatchedPassPackets_Type()
)
hwCBQoSPolicyMatchedPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedPassPackets.setStatus("current")
_HwCBQoSPolicyMatchedPassBytes_Type = Counter64
_HwCBQoSPolicyMatchedPassBytes_Object = MibTableColumn
hwCBQoSPolicyMatchedPassBytes = _HwCBQoSPolicyMatchedPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 16),
    _HwCBQoSPolicyMatchedPassBytes_Type()
)
hwCBQoSPolicyMatchedPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedPassBytes.setStatus("current")
_HwCBQoSPolicyMatchedDropPackets_Type = Counter64
_HwCBQoSPolicyMatchedDropPackets_Object = MibTableColumn
hwCBQoSPolicyMatchedDropPackets = _HwCBQoSPolicyMatchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 17),
    _HwCBQoSPolicyMatchedDropPackets_Type()
)
hwCBQoSPolicyMatchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedDropPackets.setStatus("current")
_HwCBQoSPolicyMatchedDropBytes_Type = Counter64
_HwCBQoSPolicyMatchedDropBytes_Object = MibTableColumn
hwCBQoSPolicyMatchedDropBytes = _HwCBQoSPolicyMatchedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 18),
    _HwCBQoSPolicyMatchedDropBytes_Type()
)
hwCBQoSPolicyMatchedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedDropBytes.setStatus("current")
_HwCBQoSPolicyResetFlag_Type = EnabledStatus
_HwCBQoSPolicyResetFlag_Object = MibTableColumn
hwCBQoSPolicyResetFlag = _HwCBQoSPolicyResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 19),
    _HwCBQoSPolicyResetFlag_Type()
)
hwCBQoSPolicyResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSPolicyResetFlag.setStatus("current")
_HwCBQoSPolicyMatchedPacketsRate_Type = Counter64
_HwCBQoSPolicyMatchedPacketsRate_Object = MibTableColumn
hwCBQoSPolicyMatchedPacketsRate = _HwCBQoSPolicyMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 20),
    _HwCBQoSPolicyMatchedPacketsRate_Type()
)
hwCBQoSPolicyMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedPacketsRate.setStatus("current")
_HwCBQoSPolicyMatchedBytesRate_Type = Counter64
_HwCBQoSPolicyMatchedBytesRate_Object = MibTableColumn
hwCBQoSPolicyMatchedBytesRate = _HwCBQoSPolicyMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 21),
    _HwCBQoSPolicyMatchedBytesRate_Type()
)
hwCBQoSPolicyMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedBytesRate.setStatus("current")
_HwCBQoSPolicyMatchedPassPacketsRate_Type = Counter64
_HwCBQoSPolicyMatchedPassPacketsRate_Object = MibTableColumn
hwCBQoSPolicyMatchedPassPacketsRate = _HwCBQoSPolicyMatchedPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 22),
    _HwCBQoSPolicyMatchedPassPacketsRate_Type()
)
hwCBQoSPolicyMatchedPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedPassPacketsRate.setStatus("current")
_HwCBQoSPolicyMatchedPassBytesRate_Type = Counter64
_HwCBQoSPolicyMatchedPassBytesRate_Object = MibTableColumn
hwCBQoSPolicyMatchedPassBytesRate = _HwCBQoSPolicyMatchedPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 23),
    _HwCBQoSPolicyMatchedPassBytesRate_Type()
)
hwCBQoSPolicyMatchedPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedPassBytesRate.setStatus("current")
_HwCBQoSPolicyMatchedDropPacketsRate_Type = Counter64
_HwCBQoSPolicyMatchedDropPacketsRate_Object = MibTableColumn
hwCBQoSPolicyMatchedDropPacketsRate = _HwCBQoSPolicyMatchedDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 24),
    _HwCBQoSPolicyMatchedDropPacketsRate_Type()
)
hwCBQoSPolicyMatchedDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedDropPacketsRate.setStatus("current")
_HwCBQoSPolicyMatchedDropBytesRate_Type = Counter64
_HwCBQoSPolicyMatchedDropBytesRate_Object = MibTableColumn
hwCBQoSPolicyMatchedDropBytesRate = _HwCBQoSPolicyMatchedDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 2, 1, 25),
    _HwCBQoSPolicyMatchedDropBytesRate_Type()
)
hwCBQoSPolicyMatchedDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyMatchedDropBytesRate.setStatus("current")
_HwCBQoSClassifierStatisticsTable_Object = MibTable
hwCBQoSClassifierStatisticsTable = _HwCBQoSClassifierStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierStatisticsTable.setStatus("current")
_HwCBQoSClassifierStatisticsEntry_Object = MibTableRow
hwCBQoSClassifierStatisticsEntry = _HwCBQoSClassifierStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1)
)
hwCBQoSClassifierStatisticsEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid2"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassifierIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierStatisticsEntry.setStatus("current")
_HwCBQoSPolicyClassifierIndex_Type = Integer32
_HwCBQoSPolicyClassifierIndex_Object = MibTableColumn
hwCBQoSPolicyClassifierIndex = _HwCBQoSPolicyClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 4),
    _HwCBQoSPolicyClassifierIndex_Type()
)
hwCBQoSPolicyClassifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassifierIndex.setStatus("current")
_HwCBQoSClassifierMatchedPackets_Type = Counter64
_HwCBQoSClassifierMatchedPackets_Object = MibTableColumn
hwCBQoSClassifierMatchedPackets = _HwCBQoSClassifierMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 5),
    _HwCBQoSClassifierMatchedPackets_Type()
)
hwCBQoSClassifierMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierMatchedPackets.setStatus("current")
_HwCBQoSClassifierMatchedBytes_Type = Counter64
_HwCBQoSClassifierMatchedBytes_Object = MibTableColumn
hwCBQoSClassifierMatchedBytes = _HwCBQoSClassifierMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 6),
    _HwCBQoSClassifierMatchedBytes_Type()
)
hwCBQoSClassifierMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierMatchedBytes.setStatus("current")
_HwCBQoSClassifierMatchedPassPackets_Type = Counter64
_HwCBQoSClassifierMatchedPassPackets_Object = MibTableColumn
hwCBQoSClassifierMatchedPassPackets = _HwCBQoSClassifierMatchedPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 7),
    _HwCBQoSClassifierMatchedPassPackets_Type()
)
hwCBQoSClassifierMatchedPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierMatchedPassPackets.setStatus("current")
_HwCBQoSClassifierMatchedPassBytes_Type = Counter64
_HwCBQoSClassifierMatchedPassBytes_Object = MibTableColumn
hwCBQoSClassifierMatchedPassBytes = _HwCBQoSClassifierMatchedPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 8),
    _HwCBQoSClassifierMatchedPassBytes_Type()
)
hwCBQoSClassifierMatchedPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierMatchedPassBytes.setStatus("current")
_HwCBQoSClassifierMatchedDropPackets_Type = Counter64
_HwCBQoSClassifierMatchedDropPackets_Object = MibTableColumn
hwCBQoSClassifierMatchedDropPackets = _HwCBQoSClassifierMatchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 9),
    _HwCBQoSClassifierMatchedDropPackets_Type()
)
hwCBQoSClassifierMatchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierMatchedDropPackets.setStatus("current")
_HwCBQoSClassifierMatchedDropBytes_Type = Counter64
_HwCBQoSClassifierMatchedDropBytes_Object = MibTableColumn
hwCBQoSClassifierMatchedDropBytes = _HwCBQoSClassifierMatchedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 3, 1, 10),
    _HwCBQoSClassifierMatchedDropBytes_Type()
)
hwCBQoSClassifierMatchedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierMatchedDropBytes.setStatus("current")
_HwCBQoSPolicyStatisticsClassifierTable_Object = MibTable
hwCBQoSPolicyStatisticsClassifierTable = _HwCBQoSPolicyStatisticsClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsClassifierTable.setStatus("current")
_HwCBQoSPolicyStatisticsClassifierEntry_Object = MibTableRow
hwCBQoSPolicyStatisticsClassifierEntry = _HwCBQoSPolicyStatisticsClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1)
)
hwCBQoSPolicyStatisticsClassifierEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierName"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsClassifierEntry.setStatus("current")


class _HwCBQoSPolicyStatClassifierName_Type(OctetString):
    """Custom type hwCBQoSPolicyStatClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSPolicyStatClassifierName_Type.__name__ = "OctetString"
_HwCBQoSPolicyStatClassifierName_Object = MibTableColumn
hwCBQoSPolicyStatClassifierName = _HwCBQoSPolicyStatClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 1),
    _HwCBQoSPolicyStatClassifierName_Type()
)
hwCBQoSPolicyStatClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierName.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedPackets_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedPackets_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedPackets = _HwCBQoSPolicyStatClassifierMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 2),
    _HwCBQoSPolicyStatClassifierMatchedPackets_Type()
)
hwCBQoSPolicyStatClassifierMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedPackets.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedBytes_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedBytes_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedBytes = _HwCBQoSPolicyStatClassifierMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 3),
    _HwCBQoSPolicyStatClassifierMatchedBytes_Type()
)
hwCBQoSPolicyStatClassifierMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedBytes.setStatus("current")
_HwCBQoSPolicyStatClassifierUnmatchedPackets_Type = Counter64
_HwCBQoSPolicyStatClassifierUnmatchedPackets_Object = MibTableColumn
hwCBQoSPolicyStatClassifierUnmatchedPackets = _HwCBQoSPolicyStatClassifierUnmatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 4),
    _HwCBQoSPolicyStatClassifierUnmatchedPackets_Type()
)
hwCBQoSPolicyStatClassifierUnmatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierUnmatchedPackets.setStatus("current")
_HwCBQoSPolicyStatClassifierUnmatchedBytes_Type = Counter64
_HwCBQoSPolicyStatClassifierUnmatchedBytes_Object = MibTableColumn
hwCBQoSPolicyStatClassifierUnmatchedBytes = _HwCBQoSPolicyStatClassifierUnmatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 5),
    _HwCBQoSPolicyStatClassifierUnmatchedBytes_Type()
)
hwCBQoSPolicyStatClassifierUnmatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierUnmatchedBytes.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedPassPackets_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedPassPackets_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedPassPackets = _HwCBQoSPolicyStatClassifierMatchedPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 6),
    _HwCBQoSPolicyStatClassifierMatchedPassPackets_Type()
)
hwCBQoSPolicyStatClassifierMatchedPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedPassPackets.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedPassBytes_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedPassBytes_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedPassBytes = _HwCBQoSPolicyStatClassifierMatchedPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 7),
    _HwCBQoSPolicyStatClassifierMatchedPassBytes_Type()
)
hwCBQoSPolicyStatClassifierMatchedPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedPassBytes.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedDropPackets_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedDropPackets_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedDropPackets = _HwCBQoSPolicyStatClassifierMatchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 8),
    _HwCBQoSPolicyStatClassifierMatchedDropPackets_Type()
)
hwCBQoSPolicyStatClassifierMatchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedDropPackets.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedDropBytes_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedDropBytes_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedDropBytes = _HwCBQoSPolicyStatClassifierMatchedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 9),
    _HwCBQoSPolicyStatClassifierMatchedDropBytes_Type()
)
hwCBQoSPolicyStatClassifierMatchedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedDropBytes.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedPacketsRate_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedPacketsRate_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedPacketsRate = _HwCBQoSPolicyStatClassifierMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 10),
    _HwCBQoSPolicyStatClassifierMatchedPacketsRate_Type()
)
hwCBQoSPolicyStatClassifierMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedPacketsRate.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedBytesRate_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedBytesRate_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedBytesRate = _HwCBQoSPolicyStatClassifierMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 11),
    _HwCBQoSPolicyStatClassifierMatchedBytesRate_Type()
)
hwCBQoSPolicyStatClassifierMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedBytesRate.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedPassPacketsRate_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedPassPacketsRate_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedPassPacketsRate = _HwCBQoSPolicyStatClassifierMatchedPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 12),
    _HwCBQoSPolicyStatClassifierMatchedPassPacketsRate_Type()
)
hwCBQoSPolicyStatClassifierMatchedPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedPassPacketsRate.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedPassBytesRate_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedPassBytesRate_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedPassBytesRate = _HwCBQoSPolicyStatClassifierMatchedPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 13),
    _HwCBQoSPolicyStatClassifierMatchedPassBytesRate_Type()
)
hwCBQoSPolicyStatClassifierMatchedPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedPassBytesRate.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedDropPacketsRate_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedDropPacketsRate_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedDropPacketsRate = _HwCBQoSPolicyStatClassifierMatchedDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 14),
    _HwCBQoSPolicyStatClassifierMatchedDropPacketsRate_Type()
)
hwCBQoSPolicyStatClassifierMatchedDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedDropPacketsRate.setStatus("current")
_HwCBQoSPolicyStatClassifierMatchedDropBytesRate_Type = Counter64
_HwCBQoSPolicyStatClassifierMatchedDropBytesRate_Object = MibTableColumn
hwCBQoSPolicyStatClassifierMatchedDropBytesRate = _HwCBQoSPolicyStatClassifierMatchedDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 4, 1, 15),
    _HwCBQoSPolicyStatClassifierMatchedDropBytesRate_Type()
)
hwCBQoSPolicyStatClassifierMatchedDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatClassifierMatchedDropBytesRate.setStatus("current")
_HwCBQoSVlanClassMatchRunInfoTable_Object = MibTable
hwCBQoSVlanClassMatchRunInfoTable = _HwCBQoSVlanClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSVlanClassMatchRunInfoTable.setStatus("current")
_HwCBQoSVlanClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSVlanClassMatchRunInfoEntry = _HwCBQoSVlanClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 5, 1)
)
hwCBQoSVlanClassMatchRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyVlanId"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSVlanClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSVlanClassMatchedPackets_Type = Counter64
_HwCBQoSVlanClassMatchedPackets_Object = MibTableColumn
hwCBQoSVlanClassMatchedPackets = _HwCBQoSVlanClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 5, 1, 1),
    _HwCBQoSVlanClassMatchedPackets_Type()
)
hwCBQoSVlanClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanClassMatchedPackets.setStatus("current")
_HwCBQoSVlanClassPassedPackets_Type = Counter64
_HwCBQoSVlanClassPassedPackets_Object = MibTableColumn
hwCBQoSVlanClassPassedPackets = _HwCBQoSVlanClassPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 5, 1, 2),
    _HwCBQoSVlanClassPassedPackets_Type()
)
hwCBQoSVlanClassPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanClassPassedPackets.setStatus("current")
_HwCBQoSVlanClassDroppedPackets_Type = Counter64
_HwCBQoSVlanClassDroppedPackets_Object = MibTableColumn
hwCBQoSVlanClassDroppedPackets = _HwCBQoSVlanClassDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 5, 1, 3),
    _HwCBQoSVlanClassDroppedPackets_Type()
)
hwCBQoSVlanClassDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanClassDroppedPackets.setStatus("current")
_HwCBQoSVlanCarRunInfoTable_Object = MibTable
hwCBQoSVlanCarRunInfoTable = _HwCBQoSVlanCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSVlanCarRunInfoTable.setStatus("current")
_HwCBQoSVlanCarRunInfoEntry_Object = MibTableRow
hwCBQoSVlanCarRunInfoEntry = _HwCBQoSVlanCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 6, 1)
)
hwCBQoSVlanCarRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyVlanId"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSVlanCarRunInfoEntry.setStatus("current")
_HwCBQoSVlanCarPassedPackets_Type = Counter64
_HwCBQoSVlanCarPassedPackets_Object = MibTableColumn
hwCBQoSVlanCarPassedPackets = _HwCBQoSVlanCarPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 6, 1, 1),
    _HwCBQoSVlanCarPassedPackets_Type()
)
hwCBQoSVlanCarPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanCarPassedPackets.setStatus("current")
_HwCBQoSVlanCarDiscardedPackets_Type = Counter64
_HwCBQoSVlanCarDiscardedPackets_Object = MibTableColumn
hwCBQoSVlanCarDiscardedPackets = _HwCBQoSVlanCarDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 6, 1, 2),
    _HwCBQoSVlanCarDiscardedPackets_Type()
)
hwCBQoSVlanCarDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSVlanCarDiscardedPackets.setStatus("current")
_HwCBQoSMultiPolicyStatisticsTable_Object = MibTable
hwCBQoSMultiPolicyStatisticsTable = _HwCBQoSMultiPolicyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatisticsTable.setStatus("current")
_HwCBQoSMultiPolicyStatisticsEntry_Object = MibTableRow
hwCBQoSMultiPolicyStatisticsEntry = _HwCBQoSMultiPolicyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1)
)
hwCBQoSMultiPolicyStatisticsEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyMultiPolicyVlanId"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSMultiPolicyIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatisticsEntry.setStatus("current")
_HwCBQoSMultiPolicyIndex_Type = Integer32
_HwCBQoSMultiPolicyIndex_Object = MibTableColumn
hwCBQoSMultiPolicyIndex = _HwCBQoSMultiPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 11),
    _HwCBQoSMultiPolicyIndex_Type()
)
hwCBQoSMultiPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyIndex.setStatus("current")
_HwCBQoSMultiPolicyMatchedPackets_Type = Counter64
_HwCBQoSMultiPolicyMatchedPackets_Object = MibTableColumn
hwCBQoSMultiPolicyMatchedPackets = _HwCBQoSMultiPolicyMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 12),
    _HwCBQoSMultiPolicyMatchedPackets_Type()
)
hwCBQoSMultiPolicyMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyMatchedPackets.setStatus("current")
_HwCBQoSMultiPolicyMatchedBytes_Type = Counter64
_HwCBQoSMultiPolicyMatchedBytes_Object = MibTableColumn
hwCBQoSMultiPolicyMatchedBytes = _HwCBQoSMultiPolicyMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 13),
    _HwCBQoSMultiPolicyMatchedBytes_Type()
)
hwCBQoSMultiPolicyMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyMatchedBytes.setStatus("current")
_HwCBQoSMultiPolicyUnmatchedPackets_Type = Counter64
_HwCBQoSMultiPolicyUnmatchedPackets_Object = MibTableColumn
hwCBQoSMultiPolicyUnmatchedPackets = _HwCBQoSMultiPolicyUnmatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 14),
    _HwCBQoSMultiPolicyUnmatchedPackets_Type()
)
hwCBQoSMultiPolicyUnmatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyUnmatchedPackets.setStatus("current")
_HwCBQoSMultiPolicyUnmatchedBytes_Type = Counter64
_HwCBQoSMultiPolicyUnmatchedBytes_Object = MibTableColumn
hwCBQoSMultiPolicyUnmatchedBytes = _HwCBQoSMultiPolicyUnmatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 15),
    _HwCBQoSMultiPolicyUnmatchedBytes_Type()
)
hwCBQoSMultiPolicyUnmatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyUnmatchedBytes.setStatus("current")
_HwCBQoSMultiPolicyMatchedPassPackets_Type = Counter64
_HwCBQoSMultiPolicyMatchedPassPackets_Object = MibTableColumn
hwCBQoSMultiPolicyMatchedPassPackets = _HwCBQoSMultiPolicyMatchedPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 16),
    _HwCBQoSMultiPolicyMatchedPassPackets_Type()
)
hwCBQoSMultiPolicyMatchedPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyMatchedPassPackets.setStatus("current")
_HwCBQoSMultiPolicyMatchedPassBytes_Type = Counter64
_HwCBQoSMultiPolicyMatchedPassBytes_Object = MibTableColumn
hwCBQoSMultiPolicyMatchedPassBytes = _HwCBQoSMultiPolicyMatchedPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 17),
    _HwCBQoSMultiPolicyMatchedPassBytes_Type()
)
hwCBQoSMultiPolicyMatchedPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyMatchedPassBytes.setStatus("current")
_HwCBQoSMultiPolicyMatchedDropPackets_Type = Counter64
_HwCBQoSMultiPolicyMatchedDropPackets_Object = MibTableColumn
hwCBQoSMultiPolicyMatchedDropPackets = _HwCBQoSMultiPolicyMatchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 18),
    _HwCBQoSMultiPolicyMatchedDropPackets_Type()
)
hwCBQoSMultiPolicyMatchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyMatchedDropPackets.setStatus("current")
_HwCBQoSMultiPolicyMatchedDropBytes_Type = Counter64
_HwCBQoSMultiPolicyMatchedDropBytes_Object = MibTableColumn
hwCBQoSMultiPolicyMatchedDropBytes = _HwCBQoSMultiPolicyMatchedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 19),
    _HwCBQoSMultiPolicyMatchedDropBytes_Type()
)
hwCBQoSMultiPolicyMatchedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyMatchedDropBytes.setStatus("current")
_HwCBQoSMultiPolicyResetFlag_Type = EnabledStatus
_HwCBQoSMultiPolicyResetFlag_Object = MibTableColumn
hwCBQoSMultiPolicyResetFlag = _HwCBQoSMultiPolicyResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 7, 1, 20),
    _HwCBQoSMultiPolicyResetFlag_Type()
)
hwCBQoSMultiPolicyResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyResetFlag.setStatus("current")
_HwCBQoSMultiPolicyStatisticsClassifierTable_Object = MibTable
hwCBQoSMultiPolicyStatisticsClassifierTable = _HwCBQoSMultiPolicyStatisticsClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatisticsClassifierTable.setStatus("current")
_HwCBQoSMultiPolicyStatisticsClassifierEntry_Object = MibTableRow
hwCBQoSMultiPolicyStatisticsClassifierEntry = _HwCBQoSMultiPolicyStatisticsClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1)
)
hwCBQoSMultiPolicyStatisticsClassifierEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyMultiPolicyVlanId"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyMultiPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSMultiPolicyStaPolicyIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSMultiPolicyStatClassifierIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatisticsClassifierEntry.setStatus("current")
_HwCBQoSMultiPolicyStaPolicyIndex_Type = Integer32
_HwCBQoSMultiPolicyStaPolicyIndex_Object = MibTableColumn
hwCBQoSMultiPolicyStaPolicyIndex = _HwCBQoSMultiPolicyStaPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 1),
    _HwCBQoSMultiPolicyStaPolicyIndex_Type()
)
hwCBQoSMultiPolicyStaPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStaPolicyIndex.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierIndex_Type = Integer32
_HwCBQoSMultiPolicyStatClassifierIndex_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierIndex = _HwCBQoSMultiPolicyStatClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 2),
    _HwCBQoSMultiPolicyStatClassifierIndex_Type()
)
hwCBQoSMultiPolicyStatClassifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierIndex.setStatus("current")


class _HwCBQoSMultiPolicyStatClassifierName_Type(OctetString):
    """Custom type hwCBQoSMultiPolicyStatClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSMultiPolicyStatClassifierName_Type.__name__ = "OctetString"
_HwCBQoSMultiPolicyStatClassifierName_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierName = _HwCBQoSMultiPolicyStatClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 3),
    _HwCBQoSMultiPolicyStatClassifierName_Type()
)
hwCBQoSMultiPolicyStatClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierName.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierMatchedPackets_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierMatchedPackets_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierMatchedPackets = _HwCBQoSMultiPolicyStatClassifierMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 4),
    _HwCBQoSMultiPolicyStatClassifierMatchedPackets_Type()
)
hwCBQoSMultiPolicyStatClassifierMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierMatchedPackets.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierMatchedBytes_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierMatchedBytes_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierMatchedBytes = _HwCBQoSMultiPolicyStatClassifierMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 5),
    _HwCBQoSMultiPolicyStatClassifierMatchedBytes_Type()
)
hwCBQoSMultiPolicyStatClassifierMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierMatchedBytes.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierUnmatchedPackets_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierUnmatchedPackets_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierUnmatchedPackets = _HwCBQoSMultiPolicyStatClassifierUnmatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 6),
    _HwCBQoSMultiPolicyStatClassifierUnmatchedPackets_Type()
)
hwCBQoSMultiPolicyStatClassifierUnmatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierUnmatchedPackets.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierUnmatchedBytes_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierUnmatchedBytes_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierUnmatchedBytes = _HwCBQoSMultiPolicyStatClassifierUnmatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 7),
    _HwCBQoSMultiPolicyStatClassifierUnmatchedBytes_Type()
)
hwCBQoSMultiPolicyStatClassifierUnmatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierUnmatchedBytes.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierMatchedPassPackets_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierMatchedPassPackets_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierMatchedPassPackets = _HwCBQoSMultiPolicyStatClassifierMatchedPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 8),
    _HwCBQoSMultiPolicyStatClassifierMatchedPassPackets_Type()
)
hwCBQoSMultiPolicyStatClassifierMatchedPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierMatchedPassPackets.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierMatchedPassBytes_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierMatchedPassBytes_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierMatchedPassBytes = _HwCBQoSMultiPolicyStatClassifierMatchedPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 9),
    _HwCBQoSMultiPolicyStatClassifierMatchedPassBytes_Type()
)
hwCBQoSMultiPolicyStatClassifierMatchedPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierMatchedPassBytes.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierMatchedDropPackets_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierMatchedDropPackets_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierMatchedDropPackets = _HwCBQoSMultiPolicyStatClassifierMatchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 10),
    _HwCBQoSMultiPolicyStatClassifierMatchedDropPackets_Type()
)
hwCBQoSMultiPolicyStatClassifierMatchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierMatchedDropPackets.setStatus("current")
_HwCBQoSMultiPolicyStatClassifierMatchedDropBytes_Type = Counter64
_HwCBQoSMultiPolicyStatClassifierMatchedDropBytes_Object = MibTableColumn
hwCBQoSMultiPolicyStatClassifierMatchedDropBytes = _HwCBQoSMultiPolicyStatClassifierMatchedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 8, 1, 11),
    _HwCBQoSMultiPolicyStatClassifierMatchedDropBytes_Type()
)
hwCBQoSMultiPolicyStatClassifierMatchedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSMultiPolicyStatClassifierMatchedDropBytes.setStatus("current")
_HwCBQoSPolicyStatSubPolicyClassifierRunInfoTable_Object = MibTable
hwCBQoSPolicyStatSubPolicyClassifierRunInfoTable = _HwCBQoSPolicyStatSubPolicyClassifierRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatSubPolicyClassifierRunInfoTable.setStatus("current")
_HwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry_Object = MibTableRow
hwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry = _HwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1)
)
hwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry.setStatus("current")
_HwCBQoSSubPolicyClassIndex_Type = Integer32
_HwCBQoSSubPolicyClassIndex_Object = MibTableColumn
hwCBQoSSubPolicyClassIndex = _HwCBQoSSubPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 1),
    _HwCBQoSSubPolicyClassIndex_Type()
)
hwCBQoSSubPolicyClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyClassIndex.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedPackets = _HwCBQoSSubPolicyStatClassifierMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 2),
    _HwCBQoSSubPolicyStatClassifierMatchedPackets_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedBytes = _HwCBQoSSubPolicyStatClassifierMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 3),
    _HwCBQoSSubPolicyStatClassifierMatchedBytes_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierPassPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierPassPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierPassPackets = _HwCBQoSSubPolicyStatClassifierPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 4),
    _HwCBQoSSubPolicyStatClassifierPassPackets_Type()
)
hwCBQoSSubPolicyStatClassifierPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierPassPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierPassBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierPassBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierPassBytes = _HwCBQoSSubPolicyStatClassifierPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 5),
    _HwCBQoSSubPolicyStatClassifierPassBytes_Type()
)
hwCBQoSSubPolicyStatClassifierPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierPassBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierDropPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierDropPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierDropPackets = _HwCBQoSSubPolicyStatClassifierDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 6),
    _HwCBQoSSubPolicyStatClassifierDropPackets_Type()
)
hwCBQoSSubPolicyStatClassifierDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierDropPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierDropBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierDropBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierDropBytes = _HwCBQoSSubPolicyStatClassifierDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 7),
    _HwCBQoSSubPolicyStatClassifierDropBytes_Type()
)
hwCBQoSSubPolicyStatClassifierDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierDropBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueMatchedPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueMatchedPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueMatchedPackets = _HwCBQoSSubPolicyStatClassifierQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 8),
    _HwCBQoSSubPolicyStatClassifierQueueMatchedPackets_Type()
)
hwCBQoSSubPolicyStatClassifierQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueMatchedPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueMatchedBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueMatchedBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueMatchedBytes = _HwCBQoSSubPolicyStatClassifierQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 9),
    _HwCBQoSSubPolicyStatClassifierQueueMatchedBytes_Type()
)
hwCBQoSSubPolicyStatClassifierQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueMatchedBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets = _HwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 10),
    _HwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets_Type()
)
hwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes = _HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 11),
    _HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes_Type()
)
hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueDiscardedPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueDiscardedPackets = _HwCBQoSSubPolicyStatClassifierQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 12),
    _HwCBQoSSubPolicyStatClassifierQueueDiscardedPackets_Type()
)
hwCBQoSSubPolicyStatClassifierQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueDiscardedPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueDiscardedBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueDiscardedBytes = _HwCBQoSSubPolicyStatClassifierQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 13),
    _HwCBQoSSubPolicyStatClassifierQueueDiscardedBytes_Type()
)
hwCBQoSSubPolicyStatClassifierQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueDiscardedBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarGreenPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarGreenPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarGreenPackets = _HwCBQoSSubPolicyStatClassifierCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 14),
    _HwCBQoSSubPolicyStatClassifierCarGreenPackets_Type()
)
hwCBQoSSubPolicyStatClassifierCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarGreenPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarGreenBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarGreenBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarGreenBytes = _HwCBQoSSubPolicyStatClassifierCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 15),
    _HwCBQoSSubPolicyStatClassifierCarGreenBytes_Type()
)
hwCBQoSSubPolicyStatClassifierCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarGreenBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarYellowPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarYellowPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarYellowPackets = _HwCBQoSSubPolicyStatClassifierCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 16),
    _HwCBQoSSubPolicyStatClassifierCarYellowPackets_Type()
)
hwCBQoSSubPolicyStatClassifierCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarYellowPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarYellowBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarYellowBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarYellowBytes = _HwCBQoSSubPolicyStatClassifierCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 17),
    _HwCBQoSSubPolicyStatClassifierCarYellowBytes_Type()
)
hwCBQoSSubPolicyStatClassifierCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarYellowBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarRedPackets_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarRedPackets_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarRedPackets = _HwCBQoSSubPolicyStatClassifierCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 18),
    _HwCBQoSSubPolicyStatClassifierCarRedPackets_Type()
)
hwCBQoSSubPolicyStatClassifierCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarRedPackets.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarRedBytes_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarRedBytes_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarRedBytes = _HwCBQoSSubPolicyStatClassifierCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 19),
    _HwCBQoSSubPolicyStatClassifierCarRedBytes_Type()
)
hwCBQoSSubPolicyStatClassifierCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarRedBytes.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedPacketsRate = _HwCBQoSSubPolicyStatClassifierMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 20),
    _HwCBQoSSubPolicyStatClassifierMatchedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedBytesRate = _HwCBQoSSubPolicyStatClassifierMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 21),
    _HwCBQoSSubPolicyStatClassifierMatchedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate = _HwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 22),
    _HwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedPassBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedPassBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedPassBytesRate = _HwCBQoSSubPolicyStatClassifierMatchedPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 23),
    _HwCBQoSSubPolicyStatClassifierMatchedPassBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedPassBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate = _HwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 24),
    _HwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierMatchedDropBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierMatchedDropBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierMatchedDropBytesRate = _HwCBQoSSubPolicyStatClassifierMatchedDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 25),
    _HwCBQoSSubPolicyStatClassifierMatchedDropBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierMatchedDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierMatchedDropBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate = _HwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 26),
    _HwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate = _HwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 27),
    _HwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate = _HwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 28),
    _HwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate = _HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 29),
    _HwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate = _HwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 30),
    _HwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate = _HwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 31),
    _HwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate = _HwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 32),
    _HwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate = _HwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 33),
    _HwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate = _HwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 34),
    _HwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate = _HwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 35),
    _HwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate = _HwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 36),
    _HwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate_Type()
)
hwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate.setStatus("current")
_HwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate_Type = Counter64
_HwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate_Object = MibTableColumn
hwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate = _HwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 5, 6, 9, 1, 37),
    _HwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate_Type()
)
hwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate.setStatus("current")
_HwCBQoSGeneral_ObjectIdentity = ObjectIdentity
hwCBQoSGeneral = _HwCBQoSGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6)
)
_HwCBQoSFrameId_Type = Integer32
_HwCBQoSFrameId_Object = MibScalar
hwCBQoSFrameId = _HwCBQoSFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 1),
    _HwCBQoSFrameId_Type()
)
hwCBQoSFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrameId.setStatus("current")
_HwCBQoSSlotId_Type = Integer32
_HwCBQoSSlotId_Object = MibScalar
hwCBQoSSlotId = _HwCBQoSSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 2),
    _HwCBQoSSlotId_Type()
)
hwCBQoSSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSSlotId.setStatus("current")
_HwCBQoSPortId_Type = Integer32
_HwCBQoSPortId_Object = MibScalar
hwCBQoSPortId = _HwCBQoSPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 3),
    _HwCBQoSPortId_Type()
)
hwCBQoSPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPortId.setStatus("current")


class _HwCBQoSTrapIfName_Type(OctetString):
    """Custom type hwCBQoSTrapIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSTrapIfName_Type.__name__ = "OctetString"
_HwCBQoSTrapIfName_Object = MibScalar
hwCBQoSTrapIfName = _HwCBQoSTrapIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 4),
    _HwCBQoSTrapIfName_Type()
)
hwCBQoSTrapIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapIfName.setStatus("current")


class _HwCBQoSTrapType_Type(Integer32):
    """Custom type hwCBQoSTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cir", 1),
          ("pir", 2))
    )


_HwCBQoSTrapType_Type.__name__ = "Integer32"
_HwCBQoSTrapType_Object = MibScalar
hwCBQoSTrapType = _HwCBQoSTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 5),
    _HwCBQoSTrapType_Type()
)
hwCBQoSTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapType.setStatus("current")


class _HwCBQoSTrapAction_Type(Integer32):
    """Custom type hwCBQoSTrapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("remark", 1))
    )


_HwCBQoSTrapAction_Type.__name__ = "Integer32"
_HwCBQoSTrapAction_Object = MibScalar
hwCBQoSTrapAction = _HwCBQoSTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 6),
    _HwCBQoSTrapAction_Type()
)
hwCBQoSTrapAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapAction.setStatus("current")


class _HwCBQoSTrapPolicyName_Type(OctetString):
    """Custom type hwCBQoSTrapPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSTrapPolicyName_Type.__name__ = "OctetString"
_HwCBQoSTrapPolicyName_Object = MibScalar
hwCBQoSTrapPolicyName = _HwCBQoSTrapPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 7),
    _HwCBQoSTrapPolicyName_Type()
)
hwCBQoSTrapPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapPolicyName.setStatus("current")
_HwCBQoSTrapVlanId_Type = Integer32
_HwCBQoSTrapVlanId_Object = MibScalar
hwCBQoSTrapVlanId = _HwCBQoSTrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 8),
    _HwCBQoSTrapVlanId_Type()
)
hwCBQoSTrapVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapVlanId.setStatus("current")


class _HwCBQoSTrapEgressIfName_Type(OctetString):
    """Custom type hwCBQoSTrapEgressIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSTrapEgressIfName_Type.__name__ = "OctetString"
_HwCBQoSTrapEgressIfName_Object = MibScalar
hwCBQoSTrapEgressIfName = _HwCBQoSTrapEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 9),
    _HwCBQoSTrapEgressIfName_Type()
)
hwCBQoSTrapEgressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapEgressIfName.setStatus("current")
_HwCBQoSTrapDiscardPackets_Type = Counter64
_HwCBQoSTrapDiscardPackets_Object = MibScalar
hwCBQoSTrapDiscardPackets = _HwCBQoSTrapDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 6, 10),
    _HwCBQoSTrapDiscardPackets_Type()
)
hwCBQoSTrapDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSTrapDiscardPackets.setStatus("current")
_HwCBQoSQueryObjects_ObjectIdentity = ObjectIdentity
hwCBQoSQueryObjects = _HwCBQoSQueryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 7)
)
_HwCBQoSClassifierIndexQueryTable_Object = MibTable
hwCBQoSClassifierIndexQueryTable = _HwCBQoSClassifierIndexQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierIndexQueryTable.setStatus("current")
_HwCBQoSClassifierIndexQueryEntry_Object = MibTableRow
hwCBQoSClassifierIndexQueryEntry = _HwCBQoSClassifierIndexQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 7, 1, 1)
)
hwCBQoSClassifierIndexQueryEntry.setIndexNames(
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSQueryPolicyName"),
    (0, "HUAWEI-CBQOS-MIB", "hwCBQoSQueryClassifierName"),
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierIndexQueryEntry.setStatus("current")


class _HwCBQoSQueryPolicyName_Type(OctetString):
    """Custom type hwCBQoSQueryPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSQueryPolicyName_Type.__name__ = "OctetString"
_HwCBQoSQueryPolicyName_Object = MibTableColumn
hwCBQoSQueryPolicyName = _HwCBQoSQueryPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 7, 1, 1, 1),
    _HwCBQoSQueryPolicyName_Type()
)
hwCBQoSQueryPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSQueryPolicyName.setStatus("current")


class _HwCBQoSQueryClassifierName_Type(OctetString):
    """Custom type hwCBQoSQueryClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCBQoSQueryClassifierName_Type.__name__ = "OctetString"
_HwCBQoSQueryClassifierName_Object = MibTableColumn
hwCBQoSQueryClassifierName = _HwCBQoSQueryClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 7, 1, 1, 2),
    _HwCBQoSQueryClassifierName_Type()
)
hwCBQoSQueryClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSQueryClassifierName.setStatus("current")
_HwCBQoSQueryClassifierIndex_Type = Integer32
_HwCBQoSQueryClassifierIndex_Object = MibTableColumn
hwCBQoSQueryClassifierIndex = _HwCBQoSQueryClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 1, 7, 1, 1, 3),
    _HwCBQoSQueryClassifierIndex_Type()
)
hwCBQoSQueryClassifierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueryClassifierIndex.setStatus("current")
_HwCBQoSNotifications_ObjectIdentity = ObjectIdentity
hwCBQoSNotifications = _HwCBQoSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 2)
)
_HwCBQoSConformance_ObjectIdentity = ObjectIdentity
hwCBQoSConformance = _HwCBQoSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3)
)
_HwCBQoSCompliances_ObjectIdentity = ObjectIdentity
hwCBQoSCompliances = _HwCBQoSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 1)
)
_HwCBQoSGroups_ObjectIdentity = ObjectIdentity
hwCBQoSGroups = _HwCBQoSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2)
)

# Managed Objects groups

hwCBQoSClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 1)
)
hwCBQoSClassifierGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierIndexNext"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierRuleCount"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierOperator"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierLayer"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleIfNot"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleStringValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchMacMask"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleIntValue1"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleIntValue2"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchVlanEndId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerSrcIp"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerSrcIpMask"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerDstIp"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerDstIpMask"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerSrcPort"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerDstPort"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSMatchInnerProtocol"))
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierGroup.setStatus("current")

hwCBQoSBehaviorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 2)
)
hwCBQoSBehaviorGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndexNext"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSBehaviorGroup.setStatus("current")

hwCBQoSCarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 3)
)
hwCBQoSCarGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSCarCir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarCbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarEbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarGreenAction"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarGreenRemarkValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarRedAction"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarRedRemarkValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarPir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarPbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarYellowAction"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarYellowRemarkValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQosCarAggregation"))
)
if mibBuilder.loadTexts:
    hwCBQoSCarGroup.setStatus("current")

hwCBQoSGtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 4)
)
hwCBQoSGtsGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSGtsCir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSGtsCbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSGtsPir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSGtsEbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSGtsQueueLength"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSGtsRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSGtsGroup.setStatus("current")

hwCBQoSRemarkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 5)
)
hwCBQoSRemarkGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSRemarkType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRemarkValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRemarkRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRemarkStringValue"))
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkGroup.setStatus("current")

hwCBQoSQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 6)
)
hwCBQoSQueueGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSQueueType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueDropType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueLength"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueBandwidthUnit"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueBandwidthValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueCbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueQueueNumber"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSQueueCbsRatio"))
)
if mibBuilder.loadTexts:
    hwCBQoSQueueGroup.setStatus("current")

hwCBQoSWredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 7)
)
hwCBQoSWredGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSWredType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSWredWeightConst"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSWredClassLowLimit"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSWredClassHighLimit"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSWredClassDiscardProb"))
)
if mibBuilder.loadTexts:
    hwCBQoSWredGroup.setStatus("current")

hwCBQoSNatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 9)
)
hwCBQoSNatGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSNatServiceClass"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSNatRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSNatNoPat"))
)
if mibBuilder.loadTexts:
    hwCBQoSNatGroup.setStatus("current")

hwCBQoSFirewallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 10)
)
hwCBQoSFirewallGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFirewallAction"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFirewallRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSFirewallGroup.setStatus("current")

hwCBQoSSamplingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 11)
)
hwCBQoSSamplingGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSSamplingNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSamplingRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfSamplingType"))
)
if mibBuilder.loadTexts:
    hwCBQoSSamplingGroup.setStatus("current")

hwCBQoSEgressGtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 12)
)
hwCBQoSEgressGtsGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSEgressGtsCir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSEgressGtsPir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSEgressGtsRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSEgressGtsGroup.setStatus("current")

hwCBQoSServiceClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 13)
)
hwCBQoSServiceClassGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSServiceClassQueueId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSServiceClassColor"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSServiceClassRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSServiceClassNoremarkflag"))
)
if mibBuilder.loadTexts:
    hwCBQoSServiceClassGroup.setStatus("current")

hwCBQoSPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 14)
)
hwCBQoSPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndexNext"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassCount"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassClassifierIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassClassifierName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassBehaviorIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassBehaviorName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyConfigMode"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassPrecedence"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyShareFlag"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatisticsFlag"))
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyGroup.setStatus("current")

hwCBQoSIfApplyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 15)
)
hwCBQoSIfApplyPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyLinkLayer"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyGroup.setStatus("current")

hwCBQoSAtmPvcApplyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 16)
)
hwCBQoSAtmPvcApplyPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyGroup.setStatus("current")

hwCBQoSIfVlanApplyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 17)
)
hwCBQoSIfVlanApplyPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyIfIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid1"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid2"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyLinkLayer"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyGroup.setStatus("current")

hwCBQoSFrClassApplyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 18)
)
hwCBQoSFrClassApplyPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyFrClassName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyGroup.setStatus("current")

hwCBQoSFrPvcApplyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 19)
)
hwCBQoSFrPvcApplyPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyName"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyGroup.setStatus("current")

hwCBQoSIfCbqRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 20)
)
hwCBQoSIfCbqRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqDiscard"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqEfQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqAfQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqBeQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqBeActiveQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqBeMaxActiveQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqBeTotalQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCbqAfAllocatedQueueNum"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfCbqRunInfoGroup.setStatus("current")

hwCBQoSIfClassMatchRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 21)
)
hwCBQoSIfClassMatchRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfClassMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfClassMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfClassAverageRate"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchRunInfoGroup.setStatus("current")

hwCBQoSIfCarRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 22)
)
hwCBQoSIfCarRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarGreenPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarGreenPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarGreenRemarkedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarGreenRemarkedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarGreenDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarGreenDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarYellowPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarYellowPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarYellowRemarkedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarYellowRemarkedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarYellowDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarYellowDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarRedPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarRedPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarRedRemarkedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarRedRemarkedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarRedDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfCarRedDiscardedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfCarRunInfoGroup.setStatus("current")

hwCBQoSIfGtsRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 23)
)
hwCBQoSIfGtsRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsDelayedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsDelayedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfGtsQueueSize"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfGtsRunInfoGroup.setStatus("current")

hwCBQoSIfRemarkRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 24)
)
hwCBQoSIfRemarkRunInfoGroup.setObjects(
    ("HUAWEI-CBQOS-MIB", "hwCBQoSIfRemarkedPackets")
)
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkRunInfoGroup.setStatus("current")

hwCBQoSIfQueueRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 25)
)
hwCBQoSIfQueueRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfQueueMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfQueueMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfQueueEnqueuedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfQueueEnqueuedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfQueueDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfQueueDiscardedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfQueueRunInfoGroup.setStatus("current")

hwCBQoSIfWredRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 26)
)
hwCBQoSIfWredRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfWredRandomDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfWredTailDiscardedPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfWredRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcCbqRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 27)
)
hwCBQoSAtmPvcCbqRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqDiscard"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqEfQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqAfQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqBeQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqBeActiveQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqBeMaxActiveQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqBeTotalQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCbqAfAllocatedQueueNum"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcClassMatchRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 28)
)
hwCBQoSAtmPvcClassMatchRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcClassMatchPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcClassMatchBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcClassAverageRate"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcCarRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 29)
)
hwCBQoSAtmPvcCarRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCarConformPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCarConformBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCarExceedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcCarExceedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcGtsRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 30)
)
hwCBQoSAtmPvcGtsRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsDelayedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsDelayedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcGtsQueueSize"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcRemarkRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 31)
)
hwCBQoSAtmPvcRemarkRunInfoGroup.setObjects(
    ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcRemarkedPackets")
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcQueueRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 32)
)
hwCBQoSAtmPvcQueueRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcQueueMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcQueueMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcQueueEnqueuedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcQueueEnqueuedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcQueueDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcQueueDiscardedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcWredRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 33)
)
hwCBQoSAtmPvcWredRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcWredRandomDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcWredTailDiscardedPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRunInfoGroup.setStatus("current")

hwCBQoSFrPvcCbqRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 34)
)
hwCBQoSFrPvcCbqRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqDiscard"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqEfQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqAfQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqBeQueueSize"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqBeActiveQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqBeMaxActiveQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqBeTotalQueueNum"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCbqAfAllocatedQueueNum"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqRunInfoGroup.setStatus("current")

hwCBQoSFrPvcClassMatchRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 35)
)
hwCBQoSFrPvcClassMatchRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcClassMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcClassMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcClassAverageRate"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchRunInfoGroup.setStatus("current")

hwCBQoSFrPvcCarRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 36)
)
hwCBQoSFrPvcCarRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCarConformPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCarConformBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCarExceedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcCarExceedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarRunInfoGroup.setStatus("current")

hwCBQoSFrPvcGtsRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 37)
)
hwCBQoSFrPvcGtsRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsDelayedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsDelayedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcGtsQueueSize"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsRunInfoGroup.setStatus("current")

hwCBQoSFrPvcRemarkRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 38)
)
hwCBQoSFrPvcRemarkRunInfoGroup.setObjects(
    ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcRemarkedPackets")
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkRunInfoGroup.setStatus("current")

hwCBQoSFrPvcQueueRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 39)
)
hwCBQoSFrPvcQueueRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcQueueMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcQueueMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcQueueEnqueuedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcQueueEnqueuedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcQueueDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcQueueDiscardedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueRunInfoGroup.setStatus("current")

hwCBQoSFrPvcWredRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 40)
)
hwCBQoSFrPvcWredRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcWredRandomDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcWredTailDiscardedPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRunInfoGroup.setStatus("current")

hwCBQoSIfVlanClassMatchRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 41)
)
hwCBQoSIfVlanClassMatchRunInfoGroup.setObjects(
    ("HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanClassMatchedPackets")
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchRunInfoGroup.setStatus("current")

hwCBQoSLrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 42)
)
hwCBQoSLrGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSLrUnit"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSLrCir"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSLrCbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSLrEbs"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSLrRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSLrGroup.setStatus("current")

hwCBQoSNestPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 43)
)
hwCBQoSNestPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSNestPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSNestPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyGroup.setStatus("current")

hwCBQoSIfLrRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 44)
)
hwCBQoSIfLrRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSIfLrPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfLrPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfLrDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfLrDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfLrDelayedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSIfLrDelayedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSIfLrRunInfoGroup.setStatus("current")

hwCBQoSAtmPvcLrRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 45)
)
hwCBQoSAtmPvcLrRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcLrPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcLrPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcLrDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcLrDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcLrDelayedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcLrDelayedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrRunInfoGroup.setStatus("current")

hwCBQoSFrPvcLrRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 46)
)
hwCBQoSFrPvcLrRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcLrPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcLrPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcLrDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcLrDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcLrDelayedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcLrDelayedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrRunInfoGroup.setStatus("current")

hwCBQoSCarStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 47)
)
hwCBQoSCarStatisticsGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSCarConformedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarConformedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarConformedPacketRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarConformedByteRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarExceededPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarExceededBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarExceededPacketRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarExceededByteRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarOverflowPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarOverflowBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarOverflowPacketRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarOverflowByteRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarPassedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarDroppedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarDroppedBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSCarStatisticsGroup.setStatus("current")

hwCBQoSPolicyStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 48)
)
hwCBQoSPolicyStatisticsGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyUnmatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyUnmatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyMatchedPassPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyMatchedPassBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyMatchedDropPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyMatchedDropBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyResetFlag"))
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsGroup.setStatus("current")

hwCBQoSRedirectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 49)
)
hwCBQoSRedirectGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectIpAddress"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectIfIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectVlanId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectCtrlType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectLSPDstIpAddress"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRedirectLSPSecondary"))
)
if mibBuilder.loadTexts:
    hwCBQoSRedirectGroup.setStatus("current")

hwCBQoSGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 50)
)
hwCBQoSGeneralGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrameId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSlotId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPortId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapIfName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapAction"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapVlanId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapEgressIfName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapDiscardPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSGeneralGroup.setStatus("current")

hwCBQoSPolicyShareModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 52)
)
hwCBQoSPolicyShareModeGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyShareModeFlag"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyShareModeRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyShareModeGroup.setStatus("current")

hwCBQoSClassifierStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 53)
)
hwCBQoSClassifierStatisticsGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassifierIndex"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierMatchedPassPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierMatchedPassBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierMatchedDropPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierMatchedDropBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierStatisticsGroup.setStatus("current")

hwCBQoSPolicyStatisticsClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 54)
)
hwCBQoSPolicyStatisticsClassifierGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierUnmatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierUnmatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierMatchedPassPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierMatchedPassBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierMatchedDropPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPolicyStatClassifierMatchedDropBytes"))
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatisticsClassifierGroup.setStatus("current")

hwCBQoSVlanApplyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 55)
)
hwCBQoSVlanApplyPolicyGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyRowStatus"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSVlanApplyPolicyVlanId"))
)
if mibBuilder.loadTexts:
    hwCBQoSVlanApplyPolicyGroup.setStatus("current")

hwCBQoSSVlanClassMatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 56)
)
hwCBQoSSVlanClassMatchGroup.setObjects(
    ("HUAWEI-CBQOS-MIB", "hwCBQoSVlanClassMatchedPackets")
)
if mibBuilder.loadTexts:
    hwCBQoSSVlanClassMatchGroup.setStatus("current")

hwCBQoSSVlanCarMatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 57)
)
hwCBQoSSVlanCarMatchGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSVlanCarPassedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSVlanCarDiscardedPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSSVlanCarMatchGroup.setStatus("current")

hwCBQoSRandomDiscardCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 58)
)
hwCBQoSRandomDiscardCfgInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSRandomPercent"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRandomDiscardRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSRandomDiscardCfgInfoGroup.setStatus("current")

hwCBQoSDenyPacketLengthCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 59)
)
hwCBQoSDenyPacketLengthCfgInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSDenyPacketLengthOptype"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSDenyPacketLengthMax"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSDenyPacketLengthMin"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSDenyPacketLength"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSDenyPacketLengthRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSDenyPacketLengthCfgInfoGroup.setStatus("current")

hwCBQoSDAAStatisticsCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 60)
)
hwCBQoSDAAStatisticsCfgInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSDAAStatisticsSummary"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSDAAStatisticsRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSDAAStatisticsCfgInfoGroup.setStatus("current")

hwCBQoSDAATariffLevelCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 61)
)
hwCBQoSDAATariffLevelCfgInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSDAATariffLevelValue"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSDAATariffLevelRowStatus"))
)
if mibBuilder.loadTexts:
    hwCBQoSDAATariffLevelCfgInfoGroup.setStatus("current")

hwCBQoSRuleNotSupportAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 62)
)
hwCBQoSRuleNotSupportAlarmGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSRuleDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRuleSlotID"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRuleInfo"))
)
if mibBuilder.loadTexts:
    hwCBQoSRuleNotSupportAlarmGroup.setStatus("current")

hwCBQoSActionNotSupportAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 63)
)
hwCBQoSActionNotSupportAlarmGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSActionDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSActionSlotID"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSActionInfo"))
)
if mibBuilder.loadTexts:
    hwCBQoSActionNotSupportAlarmGroup.setStatus("current")

hwCBQoSPolicyStatSubPolicyClassifierRunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 64)
)
hwCBQoSPolicyStatSubPolicyClassifierRunInfoGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierPassPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierPassBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierDropPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierDropBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueMatchedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueMatchedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueDiscardedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueDiscardedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarGreenPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarGreenBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarYellowPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarYellowBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarRedPackets"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarRedBytes"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedPassBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierMatchedDropBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate"))
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyStatSubPolicyClassifierRunInfoGroup.setStatus("current")


# Notification objects

hwCBQoSGtsDiscardThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 2, 1)
)
hwCBQoSGtsDiscardThresholdTrap.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrameId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSlotId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPortId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapIfName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapVlanId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapEgressIfName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapDiscardPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSGtsDiscardThresholdTrap.setStatus(
        "current"
    )

hwCBQoSCarOverSpeedThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 2, 2)
)
hwCBQoSCarOverSpeedThresholdTrap.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSFrameId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSSlotId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSPortId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSClassifierName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapIfName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapPolicyName"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapVlanId"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapType"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapAction"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSTrapDiscardPackets"))
)
if mibBuilder.loadTexts:
    hwCBQoSCarOverSpeedThresholdTrap.setStatus(
        "current"
    )

hwCBQoSRuleNotSupportAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 2, 3)
)
hwCBQoSRuleNotSupportAlarm.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSRuleDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRuleSlotID"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRuleInfo"))
)
if mibBuilder.loadTexts:
    hwCBQoSRuleNotSupportAlarm.setStatus(
        "current"
    )

hwCBQoSActionNotSupportAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 2, 4)
)
hwCBQoSActionNotSupportAlarm.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSActionDirection"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSActionSlotID"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSActionInfo"))
)
if mibBuilder.loadTexts:
    hwCBQoSActionNotSupportAlarm.setStatus(
        "current"
    )


# Notifications groups

hwCBQoSNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 2, 51)
)
hwCBQoSNotificationsGroup.setObjects(
      *(("HUAWEI-CBQOS-MIB", "hwCBQoSGtsDiscardThresholdTrap"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSCarOverSpeedThresholdTrap"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSRuleNotSupportAlarm"),
        ("HUAWEI-CBQOS-MIB", "hwCBQoSActionNotSupportAlarm"))
)
if mibBuilder.loadTexts:
    hwCBQoSNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwCBQoSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CBQOS-MIB",
    **{"MatchRuleType": MatchRuleType,
       "CarAction": CarAction,
       "RemarkType": RemarkType,
       "CBQueueType": CBQueueType,
       "QueueBandwidthUnit": QueueBandwidthUnit,
       "WredType": WredType,
       "SamplingType": SamplingType,
       "LrCirUnit": LrCirUnit,
       "RedirectType": RedirectType,
       "RedirectCtrlType": RedirectCtrlType,
       "UrpfCtrlType": UrpfCtrlType,
       "DirectionType": DirectionType,
       "CosType": CosType,
       "hwQoS": hwQoS,
       "hwCBQoSMIB": hwCBQoSMIB,
       "hwCBQoSObjects": hwCBQoSObjects,
       "hwCBQoSClassifierObjects": hwCBQoSClassifierObjects,
       "hwCBQoSClassifierIndexNext": hwCBQoSClassifierIndexNext,
       "hwCBQoSClassifierCfgInfoTable": hwCBQoSClassifierCfgInfoTable,
       "hwCBQoSClassifierCfgInfoEntry": hwCBQoSClassifierCfgInfoEntry,
       "hwCBQoSClassifierIndex": hwCBQoSClassifierIndex,
       "hwCBQoSClassifierName": hwCBQoSClassifierName,
       "hwCBQoSClassifierRuleCount": hwCBQoSClassifierRuleCount,
       "hwCBQoSClassifierOperator": hwCBQoSClassifierOperator,
       "hwCBQoSClassifierLayer": hwCBQoSClassifierLayer,
       "hwCBQoSClassifierRowStatus": hwCBQoSClassifierRowStatus,
       "hwCBQoSMatchRuleCfgInfoTable": hwCBQoSMatchRuleCfgInfoTable,
       "hwCBQoSMatchRuleCfgInfoEntry": hwCBQoSMatchRuleCfgInfoEntry,
       "hwCBQoSMatchRuleIndex": hwCBQoSMatchRuleIndex,
       "hwCBQoSMatchRuleIfNot": hwCBQoSMatchRuleIfNot,
       "hwCBQoSMatchRuleType": hwCBQoSMatchRuleType,
       "hwCBQoSMatchRuleStringValue": hwCBQoSMatchRuleStringValue,
       "hwCBQoSMatchRuleIntValue1": hwCBQoSMatchRuleIntValue1,
       "hwCBQoSMatchRuleIntValue2": hwCBQoSMatchRuleIntValue2,
       "hwCBQoSMatchRuleRowStatus": hwCBQoSMatchRuleRowStatus,
       "hwCBQoSMatchMacMask": hwCBQoSMatchMacMask,
       "hwCBQoSMatchVlanBeginId": hwCBQoSMatchVlanBeginId,
       "hwCBQoSMatchVlanEndId": hwCBQoSMatchVlanEndId,
       "hwCBQoSMatchInnerSrcIp": hwCBQoSMatchInnerSrcIp,
       "hwCBQoSMatchInnerSrcIpMask": hwCBQoSMatchInnerSrcIpMask,
       "hwCBQoSMatchInnerDstIp": hwCBQoSMatchInnerDstIp,
       "hwCBQoSMatchInnerDstIpMask": hwCBQoSMatchInnerDstIpMask,
       "hwCBQoSMatchInnerSrcPort": hwCBQoSMatchInnerSrcPort,
       "hwCBQoSMatchInnerDstPort": hwCBQoSMatchInnerDstPort,
       "hwCBQoSMatchInnerProtocol": hwCBQoSMatchInnerProtocol,
       "hwCBQoSBehaviorObjects": hwCBQoSBehaviorObjects,
       "hwCBQoSBehaviorIndexNext": hwCBQoSBehaviorIndexNext,
       "hwCBQoSBehaviorCfgInfoTable": hwCBQoSBehaviorCfgInfoTable,
       "hwCBQoSBehaviorCfgInfoEntry": hwCBQoSBehaviorCfgInfoEntry,
       "hwCBQoSBehaviorIndex": hwCBQoSBehaviorIndex,
       "hwCBQoSBehaviorName": hwCBQoSBehaviorName,
       "hwCBQoSBehaviorRowStatus": hwCBQoSBehaviorRowStatus,
       "hwCBQoSCarCfgInfoTable": hwCBQoSCarCfgInfoTable,
       "hwCBQoSCarCfgInfoEntry": hwCBQoSCarCfgInfoEntry,
       "hwCBQoSCarCir": hwCBQoSCarCir,
       "hwCBQoSCarCbs": hwCBQoSCarCbs,
       "hwCBQoSCarEbs": hwCBQoSCarEbs,
       "hwCBQoSCarPir": hwCBQoSCarPir,
       "hwCBQoSCarPbs": hwCBQoSCarPbs,
       "hwCBQoSCarGreenAction": hwCBQoSCarGreenAction,
       "hwCBQoSCarGreenRemarkValue": hwCBQoSCarGreenRemarkValue,
       "hwCBQoSCarYellowAction": hwCBQoSCarYellowAction,
       "hwCBQoSCarYellowRemarkValue": hwCBQoSCarYellowRemarkValue,
       "hwCBQoSCarRedAction": hwCBQoSCarRedAction,
       "hwCBQoSCarRedRemarkValue": hwCBQoSCarRedRemarkValue,
       "hwCBQoSCarRowStatus": hwCBQoSCarRowStatus,
       "hwCBQosCarAggregation": hwCBQosCarAggregation,
       "hwCBQoSGtsCfgInfoTable": hwCBQoSGtsCfgInfoTable,
       "hwCBQoSGtsCfgInfoEntry": hwCBQoSGtsCfgInfoEntry,
       "hwCBQoSGtsCir": hwCBQoSGtsCir,
       "hwCBQoSGtsCbs": hwCBQoSGtsCbs,
       "hwCBQoSGtsEbs": hwCBQoSGtsEbs,
       "hwCBQoSGtsQueueLength": hwCBQoSGtsQueueLength,
       "hwCBQoSGtsRowStatus": hwCBQoSGtsRowStatus,
       "hwCBQoSGtsPir": hwCBQoSGtsPir,
       "hwCBQoSRemarkCfgInfoTable": hwCBQoSRemarkCfgInfoTable,
       "hwCBQoSRemarkCfgInfoEntry": hwCBQoSRemarkCfgInfoEntry,
       "hwCBQoSRemarkType": hwCBQoSRemarkType,
       "hwCBQoSRemarkValue": hwCBQoSRemarkValue,
       "hwCBQoSRemarkStringValue": hwCBQoSRemarkStringValue,
       "hwCBQoSRemarkRowStatus": hwCBQoSRemarkRowStatus,
       "hwCBQoSQueueCfgInfoTable": hwCBQoSQueueCfgInfoTable,
       "hwCBQoSQueueCfgInfoEntry": hwCBQoSQueueCfgInfoEntry,
       "hwCBQoSQueueType": hwCBQoSQueueType,
       "hwCBQoSQueueDropType": hwCBQoSQueueDropType,
       "hwCBQoSQueueLength": hwCBQoSQueueLength,
       "hwCBQoSQueueBandwidthUnit": hwCBQoSQueueBandwidthUnit,
       "hwCBQoSQueueBandwidthValue": hwCBQoSQueueBandwidthValue,
       "hwCBQoSQueueCbs": hwCBQoSQueueCbs,
       "hwCBQoSQueueQueueNumber": hwCBQoSQueueQueueNumber,
       "hwCBQoSQueueRowStatus": hwCBQoSQueueRowStatus,
       "hwCBQoSQueueCbsRatio": hwCBQoSQueueCbsRatio,
       "hwCBQoSWredCfgInfoTable": hwCBQoSWredCfgInfoTable,
       "hwCBQoSWredCfgInfoEntry": hwCBQoSWredCfgInfoEntry,
       "hwCBQoSWredType": hwCBQoSWredType,
       "hwCBQoSWredWeightConst": hwCBQoSWredWeightConst,
       "hwCBQoSWredDropProfileIndex": hwCBQoSWredDropProfileIndex,
       "hwCBQoSWredCfgRowStatus": hwCBQoSWredCfgRowStatus,
       "hwCBQoSWredClassCfgInfoTable": hwCBQoSWredClassCfgInfoTable,
       "hwCBQoSWredClassCfgInfoEntry": hwCBQoSWredClassCfgInfoEntry,
       "hwCBQoSWredClassValue": hwCBQoSWredClassValue,
       "hwCBQoSWredClassLowLimit": hwCBQoSWredClassLowLimit,
       "hwCBQoSWredClassHighLimit": hwCBQoSWredClassHighLimit,
       "hwCBQoSWredClassDiscardProb": hwCBQoSWredClassDiscardProb,
       "hwCBQoSNatCfgInfoTable": hwCBQoSNatCfgInfoTable,
       "hwCBQoSNatCfgInfoEntry": hwCBQoSNatCfgInfoEntry,
       "hwCBQoSNatAddressGroup": hwCBQoSNatAddressGroup,
       "hwCBQoSNatNoPat": hwCBQoSNatNoPat,
       "hwCBQoSNatServiceClass": hwCBQoSNatServiceClass,
       "hwCBQoSNatRowStatus": hwCBQoSNatRowStatus,
       "hwCBQoSFirewallCfgInfoTable": hwCBQoSFirewallCfgInfoTable,
       "hwCBQoSFirewallCfgInfoEntry": hwCBQoSFirewallCfgInfoEntry,
       "hwCBQoSFirewallAction": hwCBQoSFirewallAction,
       "hwCBQoSFirewallRowStatus": hwCBQoSFirewallRowStatus,
       "hwCBQoSSamplingCfgInfoTable": hwCBQoSSamplingCfgInfoTable,
       "hwCBQoSSamplingCfgInfoEntry": hwCBQoSSamplingCfgInfoEntry,
       "hwCBQoSIfSamplingType": hwCBQoSIfSamplingType,
       "hwCBQoSSamplingNum": hwCBQoSSamplingNum,
       "hwCBQoSSamplingRowStatus": hwCBQoSSamplingRowStatus,
       "hwCBQoSLrCfgInfoTable": hwCBQoSLrCfgInfoTable,
       "hwCBQoSLrCfgInfoEntry": hwCBQoSLrCfgInfoEntry,
       "hwCBQoSLrUnit": hwCBQoSLrUnit,
       "hwCBQoSLrCir": hwCBQoSLrCir,
       "hwCBQoSLrCbs": hwCBQoSLrCbs,
       "hwCBQoSLrEbs": hwCBQoSLrEbs,
       "hwCBQoSLrRowStatus": hwCBQoSLrRowStatus,
       "hwCBQoSNestPolicyCfgInfoTable": hwCBQoSNestPolicyCfgInfoTable,
       "hwCBQoSNestPolicyCfgInfoEntry": hwCBQoSNestPolicyCfgInfoEntry,
       "hwCBQoSNestPolicyName": hwCBQoSNestPolicyName,
       "hwCBQoSNestPolicyRowStatus": hwCBQoSNestPolicyRowStatus,
       "hwCBQoSRedirectCfgInfoTable": hwCBQoSRedirectCfgInfoTable,
       "hwCBQoSRedirectCfgInfoEntry": hwCBQoSRedirectCfgInfoEntry,
       "hwCBQoSRedirectType": hwCBQoSRedirectType,
       "hwCBQoSRedirectIpAddress": hwCBQoSRedirectIpAddress,
       "hwCBQoSRedirectIfIndex": hwCBQoSRedirectIfIndex,
       "hwCBQoSRedirectVlanId": hwCBQoSRedirectVlanId,
       "hwCBQoSRedirectCtrlType": hwCBQoSRedirectCtrlType,
       "hwCBQoSRedirectRowStatus": hwCBQoSRedirectRowStatus,
       "hwCBQoSRedirectLSPDstIpAddress": hwCBQoSRedirectLSPDstIpAddress,
       "hwCBQoSRedirectLSPSecondary": hwCBQoSRedirectLSPSecondary,
       "hwCBQoSMirrorCfgInfoTable": hwCBQoSMirrorCfgInfoTable,
       "hwCBQoSMirrorCfgInfoEntry": hwCBQoSMirrorCfgInfoEntry,
       "hwCBQoSMirrorObserveIndex": hwCBQoSMirrorObserveIndex,
       "hwCBQoSMirrorRowStatus": hwCBQoSMirrorRowStatus,
       "hwCBQoSUrpfCfgInfoTable": hwCBQoSUrpfCfgInfoTable,
       "hwCBQoSUrpfCfgInfoEntry": hwCBQoSUrpfCfgInfoEntry,
       "hwCBQoSUrpfCtrlType": hwCBQoSUrpfCtrlType,
       "hwCBQoSUrpfAllowDefault": hwCBQoSUrpfAllowDefault,
       "hwCBQoSUrpfRowStatus": hwCBQoSUrpfRowStatus,
       "hwCBQoSCountCfgInfoTable": hwCBQoSCountCfgInfoTable,
       "hwCBQoSCountCfgInfoEntry": hwCBQoSCountCfgInfoEntry,
       "hwCBQoSCountAction": hwCBQoSCountAction,
       "hwCBQoSCountRowStatus": hwCBQoSCountRowStatus,
       "hwCBQoSHighDropCfgInfoTable": hwCBQoSHighDropCfgInfoTable,
       "hwCBQoSHighDropCfgInfoEntry": hwCBQoSHighDropCfgInfoEntry,
       "hwCBQoSHighDropPrecedence": hwCBQoSHighDropPrecedence,
       "hwCBQoSHighDropRowStatus": hwCBQoSHighDropRowStatus,
       "hwCBQoSLoadBalanceCfgInfoTable": hwCBQoSLoadBalanceCfgInfoTable,
       "hwCBQoSLoadBalanceCfgInfoEntry": hwCBQoSLoadBalanceCfgInfoEntry,
       "hwCBQoSLoadBalanceType": hwCBQoSLoadBalanceType,
       "hwCBQoSLoadBalanceRowStatus": hwCBQoSLoadBalanceRowStatus,
       "hwCBQoSEgressGtsCfgInfoTable": hwCBQoSEgressGtsCfgInfoTable,
       "hwCBQoSEgressGtsCfgInfoEntry": hwCBQoSEgressGtsCfgInfoEntry,
       "hwCBQoSEgressGtsIfIndex": hwCBQoSEgressGtsIfIndex,
       "hwCBQoSEgressGtsCir": hwCBQoSEgressGtsCir,
       "hwCBQoSEgressGtsPir": hwCBQoSEgressGtsPir,
       "hwCBQoSEgressGtsRowStatus": hwCBQoSEgressGtsRowStatus,
       "hwCBQoSServiceClassCfgInfoTable": hwCBQoSServiceClassCfgInfoTable,
       "hwCBQoSServiceClassCfgInfoEntry": hwCBQoSServiceClassCfgInfoEntry,
       "hwCBQoSServiceClassQueueId": hwCBQoSServiceClassQueueId,
       "hwCBQoSServiceClassColor": hwCBQoSServiceClassColor,
       "hwCBQoSServiceClassRowStatus": hwCBQoSServiceClassRowStatus,
       "hwCBQoSServiceClassNoremarkflag": hwCBQoSServiceClassNoremarkflag,
       "hwCBQoSRedirectMULCfgInfoTable": hwCBQoSRedirectMULCfgInfoTable,
       "hwCBQoSRedirectMULCfgInfoEntry": hwCBQoSRedirectMULCfgInfoEntry,
       "hwCBQoSRedirectMULIpAddress1": hwCBQoSRedirectMULIpAddress1,
       "hwCBQoSRedirectMULIfIndex1": hwCBQoSRedirectMULIfIndex1,
       "hwCBQoSRedirectMULIpAddress2": hwCBQoSRedirectMULIpAddress2,
       "hwCBQoSRedirectMULIfIndex2": hwCBQoSRedirectMULIfIndex2,
       "hwCBQoSRedirectMULIpAddress3": hwCBQoSRedirectMULIpAddress3,
       "hwCBQoSRedirectMULIfIndex3": hwCBQoSRedirectMULIfIndex3,
       "hwCBQoSRedirectMULIpAddress4": hwCBQoSRedirectMULIpAddress4,
       "hwCBQoSRedirectMULIfIndex4": hwCBQoSRedirectMULIfIndex4,
       "hwCBQoSRedirectMULCtrlType": hwCBQoSRedirectMULCtrlType,
       "hwCBQoSRedirectMULRowStatus": hwCBQoSRedirectMULRowStatus,
       "hwCBQoSRandomDiscardCfgInfoTable": hwCBQoSRandomDiscardCfgInfoTable,
       "hwCBQoSRandomDiscardCfgInfoEntry": hwCBQoSRandomDiscardCfgInfoEntry,
       "hwCBQoSRandomPercent": hwCBQoSRandomPercent,
       "hwCBQoSRandomDiscardRowStatus": hwCBQoSRandomDiscardRowStatus,
       "hwCBQoSDenyPacketLengthCfgInfoTable": hwCBQoSDenyPacketLengthCfgInfoTable,
       "hwCBQoSDenyPacketLengthCfgInfoEntry": hwCBQoSDenyPacketLengthCfgInfoEntry,
       "hwCBQoSDenyPacketLengthOptype": hwCBQoSDenyPacketLengthOptype,
       "hwCBQoSDenyPacketLengthMin": hwCBQoSDenyPacketLengthMin,
       "hwCBQoSDenyPacketLengthMax": hwCBQoSDenyPacketLengthMax,
       "hwCBQoSDenyPacketLength": hwCBQoSDenyPacketLength,
       "hwCBQoSDenyPacketLengthRowStatus": hwCBQoSDenyPacketLengthRowStatus,
       "hwCBQoSDAAStatisticsCfgInfoTable": hwCBQoSDAAStatisticsCfgInfoTable,
       "hwCBQoSDAAStatisticsCfgInfoEntry": hwCBQoSDAAStatisticsCfgInfoEntry,
       "hwCBQoSDAAStatisticsSummary": hwCBQoSDAAStatisticsSummary,
       "hwCBQoSDAAStatisticsRowStatus": hwCBQoSDAAStatisticsRowStatus,
       "hwCBQoSDAATariffLevelCfgInfoTable": hwCBQoSDAATariffLevelCfgInfoTable,
       "hwCBQoSDAATariffLevelCfgInfoEntry": hwCBQoSDAATariffLevelCfgInfoEntry,
       "hwCBQoSDAATariffLevelValue": hwCBQoSDAATariffLevelValue,
       "hwCBQoSDAATariffLevelRowStatus": hwCBQoSDAATariffLevelRowStatus,
       "hwCBQoSRemarkIpDfCfgInfoTable": hwCBQoSRemarkIpDfCfgInfoTable,
       "hwCBQoSRemarkIpDfCfgInfoEntry": hwCBQoSRemarkIpDfCfgInfoEntry,
       "hwCBQoSRemarkIpDf": hwCBQoSRemarkIpDf,
       "hwCBQoSRemarkIpDfRowStatus": hwCBQoSRemarkIpDfRowStatus,
       "hwCBQoSDropProfileCfgInfoTable": hwCBQoSDropProfileCfgInfoTable,
       "hwCBQoSDropProfileCfgInfoEntry": hwCBQoSDropProfileCfgInfoEntry,
       "hwCBQoSDropProfileIndex": hwCBQoSDropProfileIndex,
       "hwCBQoSDropProfileName": hwCBQoSDropProfileName,
       "hwCBQoSDropProfileType": hwCBQoSDropProfileType,
       "hwCBQoSDropProfileRowStatus": hwCBQoSDropProfileRowStatus,
       "hwCBQoSDropProfileClassCfgInfoTable": hwCBQoSDropProfileClassCfgInfoTable,
       "hwCBQoSDropProfileClassCfgInfoEntry": hwCBQoSDropProfileClassCfgInfoEntry,
       "hwCBQoSDropProfileClassValue": hwCBQoSDropProfileClassValue,
       "hwCBQoSDropProfileLowLimit": hwCBQoSDropProfileLowLimit,
       "hwCBQoSDropProfileHighLimit": hwCBQoSDropProfileHighLimit,
       "hwCBQoSDropProfileDiscardProb": hwCBQoSDropProfileDiscardProb,
       "hwCBQoSRedirectVsiTable": hwCBQoSRedirectVsiTable,
       "hwCBQoSRedirectVsiEntry": hwCBQoSRedirectVsiEntry,
       "hwCBQoSRedirectVsiName": hwCBQoSRedirectVsiName,
       "hwCBQoSRedirectVsiRowStatus": hwCBQoSRedirectVsiRowStatus,
       "hwCBQoSSuppressionCfgInfoTable": hwCBQoSSuppressionCfgInfoTable,
       "hwCBQoSSuppressionCfgInfoEntry": hwCBQoSSuppressionCfgInfoEntry,
       "hwCBQoSSuppressionType": hwCBQoSSuppressionType,
       "hwCBQoSSuppressionCir": hwCBQoSSuppressionCir,
       "hwCBQoSSuppressionCbs": hwCBQoSSuppressionCbs,
       "hwCBQoSSuppressionGreenAction": hwCBQoSSuppressionGreenAction,
       "hwCBQoSSuppressionGreenRemarkValue": hwCBQoSSuppressionGreenRemarkValue,
       "hwCBQoSSuppressionRedAction": hwCBQoSSuppressionRedAction,
       "hwCBQoSSuppressionRedRemarkValue": hwCBQoSSuppressionRedRemarkValue,
       "hwCBQoSSuppressionRowStatus": hwCBQoSSuppressionRowStatus,
       "hwCBQoSPolicyObjects": hwCBQoSPolicyObjects,
       "hwCBQoSPolicyIndexNext": hwCBQoSPolicyIndexNext,
       "hwCBQoSPolicyCfgInfoTable": hwCBQoSPolicyCfgInfoTable,
       "hwCBQoSPolicyCfgInfoEntry": hwCBQoSPolicyCfgInfoEntry,
       "hwCBQoSPolicyIndex": hwCBQoSPolicyIndex,
       "hwCBQoSPolicyName": hwCBQoSPolicyName,
       "hwCBQoSPolicyClassCount": hwCBQoSPolicyClassCount,
       "hwCBQoSPolicyConfigMode": hwCBQoSPolicyConfigMode,
       "hwCBQoSPolicyRowStatus": hwCBQoSPolicyRowStatus,
       "hwCBQoSPolicyShareFlag": hwCBQoSPolicyShareFlag,
       "hwCBQoSPolicyStatisticsFlag": hwCBQoSPolicyStatisticsFlag,
       "hwCBQoSPolicyClassCfgInfoTable": hwCBQoSPolicyClassCfgInfoTable,
       "hwCBQoSPolicyClassCfgInfoEntry": hwCBQoSPolicyClassCfgInfoEntry,
       "hwCBQoSPolicyClassIndex": hwCBQoSPolicyClassIndex,
       "hwCBQoSPolicyClassClassifierIndex": hwCBQoSPolicyClassClassifierIndex,
       "hwCBQoSPolicyClassClassifierName": hwCBQoSPolicyClassClassifierName,
       "hwCBQoSPolicyClassBehaviorIndex": hwCBQoSPolicyClassBehaviorIndex,
       "hwCBQoSPolicyClassBehaviorName": hwCBQoSPolicyClassBehaviorName,
       "hwCBQoSPolicyClassPrecedence": hwCBQoSPolicyClassPrecedence,
       "hwCBQoSPolicyClassRowStatus": hwCBQoSPolicyClassRowStatus,
       "hwCBQoSPolicyShareModeCfgInfoTable": hwCBQoSPolicyShareModeCfgInfoTable,
       "hwCBQoSPolicyShareModeCfgInfoEntry": hwCBQoSPolicyShareModeCfgInfoEntry,
       "hwCBQoSPolicyShareModeFlag": hwCBQoSPolicyShareModeFlag,
       "hwCBQoSPolicyShareModeRowStatus": hwCBQoSPolicyShareModeRowStatus,
       "hwCBQoSApplyPolicyObjects": hwCBQoSApplyPolicyObjects,
       "hwCBQoSIfApplyPolicyTable": hwCBQoSIfApplyPolicyTable,
       "hwCBQoSIfApplyPolicyEntry": hwCBQoSIfApplyPolicyEntry,
       "hwCBQoSIfApplyPolicyIfIndex": hwCBQoSIfApplyPolicyIfIndex,
       "hwCBQoSIfApplyPolicyDirection": hwCBQoSIfApplyPolicyDirection,
       "hwCBQoSIfApplyPolicyName": hwCBQoSIfApplyPolicyName,
       "hwCBQoSIfApplyPolicyRowStatus": hwCBQoSIfApplyPolicyRowStatus,
       "hwCBQoSIfApplyPolicyLinkLayer": hwCBQoSIfApplyPolicyLinkLayer,
       "hwCBQoSAtmPvcApplyPolicyTable": hwCBQoSAtmPvcApplyPolicyTable,
       "hwCBQoSAtmPvcApplyPolicyEntry": hwCBQoSAtmPvcApplyPolicyEntry,
       "hwCBQoSAtmPvcApplyPolicyIfIndex": hwCBQoSAtmPvcApplyPolicyIfIndex,
       "hwCBQoSAtmPvcApplyPolicyVPI": hwCBQoSAtmPvcApplyPolicyVPI,
       "hwCBQoSAtmPvcApplyPolicyVCI": hwCBQoSAtmPvcApplyPolicyVCI,
       "hwCBQoSAtmPvcApplyPolicyDirection": hwCBQoSAtmPvcApplyPolicyDirection,
       "hwCBQoSAtmPvcApplyPolicyName": hwCBQoSAtmPvcApplyPolicyName,
       "hwCBQoSAtmPvcApplyPolicyRowStatus": hwCBQoSAtmPvcApplyPolicyRowStatus,
       "hwCBQoSIfVlanApplyPolicyTable": hwCBQoSIfVlanApplyPolicyTable,
       "hwCBQoSIfVlanApplyPolicyEntry": hwCBQoSIfVlanApplyPolicyEntry,
       "hwCBQoSIfVlanApplyPolicyIfIndex": hwCBQoSIfVlanApplyPolicyIfIndex,
       "hwCBQoSIfVlanApplyPolicyDirection": hwCBQoSIfVlanApplyPolicyDirection,
       "hwCBQoSIfVlanApplyPolicyVlanid1": hwCBQoSIfVlanApplyPolicyVlanid1,
       "hwCBQoSIfVlanApplyPolicyVlanid2": hwCBQoSIfVlanApplyPolicyVlanid2,
       "hwCBQoSIfVlanApplyPolicyCeVidEnd": hwCBQoSIfVlanApplyPolicyCeVidEnd,
       "hwCBQoSIfVlanApplyPolicyName": hwCBQoSIfVlanApplyPolicyName,
       "hwCBQoSIfVlanApplyPolicyRowStatus": hwCBQoSIfVlanApplyPolicyRowStatus,
       "hwCBQoSIfVlanApplyPolicyLinkLayer": hwCBQoSIfVlanApplyPolicyLinkLayer,
       "hwCBQoSFrClassApplyPolicyTable": hwCBQoSFrClassApplyPolicyTable,
       "hwCBQoSFrClassApplyPolicyEntry": hwCBQoSFrClassApplyPolicyEntry,
       "hwCBQoSFrClassApplyPolicyFrClassName": hwCBQoSFrClassApplyPolicyFrClassName,
       "hwCBQoSFrClassApplyPolicyDirection": hwCBQoSFrClassApplyPolicyDirection,
       "hwCBQoSFrClassApplyPolicyName": hwCBQoSFrClassApplyPolicyName,
       "hwCBQoSFrClassApplyPolicyRowStatus": hwCBQoSFrClassApplyPolicyRowStatus,
       "hwCBQoSFrPvcApplyPolicyTable": hwCBQoSFrPvcApplyPolicyTable,
       "hwCBQoSFrPvcApplyPolicyEntry": hwCBQoSFrPvcApplyPolicyEntry,
       "hwCBQoSFrPvcApplyPolicyIfIndex": hwCBQoSFrPvcApplyPolicyIfIndex,
       "hwCBQoSFrPvcApplyPolicyDlciNum": hwCBQoSFrPvcApplyPolicyDlciNum,
       "hwCBQoSFrPvcApplyPolicyDirection": hwCBQoSFrPvcApplyPolicyDirection,
       "hwCBQoSFrPvcApplyPolicyName": hwCBQoSFrPvcApplyPolicyName,
       "hwCBQoSVsiApplyPolicyTable": hwCBQoSVsiApplyPolicyTable,
       "hwCBQoSVsiApplyPolicyEntry": hwCBQoSVsiApplyPolicyEntry,
       "hwCBQoSVsiApplyPolicyVsiIndex": hwCBQoSVsiApplyPolicyVsiIndex,
       "hwCBQoSVsiName": hwCBQoSVsiName,
       "hwCBQoSVsiApplyPolicyDirection": hwCBQoSVsiApplyPolicyDirection,
       "hwCBQoSVsiApplyPolicyName": hwCBQoSVsiApplyPolicyName,
       "hwCBQoSVsiApplyPolicyRowStatus": hwCBQoSVsiApplyPolicyRowStatus,
       "hwCBQoSVlanApplyPolicyTable": hwCBQoSVlanApplyPolicyTable,
       "hwCBQoSVlanApplyPolicyEntry": hwCBQoSVlanApplyPolicyEntry,
       "hwCBQoSVlanApplyPolicyVlanId": hwCBQoSVlanApplyPolicyVlanId,
       "hwCBQoSVlanApplyPolicyDirection": hwCBQoSVlanApplyPolicyDirection,
       "hwCBQoSVlanApplyPolicyName": hwCBQoSVlanApplyPolicyName,
       "hwCBQoSVlanApplyPolicyRowStatus": hwCBQoSVlanApplyPolicyRowStatus,
       "hwCBQoSRuleNotSupportAlarmTable": hwCBQoSRuleNotSupportAlarmTable,
       "hwCBQoSRuleNotSupportAlarmEntry": hwCBQoSRuleNotSupportAlarmEntry,
       "hwCBQoSRuleDirection": hwCBQoSRuleDirection,
       "hwCBQoSRuleSlotID": hwCBQoSRuleSlotID,
       "hwCBQoSRuleInfo": hwCBQoSRuleInfo,
       "hwCBQoSActionNotSupportAlarmTable": hwCBQoSActionNotSupportAlarmTable,
       "hwCBQoSActionNotSupportAlarmEntry": hwCBQoSActionNotSupportAlarmEntry,
       "hwCBQoSActionDirection": hwCBQoSActionDirection,
       "hwCBQoSActionSlotID": hwCBQoSActionSlotID,
       "hwCBQoSActionInfo": hwCBQoSActionInfo,
       "hwCBQoSIfApplyMultiPolicyTable": hwCBQoSIfApplyMultiPolicyTable,
       "hwCBQoSIfApplyMultiPolicyEntry": hwCBQoSIfApplyMultiPolicyEntry,
       "hwCBQoSIfApplyMultiPolicyIfIndex": hwCBQoSIfApplyMultiPolicyIfIndex,
       "hwCBQoSIfApplyMultiPolicyDirection": hwCBQoSIfApplyMultiPolicyDirection,
       "hwCBQoSIfApplyMultiPolicyIndex": hwCBQoSIfApplyMultiPolicyIndex,
       "hwCBQoSIfApplyMultiPolicyName": hwCBQoSIfApplyMultiPolicyName,
       "hwCBQoSIfApplyMultiPolicyRowStatus": hwCBQoSIfApplyMultiPolicyRowStatus,
       "hwCBQoSVlanApplyMultiPolicyTable": hwCBQoSVlanApplyMultiPolicyTable,
       "hwCBQoSVlanApplyMultiPolicyEntry": hwCBQoSVlanApplyMultiPolicyEntry,
       "hwCBQoSVlanApplyMultiPolicyVlanId": hwCBQoSVlanApplyMultiPolicyVlanId,
       "hwCBQoSVlanApplyMultiPolicyDirection": hwCBQoSVlanApplyMultiPolicyDirection,
       "hwCBQoSVlanApplyMultiPolicyIndex": hwCBQoSVlanApplyMultiPolicyIndex,
       "hwCBQoSVlanApplyMultiPolicyName": hwCBQoSVlanApplyMultiPolicyName,
       "hwCBQoSVlanApplyMultiPolicyRowStatus": hwCBQoSVlanApplyMultiPolicyRowStatus,
       "hwCBQoSApplyPolicyStaticsObjects": hwCBQoSApplyPolicyStaticsObjects,
       "hwCBQoSIfStaticsObjects": hwCBQoSIfStaticsObjects,
       "hwCBQoSIfCbqRunInfoTable": hwCBQoSIfCbqRunInfoTable,
       "hwCBQoSIfCbqRunInfoEntry": hwCBQoSIfCbqRunInfoEntry,
       "hwCBQoSIfCbqQueueSize": hwCBQoSIfCbqQueueSize,
       "hwCBQoSIfCbqDiscard": hwCBQoSIfCbqDiscard,
       "hwCBQoSIfCbqEfQueueSize": hwCBQoSIfCbqEfQueueSize,
       "hwCBQoSIfCbqAfQueueSize": hwCBQoSIfCbqAfQueueSize,
       "hwCBQoSIfCbqBeQueueSize": hwCBQoSIfCbqBeQueueSize,
       "hwCBQoSIfCbqBeActiveQueueNum": hwCBQoSIfCbqBeActiveQueueNum,
       "hwCBQoSIfCbqBeMaxActiveQueueNum": hwCBQoSIfCbqBeMaxActiveQueueNum,
       "hwCBQoSIfCbqBeTotalQueueNum": hwCBQoSIfCbqBeTotalQueueNum,
       "hwCBQoSIfCbqAfAllocatedQueueNum": hwCBQoSIfCbqAfAllocatedQueueNum,
       "hwCBQoSIfClassMatchRunInfoTable": hwCBQoSIfClassMatchRunInfoTable,
       "hwCBQoSIfClassMatchRunInfoEntry": hwCBQoSIfClassMatchRunInfoEntry,
       "hwCBQoSIfClassMatchedPackets": hwCBQoSIfClassMatchedPackets,
       "hwCBQoSIfClassMatchedBytes": hwCBQoSIfClassMatchedBytes,
       "hwCBQoSIfClassAverageRate": hwCBQoSIfClassAverageRate,
       "hwCBQosIfClassPassedPackets": hwCBQosIfClassPassedPackets,
       "hwCBQosIfClassDroppedPackets": hwCBQosIfClassDroppedPackets,
       "hwCBQoSIfCarRunInfoTable": hwCBQoSIfCarRunInfoTable,
       "hwCBQoSIfCarRunInfoEntry": hwCBQoSIfCarRunInfoEntry,
       "hwCBQoSIfCarGreenPassedPackets": hwCBQoSIfCarGreenPassedPackets,
       "hwCBQoSIfCarGreenPassedBytes": hwCBQoSIfCarGreenPassedBytes,
       "hwCBQoSIfCarGreenRemarkedPackets": hwCBQoSIfCarGreenRemarkedPackets,
       "hwCBQoSIfCarGreenRemarkedBytes": hwCBQoSIfCarGreenRemarkedBytes,
       "hwCBQoSIfCarGreenDiscardedPackets": hwCBQoSIfCarGreenDiscardedPackets,
       "hwCBQoSIfCarGreenDiscardedBytes": hwCBQoSIfCarGreenDiscardedBytes,
       "hwCBQoSIfCarYellowPassedPackets": hwCBQoSIfCarYellowPassedPackets,
       "hwCBQoSIfCarYellowPassedBytes": hwCBQoSIfCarYellowPassedBytes,
       "hwCBQoSIfCarYellowRemarkedPackets": hwCBQoSIfCarYellowRemarkedPackets,
       "hwCBQoSIfCarYellowRemarkedBytes": hwCBQoSIfCarYellowRemarkedBytes,
       "hwCBQoSIfCarYellowDiscardedPackets": hwCBQoSIfCarYellowDiscardedPackets,
       "hwCBQoSIfCarYellowDiscardedBytes": hwCBQoSIfCarYellowDiscardedBytes,
       "hwCBQoSIfCarRedPassedPackets": hwCBQoSIfCarRedPassedPackets,
       "hwCBQoSIfCarRedPassedBytes": hwCBQoSIfCarRedPassedBytes,
       "hwCBQoSIfCarRedRemarkedPackets": hwCBQoSIfCarRedRemarkedPackets,
       "hwCBQoSIfCarRedRemarkedBytes": hwCBQoSIfCarRedRemarkedBytes,
       "hwCBQoSIfCarRedDiscardedPackets": hwCBQoSIfCarRedDiscardedPackets,
       "hwCBQoSIfCarRedDiscardedBytes": hwCBQoSIfCarRedDiscardedBytes,
       "hwCBQoSIfCarGreenPassedPacketsRate": hwCBQoSIfCarGreenPassedPacketsRate,
       "hwCBQoSIfCarGreenPassedBytesRate": hwCBQoSIfCarGreenPassedBytesRate,
       "hwCBQoSIfCarGreenRemarkedPacketsRate": hwCBQoSIfCarGreenRemarkedPacketsRate,
       "hwCBQoSIfCarGreenRemarkedBytesRate": hwCBQoSIfCarGreenRemarkedBytesRate,
       "hwCBQoSIfCarGreenDiscardedPacketsRate": hwCBQoSIfCarGreenDiscardedPacketsRate,
       "hwCBQoSIfCarGreenDiscardedBytesRate": hwCBQoSIfCarGreenDiscardedBytesRate,
       "hwCBQoSIfCarYellowPassedPacketsRate": hwCBQoSIfCarYellowPassedPacketsRate,
       "hwCBQoSIfCarYellowPassedBytesRate": hwCBQoSIfCarYellowPassedBytesRate,
       "hwCBQoSIfCarYellowRemarkedPacketsRate": hwCBQoSIfCarYellowRemarkedPacketsRate,
       "hwCBQoSIfCarYellowRemarkedBytesRate": hwCBQoSIfCarYellowRemarkedBytesRate,
       "hwCBQoSIfCarYellowDiscardedPacketsRate": hwCBQoSIfCarYellowDiscardedPacketsRate,
       "hwCBQoSIfCarYellowDiscardedBytesRate": hwCBQoSIfCarYellowDiscardedBytesRate,
       "hwCBQoSIfCarRedPassedPacketsRate": hwCBQoSIfCarRedPassedPacketsRate,
       "hwCBQoSIfCarRedPassedBytesRate": hwCBQoSIfCarRedPassedBytesRate,
       "hwCBQoSIfCarRedRemarkedPacketsRate": hwCBQoSIfCarRedRemarkedPacketsRate,
       "hwCBQoSIfCarRedRemarkedBytesRate": hwCBQoSIfCarRedRemarkedBytesRate,
       "hwCBQoSIfCarRedDiscardedPacketsRate": hwCBQoSIfCarRedDiscardedPacketsRate,
       "hwCBQoSIfCarRedDiscardedBytesRate": hwCBQoSIfCarRedDiscardedBytesRate,
       "hwCBQoSIfGtsRunInfoTable": hwCBQoSIfGtsRunInfoTable,
       "hwCBQoSIfGtsRunInfoEntry": hwCBQoSIfGtsRunInfoEntry,
       "hwCBQoSIfGtsPassedPackets": hwCBQoSIfGtsPassedPackets,
       "hwCBQoSIfGtsPassedBytes": hwCBQoSIfGtsPassedBytes,
       "hwCBQoSIfGtsDiscardedPackets": hwCBQoSIfGtsDiscardedPackets,
       "hwCBQoSIfGtsDiscardedBytes": hwCBQoSIfGtsDiscardedBytes,
       "hwCBQoSIfGtsDelayedPackets": hwCBQoSIfGtsDelayedPackets,
       "hwCBQoSIfGtsDelayedBytes": hwCBQoSIfGtsDelayedBytes,
       "hwCBQoSIfGtsQueueSize": hwCBQoSIfGtsQueueSize,
       "hwCBQoSIfRemarkRunInfoTable": hwCBQoSIfRemarkRunInfoTable,
       "hwCBQoSIfRemarkRunInfoEntry": hwCBQoSIfRemarkRunInfoEntry,
       "hwCBQoSIfRemarkedPackets": hwCBQoSIfRemarkedPackets,
       "hwCBQoSIfRemarkedBytes": hwCBQoSIfRemarkedBytes,
       "hwCBQoSIfQueueRunInfoTable": hwCBQoSIfQueueRunInfoTable,
       "hwCBQoSIfQueueRunInfoEntry": hwCBQoSIfQueueRunInfoEntry,
       "hwCBQoSIfQueueMatchedPackets": hwCBQoSIfQueueMatchedPackets,
       "hwCBQoSIfQueueMatchedBytes": hwCBQoSIfQueueMatchedBytes,
       "hwCBQoSIfQueueEnqueuedPackets": hwCBQoSIfQueueEnqueuedPackets,
       "hwCBQoSIfQueueEnqueuedBytes": hwCBQoSIfQueueEnqueuedBytes,
       "hwCBQoSIfQueueDiscardedPackets": hwCBQoSIfQueueDiscardedPackets,
       "hwCBQoSIfQueueDiscardedBytes": hwCBQoSIfQueueDiscardedBytes,
       "hwCBQoSIfQueueMatchedPacketsRate": hwCBQoSIfQueueMatchedPacketsRate,
       "hwCBQoSIfQueueMatchedBytesRate": hwCBQoSIfQueueMatchedBytesRate,
       "hwCBQoSIfQueueEnqueuedPacketsRate": hwCBQoSIfQueueEnqueuedPacketsRate,
       "hwCBQoSIfQueueEnqueuedBytesRate": hwCBQoSIfQueueEnqueuedBytesRate,
       "hwCBQoSIfQueueDiscardedPacketsRate": hwCBQoSIfQueueDiscardedPacketsRate,
       "hwCBQoSIfQueueDiscardedBytesRate": hwCBQoSIfQueueDiscardedBytesRate,
       "hwCBQoSIfWredRunInfoTable": hwCBQoSIfWredRunInfoTable,
       "hwCBQoSIfWredRunInfoEntry": hwCBQoSIfWredRunInfoEntry,
       "hwCBQoSIfWredRandomDiscardedPackets": hwCBQoSIfWredRandomDiscardedPackets,
       "hwCBQoSIfWredTailDiscardedPackets": hwCBQoSIfWredTailDiscardedPackets,
       "hwCBQoSIfLrRunInfoTable": hwCBQoSIfLrRunInfoTable,
       "hwCBQoSIfLrRunInfoEntry": hwCBQoSIfLrRunInfoEntry,
       "hwCBQoSIfLrPassedPackets": hwCBQoSIfLrPassedPackets,
       "hwCBQoSIfLrPassedBytes": hwCBQoSIfLrPassedBytes,
       "hwCBQoSIfLrDiscardedPackets": hwCBQoSIfLrDiscardedPackets,
       "hwCBQoSIfLrDiscardedBytes": hwCBQoSIfLrDiscardedBytes,
       "hwCBQoSIfLrDelayedPackets": hwCBQoSIfLrDelayedPackets,
       "hwCBQoSIfLrDelayedBytes": hwCBQoSIfLrDelayedBytes,
       "hwCBQoSIfRedirectRunInfoTable": hwCBQoSIfRedirectRunInfoTable,
       "hwCBQoSIfRedirectRunInfoEntry": hwCBQoSIfRedirectRunInfoEntry,
       "hwCBQoSIfRedirectedPackets": hwCBQoSIfRedirectedPackets,
       "hwCBQoSIfRedirectedBytes": hwCBQoSIfRedirectedBytes,
       "hwCBQoSIfFirewallRunInfoTable": hwCBQoSIfFirewallRunInfoTable,
       "hwCBQoSIfFirewallRunInfoEntry": hwCBQoSIfFirewallRunInfoEntry,
       "hwCBQoSIfFilteredPackets": hwCBQoSIfFilteredPackets,
       "hwCBQoSIfFilteredBytes": hwCBQoSIfFilteredBytes,
       "hwCBQoSIfMirrorRunInfoTable": hwCBQoSIfMirrorRunInfoTable,
       "hwCBQoSIfMirrorRunInfoEntry": hwCBQoSIfMirrorRunInfoEntry,
       "hwCBQoSIfMirroredPackets": hwCBQoSIfMirroredPackets,
       "hwCBQoSIfMirroredBytes": hwCBQoSIfMirroredBytes,
       "hwCBQoSIfUrpfRunInfoTable": hwCBQoSIfUrpfRunInfoTable,
       "hwCBQoSIfUrpfRunInfoEntry": hwCBQoSIfUrpfRunInfoEntry,
       "hwCBQoSIfUrpfPassedPackets": hwCBQoSIfUrpfPassedPackets,
       "hwCBQoSIfUrpfPassedBytes": hwCBQoSIfUrpfPassedBytes,
       "hwCBQoSIfUrpfDroppedPackets": hwCBQoSIfUrpfDroppedPackets,
       "hwCBQoSIfUrpfDroppedBytes": hwCBQoSIfUrpfDroppedBytes,
       "hwCBQoSIfSampleRunInfoTable": hwCBQoSIfSampleRunInfoTable,
       "hwCBQoSIfSampleRunInfoEntry": hwCBQoSIfSampleRunInfoEntry,
       "hwCBQoSIfSampledPackets": hwCBQoSIfSampledPackets,
       "hwCBQoSIfSampledBytes": hwCBQoSIfSampledBytes,
       "hwCBQoSAtmPvcStaticsObjects": hwCBQoSAtmPvcStaticsObjects,
       "hwCBQoSAtmPvcCbqRunInfoTable": hwCBQoSAtmPvcCbqRunInfoTable,
       "hwCBQoSAtmPvcCbqRunInfoEntry": hwCBQoSAtmPvcCbqRunInfoEntry,
       "hwCBQoSAtmPvcCbqQueueSize": hwCBQoSAtmPvcCbqQueueSize,
       "hwCBQoSAtmPvcCbqDiscard": hwCBQoSAtmPvcCbqDiscard,
       "hwCBQoSAtmPvcCbqEfQueueSize": hwCBQoSAtmPvcCbqEfQueueSize,
       "hwCBQoSAtmPvcCbqAfQueueSize": hwCBQoSAtmPvcCbqAfQueueSize,
       "hwCBQoSAtmPvcCbqBeQueueSize": hwCBQoSAtmPvcCbqBeQueueSize,
       "hwCBQoSAtmPvcCbqBeActiveQueueNum": hwCBQoSAtmPvcCbqBeActiveQueueNum,
       "hwCBQoSAtmPvcCbqBeMaxActiveQueueNum": hwCBQoSAtmPvcCbqBeMaxActiveQueueNum,
       "hwCBQoSAtmPvcCbqBeTotalQueueNum": hwCBQoSAtmPvcCbqBeTotalQueueNum,
       "hwCBQoSAtmPvcCbqAfAllocatedQueueNum": hwCBQoSAtmPvcCbqAfAllocatedQueueNum,
       "hwCBQoSAtmPvcClassMatchRunInfoTable": hwCBQoSAtmPvcClassMatchRunInfoTable,
       "hwCBQoSAtmPvcClassMatchRunInfoEntry": hwCBQoSAtmPvcClassMatchRunInfoEntry,
       "hwCBQoSAtmPvcClassMatchPackets": hwCBQoSAtmPvcClassMatchPackets,
       "hwCBQoSAtmPvcClassMatchBytes": hwCBQoSAtmPvcClassMatchBytes,
       "hwCBQoSAtmPvcClassAverageRate": hwCBQoSAtmPvcClassAverageRate,
       "hwCBQoSAtmPvcCarRunInfoTable": hwCBQoSAtmPvcCarRunInfoTable,
       "hwCBQoSAtmPvcCarRunInfoEntry": hwCBQoSAtmPvcCarRunInfoEntry,
       "hwCBQoSAtmPvcCarConformPackets": hwCBQoSAtmPvcCarConformPackets,
       "hwCBQoSAtmPvcCarConformBytes": hwCBQoSAtmPvcCarConformBytes,
       "hwCBQoSAtmPvcCarExceedPackets": hwCBQoSAtmPvcCarExceedPackets,
       "hwCBQoSAtmPvcCarExceedBytes": hwCBQoSAtmPvcCarExceedBytes,
       "hwCBQoSAtmPvcCarConformPacketsRate": hwCBQoSAtmPvcCarConformPacketsRate,
       "hwCBQoSAtmPvcCarConformBytesRate": hwCBQoSAtmPvcCarConformBytesRate,
       "hwCBQoSAtmPvcCarExceedPacketsRate": hwCBQoSAtmPvcCarExceedPacketsRate,
       "hwCBQoSAtmPvcCarExceedBytesRate": hwCBQoSAtmPvcCarExceedBytesRate,
       "hwCBQoSAtmPvcGtsRunInfoTable": hwCBQoSAtmPvcGtsRunInfoTable,
       "hwCBQoSAtmPvcGtsRunInfoEntry": hwCBQoSAtmPvcGtsRunInfoEntry,
       "hwCBQoSAtmPvcGtsPassedPackets": hwCBQoSAtmPvcGtsPassedPackets,
       "hwCBQoSAtmPvcGtsPassedBytes": hwCBQoSAtmPvcGtsPassedBytes,
       "hwCBQoSAtmPvcGtsDiscardedPackets": hwCBQoSAtmPvcGtsDiscardedPackets,
       "hwCBQoSAtmPvcGtsDiscardedBytes": hwCBQoSAtmPvcGtsDiscardedBytes,
       "hwCBQoSAtmPvcGtsDelayedPackets": hwCBQoSAtmPvcGtsDelayedPackets,
       "hwCBQoSAtmPvcGtsDelayedBytes": hwCBQoSAtmPvcGtsDelayedBytes,
       "hwCBQoSAtmPvcGtsQueueSize": hwCBQoSAtmPvcGtsQueueSize,
       "hwCBQoSAtmPvcRemarkRunInfoTable": hwCBQoSAtmPvcRemarkRunInfoTable,
       "hwCBQoSAtmPvcRemarkRunInfoEntry": hwCBQoSAtmPvcRemarkRunInfoEntry,
       "hwCBQoSAtmPvcRemarkedPackets": hwCBQoSAtmPvcRemarkedPackets,
       "hwCBQoSAtmPvcQueueRunInfoTable": hwCBQoSAtmPvcQueueRunInfoTable,
       "hwCBQoSAtmPvcQueueRunInfoEntry": hwCBQoSAtmPvcQueueRunInfoEntry,
       "hwCBQoSAtmPvcQueueMatchedPackets": hwCBQoSAtmPvcQueueMatchedPackets,
       "hwCBQoSAtmPvcQueueMatchedBytes": hwCBQoSAtmPvcQueueMatchedBytes,
       "hwCBQoSAtmPvcQueueEnqueuedPackets": hwCBQoSAtmPvcQueueEnqueuedPackets,
       "hwCBQoSAtmPvcQueueEnqueuedBytes": hwCBQoSAtmPvcQueueEnqueuedBytes,
       "hwCBQoSAtmPvcQueueDiscardedPackets": hwCBQoSAtmPvcQueueDiscardedPackets,
       "hwCBQoSAtmPvcQueueDiscardedBytes": hwCBQoSAtmPvcQueueDiscardedBytes,
       "hwCBQoSAtmPvcQueueMatchedPacketsRate": hwCBQoSAtmPvcQueueMatchedPacketsRate,
       "hwCBQoSAtmPvcQueueMatchedBytesRate": hwCBQoSAtmPvcQueueMatchedBytesRate,
       "hwCBQoSAtmPvcQueueEnqueuedPacketsRate": hwCBQoSAtmPvcQueueEnqueuedPacketsRate,
       "hwCBQoSAtmPvcQueueEnqueuedBytesRate": hwCBQoSAtmPvcQueueEnqueuedBytesRate,
       "hwCBQoSAtmPvcQueueDiscardedPacketsRate": hwCBQoSAtmPvcQueueDiscardedPacketsRate,
       "hwCBQoSAtmPvcQueueDiscardedBytesRate": hwCBQoSAtmPvcQueueDiscardedBytesRate,
       "hwCBQoSAtmPvcWredRunInfoTable": hwCBQoSAtmPvcWredRunInfoTable,
       "hwCBQoSAtmPvcWredRunInfoEntry": hwCBQoSAtmPvcWredRunInfoEntry,
       "hwCBQoSAtmPvcWredRandomDiscardedPackets": hwCBQoSAtmPvcWredRandomDiscardedPackets,
       "hwCBQoSAtmPvcWredTailDiscardedPackets": hwCBQoSAtmPvcWredTailDiscardedPackets,
       "hwCBQoSAtmPvcLrRunInfoTable": hwCBQoSAtmPvcLrRunInfoTable,
       "hwCBQoSAtmPvcLrRunInfoEntry": hwCBQoSAtmPvcLrRunInfoEntry,
       "hwCBQoSAtmPvcLrPassedPackets": hwCBQoSAtmPvcLrPassedPackets,
       "hwCBQoSAtmPvcLrPassedBytes": hwCBQoSAtmPvcLrPassedBytes,
       "hwCBQoSAtmPvcLrDiscardedPackets": hwCBQoSAtmPvcLrDiscardedPackets,
       "hwCBQoSAtmPvcLrDiscardedBytes": hwCBQoSAtmPvcLrDiscardedBytes,
       "hwCBQoSAtmPvcLrDelayedPackets": hwCBQoSAtmPvcLrDelayedPackets,
       "hwCBQoSAtmPvcLrDelayedBytes": hwCBQoSAtmPvcLrDelayedBytes,
       "hwCBQoSFrPvcStaticsObjects": hwCBQoSFrPvcStaticsObjects,
       "hwCBQoSFrPvcCbqRunInfoTable": hwCBQoSFrPvcCbqRunInfoTable,
       "hwCBQoSFrPvcCbqRunInfoEntry": hwCBQoSFrPvcCbqRunInfoEntry,
       "hwCBQoSFrPvcCbqQueueSize": hwCBQoSFrPvcCbqQueueSize,
       "hwCBQoSFrPvcCbqDiscard": hwCBQoSFrPvcCbqDiscard,
       "hwCBQoSFrPvcCbqEfQueueSize": hwCBQoSFrPvcCbqEfQueueSize,
       "hwCBQoSFrPvcCbqAfQueueSize": hwCBQoSFrPvcCbqAfQueueSize,
       "hwCBQoSFrPvcCbqBeQueueSize": hwCBQoSFrPvcCbqBeQueueSize,
       "hwCBQoSFrPvcCbqBeActiveQueueNum": hwCBQoSFrPvcCbqBeActiveQueueNum,
       "hwCBQoSFrPvcCbqBeMaxActiveQueueNum": hwCBQoSFrPvcCbqBeMaxActiveQueueNum,
       "hwCBQoSFrPvcCbqBeTotalQueueNum": hwCBQoSFrPvcCbqBeTotalQueueNum,
       "hwCBQoSFrPvcCbqAfAllocatedQueueNum": hwCBQoSFrPvcCbqAfAllocatedQueueNum,
       "hwCBQoSFrPvcClassMatchRunInfoTable": hwCBQoSFrPvcClassMatchRunInfoTable,
       "hwCBQoSFrPvcClassMatchRunInfoEntry": hwCBQoSFrPvcClassMatchRunInfoEntry,
       "hwCBQoSFrPvcClassMatchedPackets": hwCBQoSFrPvcClassMatchedPackets,
       "hwCBQoSFrPvcClassMatchedBytes": hwCBQoSFrPvcClassMatchedBytes,
       "hwCBQoSFrPvcClassAverageRate": hwCBQoSFrPvcClassAverageRate,
       "hwCBQoSFrPvcCarRunInfoTable": hwCBQoSFrPvcCarRunInfoTable,
       "hwCBQoSFrPvcCarRunInfoEntry": hwCBQoSFrPvcCarRunInfoEntry,
       "hwCBQoSFrPvcCarConformPackets": hwCBQoSFrPvcCarConformPackets,
       "hwCBQoSFrPvcCarConformBytes": hwCBQoSFrPvcCarConformBytes,
       "hwCBQoSFrPvcCarExceedPackets": hwCBQoSFrPvcCarExceedPackets,
       "hwCBQoSFrPvcCarExceedBytes": hwCBQoSFrPvcCarExceedBytes,
       "hwCBQoSFrPvcCarConformPacketsRate": hwCBQoSFrPvcCarConformPacketsRate,
       "hwCBQoSFrPvcCarConformBytesRate": hwCBQoSFrPvcCarConformBytesRate,
       "hwCBQoSFrPvcCarExceedPacketsRate": hwCBQoSFrPvcCarExceedPacketsRate,
       "hwCBQoSFrPvcCarExceedBytesRate": hwCBQoSFrPvcCarExceedBytesRate,
       "hwCBQoSFrPvcGtsRunInfoTable": hwCBQoSFrPvcGtsRunInfoTable,
       "hwCBQoSFrPvcGtsRunInfoEntry": hwCBQoSFrPvcGtsRunInfoEntry,
       "hwCBQoSFrPvcGtsPassedPackets": hwCBQoSFrPvcGtsPassedPackets,
       "hwCBQoSFrPvcGtsPassedBytes": hwCBQoSFrPvcGtsPassedBytes,
       "hwCBQoSFrPvcGtsDiscardedPackets": hwCBQoSFrPvcGtsDiscardedPackets,
       "hwCBQoSFrPvcGtsDiscardedBytes": hwCBQoSFrPvcGtsDiscardedBytes,
       "hwCBQoSFrPvcGtsDelayedPackets": hwCBQoSFrPvcGtsDelayedPackets,
       "hwCBQoSFrPvcGtsDelayedBytes": hwCBQoSFrPvcGtsDelayedBytes,
       "hwCBQoSFrPvcGtsQueueSize": hwCBQoSFrPvcGtsQueueSize,
       "hwCBQoSFrPvcRemarkRunInfoTable": hwCBQoSFrPvcRemarkRunInfoTable,
       "hwCBQoSFrPvcRemarkRunInfoEntry": hwCBQoSFrPvcRemarkRunInfoEntry,
       "hwCBQoSFrPvcRemarkedPackets": hwCBQoSFrPvcRemarkedPackets,
       "hwCBQoSFrPvcQueueRunInfoTable": hwCBQoSFrPvcQueueRunInfoTable,
       "hwCBQoSFrPvcQueueRunInfoEntry": hwCBQoSFrPvcQueueRunInfoEntry,
       "hwCBQoSFrPvcQueueMatchedPackets": hwCBQoSFrPvcQueueMatchedPackets,
       "hwCBQoSFrPvcQueueMatchedBytes": hwCBQoSFrPvcQueueMatchedBytes,
       "hwCBQoSFrPvcQueueEnqueuedPackets": hwCBQoSFrPvcQueueEnqueuedPackets,
       "hwCBQoSFrPvcQueueEnqueuedBytes": hwCBQoSFrPvcQueueEnqueuedBytes,
       "hwCBQoSFrPvcQueueDiscardedPackets": hwCBQoSFrPvcQueueDiscardedPackets,
       "hwCBQoSFrPvcQueueDiscardedBytes": hwCBQoSFrPvcQueueDiscardedBytes,
       "hwCBQoSFrPvcQueueMatchedPacketsRate": hwCBQoSFrPvcQueueMatchedPacketsRate,
       "hwCBQoSFrPvcQueueMatchedBytesRate": hwCBQoSFrPvcQueueMatchedBytesRate,
       "hwCBQoSFrPvcQueueEnqueuedPacketsRate": hwCBQoSFrPvcQueueEnqueuedPacketsRate,
       "hwCBQoSFrPvcQueueEnqueuedBytesRate": hwCBQoSFrPvcQueueEnqueuedBytesRate,
       "hwCBQoSFrPvcQueueDiscardedPacketsRate": hwCBQoSFrPvcQueueDiscardedPacketsRate,
       "hwCBQoSFrPvcQueueDiscardedBytesRate": hwCBQoSFrPvcQueueDiscardedBytesRate,
       "hwCBQoSFrPvcWredRunInfoTable": hwCBQoSFrPvcWredRunInfoTable,
       "hwCBQoSFrPvcWredRunInfoEntry": hwCBQoSFrPvcWredRunInfoEntry,
       "hwCBQoSFrPvcWredRandomDiscardedPackets": hwCBQoSFrPvcWredRandomDiscardedPackets,
       "hwCBQoSFrPvcWredTailDiscardedPackets": hwCBQoSFrPvcWredTailDiscardedPackets,
       "hwCBQoSFrPvcLrRunInfoTable": hwCBQoSFrPvcLrRunInfoTable,
       "hwCBQoSFrPvcLrRunInfoEntry": hwCBQoSFrPvcLrRunInfoEntry,
       "hwCBQoSFrPvcLrPassedPackets": hwCBQoSFrPvcLrPassedPackets,
       "hwCBQoSFrPvcLrPassedBytes": hwCBQoSFrPvcLrPassedBytes,
       "hwCBQoSFrPvcLrDiscardedPackets": hwCBQoSFrPvcLrDiscardedPackets,
       "hwCBQoSFrPvcLrDiscardedBytes": hwCBQoSFrPvcLrDiscardedBytes,
       "hwCBQoSFrPvcLrDelayedPackets": hwCBQoSFrPvcLrDelayedPackets,
       "hwCBQoSFrPvcLrDelayedBytes": hwCBQoSFrPvcLrDelayedBytes,
       "hwCBQoSIfVlanStaticsObjects": hwCBQoSIfVlanStaticsObjects,
       "hwCBQoSIfVlanClassMatchRunInfoTable": hwCBQoSIfVlanClassMatchRunInfoTable,
       "hwCBQoSIfVlanClassMatchRunInfoEntry": hwCBQoSIfVlanClassMatchRunInfoEntry,
       "hwCBQoSIfVlanClassMatchedPackets": hwCBQoSIfVlanClassMatchedPackets,
       "hwCBQoSIfVlanClassMatchedBytes": hwCBQoSIfVlanClassMatchedBytes,
       "hwCBQoSVsiStaticsObjects": hwCBQoSVsiStaticsObjects,
       "hwCBQoSVsiClassMatchRunInfoTable": hwCBQoSVsiClassMatchRunInfoTable,
       "hwCBQoSVsiClassMatchRunInfoEntry": hwCBQoSVsiClassMatchRunInfoEntry,
       "hwCBQoSVsiClassMatchedPackets": hwCBQoSVsiClassMatchedPackets,
       "hwCBQoSVsiClassMatchedBytes": hwCBQoSVsiClassMatchedBytes,
       "hwCBQoSPolicyStatisticsObjects": hwCBQoSPolicyStatisticsObjects,
       "hwCBQoSCarStatisticsTable": hwCBQoSCarStatisticsTable,
       "hwCBQoSCarStatisticsEntry": hwCBQoSCarStatisticsEntry,
       "hwCBQoSCarConformedPackets": hwCBQoSCarConformedPackets,
       "hwCBQoSCarConformedBytes": hwCBQoSCarConformedBytes,
       "hwCBQoSCarConformedPacketRate": hwCBQoSCarConformedPacketRate,
       "hwCBQoSCarConformedByteRate": hwCBQoSCarConformedByteRate,
       "hwCBQoSCarExceededPackets": hwCBQoSCarExceededPackets,
       "hwCBQoSCarExceededBytes": hwCBQoSCarExceededBytes,
       "hwCBQoSCarExceededPacketRate": hwCBQoSCarExceededPacketRate,
       "hwCBQoSCarExceededByteRate": hwCBQoSCarExceededByteRate,
       "hwCBQoSCarOverflowPackets": hwCBQoSCarOverflowPackets,
       "hwCBQoSCarOverflowBytes": hwCBQoSCarOverflowBytes,
       "hwCBQoSCarOverflowPacketRate": hwCBQoSCarOverflowPacketRate,
       "hwCBQoSCarOverflowByteRate": hwCBQoSCarOverflowByteRate,
       "hwCBQoSCarPassedPackets": hwCBQoSCarPassedPackets,
       "hwCBQoSCarPassedBytes": hwCBQoSCarPassedBytes,
       "hwCBQoSCarDroppedPackets": hwCBQoSCarDroppedPackets,
       "hwCBQoSCarDroppedBytes": hwCBQoSCarDroppedBytes,
       "hwCBQoSPolicyStatisticsTable": hwCBQoSPolicyStatisticsTable,
       "hwCBQoSPolicyStatisticsEntry": hwCBQoSPolicyStatisticsEntry,
       "hwCBQoSPolicyMatchedPackets": hwCBQoSPolicyMatchedPackets,
       "hwCBQoSPolicyMatchedBytes": hwCBQoSPolicyMatchedBytes,
       "hwCBQoSPolicyUnmatchedPackets": hwCBQoSPolicyUnmatchedPackets,
       "hwCBQoSPolicyUnmatchedBytes": hwCBQoSPolicyUnmatchedBytes,
       "hwCBQoSPolicyMatchedPassPackets": hwCBQoSPolicyMatchedPassPackets,
       "hwCBQoSPolicyMatchedPassBytes": hwCBQoSPolicyMatchedPassBytes,
       "hwCBQoSPolicyMatchedDropPackets": hwCBQoSPolicyMatchedDropPackets,
       "hwCBQoSPolicyMatchedDropBytes": hwCBQoSPolicyMatchedDropBytes,
       "hwCBQoSPolicyResetFlag": hwCBQoSPolicyResetFlag,
       "hwCBQoSPolicyMatchedPacketsRate": hwCBQoSPolicyMatchedPacketsRate,
       "hwCBQoSPolicyMatchedBytesRate": hwCBQoSPolicyMatchedBytesRate,
       "hwCBQoSPolicyMatchedPassPacketsRate": hwCBQoSPolicyMatchedPassPacketsRate,
       "hwCBQoSPolicyMatchedPassBytesRate": hwCBQoSPolicyMatchedPassBytesRate,
       "hwCBQoSPolicyMatchedDropPacketsRate": hwCBQoSPolicyMatchedDropPacketsRate,
       "hwCBQoSPolicyMatchedDropBytesRate": hwCBQoSPolicyMatchedDropBytesRate,
       "hwCBQoSClassifierStatisticsTable": hwCBQoSClassifierStatisticsTable,
       "hwCBQoSClassifierStatisticsEntry": hwCBQoSClassifierStatisticsEntry,
       "hwCBQoSPolicyClassifierIndex": hwCBQoSPolicyClassifierIndex,
       "hwCBQoSClassifierMatchedPackets": hwCBQoSClassifierMatchedPackets,
       "hwCBQoSClassifierMatchedBytes": hwCBQoSClassifierMatchedBytes,
       "hwCBQoSClassifierMatchedPassPackets": hwCBQoSClassifierMatchedPassPackets,
       "hwCBQoSClassifierMatchedPassBytes": hwCBQoSClassifierMatchedPassBytes,
       "hwCBQoSClassifierMatchedDropPackets": hwCBQoSClassifierMatchedDropPackets,
       "hwCBQoSClassifierMatchedDropBytes": hwCBQoSClassifierMatchedDropBytes,
       "hwCBQoSPolicyStatisticsClassifierTable": hwCBQoSPolicyStatisticsClassifierTable,
       "hwCBQoSPolicyStatisticsClassifierEntry": hwCBQoSPolicyStatisticsClassifierEntry,
       "hwCBQoSPolicyStatClassifierName": hwCBQoSPolicyStatClassifierName,
       "hwCBQoSPolicyStatClassifierMatchedPackets": hwCBQoSPolicyStatClassifierMatchedPackets,
       "hwCBQoSPolicyStatClassifierMatchedBytes": hwCBQoSPolicyStatClassifierMatchedBytes,
       "hwCBQoSPolicyStatClassifierUnmatchedPackets": hwCBQoSPolicyStatClassifierUnmatchedPackets,
       "hwCBQoSPolicyStatClassifierUnmatchedBytes": hwCBQoSPolicyStatClassifierUnmatchedBytes,
       "hwCBQoSPolicyStatClassifierMatchedPassPackets": hwCBQoSPolicyStatClassifierMatchedPassPackets,
       "hwCBQoSPolicyStatClassifierMatchedPassBytes": hwCBQoSPolicyStatClassifierMatchedPassBytes,
       "hwCBQoSPolicyStatClassifierMatchedDropPackets": hwCBQoSPolicyStatClassifierMatchedDropPackets,
       "hwCBQoSPolicyStatClassifierMatchedDropBytes": hwCBQoSPolicyStatClassifierMatchedDropBytes,
       "hwCBQoSPolicyStatClassifierMatchedPacketsRate": hwCBQoSPolicyStatClassifierMatchedPacketsRate,
       "hwCBQoSPolicyStatClassifierMatchedBytesRate": hwCBQoSPolicyStatClassifierMatchedBytesRate,
       "hwCBQoSPolicyStatClassifierMatchedPassPacketsRate": hwCBQoSPolicyStatClassifierMatchedPassPacketsRate,
       "hwCBQoSPolicyStatClassifierMatchedPassBytesRate": hwCBQoSPolicyStatClassifierMatchedPassBytesRate,
       "hwCBQoSPolicyStatClassifierMatchedDropPacketsRate": hwCBQoSPolicyStatClassifierMatchedDropPacketsRate,
       "hwCBQoSPolicyStatClassifierMatchedDropBytesRate": hwCBQoSPolicyStatClassifierMatchedDropBytesRate,
       "hwCBQoSVlanClassMatchRunInfoTable": hwCBQoSVlanClassMatchRunInfoTable,
       "hwCBQoSVlanClassMatchRunInfoEntry": hwCBQoSVlanClassMatchRunInfoEntry,
       "hwCBQoSVlanClassMatchedPackets": hwCBQoSVlanClassMatchedPackets,
       "hwCBQoSVlanClassPassedPackets": hwCBQoSVlanClassPassedPackets,
       "hwCBQoSVlanClassDroppedPackets": hwCBQoSVlanClassDroppedPackets,
       "hwCBQoSVlanCarRunInfoTable": hwCBQoSVlanCarRunInfoTable,
       "hwCBQoSVlanCarRunInfoEntry": hwCBQoSVlanCarRunInfoEntry,
       "hwCBQoSVlanCarPassedPackets": hwCBQoSVlanCarPassedPackets,
       "hwCBQoSVlanCarDiscardedPackets": hwCBQoSVlanCarDiscardedPackets,
       "hwCBQoSMultiPolicyStatisticsTable": hwCBQoSMultiPolicyStatisticsTable,
       "hwCBQoSMultiPolicyStatisticsEntry": hwCBQoSMultiPolicyStatisticsEntry,
       "hwCBQoSMultiPolicyIndex": hwCBQoSMultiPolicyIndex,
       "hwCBQoSMultiPolicyMatchedPackets": hwCBQoSMultiPolicyMatchedPackets,
       "hwCBQoSMultiPolicyMatchedBytes": hwCBQoSMultiPolicyMatchedBytes,
       "hwCBQoSMultiPolicyUnmatchedPackets": hwCBQoSMultiPolicyUnmatchedPackets,
       "hwCBQoSMultiPolicyUnmatchedBytes": hwCBQoSMultiPolicyUnmatchedBytes,
       "hwCBQoSMultiPolicyMatchedPassPackets": hwCBQoSMultiPolicyMatchedPassPackets,
       "hwCBQoSMultiPolicyMatchedPassBytes": hwCBQoSMultiPolicyMatchedPassBytes,
       "hwCBQoSMultiPolicyMatchedDropPackets": hwCBQoSMultiPolicyMatchedDropPackets,
       "hwCBQoSMultiPolicyMatchedDropBytes": hwCBQoSMultiPolicyMatchedDropBytes,
       "hwCBQoSMultiPolicyResetFlag": hwCBQoSMultiPolicyResetFlag,
       "hwCBQoSMultiPolicyStatisticsClassifierTable": hwCBQoSMultiPolicyStatisticsClassifierTable,
       "hwCBQoSMultiPolicyStatisticsClassifierEntry": hwCBQoSMultiPolicyStatisticsClassifierEntry,
       "hwCBQoSMultiPolicyStaPolicyIndex": hwCBQoSMultiPolicyStaPolicyIndex,
       "hwCBQoSMultiPolicyStatClassifierIndex": hwCBQoSMultiPolicyStatClassifierIndex,
       "hwCBQoSMultiPolicyStatClassifierName": hwCBQoSMultiPolicyStatClassifierName,
       "hwCBQoSMultiPolicyStatClassifierMatchedPackets": hwCBQoSMultiPolicyStatClassifierMatchedPackets,
       "hwCBQoSMultiPolicyStatClassifierMatchedBytes": hwCBQoSMultiPolicyStatClassifierMatchedBytes,
       "hwCBQoSMultiPolicyStatClassifierUnmatchedPackets": hwCBQoSMultiPolicyStatClassifierUnmatchedPackets,
       "hwCBQoSMultiPolicyStatClassifierUnmatchedBytes": hwCBQoSMultiPolicyStatClassifierUnmatchedBytes,
       "hwCBQoSMultiPolicyStatClassifierMatchedPassPackets": hwCBQoSMultiPolicyStatClassifierMatchedPassPackets,
       "hwCBQoSMultiPolicyStatClassifierMatchedPassBytes": hwCBQoSMultiPolicyStatClassifierMatchedPassBytes,
       "hwCBQoSMultiPolicyStatClassifierMatchedDropPackets": hwCBQoSMultiPolicyStatClassifierMatchedDropPackets,
       "hwCBQoSMultiPolicyStatClassifierMatchedDropBytes": hwCBQoSMultiPolicyStatClassifierMatchedDropBytes,
       "hwCBQoSPolicyStatSubPolicyClassifierRunInfoTable": hwCBQoSPolicyStatSubPolicyClassifierRunInfoTable,
       "hwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry": hwCBQoSPolicyStatSubPolicyClassifierRunInfoEntry,
       "hwCBQoSSubPolicyClassIndex": hwCBQoSSubPolicyClassIndex,
       "hwCBQoSSubPolicyStatClassifierMatchedPackets": hwCBQoSSubPolicyStatClassifierMatchedPackets,
       "hwCBQoSSubPolicyStatClassifierMatchedBytes": hwCBQoSSubPolicyStatClassifierMatchedBytes,
       "hwCBQoSSubPolicyStatClassifierPassPackets": hwCBQoSSubPolicyStatClassifierPassPackets,
       "hwCBQoSSubPolicyStatClassifierPassBytes": hwCBQoSSubPolicyStatClassifierPassBytes,
       "hwCBQoSSubPolicyStatClassifierDropPackets": hwCBQoSSubPolicyStatClassifierDropPackets,
       "hwCBQoSSubPolicyStatClassifierDropBytes": hwCBQoSSubPolicyStatClassifierDropBytes,
       "hwCBQoSSubPolicyStatClassifierQueueMatchedPackets": hwCBQoSSubPolicyStatClassifierQueueMatchedPackets,
       "hwCBQoSSubPolicyStatClassifierQueueMatchedBytes": hwCBQoSSubPolicyStatClassifierQueueMatchedBytes,
       "hwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets": hwCBQoSSubPolicyStatClassifierQueueEnqueuedPackets,
       "hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes": hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytes,
       "hwCBQoSSubPolicyStatClassifierQueueDiscardedPackets": hwCBQoSSubPolicyStatClassifierQueueDiscardedPackets,
       "hwCBQoSSubPolicyStatClassifierQueueDiscardedBytes": hwCBQoSSubPolicyStatClassifierQueueDiscardedBytes,
       "hwCBQoSSubPolicyStatClassifierCarGreenPackets": hwCBQoSSubPolicyStatClassifierCarGreenPackets,
       "hwCBQoSSubPolicyStatClassifierCarGreenBytes": hwCBQoSSubPolicyStatClassifierCarGreenBytes,
       "hwCBQoSSubPolicyStatClassifierCarYellowPackets": hwCBQoSSubPolicyStatClassifierCarYellowPackets,
       "hwCBQoSSubPolicyStatClassifierCarYellowBytes": hwCBQoSSubPolicyStatClassifierCarYellowBytes,
       "hwCBQoSSubPolicyStatClassifierCarRedPackets": hwCBQoSSubPolicyStatClassifierCarRedPackets,
       "hwCBQoSSubPolicyStatClassifierCarRedBytes": hwCBQoSSubPolicyStatClassifierCarRedBytes,
       "hwCBQoSSubPolicyStatClassifierMatchedPacketsRate": hwCBQoSSubPolicyStatClassifierMatchedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierMatchedBytesRate": hwCBQoSSubPolicyStatClassifierMatchedBytesRate,
       "hwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate": hwCBQoSSubPolicyStatClassifierMatchedPassPacketsRate,
       "hwCBQoSSubPolicyStatClassifierMatchedPassBytesRate": hwCBQoSSubPolicyStatClassifierMatchedPassBytesRate,
       "hwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate": hwCBQoSSubPolicyStatClassifierMatchedDropPacketsRate,
       "hwCBQoSSubPolicyStatClassifierMatchedDropBytesRate": hwCBQoSSubPolicyStatClassifierMatchedDropBytesRate,
       "hwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate": hwCBQoSSubPolicyStatClassifierQueueMatchedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate": hwCBQoSSubPolicyStatClassifierQueueMatchedBytesRate,
       "hwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate": hwCBQoSSubPolicyStatClassifierQueueEnqueuedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate": hwCBQoSSubPolicyStatClassifierQueueEnqueuedBytesRate,
       "hwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate": hwCBQoSSubPolicyStatClassifierQueueDiscardedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate": hwCBQoSSubPolicyStatClassifierQueueDiscardedBytesRate,
       "hwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate": hwCBQoSSubPolicyStatClassifierCarGreenPassedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate": hwCBQoSSubPolicyStatClassifierCarGreenPassedBytesRate,
       "hwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate": hwCBQoSSubPolicyStatClassifierCarYellowPassedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate": hwCBQoSSubPolicyStatClassifierCarYellowPassedBytesRate,
       "hwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate": hwCBQoSSubPolicyStatClassifierCarRedPassedPacketsRate,
       "hwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate": hwCBQoSSubPolicyStatClassifierCarRedPassedBytesRate,
       "hwCBQoSGeneral": hwCBQoSGeneral,
       "hwCBQoSFrameId": hwCBQoSFrameId,
       "hwCBQoSSlotId": hwCBQoSSlotId,
       "hwCBQoSPortId": hwCBQoSPortId,
       "hwCBQoSTrapIfName": hwCBQoSTrapIfName,
       "hwCBQoSTrapType": hwCBQoSTrapType,
       "hwCBQoSTrapAction": hwCBQoSTrapAction,
       "hwCBQoSTrapPolicyName": hwCBQoSTrapPolicyName,
       "hwCBQoSTrapVlanId": hwCBQoSTrapVlanId,
       "hwCBQoSTrapEgressIfName": hwCBQoSTrapEgressIfName,
       "hwCBQoSTrapDiscardPackets": hwCBQoSTrapDiscardPackets,
       "hwCBQoSQueryObjects": hwCBQoSQueryObjects,
       "hwCBQoSClassifierIndexQueryTable": hwCBQoSClassifierIndexQueryTable,
       "hwCBQoSClassifierIndexQueryEntry": hwCBQoSClassifierIndexQueryEntry,
       "hwCBQoSQueryPolicyName": hwCBQoSQueryPolicyName,
       "hwCBQoSQueryClassifierName": hwCBQoSQueryClassifierName,
       "hwCBQoSQueryClassifierIndex": hwCBQoSQueryClassifierIndex,
       "hwCBQoSNotifications": hwCBQoSNotifications,
       "hwCBQoSGtsDiscardThresholdTrap": hwCBQoSGtsDiscardThresholdTrap,
       "hwCBQoSCarOverSpeedThresholdTrap": hwCBQoSCarOverSpeedThresholdTrap,
       "hwCBQoSRuleNotSupportAlarm": hwCBQoSRuleNotSupportAlarm,
       "hwCBQoSActionNotSupportAlarm": hwCBQoSActionNotSupportAlarm,
       "hwCBQoSConformance": hwCBQoSConformance,
       "hwCBQoSCompliances": hwCBQoSCompliances,
       "hwCBQoSCompliance": hwCBQoSCompliance,
       "hwCBQoSGroups": hwCBQoSGroups,
       "hwCBQoSClassifierGroup": hwCBQoSClassifierGroup,
       "hwCBQoSBehaviorGroup": hwCBQoSBehaviorGroup,
       "hwCBQoSCarGroup": hwCBQoSCarGroup,
       "hwCBQoSGtsGroup": hwCBQoSGtsGroup,
       "hwCBQoSRemarkGroup": hwCBQoSRemarkGroup,
       "hwCBQoSQueueGroup": hwCBQoSQueueGroup,
       "hwCBQoSWredGroup": hwCBQoSWredGroup,
       "hwCBQoSNatGroup": hwCBQoSNatGroup,
       "hwCBQoSFirewallGroup": hwCBQoSFirewallGroup,
       "hwCBQoSSamplingGroup": hwCBQoSSamplingGroup,
       "hwCBQoSEgressGtsGroup": hwCBQoSEgressGtsGroup,
       "hwCBQoSServiceClassGroup": hwCBQoSServiceClassGroup,
       "hwCBQoSPolicyGroup": hwCBQoSPolicyGroup,
       "hwCBQoSIfApplyPolicyGroup": hwCBQoSIfApplyPolicyGroup,
       "hwCBQoSAtmPvcApplyPolicyGroup": hwCBQoSAtmPvcApplyPolicyGroup,
       "hwCBQoSIfVlanApplyPolicyGroup": hwCBQoSIfVlanApplyPolicyGroup,
       "hwCBQoSFrClassApplyPolicyGroup": hwCBQoSFrClassApplyPolicyGroup,
       "hwCBQoSFrPvcApplyPolicyGroup": hwCBQoSFrPvcApplyPolicyGroup,
       "hwCBQoSIfCbqRunInfoGroup": hwCBQoSIfCbqRunInfoGroup,
       "hwCBQoSIfClassMatchRunInfoGroup": hwCBQoSIfClassMatchRunInfoGroup,
       "hwCBQoSIfCarRunInfoGroup": hwCBQoSIfCarRunInfoGroup,
       "hwCBQoSIfGtsRunInfoGroup": hwCBQoSIfGtsRunInfoGroup,
       "hwCBQoSIfRemarkRunInfoGroup": hwCBQoSIfRemarkRunInfoGroup,
       "hwCBQoSIfQueueRunInfoGroup": hwCBQoSIfQueueRunInfoGroup,
       "hwCBQoSIfWredRunInfoGroup": hwCBQoSIfWredRunInfoGroup,
       "hwCBQoSAtmPvcCbqRunInfoGroup": hwCBQoSAtmPvcCbqRunInfoGroup,
       "hwCBQoSAtmPvcClassMatchRunInfoGroup": hwCBQoSAtmPvcClassMatchRunInfoGroup,
       "hwCBQoSAtmPvcCarRunInfoGroup": hwCBQoSAtmPvcCarRunInfoGroup,
       "hwCBQoSAtmPvcGtsRunInfoGroup": hwCBQoSAtmPvcGtsRunInfoGroup,
       "hwCBQoSAtmPvcRemarkRunInfoGroup": hwCBQoSAtmPvcRemarkRunInfoGroup,
       "hwCBQoSAtmPvcQueueRunInfoGroup": hwCBQoSAtmPvcQueueRunInfoGroup,
       "hwCBQoSAtmPvcWredRunInfoGroup": hwCBQoSAtmPvcWredRunInfoGroup,
       "hwCBQoSFrPvcCbqRunInfoGroup": hwCBQoSFrPvcCbqRunInfoGroup,
       "hwCBQoSFrPvcClassMatchRunInfoGroup": hwCBQoSFrPvcClassMatchRunInfoGroup,
       "hwCBQoSFrPvcCarRunInfoGroup": hwCBQoSFrPvcCarRunInfoGroup,
       "hwCBQoSFrPvcGtsRunInfoGroup": hwCBQoSFrPvcGtsRunInfoGroup,
       "hwCBQoSFrPvcRemarkRunInfoGroup": hwCBQoSFrPvcRemarkRunInfoGroup,
       "hwCBQoSFrPvcQueueRunInfoGroup": hwCBQoSFrPvcQueueRunInfoGroup,
       "hwCBQoSFrPvcWredRunInfoGroup": hwCBQoSFrPvcWredRunInfoGroup,
       "hwCBQoSIfVlanClassMatchRunInfoGroup": hwCBQoSIfVlanClassMatchRunInfoGroup,
       "hwCBQoSLrGroup": hwCBQoSLrGroup,
       "hwCBQoSNestPolicyGroup": hwCBQoSNestPolicyGroup,
       "hwCBQoSIfLrRunInfoGroup": hwCBQoSIfLrRunInfoGroup,
       "hwCBQoSAtmPvcLrRunInfoGroup": hwCBQoSAtmPvcLrRunInfoGroup,
       "hwCBQoSFrPvcLrRunInfoGroup": hwCBQoSFrPvcLrRunInfoGroup,
       "hwCBQoSCarStatisticsGroup": hwCBQoSCarStatisticsGroup,
       "hwCBQoSPolicyStatisticsGroup": hwCBQoSPolicyStatisticsGroup,
       "hwCBQoSRedirectGroup": hwCBQoSRedirectGroup,
       "hwCBQoSGeneralGroup": hwCBQoSGeneralGroup,
       "hwCBQoSNotificationsGroup": hwCBQoSNotificationsGroup,
       "hwCBQoSPolicyShareModeGroup": hwCBQoSPolicyShareModeGroup,
       "hwCBQoSClassifierStatisticsGroup": hwCBQoSClassifierStatisticsGroup,
       "hwCBQoSPolicyStatisticsClassifierGroup": hwCBQoSPolicyStatisticsClassifierGroup,
       "hwCBQoSVlanApplyPolicyGroup": hwCBQoSVlanApplyPolicyGroup,
       "hwCBQoSSVlanClassMatchGroup": hwCBQoSSVlanClassMatchGroup,
       "hwCBQoSSVlanCarMatchGroup": hwCBQoSSVlanCarMatchGroup,
       "hwCBQoSRandomDiscardCfgInfoGroup": hwCBQoSRandomDiscardCfgInfoGroup,
       "hwCBQoSDenyPacketLengthCfgInfoGroup": hwCBQoSDenyPacketLengthCfgInfoGroup,
       "hwCBQoSDAAStatisticsCfgInfoGroup": hwCBQoSDAAStatisticsCfgInfoGroup,
       "hwCBQoSDAATariffLevelCfgInfoGroup": hwCBQoSDAATariffLevelCfgInfoGroup,
       "hwCBQoSRuleNotSupportAlarmGroup": hwCBQoSRuleNotSupportAlarmGroup,
       "hwCBQoSActionNotSupportAlarmGroup": hwCBQoSActionNotSupportAlarmGroup,
       "hwCBQoSPolicyStatSubPolicyClassifierRunInfoGroup": hwCBQoSPolicyStatSubPolicyClassifierRunInfoGroup}
)
