# SNMP MIB module (A3COM-FILTER-R5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-FILTER-R5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:12 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

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


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComFilter_ObjectIdentity = ObjectIdentity
a3ComFilter = _A3ComFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 10)
)
_A3ComFilterCtl_ObjectIdentity = ObjectIdentity
a3ComFilterCtl = _A3ComFilterCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1)
)


class _A3filterControl_Type(Integer32):
    """Custom type a3filterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableCheckAll", 2),
          ("enableMatchOne", 1))
    )


_A3filterControl_Type.__name__ = "Integer32"
_A3filterControl_Object = MibScalar
a3filterControl = _A3filterControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 1),
    _A3filterControl_Type()
)
a3filterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterControl.setStatus("mandatory")


class _A3filterDefaultAction_Type(Integer32):
    """Custom type a3filterDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_A3filterDefaultAction_Type.__name__ = "Integer32"
_A3filterDefaultAction_Object = MibScalar
a3filterDefaultAction = _A3filterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 2),
    _A3filterDefaultAction_Type()
)
a3filterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterDefaultAction.setStatus("mandatory")


class _A3filterBridgeSelect_Type(Integer32):
    """Custom type a3filterBridgeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("noFilter", 2))
    )


_A3filterBridgeSelect_Type.__name__ = "Integer32"
_A3filterBridgeSelect_Object = MibScalar
a3filterBridgeSelect = _A3filterBridgeSelect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 3),
    _A3filterBridgeSelect_Type()
)
a3filterBridgeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterBridgeSelect.setStatus("mandatory")


class _A3filterIpSelect_Type(Integer32):
    """Custom type a3filterIpSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("noFilter", 2))
    )


_A3filterIpSelect_Type.__name__ = "Integer32"
_A3filterIpSelect_Object = MibScalar
a3filterIpSelect = _A3filterIpSelect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 4),
    _A3filterIpSelect_Type()
)
a3filterIpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterIpSelect.setStatus("mandatory")


class _A3filterIpxSelect_Type(Integer32):
    """Custom type a3filterIpxSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("noFilter", 2))
    )


_A3filterIpxSelect_Type.__name__ = "Integer32"
_A3filterIpxSelect_Object = MibScalar
a3filterIpxSelect = _A3filterIpxSelect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 5),
    _A3filterIpxSelect_Type()
)
a3filterIpxSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterIpxSelect.setStatus("mandatory")


class _A3filterAppleTalkSelect_Type(Integer32):
    """Custom type a3filterAppleTalkSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("noFilter", 2))
    )


_A3filterAppleTalkSelect_Type.__name__ = "Integer32"
_A3filterAppleTalkSelect_Object = MibScalar
a3filterAppleTalkSelect = _A3filterAppleTalkSelect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 6),
    _A3filterAppleTalkSelect_Type()
)
a3filterAppleTalkSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterAppleTalkSelect.setStatus("mandatory")


class _A3filterDecSelect_Type(Integer32):
    """Custom type a3filterDecSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("noFilter", 2))
    )


_A3filterDecSelect_Type.__name__ = "Integer32"
_A3filterDecSelect_Object = MibScalar
a3filterDecSelect = _A3filterDecSelect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 1, 7),
    _A3filterDecSelect_Type()
)
a3filterDecSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterDecSelect.setStatus("mandatory")
_A3filterUserMaskTable_Object = MibTable
a3filterUserMaskTable = _A3filterUserMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2)
)
if mibBuilder.loadTexts:
    a3filterUserMaskTable.setStatus("mandatory")
_A3filterUserMaskEntry_Object = MibTableRow
a3filterUserMaskEntry = _A3filterUserMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1)
)
a3filterUserMaskEntry.setIndexNames(
    (0, "A3COM-FILTER-R5-MIB", "a3filterUserMaskIndex"),
)
if mibBuilder.loadTexts:
    a3filterUserMaskEntry.setStatus("mandatory")


class _A3filterUserMaskIndex_Type(Integer32):
    """Custom type a3filterUserMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_A3filterUserMaskIndex_Type.__name__ = "Integer32"
_A3filterUserMaskIndex_Object = MibTableColumn
a3filterUserMaskIndex = _A3filterUserMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 1),
    _A3filterUserMaskIndex_Type()
)
a3filterUserMaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterUserMaskIndex.setStatus("mandatory")


