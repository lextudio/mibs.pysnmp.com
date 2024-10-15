# SNMP MIB module (HPN-ICF-CBQOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-CBQOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:34 2024
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

hpnicfCBQos2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2)
)
hpnicfCBQos2.setRevisions(
        ("2012-07-02 00:00",
         "2005-07-30 00:00")
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("matchRuleAny", 1),
          ("matchRuleArpProtocol", 30),
          ("matchRuleAtmClp", 11),
          ("matchRuleBittorrent", 24),
          ("matchRuleClassifier", 16),
          ("matchRuleDestinationMac", 14),
          ("matchRuleDropPriority", 23),
          ("matchRuleDscp", 7),
          ("matchRuleForwardingLayer", 31),
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
          ("matchRuleMplsLabel", 26),
          ("matchRulePacketLength", 29),
          ("matchRuleQosLocalID", 15),
          ("matchRuleRtpPort", 18),
          ("matchRuleSecondMplsExp", 28),
          ("matchRuleSecondMplsLabel", 27),
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
              11,
              12)
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
          ("typeSecondMplsExp", 12),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unitAbsolute", 1),
          ("unitPercent", 2),
          ("unitRemainPercent", 3),
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atmPvc", 3),
          ("controlPlane", 5),
          ("frDlci", 4),
          ("interface", 1),
          ("vlan", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfQos2_ObjectIdentity = ObjectIdentity
hpnicfQos2 = _HpnicfQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65)
)
_HpnicfCBQoSObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSObjects = _HpnicfCBQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1)
)
_HpnicfCBQoSClassifierObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSClassifierObjects = _HpnicfCBQoSClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1)
)
_HpnicfCBQoSClassifierIndexNext_Type = Integer32
_HpnicfCBQoSClassifierIndexNext_Object = MibScalar
hpnicfCBQoSClassifierIndexNext = _HpnicfCBQoSClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 1),
    _HpnicfCBQoSClassifierIndexNext_Type()
)
hpnicfCBQoSClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierIndexNext.setStatus("current")
_HpnicfCBQoSClassifierCfgInfoTable_Object = MibTable
hpnicfCBQoSClassifierCfgInfoTable = _HpnicfCBQoSClassifierCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierCfgInfoTable.setStatus("current")
_HpnicfCBQoSClassifierCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSClassifierCfgInfoEntry = _HpnicfCBQoSClassifierCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1)
)
hpnicfCBQoSClassifierCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSClassifierIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierCfgInfoEntry.setStatus("current")
_HpnicfCBQoSClassifierIndex_Type = Integer32
_HpnicfCBQoSClassifierIndex_Object = MibTableColumn
hpnicfCBQoSClassifierIndex = _HpnicfCBQoSClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 1),
    _HpnicfCBQoSClassifierIndex_Type()
)
hpnicfCBQoSClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierIndex.setStatus("current")


class _HpnicfCBQoSClassifierName_Type(OctetString):
    """Custom type hpnicfCBQoSClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSClassifierName_Type.__name__ = "OctetString"
_HpnicfCBQoSClassifierName_Object = MibTableColumn
hpnicfCBQoSClassifierName = _HpnicfCBQoSClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 2),
    _HpnicfCBQoSClassifierName_Type()
)
hpnicfCBQoSClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierName.setStatus("current")
_HpnicfCBQoSClassifierRuleCount_Type = Integer32
_HpnicfCBQoSClassifierRuleCount_Object = MibTableColumn
hpnicfCBQoSClassifierRuleCount = _HpnicfCBQoSClassifierRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 3),
    _HpnicfCBQoSClassifierRuleCount_Type()
)
hpnicfCBQoSClassifierRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierRuleCount.setStatus("current")


class _HpnicfCBQoSClassifierOperator_Type(Integer32):
    """Custom type hpnicfCBQoSClassifierOperator based on Integer32"""
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


_HpnicfCBQoSClassifierOperator_Type.__name__ = "Integer32"
_HpnicfCBQoSClassifierOperator_Object = MibTableColumn
hpnicfCBQoSClassifierOperator = _HpnicfCBQoSClassifierOperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 4),
    _HpnicfCBQoSClassifierOperator_Type()
)
hpnicfCBQoSClassifierOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierOperator.setStatus("current")


class _HpnicfCBQoSClassifierLayer_Type(Integer32):
    """Custom type hpnicfCBQoSClassifierLayer based on Integer32"""
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


_HpnicfCBQoSClassifierLayer_Type.__name__ = "Integer32"
_HpnicfCBQoSClassifierLayer_Object = MibTableColumn
hpnicfCBQoSClassifierLayer = _HpnicfCBQoSClassifierLayer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 5),
    _HpnicfCBQoSClassifierLayer_Type()
)
hpnicfCBQoSClassifierLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierLayer.setStatus("current")


class _HpnicfCBQoSClassifierType_Type(Integer32):
    """Custom type hpnicfCBQoSClassifierType based on Integer32"""
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


_HpnicfCBQoSClassifierType_Type.__name__ = "Integer32"
_HpnicfCBQoSClassifierType_Object = MibTableColumn
hpnicfCBQoSClassifierType = _HpnicfCBQoSClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 6),
    _HpnicfCBQoSClassifierType_Type()
)
hpnicfCBQoSClassifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierType.setStatus("current")
_HpnicfCBQosClassifierMatchRuleNextIndex_Type = Integer32
_HpnicfCBQosClassifierMatchRuleNextIndex_Object = MibTableColumn
hpnicfCBQosClassifierMatchRuleNextIndex = _HpnicfCBQosClassifierMatchRuleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 7),
    _HpnicfCBQosClassifierMatchRuleNextIndex_Type()
)
hpnicfCBQosClassifierMatchRuleNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQosClassifierMatchRuleNextIndex.setStatus("current")
_HpnicfCBQoSClassifierRowStatus_Type = RowStatus
_HpnicfCBQoSClassifierRowStatus_Object = MibTableColumn
hpnicfCBQoSClassifierRowStatus = _HpnicfCBQoSClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 2, 1, 8),
    _HpnicfCBQoSClassifierRowStatus_Type()
)
hpnicfCBQoSClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassifierRowStatus.setStatus("current")
_HpnicfCBQoSMatchRuleCfgInfoTable_Object = MibTable
hpnicfCBQoSMatchRuleCfgInfoTable = _HpnicfCBQoSMatchRuleCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleCfgInfoTable.setStatus("current")
_HpnicfCBQoSMatchRuleCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSMatchRuleCfgInfoEntry = _HpnicfCBQoSMatchRuleCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1)
)
hpnicfCBQoSMatchRuleCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSClassifierIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSMatchRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleCfgInfoEntry.setStatus("current")
_HpnicfCBQoSMatchRuleIndex_Type = Integer32
_HpnicfCBQoSMatchRuleIndex_Object = MibTableColumn
hpnicfCBQoSMatchRuleIndex = _HpnicfCBQoSMatchRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 1),
    _HpnicfCBQoSMatchRuleIndex_Type()
)
hpnicfCBQoSMatchRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleIndex.setStatus("current")


class _HpnicfCBQoSMatchRuleIfNot_Type(Integer32):
    """Custom type hpnicfCBQoSMatchRuleIfNot based on Integer32"""
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


_HpnicfCBQoSMatchRuleIfNot_Type.__name__ = "Integer32"
_HpnicfCBQoSMatchRuleIfNot_Object = MibTableColumn
hpnicfCBQoSMatchRuleIfNot = _HpnicfCBQoSMatchRuleIfNot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 2),
    _HpnicfCBQoSMatchRuleIfNot_Type()
)
hpnicfCBQoSMatchRuleIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleIfNot.setStatus("current")
_HpnicfCBQoSMatchRuleType_Type = MatchRuleType
_HpnicfCBQoSMatchRuleType_Object = MibTableColumn
hpnicfCBQoSMatchRuleType = _HpnicfCBQoSMatchRuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 3),
    _HpnicfCBQoSMatchRuleType_Type()
)
hpnicfCBQoSMatchRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleType.setStatus("current")


class _HpnicfCBQoSMatchRuleStringValue_Type(OctetString):
    """Custom type hpnicfCBQoSMatchRuleStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCBQoSMatchRuleStringValue_Type.__name__ = "OctetString"
_HpnicfCBQoSMatchRuleStringValue_Object = MibTableColumn
hpnicfCBQoSMatchRuleStringValue = _HpnicfCBQoSMatchRuleStringValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 4),
    _HpnicfCBQoSMatchRuleStringValue_Type()
)
hpnicfCBQoSMatchRuleStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleStringValue.setStatus("current")
_HpnicfCBQoSMatchRuleIntValue1_Type = Unsigned32
_HpnicfCBQoSMatchRuleIntValue1_Object = MibTableColumn
hpnicfCBQoSMatchRuleIntValue1 = _HpnicfCBQoSMatchRuleIntValue1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 5),
    _HpnicfCBQoSMatchRuleIntValue1_Type()
)
hpnicfCBQoSMatchRuleIntValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleIntValue1.setStatus("current")
_HpnicfCBQoSMatchRuleIntValue2_Type = Unsigned32
_HpnicfCBQoSMatchRuleIntValue2_Object = MibTableColumn
hpnicfCBQoSMatchRuleIntValue2 = _HpnicfCBQoSMatchRuleIntValue2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 6),
    _HpnicfCBQoSMatchRuleIntValue2_Type()
)
hpnicfCBQoSMatchRuleIntValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleIntValue2.setStatus("current")
_HpnicfCBQoSMatchIpAddressType_Type = InetAddressType
_HpnicfCBQoSMatchIpAddressType_Object = MibTableColumn
hpnicfCBQoSMatchIpAddressType = _HpnicfCBQoSMatchIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 7),
    _HpnicfCBQoSMatchIpAddressType_Type()
)
hpnicfCBQoSMatchIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchIpAddressType.setStatus("current")
_HpnicfCBQoSMatchIpAddress_Type = InetAddress
_HpnicfCBQoSMatchIpAddress_Object = MibTableColumn
hpnicfCBQoSMatchIpAddress = _HpnicfCBQoSMatchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 8),
    _HpnicfCBQoSMatchIpAddress_Type()
)
hpnicfCBQoSMatchIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchIpAddress.setStatus("current")
_HpnicfCBQoSMatchRuleRowStatus_Type = RowStatus
_HpnicfCBQoSMatchRuleRowStatus_Object = MibTableColumn
hpnicfCBQoSMatchRuleRowStatus = _HpnicfCBQoSMatchRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 3, 1, 9),
    _HpnicfCBQoSMatchRuleRowStatus_Type()
)
hpnicfCBQoSMatchRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchRuleRowStatus.setStatus("current")
_HpnicfCBQoSMatchCpProtoCfgTable_Object = MibTable
hpnicfCBQoSMatchCpProtoCfgTable = _HpnicfCBQoSMatchCpProtoCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpProtoCfgTable.setStatus("current")
_HpnicfCBQoSMatchCpProtoCfgEntry_Object = MibTableRow
hpnicfCBQoSMatchCpProtoCfgEntry = _HpnicfCBQoSMatchCpProtoCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 4, 1)
)
hpnicfCBQoSMatchCpProtoCfgEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSClassifierIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSMatchRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpProtoCfgEntry.setStatus("current")


class _HpnicfCBQoSMatchCpProtoIfNot_Type(Integer32):
    """Custom type hpnicfCBQoSMatchCpProtoIfNot based on Integer32"""
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


_HpnicfCBQoSMatchCpProtoIfNot_Type.__name__ = "Integer32"
_HpnicfCBQoSMatchCpProtoIfNot_Object = MibTableColumn
hpnicfCBQoSMatchCpProtoIfNot = _HpnicfCBQoSMatchCpProtoIfNot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 4, 1, 1),
    _HpnicfCBQoSMatchCpProtoIfNot_Type()
)
hpnicfCBQoSMatchCpProtoIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpProtoIfNot.setStatus("current")


class _HpnicfCBQoSMatchCpProtoValue_Type(OctetString):
    """Custom type hpnicfCBQoSMatchCpProtoValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCBQoSMatchCpProtoValue_Type.__name__ = "OctetString"
_HpnicfCBQoSMatchCpProtoValue_Object = MibTableColumn
hpnicfCBQoSMatchCpProtoValue = _HpnicfCBQoSMatchCpProtoValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 4, 1, 2),
    _HpnicfCBQoSMatchCpProtoValue_Type()
)
hpnicfCBQoSMatchCpProtoValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpProtoValue.setStatus("current")
_HpnicfCBQoSMatchCpProtoRowStatus_Type = RowStatus
_HpnicfCBQoSMatchCpProtoRowStatus_Object = MibTableColumn
hpnicfCBQoSMatchCpProtoRowStatus = _HpnicfCBQoSMatchCpProtoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 4, 1, 3),
    _HpnicfCBQoSMatchCpProtoRowStatus_Type()
)
hpnicfCBQoSMatchCpProtoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpProtoRowStatus.setStatus("current")
_HpnicfCBQoSMatchCpGroupCfgTable_Object = MibTable
hpnicfCBQoSMatchCpGroupCfgTable = _HpnicfCBQoSMatchCpGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpGroupCfgTable.setStatus("current")
_HpnicfCBQoSMatchCpGroupCfgEntry_Object = MibTableRow
hpnicfCBQoSMatchCpGroupCfgEntry = _HpnicfCBQoSMatchCpGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 5, 1)
)
hpnicfCBQoSMatchCpGroupCfgEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSClassifierIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSMatchRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpGroupCfgEntry.setStatus("current")


class _HpnicfCBQoSMatchCpGroupIfNot_Type(Integer32):
    """Custom type hpnicfCBQoSMatchCpGroupIfNot based on Integer32"""
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


_HpnicfCBQoSMatchCpGroupIfNot_Type.__name__ = "Integer32"
_HpnicfCBQoSMatchCpGroupIfNot_Object = MibTableColumn
hpnicfCBQoSMatchCpGroupIfNot = _HpnicfCBQoSMatchCpGroupIfNot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 5, 1, 1),
    _HpnicfCBQoSMatchCpGroupIfNot_Type()
)
hpnicfCBQoSMatchCpGroupIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpGroupIfNot.setStatus("current")


class _HpnicfCBQoSMatchCpGroupValue_Type(Integer32):
    """Custom type hpnicfCBQoSMatchCpGroupValue based on Integer32"""
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
        *(("critical", 1),
          ("exception", 7),
          ("important", 2),
          ("management", 3),
          ("monitor", 6),
          ("normal", 4),
          ("redirect", 5))
    )


_HpnicfCBQoSMatchCpGroupValue_Type.__name__ = "Integer32"
_HpnicfCBQoSMatchCpGroupValue_Object = MibTableColumn
hpnicfCBQoSMatchCpGroupValue = _HpnicfCBQoSMatchCpGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 5, 1, 2),
    _HpnicfCBQoSMatchCpGroupValue_Type()
)
hpnicfCBQoSMatchCpGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpGroupValue.setStatus("current")
_HpnicfCBQoSMatchCpGroupRowStatus_Type = RowStatus
_HpnicfCBQoSMatchCpGroupRowStatus_Object = MibTableColumn
hpnicfCBQoSMatchCpGroupRowStatus = _HpnicfCBQoSMatchCpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 1, 5, 1, 3),
    _HpnicfCBQoSMatchCpGroupRowStatus_Type()
)
hpnicfCBQoSMatchCpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMatchCpGroupRowStatus.setStatus("current")
_HpnicfCBQoSBehaviorObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSBehaviorObjects = _HpnicfCBQoSBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2)
)
_HpnicfCBQoSBehaviorIndexNext_Type = Integer32
_HpnicfCBQoSBehaviorIndexNext_Object = MibScalar
hpnicfCBQoSBehaviorIndexNext = _HpnicfCBQoSBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 1),
    _HpnicfCBQoSBehaviorIndexNext_Type()
)
hpnicfCBQoSBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorIndexNext.setStatus("current")
_HpnicfCBQoSBehaviorCfgInfoTable_Object = MibTable
hpnicfCBQoSBehaviorCfgInfoTable = _HpnicfCBQoSBehaviorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorCfgInfoTable.setStatus("current")
_HpnicfCBQoSBehaviorCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSBehaviorCfgInfoEntry = _HpnicfCBQoSBehaviorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 2, 1)
)
hpnicfCBQoSBehaviorCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorCfgInfoEntry.setStatus("current")
_HpnicfCBQoSBehaviorIndex_Type = Integer32
_HpnicfCBQoSBehaviorIndex_Object = MibTableColumn
hpnicfCBQoSBehaviorIndex = _HpnicfCBQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 2, 1, 1),
    _HpnicfCBQoSBehaviorIndex_Type()
)
hpnicfCBQoSBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorIndex.setStatus("current")


class _HpnicfCBQoSBehaviorName_Type(OctetString):
    """Custom type hpnicfCBQoSBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSBehaviorName_Type.__name__ = "OctetString"
_HpnicfCBQoSBehaviorName_Object = MibTableColumn
hpnicfCBQoSBehaviorName = _HpnicfCBQoSBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 2, 1, 2),
    _HpnicfCBQoSBehaviorName_Type()
)
hpnicfCBQoSBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorName.setStatus("current")


class _HpnicfCBQoSBehaviorType_Type(Integer32):
    """Custom type hpnicfCBQoSBehaviorType based on Integer32"""
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


_HpnicfCBQoSBehaviorType_Type.__name__ = "Integer32"
_HpnicfCBQoSBehaviorType_Object = MibTableColumn
hpnicfCBQoSBehaviorType = _HpnicfCBQoSBehaviorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 2, 1, 3),
    _HpnicfCBQoSBehaviorType_Type()
)
hpnicfCBQoSBehaviorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorType.setStatus("current")
_HpnicfCBQoSBehaviorRowStatus_Type = RowStatus
_HpnicfCBQoSBehaviorRowStatus_Object = MibTableColumn
hpnicfCBQoSBehaviorRowStatus = _HpnicfCBQoSBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 2, 1, 4),
    _HpnicfCBQoSBehaviorRowStatus_Type()
)
hpnicfCBQoSBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSBehaviorRowStatus.setStatus("current")
_HpnicfCBQoSCarCfgInfoTable_Object = MibTable
hpnicfCBQoSCarCfgInfoTable = _HpnicfCBQoSCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCarCfgInfoTable.setStatus("current")
_HpnicfCBQoSCarCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSCarCfgInfoEntry = _HpnicfCBQoSCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1)
)
hpnicfCBQoSCarCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCarCfgInfoEntry.setStatus("current")
_HpnicfCBQoSCarCir_Type = Unsigned32
_HpnicfCBQoSCarCir_Object = MibTableColumn
hpnicfCBQoSCarCir = _HpnicfCBQoSCarCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 1),
    _HpnicfCBQoSCarCir_Type()
)
hpnicfCBQoSCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarCir.setStatus("current")
_HpnicfCBQoSCarCbs_Type = Unsigned32
_HpnicfCBQoSCarCbs_Object = MibTableColumn
hpnicfCBQoSCarCbs = _HpnicfCBQoSCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 2),
    _HpnicfCBQoSCarCbs_Type()
)
hpnicfCBQoSCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarCbs.setStatus("current")


class _HpnicfCBQoSCarEbs_Type(Unsigned32):
    """Custom type hpnicfCBQoSCarEbs based on Unsigned32"""
    defaultValue = 0


_HpnicfCBQoSCarEbs_Object = MibTableColumn
hpnicfCBQoSCarEbs = _HpnicfCBQoSCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 3),
    _HpnicfCBQoSCarEbs_Type()
)
hpnicfCBQoSCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarEbs.setStatus("current")
_HpnicfCBQoSCarPir_Type = Unsigned32
_HpnicfCBQoSCarPir_Object = MibTableColumn
hpnicfCBQoSCarPir = _HpnicfCBQoSCarPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 4),
    _HpnicfCBQoSCarPir_Type()
)
hpnicfCBQoSCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarPir.setStatus("current")
_HpnicfCBQoSCarPbs_Type = Unsigned32
_HpnicfCBQoSCarPbs_Object = MibTableColumn
hpnicfCBQoSCarPbs = _HpnicfCBQoSCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 5),
    _HpnicfCBQoSCarPbs_Type()
)
hpnicfCBQoSCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarPbs.setStatus("current")


class _HpnicfCBQoSCarGreenAction_Type(CarAction):
    """Custom type hpnicfCBQoSCarGreenAction based on CarAction"""


_HpnicfCBQoSCarGreenAction_Object = MibTableColumn
hpnicfCBQoSCarGreenAction = _HpnicfCBQoSCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 6),
    _HpnicfCBQoSCarGreenAction_Type()
)
hpnicfCBQoSCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarGreenAction.setStatus("current")


class _HpnicfCBQoSCarGreenRemarkValue_Type(Integer32):
    """Custom type hpnicfCBQoSCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfCBQoSCarGreenRemarkValue_Type.__name__ = "Integer32"
_HpnicfCBQoSCarGreenRemarkValue_Object = MibTableColumn
hpnicfCBQoSCarGreenRemarkValue = _HpnicfCBQoSCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 7),
    _HpnicfCBQoSCarGreenRemarkValue_Type()
)
hpnicfCBQoSCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarGreenRemarkValue.setStatus("current")


class _HpnicfCBQoSCarYellowAction_Type(CarAction):
    """Custom type hpnicfCBQoSCarYellowAction based on CarAction"""


_HpnicfCBQoSCarYellowAction_Object = MibTableColumn
hpnicfCBQoSCarYellowAction = _HpnicfCBQoSCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 8),
    _HpnicfCBQoSCarYellowAction_Type()
)
hpnicfCBQoSCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarYellowAction.setStatus("current")


class _HpnicfCBQoSCarYellowRemarkValue_Type(Integer32):
    """Custom type hpnicfCBQoSCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfCBQoSCarYellowRemarkValue_Type.__name__ = "Integer32"
_HpnicfCBQoSCarYellowRemarkValue_Object = MibTableColumn
hpnicfCBQoSCarYellowRemarkValue = _HpnicfCBQoSCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 9),
    _HpnicfCBQoSCarYellowRemarkValue_Type()
)
hpnicfCBQoSCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarYellowRemarkValue.setStatus("current")


class _HpnicfCBQoSCarRedAction_Type(CarAction):
    """Custom type hpnicfCBQoSCarRedAction based on CarAction"""


_HpnicfCBQoSCarRedAction_Object = MibTableColumn
hpnicfCBQoSCarRedAction = _HpnicfCBQoSCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 10),
    _HpnicfCBQoSCarRedAction_Type()
)
hpnicfCBQoSCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRedAction.setStatus("current")


class _HpnicfCBQoSCarRedRemarkValue_Type(Integer32):
    """Custom type hpnicfCBQoSCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfCBQoSCarRedRemarkValue_Type.__name__ = "Integer32"
_HpnicfCBQoSCarRedRemarkValue_Object = MibTableColumn
hpnicfCBQoSCarRedRemarkValue = _HpnicfCBQoSCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 11),
    _HpnicfCBQoSCarRedRemarkValue_Type()
)
hpnicfCBQoSCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRedRemarkValue.setStatus("current")


class _HpnicfCBQoSCarPolicedPriorityMapType_Type(Integer32):
    """Custom type hpnicfCBQoSCarPolicedPriorityMapType based on Integer32"""
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


_HpnicfCBQoSCarPolicedPriorityMapType_Type.__name__ = "Integer32"
_HpnicfCBQoSCarPolicedPriorityMapType_Object = MibTableColumn
hpnicfCBQoSCarPolicedPriorityMapType = _HpnicfCBQoSCarPolicedPriorityMapType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 12),
    _HpnicfCBQoSCarPolicedPriorityMapType_Type()
)
hpnicfCBQoSCarPolicedPriorityMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarPolicedPriorityMapType.setStatus("current")
_HpnicfCBQoSCarRowStatus_Type = RowStatus
_HpnicfCBQoSCarRowStatus_Object = MibTableColumn
hpnicfCBQoSCarRowStatus = _HpnicfCBQoSCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 3, 1, 13),
    _HpnicfCBQoSCarRowStatus_Type()
)
hpnicfCBQoSCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRowStatus.setStatus("current")
_HpnicfCBQoSAggregativeCarCfgInfoTable_Object = MibTable
hpnicfCBQoSAggregativeCarCfgInfoTable = _HpnicfCBQoSAggregativeCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAggregativeCarCfgInfoTable.setStatus("current")
_HpnicfCBQoSAggregativeCarCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSAggregativeCarCfgInfoEntry = _HpnicfCBQoSAggregativeCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 4, 1)
)
hpnicfCBQoSAggregativeCarCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSCarAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAggregativeCarCfgInfoEntry.setStatus("current")
_HpnicfCBQoSCarAggregativeCarIndex_Type = Integer32
_HpnicfCBQoSCarAggregativeCarIndex_Object = MibTableColumn
hpnicfCBQoSCarAggregativeCarIndex = _HpnicfCBQoSCarAggregativeCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 4, 1, 1),
    _HpnicfCBQoSCarAggregativeCarIndex_Type()
)
hpnicfCBQoSCarAggregativeCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarAggregativeCarIndex.setStatus("current")


class _HpnicfCBQoSCarAggregativeCarName_Type(OctetString):
    """Custom type hpnicfCBQoSCarAggregativeCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSCarAggregativeCarName_Type.__name__ = "OctetString"
_HpnicfCBQoSCarAggregativeCarName_Object = MibTableColumn
hpnicfCBQoSCarAggregativeCarName = _HpnicfCBQoSCarAggregativeCarName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 4, 1, 2),
    _HpnicfCBQoSCarAggregativeCarName_Type()
)
hpnicfCBQoSCarAggregativeCarName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarAggregativeCarName.setStatus("current")
_HpnicfCBQoSAggregativeCarRowStatus_Type = RowStatus
_HpnicfCBQoSAggregativeCarRowStatus_Object = MibTableColumn
hpnicfCBQoSAggregativeCarRowStatus = _HpnicfCBQoSAggregativeCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 4, 1, 3),
    _HpnicfCBQoSAggregativeCarRowStatus_Type()
)
hpnicfCBQoSAggregativeCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSAggregativeCarRowStatus.setStatus("current")
_HpnicfCBQoSGtsCfgInfoTable_Object = MibTable
hpnicfCBQoSGtsCfgInfoTable = _HpnicfCBQoSGtsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsCfgInfoTable.setStatus("current")
_HpnicfCBQoSGtsCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSGtsCfgInfoEntry = _HpnicfCBQoSGtsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1)
)
hpnicfCBQoSGtsCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsCfgInfoEntry.setStatus("current")
_HpnicfCBQoSGtsCir_Type = Unsigned32
_HpnicfCBQoSGtsCir_Object = MibTableColumn
hpnicfCBQoSGtsCir = _HpnicfCBQoSGtsCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1, 1),
    _HpnicfCBQoSGtsCir_Type()
)
hpnicfCBQoSGtsCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsCir.setStatus("current")
_HpnicfCBQoSGtsCbs_Type = Unsigned32
_HpnicfCBQoSGtsCbs_Object = MibTableColumn
hpnicfCBQoSGtsCbs = _HpnicfCBQoSGtsCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1, 2),
    _HpnicfCBQoSGtsCbs_Type()
)
hpnicfCBQoSGtsCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsCbs.setStatus("current")
_HpnicfCBQoSGtsEbs_Type = Unsigned32
_HpnicfCBQoSGtsEbs_Object = MibTableColumn
hpnicfCBQoSGtsEbs = _HpnicfCBQoSGtsEbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1, 3),
    _HpnicfCBQoSGtsEbs_Type()
)
hpnicfCBQoSGtsEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsEbs.setStatus("current")


class _HpnicfCBQoSGtsQueueLength_Type(Integer32):
    """Custom type hpnicfCBQoSGtsQueueLength based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfCBQoSGtsQueueLength_Type.__name__ = "Integer32"
_HpnicfCBQoSGtsQueueLength_Object = MibTableColumn
hpnicfCBQoSGtsQueueLength = _HpnicfCBQoSGtsQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1, 4),
    _HpnicfCBQoSGtsQueueLength_Type()
)
hpnicfCBQoSGtsQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsQueueLength.setStatus("current")
_HpnicfCBQoSGtsRowStatus_Type = RowStatus
_HpnicfCBQoSGtsRowStatus_Object = MibTableColumn
hpnicfCBQoSGtsRowStatus = _HpnicfCBQoSGtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1, 5),
    _HpnicfCBQoSGtsRowStatus_Type()
)
hpnicfCBQoSGtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsRowStatus.setStatus("current")
_HpnicfCBQoSGtsPir_Type = Unsigned32
_HpnicfCBQoSGtsPir_Object = MibTableColumn
hpnicfCBQoSGtsPir = _HpnicfCBQoSGtsPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 5, 1, 6),
    _HpnicfCBQoSGtsPir_Type()
)
hpnicfCBQoSGtsPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsPir.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsPir.setUnits("kbps")
_HpnicfCBQoSRemarkCfgInfoTable_Object = MibTable
hpnicfCBQoSRemarkCfgInfoTable = _HpnicfCBQoSRemarkCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkCfgInfoTable.setStatus("current")
_HpnicfCBQoSRemarkCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSRemarkCfgInfoEntry = _HpnicfCBQoSRemarkCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 6, 1)
)
hpnicfCBQoSRemarkCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSRemarkType"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkCfgInfoEntry.setStatus("current")
_HpnicfCBQoSRemarkType_Type = RemarkType
_HpnicfCBQoSRemarkType_Object = MibTableColumn
hpnicfCBQoSRemarkType = _HpnicfCBQoSRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 6, 1, 1),
    _HpnicfCBQoSRemarkType_Type()
)
hpnicfCBQoSRemarkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkType.setStatus("current")


class _HpnicfCBQoSRemarkValue_Type(Integer32):
    """Custom type hpnicfCBQoSRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HpnicfCBQoSRemarkValue_Type.__name__ = "Integer32"
