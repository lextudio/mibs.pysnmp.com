# SNMP MIB module (A3COM-HUAWEI-CBQOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-CBQOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:23 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cCBQos2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2)
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("matchRuleAny", 1),
          ("matchRuleAtmClp", 11),
          ("matchRuleBittorrent", 24),
          ("matchRuleClassifier", 16),
          ("matchRuleDestinationMac", 14),
          ("matchRuleDropPriority", 23),
          ("matchRuleDscp", 7),
          ("matchRuleFrDe", 12),
          ("matchRuleIPXProtocol", 6),
          ("matchRuleIPv4Protocol", 4),
          ("matchRuleIPv6Acl", 3),
          ("matchRuleIPv6Protocol", 5),
          ("matchRuleInboundInterface", 17),
          ("matchRuleIpPre", 8),
          ("matchRuleIpv4Acl", 2),
          ("matchRuleLocalPrecedence", 22),
          ("matchRuleMplsExp", 10),
          ("matchRuleQosLocalID", 15),
          ("matchRuleRtpPort", 18),
          ("matchRuleServiceDot1p", 25),
          ("matchRuleSourceIp", 19),
          ("matchRuleSourceMac", 13),
          ("matchRuleTopMostVlanID", 21),
          ("matchRuleVlan8021p", 9),
          ("matchRuleVlanID", 20))
    )



class CarAction(Integer32, TextualConvention):
    status = "current"
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
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("discard", 3),
          ("invalid", 0),
          ("pass", 1),
          ("remark", 4),
          ("remark-atm-clp-continue", 13),
          ("remark-atm-clp-pass", 14),
          ("remark-dot1p-continue", 11),
          ("remark-dot1p-pass", 12),
          ("remark-drop-pre-pass", 18),
          ("remark-dscp-continue", 9),
          ("remark-dscp-pass", 10),
          ("remark-fr-de-continue", 15),
          ("remark-fr-de-pass", 16),
          ("remark-ip-continue", 5),
          ("remark-ip-pass", 6),
          ("remark-local-pre-pass", 17),
          ("remark-mplsexp-continue", 7),
          ("remark-mplsexp-pass", 8))
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("typeAtmClp", 5),
          ("typeDropPrecedence", 9),
          ("typeDscp", 2),
          ("typeFrDe", 6),
          ("typeIpPrecedence", 1),
          ("typeLocalPrecedence", 10),
          ("typeMplsExp", 3),
          ("typeQosLocalID", 8),
          ("typeTopMostVlanID", 11),
          ("typeVlan8021p", 4),
          ("typeVlanID", 7))
    )



class WredType(Integer32, TextualConvention):
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
        *(("typeAtmClpBased", 4),
          ("typeDropLevelBased", 3),
          ("typeDscpBased", 2),
          ("typeIpPrecBased", 1),
          ("typeMplsExpBased", 6),
          ("typeVlan8021pBased", 5))
    )



class QueueType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("af", 2),
          ("ef", 1),
          ("wfq", 3))
    )



class QueueBandwidthUnit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unitAbsolute", 1),
          ("unitPercent", 2),
          ("unitUnavailable", 0))
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



class ApplyObjectType(Integer32, TextualConvention):
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
        *(("atmPvc", 3),
          ("frDlci", 4),
          ("interface", 1),
          ("vlan", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cQos2_ObjectIdentity = ObjectIdentity
h3cQos2 = _H3cQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65)
)
_H3cCBQoSObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSObjects = _H3cCBQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1)
)
_H3cCBQoSClassifierObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSClassifierObjects = _H3cCBQoSClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1)
)
_H3cCBQoSClassifierIndexNext_Type = Integer32
_H3cCBQoSClassifierIndexNext_Object = MibScalar
h3cCBQoSClassifierIndexNext = _H3cCBQoSClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 1),
    _H3cCBQoSClassifierIndexNext_Type()
)
h3cCBQoSClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierIndexNext.setStatus("current")
_H3cCBQoSClassifierCfgInfoTable_Object = MibTable
h3cCBQoSClassifierCfgInfoTable = _H3cCBQoSClassifierCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSClassifierCfgInfoTable.setStatus("current")
_H3cCBQoSClassifierCfgInfoEntry_Object = MibTableRow
h3cCBQoSClassifierCfgInfoEntry = _H3cCBQoSClassifierCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1)
)
h3cCBQoSClassifierCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSClassifierIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSClassifierCfgInfoEntry.setStatus("current")
_H3cCBQoSClassifierIndex_Type = Integer32
_H3cCBQoSClassifierIndex_Object = MibTableColumn
h3cCBQoSClassifierIndex = _H3cCBQoSClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 1),
    _H3cCBQoSClassifierIndex_Type()
)
h3cCBQoSClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierIndex.setStatus("current")


class _H3cCBQoSClassifierName_Type(OctetString):
    """Custom type h3cCBQoSClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSClassifierName_Type.__name__ = "OctetString"
_H3cCBQoSClassifierName_Object = MibTableColumn
h3cCBQoSClassifierName = _H3cCBQoSClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 2),
    _H3cCBQoSClassifierName_Type()
)
h3cCBQoSClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierName.setStatus("current")
_H3cCBQoSClassifierRuleCount_Type = Integer32
_H3cCBQoSClassifierRuleCount_Object = MibTableColumn
h3cCBQoSClassifierRuleCount = _H3cCBQoSClassifierRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 3),
    _H3cCBQoSClassifierRuleCount_Type()
)
h3cCBQoSClassifierRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierRuleCount.setStatus("current")


class _H3cCBQoSClassifierOperator_Type(Integer32):
    """Custom type h3cCBQoSClassifierOperator based on Integer32"""
    defaultValue = 1

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


_H3cCBQoSClassifierOperator_Type.__name__ = "Integer32"
_H3cCBQoSClassifierOperator_Object = MibTableColumn
h3cCBQoSClassifierOperator = _H3cCBQoSClassifierOperator_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 4),
    _H3cCBQoSClassifierOperator_Type()
)
h3cCBQoSClassifierOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierOperator.setStatus("current")


class _H3cCBQoSClassifierLayer_Type(Integer32):
    """Custom type h3cCBQoSClassifierLayer based on Integer32"""
    defaultValue = 3

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
        *(("both", 4),
          ("l2", 2),
          ("l3", 3),
          ("unavailable", 1))
    )


_H3cCBQoSClassifierLayer_Type.__name__ = "Integer32"
_H3cCBQoSClassifierLayer_Object = MibTableColumn
h3cCBQoSClassifierLayer = _H3cCBQoSClassifierLayer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 5),
    _H3cCBQoSClassifierLayer_Type()
)
h3cCBQoSClassifierLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierLayer.setStatus("current")


class _H3cCBQoSClassifierType_Type(Integer32):
    """Custom type h3cCBQoSClassifierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemDefined", 1),
          ("userDefined", 2))
    )


_H3cCBQoSClassifierType_Type.__name__ = "Integer32"
_H3cCBQoSClassifierType_Object = MibTableColumn
h3cCBQoSClassifierType = _H3cCBQoSClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 6),
    _H3cCBQoSClassifierType_Type()
)
h3cCBQoSClassifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierType.setStatus("current")
_H3cCBQosClassifierMatchRuleNextIndex_Type = Integer32
_H3cCBQosClassifierMatchRuleNextIndex_Object = MibTableColumn
h3cCBQosClassifierMatchRuleNextIndex = _H3cCBQosClassifierMatchRuleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 7),
    _H3cCBQosClassifierMatchRuleNextIndex_Type()
)
h3cCBQosClassifierMatchRuleNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQosClassifierMatchRuleNextIndex.setStatus("current")
_H3cCBQoSClassifierRowStatus_Type = RowStatus
_H3cCBQoSClassifierRowStatus_Object = MibTableColumn
h3cCBQoSClassifierRowStatus = _H3cCBQoSClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 2, 1, 8),
    _H3cCBQoSClassifierRowStatus_Type()
)
h3cCBQoSClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSClassifierRowStatus.setStatus("current")
_H3cCBQoSMatchRuleCfgInfoTable_Object = MibTable
h3cCBQoSMatchRuleCfgInfoTable = _H3cCBQoSMatchRuleCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleCfgInfoTable.setStatus("current")
_H3cCBQoSMatchRuleCfgInfoEntry_Object = MibTableRow
h3cCBQoSMatchRuleCfgInfoEntry = _H3cCBQoSMatchRuleCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1)
)
h3cCBQoSMatchRuleCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSClassifierIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSMatchRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleCfgInfoEntry.setStatus("current")
_H3cCBQoSMatchRuleIndex_Type = Integer32
_H3cCBQoSMatchRuleIndex_Object = MibTableColumn
h3cCBQoSMatchRuleIndex = _H3cCBQoSMatchRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 1),
    _H3cCBQoSMatchRuleIndex_Type()
)
h3cCBQoSMatchRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleIndex.setStatus("current")


class _H3cCBQoSMatchRuleIfNot_Type(Integer32):
    """Custom type h3cCBQoSMatchRuleIfNot based on Integer32"""
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
          ("matchNot", 2))
    )


_H3cCBQoSMatchRuleIfNot_Type.__name__ = "Integer32"
_H3cCBQoSMatchRuleIfNot_Object = MibTableColumn
h3cCBQoSMatchRuleIfNot = _H3cCBQoSMatchRuleIfNot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 2),
    _H3cCBQoSMatchRuleIfNot_Type()
)
h3cCBQoSMatchRuleIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleIfNot.setStatus("current")
_H3cCBQoSMatchRuleType_Type = MatchRuleType
_H3cCBQoSMatchRuleType_Object = MibTableColumn
h3cCBQoSMatchRuleType = _H3cCBQoSMatchRuleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 3),
    _H3cCBQoSMatchRuleType_Type()
)
h3cCBQoSMatchRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleType.setStatus("current")


class _H3cCBQoSMatchRuleStringValue_Type(OctetString):
    """Custom type h3cCBQoSMatchRuleStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cCBQoSMatchRuleStringValue_Type.__name__ = "OctetString"
_H3cCBQoSMatchRuleStringValue_Object = MibTableColumn
h3cCBQoSMatchRuleStringValue = _H3cCBQoSMatchRuleStringValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 4),
    _H3cCBQoSMatchRuleStringValue_Type()
)
h3cCBQoSMatchRuleStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleStringValue.setStatus("current")
_H3cCBQoSMatchRuleIntValue1_Type = Unsigned32
_H3cCBQoSMatchRuleIntValue1_Object = MibTableColumn
h3cCBQoSMatchRuleIntValue1 = _H3cCBQoSMatchRuleIntValue1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 5),
    _H3cCBQoSMatchRuleIntValue1_Type()
)
h3cCBQoSMatchRuleIntValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleIntValue1.setStatus("current")
_H3cCBQoSMatchRuleIntValue2_Type = Unsigned32
_H3cCBQoSMatchRuleIntValue2_Object = MibTableColumn
h3cCBQoSMatchRuleIntValue2 = _H3cCBQoSMatchRuleIntValue2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 6),
    _H3cCBQoSMatchRuleIntValue2_Type()
)
h3cCBQoSMatchRuleIntValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleIntValue2.setStatus("current")
_H3cCBQoSMatchIpAddressType_Type = InetAddressType
_H3cCBQoSMatchIpAddressType_Object = MibTableColumn
h3cCBQoSMatchIpAddressType = _H3cCBQoSMatchIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 7),
    _H3cCBQoSMatchIpAddressType_Type()
)
h3cCBQoSMatchIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchIpAddressType.setStatus("current")
_H3cCBQoSMatchIpAddress_Type = InetAddress
_H3cCBQoSMatchIpAddress_Object = MibTableColumn
h3cCBQoSMatchIpAddress = _H3cCBQoSMatchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 8),
    _H3cCBQoSMatchIpAddress_Type()
)
h3cCBQoSMatchIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchIpAddress.setStatus("current")
_H3cCBQoSMatchRuleRowStatus_Type = RowStatus
_H3cCBQoSMatchRuleRowStatus_Object = MibTableColumn
h3cCBQoSMatchRuleRowStatus = _H3cCBQoSMatchRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 1, 3, 1, 9),
    _H3cCBQoSMatchRuleRowStatus_Type()
)
h3cCBQoSMatchRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMatchRuleRowStatus.setStatus("current")
_H3cCBQoSBehaviorObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSBehaviorObjects = _H3cCBQoSBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2)
)
_H3cCBQoSBehaviorIndexNext_Type = Integer32
_H3cCBQoSBehaviorIndexNext_Object = MibScalar
h3cCBQoSBehaviorIndexNext = _H3cCBQoSBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 1),
    _H3cCBQoSBehaviorIndexNext_Type()
)
h3cCBQoSBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorIndexNext.setStatus("current")
_H3cCBQoSBehaviorCfgInfoTable_Object = MibTable
h3cCBQoSBehaviorCfgInfoTable = _H3cCBQoSBehaviorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorCfgInfoTable.setStatus("current")
_H3cCBQoSBehaviorCfgInfoEntry_Object = MibTableRow
h3cCBQoSBehaviorCfgInfoEntry = _H3cCBQoSBehaviorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 2, 1)
)
h3cCBQoSBehaviorCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorCfgInfoEntry.setStatus("current")
_H3cCBQoSBehaviorIndex_Type = Integer32
_H3cCBQoSBehaviorIndex_Object = MibTableColumn
h3cCBQoSBehaviorIndex = _H3cCBQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 2, 1, 1),
    _H3cCBQoSBehaviorIndex_Type()
)
h3cCBQoSBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorIndex.setStatus("current")


class _H3cCBQoSBehaviorName_Type(OctetString):
    """Custom type h3cCBQoSBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSBehaviorName_Type.__name__ = "OctetString"
_H3cCBQoSBehaviorName_Object = MibTableColumn
h3cCBQoSBehaviorName = _H3cCBQoSBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 2, 1, 2),
    _H3cCBQoSBehaviorName_Type()
)
h3cCBQoSBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorName.setStatus("current")


class _H3cCBQoSBehaviorType_Type(Integer32):
    """Custom type h3cCBQoSBehaviorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemDefined", 1),
          ("userDefined", 2))
    )


_H3cCBQoSBehaviorType_Type.__name__ = "Integer32"
_H3cCBQoSBehaviorType_Object = MibTableColumn
h3cCBQoSBehaviorType = _H3cCBQoSBehaviorType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 2, 1, 3),
    _H3cCBQoSBehaviorType_Type()
)
h3cCBQoSBehaviorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorType.setStatus("current")
_H3cCBQoSBehaviorRowStatus_Type = RowStatus
_H3cCBQoSBehaviorRowStatus_Object = MibTableColumn
h3cCBQoSBehaviorRowStatus = _H3cCBQoSBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 2, 1, 4),
    _H3cCBQoSBehaviorRowStatus_Type()
)
h3cCBQoSBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSBehaviorRowStatus.setStatus("current")
_H3cCBQoSCarCfgInfoTable_Object = MibTable
h3cCBQoSCarCfgInfoTable = _H3cCBQoSCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSCarCfgInfoTable.setStatus("current")
_H3cCBQoSCarCfgInfoEntry_Object = MibTableRow
h3cCBQoSCarCfgInfoEntry = _H3cCBQoSCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1)
)
h3cCBQoSCarCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSCarCfgInfoEntry.setStatus("current")
_H3cCBQoSCarCir_Type = Unsigned32
_H3cCBQoSCarCir_Object = MibTableColumn
h3cCBQoSCarCir = _H3cCBQoSCarCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 1),
    _H3cCBQoSCarCir_Type()
)
h3cCBQoSCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarCir.setStatus("current")
_H3cCBQoSCarCbs_Type = Unsigned32
_H3cCBQoSCarCbs_Object = MibTableColumn
h3cCBQoSCarCbs = _H3cCBQoSCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 2),
    _H3cCBQoSCarCbs_Type()
)
h3cCBQoSCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarCbs.setStatus("current")


class _H3cCBQoSCarEbs_Type(Unsigned32):
    """Custom type h3cCBQoSCarEbs based on Unsigned32"""
    defaultValue = 0


_H3cCBQoSCarEbs_Object = MibTableColumn
h3cCBQoSCarEbs = _H3cCBQoSCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 3),
    _H3cCBQoSCarEbs_Type()
)
h3cCBQoSCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarEbs.setStatus("current")
_H3cCBQoSCarPir_Type = Unsigned32
_H3cCBQoSCarPir_Object = MibTableColumn
h3cCBQoSCarPir = _H3cCBQoSCarPir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 4),
    _H3cCBQoSCarPir_Type()
)
h3cCBQoSCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarPir.setStatus("current")
_H3cCBQoSCarPbs_Type = Unsigned32
_H3cCBQoSCarPbs_Object = MibTableColumn
h3cCBQoSCarPbs = _H3cCBQoSCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 5),
    _H3cCBQoSCarPbs_Type()
)
h3cCBQoSCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarPbs.setStatus("current")


class _H3cCBQoSCarGreenAction_Type(CarAction):
    """Custom type h3cCBQoSCarGreenAction based on CarAction"""


_H3cCBQoSCarGreenAction_Object = MibTableColumn
h3cCBQoSCarGreenAction = _H3cCBQoSCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 6),
    _H3cCBQoSCarGreenAction_Type()
)
h3cCBQoSCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarGreenAction.setStatus("current")


class _H3cCBQoSCarGreenRemarkValue_Type(Integer32):
    """Custom type h3cCBQoSCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cCBQoSCarGreenRemarkValue_Type.__name__ = "Integer32"
_H3cCBQoSCarGreenRemarkValue_Object = MibTableColumn
h3cCBQoSCarGreenRemarkValue = _H3cCBQoSCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 7),
    _H3cCBQoSCarGreenRemarkValue_Type()
)
h3cCBQoSCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarGreenRemarkValue.setStatus("current")


class _H3cCBQoSCarYellowAction_Type(CarAction):
    """Custom type h3cCBQoSCarYellowAction based on CarAction"""


_H3cCBQoSCarYellowAction_Object = MibTableColumn
h3cCBQoSCarYellowAction = _H3cCBQoSCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 8),
    _H3cCBQoSCarYellowAction_Type()
)
h3cCBQoSCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarYellowAction.setStatus("current")


class _H3cCBQoSCarYellowRemarkValue_Type(Integer32):
    """Custom type h3cCBQoSCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cCBQoSCarYellowRemarkValue_Type.__name__ = "Integer32"
_H3cCBQoSCarYellowRemarkValue_Object = MibTableColumn
h3cCBQoSCarYellowRemarkValue = _H3cCBQoSCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 9),
    _H3cCBQoSCarYellowRemarkValue_Type()
)
h3cCBQoSCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarYellowRemarkValue.setStatus("current")


class _H3cCBQoSCarRedAction_Type(CarAction):
    """Custom type h3cCBQoSCarRedAction based on CarAction"""


_H3cCBQoSCarRedAction_Object = MibTableColumn
h3cCBQoSCarRedAction = _H3cCBQoSCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 10),
    _H3cCBQoSCarRedAction_Type()
)
h3cCBQoSCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarRedAction.setStatus("current")


class _H3cCBQoSCarRedRemarkValue_Type(Integer32):
    """Custom type h3cCBQoSCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cCBQoSCarRedRemarkValue_Type.__name__ = "Integer32"
_H3cCBQoSCarRedRemarkValue_Object = MibTableColumn
h3cCBQoSCarRedRemarkValue = _H3cCBQoSCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 11),
    _H3cCBQoSCarRedRemarkValue_Type()
)
h3cCBQoSCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarRedRemarkValue.setStatus("current")


class _H3cCBQoSCarPolicedPriorityMapType_Type(Integer32):
    """Custom type h3cCBQoSCarPolicedPriorityMapType based on Integer32"""
    defaultValue = 0

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
        *(("drop-precedence-map", 3),
          ("local-precedence-dot1p-map", 2),
          ("none", 0),
          ("policed-service-map", 1))
    )


_H3cCBQoSCarPolicedPriorityMapType_Type.__name__ = "Integer32"
_H3cCBQoSCarPolicedPriorityMapType_Object = MibTableColumn
h3cCBQoSCarPolicedPriorityMapType = _H3cCBQoSCarPolicedPriorityMapType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 12),
    _H3cCBQoSCarPolicedPriorityMapType_Type()
)
h3cCBQoSCarPolicedPriorityMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarPolicedPriorityMapType.setStatus("current")
_H3cCBQoSCarRowStatus_Type = RowStatus
_H3cCBQoSCarRowStatus_Object = MibTableColumn
h3cCBQoSCarRowStatus = _H3cCBQoSCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 3, 1, 13),
    _H3cCBQoSCarRowStatus_Type()
)
h3cCBQoSCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSCarRowStatus.setStatus("current")
_H3cCBQoSAggregativeCarCfgInfoTable_Object = MibTable
h3cCBQoSAggregativeCarCfgInfoTable = _H3cCBQoSAggregativeCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSAggregativeCarCfgInfoTable.setStatus("current")
_H3cCBQoSAggregativeCarCfgInfoEntry_Object = MibTableRow
h3cCBQoSAggregativeCarCfgInfoEntry = _H3cCBQoSAggregativeCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 4, 1)
)
h3cCBQoSAggregativeCarCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSCarAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAggregativeCarCfgInfoEntry.setStatus("current")
_H3cCBQoSCarAggregativeCarIndex_Type = Integer32
_H3cCBQoSCarAggregativeCarIndex_Object = MibTableColumn
h3cCBQoSCarAggregativeCarIndex = _H3cCBQoSCarAggregativeCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 4, 1, 1),
    _H3cCBQoSCarAggregativeCarIndex_Type()
)
h3cCBQoSCarAggregativeCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSCarAggregativeCarIndex.setStatus("current")


class _H3cCBQoSCarAggregativeCarName_Type(OctetString):
    """Custom type h3cCBQoSCarAggregativeCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSCarAggregativeCarName_Type.__name__ = "OctetString"
_H3cCBQoSCarAggregativeCarName_Object = MibTableColumn
h3cCBQoSCarAggregativeCarName = _H3cCBQoSCarAggregativeCarName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 4, 1, 2),
    _H3cCBQoSCarAggregativeCarName_Type()
)
h3cCBQoSCarAggregativeCarName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarAggregativeCarName.setStatus("current")
_H3cCBQoSAggregativeCarRowStatus_Type = RowStatus
_H3cCBQoSAggregativeCarRowStatus_Object = MibTableColumn
h3cCBQoSAggregativeCarRowStatus = _H3cCBQoSAggregativeCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 4, 1, 3),
    _H3cCBQoSAggregativeCarRowStatus_Type()
)
h3cCBQoSAggregativeCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSAggregativeCarRowStatus.setStatus("current")
_H3cCBQoSGtsCfgInfoTable_Object = MibTable
h3cCBQoSGtsCfgInfoTable = _H3cCBQoSGtsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSGtsCfgInfoTable.setStatus("current")
_H3cCBQoSGtsCfgInfoEntry_Object = MibTableRow
h3cCBQoSGtsCfgInfoEntry = _H3cCBQoSGtsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5, 1)
)
h3cCBQoSGtsCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSGtsCfgInfoEntry.setStatus("current")
_H3cCBQoSGtsCir_Type = Unsigned32
_H3cCBQoSGtsCir_Object = MibTableColumn
h3cCBQoSGtsCir = _H3cCBQoSGtsCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5, 1, 1),
    _H3cCBQoSGtsCir_Type()
)
h3cCBQoSGtsCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGtsCir.setStatus("current")
_H3cCBQoSGtsCbs_Type = Unsigned32
_H3cCBQoSGtsCbs_Object = MibTableColumn
h3cCBQoSGtsCbs = _H3cCBQoSGtsCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5, 1, 2),
    _H3cCBQoSGtsCbs_Type()
)
h3cCBQoSGtsCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGtsCbs.setStatus("current")
_H3cCBQoSGtsEbs_Type = Unsigned32
_H3cCBQoSGtsEbs_Object = MibTableColumn
h3cCBQoSGtsEbs = _H3cCBQoSGtsEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5, 1, 3),
    _H3cCBQoSGtsEbs_Type()
)
h3cCBQoSGtsEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGtsEbs.setStatus("current")


class _H3cCBQoSGtsQueueLength_Type(Integer32):
    """Custom type h3cCBQoSGtsQueueLength based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cCBQoSGtsQueueLength_Type.__name__ = "Integer32"
_H3cCBQoSGtsQueueLength_Object = MibTableColumn
h3cCBQoSGtsQueueLength = _H3cCBQoSGtsQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5, 1, 4),
    _H3cCBQoSGtsQueueLength_Type()
)
h3cCBQoSGtsQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGtsQueueLength.setStatus("current")
_H3cCBQoSGtsRowStatus_Type = RowStatus
_H3cCBQoSGtsRowStatus_Object = MibTableColumn
h3cCBQoSGtsRowStatus = _H3cCBQoSGtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 5, 1, 5),
    _H3cCBQoSGtsRowStatus_Type()
)
h3cCBQoSGtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGtsRowStatus.setStatus("current")
_H3cCBQoSRemarkCfgInfoTable_Object = MibTable
h3cCBQoSRemarkCfgInfoTable = _H3cCBQoSRemarkCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    h3cCBQoSRemarkCfgInfoTable.setStatus("current")
_H3cCBQoSRemarkCfgInfoEntry_Object = MibTableRow
h3cCBQoSRemarkCfgInfoEntry = _H3cCBQoSRemarkCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 6, 1)
)
h3cCBQoSRemarkCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSRemarkType"),
)
if mibBuilder.loadTexts:
    h3cCBQoSRemarkCfgInfoEntry.setStatus("current")
_H3cCBQoSRemarkType_Type = RemarkType
_H3cCBQoSRemarkType_Object = MibTableColumn
h3cCBQoSRemarkType = _H3cCBQoSRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 6, 1, 1),
    _H3cCBQoSRemarkType_Type()
)
h3cCBQoSRemarkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSRemarkType.setStatus("current")


class _H3cCBQoSRemarkValue_Type(Integer32):
    """Custom type h3cCBQoSRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_H3cCBQoSRemarkValue_Type.__name__ = "Integer32"
_H3cCBQoSRemarkValue_Object = MibTableColumn
h3cCBQoSRemarkValue = _H3cCBQoSRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 6, 1, 2),
    _H3cCBQoSRemarkValue_Type()
)
h3cCBQoSRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRemarkValue.setStatus("current")
_H3cCBQoSRemarkRowStatus_Type = RowStatus
_H3cCBQoSRemarkRowStatus_Object = MibTableColumn
h3cCBQoSRemarkRowStatus = _H3cCBQoSRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 6, 1, 3),
    _H3cCBQoSRemarkRowStatus_Type()
)
h3cCBQoSRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRemarkRowStatus.setStatus("current")
_H3cCBQoSQueueCfgInfoTable_Object = MibTable
h3cCBQoSQueueCfgInfoTable = _H3cCBQoSQueueCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    h3cCBQoSQueueCfgInfoTable.setStatus("current")
_H3cCBQoSQueueCfgInfoEntry_Object = MibTableRow
h3cCBQoSQueueCfgInfoEntry = _H3cCBQoSQueueCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1)
)
h3cCBQoSQueueCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSQueueCfgInfoEntry.setStatus("current")
_H3cCBQoSQueueType_Type = QueueType
_H3cCBQoSQueueType_Object = MibTableColumn
h3cCBQoSQueueType = _H3cCBQoSQueueType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 1),
    _H3cCBQoSQueueType_Type()
)
h3cCBQoSQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueType.setStatus("current")


class _H3cCBQoSQueueDropType_Type(Integer32):
    """Custom type h3cCBQoSQueueDropType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeTailDrop", 1),
          ("typeUnavailable", 0),
          ("typeWred", 2))
    )