class _A3filterUserMaskName_Type(DisplayString):
    """Custom type a3filterUserMaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_A3filterUserMaskName_Type.__name__ = "DisplayString"
_A3filterUserMaskName_Object = MibTableColumn
a3filterUserMaskName = _A3filterUserMaskName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 2),
    _A3filterUserMaskName_Type()
)
a3filterUserMaskName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskName.setStatus("mandatory")


class _A3filterUserMaskLocType_Type(Integer32):
    """Custom type a3filterUserMaskLocType based on Integer32"""
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
        *(("appleTalkOffsetLengthSemantics", 6),
          ("dataLinkOffsetLengthSemantics", 3),
          ("decNetOffsetLengthSemantics", 7),
          ("ipOffsetLengthSemantics", 4),
          ("ipxOffsetLengthSemantics", 5),
          ("offsetLengthSemantics", 2),
          ("protocolFieldSemantics", 1))
    )


_A3filterUserMaskLocType_Type.__name__ = "Integer32"
_A3filterUserMaskLocType_Object = MibTableColumn
a3filterUserMaskLocType = _A3filterUserMaskLocType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 3),
    _A3filterUserMaskLocType_Type()
)
a3filterUserMaskLocType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskLocType.setStatus("mandatory")


class _A3filterUserMaskLocField_Type(Integer32):
    """Custom type a3filterUserMaskLocField based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47)
        )
    )
    namedValues = NamedValues(
        *(("atDDPType", 38),
          ("atDestinationNetwork", 29),
          ("atDestinationNodeID", 32),
          ("atDestinationSocket", 35),
          ("atNetwork", 31),
          ("atNodeID", 34),
          ("atSocket", 37),
          ("atSourceNetwork", 30),
          ("atSourceNodeID", 33),
          ("atSourceSocket", 36),
          ("decAddress", 44),
          ("decArea", 41),
          ("decDestAddress", 42),
          ("decDestinationArea", 39),
          ("decSourceAddress", 43),
          ("decSourceArea", 40),
          ("dlAddress", 3),
          ("dlDSAP", 6),
          ("dlDestinationAddress", 1),
          ("dlLSAP", 8),
          ("dlLanID", 10),
          ("dlLength", 5),
          ("dlOUI", 9),
          ("dlProtocol", 4),
          ("dlSSAP", 7),
          ("dlSourceAddress", 2),
          ("ipAddress", 13),
          ("ipDestAddress", 11),
          ("ipDestinationPort", 15),
          ("ipOptions", 18),
          ("ipPort", 17),
          ("ipProtocol", 14),
          ("ipSourceAddress", 12),
          ("ipSourcePort", 16),
          ("ipTOS", 19),
          ("ipxAddress", 25),
          ("ipxDestAddress", 23),
          ("ipxDestNetwork", 20),
          ("ipxDestSocket", 26),
          ("ipxNetwork", 22),
          ("ipxPktLength", 45),
          ("ipxPktType", 46),
          ("ipxSocket", 28),
          ("ipxSourceAddress", 24),
          ("ipxSourceNetwork", 21),
          ("ipxSourceSocket", 27),
          ("ipxTransportCtl", 47))
    )


_A3filterUserMaskLocField_Type.__name__ = "Integer32"
_A3filterUserMaskLocField_Object = MibTableColumn
a3filterUserMaskLocField = _A3filterUserMaskLocField_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 4),
    _A3filterUserMaskLocField_Type()
)
a3filterUserMaskLocField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskLocField.setStatus("mandatory")
_A3filterUserMaskLocOffset_Type = Integer32
_A3filterUserMaskLocOffset_Object = MibTableColumn
a3filterUserMaskLocOffset = _A3filterUserMaskLocOffset_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 5),
    _A3filterUserMaskLocOffset_Type()
)
a3filterUserMaskLocOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskLocOffset.setStatus("mandatory")