_HpnicfCBQoSRemarkValue_Object = MibTableColumn
hpnicfCBQoSRemarkValue = _HpnicfCBQoSRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 6, 1, 2),
    _HpnicfCBQoSRemarkValue_Type()
)
hpnicfCBQoSRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkValue.setStatus("current")
_HpnicfCBQoSRemarkRowStatus_Type = RowStatus
_HpnicfCBQoSRemarkRowStatus_Object = MibTableColumn
hpnicfCBQoSRemarkRowStatus = _HpnicfCBQoSRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 6, 1, 3),
    _HpnicfCBQoSRemarkRowStatus_Type()
)
hpnicfCBQoSRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkRowStatus.setStatus("current")
_HpnicfCBQoSQueueCfgInfoTable_Object = MibTable
hpnicfCBQoSQueueCfgInfoTable = _HpnicfCBQoSQueueCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueCfgInfoTable.setStatus("current")
_HpnicfCBQoSQueueCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSQueueCfgInfoEntry = _HpnicfCBQoSQueueCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1)
)
hpnicfCBQoSQueueCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueCfgInfoEntry.setStatus("current")
_HpnicfCBQoSQueueType_Type = QueueType
_HpnicfCBQoSQueueType_Object = MibTableColumn
hpnicfCBQoSQueueType = _HpnicfCBQoSQueueType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 1),
    _HpnicfCBQoSQueueType_Type()
)
hpnicfCBQoSQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueType.setStatus("current")


class _HpnicfCBQoSQueueDropType_Type(Integer32):
    """Custom type hpnicfCBQoSQueueDropType based on Integer32"""
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


_HpnicfCBQoSQueueDropType_Type.__name__ = "Integer32"
_HpnicfCBQoSQueueDropType_Object = MibTableColumn
hpnicfCBQoSQueueDropType = _HpnicfCBQoSQueueDropType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 2),
    _HpnicfCBQoSQueueDropType_Type()
)
hpnicfCBQoSQueueDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueDropType.setStatus("current")


class _HpnicfCBQoSQueueLength_Type(Integer32):
    """Custom type hpnicfCBQoSQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCBQoSQueueLength_Type.__name__ = "Integer32"
_HpnicfCBQoSQueueLength_Object = MibTableColumn
hpnicfCBQoSQueueLength = _HpnicfCBQoSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 3),
    _HpnicfCBQoSQueueLength_Type()
)
hpnicfCBQoSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueLength.setStatus("current")
_HpnicfCBQoSQueueBandwidthUnit_Type = QueueBandwidthUnit
_HpnicfCBQoSQueueBandwidthUnit_Object = MibTableColumn
hpnicfCBQoSQueueBandwidthUnit = _HpnicfCBQoSQueueBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 4),
    _HpnicfCBQoSQueueBandwidthUnit_Type()
)
hpnicfCBQoSQueueBandwidthUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueBandwidthUnit.setStatus("current")


class _HpnicfCBQoSQueueBandwidthValue_Type(Integer32):
    """Custom type hpnicfCBQoSQueueBandwidthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HpnicfCBQoSQueueBandwidthValue_Type.__name__ = "Integer32"
_HpnicfCBQoSQueueBandwidthValue_Object = MibTableColumn
hpnicfCBQoSQueueBandwidthValue = _HpnicfCBQoSQueueBandwidthValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 5),
    _HpnicfCBQoSQueueBandwidthValue_Type()
)
hpnicfCBQoSQueueBandwidthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueBandwidthValue.setStatus("current")


class _HpnicfCBQoSQueueCbs_Type(Integer32):
    """Custom type hpnicfCBQoSQueueCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1000000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HpnicfCBQoSQueueCbs_Type.__name__ = "Integer32"
_HpnicfCBQoSQueueCbs_Object = MibTableColumn
hpnicfCBQoSQueueCbs = _HpnicfCBQoSQueueCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 6),
    _HpnicfCBQoSQueueCbs_Type()
)
hpnicfCBQoSQueueCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueCbs.setStatus("current")


class _HpnicfCBQoSQueueQueueNumber_Type(Integer32):
    """Custom type hpnicfCBQoSQueueQueueNumber based on Integer32"""
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


_HpnicfCBQoSQueueQueueNumber_Type.__name__ = "Integer32"
_HpnicfCBQoSQueueQueueNumber_Object = MibTableColumn
hpnicfCBQoSQueueQueueNumber = _HpnicfCBQoSQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 7),
    _HpnicfCBQoSQueueQueueNumber_Type()
)
hpnicfCBQoSQueueQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueQueueNumber.setStatus("current")


class _HpnicfCBQoSQueueCbsRatio_Type(Integer32):
    """Custom type hpnicfCBQoSQueueCbsRatio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HpnicfCBQoSQueueCbsRatio_Type.__name__ = "Integer32"
_HpnicfCBQoSQueueCbsRatio_Object = MibTableColumn
hpnicfCBQoSQueueCbsRatio = _HpnicfCBQoSQueueCbsRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 8),
    _HpnicfCBQoSQueueCbsRatio_Type()
)
hpnicfCBQoSQueueCbsRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueCbsRatio.setStatus("current")
_HpnicfCBQoSQueueRowStatus_Type = RowStatus
_HpnicfCBQoSQueueRowStatus_Object = MibTableColumn
hpnicfCBQoSQueueRowStatus = _HpnicfCBQoSQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 7, 1, 9),
    _HpnicfCBQoSQueueRowStatus_Type()
)
hpnicfCBQoSQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueRowStatus.setStatus("current")
_HpnicfCBQoSWredCfgInfoTable_Object = MibTable
hpnicfCBQoSWredCfgInfoTable = _HpnicfCBQoSWredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSWredCfgInfoTable.setStatus("current")
_HpnicfCBQoSWredCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSWredCfgInfoEntry = _HpnicfCBQoSWredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 8, 1)
)
hpnicfCBQoSWredCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSWredCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSWredType_Type(WredType):
    """Custom type hpnicfCBQoSWredType based on WredType"""
    defaultValue = 1


_HpnicfCBQoSWredType_Object = MibTableColumn
hpnicfCBQoSWredType = _HpnicfCBQoSWredType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 8, 1, 1),
    _HpnicfCBQoSWredType_Type()
)
hpnicfCBQoSWredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredType.setStatus("current")


class _HpnicfCBQoSWredWeightConst_Type(Integer32):
    """Custom type hpnicfCBQoSWredWeightConst based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfCBQoSWredWeightConst_Type.__name__ = "Integer32"
_HpnicfCBQoSWredWeightConst_Object = MibTableColumn
hpnicfCBQoSWredWeightConst = _HpnicfCBQoSWredWeightConst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 8, 1, 2),
    _HpnicfCBQoSWredWeightConst_Type()
)
hpnicfCBQoSWredWeightConst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredWeightConst.setStatus("current")
_HpnicfCBQoSWredClassCfgInfoTable_Object = MibTable
hpnicfCBQoSWredClassCfgInfoTable = _HpnicfCBQoSWredClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSWredClassCfgInfoTable.setStatus("current")
_HpnicfCBQoSWredClassCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSWredClassCfgInfoEntry = _HpnicfCBQoSWredClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 9, 1)
)
hpnicfCBQoSWredClassCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSWredClassCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSWredClassValue_Type(Integer32):
    """Custom type hpnicfCBQoSWredClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfCBQoSWredClassValue_Type.__name__ = "Integer32"
_HpnicfCBQoSWredClassValue_Object = MibTableColumn
hpnicfCBQoSWredClassValue = _HpnicfCBQoSWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 9, 1, 1),
    _HpnicfCBQoSWredClassValue_Type()
)
hpnicfCBQoSWredClassValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredClassValue.setStatus("current")


class _HpnicfCBQoSWredClassLowLimit_Type(Integer32):
    """Custom type hpnicfCBQoSWredClassLowLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfCBQoSWredClassLowLimit_Type.__name__ = "Integer32"
_HpnicfCBQoSWredClassLowLimit_Object = MibTableColumn
hpnicfCBQoSWredClassLowLimit = _HpnicfCBQoSWredClassLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 9, 1, 2),
    _HpnicfCBQoSWredClassLowLimit_Type()
)
hpnicfCBQoSWredClassLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredClassLowLimit.setStatus("current")


class _HpnicfCBQoSWredClassHighLimit_Type(Integer32):
    """Custom type hpnicfCBQoSWredClassHighLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfCBQoSWredClassHighLimit_Type.__name__ = "Integer32"
_HpnicfCBQoSWredClassHighLimit_Object = MibTableColumn
hpnicfCBQoSWredClassHighLimit = _HpnicfCBQoSWredClassHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 9, 1, 3),
    _HpnicfCBQoSWredClassHighLimit_Type()
)
hpnicfCBQoSWredClassHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredClassHighLimit.setStatus("current")


class _HpnicfCBQoSWredClassDiscardProb_Type(Integer32):
    """Custom type hpnicfCBQoSWredClassDiscardProb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfCBQoSWredClassDiscardProb_Type.__name__ = "Integer32"
_HpnicfCBQoSWredClassDiscardProb_Object = MibTableColumn
hpnicfCBQoSWredClassDiscardProb = _HpnicfCBQoSWredClassDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 9, 1, 4),
    _HpnicfCBQoSWredClassDiscardProb_Type()
)
hpnicfCBQoSWredClassDiscardProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredClassDiscardProb.setStatus("current")
_HpnicfCBQoSPolicyRouteCfgInfoTable_Object = MibTable
hpnicfCBQoSPolicyRouteCfgInfoTable = _HpnicfCBQoSPolicyRouteCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRouteCfgInfoTable.setStatus("current")
_HpnicfCBQoSPolicyRouteCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSPolicyRouteCfgInfoEntry = _HpnicfCBQoSPolicyRouteCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 10, 1)
)
hpnicfCBQoSPolicyRouteCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRouteCfgInfoEntry.setStatus("current")
_HpnicfCBQoSPolicyRouteIpAddrType_Type = InetAddressType
_HpnicfCBQoSPolicyRouteIpAddrType_Object = MibTableColumn
hpnicfCBQoSPolicyRouteIpAddrType = _HpnicfCBQoSPolicyRouteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 10, 1, 1),
    _HpnicfCBQoSPolicyRouteIpAddrType_Type()
)
hpnicfCBQoSPolicyRouteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRouteIpAddrType.setStatus("current")
_HpnicfCBQoSPolicyRouteNexthop_Type = InetAddress
_HpnicfCBQoSPolicyRouteNexthop_Object = MibTableColumn
hpnicfCBQoSPolicyRouteNexthop = _HpnicfCBQoSPolicyRouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 10, 1, 2),
    _HpnicfCBQoSPolicyRouteNexthop_Type()
)
hpnicfCBQoSPolicyRouteNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRouteNexthop.setStatus("current")


class _HpnicfCBQoSPolicyRouteBackup_Type(Integer32):
    """Custom type hpnicfCBQoSPolicyRouteBackup based on Integer32"""
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


_HpnicfCBQoSPolicyRouteBackup_Type.__name__ = "Integer32"
_HpnicfCBQoSPolicyRouteBackup_Object = MibTableColumn
hpnicfCBQoSPolicyRouteBackup = _HpnicfCBQoSPolicyRouteBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 10, 1, 3),
    _HpnicfCBQoSPolicyRouteBackup_Type()
)
hpnicfCBQoSPolicyRouteBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRouteBackup.setStatus("current")
_HpnicfCBQoSPolicyRouteRowStatus_Type = RowStatus
_HpnicfCBQoSPolicyRouteRowStatus_Object = MibTableColumn
hpnicfCBQoSPolicyRouteRowStatus = _HpnicfCBQoSPolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 10, 1, 4),
    _HpnicfCBQoSPolicyRouteRowStatus_Type()
)
hpnicfCBQoSPolicyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRouteRowStatus.setStatus("current")
_HpnicfCBQoSNatCfgInfoTable_Object = MibTable
hpnicfCBQoSNatCfgInfoTable = _HpnicfCBQoSNatCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNatCfgInfoTable.setStatus("current")
_HpnicfCBQoSNatCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSNatCfgInfoEntry = _HpnicfCBQoSNatCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 11, 1)
)
hpnicfCBQoSNatCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNatCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSNatMainNumber_Type(Integer32):
    """Custom type hpnicfCBQoSNatMainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfCBQoSNatMainNumber_Type.__name__ = "Integer32"
_HpnicfCBQoSNatMainNumber_Object = MibTableColumn
hpnicfCBQoSNatMainNumber = _HpnicfCBQoSNatMainNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 11, 1, 1),
    _HpnicfCBQoSNatMainNumber_Type()
)
hpnicfCBQoSNatMainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNatMainNumber.setStatus("current")


class _HpnicfCBQoSNatBackupNumber_Type(Integer32):
    """Custom type hpnicfCBQoSNatBackupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfCBQoSNatBackupNumber_Type.__name__ = "Integer32"
_HpnicfCBQoSNatBackupNumber_Object = MibTableColumn
hpnicfCBQoSNatBackupNumber = _HpnicfCBQoSNatBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 11, 1, 2),
    _HpnicfCBQoSNatBackupNumber_Type()
)
hpnicfCBQoSNatBackupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNatBackupNumber.setStatus("current")


class _HpnicfCBQoSNatServiceClass_Type(Integer32):
    """Custom type hpnicfCBQoSNatServiceClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpnicfCBQoSNatServiceClass_Type.__name__ = "Integer32"
_HpnicfCBQoSNatServiceClass_Object = MibTableColumn
hpnicfCBQoSNatServiceClass = _HpnicfCBQoSNatServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 11, 1, 3),
    _HpnicfCBQoSNatServiceClass_Type()
)
hpnicfCBQoSNatServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNatServiceClass.setStatus("current")
_HpnicfCBQoSNatRowStatus_Type = RowStatus
_HpnicfCBQoSNatRowStatus_Object = MibTableColumn
hpnicfCBQoSNatRowStatus = _HpnicfCBQoSNatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 11, 1, 4),
    _HpnicfCBQoSNatRowStatus_Type()
)
hpnicfCBQoSNatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNatRowStatus.setStatus("current")
_HpnicfCBQoSFirewallCfgInfoTable_Object = MibTable
hpnicfCBQoSFirewallCfgInfoTable = _HpnicfCBQoSFirewallCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFirewallCfgInfoTable.setStatus("current")
_HpnicfCBQoSFirewallCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSFirewallCfgInfoEntry = _HpnicfCBQoSFirewallCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 12, 1)
)
hpnicfCBQoSFirewallCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFirewallCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSFirewallAction_Type(Integer32):
    """Custom type hpnicfCBQoSFirewallAction based on Integer32"""
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


_HpnicfCBQoSFirewallAction_Type.__name__ = "Integer32"
_HpnicfCBQoSFirewallAction_Object = MibTableColumn
hpnicfCBQoSFirewallAction = _HpnicfCBQoSFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 12, 1, 1),
    _HpnicfCBQoSFirewallAction_Type()
)
hpnicfCBQoSFirewallAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSFirewallAction.setStatus("current")
_HpnicfCBQoSFirewallRowStatus_Type = RowStatus
_HpnicfCBQoSFirewallRowStatus_Object = MibTableColumn
hpnicfCBQoSFirewallRowStatus = _HpnicfCBQoSFirewallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 12, 1, 2),
    _HpnicfCBQoSFirewallRowStatus_Type()
)
hpnicfCBQoSFirewallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSFirewallRowStatus.setStatus("current")
_HpnicfCBQoSSamplingCfgInfoTable_Object = MibTable
hpnicfCBQoSSamplingCfgInfoTable = _HpnicfCBQoSSamplingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSSamplingCfgInfoTable.setStatus("current")
_HpnicfCBQoSSamplingCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSSamplingCfgInfoEntry = _HpnicfCBQoSSamplingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 13, 1)
)
hpnicfCBQoSSamplingCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSSamplingCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSSamplingNum_Type(Integer32):
    """Custom type hpnicfCBQoSSamplingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfCBQoSSamplingNum_Type.__name__ = "Integer32"
_HpnicfCBQoSSamplingNum_Object = MibTableColumn
hpnicfCBQoSSamplingNum = _HpnicfCBQoSSamplingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 13, 1, 1),
    _HpnicfCBQoSSamplingNum_Type()
)
hpnicfCBQoSSamplingNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSSamplingNum.setStatus("current")
_HpnicfCBQoSSamplingRowStatus_Type = RowStatus
_HpnicfCBQoSSamplingRowStatus_Object = MibTableColumn
hpnicfCBQoSSamplingRowStatus = _HpnicfCBQoSSamplingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 13, 1, 2),
    _HpnicfCBQoSSamplingRowStatus_Type()
)
hpnicfCBQoSSamplingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSSamplingRowStatus.setStatus("current")
_HpnicfCBQoSAccountCfgInfoTable_Object = MibTable
hpnicfCBQoSAccountCfgInfoTable = _HpnicfCBQoSAccountCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountCfgInfoTable.setStatus("current")
_HpnicfCBQoSAccountCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSAccountCfgInfoEntry = _HpnicfCBQoSAccountCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 14, 1)
)
hpnicfCBQoSAccountCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountCfgInfoEntry.setStatus("current")
_HpnicfCBQoSAccounting_Type = TruthValue
_HpnicfCBQoSAccounting_Object = MibTableColumn
hpnicfCBQoSAccounting = _HpnicfCBQoSAccounting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 14, 1, 1),
    _HpnicfCBQoSAccounting_Type()
)
hpnicfCBQoSAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSAccounting.setStatus("current")
_HpnicfCBQoSAccountRowStatus_Type = RowStatus
_HpnicfCBQoSAccountRowStatus_Object = MibTableColumn
hpnicfCBQoSAccountRowStatus = _HpnicfCBQoSAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 14, 1, 2),
    _HpnicfCBQoSAccountRowStatus_Type()
)
hpnicfCBQoSAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountRowStatus.setStatus("current")


class _HpnicfCBQoSAccountingMode_Type(Integer32):
    """Custom type hpnicfCBQoSAccountingMode based on Integer32"""
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
        *(("auto", 1),
          ("both", 4),
          ("byte", 3),
          ("packet", 2))
    )


_HpnicfCBQoSAccountingMode_Type.__name__ = "Integer32"
_HpnicfCBQoSAccountingMode_Object = MibTableColumn
hpnicfCBQoSAccountingMode = _HpnicfCBQoSAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 14, 1, 3),
    _HpnicfCBQoSAccountingMode_Type()
)
hpnicfCBQoSAccountingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountingMode.setStatus("current")
_HpnicfCBQoSRedirectCfgInfoTable_Object = MibTable
hpnicfCBQoSRedirectCfgInfoTable = _HpnicfCBQoSRedirectCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectCfgInfoTable.setStatus("current")
_HpnicfCBQoSRedirectCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSRedirectCfgInfoEntry = _HpnicfCBQoSRedirectCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1)
)
hpnicfCBQoSRedirectCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSRedirectType_Type(Integer32):
    """Custom type hpnicfCBQoSRedirectType based on Integer32"""
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


_HpnicfCBQoSRedirectType_Type.__name__ = "Integer32"
_HpnicfCBQoSRedirectType_Object = MibTableColumn
hpnicfCBQoSRedirectType = _HpnicfCBQoSRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 1),
    _HpnicfCBQoSRedirectType_Type()
)
hpnicfCBQoSRedirectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectType.setStatus("current")


class _HpnicfCBQoSRedirectIfIndex_Type(Integer32):
    """Custom type hpnicfCBQoSRedirectIfIndex based on Integer32"""
    defaultValue = 0


_HpnicfCBQoSRedirectIfIndex_Object = MibTableColumn
hpnicfCBQoSRedirectIfIndex = _HpnicfCBQoSRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 2),
    _HpnicfCBQoSRedirectIfIndex_Type()
)
hpnicfCBQoSRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIfIndex.setStatus("current")


class _HpnicfCBQoSRedirectIpAddressType_Type(InetAddressType):
    """Custom type hpnicfCBQoSRedirectIpAddressType based on InetAddressType"""


_HpnicfCBQoSRedirectIpAddressType_Object = MibTableColumn
hpnicfCBQoSRedirectIpAddressType = _HpnicfCBQoSRedirectIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 3),
    _HpnicfCBQoSRedirectIpAddressType_Type()
)
hpnicfCBQoSRedirectIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIpAddressType.setStatus("current")
_HpnicfCBQoSRedirectIpAddress1_Type = InetAddress
_HpnicfCBQoSRedirectIpAddress1_Object = MibTableColumn
hpnicfCBQoSRedirectIpAddress1 = _HpnicfCBQoSRedirectIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 4),
    _HpnicfCBQoSRedirectIpAddress1_Type()
)
hpnicfCBQoSRedirectIpAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIpAddress1.setStatus("current")
_HpnicfCBQoSRedirectIpAddress2_Type = InetAddress
_HpnicfCBQoSRedirectIpAddress2_Object = MibTableColumn
hpnicfCBQoSRedirectIpAddress2 = _HpnicfCBQoSRedirectIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 5),
    _HpnicfCBQoSRedirectIpAddress2_Type()
)
hpnicfCBQoSRedirectIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIpAddress2.setStatus("current")
_HpnicfCBQoSRedirectRowStatus_Type = RowStatus
_HpnicfCBQoSRedirectRowStatus_Object = MibTableColumn
hpnicfCBQoSRedirectRowStatus = _HpnicfCBQoSRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 6),
    _HpnicfCBQoSRedirectRowStatus_Type()
)
hpnicfCBQoSRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectRowStatus.setStatus("current")


class _HpnicfCBQoSRedirectIpv6Interface1_Type(Integer32):
    """Custom type hpnicfCBQoSRedirectIpv6Interface1 based on Integer32"""
    defaultValue = 0


_HpnicfCBQoSRedirectIpv6Interface1_Object = MibTableColumn
hpnicfCBQoSRedirectIpv6Interface1 = _HpnicfCBQoSRedirectIpv6Interface1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 7),
    _HpnicfCBQoSRedirectIpv6Interface1_Type()
)
hpnicfCBQoSRedirectIpv6Interface1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIpv6Interface1.setStatus("current")


class _HpnicfCBQoSRedirectIpv6Interface2_Type(Integer32):
    """Custom type hpnicfCBQoSRedirectIpv6Interface2 based on Integer32"""
    defaultValue = 0


_HpnicfCBQoSRedirectIpv6Interface2_Object = MibTableColumn
hpnicfCBQoSRedirectIpv6Interface2 = _HpnicfCBQoSRedirectIpv6Interface2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 8),
    _HpnicfCBQoSRedirectIpv6Interface2_Type()
)
hpnicfCBQoSRedirectIpv6Interface2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIpv6Interface2.setStatus("current")


class _HpnicfCBQoSRedirectIfVlanID_Type(Integer32):
    """Custom type hpnicfCBQoSRedirectIfVlanID based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfCBQoSRedirectIfVlanID_Type.__name__ = "Integer32"
_HpnicfCBQoSRedirectIfVlanID_Object = MibTableColumn
hpnicfCBQoSRedirectIfVlanID = _HpnicfCBQoSRedirectIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 15, 1, 9),
    _HpnicfCBQoSRedirectIfVlanID_Type()
)
hpnicfCBQoSRedirectIfVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSRedirectIfVlanID.setStatus("current")
_HpnicfCBQoSPriorityMapCfgInfoTable_Object = MibTable
hpnicfCBQoSPriorityMapCfgInfoTable = _HpnicfCBQoSPriorityMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapCfgInfoTable.setStatus("current")
_HpnicfCBQoSPriorityMapCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSPriorityMapCfgInfoEntry = _HpnicfCBQoSPriorityMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1)
)
hpnicfCBQoSPriorityMapCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSPriorityMapImportType_Type(Integer32):
    """Custom type hpnicfCBQoSPriorityMapImportType based on Integer32"""
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


_HpnicfCBQoSPriorityMapImportType_Type.__name__ = "Integer32"
_HpnicfCBQoSPriorityMapImportType_Object = MibTableColumn
hpnicfCBQoSPriorityMapImportType = _HpnicfCBQoSPriorityMapImportType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1, 1),
    _HpnicfCBQoSPriorityMapImportType_Type()
)
hpnicfCBQoSPriorityMapImportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapImportType.setStatus("current")


class _HpnicfCBQoSPriorityMapExportType_Type(Integer32):
    """Custom type hpnicfCBQoSPriorityMapExportType based on Integer32"""
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


_HpnicfCBQoSPriorityMapExportType_Type.__name__ = "Integer32"
_HpnicfCBQoSPriorityMapExportType_Object = MibTableColumn
hpnicfCBQoSPriorityMapExportType = _HpnicfCBQoSPriorityMapExportType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1, 2),
    _HpnicfCBQoSPriorityMapExportType_Type()
)
hpnicfCBQoSPriorityMapExportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapExportType.setStatus("current")
_HpnicfCBQoSPriorityMapGroupIndex_Type = Integer32
_HpnicfCBQoSPriorityMapGroupIndex_Object = MibTableColumn
hpnicfCBQoSPriorityMapGroupIndex = _HpnicfCBQoSPriorityMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1, 3),
    _HpnicfCBQoSPriorityMapGroupIndex_Type()
)
hpnicfCBQoSPriorityMapGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapGroupIndex.setStatus("current")


class _HpnicfCBQoSPriorityMapGroupName_Type(OctetString):
    """Custom type hpnicfCBQoSPriorityMapGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfCBQoSPriorityMapGroupName_Type.__name__ = "OctetString"
_HpnicfCBQoSPriorityMapGroupName_Object = MibTableColumn
hpnicfCBQoSPriorityMapGroupName = _HpnicfCBQoSPriorityMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1, 4),
    _HpnicfCBQoSPriorityMapGroupName_Type()
)
hpnicfCBQoSPriorityMapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapGroupName.setStatus("current")


class _HpnicfCBQoSPriorityMapAuto_Type(Integer32):
    """Custom type hpnicfCBQoSPriorityMapAuto based on Integer32"""
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


_HpnicfCBQoSPriorityMapAuto_Type.__name__ = "Integer32"
_HpnicfCBQoSPriorityMapAuto_Object = MibTableColumn
hpnicfCBQoSPriorityMapAuto = _HpnicfCBQoSPriorityMapAuto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1, 5),
    _HpnicfCBQoSPriorityMapAuto_Type()
)
hpnicfCBQoSPriorityMapAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapAuto.setStatus("current")
_HpnicfCBQoSPriorityMapRowStatus_Type = RowStatus
_HpnicfCBQoSPriorityMapRowStatus_Object = MibTableColumn
hpnicfCBQoSPriorityMapRowStatus = _HpnicfCBQoSPriorityMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 16, 1, 6),
    _HpnicfCBQoSPriorityMapRowStatus_Type()
)
hpnicfCBQoSPriorityMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPriorityMapRowStatus.setStatus("current")
_HpnicfCBQoSMirrorCfgInfoTable_Object = MibTable
hpnicfCBQoSMirrorCfgInfoTable = _HpnicfCBQoSMirrorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorCfgInfoTable.setStatus("current")
_HpnicfCBQoSMirrorCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSMirrorCfgInfoEntry = _HpnicfCBQoSMirrorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 17, 1)
)
hpnicfCBQoSMirrorCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSMirrorType_Type(Integer32):
    """Custom type hpnicfCBQoSMirrorType based on Integer32"""
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


_HpnicfCBQoSMirrorType_Type.__name__ = "Integer32"
_HpnicfCBQoSMirrorType_Object = MibTableColumn
hpnicfCBQoSMirrorType = _HpnicfCBQoSMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 17, 1, 1),
    _HpnicfCBQoSMirrorType_Type()
)
hpnicfCBQoSMirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorType.setStatus("current")


class _HpnicfCBQoSMirrorIfIndex_Type(OctetString):
    """Custom type hpnicfCBQoSMirrorIfIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCBQoSMirrorIfIndex_Type.__name__ = "OctetString"
_HpnicfCBQoSMirrorIfIndex_Object = MibTableColumn
hpnicfCBQoSMirrorIfIndex = _HpnicfCBQoSMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 17, 1, 2),
    _HpnicfCBQoSMirrorIfIndex_Type()
)
hpnicfCBQoSMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfIndex.setStatus("current")


class _HpnicfCBQoSMirrorVlanID_Type(Integer32):
    """Custom type hpnicfCBQoSMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfCBQoSMirrorVlanID_Type.__name__ = "Integer32"
_HpnicfCBQoSMirrorVlanID_Object = MibTableColumn
hpnicfCBQoSMirrorVlanID = _HpnicfCBQoSMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 17, 1, 3),
    _HpnicfCBQoSMirrorVlanID_Type()
)
hpnicfCBQoSMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorVlanID.setStatus("current")
_HpnicfCBQoSMirrorRowStatus_Type = RowStatus
_HpnicfCBQoSMirrorRowStatus_Object = MibTableColumn
hpnicfCBQoSMirrorRowStatus = _HpnicfCBQoSMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 17, 1, 4),
    _HpnicfCBQoSMirrorRowStatus_Type()
)
hpnicfCBQoSMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorRowStatus.setStatus("current")
_HpnicfCBQoSNestCfgInfoTable_Object = MibTable
hpnicfCBQoSNestCfgInfoTable = _HpnicfCBQoSNestCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNestCfgInfoTable.setStatus("current")
_HpnicfCBQoSNestCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSNestCfgInfoEntry = _HpnicfCBQoSNestCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18, 1)
)
hpnicfCBQoSNestCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNestCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSNestServiceVlanID_Type(Integer32):
    """Custom type hpnicfCBQoSNestServiceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfCBQoSNestServiceVlanID_Type.__name__ = "Integer32"
_HpnicfCBQoSNestServiceVlanID_Object = MibTableColumn
hpnicfCBQoSNestServiceVlanID = _HpnicfCBQoSNestServiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18, 1, 1),
    _HpnicfCBQoSNestServiceVlanID_Type()
)
hpnicfCBQoSNestServiceVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestServiceVlanID.setStatus("current")


class _HpnicfCBQoSNestServiceDot1pValue_Type(Integer32):
    """Custom type hpnicfCBQoSNestServiceDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfCBQoSNestServiceDot1pValue_Type.__name__ = "Integer32"
_HpnicfCBQoSNestServiceDot1pValue_Object = MibTableColumn
hpnicfCBQoSNestServiceDot1pValue = _HpnicfCBQoSNestServiceDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18, 1, 2),
    _HpnicfCBQoSNestServiceDot1pValue_Type()
)
hpnicfCBQoSNestServiceDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestServiceDot1pValue.setStatus("current")


class _HpnicfCBQoSNestCustomerVlanID_Type(Integer32):
    """Custom type hpnicfCBQoSNestCustomerVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfCBQoSNestCustomerVlanID_Type.__name__ = "Integer32"
