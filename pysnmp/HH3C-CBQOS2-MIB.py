# SNMP MIB module (HH3C-CBQOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-CBQOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:34 2024
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

hh3cCBQos2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2)
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

_Hh3cQos2_ObjectIdentity = ObjectIdentity
hh3cQos2 = _Hh3cQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65)
)
_Hh3cCBQoSObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSObjects = _Hh3cCBQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1)
)
_Hh3cCBQoSClassifierObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSClassifierObjects = _Hh3cCBQoSClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1)
)
_Hh3cCBQoSClassifierIndexNext_Type = Integer32
_Hh3cCBQoSClassifierIndexNext_Object = MibScalar
hh3cCBQoSClassifierIndexNext = _Hh3cCBQoSClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 1),
    _Hh3cCBQoSClassifierIndexNext_Type()
)
hh3cCBQoSClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierIndexNext.setStatus("current")
_Hh3cCBQoSClassifierCfgInfoTable_Object = MibTable
hh3cCBQoSClassifierCfgInfoTable = _Hh3cCBQoSClassifierCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierCfgInfoTable.setStatus("current")
_Hh3cCBQoSClassifierCfgInfoEntry_Object = MibTableRow
hh3cCBQoSClassifierCfgInfoEntry = _Hh3cCBQoSClassifierCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1)
)
hh3cCBQoSClassifierCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSClassifierIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierCfgInfoEntry.setStatus("current")
_Hh3cCBQoSClassifierIndex_Type = Integer32
_Hh3cCBQoSClassifierIndex_Object = MibTableColumn
hh3cCBQoSClassifierIndex = _Hh3cCBQoSClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 1),
    _Hh3cCBQoSClassifierIndex_Type()
)
hh3cCBQoSClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierIndex.setStatus("current")


class _Hh3cCBQoSClassifierName_Type(OctetString):
    """Custom type hh3cCBQoSClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSClassifierName_Type.__name__ = "OctetString"
_Hh3cCBQoSClassifierName_Object = MibTableColumn
hh3cCBQoSClassifierName = _Hh3cCBQoSClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 2),
    _Hh3cCBQoSClassifierName_Type()
)
hh3cCBQoSClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierName.setStatus("current")
_Hh3cCBQoSClassifierRuleCount_Type = Integer32
_Hh3cCBQoSClassifierRuleCount_Object = MibTableColumn
hh3cCBQoSClassifierRuleCount = _Hh3cCBQoSClassifierRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 3),
    _Hh3cCBQoSClassifierRuleCount_Type()
)
hh3cCBQoSClassifierRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierRuleCount.setStatus("current")


class _Hh3cCBQoSClassifierOperator_Type(Integer32):
    """Custom type hh3cCBQoSClassifierOperator based on Integer32"""
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


_Hh3cCBQoSClassifierOperator_Type.__name__ = "Integer32"
_Hh3cCBQoSClassifierOperator_Object = MibTableColumn
hh3cCBQoSClassifierOperator = _Hh3cCBQoSClassifierOperator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 4),
    _Hh3cCBQoSClassifierOperator_Type()
)
hh3cCBQoSClassifierOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierOperator.setStatus("current")


class _Hh3cCBQoSClassifierLayer_Type(Integer32):
    """Custom type hh3cCBQoSClassifierLayer based on Integer32"""
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


_Hh3cCBQoSClassifierLayer_Type.__name__ = "Integer32"
_Hh3cCBQoSClassifierLayer_Object = MibTableColumn
hh3cCBQoSClassifierLayer = _Hh3cCBQoSClassifierLayer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 5),
    _Hh3cCBQoSClassifierLayer_Type()
)
hh3cCBQoSClassifierLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierLayer.setStatus("current")


class _Hh3cCBQoSClassifierType_Type(Integer32):
    """Custom type hh3cCBQoSClassifierType based on Integer32"""
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


_Hh3cCBQoSClassifierType_Type.__name__ = "Integer32"
_Hh3cCBQoSClassifierType_Object = MibTableColumn
hh3cCBQoSClassifierType = _Hh3cCBQoSClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 6),
    _Hh3cCBQoSClassifierType_Type()
)
hh3cCBQoSClassifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierType.setStatus("current")
_Hh3cCBQosClassifierMatchRuleNextIndex_Type = Integer32
_Hh3cCBQosClassifierMatchRuleNextIndex_Object = MibTableColumn
hh3cCBQosClassifierMatchRuleNextIndex = _Hh3cCBQosClassifierMatchRuleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 7),
    _Hh3cCBQosClassifierMatchRuleNextIndex_Type()
)
hh3cCBQosClassifierMatchRuleNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQosClassifierMatchRuleNextIndex.setStatus("current")
_Hh3cCBQoSClassifierRowStatus_Type = RowStatus
_Hh3cCBQoSClassifierRowStatus_Object = MibTableColumn
hh3cCBQoSClassifierRowStatus = _Hh3cCBQoSClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 2, 1, 8),
    _Hh3cCBQoSClassifierRowStatus_Type()
)
hh3cCBQoSClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSClassifierRowStatus.setStatus("current")
_Hh3cCBQoSMatchRuleCfgInfoTable_Object = MibTable
hh3cCBQoSMatchRuleCfgInfoTable = _Hh3cCBQoSMatchRuleCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleCfgInfoTable.setStatus("current")
_Hh3cCBQoSMatchRuleCfgInfoEntry_Object = MibTableRow
hh3cCBQoSMatchRuleCfgInfoEntry = _Hh3cCBQoSMatchRuleCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1)
)
hh3cCBQoSMatchRuleCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSClassifierIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSMatchRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleCfgInfoEntry.setStatus("current")
_Hh3cCBQoSMatchRuleIndex_Type = Integer32
_Hh3cCBQoSMatchRuleIndex_Object = MibTableColumn
hh3cCBQoSMatchRuleIndex = _Hh3cCBQoSMatchRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 1),
    _Hh3cCBQoSMatchRuleIndex_Type()
)
hh3cCBQoSMatchRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleIndex.setStatus("current")


class _Hh3cCBQoSMatchRuleIfNot_Type(Integer32):
    """Custom type hh3cCBQoSMatchRuleIfNot based on Integer32"""
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


_Hh3cCBQoSMatchRuleIfNot_Type.__name__ = "Integer32"
_Hh3cCBQoSMatchRuleIfNot_Object = MibTableColumn
hh3cCBQoSMatchRuleIfNot = _Hh3cCBQoSMatchRuleIfNot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 2),
    _Hh3cCBQoSMatchRuleIfNot_Type()
)
hh3cCBQoSMatchRuleIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleIfNot.setStatus("current")
_Hh3cCBQoSMatchRuleType_Type = MatchRuleType
_Hh3cCBQoSMatchRuleType_Object = MibTableColumn
hh3cCBQoSMatchRuleType = _Hh3cCBQoSMatchRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 3),
    _Hh3cCBQoSMatchRuleType_Type()
)
hh3cCBQoSMatchRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleType.setStatus("current")


class _Hh3cCBQoSMatchRuleStringValue_Type(OctetString):
    """Custom type hh3cCBQoSMatchRuleStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCBQoSMatchRuleStringValue_Type.__name__ = "OctetString"
_Hh3cCBQoSMatchRuleStringValue_Object = MibTableColumn
hh3cCBQoSMatchRuleStringValue = _Hh3cCBQoSMatchRuleStringValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 4),
    _Hh3cCBQoSMatchRuleStringValue_Type()
)
hh3cCBQoSMatchRuleStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleStringValue.setStatus("current")
_Hh3cCBQoSMatchRuleIntValue1_Type = Unsigned32
_Hh3cCBQoSMatchRuleIntValue1_Object = MibTableColumn
hh3cCBQoSMatchRuleIntValue1 = _Hh3cCBQoSMatchRuleIntValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 5),
    _Hh3cCBQoSMatchRuleIntValue1_Type()
)
hh3cCBQoSMatchRuleIntValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleIntValue1.setStatus("current")
_Hh3cCBQoSMatchRuleIntValue2_Type = Unsigned32
_Hh3cCBQoSMatchRuleIntValue2_Object = MibTableColumn
hh3cCBQoSMatchRuleIntValue2 = _Hh3cCBQoSMatchRuleIntValue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 6),
    _Hh3cCBQoSMatchRuleIntValue2_Type()
)
hh3cCBQoSMatchRuleIntValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleIntValue2.setStatus("current")
_Hh3cCBQoSMatchIpAddressType_Type = InetAddressType
_Hh3cCBQoSMatchIpAddressType_Object = MibTableColumn
hh3cCBQoSMatchIpAddressType = _Hh3cCBQoSMatchIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 7),
    _Hh3cCBQoSMatchIpAddressType_Type()
)
hh3cCBQoSMatchIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchIpAddressType.setStatus("current")
_Hh3cCBQoSMatchIpAddress_Type = InetAddress
_Hh3cCBQoSMatchIpAddress_Object = MibTableColumn
hh3cCBQoSMatchIpAddress = _Hh3cCBQoSMatchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 8),
    _Hh3cCBQoSMatchIpAddress_Type()
)
hh3cCBQoSMatchIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchIpAddress.setStatus("current")
_Hh3cCBQoSMatchRuleRowStatus_Type = RowStatus
_Hh3cCBQoSMatchRuleRowStatus_Object = MibTableColumn
hh3cCBQoSMatchRuleRowStatus = _Hh3cCBQoSMatchRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 1, 3, 1, 9),
    _Hh3cCBQoSMatchRuleRowStatus_Type()
)
hh3cCBQoSMatchRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMatchRuleRowStatus.setStatus("current")
_Hh3cCBQoSBehaviorObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSBehaviorObjects = _Hh3cCBQoSBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2)
)
_Hh3cCBQoSBehaviorIndexNext_Type = Integer32
_Hh3cCBQoSBehaviorIndexNext_Object = MibScalar
hh3cCBQoSBehaviorIndexNext = _Hh3cCBQoSBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 1),
    _Hh3cCBQoSBehaviorIndexNext_Type()
)
hh3cCBQoSBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorIndexNext.setStatus("current")
_Hh3cCBQoSBehaviorCfgInfoTable_Object = MibTable
hh3cCBQoSBehaviorCfgInfoTable = _Hh3cCBQoSBehaviorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorCfgInfoTable.setStatus("current")
_Hh3cCBQoSBehaviorCfgInfoEntry_Object = MibTableRow
hh3cCBQoSBehaviorCfgInfoEntry = _Hh3cCBQoSBehaviorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 2, 1)
)
hh3cCBQoSBehaviorCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorCfgInfoEntry.setStatus("current")
_Hh3cCBQoSBehaviorIndex_Type = Integer32
_Hh3cCBQoSBehaviorIndex_Object = MibTableColumn
hh3cCBQoSBehaviorIndex = _Hh3cCBQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 2, 1, 1),
    _Hh3cCBQoSBehaviorIndex_Type()
)
hh3cCBQoSBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorIndex.setStatus("current")


class _Hh3cCBQoSBehaviorName_Type(OctetString):
    """Custom type hh3cCBQoSBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSBehaviorName_Type.__name__ = "OctetString"
_Hh3cCBQoSBehaviorName_Object = MibTableColumn
hh3cCBQoSBehaviorName = _Hh3cCBQoSBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 2, 1, 2),
    _Hh3cCBQoSBehaviorName_Type()
)
hh3cCBQoSBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorName.setStatus("current")


class _Hh3cCBQoSBehaviorType_Type(Integer32):
    """Custom type hh3cCBQoSBehaviorType based on Integer32"""
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


_Hh3cCBQoSBehaviorType_Type.__name__ = "Integer32"
_Hh3cCBQoSBehaviorType_Object = MibTableColumn
hh3cCBQoSBehaviorType = _Hh3cCBQoSBehaviorType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 2, 1, 3),
    _Hh3cCBQoSBehaviorType_Type()
)
hh3cCBQoSBehaviorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorType.setStatus("current")
_Hh3cCBQoSBehaviorRowStatus_Type = RowStatus
_Hh3cCBQoSBehaviorRowStatus_Object = MibTableColumn
hh3cCBQoSBehaviorRowStatus = _Hh3cCBQoSBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 2, 1, 4),
    _Hh3cCBQoSBehaviorRowStatus_Type()
)
hh3cCBQoSBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSBehaviorRowStatus.setStatus("current")
_Hh3cCBQoSCarCfgInfoTable_Object = MibTable
hh3cCBQoSCarCfgInfoTable = _Hh3cCBQoSCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSCarCfgInfoTable.setStatus("current")
_Hh3cCBQoSCarCfgInfoEntry_Object = MibTableRow
hh3cCBQoSCarCfgInfoEntry = _Hh3cCBQoSCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1)
)
hh3cCBQoSCarCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSCarCfgInfoEntry.setStatus("current")
_Hh3cCBQoSCarCir_Type = Unsigned32
_Hh3cCBQoSCarCir_Object = MibTableColumn
hh3cCBQoSCarCir = _Hh3cCBQoSCarCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 1),
    _Hh3cCBQoSCarCir_Type()
)
hh3cCBQoSCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarCir.setStatus("current")
_Hh3cCBQoSCarCbs_Type = Unsigned32
_Hh3cCBQoSCarCbs_Object = MibTableColumn
hh3cCBQoSCarCbs = _Hh3cCBQoSCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 2),
    _Hh3cCBQoSCarCbs_Type()
)
hh3cCBQoSCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarCbs.setStatus("current")


class _Hh3cCBQoSCarEbs_Type(Unsigned32):
    """Custom type hh3cCBQoSCarEbs based on Unsigned32"""
    defaultValue = 0


_Hh3cCBQoSCarEbs_Object = MibTableColumn
hh3cCBQoSCarEbs = _Hh3cCBQoSCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 3),
    _Hh3cCBQoSCarEbs_Type()
)
hh3cCBQoSCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarEbs.setStatus("current")
_Hh3cCBQoSCarPir_Type = Unsigned32
_Hh3cCBQoSCarPir_Object = MibTableColumn
hh3cCBQoSCarPir = _Hh3cCBQoSCarPir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 4),
    _Hh3cCBQoSCarPir_Type()
)
hh3cCBQoSCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarPir.setStatus("current")
_Hh3cCBQoSCarPbs_Type = Unsigned32
_Hh3cCBQoSCarPbs_Object = MibTableColumn
hh3cCBQoSCarPbs = _Hh3cCBQoSCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 5),
    _Hh3cCBQoSCarPbs_Type()
)
hh3cCBQoSCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarPbs.setStatus("current")


class _Hh3cCBQoSCarGreenAction_Type(CarAction):
    """Custom type hh3cCBQoSCarGreenAction based on CarAction"""


_Hh3cCBQoSCarGreenAction_Object = MibTableColumn
hh3cCBQoSCarGreenAction = _Hh3cCBQoSCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 6),
    _Hh3cCBQoSCarGreenAction_Type()
)
hh3cCBQoSCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarGreenAction.setStatus("current")


class _Hh3cCBQoSCarGreenRemarkValue_Type(Integer32):
    """Custom type hh3cCBQoSCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cCBQoSCarGreenRemarkValue_Type.__name__ = "Integer32"
_Hh3cCBQoSCarGreenRemarkValue_Object = MibTableColumn
hh3cCBQoSCarGreenRemarkValue = _Hh3cCBQoSCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 7),
    _Hh3cCBQoSCarGreenRemarkValue_Type()
)
hh3cCBQoSCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarGreenRemarkValue.setStatus("current")


class _Hh3cCBQoSCarYellowAction_Type(CarAction):
    """Custom type hh3cCBQoSCarYellowAction based on CarAction"""


_Hh3cCBQoSCarYellowAction_Object = MibTableColumn
hh3cCBQoSCarYellowAction = _Hh3cCBQoSCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 8),
    _Hh3cCBQoSCarYellowAction_Type()
)
hh3cCBQoSCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarYellowAction.setStatus("current")


class _Hh3cCBQoSCarYellowRemarkValue_Type(Integer32):
    """Custom type hh3cCBQoSCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cCBQoSCarYellowRemarkValue_Type.__name__ = "Integer32"
_Hh3cCBQoSCarYellowRemarkValue_Object = MibTableColumn
hh3cCBQoSCarYellowRemarkValue = _Hh3cCBQoSCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 9),
    _Hh3cCBQoSCarYellowRemarkValue_Type()
)
hh3cCBQoSCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarYellowRemarkValue.setStatus("current")


class _Hh3cCBQoSCarRedAction_Type(CarAction):
    """Custom type hh3cCBQoSCarRedAction based on CarAction"""


_Hh3cCBQoSCarRedAction_Object = MibTableColumn
hh3cCBQoSCarRedAction = _Hh3cCBQoSCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 10),
    _Hh3cCBQoSCarRedAction_Type()
)
hh3cCBQoSCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarRedAction.setStatus("current")


class _Hh3cCBQoSCarRedRemarkValue_Type(Integer32):
    """Custom type hh3cCBQoSCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cCBQoSCarRedRemarkValue_Type.__name__ = "Integer32"
_Hh3cCBQoSCarRedRemarkValue_Object = MibTableColumn
hh3cCBQoSCarRedRemarkValue = _Hh3cCBQoSCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 11),
    _Hh3cCBQoSCarRedRemarkValue_Type()
)
hh3cCBQoSCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarRedRemarkValue.setStatus("current")


class _Hh3cCBQoSCarPolicedPriorityMapType_Type(Integer32):
    """Custom type hh3cCBQoSCarPolicedPriorityMapType based on Integer32"""
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


_Hh3cCBQoSCarPolicedPriorityMapType_Type.__name__ = "Integer32"
_Hh3cCBQoSCarPolicedPriorityMapType_Object = MibTableColumn
hh3cCBQoSCarPolicedPriorityMapType = _Hh3cCBQoSCarPolicedPriorityMapType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 12),
    _Hh3cCBQoSCarPolicedPriorityMapType_Type()
)
hh3cCBQoSCarPolicedPriorityMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarPolicedPriorityMapType.setStatus("current")
_Hh3cCBQoSCarRowStatus_Type = RowStatus
_Hh3cCBQoSCarRowStatus_Object = MibTableColumn
hh3cCBQoSCarRowStatus = _Hh3cCBQoSCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 3, 1, 13),
    _Hh3cCBQoSCarRowStatus_Type()
)
hh3cCBQoSCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSCarRowStatus.setStatus("current")
_Hh3cCBQoSAggregativeCarCfgInfoTable_Object = MibTable
hh3cCBQoSAggregativeCarCfgInfoTable = _Hh3cCBQoSAggregativeCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAggregativeCarCfgInfoTable.setStatus("current")
_Hh3cCBQoSAggregativeCarCfgInfoEntry_Object = MibTableRow
hh3cCBQoSAggregativeCarCfgInfoEntry = _Hh3cCBQoSAggregativeCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 4, 1)
)
hh3cCBQoSAggregativeCarCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSCarAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAggregativeCarCfgInfoEntry.setStatus("current")
_Hh3cCBQoSCarAggregativeCarIndex_Type = Integer32
_Hh3cCBQoSCarAggregativeCarIndex_Object = MibTableColumn
hh3cCBQoSCarAggregativeCarIndex = _Hh3cCBQoSCarAggregativeCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 4, 1, 1),
    _Hh3cCBQoSCarAggregativeCarIndex_Type()
)
hh3cCBQoSCarAggregativeCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSCarAggregativeCarIndex.setStatus("current")


class _Hh3cCBQoSCarAggregativeCarName_Type(OctetString):
    """Custom type hh3cCBQoSCarAggregativeCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSCarAggregativeCarName_Type.__name__ = "OctetString"
_Hh3cCBQoSCarAggregativeCarName_Object = MibTableColumn
hh3cCBQoSCarAggregativeCarName = _Hh3cCBQoSCarAggregativeCarName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 4, 1, 2),
    _Hh3cCBQoSCarAggregativeCarName_Type()
)
hh3cCBQoSCarAggregativeCarName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarAggregativeCarName.setStatus("current")
_Hh3cCBQoSAggregativeCarRowStatus_Type = RowStatus
_Hh3cCBQoSAggregativeCarRowStatus_Object = MibTableColumn
hh3cCBQoSAggregativeCarRowStatus = _Hh3cCBQoSAggregativeCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 4, 1, 3),
    _Hh3cCBQoSAggregativeCarRowStatus_Type()
)
hh3cCBQoSAggregativeCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSAggregativeCarRowStatus.setStatus("current")
_Hh3cCBQoSGtsCfgInfoTable_Object = MibTable
hh3cCBQoSGtsCfgInfoTable = _Hh3cCBQoSGtsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSGtsCfgInfoTable.setStatus("current")
_Hh3cCBQoSGtsCfgInfoEntry_Object = MibTableRow
hh3cCBQoSGtsCfgInfoEntry = _Hh3cCBQoSGtsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5, 1)
)
hh3cCBQoSGtsCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSGtsCfgInfoEntry.setStatus("current")
_Hh3cCBQoSGtsCir_Type = Unsigned32
_Hh3cCBQoSGtsCir_Object = MibTableColumn
hh3cCBQoSGtsCir = _Hh3cCBQoSGtsCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5, 1, 1),
    _Hh3cCBQoSGtsCir_Type()
)
hh3cCBQoSGtsCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsCir.setStatus("current")
_Hh3cCBQoSGtsCbs_Type = Unsigned32
_Hh3cCBQoSGtsCbs_Object = MibTableColumn
hh3cCBQoSGtsCbs = _Hh3cCBQoSGtsCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5, 1, 2),
    _Hh3cCBQoSGtsCbs_Type()
)
hh3cCBQoSGtsCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsCbs.setStatus("current")
_Hh3cCBQoSGtsEbs_Type = Unsigned32
_Hh3cCBQoSGtsEbs_Object = MibTableColumn
hh3cCBQoSGtsEbs = _Hh3cCBQoSGtsEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5, 1, 3),
    _Hh3cCBQoSGtsEbs_Type()
)
hh3cCBQoSGtsEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsEbs.setStatus("current")


class _Hh3cCBQoSGtsQueueLength_Type(Integer32):
    """Custom type hh3cCBQoSGtsQueueLength based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cCBQoSGtsQueueLength_Type.__name__ = "Integer32"
_Hh3cCBQoSGtsQueueLength_Object = MibTableColumn
hh3cCBQoSGtsQueueLength = _Hh3cCBQoSGtsQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5, 1, 4),
    _Hh3cCBQoSGtsQueueLength_Type()
)
hh3cCBQoSGtsQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsQueueLength.setStatus("current")
_Hh3cCBQoSGtsRowStatus_Type = RowStatus
_Hh3cCBQoSGtsRowStatus_Object = MibTableColumn
hh3cCBQoSGtsRowStatus = _Hh3cCBQoSGtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 5, 1, 5),
    _Hh3cCBQoSGtsRowStatus_Type()
)
hh3cCBQoSGtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsRowStatus.setStatus("current")
_Hh3cCBQoSRemarkCfgInfoTable_Object = MibTable
hh3cCBQoSRemarkCfgInfoTable = _Hh3cCBQoSRemarkCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkCfgInfoTable.setStatus("current")
_Hh3cCBQoSRemarkCfgInfoEntry_Object = MibTableRow
hh3cCBQoSRemarkCfgInfoEntry = _Hh3cCBQoSRemarkCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 6, 1)
)
hh3cCBQoSRemarkCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSRemarkType"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkCfgInfoEntry.setStatus("current")
_Hh3cCBQoSRemarkType_Type = RemarkType
_Hh3cCBQoSRemarkType_Object = MibTableColumn
hh3cCBQoSRemarkType = _Hh3cCBQoSRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 6, 1, 1),
    _Hh3cCBQoSRemarkType_Type()
)
hh3cCBQoSRemarkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkType.setStatus("current")


class _Hh3cCBQoSRemarkValue_Type(Integer32):
    """Custom type hh3cCBQoSRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hh3cCBQoSRemarkValue_Type.__name__ = "Integer32"
_Hh3cCBQoSRemarkValue_Object = MibTableColumn
hh3cCBQoSRemarkValue = _Hh3cCBQoSRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 6, 1, 2),
    _Hh3cCBQoSRemarkValue_Type()
)
hh3cCBQoSRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkValue.setStatus("current")
_Hh3cCBQoSRemarkRowStatus_Type = RowStatus
_Hh3cCBQoSRemarkRowStatus_Object = MibTableColumn
hh3cCBQoSRemarkRowStatus = _Hh3cCBQoSRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 6, 1, 3),
    _Hh3cCBQoSRemarkRowStatus_Type()
)
hh3cCBQoSRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkRowStatus.setStatus("current")
_Hh3cCBQoSQueueCfgInfoTable_Object = MibTable
hh3cCBQoSQueueCfgInfoTable = _Hh3cCBQoSQueueCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cCBQoSQueueCfgInfoTable.setStatus("current")
_Hh3cCBQoSQueueCfgInfoEntry_Object = MibTableRow
hh3cCBQoSQueueCfgInfoEntry = _Hh3cCBQoSQueueCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1)
)
hh3cCBQoSQueueCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSQueueCfgInfoEntry.setStatus("current")
_Hh3cCBQoSQueueType_Type = QueueType
_Hh3cCBQoSQueueType_Object = MibTableColumn
hh3cCBQoSQueueType = _Hh3cCBQoSQueueType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 1),
    _Hh3cCBQoSQueueType_Type()
)
hh3cCBQoSQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueType.setStatus("current")


class _Hh3cCBQoSQueueDropType_Type(Integer32):
    """Custom type hh3cCBQoSQueueDropType based on Integer32"""
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


_Hh3cCBQoSQueueDropType_Type.__name__ = "Integer32"
_Hh3cCBQoSQueueDropType_Object = MibTableColumn
hh3cCBQoSQueueDropType = _Hh3cCBQoSQueueDropType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 2),
    _Hh3cCBQoSQueueDropType_Type()
)
hh3cCBQoSQueueDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueDropType.setStatus("current")


class _Hh3cCBQoSQueueLength_Type(Integer32):
    """Custom type hh3cCBQoSQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cCBQoSQueueLength_Type.__name__ = "Integer32"
_Hh3cCBQoSQueueLength_Object = MibTableColumn
hh3cCBQoSQueueLength = _Hh3cCBQoSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 3),
    _Hh3cCBQoSQueueLength_Type()
)
hh3cCBQoSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueLength.setStatus("current")
_Hh3cCBQoSQueueBandwidthUnit_Type = QueueBandwidthUnit
_Hh3cCBQoSQueueBandwidthUnit_Object = MibTableColumn
hh3cCBQoSQueueBandwidthUnit = _Hh3cCBQoSQueueBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 4),
    _Hh3cCBQoSQueueBandwidthUnit_Type()
)
hh3cCBQoSQueueBandwidthUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueBandwidthUnit.setStatus("current")