class _A3filterUserMaskLocLength_Type(Integer32):
    """Custom type a3filterUserMaskLocLength based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("reserved", 3),
          ("rsvd", 5),
          ("six", 6),
          ("two", 2))
    )


_A3filterUserMaskLocLength_Type.__name__ = "Integer32"
_A3filterUserMaskLocLength_Object = MibTableColumn
a3filterUserMaskLocLength = _A3filterUserMaskLocLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 6),
    _A3filterUserMaskLocLength_Type()
)
a3filterUserMaskLocLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskLocLength.setStatus("mandatory")


class _A3filterUserMaskOperator_Type(Integer32):
    """Custom type a3filterUserMaskOperator based on Integer32"""
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
        *(("and", 3),
          ("none", 1),
          ("or", 2),
          ("xor", 4))
    )


_A3filterUserMaskOperator_Type.__name__ = "Integer32"
_A3filterUserMaskOperator_Object = MibTableColumn
a3filterUserMaskOperator = _A3filterUserMaskOperator_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 7),
    _A3filterUserMaskOperator_Type()
)
a3filterUserMaskOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskOperator.setStatus("mandatory")


class _A3filterUserMaskOperand_Type(OctetString):
    """Custom type a3filterUserMaskOperand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_A3filterUserMaskOperand_Type.__name__ = "OctetString"
_A3filterUserMaskOperand_Object = MibTableColumn
a3filterUserMaskOperand = _A3filterUserMaskOperand_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 8),
    _A3filterUserMaskOperand_Type()
)
a3filterUserMaskOperand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskOperand.setStatus("mandatory")


class _A3filterUserMaskComparison_Type(Integer32):
    """Custom type a3filterUserMaskComparison based on Integer32"""
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
        *(("equal", 1),
          ("greaterThan", 3),
          ("greaterThanOrEqual", 4),
          ("inclusiveRange", 7),
          ("lessThan", 5),
          ("lessThanOrEqual", 6),
          ("notEqual", 2))
    )


_A3filterUserMaskComparison_Type.__name__ = "Integer32"
_A3filterUserMaskComparison_Object = MibTableColumn
a3filterUserMaskComparison = _A3filterUserMaskComparison_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 9),
    _A3filterUserMaskComparison_Type()
)
a3filterUserMaskComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskComparison.setStatus("mandatory")


class _A3filterUserMaskMatchType_Type(Integer32):
    """Custom type a3filterUserMaskMatchType based on Integer32"""
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
        *(("all", 1),
          ("bits", 2),
          ("userGroup", 5),
          ("value", 3),
          ("valueRange", 4))
    )


_A3filterUserMaskMatchType_Type.__name__ = "Integer32"
_A3filterUserMaskMatchType_Object = MibTableColumn
a3filterUserMaskMatchType = _A3filterUserMaskMatchType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 10),
    _A3filterUserMaskMatchType_Type()
)
a3filterUserMaskMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskMatchType.setStatus("mandatory")


class _A3filterUserMaskMatchBits_Type(OctetString):
    """Custom type a3filterUserMaskMatchBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_A3filterUserMaskMatchBits_Type.__name__ = "OctetString"
_A3filterUserMaskMatchBits_Object = MibTableColumn
a3filterUserMaskMatchBits = _A3filterUserMaskMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 11),
    _A3filterUserMaskMatchBits_Type()
)
a3filterUserMaskMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskMatchBits.setStatus("mandatory")
_A3filterUserMaskMatchValue1_Type = Integer32
_A3filterUserMaskMatchValue1_Object = MibTableColumn
a3filterUserMaskMatchValue1 = _A3filterUserMaskMatchValue1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 12),
    _A3filterUserMaskMatchValue1_Type()
)
a3filterUserMaskMatchValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskMatchValue1.setStatus("mandatory")
_A3filterUserMaskMatchValue2_Type = Integer32
_A3filterUserMaskMatchValue2_Object = MibTableColumn
a3filterUserMaskMatchValue2 = _A3filterUserMaskMatchValue2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 13),
    _A3filterUserMaskMatchValue2_Type()
)
a3filterUserMaskMatchValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskMatchValue2.setStatus("mandatory")
_A3filterUserMaskStatus_Type = RowStatus
_A3filterUserMaskStatus_Object = MibTableColumn
a3filterUserMaskStatus = _A3filterUserMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 2, 1, 14),
    _A3filterUserMaskStatus_Type()
)
a3filterUserMaskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserMaskStatus.setStatus("mandatory")
_A3filterBuiltInMaskTable_Object = MibTable
a3filterBuiltInMaskTable = _A3filterBuiltInMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 3)
)
if mibBuilder.loadTexts:
    a3filterBuiltInMaskTable.setStatus("mandatory")
_A3filterBuiltInMaskEntry_Object = MibTableRow
a3filterBuiltInMaskEntry = _A3filterBuiltInMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1)
)
a3filterBuiltInMaskEntry.setIndexNames(
    (0, "A3COM-FILTER-R5-MIB", "a3filterBuiltInMaskIndex"),
)
if mibBuilder.loadTexts:
    a3filterBuiltInMaskEntry.setStatus("mandatory")


class _A3filterBuiltInMaskIndex_Type(Integer32):
    """Custom type a3filterBuiltInMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 65535),
    )


