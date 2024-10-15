# SNMP MIB module (A3COM-HUAWEI-CBQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-CBQOS-MIB
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

(hwQoS,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "hwQoS")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwCBQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1)
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
              16,
              17,
              25)
        )
    )
    namedValues = NamedValues(
        *(("typeAcl", 2),
          ("typeAny", 1),
          ("typeClassifier", 11),
          ("typeDestinationMac", 10),
          ("typeDscp", 6),
          ("typeInboundInterface", 12),
          ("typeIpPrec", 5),
          ("typeMacGroup", 13),
          ("typeMatchClp", 17),
          ("typeMatchDe", 16),
          ("typeMplsExp", 8),
          ("typeOutboundInterface", 25),
          ("typeProtocol", 4),
          ("typeRtpPort", 3),
          ("typeSourceMac", 9),
          ("typeVlan8021p", 7))
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1),
          ("remark", 6),
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("typeAtmClp", 5),
          ("typeDscp", 2),
          ("typeFrDe", 6),
          ("typeIpPrec", 1),
          ("typeMplsExp", 3),
          ("typeVlan8021p", 4))
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
        *(("typeDscpbased", 2),
          ("typeIpPrecbased", 1))
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
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unitAbsolute", 1),
          ("unitPercent", 2),
          ("unitRemainPercent", 3),
          ("unitUnavailable", -1))
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



# MIB Managed Objects in the order of their OIDs

_HwCBQoSObjects_ObjectIdentity = ObjectIdentity
hwCBQoSObjects = _HwCBQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1)
)
_HwCBQoSClassifierObjects_ObjectIdentity = ObjectIdentity
hwCBQoSClassifierObjects = _HwCBQoSClassifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1)
)
_HwCBQoSClassifierIndexNext_Type = Integer32
_HwCBQoSClassifierIndexNext_Object = MibScalar
hwCBQoSClassifierIndexNext = _HwCBQoSClassifierIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 1),
    _HwCBQoSClassifierIndexNext_Type()
)
hwCBQoSClassifierIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierIndexNext.setStatus("current")
_HwCBQoSClassifierCfgInfoTable_Object = MibTable
hwCBQoSClassifierCfgInfoTable = _HwCBQoSClassifierCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierCfgInfoTable.setStatus("current")
_HwCBQoSClassifierCfgInfoEntry_Object = MibTableRow
hwCBQoSClassifierCfgInfoEntry = _HwCBQoSClassifierCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1)
)
hwCBQoSClassifierCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSClassifierIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSClassifierCfgInfoEntry.setStatus("current")
_HwCBQoSClassifierIndex_Type = Integer32
_HwCBQoSClassifierIndex_Object = MibTableColumn
hwCBQoSClassifierIndex = _HwCBQoSClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1, 1),
    _HwCBQoSClassifierIndex_Type()
)
hwCBQoSClassifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSClassifierIndex.setStatus("current")


class _HwCBQoSClassifierName_Type(OctetString):
    """Custom type hwCBQoSClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSClassifierName_Type.__name__ = "OctetString"
_HwCBQoSClassifierName_Object = MibTableColumn
hwCBQoSClassifierName = _HwCBQoSClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1, 2),
    _HwCBQoSClassifierName_Type()
)
hwCBQoSClassifierName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierName.setStatus("current")
_HwCBQoSClassifierRuleCount_Type = Integer32
_HwCBQoSClassifierRuleCount_Object = MibTableColumn
hwCBQoSClassifierRuleCount = _HwCBQoSClassifierRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1, 3),
    _HwCBQoSClassifierRuleCount_Type()
)
hwCBQoSClassifierRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSClassifierRuleCount.setStatus("current")


class _HwCBQoSClassifierOperator_Type(Integer32):
    """Custom type hwCBQoSClassifierOperator based on Integer32"""
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


_HwCBQoSClassifierOperator_Type.__name__ = "Integer32"
_HwCBQoSClassifierOperator_Object = MibTableColumn
hwCBQoSClassifierOperator = _HwCBQoSClassifierOperator_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1, 5),
    _HwCBQoSClassifierLayer_Type()
)
hwCBQoSClassifierLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierLayer.setStatus("current")
_HwCBQoSClassifierRowStatus_Type = RowStatus
_HwCBQoSClassifierRowStatus_Object = MibTableColumn
hwCBQoSClassifierRowStatus = _HwCBQoSClassifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 2, 1, 6),
    _HwCBQoSClassifierRowStatus_Type()
)
hwCBQoSClassifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSClassifierRowStatus.setStatus("current")
_HwCBQoSMatchRuleCfgInfoTable_Object = MibTable
hwCBQoSMatchRuleCfgInfoTable = _HwCBQoSMatchRuleCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleCfgInfoTable.setStatus("current")
_HwCBQoSMatchRuleCfgInfoEntry_Object = MibTableRow
hwCBQoSMatchRuleCfgInfoEntry = _HwCBQoSMatchRuleCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1)
)
hwCBQoSMatchRuleCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSClassifierIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSMatchRuleIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleCfgInfoEntry.setStatus("current")
_HwCBQoSMatchRuleIndex_Type = Integer32
_HwCBQoSMatchRuleIndex_Object = MibTableColumn
hwCBQoSMatchRuleIndex = _HwCBQoSMatchRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 1),
    _HwCBQoSMatchRuleIndex_Type()
)
hwCBQoSMatchRuleIndex.setMaxAccess("not-accessible")
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
          ("match-Not", 2))
    )


_HwCBQoSMatchRuleIfNot_Type.__name__ = "Integer32"
_HwCBQoSMatchRuleIfNot_Object = MibTableColumn
hwCBQoSMatchRuleIfNot = _HwCBQoSMatchRuleIfNot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 2),
    _HwCBQoSMatchRuleIfNot_Type()
)
hwCBQoSMatchRuleIfNot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIfNot.setStatus("current")
_HwCBQoSMatchRuleType_Type = MatchRuleType
_HwCBQoSMatchRuleType_Object = MibTableColumn
hwCBQoSMatchRuleType = _HwCBQoSMatchRuleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 4),
    _HwCBQoSMatchRuleStringValue_Type()
)
hwCBQoSMatchRuleStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleStringValue.setStatus("current")
_HwCBQoSMatchRuleIntValue1_Type = Unsigned32
_HwCBQoSMatchRuleIntValue1_Object = MibTableColumn
hwCBQoSMatchRuleIntValue1 = _HwCBQoSMatchRuleIntValue1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 5),
    _HwCBQoSMatchRuleIntValue1_Type()
)
hwCBQoSMatchRuleIntValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIntValue1.setStatus("current")
_HwCBQoSMatchRuleIntValue2_Type = Unsigned32
_HwCBQoSMatchRuleIntValue2_Object = MibTableColumn
hwCBQoSMatchRuleIntValue2 = _HwCBQoSMatchRuleIntValue2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 6),
    _HwCBQoSMatchRuleIntValue2_Type()
)
hwCBQoSMatchRuleIntValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleIntValue2.setStatus("current")
_HwCBQoSMatchRuleRowStatus_Type = RowStatus
_HwCBQoSMatchRuleRowStatus_Object = MibTableColumn
hwCBQoSMatchRuleRowStatus = _HwCBQoSMatchRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 1, 3, 1, 7),
    _HwCBQoSMatchRuleRowStatus_Type()
)
hwCBQoSMatchRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSMatchRuleRowStatus.setStatus("current")
_HwCBQoSBehaviorObjects_ObjectIdentity = ObjectIdentity
hwCBQoSBehaviorObjects = _HwCBQoSBehaviorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2)
)
_HwCBQoSBehaviorIndexNext_Type = Integer32
_HwCBQoSBehaviorIndexNext_Object = MibScalar
hwCBQoSBehaviorIndexNext = _HwCBQoSBehaviorIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 1),
    _HwCBQoSBehaviorIndexNext_Type()
)
hwCBQoSBehaviorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorIndexNext.setStatus("current")
_HwCBQoSBehaviorCfgInfoTable_Object = MibTable
hwCBQoSBehaviorCfgInfoTable = _HwCBQoSBehaviorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSBehaviorCfgInfoTable.setStatus("current")
_HwCBQoSBehaviorCfgInfoEntry_Object = MibTableRow
hwCBQoSBehaviorCfgInfoEntry = _HwCBQoSBehaviorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 2, 1)
)
hwCBQoSBehaviorCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSBehaviorCfgInfoEntry.setStatus("current")
_HwCBQoSBehaviorIndex_Type = Integer32
_HwCBQoSBehaviorIndex_Object = MibTableColumn
hwCBQoSBehaviorIndex = _HwCBQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 2, 1, 1),
    _HwCBQoSBehaviorIndex_Type()
)
hwCBQoSBehaviorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorIndex.setStatus("current")


class _HwCBQoSBehaviorName_Type(OctetString):
    """Custom type hwCBQoSBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSBehaviorName_Type.__name__ = "OctetString"
_HwCBQoSBehaviorName_Object = MibTableColumn
hwCBQoSBehaviorName = _HwCBQoSBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 2, 1, 2),
    _HwCBQoSBehaviorName_Type()
)
hwCBQoSBehaviorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorName.setStatus("current")
_HwCBQoSBehaviorRowStatus_Type = RowStatus
_HwCBQoSBehaviorRowStatus_Object = MibTableColumn
hwCBQoSBehaviorRowStatus = _HwCBQoSBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 2, 1, 3),
    _HwCBQoSBehaviorRowStatus_Type()
)
hwCBQoSBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSBehaviorRowStatus.setStatus("current")
_HwCBQoSCarCfgInfoTable_Object = MibTable
hwCBQoSCarCfgInfoTable = _HwCBQoSCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSCarCfgInfoTable.setStatus("current")
_HwCBQoSCarCfgInfoEntry_Object = MibTableRow
hwCBQoSCarCfgInfoEntry = _HwCBQoSCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1)
)
hwCBQoSCarCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSCarCfgInfoEntry.setStatus("current")


class _HwCBQoSCarCir_Type(Integer32):
    """Custom type hwCBQoSCarCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 10000000),
    )


_HwCBQoSCarCir_Type.__name__ = "Integer32"
_HwCBQoSCarCir_Object = MibTableColumn
hwCBQoSCarCir = _HwCBQoSCarCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 1),
    _HwCBQoSCarCir_Type()
)
hwCBQoSCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarCir.setStatus("current")


class _HwCBQoSCarCbs_Type(Integer32):
    """Custom type hwCBQoSCarCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 19375000),
    )


_HwCBQoSCarCbs_Type.__name__ = "Integer32"
_HwCBQoSCarCbs_Object = MibTableColumn
hwCBQoSCarCbs = _HwCBQoSCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 2),
    _HwCBQoSCarCbs_Type()
)
hwCBQoSCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarCbs.setStatus("current")


class _HwCBQoSCarEbs_Type(Integer32):
    """Custom type hwCBQoSCarEbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 19375000),
    )


_HwCBQoSCarEbs_Type.__name__ = "Integer32"
_HwCBQoSCarEbs_Object = MibTableColumn
hwCBQoSCarEbs = _HwCBQoSCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 3),
    _HwCBQoSCarEbs_Type()
)
hwCBQoSCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarEbs.setStatus("current")


class _HwCBQoSCarPir_Type(Integer32):
    """Custom type hwCBQoSCarPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(100, 10000000),
    )


_HwCBQoSCarPir_Type.__name__ = "Integer32"
_HwCBQoSCarPir_Object = MibTableColumn
hwCBQoSCarPir = _HwCBQoSCarPir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 4),
    _HwCBQoSCarPir_Type()
)
hwCBQoSCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarPir.setStatus("current")


class _HwCBQoSCarPbs_Type(Integer32):
    """Custom type hwCBQoSCarPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(64, 4000000),
    )


_HwCBQoSCarPbs_Type.__name__ = "Integer32"
_HwCBQoSCarPbs_Object = MibTableColumn
hwCBQoSCarPbs = _HwCBQoSCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 5),
    _HwCBQoSCarPbs_Type()
)
hwCBQoSCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarPbs.setStatus("current")


class _HwCBQoSCarGreenAction_Type(CarAction):
    """Custom type hwCBQoSCarGreenAction based on CarAction"""


_HwCBQoSCarGreenAction_Object = MibTableColumn
hwCBQoSCarGreenAction = _HwCBQoSCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 6),
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
        ValueRangeConstraint(0, 63),
    )


_HwCBQoSCarGreenRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSCarGreenRemarkValue_Object = MibTableColumn
hwCBQoSCarGreenRemarkValue = _HwCBQoSCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 7),
    _HwCBQoSCarGreenRemarkValue_Type()
)
hwCBQoSCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarGreenRemarkValue.setStatus("current")


class _HwCBQoSCarYellowAction_Type(Integer32):
    """Custom type hwCBQoSCarYellowAction based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1),
          ("remark", 6),
          ("remarkDscp", 4),
          ("remarkIpPrec", 3),
          ("remarkMplsExp", 5),
          ("unavailable", -1))
    )


_HwCBQoSCarYellowAction_Type.__name__ = "Integer32"
_HwCBQoSCarYellowAction_Object = MibTableColumn
hwCBQoSCarYellowAction = _HwCBQoSCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 8),
    _HwCBQoSCarYellowAction_Type()
)
hwCBQoSCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarYellowAction.setStatus("current")


class _HwCBQoSCarRedAction_Type(CarAction):
    """Custom type hwCBQoSCarRedAction based on CarAction"""


_HwCBQoSCarRedAction_Object = MibTableColumn
hwCBQoSCarRedAction = _HwCBQoSCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 9),
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
        ValueRangeConstraint(0, 63),
    )


_HwCBQoSCarRedRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSCarRedRemarkValue_Object = MibTableColumn
hwCBQoSCarRedRemarkValue = _HwCBQoSCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 10),
    _HwCBQoSCarRedRemarkValue_Type()
)
hwCBQoSCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarRedRemarkValue.setStatus("current")
_HwCBQoSCarRowStatus_Type = RowStatus
_HwCBQoSCarRowStatus_Object = MibTableColumn
hwCBQoSCarRowStatus = _HwCBQoSCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 3, 1, 11),
    _HwCBQoSCarRowStatus_Type()
)
hwCBQoSCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSCarRowStatus.setStatus("current")
_HwCBQoSGtsCfgInfoTable_Object = MibTable
hwCBQoSGtsCfgInfoTable = _HwCBQoSGtsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSGtsCfgInfoTable.setStatus("current")
_HwCBQoSGtsCfgInfoEntry_Object = MibTableRow
hwCBQoSGtsCfgInfoEntry = _HwCBQoSGtsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4, 1)
)
hwCBQoSGtsCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSGtsCfgInfoEntry.setStatus("current")


class _HwCBQoSGtsCir_Type(Integer32):
    """Custom type hwCBQoSGtsCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_HwCBQoSGtsCir_Type.__name__ = "Integer32"
_HwCBQoSGtsCir_Object = MibTableColumn
hwCBQoSGtsCir = _HwCBQoSGtsCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4, 1, 4),
    _HwCBQoSGtsQueueLength_Type()
)
hwCBQoSGtsQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsQueueLength.setStatus("current")
_HwCBQoSGtsRowStatus_Type = RowStatus
_HwCBQoSGtsRowStatus_Object = MibTableColumn
hwCBQoSGtsRowStatus = _HwCBQoSGtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 4, 1, 5),
    _HwCBQoSGtsRowStatus_Type()
)
hwCBQoSGtsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSGtsRowStatus.setStatus("current")
_HwCBQoSRemarkCfgInfoTable_Object = MibTable
hwCBQoSRemarkCfgInfoTable = _HwCBQoSRemarkCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkCfgInfoTable.setStatus("current")
_HwCBQoSRemarkCfgInfoEntry_Object = MibTableRow
hwCBQoSRemarkCfgInfoEntry = _HwCBQoSRemarkCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 5, 1)
)
hwCBQoSRemarkCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSRemarkType"),
)
if mibBuilder.loadTexts:
    hwCBQoSRemarkCfgInfoEntry.setStatus("current")
_HwCBQoSRemarkType_Type = RemarkType
_HwCBQoSRemarkType_Object = MibTableColumn
hwCBQoSRemarkType = _HwCBQoSRemarkType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 5, 1, 1),
    _HwCBQoSRemarkType_Type()
)
hwCBQoSRemarkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSRemarkType.setStatus("current")


class _HwCBQoSRemarkValue_Type(Integer32):
    """Custom type hwCBQoSRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwCBQoSRemarkValue_Type.__name__ = "Integer32"
_HwCBQoSRemarkValue_Object = MibTableColumn
hwCBQoSRemarkValue = _HwCBQoSRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 5, 1, 2),
    _HwCBQoSRemarkValue_Type()
)
hwCBQoSRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkValue.setStatus("current")
_HwCBQoSRemarkRowStatus_Type = RowStatus
_HwCBQoSRemarkRowStatus_Object = MibTableColumn
hwCBQoSRemarkRowStatus = _HwCBQoSRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 5, 1, 3),
    _HwCBQoSRemarkRowStatus_Type()
)
hwCBQoSRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSRemarkRowStatus.setStatus("current")
_HwCBQoSQueueCfgInfoTable_Object = MibTable
hwCBQoSQueueCfgInfoTable = _HwCBQoSQueueCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSQueueCfgInfoTable.setStatus("current")
_HwCBQoSQueueCfgInfoEntry_Object = MibTableRow
hwCBQoSQueueCfgInfoEntry = _HwCBQoSQueueCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1)
)
hwCBQoSQueueCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSQueueCfgInfoEntry.setStatus("current")
_HwCBQoSQueueType_Type = QueueType
_HwCBQoSQueueType_Object = MibTableColumn
hwCBQoSQueueType = _HwCBQoSQueueType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 1),
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
        *(("typeTailDrop", 1),
          ("typeUnavailable", -1),
          ("typeWred", 2))
    )


_HwCBQoSQueueDropType_Type.__name__ = "Integer32"
_HwCBQoSQueueDropType_Object = MibTableColumn
hwCBQoSQueueDropType = _HwCBQoSQueueDropType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 2),
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
        ValueRangeConstraint(1, 512),
    )


_HwCBQoSQueueLength_Type.__name__ = "Integer32"
_HwCBQoSQueueLength_Object = MibTableColumn
hwCBQoSQueueLength = _HwCBQoSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 3),
    _HwCBQoSQueueLength_Type()
)
hwCBQoSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueLength.setStatus("current")
_HwCBQoSQueueBandwidthUnit_Type = QueueBandwidthUnit
_HwCBQoSQueueBandwidthUnit_Object = MibTableColumn
hwCBQoSQueueBandwidthUnit = _HwCBQoSQueueBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 6),
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
          ("unavailable", -1))
    )


_HwCBQoSQueueQueueNumber_Type.__name__ = "Integer32"
_HwCBQoSQueueQueueNumber_Object = MibTableColumn
hwCBQoSQueueQueueNumber = _HwCBQoSQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 7),
    _HwCBQoSQueueQueueNumber_Type()
)
hwCBQoSQueueQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueQueueNumber.setStatus("current")
_HwCBQoSQueueRowStatus_Type = RowStatus
_HwCBQoSQueueRowStatus_Object = MibTableColumn
hwCBQoSQueueRowStatus = _HwCBQoSQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 6, 1, 9),
    _HwCBQoSQueueCbsRatio_Type()
)
hwCBQoSQueueCbsRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSQueueCbsRatio.setStatus("current")
_HwCBQoSWredCfgInfoTable_Object = MibTable
hwCBQoSWredCfgInfoTable = _HwCBQoSWredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSWredCfgInfoTable.setStatus("current")
_HwCBQoSWredCfgInfoEntry_Object = MibTableRow
hwCBQoSWredCfgInfoEntry = _HwCBQoSWredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 7, 1)
)
hwCBQoSWredCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSWredCfgInfoEntry.setStatus("current")


class _HwCBQoSWredType_Type(WredType):
    """Custom type hwCBQoSWredType based on WredType"""


_HwCBQoSWredType_Object = MibTableColumn
hwCBQoSWredType = _HwCBQoSWredType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 7, 1, 2),
    _HwCBQoSWredWeightConst_Type()
)
hwCBQoSWredWeightConst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredWeightConst.setStatus("current")
_HwCBQoSWredClassCfgInfoTable_Object = MibTable
hwCBQoSWredClassCfgInfoTable = _HwCBQoSWredClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSWredClassCfgInfoTable.setStatus("current")
_HwCBQoSWredClassCfgInfoEntry_Object = MibTableRow
hwCBQoSWredClassCfgInfoEntry = _HwCBQoSWredClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 8, 1)
)
hwCBQoSWredClassCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 8, 1, 1),
    _HwCBQoSWredClassValue_Type()
)
hwCBQoSWredClassValue.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 8, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 8, 1, 4),
    _HwCBQoSWredClassDiscardProb_Type()
)
hwCBQoSWredClassDiscardProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCBQoSWredClassDiscardProb.setStatus("current")
_HwCBQoSPolicyRouteCfgInfoTable_Object = MibTable
hwCBQoSPolicyRouteCfgInfoTable = _HwCBQoSPolicyRouteCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyRouteCfgInfoTable.setStatus("current")
_HwCBQoSPolicyRouteCfgInfoEntry_Object = MibTableRow
hwCBQoSPolicyRouteCfgInfoEntry = _HwCBQoSPolicyRouteCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 9, 1)
)
hwCBQoSPolicyRouteCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyRouteCfgInfoEntry.setStatus("current")
_HwCBQoSPolicyRouteNexthop_Type = IpAddress
_HwCBQoSPolicyRouteNexthop_Object = MibTableColumn
hwCBQoSPolicyRouteNexthop = _HwCBQoSPolicyRouteNexthop_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 9, 1, 1),
    _HwCBQoSPolicyRouteNexthop_Type()
)
hwCBQoSPolicyRouteNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyRouteNexthop.setStatus("current")


class _HwCBQoSPolicyRouteBackup_Type(Integer32):
    """Custom type hwCBQoSPolicyRouteBackup based on Integer32"""
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


_HwCBQoSPolicyRouteBackup_Type.__name__ = "Integer32"
_HwCBQoSPolicyRouteBackup_Object = MibTableColumn
hwCBQoSPolicyRouteBackup = _HwCBQoSPolicyRouteBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 9, 1, 2),
    _HwCBQoSPolicyRouteBackup_Type()
)
hwCBQoSPolicyRouteBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyRouteBackup.setStatus("current")
_HwCBQoSPolicyRouteRowStatus_Type = RowStatus
_HwCBQoSPolicyRouteRowStatus_Object = MibTableColumn
hwCBQoSPolicyRouteRowStatus = _HwCBQoSPolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 9, 1, 3),
    _HwCBQoSPolicyRouteRowStatus_Type()
)
hwCBQoSPolicyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyRouteRowStatus.setStatus("current")
_HwCBQoSNatCfgInfoTable_Object = MibTable
hwCBQoSNatCfgInfoTable = _HwCBQoSNatCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hwCBQoSNatCfgInfoTable.setStatus("current")
_HwCBQoSNatCfgInfoEntry_Object = MibTableRow
hwCBQoSNatCfgInfoEntry = _HwCBQoSNatCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 10, 1)
)
hwCBQoSNatCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSNatCfgInfoEntry.setStatus("current")


class _HwCBQoSNatMainNumber_Type(Integer32):
    """Custom type hwCBQoSNatMainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCBQoSNatMainNumber_Type.__name__ = "Integer32"
_HwCBQoSNatMainNumber_Object = MibTableColumn
hwCBQoSNatMainNumber = _HwCBQoSNatMainNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 10, 1, 1),
    _HwCBQoSNatMainNumber_Type()
)
hwCBQoSNatMainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatMainNumber.setStatus("current")


class _HwCBQoSNatBackupNumber_Type(Integer32):
    """Custom type hwCBQoSNatBackupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCBQoSNatBackupNumber_Type.__name__ = "Integer32"
_HwCBQoSNatBackupNumber_Object = MibTableColumn
hwCBQoSNatBackupNumber = _HwCBQoSNatBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 10, 1, 2),
    _HwCBQoSNatBackupNumber_Type()
)
hwCBQoSNatBackupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatBackupNumber.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 10, 1, 3),
    _HwCBQoSNatServiceClass_Type()
)
hwCBQoSNatServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatServiceClass.setStatus("current")
_HwCBQoSNatRowStatus_Type = RowStatus
_HwCBQoSNatRowStatus_Object = MibTableColumn
hwCBQoSNatRowStatus = _HwCBQoSNatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 10, 1, 4),
    _HwCBQoSNatRowStatus_Type()
)
hwCBQoSNatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNatRowStatus.setStatus("current")
_HwCBQoSFirewallCfgInfoTable_Object = MibTable
hwCBQoSFirewallCfgInfoTable = _HwCBQoSFirewallCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hwCBQoSFirewallCfgInfoTable.setStatus("current")
_HwCBQoSFirewallCfgInfoEntry_Object = MibTableRow
hwCBQoSFirewallCfgInfoEntry = _HwCBQoSFirewallCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 11, 1)
)
hwCBQoSFirewallCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 11, 1, 1),
    _HwCBQoSFirewallAction_Type()
)
hwCBQoSFirewallAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFirewallAction.setStatus("current")
_HwCBQoSFirewallRowStatus_Type = RowStatus
_HwCBQoSFirewallRowStatus_Object = MibTableColumn
hwCBQoSFirewallRowStatus = _HwCBQoSFirewallRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 11, 1, 2),
    _HwCBQoSFirewallRowStatus_Type()
)
hwCBQoSFirewallRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFirewallRowStatus.setStatus("current")
_HwCBQoSSamplingCfgInfoTable_Object = MibTable
hwCBQoSSamplingCfgInfoTable = _HwCBQoSSamplingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hwCBQoSSamplingCfgInfoTable.setStatus("current")
_HwCBQoSSamplingCfgInfoEntry_Object = MibTableRow
hwCBQoSSamplingCfgInfoEntry = _HwCBQoSSamplingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 12, 1)
)
hwCBQoSSamplingCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSSamplingCfgInfoEntry.setStatus("current")


class _HwCBQoSSamplingNum_Type(Integer32):
    """Custom type hwCBQoSSamplingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwCBQoSSamplingNum_Type.__name__ = "Integer32"
_HwCBQoSSamplingNum_Object = MibTableColumn
hwCBQoSSamplingNum = _HwCBQoSSamplingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 12, 1, 1),
    _HwCBQoSSamplingNum_Type()
)
hwCBQoSSamplingNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSamplingNum.setStatus("current")
_HwCBQoSSamplingRowStatus_Type = RowStatus
_HwCBQoSSamplingRowStatus_Object = MibTableColumn
hwCBQoSSamplingRowStatus = _HwCBQoSSamplingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 12, 1, 2),
    _HwCBQoSSamplingRowStatus_Type()
)
hwCBQoSSamplingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSSamplingRowStatus.setStatus("current")
_HwCBQoSLrCfgInfoTable_Object = MibTable
hwCBQoSLrCfgInfoTable = _HwCBQoSLrCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hwCBQoSLrCfgInfoTable.setStatus("current")
_HwCBQoSLrCfgInfoEntry_Object = MibTableRow
hwCBQoSLrCfgInfoEntry = _HwCBQoSLrCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13, 1)
)
hwCBQoSLrCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSLrCfgInfoEntry.setStatus("current")
_HwCBQoSLrUnit_Type = LrCirUnit
_HwCBQoSLrUnit_Object = MibTableColumn
hwCBQoSLrUnit = _HwCBQoSLrUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13, 1, 1),
    _HwCBQoSLrUnit_Type()
)
hwCBQoSLrUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrUnit.setStatus("current")


class _HwCBQoSLrCir_Type(Integer32):
    """Custom type hwCBQoSLrCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_HwCBQoSLrCir_Type.__name__ = "Integer32"