class _Hh3cCBQoSQueueBandwidthValue_Type(Integer32):
    """Custom type hh3cCBQoSQueueBandwidthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cCBQoSQueueBandwidthValue_Type.__name__ = "Integer32"
_Hh3cCBQoSQueueBandwidthValue_Object = MibTableColumn
hh3cCBQoSQueueBandwidthValue = _Hh3cCBQoSQueueBandwidthValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 5),
    _Hh3cCBQoSQueueBandwidthValue_Type()
)
hh3cCBQoSQueueBandwidthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueBandwidthValue.setStatus("current")


class _Hh3cCBQoSQueueCbs_Type(Integer32):
    """Custom type hh3cCBQoSQueueCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1000000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cCBQoSQueueCbs_Type.__name__ = "Integer32"
_Hh3cCBQoSQueueCbs_Object = MibTableColumn
hh3cCBQoSQueueCbs = _Hh3cCBQoSQueueCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 6),
    _Hh3cCBQoSQueueCbs_Type()
)
hh3cCBQoSQueueCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueCbs.setStatus("current")


class _Hh3cCBQoSQueueQueueNumber_Type(Integer32):
    """Custom type hh3cCBQoSQueueQueueNumber based on Integer32"""
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


_Hh3cCBQoSQueueQueueNumber_Type.__name__ = "Integer32"
_Hh3cCBQoSQueueQueueNumber_Object = MibTableColumn
hh3cCBQoSQueueQueueNumber = _Hh3cCBQoSQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 7),
    _Hh3cCBQoSQueueQueueNumber_Type()
)
hh3cCBQoSQueueQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueQueueNumber.setStatus("current")


class _Hh3cCBQoSQueueCbsRatio_Type(Integer32):
    """Custom type hh3cCBQoSQueueCbsRatio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cCBQoSQueueCbsRatio_Type.__name__ = "Integer32"
_Hh3cCBQoSQueueCbsRatio_Object = MibTableColumn
hh3cCBQoSQueueCbsRatio = _Hh3cCBQoSQueueCbsRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 8),
    _Hh3cCBQoSQueueCbsRatio_Type()
)
hh3cCBQoSQueueCbsRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueCbsRatio.setStatus("current")
_Hh3cCBQoSQueueRowStatus_Type = RowStatus
_Hh3cCBQoSQueueRowStatus_Object = MibTableColumn
hh3cCBQoSQueueRowStatus = _Hh3cCBQoSQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 7, 1, 9),
    _Hh3cCBQoSQueueRowStatus_Type()
)
hh3cCBQoSQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueRowStatus.setStatus("current")
_Hh3cCBQoSWredCfgInfoTable_Object = MibTable
hh3cCBQoSWredCfgInfoTable = _Hh3cCBQoSWredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cCBQoSWredCfgInfoTable.setStatus("current")
_Hh3cCBQoSWredCfgInfoEntry_Object = MibTableRow
hh3cCBQoSWredCfgInfoEntry = _Hh3cCBQoSWredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 8, 1)
)
hh3cCBQoSWredCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSWredCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSWredType_Type(WredType):
    """Custom type hh3cCBQoSWredType based on WredType"""
    defaultValue = 1


_Hh3cCBQoSWredType_Object = MibTableColumn
hh3cCBQoSWredType = _Hh3cCBQoSWredType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 8, 1, 1),
    _Hh3cCBQoSWredType_Type()
)
hh3cCBQoSWredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCBQoSWredType.setStatus("current")


class _Hh3cCBQoSWredWeightConst_Type(Integer32):
    """Custom type hh3cCBQoSWredWeightConst based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cCBQoSWredWeightConst_Type.__name__ = "Integer32"
_Hh3cCBQoSWredWeightConst_Object = MibTableColumn
hh3cCBQoSWredWeightConst = _Hh3cCBQoSWredWeightConst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 8, 1, 2),
    _Hh3cCBQoSWredWeightConst_Type()
)
hh3cCBQoSWredWeightConst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCBQoSWredWeightConst.setStatus("current")
_Hh3cCBQoSWredClassCfgInfoTable_Object = MibTable
hh3cCBQoSWredClassCfgInfoTable = _Hh3cCBQoSWredClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cCBQoSWredClassCfgInfoTable.setStatus("current")
_Hh3cCBQoSWredClassCfgInfoEntry_Object = MibTableRow
hh3cCBQoSWredClassCfgInfoEntry = _Hh3cCBQoSWredClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 9, 1)
)
hh3cCBQoSWredClassCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSWredClassCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSWredClassValue_Type(Integer32):
    """Custom type hh3cCBQoSWredClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cCBQoSWredClassValue_Type.__name__ = "Integer32"
_Hh3cCBQoSWredClassValue_Object = MibTableColumn
hh3cCBQoSWredClassValue = _Hh3cCBQoSWredClassValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 9, 1, 1),
    _Hh3cCBQoSWredClassValue_Type()
)
hh3cCBQoSWredClassValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSWredClassValue.setStatus("current")


class _Hh3cCBQoSWredClassLowLimit_Type(Integer32):
    """Custom type hh3cCBQoSWredClassLowLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cCBQoSWredClassLowLimit_Type.__name__ = "Integer32"
_Hh3cCBQoSWredClassLowLimit_Object = MibTableColumn
hh3cCBQoSWredClassLowLimit = _Hh3cCBQoSWredClassLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 9, 1, 2),
    _Hh3cCBQoSWredClassLowLimit_Type()
)
hh3cCBQoSWredClassLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCBQoSWredClassLowLimit.setStatus("current")


class _Hh3cCBQoSWredClassHighLimit_Type(Integer32):
    """Custom type hh3cCBQoSWredClassHighLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cCBQoSWredClassHighLimit_Type.__name__ = "Integer32"
_Hh3cCBQoSWredClassHighLimit_Object = MibTableColumn
hh3cCBQoSWredClassHighLimit = _Hh3cCBQoSWredClassHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 9, 1, 3),
    _Hh3cCBQoSWredClassHighLimit_Type()
)
hh3cCBQoSWredClassHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCBQoSWredClassHighLimit.setStatus("current")


class _Hh3cCBQoSWredClassDiscardProb_Type(Integer32):
    """Custom type hh3cCBQoSWredClassDiscardProb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cCBQoSWredClassDiscardProb_Type.__name__ = "Integer32"
_Hh3cCBQoSWredClassDiscardProb_Object = MibTableColumn
hh3cCBQoSWredClassDiscardProb = _Hh3cCBQoSWredClassDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 9, 1, 4),
    _Hh3cCBQoSWredClassDiscardProb_Type()
)
hh3cCBQoSWredClassDiscardProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCBQoSWredClassDiscardProb.setStatus("current")
_Hh3cCBQoSPolicyRouteCfgInfoTable_Object = MibTable
hh3cCBQoSPolicyRouteCfgInfoTable = _Hh3cCBQoSPolicyRouteCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRouteCfgInfoTable.setStatus("current")
_Hh3cCBQoSPolicyRouteCfgInfoEntry_Object = MibTableRow
hh3cCBQoSPolicyRouteCfgInfoEntry = _Hh3cCBQoSPolicyRouteCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 10, 1)
)
hh3cCBQoSPolicyRouteCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRouteCfgInfoEntry.setStatus("current")
_Hh3cCBQoSPolicyRouteIpAddrType_Type = InetAddressType
_Hh3cCBQoSPolicyRouteIpAddrType_Object = MibTableColumn
hh3cCBQoSPolicyRouteIpAddrType = _Hh3cCBQoSPolicyRouteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 10, 1, 1),
    _Hh3cCBQoSPolicyRouteIpAddrType_Type()
)
hh3cCBQoSPolicyRouteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRouteIpAddrType.setStatus("current")
_Hh3cCBQoSPolicyRouteNexthop_Type = InetAddress
_Hh3cCBQoSPolicyRouteNexthop_Object = MibTableColumn
hh3cCBQoSPolicyRouteNexthop = _Hh3cCBQoSPolicyRouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 10, 1, 2),
    _Hh3cCBQoSPolicyRouteNexthop_Type()
)
hh3cCBQoSPolicyRouteNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRouteNexthop.setStatus("current")


class _Hh3cCBQoSPolicyRouteBackup_Type(Integer32):
    """Custom type hh3cCBQoSPolicyRouteBackup based on Integer32"""
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


_Hh3cCBQoSPolicyRouteBackup_Type.__name__ = "Integer32"
_Hh3cCBQoSPolicyRouteBackup_Object = MibTableColumn
hh3cCBQoSPolicyRouteBackup = _Hh3cCBQoSPolicyRouteBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 10, 1, 3),
    _Hh3cCBQoSPolicyRouteBackup_Type()
)
hh3cCBQoSPolicyRouteBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRouteBackup.setStatus("current")
_Hh3cCBQoSPolicyRouteRowStatus_Type = RowStatus
_Hh3cCBQoSPolicyRouteRowStatus_Object = MibTableColumn
hh3cCBQoSPolicyRouteRowStatus = _Hh3cCBQoSPolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 10, 1, 4),
    _Hh3cCBQoSPolicyRouteRowStatus_Type()
)
hh3cCBQoSPolicyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRouteRowStatus.setStatus("current")
_Hh3cCBQoSNatCfgInfoTable_Object = MibTable
hh3cCBQoSNatCfgInfoTable = _Hh3cCBQoSNatCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cCBQoSNatCfgInfoTable.setStatus("current")
_Hh3cCBQoSNatCfgInfoEntry_Object = MibTableRow
hh3cCBQoSNatCfgInfoEntry = _Hh3cCBQoSNatCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 11, 1)
)
hh3cCBQoSNatCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSNatCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSNatMainNumber_Type(Integer32):
    """Custom type hh3cCBQoSNatMainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cCBQoSNatMainNumber_Type.__name__ = "Integer32"
_Hh3cCBQoSNatMainNumber_Object = MibTableColumn
hh3cCBQoSNatMainNumber = _Hh3cCBQoSNatMainNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 11, 1, 1),
    _Hh3cCBQoSNatMainNumber_Type()
)
hh3cCBQoSNatMainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNatMainNumber.setStatus("current")


class _Hh3cCBQoSNatBackupNumber_Type(Integer32):
    """Custom type hh3cCBQoSNatBackupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cCBQoSNatBackupNumber_Type.__name__ = "Integer32"
_Hh3cCBQoSNatBackupNumber_Object = MibTableColumn
hh3cCBQoSNatBackupNumber = _Hh3cCBQoSNatBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 11, 1, 2),
    _Hh3cCBQoSNatBackupNumber_Type()
)
hh3cCBQoSNatBackupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNatBackupNumber.setStatus("current")


class _Hh3cCBQoSNatServiceClass_Type(Integer32):
    """Custom type hh3cCBQoSNatServiceClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cCBQoSNatServiceClass_Type.__name__ = "Integer32"
_Hh3cCBQoSNatServiceClass_Object = MibTableColumn
hh3cCBQoSNatServiceClass = _Hh3cCBQoSNatServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 11, 1, 3),
    _Hh3cCBQoSNatServiceClass_Type()
)
hh3cCBQoSNatServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNatServiceClass.setStatus("current")
_Hh3cCBQoSNatRowStatus_Type = RowStatus
_Hh3cCBQoSNatRowStatus_Object = MibTableColumn
hh3cCBQoSNatRowStatus = _Hh3cCBQoSNatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 11, 1, 4),
    _Hh3cCBQoSNatRowStatus_Type()
)
hh3cCBQoSNatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNatRowStatus.setStatus("current")
_Hh3cCBQoSFirewallCfgInfoTable_Object = MibTable
hh3cCBQoSFirewallCfgInfoTable = _Hh3cCBQoSFirewallCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFirewallCfgInfoTable.setStatus("current")
_Hh3cCBQoSFirewallCfgInfoEntry_Object = MibTableRow
hh3cCBQoSFirewallCfgInfoEntry = _Hh3cCBQoSFirewallCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 12, 1)
)
hh3cCBQoSFirewallCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFirewallCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSFirewallAction_Type(Integer32):
    """Custom type hh3cCBQoSFirewallAction based on Integer32"""
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


_Hh3cCBQoSFirewallAction_Type.__name__ = "Integer32"
_Hh3cCBQoSFirewallAction_Object = MibTableColumn
hh3cCBQoSFirewallAction = _Hh3cCBQoSFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 12, 1, 1),
    _Hh3cCBQoSFirewallAction_Type()
)
hh3cCBQoSFirewallAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSFirewallAction.setStatus("current")
_Hh3cCBQoSFirewallRowStatus_Type = RowStatus
_Hh3cCBQoSFirewallRowStatus_Object = MibTableColumn
hh3cCBQoSFirewallRowStatus = _Hh3cCBQoSFirewallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 12, 1, 2),
    _Hh3cCBQoSFirewallRowStatus_Type()
)
hh3cCBQoSFirewallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSFirewallRowStatus.setStatus("current")
_Hh3cCBQoSSamplingCfgInfoTable_Object = MibTable
hh3cCBQoSSamplingCfgInfoTable = _Hh3cCBQoSSamplingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cCBQoSSamplingCfgInfoTable.setStatus("current")
_Hh3cCBQoSSamplingCfgInfoEntry_Object = MibTableRow
hh3cCBQoSSamplingCfgInfoEntry = _Hh3cCBQoSSamplingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 13, 1)
)
hh3cCBQoSSamplingCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSSamplingCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSSamplingNum_Type(Integer32):
    """Custom type hh3cCBQoSSamplingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cCBQoSSamplingNum_Type.__name__ = "Integer32"
_Hh3cCBQoSSamplingNum_Object = MibTableColumn
hh3cCBQoSSamplingNum = _Hh3cCBQoSSamplingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 13, 1, 1),
    _Hh3cCBQoSSamplingNum_Type()
)
hh3cCBQoSSamplingNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSSamplingNum.setStatus("current")
_Hh3cCBQoSSamplingRowStatus_Type = RowStatus
_Hh3cCBQoSSamplingRowStatus_Object = MibTableColumn
hh3cCBQoSSamplingRowStatus = _Hh3cCBQoSSamplingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 13, 1, 2),
    _Hh3cCBQoSSamplingRowStatus_Type()
)
hh3cCBQoSSamplingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSSamplingRowStatus.setStatus("current")
_Hh3cCBQoSAccountCfgInfoTable_Object = MibTable
hh3cCBQoSAccountCfgInfoTable = _Hh3cCBQoSAccountCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAccountCfgInfoTable.setStatus("current")
_Hh3cCBQoSAccountCfgInfoEntry_Object = MibTableRow
hh3cCBQoSAccountCfgInfoEntry = _Hh3cCBQoSAccountCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 14, 1)
)
hh3cCBQoSAccountCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAccountCfgInfoEntry.setStatus("current")
_Hh3cCBQoSAccounting_Type = TruthValue
_Hh3cCBQoSAccounting_Object = MibTableColumn
hh3cCBQoSAccounting = _Hh3cCBQoSAccounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 14, 1, 1),
    _Hh3cCBQoSAccounting_Type()
)
hh3cCBQoSAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSAccounting.setStatus("current")
_Hh3cCBQoSAccountRowStatus_Type = RowStatus
_Hh3cCBQoSAccountRowStatus_Object = MibTableColumn
hh3cCBQoSAccountRowStatus = _Hh3cCBQoSAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 14, 1, 2),
    _Hh3cCBQoSAccountRowStatus_Type()
)
hh3cCBQoSAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSAccountRowStatus.setStatus("current")
_Hh3cCBQoSRedirectCfgInfoTable_Object = MibTable
hh3cCBQoSRedirectCfgInfoTable = _Hh3cCBQoSRedirectCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectCfgInfoTable.setStatus("current")
_Hh3cCBQoSRedirectCfgInfoEntry_Object = MibTableRow
hh3cCBQoSRedirectCfgInfoEntry = _Hh3cCBQoSRedirectCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1)
)
hh3cCBQoSRedirectCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSRedirectType_Type(Integer32):
    """Custom type hh3cCBQoSRedirectType based on Integer32"""
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


_Hh3cCBQoSRedirectType_Type.__name__ = "Integer32"
_Hh3cCBQoSRedirectType_Object = MibTableColumn
hh3cCBQoSRedirectType = _Hh3cCBQoSRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 1),
    _Hh3cCBQoSRedirectType_Type()
)
hh3cCBQoSRedirectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectType.setStatus("current")


class _Hh3cCBQoSRedirectIfIndex_Type(Integer32):
    """Custom type hh3cCBQoSRedirectIfIndex based on Integer32"""
    defaultValue = 0


_Hh3cCBQoSRedirectIfIndex_Object = MibTableColumn
hh3cCBQoSRedirectIfIndex = _Hh3cCBQoSRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 2),
    _Hh3cCBQoSRedirectIfIndex_Type()
)
hh3cCBQoSRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectIfIndex.setStatus("current")


class _Hh3cCBQoSRedirectIpAddressType_Type(InetAddressType):
    """Custom type hh3cCBQoSRedirectIpAddressType based on InetAddressType"""


_Hh3cCBQoSRedirectIpAddressType_Object = MibTableColumn
hh3cCBQoSRedirectIpAddressType = _Hh3cCBQoSRedirectIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 3),
    _Hh3cCBQoSRedirectIpAddressType_Type()
)
hh3cCBQoSRedirectIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectIpAddressType.setStatus("current")
_Hh3cCBQoSRedirectIpAddress1_Type = InetAddress
_Hh3cCBQoSRedirectIpAddress1_Object = MibTableColumn
hh3cCBQoSRedirectIpAddress1 = _Hh3cCBQoSRedirectIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 4),
    _Hh3cCBQoSRedirectIpAddress1_Type()
)
hh3cCBQoSRedirectIpAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectIpAddress1.setStatus("current")
_Hh3cCBQoSRedirectIpAddress2_Type = InetAddress
_Hh3cCBQoSRedirectIpAddress2_Object = MibTableColumn
hh3cCBQoSRedirectIpAddress2 = _Hh3cCBQoSRedirectIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 5),
    _Hh3cCBQoSRedirectIpAddress2_Type()
)
hh3cCBQoSRedirectIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectIpAddress2.setStatus("current")
_Hh3cCBQoSRedirectRowStatus_Type = RowStatus
_Hh3cCBQoSRedirectRowStatus_Object = MibTableColumn
hh3cCBQoSRedirectRowStatus = _Hh3cCBQoSRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 6),
    _Hh3cCBQoSRedirectRowStatus_Type()
)
hh3cCBQoSRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectRowStatus.setStatus("current")


class _Hh3cCBQoSRedirectIpv6Interface1_Type(Integer32):
    """Custom type hh3cCBQoSRedirectIpv6Interface1 based on Integer32"""
    defaultValue = 0


_Hh3cCBQoSRedirectIpv6Interface1_Object = MibTableColumn
hh3cCBQoSRedirectIpv6Interface1 = _Hh3cCBQoSRedirectIpv6Interface1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 7),
    _Hh3cCBQoSRedirectIpv6Interface1_Type()
)
hh3cCBQoSRedirectIpv6Interface1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectIpv6Interface1.setStatus("current")


class _Hh3cCBQoSRedirectIpv6Interface2_Type(Integer32):
    """Custom type hh3cCBQoSRedirectIpv6Interface2 based on Integer32"""
    defaultValue = 0


_Hh3cCBQoSRedirectIpv6Interface2_Object = MibTableColumn
hh3cCBQoSRedirectIpv6Interface2 = _Hh3cCBQoSRedirectIpv6Interface2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 15, 1, 8),
    _Hh3cCBQoSRedirectIpv6Interface2_Type()
)
hh3cCBQoSRedirectIpv6Interface2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSRedirectIpv6Interface2.setStatus("current")
_Hh3cCBQoSPriorityMapCfgInfoTable_Object = MibTable
hh3cCBQoSPriorityMapCfgInfoTable = _Hh3cCBQoSPriorityMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapCfgInfoTable.setStatus("current")
_Hh3cCBQoSPriorityMapCfgInfoEntry_Object = MibTableRow
hh3cCBQoSPriorityMapCfgInfoEntry = _Hh3cCBQoSPriorityMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1)
)
hh3cCBQoSPriorityMapCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSPriorityMapImportType_Type(Integer32):
    """Custom type hh3cCBQoSPriorityMapImportType based on Integer32"""
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


_Hh3cCBQoSPriorityMapImportType_Type.__name__ = "Integer32"
_Hh3cCBQoSPriorityMapImportType_Object = MibTableColumn
hh3cCBQoSPriorityMapImportType = _Hh3cCBQoSPriorityMapImportType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1, 1),
    _Hh3cCBQoSPriorityMapImportType_Type()
)
hh3cCBQoSPriorityMapImportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapImportType.setStatus("current")


class _Hh3cCBQoSPriorityMapExportType_Type(Integer32):
    """Custom type hh3cCBQoSPriorityMapExportType based on Integer32"""
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


_Hh3cCBQoSPriorityMapExportType_Type.__name__ = "Integer32"
_Hh3cCBQoSPriorityMapExportType_Object = MibTableColumn
hh3cCBQoSPriorityMapExportType = _Hh3cCBQoSPriorityMapExportType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1, 2),
    _Hh3cCBQoSPriorityMapExportType_Type()
)
hh3cCBQoSPriorityMapExportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapExportType.setStatus("current")
_Hh3cCBQoSPriorityMapGroupIndex_Type = Integer32
_Hh3cCBQoSPriorityMapGroupIndex_Object = MibTableColumn
hh3cCBQoSPriorityMapGroupIndex = _Hh3cCBQoSPriorityMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1, 3),
    _Hh3cCBQoSPriorityMapGroupIndex_Type()
)
hh3cCBQoSPriorityMapGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapGroupIndex.setStatus("current")


class _Hh3cCBQoSPriorityMapGroupName_Type(OctetString):
    """Custom type hh3cCBQoSPriorityMapGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCBQoSPriorityMapGroupName_Type.__name__ = "OctetString"
_Hh3cCBQoSPriorityMapGroupName_Object = MibTableColumn
hh3cCBQoSPriorityMapGroupName = _Hh3cCBQoSPriorityMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1, 4),
    _Hh3cCBQoSPriorityMapGroupName_Type()
)
hh3cCBQoSPriorityMapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapGroupName.setStatus("current")


class _Hh3cCBQoSPriorityMapAuto_Type(Integer32):
    """Custom type hh3cCBQoSPriorityMapAuto based on Integer32"""
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


_Hh3cCBQoSPriorityMapAuto_Type.__name__ = "Integer32"
_Hh3cCBQoSPriorityMapAuto_Object = MibTableColumn
hh3cCBQoSPriorityMapAuto = _Hh3cCBQoSPriorityMapAuto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1, 5),
    _Hh3cCBQoSPriorityMapAuto_Type()
)
hh3cCBQoSPriorityMapAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapAuto.setStatus("current")
_Hh3cCBQoSPriorityMapRowStatus_Type = RowStatus
_Hh3cCBQoSPriorityMapRowStatus_Object = MibTableColumn
hh3cCBQoSPriorityMapRowStatus = _Hh3cCBQoSPriorityMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 16, 1, 6),
    _Hh3cCBQoSPriorityMapRowStatus_Type()
)
hh3cCBQoSPriorityMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPriorityMapRowStatus.setStatus("current")
_Hh3cCBQoSMirrorCfgInfoTable_Object = MibTable
hh3cCBQoSMirrorCfgInfoTable = _Hh3cCBQoSMirrorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    hh3cCBQoSMirrorCfgInfoTable.setStatus("current")
_Hh3cCBQoSMirrorCfgInfoEntry_Object = MibTableRow
hh3cCBQoSMirrorCfgInfoEntry = _Hh3cCBQoSMirrorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 17, 1)
)
hh3cCBQoSMirrorCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSMirrorCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSMirrorType_Type(Integer32):
    """Custom type hh3cCBQoSMirrorType based on Integer32"""
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


_Hh3cCBQoSMirrorType_Type.__name__ = "Integer32"
_Hh3cCBQoSMirrorType_Object = MibTableColumn
hh3cCBQoSMirrorType = _Hh3cCBQoSMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 17, 1, 1),
    _Hh3cCBQoSMirrorType_Type()
)
hh3cCBQoSMirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMirrorType.setStatus("current")


class _Hh3cCBQoSMirrorIfIndex_Type(OctetString):
    """Custom type hh3cCBQoSMirrorIfIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCBQoSMirrorIfIndex_Type.__name__ = "OctetString"
_Hh3cCBQoSMirrorIfIndex_Object = MibTableColumn
hh3cCBQoSMirrorIfIndex = _Hh3cCBQoSMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 17, 1, 2),
    _Hh3cCBQoSMirrorIfIndex_Type()
)
hh3cCBQoSMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMirrorIfIndex.setStatus("current")


class _Hh3cCBQoSMirrorVlanID_Type(Integer32):
    """Custom type hh3cCBQoSMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cCBQoSMirrorVlanID_Type.__name__ = "Integer32"
_Hh3cCBQoSMirrorVlanID_Object = MibTableColumn
hh3cCBQoSMirrorVlanID = _Hh3cCBQoSMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 17, 1, 3),
    _Hh3cCBQoSMirrorVlanID_Type()
)
hh3cCBQoSMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMirrorVlanID.setStatus("current")
_Hh3cCBQoSMirrorRowStatus_Type = RowStatus
_Hh3cCBQoSMirrorRowStatus_Object = MibTableColumn
hh3cCBQoSMirrorRowStatus = _Hh3cCBQoSMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 17, 1, 4),
    _Hh3cCBQoSMirrorRowStatus_Type()
)
hh3cCBQoSMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSMirrorRowStatus.setStatus("current")
_Hh3cCBQoSNestCfgInfoTable_Object = MibTable
hh3cCBQoSNestCfgInfoTable = _Hh3cCBQoSNestCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18)
)
if mibBuilder.loadTexts:
    hh3cCBQoSNestCfgInfoTable.setStatus("current")
_Hh3cCBQoSNestCfgInfoEntry_Object = MibTableRow
hh3cCBQoSNestCfgInfoEntry = _Hh3cCBQoSNestCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18, 1)
)
hh3cCBQoSNestCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSNestCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSNestServiceVlanID_Type(Integer32):
    """Custom type hh3cCBQoSNestServiceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cCBQoSNestServiceVlanID_Type.__name__ = "Integer32"
_Hh3cCBQoSNestServiceVlanID_Object = MibTableColumn
hh3cCBQoSNestServiceVlanID = _Hh3cCBQoSNestServiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18, 1, 1),
    _Hh3cCBQoSNestServiceVlanID_Type()
)
hh3cCBQoSNestServiceVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestServiceVlanID.setStatus("current")


class _Hh3cCBQoSNestServiceDot1pValue_Type(Integer32):
    """Custom type hh3cCBQoSNestServiceDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cCBQoSNestServiceDot1pValue_Type.__name__ = "Integer32"
_Hh3cCBQoSNestServiceDot1pValue_Object = MibTableColumn
hh3cCBQoSNestServiceDot1pValue = _Hh3cCBQoSNestServiceDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18, 1, 2),
    _Hh3cCBQoSNestServiceDot1pValue_Type()
)
hh3cCBQoSNestServiceDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestServiceDot1pValue.setStatus("current")


class _Hh3cCBQoSNestCustomerVlanID_Type(Integer32):
    """Custom type hh3cCBQoSNestCustomerVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cCBQoSNestCustomerVlanID_Type.__name__ = "Integer32"