_H3cCBQoSQueueDropType_Type.__name__ = "Integer32"
_H3cCBQoSQueueDropType_Object = MibTableColumn
h3cCBQoSQueueDropType = _H3cCBQoSQueueDropType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 2),
    _H3cCBQoSQueueDropType_Type()
)
h3cCBQoSQueueDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueDropType.setStatus("current")


class _H3cCBQoSQueueLength_Type(Integer32):
    """Custom type h3cCBQoSQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_H3cCBQoSQueueLength_Type.__name__ = "Integer32"
_H3cCBQoSQueueLength_Object = MibTableColumn
h3cCBQoSQueueLength = _H3cCBQoSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 3),
    _H3cCBQoSQueueLength_Type()
)
h3cCBQoSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueLength.setStatus("current")
_H3cCBQoSQueueBandwidthUnit_Type = QueueBandwidthUnit
_H3cCBQoSQueueBandwidthUnit_Object = MibTableColumn
h3cCBQoSQueueBandwidthUnit = _H3cCBQoSQueueBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 4),
    _H3cCBQoSQueueBandwidthUnit_Type()
)
h3cCBQoSQueueBandwidthUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueBandwidthUnit.setStatus("current")


class _H3cCBQoSQueueBandwidthValue_Type(Integer32):
    """Custom type h3cCBQoSQueueBandwidthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_H3cCBQoSQueueBandwidthValue_Type.__name__ = "Integer32"
_H3cCBQoSQueueBandwidthValue_Object = MibTableColumn
h3cCBQoSQueueBandwidthValue = _H3cCBQoSQueueBandwidthValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 5),
    _H3cCBQoSQueueBandwidthValue_Type()
)
h3cCBQoSQueueBandwidthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueBandwidthValue.setStatus("current")


class _H3cCBQoSQueueCbs_Type(Integer32):
    """Custom type h3cCBQoSQueueCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1000000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_H3cCBQoSQueueCbs_Type.__name__ = "Integer32"
_H3cCBQoSQueueCbs_Object = MibTableColumn
h3cCBQoSQueueCbs = _H3cCBQoSQueueCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 6),
    _H3cCBQoSQueueCbs_Type()
)
h3cCBQoSQueueCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueCbs.setStatus("current")


class _H3cCBQoSQueueQueueNumber_Type(Integer32):
    """Custom type h3cCBQoSQueueQueueNumber based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("a1024", 1024),
          ("a128", 128),
          ("a16", 16),
          ("a2048", 2048),
          ("a256", 256),
          ("a32", 32),
          ("a4096", 4096),
          ("a512", 512),
          ("a64", 64),
          ("unavailable", 0))
    )


_H3cCBQoSQueueQueueNumber_Type.__name__ = "Integer32"
_H3cCBQoSQueueQueueNumber_Object = MibTableColumn
h3cCBQoSQueueQueueNumber = _H3cCBQoSQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 7),
    _H3cCBQoSQueueQueueNumber_Type()
)
h3cCBQoSQueueQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueQueueNumber.setStatus("current")


class _H3cCBQoSQueueCbsRatio_Type(Integer32):
    """Custom type h3cCBQoSQueueCbsRatio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_H3cCBQoSQueueCbsRatio_Type.__name__ = "Integer32"
_H3cCBQoSQueueCbsRatio_Object = MibTableColumn
h3cCBQoSQueueCbsRatio = _H3cCBQoSQueueCbsRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 8),
    _H3cCBQoSQueueCbsRatio_Type()
)
h3cCBQoSQueueCbsRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueCbsRatio.setStatus("current")
_H3cCBQoSQueueRowStatus_Type = RowStatus
_H3cCBQoSQueueRowStatus_Object = MibTableColumn
h3cCBQoSQueueRowStatus = _H3cCBQoSQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 7, 1, 9),
    _H3cCBQoSQueueRowStatus_Type()
)
h3cCBQoSQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSQueueRowStatus.setStatus("current")
_H3cCBQoSWredCfgInfoTable_Object = MibTable
h3cCBQoSWredCfgInfoTable = _H3cCBQoSWredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    h3cCBQoSWredCfgInfoTable.setStatus("current")
_H3cCBQoSWredCfgInfoEntry_Object = MibTableRow
h3cCBQoSWredCfgInfoEntry = _H3cCBQoSWredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 8, 1)
)
h3cCBQoSWredCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSWredCfgInfoEntry.setStatus("current")


class _H3cCBQoSWredType_Type(WredType):
    """Custom type h3cCBQoSWredType based on WredType"""
    defaultValue = 1


_H3cCBQoSWredType_Object = MibTableColumn
h3cCBQoSWredType = _H3cCBQoSWredType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 8, 1, 1),
    _H3cCBQoSWredType_Type()
)
h3cCBQoSWredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCBQoSWredType.setStatus("current")


class _H3cCBQoSWredWeightConst_Type(Integer32):
    """Custom type h3cCBQoSWredWeightConst based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cCBQoSWredWeightConst_Type.__name__ = "Integer32"
_H3cCBQoSWredWeightConst_Object = MibTableColumn
h3cCBQoSWredWeightConst = _H3cCBQoSWredWeightConst_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 8, 1, 2),
    _H3cCBQoSWredWeightConst_Type()
)
h3cCBQoSWredWeightConst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCBQoSWredWeightConst.setStatus("current")
_H3cCBQoSWredClassCfgInfoTable_Object = MibTable
h3cCBQoSWredClassCfgInfoTable = _H3cCBQoSWredClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    h3cCBQoSWredClassCfgInfoTable.setStatus("current")
_H3cCBQoSWredClassCfgInfoEntry_Object = MibTableRow
h3cCBQoSWredClassCfgInfoEntry = _H3cCBQoSWredClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 9, 1)
)
h3cCBQoSWredClassCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSWredClassCfgInfoEntry.setStatus("current")


class _H3cCBQoSWredClassValue_Type(Integer32):
    """Custom type h3cCBQoSWredClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cCBQoSWredClassValue_Type.__name__ = "Integer32"
_H3cCBQoSWredClassValue_Object = MibTableColumn
h3cCBQoSWredClassValue = _H3cCBQoSWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 9, 1, 1),
    _H3cCBQoSWredClassValue_Type()
)
h3cCBQoSWredClassValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSWredClassValue.setStatus("current")


class _H3cCBQoSWredClassLowLimit_Type(Integer32):
    """Custom type h3cCBQoSWredClassLowLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cCBQoSWredClassLowLimit_Type.__name__ = "Integer32"
_H3cCBQoSWredClassLowLimit_Object = MibTableColumn
h3cCBQoSWredClassLowLimit = _H3cCBQoSWredClassLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 9, 1, 2),
    _H3cCBQoSWredClassLowLimit_Type()
)
h3cCBQoSWredClassLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCBQoSWredClassLowLimit.setStatus("current")


class _H3cCBQoSWredClassHighLimit_Type(Integer32):
    """Custom type h3cCBQoSWredClassHighLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cCBQoSWredClassHighLimit_Type.__name__ = "Integer32"
_H3cCBQoSWredClassHighLimit_Object = MibTableColumn
h3cCBQoSWredClassHighLimit = _H3cCBQoSWredClassHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 9, 1, 3),
    _H3cCBQoSWredClassHighLimit_Type()
)
h3cCBQoSWredClassHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCBQoSWredClassHighLimit.setStatus("current")


class _H3cCBQoSWredClassDiscardProb_Type(Integer32):
    """Custom type h3cCBQoSWredClassDiscardProb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cCBQoSWredClassDiscardProb_Type.__name__ = "Integer32"
_H3cCBQoSWredClassDiscardProb_Object = MibTableColumn
h3cCBQoSWredClassDiscardProb = _H3cCBQoSWredClassDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 9, 1, 4),
    _H3cCBQoSWredClassDiscardProb_Type()
)
h3cCBQoSWredClassDiscardProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCBQoSWredClassDiscardProb.setStatus("current")
_H3cCBQoSPolicyRouteCfgInfoTable_Object = MibTable
h3cCBQoSPolicyRouteCfgInfoTable = _H3cCBQoSPolicyRouteCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRouteCfgInfoTable.setStatus("current")
_H3cCBQoSPolicyRouteCfgInfoEntry_Object = MibTableRow
h3cCBQoSPolicyRouteCfgInfoEntry = _H3cCBQoSPolicyRouteCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 10, 1)
)
h3cCBQoSPolicyRouteCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRouteCfgInfoEntry.setStatus("current")
_H3cCBQoSPolicyRouteIpAddrType_Type = InetAddressType
_H3cCBQoSPolicyRouteIpAddrType_Object = MibTableColumn
h3cCBQoSPolicyRouteIpAddrType = _H3cCBQoSPolicyRouteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 10, 1, 1),
    _H3cCBQoSPolicyRouteIpAddrType_Type()
)
h3cCBQoSPolicyRouteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRouteIpAddrType.setStatus("current")
_H3cCBQoSPolicyRouteNexthop_Type = InetAddress
_H3cCBQoSPolicyRouteNexthop_Object = MibTableColumn
h3cCBQoSPolicyRouteNexthop = _H3cCBQoSPolicyRouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 10, 1, 2),
    _H3cCBQoSPolicyRouteNexthop_Type()
)
h3cCBQoSPolicyRouteNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRouteNexthop.setStatus("current")


class _H3cCBQoSPolicyRouteBackup_Type(Integer32):
    """Custom type h3cCBQoSPolicyRouteBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("notbackup", 2))
    )


_H3cCBQoSPolicyRouteBackup_Type.__name__ = "Integer32"
_H3cCBQoSPolicyRouteBackup_Object = MibTableColumn
h3cCBQoSPolicyRouteBackup = _H3cCBQoSPolicyRouteBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 10, 1, 3),
    _H3cCBQoSPolicyRouteBackup_Type()
)
h3cCBQoSPolicyRouteBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRouteBackup.setStatus("current")
_H3cCBQoSPolicyRouteRowStatus_Type = RowStatus
_H3cCBQoSPolicyRouteRowStatus_Object = MibTableColumn
h3cCBQoSPolicyRouteRowStatus = _H3cCBQoSPolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 10, 1, 4),
    _H3cCBQoSPolicyRouteRowStatus_Type()
)
h3cCBQoSPolicyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRouteRowStatus.setStatus("current")
_H3cCBQoSNatCfgInfoTable_Object = MibTable
h3cCBQoSNatCfgInfoTable = _H3cCBQoSNatCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    h3cCBQoSNatCfgInfoTable.setStatus("current")
_H3cCBQoSNatCfgInfoEntry_Object = MibTableRow
h3cCBQoSNatCfgInfoEntry = _H3cCBQoSNatCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 11, 1)
)
h3cCBQoSNatCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSNatCfgInfoEntry.setStatus("current")


class _H3cCBQoSNatMainNumber_Type(Integer32):
    """Custom type h3cCBQoSNatMainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cCBQoSNatMainNumber_Type.__name__ = "Integer32"
_H3cCBQoSNatMainNumber_Object = MibTableColumn
h3cCBQoSNatMainNumber = _H3cCBQoSNatMainNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 11, 1, 1),
    _H3cCBQoSNatMainNumber_Type()
)
h3cCBQoSNatMainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNatMainNumber.setStatus("current")


class _H3cCBQoSNatBackupNumber_Type(Integer32):
    """Custom type h3cCBQoSNatBackupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cCBQoSNatBackupNumber_Type.__name__ = "Integer32"
_H3cCBQoSNatBackupNumber_Object = MibTableColumn
h3cCBQoSNatBackupNumber = _H3cCBQoSNatBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 11, 1, 2),
    _H3cCBQoSNatBackupNumber_Type()
)
h3cCBQoSNatBackupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNatBackupNumber.setStatus("current")


class _H3cCBQoSNatServiceClass_Type(Integer32):
    """Custom type h3cCBQoSNatServiceClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_H3cCBQoSNatServiceClass_Type.__name__ = "Integer32"
_H3cCBQoSNatServiceClass_Object = MibTableColumn
h3cCBQoSNatServiceClass = _H3cCBQoSNatServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 11, 1, 3),
    _H3cCBQoSNatServiceClass_Type()
)
h3cCBQoSNatServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNatServiceClass.setStatus("current")
_H3cCBQoSNatRowStatus_Type = RowStatus
_H3cCBQoSNatRowStatus_Object = MibTableColumn
h3cCBQoSNatRowStatus = _H3cCBQoSNatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 11, 1, 4),
    _H3cCBQoSNatRowStatus_Type()
)
h3cCBQoSNatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNatRowStatus.setStatus("current")
_H3cCBQoSFirewallCfgInfoTable_Object = MibTable
h3cCBQoSFirewallCfgInfoTable = _H3cCBQoSFirewallCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    h3cCBQoSFirewallCfgInfoTable.setStatus("current")
_H3cCBQoSFirewallCfgInfoEntry_Object = MibTableRow
h3cCBQoSFirewallCfgInfoEntry = _H3cCBQoSFirewallCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 12, 1)
)
h3cCBQoSFirewallCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFirewallCfgInfoEntry.setStatus("current")


class _H3cCBQoSFirewallAction_Type(Integer32):
    """Custom type h3cCBQoSFirewallAction based on Integer32"""
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


_H3cCBQoSFirewallAction_Type.__name__ = "Integer32"
_H3cCBQoSFirewallAction_Object = MibTableColumn
h3cCBQoSFirewallAction = _H3cCBQoSFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 12, 1, 1),
    _H3cCBQoSFirewallAction_Type()
)
h3cCBQoSFirewallAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSFirewallAction.setStatus("current")
_H3cCBQoSFirewallRowStatus_Type = RowStatus
_H3cCBQoSFirewallRowStatus_Object = MibTableColumn
h3cCBQoSFirewallRowStatus = _H3cCBQoSFirewallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 12, 1, 2),
    _H3cCBQoSFirewallRowStatus_Type()
)
h3cCBQoSFirewallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSFirewallRowStatus.setStatus("current")
_H3cCBQoSSamplingCfgInfoTable_Object = MibTable
h3cCBQoSSamplingCfgInfoTable = _H3cCBQoSSamplingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    h3cCBQoSSamplingCfgInfoTable.setStatus("current")
_H3cCBQoSSamplingCfgInfoEntry_Object = MibTableRow
h3cCBQoSSamplingCfgInfoEntry = _H3cCBQoSSamplingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 13, 1)
)
h3cCBQoSSamplingCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSSamplingCfgInfoEntry.setStatus("current")


class _H3cCBQoSSamplingNum_Type(Integer32):
    """Custom type h3cCBQoSSamplingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cCBQoSSamplingNum_Type.__name__ = "Integer32"
_H3cCBQoSSamplingNum_Object = MibTableColumn
h3cCBQoSSamplingNum = _H3cCBQoSSamplingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 13, 1, 1),
    _H3cCBQoSSamplingNum_Type()
)
h3cCBQoSSamplingNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSSamplingNum.setStatus("current")
_H3cCBQoSSamplingRowStatus_Type = RowStatus
_H3cCBQoSSamplingRowStatus_Object = MibTableColumn
h3cCBQoSSamplingRowStatus = _H3cCBQoSSamplingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 13, 1, 2),
    _H3cCBQoSSamplingRowStatus_Type()
)
h3cCBQoSSamplingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSSamplingRowStatus.setStatus("current")
_H3cCBQoSAccountCfgInfoTable_Object = MibTable
h3cCBQoSAccountCfgInfoTable = _H3cCBQoSAccountCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    h3cCBQoSAccountCfgInfoTable.setStatus("current")
_H3cCBQoSAccountCfgInfoEntry_Object = MibTableRow
h3cCBQoSAccountCfgInfoEntry = _H3cCBQoSAccountCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 14, 1)
)
h3cCBQoSAccountCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAccountCfgInfoEntry.setStatus("current")
_H3cCBQoSAccounting_Type = TruthValue
_H3cCBQoSAccounting_Object = MibTableColumn
h3cCBQoSAccounting = _H3cCBQoSAccounting_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 14, 1, 1),
    _H3cCBQoSAccounting_Type()
)
h3cCBQoSAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSAccounting.setStatus("current")
_H3cCBQoSAccountRowStatus_Type = RowStatus
_H3cCBQoSAccountRowStatus_Object = MibTableColumn
h3cCBQoSAccountRowStatus = _H3cCBQoSAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 14, 1, 2),
    _H3cCBQoSAccountRowStatus_Type()
)
h3cCBQoSAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSAccountRowStatus.setStatus("current")
_H3cCBQoSRedirectCfgInfoTable_Object = MibTable
h3cCBQoSRedirectCfgInfoTable = _H3cCBQoSRedirectCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    h3cCBQoSRedirectCfgInfoTable.setStatus("current")
_H3cCBQoSRedirectCfgInfoEntry_Object = MibTableRow
h3cCBQoSRedirectCfgInfoEntry = _H3cCBQoSRedirectCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1)
)
h3cCBQoSRedirectCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSRedirectCfgInfoEntry.setStatus("current")


class _H3cCBQoSRedirectType_Type(Integer32):
    """Custom type h3cCBQoSRedirectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 1),
          ("interface", 2),
          ("nextHop", 3))
    )


_H3cCBQoSRedirectType_Type.__name__ = "Integer32"
_H3cCBQoSRedirectType_Object = MibTableColumn
h3cCBQoSRedirectType = _H3cCBQoSRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 1),
    _H3cCBQoSRedirectType_Type()
)
h3cCBQoSRedirectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectType.setStatus("current")


class _H3cCBQoSRedirectIfIndex_Type(Integer32):
    """Custom type h3cCBQoSRedirectIfIndex based on Integer32"""
    defaultValue = 0


_H3cCBQoSRedirectIfIndex_Object = MibTableColumn
h3cCBQoSRedirectIfIndex = _H3cCBQoSRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 2),
    _H3cCBQoSRedirectIfIndex_Type()
)
h3cCBQoSRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectIfIndex.setStatus("current")


class _H3cCBQoSRedirectIpAddressType_Type(InetAddressType):
    """Custom type h3cCBQoSRedirectIpAddressType based on InetAddressType"""


_H3cCBQoSRedirectIpAddressType_Object = MibTableColumn
h3cCBQoSRedirectIpAddressType = _H3cCBQoSRedirectIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 3),
    _H3cCBQoSRedirectIpAddressType_Type()
)
h3cCBQoSRedirectIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectIpAddressType.setStatus("current")
_H3cCBQoSRedirectIpAddress1_Type = InetAddress
_H3cCBQoSRedirectIpAddress1_Object = MibTableColumn
h3cCBQoSRedirectIpAddress1 = _H3cCBQoSRedirectIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 4),
    _H3cCBQoSRedirectIpAddress1_Type()
)
h3cCBQoSRedirectIpAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectIpAddress1.setStatus("current")
_H3cCBQoSRedirectIpAddress2_Type = InetAddress
_H3cCBQoSRedirectIpAddress2_Object = MibTableColumn
h3cCBQoSRedirectIpAddress2 = _H3cCBQoSRedirectIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 5),
    _H3cCBQoSRedirectIpAddress2_Type()
)
h3cCBQoSRedirectIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectIpAddress2.setStatus("current")
_H3cCBQoSRedirectRowStatus_Type = RowStatus
_H3cCBQoSRedirectRowStatus_Object = MibTableColumn
h3cCBQoSRedirectRowStatus = _H3cCBQoSRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 6),
    _H3cCBQoSRedirectRowStatus_Type()
)
h3cCBQoSRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectRowStatus.setStatus("current")


class _H3cCBQoSRedirectIpv6Interface1_Type(Integer32):
    """Custom type h3cCBQoSRedirectIpv6Interface1 based on Integer32"""
    defaultValue = 0


_H3cCBQoSRedirectIpv6Interface1_Object = MibTableColumn
h3cCBQoSRedirectIpv6Interface1 = _H3cCBQoSRedirectIpv6Interface1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 7),
    _H3cCBQoSRedirectIpv6Interface1_Type()
)
h3cCBQoSRedirectIpv6Interface1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectIpv6Interface1.setStatus("current")


class _H3cCBQoSRedirectIpv6Interface2_Type(Integer32):
    """Custom type h3cCBQoSRedirectIpv6Interface2 based on Integer32"""
    defaultValue = 0


_H3cCBQoSRedirectIpv6Interface2_Object = MibTableColumn
h3cCBQoSRedirectIpv6Interface2 = _H3cCBQoSRedirectIpv6Interface2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 15, 1, 8),
    _H3cCBQoSRedirectIpv6Interface2_Type()
)
h3cCBQoSRedirectIpv6Interface2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSRedirectIpv6Interface2.setStatus("current")
_H3cCBQoSPriorityMapCfgInfoTable_Object = MibTable
h3cCBQoSPriorityMapCfgInfoTable = _H3cCBQoSPriorityMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapCfgInfoTable.setStatus("current")
_H3cCBQoSPriorityMapCfgInfoEntry_Object = MibTableRow
h3cCBQoSPriorityMapCfgInfoEntry = _H3cCBQoSPriorityMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1)
)
h3cCBQoSPriorityMapCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapCfgInfoEntry.setStatus("current")


class _H3cCBQoSPriorityMapImportType_Type(Integer32):
    """Custom type h3cCBQoSPriorityMapImportType based on Integer32"""
    defaultValue = 1

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
        *(("dot1p", 3),
          ("dropPrecedence", 7),
          ("dscp", 2),
          ("exp", 4),
          ("invalid", 1),
          ("ipPrecedence", 5),
          ("localPrecedence", 6))
    )


_H3cCBQoSPriorityMapImportType_Type.__name__ = "Integer32"
_H3cCBQoSPriorityMapImportType_Object = MibTableColumn
h3cCBQoSPriorityMapImportType = _H3cCBQoSPriorityMapImportType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1, 1),
    _H3cCBQoSPriorityMapImportType_Type()
)
h3cCBQoSPriorityMapImportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapImportType.setStatus("current")


class _H3cCBQoSPriorityMapExportType_Type(Integer32):
    """Custom type h3cCBQoSPriorityMapExportType based on Integer32"""
    defaultValue = 1

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
        *(("dot1p", 3),
          ("dropPrecedence", 7),
          ("dscp", 2),
          ("exp", 4),
          ("invalid", 1),
          ("ipPrecedence", 5),
          ("localPrecedence", 6))
    )


_H3cCBQoSPriorityMapExportType_Type.__name__ = "Integer32"
_H3cCBQoSPriorityMapExportType_Object = MibTableColumn
h3cCBQoSPriorityMapExportType = _H3cCBQoSPriorityMapExportType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1, 2),
    _H3cCBQoSPriorityMapExportType_Type()
)
h3cCBQoSPriorityMapExportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapExportType.setStatus("current")
_H3cCBQoSPriorityMapGroupIndex_Type = Integer32
_H3cCBQoSPriorityMapGroupIndex_Object = MibTableColumn
h3cCBQoSPriorityMapGroupIndex = _H3cCBQoSPriorityMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1, 3),
    _H3cCBQoSPriorityMapGroupIndex_Type()
)
h3cCBQoSPriorityMapGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapGroupIndex.setStatus("current")


class _H3cCBQoSPriorityMapGroupName_Type(OctetString):
    """Custom type h3cCBQoSPriorityMapGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cCBQoSPriorityMapGroupName_Type.__name__ = "OctetString"
_H3cCBQoSPriorityMapGroupName_Object = MibTableColumn
h3cCBQoSPriorityMapGroupName = _H3cCBQoSPriorityMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1, 4),
    _H3cCBQoSPriorityMapGroupName_Type()
)
h3cCBQoSPriorityMapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapGroupName.setStatus("current")


class _H3cCBQoSPriorityMapAuto_Type(Integer32):
    """Custom type h3cCBQoSPriorityMapAuto based on Integer32"""
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
        *(("autoDot1p", 3),
          ("autoDscp", 2),
          ("autoIp", 5),
          ("autoMplsExp", 4),
          ("invalid", 1))
    )


_H3cCBQoSPriorityMapAuto_Type.__name__ = "Integer32"
_H3cCBQoSPriorityMapAuto_Object = MibTableColumn
h3cCBQoSPriorityMapAuto = _H3cCBQoSPriorityMapAuto_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1, 5),
    _H3cCBQoSPriorityMapAuto_Type()
)
h3cCBQoSPriorityMapAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapAuto.setStatus("current")
_H3cCBQoSPriorityMapRowStatus_Type = RowStatus
_H3cCBQoSPriorityMapRowStatus_Object = MibTableColumn
h3cCBQoSPriorityMapRowStatus = _H3cCBQoSPriorityMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 16, 1, 6),
    _H3cCBQoSPriorityMapRowStatus_Type()
)
h3cCBQoSPriorityMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPriorityMapRowStatus.setStatus("current")
_H3cCBQoSMirrorCfgInfoTable_Object = MibTable
h3cCBQoSMirrorCfgInfoTable = _H3cCBQoSMirrorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    h3cCBQoSMirrorCfgInfoTable.setStatus("current")
_H3cCBQoSMirrorCfgInfoEntry_Object = MibTableRow
h3cCBQoSMirrorCfgInfoEntry = _H3cCBQoSMirrorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 17, 1)
)
h3cCBQoSMirrorCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSMirrorCfgInfoEntry.setStatus("current")


class _H3cCBQoSMirrorType_Type(Integer32):
    """Custom type h3cCBQoSMirrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("interface", 1),
          ("vlan", 3))
    )


_H3cCBQoSMirrorType_Type.__name__ = "Integer32"
_H3cCBQoSMirrorType_Object = MibTableColumn
h3cCBQoSMirrorType = _H3cCBQoSMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 17, 1, 1),
    _H3cCBQoSMirrorType_Type()
)
h3cCBQoSMirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMirrorType.setStatus("current")


class _H3cCBQoSMirrorIfIndex_Type(OctetString):
    """Custom type h3cCBQoSMirrorIfIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cCBQoSMirrorIfIndex_Type.__name__ = "OctetString"
_H3cCBQoSMirrorIfIndex_Object = MibTableColumn
h3cCBQoSMirrorIfIndex = _H3cCBQoSMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 17, 1, 2),
    _H3cCBQoSMirrorIfIndex_Type()
)
h3cCBQoSMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMirrorIfIndex.setStatus("current")


class _H3cCBQoSMirrorVlanID_Type(Integer32):
    """Custom type h3cCBQoSMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cCBQoSMirrorVlanID_Type.__name__ = "Integer32"