_A3filterBuiltInMaskIndex_Type.__name__ = "Integer32"
_A3filterBuiltInMaskIndex_Object = MibTableColumn
a3filterBuiltInMaskIndex = _A3filterBuiltInMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1, 1),
    _A3filterBuiltInMaskIndex_Type()
)
a3filterBuiltInMaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterBuiltInMaskIndex.setStatus("mandatory")


class _A3filterBuiltInMaskName_Type(DisplayString):
    """Custom type a3filterBuiltInMaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_A3filterBuiltInMaskName_Type.__name__ = "DisplayString"
_A3filterBuiltInMaskName_Object = MibTableColumn
a3filterBuiltInMaskName = _A3filterBuiltInMaskName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1, 2),
    _A3filterBuiltInMaskName_Type()
)
a3filterBuiltInMaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterBuiltInMaskName.setStatus("mandatory")


class _A3filterBuiltInMaskFieldValue_Type(Integer32):
    """Custom type a3filterBuiltInMaskFieldValue based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60)
        )
    )
    namedValues = NamedValues(
        *(("aarp", 4),
          ("adsp", 57),
          ("aep", 54),
          ("allRouteExp", 19),
          ("allRouteType", 20),
          ("appleTalkII", 3),
          ("arp", 5),
          ("atp", 53),
          ("clnp", 6),
          ("decPhaseIV", 7),
          ("diag", 47),
          ("dlBroadCast", 1),
          ("dlMultiCast", 2),
          ("dlTest", 8),
          ("dns", 24),
          ("fileServicePkt", 43),
          ("finger", 25),
          ("five", 39),
          ("four", 38),
          ("ftp", 26),
          ("icmp", 21),
          ("ip", 9),
          ("ipNetMap", 12),
          ("ipx", 10),
          ("ipxBroadCast", 42),
          ("ipxNwSec", 60),
          ("ipxPing", 59),
          ("ipxTraceRt", 58),
          ("lat", 11),
          ("nbp", 52),
          ("netBIOS", 46),
          ("nis", 49),
          ("one", 35),
          ("rip", 45),
          ("rtmprq", 55),
          ("rtmprs", 51),
          ("rtmps", 48),
          ("sap", 44),
          ("seven", 41),
          ("simpleMailTrans", 28),
          ("singleRouteExp", 18),
          ("six", 40),
          ("snmp", 29),
          ("specificRoute", 17),
          ("stp", 14),
          ("sunRPC", 30),
          ("tcp", 22),
          ("telnet", 31),
          ("tftp", 32),
          ("three", 37),
          ("two", 36),
          ("udp", 23),
          ("vip", 15),
          ("whois", 27),
          ("x400", 33),
          ("xns", 16),
          ("xnsNetMap", 13),
          ("zero", 34),
          ("zip", 56),
          ("zis", 50))
    )


_A3filterBuiltInMaskFieldValue_Type.__name__ = "Integer32"
_A3filterBuiltInMaskFieldValue_Object = MibTableColumn
a3filterBuiltInMaskFieldValue = _A3filterBuiltInMaskFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 3, 1, 3),
    _A3filterBuiltInMaskFieldValue_Type()
)
a3filterBuiltInMaskFieldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterBuiltInMaskFieldValue.setStatus("mandatory")
_A3filterUserGrpTable_Object = MibTable
a3filterUserGrpTable = _A3filterUserGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 4)
)
if mibBuilder.loadTexts:
    a3filterUserGrpTable.setStatus("mandatory")
_A3filterUserGrpEntry_Object = MibTableRow
a3filterUserGrpEntry = _A3filterUserGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1)
)
a3filterUserGrpEntry.setIndexNames(
    (0, "A3COM-FILTER-R5-MIB", "a3filterUserGrpIndex"),
)
if mibBuilder.loadTexts:
    a3filterUserGrpEntry.setStatus("mandatory")