_Hh3cCBQoSNestCustomerVlanID_Object = MibTableColumn
hh3cCBQoSNestCustomerVlanID = _Hh3cCBQoSNestCustomerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18, 1, 3),
    _Hh3cCBQoSNestCustomerVlanID_Type()
)
hh3cCBQoSNestCustomerVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestCustomerVlanID.setStatus("current")


class _Hh3cCBQoSNestCustomerDot1pValue_Type(Integer32):
    """Custom type hh3cCBQoSNestCustomerDot1pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cCBQoSNestCustomerDot1pValue_Type.__name__ = "Integer32"
_Hh3cCBQoSNestCustomerDot1pValue_Object = MibTableColumn
hh3cCBQoSNestCustomerDot1pValue = _Hh3cCBQoSNestCustomerDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18, 1, 4),
    _Hh3cCBQoSNestCustomerDot1pValue_Type()
)
hh3cCBQoSNestCustomerDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestCustomerDot1pValue.setStatus("current")
_Hh3cCBQoSNestRowStatus_Type = RowStatus
_Hh3cCBQoSNestRowStatus_Object = MibTableColumn
hh3cCBQoSNestRowStatus = _Hh3cCBQoSNestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 18, 1, 5),
    _Hh3cCBQoSNestRowStatus_Type()
)
hh3cCBQoSNestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestRowStatus.setStatus("current")
_Hh3cCBQoSNestPolicyCfgInfoTable_Object = MibTable
hh3cCBQoSNestPolicyCfgInfoTable = _Hh3cCBQoSNestPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 19)
)
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyCfgInfoTable.setStatus("current")
_Hh3cCBQoSNestPolicyCfgInfoEntry_Object = MibTableRow
hh3cCBQoSNestPolicyCfgInfoEntry = _Hh3cCBQoSNestPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 19, 1)
)
hh3cCBQoSNestPolicyCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyCfgInfoEntry.setStatus("current")


class _Hh3cCBQoSNestPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSNestPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSNestPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSNestPolicyName_Object = MibTableColumn
hh3cCBQoSNestPolicyName = _Hh3cCBQoSNestPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 19, 1, 1),
    _Hh3cCBQoSNestPolicyName_Type()
)
hh3cCBQoSNestPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyName.setStatus("current")
_Hh3cCBQoSNestPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSNestPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSNestPolicyRowStatus = _Hh3cCBQoSNestPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 2, 19, 1, 2),
    _Hh3cCBQoSNestPolicyRowStatus_Type()
)
hh3cCBQoSNestPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyRowStatus.setStatus("current")
_Hh3cCBQoSPolicyObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSPolicyObjects = _Hh3cCBQoSPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3)
)
_Hh3cCBQoSPolicyIndexNext_Type = Integer32
_Hh3cCBQoSPolicyIndexNext_Object = MibScalar
hh3cCBQoSPolicyIndexNext = _Hh3cCBQoSPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 1),
    _Hh3cCBQoSPolicyIndexNext_Type()
)
hh3cCBQoSPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyIndexNext.setStatus("current")
_Hh3cCBQoSPolicyCfgInfoTable_Object = MibTable
hh3cCBQoSPolicyCfgInfoTable = _Hh3cCBQoSPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyCfgInfoTable.setStatus("current")
_Hh3cCBQoSPolicyCfgInfoEntry_Object = MibTableRow
hh3cCBQoSPolicyCfgInfoEntry = _Hh3cCBQoSPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1)
)
hh3cCBQoSPolicyCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyCfgInfoEntry.setStatus("current")
_Hh3cCBQoSPolicyIndex_Type = Integer32
_Hh3cCBQoSPolicyIndex_Object = MibTableColumn
hh3cCBQoSPolicyIndex = _Hh3cCBQoSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 1),
    _Hh3cCBQoSPolicyIndex_Type()
)
hh3cCBQoSPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyIndex.setStatus("current")


class _Hh3cCBQoSPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSPolicyName_Object = MibTableColumn
hh3cCBQoSPolicyName = _Hh3cCBQoSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 2),
    _Hh3cCBQoSPolicyName_Type()
)
hh3cCBQoSPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyName.setStatus("current")
_Hh3cCBQoSPolicyClassCount_Type = Integer32
_Hh3cCBQoSPolicyClassCount_Object = MibTableColumn
hh3cCBQoSPolicyClassCount = _Hh3cCBQoSPolicyClassCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 3),
    _Hh3cCBQoSPolicyClassCount_Type()
)
hh3cCBQoSPolicyClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassCount.setStatus("current")


class _Hh3cCBQoSPolicyConfigMode_Type(Integer32):
    """Custom type hh3cCBQoSPolicyConfigMode based on Integer32"""
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


_Hh3cCBQoSPolicyConfigMode_Type.__name__ = "Integer32"
_Hh3cCBQoSPolicyConfigMode_Object = MibTableColumn
hh3cCBQoSPolicyConfigMode = _Hh3cCBQoSPolicyConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 4),
    _Hh3cCBQoSPolicyConfigMode_Type()
)
hh3cCBQoSPolicyConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyConfigMode.setStatus("current")


class _Hh3cCBQoSPolicyType_Type(Integer32):
    """Custom type hh3cCBQoSPolicyType based on Integer32"""
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


_Hh3cCBQoSPolicyType_Type.__name__ = "Integer32"
_Hh3cCBQoSPolicyType_Object = MibTableColumn
hh3cCBQoSPolicyType = _Hh3cCBQoSPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 5),
    _Hh3cCBQoSPolicyType_Type()
)
hh3cCBQoSPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyType.setStatus("current")
_Hh3cCBQoSPolicyClassNextIndex_Type = Integer32
_Hh3cCBQoSPolicyClassNextIndex_Object = MibTableColumn
hh3cCBQoSPolicyClassNextIndex = _Hh3cCBQoSPolicyClassNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 6),
    _Hh3cCBQoSPolicyClassNextIndex_Type()
)
hh3cCBQoSPolicyClassNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassNextIndex.setStatus("current")
_Hh3cCBQoSPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSPolicyRowStatus = _Hh3cCBQoSPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 2, 1, 7),
    _Hh3cCBQoSPolicyRowStatus_Type()
)
hh3cCBQoSPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyRowStatus.setStatus("current")
_Hh3cCBQoSPolicyClassCfgInfoTable_Object = MibTable
hh3cCBQoSPolicyClassCfgInfoTable = _Hh3cCBQoSPolicyClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassCfgInfoTable.setStatus("current")
_Hh3cCBQoSPolicyClassCfgInfoEntry_Object = MibTableRow
hh3cCBQoSPolicyClassCfgInfoEntry = _Hh3cCBQoSPolicyClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1)
)
hh3cCBQoSPolicyClassCfgInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassCfgInfoEntry.setStatus("current")
_Hh3cCBQoSPolicyClassIndex_Type = Integer32
_Hh3cCBQoSPolicyClassIndex_Object = MibTableColumn
hh3cCBQoSPolicyClassIndex = _Hh3cCBQoSPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 1),
    _Hh3cCBQoSPolicyClassIndex_Type()
)
hh3cCBQoSPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassIndex.setStatus("current")
_Hh3cCBQoSPolicyClassClassifierIndex_Type = Integer32
_Hh3cCBQoSPolicyClassClassifierIndex_Object = MibTableColumn
hh3cCBQoSPolicyClassClassifierIndex = _Hh3cCBQoSPolicyClassClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 2),
    _Hh3cCBQoSPolicyClassClassifierIndex_Type()
)
hh3cCBQoSPolicyClassClassifierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassClassifierIndex.setStatus("current")


class _Hh3cCBQoSPolicyClassClassifierName_Type(OctetString):
    """Custom type hh3cCBQoSPolicyClassClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSPolicyClassClassifierName_Type.__name__ = "OctetString"
_Hh3cCBQoSPolicyClassClassifierName_Object = MibTableColumn
hh3cCBQoSPolicyClassClassifierName = _Hh3cCBQoSPolicyClassClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 3),
    _Hh3cCBQoSPolicyClassClassifierName_Type()
)
hh3cCBQoSPolicyClassClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassClassifierName.setStatus("current")
_Hh3cCBQoSPolicyClassBehaviorIndex_Type = Integer32
_Hh3cCBQoSPolicyClassBehaviorIndex_Object = MibTableColumn
hh3cCBQoSPolicyClassBehaviorIndex = _Hh3cCBQoSPolicyClassBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 4),
    _Hh3cCBQoSPolicyClassBehaviorIndex_Type()
)
hh3cCBQoSPolicyClassBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassBehaviorIndex.setStatus("current")


class _Hh3cCBQoSPolicyClassBehaviorName_Type(OctetString):
    """Custom type hh3cCBQoSPolicyClassBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSPolicyClassBehaviorName_Type.__name__ = "OctetString"
_Hh3cCBQoSPolicyClassBehaviorName_Object = MibTableColumn
hh3cCBQoSPolicyClassBehaviorName = _Hh3cCBQoSPolicyClassBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 5),
    _Hh3cCBQoSPolicyClassBehaviorName_Type()
)
hh3cCBQoSPolicyClassBehaviorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassBehaviorName.setStatus("current")


class _Hh3cCBQoSPolicyClassPrecedence_Type(Integer32):
    """Custom type hh3cCBQoSPolicyClassPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cCBQoSPolicyClassPrecedence_Type.__name__ = "Integer32"
_Hh3cCBQoSPolicyClassPrecedence_Object = MibTableColumn
hh3cCBQoSPolicyClassPrecedence = _Hh3cCBQoSPolicyClassPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 6),
    _Hh3cCBQoSPolicyClassPrecedence_Type()
)
hh3cCBQoSPolicyClassPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassPrecedence.setStatus("current")
_Hh3cCBQoSPolicyClassRowStatus_Type = RowStatus
_Hh3cCBQoSPolicyClassRowStatus_Object = MibTableColumn
hh3cCBQoSPolicyClassRowStatus = _Hh3cCBQoSPolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 7),
    _Hh3cCBQoSPolicyClassRowStatus_Type()
)
hh3cCBQoSPolicyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassRowStatus.setStatus("current")


class _Hh3cCBQoSPolicyClassMode_Type(Integer32):
    """Custom type hh3cCBQoSPolicyClassMode based on Integer32"""
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


_Hh3cCBQoSPolicyClassMode_Type.__name__ = "Integer32"
_Hh3cCBQoSPolicyClassMode_Object = MibTableColumn
hh3cCBQoSPolicyClassMode = _Hh3cCBQoSPolicyClassMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 8),
    _Hh3cCBQoSPolicyClassMode_Type()
)
hh3cCBQoSPolicyClassMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassMode.setStatus("current")
_Hh3cCBQoSPolicyClassCfgOrder_Type = Integer32
_Hh3cCBQoSPolicyClassCfgOrder_Object = MibTableColumn
hh3cCBQoSPolicyClassCfgOrder = _Hh3cCBQoSPolicyClassCfgOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 3, 3, 1, 9),
    _Hh3cCBQoSPolicyClassCfgOrder_Type()
)
hh3cCBQoSPolicyClassCfgOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPolicyClassCfgOrder.setStatus("current")
_Hh3cCBQoSApplyPolicyObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSApplyPolicyObjects = _Hh3cCBQoSApplyPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4)
)
_Hh3cCBQoSIfApplyPolicyTable_Object = MibTable
hh3cCBQoSIfApplyPolicyTable = _Hh3cCBQoSIfApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyTable.setStatus("current")
_Hh3cCBQoSIfApplyPolicyEntry_Object = MibTableRow
hh3cCBQoSIfApplyPolicyEntry = _Hh3cCBQoSIfApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1, 1)
)
hh3cCBQoSIfApplyPolicyEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyEntry.setStatus("current")
_Hh3cCBQoSIfApplyPolicyIfIndex_Type = Integer32
_Hh3cCBQoSIfApplyPolicyIfIndex_Object = MibTableColumn
hh3cCBQoSIfApplyPolicyIfIndex = _Hh3cCBQoSIfApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1, 1, 1),
    _Hh3cCBQoSIfApplyPolicyIfIndex_Type()
)
hh3cCBQoSIfApplyPolicyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyIfIndex.setStatus("current")
_Hh3cCBQoSIfApplyPolicyDirection_Type = DirectionType
_Hh3cCBQoSIfApplyPolicyDirection_Object = MibTableColumn
hh3cCBQoSIfApplyPolicyDirection = _Hh3cCBQoSIfApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1, 1, 2),
    _Hh3cCBQoSIfApplyPolicyDirection_Type()
)
hh3cCBQoSIfApplyPolicyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyDirection.setStatus("current")


class _Hh3cCBQoSIfApplyPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSIfApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSIfApplyPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSIfApplyPolicyName_Object = MibTableColumn
hh3cCBQoSIfApplyPolicyName = _Hh3cCBQoSIfApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1, 1, 3),
    _Hh3cCBQoSIfApplyPolicyName_Type()
)
hh3cCBQoSIfApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyName.setStatus("current")


class _Hh3cCBQoSIfApplyPolicyEnableDynamic_Type(Integer32):
    """Custom type hh3cCBQoSIfApplyPolicyEnableDynamic based on Integer32"""
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


_Hh3cCBQoSIfApplyPolicyEnableDynamic_Type.__name__ = "Integer32"
_Hh3cCBQoSIfApplyPolicyEnableDynamic_Object = MibTableColumn
hh3cCBQoSIfApplyPolicyEnableDynamic = _Hh3cCBQoSIfApplyPolicyEnableDynamic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1, 1, 4),
    _Hh3cCBQoSIfApplyPolicyEnableDynamic_Type()
)
hh3cCBQoSIfApplyPolicyEnableDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyEnableDynamic.setStatus("current")
_Hh3cCBQoSIfApplyPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSIfApplyPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSIfApplyPolicyRowStatus = _Hh3cCBQoSIfApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 1, 1, 5),
    _Hh3cCBQoSIfApplyPolicyRowStatus_Type()
)
hh3cCBQoSIfApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSIfApplyPolicyRowStatus.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyTable_Object = MibTable
hh3cCBQoSAtmPvcApplyPolicyTable = _Hh3cCBQoSAtmPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyTable.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyEntry_Object = MibTableRow
hh3cCBQoSAtmPvcApplyPolicyEntry = _Hh3cCBQoSAtmPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1)
)
hh3cCBQoSAtmPvcApplyPolicyEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyEntry.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyIfIndex_Type = Integer32
_Hh3cCBQoSAtmPvcApplyPolicyIfIndex_Object = MibTableColumn
hh3cCBQoSAtmPvcApplyPolicyIfIndex = _Hh3cCBQoSAtmPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1, 1),
    _Hh3cCBQoSAtmPvcApplyPolicyIfIndex_Type()
)
hh3cCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyIfIndex.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyVPI_Type = Integer32
_Hh3cCBQoSAtmPvcApplyPolicyVPI_Object = MibTableColumn
hh3cCBQoSAtmPvcApplyPolicyVPI = _Hh3cCBQoSAtmPvcApplyPolicyVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1, 2),
    _Hh3cCBQoSAtmPvcApplyPolicyVPI_Type()
)
hh3cCBQoSAtmPvcApplyPolicyVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyVPI.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyVCI_Type = Integer32
_Hh3cCBQoSAtmPvcApplyPolicyVCI_Object = MibTableColumn
hh3cCBQoSAtmPvcApplyPolicyVCI = _Hh3cCBQoSAtmPvcApplyPolicyVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1, 3),
    _Hh3cCBQoSAtmPvcApplyPolicyVCI_Type()
)
hh3cCBQoSAtmPvcApplyPolicyVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyVCI.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyDirection_Type = DirectionType
_Hh3cCBQoSAtmPvcApplyPolicyDirection_Object = MibTableColumn
hh3cCBQoSAtmPvcApplyPolicyDirection = _Hh3cCBQoSAtmPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1, 4),
    _Hh3cCBQoSAtmPvcApplyPolicyDirection_Type()
)
hh3cCBQoSAtmPvcApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyDirection.setStatus("current")


class _Hh3cCBQoSAtmPvcApplyPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSAtmPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSAtmPvcApplyPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSAtmPvcApplyPolicyName_Object = MibTableColumn
hh3cCBQoSAtmPvcApplyPolicyName = _Hh3cCBQoSAtmPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1, 5),
    _Hh3cCBQoSAtmPvcApplyPolicyName_Type()
)
hh3cCBQoSAtmPvcApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyName.setStatus("current")
_Hh3cCBQoSAtmPvcApplyPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSAtmPvcApplyPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSAtmPvcApplyPolicyRowStatus = _Hh3cCBQoSAtmPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 2, 1, 6),
    _Hh3cCBQoSAtmPvcApplyPolicyRowStatus_Type()
)
hh3cCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcApplyPolicyRowStatus.setStatus("current")
_Hh3cCBQoSVlanApplyPolicyTable_Object = MibTable
hh3cCBQoSVlanApplyPolicyTable = _Hh3cCBQoSVlanApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPolicyTable.setStatus("current")
_Hh3cCBQoSVlanApplyPolicyEntry_Object = MibTableRow
hh3cCBQoSVlanApplyPolicyEntry = _Hh3cCBQoSVlanApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3, 1)
)
hh3cCBQoSVlanApplyPolicyEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyVlanid"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPolicyEntry.setStatus("current")
_Hh3cCBQoSVlanApplyPolicyVlanid_Type = Integer32
_Hh3cCBQoSVlanApplyPolicyVlanid_Object = MibTableColumn
hh3cCBQoSVlanApplyPolicyVlanid = _Hh3cCBQoSVlanApplyPolicyVlanid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3, 1, 1),
    _Hh3cCBQoSVlanApplyPolicyVlanid_Type()
)
hh3cCBQoSVlanApplyPolicyVlanid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPolicyVlanid.setStatus("current")
_Hh3cCBQoSVlanApplyPolicyDirection_Type = DirectionType
_Hh3cCBQoSVlanApplyPolicyDirection_Object = MibTableColumn
hh3cCBQoSVlanApplyPolicyDirection = _Hh3cCBQoSVlanApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3, 1, 2),
    _Hh3cCBQoSVlanApplyPolicyDirection_Type()
)
hh3cCBQoSVlanApplyPolicyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPolicyDirection.setStatus("current")


class _Hh3cCBQoSVlanApplyPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSVlanApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCBQoSVlanApplyPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSVlanApplyPolicyName_Object = MibTableColumn
hh3cCBQoSVlanApplyPolicyName = _Hh3cCBQoSVlanApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3, 1, 3),
    _Hh3cCBQoSVlanApplyPolicyName_Type()
)
hh3cCBQoSVlanApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPolicyName.setStatus("current")


class _Hh3cCBQoSVlanApplyPriority_Type(Integer32):
    """Custom type hh3cCBQoSVlanApplyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hh3cCBQoSVlanApplyPriority_Type.__name__ = "Integer32"
_Hh3cCBQoSVlanApplyPriority_Object = MibTableColumn
hh3cCBQoSVlanApplyPriority = _Hh3cCBQoSVlanApplyPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3, 1, 4),
    _Hh3cCBQoSVlanApplyPriority_Type()
)
hh3cCBQoSVlanApplyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPriority.setStatus("current")
_Hh3cCBQoSVlanApplyPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSVlanApplyPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSVlanApplyPolicyRowStatus = _Hh3cCBQoSVlanApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 3, 1, 5),
    _Hh3cCBQoSVlanApplyPolicyRowStatus_Type()
)
hh3cCBQoSVlanApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyPolicyRowStatus.setStatus("current")
_Hh3cCBQoSFrClassApplyPolicyTable_Object = MibTable
hh3cCBQoSFrClassApplyPolicyTable = _Hh3cCBQoSFrClassApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrClassApplyPolicyTable.setStatus("current")
_Hh3cCBQoSFrClassApplyPolicyEntry_Object = MibTableRow
hh3cCBQoSFrClassApplyPolicyEntry = _Hh3cCBQoSFrClassApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 4, 1)
)
hh3cCBQoSFrClassApplyPolicyEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrClassApplyPolicyFrClassName"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrClassApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrClassApplyPolicyEntry.setStatus("current")


class _Hh3cCBQoSFrClassApplyPolicyFrClassName_Type(OctetString):
    """Custom type hh3cCBQoSFrClassApplyPolicyFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSFrClassApplyPolicyFrClassName_Type.__name__ = "OctetString"
_Hh3cCBQoSFrClassApplyPolicyFrClassName_Object = MibTableColumn
hh3cCBQoSFrClassApplyPolicyFrClassName = _Hh3cCBQoSFrClassApplyPolicyFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 4, 1, 1),
    _Hh3cCBQoSFrClassApplyPolicyFrClassName_Type()
)
hh3cCBQoSFrClassApplyPolicyFrClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSFrClassApplyPolicyFrClassName.setStatus("current")
_Hh3cCBQoSFrClassApplyPolicyDirection_Type = DirectionType
_Hh3cCBQoSFrClassApplyPolicyDirection_Object = MibTableColumn
hh3cCBQoSFrClassApplyPolicyDirection = _Hh3cCBQoSFrClassApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 4, 1, 2),
    _Hh3cCBQoSFrClassApplyPolicyDirection_Type()
)
hh3cCBQoSFrClassApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSFrClassApplyPolicyDirection.setStatus("current")


class _Hh3cCBQoSFrClassApplyPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSFrClassApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSFrClassApplyPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSFrClassApplyPolicyName_Object = MibTableColumn
hh3cCBQoSFrClassApplyPolicyName = _Hh3cCBQoSFrClassApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 4, 1, 3),
    _Hh3cCBQoSFrClassApplyPolicyName_Type()
)
hh3cCBQoSFrClassApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSFrClassApplyPolicyName.setStatus("current")
_Hh3cCBQoSFrClassApplyPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSFrClassApplyPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSFrClassApplyPolicyRowStatus = _Hh3cCBQoSFrClassApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 4, 1, 4),
    _Hh3cCBQoSFrClassApplyPolicyRowStatus_Type()
)
hh3cCBQoSFrClassApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSFrClassApplyPolicyRowStatus.setStatus("current")
_Hh3cCBQoSFrPvcApplyPolicyTable_Object = MibTable
hh3cCBQoSFrPvcApplyPolicyTable = _Hh3cCBQoSFrPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyTable.setStatus("current")
_Hh3cCBQoSFrPvcApplyPolicyEntry_Object = MibTableRow
hh3cCBQoSFrPvcApplyPolicyEntry = _Hh3cCBQoSFrPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5, 1)
)
hh3cCBQoSFrPvcApplyPolicyEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyEntry.setStatus("current")
_Hh3cCBQoSFrPvcApplyPolicyIfIndex_Type = Integer32
_Hh3cCBQoSFrPvcApplyPolicyIfIndex_Object = MibTableColumn
hh3cCBQoSFrPvcApplyPolicyIfIndex = _Hh3cCBQoSFrPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5, 1, 1),
    _Hh3cCBQoSFrPvcApplyPolicyIfIndex_Type()
)
hh3cCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyIfIndex.setStatus("current")


class _Hh3cCBQoSFrPvcApplyPolicyDlciNum_Type(Integer32):
    """Custom type hh3cCBQoSFrPvcApplyPolicyDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Hh3cCBQoSFrPvcApplyPolicyDlciNum_Type.__name__ = "Integer32"
_Hh3cCBQoSFrPvcApplyPolicyDlciNum_Object = MibTableColumn
hh3cCBQoSFrPvcApplyPolicyDlciNum = _Hh3cCBQoSFrPvcApplyPolicyDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5, 1, 2),
    _Hh3cCBQoSFrPvcApplyPolicyDlciNum_Type()
)
hh3cCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyDlciNum.setStatus("current")
_Hh3cCBQoSFrPvcApplyPolicyDirection_Type = DirectionType
_Hh3cCBQoSFrPvcApplyPolicyDirection_Object = MibTableColumn
hh3cCBQoSFrPvcApplyPolicyDirection = _Hh3cCBQoSFrPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5, 1, 3),
    _Hh3cCBQoSFrPvcApplyPolicyDirection_Type()
)
hh3cCBQoSFrPvcApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyDirection.setStatus("current")


class _Hh3cCBQoSFrPvcApplyPolicyName_Type(OctetString):
    """Custom type hh3cCBQoSFrPvcApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSFrPvcApplyPolicyName_Type.__name__ = "OctetString"
_Hh3cCBQoSFrPvcApplyPolicyName_Object = MibTableColumn
hh3cCBQoSFrPvcApplyPolicyName = _Hh3cCBQoSFrPvcApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5, 1, 4),
    _Hh3cCBQoSFrPvcApplyPolicyName_Type()
)
hh3cCBQoSFrPvcApplyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyName.setStatus("current")
_Hh3cCBQoSFrPvcApplyPolicyRowStatus_Type = RowStatus
_Hh3cCBQoSFrPvcApplyPolicyRowStatus_Object = MibTableColumn
hh3cCBQoSFrPvcApplyPolicyRowStatus = _Hh3cCBQoSFrPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 5, 1, 5),
    _Hh3cCBQoSFrPvcApplyPolicyRowStatus_Type()
)
hh3cCBQoSFrPvcApplyPolicyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcApplyPolicyRowStatus.setStatus("current")
_Hh3cCBQoSGlobalApplyTable_Object = MibTable
hh3cCBQoSGlobalApplyTable = _Hh3cCBQoSGlobalApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hh3cCBQoSGlobalApplyTable.setStatus("current")
_Hh3cCBQoSGlobalApplyEntry_Object = MibTableRow
hh3cCBQoSGlobalApplyEntry = _Hh3cCBQoSGlobalApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 6, 1)
)
hh3cCBQoSGlobalApplyEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSGlobalApplyDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSGlobalApplyEntry.setStatus("current")
_Hh3cCBQoSGlobalApplyDirection_Type = DirectionType
_Hh3cCBQoSGlobalApplyDirection_Object = MibTableColumn
hh3cCBQoSGlobalApplyDirection = _Hh3cCBQoSGlobalApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 6, 1, 1),
    _Hh3cCBQoSGlobalApplyDirection_Type()
)
hh3cCBQoSGlobalApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSGlobalApplyDirection.setStatus("current")