_HwCBQoSLrCir_Object = MibTableColumn
hwCBQoSLrCir = _HwCBQoSLrCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13, 1, 2),
    _HwCBQoSLrCir_Type()
)
hwCBQoSLrCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrCir.setStatus("current")


class _HwCBQoSLrCbs_Type(Integer32):
    """Custom type hwCBQoSLrCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000000000),
    )


_HwCBQoSLrCbs_Type.__name__ = "Integer32"
_HwCBQoSLrCbs_Object = MibTableColumn
hwCBQoSLrCbs = _HwCBQoSLrCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13, 1, 3),
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
        ValueRangeConstraint(0, 1000000000),
    )


_HwCBQoSLrEbs_Type.__name__ = "Integer32"
_HwCBQoSLrEbs_Object = MibTableColumn
hwCBQoSLrEbs = _HwCBQoSLrEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13, 1, 4),
    _HwCBQoSLrEbs_Type()
)
hwCBQoSLrEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrEbs.setStatus("current")
_HwCBQoSLrRowStatus_Type = RowStatus
_HwCBQoSLrRowStatus_Object = MibTableColumn
hwCBQoSLrRowStatus = _HwCBQoSLrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 13, 1, 5),
    _HwCBQoSLrRowStatus_Type()
)
hwCBQoSLrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSLrRowStatus.setStatus("current")
_HwCBQoSNestPolicyCfgInfoTable_Object = MibTable
hwCBQoSNestPolicyCfgInfoTable = _HwCBQoSNestPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyCfgInfoTable.setStatus("current")
_HwCBQoSNestPolicyCfgInfoEntry_Object = MibTableRow
hwCBQoSNestPolicyCfgInfoEntry = _HwCBQoSNestPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 14, 1)
)
hwCBQoSNestPolicyCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSBehaviorIndex"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 14, 1, 1),
    _HwCBQoSNestPolicyName_Type()
)
hwCBQoSNestPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyName.setStatus("current")
_HwCBQoSNestPolicyRowStatus_Type = RowStatus
_HwCBQoSNestPolicyRowStatus_Object = MibTableColumn
hwCBQoSNestPolicyRowStatus = _HwCBQoSNestPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 2, 14, 1, 2),
    _HwCBQoSNestPolicyRowStatus_Type()
)
hwCBQoSNestPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSNestPolicyRowStatus.setStatus("current")
_HwCBQoSPolicyObjects_ObjectIdentity = ObjectIdentity
hwCBQoSPolicyObjects = _HwCBQoSPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3)
)
_HwCBQoSPolicyIndexNext_Type = Integer32
_HwCBQoSPolicyIndexNext_Object = MibScalar
hwCBQoSPolicyIndexNext = _HwCBQoSPolicyIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 1),
    _HwCBQoSPolicyIndexNext_Type()
)
hwCBQoSPolicyIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyIndexNext.setStatus("current")
_HwCBQoSPolicyCfgInfoTable_Object = MibTable
hwCBQoSPolicyCfgInfoTable = _HwCBQoSPolicyCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyCfgInfoTable.setStatus("current")
_HwCBQoSPolicyCfgInfoEntry_Object = MibTableRow
hwCBQoSPolicyCfgInfoEntry = _HwCBQoSPolicyCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2, 1)
)
hwCBQoSPolicyCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyCfgInfoEntry.setStatus("current")
_HwCBQoSPolicyIndex_Type = Integer32
_HwCBQoSPolicyIndex_Object = MibTableColumn
hwCBQoSPolicyIndex = _HwCBQoSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2, 1, 1),
    _HwCBQoSPolicyIndex_Type()
)
hwCBQoSPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSPolicyIndex.setStatus("current")


class _HwCBQoSPolicyName_Type(OctetString):
    """Custom type hwCBQoSPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSPolicyName_Type.__name__ = "OctetString"
_HwCBQoSPolicyName_Object = MibTableColumn
hwCBQoSPolicyName = _HwCBQoSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2, 1, 2),
    _HwCBQoSPolicyName_Type()
)
hwCBQoSPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyName.setStatus("current")
_HwCBQoSPolicyClassCount_Type = Integer32
_HwCBQoSPolicyClassCount_Object = MibTableColumn
hwCBQoSPolicyClassCount = _HwCBQoSPolicyClassCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2, 1, 4),
    _HwCBQoSPolicyConfigMode_Type()
)
hwCBQoSPolicyConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyConfigMode.setStatus("current")
_HwCBQoSPolicyRowStatus_Type = RowStatus
_HwCBQoSPolicyRowStatus_Object = MibTableColumn
hwCBQoSPolicyRowStatus = _HwCBQoSPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 2, 1, 5),
    _HwCBQoSPolicyRowStatus_Type()
)
hwCBQoSPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyRowStatus.setStatus("current")
_HwCBQoSPolicyClassCfgInfoTable_Object = MibTable
hwCBQoSPolicyClassCfgInfoTable = _HwCBQoSPolicyClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassCfgInfoTable.setStatus("current")
_HwCBQoSPolicyClassCfgInfoEntry_Object = MibTableRow
hwCBQoSPolicyClassCfgInfoEntry = _HwCBQoSPolicyClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1)
)
hwCBQoSPolicyClassCfgInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassCfgInfoEntry.setStatus("current")
_HwCBQoSPolicyClassIndex_Type = Integer32
_HwCBQoSPolicyClassIndex_Object = MibTableColumn
hwCBQoSPolicyClassIndex = _HwCBQoSPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 1),
    _HwCBQoSPolicyClassIndex_Type()
)
hwCBQoSPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassIndex.setStatus("current")
_HwCBQoSPolicyClassClassifierIndex_Type = Integer32
_HwCBQoSPolicyClassClassifierIndex_Object = MibTableColumn
hwCBQoSPolicyClassClassifierIndex = _HwCBQoSPolicyClassClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 2),
    _HwCBQoSPolicyClassClassifierIndex_Type()
)
hwCBQoSPolicyClassClassifierIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassClassifierIndex.setStatus("current")


class _HwCBQoSPolicyClassClassifierName_Type(OctetString):
    """Custom type hwCBQoSPolicyClassClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSPolicyClassClassifierName_Type.__name__ = "OctetString"
_HwCBQoSPolicyClassClassifierName_Object = MibTableColumn
hwCBQoSPolicyClassClassifierName = _HwCBQoSPolicyClassClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 3),
    _HwCBQoSPolicyClassClassifierName_Type()
)
hwCBQoSPolicyClassClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassClassifierName.setStatus("current")
_HwCBQoSPolicyClassBehaviorIndex_Type = Integer32
_HwCBQoSPolicyClassBehaviorIndex_Object = MibTableColumn
hwCBQoSPolicyClassBehaviorIndex = _HwCBQoSPolicyClassBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 4),
    _HwCBQoSPolicyClassBehaviorIndex_Type()
)
hwCBQoSPolicyClassBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassBehaviorIndex.setStatus("current")


class _HwCBQoSPolicyClassBehaviorName_Type(OctetString):
    """Custom type hwCBQoSPolicyClassBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSPolicyClassBehaviorName_Type.__name__ = "OctetString"
_HwCBQoSPolicyClassBehaviorName_Object = MibTableColumn
hwCBQoSPolicyClassBehaviorName = _HwCBQoSPolicyClassBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 5),
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
        ValueRangeConstraint(0, 16383),
    )


_HwCBQoSPolicyClassPrecedence_Type.__name__ = "Integer32"
_HwCBQoSPolicyClassPrecedence_Object = MibTableColumn
hwCBQoSPolicyClassPrecedence = _HwCBQoSPolicyClassPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 6),
    _HwCBQoSPolicyClassPrecedence_Type()
)
hwCBQoSPolicyClassPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassPrecedence.setStatus("current")
_HwCBQoSPolicyClassRowStatus_Type = RowStatus
_HwCBQoSPolicyClassRowStatus_Object = MibTableColumn
hwCBQoSPolicyClassRowStatus = _HwCBQoSPolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 3, 3, 1, 7),
    _HwCBQoSPolicyClassRowStatus_Type()
)
hwCBQoSPolicyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSPolicyClassRowStatus.setStatus("current")
_HwCBQoSApplyPolicyObjects_ObjectIdentity = ObjectIdentity
hwCBQoSApplyPolicyObjects = _HwCBQoSApplyPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4)
)
_HwCBQoSIfApplyPolicyTable_Object = MibTable
hwCBQoSIfApplyPolicyTable = _HwCBQoSIfApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyTable.setStatus("current")
_HwCBQoSIfApplyPolicyEntry_Object = MibTableRow
hwCBQoSIfApplyPolicyEntry = _HwCBQoSIfApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1, 1)
)
hwCBQoSIfApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyEntry.setStatus("current")
_HwCBQoSIfApplyPolicyIfIndex_Type = Integer32
_HwCBQoSIfApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSIfApplyPolicyIfIndex = _HwCBQoSIfApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1, 1, 1),
    _HwCBQoSIfApplyPolicyIfIndex_Type()
)
hwCBQoSIfApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyIfIndex.setStatus("current")
_HwCBQoSIfApplyPolicyDirection_Type = DirectionType
_HwCBQoSIfApplyPolicyDirection_Object = MibTableColumn
hwCBQoSIfApplyPolicyDirection = _HwCBQoSIfApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1, 1, 2),
    _HwCBQoSIfApplyPolicyDirection_Type()
)
hwCBQoSIfApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyDirection.setStatus("current")


class _HwCBQoSIfApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSIfApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSIfApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSIfApplyPolicyName_Object = MibTableColumn
hwCBQoSIfApplyPolicyName = _HwCBQoSIfApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1, 1, 3),
    _HwCBQoSIfApplyPolicyName_Type()
)
hwCBQoSIfApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyName.setStatus("current")


class _HwCBQoSIfApplyPolicyEnableDynamic_Type(Integer32):
    """Custom type hwCBQoSIfApplyPolicyEnableDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unavailable", -1))
    )


_HwCBQoSIfApplyPolicyEnableDynamic_Type.__name__ = "Integer32"
_HwCBQoSIfApplyPolicyEnableDynamic_Object = MibTableColumn
hwCBQoSIfApplyPolicyEnableDynamic = _HwCBQoSIfApplyPolicyEnableDynamic_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1, 1, 4),
    _HwCBQoSIfApplyPolicyEnableDynamic_Type()
)
hwCBQoSIfApplyPolicyEnableDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyEnableDynamic.setStatus("current")
_HwCBQoSIfApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSIfApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSIfApplyPolicyRowStatus = _HwCBQoSIfApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 1, 1, 5),
    _HwCBQoSIfApplyPolicyRowStatus_Type()
)
hwCBQoSIfApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfApplyPolicyRowStatus.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyTable_Object = MibTable
hwCBQoSAtmPvcApplyPolicyTable = _HwCBQoSAtmPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyTable.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyEntry_Object = MibTableRow
hwCBQoSAtmPvcApplyPolicyEntry = _HwCBQoSAtmPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1)
)
hwCBQoSAtmPvcApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyEntry.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyIfIndex_Type = Integer32
_HwCBQoSAtmPvcApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyIfIndex = _HwCBQoSAtmPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1, 1),
    _HwCBQoSAtmPvcApplyPolicyIfIndex_Type()
)
hwCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyIfIndex.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyVPI_Type = Integer32
_HwCBQoSAtmPvcApplyPolicyVPI_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyVPI = _HwCBQoSAtmPvcApplyPolicyVPI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1, 2),
    _HwCBQoSAtmPvcApplyPolicyVPI_Type()
)
hwCBQoSAtmPvcApplyPolicyVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyVPI.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyVCI_Type = Integer32
_HwCBQoSAtmPvcApplyPolicyVCI_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyVCI = _HwCBQoSAtmPvcApplyPolicyVCI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1, 3),
    _HwCBQoSAtmPvcApplyPolicyVCI_Type()
)
hwCBQoSAtmPvcApplyPolicyVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyVCI.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyDirection_Type = DirectionType
_HwCBQoSAtmPvcApplyPolicyDirection_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyDirection = _HwCBQoSAtmPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1, 4),
    _HwCBQoSAtmPvcApplyPolicyDirection_Type()
)
hwCBQoSAtmPvcApplyPolicyDirection.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1, 5),
    _HwCBQoSAtmPvcApplyPolicyName_Type()
)
hwCBQoSAtmPvcApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyName.setStatus("current")
_HwCBQoSAtmPvcApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSAtmPvcApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSAtmPvcApplyPolicyRowStatus = _HwCBQoSAtmPvcApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 2, 1, 6),
    _HwCBQoSAtmPvcApplyPolicyRowStatus_Type()
)
hwCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcApplyPolicyRowStatus.setStatus("current")
_HwCBQoSIfVlanApplyPolicyTable_Object = MibTable
hwCBQoSIfVlanApplyPolicyTable = _HwCBQoSIfVlanApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyTable.setStatus("current")
_HwCBQoSIfVlanApplyPolicyEntry_Object = MibTableRow
hwCBQoSIfVlanApplyPolicyEntry = _HwCBQoSIfVlanApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3, 1)
)
hwCBQoSIfVlanApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyEntry.setStatus("current")
_HwCBQoSIfVlanApplyPolicyIfIndex_Type = Integer32
_HwCBQoSIfVlanApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyIfIndex = _HwCBQoSIfVlanApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3, 1, 1),
    _HwCBQoSIfVlanApplyPolicyIfIndex_Type()
)
hwCBQoSIfVlanApplyPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyIfIndex.setStatus("current")
_HwCBQoSIfVlanApplyPolicyVlanid_Type = Integer32
_HwCBQoSIfVlanApplyPolicyVlanid_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyVlanid = _HwCBQoSIfVlanApplyPolicyVlanid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3, 1, 2),
    _HwCBQoSIfVlanApplyPolicyVlanid_Type()
)
hwCBQoSIfVlanApplyPolicyVlanid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyVlanid.setStatus("current")
_HwCBQoSIfVlanApplyPolicyDirection_Type = DirectionType
_HwCBQoSIfVlanApplyPolicyDirection_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyDirection = _HwCBQoSIfVlanApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3, 1, 3),
    _HwCBQoSIfVlanApplyPolicyDirection_Type()
)
hwCBQoSIfVlanApplyPolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyDirection.setStatus("current")


class _HwCBQoSIfVlanApplyPolicyName_Type(OctetString):
    """Custom type hwCBQoSIfVlanApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCBQoSIfVlanApplyPolicyName_Type.__name__ = "OctetString"