_HpnicfCBQoSNestCustomerVlanID_Object = MibTableColumn
hpnicfCBQoSNestCustomerVlanID = _HpnicfCBQoSNestCustomerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18, 1, 3),
    _HpnicfCBQoSNestCustomerVlanID_Type()
)
hpnicfCBQoSNestCustomerVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestCustomerVlanID.setStatus("current")


class _HpnicfCBQoSNestCustomerDot1pValue_Type(Integer32):
    """Custom type hpnicfCBQoSNestCustomerDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfCBQoSNestCustomerDot1pValue_Type.__name__ = "Integer32"
_HpnicfCBQoSNestCustomerDot1pValue_Object = MibTableColumn
hpnicfCBQoSNestCustomerDot1pValue = _HpnicfCBQoSNestCustomerDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18, 1, 4),
    _HpnicfCBQoSNestCustomerDot1pValue_Type()
)
hpnicfCBQoSNestCustomerDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestCustomerDot1pValue.setStatus("current")
_HpnicfCBQoSNestRowStatus_Type = RowStatus
_HpnicfCBQoSNestRowStatus_Object = MibTableColumn
hpnicfCBQoSNestRowStatus = _HpnicfCBQoSNestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 18, 1, 5),
    _HpnicfCBQoSNestRowStatus_Type()
)
hpnicfCBQoSNestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestRowStatus.setStatus("current")
_HpnicfCBQoSNestPolicyCfgInfoTable_Object = MibTable
hpnicfCBQoSNestPolicyCfgInfoTable = _HpnicfCBQoSNestPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 19)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyCfgInfoTable.setStatus("current")
_HpnicfCBQoSNestPolicyCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSNestPolicyCfgInfoEntry = _HpnicfCBQoSNestPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 19, 1)
)
hpnicfCBQoSNestPolicyCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSNestPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSNestPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSNestPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSNestPolicyName_Object = MibTableColumn
hpnicfCBQoSNestPolicyName = _HpnicfCBQoSNestPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 19, 1, 1),
    _HpnicfCBQoSNestPolicyName_Type()
)
hpnicfCBQoSNestPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyName.setStatus("current")
_HpnicfCBQoSNestPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSNestPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSNestPolicyRowStatus = _HpnicfCBQoSNestPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 19, 1, 2),
    _HpnicfCBQoSNestPolicyRowStatus_Type()
)
hpnicfCBQoSNestPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyRowStatus.setStatus("current")
_HpnicfCBQoSMirrorIfCfgInfoTable_Object = MibTable
hpnicfCBQoSMirrorIfCfgInfoTable = _HpnicfCBQoSMirrorIfCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfCfgInfoTable.setStatus("current")
_HpnicfCBQoSMirrorIfCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSMirrorIfCfgInfoEntry = _HpnicfCBQoSMirrorIfCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20, 1)
)
hpnicfCBQoSMirrorIfCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSMirrorIfMainIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfCfgInfoEntry.setStatus("current")
_HpnicfCBQoSMirrorIfMainIfIndex_Type = Integer32
_HpnicfCBQoSMirrorIfMainIfIndex_Object = MibTableColumn
hpnicfCBQoSMirrorIfMainIfIndex = _HpnicfCBQoSMirrorIfMainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20, 1, 1),
    _HpnicfCBQoSMirrorIfMainIfIndex_Type()
)
hpnicfCBQoSMirrorIfMainIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfMainIfIndex.setStatus("current")


class _HpnicfCBQoSMirrorIfMainIfStatus_Type(Integer32):
    """Custom type hpnicfCBQoSMirrorIfMainIfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HpnicfCBQoSMirrorIfMainIfStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSMirrorIfMainIfStatus_Object = MibTableColumn
hpnicfCBQoSMirrorIfMainIfStatus = _HpnicfCBQoSMirrorIfMainIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20, 1, 2),
    _HpnicfCBQoSMirrorIfMainIfStatus_Type()
)
hpnicfCBQoSMirrorIfMainIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfMainIfStatus.setStatus("current")
_HpnicfCBQoSMirrorIfBackupIfIndex_Type = Integer32
_HpnicfCBQoSMirrorIfBackupIfIndex_Object = MibTableColumn
hpnicfCBQoSMirrorIfBackupIfIndex = _HpnicfCBQoSMirrorIfBackupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20, 1, 3),
    _HpnicfCBQoSMirrorIfBackupIfIndex_Type()
)
hpnicfCBQoSMirrorIfBackupIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfBackupIfIndex.setStatus("current")


class _HpnicfCBQoSMirrorIfBackupIfStatus_Type(Integer32):
    """Custom type hpnicfCBQoSMirrorIfBackupIfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HpnicfCBQoSMirrorIfBackupIfStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSMirrorIfBackupIfStatus_Object = MibTableColumn
hpnicfCBQoSMirrorIfBackupIfStatus = _HpnicfCBQoSMirrorIfBackupIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20, 1, 4),
    _HpnicfCBQoSMirrorIfBackupIfStatus_Type()
)
hpnicfCBQoSMirrorIfBackupIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfBackupIfStatus.setStatus("current")
_HpnicfCBQoSMirrorIfRowStatus_Type = RowStatus
_HpnicfCBQoSMirrorIfRowStatus_Object = MibTableColumn
hpnicfCBQoSMirrorIfRowStatus = _HpnicfCBQoSMirrorIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 20, 1, 5),
    _HpnicfCBQoSMirrorIfRowStatus_Type()
)
hpnicfCBQoSMirrorIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSMirrorIfRowStatus.setStatus("current")
_HpnicfCBQoSColoredRemarkCfgTable_Object = MibTable
hpnicfCBQoSColoredRemarkCfgTable = _HpnicfCBQoSColoredRemarkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 21)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSColoredRemarkCfgTable.setStatus("current")
_HpnicfCBQoSColoredRemarkCfgEntry_Object = MibTableRow
hpnicfCBQoSColoredRemarkCfgEntry = _HpnicfCBQoSColoredRemarkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 21, 1)
)
hpnicfCBQoSColoredRemarkCfgEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSColoredRemarkType"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSColoredRemarkColor"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSColoredRemarkCfgEntry.setStatus("current")
_HpnicfCBQoSColoredRemarkType_Type = RemarkType
_HpnicfCBQoSColoredRemarkType_Object = MibTableColumn
hpnicfCBQoSColoredRemarkType = _HpnicfCBQoSColoredRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 21, 1, 1),
    _HpnicfCBQoSColoredRemarkType_Type()
)
hpnicfCBQoSColoredRemarkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSColoredRemarkType.setStatus("current")


class _HpnicfCBQoSColoredRemarkColor_Type(Integer32):
    """Custom type hpnicfCBQoSColoredRemarkColor based on Integer32"""
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


_HpnicfCBQoSColoredRemarkColor_Type.__name__ = "Integer32"
_HpnicfCBQoSColoredRemarkColor_Object = MibTableColumn
hpnicfCBQoSColoredRemarkColor = _HpnicfCBQoSColoredRemarkColor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 21, 1, 2),
    _HpnicfCBQoSColoredRemarkColor_Type()
)
hpnicfCBQoSColoredRemarkColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSColoredRemarkColor.setStatus("current")


class _HpnicfCBQoSColoredRemarkValue_Type(Integer32):
    """Custom type hpnicfCBQoSColoredRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HpnicfCBQoSColoredRemarkValue_Type.__name__ = "Integer32"
_HpnicfCBQoSColoredRemarkValue_Object = MibTableColumn
hpnicfCBQoSColoredRemarkValue = _HpnicfCBQoSColoredRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 21, 1, 3),
    _HpnicfCBQoSColoredRemarkValue_Type()
)
hpnicfCBQoSColoredRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSColoredRemarkValue.setStatus("current")
_HpnicfCBQoSColoredRemarkRowStatus_Type = RowStatus
_HpnicfCBQoSColoredRemarkRowStatus_Object = MibTableColumn
hpnicfCBQoSColoredRemarkRowStatus = _HpnicfCBQoSColoredRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 21, 1, 4),
    _HpnicfCBQoSColoredRemarkRowStatus_Type()
)
hpnicfCBQoSColoredRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSColoredRemarkRowStatus.setStatus("current")
_HpnicfCBQoSPrimapCfgInfoTable_Object = MibTable
hpnicfCBQoSPrimapCfgInfoTable = _HpnicfCBQoSPrimapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 22)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPrimapCfgInfoTable.setStatus("current")
_HpnicfCBQoSPrimapCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSPrimapCfgInfoEntry = _HpnicfCBQoSPrimapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 22, 1)
)
hpnicfCBQoSPrimapCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPrimapColorType"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPrePriMapTableType"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPrimapCfgInfoEntry.setStatus("current")


class _HpnicfCBQoSPrimapColorType_Type(Integer32):
    """Custom type hpnicfCBQoSPrimapColorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorMap", 2),
          ("noColorMap", 1))
    )


_HpnicfCBQoSPrimapColorType_Type.__name__ = "Integer32"
_HpnicfCBQoSPrimapColorType_Object = MibTableColumn
hpnicfCBQoSPrimapColorType = _HpnicfCBQoSPrimapColorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 22, 1, 1),
    _HpnicfCBQoSPrimapColorType_Type()
)
hpnicfCBQoSPrimapColorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSPrimapColorType.setStatus("current")


class _HpnicfCBQoSPrePriMapTableType_Type(Integer32):
    """Custom type hpnicfCBQoSPrePriMapTableType based on Integer32"""
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("dot11eToLp", 27),
          ("dot1pToDot1p", 34),
          ("dot1pToDp", 2),
          ("dot1pToDscp", 8),
          ("dot1pToExp", 30),
          ("dot1pToLp", 1),
          ("dot1pToRpr", 15),
          ("dscpToDot1p", 7),
          ("dscpToDp", 6),
          ("dscpToDscp", 9),
          ("dscpToExp", 10),
          ("dscpToLp", 4),
          ("dscpToRpr", 16),
          ("expToDot1p", 12),
          ("expToDp", 5),
          ("expToDscp", 11),
          ("expToExp", 13),
          ("expToLp", 3),
          ("expToRpr", 17),
          ("ippreToRpr", 18),
          ("lpToDot11e", 28),
          ("lpToDot1p", 14),
          ("lpToDp", 32),
          ("lpToExp", 31),
          ("lpToLp", 29),
          ("lpTodscp", 26),
          ("upToDot1p", 19),
          ("upToDp", 22),
          ("upToDscp", 20),
          ("upToExp", 21),
          ("upToFc", 25),
          ("upToLp", 23),
          ("upToRpr", 24),
          ("upToUp", 33))
    )


_HpnicfCBQoSPrePriMapTableType_Type.__name__ = "Integer32"
_HpnicfCBQoSPrePriMapTableType_Object = MibTableColumn
hpnicfCBQoSPrePriMapTableType = _HpnicfCBQoSPrePriMapTableType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 22, 1, 2),
    _HpnicfCBQoSPrePriMapTableType_Type()
)
hpnicfCBQoSPrePriMapTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSPrePriMapTableType.setStatus("current")
_HpnicfCBQoSPrimapRowStatus_Type = RowStatus
_HpnicfCBQoSPrimapRowStatus_Object = MibTableColumn
hpnicfCBQoSPrimapRowStatus = _HpnicfCBQoSPrimapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 22, 1, 3),
    _HpnicfCBQoSPrimapRowStatus_Type()
)
hpnicfCBQoSPrimapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPrimapRowStatus.setStatus("current")
_HpnicfCBQoSColorMapDpCfgInfoTable_Object = MibTable
hpnicfCBQoSColorMapDpCfgInfoTable = _HpnicfCBQoSColorMapDpCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 23)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSColorMapDpCfgInfoTable.setStatus("current")
_HpnicfCBQoSColorMapDpCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSColorMapDpCfgInfoEntry = _HpnicfCBQoSColorMapDpCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 23, 1)
)
hpnicfCBQoSColorMapDpCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSColorMapDpCfgInfoEntry.setStatus("current")
_HpnicfCBQoSColorMapDpEnable_Type = TruthValue
_HpnicfCBQoSColorMapDpEnable_Object = MibTableColumn
hpnicfCBQoSColorMapDpEnable = _HpnicfCBQoSColorMapDpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 23, 1, 1),
    _HpnicfCBQoSColorMapDpEnable_Type()
)
hpnicfCBQoSColorMapDpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSColorMapDpEnable.setStatus("current")
_HpnicfCBQoSColorMapDpRowStatus_Type = RowStatus
_HpnicfCBQoSColorMapDpRowStatus_Object = MibTableColumn
hpnicfCBQoSColorMapDpRowStatus = _HpnicfCBQoSColorMapDpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 2, 23, 1, 2),
    _HpnicfCBQoSColorMapDpRowStatus_Type()
)
hpnicfCBQoSColorMapDpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSColorMapDpRowStatus.setStatus("current")
_HpnicfCBQoSPolicyObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSPolicyObjects = _HpnicfCBQoSPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3)
)
_HpnicfCBQoSPolicyIndexNext_Type = Integer32
_HpnicfCBQoSPolicyIndexNext_Object = MibScalar
hpnicfCBQoSPolicyIndexNext = _HpnicfCBQoSPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 1),
    _HpnicfCBQoSPolicyIndexNext_Type()
)
hpnicfCBQoSPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyIndexNext.setStatus("current")
_HpnicfCBQoSPolicyCfgInfoTable_Object = MibTable
hpnicfCBQoSPolicyCfgInfoTable = _HpnicfCBQoSPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyCfgInfoTable.setStatus("current")
_HpnicfCBQoSPolicyCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSPolicyCfgInfoEntry = _HpnicfCBQoSPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1)
)
hpnicfCBQoSPolicyCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyCfgInfoEntry.setStatus("current")
_HpnicfCBQoSPolicyIndex_Type = Integer32
_HpnicfCBQoSPolicyIndex_Object = MibTableColumn
hpnicfCBQoSPolicyIndex = _HpnicfCBQoSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 1),
    _HpnicfCBQoSPolicyIndex_Type()
)
hpnicfCBQoSPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyIndex.setStatus("current")


class _HpnicfCBQoSPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSPolicyName_Object = MibTableColumn
hpnicfCBQoSPolicyName = _HpnicfCBQoSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 2),
    _HpnicfCBQoSPolicyName_Type()
)
hpnicfCBQoSPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyName.setStatus("current")
_HpnicfCBQoSPolicyClassCount_Type = Integer32
_HpnicfCBQoSPolicyClassCount_Object = MibTableColumn
hpnicfCBQoSPolicyClassCount = _HpnicfCBQoSPolicyClassCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 3),
    _HpnicfCBQoSPolicyClassCount_Type()
)
hpnicfCBQoSPolicyClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassCount.setStatus("current")


class _HpnicfCBQoSPolicyConfigMode_Type(Integer32):
    """Custom type hpnicfCBQoSPolicyConfigMode based on Integer32"""
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


_HpnicfCBQoSPolicyConfigMode_Type.__name__ = "Integer32"
_HpnicfCBQoSPolicyConfigMode_Object = MibTableColumn
hpnicfCBQoSPolicyConfigMode = _HpnicfCBQoSPolicyConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 4),
    _HpnicfCBQoSPolicyConfigMode_Type()
)
hpnicfCBQoSPolicyConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyConfigMode.setStatus("current")


class _HpnicfCBQoSPolicyType_Type(Integer32):
    """Custom type hpnicfCBQoSPolicyType based on Integer32"""
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


_HpnicfCBQoSPolicyType_Type.__name__ = "Integer32"
_HpnicfCBQoSPolicyType_Object = MibTableColumn
hpnicfCBQoSPolicyType = _HpnicfCBQoSPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 5),
    _HpnicfCBQoSPolicyType_Type()
)
hpnicfCBQoSPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyType.setStatus("current")
_HpnicfCBQoSPolicyClassNextIndex_Type = Integer32
_HpnicfCBQoSPolicyClassNextIndex_Object = MibTableColumn
hpnicfCBQoSPolicyClassNextIndex = _HpnicfCBQoSPolicyClassNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 6),
    _HpnicfCBQoSPolicyClassNextIndex_Type()
)
hpnicfCBQoSPolicyClassNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassNextIndex.setStatus("current")
_HpnicfCBQoSPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSPolicyRowStatus = _HpnicfCBQoSPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 2, 1, 7),
    _HpnicfCBQoSPolicyRowStatus_Type()
)
hpnicfCBQoSPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyRowStatus.setStatus("current")
_HpnicfCBQoSPolicyClassCfgInfoTable_Object = MibTable
hpnicfCBQoSPolicyClassCfgInfoTable = _HpnicfCBQoSPolicyClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassCfgInfoTable.setStatus("current")
_HpnicfCBQoSPolicyClassCfgInfoEntry_Object = MibTableRow
hpnicfCBQoSPolicyClassCfgInfoEntry = _HpnicfCBQoSPolicyClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1)
)
hpnicfCBQoSPolicyClassCfgInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassCfgInfoEntry.setStatus("current")
_HpnicfCBQoSPolicyClassIndex_Type = Integer32
_HpnicfCBQoSPolicyClassIndex_Object = MibTableColumn
hpnicfCBQoSPolicyClassIndex = _HpnicfCBQoSPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 1),
    _HpnicfCBQoSPolicyClassIndex_Type()
)
hpnicfCBQoSPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassIndex.setStatus("current")
_HpnicfCBQoSPolicyClassClassifierIndex_Type = Integer32
_HpnicfCBQoSPolicyClassClassifierIndex_Object = MibTableColumn
hpnicfCBQoSPolicyClassClassifierIndex = _HpnicfCBQoSPolicyClassClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 2),
    _HpnicfCBQoSPolicyClassClassifierIndex_Type()
)
hpnicfCBQoSPolicyClassClassifierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassClassifierIndex.setStatus("current")


class _HpnicfCBQoSPolicyClassClassifierName_Type(OctetString):
    """Custom type hpnicfCBQoSPolicyClassClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSPolicyClassClassifierName_Type.__name__ = "OctetString"
_HpnicfCBQoSPolicyClassClassifierName_Object = MibTableColumn
hpnicfCBQoSPolicyClassClassifierName = _HpnicfCBQoSPolicyClassClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 3),
    _HpnicfCBQoSPolicyClassClassifierName_Type()
)
hpnicfCBQoSPolicyClassClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassClassifierName.setStatus("current")
_HpnicfCBQoSPolicyClassBehaviorIndex_Type = Integer32
_HpnicfCBQoSPolicyClassBehaviorIndex_Object = MibTableColumn
hpnicfCBQoSPolicyClassBehaviorIndex = _HpnicfCBQoSPolicyClassBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 4),
    _HpnicfCBQoSPolicyClassBehaviorIndex_Type()
)
hpnicfCBQoSPolicyClassBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassBehaviorIndex.setStatus("current")


class _HpnicfCBQoSPolicyClassBehaviorName_Type(OctetString):
    """Custom type hpnicfCBQoSPolicyClassBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSPolicyClassBehaviorName_Type.__name__ = "OctetString"
_HpnicfCBQoSPolicyClassBehaviorName_Object = MibTableColumn
hpnicfCBQoSPolicyClassBehaviorName = _HpnicfCBQoSPolicyClassBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 5),
    _HpnicfCBQoSPolicyClassBehaviorName_Type()
)
hpnicfCBQoSPolicyClassBehaviorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassBehaviorName.setStatus("current")


class _HpnicfCBQoSPolicyClassPrecedence_Type(Integer32):
    """Custom type hpnicfCBQoSPolicyClassPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HpnicfCBQoSPolicyClassPrecedence_Type.__name__ = "Integer32"
_HpnicfCBQoSPolicyClassPrecedence_Object = MibTableColumn
hpnicfCBQoSPolicyClassPrecedence = _HpnicfCBQoSPolicyClassPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 6),
    _HpnicfCBQoSPolicyClassPrecedence_Type()
)
hpnicfCBQoSPolicyClassPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassPrecedence.setStatus("current")
_HpnicfCBQoSPolicyClassRowStatus_Type = RowStatus
_HpnicfCBQoSPolicyClassRowStatus_Object = MibTableColumn
hpnicfCBQoSPolicyClassRowStatus = _HpnicfCBQoSPolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 7),
    _HpnicfCBQoSPolicyClassRowStatus_Type()
)
hpnicfCBQoSPolicyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassRowStatus.setStatus("current")


class _HpnicfCBQoSPolicyClassMode_Type(Integer32):
    """Custom type hpnicfCBQoSPolicyClassMode based on Integer32"""
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
        *(("modeDCBX", 6),
          ("modeDot1q", 2),
          ("modeIpSourceGuard", 4),
          ("modeNo", 1),
          ("modeQppb", 3),
          ("modeVoiceVlan", 5))
    )


_HpnicfCBQoSPolicyClassMode_Type.__name__ = "Integer32"
_HpnicfCBQoSPolicyClassMode_Object = MibTableColumn
hpnicfCBQoSPolicyClassMode = _HpnicfCBQoSPolicyClassMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 8),
    _HpnicfCBQoSPolicyClassMode_Type()
)
hpnicfCBQoSPolicyClassMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassMode.setStatus("current")
_HpnicfCBQoSPolicyClassCfgOrder_Type = Integer32
_HpnicfCBQoSPolicyClassCfgOrder_Object = MibTableColumn
hpnicfCBQoSPolicyClassCfgOrder = _HpnicfCBQoSPolicyClassCfgOrder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 3, 3, 1, 9),
    _HpnicfCBQoSPolicyClassCfgOrder_Type()
)
hpnicfCBQoSPolicyClassCfgOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPolicyClassCfgOrder.setStatus("current")
_HpnicfCBQoSApplyPolicyObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSApplyPolicyObjects = _HpnicfCBQoSApplyPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4)
)
_HpnicfCBQoSIfApplyPolicyTable_Object = MibTable
hpnicfCBQoSIfApplyPolicyTable = _HpnicfCBQoSIfApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyTable.setStatus("current")
_HpnicfCBQoSIfApplyPolicyEntry_Object = MibTableRow
hpnicfCBQoSIfApplyPolicyEntry = _HpnicfCBQoSIfApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1)
)
hpnicfCBQoSIfApplyPolicyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyEntry.setStatus("current")
_HpnicfCBQoSIfApplyPolicyIfIndex_Type = Integer32
_HpnicfCBQoSIfApplyPolicyIfIndex_Object = MibTableColumn
hpnicfCBQoSIfApplyPolicyIfIndex = _HpnicfCBQoSIfApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1, 1),
    _HpnicfCBQoSIfApplyPolicyIfIndex_Type()
)
hpnicfCBQoSIfApplyPolicyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyIfIndex.setStatus("current")
_HpnicfCBQoSIfApplyPolicyDirection_Type = DirectionType
_HpnicfCBQoSIfApplyPolicyDirection_Object = MibTableColumn
hpnicfCBQoSIfApplyPolicyDirection = _HpnicfCBQoSIfApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1, 2),
    _HpnicfCBQoSIfApplyPolicyDirection_Type()
)
hpnicfCBQoSIfApplyPolicyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyDirection.setStatus("current")


class _HpnicfCBQoSIfApplyPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSIfApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSIfApplyPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSIfApplyPolicyName_Object = MibTableColumn
hpnicfCBQoSIfApplyPolicyName = _HpnicfCBQoSIfApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1, 3),
    _HpnicfCBQoSIfApplyPolicyName_Type()
)
hpnicfCBQoSIfApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyName.setStatus("current")


class _HpnicfCBQoSIfApplyPolicyEnableDynamic_Type(Integer32):
    """Custom type hpnicfCBQoSIfApplyPolicyEnableDynamic based on Integer32"""
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


_HpnicfCBQoSIfApplyPolicyEnableDynamic_Type.__name__ = "Integer32"
_HpnicfCBQoSIfApplyPolicyEnableDynamic_Object = MibTableColumn
hpnicfCBQoSIfApplyPolicyEnableDynamic = _HpnicfCBQoSIfApplyPolicyEnableDynamic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1, 4),
    _HpnicfCBQoSIfApplyPolicyEnableDynamic_Type()
)
hpnicfCBQoSIfApplyPolicyEnableDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyEnableDynamic.setStatus("current")
_HpnicfCBQoSIfApplyPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSIfApplyPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSIfApplyPolicyRowStatus = _HpnicfCBQoSIfApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1, 5),
    _HpnicfCBQoSIfApplyPolicyRowStatus_Type()
)
hpnicfCBQoSIfApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyRowStatus.setStatus("current")


class _HpnicfCBQoSIfApplyPolicyStatus_Type(Integer32):
    """Custom type hpnicfCBQoSIfApplyPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partialItemFailed", 3),
          ("proccessing", 1),
          ("success", 2))
    )


_HpnicfCBQoSIfApplyPolicyStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSIfApplyPolicyStatus_Object = MibTableColumn
hpnicfCBQoSIfApplyPolicyStatus = _HpnicfCBQoSIfApplyPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 1, 1, 6),
    _HpnicfCBQoSIfApplyPolicyStatus_Type()
)
hpnicfCBQoSIfApplyPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfApplyPolicyStatus.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyTable_Object = MibTable
hpnicfCBQoSAtmPvcApplyPolicyTable = _HpnicfCBQoSAtmPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyTable.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcApplyPolicyEntry = _HpnicfCBQoSAtmPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1)
)
hpnicfCBQoSAtmPvcApplyPolicyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyEntry.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Type = Integer32
_HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Object = MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyIfIndex = _HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1, 1),
    _HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Type()
)
hpnicfCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyIfIndex.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyVPI_Type = Integer32
_HpnicfCBQoSAtmPvcApplyPolicyVPI_Object = MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyVPI = _HpnicfCBQoSAtmPvcApplyPolicyVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1, 2),
    _HpnicfCBQoSAtmPvcApplyPolicyVPI_Type()
)
hpnicfCBQoSAtmPvcApplyPolicyVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyVPI.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyVCI_Type = Integer32
_HpnicfCBQoSAtmPvcApplyPolicyVCI_Object = MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyVCI = _HpnicfCBQoSAtmPvcApplyPolicyVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1, 3),
    _HpnicfCBQoSAtmPvcApplyPolicyVCI_Type()
)
hpnicfCBQoSAtmPvcApplyPolicyVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyVCI.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyDirection_Type = DirectionType
_HpnicfCBQoSAtmPvcApplyPolicyDirection_Object = MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyDirection = _HpnicfCBQoSAtmPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1, 4),
    _HpnicfCBQoSAtmPvcApplyPolicyDirection_Type()
)
hpnicfCBQoSAtmPvcApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyDirection.setStatus("current")


class _HpnicfCBQoSAtmPvcApplyPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSAtmPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSAtmPvcApplyPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSAtmPvcApplyPolicyName_Object = MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyName = _HpnicfCBQoSAtmPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1, 5),
    _HpnicfCBQoSAtmPvcApplyPolicyName_Type()
)
hpnicfCBQoSAtmPvcApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyName.setStatus("current")
_HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyRowStatus = _HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 2, 1, 6),
    _HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Type()
)
hpnicfCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcApplyPolicyRowStatus.setStatus("current")
_HpnicfCBQoSVlanApplyPolicyTable_Object = MibTable
hpnicfCBQoSVlanApplyPolicyTable = _HpnicfCBQoSVlanApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyTable.setStatus("current")
_HpnicfCBQoSVlanApplyPolicyEntry_Object = MibTableRow
hpnicfCBQoSVlanApplyPolicyEntry = _HpnicfCBQoSVlanApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1)
)
hpnicfCBQoSVlanApplyPolicyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyVlanid"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyEntry.setStatus("current")
_HpnicfCBQoSVlanApplyPolicyVlanid_Type = Integer32
_HpnicfCBQoSVlanApplyPolicyVlanid_Object = MibTableColumn
hpnicfCBQoSVlanApplyPolicyVlanid = _HpnicfCBQoSVlanApplyPolicyVlanid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1, 1),
    _HpnicfCBQoSVlanApplyPolicyVlanid_Type()
)
hpnicfCBQoSVlanApplyPolicyVlanid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyVlanid.setStatus("current")
_HpnicfCBQoSVlanApplyPolicyDirection_Type = DirectionType
_HpnicfCBQoSVlanApplyPolicyDirection_Object = MibTableColumn
hpnicfCBQoSVlanApplyPolicyDirection = _HpnicfCBQoSVlanApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1, 2),
    _HpnicfCBQoSVlanApplyPolicyDirection_Type()
)
hpnicfCBQoSVlanApplyPolicyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyDirection.setStatus("current")


class _HpnicfCBQoSVlanApplyPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSVlanApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfCBQoSVlanApplyPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSVlanApplyPolicyName_Object = MibTableColumn
hpnicfCBQoSVlanApplyPolicyName = _HpnicfCBQoSVlanApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1, 3),
    _HpnicfCBQoSVlanApplyPolicyName_Type()
)
hpnicfCBQoSVlanApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyName.setStatus("current")


class _HpnicfCBQoSVlanApplyPriority_Type(Integer32):
    """Custom type hpnicfCBQoSVlanApplyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HpnicfCBQoSVlanApplyPriority_Type.__name__ = "Integer32"
_HpnicfCBQoSVlanApplyPriority_Object = MibTableColumn
hpnicfCBQoSVlanApplyPriority = _HpnicfCBQoSVlanApplyPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1, 4),
    _HpnicfCBQoSVlanApplyPriority_Type()
)
hpnicfCBQoSVlanApplyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPriority.setStatus("current")
_HpnicfCBQoSVlanApplyPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSVlanApplyPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSVlanApplyPolicyRowStatus = _HpnicfCBQoSVlanApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1, 5),
    _HpnicfCBQoSVlanApplyPolicyRowStatus_Type()
)
hpnicfCBQoSVlanApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyRowStatus.setStatus("current")