class _Hh3cCBQoSGlobalApplyName_Type(OctetString):
    """Custom type hh3cCBQoSGlobalApplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cCBQoSGlobalApplyName_Type.__name__ = "OctetString"
_Hh3cCBQoSGlobalApplyName_Object = MibTableColumn
hh3cCBQoSGlobalApplyName = _Hh3cCBQoSGlobalApplyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 6, 1, 2),
    _Hh3cCBQoSGlobalApplyName_Type()
)
hh3cCBQoSGlobalApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGlobalApplyName.setStatus("current")
_Hh3cCBQoSGlobalApplyRowStatus_Type = RowStatus
_Hh3cCBQoSGlobalApplyRowStatus_Object = MibTableColumn
hh3cCBQoSGlobalApplyRowStatus = _Hh3cCBQoSGlobalApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 4, 6, 1, 3),
    _Hh3cCBQoSGlobalApplyRowStatus_Type()
)
hh3cCBQoSGlobalApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCBQoSGlobalApplyRowStatus.setStatus("current")
_Hh3cCBQoSApplyPolicyStaticsObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSApplyPolicyStaticsObjects = _Hh3cCBQoSApplyPolicyStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5)
)
_Hh3cCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSIfStaticsObjects = _Hh3cCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1)
)
_Hh3cCBQoSIfCbqRunInfoTable_Object = MibTable
hh3cCBQoSIfCbqRunInfoTable = _Hh3cCBQoSIfCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqRunInfoTable.setStatus("current")
_Hh3cCBQoSIfCbqRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfCbqRunInfoEntry = _Hh3cCBQoSIfCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1)
)
hh3cCBQoSIfCbqRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfCbqQueueSize_Type = Integer32
_Hh3cCBQoSIfCbqQueueSize_Object = MibTableColumn
hh3cCBQoSIfCbqQueueSize = _Hh3cCBQoSIfCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 1),
    _Hh3cCBQoSIfCbqQueueSize_Type()
)
hh3cCBQoSIfCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqQueueSize.setStatus("current")
_Hh3cCBQoSIfCbqDiscard_Type = Counter64
_Hh3cCBQoSIfCbqDiscard_Object = MibTableColumn
hh3cCBQoSIfCbqDiscard = _Hh3cCBQoSIfCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 2),
    _Hh3cCBQoSIfCbqDiscard_Type()
)
hh3cCBQoSIfCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqDiscard.setStatus("current")
_Hh3cCBQoSIfCbqEfQueueSize_Type = Integer32
_Hh3cCBQoSIfCbqEfQueueSize_Object = MibTableColumn
hh3cCBQoSIfCbqEfQueueSize = _Hh3cCBQoSIfCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 3),
    _Hh3cCBQoSIfCbqEfQueueSize_Type()
)
hh3cCBQoSIfCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqEfQueueSize.setStatus("current")
_Hh3cCBQoSIfCbqAfQueueSize_Type = Integer32
_Hh3cCBQoSIfCbqAfQueueSize_Object = MibTableColumn
hh3cCBQoSIfCbqAfQueueSize = _Hh3cCBQoSIfCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 4),
    _Hh3cCBQoSIfCbqAfQueueSize_Type()
)
hh3cCBQoSIfCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqAfQueueSize.setStatus("current")
_Hh3cCBQoSIfCbqBeQueueSize_Type = Integer32
_Hh3cCBQoSIfCbqBeQueueSize_Object = MibTableColumn
hh3cCBQoSIfCbqBeQueueSize = _Hh3cCBQoSIfCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 5),
    _Hh3cCBQoSIfCbqBeQueueSize_Type()
)
hh3cCBQoSIfCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqBeQueueSize.setStatus("current")
_Hh3cCBQoSIfCbqBeActiveQueueNum_Type = Integer32
_Hh3cCBQoSIfCbqBeActiveQueueNum_Object = MibTableColumn
hh3cCBQoSIfCbqBeActiveQueueNum = _Hh3cCBQoSIfCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 6),
    _Hh3cCBQoSIfCbqBeActiveQueueNum_Type()
)
hh3cCBQoSIfCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqBeActiveQueueNum.setStatus("current")
_Hh3cCBQoSIfCbqBeMaxActiveQueueNum_Type = Integer32
_Hh3cCBQoSIfCbqBeMaxActiveQueueNum_Object = MibTableColumn
hh3cCBQoSIfCbqBeMaxActiveQueueNum = _Hh3cCBQoSIfCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 7),
    _Hh3cCBQoSIfCbqBeMaxActiveQueueNum_Type()
)
hh3cCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqBeMaxActiveQueueNum.setStatus("current")
_Hh3cCBQoSIfCbqBeTotalQueueNum_Type = Integer32
_Hh3cCBQoSIfCbqBeTotalQueueNum_Object = MibTableColumn
hh3cCBQoSIfCbqBeTotalQueueNum = _Hh3cCBQoSIfCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 8),
    _Hh3cCBQoSIfCbqBeTotalQueueNum_Type()
)
hh3cCBQoSIfCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqBeTotalQueueNum.setStatus("current")
_Hh3cCBQoSIfCbqAfAllocatedQueueNum_Type = Integer32
_Hh3cCBQoSIfCbqAfAllocatedQueueNum_Object = MibTableColumn
hh3cCBQoSIfCbqAfAllocatedQueueNum = _Hh3cCBQoSIfCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 1, 1, 9),
    _Hh3cCBQoSIfCbqAfAllocatedQueueNum_Type()
)
hh3cCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCbqAfAllocatedQueueNum.setStatus("current")
_Hh3cCBQoSIfClassMatchRunInfoTable_Object = MibTable
hh3cCBQoSIfClassMatchRunInfoTable = _Hh3cCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfClassMatchRunInfoTable.setStatus("current")
_Hh3cCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfClassMatchRunInfoEntry = _Hh3cCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 2, 1)
)
hh3cCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfClassMatchedPackets_Type = Counter64
_Hh3cCBQoSIfClassMatchedPackets_Object = MibTableColumn
hh3cCBQoSIfClassMatchedPackets = _Hh3cCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 2, 1, 1),
    _Hh3cCBQoSIfClassMatchedPackets_Type()
)
hh3cCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfClassMatchedPackets.setStatus("current")
_Hh3cCBQoSIfClassMatchedBytes_Type = Counter64
_Hh3cCBQoSIfClassMatchedBytes_Object = MibTableColumn
hh3cCBQoSIfClassMatchedBytes = _Hh3cCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 2, 1, 2),
    _Hh3cCBQoSIfClassMatchedBytes_Type()
)
hh3cCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfClassMatchedBytes.setStatus("current")
_Hh3cCBQoSIfClassAverageRate_Type = Counter64
_Hh3cCBQoSIfClassAverageRate_Object = MibTableColumn
hh3cCBQoSIfClassAverageRate = _Hh3cCBQoSIfClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 2, 1, 3),
    _Hh3cCBQoSIfClassAverageRate_Type()
)
hh3cCBQoSIfClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfClassAverageRate.setStatus("current")
_Hh3cCBQoSIfCarRunInfoTable_Object = MibTable
hh3cCBQoSIfCarRunInfoTable = _Hh3cCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarRunInfoTable.setStatus("current")
_Hh3cCBQoSIfCarRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfCarRunInfoEntry = _Hh3cCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1)
)
hh3cCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfCarGreenPackets_Type = Counter64
_Hh3cCBQoSIfCarGreenPackets_Object = MibTableColumn
hh3cCBQoSIfCarGreenPackets = _Hh3cCBQoSIfCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1, 1),
    _Hh3cCBQoSIfCarGreenPackets_Type()
)
hh3cCBQoSIfCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarGreenPackets.setStatus("current")
_Hh3cCBQoSIfCarGreenBytes_Type = Counter64
_Hh3cCBQoSIfCarGreenBytes_Object = MibTableColumn
hh3cCBQoSIfCarGreenBytes = _Hh3cCBQoSIfCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1, 2),
    _Hh3cCBQoSIfCarGreenBytes_Type()
)
hh3cCBQoSIfCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarGreenBytes.setStatus("current")
_Hh3cCBQoSIfCarRedPackets_Type = Counter64
_Hh3cCBQoSIfCarRedPackets_Object = MibTableColumn
hh3cCBQoSIfCarRedPackets = _Hh3cCBQoSIfCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1, 3),
    _Hh3cCBQoSIfCarRedPackets_Type()
)
hh3cCBQoSIfCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarRedPackets.setStatus("current")
_Hh3cCBQoSIfCarRedBytes_Type = Counter64
_Hh3cCBQoSIfCarRedBytes_Object = MibTableColumn
hh3cCBQoSIfCarRedBytes = _Hh3cCBQoSIfCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1, 4),
    _Hh3cCBQoSIfCarRedBytes_Type()
)
hh3cCBQoSIfCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarRedBytes.setStatus("current")
_Hh3cCBQoSIfCarYellowPackets_Type = Counter64
_Hh3cCBQoSIfCarYellowPackets_Object = MibTableColumn
hh3cCBQoSIfCarYellowPackets = _Hh3cCBQoSIfCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1, 5),
    _Hh3cCBQoSIfCarYellowPackets_Type()
)
hh3cCBQoSIfCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarYellowPackets.setStatus("current")
_Hh3cCBQoSIfCarYellowBytes_Type = Counter64
_Hh3cCBQoSIfCarYellowBytes_Object = MibTableColumn
hh3cCBQoSIfCarYellowBytes = _Hh3cCBQoSIfCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 3, 1, 6),
    _Hh3cCBQoSIfCarYellowBytes_Type()
)
hh3cCBQoSIfCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfCarYellowBytes.setStatus("current")
_Hh3cCBQoSIfGtsRunInfoTable_Object = MibTable
hh3cCBQoSIfGtsRunInfoTable = _Hh3cCBQoSIfGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsRunInfoTable.setStatus("current")
_Hh3cCBQoSIfGtsRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfGtsRunInfoEntry = _Hh3cCBQoSIfGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1)
)
hh3cCBQoSIfGtsRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfGtsPassedPackets_Type = Counter64
_Hh3cCBQoSIfGtsPassedPackets_Object = MibTableColumn
hh3cCBQoSIfGtsPassedPackets = _Hh3cCBQoSIfGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 1),
    _Hh3cCBQoSIfGtsPassedPackets_Type()
)
hh3cCBQoSIfGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsPassedPackets.setStatus("current")
_Hh3cCBQoSIfGtsPassedBytes_Type = Counter64
_Hh3cCBQoSIfGtsPassedBytes_Object = MibTableColumn
hh3cCBQoSIfGtsPassedBytes = _Hh3cCBQoSIfGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 2),
    _Hh3cCBQoSIfGtsPassedBytes_Type()
)
hh3cCBQoSIfGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsPassedBytes.setStatus("current")
_Hh3cCBQoSIfGtsDiscardedPackets_Type = Counter64
_Hh3cCBQoSIfGtsDiscardedPackets_Object = MibTableColumn
hh3cCBQoSIfGtsDiscardedPackets = _Hh3cCBQoSIfGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 3),
    _Hh3cCBQoSIfGtsDiscardedPackets_Type()
)
hh3cCBQoSIfGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsDiscardedPackets.setStatus("current")
_Hh3cCBQoSIfGtsDiscardedBytes_Type = Counter64
_Hh3cCBQoSIfGtsDiscardedBytes_Object = MibTableColumn
hh3cCBQoSIfGtsDiscardedBytes = _Hh3cCBQoSIfGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 4),
    _Hh3cCBQoSIfGtsDiscardedBytes_Type()
)
hh3cCBQoSIfGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsDiscardedBytes.setStatus("current")
_Hh3cCBQoSIfGtsDelayedPackets_Type = Counter64
_Hh3cCBQoSIfGtsDelayedPackets_Object = MibTableColumn
hh3cCBQoSIfGtsDelayedPackets = _Hh3cCBQoSIfGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 5),
    _Hh3cCBQoSIfGtsDelayedPackets_Type()
)
hh3cCBQoSIfGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsDelayedPackets.setStatus("current")
_Hh3cCBQoSIfGtsDelayedBytes_Type = Counter64
_Hh3cCBQoSIfGtsDelayedBytes_Object = MibTableColumn
hh3cCBQoSIfGtsDelayedBytes = _Hh3cCBQoSIfGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 6),
    _Hh3cCBQoSIfGtsDelayedBytes_Type()
)
hh3cCBQoSIfGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsDelayedBytes.setStatus("current")
_Hh3cCBQoSIfGtsQueueSize_Type = Integer32
_Hh3cCBQoSIfGtsQueueSize_Object = MibTableColumn
hh3cCBQoSIfGtsQueueSize = _Hh3cCBQoSIfGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 4, 1, 7),
    _Hh3cCBQoSIfGtsQueueSize_Type()
)
hh3cCBQoSIfGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfGtsQueueSize.setStatus("current")
_Hh3cCBQoSIfRemarkRunInfoTable_Object = MibTable
hh3cCBQoSIfRemarkRunInfoTable = _Hh3cCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfRemarkRunInfoTable.setStatus("current")
_Hh3cCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfRemarkRunInfoEntry = _Hh3cCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 5, 1)
)
hh3cCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfRemarkRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfRemarkedPackets_Type = Counter64
_Hh3cCBQoSIfRemarkedPackets_Object = MibTableColumn
hh3cCBQoSIfRemarkedPackets = _Hh3cCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 5, 1, 1),
    _Hh3cCBQoSIfRemarkedPackets_Type()
)
hh3cCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfRemarkedPackets.setStatus("current")
_Hh3cCBQoSIfQueueRunInfoTable_Object = MibTable
hh3cCBQoSIfQueueRunInfoTable = _Hh3cCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueRunInfoTable.setStatus("current")
_Hh3cCBQoSIfQueueRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfQueueRunInfoEntry = _Hh3cCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1)
)
hh3cCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfQueueMatchedPackets_Type = Counter64
_Hh3cCBQoSIfQueueMatchedPackets_Object = MibTableColumn
hh3cCBQoSIfQueueMatchedPackets = _Hh3cCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1, 1),
    _Hh3cCBQoSIfQueueMatchedPackets_Type()
)
hh3cCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueMatchedPackets.setStatus("current")
_Hh3cCBQoSIfQueueMatchedBytes_Type = Counter64
_Hh3cCBQoSIfQueueMatchedBytes_Object = MibTableColumn
hh3cCBQoSIfQueueMatchedBytes = _Hh3cCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1, 2),
    _Hh3cCBQoSIfQueueMatchedBytes_Type()
)
hh3cCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueMatchedBytes.setStatus("current")
_Hh3cCBQoSIfQueueEnqueuedPackets_Type = Counter64
_Hh3cCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
hh3cCBQoSIfQueueEnqueuedPackets = _Hh3cCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1, 3),
    _Hh3cCBQoSIfQueueEnqueuedPackets_Type()
)
hh3cCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueEnqueuedPackets.setStatus("current")
_Hh3cCBQoSIfQueueEnqueuedBytes_Type = Counter64
_Hh3cCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
hh3cCBQoSIfQueueEnqueuedBytes = _Hh3cCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1, 4),
    _Hh3cCBQoSIfQueueEnqueuedBytes_Type()
)
hh3cCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueEnqueuedBytes.setStatus("current")
_Hh3cCBQoSIfQueueDiscardedPackets_Type = Counter64
_Hh3cCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
hh3cCBQoSIfQueueDiscardedPackets = _Hh3cCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1, 5),
    _Hh3cCBQoSIfQueueDiscardedPackets_Type()
)
hh3cCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueDiscardedPackets.setStatus("current")
_Hh3cCBQoSIfQueueDiscardedBytes_Type = Counter64
_Hh3cCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
hh3cCBQoSIfQueueDiscardedBytes = _Hh3cCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 6, 1, 6),
    _Hh3cCBQoSIfQueueDiscardedBytes_Type()
)
hh3cCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfQueueDiscardedBytes.setStatus("current")
_Hh3cCBQoSIfWredRunInfoTable_Object = MibTable
hh3cCBQoSIfWredRunInfoTable = _Hh3cCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfWredRunInfoTable.setStatus("current")
_Hh3cCBQoSIfWredRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfWredRunInfoEntry = _Hh3cCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 7, 1)
)
hh3cCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfWredRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfWredRandomDiscardedPackets_Type = Counter64
_Hh3cCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
hh3cCBQoSIfWredRandomDiscardedPackets = _Hh3cCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 7, 1, 1),
    _Hh3cCBQoSIfWredRandomDiscardedPackets_Type()
)
hh3cCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_Hh3cCBQoSIfWredTailDiscardedPackets_Type = Counter64
_Hh3cCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
hh3cCBQoSIfWredTailDiscardedPackets = _Hh3cCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 7, 1, 2),
    _Hh3cCBQoSIfWredTailDiscardedPackets_Type()
)
hh3cCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfWredTailDiscardedPackets.setStatus("current")
_Hh3cCBQoSIfAccountingRunInfoTable_Object = MibTable
hh3cCBQoSIfAccountingRunInfoTable = _Hh3cCBQoSIfAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfAccountingRunInfoTable.setStatus("current")
_Hh3cCBQoSIfAccountingRunInfoEntry_Object = MibTableRow
hh3cCBQoSIfAccountingRunInfoEntry = _Hh3cCBQoSIfAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 8, 1)
)
hh3cCBQoSIfAccountingRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfAccountingRunInfoEntry.setStatus("current")
_Hh3cCBQoSIfAccountingPackets_Type = Counter64
_Hh3cCBQoSIfAccountingPackets_Object = MibTableColumn
hh3cCBQoSIfAccountingPackets = _Hh3cCBQoSIfAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 8, 1, 1),
    _Hh3cCBQoSIfAccountingPackets_Type()
)
hh3cCBQoSIfAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfAccountingPackets.setStatus("current")
_Hh3cCBQoSIfAccountingBytes_Type = Counter64
_Hh3cCBQoSIfAccountingBytes_Object = MibTableColumn
hh3cCBQoSIfAccountingBytes = _Hh3cCBQoSIfAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 1, 8, 1, 2),
    _Hh3cCBQoSIfAccountingBytes_Type()
)
hh3cCBQoSIfAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIfAccountingBytes.setStatus("current")
_Hh3cCBQoSAtmPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSAtmPvcStaticsObjects = _Hh3cCBQoSAtmPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2)
)
_Hh3cCBQoSAtmPvcCbqRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcCbqRunInfoTable = _Hh3cCBQoSAtmPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcCbqRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcCbqRunInfoEntry = _Hh3cCBQoSAtmPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1)
)
hh3cCBQoSAtmPvcCbqRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcCbqQueueSize_Type = Integer32
_Hh3cCBQoSAtmPvcCbqQueueSize_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqQueueSize = _Hh3cCBQoSAtmPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 1),
    _Hh3cCBQoSAtmPvcCbqQueueSize_Type()
)
hh3cCBQoSAtmPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqQueueSize.setStatus("current")
_Hh3cCBQoSAtmPvcCbqDiscard_Type = Counter64
_Hh3cCBQoSAtmPvcCbqDiscard_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqDiscard = _Hh3cCBQoSAtmPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 2),
    _Hh3cCBQoSAtmPvcCbqDiscard_Type()
)
hh3cCBQoSAtmPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqDiscard.setStatus("current")
_Hh3cCBQoSAtmPvcCbqEfQueueSize_Type = Integer32
_Hh3cCBQoSAtmPvcCbqEfQueueSize_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqEfQueueSize = _Hh3cCBQoSAtmPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 3),
    _Hh3cCBQoSAtmPvcCbqEfQueueSize_Type()
)
hh3cCBQoSAtmPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqEfQueueSize.setStatus("current")
_Hh3cCBQoSAtmPvcCbqAfQueueSize_Type = Integer32
_Hh3cCBQoSAtmPvcCbqAfQueueSize_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqAfQueueSize = _Hh3cCBQoSAtmPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 4),
    _Hh3cCBQoSAtmPvcCbqAfQueueSize_Type()
)
hh3cCBQoSAtmPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqAfQueueSize.setStatus("current")
_Hh3cCBQoSAtmPvcCbqBeQueueSize_Type = Integer32
_Hh3cCBQoSAtmPvcCbqBeQueueSize_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqBeQueueSize = _Hh3cCBQoSAtmPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 5),
    _Hh3cCBQoSAtmPvcCbqBeQueueSize_Type()
)
hh3cCBQoSAtmPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqBeQueueSize.setStatus("current")
_Hh3cCBQoSAtmPvcCbqBeActiveQueueNum_Type = Integer32
_Hh3cCBQoSAtmPvcCbqBeActiveQueueNum_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqBeActiveQueueNum = _Hh3cCBQoSAtmPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 6),
    _Hh3cCBQoSAtmPvcCbqBeActiveQueueNum_Type()
)
hh3cCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqBeActiveQueueNum.setStatus("current")
_Hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type = Integer32
_Hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum = _Hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 7),
    _Hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type()
)
hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus("current")
_Hh3cCBQoSAtmPvcCbqBeTotalQueueNum_Type = Integer32
_Hh3cCBQoSAtmPvcCbqBeTotalQueueNum_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqBeTotalQueueNum = _Hh3cCBQoSAtmPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 8),
    _Hh3cCBQoSAtmPvcCbqBeTotalQueueNum_Type()
)
hh3cCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqBeTotalQueueNum.setStatus("current")
_Hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Type = Integer32
_Hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum = _Hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 1, 1, 9),
    _Hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum_Type()
)
hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus("current")
_Hh3cCBQoSAtmPvcClassMatchRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcClassMatchRunInfoTable = _Hh3cCBQoSAtmPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcClassMatchRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcClassMatchRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcClassMatchRunInfoEntry = _Hh3cCBQoSAtmPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 2, 1)
)
hh3cCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcClassMatchRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcClassMatchPackets_Type = Counter64
_Hh3cCBQoSAtmPvcClassMatchPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcClassMatchPackets = _Hh3cCBQoSAtmPvcClassMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 2, 1, 1),
    _Hh3cCBQoSAtmPvcClassMatchPackets_Type()
)
hh3cCBQoSAtmPvcClassMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcClassMatchPackets.setStatus("current")
_Hh3cCBQoSAtmPvcClassMatchBytes_Type = Counter64
_Hh3cCBQoSAtmPvcClassMatchBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcClassMatchBytes = _Hh3cCBQoSAtmPvcClassMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 2, 1, 2),
    _Hh3cCBQoSAtmPvcClassMatchBytes_Type()
)
hh3cCBQoSAtmPvcClassMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcClassMatchBytes.setStatus("current")
_Hh3cCBQoSAtmPvcClassAverageRate_Type = Integer32
_Hh3cCBQoSAtmPvcClassAverageRate_Object = MibTableColumn
hh3cCBQoSAtmPvcClassAverageRate = _Hh3cCBQoSAtmPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 2, 1, 3),
    _Hh3cCBQoSAtmPvcClassAverageRate_Type()
)
hh3cCBQoSAtmPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcClassAverageRate.setStatus("current")
_Hh3cCBQoSAtmPvcCarRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcCarRunInfoTable = _Hh3cCBQoSAtmPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCarRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcCarRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcCarRunInfoEntry = _Hh3cCBQoSAtmPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 3, 1)
)
hh3cCBQoSAtmPvcCarRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCarRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcCarConformPackets_Type = Counter64
_Hh3cCBQoSAtmPvcCarConformPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcCarConformPackets = _Hh3cCBQoSAtmPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 3, 1, 1),
    _Hh3cCBQoSAtmPvcCarConformPackets_Type()
)
hh3cCBQoSAtmPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCarConformPackets.setStatus("current")
_Hh3cCBQoSAtmPvcCarConformBytes_Type = Counter64
_Hh3cCBQoSAtmPvcCarConformBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcCarConformBytes = _Hh3cCBQoSAtmPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 3, 1, 2),
    _Hh3cCBQoSAtmPvcCarConformBytes_Type()
)
hh3cCBQoSAtmPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCarConformBytes.setStatus("current")
_Hh3cCBQoSAtmPvcCarExceedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcCarExceedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcCarExceedPackets = _Hh3cCBQoSAtmPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 3, 1, 3),
    _Hh3cCBQoSAtmPvcCarExceedPackets_Type()
)
hh3cCBQoSAtmPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCarExceedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcCarExceedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcCarExceedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcCarExceedBytes = _Hh3cCBQoSAtmPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 3, 1, 4),
    _Hh3cCBQoSAtmPvcCarExceedBytes_Type()
)
hh3cCBQoSAtmPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcCarExceedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcGtsRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcGtsRunInfoTable = _Hh3cCBQoSAtmPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcGtsRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcGtsRunInfoEntry = _Hh3cCBQoSAtmPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1)
)
hh3cCBQoSAtmPvcGtsRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcGtsPassedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcGtsPassedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsPassedPackets = _Hh3cCBQoSAtmPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 1),
    _Hh3cCBQoSAtmPvcGtsPassedPackets_Type()
)
hh3cCBQoSAtmPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsPassedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcGtsPassedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcGtsPassedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsPassedBytes = _Hh3cCBQoSAtmPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 2),
    _Hh3cCBQoSAtmPvcGtsPassedBytes_Type()
)
hh3cCBQoSAtmPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsPassedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcGtsDiscardedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcGtsDiscardedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsDiscardedPackets = _Hh3cCBQoSAtmPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 3),
    _Hh3cCBQoSAtmPvcGtsDiscardedPackets_Type()
)
hh3cCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsDiscardedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcGtsDiscardedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcGtsDiscardedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsDiscardedBytes = _Hh3cCBQoSAtmPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 4),
    _Hh3cCBQoSAtmPvcGtsDiscardedBytes_Type()
)
hh3cCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsDiscardedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcGtsDelayedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcGtsDelayedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsDelayedPackets = _Hh3cCBQoSAtmPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 5),
    _Hh3cCBQoSAtmPvcGtsDelayedPackets_Type()
)
hh3cCBQoSAtmPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsDelayedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcGtsDelayedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcGtsDelayedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsDelayedBytes = _Hh3cCBQoSAtmPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 6),
    _Hh3cCBQoSAtmPvcGtsDelayedBytes_Type()
)
hh3cCBQoSAtmPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsDelayedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcGtsQueueSize_Type = Integer32
_Hh3cCBQoSAtmPvcGtsQueueSize_Object = MibTableColumn
hh3cCBQoSAtmPvcGtsQueueSize = _Hh3cCBQoSAtmPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 4, 1, 7),
    _Hh3cCBQoSAtmPvcGtsQueueSize_Type()
)
hh3cCBQoSAtmPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcGtsQueueSize.setStatus("current")
_Hh3cCBQoSAtmPvcRemarkRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcRemarkRunInfoTable = _Hh3cCBQoSAtmPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcRemarkRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcRemarkRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcRemarkRunInfoEntry = _Hh3cCBQoSAtmPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 5, 1)
)
hh3cCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcRemarkRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcRemarkedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcRemarkedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcRemarkedPackets = _Hh3cCBQoSAtmPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 5, 1, 1),
    _Hh3cCBQoSAtmPvcRemarkedPackets_Type()
)
hh3cCBQoSAtmPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcRemarkedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcQueueRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcQueueRunInfoTable = _Hh3cCBQoSAtmPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcQueueRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcQueueRunInfoEntry = _Hh3cCBQoSAtmPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1)
)
hh3cCBQoSAtmPvcQueueRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcQueueMatchedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcQueueMatchedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcQueueMatchedPackets = _Hh3cCBQoSAtmPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1, 1),
    _Hh3cCBQoSAtmPvcQueueMatchedPackets_Type()
)
hh3cCBQoSAtmPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueMatchedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcQueueMatchedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcQueueMatchedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcQueueMatchedBytes = _Hh3cCBQoSAtmPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1, 2),
    _Hh3cCBQoSAtmPvcQueueMatchedBytes_Type()
)
hh3cCBQoSAtmPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueMatchedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcQueueEnqueuedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcQueueEnqueuedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcQueueEnqueuedPackets = _Hh3cCBQoSAtmPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1, 3),
    _Hh3cCBQoSAtmPvcQueueEnqueuedPackets_Type()
)
hh3cCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueEnqueuedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcQueueEnqueuedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcQueueEnqueuedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcQueueEnqueuedBytes = _Hh3cCBQoSAtmPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1, 4),
    _Hh3cCBQoSAtmPvcQueueEnqueuedBytes_Type()
)
hh3cCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueEnqueuedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcQueueDiscardedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcQueueDiscardedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcQueueDiscardedPackets = _Hh3cCBQoSAtmPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1, 5),
    _Hh3cCBQoSAtmPvcQueueDiscardedPackets_Type()
)
hh3cCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueDiscardedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcQueueDiscardedBytes_Type = Counter64
_Hh3cCBQoSAtmPvcQueueDiscardedBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcQueueDiscardedBytes = _Hh3cCBQoSAtmPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 6, 1, 6),
    _Hh3cCBQoSAtmPvcQueueDiscardedBytes_Type()
)
hh3cCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcQueueDiscardedBytes.setStatus("current")
_Hh3cCBQoSAtmPvcWredRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcWredRunInfoTable = _Hh3cCBQoSAtmPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcWredRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcWredRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcWredRunInfoEntry = _Hh3cCBQoSAtmPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 7, 1)
)
hh3cCBQoSAtmPvcWredRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcWredRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcWredRandomDiscardedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcWredRandomDiscardedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcWredRandomDiscardedPackets = _Hh3cCBQoSAtmPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 7, 1, 1),
    _Hh3cCBQoSAtmPvcWredRandomDiscardedPackets_Type()
)
hh3cCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcWredRandomDiscardedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcWredTailDiscardedPackets_Type = Counter64
_Hh3cCBQoSAtmPvcWredTailDiscardedPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcWredTailDiscardedPackets = _Hh3cCBQoSAtmPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 7, 1, 2),
    _Hh3cCBQoSAtmPvcWredTailDiscardedPackets_Type()
)
hh3cCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcWredTailDiscardedPackets.setStatus("current")
_Hh3cCBQoSAtmPvcAccountingRunInfoTable_Object = MibTable
hh3cCBQoSAtmPvcAccountingRunInfoTable = _Hh3cCBQoSAtmPvcAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcAccountingRunInfoTable.setStatus("current")
_Hh3cCBQoSAtmPvcAccountingRunInfoEntry_Object = MibTableRow
hh3cCBQoSAtmPvcAccountingRunInfoEntry = _Hh3cCBQoSAtmPvcAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 8, 1)
)
hh3cCBQoSAtmPvcAccountingRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVPI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyVCI"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSAtmPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcAccountingRunInfoEntry.setStatus("current")
_Hh3cCBQoSAtmPvcAccountingPackets_Type = Counter64
_Hh3cCBQoSAtmPvcAccountingPackets_Object = MibTableColumn
hh3cCBQoSAtmPvcAccountingPackets = _Hh3cCBQoSAtmPvcAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 8, 1, 1),
    _Hh3cCBQoSAtmPvcAccountingPackets_Type()
)
hh3cCBQoSAtmPvcAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcAccountingPackets.setStatus("current")
_Hh3cCBQoSAtmPvcAccountingBytes_Type = Counter64
_Hh3cCBQoSAtmPvcAccountingBytes_Object = MibTableColumn
hh3cCBQoSAtmPvcAccountingBytes = _Hh3cCBQoSAtmPvcAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 2, 8, 1, 2),
    _Hh3cCBQoSAtmPvcAccountingBytes_Type()
)
hh3cCBQoSAtmPvcAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAtmPvcAccountingBytes.setStatus("current")
_Hh3cCBQoSFrPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSFrPvcStaticsObjects = _Hh3cCBQoSFrPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3)
)
_Hh3cCBQoSFrPvcCbqRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcCbqRunInfoTable = _Hh3cCBQoSFrPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcCbqRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcCbqRunInfoEntry = _Hh3cCBQoSFrPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1)
)
hh3cCBQoSFrPvcCbqRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcCbqQueueSize_Type = Integer32
_Hh3cCBQoSFrPvcCbqQueueSize_Object = MibTableColumn
hh3cCBQoSFrPvcCbqQueueSize = _Hh3cCBQoSFrPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 1),
    _Hh3cCBQoSFrPvcCbqQueueSize_Type()
)
hh3cCBQoSFrPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqQueueSize.setStatus("current")
_Hh3cCBQoSFrPvcCbqDiscard_Type = Counter64
_Hh3cCBQoSFrPvcCbqDiscard_Object = MibTableColumn
hh3cCBQoSFrPvcCbqDiscard = _Hh3cCBQoSFrPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 2),
    _Hh3cCBQoSFrPvcCbqDiscard_Type()
)
hh3cCBQoSFrPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqDiscard.setStatus("current")
_Hh3cCBQoSFrPvcCbqEfQueueSize_Type = Integer32
_Hh3cCBQoSFrPvcCbqEfQueueSize_Object = MibTableColumn
hh3cCBQoSFrPvcCbqEfQueueSize = _Hh3cCBQoSFrPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 3),
    _Hh3cCBQoSFrPvcCbqEfQueueSize_Type()
)
hh3cCBQoSFrPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqEfQueueSize.setStatus("current")
_Hh3cCBQoSFrPvcCbqAfQueueSize_Type = Integer32
_Hh3cCBQoSFrPvcCbqAfQueueSize_Object = MibTableColumn
hh3cCBQoSFrPvcCbqAfQueueSize = _Hh3cCBQoSFrPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 4),
    _Hh3cCBQoSFrPvcCbqAfQueueSize_Type()
)
hh3cCBQoSFrPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqAfQueueSize.setStatus("current")
_Hh3cCBQoSFrPvcCbqBeQueueSize_Type = Integer32
_Hh3cCBQoSFrPvcCbqBeQueueSize_Object = MibTableColumn
hh3cCBQoSFrPvcCbqBeQueueSize = _Hh3cCBQoSFrPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 5),
    _Hh3cCBQoSFrPvcCbqBeQueueSize_Type()
)
hh3cCBQoSFrPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqBeQueueSize.setStatus("current")
_Hh3cCBQoSFrPvcCbqBeActiveQueueNum_Type = Integer32
_Hh3cCBQoSFrPvcCbqBeActiveQueueNum_Object = MibTableColumn
hh3cCBQoSFrPvcCbqBeActiveQueueNum = _Hh3cCBQoSFrPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 6),
    _Hh3cCBQoSFrPvcCbqBeActiveQueueNum_Type()
)
hh3cCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqBeActiveQueueNum.setStatus("current")
_Hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Type = Integer32
_Hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum = _Hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 7),
    _Hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum_Type()
)
hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus("current")
_Hh3cCBQoSFrPvcCbqBeTotalQueueNum_Type = Integer32
_Hh3cCBQoSFrPvcCbqBeTotalQueueNum_Object = MibTableColumn
hh3cCBQoSFrPvcCbqBeTotalQueueNum = _Hh3cCBQoSFrPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 8),
    _Hh3cCBQoSFrPvcCbqBeTotalQueueNum_Type()
)
hh3cCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqBeTotalQueueNum.setStatus("current")
_Hh3cCBQoSFrPvcCbqAfAllocatedQueueNum_Type = Integer32
_Hh3cCBQoSFrPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hh3cCBQoSFrPvcCbqAfAllocatedQueueNum = _Hh3cCBQoSFrPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 1, 1, 9),
    _Hh3cCBQoSFrPvcCbqAfAllocatedQueueNum_Type()
)
hh3cCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus("current")
_Hh3cCBQoSFrPvcClassMatchRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcClassMatchRunInfoTable = _Hh3cCBQoSFrPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcClassMatchRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcClassMatchRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcClassMatchRunInfoEntry = _Hh3cCBQoSFrPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 2, 1)
)
hh3cCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcClassMatchRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcClassMatchedPackets_Type = Counter64
_Hh3cCBQoSFrPvcClassMatchedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcClassMatchedPackets = _Hh3cCBQoSFrPvcClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 2, 1, 1),
    _Hh3cCBQoSFrPvcClassMatchedPackets_Type()
)
hh3cCBQoSFrPvcClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcClassMatchedPackets.setStatus("current")
_Hh3cCBQoSFrPvcClassMatchedBytes_Type = Counter64
_Hh3cCBQoSFrPvcClassMatchedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcClassMatchedBytes = _Hh3cCBQoSFrPvcClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 2, 1, 2),
    _Hh3cCBQoSFrPvcClassMatchedBytes_Type()
)
hh3cCBQoSFrPvcClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcClassMatchedBytes.setStatus("current")
_Hh3cCBQoSFrPvcClassAverageRate_Type = Counter64
_Hh3cCBQoSFrPvcClassAverageRate_Object = MibTableColumn
hh3cCBQoSFrPvcClassAverageRate = _Hh3cCBQoSFrPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 2, 1, 3),
    _Hh3cCBQoSFrPvcClassAverageRate_Type()
)
hh3cCBQoSFrPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcClassAverageRate.setStatus("current")
_Hh3cCBQoSFrPvcCarRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcCarRunInfoTable = _Hh3cCBQoSFrPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCarRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcCarRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcCarRunInfoEntry = _Hh3cCBQoSFrPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 3, 1)
)
hh3cCBQoSFrPvcCarRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCarRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcCarConformPackets_Type = Counter64
_Hh3cCBQoSFrPvcCarConformPackets_Object = MibTableColumn
hh3cCBQoSFrPvcCarConformPackets = _Hh3cCBQoSFrPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 3, 1, 1),
    _Hh3cCBQoSFrPvcCarConformPackets_Type()
)
hh3cCBQoSFrPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCarConformPackets.setStatus("current")
_Hh3cCBQoSFrPvcCarConformBytes_Type = Counter64
_Hh3cCBQoSFrPvcCarConformBytes_Object = MibTableColumn
hh3cCBQoSFrPvcCarConformBytes = _Hh3cCBQoSFrPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 3, 1, 2),
    _Hh3cCBQoSFrPvcCarConformBytes_Type()
)
hh3cCBQoSFrPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCarConformBytes.setStatus("current")
_Hh3cCBQoSFrPvcCarExceedPackets_Type = Counter64
_Hh3cCBQoSFrPvcCarExceedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcCarExceedPackets = _Hh3cCBQoSFrPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 3, 1, 3),
    _Hh3cCBQoSFrPvcCarExceedPackets_Type()
)
hh3cCBQoSFrPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCarExceedPackets.setStatus("current")
_Hh3cCBQoSFrPvcCarExceedBytes_Type = Counter64
_Hh3cCBQoSFrPvcCarExceedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcCarExceedBytes = _Hh3cCBQoSFrPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 3, 1, 4),
    _Hh3cCBQoSFrPvcCarExceedBytes_Type()
)
hh3cCBQoSFrPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcCarExceedBytes.setStatus("current")
_Hh3cCBQoSFrPvcGtsRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcGtsRunInfoTable = _Hh3cCBQoSFrPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcGtsRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcGtsRunInfoEntry = _Hh3cCBQoSFrPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1)
)
hh3cCBQoSFrPvcGtsRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcGtsPassedPackets_Type = Counter64
_Hh3cCBQoSFrPvcGtsPassedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcGtsPassedPackets = _Hh3cCBQoSFrPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 1),
    _Hh3cCBQoSFrPvcGtsPassedPackets_Type()
)
hh3cCBQoSFrPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsPassedPackets.setStatus("current")
_Hh3cCBQoSFrPvcGtsPassedBytes_Type = Counter64
_Hh3cCBQoSFrPvcGtsPassedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcGtsPassedBytes = _Hh3cCBQoSFrPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 2),
    _Hh3cCBQoSFrPvcGtsPassedBytes_Type()
)
hh3cCBQoSFrPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsPassedBytes.setStatus("current")
_Hh3cCBQoSFrPvcGtsDiscardedPackets_Type = Counter64
_Hh3cCBQoSFrPvcGtsDiscardedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcGtsDiscardedPackets = _Hh3cCBQoSFrPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 3),
    _Hh3cCBQoSFrPvcGtsDiscardedPackets_Type()
)
hh3cCBQoSFrPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsDiscardedPackets.setStatus("current")
_Hh3cCBQoSFrPvcGtsDiscardedBytes_Type = Counter64
_Hh3cCBQoSFrPvcGtsDiscardedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcGtsDiscardedBytes = _Hh3cCBQoSFrPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 4),
    _Hh3cCBQoSFrPvcGtsDiscardedBytes_Type()
)
hh3cCBQoSFrPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsDiscardedBytes.setStatus("current")
_Hh3cCBQoSFrPvcGtsDelayedPackets_Type = Counter64
_Hh3cCBQoSFrPvcGtsDelayedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcGtsDelayedPackets = _Hh3cCBQoSFrPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 5),
    _Hh3cCBQoSFrPvcGtsDelayedPackets_Type()
)
hh3cCBQoSFrPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsDelayedPackets.setStatus("current")
_Hh3cCBQoSFrPvcGtsDelayedBytes_Type = Counter64
_Hh3cCBQoSFrPvcGtsDelayedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcGtsDelayedBytes = _Hh3cCBQoSFrPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 6),
    _Hh3cCBQoSFrPvcGtsDelayedBytes_Type()
)
hh3cCBQoSFrPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsDelayedBytes.setStatus("current")
_Hh3cCBQoSFrPvcGtsQueueSize_Type = Integer32
_Hh3cCBQoSFrPvcGtsQueueSize_Object = MibTableColumn
hh3cCBQoSFrPvcGtsQueueSize = _Hh3cCBQoSFrPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 4, 1, 7),
    _Hh3cCBQoSFrPvcGtsQueueSize_Type()
)
hh3cCBQoSFrPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcGtsQueueSize.setStatus("current")
_Hh3cCBQoSFrPvcRemarkRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcRemarkRunInfoTable = _Hh3cCBQoSFrPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcRemarkRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcRemarkRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcRemarkRunInfoEntry = _Hh3cCBQoSFrPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 5, 1)
)
hh3cCBQoSFrPvcRemarkRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcRemarkRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcRemarkedPackets_Type = Counter64
_Hh3cCBQoSFrPvcRemarkedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcRemarkedPackets = _Hh3cCBQoSFrPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 5, 1, 1),
    _Hh3cCBQoSFrPvcRemarkedPackets_Type()
)
hh3cCBQoSFrPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcRemarkedPackets.setStatus("current")
_Hh3cCBQoSFrPvcQueueRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcQueueRunInfoTable = _Hh3cCBQoSFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcQueueRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcQueueRunInfoEntry = _Hh3cCBQoSFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1)
)
hh3cCBQoSFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcQueueMatchedPackets_Type = Counter64
_Hh3cCBQoSFrPvcQueueMatchedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcQueueMatchedPackets = _Hh3cCBQoSFrPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1, 1),
    _Hh3cCBQoSFrPvcQueueMatchedPackets_Type()
)
hh3cCBQoSFrPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueMatchedPackets.setStatus("current")
_Hh3cCBQoSFrPvcQueueMatchedBytes_Type = Counter64
_Hh3cCBQoSFrPvcQueueMatchedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcQueueMatchedBytes = _Hh3cCBQoSFrPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1, 2),
    _Hh3cCBQoSFrPvcQueueMatchedBytes_Type()
)
hh3cCBQoSFrPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueMatchedBytes.setStatus("current")
_Hh3cCBQoSFrPvcQueueEnqueuedPackets_Type = Counter64
_Hh3cCBQoSFrPvcQueueEnqueuedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcQueueEnqueuedPackets = _Hh3cCBQoSFrPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1, 3),
    _Hh3cCBQoSFrPvcQueueEnqueuedPackets_Type()
)
hh3cCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueEnqueuedPackets.setStatus("current")
_Hh3cCBQoSFrPvcQueueEnqueuedBytes_Type = Counter64
_Hh3cCBQoSFrPvcQueueEnqueuedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcQueueEnqueuedBytes = _Hh3cCBQoSFrPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1, 4),
    _Hh3cCBQoSFrPvcQueueEnqueuedBytes_Type()
)
hh3cCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueEnqueuedBytes.setStatus("current")
_Hh3cCBQoSFrPvcQueueDiscardedPackets_Type = Counter64
_Hh3cCBQoSFrPvcQueueDiscardedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcQueueDiscardedPackets = _Hh3cCBQoSFrPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1, 5),
    _Hh3cCBQoSFrPvcQueueDiscardedPackets_Type()
)
hh3cCBQoSFrPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueDiscardedPackets.setStatus("current")
_Hh3cCBQoSFrPvcQueueDiscardedBytes_Type = Counter64
_Hh3cCBQoSFrPvcQueueDiscardedBytes_Object = MibTableColumn
hh3cCBQoSFrPvcQueueDiscardedBytes = _Hh3cCBQoSFrPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 6, 1, 6),
    _Hh3cCBQoSFrPvcQueueDiscardedBytes_Type()
)
hh3cCBQoSFrPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcQueueDiscardedBytes.setStatus("current")
_Hh3cCBQoSFrPvcWredRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcWredRunInfoTable = _Hh3cCBQoSFrPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcWredRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcWredRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcWredRunInfoEntry = _Hh3cCBQoSFrPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 7, 1)
)
hh3cCBQoSFrPvcWredRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcWredRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcWredRandomDiscardedPackets_Type = Counter64
_Hh3cCBQoSFrPvcWredRandomDiscardedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcWredRandomDiscardedPackets = _Hh3cCBQoSFrPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 7, 1, 1),
    _Hh3cCBQoSFrPvcWredRandomDiscardedPackets_Type()
)
hh3cCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcWredRandomDiscardedPackets.setStatus("current")
_Hh3cCBQoSFrPvcWredTailDiscardedPackets_Type = Counter64
_Hh3cCBQoSFrPvcWredTailDiscardedPackets_Object = MibTableColumn
hh3cCBQoSFrPvcWredTailDiscardedPackets = _Hh3cCBQoSFrPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 7, 1, 2),
    _Hh3cCBQoSFrPvcWredTailDiscardedPackets_Type()
)
hh3cCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcWredTailDiscardedPackets.setStatus("current")
_Hh3cCBQoSFrPvcAccountingRunInfoTable_Object = MibTable
hh3cCBQoSFrPvcAccountingRunInfoTable = _Hh3cCBQoSFrPvcAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcAccountingRunInfoTable.setStatus("current")
_Hh3cCBQoSFrPvcAccountingRunInfoEntry_Object = MibTableRow
hh3cCBQoSFrPvcAccountingRunInfoEntry = _Hh3cCBQoSFrPvcAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 8, 1)
)
hh3cCBQoSFrPvcAccountingRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSFrPvcApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcAccountingRunInfoEntry.setStatus("current")
_Hh3cCBQoSFrPvcAccountingPackets_Type = Counter64
_Hh3cCBQoSFrPvcAccountingPackets_Object = MibTableColumn
hh3cCBQoSFrPvcAccountingPackets = _Hh3cCBQoSFrPvcAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 8, 1, 1),
    _Hh3cCBQoSFrPvcAccountingPackets_Type()
)
hh3cCBQoSFrPvcAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcAccountingPackets.setStatus("current")
_Hh3cCBQoSFrPvcAccountingBytes_Type = Counter64
_Hh3cCBQoSFrPvcAccountingBytes_Object = MibTableColumn
hh3cCBQoSFrPvcAccountingBytes = _Hh3cCBQoSFrPvcAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 3, 8, 1, 2),
    _Hh3cCBQoSFrPvcAccountingBytes_Type()
)
hh3cCBQoSFrPvcAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSFrPvcAccountingBytes.setStatus("current")
_Hh3cCBQoSVlanStaticsObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSVlanStaticsObjects = _Hh3cCBQoSVlanStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4)
)
_Hh3cCBQoSVlanClassMatchRunInfoTable_Object = MibTable
hh3cCBQoSVlanClassMatchRunInfoTable = _Hh3cCBQoSVlanClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanClassMatchRunInfoTable.setStatus("current")
_Hh3cCBQoSVlanClassMatchRunInfoEntry_Object = MibTableRow
hh3cCBQoSVlanClassMatchRunInfoEntry = _Hh3cCBQoSVlanClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 1, 1)
)
hh3cCBQoSVlanClassMatchRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyVlanid"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanClassMatchRunInfoEntry.setStatus("current")
_Hh3cCBQoSVlanClassMatchedPackets_Type = Counter64
_Hh3cCBQoSVlanClassMatchedPackets_Object = MibTableColumn
hh3cCBQoSVlanClassMatchedPackets = _Hh3cCBQoSVlanClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 1, 1, 1),
    _Hh3cCBQoSVlanClassMatchedPackets_Type()
)
hh3cCBQoSVlanClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanClassMatchedPackets.setStatus("current")
_Hh3cCBQoSVlanAccountingRunInfoTable_Object = MibTable
hh3cCBQoSVlanAccountingRunInfoTable = _Hh3cCBQoSVlanAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanAccountingRunInfoTable.setStatus("current")
_Hh3cCBQoSVlanAccountingRunInfoEntry_Object = MibTableRow
hh3cCBQoSVlanAccountingRunInfoEntry = _Hh3cCBQoSVlanAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 2, 1)
)
hh3cCBQoSVlanAccountingRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyVlanid"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyDirection"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanAccountingRunInfoEntry.setStatus("current")
_Hh3cCBQoSVlanAccountingPackets_Type = Counter64
_Hh3cCBQoSVlanAccountingPackets_Object = MibTableColumn
hh3cCBQoSVlanAccountingPackets = _Hh3cCBQoSVlanAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 2, 1, 1),
    _Hh3cCBQoSVlanAccountingPackets_Type()
)
hh3cCBQoSVlanAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanAccountingPackets.setStatus("current")
_Hh3cCBQoSVlanAccountingBytes_Type = Counter64
_Hh3cCBQoSVlanAccountingBytes_Object = MibTableColumn
hh3cCBQoSVlanAccountingBytes = _Hh3cCBQoSVlanAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 4, 2, 1, 2),
    _Hh3cCBQoSVlanAccountingBytes_Type()
)
hh3cCBQoSVlanAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanAccountingBytes.setStatus("current")
_Hh3cCBQoSApplyPolicyIndexObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSApplyPolicyIndexObjects = _Hh3cCBQoSApplyPolicyIndexObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5)
)
_Hh3cCBQoSApplyObjectTable_Object = MibTable
hh3cCBQoSApplyObjectTable = _Hh3cCBQoSApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectTable.setStatus("current")
_Hh3cCBQoSApplyObjectEntry_Object = MibTableRow
hh3cCBQoSApplyObjectEntry = _Hh3cCBQoSApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1)
)
hh3cCBQoSApplyObjectEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectEntry.setStatus("current")
_Hh3cCBQoSApplyObjectIndex_Type = Unsigned32
_Hh3cCBQoSApplyObjectIndex_Object = MibTableColumn
hh3cCBQoSApplyObjectIndex = _Hh3cCBQoSApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 1),
    _Hh3cCBQoSApplyObjectIndex_Type()
)
hh3cCBQoSApplyObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectIndex.setStatus("current")
_Hh3cCBQoSApplyObjectType_Type = ApplyObjectType
_Hh3cCBQoSApplyObjectType_Object = MibTableColumn
hh3cCBQoSApplyObjectType = _Hh3cCBQoSApplyObjectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 2),
    _Hh3cCBQoSApplyObjectType_Type()
)
hh3cCBQoSApplyObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectType.setStatus("current")
_Hh3cCBQoSApplyObjectDirection_Type = DirectionType
_Hh3cCBQoSApplyObjectDirection_Object = MibTableColumn
hh3cCBQoSApplyObjectDirection = _Hh3cCBQoSApplyObjectDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 3),
    _Hh3cCBQoSApplyObjectDirection_Type()
)
hh3cCBQoSApplyObjectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectDirection.setStatus("current")
_Hh3cCBQoSApplyObjectMainSite_Type = Unsigned32
_Hh3cCBQoSApplyObjectMainSite_Object = MibTableColumn
hh3cCBQoSApplyObjectMainSite = _Hh3cCBQoSApplyObjectMainSite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 4),
    _Hh3cCBQoSApplyObjectMainSite_Type()
)
hh3cCBQoSApplyObjectMainSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectMainSite.setStatus("current")
_Hh3cCBQoSApplyObjectSubChannel_Type = Unsigned32
_Hh3cCBQoSApplyObjectSubChannel_Object = MibTableColumn
hh3cCBQoSApplyObjectSubChannel = _Hh3cCBQoSApplyObjectSubChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 5),
    _Hh3cCBQoSApplyObjectSubChannel_Type()
)
hh3cCBQoSApplyObjectSubChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectSubChannel.setStatus("current")
_Hh3cCBQoSApplyObjectSubClass_Type = Unsigned32
_Hh3cCBQoSApplyObjectSubClass_Object = MibTableColumn
hh3cCBQoSApplyObjectSubClass = _Hh3cCBQoSApplyObjectSubClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 6),
    _Hh3cCBQoSApplyObjectSubClass_Type()
)
hh3cCBQoSApplyObjectSubClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectSubClass.setStatus("current")
_Hh3cCBQoSApplyObjectSubClassSec_Type = Unsigned32
_Hh3cCBQoSApplyObjectSubClassSec_Object = MibTableColumn
hh3cCBQoSApplyObjectSubClassSec = _Hh3cCBQoSApplyObjectSubClassSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 1, 1, 7),
    _Hh3cCBQoSApplyObjectSubClassSec_Type()
)
hh3cCBQoSApplyObjectSubClassSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyObjectSubClassSec.setStatus("current")
_Hh3cCBQoSIntApplyObjectTable_Object = MibTable
hh3cCBQoSIntApplyObjectTable = _Hh3cCBQoSIntApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSIntApplyObjectTable.setStatus("current")
_Hh3cCBQoSIntApplyObjectEntry_Object = MibTableRow
hh3cCBQoSIntApplyObjectEntry = _Hh3cCBQoSIntApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 2, 1)
)
hh3cCBQoSIntApplyObjectEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSIntApplyObjectIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSIntApplyObjectEntry.setStatus("current")
_Hh3cCBQoSIntApplyObjectIfIndex_Type = Unsigned32
_Hh3cCBQoSIntApplyObjectIfIndex_Object = MibTableColumn
hh3cCBQoSIntApplyObjectIfIndex = _Hh3cCBQoSIntApplyObjectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 2, 1, 1),
    _Hh3cCBQoSIntApplyObjectIfIndex_Type()
)
hh3cCBQoSIntApplyObjectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSIntApplyObjectIfIndex.setStatus("current")
_Hh3cCBQoSIntApplyObjectIndex_Type = Unsigned32
_Hh3cCBQoSIntApplyObjectIndex_Object = MibTableColumn
hh3cCBQoSIntApplyObjectIndex = _Hh3cCBQoSIntApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 2, 1, 2),
    _Hh3cCBQoSIntApplyObjectIndex_Type()
)
hh3cCBQoSIntApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSIntApplyObjectIndex.setStatus("current")
_Hh3cCBQoSVlanApplyObjectTable_Object = MibTable
hh3cCBQoSVlanApplyObjectTable = _Hh3cCBQoSVlanApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyObjectTable.setStatus("current")
_Hh3cCBQoSVlanApplyObjectEntry_Object = MibTableRow
hh3cCBQoSVlanApplyObjectEntry = _Hh3cCBQoSVlanApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 3, 1)
)
hh3cCBQoSVlanApplyObjectEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyObjectVlanID"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyObjectEntry.setStatus("current")


class _Hh3cCBQoSVlanApplyObjectVlanID_Type(Unsigned32):
    """Custom type hh3cCBQoSVlanApplyObjectVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cCBQoSVlanApplyObjectVlanID_Type.__name__ = "Unsigned32"
