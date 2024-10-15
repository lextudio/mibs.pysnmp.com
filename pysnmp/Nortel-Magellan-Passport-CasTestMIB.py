# SNMP MIB module (Nortel-Magellan-Passport-CasTestMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-CasTestMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:30 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 TimeInterval,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TimeInterval",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DashedHexString,
 DigitString,
 EnterpriseDateAndTime,
 ExtendedAsciiString,
 FixedPoint1,
 FixedPoint2,
 FixedPoint3,
 FixedPoint4,
 Gauge64,
 Hex,
 HexString,
 IntegerSequence,
 Link,
 NonReplicated,
 Unsigned64,
 WildcardedDigitString) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "DigitString",
    "EnterpriseDateAndTime",
    "ExtendedAsciiString",
    "FixedPoint1",
    "FixedPoint2",
    "FixedPoint3",
    "FixedPoint4",
    "Gauge64",
    "Hex",
    "HexString",
    "IntegerSequence",
    "Link",
    "NonReplicated",
    "Unsigned64",
    "WildcardedDigitString")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Example_ObjectIdentity = ObjectIdentity
example = _Example_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000)
)
_ExampleRowStatusTable_Object = MibTable
exampleRowStatusTable = _ExampleRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1)
)
if mibBuilder.loadTexts:
    exampleRowStatusTable.setStatus("mandatory")
_ExampleRowStatusEntry_Object = MibTableRow
exampleRowStatusEntry = _ExampleRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1, 1)
)
exampleRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
)
if mibBuilder.loadTexts:
    exampleRowStatusEntry.setStatus("mandatory")
_ExampleRowStatus_Type = RowStatus
_ExampleRowStatus_Object = MibTableColumn
exampleRowStatus = _ExampleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1, 1, 1),
    _ExampleRowStatus_Type()
)
exampleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleRowStatus.setStatus("mandatory")
_ExampleComponentName_Type = DisplayString
_ExampleComponentName_Object = MibTableColumn
exampleComponentName = _ExampleComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1, 1, 2),
    _ExampleComponentName_Type()
)
exampleComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleComponentName.setStatus("mandatory")
_ExampleStorageType_Type = StorageType
_ExampleStorageType_Object = MibTableColumn
exampleStorageType = _ExampleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1, 1, 4),
    _ExampleStorageType_Type()
)
exampleStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleStorageType.setStatus("mandatory")
_ExampleIndex_Type = NonReplicated
_ExampleIndex_Object = MibTableColumn
exampleIndex = _ExampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1, 1, 10),
    _ExampleIndex_Type()
)
exampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIndex.setStatus("mandatory")
_ExampleDecimal_ObjectIdentity = ObjectIdentity
exampleDecimal = _ExampleDecimal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2)
)
_ExampleDecimalRowStatusTable_Object = MibTable
exampleDecimalRowStatusTable = _ExampleDecimalRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1)
)
if mibBuilder.loadTexts:
    exampleDecimalRowStatusTable.setStatus("mandatory")
_ExampleDecimalRowStatusEntry_Object = MibTableRow
exampleDecimalRowStatusEntry = _ExampleDecimalRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1, 1)
)
exampleDecimalRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalRowStatusEntry.setStatus("mandatory")
_ExampleDecimalRowStatus_Type = RowStatus
_ExampleDecimalRowStatus_Object = MibTableColumn
exampleDecimalRowStatus = _ExampleDecimalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1, 1, 1),
    _ExampleDecimalRowStatus_Type()
)
exampleDecimalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalRowStatus.setStatus("mandatory")
_ExampleDecimalComponentName_Type = DisplayString
_ExampleDecimalComponentName_Object = MibTableColumn
exampleDecimalComponentName = _ExampleDecimalComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1, 1, 2),
    _ExampleDecimalComponentName_Type()
)
exampleDecimalComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDecimalComponentName.setStatus("mandatory")
_ExampleDecimalStorageType_Type = StorageType
_ExampleDecimalStorageType_Object = MibTableColumn
exampleDecimalStorageType = _ExampleDecimalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1, 1, 4),
    _ExampleDecimalStorageType_Type()
)
exampleDecimalStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDecimalStorageType.setStatus("mandatory")


class _ExampleDecimalIndex_Type(Integer32):
    """Custom type exampleDecimalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ExampleDecimalIndex_Type.__name__ = "Integer32"
_ExampleDecimalIndex_Object = MibTableColumn
exampleDecimalIndex = _ExampleDecimalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1, 1, 10),
    _ExampleDecimalIndex_Type()
)
exampleDecimalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalIndex.setStatus("mandatory")
_ExampleDecimalOperationalTable_Object = MibTable
exampleDecimalOperationalTable = _ExampleDecimalOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10)
)
if mibBuilder.loadTexts:
    exampleDecimalOperationalTable.setStatus("mandatory")
_ExampleDecimalOperationalEntry_Object = MibTableRow
exampleDecimalOperationalEntry = _ExampleDecimalOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1)
)
exampleDecimalOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalOperationalEntry.setStatus("mandatory")


class _ExampleDecimalOperStructInteger_Type(Unsigned32):
    """Custom type exampleDecimalOperStructInteger based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDecimalOperStructInteger_Type.__name__ = "Unsigned32"
_ExampleDecimalOperStructInteger_Object = MibTableColumn
exampleDecimalOperStructInteger = _ExampleDecimalOperStructInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 1),
    _ExampleDecimalOperStructInteger_Type()
)
exampleDecimalOperStructInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOperStructInteger.setStatus("mandatory")


class _ExampleDecimalOperStructIntSet_Type(OctetString):
    """Custom type exampleDecimalOperStructIntSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExampleDecimalOperStructIntSet_Type.__name__ = "OctetString"
_ExampleDecimalOperStructIntSet_Object = MibTableColumn
exampleDecimalOperStructIntSet = _ExampleDecimalOperStructIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 2),
    _ExampleDecimalOperStructIntSet_Type()
)
exampleDecimalOperStructIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOperStructIntSet.setStatus("mandatory")


class _ExampleDecimalOperFreeInteger_Type(Unsigned32):
    """Custom type exampleDecimalOperFreeInteger based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(100, 200),
    )


_ExampleDecimalOperFreeInteger_Type.__name__ = "Unsigned32"
_ExampleDecimalOperFreeInteger_Object = MibTableColumn
exampleDecimalOperFreeInteger = _ExampleDecimalOperFreeInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 3),
    _ExampleDecimalOperFreeInteger_Type()
)
exampleDecimalOperFreeInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOperFreeInteger.setStatus("mandatory")


class _ExampleDecimalOperFreeIntSet_Type(OctetString):
    """Custom type exampleDecimalOperFreeIntSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExampleDecimalOperFreeIntSet_Type.__name__ = "OctetString"
_ExampleDecimalOperFreeIntSet_Object = MibTableColumn
exampleDecimalOperFreeIntSet = _ExampleDecimalOperFreeIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 4),
    _ExampleDecimalOperFreeIntSet_Type()
)
exampleDecimalOperFreeIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOperFreeIntSet.setStatus("mandatory")
_ExampleDecimalOperFreeCounter32_Type = Counter32
_ExampleDecimalOperFreeCounter32_Object = MibTableColumn
exampleDecimalOperFreeCounter32 = _ExampleDecimalOperFreeCounter32_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 5),
    _ExampleDecimalOperFreeCounter32_Type()
)
exampleDecimalOperFreeCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDecimalOperFreeCounter32.setStatus("mandatory")


class _ExampleDecimalOperFreeGauge32_Type(Gauge32):
    """Custom type exampleDecimalOperFreeGauge32 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExampleDecimalOperFreeGauge32_Type.__name__ = "Gauge32"
_ExampleDecimalOperFreeGauge32_Object = MibTableColumn
exampleDecimalOperFreeGauge32 = _ExampleDecimalOperFreeGauge32_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 6),
    _ExampleDecimalOperFreeGauge32_Type()
)
exampleDecimalOperFreeGauge32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOperFreeGauge32.setStatus("mandatory")


class _ExampleDecimalOperFreeTimeInterval_Type(TimeInterval):
    """Custom type exampleDecimalOperFreeTimeInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ExampleDecimalOperFreeTimeInterval_Type.__name__ = "TimeInterval"
_ExampleDecimalOperFreeTimeInterval_Object = MibTableColumn
exampleDecimalOperFreeTimeInterval = _ExampleDecimalOperFreeTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 10, 1, 7),
    _ExampleDecimalOperFreeTimeInterval_Type()
)
exampleDecimalOperFreeTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOperFreeTimeInterval.setStatus("mandatory")
_ExampleDecimalProvisionalTable_Object = MibTable
exampleDecimalProvisionalTable = _ExampleDecimalProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11)
)
if mibBuilder.loadTexts:
    exampleDecimalProvisionalTable.setStatus("mandatory")
_ExampleDecimalProvisionalEntry_Object = MibTableRow
exampleDecimalProvisionalEntry = _ExampleDecimalProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1)
)
exampleDecimalProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalProvisionalEntry.setStatus("mandatory")
_ExampleDecimalProvDecimalSub_Type = Link
_ExampleDecimalProvDecimalSub_Object = MibTableColumn
exampleDecimalProvDecimalSub = _ExampleDecimalProvDecimalSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 1),
    _ExampleDecimalProvDecimalSub_Type()
)
exampleDecimalProvDecimalSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvDecimalSub.setStatus("mandatory")


class _ExampleDecimalProvStructInteger_Type(Unsigned32):
    """Custom type exampleDecimalProvStructInteger based on Unsigned32"""
    defaultValue = 253

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
        ValueRangeConstraint(253, 253),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )


_ExampleDecimalProvStructInteger_Type.__name__ = "Unsigned32"
_ExampleDecimalProvStructInteger_Object = MibTableColumn
exampleDecimalProvStructInteger = _ExampleDecimalProvStructInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 2),
    _ExampleDecimalProvStructInteger_Type()
)
exampleDecimalProvStructInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvStructInteger.setStatus("mandatory")


class _ExampleDecimalProvStructIntSet_Type(OctetString):
    """Custom type exampleDecimalProvStructIntSet based on OctetString"""
    defaultHexValue = "aaaa"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExampleDecimalProvStructIntSet_Type.__name__ = "OctetString"
_ExampleDecimalProvStructIntSet_Object = MibTableColumn
exampleDecimalProvStructIntSet = _ExampleDecimalProvStructIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 3),
    _ExampleDecimalProvStructIntSet_Type()
)
exampleDecimalProvStructIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvStructIntSet.setStatus("mandatory")


class _ExampleDecimalProvFreeInteger_Type(Unsigned32):
    """Custom type exampleDecimalProvFreeInteger based on Unsigned32"""
    defaultValue = 101

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(100, 200),
    )


_ExampleDecimalProvFreeInteger_Type.__name__ = "Unsigned32"
_ExampleDecimalProvFreeInteger_Object = MibTableColumn
exampleDecimalProvFreeInteger = _ExampleDecimalProvFreeInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 4),
    _ExampleDecimalProvFreeInteger_Type()
)
exampleDecimalProvFreeInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvFreeInteger.setStatus("mandatory")


class _ExampleDecimalProvFreeInteger1_Type(Unsigned32):
    """Custom type exampleDecimalProvFreeInteger1 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 200),
    )


_ExampleDecimalProvFreeInteger1_Type.__name__ = "Unsigned32"
_ExampleDecimalProvFreeInteger1_Object = MibTableColumn
exampleDecimalProvFreeInteger1 = _ExampleDecimalProvFreeInteger1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 5),
    _ExampleDecimalProvFreeInteger1_Type()
)
exampleDecimalProvFreeInteger1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvFreeInteger1.setStatus("mandatory")


class _ExampleDecimalProvFreeInteger2_Type(Unsigned32):
    """Custom type exampleDecimalProvFreeInteger2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExampleDecimalProvFreeInteger2_Type.__name__ = "Unsigned32"
_ExampleDecimalProvFreeInteger2_Object = MibTableColumn
exampleDecimalProvFreeInteger2 = _ExampleDecimalProvFreeInteger2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 6),
    _ExampleDecimalProvFreeInteger2_Type()
)
exampleDecimalProvFreeInteger2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvFreeInteger2.setStatus("mandatory")


class _ExampleDecimalProvFreeIntSet_Type(OctetString):
    """Custom type exampleDecimalProvFreeIntSet based on OctetString"""
    defaultHexValue = "5555"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExampleDecimalProvFreeIntSet_Type.__name__ = "OctetString"
_ExampleDecimalProvFreeIntSet_Object = MibTableColumn
exampleDecimalProvFreeIntSet = _ExampleDecimalProvFreeIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 7),
    _ExampleDecimalProvFreeIntSet_Type()
)
exampleDecimalProvFreeIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvFreeIntSet.setStatus("mandatory")


class _ExampleDecimalProvFreeIntSet1_Type(OctetString):
    """Custom type exampleDecimalProvFreeIntSet1 based on OctetString"""
    defaultHexValue = "80000001"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ExampleDecimalProvFreeIntSet1_Type.__name__ = "OctetString"
_ExampleDecimalProvFreeIntSet1_Object = MibTableColumn
exampleDecimalProvFreeIntSet1 = _ExampleDecimalProvFreeIntSet1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 11, 1, 8),
    _ExampleDecimalProvFreeIntSet1_Type()
)
exampleDecimalProvFreeIntSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalProvFreeIntSet1.setStatus("mandatory")
_ExampleDecimalOsIntVectorTable_Object = MibTable
exampleDecimalOsIntVectorTable = _ExampleDecimalOsIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1012)
)
if mibBuilder.loadTexts:
    exampleDecimalOsIntVectorTable.setStatus("mandatory")
_ExampleDecimalOsIntVectorEntry_Object = MibTableRow
exampleDecimalOsIntVectorEntry = _ExampleDecimalOsIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1012, 1)
)
exampleDecimalOsIntVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOsIntVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalOsIntVectorEntry.setStatus("mandatory")


class _ExampleDecimalOsIntVectorIndex_Type(Integer32):
    """Custom type exampleDecimalOsIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDecimalOsIntVectorIndex_Type.__name__ = "Integer32"
_ExampleDecimalOsIntVectorIndex_Object = MibTableColumn
exampleDecimalOsIntVectorIndex = _ExampleDecimalOsIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1012, 1, 1),
    _ExampleDecimalOsIntVectorIndex_Type()
)
exampleDecimalOsIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOsIntVectorIndex.setStatus("mandatory")


class _ExampleDecimalOsIntVectorValue_Type(Unsigned32):
    """Custom type exampleDecimalOsIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExampleDecimalOsIntVectorValue_Type.__name__ = "Unsigned32"
_ExampleDecimalOsIntVectorValue_Object = MibTableColumn
exampleDecimalOsIntVectorValue = _ExampleDecimalOsIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1012, 1, 2),
    _ExampleDecimalOsIntVectorValue_Type()
)
exampleDecimalOsIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOsIntVectorValue.setStatus("mandatory")
_ExampleDecimalOsIntArrayTable_Object = MibTable
exampleDecimalOsIntArrayTable = _ExampleDecimalOsIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1013)
)
if mibBuilder.loadTexts:
    exampleDecimalOsIntArrayTable.setStatus("mandatory")
_ExampleDecimalOsIntArrayEntry_Object = MibTableRow
exampleDecimalOsIntArrayEntry = _ExampleDecimalOsIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1013, 1)
)
exampleDecimalOsIntArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOsIntArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOsIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalOsIntArrayEntry.setStatus("mandatory")


class _ExampleDecimalOsIntArrayRowIndex_Type(Integer32):
    """Custom type exampleDecimalOsIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDecimalOsIntArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDecimalOsIntArrayRowIndex_Object = MibTableColumn
exampleDecimalOsIntArrayRowIndex = _ExampleDecimalOsIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1013, 1, 1),
    _ExampleDecimalOsIntArrayRowIndex_Type()
)
exampleDecimalOsIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOsIntArrayRowIndex.setStatus("mandatory")


class _ExampleDecimalOsIntArrayColumnIndex_Type(Integer32):
    """Custom type exampleDecimalOsIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDecimalOsIntArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDecimalOsIntArrayColumnIndex_Object = MibTableColumn
exampleDecimalOsIntArrayColumnIndex = _ExampleDecimalOsIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1013, 1, 2),
    _ExampleDecimalOsIntArrayColumnIndex_Type()
)
exampleDecimalOsIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOsIntArrayColumnIndex.setStatus("mandatory")


class _ExampleDecimalOsIntArrayValue_Type(Unsigned32):
    """Custom type exampleDecimalOsIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDecimalOsIntArrayValue_Type.__name__ = "Unsigned32"
_ExampleDecimalOsIntArrayValue_Object = MibTableColumn
exampleDecimalOsIntArrayValue = _ExampleDecimalOsIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1013, 1, 3),
    _ExampleDecimalOsIntArrayValue_Type()
)
exampleDecimalOsIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOsIntArrayValue.setStatus("mandatory")
_ExampleDecimalOfIntVectorTable_Object = MibTable
exampleDecimalOfIntVectorTable = _ExampleDecimalOfIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1014)
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntVectorTable.setStatus("mandatory")
_ExampleDecimalOfIntVectorEntry_Object = MibTableRow
exampleDecimalOfIntVectorEntry = _ExampleDecimalOfIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1014, 1)
)
exampleDecimalOfIntVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOfIntVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntVectorEntry.setStatus("mandatory")


class _ExampleDecimalOfIntVectorIndex_Type(Integer32):
    """Custom type exampleDecimalOfIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDecimalOfIntVectorIndex_Type.__name__ = "Integer32"
_ExampleDecimalOfIntVectorIndex_Object = MibTableColumn
exampleDecimalOfIntVectorIndex = _ExampleDecimalOfIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1014, 1, 1),
    _ExampleDecimalOfIntVectorIndex_Type()
)
exampleDecimalOfIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOfIntVectorIndex.setStatus("mandatory")


class _ExampleDecimalOfIntVectorValue_Type(Unsigned32):
    """Custom type exampleDecimalOfIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExampleDecimalOfIntVectorValue_Type.__name__ = "Unsigned32"
_ExampleDecimalOfIntVectorValue_Object = MibTableColumn
exampleDecimalOfIntVectorValue = _ExampleDecimalOfIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1014, 1, 2),
    _ExampleDecimalOfIntVectorValue_Type()
)
exampleDecimalOfIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOfIntVectorValue.setStatus("mandatory")
_ExampleDecimalOfIntArrayTable_Object = MibTable
exampleDecimalOfIntArrayTable = _ExampleDecimalOfIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1015)
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntArrayTable.setStatus("mandatory")
_ExampleDecimalOfIntArrayEntry_Object = MibTableRow
exampleDecimalOfIntArrayEntry = _ExampleDecimalOfIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1015, 1)
)
exampleDecimalOfIntArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOfIntArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOfIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntArrayEntry.setStatus("mandatory")


class _ExampleDecimalOfIntArrayRowIndex_Type(Integer32):
    """Custom type exampleDecimalOfIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDecimalOfIntArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDecimalOfIntArrayRowIndex_Object = MibTableColumn
exampleDecimalOfIntArrayRowIndex = _ExampleDecimalOfIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1015, 1, 1),
    _ExampleDecimalOfIntArrayRowIndex_Type()
)
exampleDecimalOfIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOfIntArrayRowIndex.setStatus("mandatory")


class _ExampleDecimalOfIntArrayColumnIndex_Type(Integer32):
    """Custom type exampleDecimalOfIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDecimalOfIntArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDecimalOfIntArrayColumnIndex_Object = MibTableColumn
exampleDecimalOfIntArrayColumnIndex = _ExampleDecimalOfIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1015, 1, 2),
    _ExampleDecimalOfIntArrayColumnIndex_Type()
)
exampleDecimalOfIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOfIntArrayColumnIndex.setStatus("mandatory")


class _ExampleDecimalOfIntArrayValue_Type(Unsigned32):
    """Custom type exampleDecimalOfIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDecimalOfIntArrayValue_Type.__name__ = "Unsigned32"
_ExampleDecimalOfIntArrayValue_Object = MibTableColumn
exampleDecimalOfIntArrayValue = _ExampleDecimalOfIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1015, 1, 3),
    _ExampleDecimalOfIntArrayValue_Type()
)
exampleDecimalOfIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOfIntArrayValue.setStatus("mandatory")
_ExampleDecimalOfIntReplicatedTable_Object = MibTable
exampleDecimalOfIntReplicatedTable = _ExampleDecimalOfIntReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1016)
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntReplicatedTable.setStatus("mandatory")
_ExampleDecimalOfIntReplicatedEntry_Object = MibTableRow
exampleDecimalOfIntReplicatedEntry = _ExampleDecimalOfIntReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1016, 1)
)
exampleDecimalOfIntReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOfIntReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntReplicatedEntry.setStatus("mandatory")


class _ExampleDecimalOfIntReplicatedIndex_Type(Integer32):
    """Custom type exampleDecimalOfIntReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDecimalOfIntReplicatedIndex_Type.__name__ = "Integer32"
_ExampleDecimalOfIntReplicatedIndex_Object = MibTableColumn
exampleDecimalOfIntReplicatedIndex = _ExampleDecimalOfIntReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1016, 1, 1),
    _ExampleDecimalOfIntReplicatedIndex_Type()
)
exampleDecimalOfIntReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalOfIntReplicatedIndex.setStatus("mandatory")


class _ExampleDecimalOfIntReplicatedValue_Type(Unsigned32):
    """Custom type exampleDecimalOfIntReplicatedValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExampleDecimalOfIntReplicatedValue_Type.__name__ = "Unsigned32"
_ExampleDecimalOfIntReplicatedValue_Object = MibTableColumn
exampleDecimalOfIntReplicatedValue = _ExampleDecimalOfIntReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1016, 1, 2),
    _ExampleDecimalOfIntReplicatedValue_Type()
)
exampleDecimalOfIntReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOfIntReplicatedValue.setStatus("mandatory")
_ExampleDecimalOfIntReplicatedRowStatus_Type = RowStatus
_ExampleDecimalOfIntReplicatedRowStatus_Object = MibTableColumn
exampleDecimalOfIntReplicatedRowStatus = _ExampleDecimalOfIntReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1016, 1, 3),
    _ExampleDecimalOfIntReplicatedRowStatus_Type()
)
exampleDecimalOfIntReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDecimalOfIntReplicatedRowStatus.setStatus("mandatory")
_ExampleDecimalOfIntListTable_Object = MibTable
exampleDecimalOfIntListTable = _ExampleDecimalOfIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1017)
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntListTable.setStatus("mandatory")
_ExampleDecimalOfIntListEntry_Object = MibTableRow
exampleDecimalOfIntListEntry = _ExampleDecimalOfIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1017, 1)
)
exampleDecimalOfIntListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalOfIntListValue"),
)
if mibBuilder.loadTexts:
    exampleDecimalOfIntListEntry.setStatus("mandatory")


class _ExampleDecimalOfIntListValue_Type(Integer32):
    """Custom type exampleDecimalOfIntListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(1000, 2000),
    )


_ExampleDecimalOfIntListValue_Type.__name__ = "Integer32"
_ExampleDecimalOfIntListValue_Object = MibTableColumn
exampleDecimalOfIntListValue = _ExampleDecimalOfIntListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1017, 1, 1),
    _ExampleDecimalOfIntListValue_Type()
)
exampleDecimalOfIntListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalOfIntListValue.setStatus("mandatory")
_ExampleDecimalOfIntListRowStatus_Type = RowStatus
_ExampleDecimalOfIntListRowStatus_Object = MibTableColumn
exampleDecimalOfIntListRowStatus = _ExampleDecimalOfIntListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1017, 1, 2),
    _ExampleDecimalOfIntListRowStatus_Type()
)
exampleDecimalOfIntListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDecimalOfIntListRowStatus.setStatus("mandatory")
_ExampleDecimalPsIntVectorTable_Object = MibTable
exampleDecimalPsIntVectorTable = _ExampleDecimalPsIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1018)
)
if mibBuilder.loadTexts:
    exampleDecimalPsIntVectorTable.setStatus("mandatory")
_ExampleDecimalPsIntVectorEntry_Object = MibTableRow
exampleDecimalPsIntVectorEntry = _ExampleDecimalPsIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1018, 1)
)
exampleDecimalPsIntVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPsIntVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalPsIntVectorEntry.setStatus("mandatory")


class _ExampleDecimalPsIntVectorIndex_Type(Integer32):
    """Custom type exampleDecimalPsIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDecimalPsIntVectorIndex_Type.__name__ = "Integer32"
_ExampleDecimalPsIntVectorIndex_Object = MibTableColumn
exampleDecimalPsIntVectorIndex = _ExampleDecimalPsIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1018, 1, 1),
    _ExampleDecimalPsIntVectorIndex_Type()
)
exampleDecimalPsIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPsIntVectorIndex.setStatus("mandatory")


class _ExampleDecimalPsIntVectorValue_Type(Unsigned32):
    """Custom type exampleDecimalPsIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExampleDecimalPsIntVectorValue_Type.__name__ = "Unsigned32"
_ExampleDecimalPsIntVectorValue_Object = MibTableColumn
exampleDecimalPsIntVectorValue = _ExampleDecimalPsIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1018, 1, 2),
    _ExampleDecimalPsIntVectorValue_Type()
)
exampleDecimalPsIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPsIntVectorValue.setStatus("mandatory")
_ExampleDecimalPsIntArrayTable_Object = MibTable
exampleDecimalPsIntArrayTable = _ExampleDecimalPsIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1019)
)
if mibBuilder.loadTexts:
    exampleDecimalPsIntArrayTable.setStatus("mandatory")
_ExampleDecimalPsIntArrayEntry_Object = MibTableRow
exampleDecimalPsIntArrayEntry = _ExampleDecimalPsIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1019, 1)
)
exampleDecimalPsIntArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPsIntArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPsIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalPsIntArrayEntry.setStatus("mandatory")


class _ExampleDecimalPsIntArrayRowIndex_Type(Integer32):
    """Custom type exampleDecimalPsIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDecimalPsIntArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDecimalPsIntArrayRowIndex_Object = MibTableColumn
exampleDecimalPsIntArrayRowIndex = _ExampleDecimalPsIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1019, 1, 1),
    _ExampleDecimalPsIntArrayRowIndex_Type()
)
exampleDecimalPsIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPsIntArrayRowIndex.setStatus("mandatory")


class _ExampleDecimalPsIntArrayColumnIndex_Type(Integer32):
    """Custom type exampleDecimalPsIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDecimalPsIntArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDecimalPsIntArrayColumnIndex_Object = MibTableColumn
exampleDecimalPsIntArrayColumnIndex = _ExampleDecimalPsIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1019, 1, 2),
    _ExampleDecimalPsIntArrayColumnIndex_Type()
)
exampleDecimalPsIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPsIntArrayColumnIndex.setStatus("mandatory")


class _ExampleDecimalPsIntArrayValue_Type(Unsigned32):
    """Custom type exampleDecimalPsIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDecimalPsIntArrayValue_Type.__name__ = "Unsigned32"
_ExampleDecimalPsIntArrayValue_Object = MibTableColumn
exampleDecimalPsIntArrayValue = _ExampleDecimalPsIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1019, 1, 3),
    _ExampleDecimalPsIntArrayValue_Type()
)
exampleDecimalPsIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPsIntArrayValue.setStatus("mandatory")
_ExampleDecimalPfIntVectorTable_Object = MibTable
exampleDecimalPfIntVectorTable = _ExampleDecimalPfIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1020)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntVectorTable.setStatus("mandatory")
_ExampleDecimalPfIntVectorEntry_Object = MibTableRow
exampleDecimalPfIntVectorEntry = _ExampleDecimalPfIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1020, 1)
)
exampleDecimalPfIntVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntVectorEntry.setStatus("mandatory")


class _ExampleDecimalPfIntVectorIndex_Type(Integer32):
    """Custom type exampleDecimalPfIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDecimalPfIntVectorIndex_Type.__name__ = "Integer32"
_ExampleDecimalPfIntVectorIndex_Object = MibTableColumn
exampleDecimalPfIntVectorIndex = _ExampleDecimalPfIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1020, 1, 1),
    _ExampleDecimalPfIntVectorIndex_Type()
)
exampleDecimalPfIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntVectorIndex.setStatus("mandatory")


class _ExampleDecimalPfIntVectorValue_Type(Unsigned32):
    """Custom type exampleDecimalPfIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExampleDecimalPfIntVectorValue_Type.__name__ = "Unsigned32"
_ExampleDecimalPfIntVectorValue_Object = MibTableColumn
exampleDecimalPfIntVectorValue = _ExampleDecimalPfIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1020, 1, 2),
    _ExampleDecimalPfIntVectorValue_Type()
)
exampleDecimalPfIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntVectorValue.setStatus("mandatory")
_ExampleDecimalPfIntVector1Table_Object = MibTable
exampleDecimalPfIntVector1Table = _ExampleDecimalPfIntVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1021)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntVector1Table.setStatus("mandatory")
_ExampleDecimalPfIntVector1Entry_Object = MibTableRow
exampleDecimalPfIntVector1Entry = _ExampleDecimalPfIntVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1021, 1)
)
exampleDecimalPfIntVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntVector1Index"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntVector1Entry.setStatus("mandatory")


class _ExampleDecimalPfIntVector1Index_Type(Integer32):
    """Custom type exampleDecimalPfIntVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExampleDecimalPfIntVector1Index_Type.__name__ = "Integer32"
_ExampleDecimalPfIntVector1Index_Object = MibTableColumn
exampleDecimalPfIntVector1Index = _ExampleDecimalPfIntVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1021, 1, 1),
    _ExampleDecimalPfIntVector1Index_Type()
)
exampleDecimalPfIntVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntVector1Index.setStatus("mandatory")


class _ExampleDecimalPfIntVector1Value_Type(Unsigned32):
    """Custom type exampleDecimalPfIntVector1Value based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
        ValueRangeConstraint(100, 150),
    )


_ExampleDecimalPfIntVector1Value_Type.__name__ = "Unsigned32"
_ExampleDecimalPfIntVector1Value_Object = MibTableColumn
exampleDecimalPfIntVector1Value = _ExampleDecimalPfIntVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1021, 1, 2),
    _ExampleDecimalPfIntVector1Value_Type()
)
exampleDecimalPfIntVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntVector1Value.setStatus("mandatory")
_ExampleDecimalPfIntArrayTable_Object = MibTable
exampleDecimalPfIntArrayTable = _ExampleDecimalPfIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1022)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntArrayTable.setStatus("mandatory")
_ExampleDecimalPfIntArrayEntry_Object = MibTableRow
exampleDecimalPfIntArrayEntry = _ExampleDecimalPfIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1022, 1)
)
exampleDecimalPfIntArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntArrayEntry.setStatus("mandatory")


class _ExampleDecimalPfIntArrayRowIndex_Type(Integer32):
    """Custom type exampleDecimalPfIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDecimalPfIntArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDecimalPfIntArrayRowIndex_Object = MibTableColumn
exampleDecimalPfIntArrayRowIndex = _ExampleDecimalPfIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1022, 1, 1),
    _ExampleDecimalPfIntArrayRowIndex_Type()
)
exampleDecimalPfIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntArrayRowIndex.setStatus("mandatory")


class _ExampleDecimalPfIntArrayColumnIndex_Type(Integer32):
    """Custom type exampleDecimalPfIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDecimalPfIntArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDecimalPfIntArrayColumnIndex_Object = MibTableColumn
exampleDecimalPfIntArrayColumnIndex = _ExampleDecimalPfIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1022, 1, 2),
    _ExampleDecimalPfIntArrayColumnIndex_Type()
)
exampleDecimalPfIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntArrayColumnIndex.setStatus("mandatory")


class _ExampleDecimalPfIntArrayValue_Type(Unsigned32):
    """Custom type exampleDecimalPfIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDecimalPfIntArrayValue_Type.__name__ = "Unsigned32"
_ExampleDecimalPfIntArrayValue_Object = MibTableColumn
exampleDecimalPfIntArrayValue = _ExampleDecimalPfIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1022, 1, 3),
    _ExampleDecimalPfIntArrayValue_Type()
)
exampleDecimalPfIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntArrayValue.setStatus("mandatory")
_ExampleDecimalPfIntArray1Table_Object = MibTable
exampleDecimalPfIntArray1Table = _ExampleDecimalPfIntArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1023)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntArray1Table.setStatus("mandatory")
_ExampleDecimalPfIntArray1Entry_Object = MibTableRow
exampleDecimalPfIntArray1Entry = _ExampleDecimalPfIntArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1023, 1)
)
exampleDecimalPfIntArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntArray1RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntArray1Entry.setStatus("mandatory")


class _ExampleDecimalPfIntArray1RowIndex_Type(Integer32):
    """Custom type exampleDecimalPfIntArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDecimalPfIntArray1RowIndex_Type.__name__ = "Integer32"
_ExampleDecimalPfIntArray1RowIndex_Object = MibTableColumn
exampleDecimalPfIntArray1RowIndex = _ExampleDecimalPfIntArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1023, 1, 1),
    _ExampleDecimalPfIntArray1RowIndex_Type()
)
exampleDecimalPfIntArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntArray1RowIndex.setStatus("mandatory")


class _ExampleDecimalPfIntArray1ColumnIndex_Type(Integer32):
    """Custom type exampleDecimalPfIntArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDecimalPfIntArray1ColumnIndex_Type.__name__ = "Integer32"
_ExampleDecimalPfIntArray1ColumnIndex_Object = MibTableColumn
exampleDecimalPfIntArray1ColumnIndex = _ExampleDecimalPfIntArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1023, 1, 2),
    _ExampleDecimalPfIntArray1ColumnIndex_Type()
)
exampleDecimalPfIntArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntArray1ColumnIndex.setStatus("mandatory")


class _ExampleDecimalPfIntArray1Value_Type(Unsigned32):
    """Custom type exampleDecimalPfIntArray1Value based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(20, 200),
    )


_ExampleDecimalPfIntArray1Value_Type.__name__ = "Unsigned32"
_ExampleDecimalPfIntArray1Value_Object = MibTableColumn
exampleDecimalPfIntArray1Value = _ExampleDecimalPfIntArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1023, 1, 3),
    _ExampleDecimalPfIntArray1Value_Type()
)
exampleDecimalPfIntArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntArray1Value.setStatus("mandatory")
_ExampleDecimalPfIntReplicatedTable_Object = MibTable
exampleDecimalPfIntReplicatedTable = _ExampleDecimalPfIntReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1024)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicatedTable.setStatus("mandatory")
_ExampleDecimalPfIntReplicatedEntry_Object = MibTableRow
exampleDecimalPfIntReplicatedEntry = _ExampleDecimalPfIntReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1024, 1)
)
exampleDecimalPfIntReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicatedEntry.setStatus("mandatory")


class _ExampleDecimalPfIntReplicatedIndex_Type(Integer32):
    """Custom type exampleDecimalPfIntReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDecimalPfIntReplicatedIndex_Type.__name__ = "Integer32"
_ExampleDecimalPfIntReplicatedIndex_Object = MibTableColumn
exampleDecimalPfIntReplicatedIndex = _ExampleDecimalPfIntReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1024, 1, 1),
    _ExampleDecimalPfIntReplicatedIndex_Type()
)
exampleDecimalPfIntReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicatedIndex.setStatus("mandatory")


class _ExampleDecimalPfIntReplicatedValue_Type(Unsigned32):
    """Custom type exampleDecimalPfIntReplicatedValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExampleDecimalPfIntReplicatedValue_Type.__name__ = "Unsigned32"
_ExampleDecimalPfIntReplicatedValue_Object = MibTableColumn
exampleDecimalPfIntReplicatedValue = _ExampleDecimalPfIntReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1024, 1, 2),
    _ExampleDecimalPfIntReplicatedValue_Type()
)
exampleDecimalPfIntReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicatedValue.setStatus("mandatory")
_ExampleDecimalPfIntReplicatedRowStatus_Type = RowStatus
_ExampleDecimalPfIntReplicatedRowStatus_Object = MibTableColumn
exampleDecimalPfIntReplicatedRowStatus = _ExampleDecimalPfIntReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1024, 1, 3),
    _ExampleDecimalPfIntReplicatedRowStatus_Type()
)
exampleDecimalPfIntReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicatedRowStatus.setStatus("mandatory")
_ExampleDecimalPfIntReplicated1Table_Object = MibTable
exampleDecimalPfIntReplicated1Table = _ExampleDecimalPfIntReplicated1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1025)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicated1Table.setStatus("mandatory")
_ExampleDecimalPfIntReplicated1Entry_Object = MibTableRow
exampleDecimalPfIntReplicated1Entry = _ExampleDecimalPfIntReplicated1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1025, 1)
)
exampleDecimalPfIntReplicated1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntReplicated1Index"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicated1Entry.setStatus("mandatory")


class _ExampleDecimalPfIntReplicated1Index_Type(Integer32):
    """Custom type exampleDecimalPfIntReplicated1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
        ValueRangeConstraint(11, 19),
    )


_ExampleDecimalPfIntReplicated1Index_Type.__name__ = "Integer32"
_ExampleDecimalPfIntReplicated1Index_Object = MibTableColumn
exampleDecimalPfIntReplicated1Index = _ExampleDecimalPfIntReplicated1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1025, 1, 1),
    _ExampleDecimalPfIntReplicated1Index_Type()
)
exampleDecimalPfIntReplicated1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicated1Index.setStatus("mandatory")


class _ExampleDecimalPfIntReplicated1Value_Type(Unsigned32):
    """Custom type exampleDecimalPfIntReplicated1Value based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(30, 300),
    )


_ExampleDecimalPfIntReplicated1Value_Type.__name__ = "Unsigned32"
_ExampleDecimalPfIntReplicated1Value_Object = MibTableColumn
exampleDecimalPfIntReplicated1Value = _ExampleDecimalPfIntReplicated1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1025, 1, 2),
    _ExampleDecimalPfIntReplicated1Value_Type()
)
exampleDecimalPfIntReplicated1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicated1Value.setStatus("mandatory")
_ExampleDecimalPfIntReplicated1RowStatus_Type = RowStatus
_ExampleDecimalPfIntReplicated1RowStatus_Object = MibTableColumn
exampleDecimalPfIntReplicated1RowStatus = _ExampleDecimalPfIntReplicated1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1025, 1, 3),
    _ExampleDecimalPfIntReplicated1RowStatus_Type()
)
exampleDecimalPfIntReplicated1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDecimalPfIntReplicated1RowStatus.setStatus("mandatory")
_ExampleDecimalPfIntListTable_Object = MibTable
exampleDecimalPfIntListTable = _ExampleDecimalPfIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1026)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntListTable.setStatus("mandatory")
_ExampleDecimalPfIntListEntry_Object = MibTableRow
exampleDecimalPfIntListEntry = _ExampleDecimalPfIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1026, 1)
)
exampleDecimalPfIntListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntListValue"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntListEntry.setStatus("mandatory")


class _ExampleDecimalPfIntListValue_Type(Integer32):
    """Custom type exampleDecimalPfIntListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ExampleDecimalPfIntListValue_Type.__name__ = "Integer32"
_ExampleDecimalPfIntListValue_Object = MibTableColumn
exampleDecimalPfIntListValue = _ExampleDecimalPfIntListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1026, 1, 1),
    _ExampleDecimalPfIntListValue_Type()
)
exampleDecimalPfIntListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntListValue.setStatus("mandatory")
_ExampleDecimalPfIntListRowStatus_Type = RowStatus
_ExampleDecimalPfIntListRowStatus_Object = MibTableColumn
exampleDecimalPfIntListRowStatus = _ExampleDecimalPfIntListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1026, 1, 2),
    _ExampleDecimalPfIntListRowStatus_Type()
)
exampleDecimalPfIntListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDecimalPfIntListRowStatus.setStatus("mandatory")
_ExampleDecimalPfIntList1Table_Object = MibTable
exampleDecimalPfIntList1Table = _ExampleDecimalPfIntList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1027)
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntList1Table.setStatus("mandatory")
_ExampleDecimalPfIntList1Entry_Object = MibTableRow
exampleDecimalPfIntList1Entry = _ExampleDecimalPfIntList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1027, 1)
)
exampleDecimalPfIntList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalPfIntList1Value"),
)
if mibBuilder.loadTexts:
    exampleDecimalPfIntList1Entry.setStatus("mandatory")


class _ExampleDecimalPfIntList1Value_Type(Integer32):
    """Custom type exampleDecimalPfIntList1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(15, 50),
    )


_ExampleDecimalPfIntList1Value_Type.__name__ = "Integer32"
_ExampleDecimalPfIntList1Value_Object = MibTableColumn
exampleDecimalPfIntList1Value = _ExampleDecimalPfIntList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1027, 1, 1),
    _ExampleDecimalPfIntList1Value_Type()
)
exampleDecimalPfIntList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalPfIntList1Value.setStatus("mandatory")
_ExampleDecimalPfIntList1RowStatus_Type = RowStatus
_ExampleDecimalPfIntList1RowStatus_Object = MibTableColumn
exampleDecimalPfIntList1RowStatus = _ExampleDecimalPfIntList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 2, 1027, 1, 2),
    _ExampleDecimalPfIntList1RowStatus_Type()
)
exampleDecimalPfIntList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDecimalPfIntList1RowStatus.setStatus("mandatory")
_ExampleHex_ObjectIdentity = ObjectIdentity
exampleHex = _ExampleHex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3)
)
_ExampleHexRowStatusTable_Object = MibTable
exampleHexRowStatusTable = _ExampleHexRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1)
)
if mibBuilder.loadTexts:
    exampleHexRowStatusTable.setStatus("mandatory")
_ExampleHexRowStatusEntry_Object = MibTableRow
exampleHexRowStatusEntry = _ExampleHexRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1, 1)
)
exampleHexRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
)
if mibBuilder.loadTexts:
    exampleHexRowStatusEntry.setStatus("mandatory")
_ExampleHexRowStatus_Type = RowStatus
_ExampleHexRowStatus_Object = MibTableColumn
exampleHexRowStatus = _ExampleHexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1, 1, 1),
    _ExampleHexRowStatus_Type()
)
exampleHexRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexRowStatus.setStatus("mandatory")
_ExampleHexComponentName_Type = DisplayString
_ExampleHexComponentName_Object = MibTableColumn
exampleHexComponentName = _ExampleHexComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1, 1, 2),
    _ExampleHexComponentName_Type()
)
exampleHexComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHexComponentName.setStatus("mandatory")
_ExampleHexStorageType_Type = StorageType
_ExampleHexStorageType_Object = MibTableColumn
exampleHexStorageType = _ExampleHexStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1, 1, 4),
    _ExampleHexStorageType_Type()
)
exampleHexStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHexStorageType.setStatus("mandatory")


class _ExampleHexIndex_Type(Integer32):
    """Custom type exampleHexIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexIndex_Type.__name__ = "Integer32"
_ExampleHexIndex_Object = MibTableColumn
exampleHexIndex = _ExampleHexIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1, 1, 10),
    _ExampleHexIndex_Type()
)
exampleHexIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexIndex.setStatus("mandatory")
_ExampleHexOperationalTable_Object = MibTable
exampleHexOperationalTable = _ExampleHexOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 10)
)
if mibBuilder.loadTexts:
    exampleHexOperationalTable.setStatus("mandatory")
_ExampleHexOperationalEntry_Object = MibTableRow
exampleHexOperationalEntry = _ExampleHexOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 10, 1)
)
exampleHexOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
)
if mibBuilder.loadTexts:
    exampleHexOperationalEntry.setStatus("mandatory")


class _ExampleHexOperStructHex_Type(Hex):
    """Custom type exampleHexOperStructHex based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexOperStructHex_Type.__name__ = "Hex"
_ExampleHexOperStructHex_Object = MibTableColumn
exampleHexOperStructHex = _ExampleHexOperStructHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 10, 1, 1),
    _ExampleHexOperStructHex_Type()
)
exampleHexOperStructHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOperStructHex.setStatus("mandatory")


class _ExampleHexOperFreeHex_Type(Hex):
    """Custom type exampleHexOperFreeHex based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexOperFreeHex_Type.__name__ = "Hex"
_ExampleHexOperFreeHex_Object = MibTableColumn
exampleHexOperFreeHex = _ExampleHexOperFreeHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 10, 1, 2),
    _ExampleHexOperFreeHex_Type()
)
exampleHexOperFreeHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOperFreeHex.setStatus("mandatory")
_ExampleHexProvisionalTable_Object = MibTable
exampleHexProvisionalTable = _ExampleHexProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 11)
)
if mibBuilder.loadTexts:
    exampleHexProvisionalTable.setStatus("mandatory")
_ExampleHexProvisionalEntry_Object = MibTableRow
exampleHexProvisionalEntry = _ExampleHexProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 11, 1)
)
exampleHexProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvisionalEntry.setStatus("mandatory")
_ExampleHexProvEnumSub_Type = Link
_ExampleHexProvEnumSub_Object = MibTableColumn
exampleHexProvEnumSub = _ExampleHexProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 11, 1, 1),
    _ExampleHexProvEnumSub_Type()
)
exampleHexProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvEnumSub.setStatus("mandatory")


class _ExampleHexProvStructHex_Type(Hex):
    """Custom type exampleHexProvStructHex based on Hex"""
    defaultValue = 512

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(513, 513),
        ValueRangeConstraint(514, 514),
    )


_ExampleHexProvStructHex_Type.__name__ = "Hex"
_ExampleHexProvStructHex_Object = MibTableColumn
exampleHexProvStructHex = _ExampleHexProvStructHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 11, 1, 2),
    _ExampleHexProvStructHex_Type()
)
exampleHexProvStructHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvStructHex.setStatus("mandatory")


class _ExampleHexProvFreeHex_Type(Hex):
    """Custom type exampleHexProvFreeHex based on Hex"""
    defaultValue = 18

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexProvFreeHex_Type.__name__ = "Hex"
_ExampleHexProvFreeHex_Object = MibTableColumn
exampleHexProvFreeHex = _ExampleHexProvFreeHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 11, 1, 3),
    _ExampleHexProvFreeHex_Type()
)
exampleHexProvFreeHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHex.setStatus("mandatory")


class _ExampleHexProvFreeHex1_Type(Hex):
    """Custom type exampleHexProvFreeHex1 based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(256, 4096),
    )


_ExampleHexProvFreeHex1_Type.__name__ = "Hex"
_ExampleHexProvFreeHex1_Object = MibTableColumn
exampleHexProvFreeHex1 = _ExampleHexProvFreeHex1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 11, 1, 4),
    _ExampleHexProvFreeHex1_Type()
)
exampleHexProvFreeHex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHex1.setStatus("mandatory")
_ExampleHexOsHexVectorTable_Object = MibTable
exampleHexOsHexVectorTable = _ExampleHexOsHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1040)
)
if mibBuilder.loadTexts:
    exampleHexOsHexVectorTable.setStatus("mandatory")
_ExampleHexOsHexVectorEntry_Object = MibTableRow
exampleHexOsHexVectorEntry = _ExampleHexOsHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1040, 1)
)
exampleHexOsHexVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOsHexVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleHexOsHexVectorEntry.setStatus("mandatory")


class _ExampleHexOsHexVectorIndex_Type(Integer32):
    """Custom type exampleHexOsHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexOsHexVectorIndex_Type.__name__ = "Integer32"
_ExampleHexOsHexVectorIndex_Object = MibTableColumn
exampleHexOsHexVectorIndex = _ExampleHexOsHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1040, 1, 1),
    _ExampleHexOsHexVectorIndex_Type()
)
exampleHexOsHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOsHexVectorIndex.setStatus("mandatory")


class _ExampleHexOsHexVectorValue_Type(Hex):
    """Custom type exampleHexOsHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexOsHexVectorValue_Type.__name__ = "Hex"
_ExampleHexOsHexVectorValue_Object = MibTableColumn
exampleHexOsHexVectorValue = _ExampleHexOsHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1040, 1, 2),
    _ExampleHexOsHexVectorValue_Type()
)
exampleHexOsHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOsHexVectorValue.setStatus("mandatory")
_ExampleHexOsHexArrayTable_Object = MibTable
exampleHexOsHexArrayTable = _ExampleHexOsHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1041)
)
if mibBuilder.loadTexts:
    exampleHexOsHexArrayTable.setStatus("mandatory")
_ExampleHexOsHexArrayEntry_Object = MibTableRow
exampleHexOsHexArrayEntry = _ExampleHexOsHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1041, 1)
)
exampleHexOsHexArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOsHexArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOsHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleHexOsHexArrayEntry.setStatus("mandatory")


class _ExampleHexOsHexArrayRowIndex_Type(Integer32):
    """Custom type exampleHexOsHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleHexOsHexArrayRowIndex_Type.__name__ = "Integer32"
_ExampleHexOsHexArrayRowIndex_Object = MibTableColumn
exampleHexOsHexArrayRowIndex = _ExampleHexOsHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1041, 1, 1),
    _ExampleHexOsHexArrayRowIndex_Type()
)
exampleHexOsHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOsHexArrayRowIndex.setStatus("mandatory")


class _ExampleHexOsHexArrayColumnIndex_Type(Integer32):
    """Custom type exampleHexOsHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexOsHexArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleHexOsHexArrayColumnIndex_Object = MibTableColumn
exampleHexOsHexArrayColumnIndex = _ExampleHexOsHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1041, 1, 2),
    _ExampleHexOsHexArrayColumnIndex_Type()
)
exampleHexOsHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOsHexArrayColumnIndex.setStatus("mandatory")


class _ExampleHexOsHexArrayValue_Type(Hex):
    """Custom type exampleHexOsHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexOsHexArrayValue_Type.__name__ = "Hex"
_ExampleHexOsHexArrayValue_Object = MibTableColumn
exampleHexOsHexArrayValue = _ExampleHexOsHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1041, 1, 3),
    _ExampleHexOsHexArrayValue_Type()
)
exampleHexOsHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOsHexArrayValue.setStatus("mandatory")
_ExampleHexOfHexVectorTable_Object = MibTable
exampleHexOfHexVectorTable = _ExampleHexOfHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1042)
)
if mibBuilder.loadTexts:
    exampleHexOfHexVectorTable.setStatus("mandatory")
_ExampleHexOfHexVectorEntry_Object = MibTableRow
exampleHexOfHexVectorEntry = _ExampleHexOfHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1042, 1)
)
exampleHexOfHexVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOfHexVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleHexOfHexVectorEntry.setStatus("mandatory")


class _ExampleHexOfHexVectorIndex_Type(Integer32):
    """Custom type exampleHexOfHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexOfHexVectorIndex_Type.__name__ = "Integer32"
_ExampleHexOfHexVectorIndex_Object = MibTableColumn
exampleHexOfHexVectorIndex = _ExampleHexOfHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1042, 1, 1),
    _ExampleHexOfHexVectorIndex_Type()
)
exampleHexOfHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOfHexVectorIndex.setStatus("mandatory")


class _ExampleHexOfHexVectorValue_Type(Hex):
    """Custom type exampleHexOfHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexOfHexVectorValue_Type.__name__ = "Hex"
_ExampleHexOfHexVectorValue_Object = MibTableColumn
exampleHexOfHexVectorValue = _ExampleHexOfHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1042, 1, 2),
    _ExampleHexOfHexVectorValue_Type()
)
exampleHexOfHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOfHexVectorValue.setStatus("mandatory")
_ExampleHexOfHexArrayTable_Object = MibTable
exampleHexOfHexArrayTable = _ExampleHexOfHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1043)
)
if mibBuilder.loadTexts:
    exampleHexOfHexArrayTable.setStatus("mandatory")
_ExampleHexOfHexArrayEntry_Object = MibTableRow
exampleHexOfHexArrayEntry = _ExampleHexOfHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1043, 1)
)
exampleHexOfHexArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOfHexArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOfHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleHexOfHexArrayEntry.setStatus("mandatory")


class _ExampleHexOfHexArrayRowIndex_Type(Integer32):
    """Custom type exampleHexOfHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleHexOfHexArrayRowIndex_Type.__name__ = "Integer32"
_ExampleHexOfHexArrayRowIndex_Object = MibTableColumn
exampleHexOfHexArrayRowIndex = _ExampleHexOfHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1043, 1, 1),
    _ExampleHexOfHexArrayRowIndex_Type()
)
exampleHexOfHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOfHexArrayRowIndex.setStatus("mandatory")


class _ExampleHexOfHexArrayColumnIndex_Type(Integer32):
    """Custom type exampleHexOfHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexOfHexArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleHexOfHexArrayColumnIndex_Object = MibTableColumn
exampleHexOfHexArrayColumnIndex = _ExampleHexOfHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1043, 1, 2),
    _ExampleHexOfHexArrayColumnIndex_Type()
)
exampleHexOfHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOfHexArrayColumnIndex.setStatus("mandatory")


class _ExampleHexOfHexArrayValue_Type(Hex):
    """Custom type exampleHexOfHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexOfHexArrayValue_Type.__name__ = "Hex"
_ExampleHexOfHexArrayValue_Object = MibTableColumn
exampleHexOfHexArrayValue = _ExampleHexOfHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1043, 1, 3),
    _ExampleHexOfHexArrayValue_Type()
)
exampleHexOfHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOfHexArrayValue.setStatus("mandatory")
_ExampleHexOfHexReplicatedTable_Object = MibTable
exampleHexOfHexReplicatedTable = _ExampleHexOfHexReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1044)
)
if mibBuilder.loadTexts:
    exampleHexOfHexReplicatedTable.setStatus("mandatory")
_ExampleHexOfHexReplicatedEntry_Object = MibTableRow
exampleHexOfHexReplicatedEntry = _ExampleHexOfHexReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1044, 1)
)
exampleHexOfHexReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOfHexReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleHexOfHexReplicatedEntry.setStatus("mandatory")


class _ExampleHexOfHexReplicatedIndex_Type(Integer32):
    """Custom type exampleHexOfHexReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexOfHexReplicatedIndex_Type.__name__ = "Integer32"
_ExampleHexOfHexReplicatedIndex_Object = MibTableColumn
exampleHexOfHexReplicatedIndex = _ExampleHexOfHexReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1044, 1, 1),
    _ExampleHexOfHexReplicatedIndex_Type()
)
exampleHexOfHexReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexOfHexReplicatedIndex.setStatus("mandatory")


class _ExampleHexOfHexReplicatedValue_Type(Hex):
    """Custom type exampleHexOfHexReplicatedValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexOfHexReplicatedValue_Type.__name__ = "Hex"
_ExampleHexOfHexReplicatedValue_Object = MibTableColumn
exampleHexOfHexReplicatedValue = _ExampleHexOfHexReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1044, 1, 2),
    _ExampleHexOfHexReplicatedValue_Type()
)
exampleHexOfHexReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOfHexReplicatedValue.setStatus("mandatory")
_ExampleHexOfHexReplicatedRowStatus_Type = RowStatus
_ExampleHexOfHexReplicatedRowStatus_Object = MibTableColumn
exampleHexOfHexReplicatedRowStatus = _ExampleHexOfHexReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1044, 1, 3),
    _ExampleHexOfHexReplicatedRowStatus_Type()
)
exampleHexOfHexReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleHexOfHexReplicatedRowStatus.setStatus("mandatory")
_ExampleHexOfHexListTable_Object = MibTable
exampleHexOfHexListTable = _ExampleHexOfHexListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1045)
)
if mibBuilder.loadTexts:
    exampleHexOfHexListTable.setStatus("mandatory")
_ExampleHexOfHexListEntry_Object = MibTableRow
exampleHexOfHexListEntry = _ExampleHexOfHexListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1045, 1)
)
exampleHexOfHexListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexOfHexListValue"),
)
if mibBuilder.loadTexts:
    exampleHexOfHexListEntry.setStatus("mandatory")


class _ExampleHexOfHexListValue_Type(Integer32):
    """Custom type exampleHexOfHexListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ExampleHexOfHexListValue_Type.__name__ = "Integer32"
_ExampleHexOfHexListValue_Object = MibTableColumn
exampleHexOfHexListValue = _ExampleHexOfHexListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1045, 1, 1),
    _ExampleHexOfHexListValue_Type()
)
exampleHexOfHexListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexOfHexListValue.setStatus("mandatory")
_ExampleHexOfHexListRowStatus_Type = RowStatus
_ExampleHexOfHexListRowStatus_Object = MibTableColumn
exampleHexOfHexListRowStatus = _ExampleHexOfHexListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1045, 1, 2),
    _ExampleHexOfHexListRowStatus_Type()
)
exampleHexOfHexListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleHexOfHexListRowStatus.setStatus("mandatory")
_ExampleHexProvStructHexVectorTable_Object = MibTable
exampleHexProvStructHexVectorTable = _ExampleHexProvStructHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1046)
)
if mibBuilder.loadTexts:
    exampleHexProvStructHexVectorTable.setStatus("mandatory")
_ExampleHexProvStructHexVectorEntry_Object = MibTableRow
exampleHexProvStructHexVectorEntry = _ExampleHexProvStructHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1046, 1)
)
exampleHexProvStructHexVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvStructHexVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvStructHexVectorEntry.setStatus("mandatory")


class _ExampleHexProvStructHexVectorIndex_Type(Integer32):
    """Custom type exampleHexProvStructHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexProvStructHexVectorIndex_Type.__name__ = "Integer32"
_ExampleHexProvStructHexVectorIndex_Object = MibTableColumn
exampleHexProvStructHexVectorIndex = _ExampleHexProvStructHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1046, 1, 1),
    _ExampleHexProvStructHexVectorIndex_Type()
)
exampleHexProvStructHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvStructHexVectorIndex.setStatus("mandatory")


class _ExampleHexProvStructHexVectorValue_Type(Hex):
    """Custom type exampleHexProvStructHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexProvStructHexVectorValue_Type.__name__ = "Hex"
_ExampleHexProvStructHexVectorValue_Object = MibTableColumn
exampleHexProvStructHexVectorValue = _ExampleHexProvStructHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1046, 1, 2),
    _ExampleHexProvStructHexVectorValue_Type()
)
exampleHexProvStructHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvStructHexVectorValue.setStatus("mandatory")
_ExampleHexProvStructHexArrayTable_Object = MibTable
exampleHexProvStructHexArrayTable = _ExampleHexProvStructHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1047)
)
if mibBuilder.loadTexts:
    exampleHexProvStructHexArrayTable.setStatus("mandatory")
_ExampleHexProvStructHexArrayEntry_Object = MibTableRow
exampleHexProvStructHexArrayEntry = _ExampleHexProvStructHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1047, 1)
)
exampleHexProvStructHexArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvStructHexArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvStructHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvStructHexArrayEntry.setStatus("mandatory")


class _ExampleHexProvStructHexArrayRowIndex_Type(Integer32):
    """Custom type exampleHexProvStructHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleHexProvStructHexArrayRowIndex_Type.__name__ = "Integer32"
_ExampleHexProvStructHexArrayRowIndex_Object = MibTableColumn
exampleHexProvStructHexArrayRowIndex = _ExampleHexProvStructHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1047, 1, 1),
    _ExampleHexProvStructHexArrayRowIndex_Type()
)
exampleHexProvStructHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvStructHexArrayRowIndex.setStatus("mandatory")


class _ExampleHexProvStructHexArrayColumnIndex_Type(Integer32):
    """Custom type exampleHexProvStructHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexProvStructHexArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleHexProvStructHexArrayColumnIndex_Object = MibTableColumn
exampleHexProvStructHexArrayColumnIndex = _ExampleHexProvStructHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1047, 1, 2),
    _ExampleHexProvStructHexArrayColumnIndex_Type()
)
exampleHexProvStructHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvStructHexArrayColumnIndex.setStatus("mandatory")


class _ExampleHexProvStructHexArrayValue_Type(Hex):
    """Custom type exampleHexProvStructHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexProvStructHexArrayValue_Type.__name__ = "Hex"
_ExampleHexProvStructHexArrayValue_Object = MibTableColumn
exampleHexProvStructHexArrayValue = _ExampleHexProvStructHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1047, 1, 3),
    _ExampleHexProvStructHexArrayValue_Type()
)
exampleHexProvStructHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvStructHexArrayValue.setStatus("mandatory")
_ExampleHexProvFreeHexVectorTable_Object = MibTable
exampleHexProvFreeHexVectorTable = _ExampleHexProvFreeHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1048)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVectorTable.setStatus("mandatory")
_ExampleHexProvFreeHexVectorEntry_Object = MibTableRow
exampleHexProvFreeHexVectorEntry = _ExampleHexProvFreeHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1048, 1)
)
exampleHexProvFreeHexVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVectorEntry.setStatus("mandatory")


class _ExampleHexProvFreeHexVectorIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexProvFreeHexVectorIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexVectorIndex_Object = MibTableColumn
exampleHexProvFreeHexVectorIndex = _ExampleHexProvFreeHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1048, 1, 1),
    _ExampleHexProvFreeHexVectorIndex_Type()
)
exampleHexProvFreeHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVectorIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexVectorValue_Type(Hex):
    """Custom type exampleHexProvFreeHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexProvFreeHexVectorValue_Type.__name__ = "Hex"
_ExampleHexProvFreeHexVectorValue_Object = MibTableColumn
exampleHexProvFreeHexVectorValue = _ExampleHexProvFreeHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1048, 1, 2),
    _ExampleHexProvFreeHexVectorValue_Type()
)
exampleHexProvFreeHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVectorValue.setStatus("mandatory")
_ExampleHexProvFreeHexVector1Table_Object = MibTable
exampleHexProvFreeHexVector1Table = _ExampleHexProvFreeHexVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1049)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector1Table.setStatus("mandatory")
_ExampleHexProvFreeHexVector1Entry_Object = MibTableRow
exampleHexProvFreeHexVector1Entry = _ExampleHexProvFreeHexVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1049, 1)
)
exampleHexProvFreeHexVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexVector1Index"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector1Entry.setStatus("mandatory")


class _ExampleHexProvFreeHexVector1Index_Type(Integer32):
    """Custom type exampleHexProvFreeHexVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexProvFreeHexVector1Index_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexVector1Index_Object = MibTableColumn
exampleHexProvFreeHexVector1Index = _ExampleHexProvFreeHexVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1049, 1, 1),
    _ExampleHexProvFreeHexVector1Index_Type()
)
exampleHexProvFreeHexVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector1Index.setStatus("mandatory")


class _ExampleHexProvFreeHexVector1Value_Type(Hex):
    """Custom type exampleHexProvFreeHexVector1Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(256, 4096),
    )


_ExampleHexProvFreeHexVector1Value_Type.__name__ = "Hex"
_ExampleHexProvFreeHexVector1Value_Object = MibTableColumn
exampleHexProvFreeHexVector1Value = _ExampleHexProvFreeHexVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1049, 1, 2),
    _ExampleHexProvFreeHexVector1Value_Type()
)
exampleHexProvFreeHexVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector1Value.setStatus("mandatory")
_ExampleHexProvFreeHexVector2Table_Object = MibTable
exampleHexProvFreeHexVector2Table = _ExampleHexProvFreeHexVector2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1050)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector2Table.setStatus("mandatory")
_ExampleHexProvFreeHexVector2Entry_Object = MibTableRow
exampleHexProvFreeHexVector2Entry = _ExampleHexProvFreeHexVector2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1050, 1)
)
exampleHexProvFreeHexVector2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexVector2Index"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector2Entry.setStatus("mandatory")


class _ExampleHexProvFreeHexVector2Index_Type(Integer32):
    """Custom type exampleHexProvFreeHexVector2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ExampleHexProvFreeHexVector2Index_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexVector2Index_Object = MibTableColumn
exampleHexProvFreeHexVector2Index = _ExampleHexProvFreeHexVector2Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1050, 1, 1),
    _ExampleHexProvFreeHexVector2Index_Type()
)
exampleHexProvFreeHexVector2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector2Index.setStatus("mandatory")


class _ExampleHexProvFreeHexVector2Value_Type(Hex):
    """Custom type exampleHexProvFreeHexVector2Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(256, 4096),
    )


_ExampleHexProvFreeHexVector2Value_Type.__name__ = "Hex"
_ExampleHexProvFreeHexVector2Value_Object = MibTableColumn
exampleHexProvFreeHexVector2Value = _ExampleHexProvFreeHexVector2Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1050, 1, 2),
    _ExampleHexProvFreeHexVector2Value_Type()
)
exampleHexProvFreeHexVector2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexVector2Value.setStatus("mandatory")
_ExampleHexProvFreeHexArrayTable_Object = MibTable
exampleHexProvFreeHexArrayTable = _ExampleHexProvFreeHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1051)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArrayTable.setStatus("mandatory")
_ExampleHexProvFreeHexArrayEntry_Object = MibTableRow
exampleHexProvFreeHexArrayEntry = _ExampleHexProvFreeHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1051, 1)
)
exampleHexProvFreeHexArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArrayEntry.setStatus("mandatory")


class _ExampleHexProvFreeHexArrayRowIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleHexProvFreeHexArrayRowIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexArrayRowIndex_Object = MibTableColumn
exampleHexProvFreeHexArrayRowIndex = _ExampleHexProvFreeHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1051, 1, 1),
    _ExampleHexProvFreeHexArrayRowIndex_Type()
)
exampleHexProvFreeHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArrayRowIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexArrayColumnIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexProvFreeHexArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexArrayColumnIndex_Object = MibTableColumn
exampleHexProvFreeHexArrayColumnIndex = _ExampleHexProvFreeHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1051, 1, 2),
    _ExampleHexProvFreeHexArrayColumnIndex_Type()
)
exampleHexProvFreeHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArrayColumnIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexArrayValue_Type(Hex):
    """Custom type exampleHexProvFreeHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexProvFreeHexArrayValue_Type.__name__ = "Hex"
_ExampleHexProvFreeHexArrayValue_Object = MibTableColumn
exampleHexProvFreeHexArrayValue = _ExampleHexProvFreeHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1051, 1, 3),
    _ExampleHexProvFreeHexArrayValue_Type()
)
exampleHexProvFreeHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArrayValue.setStatus("mandatory")
_ExampleHexProvFreeHexArray1Table_Object = MibTable
exampleHexProvFreeHexArray1Table = _ExampleHexProvFreeHexArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1052)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray1Table.setStatus("mandatory")
_ExampleHexProvFreeHexArray1Entry_Object = MibTableRow
exampleHexProvFreeHexArray1Entry = _ExampleHexProvFreeHexArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1052, 1)
)
exampleHexProvFreeHexArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexArray1RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray1Entry.setStatus("mandatory")


class _ExampleHexProvFreeHexArray1RowIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(3, 4),
    )


_ExampleHexProvFreeHexArray1RowIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexArray1RowIndex_Object = MibTableColumn
exampleHexProvFreeHexArray1RowIndex = _ExampleHexProvFreeHexArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1052, 1, 1),
    _ExampleHexProvFreeHexArray1RowIndex_Type()
)
exampleHexProvFreeHexArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray1RowIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexArray1ColumnIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexProvFreeHexArray1ColumnIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexArray1ColumnIndex_Object = MibTableColumn
exampleHexProvFreeHexArray1ColumnIndex = _ExampleHexProvFreeHexArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1052, 1, 2),
    _ExampleHexProvFreeHexArray1ColumnIndex_Type()
)
exampleHexProvFreeHexArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray1ColumnIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexArray1Value_Type(Hex):
    """Custom type exampleHexProvFreeHexArray1Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(80, 256),
    )


_ExampleHexProvFreeHexArray1Value_Type.__name__ = "Hex"
_ExampleHexProvFreeHexArray1Value_Object = MibTableColumn
exampleHexProvFreeHexArray1Value = _ExampleHexProvFreeHexArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1052, 1, 3),
    _ExampleHexProvFreeHexArray1Value_Type()
)
exampleHexProvFreeHexArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray1Value.setStatus("mandatory")
_ExampleHexProvFreeHexArray2Table_Object = MibTable
exampleHexProvFreeHexArray2Table = _ExampleHexProvFreeHexArray2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1053)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray2Table.setStatus("mandatory")
_ExampleHexProvFreeHexArray2Entry_Object = MibTableRow
exampleHexProvFreeHexArray2Entry = _ExampleHexProvFreeHexArray2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1053, 1)
)
exampleHexProvFreeHexArray2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexArray2RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexArray2ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray2Entry.setStatus("mandatory")


class _ExampleHexProvFreeHexArray2RowIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexArray2RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexProvFreeHexArray2RowIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexArray2RowIndex_Object = MibTableColumn
exampleHexProvFreeHexArray2RowIndex = _ExampleHexProvFreeHexArray2RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1053, 1, 1),
    _ExampleHexProvFreeHexArray2RowIndex_Type()
)
exampleHexProvFreeHexArray2RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray2RowIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexArray2ColumnIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexArray2ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleHexProvFreeHexArray2ColumnIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexArray2ColumnIndex_Object = MibTableColumn
exampleHexProvFreeHexArray2ColumnIndex = _ExampleHexProvFreeHexArray2ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1053, 1, 2),
    _ExampleHexProvFreeHexArray2ColumnIndex_Type()
)
exampleHexProvFreeHexArray2ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray2ColumnIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexArray2Value_Type(Hex):
    """Custom type exampleHexProvFreeHexArray2Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(80, 256),
    )


_ExampleHexProvFreeHexArray2Value_Type.__name__ = "Hex"
_ExampleHexProvFreeHexArray2Value_Object = MibTableColumn
exampleHexProvFreeHexArray2Value = _ExampleHexProvFreeHexArray2Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1053, 1, 3),
    _ExampleHexProvFreeHexArray2Value_Type()
)
exampleHexProvFreeHexArray2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexArray2Value.setStatus("mandatory")
_ExampleHexProvFreeHexReplicatedTable_Object = MibTable
exampleHexProvFreeHexReplicatedTable = _ExampleHexProvFreeHexReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1054)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicatedTable.setStatus("mandatory")
_ExampleHexProvFreeHexReplicatedEntry_Object = MibTableRow
exampleHexProvFreeHexReplicatedEntry = _ExampleHexProvFreeHexReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1054, 1)
)
exampleHexProvFreeHexReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicatedEntry.setStatus("mandatory")


class _ExampleHexProvFreeHexReplicatedIndex_Type(Integer32):
    """Custom type exampleHexProvFreeHexReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleHexProvFreeHexReplicatedIndex_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexReplicatedIndex_Object = MibTableColumn
exampleHexProvFreeHexReplicatedIndex = _ExampleHexProvFreeHexReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1054, 1, 1),
    _ExampleHexProvFreeHexReplicatedIndex_Type()
)
exampleHexProvFreeHexReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicatedIndex.setStatus("mandatory")


class _ExampleHexProvFreeHexReplicatedValue_Type(Hex):
    """Custom type exampleHexProvFreeHexReplicatedValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ExampleHexProvFreeHexReplicatedValue_Type.__name__ = "Hex"
_ExampleHexProvFreeHexReplicatedValue_Object = MibTableColumn
exampleHexProvFreeHexReplicatedValue = _ExampleHexProvFreeHexReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1054, 1, 2),
    _ExampleHexProvFreeHexReplicatedValue_Type()
)
exampleHexProvFreeHexReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicatedValue.setStatus("mandatory")
_ExampleHexProvFreeHexReplicatedRowStatus_Type = RowStatus
_ExampleHexProvFreeHexReplicatedRowStatus_Object = MibTableColumn
exampleHexProvFreeHexReplicatedRowStatus = _ExampleHexProvFreeHexReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1054, 1, 3),
    _ExampleHexProvFreeHexReplicatedRowStatus_Type()
)
exampleHexProvFreeHexReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicatedRowStatus.setStatus("mandatory")
_ExampleHexProvFreeHexReplicated1Table_Object = MibTable
exampleHexProvFreeHexReplicated1Table = _ExampleHexProvFreeHexReplicated1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1055)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicated1Table.setStatus("mandatory")
_ExampleHexProvFreeHexReplicated1Entry_Object = MibTableRow
exampleHexProvFreeHexReplicated1Entry = _ExampleHexProvFreeHexReplicated1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1055, 1)
)
exampleHexProvFreeHexReplicated1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexReplicated1Index"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicated1Entry.setStatus("mandatory")


class _ExampleHexProvFreeHexReplicated1Index_Type(Integer32):
    """Custom type exampleHexProvFreeHexReplicated1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(5, 9),
    )


_ExampleHexProvFreeHexReplicated1Index_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexReplicated1Index_Object = MibTableColumn
exampleHexProvFreeHexReplicated1Index = _ExampleHexProvFreeHexReplicated1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1055, 1, 1),
    _ExampleHexProvFreeHexReplicated1Index_Type()
)
exampleHexProvFreeHexReplicated1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicated1Index.setStatus("mandatory")


class _ExampleHexProvFreeHexReplicated1Value_Type(Hex):
    """Custom type exampleHexProvFreeHexReplicated1Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
        ValueRangeConstraint(80, 256),
    )


_ExampleHexProvFreeHexReplicated1Value_Type.__name__ = "Hex"
_ExampleHexProvFreeHexReplicated1Value_Object = MibTableColumn
exampleHexProvFreeHexReplicated1Value = _ExampleHexProvFreeHexReplicated1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1055, 1, 2),
    _ExampleHexProvFreeHexReplicated1Value_Type()
)
exampleHexProvFreeHexReplicated1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicated1Value.setStatus("mandatory")
_ExampleHexProvFreeHexReplicated1RowStatus_Type = RowStatus
_ExampleHexProvFreeHexReplicated1RowStatus_Object = MibTableColumn
exampleHexProvFreeHexReplicated1RowStatus = _ExampleHexProvFreeHexReplicated1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1055, 1, 3),
    _ExampleHexProvFreeHexReplicated1RowStatus_Type()
)
exampleHexProvFreeHexReplicated1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexReplicated1RowStatus.setStatus("mandatory")
_ExampleHexProvFreeHexListTable_Object = MibTable
exampleHexProvFreeHexListTable = _ExampleHexProvFreeHexListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1056)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexListTable.setStatus("mandatory")
_ExampleHexProvFreeHexListEntry_Object = MibTableRow
exampleHexProvFreeHexListEntry = _ExampleHexProvFreeHexListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1056, 1)
)
exampleHexProvFreeHexListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexListValue"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexListEntry.setStatus("mandatory")


class _ExampleHexProvFreeHexListValue_Type(Integer32):
    """Custom type exampleHexProvFreeHexListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ExampleHexProvFreeHexListValue_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexListValue_Object = MibTableColumn
exampleHexProvFreeHexListValue = _ExampleHexProvFreeHexListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1056, 1, 1),
    _ExampleHexProvFreeHexListValue_Type()
)
exampleHexProvFreeHexListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexListValue.setStatus("mandatory")
_ExampleHexProvFreeHexListRowStatus_Type = RowStatus
_ExampleHexProvFreeHexListRowStatus_Object = MibTableColumn
exampleHexProvFreeHexListRowStatus = _ExampleHexProvFreeHexListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1056, 1, 2),
    _ExampleHexProvFreeHexListRowStatus_Type()
)
exampleHexProvFreeHexListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexListRowStatus.setStatus("mandatory")
_ExampleHexProvFreeHexList1Table_Object = MibTable
exampleHexProvFreeHexList1Table = _ExampleHexProvFreeHexList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1057)
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexList1Table.setStatus("mandatory")
_ExampleHexProvFreeHexList1Entry_Object = MibTableRow
exampleHexProvFreeHexList1Entry = _ExampleHexProvFreeHexList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1057, 1)
)
exampleHexProvFreeHexList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexProvFreeHexList1Value"),
)
if mibBuilder.loadTexts:
    exampleHexProvFreeHexList1Entry.setStatus("mandatory")


class _ExampleHexProvFreeHexList1Value_Type(Integer32):
    """Custom type exampleHexProvFreeHexList1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ExampleHexProvFreeHexList1Value_Type.__name__ = "Integer32"
_ExampleHexProvFreeHexList1Value_Object = MibTableColumn
exampleHexProvFreeHexList1Value = _ExampleHexProvFreeHexList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1057, 1, 1),
    _ExampleHexProvFreeHexList1Value_Type()
)
exampleHexProvFreeHexList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexList1Value.setStatus("mandatory")
_ExampleHexProvFreeHexList1RowStatus_Type = RowStatus
_ExampleHexProvFreeHexList1RowStatus_Object = MibTableColumn
exampleHexProvFreeHexList1RowStatus = _ExampleHexProvFreeHexList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 3, 1057, 1, 2),
    _ExampleHexProvFreeHexList1RowStatus_Type()
)
exampleHexProvFreeHexList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleHexProvFreeHexList1RowStatus.setStatus("mandatory")
_ExampleIpAddress_ObjectIdentity = ObjectIdentity
exampleIpAddress = _ExampleIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4)
)
_ExampleIpAddressRowStatusTable_Object = MibTable
exampleIpAddressRowStatusTable = _ExampleIpAddressRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1)
)
if mibBuilder.loadTexts:
    exampleIpAddressRowStatusTable.setStatus("mandatory")
_ExampleIpAddressRowStatusEntry_Object = MibTableRow
exampleIpAddressRowStatusEntry = _ExampleIpAddressRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1, 1)
)
exampleIpAddressRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressRowStatusEntry.setStatus("mandatory")
_ExampleIpAddressRowStatus_Type = RowStatus
_ExampleIpAddressRowStatus_Object = MibTableColumn
exampleIpAddressRowStatus = _ExampleIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1, 1, 1),
    _ExampleIpAddressRowStatus_Type()
)
exampleIpAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressRowStatus.setStatus("mandatory")
_ExampleIpAddressComponentName_Type = DisplayString
_ExampleIpAddressComponentName_Object = MibTableColumn
exampleIpAddressComponentName = _ExampleIpAddressComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1, 1, 2),
    _ExampleIpAddressComponentName_Type()
)
exampleIpAddressComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleIpAddressComponentName.setStatus("mandatory")
_ExampleIpAddressStorageType_Type = StorageType
_ExampleIpAddressStorageType_Object = MibTableColumn
exampleIpAddressStorageType = _ExampleIpAddressStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1, 1, 4),
    _ExampleIpAddressStorageType_Type()
)
exampleIpAddressStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleIpAddressStorageType.setStatus("mandatory")
_ExampleIpAddressIndex_Type = IpAddress
_ExampleIpAddressIndex_Object = MibTableColumn
exampleIpAddressIndex = _ExampleIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1, 1, 10),
    _ExampleIpAddressIndex_Type()
)
exampleIpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressIndex.setStatus("mandatory")
_ExampleIpAddressOperationalTable_Object = MibTable
exampleIpAddressOperationalTable = _ExampleIpAddressOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 10)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperationalTable.setStatus("mandatory")
_ExampleIpAddressOperationalEntry_Object = MibTableRow
exampleIpAddressOperationalEntry = _ExampleIpAddressOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 10, 1)
)
exampleIpAddressOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperationalEntry.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddress_Type = IpAddress
_ExampleIpAddressOperStructIpAddress_Object = MibTableColumn
exampleIpAddressOperStructIpAddress = _ExampleIpAddressOperStructIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 10, 1, 1),
    _ExampleIpAddressOperStructIpAddress_Type()
)
exampleIpAddressOperStructIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddress.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddress_Type = IpAddress
_ExampleIpAddressOperFreeIpAddress_Object = MibTableColumn
exampleIpAddressOperFreeIpAddress = _ExampleIpAddressOperFreeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 10, 1, 2),
    _ExampleIpAddressOperFreeIpAddress_Type()
)
exampleIpAddressOperFreeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddress.setStatus("mandatory")
_ExampleIpAddressProvisionalTable_Object = MibTable
exampleIpAddressProvisionalTable = _ExampleIpAddressProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 11)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvisionalTable.setStatus("mandatory")
_ExampleIpAddressProvisionalEntry_Object = MibTableRow
exampleIpAddressProvisionalEntry = _ExampleIpAddressProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 11, 1)
)
exampleIpAddressProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvisionalEntry.setStatus("mandatory")
_ExampleIpAddressProvEnumSub_Type = Link
_ExampleIpAddressProvEnumSub_Object = MibTableColumn
exampleIpAddressProvEnumSub = _ExampleIpAddressProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 11, 1, 1),
    _ExampleIpAddressProvEnumSub_Type()
)
exampleIpAddressProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvEnumSub.setStatus("mandatory")


class _ExampleIpAddressProvStructIpAddress_Type(IpAddress):
    """Custom type exampleIpAddressProvStructIpAddress based on IpAddress"""
    defaultHexValue = "7f000100"


_ExampleIpAddressProvStructIpAddress_Object = MibTableColumn
exampleIpAddressProvStructIpAddress = _ExampleIpAddressProvStructIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 11, 1, 2),
    _ExampleIpAddressProvStructIpAddress_Type()
)
exampleIpAddressProvStructIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddress.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddress_Type(IpAddress):
    """Custom type exampleIpAddressProvFreeIpAddress based on IpAddress"""
    defaultHexValue = "7f7f7f7f"


_ExampleIpAddressProvFreeIpAddress_Object = MibTableColumn
exampleIpAddressProvFreeIpAddress = _ExampleIpAddressProvFreeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 11, 1, 3),
    _ExampleIpAddressProvFreeIpAddress_Type()
)
exampleIpAddressProvFreeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddress.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddress1_Type = IpAddress
_ExampleIpAddressProvFreeIpAddress1_Object = MibTableColumn
exampleIpAddressProvFreeIpAddress1 = _ExampleIpAddressProvFreeIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 11, 1, 4),
    _ExampleIpAddressProvFreeIpAddress1_Type()
)
exampleIpAddressProvFreeIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddress1.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddressVectorTable_Object = MibTable
exampleIpAddressOperStructIpAddressVectorTable = _ExampleIpAddressOperStructIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1058)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressVectorTable.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddressVectorEntry_Object = MibTableRow
exampleIpAddressOperStructIpAddressVectorEntry = _ExampleIpAddressOperStructIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1058, 1)
)
exampleIpAddressOperStructIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperStructIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressVectorEntry.setStatus("mandatory")


class _ExampleIpAddressOperStructIpAddressVectorIndex_Type(Integer32):
    """Custom type exampleIpAddressOperStructIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleIpAddressOperStructIpAddressVectorIndex_Type.__name__ = "Integer32"
_ExampleIpAddressOperStructIpAddressVectorIndex_Object = MibTableColumn
exampleIpAddressOperStructIpAddressVectorIndex = _ExampleIpAddressOperStructIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1058, 1, 1),
    _ExampleIpAddressOperStructIpAddressVectorIndex_Type()
)
exampleIpAddressOperStructIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressVectorIndex.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddressVectorValue_Type = IpAddress
_ExampleIpAddressOperStructIpAddressVectorValue_Object = MibTableColumn
exampleIpAddressOperStructIpAddressVectorValue = _ExampleIpAddressOperStructIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1058, 1, 2),
    _ExampleIpAddressOperStructIpAddressVectorValue_Type()
)
exampleIpAddressOperStructIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressVectorValue.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddressArrayTable_Object = MibTable
exampleIpAddressOperStructIpAddressArrayTable = _ExampleIpAddressOperStructIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1059)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressArrayTable.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddressArrayEntry_Object = MibTableRow
exampleIpAddressOperStructIpAddressArrayEntry = _ExampleIpAddressOperStructIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1059, 1)
)
exampleIpAddressOperStructIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperStructIpAddressArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperStructIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressArrayEntry.setStatus("mandatory")


class _ExampleIpAddressOperStructIpAddressArrayRowIndex_Type(Integer32):
    """Custom type exampleIpAddressOperStructIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleIpAddressOperStructIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_ExampleIpAddressOperStructIpAddressArrayRowIndex_Object = MibTableColumn
exampleIpAddressOperStructIpAddressArrayRowIndex = _ExampleIpAddressOperStructIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1059, 1, 1),
    _ExampleIpAddressOperStructIpAddressArrayRowIndex_Type()
)
exampleIpAddressOperStructIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressArrayRowIndex.setStatus("mandatory")


class _ExampleIpAddressOperStructIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type exampleIpAddressOperStructIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressOperStructIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleIpAddressOperStructIpAddressArrayColumnIndex_Object = MibTableColumn
exampleIpAddressOperStructIpAddressArrayColumnIndex = _ExampleIpAddressOperStructIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1059, 1, 2),
    _ExampleIpAddressOperStructIpAddressArrayColumnIndex_Type()
)
exampleIpAddressOperStructIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressArrayColumnIndex.setStatus("mandatory")
_ExampleIpAddressOperStructIpAddressArrayValue_Type = IpAddress
_ExampleIpAddressOperStructIpAddressArrayValue_Object = MibTableColumn
exampleIpAddressOperStructIpAddressArrayValue = _ExampleIpAddressOperStructIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1059, 1, 3),
    _ExampleIpAddressOperStructIpAddressArrayValue_Type()
)
exampleIpAddressOperStructIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperStructIpAddressArrayValue.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressVectorTable_Object = MibTable
exampleIpAddressOperFreeIpAddressVectorTable = _ExampleIpAddressOperFreeIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1060)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressVectorTable.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressVectorEntry_Object = MibTableRow
exampleIpAddressOperFreeIpAddressVectorEntry = _ExampleIpAddressOperFreeIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1060, 1)
)
exampleIpAddressOperFreeIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperFreeIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressVectorEntry.setStatus("mandatory")


class _ExampleIpAddressOperFreeIpAddressVectorIndex_Type(Integer32):
    """Custom type exampleIpAddressOperFreeIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleIpAddressOperFreeIpAddressVectorIndex_Type.__name__ = "Integer32"
_ExampleIpAddressOperFreeIpAddressVectorIndex_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressVectorIndex = _ExampleIpAddressOperFreeIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1060, 1, 1),
    _ExampleIpAddressOperFreeIpAddressVectorIndex_Type()
)
exampleIpAddressOperFreeIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressVectorIndex.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressVectorValue_Type = IpAddress
_ExampleIpAddressOperFreeIpAddressVectorValue_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressVectorValue = _ExampleIpAddressOperFreeIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1060, 1, 2),
    _ExampleIpAddressOperFreeIpAddressVectorValue_Type()
)
exampleIpAddressOperFreeIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressVectorValue.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressArrayTable_Object = MibTable
exampleIpAddressOperFreeIpAddressArrayTable = _ExampleIpAddressOperFreeIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1061)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressArrayTable.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressArrayEntry_Object = MibTableRow
exampleIpAddressOperFreeIpAddressArrayEntry = _ExampleIpAddressOperFreeIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1061, 1)
)
exampleIpAddressOperFreeIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperFreeIpAddressArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperFreeIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressArrayEntry.setStatus("mandatory")


class _ExampleIpAddressOperFreeIpAddressArrayRowIndex_Type(Integer32):
    """Custom type exampleIpAddressOperFreeIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleIpAddressOperFreeIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_ExampleIpAddressOperFreeIpAddressArrayRowIndex_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressArrayRowIndex = _ExampleIpAddressOperFreeIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1061, 1, 1),
    _ExampleIpAddressOperFreeIpAddressArrayRowIndex_Type()
)
exampleIpAddressOperFreeIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressArrayRowIndex.setStatus("mandatory")


class _ExampleIpAddressOperFreeIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type exampleIpAddressOperFreeIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressOperFreeIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleIpAddressOperFreeIpAddressArrayColumnIndex_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressArrayColumnIndex = _ExampleIpAddressOperFreeIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1061, 1, 2),
    _ExampleIpAddressOperFreeIpAddressArrayColumnIndex_Type()
)
exampleIpAddressOperFreeIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressArrayColumnIndex.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressArrayValue_Type = IpAddress
_ExampleIpAddressOperFreeIpAddressArrayValue_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressArrayValue = _ExampleIpAddressOperFreeIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1061, 1, 3),
    _ExampleIpAddressOperFreeIpAddressArrayValue_Type()
)
exampleIpAddressOperFreeIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressArrayValue.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressReplicatedTable_Object = MibTable
exampleIpAddressOperFreeIpAddressReplicatedTable = _ExampleIpAddressOperFreeIpAddressReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1062)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressReplicatedTable.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressReplicatedEntry_Object = MibTableRow
exampleIpAddressOperFreeIpAddressReplicatedEntry = _ExampleIpAddressOperFreeIpAddressReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1062, 1)
)
exampleIpAddressOperFreeIpAddressReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperFreeIpAddressReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressReplicatedEntry.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressReplicatedIndex_Type = IpAddress
_ExampleIpAddressOperFreeIpAddressReplicatedIndex_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressReplicatedIndex = _ExampleIpAddressOperFreeIpAddressReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1062, 1, 1),
    _ExampleIpAddressOperFreeIpAddressReplicatedIndex_Type()
)
exampleIpAddressOperFreeIpAddressReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressReplicatedIndex.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressReplicatedValue_Type = IpAddress
_ExampleIpAddressOperFreeIpAddressReplicatedValue_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressReplicatedValue = _ExampleIpAddressOperFreeIpAddressReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1062, 1, 2),
    _ExampleIpAddressOperFreeIpAddressReplicatedValue_Type()
)
exampleIpAddressOperFreeIpAddressReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressReplicatedValue.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Type = RowStatus
_ExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressReplicatedRowStatus = _ExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1062, 1, 3),
    _ExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Type()
)
exampleIpAddressOperFreeIpAddressReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressReplicatedRowStatus.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressListTable_Object = MibTable
exampleIpAddressOperFreeIpAddressListTable = _ExampleIpAddressOperFreeIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1063)
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressListTable.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressListEntry_Object = MibTableRow
exampleIpAddressOperFreeIpAddressListEntry = _ExampleIpAddressOperFreeIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1063, 1)
)
exampleIpAddressOperFreeIpAddressListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressOperFreeIpAddressListValue"),
)
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressListEntry.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressListValue_Type = IpAddress
_ExampleIpAddressOperFreeIpAddressListValue_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressListValue = _ExampleIpAddressOperFreeIpAddressListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1063, 1, 1),
    _ExampleIpAddressOperFreeIpAddressListValue_Type()
)
exampleIpAddressOperFreeIpAddressListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressListValue.setStatus("mandatory")
_ExampleIpAddressOperFreeIpAddressListRowStatus_Type = RowStatus
_ExampleIpAddressOperFreeIpAddressListRowStatus_Object = MibTableColumn
exampleIpAddressOperFreeIpAddressListRowStatus = _ExampleIpAddressOperFreeIpAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1063, 1, 2),
    _ExampleIpAddressOperFreeIpAddressListRowStatus_Type()
)
exampleIpAddressOperFreeIpAddressListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleIpAddressOperFreeIpAddressListRowStatus.setStatus("mandatory")
_ExampleIpAddressProvStructIpAddressVectorTable_Object = MibTable
exampleIpAddressProvStructIpAddressVectorTable = _ExampleIpAddressProvStructIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1064)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressVectorTable.setStatus("mandatory")
_ExampleIpAddressProvStructIpAddressVectorEntry_Object = MibTableRow
exampleIpAddressProvStructIpAddressVectorEntry = _ExampleIpAddressProvStructIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1064, 1)
)
exampleIpAddressProvStructIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvStructIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressVectorEntry.setStatus("mandatory")


class _ExampleIpAddressProvStructIpAddressVectorIndex_Type(Integer32):
    """Custom type exampleIpAddressProvStructIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleIpAddressProvStructIpAddressVectorIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvStructIpAddressVectorIndex_Object = MibTableColumn
exampleIpAddressProvStructIpAddressVectorIndex = _ExampleIpAddressProvStructIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1064, 1, 1),
    _ExampleIpAddressProvStructIpAddressVectorIndex_Type()
)
exampleIpAddressProvStructIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressVectorIndex.setStatus("mandatory")
_ExampleIpAddressProvStructIpAddressVectorValue_Type = IpAddress
_ExampleIpAddressProvStructIpAddressVectorValue_Object = MibTableColumn
exampleIpAddressProvStructIpAddressVectorValue = _ExampleIpAddressProvStructIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1064, 1, 2),
    _ExampleIpAddressProvStructIpAddressVectorValue_Type()
)
exampleIpAddressProvStructIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressVectorValue.setStatus("mandatory")
_ExampleIpAddressProvStructIpAddressArrayTable_Object = MibTable
exampleIpAddressProvStructIpAddressArrayTable = _ExampleIpAddressProvStructIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1065)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressArrayTable.setStatus("mandatory")
_ExampleIpAddressProvStructIpAddressArrayEntry_Object = MibTableRow
exampleIpAddressProvStructIpAddressArrayEntry = _ExampleIpAddressProvStructIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1065, 1)
)
exampleIpAddressProvStructIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvStructIpAddressArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvStructIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressArrayEntry.setStatus("mandatory")


class _ExampleIpAddressProvStructIpAddressArrayRowIndex_Type(Integer32):
    """Custom type exampleIpAddressProvStructIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleIpAddressProvStructIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvStructIpAddressArrayRowIndex_Object = MibTableColumn
exampleIpAddressProvStructIpAddressArrayRowIndex = _ExampleIpAddressProvStructIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1065, 1, 1),
    _ExampleIpAddressProvStructIpAddressArrayRowIndex_Type()
)
exampleIpAddressProvStructIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressArrayRowIndex.setStatus("mandatory")


class _ExampleIpAddressProvStructIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type exampleIpAddressProvStructIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressProvStructIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvStructIpAddressArrayColumnIndex_Object = MibTableColumn
exampleIpAddressProvStructIpAddressArrayColumnIndex = _ExampleIpAddressProvStructIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1065, 1, 2),
    _ExampleIpAddressProvStructIpAddressArrayColumnIndex_Type()
)
exampleIpAddressProvStructIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressArrayColumnIndex.setStatus("mandatory")
_ExampleIpAddressProvStructIpAddressArrayValue_Type = IpAddress
_ExampleIpAddressProvStructIpAddressArrayValue_Object = MibTableColumn
exampleIpAddressProvStructIpAddressArrayValue = _ExampleIpAddressProvStructIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1065, 1, 3),
    _ExampleIpAddressProvStructIpAddressArrayValue_Type()
)
exampleIpAddressProvStructIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvStructIpAddressArrayValue.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressVectorTable_Object = MibTable
exampleIpAddressProvFreeIpAddressVectorTable = _ExampleIpAddressProvFreeIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1066)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVectorTable.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressVectorEntry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressVectorEntry = _ExampleIpAddressProvFreeIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1066, 1)
)
exampleIpAddressProvFreeIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVectorEntry.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddressVectorIndex_Type(Integer32):
    """Custom type exampleIpAddressProvFreeIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleIpAddressProvFreeIpAddressVectorIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvFreeIpAddressVectorIndex_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressVectorIndex = _ExampleIpAddressProvFreeIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1066, 1, 1),
    _ExampleIpAddressProvFreeIpAddressVectorIndex_Type()
)
exampleIpAddressProvFreeIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVectorIndex.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressVectorValue_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressVectorValue_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressVectorValue = _ExampleIpAddressProvFreeIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1066, 1, 2),
    _ExampleIpAddressProvFreeIpAddressVectorValue_Type()
)
exampleIpAddressProvFreeIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVectorValue.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressVector1Table_Object = MibTable
exampleIpAddressProvFreeIpAddressVector1Table = _ExampleIpAddressProvFreeIpAddressVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1067)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVector1Table.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressVector1Entry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressVector1Entry = _ExampleIpAddressProvFreeIpAddressVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1067, 1)
)
exampleIpAddressProvFreeIpAddressVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressVector1Index"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVector1Entry.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddressVector1Index_Type(Integer32):
    """Custom type exampleIpAddressProvFreeIpAddressVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressProvFreeIpAddressVector1Index_Type.__name__ = "Integer32"
_ExampleIpAddressProvFreeIpAddressVector1Index_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressVector1Index = _ExampleIpAddressProvFreeIpAddressVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1067, 1, 1),
    _ExampleIpAddressProvFreeIpAddressVector1Index_Type()
)
exampleIpAddressProvFreeIpAddressVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVector1Index.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressVector1Value_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressVector1Value_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressVector1Value = _ExampleIpAddressProvFreeIpAddressVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1067, 1, 2),
    _ExampleIpAddressProvFreeIpAddressVector1Value_Type()
)
exampleIpAddressProvFreeIpAddressVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressVector1Value.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressArrayTable_Object = MibTable
exampleIpAddressProvFreeIpAddressArrayTable = _ExampleIpAddressProvFreeIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1068)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArrayTable.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressArrayEntry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressArrayEntry = _ExampleIpAddressProvFreeIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1068, 1)
)
exampleIpAddressProvFreeIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArrayEntry.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddressArrayRowIndex_Type(Integer32):
    """Custom type exampleIpAddressProvFreeIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleIpAddressProvFreeIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvFreeIpAddressArrayRowIndex_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressArrayRowIndex = _ExampleIpAddressProvFreeIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1068, 1, 1),
    _ExampleIpAddressProvFreeIpAddressArrayRowIndex_Type()
)
exampleIpAddressProvFreeIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArrayRowIndex.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type exampleIpAddressProvFreeIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressProvFreeIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvFreeIpAddressArrayColumnIndex_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressArrayColumnIndex = _ExampleIpAddressProvFreeIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1068, 1, 2),
    _ExampleIpAddressProvFreeIpAddressArrayColumnIndex_Type()
)
exampleIpAddressProvFreeIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArrayColumnIndex.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressArrayValue_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressArrayValue_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressArrayValue = _ExampleIpAddressProvFreeIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1068, 1, 3),
    _ExampleIpAddressProvFreeIpAddressArrayValue_Type()
)
exampleIpAddressProvFreeIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArrayValue.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressArray1Table_Object = MibTable
exampleIpAddressProvFreeIpAddressArray1Table = _ExampleIpAddressProvFreeIpAddressArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1069)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArray1Table.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressArray1Entry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressArray1Entry = _ExampleIpAddressProvFreeIpAddressArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1069, 1)
)
exampleIpAddressProvFreeIpAddressArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressArray1RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArray1Entry.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddressArray1RowIndex_Type(Integer32):
    """Custom type exampleIpAddressProvFreeIpAddressArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressProvFreeIpAddressArray1RowIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvFreeIpAddressArray1RowIndex_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressArray1RowIndex = _ExampleIpAddressProvFreeIpAddressArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1069, 1, 1),
    _ExampleIpAddressProvFreeIpAddressArray1RowIndex_Type()
)
exampleIpAddressProvFreeIpAddressArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArray1RowIndex.setStatus("mandatory")


class _ExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Type(Integer32):
    """Custom type exampleIpAddressProvFreeIpAddressArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Type.__name__ = "Integer32"
_ExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressArray1ColumnIndex = _ExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1069, 1, 2),
    _ExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Type()
)
exampleIpAddressProvFreeIpAddressArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArray1ColumnIndex.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressArray1Value_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressArray1Value_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressArray1Value = _ExampleIpAddressProvFreeIpAddressArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1069, 1, 3),
    _ExampleIpAddressProvFreeIpAddressArray1Value_Type()
)
exampleIpAddressProvFreeIpAddressArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressArray1Value.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressReplicatedTable_Object = MibTable
exampleIpAddressProvFreeIpAddressReplicatedTable = _ExampleIpAddressProvFreeIpAddressReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1070)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressReplicatedTable.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressReplicatedEntry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressReplicatedEntry = _ExampleIpAddressProvFreeIpAddressReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1070, 1)
)
exampleIpAddressProvFreeIpAddressReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressReplicatedEntry.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressReplicatedIndex_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressReplicatedIndex_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressReplicatedIndex = _ExampleIpAddressProvFreeIpAddressReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1070, 1, 1),
    _ExampleIpAddressProvFreeIpAddressReplicatedIndex_Type()
)
exampleIpAddressProvFreeIpAddressReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressReplicatedIndex.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressReplicatedValue_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressReplicatedValue_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressReplicatedValue = _ExampleIpAddressProvFreeIpAddressReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1070, 1, 2),
    _ExampleIpAddressProvFreeIpAddressReplicatedValue_Type()
)
exampleIpAddressProvFreeIpAddressReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressReplicatedValue.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Type = RowStatus
_ExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressReplicatedRowStatus = _ExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1070, 1, 3),
    _ExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Type()
)
exampleIpAddressProvFreeIpAddressReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressReplicatedRowStatus.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressListTable_Object = MibTable
exampleIpAddressProvFreeIpAddressListTable = _ExampleIpAddressProvFreeIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1071)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressListTable.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressListEntry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressListEntry = _ExampleIpAddressProvFreeIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1071, 1)
)
exampleIpAddressProvFreeIpAddressListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressListValue"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressListEntry.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressListValue_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressListValue_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressListValue = _ExampleIpAddressProvFreeIpAddressListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1071, 1, 1),
    _ExampleIpAddressProvFreeIpAddressListValue_Type()
)
exampleIpAddressProvFreeIpAddressListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressListValue.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressListRowStatus_Type = RowStatus
_ExampleIpAddressProvFreeIpAddressListRowStatus_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressListRowStatus = _ExampleIpAddressProvFreeIpAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1071, 1, 2),
    _ExampleIpAddressProvFreeIpAddressListRowStatus_Type()
)
exampleIpAddressProvFreeIpAddressListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressListRowStatus.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressList1Table_Object = MibTable
exampleIpAddressProvFreeIpAddressList1Table = _ExampleIpAddressProvFreeIpAddressList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1072)
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressList1Table.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressList1Entry_Object = MibTableRow
exampleIpAddressProvFreeIpAddressList1Entry = _ExampleIpAddressProvFreeIpAddressList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1072, 1)
)
exampleIpAddressProvFreeIpAddressList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddressProvFreeIpAddressList1Value"),
)
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressList1Entry.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressList1Value_Type = IpAddress
_ExampleIpAddressProvFreeIpAddressList1Value_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressList1Value = _ExampleIpAddressProvFreeIpAddressList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1072, 1, 1),
    _ExampleIpAddressProvFreeIpAddressList1Value_Type()
)
exampleIpAddressProvFreeIpAddressList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressList1Value.setStatus("mandatory")
_ExampleIpAddressProvFreeIpAddressList1RowStatus_Type = RowStatus
_ExampleIpAddressProvFreeIpAddressList1RowStatus_Object = MibTableColumn
exampleIpAddressProvFreeIpAddressList1RowStatus = _ExampleIpAddressProvFreeIpAddressList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 4, 1072, 1, 2),
    _ExampleIpAddressProvFreeIpAddressList1RowStatus_Type()
)
exampleIpAddressProvFreeIpAddressList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleIpAddressProvFreeIpAddressList1RowStatus.setStatus("mandatory")
_ExampleString_ObjectIdentity = ObjectIdentity
exampleString = _ExampleString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5)
)
_ExampleStringRowStatusTable_Object = MibTable
exampleStringRowStatusTable = _ExampleStringRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1)
)
if mibBuilder.loadTexts:
    exampleStringRowStatusTable.setStatus("mandatory")
_ExampleStringRowStatusEntry_Object = MibTableRow
exampleStringRowStatusEntry = _ExampleStringRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1, 1)
)
exampleStringRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
)
if mibBuilder.loadTexts:
    exampleStringRowStatusEntry.setStatus("mandatory")
_ExampleStringRowStatus_Type = RowStatus
_ExampleStringRowStatus_Object = MibTableColumn
exampleStringRowStatus = _ExampleStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1, 1, 1),
    _ExampleStringRowStatus_Type()
)
exampleStringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringRowStatus.setStatus("mandatory")
_ExampleStringComponentName_Type = DisplayString
_ExampleStringComponentName_Object = MibTableColumn
exampleStringComponentName = _ExampleStringComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1, 1, 2),
    _ExampleStringComponentName_Type()
)
exampleStringComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleStringComponentName.setStatus("mandatory")
_ExampleStringStorageType_Type = StorageType
_ExampleStringStorageType_Object = MibTableColumn
exampleStringStorageType = _ExampleStringStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1, 1, 4),
    _ExampleStringStorageType_Type()
)
exampleStringStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleStringStorageType.setStatus("mandatory")


class _ExampleStringIndex_Type(AsciiStringIndex):
    """Custom type exampleStringIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleStringIndex_Type.__name__ = "AsciiStringIndex"
_ExampleStringIndex_Object = MibTableColumn
exampleStringIndex = _ExampleStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1, 1, 10),
    _ExampleStringIndex_Type()
)
exampleStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringIndex.setStatus("mandatory")
_ExampleStringOperationalTable_Object = MibTable
exampleStringOperationalTable = _ExampleStringOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 10)
)
if mibBuilder.loadTexts:
    exampleStringOperationalTable.setStatus("mandatory")
_ExampleStringOperationalEntry_Object = MibTableRow
exampleStringOperationalEntry = _ExampleStringOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 10, 1)
)
exampleStringOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
)
if mibBuilder.loadTexts:
    exampleStringOperationalEntry.setStatus("mandatory")


class _ExampleStringOperStructAsciiOnly_Type(AsciiString):
    """Custom type exampleStringOperStructAsciiOnly based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperStructAsciiOnly_Type.__name__ = "AsciiString"
_ExampleStringOperStructAsciiOnly_Object = MibTableColumn
exampleStringOperStructAsciiOnly = _ExampleStringOperStructAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 10, 1, 1),
    _ExampleStringOperStructAsciiOnly_Type()
)
exampleStringOperStructAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperStructAsciiOnly.setStatus("mandatory")


class _ExampleStringOperStructHexOnly_Type(HexString):
    """Custom type exampleStringOperStructHexOnly based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleStringOperStructHexOnly_Type.__name__ = "HexString"
_ExampleStringOperStructHexOnly_Object = MibTableColumn
exampleStringOperStructHexOnly = _ExampleStringOperStructHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 10, 1, 2),
    _ExampleStringOperStructHexOnly_Type()
)
exampleStringOperStructHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperStructHexOnly.setStatus("mandatory")


class _ExampleStringOperFreeAsciiOnly_Type(AsciiString):
    """Custom type exampleStringOperFreeAsciiOnly based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperFreeAsciiOnly_Type.__name__ = "AsciiString"
_ExampleStringOperFreeAsciiOnly_Object = MibTableColumn
exampleStringOperFreeAsciiOnly = _ExampleStringOperFreeAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 10, 1, 3),
    _ExampleStringOperFreeAsciiOnly_Type()
)
exampleStringOperFreeAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperFreeAsciiOnly.setStatus("mandatory")


class _ExampleStringOperFreeHexOnly_Type(HexString):
    """Custom type exampleStringOperFreeHexOnly based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleStringOperFreeHexOnly_Type.__name__ = "HexString"
_ExampleStringOperFreeHexOnly_Object = MibTableColumn
exampleStringOperFreeHexOnly = _ExampleStringOperFreeHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 10, 1, 4),
    _ExampleStringOperFreeHexOnly_Type()
)
exampleStringOperFreeHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperFreeHexOnly.setStatus("mandatory")
_ExampleStringProvisionalTable_Object = MibTable
exampleStringProvisionalTable = _ExampleStringProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11)
)
if mibBuilder.loadTexts:
    exampleStringProvisionalTable.setStatus("mandatory")
_ExampleStringProvisionalEntry_Object = MibTableRow
exampleStringProvisionalEntry = _ExampleStringProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1)
)
exampleStringProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvisionalEntry.setStatus("mandatory")
_ExampleStringProvStringSub_Type = Link
_ExampleStringProvStringSub_Object = MibTableColumn
exampleStringProvStringSub = _ExampleStringProvStringSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 1),
    _ExampleStringProvStringSub_Type()
)
exampleStringProvStringSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvStringSub.setStatus("mandatory")


class _ExampleStringProvStructAsciiOnly_Type(AsciiString):
    """Custom type exampleStringProvStructAsciiOnly based on AsciiString"""
    defaultHexValue = "596f2e"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_ExampleStringProvStructAsciiOnly_Type.__name__ = "AsciiString"
_ExampleStringProvStructAsciiOnly_Object = MibTableColumn
exampleStringProvStructAsciiOnly = _ExampleStringProvStructAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 2),
    _ExampleStringProvStructAsciiOnly_Type()
)
exampleStringProvStructAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvStructAsciiOnly.setStatus("mandatory")


class _ExampleStringProvStructHexOnly_Type(HexString):
    """Custom type exampleStringProvStructHexOnly based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleStringProvStructHexOnly_Type.__name__ = "HexString"
_ExampleStringProvStructHexOnly_Object = MibTableColumn
exampleStringProvStructHexOnly = _ExampleStringProvStructHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 3),
    _ExampleStringProvStructHexOnly_Type()
)
exampleStringProvStructHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvStructHexOnly.setStatus("mandatory")


class _ExampleStringProvFreeAsciiOnly_Type(AsciiString):
    """Custom type exampleStringProvFreeAsciiOnly based on AsciiString"""
    defaultHexValue = "46726565205374616e64696e6720537472696e6720212121"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_ExampleStringProvFreeAsciiOnly_Type.__name__ = "AsciiString"
_ExampleStringProvFreeAsciiOnly_Object = MibTableColumn
exampleStringProvFreeAsciiOnly = _ExampleStringProvFreeAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 4),
    _ExampleStringProvFreeAsciiOnly_Type()
)
exampleStringProvFreeAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeAsciiOnly.setStatus("mandatory")


class _ExampleStringProvFreeAsciiOnly1_Type(AsciiString):
    """Custom type exampleStringProvFreeAsciiOnly1 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeAsciiOnly1_Type.__name__ = "AsciiString"
_ExampleStringProvFreeAsciiOnly1_Object = MibTableColumn
exampleStringProvFreeAsciiOnly1 = _ExampleStringProvFreeAsciiOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 5),
    _ExampleStringProvFreeAsciiOnly1_Type()
)
exampleStringProvFreeAsciiOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeAsciiOnly1.setStatus("mandatory")


class _ExampleStringProvFreeHexOnly_Type(HexString):
    """Custom type exampleStringProvFreeHexOnly based on HexString"""
    defaultHexValue = "0102030405060708090A"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleStringProvFreeHexOnly_Type.__name__ = "HexString"
_ExampleStringProvFreeHexOnly_Object = MibTableColumn
exampleStringProvFreeHexOnly = _ExampleStringProvFreeHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 6),
    _ExampleStringProvFreeHexOnly_Type()
)
exampleStringProvFreeHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeHexOnly.setStatus("mandatory")


class _ExampleStringProvFreeHexOnly1_Type(HexString):
    """Custom type exampleStringProvFreeHexOnly1 based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ExampleStringProvFreeHexOnly1_Type.__name__ = "HexString"
_ExampleStringProvFreeHexOnly1_Object = MibTableColumn
exampleStringProvFreeHexOnly1 = _ExampleStringProvFreeHexOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 11, 1, 7),
    _ExampleStringProvFreeHexOnly1_Type()
)
exampleStringProvFreeHexOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeHexOnly1.setStatus("mandatory")
_ExampleStringOperStructStrVectorTable_Object = MibTable
exampleStringOperStructStrVectorTable = _ExampleStringOperStructStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1073)
)
if mibBuilder.loadTexts:
    exampleStringOperStructStrVectorTable.setStatus("mandatory")
_ExampleStringOperStructStrVectorEntry_Object = MibTableRow
exampleStringOperStructStrVectorEntry = _ExampleStringOperStructStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1073, 1)
)
exampleStringOperStructStrVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperStructStrVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleStringOperStructStrVectorEntry.setStatus("mandatory")


class _ExampleStringOperStructStrVectorIndex_Type(Integer32):
    """Custom type exampleStringOperStructStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleStringOperStructStrVectorIndex_Type.__name__ = "Integer32"
_ExampleStringOperStructStrVectorIndex_Object = MibTableColumn
exampleStringOperStructStrVectorIndex = _ExampleStringOperStructStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1073, 1, 1),
    _ExampleStringOperStructStrVectorIndex_Type()
)
exampleStringOperStructStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperStructStrVectorIndex.setStatus("mandatory")


class _ExampleStringOperStructStrVectorValue_Type(AsciiString):
    """Custom type exampleStringOperStructStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperStructStrVectorValue_Type.__name__ = "AsciiString"
_ExampleStringOperStructStrVectorValue_Object = MibTableColumn
exampleStringOperStructStrVectorValue = _ExampleStringOperStructStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1073, 1, 2),
    _ExampleStringOperStructStrVectorValue_Type()
)
exampleStringOperStructStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperStructStrVectorValue.setStatus("mandatory")
_ExampleStringOperStructStrArrayTable_Object = MibTable
exampleStringOperStructStrArrayTable = _ExampleStringOperStructStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1074)
)
if mibBuilder.loadTexts:
    exampleStringOperStructStrArrayTable.setStatus("mandatory")
_ExampleStringOperStructStrArrayEntry_Object = MibTableRow
exampleStringOperStructStrArrayEntry = _ExampleStringOperStructStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1074, 1)
)
exampleStringOperStructStrArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperStructStrArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperStructStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleStringOperStructStrArrayEntry.setStatus("mandatory")


class _ExampleStringOperStructStrArrayRowIndex_Type(Integer32):
    """Custom type exampleStringOperStructStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleStringOperStructStrArrayRowIndex_Type.__name__ = "Integer32"
_ExampleStringOperStructStrArrayRowIndex_Object = MibTableColumn
exampleStringOperStructStrArrayRowIndex = _ExampleStringOperStructStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1074, 1, 1),
    _ExampleStringOperStructStrArrayRowIndex_Type()
)
exampleStringOperStructStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperStructStrArrayRowIndex.setStatus("mandatory")


class _ExampleStringOperStructStrArrayColumnIndex_Type(Integer32):
    """Custom type exampleStringOperStructStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleStringOperStructStrArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleStringOperStructStrArrayColumnIndex_Object = MibTableColumn
exampleStringOperStructStrArrayColumnIndex = _ExampleStringOperStructStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1074, 1, 2),
    _ExampleStringOperStructStrArrayColumnIndex_Type()
)
exampleStringOperStructStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperStructStrArrayColumnIndex.setStatus("mandatory")


class _ExampleStringOperStructStrArrayValue_Type(AsciiString):
    """Custom type exampleStringOperStructStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperStructStrArrayValue_Type.__name__ = "AsciiString"
_ExampleStringOperStructStrArrayValue_Object = MibTableColumn
exampleStringOperStructStrArrayValue = _ExampleStringOperStructStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1074, 1, 3),
    _ExampleStringOperStructStrArrayValue_Type()
)
exampleStringOperStructStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperStructStrArrayValue.setStatus("mandatory")
_ExampleStringOperFreeStrVectorTable_Object = MibTable
exampleStringOperFreeStrVectorTable = _ExampleStringOperFreeStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1075)
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrVectorTable.setStatus("mandatory")
_ExampleStringOperFreeStrVectorEntry_Object = MibTableRow
exampleStringOperFreeStrVectorEntry = _ExampleStringOperFreeStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1075, 1)
)
exampleStringOperFreeStrVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperFreeStrVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrVectorEntry.setStatus("mandatory")


class _ExampleStringOperFreeStrVectorIndex_Type(Integer32):
    """Custom type exampleStringOperFreeStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleStringOperFreeStrVectorIndex_Type.__name__ = "Integer32"
_ExampleStringOperFreeStrVectorIndex_Object = MibTableColumn
exampleStringOperFreeStrVectorIndex = _ExampleStringOperFreeStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1075, 1, 1),
    _ExampleStringOperFreeStrVectorIndex_Type()
)
exampleStringOperFreeStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrVectorIndex.setStatus("mandatory")


class _ExampleStringOperFreeStrVectorValue_Type(AsciiString):
    """Custom type exampleStringOperFreeStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperFreeStrVectorValue_Type.__name__ = "AsciiString"
_ExampleStringOperFreeStrVectorValue_Object = MibTableColumn
exampleStringOperFreeStrVectorValue = _ExampleStringOperFreeStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1075, 1, 2),
    _ExampleStringOperFreeStrVectorValue_Type()
)
exampleStringOperFreeStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrVectorValue.setStatus("mandatory")
_ExampleStringOperFreeStrArrayTable_Object = MibTable
exampleStringOperFreeStrArrayTable = _ExampleStringOperFreeStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1076)
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrArrayTable.setStatus("mandatory")
_ExampleStringOperFreeStrArrayEntry_Object = MibTableRow
exampleStringOperFreeStrArrayEntry = _ExampleStringOperFreeStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1076, 1)
)
exampleStringOperFreeStrArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperFreeStrArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperFreeStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrArrayEntry.setStatus("mandatory")


class _ExampleStringOperFreeStrArrayRowIndex_Type(Integer32):
    """Custom type exampleStringOperFreeStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleStringOperFreeStrArrayRowIndex_Type.__name__ = "Integer32"
_ExampleStringOperFreeStrArrayRowIndex_Object = MibTableColumn
exampleStringOperFreeStrArrayRowIndex = _ExampleStringOperFreeStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1076, 1, 1),
    _ExampleStringOperFreeStrArrayRowIndex_Type()
)
exampleStringOperFreeStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrArrayRowIndex.setStatus("mandatory")


class _ExampleStringOperFreeStrArrayColumnIndex_Type(Integer32):
    """Custom type exampleStringOperFreeStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleStringOperFreeStrArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleStringOperFreeStrArrayColumnIndex_Object = MibTableColumn
exampleStringOperFreeStrArrayColumnIndex = _ExampleStringOperFreeStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1076, 1, 2),
    _ExampleStringOperFreeStrArrayColumnIndex_Type()
)
exampleStringOperFreeStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrArrayColumnIndex.setStatus("mandatory")


class _ExampleStringOperFreeStrArrayValue_Type(AsciiString):
    """Custom type exampleStringOperFreeStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperFreeStrArrayValue_Type.__name__ = "AsciiString"
_ExampleStringOperFreeStrArrayValue_Object = MibTableColumn
exampleStringOperFreeStrArrayValue = _ExampleStringOperFreeStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1076, 1, 3),
    _ExampleStringOperFreeStrArrayValue_Type()
)
exampleStringOperFreeStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrArrayValue.setStatus("mandatory")
_ExampleStringOperFreeStrReplicatedTable_Object = MibTable
exampleStringOperFreeStrReplicatedTable = _ExampleStringOperFreeStrReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1077)
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrReplicatedTable.setStatus("mandatory")
_ExampleStringOperFreeStrReplicatedEntry_Object = MibTableRow
exampleStringOperFreeStrReplicatedEntry = _ExampleStringOperFreeStrReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1077, 1)
)
exampleStringOperFreeStrReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperFreeStrReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrReplicatedEntry.setStatus("mandatory")


class _ExampleStringOperFreeStrReplicatedIndex_Type(AsciiString):
    """Custom type exampleStringOperFreeStrReplicatedIndex based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperFreeStrReplicatedIndex_Type.__name__ = "AsciiString"
_ExampleStringOperFreeStrReplicatedIndex_Object = MibTableColumn
exampleStringOperFreeStrReplicatedIndex = _ExampleStringOperFreeStrReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1077, 1, 1),
    _ExampleStringOperFreeStrReplicatedIndex_Type()
)
exampleStringOperFreeStrReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrReplicatedIndex.setStatus("mandatory")


class _ExampleStringOperFreeStrReplicatedValue_Type(AsciiString):
    """Custom type exampleStringOperFreeStrReplicatedValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringOperFreeStrReplicatedValue_Type.__name__ = "AsciiString"
_ExampleStringOperFreeStrReplicatedValue_Object = MibTableColumn
exampleStringOperFreeStrReplicatedValue = _ExampleStringOperFreeStrReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1077, 1, 2),
    _ExampleStringOperFreeStrReplicatedValue_Type()
)
exampleStringOperFreeStrReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrReplicatedValue.setStatus("mandatory")
_ExampleStringOperFreeStrReplicatedRowStatus_Type = RowStatus
_ExampleStringOperFreeStrReplicatedRowStatus_Object = MibTableColumn
exampleStringOperFreeStrReplicatedRowStatus = _ExampleStringOperFreeStrReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1077, 1, 3),
    _ExampleStringOperFreeStrReplicatedRowStatus_Type()
)
exampleStringOperFreeStrReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrReplicatedRowStatus.setStatus("mandatory")
_ExampleStringOperFreeStrListTable_Object = MibTable
exampleStringOperFreeStrListTable = _ExampleStringOperFreeStrListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1078)
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrListTable.setStatus("mandatory")
_ExampleStringOperFreeStrListEntry_Object = MibTableRow
exampleStringOperFreeStrListEntry = _ExampleStringOperFreeStrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1078, 1)
)
exampleStringOperFreeStrListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringOperFreeStrListValue"),
)
if mibBuilder.loadTexts:
    exampleStringOperFreeStrListEntry.setStatus("mandatory")


class _ExampleStringOperFreeStrListValue_Type(AsciiString):
    """Custom type exampleStringOperFreeStrListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ExampleStringOperFreeStrListValue_Type.__name__ = "AsciiString"
_ExampleStringOperFreeStrListValue_Object = MibTableColumn
exampleStringOperFreeStrListValue = _ExampleStringOperFreeStrListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1078, 1, 1),
    _ExampleStringOperFreeStrListValue_Type()
)
exampleStringOperFreeStrListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrListValue.setStatus("mandatory")
_ExampleStringOperFreeStrListRowStatus_Type = RowStatus
_ExampleStringOperFreeStrListRowStatus_Object = MibTableColumn
exampleStringOperFreeStrListRowStatus = _ExampleStringOperFreeStrListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1078, 1, 2),
    _ExampleStringOperFreeStrListRowStatus_Type()
)
exampleStringOperFreeStrListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleStringOperFreeStrListRowStatus.setStatus("mandatory")
_ExampleStringProvStructStrVectorTable_Object = MibTable
exampleStringProvStructStrVectorTable = _ExampleStringProvStructStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1079)
)
if mibBuilder.loadTexts:
    exampleStringProvStructStrVectorTable.setStatus("mandatory")
_ExampleStringProvStructStrVectorEntry_Object = MibTableRow
exampleStringProvStructStrVectorEntry = _ExampleStringProvStructStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1079, 1)
)
exampleStringProvStructStrVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvStructStrVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvStructStrVectorEntry.setStatus("mandatory")


class _ExampleStringProvStructStrVectorIndex_Type(Integer32):
    """Custom type exampleStringProvStructStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleStringProvStructStrVectorIndex_Type.__name__ = "Integer32"
_ExampleStringProvStructStrVectorIndex_Object = MibTableColumn
exampleStringProvStructStrVectorIndex = _ExampleStringProvStructStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1079, 1, 1),
    _ExampleStringProvStructStrVectorIndex_Type()
)
exampleStringProvStructStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvStructStrVectorIndex.setStatus("mandatory")


class _ExampleStringProvStructStrVectorValue_Type(AsciiString):
    """Custom type exampleStringProvStructStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvStructStrVectorValue_Type.__name__ = "AsciiString"
_ExampleStringProvStructStrVectorValue_Object = MibTableColumn
exampleStringProvStructStrVectorValue = _ExampleStringProvStructStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1079, 1, 2),
    _ExampleStringProvStructStrVectorValue_Type()
)
exampleStringProvStructStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvStructStrVectorValue.setStatus("mandatory")
_ExampleStringProvStructStrArrayTable_Object = MibTable
exampleStringProvStructStrArrayTable = _ExampleStringProvStructStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1080)
)
if mibBuilder.loadTexts:
    exampleStringProvStructStrArrayTable.setStatus("mandatory")
_ExampleStringProvStructStrArrayEntry_Object = MibTableRow
exampleStringProvStructStrArrayEntry = _ExampleStringProvStructStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1080, 1)
)
exampleStringProvStructStrArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvStructStrArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvStructStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvStructStrArrayEntry.setStatus("mandatory")


class _ExampleStringProvStructStrArrayRowIndex_Type(Integer32):
    """Custom type exampleStringProvStructStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleStringProvStructStrArrayRowIndex_Type.__name__ = "Integer32"
_ExampleStringProvStructStrArrayRowIndex_Object = MibTableColumn
exampleStringProvStructStrArrayRowIndex = _ExampleStringProvStructStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1080, 1, 1),
    _ExampleStringProvStructStrArrayRowIndex_Type()
)
exampleStringProvStructStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvStructStrArrayRowIndex.setStatus("mandatory")


class _ExampleStringProvStructStrArrayColumnIndex_Type(Integer32):
    """Custom type exampleStringProvStructStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleStringProvStructStrArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleStringProvStructStrArrayColumnIndex_Object = MibTableColumn
exampleStringProvStructStrArrayColumnIndex = _ExampleStringProvStructStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1080, 1, 2),
    _ExampleStringProvStructStrArrayColumnIndex_Type()
)
exampleStringProvStructStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvStructStrArrayColumnIndex.setStatus("mandatory")


class _ExampleStringProvStructStrArrayValue_Type(AsciiString):
    """Custom type exampleStringProvStructStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvStructStrArrayValue_Type.__name__ = "AsciiString"
_ExampleStringProvStructStrArrayValue_Object = MibTableColumn
exampleStringProvStructStrArrayValue = _ExampleStringProvStructStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1080, 1, 3),
    _ExampleStringProvStructStrArrayValue_Type()
)
exampleStringProvStructStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvStructStrArrayValue.setStatus("mandatory")
_ExampleStringProvFreeStrVectorTable_Object = MibTable
exampleStringProvFreeStrVectorTable = _ExampleStringProvFreeStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1081)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVectorTable.setStatus("mandatory")
_ExampleStringProvFreeStrVectorEntry_Object = MibTableRow
exampleStringProvFreeStrVectorEntry = _ExampleStringProvFreeStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1081, 1)
)
exampleStringProvFreeStrVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVectorEntry.setStatus("mandatory")


class _ExampleStringProvFreeStrVectorIndex_Type(Integer32):
    """Custom type exampleStringProvFreeStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleStringProvFreeStrVectorIndex_Type.__name__ = "Integer32"
_ExampleStringProvFreeStrVectorIndex_Object = MibTableColumn
exampleStringProvFreeStrVectorIndex = _ExampleStringProvFreeStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1081, 1, 1),
    _ExampleStringProvFreeStrVectorIndex_Type()
)
exampleStringProvFreeStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVectorIndex.setStatus("mandatory")


class _ExampleStringProvFreeStrVectorValue_Type(AsciiString):
    """Custom type exampleStringProvFreeStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeStrVectorValue_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrVectorValue_Object = MibTableColumn
exampleStringProvFreeStrVectorValue = _ExampleStringProvFreeStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1081, 1, 2),
    _ExampleStringProvFreeStrVectorValue_Type()
)
exampleStringProvFreeStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVectorValue.setStatus("mandatory")
_ExampleStringProvFreeStrVector1Table_Object = MibTable
exampleStringProvFreeStrVector1Table = _ExampleStringProvFreeStrVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1082)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVector1Table.setStatus("mandatory")
_ExampleStringProvFreeStrVector1Entry_Object = MibTableRow
exampleStringProvFreeStrVector1Entry = _ExampleStringProvFreeStrVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1082, 1)
)
exampleStringProvFreeStrVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrVector1Index"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVector1Entry.setStatus("mandatory")


class _ExampleStringProvFreeStrVector1Index_Type(Integer32):
    """Custom type exampleStringProvFreeStrVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ExampleStringProvFreeStrVector1Index_Type.__name__ = "Integer32"
_ExampleStringProvFreeStrVector1Index_Object = MibTableColumn
exampleStringProvFreeStrVector1Index = _ExampleStringProvFreeStrVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1082, 1, 1),
    _ExampleStringProvFreeStrVector1Index_Type()
)
exampleStringProvFreeStrVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVector1Index.setStatus("mandatory")


class _ExampleStringProvFreeStrVector1Value_Type(AsciiString):
    """Custom type exampleStringProvFreeStrVector1Value based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeStrVector1Value_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrVector1Value_Object = MibTableColumn
exampleStringProvFreeStrVector1Value = _ExampleStringProvFreeStrVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1082, 1, 2),
    _ExampleStringProvFreeStrVector1Value_Type()
)
exampleStringProvFreeStrVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrVector1Value.setStatus("mandatory")
_ExampleStringProvFreeStrArrayTable_Object = MibTable
exampleStringProvFreeStrArrayTable = _ExampleStringProvFreeStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1083)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArrayTable.setStatus("mandatory")
_ExampleStringProvFreeStrArrayEntry_Object = MibTableRow
exampleStringProvFreeStrArrayEntry = _ExampleStringProvFreeStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1083, 1)
)
exampleStringProvFreeStrArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArrayEntry.setStatus("mandatory")


class _ExampleStringProvFreeStrArrayRowIndex_Type(Integer32):
    """Custom type exampleStringProvFreeStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleStringProvFreeStrArrayRowIndex_Type.__name__ = "Integer32"
_ExampleStringProvFreeStrArrayRowIndex_Object = MibTableColumn
exampleStringProvFreeStrArrayRowIndex = _ExampleStringProvFreeStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1083, 1, 1),
    _ExampleStringProvFreeStrArrayRowIndex_Type()
)
exampleStringProvFreeStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArrayRowIndex.setStatus("mandatory")


class _ExampleStringProvFreeStrArrayColumnIndex_Type(Integer32):
    """Custom type exampleStringProvFreeStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleStringProvFreeStrArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleStringProvFreeStrArrayColumnIndex_Object = MibTableColumn
exampleStringProvFreeStrArrayColumnIndex = _ExampleStringProvFreeStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1083, 1, 2),
    _ExampleStringProvFreeStrArrayColumnIndex_Type()
)
exampleStringProvFreeStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArrayColumnIndex.setStatus("mandatory")


class _ExampleStringProvFreeStrArrayValue_Type(AsciiString):
    """Custom type exampleStringProvFreeStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeStrArrayValue_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrArrayValue_Object = MibTableColumn
exampleStringProvFreeStrArrayValue = _ExampleStringProvFreeStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1083, 1, 3),
    _ExampleStringProvFreeStrArrayValue_Type()
)
exampleStringProvFreeStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArrayValue.setStatus("mandatory")
_ExampleStringProvFreeStrArray1Table_Object = MibTable
exampleStringProvFreeStrArray1Table = _ExampleStringProvFreeStrArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1084)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArray1Table.setStatus("mandatory")
_ExampleStringProvFreeStrArray1Entry_Object = MibTableRow
exampleStringProvFreeStrArray1Entry = _ExampleStringProvFreeStrArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1084, 1)
)
exampleStringProvFreeStrArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrArray1RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArray1Entry.setStatus("mandatory")


class _ExampleStringProvFreeStrArray1RowIndex_Type(Integer32):
    """Custom type exampleStringProvFreeStrArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ExampleStringProvFreeStrArray1RowIndex_Type.__name__ = "Integer32"
_ExampleStringProvFreeStrArray1RowIndex_Object = MibTableColumn
exampleStringProvFreeStrArray1RowIndex = _ExampleStringProvFreeStrArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1084, 1, 1),
    _ExampleStringProvFreeStrArray1RowIndex_Type()
)
exampleStringProvFreeStrArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArray1RowIndex.setStatus("mandatory")


class _ExampleStringProvFreeStrArray1ColumnIndex_Type(Integer32):
    """Custom type exampleStringProvFreeStrArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleStringProvFreeStrArray1ColumnIndex_Type.__name__ = "Integer32"
_ExampleStringProvFreeStrArray1ColumnIndex_Object = MibTableColumn
exampleStringProvFreeStrArray1ColumnIndex = _ExampleStringProvFreeStrArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1084, 1, 2),
    _ExampleStringProvFreeStrArray1ColumnIndex_Type()
)
exampleStringProvFreeStrArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArray1ColumnIndex.setStatus("mandatory")


class _ExampleStringProvFreeStrArray1Value_Type(AsciiString):
    """Custom type exampleStringProvFreeStrArray1Value based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeStrArray1Value_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrArray1Value_Object = MibTableColumn
exampleStringProvFreeStrArray1Value = _ExampleStringProvFreeStrArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1084, 1, 3),
    _ExampleStringProvFreeStrArray1Value_Type()
)
exampleStringProvFreeStrArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrArray1Value.setStatus("mandatory")
_ExampleStringProvFreeStrReplicatedTable_Object = MibTable
exampleStringProvFreeStrReplicatedTable = _ExampleStringProvFreeStrReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1085)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrReplicatedTable.setStatus("mandatory")
_ExampleStringProvFreeStrReplicatedEntry_Object = MibTableRow
exampleStringProvFreeStrReplicatedEntry = _ExampleStringProvFreeStrReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1085, 1)
)
exampleStringProvFreeStrReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrReplicatedEntry.setStatus("mandatory")


class _ExampleStringProvFreeStrReplicatedIndex_Type(AsciiString):
    """Custom type exampleStringProvFreeStrReplicatedIndex based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeStrReplicatedIndex_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrReplicatedIndex_Object = MibTableColumn
exampleStringProvFreeStrReplicatedIndex = _ExampleStringProvFreeStrReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1085, 1, 1),
    _ExampleStringProvFreeStrReplicatedIndex_Type()
)
exampleStringProvFreeStrReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrReplicatedIndex.setStatus("mandatory")


class _ExampleStringProvFreeStrReplicatedValue_Type(AsciiString):
    """Custom type exampleStringProvFreeStrReplicatedValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleStringProvFreeStrReplicatedValue_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrReplicatedValue_Object = MibTableColumn
exampleStringProvFreeStrReplicatedValue = _ExampleStringProvFreeStrReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1085, 1, 2),
    _ExampleStringProvFreeStrReplicatedValue_Type()
)
exampleStringProvFreeStrReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrReplicatedValue.setStatus("mandatory")
_ExampleStringProvFreeStrReplicatedRowStatus_Type = RowStatus
_ExampleStringProvFreeStrReplicatedRowStatus_Object = MibTableColumn
exampleStringProvFreeStrReplicatedRowStatus = _ExampleStringProvFreeStrReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1085, 1, 3),
    _ExampleStringProvFreeStrReplicatedRowStatus_Type()
)
exampleStringProvFreeStrReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrReplicatedRowStatus.setStatus("mandatory")
_ExampleStringProvFreeStrListTable_Object = MibTable
exampleStringProvFreeStrListTable = _ExampleStringProvFreeStrListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1086)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrListTable.setStatus("mandatory")
_ExampleStringProvFreeStrListEntry_Object = MibTableRow
exampleStringProvFreeStrListEntry = _ExampleStringProvFreeStrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1086, 1)
)
exampleStringProvFreeStrListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrListValue"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrListEntry.setStatus("mandatory")


class _ExampleStringProvFreeStrListValue_Type(AsciiString):
    """Custom type exampleStringProvFreeStrListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ExampleStringProvFreeStrListValue_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrListValue_Object = MibTableColumn
exampleStringProvFreeStrListValue = _ExampleStringProvFreeStrListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1086, 1, 1),
    _ExampleStringProvFreeStrListValue_Type()
)
exampleStringProvFreeStrListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrListValue.setStatus("mandatory")
_ExampleStringProvFreeStrListRowStatus_Type = RowStatus
_ExampleStringProvFreeStrListRowStatus_Object = MibTableColumn
exampleStringProvFreeStrListRowStatus = _ExampleStringProvFreeStrListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1086, 1, 2),
    _ExampleStringProvFreeStrListRowStatus_Type()
)
exampleStringProvFreeStrListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrListRowStatus.setStatus("mandatory")
_ExampleStringProvFreeStrList1Table_Object = MibTable
exampleStringProvFreeStrList1Table = _ExampleStringProvFreeStrList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1087)
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrList1Table.setStatus("mandatory")
_ExampleStringProvFreeStrList1Entry_Object = MibTableRow
exampleStringProvFreeStrList1Entry = _ExampleStringProvFreeStrList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1087, 1)
)
exampleStringProvFreeStrList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleStringProvFreeStrList1Value"),
)
if mibBuilder.loadTexts:
    exampleStringProvFreeStrList1Entry.setStatus("mandatory")


class _ExampleStringProvFreeStrList1Value_Type(AsciiString):
    """Custom type exampleStringProvFreeStrList1Value based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ExampleStringProvFreeStrList1Value_Type.__name__ = "AsciiString"
_ExampleStringProvFreeStrList1Value_Object = MibTableColumn
exampleStringProvFreeStrList1Value = _ExampleStringProvFreeStrList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1087, 1, 1),
    _ExampleStringProvFreeStrList1Value_Type()
)
exampleStringProvFreeStrList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrList1Value.setStatus("mandatory")
_ExampleStringProvFreeStrList1RowStatus_Type = RowStatus
_ExampleStringProvFreeStrList1RowStatus_Object = MibTableColumn
exampleStringProvFreeStrList1RowStatus = _ExampleStringProvFreeStrList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 5, 1087, 1, 2),
    _ExampleStringProvFreeStrList1RowStatus_Type()
)
exampleStringProvFreeStrList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleStringProvFreeStrList1RowStatus.setStatus("mandatory")
_ExampleFixedPt_ObjectIdentity = ObjectIdentity
exampleFixedPt = _ExampleFixedPt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6)
)
_ExampleFixedPtRowStatusTable_Object = MibTable
exampleFixedPtRowStatusTable = _ExampleFixedPtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1)
)
if mibBuilder.loadTexts:
    exampleFixedPtRowStatusTable.setStatus("mandatory")
_ExampleFixedPtRowStatusEntry_Object = MibTableRow
exampleFixedPtRowStatusEntry = _ExampleFixedPtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1, 1)
)
exampleFixedPtRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtRowStatusEntry.setStatus("mandatory")
_ExampleFixedPtRowStatus_Type = RowStatus
_ExampleFixedPtRowStatus_Object = MibTableColumn
exampleFixedPtRowStatus = _ExampleFixedPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1, 1, 1),
    _ExampleFixedPtRowStatus_Type()
)
exampleFixedPtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtRowStatus.setStatus("mandatory")
_ExampleFixedPtComponentName_Type = DisplayString
_ExampleFixedPtComponentName_Object = MibTableColumn
exampleFixedPtComponentName = _ExampleFixedPtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1, 1, 2),
    _ExampleFixedPtComponentName_Type()
)
exampleFixedPtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleFixedPtComponentName.setStatus("mandatory")
_ExampleFixedPtStorageType_Type = StorageType
_ExampleFixedPtStorageType_Object = MibTableColumn
exampleFixedPtStorageType = _ExampleFixedPtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1, 1, 4),
    _ExampleFixedPtStorageType_Type()
)
exampleFixedPtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleFixedPtStorageType.setStatus("mandatory")
_ExampleFixedPtIndex_Type = NonReplicated
_ExampleFixedPtIndex_Object = MibTableColumn
exampleFixedPtIndex = _ExampleFixedPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1, 1, 10),
    _ExampleFixedPtIndex_Type()
)
exampleFixedPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtIndex.setStatus("mandatory")
_ExampleFixedPtOperationalTable_Object = MibTable
exampleFixedPtOperationalTable = _ExampleFixedPtOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 10)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperationalTable.setStatus("mandatory")
_ExampleFixedPtOperationalEntry_Object = MibTableRow
exampleFixedPtOperationalEntry = _ExampleFixedPtOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 10, 1)
)
exampleFixedPtOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperationalEntry.setStatus("mandatory")


class _ExampleFixedPtOperStructFixedPt_Type(FixedPoint4):
    """Custom type exampleFixedPtOperStructFixedPt based on FixedPoint4"""
    subtypeSpec = FixedPoint4.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2553300),
    )


_ExampleFixedPtOperStructFixedPt_Type.__name__ = "FixedPoint4"
_ExampleFixedPtOperStructFixedPt_Object = MibTableColumn
exampleFixedPtOperStructFixedPt = _ExampleFixedPtOperStructFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 10, 1, 1),
    _ExampleFixedPtOperStructFixedPt_Type()
)
exampleFixedPtOperStructFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPt.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPt_Type(FixedPoint2):
    """Custom type exampleFixedPtOperFreeFixedPt based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1099),
        ValueRangeConstraint(10001, 20000),
    )


_ExampleFixedPtOperFreeFixedPt_Type.__name__ = "FixedPoint2"
_ExampleFixedPtOperFreeFixedPt_Object = MibTableColumn
exampleFixedPtOperFreeFixedPt = _ExampleFixedPtOperFreeFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 10, 1, 2),
    _ExampleFixedPtOperFreeFixedPt_Type()
)
exampleFixedPtOperFreeFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPt.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtSet_Type(OctetString):
    """Custom type exampleFixedPtOperFreeFixedPtSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ExampleFixedPtOperFreeFixedPtSet_Type.__name__ = "OctetString"
_ExampleFixedPtOperFreeFixedPtSet_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtSet = _ExampleFixedPtOperFreeFixedPtSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 10, 1, 3),
    _ExampleFixedPtOperFreeFixedPtSet_Type()
)
exampleFixedPtOperFreeFixedPtSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtSet.setStatus("mandatory")
_ExampleFixedPtProvisionalTable_Object = MibTable
exampleFixedPtProvisionalTable = _ExampleFixedPtProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvisionalTable.setStatus("mandatory")
_ExampleFixedPtProvisionalEntry_Object = MibTableRow
exampleFixedPtProvisionalEntry = _ExampleFixedPtProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11, 1)
)
exampleFixedPtProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvisionalEntry.setStatus("mandatory")
_ExampleFixedPtProvFixedPtSubcomponent_Type = Link
_ExampleFixedPtProvFixedPtSubcomponent_Object = MibTableColumn
exampleFixedPtProvFixedPtSubcomponent = _ExampleFixedPtProvFixedPtSubcomponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11, 1, 1),
    _ExampleFixedPtProvFixedPtSubcomponent_Type()
)
exampleFixedPtProvFixedPtSubcomponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFixedPtSubcomponent.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPt_Type(FixedPoint3):
    """Custom type exampleFixedPtProvStructFixedPt based on FixedPoint3"""
    defaultValue = 253000

    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252000),
        ValueRangeConstraint(253000, 253000),
        ValueRangeConstraint(254000, 254000),
        ValueRangeConstraint(255000, 255000),
    )


_ExampleFixedPtProvStructFixedPt_Type.__name__ = "FixedPoint3"
_ExampleFixedPtProvStructFixedPt_Object = MibTableColumn
exampleFixedPtProvStructFixedPt = _ExampleFixedPtProvStructFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11, 1, 2),
    _ExampleFixedPtProvStructFixedPt_Type()
)
exampleFixedPtProvStructFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPt.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPtSet_Type(OctetString):
    """Custom type exampleFixedPtProvStructFixedPtSet based on OctetString"""
    defaultHexValue = "c8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExampleFixedPtProvStructFixedPtSet_Type.__name__ = "OctetString"
_ExampleFixedPtProvStructFixedPtSet_Object = MibTableColumn
exampleFixedPtProvStructFixedPtSet = _ExampleFixedPtProvStructFixedPtSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11, 1, 3),
    _ExampleFixedPtProvStructFixedPtSet_Type()
)
exampleFixedPtProvStructFixedPtSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtSet.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPt_Type(FixedPoint2):
    """Custom type exampleFixedPtProvFreeFixedPt based on FixedPoint2"""
    defaultValue = 10101

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1099),
        ValueRangeConstraint(10001, 20099),
    )


_ExampleFixedPtProvFreeFixedPt_Type.__name__ = "FixedPoint2"
_ExampleFixedPtProvFreeFixedPt_Object = MibTableColumn
exampleFixedPtProvFreeFixedPt = _ExampleFixedPtProvFreeFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11, 1, 4),
    _ExampleFixedPtProvFreeFixedPt_Type()
)
exampleFixedPtProvFreeFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPt.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtSet_Type(OctetString):
    """Custom type exampleFixedPtProvFreeFixedPtSet based on OctetString"""
    defaultHexValue = "05500002"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ExampleFixedPtProvFreeFixedPtSet_Type.__name__ = "OctetString"
_ExampleFixedPtProvFreeFixedPtSet_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtSet = _ExampleFixedPtProvFreeFixedPtSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 11, 1, 5),
    _ExampleFixedPtProvFreeFixedPtSet_Type()
)
exampleFixedPtProvFreeFixedPtSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtSet.setStatus("mandatory")
_ExampleFixedPtOperStructFixedPtVectorTable_Object = MibTable
exampleFixedPtOperStructFixedPtVectorTable = _ExampleFixedPtOperStructFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1028)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtVectorTable.setStatus("mandatory")
_ExampleFixedPtOperStructFixedPtVectorEntry_Object = MibTableRow
exampleFixedPtOperStructFixedPtVectorEntry = _ExampleFixedPtOperStructFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1028, 1)
)
exampleFixedPtOperStructFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperStructFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtVectorEntry.setStatus("mandatory")


class _ExampleFixedPtOperStructFixedPtVectorIndex_Type(Integer32):
    """Custom type exampleFixedPtOperStructFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleFixedPtOperStructFixedPtVectorIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperStructFixedPtVectorIndex_Object = MibTableColumn
exampleFixedPtOperStructFixedPtVectorIndex = _ExampleFixedPtOperStructFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1028, 1, 1),
    _ExampleFixedPtOperStructFixedPtVectorIndex_Type()
)
exampleFixedPtOperStructFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtVectorIndex.setStatus("mandatory")


class _ExampleFixedPtOperStructFixedPtVectorValue_Type(FixedPoint3):
    """Custom type exampleFixedPtOperStructFixedPtVectorValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100100),
    )


_ExampleFixedPtOperStructFixedPtVectorValue_Type.__name__ = "FixedPoint3"
_ExampleFixedPtOperStructFixedPtVectorValue_Object = MibTableColumn
exampleFixedPtOperStructFixedPtVectorValue = _ExampleFixedPtOperStructFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1028, 1, 2),
    _ExampleFixedPtOperStructFixedPtVectorValue_Type()
)
exampleFixedPtOperStructFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtVectorValue.setStatus("mandatory")
_ExampleFixedPtOperStructFixedPtArrayTable_Object = MibTable
exampleFixedPtOperStructFixedPtArrayTable = _ExampleFixedPtOperStructFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1029)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtArrayTable.setStatus("mandatory")
_ExampleFixedPtOperStructFixedPtArrayEntry_Object = MibTableRow
exampleFixedPtOperStructFixedPtArrayEntry = _ExampleFixedPtOperStructFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1029, 1)
)
exampleFixedPtOperStructFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperStructFixedPtArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperStructFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtArrayEntry.setStatus("mandatory")


class _ExampleFixedPtOperStructFixedPtArrayRowIndex_Type(Integer32):
    """Custom type exampleFixedPtOperStructFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleFixedPtOperStructFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperStructFixedPtArrayRowIndex_Object = MibTableColumn
exampleFixedPtOperStructFixedPtArrayRowIndex = _ExampleFixedPtOperStructFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1029, 1, 1),
    _ExampleFixedPtOperStructFixedPtArrayRowIndex_Type()
)
exampleFixedPtOperStructFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtArrayRowIndex.setStatus("mandatory")


class _ExampleFixedPtOperStructFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type exampleFixedPtOperStructFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleFixedPtOperStructFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperStructFixedPtArrayColumnIndex_Object = MibTableColumn
exampleFixedPtOperStructFixedPtArrayColumnIndex = _ExampleFixedPtOperStructFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1029, 1, 2),
    _ExampleFixedPtOperStructFixedPtArrayColumnIndex_Type()
)
exampleFixedPtOperStructFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtArrayColumnIndex.setStatus("mandatory")


class _ExampleFixedPtOperStructFixedPtArrayValue_Type(FixedPoint3):
    """Custom type exampleFixedPtOperStructFixedPtArrayValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 255880),
    )


_ExampleFixedPtOperStructFixedPtArrayValue_Type.__name__ = "FixedPoint3"
_ExampleFixedPtOperStructFixedPtArrayValue_Object = MibTableColumn
exampleFixedPtOperStructFixedPtArrayValue = _ExampleFixedPtOperStructFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1029, 1, 3),
    _ExampleFixedPtOperStructFixedPtArrayValue_Type()
)
exampleFixedPtOperStructFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperStructFixedPtArrayValue.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtVectorTable_Object = MibTable
exampleFixedPtOperFreeFixedPtVectorTable = _ExampleFixedPtOperFreeFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1030)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtVectorTable.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtVectorEntry_Object = MibTableRow
exampleFixedPtOperFreeFixedPtVectorEntry = _ExampleFixedPtOperFreeFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1030, 1)
)
exampleFixedPtOperFreeFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperFreeFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtVectorEntry.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtVectorIndex_Type(Integer32):
    """Custom type exampleFixedPtOperFreeFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleFixedPtOperFreeFixedPtVectorIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperFreeFixedPtVectorIndex_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtVectorIndex = _ExampleFixedPtOperFreeFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1030, 1, 1),
    _ExampleFixedPtOperFreeFixedPtVectorIndex_Type()
)
exampleFixedPtOperFreeFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtVectorIndex.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtVectorValue_Type(FixedPoint2):
    """Custom type exampleFixedPtOperFreeFixedPtVectorValue based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ExampleFixedPtOperFreeFixedPtVectorValue_Type.__name__ = "FixedPoint2"
_ExampleFixedPtOperFreeFixedPtVectorValue_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtVectorValue = _ExampleFixedPtOperFreeFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1030, 1, 2),
    _ExampleFixedPtOperFreeFixedPtVectorValue_Type()
)
exampleFixedPtOperFreeFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtVectorValue.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtArrayTable_Object = MibTable
exampleFixedPtOperFreeFixedPtArrayTable = _ExampleFixedPtOperFreeFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1031)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtArrayTable.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtArrayEntry_Object = MibTableRow
exampleFixedPtOperFreeFixedPtArrayEntry = _ExampleFixedPtOperFreeFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1031, 1)
)
exampleFixedPtOperFreeFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperFreeFixedPtArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperFreeFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtArrayEntry.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtArrayRowIndex_Type(Integer32):
    """Custom type exampleFixedPtOperFreeFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleFixedPtOperFreeFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperFreeFixedPtArrayRowIndex_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtArrayRowIndex = _ExampleFixedPtOperFreeFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1031, 1, 1),
    _ExampleFixedPtOperFreeFixedPtArrayRowIndex_Type()
)
exampleFixedPtOperFreeFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtArrayRowIndex.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type exampleFixedPtOperFreeFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleFixedPtOperFreeFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperFreeFixedPtArrayColumnIndex_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtArrayColumnIndex = _ExampleFixedPtOperFreeFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1031, 1, 2),
    _ExampleFixedPtOperFreeFixedPtArrayColumnIndex_Type()
)
exampleFixedPtOperFreeFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtArrayColumnIndex.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtArrayValue_Type(FixedPoint3):
    """Custom type exampleFixedPtOperFreeFixedPtArrayValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 255),
    )


_ExampleFixedPtOperFreeFixedPtArrayValue_Type.__name__ = "FixedPoint3"
_ExampleFixedPtOperFreeFixedPtArrayValue_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtArrayValue = _ExampleFixedPtOperFreeFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1031, 1, 3),
    _ExampleFixedPtOperFreeFixedPtArrayValue_Type()
)
exampleFixedPtOperFreeFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtArrayValue.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtReplicatedTable_Object = MibTable
exampleFixedPtOperFreeFixedPtReplicatedTable = _ExampleFixedPtOperFreeFixedPtReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1032)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtReplicatedTable.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtReplicatedEntry_Object = MibTableRow
exampleFixedPtOperFreeFixedPtReplicatedEntry = _ExampleFixedPtOperFreeFixedPtReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1032, 1)
)
exampleFixedPtOperFreeFixedPtReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperFreeFixedPtReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtReplicatedEntry.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtReplicatedIndex_Type(Integer32):
    """Custom type exampleFixedPtOperFreeFixedPtReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleFixedPtOperFreeFixedPtReplicatedIndex_Type.__name__ = "Integer32"
_ExampleFixedPtOperFreeFixedPtReplicatedIndex_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtReplicatedIndex = _ExampleFixedPtOperFreeFixedPtReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1032, 1, 1),
    _ExampleFixedPtOperFreeFixedPtReplicatedIndex_Type()
)
exampleFixedPtOperFreeFixedPtReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtReplicatedIndex.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtReplicatedValue_Type(FixedPoint1):
    """Custom type exampleFixedPtOperFreeFixedPtReplicatedValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655350),
    )


_ExampleFixedPtOperFreeFixedPtReplicatedValue_Type.__name__ = "FixedPoint1"
_ExampleFixedPtOperFreeFixedPtReplicatedValue_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtReplicatedValue = _ExampleFixedPtOperFreeFixedPtReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1032, 1, 2),
    _ExampleFixedPtOperFreeFixedPtReplicatedValue_Type()
)
exampleFixedPtOperFreeFixedPtReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtReplicatedValue.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Type = RowStatus
_ExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtReplicatedRowStatus = _ExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1032, 1, 3),
    _ExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Type()
)
exampleFixedPtOperFreeFixedPtReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtReplicatedRowStatus.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtListTable_Object = MibTable
exampleFixedPtOperFreeFixedPtListTable = _ExampleFixedPtOperFreeFixedPtListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1033)
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtListTable.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtListEntry_Object = MibTableRow
exampleFixedPtOperFreeFixedPtListEntry = _ExampleFixedPtOperFreeFixedPtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1033, 1)
)
exampleFixedPtOperFreeFixedPtListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtOperFreeFixedPtListValue"),
)
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtListEntry.setStatus("mandatory")


class _ExampleFixedPtOperFreeFixedPtListValue_Type(Integer32):
    """Custom type exampleFixedPtOperFreeFixedPtListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(10000, 20000),
    )


_ExampleFixedPtOperFreeFixedPtListValue_Type.__name__ = "Integer32"
_ExampleFixedPtOperFreeFixedPtListValue_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtListValue = _ExampleFixedPtOperFreeFixedPtListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1033, 1, 1),
    _ExampleFixedPtOperFreeFixedPtListValue_Type()
)
exampleFixedPtOperFreeFixedPtListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtListValue.setStatus("mandatory")
_ExampleFixedPtOperFreeFixedPtListRowStatus_Type = RowStatus
_ExampleFixedPtOperFreeFixedPtListRowStatus_Object = MibTableColumn
exampleFixedPtOperFreeFixedPtListRowStatus = _ExampleFixedPtOperFreeFixedPtListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1033, 1, 2),
    _ExampleFixedPtOperFreeFixedPtListRowStatus_Type()
)
exampleFixedPtOperFreeFixedPtListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleFixedPtOperFreeFixedPtListRowStatus.setStatus("mandatory")
_ExampleFixedPtProvStructFixedPtVectorTable_Object = MibTable
exampleFixedPtProvStructFixedPtVectorTable = _ExampleFixedPtProvStructFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1034)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtVectorTable.setStatus("mandatory")
_ExampleFixedPtProvStructFixedPtVectorEntry_Object = MibTableRow
exampleFixedPtProvStructFixedPtVectorEntry = _ExampleFixedPtProvStructFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1034, 1)
)
exampleFixedPtProvStructFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvStructFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtVectorEntry.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPtVectorIndex_Type(Integer32):
    """Custom type exampleFixedPtProvStructFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleFixedPtProvStructFixedPtVectorIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvStructFixedPtVectorIndex_Object = MibTableColumn
exampleFixedPtProvStructFixedPtVectorIndex = _ExampleFixedPtProvStructFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1034, 1, 1),
    _ExampleFixedPtProvStructFixedPtVectorIndex_Type()
)
exampleFixedPtProvStructFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtVectorIndex.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPtVectorValue_Type(FixedPoint3):
    """Custom type exampleFixedPtProvStructFixedPtVectorValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100100),
    )


_ExampleFixedPtProvStructFixedPtVectorValue_Type.__name__ = "FixedPoint3"
_ExampleFixedPtProvStructFixedPtVectorValue_Object = MibTableColumn
exampleFixedPtProvStructFixedPtVectorValue = _ExampleFixedPtProvStructFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1034, 1, 2),
    _ExampleFixedPtProvStructFixedPtVectorValue_Type()
)
exampleFixedPtProvStructFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtVectorValue.setStatus("mandatory")
_ExampleFixedPtProvStructFixedPtArrayTable_Object = MibTable
exampleFixedPtProvStructFixedPtArrayTable = _ExampleFixedPtProvStructFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1035)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtArrayTable.setStatus("mandatory")
_ExampleFixedPtProvStructFixedPtArrayEntry_Object = MibTableRow
exampleFixedPtProvStructFixedPtArrayEntry = _ExampleFixedPtProvStructFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1035, 1)
)
exampleFixedPtProvStructFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvStructFixedPtArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvStructFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtArrayEntry.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPtArrayRowIndex_Type(Integer32):
    """Custom type exampleFixedPtProvStructFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleFixedPtProvStructFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvStructFixedPtArrayRowIndex_Object = MibTableColumn
exampleFixedPtProvStructFixedPtArrayRowIndex = _ExampleFixedPtProvStructFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1035, 1, 1),
    _ExampleFixedPtProvStructFixedPtArrayRowIndex_Type()
)
exampleFixedPtProvStructFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtArrayRowIndex.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type exampleFixedPtProvStructFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleFixedPtProvStructFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvStructFixedPtArrayColumnIndex_Object = MibTableColumn
exampleFixedPtProvStructFixedPtArrayColumnIndex = _ExampleFixedPtProvStructFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1035, 1, 2),
    _ExampleFixedPtProvStructFixedPtArrayColumnIndex_Type()
)
exampleFixedPtProvStructFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtArrayColumnIndex.setStatus("mandatory")


class _ExampleFixedPtProvStructFixedPtArrayValue_Type(FixedPoint1):
    """Custom type exampleFixedPtProvStructFixedPtArrayValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 300),
    )


_ExampleFixedPtProvStructFixedPtArrayValue_Type.__name__ = "FixedPoint1"
_ExampleFixedPtProvStructFixedPtArrayValue_Object = MibTableColumn
exampleFixedPtProvStructFixedPtArrayValue = _ExampleFixedPtProvStructFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1035, 1, 3),
    _ExampleFixedPtProvStructFixedPtArrayValue_Type()
)
exampleFixedPtProvStructFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvStructFixedPtArrayValue.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtVectorTable_Object = MibTable
exampleFixedPtProvFreeFixedPtVectorTable = _ExampleFixedPtProvFreeFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1036)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtVectorTable.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtVectorEntry_Object = MibTableRow
exampleFixedPtProvFreeFixedPtVectorEntry = _ExampleFixedPtProvFreeFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1036, 1)
)
exampleFixedPtProvFreeFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvFreeFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtVectorEntry.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtVectorIndex_Type(Integer32):
    """Custom type exampleFixedPtProvFreeFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleFixedPtProvFreeFixedPtVectorIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvFreeFixedPtVectorIndex_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtVectorIndex = _ExampleFixedPtProvFreeFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1036, 1, 1),
    _ExampleFixedPtProvFreeFixedPtVectorIndex_Type()
)
exampleFixedPtProvFreeFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtVectorIndex.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtVectorValue_Type(FixedPoint1):
    """Custom type exampleFixedPtProvFreeFixedPtVectorValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ExampleFixedPtProvFreeFixedPtVectorValue_Type.__name__ = "FixedPoint1"
_ExampleFixedPtProvFreeFixedPtVectorValue_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtVectorValue = _ExampleFixedPtProvFreeFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1036, 1, 2),
    _ExampleFixedPtProvFreeFixedPtVectorValue_Type()
)
exampleFixedPtProvFreeFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtVectorValue.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtArrayTable_Object = MibTable
exampleFixedPtProvFreeFixedPtArrayTable = _ExampleFixedPtProvFreeFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1037)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtArrayTable.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtArrayEntry_Object = MibTableRow
exampleFixedPtProvFreeFixedPtArrayEntry = _ExampleFixedPtProvFreeFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1037, 1)
)
exampleFixedPtProvFreeFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvFreeFixedPtArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvFreeFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtArrayEntry.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtArrayRowIndex_Type(Integer32):
    """Custom type exampleFixedPtProvFreeFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleFixedPtProvFreeFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvFreeFixedPtArrayRowIndex_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtArrayRowIndex = _ExampleFixedPtProvFreeFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1037, 1, 1),
    _ExampleFixedPtProvFreeFixedPtArrayRowIndex_Type()
)
exampleFixedPtProvFreeFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtArrayRowIndex.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type exampleFixedPtProvFreeFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleFixedPtProvFreeFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvFreeFixedPtArrayColumnIndex_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtArrayColumnIndex = _ExampleFixedPtProvFreeFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1037, 1, 2),
    _ExampleFixedPtProvFreeFixedPtArrayColumnIndex_Type()
)
exampleFixedPtProvFreeFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtArrayColumnIndex.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtArrayValue_Type(FixedPoint2):
    """Custom type exampleFixedPtProvFreeFixedPtArrayValue based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25555),
    )


_ExampleFixedPtProvFreeFixedPtArrayValue_Type.__name__ = "FixedPoint2"
_ExampleFixedPtProvFreeFixedPtArrayValue_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtArrayValue = _ExampleFixedPtProvFreeFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1037, 1, 3),
    _ExampleFixedPtProvFreeFixedPtArrayValue_Type()
)
exampleFixedPtProvFreeFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtArrayValue.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtReplicatedTable_Object = MibTable
exampleFixedPtProvFreeFixedPtReplicatedTable = _ExampleFixedPtProvFreeFixedPtReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1038)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtReplicatedTable.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtReplicatedEntry_Object = MibTableRow
exampleFixedPtProvFreeFixedPtReplicatedEntry = _ExampleFixedPtProvFreeFixedPtReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1038, 1)
)
exampleFixedPtProvFreeFixedPtReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvFreeFixedPtReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtReplicatedEntry.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtReplicatedIndex_Type(Integer32):
    """Custom type exampleFixedPtProvFreeFixedPtReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleFixedPtProvFreeFixedPtReplicatedIndex_Type.__name__ = "Integer32"
_ExampleFixedPtProvFreeFixedPtReplicatedIndex_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtReplicatedIndex = _ExampleFixedPtProvFreeFixedPtReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1038, 1, 1),
    _ExampleFixedPtProvFreeFixedPtReplicatedIndex_Type()
)
exampleFixedPtProvFreeFixedPtReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtReplicatedIndex.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtReplicatedValue_Type(FixedPoint2):
    """Custom type exampleFixedPtProvFreeFixedPtReplicatedValue based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExampleFixedPtProvFreeFixedPtReplicatedValue_Type.__name__ = "FixedPoint2"
_ExampleFixedPtProvFreeFixedPtReplicatedValue_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtReplicatedValue = _ExampleFixedPtProvFreeFixedPtReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1038, 1, 2),
    _ExampleFixedPtProvFreeFixedPtReplicatedValue_Type()
)
exampleFixedPtProvFreeFixedPtReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtReplicatedValue.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Type = RowStatus
_ExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtReplicatedRowStatus = _ExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1038, 1, 3),
    _ExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Type()
)
exampleFixedPtProvFreeFixedPtReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtReplicatedRowStatus.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtListTable_Object = MibTable
exampleFixedPtProvFreeFixedPtListTable = _ExampleFixedPtProvFreeFixedPtListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1039)
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtListTable.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtListEntry_Object = MibTableRow
exampleFixedPtProvFreeFixedPtListEntry = _ExampleFixedPtProvFreeFixedPtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1039, 1)
)
exampleFixedPtProvFreeFixedPtListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFixedPtProvFreeFixedPtListValue"),
)
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtListEntry.setStatus("mandatory")


class _ExampleFixedPtProvFreeFixedPtListValue_Type(Integer32):
    """Custom type exampleFixedPtProvFreeFixedPtListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_ExampleFixedPtProvFreeFixedPtListValue_Type.__name__ = "Integer32"
_ExampleFixedPtProvFreeFixedPtListValue_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtListValue = _ExampleFixedPtProvFreeFixedPtListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1039, 1, 1),
    _ExampleFixedPtProvFreeFixedPtListValue_Type()
)
exampleFixedPtProvFreeFixedPtListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtListValue.setStatus("mandatory")
_ExampleFixedPtProvFreeFixedPtListRowStatus_Type = RowStatus
_ExampleFixedPtProvFreeFixedPtListRowStatus_Object = MibTableColumn
exampleFixedPtProvFreeFixedPtListRowStatus = _ExampleFixedPtProvFreeFixedPtListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 6, 1039, 1, 2),
    _ExampleFixedPtProvFreeFixedPtListRowStatus_Type()
)
exampleFixedPtProvFreeFixedPtListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleFixedPtProvFreeFixedPtListRowStatus.setStatus("mandatory")
_ExampleDashed_ObjectIdentity = ObjectIdentity
exampleDashed = _ExampleDashed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7)
)
_ExampleDashedRowStatusTable_Object = MibTable
exampleDashedRowStatusTable = _ExampleDashedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1)
)
if mibBuilder.loadTexts:
    exampleDashedRowStatusTable.setStatus("mandatory")
_ExampleDashedRowStatusEntry_Object = MibTableRow
exampleDashedRowStatusEntry = _ExampleDashedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1, 1)
)
exampleDashedRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedRowStatusEntry.setStatus("mandatory")
_ExampleDashedRowStatus_Type = RowStatus
_ExampleDashedRowStatus_Object = MibTableColumn
exampleDashedRowStatus = _ExampleDashedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1, 1, 1),
    _ExampleDashedRowStatus_Type()
)
exampleDashedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedRowStatus.setStatus("mandatory")
_ExampleDashedComponentName_Type = DisplayString
_ExampleDashedComponentName_Object = MibTableColumn
exampleDashedComponentName = _ExampleDashedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1, 1, 2),
    _ExampleDashedComponentName_Type()
)
exampleDashedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDashedComponentName.setStatus("mandatory")
_ExampleDashedStorageType_Type = StorageType
_ExampleDashedStorageType_Object = MibTableColumn
exampleDashedStorageType = _ExampleDashedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1, 1, 4),
    _ExampleDashedStorageType_Type()
)
exampleDashedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDashedStorageType.setStatus("mandatory")


class _ExampleDashedIndex_Type(DashedHexString):
    """Custom type exampleDashedIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedIndex_Type.__name__ = "DashedHexString"
_ExampleDashedIndex_Object = MibTableColumn
exampleDashedIndex = _ExampleDashedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1, 1, 10),
    _ExampleDashedIndex_Type()
)
exampleDashedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedIndex.setStatus("mandatory")
_ExampleDashedOperationalTable_Object = MibTable
exampleDashedOperationalTable = _ExampleDashedOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 10)
)
if mibBuilder.loadTexts:
    exampleDashedOperationalTable.setStatus("mandatory")
_ExampleDashedOperationalEntry_Object = MibTableRow
exampleDashedOperationalEntry = _ExampleDashedOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 10, 1)
)
exampleDashedOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedOperationalEntry.setStatus("mandatory")


class _ExampleDashedOperStructDashed_Type(DashedHexString):
    """Custom type exampleDashedOperStructDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedOperStructDashed_Type.__name__ = "DashedHexString"
_ExampleDashedOperStructDashed_Object = MibTableColumn
exampleDashedOperStructDashed = _ExampleDashedOperStructDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 10, 1, 1),
    _ExampleDashedOperStructDashed_Type()
)
exampleDashedOperStructDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOperStructDashed.setStatus("mandatory")


class _ExampleDashedOperFreeDashed_Type(DashedHexString):
    """Custom type exampleDashedOperFreeDashed based on DashedHexString"""
    defaultHexValue = "123456"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedOperFreeDashed_Type.__name__ = "DashedHexString"
_ExampleDashedOperFreeDashed_Object = MibTableColumn
exampleDashedOperFreeDashed = _ExampleDashedOperFreeDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 10, 1, 2),
    _ExampleDashedOperFreeDashed_Type()
)
exampleDashedOperFreeDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOperFreeDashed.setStatus("mandatory")
_ExampleDashedProvisionalTable_Object = MibTable
exampleDashedProvisionalTable = _ExampleDashedProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 11)
)
if mibBuilder.loadTexts:
    exampleDashedProvisionalTable.setStatus("mandatory")
_ExampleDashedProvisionalEntry_Object = MibTableRow
exampleDashedProvisionalEntry = _ExampleDashedProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 11, 1)
)
exampleDashedProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedProvisionalEntry.setStatus("mandatory")


class _ExampleDashedProvStructDashed_Type(DashedHexString):
    """Custom type exampleDashedProvStructDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedProvStructDashed_Type.__name__ = "DashedHexString"
_ExampleDashedProvStructDashed_Object = MibTableColumn
exampleDashedProvStructDashed = _ExampleDashedProvStructDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 11, 1, 1),
    _ExampleDashedProvStructDashed_Type()
)
exampleDashedProvStructDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvStructDashed.setStatus("mandatory")


class _ExampleDashedProvFreeDashed_Type(DashedHexString):
    """Custom type exampleDashedProvFreeDashed based on DashedHexString"""
    defaultHexValue = "123456"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedProvFreeDashed_Type.__name__ = "DashedHexString"
_ExampleDashedProvFreeDashed_Object = MibTableColumn
exampleDashedProvFreeDashed = _ExampleDashedProvFreeDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 11, 1, 2),
    _ExampleDashedProvFreeDashed_Type()
)
exampleDashedProvFreeDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashed.setStatus("mandatory")
_ExampleDashedOsDashedArrayTable_Object = MibTable
exampleDashedOsDashedArrayTable = _ExampleDashedOsDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1088)
)
if mibBuilder.loadTexts:
    exampleDashedOsDashedArrayTable.setStatus("mandatory")
_ExampleDashedOsDashedArrayEntry_Object = MibTableRow
exampleDashedOsDashedArrayEntry = _ExampleDashedOsDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1088, 1)
)
exampleDashedOsDashedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOsDashedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOsDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedOsDashedArrayEntry.setStatus("mandatory")


class _ExampleDashedOsDashedArrayRowIndex_Type(Integer32):
    """Custom type exampleDashedOsDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDashedOsDashedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDashedOsDashedArrayRowIndex_Object = MibTableColumn
exampleDashedOsDashedArrayRowIndex = _ExampleDashedOsDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1088, 1, 1),
    _ExampleDashedOsDashedArrayRowIndex_Type()
)
exampleDashedOsDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOsDashedArrayRowIndex.setStatus("mandatory")


class _ExampleDashedOsDashedArrayColumnIndex_Type(Integer32):
    """Custom type exampleDashedOsDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDashedOsDashedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDashedOsDashedArrayColumnIndex_Object = MibTableColumn
exampleDashedOsDashedArrayColumnIndex = _ExampleDashedOsDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1088, 1, 2),
    _ExampleDashedOsDashedArrayColumnIndex_Type()
)
exampleDashedOsDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOsDashedArrayColumnIndex.setStatus("mandatory")


class _ExampleDashedOsDashedArrayValue_Type(DashedHexString):
    """Custom type exampleDashedOsDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedOsDashedArrayValue_Type.__name__ = "DashedHexString"
_ExampleDashedOsDashedArrayValue_Object = MibTableColumn
exampleDashedOsDashedArrayValue = _ExampleDashedOsDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1088, 1, 3),
    _ExampleDashedOsDashedArrayValue_Type()
)
exampleDashedOsDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOsDashedArrayValue.setStatus("mandatory")
_ExampleDashedOsDashedVectorTable_Object = MibTable
exampleDashedOsDashedVectorTable = _ExampleDashedOsDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1089)
)
if mibBuilder.loadTexts:
    exampleDashedOsDashedVectorTable.setStatus("mandatory")
_ExampleDashedOsDashedVectorEntry_Object = MibTableRow
exampleDashedOsDashedVectorEntry = _ExampleDashedOsDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1089, 1)
)
exampleDashedOsDashedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOsDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedOsDashedVectorEntry.setStatus("mandatory")


class _ExampleDashedOsDashedVectorIndex_Type(Integer32):
    """Custom type exampleDashedOsDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDashedOsDashedVectorIndex_Type.__name__ = "Integer32"
_ExampleDashedOsDashedVectorIndex_Object = MibTableColumn
exampleDashedOsDashedVectorIndex = _ExampleDashedOsDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1089, 1, 1),
    _ExampleDashedOsDashedVectorIndex_Type()
)
exampleDashedOsDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOsDashedVectorIndex.setStatus("mandatory")


class _ExampleDashedOsDashedVectorValue_Type(DashedHexString):
    """Custom type exampleDashedOsDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedOsDashedVectorValue_Type.__name__ = "DashedHexString"
_ExampleDashedOsDashedVectorValue_Object = MibTableColumn
exampleDashedOsDashedVectorValue = _ExampleDashedOsDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1089, 1, 2),
    _ExampleDashedOsDashedVectorValue_Type()
)
exampleDashedOsDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOsDashedVectorValue.setStatus("mandatory")
_ExampleDashedOfDashedListTable_Object = MibTable
exampleDashedOfDashedListTable = _ExampleDashedOfDashedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1090)
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedListTable.setStatus("mandatory")
_ExampleDashedOfDashedListEntry_Object = MibTableRow
exampleDashedOfDashedListEntry = _ExampleDashedOfDashedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1090, 1)
)
exampleDashedOfDashedListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOfDashedListValue"),
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedListEntry.setStatus("mandatory")


class _ExampleDashedOfDashedListValue_Type(DashedHexString):
    """Custom type exampleDashedOfDashedListValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedOfDashedListValue_Type.__name__ = "DashedHexString"
_ExampleDashedOfDashedListValue_Object = MibTableColumn
exampleDashedOfDashedListValue = _ExampleDashedOfDashedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1090, 1, 1),
    _ExampleDashedOfDashedListValue_Type()
)
exampleDashedOfDashedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOfDashedListValue.setStatus("mandatory")
_ExampleDashedOfDashedListRowStatus_Type = RowStatus
_ExampleDashedOfDashedListRowStatus_Object = MibTableColumn
exampleDashedOfDashedListRowStatus = _ExampleDashedOfDashedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1090, 1, 2),
    _ExampleDashedOfDashedListRowStatus_Type()
)
exampleDashedOfDashedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDashedOfDashedListRowStatus.setStatus("mandatory")
_ExampleDashedOfDashedReplicatedTable_Object = MibTable
exampleDashedOfDashedReplicatedTable = _ExampleDashedOfDashedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1091)
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedReplicatedTable.setStatus("mandatory")
_ExampleDashedOfDashedReplicatedEntry_Object = MibTableRow
exampleDashedOfDashedReplicatedEntry = _ExampleDashedOfDashedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1091, 1)
)
exampleDashedOfDashedReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOfDashedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedReplicatedEntry.setStatus("mandatory")


class _ExampleDashedOfDashedReplicatedIndex_Type(DashedHexString):
    """Custom type exampleDashedOfDashedReplicatedIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedOfDashedReplicatedIndex_Type.__name__ = "DashedHexString"
_ExampleDashedOfDashedReplicatedIndex_Object = MibTableColumn
exampleDashedOfDashedReplicatedIndex = _ExampleDashedOfDashedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1091, 1, 1),
    _ExampleDashedOfDashedReplicatedIndex_Type()
)
exampleDashedOfDashedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOfDashedReplicatedIndex.setStatus("mandatory")


class _ExampleDashedOfDashedReplicatedValue_Type(DashedHexString):
    """Custom type exampleDashedOfDashedReplicatedValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedOfDashedReplicatedValue_Type.__name__ = "DashedHexString"
_ExampleDashedOfDashedReplicatedValue_Object = MibTableColumn
exampleDashedOfDashedReplicatedValue = _ExampleDashedOfDashedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1091, 1, 2),
    _ExampleDashedOfDashedReplicatedValue_Type()
)
exampleDashedOfDashedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOfDashedReplicatedValue.setStatus("mandatory")
_ExampleDashedOfDashedReplicatedRowStatus_Type = RowStatus
_ExampleDashedOfDashedReplicatedRowStatus_Object = MibTableColumn
exampleDashedOfDashedReplicatedRowStatus = _ExampleDashedOfDashedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1091, 1, 3),
    _ExampleDashedOfDashedReplicatedRowStatus_Type()
)
exampleDashedOfDashedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDashedOfDashedReplicatedRowStatus.setStatus("mandatory")
_ExampleDashedOfDashedArrayTable_Object = MibTable
exampleDashedOfDashedArrayTable = _ExampleDashedOfDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1092)
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedArrayTable.setStatus("mandatory")
_ExampleDashedOfDashedArrayEntry_Object = MibTableRow
exampleDashedOfDashedArrayEntry = _ExampleDashedOfDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1092, 1)
)
exampleDashedOfDashedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOfDashedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOfDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedArrayEntry.setStatus("mandatory")


class _ExampleDashedOfDashedArrayRowIndex_Type(Integer32):
    """Custom type exampleDashedOfDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDashedOfDashedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDashedOfDashedArrayRowIndex_Object = MibTableColumn
exampleDashedOfDashedArrayRowIndex = _ExampleDashedOfDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1092, 1, 1),
    _ExampleDashedOfDashedArrayRowIndex_Type()
)
exampleDashedOfDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOfDashedArrayRowIndex.setStatus("mandatory")


class _ExampleDashedOfDashedArrayColumnIndex_Type(Integer32):
    """Custom type exampleDashedOfDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDashedOfDashedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDashedOfDashedArrayColumnIndex_Object = MibTableColumn
exampleDashedOfDashedArrayColumnIndex = _ExampleDashedOfDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1092, 1, 2),
    _ExampleDashedOfDashedArrayColumnIndex_Type()
)
exampleDashedOfDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOfDashedArrayColumnIndex.setStatus("mandatory")


class _ExampleDashedOfDashedArrayValue_Type(DashedHexString):
    """Custom type exampleDashedOfDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedOfDashedArrayValue_Type.__name__ = "DashedHexString"
_ExampleDashedOfDashedArrayValue_Object = MibTableColumn
exampleDashedOfDashedArrayValue = _ExampleDashedOfDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1092, 1, 3),
    _ExampleDashedOfDashedArrayValue_Type()
)
exampleDashedOfDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOfDashedArrayValue.setStatus("mandatory")
_ExampleDashedOfDashedVectorTable_Object = MibTable
exampleDashedOfDashedVectorTable = _ExampleDashedOfDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1093)
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedVectorTable.setStatus("mandatory")
_ExampleDashedOfDashedVectorEntry_Object = MibTableRow
exampleDashedOfDashedVectorEntry = _ExampleDashedOfDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1093, 1)
)
exampleDashedOfDashedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedOfDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedOfDashedVectorEntry.setStatus("mandatory")


class _ExampleDashedOfDashedVectorIndex_Type(Integer32):
    """Custom type exampleDashedOfDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDashedOfDashedVectorIndex_Type.__name__ = "Integer32"
_ExampleDashedOfDashedVectorIndex_Object = MibTableColumn
exampleDashedOfDashedVectorIndex = _ExampleDashedOfDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1093, 1, 1),
    _ExampleDashedOfDashedVectorIndex_Type()
)
exampleDashedOfDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedOfDashedVectorIndex.setStatus("mandatory")


class _ExampleDashedOfDashedVectorValue_Type(DashedHexString):
    """Custom type exampleDashedOfDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedOfDashedVectorValue_Type.__name__ = "DashedHexString"
_ExampleDashedOfDashedVectorValue_Object = MibTableColumn
exampleDashedOfDashedVectorValue = _ExampleDashedOfDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1093, 1, 2),
    _ExampleDashedOfDashedVectorValue_Type()
)
exampleDashedOfDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedOfDashedVectorValue.setStatus("mandatory")
_ExampleDashedProvStructDashedArrayTable_Object = MibTable
exampleDashedProvStructDashedArrayTable = _ExampleDashedProvStructDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1094)
)
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedArrayTable.setStatus("mandatory")
_ExampleDashedProvStructDashedArrayEntry_Object = MibTableRow
exampleDashedProvStructDashedArrayEntry = _ExampleDashedProvStructDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1094, 1)
)
exampleDashedProvStructDashedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvStructDashedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvStructDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedArrayEntry.setStatus("mandatory")


class _ExampleDashedProvStructDashedArrayRowIndex_Type(Integer32):
    """Custom type exampleDashedProvStructDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDashedProvStructDashedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDashedProvStructDashedArrayRowIndex_Object = MibTableColumn
exampleDashedProvStructDashedArrayRowIndex = _ExampleDashedProvStructDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1094, 1, 1),
    _ExampleDashedProvStructDashedArrayRowIndex_Type()
)
exampleDashedProvStructDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedArrayRowIndex.setStatus("mandatory")


class _ExampleDashedProvStructDashedArrayColumnIndex_Type(Integer32):
    """Custom type exampleDashedProvStructDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDashedProvStructDashedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDashedProvStructDashedArrayColumnIndex_Object = MibTableColumn
exampleDashedProvStructDashedArrayColumnIndex = _ExampleDashedProvStructDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1094, 1, 2),
    _ExampleDashedProvStructDashedArrayColumnIndex_Type()
)
exampleDashedProvStructDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedArrayColumnIndex.setStatus("mandatory")


class _ExampleDashedProvStructDashedArrayValue_Type(DashedHexString):
    """Custom type exampleDashedProvStructDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleDashedProvStructDashedArrayValue_Type.__name__ = "DashedHexString"
_ExampleDashedProvStructDashedArrayValue_Object = MibTableColumn
exampleDashedProvStructDashedArrayValue = _ExampleDashedProvStructDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1094, 1, 3),
    _ExampleDashedProvStructDashedArrayValue_Type()
)
exampleDashedProvStructDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedArrayValue.setStatus("mandatory")
_ExampleDashedProvStructDashedVectorTable_Object = MibTable
exampleDashedProvStructDashedVectorTable = _ExampleDashedProvStructDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1095)
)
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedVectorTable.setStatus("mandatory")
_ExampleDashedProvStructDashedVectorEntry_Object = MibTableRow
exampleDashedProvStructDashedVectorEntry = _ExampleDashedProvStructDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1095, 1)
)
exampleDashedProvStructDashedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvStructDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedVectorEntry.setStatus("mandatory")


class _ExampleDashedProvStructDashedVectorIndex_Type(Integer32):
    """Custom type exampleDashedProvStructDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDashedProvStructDashedVectorIndex_Type.__name__ = "Integer32"
_ExampleDashedProvStructDashedVectorIndex_Object = MibTableColumn
exampleDashedProvStructDashedVectorIndex = _ExampleDashedProvStructDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1095, 1, 1),
    _ExampleDashedProvStructDashedVectorIndex_Type()
)
exampleDashedProvStructDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedVectorIndex.setStatus("mandatory")


class _ExampleDashedProvStructDashedVectorValue_Type(DashedHexString):
    """Custom type exampleDashedProvStructDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleDashedProvStructDashedVectorValue_Type.__name__ = "DashedHexString"
_ExampleDashedProvStructDashedVectorValue_Object = MibTableColumn
exampleDashedProvStructDashedVectorValue = _ExampleDashedProvStructDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1095, 1, 2),
    _ExampleDashedProvStructDashedVectorValue_Type()
)
exampleDashedProvStructDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvStructDashedVectorValue.setStatus("mandatory")
_ExampleDashedProvFreeDashedListTable_Object = MibTable
exampleDashedProvFreeDashedListTable = _ExampleDashedProvFreeDashedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1096)
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedListTable.setStatus("mandatory")
_ExampleDashedProvFreeDashedListEntry_Object = MibTableRow
exampleDashedProvFreeDashedListEntry = _ExampleDashedProvFreeDashedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1096, 1)
)
exampleDashedProvFreeDashedListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvFreeDashedListValue"),
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedListEntry.setStatus("mandatory")


class _ExampleDashedProvFreeDashedListValue_Type(DashedHexString):
    """Custom type exampleDashedProvFreeDashedListValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedProvFreeDashedListValue_Type.__name__ = "DashedHexString"
_ExampleDashedProvFreeDashedListValue_Object = MibTableColumn
exampleDashedProvFreeDashedListValue = _ExampleDashedProvFreeDashedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1096, 1, 1),
    _ExampleDashedProvFreeDashedListValue_Type()
)
exampleDashedProvFreeDashedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedListValue.setStatus("mandatory")
_ExampleDashedProvFreeDashedListRowStatus_Type = RowStatus
_ExampleDashedProvFreeDashedListRowStatus_Object = MibTableColumn
exampleDashedProvFreeDashedListRowStatus = _ExampleDashedProvFreeDashedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1096, 1, 2),
    _ExampleDashedProvFreeDashedListRowStatus_Type()
)
exampleDashedProvFreeDashedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedListRowStatus.setStatus("mandatory")
_ExampleDashedProvFreeDashedReplicatedTable_Object = MibTable
exampleDashedProvFreeDashedReplicatedTable = _ExampleDashedProvFreeDashedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1097)
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedReplicatedTable.setStatus("mandatory")
_ExampleDashedProvFreeDashedReplicatedEntry_Object = MibTableRow
exampleDashedProvFreeDashedReplicatedEntry = _ExampleDashedProvFreeDashedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1097, 1)
)
exampleDashedProvFreeDashedReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvFreeDashedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedReplicatedEntry.setStatus("mandatory")


class _ExampleDashedProvFreeDashedReplicatedIndex_Type(DashedHexString):
    """Custom type exampleDashedProvFreeDashedReplicatedIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleDashedProvFreeDashedReplicatedIndex_Type.__name__ = "DashedHexString"
_ExampleDashedProvFreeDashedReplicatedIndex_Object = MibTableColumn
exampleDashedProvFreeDashedReplicatedIndex = _ExampleDashedProvFreeDashedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1097, 1, 1),
    _ExampleDashedProvFreeDashedReplicatedIndex_Type()
)
exampleDashedProvFreeDashedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedReplicatedIndex.setStatus("mandatory")


class _ExampleDashedProvFreeDashedReplicatedValue_Type(DashedHexString):
    """Custom type exampleDashedProvFreeDashedReplicatedValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedProvFreeDashedReplicatedValue_Type.__name__ = "DashedHexString"
_ExampleDashedProvFreeDashedReplicatedValue_Object = MibTableColumn
exampleDashedProvFreeDashedReplicatedValue = _ExampleDashedProvFreeDashedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1097, 1, 2),
    _ExampleDashedProvFreeDashedReplicatedValue_Type()
)
exampleDashedProvFreeDashedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedReplicatedValue.setStatus("mandatory")
_ExampleDashedProvFreeDashedReplicatedRowStatus_Type = RowStatus
_ExampleDashedProvFreeDashedReplicatedRowStatus_Object = MibTableColumn
exampleDashedProvFreeDashedReplicatedRowStatus = _ExampleDashedProvFreeDashedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1097, 1, 3),
    _ExampleDashedProvFreeDashedReplicatedRowStatus_Type()
)
exampleDashedProvFreeDashedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedReplicatedRowStatus.setStatus("mandatory")
_ExampleDashedProvFreeDashedArrayTable_Object = MibTable
exampleDashedProvFreeDashedArrayTable = _ExampleDashedProvFreeDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1098)
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedArrayTable.setStatus("mandatory")
_ExampleDashedProvFreeDashedArrayEntry_Object = MibTableRow
exampleDashedProvFreeDashedArrayEntry = _ExampleDashedProvFreeDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1098, 1)
)
exampleDashedProvFreeDashedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvFreeDashedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvFreeDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedArrayEntry.setStatus("mandatory")


class _ExampleDashedProvFreeDashedArrayRowIndex_Type(Integer32):
    """Custom type exampleDashedProvFreeDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleDashedProvFreeDashedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleDashedProvFreeDashedArrayRowIndex_Object = MibTableColumn
exampleDashedProvFreeDashedArrayRowIndex = _ExampleDashedProvFreeDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1098, 1, 1),
    _ExampleDashedProvFreeDashedArrayRowIndex_Type()
)
exampleDashedProvFreeDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedArrayRowIndex.setStatus("mandatory")


class _ExampleDashedProvFreeDashedArrayColumnIndex_Type(Integer32):
    """Custom type exampleDashedProvFreeDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleDashedProvFreeDashedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleDashedProvFreeDashedArrayColumnIndex_Object = MibTableColumn
exampleDashedProvFreeDashedArrayColumnIndex = _ExampleDashedProvFreeDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1098, 1, 2),
    _ExampleDashedProvFreeDashedArrayColumnIndex_Type()
)
exampleDashedProvFreeDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedArrayColumnIndex.setStatus("mandatory")


class _ExampleDashedProvFreeDashedArrayValue_Type(DashedHexString):
    """Custom type exampleDashedProvFreeDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleDashedProvFreeDashedArrayValue_Type.__name__ = "DashedHexString"
_ExampleDashedProvFreeDashedArrayValue_Object = MibTableColumn
exampleDashedProvFreeDashedArrayValue = _ExampleDashedProvFreeDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1098, 1, 3),
    _ExampleDashedProvFreeDashedArrayValue_Type()
)
exampleDashedProvFreeDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedArrayValue.setStatus("mandatory")
_ExampleDashedProvFreeDashedVectorTable_Object = MibTable
exampleDashedProvFreeDashedVectorTable = _ExampleDashedProvFreeDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1099)
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedVectorTable.setStatus("mandatory")
_ExampleDashedProvFreeDashedVectorEntry_Object = MibTableRow
exampleDashedProvFreeDashedVectorEntry = _ExampleDashedProvFreeDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1099, 1)
)
exampleDashedProvFreeDashedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedProvFreeDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedVectorEntry.setStatus("mandatory")


class _ExampleDashedProvFreeDashedVectorIndex_Type(Integer32):
    """Custom type exampleDashedProvFreeDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleDashedProvFreeDashedVectorIndex_Type.__name__ = "Integer32"
_ExampleDashedProvFreeDashedVectorIndex_Object = MibTableColumn
exampleDashedProvFreeDashedVectorIndex = _ExampleDashedProvFreeDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1099, 1, 1),
    _ExampleDashedProvFreeDashedVectorIndex_Type()
)
exampleDashedProvFreeDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedVectorIndex.setStatus("mandatory")


class _ExampleDashedProvFreeDashedVectorValue_Type(DashedHexString):
    """Custom type exampleDashedProvFreeDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleDashedProvFreeDashedVectorValue_Type.__name__ = "DashedHexString"
_ExampleDashedProvFreeDashedVectorValue_Object = MibTableColumn
exampleDashedProvFreeDashedVectorValue = _ExampleDashedProvFreeDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 7, 1099, 1, 2),
    _ExampleDashedProvFreeDashedVectorValue_Type()
)
exampleDashedProvFreeDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedProvFreeDashedVectorValue.setStatus("mandatory")
_ExampleExtended_ObjectIdentity = ObjectIdentity
exampleExtended = _ExampleExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8)
)
_ExampleExtendedRowStatusTable_Object = MibTable
exampleExtendedRowStatusTable = _ExampleExtendedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1)
)
if mibBuilder.loadTexts:
    exampleExtendedRowStatusTable.setStatus("mandatory")
_ExampleExtendedRowStatusEntry_Object = MibTableRow
exampleExtendedRowStatusEntry = _ExampleExtendedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1, 1)
)
exampleExtendedRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedRowStatusEntry.setStatus("mandatory")
_ExampleExtendedRowStatus_Type = RowStatus
_ExampleExtendedRowStatus_Object = MibTableColumn
exampleExtendedRowStatus = _ExampleExtendedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1, 1, 1),
    _ExampleExtendedRowStatus_Type()
)
exampleExtendedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedRowStatus.setStatus("mandatory")
_ExampleExtendedComponentName_Type = DisplayString
_ExampleExtendedComponentName_Object = MibTableColumn
exampleExtendedComponentName = _ExampleExtendedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1, 1, 2),
    _ExampleExtendedComponentName_Type()
)
exampleExtendedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleExtendedComponentName.setStatus("mandatory")
_ExampleExtendedStorageType_Type = StorageType
_ExampleExtendedStorageType_Object = MibTableColumn
exampleExtendedStorageType = _ExampleExtendedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1, 1, 4),
    _ExampleExtendedStorageType_Type()
)
exampleExtendedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleExtendedStorageType.setStatus("mandatory")
_ExampleExtendedIndex_Type = NonReplicated
_ExampleExtendedIndex_Object = MibTableColumn
exampleExtendedIndex = _ExampleExtendedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1, 1, 10),
    _ExampleExtendedIndex_Type()
)
exampleExtendedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedIndex.setStatus("mandatory")
_ExampleExtendedOperationalTable_Object = MibTable
exampleExtendedOperationalTable = _ExampleExtendedOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 10)
)
if mibBuilder.loadTexts:
    exampleExtendedOperationalTable.setStatus("mandatory")
_ExampleExtendedOperationalEntry_Object = MibTableRow
exampleExtendedOperationalEntry = _ExampleExtendedOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 10, 1)
)
exampleExtendedOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperationalEntry.setStatus("mandatory")


class _ExampleExtendedOperStructExtended_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperStructExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleExtendedOperStructExtended_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperStructExtended_Object = MibTableColumn
exampleExtendedOperStructExtended = _ExampleExtendedOperStructExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 10, 1, 1),
    _ExampleExtendedOperStructExtended_Type()
)
exampleExtendedOperStructExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtended.setStatus("mandatory")


class _ExampleExtendedOperFreeExtended_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperFreeExtended based on ExtendedAsciiString"""
    defaultHexValue = "68656c6c6f5c6162"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleExtendedOperFreeExtended_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperFreeExtended_Object = MibTableColumn
exampleExtendedOperFreeExtended = _ExampleExtendedOperFreeExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 10, 1, 2),
    _ExampleExtendedOperFreeExtended_Type()
)
exampleExtendedOperFreeExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtended.setStatus("mandatory")
_ExampleExtendedProvisionalTable_Object = MibTable
exampleExtendedProvisionalTable = _ExampleExtendedProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 11)
)
if mibBuilder.loadTexts:
    exampleExtendedProvisionalTable.setStatus("mandatory")
_ExampleExtendedProvisionalEntry_Object = MibTableRow
exampleExtendedProvisionalEntry = _ExampleExtendedProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 11, 1)
)
exampleExtendedProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvisionalEntry.setStatus("mandatory")
_ExampleExtendedProvEnumSub_Type = Link
_ExampleExtendedProvEnumSub_Object = MibTableColumn
exampleExtendedProvEnumSub = _ExampleExtendedProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 11, 1, 1),
    _ExampleExtendedProvEnumSub_Type()
)
exampleExtendedProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvEnumSub.setStatus("mandatory")


class _ExampleExtendedProvStructExtended_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvStructExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleExtendedProvStructExtended_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvStructExtended_Object = MibTableColumn
exampleExtendedProvStructExtended = _ExampleExtendedProvStructExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 11, 1, 2),
    _ExampleExtendedProvStructExtended_Type()
)
exampleExtendedProvStructExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtended.setStatus("mandatory")


class _ExampleExtendedProvFreeExtended_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvFreeExtended based on ExtendedAsciiString"""
    defaultHexValue = "48656c6c6f5c61626364"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleExtendedProvFreeExtended_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvFreeExtended_Object = MibTableColumn
exampleExtendedProvFreeExtended = _ExampleExtendedProvFreeExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 11, 1, 3),
    _ExampleExtendedProvFreeExtended_Type()
)
exampleExtendedProvFreeExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtended.setStatus("mandatory")
_ExampleExtendedOperStructExtendedArrayTable_Object = MibTable
exampleExtendedOperStructExtendedArrayTable = _ExampleExtendedOperStructExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1100)
)
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedArrayTable.setStatus("mandatory")
_ExampleExtendedOperStructExtendedArrayEntry_Object = MibTableRow
exampleExtendedOperStructExtendedArrayEntry = _ExampleExtendedOperStructExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1100, 1)
)
exampleExtendedOperStructExtendedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperStructExtendedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperStructExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedArrayEntry.setStatus("mandatory")


class _ExampleExtendedOperStructExtendedArrayRowIndex_Type(Integer32):
    """Custom type exampleExtendedOperStructExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleExtendedOperStructExtendedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleExtendedOperStructExtendedArrayRowIndex_Object = MibTableColumn
exampleExtendedOperStructExtendedArrayRowIndex = _ExampleExtendedOperStructExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1100, 1, 1),
    _ExampleExtendedOperStructExtendedArrayRowIndex_Type()
)
exampleExtendedOperStructExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedArrayRowIndex.setStatus("mandatory")


class _ExampleExtendedOperStructExtendedArrayColumnIndex_Type(Integer32):
    """Custom type exampleExtendedOperStructExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleExtendedOperStructExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleExtendedOperStructExtendedArrayColumnIndex_Object = MibTableColumn
exampleExtendedOperStructExtendedArrayColumnIndex = _ExampleExtendedOperStructExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1100, 1, 2),
    _ExampleExtendedOperStructExtendedArrayColumnIndex_Type()
)
exampleExtendedOperStructExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedArrayColumnIndex.setStatus("mandatory")


class _ExampleExtendedOperStructExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperStructExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedOperStructExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperStructExtendedArrayValue_Object = MibTableColumn
exampleExtendedOperStructExtendedArrayValue = _ExampleExtendedOperStructExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1100, 1, 3),
    _ExampleExtendedOperStructExtendedArrayValue_Type()
)
exampleExtendedOperStructExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedArrayValue.setStatus("mandatory")
_ExampleExtendedOperStructExtendedVectorTable_Object = MibTable
exampleExtendedOperStructExtendedVectorTable = _ExampleExtendedOperStructExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1101)
)
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedVectorTable.setStatus("mandatory")
_ExampleExtendedOperStructExtendedVectorEntry_Object = MibTableRow
exampleExtendedOperStructExtendedVectorEntry = _ExampleExtendedOperStructExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1101, 1)
)
exampleExtendedOperStructExtendedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperStructExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedVectorEntry.setStatus("mandatory")


class _ExampleExtendedOperStructExtendedVectorIndex_Type(Integer32):
    """Custom type exampleExtendedOperStructExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleExtendedOperStructExtendedVectorIndex_Type.__name__ = "Integer32"
_ExampleExtendedOperStructExtendedVectorIndex_Object = MibTableColumn
exampleExtendedOperStructExtendedVectorIndex = _ExampleExtendedOperStructExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1101, 1, 1),
    _ExampleExtendedOperStructExtendedVectorIndex_Type()
)
exampleExtendedOperStructExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedVectorIndex.setStatus("mandatory")


class _ExampleExtendedOperStructExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperStructExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedOperStructExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperStructExtendedVectorValue_Object = MibTableColumn
exampleExtendedOperStructExtendedVectorValue = _ExampleExtendedOperStructExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1101, 1, 2),
    _ExampleExtendedOperStructExtendedVectorValue_Type()
)
exampleExtendedOperStructExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperStructExtendedVectorValue.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedListTable_Object = MibTable
exampleExtendedOperFreeExtendedListTable = _ExampleExtendedOperFreeExtendedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1102)
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedListTable.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedListEntry_Object = MibTableRow
exampleExtendedOperFreeExtendedListEntry = _ExampleExtendedOperFreeExtendedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1102, 1)
)
exampleExtendedOperFreeExtendedListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperFreeExtendedListValue"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedListEntry.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedListValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperFreeExtendedListValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedOperFreeExtendedListValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperFreeExtendedListValue_Object = MibTableColumn
exampleExtendedOperFreeExtendedListValue = _ExampleExtendedOperFreeExtendedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1102, 1, 1),
    _ExampleExtendedOperFreeExtendedListValue_Type()
)
exampleExtendedOperFreeExtendedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedListValue.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedListRowStatus_Type = RowStatus
_ExampleExtendedOperFreeExtendedListRowStatus_Object = MibTableColumn
exampleExtendedOperFreeExtendedListRowStatus = _ExampleExtendedOperFreeExtendedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1102, 1, 2),
    _ExampleExtendedOperFreeExtendedListRowStatus_Type()
)
exampleExtendedOperFreeExtendedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedListRowStatus.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedReplicatedTable_Object = MibTable
exampleExtendedOperFreeExtendedReplicatedTable = _ExampleExtendedOperFreeExtendedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1103)
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedReplicatedTable.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedReplicatedEntry_Object = MibTableRow
exampleExtendedOperFreeExtendedReplicatedEntry = _ExampleExtendedOperFreeExtendedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1103, 1)
)
exampleExtendedOperFreeExtendedReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperFreeExtendedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedReplicatedEntry.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedReplicatedIndex_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperFreeExtendedReplicatedIndex based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedOperFreeExtendedReplicatedIndex_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperFreeExtendedReplicatedIndex_Object = MibTableColumn
exampleExtendedOperFreeExtendedReplicatedIndex = _ExampleExtendedOperFreeExtendedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1103, 1, 1),
    _ExampleExtendedOperFreeExtendedReplicatedIndex_Type()
)
exampleExtendedOperFreeExtendedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedReplicatedIndex.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedReplicatedValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperFreeExtendedReplicatedValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleExtendedOperFreeExtendedReplicatedValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperFreeExtendedReplicatedValue_Object = MibTableColumn
exampleExtendedOperFreeExtendedReplicatedValue = _ExampleExtendedOperFreeExtendedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1103, 1, 2),
    _ExampleExtendedOperFreeExtendedReplicatedValue_Type()
)
exampleExtendedOperFreeExtendedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedReplicatedValue.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedReplicatedRowStatus_Type = RowStatus
_ExampleExtendedOperFreeExtendedReplicatedRowStatus_Object = MibTableColumn
exampleExtendedOperFreeExtendedReplicatedRowStatus = _ExampleExtendedOperFreeExtendedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1103, 1, 3),
    _ExampleExtendedOperFreeExtendedReplicatedRowStatus_Type()
)
exampleExtendedOperFreeExtendedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedReplicatedRowStatus.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedArrayTable_Object = MibTable
exampleExtendedOperFreeExtendedArrayTable = _ExampleExtendedOperFreeExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1104)
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedArrayTable.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedArrayEntry_Object = MibTableRow
exampleExtendedOperFreeExtendedArrayEntry = _ExampleExtendedOperFreeExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1104, 1)
)
exampleExtendedOperFreeExtendedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperFreeExtendedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperFreeExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedArrayEntry.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedArrayRowIndex_Type(Integer32):
    """Custom type exampleExtendedOperFreeExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleExtendedOperFreeExtendedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleExtendedOperFreeExtendedArrayRowIndex_Object = MibTableColumn
exampleExtendedOperFreeExtendedArrayRowIndex = _ExampleExtendedOperFreeExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1104, 1, 1),
    _ExampleExtendedOperFreeExtendedArrayRowIndex_Type()
)
exampleExtendedOperFreeExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedArrayRowIndex.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedArrayColumnIndex_Type(Integer32):
    """Custom type exampleExtendedOperFreeExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleExtendedOperFreeExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleExtendedOperFreeExtendedArrayColumnIndex_Object = MibTableColumn
exampleExtendedOperFreeExtendedArrayColumnIndex = _ExampleExtendedOperFreeExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1104, 1, 2),
    _ExampleExtendedOperFreeExtendedArrayColumnIndex_Type()
)
exampleExtendedOperFreeExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedArrayColumnIndex.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperFreeExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedOperFreeExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperFreeExtendedArrayValue_Object = MibTableColumn
exampleExtendedOperFreeExtendedArrayValue = _ExampleExtendedOperFreeExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1104, 1, 3),
    _ExampleExtendedOperFreeExtendedArrayValue_Type()
)
exampleExtendedOperFreeExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedArrayValue.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedVectorTable_Object = MibTable
exampleExtendedOperFreeExtendedVectorTable = _ExampleExtendedOperFreeExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1105)
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedVectorTable.setStatus("mandatory")
_ExampleExtendedOperFreeExtendedVectorEntry_Object = MibTableRow
exampleExtendedOperFreeExtendedVectorEntry = _ExampleExtendedOperFreeExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1105, 1)
)
exampleExtendedOperFreeExtendedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedOperFreeExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedVectorEntry.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedVectorIndex_Type(Integer32):
    """Custom type exampleExtendedOperFreeExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleExtendedOperFreeExtendedVectorIndex_Type.__name__ = "Integer32"
_ExampleExtendedOperFreeExtendedVectorIndex_Object = MibTableColumn
exampleExtendedOperFreeExtendedVectorIndex = _ExampleExtendedOperFreeExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1105, 1, 1),
    _ExampleExtendedOperFreeExtendedVectorIndex_Type()
)
exampleExtendedOperFreeExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedVectorIndex.setStatus("mandatory")


class _ExampleExtendedOperFreeExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedOperFreeExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedOperFreeExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedOperFreeExtendedVectorValue_Object = MibTableColumn
exampleExtendedOperFreeExtendedVectorValue = _ExampleExtendedOperFreeExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1105, 1, 2),
    _ExampleExtendedOperFreeExtendedVectorValue_Type()
)
exampleExtendedOperFreeExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedOperFreeExtendedVectorValue.setStatus("mandatory")
_ExampleExtendedProvStructExtendedArrayTable_Object = MibTable
exampleExtendedProvStructExtendedArrayTable = _ExampleExtendedProvStructExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1106)
)
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedArrayTable.setStatus("mandatory")
_ExampleExtendedProvStructExtendedArrayEntry_Object = MibTableRow
exampleExtendedProvStructExtendedArrayEntry = _ExampleExtendedProvStructExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1106, 1)
)
exampleExtendedProvStructExtendedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvStructExtendedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvStructExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedArrayEntry.setStatus("mandatory")


class _ExampleExtendedProvStructExtendedArrayRowIndex_Type(Integer32):
    """Custom type exampleExtendedProvStructExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleExtendedProvStructExtendedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleExtendedProvStructExtendedArrayRowIndex_Object = MibTableColumn
exampleExtendedProvStructExtendedArrayRowIndex = _ExampleExtendedProvStructExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1106, 1, 1),
    _ExampleExtendedProvStructExtendedArrayRowIndex_Type()
)
exampleExtendedProvStructExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedArrayRowIndex.setStatus("mandatory")


class _ExampleExtendedProvStructExtendedArrayColumnIndex_Type(Integer32):
    """Custom type exampleExtendedProvStructExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleExtendedProvStructExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleExtendedProvStructExtendedArrayColumnIndex_Object = MibTableColumn
exampleExtendedProvStructExtendedArrayColumnIndex = _ExampleExtendedProvStructExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1106, 1, 2),
    _ExampleExtendedProvStructExtendedArrayColumnIndex_Type()
)
exampleExtendedProvStructExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedArrayColumnIndex.setStatus("mandatory")


class _ExampleExtendedProvStructExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvStructExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleExtendedProvStructExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvStructExtendedArrayValue_Object = MibTableColumn
exampleExtendedProvStructExtendedArrayValue = _ExampleExtendedProvStructExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1106, 1, 3),
    _ExampleExtendedProvStructExtendedArrayValue_Type()
)
exampleExtendedProvStructExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedArrayValue.setStatus("mandatory")
_ExampleExtendedProvStructExtendedVectorTable_Object = MibTable
exampleExtendedProvStructExtendedVectorTable = _ExampleExtendedProvStructExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1107)
)
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedVectorTable.setStatus("mandatory")
_ExampleExtendedProvStructExtendedVectorEntry_Object = MibTableRow
exampleExtendedProvStructExtendedVectorEntry = _ExampleExtendedProvStructExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1107, 1)
)
exampleExtendedProvStructExtendedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvStructExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedVectorEntry.setStatus("mandatory")


class _ExampleExtendedProvStructExtendedVectorIndex_Type(Integer32):
    """Custom type exampleExtendedProvStructExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleExtendedProvStructExtendedVectorIndex_Type.__name__ = "Integer32"
_ExampleExtendedProvStructExtendedVectorIndex_Object = MibTableColumn
exampleExtendedProvStructExtendedVectorIndex = _ExampleExtendedProvStructExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1107, 1, 1),
    _ExampleExtendedProvStructExtendedVectorIndex_Type()
)
exampleExtendedProvStructExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedVectorIndex.setStatus("mandatory")


class _ExampleExtendedProvStructExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvStructExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleExtendedProvStructExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvStructExtendedVectorValue_Object = MibTableColumn
exampleExtendedProvStructExtendedVectorValue = _ExampleExtendedProvStructExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1107, 1, 2),
    _ExampleExtendedProvStructExtendedVectorValue_Type()
)
exampleExtendedProvStructExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvStructExtendedVectorValue.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedListTable_Object = MibTable
exampleExtendedProvFreeExtendedListTable = _ExampleExtendedProvFreeExtendedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1108)
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedListTable.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedListEntry_Object = MibTableRow
exampleExtendedProvFreeExtendedListEntry = _ExampleExtendedProvFreeExtendedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1108, 1)
)
exampleExtendedProvFreeExtendedListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvFreeExtendedListValue"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedListEntry.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedListValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvFreeExtendedListValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedProvFreeExtendedListValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvFreeExtendedListValue_Object = MibTableColumn
exampleExtendedProvFreeExtendedListValue = _ExampleExtendedProvFreeExtendedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1108, 1, 1),
    _ExampleExtendedProvFreeExtendedListValue_Type()
)
exampleExtendedProvFreeExtendedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedListValue.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedListRowStatus_Type = RowStatus
_ExampleExtendedProvFreeExtendedListRowStatus_Object = MibTableColumn
exampleExtendedProvFreeExtendedListRowStatus = _ExampleExtendedProvFreeExtendedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1108, 1, 2),
    _ExampleExtendedProvFreeExtendedListRowStatus_Type()
)
exampleExtendedProvFreeExtendedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedListRowStatus.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedReplicatedTable_Object = MibTable
exampleExtendedProvFreeExtendedReplicatedTable = _ExampleExtendedProvFreeExtendedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1109)
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedReplicatedTable.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedReplicatedEntry_Object = MibTableRow
exampleExtendedProvFreeExtendedReplicatedEntry = _ExampleExtendedProvFreeExtendedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1109, 1)
)
exampleExtendedProvFreeExtendedReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvFreeExtendedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedReplicatedEntry.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedReplicatedIndex_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvFreeExtendedReplicatedIndex based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_ExampleExtendedProvFreeExtendedReplicatedIndex_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvFreeExtendedReplicatedIndex_Object = MibTableColumn
exampleExtendedProvFreeExtendedReplicatedIndex = _ExampleExtendedProvFreeExtendedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1109, 1, 1),
    _ExampleExtendedProvFreeExtendedReplicatedIndex_Type()
)
exampleExtendedProvFreeExtendedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedReplicatedIndex.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedReplicatedValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvFreeExtendedReplicatedValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleExtendedProvFreeExtendedReplicatedValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvFreeExtendedReplicatedValue_Object = MibTableColumn
exampleExtendedProvFreeExtendedReplicatedValue = _ExampleExtendedProvFreeExtendedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1109, 1, 2),
    _ExampleExtendedProvFreeExtendedReplicatedValue_Type()
)
exampleExtendedProvFreeExtendedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedReplicatedValue.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedReplicatedRowStatus_Type = RowStatus
_ExampleExtendedProvFreeExtendedReplicatedRowStatus_Object = MibTableColumn
exampleExtendedProvFreeExtendedReplicatedRowStatus = _ExampleExtendedProvFreeExtendedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1109, 1, 3),
    _ExampleExtendedProvFreeExtendedReplicatedRowStatus_Type()
)
exampleExtendedProvFreeExtendedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedReplicatedRowStatus.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedArrayTable_Object = MibTable
exampleExtendedProvFreeExtendedArrayTable = _ExampleExtendedProvFreeExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1110)
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedArrayTable.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedArrayEntry_Object = MibTableRow
exampleExtendedProvFreeExtendedArrayEntry = _ExampleExtendedProvFreeExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1110, 1)
)
exampleExtendedProvFreeExtendedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvFreeExtendedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvFreeExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedArrayEntry.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedArrayRowIndex_Type(Integer32):
    """Custom type exampleExtendedProvFreeExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleExtendedProvFreeExtendedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleExtendedProvFreeExtendedArrayRowIndex_Object = MibTableColumn
exampleExtendedProvFreeExtendedArrayRowIndex = _ExampleExtendedProvFreeExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1110, 1, 1),
    _ExampleExtendedProvFreeExtendedArrayRowIndex_Type()
)
exampleExtendedProvFreeExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedArrayRowIndex.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedArrayColumnIndex_Type(Integer32):
    """Custom type exampleExtendedProvFreeExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleExtendedProvFreeExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleExtendedProvFreeExtendedArrayColumnIndex_Object = MibTableColumn
exampleExtendedProvFreeExtendedArrayColumnIndex = _ExampleExtendedProvFreeExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1110, 1, 2),
    _ExampleExtendedProvFreeExtendedArrayColumnIndex_Type()
)
exampleExtendedProvFreeExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedArrayColumnIndex.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvFreeExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleExtendedProvFreeExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvFreeExtendedArrayValue_Object = MibTableColumn
exampleExtendedProvFreeExtendedArrayValue = _ExampleExtendedProvFreeExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1110, 1, 3),
    _ExampleExtendedProvFreeExtendedArrayValue_Type()
)
exampleExtendedProvFreeExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedArrayValue.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedVectorTable_Object = MibTable
exampleExtendedProvFreeExtendedVectorTable = _ExampleExtendedProvFreeExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1111)
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedVectorTable.setStatus("mandatory")
_ExampleExtendedProvFreeExtendedVectorEntry_Object = MibTableRow
exampleExtendedProvFreeExtendedVectorEntry = _ExampleExtendedProvFreeExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1111, 1)
)
exampleExtendedProvFreeExtendedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleExtendedProvFreeExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedVectorEntry.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedVectorIndex_Type(Integer32):
    """Custom type exampleExtendedProvFreeExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleExtendedProvFreeExtendedVectorIndex_Type.__name__ = "Integer32"
_ExampleExtendedProvFreeExtendedVectorIndex_Object = MibTableColumn
exampleExtendedProvFreeExtendedVectorIndex = _ExampleExtendedProvFreeExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1111, 1, 1),
    _ExampleExtendedProvFreeExtendedVectorIndex_Type()
)
exampleExtendedProvFreeExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedVectorIndex.setStatus("mandatory")


class _ExampleExtendedProvFreeExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type exampleExtendedProvFreeExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleExtendedProvFreeExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_ExampleExtendedProvFreeExtendedVectorValue_Object = MibTableColumn
exampleExtendedProvFreeExtendedVectorValue = _ExampleExtendedProvFreeExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 8, 1111, 1, 2),
    _ExampleExtendedProvFreeExtendedVectorValue_Type()
)
exampleExtendedProvFreeExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleExtendedProvFreeExtendedVectorValue.setStatus("mandatory")
_ExampleBcd_ObjectIdentity = ObjectIdentity
exampleBcd = _ExampleBcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9)
)
_ExampleBcdRowStatusTable_Object = MibTable
exampleBcdRowStatusTable = _ExampleBcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1)
)
if mibBuilder.loadTexts:
    exampleBcdRowStatusTable.setStatus("mandatory")
_ExampleBcdRowStatusEntry_Object = MibTableRow
exampleBcdRowStatusEntry = _ExampleBcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1, 1)
)
exampleBcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdRowStatusEntry.setStatus("mandatory")
_ExampleBcdRowStatus_Type = RowStatus
_ExampleBcdRowStatus_Object = MibTableColumn
exampleBcdRowStatus = _ExampleBcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1, 1, 1),
    _ExampleBcdRowStatus_Type()
)
exampleBcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdRowStatus.setStatus("mandatory")
_ExampleBcdComponentName_Type = DisplayString
_ExampleBcdComponentName_Object = MibTableColumn
exampleBcdComponentName = _ExampleBcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1, 1, 2),
    _ExampleBcdComponentName_Type()
)
exampleBcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleBcdComponentName.setStatus("mandatory")
_ExampleBcdStorageType_Type = StorageType
_ExampleBcdStorageType_Object = MibTableColumn
exampleBcdStorageType = _ExampleBcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1, 1, 4),
    _ExampleBcdStorageType_Type()
)
exampleBcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleBcdStorageType.setStatus("mandatory")


class _ExampleBcdIndex_Type(DigitString):
    """Custom type exampleBcdIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleBcdIndex_Type.__name__ = "DigitString"
_ExampleBcdIndex_Object = MibTableColumn
exampleBcdIndex = _ExampleBcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1, 1, 10),
    _ExampleBcdIndex_Type()
)
exampleBcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdIndex.setStatus("mandatory")
_ExampleBcdOperationalTable_Object = MibTable
exampleBcdOperationalTable = _ExampleBcdOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 10)
)
if mibBuilder.loadTexts:
    exampleBcdOperationalTable.setStatus("mandatory")
_ExampleBcdOperationalEntry_Object = MibTableRow
exampleBcdOperationalEntry = _ExampleBcdOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 10, 1)
)
exampleBcdOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdOperationalEntry.setStatus("mandatory")


class _ExampleBcdOperStructBcd_Type(DigitString):
    """Custom type exampleBcdOperStructBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdOperStructBcd_Type.__name__ = "DigitString"
_ExampleBcdOperStructBcd_Object = MibTableColumn
exampleBcdOperStructBcd = _ExampleBcdOperStructBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 10, 1, 1),
    _ExampleBcdOperStructBcd_Type()
)
exampleBcdOperStructBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperStructBcd.setStatus("mandatory")


class _ExampleBcdOperFreeBcd_Type(DigitString):
    """Custom type exampleBcdOperFreeBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdOperFreeBcd_Type.__name__ = "DigitString"
_ExampleBcdOperFreeBcd_Object = MibTableColumn
exampleBcdOperFreeBcd = _ExampleBcdOperFreeBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 10, 1, 2),
    _ExampleBcdOperFreeBcd_Type()
)
exampleBcdOperFreeBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcd.setStatus("mandatory")
_ExampleBcdProvisionalTable_Object = MibTable
exampleBcdProvisionalTable = _ExampleBcdProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 11)
)
if mibBuilder.loadTexts:
    exampleBcdProvisionalTable.setStatus("mandatory")
_ExampleBcdProvisionalEntry_Object = MibTableRow
exampleBcdProvisionalEntry = _ExampleBcdProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 11, 1)
)
exampleBcdProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvisionalEntry.setStatus("mandatory")
_ExampleBcdProvEnumSub_Type = Link
_ExampleBcdProvEnumSub_Object = MibTableColumn
exampleBcdProvEnumSub = _ExampleBcdProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 11, 1, 1),
    _ExampleBcdProvEnumSub_Type()
)
exampleBcdProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvEnumSub.setStatus("mandatory")


class _ExampleBcdProvStructBcd_Type(DigitString):
    """Custom type exampleBcdProvStructBcd based on DigitString"""
    defaultHexValue = "30313233343536373839"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdProvStructBcd_Type.__name__ = "DigitString"
_ExampleBcdProvStructBcd_Object = MibTableColumn
exampleBcdProvStructBcd = _ExampleBcdProvStructBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 11, 1, 2),
    _ExampleBcdProvStructBcd_Type()
)
exampleBcdProvStructBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvStructBcd.setStatus("mandatory")


class _ExampleBcdProvFreeBcd_Type(DigitString):
    """Custom type exampleBcdProvFreeBcd based on DigitString"""
    defaultHexValue = "31323334353637383930"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_ExampleBcdProvFreeBcd_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcd_Object = MibTableColumn
exampleBcdProvFreeBcd = _ExampleBcdProvFreeBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 11, 1, 3),
    _ExampleBcdProvFreeBcd_Type()
)
exampleBcdProvFreeBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcd.setStatus("mandatory")


class _ExampleBcdProvFreeBcd1_Type(DigitString):
    """Custom type exampleBcdProvFreeBcd1 based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_ExampleBcdProvFreeBcd1_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcd1_Object = MibTableColumn
exampleBcdProvFreeBcd1 = _ExampleBcdProvFreeBcd1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 11, 1, 4),
    _ExampleBcdProvFreeBcd1_Type()
)
exampleBcdProvFreeBcd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcd1.setStatus("mandatory")
_ExampleBcdOperStructBcdVectorTable_Object = MibTable
exampleBcdOperStructBcdVectorTable = _ExampleBcdOperStructBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1120)
)
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdVectorTable.setStatus("mandatory")
_ExampleBcdOperStructBcdVectorEntry_Object = MibTableRow
exampleBcdOperStructBcdVectorEntry = _ExampleBcdOperStructBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1120, 1)
)
exampleBcdOperStructBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperStructBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdVectorEntry.setStatus("mandatory")


class _ExampleBcdOperStructBcdVectorIndex_Type(Integer32):
    """Custom type exampleBcdOperStructBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleBcdOperStructBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleBcdOperStructBcdVectorIndex_Object = MibTableColumn
exampleBcdOperStructBcdVectorIndex = _ExampleBcdOperStructBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1120, 1, 1),
    _ExampleBcdOperStructBcdVectorIndex_Type()
)
exampleBcdOperStructBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdVectorIndex.setStatus("mandatory")


class _ExampleBcdOperStructBcdVectorValue_Type(DigitString):
    """Custom type exampleBcdOperStructBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdOperStructBcdVectorValue_Type.__name__ = "DigitString"
_ExampleBcdOperStructBcdVectorValue_Object = MibTableColumn
exampleBcdOperStructBcdVectorValue = _ExampleBcdOperStructBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1120, 1, 2),
    _ExampleBcdOperStructBcdVectorValue_Type()
)
exampleBcdOperStructBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdVectorValue.setStatus("mandatory")
_ExampleBcdOperStructBcdArrayTable_Object = MibTable
exampleBcdOperStructBcdArrayTable = _ExampleBcdOperStructBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1121)
)
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdArrayTable.setStatus("mandatory")
_ExampleBcdOperStructBcdArrayEntry_Object = MibTableRow
exampleBcdOperStructBcdArrayEntry = _ExampleBcdOperStructBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1121, 1)
)
exampleBcdOperStructBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperStructBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperStructBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdArrayEntry.setStatus("mandatory")


class _ExampleBcdOperStructBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleBcdOperStructBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleBcdOperStructBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleBcdOperStructBcdArrayRowIndex_Object = MibTableColumn
exampleBcdOperStructBcdArrayRowIndex = _ExampleBcdOperStructBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1121, 1, 1),
    _ExampleBcdOperStructBcdArrayRowIndex_Type()
)
exampleBcdOperStructBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdArrayRowIndex.setStatus("mandatory")


class _ExampleBcdOperStructBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleBcdOperStructBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleBcdOperStructBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleBcdOperStructBcdArrayColumnIndex_Object = MibTableColumn
exampleBcdOperStructBcdArrayColumnIndex = _ExampleBcdOperStructBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1121, 1, 2),
    _ExampleBcdOperStructBcdArrayColumnIndex_Type()
)
exampleBcdOperStructBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleBcdOperStructBcdArrayValue_Type(DigitString):
    """Custom type exampleBcdOperStructBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdOperStructBcdArrayValue_Type.__name__ = "DigitString"
_ExampleBcdOperStructBcdArrayValue_Object = MibTableColumn
exampleBcdOperStructBcdArrayValue = _ExampleBcdOperStructBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1121, 1, 3),
    _ExampleBcdOperStructBcdArrayValue_Type()
)
exampleBcdOperStructBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperStructBcdArrayValue.setStatus("mandatory")
_ExampleBcdOperFreeBcdVectorTable_Object = MibTable
exampleBcdOperFreeBcdVectorTable = _ExampleBcdOperFreeBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1122)
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdVectorTable.setStatus("mandatory")
_ExampleBcdOperFreeBcdVectorEntry_Object = MibTableRow
exampleBcdOperFreeBcdVectorEntry = _ExampleBcdOperFreeBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1122, 1)
)
exampleBcdOperFreeBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperFreeBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdVectorEntry.setStatus("mandatory")


class _ExampleBcdOperFreeBcdVectorIndex_Type(Integer32):
    """Custom type exampleBcdOperFreeBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleBcdOperFreeBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleBcdOperFreeBcdVectorIndex_Object = MibTableColumn
exampleBcdOperFreeBcdVectorIndex = _ExampleBcdOperFreeBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1122, 1, 1),
    _ExampleBcdOperFreeBcdVectorIndex_Type()
)
exampleBcdOperFreeBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdVectorIndex.setStatus("mandatory")


class _ExampleBcdOperFreeBcdVectorValue_Type(DigitString):
    """Custom type exampleBcdOperFreeBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdOperFreeBcdVectorValue_Type.__name__ = "DigitString"
_ExampleBcdOperFreeBcdVectorValue_Object = MibTableColumn
exampleBcdOperFreeBcdVectorValue = _ExampleBcdOperFreeBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1122, 1, 2),
    _ExampleBcdOperFreeBcdVectorValue_Type()
)
exampleBcdOperFreeBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdVectorValue.setStatus("mandatory")
_ExampleBcdOperFreeBcdArrayTable_Object = MibTable
exampleBcdOperFreeBcdArrayTable = _ExampleBcdOperFreeBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1123)
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdArrayTable.setStatus("mandatory")
_ExampleBcdOperFreeBcdArrayEntry_Object = MibTableRow
exampleBcdOperFreeBcdArrayEntry = _ExampleBcdOperFreeBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1123, 1)
)
exampleBcdOperFreeBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperFreeBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperFreeBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdArrayEntry.setStatus("mandatory")


class _ExampleBcdOperFreeBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleBcdOperFreeBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleBcdOperFreeBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleBcdOperFreeBcdArrayRowIndex_Object = MibTableColumn
exampleBcdOperFreeBcdArrayRowIndex = _ExampleBcdOperFreeBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1123, 1, 1),
    _ExampleBcdOperFreeBcdArrayRowIndex_Type()
)
exampleBcdOperFreeBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdArrayRowIndex.setStatus("mandatory")


class _ExampleBcdOperFreeBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleBcdOperFreeBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleBcdOperFreeBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleBcdOperFreeBcdArrayColumnIndex_Object = MibTableColumn
exampleBcdOperFreeBcdArrayColumnIndex = _ExampleBcdOperFreeBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1123, 1, 2),
    _ExampleBcdOperFreeBcdArrayColumnIndex_Type()
)
exampleBcdOperFreeBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleBcdOperFreeBcdArrayValue_Type(DigitString):
    """Custom type exampleBcdOperFreeBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdOperFreeBcdArrayValue_Type.__name__ = "DigitString"
_ExampleBcdOperFreeBcdArrayValue_Object = MibTableColumn
exampleBcdOperFreeBcdArrayValue = _ExampleBcdOperFreeBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1123, 1, 3),
    _ExampleBcdOperFreeBcdArrayValue_Type()
)
exampleBcdOperFreeBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdArrayValue.setStatus("mandatory")
_ExampleBcdOperFreeBcdReplicatedTable_Object = MibTable
exampleBcdOperFreeBcdReplicatedTable = _ExampleBcdOperFreeBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1124)
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdReplicatedTable.setStatus("mandatory")
_ExampleBcdOperFreeBcdReplicatedEntry_Object = MibTableRow
exampleBcdOperFreeBcdReplicatedEntry = _ExampleBcdOperFreeBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1124, 1)
)
exampleBcdOperFreeBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperFreeBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdReplicatedEntry.setStatus("mandatory")


class _ExampleBcdOperFreeBcdReplicatedIndex_Type(DigitString):
    """Custom type exampleBcdOperFreeBcdReplicatedIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdOperFreeBcdReplicatedIndex_Type.__name__ = "DigitString"
_ExampleBcdOperFreeBcdReplicatedIndex_Object = MibTableColumn
exampleBcdOperFreeBcdReplicatedIndex = _ExampleBcdOperFreeBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1124, 1, 1),
    _ExampleBcdOperFreeBcdReplicatedIndex_Type()
)
exampleBcdOperFreeBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdReplicatedIndex.setStatus("mandatory")


class _ExampleBcdOperFreeBcdReplicatedValue_Type(DigitString):
    """Custom type exampleBcdOperFreeBcdReplicatedValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdOperFreeBcdReplicatedValue_Type.__name__ = "DigitString"
_ExampleBcdOperFreeBcdReplicatedValue_Object = MibTableColumn
exampleBcdOperFreeBcdReplicatedValue = _ExampleBcdOperFreeBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1124, 1, 2),
    _ExampleBcdOperFreeBcdReplicatedValue_Type()
)
exampleBcdOperFreeBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdReplicatedValue.setStatus("mandatory")
_ExampleBcdOperFreeBcdReplicatedRowStatus_Type = RowStatus
_ExampleBcdOperFreeBcdReplicatedRowStatus_Object = MibTableColumn
exampleBcdOperFreeBcdReplicatedRowStatus = _ExampleBcdOperFreeBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1124, 1, 3),
    _ExampleBcdOperFreeBcdReplicatedRowStatus_Type()
)
exampleBcdOperFreeBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdReplicatedRowStatus.setStatus("mandatory")
_ExampleBcdOperFreeBcdListTable_Object = MibTable
exampleBcdOperFreeBcdListTable = _ExampleBcdOperFreeBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1125)
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdListTable.setStatus("mandatory")
_ExampleBcdOperFreeBcdListEntry_Object = MibTableRow
exampleBcdOperFreeBcdListEntry = _ExampleBcdOperFreeBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1125, 1)
)
exampleBcdOperFreeBcdListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdOperFreeBcdListValue"),
)
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdListEntry.setStatus("mandatory")


class _ExampleBcdOperFreeBcdListValue_Type(DigitString):
    """Custom type exampleBcdOperFreeBcdListValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdOperFreeBcdListValue_Type.__name__ = "DigitString"
_ExampleBcdOperFreeBcdListValue_Object = MibTableColumn
exampleBcdOperFreeBcdListValue = _ExampleBcdOperFreeBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1125, 1, 1),
    _ExampleBcdOperFreeBcdListValue_Type()
)
exampleBcdOperFreeBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdListValue.setStatus("mandatory")
_ExampleBcdOperFreeBcdListRowStatus_Type = RowStatus
_ExampleBcdOperFreeBcdListRowStatus_Object = MibTableColumn
exampleBcdOperFreeBcdListRowStatus = _ExampleBcdOperFreeBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1125, 1, 2),
    _ExampleBcdOperFreeBcdListRowStatus_Type()
)
exampleBcdOperFreeBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleBcdOperFreeBcdListRowStatus.setStatus("mandatory")
_ExampleBcdProvStructBcdVectorTable_Object = MibTable
exampleBcdProvStructBcdVectorTable = _ExampleBcdProvStructBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1126)
)
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdVectorTable.setStatus("mandatory")
_ExampleBcdProvStructBcdVectorEntry_Object = MibTableRow
exampleBcdProvStructBcdVectorEntry = _ExampleBcdProvStructBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1126, 1)
)
exampleBcdProvStructBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvStructBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdVectorEntry.setStatus("mandatory")


class _ExampleBcdProvStructBcdVectorIndex_Type(Integer32):
    """Custom type exampleBcdProvStructBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleBcdProvStructBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleBcdProvStructBcdVectorIndex_Object = MibTableColumn
exampleBcdProvStructBcdVectorIndex = _ExampleBcdProvStructBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1126, 1, 1),
    _ExampleBcdProvStructBcdVectorIndex_Type()
)
exampleBcdProvStructBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdVectorIndex.setStatus("mandatory")


class _ExampleBcdProvStructBcdVectorValue_Type(DigitString):
    """Custom type exampleBcdProvStructBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvStructBcdVectorValue_Type.__name__ = "DigitString"
_ExampleBcdProvStructBcdVectorValue_Object = MibTableColumn
exampleBcdProvStructBcdVectorValue = _ExampleBcdProvStructBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1126, 1, 2),
    _ExampleBcdProvStructBcdVectorValue_Type()
)
exampleBcdProvStructBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdVectorValue.setStatus("mandatory")
_ExampleBcdProvStructBcdArrayTable_Object = MibTable
exampleBcdProvStructBcdArrayTable = _ExampleBcdProvStructBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1127)
)
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdArrayTable.setStatus("mandatory")
_ExampleBcdProvStructBcdArrayEntry_Object = MibTableRow
exampleBcdProvStructBcdArrayEntry = _ExampleBcdProvStructBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1127, 1)
)
exampleBcdProvStructBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvStructBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvStructBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdArrayEntry.setStatus("mandatory")


class _ExampleBcdProvStructBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleBcdProvStructBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleBcdProvStructBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleBcdProvStructBcdArrayRowIndex_Object = MibTableColumn
exampleBcdProvStructBcdArrayRowIndex = _ExampleBcdProvStructBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1127, 1, 1),
    _ExampleBcdProvStructBcdArrayRowIndex_Type()
)
exampleBcdProvStructBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdArrayRowIndex.setStatus("mandatory")


class _ExampleBcdProvStructBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleBcdProvStructBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleBcdProvStructBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleBcdProvStructBcdArrayColumnIndex_Object = MibTableColumn
exampleBcdProvStructBcdArrayColumnIndex = _ExampleBcdProvStructBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1127, 1, 2),
    _ExampleBcdProvStructBcdArrayColumnIndex_Type()
)
exampleBcdProvStructBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleBcdProvStructBcdArrayValue_Type(DigitString):
    """Custom type exampleBcdProvStructBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvStructBcdArrayValue_Type.__name__ = "DigitString"
_ExampleBcdProvStructBcdArrayValue_Object = MibTableColumn
exampleBcdProvStructBcdArrayValue = _ExampleBcdProvStructBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1127, 1, 3),
    _ExampleBcdProvStructBcdArrayValue_Type()
)
exampleBcdProvStructBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvStructBcdArrayValue.setStatus("mandatory")
_ExampleBcdProvFreeBcdVectorTable_Object = MibTable
exampleBcdProvFreeBcdVectorTable = _ExampleBcdProvFreeBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1128)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVectorTable.setStatus("mandatory")
_ExampleBcdProvFreeBcdVectorEntry_Object = MibTableRow
exampleBcdProvFreeBcdVectorEntry = _ExampleBcdProvFreeBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1128, 1)
)
exampleBcdProvFreeBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVectorEntry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdVectorIndex_Type(Integer32):
    """Custom type exampleBcdProvFreeBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleBcdProvFreeBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleBcdProvFreeBcdVectorIndex_Object = MibTableColumn
exampleBcdProvFreeBcdVectorIndex = _ExampleBcdProvFreeBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1128, 1, 1),
    _ExampleBcdProvFreeBcdVectorIndex_Type()
)
exampleBcdProvFreeBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVectorIndex.setStatus("mandatory")


class _ExampleBcdProvFreeBcdVectorValue_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvFreeBcdVectorValue_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdVectorValue_Object = MibTableColumn
exampleBcdProvFreeBcdVectorValue = _ExampleBcdProvFreeBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1128, 1, 2),
    _ExampleBcdProvFreeBcdVectorValue_Type()
)
exampleBcdProvFreeBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVectorValue.setStatus("mandatory")
_ExampleBcdProvFreeBcdVector1Table_Object = MibTable
exampleBcdProvFreeBcdVector1Table = _ExampleBcdProvFreeBcdVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1129)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVector1Table.setStatus("mandatory")
_ExampleBcdProvFreeBcdVector1Entry_Object = MibTableRow
exampleBcdProvFreeBcdVector1Entry = _ExampleBcdProvFreeBcdVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1129, 1)
)
exampleBcdProvFreeBcdVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdVector1Index"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVector1Entry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdVector1Index_Type(Integer32):
    """Custom type exampleBcdProvFreeBcdVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ExampleBcdProvFreeBcdVector1Index_Type.__name__ = "Integer32"
_ExampleBcdProvFreeBcdVector1Index_Object = MibTableColumn
exampleBcdProvFreeBcdVector1Index = _ExampleBcdProvFreeBcdVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1129, 1, 1),
    _ExampleBcdProvFreeBcdVector1Index_Type()
)
exampleBcdProvFreeBcdVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVector1Index.setStatus("mandatory")


class _ExampleBcdProvFreeBcdVector1Value_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdVector1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvFreeBcdVector1Value_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdVector1Value_Object = MibTableColumn
exampleBcdProvFreeBcdVector1Value = _ExampleBcdProvFreeBcdVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1129, 1, 2),
    _ExampleBcdProvFreeBcdVector1Value_Type()
)
exampleBcdProvFreeBcdVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdVector1Value.setStatus("mandatory")
_ExampleBcdProvFreeBcdArrayTable_Object = MibTable
exampleBcdProvFreeBcdArrayTable = _ExampleBcdProvFreeBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1130)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArrayTable.setStatus("mandatory")
_ExampleBcdProvFreeBcdArrayEntry_Object = MibTableRow
exampleBcdProvFreeBcdArrayEntry = _ExampleBcdProvFreeBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1130, 1)
)
exampleBcdProvFreeBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArrayEntry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleBcdProvFreeBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleBcdProvFreeBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleBcdProvFreeBcdArrayRowIndex_Object = MibTableColumn
exampleBcdProvFreeBcdArrayRowIndex = _ExampleBcdProvFreeBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1130, 1, 1),
    _ExampleBcdProvFreeBcdArrayRowIndex_Type()
)
exampleBcdProvFreeBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArrayRowIndex.setStatus("mandatory")


class _ExampleBcdProvFreeBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleBcdProvFreeBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleBcdProvFreeBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleBcdProvFreeBcdArrayColumnIndex_Object = MibTableColumn
exampleBcdProvFreeBcdArrayColumnIndex = _ExampleBcdProvFreeBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1130, 1, 2),
    _ExampleBcdProvFreeBcdArrayColumnIndex_Type()
)
exampleBcdProvFreeBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleBcdProvFreeBcdArrayValue_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvFreeBcdArrayValue_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdArrayValue_Object = MibTableColumn
exampleBcdProvFreeBcdArrayValue = _ExampleBcdProvFreeBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1130, 1, 3),
    _ExampleBcdProvFreeBcdArrayValue_Type()
)
exampleBcdProvFreeBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArrayValue.setStatus("mandatory")
_ExampleBcdProvFreeBcdArray1Table_Object = MibTable
exampleBcdProvFreeBcdArray1Table = _ExampleBcdProvFreeBcdArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1131)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArray1Table.setStatus("mandatory")
_ExampleBcdProvFreeBcdArray1Entry_Object = MibTableRow
exampleBcdProvFreeBcdArray1Entry = _ExampleBcdProvFreeBcdArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1131, 1)
)
exampleBcdProvFreeBcdArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdArray1RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArray1Entry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdArray1RowIndex_Type(Integer32):
    """Custom type exampleBcdProvFreeBcdArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleBcdProvFreeBcdArray1RowIndex_Type.__name__ = "Integer32"
_ExampleBcdProvFreeBcdArray1RowIndex_Object = MibTableColumn
exampleBcdProvFreeBcdArray1RowIndex = _ExampleBcdProvFreeBcdArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1131, 1, 1),
    _ExampleBcdProvFreeBcdArray1RowIndex_Type()
)
exampleBcdProvFreeBcdArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArray1RowIndex.setStatus("mandatory")


class _ExampleBcdProvFreeBcdArray1ColumnIndex_Type(Integer32):
    """Custom type exampleBcdProvFreeBcdArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleBcdProvFreeBcdArray1ColumnIndex_Type.__name__ = "Integer32"
_ExampleBcdProvFreeBcdArray1ColumnIndex_Object = MibTableColumn
exampleBcdProvFreeBcdArray1ColumnIndex = _ExampleBcdProvFreeBcdArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1131, 1, 2),
    _ExampleBcdProvFreeBcdArray1ColumnIndex_Type()
)
exampleBcdProvFreeBcdArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArray1ColumnIndex.setStatus("mandatory")


class _ExampleBcdProvFreeBcdArray1Value_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdArray1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvFreeBcdArray1Value_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdArray1Value_Object = MibTableColumn
exampleBcdProvFreeBcdArray1Value = _ExampleBcdProvFreeBcdArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1131, 1, 3),
    _ExampleBcdProvFreeBcdArray1Value_Type()
)
exampleBcdProvFreeBcdArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdArray1Value.setStatus("mandatory")
_ExampleBcdProvFreeBcdReplicatedTable_Object = MibTable
exampleBcdProvFreeBcdReplicatedTable = _ExampleBcdProvFreeBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1132)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicatedTable.setStatus("mandatory")
_ExampleBcdProvFreeBcdReplicatedEntry_Object = MibTableRow
exampleBcdProvFreeBcdReplicatedEntry = _ExampleBcdProvFreeBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1132, 1)
)
exampleBcdProvFreeBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicatedEntry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdReplicatedIndex_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdReplicatedIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvFreeBcdReplicatedIndex_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdReplicatedIndex_Object = MibTableColumn
exampleBcdProvFreeBcdReplicatedIndex = _ExampleBcdProvFreeBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1132, 1, 1),
    _ExampleBcdProvFreeBcdReplicatedIndex_Type()
)
exampleBcdProvFreeBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicatedIndex.setStatus("mandatory")


class _ExampleBcdProvFreeBcdReplicatedValue_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdReplicatedValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdProvFreeBcdReplicatedValue_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdReplicatedValue_Object = MibTableColumn
exampleBcdProvFreeBcdReplicatedValue = _ExampleBcdProvFreeBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1132, 1, 2),
    _ExampleBcdProvFreeBcdReplicatedValue_Type()
)
exampleBcdProvFreeBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicatedValue.setStatus("mandatory")
_ExampleBcdProvFreeBcdReplicatedRowStatus_Type = RowStatus
_ExampleBcdProvFreeBcdReplicatedRowStatus_Object = MibTableColumn
exampleBcdProvFreeBcdReplicatedRowStatus = _ExampleBcdProvFreeBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1132, 1, 3),
    _ExampleBcdProvFreeBcdReplicatedRowStatus_Type()
)
exampleBcdProvFreeBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicatedRowStatus.setStatus("mandatory")
_ExampleBcdProvFreeBcdReplicated1Table_Object = MibTable
exampleBcdProvFreeBcdReplicated1Table = _ExampleBcdProvFreeBcdReplicated1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1133)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicated1Table.setStatus("mandatory")
_ExampleBcdProvFreeBcdReplicated1Entry_Object = MibTableRow
exampleBcdProvFreeBcdReplicated1Entry = _ExampleBcdProvFreeBcdReplicated1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1133, 1)
)
exampleBcdProvFreeBcdReplicated1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdReplicated1Index"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicated1Entry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdReplicated1Index_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdReplicated1Index based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_ExampleBcdProvFreeBcdReplicated1Index_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdReplicated1Index_Object = MibTableColumn
exampleBcdProvFreeBcdReplicated1Index = _ExampleBcdProvFreeBcdReplicated1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1133, 1, 1),
    _ExampleBcdProvFreeBcdReplicated1Index_Type()
)
exampleBcdProvFreeBcdReplicated1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicated1Index.setStatus("mandatory")


class _ExampleBcdProvFreeBcdReplicated1Value_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdReplicated1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleBcdProvFreeBcdReplicated1Value_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdReplicated1Value_Object = MibTableColumn
exampleBcdProvFreeBcdReplicated1Value = _ExampleBcdProvFreeBcdReplicated1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1133, 1, 2),
    _ExampleBcdProvFreeBcdReplicated1Value_Type()
)
exampleBcdProvFreeBcdReplicated1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicated1Value.setStatus("mandatory")
_ExampleBcdProvFreeBcdReplicated1RowStatus_Type = RowStatus
_ExampleBcdProvFreeBcdReplicated1RowStatus_Object = MibTableColumn
exampleBcdProvFreeBcdReplicated1RowStatus = _ExampleBcdProvFreeBcdReplicated1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1133, 1, 3),
    _ExampleBcdProvFreeBcdReplicated1RowStatus_Type()
)
exampleBcdProvFreeBcdReplicated1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdReplicated1RowStatus.setStatus("mandatory")
_ExampleBcdProvFreeBcdListTable_Object = MibTable
exampleBcdProvFreeBcdListTable = _ExampleBcdProvFreeBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1134)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdListTable.setStatus("mandatory")
_ExampleBcdProvFreeBcdListEntry_Object = MibTableRow
exampleBcdProvFreeBcdListEntry = _ExampleBcdProvFreeBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1134, 1)
)
exampleBcdProvFreeBcdListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdListValue"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdListEntry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdListValue_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdListValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdProvFreeBcdListValue_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdListValue_Object = MibTableColumn
exampleBcdProvFreeBcdListValue = _ExampleBcdProvFreeBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1134, 1, 1),
    _ExampleBcdProvFreeBcdListValue_Type()
)
exampleBcdProvFreeBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdListValue.setStatus("mandatory")
_ExampleBcdProvFreeBcdListRowStatus_Type = RowStatus
_ExampleBcdProvFreeBcdListRowStatus_Object = MibTableColumn
exampleBcdProvFreeBcdListRowStatus = _ExampleBcdProvFreeBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1134, 1, 2),
    _ExampleBcdProvFreeBcdListRowStatus_Type()
)
exampleBcdProvFreeBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdListRowStatus.setStatus("mandatory")
_ExampleBcdProvFreeBcdList1Table_Object = MibTable
exampleBcdProvFreeBcdList1Table = _ExampleBcdProvFreeBcdList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1135)
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdList1Table.setStatus("mandatory")
_ExampleBcdProvFreeBcdList1Entry_Object = MibTableRow
exampleBcdProvFreeBcdList1Entry = _ExampleBcdProvFreeBcdList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1135, 1)
)
exampleBcdProvFreeBcdList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdProvFreeBcdList1Value"),
)
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdList1Entry.setStatus("mandatory")


class _ExampleBcdProvFreeBcdList1Value_Type(DigitString):
    """Custom type exampleBcdProvFreeBcdList1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleBcdProvFreeBcdList1Value_Type.__name__ = "DigitString"
_ExampleBcdProvFreeBcdList1Value_Object = MibTableColumn
exampleBcdProvFreeBcdList1Value = _ExampleBcdProvFreeBcdList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1135, 1, 1),
    _ExampleBcdProvFreeBcdList1Value_Type()
)
exampleBcdProvFreeBcdList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdList1Value.setStatus("mandatory")
_ExampleBcdProvFreeBcdList1RowStatus_Type = RowStatus
_ExampleBcdProvFreeBcdList1RowStatus_Object = MibTableColumn
exampleBcdProvFreeBcdList1RowStatus = _ExampleBcdProvFreeBcdList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 9, 1135, 1, 2),
    _ExampleBcdProvFreeBcdList1RowStatus_Type()
)
exampleBcdProvFreeBcdList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleBcdProvFreeBcdList1RowStatus.setStatus("mandatory")
_ExampleWildBcd_ObjectIdentity = ObjectIdentity
exampleWildBcd = _ExampleWildBcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10)
)
_ExampleWildBcdRowStatusTable_Object = MibTable
exampleWildBcdRowStatusTable = _ExampleWildBcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1)
)
if mibBuilder.loadTexts:
    exampleWildBcdRowStatusTable.setStatus("mandatory")
_ExampleWildBcdRowStatusEntry_Object = MibTableRow
exampleWildBcdRowStatusEntry = _ExampleWildBcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1, 1)
)
exampleWildBcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdRowStatusEntry.setStatus("mandatory")
_ExampleWildBcdRowStatus_Type = RowStatus
_ExampleWildBcdRowStatus_Object = MibTableColumn
exampleWildBcdRowStatus = _ExampleWildBcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1, 1, 1),
    _ExampleWildBcdRowStatus_Type()
)
exampleWildBcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdRowStatus.setStatus("mandatory")
_ExampleWildBcdComponentName_Type = DisplayString
_ExampleWildBcdComponentName_Object = MibTableColumn
exampleWildBcdComponentName = _ExampleWildBcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1, 1, 2),
    _ExampleWildBcdComponentName_Type()
)
exampleWildBcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleWildBcdComponentName.setStatus("mandatory")
_ExampleWildBcdStorageType_Type = StorageType
_ExampleWildBcdStorageType_Object = MibTableColumn
exampleWildBcdStorageType = _ExampleWildBcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1, 1, 4),
    _ExampleWildBcdStorageType_Type()
)
exampleWildBcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleWildBcdStorageType.setStatus("mandatory")


class _ExampleWildBcdIndex_Type(WildcardedDigitString):
    """Custom type exampleWildBcdIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleWildBcdIndex_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdIndex_Object = MibTableColumn
exampleWildBcdIndex = _ExampleWildBcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1, 1, 10),
    _ExampleWildBcdIndex_Type()
)
exampleWildBcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdIndex.setStatus("mandatory")
_ExampleWildBcdOperationalTable_Object = MibTable
exampleWildBcdOperationalTable = _ExampleWildBcdOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 10)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperationalTable.setStatus("mandatory")
_ExampleWildBcdOperationalEntry_Object = MibTableRow
exampleWildBcdOperationalEntry = _ExampleWildBcdOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 10, 1)
)
exampleWildBcdOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperationalEntry.setStatus("mandatory")


class _ExampleWildBcdOperStructWildBcd_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperStructWildBcd based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdOperStructWildBcd_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperStructWildBcd_Object = MibTableColumn
exampleWildBcdOperStructWildBcd = _ExampleWildBcdOperStructWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 10, 1, 1),
    _ExampleWildBcdOperStructWildBcd_Type()
)
exampleWildBcdOperStructWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcd.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcd_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperFreeWildBcd based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdOperFreeWildBcd_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperFreeWildBcd_Object = MibTableColumn
exampleWildBcdOperFreeWildBcd = _ExampleWildBcdOperFreeWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 10, 1, 2),
    _ExampleWildBcdOperFreeWildBcd_Type()
)
exampleWildBcdOperFreeWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcd.setStatus("mandatory")
_ExampleWildBcdProvisionalTable_Object = MibTable
exampleWildBcdProvisionalTable = _ExampleWildBcdProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 11)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvisionalTable.setStatus("mandatory")
_ExampleWildBcdProvisionalEntry_Object = MibTableRow
exampleWildBcdProvisionalEntry = _ExampleWildBcdProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 11, 1)
)
exampleWildBcdProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvisionalEntry.setStatus("mandatory")


class _ExampleWildBcdProvStructWildBcd_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvStructWildBcd based on WildcardedDigitString"""
    defaultHexValue = "30313233343536373839"

    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdProvStructWildBcd_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvStructWildBcd_Object = MibTableColumn
exampleWildBcdProvStructWildBcd = _ExampleWildBcdProvStructWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 11, 1, 1),
    _ExampleWildBcdProvStructWildBcd_Type()
)
exampleWildBcdProvStructWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcd.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcd_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvFreeWildBcd based on WildcardedDigitString"""
    defaultHexValue = "31323334353637383930"

    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_ExampleWildBcdProvFreeWildBcd_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvFreeWildBcd_Object = MibTableColumn
exampleWildBcdProvFreeWildBcd = _ExampleWildBcdProvFreeWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 11, 1, 2),
    _ExampleWildBcdProvFreeWildBcd_Type()
)
exampleWildBcdProvFreeWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcd.setStatus("mandatory")
_ExampleWildBcdOperStructWildBcdVectorTable_Object = MibTable
exampleWildBcdOperStructWildBcdVectorTable = _ExampleWildBcdOperStructWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1136)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdVectorTable.setStatus("mandatory")
_ExampleWildBcdOperStructWildBcdVectorEntry_Object = MibTableRow
exampleWildBcdOperStructWildBcdVectorEntry = _ExampleWildBcdOperStructWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1136, 1)
)
exampleWildBcdOperStructWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperStructWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdVectorEntry.setStatus("mandatory")


class _ExampleWildBcdOperStructWildBcdVectorIndex_Type(Integer32):
    """Custom type exampleWildBcdOperStructWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleWildBcdOperStructWildBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleWildBcdOperStructWildBcdVectorIndex_Object = MibTableColumn
exampleWildBcdOperStructWildBcdVectorIndex = _ExampleWildBcdOperStructWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1136, 1, 1),
    _ExampleWildBcdOperStructWildBcdVectorIndex_Type()
)
exampleWildBcdOperStructWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdVectorIndex.setStatus("mandatory")


class _ExampleWildBcdOperStructWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperStructWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdOperStructWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperStructWildBcdVectorValue_Object = MibTableColumn
exampleWildBcdOperStructWildBcdVectorValue = _ExampleWildBcdOperStructWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1136, 1, 2),
    _ExampleWildBcdOperStructWildBcdVectorValue_Type()
)
exampleWildBcdOperStructWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdVectorValue.setStatus("mandatory")
_ExampleWildBcdOperStructWildBcdArrayTable_Object = MibTable
exampleWildBcdOperStructWildBcdArrayTable = _ExampleWildBcdOperStructWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1137)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdArrayTable.setStatus("mandatory")
_ExampleWildBcdOperStructWildBcdArrayEntry_Object = MibTableRow
exampleWildBcdOperStructWildBcdArrayEntry = _ExampleWildBcdOperStructWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1137, 1)
)
exampleWildBcdOperStructWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperStructWildBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperStructWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdArrayEntry.setStatus("mandatory")


class _ExampleWildBcdOperStructWildBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleWildBcdOperStructWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleWildBcdOperStructWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleWildBcdOperStructWildBcdArrayRowIndex_Object = MibTableColumn
exampleWildBcdOperStructWildBcdArrayRowIndex = _ExampleWildBcdOperStructWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1137, 1, 1),
    _ExampleWildBcdOperStructWildBcdArrayRowIndex_Type()
)
exampleWildBcdOperStructWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdArrayRowIndex.setStatus("mandatory")


class _ExampleWildBcdOperStructWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleWildBcdOperStructWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleWildBcdOperStructWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleWildBcdOperStructWildBcdArrayColumnIndex_Object = MibTableColumn
exampleWildBcdOperStructWildBcdArrayColumnIndex = _ExampleWildBcdOperStructWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1137, 1, 2),
    _ExampleWildBcdOperStructWildBcdArrayColumnIndex_Type()
)
exampleWildBcdOperStructWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleWildBcdOperStructWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperStructWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdOperStructWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperStructWildBcdArrayValue_Object = MibTableColumn
exampleWildBcdOperStructWildBcdArrayValue = _ExampleWildBcdOperStructWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1137, 1, 3),
    _ExampleWildBcdOperStructWildBcdArrayValue_Type()
)
exampleWildBcdOperStructWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperStructWildBcdArrayValue.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdVectorTable_Object = MibTable
exampleWildBcdOperFreeWildBcdVectorTable = _ExampleWildBcdOperFreeWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1138)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdVectorTable.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdVectorEntry_Object = MibTableRow
exampleWildBcdOperFreeWildBcdVectorEntry = _ExampleWildBcdOperFreeWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1138, 1)
)
exampleWildBcdOperFreeWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperFreeWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdVectorEntry.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdVectorIndex_Type(Integer32):
    """Custom type exampleWildBcdOperFreeWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleWildBcdOperFreeWildBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleWildBcdOperFreeWildBcdVectorIndex_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdVectorIndex = _ExampleWildBcdOperFreeWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1138, 1, 1),
    _ExampleWildBcdOperFreeWildBcdVectorIndex_Type()
)
exampleWildBcdOperFreeWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdVectorIndex.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperFreeWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdOperFreeWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperFreeWildBcdVectorValue_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdVectorValue = _ExampleWildBcdOperFreeWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1138, 1, 2),
    _ExampleWildBcdOperFreeWildBcdVectorValue_Type()
)
exampleWildBcdOperFreeWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdVectorValue.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdArrayTable_Object = MibTable
exampleWildBcdOperFreeWildBcdArrayTable = _ExampleWildBcdOperFreeWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1139)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdArrayTable.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdArrayEntry_Object = MibTableRow
exampleWildBcdOperFreeWildBcdArrayEntry = _ExampleWildBcdOperFreeWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1139, 1)
)
exampleWildBcdOperFreeWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperFreeWildBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperFreeWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdArrayEntry.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleWildBcdOperFreeWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleWildBcdOperFreeWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleWildBcdOperFreeWildBcdArrayRowIndex_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdArrayRowIndex = _ExampleWildBcdOperFreeWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1139, 1, 1),
    _ExampleWildBcdOperFreeWildBcdArrayRowIndex_Type()
)
exampleWildBcdOperFreeWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdArrayRowIndex.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleWildBcdOperFreeWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleWildBcdOperFreeWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleWildBcdOperFreeWildBcdArrayColumnIndex_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdArrayColumnIndex = _ExampleWildBcdOperFreeWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1139, 1, 2),
    _ExampleWildBcdOperFreeWildBcdArrayColumnIndex_Type()
)
exampleWildBcdOperFreeWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperFreeWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdOperFreeWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperFreeWildBcdArrayValue_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdArrayValue = _ExampleWildBcdOperFreeWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1139, 1, 3),
    _ExampleWildBcdOperFreeWildBcdArrayValue_Type()
)
exampleWildBcdOperFreeWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdArrayValue.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdReplicatedTable_Object = MibTable
exampleWildBcdOperFreeWildBcdReplicatedTable = _ExampleWildBcdOperFreeWildBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1140)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdReplicatedTable.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdReplicatedEntry_Object = MibTableRow
exampleWildBcdOperFreeWildBcdReplicatedEntry = _ExampleWildBcdOperFreeWildBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1140, 1)
)
exampleWildBcdOperFreeWildBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperFreeWildBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdReplicatedEntry.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdReplicatedIndex_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperFreeWildBcdReplicatedIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdOperFreeWildBcdReplicatedIndex_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperFreeWildBcdReplicatedIndex_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdReplicatedIndex = _ExampleWildBcdOperFreeWildBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1140, 1, 1),
    _ExampleWildBcdOperFreeWildBcdReplicatedIndex_Type()
)
exampleWildBcdOperFreeWildBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdReplicatedIndex.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdReplicatedValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperFreeWildBcdReplicatedValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdOperFreeWildBcdReplicatedValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperFreeWildBcdReplicatedValue_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdReplicatedValue = _ExampleWildBcdOperFreeWildBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1140, 1, 2),
    _ExampleWildBcdOperFreeWildBcdReplicatedValue_Type()
)
exampleWildBcdOperFreeWildBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdReplicatedValue.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Type = RowStatus
_ExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdReplicatedRowStatus = _ExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1140, 1, 3),
    _ExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Type()
)
exampleWildBcdOperFreeWildBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdReplicatedRowStatus.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdListTable_Object = MibTable
exampleWildBcdOperFreeWildBcdListTable = _ExampleWildBcdOperFreeWildBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1141)
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdListTable.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdListEntry_Object = MibTableRow
exampleWildBcdOperFreeWildBcdListEntry = _ExampleWildBcdOperFreeWildBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1141, 1)
)
exampleWildBcdOperFreeWildBcdListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdOperFreeWildBcdListValue"),
)
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdListEntry.setStatus("mandatory")


class _ExampleWildBcdOperFreeWildBcdListValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdOperFreeWildBcdListValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdOperFreeWildBcdListValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdOperFreeWildBcdListValue_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdListValue = _ExampleWildBcdOperFreeWildBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1141, 1, 1),
    _ExampleWildBcdOperFreeWildBcdListValue_Type()
)
exampleWildBcdOperFreeWildBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdListValue.setStatus("mandatory")
_ExampleWildBcdOperFreeWildBcdListRowStatus_Type = RowStatus
_ExampleWildBcdOperFreeWildBcdListRowStatus_Object = MibTableColumn
exampleWildBcdOperFreeWildBcdListRowStatus = _ExampleWildBcdOperFreeWildBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1141, 1, 2),
    _ExampleWildBcdOperFreeWildBcdListRowStatus_Type()
)
exampleWildBcdOperFreeWildBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleWildBcdOperFreeWildBcdListRowStatus.setStatus("mandatory")
_ExampleWildBcdProvStructWildBcdVectorTable_Object = MibTable
exampleWildBcdProvStructWildBcdVectorTable = _ExampleWildBcdProvStructWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1142)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdVectorTable.setStatus("mandatory")
_ExampleWildBcdProvStructWildBcdVectorEntry_Object = MibTableRow
exampleWildBcdProvStructWildBcdVectorEntry = _ExampleWildBcdProvStructWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1142, 1)
)
exampleWildBcdProvStructWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvStructWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdVectorEntry.setStatus("mandatory")


class _ExampleWildBcdProvStructWildBcdVectorIndex_Type(Integer32):
    """Custom type exampleWildBcdProvStructWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleWildBcdProvStructWildBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleWildBcdProvStructWildBcdVectorIndex_Object = MibTableColumn
exampleWildBcdProvStructWildBcdVectorIndex = _ExampleWildBcdProvStructWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1142, 1, 1),
    _ExampleWildBcdProvStructWildBcdVectorIndex_Type()
)
exampleWildBcdProvStructWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdVectorIndex.setStatus("mandatory")


class _ExampleWildBcdProvStructWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvStructWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdProvStructWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvStructWildBcdVectorValue_Object = MibTableColumn
exampleWildBcdProvStructWildBcdVectorValue = _ExampleWildBcdProvStructWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1142, 1, 2),
    _ExampleWildBcdProvStructWildBcdVectorValue_Type()
)
exampleWildBcdProvStructWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdVectorValue.setStatus("mandatory")
_ExampleWildBcdProvStructWildBcdArrayTable_Object = MibTable
exampleWildBcdProvStructWildBcdArrayTable = _ExampleWildBcdProvStructWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1143)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdArrayTable.setStatus("mandatory")
_ExampleWildBcdProvStructWildBcdArrayEntry_Object = MibTableRow
exampleWildBcdProvStructWildBcdArrayEntry = _ExampleWildBcdProvStructWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1143, 1)
)
exampleWildBcdProvStructWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvStructWildBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvStructWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdArrayEntry.setStatus("mandatory")


class _ExampleWildBcdProvStructWildBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleWildBcdProvStructWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleWildBcdProvStructWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleWildBcdProvStructWildBcdArrayRowIndex_Object = MibTableColumn
exampleWildBcdProvStructWildBcdArrayRowIndex = _ExampleWildBcdProvStructWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1143, 1, 1),
    _ExampleWildBcdProvStructWildBcdArrayRowIndex_Type()
)
exampleWildBcdProvStructWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdArrayRowIndex.setStatus("mandatory")


class _ExampleWildBcdProvStructWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleWildBcdProvStructWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleWildBcdProvStructWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleWildBcdProvStructWildBcdArrayColumnIndex_Object = MibTableColumn
exampleWildBcdProvStructWildBcdArrayColumnIndex = _ExampleWildBcdProvStructWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1143, 1, 2),
    _ExampleWildBcdProvStructWildBcdArrayColumnIndex_Type()
)
exampleWildBcdProvStructWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleWildBcdProvStructWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvStructWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdProvStructWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvStructWildBcdArrayValue_Object = MibTableColumn
exampleWildBcdProvStructWildBcdArrayValue = _ExampleWildBcdProvStructWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1143, 1, 3),
    _ExampleWildBcdProvStructWildBcdArrayValue_Type()
)
exampleWildBcdProvStructWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvStructWildBcdArrayValue.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdVectorTable_Object = MibTable
exampleWildBcdProvFreeWildBcdVectorTable = _ExampleWildBcdProvFreeWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1144)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdVectorTable.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdVectorEntry_Object = MibTableRow
exampleWildBcdProvFreeWildBcdVectorEntry = _ExampleWildBcdProvFreeWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1144, 1)
)
exampleWildBcdProvFreeWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvFreeWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdVectorEntry.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdVectorIndex_Type(Integer32):
    """Custom type exampleWildBcdProvFreeWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleWildBcdProvFreeWildBcdVectorIndex_Type.__name__ = "Integer32"
_ExampleWildBcdProvFreeWildBcdVectorIndex_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdVectorIndex = _ExampleWildBcdProvFreeWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1144, 1, 1),
    _ExampleWildBcdProvFreeWildBcdVectorIndex_Type()
)
exampleWildBcdProvFreeWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdVectorIndex.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvFreeWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdProvFreeWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvFreeWildBcdVectorValue_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdVectorValue = _ExampleWildBcdProvFreeWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1144, 1, 2),
    _ExampleWildBcdProvFreeWildBcdVectorValue_Type()
)
exampleWildBcdProvFreeWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdVectorValue.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdArrayTable_Object = MibTable
exampleWildBcdProvFreeWildBcdArrayTable = _ExampleWildBcdProvFreeWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1145)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdArrayTable.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdArrayEntry_Object = MibTableRow
exampleWildBcdProvFreeWildBcdArrayEntry = _ExampleWildBcdProvFreeWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1145, 1)
)
exampleWildBcdProvFreeWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvFreeWildBcdArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvFreeWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdArrayEntry.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdArrayRowIndex_Type(Integer32):
    """Custom type exampleWildBcdProvFreeWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleWildBcdProvFreeWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_ExampleWildBcdProvFreeWildBcdArrayRowIndex_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdArrayRowIndex = _ExampleWildBcdProvFreeWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1145, 1, 1),
    _ExampleWildBcdProvFreeWildBcdArrayRowIndex_Type()
)
exampleWildBcdProvFreeWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdArrayRowIndex.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type exampleWildBcdProvFreeWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleWildBcdProvFreeWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleWildBcdProvFreeWildBcdArrayColumnIndex_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdArrayColumnIndex = _ExampleWildBcdProvFreeWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1145, 1, 2),
    _ExampleWildBcdProvFreeWildBcdArrayColumnIndex_Type()
)
exampleWildBcdProvFreeWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdArrayColumnIndex.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvFreeWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdProvFreeWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvFreeWildBcdArrayValue_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdArrayValue = _ExampleWildBcdProvFreeWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1145, 1, 3),
    _ExampleWildBcdProvFreeWildBcdArrayValue_Type()
)
exampleWildBcdProvFreeWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdArrayValue.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdReplicatedTable_Object = MibTable
exampleWildBcdProvFreeWildBcdReplicatedTable = _ExampleWildBcdProvFreeWildBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1146)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdReplicatedTable.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdReplicatedEntry_Object = MibTableRow
exampleWildBcdProvFreeWildBcdReplicatedEntry = _ExampleWildBcdProvFreeWildBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1146, 1)
)
exampleWildBcdProvFreeWildBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvFreeWildBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdReplicatedEntry.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdReplicatedIndex_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvFreeWildBcdReplicatedIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExampleWildBcdProvFreeWildBcdReplicatedIndex_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvFreeWildBcdReplicatedIndex_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdReplicatedIndex = _ExampleWildBcdProvFreeWildBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1146, 1, 1),
    _ExampleWildBcdProvFreeWildBcdReplicatedIndex_Type()
)
exampleWildBcdProvFreeWildBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdReplicatedIndex.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdReplicatedValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvFreeWildBcdReplicatedValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdProvFreeWildBcdReplicatedValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvFreeWildBcdReplicatedValue_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdReplicatedValue = _ExampleWildBcdProvFreeWildBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1146, 1, 2),
    _ExampleWildBcdProvFreeWildBcdReplicatedValue_Type()
)
exampleWildBcdProvFreeWildBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdReplicatedValue.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Type = RowStatus
_ExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdReplicatedRowStatus = _ExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1146, 1, 3),
    _ExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Type()
)
exampleWildBcdProvFreeWildBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdReplicatedRowStatus.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdListTable_Object = MibTable
exampleWildBcdProvFreeWildBcdListTable = _ExampleWildBcdProvFreeWildBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1147)
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdListTable.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdListEntry_Object = MibTableRow
exampleWildBcdProvFreeWildBcdListEntry = _ExampleWildBcdProvFreeWildBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1147, 1)
)
exampleWildBcdProvFreeWildBcdListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleWildBcdProvFreeWildBcdListValue"),
)
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdListEntry.setStatus("mandatory")


class _ExampleWildBcdProvFreeWildBcdListValue_Type(WildcardedDigitString):
    """Custom type exampleWildBcdProvFreeWildBcdListValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExampleWildBcdProvFreeWildBcdListValue_Type.__name__ = "WildcardedDigitString"
_ExampleWildBcdProvFreeWildBcdListValue_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdListValue = _ExampleWildBcdProvFreeWildBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1147, 1, 1),
    _ExampleWildBcdProvFreeWildBcdListValue_Type()
)
exampleWildBcdProvFreeWildBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdListValue.setStatus("mandatory")
_ExampleWildBcdProvFreeWildBcdListRowStatus_Type = RowStatus
_ExampleWildBcdProvFreeWildBcdListRowStatus_Object = MibTableColumn
exampleWildBcdProvFreeWildBcdListRowStatus = _ExampleWildBcdProvFreeWildBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 10, 1147, 1, 2),
    _ExampleWildBcdProvFreeWildBcdListRowStatus_Type()
)
exampleWildBcdProvFreeWildBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleWildBcdProvFreeWildBcdListRowStatus.setStatus("mandatory")
_ExampleEnum_ObjectIdentity = ObjectIdentity
exampleEnum = _ExampleEnum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11)
)
_ExampleEnumRowStatusTable_Object = MibTable
exampleEnumRowStatusTable = _ExampleEnumRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1)
)
if mibBuilder.loadTexts:
    exampleEnumRowStatusTable.setStatus("mandatory")
_ExampleEnumRowStatusEntry_Object = MibTableRow
exampleEnumRowStatusEntry = _ExampleEnumRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1, 1)
)
exampleEnumRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumRowStatusEntry.setStatus("mandatory")
_ExampleEnumRowStatus_Type = RowStatus
_ExampleEnumRowStatus_Object = MibTableColumn
exampleEnumRowStatus = _ExampleEnumRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1, 1, 1),
    _ExampleEnumRowStatus_Type()
)
exampleEnumRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumRowStatus.setStatus("mandatory")
_ExampleEnumComponentName_Type = DisplayString
_ExampleEnumComponentName_Object = MibTableColumn
exampleEnumComponentName = _ExampleEnumComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1, 1, 2),
    _ExampleEnumComponentName_Type()
)
exampleEnumComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleEnumComponentName.setStatus("mandatory")
_ExampleEnumStorageType_Type = StorageType
_ExampleEnumStorageType_Object = MibTableColumn
exampleEnumStorageType = _ExampleEnumStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1, 1, 4),
    _ExampleEnumStorageType_Type()
)
exampleEnumStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleEnumStorageType.setStatus("mandatory")


class _ExampleEnumIndex_Type(Integer32):
    """Custom type exampleEnumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )


_ExampleEnumIndex_Type.__name__ = "Integer32"
_ExampleEnumIndex_Object = MibTableColumn
exampleEnumIndex = _ExampleEnumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1, 1, 10),
    _ExampleEnumIndex_Type()
)
exampleEnumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumIndex.setStatus("mandatory")
_ExampleEnumOperationalTable_Object = MibTable
exampleEnumOperationalTable = _ExampleEnumOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 10)
)
if mibBuilder.loadTexts:
    exampleEnumOperationalTable.setStatus("mandatory")
_ExampleEnumOperationalEntry_Object = MibTableRow
exampleEnumOperationalEntry = _ExampleEnumOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 10, 1)
)
exampleEnumOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumOperationalEntry.setStatus("mandatory")


class _ExampleEnumOperStructEnum_Type(Integer32):
    """Custom type exampleEnumOperStructEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperStructEnum_Type.__name__ = "Integer32"
_ExampleEnumOperStructEnum_Object = MibTableColumn
exampleEnumOperStructEnum = _ExampleEnumOperStructEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 10, 1, 1),
    _ExampleEnumOperStructEnum_Type()
)
exampleEnumOperStructEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnum.setStatus("mandatory")


class _ExampleEnumOperStructEnumSet_Type(OctetString):
    """Custom type exampleEnumOperStructEnumSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExampleEnumOperStructEnumSet_Type.__name__ = "OctetString"
_ExampleEnumOperStructEnumSet_Object = MibTableColumn
exampleEnumOperStructEnumSet = _ExampleEnumOperStructEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 10, 1, 2),
    _ExampleEnumOperStructEnumSet_Type()
)
exampleEnumOperStructEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumSet.setStatus("mandatory")


class _ExampleEnumOperFreeEnum_Type(Integer32):
    """Custom type exampleEnumOperFreeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("february", 1),
          ("january", 0),
          ("june", 5),
          ("march", 2),
          ("may", 4))
    )


_ExampleEnumOperFreeEnum_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnum_Object = MibTableColumn
exampleEnumOperFreeEnum = _ExampleEnumOperFreeEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 10, 1, 3),
    _ExampleEnumOperFreeEnum_Type()
)
exampleEnumOperFreeEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnum.setStatus("mandatory")


class _ExampleEnumOperFreeEnumSet_Type(OctetString):
    """Custom type exampleEnumOperFreeEnumSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExampleEnumOperFreeEnumSet_Type.__name__ = "OctetString"
_ExampleEnumOperFreeEnumSet_Object = MibTableColumn
exampleEnumOperFreeEnumSet = _ExampleEnumOperFreeEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 10, 1, 4),
    _ExampleEnumOperFreeEnumSet_Type()
)
exampleEnumOperFreeEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumSet.setStatus("mandatory")
_ExampleEnumProvisionalTable_Object = MibTable
exampleEnumProvisionalTable = _ExampleEnumProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11)
)
if mibBuilder.loadTexts:
    exampleEnumProvisionalTable.setStatus("mandatory")
_ExampleEnumProvisionalEntry_Object = MibTableRow
exampleEnumProvisionalEntry = _ExampleEnumProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1)
)
exampleEnumProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvisionalEntry.setStatus("mandatory")
_ExampleEnumProvEnumSub_Type = Link
_ExampleEnumProvEnumSub_Object = MibTableColumn
exampleEnumProvEnumSub = _ExampleEnumProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 1),
    _ExampleEnumProvEnumSub_Type()
)
exampleEnumProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvEnumSub.setStatus("mandatory")


class _ExampleEnumProvStructEnum_Type(Integer32):
    """Custom type exampleEnumProvStructEnum based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvStructEnum_Type.__name__ = "Integer32"
_ExampleEnumProvStructEnum_Object = MibTableColumn
exampleEnumProvStructEnum = _ExampleEnumProvStructEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 2),
    _ExampleEnumProvStructEnum_Type()
)
exampleEnumProvStructEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnum.setStatus("mandatory")


class _ExampleEnumProvStructEnumSet_Type(OctetString):
    """Custom type exampleEnumProvStructEnumSet based on OctetString"""
    defaultHexValue = "aa"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExampleEnumProvStructEnumSet_Type.__name__ = "OctetString"
_ExampleEnumProvStructEnumSet_Object = MibTableColumn
exampleEnumProvStructEnumSet = _ExampleEnumProvStructEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 3),
    _ExampleEnumProvStructEnumSet_Type()
)
exampleEnumProvStructEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumSet.setStatus("mandatory")


class _ExampleEnumProvFreeEnum_Type(Integer32):
    """Custom type exampleEnumProvFreeEnum based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("february", 1),
          ("january", 0),
          ("june", 5),
          ("march", 2),
          ("may", 4))
    )


_ExampleEnumProvFreeEnum_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnum_Object = MibTableColumn
exampleEnumProvFreeEnum = _ExampleEnumProvFreeEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 4),
    _ExampleEnumProvFreeEnum_Type()
)
exampleEnumProvFreeEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnum.setStatus("mandatory")


class _ExampleEnumProvFreeEnum1_Type(Integer32):
    """Custom type exampleEnumProvFreeEnum1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("apple", 1),
          ("banana", 3),
          ("grapes", 12),
          ("orange", 2),
          ("pear", 11),
          ("pineapple", 13),
          ("watermelon", 14))
    )


_ExampleEnumProvFreeEnum1_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnum1_Object = MibTableColumn
exampleEnumProvFreeEnum1 = _ExampleEnumProvFreeEnum1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 5),
    _ExampleEnumProvFreeEnum1_Type()
)
exampleEnumProvFreeEnum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnum1.setStatus("mandatory")


class _ExampleEnumProvFreeEnumSet_Type(OctetString):
    """Custom type exampleEnumProvFreeEnumSet based on OctetString"""
    defaultHexValue = "0070"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExampleEnumProvFreeEnumSet_Type.__name__ = "OctetString"
_ExampleEnumProvFreeEnumSet_Object = MibTableColumn
exampleEnumProvFreeEnumSet = _ExampleEnumProvFreeEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 6),
    _ExampleEnumProvFreeEnumSet_Type()
)
exampleEnumProvFreeEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumSet.setStatus("mandatory")


class _ExampleEnumProvFreeEnumSet1_Type(OctetString):
    """Custom type exampleEnumProvFreeEnumSet1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExampleEnumProvFreeEnumSet1_Type.__name__ = "OctetString"
_ExampleEnumProvFreeEnumSet1_Object = MibTableColumn
exampleEnumProvFreeEnumSet1 = _ExampleEnumProvFreeEnumSet1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 11, 1, 7),
    _ExampleEnumProvFreeEnumSet1_Type()
)
exampleEnumProvFreeEnumSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumSet1.setStatus("mandatory")
_ExampleEnumOperStructEnumVectorTable_Object = MibTable
exampleEnumOperStructEnumVectorTable = _ExampleEnumOperStructEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1162)
)
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumVectorTable.setStatus("mandatory")
_ExampleEnumOperStructEnumVectorEntry_Object = MibTableRow
exampleEnumOperStructEnumVectorEntry = _ExampleEnumOperStructEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1162, 1)
)
exampleEnumOperStructEnumVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperStructEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumVectorEntry.setStatus("mandatory")


class _ExampleEnumOperStructEnumVectorIndex_Type(Integer32):
    """Custom type exampleEnumOperStructEnumVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperStructEnumVectorIndex_Type.__name__ = "Integer32"
_ExampleEnumOperStructEnumVectorIndex_Object = MibTableColumn
exampleEnumOperStructEnumVectorIndex = _ExampleEnumOperStructEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1162, 1, 1),
    _ExampleEnumOperStructEnumVectorIndex_Type()
)
exampleEnumOperStructEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumVectorIndex.setStatus("mandatory")


class _ExampleEnumOperStructEnumVectorValue_Type(Integer32):
    """Custom type exampleEnumOperStructEnumVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperStructEnumVectorValue_Type.__name__ = "Integer32"
_ExampleEnumOperStructEnumVectorValue_Object = MibTableColumn
exampleEnumOperStructEnumVectorValue = _ExampleEnumOperStructEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1162, 1, 2),
    _ExampleEnumOperStructEnumVectorValue_Type()
)
exampleEnumOperStructEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumVectorValue.setStatus("mandatory")
_ExampleEnumOperStructEnumArrayTable_Object = MibTable
exampleEnumOperStructEnumArrayTable = _ExampleEnumOperStructEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1163)
)
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumArrayTable.setStatus("mandatory")
_ExampleEnumOperStructEnumArrayEntry_Object = MibTableRow
exampleEnumOperStructEnumArrayEntry = _ExampleEnumOperStructEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1163, 1)
)
exampleEnumOperStructEnumArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperStructEnumArrayMonthIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperStructEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumArrayEntry.setStatus("mandatory")


class _ExampleEnumOperStructEnumArrayMonthIndex_Type(Integer32):
    """Custom type exampleEnumOperStructEnumArrayMonthIndex based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumOperStructEnumArrayMonthIndex_Type.__name__ = "Integer32"
_ExampleEnumOperStructEnumArrayMonthIndex_Object = MibTableColumn
exampleEnumOperStructEnumArrayMonthIndex = _ExampleEnumOperStructEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1163, 1, 1),
    _ExampleEnumOperStructEnumArrayMonthIndex_Type()
)
exampleEnumOperStructEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumArrayMonthIndex.setStatus("mandatory")


class _ExampleEnumOperStructEnumArrayDayIndex_Type(Integer32):
    """Custom type exampleEnumOperStructEnumArrayDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fridayaaaa", 4),
          ("mondayaaaa", 0),
          ("saturdayaaaa", 5),
          ("sundayaaaa", 6),
          ("thursdayaaaa", 3),
          ("tuesdayaaaa", 1),
          ("wednesdayaaaa", 2))
    )


_ExampleEnumOperStructEnumArrayDayIndex_Type.__name__ = "Integer32"
_ExampleEnumOperStructEnumArrayDayIndex_Object = MibTableColumn
exampleEnumOperStructEnumArrayDayIndex = _ExampleEnumOperStructEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1163, 1, 2),
    _ExampleEnumOperStructEnumArrayDayIndex_Type()
)
exampleEnumOperStructEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumArrayDayIndex.setStatus("mandatory")


class _ExampleEnumOperStructEnumArrayValue_Type(Integer32):
    """Custom type exampleEnumOperStructEnumArrayValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumOperStructEnumArrayValue_Type.__name__ = "Integer32"
_ExampleEnumOperStructEnumArrayValue_Object = MibTableColumn
exampleEnumOperStructEnumArrayValue = _ExampleEnumOperStructEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1163, 1, 3),
    _ExampleEnumOperStructEnumArrayValue_Type()
)
exampleEnumOperStructEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperStructEnumArrayValue.setStatus("mandatory")
_ExampleEnumOperFreeEnumVectorTable_Object = MibTable
exampleEnumOperFreeEnumVectorTable = _ExampleEnumOperFreeEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1164)
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumVectorTable.setStatus("mandatory")
_ExampleEnumOperFreeEnumVectorEntry_Object = MibTableRow
exampleEnumOperFreeEnumVectorEntry = _ExampleEnumOperFreeEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1164, 1)
)
exampleEnumOperFreeEnumVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperFreeEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumVectorEntry.setStatus("mandatory")


class _ExampleEnumOperFreeEnumVectorIndex_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperFreeEnumVectorIndex_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumVectorIndex_Object = MibTableColumn
exampleEnumOperFreeEnumVectorIndex = _ExampleEnumOperFreeEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1164, 1, 1),
    _ExampleEnumOperFreeEnumVectorIndex_Type()
)
exampleEnumOperFreeEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumVectorIndex.setStatus("mandatory")


class _ExampleEnumOperFreeEnumVectorValue_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperFreeEnumVectorValue_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumVectorValue_Object = MibTableColumn
exampleEnumOperFreeEnumVectorValue = _ExampleEnumOperFreeEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1164, 1, 2),
    _ExampleEnumOperFreeEnumVectorValue_Type()
)
exampleEnumOperFreeEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumVectorValue.setStatus("mandatory")
_ExampleEnumOperFreeEnumArrayTable_Object = MibTable
exampleEnumOperFreeEnumArrayTable = _ExampleEnumOperFreeEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1165)
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumArrayTable.setStatus("mandatory")
_ExampleEnumOperFreeEnumArrayEntry_Object = MibTableRow
exampleEnumOperFreeEnumArrayEntry = _ExampleEnumOperFreeEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1165, 1)
)
exampleEnumOperFreeEnumArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperFreeEnumArrayMonthIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperFreeEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumArrayEntry.setStatus("mandatory")


class _ExampleEnumOperFreeEnumArrayMonthIndex_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumArrayMonthIndex based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumOperFreeEnumArrayMonthIndex_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumArrayMonthIndex_Object = MibTableColumn
exampleEnumOperFreeEnumArrayMonthIndex = _ExampleEnumOperFreeEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1165, 1, 1),
    _ExampleEnumOperFreeEnumArrayMonthIndex_Type()
)
exampleEnumOperFreeEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumArrayMonthIndex.setStatus("mandatory")


class _ExampleEnumOperFreeEnumArrayDayIndex_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumArrayDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperFreeEnumArrayDayIndex_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumArrayDayIndex_Object = MibTableColumn
exampleEnumOperFreeEnumArrayDayIndex = _ExampleEnumOperFreeEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1165, 1, 2),
    _ExampleEnumOperFreeEnumArrayDayIndex_Type()
)
exampleEnumOperFreeEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumArrayDayIndex.setStatus("mandatory")


class _ExampleEnumOperFreeEnumArrayValue_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumArrayValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumOperFreeEnumArrayValue_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumArrayValue_Object = MibTableColumn
exampleEnumOperFreeEnumArrayValue = _ExampleEnumOperFreeEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1165, 1, 3),
    _ExampleEnumOperFreeEnumArrayValue_Type()
)
exampleEnumOperFreeEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumArrayValue.setStatus("mandatory")
_ExampleEnumOperFreeEnumReplicatedTable_Object = MibTable
exampleEnumOperFreeEnumReplicatedTable = _ExampleEnumOperFreeEnumReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1166)
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumReplicatedTable.setStatus("mandatory")
_ExampleEnumOperFreeEnumReplicatedEntry_Object = MibTableRow
exampleEnumOperFreeEnumReplicatedEntry = _ExampleEnumOperFreeEnumReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1166, 1)
)
exampleEnumOperFreeEnumReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperFreeEnumReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumReplicatedEntry.setStatus("mandatory")


class _ExampleEnumOperFreeEnumReplicatedIndex_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumOperFreeEnumReplicatedIndex_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumReplicatedIndex_Object = MibTableColumn
exampleEnumOperFreeEnumReplicatedIndex = _ExampleEnumOperFreeEnumReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1166, 1, 1),
    _ExampleEnumOperFreeEnumReplicatedIndex_Type()
)
exampleEnumOperFreeEnumReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumReplicatedIndex.setStatus("mandatory")


class _ExampleEnumOperFreeEnumReplicatedValue_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumReplicatedValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumOperFreeEnumReplicatedValue_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumReplicatedValue_Object = MibTableColumn
exampleEnumOperFreeEnumReplicatedValue = _ExampleEnumOperFreeEnumReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1166, 1, 2),
    _ExampleEnumOperFreeEnumReplicatedValue_Type()
)
exampleEnumOperFreeEnumReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumReplicatedValue.setStatus("mandatory")
_ExampleEnumOperFreeEnumReplicatedRowStatus_Type = RowStatus
_ExampleEnumOperFreeEnumReplicatedRowStatus_Object = MibTableColumn
exampleEnumOperFreeEnumReplicatedRowStatus = _ExampleEnumOperFreeEnumReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1166, 1, 3),
    _ExampleEnumOperFreeEnumReplicatedRowStatus_Type()
)
exampleEnumOperFreeEnumReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumReplicatedRowStatus.setStatus("mandatory")
_ExampleEnumOperFreeEnumListTable_Object = MibTable
exampleEnumOperFreeEnumListTable = _ExampleEnumOperFreeEnumListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1167)
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumListTable.setStatus("mandatory")
_ExampleEnumOperFreeEnumListEntry_Object = MibTableRow
exampleEnumOperFreeEnumListEntry = _ExampleEnumOperFreeEnumListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1167, 1)
)
exampleEnumOperFreeEnumListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumOperFreeEnumListValue"),
)
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumListEntry.setStatus("mandatory")


class _ExampleEnumOperFreeEnumListValue_Type(Integer32):
    """Custom type exampleEnumOperFreeEnumListValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumOperFreeEnumListValue_Type.__name__ = "Integer32"
_ExampleEnumOperFreeEnumListValue_Object = MibTableColumn
exampleEnumOperFreeEnumListValue = _ExampleEnumOperFreeEnumListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1167, 1, 1),
    _ExampleEnumOperFreeEnumListValue_Type()
)
exampleEnumOperFreeEnumListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumListValue.setStatus("mandatory")
_ExampleEnumOperFreeEnumListRowStatus_Type = RowStatus
_ExampleEnumOperFreeEnumListRowStatus_Object = MibTableColumn
exampleEnumOperFreeEnumListRowStatus = _ExampleEnumOperFreeEnumListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1167, 1, 2),
    _ExampleEnumOperFreeEnumListRowStatus_Type()
)
exampleEnumOperFreeEnumListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleEnumOperFreeEnumListRowStatus.setStatus("mandatory")
_ExampleEnumProvStructEnumVectorTable_Object = MibTable
exampleEnumProvStructEnumVectorTable = _ExampleEnumProvStructEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1168)
)
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumVectorTable.setStatus("mandatory")
_ExampleEnumProvStructEnumVectorEntry_Object = MibTableRow
exampleEnumProvStructEnumVectorEntry = _ExampleEnumProvStructEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1168, 1)
)
exampleEnumProvStructEnumVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvStructEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumVectorEntry.setStatus("mandatory")


class _ExampleEnumProvStructEnumVectorIndex_Type(Integer32):
    """Custom type exampleEnumProvStructEnumVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvStructEnumVectorIndex_Type.__name__ = "Integer32"
_ExampleEnumProvStructEnumVectorIndex_Object = MibTableColumn
exampleEnumProvStructEnumVectorIndex = _ExampleEnumProvStructEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1168, 1, 1),
    _ExampleEnumProvStructEnumVectorIndex_Type()
)
exampleEnumProvStructEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumVectorIndex.setStatus("mandatory")


class _ExampleEnumProvStructEnumVectorValue_Type(Integer32):
    """Custom type exampleEnumProvStructEnumVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvStructEnumVectorValue_Type.__name__ = "Integer32"
_ExampleEnumProvStructEnumVectorValue_Object = MibTableColumn
exampleEnumProvStructEnumVectorValue = _ExampleEnumProvStructEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1168, 1, 2),
    _ExampleEnumProvStructEnumVectorValue_Type()
)
exampleEnumProvStructEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumVectorValue.setStatus("mandatory")
_ExampleEnumProvStructEnumArrayTable_Object = MibTable
exampleEnumProvStructEnumArrayTable = _ExampleEnumProvStructEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1169)
)
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumArrayTable.setStatus("mandatory")
_ExampleEnumProvStructEnumArrayEntry_Object = MibTableRow
exampleEnumProvStructEnumArrayEntry = _ExampleEnumProvStructEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1169, 1)
)
exampleEnumProvStructEnumArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvStructEnumArrayMonthIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvStructEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumArrayEntry.setStatus("mandatory")


class _ExampleEnumProvStructEnumArrayMonthIndex_Type(Integer32):
    """Custom type exampleEnumProvStructEnumArrayMonthIndex based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvStructEnumArrayMonthIndex_Type.__name__ = "Integer32"
_ExampleEnumProvStructEnumArrayMonthIndex_Object = MibTableColumn
exampleEnumProvStructEnumArrayMonthIndex = _ExampleEnumProvStructEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1169, 1, 1),
    _ExampleEnumProvStructEnumArrayMonthIndex_Type()
)
exampleEnumProvStructEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumArrayMonthIndex.setStatus("mandatory")


class _ExampleEnumProvStructEnumArrayDayIndex_Type(Integer32):
    """Custom type exampleEnumProvStructEnumArrayDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvStructEnumArrayDayIndex_Type.__name__ = "Integer32"
_ExampleEnumProvStructEnumArrayDayIndex_Object = MibTableColumn
exampleEnumProvStructEnumArrayDayIndex = _ExampleEnumProvStructEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1169, 1, 2),
    _ExampleEnumProvStructEnumArrayDayIndex_Type()
)
exampleEnumProvStructEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumArrayDayIndex.setStatus("mandatory")


class _ExampleEnumProvStructEnumArrayValue_Type(Integer32):
    """Custom type exampleEnumProvStructEnumArrayValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvStructEnumArrayValue_Type.__name__ = "Integer32"
_ExampleEnumProvStructEnumArrayValue_Object = MibTableColumn
exampleEnumProvStructEnumArrayValue = _ExampleEnumProvStructEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1169, 1, 3),
    _ExampleEnumProvStructEnumArrayValue_Type()
)
exampleEnumProvStructEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvStructEnumArrayValue.setStatus("mandatory")
_ExampleEnumProvFreeEnumVectorTable_Object = MibTable
exampleEnumProvFreeEnumVectorTable = _ExampleEnumProvFreeEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1170)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVectorTable.setStatus("mandatory")
_ExampleEnumProvFreeEnumVectorEntry_Object = MibTableRow
exampleEnumProvFreeEnumVectorEntry = _ExampleEnumProvFreeEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1170, 1)
)
exampleEnumProvFreeEnumVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVectorEntry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumVectorIndex_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvFreeEnumVectorIndex_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumVectorIndex_Object = MibTableColumn
exampleEnumProvFreeEnumVectorIndex = _ExampleEnumProvFreeEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1170, 1, 1),
    _ExampleEnumProvFreeEnumVectorIndex_Type()
)
exampleEnumProvFreeEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVectorIndex.setStatus("mandatory")


class _ExampleEnumProvFreeEnumVectorValue_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvFreeEnumVectorValue_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumVectorValue_Object = MibTableColumn
exampleEnumProvFreeEnumVectorValue = _ExampleEnumProvFreeEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1170, 1, 2),
    _ExampleEnumProvFreeEnumVectorValue_Type()
)
exampleEnumProvFreeEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVectorValue.setStatus("mandatory")
_ExampleEnumProvFreeEnumVector1Table_Object = MibTable
exampleEnumProvFreeEnumVector1Table = _ExampleEnumProvFreeEnumVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1171)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVector1Table.setStatus("mandatory")
_ExampleEnumProvFreeEnumVector1Entry_Object = MibTableRow
exampleEnumProvFreeEnumVector1Entry = _ExampleEnumProvFreeEnumVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1171, 1)
)
exampleEnumProvFreeEnumVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumVector1Index"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVector1Entry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumVector1Index_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvFreeEnumVector1Index_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumVector1Index_Object = MibTableColumn
exampleEnumProvFreeEnumVector1Index = _ExampleEnumProvFreeEnumVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1171, 1, 1),
    _ExampleEnumProvFreeEnumVector1Index_Type()
)
exampleEnumProvFreeEnumVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVector1Index.setStatus("mandatory")


class _ExampleEnumProvFreeEnumVector1Value_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumVector1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("february", 1),
          ("january", 0),
          ("march", 2),
          ("may", 4))
    )


_ExampleEnumProvFreeEnumVector1Value_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumVector1Value_Object = MibTableColumn
exampleEnumProvFreeEnumVector1Value = _ExampleEnumProvFreeEnumVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1171, 1, 2),
    _ExampleEnumProvFreeEnumVector1Value_Type()
)
exampleEnumProvFreeEnumVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumVector1Value.setStatus("mandatory")
_ExampleEnumProvFreeEnumArrayTable_Object = MibTable
exampleEnumProvFreeEnumArrayTable = _ExampleEnumProvFreeEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1172)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArrayTable.setStatus("mandatory")
_ExampleEnumProvFreeEnumArrayEntry_Object = MibTableRow
exampleEnumProvFreeEnumArrayEntry = _ExampleEnumProvFreeEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1172, 1)
)
exampleEnumProvFreeEnumArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumArrayMonthIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArrayEntry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumArrayMonthIndex_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumArrayMonthIndex based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvFreeEnumArrayMonthIndex_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumArrayMonthIndex_Object = MibTableColumn
exampleEnumProvFreeEnumArrayMonthIndex = _ExampleEnumProvFreeEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1172, 1, 1),
    _ExampleEnumProvFreeEnumArrayMonthIndex_Type()
)
exampleEnumProvFreeEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArrayMonthIndex.setStatus("mandatory")


class _ExampleEnumProvFreeEnumArrayDayIndex_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumArrayDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvFreeEnumArrayDayIndex_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumArrayDayIndex_Object = MibTableColumn
exampleEnumProvFreeEnumArrayDayIndex = _ExampleEnumProvFreeEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1172, 1, 2),
    _ExampleEnumProvFreeEnumArrayDayIndex_Type()
)
exampleEnumProvFreeEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArrayDayIndex.setStatus("mandatory")


class _ExampleEnumProvFreeEnumArrayValue_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumArrayValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvFreeEnumArrayValue_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumArrayValue_Object = MibTableColumn
exampleEnumProvFreeEnumArrayValue = _ExampleEnumProvFreeEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1172, 1, 3),
    _ExampleEnumProvFreeEnumArrayValue_Type()
)
exampleEnumProvFreeEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArrayValue.setStatus("mandatory")
_ExampleEnumProvFreeEnumArray1Table_Object = MibTable
exampleEnumProvFreeEnumArray1Table = _ExampleEnumProvFreeEnumArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1173)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArray1Table.setStatus("mandatory")
_ExampleEnumProvFreeEnumArray1Entry_Object = MibTableRow
exampleEnumProvFreeEnumArray1Entry = _ExampleEnumProvFreeEnumArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1173, 1)
)
exampleEnumProvFreeEnumArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumArray1MonthIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumArray1DayIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArray1Entry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumArray1MonthIndex_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumArray1MonthIndex based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvFreeEnumArray1MonthIndex_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumArray1MonthIndex_Object = MibTableColumn
exampleEnumProvFreeEnumArray1MonthIndex = _ExampleEnumProvFreeEnumArray1MonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1173, 1, 1),
    _ExampleEnumProvFreeEnumArray1MonthIndex_Type()
)
exampleEnumProvFreeEnumArray1MonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArray1MonthIndex.setStatus("mandatory")


class _ExampleEnumProvFreeEnumArray1DayIndex_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumArray1DayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvFreeEnumArray1DayIndex_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumArray1DayIndex_Object = MibTableColumn
exampleEnumProvFreeEnumArray1DayIndex = _ExampleEnumProvFreeEnumArray1DayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1173, 1, 2),
    _ExampleEnumProvFreeEnumArray1DayIndex_Type()
)
exampleEnumProvFreeEnumArray1DayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArray1DayIndex.setStatus("mandatory")


class _ExampleEnumProvFreeEnumArray1Value_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumArray1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("apple", 1),
          ("banana", 3),
          ("grapes", 12),
          ("orange", 2),
          ("pear", 11),
          ("pineapple", 13),
          ("watermelon", 14))
    )


_ExampleEnumProvFreeEnumArray1Value_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumArray1Value_Object = MibTableColumn
exampleEnumProvFreeEnumArray1Value = _ExampleEnumProvFreeEnumArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1173, 1, 3),
    _ExampleEnumProvFreeEnumArray1Value_Type()
)
exampleEnumProvFreeEnumArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumArray1Value.setStatus("mandatory")
_ExampleEnumProvFreeEnumReplicatedTable_Object = MibTable
exampleEnumProvFreeEnumReplicatedTable = _ExampleEnumProvFreeEnumReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1174)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumReplicatedTable.setStatus("mandatory")
_ExampleEnumProvFreeEnumReplicatedEntry_Object = MibTableRow
exampleEnumProvFreeEnumReplicatedEntry = _ExampleEnumProvFreeEnumReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1174, 1)
)
exampleEnumProvFreeEnumReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumReplicatedEntry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumReplicatedIndex_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_ExampleEnumProvFreeEnumReplicatedIndex_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumReplicatedIndex_Object = MibTableColumn
exampleEnumProvFreeEnumReplicatedIndex = _ExampleEnumProvFreeEnumReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1174, 1, 1),
    _ExampleEnumProvFreeEnumReplicatedIndex_Type()
)
exampleEnumProvFreeEnumReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumReplicatedIndex.setStatus("mandatory")


class _ExampleEnumProvFreeEnumReplicatedValue_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumReplicatedValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvFreeEnumReplicatedValue_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumReplicatedValue_Object = MibTableColumn
exampleEnumProvFreeEnumReplicatedValue = _ExampleEnumProvFreeEnumReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1174, 1, 2),
    _ExampleEnumProvFreeEnumReplicatedValue_Type()
)
exampleEnumProvFreeEnumReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumReplicatedValue.setStatus("mandatory")
_ExampleEnumProvFreeEnumReplicatedRowStatus_Type = RowStatus
_ExampleEnumProvFreeEnumReplicatedRowStatus_Object = MibTableColumn
exampleEnumProvFreeEnumReplicatedRowStatus = _ExampleEnumProvFreeEnumReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1174, 1, 3),
    _ExampleEnumProvFreeEnumReplicatedRowStatus_Type()
)
exampleEnumProvFreeEnumReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumReplicatedRowStatus.setStatus("mandatory")
_ExampleEnumProvFreeEnumListTable_Object = MibTable
exampleEnumProvFreeEnumListTable = _ExampleEnumProvFreeEnumListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1175)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumListTable.setStatus("mandatory")
_ExampleEnumProvFreeEnumListEntry_Object = MibTableRow
exampleEnumProvFreeEnumListEntry = _ExampleEnumProvFreeEnumListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1175, 1)
)
exampleEnumProvFreeEnumListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumListValue"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumListEntry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumListValue_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumListValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvFreeEnumListValue_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumListValue_Object = MibTableColumn
exampleEnumProvFreeEnumListValue = _ExampleEnumProvFreeEnumListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1175, 1, 1),
    _ExampleEnumProvFreeEnumListValue_Type()
)
exampleEnumProvFreeEnumListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumListValue.setStatus("mandatory")
_ExampleEnumProvFreeEnumListRowStatus_Type = RowStatus
_ExampleEnumProvFreeEnumListRowStatus_Object = MibTableColumn
exampleEnumProvFreeEnumListRowStatus = _ExampleEnumProvFreeEnumListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1175, 1, 2),
    _ExampleEnumProvFreeEnumListRowStatus_Type()
)
exampleEnumProvFreeEnumListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumListRowStatus.setStatus("mandatory")
_ExampleEnumProvFreeEnumList1Table_Object = MibTable
exampleEnumProvFreeEnumList1Table = _ExampleEnumProvFreeEnumList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1176)
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumList1Table.setStatus("mandatory")
_ExampleEnumProvFreeEnumList1Entry_Object = MibTableRow
exampleEnumProvFreeEnumList1Entry = _ExampleEnumProvFreeEnumList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1176, 1)
)
exampleEnumProvFreeEnumList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumProvFreeEnumList1Value"),
)
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumList1Entry.setStatus("mandatory")


class _ExampleEnumProvFreeEnumList1Value_Type(Integer32):
    """Custom type exampleEnumProvFreeEnumList1Value based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_ExampleEnumProvFreeEnumList1Value_Type.__name__ = "Integer32"
_ExampleEnumProvFreeEnumList1Value_Object = MibTableColumn
exampleEnumProvFreeEnumList1Value = _ExampleEnumProvFreeEnumList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1176, 1, 1),
    _ExampleEnumProvFreeEnumList1Value_Type()
)
exampleEnumProvFreeEnumList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumList1Value.setStatus("mandatory")
_ExampleEnumProvFreeEnumList1RowStatus_Type = RowStatus
_ExampleEnumProvFreeEnumList1RowStatus_Object = MibTableColumn
exampleEnumProvFreeEnumList1RowStatus = _ExampleEnumProvFreeEnumList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 11, 1176, 1, 2),
    _ExampleEnumProvFreeEnumList1RowStatus_Type()
)
exampleEnumProvFreeEnumList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleEnumProvFreeEnumList1RowStatus.setStatus("mandatory")
_ExampleObjectId_ObjectIdentity = ObjectIdentity
exampleObjectId = _ExampleObjectId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12)
)
_ExampleObjectIdRowStatusTable_Object = MibTable
exampleObjectIdRowStatusTable = _ExampleObjectIdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1)
)
if mibBuilder.loadTexts:
    exampleObjectIdRowStatusTable.setStatus("mandatory")
_ExampleObjectIdRowStatusEntry_Object = MibTableRow
exampleObjectIdRowStatusEntry = _ExampleObjectIdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1, 1)
)
exampleObjectIdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
)
if mibBuilder.loadTexts:
    exampleObjectIdRowStatusEntry.setStatus("mandatory")
_ExampleObjectIdRowStatus_Type = RowStatus
_ExampleObjectIdRowStatus_Object = MibTableColumn
exampleObjectIdRowStatus = _ExampleObjectIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1, 1, 1),
    _ExampleObjectIdRowStatus_Type()
)
exampleObjectIdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdRowStatus.setStatus("mandatory")
_ExampleObjectIdComponentName_Type = DisplayString
_ExampleObjectIdComponentName_Object = MibTableColumn
exampleObjectIdComponentName = _ExampleObjectIdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1, 1, 2),
    _ExampleObjectIdComponentName_Type()
)
exampleObjectIdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleObjectIdComponentName.setStatus("mandatory")
_ExampleObjectIdStorageType_Type = StorageType
_ExampleObjectIdStorageType_Object = MibTableColumn
exampleObjectIdStorageType = _ExampleObjectIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1, 1, 4),
    _ExampleObjectIdStorageType_Type()
)
exampleObjectIdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleObjectIdStorageType.setStatus("mandatory")
_ExampleObjectIdIndex_Type = ObjectIdentifier
_ExampleObjectIdIndex_Object = MibTableColumn
exampleObjectIdIndex = _ExampleObjectIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1, 1, 10),
    _ExampleObjectIdIndex_Type()
)
exampleObjectIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleObjectIdIndex.setStatus("mandatory")
_ExampleObjectIdOperationalTable_Object = MibTable
exampleObjectIdOperationalTable = _ExampleObjectIdOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 10)
)
if mibBuilder.loadTexts:
    exampleObjectIdOperationalTable.setStatus("mandatory")
_ExampleObjectIdOperationalEntry_Object = MibTableRow
exampleObjectIdOperationalEntry = _ExampleObjectIdOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 10, 1)
)
exampleObjectIdOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
)
if mibBuilder.loadTexts:
    exampleObjectIdOperationalEntry.setStatus("mandatory")
_ExampleObjectIdOperFreeObjId_Type = ObjectIdentifier
_ExampleObjectIdOperFreeObjId_Object = MibTableColumn
exampleObjectIdOperFreeObjId = _ExampleObjectIdOperFreeObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 10, 1, 1),
    _ExampleObjectIdOperFreeObjId_Type()
)
exampleObjectIdOperFreeObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjId.setStatus("mandatory")
_ExampleObjectIdProvisionalTable_Object = MibTable
exampleObjectIdProvisionalTable = _ExampleObjectIdProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 11)
)
if mibBuilder.loadTexts:
    exampleObjectIdProvisionalTable.setStatus("mandatory")
_ExampleObjectIdProvisionalEntry_Object = MibTableRow
exampleObjectIdProvisionalEntry = _ExampleObjectIdProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 11, 1)
)
exampleObjectIdProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
)
if mibBuilder.loadTexts:
    exampleObjectIdProvisionalEntry.setStatus("mandatory")
_ExampleObjectIdProvEnumSub_Type = Link
_ExampleObjectIdProvEnumSub_Object = MibTableColumn
exampleObjectIdProvEnumSub = _ExampleObjectIdProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 11, 1, 1),
    _ExampleObjectIdProvEnumSub_Type()
)
exampleObjectIdProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdProvEnumSub.setStatus("mandatory")
_ExampleObjectIdProvFreeObjId_Type = ObjectIdentifier
_ExampleObjectIdProvFreeObjId_Object = MibTableColumn
exampleObjectIdProvFreeObjId = _ExampleObjectIdProvFreeObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 11, 1, 2),
    _ExampleObjectIdProvFreeObjId_Type()
)
exampleObjectIdProvFreeObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjId.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdReplicatedTable_Object = MibTable
exampleObjectIdOperFreeObjIdReplicatedTable = _ExampleObjectIdOperFreeObjIdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1116)
)
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdReplicatedTable.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdReplicatedEntry_Object = MibTableRow
exampleObjectIdOperFreeObjIdReplicatedEntry = _ExampleObjectIdOperFreeObjIdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1116, 1)
)
exampleObjectIdOperFreeObjIdReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdOperFreeObjIdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdReplicatedEntry.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdReplicatedIndex_Type = ObjectIdentifier
_ExampleObjectIdOperFreeObjIdReplicatedIndex_Object = MibTableColumn
exampleObjectIdOperFreeObjIdReplicatedIndex = _ExampleObjectIdOperFreeObjIdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1116, 1, 1),
    _ExampleObjectIdOperFreeObjIdReplicatedIndex_Type()
)
exampleObjectIdOperFreeObjIdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdReplicatedIndex.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdReplicatedValue_Type = ObjectIdentifier
_ExampleObjectIdOperFreeObjIdReplicatedValue_Object = MibTableColumn
exampleObjectIdOperFreeObjIdReplicatedValue = _ExampleObjectIdOperFreeObjIdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1116, 1, 2),
    _ExampleObjectIdOperFreeObjIdReplicatedValue_Type()
)
exampleObjectIdOperFreeObjIdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdReplicatedValue.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdReplicatedRowStatus_Type = RowStatus
_ExampleObjectIdOperFreeObjIdReplicatedRowStatus_Object = MibTableColumn
exampleObjectIdOperFreeObjIdReplicatedRowStatus = _ExampleObjectIdOperFreeObjIdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1116, 1, 3),
    _ExampleObjectIdOperFreeObjIdReplicatedRowStatus_Type()
)
exampleObjectIdOperFreeObjIdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdReplicatedRowStatus.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdListTable_Object = MibTable
exampleObjectIdOperFreeObjIdListTable = _ExampleObjectIdOperFreeObjIdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1117)
)
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdListTable.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdListEntry_Object = MibTableRow
exampleObjectIdOperFreeObjIdListEntry = _ExampleObjectIdOperFreeObjIdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1117, 1)
)
exampleObjectIdOperFreeObjIdListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdOperFreeObjIdListValue"),
)
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdListEntry.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdListValue_Type = IntegerSequence
_ExampleObjectIdOperFreeObjIdListValue_Object = MibTableColumn
exampleObjectIdOperFreeObjIdListValue = _ExampleObjectIdOperFreeObjIdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1117, 1, 1),
    _ExampleObjectIdOperFreeObjIdListValue_Type()
)
exampleObjectIdOperFreeObjIdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdListValue.setStatus("mandatory")
_ExampleObjectIdOperFreeObjIdListRowStatus_Type = RowStatus
_ExampleObjectIdOperFreeObjIdListRowStatus_Object = MibTableColumn
exampleObjectIdOperFreeObjIdListRowStatus = _ExampleObjectIdOperFreeObjIdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1117, 1, 2),
    _ExampleObjectIdOperFreeObjIdListRowStatus_Type()
)
exampleObjectIdOperFreeObjIdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleObjectIdOperFreeObjIdListRowStatus.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdReplicatedTable_Object = MibTable
exampleObjectIdProvFreeObjIdReplicatedTable = _ExampleObjectIdProvFreeObjIdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1118)
)
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdReplicatedTable.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdReplicatedEntry_Object = MibTableRow
exampleObjectIdProvFreeObjIdReplicatedEntry = _ExampleObjectIdProvFreeObjIdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1118, 1)
)
exampleObjectIdProvFreeObjIdReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdProvFreeObjIdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdReplicatedEntry.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdReplicatedIndex_Type = ObjectIdentifier
_ExampleObjectIdProvFreeObjIdReplicatedIndex_Object = MibTableColumn
exampleObjectIdProvFreeObjIdReplicatedIndex = _ExampleObjectIdProvFreeObjIdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1118, 1, 1),
    _ExampleObjectIdProvFreeObjIdReplicatedIndex_Type()
)
exampleObjectIdProvFreeObjIdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdReplicatedIndex.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdReplicatedValue_Type = ObjectIdentifier
_ExampleObjectIdProvFreeObjIdReplicatedValue_Object = MibTableColumn
exampleObjectIdProvFreeObjIdReplicatedValue = _ExampleObjectIdProvFreeObjIdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1118, 1, 2),
    _ExampleObjectIdProvFreeObjIdReplicatedValue_Type()
)
exampleObjectIdProvFreeObjIdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdReplicatedValue.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdReplicatedRowStatus_Type = RowStatus
_ExampleObjectIdProvFreeObjIdReplicatedRowStatus_Object = MibTableColumn
exampleObjectIdProvFreeObjIdReplicatedRowStatus = _ExampleObjectIdProvFreeObjIdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1118, 1, 3),
    _ExampleObjectIdProvFreeObjIdReplicatedRowStatus_Type()
)
exampleObjectIdProvFreeObjIdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdReplicatedRowStatus.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdListTable_Object = MibTable
exampleObjectIdProvFreeObjIdListTable = _ExampleObjectIdProvFreeObjIdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1119)
)
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdListTable.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdListEntry_Object = MibTableRow
exampleObjectIdProvFreeObjIdListEntry = _ExampleObjectIdProvFreeObjIdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1119, 1)
)
exampleObjectIdProvFreeObjIdListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjectIdProvFreeObjIdListValue"),
)
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdListEntry.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdListValue_Type = IntegerSequence
_ExampleObjectIdProvFreeObjIdListValue_Object = MibTableColumn
exampleObjectIdProvFreeObjIdListValue = _ExampleObjectIdProvFreeObjIdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1119, 1, 1),
    _ExampleObjectIdProvFreeObjIdListValue_Type()
)
exampleObjectIdProvFreeObjIdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdListValue.setStatus("mandatory")
_ExampleObjectIdProvFreeObjIdListRowStatus_Type = RowStatus
_ExampleObjectIdProvFreeObjIdListRowStatus_Object = MibTableColumn
exampleObjectIdProvFreeObjIdListRowStatus = _ExampleObjectIdProvFreeObjIdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 12, 1119, 1, 2),
    _ExampleObjectIdProvFreeObjIdListRowStatus_Type()
)
exampleObjectIdProvFreeObjIdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleObjectIdProvFreeObjIdListRowStatus.setStatus("mandatory")
_ExampleSequence_ObjectIdentity = ObjectIdentity
exampleSequence = _ExampleSequence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13)
)
_ExampleSequenceRowStatusTable_Object = MibTable
exampleSequenceRowStatusTable = _ExampleSequenceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1)
)
if mibBuilder.loadTexts:
    exampleSequenceRowStatusTable.setStatus("mandatory")
_ExampleSequenceRowStatusEntry_Object = MibTableRow
exampleSequenceRowStatusEntry = _ExampleSequenceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1, 1)
)
exampleSequenceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceRowStatusEntry.setStatus("mandatory")
_ExampleSequenceRowStatus_Type = RowStatus
_ExampleSequenceRowStatus_Object = MibTableColumn
exampleSequenceRowStatus = _ExampleSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1, 1, 1),
    _ExampleSequenceRowStatus_Type()
)
exampleSequenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceRowStatus.setStatus("mandatory")
_ExampleSequenceComponentName_Type = DisplayString
_ExampleSequenceComponentName_Object = MibTableColumn
exampleSequenceComponentName = _ExampleSequenceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1, 1, 2),
    _ExampleSequenceComponentName_Type()
)
exampleSequenceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleSequenceComponentName.setStatus("mandatory")
_ExampleSequenceStorageType_Type = StorageType
_ExampleSequenceStorageType_Object = MibTableColumn
exampleSequenceStorageType = _ExampleSequenceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1, 1, 4),
    _ExampleSequenceStorageType_Type()
)
exampleSequenceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleSequenceStorageType.setStatus("mandatory")
_ExampleSequenceIndex_Type = ObjectIdentifier
_ExampleSequenceIndex_Object = MibTableColumn
exampleSequenceIndex = _ExampleSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1, 1, 10),
    _ExampleSequenceIndex_Type()
)
exampleSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSequenceIndex.setStatus("mandatory")
_ExampleSequenceOperationalTable_Object = MibTable
exampleSequenceOperationalTable = _ExampleSequenceOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 10)
)
if mibBuilder.loadTexts:
    exampleSequenceOperationalTable.setStatus("mandatory")
_ExampleSequenceOperationalEntry_Object = MibTableRow
exampleSequenceOperationalEntry = _ExampleSequenceOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 10, 1)
)
exampleSequenceOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceOperationalEntry.setStatus("mandatory")


class _ExampleSequenceOperStructSequence_Type(IntegerSequence):
    """Custom type exampleSequenceOperStructSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_ExampleSequenceOperStructSequence_Type.__name__ = "IntegerSequence"
_ExampleSequenceOperStructSequence_Object = MibTableColumn
exampleSequenceOperStructSequence = _ExampleSequenceOperStructSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 10, 1, 1),
    _ExampleSequenceOperStructSequence_Type()
)
exampleSequenceOperStructSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceOperStructSequence.setStatus("mandatory")


class _ExampleSequenceOperFreeSequence_Type(IntegerSequence):
    """Custom type exampleSequenceOperFreeSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_ExampleSequenceOperFreeSequence_Type.__name__ = "IntegerSequence"
_ExampleSequenceOperFreeSequence_Object = MibTableColumn
exampleSequenceOperFreeSequence = _ExampleSequenceOperFreeSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 10, 1, 2),
    _ExampleSequenceOperFreeSequence_Type()
)
exampleSequenceOperFreeSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequence.setStatus("mandatory")
_ExampleSequenceProvisionalTable_Object = MibTable
exampleSequenceProvisionalTable = _ExampleSequenceProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 11)
)
if mibBuilder.loadTexts:
    exampleSequenceProvisionalTable.setStatus("mandatory")
_ExampleSequenceProvisionalEntry_Object = MibTableRow
exampleSequenceProvisionalEntry = _ExampleSequenceProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 11, 1)
)
exampleSequenceProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceProvisionalEntry.setStatus("mandatory")


class _ExampleSequenceProvStructSequence_Type(IntegerSequence):
    """Custom type exampleSequenceProvStructSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_ExampleSequenceProvStructSequence_Type.__name__ = "IntegerSequence"
_ExampleSequenceProvStructSequence_Object = MibTableColumn
exampleSequenceProvStructSequence = _ExampleSequenceProvStructSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 11, 1, 1),
    _ExampleSequenceProvStructSequence_Type()
)
exampleSequenceProvStructSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceProvStructSequence.setStatus("mandatory")


class _ExampleSequenceProvFreeSequence_Type(IntegerSequence):
    """Custom type exampleSequenceProvFreeSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExampleSequenceProvFreeSequence_Type.__name__ = "IntegerSequence"
_ExampleSequenceProvFreeSequence_Object = MibTableColumn
exampleSequenceProvFreeSequence = _ExampleSequenceProvFreeSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 11, 1, 2),
    _ExampleSequenceProvFreeSequence_Type()
)
exampleSequenceProvFreeSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequence.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceReplicatedTable_Object = MibTable
exampleSequenceOperFreeSequenceReplicatedTable = _ExampleSequenceOperFreeSequenceReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1112)
)
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceReplicatedTable.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceReplicatedEntry_Object = MibTableRow
exampleSequenceOperFreeSequenceReplicatedEntry = _ExampleSequenceOperFreeSequenceReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1112, 1)
)
exampleSequenceOperFreeSequenceReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceOperFreeSequenceReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceReplicatedEntry.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceReplicatedIndex_Type = ObjectIdentifier
_ExampleSequenceOperFreeSequenceReplicatedIndex_Object = MibTableColumn
exampleSequenceOperFreeSequenceReplicatedIndex = _ExampleSequenceOperFreeSequenceReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1112, 1, 1),
    _ExampleSequenceOperFreeSequenceReplicatedIndex_Type()
)
exampleSequenceOperFreeSequenceReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceReplicatedIndex.setStatus("mandatory")


class _ExampleSequenceOperFreeSequenceReplicatedValue_Type(IntegerSequence):
    """Custom type exampleSequenceOperFreeSequenceReplicatedValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_ExampleSequenceOperFreeSequenceReplicatedValue_Type.__name__ = "IntegerSequence"
_ExampleSequenceOperFreeSequenceReplicatedValue_Object = MibTableColumn
exampleSequenceOperFreeSequenceReplicatedValue = _ExampleSequenceOperFreeSequenceReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1112, 1, 2),
    _ExampleSequenceOperFreeSequenceReplicatedValue_Type()
)
exampleSequenceOperFreeSequenceReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceReplicatedValue.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceReplicatedRowStatus_Type = RowStatus
_ExampleSequenceOperFreeSequenceReplicatedRowStatus_Object = MibTableColumn
exampleSequenceOperFreeSequenceReplicatedRowStatus = _ExampleSequenceOperFreeSequenceReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1112, 1, 3),
    _ExampleSequenceOperFreeSequenceReplicatedRowStatus_Type()
)
exampleSequenceOperFreeSequenceReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceReplicatedRowStatus.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceListTable_Object = MibTable
exampleSequenceOperFreeSequenceListTable = _ExampleSequenceOperFreeSequenceListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1113)
)
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceListTable.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceListEntry_Object = MibTableRow
exampleSequenceOperFreeSequenceListEntry = _ExampleSequenceOperFreeSequenceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1113, 1)
)
exampleSequenceOperFreeSequenceListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceOperFreeSequenceListValue"),
)
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceListEntry.setStatus("mandatory")


class _ExampleSequenceOperFreeSequenceListValue_Type(IntegerSequence):
    """Custom type exampleSequenceOperFreeSequenceListValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_ExampleSequenceOperFreeSequenceListValue_Type.__name__ = "IntegerSequence"
_ExampleSequenceOperFreeSequenceListValue_Object = MibTableColumn
exampleSequenceOperFreeSequenceListValue = _ExampleSequenceOperFreeSequenceListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1113, 1, 1),
    _ExampleSequenceOperFreeSequenceListValue_Type()
)
exampleSequenceOperFreeSequenceListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceListValue.setStatus("mandatory")
_ExampleSequenceOperFreeSequenceListRowStatus_Type = RowStatus
_ExampleSequenceOperFreeSequenceListRowStatus_Object = MibTableColumn
exampleSequenceOperFreeSequenceListRowStatus = _ExampleSequenceOperFreeSequenceListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1113, 1, 2),
    _ExampleSequenceOperFreeSequenceListRowStatus_Type()
)
exampleSequenceOperFreeSequenceListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSequenceOperFreeSequenceListRowStatus.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceReplicatedTable_Object = MibTable
exampleSequenceProvFreeSequenceReplicatedTable = _ExampleSequenceProvFreeSequenceReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1114)
)
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceReplicatedTable.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceReplicatedEntry_Object = MibTableRow
exampleSequenceProvFreeSequenceReplicatedEntry = _ExampleSequenceProvFreeSequenceReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1114, 1)
)
exampleSequenceProvFreeSequenceReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceProvFreeSequenceReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceReplicatedEntry.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceReplicatedIndex_Type = ObjectIdentifier
_ExampleSequenceProvFreeSequenceReplicatedIndex_Object = MibTableColumn
exampleSequenceProvFreeSequenceReplicatedIndex = _ExampleSequenceProvFreeSequenceReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1114, 1, 1),
    _ExampleSequenceProvFreeSequenceReplicatedIndex_Type()
)
exampleSequenceProvFreeSequenceReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceReplicatedIndex.setStatus("mandatory")


class _ExampleSequenceProvFreeSequenceReplicatedValue_Type(IntegerSequence):
    """Custom type exampleSequenceProvFreeSequenceReplicatedValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_ExampleSequenceProvFreeSequenceReplicatedValue_Type.__name__ = "IntegerSequence"
_ExampleSequenceProvFreeSequenceReplicatedValue_Object = MibTableColumn
exampleSequenceProvFreeSequenceReplicatedValue = _ExampleSequenceProvFreeSequenceReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1114, 1, 2),
    _ExampleSequenceProvFreeSequenceReplicatedValue_Type()
)
exampleSequenceProvFreeSequenceReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceReplicatedValue.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceReplicatedRowStatus_Type = RowStatus
_ExampleSequenceProvFreeSequenceReplicatedRowStatus_Object = MibTableColumn
exampleSequenceProvFreeSequenceReplicatedRowStatus = _ExampleSequenceProvFreeSequenceReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1114, 1, 3),
    _ExampleSequenceProvFreeSequenceReplicatedRowStatus_Type()
)
exampleSequenceProvFreeSequenceReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceReplicatedRowStatus.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceListTable_Object = MibTable
exampleSequenceProvFreeSequenceListTable = _ExampleSequenceProvFreeSequenceListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1115)
)
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceListTable.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceListEntry_Object = MibTableRow
exampleSequenceProvFreeSequenceListEntry = _ExampleSequenceProvFreeSequenceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1115, 1)
)
exampleSequenceProvFreeSequenceListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceProvFreeSequenceListValue"),
)
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceListEntry.setStatus("mandatory")


class _ExampleSequenceProvFreeSequenceListValue_Type(IntegerSequence):
    """Custom type exampleSequenceProvFreeSequenceListValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_ExampleSequenceProvFreeSequenceListValue_Type.__name__ = "IntegerSequence"
_ExampleSequenceProvFreeSequenceListValue_Object = MibTableColumn
exampleSequenceProvFreeSequenceListValue = _ExampleSequenceProvFreeSequenceListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1115, 1, 1),
    _ExampleSequenceProvFreeSequenceListValue_Type()
)
exampleSequenceProvFreeSequenceListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceListValue.setStatus("mandatory")
_ExampleSequenceProvFreeSequenceListRowStatus_Type = RowStatus
_ExampleSequenceProvFreeSequenceListRowStatus_Object = MibTableColumn
exampleSequenceProvFreeSequenceListRowStatus = _ExampleSequenceProvFreeSequenceListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 13, 1115, 1, 2),
    _ExampleSequenceProvFreeSequenceListRowStatus_Type()
)
exampleSequenceProvFreeSequenceListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSequenceProvFreeSequenceListRowStatus.setStatus("mandatory")
_ExampleSigned_ObjectIdentity = ObjectIdentity
exampleSigned = _ExampleSigned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14)
)
_ExampleSignedRowStatusTable_Object = MibTable
exampleSignedRowStatusTable = _ExampleSignedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1)
)
if mibBuilder.loadTexts:
    exampleSignedRowStatusTable.setStatus("mandatory")
_ExampleSignedRowStatusEntry_Object = MibTableRow
exampleSignedRowStatusEntry = _ExampleSignedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1, 1)
)
exampleSignedRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedRowStatusEntry.setStatus("mandatory")
_ExampleSignedRowStatus_Type = RowStatus
_ExampleSignedRowStatus_Object = MibTableColumn
exampleSignedRowStatus = _ExampleSignedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1, 1, 1),
    _ExampleSignedRowStatus_Type()
)
exampleSignedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedRowStatus.setStatus("mandatory")
_ExampleSignedComponentName_Type = DisplayString
_ExampleSignedComponentName_Object = MibTableColumn
exampleSignedComponentName = _ExampleSignedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1, 1, 2),
    _ExampleSignedComponentName_Type()
)
exampleSignedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleSignedComponentName.setStatus("mandatory")
_ExampleSignedStorageType_Type = StorageType
_ExampleSignedStorageType_Object = MibTableColumn
exampleSignedStorageType = _ExampleSignedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1, 1, 4),
    _ExampleSignedStorageType_Type()
)
exampleSignedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleSignedStorageType.setStatus("mandatory")
_ExampleSignedIndex_Type = NonReplicated
_ExampleSignedIndex_Object = MibTableColumn
exampleSignedIndex = _ExampleSignedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1, 1, 10),
    _ExampleSignedIndex_Type()
)
exampleSignedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedIndex.setStatus("mandatory")
_ExampleSignedOperationalTable_Object = MibTable
exampleSignedOperationalTable = _ExampleSignedOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 10)
)
if mibBuilder.loadTexts:
    exampleSignedOperationalTable.setStatus("mandatory")
_ExampleSignedOperationalEntry_Object = MibTableRow
exampleSignedOperationalEntry = _ExampleSignedOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 10, 1)
)
exampleSignedOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedOperationalEntry.setStatus("mandatory")


class _ExampleSignedOperStructSigned_Type(Integer32):
    """Custom type exampleSignedOperStructSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_ExampleSignedOperStructSigned_Type.__name__ = "Integer32"
_ExampleSignedOperStructSigned_Object = MibTableColumn
exampleSignedOperStructSigned = _ExampleSignedOperStructSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 10, 1, 1),
    _ExampleSignedOperStructSigned_Type()
)
exampleSignedOperStructSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperStructSigned.setStatus("mandatory")


class _ExampleSignedOperFreeSigned_Type(Integer32):
    """Custom type exampleSignedOperFreeSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_ExampleSignedOperFreeSigned_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSigned_Object = MibTableColumn
exampleSignedOperFreeSigned = _ExampleSignedOperFreeSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 10, 1, 2),
    _ExampleSignedOperFreeSigned_Type()
)
exampleSignedOperFreeSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSigned.setStatus("mandatory")
_ExampleSignedProvisionalTable_Object = MibTable
exampleSignedProvisionalTable = _ExampleSignedProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 11)
)
if mibBuilder.loadTexts:
    exampleSignedProvisionalTable.setStatus("mandatory")
_ExampleSignedProvisionalEntry_Object = MibTableRow
exampleSignedProvisionalEntry = _ExampleSignedProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 11, 1)
)
exampleSignedProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvisionalEntry.setStatus("mandatory")
_ExampleSignedProvSignedSub_Type = Link
_ExampleSignedProvSignedSub_Object = MibTableColumn
exampleSignedProvSignedSub = _ExampleSignedProvSignedSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 11, 1, 1),
    _ExampleSignedProvSignedSub_Type()
)
exampleSignedProvSignedSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvSignedSub.setStatus("mandatory")


class _ExampleSignedProvStructSigned_Type(Integer32):
    """Custom type exampleSignedProvStructSigned based on Integer32"""
    defaultValue = -17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-17, -17),
        ValueRangeConstraint(-16, 16),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(18, 18),
    )


_ExampleSignedProvStructSigned_Type.__name__ = "Integer32"
_ExampleSignedProvStructSigned_Object = MibTableColumn
exampleSignedProvStructSigned = _ExampleSignedProvStructSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 11, 1, 2),
    _ExampleSignedProvStructSigned_Type()
)
exampleSignedProvStructSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvStructSigned.setStatus("mandatory")


class _ExampleSignedProvFreeSigned_Type(Integer32):
    """Custom type exampleSignedProvFreeSigned based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_ExampleSignedProvFreeSigned_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSigned_Object = MibTableColumn
exampleSignedProvFreeSigned = _ExampleSignedProvFreeSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 11, 1, 3),
    _ExampleSignedProvFreeSigned_Type()
)
exampleSignedProvFreeSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSigned.setStatus("mandatory")


class _ExampleSignedProvFreeSigned1_Type(Integer32):
    """Custom type exampleSignedProvFreeSigned1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_ExampleSignedProvFreeSigned1_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSigned1_Object = MibTableColumn
exampleSignedProvFreeSigned1 = _ExampleSignedProvFreeSigned1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 11, 1, 4),
    _ExampleSignedProvFreeSigned1_Type()
)
exampleSignedProvFreeSigned1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSigned1.setStatus("mandatory")
_ExampleSignedOperStructSignedVectorTable_Object = MibTable
exampleSignedOperStructSignedVectorTable = _ExampleSignedOperStructSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1148)
)
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedVectorTable.setStatus("mandatory")
_ExampleSignedOperStructSignedVectorEntry_Object = MibTableRow
exampleSignedOperStructSignedVectorEntry = _ExampleSignedOperStructSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1148, 1)
)
exampleSignedOperStructSignedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperStructSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedVectorEntry.setStatus("mandatory")


class _ExampleSignedOperStructSignedVectorIndex_Type(Integer32):
    """Custom type exampleSignedOperStructSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleSignedOperStructSignedVectorIndex_Type.__name__ = "Integer32"
_ExampleSignedOperStructSignedVectorIndex_Object = MibTableColumn
exampleSignedOperStructSignedVectorIndex = _ExampleSignedOperStructSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1148, 1, 1),
    _ExampleSignedOperStructSignedVectorIndex_Type()
)
exampleSignedOperStructSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedVectorIndex.setStatus("mandatory")


class _ExampleSignedOperStructSignedVectorValue_Type(Integer32):
    """Custom type exampleSignedOperStructSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedOperStructSignedVectorValue_Type.__name__ = "Integer32"
_ExampleSignedOperStructSignedVectorValue_Object = MibTableColumn
exampleSignedOperStructSignedVectorValue = _ExampleSignedOperStructSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1148, 1, 2),
    _ExampleSignedOperStructSignedVectorValue_Type()
)
exampleSignedOperStructSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedVectorValue.setStatus("mandatory")
_ExampleSignedOperStructSignedArrayTable_Object = MibTable
exampleSignedOperStructSignedArrayTable = _ExampleSignedOperStructSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1149)
)
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedArrayTable.setStatus("mandatory")
_ExampleSignedOperStructSignedArrayEntry_Object = MibTableRow
exampleSignedOperStructSignedArrayEntry = _ExampleSignedOperStructSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1149, 1)
)
exampleSignedOperStructSignedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperStructSignedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperStructSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedArrayEntry.setStatus("mandatory")


class _ExampleSignedOperStructSignedArrayRowIndex_Type(Integer32):
    """Custom type exampleSignedOperStructSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleSignedOperStructSignedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleSignedOperStructSignedArrayRowIndex_Object = MibTableColumn
exampleSignedOperStructSignedArrayRowIndex = _ExampleSignedOperStructSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1149, 1, 1),
    _ExampleSignedOperStructSignedArrayRowIndex_Type()
)
exampleSignedOperStructSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedArrayRowIndex.setStatus("mandatory")


class _ExampleSignedOperStructSignedArrayColumnIndex_Type(Integer32):
    """Custom type exampleSignedOperStructSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleSignedOperStructSignedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleSignedOperStructSignedArrayColumnIndex_Object = MibTableColumn
exampleSignedOperStructSignedArrayColumnIndex = _ExampleSignedOperStructSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1149, 1, 2),
    _ExampleSignedOperStructSignedArrayColumnIndex_Type()
)
exampleSignedOperStructSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedArrayColumnIndex.setStatus("mandatory")


class _ExampleSignedOperStructSignedArrayValue_Type(Integer32):
    """Custom type exampleSignedOperStructSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedOperStructSignedArrayValue_Type.__name__ = "Integer32"
_ExampleSignedOperStructSignedArrayValue_Object = MibTableColumn
exampleSignedOperStructSignedArrayValue = _ExampleSignedOperStructSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1149, 1, 3),
    _ExampleSignedOperStructSignedArrayValue_Type()
)
exampleSignedOperStructSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperStructSignedArrayValue.setStatus("mandatory")
_ExampleSignedOperFreeSignedVectorTable_Object = MibTable
exampleSignedOperFreeSignedVectorTable = _ExampleSignedOperFreeSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1150)
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedVectorTable.setStatus("mandatory")
_ExampleSignedOperFreeSignedVectorEntry_Object = MibTableRow
exampleSignedOperFreeSignedVectorEntry = _ExampleSignedOperFreeSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1150, 1)
)
exampleSignedOperFreeSignedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperFreeSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedVectorEntry.setStatus("mandatory")


class _ExampleSignedOperFreeSignedVectorIndex_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleSignedOperFreeSignedVectorIndex_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedVectorIndex_Object = MibTableColumn
exampleSignedOperFreeSignedVectorIndex = _ExampleSignedOperFreeSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1150, 1, 1),
    _ExampleSignedOperFreeSignedVectorIndex_Type()
)
exampleSignedOperFreeSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedVectorIndex.setStatus("mandatory")


class _ExampleSignedOperFreeSignedVectorValue_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedOperFreeSignedVectorValue_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedVectorValue_Object = MibTableColumn
exampleSignedOperFreeSignedVectorValue = _ExampleSignedOperFreeSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1150, 1, 2),
    _ExampleSignedOperFreeSignedVectorValue_Type()
)
exampleSignedOperFreeSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedVectorValue.setStatus("mandatory")
_ExampleSignedOperFreeSignedArrayTable_Object = MibTable
exampleSignedOperFreeSignedArrayTable = _ExampleSignedOperFreeSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1151)
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedArrayTable.setStatus("mandatory")
_ExampleSignedOperFreeSignedArrayEntry_Object = MibTableRow
exampleSignedOperFreeSignedArrayEntry = _ExampleSignedOperFreeSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1151, 1)
)
exampleSignedOperFreeSignedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperFreeSignedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperFreeSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedArrayEntry.setStatus("mandatory")


class _ExampleSignedOperFreeSignedArrayRowIndex_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleSignedOperFreeSignedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedArrayRowIndex_Object = MibTableColumn
exampleSignedOperFreeSignedArrayRowIndex = _ExampleSignedOperFreeSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1151, 1, 1),
    _ExampleSignedOperFreeSignedArrayRowIndex_Type()
)
exampleSignedOperFreeSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedArrayRowIndex.setStatus("mandatory")


class _ExampleSignedOperFreeSignedArrayColumnIndex_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleSignedOperFreeSignedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedArrayColumnIndex_Object = MibTableColumn
exampleSignedOperFreeSignedArrayColumnIndex = _ExampleSignedOperFreeSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1151, 1, 2),
    _ExampleSignedOperFreeSignedArrayColumnIndex_Type()
)
exampleSignedOperFreeSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedArrayColumnIndex.setStatus("mandatory")


class _ExampleSignedOperFreeSignedArrayValue_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedOperFreeSignedArrayValue_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedArrayValue_Object = MibTableColumn
exampleSignedOperFreeSignedArrayValue = _ExampleSignedOperFreeSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1151, 1, 3),
    _ExampleSignedOperFreeSignedArrayValue_Type()
)
exampleSignedOperFreeSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedArrayValue.setStatus("mandatory")
_ExampleSignedOperFreeSignedReplicatedTable_Object = MibTable
exampleSignedOperFreeSignedReplicatedTable = _ExampleSignedOperFreeSignedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1152)
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedReplicatedTable.setStatus("mandatory")
_ExampleSignedOperFreeSignedReplicatedEntry_Object = MibTableRow
exampleSignedOperFreeSignedReplicatedEntry = _ExampleSignedOperFreeSignedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1152, 1)
)
exampleSignedOperFreeSignedReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperFreeSignedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedReplicatedEntry.setStatus("mandatory")


class _ExampleSignedOperFreeSignedReplicatedIndex_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedOperFreeSignedReplicatedIndex_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedReplicatedIndex_Object = MibTableColumn
exampleSignedOperFreeSignedReplicatedIndex = _ExampleSignedOperFreeSignedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1152, 1, 1),
    _ExampleSignedOperFreeSignedReplicatedIndex_Type()
)
exampleSignedOperFreeSignedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedReplicatedIndex.setStatus("mandatory")


class _ExampleSignedOperFreeSignedReplicatedValue_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedReplicatedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_ExampleSignedOperFreeSignedReplicatedValue_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedReplicatedValue_Object = MibTableColumn
exampleSignedOperFreeSignedReplicatedValue = _ExampleSignedOperFreeSignedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1152, 1, 2),
    _ExampleSignedOperFreeSignedReplicatedValue_Type()
)
exampleSignedOperFreeSignedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedReplicatedValue.setStatus("mandatory")
_ExampleSignedOperFreeSignedReplicatedRowStatus_Type = RowStatus
_ExampleSignedOperFreeSignedReplicatedRowStatus_Object = MibTableColumn
exampleSignedOperFreeSignedReplicatedRowStatus = _ExampleSignedOperFreeSignedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1152, 1, 3),
    _ExampleSignedOperFreeSignedReplicatedRowStatus_Type()
)
exampleSignedOperFreeSignedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedReplicatedRowStatus.setStatus("mandatory")
_ExampleSignedOperFreeSignedListTable_Object = MibTable
exampleSignedOperFreeSignedListTable = _ExampleSignedOperFreeSignedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1153)
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedListTable.setStatus("mandatory")
_ExampleSignedOperFreeSignedListEntry_Object = MibTableRow
exampleSignedOperFreeSignedListEntry = _ExampleSignedOperFreeSignedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1153, 1)
)
exampleSignedOperFreeSignedListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedOperFreeSignedListValue"),
)
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedListEntry.setStatus("mandatory")


class _ExampleSignedOperFreeSignedListValue_Type(Integer32):
    """Custom type exampleSignedOperFreeSignedListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_ExampleSignedOperFreeSignedListValue_Type.__name__ = "Integer32"
_ExampleSignedOperFreeSignedListValue_Object = MibTableColumn
exampleSignedOperFreeSignedListValue = _ExampleSignedOperFreeSignedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1153, 1, 1),
    _ExampleSignedOperFreeSignedListValue_Type()
)
exampleSignedOperFreeSignedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedListValue.setStatus("mandatory")
_ExampleSignedOperFreeSignedListRowStatus_Type = RowStatus
_ExampleSignedOperFreeSignedListRowStatus_Object = MibTableColumn
exampleSignedOperFreeSignedListRowStatus = _ExampleSignedOperFreeSignedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1153, 1, 2),
    _ExampleSignedOperFreeSignedListRowStatus_Type()
)
exampleSignedOperFreeSignedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSignedOperFreeSignedListRowStatus.setStatus("mandatory")
_ExampleSignedProvStructSignedVectorTable_Object = MibTable
exampleSignedProvStructSignedVectorTable = _ExampleSignedProvStructSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1154)
)
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedVectorTable.setStatus("mandatory")
_ExampleSignedProvStructSignedVectorEntry_Object = MibTableRow
exampleSignedProvStructSignedVectorEntry = _ExampleSignedProvStructSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1154, 1)
)
exampleSignedProvStructSignedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvStructSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedVectorEntry.setStatus("mandatory")


class _ExampleSignedProvStructSignedVectorIndex_Type(Integer32):
    """Custom type exampleSignedProvStructSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleSignedProvStructSignedVectorIndex_Type.__name__ = "Integer32"
_ExampleSignedProvStructSignedVectorIndex_Object = MibTableColumn
exampleSignedProvStructSignedVectorIndex = _ExampleSignedProvStructSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1154, 1, 1),
    _ExampleSignedProvStructSignedVectorIndex_Type()
)
exampleSignedProvStructSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedVectorIndex.setStatus("mandatory")


class _ExampleSignedProvStructSignedVectorValue_Type(Integer32):
    """Custom type exampleSignedProvStructSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedProvStructSignedVectorValue_Type.__name__ = "Integer32"
_ExampleSignedProvStructSignedVectorValue_Object = MibTableColumn
exampleSignedProvStructSignedVectorValue = _ExampleSignedProvStructSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1154, 1, 2),
    _ExampleSignedProvStructSignedVectorValue_Type()
)
exampleSignedProvStructSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedVectorValue.setStatus("mandatory")
_ExampleSignedProvStructSignedArrayTable_Object = MibTable
exampleSignedProvStructSignedArrayTable = _ExampleSignedProvStructSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1155)
)
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedArrayTable.setStatus("mandatory")
_ExampleSignedProvStructSignedArrayEntry_Object = MibTableRow
exampleSignedProvStructSignedArrayEntry = _ExampleSignedProvStructSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1155, 1)
)
exampleSignedProvStructSignedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvStructSignedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvStructSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedArrayEntry.setStatus("mandatory")


class _ExampleSignedProvStructSignedArrayRowIndex_Type(Integer32):
    """Custom type exampleSignedProvStructSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleSignedProvStructSignedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleSignedProvStructSignedArrayRowIndex_Object = MibTableColumn
exampleSignedProvStructSignedArrayRowIndex = _ExampleSignedProvStructSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1155, 1, 1),
    _ExampleSignedProvStructSignedArrayRowIndex_Type()
)
exampleSignedProvStructSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedArrayRowIndex.setStatus("mandatory")


class _ExampleSignedProvStructSignedArrayColumnIndex_Type(Integer32):
    """Custom type exampleSignedProvStructSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleSignedProvStructSignedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleSignedProvStructSignedArrayColumnIndex_Object = MibTableColumn
exampleSignedProvStructSignedArrayColumnIndex = _ExampleSignedProvStructSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1155, 1, 2),
    _ExampleSignedProvStructSignedArrayColumnIndex_Type()
)
exampleSignedProvStructSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedArrayColumnIndex.setStatus("mandatory")


class _ExampleSignedProvStructSignedArrayValue_Type(Integer32):
    """Custom type exampleSignedProvStructSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedProvStructSignedArrayValue_Type.__name__ = "Integer32"
_ExampleSignedProvStructSignedArrayValue_Object = MibTableColumn
exampleSignedProvStructSignedArrayValue = _ExampleSignedProvStructSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1155, 1, 3),
    _ExampleSignedProvStructSignedArrayValue_Type()
)
exampleSignedProvStructSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvStructSignedArrayValue.setStatus("mandatory")
_ExampleSignedProvFreeSignedVectorTable_Object = MibTable
exampleSignedProvFreeSignedVectorTable = _ExampleSignedProvFreeSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1156)
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVectorTable.setStatus("mandatory")
_ExampleSignedProvFreeSignedVectorEntry_Object = MibTableRow
exampleSignedProvFreeSignedVectorEntry = _ExampleSignedProvFreeSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1156, 1)
)
exampleSignedProvFreeSignedVectorEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVectorEntry.setStatus("mandatory")


class _ExampleSignedProvFreeSignedVectorIndex_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleSignedProvFreeSignedVectorIndex_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedVectorIndex_Object = MibTableColumn
exampleSignedProvFreeSignedVectorIndex = _ExampleSignedProvFreeSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1156, 1, 1),
    _ExampleSignedProvFreeSignedVectorIndex_Type()
)
exampleSignedProvFreeSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVectorIndex.setStatus("mandatory")


class _ExampleSignedProvFreeSignedVectorValue_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedProvFreeSignedVectorValue_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedVectorValue_Object = MibTableColumn
exampleSignedProvFreeSignedVectorValue = _ExampleSignedProvFreeSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1156, 1, 2),
    _ExampleSignedProvFreeSignedVectorValue_Type()
)
exampleSignedProvFreeSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVectorValue.setStatus("mandatory")
_ExampleSignedProvFreeSignedVector1Table_Object = MibTable
exampleSignedProvFreeSignedVector1Table = _ExampleSignedProvFreeSignedVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1157)
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVector1Table.setStatus("mandatory")
_ExampleSignedProvFreeSignedVector1Entry_Object = MibTableRow
exampleSignedProvFreeSignedVector1Entry = _ExampleSignedProvFreeSignedVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1157, 1)
)
exampleSignedProvFreeSignedVector1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedVector1Index"),
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVector1Entry.setStatus("mandatory")


class _ExampleSignedProvFreeSignedVector1Index_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleSignedProvFreeSignedVector1Index_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedVector1Index_Object = MibTableColumn
exampleSignedProvFreeSignedVector1Index = _ExampleSignedProvFreeSignedVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1157, 1, 1),
    _ExampleSignedProvFreeSignedVector1Index_Type()
)
exampleSignedProvFreeSignedVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVector1Index.setStatus("mandatory")


class _ExampleSignedProvFreeSignedVector1Value_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedVector1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_ExampleSignedProvFreeSignedVector1Value_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedVector1Value_Object = MibTableColumn
exampleSignedProvFreeSignedVector1Value = _ExampleSignedProvFreeSignedVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1157, 1, 2),
    _ExampleSignedProvFreeSignedVector1Value_Type()
)
exampleSignedProvFreeSignedVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedVector1Value.setStatus("mandatory")
_ExampleSignedProvFreeSignedArrayTable_Object = MibTable
exampleSignedProvFreeSignedArrayTable = _ExampleSignedProvFreeSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1158)
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArrayTable.setStatus("mandatory")
_ExampleSignedProvFreeSignedArrayEntry_Object = MibTableRow
exampleSignedProvFreeSignedArrayEntry = _ExampleSignedProvFreeSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1158, 1)
)
exampleSignedProvFreeSignedArrayEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedArrayRowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArrayEntry.setStatus("mandatory")


class _ExampleSignedProvFreeSignedArrayRowIndex_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleSignedProvFreeSignedArrayRowIndex_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedArrayRowIndex_Object = MibTableColumn
exampleSignedProvFreeSignedArrayRowIndex = _ExampleSignedProvFreeSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1158, 1, 1),
    _ExampleSignedProvFreeSignedArrayRowIndex_Type()
)
exampleSignedProvFreeSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArrayRowIndex.setStatus("mandatory")


class _ExampleSignedProvFreeSignedArrayColumnIndex_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleSignedProvFreeSignedArrayColumnIndex_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedArrayColumnIndex_Object = MibTableColumn
exampleSignedProvFreeSignedArrayColumnIndex = _ExampleSignedProvFreeSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1158, 1, 2),
    _ExampleSignedProvFreeSignedArrayColumnIndex_Type()
)
exampleSignedProvFreeSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArrayColumnIndex.setStatus("mandatory")


class _ExampleSignedProvFreeSignedArrayValue_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 4000),
    )


_ExampleSignedProvFreeSignedArrayValue_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedArrayValue_Object = MibTableColumn
exampleSignedProvFreeSignedArrayValue = _ExampleSignedProvFreeSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1158, 1, 3),
    _ExampleSignedProvFreeSignedArrayValue_Type()
)
exampleSignedProvFreeSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArrayValue.setStatus("mandatory")
_ExampleSignedProvFreeSignedArray1Table_Object = MibTable
exampleSignedProvFreeSignedArray1Table = _ExampleSignedProvFreeSignedArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1159)
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArray1Table.setStatus("mandatory")
_ExampleSignedProvFreeSignedArray1Entry_Object = MibTableRow
exampleSignedProvFreeSignedArray1Entry = _ExampleSignedProvFreeSignedArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1159, 1)
)
exampleSignedProvFreeSignedArray1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedArray1RowIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArray1Entry.setStatus("mandatory")


class _ExampleSignedProvFreeSignedArray1RowIndex_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ExampleSignedProvFreeSignedArray1RowIndex_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedArray1RowIndex_Object = MibTableColumn
exampleSignedProvFreeSignedArray1RowIndex = _ExampleSignedProvFreeSignedArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1159, 1, 1),
    _ExampleSignedProvFreeSignedArray1RowIndex_Type()
)
exampleSignedProvFreeSignedArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArray1RowIndex.setStatus("mandatory")


class _ExampleSignedProvFreeSignedArray1ColumnIndex_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ExampleSignedProvFreeSignedArray1ColumnIndex_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedArray1ColumnIndex_Object = MibTableColumn
exampleSignedProvFreeSignedArray1ColumnIndex = _ExampleSignedProvFreeSignedArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1159, 1, 2),
    _ExampleSignedProvFreeSignedArray1ColumnIndex_Type()
)
exampleSignedProvFreeSignedArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArray1ColumnIndex.setStatus("mandatory")


class _ExampleSignedProvFreeSignedArray1Value_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedArray1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 4000),
    )


_ExampleSignedProvFreeSignedArray1Value_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedArray1Value_Object = MibTableColumn
exampleSignedProvFreeSignedArray1Value = _ExampleSignedProvFreeSignedArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1159, 1, 3),
    _ExampleSignedProvFreeSignedArray1Value_Type()
)
exampleSignedProvFreeSignedArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedArray1Value.setStatus("mandatory")
_ExampleSignedProvFreeSignedReplicatedTable_Object = MibTable
exampleSignedProvFreeSignedReplicatedTable = _ExampleSignedProvFreeSignedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1160)
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedReplicatedTable.setStatus("mandatory")
_ExampleSignedProvFreeSignedReplicatedEntry_Object = MibTableRow
exampleSignedProvFreeSignedReplicatedEntry = _ExampleSignedProvFreeSignedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1160, 1)
)
exampleSignedProvFreeSignedReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedReplicatedEntry.setStatus("mandatory")


class _ExampleSignedProvFreeSignedReplicatedIndex_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ExampleSignedProvFreeSignedReplicatedIndex_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedReplicatedIndex_Object = MibTableColumn
exampleSignedProvFreeSignedReplicatedIndex = _ExampleSignedProvFreeSignedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1160, 1, 1),
    _ExampleSignedProvFreeSignedReplicatedIndex_Type()
)
exampleSignedProvFreeSignedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedReplicatedIndex.setStatus("mandatory")


class _ExampleSignedProvFreeSignedReplicatedValue_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedReplicatedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 13),
    )


_ExampleSignedProvFreeSignedReplicatedValue_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedReplicatedValue_Object = MibTableColumn
exampleSignedProvFreeSignedReplicatedValue = _ExampleSignedProvFreeSignedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1160, 1, 2),
    _ExampleSignedProvFreeSignedReplicatedValue_Type()
)
exampleSignedProvFreeSignedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedReplicatedValue.setStatus("mandatory")
_ExampleSignedProvFreeSignedReplicatedRowStatus_Type = RowStatus
_ExampleSignedProvFreeSignedReplicatedRowStatus_Object = MibTableColumn
exampleSignedProvFreeSignedReplicatedRowStatus = _ExampleSignedProvFreeSignedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1160, 1, 3),
    _ExampleSignedProvFreeSignedReplicatedRowStatus_Type()
)
exampleSignedProvFreeSignedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedReplicatedRowStatus.setStatus("mandatory")
_ExampleSignedProvFreeSignedListTable_Object = MibTable
exampleSignedProvFreeSignedListTable = _ExampleSignedProvFreeSignedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1161)
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedListTable.setStatus("mandatory")
_ExampleSignedProvFreeSignedListEntry_Object = MibTableRow
exampleSignedProvFreeSignedListEntry = _ExampleSignedProvFreeSignedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1161, 1)
)
exampleSignedProvFreeSignedListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSignedProvFreeSignedListValue"),
)
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedListEntry.setStatus("mandatory")


class _ExampleSignedProvFreeSignedListValue_Type(Integer32):
    """Custom type exampleSignedProvFreeSignedListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 160),
    )


_ExampleSignedProvFreeSignedListValue_Type.__name__ = "Integer32"
_ExampleSignedProvFreeSignedListValue_Object = MibTableColumn
exampleSignedProvFreeSignedListValue = _ExampleSignedProvFreeSignedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1161, 1, 1),
    _ExampleSignedProvFreeSignedListValue_Type()
)
exampleSignedProvFreeSignedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedListValue.setStatus("mandatory")
_ExampleSignedProvFreeSignedListRowStatus_Type = RowStatus
_ExampleSignedProvFreeSignedListRowStatus_Object = MibTableColumn
exampleSignedProvFreeSignedListRowStatus = _ExampleSignedProvFreeSignedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 14, 1161, 1, 2),
    _ExampleSignedProvFreeSignedListRowStatus_Type()
)
exampleSignedProvFreeSignedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleSignedProvFreeSignedListRowStatus.setStatus("mandatory")
_ExampleMiscellaneous_ObjectIdentity = ObjectIdentity
exampleMiscellaneous = _ExampleMiscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15)
)
_ExampleMiscellaneousRowStatusTable_Object = MibTable
exampleMiscellaneousRowStatusTable = _ExampleMiscellaneousRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousRowStatusTable.setStatus("mandatory")
_ExampleMiscellaneousRowStatusEntry_Object = MibTableRow
exampleMiscellaneousRowStatusEntry = _ExampleMiscellaneousRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1, 1)
)
exampleMiscellaneousRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousRowStatusEntry.setStatus("mandatory")
_ExampleMiscellaneousRowStatus_Type = RowStatus
_ExampleMiscellaneousRowStatus_Object = MibTableColumn
exampleMiscellaneousRowStatus = _ExampleMiscellaneousRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1, 1, 1),
    _ExampleMiscellaneousRowStatus_Type()
)
exampleMiscellaneousRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousRowStatus.setStatus("mandatory")
_ExampleMiscellaneousComponentName_Type = DisplayString
_ExampleMiscellaneousComponentName_Object = MibTableColumn
exampleMiscellaneousComponentName = _ExampleMiscellaneousComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1, 1, 2),
    _ExampleMiscellaneousComponentName_Type()
)
exampleMiscellaneousComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousComponentName.setStatus("mandatory")
_ExampleMiscellaneousStorageType_Type = StorageType
_ExampleMiscellaneousStorageType_Object = MibTableColumn
exampleMiscellaneousStorageType = _ExampleMiscellaneousStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1, 1, 4),
    _ExampleMiscellaneousStorageType_Type()
)
exampleMiscellaneousStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousStorageType.setStatus("mandatory")
_ExampleMiscellaneousIndex_Type = NonReplicated
_ExampleMiscellaneousIndex_Object = MibTableColumn
exampleMiscellaneousIndex = _ExampleMiscellaneousIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1, 1, 10),
    _ExampleMiscellaneousIndex_Type()
)
exampleMiscellaneousIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleMiscellaneousIndex.setStatus("mandatory")
_ExampleMiscellaneousOperationalTable_Object = MibTable
exampleMiscellaneousOperationalTable = _ExampleMiscellaneousOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperationalTable.setStatus("mandatory")
_ExampleMiscellaneousOperationalEntry_Object = MibTableRow
exampleMiscellaneousOperationalEntry = _ExampleMiscellaneousOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1)
)
exampleMiscellaneousOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperationalEntry.setStatus("mandatory")


class _ExampleMiscellaneousOperStructLong_Type(Unsigned64):
    """Custom type exampleMiscellaneousOperStructLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousOperStructLong_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousOperStructLong_Object = MibTableColumn
exampleMiscellaneousOperStructLong = _ExampleMiscellaneousOperStructLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 1),
    _ExampleMiscellaneousOperStructLong_Type()
)
exampleMiscellaneousOperStructLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperStructLong.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeLong_Type(Unsigned64):
    """Custom type exampleMiscellaneousOperFreeLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousOperFreeLong_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousOperFreeLong_Object = MibTableColumn
exampleMiscellaneousOperFreeLong = _ExampleMiscellaneousOperFreeLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 2),
    _ExampleMiscellaneousOperFreeLong_Type()
)
exampleMiscellaneousOperFreeLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLong.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeTime_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousOperFreeTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_ExampleMiscellaneousOperFreeTime_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousOperFreeTime_Object = MibTableColumn
exampleMiscellaneousOperFreeTime = _ExampleMiscellaneousOperFreeTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 3),
    _ExampleMiscellaneousOperFreeTime_Type()
)
exampleMiscellaneousOperFreeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTime.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeTimeDateOnly_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousOperFreeTimeDateOnly based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_ExampleMiscellaneousOperFreeTimeDateOnly_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousOperFreeTimeDateOnly_Object = MibTableColumn
exampleMiscellaneousOperFreeTimeDateOnly = _ExampleMiscellaneousOperFreeTimeDateOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 4),
    _ExampleMiscellaneousOperFreeTimeDateOnly_Type()
)
exampleMiscellaneousOperFreeTimeDateOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeDateOnly.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeTimeTimeOnly_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousOperFreeTimeTimeOnly based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_ExampleMiscellaneousOperFreeTimeTimeOnly_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousOperFreeTimeTimeOnly_Object = MibTableColumn
exampleMiscellaneousOperFreeTimeTimeOnly = _ExampleMiscellaneousOperFreeTimeTimeOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 5),
    _ExampleMiscellaneousOperFreeTimeTimeOnly_Type()
)
exampleMiscellaneousOperFreeTimeTimeOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeTimeOnly.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeTimeDateTimeMinute_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousOperFreeTimeDateTimeMinute based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_ExampleMiscellaneousOperFreeTimeDateTimeMinute_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousOperFreeTimeDateTimeMinute_Object = MibTableColumn
exampleMiscellaneousOperFreeTimeDateTimeMinute = _ExampleMiscellaneousOperFreeTimeDateTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 6),
    _ExampleMiscellaneousOperFreeTimeDateTimeMinute_Type()
)
exampleMiscellaneousOperFreeTimeDateTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeDateTimeMinute.setStatus("mandatory")
_ExampleMiscellaneousOperFreeCounter64_Type = PassportCounter64
_ExampleMiscellaneousOperFreeCounter64_Object = MibTableColumn
exampleMiscellaneousOperFreeCounter64 = _ExampleMiscellaneousOperFreeCounter64_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 7),
    _ExampleMiscellaneousOperFreeCounter64_Type()
)
exampleMiscellaneousOperFreeCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeCounter64.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeGauge64_Type(Gauge64):
    """Custom type exampleMiscellaneousOperFreeGauge64 based on Gauge64"""
    subtypeSpec = Gauge64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousOperFreeGauge64_Type.__name__ = "Gauge64"
_ExampleMiscellaneousOperFreeGauge64_Object = MibTableColumn
exampleMiscellaneousOperFreeGauge64 = _ExampleMiscellaneousOperFreeGauge64_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 8),
    _ExampleMiscellaneousOperFreeGauge64_Type()
)
exampleMiscellaneousOperFreeGauge64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeGauge64.setStatus("mandatory")
_ExampleMiscellaneousOperStructCounter64_Type = PassportCounter64
_ExampleMiscellaneousOperStructCounter64_Object = MibTableColumn
exampleMiscellaneousOperStructCounter64 = _ExampleMiscellaneousOperStructCounter64_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 10, 1, 9),
    _ExampleMiscellaneousOperStructCounter64_Type()
)
exampleMiscellaneousOperStructCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperStructCounter64.setStatus("mandatory")
_ExampleMiscellaneousProvisionalTable_Object = MibTable
exampleMiscellaneousProvisionalTable = _ExampleMiscellaneousProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvisionalTable.setStatus("mandatory")
_ExampleMiscellaneousProvisionalEntry_Object = MibTableRow
exampleMiscellaneousProvisionalEntry = _ExampleMiscellaneousProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1)
)
exampleMiscellaneousProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvisionalEntry.setStatus("mandatory")
_ExampleMiscellaneousProvEnumSub_Type = Link
_ExampleMiscellaneousProvEnumSub_Object = MibTableColumn
exampleMiscellaneousProvEnumSub = _ExampleMiscellaneousProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 1),
    _ExampleMiscellaneousProvEnumSub_Type()
)
exampleMiscellaneousProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvEnumSub.setStatus("mandatory")


class _ExampleMiscellaneousProvStructLong_Type(Unsigned64):
    """Custom type exampleMiscellaneousProvStructLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvStructLong_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousProvStructLong_Object = MibTableColumn
exampleMiscellaneousProvStructLong = _ExampleMiscellaneousProvStructLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 2),
    _ExampleMiscellaneousProvStructLong_Type()
)
exampleMiscellaneousProvStructLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvStructLong.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeLong_Type(Unsigned64):
    """Custom type exampleMiscellaneousProvFreeLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvFreeLong_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousProvFreeLong_Object = MibTableColumn
exampleMiscellaneousProvFreeLong = _ExampleMiscellaneousProvFreeLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 3),
    _ExampleMiscellaneousProvFreeLong_Type()
)
exampleMiscellaneousProvFreeLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLong.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTime_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTime based on EnterpriseDateAndTime"""
    defaultHexValue = "313939322d31302d31352031303a33393a3030"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_ExampleMiscellaneousProvFreeTime_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTime_Object = MibTableColumn
exampleMiscellaneousProvFreeTime = _ExampleMiscellaneousProvFreeTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 4),
    _ExampleMiscellaneousProvFreeTime_Type()
)
exampleMiscellaneousProvFreeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTime.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeDateOnly_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeDateOnly based on EnterpriseDateAndTime"""
    defaultHexValue = "313939322d31302d3135"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_ExampleMiscellaneousProvFreeTimeDateOnly_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeDateOnly_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeDateOnly = _ExampleMiscellaneousProvFreeTimeDateOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 5),
    _ExampleMiscellaneousProvFreeTimeDateOnly_Type()
)
exampleMiscellaneousProvFreeTimeDateOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeDateOnly.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeTimeOnly_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeTimeOnly based on EnterpriseDateAndTime"""
    defaultHexValue = "31303a3339"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_ExampleMiscellaneousProvFreeTimeTimeOnly_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeTimeOnly_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeTimeOnly = _ExampleMiscellaneousProvFreeTimeTimeOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 6),
    _ExampleMiscellaneousProvFreeTimeTimeOnly_Type()
)
exampleMiscellaneousProvFreeTimeTimeOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeTimeOnly.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeDateTimeMinute_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeDateTimeMinute based on EnterpriseDateAndTime"""
    defaultHexValue = "313939322d31302d31352031303a3330"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_ExampleMiscellaneousProvFreeTimeDateTimeMinute_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeDateTimeMinute_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeDateTimeMinute = _ExampleMiscellaneousProvFreeTimeDateTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 7),
    _ExampleMiscellaneousProvFreeTimeDateTimeMinute_Type()
)
exampleMiscellaneousProvFreeTimeDateTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeDateTimeMinute.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTime1_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTime1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_ExampleMiscellaneousProvFreeTime1_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTime1_Object = MibTableColumn
exampleMiscellaneousProvFreeTime1 = _ExampleMiscellaneousProvFreeTime1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 8),
    _ExampleMiscellaneousProvFreeTime1_Type()
)
exampleMiscellaneousProvFreeTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTime1.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeDateOnly1_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeDateOnly1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_ExampleMiscellaneousProvFreeTimeDateOnly1_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeDateOnly1_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeDateOnly1 = _ExampleMiscellaneousProvFreeTimeDateOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 9),
    _ExampleMiscellaneousProvFreeTimeDateOnly1_Type()
)
exampleMiscellaneousProvFreeTimeDateOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeDateOnly1.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeTimeOnly1_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeTimeOnly1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvFreeTimeTimeOnly1_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeTimeOnly1_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeTimeOnly1 = _ExampleMiscellaneousProvFreeTimeTimeOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 10),
    _ExampleMiscellaneousProvFreeTimeTimeOnly1_Type()
)
exampleMiscellaneousProvFreeTimeTimeOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeTimeOnly1.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeDateTimeMinute1_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeDateTimeMinute1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_ExampleMiscellaneousProvFreeTimeDateTimeMinute1_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeDateTimeMinute1_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeDateTimeMinute1 = _ExampleMiscellaneousProvFreeTimeDateTimeMinute1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 11, 1, 11),
    _ExampleMiscellaneousProvFreeTimeDateTimeMinute1_Type()
)
exampleMiscellaneousProvFreeTimeDateTimeMinute1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeDateTimeMinute1.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongReplicatedTable_Object = MibTable
exampleMiscellaneousOperFreeLongReplicatedTable = _ExampleMiscellaneousOperFreeLongReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1177)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongReplicatedTable.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongReplicatedEntry_Object = MibTableRow
exampleMiscellaneousOperFreeLongReplicatedEntry = _ExampleMiscellaneousOperFreeLongReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1177, 1)
)
exampleMiscellaneousOperFreeLongReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousOperFreeLongReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongReplicatedEntry.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongReplicatedIndex_Type = Unsigned64
_ExampleMiscellaneousOperFreeLongReplicatedIndex_Object = MibTableColumn
exampleMiscellaneousOperFreeLongReplicatedIndex = _ExampleMiscellaneousOperFreeLongReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1177, 1, 1),
    _ExampleMiscellaneousOperFreeLongReplicatedIndex_Type()
)
exampleMiscellaneousOperFreeLongReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongReplicatedIndex.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeLongReplicatedValue_Type(Unsigned64):
    """Custom type exampleMiscellaneousOperFreeLongReplicatedValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousOperFreeLongReplicatedValue_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousOperFreeLongReplicatedValue_Object = MibTableColumn
exampleMiscellaneousOperFreeLongReplicatedValue = _ExampleMiscellaneousOperFreeLongReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1177, 1, 2),
    _ExampleMiscellaneousOperFreeLongReplicatedValue_Type()
)
exampleMiscellaneousOperFreeLongReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongReplicatedValue.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongReplicatedRowStatus_Type = RowStatus
_ExampleMiscellaneousOperFreeLongReplicatedRowStatus_Object = MibTableColumn
exampleMiscellaneousOperFreeLongReplicatedRowStatus = _ExampleMiscellaneousOperFreeLongReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1177, 1, 3),
    _ExampleMiscellaneousOperFreeLongReplicatedRowStatus_Type()
)
exampleMiscellaneousOperFreeLongReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongReplicatedRowStatus.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongListTable_Object = MibTable
exampleMiscellaneousOperFreeLongListTable = _ExampleMiscellaneousOperFreeLongListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1178)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongListTable.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongListEntry_Object = MibTableRow
exampleMiscellaneousOperFreeLongListEntry = _ExampleMiscellaneousOperFreeLongListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1178, 1)
)
exampleMiscellaneousOperFreeLongListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousOperFreeLongListValue"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongListEntry.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeLongListValue_Type(Unsigned64):
    """Custom type exampleMiscellaneousOperFreeLongListValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousOperFreeLongListValue_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousOperFreeLongListValue_Object = MibTableColumn
exampleMiscellaneousOperFreeLongListValue = _ExampleMiscellaneousOperFreeLongListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1178, 1, 1),
    _ExampleMiscellaneousOperFreeLongListValue_Type()
)
exampleMiscellaneousOperFreeLongListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongListValue.setStatus("mandatory")
_ExampleMiscellaneousOperFreeLongListRowStatus_Type = RowStatus
_ExampleMiscellaneousOperFreeLongListRowStatus_Object = MibTableColumn
exampleMiscellaneousOperFreeLongListRowStatus = _ExampleMiscellaneousOperFreeLongListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1178, 1, 2),
    _ExampleMiscellaneousOperFreeLongListRowStatus_Type()
)
exampleMiscellaneousOperFreeLongListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeLongListRowStatus.setStatus("mandatory")
_ExampleMiscellaneousOperFreeTimeListTable_Object = MibTable
exampleMiscellaneousOperFreeTimeListTable = _ExampleMiscellaneousOperFreeTimeListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1179)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeListTable.setStatus("mandatory")
_ExampleMiscellaneousOperFreeTimeListEntry_Object = MibTableRow
exampleMiscellaneousOperFreeTimeListEntry = _ExampleMiscellaneousOperFreeTimeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1179, 1)
)
exampleMiscellaneousOperFreeTimeListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousOperFreeTimeListValue"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeListEntry.setStatus("mandatory")


class _ExampleMiscellaneousOperFreeTimeListValue_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousOperFreeTimeListValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ExampleMiscellaneousOperFreeTimeListValue_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousOperFreeTimeListValue_Object = MibTableColumn
exampleMiscellaneousOperFreeTimeListValue = _ExampleMiscellaneousOperFreeTimeListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1179, 1, 1),
    _ExampleMiscellaneousOperFreeTimeListValue_Type()
)
exampleMiscellaneousOperFreeTimeListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeListValue.setStatus("mandatory")
_ExampleMiscellaneousOperFreeTimeListRowStatus_Type = RowStatus
_ExampleMiscellaneousOperFreeTimeListRowStatus_Object = MibTableColumn
exampleMiscellaneousOperFreeTimeListRowStatus = _ExampleMiscellaneousOperFreeTimeListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1179, 1, 2),
    _ExampleMiscellaneousOperFreeTimeListRowStatus_Type()
)
exampleMiscellaneousOperFreeTimeListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousOperFreeTimeListRowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongReplicatedTable_Object = MibTable
exampleMiscellaneousProvFreeLongReplicatedTable = _ExampleMiscellaneousProvFreeLongReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1180)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongReplicatedTable.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongReplicatedEntry_Object = MibTableRow
exampleMiscellaneousProvFreeLongReplicatedEntry = _ExampleMiscellaneousProvFreeLongReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1180, 1)
)
exampleMiscellaneousProvFreeLongReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeLongReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongReplicatedEntry.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongReplicatedIndex_Type = Unsigned64
_ExampleMiscellaneousProvFreeLongReplicatedIndex_Object = MibTableColumn
exampleMiscellaneousProvFreeLongReplicatedIndex = _ExampleMiscellaneousProvFreeLongReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1180, 1, 1),
    _ExampleMiscellaneousProvFreeLongReplicatedIndex_Type()
)
exampleMiscellaneousProvFreeLongReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongReplicatedIndex.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeLongReplicatedValue_Type(Unsigned64):
    """Custom type exampleMiscellaneousProvFreeLongReplicatedValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvFreeLongReplicatedValue_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousProvFreeLongReplicatedValue_Object = MibTableColumn
exampleMiscellaneousProvFreeLongReplicatedValue = _ExampleMiscellaneousProvFreeLongReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1180, 1, 2),
    _ExampleMiscellaneousProvFreeLongReplicatedValue_Type()
)
exampleMiscellaneousProvFreeLongReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongReplicatedValue.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongReplicatedRowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeLongReplicatedRowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeLongReplicatedRowStatus = _ExampleMiscellaneousProvFreeLongReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1180, 1, 3),
    _ExampleMiscellaneousProvFreeLongReplicatedRowStatus_Type()
)
exampleMiscellaneousProvFreeLongReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongReplicatedRowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongListTable_Object = MibTable
exampleMiscellaneousProvFreeLongListTable = _ExampleMiscellaneousProvFreeLongListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1181)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongListTable.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongListEntry_Object = MibTableRow
exampleMiscellaneousProvFreeLongListEntry = _ExampleMiscellaneousProvFreeLongListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1181, 1)
)
exampleMiscellaneousProvFreeLongListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeLongListValue"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongListEntry.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeLongListValue_Type(Unsigned64):
    """Custom type exampleMiscellaneousProvFreeLongListValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvFreeLongListValue_Type.__name__ = "Unsigned64"
_ExampleMiscellaneousProvFreeLongListValue_Object = MibTableColumn
exampleMiscellaneousProvFreeLongListValue = _ExampleMiscellaneousProvFreeLongListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1181, 1, 1),
    _ExampleMiscellaneousProvFreeLongListValue_Type()
)
exampleMiscellaneousProvFreeLongListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongListValue.setStatus("mandatory")
_ExampleMiscellaneousProvFreeLongListRowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeLongListRowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeLongListRowStatus = _ExampleMiscellaneousProvFreeLongListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1181, 1, 2),
    _ExampleMiscellaneousProvFreeLongListRowStatus_Type()
)
exampleMiscellaneousProvFreeLongListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeLongListRowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeReplicatedTable_Object = MibTable
exampleMiscellaneousProvFreeTimeReplicatedTable = _ExampleMiscellaneousProvFreeTimeReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1182)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeReplicatedTable.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeReplicatedEntry_Object = MibTableRow
exampleMiscellaneousProvFreeTimeReplicatedEntry = _ExampleMiscellaneousProvFreeTimeReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1182, 1)
)
exampleMiscellaneousProvFreeTimeReplicatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeTimeReplicatedIndex"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeReplicatedEntry.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeReplicatedIndex_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeReplicatedIndex based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_ExampleMiscellaneousProvFreeTimeReplicatedIndex_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeReplicatedIndex_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeReplicatedIndex = _ExampleMiscellaneousProvFreeTimeReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1182, 1, 1),
    _ExampleMiscellaneousProvFreeTimeReplicatedIndex_Type()
)
exampleMiscellaneousProvFreeTimeReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeReplicatedIndex.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeReplicatedValue_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeReplicatedValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvFreeTimeReplicatedValue_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeReplicatedValue_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeReplicatedValue = _ExampleMiscellaneousProvFreeTimeReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1182, 1, 2),
    _ExampleMiscellaneousProvFreeTimeReplicatedValue_Type()
)
exampleMiscellaneousProvFreeTimeReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeReplicatedValue.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeReplicatedRowStatus = _ExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1182, 1, 3),
    _ExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Type()
)
exampleMiscellaneousProvFreeTimeReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeReplicatedRowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeListTable_Object = MibTable
exampleMiscellaneousProvFreeTimeListTable = _ExampleMiscellaneousProvFreeTimeListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1183)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeListTable.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeListEntry_Object = MibTableRow
exampleMiscellaneousProvFreeTimeListEntry = _ExampleMiscellaneousProvFreeTimeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1183, 1)
)
exampleMiscellaneousProvFreeTimeListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeTimeListValue"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeListEntry.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeListValue_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeListValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_ExampleMiscellaneousProvFreeTimeListValue_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeListValue_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeListValue = _ExampleMiscellaneousProvFreeTimeListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1183, 1, 1),
    _ExampleMiscellaneousProvFreeTimeListValue_Type()
)
exampleMiscellaneousProvFreeTimeListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeListValue.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeListRowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeTimeListRowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeListRowStatus = _ExampleMiscellaneousProvFreeTimeListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1183, 1, 2),
    _ExampleMiscellaneousProvFreeTimeListRowStatus_Type()
)
exampleMiscellaneousProvFreeTimeListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeListRowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList1Table_Object = MibTable
exampleMiscellaneousProvFreeTimeList1Table = _ExampleMiscellaneousProvFreeTimeList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1184)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList1Table.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList1Entry_Object = MibTableRow
exampleMiscellaneousProvFreeTimeList1Entry = _ExampleMiscellaneousProvFreeTimeList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1184, 1)
)
exampleMiscellaneousProvFreeTimeList1Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeTimeList1Value"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList1Entry.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeList1Value_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeList1Value based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_ExampleMiscellaneousProvFreeTimeList1Value_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeList1Value_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeList1Value = _ExampleMiscellaneousProvFreeTimeList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1184, 1, 1),
    _ExampleMiscellaneousProvFreeTimeList1Value_Type()
)
exampleMiscellaneousProvFreeTimeList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList1Value.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList1RowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeTimeList1RowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeList1RowStatus = _ExampleMiscellaneousProvFreeTimeList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1184, 1, 2),
    _ExampleMiscellaneousProvFreeTimeList1RowStatus_Type()
)
exampleMiscellaneousProvFreeTimeList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList1RowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList2Table_Object = MibTable
exampleMiscellaneousProvFreeTimeList2Table = _ExampleMiscellaneousProvFreeTimeList2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1185)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList2Table.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList2Entry_Object = MibTableRow
exampleMiscellaneousProvFreeTimeList2Entry = _ExampleMiscellaneousProvFreeTimeList2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1185, 1)
)
exampleMiscellaneousProvFreeTimeList2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeTimeList2Value"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList2Entry.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeList2Value_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeList2Value based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExampleMiscellaneousProvFreeTimeList2Value_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeList2Value_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeList2Value = _ExampleMiscellaneousProvFreeTimeList2Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1185, 1, 1),
    _ExampleMiscellaneousProvFreeTimeList2Value_Type()
)
exampleMiscellaneousProvFreeTimeList2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList2Value.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList2RowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeTimeList2RowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeList2RowStatus = _ExampleMiscellaneousProvFreeTimeList2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1185, 1, 2),
    _ExampleMiscellaneousProvFreeTimeList2RowStatus_Type()
)
exampleMiscellaneousProvFreeTimeList2RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList2RowStatus.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList3Table_Object = MibTable
exampleMiscellaneousProvFreeTimeList3Table = _ExampleMiscellaneousProvFreeTimeList3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1186)
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList3Table.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList3Entry_Object = MibTableRow
exampleMiscellaneousProvFreeTimeList3Entry = _ExampleMiscellaneousProvFreeTimeList3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1186, 1)
)
exampleMiscellaneousProvFreeTimeList3Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleMiscellaneousProvFreeTimeList3Value"),
)
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList3Entry.setStatus("mandatory")


class _ExampleMiscellaneousProvFreeTimeList3Value_Type(EnterpriseDateAndTime):
    """Custom type exampleMiscellaneousProvFreeTimeList3Value based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ExampleMiscellaneousProvFreeTimeList3Value_Type.__name__ = "EnterpriseDateAndTime"
_ExampleMiscellaneousProvFreeTimeList3Value_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeList3Value = _ExampleMiscellaneousProvFreeTimeList3Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1186, 1, 1),
    _ExampleMiscellaneousProvFreeTimeList3Value_Type()
)
exampleMiscellaneousProvFreeTimeList3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList3Value.setStatus("mandatory")
_ExampleMiscellaneousProvFreeTimeList3RowStatus_Type = RowStatus
_ExampleMiscellaneousProvFreeTimeList3RowStatus_Object = MibTableColumn
exampleMiscellaneousProvFreeTimeList3RowStatus = _ExampleMiscellaneousProvFreeTimeList3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 15, 1186, 1, 2),
    _ExampleMiscellaneousProvFreeTimeList3RowStatus_Type()
)
exampleMiscellaneousProvFreeTimeList3RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleMiscellaneousProvFreeTimeList3RowStatus.setStatus("mandatory")
_ExampleOneIndex_ObjectIdentity = ObjectIdentity
exampleOneIndex = _ExampleOneIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16)
)
_ExampleOneIndexRowStatusTable_Object = MibTable
exampleOneIndexRowStatusTable = _ExampleOneIndexRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 1)
)
if mibBuilder.loadTexts:
    exampleOneIndexRowStatusTable.setStatus("mandatory")
_ExampleOneIndexRowStatusEntry_Object = MibTableRow
exampleOneIndexRowStatusEntry = _ExampleOneIndexRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 1, 1)
)
exampleOneIndexRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOneIndexOneIndex"),
)
if mibBuilder.loadTexts:
    exampleOneIndexRowStatusEntry.setStatus("mandatory")
_ExampleOneIndexRowStatus_Type = RowStatus
_ExampleOneIndexRowStatus_Object = MibTableColumn
exampleOneIndexRowStatus = _ExampleOneIndexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 1, 1, 1),
    _ExampleOneIndexRowStatus_Type()
)
exampleOneIndexRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOneIndexRowStatus.setStatus("mandatory")
_ExampleOneIndexComponentName_Type = DisplayString
_ExampleOneIndexComponentName_Object = MibTableColumn
exampleOneIndexComponentName = _ExampleOneIndexComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 1, 1, 2),
    _ExampleOneIndexComponentName_Type()
)
exampleOneIndexComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleOneIndexComponentName.setStatus("mandatory")
_ExampleOneIndexStorageType_Type = StorageType
_ExampleOneIndexStorageType_Object = MibTableColumn
exampleOneIndexStorageType = _ExampleOneIndexStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 1, 1, 4),
    _ExampleOneIndexStorageType_Type()
)
exampleOneIndexStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleOneIndexStorageType.setStatus("mandatory")


class _ExampleOneIndexOneIndex_Type(Integer32):
    """Custom type exampleOneIndexOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleOneIndexOneIndex_Type.__name__ = "Integer32"
_ExampleOneIndexOneIndex_Object = MibTableColumn
exampleOneIndexOneIndex = _ExampleOneIndexOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 1, 1, 10),
    _ExampleOneIndexOneIndex_Type()
)
exampleOneIndexOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleOneIndexOneIndex.setStatus("mandatory")
_ExampleOneIndexProvisionedTable_Object = MibTable
exampleOneIndexProvisionedTable = _ExampleOneIndexProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 10)
)
if mibBuilder.loadTexts:
    exampleOneIndexProvisionedTable.setStatus("mandatory")
_ExampleOneIndexProvisionedEntry_Object = MibTableRow
exampleOneIndexProvisionedEntry = _ExampleOneIndexProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 10, 1)
)
exampleOneIndexProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOneIndexOneIndex"),
)
if mibBuilder.loadTexts:
    exampleOneIndexProvisionedEntry.setStatus("mandatory")


class _ExampleOneIndexProvAttribute_Type(Unsigned32):
    """Custom type exampleOneIndexProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleOneIndexProvAttribute_Type.__name__ = "Unsigned32"
_ExampleOneIndexProvAttribute_Object = MibTableColumn
exampleOneIndexProvAttribute = _ExampleOneIndexProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 16, 10, 1, 1),
    _ExampleOneIndexProvAttribute_Type()
)
exampleOneIndexProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOneIndexProvAttribute.setStatus("mandatory")
_ExampleTwoIndices_ObjectIdentity = ObjectIdentity
exampleTwoIndices = _ExampleTwoIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17)
)
_ExampleTwoIndicesRowStatusTable_Object = MibTable
exampleTwoIndicesRowStatusTable = _ExampleTwoIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1)
)
if mibBuilder.loadTexts:
    exampleTwoIndicesRowStatusTable.setStatus("mandatory")
_ExampleTwoIndicesRowStatusEntry_Object = MibTableRow
exampleTwoIndicesRowStatusEntry = _ExampleTwoIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1, 1)
)
exampleTwoIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleTwoIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleTwoIndicesTwoIndex"),
)
if mibBuilder.loadTexts:
    exampleTwoIndicesRowStatusEntry.setStatus("mandatory")
_ExampleTwoIndicesRowStatus_Type = RowStatus
_ExampleTwoIndicesRowStatus_Object = MibTableColumn
exampleTwoIndicesRowStatus = _ExampleTwoIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1, 1, 1),
    _ExampleTwoIndicesRowStatus_Type()
)
exampleTwoIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleTwoIndicesRowStatus.setStatus("mandatory")
_ExampleTwoIndicesComponentName_Type = DisplayString
_ExampleTwoIndicesComponentName_Object = MibTableColumn
exampleTwoIndicesComponentName = _ExampleTwoIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1, 1, 2),
    _ExampleTwoIndicesComponentName_Type()
)
exampleTwoIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleTwoIndicesComponentName.setStatus("mandatory")
_ExampleTwoIndicesStorageType_Type = StorageType
_ExampleTwoIndicesStorageType_Object = MibTableColumn
exampleTwoIndicesStorageType = _ExampleTwoIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1, 1, 4),
    _ExampleTwoIndicesStorageType_Type()
)
exampleTwoIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleTwoIndicesStorageType.setStatus("mandatory")


class _ExampleTwoIndicesOneIndex_Type(Integer32):
    """Custom type exampleTwoIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleTwoIndicesOneIndex_Type.__name__ = "Integer32"
_ExampleTwoIndicesOneIndex_Object = MibTableColumn
exampleTwoIndicesOneIndex = _ExampleTwoIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1, 1, 10),
    _ExampleTwoIndicesOneIndex_Type()
)
exampleTwoIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleTwoIndicesOneIndex.setStatus("mandatory")


class _ExampleTwoIndicesTwoIndex_Type(Integer32):
    """Custom type exampleTwoIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleTwoIndicesTwoIndex_Type.__name__ = "Integer32"
_ExampleTwoIndicesTwoIndex_Object = MibTableColumn
exampleTwoIndicesTwoIndex = _ExampleTwoIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 1, 1, 11),
    _ExampleTwoIndicesTwoIndex_Type()
)
exampleTwoIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleTwoIndicesTwoIndex.setStatus("mandatory")
_ExampleTwoIndicesProvisionedTable_Object = MibTable
exampleTwoIndicesProvisionedTable = _ExampleTwoIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 10)
)
if mibBuilder.loadTexts:
    exampleTwoIndicesProvisionedTable.setStatus("mandatory")
_ExampleTwoIndicesProvisionedEntry_Object = MibTableRow
exampleTwoIndicesProvisionedEntry = _ExampleTwoIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 10, 1)
)
exampleTwoIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleTwoIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleTwoIndicesTwoIndex"),
)
if mibBuilder.loadTexts:
    exampleTwoIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleTwoIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleTwoIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleTwoIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleTwoIndicesProvAttribute_Object = MibTableColumn
exampleTwoIndicesProvAttribute = _ExampleTwoIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 17, 10, 1, 1),
    _ExampleTwoIndicesProvAttribute_Type()
)
exampleTwoIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleTwoIndicesProvAttribute.setStatus("mandatory")
_ExampleThreeIndices_ObjectIdentity = ObjectIdentity
exampleThreeIndices = _ExampleThreeIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18)
)
_ExampleThreeIndicesRowStatusTable_Object = MibTable
exampleThreeIndicesRowStatusTable = _ExampleThreeIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1)
)
if mibBuilder.loadTexts:
    exampleThreeIndicesRowStatusTable.setStatus("mandatory")
_ExampleThreeIndicesRowStatusEntry_Object = MibTableRow
exampleThreeIndicesRowStatusEntry = _ExampleThreeIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1)
)
exampleThreeIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleThreeIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleThreeIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleThreeIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleThreeIndicesRowStatusEntry.setStatus("mandatory")
_ExampleThreeIndicesRowStatus_Type = RowStatus
_ExampleThreeIndicesRowStatus_Object = MibTableColumn
exampleThreeIndicesRowStatus = _ExampleThreeIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1, 1),
    _ExampleThreeIndicesRowStatus_Type()
)
exampleThreeIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleThreeIndicesRowStatus.setStatus("mandatory")
_ExampleThreeIndicesComponentName_Type = DisplayString
_ExampleThreeIndicesComponentName_Object = MibTableColumn
exampleThreeIndicesComponentName = _ExampleThreeIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1, 2),
    _ExampleThreeIndicesComponentName_Type()
)
exampleThreeIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleThreeIndicesComponentName.setStatus("mandatory")
_ExampleThreeIndicesStorageType_Type = StorageType
_ExampleThreeIndicesStorageType_Object = MibTableColumn
exampleThreeIndicesStorageType = _ExampleThreeIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1, 4),
    _ExampleThreeIndicesStorageType_Type()
)
exampleThreeIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleThreeIndicesStorageType.setStatus("mandatory")


class _ExampleThreeIndicesOneIndex_Type(Integer32):
    """Custom type exampleThreeIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleThreeIndicesOneIndex_Type.__name__ = "Integer32"
_ExampleThreeIndicesOneIndex_Object = MibTableColumn
exampleThreeIndicesOneIndex = _ExampleThreeIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1, 10),
    _ExampleThreeIndicesOneIndex_Type()
)
exampleThreeIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleThreeIndicesOneIndex.setStatus("mandatory")


class _ExampleThreeIndicesTwoIndex_Type(Integer32):
    """Custom type exampleThreeIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleThreeIndicesTwoIndex_Type.__name__ = "Integer32"
_ExampleThreeIndicesTwoIndex_Object = MibTableColumn
exampleThreeIndicesTwoIndex = _ExampleThreeIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1, 11),
    _ExampleThreeIndicesTwoIndex_Type()
)
exampleThreeIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleThreeIndicesTwoIndex.setStatus("mandatory")


class _ExampleThreeIndicesThreeIndex_Type(Integer32):
    """Custom type exampleThreeIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleThreeIndicesThreeIndex_Type.__name__ = "Integer32"
_ExampleThreeIndicesThreeIndex_Object = MibTableColumn
exampleThreeIndicesThreeIndex = _ExampleThreeIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 1, 1, 12),
    _ExampleThreeIndicesThreeIndex_Type()
)
exampleThreeIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleThreeIndicesThreeIndex.setStatus("mandatory")
_ExampleThreeIndicesProvisionedTable_Object = MibTable
exampleThreeIndicesProvisionedTable = _ExampleThreeIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 10)
)
if mibBuilder.loadTexts:
    exampleThreeIndicesProvisionedTable.setStatus("mandatory")
_ExampleThreeIndicesProvisionedEntry_Object = MibTableRow
exampleThreeIndicesProvisionedEntry = _ExampleThreeIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 10, 1)
)
exampleThreeIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleThreeIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleThreeIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleThreeIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleThreeIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleThreeIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleThreeIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleThreeIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleThreeIndicesProvAttribute_Object = MibTableColumn
exampleThreeIndicesProvAttribute = _ExampleThreeIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 18, 10, 1, 1),
    _ExampleThreeIndicesProvAttribute_Type()
)
exampleThreeIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleThreeIndicesProvAttribute.setStatus("mandatory")
_ExampleFourIndices_ObjectIdentity = ObjectIdentity
exampleFourIndices = _ExampleFourIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19)
)
_ExampleFourIndicesRowStatusTable_Object = MibTable
exampleFourIndicesRowStatusTable = _ExampleFourIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1)
)
if mibBuilder.loadTexts:
    exampleFourIndicesRowStatusTable.setStatus("mandatory")
_ExampleFourIndicesRowStatusEntry_Object = MibTableRow
exampleFourIndicesRowStatusEntry = _ExampleFourIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1)
)
exampleFourIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesThreeIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesFourIndex"),
)
if mibBuilder.loadTexts:
    exampleFourIndicesRowStatusEntry.setStatus("mandatory")
_ExampleFourIndicesRowStatus_Type = RowStatus
_ExampleFourIndicesRowStatus_Object = MibTableColumn
exampleFourIndicesRowStatus = _ExampleFourIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 1),
    _ExampleFourIndicesRowStatus_Type()
)
exampleFourIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFourIndicesRowStatus.setStatus("mandatory")
_ExampleFourIndicesComponentName_Type = DisplayString
_ExampleFourIndicesComponentName_Object = MibTableColumn
exampleFourIndicesComponentName = _ExampleFourIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 2),
    _ExampleFourIndicesComponentName_Type()
)
exampleFourIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleFourIndicesComponentName.setStatus("mandatory")
_ExampleFourIndicesStorageType_Type = StorageType
_ExampleFourIndicesStorageType_Object = MibTableColumn
exampleFourIndicesStorageType = _ExampleFourIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 4),
    _ExampleFourIndicesStorageType_Type()
)
exampleFourIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleFourIndicesStorageType.setStatus("mandatory")


class _ExampleFourIndicesOneIndex_Type(Integer32):
    """Custom type exampleFourIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleFourIndicesOneIndex_Type.__name__ = "Integer32"
_ExampleFourIndicesOneIndex_Object = MibTableColumn
exampleFourIndicesOneIndex = _ExampleFourIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 10),
    _ExampleFourIndicesOneIndex_Type()
)
exampleFourIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFourIndicesOneIndex.setStatus("mandatory")


class _ExampleFourIndicesTwoIndex_Type(Integer32):
    """Custom type exampleFourIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleFourIndicesTwoIndex_Type.__name__ = "Integer32"
_ExampleFourIndicesTwoIndex_Object = MibTableColumn
exampleFourIndicesTwoIndex = _ExampleFourIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 11),
    _ExampleFourIndicesTwoIndex_Type()
)
exampleFourIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFourIndicesTwoIndex.setStatus("mandatory")


class _ExampleFourIndicesThreeIndex_Type(Integer32):
    """Custom type exampleFourIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleFourIndicesThreeIndex_Type.__name__ = "Integer32"
_ExampleFourIndicesThreeIndex_Object = MibTableColumn
exampleFourIndicesThreeIndex = _ExampleFourIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 12),
    _ExampleFourIndicesThreeIndex_Type()
)
exampleFourIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFourIndicesThreeIndex.setStatus("mandatory")


class _ExampleFourIndicesFourIndex_Type(Integer32):
    """Custom type exampleFourIndicesFourIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleFourIndicesFourIndex_Type.__name__ = "Integer32"
_ExampleFourIndicesFourIndex_Object = MibTableColumn
exampleFourIndicesFourIndex = _ExampleFourIndicesFourIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 1, 1, 13),
    _ExampleFourIndicesFourIndex_Type()
)
exampleFourIndicesFourIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleFourIndicesFourIndex.setStatus("mandatory")
_ExampleFourIndicesProvisionedTable_Object = MibTable
exampleFourIndicesProvisionedTable = _ExampleFourIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 10)
)
if mibBuilder.loadTexts:
    exampleFourIndicesProvisionedTable.setStatus("mandatory")
_ExampleFourIndicesProvisionedEntry_Object = MibTableRow
exampleFourIndicesProvisionedEntry = _ExampleFourIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 10, 1)
)
exampleFourIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesThreeIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleFourIndicesFourIndex"),
)
if mibBuilder.loadTexts:
    exampleFourIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleFourIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleFourIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleFourIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleFourIndicesProvAttribute_Object = MibTableColumn
exampleFourIndicesProvAttribute = _ExampleFourIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 19, 10, 1, 1),
    _ExampleFourIndicesProvAttribute_Type()
)
exampleFourIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleFourIndicesProvAttribute.setStatus("mandatory")
_ExampleDecimalIndices_ObjectIdentity = ObjectIdentity
exampleDecimalIndices = _ExampleDecimalIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20)
)
_ExampleDecimalIndicesRowStatusTable_Object = MibTable
exampleDecimalIndicesRowStatusTable = _ExampleDecimalIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1)
)
if mibBuilder.loadTexts:
    exampleDecimalIndicesRowStatusTable.setStatus("mandatory")
_ExampleDecimalIndicesRowStatusEntry_Object = MibTableRow
exampleDecimalIndicesRowStatusEntry = _ExampleDecimalIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1)
)
exampleDecimalIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalIndicesRowStatusEntry.setStatus("mandatory")
_ExampleDecimalIndicesRowStatus_Type = RowStatus
_ExampleDecimalIndicesRowStatus_Object = MibTableColumn
exampleDecimalIndicesRowStatus = _ExampleDecimalIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1, 1),
    _ExampleDecimalIndicesRowStatus_Type()
)
exampleDecimalIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalIndicesRowStatus.setStatus("mandatory")
_ExampleDecimalIndicesComponentName_Type = DisplayString
_ExampleDecimalIndicesComponentName_Object = MibTableColumn
exampleDecimalIndicesComponentName = _ExampleDecimalIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1, 2),
    _ExampleDecimalIndicesComponentName_Type()
)
exampleDecimalIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDecimalIndicesComponentName.setStatus("mandatory")
_ExampleDecimalIndicesStorageType_Type = StorageType
_ExampleDecimalIndicesStorageType_Object = MibTableColumn
exampleDecimalIndicesStorageType = _ExampleDecimalIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1, 4),
    _ExampleDecimalIndicesStorageType_Type()
)
exampleDecimalIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDecimalIndicesStorageType.setStatus("mandatory")


class _ExampleDecimalIndicesOneIndex_Type(Integer32):
    """Custom type exampleDecimalIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 100),
    )


_ExampleDecimalIndicesOneIndex_Type.__name__ = "Integer32"
_ExampleDecimalIndicesOneIndex_Object = MibTableColumn
exampleDecimalIndicesOneIndex = _ExampleDecimalIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1, 10),
    _ExampleDecimalIndicesOneIndex_Type()
)
exampleDecimalIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalIndicesOneIndex.setStatus("mandatory")


class _ExampleDecimalIndicesTwoIndex_Type(Integer32):
    """Custom type exampleDecimalIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 100),
    )


_ExampleDecimalIndicesTwoIndex_Type.__name__ = "Integer32"
_ExampleDecimalIndicesTwoIndex_Object = MibTableColumn
exampleDecimalIndicesTwoIndex = _ExampleDecimalIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1, 11),
    _ExampleDecimalIndicesTwoIndex_Type()
)
exampleDecimalIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalIndicesTwoIndex.setStatus("mandatory")


class _ExampleDecimalIndicesThreeIndex_Type(Integer32):
    """Custom type exampleDecimalIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 100),
    )


_ExampleDecimalIndicesThreeIndex_Type.__name__ = "Integer32"
_ExampleDecimalIndicesThreeIndex_Object = MibTableColumn
exampleDecimalIndicesThreeIndex = _ExampleDecimalIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 1, 1, 12),
    _ExampleDecimalIndicesThreeIndex_Type()
)
exampleDecimalIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDecimalIndicesThreeIndex.setStatus("mandatory")
_ExampleDecimalIndicesProvisionedTable_Object = MibTable
exampleDecimalIndicesProvisionedTable = _ExampleDecimalIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 10)
)
if mibBuilder.loadTexts:
    exampleDecimalIndicesProvisionedTable.setStatus("mandatory")
_ExampleDecimalIndicesProvisionedEntry_Object = MibTableRow
exampleDecimalIndicesProvisionedEntry = _ExampleDecimalIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 10, 1)
)
exampleDecimalIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDecimalIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleDecimalIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleDecimalIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleDecimalIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDecimalIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleDecimalIndicesProvAttribute_Object = MibTableColumn
exampleDecimalIndicesProvAttribute = _ExampleDecimalIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 20, 10, 1, 1),
    _ExampleDecimalIndicesProvAttribute_Type()
)
exampleDecimalIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDecimalIndicesProvAttribute.setStatus("mandatory")
_ExampleHexIndices_ObjectIdentity = ObjectIdentity
exampleHexIndices = _ExampleHexIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21)
)
_ExampleHexIndicesRowStatusTable_Object = MibTable
exampleHexIndicesRowStatusTable = _ExampleHexIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1)
)
if mibBuilder.loadTexts:
    exampleHexIndicesRowStatusTable.setStatus("mandatory")
_ExampleHexIndicesRowStatusEntry_Object = MibTableRow
exampleHexIndicesRowStatusEntry = _ExampleHexIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1)
)
exampleHexIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleHexIndicesRowStatusEntry.setStatus("mandatory")
_ExampleHexIndicesRowStatus_Type = RowStatus
_ExampleHexIndicesRowStatus_Object = MibTableColumn
exampleHexIndicesRowStatus = _ExampleHexIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1, 1),
    _ExampleHexIndicesRowStatus_Type()
)
exampleHexIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexIndicesRowStatus.setStatus("mandatory")
_ExampleHexIndicesComponentName_Type = DisplayString
_ExampleHexIndicesComponentName_Object = MibTableColumn
exampleHexIndicesComponentName = _ExampleHexIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1, 2),
    _ExampleHexIndicesComponentName_Type()
)
exampleHexIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHexIndicesComponentName.setStatus("mandatory")
_ExampleHexIndicesStorageType_Type = StorageType
_ExampleHexIndicesStorageType_Object = MibTableColumn
exampleHexIndicesStorageType = _ExampleHexIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1, 4),
    _ExampleHexIndicesStorageType_Type()
)
exampleHexIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHexIndicesStorageType.setStatus("mandatory")


class _ExampleHexIndicesOneIndex_Type(Integer32):
    """Custom type exampleHexIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(256, 256),
    )


_ExampleHexIndicesOneIndex_Type.__name__ = "Integer32"
_ExampleHexIndicesOneIndex_Object = MibTableColumn
exampleHexIndicesOneIndex = _ExampleHexIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1, 10),
    _ExampleHexIndicesOneIndex_Type()
)
exampleHexIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexIndicesOneIndex.setStatus("mandatory")


class _ExampleHexIndicesTwoIndex_Type(Integer32):
    """Custom type exampleHexIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(256, 256),
    )


_ExampleHexIndicesTwoIndex_Type.__name__ = "Integer32"
_ExampleHexIndicesTwoIndex_Object = MibTableColumn
exampleHexIndicesTwoIndex = _ExampleHexIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1, 11),
    _ExampleHexIndicesTwoIndex_Type()
)
exampleHexIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexIndicesTwoIndex.setStatus("mandatory")


class _ExampleHexIndicesThreeIndex_Type(Integer32):
    """Custom type exampleHexIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(256, 256),
    )


_ExampleHexIndicesThreeIndex_Type.__name__ = "Integer32"
_ExampleHexIndicesThreeIndex_Object = MibTableColumn
exampleHexIndicesThreeIndex = _ExampleHexIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 1, 1, 12),
    _ExampleHexIndicesThreeIndex_Type()
)
exampleHexIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexIndicesThreeIndex.setStatus("mandatory")
_ExampleHexIndicesProvisionedTable_Object = MibTable
exampleHexIndicesProvisionedTable = _ExampleHexIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 10)
)
if mibBuilder.loadTexts:
    exampleHexIndicesProvisionedTable.setStatus("mandatory")
_ExampleHexIndicesProvisionedEntry_Object = MibTableRow
exampleHexIndicesProvisionedEntry = _ExampleHexIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 10, 1)
)
exampleHexIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleHexIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleHexIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleHexIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleHexIndicesProvAttribute_Object = MibTableColumn
exampleHexIndicesProvAttribute = _ExampleHexIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 21, 10, 1, 1),
    _ExampleHexIndicesProvAttribute_Type()
)
exampleHexIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexIndicesProvAttribute.setStatus("mandatory")
_ExampleIpAddrIndices_ObjectIdentity = ObjectIdentity
exampleIpAddrIndices = _ExampleIpAddrIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22)
)
_ExampleIpAddrIndicesRowStatusTable_Object = MibTable
exampleIpAddrIndicesRowStatusTable = _ExampleIpAddrIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1)
)
if mibBuilder.loadTexts:
    exampleIpAddrIndicesRowStatusTable.setStatus("mandatory")
_ExampleIpAddrIndicesRowStatusEntry_Object = MibTableRow
exampleIpAddrIndicesRowStatusEntry = _ExampleIpAddrIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1)
)
exampleIpAddrIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddrIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddrIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddrIndicesRowStatusEntry.setStatus("mandatory")
_ExampleIpAddrIndicesRowStatus_Type = RowStatus
_ExampleIpAddrIndicesRowStatus_Object = MibTableColumn
exampleIpAddrIndicesRowStatus = _ExampleIpAddrIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1, 1),
    _ExampleIpAddrIndicesRowStatus_Type()
)
exampleIpAddrIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesRowStatus.setStatus("mandatory")
_ExampleIpAddrIndicesComponentName_Type = DisplayString
_ExampleIpAddrIndicesComponentName_Object = MibTableColumn
exampleIpAddrIndicesComponentName = _ExampleIpAddrIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1, 2),
    _ExampleIpAddrIndicesComponentName_Type()
)
exampleIpAddrIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesComponentName.setStatus("mandatory")
_ExampleIpAddrIndicesStorageType_Type = StorageType
_ExampleIpAddrIndicesStorageType_Object = MibTableColumn
exampleIpAddrIndicesStorageType = _ExampleIpAddrIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1, 4),
    _ExampleIpAddrIndicesStorageType_Type()
)
exampleIpAddrIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesStorageType.setStatus("mandatory")
_ExampleIpAddrIndicesOneIndex_Type = IpAddress
_ExampleIpAddrIndicesOneIndex_Object = MibTableColumn
exampleIpAddrIndicesOneIndex = _ExampleIpAddrIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1, 10),
    _ExampleIpAddrIndicesOneIndex_Type()
)
exampleIpAddrIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesOneIndex.setStatus("mandatory")
_ExampleIpAddrIndicesTwoIndex_Type = IpAddress
_ExampleIpAddrIndicesTwoIndex_Object = MibTableColumn
exampleIpAddrIndicesTwoIndex = _ExampleIpAddrIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1, 11),
    _ExampleIpAddrIndicesTwoIndex_Type()
)
exampleIpAddrIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesTwoIndex.setStatus("mandatory")
_ExampleIpAddrIndicesThreeIndex_Type = IpAddress
_ExampleIpAddrIndicesThreeIndex_Object = MibTableColumn
exampleIpAddrIndicesThreeIndex = _ExampleIpAddrIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 1, 1, 12),
    _ExampleIpAddrIndicesThreeIndex_Type()
)
exampleIpAddrIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesThreeIndex.setStatus("mandatory")
_ExampleIpAddrIndicesProvisionedTable_Object = MibTable
exampleIpAddrIndicesProvisionedTable = _ExampleIpAddrIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 10)
)
if mibBuilder.loadTexts:
    exampleIpAddrIndicesProvisionedTable.setStatus("mandatory")
_ExampleIpAddrIndicesProvisionedEntry_Object = MibTableRow
exampleIpAddrIndicesProvisionedEntry = _ExampleIpAddrIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 10, 1)
)
exampleIpAddrIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddrIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddrIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIpAddrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleIpAddrIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleIpAddrIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleIpAddrIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleIpAddrIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleIpAddrIndicesProvAttribute_Object = MibTableColumn
exampleIpAddrIndicesProvAttribute = _ExampleIpAddrIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 22, 10, 1, 1),
    _ExampleIpAddrIndicesProvAttribute_Type()
)
exampleIpAddrIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleIpAddrIndicesProvAttribute.setStatus("mandatory")
_ExampleAsciiIndices_ObjectIdentity = ObjectIdentity
exampleAsciiIndices = _ExampleAsciiIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23)
)
_ExampleAsciiIndicesRowStatusTable_Object = MibTable
exampleAsciiIndicesRowStatusTable = _ExampleAsciiIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1)
)
if mibBuilder.loadTexts:
    exampleAsciiIndicesRowStatusTable.setStatus("mandatory")
_ExampleAsciiIndicesRowStatusEntry_Object = MibTableRow
exampleAsciiIndicesRowStatusEntry = _ExampleAsciiIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1)
)
exampleAsciiIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleAsciiIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleAsciiIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleAsciiIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleAsciiIndicesRowStatusEntry.setStatus("mandatory")
_ExampleAsciiIndicesRowStatus_Type = RowStatus
_ExampleAsciiIndicesRowStatus_Object = MibTableColumn
exampleAsciiIndicesRowStatus = _ExampleAsciiIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1, 1),
    _ExampleAsciiIndicesRowStatus_Type()
)
exampleAsciiIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleAsciiIndicesRowStatus.setStatus("mandatory")
_ExampleAsciiIndicesComponentName_Type = DisplayString
_ExampleAsciiIndicesComponentName_Object = MibTableColumn
exampleAsciiIndicesComponentName = _ExampleAsciiIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1, 2),
    _ExampleAsciiIndicesComponentName_Type()
)
exampleAsciiIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAsciiIndicesComponentName.setStatus("mandatory")
_ExampleAsciiIndicesStorageType_Type = StorageType
_ExampleAsciiIndicesStorageType_Object = MibTableColumn
exampleAsciiIndicesStorageType = _ExampleAsciiIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1, 4),
    _ExampleAsciiIndicesStorageType_Type()
)
exampleAsciiIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleAsciiIndicesStorageType.setStatus("mandatory")


class _ExampleAsciiIndicesOneIndex_Type(AsciiStringIndex):
    """Custom type exampleAsciiIndicesOneIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleAsciiIndicesOneIndex_Type.__name__ = "AsciiStringIndex"
_ExampleAsciiIndicesOneIndex_Object = MibTableColumn
exampleAsciiIndicesOneIndex = _ExampleAsciiIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1, 10),
    _ExampleAsciiIndicesOneIndex_Type()
)
exampleAsciiIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleAsciiIndicesOneIndex.setStatus("mandatory")


class _ExampleAsciiIndicesTwoIndex_Type(AsciiStringIndex):
    """Custom type exampleAsciiIndicesTwoIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleAsciiIndicesTwoIndex_Type.__name__ = "AsciiStringIndex"
_ExampleAsciiIndicesTwoIndex_Object = MibTableColumn
exampleAsciiIndicesTwoIndex = _ExampleAsciiIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1, 11),
    _ExampleAsciiIndicesTwoIndex_Type()
)
exampleAsciiIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleAsciiIndicesTwoIndex.setStatus("mandatory")


class _ExampleAsciiIndicesThreeIndex_Type(AsciiStringIndex):
    """Custom type exampleAsciiIndicesThreeIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleAsciiIndicesThreeIndex_Type.__name__ = "AsciiStringIndex"
_ExampleAsciiIndicesThreeIndex_Object = MibTableColumn
exampleAsciiIndicesThreeIndex = _ExampleAsciiIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 1, 1, 12),
    _ExampleAsciiIndicesThreeIndex_Type()
)
exampleAsciiIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleAsciiIndicesThreeIndex.setStatus("mandatory")
_ExampleAsciiIndicesProvisionedTable_Object = MibTable
exampleAsciiIndicesProvisionedTable = _ExampleAsciiIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 10)
)
if mibBuilder.loadTexts:
    exampleAsciiIndicesProvisionedTable.setStatus("mandatory")
_ExampleAsciiIndicesProvisionedEntry_Object = MibTableRow
exampleAsciiIndicesProvisionedEntry = _ExampleAsciiIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 10, 1)
)
exampleAsciiIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleAsciiIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleAsciiIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleAsciiIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleAsciiIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleAsciiIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleAsciiIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleAsciiIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleAsciiIndicesProvAttribute_Object = MibTableColumn
exampleAsciiIndicesProvAttribute = _ExampleAsciiIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 23, 10, 1, 1),
    _ExampleAsciiIndicesProvAttribute_Type()
)
exampleAsciiIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleAsciiIndicesProvAttribute.setStatus("mandatory")
_ExampleHexStrIndices_ObjectIdentity = ObjectIdentity
exampleHexStrIndices = _ExampleHexStrIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24)
)
_ExampleHexStrIndicesRowStatusTable_Object = MibTable
exampleHexStrIndicesRowStatusTable = _ExampleHexStrIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1)
)
if mibBuilder.loadTexts:
    exampleHexStrIndicesRowStatusTable.setStatus("mandatory")
_ExampleHexStrIndicesRowStatusEntry_Object = MibTableRow
exampleHexStrIndicesRowStatusEntry = _ExampleHexStrIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1)
)
exampleHexStrIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexStrIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexStrIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexStrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleHexStrIndicesRowStatusEntry.setStatus("mandatory")
_ExampleHexStrIndicesRowStatus_Type = RowStatus
_ExampleHexStrIndicesRowStatus_Object = MibTableColumn
exampleHexStrIndicesRowStatus = _ExampleHexStrIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1, 1),
    _ExampleHexStrIndicesRowStatus_Type()
)
exampleHexStrIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexStrIndicesRowStatus.setStatus("mandatory")
_ExampleHexStrIndicesComponentName_Type = DisplayString
_ExampleHexStrIndicesComponentName_Object = MibTableColumn
exampleHexStrIndicesComponentName = _ExampleHexStrIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1, 2),
    _ExampleHexStrIndicesComponentName_Type()
)
exampleHexStrIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHexStrIndicesComponentName.setStatus("mandatory")
_ExampleHexStrIndicesStorageType_Type = StorageType
_ExampleHexStrIndicesStorageType_Object = MibTableColumn
exampleHexStrIndicesStorageType = _ExampleHexStrIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1, 4),
    _ExampleHexStrIndicesStorageType_Type()
)
exampleHexStrIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleHexStrIndicesStorageType.setStatus("mandatory")


class _ExampleHexStrIndicesOneIndex_Type(HexString):
    """Custom type exampleHexStrIndicesOneIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleHexStrIndicesOneIndex_Type.__name__ = "HexString"
_ExampleHexStrIndicesOneIndex_Object = MibTableColumn
exampleHexStrIndicesOneIndex = _ExampleHexStrIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1, 10),
    _ExampleHexStrIndicesOneIndex_Type()
)
exampleHexStrIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexStrIndicesOneIndex.setStatus("mandatory")


class _ExampleHexStrIndicesTwoIndex_Type(HexString):
    """Custom type exampleHexStrIndicesTwoIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleHexStrIndicesTwoIndex_Type.__name__ = "HexString"
_ExampleHexStrIndicesTwoIndex_Object = MibTableColumn
exampleHexStrIndicesTwoIndex = _ExampleHexStrIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1, 11),
    _ExampleHexStrIndicesTwoIndex_Type()
)
exampleHexStrIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexStrIndicesTwoIndex.setStatus("mandatory")


class _ExampleHexStrIndicesThreeIndex_Type(HexString):
    """Custom type exampleHexStrIndicesThreeIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleHexStrIndicesThreeIndex_Type.__name__ = "HexString"
_ExampleHexStrIndicesThreeIndex_Object = MibTableColumn
exampleHexStrIndicesThreeIndex = _ExampleHexStrIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 1, 1, 12),
    _ExampleHexStrIndicesThreeIndex_Type()
)
exampleHexStrIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleHexStrIndicesThreeIndex.setStatus("mandatory")
_ExampleHexStrIndicesProvisionedTable_Object = MibTable
exampleHexStrIndicesProvisionedTable = _ExampleHexStrIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 10)
)
if mibBuilder.loadTexts:
    exampleHexStrIndicesProvisionedTable.setStatus("mandatory")
_ExampleHexStrIndicesProvisionedEntry_Object = MibTableRow
exampleHexStrIndicesProvisionedEntry = _ExampleHexStrIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 10, 1)
)
exampleHexStrIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexStrIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexStrIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleHexStrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleHexStrIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleHexStrIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleHexStrIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleHexStrIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleHexStrIndicesProvAttribute_Object = MibTableColumn
exampleHexStrIndicesProvAttribute = _ExampleHexStrIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 24, 10, 1, 1),
    _ExampleHexStrIndicesProvAttribute_Type()
)
exampleHexStrIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleHexStrIndicesProvAttribute.setStatus("mandatory")
_ExampleBcdIndices_ObjectIdentity = ObjectIdentity
exampleBcdIndices = _ExampleBcdIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25)
)
_ExampleBcdIndicesRowStatusTable_Object = MibTable
exampleBcdIndicesRowStatusTable = _ExampleBcdIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1)
)
if mibBuilder.loadTexts:
    exampleBcdIndicesRowStatusTable.setStatus("mandatory")
_ExampleBcdIndicesRowStatusEntry_Object = MibTableRow
exampleBcdIndicesRowStatusEntry = _ExampleBcdIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1)
)
exampleBcdIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdIndicesRowStatusEntry.setStatus("mandatory")
_ExampleBcdIndicesRowStatus_Type = RowStatus
_ExampleBcdIndicesRowStatus_Object = MibTableColumn
exampleBcdIndicesRowStatus = _ExampleBcdIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1, 1),
    _ExampleBcdIndicesRowStatus_Type()
)
exampleBcdIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdIndicesRowStatus.setStatus("mandatory")
_ExampleBcdIndicesComponentName_Type = DisplayString
_ExampleBcdIndicesComponentName_Object = MibTableColumn
exampleBcdIndicesComponentName = _ExampleBcdIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1, 2),
    _ExampleBcdIndicesComponentName_Type()
)
exampleBcdIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleBcdIndicesComponentName.setStatus("mandatory")
_ExampleBcdIndicesStorageType_Type = StorageType
_ExampleBcdIndicesStorageType_Object = MibTableColumn
exampleBcdIndicesStorageType = _ExampleBcdIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1, 4),
    _ExampleBcdIndicesStorageType_Type()
)
exampleBcdIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleBcdIndicesStorageType.setStatus("mandatory")


class _ExampleBcdIndicesOneIndex_Type(DigitString):
    """Custom type exampleBcdIndicesOneIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleBcdIndicesOneIndex_Type.__name__ = "DigitString"
_ExampleBcdIndicesOneIndex_Object = MibTableColumn
exampleBcdIndicesOneIndex = _ExampleBcdIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1, 10),
    _ExampleBcdIndicesOneIndex_Type()
)
exampleBcdIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdIndicesOneIndex.setStatus("mandatory")


class _ExampleBcdIndicesTwoIndex_Type(DigitString):
    """Custom type exampleBcdIndicesTwoIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleBcdIndicesTwoIndex_Type.__name__ = "DigitString"
_ExampleBcdIndicesTwoIndex_Object = MibTableColumn
exampleBcdIndicesTwoIndex = _ExampleBcdIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1, 11),
    _ExampleBcdIndicesTwoIndex_Type()
)
exampleBcdIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdIndicesTwoIndex.setStatus("mandatory")


class _ExampleBcdIndicesThreeIndex_Type(DigitString):
    """Custom type exampleBcdIndicesThreeIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleBcdIndicesThreeIndex_Type.__name__ = "DigitString"
_ExampleBcdIndicesThreeIndex_Object = MibTableColumn
exampleBcdIndicesThreeIndex = _ExampleBcdIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 1, 1, 12),
    _ExampleBcdIndicesThreeIndex_Type()
)
exampleBcdIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleBcdIndicesThreeIndex.setStatus("mandatory")
_ExampleBcdIndicesProvisionedTable_Object = MibTable
exampleBcdIndicesProvisionedTable = _ExampleBcdIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 10)
)
if mibBuilder.loadTexts:
    exampleBcdIndicesProvisionedTable.setStatus("mandatory")
_ExampleBcdIndicesProvisionedEntry_Object = MibTableRow
exampleBcdIndicesProvisionedEntry = _ExampleBcdIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 10, 1)
)
exampleBcdIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleBcdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleBcdIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleBcdIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleBcdIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleBcdIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleBcdIndicesProvAttribute_Object = MibTableColumn
exampleBcdIndicesProvAttribute = _ExampleBcdIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 25, 10, 1, 1),
    _ExampleBcdIndicesProvAttribute_Type()
)
exampleBcdIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleBcdIndicesProvAttribute.setStatus("mandatory")
_ExampleEnumIndices_ObjectIdentity = ObjectIdentity
exampleEnumIndices = _ExampleEnumIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26)
)
_ExampleEnumIndicesRowStatusTable_Object = MibTable
exampleEnumIndicesRowStatusTable = _ExampleEnumIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1)
)
if mibBuilder.loadTexts:
    exampleEnumIndicesRowStatusTable.setStatus("mandatory")
_ExampleEnumIndicesRowStatusEntry_Object = MibTableRow
exampleEnumIndicesRowStatusEntry = _ExampleEnumIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1)
)
exampleEnumIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumIndicesRowStatusEntry.setStatus("mandatory")
_ExampleEnumIndicesRowStatus_Type = RowStatus
_ExampleEnumIndicesRowStatus_Object = MibTableColumn
exampleEnumIndicesRowStatus = _ExampleEnumIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1, 1),
    _ExampleEnumIndicesRowStatus_Type()
)
exampleEnumIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumIndicesRowStatus.setStatus("mandatory")
_ExampleEnumIndicesComponentName_Type = DisplayString
_ExampleEnumIndicesComponentName_Object = MibTableColumn
exampleEnumIndicesComponentName = _ExampleEnumIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1, 2),
    _ExampleEnumIndicesComponentName_Type()
)
exampleEnumIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleEnumIndicesComponentName.setStatus("mandatory")
_ExampleEnumIndicesStorageType_Type = StorageType
_ExampleEnumIndicesStorageType_Object = MibTableColumn
exampleEnumIndicesStorageType = _ExampleEnumIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1, 4),
    _ExampleEnumIndicesStorageType_Type()
)
exampleEnumIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleEnumIndicesStorageType.setStatus("mandatory")


class _ExampleEnumIndicesOneIndex_Type(Integer32):
    """Custom type exampleEnumIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )


_ExampleEnumIndicesOneIndex_Type.__name__ = "Integer32"
_ExampleEnumIndicesOneIndex_Object = MibTableColumn
exampleEnumIndicesOneIndex = _ExampleEnumIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1, 10),
    _ExampleEnumIndicesOneIndex_Type()
)
exampleEnumIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumIndicesOneIndex.setStatus("mandatory")


class _ExampleEnumIndicesTwoIndex_Type(Integer32):
    """Custom type exampleEnumIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )


_ExampleEnumIndicesTwoIndex_Type.__name__ = "Integer32"
_ExampleEnumIndicesTwoIndex_Object = MibTableColumn
exampleEnumIndicesTwoIndex = _ExampleEnumIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1, 11),
    _ExampleEnumIndicesTwoIndex_Type()
)
exampleEnumIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumIndicesTwoIndex.setStatus("mandatory")


class _ExampleEnumIndicesThreeIndex_Type(Integer32):
    """Custom type exampleEnumIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )


_ExampleEnumIndicesThreeIndex_Type.__name__ = "Integer32"
_ExampleEnumIndicesThreeIndex_Object = MibTableColumn
exampleEnumIndicesThreeIndex = _ExampleEnumIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 1, 1, 12),
    _ExampleEnumIndicesThreeIndex_Type()
)
exampleEnumIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleEnumIndicesThreeIndex.setStatus("mandatory")
_ExampleEnumIndicesProvisionedTable_Object = MibTable
exampleEnumIndicesProvisionedTable = _ExampleEnumIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 10)
)
if mibBuilder.loadTexts:
    exampleEnumIndicesProvisionedTable.setStatus("mandatory")
_ExampleEnumIndicesProvisionedEntry_Object = MibTableRow
exampleEnumIndicesProvisionedEntry = _ExampleEnumIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 10, 1)
)
exampleEnumIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleEnumIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleEnumIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleEnumIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleEnumIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleEnumIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleEnumIndicesProvAttribute_Object = MibTableColumn
exampleEnumIndicesProvAttribute = _ExampleEnumIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 26, 10, 1, 1),
    _ExampleEnumIndicesProvAttribute_Type()
)
exampleEnumIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleEnumIndicesProvAttribute.setStatus("mandatory")
_ExampleSequenceIndices_ObjectIdentity = ObjectIdentity
exampleSequenceIndices = _ExampleSequenceIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27)
)
_ExampleSequenceIndicesRowStatusTable_Object = MibTable
exampleSequenceIndicesRowStatusTable = _ExampleSequenceIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1)
)
if mibBuilder.loadTexts:
    exampleSequenceIndicesRowStatusTable.setStatus("mandatory")
_ExampleSequenceIndicesRowStatusEntry_Object = MibTableRow
exampleSequenceIndicesRowStatusEntry = _ExampleSequenceIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1)
)
exampleSequenceIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceIndicesRowStatusEntry.setStatus("mandatory")
_ExampleSequenceIndicesRowStatus_Type = RowStatus
_ExampleSequenceIndicesRowStatus_Object = MibTableColumn
exampleSequenceIndicesRowStatus = _ExampleSequenceIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1, 1),
    _ExampleSequenceIndicesRowStatus_Type()
)
exampleSequenceIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceIndicesRowStatus.setStatus("mandatory")
_ExampleSequenceIndicesComponentName_Type = DisplayString
_ExampleSequenceIndicesComponentName_Object = MibTableColumn
exampleSequenceIndicesComponentName = _ExampleSequenceIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1, 2),
    _ExampleSequenceIndicesComponentName_Type()
)
exampleSequenceIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleSequenceIndicesComponentName.setStatus("mandatory")
_ExampleSequenceIndicesStorageType_Type = StorageType
_ExampleSequenceIndicesStorageType_Object = MibTableColumn
exampleSequenceIndicesStorageType = _ExampleSequenceIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1, 4),
    _ExampleSequenceIndicesStorageType_Type()
)
exampleSequenceIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleSequenceIndicesStorageType.setStatus("mandatory")
_ExampleSequenceIndicesOneIndex_Type = ObjectIdentifier
_ExampleSequenceIndicesOneIndex_Object = MibTableColumn
exampleSequenceIndicesOneIndex = _ExampleSequenceIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1, 10),
    _ExampleSequenceIndicesOneIndex_Type()
)
exampleSequenceIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSequenceIndicesOneIndex.setStatus("mandatory")
_ExampleSequenceIndicesTwoIndex_Type = ObjectIdentifier
_ExampleSequenceIndicesTwoIndex_Object = MibTableColumn
exampleSequenceIndicesTwoIndex = _ExampleSequenceIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1, 11),
    _ExampleSequenceIndicesTwoIndex_Type()
)
exampleSequenceIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSequenceIndicesTwoIndex.setStatus("mandatory")
_ExampleSequenceIndicesThreeIndex_Type = ObjectIdentifier
_ExampleSequenceIndicesThreeIndex_Object = MibTableColumn
exampleSequenceIndicesThreeIndex = _ExampleSequenceIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 1, 1, 12),
    _ExampleSequenceIndicesThreeIndex_Type()
)
exampleSequenceIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleSequenceIndicesThreeIndex.setStatus("mandatory")
_ExampleSequenceIndicesProvisionedTable_Object = MibTable
exampleSequenceIndicesProvisionedTable = _ExampleSequenceIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 10)
)
if mibBuilder.loadTexts:
    exampleSequenceIndicesProvisionedTable.setStatus("mandatory")
_ExampleSequenceIndicesProvisionedEntry_Object = MibTableRow
exampleSequenceIndicesProvisionedEntry = _ExampleSequenceIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 10, 1)
)
exampleSequenceIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleSequenceIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleSequenceIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleSequenceIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleSequenceIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleSequenceIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleSequenceIndicesProvAttribute_Object = MibTableColumn
exampleSequenceIndicesProvAttribute = _ExampleSequenceIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 27, 10, 1, 1),
    _ExampleSequenceIndicesProvAttribute_Type()
)
exampleSequenceIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleSequenceIndicesProvAttribute.setStatus("mandatory")
_ExampleObjIdIndices_ObjectIdentity = ObjectIdentity
exampleObjIdIndices = _ExampleObjIdIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28)
)
_ExampleObjIdIndicesRowStatusTable_Object = MibTable
exampleObjIdIndicesRowStatusTable = _ExampleObjIdIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1)
)
if mibBuilder.loadTexts:
    exampleObjIdIndicesRowStatusTable.setStatus("mandatory")
_ExampleObjIdIndicesRowStatusEntry_Object = MibTableRow
exampleObjIdIndicesRowStatusEntry = _ExampleObjIdIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1)
)
exampleObjIdIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjIdIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjIdIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjIdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleObjIdIndicesRowStatusEntry.setStatus("mandatory")
_ExampleObjIdIndicesRowStatus_Type = RowStatus
_ExampleObjIdIndicesRowStatus_Object = MibTableColumn
exampleObjIdIndicesRowStatus = _ExampleObjIdIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1, 1),
    _ExampleObjIdIndicesRowStatus_Type()
)
exampleObjIdIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjIdIndicesRowStatus.setStatus("mandatory")
_ExampleObjIdIndicesComponentName_Type = DisplayString
_ExampleObjIdIndicesComponentName_Object = MibTableColumn
exampleObjIdIndicesComponentName = _ExampleObjIdIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1, 2),
    _ExampleObjIdIndicesComponentName_Type()
)
exampleObjIdIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleObjIdIndicesComponentName.setStatus("mandatory")
_ExampleObjIdIndicesStorageType_Type = StorageType
_ExampleObjIdIndicesStorageType_Object = MibTableColumn
exampleObjIdIndicesStorageType = _ExampleObjIdIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1, 4),
    _ExampleObjIdIndicesStorageType_Type()
)
exampleObjIdIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleObjIdIndicesStorageType.setStatus("mandatory")
_ExampleObjIdIndicesOneIndex_Type = ObjectIdentifier
_ExampleObjIdIndicesOneIndex_Object = MibTableColumn
exampleObjIdIndicesOneIndex = _ExampleObjIdIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1, 10),
    _ExampleObjIdIndicesOneIndex_Type()
)
exampleObjIdIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleObjIdIndicesOneIndex.setStatus("mandatory")
_ExampleObjIdIndicesTwoIndex_Type = ObjectIdentifier
_ExampleObjIdIndicesTwoIndex_Object = MibTableColumn
exampleObjIdIndicesTwoIndex = _ExampleObjIdIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1, 11),
    _ExampleObjIdIndicesTwoIndex_Type()
)
exampleObjIdIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleObjIdIndicesTwoIndex.setStatus("mandatory")
_ExampleObjIdIndicesThreeIndex_Type = ObjectIdentifier
_ExampleObjIdIndicesThreeIndex_Object = MibTableColumn
exampleObjIdIndicesThreeIndex = _ExampleObjIdIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 1, 1, 12),
    _ExampleObjIdIndicesThreeIndex_Type()
)
exampleObjIdIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleObjIdIndicesThreeIndex.setStatus("mandatory")
_ExampleObjIdIndicesProvisionedTable_Object = MibTable
exampleObjIdIndicesProvisionedTable = _ExampleObjIdIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 10)
)
if mibBuilder.loadTexts:
    exampleObjIdIndicesProvisionedTable.setStatus("mandatory")
_ExampleObjIdIndicesProvisionedEntry_Object = MibTableRow
exampleObjIdIndicesProvisionedEntry = _ExampleObjIdIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 10, 1)
)
exampleObjIdIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjIdIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjIdIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleObjIdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleObjIdIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleObjIdIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleObjIdIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleObjIdIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleObjIdIndicesProvAttribute_Object = MibTableColumn
exampleObjIdIndicesProvAttribute = _ExampleObjIdIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 28, 10, 1, 1),
    _ExampleObjIdIndicesProvAttribute_Type()
)
exampleObjIdIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleObjIdIndicesProvAttribute.setStatus("mandatory")
_ExampleDashedIndices_ObjectIdentity = ObjectIdentity
exampleDashedIndices = _ExampleDashedIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30)
)
_ExampleDashedIndicesRowStatusTable_Object = MibTable
exampleDashedIndicesRowStatusTable = _ExampleDashedIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1)
)
if mibBuilder.loadTexts:
    exampleDashedIndicesRowStatusTable.setStatus("mandatory")
_ExampleDashedIndicesRowStatusEntry_Object = MibTableRow
exampleDashedIndicesRowStatusEntry = _ExampleDashedIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1)
)
exampleDashedIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedIndicesRowStatusEntry.setStatus("mandatory")
_ExampleDashedIndicesRowStatus_Type = RowStatus
_ExampleDashedIndicesRowStatus_Object = MibTableColumn
exampleDashedIndicesRowStatus = _ExampleDashedIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1, 1),
    _ExampleDashedIndicesRowStatus_Type()
)
exampleDashedIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedIndicesRowStatus.setStatus("mandatory")
_ExampleDashedIndicesComponentName_Type = DisplayString
_ExampleDashedIndicesComponentName_Object = MibTableColumn
exampleDashedIndicesComponentName = _ExampleDashedIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1, 2),
    _ExampleDashedIndicesComponentName_Type()
)
exampleDashedIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDashedIndicesComponentName.setStatus("mandatory")
_ExampleDashedIndicesStorageType_Type = StorageType
_ExampleDashedIndicesStorageType_Object = MibTableColumn
exampleDashedIndicesStorageType = _ExampleDashedIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1, 4),
    _ExampleDashedIndicesStorageType_Type()
)
exampleDashedIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleDashedIndicesStorageType.setStatus("mandatory")


class _ExampleDashedIndicesOneIndex_Type(DashedHexString):
    """Custom type exampleDashedIndicesOneIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedIndicesOneIndex_Type.__name__ = "DashedHexString"
_ExampleDashedIndicesOneIndex_Object = MibTableColumn
exampleDashedIndicesOneIndex = _ExampleDashedIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1, 10),
    _ExampleDashedIndicesOneIndex_Type()
)
exampleDashedIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedIndicesOneIndex.setStatus("mandatory")


class _ExampleDashedIndicesTwoIndex_Type(DashedHexString):
    """Custom type exampleDashedIndicesTwoIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedIndicesTwoIndex_Type.__name__ = "DashedHexString"
_ExampleDashedIndicesTwoIndex_Object = MibTableColumn
exampleDashedIndicesTwoIndex = _ExampleDashedIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1, 11),
    _ExampleDashedIndicesTwoIndex_Type()
)
exampleDashedIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedIndicesTwoIndex.setStatus("mandatory")


class _ExampleDashedIndicesThreeIndex_Type(DashedHexString):
    """Custom type exampleDashedIndicesThreeIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExampleDashedIndicesThreeIndex_Type.__name__ = "DashedHexString"
_ExampleDashedIndicesThreeIndex_Object = MibTableColumn
exampleDashedIndicesThreeIndex = _ExampleDashedIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 1, 1, 12),
    _ExampleDashedIndicesThreeIndex_Type()
)
exampleDashedIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleDashedIndicesThreeIndex.setStatus("mandatory")
_ExampleDashedIndicesProvisionedTable_Object = MibTable
exampleDashedIndicesProvisionedTable = _ExampleDashedIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 10)
)
if mibBuilder.loadTexts:
    exampleDashedIndicesProvisionedTable.setStatus("mandatory")
_ExampleDashedIndicesProvisionedEntry_Object = MibTableRow
exampleDashedIndicesProvisionedEntry = _ExampleDashedIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 10, 1)
)
exampleDashedIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndicesOneIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndicesTwoIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleDashedIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    exampleDashedIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleDashedIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleDashedIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleDashedIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleDashedIndicesProvAttribute_Object = MibTableColumn
exampleDashedIndicesProvAttribute = _ExampleDashedIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 30, 10, 1, 1),
    _ExampleDashedIndicesProvAttribute_Type()
)
exampleDashedIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleDashedIndicesProvAttribute.setStatus("mandatory")
_ExampleRequiredIndices_ObjectIdentity = ObjectIdentity
exampleRequiredIndices = _ExampleRequiredIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31)
)
_ExampleRequiredIndicesRowStatusTable_Object = MibTable
exampleRequiredIndicesRowStatusTable = _ExampleRequiredIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1)
)
if mibBuilder.loadTexts:
    exampleRequiredIndicesRowStatusTable.setStatus("mandatory")
_ExampleRequiredIndicesRowStatusEntry_Object = MibTableRow
exampleRequiredIndicesRowStatusEntry = _ExampleRequiredIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1, 1)
)
exampleRequiredIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleRequiredIndicesDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleRequiredIndicesEnumerationIndex"),
)
if mibBuilder.loadTexts:
    exampleRequiredIndicesRowStatusEntry.setStatus("mandatory")
_ExampleRequiredIndicesRowStatus_Type = RowStatus
_ExampleRequiredIndicesRowStatus_Object = MibTableColumn
exampleRequiredIndicesRowStatus = _ExampleRequiredIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1, 1, 1),
    _ExampleRequiredIndicesRowStatus_Type()
)
exampleRequiredIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleRequiredIndicesRowStatus.setStatus("mandatory")
_ExampleRequiredIndicesComponentName_Type = DisplayString
_ExampleRequiredIndicesComponentName_Object = MibTableColumn
exampleRequiredIndicesComponentName = _ExampleRequiredIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1, 1, 2),
    _ExampleRequiredIndicesComponentName_Type()
)
exampleRequiredIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleRequiredIndicesComponentName.setStatus("mandatory")
_ExampleRequiredIndicesStorageType_Type = StorageType
_ExampleRequiredIndicesStorageType_Object = MibTableColumn
exampleRequiredIndicesStorageType = _ExampleRequiredIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1, 1, 4),
    _ExampleRequiredIndicesStorageType_Type()
)
exampleRequiredIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleRequiredIndicesStorageType.setStatus("mandatory")


class _ExampleRequiredIndicesDecimalIndex_Type(Integer32):
    """Custom type exampleRequiredIndicesDecimalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_ExampleRequiredIndicesDecimalIndex_Type.__name__ = "Integer32"
_ExampleRequiredIndicesDecimalIndex_Object = MibTableColumn
exampleRequiredIndicesDecimalIndex = _ExampleRequiredIndicesDecimalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1, 1, 10),
    _ExampleRequiredIndicesDecimalIndex_Type()
)
exampleRequiredIndicesDecimalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleRequiredIndicesDecimalIndex.setStatus("mandatory")


class _ExampleRequiredIndicesEnumerationIndex_Type(Integer32):
    """Custom type exampleRequiredIndicesEnumerationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )


_ExampleRequiredIndicesEnumerationIndex_Type.__name__ = "Integer32"
_ExampleRequiredIndicesEnumerationIndex_Object = MibTableColumn
exampleRequiredIndicesEnumerationIndex = _ExampleRequiredIndicesEnumerationIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 1, 1, 11),
    _ExampleRequiredIndicesEnumerationIndex_Type()
)
exampleRequiredIndicesEnumerationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleRequiredIndicesEnumerationIndex.setStatus("mandatory")
_ExampleRequiredIndicesProvisionedTable_Object = MibTable
exampleRequiredIndicesProvisionedTable = _ExampleRequiredIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 10)
)
if mibBuilder.loadTexts:
    exampleRequiredIndicesProvisionedTable.setStatus("mandatory")
_ExampleRequiredIndicesProvisionedEntry_Object = MibTableRow
exampleRequiredIndicesProvisionedEntry = _ExampleRequiredIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 10, 1)
)
exampleRequiredIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleRequiredIndicesDecimalIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleRequiredIndicesEnumerationIndex"),
)
if mibBuilder.loadTexts:
    exampleRequiredIndicesProvisionedEntry.setStatus("mandatory")


class _ExampleRequiredIndicesProvAttribute_Type(Unsigned32):
    """Custom type exampleRequiredIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExampleRequiredIndicesProvAttribute_Type.__name__ = "Unsigned32"
_ExampleRequiredIndicesProvAttribute_Object = MibTableColumn
exampleRequiredIndicesProvAttribute = _ExampleRequiredIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 31, 10, 1, 1),
    _ExampleRequiredIndicesProvAttribute_Type()
)
exampleRequiredIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleRequiredIndicesProvAttribute.setStatus("mandatory")
_ExampleNsap_ObjectIdentity = ObjectIdentity
exampleNsap = _ExampleNsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32)
)
_ExampleNsapRowStatusTable_Object = MibTable
exampleNsapRowStatusTable = _ExampleNsapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1)
)
if mibBuilder.loadTexts:
    exampleNsapRowStatusTable.setStatus("mandatory")
_ExampleNsapRowStatusEntry_Object = MibTableRow
exampleNsapRowStatusEntry = _ExampleNsapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1, 1)
)
exampleNsapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleNsapIndex"),
)
if mibBuilder.loadTexts:
    exampleNsapRowStatusEntry.setStatus("mandatory")
_ExampleNsapRowStatus_Type = RowStatus
_ExampleNsapRowStatus_Object = MibTableColumn
exampleNsapRowStatus = _ExampleNsapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1, 1, 1),
    _ExampleNsapRowStatus_Type()
)
exampleNsapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleNsapRowStatus.setStatus("mandatory")
_ExampleNsapComponentName_Type = DisplayString
_ExampleNsapComponentName_Object = MibTableColumn
exampleNsapComponentName = _ExampleNsapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1, 1, 2),
    _ExampleNsapComponentName_Type()
)
exampleNsapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleNsapComponentName.setStatus("mandatory")
_ExampleNsapStorageType_Type = StorageType
_ExampleNsapStorageType_Object = MibTableColumn
exampleNsapStorageType = _ExampleNsapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1, 1, 4),
    _ExampleNsapStorageType_Type()
)
exampleNsapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exampleNsapStorageType.setStatus("mandatory")


class _ExampleNsapIndex_Type(AsciiStringIndex):
    """Custom type exampleNsapIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_ExampleNsapIndex_Type.__name__ = "AsciiStringIndex"
_ExampleNsapIndex_Object = MibTableColumn
exampleNsapIndex = _ExampleNsapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1, 1, 10),
    _ExampleNsapIndex_Type()
)
exampleNsapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleNsapIndex.setStatus("mandatory")
_ExampleNsapAtmAddrTable_Object = MibTable
exampleNsapAtmAddrTable = _ExampleNsapAtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 102)
)
if mibBuilder.loadTexts:
    exampleNsapAtmAddrTable.setStatus("mandatory")
_ExampleNsapAtmAddrEntry_Object = MibTableRow
exampleNsapAtmAddrEntry = _ExampleNsapAtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 102, 1)
)
exampleNsapAtmAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleNsapIndex"),
)
if mibBuilder.loadTexts:
    exampleNsapAtmAddrEntry.setStatus("mandatory")


class _ExampleNsapNsapNativeAddress_Type(AsciiString):
    """Custom type exampleNsapNsapNativeAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_ExampleNsapNsapNativeAddress_Type.__name__ = "AsciiString"
_ExampleNsapNsapNativeAddress_Object = MibTableColumn
exampleNsapNsapNativeAddress = _ExampleNsapNsapNativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 102, 1, 1246),
    _ExampleNsapNsapNativeAddress_Type()
)
exampleNsapNsapNativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleNsapNsapNativeAddress.setStatus("mandatory")
_ExampleNsapNativeTable_Object = MibTable
exampleNsapNativeTable = _ExampleNsapNativeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1247)
)
if mibBuilder.loadTexts:
    exampleNsapNativeTable.setStatus("mandatory")
_ExampleNsapNativeEntry_Object = MibTableRow
exampleNsapNativeEntry = _ExampleNsapNativeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1247, 1)
)
exampleNsapNativeEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleNsapIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleNsapNativeIndex"),
)
if mibBuilder.loadTexts:
    exampleNsapNativeEntry.setStatus("mandatory")


class _ExampleNsapNativeIndex_Type(Integer32):
    """Custom type exampleNsapNativeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ExampleNsapNativeIndex_Type.__name__ = "Integer32"
_ExampleNsapNativeIndex_Object = MibTableColumn
exampleNsapNativeIndex = _ExampleNsapNativeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1247, 1, 1),
    _ExampleNsapNativeIndex_Type()
)
exampleNsapNativeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exampleNsapNativeIndex.setStatus("mandatory")


class _ExampleNsapNativeValue_Type(AsciiString):
    """Custom type exampleNsapNativeValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_ExampleNsapNativeValue_Type.__name__ = "AsciiString"
_ExampleNsapNativeValue_Object = MibTableColumn
exampleNsapNativeValue = _ExampleNsapNativeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 32, 1247, 1, 2),
    _ExampleNsapNativeValue_Type()
)
exampleNsapNativeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleNsapNativeValue.setStatus("mandatory")
_ExampleOperationalTable_Object = MibTable
exampleOperationalTable = _ExampleOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 100)
)
if mibBuilder.loadTexts:
    exampleOperationalTable.setStatus("mandatory")
_ExampleOperationalEntry_Object = MibTableRow
exampleOperationalEntry = _ExampleOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 100, 1)
)
exampleOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
)
if mibBuilder.loadTexts:
    exampleOperationalEntry.setStatus("mandatory")
_ExampleOperMyComponentName_Type = RowPointer
_ExampleOperMyComponentName_Object = MibTableColumn
exampleOperMyComponentName = _ExampleOperMyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 100, 1, 1),
    _ExampleOperMyComponentName_Type()
)
exampleOperMyComponentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOperMyComponentName.setStatus("mandatory")
_ExampleProvisionalTable_Object = MibTable
exampleProvisionalTable = _ExampleProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 101)
)
if mibBuilder.loadTexts:
    exampleProvisionalTable.setStatus("mandatory")
_ExampleProvisionalEntry_Object = MibTableRow
exampleProvisionalEntry = _ExampleProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 101, 1)
)
exampleProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
)
if mibBuilder.loadTexts:
    exampleProvisionalEntry.setStatus("mandatory")
_ExampleProvMyComponentName_Type = RowPointer
_ExampleProvMyComponentName_Object = MibTableColumn
exampleProvMyComponentName = _ExampleProvMyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 101, 1, 1),
    _ExampleProvMyComponentName_Type()
)
exampleProvMyComponentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleProvMyComponentName.setStatus("mandatory")
_ExampleOperDecimalSubCreatedTable_Object = MibTable
exampleOperDecimalSubCreatedTable = _ExampleOperDecimalSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1002)
)
if mibBuilder.loadTexts:
    exampleOperDecimalSubCreatedTable.setStatus("mandatory")
_ExampleOperDecimalSubCreatedEntry_Object = MibTableRow
exampleOperDecimalSubCreatedEntry = _ExampleOperDecimalSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1002, 1)
)
exampleOperDecimalSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOperDecimalSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleOperDecimalSubCreatedEntry.setStatus("mandatory")
_ExampleOperDecimalSubCreatedValue_Type = RowPointer
_ExampleOperDecimalSubCreatedValue_Object = MibTableColumn
exampleOperDecimalSubCreatedValue = _ExampleOperDecimalSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1002, 1, 1),
    _ExampleOperDecimalSubCreatedValue_Type()
)
exampleOperDecimalSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOperDecimalSubCreatedValue.setStatus("mandatory")
_ExampleOperDecimalSubCreatedRowStatus_Type = RowStatus
_ExampleOperDecimalSubCreatedRowStatus_Object = MibTableColumn
exampleOperDecimalSubCreatedRowStatus = _ExampleOperDecimalSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1002, 1, 2),
    _ExampleOperDecimalSubCreatedRowStatus_Type()
)
exampleOperDecimalSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleOperDecimalSubCreatedRowStatus.setStatus("mandatory")
_ExampleOperFixedPtSubcomponentsCreatedTable_Object = MibTable
exampleOperFixedPtSubcomponentsCreatedTable = _ExampleOperFixedPtSubcomponentsCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1003)
)
if mibBuilder.loadTexts:
    exampleOperFixedPtSubcomponentsCreatedTable.setStatus("mandatory")
_ExampleOperFixedPtSubcomponentsCreatedEntry_Object = MibTableRow
exampleOperFixedPtSubcomponentsCreatedEntry = _ExampleOperFixedPtSubcomponentsCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1003, 1)
)
exampleOperFixedPtSubcomponentsCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOperFixedPtSubcomponentsCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleOperFixedPtSubcomponentsCreatedEntry.setStatus("mandatory")
_ExampleOperFixedPtSubcomponentsCreatedValue_Type = RowPointer
_ExampleOperFixedPtSubcomponentsCreatedValue_Object = MibTableColumn
exampleOperFixedPtSubcomponentsCreatedValue = _ExampleOperFixedPtSubcomponentsCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1003, 1, 1),
    _ExampleOperFixedPtSubcomponentsCreatedValue_Type()
)
exampleOperFixedPtSubcomponentsCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOperFixedPtSubcomponentsCreatedValue.setStatus("mandatory")
_ExampleOperFixedPtSubcomponentsCreatedRowStatus_Type = RowStatus
_ExampleOperFixedPtSubcomponentsCreatedRowStatus_Object = MibTableColumn
exampleOperFixedPtSubcomponentsCreatedRowStatus = _ExampleOperFixedPtSubcomponentsCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1003, 1, 2),
    _ExampleOperFixedPtSubcomponentsCreatedRowStatus_Type()
)
exampleOperFixedPtSubcomponentsCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleOperFixedPtSubcomponentsCreatedRowStatus.setStatus("mandatory")
_ExampleOperStringSubCreatedTable_Object = MibTable
exampleOperStringSubCreatedTable = _ExampleOperStringSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1004)
)
if mibBuilder.loadTexts:
    exampleOperStringSubCreatedTable.setStatus("mandatory")
_ExampleOperStringSubCreatedEntry_Object = MibTableRow
exampleOperStringSubCreatedEntry = _ExampleOperStringSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1004, 1)
)
exampleOperStringSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOperStringSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleOperStringSubCreatedEntry.setStatus("mandatory")
_ExampleOperStringSubCreatedValue_Type = RowPointer
_ExampleOperStringSubCreatedValue_Object = MibTableColumn
exampleOperStringSubCreatedValue = _ExampleOperStringSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1004, 1, 1),
    _ExampleOperStringSubCreatedValue_Type()
)
exampleOperStringSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOperStringSubCreatedValue.setStatus("mandatory")
_ExampleOperStringSubCreatedRowStatus_Type = RowStatus
_ExampleOperStringSubCreatedRowStatus_Object = MibTableColumn
exampleOperStringSubCreatedRowStatus = _ExampleOperStringSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1004, 1, 2),
    _ExampleOperStringSubCreatedRowStatus_Type()
)
exampleOperStringSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleOperStringSubCreatedRowStatus.setStatus("mandatory")
_ExampleOperEnumSubCreatedTable_Object = MibTable
exampleOperEnumSubCreatedTable = _ExampleOperEnumSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1005)
)
if mibBuilder.loadTexts:
    exampleOperEnumSubCreatedTable.setStatus("mandatory")
_ExampleOperEnumSubCreatedEntry_Object = MibTableRow
exampleOperEnumSubCreatedEntry = _ExampleOperEnumSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1005, 1)
)
exampleOperEnumSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOperEnumSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleOperEnumSubCreatedEntry.setStatus("mandatory")
_ExampleOperEnumSubCreatedValue_Type = RowPointer
_ExampleOperEnumSubCreatedValue_Object = MibTableColumn
exampleOperEnumSubCreatedValue = _ExampleOperEnumSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1005, 1, 1),
    _ExampleOperEnumSubCreatedValue_Type()
)
exampleOperEnumSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOperEnumSubCreatedValue.setStatus("mandatory")
_ExampleOperEnumSubCreatedRowStatus_Type = RowStatus
_ExampleOperEnumSubCreatedRowStatus_Object = MibTableColumn
exampleOperEnumSubCreatedRowStatus = _ExampleOperEnumSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1005, 1, 2),
    _ExampleOperEnumSubCreatedRowStatus_Type()
)
exampleOperEnumSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleOperEnumSubCreatedRowStatus.setStatus("mandatory")
_ExampleOperSignedSubCreatedTable_Object = MibTable
exampleOperSignedSubCreatedTable = _ExampleOperSignedSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1006)
)
if mibBuilder.loadTexts:
    exampleOperSignedSubCreatedTable.setStatus("mandatory")
_ExampleOperSignedSubCreatedEntry_Object = MibTableRow
exampleOperSignedSubCreatedEntry = _ExampleOperSignedSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1006, 1)
)
exampleOperSignedSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleOperSignedSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleOperSignedSubCreatedEntry.setStatus("mandatory")
_ExampleOperSignedSubCreatedValue_Type = RowPointer
_ExampleOperSignedSubCreatedValue_Object = MibTableColumn
exampleOperSignedSubCreatedValue = _ExampleOperSignedSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1006, 1, 1),
    _ExampleOperSignedSubCreatedValue_Type()
)
exampleOperSignedSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleOperSignedSubCreatedValue.setStatus("mandatory")
_ExampleOperSignedSubCreatedRowStatus_Type = RowStatus
_ExampleOperSignedSubCreatedRowStatus_Object = MibTableColumn
exampleOperSignedSubCreatedRowStatus = _ExampleOperSignedSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1006, 1, 2),
    _ExampleOperSignedSubCreatedRowStatus_Type()
)
exampleOperSignedSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleOperSignedSubCreatedRowStatus.setStatus("mandatory")
_ExampleProvDecimalSubCreatedTable_Object = MibTable
exampleProvDecimalSubCreatedTable = _ExampleProvDecimalSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1007)
)
if mibBuilder.loadTexts:
    exampleProvDecimalSubCreatedTable.setStatus("mandatory")
_ExampleProvDecimalSubCreatedEntry_Object = MibTableRow
exampleProvDecimalSubCreatedEntry = _ExampleProvDecimalSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1007, 1)
)
exampleProvDecimalSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleProvDecimalSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleProvDecimalSubCreatedEntry.setStatus("mandatory")
_ExampleProvDecimalSubCreatedValue_Type = Link
_ExampleProvDecimalSubCreatedValue_Object = MibTableColumn
exampleProvDecimalSubCreatedValue = _ExampleProvDecimalSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1007, 1, 1),
    _ExampleProvDecimalSubCreatedValue_Type()
)
exampleProvDecimalSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleProvDecimalSubCreatedValue.setStatus("mandatory")
_ExampleProvDecimalSubCreatedRowStatus_Type = RowStatus
_ExampleProvDecimalSubCreatedRowStatus_Object = MibTableColumn
exampleProvDecimalSubCreatedRowStatus = _ExampleProvDecimalSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1007, 1, 2),
    _ExampleProvDecimalSubCreatedRowStatus_Type()
)
exampleProvDecimalSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleProvDecimalSubCreatedRowStatus.setStatus("mandatory")
_ExampleProvFixedPtSubCreatedTable_Object = MibTable
exampleProvFixedPtSubCreatedTable = _ExampleProvFixedPtSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1008)
)
if mibBuilder.loadTexts:
    exampleProvFixedPtSubCreatedTable.setStatus("mandatory")
_ExampleProvFixedPtSubCreatedEntry_Object = MibTableRow
exampleProvFixedPtSubCreatedEntry = _ExampleProvFixedPtSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1008, 1)
)
exampleProvFixedPtSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleProvFixedPtSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleProvFixedPtSubCreatedEntry.setStatus("mandatory")
_ExampleProvFixedPtSubCreatedValue_Type = Link
_ExampleProvFixedPtSubCreatedValue_Object = MibTableColumn
exampleProvFixedPtSubCreatedValue = _ExampleProvFixedPtSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1008, 1, 1),
    _ExampleProvFixedPtSubCreatedValue_Type()
)
exampleProvFixedPtSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleProvFixedPtSubCreatedValue.setStatus("mandatory")
_ExampleProvFixedPtSubCreatedRowStatus_Type = RowStatus
_ExampleProvFixedPtSubCreatedRowStatus_Object = MibTableColumn
exampleProvFixedPtSubCreatedRowStatus = _ExampleProvFixedPtSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1008, 1, 2),
    _ExampleProvFixedPtSubCreatedRowStatus_Type()
)
exampleProvFixedPtSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleProvFixedPtSubCreatedRowStatus.setStatus("mandatory")
_ExampleProvSignedSubCreatedTable_Object = MibTable
exampleProvSignedSubCreatedTable = _ExampleProvSignedSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1009)
)
if mibBuilder.loadTexts:
    exampleProvSignedSubCreatedTable.setStatus("mandatory")
_ExampleProvSignedSubCreatedEntry_Object = MibTableRow
exampleProvSignedSubCreatedEntry = _ExampleProvSignedSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1009, 1)
)
exampleProvSignedSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleProvSignedSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleProvSignedSubCreatedEntry.setStatus("mandatory")
_ExampleProvSignedSubCreatedValue_Type = Link
_ExampleProvSignedSubCreatedValue_Object = MibTableColumn
exampleProvSignedSubCreatedValue = _ExampleProvSignedSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1009, 1, 1),
    _ExampleProvSignedSubCreatedValue_Type()
)
exampleProvSignedSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleProvSignedSubCreatedValue.setStatus("mandatory")
_ExampleProvSignedSubCreatedRowStatus_Type = RowStatus
_ExampleProvSignedSubCreatedRowStatus_Object = MibTableColumn
exampleProvSignedSubCreatedRowStatus = _ExampleProvSignedSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1009, 1, 2),
    _ExampleProvSignedSubCreatedRowStatus_Type()
)
exampleProvSignedSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleProvSignedSubCreatedRowStatus.setStatus("mandatory")
_ExampleProvStringSubCreatedTable_Object = MibTable
exampleProvStringSubCreatedTable = _ExampleProvStringSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1010)
)
if mibBuilder.loadTexts:
    exampleProvStringSubCreatedTable.setStatus("mandatory")
_ExampleProvStringSubCreatedEntry_Object = MibTableRow
exampleProvStringSubCreatedEntry = _ExampleProvStringSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1010, 1)
)
exampleProvStringSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleProvStringSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleProvStringSubCreatedEntry.setStatus("mandatory")
_ExampleProvStringSubCreatedValue_Type = Link
_ExampleProvStringSubCreatedValue_Object = MibTableColumn
exampleProvStringSubCreatedValue = _ExampleProvStringSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1010, 1, 1),
    _ExampleProvStringSubCreatedValue_Type()
)
exampleProvStringSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleProvStringSubCreatedValue.setStatus("mandatory")
_ExampleProvStringSubCreatedRowStatus_Type = RowStatus
_ExampleProvStringSubCreatedRowStatus_Object = MibTableColumn
exampleProvStringSubCreatedRowStatus = _ExampleProvStringSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1010, 1, 2),
    _ExampleProvStringSubCreatedRowStatus_Type()
)
exampleProvStringSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleProvStringSubCreatedRowStatus.setStatus("mandatory")
_ExampleProvEnumSubCreatedTable_Object = MibTable
exampleProvEnumSubCreatedTable = _ExampleProvEnumSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1011)
)
if mibBuilder.loadTexts:
    exampleProvEnumSubCreatedTable.setStatus("mandatory")
_ExampleProvEnumSubCreatedEntry_Object = MibTableRow
exampleProvEnumSubCreatedEntry = _ExampleProvEnumSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1011, 1)
)
exampleProvEnumSubCreatedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "exampleProvEnumSubCreatedValue"),
)
if mibBuilder.loadTexts:
    exampleProvEnumSubCreatedEntry.setStatus("mandatory")
_ExampleProvEnumSubCreatedValue_Type = Link
_ExampleProvEnumSubCreatedValue_Object = MibTableColumn
exampleProvEnumSubCreatedValue = _ExampleProvEnumSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1011, 1, 1),
    _ExampleProvEnumSubCreatedValue_Type()
)
exampleProvEnumSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exampleProvEnumSubCreatedValue.setStatus("mandatory")
_ExampleProvEnumSubCreatedRowStatus_Type = RowStatus
_ExampleProvEnumSubCreatedRowStatus_Object = MibTableColumn
exampleProvEnumSubCreatedRowStatus = _ExampleProvEnumSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5000, 1011, 1, 2),
    _ExampleProvEnumSubCreatedRowStatus_Type()
)
exampleProvEnumSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    exampleProvEnumSubCreatedRowStatus.setStatus("mandatory")
_Fri_ObjectIdentity = ObjectIdentity
fri = _Fri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001)
)
_FriRowStatusTable_Object = MibTable
friRowStatusTable = _FriRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1)
)
if mibBuilder.loadTexts:
    friRowStatusTable.setStatus("mandatory")
_FriRowStatusEntry_Object = MibTableRow
friRowStatusEntry = _FriRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1, 1)
)
friRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
)
if mibBuilder.loadTexts:
    friRowStatusEntry.setStatus("mandatory")
_FriRowStatus_Type = RowStatus
_FriRowStatus_Object = MibTableColumn
friRowStatus = _FriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1, 1, 1),
    _FriRowStatus_Type()
)
friRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friRowStatus.setStatus("mandatory")
_FriComponentName_Type = DisplayString
_FriComponentName_Object = MibTableColumn
friComponentName = _FriComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1, 1, 2),
    _FriComponentName_Type()
)
friComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friComponentName.setStatus("mandatory")
_FriStorageType_Type = StorageType
_FriStorageType_Object = MibTableColumn
friStorageType = _FriStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1, 1, 4),
    _FriStorageType_Type()
)
friStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friStorageType.setStatus("mandatory")


class _FriIndex_Type(Integer32):
    """Custom type friIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FriIndex_Type.__name__ = "Integer32"
_FriIndex_Object = MibTableColumn
friIndex = _FriIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1, 1, 10),
    _FriIndex_Type()
)
friIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friIndex.setStatus("mandatory")
_FriDna_ObjectIdentity = ObjectIdentity
friDna = _FriDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4)
)
_FriDnaRowStatusTable_Object = MibTable
friDnaRowStatusTable = _FriDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 1)
)
if mibBuilder.loadTexts:
    friDnaRowStatusTable.setStatus("mandatory")
_FriDnaRowStatusEntry_Object = MibTableRow
friDnaRowStatusEntry = _FriDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 1, 1)
)
friDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDnaIndex"),
)
if mibBuilder.loadTexts:
    friDnaRowStatusEntry.setStatus("mandatory")
_FriDnaRowStatus_Type = RowStatus
_FriDnaRowStatus_Object = MibTableColumn
friDnaRowStatus = _FriDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 1, 1, 1),
    _FriDnaRowStatus_Type()
)
friDnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDnaRowStatus.setStatus("mandatory")
_FriDnaComponentName_Type = DisplayString
_FriDnaComponentName_Object = MibTableColumn
friDnaComponentName = _FriDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 1, 1, 2),
    _FriDnaComponentName_Type()
)
friDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDnaComponentName.setStatus("mandatory")
_FriDnaStorageType_Type = StorageType
_FriDnaStorageType_Object = MibTableColumn
friDnaStorageType = _FriDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 1, 1, 4),
    _FriDnaStorageType_Type()
)
friDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDnaStorageType.setStatus("mandatory")


class _FriDnaIndex_Type(Integer32):
    """Custom type friDnaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FriDnaIndex_Type.__name__ = "Integer32"
_FriDnaIndex_Object = MibTableColumn
friDnaIndex = _FriDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 1, 1, 10),
    _FriDnaIndex_Type()
)
friDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDnaIndex.setStatus("mandatory")
_FriDnaOperationalTable_Object = MibTable
friDnaOperationalTable = _FriDnaOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 10)
)
if mibBuilder.loadTexts:
    friDnaOperationalTable.setStatus("mandatory")
_FriDnaOperationalEntry_Object = MibTableRow
friDnaOperationalEntry = _FriDnaOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 10, 1)
)
friDnaOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDnaIndex"),
)
if mibBuilder.loadTexts:
    friDnaOperationalEntry.setStatus("mandatory")


class _FriDnaAttribute_Type(Unsigned32):
    """Custom type friDnaAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FriDnaAttribute_Type.__name__ = "Unsigned32"
_FriDnaAttribute_Object = MibTableColumn
friDnaAttribute = _FriDnaAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 10, 1, 1),
    _FriDnaAttribute_Type()
)
friDnaAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDnaAttribute.setStatus("mandatory")
_FriDnaProvisionalTable_Object = MibTable
friDnaProvisionalTable = _FriDnaProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 11)
)
if mibBuilder.loadTexts:
    friDnaProvisionalTable.setStatus("mandatory")
_FriDnaProvisionalEntry_Object = MibTableRow
friDnaProvisionalEntry = _FriDnaProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 11, 1)
)
friDnaProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDnaIndex"),
)
if mibBuilder.loadTexts:
    friDnaProvisionalEntry.setStatus("mandatory")


class _FriDnaTypeOfAddress_Type(Integer32):
    """Custom type friDnaTypeOfAddress based on Integer32"""
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
        *(("international", 1),
          ("national", 2),
          ("networkDepend", 0))
    )


_FriDnaTypeOfAddress_Type.__name__ = "Integer32"
_FriDnaTypeOfAddress_Object = MibTableColumn
friDnaTypeOfAddress = _FriDnaTypeOfAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 11, 1, 1),
    _FriDnaTypeOfAddress_Type()
)
friDnaTypeOfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDnaTypeOfAddress.setStatus("mandatory")


class _FriDnaNumberPlanIndicator_Type(Integer32):
    """Custom type friDnaNumberPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_FriDnaNumberPlanIndicator_Type.__name__ = "Integer32"
_FriDnaNumberPlanIndicator_Object = MibTableColumn
friDnaNumberPlanIndicator = _FriDnaNumberPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 11, 1, 2),
    _FriDnaNumberPlanIndicator_Type()
)
friDnaNumberPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDnaNumberPlanIndicator.setStatus("mandatory")


class _FriDnaDataNetworkAddress_Type(DigitString):
    """Custom type friDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FriDnaDataNetworkAddress_Type.__name__ = "DigitString"
_FriDnaDataNetworkAddress_Object = MibTableColumn
friDnaDataNetworkAddress = _FriDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 4, 11, 1, 3),
    _FriDnaDataNetworkAddress_Type()
)
friDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDnaDataNetworkAddress.setStatus("mandatory")
_FriDynamic_ObjectIdentity = ObjectIdentity
friDynamic = _FriDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7)
)
_FriDynamicRowStatusTable_Object = MibTable
friDynamicRowStatusTable = _FriDynamicRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 1)
)
if mibBuilder.loadTexts:
    friDynamicRowStatusTable.setStatus("mandatory")
_FriDynamicRowStatusEntry_Object = MibTableRow
friDynamicRowStatusEntry = _FriDynamicRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 1, 1)
)
friDynamicRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynamicIndex"),
)
if mibBuilder.loadTexts:
    friDynamicRowStatusEntry.setStatus("mandatory")
_FriDynamicRowStatus_Type = RowStatus
_FriDynamicRowStatus_Object = MibTableColumn
friDynamicRowStatus = _FriDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 1, 1, 1),
    _FriDynamicRowStatus_Type()
)
friDynamicRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynamicRowStatus.setStatus("mandatory")
_FriDynamicComponentName_Type = DisplayString
_FriDynamicComponentName_Object = MibTableColumn
friDynamicComponentName = _FriDynamicComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 1, 1, 2),
    _FriDynamicComponentName_Type()
)
friDynamicComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynamicComponentName.setStatus("mandatory")
_FriDynamicStorageType_Type = StorageType
_FriDynamicStorageType_Object = MibTableColumn
friDynamicStorageType = _FriDynamicStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 1, 1, 4),
    _FriDynamicStorageType_Type()
)
friDynamicStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynamicStorageType.setStatus("mandatory")


class _FriDynamicIndex_Type(Integer32):
    """Custom type friDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FriDynamicIndex_Type.__name__ = "Integer32"
_FriDynamicIndex_Object = MibTableColumn
friDynamicIndex = _FriDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 1, 1, 10),
    _FriDynamicIndex_Type()
)
friDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDynamicIndex.setStatus("mandatory")
_FriDynamicOperationalTable_Object = MibTable
friDynamicOperationalTable = _FriDynamicOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 10)
)
if mibBuilder.loadTexts:
    friDynamicOperationalTable.setStatus("mandatory")
_FriDynamicOperationalEntry_Object = MibTableRow
friDynamicOperationalEntry = _FriDynamicOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 10, 1)
)
friDynamicOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynamicIndex"),
)
if mibBuilder.loadTexts:
    friDynamicOperationalEntry.setStatus("mandatory")


class _FriDynamicAttribute_Type(Unsigned32):
    """Custom type friDynamicAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynamicAttribute_Type.__name__ = "Unsigned32"
_FriDynamicAttribute_Object = MibTableColumn
friDynamicAttribute = _FriDynamicAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 7, 10, 1, 1),
    _FriDynamicAttribute_Type()
)
friDynamicAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynamicAttribute.setStatus("mandatory")
_FriDynOp_ObjectIdentity = ObjectIdentity
friDynOp = _FriDynOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8)
)
_FriDynOpRowStatusTable_Object = MibTable
friDynOpRowStatusTable = _FriDynOpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 1)
)
if mibBuilder.loadTexts:
    friDynOpRowStatusTable.setStatus("mandatory")
_FriDynOpRowStatusEntry_Object = MibTableRow
friDynOpRowStatusEntry = _FriDynOpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 1, 1)
)
friDynOpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
)
if mibBuilder.loadTexts:
    friDynOpRowStatusEntry.setStatus("mandatory")
_FriDynOpRowStatus_Type = RowStatus
_FriDynOpRowStatus_Object = MibTableColumn
friDynOpRowStatus = _FriDynOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 1, 1, 1),
    _FriDynOpRowStatus_Type()
)
friDynOpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpRowStatus.setStatus("mandatory")
_FriDynOpComponentName_Type = DisplayString
_FriDynOpComponentName_Object = MibTableColumn
friDynOpComponentName = _FriDynOpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 1, 1, 2),
    _FriDynOpComponentName_Type()
)
friDynOpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpComponentName.setStatus("mandatory")
_FriDynOpStorageType_Type = StorageType
_FriDynOpStorageType_Object = MibTableColumn
friDynOpStorageType = _FriDynOpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 1, 1, 4),
    _FriDynOpStorageType_Type()
)
friDynOpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpStorageType.setStatus("mandatory")


class _FriDynOpIndex_Type(Integer32):
    """Custom type friDynOpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FriDynOpIndex_Type.__name__ = "Integer32"
_FriDynOpIndex_Object = MibTableColumn
friDynOpIndex = _FriDynOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 1, 1, 10),
    _FriDynOpIndex_Type()
)
friDynOpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDynOpIndex.setStatus("mandatory")
_FriDynOpInitial_ObjectIdentity = ObjectIdentity
friDynOpInitial = _FriDynOpInitial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2)
)
_FriDynOpInitialRowStatusTable_Object = MibTable
friDynOpInitialRowStatusTable = _FriDynOpInitialRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 1)
)
if mibBuilder.loadTexts:
    friDynOpInitialRowStatusTable.setStatus("mandatory")
_FriDynOpInitialRowStatusEntry_Object = MibTableRow
friDynOpInitialRowStatusEntry = _FriDynOpInitialRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 1, 1)
)
friDynOpInitialRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpInitialIndex"),
)
if mibBuilder.loadTexts:
    friDynOpInitialRowStatusEntry.setStatus("mandatory")
_FriDynOpInitialRowStatus_Type = RowStatus
_FriDynOpInitialRowStatus_Object = MibTableColumn
friDynOpInitialRowStatus = _FriDynOpInitialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 1, 1, 1),
    _FriDynOpInitialRowStatus_Type()
)
friDynOpInitialRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpInitialRowStatus.setStatus("mandatory")
_FriDynOpInitialComponentName_Type = DisplayString
_FriDynOpInitialComponentName_Object = MibTableColumn
friDynOpInitialComponentName = _FriDynOpInitialComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 1, 1, 2),
    _FriDynOpInitialComponentName_Type()
)
friDynOpInitialComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpInitialComponentName.setStatus("mandatory")
_FriDynOpInitialStorageType_Type = StorageType
_FriDynOpInitialStorageType_Object = MibTableColumn
friDynOpInitialStorageType = _FriDynOpInitialStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 1, 1, 4),
    _FriDynOpInitialStorageType_Type()
)
friDynOpInitialStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpInitialStorageType.setStatus("mandatory")
_FriDynOpInitialIndex_Type = NonReplicated
_FriDynOpInitialIndex_Object = MibTableColumn
friDynOpInitialIndex = _FriDynOpInitialIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 1, 1, 10),
    _FriDynOpInitialIndex_Type()
)
friDynOpInitialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDynOpInitialIndex.setStatus("mandatory")
_FriDynOpInitialOperationalTable_Object = MibTable
friDynOpInitialOperationalTable = _FriDynOpInitialOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 10)
)
if mibBuilder.loadTexts:
    friDynOpInitialOperationalTable.setStatus("mandatory")
_FriDynOpInitialOperationalEntry_Object = MibTableRow
friDynOpInitialOperationalEntry = _FriDynOpInitialOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 10, 1)
)
friDynOpInitialOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpInitialIndex"),
)
if mibBuilder.loadTexts:
    friDynOpInitialOperationalEntry.setStatus("mandatory")


class _FriDynOpInitialAttribute_Type(Unsigned32):
    """Custom type friDynOpInitialAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpInitialAttribute_Type.__name__ = "Unsigned32"
_FriDynOpInitialAttribute_Object = MibTableColumn
friDynOpInitialAttribute = _FriDynOpInitialAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 10, 1, 1),
    _FriDynOpInitialAttribute_Type()
)
friDynOpInitialAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpInitialAttribute.setStatus("mandatory")
_FriDynOpInitialProvisionedTable_Object = MibTable
friDynOpInitialProvisionedTable = _FriDynOpInitialProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 11)
)
if mibBuilder.loadTexts:
    friDynOpInitialProvisionedTable.setStatus("mandatory")
_FriDynOpInitialProvisionedEntry_Object = MibTableRow
friDynOpInitialProvisionedEntry = _FriDynOpInitialProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 11, 1)
)
friDynOpInitialProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpInitialIndex"),
)
if mibBuilder.loadTexts:
    friDynOpInitialProvisionedEntry.setStatus("mandatory")


class _FriDynOpInitialProvAttribute_Type(Unsigned32):
    """Custom type friDynOpInitialProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpInitialProvAttribute_Type.__name__ = "Unsigned32"
_FriDynOpInitialProvAttribute_Object = MibTableColumn
friDynOpInitialProvAttribute = _FriDynOpInitialProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 2, 11, 1, 1),
    _FriDynOpInitialProvAttribute_Type()
)
friDynOpInitialProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpInitialProvAttribute.setStatus("mandatory")
_FriDynOpOptional_ObjectIdentity = ObjectIdentity
friDynOpOptional = _FriDynOpOptional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3)
)
_FriDynOpOptionalRowStatusTable_Object = MibTable
friDynOpOptionalRowStatusTable = _FriDynOpOptionalRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 1)
)
if mibBuilder.loadTexts:
    friDynOpOptionalRowStatusTable.setStatus("mandatory")
_FriDynOpOptionalRowStatusEntry_Object = MibTableRow
friDynOpOptionalRowStatusEntry = _FriDynOpOptionalRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 1, 1)
)
friDynOpOptionalRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpOptionalIndex"),
)
if mibBuilder.loadTexts:
    friDynOpOptionalRowStatusEntry.setStatus("mandatory")
_FriDynOpOptionalRowStatus_Type = RowStatus
_FriDynOpOptionalRowStatus_Object = MibTableColumn
friDynOpOptionalRowStatus = _FriDynOpOptionalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 1, 1, 1),
    _FriDynOpOptionalRowStatus_Type()
)
friDynOpOptionalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpOptionalRowStatus.setStatus("mandatory")
_FriDynOpOptionalComponentName_Type = DisplayString
_FriDynOpOptionalComponentName_Object = MibTableColumn
friDynOpOptionalComponentName = _FriDynOpOptionalComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 1, 1, 2),
    _FriDynOpOptionalComponentName_Type()
)
friDynOpOptionalComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpOptionalComponentName.setStatus("mandatory")
_FriDynOpOptionalStorageType_Type = StorageType
_FriDynOpOptionalStorageType_Object = MibTableColumn
friDynOpOptionalStorageType = _FriDynOpOptionalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 1, 1, 4),
    _FriDynOpOptionalStorageType_Type()
)
friDynOpOptionalStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpOptionalStorageType.setStatus("mandatory")
_FriDynOpOptionalIndex_Type = NonReplicated
_FriDynOpOptionalIndex_Object = MibTableColumn
friDynOpOptionalIndex = _FriDynOpOptionalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 1, 1, 10),
    _FriDynOpOptionalIndex_Type()
)
friDynOpOptionalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDynOpOptionalIndex.setStatus("mandatory")
_FriDynOpOptionalOperationalTable_Object = MibTable
friDynOpOptionalOperationalTable = _FriDynOpOptionalOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 10)
)
if mibBuilder.loadTexts:
    friDynOpOptionalOperationalTable.setStatus("mandatory")
_FriDynOpOptionalOperationalEntry_Object = MibTableRow
friDynOpOptionalOperationalEntry = _FriDynOpOptionalOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 10, 1)
)
friDynOpOptionalOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpOptionalIndex"),
)
if mibBuilder.loadTexts:
    friDynOpOptionalOperationalEntry.setStatus("mandatory")


class _FriDynOpOptionalAttribute_Type(Unsigned32):
    """Custom type friDynOpOptionalAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpOptionalAttribute_Type.__name__ = "Unsigned32"
_FriDynOpOptionalAttribute_Object = MibTableColumn
friDynOpOptionalAttribute = _FriDynOpOptionalAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 10, 1, 1),
    _FriDynOpOptionalAttribute_Type()
)
friDynOpOptionalAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpOptionalAttribute.setStatus("mandatory")
_FriDynOpOptionalProvisionedTable_Object = MibTable
friDynOpOptionalProvisionedTable = _FriDynOpOptionalProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 11)
)
if mibBuilder.loadTexts:
    friDynOpOptionalProvisionedTable.setStatus("mandatory")
_FriDynOpOptionalProvisionedEntry_Object = MibTableRow
friDynOpOptionalProvisionedEntry = _FriDynOpOptionalProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 11, 1)
)
friDynOpOptionalProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpOptionalIndex"),
)
if mibBuilder.loadTexts:
    friDynOpOptionalProvisionedEntry.setStatus("mandatory")


class _FriDynOpOptionalProvAttribute_Type(Unsigned32):
    """Custom type friDynOpOptionalProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpOptionalProvAttribute_Type.__name__ = "Unsigned32"
_FriDynOpOptionalProvAttribute_Object = MibTableColumn
friDynOpOptionalProvAttribute = _FriDynOpOptionalProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 3, 11, 1, 1),
    _FriDynOpOptionalProvAttribute_Type()
)
friDynOpOptionalProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpOptionalProvAttribute.setStatus("mandatory")
_FriDynOpDynamic_ObjectIdentity = ObjectIdentity
friDynOpDynamic = _FriDynOpDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4)
)
_FriDynOpDynamicRowStatusTable_Object = MibTable
friDynOpDynamicRowStatusTable = _FriDynOpDynamicRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 1)
)
if mibBuilder.loadTexts:
    friDynOpDynamicRowStatusTable.setStatus("mandatory")
_FriDynOpDynamicRowStatusEntry_Object = MibTableRow
friDynOpDynamicRowStatusEntry = _FriDynOpDynamicRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 1, 1)
)
friDynOpDynamicRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpDynamicIndex"),
)
if mibBuilder.loadTexts:
    friDynOpDynamicRowStatusEntry.setStatus("mandatory")
_FriDynOpDynamicRowStatus_Type = RowStatus
_FriDynOpDynamicRowStatus_Object = MibTableColumn
friDynOpDynamicRowStatus = _FriDynOpDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 1, 1, 1),
    _FriDynOpDynamicRowStatus_Type()
)
friDynOpDynamicRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpDynamicRowStatus.setStatus("mandatory")
_FriDynOpDynamicComponentName_Type = DisplayString
_FriDynOpDynamicComponentName_Object = MibTableColumn
friDynOpDynamicComponentName = _FriDynOpDynamicComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 1, 1, 2),
    _FriDynOpDynamicComponentName_Type()
)
friDynOpDynamicComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpDynamicComponentName.setStatus("mandatory")
_FriDynOpDynamicStorageType_Type = StorageType
_FriDynOpDynamicStorageType_Object = MibTableColumn
friDynOpDynamicStorageType = _FriDynOpDynamicStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 1, 1, 4),
    _FriDynOpDynamicStorageType_Type()
)
friDynOpDynamicStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpDynamicStorageType.setStatus("mandatory")
_FriDynOpDynamicIndex_Type = NonReplicated
_FriDynOpDynamicIndex_Object = MibTableColumn
friDynOpDynamicIndex = _FriDynOpDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 1, 1, 10),
    _FriDynOpDynamicIndex_Type()
)
friDynOpDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDynOpDynamicIndex.setStatus("mandatory")
_FriDynOpDynamicOperationalTable_Object = MibTable
friDynOpDynamicOperationalTable = _FriDynOpDynamicOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 10)
)
if mibBuilder.loadTexts:
    friDynOpDynamicOperationalTable.setStatus("mandatory")
_FriDynOpDynamicOperationalEntry_Object = MibTableRow
friDynOpDynamicOperationalEntry = _FriDynOpDynamicOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 10, 1)
)
friDynOpDynamicOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpDynamicIndex"),
)
if mibBuilder.loadTexts:
    friDynOpDynamicOperationalEntry.setStatus("mandatory")


class _FriDynOpDynamicAttribute_Type(Unsigned32):
    """Custom type friDynOpDynamicAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpDynamicAttribute_Type.__name__ = "Unsigned32"
_FriDynOpDynamicAttribute_Object = MibTableColumn
friDynOpDynamicAttribute = _FriDynOpDynamicAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 4, 10, 1, 1),
    _FriDynOpDynamicAttribute_Type()
)
friDynOpDynamicAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpDynamicAttribute.setStatus("mandatory")
_FriDynOpDynOpJr_ObjectIdentity = ObjectIdentity
friDynOpDynOpJr = _FriDynOpDynOpJr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5)
)
_FriDynOpDynOpJrRowStatusTable_Object = MibTable
friDynOpDynOpJrRowStatusTable = _FriDynOpDynOpJrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 1)
)
if mibBuilder.loadTexts:
    friDynOpDynOpJrRowStatusTable.setStatus("mandatory")
_FriDynOpDynOpJrRowStatusEntry_Object = MibTableRow
friDynOpDynOpJrRowStatusEntry = _FriDynOpDynOpJrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 1, 1)
)
friDynOpDynOpJrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpDynOpJrIndex"),
)
if mibBuilder.loadTexts:
    friDynOpDynOpJrRowStatusEntry.setStatus("mandatory")
_FriDynOpDynOpJrRowStatus_Type = RowStatus
_FriDynOpDynOpJrRowStatus_Object = MibTableColumn
friDynOpDynOpJrRowStatus = _FriDynOpDynOpJrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 1, 1, 1),
    _FriDynOpDynOpJrRowStatus_Type()
)
friDynOpDynOpJrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpDynOpJrRowStatus.setStatus("mandatory")
_FriDynOpDynOpJrComponentName_Type = DisplayString
_FriDynOpDynOpJrComponentName_Object = MibTableColumn
friDynOpDynOpJrComponentName = _FriDynOpDynOpJrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 1, 1, 2),
    _FriDynOpDynOpJrComponentName_Type()
)
friDynOpDynOpJrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpDynOpJrComponentName.setStatus("mandatory")
_FriDynOpDynOpJrStorageType_Type = StorageType
_FriDynOpDynOpJrStorageType_Object = MibTableColumn
friDynOpDynOpJrStorageType = _FriDynOpDynOpJrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 1, 1, 4),
    _FriDynOpDynOpJrStorageType_Type()
)
friDynOpDynOpJrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDynOpDynOpJrStorageType.setStatus("mandatory")
_FriDynOpDynOpJrIndex_Type = NonReplicated
_FriDynOpDynOpJrIndex_Object = MibTableColumn
friDynOpDynOpJrIndex = _FriDynOpDynOpJrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 1, 1, 10),
    _FriDynOpDynOpJrIndex_Type()
)
friDynOpDynOpJrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friDynOpDynOpJrIndex.setStatus("mandatory")
_FriDynOpDynOpJrOperationalTable_Object = MibTable
friDynOpDynOpJrOperationalTable = _FriDynOpDynOpJrOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 10)
)
if mibBuilder.loadTexts:
    friDynOpDynOpJrOperationalTable.setStatus("mandatory")
_FriDynOpDynOpJrOperationalEntry_Object = MibTableRow
friDynOpDynOpJrOperationalEntry = _FriDynOpDynOpJrOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 10, 1)
)
friDynOpDynOpJrOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpDynOpJrIndex"),
)
if mibBuilder.loadTexts:
    friDynOpDynOpJrOperationalEntry.setStatus("mandatory")


class _FriDynOpDynOpJrAttribute_Type(Unsigned32):
    """Custom type friDynOpDynOpJrAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpDynOpJrAttribute_Type.__name__ = "Unsigned32"
_FriDynOpDynOpJrAttribute_Object = MibTableColumn
friDynOpDynOpJrAttribute = _FriDynOpDynOpJrAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 5, 10, 1, 1),
    _FriDynOpDynOpJrAttribute_Type()
)
friDynOpDynOpJrAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpDynOpJrAttribute.setStatus("mandatory")
_FriDynOpOperationalTable_Object = MibTable
friDynOpOperationalTable = _FriDynOpOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 10)
)
if mibBuilder.loadTexts:
    friDynOpOperationalTable.setStatus("mandatory")
_FriDynOpOperationalEntry_Object = MibTableRow
friDynOpOperationalEntry = _FriDynOpOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 10, 1)
)
friDynOpOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friDynOpIndex"),
)
if mibBuilder.loadTexts:
    friDynOpOperationalEntry.setStatus("mandatory")


class _FriDynOpAttribute_Type(Unsigned32):
    """Custom type friDynOpAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriDynOpAttribute_Type.__name__ = "Unsigned32"
_FriDynOpAttribute_Object = MibTableColumn
friDynOpAttribute = _FriDynOpAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 8, 10, 1, 1),
    _FriDynOpAttribute_Type()
)
friDynOpAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friDynOpAttribute.setStatus("mandatory")
_FriEvent_ObjectIdentity = ObjectIdentity
friEvent = _FriEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9)
)
_FriEventRowStatusTable_Object = MibTable
friEventRowStatusTable = _FriEventRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9, 1)
)
if mibBuilder.loadTexts:
    friEventRowStatusTable.setStatus("mandatory")
_FriEventRowStatusEntry_Object = MibTableRow
friEventRowStatusEntry = _FriEventRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9, 1, 1)
)
friEventRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friEventIndex"),
)
if mibBuilder.loadTexts:
    friEventRowStatusEntry.setStatus("mandatory")
_FriEventRowStatus_Type = RowStatus
_FriEventRowStatus_Object = MibTableColumn
friEventRowStatus = _FriEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9, 1, 1, 1),
    _FriEventRowStatus_Type()
)
friEventRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friEventRowStatus.setStatus("mandatory")
_FriEventComponentName_Type = DisplayString
_FriEventComponentName_Object = MibTableColumn
friEventComponentName = _FriEventComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9, 1, 1, 2),
    _FriEventComponentName_Type()
)
friEventComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friEventComponentName.setStatus("mandatory")
_FriEventStorageType_Type = StorageType
_FriEventStorageType_Object = MibTableColumn
friEventStorageType = _FriEventStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9, 1, 1, 4),
    _FriEventStorageType_Type()
)
friEventStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friEventStorageType.setStatus("mandatory")
_FriEventIndex_Type = NonReplicated
_FriEventIndex_Object = MibTableColumn
friEventIndex = _FriEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 9, 1, 1, 10),
    _FriEventIndex_Type()
)
friEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friEventIndex.setStatus("mandatory")
_FriRegistered_ObjectIdentity = ObjectIdentity
friRegistered = _FriRegistered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18)
)
_FriRegisteredRowStatusTable_Object = MibTable
friRegisteredRowStatusTable = _FriRegisteredRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 1)
)
if mibBuilder.loadTexts:
    friRegisteredRowStatusTable.setStatus("mandatory")
_FriRegisteredRowStatusEntry_Object = MibTableRow
friRegisteredRowStatusEntry = _FriRegisteredRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 1, 1)
)
friRegisteredRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friRegisteredIndex"),
)
if mibBuilder.loadTexts:
    friRegisteredRowStatusEntry.setStatus("mandatory")
_FriRegisteredRowStatus_Type = RowStatus
_FriRegisteredRowStatus_Object = MibTableColumn
friRegisteredRowStatus = _FriRegisteredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 1, 1, 1),
    _FriRegisteredRowStatus_Type()
)
friRegisteredRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friRegisteredRowStatus.setStatus("mandatory")
_FriRegisteredComponentName_Type = DisplayString
_FriRegisteredComponentName_Object = MibTableColumn
friRegisteredComponentName = _FriRegisteredComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 1, 1, 2),
    _FriRegisteredComponentName_Type()
)
friRegisteredComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friRegisteredComponentName.setStatus("mandatory")
_FriRegisteredStorageType_Type = StorageType
_FriRegisteredStorageType_Object = MibTableColumn
friRegisteredStorageType = _FriRegisteredStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 1, 1, 4),
    _FriRegisteredStorageType_Type()
)
friRegisteredStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friRegisteredStorageType.setStatus("mandatory")


class _FriRegisteredIndex_Type(Integer32):
    """Custom type friRegisteredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FriRegisteredIndex_Type.__name__ = "Integer32"
_FriRegisteredIndex_Object = MibTableColumn
friRegisteredIndex = _FriRegisteredIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 1, 1, 10),
    _FriRegisteredIndex_Type()
)
friRegisteredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friRegisteredIndex.setStatus("mandatory")
_FriRegisteredDataTable_Object = MibTable
friRegisteredDataTable = _FriRegisteredDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 10)
)
if mibBuilder.loadTexts:
    friRegisteredDataTable.setStatus("mandatory")
_FriRegisteredDataEntry_Object = MibTableRow
friRegisteredDataEntry = _FriRegisteredDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 10, 1)
)
friRegisteredDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friRegisteredIndex"),
)
if mibBuilder.loadTexts:
    friRegisteredDataEntry.setStatus("mandatory")


class _FriRegisteredAttribute_Type(Unsigned32):
    """Custom type friRegisteredAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriRegisteredAttribute_Type.__name__ = "Unsigned32"
_FriRegisteredAttribute_Object = MibTableColumn
friRegisteredAttribute = _FriRegisteredAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 18, 10, 1, 1),
    _FriRegisteredAttribute_Type()
)
friRegisteredAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friRegisteredAttribute.setStatus("mandatory")
_FriOperationalTable_Object = MibTable
friOperationalTable = _FriOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100)
)
if mibBuilder.loadTexts:
    friOperationalTable.setStatus("mandatory")
_FriOperationalEntry_Object = MibTableRow
friOperationalEntry = _FriOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1)
)
friOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
)
if mibBuilder.loadTexts:
    friOperationalEntry.setStatus("mandatory")


class _FriOperationalFreeSimpleAscii_Type(AsciiString):
    """Custom type friOperationalFreeSimpleAscii based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalFreeSimpleAscii_Type.__name__ = "AsciiString"
_FriOperationalFreeSimpleAscii_Object = MibTableColumn
friOperationalFreeSimpleAscii = _FriOperationalFreeSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 1),
    _FriOperationalFreeSimpleAscii_Type()
)
friOperationalFreeSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleAscii.setStatus("mandatory")


class _FriOperationalFreeSimpleDashed_Type(DashedHexString):
    """Custom type friOperationalFreeSimpleDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalFreeSimpleDashed_Type.__name__ = "DashedHexString"
_FriOperationalFreeSimpleDashed_Object = MibTableColumn
friOperationalFreeSimpleDashed = _FriOperationalFreeSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 2),
    _FriOperationalFreeSimpleDashed_Type()
)
friOperationalFreeSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleDashed.setStatus("mandatory")


class _FriOperationalFreeSimpleExtended_Type(ExtendedAsciiString):
    """Custom type friOperationalFreeSimpleExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalFreeSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_FriOperationalFreeSimpleExtended_Object = MibTableColumn
friOperationalFreeSimpleExtended = _FriOperationalFreeSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 3),
    _FriOperationalFreeSimpleExtended_Type()
)
friOperationalFreeSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleExtended.setStatus("mandatory")


class _FriOperationalFreeSimpleBcd_Type(DigitString):
    """Custom type friOperationalFreeSimpleBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_FriOperationalFreeSimpleBcd_Type.__name__ = "DigitString"
_FriOperationalFreeSimpleBcd_Object = MibTableColumn
friOperationalFreeSimpleBcd = _FriOperationalFreeSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 4),
    _FriOperationalFreeSimpleBcd_Type()
)
friOperationalFreeSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleBcd.setStatus("mandatory")


class _FriOperationalFreeSimpleSigned_Type(Integer32):
    """Custom type friOperationalFreeSimpleSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 10),
    )


_FriOperationalFreeSimpleSigned_Type.__name__ = "Integer32"
_FriOperationalFreeSimpleSigned_Object = MibTableColumn
friOperationalFreeSimpleSigned = _FriOperationalFreeSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 5),
    _FriOperationalFreeSimpleSigned_Type()
)
friOperationalFreeSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleSigned.setStatus("mandatory")


class _FriOperationalFreeSimpleFixed_Type(FixedPoint1):
    """Custom type friOperationalFreeSimpleFixed based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(55, 66),
    )


_FriOperationalFreeSimpleFixed_Type.__name__ = "FixedPoint1"
_FriOperationalFreeSimpleFixed_Object = MibTableColumn
friOperationalFreeSimpleFixed = _FriOperationalFreeSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 6),
    _FriOperationalFreeSimpleFixed_Type()
)
friOperationalFreeSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleFixed.setStatus("mandatory")


class _FriOperationalFreeSimpleSequence_Type(IntegerSequence):
    """Custom type friOperationalFreeSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 11),
    )


_FriOperationalFreeSimpleSequence_Type.__name__ = "IntegerSequence"
_FriOperationalFreeSimpleSequence_Object = MibTableColumn
friOperationalFreeSimpleSequence = _FriOperationalFreeSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 7),
    _FriOperationalFreeSimpleSequence_Type()
)
friOperationalFreeSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleSequence.setStatus("mandatory")
_FriOperationalFreeSimpleObjId_Type = IntegerSequence
_FriOperationalFreeSimpleObjId_Object = MibTableColumn
friOperationalFreeSimpleObjId = _FriOperationalFreeSimpleObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 8),
    _FriOperationalFreeSimpleObjId_Type()
)
friOperationalFreeSimpleObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleObjId.setStatus("mandatory")
_FriOperationalFreeSimpleComponent_Type = RowPointer
_FriOperationalFreeSimpleComponent_Object = MibTableColumn
friOperationalFreeSimpleComponent = _FriOperationalFreeSimpleComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 9),
    _FriOperationalFreeSimpleComponent_Type()
)
friOperationalFreeSimpleComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleComponent.setStatus("mandatory")


class _FriOperationalFreeSimpleHex_Type(HexString):
    """Custom type friOperationalFreeSimpleHex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_FriOperationalFreeSimpleHex_Type.__name__ = "HexString"
_FriOperationalFreeSimpleHex_Object = MibTableColumn
friOperationalFreeSimpleHex = _FriOperationalFreeSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 10),
    _FriOperationalFreeSimpleHex_Type()
)
friOperationalFreeSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalFreeSimpleHex.setStatus("mandatory")


class _FriOperationalStructSetEnumeration_Type(OctetString):
    """Custom type friOperationalStructSetEnumeration based on OctetString"""
    defaultHexValue = "9100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FriOperationalStructSetEnumeration_Type.__name__ = "OctetString"
_FriOperationalStructSetEnumeration_Object = MibTableColumn
friOperationalStructSetEnumeration = _FriOperationalStructSetEnumeration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 11),
    _FriOperationalStructSetEnumeration_Type()
)
friOperationalStructSetEnumeration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSetEnumeration.setStatus("mandatory")


class _FriOperationalStructSetUnsigned_Type(OctetString):
    """Custom type friOperationalStructSetUnsigned based on OctetString"""
    defaultHexValue = "54"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FriOperationalStructSetUnsigned_Type.__name__ = "OctetString"
_FriOperationalStructSetUnsigned_Object = MibTableColumn
friOperationalStructSetUnsigned = _FriOperationalStructSetUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 12),
    _FriOperationalStructSetUnsigned_Type()
)
friOperationalStructSetUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSetUnsigned.setStatus("mandatory")


class _FriOperationalStructSimpleAscii_Type(AsciiString):
    """Custom type friOperationalStructSimpleAscii based on AsciiString"""
    defaultHexValue = "61313063686172737472696e67"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalStructSimpleAscii_Type.__name__ = "AsciiString"
_FriOperationalStructSimpleAscii_Object = MibTableColumn
friOperationalStructSimpleAscii = _FriOperationalStructSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 13),
    _FriOperationalStructSimpleAscii_Type()
)
friOperationalStructSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleAscii.setStatus("mandatory")


class _FriOperationalStructSimpleDashed_Type(DashedHexString):
    """Custom type friOperationalStructSimpleDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalStructSimpleDashed_Type.__name__ = "DashedHexString"
_FriOperationalStructSimpleDashed_Object = MibTableColumn
friOperationalStructSimpleDashed = _FriOperationalStructSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 14),
    _FriOperationalStructSimpleDashed_Type()
)
friOperationalStructSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleDashed.setStatus("mandatory")


class _FriOperationalStructSimpleExtended_Type(ExtendedAsciiString):
    """Custom type friOperationalStructSimpleExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalStructSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_FriOperationalStructSimpleExtended_Object = MibTableColumn
friOperationalStructSimpleExtended = _FriOperationalStructSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 15),
    _FriOperationalStructSimpleExtended_Type()
)
friOperationalStructSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleExtended.setStatus("mandatory")


class _FriOperationalStructSimpleBcd_Type(DigitString):
    """Custom type friOperationalStructSimpleBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_FriOperationalStructSimpleBcd_Type.__name__ = "DigitString"
_FriOperationalStructSimpleBcd_Object = MibTableColumn
friOperationalStructSimpleBcd = _FriOperationalStructSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 16),
    _FriOperationalStructSimpleBcd_Type()
)
friOperationalStructSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleBcd.setStatus("mandatory")


class _FriOperationalStructSimpleSigned_Type(Integer32):
    """Custom type friOperationalStructSimpleSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 10),
    )


_FriOperationalStructSimpleSigned_Type.__name__ = "Integer32"
_FriOperationalStructSimpleSigned_Object = MibTableColumn
friOperationalStructSimpleSigned = _FriOperationalStructSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 17),
    _FriOperationalStructSimpleSigned_Type()
)
friOperationalStructSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleSigned.setStatus("mandatory")


class _FriOperationalStructSimpleFixed_Type(FixedPoint1):
    """Custom type friOperationalStructSimpleFixed based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 29),
    )


_FriOperationalStructSimpleFixed_Type.__name__ = "FixedPoint1"
_FriOperationalStructSimpleFixed_Object = MibTableColumn
friOperationalStructSimpleFixed = _FriOperationalStructSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 18),
    _FriOperationalStructSimpleFixed_Type()
)
friOperationalStructSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleFixed.setStatus("mandatory")


class _FriOperationalStructSimpleSequence_Type(IntegerSequence):
    """Custom type friOperationalStructSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_FriOperationalStructSimpleSequence_Type.__name__ = "IntegerSequence"
_FriOperationalStructSimpleSequence_Object = MibTableColumn
friOperationalStructSimpleSequence = _FriOperationalStructSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 19),
    _FriOperationalStructSimpleSequence_Type()
)
friOperationalStructSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleSequence.setStatus("mandatory")


class _FriOperationalStructSimpleEnum_Type(Integer32):
    """Custom type friOperationalStructSimpleEnum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saterday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )


_FriOperationalStructSimpleEnum_Type.__name__ = "Integer32"
_FriOperationalStructSimpleEnum_Object = MibTableColumn
friOperationalStructSimpleEnum = _FriOperationalStructSimpleEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 20),
    _FriOperationalStructSimpleEnum_Type()
)
friOperationalStructSimpleEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleEnum.setStatus("mandatory")


class _FriOperationalStructSimpleHex_Type(HexString):
    """Custom type friOperationalStructSimpleHex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriOperationalStructSimpleHex_Type.__name__ = "HexString"
_FriOperationalStructSimpleHex_Object = MibTableColumn
friOperationalStructSimpleHex = _FriOperationalStructSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 21),
    _FriOperationalStructSimpleHex_Type()
)
friOperationalStructSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleHex.setStatus("mandatory")


class _FriOperationalStructSimpleUnsigned_Type(Unsigned32):
    """Custom type friOperationalStructSimpleUnsigned based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_FriOperationalStructSimpleUnsigned_Type.__name__ = "Unsigned32"
_FriOperationalStructSimpleUnsigned_Object = MibTableColumn
friOperationalStructSimpleUnsigned = _FriOperationalStructSimpleUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 100, 1, 22),
    _FriOperationalStructSimpleUnsigned_Type()
)
friOperationalStructSimpleUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOperationalStructSimpleUnsigned.setStatus("mandatory")
_FriProvisionalTable_Object = MibTable
friProvisionalTable = _FriProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101)
)
if mibBuilder.loadTexts:
    friProvisionalTable.setStatus("mandatory")
_FriProvisionalEntry_Object = MibTableRow
friProvisionalEntry = _FriProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1)
)
friProvisionalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
)
if mibBuilder.loadTexts:
    friProvisionalEntry.setStatus("mandatory")


class _FriProvisionalStructSetEnumeration_Type(OctetString):
    """Custom type friProvisionalStructSetEnumeration based on OctetString"""
    defaultHexValue = "a8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FriProvisionalStructSetEnumeration_Type.__name__ = "OctetString"
_FriProvisionalStructSetEnumeration_Object = MibTableColumn
friProvisionalStructSetEnumeration = _FriProvisionalStructSetEnumeration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 1),
    _FriProvisionalStructSetEnumeration_Type()
)
friProvisionalStructSetEnumeration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSetEnumeration.setStatus("mandatory")


class _FriProvisionalStructSetUnsigned_Type(OctetString):
    """Custom type friProvisionalStructSetUnsigned based on OctetString"""
    defaultHexValue = "aaa8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FriProvisionalStructSetUnsigned_Type.__name__ = "OctetString"
_FriProvisionalStructSetUnsigned_Object = MibTableColumn
friProvisionalStructSetUnsigned = _FriProvisionalStructSetUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 2),
    _FriProvisionalStructSetUnsigned_Type()
)
friProvisionalStructSetUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSetUnsigned.setStatus("mandatory")


class _FriProvisionalStructSimpleAscii_Type(AsciiString):
    """Custom type friProvisionalStructSimpleAscii based on AsciiString"""
    defaultHexValue = "61737472696e676f663131"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalStructSimpleAscii_Type.__name__ = "AsciiString"
_FriProvisionalStructSimpleAscii_Object = MibTableColumn
friProvisionalStructSimpleAscii = _FriProvisionalStructSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 3),
    _FriProvisionalStructSimpleAscii_Type()
)
friProvisionalStructSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleAscii.setStatus("mandatory")


class _FriProvisionalStructSimpleDashed_Type(DashedHexString):
    """Custom type friProvisionalStructSimpleDashed based on DashedHexString"""
    defaultHexValue = "01234556789abCDef0ee"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalStructSimpleDashed_Type.__name__ = "DashedHexString"
_FriProvisionalStructSimpleDashed_Object = MibTableColumn
friProvisionalStructSimpleDashed = _FriProvisionalStructSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 4),
    _FriProvisionalStructSimpleDashed_Type()
)
friProvisionalStructSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleDashed.setStatus("mandatory")


class _FriProvisionalStructSimpleExtended_Type(ExtendedAsciiString):
    """Custom type friProvisionalStructSimpleExtended based on ExtendedAsciiString"""
    defaultHexValue = "61006211632264336544"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalStructSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_FriProvisionalStructSimpleExtended_Object = MibTableColumn
friProvisionalStructSimpleExtended = _FriProvisionalStructSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 5),
    _FriProvisionalStructSimpleExtended_Type()
)
friProvisionalStructSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleExtended.setStatus("mandatory")


class _FriProvisionalStructSimpleBcd_Type(DigitString):
    """Custom type friProvisionalStructSimpleBcd based on DigitString"""
    defaultHexValue = "31323334"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_FriProvisionalStructSimpleBcd_Type.__name__ = "DigitString"
_FriProvisionalStructSimpleBcd_Object = MibTableColumn
friProvisionalStructSimpleBcd = _FriProvisionalStructSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 6),
    _FriProvisionalStructSimpleBcd_Type()
)
friProvisionalStructSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleBcd.setStatus("mandatory")


class _FriProvisionalStructSimpleSequence_Type(IntegerSequence):
    """Custom type friProvisionalStructSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_FriProvisionalStructSimpleSequence_Type.__name__ = "IntegerSequence"
_FriProvisionalStructSimpleSequence_Object = MibTableColumn
friProvisionalStructSimpleSequence = _FriProvisionalStructSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 7),
    _FriProvisionalStructSimpleSequence_Type()
)
friProvisionalStructSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleSequence.setStatus("mandatory")


class _FriProvisionalStructSimpleEnum_Type(Integer32):
    """Custom type friProvisionalStructSimpleEnum based on Integer32"""
    defaultValue = 1

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_FriProvisionalStructSimpleEnum_Type.__name__ = "Integer32"
_FriProvisionalStructSimpleEnum_Object = MibTableColumn
friProvisionalStructSimpleEnum = _FriProvisionalStructSimpleEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 8),
    _FriProvisionalStructSimpleEnum_Type()
)
friProvisionalStructSimpleEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleEnum.setStatus("mandatory")


class _FriProvisionalStructSimpleHex_Type(HexString):
    """Custom type friProvisionalStructSimpleHex based on HexString"""
    defaultHexValue = "3039303930393039303930393039303930393039303930393039"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalStructSimpleHex_Type.__name__ = "HexString"
_FriProvisionalStructSimpleHex_Object = MibTableColumn
friProvisionalStructSimpleHex = _FriProvisionalStructSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 9),
    _FriProvisionalStructSimpleHex_Type()
)
friProvisionalStructSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleHex.setStatus("mandatory")


class _FriProvisionalStructSimpleUnsigned_Type(Unsigned32):
    """Custom type friProvisionalStructSimpleUnsigned based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriProvisionalStructSimpleUnsigned_Type.__name__ = "Unsigned32"
_FriProvisionalStructSimpleUnsigned_Object = MibTableColumn
friProvisionalStructSimpleUnsigned = _FriProvisionalStructSimpleUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 10),
    _FriProvisionalStructSimpleUnsigned_Type()
)
friProvisionalStructSimpleUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleUnsigned.setStatus("mandatory")


class _FriProvisionalStructSimpleSigned_Type(Integer32):
    """Custom type friProvisionalStructSimpleSigned based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_FriProvisionalStructSimpleSigned_Type.__name__ = "Integer32"
_FriProvisionalStructSimpleSigned_Object = MibTableColumn
friProvisionalStructSimpleSigned = _FriProvisionalStructSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 11),
    _FriProvisionalStructSimpleSigned_Type()
)
friProvisionalStructSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleSigned.setStatus("mandatory")


class _FriProvisionalStructSimpleFixed_Type(FixedPoint2):
    """Custom type friProvisionalStructSimpleFixed based on FixedPoint2"""
    defaultValue = 350

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(254, 355),
    )


_FriProvisionalStructSimpleFixed_Type.__name__ = "FixedPoint2"
_FriProvisionalStructSimpleFixed_Object = MibTableColumn
friProvisionalStructSimpleFixed = _FriProvisionalStructSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 12),
    _FriProvisionalStructSimpleFixed_Type()
)
friProvisionalStructSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalStructSimpleFixed.setStatus("mandatory")


class _FriProvisionalFreeSimpleAscii_Type(AsciiString):
    """Custom type friProvisionalFreeSimpleAscii based on AsciiString"""
    defaultHexValue = "61737472696e676f663131"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalFreeSimpleAscii_Type.__name__ = "AsciiString"
_FriProvisionalFreeSimpleAscii_Object = MibTableColumn
friProvisionalFreeSimpleAscii = _FriProvisionalFreeSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 13),
    _FriProvisionalFreeSimpleAscii_Type()
)
friProvisionalFreeSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleAscii.setStatus("mandatory")


class _FriProvisionalFreeSimpleDashed_Type(DashedHexString):
    """Custom type friProvisionalFreeSimpleDashed based on DashedHexString"""
    defaultHexValue = "00112233445566778899aabbccddeeff"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalFreeSimpleDashed_Type.__name__ = "DashedHexString"
_FriProvisionalFreeSimpleDashed_Object = MibTableColumn
friProvisionalFreeSimpleDashed = _FriProvisionalFreeSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 14),
    _FriProvisionalFreeSimpleDashed_Type()
)
friProvisionalFreeSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleDashed.setStatus("mandatory")


class _FriProvisionalFreeSimpleExtended_Type(ExtendedAsciiString):
    """Custom type friProvisionalFreeSimpleExtended based on ExtendedAsciiString"""
    defaultHexValue = "61626300006465665555676869"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalFreeSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_FriProvisionalFreeSimpleExtended_Object = MibTableColumn
friProvisionalFreeSimpleExtended = _FriProvisionalFreeSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 15),
    _FriProvisionalFreeSimpleExtended_Type()
)
friProvisionalFreeSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleExtended.setStatus("mandatory")


class _FriProvisionalFreeSimpleBcd_Type(DigitString):
    """Custom type friProvisionalFreeSimpleBcd based on DigitString"""
    defaultHexValue = "31323334"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_FriProvisionalFreeSimpleBcd_Type.__name__ = "DigitString"
_FriProvisionalFreeSimpleBcd_Object = MibTableColumn
friProvisionalFreeSimpleBcd = _FriProvisionalFreeSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 16),
    _FriProvisionalFreeSimpleBcd_Type()
)
friProvisionalFreeSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleBcd.setStatus("mandatory")


class _FriProvisionalFreeSimpleSequence_Type(IntegerSequence):
    """Custom type friProvisionalFreeSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )


_FriProvisionalFreeSimpleSequence_Type.__name__ = "IntegerSequence"
_FriProvisionalFreeSimpleSequence_Object = MibTableColumn
friProvisionalFreeSimpleSequence = _FriProvisionalFreeSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 17),
    _FriProvisionalFreeSimpleSequence_Type()
)
friProvisionalFreeSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleSequence.setStatus("mandatory")


class _FriProvisionalFreeSimpleSigned_Type(Integer32):
    """Custom type friProvisionalFreeSimpleSigned based on Integer32"""
    defaultValue = -11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FriProvisionalFreeSimpleSigned_Type.__name__ = "Integer32"
_FriProvisionalFreeSimpleSigned_Object = MibTableColumn
friProvisionalFreeSimpleSigned = _FriProvisionalFreeSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 18),
    _FriProvisionalFreeSimpleSigned_Type()
)
friProvisionalFreeSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleSigned.setStatus("mandatory")


class _FriProvisionalFreeSimpleFixed_Type(FixedPoint2):
    """Custom type friProvisionalFreeSimpleFixed based on FixedPoint2"""
    defaultValue = 122

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 233),
    )


_FriProvisionalFreeSimpleFixed_Type.__name__ = "FixedPoint2"
_FriProvisionalFreeSimpleFixed_Object = MibTableColumn
friProvisionalFreeSimpleFixed = _FriProvisionalFreeSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 19),
    _FriProvisionalFreeSimpleFixed_Type()
)
friProvisionalFreeSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleFixed.setStatus("mandatory")
_FriProvisionalFreeSimpleObjId_Type = IntegerSequence
_FriProvisionalFreeSimpleObjId_Object = MibTableColumn
friProvisionalFreeSimpleObjId = _FriProvisionalFreeSimpleObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 20),
    _FriProvisionalFreeSimpleObjId_Type()
)
friProvisionalFreeSimpleObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleObjId.setStatus("mandatory")
_FriProvisionalFreeSimpleComponent_Type = RowPointer
_FriProvisionalFreeSimpleComponent_Object = MibTableColumn
friProvisionalFreeSimpleComponent = _FriProvisionalFreeSimpleComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 21),
    _FriProvisionalFreeSimpleComponent_Type()
)
friProvisionalFreeSimpleComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleComponent.setStatus("mandatory")


class _FriProvisionalFreeSimpleHex_Type(HexString):
    """Custom type friProvisionalFreeSimpleHex based on HexString"""
    defaultHexValue = "00112233445566778899aaBBcCDdeeFF313233"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_FriProvisionalFreeSimpleHex_Type.__name__ = "HexString"
_FriProvisionalFreeSimpleHex_Object = MibTableColumn
friProvisionalFreeSimpleHex = _FriProvisionalFreeSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 22),
    _FriProvisionalFreeSimpleHex_Type()
)
friProvisionalFreeSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friProvisionalFreeSimpleHex.setStatus("mandatory")


class _FriEscapeCheckAttribute_Type(Unsigned32):
    """Custom type friEscapeCheckAttribute based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriEscapeCheckAttribute_Type.__name__ = "Unsigned32"
_FriEscapeCheckAttribute_Object = MibTableColumn
friEscapeCheckAttribute = _FriEscapeCheckAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 23),
    _FriEscapeCheckAttribute_Type()
)
friEscapeCheckAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friEscapeCheckAttribute.setStatus("mandatory")


class _FriEscapeDefaultsComponent_Type(Unsigned32):
    """Custom type friEscapeDefaultsComponent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriEscapeDefaultsComponent_Type.__name__ = "Unsigned32"
_FriEscapeDefaultsComponent_Object = MibTableColumn
friEscapeDefaultsComponent = _FriEscapeDefaultsComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 24),
    _FriEscapeDefaultsComponent_Type()
)
friEscapeDefaultsComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friEscapeDefaultsComponent.setStatus("mandatory")


class _FriEscapeDefaultsGroup_Type(Unsigned32):
    """Custom type friEscapeDefaultsGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriEscapeDefaultsGroup_Type.__name__ = "Unsigned32"
_FriEscapeDefaultsGroup_Object = MibTableColumn
friEscapeDefaultsGroup = _FriEscapeDefaultsGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 25),
    _FriEscapeDefaultsGroup_Type()
)
friEscapeDefaultsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friEscapeDefaultsGroup.setStatus("mandatory")


class _FriEscapeSet_Type(AsciiString):
    """Custom type friEscapeSet based on AsciiString"""
    defaultHexValue = "70617373776f7264"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_FriEscapeSet_Type.__name__ = "AsciiString"
_FriEscapeSet_Object = MibTableColumn
friEscapeSet = _FriEscapeSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 26),
    _FriEscapeSet_Type()
)
friEscapeSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friEscapeSet.setStatus("mandatory")


class _FriEscapeCopyComponent_Type(Unsigned32):
    """Custom type friEscapeCopyComponent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FriEscapeCopyComponent_Type.__name__ = "Unsigned32"
_FriEscapeCopyComponent_Object = MibTableColumn
friEscapeCopyComponent = _FriEscapeCopyComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 27),
    _FriEscapeCopyComponent_Type()
)
friEscapeCopyComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friEscapeCopyComponent.setStatus("mandatory")


class _FriEscapeCopyGroup_Type(Unsigned32):
    """Custom type friEscapeCopyGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FriEscapeCopyGroup_Type.__name__ = "Unsigned32"
_FriEscapeCopyGroup_Object = MibTableColumn
friEscapeCopyGroup = _FriEscapeCopyGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 28),
    _FriEscapeCopyGroup_Type()
)
friEscapeCopyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friEscapeCopyGroup.setStatus("mandatory")


class _FriEscapeCopyAttribute_Type(Unsigned32):
    """Custom type friEscapeCopyAttribute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FriEscapeCopyAttribute_Type.__name__ = "Unsigned32"
_FriEscapeCopyAttribute_Object = MibTableColumn
friEscapeCopyAttribute = _FriEscapeCopyAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 101, 1, 29),
    _FriEscapeCopyAttribute_Type()
)
friEscapeCopyAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friEscapeCopyAttribute.setStatus("mandatory")
_FriStateTable_Object = MibTable
friStateTable = _FriStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102)
)
if mibBuilder.loadTexts:
    friStateTable.setStatus("mandatory")
_FriStateEntry_Object = MibTableRow
friStateEntry = _FriStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1)
)
friStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
)
if mibBuilder.loadTexts:
    friStateEntry.setStatus("mandatory")


class _FriAdminState_Type(Integer32):
    """Custom type friAdminState based on Integer32"""
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
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_FriAdminState_Type.__name__ = "Integer32"
_FriAdminState_Object = MibTableColumn
friAdminState = _FriAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 1),
    _FriAdminState_Type()
)
friAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friAdminState.setStatus("mandatory")


class _FriOperationalState_Type(Integer32):
    """Custom type friOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FriOperationalState_Type.__name__ = "Integer32"
_FriOperationalState_Object = MibTableColumn
friOperationalState = _FriOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 2),
    _FriOperationalState_Type()
)
friOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friOperationalState.setStatus("mandatory")


class _FriUsageState_Type(Integer32):
    """Custom type friUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_FriUsageState_Type.__name__ = "Integer32"
_FriUsageState_Object = MibTableColumn
friUsageState = _FriUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 3),
    _FriUsageState_Type()
)
friUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friUsageState.setStatus("mandatory")


class _FriAvailabilityStatus_Type(OctetString):
    """Custom type friAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FriAvailabilityStatus_Type.__name__ = "OctetString"
_FriAvailabilityStatus_Object = MibTableColumn
friAvailabilityStatus = _FriAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 4),
    _FriAvailabilityStatus_Type()
)
friAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friAvailabilityStatus.setStatus("mandatory")


class _FriProceduralStatus_Type(OctetString):
    """Custom type friProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FriProceduralStatus_Type.__name__ = "OctetString"
_FriProceduralStatus_Object = MibTableColumn
friProceduralStatus = _FriProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 5),
    _FriProceduralStatus_Type()
)
friProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friProceduralStatus.setStatus("mandatory")


class _FriControlStatus_Type(OctetString):
    """Custom type friControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FriControlStatus_Type.__name__ = "OctetString"
_FriControlStatus_Object = MibTableColumn
friControlStatus = _FriControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 6),
    _FriControlStatus_Type()
)
friControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friControlStatus.setStatus("mandatory")


class _FriAlarmStatus_Type(OctetString):
    """Custom type friAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FriAlarmStatus_Type.__name__ = "OctetString"
_FriAlarmStatus_Object = MibTableColumn
friAlarmStatus = _FriAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 7),
    _FriAlarmStatus_Type()
)
friAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friAlarmStatus.setStatus("mandatory")


class _FriStandbyStatus_Type(Integer32):
    """Custom type friStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_FriStandbyStatus_Type.__name__ = "Integer32"
_FriStandbyStatus_Object = MibTableColumn
friStandbyStatus = _FriStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 8),
    _FriStandbyStatus_Type()
)
friStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friStandbyStatus.setStatus("mandatory")


class _FriUnknownStatus_Type(Integer32):
    """Custom type friUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FriUnknownStatus_Type.__name__ = "Integer32"
_FriUnknownStatus_Object = MibTableColumn
friUnknownStatus = _FriUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 102, 1, 9),
    _FriUnknownStatus_Type()
)
friUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friUnknownStatus.setStatus("mandatory")
_FriPfListAsciiTable_Object = MibTable
friPfListAsciiTable = _FriPfListAsciiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1187)
)
if mibBuilder.loadTexts:
    friPfListAsciiTable.setStatus("mandatory")
_FriPfListAsciiEntry_Object = MibTableRow
friPfListAsciiEntry = _FriPfListAsciiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1187, 1)
)
friPfListAsciiEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friPfListAsciiValue"),
)
if mibBuilder.loadTexts:
    friPfListAsciiEntry.setStatus("mandatory")


class _FriPfListAsciiValue_Type(AsciiString):
    """Custom type friPfListAsciiValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FriPfListAsciiValue_Type.__name__ = "AsciiString"
_FriPfListAsciiValue_Object = MibTableColumn
friPfListAsciiValue = _FriPfListAsciiValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1187, 1, 1),
    _FriPfListAsciiValue_Type()
)
friPfListAsciiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPfListAsciiValue.setStatus("mandatory")
_FriPfListAsciiRowStatus_Type = RowStatus
_FriPfListAsciiRowStatus_Object = MibTableColumn
friPfListAsciiRowStatus = _FriPfListAsciiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1187, 1, 2),
    _FriPfListAsciiRowStatus_Type()
)
friPfListAsciiRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friPfListAsciiRowStatus.setStatus("mandatory")
_FriPfListUnsignedTable_Object = MibTable
friPfListUnsignedTable = _FriPfListUnsignedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1188)
)
if mibBuilder.loadTexts:
    friPfListUnsignedTable.setStatus("mandatory")
_FriPfListUnsignedEntry_Object = MibTableRow
friPfListUnsignedEntry = _FriPfListUnsignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1188, 1)
)
friPfListUnsignedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friPfListUnsignedValue"),
)
if mibBuilder.loadTexts:
    friPfListUnsignedEntry.setStatus("mandatory")


class _FriPfListUnsignedValue_Type(Integer32):
    """Custom type friPfListUnsignedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriPfListUnsignedValue_Type.__name__ = "Integer32"
_FriPfListUnsignedValue_Object = MibTableColumn
friPfListUnsignedValue = _FriPfListUnsignedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1188, 1, 1),
    _FriPfListUnsignedValue_Type()
)
friPfListUnsignedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPfListUnsignedValue.setStatus("mandatory")
_FriPfListUnsignedRowStatus_Type = RowStatus
_FriPfListUnsignedRowStatus_Object = MibTableColumn
friPfListUnsignedRowStatus = _FriPfListUnsignedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1188, 1, 2),
    _FriPfListUnsignedRowStatus_Type()
)
friPfListUnsignedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friPfListUnsignedRowStatus.setStatus("mandatory")
_FriPfListFixedTable_Object = MibTable
friPfListFixedTable = _FriPfListFixedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1189)
)
if mibBuilder.loadTexts:
    friPfListFixedTable.setStatus("mandatory")
_FriPfListFixedEntry_Object = MibTableRow
friPfListFixedEntry = _FriPfListFixedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1189, 1)
)
friPfListFixedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friPfListFixedValue"),
)
if mibBuilder.loadTexts:
    friPfListFixedEntry.setStatus("mandatory")


class _FriPfListFixedValue_Type(Integer32):
    """Custom type friPfListFixedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2559),
    )


_FriPfListFixedValue_Type.__name__ = "Integer32"
_FriPfListFixedValue_Object = MibTableColumn
friPfListFixedValue = _FriPfListFixedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1189, 1, 1),
    _FriPfListFixedValue_Type()
)
friPfListFixedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPfListFixedValue.setStatus("mandatory")
_FriPfListFixedRowStatus_Type = RowStatus
_FriPfListFixedRowStatus_Object = MibTableColumn
friPfListFixedRowStatus = _FriPfListFixedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1189, 1, 2),
    _FriPfListFixedRowStatus_Type()
)
friPfListFixedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friPfListFixedRowStatus.setStatus("mandatory")
_FriPfListSignedTable_Object = MibTable
friPfListSignedTable = _FriPfListSignedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1190)
)
if mibBuilder.loadTexts:
    friPfListSignedTable.setStatus("mandatory")
_FriPfListSignedEntry_Object = MibTableRow
friPfListSignedEntry = _FriPfListSignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1190, 1)
)
friPfListSignedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friPfListSignedValue"),
)
if mibBuilder.loadTexts:
    friPfListSignedEntry.setStatus("mandatory")


class _FriPfListSignedValue_Type(Integer32):
    """Custom type friPfListSignedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 255),
    )


_FriPfListSignedValue_Type.__name__ = "Integer32"
_FriPfListSignedValue_Object = MibTableColumn
friPfListSignedValue = _FriPfListSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1190, 1, 1),
    _FriPfListSignedValue_Type()
)
friPfListSignedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPfListSignedValue.setStatus("mandatory")
_FriPfListSignedRowStatus_Type = RowStatus
_FriPfListSignedRowStatus_Object = MibTableColumn
friPfListSignedRowStatus = _FriPfListSignedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1190, 1, 2),
    _FriPfListSignedRowStatus_Type()
)
friPfListSignedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friPfListSignedRowStatus.setStatus("mandatory")
_FriOfListComponentTable_Object = MibTable
friOfListComponentTable = _FriOfListComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1191)
)
if mibBuilder.loadTexts:
    friOfListComponentTable.setStatus("mandatory")
_FriOfListComponentEntry_Object = MibTableRow
friOfListComponentEntry = _FriOfListComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1191, 1)
)
friOfListComponentEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friOfListComponentValue"),
)
if mibBuilder.loadTexts:
    friOfListComponentEntry.setStatus("mandatory")
_FriOfListComponentValue_Type = RowPointer
_FriOfListComponentValue_Object = MibTableColumn
friOfListComponentValue = _FriOfListComponentValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1191, 1, 1),
    _FriOfListComponentValue_Type()
)
friOfListComponentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOfListComponentValue.setStatus("mandatory")
_FriOfListComponentRowStatus_Type = RowStatus
_FriOfListComponentRowStatus_Object = MibTableColumn
friOfListComponentRowStatus = _FriOfListComponentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1191, 1, 2),
    _FriOfListComponentRowStatus_Type()
)
friOfListComponentRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friOfListComponentRowStatus.setStatus("mandatory")
_FriOfListEnumerationTable_Object = MibTable
friOfListEnumerationTable = _FriOfListEnumerationTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1192)
)
if mibBuilder.loadTexts:
    friOfListEnumerationTable.setStatus("mandatory")
_FriOfListEnumerationEntry_Object = MibTableRow
friOfListEnumerationEntry = _FriOfListEnumerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1192, 1)
)
friOfListEnumerationEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friIndex"),
    (0, "Nortel-Magellan-Passport-CasTestMIB", "friOfListEnumerationValue"),
)
if mibBuilder.loadTexts:
    friOfListEnumerationEntry.setStatus("mandatory")


class _FriOfListEnumerationValue_Type(Integer32):
    """Custom type friOfListEnumerationValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_FriOfListEnumerationValue_Type.__name__ = "Integer32"
_FriOfListEnumerationValue_Object = MibTableColumn
friOfListEnumerationValue = _FriOfListEnumerationValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1192, 1, 1),
    _FriOfListEnumerationValue_Type()
)
friOfListEnumerationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friOfListEnumerationValue.setStatus("mandatory")
_FriOfListEnumerationRowStatus_Type = RowStatus
_FriOfListEnumerationRowStatus_Object = MibTableColumn
friOfListEnumerationRowStatus = _FriOfListEnumerationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5001, 1192, 1, 2),
    _FriOfListEnumerationRowStatus_Type()
)
friOfListEnumerationRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friOfListEnumerationRowStatus.setStatus("mandatory")
_Registered_ObjectIdentity = ObjectIdentity
registered = _Registered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004)
)
_RegisteredRowStatusTable_Object = MibTable
registeredRowStatusTable = _RegisteredRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 1)
)
if mibBuilder.loadTexts:
    registeredRowStatusTable.setStatus("mandatory")
_RegisteredRowStatusEntry_Object = MibTableRow
registeredRowStatusEntry = _RegisteredRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 1, 1)
)
registeredRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "registeredIndex"),
)
if mibBuilder.loadTexts:
    registeredRowStatusEntry.setStatus("mandatory")
_RegisteredRowStatus_Type = RowStatus
_RegisteredRowStatus_Object = MibTableColumn
registeredRowStatus = _RegisteredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 1, 1, 1),
    _RegisteredRowStatus_Type()
)
registeredRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registeredRowStatus.setStatus("mandatory")
_RegisteredComponentName_Type = DisplayString
_RegisteredComponentName_Object = MibTableColumn
registeredComponentName = _RegisteredComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 1, 1, 2),
    _RegisteredComponentName_Type()
)
registeredComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registeredComponentName.setStatus("mandatory")
_RegisteredStorageType_Type = StorageType
_RegisteredStorageType_Object = MibTableColumn
registeredStorageType = _RegisteredStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 1, 1, 4),
    _RegisteredStorageType_Type()
)
registeredStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registeredStorageType.setStatus("mandatory")


class _RegisteredIndex_Type(Integer32):
    """Custom type registeredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RegisteredIndex_Type.__name__ = "Integer32"
_RegisteredIndex_Object = MibTableColumn
registeredIndex = _RegisteredIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 1, 1, 10),
    _RegisteredIndex_Type()
)
registeredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    registeredIndex.setStatus("mandatory")
_RegisteredDataTable_Object = MibTable
registeredDataTable = _RegisteredDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 10)
)
if mibBuilder.loadTexts:
    registeredDataTable.setStatus("mandatory")
_RegisteredDataEntry_Object = MibTableRow
registeredDataEntry = _RegisteredDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 10, 1)
)
registeredDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-CasTestMIB", "registeredIndex"),
)
if mibBuilder.loadTexts:
    registeredDataEntry.setStatus("mandatory")


class _RegisteredAttribute_Type(Unsigned32):
    """Custom type registeredAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RegisteredAttribute_Type.__name__ = "Unsigned32"
_RegisteredAttribute_Object = MibTableColumn
registeredAttribute = _RegisteredAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5004, 10, 1, 1),
    _RegisteredAttribute_Type()
)
registeredAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registeredAttribute.setStatus("mandatory")
_CasTestMIB_ObjectIdentity = ObjectIdentity
casTestMIB = _CasTestMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103)
)
_CasTestGroup_ObjectIdentity = ObjectIdentity
casTestGroup = _CasTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 1)
)
_CasTestGroupBE_ObjectIdentity = ObjectIdentity
casTestGroupBE = _CasTestGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 1, 5)
)
_CasTestGroupBE01_ObjectIdentity = ObjectIdentity
casTestGroupBE01 = _CasTestGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 1, 5, 2)
)
_CasTestGroupBE01A_ObjectIdentity = ObjectIdentity
casTestGroupBE01A = _CasTestGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 1, 5, 2, 2)
)
_CasTestCapabilities_ObjectIdentity = ObjectIdentity
casTestCapabilities = _CasTestCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 3)
)
_CasTestCapabilitiesBE_ObjectIdentity = ObjectIdentity
casTestCapabilitiesBE = _CasTestCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 3, 5)
)
_CasTestCapabilitiesBE01_ObjectIdentity = ObjectIdentity
casTestCapabilitiesBE01 = _CasTestCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 3, 5, 2)
)
_CasTestCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
casTestCapabilitiesBE01A = _CasTestCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 103, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-CasTestMIB",
    **{"example": example,
       "exampleRowStatusTable": exampleRowStatusTable,
       "exampleRowStatusEntry": exampleRowStatusEntry,
       "exampleRowStatus": exampleRowStatus,
       "exampleComponentName": exampleComponentName,
       "exampleStorageType": exampleStorageType,
       "exampleIndex": exampleIndex,
       "exampleDecimal": exampleDecimal,
       "exampleDecimalRowStatusTable": exampleDecimalRowStatusTable,
       "exampleDecimalRowStatusEntry": exampleDecimalRowStatusEntry,
       "exampleDecimalRowStatus": exampleDecimalRowStatus,
       "exampleDecimalComponentName": exampleDecimalComponentName,
       "exampleDecimalStorageType": exampleDecimalStorageType,
       "exampleDecimalIndex": exampleDecimalIndex,
       "exampleDecimalOperationalTable": exampleDecimalOperationalTable,
       "exampleDecimalOperationalEntry": exampleDecimalOperationalEntry,
       "exampleDecimalOperStructInteger": exampleDecimalOperStructInteger,
       "exampleDecimalOperStructIntSet": exampleDecimalOperStructIntSet,
       "exampleDecimalOperFreeInteger": exampleDecimalOperFreeInteger,
       "exampleDecimalOperFreeIntSet": exampleDecimalOperFreeIntSet,
       "exampleDecimalOperFreeCounter32": exampleDecimalOperFreeCounter32,
       "exampleDecimalOperFreeGauge32": exampleDecimalOperFreeGauge32,
       "exampleDecimalOperFreeTimeInterval": exampleDecimalOperFreeTimeInterval,
       "exampleDecimalProvisionalTable": exampleDecimalProvisionalTable,
       "exampleDecimalProvisionalEntry": exampleDecimalProvisionalEntry,
       "exampleDecimalProvDecimalSub": exampleDecimalProvDecimalSub,
       "exampleDecimalProvStructInteger": exampleDecimalProvStructInteger,
       "exampleDecimalProvStructIntSet": exampleDecimalProvStructIntSet,
       "exampleDecimalProvFreeInteger": exampleDecimalProvFreeInteger,
       "exampleDecimalProvFreeInteger1": exampleDecimalProvFreeInteger1,
       "exampleDecimalProvFreeInteger2": exampleDecimalProvFreeInteger2,
       "exampleDecimalProvFreeIntSet": exampleDecimalProvFreeIntSet,
       "exampleDecimalProvFreeIntSet1": exampleDecimalProvFreeIntSet1,
       "exampleDecimalOsIntVectorTable": exampleDecimalOsIntVectorTable,
       "exampleDecimalOsIntVectorEntry": exampleDecimalOsIntVectorEntry,
       "exampleDecimalOsIntVectorIndex": exampleDecimalOsIntVectorIndex,
       "exampleDecimalOsIntVectorValue": exampleDecimalOsIntVectorValue,
       "exampleDecimalOsIntArrayTable": exampleDecimalOsIntArrayTable,
       "exampleDecimalOsIntArrayEntry": exampleDecimalOsIntArrayEntry,
       "exampleDecimalOsIntArrayRowIndex": exampleDecimalOsIntArrayRowIndex,
       "exampleDecimalOsIntArrayColumnIndex": exampleDecimalOsIntArrayColumnIndex,
       "exampleDecimalOsIntArrayValue": exampleDecimalOsIntArrayValue,
       "exampleDecimalOfIntVectorTable": exampleDecimalOfIntVectorTable,
       "exampleDecimalOfIntVectorEntry": exampleDecimalOfIntVectorEntry,
       "exampleDecimalOfIntVectorIndex": exampleDecimalOfIntVectorIndex,
       "exampleDecimalOfIntVectorValue": exampleDecimalOfIntVectorValue,
       "exampleDecimalOfIntArrayTable": exampleDecimalOfIntArrayTable,
       "exampleDecimalOfIntArrayEntry": exampleDecimalOfIntArrayEntry,
       "exampleDecimalOfIntArrayRowIndex": exampleDecimalOfIntArrayRowIndex,
       "exampleDecimalOfIntArrayColumnIndex": exampleDecimalOfIntArrayColumnIndex,
       "exampleDecimalOfIntArrayValue": exampleDecimalOfIntArrayValue,
       "exampleDecimalOfIntReplicatedTable": exampleDecimalOfIntReplicatedTable,
       "exampleDecimalOfIntReplicatedEntry": exampleDecimalOfIntReplicatedEntry,
       "exampleDecimalOfIntReplicatedIndex": exampleDecimalOfIntReplicatedIndex,
       "exampleDecimalOfIntReplicatedValue": exampleDecimalOfIntReplicatedValue,
       "exampleDecimalOfIntReplicatedRowStatus": exampleDecimalOfIntReplicatedRowStatus,
       "exampleDecimalOfIntListTable": exampleDecimalOfIntListTable,
       "exampleDecimalOfIntListEntry": exampleDecimalOfIntListEntry,
       "exampleDecimalOfIntListValue": exampleDecimalOfIntListValue,
       "exampleDecimalOfIntListRowStatus": exampleDecimalOfIntListRowStatus,
       "exampleDecimalPsIntVectorTable": exampleDecimalPsIntVectorTable,
       "exampleDecimalPsIntVectorEntry": exampleDecimalPsIntVectorEntry,
       "exampleDecimalPsIntVectorIndex": exampleDecimalPsIntVectorIndex,
       "exampleDecimalPsIntVectorValue": exampleDecimalPsIntVectorValue,
       "exampleDecimalPsIntArrayTable": exampleDecimalPsIntArrayTable,
       "exampleDecimalPsIntArrayEntry": exampleDecimalPsIntArrayEntry,
       "exampleDecimalPsIntArrayRowIndex": exampleDecimalPsIntArrayRowIndex,
       "exampleDecimalPsIntArrayColumnIndex": exampleDecimalPsIntArrayColumnIndex,
       "exampleDecimalPsIntArrayValue": exampleDecimalPsIntArrayValue,
       "exampleDecimalPfIntVectorTable": exampleDecimalPfIntVectorTable,
       "exampleDecimalPfIntVectorEntry": exampleDecimalPfIntVectorEntry,
       "exampleDecimalPfIntVectorIndex": exampleDecimalPfIntVectorIndex,
       "exampleDecimalPfIntVectorValue": exampleDecimalPfIntVectorValue,
       "exampleDecimalPfIntVector1Table": exampleDecimalPfIntVector1Table,
       "exampleDecimalPfIntVector1Entry": exampleDecimalPfIntVector1Entry,
       "exampleDecimalPfIntVector1Index": exampleDecimalPfIntVector1Index,
       "exampleDecimalPfIntVector1Value": exampleDecimalPfIntVector1Value,
       "exampleDecimalPfIntArrayTable": exampleDecimalPfIntArrayTable,
       "exampleDecimalPfIntArrayEntry": exampleDecimalPfIntArrayEntry,
       "exampleDecimalPfIntArrayRowIndex": exampleDecimalPfIntArrayRowIndex,
       "exampleDecimalPfIntArrayColumnIndex": exampleDecimalPfIntArrayColumnIndex,
       "exampleDecimalPfIntArrayValue": exampleDecimalPfIntArrayValue,
       "exampleDecimalPfIntArray1Table": exampleDecimalPfIntArray1Table,
       "exampleDecimalPfIntArray1Entry": exampleDecimalPfIntArray1Entry,
       "exampleDecimalPfIntArray1RowIndex": exampleDecimalPfIntArray1RowIndex,
       "exampleDecimalPfIntArray1ColumnIndex": exampleDecimalPfIntArray1ColumnIndex,
       "exampleDecimalPfIntArray1Value": exampleDecimalPfIntArray1Value,
       "exampleDecimalPfIntReplicatedTable": exampleDecimalPfIntReplicatedTable,
       "exampleDecimalPfIntReplicatedEntry": exampleDecimalPfIntReplicatedEntry,
       "exampleDecimalPfIntReplicatedIndex": exampleDecimalPfIntReplicatedIndex,
       "exampleDecimalPfIntReplicatedValue": exampleDecimalPfIntReplicatedValue,
       "exampleDecimalPfIntReplicatedRowStatus": exampleDecimalPfIntReplicatedRowStatus,
       "exampleDecimalPfIntReplicated1Table": exampleDecimalPfIntReplicated1Table,
       "exampleDecimalPfIntReplicated1Entry": exampleDecimalPfIntReplicated1Entry,
       "exampleDecimalPfIntReplicated1Index": exampleDecimalPfIntReplicated1Index,
       "exampleDecimalPfIntReplicated1Value": exampleDecimalPfIntReplicated1Value,
       "exampleDecimalPfIntReplicated1RowStatus": exampleDecimalPfIntReplicated1RowStatus,
       "exampleDecimalPfIntListTable": exampleDecimalPfIntListTable,
       "exampleDecimalPfIntListEntry": exampleDecimalPfIntListEntry,
       "exampleDecimalPfIntListValue": exampleDecimalPfIntListValue,
       "exampleDecimalPfIntListRowStatus": exampleDecimalPfIntListRowStatus,
       "exampleDecimalPfIntList1Table": exampleDecimalPfIntList1Table,
       "exampleDecimalPfIntList1Entry": exampleDecimalPfIntList1Entry,
       "exampleDecimalPfIntList1Value": exampleDecimalPfIntList1Value,
       "exampleDecimalPfIntList1RowStatus": exampleDecimalPfIntList1RowStatus,
       "exampleHex": exampleHex,
       "exampleHexRowStatusTable": exampleHexRowStatusTable,
       "exampleHexRowStatusEntry": exampleHexRowStatusEntry,
       "exampleHexRowStatus": exampleHexRowStatus,
       "exampleHexComponentName": exampleHexComponentName,
       "exampleHexStorageType": exampleHexStorageType,
       "exampleHexIndex": exampleHexIndex,
       "exampleHexOperationalTable": exampleHexOperationalTable,
       "exampleHexOperationalEntry": exampleHexOperationalEntry,
       "exampleHexOperStructHex": exampleHexOperStructHex,
       "exampleHexOperFreeHex": exampleHexOperFreeHex,
       "exampleHexProvisionalTable": exampleHexProvisionalTable,
       "exampleHexProvisionalEntry": exampleHexProvisionalEntry,
       "exampleHexProvEnumSub": exampleHexProvEnumSub,
       "exampleHexProvStructHex": exampleHexProvStructHex,
       "exampleHexProvFreeHex": exampleHexProvFreeHex,
       "exampleHexProvFreeHex1": exampleHexProvFreeHex1,
       "exampleHexOsHexVectorTable": exampleHexOsHexVectorTable,
       "exampleHexOsHexVectorEntry": exampleHexOsHexVectorEntry,
       "exampleHexOsHexVectorIndex": exampleHexOsHexVectorIndex,
       "exampleHexOsHexVectorValue": exampleHexOsHexVectorValue,
       "exampleHexOsHexArrayTable": exampleHexOsHexArrayTable,
       "exampleHexOsHexArrayEntry": exampleHexOsHexArrayEntry,
       "exampleHexOsHexArrayRowIndex": exampleHexOsHexArrayRowIndex,
       "exampleHexOsHexArrayColumnIndex": exampleHexOsHexArrayColumnIndex,
       "exampleHexOsHexArrayValue": exampleHexOsHexArrayValue,
       "exampleHexOfHexVectorTable": exampleHexOfHexVectorTable,
       "exampleHexOfHexVectorEntry": exampleHexOfHexVectorEntry,
       "exampleHexOfHexVectorIndex": exampleHexOfHexVectorIndex,
       "exampleHexOfHexVectorValue": exampleHexOfHexVectorValue,
       "exampleHexOfHexArrayTable": exampleHexOfHexArrayTable,
       "exampleHexOfHexArrayEntry": exampleHexOfHexArrayEntry,
       "exampleHexOfHexArrayRowIndex": exampleHexOfHexArrayRowIndex,
       "exampleHexOfHexArrayColumnIndex": exampleHexOfHexArrayColumnIndex,
       "exampleHexOfHexArrayValue": exampleHexOfHexArrayValue,
       "exampleHexOfHexReplicatedTable": exampleHexOfHexReplicatedTable,
       "exampleHexOfHexReplicatedEntry": exampleHexOfHexReplicatedEntry,
       "exampleHexOfHexReplicatedIndex": exampleHexOfHexReplicatedIndex,
       "exampleHexOfHexReplicatedValue": exampleHexOfHexReplicatedValue,
       "exampleHexOfHexReplicatedRowStatus": exampleHexOfHexReplicatedRowStatus,
       "exampleHexOfHexListTable": exampleHexOfHexListTable,
       "exampleHexOfHexListEntry": exampleHexOfHexListEntry,
       "exampleHexOfHexListValue": exampleHexOfHexListValue,
       "exampleHexOfHexListRowStatus": exampleHexOfHexListRowStatus,
       "exampleHexProvStructHexVectorTable": exampleHexProvStructHexVectorTable,
       "exampleHexProvStructHexVectorEntry": exampleHexProvStructHexVectorEntry,
       "exampleHexProvStructHexVectorIndex": exampleHexProvStructHexVectorIndex,
       "exampleHexProvStructHexVectorValue": exampleHexProvStructHexVectorValue,
       "exampleHexProvStructHexArrayTable": exampleHexProvStructHexArrayTable,
       "exampleHexProvStructHexArrayEntry": exampleHexProvStructHexArrayEntry,
       "exampleHexProvStructHexArrayRowIndex": exampleHexProvStructHexArrayRowIndex,
       "exampleHexProvStructHexArrayColumnIndex": exampleHexProvStructHexArrayColumnIndex,
       "exampleHexProvStructHexArrayValue": exampleHexProvStructHexArrayValue,
       "exampleHexProvFreeHexVectorTable": exampleHexProvFreeHexVectorTable,
       "exampleHexProvFreeHexVectorEntry": exampleHexProvFreeHexVectorEntry,
       "exampleHexProvFreeHexVectorIndex": exampleHexProvFreeHexVectorIndex,
       "exampleHexProvFreeHexVectorValue": exampleHexProvFreeHexVectorValue,
       "exampleHexProvFreeHexVector1Table": exampleHexProvFreeHexVector1Table,
       "exampleHexProvFreeHexVector1Entry": exampleHexProvFreeHexVector1Entry,
       "exampleHexProvFreeHexVector1Index": exampleHexProvFreeHexVector1Index,
       "exampleHexProvFreeHexVector1Value": exampleHexProvFreeHexVector1Value,
       "exampleHexProvFreeHexVector2Table": exampleHexProvFreeHexVector2Table,
       "exampleHexProvFreeHexVector2Entry": exampleHexProvFreeHexVector2Entry,
       "exampleHexProvFreeHexVector2Index": exampleHexProvFreeHexVector2Index,
       "exampleHexProvFreeHexVector2Value": exampleHexProvFreeHexVector2Value,
       "exampleHexProvFreeHexArrayTable": exampleHexProvFreeHexArrayTable,
       "exampleHexProvFreeHexArrayEntry": exampleHexProvFreeHexArrayEntry,
       "exampleHexProvFreeHexArrayRowIndex": exampleHexProvFreeHexArrayRowIndex,
       "exampleHexProvFreeHexArrayColumnIndex": exampleHexProvFreeHexArrayColumnIndex,
       "exampleHexProvFreeHexArrayValue": exampleHexProvFreeHexArrayValue,
       "exampleHexProvFreeHexArray1Table": exampleHexProvFreeHexArray1Table,
       "exampleHexProvFreeHexArray1Entry": exampleHexProvFreeHexArray1Entry,
       "exampleHexProvFreeHexArray1RowIndex": exampleHexProvFreeHexArray1RowIndex,
       "exampleHexProvFreeHexArray1ColumnIndex": exampleHexProvFreeHexArray1ColumnIndex,
       "exampleHexProvFreeHexArray1Value": exampleHexProvFreeHexArray1Value,
       "exampleHexProvFreeHexArray2Table": exampleHexProvFreeHexArray2Table,
       "exampleHexProvFreeHexArray2Entry": exampleHexProvFreeHexArray2Entry,
       "exampleHexProvFreeHexArray2RowIndex": exampleHexProvFreeHexArray2RowIndex,
       "exampleHexProvFreeHexArray2ColumnIndex": exampleHexProvFreeHexArray2ColumnIndex,
       "exampleHexProvFreeHexArray2Value": exampleHexProvFreeHexArray2Value,
       "exampleHexProvFreeHexReplicatedTable": exampleHexProvFreeHexReplicatedTable,
       "exampleHexProvFreeHexReplicatedEntry": exampleHexProvFreeHexReplicatedEntry,
       "exampleHexProvFreeHexReplicatedIndex": exampleHexProvFreeHexReplicatedIndex,
       "exampleHexProvFreeHexReplicatedValue": exampleHexProvFreeHexReplicatedValue,
       "exampleHexProvFreeHexReplicatedRowStatus": exampleHexProvFreeHexReplicatedRowStatus,
       "exampleHexProvFreeHexReplicated1Table": exampleHexProvFreeHexReplicated1Table,
       "exampleHexProvFreeHexReplicated1Entry": exampleHexProvFreeHexReplicated1Entry,
       "exampleHexProvFreeHexReplicated1Index": exampleHexProvFreeHexReplicated1Index,
       "exampleHexProvFreeHexReplicated1Value": exampleHexProvFreeHexReplicated1Value,
       "exampleHexProvFreeHexReplicated1RowStatus": exampleHexProvFreeHexReplicated1RowStatus,
       "exampleHexProvFreeHexListTable": exampleHexProvFreeHexListTable,
       "exampleHexProvFreeHexListEntry": exampleHexProvFreeHexListEntry,
       "exampleHexProvFreeHexListValue": exampleHexProvFreeHexListValue,
       "exampleHexProvFreeHexListRowStatus": exampleHexProvFreeHexListRowStatus,
       "exampleHexProvFreeHexList1Table": exampleHexProvFreeHexList1Table,
       "exampleHexProvFreeHexList1Entry": exampleHexProvFreeHexList1Entry,
       "exampleHexProvFreeHexList1Value": exampleHexProvFreeHexList1Value,
       "exampleHexProvFreeHexList1RowStatus": exampleHexProvFreeHexList1RowStatus,
       "exampleIpAddress": exampleIpAddress,
       "exampleIpAddressRowStatusTable": exampleIpAddressRowStatusTable,
       "exampleIpAddressRowStatusEntry": exampleIpAddressRowStatusEntry,
       "exampleIpAddressRowStatus": exampleIpAddressRowStatus,
       "exampleIpAddressComponentName": exampleIpAddressComponentName,
       "exampleIpAddressStorageType": exampleIpAddressStorageType,
       "exampleIpAddressIndex": exampleIpAddressIndex,
       "exampleIpAddressOperationalTable": exampleIpAddressOperationalTable,
       "exampleIpAddressOperationalEntry": exampleIpAddressOperationalEntry,
       "exampleIpAddressOperStructIpAddress": exampleIpAddressOperStructIpAddress,
       "exampleIpAddressOperFreeIpAddress": exampleIpAddressOperFreeIpAddress,
       "exampleIpAddressProvisionalTable": exampleIpAddressProvisionalTable,
       "exampleIpAddressProvisionalEntry": exampleIpAddressProvisionalEntry,
       "exampleIpAddressProvEnumSub": exampleIpAddressProvEnumSub,
       "exampleIpAddressProvStructIpAddress": exampleIpAddressProvStructIpAddress,
       "exampleIpAddressProvFreeIpAddress": exampleIpAddressProvFreeIpAddress,
       "exampleIpAddressProvFreeIpAddress1": exampleIpAddressProvFreeIpAddress1,
       "exampleIpAddressOperStructIpAddressVectorTable": exampleIpAddressOperStructIpAddressVectorTable,
       "exampleIpAddressOperStructIpAddressVectorEntry": exampleIpAddressOperStructIpAddressVectorEntry,
       "exampleIpAddressOperStructIpAddressVectorIndex": exampleIpAddressOperStructIpAddressVectorIndex,
       "exampleIpAddressOperStructIpAddressVectorValue": exampleIpAddressOperStructIpAddressVectorValue,
       "exampleIpAddressOperStructIpAddressArrayTable": exampleIpAddressOperStructIpAddressArrayTable,
       "exampleIpAddressOperStructIpAddressArrayEntry": exampleIpAddressOperStructIpAddressArrayEntry,
       "exampleIpAddressOperStructIpAddressArrayRowIndex": exampleIpAddressOperStructIpAddressArrayRowIndex,
       "exampleIpAddressOperStructIpAddressArrayColumnIndex": exampleIpAddressOperStructIpAddressArrayColumnIndex,
       "exampleIpAddressOperStructIpAddressArrayValue": exampleIpAddressOperStructIpAddressArrayValue,
       "exampleIpAddressOperFreeIpAddressVectorTable": exampleIpAddressOperFreeIpAddressVectorTable,
       "exampleIpAddressOperFreeIpAddressVectorEntry": exampleIpAddressOperFreeIpAddressVectorEntry,
       "exampleIpAddressOperFreeIpAddressVectorIndex": exampleIpAddressOperFreeIpAddressVectorIndex,
       "exampleIpAddressOperFreeIpAddressVectorValue": exampleIpAddressOperFreeIpAddressVectorValue,
       "exampleIpAddressOperFreeIpAddressArrayTable": exampleIpAddressOperFreeIpAddressArrayTable,
       "exampleIpAddressOperFreeIpAddressArrayEntry": exampleIpAddressOperFreeIpAddressArrayEntry,
       "exampleIpAddressOperFreeIpAddressArrayRowIndex": exampleIpAddressOperFreeIpAddressArrayRowIndex,
       "exampleIpAddressOperFreeIpAddressArrayColumnIndex": exampleIpAddressOperFreeIpAddressArrayColumnIndex,
       "exampleIpAddressOperFreeIpAddressArrayValue": exampleIpAddressOperFreeIpAddressArrayValue,
       "exampleIpAddressOperFreeIpAddressReplicatedTable": exampleIpAddressOperFreeIpAddressReplicatedTable,
       "exampleIpAddressOperFreeIpAddressReplicatedEntry": exampleIpAddressOperFreeIpAddressReplicatedEntry,
       "exampleIpAddressOperFreeIpAddressReplicatedIndex": exampleIpAddressOperFreeIpAddressReplicatedIndex,
       "exampleIpAddressOperFreeIpAddressReplicatedValue": exampleIpAddressOperFreeIpAddressReplicatedValue,
       "exampleIpAddressOperFreeIpAddressReplicatedRowStatus": exampleIpAddressOperFreeIpAddressReplicatedRowStatus,
       "exampleIpAddressOperFreeIpAddressListTable": exampleIpAddressOperFreeIpAddressListTable,
       "exampleIpAddressOperFreeIpAddressListEntry": exampleIpAddressOperFreeIpAddressListEntry,
       "exampleIpAddressOperFreeIpAddressListValue": exampleIpAddressOperFreeIpAddressListValue,
       "exampleIpAddressOperFreeIpAddressListRowStatus": exampleIpAddressOperFreeIpAddressListRowStatus,
       "exampleIpAddressProvStructIpAddressVectorTable": exampleIpAddressProvStructIpAddressVectorTable,
       "exampleIpAddressProvStructIpAddressVectorEntry": exampleIpAddressProvStructIpAddressVectorEntry,
       "exampleIpAddressProvStructIpAddressVectorIndex": exampleIpAddressProvStructIpAddressVectorIndex,
       "exampleIpAddressProvStructIpAddressVectorValue": exampleIpAddressProvStructIpAddressVectorValue,
       "exampleIpAddressProvStructIpAddressArrayTable": exampleIpAddressProvStructIpAddressArrayTable,
       "exampleIpAddressProvStructIpAddressArrayEntry": exampleIpAddressProvStructIpAddressArrayEntry,
       "exampleIpAddressProvStructIpAddressArrayRowIndex": exampleIpAddressProvStructIpAddressArrayRowIndex,
       "exampleIpAddressProvStructIpAddressArrayColumnIndex": exampleIpAddressProvStructIpAddressArrayColumnIndex,
       "exampleIpAddressProvStructIpAddressArrayValue": exampleIpAddressProvStructIpAddressArrayValue,
       "exampleIpAddressProvFreeIpAddressVectorTable": exampleIpAddressProvFreeIpAddressVectorTable,
       "exampleIpAddressProvFreeIpAddressVectorEntry": exampleIpAddressProvFreeIpAddressVectorEntry,
       "exampleIpAddressProvFreeIpAddressVectorIndex": exampleIpAddressProvFreeIpAddressVectorIndex,
       "exampleIpAddressProvFreeIpAddressVectorValue": exampleIpAddressProvFreeIpAddressVectorValue,
       "exampleIpAddressProvFreeIpAddressVector1Table": exampleIpAddressProvFreeIpAddressVector1Table,
       "exampleIpAddressProvFreeIpAddressVector1Entry": exampleIpAddressProvFreeIpAddressVector1Entry,
       "exampleIpAddressProvFreeIpAddressVector1Index": exampleIpAddressProvFreeIpAddressVector1Index,
       "exampleIpAddressProvFreeIpAddressVector1Value": exampleIpAddressProvFreeIpAddressVector1Value,
       "exampleIpAddressProvFreeIpAddressArrayTable": exampleIpAddressProvFreeIpAddressArrayTable,
       "exampleIpAddressProvFreeIpAddressArrayEntry": exampleIpAddressProvFreeIpAddressArrayEntry,
       "exampleIpAddressProvFreeIpAddressArrayRowIndex": exampleIpAddressProvFreeIpAddressArrayRowIndex,
       "exampleIpAddressProvFreeIpAddressArrayColumnIndex": exampleIpAddressProvFreeIpAddressArrayColumnIndex,
       "exampleIpAddressProvFreeIpAddressArrayValue": exampleIpAddressProvFreeIpAddressArrayValue,
       "exampleIpAddressProvFreeIpAddressArray1Table": exampleIpAddressProvFreeIpAddressArray1Table,
       "exampleIpAddressProvFreeIpAddressArray1Entry": exampleIpAddressProvFreeIpAddressArray1Entry,
       "exampleIpAddressProvFreeIpAddressArray1RowIndex": exampleIpAddressProvFreeIpAddressArray1RowIndex,
       "exampleIpAddressProvFreeIpAddressArray1ColumnIndex": exampleIpAddressProvFreeIpAddressArray1ColumnIndex,
       "exampleIpAddressProvFreeIpAddressArray1Value": exampleIpAddressProvFreeIpAddressArray1Value,
       "exampleIpAddressProvFreeIpAddressReplicatedTable": exampleIpAddressProvFreeIpAddressReplicatedTable,
       "exampleIpAddressProvFreeIpAddressReplicatedEntry": exampleIpAddressProvFreeIpAddressReplicatedEntry,
       "exampleIpAddressProvFreeIpAddressReplicatedIndex": exampleIpAddressProvFreeIpAddressReplicatedIndex,
       "exampleIpAddressProvFreeIpAddressReplicatedValue": exampleIpAddressProvFreeIpAddressReplicatedValue,
       "exampleIpAddressProvFreeIpAddressReplicatedRowStatus": exampleIpAddressProvFreeIpAddressReplicatedRowStatus,
       "exampleIpAddressProvFreeIpAddressListTable": exampleIpAddressProvFreeIpAddressListTable,
       "exampleIpAddressProvFreeIpAddressListEntry": exampleIpAddressProvFreeIpAddressListEntry,
       "exampleIpAddressProvFreeIpAddressListValue": exampleIpAddressProvFreeIpAddressListValue,
       "exampleIpAddressProvFreeIpAddressListRowStatus": exampleIpAddressProvFreeIpAddressListRowStatus,
       "exampleIpAddressProvFreeIpAddressList1Table": exampleIpAddressProvFreeIpAddressList1Table,
       "exampleIpAddressProvFreeIpAddressList1Entry": exampleIpAddressProvFreeIpAddressList1Entry,
       "exampleIpAddressProvFreeIpAddressList1Value": exampleIpAddressProvFreeIpAddressList1Value,
       "exampleIpAddressProvFreeIpAddressList1RowStatus": exampleIpAddressProvFreeIpAddressList1RowStatus,
       "exampleString": exampleString,
       "exampleStringRowStatusTable": exampleStringRowStatusTable,
       "exampleStringRowStatusEntry": exampleStringRowStatusEntry,
       "exampleStringRowStatus": exampleStringRowStatus,
       "exampleStringComponentName": exampleStringComponentName,
       "exampleStringStorageType": exampleStringStorageType,
       "exampleStringIndex": exampleStringIndex,
       "exampleStringOperationalTable": exampleStringOperationalTable,
       "exampleStringOperationalEntry": exampleStringOperationalEntry,
       "exampleStringOperStructAsciiOnly": exampleStringOperStructAsciiOnly,
       "exampleStringOperStructHexOnly": exampleStringOperStructHexOnly,
       "exampleStringOperFreeAsciiOnly": exampleStringOperFreeAsciiOnly,
       "exampleStringOperFreeHexOnly": exampleStringOperFreeHexOnly,
       "exampleStringProvisionalTable": exampleStringProvisionalTable,
       "exampleStringProvisionalEntry": exampleStringProvisionalEntry,
       "exampleStringProvStringSub": exampleStringProvStringSub,
       "exampleStringProvStructAsciiOnly": exampleStringProvStructAsciiOnly,
       "exampleStringProvStructHexOnly": exampleStringProvStructHexOnly,
       "exampleStringProvFreeAsciiOnly": exampleStringProvFreeAsciiOnly,
       "exampleStringProvFreeAsciiOnly1": exampleStringProvFreeAsciiOnly1,
       "exampleStringProvFreeHexOnly": exampleStringProvFreeHexOnly,
       "exampleStringProvFreeHexOnly1": exampleStringProvFreeHexOnly1,
       "exampleStringOperStructStrVectorTable": exampleStringOperStructStrVectorTable,
       "exampleStringOperStructStrVectorEntry": exampleStringOperStructStrVectorEntry,
       "exampleStringOperStructStrVectorIndex": exampleStringOperStructStrVectorIndex,
       "exampleStringOperStructStrVectorValue": exampleStringOperStructStrVectorValue,
       "exampleStringOperStructStrArrayTable": exampleStringOperStructStrArrayTable,
       "exampleStringOperStructStrArrayEntry": exampleStringOperStructStrArrayEntry,
       "exampleStringOperStructStrArrayRowIndex": exampleStringOperStructStrArrayRowIndex,
       "exampleStringOperStructStrArrayColumnIndex": exampleStringOperStructStrArrayColumnIndex,
       "exampleStringOperStructStrArrayValue": exampleStringOperStructStrArrayValue,
       "exampleStringOperFreeStrVectorTable": exampleStringOperFreeStrVectorTable,
       "exampleStringOperFreeStrVectorEntry": exampleStringOperFreeStrVectorEntry,
       "exampleStringOperFreeStrVectorIndex": exampleStringOperFreeStrVectorIndex,
       "exampleStringOperFreeStrVectorValue": exampleStringOperFreeStrVectorValue,
       "exampleStringOperFreeStrArrayTable": exampleStringOperFreeStrArrayTable,
       "exampleStringOperFreeStrArrayEntry": exampleStringOperFreeStrArrayEntry,
       "exampleStringOperFreeStrArrayRowIndex": exampleStringOperFreeStrArrayRowIndex,
       "exampleStringOperFreeStrArrayColumnIndex": exampleStringOperFreeStrArrayColumnIndex,
       "exampleStringOperFreeStrArrayValue": exampleStringOperFreeStrArrayValue,
       "exampleStringOperFreeStrReplicatedTable": exampleStringOperFreeStrReplicatedTable,
       "exampleStringOperFreeStrReplicatedEntry": exampleStringOperFreeStrReplicatedEntry,
       "exampleStringOperFreeStrReplicatedIndex": exampleStringOperFreeStrReplicatedIndex,
       "exampleStringOperFreeStrReplicatedValue": exampleStringOperFreeStrReplicatedValue,
       "exampleStringOperFreeStrReplicatedRowStatus": exampleStringOperFreeStrReplicatedRowStatus,
       "exampleStringOperFreeStrListTable": exampleStringOperFreeStrListTable,
       "exampleStringOperFreeStrListEntry": exampleStringOperFreeStrListEntry,
       "exampleStringOperFreeStrListValue": exampleStringOperFreeStrListValue,
       "exampleStringOperFreeStrListRowStatus": exampleStringOperFreeStrListRowStatus,
       "exampleStringProvStructStrVectorTable": exampleStringProvStructStrVectorTable,
       "exampleStringProvStructStrVectorEntry": exampleStringProvStructStrVectorEntry,
       "exampleStringProvStructStrVectorIndex": exampleStringProvStructStrVectorIndex,
       "exampleStringProvStructStrVectorValue": exampleStringProvStructStrVectorValue,
       "exampleStringProvStructStrArrayTable": exampleStringProvStructStrArrayTable,
       "exampleStringProvStructStrArrayEntry": exampleStringProvStructStrArrayEntry,
       "exampleStringProvStructStrArrayRowIndex": exampleStringProvStructStrArrayRowIndex,
       "exampleStringProvStructStrArrayColumnIndex": exampleStringProvStructStrArrayColumnIndex,
       "exampleStringProvStructStrArrayValue": exampleStringProvStructStrArrayValue,
       "exampleStringProvFreeStrVectorTable": exampleStringProvFreeStrVectorTable,
       "exampleStringProvFreeStrVectorEntry": exampleStringProvFreeStrVectorEntry,
       "exampleStringProvFreeStrVectorIndex": exampleStringProvFreeStrVectorIndex,
       "exampleStringProvFreeStrVectorValue": exampleStringProvFreeStrVectorValue,
       "exampleStringProvFreeStrVector1Table": exampleStringProvFreeStrVector1Table,
       "exampleStringProvFreeStrVector1Entry": exampleStringProvFreeStrVector1Entry,
       "exampleStringProvFreeStrVector1Index": exampleStringProvFreeStrVector1Index,
       "exampleStringProvFreeStrVector1Value": exampleStringProvFreeStrVector1Value,
       "exampleStringProvFreeStrArrayTable": exampleStringProvFreeStrArrayTable,
       "exampleStringProvFreeStrArrayEntry": exampleStringProvFreeStrArrayEntry,
       "exampleStringProvFreeStrArrayRowIndex": exampleStringProvFreeStrArrayRowIndex,
       "exampleStringProvFreeStrArrayColumnIndex": exampleStringProvFreeStrArrayColumnIndex,
       "exampleStringProvFreeStrArrayValue": exampleStringProvFreeStrArrayValue,
       "exampleStringProvFreeStrArray1Table": exampleStringProvFreeStrArray1Table,
       "exampleStringProvFreeStrArray1Entry": exampleStringProvFreeStrArray1Entry,
       "exampleStringProvFreeStrArray1RowIndex": exampleStringProvFreeStrArray1RowIndex,
       "exampleStringProvFreeStrArray1ColumnIndex": exampleStringProvFreeStrArray1ColumnIndex,
       "exampleStringProvFreeStrArray1Value": exampleStringProvFreeStrArray1Value,
       "exampleStringProvFreeStrReplicatedTable": exampleStringProvFreeStrReplicatedTable,
       "exampleStringProvFreeStrReplicatedEntry": exampleStringProvFreeStrReplicatedEntry,
       "exampleStringProvFreeStrReplicatedIndex": exampleStringProvFreeStrReplicatedIndex,
       "exampleStringProvFreeStrReplicatedValue": exampleStringProvFreeStrReplicatedValue,
       "exampleStringProvFreeStrReplicatedRowStatus": exampleStringProvFreeStrReplicatedRowStatus,
       "exampleStringProvFreeStrListTable": exampleStringProvFreeStrListTable,
       "exampleStringProvFreeStrListEntry": exampleStringProvFreeStrListEntry,
       "exampleStringProvFreeStrListValue": exampleStringProvFreeStrListValue,
       "exampleStringProvFreeStrListRowStatus": exampleStringProvFreeStrListRowStatus,
       "exampleStringProvFreeStrList1Table": exampleStringProvFreeStrList1Table,
       "exampleStringProvFreeStrList1Entry": exampleStringProvFreeStrList1Entry,
       "exampleStringProvFreeStrList1Value": exampleStringProvFreeStrList1Value,
       "exampleStringProvFreeStrList1RowStatus": exampleStringProvFreeStrList1RowStatus,
       "exampleFixedPt": exampleFixedPt,
       "exampleFixedPtRowStatusTable": exampleFixedPtRowStatusTable,
       "exampleFixedPtRowStatusEntry": exampleFixedPtRowStatusEntry,
       "exampleFixedPtRowStatus": exampleFixedPtRowStatus,
       "exampleFixedPtComponentName": exampleFixedPtComponentName,
       "exampleFixedPtStorageType": exampleFixedPtStorageType,
       "exampleFixedPtIndex": exampleFixedPtIndex,
       "exampleFixedPtOperationalTable": exampleFixedPtOperationalTable,
       "exampleFixedPtOperationalEntry": exampleFixedPtOperationalEntry,
       "exampleFixedPtOperStructFixedPt": exampleFixedPtOperStructFixedPt,
       "exampleFixedPtOperFreeFixedPt": exampleFixedPtOperFreeFixedPt,
       "exampleFixedPtOperFreeFixedPtSet": exampleFixedPtOperFreeFixedPtSet,
       "exampleFixedPtProvisionalTable": exampleFixedPtProvisionalTable,
       "exampleFixedPtProvisionalEntry": exampleFixedPtProvisionalEntry,
       "exampleFixedPtProvFixedPtSubcomponent": exampleFixedPtProvFixedPtSubcomponent,
       "exampleFixedPtProvStructFixedPt": exampleFixedPtProvStructFixedPt,
       "exampleFixedPtProvStructFixedPtSet": exampleFixedPtProvStructFixedPtSet,
       "exampleFixedPtProvFreeFixedPt": exampleFixedPtProvFreeFixedPt,
       "exampleFixedPtProvFreeFixedPtSet": exampleFixedPtProvFreeFixedPtSet,
       "exampleFixedPtOperStructFixedPtVectorTable": exampleFixedPtOperStructFixedPtVectorTable,
       "exampleFixedPtOperStructFixedPtVectorEntry": exampleFixedPtOperStructFixedPtVectorEntry,
       "exampleFixedPtOperStructFixedPtVectorIndex": exampleFixedPtOperStructFixedPtVectorIndex,
       "exampleFixedPtOperStructFixedPtVectorValue": exampleFixedPtOperStructFixedPtVectorValue,
       "exampleFixedPtOperStructFixedPtArrayTable": exampleFixedPtOperStructFixedPtArrayTable,
       "exampleFixedPtOperStructFixedPtArrayEntry": exampleFixedPtOperStructFixedPtArrayEntry,
       "exampleFixedPtOperStructFixedPtArrayRowIndex": exampleFixedPtOperStructFixedPtArrayRowIndex,
       "exampleFixedPtOperStructFixedPtArrayColumnIndex": exampleFixedPtOperStructFixedPtArrayColumnIndex,
       "exampleFixedPtOperStructFixedPtArrayValue": exampleFixedPtOperStructFixedPtArrayValue,
       "exampleFixedPtOperFreeFixedPtVectorTable": exampleFixedPtOperFreeFixedPtVectorTable,
       "exampleFixedPtOperFreeFixedPtVectorEntry": exampleFixedPtOperFreeFixedPtVectorEntry,
       "exampleFixedPtOperFreeFixedPtVectorIndex": exampleFixedPtOperFreeFixedPtVectorIndex,
       "exampleFixedPtOperFreeFixedPtVectorValue": exampleFixedPtOperFreeFixedPtVectorValue,
       "exampleFixedPtOperFreeFixedPtArrayTable": exampleFixedPtOperFreeFixedPtArrayTable,
       "exampleFixedPtOperFreeFixedPtArrayEntry": exampleFixedPtOperFreeFixedPtArrayEntry,
       "exampleFixedPtOperFreeFixedPtArrayRowIndex": exampleFixedPtOperFreeFixedPtArrayRowIndex,
       "exampleFixedPtOperFreeFixedPtArrayColumnIndex": exampleFixedPtOperFreeFixedPtArrayColumnIndex,
       "exampleFixedPtOperFreeFixedPtArrayValue": exampleFixedPtOperFreeFixedPtArrayValue,
       "exampleFixedPtOperFreeFixedPtReplicatedTable": exampleFixedPtOperFreeFixedPtReplicatedTable,
       "exampleFixedPtOperFreeFixedPtReplicatedEntry": exampleFixedPtOperFreeFixedPtReplicatedEntry,
       "exampleFixedPtOperFreeFixedPtReplicatedIndex": exampleFixedPtOperFreeFixedPtReplicatedIndex,
       "exampleFixedPtOperFreeFixedPtReplicatedValue": exampleFixedPtOperFreeFixedPtReplicatedValue,
       "exampleFixedPtOperFreeFixedPtReplicatedRowStatus": exampleFixedPtOperFreeFixedPtReplicatedRowStatus,
       "exampleFixedPtOperFreeFixedPtListTable": exampleFixedPtOperFreeFixedPtListTable,
       "exampleFixedPtOperFreeFixedPtListEntry": exampleFixedPtOperFreeFixedPtListEntry,
       "exampleFixedPtOperFreeFixedPtListValue": exampleFixedPtOperFreeFixedPtListValue,
       "exampleFixedPtOperFreeFixedPtListRowStatus": exampleFixedPtOperFreeFixedPtListRowStatus,
       "exampleFixedPtProvStructFixedPtVectorTable": exampleFixedPtProvStructFixedPtVectorTable,
       "exampleFixedPtProvStructFixedPtVectorEntry": exampleFixedPtProvStructFixedPtVectorEntry,
       "exampleFixedPtProvStructFixedPtVectorIndex": exampleFixedPtProvStructFixedPtVectorIndex,
       "exampleFixedPtProvStructFixedPtVectorValue": exampleFixedPtProvStructFixedPtVectorValue,
       "exampleFixedPtProvStructFixedPtArrayTable": exampleFixedPtProvStructFixedPtArrayTable,
       "exampleFixedPtProvStructFixedPtArrayEntry": exampleFixedPtProvStructFixedPtArrayEntry,
       "exampleFixedPtProvStructFixedPtArrayRowIndex": exampleFixedPtProvStructFixedPtArrayRowIndex,
       "exampleFixedPtProvStructFixedPtArrayColumnIndex": exampleFixedPtProvStructFixedPtArrayColumnIndex,
       "exampleFixedPtProvStructFixedPtArrayValue": exampleFixedPtProvStructFixedPtArrayValue,
       "exampleFixedPtProvFreeFixedPtVectorTable": exampleFixedPtProvFreeFixedPtVectorTable,
       "exampleFixedPtProvFreeFixedPtVectorEntry": exampleFixedPtProvFreeFixedPtVectorEntry,
       "exampleFixedPtProvFreeFixedPtVectorIndex": exampleFixedPtProvFreeFixedPtVectorIndex,
       "exampleFixedPtProvFreeFixedPtVectorValue": exampleFixedPtProvFreeFixedPtVectorValue,
       "exampleFixedPtProvFreeFixedPtArrayTable": exampleFixedPtProvFreeFixedPtArrayTable,
       "exampleFixedPtProvFreeFixedPtArrayEntry": exampleFixedPtProvFreeFixedPtArrayEntry,
       "exampleFixedPtProvFreeFixedPtArrayRowIndex": exampleFixedPtProvFreeFixedPtArrayRowIndex,
       "exampleFixedPtProvFreeFixedPtArrayColumnIndex": exampleFixedPtProvFreeFixedPtArrayColumnIndex,
       "exampleFixedPtProvFreeFixedPtArrayValue": exampleFixedPtProvFreeFixedPtArrayValue,
       "exampleFixedPtProvFreeFixedPtReplicatedTable": exampleFixedPtProvFreeFixedPtReplicatedTable,
       "exampleFixedPtProvFreeFixedPtReplicatedEntry": exampleFixedPtProvFreeFixedPtReplicatedEntry,
       "exampleFixedPtProvFreeFixedPtReplicatedIndex": exampleFixedPtProvFreeFixedPtReplicatedIndex,
       "exampleFixedPtProvFreeFixedPtReplicatedValue": exampleFixedPtProvFreeFixedPtReplicatedValue,
       "exampleFixedPtProvFreeFixedPtReplicatedRowStatus": exampleFixedPtProvFreeFixedPtReplicatedRowStatus,
       "exampleFixedPtProvFreeFixedPtListTable": exampleFixedPtProvFreeFixedPtListTable,
       "exampleFixedPtProvFreeFixedPtListEntry": exampleFixedPtProvFreeFixedPtListEntry,
       "exampleFixedPtProvFreeFixedPtListValue": exampleFixedPtProvFreeFixedPtListValue,
       "exampleFixedPtProvFreeFixedPtListRowStatus": exampleFixedPtProvFreeFixedPtListRowStatus,
       "exampleDashed": exampleDashed,
       "exampleDashedRowStatusTable": exampleDashedRowStatusTable,
       "exampleDashedRowStatusEntry": exampleDashedRowStatusEntry,
       "exampleDashedRowStatus": exampleDashedRowStatus,
       "exampleDashedComponentName": exampleDashedComponentName,
       "exampleDashedStorageType": exampleDashedStorageType,
       "exampleDashedIndex": exampleDashedIndex,
       "exampleDashedOperationalTable": exampleDashedOperationalTable,
       "exampleDashedOperationalEntry": exampleDashedOperationalEntry,
       "exampleDashedOperStructDashed": exampleDashedOperStructDashed,
       "exampleDashedOperFreeDashed": exampleDashedOperFreeDashed,
       "exampleDashedProvisionalTable": exampleDashedProvisionalTable,
       "exampleDashedProvisionalEntry": exampleDashedProvisionalEntry,
       "exampleDashedProvStructDashed": exampleDashedProvStructDashed,
       "exampleDashedProvFreeDashed": exampleDashedProvFreeDashed,
       "exampleDashedOsDashedArrayTable": exampleDashedOsDashedArrayTable,
       "exampleDashedOsDashedArrayEntry": exampleDashedOsDashedArrayEntry,
       "exampleDashedOsDashedArrayRowIndex": exampleDashedOsDashedArrayRowIndex,
       "exampleDashedOsDashedArrayColumnIndex": exampleDashedOsDashedArrayColumnIndex,
       "exampleDashedOsDashedArrayValue": exampleDashedOsDashedArrayValue,
       "exampleDashedOsDashedVectorTable": exampleDashedOsDashedVectorTable,
       "exampleDashedOsDashedVectorEntry": exampleDashedOsDashedVectorEntry,
       "exampleDashedOsDashedVectorIndex": exampleDashedOsDashedVectorIndex,
       "exampleDashedOsDashedVectorValue": exampleDashedOsDashedVectorValue,
       "exampleDashedOfDashedListTable": exampleDashedOfDashedListTable,
       "exampleDashedOfDashedListEntry": exampleDashedOfDashedListEntry,
       "exampleDashedOfDashedListValue": exampleDashedOfDashedListValue,
       "exampleDashedOfDashedListRowStatus": exampleDashedOfDashedListRowStatus,
       "exampleDashedOfDashedReplicatedTable": exampleDashedOfDashedReplicatedTable,
       "exampleDashedOfDashedReplicatedEntry": exampleDashedOfDashedReplicatedEntry,
       "exampleDashedOfDashedReplicatedIndex": exampleDashedOfDashedReplicatedIndex,
       "exampleDashedOfDashedReplicatedValue": exampleDashedOfDashedReplicatedValue,
       "exampleDashedOfDashedReplicatedRowStatus": exampleDashedOfDashedReplicatedRowStatus,
       "exampleDashedOfDashedArrayTable": exampleDashedOfDashedArrayTable,
       "exampleDashedOfDashedArrayEntry": exampleDashedOfDashedArrayEntry,
       "exampleDashedOfDashedArrayRowIndex": exampleDashedOfDashedArrayRowIndex,
       "exampleDashedOfDashedArrayColumnIndex": exampleDashedOfDashedArrayColumnIndex,
       "exampleDashedOfDashedArrayValue": exampleDashedOfDashedArrayValue,
       "exampleDashedOfDashedVectorTable": exampleDashedOfDashedVectorTable,
       "exampleDashedOfDashedVectorEntry": exampleDashedOfDashedVectorEntry,
       "exampleDashedOfDashedVectorIndex": exampleDashedOfDashedVectorIndex,
       "exampleDashedOfDashedVectorValue": exampleDashedOfDashedVectorValue,
       "exampleDashedProvStructDashedArrayTable": exampleDashedProvStructDashedArrayTable,
       "exampleDashedProvStructDashedArrayEntry": exampleDashedProvStructDashedArrayEntry,
       "exampleDashedProvStructDashedArrayRowIndex": exampleDashedProvStructDashedArrayRowIndex,
       "exampleDashedProvStructDashedArrayColumnIndex": exampleDashedProvStructDashedArrayColumnIndex,
       "exampleDashedProvStructDashedArrayValue": exampleDashedProvStructDashedArrayValue,
       "exampleDashedProvStructDashedVectorTable": exampleDashedProvStructDashedVectorTable,
       "exampleDashedProvStructDashedVectorEntry": exampleDashedProvStructDashedVectorEntry,
       "exampleDashedProvStructDashedVectorIndex": exampleDashedProvStructDashedVectorIndex,
       "exampleDashedProvStructDashedVectorValue": exampleDashedProvStructDashedVectorValue,
       "exampleDashedProvFreeDashedListTable": exampleDashedProvFreeDashedListTable,
       "exampleDashedProvFreeDashedListEntry": exampleDashedProvFreeDashedListEntry,
       "exampleDashedProvFreeDashedListValue": exampleDashedProvFreeDashedListValue,
       "exampleDashedProvFreeDashedListRowStatus": exampleDashedProvFreeDashedListRowStatus,
       "exampleDashedProvFreeDashedReplicatedTable": exampleDashedProvFreeDashedReplicatedTable,
       "exampleDashedProvFreeDashedReplicatedEntry": exampleDashedProvFreeDashedReplicatedEntry,
       "exampleDashedProvFreeDashedReplicatedIndex": exampleDashedProvFreeDashedReplicatedIndex,
       "exampleDashedProvFreeDashedReplicatedValue": exampleDashedProvFreeDashedReplicatedValue,
       "exampleDashedProvFreeDashedReplicatedRowStatus": exampleDashedProvFreeDashedReplicatedRowStatus,
       "exampleDashedProvFreeDashedArrayTable": exampleDashedProvFreeDashedArrayTable,
       "exampleDashedProvFreeDashedArrayEntry": exampleDashedProvFreeDashedArrayEntry,
       "exampleDashedProvFreeDashedArrayRowIndex": exampleDashedProvFreeDashedArrayRowIndex,
       "exampleDashedProvFreeDashedArrayColumnIndex": exampleDashedProvFreeDashedArrayColumnIndex,
       "exampleDashedProvFreeDashedArrayValue": exampleDashedProvFreeDashedArrayValue,
       "exampleDashedProvFreeDashedVectorTable": exampleDashedProvFreeDashedVectorTable,
       "exampleDashedProvFreeDashedVectorEntry": exampleDashedProvFreeDashedVectorEntry,
       "exampleDashedProvFreeDashedVectorIndex": exampleDashedProvFreeDashedVectorIndex,
       "exampleDashedProvFreeDashedVectorValue": exampleDashedProvFreeDashedVectorValue,
       "exampleExtended": exampleExtended,
       "exampleExtendedRowStatusTable": exampleExtendedRowStatusTable,
       "exampleExtendedRowStatusEntry": exampleExtendedRowStatusEntry,
       "exampleExtendedRowStatus": exampleExtendedRowStatus,
       "exampleExtendedComponentName": exampleExtendedComponentName,
       "exampleExtendedStorageType": exampleExtendedStorageType,
       "exampleExtendedIndex": exampleExtendedIndex,
       "exampleExtendedOperationalTable": exampleExtendedOperationalTable,
       "exampleExtendedOperationalEntry": exampleExtendedOperationalEntry,
       "exampleExtendedOperStructExtended": exampleExtendedOperStructExtended,
       "exampleExtendedOperFreeExtended": exampleExtendedOperFreeExtended,
       "exampleExtendedProvisionalTable": exampleExtendedProvisionalTable,
       "exampleExtendedProvisionalEntry": exampleExtendedProvisionalEntry,
       "exampleExtendedProvEnumSub": exampleExtendedProvEnumSub,
       "exampleExtendedProvStructExtended": exampleExtendedProvStructExtended,
       "exampleExtendedProvFreeExtended": exampleExtendedProvFreeExtended,
       "exampleExtendedOperStructExtendedArrayTable": exampleExtendedOperStructExtendedArrayTable,
       "exampleExtendedOperStructExtendedArrayEntry": exampleExtendedOperStructExtendedArrayEntry,
       "exampleExtendedOperStructExtendedArrayRowIndex": exampleExtendedOperStructExtendedArrayRowIndex,
       "exampleExtendedOperStructExtendedArrayColumnIndex": exampleExtendedOperStructExtendedArrayColumnIndex,
       "exampleExtendedOperStructExtendedArrayValue": exampleExtendedOperStructExtendedArrayValue,
       "exampleExtendedOperStructExtendedVectorTable": exampleExtendedOperStructExtendedVectorTable,
       "exampleExtendedOperStructExtendedVectorEntry": exampleExtendedOperStructExtendedVectorEntry,
       "exampleExtendedOperStructExtendedVectorIndex": exampleExtendedOperStructExtendedVectorIndex,
       "exampleExtendedOperStructExtendedVectorValue": exampleExtendedOperStructExtendedVectorValue,
       "exampleExtendedOperFreeExtendedListTable": exampleExtendedOperFreeExtendedListTable,
       "exampleExtendedOperFreeExtendedListEntry": exampleExtendedOperFreeExtendedListEntry,
       "exampleExtendedOperFreeExtendedListValue": exampleExtendedOperFreeExtendedListValue,
       "exampleExtendedOperFreeExtendedListRowStatus": exampleExtendedOperFreeExtendedListRowStatus,
       "exampleExtendedOperFreeExtendedReplicatedTable": exampleExtendedOperFreeExtendedReplicatedTable,
       "exampleExtendedOperFreeExtendedReplicatedEntry": exampleExtendedOperFreeExtendedReplicatedEntry,
       "exampleExtendedOperFreeExtendedReplicatedIndex": exampleExtendedOperFreeExtendedReplicatedIndex,
       "exampleExtendedOperFreeExtendedReplicatedValue": exampleExtendedOperFreeExtendedReplicatedValue,
       "exampleExtendedOperFreeExtendedReplicatedRowStatus": exampleExtendedOperFreeExtendedReplicatedRowStatus,
       "exampleExtendedOperFreeExtendedArrayTable": exampleExtendedOperFreeExtendedArrayTable,
       "exampleExtendedOperFreeExtendedArrayEntry": exampleExtendedOperFreeExtendedArrayEntry,
       "exampleExtendedOperFreeExtendedArrayRowIndex": exampleExtendedOperFreeExtendedArrayRowIndex,
       "exampleExtendedOperFreeExtendedArrayColumnIndex": exampleExtendedOperFreeExtendedArrayColumnIndex,
       "exampleExtendedOperFreeExtendedArrayValue": exampleExtendedOperFreeExtendedArrayValue,
       "exampleExtendedOperFreeExtendedVectorTable": exampleExtendedOperFreeExtendedVectorTable,
       "exampleExtendedOperFreeExtendedVectorEntry": exampleExtendedOperFreeExtendedVectorEntry,
       "exampleExtendedOperFreeExtendedVectorIndex": exampleExtendedOperFreeExtendedVectorIndex,
       "exampleExtendedOperFreeExtendedVectorValue": exampleExtendedOperFreeExtendedVectorValue,
       "exampleExtendedProvStructExtendedArrayTable": exampleExtendedProvStructExtendedArrayTable,
       "exampleExtendedProvStructExtendedArrayEntry": exampleExtendedProvStructExtendedArrayEntry,
       "exampleExtendedProvStructExtendedArrayRowIndex": exampleExtendedProvStructExtendedArrayRowIndex,
       "exampleExtendedProvStructExtendedArrayColumnIndex": exampleExtendedProvStructExtendedArrayColumnIndex,
       "exampleExtendedProvStructExtendedArrayValue": exampleExtendedProvStructExtendedArrayValue,
       "exampleExtendedProvStructExtendedVectorTable": exampleExtendedProvStructExtendedVectorTable,
       "exampleExtendedProvStructExtendedVectorEntry": exampleExtendedProvStructExtendedVectorEntry,
       "exampleExtendedProvStructExtendedVectorIndex": exampleExtendedProvStructExtendedVectorIndex,
       "exampleExtendedProvStructExtendedVectorValue": exampleExtendedProvStructExtendedVectorValue,
       "exampleExtendedProvFreeExtendedListTable": exampleExtendedProvFreeExtendedListTable,
       "exampleExtendedProvFreeExtendedListEntry": exampleExtendedProvFreeExtendedListEntry,
       "exampleExtendedProvFreeExtendedListValue": exampleExtendedProvFreeExtendedListValue,
       "exampleExtendedProvFreeExtendedListRowStatus": exampleExtendedProvFreeExtendedListRowStatus,
       "exampleExtendedProvFreeExtendedReplicatedTable": exampleExtendedProvFreeExtendedReplicatedTable,
       "exampleExtendedProvFreeExtendedReplicatedEntry": exampleExtendedProvFreeExtendedReplicatedEntry,
       "exampleExtendedProvFreeExtendedReplicatedIndex": exampleExtendedProvFreeExtendedReplicatedIndex,
       "exampleExtendedProvFreeExtendedReplicatedValue": exampleExtendedProvFreeExtendedReplicatedValue,
       "exampleExtendedProvFreeExtendedReplicatedRowStatus": exampleExtendedProvFreeExtendedReplicatedRowStatus,
       "exampleExtendedProvFreeExtendedArrayTable": exampleExtendedProvFreeExtendedArrayTable,
       "exampleExtendedProvFreeExtendedArrayEntry": exampleExtendedProvFreeExtendedArrayEntry,
       "exampleExtendedProvFreeExtendedArrayRowIndex": exampleExtendedProvFreeExtendedArrayRowIndex,
       "exampleExtendedProvFreeExtendedArrayColumnIndex": exampleExtendedProvFreeExtendedArrayColumnIndex,
       "exampleExtendedProvFreeExtendedArrayValue": exampleExtendedProvFreeExtendedArrayValue,
       "exampleExtendedProvFreeExtendedVectorTable": exampleExtendedProvFreeExtendedVectorTable,
       "exampleExtendedProvFreeExtendedVectorEntry": exampleExtendedProvFreeExtendedVectorEntry,
       "exampleExtendedProvFreeExtendedVectorIndex": exampleExtendedProvFreeExtendedVectorIndex,
       "exampleExtendedProvFreeExtendedVectorValue": exampleExtendedProvFreeExtendedVectorValue,
       "exampleBcd": exampleBcd,
       "exampleBcdRowStatusTable": exampleBcdRowStatusTable,
       "exampleBcdRowStatusEntry": exampleBcdRowStatusEntry,
       "exampleBcdRowStatus": exampleBcdRowStatus,
       "exampleBcdComponentName": exampleBcdComponentName,
       "exampleBcdStorageType": exampleBcdStorageType,
       "exampleBcdIndex": exampleBcdIndex,
       "exampleBcdOperationalTable": exampleBcdOperationalTable,
       "exampleBcdOperationalEntry": exampleBcdOperationalEntry,
       "exampleBcdOperStructBcd": exampleBcdOperStructBcd,
       "exampleBcdOperFreeBcd": exampleBcdOperFreeBcd,
       "exampleBcdProvisionalTable": exampleBcdProvisionalTable,
       "exampleBcdProvisionalEntry": exampleBcdProvisionalEntry,
       "exampleBcdProvEnumSub": exampleBcdProvEnumSub,
       "exampleBcdProvStructBcd": exampleBcdProvStructBcd,
       "exampleBcdProvFreeBcd": exampleBcdProvFreeBcd,
       "exampleBcdProvFreeBcd1": exampleBcdProvFreeBcd1,
       "exampleBcdOperStructBcdVectorTable": exampleBcdOperStructBcdVectorTable,
       "exampleBcdOperStructBcdVectorEntry": exampleBcdOperStructBcdVectorEntry,
       "exampleBcdOperStructBcdVectorIndex": exampleBcdOperStructBcdVectorIndex,
       "exampleBcdOperStructBcdVectorValue": exampleBcdOperStructBcdVectorValue,
       "exampleBcdOperStructBcdArrayTable": exampleBcdOperStructBcdArrayTable,
       "exampleBcdOperStructBcdArrayEntry": exampleBcdOperStructBcdArrayEntry,
       "exampleBcdOperStructBcdArrayRowIndex": exampleBcdOperStructBcdArrayRowIndex,
       "exampleBcdOperStructBcdArrayColumnIndex": exampleBcdOperStructBcdArrayColumnIndex,
       "exampleBcdOperStructBcdArrayValue": exampleBcdOperStructBcdArrayValue,
       "exampleBcdOperFreeBcdVectorTable": exampleBcdOperFreeBcdVectorTable,
       "exampleBcdOperFreeBcdVectorEntry": exampleBcdOperFreeBcdVectorEntry,
       "exampleBcdOperFreeBcdVectorIndex": exampleBcdOperFreeBcdVectorIndex,
       "exampleBcdOperFreeBcdVectorValue": exampleBcdOperFreeBcdVectorValue,
       "exampleBcdOperFreeBcdArrayTable": exampleBcdOperFreeBcdArrayTable,
       "exampleBcdOperFreeBcdArrayEntry": exampleBcdOperFreeBcdArrayEntry,
       "exampleBcdOperFreeBcdArrayRowIndex": exampleBcdOperFreeBcdArrayRowIndex,
       "exampleBcdOperFreeBcdArrayColumnIndex": exampleBcdOperFreeBcdArrayColumnIndex,
       "exampleBcdOperFreeBcdArrayValue": exampleBcdOperFreeBcdArrayValue,
       "exampleBcdOperFreeBcdReplicatedTable": exampleBcdOperFreeBcdReplicatedTable,
       "exampleBcdOperFreeBcdReplicatedEntry": exampleBcdOperFreeBcdReplicatedEntry,
       "exampleBcdOperFreeBcdReplicatedIndex": exampleBcdOperFreeBcdReplicatedIndex,
       "exampleBcdOperFreeBcdReplicatedValue": exampleBcdOperFreeBcdReplicatedValue,
       "exampleBcdOperFreeBcdReplicatedRowStatus": exampleBcdOperFreeBcdReplicatedRowStatus,
       "exampleBcdOperFreeBcdListTable": exampleBcdOperFreeBcdListTable,
       "exampleBcdOperFreeBcdListEntry": exampleBcdOperFreeBcdListEntry,
       "exampleBcdOperFreeBcdListValue": exampleBcdOperFreeBcdListValue,
       "exampleBcdOperFreeBcdListRowStatus": exampleBcdOperFreeBcdListRowStatus,
       "exampleBcdProvStructBcdVectorTable": exampleBcdProvStructBcdVectorTable,
       "exampleBcdProvStructBcdVectorEntry": exampleBcdProvStructBcdVectorEntry,
       "exampleBcdProvStructBcdVectorIndex": exampleBcdProvStructBcdVectorIndex,
       "exampleBcdProvStructBcdVectorValue": exampleBcdProvStructBcdVectorValue,
       "exampleBcdProvStructBcdArrayTable": exampleBcdProvStructBcdArrayTable,
       "exampleBcdProvStructBcdArrayEntry": exampleBcdProvStructBcdArrayEntry,
       "exampleBcdProvStructBcdArrayRowIndex": exampleBcdProvStructBcdArrayRowIndex,
       "exampleBcdProvStructBcdArrayColumnIndex": exampleBcdProvStructBcdArrayColumnIndex,
       "exampleBcdProvStructBcdArrayValue": exampleBcdProvStructBcdArrayValue,
       "exampleBcdProvFreeBcdVectorTable": exampleBcdProvFreeBcdVectorTable,
       "exampleBcdProvFreeBcdVectorEntry": exampleBcdProvFreeBcdVectorEntry,
       "exampleBcdProvFreeBcdVectorIndex": exampleBcdProvFreeBcdVectorIndex,
       "exampleBcdProvFreeBcdVectorValue": exampleBcdProvFreeBcdVectorValue,
       "exampleBcdProvFreeBcdVector1Table": exampleBcdProvFreeBcdVector1Table,
       "exampleBcdProvFreeBcdVector1Entry": exampleBcdProvFreeBcdVector1Entry,
       "exampleBcdProvFreeBcdVector1Index": exampleBcdProvFreeBcdVector1Index,
       "exampleBcdProvFreeBcdVector1Value": exampleBcdProvFreeBcdVector1Value,
       "exampleBcdProvFreeBcdArrayTable": exampleBcdProvFreeBcdArrayTable,
       "exampleBcdProvFreeBcdArrayEntry": exampleBcdProvFreeBcdArrayEntry,
       "exampleBcdProvFreeBcdArrayRowIndex": exampleBcdProvFreeBcdArrayRowIndex,
       "exampleBcdProvFreeBcdArrayColumnIndex": exampleBcdProvFreeBcdArrayColumnIndex,
       "exampleBcdProvFreeBcdArrayValue": exampleBcdProvFreeBcdArrayValue,
       "exampleBcdProvFreeBcdArray1Table": exampleBcdProvFreeBcdArray1Table,
       "exampleBcdProvFreeBcdArray1Entry": exampleBcdProvFreeBcdArray1Entry,
       "exampleBcdProvFreeBcdArray1RowIndex": exampleBcdProvFreeBcdArray1RowIndex,
       "exampleBcdProvFreeBcdArray1ColumnIndex": exampleBcdProvFreeBcdArray1ColumnIndex,
       "exampleBcdProvFreeBcdArray1Value": exampleBcdProvFreeBcdArray1Value,
       "exampleBcdProvFreeBcdReplicatedTable": exampleBcdProvFreeBcdReplicatedTable,
       "exampleBcdProvFreeBcdReplicatedEntry": exampleBcdProvFreeBcdReplicatedEntry,
       "exampleBcdProvFreeBcdReplicatedIndex": exampleBcdProvFreeBcdReplicatedIndex,
       "exampleBcdProvFreeBcdReplicatedValue": exampleBcdProvFreeBcdReplicatedValue,
       "exampleBcdProvFreeBcdReplicatedRowStatus": exampleBcdProvFreeBcdReplicatedRowStatus,
       "exampleBcdProvFreeBcdReplicated1Table": exampleBcdProvFreeBcdReplicated1Table,
       "exampleBcdProvFreeBcdReplicated1Entry": exampleBcdProvFreeBcdReplicated1Entry,
       "exampleBcdProvFreeBcdReplicated1Index": exampleBcdProvFreeBcdReplicated1Index,
       "exampleBcdProvFreeBcdReplicated1Value": exampleBcdProvFreeBcdReplicated1Value,
       "exampleBcdProvFreeBcdReplicated1RowStatus": exampleBcdProvFreeBcdReplicated1RowStatus,
       "exampleBcdProvFreeBcdListTable": exampleBcdProvFreeBcdListTable,
       "exampleBcdProvFreeBcdListEntry": exampleBcdProvFreeBcdListEntry,
       "exampleBcdProvFreeBcdListValue": exampleBcdProvFreeBcdListValue,
       "exampleBcdProvFreeBcdListRowStatus": exampleBcdProvFreeBcdListRowStatus,
       "exampleBcdProvFreeBcdList1Table": exampleBcdProvFreeBcdList1Table,
       "exampleBcdProvFreeBcdList1Entry": exampleBcdProvFreeBcdList1Entry,
       "exampleBcdProvFreeBcdList1Value": exampleBcdProvFreeBcdList1Value,
       "exampleBcdProvFreeBcdList1RowStatus": exampleBcdProvFreeBcdList1RowStatus,
       "exampleWildBcd": exampleWildBcd,
       "exampleWildBcdRowStatusTable": exampleWildBcdRowStatusTable,
       "exampleWildBcdRowStatusEntry": exampleWildBcdRowStatusEntry,
       "exampleWildBcdRowStatus": exampleWildBcdRowStatus,
       "exampleWildBcdComponentName": exampleWildBcdComponentName,
       "exampleWildBcdStorageType": exampleWildBcdStorageType,
       "exampleWildBcdIndex": exampleWildBcdIndex,
       "exampleWildBcdOperationalTable": exampleWildBcdOperationalTable,
       "exampleWildBcdOperationalEntry": exampleWildBcdOperationalEntry,
       "exampleWildBcdOperStructWildBcd": exampleWildBcdOperStructWildBcd,
       "exampleWildBcdOperFreeWildBcd": exampleWildBcdOperFreeWildBcd,
       "exampleWildBcdProvisionalTable": exampleWildBcdProvisionalTable,
       "exampleWildBcdProvisionalEntry": exampleWildBcdProvisionalEntry,
       "exampleWildBcdProvStructWildBcd": exampleWildBcdProvStructWildBcd,
       "exampleWildBcdProvFreeWildBcd": exampleWildBcdProvFreeWildBcd,
       "exampleWildBcdOperStructWildBcdVectorTable": exampleWildBcdOperStructWildBcdVectorTable,
       "exampleWildBcdOperStructWildBcdVectorEntry": exampleWildBcdOperStructWildBcdVectorEntry,
       "exampleWildBcdOperStructWildBcdVectorIndex": exampleWildBcdOperStructWildBcdVectorIndex,
       "exampleWildBcdOperStructWildBcdVectorValue": exampleWildBcdOperStructWildBcdVectorValue,
       "exampleWildBcdOperStructWildBcdArrayTable": exampleWildBcdOperStructWildBcdArrayTable,
       "exampleWildBcdOperStructWildBcdArrayEntry": exampleWildBcdOperStructWildBcdArrayEntry,
       "exampleWildBcdOperStructWildBcdArrayRowIndex": exampleWildBcdOperStructWildBcdArrayRowIndex,
       "exampleWildBcdOperStructWildBcdArrayColumnIndex": exampleWildBcdOperStructWildBcdArrayColumnIndex,
       "exampleWildBcdOperStructWildBcdArrayValue": exampleWildBcdOperStructWildBcdArrayValue,
       "exampleWildBcdOperFreeWildBcdVectorTable": exampleWildBcdOperFreeWildBcdVectorTable,
       "exampleWildBcdOperFreeWildBcdVectorEntry": exampleWildBcdOperFreeWildBcdVectorEntry,
       "exampleWildBcdOperFreeWildBcdVectorIndex": exampleWildBcdOperFreeWildBcdVectorIndex,
       "exampleWildBcdOperFreeWildBcdVectorValue": exampleWildBcdOperFreeWildBcdVectorValue,
       "exampleWildBcdOperFreeWildBcdArrayTable": exampleWildBcdOperFreeWildBcdArrayTable,
       "exampleWildBcdOperFreeWildBcdArrayEntry": exampleWildBcdOperFreeWildBcdArrayEntry,
       "exampleWildBcdOperFreeWildBcdArrayRowIndex": exampleWildBcdOperFreeWildBcdArrayRowIndex,
       "exampleWildBcdOperFreeWildBcdArrayColumnIndex": exampleWildBcdOperFreeWildBcdArrayColumnIndex,
       "exampleWildBcdOperFreeWildBcdArrayValue": exampleWildBcdOperFreeWildBcdArrayValue,
       "exampleWildBcdOperFreeWildBcdReplicatedTable": exampleWildBcdOperFreeWildBcdReplicatedTable,
       "exampleWildBcdOperFreeWildBcdReplicatedEntry": exampleWildBcdOperFreeWildBcdReplicatedEntry,
       "exampleWildBcdOperFreeWildBcdReplicatedIndex": exampleWildBcdOperFreeWildBcdReplicatedIndex,
       "exampleWildBcdOperFreeWildBcdReplicatedValue": exampleWildBcdOperFreeWildBcdReplicatedValue,
       "exampleWildBcdOperFreeWildBcdReplicatedRowStatus": exampleWildBcdOperFreeWildBcdReplicatedRowStatus,
       "exampleWildBcdOperFreeWildBcdListTable": exampleWildBcdOperFreeWildBcdListTable,
       "exampleWildBcdOperFreeWildBcdListEntry": exampleWildBcdOperFreeWildBcdListEntry,
       "exampleWildBcdOperFreeWildBcdListValue": exampleWildBcdOperFreeWildBcdListValue,
       "exampleWildBcdOperFreeWildBcdListRowStatus": exampleWildBcdOperFreeWildBcdListRowStatus,
       "exampleWildBcdProvStructWildBcdVectorTable": exampleWildBcdProvStructWildBcdVectorTable,
       "exampleWildBcdProvStructWildBcdVectorEntry": exampleWildBcdProvStructWildBcdVectorEntry,
       "exampleWildBcdProvStructWildBcdVectorIndex": exampleWildBcdProvStructWildBcdVectorIndex,
       "exampleWildBcdProvStructWildBcdVectorValue": exampleWildBcdProvStructWildBcdVectorValue,
       "exampleWildBcdProvStructWildBcdArrayTable": exampleWildBcdProvStructWildBcdArrayTable,
       "exampleWildBcdProvStructWildBcdArrayEntry": exampleWildBcdProvStructWildBcdArrayEntry,
       "exampleWildBcdProvStructWildBcdArrayRowIndex": exampleWildBcdProvStructWildBcdArrayRowIndex,
       "exampleWildBcdProvStructWildBcdArrayColumnIndex": exampleWildBcdProvStructWildBcdArrayColumnIndex,
       "exampleWildBcdProvStructWildBcdArrayValue": exampleWildBcdProvStructWildBcdArrayValue,
       "exampleWildBcdProvFreeWildBcdVectorTable": exampleWildBcdProvFreeWildBcdVectorTable,
       "exampleWildBcdProvFreeWildBcdVectorEntry": exampleWildBcdProvFreeWildBcdVectorEntry,
       "exampleWildBcdProvFreeWildBcdVectorIndex": exampleWildBcdProvFreeWildBcdVectorIndex,
       "exampleWildBcdProvFreeWildBcdVectorValue": exampleWildBcdProvFreeWildBcdVectorValue,
       "exampleWildBcdProvFreeWildBcdArrayTable": exampleWildBcdProvFreeWildBcdArrayTable,
       "exampleWildBcdProvFreeWildBcdArrayEntry": exampleWildBcdProvFreeWildBcdArrayEntry,
       "exampleWildBcdProvFreeWildBcdArrayRowIndex": exampleWildBcdProvFreeWildBcdArrayRowIndex,
       "exampleWildBcdProvFreeWildBcdArrayColumnIndex": exampleWildBcdProvFreeWildBcdArrayColumnIndex,
       "exampleWildBcdProvFreeWildBcdArrayValue": exampleWildBcdProvFreeWildBcdArrayValue,
       "exampleWildBcdProvFreeWildBcdReplicatedTable": exampleWildBcdProvFreeWildBcdReplicatedTable,
       "exampleWildBcdProvFreeWildBcdReplicatedEntry": exampleWildBcdProvFreeWildBcdReplicatedEntry,
       "exampleWildBcdProvFreeWildBcdReplicatedIndex": exampleWildBcdProvFreeWildBcdReplicatedIndex,
       "exampleWildBcdProvFreeWildBcdReplicatedValue": exampleWildBcdProvFreeWildBcdReplicatedValue,
       "exampleWildBcdProvFreeWildBcdReplicatedRowStatus": exampleWildBcdProvFreeWildBcdReplicatedRowStatus,
       "exampleWildBcdProvFreeWildBcdListTable": exampleWildBcdProvFreeWildBcdListTable,
       "exampleWildBcdProvFreeWildBcdListEntry": exampleWildBcdProvFreeWildBcdListEntry,
       "exampleWildBcdProvFreeWildBcdListValue": exampleWildBcdProvFreeWildBcdListValue,
       "exampleWildBcdProvFreeWildBcdListRowStatus": exampleWildBcdProvFreeWildBcdListRowStatus,
       "exampleEnum": exampleEnum,
       "exampleEnumRowStatusTable": exampleEnumRowStatusTable,
       "exampleEnumRowStatusEntry": exampleEnumRowStatusEntry,
       "exampleEnumRowStatus": exampleEnumRowStatus,
       "exampleEnumComponentName": exampleEnumComponentName,
       "exampleEnumStorageType": exampleEnumStorageType,
       "exampleEnumIndex": exampleEnumIndex,
       "exampleEnumOperationalTable": exampleEnumOperationalTable,
       "exampleEnumOperationalEntry": exampleEnumOperationalEntry,
       "exampleEnumOperStructEnum": exampleEnumOperStructEnum,
       "exampleEnumOperStructEnumSet": exampleEnumOperStructEnumSet,
       "exampleEnumOperFreeEnum": exampleEnumOperFreeEnum,
       "exampleEnumOperFreeEnumSet": exampleEnumOperFreeEnumSet,
       "exampleEnumProvisionalTable": exampleEnumProvisionalTable,
       "exampleEnumProvisionalEntry": exampleEnumProvisionalEntry,
       "exampleEnumProvEnumSub": exampleEnumProvEnumSub,
       "exampleEnumProvStructEnum": exampleEnumProvStructEnum,
       "exampleEnumProvStructEnumSet": exampleEnumProvStructEnumSet,
       "exampleEnumProvFreeEnum": exampleEnumProvFreeEnum,
       "exampleEnumProvFreeEnum1": exampleEnumProvFreeEnum1,
       "exampleEnumProvFreeEnumSet": exampleEnumProvFreeEnumSet,
       "exampleEnumProvFreeEnumSet1": exampleEnumProvFreeEnumSet1,
       "exampleEnumOperStructEnumVectorTable": exampleEnumOperStructEnumVectorTable,
       "exampleEnumOperStructEnumVectorEntry": exampleEnumOperStructEnumVectorEntry,
       "exampleEnumOperStructEnumVectorIndex": exampleEnumOperStructEnumVectorIndex,
       "exampleEnumOperStructEnumVectorValue": exampleEnumOperStructEnumVectorValue,
       "exampleEnumOperStructEnumArrayTable": exampleEnumOperStructEnumArrayTable,
       "exampleEnumOperStructEnumArrayEntry": exampleEnumOperStructEnumArrayEntry,
       "exampleEnumOperStructEnumArrayMonthIndex": exampleEnumOperStructEnumArrayMonthIndex,
       "exampleEnumOperStructEnumArrayDayIndex": exampleEnumOperStructEnumArrayDayIndex,
       "exampleEnumOperStructEnumArrayValue": exampleEnumOperStructEnumArrayValue,
       "exampleEnumOperFreeEnumVectorTable": exampleEnumOperFreeEnumVectorTable,
       "exampleEnumOperFreeEnumVectorEntry": exampleEnumOperFreeEnumVectorEntry,
       "exampleEnumOperFreeEnumVectorIndex": exampleEnumOperFreeEnumVectorIndex,
       "exampleEnumOperFreeEnumVectorValue": exampleEnumOperFreeEnumVectorValue,
       "exampleEnumOperFreeEnumArrayTable": exampleEnumOperFreeEnumArrayTable,
       "exampleEnumOperFreeEnumArrayEntry": exampleEnumOperFreeEnumArrayEntry,
       "exampleEnumOperFreeEnumArrayMonthIndex": exampleEnumOperFreeEnumArrayMonthIndex,
       "exampleEnumOperFreeEnumArrayDayIndex": exampleEnumOperFreeEnumArrayDayIndex,
       "exampleEnumOperFreeEnumArrayValue": exampleEnumOperFreeEnumArrayValue,
       "exampleEnumOperFreeEnumReplicatedTable": exampleEnumOperFreeEnumReplicatedTable,
       "exampleEnumOperFreeEnumReplicatedEntry": exampleEnumOperFreeEnumReplicatedEntry,
       "exampleEnumOperFreeEnumReplicatedIndex": exampleEnumOperFreeEnumReplicatedIndex,
       "exampleEnumOperFreeEnumReplicatedValue": exampleEnumOperFreeEnumReplicatedValue,
       "exampleEnumOperFreeEnumReplicatedRowStatus": exampleEnumOperFreeEnumReplicatedRowStatus,
       "exampleEnumOperFreeEnumListTable": exampleEnumOperFreeEnumListTable,
       "exampleEnumOperFreeEnumListEntry": exampleEnumOperFreeEnumListEntry,
       "exampleEnumOperFreeEnumListValue": exampleEnumOperFreeEnumListValue,
       "exampleEnumOperFreeEnumListRowStatus": exampleEnumOperFreeEnumListRowStatus,
       "exampleEnumProvStructEnumVectorTable": exampleEnumProvStructEnumVectorTable,
       "exampleEnumProvStructEnumVectorEntry": exampleEnumProvStructEnumVectorEntry,
       "exampleEnumProvStructEnumVectorIndex": exampleEnumProvStructEnumVectorIndex,
       "exampleEnumProvStructEnumVectorValue": exampleEnumProvStructEnumVectorValue,
       "exampleEnumProvStructEnumArrayTable": exampleEnumProvStructEnumArrayTable,
       "exampleEnumProvStructEnumArrayEntry": exampleEnumProvStructEnumArrayEntry,
       "exampleEnumProvStructEnumArrayMonthIndex": exampleEnumProvStructEnumArrayMonthIndex,
       "exampleEnumProvStructEnumArrayDayIndex": exampleEnumProvStructEnumArrayDayIndex,
       "exampleEnumProvStructEnumArrayValue": exampleEnumProvStructEnumArrayValue,
       "exampleEnumProvFreeEnumVectorTable": exampleEnumProvFreeEnumVectorTable,
       "exampleEnumProvFreeEnumVectorEntry": exampleEnumProvFreeEnumVectorEntry,
       "exampleEnumProvFreeEnumVectorIndex": exampleEnumProvFreeEnumVectorIndex,
       "exampleEnumProvFreeEnumVectorValue": exampleEnumProvFreeEnumVectorValue,
       "exampleEnumProvFreeEnumVector1Table": exampleEnumProvFreeEnumVector1Table,
       "exampleEnumProvFreeEnumVector1Entry": exampleEnumProvFreeEnumVector1Entry,
       "exampleEnumProvFreeEnumVector1Index": exampleEnumProvFreeEnumVector1Index,
       "exampleEnumProvFreeEnumVector1Value": exampleEnumProvFreeEnumVector1Value,
       "exampleEnumProvFreeEnumArrayTable": exampleEnumProvFreeEnumArrayTable,
       "exampleEnumProvFreeEnumArrayEntry": exampleEnumProvFreeEnumArrayEntry,
       "exampleEnumProvFreeEnumArrayMonthIndex": exampleEnumProvFreeEnumArrayMonthIndex,
       "exampleEnumProvFreeEnumArrayDayIndex": exampleEnumProvFreeEnumArrayDayIndex,
       "exampleEnumProvFreeEnumArrayValue": exampleEnumProvFreeEnumArrayValue,
       "exampleEnumProvFreeEnumArray1Table": exampleEnumProvFreeEnumArray1Table,
       "exampleEnumProvFreeEnumArray1Entry": exampleEnumProvFreeEnumArray1Entry,
       "exampleEnumProvFreeEnumArray1MonthIndex": exampleEnumProvFreeEnumArray1MonthIndex,
       "exampleEnumProvFreeEnumArray1DayIndex": exampleEnumProvFreeEnumArray1DayIndex,
       "exampleEnumProvFreeEnumArray1Value": exampleEnumProvFreeEnumArray1Value,
       "exampleEnumProvFreeEnumReplicatedTable": exampleEnumProvFreeEnumReplicatedTable,
       "exampleEnumProvFreeEnumReplicatedEntry": exampleEnumProvFreeEnumReplicatedEntry,
       "exampleEnumProvFreeEnumReplicatedIndex": exampleEnumProvFreeEnumReplicatedIndex,
       "exampleEnumProvFreeEnumReplicatedValue": exampleEnumProvFreeEnumReplicatedValue,
       "exampleEnumProvFreeEnumReplicatedRowStatus": exampleEnumProvFreeEnumReplicatedRowStatus,
       "exampleEnumProvFreeEnumListTable": exampleEnumProvFreeEnumListTable,
       "exampleEnumProvFreeEnumListEntry": exampleEnumProvFreeEnumListEntry,
       "exampleEnumProvFreeEnumListValue": exampleEnumProvFreeEnumListValue,
       "exampleEnumProvFreeEnumListRowStatus": exampleEnumProvFreeEnumListRowStatus,
       "exampleEnumProvFreeEnumList1Table": exampleEnumProvFreeEnumList1Table,
       "exampleEnumProvFreeEnumList1Entry": exampleEnumProvFreeEnumList1Entry,
       "exampleEnumProvFreeEnumList1Value": exampleEnumProvFreeEnumList1Value,
       "exampleEnumProvFreeEnumList1RowStatus": exampleEnumProvFreeEnumList1RowStatus,
       "exampleObjectId": exampleObjectId,
       "exampleObjectIdRowStatusTable": exampleObjectIdRowStatusTable,
       "exampleObjectIdRowStatusEntry": exampleObjectIdRowStatusEntry,
       "exampleObjectIdRowStatus": exampleObjectIdRowStatus,
       "exampleObjectIdComponentName": exampleObjectIdComponentName,
       "exampleObjectIdStorageType": exampleObjectIdStorageType,
       "exampleObjectIdIndex": exampleObjectIdIndex,
       "exampleObjectIdOperationalTable": exampleObjectIdOperationalTable,
       "exampleObjectIdOperationalEntry": exampleObjectIdOperationalEntry,
       "exampleObjectIdOperFreeObjId": exampleObjectIdOperFreeObjId,
       "exampleObjectIdProvisionalTable": exampleObjectIdProvisionalTable,
       "exampleObjectIdProvisionalEntry": exampleObjectIdProvisionalEntry,
       "exampleObjectIdProvEnumSub": exampleObjectIdProvEnumSub,
       "exampleObjectIdProvFreeObjId": exampleObjectIdProvFreeObjId,
       "exampleObjectIdOperFreeObjIdReplicatedTable": exampleObjectIdOperFreeObjIdReplicatedTable,
       "exampleObjectIdOperFreeObjIdReplicatedEntry": exampleObjectIdOperFreeObjIdReplicatedEntry,
       "exampleObjectIdOperFreeObjIdReplicatedIndex": exampleObjectIdOperFreeObjIdReplicatedIndex,
       "exampleObjectIdOperFreeObjIdReplicatedValue": exampleObjectIdOperFreeObjIdReplicatedValue,
       "exampleObjectIdOperFreeObjIdReplicatedRowStatus": exampleObjectIdOperFreeObjIdReplicatedRowStatus,
       "exampleObjectIdOperFreeObjIdListTable": exampleObjectIdOperFreeObjIdListTable,
       "exampleObjectIdOperFreeObjIdListEntry": exampleObjectIdOperFreeObjIdListEntry,
       "exampleObjectIdOperFreeObjIdListValue": exampleObjectIdOperFreeObjIdListValue,
       "exampleObjectIdOperFreeObjIdListRowStatus": exampleObjectIdOperFreeObjIdListRowStatus,
       "exampleObjectIdProvFreeObjIdReplicatedTable": exampleObjectIdProvFreeObjIdReplicatedTable,
       "exampleObjectIdProvFreeObjIdReplicatedEntry": exampleObjectIdProvFreeObjIdReplicatedEntry,
       "exampleObjectIdProvFreeObjIdReplicatedIndex": exampleObjectIdProvFreeObjIdReplicatedIndex,
       "exampleObjectIdProvFreeObjIdReplicatedValue": exampleObjectIdProvFreeObjIdReplicatedValue,
       "exampleObjectIdProvFreeObjIdReplicatedRowStatus": exampleObjectIdProvFreeObjIdReplicatedRowStatus,
       "exampleObjectIdProvFreeObjIdListTable": exampleObjectIdProvFreeObjIdListTable,
       "exampleObjectIdProvFreeObjIdListEntry": exampleObjectIdProvFreeObjIdListEntry,
       "exampleObjectIdProvFreeObjIdListValue": exampleObjectIdProvFreeObjIdListValue,
       "exampleObjectIdProvFreeObjIdListRowStatus": exampleObjectIdProvFreeObjIdListRowStatus,
       "exampleSequence": exampleSequence,
       "exampleSequenceRowStatusTable": exampleSequenceRowStatusTable,
       "exampleSequenceRowStatusEntry": exampleSequenceRowStatusEntry,
       "exampleSequenceRowStatus": exampleSequenceRowStatus,
       "exampleSequenceComponentName": exampleSequenceComponentName,
       "exampleSequenceStorageType": exampleSequenceStorageType,
       "exampleSequenceIndex": exampleSequenceIndex,
       "exampleSequenceOperationalTable": exampleSequenceOperationalTable,
       "exampleSequenceOperationalEntry": exampleSequenceOperationalEntry,
       "exampleSequenceOperStructSequence": exampleSequenceOperStructSequence,
       "exampleSequenceOperFreeSequence": exampleSequenceOperFreeSequence,
       "exampleSequenceProvisionalTable": exampleSequenceProvisionalTable,
       "exampleSequenceProvisionalEntry": exampleSequenceProvisionalEntry,
       "exampleSequenceProvStructSequence": exampleSequenceProvStructSequence,
       "exampleSequenceProvFreeSequence": exampleSequenceProvFreeSequence,
       "exampleSequenceOperFreeSequenceReplicatedTable": exampleSequenceOperFreeSequenceReplicatedTable,
       "exampleSequenceOperFreeSequenceReplicatedEntry": exampleSequenceOperFreeSequenceReplicatedEntry,
       "exampleSequenceOperFreeSequenceReplicatedIndex": exampleSequenceOperFreeSequenceReplicatedIndex,
       "exampleSequenceOperFreeSequenceReplicatedValue": exampleSequenceOperFreeSequenceReplicatedValue,
       "exampleSequenceOperFreeSequenceReplicatedRowStatus": exampleSequenceOperFreeSequenceReplicatedRowStatus,
       "exampleSequenceOperFreeSequenceListTable": exampleSequenceOperFreeSequenceListTable,
       "exampleSequenceOperFreeSequenceListEntry": exampleSequenceOperFreeSequenceListEntry,
       "exampleSequenceOperFreeSequenceListValue": exampleSequenceOperFreeSequenceListValue,
       "exampleSequenceOperFreeSequenceListRowStatus": exampleSequenceOperFreeSequenceListRowStatus,
       "exampleSequenceProvFreeSequenceReplicatedTable": exampleSequenceProvFreeSequenceReplicatedTable,
       "exampleSequenceProvFreeSequenceReplicatedEntry": exampleSequenceProvFreeSequenceReplicatedEntry,
       "exampleSequenceProvFreeSequenceReplicatedIndex": exampleSequenceProvFreeSequenceReplicatedIndex,
       "exampleSequenceProvFreeSequenceReplicatedValue": exampleSequenceProvFreeSequenceReplicatedValue,
       "exampleSequenceProvFreeSequenceReplicatedRowStatus": exampleSequenceProvFreeSequenceReplicatedRowStatus,
       "exampleSequenceProvFreeSequenceListTable": exampleSequenceProvFreeSequenceListTable,
       "exampleSequenceProvFreeSequenceListEntry": exampleSequenceProvFreeSequenceListEntry,
       "exampleSequenceProvFreeSequenceListValue": exampleSequenceProvFreeSequenceListValue,
       "exampleSequenceProvFreeSequenceListRowStatus": exampleSequenceProvFreeSequenceListRowStatus,
       "exampleSigned": exampleSigned,
       "exampleSignedRowStatusTable": exampleSignedRowStatusTable,
       "exampleSignedRowStatusEntry": exampleSignedRowStatusEntry,
       "exampleSignedRowStatus": exampleSignedRowStatus,
       "exampleSignedComponentName": exampleSignedComponentName,
       "exampleSignedStorageType": exampleSignedStorageType,
       "exampleSignedIndex": exampleSignedIndex,
       "exampleSignedOperationalTable": exampleSignedOperationalTable,
       "exampleSignedOperationalEntry": exampleSignedOperationalEntry,
       "exampleSignedOperStructSigned": exampleSignedOperStructSigned,
       "exampleSignedOperFreeSigned": exampleSignedOperFreeSigned,
       "exampleSignedProvisionalTable": exampleSignedProvisionalTable,
       "exampleSignedProvisionalEntry": exampleSignedProvisionalEntry,
       "exampleSignedProvSignedSub": exampleSignedProvSignedSub,
       "exampleSignedProvStructSigned": exampleSignedProvStructSigned,
       "exampleSignedProvFreeSigned": exampleSignedProvFreeSigned,
       "exampleSignedProvFreeSigned1": exampleSignedProvFreeSigned1,
       "exampleSignedOperStructSignedVectorTable": exampleSignedOperStructSignedVectorTable,
       "exampleSignedOperStructSignedVectorEntry": exampleSignedOperStructSignedVectorEntry,
       "exampleSignedOperStructSignedVectorIndex": exampleSignedOperStructSignedVectorIndex,
       "exampleSignedOperStructSignedVectorValue": exampleSignedOperStructSignedVectorValue,
       "exampleSignedOperStructSignedArrayTable": exampleSignedOperStructSignedArrayTable,
       "exampleSignedOperStructSignedArrayEntry": exampleSignedOperStructSignedArrayEntry,
       "exampleSignedOperStructSignedArrayRowIndex": exampleSignedOperStructSignedArrayRowIndex,
       "exampleSignedOperStructSignedArrayColumnIndex": exampleSignedOperStructSignedArrayColumnIndex,
       "exampleSignedOperStructSignedArrayValue": exampleSignedOperStructSignedArrayValue,
       "exampleSignedOperFreeSignedVectorTable": exampleSignedOperFreeSignedVectorTable,
       "exampleSignedOperFreeSignedVectorEntry": exampleSignedOperFreeSignedVectorEntry,
       "exampleSignedOperFreeSignedVectorIndex": exampleSignedOperFreeSignedVectorIndex,
       "exampleSignedOperFreeSignedVectorValue": exampleSignedOperFreeSignedVectorValue,
       "exampleSignedOperFreeSignedArrayTable": exampleSignedOperFreeSignedArrayTable,
       "exampleSignedOperFreeSignedArrayEntry": exampleSignedOperFreeSignedArrayEntry,
       "exampleSignedOperFreeSignedArrayRowIndex": exampleSignedOperFreeSignedArrayRowIndex,
       "exampleSignedOperFreeSignedArrayColumnIndex": exampleSignedOperFreeSignedArrayColumnIndex,
       "exampleSignedOperFreeSignedArrayValue": exampleSignedOperFreeSignedArrayValue,
       "exampleSignedOperFreeSignedReplicatedTable": exampleSignedOperFreeSignedReplicatedTable,
       "exampleSignedOperFreeSignedReplicatedEntry": exampleSignedOperFreeSignedReplicatedEntry,
       "exampleSignedOperFreeSignedReplicatedIndex": exampleSignedOperFreeSignedReplicatedIndex,
       "exampleSignedOperFreeSignedReplicatedValue": exampleSignedOperFreeSignedReplicatedValue,
       "exampleSignedOperFreeSignedReplicatedRowStatus": exampleSignedOperFreeSignedReplicatedRowStatus,
       "exampleSignedOperFreeSignedListTable": exampleSignedOperFreeSignedListTable,
       "exampleSignedOperFreeSignedListEntry": exampleSignedOperFreeSignedListEntry,
       "exampleSignedOperFreeSignedListValue": exampleSignedOperFreeSignedListValue,
       "exampleSignedOperFreeSignedListRowStatus": exampleSignedOperFreeSignedListRowStatus,
       "exampleSignedProvStructSignedVectorTable": exampleSignedProvStructSignedVectorTable,
       "exampleSignedProvStructSignedVectorEntry": exampleSignedProvStructSignedVectorEntry,
       "exampleSignedProvStructSignedVectorIndex": exampleSignedProvStructSignedVectorIndex,
       "exampleSignedProvStructSignedVectorValue": exampleSignedProvStructSignedVectorValue,
       "exampleSignedProvStructSignedArrayTable": exampleSignedProvStructSignedArrayTable,
       "exampleSignedProvStructSignedArrayEntry": exampleSignedProvStructSignedArrayEntry,
       "exampleSignedProvStructSignedArrayRowIndex": exampleSignedProvStructSignedArrayRowIndex,
       "exampleSignedProvStructSignedArrayColumnIndex": exampleSignedProvStructSignedArrayColumnIndex,
       "exampleSignedProvStructSignedArrayValue": exampleSignedProvStructSignedArrayValue,
       "exampleSignedProvFreeSignedVectorTable": exampleSignedProvFreeSignedVectorTable,
       "exampleSignedProvFreeSignedVectorEntry": exampleSignedProvFreeSignedVectorEntry,
       "exampleSignedProvFreeSignedVectorIndex": exampleSignedProvFreeSignedVectorIndex,
       "exampleSignedProvFreeSignedVectorValue": exampleSignedProvFreeSignedVectorValue,
       "exampleSignedProvFreeSignedVector1Table": exampleSignedProvFreeSignedVector1Table,
       "exampleSignedProvFreeSignedVector1Entry": exampleSignedProvFreeSignedVector1Entry,
       "exampleSignedProvFreeSignedVector1Index": exampleSignedProvFreeSignedVector1Index,
       "exampleSignedProvFreeSignedVector1Value": exampleSignedProvFreeSignedVector1Value,
       "exampleSignedProvFreeSignedArrayTable": exampleSignedProvFreeSignedArrayTable,
       "exampleSignedProvFreeSignedArrayEntry": exampleSignedProvFreeSignedArrayEntry,
       "exampleSignedProvFreeSignedArrayRowIndex": exampleSignedProvFreeSignedArrayRowIndex,
       "exampleSignedProvFreeSignedArrayColumnIndex": exampleSignedProvFreeSignedArrayColumnIndex,
       "exampleSignedProvFreeSignedArrayValue": exampleSignedProvFreeSignedArrayValue,
       "exampleSignedProvFreeSignedArray1Table": exampleSignedProvFreeSignedArray1Table,
       "exampleSignedProvFreeSignedArray1Entry": exampleSignedProvFreeSignedArray1Entry,
       "exampleSignedProvFreeSignedArray1RowIndex": exampleSignedProvFreeSignedArray1RowIndex,
       "exampleSignedProvFreeSignedArray1ColumnIndex": exampleSignedProvFreeSignedArray1ColumnIndex,
       "exampleSignedProvFreeSignedArray1Value": exampleSignedProvFreeSignedArray1Value,
       "exampleSignedProvFreeSignedReplicatedTable": exampleSignedProvFreeSignedReplicatedTable,
       "exampleSignedProvFreeSignedReplicatedEntry": exampleSignedProvFreeSignedReplicatedEntry,
       "exampleSignedProvFreeSignedReplicatedIndex": exampleSignedProvFreeSignedReplicatedIndex,
       "exampleSignedProvFreeSignedReplicatedValue": exampleSignedProvFreeSignedReplicatedValue,
       "exampleSignedProvFreeSignedReplicatedRowStatus": exampleSignedProvFreeSignedReplicatedRowStatus,
       "exampleSignedProvFreeSignedListTable": exampleSignedProvFreeSignedListTable,
       "exampleSignedProvFreeSignedListEntry": exampleSignedProvFreeSignedListEntry,
       "exampleSignedProvFreeSignedListValue": exampleSignedProvFreeSignedListValue,
       "exampleSignedProvFreeSignedListRowStatus": exampleSignedProvFreeSignedListRowStatus,
       "exampleMiscellaneous": exampleMiscellaneous,
       "exampleMiscellaneousRowStatusTable": exampleMiscellaneousRowStatusTable,
       "exampleMiscellaneousRowStatusEntry": exampleMiscellaneousRowStatusEntry,
       "exampleMiscellaneousRowStatus": exampleMiscellaneousRowStatus,
       "exampleMiscellaneousComponentName": exampleMiscellaneousComponentName,
       "exampleMiscellaneousStorageType": exampleMiscellaneousStorageType,
       "exampleMiscellaneousIndex": exampleMiscellaneousIndex,
       "exampleMiscellaneousOperationalTable": exampleMiscellaneousOperationalTable,
       "exampleMiscellaneousOperationalEntry": exampleMiscellaneousOperationalEntry,
       "exampleMiscellaneousOperStructLong": exampleMiscellaneousOperStructLong,
       "exampleMiscellaneousOperFreeLong": exampleMiscellaneousOperFreeLong,
       "exampleMiscellaneousOperFreeTime": exampleMiscellaneousOperFreeTime,
       "exampleMiscellaneousOperFreeTimeDateOnly": exampleMiscellaneousOperFreeTimeDateOnly,
       "exampleMiscellaneousOperFreeTimeTimeOnly": exampleMiscellaneousOperFreeTimeTimeOnly,
       "exampleMiscellaneousOperFreeTimeDateTimeMinute": exampleMiscellaneousOperFreeTimeDateTimeMinute,
       "exampleMiscellaneousOperFreeCounter64": exampleMiscellaneousOperFreeCounter64,
       "exampleMiscellaneousOperFreeGauge64": exampleMiscellaneousOperFreeGauge64,
       "exampleMiscellaneousOperStructCounter64": exampleMiscellaneousOperStructCounter64,
       "exampleMiscellaneousProvisionalTable": exampleMiscellaneousProvisionalTable,
       "exampleMiscellaneousProvisionalEntry": exampleMiscellaneousProvisionalEntry,
       "exampleMiscellaneousProvEnumSub": exampleMiscellaneousProvEnumSub,
       "exampleMiscellaneousProvStructLong": exampleMiscellaneousProvStructLong,
       "exampleMiscellaneousProvFreeLong": exampleMiscellaneousProvFreeLong,
       "exampleMiscellaneousProvFreeTime": exampleMiscellaneousProvFreeTime,
       "exampleMiscellaneousProvFreeTimeDateOnly": exampleMiscellaneousProvFreeTimeDateOnly,
       "exampleMiscellaneousProvFreeTimeTimeOnly": exampleMiscellaneousProvFreeTimeTimeOnly,
       "exampleMiscellaneousProvFreeTimeDateTimeMinute": exampleMiscellaneousProvFreeTimeDateTimeMinute,
       "exampleMiscellaneousProvFreeTime1": exampleMiscellaneousProvFreeTime1,
       "exampleMiscellaneousProvFreeTimeDateOnly1": exampleMiscellaneousProvFreeTimeDateOnly1,
       "exampleMiscellaneousProvFreeTimeTimeOnly1": exampleMiscellaneousProvFreeTimeTimeOnly1,
       "exampleMiscellaneousProvFreeTimeDateTimeMinute1": exampleMiscellaneousProvFreeTimeDateTimeMinute1,
       "exampleMiscellaneousOperFreeLongReplicatedTable": exampleMiscellaneousOperFreeLongReplicatedTable,
       "exampleMiscellaneousOperFreeLongReplicatedEntry": exampleMiscellaneousOperFreeLongReplicatedEntry,
       "exampleMiscellaneousOperFreeLongReplicatedIndex": exampleMiscellaneousOperFreeLongReplicatedIndex,
       "exampleMiscellaneousOperFreeLongReplicatedValue": exampleMiscellaneousOperFreeLongReplicatedValue,
       "exampleMiscellaneousOperFreeLongReplicatedRowStatus": exampleMiscellaneousOperFreeLongReplicatedRowStatus,
       "exampleMiscellaneousOperFreeLongListTable": exampleMiscellaneousOperFreeLongListTable,
       "exampleMiscellaneousOperFreeLongListEntry": exampleMiscellaneousOperFreeLongListEntry,
       "exampleMiscellaneousOperFreeLongListValue": exampleMiscellaneousOperFreeLongListValue,
       "exampleMiscellaneousOperFreeLongListRowStatus": exampleMiscellaneousOperFreeLongListRowStatus,
       "exampleMiscellaneousOperFreeTimeListTable": exampleMiscellaneousOperFreeTimeListTable,
       "exampleMiscellaneousOperFreeTimeListEntry": exampleMiscellaneousOperFreeTimeListEntry,
       "exampleMiscellaneousOperFreeTimeListValue": exampleMiscellaneousOperFreeTimeListValue,
       "exampleMiscellaneousOperFreeTimeListRowStatus": exampleMiscellaneousOperFreeTimeListRowStatus,
       "exampleMiscellaneousProvFreeLongReplicatedTable": exampleMiscellaneousProvFreeLongReplicatedTable,
       "exampleMiscellaneousProvFreeLongReplicatedEntry": exampleMiscellaneousProvFreeLongReplicatedEntry,
       "exampleMiscellaneousProvFreeLongReplicatedIndex": exampleMiscellaneousProvFreeLongReplicatedIndex,
       "exampleMiscellaneousProvFreeLongReplicatedValue": exampleMiscellaneousProvFreeLongReplicatedValue,
       "exampleMiscellaneousProvFreeLongReplicatedRowStatus": exampleMiscellaneousProvFreeLongReplicatedRowStatus,
       "exampleMiscellaneousProvFreeLongListTable": exampleMiscellaneousProvFreeLongListTable,
       "exampleMiscellaneousProvFreeLongListEntry": exampleMiscellaneousProvFreeLongListEntry,
       "exampleMiscellaneousProvFreeLongListValue": exampleMiscellaneousProvFreeLongListValue,
       "exampleMiscellaneousProvFreeLongListRowStatus": exampleMiscellaneousProvFreeLongListRowStatus,
       "exampleMiscellaneousProvFreeTimeReplicatedTable": exampleMiscellaneousProvFreeTimeReplicatedTable,
       "exampleMiscellaneousProvFreeTimeReplicatedEntry": exampleMiscellaneousProvFreeTimeReplicatedEntry,
       "exampleMiscellaneousProvFreeTimeReplicatedIndex": exampleMiscellaneousProvFreeTimeReplicatedIndex,
       "exampleMiscellaneousProvFreeTimeReplicatedValue": exampleMiscellaneousProvFreeTimeReplicatedValue,
       "exampleMiscellaneousProvFreeTimeReplicatedRowStatus": exampleMiscellaneousProvFreeTimeReplicatedRowStatus,
       "exampleMiscellaneousProvFreeTimeListTable": exampleMiscellaneousProvFreeTimeListTable,
       "exampleMiscellaneousProvFreeTimeListEntry": exampleMiscellaneousProvFreeTimeListEntry,
       "exampleMiscellaneousProvFreeTimeListValue": exampleMiscellaneousProvFreeTimeListValue,
       "exampleMiscellaneousProvFreeTimeListRowStatus": exampleMiscellaneousProvFreeTimeListRowStatus,
       "exampleMiscellaneousProvFreeTimeList1Table": exampleMiscellaneousProvFreeTimeList1Table,
       "exampleMiscellaneousProvFreeTimeList1Entry": exampleMiscellaneousProvFreeTimeList1Entry,
       "exampleMiscellaneousProvFreeTimeList1Value": exampleMiscellaneousProvFreeTimeList1Value,
       "exampleMiscellaneousProvFreeTimeList1RowStatus": exampleMiscellaneousProvFreeTimeList1RowStatus,
       "exampleMiscellaneousProvFreeTimeList2Table": exampleMiscellaneousProvFreeTimeList2Table,
       "exampleMiscellaneousProvFreeTimeList2Entry": exampleMiscellaneousProvFreeTimeList2Entry,
       "exampleMiscellaneousProvFreeTimeList2Value": exampleMiscellaneousProvFreeTimeList2Value,
       "exampleMiscellaneousProvFreeTimeList2RowStatus": exampleMiscellaneousProvFreeTimeList2RowStatus,
       "exampleMiscellaneousProvFreeTimeList3Table": exampleMiscellaneousProvFreeTimeList3Table,
       "exampleMiscellaneousProvFreeTimeList3Entry": exampleMiscellaneousProvFreeTimeList3Entry,
       "exampleMiscellaneousProvFreeTimeList3Value": exampleMiscellaneousProvFreeTimeList3Value,
       "exampleMiscellaneousProvFreeTimeList3RowStatus": exampleMiscellaneousProvFreeTimeList3RowStatus,
       "exampleOneIndex": exampleOneIndex,
       "exampleOneIndexRowStatusTable": exampleOneIndexRowStatusTable,
       "exampleOneIndexRowStatusEntry": exampleOneIndexRowStatusEntry,
       "exampleOneIndexRowStatus": exampleOneIndexRowStatus,
       "exampleOneIndexComponentName": exampleOneIndexComponentName,
       "exampleOneIndexStorageType": exampleOneIndexStorageType,
       "exampleOneIndexOneIndex": exampleOneIndexOneIndex,
       "exampleOneIndexProvisionedTable": exampleOneIndexProvisionedTable,
       "exampleOneIndexProvisionedEntry": exampleOneIndexProvisionedEntry,
       "exampleOneIndexProvAttribute": exampleOneIndexProvAttribute,
       "exampleTwoIndices": exampleTwoIndices,
       "exampleTwoIndicesRowStatusTable": exampleTwoIndicesRowStatusTable,
       "exampleTwoIndicesRowStatusEntry": exampleTwoIndicesRowStatusEntry,
       "exampleTwoIndicesRowStatus": exampleTwoIndicesRowStatus,
       "exampleTwoIndicesComponentName": exampleTwoIndicesComponentName,
       "exampleTwoIndicesStorageType": exampleTwoIndicesStorageType,
       "exampleTwoIndicesOneIndex": exampleTwoIndicesOneIndex,
       "exampleTwoIndicesTwoIndex": exampleTwoIndicesTwoIndex,
       "exampleTwoIndicesProvisionedTable": exampleTwoIndicesProvisionedTable,
       "exampleTwoIndicesProvisionedEntry": exampleTwoIndicesProvisionedEntry,
       "exampleTwoIndicesProvAttribute": exampleTwoIndicesProvAttribute,
       "exampleThreeIndices": exampleThreeIndices,
       "exampleThreeIndicesRowStatusTable": exampleThreeIndicesRowStatusTable,
       "exampleThreeIndicesRowStatusEntry": exampleThreeIndicesRowStatusEntry,
       "exampleThreeIndicesRowStatus": exampleThreeIndicesRowStatus,
       "exampleThreeIndicesComponentName": exampleThreeIndicesComponentName,
       "exampleThreeIndicesStorageType": exampleThreeIndicesStorageType,
       "exampleThreeIndicesOneIndex": exampleThreeIndicesOneIndex,
       "exampleThreeIndicesTwoIndex": exampleThreeIndicesTwoIndex,
       "exampleThreeIndicesThreeIndex": exampleThreeIndicesThreeIndex,
       "exampleThreeIndicesProvisionedTable": exampleThreeIndicesProvisionedTable,
       "exampleThreeIndicesProvisionedEntry": exampleThreeIndicesProvisionedEntry,
       "exampleThreeIndicesProvAttribute": exampleThreeIndicesProvAttribute,
       "exampleFourIndices": exampleFourIndices,
       "exampleFourIndicesRowStatusTable": exampleFourIndicesRowStatusTable,
       "exampleFourIndicesRowStatusEntry": exampleFourIndicesRowStatusEntry,
       "exampleFourIndicesRowStatus": exampleFourIndicesRowStatus,
       "exampleFourIndicesComponentName": exampleFourIndicesComponentName,
       "exampleFourIndicesStorageType": exampleFourIndicesStorageType,
       "exampleFourIndicesOneIndex": exampleFourIndicesOneIndex,
       "exampleFourIndicesTwoIndex": exampleFourIndicesTwoIndex,
       "exampleFourIndicesThreeIndex": exampleFourIndicesThreeIndex,
       "exampleFourIndicesFourIndex": exampleFourIndicesFourIndex,
       "exampleFourIndicesProvisionedTable": exampleFourIndicesProvisionedTable,
       "exampleFourIndicesProvisionedEntry": exampleFourIndicesProvisionedEntry,
       "exampleFourIndicesProvAttribute": exampleFourIndicesProvAttribute,
       "exampleDecimalIndices": exampleDecimalIndices,
       "exampleDecimalIndicesRowStatusTable": exampleDecimalIndicesRowStatusTable,
       "exampleDecimalIndicesRowStatusEntry": exampleDecimalIndicesRowStatusEntry,
       "exampleDecimalIndicesRowStatus": exampleDecimalIndicesRowStatus,
       "exampleDecimalIndicesComponentName": exampleDecimalIndicesComponentName,
       "exampleDecimalIndicesStorageType": exampleDecimalIndicesStorageType,
       "exampleDecimalIndicesOneIndex": exampleDecimalIndicesOneIndex,
       "exampleDecimalIndicesTwoIndex": exampleDecimalIndicesTwoIndex,
       "exampleDecimalIndicesThreeIndex": exampleDecimalIndicesThreeIndex,
       "exampleDecimalIndicesProvisionedTable": exampleDecimalIndicesProvisionedTable,
       "exampleDecimalIndicesProvisionedEntry": exampleDecimalIndicesProvisionedEntry,
       "exampleDecimalIndicesProvAttribute": exampleDecimalIndicesProvAttribute,
       "exampleHexIndices": exampleHexIndices,
       "exampleHexIndicesRowStatusTable": exampleHexIndicesRowStatusTable,
       "exampleHexIndicesRowStatusEntry": exampleHexIndicesRowStatusEntry,
       "exampleHexIndicesRowStatus": exampleHexIndicesRowStatus,
       "exampleHexIndicesComponentName": exampleHexIndicesComponentName,
       "exampleHexIndicesStorageType": exampleHexIndicesStorageType,
       "exampleHexIndicesOneIndex": exampleHexIndicesOneIndex,
       "exampleHexIndicesTwoIndex": exampleHexIndicesTwoIndex,
       "exampleHexIndicesThreeIndex": exampleHexIndicesThreeIndex,
       "exampleHexIndicesProvisionedTable": exampleHexIndicesProvisionedTable,
       "exampleHexIndicesProvisionedEntry": exampleHexIndicesProvisionedEntry,
       "exampleHexIndicesProvAttribute": exampleHexIndicesProvAttribute,
       "exampleIpAddrIndices": exampleIpAddrIndices,
       "exampleIpAddrIndicesRowStatusTable": exampleIpAddrIndicesRowStatusTable,
       "exampleIpAddrIndicesRowStatusEntry": exampleIpAddrIndicesRowStatusEntry,
       "exampleIpAddrIndicesRowStatus": exampleIpAddrIndicesRowStatus,
       "exampleIpAddrIndicesComponentName": exampleIpAddrIndicesComponentName,
       "exampleIpAddrIndicesStorageType": exampleIpAddrIndicesStorageType,
       "exampleIpAddrIndicesOneIndex": exampleIpAddrIndicesOneIndex,
       "exampleIpAddrIndicesTwoIndex": exampleIpAddrIndicesTwoIndex,
       "exampleIpAddrIndicesThreeIndex": exampleIpAddrIndicesThreeIndex,
       "exampleIpAddrIndicesProvisionedTable": exampleIpAddrIndicesProvisionedTable,
       "exampleIpAddrIndicesProvisionedEntry": exampleIpAddrIndicesProvisionedEntry,
       "exampleIpAddrIndicesProvAttribute": exampleIpAddrIndicesProvAttribute,
       "exampleAsciiIndices": exampleAsciiIndices,
       "exampleAsciiIndicesRowStatusTable": exampleAsciiIndicesRowStatusTable,
       "exampleAsciiIndicesRowStatusEntry": exampleAsciiIndicesRowStatusEntry,
       "exampleAsciiIndicesRowStatus": exampleAsciiIndicesRowStatus,
       "exampleAsciiIndicesComponentName": exampleAsciiIndicesComponentName,
       "exampleAsciiIndicesStorageType": exampleAsciiIndicesStorageType,
       "exampleAsciiIndicesOneIndex": exampleAsciiIndicesOneIndex,
       "exampleAsciiIndicesTwoIndex": exampleAsciiIndicesTwoIndex,
       "exampleAsciiIndicesThreeIndex": exampleAsciiIndicesThreeIndex,
       "exampleAsciiIndicesProvisionedTable": exampleAsciiIndicesProvisionedTable,
       "exampleAsciiIndicesProvisionedEntry": exampleAsciiIndicesProvisionedEntry,
       "exampleAsciiIndicesProvAttribute": exampleAsciiIndicesProvAttribute,
       "exampleHexStrIndices": exampleHexStrIndices,
       "exampleHexStrIndicesRowStatusTable": exampleHexStrIndicesRowStatusTable,
       "exampleHexStrIndicesRowStatusEntry": exampleHexStrIndicesRowStatusEntry,
       "exampleHexStrIndicesRowStatus": exampleHexStrIndicesRowStatus,
       "exampleHexStrIndicesComponentName": exampleHexStrIndicesComponentName,
       "exampleHexStrIndicesStorageType": exampleHexStrIndicesStorageType,
       "exampleHexStrIndicesOneIndex": exampleHexStrIndicesOneIndex,
       "exampleHexStrIndicesTwoIndex": exampleHexStrIndicesTwoIndex,
       "exampleHexStrIndicesThreeIndex": exampleHexStrIndicesThreeIndex,
       "exampleHexStrIndicesProvisionedTable": exampleHexStrIndicesProvisionedTable,
       "exampleHexStrIndicesProvisionedEntry": exampleHexStrIndicesProvisionedEntry,
       "exampleHexStrIndicesProvAttribute": exampleHexStrIndicesProvAttribute,
       "exampleBcdIndices": exampleBcdIndices,
       "exampleBcdIndicesRowStatusTable": exampleBcdIndicesRowStatusTable,
       "exampleBcdIndicesRowStatusEntry": exampleBcdIndicesRowStatusEntry,
       "exampleBcdIndicesRowStatus": exampleBcdIndicesRowStatus,
       "exampleBcdIndicesComponentName": exampleBcdIndicesComponentName,
       "exampleBcdIndicesStorageType": exampleBcdIndicesStorageType,
       "exampleBcdIndicesOneIndex": exampleBcdIndicesOneIndex,
       "exampleBcdIndicesTwoIndex": exampleBcdIndicesTwoIndex,
       "exampleBcdIndicesThreeIndex": exampleBcdIndicesThreeIndex,
       "exampleBcdIndicesProvisionedTable": exampleBcdIndicesProvisionedTable,
       "exampleBcdIndicesProvisionedEntry": exampleBcdIndicesProvisionedEntry,
       "exampleBcdIndicesProvAttribute": exampleBcdIndicesProvAttribute,
       "exampleEnumIndices": exampleEnumIndices,
       "exampleEnumIndicesRowStatusTable": exampleEnumIndicesRowStatusTable,
       "exampleEnumIndicesRowStatusEntry": exampleEnumIndicesRowStatusEntry,
       "exampleEnumIndicesRowStatus": exampleEnumIndicesRowStatus,
       "exampleEnumIndicesComponentName": exampleEnumIndicesComponentName,
       "exampleEnumIndicesStorageType": exampleEnumIndicesStorageType,
       "exampleEnumIndicesOneIndex": exampleEnumIndicesOneIndex,
       "exampleEnumIndicesTwoIndex": exampleEnumIndicesTwoIndex,
       "exampleEnumIndicesThreeIndex": exampleEnumIndicesThreeIndex,
       "exampleEnumIndicesProvisionedTable": exampleEnumIndicesProvisionedTable,
       "exampleEnumIndicesProvisionedEntry": exampleEnumIndicesProvisionedEntry,
       "exampleEnumIndicesProvAttribute": exampleEnumIndicesProvAttribute,
       "exampleSequenceIndices": exampleSequenceIndices,
       "exampleSequenceIndicesRowStatusTable": exampleSequenceIndicesRowStatusTable,
       "exampleSequenceIndicesRowStatusEntry": exampleSequenceIndicesRowStatusEntry,
       "exampleSequenceIndicesRowStatus": exampleSequenceIndicesRowStatus,
       "exampleSequenceIndicesComponentName": exampleSequenceIndicesComponentName,
       "exampleSequenceIndicesStorageType": exampleSequenceIndicesStorageType,
       "exampleSequenceIndicesOneIndex": exampleSequenceIndicesOneIndex,
       "exampleSequenceIndicesTwoIndex": exampleSequenceIndicesTwoIndex,
       "exampleSequenceIndicesThreeIndex": exampleSequenceIndicesThreeIndex,
       "exampleSequenceIndicesProvisionedTable": exampleSequenceIndicesProvisionedTable,
       "exampleSequenceIndicesProvisionedEntry": exampleSequenceIndicesProvisionedEntry,
       "exampleSequenceIndicesProvAttribute": exampleSequenceIndicesProvAttribute,
       "exampleObjIdIndices": exampleObjIdIndices,
       "exampleObjIdIndicesRowStatusTable": exampleObjIdIndicesRowStatusTable,
       "exampleObjIdIndicesRowStatusEntry": exampleObjIdIndicesRowStatusEntry,
       "exampleObjIdIndicesRowStatus": exampleObjIdIndicesRowStatus,
       "exampleObjIdIndicesComponentName": exampleObjIdIndicesComponentName,
       "exampleObjIdIndicesStorageType": exampleObjIdIndicesStorageType,
       "exampleObjIdIndicesOneIndex": exampleObjIdIndicesOneIndex,
       "exampleObjIdIndicesTwoIndex": exampleObjIdIndicesTwoIndex,
       "exampleObjIdIndicesThreeIndex": exampleObjIdIndicesThreeIndex,
       "exampleObjIdIndicesProvisionedTable": exampleObjIdIndicesProvisionedTable,
       "exampleObjIdIndicesProvisionedEntry": exampleObjIdIndicesProvisionedEntry,
       "exampleObjIdIndicesProvAttribute": exampleObjIdIndicesProvAttribute,
       "exampleDashedIndices": exampleDashedIndices,
       "exampleDashedIndicesRowStatusTable": exampleDashedIndicesRowStatusTable,
       "exampleDashedIndicesRowStatusEntry": exampleDashedIndicesRowStatusEntry,
       "exampleDashedIndicesRowStatus": exampleDashedIndicesRowStatus,
       "exampleDashedIndicesComponentName": exampleDashedIndicesComponentName,
       "exampleDashedIndicesStorageType": exampleDashedIndicesStorageType,
       "exampleDashedIndicesOneIndex": exampleDashedIndicesOneIndex,
       "exampleDashedIndicesTwoIndex": exampleDashedIndicesTwoIndex,
       "exampleDashedIndicesThreeIndex": exampleDashedIndicesThreeIndex,
       "exampleDashedIndicesProvisionedTable": exampleDashedIndicesProvisionedTable,
       "exampleDashedIndicesProvisionedEntry": exampleDashedIndicesProvisionedEntry,
       "exampleDashedIndicesProvAttribute": exampleDashedIndicesProvAttribute,
       "exampleRequiredIndices": exampleRequiredIndices,
       "exampleRequiredIndicesRowStatusTable": exampleRequiredIndicesRowStatusTable,
       "exampleRequiredIndicesRowStatusEntry": exampleRequiredIndicesRowStatusEntry,
       "exampleRequiredIndicesRowStatus": exampleRequiredIndicesRowStatus,
       "exampleRequiredIndicesComponentName": exampleRequiredIndicesComponentName,
       "exampleRequiredIndicesStorageType": exampleRequiredIndicesStorageType,
       "exampleRequiredIndicesDecimalIndex": exampleRequiredIndicesDecimalIndex,
       "exampleRequiredIndicesEnumerationIndex": exampleRequiredIndicesEnumerationIndex,
       "exampleRequiredIndicesProvisionedTable": exampleRequiredIndicesProvisionedTable,
       "exampleRequiredIndicesProvisionedEntry": exampleRequiredIndicesProvisionedEntry,
       "exampleRequiredIndicesProvAttribute": exampleRequiredIndicesProvAttribute,
       "exampleNsap": exampleNsap,
       "exampleNsapRowStatusTable": exampleNsapRowStatusTable,
       "exampleNsapRowStatusEntry": exampleNsapRowStatusEntry,
       "exampleNsapRowStatus": exampleNsapRowStatus,
       "exampleNsapComponentName": exampleNsapComponentName,
       "exampleNsapStorageType": exampleNsapStorageType,
       "exampleNsapIndex": exampleNsapIndex,
       "exampleNsapAtmAddrTable": exampleNsapAtmAddrTable,
       "exampleNsapAtmAddrEntry": exampleNsapAtmAddrEntry,
       "exampleNsapNsapNativeAddress": exampleNsapNsapNativeAddress,
       "exampleNsapNativeTable": exampleNsapNativeTable,
       "exampleNsapNativeEntry": exampleNsapNativeEntry,
       "exampleNsapNativeIndex": exampleNsapNativeIndex,
       "exampleNsapNativeValue": exampleNsapNativeValue,
       "exampleOperationalTable": exampleOperationalTable,
       "exampleOperationalEntry": exampleOperationalEntry,
       "exampleOperMyComponentName": exampleOperMyComponentName,
       "exampleProvisionalTable": exampleProvisionalTable,
       "exampleProvisionalEntry": exampleProvisionalEntry,
       "exampleProvMyComponentName": exampleProvMyComponentName,
       "exampleOperDecimalSubCreatedTable": exampleOperDecimalSubCreatedTable,
       "exampleOperDecimalSubCreatedEntry": exampleOperDecimalSubCreatedEntry,
       "exampleOperDecimalSubCreatedValue": exampleOperDecimalSubCreatedValue,
       "exampleOperDecimalSubCreatedRowStatus": exampleOperDecimalSubCreatedRowStatus,
       "exampleOperFixedPtSubcomponentsCreatedTable": exampleOperFixedPtSubcomponentsCreatedTable,
       "exampleOperFixedPtSubcomponentsCreatedEntry": exampleOperFixedPtSubcomponentsCreatedEntry,
       "exampleOperFixedPtSubcomponentsCreatedValue": exampleOperFixedPtSubcomponentsCreatedValue,
       "exampleOperFixedPtSubcomponentsCreatedRowStatus": exampleOperFixedPtSubcomponentsCreatedRowStatus,
       "exampleOperStringSubCreatedTable": exampleOperStringSubCreatedTable,
       "exampleOperStringSubCreatedEntry": exampleOperStringSubCreatedEntry,
       "exampleOperStringSubCreatedValue": exampleOperStringSubCreatedValue,
       "exampleOperStringSubCreatedRowStatus": exampleOperStringSubCreatedRowStatus,
       "exampleOperEnumSubCreatedTable": exampleOperEnumSubCreatedTable,
       "exampleOperEnumSubCreatedEntry": exampleOperEnumSubCreatedEntry,
       "exampleOperEnumSubCreatedValue": exampleOperEnumSubCreatedValue,
       "exampleOperEnumSubCreatedRowStatus": exampleOperEnumSubCreatedRowStatus,
       "exampleOperSignedSubCreatedTable": exampleOperSignedSubCreatedTable,
       "exampleOperSignedSubCreatedEntry": exampleOperSignedSubCreatedEntry,
       "exampleOperSignedSubCreatedValue": exampleOperSignedSubCreatedValue,
       "exampleOperSignedSubCreatedRowStatus": exampleOperSignedSubCreatedRowStatus,
       "exampleProvDecimalSubCreatedTable": exampleProvDecimalSubCreatedTable,
       "exampleProvDecimalSubCreatedEntry": exampleProvDecimalSubCreatedEntry,
       "exampleProvDecimalSubCreatedValue": exampleProvDecimalSubCreatedValue,
       "exampleProvDecimalSubCreatedRowStatus": exampleProvDecimalSubCreatedRowStatus,
       "exampleProvFixedPtSubCreatedTable": exampleProvFixedPtSubCreatedTable,
       "exampleProvFixedPtSubCreatedEntry": exampleProvFixedPtSubCreatedEntry,
       "exampleProvFixedPtSubCreatedValue": exampleProvFixedPtSubCreatedValue,
       "exampleProvFixedPtSubCreatedRowStatus": exampleProvFixedPtSubCreatedRowStatus,
       "exampleProvSignedSubCreatedTable": exampleProvSignedSubCreatedTable,
       "exampleProvSignedSubCreatedEntry": exampleProvSignedSubCreatedEntry,
       "exampleProvSignedSubCreatedValue": exampleProvSignedSubCreatedValue,
       "exampleProvSignedSubCreatedRowStatus": exampleProvSignedSubCreatedRowStatus,
       "exampleProvStringSubCreatedTable": exampleProvStringSubCreatedTable,
       "exampleProvStringSubCreatedEntry": exampleProvStringSubCreatedEntry,
       "exampleProvStringSubCreatedValue": exampleProvStringSubCreatedValue,
       "exampleProvStringSubCreatedRowStatus": exampleProvStringSubCreatedRowStatus,
       "exampleProvEnumSubCreatedTable": exampleProvEnumSubCreatedTable,
       "exampleProvEnumSubCreatedEntry": exampleProvEnumSubCreatedEntry,
       "exampleProvEnumSubCreatedValue": exampleProvEnumSubCreatedValue,
       "exampleProvEnumSubCreatedRowStatus": exampleProvEnumSubCreatedRowStatus,
       "fri": fri,
       "friRowStatusTable": friRowStatusTable,
       "friRowStatusEntry": friRowStatusEntry,
       "friRowStatus": friRowStatus,
       "friComponentName": friComponentName,
       "friStorageType": friStorageType,
       "friIndex": friIndex,
       "friDna": friDna,
       "friDnaRowStatusTable": friDnaRowStatusTable,
       "friDnaRowStatusEntry": friDnaRowStatusEntry,
       "friDnaRowStatus": friDnaRowStatus,
       "friDnaComponentName": friDnaComponentName,
       "friDnaStorageType": friDnaStorageType,
       "friDnaIndex": friDnaIndex,
       "friDnaOperationalTable": friDnaOperationalTable,
       "friDnaOperationalEntry": friDnaOperationalEntry,
       "friDnaAttribute": friDnaAttribute,
       "friDnaProvisionalTable": friDnaProvisionalTable,
       "friDnaProvisionalEntry": friDnaProvisionalEntry,
       "friDnaTypeOfAddress": friDnaTypeOfAddress,
       "friDnaNumberPlanIndicator": friDnaNumberPlanIndicator,
       "friDnaDataNetworkAddress": friDnaDataNetworkAddress,
       "friDynamic": friDynamic,
       "friDynamicRowStatusTable": friDynamicRowStatusTable,
       "friDynamicRowStatusEntry": friDynamicRowStatusEntry,
       "friDynamicRowStatus": friDynamicRowStatus,
       "friDynamicComponentName": friDynamicComponentName,
       "friDynamicStorageType": friDynamicStorageType,
       "friDynamicIndex": friDynamicIndex,
       "friDynamicOperationalTable": friDynamicOperationalTable,
       "friDynamicOperationalEntry": friDynamicOperationalEntry,
       "friDynamicAttribute": friDynamicAttribute,
       "friDynOp": friDynOp,
       "friDynOpRowStatusTable": friDynOpRowStatusTable,
       "friDynOpRowStatusEntry": friDynOpRowStatusEntry,
       "friDynOpRowStatus": friDynOpRowStatus,
       "friDynOpComponentName": friDynOpComponentName,
       "friDynOpStorageType": friDynOpStorageType,
       "friDynOpIndex": friDynOpIndex,
       "friDynOpInitial": friDynOpInitial,
       "friDynOpInitialRowStatusTable": friDynOpInitialRowStatusTable,
       "friDynOpInitialRowStatusEntry": friDynOpInitialRowStatusEntry,
       "friDynOpInitialRowStatus": friDynOpInitialRowStatus,
       "friDynOpInitialComponentName": friDynOpInitialComponentName,
       "friDynOpInitialStorageType": friDynOpInitialStorageType,
       "friDynOpInitialIndex": friDynOpInitialIndex,
       "friDynOpInitialOperationalTable": friDynOpInitialOperationalTable,
       "friDynOpInitialOperationalEntry": friDynOpInitialOperationalEntry,
       "friDynOpInitialAttribute": friDynOpInitialAttribute,
       "friDynOpInitialProvisionedTable": friDynOpInitialProvisionedTable,
       "friDynOpInitialProvisionedEntry": friDynOpInitialProvisionedEntry,
       "friDynOpInitialProvAttribute": friDynOpInitialProvAttribute,
       "friDynOpOptional": friDynOpOptional,
       "friDynOpOptionalRowStatusTable": friDynOpOptionalRowStatusTable,
       "friDynOpOptionalRowStatusEntry": friDynOpOptionalRowStatusEntry,
       "friDynOpOptionalRowStatus": friDynOpOptionalRowStatus,
       "friDynOpOptionalComponentName": friDynOpOptionalComponentName,
       "friDynOpOptionalStorageType": friDynOpOptionalStorageType,
       "friDynOpOptionalIndex": friDynOpOptionalIndex,
       "friDynOpOptionalOperationalTable": friDynOpOptionalOperationalTable,
       "friDynOpOptionalOperationalEntry": friDynOpOptionalOperationalEntry,
       "friDynOpOptionalAttribute": friDynOpOptionalAttribute,
       "friDynOpOptionalProvisionedTable": friDynOpOptionalProvisionedTable,
       "friDynOpOptionalProvisionedEntry": friDynOpOptionalProvisionedEntry,
       "friDynOpOptionalProvAttribute": friDynOpOptionalProvAttribute,
       "friDynOpDynamic": friDynOpDynamic,
       "friDynOpDynamicRowStatusTable": friDynOpDynamicRowStatusTable,
       "friDynOpDynamicRowStatusEntry": friDynOpDynamicRowStatusEntry,
       "friDynOpDynamicRowStatus": friDynOpDynamicRowStatus,
       "friDynOpDynamicComponentName": friDynOpDynamicComponentName,
       "friDynOpDynamicStorageType": friDynOpDynamicStorageType,
       "friDynOpDynamicIndex": friDynOpDynamicIndex,
       "friDynOpDynamicOperationalTable": friDynOpDynamicOperationalTable,
       "friDynOpDynamicOperationalEntry": friDynOpDynamicOperationalEntry,
       "friDynOpDynamicAttribute": friDynOpDynamicAttribute,
       "friDynOpDynOpJr": friDynOpDynOpJr,
       "friDynOpDynOpJrRowStatusTable": friDynOpDynOpJrRowStatusTable,
       "friDynOpDynOpJrRowStatusEntry": friDynOpDynOpJrRowStatusEntry,
       "friDynOpDynOpJrRowStatus": friDynOpDynOpJrRowStatus,
       "friDynOpDynOpJrComponentName": friDynOpDynOpJrComponentName,
       "friDynOpDynOpJrStorageType": friDynOpDynOpJrStorageType,
       "friDynOpDynOpJrIndex": friDynOpDynOpJrIndex,
       "friDynOpDynOpJrOperationalTable": friDynOpDynOpJrOperationalTable,
       "friDynOpDynOpJrOperationalEntry": friDynOpDynOpJrOperationalEntry,
       "friDynOpDynOpJrAttribute": friDynOpDynOpJrAttribute,
       "friDynOpOperationalTable": friDynOpOperationalTable,
       "friDynOpOperationalEntry": friDynOpOperationalEntry,
       "friDynOpAttribute": friDynOpAttribute,
       "friEvent": friEvent,
       "friEventRowStatusTable": friEventRowStatusTable,
       "friEventRowStatusEntry": friEventRowStatusEntry,
       "friEventRowStatus": friEventRowStatus,
       "friEventComponentName": friEventComponentName,
       "friEventStorageType": friEventStorageType,
       "friEventIndex": friEventIndex,
       "friRegistered": friRegistered,
       "friRegisteredRowStatusTable": friRegisteredRowStatusTable,
       "friRegisteredRowStatusEntry": friRegisteredRowStatusEntry,
       "friRegisteredRowStatus": friRegisteredRowStatus,
       "friRegisteredComponentName": friRegisteredComponentName,
       "friRegisteredStorageType": friRegisteredStorageType,
       "friRegisteredIndex": friRegisteredIndex,
       "friRegisteredDataTable": friRegisteredDataTable,
       "friRegisteredDataEntry": friRegisteredDataEntry,
       "friRegisteredAttribute": friRegisteredAttribute,
       "friOperationalTable": friOperationalTable,
       "friOperationalEntry": friOperationalEntry,
       "friOperationalFreeSimpleAscii": friOperationalFreeSimpleAscii,
       "friOperationalFreeSimpleDashed": friOperationalFreeSimpleDashed,
       "friOperationalFreeSimpleExtended": friOperationalFreeSimpleExtended,
       "friOperationalFreeSimpleBcd": friOperationalFreeSimpleBcd,
       "friOperationalFreeSimpleSigned": friOperationalFreeSimpleSigned,
       "friOperationalFreeSimpleFixed": friOperationalFreeSimpleFixed,
       "friOperationalFreeSimpleSequence": friOperationalFreeSimpleSequence,
       "friOperationalFreeSimpleObjId": friOperationalFreeSimpleObjId,
       "friOperationalFreeSimpleComponent": friOperationalFreeSimpleComponent,
       "friOperationalFreeSimpleHex": friOperationalFreeSimpleHex,
       "friOperationalStructSetEnumeration": friOperationalStructSetEnumeration,
       "friOperationalStructSetUnsigned": friOperationalStructSetUnsigned,
       "friOperationalStructSimpleAscii": friOperationalStructSimpleAscii,
       "friOperationalStructSimpleDashed": friOperationalStructSimpleDashed,
       "friOperationalStructSimpleExtended": friOperationalStructSimpleExtended,
       "friOperationalStructSimpleBcd": friOperationalStructSimpleBcd,
       "friOperationalStructSimpleSigned": friOperationalStructSimpleSigned,
       "friOperationalStructSimpleFixed": friOperationalStructSimpleFixed,
       "friOperationalStructSimpleSequence": friOperationalStructSimpleSequence,
       "friOperationalStructSimpleEnum": friOperationalStructSimpleEnum,
       "friOperationalStructSimpleHex": friOperationalStructSimpleHex,
       "friOperationalStructSimpleUnsigned": friOperationalStructSimpleUnsigned,
       "friProvisionalTable": friProvisionalTable,
       "friProvisionalEntry": friProvisionalEntry,
       "friProvisionalStructSetEnumeration": friProvisionalStructSetEnumeration,
       "friProvisionalStructSetUnsigned": friProvisionalStructSetUnsigned,
       "friProvisionalStructSimpleAscii": friProvisionalStructSimpleAscii,
       "friProvisionalStructSimpleDashed": friProvisionalStructSimpleDashed,
       "friProvisionalStructSimpleExtended": friProvisionalStructSimpleExtended,
       "friProvisionalStructSimpleBcd": friProvisionalStructSimpleBcd,
       "friProvisionalStructSimpleSequence": friProvisionalStructSimpleSequence,
       "friProvisionalStructSimpleEnum": friProvisionalStructSimpleEnum,
       "friProvisionalStructSimpleHex": friProvisionalStructSimpleHex,
       "friProvisionalStructSimpleUnsigned": friProvisionalStructSimpleUnsigned,
       "friProvisionalStructSimpleSigned": friProvisionalStructSimpleSigned,
       "friProvisionalStructSimpleFixed": friProvisionalStructSimpleFixed,
       "friProvisionalFreeSimpleAscii": friProvisionalFreeSimpleAscii,
       "friProvisionalFreeSimpleDashed": friProvisionalFreeSimpleDashed,
       "friProvisionalFreeSimpleExtended": friProvisionalFreeSimpleExtended,
       "friProvisionalFreeSimpleBcd": friProvisionalFreeSimpleBcd,
       "friProvisionalFreeSimpleSequence": friProvisionalFreeSimpleSequence,
       "friProvisionalFreeSimpleSigned": friProvisionalFreeSimpleSigned,
       "friProvisionalFreeSimpleFixed": friProvisionalFreeSimpleFixed,
       "friProvisionalFreeSimpleObjId": friProvisionalFreeSimpleObjId,
       "friProvisionalFreeSimpleComponent": friProvisionalFreeSimpleComponent,
       "friProvisionalFreeSimpleHex": friProvisionalFreeSimpleHex,
       "friEscapeCheckAttribute": friEscapeCheckAttribute,
       "friEscapeDefaultsComponent": friEscapeDefaultsComponent,
       "friEscapeDefaultsGroup": friEscapeDefaultsGroup,
       "friEscapeSet": friEscapeSet,
       "friEscapeCopyComponent": friEscapeCopyComponent,
       "friEscapeCopyGroup": friEscapeCopyGroup,
       "friEscapeCopyAttribute": friEscapeCopyAttribute,
       "friStateTable": friStateTable,
       "friStateEntry": friStateEntry,
       "friAdminState": friAdminState,
       "friOperationalState": friOperationalState,
       "friUsageState": friUsageState,
       "friAvailabilityStatus": friAvailabilityStatus,
       "friProceduralStatus": friProceduralStatus,
       "friControlStatus": friControlStatus,
       "friAlarmStatus": friAlarmStatus,
       "friStandbyStatus": friStandbyStatus,
       "friUnknownStatus": friUnknownStatus,
       "friPfListAsciiTable": friPfListAsciiTable,
       "friPfListAsciiEntry": friPfListAsciiEntry,
       "friPfListAsciiValue": friPfListAsciiValue,
       "friPfListAsciiRowStatus": friPfListAsciiRowStatus,
       "friPfListUnsignedTable": friPfListUnsignedTable,
       "friPfListUnsignedEntry": friPfListUnsignedEntry,
       "friPfListUnsignedValue": friPfListUnsignedValue,
       "friPfListUnsignedRowStatus": friPfListUnsignedRowStatus,
       "friPfListFixedTable": friPfListFixedTable,
       "friPfListFixedEntry": friPfListFixedEntry,
       "friPfListFixedValue": friPfListFixedValue,
       "friPfListFixedRowStatus": friPfListFixedRowStatus,
       "friPfListSignedTable": friPfListSignedTable,
       "friPfListSignedEntry": friPfListSignedEntry,
       "friPfListSignedValue": friPfListSignedValue,
       "friPfListSignedRowStatus": friPfListSignedRowStatus,
       "friOfListComponentTable": friOfListComponentTable,
       "friOfListComponentEntry": friOfListComponentEntry,
       "friOfListComponentValue": friOfListComponentValue,
       "friOfListComponentRowStatus": friOfListComponentRowStatus,
       "friOfListEnumerationTable": friOfListEnumerationTable,
       "friOfListEnumerationEntry": friOfListEnumerationEntry,
       "friOfListEnumerationValue": friOfListEnumerationValue,
       "friOfListEnumerationRowStatus": friOfListEnumerationRowStatus,
       "registered": registered,
       "registeredRowStatusTable": registeredRowStatusTable,
       "registeredRowStatusEntry": registeredRowStatusEntry,
       "registeredRowStatus": registeredRowStatus,
       "registeredComponentName": registeredComponentName,
       "registeredStorageType": registeredStorageType,
       "registeredIndex": registeredIndex,
       "registeredDataTable": registeredDataTable,
       "registeredDataEntry": registeredDataEntry,
       "registeredAttribute": registeredAttribute,
       "casTestMIB": casTestMIB,
       "casTestGroup": casTestGroup,
       "casTestGroupBE": casTestGroupBE,
       "casTestGroupBE01": casTestGroupBE01,
       "casTestGroupBE01A": casTestGroupBE01A,
       "casTestCapabilities": casTestCapabilities,
       "casTestCapabilitiesBE": casTestCapabilitiesBE,
       "casTestCapabilitiesBE01": casTestCapabilitiesBE01,
       "casTestCapabilitiesBE01A": casTestCapabilitiesBE01A}
)