class _HpnicfCBQoSVlanApplyPolicyStatus_Type(Integer32):
    """Custom type hpnicfCBQoSVlanApplyPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partialItemFailed", 3),
          ("proccessing", 1),
          ("success", 2))
    )


_HpnicfCBQoSVlanApplyPolicyStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSVlanApplyPolicyStatus_Object = MibTableColumn
hpnicfCBQoSVlanApplyPolicyStatus = _HpnicfCBQoSVlanApplyPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 3, 1, 6),
    _HpnicfCBQoSVlanApplyPolicyStatus_Type()
)
hpnicfCBQoSVlanApplyPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyPolicyStatus.setStatus("current")
_HpnicfCBQoSFrClassApplyPolicyTable_Object = MibTable
hpnicfCBQoSFrClassApplyPolicyTable = _HpnicfCBQoSFrClassApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrClassApplyPolicyTable.setStatus("current")
_HpnicfCBQoSFrClassApplyPolicyEntry_Object = MibTableRow
hpnicfCBQoSFrClassApplyPolicyEntry = _HpnicfCBQoSFrClassApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 4, 1)
)
hpnicfCBQoSFrClassApplyPolicyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrClassApplyPolicyFrClassName"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrClassApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrClassApplyPolicyEntry.setStatus("current")


class _HpnicfCBQoSFrClassApplyPolicyFrClassName_Type(OctetString):
    """Custom type hpnicfCBQoSFrClassApplyPolicyFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSFrClassApplyPolicyFrClassName_Type.__name__ = "OctetString"
_HpnicfCBQoSFrClassApplyPolicyFrClassName_Object = MibTableColumn
hpnicfCBQoSFrClassApplyPolicyFrClassName = _HpnicfCBQoSFrClassApplyPolicyFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 4, 1, 1),
    _HpnicfCBQoSFrClassApplyPolicyFrClassName_Type()
)
hpnicfCBQoSFrClassApplyPolicyFrClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrClassApplyPolicyFrClassName.setStatus("current")
_HpnicfCBQoSFrClassApplyPolicyDirection_Type = DirectionType
_HpnicfCBQoSFrClassApplyPolicyDirection_Object = MibTableColumn
hpnicfCBQoSFrClassApplyPolicyDirection = _HpnicfCBQoSFrClassApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 4, 1, 2),
    _HpnicfCBQoSFrClassApplyPolicyDirection_Type()
)
hpnicfCBQoSFrClassApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrClassApplyPolicyDirection.setStatus("current")


class _HpnicfCBQoSFrClassApplyPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSFrClassApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSFrClassApplyPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSFrClassApplyPolicyName_Object = MibTableColumn
hpnicfCBQoSFrClassApplyPolicyName = _HpnicfCBQoSFrClassApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 4, 1, 3),
    _HpnicfCBQoSFrClassApplyPolicyName_Type()
)
hpnicfCBQoSFrClassApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrClassApplyPolicyName.setStatus("current")
_HpnicfCBQoSFrClassApplyPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSFrClassApplyPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSFrClassApplyPolicyRowStatus = _HpnicfCBQoSFrClassApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 4, 1, 4),
    _HpnicfCBQoSFrClassApplyPolicyRowStatus_Type()
)
hpnicfCBQoSFrClassApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrClassApplyPolicyRowStatus.setStatus("current")
_HpnicfCBQoSFrPvcApplyPolicyTable_Object = MibTable
hpnicfCBQoSFrPvcApplyPolicyTable = _HpnicfCBQoSFrPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyTable.setStatus("current")
_HpnicfCBQoSFrPvcApplyPolicyEntry_Object = MibTableRow
hpnicfCBQoSFrPvcApplyPolicyEntry = _HpnicfCBQoSFrPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5, 1)
)
hpnicfCBQoSFrPvcApplyPolicyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyEntry.setStatus("current")
_HpnicfCBQoSFrPvcApplyPolicyIfIndex_Type = Integer32
_HpnicfCBQoSFrPvcApplyPolicyIfIndex_Object = MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyIfIndex = _HpnicfCBQoSFrPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5, 1, 1),
    _HpnicfCBQoSFrPvcApplyPolicyIfIndex_Type()
)
hpnicfCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyIfIndex.setStatus("current")


class _HpnicfCBQoSFrPvcApplyPolicyDlciNum_Type(Integer32):
    """Custom type hpnicfCBQoSFrPvcApplyPolicyDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_HpnicfCBQoSFrPvcApplyPolicyDlciNum_Type.__name__ = "Integer32"
_HpnicfCBQoSFrPvcApplyPolicyDlciNum_Object = MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyDlciNum = _HpnicfCBQoSFrPvcApplyPolicyDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5, 1, 2),
    _HpnicfCBQoSFrPvcApplyPolicyDlciNum_Type()
)
hpnicfCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyDlciNum.setStatus("current")
_HpnicfCBQoSFrPvcApplyPolicyDirection_Type = DirectionType
_HpnicfCBQoSFrPvcApplyPolicyDirection_Object = MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyDirection = _HpnicfCBQoSFrPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5, 1, 3),
    _HpnicfCBQoSFrPvcApplyPolicyDirection_Type()
)
hpnicfCBQoSFrPvcApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyDirection.setStatus("current")


class _HpnicfCBQoSFrPvcApplyPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSFrPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSFrPvcApplyPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSFrPvcApplyPolicyName_Object = MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyName = _HpnicfCBQoSFrPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5, 1, 4),
    _HpnicfCBQoSFrPvcApplyPolicyName_Type()
)
hpnicfCBQoSFrPvcApplyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyName.setStatus("current")
_HpnicfCBQoSFrPvcApplyPolicyRowStatus_Type = RowStatus
_HpnicfCBQoSFrPvcApplyPolicyRowStatus_Object = MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyRowStatus = _HpnicfCBQoSFrPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 5, 1, 5),
    _HpnicfCBQoSFrPvcApplyPolicyRowStatus_Type()
)
hpnicfCBQoSFrPvcApplyPolicyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcApplyPolicyRowStatus.setStatus("current")
_HpnicfCBQoSGlobalApplyTable_Object = MibTable
hpnicfCBQoSGlobalApplyTable = _HpnicfCBQoSGlobalApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSGlobalApplyTable.setStatus("current")
_HpnicfCBQoSGlobalApplyEntry_Object = MibTableRow
hpnicfCBQoSGlobalApplyEntry = _HpnicfCBQoSGlobalApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 6, 1)
)
hpnicfCBQoSGlobalApplyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSGlobalApplyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSGlobalApplyEntry.setStatus("current")
_HpnicfCBQoSGlobalApplyDirection_Type = DirectionType
_HpnicfCBQoSGlobalApplyDirection_Object = MibTableColumn
hpnicfCBQoSGlobalApplyDirection = _HpnicfCBQoSGlobalApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 6, 1, 1),
    _HpnicfCBQoSGlobalApplyDirection_Type()
)
hpnicfCBQoSGlobalApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSGlobalApplyDirection.setStatus("current")


class _HpnicfCBQoSGlobalApplyName_Type(OctetString):
    """Custom type hpnicfCBQoSGlobalApplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSGlobalApplyName_Type.__name__ = "OctetString"
_HpnicfCBQoSGlobalApplyName_Object = MibTableColumn
hpnicfCBQoSGlobalApplyName = _HpnicfCBQoSGlobalApplyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 6, 1, 2),
    _HpnicfCBQoSGlobalApplyName_Type()
)
hpnicfCBQoSGlobalApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGlobalApplyName.setStatus("current")
_HpnicfCBQoSGlobalApplyRowStatus_Type = RowStatus
_HpnicfCBQoSGlobalApplyRowStatus_Object = MibTableColumn
hpnicfCBQoSGlobalApplyRowStatus = _HpnicfCBQoSGlobalApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 6, 1, 3),
    _HpnicfCBQoSGlobalApplyRowStatus_Type()
)
hpnicfCBQoSGlobalApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSGlobalApplyRowStatus.setStatus("current")


class _HpnicfCBQoSGlobalApplyStatus_Type(Integer32):
    """Custom type hpnicfCBQoSGlobalApplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partialItemFailed", 3),
          ("proccessing", 1),
          ("success", 2))
    )


_HpnicfCBQoSGlobalApplyStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSGlobalApplyStatus_Object = MibTableColumn
hpnicfCBQoSGlobalApplyStatus = _HpnicfCBQoSGlobalApplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 6, 1, 4),
    _HpnicfCBQoSGlobalApplyStatus_Type()
)
hpnicfCBQoSGlobalApplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGlobalApplyStatus.setStatus("current")
_HpnicfCBQoSCpApplyPolicyTable_Object = MibTable
hpnicfCBQoSCpApplyPolicyTable = _HpnicfCBQoSCpApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicyTable.setStatus("current")
_HpnicfCBQoSCpApplyPolicyEntry_Object = MibTableRow
hpnicfCBQoSCpApplyPolicyEntry = _HpnicfCBQoSCpApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1)
)
hpnicfCBQoSCpApplyPolicyEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSCpApplyPolicyChassis"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSCpApplyPolicySlot"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSCpApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicyEntry.setStatus("current")
_HpnicfCBQoSCpApplyPolicyChassis_Type = Unsigned32
_HpnicfCBQoSCpApplyPolicyChassis_Object = MibTableColumn
hpnicfCBQoSCpApplyPolicyChassis = _HpnicfCBQoSCpApplyPolicyChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1, 1),
    _HpnicfCBQoSCpApplyPolicyChassis_Type()
)
hpnicfCBQoSCpApplyPolicyChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicyChassis.setStatus("current")
_HpnicfCBQoSCpApplyPolicySlot_Type = Unsigned32
_HpnicfCBQoSCpApplyPolicySlot_Object = MibTableColumn
hpnicfCBQoSCpApplyPolicySlot = _HpnicfCBQoSCpApplyPolicySlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1, 2),
    _HpnicfCBQoSCpApplyPolicySlot_Type()
)
hpnicfCBQoSCpApplyPolicySlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicySlot.setStatus("current")
_HpnicfCBQoSCpApplyPolicyDirection_Type = DirectionType
_HpnicfCBQoSCpApplyPolicyDirection_Object = MibTableColumn
hpnicfCBQoSCpApplyPolicyDirection = _HpnicfCBQoSCpApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1, 3),
    _HpnicfCBQoSCpApplyPolicyDirection_Type()
)
hpnicfCBQoSCpApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicyDirection.setStatus("current")


class _HpnicfCBQoSCpApplyPolicyName_Type(OctetString):
    """Custom type hpnicfCBQoSCpApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfCBQoSCpApplyPolicyName_Type.__name__ = "OctetString"
_HpnicfCBQoSCpApplyPolicyName_Object = MibTableColumn
hpnicfCBQoSCpApplyPolicyName = _HpnicfCBQoSCpApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1, 4),
    _HpnicfCBQoSCpApplyPolicyName_Type()
)
hpnicfCBQoSCpApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicyName.setStatus("current")