_Hh3cCBQoSVlanApplyObjectVlanID_Object = MibTableColumn
hh3cCBQoSVlanApplyObjectVlanID = _Hh3cCBQoSVlanApplyObjectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 3, 1, 1),
    _Hh3cCBQoSVlanApplyObjectVlanID_Type()
)
hh3cCBQoSVlanApplyObjectVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyObjectVlanID.setStatus("current")
_Hh3cCBQoSVlanApplyObjectIndex_Type = Unsigned32
_Hh3cCBQoSVlanApplyObjectIndex_Object = MibTableColumn
hh3cCBQoSVlanApplyObjectIndex = _Hh3cCBQoSVlanApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 3, 1, 2),
    _Hh3cCBQoSVlanApplyObjectIndex_Type()
)
hh3cCBQoSVlanApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSVlanApplyObjectIndex.setStatus("current")
_Hh3cCBQoSPvcApplyObjectTable_Object = MibTable
hh3cCBQoSPvcApplyObjectTable = _Hh3cCBQoSPvcApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSPvcApplyObjectTable.setStatus("current")
_Hh3cCBQoSPvcApplyObjectEntry_Object = MibTableRow
hh3cCBQoSPvcApplyObjectEntry = _Hh3cCBQoSPvcApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 4, 1)
)
hh3cCBQoSPvcApplyObjectEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPvcApplyObjectIfIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPvcApplyObjectPvcID"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectDirection"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSPvcApplyObjectEntry.setStatus("current")
_Hh3cCBQoSPvcApplyObjectIfIndex_Type = Unsigned32
_Hh3cCBQoSPvcApplyObjectIfIndex_Object = MibTableColumn
hh3cCBQoSPvcApplyObjectIfIndex = _Hh3cCBQoSPvcApplyObjectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 4, 1, 1),
    _Hh3cCBQoSPvcApplyObjectIfIndex_Type()
)
hh3cCBQoSPvcApplyObjectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSPvcApplyObjectIfIndex.setStatus("current")
_Hh3cCBQoSPvcApplyObjectPvcID_Type = Unsigned32
_Hh3cCBQoSPvcApplyObjectPvcID_Object = MibTableColumn
hh3cCBQoSPvcApplyObjectPvcID = _Hh3cCBQoSPvcApplyObjectPvcID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 4, 1, 2),
    _Hh3cCBQoSPvcApplyObjectPvcID_Type()
)
hh3cCBQoSPvcApplyObjectPvcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSPvcApplyObjectPvcID.setStatus("current")
_Hh3cCBQoSPvcApplyObjectIndex_Type = Unsigned32
_Hh3cCBQoSPvcApplyObjectIndex_Object = MibTableColumn
hh3cCBQoSPvcApplyObjectIndex = _Hh3cCBQoSPvcApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 4, 1, 3),
    _Hh3cCBQoSPvcApplyObjectIndex_Type()
)
hh3cCBQoSPvcApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSPvcApplyObjectIndex.setStatus("current")
_Hh3cCBQoSNestPolicyApplyObjectTable_Object = MibTable
hh3cCBQoSNestPolicyApplyObjectTable = _Hh3cCBQoSNestPolicyApplyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyApplyObjectTable.setStatus("current")
_Hh3cCBQoSNestPolicyApplyObjectEntry_Object = MibTableRow
hh3cCBQoSNestPolicyApplyObjectEntry = _Hh3cCBQoSNestPolicyApplyObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 5, 1)
)
hh3cCBQoSNestPolicyApplyObjectEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSNestPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyApplyObjectEntry.setStatus("current")
_Hh3cCBQoSNestPolicyClassIndex_Type = Unsigned32
_Hh3cCBQoSNestPolicyClassIndex_Object = MibTableColumn
hh3cCBQoSNestPolicyClassIndex = _Hh3cCBQoSNestPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 5, 1, 1),
    _Hh3cCBQoSNestPolicyClassIndex_Type()
)
hh3cCBQoSNestPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyClassIndex.setStatus("current")
_Hh3cCBQoSNestPolicyApplyObjectIndex_Type = Unsigned32
_Hh3cCBQoSNestPolicyApplyObjectIndex_Object = MibTableColumn
hh3cCBQoSNestPolicyApplyObjectIndex = _Hh3cCBQoSNestPolicyApplyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 5, 5, 1, 2),
    _Hh3cCBQoSNestPolicyApplyObjectIndex_Type()
)
hh3cCBQoSNestPolicyApplyObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSNestPolicyApplyObjectIndex.setStatus("current")
_Hh3cCBQoSStaticsObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSStaticsObjects = _Hh3cCBQoSStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6)
)
_Hh3cCBQoSCbqRunInfoTable_Object = MibTable
hh3cCBQoSCbqRunInfoTable = _Hh3cCBQoSCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cCBQoSCbqRunInfoTable.setStatus("current")
_Hh3cCBQoSCbqRunInfoEntry_Object = MibTableRow
hh3cCBQoSCbqRunInfoEntry = _Hh3cCBQoSCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1)
)
hh3cCBQoSCbqRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSCbqRunInfoEntry.setStatus("current")
_Hh3cCBQoSCbqQueueSize_Type = Integer32
_Hh3cCBQoSCbqQueueSize_Object = MibTableColumn
hh3cCBQoSCbqQueueSize = _Hh3cCBQoSCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 1),
    _Hh3cCBQoSCbqQueueSize_Type()
)
hh3cCBQoSCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqQueueSize.setStatus("current")
_Hh3cCBQoSCbqDiscard_Type = Counter64
_Hh3cCBQoSCbqDiscard_Object = MibTableColumn
hh3cCBQoSCbqDiscard = _Hh3cCBQoSCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 2),
    _Hh3cCBQoSCbqDiscard_Type()
)
hh3cCBQoSCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqDiscard.setStatus("current")
_Hh3cCBQoSCbqEfQueueSize_Type = Integer32
_Hh3cCBQoSCbqEfQueueSize_Object = MibTableColumn
hh3cCBQoSCbqEfQueueSize = _Hh3cCBQoSCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 3),
    _Hh3cCBQoSCbqEfQueueSize_Type()
)
hh3cCBQoSCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqEfQueueSize.setStatus("current")
_Hh3cCBQoSCbqAfQueueSize_Type = Integer32
_Hh3cCBQoSCbqAfQueueSize_Object = MibTableColumn
hh3cCBQoSCbqAfQueueSize = _Hh3cCBQoSCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 4),
    _Hh3cCBQoSCbqAfQueueSize_Type()
)
hh3cCBQoSCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqAfQueueSize.setStatus("current")
_Hh3cCBQoSCbqBeQueueSize_Type = Integer32
_Hh3cCBQoSCbqBeQueueSize_Object = MibTableColumn
hh3cCBQoSCbqBeQueueSize = _Hh3cCBQoSCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 5),
    _Hh3cCBQoSCbqBeQueueSize_Type()
)
hh3cCBQoSCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqBeQueueSize.setStatus("current")
_Hh3cCBQoSCbqBeActiveQueueNum_Type = Integer32
_Hh3cCBQoSCbqBeActiveQueueNum_Object = MibTableColumn
hh3cCBQoSCbqBeActiveQueueNum = _Hh3cCBQoSCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 6),
    _Hh3cCBQoSCbqBeActiveQueueNum_Type()
)
hh3cCBQoSCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqBeActiveQueueNum.setStatus("current")
_Hh3cCBQoSCbqBeMaxActiveQueueNum_Type = Integer32
_Hh3cCBQoSCbqBeMaxActiveQueueNum_Object = MibTableColumn
hh3cCBQoSCbqBeMaxActiveQueueNum = _Hh3cCBQoSCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 7),
    _Hh3cCBQoSCbqBeMaxActiveQueueNum_Type()
)
hh3cCBQoSCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqBeMaxActiveQueueNum.setStatus("current")
_Hh3cCBQoSCbqBeTotalQueueNum_Type = Integer32
_Hh3cCBQoSCbqBeTotalQueueNum_Object = MibTableColumn
hh3cCBQoSCbqBeTotalQueueNum = _Hh3cCBQoSCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 8),
    _Hh3cCBQoSCbqBeTotalQueueNum_Type()
)
hh3cCBQoSCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqBeTotalQueueNum.setStatus("current")
_Hh3cCBQoSCbqAfAllocatedQueueNum_Type = Integer32
_Hh3cCBQoSCbqAfAllocatedQueueNum_Object = MibTableColumn
hh3cCBQoSCbqAfAllocatedQueueNum = _Hh3cCBQoSCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 1, 1, 9),
    _Hh3cCBQoSCbqAfAllocatedQueueNum_Type()
)
hh3cCBQoSCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCbqAfAllocatedQueueNum.setStatus("current")
_Hh3cCBQoSClassMatchRunInfoTable_Object = MibTable
hh3cCBQoSClassMatchRunInfoTable = _Hh3cCBQoSClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cCBQoSClassMatchRunInfoTable.setStatus("current")
_Hh3cCBQoSClassMatchRunInfoEntry_Object = MibTableRow
hh3cCBQoSClassMatchRunInfoEntry = _Hh3cCBQoSClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1)
)
hh3cCBQoSClassMatchRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSClassMatchRunInfoEntry.setStatus("current")
_Hh3cCBQoSClassMatchedPackets_Type = Counter64
_Hh3cCBQoSClassMatchedPackets_Object = MibTableColumn
hh3cCBQoSClassMatchedPackets = _Hh3cCBQoSClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 1),
    _Hh3cCBQoSClassMatchedPackets_Type()
)
hh3cCBQoSClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassMatchedPackets.setStatus("current")
_Hh3cCBQoSClassMatchedBytes_Type = Counter64
_Hh3cCBQoSClassMatchedBytes_Object = MibTableColumn
hh3cCBQoSClassMatchedBytes = _Hh3cCBQoSClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 2),
    _Hh3cCBQoSClassMatchedBytes_Type()
)
hh3cCBQoSClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassMatchedBytes.setStatus("current")
_Hh3cCBQoSClassFwdPktpps_Type = Unsigned32
_Hh3cCBQoSClassFwdPktpps_Object = MibTableColumn
hh3cCBQoSClassFwdPktpps = _Hh3cCBQoSClassFwdPktpps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 3),
    _Hh3cCBQoSClassFwdPktpps_Type()
)
hh3cCBQoSClassFwdPktpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassFwdPktpps.setStatus("current")
_Hh3cCBQoSClassFwdPktbps_Type = Unsigned32
_Hh3cCBQoSClassFwdPktbps_Object = MibTableColumn
hh3cCBQoSClassFwdPktbps = _Hh3cCBQoSClassFwdPktbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 4),
    _Hh3cCBQoSClassFwdPktbps_Type()
)
hh3cCBQoSClassFwdPktbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassFwdPktbps.setStatus("current")
_Hh3cCBQoSClassDropPktpps_Type = Unsigned32
_Hh3cCBQoSClassDropPktpps_Object = MibTableColumn
hh3cCBQoSClassDropPktpps = _Hh3cCBQoSClassDropPktpps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 5),
    _Hh3cCBQoSClassDropPktpps_Type()
)
hh3cCBQoSClassDropPktpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassDropPktpps.setStatus("current")
_Hh3cCBQoSClassDropPktbps_Type = Unsigned32
_Hh3cCBQoSClassDropPktbps_Object = MibTableColumn
hh3cCBQoSClassDropPktbps = _Hh3cCBQoSClassDropPktbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 6),
    _Hh3cCBQoSClassDropPktbps_Type()
)
hh3cCBQoSClassDropPktbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassDropPktbps.setStatus("current")
_Hh3cCBQoSClassFlowStatInterval_Type = Unsigned32
_Hh3cCBQoSClassFlowStatInterval_Object = MibTableColumn
hh3cCBQoSClassFlowStatInterval = _Hh3cCBQoSClassFlowStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 7),
    _Hh3cCBQoSClassFlowStatInterval_Type()
)
hh3cCBQoSClassFlowStatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassFlowStatInterval.setStatus("current")