class _A3filterUserGrpIndex_Type(Integer32):
    """Custom type a3filterUserGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_A3filterUserGrpIndex_Type.__name__ = "Integer32"
_A3filterUserGrpIndex_Object = MibTableColumn
a3filterUserGrpIndex = _A3filterUserGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1, 1),
    _A3filterUserGrpIndex_Type()
)
a3filterUserGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterUserGrpIndex.setStatus("mandatory")


class _A3filterUserGrpName_Type(DisplayString):
    """Custom type a3filterUserGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_A3filterUserGrpName_Type.__name__ = "DisplayString"
_A3filterUserGrpName_Object = MibTableColumn
a3filterUserGrpName = _A3filterUserGrpName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1, 2),
    _A3filterUserGrpName_Type()
)
a3filterUserGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserGrpName.setStatus("mandatory")
_A3filterUserGrpStatus_Type = RowStatus
_A3filterUserGrpStatus_Object = MibTableColumn
a3filterUserGrpStatus = _A3filterUserGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 4, 1, 3),
    _A3filterUserGrpStatus_Type()
)
a3filterUserGrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserGrpStatus.setStatus("mandatory")
_A3filterUserGrpAddrTable_Object = MibTable
a3filterUserGrpAddrTable = _A3filterUserGrpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 5)
)
if mibBuilder.loadTexts:
    a3filterUserGrpAddrTable.setStatus("mandatory")
_A3filterUserGrpAddrEntry_Object = MibTableRow
a3filterUserGrpAddrEntry = _A3filterUserGrpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1)
)
a3filterUserGrpAddrEntry.setIndexNames(
    (0, "A3COM-FILTER-R5-MIB", "a3filterUserGrpAddrIndex"),
    (0, "A3COM-FILTER-R5-MIB", "a3filterUserGrpAddress"),
)
if mibBuilder.loadTexts:
    a3filterUserGrpAddrEntry.setStatus("mandatory")


class _A3filterUserGrpAddrIndex_Type(Integer32):
    """Custom type a3filterUserGrpAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_A3filterUserGrpAddrIndex_Type.__name__ = "Integer32"
_A3filterUserGrpAddrIndex_Object = MibTableColumn
a3filterUserGrpAddrIndex = _A3filterUserGrpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1, 1),
    _A3filterUserGrpAddrIndex_Type()
)
a3filterUserGrpAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterUserGrpAddrIndex.setStatus("mandatory")
_A3filterUserGrpAddress_Type = MacAddress
_A3filterUserGrpAddress_Object = MibTableColumn
a3filterUserGrpAddress = _A3filterUserGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1, 2),
    _A3filterUserGrpAddress_Type()
)
a3filterUserGrpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterUserGrpAddress.setStatus("mandatory")
_A3filterUserGrpAddrStatus_Type = RowStatus
_A3filterUserGrpAddrStatus_Object = MibTableColumn
a3filterUserGrpAddrStatus = _A3filterUserGrpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 5, 1, 3),
    _A3filterUserGrpAddrStatus_Type()
)
a3filterUserGrpAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterUserGrpAddrStatus.setStatus("mandatory")
_A3filterPolicyTable_Object = MibTable
a3filterPolicyTable = _A3filterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6)
)
if mibBuilder.loadTexts:
    a3filterPolicyTable.setStatus("mandatory")
_A3filterPolicyEntry_Object = MibTableRow
a3filterPolicyEntry = _A3filterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1)
)
a3filterPolicyEntry.setIndexNames(
    (0, "A3COM-FILTER-R5-MIB", "a3filterPolicyIndex"),
)
if mibBuilder.loadTexts:
    a3filterPolicyEntry.setStatus("mandatory")


class _A3filterPolicyIndex_Type(Integer32):
    """Custom type a3filterPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_A3filterPolicyIndex_Type.__name__ = "Integer32"
_A3filterPolicyIndex_Object = MibTableColumn
a3filterPolicyIndex = _A3filterPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 1),
    _A3filterPolicyIndex_Type()
)
a3filterPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterPolicyIndex.setStatus("mandatory")