class _HpnicfCBQoSCpApplyPolicyStatus_Type(Integer32):
    """Custom type hpnicfCBQoSCpApplyPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partialItemFailed", 3),
          ("proccessing", 1),
          ("success", 2))
    )


_HpnicfCBQoSCpApplyPolicyStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSCpApplyPolicyStatus_Object = MibTableColumn
hpnicfCBQoSCpApplyPolicyStatus = _HpnicfCBQoSCpApplyPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1, 5),
    _HpnicfCBQoSCpApplyPolicyStatus_Type()
)
hpnicfCBQoSCpApplyPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyPolicyStatus.setStatus("current")
_HpnicfCBQoSCpApplyRowStatus_Type = RowStatus
_HpnicfCBQoSCpApplyRowStatus_Object = MibTableColumn
hpnicfCBQoSCpApplyRowStatus = _HpnicfCBQoSCpApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 4, 7, 1, 6),
    _HpnicfCBQoSCpApplyRowStatus_Type()
)
hpnicfCBQoSCpApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyRowStatus.setStatus("current")
_HpnicfCBQoSApplyPolicyStaticsObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSApplyPolicyStaticsObjects = _HpnicfCBQoSApplyPolicyStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5)
)
_HpnicfCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSIfStaticsObjects = _HpnicfCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1)
)
_HpnicfCBQoSIfCbqRunInfoTable_Object = MibTable
hpnicfCBQoSIfCbqRunInfoTable = _HpnicfCBQoSIfCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqRunInfoTable.setStatus("current")
_HpnicfCBQoSIfCbqRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfCbqRunInfoEntry = _HpnicfCBQoSIfCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1)
)
hpnicfCBQoSIfCbqRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfCbqQueueSize_Type = Integer32
_HpnicfCBQoSIfCbqQueueSize_Object = MibTableColumn
hpnicfCBQoSIfCbqQueueSize = _HpnicfCBQoSIfCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 1),
    _HpnicfCBQoSIfCbqQueueSize_Type()
)
hpnicfCBQoSIfCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqQueueSize.setStatus("current")
_HpnicfCBQoSIfCbqDiscard_Type = Counter64
_HpnicfCBQoSIfCbqDiscard_Object = MibTableColumn
hpnicfCBQoSIfCbqDiscard = _HpnicfCBQoSIfCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 2),
    _HpnicfCBQoSIfCbqDiscard_Type()
)
hpnicfCBQoSIfCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqDiscard.setStatus("current")
_HpnicfCBQoSIfCbqEfQueueSize_Type = Integer32
_HpnicfCBQoSIfCbqEfQueueSize_Object = MibTableColumn
hpnicfCBQoSIfCbqEfQueueSize = _HpnicfCBQoSIfCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 3),
    _HpnicfCBQoSIfCbqEfQueueSize_Type()
)
hpnicfCBQoSIfCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqEfQueueSize.setStatus("current")
_HpnicfCBQoSIfCbqAfQueueSize_Type = Integer32
_HpnicfCBQoSIfCbqAfQueueSize_Object = MibTableColumn
hpnicfCBQoSIfCbqAfQueueSize = _HpnicfCBQoSIfCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 4),
    _HpnicfCBQoSIfCbqAfQueueSize_Type()
)
hpnicfCBQoSIfCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqAfQueueSize.setStatus("current")
_HpnicfCBQoSIfCbqBeQueueSize_Type = Integer32
_HpnicfCBQoSIfCbqBeQueueSize_Object = MibTableColumn
hpnicfCBQoSIfCbqBeQueueSize = _HpnicfCBQoSIfCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 5),
    _HpnicfCBQoSIfCbqBeQueueSize_Type()
)
hpnicfCBQoSIfCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqBeQueueSize.setStatus("current")
_HpnicfCBQoSIfCbqBeActiveQueueNum_Type = Integer32
_HpnicfCBQoSIfCbqBeActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSIfCbqBeActiveQueueNum = _HpnicfCBQoSIfCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 6),
    _HpnicfCBQoSIfCbqBeActiveQueueNum_Type()
)
hpnicfCBQoSIfCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqBeActiveQueueNum.setStatus("current")
_HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Type = Integer32
_HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSIfCbqBeMaxActiveQueueNum = _HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 7),
    _HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Type()
)
hpnicfCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqBeMaxActiveQueueNum.setStatus("current")
_HpnicfCBQoSIfCbqBeTotalQueueNum_Type = Integer32
_HpnicfCBQoSIfCbqBeTotalQueueNum_Object = MibTableColumn
hpnicfCBQoSIfCbqBeTotalQueueNum = _HpnicfCBQoSIfCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 8),
    _HpnicfCBQoSIfCbqBeTotalQueueNum_Type()
)
hpnicfCBQoSIfCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqBeTotalQueueNum.setStatus("current")
_HpnicfCBQoSIfCbqAfAllocatedQueueNum_Type = Integer32
_HpnicfCBQoSIfCbqAfAllocatedQueueNum_Object = MibTableColumn
hpnicfCBQoSIfCbqAfAllocatedQueueNum = _HpnicfCBQoSIfCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 1, 1, 9),
    _HpnicfCBQoSIfCbqAfAllocatedQueueNum_Type()
)
hpnicfCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCbqAfAllocatedQueueNum.setStatus("current")
_HpnicfCBQoSIfClassMatchRunInfoTable_Object = MibTable
hpnicfCBQoSIfClassMatchRunInfoTable = _HpnicfCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfClassMatchRunInfoTable.setStatus("current")
_HpnicfCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfClassMatchRunInfoEntry = _HpnicfCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 2, 1)
)
hpnicfCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfClassMatchedPackets_Type = Counter64
_HpnicfCBQoSIfClassMatchedPackets_Object = MibTableColumn
hpnicfCBQoSIfClassMatchedPackets = _HpnicfCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 2, 1, 1),
    _HpnicfCBQoSIfClassMatchedPackets_Type()
)
hpnicfCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfClassMatchedPackets.setStatus("current")
_HpnicfCBQoSIfClassMatchedBytes_Type = Counter64
_HpnicfCBQoSIfClassMatchedBytes_Object = MibTableColumn
hpnicfCBQoSIfClassMatchedBytes = _HpnicfCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 2, 1, 2),
    _HpnicfCBQoSIfClassMatchedBytes_Type()
)
hpnicfCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfClassMatchedBytes.setStatus("current")
_HpnicfCBQoSIfClassAverageRate_Type = Counter64
_HpnicfCBQoSIfClassAverageRate_Object = MibTableColumn
hpnicfCBQoSIfClassAverageRate = _HpnicfCBQoSIfClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 2, 1, 3),
    _HpnicfCBQoSIfClassAverageRate_Type()
)
hpnicfCBQoSIfClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfClassAverageRate.setStatus("current")
_HpnicfCBQoSIfCarRunInfoTable_Object = MibTable
hpnicfCBQoSIfCarRunInfoTable = _HpnicfCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarRunInfoTable.setStatus("current")
_HpnicfCBQoSIfCarRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfCarRunInfoEntry = _HpnicfCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1)
)
hpnicfCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfCarGreenPackets_Type = Counter64
_HpnicfCBQoSIfCarGreenPackets_Object = MibTableColumn
hpnicfCBQoSIfCarGreenPackets = _HpnicfCBQoSIfCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1, 1),
    _HpnicfCBQoSIfCarGreenPackets_Type()
)
hpnicfCBQoSIfCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarGreenPackets.setStatus("current")
_HpnicfCBQoSIfCarGreenBytes_Type = Counter64
_HpnicfCBQoSIfCarGreenBytes_Object = MibTableColumn
hpnicfCBQoSIfCarGreenBytes = _HpnicfCBQoSIfCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1, 2),
    _HpnicfCBQoSIfCarGreenBytes_Type()
)
hpnicfCBQoSIfCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarGreenBytes.setStatus("current")
_HpnicfCBQoSIfCarRedPackets_Type = Counter64
_HpnicfCBQoSIfCarRedPackets_Object = MibTableColumn
hpnicfCBQoSIfCarRedPackets = _HpnicfCBQoSIfCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1, 3),
    _HpnicfCBQoSIfCarRedPackets_Type()
)
hpnicfCBQoSIfCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarRedPackets.setStatus("current")
_HpnicfCBQoSIfCarRedBytes_Type = Counter64
_HpnicfCBQoSIfCarRedBytes_Object = MibTableColumn
hpnicfCBQoSIfCarRedBytes = _HpnicfCBQoSIfCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1, 4),
    _HpnicfCBQoSIfCarRedBytes_Type()
)
hpnicfCBQoSIfCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarRedBytes.setStatus("current")
_HpnicfCBQoSIfCarYellowPackets_Type = Counter64
_HpnicfCBQoSIfCarYellowPackets_Object = MibTableColumn
hpnicfCBQoSIfCarYellowPackets = _HpnicfCBQoSIfCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1, 5),
    _HpnicfCBQoSIfCarYellowPackets_Type()
)
hpnicfCBQoSIfCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarYellowPackets.setStatus("current")
_HpnicfCBQoSIfCarYellowBytes_Type = Counter64
_HpnicfCBQoSIfCarYellowBytes_Object = MibTableColumn
hpnicfCBQoSIfCarYellowBytes = _HpnicfCBQoSIfCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 3, 1, 6),
    _HpnicfCBQoSIfCarYellowBytes_Type()
)
hpnicfCBQoSIfCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfCarYellowBytes.setStatus("current")
_HpnicfCBQoSIfGtsRunInfoTable_Object = MibTable
hpnicfCBQoSIfGtsRunInfoTable = _HpnicfCBQoSIfGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsRunInfoTable.setStatus("current")
_HpnicfCBQoSIfGtsRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfGtsRunInfoEntry = _HpnicfCBQoSIfGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1)
)
hpnicfCBQoSIfGtsRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfGtsPassedPackets_Type = Counter64
_HpnicfCBQoSIfGtsPassedPackets_Object = MibTableColumn
hpnicfCBQoSIfGtsPassedPackets = _HpnicfCBQoSIfGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 1),
    _HpnicfCBQoSIfGtsPassedPackets_Type()
)
hpnicfCBQoSIfGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsPassedPackets.setStatus("current")
_HpnicfCBQoSIfGtsPassedBytes_Type = Counter64
_HpnicfCBQoSIfGtsPassedBytes_Object = MibTableColumn
hpnicfCBQoSIfGtsPassedBytes = _HpnicfCBQoSIfGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 2),
    _HpnicfCBQoSIfGtsPassedBytes_Type()
)
hpnicfCBQoSIfGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsPassedBytes.setStatus("current")
_HpnicfCBQoSIfGtsDiscardedPackets_Type = Counter64
_HpnicfCBQoSIfGtsDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSIfGtsDiscardedPackets = _HpnicfCBQoSIfGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 3),
    _HpnicfCBQoSIfGtsDiscardedPackets_Type()
)
hpnicfCBQoSIfGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsDiscardedPackets.setStatus("current")
_HpnicfCBQoSIfGtsDiscardedBytes_Type = Counter64
_HpnicfCBQoSIfGtsDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSIfGtsDiscardedBytes = _HpnicfCBQoSIfGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 4),
    _HpnicfCBQoSIfGtsDiscardedBytes_Type()
)
hpnicfCBQoSIfGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsDiscardedBytes.setStatus("current")
_HpnicfCBQoSIfGtsDelayedPackets_Type = Counter64
_HpnicfCBQoSIfGtsDelayedPackets_Object = MibTableColumn
hpnicfCBQoSIfGtsDelayedPackets = _HpnicfCBQoSIfGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 5),
    _HpnicfCBQoSIfGtsDelayedPackets_Type()
)
hpnicfCBQoSIfGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsDelayedPackets.setStatus("current")
_HpnicfCBQoSIfGtsDelayedBytes_Type = Counter64
_HpnicfCBQoSIfGtsDelayedBytes_Object = MibTableColumn
hpnicfCBQoSIfGtsDelayedBytes = _HpnicfCBQoSIfGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 6),
    _HpnicfCBQoSIfGtsDelayedBytes_Type()
)
hpnicfCBQoSIfGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsDelayedBytes.setStatus("current")
_HpnicfCBQoSIfGtsQueueSize_Type = Integer32
_HpnicfCBQoSIfGtsQueueSize_Object = MibTableColumn
hpnicfCBQoSIfGtsQueueSize = _HpnicfCBQoSIfGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 4, 1, 7),
    _HpnicfCBQoSIfGtsQueueSize_Type()
)
hpnicfCBQoSIfGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfGtsQueueSize.setStatus("current")
_HpnicfCBQoSIfRemarkRunInfoTable_Object = MibTable
hpnicfCBQoSIfRemarkRunInfoTable = _HpnicfCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfRemarkRunInfoTable.setStatus("current")
_HpnicfCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfRemarkRunInfoEntry = _HpnicfCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 5, 1)
)
hpnicfCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfRemarkRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfRemarkedPackets_Type = Counter64
_HpnicfCBQoSIfRemarkedPackets_Object = MibTableColumn
hpnicfCBQoSIfRemarkedPackets = _HpnicfCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 5, 1, 1),
    _HpnicfCBQoSIfRemarkedPackets_Type()
)
hpnicfCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfRemarkedPackets.setStatus("current")
_HpnicfCBQoSIfQueueRunInfoTable_Object = MibTable
hpnicfCBQoSIfQueueRunInfoTable = _HpnicfCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueRunInfoTable.setStatus("current")
_HpnicfCBQoSIfQueueRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfQueueRunInfoEntry = _HpnicfCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1)
)
hpnicfCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfQueueMatchedPackets_Type = Counter64
_HpnicfCBQoSIfQueueMatchedPackets_Object = MibTableColumn
hpnicfCBQoSIfQueueMatchedPackets = _HpnicfCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1, 1),
    _HpnicfCBQoSIfQueueMatchedPackets_Type()
)
hpnicfCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueMatchedPackets.setStatus("current")
_HpnicfCBQoSIfQueueMatchedBytes_Type = Counter64
_HpnicfCBQoSIfQueueMatchedBytes_Object = MibTableColumn
hpnicfCBQoSIfQueueMatchedBytes = _HpnicfCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1, 2),
    _HpnicfCBQoSIfQueueMatchedBytes_Type()
)
hpnicfCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueMatchedBytes.setStatus("current")
_HpnicfCBQoSIfQueueEnqueuedPackets_Type = Counter64
_HpnicfCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
hpnicfCBQoSIfQueueEnqueuedPackets = _HpnicfCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1, 3),
    _HpnicfCBQoSIfQueueEnqueuedPackets_Type()
)
hpnicfCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueEnqueuedPackets.setStatus("current")
_HpnicfCBQoSIfQueueEnqueuedBytes_Type = Counter64
_HpnicfCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
hpnicfCBQoSIfQueueEnqueuedBytes = _HpnicfCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1, 4),
    _HpnicfCBQoSIfQueueEnqueuedBytes_Type()
)
hpnicfCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueEnqueuedBytes.setStatus("current")
_HpnicfCBQoSIfQueueDiscardedPackets_Type = Counter64
_HpnicfCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSIfQueueDiscardedPackets = _HpnicfCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1, 5),
    _HpnicfCBQoSIfQueueDiscardedPackets_Type()
)
hpnicfCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueDiscardedPackets.setStatus("current")
_HpnicfCBQoSIfQueueDiscardedBytes_Type = Counter64
_HpnicfCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSIfQueueDiscardedBytes = _HpnicfCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 6, 1, 6),
    _HpnicfCBQoSIfQueueDiscardedBytes_Type()
)
hpnicfCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfQueueDiscardedBytes.setStatus("current")
_HpnicfCBQoSIfWredRunInfoTable_Object = MibTable
hpnicfCBQoSIfWredRunInfoTable = _HpnicfCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfWredRunInfoTable.setStatus("current")
_HpnicfCBQoSIfWredRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfWredRunInfoEntry = _HpnicfCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 7, 1)
)
hpnicfCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfWredRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_HpnicfCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSIfWredRandomDiscardedPackets = _HpnicfCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 7, 1, 1),
    _HpnicfCBQoSIfWredRandomDiscardedPackets_Type()
)
hpnicfCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_HpnicfCBQoSIfWredTailDiscardedPackets_Type = Counter64
_HpnicfCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSIfWredTailDiscardedPackets = _HpnicfCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 7, 1, 2),
    _HpnicfCBQoSIfWredTailDiscardedPackets_Type()
)
hpnicfCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfWredTailDiscardedPackets.setStatus("current")
_HpnicfCBQoSIfAccountingRunInfoTable_Object = MibTable
hpnicfCBQoSIfAccountingRunInfoTable = _HpnicfCBQoSIfAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfAccountingRunInfoTable.setStatus("current")
_HpnicfCBQoSIfAccountingRunInfoEntry_Object = MibTableRow
hpnicfCBQoSIfAccountingRunInfoEntry = _HpnicfCBQoSIfAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 8, 1)
)
hpnicfCBQoSIfAccountingRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfAccountingRunInfoEntry.setStatus("current")
_HpnicfCBQoSIfAccountingPackets_Type = Counter64
_HpnicfCBQoSIfAccountingPackets_Object = MibTableColumn
hpnicfCBQoSIfAccountingPackets = _HpnicfCBQoSIfAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 8, 1, 1),
    _HpnicfCBQoSIfAccountingPackets_Type()
)
hpnicfCBQoSIfAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfAccountingPackets.setStatus("current")
_HpnicfCBQoSIfAccountingBytes_Type = Counter64
_HpnicfCBQoSIfAccountingBytes_Object = MibTableColumn
hpnicfCBQoSIfAccountingBytes = _HpnicfCBQoSIfAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 1, 8, 1, 2),
    _HpnicfCBQoSIfAccountingBytes_Type()
)
hpnicfCBQoSIfAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIfAccountingBytes.setStatus("current")
_HpnicfCBQoSAtmPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSAtmPvcStaticsObjects = _HpnicfCBQoSAtmPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2)
)
_HpnicfCBQoSAtmPvcCbqRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcCbqRunInfoTable = _HpnicfCBQoSAtmPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcCbqRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcCbqRunInfoEntry = _HpnicfCBQoSAtmPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1)
)
hpnicfCBQoSAtmPvcCbqRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcCbqQueueSize_Type = Integer32
_HpnicfCBQoSAtmPvcCbqQueueSize_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqQueueSize = _HpnicfCBQoSAtmPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 1),
    _HpnicfCBQoSAtmPvcCbqQueueSize_Type()
)
hpnicfCBQoSAtmPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqQueueSize.setStatus("current")
_HpnicfCBQoSAtmPvcCbqDiscard_Type = Counter64
_HpnicfCBQoSAtmPvcCbqDiscard_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqDiscard = _HpnicfCBQoSAtmPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 2),
    _HpnicfCBQoSAtmPvcCbqDiscard_Type()
)
hpnicfCBQoSAtmPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqDiscard.setStatus("current")
_HpnicfCBQoSAtmPvcCbqEfQueueSize_Type = Integer32
_HpnicfCBQoSAtmPvcCbqEfQueueSize_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqEfQueueSize = _HpnicfCBQoSAtmPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 3),
    _HpnicfCBQoSAtmPvcCbqEfQueueSize_Type()
)
hpnicfCBQoSAtmPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqEfQueueSize.setStatus("current")
_HpnicfCBQoSAtmPvcCbqAfQueueSize_Type = Integer32
_HpnicfCBQoSAtmPvcCbqAfQueueSize_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqAfQueueSize = _HpnicfCBQoSAtmPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 4),
    _HpnicfCBQoSAtmPvcCbqAfQueueSize_Type()
)
hpnicfCBQoSAtmPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqAfQueueSize.setStatus("current")
_HpnicfCBQoSAtmPvcCbqBeQueueSize_Type = Integer32
_HpnicfCBQoSAtmPvcCbqBeQueueSize_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqBeQueueSize = _HpnicfCBQoSAtmPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 5),
    _HpnicfCBQoSAtmPvcCbqBeQueueSize_Type()
)
hpnicfCBQoSAtmPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqBeQueueSize.setStatus("current")
_HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Type = Integer32
_HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqBeActiveQueueNum = _HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 6),
    _HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Type()
)
hpnicfCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqBeActiveQueueNum.setStatus("current")
_HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type = Integer32
_HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum = _HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 7),
    _HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type()
)
hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus("current")
_HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Type = Integer32
_HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqBeTotalQueueNum = _HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 8),
    _HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Type()
)
hpnicfCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqBeTotalQueueNum.setStatus("current")
_HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Type = Integer32
_HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum = _HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 1, 1, 9),
    _HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Type()
)
hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus("current")
_HpnicfCBQoSAtmPvcClassMatchRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcClassMatchRunInfoTable = _HpnicfCBQoSAtmPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcClassMatchRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcClassMatchRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcClassMatchRunInfoEntry = _HpnicfCBQoSAtmPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 2, 1)
)
hpnicfCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcClassMatchRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcClassMatchPackets_Type = Counter64
_HpnicfCBQoSAtmPvcClassMatchPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcClassMatchPackets = _HpnicfCBQoSAtmPvcClassMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 2, 1, 1),
    _HpnicfCBQoSAtmPvcClassMatchPackets_Type()
)
hpnicfCBQoSAtmPvcClassMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcClassMatchPackets.setStatus("current")
_HpnicfCBQoSAtmPvcClassMatchBytes_Type = Counter64
_HpnicfCBQoSAtmPvcClassMatchBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcClassMatchBytes = _HpnicfCBQoSAtmPvcClassMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 2, 1, 2),
    _HpnicfCBQoSAtmPvcClassMatchBytes_Type()
)
hpnicfCBQoSAtmPvcClassMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcClassMatchBytes.setStatus("current")
_HpnicfCBQoSAtmPvcClassAverageRate_Type = Integer32
_HpnicfCBQoSAtmPvcClassAverageRate_Object = MibTableColumn
hpnicfCBQoSAtmPvcClassAverageRate = _HpnicfCBQoSAtmPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 2, 1, 3),
    _HpnicfCBQoSAtmPvcClassAverageRate_Type()
)
hpnicfCBQoSAtmPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcClassAverageRate.setStatus("current")
_HpnicfCBQoSAtmPvcCarRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcCarRunInfoTable = _HpnicfCBQoSAtmPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCarRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcCarRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcCarRunInfoEntry = _HpnicfCBQoSAtmPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 3, 1)
)
hpnicfCBQoSAtmPvcCarRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCarRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcCarConformPackets_Type = Counter64
_HpnicfCBQoSAtmPvcCarConformPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcCarConformPackets = _HpnicfCBQoSAtmPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 3, 1, 1),
    _HpnicfCBQoSAtmPvcCarConformPackets_Type()
)
hpnicfCBQoSAtmPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCarConformPackets.setStatus("current")
_HpnicfCBQoSAtmPvcCarConformBytes_Type = Counter64
_HpnicfCBQoSAtmPvcCarConformBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcCarConformBytes = _HpnicfCBQoSAtmPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 3, 1, 2),
    _HpnicfCBQoSAtmPvcCarConformBytes_Type()
)
hpnicfCBQoSAtmPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCarConformBytes.setStatus("current")
_HpnicfCBQoSAtmPvcCarExceedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcCarExceedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcCarExceedPackets = _HpnicfCBQoSAtmPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 3, 1, 3),
    _HpnicfCBQoSAtmPvcCarExceedPackets_Type()
)
hpnicfCBQoSAtmPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCarExceedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcCarExceedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcCarExceedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcCarExceedBytes = _HpnicfCBQoSAtmPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 3, 1, 4),
    _HpnicfCBQoSAtmPvcCarExceedBytes_Type()
)
hpnicfCBQoSAtmPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcCarExceedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcGtsRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcGtsRunInfoTable = _HpnicfCBQoSAtmPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcGtsRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcGtsRunInfoEntry = _HpnicfCBQoSAtmPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1)
)
hpnicfCBQoSAtmPvcGtsRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcGtsPassedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcGtsPassedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsPassedPackets = _HpnicfCBQoSAtmPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 1),
    _HpnicfCBQoSAtmPvcGtsPassedPackets_Type()
)
hpnicfCBQoSAtmPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsPassedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcGtsPassedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcGtsPassedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsPassedBytes = _HpnicfCBQoSAtmPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 2),
    _HpnicfCBQoSAtmPvcGtsPassedBytes_Type()
)
hpnicfCBQoSAtmPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsPassedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcGtsDiscardedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcGtsDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsDiscardedPackets = _HpnicfCBQoSAtmPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 3),
    _HpnicfCBQoSAtmPvcGtsDiscardedPackets_Type()
)
hpnicfCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsDiscardedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcGtsDiscardedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcGtsDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsDiscardedBytes = _HpnicfCBQoSAtmPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 4),
    _HpnicfCBQoSAtmPvcGtsDiscardedBytes_Type()
)
hpnicfCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsDiscardedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcGtsDelayedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcGtsDelayedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsDelayedPackets = _HpnicfCBQoSAtmPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 5),
    _HpnicfCBQoSAtmPvcGtsDelayedPackets_Type()
)
hpnicfCBQoSAtmPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsDelayedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcGtsDelayedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcGtsDelayedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsDelayedBytes = _HpnicfCBQoSAtmPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 6),
    _HpnicfCBQoSAtmPvcGtsDelayedBytes_Type()
)
hpnicfCBQoSAtmPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsDelayedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcGtsQueueSize_Type = Integer32
_HpnicfCBQoSAtmPvcGtsQueueSize_Object = MibTableColumn
hpnicfCBQoSAtmPvcGtsQueueSize = _HpnicfCBQoSAtmPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 4, 1, 7),
    _HpnicfCBQoSAtmPvcGtsQueueSize_Type()
)
hpnicfCBQoSAtmPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcGtsQueueSize.setStatus("current")
_HpnicfCBQoSAtmPvcRemarkRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcRemarkRunInfoTable = _HpnicfCBQoSAtmPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcRemarkRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcRemarkRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcRemarkRunInfoEntry = _HpnicfCBQoSAtmPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 5, 1)
)
hpnicfCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcRemarkRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcRemarkedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcRemarkedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcRemarkedPackets = _HpnicfCBQoSAtmPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 5, 1, 1),
    _HpnicfCBQoSAtmPvcRemarkedPackets_Type()
)
hpnicfCBQoSAtmPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcRemarkedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcQueueRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcQueueRunInfoTable = _HpnicfCBQoSAtmPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcQueueRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcQueueRunInfoEntry = _HpnicfCBQoSAtmPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1)
)
hpnicfCBQoSAtmPvcQueueRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcQueueMatchedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcQueueMatchedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcQueueMatchedPackets = _HpnicfCBQoSAtmPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1, 1),
    _HpnicfCBQoSAtmPvcQueueMatchedPackets_Type()
)
hpnicfCBQoSAtmPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueMatchedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcQueueMatchedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcQueueMatchedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcQueueMatchedBytes = _HpnicfCBQoSAtmPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1, 2),
    _HpnicfCBQoSAtmPvcQueueMatchedBytes_Type()
)
hpnicfCBQoSAtmPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueMatchedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcQueueEnqueuedPackets = _HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1, 3),
    _HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Type()
)
hpnicfCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueEnqueuedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcQueueEnqueuedBytes = _HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1, 4),
    _HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Type()
)
hpnicfCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueEnqueuedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcQueueDiscardedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcQueueDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcQueueDiscardedPackets = _HpnicfCBQoSAtmPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1, 5),
    _HpnicfCBQoSAtmPvcQueueDiscardedPackets_Type()
)
hpnicfCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueDiscardedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcQueueDiscardedBytes_Type = Counter64
_HpnicfCBQoSAtmPvcQueueDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcQueueDiscardedBytes = _HpnicfCBQoSAtmPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 6, 1, 6),
    _HpnicfCBQoSAtmPvcQueueDiscardedBytes_Type()
)
hpnicfCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcQueueDiscardedBytes.setStatus("current")
_HpnicfCBQoSAtmPvcWredRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcWredRunInfoTable = _HpnicfCBQoSAtmPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcWredRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcWredRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcWredRunInfoEntry = _HpnicfCBQoSAtmPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 7, 1)
)
hpnicfCBQoSAtmPvcWredRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcWredRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcWredRandomDiscardedPackets = _HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 7, 1, 1),
    _HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Type()
)
hpnicfCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcWredRandomDiscardedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Type = Counter64
_HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcWredTailDiscardedPackets = _HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 7, 1, 2),
    _HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Type()
)
hpnicfCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcWredTailDiscardedPackets.setStatus("current")
_HpnicfCBQoSAtmPvcAccountingRunInfoTable_Object = MibTable
hpnicfCBQoSAtmPvcAccountingRunInfoTable = _HpnicfCBQoSAtmPvcAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcAccountingRunInfoTable.setStatus("current")
_HpnicfCBQoSAtmPvcAccountingRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAtmPvcAccountingRunInfoEntry = _HpnicfCBQoSAtmPvcAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 8, 1)
)
hpnicfCBQoSAtmPvcAccountingRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcAccountingRunInfoEntry.setStatus("current")
_HpnicfCBQoSAtmPvcAccountingPackets_Type = Counter64
_HpnicfCBQoSAtmPvcAccountingPackets_Object = MibTableColumn
hpnicfCBQoSAtmPvcAccountingPackets = _HpnicfCBQoSAtmPvcAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 8, 1, 1),
    _HpnicfCBQoSAtmPvcAccountingPackets_Type()
)
hpnicfCBQoSAtmPvcAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcAccountingPackets.setStatus("current")
_HpnicfCBQoSAtmPvcAccountingBytes_Type = Counter64
_HpnicfCBQoSAtmPvcAccountingBytes_Object = MibTableColumn
hpnicfCBQoSAtmPvcAccountingBytes = _HpnicfCBQoSAtmPvcAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 2, 8, 1, 2),
    _HpnicfCBQoSAtmPvcAccountingBytes_Type()
)
hpnicfCBQoSAtmPvcAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAtmPvcAccountingBytes.setStatus("current")
_HpnicfCBQoSFrPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSFrPvcStaticsObjects = _HpnicfCBQoSFrPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3)
)
_HpnicfCBQoSFrPvcCbqRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcCbqRunInfoTable = _HpnicfCBQoSFrPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcCbqRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcCbqRunInfoEntry = _HpnicfCBQoSFrPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1)
)
hpnicfCBQoSFrPvcCbqRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcCbqQueueSize_Type = Integer32
_HpnicfCBQoSFrPvcCbqQueueSize_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqQueueSize = _HpnicfCBQoSFrPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 1),
    _HpnicfCBQoSFrPvcCbqQueueSize_Type()
)
hpnicfCBQoSFrPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqQueueSize.setStatus("current")
_HpnicfCBQoSFrPvcCbqDiscard_Type = Counter64
_HpnicfCBQoSFrPvcCbqDiscard_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqDiscard = _HpnicfCBQoSFrPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 2),
    _HpnicfCBQoSFrPvcCbqDiscard_Type()
)
hpnicfCBQoSFrPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqDiscard.setStatus("current")
_HpnicfCBQoSFrPvcCbqEfQueueSize_Type = Integer32
_HpnicfCBQoSFrPvcCbqEfQueueSize_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqEfQueueSize = _HpnicfCBQoSFrPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 3),
    _HpnicfCBQoSFrPvcCbqEfQueueSize_Type()
)
hpnicfCBQoSFrPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqEfQueueSize.setStatus("current")
_HpnicfCBQoSFrPvcCbqAfQueueSize_Type = Integer32
_HpnicfCBQoSFrPvcCbqAfQueueSize_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqAfQueueSize = _HpnicfCBQoSFrPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 4),
    _HpnicfCBQoSFrPvcCbqAfQueueSize_Type()
)
hpnicfCBQoSFrPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqAfQueueSize.setStatus("current")
_HpnicfCBQoSFrPvcCbqBeQueueSize_Type = Integer32
_HpnicfCBQoSFrPvcCbqBeQueueSize_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqBeQueueSize = _HpnicfCBQoSFrPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 5),
    _HpnicfCBQoSFrPvcCbqBeQueueSize_Type()
)
hpnicfCBQoSFrPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqBeQueueSize.setStatus("current")
_HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Type = Integer32
_HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqBeActiveQueueNum = _HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 6),
    _HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Type()
)
hpnicfCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqBeActiveQueueNum.setStatus("current")
_HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Type = Integer32
_HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum = _HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 7),
    _HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Type()
)
hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus("current")
_HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Type = Integer32
_HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqBeTotalQueueNum = _HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 8),
    _HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Type()
)
hpnicfCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqBeTotalQueueNum.setStatus("current")
_HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Type = Integer32
_HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum = _HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 1, 1, 9),
    _HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Type()
)
hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus("current")
_HpnicfCBQoSFrPvcClassMatchRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcClassMatchRunInfoTable = _HpnicfCBQoSFrPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcClassMatchRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcClassMatchRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcClassMatchRunInfoEntry = _HpnicfCBQoSFrPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 2, 1)
)
hpnicfCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcClassMatchRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcClassMatchedPackets_Type = Counter64
_HpnicfCBQoSFrPvcClassMatchedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcClassMatchedPackets = _HpnicfCBQoSFrPvcClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 2, 1, 1),
    _HpnicfCBQoSFrPvcClassMatchedPackets_Type()
)
hpnicfCBQoSFrPvcClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcClassMatchedPackets.setStatus("current")
_HpnicfCBQoSFrPvcClassMatchedBytes_Type = Counter64
_HpnicfCBQoSFrPvcClassMatchedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcClassMatchedBytes = _HpnicfCBQoSFrPvcClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 2, 1, 2),
    _HpnicfCBQoSFrPvcClassMatchedBytes_Type()
)
hpnicfCBQoSFrPvcClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcClassMatchedBytes.setStatus("current")
_HpnicfCBQoSFrPvcClassAverageRate_Type = Counter64
_HpnicfCBQoSFrPvcClassAverageRate_Object = MibTableColumn
hpnicfCBQoSFrPvcClassAverageRate = _HpnicfCBQoSFrPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 2, 1, 3),
    _HpnicfCBQoSFrPvcClassAverageRate_Type()
)
hpnicfCBQoSFrPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcClassAverageRate.setStatus("current")
_HpnicfCBQoSFrPvcCarRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcCarRunInfoTable = _HpnicfCBQoSFrPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCarRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcCarRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcCarRunInfoEntry = _HpnicfCBQoSFrPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 3, 1)
)
hpnicfCBQoSFrPvcCarRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCarRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcCarConformPackets_Type = Counter64
_HpnicfCBQoSFrPvcCarConformPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcCarConformPackets = _HpnicfCBQoSFrPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 3, 1, 1),
    _HpnicfCBQoSFrPvcCarConformPackets_Type()
)
hpnicfCBQoSFrPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCarConformPackets.setStatus("current")
_HpnicfCBQoSFrPvcCarConformBytes_Type = Counter64
_HpnicfCBQoSFrPvcCarConformBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcCarConformBytes = _HpnicfCBQoSFrPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 3, 1, 2),
    _HpnicfCBQoSFrPvcCarConformBytes_Type()
)
hpnicfCBQoSFrPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCarConformBytes.setStatus("current")
_HpnicfCBQoSFrPvcCarExceedPackets_Type = Counter64
_HpnicfCBQoSFrPvcCarExceedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcCarExceedPackets = _HpnicfCBQoSFrPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 3, 1, 3),
    _HpnicfCBQoSFrPvcCarExceedPackets_Type()
)
hpnicfCBQoSFrPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCarExceedPackets.setStatus("current")
_HpnicfCBQoSFrPvcCarExceedBytes_Type = Counter64
_HpnicfCBQoSFrPvcCarExceedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcCarExceedBytes = _HpnicfCBQoSFrPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 3, 1, 4),
    _HpnicfCBQoSFrPvcCarExceedBytes_Type()
)
hpnicfCBQoSFrPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcCarExceedBytes.setStatus("current")
_HpnicfCBQoSFrPvcGtsRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcGtsRunInfoTable = _HpnicfCBQoSFrPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcGtsRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcGtsRunInfoEntry = _HpnicfCBQoSFrPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1)
)
hpnicfCBQoSFrPvcGtsRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcGtsPassedPackets_Type = Counter64
_HpnicfCBQoSFrPvcGtsPassedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsPassedPackets = _HpnicfCBQoSFrPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 1),
    _HpnicfCBQoSFrPvcGtsPassedPackets_Type()
)
hpnicfCBQoSFrPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsPassedPackets.setStatus("current")
_HpnicfCBQoSFrPvcGtsPassedBytes_Type = Counter64
_HpnicfCBQoSFrPvcGtsPassedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsPassedBytes = _HpnicfCBQoSFrPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 2),
    _HpnicfCBQoSFrPvcGtsPassedBytes_Type()
)
hpnicfCBQoSFrPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsPassedBytes.setStatus("current")
_HpnicfCBQoSFrPvcGtsDiscardedPackets_Type = Counter64
_HpnicfCBQoSFrPvcGtsDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsDiscardedPackets = _HpnicfCBQoSFrPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 3),
    _HpnicfCBQoSFrPvcGtsDiscardedPackets_Type()
)
hpnicfCBQoSFrPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsDiscardedPackets.setStatus("current")
_HpnicfCBQoSFrPvcGtsDiscardedBytes_Type = Counter64
_HpnicfCBQoSFrPvcGtsDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsDiscardedBytes = _HpnicfCBQoSFrPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 4),
    _HpnicfCBQoSFrPvcGtsDiscardedBytes_Type()
)
hpnicfCBQoSFrPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsDiscardedBytes.setStatus("current")
_HpnicfCBQoSFrPvcGtsDelayedPackets_Type = Counter64
_HpnicfCBQoSFrPvcGtsDelayedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsDelayedPackets = _HpnicfCBQoSFrPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 5),
    _HpnicfCBQoSFrPvcGtsDelayedPackets_Type()
)
hpnicfCBQoSFrPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsDelayedPackets.setStatus("current")
_HpnicfCBQoSFrPvcGtsDelayedBytes_Type = Counter64
_HpnicfCBQoSFrPvcGtsDelayedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsDelayedBytes = _HpnicfCBQoSFrPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 6),
    _HpnicfCBQoSFrPvcGtsDelayedBytes_Type()
)
hpnicfCBQoSFrPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsDelayedBytes.setStatus("current")
_HpnicfCBQoSFrPvcGtsQueueSize_Type = Integer32
_HpnicfCBQoSFrPvcGtsQueueSize_Object = MibTableColumn
hpnicfCBQoSFrPvcGtsQueueSize = _HpnicfCBQoSFrPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 4, 1, 7),
    _HpnicfCBQoSFrPvcGtsQueueSize_Type()
)
hpnicfCBQoSFrPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcGtsQueueSize.setStatus("current")
_HpnicfCBQoSFrPvcRemarkRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcRemarkRunInfoTable = _HpnicfCBQoSFrPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcRemarkRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcRemarkRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcRemarkRunInfoEntry = _HpnicfCBQoSFrPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 5, 1)
)
hpnicfCBQoSFrPvcRemarkRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcRemarkRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcRemarkedPackets_Type = Counter64
_HpnicfCBQoSFrPvcRemarkedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcRemarkedPackets = _HpnicfCBQoSFrPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 5, 1, 1),
    _HpnicfCBQoSFrPvcRemarkedPackets_Type()
)
hpnicfCBQoSFrPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcRemarkedPackets.setStatus("current")
_HpnicfCBQoSFrPvcQueueRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcQueueRunInfoTable = _HpnicfCBQoSFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcQueueRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcQueueRunInfoEntry = _HpnicfCBQoSFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1)
)
hpnicfCBQoSFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcQueueMatchedPackets_Type = Counter64
_HpnicfCBQoSFrPvcQueueMatchedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcQueueMatchedPackets = _HpnicfCBQoSFrPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1, 1),
    _HpnicfCBQoSFrPvcQueueMatchedPackets_Type()
)
hpnicfCBQoSFrPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueMatchedPackets.setStatus("current")
_HpnicfCBQoSFrPvcQueueMatchedBytes_Type = Counter64
_HpnicfCBQoSFrPvcQueueMatchedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcQueueMatchedBytes = _HpnicfCBQoSFrPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1, 2),
    _HpnicfCBQoSFrPvcQueueMatchedBytes_Type()
)
hpnicfCBQoSFrPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueMatchedBytes.setStatus("current")
_HpnicfCBQoSFrPvcQueueEnqueuedPackets_Type = Counter64
_HpnicfCBQoSFrPvcQueueEnqueuedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcQueueEnqueuedPackets = _HpnicfCBQoSFrPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1, 3),
    _HpnicfCBQoSFrPvcQueueEnqueuedPackets_Type()
)
hpnicfCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueEnqueuedPackets.setStatus("current")
_HpnicfCBQoSFrPvcQueueEnqueuedBytes_Type = Counter64
_HpnicfCBQoSFrPvcQueueEnqueuedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcQueueEnqueuedBytes = _HpnicfCBQoSFrPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1, 4),
    _HpnicfCBQoSFrPvcQueueEnqueuedBytes_Type()
)
hpnicfCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueEnqueuedBytes.setStatus("current")
_HpnicfCBQoSFrPvcQueueDiscardedPackets_Type = Counter64
_HpnicfCBQoSFrPvcQueueDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcQueueDiscardedPackets = _HpnicfCBQoSFrPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1, 5),
    _HpnicfCBQoSFrPvcQueueDiscardedPackets_Type()
)
hpnicfCBQoSFrPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueDiscardedPackets.setStatus("current")
_HpnicfCBQoSFrPvcQueueDiscardedBytes_Type = Counter64
_HpnicfCBQoSFrPvcQueueDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcQueueDiscardedBytes = _HpnicfCBQoSFrPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 6, 1, 6),
    _HpnicfCBQoSFrPvcQueueDiscardedBytes_Type()
)
hpnicfCBQoSFrPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcQueueDiscardedBytes.setStatus("current")
_HpnicfCBQoSFrPvcWredRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcWredRunInfoTable = _HpnicfCBQoSFrPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcWredRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcWredRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcWredRunInfoEntry = _HpnicfCBQoSFrPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 7, 1)
)
hpnicfCBQoSFrPvcWredRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcWredRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Type = Counter64
_HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcWredRandomDiscardedPackets = _HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 7, 1, 1),
    _HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Type()
)
hpnicfCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcWredRandomDiscardedPackets.setStatus("current")
_HpnicfCBQoSFrPvcWredTailDiscardedPackets_Type = Counter64
_HpnicfCBQoSFrPvcWredTailDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcWredTailDiscardedPackets = _HpnicfCBQoSFrPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 7, 1, 2),
    _HpnicfCBQoSFrPvcWredTailDiscardedPackets_Type()
)
hpnicfCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcWredTailDiscardedPackets.setStatus("current")
_HpnicfCBQoSFrPvcAccountingRunInfoTable_Object = MibTable
hpnicfCBQoSFrPvcAccountingRunInfoTable = _HpnicfCBQoSFrPvcAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcAccountingRunInfoTable.setStatus("current")
_HpnicfCBQoSFrPvcAccountingRunInfoEntry_Object = MibTableRow
hpnicfCBQoSFrPvcAccountingRunInfoEntry = _HpnicfCBQoSFrPvcAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 8, 1)
)
hpnicfCBQoSFrPvcAccountingRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSFrPvcApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcAccountingRunInfoEntry.setStatus("current")
_HpnicfCBQoSFrPvcAccountingPackets_Type = Counter64
_HpnicfCBQoSFrPvcAccountingPackets_Object = MibTableColumn
hpnicfCBQoSFrPvcAccountingPackets = _HpnicfCBQoSFrPvcAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 8, 1, 1),
    _HpnicfCBQoSFrPvcAccountingPackets_Type()
)
hpnicfCBQoSFrPvcAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcAccountingPackets.setStatus("current")
_HpnicfCBQoSFrPvcAccountingBytes_Type = Counter64
_HpnicfCBQoSFrPvcAccountingBytes_Object = MibTableColumn
hpnicfCBQoSFrPvcAccountingBytes = _HpnicfCBQoSFrPvcAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 3, 8, 1, 2),
    _HpnicfCBQoSFrPvcAccountingBytes_Type()
)
hpnicfCBQoSFrPvcAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSFrPvcAccountingBytes.setStatus("current")
_HpnicfCBQoSVlanStaticsObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSVlanStaticsObjects = _HpnicfCBQoSVlanStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4)
)
_HpnicfCBQoSVlanClassMatchRunInfoTable_Object = MibTable
hpnicfCBQoSVlanClassMatchRunInfoTable = _HpnicfCBQoSVlanClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanClassMatchRunInfoTable.setStatus("current")
_HpnicfCBQoSVlanClassMatchRunInfoEntry_Object = MibTableRow
hpnicfCBQoSVlanClassMatchRunInfoEntry = _HpnicfCBQoSVlanClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 1, 1)
)
hpnicfCBQoSVlanClassMatchRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyVlanid"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanClassMatchRunInfoEntry.setStatus("current")
_HpnicfCBQoSVlanClassMatchedPackets_Type = Counter64
_HpnicfCBQoSVlanClassMatchedPackets_Object = MibTableColumn
hpnicfCBQoSVlanClassMatchedPackets = _HpnicfCBQoSVlanClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 1, 1, 1),
    _HpnicfCBQoSVlanClassMatchedPackets_Type()
)
hpnicfCBQoSVlanClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanClassMatchedPackets.setStatus("current")
_HpnicfCBQoSVlanAccountingRunInfoTable_Object = MibTable
hpnicfCBQoSVlanAccountingRunInfoTable = _HpnicfCBQoSVlanAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanAccountingRunInfoTable.setStatus("current")
_HpnicfCBQoSVlanAccountingRunInfoEntry_Object = MibTableRow
hpnicfCBQoSVlanAccountingRunInfoEntry = _HpnicfCBQoSVlanAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 2, 1)
)
hpnicfCBQoSVlanAccountingRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyVlanid"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyDirection"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanAccountingRunInfoEntry.setStatus("current")
_HpnicfCBQoSVlanAccountingPackets_Type = Counter64
_HpnicfCBQoSVlanAccountingPackets_Object = MibTableColumn
hpnicfCBQoSVlanAccountingPackets = _HpnicfCBQoSVlanAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 2, 1, 1),
    _HpnicfCBQoSVlanAccountingPackets_Type()
)
hpnicfCBQoSVlanAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanAccountingPackets.setStatus("current")
_HpnicfCBQoSVlanAccountingBytes_Type = Counter64
_HpnicfCBQoSVlanAccountingBytes_Object = MibTableColumn
hpnicfCBQoSVlanAccountingBytes = _HpnicfCBQoSVlanAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 4, 2, 1, 2),
    _HpnicfCBQoSVlanAccountingBytes_Type()
)
hpnicfCBQoSVlanAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanAccountingBytes.setStatus("current")
_HpnicfCBQoSApplyPolicyIndexObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSApplyPolicyIndexObjects = _HpnicfCBQoSApplyPolicyIndexObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5)
)
_HpnicfCBQoSApplyObjectTable_Object = MibTable
hpnicfCBQoSApplyObjectTable = _HpnicfCBQoSApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectTable.setStatus("current")
_HpnicfCBQoSApplyObjectEntry_Object = MibTableRow
hpnicfCBQoSApplyObjectEntry = _HpnicfCBQoSApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1)
)
hpnicfCBQoSApplyObjectEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectEntry.setStatus("current")
_HpnicfCBQoSApplyObjectIndex_Type = Unsigned32
_HpnicfCBQoSApplyObjectIndex_Object = MibTableColumn
hpnicfCBQoSApplyObjectIndex = _HpnicfCBQoSApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 1),
    _HpnicfCBQoSApplyObjectIndex_Type()
)
hpnicfCBQoSApplyObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectIndex.setStatus("current")
_HpnicfCBQoSApplyObjectType_Type = ApplyObjectType
_HpnicfCBQoSApplyObjectType_Object = MibTableColumn
hpnicfCBQoSApplyObjectType = _HpnicfCBQoSApplyObjectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 2),
    _HpnicfCBQoSApplyObjectType_Type()
)
hpnicfCBQoSApplyObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectType.setStatus("current")
_HpnicfCBQoSApplyObjectDirection_Type = DirectionType
_HpnicfCBQoSApplyObjectDirection_Object = MibTableColumn
hpnicfCBQoSApplyObjectDirection = _HpnicfCBQoSApplyObjectDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 3),
    _HpnicfCBQoSApplyObjectDirection_Type()
)
hpnicfCBQoSApplyObjectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectDirection.setStatus("current")
_HpnicfCBQoSApplyObjectMainSite_Type = Unsigned32
_HpnicfCBQoSApplyObjectMainSite_Object = MibTableColumn
hpnicfCBQoSApplyObjectMainSite = _HpnicfCBQoSApplyObjectMainSite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 4),
    _HpnicfCBQoSApplyObjectMainSite_Type()
)
hpnicfCBQoSApplyObjectMainSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectMainSite.setStatus("current")
_HpnicfCBQoSApplyObjectSubChannel_Type = Unsigned32
_HpnicfCBQoSApplyObjectSubChannel_Object = MibTableColumn
hpnicfCBQoSApplyObjectSubChannel = _HpnicfCBQoSApplyObjectSubChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 5),
    _HpnicfCBQoSApplyObjectSubChannel_Type()
)
hpnicfCBQoSApplyObjectSubChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectSubChannel.setStatus("current")
_HpnicfCBQoSApplyObjectSubClass_Type = Unsigned32
_HpnicfCBQoSApplyObjectSubClass_Object = MibTableColumn
hpnicfCBQoSApplyObjectSubClass = _HpnicfCBQoSApplyObjectSubClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 6),
    _HpnicfCBQoSApplyObjectSubClass_Type()
)
hpnicfCBQoSApplyObjectSubClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectSubClass.setStatus("current")
_HpnicfCBQoSApplyObjectSubClassSec_Type = Unsigned32
_HpnicfCBQoSApplyObjectSubClassSec_Object = MibTableColumn
hpnicfCBQoSApplyObjectSubClassSec = _HpnicfCBQoSApplyObjectSubClassSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 1, 1, 7),
    _HpnicfCBQoSApplyObjectSubClassSec_Type()
)
hpnicfCBQoSApplyObjectSubClassSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyObjectSubClassSec.setStatus("current")
_HpnicfCBQoSIntApplyObjectTable_Object = MibTable
hpnicfCBQoSIntApplyObjectTable = _HpnicfCBQoSIntApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIntApplyObjectTable.setStatus("current")
_HpnicfCBQoSIntApplyObjectEntry_Object = MibTableRow
hpnicfCBQoSIntApplyObjectEntry = _HpnicfCBQoSIntApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 2, 1)
)
hpnicfCBQoSIntApplyObjectEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIntApplyObjectIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIntApplyObjectEntry.setStatus("current")
_HpnicfCBQoSIntApplyObjectIfIndex_Type = Unsigned32
_HpnicfCBQoSIntApplyObjectIfIndex_Object = MibTableColumn
hpnicfCBQoSIntApplyObjectIfIndex = _HpnicfCBQoSIntApplyObjectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 2, 1, 1),
    _HpnicfCBQoSIntApplyObjectIfIndex_Type()
)
hpnicfCBQoSIntApplyObjectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSIntApplyObjectIfIndex.setStatus("current")
_HpnicfCBQoSIntApplyObjectIndex_Type = Unsigned32
_HpnicfCBQoSIntApplyObjectIndex_Object = MibTableColumn
hpnicfCBQoSIntApplyObjectIndex = _HpnicfCBQoSIntApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 2, 1, 2),
    _HpnicfCBQoSIntApplyObjectIndex_Type()
)
hpnicfCBQoSIntApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSIntApplyObjectIndex.setStatus("current")
_HpnicfCBQoSVlanApplyObjectTable_Object = MibTable
hpnicfCBQoSVlanApplyObjectTable = _HpnicfCBQoSVlanApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyObjectTable.setStatus("current")
_HpnicfCBQoSVlanApplyObjectEntry_Object = MibTableRow
hpnicfCBQoSVlanApplyObjectEntry = _HpnicfCBQoSVlanApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 3, 1)
)
hpnicfCBQoSVlanApplyObjectEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyObjectVlanID"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyObjectEntry.setStatus("current")


class _HpnicfCBQoSVlanApplyObjectVlanID_Type(Unsigned32):
    """Custom type hpnicfCBQoSVlanApplyObjectVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfCBQoSVlanApplyObjectVlanID_Type.__name__ = "Unsigned32"