_HwCBQoSIfVlanApplyPolicyName_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyName = _HwCBQoSIfVlanApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3, 1, 4),
    _HwCBQoSIfVlanApplyPolicyName_Type()
)
hwCBQoSIfVlanApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyName.setStatus("current")
_HwCBQoSIfVlanApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSIfVlanApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSIfVlanApplyPolicyRowStatus = _HwCBQoSIfVlanApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 3, 1, 5),
    _HwCBQoSIfVlanApplyPolicyRowStatus_Type()
)
hwCBQoSIfVlanApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanApplyPolicyRowStatus.setStatus("current")
_HwCBQoSFrClassApplyPolicyTable_Object = MibTable
hwCBQoSFrClassApplyPolicyTable = _HwCBQoSFrClassApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyTable.setStatus("current")
_HwCBQoSFrClassApplyPolicyEntry_Object = MibTableRow
hwCBQoSFrClassApplyPolicyEntry = _HwCBQoSFrClassApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 4, 1)
)
hwCBQoSFrClassApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyFrClassName"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrClassApplyPolicyDirection"),
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 4, 1, 1),
    _HwCBQoSFrClassApplyPolicyFrClassName_Type()
)
hwCBQoSFrClassApplyPolicyFrClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyFrClassName.setStatus("current")
_HwCBQoSFrClassApplyPolicyDirection_Type = DirectionType
_HwCBQoSFrClassApplyPolicyDirection_Object = MibTableColumn
hwCBQoSFrClassApplyPolicyDirection = _HwCBQoSFrClassApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 4, 1, 2),
    _HwCBQoSFrClassApplyPolicyDirection_Type()
)
hwCBQoSFrClassApplyPolicyDirection.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 4, 1, 3),
    _HwCBQoSFrClassApplyPolicyName_Type()
)
hwCBQoSFrClassApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyName.setStatus("current")
_HwCBQoSFrClassApplyPolicyRowStatus_Type = RowStatus
_HwCBQoSFrClassApplyPolicyRowStatus_Object = MibTableColumn
hwCBQoSFrClassApplyPolicyRowStatus = _HwCBQoSFrClassApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 4, 1, 4),
    _HwCBQoSFrClassApplyPolicyRowStatus_Type()
)
hwCBQoSFrClassApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCBQoSFrClassApplyPolicyRowStatus.setStatus("current")
_HwCBQoSFrPvcApplyPolicyTable_Object = MibTable
hwCBQoSFrPvcApplyPolicyTable = _HwCBQoSFrPvcApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyTable.setStatus("current")
_HwCBQoSFrPvcApplyPolicyEntry_Object = MibTableRow
hwCBQoSFrPvcApplyPolicyEntry = _HwCBQoSFrPvcApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 5, 1)
)
hwCBQoSFrPvcApplyPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyEntry.setStatus("current")
_HwCBQoSFrPvcApplyPolicyIfIndex_Type = Integer32
_HwCBQoSFrPvcApplyPolicyIfIndex_Object = MibTableColumn
hwCBQoSFrPvcApplyPolicyIfIndex = _HwCBQoSFrPvcApplyPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 5, 1, 1),
    _HwCBQoSFrPvcApplyPolicyIfIndex_Type()
)
hwCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 5, 1, 2),
    _HwCBQoSFrPvcApplyPolicyDlciNum_Type()
)
hwCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyDlciNum.setStatus("current")
_HwCBQoSFrPvcApplyPolicyDirection_Type = DirectionType
_HwCBQoSFrPvcApplyPolicyDirection_Object = MibTableColumn
hwCBQoSFrPvcApplyPolicyDirection = _HwCBQoSFrPvcApplyPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 5, 1, 3),
    _HwCBQoSFrPvcApplyPolicyDirection_Type()
)
hwCBQoSFrPvcApplyPolicyDirection.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 4, 5, 1, 4),
    _HwCBQoSFrPvcApplyPolicyName_Type()
)
hwCBQoSFrPvcApplyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcApplyPolicyName.setStatus("current")
_HwCBQoSApplyPolicyStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSApplyPolicyStaticsObjects = _HwCBQoSApplyPolicyStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5)
)
_HwCBQoSIfStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSIfStaticsObjects = _HwCBQoSIfStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1)
)
_HwCBQoSIfCbqRunInfoTable_Object = MibTable
hwCBQoSIfCbqRunInfoTable = _HwCBQoSIfCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSIfCbqRunInfoTable.setStatus("current")
_HwCBQoSIfCbqRunInfoEntry_Object = MibTableRow
hwCBQoSIfCbqRunInfoEntry = _HwCBQoSIfCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1)
)
hwCBQoSIfCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfCbqRunInfoEntry.setStatus("current")
_HwCBQoSIfCbqQueueSize_Type = Integer32
_HwCBQoSIfCbqQueueSize_Object = MibTableColumn
hwCBQoSIfCbqQueueSize = _HwCBQoSIfCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 1),
    _HwCBQoSIfCbqQueueSize_Type()
)
hwCBQoSIfCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqQueueSize.setStatus("current")
_HwCBQoSIfCbqDiscard_Type = Counter32
_HwCBQoSIfCbqDiscard_Object = MibTableColumn
hwCBQoSIfCbqDiscard = _HwCBQoSIfCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 2),
    _HwCBQoSIfCbqDiscard_Type()
)
hwCBQoSIfCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqDiscard.setStatus("current")
_HwCBQoSIfCbqEfQueueSize_Type = Integer32
_HwCBQoSIfCbqEfQueueSize_Object = MibTableColumn
hwCBQoSIfCbqEfQueueSize = _HwCBQoSIfCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 3),
    _HwCBQoSIfCbqEfQueueSize_Type()
)
hwCBQoSIfCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqEfQueueSize.setStatus("current")
_HwCBQoSIfCbqAfQueueSize_Type = Integer32
_HwCBQoSIfCbqAfQueueSize_Object = MibTableColumn
hwCBQoSIfCbqAfQueueSize = _HwCBQoSIfCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 4),
    _HwCBQoSIfCbqAfQueueSize_Type()
)
hwCBQoSIfCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqAfQueueSize.setStatus("current")
_HwCBQoSIfCbqBeQueueSize_Type = Integer32
_HwCBQoSIfCbqBeQueueSize_Object = MibTableColumn
hwCBQoSIfCbqBeQueueSize = _HwCBQoSIfCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 5),
    _HwCBQoSIfCbqBeQueueSize_Type()
)
hwCBQoSIfCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeQueueSize.setStatus("current")
_HwCBQoSIfCbqBeActiveQueueNum_Type = Integer32
_HwCBQoSIfCbqBeActiveQueueNum_Object = MibTableColumn
hwCBQoSIfCbqBeActiveQueueNum = _HwCBQoSIfCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 6),
    _HwCBQoSIfCbqBeActiveQueueNum_Type()
)
hwCBQoSIfCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeActiveQueueNum.setStatus("current")
_HwCBQoSIfCbqBeMaxActiveQueueNum_Type = Integer32
_HwCBQoSIfCbqBeMaxActiveQueueNum_Object = MibTableColumn
hwCBQoSIfCbqBeMaxActiveQueueNum = _HwCBQoSIfCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 7),
    _HwCBQoSIfCbqBeMaxActiveQueueNum_Type()
)
hwCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeMaxActiveQueueNum.setStatus("current")
_HwCBQoSIfCbqBeTotalQueueNum_Type = Integer32
_HwCBQoSIfCbqBeTotalQueueNum_Object = MibTableColumn
hwCBQoSIfCbqBeTotalQueueNum = _HwCBQoSIfCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 8),
    _HwCBQoSIfCbqBeTotalQueueNum_Type()
)
hwCBQoSIfCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqBeTotalQueueNum.setStatus("current")
_HwCBQoSIfCbqAfAllocatedQueueNum_Type = Integer32
_HwCBQoSIfCbqAfAllocatedQueueNum_Object = MibTableColumn
hwCBQoSIfCbqAfAllocatedQueueNum = _HwCBQoSIfCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 1, 1, 9),
    _HwCBQoSIfCbqAfAllocatedQueueNum_Type()
)
hwCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCbqAfAllocatedQueueNum.setStatus("current")
_HwCBQoSIfClassMatchRunInfoTable_Object = MibTable
hwCBQoSIfClassMatchRunInfoTable = _HwCBQoSIfClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchRunInfoTable.setStatus("current")
_HwCBQoSIfClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSIfClassMatchRunInfoEntry = _HwCBQoSIfClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 2, 1)
)
hwCBQoSIfClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSIfClassMatchedPackets_Type = Counter32
_HwCBQoSIfClassMatchedPackets_Object = MibTableColumn
hwCBQoSIfClassMatchedPackets = _HwCBQoSIfClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 2, 1, 1),
    _HwCBQoSIfClassMatchedPackets_Type()
)
hwCBQoSIfClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchedPackets.setStatus("current")
_HwCBQoSIfClassMatchedBytes_Type = Counter32
_HwCBQoSIfClassMatchedBytes_Object = MibTableColumn
hwCBQoSIfClassMatchedBytes = _HwCBQoSIfClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 2, 1, 2),
    _HwCBQoSIfClassMatchedBytes_Type()
)
hwCBQoSIfClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfClassMatchedBytes.setStatus("current")
_HwCBQoSIfClassAverageRate_Type = Counter64
_HwCBQoSIfClassAverageRate_Object = MibTableColumn
hwCBQoSIfClassAverageRate = _HwCBQoSIfClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 2, 1, 3),
    _HwCBQoSIfClassAverageRate_Type()
)
hwCBQoSIfClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfClassAverageRate.setStatus("current")
_HwCBQoSIfCarRunInfoTable_Object = MibTable
hwCBQoSIfCarRunInfoTable = _HwCBQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSIfCarRunInfoTable.setStatus("current")
_HwCBQoSIfCarRunInfoEntry_Object = MibTableRow
hwCBQoSIfCarRunInfoEntry = _HwCBQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 3, 1)
)
hwCBQoSIfCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfCarRunInfoEntry.setStatus("current")
_HwCBQoSIfCarGreenPackets_Type = Counter32
_HwCBQoSIfCarGreenPackets_Object = MibTableColumn
hwCBQoSIfCarGreenPackets = _HwCBQoSIfCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 3, 1, 1),
    _HwCBQoSIfCarGreenPackets_Type()
)
hwCBQoSIfCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenPackets.setStatus("current")
_HwCBQoSIfCarGreenBytes_Type = Counter32
_HwCBQoSIfCarGreenBytes_Object = MibTableColumn
hwCBQoSIfCarGreenBytes = _HwCBQoSIfCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 3, 1, 2),
    _HwCBQoSIfCarGreenBytes_Type()
)
hwCBQoSIfCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarGreenBytes.setStatus("current")
_HwCBQoSIfCarRedPackets_Type = Counter32
_HwCBQoSIfCarRedPackets_Object = MibTableColumn
hwCBQoSIfCarRedPackets = _HwCBQoSIfCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 3, 1, 3),
    _HwCBQoSIfCarRedPackets_Type()
)
hwCBQoSIfCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedPackets.setStatus("current")
_HwCBQoSIfCarRedBytes_Type = Counter32
_HwCBQoSIfCarRedBytes_Object = MibTableColumn
hwCBQoSIfCarRedBytes = _HwCBQoSIfCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 3, 1, 4),
    _HwCBQoSIfCarRedBytes_Type()
)
hwCBQoSIfCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfCarRedBytes.setStatus("current")
_HwCBQoSIfGtsRunInfoTable_Object = MibTable
hwCBQoSIfGtsRunInfoTable = _HwCBQoSIfGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSIfGtsRunInfoTable.setStatus("current")
_HwCBQoSIfGtsRunInfoEntry_Object = MibTableRow
hwCBQoSIfGtsRunInfoEntry = _HwCBQoSIfGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1)
)
hwCBQoSIfGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfGtsRunInfoEntry.setStatus("current")
_HwCBQoSIfGtsPassedPackets_Type = Counter32
_HwCBQoSIfGtsPassedPackets_Object = MibTableColumn
hwCBQoSIfGtsPassedPackets = _HwCBQoSIfGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 1),
    _HwCBQoSIfGtsPassedPackets_Type()
)
hwCBQoSIfGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsPassedPackets.setStatus("current")
_HwCBQoSIfGtsPassedBytes_Type = Counter32
_HwCBQoSIfGtsPassedBytes_Object = MibTableColumn
hwCBQoSIfGtsPassedBytes = _HwCBQoSIfGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 2),
    _HwCBQoSIfGtsPassedBytes_Type()
)
hwCBQoSIfGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsPassedBytes.setStatus("current")
_HwCBQoSIfGtsDiscardedPackets_Type = Counter32
_HwCBQoSIfGtsDiscardedPackets_Object = MibTableColumn
hwCBQoSIfGtsDiscardedPackets = _HwCBQoSIfGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 3),
    _HwCBQoSIfGtsDiscardedPackets_Type()
)
hwCBQoSIfGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDiscardedPackets.setStatus("current")
_HwCBQoSIfGtsDiscardedBytes_Type = Counter32
_HwCBQoSIfGtsDiscardedBytes_Object = MibTableColumn
hwCBQoSIfGtsDiscardedBytes = _HwCBQoSIfGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 4),
    _HwCBQoSIfGtsDiscardedBytes_Type()
)
hwCBQoSIfGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDiscardedBytes.setStatus("current")
_HwCBQoSIfGtsDelayedPackets_Type = Counter32
_HwCBQoSIfGtsDelayedPackets_Object = MibTableColumn
hwCBQoSIfGtsDelayedPackets = _HwCBQoSIfGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 5),
    _HwCBQoSIfGtsDelayedPackets_Type()
)
hwCBQoSIfGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDelayedPackets.setStatus("current")
_HwCBQoSIfGtsDelayedBytes_Type = Counter32
_HwCBQoSIfGtsDelayedBytes_Object = MibTableColumn
hwCBQoSIfGtsDelayedBytes = _HwCBQoSIfGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 6),
    _HwCBQoSIfGtsDelayedBytes_Type()
)
hwCBQoSIfGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsDelayedBytes.setStatus("current")
_HwCBQoSIfGtsQueueSize_Type = Integer32
_HwCBQoSIfGtsQueueSize_Object = MibTableColumn
hwCBQoSIfGtsQueueSize = _HwCBQoSIfGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 4, 1, 7),
    _HwCBQoSIfGtsQueueSize_Type()
)
hwCBQoSIfGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfGtsQueueSize.setStatus("current")
_HwCBQoSIfRemarkRunInfoTable_Object = MibTable
hwCBQoSIfRemarkRunInfoTable = _HwCBQoSIfRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkRunInfoTable.setStatus("current")
_HwCBQoSIfRemarkRunInfoEntry_Object = MibTableRow
hwCBQoSIfRemarkRunInfoEntry = _HwCBQoSIfRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 5, 1)
)
hwCBQoSIfRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkRunInfoEntry.setStatus("current")
_HwCBQoSIfRemarkedPackets_Type = Counter32
_HwCBQoSIfRemarkedPackets_Object = MibTableColumn
hwCBQoSIfRemarkedPackets = _HwCBQoSIfRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 5, 1, 1),
    _HwCBQoSIfRemarkedPackets_Type()
)
hwCBQoSIfRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfRemarkedPackets.setStatus("current")
_HwCBQoSIfQueueRunInfoTable_Object = MibTable
hwCBQoSIfQueueRunInfoTable = _HwCBQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSIfQueueRunInfoTable.setStatus("current")
_HwCBQoSIfQueueRunInfoEntry_Object = MibTableRow
hwCBQoSIfQueueRunInfoEntry = _HwCBQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1)
)
hwCBQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfQueueRunInfoEntry.setStatus("current")
_HwCBQoSIfQueueMatchedPackets_Type = Counter32
_HwCBQoSIfQueueMatchedPackets_Object = MibTableColumn
hwCBQoSIfQueueMatchedPackets = _HwCBQoSIfQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1, 1),
    _HwCBQoSIfQueueMatchedPackets_Type()
)
hwCBQoSIfQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueMatchedPackets.setStatus("current")
_HwCBQoSIfQueueMatchedBytes_Type = Counter32
_HwCBQoSIfQueueMatchedBytes_Object = MibTableColumn
hwCBQoSIfQueueMatchedBytes = _HwCBQoSIfQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1, 2),
    _HwCBQoSIfQueueMatchedBytes_Type()
)
hwCBQoSIfQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueMatchedBytes.setStatus("current")
_HwCBQoSIfQueueEnqueuedPackets_Type = Counter32
_HwCBQoSIfQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSIfQueueEnqueuedPackets = _HwCBQoSIfQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1, 3),
    _HwCBQoSIfQueueEnqueuedPackets_Type()
)
hwCBQoSIfQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueEnqueuedPackets.setStatus("current")
_HwCBQoSIfQueueEnqueuedBytes_Type = Counter32
_HwCBQoSIfQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSIfQueueEnqueuedBytes = _HwCBQoSIfQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1, 4),
    _HwCBQoSIfQueueEnqueuedBytes_Type()
)
hwCBQoSIfQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueEnqueuedBytes.setStatus("current")
_HwCBQoSIfQueueDiscardedPackets_Type = Counter32
_HwCBQoSIfQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSIfQueueDiscardedPackets = _HwCBQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1, 5),
    _HwCBQoSIfQueueDiscardedPackets_Type()
)
hwCBQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueDiscardedPackets.setStatus("current")
_HwCBQoSIfQueueDiscardedBytes_Type = Counter32
_HwCBQoSIfQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSIfQueueDiscardedBytes = _HwCBQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 6, 1, 6),
    _HwCBQoSIfQueueDiscardedBytes_Type()
)
hwCBQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfQueueDiscardedBytes.setStatus("current")
_HwCBQoSIfWredRunInfoTable_Object = MibTable
hwCBQoSIfWredRunInfoTable = _HwCBQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSIfWredRunInfoTable.setStatus("current")
_HwCBQoSIfWredRunInfoEntry_Object = MibTableRow
hwCBQoSIfWredRunInfoEntry = _HwCBQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 7, 1)
)
hwCBQoSIfWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfWredRunInfoEntry.setStatus("current")
_HwCBQoSIfWredRandomDiscardedPackets_Type = Counter32
_HwCBQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
hwCBQoSIfWredRandomDiscardedPackets = _HwCBQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 7, 1, 1),
    _HwCBQoSIfWredRandomDiscardedPackets_Type()
)
hwCBQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfWredRandomDiscardedPackets.setStatus("current")
_HwCBQoSIfWredTailDiscardedPackets_Type = Counter32
_HwCBQoSIfWredTailDiscardedPackets_Object = MibTableColumn
hwCBQoSIfWredTailDiscardedPackets = _HwCBQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 7, 1, 2),
    _HwCBQoSIfWredTailDiscardedPackets_Type()
)
hwCBQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfWredTailDiscardedPackets.setStatus("current")
_HwCBQoSIfLrRunInfoTable_Object = MibTable
hwCBQoSIfLrRunInfoTable = _HwCBQoSIfLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSIfLrRunInfoTable.setStatus("current")
_HwCBQoSIfLrRunInfoEntry_Object = MibTableRow
hwCBQoSIfLrRunInfoEntry = _HwCBQoSIfLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1)
)
hwCBQoSIfLrRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfLrRunInfoEntry.setStatus("current")
_HwCBQoSIfLrPassedPackets_Type = Counter32
_HwCBQoSIfLrPassedPackets_Object = MibTableColumn
hwCBQoSIfLrPassedPackets = _HwCBQoSIfLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 1),
    _HwCBQoSIfLrPassedPackets_Type()
)
hwCBQoSIfLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrPassedPackets.setStatus("current")
_HwCBQoSIfLrPassedBytes_Type = Counter32
_HwCBQoSIfLrPassedBytes_Object = MibTableColumn
hwCBQoSIfLrPassedBytes = _HwCBQoSIfLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 2),
    _HwCBQoSIfLrPassedBytes_Type()
)
hwCBQoSIfLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrPassedBytes.setStatus("current")
_HwCBQoSIfLrDiscardedPackets_Type = Counter32
_HwCBQoSIfLrDiscardedPackets_Object = MibTableColumn
hwCBQoSIfLrDiscardedPackets = _HwCBQoSIfLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 3),
    _HwCBQoSIfLrDiscardedPackets_Type()
)
hwCBQoSIfLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDiscardedPackets.setStatus("current")
_HwCBQoSIfLrDiscardedBytes_Type = Counter32
_HwCBQoSIfLrDiscardedBytes_Object = MibTableColumn
hwCBQoSIfLrDiscardedBytes = _HwCBQoSIfLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 4),
    _HwCBQoSIfLrDiscardedBytes_Type()
)
hwCBQoSIfLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDiscardedBytes.setStatus("current")
_HwCBQoSIfLrDelayedPackets_Type = Counter32
_HwCBQoSIfLrDelayedPackets_Object = MibTableColumn
hwCBQoSIfLrDelayedPackets = _HwCBQoSIfLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 5),
    _HwCBQoSIfLrDelayedPackets_Type()
)
hwCBQoSIfLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDelayedPackets.setStatus("current")
_HwCBQoSIfLrDelayedBytes_Type = Counter32
_HwCBQoSIfLrDelayedBytes_Object = MibTableColumn
hwCBQoSIfLrDelayedBytes = _HwCBQoSIfLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 6),
    _HwCBQoSIfLrDelayedBytes_Type()
)
hwCBQoSIfLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrDelayedBytes.setStatus("current")
_HwCBQoSIfLrQueueSize_Type = Integer32
_HwCBQoSIfLrQueueSize_Object = MibTableColumn
hwCBQoSIfLrQueueSize = _HwCBQoSIfLrQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 1, 8, 1, 7),
    _HwCBQoSIfLrQueueSize_Type()
)
hwCBQoSIfLrQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfLrQueueSize.setStatus("current")
_HwCBQoSAtmPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSAtmPvcStaticsObjects = _HwCBQoSAtmPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2)
)
_HwCBQoSAtmPvcCbqRunInfoTable_Object = MibTable
hwCBQoSAtmPvcCbqRunInfoTable = _HwCBQoSAtmPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcCbqRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcCbqRunInfoEntry = _HwCBQoSAtmPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1)
)
hwCBQoSAtmPvcCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcCbqQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqQueueSize = _HwCBQoSAtmPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 1),
    _HwCBQoSAtmPvcCbqQueueSize_Type()
)
hwCBQoSAtmPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqDiscard_Type = Counter32
_HwCBQoSAtmPvcCbqDiscard_Object = MibTableColumn
hwCBQoSAtmPvcCbqDiscard = _HwCBQoSAtmPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 2),
    _HwCBQoSAtmPvcCbqDiscard_Type()
)
hwCBQoSAtmPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqDiscard.setStatus("current")
_HwCBQoSAtmPvcCbqEfQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqEfQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqEfQueueSize = _HwCBQoSAtmPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 3),
    _HwCBQoSAtmPvcCbqEfQueueSize_Type()
)
hwCBQoSAtmPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqEfQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqAfQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqAfQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqAfQueueSize = _HwCBQoSAtmPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 4),
    _HwCBQoSAtmPvcCbqAfQueueSize_Type()
)
hwCBQoSAtmPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqAfQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqBeQueueSize_Type = Integer32
_HwCBQoSAtmPvcCbqBeQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeQueueSize = _HwCBQoSAtmPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 5),
    _HwCBQoSAtmPvcCbqBeQueueSize_Type()
)
hwCBQoSAtmPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeQueueSize.setStatus("current")
_HwCBQoSAtmPvcCbqBeActiveQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqBeActiveQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeActiveQueueNum = _HwCBQoSAtmPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 6),
    _HwCBQoSAtmPvcCbqBeActiveQueueNum_Type()
)
hwCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeActiveQueueNum.setStatus("current")
_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeMaxActiveQueueNum = _HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 7),
    _HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type()
)
hwCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus("current")
_HwCBQoSAtmPvcCbqBeTotalQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqBeTotalQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqBeTotalQueueNum = _HwCBQoSAtmPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 8),
    _HwCBQoSAtmPvcCbqBeTotalQueueNum_Type()
)
hwCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqBeTotalQueueNum.setStatus("current")
_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Type = Integer32
_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hwCBQoSAtmPvcCbqAfAllocatedQueueNum = _HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 1, 1, 9),
    _HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Type()
)
hwCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus("current")
_HwCBQoSAtmPvcClassMatchRunInfoTable_Object = MibTable
hwCBQoSAtmPvcClassMatchRunInfoTable = _HwCBQoSAtmPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcClassMatchRunInfoEntry = _HwCBQoSAtmPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 2, 1)
)
hwCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcClassMatchPackets_Type = Counter32
_HwCBQoSAtmPvcClassMatchPackets_Object = MibTableColumn
hwCBQoSAtmPvcClassMatchPackets = _HwCBQoSAtmPvcClassMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 2, 1, 1),
    _HwCBQoSAtmPvcClassMatchPackets_Type()
)
hwCBQoSAtmPvcClassMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchPackets.setStatus("current")
_HwCBQoSAtmPvcClassMatchBytes_Type = Counter32
_HwCBQoSAtmPvcClassMatchBytes_Object = MibTableColumn
hwCBQoSAtmPvcClassMatchBytes = _HwCBQoSAtmPvcClassMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 2, 1, 2),
    _HwCBQoSAtmPvcClassMatchBytes_Type()
)
hwCBQoSAtmPvcClassMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassMatchBytes.setStatus("current")
_HwCBQoSAtmPvcClassAverageRate_Type = Counter64
_HwCBQoSAtmPvcClassAverageRate_Object = MibTableColumn
hwCBQoSAtmPvcClassAverageRate = _HwCBQoSAtmPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 2, 1, 3),
    _HwCBQoSAtmPvcClassAverageRate_Type()
)
hwCBQoSAtmPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcClassAverageRate.setStatus("current")
_HwCBQoSAtmPvcCarRunInfoTable_Object = MibTable
hwCBQoSAtmPvcCarRunInfoTable = _HwCBQoSAtmPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcCarRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcCarRunInfoEntry = _HwCBQoSAtmPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 3, 1)
)
hwCBQoSAtmPvcCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcCarConformPackets_Type = Counter32
_HwCBQoSAtmPvcCarConformPackets_Object = MibTableColumn
hwCBQoSAtmPvcCarConformPackets = _HwCBQoSAtmPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 3, 1, 1),
    _HwCBQoSAtmPvcCarConformPackets_Type()
)
hwCBQoSAtmPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarConformPackets.setStatus("current")
_HwCBQoSAtmPvcCarConformBytes_Type = Counter32
_HwCBQoSAtmPvcCarConformBytes_Object = MibTableColumn
hwCBQoSAtmPvcCarConformBytes = _HwCBQoSAtmPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 3, 1, 2),
    _HwCBQoSAtmPvcCarConformBytes_Type()
)
hwCBQoSAtmPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarConformBytes.setStatus("current")
_HwCBQoSAtmPvcCarExceedPackets_Type = Counter32
_HwCBQoSAtmPvcCarExceedPackets_Object = MibTableColumn
hwCBQoSAtmPvcCarExceedPackets = _HwCBQoSAtmPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 3, 1, 3),
    _HwCBQoSAtmPvcCarExceedPackets_Type()
)
hwCBQoSAtmPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarExceedPackets.setStatus("current")
_HwCBQoSAtmPvcCarExceedBytes_Type = Counter32
_HwCBQoSAtmPvcCarExceedBytes_Object = MibTableColumn
hwCBQoSAtmPvcCarExceedBytes = _HwCBQoSAtmPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 3, 1, 4),
    _HwCBQoSAtmPvcCarExceedBytes_Type()
)
hwCBQoSAtmPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcCarExceedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsRunInfoTable_Object = MibTable
hwCBQoSAtmPvcGtsRunInfoTable = _HwCBQoSAtmPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcGtsRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcGtsRunInfoEntry = _HwCBQoSAtmPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1)
)
hwCBQoSAtmPvcGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcGtsPassedPackets_Type = Counter32
_HwCBQoSAtmPvcGtsPassedPackets_Object = MibTableColumn
hwCBQoSAtmPvcGtsPassedPackets = _HwCBQoSAtmPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 1),
    _HwCBQoSAtmPvcGtsPassedPackets_Type()
)
hwCBQoSAtmPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsPassedPackets.setStatus("current")
_HwCBQoSAtmPvcGtsPassedBytes_Type = Counter32
_HwCBQoSAtmPvcGtsPassedBytes_Object = MibTableColumn
hwCBQoSAtmPvcGtsPassedBytes = _HwCBQoSAtmPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 2),
    _HwCBQoSAtmPvcGtsPassedBytes_Type()
)
hwCBQoSAtmPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsPassedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsDiscardedPackets_Type = Counter32
_HwCBQoSAtmPvcGtsDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcGtsDiscardedPackets = _HwCBQoSAtmPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 3),
    _HwCBQoSAtmPvcGtsDiscardedPackets_Type()
)
hwCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcGtsDiscardedBytes_Type = Counter32
_HwCBQoSAtmPvcGtsDiscardedBytes_Object = MibTableColumn
hwCBQoSAtmPvcGtsDiscardedBytes = _HwCBQoSAtmPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 4),
    _HwCBQoSAtmPvcGtsDiscardedBytes_Type()
)
hwCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDiscardedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsDelayedPackets_Type = Counter32
_HwCBQoSAtmPvcGtsDelayedPackets_Object = MibTableColumn
hwCBQoSAtmPvcGtsDelayedPackets = _HwCBQoSAtmPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 5),
    _HwCBQoSAtmPvcGtsDelayedPackets_Type()
)
hwCBQoSAtmPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDelayedPackets.setStatus("current")
_HwCBQoSAtmPvcGtsDelayedBytes_Type = Counter32
_HwCBQoSAtmPvcGtsDelayedBytes_Object = MibTableColumn
hwCBQoSAtmPvcGtsDelayedBytes = _HwCBQoSAtmPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 6),
    _HwCBQoSAtmPvcGtsDelayedBytes_Type()
)
hwCBQoSAtmPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsDelayedBytes.setStatus("current")
_HwCBQoSAtmPvcGtsQueueSize_Type = Integer32
_HwCBQoSAtmPvcGtsQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcGtsQueueSize = _HwCBQoSAtmPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 4, 1, 7),
    _HwCBQoSAtmPvcGtsQueueSize_Type()
)
hwCBQoSAtmPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcGtsQueueSize.setStatus("current")
_HwCBQoSAtmPvcRemarkRunInfoTable_Object = MibTable
hwCBQoSAtmPvcRemarkRunInfoTable = _HwCBQoSAtmPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcRemarkRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcRemarkRunInfoEntry = _HwCBQoSAtmPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 5, 1)
)
hwCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcRemarkedPackets_Type = Counter32
_HwCBQoSAtmPvcRemarkedPackets_Object = MibTableColumn
hwCBQoSAtmPvcRemarkedPackets = _HwCBQoSAtmPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 5, 1, 1),
    _HwCBQoSAtmPvcRemarkedPackets_Type()
)
hwCBQoSAtmPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcRemarkedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueRunInfoTable_Object = MibTable
hwCBQoSAtmPvcQueueRunInfoTable = _HwCBQoSAtmPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcQueueRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcQueueRunInfoEntry = _HwCBQoSAtmPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1)
)
hwCBQoSAtmPvcQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcQueueMatchedPackets_Type = Counter32
_HwCBQoSAtmPvcQueueMatchedPackets_Object = MibTableColumn
hwCBQoSAtmPvcQueueMatchedPackets = _HwCBQoSAtmPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1, 1),
    _HwCBQoSAtmPvcQueueMatchedPackets_Type()
)
hwCBQoSAtmPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueMatchedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueMatchedBytes_Type = Counter32
_HwCBQoSAtmPvcQueueMatchedBytes_Object = MibTableColumn
hwCBQoSAtmPvcQueueMatchedBytes = _HwCBQoSAtmPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1, 2),
    _HwCBQoSAtmPvcQueueMatchedBytes_Type()
)
hwCBQoSAtmPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueMatchedBytes.setStatus("current")
_HwCBQoSAtmPvcQueueEnqueuedPackets_Type = Counter32
_HwCBQoSAtmPvcQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedPackets = _HwCBQoSAtmPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1, 3),
    _HwCBQoSAtmPvcQueueEnqueuedPackets_Type()
)
hwCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueEnqueuedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueEnqueuedBytes_Type = Counter32
_HwCBQoSAtmPvcQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedBytes = _HwCBQoSAtmPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1, 4),
    _HwCBQoSAtmPvcQueueEnqueuedBytes_Type()
)
hwCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueEnqueuedBytes.setStatus("current")
_HwCBQoSAtmPvcQueueDiscardedPackets_Type = Counter32
_HwCBQoSAtmPvcQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcQueueDiscardedPackets = _HwCBQoSAtmPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1, 5),
    _HwCBQoSAtmPvcQueueDiscardedPackets_Type()
)
hwCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcQueueDiscardedBytes_Type = Counter32
_HwCBQoSAtmPvcQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSAtmPvcQueueDiscardedBytes = _HwCBQoSAtmPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 6, 1, 6),
    _HwCBQoSAtmPvcQueueDiscardedBytes_Type()
)
hwCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcQueueDiscardedBytes.setStatus("current")
_HwCBQoSAtmPvcWredRunInfoTable_Object = MibTable
hwCBQoSAtmPvcWredRunInfoTable = _HwCBQoSAtmPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcWredRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcWredRunInfoEntry = _HwCBQoSAtmPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 7, 1)
)
hwCBQoSAtmPvcWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcWredRandomDiscardedPackets_Type = Counter32
_HwCBQoSAtmPvcWredRandomDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcWredRandomDiscardedPackets = _HwCBQoSAtmPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 7, 1, 1),
    _HwCBQoSAtmPvcWredRandomDiscardedPackets_Type()
)
hwCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredRandomDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcWredTailDiscardedPackets_Type = Counter32
_HwCBQoSAtmPvcWredTailDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcWredTailDiscardedPackets = _HwCBQoSAtmPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 7, 1, 2),
    _HwCBQoSAtmPvcWredTailDiscardedPackets_Type()
)
hwCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcWredTailDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcLrRunInfoTable_Object = MibTable
hwCBQoSAtmPvcLrRunInfoTable = _HwCBQoSAtmPvcLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrRunInfoTable.setStatus("current")
_HwCBQoSAtmPvcLrRunInfoEntry_Object = MibTableRow
hwCBQoSAtmPvcLrRunInfoEntry = _HwCBQoSAtmPvcLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1)
)
hwCBQoSAtmPvcLrRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVPI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyVCI"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSAtmPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrRunInfoEntry.setStatus("current")
_HwCBQoSAtmPvcLrPassedPackets_Type = Counter32
_HwCBQoSAtmPvcLrPassedPackets_Object = MibTableColumn
hwCBQoSAtmPvcLrPassedPackets = _HwCBQoSAtmPvcLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 1),
    _HwCBQoSAtmPvcLrPassedPackets_Type()
)
hwCBQoSAtmPvcLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrPassedPackets.setStatus("current")
_HwCBQoSAtmPvcLrPassedBytes_Type = Counter32
_HwCBQoSAtmPvcLrPassedBytes_Object = MibTableColumn
hwCBQoSAtmPvcLrPassedBytes = _HwCBQoSAtmPvcLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 2),
    _HwCBQoSAtmPvcLrPassedBytes_Type()
)
hwCBQoSAtmPvcLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrPassedBytes.setStatus("current")
_HwCBQoSAtmPvcLrDiscardedPackets_Type = Counter32
_HwCBQoSAtmPvcLrDiscardedPackets_Object = MibTableColumn
hwCBQoSAtmPvcLrDiscardedPackets = _HwCBQoSAtmPvcLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 3),
    _HwCBQoSAtmPvcLrDiscardedPackets_Type()
)
hwCBQoSAtmPvcLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDiscardedPackets.setStatus("current")
_HwCBQoSAtmPvcLrDiscardedBytes_Type = Counter32
_HwCBQoSAtmPvcLrDiscardedBytes_Object = MibTableColumn
hwCBQoSAtmPvcLrDiscardedBytes = _HwCBQoSAtmPvcLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 4),
    _HwCBQoSAtmPvcLrDiscardedBytes_Type()
)
hwCBQoSAtmPvcLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDiscardedBytes.setStatus("current")
_HwCBQoSAtmPvcLrDelayedPackets_Type = Counter32
_HwCBQoSAtmPvcLrDelayedPackets_Object = MibTableColumn
hwCBQoSAtmPvcLrDelayedPackets = _HwCBQoSAtmPvcLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 5),
    _HwCBQoSAtmPvcLrDelayedPackets_Type()
)
hwCBQoSAtmPvcLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDelayedPackets.setStatus("current")
_HwCBQoSAtmPvcLrDelayedBytes_Type = Counter32
_HwCBQoSAtmPvcLrDelayedBytes_Object = MibTableColumn
hwCBQoSAtmPvcLrDelayedBytes = _HwCBQoSAtmPvcLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 6),
    _HwCBQoSAtmPvcLrDelayedBytes_Type()
)
hwCBQoSAtmPvcLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrDelayedBytes.setStatus("current")
_HwCBQoSAtmPvcLrQueueSize_Type = Integer32
_HwCBQoSAtmPvcLrQueueSize_Object = MibTableColumn
hwCBQoSAtmPvcLrQueueSize = _HwCBQoSAtmPvcLrQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 2, 8, 1, 7),
    _HwCBQoSAtmPvcLrQueueSize_Type()
)
hwCBQoSAtmPvcLrQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSAtmPvcLrQueueSize.setStatus("current")
_HwCBQoSFrPvcStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSFrPvcStaticsObjects = _HwCBQoSFrPvcStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3)
)
_HwCBQoSFrPvcCbqRunInfoTable_Object = MibTable
hwCBQoSFrPvcCbqRunInfoTable = _HwCBQoSFrPvcCbqRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqRunInfoTable.setStatus("current")
_HwCBQoSFrPvcCbqRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcCbqRunInfoEntry = _HwCBQoSFrPvcCbqRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1)
)
hwCBQoSFrPvcCbqRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcCbqQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqQueueSize = _HwCBQoSFrPvcCbqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 1),
    _HwCBQoSFrPvcCbqQueueSize_Type()
)
hwCBQoSFrPvcCbqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqDiscard_Type = Counter32
_HwCBQoSFrPvcCbqDiscard_Object = MibTableColumn
hwCBQoSFrPvcCbqDiscard = _HwCBQoSFrPvcCbqDiscard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 2),
    _HwCBQoSFrPvcCbqDiscard_Type()
)
hwCBQoSFrPvcCbqDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqDiscard.setStatus("current")
_HwCBQoSFrPvcCbqEfQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqEfQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqEfQueueSize = _HwCBQoSFrPvcCbqEfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 3),
    _HwCBQoSFrPvcCbqEfQueueSize_Type()
)
hwCBQoSFrPvcCbqEfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqEfQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqAfQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqAfQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqAfQueueSize = _HwCBQoSFrPvcCbqAfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 4),
    _HwCBQoSFrPvcCbqAfQueueSize_Type()
)
hwCBQoSFrPvcCbqAfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqAfQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqBeQueueSize_Type = Integer32
_HwCBQoSFrPvcCbqBeQueueSize_Object = MibTableColumn
hwCBQoSFrPvcCbqBeQueueSize = _HwCBQoSFrPvcCbqBeQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 5),
    _HwCBQoSFrPvcCbqBeQueueSize_Type()
)
hwCBQoSFrPvcCbqBeQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeQueueSize.setStatus("current")
_HwCBQoSFrPvcCbqBeActiveQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqBeActiveQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqBeActiveQueueNum = _HwCBQoSFrPvcCbqBeActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 6),
    _HwCBQoSFrPvcCbqBeActiveQueueNum_Type()
)
hwCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeActiveQueueNum.setStatus("current")
_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqBeMaxActiveQueueNum = _HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 7),
    _HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Type()
)
hwCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus("current")
_HwCBQoSFrPvcCbqBeTotalQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqBeTotalQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqBeTotalQueueNum = _HwCBQoSFrPvcCbqBeTotalQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 8),
    _HwCBQoSFrPvcCbqBeTotalQueueNum_Type()
)
hwCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqBeTotalQueueNum.setStatus("current")
_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Type = Integer32
_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Object = MibTableColumn
hwCBQoSFrPvcCbqAfAllocatedQueueNum = _HwCBQoSFrPvcCbqAfAllocatedQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 1, 1, 9),
    _HwCBQoSFrPvcCbqAfAllocatedQueueNum_Type()
)
hwCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus("current")
_HwCBQoSFrPvcClassMatchRunInfoTable_Object = MibTable
hwCBQoSFrPvcClassMatchRunInfoTable = _HwCBQoSFrPvcClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchRunInfoTable.setStatus("current")
_HwCBQoSFrPvcClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcClassMatchRunInfoEntry = _HwCBQoSFrPvcClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 2, 1)
)
hwCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcClassMatchedPackets_Type = Counter32
_HwCBQoSFrPvcClassMatchedPackets_Object = MibTableColumn
hwCBQoSFrPvcClassMatchedPackets = _HwCBQoSFrPvcClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 2, 1, 1),
    _HwCBQoSFrPvcClassMatchedPackets_Type()
)
hwCBQoSFrPvcClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchedPackets.setStatus("current")
_HwCBQoSFrPvcClassMatchedBytes_Type = Counter32
_HwCBQoSFrPvcClassMatchedBytes_Object = MibTableColumn
hwCBQoSFrPvcClassMatchedBytes = _HwCBQoSFrPvcClassMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 2, 1, 2),
    _HwCBQoSFrPvcClassMatchedBytes_Type()
)
hwCBQoSFrPvcClassMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassMatchedBytes.setStatus("current")
_HwCBQoSFrPvcClassAverageRate_Type = Counter64
_HwCBQoSFrPvcClassAverageRate_Object = MibTableColumn
hwCBQoSFrPvcClassAverageRate = _HwCBQoSFrPvcClassAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 2, 1, 3),
    _HwCBQoSFrPvcClassAverageRate_Type()
)
hwCBQoSFrPvcClassAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcClassAverageRate.setStatus("current")
_HwCBQoSFrPvcCarRunInfoTable_Object = MibTable
hwCBQoSFrPvcCarRunInfoTable = _HwCBQoSFrPvcCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarRunInfoTable.setStatus("current")
_HwCBQoSFrPvcCarRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcCarRunInfoEntry = _HwCBQoSFrPvcCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 3, 1)
)
hwCBQoSFrPvcCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcCarConformPackets_Type = Counter32
_HwCBQoSFrPvcCarConformPackets_Object = MibTableColumn
hwCBQoSFrPvcCarConformPackets = _HwCBQoSFrPvcCarConformPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 3, 1, 1),
    _HwCBQoSFrPvcCarConformPackets_Type()
)
hwCBQoSFrPvcCarConformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarConformPackets.setStatus("current")
_HwCBQoSFrPvcCarConformBytes_Type = Counter32
_HwCBQoSFrPvcCarConformBytes_Object = MibTableColumn
hwCBQoSFrPvcCarConformBytes = _HwCBQoSFrPvcCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 3, 1, 2),
    _HwCBQoSFrPvcCarConformBytes_Type()
)
hwCBQoSFrPvcCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarConformBytes.setStatus("current")
_HwCBQoSFrPvcCarExceedPackets_Type = Counter32
_HwCBQoSFrPvcCarExceedPackets_Object = MibTableColumn
hwCBQoSFrPvcCarExceedPackets = _HwCBQoSFrPvcCarExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 3, 1, 3),
    _HwCBQoSFrPvcCarExceedPackets_Type()
)
hwCBQoSFrPvcCarExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarExceedPackets.setStatus("current")
_HwCBQoSFrPvcCarExceedBytes_Type = Counter32
_HwCBQoSFrPvcCarExceedBytes_Object = MibTableColumn
hwCBQoSFrPvcCarExceedBytes = _HwCBQoSFrPvcCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 3, 1, 4),
    _HwCBQoSFrPvcCarExceedBytes_Type()
)
hwCBQoSFrPvcCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcCarExceedBytes.setStatus("current")
_HwCBQoSFrPvcGtsRunInfoTable_Object = MibTable
hwCBQoSFrPvcGtsRunInfoTable = _HwCBQoSFrPvcGtsRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsRunInfoTable.setStatus("current")
_HwCBQoSFrPvcGtsRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcGtsRunInfoEntry = _HwCBQoSFrPvcGtsRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1)
)
hwCBQoSFrPvcGtsRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcGtsPassedPackets_Type = Counter32
_HwCBQoSFrPvcGtsPassedPackets_Object = MibTableColumn
hwCBQoSFrPvcGtsPassedPackets = _HwCBQoSFrPvcGtsPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 1),
    _HwCBQoSFrPvcGtsPassedPackets_Type()
)
hwCBQoSFrPvcGtsPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsPassedPackets.setStatus("current")
_HwCBQoSFrPvcGtsPassedBytes_Type = Counter32
_HwCBQoSFrPvcGtsPassedBytes_Object = MibTableColumn
hwCBQoSFrPvcGtsPassedBytes = _HwCBQoSFrPvcGtsPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 2),
    _HwCBQoSFrPvcGtsPassedBytes_Type()
)
hwCBQoSFrPvcGtsPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsPassedBytes.setStatus("current")
_HwCBQoSFrPvcGtsDiscardedPackets_Type = Counter32
_HwCBQoSFrPvcGtsDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcGtsDiscardedPackets = _HwCBQoSFrPvcGtsDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 3),
    _HwCBQoSFrPvcGtsDiscardedPackets_Type()
)
hwCBQoSFrPvcGtsDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcGtsDiscardedBytes_Type = Counter32
_HwCBQoSFrPvcGtsDiscardedBytes_Object = MibTableColumn
hwCBQoSFrPvcGtsDiscardedBytes = _HwCBQoSFrPvcGtsDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 4),
    _HwCBQoSFrPvcGtsDiscardedBytes_Type()
)
hwCBQoSFrPvcGtsDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDiscardedBytes.setStatus("current")
_HwCBQoSFrPvcGtsDelayedPackets_Type = Counter32
_HwCBQoSFrPvcGtsDelayedPackets_Object = MibTableColumn
hwCBQoSFrPvcGtsDelayedPackets = _HwCBQoSFrPvcGtsDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 5),
    _HwCBQoSFrPvcGtsDelayedPackets_Type()
)
hwCBQoSFrPvcGtsDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDelayedPackets.setStatus("current")
_HwCBQoSFrPvcGtsDelayedBytes_Type = Counter32
_HwCBQoSFrPvcGtsDelayedBytes_Object = MibTableColumn
hwCBQoSFrPvcGtsDelayedBytes = _HwCBQoSFrPvcGtsDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 6),
    _HwCBQoSFrPvcGtsDelayedBytes_Type()
)
hwCBQoSFrPvcGtsDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsDelayedBytes.setStatus("current")
_HwCBQoSFrPvcGtsQueueSize_Type = Integer32
_HwCBQoSFrPvcGtsQueueSize_Object = MibTableColumn
hwCBQoSFrPvcGtsQueueSize = _HwCBQoSFrPvcGtsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 4, 1, 7),
    _HwCBQoSFrPvcGtsQueueSize_Type()
)
hwCBQoSFrPvcGtsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcGtsQueueSize.setStatus("current")
_HwCBQoSFrPvcRemarkRunInfoTable_Object = MibTable
hwCBQoSFrPvcRemarkRunInfoTable = _HwCBQoSFrPvcRemarkRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkRunInfoTable.setStatus("current")
_HwCBQoSFrPvcRemarkRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcRemarkRunInfoEntry = _HwCBQoSFrPvcRemarkRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 5, 1)
)
hwCBQoSFrPvcRemarkRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcRemarkedPackets_Type = Counter32
_HwCBQoSFrPvcRemarkedPackets_Object = MibTableColumn
hwCBQoSFrPvcRemarkedPackets = _HwCBQoSFrPvcRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 5, 1, 1),
    _HwCBQoSFrPvcRemarkedPackets_Type()
)
hwCBQoSFrPvcRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcRemarkedPackets.setStatus("current")
_HwCBQoSFrPvcQueueRunInfoTable_Object = MibTable
hwCBQoSFrPvcQueueRunInfoTable = _HwCBQoSFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueRunInfoTable.setStatus("current")
_HwCBQoSFrPvcQueueRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcQueueRunInfoEntry = _HwCBQoSFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1)
)
hwCBQoSFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcQueueMatchedPackets_Type = Counter32
_HwCBQoSFrPvcQueueMatchedPackets_Object = MibTableColumn
hwCBQoSFrPvcQueueMatchedPackets = _HwCBQoSFrPvcQueueMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1, 1),
    _HwCBQoSFrPvcQueueMatchedPackets_Type()
)
hwCBQoSFrPvcQueueMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueMatchedPackets.setStatus("current")
_HwCBQoSFrPvcQueueMatchedBytes_Type = Counter32
_HwCBQoSFrPvcQueueMatchedBytes_Object = MibTableColumn
hwCBQoSFrPvcQueueMatchedBytes = _HwCBQoSFrPvcQueueMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1, 2),
    _HwCBQoSFrPvcQueueMatchedBytes_Type()
)
hwCBQoSFrPvcQueueMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueMatchedBytes.setStatus("current")
_HwCBQoSFrPvcQueueEnqueuedPackets_Type = Counter32
_HwCBQoSFrPvcQueueEnqueuedPackets_Object = MibTableColumn
hwCBQoSFrPvcQueueEnqueuedPackets = _HwCBQoSFrPvcQueueEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1, 3),
    _HwCBQoSFrPvcQueueEnqueuedPackets_Type()
)
hwCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueEnqueuedPackets.setStatus("current")
_HwCBQoSFrPvcQueueEnqueuedBytes_Type = Counter32
_HwCBQoSFrPvcQueueEnqueuedBytes_Object = MibTableColumn
hwCBQoSFrPvcQueueEnqueuedBytes = _HwCBQoSFrPvcQueueEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1, 4),
    _HwCBQoSFrPvcQueueEnqueuedBytes_Type()
)
hwCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueEnqueuedBytes.setStatus("current")
_HwCBQoSFrPvcQueueDiscardedPackets_Type = Counter32
_HwCBQoSFrPvcQueueDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcQueueDiscardedPackets = _HwCBQoSFrPvcQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1, 5),
    _HwCBQoSFrPvcQueueDiscardedPackets_Type()
)
hwCBQoSFrPvcQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcQueueDiscardedBytes_Type = Counter32
_HwCBQoSFrPvcQueueDiscardedBytes_Object = MibTableColumn
hwCBQoSFrPvcQueueDiscardedBytes = _HwCBQoSFrPvcQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 6, 1, 6),
    _HwCBQoSFrPvcQueueDiscardedBytes_Type()
)
hwCBQoSFrPvcQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcQueueDiscardedBytes.setStatus("current")
_HwCBQoSFrPvcWredRunInfoTable_Object = MibTable
hwCBQoSFrPvcWredRunInfoTable = _HwCBQoSFrPvcWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRunInfoTable.setStatus("current")
_HwCBQoSFrPvcWredRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcWredRunInfoEntry = _HwCBQoSFrPvcWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 7, 1)
)
hwCBQoSFrPvcWredRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSWredClassValue"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcWredRandomDiscardedPackets_Type = Counter32
_HwCBQoSFrPvcWredRandomDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcWredRandomDiscardedPackets = _HwCBQoSFrPvcWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 7, 1, 1),
    _HwCBQoSFrPvcWredRandomDiscardedPackets_Type()
)
hwCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredRandomDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcWredTailDiscardedPackets_Type = Counter32
_HwCBQoSFrPvcWredTailDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcWredTailDiscardedPackets = _HwCBQoSFrPvcWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 7, 1, 2),
    _HwCBQoSFrPvcWredTailDiscardedPackets_Type()
)
hwCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcWredTailDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcLrRunInfoTable_Object = MibTable
hwCBQoSFrPvcLrRunInfoTable = _HwCBQoSFrPvcLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrRunInfoTable.setStatus("current")
_HwCBQoSFrPvcLrRunInfoEntry_Object = MibTableRow
hwCBQoSFrPvcLrRunInfoEntry = _HwCBQoSFrPvcLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1)
)
hwCBQoSFrPvcLrRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDlciNum"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSFrPvcApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrRunInfoEntry.setStatus("current")
_HwCBQoSFrPvcLrPassedPackets_Type = Counter32
_HwCBQoSFrPvcLrPassedPackets_Object = MibTableColumn
hwCBQoSFrPvcLrPassedPackets = _HwCBQoSFrPvcLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 1),
    _HwCBQoSFrPvcLrPassedPackets_Type()
)
hwCBQoSFrPvcLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrPassedPackets.setStatus("current")
_HwCBQoSFrPvcLrPassedBytes_Type = Counter32
_HwCBQoSFrPvcLrPassedBytes_Object = MibTableColumn
hwCBQoSFrPvcLrPassedBytes = _HwCBQoSFrPvcLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 2),
    _HwCBQoSFrPvcLrPassedBytes_Type()
)
hwCBQoSFrPvcLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrPassedBytes.setStatus("current")
_HwCBQoSFrPvcLrDiscardedPackets_Type = Counter32
_HwCBQoSFrPvcLrDiscardedPackets_Object = MibTableColumn
hwCBQoSFrPvcLrDiscardedPackets = _HwCBQoSFrPvcLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 3),
    _HwCBQoSFrPvcLrDiscardedPackets_Type()
)
hwCBQoSFrPvcLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDiscardedPackets.setStatus("current")
_HwCBQoSFrPvcLrDiscardedBytes_Type = Counter32
_HwCBQoSFrPvcLrDiscardedBytes_Object = MibTableColumn
hwCBQoSFrPvcLrDiscardedBytes = _HwCBQoSFrPvcLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 4),
    _HwCBQoSFrPvcLrDiscardedBytes_Type()
)
hwCBQoSFrPvcLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDiscardedBytes.setStatus("current")
_HwCBQoSFrPvcLrDelayedPackets_Type = Counter32
_HwCBQoSFrPvcLrDelayedPackets_Object = MibTableColumn
hwCBQoSFrPvcLrDelayedPackets = _HwCBQoSFrPvcLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 5),
    _HwCBQoSFrPvcLrDelayedPackets_Type()
)
hwCBQoSFrPvcLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDelayedPackets.setStatus("current")
_HwCBQoSFrPvcLrDelayedBytes_Type = Counter32
_HwCBQoSFrPvcLrDelayedBytes_Object = MibTableColumn
hwCBQoSFrPvcLrDelayedBytes = _HwCBQoSFrPvcLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 6),
    _HwCBQoSFrPvcLrDelayedBytes_Type()
)
hwCBQoSFrPvcLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrDelayedBytes.setStatus("current")
_HwCBQoSFrPvcLrQueueSize_Type = Integer32
_HwCBQoSFrPvcLrQueueSize_Object = MibTableColumn
hwCBQoSFrPvcLrQueueSize = _HwCBQoSFrPvcLrQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 3, 8, 1, 7),
    _HwCBQoSFrPvcLrQueueSize_Type()
)
hwCBQoSFrPvcLrQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSFrPvcLrQueueSize.setStatus("current")
_HwCBQoSIfVlanStaticsObjects_ObjectIdentity = ObjectIdentity
hwCBQoSIfVlanStaticsObjects = _HwCBQoSIfVlanStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 4)
)
_HwCBQoSIfVlanClassMatchRunInfoTable_Object = MibTable
hwCBQoSIfVlanClassMatchRunInfoTable = _HwCBQoSIfVlanClassMatchRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchRunInfoTable.setStatus("current")
_HwCBQoSIfVlanClassMatchRunInfoEntry_Object = MibTableRow
hwCBQoSIfVlanClassMatchRunInfoEntry = _HwCBQoSIfVlanClassMatchRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 4, 1, 1)
)
hwCBQoSIfVlanClassMatchRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyIfIndex"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyVlanid"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSIfVlanApplyPolicyDirection"),
    (0, "A3COM-HUAWEI-CBQOS-MIB", "hwCBQoSPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchRunInfoEntry.setStatus("current")
_HwCBQoSIfVlanClassMatchedPackets_Type = Counter32
_HwCBQoSIfVlanClassMatchedPackets_Object = MibTableColumn
hwCBQoSIfVlanClassMatchedPackets = _HwCBQoSIfVlanClassMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 32, 1, 1, 5, 4, 1, 1, 1),
    _HwCBQoSIfVlanClassMatchedPackets_Type()
)
hwCBQoSIfVlanClassMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCBQoSIfVlanClassMatchedPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-CBQOS-MIB",
    **{"MatchRuleType": MatchRuleType,
       "CarAction": CarAction,
       "RemarkType": RemarkType,
       "WredType": WredType,
       "QueueType": QueueType,
       "QueueBandwidthUnit": QueueBandwidthUnit,
       "LrCirUnit": LrCirUnit,
       "DirectionType": DirectionType,
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
       "hwCBQoSCarRedAction": hwCBQoSCarRedAction,
       "hwCBQoSCarRedRemarkValue": hwCBQoSCarRedRemarkValue,
       "hwCBQoSCarRowStatus": hwCBQoSCarRowStatus,
       "hwCBQoSGtsCfgInfoTable": hwCBQoSGtsCfgInfoTable,
       "hwCBQoSGtsCfgInfoEntry": hwCBQoSGtsCfgInfoEntry,
       "hwCBQoSGtsCir": hwCBQoSGtsCir,
       "hwCBQoSGtsCbs": hwCBQoSGtsCbs,
       "hwCBQoSGtsEbs": hwCBQoSGtsEbs,
       "hwCBQoSGtsQueueLength": hwCBQoSGtsQueueLength,
       "hwCBQoSGtsRowStatus": hwCBQoSGtsRowStatus,
       "hwCBQoSRemarkCfgInfoTable": hwCBQoSRemarkCfgInfoTable,
       "hwCBQoSRemarkCfgInfoEntry": hwCBQoSRemarkCfgInfoEntry,
       "hwCBQoSRemarkType": hwCBQoSRemarkType,
       "hwCBQoSRemarkValue": hwCBQoSRemarkValue,
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
       "hwCBQoSWredClassCfgInfoTable": hwCBQoSWredClassCfgInfoTable,
       "hwCBQoSWredClassCfgInfoEntry": hwCBQoSWredClassCfgInfoEntry,
       "hwCBQoSWredClassValue": hwCBQoSWredClassValue,
       "hwCBQoSWredClassLowLimit": hwCBQoSWredClassLowLimit,
       "hwCBQoSWredClassHighLimit": hwCBQoSWredClassHighLimit,
       "hwCBQoSWredClassDiscardProb": hwCBQoSWredClassDiscardProb,
       "hwCBQoSPolicyRouteCfgInfoTable": hwCBQoSPolicyRouteCfgInfoTable,
       "hwCBQoSPolicyRouteCfgInfoEntry": hwCBQoSPolicyRouteCfgInfoEntry,
       "hwCBQoSPolicyRouteNexthop": hwCBQoSPolicyRouteNexthop,
       "hwCBQoSPolicyRouteBackup": hwCBQoSPolicyRouteBackup,
       "hwCBQoSPolicyRouteRowStatus": hwCBQoSPolicyRouteRowStatus,
       "hwCBQoSNatCfgInfoTable": hwCBQoSNatCfgInfoTable,
       "hwCBQoSNatCfgInfoEntry": hwCBQoSNatCfgInfoEntry,
       "hwCBQoSNatMainNumber": hwCBQoSNatMainNumber,
       "hwCBQoSNatBackupNumber": hwCBQoSNatBackupNumber,
       "hwCBQoSNatServiceClass": hwCBQoSNatServiceClass,
       "hwCBQoSNatRowStatus": hwCBQoSNatRowStatus,
       "hwCBQoSFirewallCfgInfoTable": hwCBQoSFirewallCfgInfoTable,
       "hwCBQoSFirewallCfgInfoEntry": hwCBQoSFirewallCfgInfoEntry,
       "hwCBQoSFirewallAction": hwCBQoSFirewallAction,
       "hwCBQoSFirewallRowStatus": hwCBQoSFirewallRowStatus,
       "hwCBQoSSamplingCfgInfoTable": hwCBQoSSamplingCfgInfoTable,
       "hwCBQoSSamplingCfgInfoEntry": hwCBQoSSamplingCfgInfoEntry,
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
       "hwCBQoSPolicyObjects": hwCBQoSPolicyObjects,
       "hwCBQoSPolicyIndexNext": hwCBQoSPolicyIndexNext,
       "hwCBQoSPolicyCfgInfoTable": hwCBQoSPolicyCfgInfoTable,
       "hwCBQoSPolicyCfgInfoEntry": hwCBQoSPolicyCfgInfoEntry,
       "hwCBQoSPolicyIndex": hwCBQoSPolicyIndex,
       "hwCBQoSPolicyName": hwCBQoSPolicyName,
       "hwCBQoSPolicyClassCount": hwCBQoSPolicyClassCount,
       "hwCBQoSPolicyConfigMode": hwCBQoSPolicyConfigMode,
       "hwCBQoSPolicyRowStatus": hwCBQoSPolicyRowStatus,
       "hwCBQoSPolicyClassCfgInfoTable": hwCBQoSPolicyClassCfgInfoTable,
       "hwCBQoSPolicyClassCfgInfoEntry": hwCBQoSPolicyClassCfgInfoEntry,
       "hwCBQoSPolicyClassIndex": hwCBQoSPolicyClassIndex,
       "hwCBQoSPolicyClassClassifierIndex": hwCBQoSPolicyClassClassifierIndex,
       "hwCBQoSPolicyClassClassifierName": hwCBQoSPolicyClassClassifierName,
       "hwCBQoSPolicyClassBehaviorIndex": hwCBQoSPolicyClassBehaviorIndex,
       "hwCBQoSPolicyClassBehaviorName": hwCBQoSPolicyClassBehaviorName,
       "hwCBQoSPolicyClassPrecedence": hwCBQoSPolicyClassPrecedence,
       "hwCBQoSPolicyClassRowStatus": hwCBQoSPolicyClassRowStatus,
       "hwCBQoSApplyPolicyObjects": hwCBQoSApplyPolicyObjects,
       "hwCBQoSIfApplyPolicyTable": hwCBQoSIfApplyPolicyTable,
       "hwCBQoSIfApplyPolicyEntry": hwCBQoSIfApplyPolicyEntry,
       "hwCBQoSIfApplyPolicyIfIndex": hwCBQoSIfApplyPolicyIfIndex,
       "hwCBQoSIfApplyPolicyDirection": hwCBQoSIfApplyPolicyDirection,
       "hwCBQoSIfApplyPolicyName": hwCBQoSIfApplyPolicyName,
       "hwCBQoSIfApplyPolicyEnableDynamic": hwCBQoSIfApplyPolicyEnableDynamic,
       "hwCBQoSIfApplyPolicyRowStatus": hwCBQoSIfApplyPolicyRowStatus,
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
       "hwCBQoSIfVlanApplyPolicyVlanid": hwCBQoSIfVlanApplyPolicyVlanid,
       "hwCBQoSIfVlanApplyPolicyDirection": hwCBQoSIfVlanApplyPolicyDirection,
       "hwCBQoSIfVlanApplyPolicyName": hwCBQoSIfVlanApplyPolicyName,
       "hwCBQoSIfVlanApplyPolicyRowStatus": hwCBQoSIfVlanApplyPolicyRowStatus,
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
       "hwCBQoSIfCarRunInfoTable": hwCBQoSIfCarRunInfoTable,
       "hwCBQoSIfCarRunInfoEntry": hwCBQoSIfCarRunInfoEntry,
       "hwCBQoSIfCarGreenPackets": hwCBQoSIfCarGreenPackets,
       "hwCBQoSIfCarGreenBytes": hwCBQoSIfCarGreenBytes,
       "hwCBQoSIfCarRedPackets": hwCBQoSIfCarRedPackets,
       "hwCBQoSIfCarRedBytes": hwCBQoSIfCarRedBytes,
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
       "hwCBQoSIfQueueRunInfoTable": hwCBQoSIfQueueRunInfoTable,
       "hwCBQoSIfQueueRunInfoEntry": hwCBQoSIfQueueRunInfoEntry,
       "hwCBQoSIfQueueMatchedPackets": hwCBQoSIfQueueMatchedPackets,
       "hwCBQoSIfQueueMatchedBytes": hwCBQoSIfQueueMatchedBytes,
       "hwCBQoSIfQueueEnqueuedPackets": hwCBQoSIfQueueEnqueuedPackets,
       "hwCBQoSIfQueueEnqueuedBytes": hwCBQoSIfQueueEnqueuedBytes,
       "hwCBQoSIfQueueDiscardedPackets": hwCBQoSIfQueueDiscardedPackets,
       "hwCBQoSIfQueueDiscardedBytes": hwCBQoSIfQueueDiscardedBytes,
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
       "hwCBQoSIfLrQueueSize": hwCBQoSIfLrQueueSize,
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
       "hwCBQoSAtmPvcLrQueueSize": hwCBQoSAtmPvcLrQueueSize,
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
       "hwCBQoSFrPvcLrQueueSize": hwCBQoSFrPvcLrQueueSize,
       "hwCBQoSIfVlanStaticsObjects": hwCBQoSIfVlanStaticsObjects,
       "hwCBQoSIfVlanClassMatchRunInfoTable": hwCBQoSIfVlanClassMatchRunInfoTable,
       "hwCBQoSIfVlanClassMatchRunInfoEntry": hwCBQoSIfVlanClassMatchRunInfoEntry,
       "hwCBQoSIfVlanClassMatchedPackets": hwCBQoSIfVlanClassMatchedPackets}
)