_H3cCBQoSMirrorVlanID_Object = MibTableColumn
h3cCBQoSMirrorVlanID = _H3cCBQoSMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 17, 1, 3),
    _H3cCBQoSMirrorVlanID_Type()
)
h3cCBQoSMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMirrorVlanID.setStatus("current")
_H3cCBQoSMirrorRowStatus_Type = RowStatus
_H3cCBQoSMirrorRowStatus_Object = MibTableColumn
h3cCBQoSMirrorRowStatus = _H3cCBQoSMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 17, 1, 4),
    _H3cCBQoSMirrorRowStatus_Type()
)
h3cCBQoSMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSMirrorRowStatus.setStatus("current")
_H3cCBQoSNestCfgInfoTable_Object = MibTable
h3cCBQoSNestCfgInfoTable = _H3cCBQoSNestCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18)
)
if mibBuilder.loadTexts:
    h3cCBQoSNestCfgInfoTable.setStatus("current")
_H3cCBQoSNestCfgInfoEntry_Object = MibTableRow
h3cCBQoSNestCfgInfoEntry = _H3cCBQoSNestCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18, 1)
)
h3cCBQoSNestCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSNestCfgInfoEntry.setStatus("current")


class _H3cCBQoSNestServiceVlanID_Type(Integer32):
    """Custom type h3cCBQoSNestServiceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_H3cCBQoSNestServiceVlanID_Type.__name__ = "Integer32"
_H3cCBQoSNestServiceVlanID_Object = MibTableColumn
h3cCBQoSNestServiceVlanID = _H3cCBQoSNestServiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18, 1, 1),
    _H3cCBQoSNestServiceVlanID_Type()
)
h3cCBQoSNestServiceVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestServiceVlanID.setStatus("current")


class _H3cCBQoSNestServiceDot1pValue_Type(Integer32):
    """Custom type h3cCBQoSNestServiceDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_H3cCBQoSNestServiceDot1pValue_Type.__name__ = "Integer32"
_H3cCBQoSNestServiceDot1pValue_Object = MibTableColumn
h3cCBQoSNestServiceDot1pValue = _H3cCBQoSNestServiceDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18, 1, 2),
    _H3cCBQoSNestServiceDot1pValue_Type()
)
h3cCBQoSNestServiceDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestServiceDot1pValue.setStatus("current")


class _H3cCBQoSNestCustomerVlanID_Type(Integer32):
    """Custom type h3cCBQoSNestCustomerVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_H3cCBQoSNestCustomerVlanID_Type.__name__ = "Integer32"
_H3cCBQoSNestCustomerVlanID_Object = MibTableColumn
h3cCBQoSNestCustomerVlanID = _H3cCBQoSNestCustomerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18, 1, 3),
    _H3cCBQoSNestCustomerVlanID_Type()
)
h3cCBQoSNestCustomerVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestCustomerVlanID.setStatus("current")


class _H3cCBQoSNestCustomerDot1pValue_Type(Integer32):
    """Custom type h3cCBQoSNestCustomerDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_H3cCBQoSNestCustomerDot1pValue_Type.__name__ = "Integer32"
_H3cCBQoSNestCustomerDot1pValue_Object = MibTableColumn
h3cCBQoSNestCustomerDot1pValue = _H3cCBQoSNestCustomerDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18, 1, 4),
    _H3cCBQoSNestCustomerDot1pValue_Type()
)
h3cCBQoSNestCustomerDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestCustomerDot1pValue.setStatus("current")
_H3cCBQoSNestRowStatus_Type = RowStatus
_H3cCBQoSNestRowStatus_Object = MibTableColumn
h3cCBQoSNestRowStatus = _H3cCBQoSNestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 18, 1, 5),
    _H3cCBQoSNestRowStatus_Type()
)
h3cCBQoSNestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestRowStatus.setStatus("current")
_H3cCBQoSNestPolicyCfgInfoTable_Object = MibTable
h3cCBQoSNestPolicyCfgInfoTable = _H3cCBQoSNestPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 19)
)
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyCfgInfoTable.setStatus("current")
_H3cCBQoSNestPolicyCfgInfoEntry_Object = MibTableRow
h3cCBQoSNestPolicyCfgInfoEntry = _H3cCBQoSNestPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 19, 1)
)
h3cCBQoSNestPolicyCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyCfgInfoEntry.setStatus("current")


class _H3cCBQoSNestPolicyName_Type(OctetString):
    """Custom type h3cCBQoSNestPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSNestPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSNestPolicyName_Object = MibTableColumn
h3cCBQoSNestPolicyName = _H3cCBQoSNestPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 19, 1, 1),
    _H3cCBQoSNestPolicyName_Type()
)
h3cCBQoSNestPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyName.setStatus("current")
_H3cCBQoSNestPolicyRowStatus_Type = RowStatus
_H3cCBQoSNestPolicyRowStatus_Object = MibTableColumn
h3cCBQoSNestPolicyRowStatus = _H3cCBQoSNestPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 2, 19, 1, 2),
    _H3cCBQoSNestPolicyRowStatus_Type()
)
h3cCBQoSNestPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyRowStatus.setStatus("current")
_H3cCBQoSPolicyObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSPolicyObjects = _H3cCBQoSPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3)
)
_H3cCBQoSPolicyIndexNext_Type = Integer32
_H3cCBQoSPolicyIndexNext_Object = MibScalar
h3cCBQoSPolicyIndexNext = _H3cCBQoSPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 1),
    _H3cCBQoSPolicyIndexNext_Type()
)
h3cCBQoSPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyIndexNext.setStatus("current")
_H3cCBQoSPolicyCfgInfoTable_Object = MibTable
h3cCBQoSPolicyCfgInfoTable = _H3cCBQoSPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSPolicyCfgInfoTable.setStatus("current")
_H3cCBQoSPolicyCfgInfoEntry_Object = MibTableRow
h3cCBQoSPolicyCfgInfoEntry = _H3cCBQoSPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1)
)
h3cCBQoSPolicyCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSPolicyCfgInfoEntry.setStatus("current")
_H3cCBQoSPolicyIndex_Type = Integer32
_H3cCBQoSPolicyIndex_Object = MibTableColumn
h3cCBQoSPolicyIndex = _H3cCBQoSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 1),
    _H3cCBQoSPolicyIndex_Type()
)
h3cCBQoSPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyIndex.setStatus("current")


class _H3cCBQoSPolicyName_Type(OctetString):
    """Custom type h3cCBQoSPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSPolicyName_Object = MibTableColumn
h3cCBQoSPolicyName = _H3cCBQoSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 2),
    _H3cCBQoSPolicyName_Type()
)
h3cCBQoSPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyName.setStatus("current")
_H3cCBQoSPolicyClassCount_Type = Integer32
_H3cCBQoSPolicyClassCount_Object = MibTableColumn
h3cCBQoSPolicyClassCount = _H3cCBQoSPolicyClassCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 3),
    _H3cCBQoSPolicyClassCount_Type()
)
h3cCBQoSPolicyClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassCount.setStatus("current")


class _H3cCBQoSPolicyConfigMode_Type(Integer32):
    """Custom type h3cCBQoSPolicyConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1),
          ("unavailable", 0))
    )


_H3cCBQoSPolicyConfigMode_Type.__name__ = "Integer32"
_H3cCBQoSPolicyConfigMode_Object = MibTableColumn
h3cCBQoSPolicyConfigMode = _H3cCBQoSPolicyConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 4),
    _H3cCBQoSPolicyConfigMode_Type()
)
h3cCBQoSPolicyConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyConfigMode.setStatus("current")


class _H3cCBQoSPolicyType_Type(Integer32):
    """Custom type h3cCBQoSPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemDefined", 1),
          ("userDefined", 2))
    )


_H3cCBQoSPolicyType_Type.__name__ = "Integer32"
_H3cCBQoSPolicyType_Object = MibTableColumn
h3cCBQoSPolicyType = _H3cCBQoSPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 5),
    _H3cCBQoSPolicyType_Type()
)
h3cCBQoSPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyType.setStatus("current")
_H3cCBQoSPolicyClassNextIndex_Type = Integer32
_H3cCBQoSPolicyClassNextIndex_Object = MibTableColumn
h3cCBQoSPolicyClassNextIndex = _H3cCBQoSPolicyClassNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 6),
    _H3cCBQoSPolicyClassNextIndex_Type()
)
h3cCBQoSPolicyClassNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassNextIndex.setStatus("current")
_H3cCBQoSPolicyRowStatus_Type = RowStatus
_H3cCBQoSPolicyRowStatus_Object = MibTableColumn
h3cCBQoSPolicyRowStatus = _H3cCBQoSPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 2, 1, 7),
    _H3cCBQoSPolicyRowStatus_Type()
)
h3cCBQoSPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyRowStatus.setStatus("current")
_H3cCBQoSPolicyClassCfgInfoTable_Object = MibTable
h3cCBQoSPolicyClassCfgInfoTable = _H3cCBQoSPolicyClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassCfgInfoTable.setStatus("current")
_H3cCBQoSPolicyClassCfgInfoEntry_Object = MibTableRow
h3cCBQoSPolicyClassCfgInfoEntry = _H3cCBQoSPolicyClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1)
)
h3cCBQoSPolicyClassCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassCfgInfoEntry.setStatus("current")
_H3cCBQoSPolicyClassIndex_Type = Integer32
_H3cCBQoSPolicyClassIndex_Object = MibTableColumn
h3cCBQoSPolicyClassIndex = _H3cCBQoSPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 1),
    _H3cCBQoSPolicyClassIndex_Type()
)
h3cCBQoSPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassIndex.setStatus("current")
_H3cCBQoSPolicyClassClassifierIndex_Type = Integer32
_H3cCBQoSPolicyClassClassifierIndex_Object = MibTableColumn
h3cCBQoSPolicyClassClassifierIndex = _H3cCBQoSPolicyClassClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 2),
    _H3cCBQoSPolicyClassClassifierIndex_Type()
)
h3cCBQoSPolicyClassClassifierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassClassifierIndex.setStatus("current")


class _H3cCBQoSPolicyClassClassifierName_Type(OctetString):
    """Custom type h3cCBQoSPolicyClassClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSPolicyClassClassifierName_Type.__name__ = "OctetString"
_H3cCBQoSPolicyClassClassifierName_Object = MibTableColumn
h3cCBQoSPolicyClassClassifierName = _H3cCBQoSPolicyClassClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 3),
    _H3cCBQoSPolicyClassClassifierName_Type()
)
h3cCBQoSPolicyClassClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassClassifierName.setStatus("current")
_H3cCBQoSPolicyClassBehaviorIndex_Type = Integer32
_H3cCBQoSPolicyClassBehaviorIndex_Object = MibTableColumn
h3cCBQoSPolicyClassBehaviorIndex = _H3cCBQoSPolicyClassBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 4),
    _H3cCBQoSPolicyClassBehaviorIndex_Type()
)
h3cCBQoSPolicyClassBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassBehaviorIndex.setStatus("current")


class _H3cCBQoSPolicyClassBehaviorName_Type(OctetString):
    """Custom type h3cCBQoSPolicyClassBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSPolicyClassBehaviorName_Type.__name__ = "OctetString"
_H3cCBQoSPolicyClassBehaviorName_Object = MibTableColumn
h3cCBQoSPolicyClassBehaviorName = _H3cCBQoSPolicyClassBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 5),
    _H3cCBQoSPolicyClassBehaviorName_Type()
)
h3cCBQoSPolicyClassBehaviorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassBehaviorName.setStatus("current")


class _H3cCBQoSPolicyClassPrecedence_Type(Integer32):
    """Custom type h3cCBQoSPolicyClassPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_H3cCBQoSPolicyClassPrecedence_Type.__name__ = "Integer32"
_H3cCBQoSPolicyClassPrecedence_Object = MibTableColumn
h3cCBQoSPolicyClassPrecedence = _H3cCBQoSPolicyClassPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 6),
    _H3cCBQoSPolicyClassPrecedence_Type()
)
h3cCBQoSPolicyClassPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassPrecedence.setStatus("current")
_H3cCBQoSPolicyClassRowStatus_Type = RowStatus
_H3cCBQoSPolicyClassRowStatus_Object = MibTableColumn
h3cCBQoSPolicyClassRowStatus = _H3cCBQoSPolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 7),
    _H3cCBQoSPolicyClassRowStatus_Type()
)
h3cCBQoSPolicyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassRowStatus.setStatus("current")


class _H3cCBQoSPolicyClassMode_Type(Integer32):
    """Custom type h3cCBQoSPolicyClassMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeDot1q", 2),
          ("modeNo", 1))
    )


_H3cCBQoSPolicyClassMode_Type.__name__ = "Integer32"
_H3cCBQoSPolicyClassMode_Object = MibTableColumn
h3cCBQoSPolicyClassMode = _H3cCBQoSPolicyClassMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 8),
    _H3cCBQoSPolicyClassMode_Type()
)
h3cCBQoSPolicyClassMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassMode.setStatus("current")
_H3cCBQoSPolicyClassCfgOrder_Type = Integer32
_H3cCBQoSPolicyClassCfgOrder_Object = MibTableColumn
h3cCBQoSPolicyClassCfgOrder = _H3cCBQoSPolicyClassCfgOrder_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 3, 3, 1, 9),
    _H3cCBQoSPolicyClassCfgOrder_Type()
)
h3cCBQoSPolicyClassCfgOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPolicyClassCfgOrder.setStatus("current")
_H3cCBQoSApplyPolicyObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSApplyPolicyObjects = _H3cCBQoSApplyPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4)
)
_H3cCBQoSIfApplyPolicyTable_Object = MibTable
h3cCBQoSIfApplyPolicyTable = _H3cCBQoSIfApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyTable.setStatus("current")
_H3cCBQoSIfApplyPolicyEntry_Object = MibTableRow
h3cCBQoSIfApplyPolicyEntry = _H3cCBQoSIfApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1, 1)
)
h3cCBQoSIfApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyEntry.setStatus("current")
_H3cCBQoSIfApplyPolicyIfIndex_Type = Integer32
_H3cCBQoSIfApplyPolicyIfIndex_Object = MibTableColumn
h3cCBQoSIfApplyPolicyIfIndex = _H3cCBQoSIfApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1, 1, 1),
    _H3cCBQoSIfApplyPolicyIfIndex_Type()
)
h3cCBQoSIfApplyPolicyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyIfIndex.setStatus("current")
_H3cCBQoSIfApplyPolicyDirection_Type = DirectionType
_H3cCBQoSIfApplyPolicyDirection_Object = MibTableColumn
h3cCBQoSIfApplyPolicyDirection = _H3cCBQoSIfApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1, 1, 2),
    _H3cCBQoSIfApplyPolicyDirection_Type()
)
h3cCBQoSIfApplyPolicyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyDirection.setStatus("current")


class _H3cCBQoSIfApplyPolicyName_Type(OctetString):
    """Custom type h3cCBQoSIfApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSIfApplyPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSIfApplyPolicyName_Object = MibTableColumn
h3cCBQoSIfApplyPolicyName = _H3cCBQoSIfApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1, 1, 3),
    _H3cCBQoSIfApplyPolicyName_Type()
)
h3cCBQoSIfApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyName.setStatus("current")


class _H3cCBQoSIfApplyPolicyEnableDynamic_Type(Integer32):
    """Custom type h3cCBQoSIfApplyPolicyEnableDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("true", 2),
          ("unavailable", 1))
    )


_H3cCBQoSIfApplyPolicyEnableDynamic_Type.__name__ = "Integer32"
_H3cCBQoSIfApplyPolicyEnableDynamic_Object = MibTableColumn
h3cCBQoSIfApplyPolicyEnableDynamic = _H3cCBQoSIfApplyPolicyEnableDynamic_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1, 1, 4),
    _H3cCBQoSIfApplyPolicyEnableDynamic_Type()
)
h3cCBQoSIfApplyPolicyEnableDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyEnableDynamic.setStatus("current")
_H3cCBQoSIfApplyPolicyRowStatus_Type = RowStatus
_H3cCBQoSIfApplyPolicyRowStatus_Object = MibTableColumn
h3cCBQoSIfApplyPolicyRowStatus = _H3cCBQoSIfApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 1, 1, 5),
    _H3cCBQoSIfApplyPolicyRowStatus_Type()
)
h3cCBQoSIfApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSIfApplyPolicyRowStatus.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyTable_Object = MibTable
h3cCBQoSAtmPvcApplyPolicyTable = _H3cCBQoSAtmPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyTable.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyEntry_Object = MibTableRow
h3cCBQoSAtmPvcApplyPolicyEntry = _H3cCBQoSAtmPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1)
)
h3cCBQoSAtmPvcApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyEntry.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyIfIndex_Type = Integer32
_H3cCBQoSAtmPvcApplyPolicyIfIndex_Object = MibTableColumn
h3cCBQoSAtmPvcApplyPolicyIfIndex = _H3cCBQoSAtmPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1, 1),
    _H3cCBQoSAtmPvcApplyPolicyIfIndex_Type()
)
h3cCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyIfIndex.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyVPI_Type = Integer32
_H3cCBQoSAtmPvcApplyPolicyVPI_Object = MibTableColumn
h3cCBQoSAtmPvcApplyPolicyVPI = _H3cCBQoSAtmPvcApplyPolicyVPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1, 2),
    _H3cCBQoSAtmPvcApplyPolicyVPI_Type()
)
h3cCBQoSAtmPvcApplyPolicyVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyVPI.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyVCI_Type = Integer32
_H3cCBQoSAtmPvcApplyPolicyVCI_Object = MibTableColumn
h3cCBQoSAtmPvcApplyPolicyVCI = _H3cCBQoSAtmPvcApplyPolicyVCI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1, 3),
    _H3cCBQoSAtmPvcApplyPolicyVCI_Type()
)
h3cCBQoSAtmPvcApplyPolicyVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyVCI.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyDirection_Type = DirectionType
_H3cCBQoSAtmPvcApplyPolicyDirection_Object = MibTableColumn
h3cCBQoSAtmPvcApplyPolicyDirection = _H3cCBQoSAtmPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1, 4),
    _H3cCBQoSAtmPvcApplyPolicyDirection_Type()
)
h3cCBQoSAtmPvcApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyDirection.setStatus("current")


class _H3cCBQoSAtmPvcApplyPolicyName_Type(OctetString):
    """Custom type h3cCBQoSAtmPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSAtmPvcApplyPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSAtmPvcApplyPolicyName_Object = MibTableColumn
h3cCBQoSAtmPvcApplyPolicyName = _H3cCBQoSAtmPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1, 5),
    _H3cCBQoSAtmPvcApplyPolicyName_Type()
)
h3cCBQoSAtmPvcApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyName.setStatus("current")
_H3cCBQoSAtmPvcApplyPolicyRowStatus_Type = RowStatus
_H3cCBQoSAtmPvcApplyPolicyRowStatus_Object = MibTableColumn
h3cCBQoSAtmPvcApplyPolicyRowStatus = _H3cCBQoSAtmPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 2, 1, 6),
    _H3cCBQoSAtmPvcApplyPolicyRowStatus_Type()
)
h3cCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcApplyPolicyRowStatus.setStatus("current")
_H3cCBQoSVlanApplyPolicyTable_Object = MibTable
h3cCBQoSVlanApplyPolicyTable = _H3cCBQoSVlanApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPolicyTable.setStatus("current")
_H3cCBQoSVlanApplyPolicyEntry_Object = MibTableRow
h3cCBQoSVlanApplyPolicyEntry = _H3cCBQoSVlanApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3, 1)
)
h3cCBQoSVlanApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyVlanid"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPolicyEntry.setStatus("current")
_H3cCBQoSVlanApplyPolicyVlanid_Type = Integer32
_H3cCBQoSVlanApplyPolicyVlanid_Object = MibTableColumn
h3cCBQoSVlanApplyPolicyVlanid = _H3cCBQoSVlanApplyPolicyVlanid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3, 1, 1),
    _H3cCBQoSVlanApplyPolicyVlanid_Type()
)
h3cCBQoSVlanApplyPolicyVlanid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPolicyVlanid.setStatus("current")
_H3cCBQoSVlanApplyPolicyDirection_Type = DirectionType
_H3cCBQoSVlanApplyPolicyDirection_Object = MibTableColumn
h3cCBQoSVlanApplyPolicyDirection = _H3cCBQoSVlanApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3, 1, 2),
    _H3cCBQoSVlanApplyPolicyDirection_Type()
)
h3cCBQoSVlanApplyPolicyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPolicyDirection.setStatus("current")


class _H3cCBQoSVlanApplyPolicyName_Type(OctetString):
    """Custom type h3cCBQoSVlanApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cCBQoSVlanApplyPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSVlanApplyPolicyName_Object = MibTableColumn
h3cCBQoSVlanApplyPolicyName = _H3cCBQoSVlanApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3, 1, 3),
    _H3cCBQoSVlanApplyPolicyName_Type()
)
h3cCBQoSVlanApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPolicyName.setStatus("current")


class _H3cCBQoSVlanApplyPriority_Type(Integer32):
    """Custom type h3cCBQoSVlanApplyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_H3cCBQoSVlanApplyPriority_Type.__name__ = "Integer32"
_H3cCBQoSVlanApplyPriority_Object = MibTableColumn
h3cCBQoSVlanApplyPriority = _H3cCBQoSVlanApplyPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3, 1, 4),
    _H3cCBQoSVlanApplyPriority_Type()
)
h3cCBQoSVlanApplyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPriority.setStatus("current")
_H3cCBQoSVlanApplyPolicyRowStatus_Type = RowStatus
_H3cCBQoSVlanApplyPolicyRowStatus_Object = MibTableColumn
h3cCBQoSVlanApplyPolicyRowStatus = _H3cCBQoSVlanApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 3, 1, 5),
    _H3cCBQoSVlanApplyPolicyRowStatus_Type()
)
h3cCBQoSVlanApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyPolicyRowStatus.setStatus("current")
_H3cCBQoSFrClassApplyPolicyTable_Object = MibTable
h3cCBQoSFrClassApplyPolicyTable = _H3cCBQoSFrClassApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrClassApplyPolicyTable.setStatus("current")
_H3cCBQoSFrClassApplyPolicyEntry_Object = MibTableRow
h3cCBQoSFrClassApplyPolicyEntry = _H3cCBQoSFrClassApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 4, 1)
)
h3cCBQoSFrClassApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrClassApplyPolicyFrClassName"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrClassApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrClassApplyPolicyEntry.setStatus("current")


class _H3cCBQoSFrClassApplyPolicyFrClassName_Type(OctetString):
    """Custom type h3cCBQoSFrClassApplyPolicyFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSFrClassApplyPolicyFrClassName_Type.__name__ = "OctetString"
_H3cCBQoSFrClassApplyPolicyFrClassName_Object = MibTableColumn
h3cCBQoSFrClassApplyPolicyFrClassName = _H3cCBQoSFrClassApplyPolicyFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 4, 1, 1),
    _H3cCBQoSFrClassApplyPolicyFrClassName_Type()
)
h3cCBQoSFrClassApplyPolicyFrClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSFrClassApplyPolicyFrClassName.setStatus("current")
_H3cCBQoSFrClassApplyPolicyDirection_Type = DirectionType
_H3cCBQoSFrClassApplyPolicyDirection_Object = MibTableColumn
h3cCBQoSFrClassApplyPolicyDirection = _H3cCBQoSFrClassApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 4, 1, 2),
    _H3cCBQoSFrClassApplyPolicyDirection_Type()
)
h3cCBQoSFrClassApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSFrClassApplyPolicyDirection.setStatus("current")


class _H3cCBQoSFrClassApplyPolicyName_Type(OctetString):
    """Custom type h3cCBQoSFrClassApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSFrClassApplyPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSFrClassApplyPolicyName_Object = MibTableColumn
h3cCBQoSFrClassApplyPolicyName = _H3cCBQoSFrClassApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 4, 1, 3),
    _H3cCBQoSFrClassApplyPolicyName_Type()
)
h3cCBQoSFrClassApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSFrClassApplyPolicyName.setStatus("current")
_H3cCBQoSFrClassApplyPolicyRowStatus_Type = RowStatus
_H3cCBQoSFrClassApplyPolicyRowStatus_Object = MibTableColumn
h3cCBQoSFrClassApplyPolicyRowStatus = _H3cCBQoSFrClassApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 4, 1, 4),
    _H3cCBQoSFrClassApplyPolicyRowStatus_Type()
)
h3cCBQoSFrClassApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSFrClassApplyPolicyRowStatus.setStatus("current")
_H3cCBQoSFrPvcApplyPolicyTable_Object = MibTable
h3cCBQoSFrPvcApplyPolicyTable = _H3cCBQoSFrPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyTable.setStatus("current")
_H3cCBQoSFrPvcApplyPolicyEntry_Object = MibTableRow
h3cCBQoSFrPvcApplyPolicyEntry = _H3cCBQoSFrPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5, 1)
)
h3cCBQoSFrPvcApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyEntry.setStatus("current")
_H3cCBQoSFrPvcApplyPolicyIfIndex_Type = Integer32
_H3cCBQoSFrPvcApplyPolicyIfIndex_Object = MibTableColumn
h3cCBQoSFrPvcApplyPolicyIfIndex = _H3cCBQoSFrPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5, 1, 1),
    _H3cCBQoSFrPvcApplyPolicyIfIndex_Type()
)
h3cCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyIfIndex.setStatus("current")


class _H3cCBQoSFrPvcApplyPolicyDlciNum_Type(Integer32):
    """Custom type h3cCBQoSFrPvcApplyPolicyDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_H3cCBQoSFrPvcApplyPolicyDlciNum_Type.__name__ = "Integer32"
_H3cCBQoSFrPvcApplyPolicyDlciNum_Object = MibTableColumn
h3cCBQoSFrPvcApplyPolicyDlciNum = _H3cCBQoSFrPvcApplyPolicyDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5, 1, 2),
    _H3cCBQoSFrPvcApplyPolicyDlciNum_Type()
)
h3cCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyDlciNum.setStatus("current")
_H3cCBQoSFrPvcApplyPolicyDirection_Type = DirectionType
_H3cCBQoSFrPvcApplyPolicyDirection_Object = MibTableColumn
h3cCBQoSFrPvcApplyPolicyDirection = _H3cCBQoSFrPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5, 1, 3),
    _H3cCBQoSFrPvcApplyPolicyDirection_Type()
)
h3cCBQoSFrPvcApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyDirection.setStatus("current")