_HpnicfCBQoSVlanApplyObjectVlanID_Object = MibTableColumn
hpnicfCBQoSVlanApplyObjectVlanID = _HpnicfCBQoSVlanApplyObjectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 3, 1, 1),
    _HpnicfCBQoSVlanApplyObjectVlanID_Type()
)
hpnicfCBQoSVlanApplyObjectVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyObjectVlanID.setStatus("current")
_HpnicfCBQoSVlanApplyObjectIndex_Type = Unsigned32
_HpnicfCBQoSVlanApplyObjectIndex_Object = MibTableColumn
hpnicfCBQoSVlanApplyObjectIndex = _HpnicfCBQoSVlanApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 3, 1, 2),
    _HpnicfCBQoSVlanApplyObjectIndex_Type()
)
hpnicfCBQoSVlanApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanApplyObjectIndex.setStatus("current")
_HpnicfCBQoSPvcApplyObjectTable_Object = MibTable
hpnicfCBQoSPvcApplyObjectTable = _HpnicfCBQoSPvcApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPvcApplyObjectTable.setStatus("current")
_HpnicfCBQoSPvcApplyObjectEntry_Object = MibTableRow
hpnicfCBQoSPvcApplyObjectEntry = _HpnicfCBQoSPvcApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 4, 1)
)
hpnicfCBQoSPvcApplyObjectEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPvcApplyObjectIfIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPvcApplyObjectPvcID"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSPvcApplyObjectEntry.setStatus("current")
_HpnicfCBQoSPvcApplyObjectIfIndex_Type = Unsigned32
_HpnicfCBQoSPvcApplyObjectIfIndex_Object = MibTableColumn
hpnicfCBQoSPvcApplyObjectIfIndex = _HpnicfCBQoSPvcApplyObjectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 4, 1, 1),
    _HpnicfCBQoSPvcApplyObjectIfIndex_Type()
)
hpnicfCBQoSPvcApplyObjectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSPvcApplyObjectIfIndex.setStatus("current")
_HpnicfCBQoSPvcApplyObjectPvcID_Type = Unsigned32
_HpnicfCBQoSPvcApplyObjectPvcID_Object = MibTableColumn
hpnicfCBQoSPvcApplyObjectPvcID = _HpnicfCBQoSPvcApplyObjectPvcID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 4, 1, 2),
    _HpnicfCBQoSPvcApplyObjectPvcID_Type()
)
hpnicfCBQoSPvcApplyObjectPvcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSPvcApplyObjectPvcID.setStatus("current")
_HpnicfCBQoSPvcApplyObjectIndex_Type = Unsigned32
_HpnicfCBQoSPvcApplyObjectIndex_Object = MibTableColumn
hpnicfCBQoSPvcApplyObjectIndex = _HpnicfCBQoSPvcApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 4, 1, 3),
    _HpnicfCBQoSPvcApplyObjectIndex_Type()
)
hpnicfCBQoSPvcApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSPvcApplyObjectIndex.setStatus("current")
_HpnicfCBQoSNestPolicyApplyObjectTable_Object = MibTable
hpnicfCBQoSNestPolicyApplyObjectTable = _HpnicfCBQoSNestPolicyApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyApplyObjectTable.setStatus("current")
_HpnicfCBQoSNestPolicyApplyObjectEntry_Object = MibTableRow
hpnicfCBQoSNestPolicyApplyObjectEntry = _HpnicfCBQoSNestPolicyApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 5, 1)
)
hpnicfCBQoSNestPolicyApplyObjectEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSNestPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyApplyObjectEntry.setStatus("current")
_HpnicfCBQoSNestPolicyClassIndex_Type = Unsigned32
_HpnicfCBQoSNestPolicyClassIndex_Object = MibTableColumn
hpnicfCBQoSNestPolicyClassIndex = _HpnicfCBQoSNestPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 5, 1, 1),
    _HpnicfCBQoSNestPolicyClassIndex_Type()
)
hpnicfCBQoSNestPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyClassIndex.setStatus("current")
_HpnicfCBQoSNestPolicyApplyObjectIndex_Type = Unsigned32
_HpnicfCBQoSNestPolicyApplyObjectIndex_Object = MibTableColumn
hpnicfCBQoSNestPolicyApplyObjectIndex = _HpnicfCBQoSNestPolicyApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 5, 1, 2),
    _HpnicfCBQoSNestPolicyApplyObjectIndex_Type()
)
hpnicfCBQoSNestPolicyApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSNestPolicyApplyObjectIndex.setStatus("current")
_HpnicfCBQoSCpApplyObjectTable_Object = MibTable
hpnicfCBQoSCpApplyObjectTable = _HpnicfCBQoSCpApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyObjectTable.setStatus("current")
_HpnicfCBQoSCpApplyObjectEntry_Object = MibTableRow
hpnicfCBQoSCpApplyObjectEntry = _HpnicfCBQoSCpApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 6, 1)
)
hpnicfCBQoSCpApplyObjectEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSCpApplyObjectChassis"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSCpApplyObjectSlot"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyObjectEntry.setStatus("current")
_HpnicfCBQoSCpApplyObjectChassis_Type = Unsigned32
_HpnicfCBQoSCpApplyObjectChassis_Object = MibTableColumn
hpnicfCBQoSCpApplyObjectChassis = _HpnicfCBQoSCpApplyObjectChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 6, 1, 1),
    _HpnicfCBQoSCpApplyObjectChassis_Type()
)
hpnicfCBQoSCpApplyObjectChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyObjectChassis.setStatus("current")
_HpnicfCBQoSCpApplyObjectSlot_Type = Unsigned32
_HpnicfCBQoSCpApplyObjectSlot_Object = MibTableColumn
hpnicfCBQoSCpApplyObjectSlot = _HpnicfCBQoSCpApplyObjectSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 6, 1, 2),
    _HpnicfCBQoSCpApplyObjectSlot_Type()
)
hpnicfCBQoSCpApplyObjectSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyObjectSlot.setStatus("current")
_HpnicfCBQoSCpApplyObjectIndex_Type = Unsigned32
_HpnicfCBQoSCpApplyObjectIndex_Object = MibTableColumn
hpnicfCBQoSCpApplyObjectIndex = _HpnicfCBQoSCpApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 5, 6, 1, 3),
    _HpnicfCBQoSCpApplyObjectIndex_Type()
)
hpnicfCBQoSCpApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCpApplyObjectIndex.setStatus("current")
_HpnicfCBQoSStaticsObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSStaticsObjects = _HpnicfCBQoSStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6)
)
_HpnicfCBQoSCbqRunInfoTable_Object = MibTable
hpnicfCBQoSCbqRunInfoTable = _HpnicfCBQoSCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqRunInfoTable.setStatus("current")
_HpnicfCBQoSCbqRunInfoEntry_Object = MibTableRow
hpnicfCBQoSCbqRunInfoEntry = _HpnicfCBQoSCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1)
)
hpnicfCBQoSCbqRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqRunInfoEntry.setStatus("current")
_HpnicfCBQoSCbqQueueSize_Type = Integer32
_HpnicfCBQoSCbqQueueSize_Object = MibTableColumn
hpnicfCBQoSCbqQueueSize = _HpnicfCBQoSCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 1),
    _HpnicfCBQoSCbqQueueSize_Type()
)
hpnicfCBQoSCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqQueueSize.setStatus("current")
_HpnicfCBQoSCbqDiscard_Type = Counter64
_HpnicfCBQoSCbqDiscard_Object = MibTableColumn
hpnicfCBQoSCbqDiscard = _HpnicfCBQoSCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 2),
    _HpnicfCBQoSCbqDiscard_Type()
)
hpnicfCBQoSCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqDiscard.setStatus("current")
_HpnicfCBQoSCbqEfQueueSize_Type = Integer32
_HpnicfCBQoSCbqEfQueueSize_Object = MibTableColumn
hpnicfCBQoSCbqEfQueueSize = _HpnicfCBQoSCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 3),
    _HpnicfCBQoSCbqEfQueueSize_Type()
)
hpnicfCBQoSCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqEfQueueSize.setStatus("current")
_HpnicfCBQoSCbqAfQueueSize_Type = Integer32
_HpnicfCBQoSCbqAfQueueSize_Object = MibTableColumn
hpnicfCBQoSCbqAfQueueSize = _HpnicfCBQoSCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 4),
    _HpnicfCBQoSCbqAfQueueSize_Type()
)
hpnicfCBQoSCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqAfQueueSize.setStatus("current")
_HpnicfCBQoSCbqBeQueueSize_Type = Integer32
_HpnicfCBQoSCbqBeQueueSize_Object = MibTableColumn
hpnicfCBQoSCbqBeQueueSize = _HpnicfCBQoSCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 5),
    _HpnicfCBQoSCbqBeQueueSize_Type()
)
hpnicfCBQoSCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqBeQueueSize.setStatus("current")
_HpnicfCBQoSCbqBeActiveQueueNum_Type = Integer32
_HpnicfCBQoSCbqBeActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSCbqBeActiveQueueNum = _HpnicfCBQoSCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 6),
    _HpnicfCBQoSCbqBeActiveQueueNum_Type()
)
hpnicfCBQoSCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqBeActiveQueueNum.setStatus("current")
_HpnicfCBQoSCbqBeMaxActiveQueueNum_Type = Integer32
_HpnicfCBQoSCbqBeMaxActiveQueueNum_Object = MibTableColumn
hpnicfCBQoSCbqBeMaxActiveQueueNum = _HpnicfCBQoSCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 7),
    _HpnicfCBQoSCbqBeMaxActiveQueueNum_Type()
)
hpnicfCBQoSCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqBeMaxActiveQueueNum.setStatus("current")
_HpnicfCBQoSCbqBeTotalQueueNum_Type = Integer32
_HpnicfCBQoSCbqBeTotalQueueNum_Object = MibTableColumn
hpnicfCBQoSCbqBeTotalQueueNum = _HpnicfCBQoSCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 8),
    _HpnicfCBQoSCbqBeTotalQueueNum_Type()
)
hpnicfCBQoSCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqBeTotalQueueNum.setStatus("current")
_HpnicfCBQoSCbqAfAllocatedQueueNum_Type = Integer32
_HpnicfCBQoSCbqAfAllocatedQueueNum_Object = MibTableColumn
hpnicfCBQoSCbqAfAllocatedQueueNum = _HpnicfCBQoSCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 1, 1, 9),
    _HpnicfCBQoSCbqAfAllocatedQueueNum_Type()
)
hpnicfCBQoSCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCbqAfAllocatedQueueNum.setStatus("current")
_HpnicfCBQoSClassMatchRunInfoTable_Object = MibTable
hpnicfCBQoSClassMatchRunInfoTable = _HpnicfCBQoSClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSClassMatchRunInfoTable.setStatus("current")
_HpnicfCBQoSClassMatchRunInfoEntry_Object = MibTableRow
hpnicfCBQoSClassMatchRunInfoEntry = _HpnicfCBQoSClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1)
)
hpnicfCBQoSClassMatchRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSClassMatchRunInfoEntry.setStatus("current")
_HpnicfCBQoSClassMatchedPackets_Type = Counter64
_HpnicfCBQoSClassMatchedPackets_Object = MibTableColumn
hpnicfCBQoSClassMatchedPackets = _HpnicfCBQoSClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 1),
    _HpnicfCBQoSClassMatchedPackets_Type()
)
hpnicfCBQoSClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassMatchedPackets.setStatus("current")
_HpnicfCBQoSClassMatchedBytes_Type = Counter64
_HpnicfCBQoSClassMatchedBytes_Object = MibTableColumn
hpnicfCBQoSClassMatchedBytes = _HpnicfCBQoSClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 2),
    _HpnicfCBQoSClassMatchedBytes_Type()
)
hpnicfCBQoSClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassMatchedBytes.setStatus("current")
_HpnicfCBQoSClassFwdPktpps_Type = Unsigned32
_HpnicfCBQoSClassFwdPktpps_Object = MibTableColumn
hpnicfCBQoSClassFwdPktpps = _HpnicfCBQoSClassFwdPktpps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 3),
    _HpnicfCBQoSClassFwdPktpps_Type()
)
hpnicfCBQoSClassFwdPktpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassFwdPktpps.setStatus("current")
_HpnicfCBQoSClassFwdPktbps_Type = Unsigned32
_HpnicfCBQoSClassFwdPktbps_Object = MibTableColumn
hpnicfCBQoSClassFwdPktbps = _HpnicfCBQoSClassFwdPktbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 4),
    _HpnicfCBQoSClassFwdPktbps_Type()
)
hpnicfCBQoSClassFwdPktbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassFwdPktbps.setStatus("current")
_HpnicfCBQoSClassDropPktpps_Type = Unsigned32
_HpnicfCBQoSClassDropPktpps_Object = MibTableColumn
hpnicfCBQoSClassDropPktpps = _HpnicfCBQoSClassDropPktpps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 5),
    _HpnicfCBQoSClassDropPktpps_Type()
)
hpnicfCBQoSClassDropPktpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassDropPktpps.setStatus("current")
_HpnicfCBQoSClassDropPktbps_Type = Unsigned32
_HpnicfCBQoSClassDropPktbps_Object = MibTableColumn
hpnicfCBQoSClassDropPktbps = _HpnicfCBQoSClassDropPktbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 6),
    _HpnicfCBQoSClassDropPktbps_Type()
)
hpnicfCBQoSClassDropPktbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassDropPktbps.setStatus("current")
_HpnicfCBQoSClassFlowStatInterval_Type = Unsigned32
_HpnicfCBQoSClassFlowStatInterval_Object = MibTableColumn
hpnicfCBQoSClassFlowStatInterval = _HpnicfCBQoSClassFlowStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 7),
    _HpnicfCBQoSClassFlowStatInterval_Type()
)
hpnicfCBQoSClassFlowStatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassFlowStatInterval.setStatus("current")