class _A3filterPolicyName_Type(DisplayString):
    """Custom type a3filterPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_A3filterPolicyName_Type.__name__ = "DisplayString"
_A3filterPolicyName_Object = MibTableColumn
a3filterPolicyName = _A3filterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 2),
    _A3filterPolicyName_Type()
)
a3filterPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyName.setStatus("mandatory")


class _A3filterPolicyAction_Type(Integer32):
    """Custom type a3filterPolicyAction based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("count", 3),
          ("discard", 1),
          ("doddiscard", 8),
          ("forward", 2),
          ("prioritizeHigh", 5),
          ("prioritizeLow", 7),
          ("prioritizeMed", 6),
          ("sequence", 4),
          ("x25ProfId", 9))
    )


_A3filterPolicyAction_Type.__name__ = "Integer32"
_A3filterPolicyAction_Object = MibTableColumn
a3filterPolicyAction = _A3filterPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 3),
    _A3filterPolicyAction_Type()
)
a3filterPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyAction.setStatus("mandatory")
_A3filterPolicyMask1_Type = Integer32
_A3filterPolicyMask1_Object = MibTableColumn
a3filterPolicyMask1 = _A3filterPolicyMask1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 4),
    _A3filterPolicyMask1_Type()
)
a3filterPolicyMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyMask1.setStatus("mandatory")
_A3filterPolicyMask2_Type = Integer32
_A3filterPolicyMask2_Object = MibTableColumn
a3filterPolicyMask2 = _A3filterPolicyMask2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 5),
    _A3filterPolicyMask2_Type()
)
a3filterPolicyMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyMask2.setStatus("mandatory")
_A3filterPolicyMask3_Type = Integer32
_A3filterPolicyMask3_Object = MibTableColumn
a3filterPolicyMask3 = _A3filterPolicyMask3_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 6),
    _A3filterPolicyMask3_Type()
)
a3filterPolicyMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyMask3.setStatus("mandatory")
_A3filterPolicyMask4_Type = Integer32
_A3filterPolicyMask4_Object = MibTableColumn
a3filterPolicyMask4 = _A3filterPolicyMask4_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 7),
    _A3filterPolicyMask4_Type()
)
a3filterPolicyMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyMask4.setStatus("mandatory")


class _A3filterPolicyContext_Type(Integer32):
    """Custom type a3filterPolicyContext based on Integer32"""
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
        *(("all", 1),
          ("amongPorts1", 7),
          ("atPorts1", 2),
          ("betweenPorts1AndPorts2", 6),
          ("fromPorts1", 3),
          ("fromPorts1ToPorts2", 4),
          ("toPorts1", 5))
    )