class _H3cCBQoSFrPvcApplyPolicyName_Type(OctetString):
    """Custom type h3cCBQoSFrPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSFrPvcApplyPolicyName_Type.__name__ = "OctetString"
_H3cCBQoSFrPvcApplyPolicyName_Object = MibTableColumn
h3cCBQoSFrPvcApplyPolicyName = _H3cCBQoSFrPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5, 1, 4),
    _H3cCBQoSFrPvcApplyPolicyName_Type()
)
h3cCBQoSFrPvcApplyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyName.setStatus("current")
_H3cCBQoSFrPvcApplyPolicyRowStatus_Type = RowStatus
_H3cCBQoSFrPvcApplyPolicyRowStatus_Object = MibTableColumn
h3cCBQoSFrPvcApplyPolicyRowStatus = _H3cCBQoSFrPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 5, 1, 5),
    _H3cCBQoSFrPvcApplyPolicyRowStatus_Type()
)
h3cCBQoSFrPvcApplyPolicyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcApplyPolicyRowStatus.setStatus("current")
_H3cCBQoSGlobalApplyTable_Object = MibTable
h3cCBQoSGlobalApplyTable = _H3cCBQoSGlobalApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    h3cCBQoSGlobalApplyTable.setStatus("current")
_H3cCBQoSGlobalApplyEntry_Object = MibTableRow
h3cCBQoSGlobalApplyEntry = _H3cCBQoSGlobalApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 6, 1)
)
h3cCBQoSGlobalApplyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSGlobalApplyDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSGlobalApplyEntry.setStatus("current")
_H3cCBQoSGlobalApplyDirection_Type = DirectionType
_H3cCBQoSGlobalApplyDirection_Object = MibTableColumn
h3cCBQoSGlobalApplyDirection = _H3cCBQoSGlobalApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 6, 1, 1),
    _H3cCBQoSGlobalApplyDirection_Type()
)
h3cCBQoSGlobalApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSGlobalApplyDirection.setStatus("current")


class _H3cCBQoSGlobalApplyName_Type(OctetString):
    """Custom type h3cCBQoSGlobalApplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cCBQoSGlobalApplyName_Type.__name__ = "OctetString"