class _HpnicfCBQoSClassBehaviorStatus_Type(Integer32):
    """Custom type hpnicfCBQoSClassBehaviorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("partialSuccess", 3),
          ("success", 1))
    )


_HpnicfCBQoSClassBehaviorStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSClassBehaviorStatus_Object = MibTableColumn
hpnicfCBQoSClassBehaviorStatus = _HpnicfCBQoSClassBehaviorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 2, 1, 8),
    _HpnicfCBQoSClassBehaviorStatus_Type()
)
hpnicfCBQoSClassBehaviorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSClassBehaviorStatus.setStatus("current")
_HpnicfCBQoSCarRunInfoTable_Object = MibTable
hpnicfCBQoSCarRunInfoTable = _HpnicfCBQoSCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRunInfoTable.setStatus("current")
_HpnicfCBQoSCarRunInfoEntry_Object = MibTableRow
hpnicfCBQoSCarRunInfoEntry = _HpnicfCBQoSCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1)
)
hpnicfCBQoSCarRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRunInfoEntry.setStatus("current")
_HpnicfCBQoSCarGreenPackets_Type = Counter64
_HpnicfCBQoSCarGreenPackets_Object = MibTableColumn
hpnicfCBQoSCarGreenPackets = _HpnicfCBQoSCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1, 1),
    _HpnicfCBQoSCarGreenPackets_Type()
)
hpnicfCBQoSCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarGreenPackets.setStatus("current")
_HpnicfCBQoSCarGreenBytes_Type = Counter64
_HpnicfCBQoSCarGreenBytes_Object = MibTableColumn
hpnicfCBQoSCarGreenBytes = _HpnicfCBQoSCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1, 2),
    _HpnicfCBQoSCarGreenBytes_Type()
)
hpnicfCBQoSCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarGreenBytes.setStatus("current")
_HpnicfCBQoSCarRedPackets_Type = Counter64
_HpnicfCBQoSCarRedPackets_Object = MibTableColumn
hpnicfCBQoSCarRedPackets = _HpnicfCBQoSCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1, 3),
    _HpnicfCBQoSCarRedPackets_Type()
)
hpnicfCBQoSCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRedPackets.setStatus("current")
_HpnicfCBQoSCarRedBytes_Type = Counter64
_HpnicfCBQoSCarRedBytes_Object = MibTableColumn
hpnicfCBQoSCarRedBytes = _HpnicfCBQoSCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1, 4),
    _HpnicfCBQoSCarRedBytes_Type()
)
hpnicfCBQoSCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarRedBytes.setStatus("current")
_HpnicfCBQoSCarYellowPackets_Type = Counter64
_HpnicfCBQoSCarYellowPackets_Object = MibTableColumn
hpnicfCBQoSCarYellowPackets = _HpnicfCBQoSCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1, 5),
    _HpnicfCBQoSCarYellowPackets_Type()
)
hpnicfCBQoSCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarYellowPackets.setStatus("current")
_HpnicfCBQoSCarYellowBytes_Type = Counter64
_HpnicfCBQoSCarYellowBytes_Object = MibTableColumn
hpnicfCBQoSCarYellowBytes = _HpnicfCBQoSCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 3, 1, 6),
    _HpnicfCBQoSCarYellowBytes_Type()
)
hpnicfCBQoSCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSCarYellowBytes.setStatus("current")
_HpnicfCBQoSGtsRunInfoTable_Object = MibTable
hpnicfCBQoSGtsRunInfoTable = _HpnicfCBQoSGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsRunInfoTable.setStatus("current")
_HpnicfCBQoSGtsRunInfoEntry_Object = MibTableRow
hpnicfCBQoSGtsRunInfoEntry = _HpnicfCBQoSGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1)
)
hpnicfCBQoSGtsRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsRunInfoEntry.setStatus("current")
_HpnicfCBQoSGtsPassedPackets_Type = Counter64
_HpnicfCBQoSGtsPassedPackets_Object = MibTableColumn
hpnicfCBQoSGtsPassedPackets = _HpnicfCBQoSGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 1),
    _HpnicfCBQoSGtsPassedPackets_Type()
)
hpnicfCBQoSGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsPassedPackets.setStatus("current")
_HpnicfCBQoSGtsPassedBytes_Type = Counter64
_HpnicfCBQoSGtsPassedBytes_Object = MibTableColumn
hpnicfCBQoSGtsPassedBytes = _HpnicfCBQoSGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 2),
    _HpnicfCBQoSGtsPassedBytes_Type()
)
hpnicfCBQoSGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsPassedBytes.setStatus("current")
_HpnicfCBQoSGtsDiscardedPackets_Type = Counter64
_HpnicfCBQoSGtsDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSGtsDiscardedPackets = _HpnicfCBQoSGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 3),
    _HpnicfCBQoSGtsDiscardedPackets_Type()
)
hpnicfCBQoSGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsDiscardedPackets.setStatus("current")
_HpnicfCBQoSGtsDiscardedBytes_Type = Counter64
_HpnicfCBQoSGtsDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSGtsDiscardedBytes = _HpnicfCBQoSGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 4),
    _HpnicfCBQoSGtsDiscardedBytes_Type()
)
hpnicfCBQoSGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsDiscardedBytes.setStatus("current")
_HpnicfCBQoSGtsDelayedPackets_Type = Counter64
_HpnicfCBQoSGtsDelayedPackets_Object = MibTableColumn
hpnicfCBQoSGtsDelayedPackets = _HpnicfCBQoSGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 5),
    _HpnicfCBQoSGtsDelayedPackets_Type()
)
hpnicfCBQoSGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsDelayedPackets.setStatus("current")
_HpnicfCBQoSGtsDelayedBytes_Type = Counter64
_HpnicfCBQoSGtsDelayedBytes_Object = MibTableColumn
hpnicfCBQoSGtsDelayedBytes = _HpnicfCBQoSGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 6),
    _HpnicfCBQoSGtsDelayedBytes_Type()
)
hpnicfCBQoSGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsDelayedBytes.setStatus("current")
_HpnicfCBQoSGtsQueueSize_Type = Integer32
_HpnicfCBQoSGtsQueueSize_Object = MibTableColumn
hpnicfCBQoSGtsQueueSize = _HpnicfCBQoSGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 4, 1, 7),
    _HpnicfCBQoSGtsQueueSize_Type()
)
hpnicfCBQoSGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSGtsQueueSize.setStatus("current")
_HpnicfCBQoSRemarkRunInfoTable_Object = MibTable
hpnicfCBQoSRemarkRunInfoTable = _HpnicfCBQoSRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkRunInfoTable.setStatus("current")
_HpnicfCBQoSRemarkRunInfoEntry_Object = MibTableRow
hpnicfCBQoSRemarkRunInfoEntry = _HpnicfCBQoSRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 5, 1)
)
hpnicfCBQoSRemarkRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkRunInfoEntry.setStatus("current")
_HpnicfCBQoSRemarkedPackets_Type = Counter64
_HpnicfCBQoSRemarkedPackets_Object = MibTableColumn
hpnicfCBQoSRemarkedPackets = _HpnicfCBQoSRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 5, 1, 1),
    _HpnicfCBQoSRemarkedPackets_Type()
)
hpnicfCBQoSRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSRemarkedPackets.setStatus("current")
_HpnicfCBQoSQueueRunInfoTable_Object = MibTable
hpnicfCBQoSQueueRunInfoTable = _HpnicfCBQoSQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueRunInfoTable.setStatus("current")
_HpnicfCBQoSQueueRunInfoEntry_Object = MibTableRow
hpnicfCBQoSQueueRunInfoEntry = _HpnicfCBQoSQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1)
)
hpnicfCBQoSQueueRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueRunInfoEntry.setStatus("current")
_HpnicfCBQoSQueueMatchedPackets_Type = Counter64
_HpnicfCBQoSQueueMatchedPackets_Object = MibTableColumn
hpnicfCBQoSQueueMatchedPackets = _HpnicfCBQoSQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1, 1),
    _HpnicfCBQoSQueueMatchedPackets_Type()
)
hpnicfCBQoSQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueMatchedPackets.setStatus("current")
_HpnicfCBQoSQueueMatchedBytes_Type = Counter64
_HpnicfCBQoSQueueMatchedBytes_Object = MibTableColumn
hpnicfCBQoSQueueMatchedBytes = _HpnicfCBQoSQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1, 2),
    _HpnicfCBQoSQueueMatchedBytes_Type()
)
hpnicfCBQoSQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueMatchedBytes.setStatus("current")
_HpnicfCBQoSQueueEnqueuedPackets_Type = Counter64
_HpnicfCBQoSQueueEnqueuedPackets_Object = MibTableColumn
hpnicfCBQoSQueueEnqueuedPackets = _HpnicfCBQoSQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1, 3),
    _HpnicfCBQoSQueueEnqueuedPackets_Type()
)
hpnicfCBQoSQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueEnqueuedPackets.setStatus("current")
_HpnicfCBQoSQueueEnqueuedBytes_Type = Counter64
_HpnicfCBQoSQueueEnqueuedBytes_Object = MibTableColumn
hpnicfCBQoSQueueEnqueuedBytes = _HpnicfCBQoSQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1, 4),
    _HpnicfCBQoSQueueEnqueuedBytes_Type()
)
hpnicfCBQoSQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueEnqueuedBytes.setStatus("current")
_HpnicfCBQoSQueueDiscardedPackets_Type = Counter64
_HpnicfCBQoSQueueDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSQueueDiscardedPackets = _HpnicfCBQoSQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1, 5),
    _HpnicfCBQoSQueueDiscardedPackets_Type()
)
hpnicfCBQoSQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueDiscardedPackets.setStatus("current")
_HpnicfCBQoSQueueDiscardedBytes_Type = Counter64
_HpnicfCBQoSQueueDiscardedBytes_Object = MibTableColumn
hpnicfCBQoSQueueDiscardedBytes = _HpnicfCBQoSQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 6, 1, 6),
    _HpnicfCBQoSQueueDiscardedBytes_Type()
)
hpnicfCBQoSQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSQueueDiscardedBytes.setStatus("current")
_HpnicfCBQoSWredRunInfoTable_Object = MibTable
hpnicfCBQoSWredRunInfoTable = _HpnicfCBQoSWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSWredRunInfoTable.setStatus("current")
_HpnicfCBQoSWredRunInfoEntry_Object = MibTableRow
hpnicfCBQoSWredRunInfoEntry = _HpnicfCBQoSWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 7, 1)
)
hpnicfCBQoSWredRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSWredRunInfoEntry.setStatus("current")
_HpnicfCBQoSWredRandomDiscardedPackets_Type = Counter64
_HpnicfCBQoSWredRandomDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSWredRandomDiscardedPackets = _HpnicfCBQoSWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 7, 1, 1),
    _HpnicfCBQoSWredRandomDiscardedPackets_Type()
)
hpnicfCBQoSWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredRandomDiscardedPackets.setStatus("current")
_HpnicfCBQoSWredTailDiscardedPackets_Type = Counter64
_HpnicfCBQoSWredTailDiscardedPackets_Object = MibTableColumn
hpnicfCBQoSWredTailDiscardedPackets = _HpnicfCBQoSWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 7, 1, 2),
    _HpnicfCBQoSWredTailDiscardedPackets_Type()
)
hpnicfCBQoSWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSWredTailDiscardedPackets.setStatus("current")
_HpnicfCBQoSAccountingRunInfoTable_Object = MibTable
hpnicfCBQoSAccountingRunInfoTable = _HpnicfCBQoSAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 8)
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountingRunInfoTable.setStatus("current")
_HpnicfCBQoSAccountingRunInfoEntry_Object = MibTableRow
hpnicfCBQoSAccountingRunInfoEntry = _HpnicfCBQoSAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 8, 1)
)
hpnicfCBQoSAccountingRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSApplyObjectIndex"),
    (0, "HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountingRunInfoEntry.setStatus("current")
_HpnicfCBQoSAccountingPackets_Type = Counter64
_HpnicfCBQoSAccountingPackets_Object = MibTableColumn
hpnicfCBQoSAccountingPackets = _HpnicfCBQoSAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 8, 1, 1),
    _HpnicfCBQoSAccountingPackets_Type()
)
hpnicfCBQoSAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountingPackets.setStatus("current")
_HpnicfCBQoSAccountingBytes_Type = Counter64
_HpnicfCBQoSAccountingBytes_Object = MibTableColumn
hpnicfCBQoSAccountingBytes = _HpnicfCBQoSAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 5, 6, 8, 1, 2),
    _HpnicfCBQoSAccountingBytes_Type()
)
hpnicfCBQoSAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSAccountingBytes.setStatus("current")
_HpnicfCBQoSApplyingStatusObjects_ObjectIdentity = ObjectIdentity
hpnicfCBQoSApplyingStatusObjects = _HpnicfCBQoSApplyingStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 6)
)


class _HpnicfCBQoSApplyingStatus_Type(Integer32):
    """Custom type hpnicfCBQoSApplyingStatus based on Integer32"""
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


_HpnicfCBQoSApplyingStatus_Type.__name__ = "Integer32"
_HpnicfCBQoSApplyingStatus_Object = MibScalar
hpnicfCBQoSApplyingStatus = _HpnicfCBQoSApplyingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 6, 1),
    _HpnicfCBQoSApplyingStatus_Type()
)
hpnicfCBQoSApplyingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCBQoSApplyingStatus.setStatus("current")
_HpnicfCBQoSNotifications_ObjectIdentity = ObjectIdentity
hpnicfCBQoSNotifications = _HpnicfCBQoSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 7)
)
_HpnicfCBQoSNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpnicfCBQoSNotificationsPrefix = _HpnicfCBQoSNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 7, 0)
)

# Managed Objects groups


# Notification objects

hpnicfCBQoSIfPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 7, 0, 1)
)
hpnicfCBQoSIfPolicyChanged.setObjects(
      *(("HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyIfIndex"),
        ("HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSIfApplyPolicyDirection"))
)
if mibBuilder.loadTexts:
    hpnicfCBQoSIfPolicyChanged.setStatus(
        "current"
    )

hpnicfCBQoSVlanPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2, 1, 7, 0, 2)
)
hpnicfCBQoSVlanPolicyChanged.setObjects(
      *(("HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyVlanid"),
        ("HPN-ICF-CBQOS2-MIB", "hpnicfCBQoSVlanApplyPolicyDirection"))
)
if mibBuilder.loadTexts:
    hpnicfCBQoSVlanPolicyChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-CBQOS2-MIB",
    **{"MatchRuleType": MatchRuleType,
       "CarAction": CarAction,
       "RemarkType": RemarkType,
       "WredType": WredType,
       "QueueType": QueueType,
       "QueueBandwidthUnit": QueueBandwidthUnit,
       "DirectionType": DirectionType,
       "ApplyObjectType": ApplyObjectType,
       "hpnicfQos2": hpnicfQos2,
       "hpnicfCBQos2": hpnicfCBQos2,
       "hpnicfCBQoSObjects": hpnicfCBQoSObjects,
       "hpnicfCBQoSClassifierObjects": hpnicfCBQoSClassifierObjects,
       "hpnicfCBQoSClassifierIndexNext": hpnicfCBQoSClassifierIndexNext,
       "hpnicfCBQoSClassifierCfgInfoTable": hpnicfCBQoSClassifierCfgInfoTable,
       "hpnicfCBQoSClassifierCfgInfoEntry": hpnicfCBQoSClassifierCfgInfoEntry,
       "hpnicfCBQoSClassifierIndex": hpnicfCBQoSClassifierIndex,
       "hpnicfCBQoSClassifierName": hpnicfCBQoSClassifierName,
       "hpnicfCBQoSClassifierRuleCount": hpnicfCBQoSClassifierRuleCount,
       "hpnicfCBQoSClassifierOperator": hpnicfCBQoSClassifierOperator,
       "hpnicfCBQoSClassifierLayer": hpnicfCBQoSClassifierLayer,
       "hpnicfCBQoSClassifierType": hpnicfCBQoSClassifierType,
       "hpnicfCBQosClassifierMatchRuleNextIndex": hpnicfCBQosClassifierMatchRuleNextIndex,
       "hpnicfCBQoSClassifierRowStatus": hpnicfCBQoSClassifierRowStatus,
       "hpnicfCBQoSMatchRuleCfgInfoTable": hpnicfCBQoSMatchRuleCfgInfoTable,
       "hpnicfCBQoSMatchRuleCfgInfoEntry": hpnicfCBQoSMatchRuleCfgInfoEntry,
       "hpnicfCBQoSMatchRuleIndex": hpnicfCBQoSMatchRuleIndex,
       "hpnicfCBQoSMatchRuleIfNot": hpnicfCBQoSMatchRuleIfNot,
       "hpnicfCBQoSMatchRuleType": hpnicfCBQoSMatchRuleType,
       "hpnicfCBQoSMatchRuleStringValue": hpnicfCBQoSMatchRuleStringValue,
       "hpnicfCBQoSMatchRuleIntValue1": hpnicfCBQoSMatchRuleIntValue1,
       "hpnicfCBQoSMatchRuleIntValue2": hpnicfCBQoSMatchRuleIntValue2,
       "hpnicfCBQoSMatchIpAddressType": hpnicfCBQoSMatchIpAddressType,
       "hpnicfCBQoSMatchIpAddress": hpnicfCBQoSMatchIpAddress,
       "hpnicfCBQoSMatchRuleRowStatus": hpnicfCBQoSMatchRuleRowStatus,
       "hpnicfCBQoSMatchCpProtoCfgTable": hpnicfCBQoSMatchCpProtoCfgTable,
       "hpnicfCBQoSMatchCpProtoCfgEntry": hpnicfCBQoSMatchCpProtoCfgEntry,
       "hpnicfCBQoSMatchCpProtoIfNot": hpnicfCBQoSMatchCpProtoIfNot,
       "hpnicfCBQoSMatchCpProtoValue": hpnicfCBQoSMatchCpProtoValue,
       "hpnicfCBQoSMatchCpProtoRowStatus": hpnicfCBQoSMatchCpProtoRowStatus,
       "hpnicfCBQoSMatchCpGroupCfgTable": hpnicfCBQoSMatchCpGroupCfgTable,
       "hpnicfCBQoSMatchCpGroupCfgEntry": hpnicfCBQoSMatchCpGroupCfgEntry,
       "hpnicfCBQoSMatchCpGroupIfNot": hpnicfCBQoSMatchCpGroupIfNot,
       "hpnicfCBQoSMatchCpGroupValue": hpnicfCBQoSMatchCpGroupValue,
       "hpnicfCBQoSMatchCpGroupRowStatus": hpnicfCBQoSMatchCpGroupRowStatus,
       "hpnicfCBQoSBehaviorObjects": hpnicfCBQoSBehaviorObjects,
       "hpnicfCBQoSBehaviorIndexNext": hpnicfCBQoSBehaviorIndexNext,
       "hpnicfCBQoSBehaviorCfgInfoTable": hpnicfCBQoSBehaviorCfgInfoTable,
       "hpnicfCBQoSBehaviorCfgInfoEntry": hpnicfCBQoSBehaviorCfgInfoEntry,
       "hpnicfCBQoSBehaviorIndex": hpnicfCBQoSBehaviorIndex,
       "hpnicfCBQoSBehaviorName": hpnicfCBQoSBehaviorName,
       "hpnicfCBQoSBehaviorType": hpnicfCBQoSBehaviorType,
       "hpnicfCBQoSBehaviorRowStatus": hpnicfCBQoSBehaviorRowStatus,
       "hpnicfCBQoSCarCfgInfoTable": hpnicfCBQoSCarCfgInfoTable,
       "hpnicfCBQoSCarCfgInfoEntry": hpnicfCBQoSCarCfgInfoEntry,
       "hpnicfCBQoSCarCir": hpnicfCBQoSCarCir,
       "hpnicfCBQoSCarCbs": hpnicfCBQoSCarCbs,
       "hpnicfCBQoSCarEbs": hpnicfCBQoSCarEbs,
       "hpnicfCBQoSCarPir": hpnicfCBQoSCarPir,
       "hpnicfCBQoSCarPbs": hpnicfCBQoSCarPbs,
       "hpnicfCBQoSCarGreenAction": hpnicfCBQoSCarGreenAction,
       "hpnicfCBQoSCarGreenRemarkValue": hpnicfCBQoSCarGreenRemarkValue,
       "hpnicfCBQoSCarYellowAction": hpnicfCBQoSCarYellowAction,
       "hpnicfCBQoSCarYellowRemarkValue": hpnicfCBQoSCarYellowRemarkValue,
       "hpnicfCBQoSCarRedAction": hpnicfCBQoSCarRedAction,
       "hpnicfCBQoSCarRedRemarkValue": hpnicfCBQoSCarRedRemarkValue,
       "hpnicfCBQoSCarPolicedPriorityMapType": hpnicfCBQoSCarPolicedPriorityMapType,
       "hpnicfCBQoSCarRowStatus": hpnicfCBQoSCarRowStatus,
       "hpnicfCBQoSAggregativeCarCfgInfoTable": hpnicfCBQoSAggregativeCarCfgInfoTable,
       "hpnicfCBQoSAggregativeCarCfgInfoEntry": hpnicfCBQoSAggregativeCarCfgInfoEntry,
       "hpnicfCBQoSCarAggregativeCarIndex": hpnicfCBQoSCarAggregativeCarIndex,
       "hpnicfCBQoSCarAggregativeCarName": hpnicfCBQoSCarAggregativeCarName,
       "hpnicfCBQoSAggregativeCarRowStatus": hpnicfCBQoSAggregativeCarRowStatus,
       "hpnicfCBQoSGtsCfgInfoTable": hpnicfCBQoSGtsCfgInfoTable,
       "hpnicfCBQoSGtsCfgInfoEntry": hpnicfCBQoSGtsCfgInfoEntry,
       "hpnicfCBQoSGtsCir": hpnicfCBQoSGtsCir,
       "hpnicfCBQoSGtsCbs": hpnicfCBQoSGtsCbs,
       "hpnicfCBQoSGtsEbs": hpnicfCBQoSGtsEbs,
       "hpnicfCBQoSGtsQueueLength": hpnicfCBQoSGtsQueueLength,
       "hpnicfCBQoSGtsRowStatus": hpnicfCBQoSGtsRowStatus,
       "hpnicfCBQoSGtsPir": hpnicfCBQoSGtsPir,
       "hpnicfCBQoSRemarkCfgInfoTable": hpnicfCBQoSRemarkCfgInfoTable,
       "hpnicfCBQoSRemarkCfgInfoEntry": hpnicfCBQoSRemarkCfgInfoEntry,
       "hpnicfCBQoSRemarkType": hpnicfCBQoSRemarkType,
       "hpnicfCBQoSRemarkValue": hpnicfCBQoSRemarkValue,
       "hpnicfCBQoSRemarkRowStatus": hpnicfCBQoSRemarkRowStatus,
       "hpnicfCBQoSQueueCfgInfoTable": hpnicfCBQoSQueueCfgInfoTable,
       "hpnicfCBQoSQueueCfgInfoEntry": hpnicfCBQoSQueueCfgInfoEntry,
       "hpnicfCBQoSQueueType": hpnicfCBQoSQueueType,
       "hpnicfCBQoSQueueDropType": hpnicfCBQoSQueueDropType,
       "hpnicfCBQoSQueueLength": hpnicfCBQoSQueueLength,
       "hpnicfCBQoSQueueBandwidthUnit": hpnicfCBQoSQueueBandwidthUnit,
       "hpnicfCBQoSQueueBandwidthValue": hpnicfCBQoSQueueBandwidthValue,
       "hpnicfCBQoSQueueCbs": hpnicfCBQoSQueueCbs,
       "hpnicfCBQoSQueueQueueNumber": hpnicfCBQoSQueueQueueNumber,
       "hpnicfCBQoSQueueCbsRatio": hpnicfCBQoSQueueCbsRatio,
       "hpnicfCBQoSQueueRowStatus": hpnicfCBQoSQueueRowStatus,
       "hpnicfCBQoSWredCfgInfoTable": hpnicfCBQoSWredCfgInfoTable,
       "hpnicfCBQoSWredCfgInfoEntry": hpnicfCBQoSWredCfgInfoEntry,
       "hpnicfCBQoSWredType": hpnicfCBQoSWredType,
       "hpnicfCBQoSWredWeightConst": hpnicfCBQoSWredWeightConst,
       "hpnicfCBQoSWredClassCfgInfoTable": hpnicfCBQoSWredClassCfgInfoTable,
       "hpnicfCBQoSWredClassCfgInfoEntry": hpnicfCBQoSWredClassCfgInfoEntry,
       "hpnicfCBQoSWredClassValue": hpnicfCBQoSWredClassValue,
       "hpnicfCBQoSWredClassLowLimit": hpnicfCBQoSWredClassLowLimit,
       "hpnicfCBQoSWredClassHighLimit": hpnicfCBQoSWredClassHighLimit,
       "hpnicfCBQoSWredClassDiscardProb": hpnicfCBQoSWredClassDiscardProb,
       "hpnicfCBQoSPolicyRouteCfgInfoTable": hpnicfCBQoSPolicyRouteCfgInfoTable,
       "hpnicfCBQoSPolicyRouteCfgInfoEntry": hpnicfCBQoSPolicyRouteCfgInfoEntry,
       "hpnicfCBQoSPolicyRouteIpAddrType": hpnicfCBQoSPolicyRouteIpAddrType,
       "hpnicfCBQoSPolicyRouteNexthop": hpnicfCBQoSPolicyRouteNexthop,
       "hpnicfCBQoSPolicyRouteBackup": hpnicfCBQoSPolicyRouteBackup,
       "hpnicfCBQoSPolicyRouteRowStatus": hpnicfCBQoSPolicyRouteRowStatus,
       "hpnicfCBQoSNatCfgInfoTable": hpnicfCBQoSNatCfgInfoTable,
       "hpnicfCBQoSNatCfgInfoEntry": hpnicfCBQoSNatCfgInfoEntry,
       "hpnicfCBQoSNatMainNumber": hpnicfCBQoSNatMainNumber,
       "hpnicfCBQoSNatBackupNumber": hpnicfCBQoSNatBackupNumber,
       "hpnicfCBQoSNatServiceClass": hpnicfCBQoSNatServiceClass,
       "hpnicfCBQoSNatRowStatus": hpnicfCBQoSNatRowStatus,
       "hpnicfCBQoSFirewallCfgInfoTable": hpnicfCBQoSFirewallCfgInfoTable,
       "hpnicfCBQoSFirewallCfgInfoEntry": hpnicfCBQoSFirewallCfgInfoEntry,
       "hpnicfCBQoSFirewallAction": hpnicfCBQoSFirewallAction,
       "hpnicfCBQoSFirewallRowStatus": hpnicfCBQoSFirewallRowStatus,
       "hpnicfCBQoSSamplingCfgInfoTable": hpnicfCBQoSSamplingCfgInfoTable,
       "hpnicfCBQoSSamplingCfgInfoEntry": hpnicfCBQoSSamplingCfgInfoEntry,
       "hpnicfCBQoSSamplingNum": hpnicfCBQoSSamplingNum,
       "hpnicfCBQoSSamplingRowStatus": hpnicfCBQoSSamplingRowStatus,
       "hpnicfCBQoSAccountCfgInfoTable": hpnicfCBQoSAccountCfgInfoTable,
       "hpnicfCBQoSAccountCfgInfoEntry": hpnicfCBQoSAccountCfgInfoEntry,
       "hpnicfCBQoSAccounting": hpnicfCBQoSAccounting,
       "hpnicfCBQoSAccountRowStatus": hpnicfCBQoSAccountRowStatus,
       "hpnicfCBQoSAccountingMode": hpnicfCBQoSAccountingMode,
       "hpnicfCBQoSRedirectCfgInfoTable": hpnicfCBQoSRedirectCfgInfoTable,
       "hpnicfCBQoSRedirectCfgInfoEntry": hpnicfCBQoSRedirectCfgInfoEntry,
       "hpnicfCBQoSRedirectType": hpnicfCBQoSRedirectType,
       "hpnicfCBQoSRedirectIfIndex": hpnicfCBQoSRedirectIfIndex,
       "hpnicfCBQoSRedirectIpAddressType": hpnicfCBQoSRedirectIpAddressType,
       "hpnicfCBQoSRedirectIpAddress1": hpnicfCBQoSRedirectIpAddress1,
       "hpnicfCBQoSRedirectIpAddress2": hpnicfCBQoSRedirectIpAddress2,
       "hpnicfCBQoSRedirectRowStatus": hpnicfCBQoSRedirectRowStatus,
       "hpnicfCBQoSRedirectIpv6Interface1": hpnicfCBQoSRedirectIpv6Interface1,
       "hpnicfCBQoSRedirectIpv6Interface2": hpnicfCBQoSRedirectIpv6Interface2,
       "hpnicfCBQoSRedirectIfVlanID": hpnicfCBQoSRedirectIfVlanID,
       "hpnicfCBQoSPriorityMapCfgInfoTable": hpnicfCBQoSPriorityMapCfgInfoTable,
       "hpnicfCBQoSPriorityMapCfgInfoEntry": hpnicfCBQoSPriorityMapCfgInfoEntry,
       "hpnicfCBQoSPriorityMapImportType": hpnicfCBQoSPriorityMapImportType,
       "hpnicfCBQoSPriorityMapExportType": hpnicfCBQoSPriorityMapExportType,
       "hpnicfCBQoSPriorityMapGroupIndex": hpnicfCBQoSPriorityMapGroupIndex,
       "hpnicfCBQoSPriorityMapGroupName": hpnicfCBQoSPriorityMapGroupName,
       "hpnicfCBQoSPriorityMapAuto": hpnicfCBQoSPriorityMapAuto,
       "hpnicfCBQoSPriorityMapRowStatus": hpnicfCBQoSPriorityMapRowStatus,
       "hpnicfCBQoSMirrorCfgInfoTable": hpnicfCBQoSMirrorCfgInfoTable,
       "hpnicfCBQoSMirrorCfgInfoEntry": hpnicfCBQoSMirrorCfgInfoEntry,
       "hpnicfCBQoSMirrorType": hpnicfCBQoSMirrorType,
       "hpnicfCBQoSMirrorIfIndex": hpnicfCBQoSMirrorIfIndex,
       "hpnicfCBQoSMirrorVlanID": hpnicfCBQoSMirrorVlanID,
       "hpnicfCBQoSMirrorRowStatus": hpnicfCBQoSMirrorRowStatus,
       "hpnicfCBQoSNestCfgInfoTable": hpnicfCBQoSNestCfgInfoTable,
       "hpnicfCBQoSNestCfgInfoEntry": hpnicfCBQoSNestCfgInfoEntry,
       "hpnicfCBQoSNestServiceVlanID": hpnicfCBQoSNestServiceVlanID,
       "hpnicfCBQoSNestServiceDot1pValue": hpnicfCBQoSNestServiceDot1pValue,
       "hpnicfCBQoSNestCustomerVlanID": hpnicfCBQoSNestCustomerVlanID,
       "hpnicfCBQoSNestCustomerDot1pValue": hpnicfCBQoSNestCustomerDot1pValue,
       "hpnicfCBQoSNestRowStatus": hpnicfCBQoSNestRowStatus,
       "hpnicfCBQoSNestPolicyCfgInfoTable": hpnicfCBQoSNestPolicyCfgInfoTable,
       "hpnicfCBQoSNestPolicyCfgInfoEntry": hpnicfCBQoSNestPolicyCfgInfoEntry,
       "hpnicfCBQoSNestPolicyName": hpnicfCBQoSNestPolicyName,
       "hpnicfCBQoSNestPolicyRowStatus": hpnicfCBQoSNestPolicyRowStatus,
       "hpnicfCBQoSMirrorIfCfgInfoTable": hpnicfCBQoSMirrorIfCfgInfoTable,
       "hpnicfCBQoSMirrorIfCfgInfoEntry": hpnicfCBQoSMirrorIfCfgInfoEntry,
       "hpnicfCBQoSMirrorIfMainIfIndex": hpnicfCBQoSMirrorIfMainIfIndex,
       "hpnicfCBQoSMirrorIfMainIfStatus": hpnicfCBQoSMirrorIfMainIfStatus,
       "hpnicfCBQoSMirrorIfBackupIfIndex": hpnicfCBQoSMirrorIfBackupIfIndex,
       "hpnicfCBQoSMirrorIfBackupIfStatus": hpnicfCBQoSMirrorIfBackupIfStatus,
       "hpnicfCBQoSMirrorIfRowStatus": hpnicfCBQoSMirrorIfRowStatus,
       "hpnicfCBQoSColoredRemarkCfgTable": hpnicfCBQoSColoredRemarkCfgTable,
       "hpnicfCBQoSColoredRemarkCfgEntry": hpnicfCBQoSColoredRemarkCfgEntry,
       "hpnicfCBQoSColoredRemarkType": hpnicfCBQoSColoredRemarkType,
       "hpnicfCBQoSColoredRemarkColor": hpnicfCBQoSColoredRemarkColor,
       "hpnicfCBQoSColoredRemarkValue": hpnicfCBQoSColoredRemarkValue,
       "hpnicfCBQoSColoredRemarkRowStatus": hpnicfCBQoSColoredRemarkRowStatus,
       "hpnicfCBQoSPrimapCfgInfoTable": hpnicfCBQoSPrimapCfgInfoTable,
       "hpnicfCBQoSPrimapCfgInfoEntry": hpnicfCBQoSPrimapCfgInfoEntry,
       "hpnicfCBQoSPrimapColorType": hpnicfCBQoSPrimapColorType,
       "hpnicfCBQoSPrePriMapTableType": hpnicfCBQoSPrePriMapTableType,
       "hpnicfCBQoSPrimapRowStatus": hpnicfCBQoSPrimapRowStatus,
       "hpnicfCBQoSColorMapDpCfgInfoTable": hpnicfCBQoSColorMapDpCfgInfoTable,
       "hpnicfCBQoSColorMapDpCfgInfoEntry": hpnicfCBQoSColorMapDpCfgInfoEntry,
       "hpnicfCBQoSColorMapDpEnable": hpnicfCBQoSColorMapDpEnable,
       "hpnicfCBQoSColorMapDpRowStatus": hpnicfCBQoSColorMapDpRowStatus,
       "hpnicfCBQoSPolicyObjects": hpnicfCBQoSPolicyObjects,
       "hpnicfCBQoSPolicyIndexNext": hpnicfCBQoSPolicyIndexNext,
       "hpnicfCBQoSPolicyCfgInfoTable": hpnicfCBQoSPolicyCfgInfoTable,
       "hpnicfCBQoSPolicyCfgInfoEntry": hpnicfCBQoSPolicyCfgInfoEntry,
       "hpnicfCBQoSPolicyIndex": hpnicfCBQoSPolicyIndex,
       "hpnicfCBQoSPolicyName": hpnicfCBQoSPolicyName,
       "hpnicfCBQoSPolicyClassCount": hpnicfCBQoSPolicyClassCount,
       "hpnicfCBQoSPolicyConfigMode": hpnicfCBQoSPolicyConfigMode,
       "hpnicfCBQoSPolicyType": hpnicfCBQoSPolicyType,
       "hpnicfCBQoSPolicyClassNextIndex": hpnicfCBQoSPolicyClassNextIndex,
       "hpnicfCBQoSPolicyRowStatus": hpnicfCBQoSPolicyRowStatus,
       "hpnicfCBQoSPolicyClassCfgInfoTable": hpnicfCBQoSPolicyClassCfgInfoTable,
       "hpnicfCBQoSPolicyClassCfgInfoEntry": hpnicfCBQoSPolicyClassCfgInfoEntry,
       "hpnicfCBQoSPolicyClassIndex": hpnicfCBQoSPolicyClassIndex,
       "hpnicfCBQoSPolicyClassClassifierIndex": hpnicfCBQoSPolicyClassClassifierIndex,
       "hpnicfCBQoSPolicyClassClassifierName": hpnicfCBQoSPolicyClassClassifierName,
       "hpnicfCBQoSPolicyClassBehaviorIndex": hpnicfCBQoSPolicyClassBehaviorIndex,
       "hpnicfCBQoSPolicyClassBehaviorName": hpnicfCBQoSPolicyClassBehaviorName,
       "hpnicfCBQoSPolicyClassPrecedence": hpnicfCBQoSPolicyClassPrecedence,
       "hpnicfCBQoSPolicyClassRowStatus": hpnicfCBQoSPolicyClassRowStatus,
       "hpnicfCBQoSPolicyClassMode": hpnicfCBQoSPolicyClassMode,
       "hpnicfCBQoSPolicyClassCfgOrder": hpnicfCBQoSPolicyClassCfgOrder,
       "hpnicfCBQoSApplyPolicyObjects": hpnicfCBQoSApplyPolicyObjects,
       "hpnicfCBQoSIfApplyPolicyTable": hpnicfCBQoSIfApplyPolicyTable,
       "hpnicfCBQoSIfApplyPolicyEntry": hpnicfCBQoSIfApplyPolicyEntry,
       "hpnicfCBQoSIfApplyPolicyIfIndex": hpnicfCBQoSIfApplyPolicyIfIndex,
       "hpnicfCBQoSIfApplyPolicyDirection": hpnicfCBQoSIfApplyPolicyDirection,
       "hpnicfCBQoSIfApplyPolicyName": hpnicfCBQoSIfApplyPolicyName,
       "hpnicfCBQoSIfApplyPolicyEnableDynamic": hpnicfCBQoSIfApplyPolicyEnableDynamic,
       "hpnicfCBQoSIfApplyPolicyRowStatus": hpnicfCBQoSIfApplyPolicyRowStatus,
       "hpnicfCBQoSIfApplyPolicyStatus": hpnicfCBQoSIfApplyPolicyStatus,
       "hpnicfCBQoSAtmPvcApplyPolicyTable": hpnicfCBQoSAtmPvcApplyPolicyTable,
       "hpnicfCBQoSAtmPvcApplyPolicyEntry": hpnicfCBQoSAtmPvcApplyPolicyEntry,
       "hpnicfCBQoSAtmPvcApplyPolicyIfIndex": hpnicfCBQoSAtmPvcApplyPolicyIfIndex,
       "hpnicfCBQoSAtmPvcApplyPolicyVPI": hpnicfCBQoSAtmPvcApplyPolicyVPI,
       "hpnicfCBQoSAtmPvcApplyPolicyVCI": hpnicfCBQoSAtmPvcApplyPolicyVCI,
       "hpnicfCBQoSAtmPvcApplyPolicyDirection": hpnicfCBQoSAtmPvcApplyPolicyDirection,
       "hpnicfCBQoSAtmPvcApplyPolicyName": hpnicfCBQoSAtmPvcApplyPolicyName,
       "hpnicfCBQoSAtmPvcApplyPolicyRowStatus": hpnicfCBQoSAtmPvcApplyPolicyRowStatus,
       "hpnicfCBQoSVlanApplyPolicyTable": hpnicfCBQoSVlanApplyPolicyTable,
       "hpnicfCBQoSVlanApplyPolicyEntry": hpnicfCBQoSVlanApplyPolicyEntry,
       "hpnicfCBQoSVlanApplyPolicyVlanid": hpnicfCBQoSVlanApplyPolicyVlanid,
       "hpnicfCBQoSVlanApplyPolicyDirection": hpnicfCBQoSVlanApplyPolicyDirection,
       "hpnicfCBQoSVlanApplyPolicyName": hpnicfCBQoSVlanApplyPolicyName,
       "hpnicfCBQoSVlanApplyPriority": hpnicfCBQoSVlanApplyPriority,
       "hpnicfCBQoSVlanApplyPolicyRowStatus": hpnicfCBQoSVlanApplyPolicyRowStatus,
       "hpnicfCBQoSVlanApplyPolicyStatus": hpnicfCBQoSVlanApplyPolicyStatus,
       "hpnicfCBQoSFrClassApplyPolicyTable": hpnicfCBQoSFrClassApplyPolicyTable,
       "hpnicfCBQoSFrClassApplyPolicyEntry": hpnicfCBQoSFrClassApplyPolicyEntry,
       "hpnicfCBQoSFrClassApplyPolicyFrClassName": hpnicfCBQoSFrClassApplyPolicyFrClassName,
       "hpnicfCBQoSFrClassApplyPolicyDirection": hpnicfCBQoSFrClassApplyPolicyDirection,
       "hpnicfCBQoSFrClassApplyPolicyName": hpnicfCBQoSFrClassApplyPolicyName,
       "hpnicfCBQoSFrClassApplyPolicyRowStatus": hpnicfCBQoSFrClassApplyPolicyRowStatus,
       "hpnicfCBQoSFrPvcApplyPolicyTable": hpnicfCBQoSFrPvcApplyPolicyTable,
       "hpnicfCBQoSFrPvcApplyPolicyEntry": hpnicfCBQoSFrPvcApplyPolicyEntry,
       "hpnicfCBQoSFrPvcApplyPolicyIfIndex": hpnicfCBQoSFrPvcApplyPolicyIfIndex,
       "hpnicfCBQoSFrPvcApplyPolicyDlciNum": hpnicfCBQoSFrPvcApplyPolicyDlciNum,
       "hpnicfCBQoSFrPvcApplyPolicyDirection": hpnicfCBQoSFrPvcApplyPolicyDirection,
       "hpnicfCBQoSFrPvcApplyPolicyName": hpnicfCBQoSFrPvcApplyPolicyName,
       "hpnicfCBQoSFrPvcApplyPolicyRowStatus": hpnicfCBQoSFrPvcApplyPolicyRowStatus,
       "hpnicfCBQoSGlobalApplyTable": hpnicfCBQoSGlobalApplyTable,
       "hpnicfCBQoSGlobalApplyEntry": hpnicfCBQoSGlobalApplyEntry,
       "hpnicfCBQoSGlobalApplyDirection": hpnicfCBQoSGlobalApplyDirection,
       "hpnicfCBQoSGlobalApplyName": hpnicfCBQoSGlobalApplyName,
       "hpnicfCBQoSGlobalApplyRowStatus": hpnicfCBQoSGlobalApplyRowStatus,
       "hpnicfCBQoSGlobalApplyStatus": hpnicfCBQoSGlobalApplyStatus,
       "hpnicfCBQoSCpApplyPolicyTable": hpnicfCBQoSCpApplyPolicyTable,
       "hpnicfCBQoSCpApplyPolicyEntry": hpnicfCBQoSCpApplyPolicyEntry,
       "hpnicfCBQoSCpApplyPolicyChassis": hpnicfCBQoSCpApplyPolicyChassis,
       "hpnicfCBQoSCpApplyPolicySlot": hpnicfCBQoSCpApplyPolicySlot,
       "hpnicfCBQoSCpApplyPolicyDirection": hpnicfCBQoSCpApplyPolicyDirection,
       "hpnicfCBQoSCpApplyPolicyName": hpnicfCBQoSCpApplyPolicyName,
       "hpnicfCBQoSCpApplyPolicyStatus": hpnicfCBQoSCpApplyPolicyStatus,
       "hpnicfCBQoSCpApplyRowStatus": hpnicfCBQoSCpApplyRowStatus,
       "hpnicfCBQoSApplyPolicyStaticsObjects": hpnicfCBQoSApplyPolicyStaticsObjects,
       "hpnicfCBQoSIfStaticsObjects": hpnicfCBQoSIfStaticsObjects,
       "hpnicfCBQoSIfCbqRunInfoTable": hpnicfCBQoSIfCbqRunInfoTable,
       "hpnicfCBQoSIfCbqRunInfoEntry": hpnicfCBQoSIfCbqRunInfoEntry,
       "hpnicfCBQoSIfCbqQueueSize": hpnicfCBQoSIfCbqQueueSize,
       "hpnicfCBQoSIfCbqDiscard": hpnicfCBQoSIfCbqDiscard,
       "hpnicfCBQoSIfCbqEfQueueSize": hpnicfCBQoSIfCbqEfQueueSize,
       "hpnicfCBQoSIfCbqAfQueueSize": hpnicfCBQoSIfCbqAfQueueSize,
       "hpnicfCBQoSIfCbqBeQueueSize": hpnicfCBQoSIfCbqBeQueueSize,
       "hpnicfCBQoSIfCbqBeActiveQueueNum": hpnicfCBQoSIfCbqBeActiveQueueNum,
       "hpnicfCBQoSIfCbqBeMaxActiveQueueNum": hpnicfCBQoSIfCbqBeMaxActiveQueueNum,
       "hpnicfCBQoSIfCbqBeTotalQueueNum": hpnicfCBQoSIfCbqBeTotalQueueNum,
       "hpnicfCBQoSIfCbqAfAllocatedQueueNum": hpnicfCBQoSIfCbqAfAllocatedQueueNum,
       "hpnicfCBQoSIfClassMatchRunInfoTable": hpnicfCBQoSIfClassMatchRunInfoTable,
       "hpnicfCBQoSIfClassMatchRunInfoEntry": hpnicfCBQoSIfClassMatchRunInfoEntry,
       "hpnicfCBQoSIfClassMatchedPackets": hpnicfCBQoSIfClassMatchedPackets,
       "hpnicfCBQoSIfClassMatchedBytes": hpnicfCBQoSIfClassMatchedBytes,
       "hpnicfCBQoSIfClassAverageRate": hpnicfCBQoSIfClassAverageRate,
       "hpnicfCBQoSIfCarRunInfoTable": hpnicfCBQoSIfCarRunInfoTable,
       "hpnicfCBQoSIfCarRunInfoEntry": hpnicfCBQoSIfCarRunInfoEntry,
       "hpnicfCBQoSIfCarGreenPackets": hpnicfCBQoSIfCarGreenPackets,
       "hpnicfCBQoSIfCarGreenBytes": hpnicfCBQoSIfCarGreenBytes,
       "hpnicfCBQoSIfCarRedPackets": hpnicfCBQoSIfCarRedPackets,
       "hpnicfCBQoSIfCarRedBytes": hpnicfCBQoSIfCarRedBytes,
       "hpnicfCBQoSIfCarYellowPackets": hpnicfCBQoSIfCarYellowPackets,
       "hpnicfCBQoSIfCarYellowBytes": hpnicfCBQoSIfCarYellowBytes,
       "hpnicfCBQoSIfGtsRunInfoTable": hpnicfCBQoSIfGtsRunInfoTable,
       "hpnicfCBQoSIfGtsRunInfoEntry": hpnicfCBQoSIfGtsRunInfoEntry,
       "hpnicfCBQoSIfGtsPassedPackets": hpnicfCBQoSIfGtsPassedPackets,
       "hpnicfCBQoSIfGtsPassedBytes": hpnicfCBQoSIfGtsPassedBytes,
       "hpnicfCBQoSIfGtsDiscardedPackets": hpnicfCBQoSIfGtsDiscardedPackets,
       "hpnicfCBQoSIfGtsDiscardedBytes": hpnicfCBQoSIfGtsDiscardedBytes,
       "hpnicfCBQoSIfGtsDelayedPackets": hpnicfCBQoSIfGtsDelayedPackets,
       "hpnicfCBQoSIfGtsDelayedBytes": hpnicfCBQoSIfGtsDelayedBytes,
       "hpnicfCBQoSIfGtsQueueSize": hpnicfCBQoSIfGtsQueueSize,
       "hpnicfCBQoSIfRemarkRunInfoTable": hpnicfCBQoSIfRemarkRunInfoTable,
       "hpnicfCBQoSIfRemarkRunInfoEntry": hpnicfCBQoSIfRemarkRunInfoEntry,
       "hpnicfCBQoSIfRemarkedPackets": hpnicfCBQoSIfRemarkedPackets,
       "hpnicfCBQoSIfQueueRunInfoTable": hpnicfCBQoSIfQueueRunInfoTable,
       "hpnicfCBQoSIfQueueRunInfoEntry": hpnicfCBQoSIfQueueRunInfoEntry,
       "hpnicfCBQoSIfQueueMatchedPackets": hpnicfCBQoSIfQueueMatchedPackets,
       "hpnicfCBQoSIfQueueMatchedBytes": hpnicfCBQoSIfQueueMatchedBytes,
       "hpnicfCBQoSIfQueueEnqueuedPackets": hpnicfCBQoSIfQueueEnqueuedPackets,
       "hpnicfCBQoSIfQueueEnqueuedBytes": hpnicfCBQoSIfQueueEnqueuedBytes,
       "hpnicfCBQoSIfQueueDiscardedPackets": hpnicfCBQoSIfQueueDiscardedPackets,
       "hpnicfCBQoSIfQueueDiscardedBytes": hpnicfCBQoSIfQueueDiscardedBytes,
       "hpnicfCBQoSIfWredRunInfoTable": hpnicfCBQoSIfWredRunInfoTable,
       "hpnicfCBQoSIfWredRunInfoEntry": hpnicfCBQoSIfWredRunInfoEntry,
       "hpnicfCBQoSIfWredRandomDiscardedPackets": hpnicfCBQoSIfWredRandomDiscardedPackets,
       "hpnicfCBQoSIfWredTailDiscardedPackets": hpnicfCBQoSIfWredTailDiscardedPackets,
       "hpnicfCBQoSIfAccountingRunInfoTable": hpnicfCBQoSIfAccountingRunInfoTable,
       "hpnicfCBQoSIfAccountingRunInfoEntry": hpnicfCBQoSIfAccountingRunInfoEntry,
       "hpnicfCBQoSIfAccountingPackets": hpnicfCBQoSIfAccountingPackets,
       "hpnicfCBQoSIfAccountingBytes": hpnicfCBQoSIfAccountingBytes,
       "hpnicfCBQoSAtmPvcStaticsObjects": hpnicfCBQoSAtmPvcStaticsObjects,
       "hpnicfCBQoSAtmPvcCbqRunInfoTable": hpnicfCBQoSAtmPvcCbqRunInfoTable,
       "hpnicfCBQoSAtmPvcCbqRunInfoEntry": hpnicfCBQoSAtmPvcCbqRunInfoEntry,
       "hpnicfCBQoSAtmPvcCbqQueueSize": hpnicfCBQoSAtmPvcCbqQueueSize,
       "hpnicfCBQoSAtmPvcCbqDiscard": hpnicfCBQoSAtmPvcCbqDiscard,
       "hpnicfCBQoSAtmPvcCbqEfQueueSize": hpnicfCBQoSAtmPvcCbqEfQueueSize,
       "hpnicfCBQoSAtmPvcCbqAfQueueSize": hpnicfCBQoSAtmPvcCbqAfQueueSize,
       "hpnicfCBQoSAtmPvcCbqBeQueueSize": hpnicfCBQoSAtmPvcCbqBeQueueSize,
       "hpnicfCBQoSAtmPvcCbqBeActiveQueueNum": hpnicfCBQoSAtmPvcCbqBeActiveQueueNum,
       "hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum": hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum,
       "hpnicfCBQoSAtmPvcCbqBeTotalQueueNum": hpnicfCBQoSAtmPvcCbqBeTotalQueueNum,
       "hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum": hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum,
       "hpnicfCBQoSAtmPvcClassMatchRunInfoTable": hpnicfCBQoSAtmPvcClassMatchRunInfoTable,
       "hpnicfCBQoSAtmPvcClassMatchRunInfoEntry": hpnicfCBQoSAtmPvcClassMatchRunInfoEntry,
       "hpnicfCBQoSAtmPvcClassMatchPackets": hpnicfCBQoSAtmPvcClassMatchPackets,
       "hpnicfCBQoSAtmPvcClassMatchBytes": hpnicfCBQoSAtmPvcClassMatchBytes,
       "hpnicfCBQoSAtmPvcClassAverageRate": hpnicfCBQoSAtmPvcClassAverageRate,
       "hpnicfCBQoSAtmPvcCarRunInfoTable": hpnicfCBQoSAtmPvcCarRunInfoTable,
       "hpnicfCBQoSAtmPvcCarRunInfoEntry": hpnicfCBQoSAtmPvcCarRunInfoEntry,
       "hpnicfCBQoSAtmPvcCarConformPackets": hpnicfCBQoSAtmPvcCarConformPackets,
       "hpnicfCBQoSAtmPvcCarConformBytes": hpnicfCBQoSAtmPvcCarConformBytes,
       "hpnicfCBQoSAtmPvcCarExceedPackets": hpnicfCBQoSAtmPvcCarExceedPackets,
       "hpnicfCBQoSAtmPvcCarExceedBytes": hpnicfCBQoSAtmPvcCarExceedBytes,
       "hpnicfCBQoSAtmPvcGtsRunInfoTable": hpnicfCBQoSAtmPvcGtsRunInfoTable,
       "hpnicfCBQoSAtmPvcGtsRunInfoEntry": hpnicfCBQoSAtmPvcGtsRunInfoEntry,
       "hpnicfCBQoSAtmPvcGtsPassedPackets": hpnicfCBQoSAtmPvcGtsPassedPackets,
       "hpnicfCBQoSAtmPvcGtsPassedBytes": hpnicfCBQoSAtmPvcGtsPassedBytes,
       "hpnicfCBQoSAtmPvcGtsDiscardedPackets": hpnicfCBQoSAtmPvcGtsDiscardedPackets,
       "hpnicfCBQoSAtmPvcGtsDiscardedBytes": hpnicfCBQoSAtmPvcGtsDiscardedBytes,
       "hpnicfCBQoSAtmPvcGtsDelayedPackets": hpnicfCBQoSAtmPvcGtsDelayedPackets,
       "hpnicfCBQoSAtmPvcGtsDelayedBytes": hpnicfCBQoSAtmPvcGtsDelayedBytes,
       "hpnicfCBQoSAtmPvcGtsQueueSize": hpnicfCBQoSAtmPvcGtsQueueSize,
       "hpnicfCBQoSAtmPvcRemarkRunInfoTable": hpnicfCBQoSAtmPvcRemarkRunInfoTable,
       "hpnicfCBQoSAtmPvcRemarkRunInfoEntry": hpnicfCBQoSAtmPvcRemarkRunInfoEntry,
       "hpnicfCBQoSAtmPvcRemarkedPackets": hpnicfCBQoSAtmPvcRemarkedPackets,
       "hpnicfCBQoSAtmPvcQueueRunInfoTable": hpnicfCBQoSAtmPvcQueueRunInfoTable,
       "hpnicfCBQoSAtmPvcQueueRunInfoEntry": hpnicfCBQoSAtmPvcQueueRunInfoEntry,
       "hpnicfCBQoSAtmPvcQueueMatchedPackets": hpnicfCBQoSAtmPvcQueueMatchedPackets,
       "hpnicfCBQoSAtmPvcQueueMatchedBytes": hpnicfCBQoSAtmPvcQueueMatchedBytes,
       "hpnicfCBQoSAtmPvcQueueEnqueuedPackets": hpnicfCBQoSAtmPvcQueueEnqueuedPackets,
       "hpnicfCBQoSAtmPvcQueueEnqueuedBytes": hpnicfCBQoSAtmPvcQueueEnqueuedBytes,
       "hpnicfCBQoSAtmPvcQueueDiscardedPackets": hpnicfCBQoSAtmPvcQueueDiscardedPackets,
       "hpnicfCBQoSAtmPvcQueueDiscardedBytes": hpnicfCBQoSAtmPvcQueueDiscardedBytes,
       "hpnicfCBQoSAtmPvcWredRunInfoTable": hpnicfCBQoSAtmPvcWredRunInfoTable,
       "hpnicfCBQoSAtmPvcWredRunInfoEntry": hpnicfCBQoSAtmPvcWredRunInfoEntry,
       "hpnicfCBQoSAtmPvcWredRandomDiscardedPackets": hpnicfCBQoSAtmPvcWredRandomDiscardedPackets,
       "hpnicfCBQoSAtmPvcWredTailDiscardedPackets": hpnicfCBQoSAtmPvcWredTailDiscardedPackets,
       "hpnicfCBQoSAtmPvcAccountingRunInfoTable": hpnicfCBQoSAtmPvcAccountingRunInfoTable,
       "hpnicfCBQoSAtmPvcAccountingRunInfoEntry": hpnicfCBQoSAtmPvcAccountingRunInfoEntry,
       "hpnicfCBQoSAtmPvcAccountingPackets": hpnicfCBQoSAtmPvcAccountingPackets,
       "hpnicfCBQoSAtmPvcAccountingBytes": hpnicfCBQoSAtmPvcAccountingBytes,
       "hpnicfCBQoSFrPvcStaticsObjects": hpnicfCBQoSFrPvcStaticsObjects,
       "hpnicfCBQoSFrPvcCbqRunInfoTable": hpnicfCBQoSFrPvcCbqRunInfoTable,
       "hpnicfCBQoSFrPvcCbqRunInfoEntry": hpnicfCBQoSFrPvcCbqRunInfoEntry,
       "hpnicfCBQoSFrPvcCbqQueueSize": hpnicfCBQoSFrPvcCbqQueueSize,
       "hpnicfCBQoSFrPvcCbqDiscard": hpnicfCBQoSFrPvcCbqDiscard,
       "hpnicfCBQoSFrPvcCbqEfQueueSize": hpnicfCBQoSFrPvcCbqEfQueueSize,
       "hpnicfCBQoSFrPvcCbqAfQueueSize": hpnicfCBQoSFrPvcCbqAfQueueSize,
       "hpnicfCBQoSFrPvcCbqBeQueueSize": hpnicfCBQoSFrPvcCbqBeQueueSize,
       "hpnicfCBQoSFrPvcCbqBeActiveQueueNum": hpnicfCBQoSFrPvcCbqBeActiveQueueNum,
       "hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum": hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum,
       "hpnicfCBQoSFrPvcCbqBeTotalQueueNum": hpnicfCBQoSFrPvcCbqBeTotalQueueNum,
       "hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum": hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum,
       "hpnicfCBQoSFrPvcClassMatchRunInfoTable": hpnicfCBQoSFrPvcClassMatchRunInfoTable,
       "hpnicfCBQoSFrPvcClassMatchRunInfoEntry": hpnicfCBQoSFrPvcClassMatchRunInfoEntry,
       "hpnicfCBQoSFrPvcClassMatchedPackets": hpnicfCBQoSFrPvcClassMatchedPackets,
       "hpnicfCBQoSFrPvcClassMatchedBytes": hpnicfCBQoSFrPvcClassMatchedBytes,
       "hpnicfCBQoSFrPvcClassAverageRate": hpnicfCBQoSFrPvcClassAverageRate,
       "hpnicfCBQoSFrPvcCarRunInfoTable": hpnicfCBQoSFrPvcCarRunInfoTable,
       "hpnicfCBQoSFrPvcCarRunInfoEntry": hpnicfCBQoSFrPvcCarRunInfoEntry,
       "hpnicfCBQoSFrPvcCarConformPackets": hpnicfCBQoSFrPvcCarConformPackets,
       "hpnicfCBQoSFrPvcCarConformBytes": hpnicfCBQoSFrPvcCarConformBytes,
       "hpnicfCBQoSFrPvcCarExceedPackets": hpnicfCBQoSFrPvcCarExceedPackets,
       "hpnicfCBQoSFrPvcCarExceedBytes": hpnicfCBQoSFrPvcCarExceedBytes,
       "hpnicfCBQoSFrPvcGtsRunInfoTable": hpnicfCBQoSFrPvcGtsRunInfoTable,
       "hpnicfCBQoSFrPvcGtsRunInfoEntry": hpnicfCBQoSFrPvcGtsRunInfoEntry,
       "hpnicfCBQoSFrPvcGtsPassedPackets": hpnicfCBQoSFrPvcGtsPassedPackets,
       "hpnicfCBQoSFrPvcGtsPassedBytes": hpnicfCBQoSFrPvcGtsPassedBytes,
       "hpnicfCBQoSFrPvcGtsDiscardedPackets": hpnicfCBQoSFrPvcGtsDiscardedPackets,
       "hpnicfCBQoSFrPvcGtsDiscardedBytes": hpnicfCBQoSFrPvcGtsDiscardedBytes,
       "hpnicfCBQoSFrPvcGtsDelayedPackets": hpnicfCBQoSFrPvcGtsDelayedPackets,
       "hpnicfCBQoSFrPvcGtsDelayedBytes": hpnicfCBQoSFrPvcGtsDelayedBytes,
       "hpnicfCBQoSFrPvcGtsQueueSize": hpnicfCBQoSFrPvcGtsQueueSize,
       "hpnicfCBQoSFrPvcRemarkRunInfoTable": hpnicfCBQoSFrPvcRemarkRunInfoTable,
       "hpnicfCBQoSFrPvcRemarkRunInfoEntry": hpnicfCBQoSFrPvcRemarkRunInfoEntry,
       "hpnicfCBQoSFrPvcRemarkedPackets": hpnicfCBQoSFrPvcRemarkedPackets,
       "hpnicfCBQoSFrPvcQueueRunInfoTable": hpnicfCBQoSFrPvcQueueRunInfoTable,
       "hpnicfCBQoSFrPvcQueueRunInfoEntry": hpnicfCBQoSFrPvcQueueRunInfoEntry,
       "hpnicfCBQoSFrPvcQueueMatchedPackets": hpnicfCBQoSFrPvcQueueMatchedPackets,
       "hpnicfCBQoSFrPvcQueueMatchedBytes": hpnicfCBQoSFrPvcQueueMatchedBytes,
       "hpnicfCBQoSFrPvcQueueEnqueuedPackets": hpnicfCBQoSFrPvcQueueEnqueuedPackets,
       "hpnicfCBQoSFrPvcQueueEnqueuedBytes": hpnicfCBQoSFrPvcQueueEnqueuedBytes,
       "hpnicfCBQoSFrPvcQueueDiscardedPackets": hpnicfCBQoSFrPvcQueueDiscardedPackets,
       "hpnicfCBQoSFrPvcQueueDiscardedBytes": hpnicfCBQoSFrPvcQueueDiscardedBytes,
       "hpnicfCBQoSFrPvcWredRunInfoTable": hpnicfCBQoSFrPvcWredRunInfoTable,
       "hpnicfCBQoSFrPvcWredRunInfoEntry": hpnicfCBQoSFrPvcWredRunInfoEntry,
       "hpnicfCBQoSFrPvcWredRandomDiscardedPackets": hpnicfCBQoSFrPvcWredRandomDiscardedPackets,
       "hpnicfCBQoSFrPvcWredTailDiscardedPackets": hpnicfCBQoSFrPvcWredTailDiscardedPackets,
       "hpnicfCBQoSFrPvcAccountingRunInfoTable": hpnicfCBQoSFrPvcAccountingRunInfoTable,
       "hpnicfCBQoSFrPvcAccountingRunInfoEntry": hpnicfCBQoSFrPvcAccountingRunInfoEntry,
       "hpnicfCBQoSFrPvcAccountingPackets": hpnicfCBQoSFrPvcAccountingPackets,
       "hpnicfCBQoSFrPvcAccountingBytes": hpnicfCBQoSFrPvcAccountingBytes,
       "hpnicfCBQoSVlanStaticsObjects": hpnicfCBQoSVlanStaticsObjects,
       "hpnicfCBQoSVlanClassMatchRunInfoTable": hpnicfCBQoSVlanClassMatchRunInfoTable,
       "hpnicfCBQoSVlanClassMatchRunInfoEntry": hpnicfCBQoSVlanClassMatchRunInfoEntry,
       "hpnicfCBQoSVlanClassMatchedPackets": hpnicfCBQoSVlanClassMatchedPackets,
       "hpnicfCBQoSVlanAccountingRunInfoTable": hpnicfCBQoSVlanAccountingRunInfoTable,
       "hpnicfCBQoSVlanAccountingRunInfoEntry": hpnicfCBQoSVlanAccountingRunInfoEntry,
       "hpnicfCBQoSVlanAccountingPackets": hpnicfCBQoSVlanAccountingPackets,
       "hpnicfCBQoSVlanAccountingBytes": hpnicfCBQoSVlanAccountingBytes,
       "hpnicfCBQoSApplyPolicyIndexObjects": hpnicfCBQoSApplyPolicyIndexObjects,
       "hpnicfCBQoSApplyObjectTable": hpnicfCBQoSApplyObjectTable,
       "hpnicfCBQoSApplyObjectEntry": hpnicfCBQoSApplyObjectEntry,
       "hpnicfCBQoSApplyObjectIndex": hpnicfCBQoSApplyObjectIndex,
       "hpnicfCBQoSApplyObjectType": hpnicfCBQoSApplyObjectType,
       "hpnicfCBQoSApplyObjectDirection": hpnicfCBQoSApplyObjectDirection,
       "hpnicfCBQoSApplyObjectMainSite": hpnicfCBQoSApplyObjectMainSite,
       "hpnicfCBQoSApplyObjectSubChannel": hpnicfCBQoSApplyObjectSubChannel,
       "hpnicfCBQoSApplyObjectSubClass": hpnicfCBQoSApplyObjectSubClass,
       "hpnicfCBQoSApplyObjectSubClassSec": hpnicfCBQoSApplyObjectSubClassSec,
       "hpnicfCBQoSIntApplyObjectTable": hpnicfCBQoSIntApplyObjectTable,
       "hpnicfCBQoSIntApplyObjectEntry": hpnicfCBQoSIntApplyObjectEntry,
       "hpnicfCBQoSIntApplyObjectIfIndex": hpnicfCBQoSIntApplyObjectIfIndex,
       "hpnicfCBQoSIntApplyObjectIndex": hpnicfCBQoSIntApplyObjectIndex,
       "hpnicfCBQoSVlanApplyObjectTable": hpnicfCBQoSVlanApplyObjectTable,
       "hpnicfCBQoSVlanApplyObjectEntry": hpnicfCBQoSVlanApplyObjectEntry,
       "hpnicfCBQoSVlanApplyObjectVlanID": hpnicfCBQoSVlanApplyObjectVlanID,
       "hpnicfCBQoSVlanApplyObjectIndex": hpnicfCBQoSVlanApplyObjectIndex,
       "hpnicfCBQoSPvcApplyObjectTable": hpnicfCBQoSPvcApplyObjectTable,
       "hpnicfCBQoSPvcApplyObjectEntry": hpnicfCBQoSPvcApplyObjectEntry,
       "hpnicfCBQoSPvcApplyObjectIfIndex": hpnicfCBQoSPvcApplyObjectIfIndex,
       "hpnicfCBQoSPvcApplyObjectPvcID": hpnicfCBQoSPvcApplyObjectPvcID,
       "hpnicfCBQoSPvcApplyObjectIndex": hpnicfCBQoSPvcApplyObjectIndex,
       "hpnicfCBQoSNestPolicyApplyObjectTable": hpnicfCBQoSNestPolicyApplyObjectTable,
       "hpnicfCBQoSNestPolicyApplyObjectEntry": hpnicfCBQoSNestPolicyApplyObjectEntry,
       "hpnicfCBQoSNestPolicyClassIndex": hpnicfCBQoSNestPolicyClassIndex,
       "hpnicfCBQoSNestPolicyApplyObjectIndex": hpnicfCBQoSNestPolicyApplyObjectIndex,
       "hpnicfCBQoSCpApplyObjectTable": hpnicfCBQoSCpApplyObjectTable,
       "hpnicfCBQoSCpApplyObjectEntry": hpnicfCBQoSCpApplyObjectEntry,
       "hpnicfCBQoSCpApplyObjectChassis": hpnicfCBQoSCpApplyObjectChassis,
       "hpnicfCBQoSCpApplyObjectSlot": hpnicfCBQoSCpApplyObjectSlot,
       "hpnicfCBQoSCpApplyObjectIndex": hpnicfCBQoSCpApplyObjectIndex,
       "hpnicfCBQoSStaticsObjects": hpnicfCBQoSStaticsObjects,
       "hpnicfCBQoSCbqRunInfoTable": hpnicfCBQoSCbqRunInfoTable,
       "hpnicfCBQoSCbqRunInfoEntry": hpnicfCBQoSCbqRunInfoEntry,
       "hpnicfCBQoSCbqQueueSize": hpnicfCBQoSCbqQueueSize,
       "hpnicfCBQoSCbqDiscard": hpnicfCBQoSCbqDiscard,
       "hpnicfCBQoSCbqEfQueueSize": hpnicfCBQoSCbqEfQueueSize,
       "hpnicfCBQoSCbqAfQueueSize": hpnicfCBQoSCbqAfQueueSize,
       "hpnicfCBQoSCbqBeQueueSize": hpnicfCBQoSCbqBeQueueSize,
       "hpnicfCBQoSCbqBeActiveQueueNum": hpnicfCBQoSCbqBeActiveQueueNum,
       "hpnicfCBQoSCbqBeMaxActiveQueueNum": hpnicfCBQoSCbqBeMaxActiveQueueNum,
       "hpnicfCBQoSCbqBeTotalQueueNum": hpnicfCBQoSCbqBeTotalQueueNum,
       "hpnicfCBQoSCbqAfAllocatedQueueNum": hpnicfCBQoSCbqAfAllocatedQueueNum,
       "hpnicfCBQoSClassMatchRunInfoTable": hpnicfCBQoSClassMatchRunInfoTable,
       "hpnicfCBQoSClassMatchRunInfoEntry": hpnicfCBQoSClassMatchRunInfoEntry,
       "hpnicfCBQoSClassMatchedPackets": hpnicfCBQoSClassMatchedPackets,
       "hpnicfCBQoSClassMatchedBytes": hpnicfCBQoSClassMatchedBytes,
       "hpnicfCBQoSClassFwdPktpps": hpnicfCBQoSClassFwdPktpps,
       "hpnicfCBQoSClassFwdPktbps": hpnicfCBQoSClassFwdPktbps,
       "hpnicfCBQoSClassDropPktpps": hpnicfCBQoSClassDropPktpps,
       "hpnicfCBQoSClassDropPktbps": hpnicfCBQoSClassDropPktbps,
       "hpnicfCBQoSClassFlowStatInterval": hpnicfCBQoSClassFlowStatInterval,
       "hpnicfCBQoSClassBehaviorStatus": hpnicfCBQoSClassBehaviorStatus,
       "hpnicfCBQoSCarRunInfoTable": hpnicfCBQoSCarRunInfoTable,
       "hpnicfCBQoSCarRunInfoEntry": hpnicfCBQoSCarRunInfoEntry,
       "hpnicfCBQoSCarGreenPackets": hpnicfCBQoSCarGreenPackets,
       "hpnicfCBQoSCarGreenBytes": hpnicfCBQoSCarGreenBytes,
       "hpnicfCBQoSCarRedPackets": hpnicfCBQoSCarRedPackets,
       "hpnicfCBQoSCarRedBytes": hpnicfCBQoSCarRedBytes,
       "hpnicfCBQoSCarYellowPackets": hpnicfCBQoSCarYellowPackets,
       "hpnicfCBQoSCarYellowBytes": hpnicfCBQoSCarYellowBytes,
       "hpnicfCBQoSGtsRunInfoTable": hpnicfCBQoSGtsRunInfoTable,
       "hpnicfCBQoSGtsRunInfoEntry": hpnicfCBQoSGtsRunInfoEntry,
       "hpnicfCBQoSGtsPassedPackets": hpnicfCBQoSGtsPassedPackets,
       "hpnicfCBQoSGtsPassedBytes": hpnicfCBQoSGtsPassedBytes,
       "hpnicfCBQoSGtsDiscardedPackets": hpnicfCBQoSGtsDiscardedPackets,
       "hpnicfCBQoSGtsDiscardedBytes": hpnicfCBQoSGtsDiscardedBytes,
       "hpnicfCBQoSGtsDelayedPackets": hpnicfCBQoSGtsDelayedPackets,
       "hpnicfCBQoSGtsDelayedBytes": hpnicfCBQoSGtsDelayedBytes,
       "hpnicfCBQoSGtsQueueSize": hpnicfCBQoSGtsQueueSize,
       "hpnicfCBQoSRemarkRunInfoTable": hpnicfCBQoSRemarkRunInfoTable,
       "hpnicfCBQoSRemarkRunInfoEntry": hpnicfCBQoSRemarkRunInfoEntry,
       "hpnicfCBQoSRemarkedPackets": hpnicfCBQoSRemarkedPackets,
       "hpnicfCBQoSQueueRunInfoTable": hpnicfCBQoSQueueRunInfoTable,
       "hpnicfCBQoSQueueRunInfoEntry": hpnicfCBQoSQueueRunInfoEntry,
       "hpnicfCBQoSQueueMatchedPackets": hpnicfCBQoSQueueMatchedPackets,
       "hpnicfCBQoSQueueMatchedBytes": hpnicfCBQoSQueueMatchedBytes,
       "hpnicfCBQoSQueueEnqueuedPackets": hpnicfCBQoSQueueEnqueuedPackets,
       "hpnicfCBQoSQueueEnqueuedBytes": hpnicfCBQoSQueueEnqueuedBytes,
       "hpnicfCBQoSQueueDiscardedPackets": hpnicfCBQoSQueueDiscardedPackets,
       "hpnicfCBQoSQueueDiscardedBytes": hpnicfCBQoSQueueDiscardedBytes,
       "hpnicfCBQoSWredRunInfoTable": hpnicfCBQoSWredRunInfoTable,
       "hpnicfCBQoSWredRunInfoEntry": hpnicfCBQoSWredRunInfoEntry,
       "hpnicfCBQoSWredRandomDiscardedPackets": hpnicfCBQoSWredRandomDiscardedPackets,
       "hpnicfCBQoSWredTailDiscardedPackets": hpnicfCBQoSWredTailDiscardedPackets,
       "hpnicfCBQoSAccountingRunInfoTable": hpnicfCBQoSAccountingRunInfoTable,
       "hpnicfCBQoSAccountingRunInfoEntry": hpnicfCBQoSAccountingRunInfoEntry,
       "hpnicfCBQoSAccountingPackets": hpnicfCBQoSAccountingPackets,
       "hpnicfCBQoSAccountingBytes": hpnicfCBQoSAccountingBytes,
       "hpnicfCBQoSApplyingStatusObjects": hpnicfCBQoSApplyingStatusObjects,
       "hpnicfCBQoSApplyingStatus": hpnicfCBQoSApplyingStatus,
       "hpnicfCBQoSNotifications": hpnicfCBQoSNotifications,
       "hpnicfCBQoSNotificationsPrefix": hpnicfCBQoSNotificationsPrefix,
       "hpnicfCBQoSIfPolicyChanged": hpnicfCBQoSIfPolicyChanged,
       "hpnicfCBQoSVlanPolicyChanged": hpnicfCBQoSVlanPolicyChanged}
)