class _Hh3cCBQoSClassBehaviorStatus_Type(Integer32):
    """Custom type hh3cCBQoSClassBehaviorStatus based on Integer32"""
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


_Hh3cCBQoSClassBehaviorStatus_Type.__name__ = "Integer32"
_Hh3cCBQoSClassBehaviorStatus_Object = MibTableColumn
hh3cCBQoSClassBehaviorStatus = _Hh3cCBQoSClassBehaviorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 2, 1, 8),
    _Hh3cCBQoSClassBehaviorStatus_Type()
)
hh3cCBQoSClassBehaviorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSClassBehaviorStatus.setStatus("current")
_Hh3cCBQoSCarRunInfoTable_Object = MibTable
hh3cCBQoSCarRunInfoTable = _Hh3cCBQoSCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3)
)
if mibBuilder.loadTexts:
    hh3cCBQoSCarRunInfoTable.setStatus("current")
_Hh3cCBQoSCarRunInfoEntry_Object = MibTableRow
hh3cCBQoSCarRunInfoEntry = _Hh3cCBQoSCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1)
)
hh3cCBQoSCarRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSCarRunInfoEntry.setStatus("current")
_Hh3cCBQoSCarGreenPackets_Type = Counter64
_Hh3cCBQoSCarGreenPackets_Object = MibTableColumn
hh3cCBQoSCarGreenPackets = _Hh3cCBQoSCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1, 1),
    _Hh3cCBQoSCarGreenPackets_Type()
)
hh3cCBQoSCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarGreenPackets.setStatus("current")
_Hh3cCBQoSCarGreenBytes_Type = Counter64
_Hh3cCBQoSCarGreenBytes_Object = MibTableColumn
hh3cCBQoSCarGreenBytes = _Hh3cCBQoSCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1, 2),
    _Hh3cCBQoSCarGreenBytes_Type()
)
hh3cCBQoSCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarGreenBytes.setStatus("current")
_Hh3cCBQoSCarRedPackets_Type = Counter64
_Hh3cCBQoSCarRedPackets_Object = MibTableColumn
hh3cCBQoSCarRedPackets = _Hh3cCBQoSCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1, 3),
    _Hh3cCBQoSCarRedPackets_Type()
)
hh3cCBQoSCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarRedPackets.setStatus("current")
_Hh3cCBQoSCarRedBytes_Type = Counter64
_Hh3cCBQoSCarRedBytes_Object = MibTableColumn
hh3cCBQoSCarRedBytes = _Hh3cCBQoSCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1, 4),
    _Hh3cCBQoSCarRedBytes_Type()
)
hh3cCBQoSCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarRedBytes.setStatus("current")
_Hh3cCBQoSCarYellowPackets_Type = Counter64
_Hh3cCBQoSCarYellowPackets_Object = MibTableColumn
hh3cCBQoSCarYellowPackets = _Hh3cCBQoSCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1, 5),
    _Hh3cCBQoSCarYellowPackets_Type()
)
hh3cCBQoSCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarYellowPackets.setStatus("current")
_Hh3cCBQoSCarYellowBytes_Type = Counter64
_Hh3cCBQoSCarYellowBytes_Object = MibTableColumn
hh3cCBQoSCarYellowBytes = _Hh3cCBQoSCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 3, 1, 6),
    _Hh3cCBQoSCarYellowBytes_Type()
)
hh3cCBQoSCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSCarYellowBytes.setStatus("current")
_Hh3cCBQoSGtsRunInfoTable_Object = MibTable
hh3cCBQoSGtsRunInfoTable = _Hh3cCBQoSGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    hh3cCBQoSGtsRunInfoTable.setStatus("current")
_Hh3cCBQoSGtsRunInfoEntry_Object = MibTableRow
hh3cCBQoSGtsRunInfoEntry = _Hh3cCBQoSGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1)
)
hh3cCBQoSGtsRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSGtsRunInfoEntry.setStatus("current")
_Hh3cCBQoSGtsPassedPackets_Type = Counter64
_Hh3cCBQoSGtsPassedPackets_Object = MibTableColumn
hh3cCBQoSGtsPassedPackets = _Hh3cCBQoSGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 1),
    _Hh3cCBQoSGtsPassedPackets_Type()
)
hh3cCBQoSGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsPassedPackets.setStatus("current")
_Hh3cCBQoSGtsPassedBytes_Type = Counter64
_Hh3cCBQoSGtsPassedBytes_Object = MibTableColumn
hh3cCBQoSGtsPassedBytes = _Hh3cCBQoSGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 2),
    _Hh3cCBQoSGtsPassedBytes_Type()
)
hh3cCBQoSGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsPassedBytes.setStatus("current")
_Hh3cCBQoSGtsDiscardedPackets_Type = Counter64
_Hh3cCBQoSGtsDiscardedPackets_Object = MibTableColumn
hh3cCBQoSGtsDiscardedPackets = _Hh3cCBQoSGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 3),
    _Hh3cCBQoSGtsDiscardedPackets_Type()
)
hh3cCBQoSGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsDiscardedPackets.setStatus("current")
_Hh3cCBQoSGtsDiscardedBytes_Type = Counter64
_Hh3cCBQoSGtsDiscardedBytes_Object = MibTableColumn
hh3cCBQoSGtsDiscardedBytes = _Hh3cCBQoSGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 4),
    _Hh3cCBQoSGtsDiscardedBytes_Type()
)
hh3cCBQoSGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsDiscardedBytes.setStatus("current")
_Hh3cCBQoSGtsDelayedPackets_Type = Counter64
_Hh3cCBQoSGtsDelayedPackets_Object = MibTableColumn
hh3cCBQoSGtsDelayedPackets = _Hh3cCBQoSGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 5),
    _Hh3cCBQoSGtsDelayedPackets_Type()
)
hh3cCBQoSGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsDelayedPackets.setStatus("current")
_Hh3cCBQoSGtsDelayedBytes_Type = Counter64
_Hh3cCBQoSGtsDelayedBytes_Object = MibTableColumn
hh3cCBQoSGtsDelayedBytes = _Hh3cCBQoSGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 6),
    _Hh3cCBQoSGtsDelayedBytes_Type()
)
hh3cCBQoSGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsDelayedBytes.setStatus("current")
_Hh3cCBQoSGtsQueueSize_Type = Integer32
_Hh3cCBQoSGtsQueueSize_Object = MibTableColumn
hh3cCBQoSGtsQueueSize = _Hh3cCBQoSGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 4, 1, 7),
    _Hh3cCBQoSGtsQueueSize_Type()
)
hh3cCBQoSGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSGtsQueueSize.setStatus("current")
_Hh3cCBQoSRemarkRunInfoTable_Object = MibTable
hh3cCBQoSRemarkRunInfoTable = _Hh3cCBQoSRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkRunInfoTable.setStatus("current")
_Hh3cCBQoSRemarkRunInfoEntry_Object = MibTableRow
hh3cCBQoSRemarkRunInfoEntry = _Hh3cCBQoSRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 5, 1)
)
hh3cCBQoSRemarkRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkRunInfoEntry.setStatus("current")
_Hh3cCBQoSRemarkedPackets_Type = Counter64
_Hh3cCBQoSRemarkedPackets_Object = MibTableColumn
hh3cCBQoSRemarkedPackets = _Hh3cCBQoSRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 5, 1, 1),
    _Hh3cCBQoSRemarkedPackets_Type()
)
hh3cCBQoSRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSRemarkedPackets.setStatus("current")
_Hh3cCBQoSQueueRunInfoTable_Object = MibTable
hh3cCBQoSQueueRunInfoTable = _Hh3cCBQoSQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    hh3cCBQoSQueueRunInfoTable.setStatus("current")
_Hh3cCBQoSQueueRunInfoEntry_Object = MibTableRow
hh3cCBQoSQueueRunInfoEntry = _Hh3cCBQoSQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1)
)
hh3cCBQoSQueueRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSQueueRunInfoEntry.setStatus("current")
_Hh3cCBQoSQueueMatchedPackets_Type = Counter64
_Hh3cCBQoSQueueMatchedPackets_Object = MibTableColumn
hh3cCBQoSQueueMatchedPackets = _Hh3cCBQoSQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1, 1),
    _Hh3cCBQoSQueueMatchedPackets_Type()
)
hh3cCBQoSQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueMatchedPackets.setStatus("current")
_Hh3cCBQoSQueueMatchedBytes_Type = Counter64
_Hh3cCBQoSQueueMatchedBytes_Object = MibTableColumn
hh3cCBQoSQueueMatchedBytes = _Hh3cCBQoSQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1, 2),
    _Hh3cCBQoSQueueMatchedBytes_Type()
)
hh3cCBQoSQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueMatchedBytes.setStatus("current")
_Hh3cCBQoSQueueEnqueuedPackets_Type = Counter64
_Hh3cCBQoSQueueEnqueuedPackets_Object = MibTableColumn
hh3cCBQoSQueueEnqueuedPackets = _Hh3cCBQoSQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1, 3),
    _Hh3cCBQoSQueueEnqueuedPackets_Type()
)
hh3cCBQoSQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueEnqueuedPackets.setStatus("current")
_Hh3cCBQoSQueueEnqueuedBytes_Type = Counter64
_Hh3cCBQoSQueueEnqueuedBytes_Object = MibTableColumn
hh3cCBQoSQueueEnqueuedBytes = _Hh3cCBQoSQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1, 4),
    _Hh3cCBQoSQueueEnqueuedBytes_Type()
)
hh3cCBQoSQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueEnqueuedBytes.setStatus("current")
_Hh3cCBQoSQueueDiscardedPackets_Type = Counter64
_Hh3cCBQoSQueueDiscardedPackets_Object = MibTableColumn
hh3cCBQoSQueueDiscardedPackets = _Hh3cCBQoSQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1, 5),
    _Hh3cCBQoSQueueDiscardedPackets_Type()
)
hh3cCBQoSQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueDiscardedPackets.setStatus("current")
_Hh3cCBQoSQueueDiscardedBytes_Type = Counter64
_Hh3cCBQoSQueueDiscardedBytes_Object = MibTableColumn
hh3cCBQoSQueueDiscardedBytes = _Hh3cCBQoSQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 6, 1, 6),
    _Hh3cCBQoSQueueDiscardedBytes_Type()
)
hh3cCBQoSQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSQueueDiscardedBytes.setStatus("current")
_Hh3cCBQoSWredRunInfoTable_Object = MibTable
hh3cCBQoSWredRunInfoTable = _Hh3cCBQoSWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    hh3cCBQoSWredRunInfoTable.setStatus("current")
_Hh3cCBQoSWredRunInfoEntry_Object = MibTableRow
hh3cCBQoSWredRunInfoEntry = _Hh3cCBQoSWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 7, 1)
)
hh3cCBQoSWredRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSWredRunInfoEntry.setStatus("current")
_Hh3cCBQoSWredRandomDiscardedPackets_Type = Counter64
_Hh3cCBQoSWredRandomDiscardedPackets_Object = MibTableColumn
hh3cCBQoSWredRandomDiscardedPackets = _Hh3cCBQoSWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 7, 1, 1),
    _Hh3cCBQoSWredRandomDiscardedPackets_Type()
)
hh3cCBQoSWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSWredRandomDiscardedPackets.setStatus("current")
_Hh3cCBQoSWredTailDiscardedPackets_Type = Counter64
_Hh3cCBQoSWredTailDiscardedPackets_Object = MibTableColumn
hh3cCBQoSWredTailDiscardedPackets = _Hh3cCBQoSWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 7, 1, 2),
    _Hh3cCBQoSWredTailDiscardedPackets_Type()
)
hh3cCBQoSWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSWredTailDiscardedPackets.setStatus("current")
_Hh3cCBQoSAccountingRunInfoTable_Object = MibTable
hh3cCBQoSAccountingRunInfoTable = _Hh3cCBQoSAccountingRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 8)
)
if mibBuilder.loadTexts:
    hh3cCBQoSAccountingRunInfoTable.setStatus("current")
_Hh3cCBQoSAccountingRunInfoEntry_Object = MibTableRow
hh3cCBQoSAccountingRunInfoEntry = _Hh3cCBQoSAccountingRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 8, 1)
)
hh3cCBQoSAccountingRunInfoEntry.setIndexNames(
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSApplyObjectIndex"),
    (0, "HH3C-CBQOS2-MIB", "hh3cCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hh3cCBQoSAccountingRunInfoEntry.setStatus("current")
_Hh3cCBQoSAccountingPackets_Type = Counter64
_Hh3cCBQoSAccountingPackets_Object = MibTableColumn
hh3cCBQoSAccountingPackets = _Hh3cCBQoSAccountingPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 8, 1, 1),
    _Hh3cCBQoSAccountingPackets_Type()
)
hh3cCBQoSAccountingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAccountingPackets.setStatus("current")
_Hh3cCBQoSAccountingBytes_Type = Counter64
_Hh3cCBQoSAccountingBytes_Object = MibTableColumn
hh3cCBQoSAccountingBytes = _Hh3cCBQoSAccountingBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 5, 6, 8, 1, 2),
    _Hh3cCBQoSAccountingBytes_Type()
)
hh3cCBQoSAccountingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSAccountingBytes.setStatus("current")
_Hh3cCBQoSApplyingStatusObjects_ObjectIdentity = ObjectIdentity
hh3cCBQoSApplyingStatusObjects = _Hh3cCBQoSApplyingStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 6)
)


class _Hh3cCBQoSApplyingStatus_Type(Integer32):
    """Custom type hh3cCBQoSApplyingStatus based on Integer32"""
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