_H3cCBQoSGlobalApplyName_Object = MibTableColumn
h3cCBQoSGlobalApplyName = _H3cCBQoSGlobalApplyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 6, 1, 2),
    _H3cCBQoSGlobalApplyName_Type()
)
h3cCBQoSGlobalApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGlobalApplyName.setStatus("current")
_H3cCBQoSGlobalApplyRowStatus_Type = RowStatus
_H3cCBQoSGlobalApplyRowStatus_Object = MibTableColumn
h3cCBQoSGlobalApplyRowStatus = _H3cCBQoSGlobalApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 4, 6, 1, 3),
    _H3cCBQoSGlobalApplyRowStatus_Type()
)
h3cCBQoSGlobalApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCBQoSGlobalApplyRowStatus.setStatus("current")
_H3cCBQoSApplyPolicyStaticsObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSApplyPolicyStaticsObjects = _H3cCBQoSApplyPolicyStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5)
)
_H3cCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSIfStaticsObjects = _H3cCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1)
)
_H3cCBQoSIfCbqRunInfoTable_Object = MibTable
h3cCBQoSIfCbqRunInfoTable = _H3cCBQoSIfCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqRunInfoTable.setStatus("current")
_H3cCBQoSIfCbqRunInfoEntry_Object = MibTableRow
h3cCBQoSIfCbqRunInfoEntry = _H3cCBQoSIfCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1)
)
h3cCBQoSIfCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqRunInfoEntry.setStatus("current")
_H3cCBQoSIfCbqQueueSize_Type = Integer32
_H3cCBQoSIfCbqQueueSize_Object = MibTableColumn
h3cCBQoSIfCbqQueueSize = _H3cCBQoSIfCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 1),
    _H3cCBQoSIfCbqQueueSize_Type()
)
h3cCBQoSIfCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqQueueSize.setStatus("current")
_H3cCBQoSIfCbqDiscard_Type = Counter64
_H3cCBQoSIfCbqDiscard_Object = MibTableColumn
h3cCBQoSIfCbqDiscard = _H3cCBQoSIfCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 2),
    _H3cCBQoSIfCbqDiscard_Type()
)
h3cCBQoSIfCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqDiscard.setStatus("current")
_H3cCBQoSIfCbqEfQueueSize_Type = Integer32
_H3cCBQoSIfCbqEfQueueSize_Object = MibTableColumn
h3cCBQoSIfCbqEfQueueSize = _H3cCBQoSIfCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 3),
    _H3cCBQoSIfCbqEfQueueSize_Type()
)
h3cCBQoSIfCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqEfQueueSize.setStatus("current")
_H3cCBQoSIfCbqAfQueueSize_Type = Integer32
_H3cCBQoSIfCbqAfQueueSize_Object = MibTableColumn
h3cCBQoSIfCbqAfQueueSize = _H3cCBQoSIfCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 4),
    _H3cCBQoSIfCbqAfQueueSize_Type()
)
h3cCBQoSIfCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqAfQueueSize.setStatus("current")
_H3cCBQoSIfCbqBeQueueSize_Type = Integer32
_H3cCBQoSIfCbqBeQueueSize_Object = MibTableColumn
h3cCBQoSIfCbqBeQueueSize = _H3cCBQoSIfCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 5),
    _H3cCBQoSIfCbqBeQueueSize_Type()
)
h3cCBQoSIfCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqBeQueueSize.setStatus("current")
_H3cCBQoSIfCbqBeActiveQueueNum_Type = Integer32
_H3cCBQoSIfCbqBeActiveQueueNum_Object = MibTableColumn
h3cCBQoSIfCbqBeActiveQueueNum = _H3cCBQoSIfCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 6),
    _H3cCBQoSIfCbqBeActiveQueueNum_Type()
)
h3cCBQoSIfCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqBeActiveQueueNum.setStatus("current")
_H3cCBQoSIfCbqBeMaxActiveQueueNum_Type = Integer32
_H3cCBQoSIfCbqBeMaxActiveQueueNum_Object = MibTableColumn
h3cCBQoSIfCbqBeMaxActiveQueueNum = _H3cCBQoSIfCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 7),
    _H3cCBQoSIfCbqBeMaxActiveQueueNum_Type()
)
h3cCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqBeMaxActiveQueueNum.setStatus("current")
_H3cCBQoSIfCbqBeTotalQueueNum_Type = Integer32
_H3cCBQoSIfCbqBeTotalQueueNum_Object = MibTableColumn
h3cCBQoSIfCbqBeTotalQueueNum = _H3cCBQoSIfCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 8),
    _H3cCBQoSIfCbqBeTotalQueueNum_Type()
)
h3cCBQoSIfCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqBeTotalQueueNum.setStatus("current")
_H3cCBQoSIfCbqAfAllocatedQueueNum_Type = Integer32
_H3cCBQoSIfCbqAfAllocatedQueueNum_Object = MibTableColumn
h3cCBQoSIfCbqAfAllocatedQueueNum = _H3cCBQoSIfCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 1, 1, 9),
    _H3cCBQoSIfCbqAfAllocatedQueueNum_Type()
)
h3cCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCbqAfAllocatedQueueNum.setStatus("current")
_H3cCBQoSIfClassMatchRunInfoTable_Object = MibTable
h3cCBQoSIfClassMatchRunInfoTable = _H3cCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfClassMatchRunInfoTable.setStatus("current")
_H3cCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
h3cCBQoSIfClassMatchRunInfoEntry = _H3cCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 2, 1)
)
h3cCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_H3cCBQoSIfClassMatchedPackets_Type = Counter64
_H3cCBQoSIfClassMatchedPackets_Object = MibTableColumn
h3cCBQoSIfClassMatchedPackets = _H3cCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 2, 1, 1),
    _H3cCBQoSIfClassMatchedPackets_Type()
)
h3cCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfClassMatchedPackets.setStatus("current")
_H3cCBQoSIfClassMatchedBytes_Type = Counter64
_H3cCBQoSIfClassMatchedBytes_Object = MibTableColumn
h3cCBQoSIfClassMatchedBytes = _H3cCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 2, 1, 2),
    _H3cCBQoSIfClassMatchedBytes_Type()
)
h3cCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfClassMatchedBytes.setStatus("current")
_H3cCBQoSIfClassAverageRate_Type = Counter64
_H3cCBQoSIfClassAverageRate_Object = MibTableColumn
h3cCBQoSIfClassAverageRate = _H3cCBQoSIfClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 2, 1, 3),
    _H3cCBQoSIfClassAverageRate_Type()
)
h3cCBQoSIfClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfClassAverageRate.setStatus("current")
_H3cCBQoSIfCarRunInfoTable_Object = MibTable
h3cCBQoSIfCarRunInfoTable = _H3cCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfCarRunInfoTable.setStatus("current")
_H3cCBQoSIfCarRunInfoEntry_Object = MibTableRow
h3cCBQoSIfCarRunInfoEntry = _H3cCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1)
)
h3cCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfCarRunInfoEntry.setStatus("current")
_H3cCBQoSIfCarGreenPackets_Type = Counter64
_H3cCBQoSIfCarGreenPackets_Object = MibTableColumn
h3cCBQoSIfCarGreenPackets = _H3cCBQoSIfCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1, 1),
    _H3cCBQoSIfCarGreenPackets_Type()
)
h3cCBQoSIfCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCarGreenPackets.setStatus("current")
_H3cCBQoSIfCarGreenBytes_Type = Counter64
_H3cCBQoSIfCarGreenBytes_Object = MibTableColumn
h3cCBQoSIfCarGreenBytes = _H3cCBQoSIfCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1, 2),
    _H3cCBQoSIfCarGreenBytes_Type()
)
h3cCBQoSIfCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCarGreenBytes.setStatus("current")
_H3cCBQoSIfCarRedPackets_Type = Counter64
_H3cCBQoSIfCarRedPackets_Object = MibTableColumn
h3cCBQoSIfCarRedPackets = _H3cCBQoSIfCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1, 3),
    _H3cCBQoSIfCarRedPackets_Type()
)
h3cCBQoSIfCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCarRedPackets.setStatus("current")
_H3cCBQoSIfCarRedBytes_Type = Counter64
_H3cCBQoSIfCarRedBytes_Object = MibTableColumn
h3cCBQoSIfCarRedBytes = _H3cCBQoSIfCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1, 4),
    _H3cCBQoSIfCarRedBytes_Type()
)
h3cCBQoSIfCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCarRedBytes.setStatus("current")
_H3cCBQoSIfCarYellowPackets_Type = Counter64
_H3cCBQoSIfCarYellowPackets_Object = MibTableColumn
h3cCBQoSIfCarYellowPackets = _H3cCBQoSIfCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1, 5),
    _H3cCBQoSIfCarYellowPackets_Type()
)
h3cCBQoSIfCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCarYellowPackets.setStatus("current")
_H3cCBQoSIfCarYellowBytes_Type = Counter64
_H3cCBQoSIfCarYellowBytes_Object = MibTableColumn
h3cCBQoSIfCarYellowBytes = _H3cCBQoSIfCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 3, 1, 6),
    _H3cCBQoSIfCarYellowBytes_Type()
)
h3cCBQoSIfCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfCarYellowBytes.setStatus("current")
_H3cCBQoSIfGtsRunInfoTable_Object = MibTable
h3cCBQoSIfGtsRunInfoTable = _H3cCBQoSIfGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsRunInfoTable.setStatus("current")
_H3cCBQoSIfGtsRunInfoEntry_Object = MibTableRow
h3cCBQoSIfGtsRunInfoEntry = _H3cCBQoSIfGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1)
)
h3cCBQoSIfGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsRunInfoEntry.setStatus("current")
_H3cCBQoSIfGtsPassedPackets_Type = Counter64
_H3cCBQoSIfGtsPassedPackets_Object = MibTableColumn
h3cCBQoSIfGtsPassedPackets = _H3cCBQoSIfGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 1),
    _H3cCBQoSIfGtsPassedPackets_Type()
)
h3cCBQoSIfGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsPassedPackets.setStatus("current")
_H3cCBQoSIfGtsPassedBytes_Type = Counter64
_H3cCBQoSIfGtsPassedBytes_Object = MibTableColumn
h3cCBQoSIfGtsPassedBytes = _H3cCBQoSIfGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 2),
    _H3cCBQoSIfGtsPassedBytes_Type()
)
h3cCBQoSIfGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsPassedBytes.setStatus("current")
_H3cCBQoSIfGtsDiscardedPackets_Type = Counter64
_H3cCBQoSIfGtsDiscardedPackets_Object = MibTableColumn
h3cCBQoSIfGtsDiscardedPackets = _H3cCBQoSIfGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 3),
    _H3cCBQoSIfGtsDiscardedPackets_Type()
)
h3cCBQoSIfGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsDiscardedPackets.setStatus("current")
_H3cCBQoSIfGtsDiscardedBytes_Type = Counter64
_H3cCBQoSIfGtsDiscardedBytes_Object = MibTableColumn
h3cCBQoSIfGtsDiscardedBytes = _H3cCBQoSIfGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 4),
    _H3cCBQoSIfGtsDiscardedBytes_Type()
)
h3cCBQoSIfGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsDiscardedBytes.setStatus("current")
_H3cCBQoSIfGtsDelayedPackets_Type = Counter64
_H3cCBQoSIfGtsDelayedPackets_Object = MibTableColumn
h3cCBQoSIfGtsDelayedPackets = _H3cCBQoSIfGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 5),
    _H3cCBQoSIfGtsDelayedPackets_Type()
)
h3cCBQoSIfGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsDelayedPackets.setStatus("current")
_H3cCBQoSIfGtsDelayedBytes_Type = Counter64
_H3cCBQoSIfGtsDelayedBytes_Object = MibTableColumn
h3cCBQoSIfGtsDelayedBytes = _H3cCBQoSIfGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 6),
    _H3cCBQoSIfGtsDelayedBytes_Type()
)
h3cCBQoSIfGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsDelayedBytes.setStatus("current")
_H3cCBQoSIfGtsQueueSize_Type = Integer32
_H3cCBQoSIfGtsQueueSize_Object = MibTableColumn
h3cCBQoSIfGtsQueueSize = _H3cCBQoSIfGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 4, 1, 7),
    _H3cCBQoSIfGtsQueueSize_Type()
)
h3cCBQoSIfGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfGtsQueueSize.setStatus("current")
_H3cCBQoSIfRemarkRunInfoTable_Object = MibTable
h3cCBQoSIfRemarkRunInfoTable = _H3cCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfRemarkRunInfoTable.setStatus("current")
_H3cCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
h3cCBQoSIfRemarkRunInfoEntry = _H3cCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 5, 1)
)
h3cCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfRemarkRunInfoEntry.setStatus("current")
_H3cCBQoSIfRemarkedPackets_Type = Counter64
_H3cCBQoSIfRemarkedPackets_Object = MibTableColumn
h3cCBQoSIfRemarkedPackets = _H3cCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 5, 1, 1),
    _H3cCBQoSIfRemarkedPackets_Type()
)
h3cCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfRemarkedPackets.setStatus("current")
_H3cCBQoSIfQueueRunInfoTable_Object = MibTable
h3cCBQoSIfQueueRunInfoTable = _H3cCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueRunInfoTable.setStatus("current")
_H3cCBQoSIfQueueRunInfoEntry_Object = MibTableRow
h3cCBQoSIfQueueRunInfoEntry = _H3cCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1)
)
h3cCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueRunInfoEntry.setStatus("current")
_H3cCBQoSIfQueueMatchedPackets_Type = Counter64
_H3cCBQoSIfQueueMatchedPackets_Object = MibTableColumn
h3cCBQoSIfQueueMatchedPackets = _H3cCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1, 1),
    _H3cCBQoSIfQueueMatchedPackets_Type()
)
h3cCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueMatchedPackets.setStatus("current")
_H3cCBQoSIfQueueMatchedBytes_Type = Counter64
_H3cCBQoSIfQueueMatchedBytes_Object = MibTableColumn
h3cCBQoSIfQueueMatchedBytes = _H3cCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1, 2),
    _H3cCBQoSIfQueueMatchedBytes_Type()
)
h3cCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueMatchedBytes.setStatus("current")
_H3cCBQoSIfQueueEnqueuedPackets_Type = Counter64
_H3cCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
h3cCBQoSIfQueueEnqueuedPackets = _H3cCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1, 3),
    _H3cCBQoSIfQueueEnqueuedPackets_Type()
)
h3cCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueEnqueuedPackets.setStatus("current")
_H3cCBQoSIfQueueEnqueuedBytes_Type = Counter64
_H3cCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
h3cCBQoSIfQueueEnqueuedBytes = _H3cCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1, 4),
    _H3cCBQoSIfQueueEnqueuedBytes_Type()
)
h3cCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueEnqueuedBytes.setStatus("current")
_H3cCBQoSIfQueueDiscardedPackets_Type = Counter64
_H3cCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
h3cCBQoSIfQueueDiscardedPackets = _H3cCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1, 5),
    _H3cCBQoSIfQueueDiscardedPackets_Type()
)
h3cCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueDiscardedPackets.setStatus("current")
_H3cCBQoSIfQueueDiscardedBytes_Type = Counter64
_H3cCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
h3cCBQoSIfQueueDiscardedBytes = _H3cCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 6, 1, 6),
    _H3cCBQoSIfQueueDiscardedBytes_Type()
)
h3cCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfQueueDiscardedBytes.setStatus("current")
_H3cCBQoSIfWredRunInfoTable_Object = MibTable
h3cCBQoSIfWredRunInfoTable = _H3cCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfWredRunInfoTable.setStatus("current")
_H3cCBQoSIfWredRunInfoEntry_Object = MibTableRow
h3cCBQoSIfWredRunInfoEntry = _H3cCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 7, 1)
)
h3cCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfWredRunInfoEntry.setStatus("current")
_H3cCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_H3cCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
h3cCBQoSIfWredRandomDiscardedPackets = _H3cCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 7, 1, 1),
    _H3cCBQoSIfWredRandomDiscardedPackets_Type()
)
h3cCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_H3cCBQoSIfWredTailDiscardedPackets_Type = Counter64
_H3cCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
h3cCBQoSIfWredTailDiscardedPackets = _H3cCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 7, 1, 2),
    _H3cCBQoSIfWredTailDiscardedPackets_Type()
)
h3cCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfWredTailDiscardedPackets.setStatus("current")
_H3cCBQoSIfAccountingRunInfoTable_Object = MibTable
h3cCBQoSIfAccountingRunInfoTable = _H3cCBQoSIfAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    h3cCBQoSIfAccountingRunInfoTable.setStatus("current")
_H3cCBQoSIfAccountingRunInfoEntry_Object = MibTableRow
h3cCBQoSIfAccountingRunInfoEntry = _H3cCBQoSIfAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 8, 1)
)
h3cCBQoSIfAccountingRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIfAccountingRunInfoEntry.setStatus("current")
_H3cCBQoSIfAccountingPackets_Type = Counter64
_H3cCBQoSIfAccountingPackets_Object = MibTableColumn
h3cCBQoSIfAccountingPackets = _H3cCBQoSIfAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 8, 1, 1),
    _H3cCBQoSIfAccountingPackets_Type()
)
h3cCBQoSIfAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfAccountingPackets.setStatus("current")
_H3cCBQoSIfAccountingBytes_Type = Counter64
_H3cCBQoSIfAccountingBytes_Object = MibTableColumn
h3cCBQoSIfAccountingBytes = _H3cCBQoSIfAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 1, 8, 1, 2),
    _H3cCBQoSIfAccountingBytes_Type()
)
h3cCBQoSIfAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIfAccountingBytes.setStatus("current")
_H3cCBQoSAtmPvcStaticsObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSAtmPvcStaticsObjects = _H3cCBQoSAtmPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2)
)
_H3cCBQoSAtmPvcCbqRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcCbqRunInfoTable = _H3cCBQoSAtmPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcCbqRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcCbqRunInfoEntry = _H3cCBQoSAtmPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1)
)
h3cCBQoSAtmPvcCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcCbqQueueSize_Type = Integer32
_H3cCBQoSAtmPvcCbqQueueSize_Object = MibTableColumn
h3cCBQoSAtmPvcCbqQueueSize = _H3cCBQoSAtmPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 1),
    _H3cCBQoSAtmPvcCbqQueueSize_Type()
)
h3cCBQoSAtmPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqQueueSize.setStatus("current")
_H3cCBQoSAtmPvcCbqDiscard_Type = Counter64
_H3cCBQoSAtmPvcCbqDiscard_Object = MibTableColumn
h3cCBQoSAtmPvcCbqDiscard = _H3cCBQoSAtmPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 2),
    _H3cCBQoSAtmPvcCbqDiscard_Type()
)
h3cCBQoSAtmPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqDiscard.setStatus("current")
_H3cCBQoSAtmPvcCbqEfQueueSize_Type = Integer32
_H3cCBQoSAtmPvcCbqEfQueueSize_Object = MibTableColumn
h3cCBQoSAtmPvcCbqEfQueueSize = _H3cCBQoSAtmPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 3),
    _H3cCBQoSAtmPvcCbqEfQueueSize_Type()
)
h3cCBQoSAtmPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqEfQueueSize.setStatus("current")
_H3cCBQoSAtmPvcCbqAfQueueSize_Type = Integer32
_H3cCBQoSAtmPvcCbqAfQueueSize_Object = MibTableColumn
h3cCBQoSAtmPvcCbqAfQueueSize = _H3cCBQoSAtmPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 4),
    _H3cCBQoSAtmPvcCbqAfQueueSize_Type()
)
h3cCBQoSAtmPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqAfQueueSize.setStatus("current")
_H3cCBQoSAtmPvcCbqBeQueueSize_Type = Integer32
_H3cCBQoSAtmPvcCbqBeQueueSize_Object = MibTableColumn
h3cCBQoSAtmPvcCbqBeQueueSize = _H3cCBQoSAtmPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 5),
    _H3cCBQoSAtmPvcCbqBeQueueSize_Type()
)
h3cCBQoSAtmPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqBeQueueSize.setStatus("current")
_H3cCBQoSAtmPvcCbqBeActiveQueueNum_Type = Integer32
_H3cCBQoSAtmPvcCbqBeActiveQueueNum_Object = MibTableColumn
h3cCBQoSAtmPvcCbqBeActiveQueueNum = _H3cCBQoSAtmPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 6),
    _H3cCBQoSAtmPvcCbqBeActiveQueueNum_Type()
)
h3cCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqBeActiveQueueNum.setStatus("current")
_H3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type = Integer32
_H3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
h3cCBQoSAtmPvcCbqBeMaxActiveQueueNum = _H3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 7),
    _H3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type()
)
h3cCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus("current")
_H3cCBQoSAtmPvcCbqBeTotalQueueNum_Type = Integer32
_H3cCBQoSAtmPvcCbqBeTotalQueueNum_Object = MibTableColumn
h3cCBQoSAtmPvcCbqBeTotalQueueNum = _H3cCBQoSAtmPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 8),
    _H3cCBQoSAtmPvcCbqBeTotalQueueNum_Type()
)
h3cCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqBeTotalQueueNum.setStatus("current")
_H3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Type = Integer32
_H3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
h3cCBQoSAtmPvcCbqAfAllocatedQueueNum = _H3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 1, 1, 9),
    _H3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Type()
)
h3cCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus("current")
_H3cCBQoSAtmPvcClassMatchRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcClassMatchRunInfoTable = _H3cCBQoSAtmPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcClassMatchRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcClassMatchRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcClassMatchRunInfoEntry = _H3cCBQoSAtmPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 2, 1)
)
h3cCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcClassMatchRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcClassMatchPackets_Type = Counter64
_H3cCBQoSAtmPvcClassMatchPackets_Object = MibTableColumn
h3cCBQoSAtmPvcClassMatchPackets = _H3cCBQoSAtmPvcClassMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 2, 1, 1),
    _H3cCBQoSAtmPvcClassMatchPackets_Type()
)
h3cCBQoSAtmPvcClassMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcClassMatchPackets.setStatus("current")
_H3cCBQoSAtmPvcClassMatchBytes_Type = Counter64
_H3cCBQoSAtmPvcClassMatchBytes_Object = MibTableColumn
h3cCBQoSAtmPvcClassMatchBytes = _H3cCBQoSAtmPvcClassMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 2, 1, 2),
    _H3cCBQoSAtmPvcClassMatchBytes_Type()
)
h3cCBQoSAtmPvcClassMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcClassMatchBytes.setStatus("current")
_H3cCBQoSAtmPvcClassAverageRate_Type = Integer32
_H3cCBQoSAtmPvcClassAverageRate_Object = MibTableColumn
h3cCBQoSAtmPvcClassAverageRate = _H3cCBQoSAtmPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 2, 1, 3),
    _H3cCBQoSAtmPvcClassAverageRate_Type()
)
h3cCBQoSAtmPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcClassAverageRate.setStatus("current")
_H3cCBQoSAtmPvcCarRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcCarRunInfoTable = _H3cCBQoSAtmPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCarRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcCarRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcCarRunInfoEntry = _H3cCBQoSAtmPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 3, 1)
)
h3cCBQoSAtmPvcCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCarRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcCarConformPackets_Type = Counter64
_H3cCBQoSAtmPvcCarConformPackets_Object = MibTableColumn
h3cCBQoSAtmPvcCarConformPackets = _H3cCBQoSAtmPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 3, 1, 1),
    _H3cCBQoSAtmPvcCarConformPackets_Type()
)
h3cCBQoSAtmPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCarConformPackets.setStatus("current")
_H3cCBQoSAtmPvcCarConformBytes_Type = Counter64
_H3cCBQoSAtmPvcCarConformBytes_Object = MibTableColumn
h3cCBQoSAtmPvcCarConformBytes = _H3cCBQoSAtmPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 3, 1, 2),
    _H3cCBQoSAtmPvcCarConformBytes_Type()
)
h3cCBQoSAtmPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCarConformBytes.setStatus("current")
_H3cCBQoSAtmPvcCarExceedPackets_Type = Counter64
_H3cCBQoSAtmPvcCarExceedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcCarExceedPackets = _H3cCBQoSAtmPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 3, 1, 3),
    _H3cCBQoSAtmPvcCarExceedPackets_Type()
)
h3cCBQoSAtmPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCarExceedPackets.setStatus("current")
_H3cCBQoSAtmPvcCarExceedBytes_Type = Counter64
_H3cCBQoSAtmPvcCarExceedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcCarExceedBytes = _H3cCBQoSAtmPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 3, 1, 4),
    _H3cCBQoSAtmPvcCarExceedBytes_Type()
)
h3cCBQoSAtmPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcCarExceedBytes.setStatus("current")
_H3cCBQoSAtmPvcGtsRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcGtsRunInfoTable = _H3cCBQoSAtmPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcGtsRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcGtsRunInfoEntry = _H3cCBQoSAtmPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1)
)
h3cCBQoSAtmPvcGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcGtsPassedPackets_Type = Counter64
_H3cCBQoSAtmPvcGtsPassedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcGtsPassedPackets = _H3cCBQoSAtmPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 1),
    _H3cCBQoSAtmPvcGtsPassedPackets_Type()
)
h3cCBQoSAtmPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsPassedPackets.setStatus("current")
_H3cCBQoSAtmPvcGtsPassedBytes_Type = Counter64
_H3cCBQoSAtmPvcGtsPassedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcGtsPassedBytes = _H3cCBQoSAtmPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 2),
    _H3cCBQoSAtmPvcGtsPassedBytes_Type()
)
h3cCBQoSAtmPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsPassedBytes.setStatus("current")
_H3cCBQoSAtmPvcGtsDiscardedPackets_Type = Counter64
_H3cCBQoSAtmPvcGtsDiscardedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcGtsDiscardedPackets = _H3cCBQoSAtmPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 3),
    _H3cCBQoSAtmPvcGtsDiscardedPackets_Type()
)
h3cCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsDiscardedPackets.setStatus("current")
_H3cCBQoSAtmPvcGtsDiscardedBytes_Type = Counter64
_H3cCBQoSAtmPvcGtsDiscardedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcGtsDiscardedBytes = _H3cCBQoSAtmPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 4),
    _H3cCBQoSAtmPvcGtsDiscardedBytes_Type()
)
h3cCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsDiscardedBytes.setStatus("current")
_H3cCBQoSAtmPvcGtsDelayedPackets_Type = Counter64
_H3cCBQoSAtmPvcGtsDelayedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcGtsDelayedPackets = _H3cCBQoSAtmPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 5),
    _H3cCBQoSAtmPvcGtsDelayedPackets_Type()
)
h3cCBQoSAtmPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsDelayedPackets.setStatus("current")
_H3cCBQoSAtmPvcGtsDelayedBytes_Type = Counter64
_H3cCBQoSAtmPvcGtsDelayedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcGtsDelayedBytes = _H3cCBQoSAtmPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 6),
    _H3cCBQoSAtmPvcGtsDelayedBytes_Type()
)
h3cCBQoSAtmPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsDelayedBytes.setStatus("current")
_H3cCBQoSAtmPvcGtsQueueSize_Type = Integer32
_H3cCBQoSAtmPvcGtsQueueSize_Object = MibTableColumn
h3cCBQoSAtmPvcGtsQueueSize = _H3cCBQoSAtmPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 4, 1, 7),
    _H3cCBQoSAtmPvcGtsQueueSize_Type()
)
h3cCBQoSAtmPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcGtsQueueSize.setStatus("current")
_H3cCBQoSAtmPvcRemarkRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcRemarkRunInfoTable = _H3cCBQoSAtmPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcRemarkRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcRemarkRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcRemarkRunInfoEntry = _H3cCBQoSAtmPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 5, 1)
)
h3cCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcRemarkRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcRemarkedPackets_Type = Counter64
_H3cCBQoSAtmPvcRemarkedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcRemarkedPackets = _H3cCBQoSAtmPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 5, 1, 1),
    _H3cCBQoSAtmPvcRemarkedPackets_Type()
)
h3cCBQoSAtmPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcRemarkedPackets.setStatus("current")
_H3cCBQoSAtmPvcQueueRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcQueueRunInfoTable = _H3cCBQoSAtmPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcQueueRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcQueueRunInfoEntry = _H3cCBQoSAtmPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1)
)
h3cCBQoSAtmPvcQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcQueueMatchedPackets_Type = Counter64
_H3cCBQoSAtmPvcQueueMatchedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcQueueMatchedPackets = _H3cCBQoSAtmPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1, 1),
    _H3cCBQoSAtmPvcQueueMatchedPackets_Type()
)
h3cCBQoSAtmPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueMatchedPackets.setStatus("current")
_H3cCBQoSAtmPvcQueueMatchedBytes_Type = Counter64
_H3cCBQoSAtmPvcQueueMatchedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcQueueMatchedBytes = _H3cCBQoSAtmPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1, 2),
    _H3cCBQoSAtmPvcQueueMatchedBytes_Type()
)
h3cCBQoSAtmPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueMatchedBytes.setStatus("current")
_H3cCBQoSAtmPvcQueueEnqueuedPackets_Type = Counter64
_H3cCBQoSAtmPvcQueueEnqueuedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcQueueEnqueuedPackets = _H3cCBQoSAtmPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1, 3),
    _H3cCBQoSAtmPvcQueueEnqueuedPackets_Type()
)
h3cCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueEnqueuedPackets.setStatus("current")
_H3cCBQoSAtmPvcQueueEnqueuedBytes_Type = Counter64
_H3cCBQoSAtmPvcQueueEnqueuedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcQueueEnqueuedBytes = _H3cCBQoSAtmPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1, 4),
    _H3cCBQoSAtmPvcQueueEnqueuedBytes_Type()
)
h3cCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueEnqueuedBytes.setStatus("current")
_H3cCBQoSAtmPvcQueueDiscardedPackets_Type = Counter64
_H3cCBQoSAtmPvcQueueDiscardedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcQueueDiscardedPackets = _H3cCBQoSAtmPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1, 5),
    _H3cCBQoSAtmPvcQueueDiscardedPackets_Type()
)
h3cCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueDiscardedPackets.setStatus("current")
_H3cCBQoSAtmPvcQueueDiscardedBytes_Type = Counter64
_H3cCBQoSAtmPvcQueueDiscardedBytes_Object = MibTableColumn
h3cCBQoSAtmPvcQueueDiscardedBytes = _H3cCBQoSAtmPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 6, 1, 6),
    _H3cCBQoSAtmPvcQueueDiscardedBytes_Type()
)
h3cCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcQueueDiscardedBytes.setStatus("current")
_H3cCBQoSAtmPvcWredRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcWredRunInfoTable = _H3cCBQoSAtmPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcWredRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcWredRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcWredRunInfoEntry = _H3cCBQoSAtmPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 7, 1)
)
h3cCBQoSAtmPvcWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcWredRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcWredRandomDiscardedPackets_Type = Counter64
_H3cCBQoSAtmPvcWredRandomDiscardedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcWredRandomDiscardedPackets = _H3cCBQoSAtmPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 7, 1, 1),
    _H3cCBQoSAtmPvcWredRandomDiscardedPackets_Type()
)
h3cCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcWredRandomDiscardedPackets.setStatus("current")
_H3cCBQoSAtmPvcWredTailDiscardedPackets_Type = Counter64
_H3cCBQoSAtmPvcWredTailDiscardedPackets_Object = MibTableColumn
h3cCBQoSAtmPvcWredTailDiscardedPackets = _H3cCBQoSAtmPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 7, 1, 2),
    _H3cCBQoSAtmPvcWredTailDiscardedPackets_Type()
)
h3cCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcWredTailDiscardedPackets.setStatus("current")
_H3cCBQoSAtmPvcAccountingRunInfoTable_Object = MibTable
h3cCBQoSAtmPvcAccountingRunInfoTable = _H3cCBQoSAtmPvcAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcAccountingRunInfoTable.setStatus("current")
_H3cCBQoSAtmPvcAccountingRunInfoEntry_Object = MibTableRow
h3cCBQoSAtmPvcAccountingRunInfoEntry = _H3cCBQoSAtmPvcAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 8, 1)
)
h3cCBQoSAtmPvcAccountingRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcAccountingRunInfoEntry.setStatus("current")
_H3cCBQoSAtmPvcAccountingPackets_Type = Counter64
_H3cCBQoSAtmPvcAccountingPackets_Object = MibTableColumn
h3cCBQoSAtmPvcAccountingPackets = _H3cCBQoSAtmPvcAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 8, 1, 1),
    _H3cCBQoSAtmPvcAccountingPackets_Type()
)
h3cCBQoSAtmPvcAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcAccountingPackets.setStatus("current")
_H3cCBQoSAtmPvcAccountingBytes_Type = Counter64
_H3cCBQoSAtmPvcAccountingBytes_Object = MibTableColumn
h3cCBQoSAtmPvcAccountingBytes = _H3cCBQoSAtmPvcAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 2, 8, 1, 2),
    _H3cCBQoSAtmPvcAccountingBytes_Type()
)
h3cCBQoSAtmPvcAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAtmPvcAccountingBytes.setStatus("current")
_H3cCBQoSFrPvcStaticsObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSFrPvcStaticsObjects = _H3cCBQoSFrPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3)
)
_H3cCBQoSFrPvcCbqRunInfoTable_Object = MibTable
h3cCBQoSFrPvcCbqRunInfoTable = _H3cCBQoSFrPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcCbqRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcCbqRunInfoEntry = _H3cCBQoSFrPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1)
)
h3cCBQoSFrPvcCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcCbqQueueSize_Type = Integer32
_H3cCBQoSFrPvcCbqQueueSize_Object = MibTableColumn
h3cCBQoSFrPvcCbqQueueSize = _H3cCBQoSFrPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 1),
    _H3cCBQoSFrPvcCbqQueueSize_Type()
)
h3cCBQoSFrPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqQueueSize.setStatus("current")
_H3cCBQoSFrPvcCbqDiscard_Type = Counter64
_H3cCBQoSFrPvcCbqDiscard_Object = MibTableColumn
h3cCBQoSFrPvcCbqDiscard = _H3cCBQoSFrPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 2),
    _H3cCBQoSFrPvcCbqDiscard_Type()
)
h3cCBQoSFrPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqDiscard.setStatus("current")
_H3cCBQoSFrPvcCbqEfQueueSize_Type = Integer32
_H3cCBQoSFrPvcCbqEfQueueSize_Object = MibTableColumn
h3cCBQoSFrPvcCbqEfQueueSize = _H3cCBQoSFrPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 3),
    _H3cCBQoSFrPvcCbqEfQueueSize_Type()
)
h3cCBQoSFrPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqEfQueueSize.setStatus("current")
_H3cCBQoSFrPvcCbqAfQueueSize_Type = Integer32
_H3cCBQoSFrPvcCbqAfQueueSize_Object = MibTableColumn
h3cCBQoSFrPvcCbqAfQueueSize = _H3cCBQoSFrPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 4),
    _H3cCBQoSFrPvcCbqAfQueueSize_Type()
)
h3cCBQoSFrPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqAfQueueSize.setStatus("current")
_H3cCBQoSFrPvcCbqBeQueueSize_Type = Integer32
_H3cCBQoSFrPvcCbqBeQueueSize_Object = MibTableColumn
h3cCBQoSFrPvcCbqBeQueueSize = _H3cCBQoSFrPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 5),
    _H3cCBQoSFrPvcCbqBeQueueSize_Type()
)
h3cCBQoSFrPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqBeQueueSize.setStatus("current")
_H3cCBQoSFrPvcCbqBeActiveQueueNum_Type = Integer32
_H3cCBQoSFrPvcCbqBeActiveQueueNum_Object = MibTableColumn
h3cCBQoSFrPvcCbqBeActiveQueueNum = _H3cCBQoSFrPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 6),
    _H3cCBQoSFrPvcCbqBeActiveQueueNum_Type()
)
h3cCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqBeActiveQueueNum.setStatus("current")
_H3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Type = Integer32
_H3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
h3cCBQoSFrPvcCbqBeMaxActiveQueueNum = _H3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 7),
    _H3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Type()
)
h3cCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus("current")
_H3cCBQoSFrPvcCbqBeTotalQueueNum_Type = Integer32
_H3cCBQoSFrPvcCbqBeTotalQueueNum_Object = MibTableColumn
h3cCBQoSFrPvcCbqBeTotalQueueNum = _H3cCBQoSFrPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 8),
    _H3cCBQoSFrPvcCbqBeTotalQueueNum_Type()
)
h3cCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqBeTotalQueueNum.setStatus("current")
_H3cCBQoSFrPvcCbqAfAllocatedQueueNum_Type = Integer32
_H3cCBQoSFrPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
h3cCBQoSFrPvcCbqAfAllocatedQueueNum = _H3cCBQoSFrPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 1, 1, 9),
    _H3cCBQoSFrPvcCbqAfAllocatedQueueNum_Type()
)
h3cCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus("current")
_H3cCBQoSFrPvcClassMatchRunInfoTable_Object = MibTable
h3cCBQoSFrPvcClassMatchRunInfoTable = _H3cCBQoSFrPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcClassMatchRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcClassMatchRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcClassMatchRunInfoEntry = _H3cCBQoSFrPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 2, 1)
)
h3cCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcClassMatchRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcClassMatchedPackets_Type = Counter64
_H3cCBQoSFrPvcClassMatchedPackets_Object = MibTableColumn
h3cCBQoSFrPvcClassMatchedPackets = _H3cCBQoSFrPvcClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 2, 1, 1),
    _H3cCBQoSFrPvcClassMatchedPackets_Type()
)
h3cCBQoSFrPvcClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcClassMatchedPackets.setStatus("current")
_H3cCBQoSFrPvcClassMatchedBytes_Type = Counter64
_H3cCBQoSFrPvcClassMatchedBytes_Object = MibTableColumn
h3cCBQoSFrPvcClassMatchedBytes = _H3cCBQoSFrPvcClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 2, 1, 2),
    _H3cCBQoSFrPvcClassMatchedBytes_Type()
)
h3cCBQoSFrPvcClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcClassMatchedBytes.setStatus("current")
_H3cCBQoSFrPvcClassAverageRate_Type = Counter64
_H3cCBQoSFrPvcClassAverageRate_Object = MibTableColumn
h3cCBQoSFrPvcClassAverageRate = _H3cCBQoSFrPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 2, 1, 3),
    _H3cCBQoSFrPvcClassAverageRate_Type()
)
h3cCBQoSFrPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcClassAverageRate.setStatus("current")
_H3cCBQoSFrPvcCarRunInfoTable_Object = MibTable
h3cCBQoSFrPvcCarRunInfoTable = _H3cCBQoSFrPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCarRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcCarRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcCarRunInfoEntry = _H3cCBQoSFrPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 3, 1)
)
h3cCBQoSFrPvcCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCarRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcCarConformPackets_Type = Counter64
_H3cCBQoSFrPvcCarConformPackets_Object = MibTableColumn
h3cCBQoSFrPvcCarConformPackets = _H3cCBQoSFrPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 3, 1, 1),
    _H3cCBQoSFrPvcCarConformPackets_Type()
)
h3cCBQoSFrPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCarConformPackets.setStatus("current")
_H3cCBQoSFrPvcCarConformBytes_Type = Counter64
_H3cCBQoSFrPvcCarConformBytes_Object = MibTableColumn
h3cCBQoSFrPvcCarConformBytes = _H3cCBQoSFrPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 3, 1, 2),
    _H3cCBQoSFrPvcCarConformBytes_Type()
)
h3cCBQoSFrPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCarConformBytes.setStatus("current")
_H3cCBQoSFrPvcCarExceedPackets_Type = Counter64
_H3cCBQoSFrPvcCarExceedPackets_Object = MibTableColumn
h3cCBQoSFrPvcCarExceedPackets = _H3cCBQoSFrPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 3, 1, 3),
    _H3cCBQoSFrPvcCarExceedPackets_Type()
)
h3cCBQoSFrPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCarExceedPackets.setStatus("current")
_H3cCBQoSFrPvcCarExceedBytes_Type = Counter64
_H3cCBQoSFrPvcCarExceedBytes_Object = MibTableColumn
h3cCBQoSFrPvcCarExceedBytes = _H3cCBQoSFrPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 3, 1, 4),
    _H3cCBQoSFrPvcCarExceedBytes_Type()
)
h3cCBQoSFrPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcCarExceedBytes.setStatus("current")
_H3cCBQoSFrPvcGtsRunInfoTable_Object = MibTable
h3cCBQoSFrPvcGtsRunInfoTable = _H3cCBQoSFrPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcGtsRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcGtsRunInfoEntry = _H3cCBQoSFrPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1)
)
h3cCBQoSFrPvcGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcGtsPassedPackets_Type = Counter64
_H3cCBQoSFrPvcGtsPassedPackets_Object = MibTableColumn
h3cCBQoSFrPvcGtsPassedPackets = _H3cCBQoSFrPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 1),
    _H3cCBQoSFrPvcGtsPassedPackets_Type()
)
h3cCBQoSFrPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsPassedPackets.setStatus("current")
_H3cCBQoSFrPvcGtsPassedBytes_Type = Counter64
_H3cCBQoSFrPvcGtsPassedBytes_Object = MibTableColumn
h3cCBQoSFrPvcGtsPassedBytes = _H3cCBQoSFrPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 2),
    _H3cCBQoSFrPvcGtsPassedBytes_Type()
)
h3cCBQoSFrPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsPassedBytes.setStatus("current")
_H3cCBQoSFrPvcGtsDiscardedPackets_Type = Counter64
_H3cCBQoSFrPvcGtsDiscardedPackets_Object = MibTableColumn
h3cCBQoSFrPvcGtsDiscardedPackets = _H3cCBQoSFrPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 3),
    _H3cCBQoSFrPvcGtsDiscardedPackets_Type()
)
h3cCBQoSFrPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsDiscardedPackets.setStatus("current")
_H3cCBQoSFrPvcGtsDiscardedBytes_Type = Counter64
_H3cCBQoSFrPvcGtsDiscardedBytes_Object = MibTableColumn
h3cCBQoSFrPvcGtsDiscardedBytes = _H3cCBQoSFrPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 4),
    _H3cCBQoSFrPvcGtsDiscardedBytes_Type()
)
h3cCBQoSFrPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsDiscardedBytes.setStatus("current")
_H3cCBQoSFrPvcGtsDelayedPackets_Type = Counter64
_H3cCBQoSFrPvcGtsDelayedPackets_Object = MibTableColumn
h3cCBQoSFrPvcGtsDelayedPackets = _H3cCBQoSFrPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 5),
    _H3cCBQoSFrPvcGtsDelayedPackets_Type()
)
h3cCBQoSFrPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsDelayedPackets.setStatus("current")
_H3cCBQoSFrPvcGtsDelayedBytes_Type = Counter64
_H3cCBQoSFrPvcGtsDelayedBytes_Object = MibTableColumn
h3cCBQoSFrPvcGtsDelayedBytes = _H3cCBQoSFrPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 6),
    _H3cCBQoSFrPvcGtsDelayedBytes_Type()
)
h3cCBQoSFrPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsDelayedBytes.setStatus("current")
_H3cCBQoSFrPvcGtsQueueSize_Type = Integer32
_H3cCBQoSFrPvcGtsQueueSize_Object = MibTableColumn
h3cCBQoSFrPvcGtsQueueSize = _H3cCBQoSFrPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 4, 1, 7),
    _H3cCBQoSFrPvcGtsQueueSize_Type()
)
h3cCBQoSFrPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcGtsQueueSize.setStatus("current")
_H3cCBQoSFrPvcRemarkRunInfoTable_Object = MibTable
h3cCBQoSFrPvcRemarkRunInfoTable = _H3cCBQoSFrPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcRemarkRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcRemarkRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcRemarkRunInfoEntry = _H3cCBQoSFrPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 5, 1)
)
h3cCBQoSFrPvcRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcRemarkRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcRemarkedPackets_Type = Counter64
_H3cCBQoSFrPvcRemarkedPackets_Object = MibTableColumn
h3cCBQoSFrPvcRemarkedPackets = _H3cCBQoSFrPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 5, 1, 1),
    _H3cCBQoSFrPvcRemarkedPackets_Type()
)
h3cCBQoSFrPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcRemarkedPackets.setStatus("current")
_H3cCBQoSFrPvcQueueRunInfoTable_Object = MibTable
h3cCBQoSFrPvcQueueRunInfoTable = _H3cCBQoSFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcQueueRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcQueueRunInfoEntry = _H3cCBQoSFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1)
)
h3cCBQoSFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcQueueMatchedPackets_Type = Counter64
_H3cCBQoSFrPvcQueueMatchedPackets_Object = MibTableColumn
h3cCBQoSFrPvcQueueMatchedPackets = _H3cCBQoSFrPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1, 1),
    _H3cCBQoSFrPvcQueueMatchedPackets_Type()
)
h3cCBQoSFrPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueMatchedPackets.setStatus("current")
_H3cCBQoSFrPvcQueueMatchedBytes_Type = Counter64
_H3cCBQoSFrPvcQueueMatchedBytes_Object = MibTableColumn
h3cCBQoSFrPvcQueueMatchedBytes = _H3cCBQoSFrPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1, 2),
    _H3cCBQoSFrPvcQueueMatchedBytes_Type()
)
h3cCBQoSFrPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueMatchedBytes.setStatus("current")
_H3cCBQoSFrPvcQueueEnqueuedPackets_Type = Counter64
_H3cCBQoSFrPvcQueueEnqueuedPackets_Object = MibTableColumn
h3cCBQoSFrPvcQueueEnqueuedPackets = _H3cCBQoSFrPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1, 3),
    _H3cCBQoSFrPvcQueueEnqueuedPackets_Type()
)
h3cCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueEnqueuedPackets.setStatus("current")
_H3cCBQoSFrPvcQueueEnqueuedBytes_Type = Counter64
_H3cCBQoSFrPvcQueueEnqueuedBytes_Object = MibTableColumn
h3cCBQoSFrPvcQueueEnqueuedBytes = _H3cCBQoSFrPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1, 4),
    _H3cCBQoSFrPvcQueueEnqueuedBytes_Type()
)
h3cCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueEnqueuedBytes.setStatus("current")
_H3cCBQoSFrPvcQueueDiscardedPackets_Type = Counter64
_H3cCBQoSFrPvcQueueDiscardedPackets_Object = MibTableColumn
h3cCBQoSFrPvcQueueDiscardedPackets = _H3cCBQoSFrPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1, 5),
    _H3cCBQoSFrPvcQueueDiscardedPackets_Type()
)
h3cCBQoSFrPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueDiscardedPackets.setStatus("current")
_H3cCBQoSFrPvcQueueDiscardedBytes_Type = Counter64
_H3cCBQoSFrPvcQueueDiscardedBytes_Object = MibTableColumn
h3cCBQoSFrPvcQueueDiscardedBytes = _H3cCBQoSFrPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 6, 1, 6),
    _H3cCBQoSFrPvcQueueDiscardedBytes_Type()
)
h3cCBQoSFrPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcQueueDiscardedBytes.setStatus("current")
_H3cCBQoSFrPvcWredRunInfoTable_Object = MibTable
h3cCBQoSFrPvcWredRunInfoTable = _H3cCBQoSFrPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcWredRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcWredRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcWredRunInfoEntry = _H3cCBQoSFrPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 7, 1)
)
h3cCBQoSFrPvcWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcWredRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcWredRandomDiscardedPackets_Type = Counter64
_H3cCBQoSFrPvcWredRandomDiscardedPackets_Object = MibTableColumn
h3cCBQoSFrPvcWredRandomDiscardedPackets = _H3cCBQoSFrPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 7, 1, 1),
    _H3cCBQoSFrPvcWredRandomDiscardedPackets_Type()
)
h3cCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcWredRandomDiscardedPackets.setStatus("current")
_H3cCBQoSFrPvcWredTailDiscardedPackets_Type = Counter64
_H3cCBQoSFrPvcWredTailDiscardedPackets_Object = MibTableColumn
h3cCBQoSFrPvcWredTailDiscardedPackets = _H3cCBQoSFrPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 7, 1, 2),
    _H3cCBQoSFrPvcWredTailDiscardedPackets_Type()
)
h3cCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcWredTailDiscardedPackets.setStatus("current")
_H3cCBQoSFrPvcAccountingRunInfoTable_Object = MibTable
h3cCBQoSFrPvcAccountingRunInfoTable = _H3cCBQoSFrPvcAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcAccountingRunInfoTable.setStatus("current")
_H3cCBQoSFrPvcAccountingRunInfoEntry_Object = MibTableRow
h3cCBQoSFrPvcAccountingRunInfoEntry = _H3cCBQoSFrPvcAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 8, 1)
)
h3cCBQoSFrPvcAccountingRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcAccountingRunInfoEntry.setStatus("current")
_H3cCBQoSFrPvcAccountingPackets_Type = Counter64
_H3cCBQoSFrPvcAccountingPackets_Object = MibTableColumn
h3cCBQoSFrPvcAccountingPackets = _H3cCBQoSFrPvcAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 8, 1, 1),
    _H3cCBQoSFrPvcAccountingPackets_Type()
)
h3cCBQoSFrPvcAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcAccountingPackets.setStatus("current")
_H3cCBQoSFrPvcAccountingBytes_Type = Counter64
_H3cCBQoSFrPvcAccountingBytes_Object = MibTableColumn
h3cCBQoSFrPvcAccountingBytes = _H3cCBQoSFrPvcAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 3, 8, 1, 2),
    _H3cCBQoSFrPvcAccountingBytes_Type()
)
h3cCBQoSFrPvcAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSFrPvcAccountingBytes.setStatus("current")
_H3cCBQoSVlanStaticsObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSVlanStaticsObjects = _H3cCBQoSVlanStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4)
)
_H3cCBQoSVlanClassMatchRunInfoTable_Object = MibTable
h3cCBQoSVlanClassMatchRunInfoTable = _H3cCBQoSVlanClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanClassMatchRunInfoTable.setStatus("current")
_H3cCBQoSVlanClassMatchRunInfoEntry_Object = MibTableRow
h3cCBQoSVlanClassMatchRunInfoEntry = _H3cCBQoSVlanClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 1, 1)
)
h3cCBQoSVlanClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyVlanid"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanClassMatchRunInfoEntry.setStatus("current")
_H3cCBQoSVlanClassMatchedPackets_Type = Counter64
_H3cCBQoSVlanClassMatchedPackets_Object = MibTableColumn
h3cCBQoSVlanClassMatchedPackets = _H3cCBQoSVlanClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 1, 1, 1),
    _H3cCBQoSVlanClassMatchedPackets_Type()
)
h3cCBQoSVlanClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSVlanClassMatchedPackets.setStatus("current")
_H3cCBQoSVlanAccountingRunInfoTable_Object = MibTable
h3cCBQoSVlanAccountingRunInfoTable = _H3cCBQoSVlanAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanAccountingRunInfoTable.setStatus("current")
_H3cCBQoSVlanAccountingRunInfoEntry_Object = MibTableRow
h3cCBQoSVlanAccountingRunInfoEntry = _H3cCBQoSVlanAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 2, 1)
)
h3cCBQoSVlanAccountingRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyVlanid"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanAccountingRunInfoEntry.setStatus("current")
_H3cCBQoSVlanAccountingPackets_Type = Counter64
_H3cCBQoSVlanAccountingPackets_Object = MibTableColumn
h3cCBQoSVlanAccountingPackets = _H3cCBQoSVlanAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 2, 1, 1),
    _H3cCBQoSVlanAccountingPackets_Type()
)
h3cCBQoSVlanAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSVlanAccountingPackets.setStatus("current")
_H3cCBQoSVlanAccountingBytes_Type = Counter64
_H3cCBQoSVlanAccountingBytes_Object = MibTableColumn
h3cCBQoSVlanAccountingBytes = _H3cCBQoSVlanAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 4, 2, 1, 2),
    _H3cCBQoSVlanAccountingBytes_Type()
)
h3cCBQoSVlanAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSVlanAccountingBytes.setStatus("current")
_H3cCBQoSApplyPolicyIndexObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSApplyPolicyIndexObjects = _H3cCBQoSApplyPolicyIndexObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5)
)
_H3cCBQoSApplyObjectTable_Object = MibTable
h3cCBQoSApplyObjectTable = _H3cCBQoSApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectTable.setStatus("current")
_H3cCBQoSApplyObjectEntry_Object = MibTableRow
h3cCBQoSApplyObjectEntry = _H3cCBQoSApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1)
)
h3cCBQoSApplyObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectEntry.setStatus("current")
_H3cCBQoSApplyObjectIndex_Type = Unsigned32
_H3cCBQoSApplyObjectIndex_Object = MibTableColumn
h3cCBQoSApplyObjectIndex = _H3cCBQoSApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 1),
    _H3cCBQoSApplyObjectIndex_Type()
)
h3cCBQoSApplyObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectIndex.setStatus("current")
_H3cCBQoSApplyObjectType_Type = ApplyObjectType
_H3cCBQoSApplyObjectType_Object = MibTableColumn
h3cCBQoSApplyObjectType = _H3cCBQoSApplyObjectType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 2),
    _H3cCBQoSApplyObjectType_Type()
)
h3cCBQoSApplyObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectType.setStatus("current")
_H3cCBQoSApplyObjectDirection_Type = DirectionType
_H3cCBQoSApplyObjectDirection_Object = MibTableColumn
h3cCBQoSApplyObjectDirection = _H3cCBQoSApplyObjectDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 3),
    _H3cCBQoSApplyObjectDirection_Type()
)
h3cCBQoSApplyObjectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectDirection.setStatus("current")
_H3cCBQoSApplyObjectMainSite_Type = Unsigned32
_H3cCBQoSApplyObjectMainSite_Object = MibTableColumn
h3cCBQoSApplyObjectMainSite = _H3cCBQoSApplyObjectMainSite_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 4),
    _H3cCBQoSApplyObjectMainSite_Type()
)
h3cCBQoSApplyObjectMainSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectMainSite.setStatus("current")
_H3cCBQoSApplyObjectSubChannel_Type = Unsigned32
_H3cCBQoSApplyObjectSubChannel_Object = MibTableColumn
h3cCBQoSApplyObjectSubChannel = _H3cCBQoSApplyObjectSubChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 5),
    _H3cCBQoSApplyObjectSubChannel_Type()
)
h3cCBQoSApplyObjectSubChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectSubChannel.setStatus("current")
_H3cCBQoSApplyObjectSubClass_Type = Unsigned32
_H3cCBQoSApplyObjectSubClass_Object = MibTableColumn
h3cCBQoSApplyObjectSubClass = _H3cCBQoSApplyObjectSubClass_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 6),
    _H3cCBQoSApplyObjectSubClass_Type()
)
h3cCBQoSApplyObjectSubClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectSubClass.setStatus("current")
_H3cCBQoSApplyObjectSubClassSec_Type = Unsigned32
_H3cCBQoSApplyObjectSubClassSec_Object = MibTableColumn
h3cCBQoSApplyObjectSubClassSec = _H3cCBQoSApplyObjectSubClassSec_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 1, 1, 7),
    _H3cCBQoSApplyObjectSubClassSec_Type()
)
h3cCBQoSApplyObjectSubClassSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyObjectSubClassSec.setStatus("current")
_H3cCBQoSIntApplyObjectTable_Object = MibTable
h3cCBQoSIntApplyObjectTable = _H3cCBQoSIntApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSIntApplyObjectTable.setStatus("current")
_H3cCBQoSIntApplyObjectEntry_Object = MibTableRow
h3cCBQoSIntApplyObjectEntry = _H3cCBQoSIntApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 2, 1)
)
h3cCBQoSIntApplyObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIntApplyObjectIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSIntApplyObjectEntry.setStatus("current")
_H3cCBQoSIntApplyObjectIfIndex_Type = Unsigned32
_H3cCBQoSIntApplyObjectIfIndex_Object = MibTableColumn
h3cCBQoSIntApplyObjectIfIndex = _H3cCBQoSIntApplyObjectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 2, 1, 1),
    _H3cCBQoSIntApplyObjectIfIndex_Type()
)
h3cCBQoSIntApplyObjectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSIntApplyObjectIfIndex.setStatus("current")
_H3cCBQoSIntApplyObjectIndex_Type = Unsigned32
_H3cCBQoSIntApplyObjectIndex_Object = MibTableColumn
h3cCBQoSIntApplyObjectIndex = _H3cCBQoSIntApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 2, 1, 2),
    _H3cCBQoSIntApplyObjectIndex_Type()
)
h3cCBQoSIntApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSIntApplyObjectIndex.setStatus("current")
_H3cCBQoSVlanApplyObjectTable_Object = MibTable
h3cCBQoSVlanApplyObjectTable = _H3cCBQoSVlanApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyObjectTable.setStatus("current")
_H3cCBQoSVlanApplyObjectEntry_Object = MibTableRow
h3cCBQoSVlanApplyObjectEntry = _H3cCBQoSVlanApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 3, 1)
)
h3cCBQoSVlanApplyObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyObjectVlanID"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyObjectEntry.setStatus("current")