_A3filterPolicyContext_Type.__name__ = "Integer32"
_A3filterPolicyContext_Object = MibTableColumn
a3filterPolicyContext = _A3filterPolicyContext_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 8),
    _A3filterPolicyContext_Type()
)
a3filterPolicyContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyContext.setStatus("mandatory")
_A3filterPolicyPorts1_Type = OctetString
_A3filterPolicyPorts1_Object = MibTableColumn
a3filterPolicyPorts1 = _A3filterPolicyPorts1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 9),
    _A3filterPolicyPorts1_Type()
)
a3filterPolicyPorts1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyPorts1.setStatus("mandatory")
_A3filterPolicyPorts2_Type = OctetString
_A3filterPolicyPorts2_Object = MibTableColumn
a3filterPolicyPorts2 = _A3filterPolicyPorts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 10),
    _A3filterPolicyPorts2_Type()
)
a3filterPolicyPorts2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyPorts2.setStatus("mandatory")
_A3filterPolicyPackets_Type = Counter32
_A3filterPolicyPackets_Object = MibTableColumn
a3filterPolicyPackets = _A3filterPolicyPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 11),
    _A3filterPolicyPackets_Type()
)
a3filterPolicyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterPolicyPackets.setStatus("mandatory")
_A3filterPolicyBytes_Type = Counter32
_A3filterPolicyBytes_Object = MibTableColumn
a3filterPolicyBytes = _A3filterPolicyBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 12),
    _A3filterPolicyBytes_Type()
)
a3filterPolicyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3filterPolicyBytes.setStatus("mandatory")
_A3filterPolicyStatus_Type = RowStatus
_A3filterPolicyStatus_Object = MibTableColumn
a3filterPolicyStatus = _A3filterPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 13),
    _A3filterPolicyStatus_Type()
)
a3filterPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyStatus.setStatus("mandatory")
_A3filterPolicyX25ProfId_Type = Integer32
_A3filterPolicyX25ProfId_Object = MibTableColumn
a3filterPolicyX25ProfId = _A3filterPolicyX25ProfId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 10, 6, 1, 14),
    _A3filterPolicyX25ProfId_Type()
)
a3filterPolicyX25ProfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3filterPolicyX25ProfId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-FILTER-R5-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComFilter": a3ComFilter,
       "a3ComFilterCtl": a3ComFilterCtl,
       "a3filterControl": a3filterControl,
       "a3filterDefaultAction": a3filterDefaultAction,
       "a3filterBridgeSelect": a3filterBridgeSelect,
       "a3filterIpSelect": a3filterIpSelect,
       "a3filterIpxSelect": a3filterIpxSelect,
       "a3filterAppleTalkSelect": a3filterAppleTalkSelect,
       "a3filterDecSelect": a3filterDecSelect,
       "a3filterUserMaskTable": a3filterUserMaskTable,
       "a3filterUserMaskEntry": a3filterUserMaskEntry,
       "a3filterUserMaskIndex": a3filterUserMaskIndex,
       "a3filterUserMaskName": a3filterUserMaskName,
       "a3filterUserMaskLocType": a3filterUserMaskLocType,
       "a3filterUserMaskLocField": a3filterUserMaskLocField,
       "a3filterUserMaskLocOffset": a3filterUserMaskLocOffset,
       "a3filterUserMaskLocLength": a3filterUserMaskLocLength,
       "a3filterUserMaskOperator": a3filterUserMaskOperator,
       "a3filterUserMaskOperand": a3filterUserMaskOperand,
       "a3filterUserMaskComparison": a3filterUserMaskComparison,
       "a3filterUserMaskMatchType": a3filterUserMaskMatchType,
       "a3filterUserMaskMatchBits": a3filterUserMaskMatchBits,
       "a3filterUserMaskMatchValue1": a3filterUserMaskMatchValue1,
       "a3filterUserMaskMatchValue2": a3filterUserMaskMatchValue2,
       "a3filterUserMaskStatus": a3filterUserMaskStatus,
       "a3filterBuiltInMaskTable": a3filterBuiltInMaskTable,
       "a3filterBuiltInMaskEntry": a3filterBuiltInMaskEntry,
       "a3filterBuiltInMaskIndex": a3filterBuiltInMaskIndex,
       "a3filterBuiltInMaskName": a3filterBuiltInMaskName,
       "a3filterBuiltInMaskFieldValue": a3filterBuiltInMaskFieldValue,
       "a3filterUserGrpTable": a3filterUserGrpTable,
       "a3filterUserGrpEntry": a3filterUserGrpEntry,
       "a3filterUserGrpIndex": a3filterUserGrpIndex,
       "a3filterUserGrpName": a3filterUserGrpName,
       "a3filterUserGrpStatus": a3filterUserGrpStatus,
       "a3filterUserGrpAddrTable": a3filterUserGrpAddrTable,
       "a3filterUserGrpAddrEntry": a3filterUserGrpAddrEntry,
       "a3filterUserGrpAddrIndex": a3filterUserGrpAddrIndex,
       "a3filterUserGrpAddress": a3filterUserGrpAddress,
       "a3filterUserGrpAddrStatus": a3filterUserGrpAddrStatus,
       "a3filterPolicyTable": a3filterPolicyTable,
       "a3filterPolicyEntry": a3filterPolicyEntry,
       "a3filterPolicyIndex": a3filterPolicyIndex,
       "a3filterPolicyName": a3filterPolicyName,
       "a3filterPolicyAction": a3filterPolicyAction,
       "a3filterPolicyMask1": a3filterPolicyMask1,
       "a3filterPolicyMask2": a3filterPolicyMask2,
       "a3filterPolicyMask3": a3filterPolicyMask3,
       "a3filterPolicyMask4": a3filterPolicyMask4,
       "a3filterPolicyContext": a3filterPolicyContext,
       "a3filterPolicyPorts1": a3filterPolicyPorts1,
       "a3filterPolicyPorts2": a3filterPolicyPorts2,
       "a3filterPolicyPackets": a3filterPolicyPackets,
       "a3filterPolicyBytes": a3filterPolicyBytes,
       "a3filterPolicyStatus": a3filterPolicyStatus,
       "a3filterPolicyX25ProfId": a3filterPolicyX25ProfId}
)