_Hh3cCBQoSApplyingStatus_Type.__name__ = "Integer32"
_Hh3cCBQoSApplyingStatus_Object = MibScalar
hh3cCBQoSApplyingStatus = _Hh3cCBQoSApplyingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 6, 1),
    _Hh3cCBQoSApplyingStatus_Type()
)
hh3cCBQoSApplyingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCBQoSApplyingStatus.setStatus("current")
_Hh3cCBQoSNotifications_ObjectIdentity = ObjectIdentity
hh3cCBQoSNotifications = _Hh3cCBQoSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 7)
)
_Hh3cCBQoSNotificationsPrefix_ObjectIdentity = ObjectIdentity
hh3cCBQoSNotificationsPrefix = _Hh3cCBQoSNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 7, 0)
)

# Managed Objects groups


# Notification objects

hh3cCBQoSIfPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 7, 0, 1)
)
hh3cCBQoSIfPolicyChanged.setObjects(
      *(("HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyIfIndex"),
        ("HH3C-CBQOS2-MIB", "hh3cCBQoSIfApplyPolicyDirection"))
)
if mibBuilder.loadTexts:
    hh3cCBQoSIfPolicyChanged.setStatus(
        "current"
    )

hh3cCBQoSVlanPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2, 1, 7, 0, 2)
)
hh3cCBQoSVlanPolicyChanged.setObjects(
      *(("HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyVlanid"),
        ("HH3C-CBQOS2-MIB", "hh3cCBQoSVlanApplyPolicyDirection"))
)
if mibBuilder.loadTexts:
    hh3cCBQoSVlanPolicyChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CBQOS2-MIB",
    **{"MatchRuleType": MatchRuleType,
       "CarAction": CarAction,
       "RemarkType": RemarkType,
       "WredType": WredType,
       "QueueType": QueueType,
       "QueueBandwidthUnit": QueueBandwidthUnit,
       "DirectionType": DirectionType,
       "ApplyObjectType": ApplyObjectType,
       "hh3cQos2": hh3cQos2,
       "hh3cCBQos2": hh3cCBQos2,
       "hh3cCBQoSObjects": hh3cCBQoSObjects,
       "hh3cCBQoSClassifierObjects": hh3cCBQoSClassifierObjects,
       "hh3cCBQoSClassifierIndexNext": hh3cCBQoSClassifierIndexNext,
       "hh3cCBQoSClassifierCfgInfoTable": hh3cCBQoSClassifierCfgInfoTable,
       "hh3cCBQoSClassifierCfgInfoEntry": hh3cCBQoSClassifierCfgInfoEntry,
       "hh3cCBQoSClassifierIndex": hh3cCBQoSClassifierIndex,
       "hh3cCBQoSClassifierName": hh3cCBQoSClassifierName,
       "hh3cCBQoSClassifierRuleCount": hh3cCBQoSClassifierRuleCount,
       "hh3cCBQoSClassifierOperator": hh3cCBQoSClassifierOperator,
       "hh3cCBQoSClassifierLayer": hh3cCBQoSClassifierLayer,
       "hh3cCBQoSClassifierType": hh3cCBQoSClassifierType,
       "hh3cCBQosClassifierMatchRuleNextIndex": hh3cCBQosClassifierMatchRuleNextIndex,
       "hh3cCBQoSClassifierRowStatus": hh3cCBQoSClassifierRowStatus,
       "hh3cCBQoSMatchRuleCfgInfoTable": hh3cCBQoSMatchRuleCfgInfoTable,
       "hh3cCBQoSMatchRuleCfgInfoEntry": hh3cCBQoSMatchRuleCfgInfoEntry,
       "hh3cCBQoSMatchRuleIndex": hh3cCBQoSMatchRuleIndex,
       "hh3cCBQoSMatchRuleIfNot": hh3cCBQoSMatchRuleIfNot,
       "hh3cCBQoSMatchRuleType": hh3cCBQoSMatchRuleType,
       "hh3cCBQoSMatchRuleStringValue": hh3cCBQoSMatchRuleStringValue,
       "hh3cCBQoSMatchRuleIntValue1": hh3cCBQoSMatchRuleIntValue1,
       "hh3cCBQoSMatchRuleIntValue2": hh3cCBQoSMatchRuleIntValue2,
       "hh3cCBQoSMatchIpAddressType": hh3cCBQoSMatchIpAddressType,
       "hh3cCBQoSMatchIpAddress": hh3cCBQoSMatchIpAddress,
       "hh3cCBQoSMatchRuleRowStatus": hh3cCBQoSMatchRuleRowStatus,
       "hh3cCBQoSBehaviorObjects": hh3cCBQoSBehaviorObjects,
       "hh3cCBQoSBehaviorIndexNext": hh3cCBQoSBehaviorIndexNext,
       "hh3cCBQoSBehaviorCfgInfoTable": hh3cCBQoSBehaviorCfgInfoTable,
       "hh3cCBQoSBehaviorCfgInfoEntry": hh3cCBQoSBehaviorCfgInfoEntry,
       "hh3cCBQoSBehaviorIndex": hh3cCBQoSBehaviorIndex,
       "hh3cCBQoSBehaviorName": hh3cCBQoSBehaviorName,
       "hh3cCBQoSBehaviorType": hh3cCBQoSBehaviorType,
       "hh3cCBQoSBehaviorRowStatus": hh3cCBQoSBehaviorRowStatus,
       "hh3cCBQoSCarCfgInfoTable": hh3cCBQoSCarCfgInfoTable,
       "hh3cCBQoSCarCfgInfoEntry": hh3cCBQoSCarCfgInfoEntry,
       "hh3cCBQoSCarCir": hh3cCBQoSCarCir,
       "hh3cCBQoSCarCbs": hh3cCBQoSCarCbs,
       "hh3cCBQoSCarEbs": hh3cCBQoSCarEbs,
       "hh3cCBQoSCarPir": hh3cCBQoSCarPir,
       "hh3cCBQoSCarPbs": hh3cCBQoSCarPbs,
       "hh3cCBQoSCarGreenAction": hh3cCBQoSCarGreenAction,
       "hh3cCBQoSCarGreenRemarkValue": hh3cCBQoSCarGreenRemarkValue,
       "hh3cCBQoSCarYellowAction": hh3cCBQoSCarYellowAction,
       "hh3cCBQoSCarYellowRemarkValue": hh3cCBQoSCarYellowRemarkValue,
       "hh3cCBQoSCarRedAction": hh3cCBQoSCarRedAction,
       "hh3cCBQoSCarRedRemarkValue": hh3cCBQoSCarRedRemarkValue,
       "hh3cCBQoSCarPolicedPriorityMapType": hh3cCBQoSCarPolicedPriorityMapType,
       "hh3cCBQoSCarRowStatus": hh3cCBQoSCarRowStatus,
       "hh3cCBQoSAggregativeCarCfgInfoTable": hh3cCBQoSAggregativeCarCfgInfoTable,
       "hh3cCBQoSAggregativeCarCfgInfoEntry": hh3cCBQoSAggregativeCarCfgInfoEntry,
       "hh3cCBQoSCarAggregativeCarIndex": hh3cCBQoSCarAggregativeCarIndex,
       "hh3cCBQoSCarAggregativeCarName": hh3cCBQoSCarAggregativeCarName,
       "hh3cCBQoSAggregativeCarRowStatus": hh3cCBQoSAggregativeCarRowStatus,
       "hh3cCBQoSGtsCfgInfoTable": hh3cCBQoSGtsCfgInfoTable,
       "hh3cCBQoSGtsCfgInfoEntry": hh3cCBQoSGtsCfgInfoEntry,
       "hh3cCBQoSGtsCir": hh3cCBQoSGtsCir,
       "hh3cCBQoSGtsCbs": hh3cCBQoSGtsCbs,
       "hh3cCBQoSGtsEbs": hh3cCBQoSGtsEbs,
       "hh3cCBQoSGtsQueueLength": hh3cCBQoSGtsQueueLength,
       "hh3cCBQoSGtsRowStatus": hh3cCBQoSGtsRowStatus,
       "hh3cCBQoSRemarkCfgInfoTable": hh3cCBQoSRemarkCfgInfoTable,
       "hh3cCBQoSRemarkCfgInfoEntry": hh3cCBQoSRemarkCfgInfoEntry,
       "hh3cCBQoSRemarkType": hh3cCBQoSRemarkType,
       "hh3cCBQoSRemarkValue": hh3cCBQoSRemarkValue,
       "hh3cCBQoSRemarkRowStatus": hh3cCBQoSRemarkRowStatus,
       "hh3cCBQoSQueueCfgInfoTable": hh3cCBQoSQueueCfgInfoTable,
       "hh3cCBQoSQueueCfgInfoEntry": hh3cCBQoSQueueCfgInfoEntry,
       "hh3cCBQoSQueueType": hh3cCBQoSQueueType,
       "hh3cCBQoSQueueDropType": hh3cCBQoSQueueDropType,
       "hh3cCBQoSQueueLength": hh3cCBQoSQueueLength,
       "hh3cCBQoSQueueBandwidthUnit": hh3cCBQoSQueueBandwidthUnit,
       "hh3cCBQoSQueueBandwidthValue": hh3cCBQoSQueueBandwidthValue,
       "hh3cCBQoSQueueCbs": hh3cCBQoSQueueCbs,
       "hh3cCBQoSQueueQueueNumber": hh3cCBQoSQueueQueueNumber,
       "hh3cCBQoSQueueCbsRatio": hh3cCBQoSQueueCbsRatio,
       "hh3cCBQoSQueueRowStatus": hh3cCBQoSQueueRowStatus,
       "hh3cCBQoSWredCfgInfoTable": hh3cCBQoSWredCfgInfoTable,
       "hh3cCBQoSWredCfgInfoEntry": hh3cCBQoSWredCfgInfoEntry,
       "hh3cCBQoSWredType": hh3cCBQoSWredType,
       "hh3cCBQoSWredWeightConst": hh3cCBQoSWredWeightConst,
       "hh3cCBQoSWredClassCfgInfoTable": hh3cCBQoSWredClassCfgInfoTable,
       "hh3cCBQoSWredClassCfgInfoEntry": hh3cCBQoSWredClassCfgInfoEntry,
       "hh3cCBQoSWredClassValue": hh3cCBQoSWredClassValue,
       "hh3cCBQoSWredClassLowLimit": hh3cCBQoSWredClassLowLimit,
       "hh3cCBQoSWredClassHighLimit": hh3cCBQoSWredClassHighLimit,
       "hh3cCBQoSWredClassDiscardProb": hh3cCBQoSWredClassDiscardProb,
       "hh3cCBQoSPolicyRouteCfgInfoTable": hh3cCBQoSPolicyRouteCfgInfoTable,
       "hh3cCBQoSPolicyRouteCfgInfoEntry": hh3cCBQoSPolicyRouteCfgInfoEntry,
       "hh3cCBQoSPolicyRouteIpAddrType": hh3cCBQoSPolicyRouteIpAddrType,
       "hh3cCBQoSPolicyRouteNexthop": hh3cCBQoSPolicyRouteNexthop,
       "hh3cCBQoSPolicyRouteBackup": hh3cCBQoSPolicyRouteBackup,
       "hh3cCBQoSPolicyRouteRowStatus": hh3cCBQoSPolicyRouteRowStatus,
       "hh3cCBQoSNatCfgInfoTable": hh3cCBQoSNatCfgInfoTable,
       "hh3cCBQoSNatCfgInfoEntry": hh3cCBQoSNatCfgInfoEntry,
       "hh3cCBQoSNatMainNumber": hh3cCBQoSNatMainNumber,
       "hh3cCBQoSNatBackupNumber": hh3cCBQoSNatBackupNumber,
       "hh3cCBQoSNatServiceClass": hh3cCBQoSNatServiceClass,
       "hh3cCBQoSNatRowStatus": hh3cCBQoSNatRowStatus,
       "hh3cCBQoSFirewallCfgInfoTable": hh3cCBQoSFirewallCfgInfoTable,
       "hh3cCBQoSFirewallCfgInfoEntry": hh3cCBQoSFirewallCfgInfoEntry,
       "hh3cCBQoSFirewallAction": hh3cCBQoSFirewallAction,
       "hh3cCBQoSFirewallRowStatus": hh3cCBQoSFirewallRowStatus,
       "hh3cCBQoSSamplingCfgInfoTable": hh3cCBQoSSamplingCfgInfoTable,
       "hh3cCBQoSSamplingCfgInfoEntry": hh3cCBQoSSamplingCfgInfoEntry,
       "hh3cCBQoSSamplingNum": hh3cCBQoSSamplingNum,
       "hh3cCBQoSSamplingRowStatus": hh3cCBQoSSamplingRowStatus,
       "hh3cCBQoSAccountCfgInfoTable": hh3cCBQoSAccountCfgInfoTable,
       "hh3cCBQoSAccountCfgInfoEntry": hh3cCBQoSAccountCfgInfoEntry,
       "hh3cCBQoSAccounting": hh3cCBQoSAccounting,
       "hh3cCBQoSAccountRowStatus": hh3cCBQoSAccountRowStatus,
       "hh3cCBQoSRedirectCfgInfoTable": hh3cCBQoSRedirectCfgInfoTable,
       "hh3cCBQoSRedirectCfgInfoEntry": hh3cCBQoSRedirectCfgInfoEntry,
       "hh3cCBQoSRedirectType": hh3cCBQoSRedirectType,
       "hh3cCBQoSRedirectIfIndex": hh3cCBQoSRedirectIfIndex,
       "hh3cCBQoSRedirectIpAddressType": hh3cCBQoSRedirectIpAddressType,
       "hh3cCBQoSRedirectIpAddress1": hh3cCBQoSRedirectIpAddress1,
       "hh3cCBQoSRedirectIpAddress2": hh3cCBQoSRedirectIpAddress2,
       "hh3cCBQoSRedirectRowStatus": hh3cCBQoSRedirectRowStatus,
       "hh3cCBQoSRedirectIpv6Interface1": hh3cCBQoSRedirectIpv6Interface1,
       "hh3cCBQoSRedirectIpv6Interface2": hh3cCBQoSRedirectIpv6Interface2,
       "hh3cCBQoSPriorityMapCfgInfoTable": hh3cCBQoSPriorityMapCfgInfoTable,
       "hh3cCBQoSPriorityMapCfgInfoEntry": hh3cCBQoSPriorityMapCfgInfoEntry,
       "hh3cCBQoSPriorityMapImportType": hh3cCBQoSPriorityMapImportType,
       "hh3cCBQoSPriorityMapExportType": hh3cCBQoSPriorityMapExportType,
       "hh3cCBQoSPriorityMapGroupIndex": hh3cCBQoSPriorityMapGroupIndex,
       "hh3cCBQoSPriorityMapGroupName": hh3cCBQoSPriorityMapGroupName,
       "hh3cCBQoSPriorityMapAuto": hh3cCBQoSPriorityMapAuto,
       "hh3cCBQoSPriorityMapRowStatus": hh3cCBQoSPriorityMapRowStatus,
       "hh3cCBQoSMirrorCfgInfoTable": hh3cCBQoSMirrorCfgInfoTable,
       "hh3cCBQoSMirrorCfgInfoEntry": hh3cCBQoSMirrorCfgInfoEntry,
       "hh3cCBQoSMirrorType": hh3cCBQoSMirrorType,
       "hh3cCBQoSMirrorIfIndex": hh3cCBQoSMirrorIfIndex,
       "hh3cCBQoSMirrorVlanID": hh3cCBQoSMirrorVlanID,
       "hh3cCBQoSMirrorRowStatus": hh3cCBQoSMirrorRowStatus,
       "hh3cCBQoSNestCfgInfoTable": hh3cCBQoSNestCfgInfoTable,
       "hh3cCBQoSNestCfgInfoEntry": hh3cCBQoSNestCfgInfoEntry,
       "hh3cCBQoSNestServiceVlanID": hh3cCBQoSNestServiceVlanID,
       "hh3cCBQoSNestServiceDot1pValue": hh3cCBQoSNestServiceDot1pValue,
       "hh3cCBQoSNestCustomerVlanID": hh3cCBQoSNestCustomerVlanID,
       "hh3cCBQoSNestCustomerDot1pValue": hh3cCBQoSNestCustomerDot1pValue,
       "hh3cCBQoSNestRowStatus": hh3cCBQoSNestRowStatus,
       "hh3cCBQoSNestPolicyCfgInfoTable": hh3cCBQoSNestPolicyCfgInfoTable,
       "hh3cCBQoSNestPolicyCfgInfoEntry": hh3cCBQoSNestPolicyCfgInfoEntry,
       "hh3cCBQoSNestPolicyName": hh3cCBQoSNestPolicyName,
       "hh3cCBQoSNestPolicyRowStatus": hh3cCBQoSNestPolicyRowStatus,
       "hh3cCBQoSPolicyObjects": hh3cCBQoSPolicyObjects,
       "hh3cCBQoSPolicyIndexNext": hh3cCBQoSPolicyIndexNext,
       "hh3cCBQoSPolicyCfgInfoTable": hh3cCBQoSPolicyCfgInfoTable,
       "hh3cCBQoSPolicyCfgInfoEntry": hh3cCBQoSPolicyCfgInfoEntry,
       "hh3cCBQoSPolicyIndex": hh3cCBQoSPolicyIndex,
       "hh3cCBQoSPolicyName": hh3cCBQoSPolicyName,
       "hh3cCBQoSPolicyClassCount": hh3cCBQoSPolicyClassCount,
       "hh3cCBQoSPolicyConfigMode": hh3cCBQoSPolicyConfigMode,
       "hh3cCBQoSPolicyType": hh3cCBQoSPolicyType,
       "hh3cCBQoSPolicyClassNextIndex": hh3cCBQoSPolicyClassNextIndex,
       "hh3cCBQoSPolicyRowStatus": hh3cCBQoSPolicyRowStatus,
       "hh3cCBQoSPolicyClassCfgInfoTable": hh3cCBQoSPolicyClassCfgInfoTable,
       "hh3cCBQoSPolicyClassCfgInfoEntry": hh3cCBQoSPolicyClassCfgInfoEntry,
       "hh3cCBQoSPolicyClassIndex": hh3cCBQoSPolicyClassIndex,
       "hh3cCBQoSPolicyClassClassifierIndex": hh3cCBQoSPolicyClassClassifierIndex,
       "hh3cCBQoSPolicyClassClassifierName": hh3cCBQoSPolicyClassClassifierName,
       "hh3cCBQoSPolicyClassBehaviorIndex": hh3cCBQoSPolicyClassBehaviorIndex,
       "hh3cCBQoSPolicyClassBehaviorName": hh3cCBQoSPolicyClassBehaviorName,
       "hh3cCBQoSPolicyClassPrecedence": hh3cCBQoSPolicyClassPrecedence,
       "hh3cCBQoSPolicyClassRowStatus": hh3cCBQoSPolicyClassRowStatus,
       "hh3cCBQoSPolicyClassMode": hh3cCBQoSPolicyClassMode,
       "hh3cCBQoSPolicyClassCfgOrder": hh3cCBQoSPolicyClassCfgOrder,
       "hh3cCBQoSApplyPolicyObjects": hh3cCBQoSApplyPolicyObjects,
       "hh3cCBQoSIfApplyPolicyTable": hh3cCBQoSIfApplyPolicyTable,
       "hh3cCBQoSIfApplyPolicyEntry": hh3cCBQoSIfApplyPolicyEntry,
       "hh3cCBQoSIfApplyPolicyIfIndex": hh3cCBQoSIfApplyPolicyIfIndex,
       "hh3cCBQoSIfApplyPolicyDirection": hh3cCBQoSIfApplyPolicyDirection,
       "hh3cCBQoSIfApplyPolicyName": hh3cCBQoSIfApplyPolicyName,
       "hh3cCBQoSIfApplyPolicyEnableDynamic": hh3cCBQoSIfApplyPolicyEnableDynamic,
       "hh3cCBQoSIfApplyPolicyRowStatus": hh3cCBQoSIfApplyPolicyRowStatus,
       "hh3cCBQoSAtmPvcApplyPolicyTable": hh3cCBQoSAtmPvcApplyPolicyTable,
       "hh3cCBQoSAtmPvcApplyPolicyEntry": hh3cCBQoSAtmPvcApplyPolicyEntry,
       "hh3cCBQoSAtmPvcApplyPolicyIfIndex": hh3cCBQoSAtmPvcApplyPolicyIfIndex,
       "hh3cCBQoSAtmPvcApplyPolicyVPI": hh3cCBQoSAtmPvcApplyPolicyVPI,
       "hh3cCBQoSAtmPvcApplyPolicyVCI": hh3cCBQoSAtmPvcApplyPolicyVCI,
       "hh3cCBQoSAtmPvcApplyPolicyDirection": hh3cCBQoSAtmPvcApplyPolicyDirection,
       "hh3cCBQoSAtmPvcApplyPolicyName": hh3cCBQoSAtmPvcApplyPolicyName,
       "hh3cCBQoSAtmPvcApplyPolicyRowStatus": hh3cCBQoSAtmPvcApplyPolicyRowStatus,
       "hh3cCBQoSVlanApplyPolicyTable": hh3cCBQoSVlanApplyPolicyTable,
       "hh3cCBQoSVlanApplyPolicyEntry": hh3cCBQoSVlanApplyPolicyEntry,
       "hh3cCBQoSVlanApplyPolicyVlanid": hh3cCBQoSVlanApplyPolicyVlanid,
       "hh3cCBQoSVlanApplyPolicyDirection": hh3cCBQoSVlanApplyPolicyDirection,
       "hh3cCBQoSVlanApplyPolicyName": hh3cCBQoSVlanApplyPolicyName,
       "hh3cCBQoSVlanApplyPriority": hh3cCBQoSVlanApplyPriority,
       "hh3cCBQoSVlanApplyPolicyRowStatus": hh3cCBQoSVlanApplyPolicyRowStatus,
       "hh3cCBQoSFrClassApplyPolicyTable": hh3cCBQoSFrClassApplyPolicyTable,
       "hh3cCBQoSFrClassApplyPolicyEntry": hh3cCBQoSFrClassApplyPolicyEntry,
       "hh3cCBQoSFrClassApplyPolicyFrClassName": hh3cCBQoSFrClassApplyPolicyFrClassName,
       "hh3cCBQoSFrClassApplyPolicyDirection": hh3cCBQoSFrClassApplyPolicyDirection,
       "hh3cCBQoSFrClassApplyPolicyName": hh3cCBQoSFrClassApplyPolicyName,
       "hh3cCBQoSFrClassApplyPolicyRowStatus": hh3cCBQoSFrClassApplyPolicyRowStatus,
       "hh3cCBQoSFrPvcApplyPolicyTable": hh3cCBQoSFrPvcApplyPolicyTable,
       "hh3cCBQoSFrPvcApplyPolicyEntry": hh3cCBQoSFrPvcApplyPolicyEntry,
       "hh3cCBQoSFrPvcApplyPolicyIfIndex": hh3cCBQoSFrPvcApplyPolicyIfIndex,
       "hh3cCBQoSFrPvcApplyPolicyDlciNum": hh3cCBQoSFrPvcApplyPolicyDlciNum,
       "hh3cCBQoSFrPvcApplyPolicyDirection": hh3cCBQoSFrPvcApplyPolicyDirection,
       "hh3cCBQoSFrPvcApplyPolicyName": hh3cCBQoSFrPvcApplyPolicyName,
       "hh3cCBQoSFrPvcApplyPolicyRowStatus": hh3cCBQoSFrPvcApplyPolicyRowStatus,
       "hh3cCBQoSGlobalApplyTable": hh3cCBQoSGlobalApplyTable,
       "hh3cCBQoSGlobalApplyEntry": hh3cCBQoSGlobalApplyEntry,
       "hh3cCBQoSGlobalApplyDirection": hh3cCBQoSGlobalApplyDirection,
       "hh3cCBQoSGlobalApplyName": hh3cCBQoSGlobalApplyName,
       "hh3cCBQoSGlobalApplyRowStatus": hh3cCBQoSGlobalApplyRowStatus,
       "hh3cCBQoSApplyPolicyStaticsObjects": hh3cCBQoSApplyPolicyStaticsObjects,
       "hh3cCBQoSIfStaticsObjects": hh3cCBQoSIfStaticsObjects,
       "hh3cCBQoSIfCbqRunInfoTable": hh3cCBQoSIfCbqRunInfoTable,
       "hh3cCBQoSIfCbqRunInfoEntry": hh3cCBQoSIfCbqRunInfoEntry,
       "hh3cCBQoSIfCbqQueueSize": hh3cCBQoSIfCbqQueueSize,
       "hh3cCBQoSIfCbqDiscard": hh3cCBQoSIfCbqDiscard,
       "hh3cCBQoSIfCbqEfQueueSize": hh3cCBQoSIfCbqEfQueueSize,
       "hh3cCBQoSIfCbqAfQueueSize": hh3cCBQoSIfCbqAfQueueSize,
       "hh3cCBQoSIfCbqBeQueueSize": hh3cCBQoSIfCbqBeQueueSize,
       "hh3cCBQoSIfCbqBeActiveQueueNum": hh3cCBQoSIfCbqBeActiveQueueNum,
       "hh3cCBQoSIfCbqBeMaxActiveQueueNum": hh3cCBQoSIfCbqBeMaxActiveQueueNum,
       "hh3cCBQoSIfCbqBeTotalQueueNum": hh3cCBQoSIfCbqBeTotalQueueNum,
       "hh3cCBQoSIfCbqAfAllocatedQueueNum": hh3cCBQoSIfCbqAfAllocatedQueueNum,
       "hh3cCBQoSIfClassMatchRunInfoTable": hh3cCBQoSIfClassMatchRunInfoTable,
       "hh3cCBQoSIfClassMatchRunInfoEntry": hh3cCBQoSIfClassMatchRunInfoEntry,
       "hh3cCBQoSIfClassMatchedPackets": hh3cCBQoSIfClassMatchedPackets,
       "hh3cCBQoSIfClassMatchedBytes": hh3cCBQoSIfClassMatchedBytes,
       "hh3cCBQoSIfClassAverageRate": hh3cCBQoSIfClassAverageRate,
       "hh3cCBQoSIfCarRunInfoTable": hh3cCBQoSIfCarRunInfoTable,
       "hh3cCBQoSIfCarRunInfoEntry": hh3cCBQoSIfCarRunInfoEntry,
       "hh3cCBQoSIfCarGreenPackets": hh3cCBQoSIfCarGreenPackets,
       "hh3cCBQoSIfCarGreenBytes": hh3cCBQoSIfCarGreenBytes,
       "hh3cCBQoSIfCarRedPackets": hh3cCBQoSIfCarRedPackets,
       "hh3cCBQoSIfCarRedBytes": hh3cCBQoSIfCarRedBytes,
       "hh3cCBQoSIfCarYellowPackets": hh3cCBQoSIfCarYellowPackets,
       "hh3cCBQoSIfCarYellowBytes": hh3cCBQoSIfCarYellowBytes,
       "hh3cCBQoSIfGtsRunInfoTable": hh3cCBQoSIfGtsRunInfoTable,
       "hh3cCBQoSIfGtsRunInfoEntry": hh3cCBQoSIfGtsRunInfoEntry,
       "hh3cCBQoSIfGtsPassedPackets": hh3cCBQoSIfGtsPassedPackets,
       "hh3cCBQoSIfGtsPassedBytes": hh3cCBQoSIfGtsPassedBytes,
       "hh3cCBQoSIfGtsDiscardedPackets": hh3cCBQoSIfGtsDiscardedPackets,
       "hh3cCBQoSIfGtsDiscardedBytes": hh3cCBQoSIfGtsDiscardedBytes,
       "hh3cCBQoSIfGtsDelayedPackets": hh3cCBQoSIfGtsDelayedPackets,
       "hh3cCBQoSIfGtsDelayedBytes": hh3cCBQoSIfGtsDelayedBytes,
       "hh3cCBQoSIfGtsQueueSize": hh3cCBQoSIfGtsQueueSize,
       "hh3cCBQoSIfRemarkRunInfoTable": hh3cCBQoSIfRemarkRunInfoTable,
       "hh3cCBQoSIfRemarkRunInfoEntry": hh3cCBQoSIfRemarkRunInfoEntry,
       "hh3cCBQoSIfRemarkedPackets": hh3cCBQoSIfRemarkedPackets,
       "hh3cCBQoSIfQueueRunInfoTable": hh3cCBQoSIfQueueRunInfoTable,
       "hh3cCBQoSIfQueueRunInfoEntry": hh3cCBQoSIfQueueRunInfoEntry,
       "hh3cCBQoSIfQueueMatchedPackets": hh3cCBQoSIfQueueMatchedPackets,
       "hh3cCBQoSIfQueueMatchedBytes": hh3cCBQoSIfQueueMatchedBytes,
       "hh3cCBQoSIfQueueEnqueuedPackets": hh3cCBQoSIfQueueEnqueuedPackets,
       "hh3cCBQoSIfQueueEnqueuedBytes": hh3cCBQoSIfQueueEnqueuedBytes,
       "hh3cCBQoSIfQueueDiscardedPackets": hh3cCBQoSIfQueueDiscardedPackets,
       "hh3cCBQoSIfQueueDiscardedBytes": hh3cCBQoSIfQueueDiscardedBytes,
       "hh3cCBQoSIfWredRunInfoTable": hh3cCBQoSIfWredRunInfoTable,
       "hh3cCBQoSIfWredRunInfoEntry": hh3cCBQoSIfWredRunInfoEntry,
       "hh3cCBQoSIfWredRandomDiscardedPackets": hh3cCBQoSIfWredRandomDiscardedPackets,
       "hh3cCBQoSIfWredTailDiscardedPackets": hh3cCBQoSIfWredTailDiscardedPackets,
       "hh3cCBQoSIfAccountingRunInfoTable": hh3cCBQoSIfAccountingRunInfoTable,
       "hh3cCBQoSIfAccountingRunInfoEntry": hh3cCBQoSIfAccountingRunInfoEntry,
       "hh3cCBQoSIfAccountingPackets": hh3cCBQoSIfAccountingPackets,
       "hh3cCBQoSIfAccountingBytes": hh3cCBQoSIfAccountingBytes,
       "hh3cCBQoSAtmPvcStaticsObjects": hh3cCBQoSAtmPvcStaticsObjects,
       "hh3cCBQoSAtmPvcCbqRunInfoTable": hh3cCBQoSAtmPvcCbqRunInfoTable,
       "hh3cCBQoSAtmPvcCbqRunInfoEntry": hh3cCBQoSAtmPvcCbqRunInfoEntry,
       "hh3cCBQoSAtmPvcCbqQueueSize": hh3cCBQoSAtmPvcCbqQueueSize,
       "hh3cCBQoSAtmPvcCbqDiscard": hh3cCBQoSAtmPvcCbqDiscard,
       "hh3cCBQoSAtmPvcCbqEfQueueSize": hh3cCBQoSAtmPvcCbqEfQueueSize,
       "hh3cCBQoSAtmPvcCbqAfQueueSize": hh3cCBQoSAtmPvcCbqAfQueueSize,
       "hh3cCBQoSAtmPvcCbqBeQueueSize": hh3cCBQoSAtmPvcCbqBeQueueSize,
       "hh3cCBQoSAtmPvcCbqBeActiveQueueNum": hh3cCBQoSAtmPvcCbqBeActiveQueueNum,
       "hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum": hh3cCBQoSAtmPvcCbqBeMaxActiveQueueNum,
       "hh3cCBQoSAtmPvcCbqBeTotalQueueNum": hh3cCBQoSAtmPvcCbqBeTotalQueueNum,
       "hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum": hh3cCBQoSAtmPvcCbqAfAllocatedQueueNum,
       "hh3cCBQoSAtmPvcClassMatchRunInfoTable": hh3cCBQoSAtmPvcClassMatchRunInfoTable,
       "hh3cCBQoSAtmPvcClassMatchRunInfoEntry": hh3cCBQoSAtmPvcClassMatchRunInfoEntry,
       "hh3cCBQoSAtmPvcClassMatchPackets": hh3cCBQoSAtmPvcClassMatchPackets,
       "hh3cCBQoSAtmPvcClassMatchBytes": hh3cCBQoSAtmPvcClassMatchBytes,
       "hh3cCBQoSAtmPvcClassAverageRate": hh3cCBQoSAtmPvcClassAverageRate,
       "hh3cCBQoSAtmPvcCarRunInfoTable": hh3cCBQoSAtmPvcCarRunInfoTable,
       "hh3cCBQoSAtmPvcCarRunInfoEntry": hh3cCBQoSAtmPvcCarRunInfoEntry,
       "hh3cCBQoSAtmPvcCarConformPackets": hh3cCBQoSAtmPvcCarConformPackets,
       "hh3cCBQoSAtmPvcCarConformBytes": hh3cCBQoSAtmPvcCarConformBytes,
       "hh3cCBQoSAtmPvcCarExceedPackets": hh3cCBQoSAtmPvcCarExceedPackets,
       "hh3cCBQoSAtmPvcCarExceedBytes": hh3cCBQoSAtmPvcCarExceedBytes,
       "hh3cCBQoSAtmPvcGtsRunInfoTable": hh3cCBQoSAtmPvcGtsRunInfoTable,
       "hh3cCBQoSAtmPvcGtsRunInfoEntry": hh3cCBQoSAtmPvcGtsRunInfoEntry,
       "hh3cCBQoSAtmPvcGtsPassedPackets": hh3cCBQoSAtmPvcGtsPassedPackets,
       "hh3cCBQoSAtmPvcGtsPassedBytes": hh3cCBQoSAtmPvcGtsPassedBytes,
       "hh3cCBQoSAtmPvcGtsDiscardedPackets": hh3cCBQoSAtmPvcGtsDiscardedPackets,
       "hh3cCBQoSAtmPvcGtsDiscardedBytes": hh3cCBQoSAtmPvcGtsDiscardedBytes,
       "hh3cCBQoSAtmPvcGtsDelayedPackets": hh3cCBQoSAtmPvcGtsDelayedPackets,
       "hh3cCBQoSAtmPvcGtsDelayedBytes": hh3cCBQoSAtmPvcGtsDelayedBytes,
       "hh3cCBQoSAtmPvcGtsQueueSize": hh3cCBQoSAtmPvcGtsQueueSize,
       "hh3cCBQoSAtmPvcRemarkRunInfoTable": hh3cCBQoSAtmPvcRemarkRunInfoTable,
       "hh3cCBQoSAtmPvcRemarkRunInfoEntry": hh3cCBQoSAtmPvcRemarkRunInfoEntry,
       "hh3cCBQoSAtmPvcRemarkedPackets": hh3cCBQoSAtmPvcRemarkedPackets,
       "hh3cCBQoSAtmPvcQueueRunInfoTable": hh3cCBQoSAtmPvcQueueRunInfoTable,
       "hh3cCBQoSAtmPvcQueueRunInfoEntry": hh3cCBQoSAtmPvcQueueRunInfoEntry,
       "hh3cCBQoSAtmPvcQueueMatchedPackets": hh3cCBQoSAtmPvcQueueMatchedPackets,
       "hh3cCBQoSAtmPvcQueueMatchedBytes": hh3cCBQoSAtmPvcQueueMatchedBytes,
       "hh3cCBQoSAtmPvcQueueEnqueuedPackets": hh3cCBQoSAtmPvcQueueEnqueuedPackets,
       "hh3cCBQoSAtmPvcQueueEnqueuedBytes": hh3cCBQoSAtmPvcQueueEnqueuedBytes,
       "hh3cCBQoSAtmPvcQueueDiscardedPackets": hh3cCBQoSAtmPvcQueueDiscardedPackets,
       "hh3cCBQoSAtmPvcQueueDiscardedBytes": hh3cCBQoSAtmPvcQueueDiscardedBytes,
       "hh3cCBQoSAtmPvcWredRunInfoTable": hh3cCBQoSAtmPvcWredRunInfoTable,
       "hh3cCBQoSAtmPvcWredRunInfoEntry": hh3cCBQoSAtmPvcWredRunInfoEntry,
       "hh3cCBQoSAtmPvcWredRandomDiscardedPackets": hh3cCBQoSAtmPvcWredRandomDiscardedPackets,
       "hh3cCBQoSAtmPvcWredTailDiscardedPackets": hh3cCBQoSAtmPvcWredTailDiscardedPackets,
       "hh3cCBQoSAtmPvcAccountingRunInfoTable": hh3cCBQoSAtmPvcAccountingRunInfoTable,
       "hh3cCBQoSAtmPvcAccountingRunInfoEntry": hh3cCBQoSAtmPvcAccountingRunInfoEntry,
       "hh3cCBQoSAtmPvcAccountingPackets": hh3cCBQoSAtmPvcAccountingPackets,
       "hh3cCBQoSAtmPvcAccountingBytes": hh3cCBQoSAtmPvcAccountingBytes,
       "hh3cCBQoSFrPvcStaticsObjects": hh3cCBQoSFrPvcStaticsObjects,
       "hh3cCBQoSFrPvcCbqRunInfoTable": hh3cCBQoSFrPvcCbqRunInfoTable,
       "hh3cCBQoSFrPvcCbqRunInfoEntry": hh3cCBQoSFrPvcCbqRunInfoEntry,
       "hh3cCBQoSFrPvcCbqQueueSize": hh3cCBQoSFrPvcCbqQueueSize,
       "hh3cCBQoSFrPvcCbqDiscard": hh3cCBQoSFrPvcCbqDiscard,
       "hh3cCBQoSFrPvcCbqEfQueueSize": hh3cCBQoSFrPvcCbqEfQueueSize,
       "hh3cCBQoSFrPvcCbqAfQueueSize": hh3cCBQoSFrPvcCbqAfQueueSize,
       "hh3cCBQoSFrPvcCbqBeQueueSize": hh3cCBQoSFrPvcCbqBeQueueSize,
       "hh3cCBQoSFrPvcCbqBeActiveQueueNum": hh3cCBQoSFrPvcCbqBeActiveQueueNum,
       "hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum": hh3cCBQoSFrPvcCbqBeMaxActiveQueueNum,
       "hh3cCBQoSFrPvcCbqBeTotalQueueNum": hh3cCBQoSFrPvcCbqBeTotalQueueNum,
       "hh3cCBQoSFrPvcCbqAfAllocatedQueueNum": hh3cCBQoSFrPvcCbqAfAllocatedQueueNum,
       "hh3cCBQoSFrPvcClassMatchRunInfoTable": hh3cCBQoSFrPvcClassMatchRunInfoTable,
       "hh3cCBQoSFrPvcClassMatchRunInfoEntry": hh3cCBQoSFrPvcClassMatchRunInfoEntry,
       "hh3cCBQoSFrPvcClassMatchedPackets": hh3cCBQoSFrPvcClassMatchedPackets,
       "hh3cCBQoSFrPvcClassMatchedBytes": hh3cCBQoSFrPvcClassMatchedBytes,
       "hh3cCBQoSFrPvcClassAverageRate": hh3cCBQoSFrPvcClassAverageRate,
       "hh3cCBQoSFrPvcCarRunInfoTable": hh3cCBQoSFrPvcCarRunInfoTable,
       "hh3cCBQoSFrPvcCarRunInfoEntry": hh3cCBQoSFrPvcCarRunInfoEntry,
       "hh3cCBQoSFrPvcCarConformPackets": hh3cCBQoSFrPvcCarConformPackets,
       "hh3cCBQoSFrPvcCarConformBytes": hh3cCBQoSFrPvcCarConformBytes,
       "hh3cCBQoSFrPvcCarExceedPackets": hh3cCBQoSFrPvcCarExceedPackets,
       "hh3cCBQoSFrPvcCarExceedBytes": hh3cCBQoSFrPvcCarExceedBytes,
       "hh3cCBQoSFrPvcGtsRunInfoTable": hh3cCBQoSFrPvcGtsRunInfoTable,
       "hh3cCBQoSFrPvcGtsRunInfoEntry": hh3cCBQoSFrPvcGtsRunInfoEntry,
       "hh3cCBQoSFrPvcGtsPassedPackets": hh3cCBQoSFrPvcGtsPassedPackets,
       "hh3cCBQoSFrPvcGtsPassedBytes": hh3cCBQoSFrPvcGtsPassedBytes,
       "hh3cCBQoSFrPvcGtsDiscardedPackets": hh3cCBQoSFrPvcGtsDiscardedPackets,
       "hh3cCBQoSFrPvcGtsDiscardedBytes": hh3cCBQoSFrPvcGtsDiscardedBytes,
       "hh3cCBQoSFrPvcGtsDelayedPackets": hh3cCBQoSFrPvcGtsDelayedPackets,
       "hh3cCBQoSFrPvcGtsDelayedBytes": hh3cCBQoSFrPvcGtsDelayedBytes,
       "hh3cCBQoSFrPvcGtsQueueSize": hh3cCBQoSFrPvcGtsQueueSize,
       "hh3cCBQoSFrPvcRemarkRunInfoTable": hh3cCBQoSFrPvcRemarkRunInfoTable,
       "hh3cCBQoSFrPvcRemarkRunInfoEntry": hh3cCBQoSFrPvcRemarkRunInfoEntry,
       "hh3cCBQoSFrPvcRemarkedPackets": hh3cCBQoSFrPvcRemarkedPackets,
       "hh3cCBQoSFrPvcQueueRunInfoTable": hh3cCBQoSFrPvcQueueRunInfoTable,
       "hh3cCBQoSFrPvcQueueRunInfoEntry": hh3cCBQoSFrPvcQueueRunInfoEntry,
       "hh3cCBQoSFrPvcQueueMatchedPackets": hh3cCBQoSFrPvcQueueMatchedPackets,
       "hh3cCBQoSFrPvcQueueMatchedBytes": hh3cCBQoSFrPvcQueueMatchedBytes,
       "hh3cCBQoSFrPvcQueueEnqueuedPackets": hh3cCBQoSFrPvcQueueEnqueuedPackets,
       "hh3cCBQoSFrPvcQueueEnqueuedBytes": hh3cCBQoSFrPvcQueueEnqueuedBytes,
       "hh3cCBQoSFrPvcQueueDiscardedPackets": hh3cCBQoSFrPvcQueueDiscardedPackets,
       "hh3cCBQoSFrPvcQueueDiscardedBytes": hh3cCBQoSFrPvcQueueDiscardedBytes,
       "hh3cCBQoSFrPvcWredRunInfoTable": hh3cCBQoSFrPvcWredRunInfoTable,
       "hh3cCBQoSFrPvcWredRunInfoEntry": hh3cCBQoSFrPvcWredRunInfoEntry,
       "hh3cCBQoSFrPvcWredRandomDiscardedPackets": hh3cCBQoSFrPvcWredRandomDiscardedPackets,
       "hh3cCBQoSFrPvcWredTailDiscardedPackets": hh3cCBQoSFrPvcWredTailDiscardedPackets,
       "hh3cCBQoSFrPvcAccountingRunInfoTable": hh3cCBQoSFrPvcAccountingRunInfoTable,
       "hh3cCBQoSFrPvcAccountingRunInfoEntry": hh3cCBQoSFrPvcAccountingRunInfoEntry,
       "hh3cCBQoSFrPvcAccountingPackets": hh3cCBQoSFrPvcAccountingPackets,
       "hh3cCBQoSFrPvcAccountingBytes": hh3cCBQoSFrPvcAccountingBytes,
       "hh3cCBQoSVlanStaticsObjects": hh3cCBQoSVlanStaticsObjects,
       "hh3cCBQoSVlanClassMatchRunInfoTable": hh3cCBQoSVlanClassMatchRunInfoTable,
       "hh3cCBQoSVlanClassMatchRunInfoEntry": hh3cCBQoSVlanClassMatchRunInfoEntry,
       "hh3cCBQoSVlanClassMatchedPackets": hh3cCBQoSVlanClassMatchedPackets,
       "hh3cCBQoSVlanAccountingRunInfoTable": hh3cCBQoSVlanAccountingRunInfoTable,
       "hh3cCBQoSVlanAccountingRunInfoEntry": hh3cCBQoSVlanAccountingRunInfoEntry,
       "hh3cCBQoSVlanAccountingPackets": hh3cCBQoSVlanAccountingPackets,
       "hh3cCBQoSVlanAccountingBytes": hh3cCBQoSVlanAccountingBytes,
       "hh3cCBQoSApplyPolicyIndexObjects": hh3cCBQoSApplyPolicyIndexObjects,
       "hh3cCBQoSApplyObjectTable": hh3cCBQoSApplyObjectTable,
       "hh3cCBQoSApplyObjectEntry": hh3cCBQoSApplyObjectEntry,
       "hh3cCBQoSApplyObjectIndex": hh3cCBQoSApplyObjectIndex,
       "hh3cCBQoSApplyObjectType": hh3cCBQoSApplyObjectType,
       "hh3cCBQoSApplyObjectDirection": hh3cCBQoSApplyObjectDirection,
       "hh3cCBQoSApplyObjectMainSite": hh3cCBQoSApplyObjectMainSite,
       "hh3cCBQoSApplyObjectSubChannel": hh3cCBQoSApplyObjectSubChannel,
       "hh3cCBQoSApplyObjectSubClass": hh3cCBQoSApplyObjectSubClass,
       "hh3cCBQoSApplyObjectSubClassSec": hh3cCBQoSApplyObjectSubClassSec,
       "hh3cCBQoSIntApplyObjectTable": hh3cCBQoSIntApplyObjectTable,
       "hh3cCBQoSIntApplyObjectEntry": hh3cCBQoSIntApplyObjectEntry,
       "hh3cCBQoSIntApplyObjectIfIndex": hh3cCBQoSIntApplyObjectIfIndex,
       "hh3cCBQoSIntApplyObjectIndex": hh3cCBQoSIntApplyObjectIndex,
       "hh3cCBQoSVlanApplyObjectTable": hh3cCBQoSVlanApplyObjectTable,
       "hh3cCBQoSVlanApplyObjectEntry": hh3cCBQoSVlanApplyObjectEntry,
       "hh3cCBQoSVlanApplyObjectVlanID": hh3cCBQoSVlanApplyObjectVlanID,
       "hh3cCBQoSVlanApplyObjectIndex": hh3cCBQoSVlanApplyObjectIndex,
       "hh3cCBQoSPvcApplyObjectTable": hh3cCBQoSPvcApplyObjectTable,
       "hh3cCBQoSPvcApplyObjectEntry": hh3cCBQoSPvcApplyObjectEntry,
       "hh3cCBQoSPvcApplyObjectIfIndex": hh3cCBQoSPvcApplyObjectIfIndex,
       "hh3cCBQoSPvcApplyObjectPvcID": hh3cCBQoSPvcApplyObjectPvcID,
       "hh3cCBQoSPvcApplyObjectIndex": hh3cCBQoSPvcApplyObjectIndex,
       "hh3cCBQoSNestPolicyApplyObjectTable": hh3cCBQoSNestPolicyApplyObjectTable,
       "hh3cCBQoSNestPolicyApplyObjectEntry": hh3cCBQoSNestPolicyApplyObjectEntry,
       "hh3cCBQoSNestPolicyClassIndex": hh3cCBQoSNestPolicyClassIndex,
       "hh3cCBQoSNestPolicyApplyObjectIndex": hh3cCBQoSNestPolicyApplyObjectIndex,
       "hh3cCBQoSStaticsObjects": hh3cCBQoSStaticsObjects,
       "hh3cCBQoSCbqRunInfoTable": hh3cCBQoSCbqRunInfoTable,
       "hh3cCBQoSCbqRunInfoEntry": hh3cCBQoSCbqRunInfoEntry,
       "hh3cCBQoSCbqQueueSize": hh3cCBQoSCbqQueueSize,
       "hh3cCBQoSCbqDiscard": hh3cCBQoSCbqDiscard,
       "hh3cCBQoSCbqEfQueueSize": hh3cCBQoSCbqEfQueueSize,
       "hh3cCBQoSCbqAfQueueSize": hh3cCBQoSCbqAfQueueSize,
       "hh3cCBQoSCbqBeQueueSize": hh3cCBQoSCbqBeQueueSize,
       "hh3cCBQoSCbqBeActiveQueueNum": hh3cCBQoSCbqBeActiveQueueNum,
       "hh3cCBQoSCbqBeMaxActiveQueueNum": hh3cCBQoSCbqBeMaxActiveQueueNum,
       "hh3cCBQoSCbqBeTotalQueueNum": hh3cCBQoSCbqBeTotalQueueNum,
       "hh3cCBQoSCbqAfAllocatedQueueNum": hh3cCBQoSCbqAfAllocatedQueueNum,
       "hh3cCBQoSClassMatchRunInfoTable": hh3cCBQoSClassMatchRunInfoTable,
       "hh3cCBQoSClassMatchRunInfoEntry": hh3cCBQoSClassMatchRunInfoEntry,
       "hh3cCBQoSClassMatchedPackets": hh3cCBQoSClassMatchedPackets,
       "hh3cCBQoSClassMatchedBytes": hh3cCBQoSClassMatchedBytes,
       "hh3cCBQoSClassFwdPktpps": hh3cCBQoSClassFwdPktpps,
       "hh3cCBQoSClassFwdPktbps": hh3cCBQoSClassFwdPktbps,
       "hh3cCBQoSClassDropPktpps": hh3cCBQoSClassDropPktpps,
       "hh3cCBQoSClassDropPktbps": hh3cCBQoSClassDropPktbps,
       "hh3cCBQoSClassFlowStatInterval": hh3cCBQoSClassFlowStatInterval,
       "hh3cCBQoSClassBehaviorStatus": hh3cCBQoSClassBehaviorStatus,
       "hh3cCBQoSCarRunInfoTable": hh3cCBQoSCarRunInfoTable,
       "hh3cCBQoSCarRunInfoEntry": hh3cCBQoSCarRunInfoEntry,
       "hh3cCBQoSCarGreenPackets": hh3cCBQoSCarGreenPackets,
       "hh3cCBQoSCarGreenBytes": hh3cCBQoSCarGreenBytes,
       "hh3cCBQoSCarRedPackets": hh3cCBQoSCarRedPackets,
       "hh3cCBQoSCarRedBytes": hh3cCBQoSCarRedBytes,
       "hh3cCBQoSCarYellowPackets": hh3cCBQoSCarYellowPackets,
       "hh3cCBQoSCarYellowBytes": hh3cCBQoSCarYellowBytes,
       "hh3cCBQoSGtsRunInfoTable": hh3cCBQoSGtsRunInfoTable,
       "hh3cCBQoSGtsRunInfoEntry": hh3cCBQoSGtsRunInfoEntry,
       "hh3cCBQoSGtsPassedPackets": hh3cCBQoSGtsPassedPackets,
       "hh3cCBQoSGtsPassedBytes": hh3cCBQoSGtsPassedBytes,
       "hh3cCBQoSGtsDiscardedPackets": hh3cCBQoSGtsDiscardedPackets,
       "hh3cCBQoSGtsDiscardedBytes": hh3cCBQoSGtsDiscardedBytes,
       "hh3cCBQoSGtsDelayedPackets": hh3cCBQoSGtsDelayedPackets,
       "hh3cCBQoSGtsDelayedBytes": hh3cCBQoSGtsDelayedBytes,
       "hh3cCBQoSGtsQueueSize": hh3cCBQoSGtsQueueSize,
       "hh3cCBQoSRemarkRunInfoTable": hh3cCBQoSRemarkRunInfoTable,
       "hh3cCBQoSRemarkRunInfoEntry": hh3cCBQoSRemarkRunInfoEntry,
       "hh3cCBQoSRemarkedPackets": hh3cCBQoSRemarkedPackets,
       "hh3cCBQoSQueueRunInfoTable": hh3cCBQoSQueueRunInfoTable,
       "hh3cCBQoSQueueRunInfoEntry": hh3cCBQoSQueueRunInfoEntry,
       "hh3cCBQoSQueueMatchedPackets": hh3cCBQoSQueueMatchedPackets,
       "hh3cCBQoSQueueMatchedBytes": hh3cCBQoSQueueMatchedBytes,
       "hh3cCBQoSQueueEnqueuedPackets": hh3cCBQoSQueueEnqueuedPackets,
       "hh3cCBQoSQueueEnqueuedBytes": hh3cCBQoSQueueEnqueuedBytes,
       "hh3cCBQoSQueueDiscardedPackets": hh3cCBQoSQueueDiscardedPackets,
       "hh3cCBQoSQueueDiscardedBytes": hh3cCBQoSQueueDiscardedBytes,
       "hh3cCBQoSWredRunInfoTable": hh3cCBQoSWredRunInfoTable,
       "hh3cCBQoSWredRunInfoEntry": hh3cCBQoSWredRunInfoEntry,
       "hh3cCBQoSWredRandomDiscardedPackets": hh3cCBQoSWredRandomDiscardedPackets,
       "hh3cCBQoSWredTailDiscardedPackets": hh3cCBQoSWredTailDiscardedPackets,
       "hh3cCBQoSAccountingRunInfoTable": hh3cCBQoSAccountingRunInfoTable,
       "hh3cCBQoSAccountingRunInfoEntry": hh3cCBQoSAccountingRunInfoEntry,
       "hh3cCBQoSAccountingPackets": hh3cCBQoSAccountingPackets,
       "hh3cCBQoSAccountingBytes": hh3cCBQoSAccountingBytes,
       "hh3cCBQoSApplyingStatusObjects": hh3cCBQoSApplyingStatusObjects,
       "hh3cCBQoSApplyingStatus": hh3cCBQoSApplyingStatus,
       "hh3cCBQoSNotifications": hh3cCBQoSNotifications,
       "hh3cCBQoSNotificationsPrefix": hh3cCBQoSNotificationsPrefix,
       "hh3cCBQoSIfPolicyChanged": hh3cCBQoSIfPolicyChanged,
       "hh3cCBQoSVlanPolicyChanged": hh3cCBQoSVlanPolicyChanged}
)