class _H3cCBQoSVlanApplyObjectVlanID_Type(Unsigned32):
    """Custom type h3cCBQoSVlanApplyObjectVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cCBQoSVlanApplyObjectVlanID_Type.__name__ = "Unsigned32"
_H3cCBQoSVlanApplyObjectVlanID_Object = MibTableColumn
h3cCBQoSVlanApplyObjectVlanID = _H3cCBQoSVlanApplyObjectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 3, 1, 1),
    _H3cCBQoSVlanApplyObjectVlanID_Type()
)
h3cCBQoSVlanApplyObjectVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyObjectVlanID.setStatus("current")
_H3cCBQoSVlanApplyObjectIndex_Type = Unsigned32
_H3cCBQoSVlanApplyObjectIndex_Object = MibTableColumn
h3cCBQoSVlanApplyObjectIndex = _H3cCBQoSVlanApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 3, 1, 2),
    _H3cCBQoSVlanApplyObjectIndex_Type()
)
h3cCBQoSVlanApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSVlanApplyObjectIndex.setStatus("current")
_H3cCBQoSPvcApplyObjectTable_Object = MibTable
h3cCBQoSPvcApplyObjectTable = _H3cCBQoSPvcApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSPvcApplyObjectTable.setStatus("current")
_H3cCBQoSPvcApplyObjectEntry_Object = MibTableRow
h3cCBQoSPvcApplyObjectEntry = _H3cCBQoSPvcApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 4, 1)
)
h3cCBQoSPvcApplyObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPvcApplyObjectIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPvcApplyObjectPvcID"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    h3cCBQoSPvcApplyObjectEntry.setStatus("current")
_H3cCBQoSPvcApplyObjectIfIndex_Type = Unsigned32
_H3cCBQoSPvcApplyObjectIfIndex_Object = MibTableColumn
h3cCBQoSPvcApplyObjectIfIndex = _H3cCBQoSPvcApplyObjectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 4, 1, 1),
    _H3cCBQoSPvcApplyObjectIfIndex_Type()
)
h3cCBQoSPvcApplyObjectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSPvcApplyObjectIfIndex.setStatus("current")
_H3cCBQoSPvcApplyObjectPvcID_Type = Unsigned32
_H3cCBQoSPvcApplyObjectPvcID_Object = MibTableColumn
h3cCBQoSPvcApplyObjectPvcID = _H3cCBQoSPvcApplyObjectPvcID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 4, 1, 2),
    _H3cCBQoSPvcApplyObjectPvcID_Type()
)
h3cCBQoSPvcApplyObjectPvcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSPvcApplyObjectPvcID.setStatus("current")
_H3cCBQoSPvcApplyObjectIndex_Type = Unsigned32
_H3cCBQoSPvcApplyObjectIndex_Object = MibTableColumn
h3cCBQoSPvcApplyObjectIndex = _H3cCBQoSPvcApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 4, 1, 3),
    _H3cCBQoSPvcApplyObjectIndex_Type()
)
h3cCBQoSPvcApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSPvcApplyObjectIndex.setStatus("current")
_H3cCBQoSNestPolicyApplyObjectTable_Object = MibTable
h3cCBQoSNestPolicyApplyObjectTable = _H3cCBQoSNestPolicyApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyApplyObjectTable.setStatus("current")
_H3cCBQoSNestPolicyApplyObjectEntry_Object = MibTableRow
h3cCBQoSNestPolicyApplyObjectEntry = _H3cCBQoSNestPolicyApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 5, 1)
)
h3cCBQoSNestPolicyApplyObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSNestPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyApplyObjectEntry.setStatus("current")
_H3cCBQoSNestPolicyClassIndex_Type = Unsigned32
_H3cCBQoSNestPolicyClassIndex_Object = MibTableColumn
h3cCBQoSNestPolicyClassIndex = _H3cCBQoSNestPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 5, 1, 1),
    _H3cCBQoSNestPolicyClassIndex_Type()
)
h3cCBQoSNestPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyClassIndex.setStatus("current")
_H3cCBQoSNestPolicyApplyObjectIndex_Type = Unsigned32
_H3cCBQoSNestPolicyApplyObjectIndex_Object = MibTableColumn
h3cCBQoSNestPolicyApplyObjectIndex = _H3cCBQoSNestPolicyApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 5, 5, 1, 2),
    _H3cCBQoSNestPolicyApplyObjectIndex_Type()
)
h3cCBQoSNestPolicyApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSNestPolicyApplyObjectIndex.setStatus("current")
_H3cCBQoSStaticsObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSStaticsObjects = _H3cCBQoSStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6)
)
_H3cCBQoSCbqRunInfoTable_Object = MibTable
h3cCBQoSCbqRunInfoTable = _H3cCBQoSCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    h3cCBQoSCbqRunInfoTable.setStatus("current")
_H3cCBQoSCbqRunInfoEntry_Object = MibTableRow
h3cCBQoSCbqRunInfoEntry = _H3cCBQoSCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1)
)
h3cCBQoSCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSCbqRunInfoEntry.setStatus("current")
_H3cCBQoSCbqQueueSize_Type = Integer32
_H3cCBQoSCbqQueueSize_Object = MibTableColumn
h3cCBQoSCbqQueueSize = _H3cCBQoSCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 1),
    _H3cCBQoSCbqQueueSize_Type()
)
h3cCBQoSCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqQueueSize.setStatus("current")
_H3cCBQoSCbqDiscard_Type = Counter64
_H3cCBQoSCbqDiscard_Object = MibTableColumn
h3cCBQoSCbqDiscard = _H3cCBQoSCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 2),
    _H3cCBQoSCbqDiscard_Type()
)
h3cCBQoSCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqDiscard.setStatus("current")
_H3cCBQoSCbqEfQueueSize_Type = Integer32
_H3cCBQoSCbqEfQueueSize_Object = MibTableColumn
h3cCBQoSCbqEfQueueSize = _H3cCBQoSCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 3),
    _H3cCBQoSCbqEfQueueSize_Type()
)
h3cCBQoSCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqEfQueueSize.setStatus("current")
_H3cCBQoSCbqAfQueueSize_Type = Integer32
_H3cCBQoSCbqAfQueueSize_Object = MibTableColumn
h3cCBQoSCbqAfQueueSize = _H3cCBQoSCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 4),
    _H3cCBQoSCbqAfQueueSize_Type()
)
h3cCBQoSCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqAfQueueSize.setStatus("current")
_H3cCBQoSCbqBeQueueSize_Type = Integer32
_H3cCBQoSCbqBeQueueSize_Object = MibTableColumn
h3cCBQoSCbqBeQueueSize = _H3cCBQoSCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 5),
    _H3cCBQoSCbqBeQueueSize_Type()
)
h3cCBQoSCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqBeQueueSize.setStatus("current")
_H3cCBQoSCbqBeActiveQueueNum_Type = Integer32
_H3cCBQoSCbqBeActiveQueueNum_Object = MibTableColumn
h3cCBQoSCbqBeActiveQueueNum = _H3cCBQoSCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 6),
    _H3cCBQoSCbqBeActiveQueueNum_Type()
)
h3cCBQoSCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqBeActiveQueueNum.setStatus("current")
_H3cCBQoSCbqBeMaxActiveQueueNum_Type = Integer32
_H3cCBQoSCbqBeMaxActiveQueueNum_Object = MibTableColumn
h3cCBQoSCbqBeMaxActiveQueueNum = _H3cCBQoSCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 7),
    _H3cCBQoSCbqBeMaxActiveQueueNum_Type()
)
h3cCBQoSCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqBeMaxActiveQueueNum.setStatus("current")
_H3cCBQoSCbqBeTotalQueueNum_Type = Integer32
_H3cCBQoSCbqBeTotalQueueNum_Object = MibTableColumn
h3cCBQoSCbqBeTotalQueueNum = _H3cCBQoSCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 8),
    _H3cCBQoSCbqBeTotalQueueNum_Type()
)
h3cCBQoSCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqBeTotalQueueNum.setStatus("current")
_H3cCBQoSCbqAfAllocatedQueueNum_Type = Integer32
_H3cCBQoSCbqAfAllocatedQueueNum_Object = MibTableColumn
h3cCBQoSCbqAfAllocatedQueueNum = _H3cCBQoSCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 1, 1, 9),
    _H3cCBQoSCbqAfAllocatedQueueNum_Type()
)
h3cCBQoSCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCbqAfAllocatedQueueNum.setStatus("current")
_H3cCBQoSClassMatchRunInfoTable_Object = MibTable
h3cCBQoSClassMatchRunInfoTable = _H3cCBQoSClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    h3cCBQoSClassMatchRunInfoTable.setStatus("current")
_H3cCBQoSClassMatchRunInfoEntry_Object = MibTableRow
h3cCBQoSClassMatchRunInfoEntry = _H3cCBQoSClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1)
)
h3cCBQoSClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSClassMatchRunInfoEntry.setStatus("current")
_H3cCBQoSClassMatchedPackets_Type = Counter64
_H3cCBQoSClassMatchedPackets_Object = MibTableColumn
h3cCBQoSClassMatchedPackets = _H3cCBQoSClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 1),
    _H3cCBQoSClassMatchedPackets_Type()
)
h3cCBQoSClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassMatchedPackets.setStatus("current")
_H3cCBQoSClassMatchedBytes_Type = Counter64
_H3cCBQoSClassMatchedBytes_Object = MibTableColumn
h3cCBQoSClassMatchedBytes = _H3cCBQoSClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 2),
    _H3cCBQoSClassMatchedBytes_Type()
)
h3cCBQoSClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassMatchedBytes.setStatus("current")
_H3cCBQoSClassFwdPktpps_Type = Unsigned32
_H3cCBQoSClassFwdPktpps_Object = MibTableColumn
h3cCBQoSClassFwdPktpps = _H3cCBQoSClassFwdPktpps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 3),
    _H3cCBQoSClassFwdPktpps_Type()
)
h3cCBQoSClassFwdPktpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassFwdPktpps.setStatus("current")
_H3cCBQoSClassFwdPktbps_Type = Unsigned32
_H3cCBQoSClassFwdPktbps_Object = MibTableColumn
h3cCBQoSClassFwdPktbps = _H3cCBQoSClassFwdPktbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 4),
    _H3cCBQoSClassFwdPktbps_Type()
)
h3cCBQoSClassFwdPktbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassFwdPktbps.setStatus("current")
_H3cCBQoSClassDropPktpps_Type = Unsigned32
_H3cCBQoSClassDropPktpps_Object = MibTableColumn
h3cCBQoSClassDropPktpps = _H3cCBQoSClassDropPktpps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 5),
    _H3cCBQoSClassDropPktpps_Type()
)
h3cCBQoSClassDropPktpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassDropPktpps.setStatus("current")
_H3cCBQoSClassDropPktbps_Type = Unsigned32
_H3cCBQoSClassDropPktbps_Object = MibTableColumn
h3cCBQoSClassDropPktbps = _H3cCBQoSClassDropPktbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 6),
    _H3cCBQoSClassDropPktbps_Type()
)
h3cCBQoSClassDropPktbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassDropPktbps.setStatus("current")
_H3cCBQoSClassFlowStatInterval_Type = Unsigned32
_H3cCBQoSClassFlowStatInterval_Object = MibTableColumn
h3cCBQoSClassFlowStatInterval = _H3cCBQoSClassFlowStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 7),
    _H3cCBQoSClassFlowStatInterval_Type()
)
h3cCBQoSClassFlowStatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassFlowStatInterval.setStatus("current")


class _H3cCBQoSClassBehaviorStatus_Type(Integer32):
    """Custom type h3cCBQoSClassBehaviorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_H3cCBQoSClassBehaviorStatus_Type.__name__ = "Integer32"
_H3cCBQoSClassBehaviorStatus_Object = MibTableColumn
h3cCBQoSClassBehaviorStatus = _H3cCBQoSClassBehaviorStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 2, 1, 8),
    _H3cCBQoSClassBehaviorStatus_Type()
)
h3cCBQoSClassBehaviorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSClassBehaviorStatus.setStatus("current")
_H3cCBQoSCarRunInfoTable_Object = MibTable
h3cCBQoSCarRunInfoTable = _H3cCBQoSCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3)
)
if mibBuilder.loadTexts:
    h3cCBQoSCarRunInfoTable.setStatus("current")
_H3cCBQoSCarRunInfoEntry_Object = MibTableRow
h3cCBQoSCarRunInfoEntry = _H3cCBQoSCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1)
)
h3cCBQoSCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSCarRunInfoEntry.setStatus("current")
_H3cCBQoSCarGreenPackets_Type = Counter64
_H3cCBQoSCarGreenPackets_Object = MibTableColumn
h3cCBQoSCarGreenPackets = _H3cCBQoSCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1, 1),
    _H3cCBQoSCarGreenPackets_Type()
)
h3cCBQoSCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarGreenPackets.setStatus("current")
_H3cCBQoSCarGreenBytes_Type = Counter64
_H3cCBQoSCarGreenBytes_Object = MibTableColumn
h3cCBQoSCarGreenBytes = _H3cCBQoSCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1, 2),
    _H3cCBQoSCarGreenBytes_Type()
)
h3cCBQoSCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarGreenBytes.setStatus("current")
_H3cCBQoSCarRedPackets_Type = Counter64
_H3cCBQoSCarRedPackets_Object = MibTableColumn
h3cCBQoSCarRedPackets = _H3cCBQoSCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1, 3),
    _H3cCBQoSCarRedPackets_Type()
)
h3cCBQoSCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarRedPackets.setStatus("current")
_H3cCBQoSCarRedBytes_Type = Counter64
_H3cCBQoSCarRedBytes_Object = MibTableColumn
h3cCBQoSCarRedBytes = _H3cCBQoSCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1, 4),
    _H3cCBQoSCarRedBytes_Type()
)
h3cCBQoSCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarRedBytes.setStatus("current")
_H3cCBQoSCarYellowPackets_Type = Counter64
_H3cCBQoSCarYellowPackets_Object = MibTableColumn
h3cCBQoSCarYellowPackets = _H3cCBQoSCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1, 5),
    _H3cCBQoSCarYellowPackets_Type()
)
h3cCBQoSCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarYellowPackets.setStatus("current")
_H3cCBQoSCarYellowBytes_Type = Counter64
_H3cCBQoSCarYellowBytes_Object = MibTableColumn
h3cCBQoSCarYellowBytes = _H3cCBQoSCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 3, 1, 6),
    _H3cCBQoSCarYellowBytes_Type()
)
h3cCBQoSCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSCarYellowBytes.setStatus("current")
_H3cCBQoSGtsRunInfoTable_Object = MibTable
h3cCBQoSGtsRunInfoTable = _H3cCBQoSGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    h3cCBQoSGtsRunInfoTable.setStatus("current")
_H3cCBQoSGtsRunInfoEntry_Object = MibTableRow
h3cCBQoSGtsRunInfoEntry = _H3cCBQoSGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1)
)
h3cCBQoSGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSGtsRunInfoEntry.setStatus("current")
_H3cCBQoSGtsPassedPackets_Type = Counter64
_H3cCBQoSGtsPassedPackets_Object = MibTableColumn
h3cCBQoSGtsPassedPackets = _H3cCBQoSGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 1),
    _H3cCBQoSGtsPassedPackets_Type()
)
h3cCBQoSGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsPassedPackets.setStatus("current")
_H3cCBQoSGtsPassedBytes_Type = Counter64
_H3cCBQoSGtsPassedBytes_Object = MibTableColumn
h3cCBQoSGtsPassedBytes = _H3cCBQoSGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 2),
    _H3cCBQoSGtsPassedBytes_Type()
)
h3cCBQoSGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsPassedBytes.setStatus("current")
_H3cCBQoSGtsDiscardedPackets_Type = Counter64
_H3cCBQoSGtsDiscardedPackets_Object = MibTableColumn
h3cCBQoSGtsDiscardedPackets = _H3cCBQoSGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 3),
    _H3cCBQoSGtsDiscardedPackets_Type()
)
h3cCBQoSGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsDiscardedPackets.setStatus("current")
_H3cCBQoSGtsDiscardedBytes_Type = Counter64
_H3cCBQoSGtsDiscardedBytes_Object = MibTableColumn
h3cCBQoSGtsDiscardedBytes = _H3cCBQoSGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 4),
    _H3cCBQoSGtsDiscardedBytes_Type()
)
h3cCBQoSGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsDiscardedBytes.setStatus("current")
_H3cCBQoSGtsDelayedPackets_Type = Counter64
_H3cCBQoSGtsDelayedPackets_Object = MibTableColumn
h3cCBQoSGtsDelayedPackets = _H3cCBQoSGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 5),
    _H3cCBQoSGtsDelayedPackets_Type()
)
h3cCBQoSGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsDelayedPackets.setStatus("current")
_H3cCBQoSGtsDelayedBytes_Type = Counter64
_H3cCBQoSGtsDelayedBytes_Object = MibTableColumn
h3cCBQoSGtsDelayedBytes = _H3cCBQoSGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 6),
    _H3cCBQoSGtsDelayedBytes_Type()
)
h3cCBQoSGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsDelayedBytes.setStatus("current")
_H3cCBQoSGtsQueueSize_Type = Integer32
_H3cCBQoSGtsQueueSize_Object = MibTableColumn
h3cCBQoSGtsQueueSize = _H3cCBQoSGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 4, 1, 7),
    _H3cCBQoSGtsQueueSize_Type()
)
h3cCBQoSGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSGtsQueueSize.setStatus("current")
_H3cCBQoSRemarkRunInfoTable_Object = MibTable
h3cCBQoSRemarkRunInfoTable = _H3cCBQoSRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    h3cCBQoSRemarkRunInfoTable.setStatus("current")
_H3cCBQoSRemarkRunInfoEntry_Object = MibTableRow
h3cCBQoSRemarkRunInfoEntry = _H3cCBQoSRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 5, 1)
)
h3cCBQoSRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSRemarkRunInfoEntry.setStatus("current")
_H3cCBQoSRemarkedPackets_Type = Counter64
_H3cCBQoSRemarkedPackets_Object = MibTableColumn
h3cCBQoSRemarkedPackets = _H3cCBQoSRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 5, 1, 1),
    _H3cCBQoSRemarkedPackets_Type()
)
h3cCBQoSRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSRemarkedPackets.setStatus("current")
_H3cCBQoSQueueRunInfoTable_Object = MibTable
h3cCBQoSQueueRunInfoTable = _H3cCBQoSQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    h3cCBQoSQueueRunInfoTable.setStatus("current")
_H3cCBQoSQueueRunInfoEntry_Object = MibTableRow
h3cCBQoSQueueRunInfoEntry = _H3cCBQoSQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1)
)
h3cCBQoSQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSQueueRunInfoEntry.setStatus("current")
_H3cCBQoSQueueMatchedPackets_Type = Counter64
_H3cCBQoSQueueMatchedPackets_Object = MibTableColumn
h3cCBQoSQueueMatchedPackets = _H3cCBQoSQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1, 1),
    _H3cCBQoSQueueMatchedPackets_Type()
)
h3cCBQoSQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSQueueMatchedPackets.setStatus("current")
_H3cCBQoSQueueMatchedBytes_Type = Counter64
_H3cCBQoSQueueMatchedBytes_Object = MibTableColumn
h3cCBQoSQueueMatchedBytes = _H3cCBQoSQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1, 2),
    _H3cCBQoSQueueMatchedBytes_Type()
)
h3cCBQoSQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSQueueMatchedBytes.setStatus("current")
_H3cCBQoSQueueEnqueuedPackets_Type = Counter64
_H3cCBQoSQueueEnqueuedPackets_Object = MibTableColumn
h3cCBQoSQueueEnqueuedPackets = _H3cCBQoSQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1, 3),
    _H3cCBQoSQueueEnqueuedPackets_Type()
)
h3cCBQoSQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSQueueEnqueuedPackets.setStatus("current")
_H3cCBQoSQueueEnqueuedBytes_Type = Counter64
_H3cCBQoSQueueEnqueuedBytes_Object = MibTableColumn
h3cCBQoSQueueEnqueuedBytes = _H3cCBQoSQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1, 4),
    _H3cCBQoSQueueEnqueuedBytes_Type()
)
h3cCBQoSQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSQueueEnqueuedBytes.setStatus("current")
_H3cCBQoSQueueDiscardedPackets_Type = Counter64
_H3cCBQoSQueueDiscardedPackets_Object = MibTableColumn
h3cCBQoSQueueDiscardedPackets = _H3cCBQoSQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1, 5),
    _H3cCBQoSQueueDiscardedPackets_Type()
)
h3cCBQoSQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSQueueDiscardedPackets.setStatus("current")
_H3cCBQoSQueueDiscardedBytes_Type = Counter64
_H3cCBQoSQueueDiscardedBytes_Object = MibTableColumn
h3cCBQoSQueueDiscardedBytes = _H3cCBQoSQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 6, 1, 6),
    _H3cCBQoSQueueDiscardedBytes_Type()
)
h3cCBQoSQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSQueueDiscardedBytes.setStatus("current")
_H3cCBQoSWredRunInfoTable_Object = MibTable
h3cCBQoSWredRunInfoTable = _H3cCBQoSWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    h3cCBQoSWredRunInfoTable.setStatus("current")
_H3cCBQoSWredRunInfoEntry_Object = MibTableRow
h3cCBQoSWredRunInfoEntry = _H3cCBQoSWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 7, 1)
)
h3cCBQoSWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    h3cCBQoSWredRunInfoEntry.setStatus("current")
_H3cCBQoSWredRandomDiscardedPackets_Type = Counter64
_H3cCBQoSWredRandomDiscardedPackets_Object = MibTableColumn
h3cCBQoSWredRandomDiscardedPackets = _H3cCBQoSWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 7, 1, 1),
    _H3cCBQoSWredRandomDiscardedPackets_Type()
)
h3cCBQoSWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSWredRandomDiscardedPackets.setStatus("current")
_H3cCBQoSWredTailDiscardedPackets_Type = Counter64
_H3cCBQoSWredTailDiscardedPackets_Object = MibTableColumn
h3cCBQoSWredTailDiscardedPackets = _H3cCBQoSWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 7, 1, 2),
    _H3cCBQoSWredTailDiscardedPackets_Type()
)
h3cCBQoSWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSWredTailDiscardedPackets.setStatus("current")
_H3cCBQoSAccountingRunInfoTable_Object = MibTable
h3cCBQoSAccountingRunInfoTable = _H3cCBQoSAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 8)
)
if mibBuilder.loadTexts:
    h3cCBQoSAccountingRunInfoTable.setStatus("current")
_H3cCBQoSAccountingRunInfoEntry_Object = MibTableRow
h3cCBQoSAccountingRunInfoEntry = _H3cCBQoSAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 8, 1)
)
h3cCBQoSAccountingRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSApplyObjectIndex"),
    (0, "A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    h3cCBQoSAccountingRunInfoEntry.setStatus("current")
_H3cCBQoSAccountingPackets_Type = Counter64
_H3cCBQoSAccountingPackets_Object = MibTableColumn
h3cCBQoSAccountingPackets = _H3cCBQoSAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 8, 1, 1),
    _H3cCBQoSAccountingPackets_Type()
)
h3cCBQoSAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAccountingPackets.setStatus("current")
_H3cCBQoSAccountingBytes_Type = Counter64
_H3cCBQoSAccountingBytes_Object = MibTableColumn
h3cCBQoSAccountingBytes = _H3cCBQoSAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 5, 6, 8, 1, 2),
    _H3cCBQoSAccountingBytes_Type()
)
h3cCBQoSAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSAccountingBytes.setStatus("current")
_H3cCBQoSApplyingStatusObjects_ObjectIdentity = ObjectIdentity
h3cCBQoSApplyingStatusObjects = _H3cCBQoSApplyingStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 6)
)


class _H3cCBQoSApplyingStatus_Type(Integer32):
    """Custom type h3cCBQoSApplyingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 1))
    )


_H3cCBQoSApplyingStatus_Type.__name__ = "Integer32"
_H3cCBQoSApplyingStatus_Object = MibScalar
h3cCBQoSApplyingStatus = _H3cCBQoSApplyingStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 6, 1),
    _H3cCBQoSApplyingStatus_Type()
)
h3cCBQoSApplyingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCBQoSApplyingStatus.setStatus("current")
_H3cCBQoSNotifications_ObjectIdentity = ObjectIdentity
h3cCBQoSNotifications = _H3cCBQoSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 7)
)
_H3cCBQoSNotificationsPrefix_ObjectIdentity = ObjectIdentity
h3cCBQoSNotificationsPrefix = _H3cCBQoSNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 7, 0)
)

# Managed Objects groups


# Notification objects

h3cCBQoSIfPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 7, 0, 1)
)
h3cCBQoSIfPolicyChanged.setObjects(
      *(("A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyIfIndex"),
        ("A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSIfApplyPolicyDirection"))
)
if mibBuilder.loadTexts:
    h3cCBQoSIfPolicyChanged.setStatus(
        "current"
    )

h3cCBQoSVlanPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 2, 1, 7, 0, 2)
)
h3cCBQoSVlanPolicyChanged.setObjects(
      *(("A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyVlanid"),
        ("A3COM-HUAWEI-CBQOS2-MIB", "h3cCBQoSVlanApplyPolicyDirection"))
)
if mibBuilder.loadTexts:
    h3cCBQoSVlanPolicyChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-CBQOS2-MIB",
    **{"MatchRuleType": MatchRuleType,
       "CarAction": CarAction,
       "RemarkType": RemarkType,
       "WredType": WredType,
       "QueueType": QueueType,
       "QueueBandwidthUnit": QueueBandwidthUnit,
       "DirectionType": DirectionType,
       "ApplyObjectType": ApplyObjectType,
       "h3cQos2": h3cQos2,
       "h3cCBQos2": h3cCBQos2,
       "h3cCBQoSObjects": h3cCBQoSObjects,
       "h3cCBQoSClassifierObjects": h3cCBQoSClassifierObjects,
       "h3cCBQoSClassifierIndexNext": h3cCBQoSClassifierIndexNext,
       "h3cCBQoSClassifierCfgInfoTable": h3cCBQoSClassifierCfgInfoTable,
       "h3cCBQoSClassifierCfgInfoEntry": h3cCBQoSClassifierCfgInfoEntry,
       "h3cCBQoSClassifierIndex": h3cCBQoSClassifierIndex,
       "h3cCBQoSClassifierName": h3cCBQoSClassifierName,
       "h3cCBQoSClassifierRuleCount": h3cCBQoSClassifierRuleCount,
       "h3cCBQoSClassifierOperator": h3cCBQoSClassifierOperator,
       "h3cCBQoSClassifierLayer": h3cCBQoSClassifierLayer,
       "h3cCBQoSClassifierType": h3cCBQoSClassifierType,
       "h3cCBQosClassifierMatchRuleNextIndex": h3cCBQosClassifierMatchRuleNextIndex,
       "h3cCBQoSClassifierRowStatus": h3cCBQoSClassifierRowStatus,
       "h3cCBQoSMatchRuleCfgInfoTable": h3cCBQoSMatchRuleCfgInfoTable,
       "h3cCBQoSMatchRuleCfgInfoEntry": h3cCBQoSMatchRuleCfgInfoEntry,
       "h3cCBQoSMatchRuleIndex": h3cCBQoSMatchRuleIndex,
       "h3cCBQoSMatchRuleIfNot": h3cCBQoSMatchRuleIfNot,
       "h3cCBQoSMatchRuleType": h3cCBQoSMatchRuleType,
       "h3cCBQoSMatchRuleStringValue": h3cCBQoSMatchRuleStringValue,
       "h3cCBQoSMatchRuleIntValue1": h3cCBQoSMatchRuleIntValue1,
       "h3cCBQoSMatchRuleIntValue2": h3cCBQoSMatchRuleIntValue2,
       "h3cCBQoSMatchIpAddressType": h3cCBQoSMatchIpAddressType,
       "h3cCBQoSMatchIpAddress": h3cCBQoSMatchIpAddress,
       "h3cCBQoSMatchRuleRowStatus": h3cCBQoSMatchRuleRowStatus,
       "h3cCBQoSBehaviorObjects": h3cCBQoSBehaviorObjects,
       "h3cCBQoSBehaviorIndexNext": h3cCBQoSBehaviorIndexNext,
       "h3cCBQoSBehaviorCfgInfoTable": h3cCBQoSBehaviorCfgInfoTable,
       "h3cCBQoSBehaviorCfgInfoEntry": h3cCBQoSBehaviorCfgInfoEntry,
       "h3cCBQoSBehaviorIndex": h3cCBQoSBehaviorIndex,
       "h3cCBQoSBehaviorName": h3cCBQoSBehaviorName,
       "h3cCBQoSBehaviorType": h3cCBQoSBehaviorType,
       "h3cCBQoSBehaviorRowStatus": h3cCBQoSBehaviorRowStatus,
       "h3cCBQoSCarCfgInfoTable": h3cCBQoSCarCfgInfoTable,
       "h3cCBQoSCarCfgInfoEntry": h3cCBQoSCarCfgInfoEntry,
       "h3cCBQoSCarCir": h3cCBQoSCarCir,
       "h3cCBQoSCarCbs": h3cCBQoSCarCbs,
       "h3cCBQoSCarEbs": h3cCBQoSCarEbs,
       "h3cCBQoSCarPir": h3cCBQoSCarPir,
       "h3cCBQoSCarPbs": h3cCBQoSCarPbs,
       "h3cCBQoSCarGreenAction": h3cCBQoSCarGreenAction,
       "h3cCBQoSCarGreenRemarkValue": h3cCBQoSCarGreenRemarkValue,
       "h3cCBQoSCarYellowAction": h3cCBQoSCarYellowAction,
       "h3cCBQoSCarYellowRemarkValue": h3cCBQoSCarYellowRemarkValue,
       "h3cCBQoSCarRedAction": h3cCBQoSCarRedAction,
       "h3cCBQoSCarRedRemarkValue": h3cCBQoSCarRedRemarkValue,
       "h3cCBQoSCarPolicedPriorityMapType": h3cCBQoSCarPolicedPriorityMapType,
       "h3cCBQoSCarRowStatus": h3cCBQoSCarRowStatus,
       "h3cCBQoSAggregativeCarCfgInfoTable": h3cCBQoSAggregativeCarCfgInfoTable,
       "h3cCBQoSAggregativeCarCfgInfoEntry": h3cCBQoSAggregativeCarCfgInfoEntry,
       "h3cCBQoSCarAggregativeCarIndex": h3cCBQoSCarAggregativeCarIndex,
       "h3cCBQoSCarAggregativeCarName": h3cCBQoSCarAggregativeCarName,
       "h3cCBQoSAggregativeCarRowStatus": h3cCBQoSAggregativeCarRowStatus,
       "h3cCBQoSGtsCfgInfoTable": h3cCBQoSGtsCfgInfoTable,
       "h3cCBQoSGtsCfgInfoEntry": h3cCBQoSGtsCfgInfoEntry,
       "h3cCBQoSGtsCir": h3cCBQoSGtsCir,
       "h3cCBQoSGtsCbs": h3cCBQoSGtsCbs,
       "h3cCBQoSGtsEbs": h3cCBQoSGtsEbs,
       "h3cCBQoSGtsQueueLength": h3cCBQoSGtsQueueLength,
       "h3cCBQoSGtsRowStatus": h3cCBQoSGtsRowStatus,
       "h3cCBQoSRemarkCfgInfoTable": h3cCBQoSRemarkCfgInfoTable,
       "h3cCBQoSRemarkCfgInfoEntry": h3cCBQoSRemarkCfgInfoEntry,
       "h3cCBQoSRemarkType": h3cCBQoSRemarkType,
       "h3cCBQoSRemarkValue": h3cCBQoSRemarkValue,
       "h3cCBQoSRemarkRowStatus": h3cCBQoSRemarkRowStatus,
       "h3cCBQoSQueueCfgInfoTable": h3cCBQoSQueueCfgInfoTable,
       "h3cCBQoSQueueCfgInfoEntry": h3cCBQoSQueueCfgInfoEntry,
       "h3cCBQoSQueueType": h3cCBQoSQueueType,
       "h3cCBQoSQueueDropType": h3cCBQoSQueueDropType,
       "h3cCBQoSQueueLength": h3cCBQoSQueueLength,
       "h3cCBQoSQueueBandwidthUnit": h3cCBQoSQueueBandwidthUnit,
       "h3cCBQoSQueueBandwidthValue": h3cCBQoSQueueBandwidthValue,
       "h3cCBQoSQueueCbs": h3cCBQoSQueueCbs,
       "h3cCBQoSQueueQueueNumber": h3cCBQoSQueueQueueNumber,
       "h3cCBQoSQueueCbsRatio": h3cCBQoSQueueCbsRatio,
       "h3cCBQoSQueueRowStatus": h3cCBQoSQueueRowStatus,
       "h3cCBQoSWredCfgInfoTable": h3cCBQoSWredCfgInfoTable,
       "h3cCBQoSWredCfgInfoEntry": h3cCBQoSWredCfgInfoEntry,
       "h3cCBQoSWredType": h3cCBQoSWredType,
       "h3cCBQoSWredWeightConst": h3cCBQoSWredWeightConst,
       "h3cCBQoSWredClassCfgInfoTable": h3cCBQoSWredClassCfgInfoTable,
       "h3cCBQoSWredClassCfgInfoEntry": h3cCBQoSWredClassCfgInfoEntry,
       "h3cCBQoSWredClassValue": h3cCBQoSWredClassValue,
       "h3cCBQoSWredClassLowLimit": h3cCBQoSWredClassLowLimit,
       "h3cCBQoSWredClassHighLimit": h3cCBQoSWredClassHighLimit,
       "h3cCBQoSWredClassDiscardProb": h3cCBQoSWredClassDiscardProb,
       "h3cCBQoSPolicyRouteCfgInfoTable": h3cCBQoSPolicyRouteCfgInfoTable,
       "h3cCBQoSPolicyRouteCfgInfoEntry": h3cCBQoSPolicyRouteCfgInfoEntry,
       "h3cCBQoSPolicyRouteIpAddrType": h3cCBQoSPolicyRouteIpAddrType,
       "h3cCBQoSPolicyRouteNexthop": h3cCBQoSPolicyRouteNexthop,
       "h3cCBQoSPolicyRouteBackup": h3cCBQoSPolicyRouteBackup,
       "h3cCBQoSPolicyRouteRowStatus": h3cCBQoSPolicyRouteRowStatus,
       "h3cCBQoSNatCfgInfoTable": h3cCBQoSNatCfgInfoTable,
       "h3cCBQoSNatCfgInfoEntry": h3cCBQoSNatCfgInfoEntry,
       "h3cCBQoSNatMainNumber": h3cCBQoSNatMainNumber,
       "h3cCBQoSNatBackupNumber": h3cCBQoSNatBackupNumber,
       "h3cCBQoSNatServiceClass": h3cCBQoSNatServiceClass,
       "h3cCBQoSNatRowStatus": h3cCBQoSNatRowStatus,
       "h3cCBQoSFirewallCfgInfoTable": h3cCBQoSFirewallCfgInfoTable,
       "h3cCBQoSFirewallCfgInfoEntry": h3cCBQoSFirewallCfgInfoEntry,
       "h3cCBQoSFirewallAction": h3cCBQoSFirewallAction,
       "h3cCBQoSFirewallRowStatus": h3cCBQoSFirewallRowStatus,
       "h3cCBQoSSamplingCfgInfoTable": h3cCBQoSSamplingCfgInfoTable,
       "h3cCBQoSSamplingCfgInfoEntry": h3cCBQoSSamplingCfgInfoEntry,
       "h3cCBQoSSamplingNum": h3cCBQoSSamplingNum,
       "h3cCBQoSSamplingRowStatus": h3cCBQoSSamplingRowStatus,
       "h3cCBQoSAccountCfgInfoTable": h3cCBQoSAccountCfgInfoTable,
       "h3cCBQoSAccountCfgInfoEntry": h3cCBQoSAccountCfgInfoEntry,
       "h3cCBQoSAccounting": h3cCBQoSAccounting,
       "h3cCBQoSAccountRowStatus": h3cCBQoSAccountRowStatus,
       "h3cCBQoSRedirectCfgInfoTable": h3cCBQoSRedirectCfgInfoTable,
       "h3cCBQoSRedirectCfgInfoEntry": h3cCBQoSRedirectCfgInfoEntry,
       "h3cCBQoSRedirectType": h3cCBQoSRedirectType,
       "h3cCBQoSRedirectIfIndex": h3cCBQoSRedirectIfIndex,
       "h3cCBQoSRedirectIpAddressType": h3cCBQoSRedirectIpAddressType,
       "h3cCBQoSRedirectIpAddress1": h3cCBQoSRedirectIpAddress1,
       "h3cCBQoSRedirectIpAddress2": h3cCBQoSRedirectIpAddress2,
       "h3cCBQoSRedirectRowStatus": h3cCBQoSRedirectRowStatus,
       "h3cCBQoSRedirectIpv6Interface1": h3cCBQoSRedirectIpv6Interface1,
       "h3cCBQoSRedirectIpv6Interface2": h3cCBQoSRedirectIpv6Interface2,
       "h3cCBQoSPriorityMapCfgInfoTable": h3cCBQoSPriorityMapCfgInfoTable,
       "h3cCBQoSPriorityMapCfgInfoEntry": h3cCBQoSPriorityMapCfgInfoEntry,
       "h3cCBQoSPriorityMapImportType": h3cCBQoSPriorityMapImportType,
       "h3cCBQoSPriorityMapExportType": h3cCBQoSPriorityMapExportType,
       "h3cCBQoSPriorityMapGroupIndex": h3cCBQoSPriorityMapGroupIndex,
       "h3cCBQoSPriorityMapGroupName": h3cCBQoSPriorityMapGroupName,
       "h3cCBQoSPriorityMapAuto": h3cCBQoSPriorityMapAuto,
       "h3cCBQoSPriorityMapRowStatus": h3cCBQoSPriorityMapRowStatus,
       "h3cCBQoSMirrorCfgInfoTable": h3cCBQoSMirrorCfgInfoTable,
       "h3cCBQoSMirrorCfgInfoEntry": h3cCBQoSMirrorCfgInfoEntry,
       "h3cCBQoSMirrorType": h3cCBQoSMirrorType,
       "h3cCBQoSMirrorIfIndex": h3cCBQoSMirrorIfIndex,
       "h3cCBQoSMirrorVlanID": h3cCBQoSMirrorVlanID,
       "h3cCBQoSMirrorRowStatus": h3cCBQoSMirrorRowStatus,
       "h3cCBQoSNestCfgInfoTable": h3cCBQoSNestCfgInfoTable,
       "h3cCBQoSNestCfgInfoEntry": h3cCBQoSNestCfgInfoEntry,
       "h3cCBQoSNestServiceVlanID": h3cCBQoSNestServiceVlanID,
       "h3cCBQoSNestServiceDot1pValue": h3cCBQoSNestServiceDot1pValue,
       "h3cCBQoSNestCustomerVlanID": h3cCBQoSNestCustomerVlanID,
       "h3cCBQoSNestCustomerDot1pValue": h3cCBQoSNestCustomerDot1pValue,
       "h3cCBQoSNestRowStatus": h3cCBQoSNestRowStatus,
       "h3cCBQoSNestPolicyCfgInfoTable": h3cCBQoSNestPolicyCfgInfoTable,
       "h3cCBQoSNestPolicyCfgInfoEntry": h3cCBQoSNestPolicyCfgInfoEntry,
       "h3cCBQoSNestPolicyName": h3cCBQoSNestPolicyName,
       "h3cCBQoSNestPolicyRowStatus": h3cCBQoSNestPolicyRowStatus,
       "h3cCBQoSPolicyObjects": h3cCBQoSPolicyObjects,
       "h3cCBQoSPolicyIndexNext": h3cCBQoSPolicyIndexNext,
       "h3cCBQoSPolicyCfgInfoTable": h3cCBQoSPolicyCfgInfoTable,
       "h3cCBQoSPolicyCfgInfoEntry": h3cCBQoSPolicyCfgInfoEntry,
       "h3cCBQoSPolicyIndex": h3cCBQoSPolicyIndex,
       "h3cCBQoSPolicyName": h3cCBQoSPolicyName,
       "h3cCBQoSPolicyClassCount": h3cCBQoSPolicyClassCount,
       "h3cCBQoSPolicyConfigMode": h3cCBQoSPolicyConfigMode,
       "h3cCBQoSPolicyType": h3cCBQoSPolicyType,
       "h3cCBQoSPolicyClassNextIndex": h3cCBQoSPolicyClassNextIndex,
       "h3cCBQoSPolicyRowStatus": h3cCBQoSPolicyRowStatus,
       "h3cCBQoSPolicyClassCfgInfoTable": h3cCBQoSPolicyClassCfgInfoTable,
       "h3cCBQoSPolicyClassCfgInfoEntry": h3cCBQoSPolicyClassCfgInfoEntry,
       "h3cCBQoSPolicyClassIndex": h3cCBQoSPolicyClassIndex,
       "h3cCBQoSPolicyClassClassifierIndex": h3cCBQoSPolicyClassClassifierIndex,
       "h3cCBQoSPolicyClassClassifierName": h3cCBQoSPolicyClassClassifierName,
       "h3cCBQoSPolicyClassBehaviorIndex": h3cCBQoSPolicyClassBehaviorIndex,
       "h3cCBQoSPolicyClassBehaviorName": h3cCBQoSPolicyClassBehaviorName,
       "h3cCBQoSPolicyClassPrecedence": h3cCBQoSPolicyClassPrecedence,
       "h3cCBQoSPolicyClassRowStatus": h3cCBQoSPolicyClassRowStatus,
       "h3cCBQoSPolicyClassMode": h3cCBQoSPolicyClassMode,
       "h3cCBQoSPolicyClassCfgOrder": h3cCBQoSPolicyClassCfgOrder,
       "h3cCBQoSApplyPolicyObjects": h3cCBQoSApplyPolicyObjects,
       "h3cCBQoSIfApplyPolicyTable": h3cCBQoSIfApplyPolicyTable,
       "h3cCBQoSIfApplyPolicyEntry": h3cCBQoSIfApplyPolicyEntry,
       "h3cCBQoSIfApplyPolicyIfIndex": h3cCBQoSIfApplyPolicyIfIndex,
       "h3cCBQoSIfApplyPolicyDirection": h3cCBQoSIfApplyPolicyDirection,
       "h3cCBQoSIfApplyPolicyName": h3cCBQoSIfApplyPolicyName,
       "h3cCBQoSIfApplyPolicyEnableDynamic": h3cCBQoSIfApplyPolicyEnableDynamic,
       "h3cCBQoSIfApplyPolicyRowStatus": h3cCBQoSIfApplyPolicyRowStatus,
       "h3cCBQoSAtmPvcApplyPolicyTable": h3cCBQoSAtmPvcApplyPolicyTable,
       "h3cCBQoSAtmPvcApplyPolicyEntry": h3cCBQoSAtmPvcApplyPolicyEntry,
       "h3cCBQoSAtmPvcApplyPolicyIfIndex": h3cCBQoSAtmPvcApplyPolicyIfIndex,
       "h3cCBQoSAtmPvcApplyPolicyVPI": h3cCBQoSAtmPvcApplyPolicyVPI,
       "h3cCBQoSAtmPvcApplyPolicyVCI": h3cCBQoSAtmPvcApplyPolicyVCI,
       "h3cCBQoSAtmPvcApplyPolicyDirection": h3cCBQoSAtmPvcApplyPolicyDirection,
       "h3cCBQoSAtmPvcApplyPolicyName": h3cCBQoSAtmPvcApplyPolicyName,
       "h3cCBQoSAtmPvcApplyPolicyRowStatus": h3cCBQoSAtmPvcApplyPolicyRowStatus,
       "h3cCBQoSVlanApplyPolicyTable": h3cCBQoSVlanApplyPolicyTable,
       "h3cCBQoSVlanApplyPolicyEntry": h3cCBQoSVlanApplyPolicyEntry,
       "h3cCBQoSVlanApplyPolicyVlanid": h3cCBQoSVlanApplyPolicyVlanid,
       "h3cCBQoSVlanApplyPolicyDirection": h3cCBQoSVlanApplyPolicyDirection,
       "h3cCBQoSVlanApplyPolicyName": h3cCBQoSVlanApplyPolicyName,
       "h3cCBQoSVlanApplyPriority": h3cCBQoSVlanApplyPriority,
       "h3cCBQoSVlanApplyPolicyRowStatus": h3cCBQoSVlanApplyPolicyRowStatus,
       "h3cCBQoSFrClassApplyPolicyTable": h3cCBQoSFrClassApplyPolicyTable,
       "h3cCBQoSFrClassApplyPolicyEntry": h3cCBQoSFrClassApplyPolicyEntry,
       "h3cCBQoSFrClassApplyPolicyFrClassName": h3cCBQoSFrClassApplyPolicyFrClassName,
       "h3cCBQoSFrClassApplyPolicyDirection": h3cCBQoSFrClassApplyPolicyDirection,
       "h3cCBQoSFrClassApplyPolicyName": h3cCBQoSFrClassApplyPolicyName,
       "h3cCBQoSFrClassApplyPolicyRowStatus": h3cCBQoSFrClassApplyPolicyRowStatus,
       "h3cCBQoSFrPvcApplyPolicyTable": h3cCBQoSFrPvcApplyPolicyTable,
       "h3cCBQoSFrPvcApplyPolicyEntry": h3cCBQoSFrPvcApplyPolicyEntry,
       "h3cCBQoSFrPvcApplyPolicyIfIndex": h3cCBQoSFrPvcApplyPolicyIfIndex,
       "h3cCBQoSFrPvcApplyPolicyDlciNum": h3cCBQoSFrPvcApplyPolicyDlciNum,
       "h3cCBQoSFrPvcApplyPolicyDirection": h3cCBQoSFrPvcApplyPolicyDirection,
       "h3cCBQoSFrPvcApplyPolicyName": h3cCBQoSFrPvcApplyPolicyName,
       "h3cCBQoSFrPvcApplyPolicyRowStatus": h3cCBQoSFrPvcApplyPolicyRowStatus,
       "h3cCBQoSGlobalApplyTable": h3cCBQoSGlobalApplyTable,
       "h3cCBQoSGlobalApplyEntry": h3cCBQoSGlobalApplyEntry,
       "h3cCBQoSGlobalApplyDirection": h3cCBQoSGlobalApplyDirection,
       "h3cCBQoSGlobalApplyName": h3cCBQoSGlobalApplyName,
       "h3cCBQoSGlobalApplyRowStatus": h3cCBQoSGlobalApplyRowStatus,
       "h3cCBQoSApplyPolicyStaticsObjects": h3cCBQoSApplyPolicyStaticsObjects,
       "h3cCBQoSIfStaticsObjects": h3cCBQoSIfStaticsObjects,
       "h3cCBQoSIfCbqRunInfoTable": h3cCBQoSIfCbqRunInfoTable,
       "h3cCBQoSIfCbqRunInfoEntry": h3cCBQoSIfCbqRunInfoEntry,
       "h3cCBQoSIfCbqQueueSize": h3cCBQoSIfCbqQueueSize,
       "h3cCBQoSIfCbqDiscard": h3cCBQoSIfCbqDiscard,
       "h3cCBQoSIfCbqEfQueueSize": h3cCBQoSIfCbqEfQueueSize,
       "h3cCBQoSIfCbqAfQueueSize": h3cCBQoSIfCbqAfQueueSize,
       "h3cCBQoSIfCbqBeQueueSize": h3cCBQoSIfCbqBeQueueSize,
       "h3cCBQoSIfCbqBeActiveQueueNum": h3cCBQoSIfCbqBeActiveQueueNum,
       "h3cCBQoSIfCbqBeMaxActiveQueueNum": h3cCBQoSIfCbqBeMaxActiveQueueNum,
       "h3cCBQoSIfCbqBeTotalQueueNum": h3cCBQoSIfCbqBeTotalQueueNum,
       "h3cCBQoSIfCbqAfAllocatedQueueNum": h3cCBQoSIfCbqAfAllocatedQueueNum,
       "h3cCBQoSIfClassMatchRunInfoTable": h3cCBQoSIfClassMatchRunInfoTable,
       "h3cCBQoSIfClassMatchRunInfoEntry": h3cCBQoSIfClassMatchRunInfoEntry,
       "h3cCBQoSIfClassMatchedPackets": h3cCBQoSIfClassMatchedPackets,
       "h3cCBQoSIfClassMatchedBytes": h3cCBQoSIfClassMatchedBytes,
       "h3cCBQoSIfClassAverageRate": h3cCBQoSIfClassAverageRate,
       "h3cCBQoSIfCarRunInfoTable": h3cCBQoSIfCarRunInfoTable,
       "h3cCBQoSIfCarRunInfoEntry": h3cCBQoSIfCarRunInfoEntry,
       "h3cCBQoSIfCarGreenPackets": h3cCBQoSIfCarGreenPackets,
       "h3cCBQoSIfCarGreenBytes": h3cCBQoSIfCarGreenBytes,
       "h3cCBQoSIfCarRedPackets": h3cCBQoSIfCarRedPackets,
       "h3cCBQoSIfCarRedBytes": h3cCBQoSIfCarRedBytes,
       "h3cCBQoSIfCarYellowPackets": h3cCBQoSIfCarYellowPackets,
       "h3cCBQoSIfCarYellowBytes": h3cCBQoSIfCarYellowBytes,
       "h3cCBQoSIfGtsRunInfoTable": h3cCBQoSIfGtsRunInfoTable,
       "h3cCBQoSIfGtsRunInfoEntry": h3cCBQoSIfGtsRunInfoEntry,
       "h3cCBQoSIfGtsPassedPackets": h3cCBQoSIfGtsPassedPackets,
       "h3cCBQoSIfGtsPassedBytes": h3cCBQoSIfGtsPassedBytes,
       "h3cCBQoSIfGtsDiscardedPackets": h3cCBQoSIfGtsDiscardedPackets,
       "h3cCBQoSIfGtsDiscardedBytes": h3cCBQoSIfGtsDiscardedBytes,
       "h3cCBQoSIfGtsDelayedPackets": h3cCBQoSIfGtsDelayedPackets,
       "h3cCBQoSIfGtsDelayedBytes": h3cCBQoSIfGtsDelayedBytes,
       "h3cCBQoSIfGtsQueueSize": h3cCBQoSIfGtsQueueSize,
       "h3cCBQoSIfRemarkRunInfoTable": h3cCBQoSIfRemarkRunInfoTable,
       "h3cCBQoSIfRemarkRunInfoEntry": h3cCBQoSIfRemarkRunInfoEntry,
       "h3cCBQoSIfRemarkedPackets": h3cCBQoSIfRemarkedPackets,
       "h3cCBQoSIfQueueRunInfoTable": h3cCBQoSIfQueueRunInfoTable,
       "h3cCBQoSIfQueueRunInfoEntry": h3cCBQoSIfQueueRunInfoEntry,
       "h3cCBQoSIfQueueMatchedPackets": h3cCBQoSIfQueueMatchedPackets,
       "h3cCBQoSIfQueueMatchedBytes": h3cCBQoSIfQueueMatchedBytes,
       "h3cCBQoSIfQueueEnqueuedPackets": h3cCBQoSIfQueueEnqueuedPackets,
       "h3cCBQoSIfQueueEnqueuedBytes": h3cCBQoSIfQueueEnqueuedBytes,
       "h3cCBQoSIfQueueDiscardedPackets": h3cCBQoSIfQueueDiscardedPackets,
       "h3cCBQoSIfQueueDiscardedBytes": h3cCBQoSIfQueueDiscardedBytes,
       "h3cCBQoSIfWredRunInfoTable": h3cCBQoSIfWredRunInfoTable,
       "h3cCBQoSIfWredRunInfoEntry": h3cCBQoSIfWredRunInfoEntry,
       "h3cCBQoSIfWredRandomDiscardedPackets": h3cCBQoSIfWredRandomDiscardedPackets,
       "h3cCBQoSIfWredTailDiscardedPackets": h3cCBQoSIfWredTailDiscardedPackets,
       "h3cCBQoSIfAccountingRunInfoTable": h3cCBQoSIfAccountingRunInfoTable,
       "h3cCBQoSIfAccountingRunInfoEntry": h3cCBQoSIfAccountingRunInfoEntry,
       "h3cCBQoSIfAccountingPackets": h3cCBQoSIfAccountingPackets,
       "h3cCBQoSIfAccountingBytes": h3cCBQoSIfAccountingBytes,
       "h3cCBQoSAtmPvcStaticsObjects": h3cCBQoSAtmPvcStaticsObjects,
       "h3cCBQoSAtmPvcCbqRunInfoTable": h3cCBQoSAtmPvcCbqRunInfoTable,
       "h3cCBQoSAtmPvcCbqRunInfoEntry": h3cCBQoSAtmPvcCbqRunInfoEntry,
       "h3cCBQoSAtmPvcCbqQueueSize": h3cCBQoSAtmPvcCbqQueueSize,
       "h3cCBQoSAtmPvcCbqDiscard": h3cCBQoSAtmPvcCbqDiscard,
       "h3cCBQoSAtmPvcCbqEfQueueSize": h3cCBQoSAtmPvcCbqEfQueueSize,
       "h3cCBQoSAtmPvcCbqAfQueueSize": h3cCBQoSAtmPvcCbqAfQueueSize,
       "h3cCBQoSAtmPvcCbqBeQueueSize": h3cCBQoSAtmPvcCbqBeQueueSize,
       "h3cCBQoSAtmPvcCbqBeActiveQueueNum": h3cCBQoSAtmPvcCbqBeActiveQueueNum,
       "h3cCBQoSAtmPvcCbqBeMaxActiveQueueNum": h3cCBQoSAtmPvcCbqBeMaxActiveQueueNum,
       "h3cCBQoSAtmPvcCbqBeTotalQueueNum": h3cCBQoSAtmPvcCbqBeTotalQueueNum,
       "h3cCBQoSAtmPvcCbqAfAllocatedQueueNum": h3cCBQoSAtmPvcCbqAfAllocatedQueueNum,
       "h3cCBQoSAtmPvcClassMatchRunInfoTable": h3cCBQoSAtmPvcClassMatchRunInfoTable,
       "h3cCBQoSAtmPvcClassMatchRunInfoEntry": h3cCBQoSAtmPvcClassMatchRunInfoEntry,
       "h3cCBQoSAtmPvcClassMatchPackets": h3cCBQoSAtmPvcClassMatchPackets,
       "h3cCBQoSAtmPvcClassMatchBytes": h3cCBQoSAtmPvcClassMatchBytes,
       "h3cCBQoSAtmPvcClassAverageRate": h3cCBQoSAtmPvcClassAverageRate,
       "h3cCBQoSAtmPvcCarRunInfoTable": h3cCBQoSAtmPvcCarRunInfoTable,
       "h3cCBQoSAtmPvcCarRunInfoEntry": h3cCBQoSAtmPvcCarRunInfoEntry,
       "h3cCBQoSAtmPvcCarConformPackets": h3cCBQoSAtmPvcCarConformPackets,
       "h3cCBQoSAtmPvcCarConformBytes": h3cCBQoSAtmPvcCarConformBytes,
       "h3cCBQoSAtmPvcCarExceedPackets": h3cCBQoSAtmPvcCarExceedPackets,
       "h3cCBQoSAtmPvcCarExceedBytes": h3cCBQoSAtmPvcCarExceedBytes,
       "h3cCBQoSAtmPvcGtsRunInfoTable": h3cCBQoSAtmPvcGtsRunInfoTable,
       "h3cCBQoSAtmPvcGtsRunInfoEntry": h3cCBQoSAtmPvcGtsRunInfoEntry,
       "h3cCBQoSAtmPvcGtsPassedPackets": h3cCBQoSAtmPvcGtsPassedPackets,
       "h3cCBQoSAtmPvcGtsPassedBytes": h3cCBQoSAtmPvcGtsPassedBytes,
       "h3cCBQoSAtmPvcGtsDiscardedPackets": h3cCBQoSAtmPvcGtsDiscardedPackets,
       "h3cCBQoSAtmPvcGtsDiscardedBytes": h3cCBQoSAtmPvcGtsDiscardedBytes,
       "h3cCBQoSAtmPvcGtsDelayedPackets": h3cCBQoSAtmPvcGtsDelayedPackets,
       "h3cCBQoSAtmPvcGtsDelayedBytes": h3cCBQoSAtmPvcGtsDelayedBytes,
       "h3cCBQoSAtmPvcGtsQueueSize": h3cCBQoSAtmPvcGtsQueueSize,
       "h3cCBQoSAtmPvcRemarkRunInfoTable": h3cCBQoSAtmPvcRemarkRunInfoTable,
       "h3cCBQoSAtmPvcRemarkRunInfoEntry": h3cCBQoSAtmPvcRemarkRunInfoEntry,
       "h3cCBQoSAtmPvcRemarkedPackets": h3cCBQoSAtmPvcRemarkedPackets,
       "h3cCBQoSAtmPvcQueueRunInfoTable": h3cCBQoSAtmPvcQueueRunInfoTable,
       "h3cCBQoSAtmPvcQueueRunInfoEntry": h3cCBQoSAtmPvcQueueRunInfoEntry,
       "h3cCBQoSAtmPvcQueueMatchedPackets": h3cCBQoSAtmPvcQueueMatchedPackets,
       "h3cCBQoSAtmPvcQueueMatchedBytes": h3cCBQoSAtmPvcQueueMatchedBytes,
       "h3cCBQoSAtmPvcQueueEnqueuedPackets": h3cCBQoSAtmPvcQueueEnqueuedPackets,
       "h3cCBQoSAtmPvcQueueEnqueuedBytes": h3cCBQoSAtmPvcQueueEnqueuedBytes,
       "h3cCBQoSAtmPvcQueueDiscardedPackets": h3cCBQoSAtmPvcQueueDiscardedPackets,
       "h3cCBQoSAtmPvcQueueDiscardedBytes": h3cCBQoSAtmPvcQueueDiscardedBytes,
       "h3cCBQoSAtmPvcWredRunInfoTable": h3cCBQoSAtmPvcWredRunInfoTable,
       "h3cCBQoSAtmPvcWredRunInfoEntry": h3cCBQoSAtmPvcWredRunInfoEntry,
       "h3cCBQoSAtmPvcWredRandomDiscardedPackets": h3cCBQoSAtmPvcWredRandomDiscardedPackets,
       "h3cCBQoSAtmPvcWredTailDiscardedPackets": h3cCBQoSAtmPvcWredTailDiscardedPackets,
       "h3cCBQoSAtmPvcAccountingRunInfoTable": h3cCBQoSAtmPvcAccountingRunInfoTable,
       "h3cCBQoSAtmPvcAccountingRunInfoEntry": h3cCBQoSAtmPvcAccountingRunInfoEntry,
       "h3cCBQoSAtmPvcAccountingPackets": h3cCBQoSAtmPvcAccountingPackets,
       "h3cCBQoSAtmPvcAccountingBytes": h3cCBQoSAtmPvcAccountingBytes,
       "h3cCBQoSFrPvcStaticsObjects": h3cCBQoSFrPvcStaticsObjects,
       "h3cCBQoSFrPvcCbqRunInfoTable": h3cCBQoSFrPvcCbqRunInfoTable,
       "h3cCBQoSFrPvcCbqRunInfoEntry": h3cCBQoSFrPvcCbqRunInfoEntry,
       "h3cCBQoSFrPvcCbqQueueSize": h3cCBQoSFrPvcCbqQueueSize,
       "h3cCBQoSFrPvcCbqDiscard": h3cCBQoSFrPvcCbqDiscard,
       "h3cCBQoSFrPvcCbqEfQueueSize": h3cCBQoSFrPvcCbqEfQueueSize,
       "h3cCBQoSFrPvcCbqAfQueueSize": h3cCBQoSFrPvcCbqAfQueueSize,
       "h3cCBQoSFrPvcCbqBeQueueSize": h3cCBQoSFrPvcCbqBeQueueSize,
       "h3cCBQoSFrPvcCbqBeActiveQueueNum": h3cCBQoSFrPvcCbqBeActiveQueueNum,
       "h3cCBQoSFrPvcCbqBeMaxActiveQueueNum": h3cCBQoSFrPvcCbqBeMaxActiveQueueNum,
       "h3cCBQoSFrPvcCbqBeTotalQueueNum": h3cCBQoSFrPvcCbqBeTotalQueueNum,
       "h3cCBQoSFrPvcCbqAfAllocatedQueueNum": h3cCBQoSFrPvcCbqAfAllocatedQueueNum,
       "h3cCBQoSFrPvcClassMatchRunInfoTable": h3cCBQoSFrPvcClassMatchRunInfoTable,
       "h3cCBQoSFrPvcClassMatchRunInfoEntry": h3cCBQoSFrPvcClassMatchRunInfoEntry,
       "h3cCBQoSFrPvcClassMatchedPackets": h3cCBQoSFrPvcClassMatchedPackets,
       "h3cCBQoSFrPvcClassMatchedBytes": h3cCBQoSFrPvcClassMatchedBytes,
       "h3cCBQoSFrPvcClassAverageRate": h3cCBQoSFrPvcClassAverageRate,
       "h3cCBQoSFrPvcCarRunInfoTable": h3cCBQoSFrPvcCarRunInfoTable,
       "h3cCBQoSFrPvcCarRunInfoEntry": h3cCBQoSFrPvcCarRunInfoEntry,
       "h3cCBQoSFrPvcCarConformPackets": h3cCBQoSFrPvcCarConformPackets,
       "h3cCBQoSFrPvcCarConformBytes": h3cCBQoSFrPvcCarConformBytes,
       "h3cCBQoSFrPvcCarExceedPackets": h3cCBQoSFrPvcCarExceedPackets,
       "h3cCBQoSFrPvcCarExceedBytes": h3cCBQoSFrPvcCarExceedBytes,
       "h3cCBQoSFrPvcGtsRunInfoTable": h3cCBQoSFrPvcGtsRunInfoTable,
       "h3cCBQoSFrPvcGtsRunInfoEntry": h3cCBQoSFrPvcGtsRunInfoEntry,
       "h3cCBQoSFrPvcGtsPassedPackets": h3cCBQoSFrPvcGtsPassedPackets,
       "h3cCBQoSFrPvcGtsPassedBytes": h3cCBQoSFrPvcGtsPassedBytes,
       "h3cCBQoSFrPvcGtsDiscardedPackets": h3cCBQoSFrPvcGtsDiscardedPackets,
       "h3cCBQoSFrPvcGtsDiscardedBytes": h3cCBQoSFrPvcGtsDiscardedBytes,
       "h3cCBQoSFrPvcGtsDelayedPackets": h3cCBQoSFrPvcGtsDelayedPackets,
       "h3cCBQoSFrPvcGtsDelayedBytes": h3cCBQoSFrPvcGtsDelayedBytes,
       "h3cCBQoSFrPvcGtsQueueSize": h3cCBQoSFrPvcGtsQueueSize,
       "h3cCBQoSFrPvcRemarkRunInfoTable": h3cCBQoSFrPvcRemarkRunInfoTable,
       "h3cCBQoSFrPvcRemarkRunInfoEntry": h3cCBQoSFrPvcRemarkRunInfoEntry,
       "h3cCBQoSFrPvcRemarkedPackets": h3cCBQoSFrPvcRemarkedPackets,
       "h3cCBQoSFrPvcQueueRunInfoTable": h3cCBQoSFrPvcQueueRunInfoTable,
       "h3cCBQoSFrPvcQueueRunInfoEntry": h3cCBQoSFrPvcQueueRunInfoEntry,
       "h3cCBQoSFrPvcQueueMatchedPackets": h3cCBQoSFrPvcQueueMatchedPackets,
       "h3cCBQoSFrPvcQueueMatchedBytes": h3cCBQoSFrPvcQueueMatchedBytes,
       "h3cCBQoSFrPvcQueueEnqueuedPackets": h3cCBQoSFrPvcQueueEnqueuedPackets,
       "h3cCBQoSFrPvcQueueEnqueuedBytes": h3cCBQoSFrPvcQueueEnqueuedBytes,
       "h3cCBQoSFrPvcQueueDiscardedPackets": h3cCBQoSFrPvcQueueDiscardedPackets,
       "h3cCBQoSFrPvcQueueDiscardedBytes": h3cCBQoSFrPvcQueueDiscardedBytes,
       "h3cCBQoSFrPvcWredRunInfoTable": h3cCBQoSFrPvcWredRunInfoTable,
       "h3cCBQoSFrPvcWredRunInfoEntry": h3cCBQoSFrPvcWredRunInfoEntry,
       "h3cCBQoSFrPvcWredRandomDiscardedPackets": h3cCBQoSFrPvcWredRandomDiscardedPackets,
       "h3cCBQoSFrPvcWredTailDiscardedPackets": h3cCBQoSFrPvcWredTailDiscardedPackets,
       "h3cCBQoSFrPvcAccountingRunInfoTable": h3cCBQoSFrPvcAccountingRunInfoTable,
       "h3cCBQoSFrPvcAccountingRunInfoEntry": h3cCBQoSFrPvcAccountingRunInfoEntry,
       "h3cCBQoSFrPvcAccountingPackets": h3cCBQoSFrPvcAccountingPackets,
       "h3cCBQoSFrPvcAccountingBytes": h3cCBQoSFrPvcAccountingBytes,
       "h3cCBQoSVlanStaticsObjects": h3cCBQoSVlanStaticsObjects,
       "h3cCBQoSVlanClassMatchRunInfoTable": h3cCBQoSVlanClassMatchRunInfoTable,
       "h3cCBQoSVlanClassMatchRunInfoEntry": h3cCBQoSVlanClassMatchRunInfoEntry,
       "h3cCBQoSVlanClassMatchedPackets": h3cCBQoSVlanClassMatchedPackets,
       "h3cCBQoSVlanAccountingRunInfoTable": h3cCBQoSVlanAccountingRunInfoTable,
       "h3cCBQoSVlanAccountingRunInfoEntry": h3cCBQoSVlanAccountingRunInfoEntry,
       "h3cCBQoSVlanAccountingPackets": h3cCBQoSVlanAccountingPackets,
       "h3cCBQoSVlanAccountingBytes": h3cCBQoSVlanAccountingBytes,
       "h3cCBQoSApplyPolicyIndexObjects": h3cCBQoSApplyPolicyIndexObjects,
       "h3cCBQoSApplyObjectTable": h3cCBQoSApplyObjectTable,
       "h3cCBQoSApplyObjectEntry": h3cCBQoSApplyObjectEntry,
       "h3cCBQoSApplyObjectIndex": h3cCBQoSApplyObjectIndex,
       "h3cCBQoSApplyObjectType": h3cCBQoSApplyObjectType,
       "h3cCBQoSApplyObjectDirection": h3cCBQoSApplyObjectDirection,
       "h3cCBQoSApplyObjectMainSite": h3cCBQoSApplyObjectMainSite,
       "h3cCBQoSApplyObjectSubChannel": h3cCBQoSApplyObjectSubChannel,
       "h3cCBQoSApplyObjectSubClass": h3cCBQoSApplyObjectSubClass,
       "h3cCBQoSApplyObjectSubClassSec": h3cCBQoSApplyObjectSubClassSec,
       "h3cCBQoSIntApplyObjectTable": h3cCBQoSIntApplyObjectTable,
       "h3cCBQoSIntApplyObjectEntry": h3cCBQoSIntApplyObjectEntry,
       "h3cCBQoSIntApplyObjectIfIndex": h3cCBQoSIntApplyObjectIfIndex,
       "h3cCBQoSIntApplyObjectIndex": h3cCBQoSIntApplyObjectIndex,
       "h3cCBQoSVlanApplyObjectTable": h3cCBQoSVlanApplyObjectTable,
       "h3cCBQoSVlanApplyObjectEntry": h3cCBQoSVlanApplyObjectEntry,
       "h3cCBQoSVlanApplyObjectVlanID": h3cCBQoSVlanApplyObjectVlanID,
       "h3cCBQoSVlanApplyObjectIndex": h3cCBQoSVlanApplyObjectIndex,
       "h3cCBQoSPvcApplyObjectTable": h3cCBQoSPvcApplyObjectTable,
       "h3cCBQoSPvcApplyObjectEntry": h3cCBQoSPvcApplyObjectEntry,
       "h3cCBQoSPvcApplyObjectIfIndex": h3cCBQoSPvcApplyObjectIfIndex,
       "h3cCBQoSPvcApplyObjectPvcID": h3cCBQoSPvcApplyObjectPvcID,
       "h3cCBQoSPvcApplyObjectIndex": h3cCBQoSPvcApplyObjectIndex,
       "h3cCBQoSNestPolicyApplyObjectTable": h3cCBQoSNestPolicyApplyObjectTable,
       "h3cCBQoSNestPolicyApplyObjectEntry": h3cCBQoSNestPolicyApplyObjectEntry,
       "h3cCBQoSNestPolicyClassIndex": h3cCBQoSNestPolicyClassIndex,
       "h3cCBQoSNestPolicyApplyObjectIndex": h3cCBQoSNestPolicyApplyObjectIndex,
       "h3cCBQoSStaticsObjects": h3cCBQoSStaticsObjects,
       "h3cCBQoSCbqRunInfoTable": h3cCBQoSCbqRunInfoTable,
       "h3cCBQoSCbqRunInfoEntry": h3cCBQoSCbqRunInfoEntry,
       "h3cCBQoSCbqQueueSize": h3cCBQoSCbqQueueSize,
       "h3cCBQoSCbqDiscard": h3cCBQoSCbqDiscard,
       "h3cCBQoSCbqEfQueueSize": h3cCBQoSCbqEfQueueSize,
       "h3cCBQoSCbqAfQueueSize": h3cCBQoSCbqAfQueueSize,
       "h3cCBQoSCbqBeQueueSize": h3cCBQoSCbqBeQueueSize,
       "h3cCBQoSCbqBeActiveQueueNum": h3cCBQoSCbqBeActiveQueueNum,
       "h3cCBQoSCbqBeMaxActiveQueueNum": h3cCBQoSCbqBeMaxActiveQueueNum,
       "h3cCBQoSCbqBeTotalQueueNum": h3cCBQoSCbqBeTotalQueueNum,
       "h3cCBQoSCbqAfAllocatedQueueNum": h3cCBQoSCbqAfAllocatedQueueNum,
       "h3cCBQoSClassMatchRunInfoTable": h3cCBQoSClassMatchRunInfoTable,
       "h3cCBQoSClassMatchRunInfoEntry": h3cCBQoSClassMatchRunInfoEntry,
       "h3cCBQoSClassMatchedPackets": h3cCBQoSClassMatchedPackets,
       "h3cCBQoSClassMatchedBytes": h3cCBQoSClassMatchedBytes,
       "h3cCBQoSClassFwdPktpps": h3cCBQoSClassFwdPktpps,
       "h3cCBQoSClassFwdPktbps": h3cCBQoSClassFwdPktbps,
       "h3cCBQoSClassDropPktpps": h3cCBQoSClassDropPktpps,
       "h3cCBQoSClassDropPktbps": h3cCBQoSClassDropPktbps,
       "h3cCBQoSClassFlowStatInterval": h3cCBQoSClassFlowStatInterval,
       "h3cCBQoSClassBehaviorStatus": h3cCBQoSClassBehaviorStatus,
       "h3cCBQoSCarRunInfoTable": h3cCBQoSCarRunInfoTable,
       "h3cCBQoSCarRunInfoEntry": h3cCBQoSCarRunInfoEntry,
       "h3cCBQoSCarGreenPackets": h3cCBQoSCarGreenPackets,
       "h3cCBQoSCarGreenBytes": h3cCBQoSCarGreenBytes,
       "h3cCBQoSCarRedPackets": h3cCBQoSCarRedPackets,
       "h3cCBQoSCarRedBytes": h3cCBQoSCarRedBytes,
       "h3cCBQoSCarYellowPackets": h3cCBQoSCarYellowPackets,
       "h3cCBQoSCarYellowBytes": h3cCBQoSCarYellowBytes,
       "h3cCBQoSGtsRunInfoTable": h3cCBQoSGtsRunInfoTable,
       "h3cCBQoSGtsRunInfoEntry": h3cCBQoSGtsRunInfoEntry,
       "h3cCBQoSGtsPassedPackets": h3cCBQoSGtsPassedPackets,
       "h3cCBQoSGtsPassedBytes": h3cCBQoSGtsPassedBytes,
       "h3cCBQoSGtsDiscardedPackets": h3cCBQoSGtsDiscardedPackets,
       "h3cCBQoSGtsDiscardedBytes": h3cCBQoSGtsDiscardedBytes,
       "h3cCBQoSGtsDelayedPackets": h3cCBQoSGtsDelayedPackets,
       "h3cCBQoSGtsDelayedBytes": h3cCBQoSGtsDelayedBytes,
       "h3cCBQoSGtsQueueSize": h3cCBQoSGtsQueueSize,
       "h3cCBQoSRemarkRunInfoTable": h3cCBQoSRemarkRunInfoTable,
       "h3cCBQoSRemarkRunInfoEntry": h3cCBQoSRemarkRunInfoEntry,
       "h3cCBQoSRemarkedPackets": h3cCBQoSRemarkedPackets,
       "h3cCBQoSQueueRunInfoTable": h3cCBQoSQueueRunInfoTable,
       "h3cCBQoSQueueRunInfoEntry": h3cCBQoSQueueRunInfoEntry,
       "h3cCBQoSQueueMatchedPackets": h3cCBQoSQueueMatchedPackets,
       "h3cCBQoSQueueMatchedBytes": h3cCBQoSQueueMatchedBytes,
       "h3cCBQoSQueueEnqueuedPackets": h3cCBQoSQueueEnqueuedPackets,
       "h3cCBQoSQueueEnqueuedBytes": h3cCBQoSQueueEnqueuedBytes,
       "h3cCBQoSQueueDiscardedPackets": h3cCBQoSQueueDiscardedPackets,
       "h3cCBQoSQueueDiscardedBytes": h3cCBQoSQueueDiscardedBytes,
       "h3cCBQoSWredRunInfoTable": h3cCBQoSWredRunInfoTable,
       "h3cCBQoSWredRunInfoEntry": h3cCBQoSWredRunInfoEntry,
       "h3cCBQoSWredRandomDiscardedPackets": h3cCBQoSWredRandomDiscardedPackets,
       "h3cCBQoSWredTailDiscardedPackets": h3cCBQoSWredTailDiscardedPackets,
       "h3cCBQoSAccountingRunInfoTable": h3cCBQoSAccountingRunInfoTable,
       "h3cCBQoSAccountingRunInfoEntry": h3cCBQoSAccountingRunInfoEntry,
       "h3cCBQoSAccountingPackets": h3cCBQoSAccountingPackets,
       "h3cCBQoSAccountingBytes": h3cCBQoSAccountingBytes,
       "h3cCBQoSApplyingStatusObjects": h3cCBQoSApplyingStatusObjects,
       "h3cCBQoSApplyingStatus": h3cCBQoSApplyingStatus,
       "h3cCBQoSNotifications": h3cCBQoSNotifications,
       "h3cCBQoSNotificationsPrefix": h3cCBQoSNotificationsPrefix,
       "h3cCBQoSIfPolicyChanged": h3cCBQoSIfPolicyChanged,
       "h3cCBQoSVlanPolicyChanged": h3cCBQoSVlanPolicyChanged}
)
