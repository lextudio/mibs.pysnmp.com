# SNMP MIB module (Nortel-MsCarrier-MscPassport-CasTestMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-CasTestMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:06 2024
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
 RowPointer,
 RowStatus,
 StorageType,
 TimeInterval,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
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
 PassportCounter64,
 Unsigned64,
 WildcardedDigitString) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
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
    "PassportCounter64",
    "Unsigned64",
    "WildcardedDigitString")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscExample_ObjectIdentity = ObjectIdentity
mscExample = _MscExample_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000)
)
_MscExampleRowStatusTable_Object = MibTable
mscExampleRowStatusTable = _MscExampleRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1)
)
if mibBuilder.loadTexts:
    mscExampleRowStatusTable.setStatus("mandatory")
_MscExampleRowStatusEntry_Object = MibTableRow
mscExampleRowStatusEntry = _MscExampleRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1, 1)
)
mscExampleRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
)
if mibBuilder.loadTexts:
    mscExampleRowStatusEntry.setStatus("mandatory")
_MscExampleRowStatus_Type = RowStatus
_MscExampleRowStatus_Object = MibTableColumn
mscExampleRowStatus = _MscExampleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1, 1, 1),
    _MscExampleRowStatus_Type()
)
mscExampleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleRowStatus.setStatus("mandatory")
_MscExampleComponentName_Type = DisplayString
_MscExampleComponentName_Object = MibTableColumn
mscExampleComponentName = _MscExampleComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1, 1, 2),
    _MscExampleComponentName_Type()
)
mscExampleComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleComponentName.setStatus("mandatory")
_MscExampleStorageType_Type = StorageType
_MscExampleStorageType_Object = MibTableColumn
mscExampleStorageType = _MscExampleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1, 1, 4),
    _MscExampleStorageType_Type()
)
mscExampleStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleStorageType.setStatus("mandatory")
_MscExampleIndex_Type = NonReplicated
_MscExampleIndex_Object = MibTableColumn
mscExampleIndex = _MscExampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1, 1, 10),
    _MscExampleIndex_Type()
)
mscExampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIndex.setStatus("mandatory")
_MscExampleDecimal_ObjectIdentity = ObjectIdentity
mscExampleDecimal = _MscExampleDecimal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2)
)
_MscExampleDecimalRowStatusTable_Object = MibTable
mscExampleDecimalRowStatusTable = _MscExampleDecimalRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1)
)
if mibBuilder.loadTexts:
    mscExampleDecimalRowStatusTable.setStatus("mandatory")
_MscExampleDecimalRowStatusEntry_Object = MibTableRow
mscExampleDecimalRowStatusEntry = _MscExampleDecimalRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1, 1)
)
mscExampleDecimalRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalRowStatusEntry.setStatus("mandatory")
_MscExampleDecimalRowStatus_Type = RowStatus
_MscExampleDecimalRowStatus_Object = MibTableColumn
mscExampleDecimalRowStatus = _MscExampleDecimalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1, 1, 1),
    _MscExampleDecimalRowStatus_Type()
)
mscExampleDecimalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalRowStatus.setStatus("mandatory")
_MscExampleDecimalComponentName_Type = DisplayString
_MscExampleDecimalComponentName_Object = MibTableColumn
mscExampleDecimalComponentName = _MscExampleDecimalComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1, 1, 2),
    _MscExampleDecimalComponentName_Type()
)
mscExampleDecimalComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDecimalComponentName.setStatus("mandatory")
_MscExampleDecimalStorageType_Type = StorageType
_MscExampleDecimalStorageType_Object = MibTableColumn
mscExampleDecimalStorageType = _MscExampleDecimalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1, 1, 4),
    _MscExampleDecimalStorageType_Type()
)
mscExampleDecimalStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDecimalStorageType.setStatus("mandatory")


class _MscExampleDecimalIndex_Type(Integer32):
    """Custom type mscExampleDecimalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscExampleDecimalIndex_Type.__name__ = "Integer32"
_MscExampleDecimalIndex_Object = MibTableColumn
mscExampleDecimalIndex = _MscExampleDecimalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1, 1, 10),
    _MscExampleDecimalIndex_Type()
)
mscExampleDecimalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalIndex.setStatus("mandatory")
_MscExampleDecimalOperationalTable_Object = MibTable
mscExampleDecimalOperationalTable = _MscExampleDecimalOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOperationalTable.setStatus("mandatory")
_MscExampleDecimalOperationalEntry_Object = MibTableRow
mscExampleDecimalOperationalEntry = _MscExampleDecimalOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1)
)
mscExampleDecimalOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOperationalEntry.setStatus("mandatory")


class _MscExampleDecimalOperStructInteger_Type(Unsigned32):
    """Custom type mscExampleDecimalOperStructInteger based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDecimalOperStructInteger_Type.__name__ = "Unsigned32"
_MscExampleDecimalOperStructInteger_Object = MibTableColumn
mscExampleDecimalOperStructInteger = _MscExampleDecimalOperStructInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 1),
    _MscExampleDecimalOperStructInteger_Type()
)
mscExampleDecimalOperStructInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOperStructInteger.setStatus("mandatory")


class _MscExampleDecimalOperStructIntSet_Type(OctetString):
    """Custom type mscExampleDecimalOperStructIntSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscExampleDecimalOperStructIntSet_Type.__name__ = "OctetString"
_MscExampleDecimalOperStructIntSet_Object = MibTableColumn
mscExampleDecimalOperStructIntSet = _MscExampleDecimalOperStructIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 2),
    _MscExampleDecimalOperStructIntSet_Type()
)
mscExampleDecimalOperStructIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOperStructIntSet.setStatus("mandatory")


class _MscExampleDecimalOperFreeInteger_Type(Unsigned32):
    """Custom type mscExampleDecimalOperFreeInteger based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(100, 200),
    )


_MscExampleDecimalOperFreeInteger_Type.__name__ = "Unsigned32"
_MscExampleDecimalOperFreeInteger_Object = MibTableColumn
mscExampleDecimalOperFreeInteger = _MscExampleDecimalOperFreeInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 3),
    _MscExampleDecimalOperFreeInteger_Type()
)
mscExampleDecimalOperFreeInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOperFreeInteger.setStatus("mandatory")


class _MscExampleDecimalOperFreeIntSet_Type(OctetString):
    """Custom type mscExampleDecimalOperFreeIntSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscExampleDecimalOperFreeIntSet_Type.__name__ = "OctetString"
_MscExampleDecimalOperFreeIntSet_Object = MibTableColumn
mscExampleDecimalOperFreeIntSet = _MscExampleDecimalOperFreeIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 4),
    _MscExampleDecimalOperFreeIntSet_Type()
)
mscExampleDecimalOperFreeIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOperFreeIntSet.setStatus("mandatory")
_MscExampleDecimalOperFreeCounter32_Type = Counter32
_MscExampleDecimalOperFreeCounter32_Object = MibTableColumn
mscExampleDecimalOperFreeCounter32 = _MscExampleDecimalOperFreeCounter32_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 5),
    _MscExampleDecimalOperFreeCounter32_Type()
)
mscExampleDecimalOperFreeCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDecimalOperFreeCounter32.setStatus("mandatory")


class _MscExampleDecimalOperFreeGauge32_Type(Gauge32):
    """Custom type mscExampleDecimalOperFreeGauge32 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscExampleDecimalOperFreeGauge32_Type.__name__ = "Gauge32"
_MscExampleDecimalOperFreeGauge32_Object = MibTableColumn
mscExampleDecimalOperFreeGauge32 = _MscExampleDecimalOperFreeGauge32_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 6),
    _MscExampleDecimalOperFreeGauge32_Type()
)
mscExampleDecimalOperFreeGauge32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOperFreeGauge32.setStatus("mandatory")


class _MscExampleDecimalOperFreeTimeInterval_Type(TimeInterval):
    """Custom type mscExampleDecimalOperFreeTimeInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscExampleDecimalOperFreeTimeInterval_Type.__name__ = "TimeInterval"
_MscExampleDecimalOperFreeTimeInterval_Object = MibTableColumn
mscExampleDecimalOperFreeTimeInterval = _MscExampleDecimalOperFreeTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 10, 1, 7),
    _MscExampleDecimalOperFreeTimeInterval_Type()
)
mscExampleDecimalOperFreeTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOperFreeTimeInterval.setStatus("mandatory")
_MscExampleDecimalProvisionalTable_Object = MibTable
mscExampleDecimalProvisionalTable = _MscExampleDecimalProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11)
)
if mibBuilder.loadTexts:
    mscExampleDecimalProvisionalTable.setStatus("mandatory")
_MscExampleDecimalProvisionalEntry_Object = MibTableRow
mscExampleDecimalProvisionalEntry = _MscExampleDecimalProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1)
)
mscExampleDecimalProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalProvisionalEntry.setStatus("mandatory")
_MscExampleDecimalProvDecimalSub_Type = Link
_MscExampleDecimalProvDecimalSub_Object = MibTableColumn
mscExampleDecimalProvDecimalSub = _MscExampleDecimalProvDecimalSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 1),
    _MscExampleDecimalProvDecimalSub_Type()
)
mscExampleDecimalProvDecimalSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvDecimalSub.setStatus("mandatory")


class _MscExampleDecimalProvStructInteger_Type(Unsigned32):
    """Custom type mscExampleDecimalProvStructInteger based on Unsigned32"""
    defaultValue = 253

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
        ValueRangeConstraint(253, 253),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )


_MscExampleDecimalProvStructInteger_Type.__name__ = "Unsigned32"
_MscExampleDecimalProvStructInteger_Object = MibTableColumn
mscExampleDecimalProvStructInteger = _MscExampleDecimalProvStructInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 2),
    _MscExampleDecimalProvStructInteger_Type()
)
mscExampleDecimalProvStructInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvStructInteger.setStatus("mandatory")


class _MscExampleDecimalProvStructIntSet_Type(OctetString):
    """Custom type mscExampleDecimalProvStructIntSet based on OctetString"""
    defaultHexValue = "aaaa"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscExampleDecimalProvStructIntSet_Type.__name__ = "OctetString"
_MscExampleDecimalProvStructIntSet_Object = MibTableColumn
mscExampleDecimalProvStructIntSet = _MscExampleDecimalProvStructIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 3),
    _MscExampleDecimalProvStructIntSet_Type()
)
mscExampleDecimalProvStructIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvStructIntSet.setStatus("mandatory")


class _MscExampleDecimalProvFreeInteger_Type(Unsigned32):
    """Custom type mscExampleDecimalProvFreeInteger based on Unsigned32"""
    defaultValue = 101

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(100, 200),
    )


_MscExampleDecimalProvFreeInteger_Type.__name__ = "Unsigned32"
_MscExampleDecimalProvFreeInteger_Object = MibTableColumn
mscExampleDecimalProvFreeInteger = _MscExampleDecimalProvFreeInteger_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 4),
    _MscExampleDecimalProvFreeInteger_Type()
)
mscExampleDecimalProvFreeInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvFreeInteger.setStatus("mandatory")


class _MscExampleDecimalProvFreeInteger1_Type(Unsigned32):
    """Custom type mscExampleDecimalProvFreeInteger1 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 200),
    )


_MscExampleDecimalProvFreeInteger1_Type.__name__ = "Unsigned32"
_MscExampleDecimalProvFreeInteger1_Object = MibTableColumn
mscExampleDecimalProvFreeInteger1 = _MscExampleDecimalProvFreeInteger1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 5),
    _MscExampleDecimalProvFreeInteger1_Type()
)
mscExampleDecimalProvFreeInteger1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvFreeInteger1.setStatus("mandatory")


class _MscExampleDecimalProvFreeInteger2_Type(Unsigned32):
    """Custom type mscExampleDecimalProvFreeInteger2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscExampleDecimalProvFreeInteger2_Type.__name__ = "Unsigned32"
_MscExampleDecimalProvFreeInteger2_Object = MibTableColumn
mscExampleDecimalProvFreeInteger2 = _MscExampleDecimalProvFreeInteger2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 6),
    _MscExampleDecimalProvFreeInteger2_Type()
)
mscExampleDecimalProvFreeInteger2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvFreeInteger2.setStatus("mandatory")


class _MscExampleDecimalProvFreeIntSet_Type(OctetString):
    """Custom type mscExampleDecimalProvFreeIntSet based on OctetString"""
    defaultHexValue = "5555"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscExampleDecimalProvFreeIntSet_Type.__name__ = "OctetString"
_MscExampleDecimalProvFreeIntSet_Object = MibTableColumn
mscExampleDecimalProvFreeIntSet = _MscExampleDecimalProvFreeIntSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 7),
    _MscExampleDecimalProvFreeIntSet_Type()
)
mscExampleDecimalProvFreeIntSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvFreeIntSet.setStatus("mandatory")


class _MscExampleDecimalProvFreeIntSet1_Type(OctetString):
    """Custom type mscExampleDecimalProvFreeIntSet1 based on OctetString"""
    defaultHexValue = "80000001"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscExampleDecimalProvFreeIntSet1_Type.__name__ = "OctetString"
_MscExampleDecimalProvFreeIntSet1_Object = MibTableColumn
mscExampleDecimalProvFreeIntSet1 = _MscExampleDecimalProvFreeIntSet1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 11, 1, 8),
    _MscExampleDecimalProvFreeIntSet1_Type()
)
mscExampleDecimalProvFreeIntSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalProvFreeIntSet1.setStatus("mandatory")
_MscExampleDecimalOsIntVectorTable_Object = MibTable
mscExampleDecimalOsIntVectorTable = _MscExampleDecimalOsIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1012)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntVectorTable.setStatus("mandatory")
_MscExampleDecimalOsIntVectorEntry_Object = MibTableRow
mscExampleDecimalOsIntVectorEntry = _MscExampleDecimalOsIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1012, 1)
)
mscExampleDecimalOsIntVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOsIntVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntVectorEntry.setStatus("mandatory")


class _MscExampleDecimalOsIntVectorIndex_Type(Integer32):
    """Custom type mscExampleDecimalOsIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDecimalOsIntVectorIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOsIntVectorIndex_Object = MibTableColumn
mscExampleDecimalOsIntVectorIndex = _MscExampleDecimalOsIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1012, 1, 1),
    _MscExampleDecimalOsIntVectorIndex_Type()
)
mscExampleDecimalOsIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntVectorIndex.setStatus("mandatory")


class _MscExampleDecimalOsIntVectorValue_Type(Unsigned32):
    """Custom type mscExampleDecimalOsIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscExampleDecimalOsIntVectorValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalOsIntVectorValue_Object = MibTableColumn
mscExampleDecimalOsIntVectorValue = _MscExampleDecimalOsIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1012, 1, 2),
    _MscExampleDecimalOsIntVectorValue_Type()
)
mscExampleDecimalOsIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntVectorValue.setStatus("mandatory")
_MscExampleDecimalOsIntArrayTable_Object = MibTable
mscExampleDecimalOsIntArrayTable = _MscExampleDecimalOsIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1013)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntArrayTable.setStatus("mandatory")
_MscExampleDecimalOsIntArrayEntry_Object = MibTableRow
mscExampleDecimalOsIntArrayEntry = _MscExampleDecimalOsIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1013, 1)
)
mscExampleDecimalOsIntArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOsIntArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOsIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntArrayEntry.setStatus("mandatory")


class _MscExampleDecimalOsIntArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDecimalOsIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDecimalOsIntArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOsIntArrayRowIndex_Object = MibTableColumn
mscExampleDecimalOsIntArrayRowIndex = _MscExampleDecimalOsIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1013, 1, 1),
    _MscExampleDecimalOsIntArrayRowIndex_Type()
)
mscExampleDecimalOsIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntArrayRowIndex.setStatus("mandatory")


class _MscExampleDecimalOsIntArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDecimalOsIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDecimalOsIntArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOsIntArrayColumnIndex_Object = MibTableColumn
mscExampleDecimalOsIntArrayColumnIndex = _MscExampleDecimalOsIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1013, 1, 2),
    _MscExampleDecimalOsIntArrayColumnIndex_Type()
)
mscExampleDecimalOsIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntArrayColumnIndex.setStatus("mandatory")


class _MscExampleDecimalOsIntArrayValue_Type(Unsigned32):
    """Custom type mscExampleDecimalOsIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDecimalOsIntArrayValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalOsIntArrayValue_Object = MibTableColumn
mscExampleDecimalOsIntArrayValue = _MscExampleDecimalOsIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1013, 1, 3),
    _MscExampleDecimalOsIntArrayValue_Type()
)
mscExampleDecimalOsIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOsIntArrayValue.setStatus("mandatory")
_MscExampleDecimalOfIntVectorTable_Object = MibTable
mscExampleDecimalOfIntVectorTable = _MscExampleDecimalOfIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1014)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntVectorTable.setStatus("mandatory")
_MscExampleDecimalOfIntVectorEntry_Object = MibTableRow
mscExampleDecimalOfIntVectorEntry = _MscExampleDecimalOfIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1014, 1)
)
mscExampleDecimalOfIntVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOfIntVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntVectorEntry.setStatus("mandatory")


class _MscExampleDecimalOfIntVectorIndex_Type(Integer32):
    """Custom type mscExampleDecimalOfIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDecimalOfIntVectorIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOfIntVectorIndex_Object = MibTableColumn
mscExampleDecimalOfIntVectorIndex = _MscExampleDecimalOfIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1014, 1, 1),
    _MscExampleDecimalOfIntVectorIndex_Type()
)
mscExampleDecimalOfIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntVectorIndex.setStatus("mandatory")


class _MscExampleDecimalOfIntVectorValue_Type(Unsigned32):
    """Custom type mscExampleDecimalOfIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscExampleDecimalOfIntVectorValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalOfIntVectorValue_Object = MibTableColumn
mscExampleDecimalOfIntVectorValue = _MscExampleDecimalOfIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1014, 1, 2),
    _MscExampleDecimalOfIntVectorValue_Type()
)
mscExampleDecimalOfIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntVectorValue.setStatus("mandatory")
_MscExampleDecimalOfIntArrayTable_Object = MibTable
mscExampleDecimalOfIntArrayTable = _MscExampleDecimalOfIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1015)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntArrayTable.setStatus("mandatory")
_MscExampleDecimalOfIntArrayEntry_Object = MibTableRow
mscExampleDecimalOfIntArrayEntry = _MscExampleDecimalOfIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1015, 1)
)
mscExampleDecimalOfIntArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOfIntArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOfIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntArrayEntry.setStatus("mandatory")


class _MscExampleDecimalOfIntArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDecimalOfIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDecimalOfIntArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOfIntArrayRowIndex_Object = MibTableColumn
mscExampleDecimalOfIntArrayRowIndex = _MscExampleDecimalOfIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1015, 1, 1),
    _MscExampleDecimalOfIntArrayRowIndex_Type()
)
mscExampleDecimalOfIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntArrayRowIndex.setStatus("mandatory")


class _MscExampleDecimalOfIntArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDecimalOfIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDecimalOfIntArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOfIntArrayColumnIndex_Object = MibTableColumn
mscExampleDecimalOfIntArrayColumnIndex = _MscExampleDecimalOfIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1015, 1, 2),
    _MscExampleDecimalOfIntArrayColumnIndex_Type()
)
mscExampleDecimalOfIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntArrayColumnIndex.setStatus("mandatory")


class _MscExampleDecimalOfIntArrayValue_Type(Unsigned32):
    """Custom type mscExampleDecimalOfIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDecimalOfIntArrayValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalOfIntArrayValue_Object = MibTableColumn
mscExampleDecimalOfIntArrayValue = _MscExampleDecimalOfIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1015, 1, 3),
    _MscExampleDecimalOfIntArrayValue_Type()
)
mscExampleDecimalOfIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntArrayValue.setStatus("mandatory")
_MscExampleDecimalOfIntReplicatedTable_Object = MibTable
mscExampleDecimalOfIntReplicatedTable = _MscExampleDecimalOfIntReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1016)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntReplicatedTable.setStatus("mandatory")
_MscExampleDecimalOfIntReplicatedEntry_Object = MibTableRow
mscExampleDecimalOfIntReplicatedEntry = _MscExampleDecimalOfIntReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1016, 1)
)
mscExampleDecimalOfIntReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOfIntReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntReplicatedEntry.setStatus("mandatory")


class _MscExampleDecimalOfIntReplicatedIndex_Type(Integer32):
    """Custom type mscExampleDecimalOfIntReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDecimalOfIntReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleDecimalOfIntReplicatedIndex_Object = MibTableColumn
mscExampleDecimalOfIntReplicatedIndex = _MscExampleDecimalOfIntReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1016, 1, 1),
    _MscExampleDecimalOfIntReplicatedIndex_Type()
)
mscExampleDecimalOfIntReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntReplicatedIndex.setStatus("mandatory")


class _MscExampleDecimalOfIntReplicatedValue_Type(Unsigned32):
    """Custom type mscExampleDecimalOfIntReplicatedValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscExampleDecimalOfIntReplicatedValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalOfIntReplicatedValue_Object = MibTableColumn
mscExampleDecimalOfIntReplicatedValue = _MscExampleDecimalOfIntReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1016, 1, 2),
    _MscExampleDecimalOfIntReplicatedValue_Type()
)
mscExampleDecimalOfIntReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntReplicatedValue.setStatus("mandatory")
_MscExampleDecimalOfIntReplicatedRowStatus_Type = RowStatus
_MscExampleDecimalOfIntReplicatedRowStatus_Object = MibTableColumn
mscExampleDecimalOfIntReplicatedRowStatus = _MscExampleDecimalOfIntReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1016, 1, 3),
    _MscExampleDecimalOfIntReplicatedRowStatus_Type()
)
mscExampleDecimalOfIntReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntReplicatedRowStatus.setStatus("mandatory")
_MscExampleDecimalOfIntListTable_Object = MibTable
mscExampleDecimalOfIntListTable = _MscExampleDecimalOfIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1017)
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntListTable.setStatus("mandatory")
_MscExampleDecimalOfIntListEntry_Object = MibTableRow
mscExampleDecimalOfIntListEntry = _MscExampleDecimalOfIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1017, 1)
)
mscExampleDecimalOfIntListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalOfIntListValue"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntListEntry.setStatus("mandatory")


class _MscExampleDecimalOfIntListValue_Type(Integer32):
    """Custom type mscExampleDecimalOfIntListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(1000, 2000),
    )


_MscExampleDecimalOfIntListValue_Type.__name__ = "Integer32"
_MscExampleDecimalOfIntListValue_Object = MibTableColumn
mscExampleDecimalOfIntListValue = _MscExampleDecimalOfIntListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1017, 1, 1),
    _MscExampleDecimalOfIntListValue_Type()
)
mscExampleDecimalOfIntListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntListValue.setStatus("mandatory")
_MscExampleDecimalOfIntListRowStatus_Type = RowStatus
_MscExampleDecimalOfIntListRowStatus_Object = MibTableColumn
mscExampleDecimalOfIntListRowStatus = _MscExampleDecimalOfIntListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1017, 1, 2),
    _MscExampleDecimalOfIntListRowStatus_Type()
)
mscExampleDecimalOfIntListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDecimalOfIntListRowStatus.setStatus("mandatory")
_MscExampleDecimalPsIntVectorTable_Object = MibTable
mscExampleDecimalPsIntVectorTable = _MscExampleDecimalPsIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1018)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntVectorTable.setStatus("mandatory")
_MscExampleDecimalPsIntVectorEntry_Object = MibTableRow
mscExampleDecimalPsIntVectorEntry = _MscExampleDecimalPsIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1018, 1)
)
mscExampleDecimalPsIntVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPsIntVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntVectorEntry.setStatus("mandatory")


class _MscExampleDecimalPsIntVectorIndex_Type(Integer32):
    """Custom type mscExampleDecimalPsIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDecimalPsIntVectorIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPsIntVectorIndex_Object = MibTableColumn
mscExampleDecimalPsIntVectorIndex = _MscExampleDecimalPsIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1018, 1, 1),
    _MscExampleDecimalPsIntVectorIndex_Type()
)
mscExampleDecimalPsIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntVectorIndex.setStatus("mandatory")


class _MscExampleDecimalPsIntVectorValue_Type(Unsigned32):
    """Custom type mscExampleDecimalPsIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscExampleDecimalPsIntVectorValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalPsIntVectorValue_Object = MibTableColumn
mscExampleDecimalPsIntVectorValue = _MscExampleDecimalPsIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1018, 1, 2),
    _MscExampleDecimalPsIntVectorValue_Type()
)
mscExampleDecimalPsIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntVectorValue.setStatus("mandatory")
_MscExampleDecimalPsIntArrayTable_Object = MibTable
mscExampleDecimalPsIntArrayTable = _MscExampleDecimalPsIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1019)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntArrayTable.setStatus("mandatory")
_MscExampleDecimalPsIntArrayEntry_Object = MibTableRow
mscExampleDecimalPsIntArrayEntry = _MscExampleDecimalPsIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1019, 1)
)
mscExampleDecimalPsIntArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPsIntArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPsIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntArrayEntry.setStatus("mandatory")


class _MscExampleDecimalPsIntArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDecimalPsIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDecimalPsIntArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPsIntArrayRowIndex_Object = MibTableColumn
mscExampleDecimalPsIntArrayRowIndex = _MscExampleDecimalPsIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1019, 1, 1),
    _MscExampleDecimalPsIntArrayRowIndex_Type()
)
mscExampleDecimalPsIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntArrayRowIndex.setStatus("mandatory")


class _MscExampleDecimalPsIntArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDecimalPsIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDecimalPsIntArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPsIntArrayColumnIndex_Object = MibTableColumn
mscExampleDecimalPsIntArrayColumnIndex = _MscExampleDecimalPsIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1019, 1, 2),
    _MscExampleDecimalPsIntArrayColumnIndex_Type()
)
mscExampleDecimalPsIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntArrayColumnIndex.setStatus("mandatory")


class _MscExampleDecimalPsIntArrayValue_Type(Unsigned32):
    """Custom type mscExampleDecimalPsIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDecimalPsIntArrayValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalPsIntArrayValue_Object = MibTableColumn
mscExampleDecimalPsIntArrayValue = _MscExampleDecimalPsIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1019, 1, 3),
    _MscExampleDecimalPsIntArrayValue_Type()
)
mscExampleDecimalPsIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPsIntArrayValue.setStatus("mandatory")
_MscExampleDecimalPfIntVectorTable_Object = MibTable
mscExampleDecimalPfIntVectorTable = _MscExampleDecimalPfIntVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1020)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVectorTable.setStatus("mandatory")
_MscExampleDecimalPfIntVectorEntry_Object = MibTableRow
mscExampleDecimalPfIntVectorEntry = _MscExampleDecimalPfIntVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1020, 1)
)
mscExampleDecimalPfIntVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVectorEntry.setStatus("mandatory")


class _MscExampleDecimalPfIntVectorIndex_Type(Integer32):
    """Custom type mscExampleDecimalPfIntVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDecimalPfIntVectorIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntVectorIndex_Object = MibTableColumn
mscExampleDecimalPfIntVectorIndex = _MscExampleDecimalPfIntVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1020, 1, 1),
    _MscExampleDecimalPfIntVectorIndex_Type()
)
mscExampleDecimalPfIntVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVectorIndex.setStatus("mandatory")


class _MscExampleDecimalPfIntVectorValue_Type(Unsigned32):
    """Custom type mscExampleDecimalPfIntVectorValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscExampleDecimalPfIntVectorValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalPfIntVectorValue_Object = MibTableColumn
mscExampleDecimalPfIntVectorValue = _MscExampleDecimalPfIntVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1020, 1, 2),
    _MscExampleDecimalPfIntVectorValue_Type()
)
mscExampleDecimalPfIntVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVectorValue.setStatus("mandatory")
_MscExampleDecimalPfIntVector1Table_Object = MibTable
mscExampleDecimalPfIntVector1Table = _MscExampleDecimalPfIntVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1021)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVector1Table.setStatus("mandatory")
_MscExampleDecimalPfIntVector1Entry_Object = MibTableRow
mscExampleDecimalPfIntVector1Entry = _MscExampleDecimalPfIntVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1021, 1)
)
mscExampleDecimalPfIntVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVector1Entry.setStatus("mandatory")


class _MscExampleDecimalPfIntVector1Index_Type(Integer32):
    """Custom type mscExampleDecimalPfIntVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscExampleDecimalPfIntVector1Index_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntVector1Index_Object = MibTableColumn
mscExampleDecimalPfIntVector1Index = _MscExampleDecimalPfIntVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1021, 1, 1),
    _MscExampleDecimalPfIntVector1Index_Type()
)
mscExampleDecimalPfIntVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVector1Index.setStatus("mandatory")


class _MscExampleDecimalPfIntVector1Value_Type(Unsigned32):
    """Custom type mscExampleDecimalPfIntVector1Value based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
        ValueRangeConstraint(100, 150),
    )


_MscExampleDecimalPfIntVector1Value_Type.__name__ = "Unsigned32"
_MscExampleDecimalPfIntVector1Value_Object = MibTableColumn
mscExampleDecimalPfIntVector1Value = _MscExampleDecimalPfIntVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1021, 1, 2),
    _MscExampleDecimalPfIntVector1Value_Type()
)
mscExampleDecimalPfIntVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntVector1Value.setStatus("mandatory")
_MscExampleDecimalPfIntArrayTable_Object = MibTable
mscExampleDecimalPfIntArrayTable = _MscExampleDecimalPfIntArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1022)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArrayTable.setStatus("mandatory")
_MscExampleDecimalPfIntArrayEntry_Object = MibTableRow
mscExampleDecimalPfIntArrayEntry = _MscExampleDecimalPfIntArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1022, 1)
)
mscExampleDecimalPfIntArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArrayEntry.setStatus("mandatory")


class _MscExampleDecimalPfIntArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDecimalPfIntArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDecimalPfIntArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntArrayRowIndex_Object = MibTableColumn
mscExampleDecimalPfIntArrayRowIndex = _MscExampleDecimalPfIntArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1022, 1, 1),
    _MscExampleDecimalPfIntArrayRowIndex_Type()
)
mscExampleDecimalPfIntArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArrayRowIndex.setStatus("mandatory")


class _MscExampleDecimalPfIntArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDecimalPfIntArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDecimalPfIntArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntArrayColumnIndex_Object = MibTableColumn
mscExampleDecimalPfIntArrayColumnIndex = _MscExampleDecimalPfIntArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1022, 1, 2),
    _MscExampleDecimalPfIntArrayColumnIndex_Type()
)
mscExampleDecimalPfIntArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArrayColumnIndex.setStatus("mandatory")


class _MscExampleDecimalPfIntArrayValue_Type(Unsigned32):
    """Custom type mscExampleDecimalPfIntArrayValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDecimalPfIntArrayValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalPfIntArrayValue_Object = MibTableColumn
mscExampleDecimalPfIntArrayValue = _MscExampleDecimalPfIntArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1022, 1, 3),
    _MscExampleDecimalPfIntArrayValue_Type()
)
mscExampleDecimalPfIntArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArrayValue.setStatus("mandatory")
_MscExampleDecimalPfIntArray1Table_Object = MibTable
mscExampleDecimalPfIntArray1Table = _MscExampleDecimalPfIntArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1023)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArray1Table.setStatus("mandatory")
_MscExampleDecimalPfIntArray1Entry_Object = MibTableRow
mscExampleDecimalPfIntArray1Entry = _MscExampleDecimalPfIntArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1023, 1)
)
mscExampleDecimalPfIntArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntArray1RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArray1Entry.setStatus("mandatory")


class _MscExampleDecimalPfIntArray1RowIndex_Type(Integer32):
    """Custom type mscExampleDecimalPfIntArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDecimalPfIntArray1RowIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntArray1RowIndex_Object = MibTableColumn
mscExampleDecimalPfIntArray1RowIndex = _MscExampleDecimalPfIntArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1023, 1, 1),
    _MscExampleDecimalPfIntArray1RowIndex_Type()
)
mscExampleDecimalPfIntArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArray1RowIndex.setStatus("mandatory")


class _MscExampleDecimalPfIntArray1ColumnIndex_Type(Integer32):
    """Custom type mscExampleDecimalPfIntArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDecimalPfIntArray1ColumnIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntArray1ColumnIndex_Object = MibTableColumn
mscExampleDecimalPfIntArray1ColumnIndex = _MscExampleDecimalPfIntArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1023, 1, 2),
    _MscExampleDecimalPfIntArray1ColumnIndex_Type()
)
mscExampleDecimalPfIntArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArray1ColumnIndex.setStatus("mandatory")


class _MscExampleDecimalPfIntArray1Value_Type(Unsigned32):
    """Custom type mscExampleDecimalPfIntArray1Value based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
        ValueRangeConstraint(20, 200),
    )


_MscExampleDecimalPfIntArray1Value_Type.__name__ = "Unsigned32"
_MscExampleDecimalPfIntArray1Value_Object = MibTableColumn
mscExampleDecimalPfIntArray1Value = _MscExampleDecimalPfIntArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1023, 1, 3),
    _MscExampleDecimalPfIntArray1Value_Type()
)
mscExampleDecimalPfIntArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntArray1Value.setStatus("mandatory")
_MscExampleDecimalPfIntReplicatedTable_Object = MibTable
mscExampleDecimalPfIntReplicatedTable = _MscExampleDecimalPfIntReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1024)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicatedTable.setStatus("mandatory")
_MscExampleDecimalPfIntReplicatedEntry_Object = MibTableRow
mscExampleDecimalPfIntReplicatedEntry = _MscExampleDecimalPfIntReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1024, 1)
)
mscExampleDecimalPfIntReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicatedEntry.setStatus("mandatory")


class _MscExampleDecimalPfIntReplicatedIndex_Type(Integer32):
    """Custom type mscExampleDecimalPfIntReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDecimalPfIntReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntReplicatedIndex_Object = MibTableColumn
mscExampleDecimalPfIntReplicatedIndex = _MscExampleDecimalPfIntReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1024, 1, 1),
    _MscExampleDecimalPfIntReplicatedIndex_Type()
)
mscExampleDecimalPfIntReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicatedIndex.setStatus("mandatory")


class _MscExampleDecimalPfIntReplicatedValue_Type(Unsigned32):
    """Custom type mscExampleDecimalPfIntReplicatedValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscExampleDecimalPfIntReplicatedValue_Type.__name__ = "Unsigned32"
_MscExampleDecimalPfIntReplicatedValue_Object = MibTableColumn
mscExampleDecimalPfIntReplicatedValue = _MscExampleDecimalPfIntReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1024, 1, 2),
    _MscExampleDecimalPfIntReplicatedValue_Type()
)
mscExampleDecimalPfIntReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicatedValue.setStatus("mandatory")
_MscExampleDecimalPfIntReplicatedRowStatus_Type = RowStatus
_MscExampleDecimalPfIntReplicatedRowStatus_Object = MibTableColumn
mscExampleDecimalPfIntReplicatedRowStatus = _MscExampleDecimalPfIntReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1024, 1, 3),
    _MscExampleDecimalPfIntReplicatedRowStatus_Type()
)
mscExampleDecimalPfIntReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicatedRowStatus.setStatus("mandatory")
_MscExampleDecimalPfIntReplicated1Table_Object = MibTable
mscExampleDecimalPfIntReplicated1Table = _MscExampleDecimalPfIntReplicated1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1025)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicated1Table.setStatus("mandatory")
_MscExampleDecimalPfIntReplicated1Entry_Object = MibTableRow
mscExampleDecimalPfIntReplicated1Entry = _MscExampleDecimalPfIntReplicated1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1025, 1)
)
mscExampleDecimalPfIntReplicated1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntReplicated1Index"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicated1Entry.setStatus("mandatory")


class _MscExampleDecimalPfIntReplicated1Index_Type(Integer32):
    """Custom type mscExampleDecimalPfIntReplicated1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
        ValueRangeConstraint(11, 19),
    )


_MscExampleDecimalPfIntReplicated1Index_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntReplicated1Index_Object = MibTableColumn
mscExampleDecimalPfIntReplicated1Index = _MscExampleDecimalPfIntReplicated1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1025, 1, 1),
    _MscExampleDecimalPfIntReplicated1Index_Type()
)
mscExampleDecimalPfIntReplicated1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicated1Index.setStatus("mandatory")


class _MscExampleDecimalPfIntReplicated1Value_Type(Unsigned32):
    """Custom type mscExampleDecimalPfIntReplicated1Value based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(30, 300),
    )


_MscExampleDecimalPfIntReplicated1Value_Type.__name__ = "Unsigned32"
_MscExampleDecimalPfIntReplicated1Value_Object = MibTableColumn
mscExampleDecimalPfIntReplicated1Value = _MscExampleDecimalPfIntReplicated1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1025, 1, 2),
    _MscExampleDecimalPfIntReplicated1Value_Type()
)
mscExampleDecimalPfIntReplicated1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicated1Value.setStatus("mandatory")
_MscExampleDecimalPfIntReplicated1RowStatus_Type = RowStatus
_MscExampleDecimalPfIntReplicated1RowStatus_Object = MibTableColumn
mscExampleDecimalPfIntReplicated1RowStatus = _MscExampleDecimalPfIntReplicated1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1025, 1, 3),
    _MscExampleDecimalPfIntReplicated1RowStatus_Type()
)
mscExampleDecimalPfIntReplicated1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntReplicated1RowStatus.setStatus("mandatory")
_MscExampleDecimalPfIntListTable_Object = MibTable
mscExampleDecimalPfIntListTable = _MscExampleDecimalPfIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1026)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntListTable.setStatus("mandatory")
_MscExampleDecimalPfIntListEntry_Object = MibTableRow
mscExampleDecimalPfIntListEntry = _MscExampleDecimalPfIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1026, 1)
)
mscExampleDecimalPfIntListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntListValue"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntListEntry.setStatus("mandatory")


class _MscExampleDecimalPfIntListValue_Type(Integer32):
    """Custom type mscExampleDecimalPfIntListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MscExampleDecimalPfIntListValue_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntListValue_Object = MibTableColumn
mscExampleDecimalPfIntListValue = _MscExampleDecimalPfIntListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1026, 1, 1),
    _MscExampleDecimalPfIntListValue_Type()
)
mscExampleDecimalPfIntListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntListValue.setStatus("mandatory")
_MscExampleDecimalPfIntListRowStatus_Type = RowStatus
_MscExampleDecimalPfIntListRowStatus_Object = MibTableColumn
mscExampleDecimalPfIntListRowStatus = _MscExampleDecimalPfIntListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1026, 1, 2),
    _MscExampleDecimalPfIntListRowStatus_Type()
)
mscExampleDecimalPfIntListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntListRowStatus.setStatus("mandatory")
_MscExampleDecimalPfIntList1Table_Object = MibTable
mscExampleDecimalPfIntList1Table = _MscExampleDecimalPfIntList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1027)
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntList1Table.setStatus("mandatory")
_MscExampleDecimalPfIntList1Entry_Object = MibTableRow
mscExampleDecimalPfIntList1Entry = _MscExampleDecimalPfIntList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1027, 1)
)
mscExampleDecimalPfIntList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalPfIntList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntList1Entry.setStatus("mandatory")


class _MscExampleDecimalPfIntList1Value_Type(Integer32):
    """Custom type mscExampleDecimalPfIntList1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(15, 50),
    )


_MscExampleDecimalPfIntList1Value_Type.__name__ = "Integer32"
_MscExampleDecimalPfIntList1Value_Object = MibTableColumn
mscExampleDecimalPfIntList1Value = _MscExampleDecimalPfIntList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1027, 1, 1),
    _MscExampleDecimalPfIntList1Value_Type()
)
mscExampleDecimalPfIntList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntList1Value.setStatus("mandatory")
_MscExampleDecimalPfIntList1RowStatus_Type = RowStatus
_MscExampleDecimalPfIntList1RowStatus_Object = MibTableColumn
mscExampleDecimalPfIntList1RowStatus = _MscExampleDecimalPfIntList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 2, 1027, 1, 2),
    _MscExampleDecimalPfIntList1RowStatus_Type()
)
mscExampleDecimalPfIntList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDecimalPfIntList1RowStatus.setStatus("mandatory")
_MscExampleHex_ObjectIdentity = ObjectIdentity
mscExampleHex = _MscExampleHex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3)
)
_MscExampleHexRowStatusTable_Object = MibTable
mscExampleHexRowStatusTable = _MscExampleHexRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1)
)
if mibBuilder.loadTexts:
    mscExampleHexRowStatusTable.setStatus("mandatory")
_MscExampleHexRowStatusEntry_Object = MibTableRow
mscExampleHexRowStatusEntry = _MscExampleHexRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1, 1)
)
mscExampleHexRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexRowStatusEntry.setStatus("mandatory")
_MscExampleHexRowStatus_Type = RowStatus
_MscExampleHexRowStatus_Object = MibTableColumn
mscExampleHexRowStatus = _MscExampleHexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1, 1, 1),
    _MscExampleHexRowStatus_Type()
)
mscExampleHexRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexRowStatus.setStatus("mandatory")
_MscExampleHexComponentName_Type = DisplayString
_MscExampleHexComponentName_Object = MibTableColumn
mscExampleHexComponentName = _MscExampleHexComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1, 1, 2),
    _MscExampleHexComponentName_Type()
)
mscExampleHexComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleHexComponentName.setStatus("mandatory")
_MscExampleHexStorageType_Type = StorageType
_MscExampleHexStorageType_Object = MibTableColumn
mscExampleHexStorageType = _MscExampleHexStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1, 1, 4),
    _MscExampleHexStorageType_Type()
)
mscExampleHexStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleHexStorageType.setStatus("mandatory")


class _MscExampleHexIndex_Type(Integer32):
    """Custom type mscExampleHexIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexIndex_Type.__name__ = "Integer32"
_MscExampleHexIndex_Object = MibTableColumn
mscExampleHexIndex = _MscExampleHexIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1, 1, 10),
    _MscExampleHexIndex_Type()
)
mscExampleHexIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexIndex.setStatus("mandatory")
_MscExampleHexOperationalTable_Object = MibTable
mscExampleHexOperationalTable = _MscExampleHexOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 10)
)
if mibBuilder.loadTexts:
    mscExampleHexOperationalTable.setStatus("mandatory")
_MscExampleHexOperationalEntry_Object = MibTableRow
mscExampleHexOperationalEntry = _MscExampleHexOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 10, 1)
)
mscExampleHexOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexOperationalEntry.setStatus("mandatory")


class _MscExampleHexOperStructHex_Type(Hex):
    """Custom type mscExampleHexOperStructHex based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexOperStructHex_Type.__name__ = "Hex"
_MscExampleHexOperStructHex_Object = MibTableColumn
mscExampleHexOperStructHex = _MscExampleHexOperStructHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 10, 1, 1),
    _MscExampleHexOperStructHex_Type()
)
mscExampleHexOperStructHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOperStructHex.setStatus("mandatory")


class _MscExampleHexOperFreeHex_Type(Hex):
    """Custom type mscExampleHexOperFreeHex based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexOperFreeHex_Type.__name__ = "Hex"
_MscExampleHexOperFreeHex_Object = MibTableColumn
mscExampleHexOperFreeHex = _MscExampleHexOperFreeHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 10, 1, 2),
    _MscExampleHexOperFreeHex_Type()
)
mscExampleHexOperFreeHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOperFreeHex.setStatus("mandatory")
_MscExampleHexProvisionalTable_Object = MibTable
mscExampleHexProvisionalTable = _MscExampleHexProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 11)
)
if mibBuilder.loadTexts:
    mscExampleHexProvisionalTable.setStatus("mandatory")
_MscExampleHexProvisionalEntry_Object = MibTableRow
mscExampleHexProvisionalEntry = _MscExampleHexProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 11, 1)
)
mscExampleHexProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvisionalEntry.setStatus("mandatory")
_MscExampleHexProvEnumSub_Type = Link
_MscExampleHexProvEnumSub_Object = MibTableColumn
mscExampleHexProvEnumSub = _MscExampleHexProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 11, 1, 1),
    _MscExampleHexProvEnumSub_Type()
)
mscExampleHexProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvEnumSub.setStatus("mandatory")


class _MscExampleHexProvStructHex_Type(Hex):
    """Custom type mscExampleHexProvStructHex based on Hex"""
    defaultValue = 512

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(513, 513),
        ValueRangeConstraint(514, 514),
    )


_MscExampleHexProvStructHex_Type.__name__ = "Hex"
_MscExampleHexProvStructHex_Object = MibTableColumn
mscExampleHexProvStructHex = _MscExampleHexProvStructHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 11, 1, 2),
    _MscExampleHexProvStructHex_Type()
)
mscExampleHexProvStructHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvStructHex.setStatus("mandatory")


class _MscExampleHexProvFreeHex_Type(Hex):
    """Custom type mscExampleHexProvFreeHex based on Hex"""
    defaultValue = 18

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexProvFreeHex_Type.__name__ = "Hex"
_MscExampleHexProvFreeHex_Object = MibTableColumn
mscExampleHexProvFreeHex = _MscExampleHexProvFreeHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 11, 1, 3),
    _MscExampleHexProvFreeHex_Type()
)
mscExampleHexProvFreeHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHex.setStatus("mandatory")


class _MscExampleHexProvFreeHex1_Type(Hex):
    """Custom type mscExampleHexProvFreeHex1 based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(256, 4096),
    )


_MscExampleHexProvFreeHex1_Type.__name__ = "Hex"
_MscExampleHexProvFreeHex1_Object = MibTableColumn
mscExampleHexProvFreeHex1 = _MscExampleHexProvFreeHex1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 11, 1, 4),
    _MscExampleHexProvFreeHex1_Type()
)
mscExampleHexProvFreeHex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHex1.setStatus("mandatory")
_MscExampleHexOsHexVectorTable_Object = MibTable
mscExampleHexOsHexVectorTable = _MscExampleHexOsHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1040)
)
if mibBuilder.loadTexts:
    mscExampleHexOsHexVectorTable.setStatus("mandatory")
_MscExampleHexOsHexVectorEntry_Object = MibTableRow
mscExampleHexOsHexVectorEntry = _MscExampleHexOsHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1040, 1)
)
mscExampleHexOsHexVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOsHexVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexOsHexVectorEntry.setStatus("mandatory")


class _MscExampleHexOsHexVectorIndex_Type(Integer32):
    """Custom type mscExampleHexOsHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexOsHexVectorIndex_Type.__name__ = "Integer32"
_MscExampleHexOsHexVectorIndex_Object = MibTableColumn
mscExampleHexOsHexVectorIndex = _MscExampleHexOsHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1040, 1, 1),
    _MscExampleHexOsHexVectorIndex_Type()
)
mscExampleHexOsHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOsHexVectorIndex.setStatus("mandatory")


class _MscExampleHexOsHexVectorValue_Type(Hex):
    """Custom type mscExampleHexOsHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexOsHexVectorValue_Type.__name__ = "Hex"
_MscExampleHexOsHexVectorValue_Object = MibTableColumn
mscExampleHexOsHexVectorValue = _MscExampleHexOsHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1040, 1, 2),
    _MscExampleHexOsHexVectorValue_Type()
)
mscExampleHexOsHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOsHexVectorValue.setStatus("mandatory")
_MscExampleHexOsHexArrayTable_Object = MibTable
mscExampleHexOsHexArrayTable = _MscExampleHexOsHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1041)
)
if mibBuilder.loadTexts:
    mscExampleHexOsHexArrayTable.setStatus("mandatory")
_MscExampleHexOsHexArrayEntry_Object = MibTableRow
mscExampleHexOsHexArrayEntry = _MscExampleHexOsHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1041, 1)
)
mscExampleHexOsHexArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOsHexArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOsHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexOsHexArrayEntry.setStatus("mandatory")


class _MscExampleHexOsHexArrayRowIndex_Type(Integer32):
    """Custom type mscExampleHexOsHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleHexOsHexArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleHexOsHexArrayRowIndex_Object = MibTableColumn
mscExampleHexOsHexArrayRowIndex = _MscExampleHexOsHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1041, 1, 1),
    _MscExampleHexOsHexArrayRowIndex_Type()
)
mscExampleHexOsHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOsHexArrayRowIndex.setStatus("mandatory")


class _MscExampleHexOsHexArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleHexOsHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexOsHexArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleHexOsHexArrayColumnIndex_Object = MibTableColumn
mscExampleHexOsHexArrayColumnIndex = _MscExampleHexOsHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1041, 1, 2),
    _MscExampleHexOsHexArrayColumnIndex_Type()
)
mscExampleHexOsHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOsHexArrayColumnIndex.setStatus("mandatory")


class _MscExampleHexOsHexArrayValue_Type(Hex):
    """Custom type mscExampleHexOsHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexOsHexArrayValue_Type.__name__ = "Hex"
_MscExampleHexOsHexArrayValue_Object = MibTableColumn
mscExampleHexOsHexArrayValue = _MscExampleHexOsHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1041, 1, 3),
    _MscExampleHexOsHexArrayValue_Type()
)
mscExampleHexOsHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOsHexArrayValue.setStatus("mandatory")
_MscExampleHexOfHexVectorTable_Object = MibTable
mscExampleHexOfHexVectorTable = _MscExampleHexOfHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1042)
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexVectorTable.setStatus("mandatory")
_MscExampleHexOfHexVectorEntry_Object = MibTableRow
mscExampleHexOfHexVectorEntry = _MscExampleHexOfHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1042, 1)
)
mscExampleHexOfHexVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOfHexVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexVectorEntry.setStatus("mandatory")


class _MscExampleHexOfHexVectorIndex_Type(Integer32):
    """Custom type mscExampleHexOfHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexOfHexVectorIndex_Type.__name__ = "Integer32"
_MscExampleHexOfHexVectorIndex_Object = MibTableColumn
mscExampleHexOfHexVectorIndex = _MscExampleHexOfHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1042, 1, 1),
    _MscExampleHexOfHexVectorIndex_Type()
)
mscExampleHexOfHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOfHexVectorIndex.setStatus("mandatory")


class _MscExampleHexOfHexVectorValue_Type(Hex):
    """Custom type mscExampleHexOfHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexOfHexVectorValue_Type.__name__ = "Hex"
_MscExampleHexOfHexVectorValue_Object = MibTableColumn
mscExampleHexOfHexVectorValue = _MscExampleHexOfHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1042, 1, 2),
    _MscExampleHexOfHexVectorValue_Type()
)
mscExampleHexOfHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOfHexVectorValue.setStatus("mandatory")
_MscExampleHexOfHexArrayTable_Object = MibTable
mscExampleHexOfHexArrayTable = _MscExampleHexOfHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1043)
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexArrayTable.setStatus("mandatory")
_MscExampleHexOfHexArrayEntry_Object = MibTableRow
mscExampleHexOfHexArrayEntry = _MscExampleHexOfHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1043, 1)
)
mscExampleHexOfHexArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOfHexArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOfHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexArrayEntry.setStatus("mandatory")


class _MscExampleHexOfHexArrayRowIndex_Type(Integer32):
    """Custom type mscExampleHexOfHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleHexOfHexArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleHexOfHexArrayRowIndex_Object = MibTableColumn
mscExampleHexOfHexArrayRowIndex = _MscExampleHexOfHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1043, 1, 1),
    _MscExampleHexOfHexArrayRowIndex_Type()
)
mscExampleHexOfHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOfHexArrayRowIndex.setStatus("mandatory")


class _MscExampleHexOfHexArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleHexOfHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexOfHexArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleHexOfHexArrayColumnIndex_Object = MibTableColumn
mscExampleHexOfHexArrayColumnIndex = _MscExampleHexOfHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1043, 1, 2),
    _MscExampleHexOfHexArrayColumnIndex_Type()
)
mscExampleHexOfHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOfHexArrayColumnIndex.setStatus("mandatory")


class _MscExampleHexOfHexArrayValue_Type(Hex):
    """Custom type mscExampleHexOfHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexOfHexArrayValue_Type.__name__ = "Hex"
_MscExampleHexOfHexArrayValue_Object = MibTableColumn
mscExampleHexOfHexArrayValue = _MscExampleHexOfHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1043, 1, 3),
    _MscExampleHexOfHexArrayValue_Type()
)
mscExampleHexOfHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOfHexArrayValue.setStatus("mandatory")
_MscExampleHexOfHexReplicatedTable_Object = MibTable
mscExampleHexOfHexReplicatedTable = _MscExampleHexOfHexReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1044)
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexReplicatedTable.setStatus("mandatory")
_MscExampleHexOfHexReplicatedEntry_Object = MibTableRow
mscExampleHexOfHexReplicatedEntry = _MscExampleHexOfHexReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1044, 1)
)
mscExampleHexOfHexReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOfHexReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexReplicatedEntry.setStatus("mandatory")


class _MscExampleHexOfHexReplicatedIndex_Type(Integer32):
    """Custom type mscExampleHexOfHexReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexOfHexReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleHexOfHexReplicatedIndex_Object = MibTableColumn
mscExampleHexOfHexReplicatedIndex = _MscExampleHexOfHexReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1044, 1, 1),
    _MscExampleHexOfHexReplicatedIndex_Type()
)
mscExampleHexOfHexReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexOfHexReplicatedIndex.setStatus("mandatory")


class _MscExampleHexOfHexReplicatedValue_Type(Hex):
    """Custom type mscExampleHexOfHexReplicatedValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexOfHexReplicatedValue_Type.__name__ = "Hex"
_MscExampleHexOfHexReplicatedValue_Object = MibTableColumn
mscExampleHexOfHexReplicatedValue = _MscExampleHexOfHexReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1044, 1, 2),
    _MscExampleHexOfHexReplicatedValue_Type()
)
mscExampleHexOfHexReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOfHexReplicatedValue.setStatus("mandatory")
_MscExampleHexOfHexReplicatedRowStatus_Type = RowStatus
_MscExampleHexOfHexReplicatedRowStatus_Object = MibTableColumn
mscExampleHexOfHexReplicatedRowStatus = _MscExampleHexOfHexReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1044, 1, 3),
    _MscExampleHexOfHexReplicatedRowStatus_Type()
)
mscExampleHexOfHexReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleHexOfHexReplicatedRowStatus.setStatus("mandatory")
_MscExampleHexOfHexListTable_Object = MibTable
mscExampleHexOfHexListTable = _MscExampleHexOfHexListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1045)
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexListTable.setStatus("mandatory")
_MscExampleHexOfHexListEntry_Object = MibTableRow
mscExampleHexOfHexListEntry = _MscExampleHexOfHexListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1045, 1)
)
mscExampleHexOfHexListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexOfHexListValue"),
)
if mibBuilder.loadTexts:
    mscExampleHexOfHexListEntry.setStatus("mandatory")


class _MscExampleHexOfHexListValue_Type(Integer32):
    """Custom type mscExampleHexOfHexListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscExampleHexOfHexListValue_Type.__name__ = "Integer32"
_MscExampleHexOfHexListValue_Object = MibTableColumn
mscExampleHexOfHexListValue = _MscExampleHexOfHexListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1045, 1, 1),
    _MscExampleHexOfHexListValue_Type()
)
mscExampleHexOfHexListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexOfHexListValue.setStatus("mandatory")
_MscExampleHexOfHexListRowStatus_Type = RowStatus
_MscExampleHexOfHexListRowStatus_Object = MibTableColumn
mscExampleHexOfHexListRowStatus = _MscExampleHexOfHexListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1045, 1, 2),
    _MscExampleHexOfHexListRowStatus_Type()
)
mscExampleHexOfHexListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleHexOfHexListRowStatus.setStatus("mandatory")
_MscExampleHexProvStructHexVectorTable_Object = MibTable
mscExampleHexProvStructHexVectorTable = _MscExampleHexProvStructHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1046)
)
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexVectorTable.setStatus("mandatory")
_MscExampleHexProvStructHexVectorEntry_Object = MibTableRow
mscExampleHexProvStructHexVectorEntry = _MscExampleHexProvStructHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1046, 1)
)
mscExampleHexProvStructHexVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvStructHexVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexVectorEntry.setStatus("mandatory")


class _MscExampleHexProvStructHexVectorIndex_Type(Integer32):
    """Custom type mscExampleHexProvStructHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexProvStructHexVectorIndex_Type.__name__ = "Integer32"
_MscExampleHexProvStructHexVectorIndex_Object = MibTableColumn
mscExampleHexProvStructHexVectorIndex = _MscExampleHexProvStructHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1046, 1, 1),
    _MscExampleHexProvStructHexVectorIndex_Type()
)
mscExampleHexProvStructHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexVectorIndex.setStatus("mandatory")


class _MscExampleHexProvStructHexVectorValue_Type(Hex):
    """Custom type mscExampleHexProvStructHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexProvStructHexVectorValue_Type.__name__ = "Hex"
_MscExampleHexProvStructHexVectorValue_Object = MibTableColumn
mscExampleHexProvStructHexVectorValue = _MscExampleHexProvStructHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1046, 1, 2),
    _MscExampleHexProvStructHexVectorValue_Type()
)
mscExampleHexProvStructHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexVectorValue.setStatus("mandatory")
_MscExampleHexProvStructHexArrayTable_Object = MibTable
mscExampleHexProvStructHexArrayTable = _MscExampleHexProvStructHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1047)
)
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexArrayTable.setStatus("mandatory")
_MscExampleHexProvStructHexArrayEntry_Object = MibTableRow
mscExampleHexProvStructHexArrayEntry = _MscExampleHexProvStructHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1047, 1)
)
mscExampleHexProvStructHexArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvStructHexArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvStructHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexArrayEntry.setStatus("mandatory")


class _MscExampleHexProvStructHexArrayRowIndex_Type(Integer32):
    """Custom type mscExampleHexProvStructHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleHexProvStructHexArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleHexProvStructHexArrayRowIndex_Object = MibTableColumn
mscExampleHexProvStructHexArrayRowIndex = _MscExampleHexProvStructHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1047, 1, 1),
    _MscExampleHexProvStructHexArrayRowIndex_Type()
)
mscExampleHexProvStructHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexArrayRowIndex.setStatus("mandatory")


class _MscExampleHexProvStructHexArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleHexProvStructHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexProvStructHexArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleHexProvStructHexArrayColumnIndex_Object = MibTableColumn
mscExampleHexProvStructHexArrayColumnIndex = _MscExampleHexProvStructHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1047, 1, 2),
    _MscExampleHexProvStructHexArrayColumnIndex_Type()
)
mscExampleHexProvStructHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexArrayColumnIndex.setStatus("mandatory")


class _MscExampleHexProvStructHexArrayValue_Type(Hex):
    """Custom type mscExampleHexProvStructHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexProvStructHexArrayValue_Type.__name__ = "Hex"
_MscExampleHexProvStructHexArrayValue_Object = MibTableColumn
mscExampleHexProvStructHexArrayValue = _MscExampleHexProvStructHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1047, 1, 3),
    _MscExampleHexProvStructHexArrayValue_Type()
)
mscExampleHexProvStructHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvStructHexArrayValue.setStatus("mandatory")
_MscExampleHexProvFreeHexVectorTable_Object = MibTable
mscExampleHexProvFreeHexVectorTable = _MscExampleHexProvFreeHexVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1048)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVectorTable.setStatus("mandatory")
_MscExampleHexProvFreeHexVectorEntry_Object = MibTableRow
mscExampleHexProvFreeHexVectorEntry = _MscExampleHexProvFreeHexVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1048, 1)
)
mscExampleHexProvFreeHexVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVectorEntry.setStatus("mandatory")


class _MscExampleHexProvFreeHexVectorIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexProvFreeHexVectorIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexVectorIndex_Object = MibTableColumn
mscExampleHexProvFreeHexVectorIndex = _MscExampleHexProvFreeHexVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1048, 1, 1),
    _MscExampleHexProvFreeHexVectorIndex_Type()
)
mscExampleHexProvFreeHexVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVectorIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexVectorValue_Type(Hex):
    """Custom type mscExampleHexProvFreeHexVectorValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexProvFreeHexVectorValue_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexVectorValue_Object = MibTableColumn
mscExampleHexProvFreeHexVectorValue = _MscExampleHexProvFreeHexVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1048, 1, 2),
    _MscExampleHexProvFreeHexVectorValue_Type()
)
mscExampleHexProvFreeHexVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVectorValue.setStatus("mandatory")
_MscExampleHexProvFreeHexVector1Table_Object = MibTable
mscExampleHexProvFreeHexVector1Table = _MscExampleHexProvFreeHexVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1049)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector1Table.setStatus("mandatory")
_MscExampleHexProvFreeHexVector1Entry_Object = MibTableRow
mscExampleHexProvFreeHexVector1Entry = _MscExampleHexProvFreeHexVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1049, 1)
)
mscExampleHexProvFreeHexVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector1Entry.setStatus("mandatory")


class _MscExampleHexProvFreeHexVector1Index_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexProvFreeHexVector1Index_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexVector1Index_Object = MibTableColumn
mscExampleHexProvFreeHexVector1Index = _MscExampleHexProvFreeHexVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1049, 1, 1),
    _MscExampleHexProvFreeHexVector1Index_Type()
)
mscExampleHexProvFreeHexVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector1Index.setStatus("mandatory")


class _MscExampleHexProvFreeHexVector1Value_Type(Hex):
    """Custom type mscExampleHexProvFreeHexVector1Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(256, 4096),
    )


_MscExampleHexProvFreeHexVector1Value_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexVector1Value_Object = MibTableColumn
mscExampleHexProvFreeHexVector1Value = _MscExampleHexProvFreeHexVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1049, 1, 2),
    _MscExampleHexProvFreeHexVector1Value_Type()
)
mscExampleHexProvFreeHexVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector1Value.setStatus("mandatory")
_MscExampleHexProvFreeHexVector2Table_Object = MibTable
mscExampleHexProvFreeHexVector2Table = _MscExampleHexProvFreeHexVector2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1050)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector2Table.setStatus("mandatory")
_MscExampleHexProvFreeHexVector2Entry_Object = MibTableRow
mscExampleHexProvFreeHexVector2Entry = _MscExampleHexProvFreeHexVector2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1050, 1)
)
mscExampleHexProvFreeHexVector2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexVector2Index"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector2Entry.setStatus("mandatory")


class _MscExampleHexProvFreeHexVector2Index_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexVector2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MscExampleHexProvFreeHexVector2Index_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexVector2Index_Object = MibTableColumn
mscExampleHexProvFreeHexVector2Index = _MscExampleHexProvFreeHexVector2Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1050, 1, 1),
    _MscExampleHexProvFreeHexVector2Index_Type()
)
mscExampleHexProvFreeHexVector2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector2Index.setStatus("mandatory")


class _MscExampleHexProvFreeHexVector2Value_Type(Hex):
    """Custom type mscExampleHexProvFreeHexVector2Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(256, 4096),
    )


_MscExampleHexProvFreeHexVector2Value_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexVector2Value_Object = MibTableColumn
mscExampleHexProvFreeHexVector2Value = _MscExampleHexProvFreeHexVector2Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1050, 1, 2),
    _MscExampleHexProvFreeHexVector2Value_Type()
)
mscExampleHexProvFreeHexVector2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexVector2Value.setStatus("mandatory")
_MscExampleHexProvFreeHexArrayTable_Object = MibTable
mscExampleHexProvFreeHexArrayTable = _MscExampleHexProvFreeHexArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1051)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArrayTable.setStatus("mandatory")
_MscExampleHexProvFreeHexArrayEntry_Object = MibTableRow
mscExampleHexProvFreeHexArrayEntry = _MscExampleHexProvFreeHexArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1051, 1)
)
mscExampleHexProvFreeHexArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArrayEntry.setStatus("mandatory")


class _MscExampleHexProvFreeHexArrayRowIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleHexProvFreeHexArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexArrayRowIndex_Object = MibTableColumn
mscExampleHexProvFreeHexArrayRowIndex = _MscExampleHexProvFreeHexArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1051, 1, 1),
    _MscExampleHexProvFreeHexArrayRowIndex_Type()
)
mscExampleHexProvFreeHexArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArrayRowIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexProvFreeHexArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexArrayColumnIndex_Object = MibTableColumn
mscExampleHexProvFreeHexArrayColumnIndex = _MscExampleHexProvFreeHexArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1051, 1, 2),
    _MscExampleHexProvFreeHexArrayColumnIndex_Type()
)
mscExampleHexProvFreeHexArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArrayColumnIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexArrayValue_Type(Hex):
    """Custom type mscExampleHexProvFreeHexArrayValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexProvFreeHexArrayValue_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexArrayValue_Object = MibTableColumn
mscExampleHexProvFreeHexArrayValue = _MscExampleHexProvFreeHexArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1051, 1, 3),
    _MscExampleHexProvFreeHexArrayValue_Type()
)
mscExampleHexProvFreeHexArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArrayValue.setStatus("mandatory")
_MscExampleHexProvFreeHexArray1Table_Object = MibTable
mscExampleHexProvFreeHexArray1Table = _MscExampleHexProvFreeHexArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1052)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray1Table.setStatus("mandatory")
_MscExampleHexProvFreeHexArray1Entry_Object = MibTableRow
mscExampleHexProvFreeHexArray1Entry = _MscExampleHexProvFreeHexArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1052, 1)
)
mscExampleHexProvFreeHexArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexArray1RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray1Entry.setStatus("mandatory")


class _MscExampleHexProvFreeHexArray1RowIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(3, 4),
    )


_MscExampleHexProvFreeHexArray1RowIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexArray1RowIndex_Object = MibTableColumn
mscExampleHexProvFreeHexArray1RowIndex = _MscExampleHexProvFreeHexArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1052, 1, 1),
    _MscExampleHexProvFreeHexArray1RowIndex_Type()
)
mscExampleHexProvFreeHexArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray1RowIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexArray1ColumnIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexProvFreeHexArray1ColumnIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexArray1ColumnIndex_Object = MibTableColumn
mscExampleHexProvFreeHexArray1ColumnIndex = _MscExampleHexProvFreeHexArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1052, 1, 2),
    _MscExampleHexProvFreeHexArray1ColumnIndex_Type()
)
mscExampleHexProvFreeHexArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray1ColumnIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexArray1Value_Type(Hex):
    """Custom type mscExampleHexProvFreeHexArray1Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(80, 256),
    )


_MscExampleHexProvFreeHexArray1Value_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexArray1Value_Object = MibTableColumn
mscExampleHexProvFreeHexArray1Value = _MscExampleHexProvFreeHexArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1052, 1, 3),
    _MscExampleHexProvFreeHexArray1Value_Type()
)
mscExampleHexProvFreeHexArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray1Value.setStatus("mandatory")
_MscExampleHexProvFreeHexArray2Table_Object = MibTable
mscExampleHexProvFreeHexArray2Table = _MscExampleHexProvFreeHexArray2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1053)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray2Table.setStatus("mandatory")
_MscExampleHexProvFreeHexArray2Entry_Object = MibTableRow
mscExampleHexProvFreeHexArray2Entry = _MscExampleHexProvFreeHexArray2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1053, 1)
)
mscExampleHexProvFreeHexArray2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexArray2RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexArray2ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray2Entry.setStatus("mandatory")


class _MscExampleHexProvFreeHexArray2RowIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexArray2RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexProvFreeHexArray2RowIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexArray2RowIndex_Object = MibTableColumn
mscExampleHexProvFreeHexArray2RowIndex = _MscExampleHexProvFreeHexArray2RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1053, 1, 1),
    _MscExampleHexProvFreeHexArray2RowIndex_Type()
)
mscExampleHexProvFreeHexArray2RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray2RowIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexArray2ColumnIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexArray2ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleHexProvFreeHexArray2ColumnIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexArray2ColumnIndex_Object = MibTableColumn
mscExampleHexProvFreeHexArray2ColumnIndex = _MscExampleHexProvFreeHexArray2ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1053, 1, 2),
    _MscExampleHexProvFreeHexArray2ColumnIndex_Type()
)
mscExampleHexProvFreeHexArray2ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray2ColumnIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexArray2Value_Type(Hex):
    """Custom type mscExampleHexProvFreeHexArray2Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
        ValueRangeConstraint(80, 256),
    )


_MscExampleHexProvFreeHexArray2Value_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexArray2Value_Object = MibTableColumn
mscExampleHexProvFreeHexArray2Value = _MscExampleHexProvFreeHexArray2Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1053, 1, 3),
    _MscExampleHexProvFreeHexArray2Value_Type()
)
mscExampleHexProvFreeHexArray2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexArray2Value.setStatus("mandatory")
_MscExampleHexProvFreeHexReplicatedTable_Object = MibTable
mscExampleHexProvFreeHexReplicatedTable = _MscExampleHexProvFreeHexReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1054)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicatedTable.setStatus("mandatory")
_MscExampleHexProvFreeHexReplicatedEntry_Object = MibTableRow
mscExampleHexProvFreeHexReplicatedEntry = _MscExampleHexProvFreeHexReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1054, 1)
)
mscExampleHexProvFreeHexReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicatedEntry.setStatus("mandatory")


class _MscExampleHexProvFreeHexReplicatedIndex_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleHexProvFreeHexReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexReplicatedIndex_Object = MibTableColumn
mscExampleHexProvFreeHexReplicatedIndex = _MscExampleHexProvFreeHexReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1054, 1, 1),
    _MscExampleHexProvFreeHexReplicatedIndex_Type()
)
mscExampleHexProvFreeHexReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicatedIndex.setStatus("mandatory")


class _MscExampleHexProvFreeHexReplicatedValue_Type(Hex):
    """Custom type mscExampleHexProvFreeHexReplicatedValue based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MscExampleHexProvFreeHexReplicatedValue_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexReplicatedValue_Object = MibTableColumn
mscExampleHexProvFreeHexReplicatedValue = _MscExampleHexProvFreeHexReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1054, 1, 2),
    _MscExampleHexProvFreeHexReplicatedValue_Type()
)
mscExampleHexProvFreeHexReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicatedValue.setStatus("mandatory")
_MscExampleHexProvFreeHexReplicatedRowStatus_Type = RowStatus
_MscExampleHexProvFreeHexReplicatedRowStatus_Object = MibTableColumn
mscExampleHexProvFreeHexReplicatedRowStatus = _MscExampleHexProvFreeHexReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1054, 1, 3),
    _MscExampleHexProvFreeHexReplicatedRowStatus_Type()
)
mscExampleHexProvFreeHexReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicatedRowStatus.setStatus("mandatory")
_MscExampleHexProvFreeHexReplicated1Table_Object = MibTable
mscExampleHexProvFreeHexReplicated1Table = _MscExampleHexProvFreeHexReplicated1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1055)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicated1Table.setStatus("mandatory")
_MscExampleHexProvFreeHexReplicated1Entry_Object = MibTableRow
mscExampleHexProvFreeHexReplicated1Entry = _MscExampleHexProvFreeHexReplicated1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1055, 1)
)
mscExampleHexProvFreeHexReplicated1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexReplicated1Index"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicated1Entry.setStatus("mandatory")


class _MscExampleHexProvFreeHexReplicated1Index_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexReplicated1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
        ValueRangeConstraint(5, 9),
    )


_MscExampleHexProvFreeHexReplicated1Index_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexReplicated1Index_Object = MibTableColumn
mscExampleHexProvFreeHexReplicated1Index = _MscExampleHexProvFreeHexReplicated1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1055, 1, 1),
    _MscExampleHexProvFreeHexReplicated1Index_Type()
)
mscExampleHexProvFreeHexReplicated1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicated1Index.setStatus("mandatory")


class _MscExampleHexProvFreeHexReplicated1Value_Type(Hex):
    """Custom type mscExampleHexProvFreeHexReplicated1Value based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
        ValueRangeConstraint(80, 256),
    )


_MscExampleHexProvFreeHexReplicated1Value_Type.__name__ = "Hex"
_MscExampleHexProvFreeHexReplicated1Value_Object = MibTableColumn
mscExampleHexProvFreeHexReplicated1Value = _MscExampleHexProvFreeHexReplicated1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1055, 1, 2),
    _MscExampleHexProvFreeHexReplicated1Value_Type()
)
mscExampleHexProvFreeHexReplicated1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicated1Value.setStatus("mandatory")
_MscExampleHexProvFreeHexReplicated1RowStatus_Type = RowStatus
_MscExampleHexProvFreeHexReplicated1RowStatus_Object = MibTableColumn
mscExampleHexProvFreeHexReplicated1RowStatus = _MscExampleHexProvFreeHexReplicated1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1055, 1, 3),
    _MscExampleHexProvFreeHexReplicated1RowStatus_Type()
)
mscExampleHexProvFreeHexReplicated1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexReplicated1RowStatus.setStatus("mandatory")
_MscExampleHexProvFreeHexListTable_Object = MibTable
mscExampleHexProvFreeHexListTable = _MscExampleHexProvFreeHexListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1056)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexListTable.setStatus("mandatory")
_MscExampleHexProvFreeHexListEntry_Object = MibTableRow
mscExampleHexProvFreeHexListEntry = _MscExampleHexProvFreeHexListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1056, 1)
)
mscExampleHexProvFreeHexListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexListValue"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexListEntry.setStatus("mandatory")


class _MscExampleHexProvFreeHexListValue_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscExampleHexProvFreeHexListValue_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexListValue_Object = MibTableColumn
mscExampleHexProvFreeHexListValue = _MscExampleHexProvFreeHexListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1056, 1, 1),
    _MscExampleHexProvFreeHexListValue_Type()
)
mscExampleHexProvFreeHexListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexListValue.setStatus("mandatory")
_MscExampleHexProvFreeHexListRowStatus_Type = RowStatus
_MscExampleHexProvFreeHexListRowStatus_Object = MibTableColumn
mscExampleHexProvFreeHexListRowStatus = _MscExampleHexProvFreeHexListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1056, 1, 2),
    _MscExampleHexProvFreeHexListRowStatus_Type()
)
mscExampleHexProvFreeHexListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexListRowStatus.setStatus("mandatory")
_MscExampleHexProvFreeHexList1Table_Object = MibTable
mscExampleHexProvFreeHexList1Table = _MscExampleHexProvFreeHexList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1057)
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexList1Table.setStatus("mandatory")
_MscExampleHexProvFreeHexList1Entry_Object = MibTableRow
mscExampleHexProvFreeHexList1Entry = _MscExampleHexProvFreeHexList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1057, 1)
)
mscExampleHexProvFreeHexList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexProvFreeHexList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexList1Entry.setStatus("mandatory")


class _MscExampleHexProvFreeHexList1Value_Type(Integer32):
    """Custom type mscExampleHexProvFreeHexList1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscExampleHexProvFreeHexList1Value_Type.__name__ = "Integer32"
_MscExampleHexProvFreeHexList1Value_Object = MibTableColumn
mscExampleHexProvFreeHexList1Value = _MscExampleHexProvFreeHexList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1057, 1, 1),
    _MscExampleHexProvFreeHexList1Value_Type()
)
mscExampleHexProvFreeHexList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexList1Value.setStatus("mandatory")
_MscExampleHexProvFreeHexList1RowStatus_Type = RowStatus
_MscExampleHexProvFreeHexList1RowStatus_Object = MibTableColumn
mscExampleHexProvFreeHexList1RowStatus = _MscExampleHexProvFreeHexList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 3, 1057, 1, 2),
    _MscExampleHexProvFreeHexList1RowStatus_Type()
)
mscExampleHexProvFreeHexList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleHexProvFreeHexList1RowStatus.setStatus("mandatory")
_MscExampleIpAddress_ObjectIdentity = ObjectIdentity
mscExampleIpAddress = _MscExampleIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4)
)
_MscExampleIpAddressRowStatusTable_Object = MibTable
mscExampleIpAddressRowStatusTable = _MscExampleIpAddressRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressRowStatusTable.setStatus("mandatory")
_MscExampleIpAddressRowStatusEntry_Object = MibTableRow
mscExampleIpAddressRowStatusEntry = _MscExampleIpAddressRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1, 1)
)
mscExampleIpAddressRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressRowStatusEntry.setStatus("mandatory")
_MscExampleIpAddressRowStatus_Type = RowStatus
_MscExampleIpAddressRowStatus_Object = MibTableColumn
mscExampleIpAddressRowStatus = _MscExampleIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1, 1, 1),
    _MscExampleIpAddressRowStatus_Type()
)
mscExampleIpAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressRowStatus.setStatus("mandatory")
_MscExampleIpAddressComponentName_Type = DisplayString
_MscExampleIpAddressComponentName_Object = MibTableColumn
mscExampleIpAddressComponentName = _MscExampleIpAddressComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1, 1, 2),
    _MscExampleIpAddressComponentName_Type()
)
mscExampleIpAddressComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressComponentName.setStatus("mandatory")
_MscExampleIpAddressStorageType_Type = StorageType
_MscExampleIpAddressStorageType_Object = MibTableColumn
mscExampleIpAddressStorageType = _MscExampleIpAddressStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1, 1, 4),
    _MscExampleIpAddressStorageType_Type()
)
mscExampleIpAddressStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressStorageType.setStatus("mandatory")
_MscExampleIpAddressIndex_Type = IpAddress
_MscExampleIpAddressIndex_Object = MibTableColumn
mscExampleIpAddressIndex = _MscExampleIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1, 1, 10),
    _MscExampleIpAddressIndex_Type()
)
mscExampleIpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressIndex.setStatus("mandatory")
_MscExampleIpAddressOperationalTable_Object = MibTable
mscExampleIpAddressOperationalTable = _MscExampleIpAddressOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 10)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperationalTable.setStatus("mandatory")
_MscExampleIpAddressOperationalEntry_Object = MibTableRow
mscExampleIpAddressOperationalEntry = _MscExampleIpAddressOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 10, 1)
)
mscExampleIpAddressOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperationalEntry.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddress_Type = IpAddress
_MscExampleIpAddressOperStructIpAddress_Object = MibTableColumn
mscExampleIpAddressOperStructIpAddress = _MscExampleIpAddressOperStructIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 10, 1, 1),
    _MscExampleIpAddressOperStructIpAddress_Type()
)
mscExampleIpAddressOperStructIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddress.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddress_Type = IpAddress
_MscExampleIpAddressOperFreeIpAddress_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddress = _MscExampleIpAddressOperFreeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 10, 1, 2),
    _MscExampleIpAddressOperFreeIpAddress_Type()
)
mscExampleIpAddressOperFreeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddress.setStatus("mandatory")
_MscExampleIpAddressProvisionalTable_Object = MibTable
mscExampleIpAddressProvisionalTable = _MscExampleIpAddressProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 11)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvisionalTable.setStatus("mandatory")
_MscExampleIpAddressProvisionalEntry_Object = MibTableRow
mscExampleIpAddressProvisionalEntry = _MscExampleIpAddressProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 11, 1)
)
mscExampleIpAddressProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvisionalEntry.setStatus("mandatory")
_MscExampleIpAddressProvEnumSub_Type = Link
_MscExampleIpAddressProvEnumSub_Object = MibTableColumn
mscExampleIpAddressProvEnumSub = _MscExampleIpAddressProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 11, 1, 1),
    _MscExampleIpAddressProvEnumSub_Type()
)
mscExampleIpAddressProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvEnumSub.setStatus("mandatory")


class _MscExampleIpAddressProvStructIpAddress_Type(IpAddress):
    """Custom type mscExampleIpAddressProvStructIpAddress based on IpAddress"""
    defaultHexValue = "7f000100"


_MscExampleIpAddressProvStructIpAddress_Object = MibTableColumn
mscExampleIpAddressProvStructIpAddress = _MscExampleIpAddressProvStructIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 11, 1, 2),
    _MscExampleIpAddressProvStructIpAddress_Type()
)
mscExampleIpAddressProvStructIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddress.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddress_Type(IpAddress):
    """Custom type mscExampleIpAddressProvFreeIpAddress based on IpAddress"""
    defaultHexValue = "7f7f7f7f"


_MscExampleIpAddressProvFreeIpAddress_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddress = _MscExampleIpAddressProvFreeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 11, 1, 3),
    _MscExampleIpAddressProvFreeIpAddress_Type()
)
mscExampleIpAddressProvFreeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddress.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddress1_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddress1_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddress1 = _MscExampleIpAddressProvFreeIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 11, 1, 4),
    _MscExampleIpAddressProvFreeIpAddress1_Type()
)
mscExampleIpAddressProvFreeIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddress1.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddressVectorTable_Object = MibTable
mscExampleIpAddressOperStructIpAddressVectorTable = _MscExampleIpAddressOperStructIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1058)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressVectorTable.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddressVectorEntry_Object = MibTableRow
mscExampleIpAddressOperStructIpAddressVectorEntry = _MscExampleIpAddressOperStructIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1058, 1)
)
mscExampleIpAddressOperStructIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperStructIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressVectorEntry.setStatus("mandatory")


class _MscExampleIpAddressOperStructIpAddressVectorIndex_Type(Integer32):
    """Custom type mscExampleIpAddressOperStructIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleIpAddressOperStructIpAddressVectorIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressOperStructIpAddressVectorIndex_Object = MibTableColumn
mscExampleIpAddressOperStructIpAddressVectorIndex = _MscExampleIpAddressOperStructIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1058, 1, 1),
    _MscExampleIpAddressOperStructIpAddressVectorIndex_Type()
)
mscExampleIpAddressOperStructIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressVectorIndex.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddressVectorValue_Type = IpAddress
_MscExampleIpAddressOperStructIpAddressVectorValue_Object = MibTableColumn
mscExampleIpAddressOperStructIpAddressVectorValue = _MscExampleIpAddressOperStructIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1058, 1, 2),
    _MscExampleIpAddressOperStructIpAddressVectorValue_Type()
)
mscExampleIpAddressOperStructIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressVectorValue.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddressArrayTable_Object = MibTable
mscExampleIpAddressOperStructIpAddressArrayTable = _MscExampleIpAddressOperStructIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1059)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressArrayTable.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddressArrayEntry_Object = MibTableRow
mscExampleIpAddressOperStructIpAddressArrayEntry = _MscExampleIpAddressOperStructIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1059, 1)
)
mscExampleIpAddressOperStructIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperStructIpAddressArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperStructIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressArrayEntry.setStatus("mandatory")


class _MscExampleIpAddressOperStructIpAddressArrayRowIndex_Type(Integer32):
    """Custom type mscExampleIpAddressOperStructIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleIpAddressOperStructIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressOperStructIpAddressArrayRowIndex_Object = MibTableColumn
mscExampleIpAddressOperStructIpAddressArrayRowIndex = _MscExampleIpAddressOperStructIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1059, 1, 1),
    _MscExampleIpAddressOperStructIpAddressArrayRowIndex_Type()
)
mscExampleIpAddressOperStructIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressArrayRowIndex.setStatus("mandatory")


class _MscExampleIpAddressOperStructIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleIpAddressOperStructIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressOperStructIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressOperStructIpAddressArrayColumnIndex_Object = MibTableColumn
mscExampleIpAddressOperStructIpAddressArrayColumnIndex = _MscExampleIpAddressOperStructIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1059, 1, 2),
    _MscExampleIpAddressOperStructIpAddressArrayColumnIndex_Type()
)
mscExampleIpAddressOperStructIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressArrayColumnIndex.setStatus("mandatory")
_MscExampleIpAddressOperStructIpAddressArrayValue_Type = IpAddress
_MscExampleIpAddressOperStructIpAddressArrayValue_Object = MibTableColumn
mscExampleIpAddressOperStructIpAddressArrayValue = _MscExampleIpAddressOperStructIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1059, 1, 3),
    _MscExampleIpAddressOperStructIpAddressArrayValue_Type()
)
mscExampleIpAddressOperStructIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperStructIpAddressArrayValue.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressVectorTable_Object = MibTable
mscExampleIpAddressOperFreeIpAddressVectorTable = _MscExampleIpAddressOperFreeIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1060)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressVectorTable.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressVectorEntry_Object = MibTableRow
mscExampleIpAddressOperFreeIpAddressVectorEntry = _MscExampleIpAddressOperFreeIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1060, 1)
)
mscExampleIpAddressOperFreeIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperFreeIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressVectorEntry.setStatus("mandatory")


class _MscExampleIpAddressOperFreeIpAddressVectorIndex_Type(Integer32):
    """Custom type mscExampleIpAddressOperFreeIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleIpAddressOperFreeIpAddressVectorIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressOperFreeIpAddressVectorIndex_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressVectorIndex = _MscExampleIpAddressOperFreeIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1060, 1, 1),
    _MscExampleIpAddressOperFreeIpAddressVectorIndex_Type()
)
mscExampleIpAddressOperFreeIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressVectorIndex.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressVectorValue_Type = IpAddress
_MscExampleIpAddressOperFreeIpAddressVectorValue_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressVectorValue = _MscExampleIpAddressOperFreeIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1060, 1, 2),
    _MscExampleIpAddressOperFreeIpAddressVectorValue_Type()
)
mscExampleIpAddressOperFreeIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressVectorValue.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressArrayTable_Object = MibTable
mscExampleIpAddressOperFreeIpAddressArrayTable = _MscExampleIpAddressOperFreeIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1061)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressArrayTable.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressArrayEntry_Object = MibTableRow
mscExampleIpAddressOperFreeIpAddressArrayEntry = _MscExampleIpAddressOperFreeIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1061, 1)
)
mscExampleIpAddressOperFreeIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperFreeIpAddressArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperFreeIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressArrayEntry.setStatus("mandatory")


class _MscExampleIpAddressOperFreeIpAddressArrayRowIndex_Type(Integer32):
    """Custom type mscExampleIpAddressOperFreeIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleIpAddressOperFreeIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressOperFreeIpAddressArrayRowIndex_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressArrayRowIndex = _MscExampleIpAddressOperFreeIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1061, 1, 1),
    _MscExampleIpAddressOperFreeIpAddressArrayRowIndex_Type()
)
mscExampleIpAddressOperFreeIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressArrayRowIndex.setStatus("mandatory")


class _MscExampleIpAddressOperFreeIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleIpAddressOperFreeIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressOperFreeIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressOperFreeIpAddressArrayColumnIndex_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressArrayColumnIndex = _MscExampleIpAddressOperFreeIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1061, 1, 2),
    _MscExampleIpAddressOperFreeIpAddressArrayColumnIndex_Type()
)
mscExampleIpAddressOperFreeIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressArrayColumnIndex.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressArrayValue_Type = IpAddress
_MscExampleIpAddressOperFreeIpAddressArrayValue_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressArrayValue = _MscExampleIpAddressOperFreeIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1061, 1, 3),
    _MscExampleIpAddressOperFreeIpAddressArrayValue_Type()
)
mscExampleIpAddressOperFreeIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressArrayValue.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressReplicatedTable_Object = MibTable
mscExampleIpAddressOperFreeIpAddressReplicatedTable = _MscExampleIpAddressOperFreeIpAddressReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1062)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressReplicatedTable.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressReplicatedEntry_Object = MibTableRow
mscExampleIpAddressOperFreeIpAddressReplicatedEntry = _MscExampleIpAddressOperFreeIpAddressReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1062, 1)
)
mscExampleIpAddressOperFreeIpAddressReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperFreeIpAddressReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressReplicatedEntry.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressReplicatedIndex_Type = IpAddress
_MscExampleIpAddressOperFreeIpAddressReplicatedIndex_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressReplicatedIndex = _MscExampleIpAddressOperFreeIpAddressReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1062, 1, 1),
    _MscExampleIpAddressOperFreeIpAddressReplicatedIndex_Type()
)
mscExampleIpAddressOperFreeIpAddressReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressReplicatedIndex.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressReplicatedValue_Type = IpAddress
_MscExampleIpAddressOperFreeIpAddressReplicatedValue_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressReplicatedValue = _MscExampleIpAddressOperFreeIpAddressReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1062, 1, 2),
    _MscExampleIpAddressOperFreeIpAddressReplicatedValue_Type()
)
mscExampleIpAddressOperFreeIpAddressReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressReplicatedValue.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Type = RowStatus
_MscExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressReplicatedRowStatus = _MscExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1062, 1, 3),
    _MscExampleIpAddressOperFreeIpAddressReplicatedRowStatus_Type()
)
mscExampleIpAddressOperFreeIpAddressReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressReplicatedRowStatus.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressListTable_Object = MibTable
mscExampleIpAddressOperFreeIpAddressListTable = _MscExampleIpAddressOperFreeIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1063)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressListTable.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressListEntry_Object = MibTableRow
mscExampleIpAddressOperFreeIpAddressListEntry = _MscExampleIpAddressOperFreeIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1063, 1)
)
mscExampleIpAddressOperFreeIpAddressListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressOperFreeIpAddressListValue"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressListEntry.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressListValue_Type = IpAddress
_MscExampleIpAddressOperFreeIpAddressListValue_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressListValue = _MscExampleIpAddressOperFreeIpAddressListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1063, 1, 1),
    _MscExampleIpAddressOperFreeIpAddressListValue_Type()
)
mscExampleIpAddressOperFreeIpAddressListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressListValue.setStatus("mandatory")
_MscExampleIpAddressOperFreeIpAddressListRowStatus_Type = RowStatus
_MscExampleIpAddressOperFreeIpAddressListRowStatus_Object = MibTableColumn
mscExampleIpAddressOperFreeIpAddressListRowStatus = _MscExampleIpAddressOperFreeIpAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1063, 1, 2),
    _MscExampleIpAddressOperFreeIpAddressListRowStatus_Type()
)
mscExampleIpAddressOperFreeIpAddressListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressOperFreeIpAddressListRowStatus.setStatus("mandatory")
_MscExampleIpAddressProvStructIpAddressVectorTable_Object = MibTable
mscExampleIpAddressProvStructIpAddressVectorTable = _MscExampleIpAddressProvStructIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1064)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressVectorTable.setStatus("mandatory")
_MscExampleIpAddressProvStructIpAddressVectorEntry_Object = MibTableRow
mscExampleIpAddressProvStructIpAddressVectorEntry = _MscExampleIpAddressProvStructIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1064, 1)
)
mscExampleIpAddressProvStructIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvStructIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressVectorEntry.setStatus("mandatory")


class _MscExampleIpAddressProvStructIpAddressVectorIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvStructIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleIpAddressProvStructIpAddressVectorIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvStructIpAddressVectorIndex_Object = MibTableColumn
mscExampleIpAddressProvStructIpAddressVectorIndex = _MscExampleIpAddressProvStructIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1064, 1, 1),
    _MscExampleIpAddressProvStructIpAddressVectorIndex_Type()
)
mscExampleIpAddressProvStructIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressVectorIndex.setStatus("mandatory")
_MscExampleIpAddressProvStructIpAddressVectorValue_Type = IpAddress
_MscExampleIpAddressProvStructIpAddressVectorValue_Object = MibTableColumn
mscExampleIpAddressProvStructIpAddressVectorValue = _MscExampleIpAddressProvStructIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1064, 1, 2),
    _MscExampleIpAddressProvStructIpAddressVectorValue_Type()
)
mscExampleIpAddressProvStructIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressVectorValue.setStatus("mandatory")
_MscExampleIpAddressProvStructIpAddressArrayTable_Object = MibTable
mscExampleIpAddressProvStructIpAddressArrayTable = _MscExampleIpAddressProvStructIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1065)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressArrayTable.setStatus("mandatory")
_MscExampleIpAddressProvStructIpAddressArrayEntry_Object = MibTableRow
mscExampleIpAddressProvStructIpAddressArrayEntry = _MscExampleIpAddressProvStructIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1065, 1)
)
mscExampleIpAddressProvStructIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvStructIpAddressArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvStructIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressArrayEntry.setStatus("mandatory")


class _MscExampleIpAddressProvStructIpAddressArrayRowIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvStructIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleIpAddressProvStructIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvStructIpAddressArrayRowIndex_Object = MibTableColumn
mscExampleIpAddressProvStructIpAddressArrayRowIndex = _MscExampleIpAddressProvStructIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1065, 1, 1),
    _MscExampleIpAddressProvStructIpAddressArrayRowIndex_Type()
)
mscExampleIpAddressProvStructIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressArrayRowIndex.setStatus("mandatory")


class _MscExampleIpAddressProvStructIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvStructIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressProvStructIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvStructIpAddressArrayColumnIndex_Object = MibTableColumn
mscExampleIpAddressProvStructIpAddressArrayColumnIndex = _MscExampleIpAddressProvStructIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1065, 1, 2),
    _MscExampleIpAddressProvStructIpAddressArrayColumnIndex_Type()
)
mscExampleIpAddressProvStructIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressArrayColumnIndex.setStatus("mandatory")
_MscExampleIpAddressProvStructIpAddressArrayValue_Type = IpAddress
_MscExampleIpAddressProvStructIpAddressArrayValue_Object = MibTableColumn
mscExampleIpAddressProvStructIpAddressArrayValue = _MscExampleIpAddressProvStructIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1065, 1, 3),
    _MscExampleIpAddressProvStructIpAddressArrayValue_Type()
)
mscExampleIpAddressProvStructIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvStructIpAddressArrayValue.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressVectorTable_Object = MibTable
mscExampleIpAddressProvFreeIpAddressVectorTable = _MscExampleIpAddressProvFreeIpAddressVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1066)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVectorTable.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressVectorEntry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressVectorEntry = _MscExampleIpAddressProvFreeIpAddressVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1066, 1)
)
mscExampleIpAddressProvFreeIpAddressVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVectorEntry.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddressVectorIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvFreeIpAddressVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleIpAddressProvFreeIpAddressVectorIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvFreeIpAddressVectorIndex_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressVectorIndex = _MscExampleIpAddressProvFreeIpAddressVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1066, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressVectorIndex_Type()
)
mscExampleIpAddressProvFreeIpAddressVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVectorIndex.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressVectorValue_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressVectorValue_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressVectorValue = _MscExampleIpAddressProvFreeIpAddressVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1066, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressVectorValue_Type()
)
mscExampleIpAddressProvFreeIpAddressVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVectorValue.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressVector1Table_Object = MibTable
mscExampleIpAddressProvFreeIpAddressVector1Table = _MscExampleIpAddressProvFreeIpAddressVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1067)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVector1Table.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressVector1Entry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressVector1Entry = _MscExampleIpAddressProvFreeIpAddressVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1067, 1)
)
mscExampleIpAddressProvFreeIpAddressVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVector1Entry.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddressVector1Index_Type(Integer32):
    """Custom type mscExampleIpAddressProvFreeIpAddressVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressProvFreeIpAddressVector1Index_Type.__name__ = "Integer32"
_MscExampleIpAddressProvFreeIpAddressVector1Index_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressVector1Index = _MscExampleIpAddressProvFreeIpAddressVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1067, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressVector1Index_Type()
)
mscExampleIpAddressProvFreeIpAddressVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVector1Index.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressVector1Value_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressVector1Value_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressVector1Value = _MscExampleIpAddressProvFreeIpAddressVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1067, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressVector1Value_Type()
)
mscExampleIpAddressProvFreeIpAddressVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressVector1Value.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressArrayTable_Object = MibTable
mscExampleIpAddressProvFreeIpAddressArrayTable = _MscExampleIpAddressProvFreeIpAddressArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1068)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArrayTable.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressArrayEntry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressArrayEntry = _MscExampleIpAddressProvFreeIpAddressArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1068, 1)
)
mscExampleIpAddressProvFreeIpAddressArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArrayEntry.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddressArrayRowIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvFreeIpAddressArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleIpAddressProvFreeIpAddressArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvFreeIpAddressArrayRowIndex_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressArrayRowIndex = _MscExampleIpAddressProvFreeIpAddressArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1068, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressArrayRowIndex_Type()
)
mscExampleIpAddressProvFreeIpAddressArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArrayRowIndex.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddressArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvFreeIpAddressArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressProvFreeIpAddressArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvFreeIpAddressArrayColumnIndex_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressArrayColumnIndex = _MscExampleIpAddressProvFreeIpAddressArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1068, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressArrayColumnIndex_Type()
)
mscExampleIpAddressProvFreeIpAddressArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArrayColumnIndex.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressArrayValue_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressArrayValue_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressArrayValue = _MscExampleIpAddressProvFreeIpAddressArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1068, 1, 3),
    _MscExampleIpAddressProvFreeIpAddressArrayValue_Type()
)
mscExampleIpAddressProvFreeIpAddressArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArrayValue.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressArray1Table_Object = MibTable
mscExampleIpAddressProvFreeIpAddressArray1Table = _MscExampleIpAddressProvFreeIpAddressArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1069)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArray1Table.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressArray1Entry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressArray1Entry = _MscExampleIpAddressProvFreeIpAddressArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1069, 1)
)
mscExampleIpAddressProvFreeIpAddressArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressArray1RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArray1Entry.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddressArray1RowIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvFreeIpAddressArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressProvFreeIpAddressArray1RowIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvFreeIpAddressArray1RowIndex_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressArray1RowIndex = _MscExampleIpAddressProvFreeIpAddressArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1069, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressArray1RowIndex_Type()
)
mscExampleIpAddressProvFreeIpAddressArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArray1RowIndex.setStatus("mandatory")


class _MscExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Type(Integer32):
    """Custom type mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Type.__name__ = "Integer32"
_MscExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex = _MscExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1069, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressArray1ColumnIndex_Type()
)
mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressArray1Value_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressArray1Value_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressArray1Value = _MscExampleIpAddressProvFreeIpAddressArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1069, 1, 3),
    _MscExampleIpAddressProvFreeIpAddressArray1Value_Type()
)
mscExampleIpAddressProvFreeIpAddressArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressArray1Value.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressReplicatedTable_Object = MibTable
mscExampleIpAddressProvFreeIpAddressReplicatedTable = _MscExampleIpAddressProvFreeIpAddressReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1070)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressReplicatedTable.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressReplicatedEntry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressReplicatedEntry = _MscExampleIpAddressProvFreeIpAddressReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1070, 1)
)
mscExampleIpAddressProvFreeIpAddressReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressReplicatedEntry.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressReplicatedIndex_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressReplicatedIndex_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressReplicatedIndex = _MscExampleIpAddressProvFreeIpAddressReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1070, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressReplicatedIndex_Type()
)
mscExampleIpAddressProvFreeIpAddressReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressReplicatedIndex.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressReplicatedValue_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressReplicatedValue_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressReplicatedValue = _MscExampleIpAddressProvFreeIpAddressReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1070, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressReplicatedValue_Type()
)
mscExampleIpAddressProvFreeIpAddressReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressReplicatedValue.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Type = RowStatus
_MscExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressReplicatedRowStatus = _MscExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1070, 1, 3),
    _MscExampleIpAddressProvFreeIpAddressReplicatedRowStatus_Type()
)
mscExampleIpAddressProvFreeIpAddressReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressReplicatedRowStatus.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressListTable_Object = MibTable
mscExampleIpAddressProvFreeIpAddressListTable = _MscExampleIpAddressProvFreeIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1071)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressListTable.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressListEntry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressListEntry = _MscExampleIpAddressProvFreeIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1071, 1)
)
mscExampleIpAddressProvFreeIpAddressListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressListValue"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressListEntry.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressListValue_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressListValue_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressListValue = _MscExampleIpAddressProvFreeIpAddressListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1071, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressListValue_Type()
)
mscExampleIpAddressProvFreeIpAddressListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressListValue.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressListRowStatus_Type = RowStatus
_MscExampleIpAddressProvFreeIpAddressListRowStatus_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressListRowStatus = _MscExampleIpAddressProvFreeIpAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1071, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressListRowStatus_Type()
)
mscExampleIpAddressProvFreeIpAddressListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressListRowStatus.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressList1Table_Object = MibTable
mscExampleIpAddressProvFreeIpAddressList1Table = _MscExampleIpAddressProvFreeIpAddressList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1072)
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressList1Table.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressList1Entry_Object = MibTableRow
mscExampleIpAddressProvFreeIpAddressList1Entry = _MscExampleIpAddressProvFreeIpAddressList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1072, 1)
)
mscExampleIpAddressProvFreeIpAddressList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddressProvFreeIpAddressList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressList1Entry.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressList1Value_Type = IpAddress
_MscExampleIpAddressProvFreeIpAddressList1Value_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressList1Value = _MscExampleIpAddressProvFreeIpAddressList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1072, 1, 1),
    _MscExampleIpAddressProvFreeIpAddressList1Value_Type()
)
mscExampleIpAddressProvFreeIpAddressList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressList1Value.setStatus("mandatory")
_MscExampleIpAddressProvFreeIpAddressList1RowStatus_Type = RowStatus
_MscExampleIpAddressProvFreeIpAddressList1RowStatus_Object = MibTableColumn
mscExampleIpAddressProvFreeIpAddressList1RowStatus = _MscExampleIpAddressProvFreeIpAddressList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 4, 1072, 1, 2),
    _MscExampleIpAddressProvFreeIpAddressList1RowStatus_Type()
)
mscExampleIpAddressProvFreeIpAddressList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleIpAddressProvFreeIpAddressList1RowStatus.setStatus("mandatory")
_MscExampleString_ObjectIdentity = ObjectIdentity
mscExampleString = _MscExampleString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5)
)
_MscExampleStringRowStatusTable_Object = MibTable
mscExampleStringRowStatusTable = _MscExampleStringRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1)
)
if mibBuilder.loadTexts:
    mscExampleStringRowStatusTable.setStatus("mandatory")
_MscExampleStringRowStatusEntry_Object = MibTableRow
mscExampleStringRowStatusEntry = _MscExampleStringRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1, 1)
)
mscExampleStringRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringRowStatusEntry.setStatus("mandatory")
_MscExampleStringRowStatus_Type = RowStatus
_MscExampleStringRowStatus_Object = MibTableColumn
mscExampleStringRowStatus = _MscExampleStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1, 1, 1),
    _MscExampleStringRowStatus_Type()
)
mscExampleStringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringRowStatus.setStatus("mandatory")
_MscExampleStringComponentName_Type = DisplayString
_MscExampleStringComponentName_Object = MibTableColumn
mscExampleStringComponentName = _MscExampleStringComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1, 1, 2),
    _MscExampleStringComponentName_Type()
)
mscExampleStringComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleStringComponentName.setStatus("mandatory")
_MscExampleStringStorageType_Type = StorageType
_MscExampleStringStorageType_Object = MibTableColumn
mscExampleStringStorageType = _MscExampleStringStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1, 1, 4),
    _MscExampleStringStorageType_Type()
)
mscExampleStringStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleStringStorageType.setStatus("mandatory")


class _MscExampleStringIndex_Type(AsciiStringIndex):
    """Custom type mscExampleStringIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleStringIndex_Type.__name__ = "AsciiStringIndex"
_MscExampleStringIndex_Object = MibTableColumn
mscExampleStringIndex = _MscExampleStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1, 1, 10),
    _MscExampleStringIndex_Type()
)
mscExampleStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringIndex.setStatus("mandatory")
_MscExampleStringOperationalTable_Object = MibTable
mscExampleStringOperationalTable = _MscExampleStringOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 10)
)
if mibBuilder.loadTexts:
    mscExampleStringOperationalTable.setStatus("mandatory")
_MscExampleStringOperationalEntry_Object = MibTableRow
mscExampleStringOperationalEntry = _MscExampleStringOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 10, 1)
)
mscExampleStringOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperationalEntry.setStatus("mandatory")


class _MscExampleStringOperStructAsciiOnly_Type(AsciiString):
    """Custom type mscExampleStringOperStructAsciiOnly based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperStructAsciiOnly_Type.__name__ = "AsciiString"
_MscExampleStringOperStructAsciiOnly_Object = MibTableColumn
mscExampleStringOperStructAsciiOnly = _MscExampleStringOperStructAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 10, 1, 1),
    _MscExampleStringOperStructAsciiOnly_Type()
)
mscExampleStringOperStructAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperStructAsciiOnly.setStatus("mandatory")


class _MscExampleStringOperStructHexOnly_Type(HexString):
    """Custom type mscExampleStringOperStructHexOnly based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleStringOperStructHexOnly_Type.__name__ = "HexString"
_MscExampleStringOperStructHexOnly_Object = MibTableColumn
mscExampleStringOperStructHexOnly = _MscExampleStringOperStructHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 10, 1, 2),
    _MscExampleStringOperStructHexOnly_Type()
)
mscExampleStringOperStructHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperStructHexOnly.setStatus("mandatory")


class _MscExampleStringOperFreeAsciiOnly_Type(AsciiString):
    """Custom type mscExampleStringOperFreeAsciiOnly based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperFreeAsciiOnly_Type.__name__ = "AsciiString"
_MscExampleStringOperFreeAsciiOnly_Object = MibTableColumn
mscExampleStringOperFreeAsciiOnly = _MscExampleStringOperFreeAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 10, 1, 3),
    _MscExampleStringOperFreeAsciiOnly_Type()
)
mscExampleStringOperFreeAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeAsciiOnly.setStatus("mandatory")


class _MscExampleStringOperFreeHexOnly_Type(HexString):
    """Custom type mscExampleStringOperFreeHexOnly based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleStringOperFreeHexOnly_Type.__name__ = "HexString"
_MscExampleStringOperFreeHexOnly_Object = MibTableColumn
mscExampleStringOperFreeHexOnly = _MscExampleStringOperFreeHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 10, 1, 4),
    _MscExampleStringOperFreeHexOnly_Type()
)
mscExampleStringOperFreeHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeHexOnly.setStatus("mandatory")
_MscExampleStringProvisionalTable_Object = MibTable
mscExampleStringProvisionalTable = _MscExampleStringProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11)
)
if mibBuilder.loadTexts:
    mscExampleStringProvisionalTable.setStatus("mandatory")
_MscExampleStringProvisionalEntry_Object = MibTableRow
mscExampleStringProvisionalEntry = _MscExampleStringProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1)
)
mscExampleStringProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvisionalEntry.setStatus("mandatory")
_MscExampleStringProvStringSub_Type = Link
_MscExampleStringProvStringSub_Object = MibTableColumn
mscExampleStringProvStringSub = _MscExampleStringProvStringSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 1),
    _MscExampleStringProvStringSub_Type()
)
mscExampleStringProvStringSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvStringSub.setStatus("mandatory")


class _MscExampleStringProvStructAsciiOnly_Type(AsciiString):
    """Custom type mscExampleStringProvStructAsciiOnly based on AsciiString"""
    defaultHexValue = "596f2e"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_MscExampleStringProvStructAsciiOnly_Type.__name__ = "AsciiString"
_MscExampleStringProvStructAsciiOnly_Object = MibTableColumn
mscExampleStringProvStructAsciiOnly = _MscExampleStringProvStructAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 2),
    _MscExampleStringProvStructAsciiOnly_Type()
)
mscExampleStringProvStructAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvStructAsciiOnly.setStatus("mandatory")


class _MscExampleStringProvStructHexOnly_Type(HexString):
    """Custom type mscExampleStringProvStructHexOnly based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleStringProvStructHexOnly_Type.__name__ = "HexString"
_MscExampleStringProvStructHexOnly_Object = MibTableColumn
mscExampleStringProvStructHexOnly = _MscExampleStringProvStructHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 3),
    _MscExampleStringProvStructHexOnly_Type()
)
mscExampleStringProvStructHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvStructHexOnly.setStatus("mandatory")


class _MscExampleStringProvFreeAsciiOnly_Type(AsciiString):
    """Custom type mscExampleStringProvFreeAsciiOnly based on AsciiString"""
    defaultHexValue = "46726565205374616e64696e6720537472696e6720212121"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_MscExampleStringProvFreeAsciiOnly_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeAsciiOnly_Object = MibTableColumn
mscExampleStringProvFreeAsciiOnly = _MscExampleStringProvFreeAsciiOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 4),
    _MscExampleStringProvFreeAsciiOnly_Type()
)
mscExampleStringProvFreeAsciiOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeAsciiOnly.setStatus("mandatory")


class _MscExampleStringProvFreeAsciiOnly1_Type(AsciiString):
    """Custom type mscExampleStringProvFreeAsciiOnly1 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeAsciiOnly1_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeAsciiOnly1_Object = MibTableColumn
mscExampleStringProvFreeAsciiOnly1 = _MscExampleStringProvFreeAsciiOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 5),
    _MscExampleStringProvFreeAsciiOnly1_Type()
)
mscExampleStringProvFreeAsciiOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeAsciiOnly1.setStatus("mandatory")


class _MscExampleStringProvFreeHexOnly_Type(HexString):
    """Custom type mscExampleStringProvFreeHexOnly based on HexString"""
    defaultHexValue = "0102030405060708090A"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleStringProvFreeHexOnly_Type.__name__ = "HexString"
_MscExampleStringProvFreeHexOnly_Object = MibTableColumn
mscExampleStringProvFreeHexOnly = _MscExampleStringProvFreeHexOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 6),
    _MscExampleStringProvFreeHexOnly_Type()
)
mscExampleStringProvFreeHexOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeHexOnly.setStatus("mandatory")


class _MscExampleStringProvFreeHexOnly1_Type(HexString):
    """Custom type mscExampleStringProvFreeHexOnly1 based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MscExampleStringProvFreeHexOnly1_Type.__name__ = "HexString"
_MscExampleStringProvFreeHexOnly1_Object = MibTableColumn
mscExampleStringProvFreeHexOnly1 = _MscExampleStringProvFreeHexOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 11, 1, 7),
    _MscExampleStringProvFreeHexOnly1_Type()
)
mscExampleStringProvFreeHexOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeHexOnly1.setStatus("mandatory")
_MscExampleStringOperStructStrVectorTable_Object = MibTable
mscExampleStringOperStructStrVectorTable = _MscExampleStringOperStructStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1073)
)
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrVectorTable.setStatus("mandatory")
_MscExampleStringOperStructStrVectorEntry_Object = MibTableRow
mscExampleStringOperStructStrVectorEntry = _MscExampleStringOperStructStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1073, 1)
)
mscExampleStringOperStructStrVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperStructStrVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrVectorEntry.setStatus("mandatory")


class _MscExampleStringOperStructStrVectorIndex_Type(Integer32):
    """Custom type mscExampleStringOperStructStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleStringOperStructStrVectorIndex_Type.__name__ = "Integer32"
_MscExampleStringOperStructStrVectorIndex_Object = MibTableColumn
mscExampleStringOperStructStrVectorIndex = _MscExampleStringOperStructStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1073, 1, 1),
    _MscExampleStringOperStructStrVectorIndex_Type()
)
mscExampleStringOperStructStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrVectorIndex.setStatus("mandatory")


class _MscExampleStringOperStructStrVectorValue_Type(AsciiString):
    """Custom type mscExampleStringOperStructStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperStructStrVectorValue_Type.__name__ = "AsciiString"
_MscExampleStringOperStructStrVectorValue_Object = MibTableColumn
mscExampleStringOperStructStrVectorValue = _MscExampleStringOperStructStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1073, 1, 2),
    _MscExampleStringOperStructStrVectorValue_Type()
)
mscExampleStringOperStructStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrVectorValue.setStatus("mandatory")
_MscExampleStringOperStructStrArrayTable_Object = MibTable
mscExampleStringOperStructStrArrayTable = _MscExampleStringOperStructStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1074)
)
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrArrayTable.setStatus("mandatory")
_MscExampleStringOperStructStrArrayEntry_Object = MibTableRow
mscExampleStringOperStructStrArrayEntry = _MscExampleStringOperStructStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1074, 1)
)
mscExampleStringOperStructStrArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperStructStrArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperStructStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrArrayEntry.setStatus("mandatory")


class _MscExampleStringOperStructStrArrayRowIndex_Type(Integer32):
    """Custom type mscExampleStringOperStructStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleStringOperStructStrArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleStringOperStructStrArrayRowIndex_Object = MibTableColumn
mscExampleStringOperStructStrArrayRowIndex = _MscExampleStringOperStructStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1074, 1, 1),
    _MscExampleStringOperStructStrArrayRowIndex_Type()
)
mscExampleStringOperStructStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrArrayRowIndex.setStatus("mandatory")


class _MscExampleStringOperStructStrArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleStringOperStructStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleStringOperStructStrArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleStringOperStructStrArrayColumnIndex_Object = MibTableColumn
mscExampleStringOperStructStrArrayColumnIndex = _MscExampleStringOperStructStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1074, 1, 2),
    _MscExampleStringOperStructStrArrayColumnIndex_Type()
)
mscExampleStringOperStructStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrArrayColumnIndex.setStatus("mandatory")


class _MscExampleStringOperStructStrArrayValue_Type(AsciiString):
    """Custom type mscExampleStringOperStructStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperStructStrArrayValue_Type.__name__ = "AsciiString"
_MscExampleStringOperStructStrArrayValue_Object = MibTableColumn
mscExampleStringOperStructStrArrayValue = _MscExampleStringOperStructStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1074, 1, 3),
    _MscExampleStringOperStructStrArrayValue_Type()
)
mscExampleStringOperStructStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperStructStrArrayValue.setStatus("mandatory")
_MscExampleStringOperFreeStrVectorTable_Object = MibTable
mscExampleStringOperFreeStrVectorTable = _MscExampleStringOperFreeStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1075)
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrVectorTable.setStatus("mandatory")
_MscExampleStringOperFreeStrVectorEntry_Object = MibTableRow
mscExampleStringOperFreeStrVectorEntry = _MscExampleStringOperFreeStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1075, 1)
)
mscExampleStringOperFreeStrVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperFreeStrVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrVectorEntry.setStatus("mandatory")


class _MscExampleStringOperFreeStrVectorIndex_Type(Integer32):
    """Custom type mscExampleStringOperFreeStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleStringOperFreeStrVectorIndex_Type.__name__ = "Integer32"
_MscExampleStringOperFreeStrVectorIndex_Object = MibTableColumn
mscExampleStringOperFreeStrVectorIndex = _MscExampleStringOperFreeStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1075, 1, 1),
    _MscExampleStringOperFreeStrVectorIndex_Type()
)
mscExampleStringOperFreeStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrVectorIndex.setStatus("mandatory")


class _MscExampleStringOperFreeStrVectorValue_Type(AsciiString):
    """Custom type mscExampleStringOperFreeStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperFreeStrVectorValue_Type.__name__ = "AsciiString"
_MscExampleStringOperFreeStrVectorValue_Object = MibTableColumn
mscExampleStringOperFreeStrVectorValue = _MscExampleStringOperFreeStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1075, 1, 2),
    _MscExampleStringOperFreeStrVectorValue_Type()
)
mscExampleStringOperFreeStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrVectorValue.setStatus("mandatory")
_MscExampleStringOperFreeStrArrayTable_Object = MibTable
mscExampleStringOperFreeStrArrayTable = _MscExampleStringOperFreeStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1076)
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrArrayTable.setStatus("mandatory")
_MscExampleStringOperFreeStrArrayEntry_Object = MibTableRow
mscExampleStringOperFreeStrArrayEntry = _MscExampleStringOperFreeStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1076, 1)
)
mscExampleStringOperFreeStrArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperFreeStrArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperFreeStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrArrayEntry.setStatus("mandatory")


class _MscExampleStringOperFreeStrArrayRowIndex_Type(Integer32):
    """Custom type mscExampleStringOperFreeStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleStringOperFreeStrArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleStringOperFreeStrArrayRowIndex_Object = MibTableColumn
mscExampleStringOperFreeStrArrayRowIndex = _MscExampleStringOperFreeStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1076, 1, 1),
    _MscExampleStringOperFreeStrArrayRowIndex_Type()
)
mscExampleStringOperFreeStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrArrayRowIndex.setStatus("mandatory")


class _MscExampleStringOperFreeStrArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleStringOperFreeStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleStringOperFreeStrArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleStringOperFreeStrArrayColumnIndex_Object = MibTableColumn
mscExampleStringOperFreeStrArrayColumnIndex = _MscExampleStringOperFreeStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1076, 1, 2),
    _MscExampleStringOperFreeStrArrayColumnIndex_Type()
)
mscExampleStringOperFreeStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrArrayColumnIndex.setStatus("mandatory")


class _MscExampleStringOperFreeStrArrayValue_Type(AsciiString):
    """Custom type mscExampleStringOperFreeStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperFreeStrArrayValue_Type.__name__ = "AsciiString"
_MscExampleStringOperFreeStrArrayValue_Object = MibTableColumn
mscExampleStringOperFreeStrArrayValue = _MscExampleStringOperFreeStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1076, 1, 3),
    _MscExampleStringOperFreeStrArrayValue_Type()
)
mscExampleStringOperFreeStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrArrayValue.setStatus("mandatory")
_MscExampleStringOperFreeStrReplicatedTable_Object = MibTable
mscExampleStringOperFreeStrReplicatedTable = _MscExampleStringOperFreeStrReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1077)
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrReplicatedTable.setStatus("mandatory")
_MscExampleStringOperFreeStrReplicatedEntry_Object = MibTableRow
mscExampleStringOperFreeStrReplicatedEntry = _MscExampleStringOperFreeStrReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1077, 1)
)
mscExampleStringOperFreeStrReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperFreeStrReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrReplicatedEntry.setStatus("mandatory")


class _MscExampleStringOperFreeStrReplicatedIndex_Type(AsciiString):
    """Custom type mscExampleStringOperFreeStrReplicatedIndex based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperFreeStrReplicatedIndex_Type.__name__ = "AsciiString"
_MscExampleStringOperFreeStrReplicatedIndex_Object = MibTableColumn
mscExampleStringOperFreeStrReplicatedIndex = _MscExampleStringOperFreeStrReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1077, 1, 1),
    _MscExampleStringOperFreeStrReplicatedIndex_Type()
)
mscExampleStringOperFreeStrReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrReplicatedIndex.setStatus("mandatory")


class _MscExampleStringOperFreeStrReplicatedValue_Type(AsciiString):
    """Custom type mscExampleStringOperFreeStrReplicatedValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringOperFreeStrReplicatedValue_Type.__name__ = "AsciiString"
_MscExampleStringOperFreeStrReplicatedValue_Object = MibTableColumn
mscExampleStringOperFreeStrReplicatedValue = _MscExampleStringOperFreeStrReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1077, 1, 2),
    _MscExampleStringOperFreeStrReplicatedValue_Type()
)
mscExampleStringOperFreeStrReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrReplicatedValue.setStatus("mandatory")
_MscExampleStringOperFreeStrReplicatedRowStatus_Type = RowStatus
_MscExampleStringOperFreeStrReplicatedRowStatus_Object = MibTableColumn
mscExampleStringOperFreeStrReplicatedRowStatus = _MscExampleStringOperFreeStrReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1077, 1, 3),
    _MscExampleStringOperFreeStrReplicatedRowStatus_Type()
)
mscExampleStringOperFreeStrReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrReplicatedRowStatus.setStatus("mandatory")
_MscExampleStringOperFreeStrListTable_Object = MibTable
mscExampleStringOperFreeStrListTable = _MscExampleStringOperFreeStrListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1078)
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrListTable.setStatus("mandatory")
_MscExampleStringOperFreeStrListEntry_Object = MibTableRow
mscExampleStringOperFreeStrListEntry = _MscExampleStringOperFreeStrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1078, 1)
)
mscExampleStringOperFreeStrListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringOperFreeStrListValue"),
)
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrListEntry.setStatus("mandatory")


class _MscExampleStringOperFreeStrListValue_Type(AsciiString):
    """Custom type mscExampleStringOperFreeStrListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MscExampleStringOperFreeStrListValue_Type.__name__ = "AsciiString"
_MscExampleStringOperFreeStrListValue_Object = MibTableColumn
mscExampleStringOperFreeStrListValue = _MscExampleStringOperFreeStrListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1078, 1, 1),
    _MscExampleStringOperFreeStrListValue_Type()
)
mscExampleStringOperFreeStrListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrListValue.setStatus("mandatory")
_MscExampleStringOperFreeStrListRowStatus_Type = RowStatus
_MscExampleStringOperFreeStrListRowStatus_Object = MibTableColumn
mscExampleStringOperFreeStrListRowStatus = _MscExampleStringOperFreeStrListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1078, 1, 2),
    _MscExampleStringOperFreeStrListRowStatus_Type()
)
mscExampleStringOperFreeStrListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleStringOperFreeStrListRowStatus.setStatus("mandatory")
_MscExampleStringProvStructStrVectorTable_Object = MibTable
mscExampleStringProvStructStrVectorTable = _MscExampleStringProvStructStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1079)
)
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrVectorTable.setStatus("mandatory")
_MscExampleStringProvStructStrVectorEntry_Object = MibTableRow
mscExampleStringProvStructStrVectorEntry = _MscExampleStringProvStructStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1079, 1)
)
mscExampleStringProvStructStrVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvStructStrVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrVectorEntry.setStatus("mandatory")


class _MscExampleStringProvStructStrVectorIndex_Type(Integer32):
    """Custom type mscExampleStringProvStructStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleStringProvStructStrVectorIndex_Type.__name__ = "Integer32"
_MscExampleStringProvStructStrVectorIndex_Object = MibTableColumn
mscExampleStringProvStructStrVectorIndex = _MscExampleStringProvStructStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1079, 1, 1),
    _MscExampleStringProvStructStrVectorIndex_Type()
)
mscExampleStringProvStructStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrVectorIndex.setStatus("mandatory")


class _MscExampleStringProvStructStrVectorValue_Type(AsciiString):
    """Custom type mscExampleStringProvStructStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvStructStrVectorValue_Type.__name__ = "AsciiString"
_MscExampleStringProvStructStrVectorValue_Object = MibTableColumn
mscExampleStringProvStructStrVectorValue = _MscExampleStringProvStructStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1079, 1, 2),
    _MscExampleStringProvStructStrVectorValue_Type()
)
mscExampleStringProvStructStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrVectorValue.setStatus("mandatory")
_MscExampleStringProvStructStrArrayTable_Object = MibTable
mscExampleStringProvStructStrArrayTable = _MscExampleStringProvStructStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1080)
)
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrArrayTable.setStatus("mandatory")
_MscExampleStringProvStructStrArrayEntry_Object = MibTableRow
mscExampleStringProvStructStrArrayEntry = _MscExampleStringProvStructStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1080, 1)
)
mscExampleStringProvStructStrArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvStructStrArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvStructStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrArrayEntry.setStatus("mandatory")


class _MscExampleStringProvStructStrArrayRowIndex_Type(Integer32):
    """Custom type mscExampleStringProvStructStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleStringProvStructStrArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleStringProvStructStrArrayRowIndex_Object = MibTableColumn
mscExampleStringProvStructStrArrayRowIndex = _MscExampleStringProvStructStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1080, 1, 1),
    _MscExampleStringProvStructStrArrayRowIndex_Type()
)
mscExampleStringProvStructStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrArrayRowIndex.setStatus("mandatory")


class _MscExampleStringProvStructStrArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleStringProvStructStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleStringProvStructStrArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleStringProvStructStrArrayColumnIndex_Object = MibTableColumn
mscExampleStringProvStructStrArrayColumnIndex = _MscExampleStringProvStructStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1080, 1, 2),
    _MscExampleStringProvStructStrArrayColumnIndex_Type()
)
mscExampleStringProvStructStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrArrayColumnIndex.setStatus("mandatory")


class _MscExampleStringProvStructStrArrayValue_Type(AsciiString):
    """Custom type mscExampleStringProvStructStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvStructStrArrayValue_Type.__name__ = "AsciiString"
_MscExampleStringProvStructStrArrayValue_Object = MibTableColumn
mscExampleStringProvStructStrArrayValue = _MscExampleStringProvStructStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1080, 1, 3),
    _MscExampleStringProvStructStrArrayValue_Type()
)
mscExampleStringProvStructStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvStructStrArrayValue.setStatus("mandatory")
_MscExampleStringProvFreeStrVectorTable_Object = MibTable
mscExampleStringProvFreeStrVectorTable = _MscExampleStringProvFreeStrVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1081)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVectorTable.setStatus("mandatory")
_MscExampleStringProvFreeStrVectorEntry_Object = MibTableRow
mscExampleStringProvFreeStrVectorEntry = _MscExampleStringProvFreeStrVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1081, 1)
)
mscExampleStringProvFreeStrVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVectorEntry.setStatus("mandatory")


class _MscExampleStringProvFreeStrVectorIndex_Type(Integer32):
    """Custom type mscExampleStringProvFreeStrVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleStringProvFreeStrVectorIndex_Type.__name__ = "Integer32"
_MscExampleStringProvFreeStrVectorIndex_Object = MibTableColumn
mscExampleStringProvFreeStrVectorIndex = _MscExampleStringProvFreeStrVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1081, 1, 1),
    _MscExampleStringProvFreeStrVectorIndex_Type()
)
mscExampleStringProvFreeStrVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVectorIndex.setStatus("mandatory")


class _MscExampleStringProvFreeStrVectorValue_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrVectorValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrVectorValue_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrVectorValue_Object = MibTableColumn
mscExampleStringProvFreeStrVectorValue = _MscExampleStringProvFreeStrVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1081, 1, 2),
    _MscExampleStringProvFreeStrVectorValue_Type()
)
mscExampleStringProvFreeStrVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVectorValue.setStatus("mandatory")
_MscExampleStringProvFreeStrVector1Table_Object = MibTable
mscExampleStringProvFreeStrVector1Table = _MscExampleStringProvFreeStrVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1082)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVector1Table.setStatus("mandatory")
_MscExampleStringProvFreeStrVector1Entry_Object = MibTableRow
mscExampleStringProvFreeStrVector1Entry = _MscExampleStringProvFreeStrVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1082, 1)
)
mscExampleStringProvFreeStrVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVector1Entry.setStatus("mandatory")


class _MscExampleStringProvFreeStrVector1Index_Type(Integer32):
    """Custom type mscExampleStringProvFreeStrVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrVector1Index_Type.__name__ = "Integer32"
_MscExampleStringProvFreeStrVector1Index_Object = MibTableColumn
mscExampleStringProvFreeStrVector1Index = _MscExampleStringProvFreeStrVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1082, 1, 1),
    _MscExampleStringProvFreeStrVector1Index_Type()
)
mscExampleStringProvFreeStrVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVector1Index.setStatus("mandatory")


class _MscExampleStringProvFreeStrVector1Value_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrVector1Value based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrVector1Value_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrVector1Value_Object = MibTableColumn
mscExampleStringProvFreeStrVector1Value = _MscExampleStringProvFreeStrVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1082, 1, 2),
    _MscExampleStringProvFreeStrVector1Value_Type()
)
mscExampleStringProvFreeStrVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrVector1Value.setStatus("mandatory")
_MscExampleStringProvFreeStrArrayTable_Object = MibTable
mscExampleStringProvFreeStrArrayTable = _MscExampleStringProvFreeStrArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1083)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArrayTable.setStatus("mandatory")
_MscExampleStringProvFreeStrArrayEntry_Object = MibTableRow
mscExampleStringProvFreeStrArrayEntry = _MscExampleStringProvFreeStrArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1083, 1)
)
mscExampleStringProvFreeStrArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArrayEntry.setStatus("mandatory")


class _MscExampleStringProvFreeStrArrayRowIndex_Type(Integer32):
    """Custom type mscExampleStringProvFreeStrArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleStringProvFreeStrArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleStringProvFreeStrArrayRowIndex_Object = MibTableColumn
mscExampleStringProvFreeStrArrayRowIndex = _MscExampleStringProvFreeStrArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1083, 1, 1),
    _MscExampleStringProvFreeStrArrayRowIndex_Type()
)
mscExampleStringProvFreeStrArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArrayRowIndex.setStatus("mandatory")


class _MscExampleStringProvFreeStrArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleStringProvFreeStrArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleStringProvFreeStrArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleStringProvFreeStrArrayColumnIndex_Object = MibTableColumn
mscExampleStringProvFreeStrArrayColumnIndex = _MscExampleStringProvFreeStrArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1083, 1, 2),
    _MscExampleStringProvFreeStrArrayColumnIndex_Type()
)
mscExampleStringProvFreeStrArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArrayColumnIndex.setStatus("mandatory")


class _MscExampleStringProvFreeStrArrayValue_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrArrayValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrArrayValue_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrArrayValue_Object = MibTableColumn
mscExampleStringProvFreeStrArrayValue = _MscExampleStringProvFreeStrArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1083, 1, 3),
    _MscExampleStringProvFreeStrArrayValue_Type()
)
mscExampleStringProvFreeStrArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArrayValue.setStatus("mandatory")
_MscExampleStringProvFreeStrArray1Table_Object = MibTable
mscExampleStringProvFreeStrArray1Table = _MscExampleStringProvFreeStrArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1084)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArray1Table.setStatus("mandatory")
_MscExampleStringProvFreeStrArray1Entry_Object = MibTableRow
mscExampleStringProvFreeStrArray1Entry = _MscExampleStringProvFreeStrArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1084, 1)
)
mscExampleStringProvFreeStrArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrArray1RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArray1Entry.setStatus("mandatory")


class _MscExampleStringProvFreeStrArray1RowIndex_Type(Integer32):
    """Custom type mscExampleStringProvFreeStrArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscExampleStringProvFreeStrArray1RowIndex_Type.__name__ = "Integer32"
_MscExampleStringProvFreeStrArray1RowIndex_Object = MibTableColumn
mscExampleStringProvFreeStrArray1RowIndex = _MscExampleStringProvFreeStrArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1084, 1, 1),
    _MscExampleStringProvFreeStrArray1RowIndex_Type()
)
mscExampleStringProvFreeStrArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArray1RowIndex.setStatus("mandatory")


class _MscExampleStringProvFreeStrArray1ColumnIndex_Type(Integer32):
    """Custom type mscExampleStringProvFreeStrArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleStringProvFreeStrArray1ColumnIndex_Type.__name__ = "Integer32"
_MscExampleStringProvFreeStrArray1ColumnIndex_Object = MibTableColumn
mscExampleStringProvFreeStrArray1ColumnIndex = _MscExampleStringProvFreeStrArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1084, 1, 2),
    _MscExampleStringProvFreeStrArray1ColumnIndex_Type()
)
mscExampleStringProvFreeStrArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArray1ColumnIndex.setStatus("mandatory")


class _MscExampleStringProvFreeStrArray1Value_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrArray1Value based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrArray1Value_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrArray1Value_Object = MibTableColumn
mscExampleStringProvFreeStrArray1Value = _MscExampleStringProvFreeStrArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1084, 1, 3),
    _MscExampleStringProvFreeStrArray1Value_Type()
)
mscExampleStringProvFreeStrArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrArray1Value.setStatus("mandatory")
_MscExampleStringProvFreeStrReplicatedTable_Object = MibTable
mscExampleStringProvFreeStrReplicatedTable = _MscExampleStringProvFreeStrReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1085)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrReplicatedTable.setStatus("mandatory")
_MscExampleStringProvFreeStrReplicatedEntry_Object = MibTableRow
mscExampleStringProvFreeStrReplicatedEntry = _MscExampleStringProvFreeStrReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1085, 1)
)
mscExampleStringProvFreeStrReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrReplicatedEntry.setStatus("mandatory")


class _MscExampleStringProvFreeStrReplicatedIndex_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrReplicatedIndex based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrReplicatedIndex_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrReplicatedIndex_Object = MibTableColumn
mscExampleStringProvFreeStrReplicatedIndex = _MscExampleStringProvFreeStrReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1085, 1, 1),
    _MscExampleStringProvFreeStrReplicatedIndex_Type()
)
mscExampleStringProvFreeStrReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrReplicatedIndex.setStatus("mandatory")


class _MscExampleStringProvFreeStrReplicatedValue_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrReplicatedValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleStringProvFreeStrReplicatedValue_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrReplicatedValue_Object = MibTableColumn
mscExampleStringProvFreeStrReplicatedValue = _MscExampleStringProvFreeStrReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1085, 1, 2),
    _MscExampleStringProvFreeStrReplicatedValue_Type()
)
mscExampleStringProvFreeStrReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrReplicatedValue.setStatus("mandatory")
_MscExampleStringProvFreeStrReplicatedRowStatus_Type = RowStatus
_MscExampleStringProvFreeStrReplicatedRowStatus_Object = MibTableColumn
mscExampleStringProvFreeStrReplicatedRowStatus = _MscExampleStringProvFreeStrReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1085, 1, 3),
    _MscExampleStringProvFreeStrReplicatedRowStatus_Type()
)
mscExampleStringProvFreeStrReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrReplicatedRowStatus.setStatus("mandatory")
_MscExampleStringProvFreeStrListTable_Object = MibTable
mscExampleStringProvFreeStrListTable = _MscExampleStringProvFreeStrListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1086)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrListTable.setStatus("mandatory")
_MscExampleStringProvFreeStrListEntry_Object = MibTableRow
mscExampleStringProvFreeStrListEntry = _MscExampleStringProvFreeStrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1086, 1)
)
mscExampleStringProvFreeStrListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrListValue"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrListEntry.setStatus("mandatory")


class _MscExampleStringProvFreeStrListValue_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrListValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MscExampleStringProvFreeStrListValue_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrListValue_Object = MibTableColumn
mscExampleStringProvFreeStrListValue = _MscExampleStringProvFreeStrListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1086, 1, 1),
    _MscExampleStringProvFreeStrListValue_Type()
)
mscExampleStringProvFreeStrListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrListValue.setStatus("mandatory")
_MscExampleStringProvFreeStrListRowStatus_Type = RowStatus
_MscExampleStringProvFreeStrListRowStatus_Object = MibTableColumn
mscExampleStringProvFreeStrListRowStatus = _MscExampleStringProvFreeStrListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1086, 1, 2),
    _MscExampleStringProvFreeStrListRowStatus_Type()
)
mscExampleStringProvFreeStrListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrListRowStatus.setStatus("mandatory")
_MscExampleStringProvFreeStrList1Table_Object = MibTable
mscExampleStringProvFreeStrList1Table = _MscExampleStringProvFreeStrList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1087)
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrList1Table.setStatus("mandatory")
_MscExampleStringProvFreeStrList1Entry_Object = MibTableRow
mscExampleStringProvFreeStrList1Entry = _MscExampleStringProvFreeStrList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1087, 1)
)
mscExampleStringProvFreeStrList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleStringProvFreeStrList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrList1Entry.setStatus("mandatory")


class _MscExampleStringProvFreeStrList1Value_Type(AsciiString):
    """Custom type mscExampleStringProvFreeStrList1Value based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MscExampleStringProvFreeStrList1Value_Type.__name__ = "AsciiString"
_MscExampleStringProvFreeStrList1Value_Object = MibTableColumn
mscExampleStringProvFreeStrList1Value = _MscExampleStringProvFreeStrList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1087, 1, 1),
    _MscExampleStringProvFreeStrList1Value_Type()
)
mscExampleStringProvFreeStrList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrList1Value.setStatus("mandatory")
_MscExampleStringProvFreeStrList1RowStatus_Type = RowStatus
_MscExampleStringProvFreeStrList1RowStatus_Object = MibTableColumn
mscExampleStringProvFreeStrList1RowStatus = _MscExampleStringProvFreeStrList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 5, 1087, 1, 2),
    _MscExampleStringProvFreeStrList1RowStatus_Type()
)
mscExampleStringProvFreeStrList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleStringProvFreeStrList1RowStatus.setStatus("mandatory")
_MscExampleFixedPt_ObjectIdentity = ObjectIdentity
mscExampleFixedPt = _MscExampleFixedPt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6)
)
_MscExampleFixedPtRowStatusTable_Object = MibTable
mscExampleFixedPtRowStatusTable = _MscExampleFixedPtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtRowStatusTable.setStatus("mandatory")
_MscExampleFixedPtRowStatusEntry_Object = MibTableRow
mscExampleFixedPtRowStatusEntry = _MscExampleFixedPtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1, 1)
)
mscExampleFixedPtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtRowStatusEntry.setStatus("mandatory")
_MscExampleFixedPtRowStatus_Type = RowStatus
_MscExampleFixedPtRowStatus_Object = MibTableColumn
mscExampleFixedPtRowStatus = _MscExampleFixedPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1, 1, 1),
    _MscExampleFixedPtRowStatus_Type()
)
mscExampleFixedPtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtRowStatus.setStatus("mandatory")
_MscExampleFixedPtComponentName_Type = DisplayString
_MscExampleFixedPtComponentName_Object = MibTableColumn
mscExampleFixedPtComponentName = _MscExampleFixedPtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1, 1, 2),
    _MscExampleFixedPtComponentName_Type()
)
mscExampleFixedPtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleFixedPtComponentName.setStatus("mandatory")
_MscExampleFixedPtStorageType_Type = StorageType
_MscExampleFixedPtStorageType_Object = MibTableColumn
mscExampleFixedPtStorageType = _MscExampleFixedPtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1, 1, 4),
    _MscExampleFixedPtStorageType_Type()
)
mscExampleFixedPtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleFixedPtStorageType.setStatus("mandatory")
_MscExampleFixedPtIndex_Type = NonReplicated
_MscExampleFixedPtIndex_Object = MibTableColumn
mscExampleFixedPtIndex = _MscExampleFixedPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1, 1, 10),
    _MscExampleFixedPtIndex_Type()
)
mscExampleFixedPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtIndex.setStatus("mandatory")
_MscExampleFixedPtOperationalTable_Object = MibTable
mscExampleFixedPtOperationalTable = _MscExampleFixedPtOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 10)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperationalTable.setStatus("mandatory")
_MscExampleFixedPtOperationalEntry_Object = MibTableRow
mscExampleFixedPtOperationalEntry = _MscExampleFixedPtOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 10, 1)
)
mscExampleFixedPtOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperationalEntry.setStatus("mandatory")


class _MscExampleFixedPtOperStructFixedPt_Type(FixedPoint4):
    """Custom type mscExampleFixedPtOperStructFixedPt based on FixedPoint4"""
    subtypeSpec = FixedPoint4.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2553300),
    )


_MscExampleFixedPtOperStructFixedPt_Type.__name__ = "FixedPoint4"
_MscExampleFixedPtOperStructFixedPt_Object = MibTableColumn
mscExampleFixedPtOperStructFixedPt = _MscExampleFixedPtOperStructFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 10, 1, 1),
    _MscExampleFixedPtOperStructFixedPt_Type()
)
mscExampleFixedPtOperStructFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPt.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPt_Type(FixedPoint2):
    """Custom type mscExampleFixedPtOperFreeFixedPt based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1099),
        ValueRangeConstraint(10001, 20000),
    )


_MscExampleFixedPtOperFreeFixedPt_Type.__name__ = "FixedPoint2"
_MscExampleFixedPtOperFreeFixedPt_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPt = _MscExampleFixedPtOperFreeFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 10, 1, 2),
    _MscExampleFixedPtOperFreeFixedPt_Type()
)
mscExampleFixedPtOperFreeFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPt.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtSet_Type(OctetString):
    """Custom type mscExampleFixedPtOperFreeFixedPtSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscExampleFixedPtOperFreeFixedPtSet_Type.__name__ = "OctetString"
_MscExampleFixedPtOperFreeFixedPtSet_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtSet = _MscExampleFixedPtOperFreeFixedPtSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 10, 1, 3),
    _MscExampleFixedPtOperFreeFixedPtSet_Type()
)
mscExampleFixedPtOperFreeFixedPtSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtSet.setStatus("mandatory")
_MscExampleFixedPtProvisionalTable_Object = MibTable
mscExampleFixedPtProvisionalTable = _MscExampleFixedPtProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvisionalTable.setStatus("mandatory")
_MscExampleFixedPtProvisionalEntry_Object = MibTableRow
mscExampleFixedPtProvisionalEntry = _MscExampleFixedPtProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11, 1)
)
mscExampleFixedPtProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvisionalEntry.setStatus("mandatory")
_MscExampleFixedPtProvFixedPtSubcomponent_Type = Link
_MscExampleFixedPtProvFixedPtSubcomponent_Object = MibTableColumn
mscExampleFixedPtProvFixedPtSubcomponent = _MscExampleFixedPtProvFixedPtSubcomponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11, 1, 1),
    _MscExampleFixedPtProvFixedPtSubcomponent_Type()
)
mscExampleFixedPtProvFixedPtSubcomponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFixedPtSubcomponent.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPt_Type(FixedPoint3):
    """Custom type mscExampleFixedPtProvStructFixedPt based on FixedPoint3"""
    defaultValue = 253000

    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252000),
        ValueRangeConstraint(253000, 253000),
        ValueRangeConstraint(254000, 254000),
        ValueRangeConstraint(255000, 255000),
    )


_MscExampleFixedPtProvStructFixedPt_Type.__name__ = "FixedPoint3"
_MscExampleFixedPtProvStructFixedPt_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPt = _MscExampleFixedPtProvStructFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11, 1, 2),
    _MscExampleFixedPtProvStructFixedPt_Type()
)
mscExampleFixedPtProvStructFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPt.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPtSet_Type(OctetString):
    """Custom type mscExampleFixedPtProvStructFixedPtSet based on OctetString"""
    defaultHexValue = "c8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscExampleFixedPtProvStructFixedPtSet_Type.__name__ = "OctetString"
_MscExampleFixedPtProvStructFixedPtSet_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPtSet = _MscExampleFixedPtProvStructFixedPtSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11, 1, 3),
    _MscExampleFixedPtProvStructFixedPtSet_Type()
)
mscExampleFixedPtProvStructFixedPtSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtSet.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPt_Type(FixedPoint2):
    """Custom type mscExampleFixedPtProvFreeFixedPt based on FixedPoint2"""
    defaultValue = 10101

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1099),
        ValueRangeConstraint(10001, 20099),
    )


_MscExampleFixedPtProvFreeFixedPt_Type.__name__ = "FixedPoint2"
_MscExampleFixedPtProvFreeFixedPt_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPt = _MscExampleFixedPtProvFreeFixedPt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11, 1, 4),
    _MscExampleFixedPtProvFreeFixedPt_Type()
)
mscExampleFixedPtProvFreeFixedPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPt.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtSet_Type(OctetString):
    """Custom type mscExampleFixedPtProvFreeFixedPtSet based on OctetString"""
    defaultHexValue = "05500002"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscExampleFixedPtProvFreeFixedPtSet_Type.__name__ = "OctetString"
_MscExampleFixedPtProvFreeFixedPtSet_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtSet = _MscExampleFixedPtProvFreeFixedPtSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 11, 1, 5),
    _MscExampleFixedPtProvFreeFixedPtSet_Type()
)
mscExampleFixedPtProvFreeFixedPtSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtSet.setStatus("mandatory")
_MscExampleFixedPtOperStructFixedPtVectorTable_Object = MibTable
mscExampleFixedPtOperStructFixedPtVectorTable = _MscExampleFixedPtOperStructFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1028)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtVectorTable.setStatus("mandatory")
_MscExampleFixedPtOperStructFixedPtVectorEntry_Object = MibTableRow
mscExampleFixedPtOperStructFixedPtVectorEntry = _MscExampleFixedPtOperStructFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1028, 1)
)
mscExampleFixedPtOperStructFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperStructFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtVectorEntry.setStatus("mandatory")


class _MscExampleFixedPtOperStructFixedPtVectorIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperStructFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleFixedPtOperStructFixedPtVectorIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperStructFixedPtVectorIndex_Object = MibTableColumn
mscExampleFixedPtOperStructFixedPtVectorIndex = _MscExampleFixedPtOperStructFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1028, 1, 1),
    _MscExampleFixedPtOperStructFixedPtVectorIndex_Type()
)
mscExampleFixedPtOperStructFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtVectorIndex.setStatus("mandatory")


class _MscExampleFixedPtOperStructFixedPtVectorValue_Type(FixedPoint3):
    """Custom type mscExampleFixedPtOperStructFixedPtVectorValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100100),
    )


_MscExampleFixedPtOperStructFixedPtVectorValue_Type.__name__ = "FixedPoint3"
_MscExampleFixedPtOperStructFixedPtVectorValue_Object = MibTableColumn
mscExampleFixedPtOperStructFixedPtVectorValue = _MscExampleFixedPtOperStructFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1028, 1, 2),
    _MscExampleFixedPtOperStructFixedPtVectorValue_Type()
)
mscExampleFixedPtOperStructFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtVectorValue.setStatus("mandatory")
_MscExampleFixedPtOperStructFixedPtArrayTable_Object = MibTable
mscExampleFixedPtOperStructFixedPtArrayTable = _MscExampleFixedPtOperStructFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1029)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtArrayTable.setStatus("mandatory")
_MscExampleFixedPtOperStructFixedPtArrayEntry_Object = MibTableRow
mscExampleFixedPtOperStructFixedPtArrayEntry = _MscExampleFixedPtOperStructFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1029, 1)
)
mscExampleFixedPtOperStructFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperStructFixedPtArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperStructFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtArrayEntry.setStatus("mandatory")


class _MscExampleFixedPtOperStructFixedPtArrayRowIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperStructFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleFixedPtOperStructFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperStructFixedPtArrayRowIndex_Object = MibTableColumn
mscExampleFixedPtOperStructFixedPtArrayRowIndex = _MscExampleFixedPtOperStructFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1029, 1, 1),
    _MscExampleFixedPtOperStructFixedPtArrayRowIndex_Type()
)
mscExampleFixedPtOperStructFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtArrayRowIndex.setStatus("mandatory")


class _MscExampleFixedPtOperStructFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperStructFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleFixedPtOperStructFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperStructFixedPtArrayColumnIndex_Object = MibTableColumn
mscExampleFixedPtOperStructFixedPtArrayColumnIndex = _MscExampleFixedPtOperStructFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1029, 1, 2),
    _MscExampleFixedPtOperStructFixedPtArrayColumnIndex_Type()
)
mscExampleFixedPtOperStructFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtArrayColumnIndex.setStatus("mandatory")


class _MscExampleFixedPtOperStructFixedPtArrayValue_Type(FixedPoint3):
    """Custom type mscExampleFixedPtOperStructFixedPtArrayValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 255880),
    )


_MscExampleFixedPtOperStructFixedPtArrayValue_Type.__name__ = "FixedPoint3"
_MscExampleFixedPtOperStructFixedPtArrayValue_Object = MibTableColumn
mscExampleFixedPtOperStructFixedPtArrayValue = _MscExampleFixedPtOperStructFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1029, 1, 3),
    _MscExampleFixedPtOperStructFixedPtArrayValue_Type()
)
mscExampleFixedPtOperStructFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperStructFixedPtArrayValue.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtVectorTable_Object = MibTable
mscExampleFixedPtOperFreeFixedPtVectorTable = _MscExampleFixedPtOperFreeFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1030)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtVectorTable.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtVectorEntry_Object = MibTableRow
mscExampleFixedPtOperFreeFixedPtVectorEntry = _MscExampleFixedPtOperFreeFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1030, 1)
)
mscExampleFixedPtOperFreeFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperFreeFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtVectorEntry.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtVectorIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperFreeFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleFixedPtOperFreeFixedPtVectorIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperFreeFixedPtVectorIndex_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtVectorIndex = _MscExampleFixedPtOperFreeFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1030, 1, 1),
    _MscExampleFixedPtOperFreeFixedPtVectorIndex_Type()
)
mscExampleFixedPtOperFreeFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtVectorIndex.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtVectorValue_Type(FixedPoint2):
    """Custom type mscExampleFixedPtOperFreeFixedPtVectorValue based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscExampleFixedPtOperFreeFixedPtVectorValue_Type.__name__ = "FixedPoint2"
_MscExampleFixedPtOperFreeFixedPtVectorValue_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtVectorValue = _MscExampleFixedPtOperFreeFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1030, 1, 2),
    _MscExampleFixedPtOperFreeFixedPtVectorValue_Type()
)
mscExampleFixedPtOperFreeFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtVectorValue.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtArrayTable_Object = MibTable
mscExampleFixedPtOperFreeFixedPtArrayTable = _MscExampleFixedPtOperFreeFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1031)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtArrayTable.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtArrayEntry_Object = MibTableRow
mscExampleFixedPtOperFreeFixedPtArrayEntry = _MscExampleFixedPtOperFreeFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1031, 1)
)
mscExampleFixedPtOperFreeFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperFreeFixedPtArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperFreeFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtArrayEntry.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtArrayRowIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperFreeFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleFixedPtOperFreeFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperFreeFixedPtArrayRowIndex_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtArrayRowIndex = _MscExampleFixedPtOperFreeFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1031, 1, 1),
    _MscExampleFixedPtOperFreeFixedPtArrayRowIndex_Type()
)
mscExampleFixedPtOperFreeFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtArrayRowIndex.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperFreeFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleFixedPtOperFreeFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperFreeFixedPtArrayColumnIndex_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtArrayColumnIndex = _MscExampleFixedPtOperFreeFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1031, 1, 2),
    _MscExampleFixedPtOperFreeFixedPtArrayColumnIndex_Type()
)
mscExampleFixedPtOperFreeFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtArrayColumnIndex.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtArrayValue_Type(FixedPoint3):
    """Custom type mscExampleFixedPtOperFreeFixedPtArrayValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 255),
    )


_MscExampleFixedPtOperFreeFixedPtArrayValue_Type.__name__ = "FixedPoint3"
_MscExampleFixedPtOperFreeFixedPtArrayValue_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtArrayValue = _MscExampleFixedPtOperFreeFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1031, 1, 3),
    _MscExampleFixedPtOperFreeFixedPtArrayValue_Type()
)
mscExampleFixedPtOperFreeFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtArrayValue.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtReplicatedTable_Object = MibTable
mscExampleFixedPtOperFreeFixedPtReplicatedTable = _MscExampleFixedPtOperFreeFixedPtReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1032)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtReplicatedTable.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtReplicatedEntry_Object = MibTableRow
mscExampleFixedPtOperFreeFixedPtReplicatedEntry = _MscExampleFixedPtOperFreeFixedPtReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1032, 1)
)
mscExampleFixedPtOperFreeFixedPtReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperFreeFixedPtReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtReplicatedEntry.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtReplicatedIndex_Type(Integer32):
    """Custom type mscExampleFixedPtOperFreeFixedPtReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleFixedPtOperFreeFixedPtReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtOperFreeFixedPtReplicatedIndex_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtReplicatedIndex = _MscExampleFixedPtOperFreeFixedPtReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1032, 1, 1),
    _MscExampleFixedPtOperFreeFixedPtReplicatedIndex_Type()
)
mscExampleFixedPtOperFreeFixedPtReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtReplicatedIndex.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtReplicatedValue_Type(FixedPoint1):
    """Custom type mscExampleFixedPtOperFreeFixedPtReplicatedValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655350),
    )


_MscExampleFixedPtOperFreeFixedPtReplicatedValue_Type.__name__ = "FixedPoint1"
_MscExampleFixedPtOperFreeFixedPtReplicatedValue_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtReplicatedValue = _MscExampleFixedPtOperFreeFixedPtReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1032, 1, 2),
    _MscExampleFixedPtOperFreeFixedPtReplicatedValue_Type()
)
mscExampleFixedPtOperFreeFixedPtReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtReplicatedValue.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Type = RowStatus
_MscExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtReplicatedRowStatus = _MscExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1032, 1, 3),
    _MscExampleFixedPtOperFreeFixedPtReplicatedRowStatus_Type()
)
mscExampleFixedPtOperFreeFixedPtReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtReplicatedRowStatus.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtListTable_Object = MibTable
mscExampleFixedPtOperFreeFixedPtListTable = _MscExampleFixedPtOperFreeFixedPtListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1033)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtListTable.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtListEntry_Object = MibTableRow
mscExampleFixedPtOperFreeFixedPtListEntry = _MscExampleFixedPtOperFreeFixedPtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1033, 1)
)
mscExampleFixedPtOperFreeFixedPtListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtOperFreeFixedPtListValue"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtListEntry.setStatus("mandatory")


class _MscExampleFixedPtOperFreeFixedPtListValue_Type(Integer32):
    """Custom type mscExampleFixedPtOperFreeFixedPtListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(10000, 20000),
    )


_MscExampleFixedPtOperFreeFixedPtListValue_Type.__name__ = "Integer32"
_MscExampleFixedPtOperFreeFixedPtListValue_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtListValue = _MscExampleFixedPtOperFreeFixedPtListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1033, 1, 1),
    _MscExampleFixedPtOperFreeFixedPtListValue_Type()
)
mscExampleFixedPtOperFreeFixedPtListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtListValue.setStatus("mandatory")
_MscExampleFixedPtOperFreeFixedPtListRowStatus_Type = RowStatus
_MscExampleFixedPtOperFreeFixedPtListRowStatus_Object = MibTableColumn
mscExampleFixedPtOperFreeFixedPtListRowStatus = _MscExampleFixedPtOperFreeFixedPtListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1033, 1, 2),
    _MscExampleFixedPtOperFreeFixedPtListRowStatus_Type()
)
mscExampleFixedPtOperFreeFixedPtListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleFixedPtOperFreeFixedPtListRowStatus.setStatus("mandatory")
_MscExampleFixedPtProvStructFixedPtVectorTable_Object = MibTable
mscExampleFixedPtProvStructFixedPtVectorTable = _MscExampleFixedPtProvStructFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1034)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtVectorTable.setStatus("mandatory")
_MscExampleFixedPtProvStructFixedPtVectorEntry_Object = MibTableRow
mscExampleFixedPtProvStructFixedPtVectorEntry = _MscExampleFixedPtProvStructFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1034, 1)
)
mscExampleFixedPtProvStructFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvStructFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtVectorEntry.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPtVectorIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvStructFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleFixedPtProvStructFixedPtVectorIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvStructFixedPtVectorIndex_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPtVectorIndex = _MscExampleFixedPtProvStructFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1034, 1, 1),
    _MscExampleFixedPtProvStructFixedPtVectorIndex_Type()
)
mscExampleFixedPtProvStructFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtVectorIndex.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPtVectorValue_Type(FixedPoint3):
    """Custom type mscExampleFixedPtProvStructFixedPtVectorValue based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100100),
    )


_MscExampleFixedPtProvStructFixedPtVectorValue_Type.__name__ = "FixedPoint3"
_MscExampleFixedPtProvStructFixedPtVectorValue_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPtVectorValue = _MscExampleFixedPtProvStructFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1034, 1, 2),
    _MscExampleFixedPtProvStructFixedPtVectorValue_Type()
)
mscExampleFixedPtProvStructFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtVectorValue.setStatus("mandatory")
_MscExampleFixedPtProvStructFixedPtArrayTable_Object = MibTable
mscExampleFixedPtProvStructFixedPtArrayTable = _MscExampleFixedPtProvStructFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1035)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtArrayTable.setStatus("mandatory")
_MscExampleFixedPtProvStructFixedPtArrayEntry_Object = MibTableRow
mscExampleFixedPtProvStructFixedPtArrayEntry = _MscExampleFixedPtProvStructFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1035, 1)
)
mscExampleFixedPtProvStructFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvStructFixedPtArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvStructFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtArrayEntry.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPtArrayRowIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvStructFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleFixedPtProvStructFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvStructFixedPtArrayRowIndex_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPtArrayRowIndex = _MscExampleFixedPtProvStructFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1035, 1, 1),
    _MscExampleFixedPtProvStructFixedPtArrayRowIndex_Type()
)
mscExampleFixedPtProvStructFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtArrayRowIndex.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvStructFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleFixedPtProvStructFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvStructFixedPtArrayColumnIndex_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPtArrayColumnIndex = _MscExampleFixedPtProvStructFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1035, 1, 2),
    _MscExampleFixedPtProvStructFixedPtArrayColumnIndex_Type()
)
mscExampleFixedPtProvStructFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtArrayColumnIndex.setStatus("mandatory")


class _MscExampleFixedPtProvStructFixedPtArrayValue_Type(FixedPoint1):
    """Custom type mscExampleFixedPtProvStructFixedPtArrayValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 300),
    )


_MscExampleFixedPtProvStructFixedPtArrayValue_Type.__name__ = "FixedPoint1"
_MscExampleFixedPtProvStructFixedPtArrayValue_Object = MibTableColumn
mscExampleFixedPtProvStructFixedPtArrayValue = _MscExampleFixedPtProvStructFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1035, 1, 3),
    _MscExampleFixedPtProvStructFixedPtArrayValue_Type()
)
mscExampleFixedPtProvStructFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvStructFixedPtArrayValue.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtVectorTable_Object = MibTable
mscExampleFixedPtProvFreeFixedPtVectorTable = _MscExampleFixedPtProvFreeFixedPtVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1036)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtVectorTable.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtVectorEntry_Object = MibTableRow
mscExampleFixedPtProvFreeFixedPtVectorEntry = _MscExampleFixedPtProvFreeFixedPtVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1036, 1)
)
mscExampleFixedPtProvFreeFixedPtVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvFreeFixedPtVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtVectorEntry.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtVectorIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvFreeFixedPtVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleFixedPtProvFreeFixedPtVectorIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvFreeFixedPtVectorIndex_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtVectorIndex = _MscExampleFixedPtProvFreeFixedPtVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1036, 1, 1),
    _MscExampleFixedPtProvFreeFixedPtVectorIndex_Type()
)
mscExampleFixedPtProvFreeFixedPtVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtVectorIndex.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtVectorValue_Type(FixedPoint1):
    """Custom type mscExampleFixedPtProvFreeFixedPtVectorValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscExampleFixedPtProvFreeFixedPtVectorValue_Type.__name__ = "FixedPoint1"
_MscExampleFixedPtProvFreeFixedPtVectorValue_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtVectorValue = _MscExampleFixedPtProvFreeFixedPtVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1036, 1, 2),
    _MscExampleFixedPtProvFreeFixedPtVectorValue_Type()
)
mscExampleFixedPtProvFreeFixedPtVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtVectorValue.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtArrayTable_Object = MibTable
mscExampleFixedPtProvFreeFixedPtArrayTable = _MscExampleFixedPtProvFreeFixedPtArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1037)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtArrayTable.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtArrayEntry_Object = MibTableRow
mscExampleFixedPtProvFreeFixedPtArrayEntry = _MscExampleFixedPtProvFreeFixedPtArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1037, 1)
)
mscExampleFixedPtProvFreeFixedPtArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvFreeFixedPtArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvFreeFixedPtArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtArrayEntry.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtArrayRowIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvFreeFixedPtArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleFixedPtProvFreeFixedPtArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvFreeFixedPtArrayRowIndex_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtArrayRowIndex = _MscExampleFixedPtProvFreeFixedPtArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1037, 1, 1),
    _MscExampleFixedPtProvFreeFixedPtArrayRowIndex_Type()
)
mscExampleFixedPtProvFreeFixedPtArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtArrayRowIndex.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvFreeFixedPtArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleFixedPtProvFreeFixedPtArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvFreeFixedPtArrayColumnIndex_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtArrayColumnIndex = _MscExampleFixedPtProvFreeFixedPtArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1037, 1, 2),
    _MscExampleFixedPtProvFreeFixedPtArrayColumnIndex_Type()
)
mscExampleFixedPtProvFreeFixedPtArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtArrayColumnIndex.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtArrayValue_Type(FixedPoint2):
    """Custom type mscExampleFixedPtProvFreeFixedPtArrayValue based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25555),
    )


_MscExampleFixedPtProvFreeFixedPtArrayValue_Type.__name__ = "FixedPoint2"
_MscExampleFixedPtProvFreeFixedPtArrayValue_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtArrayValue = _MscExampleFixedPtProvFreeFixedPtArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1037, 1, 3),
    _MscExampleFixedPtProvFreeFixedPtArrayValue_Type()
)
mscExampleFixedPtProvFreeFixedPtArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtArrayValue.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtReplicatedTable_Object = MibTable
mscExampleFixedPtProvFreeFixedPtReplicatedTable = _MscExampleFixedPtProvFreeFixedPtReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1038)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtReplicatedTable.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtReplicatedEntry_Object = MibTableRow
mscExampleFixedPtProvFreeFixedPtReplicatedEntry = _MscExampleFixedPtProvFreeFixedPtReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1038, 1)
)
mscExampleFixedPtProvFreeFixedPtReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvFreeFixedPtReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtReplicatedEntry.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtReplicatedIndex_Type(Integer32):
    """Custom type mscExampleFixedPtProvFreeFixedPtReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleFixedPtProvFreeFixedPtReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleFixedPtProvFreeFixedPtReplicatedIndex_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtReplicatedIndex = _MscExampleFixedPtProvFreeFixedPtReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1038, 1, 1),
    _MscExampleFixedPtProvFreeFixedPtReplicatedIndex_Type()
)
mscExampleFixedPtProvFreeFixedPtReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtReplicatedIndex.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtReplicatedValue_Type(FixedPoint2):
    """Custom type mscExampleFixedPtProvFreeFixedPtReplicatedValue based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscExampleFixedPtProvFreeFixedPtReplicatedValue_Type.__name__ = "FixedPoint2"
_MscExampleFixedPtProvFreeFixedPtReplicatedValue_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtReplicatedValue = _MscExampleFixedPtProvFreeFixedPtReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1038, 1, 2),
    _MscExampleFixedPtProvFreeFixedPtReplicatedValue_Type()
)
mscExampleFixedPtProvFreeFixedPtReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtReplicatedValue.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Type = RowStatus
_MscExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtReplicatedRowStatus = _MscExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1038, 1, 3),
    _MscExampleFixedPtProvFreeFixedPtReplicatedRowStatus_Type()
)
mscExampleFixedPtProvFreeFixedPtReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtReplicatedRowStatus.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtListTable_Object = MibTable
mscExampleFixedPtProvFreeFixedPtListTable = _MscExampleFixedPtProvFreeFixedPtListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1039)
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtListTable.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtListEntry_Object = MibTableRow
mscExampleFixedPtProvFreeFixedPtListEntry = _MscExampleFixedPtProvFreeFixedPtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1039, 1)
)
mscExampleFixedPtProvFreeFixedPtListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFixedPtProvFreeFixedPtListValue"),
)
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtListEntry.setStatus("mandatory")


class _MscExampleFixedPtProvFreeFixedPtListValue_Type(Integer32):
    """Custom type mscExampleFixedPtProvFreeFixedPtListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_MscExampleFixedPtProvFreeFixedPtListValue_Type.__name__ = "Integer32"
_MscExampleFixedPtProvFreeFixedPtListValue_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtListValue = _MscExampleFixedPtProvFreeFixedPtListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1039, 1, 1),
    _MscExampleFixedPtProvFreeFixedPtListValue_Type()
)
mscExampleFixedPtProvFreeFixedPtListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtListValue.setStatus("mandatory")
_MscExampleFixedPtProvFreeFixedPtListRowStatus_Type = RowStatus
_MscExampleFixedPtProvFreeFixedPtListRowStatus_Object = MibTableColumn
mscExampleFixedPtProvFreeFixedPtListRowStatus = _MscExampleFixedPtProvFreeFixedPtListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 6, 1039, 1, 2),
    _MscExampleFixedPtProvFreeFixedPtListRowStatus_Type()
)
mscExampleFixedPtProvFreeFixedPtListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleFixedPtProvFreeFixedPtListRowStatus.setStatus("mandatory")
_MscExampleDashed_ObjectIdentity = ObjectIdentity
mscExampleDashed = _MscExampleDashed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7)
)
_MscExampleDashedRowStatusTable_Object = MibTable
mscExampleDashedRowStatusTable = _MscExampleDashedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1)
)
if mibBuilder.loadTexts:
    mscExampleDashedRowStatusTable.setStatus("mandatory")
_MscExampleDashedRowStatusEntry_Object = MibTableRow
mscExampleDashedRowStatusEntry = _MscExampleDashedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1, 1)
)
mscExampleDashedRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedRowStatusEntry.setStatus("mandatory")
_MscExampleDashedRowStatus_Type = RowStatus
_MscExampleDashedRowStatus_Object = MibTableColumn
mscExampleDashedRowStatus = _MscExampleDashedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1, 1, 1),
    _MscExampleDashedRowStatus_Type()
)
mscExampleDashedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedRowStatus.setStatus("mandatory")
_MscExampleDashedComponentName_Type = DisplayString
_MscExampleDashedComponentName_Object = MibTableColumn
mscExampleDashedComponentName = _MscExampleDashedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1, 1, 2),
    _MscExampleDashedComponentName_Type()
)
mscExampleDashedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDashedComponentName.setStatus("mandatory")
_MscExampleDashedStorageType_Type = StorageType
_MscExampleDashedStorageType_Object = MibTableColumn
mscExampleDashedStorageType = _MscExampleDashedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1, 1, 4),
    _MscExampleDashedStorageType_Type()
)
mscExampleDashedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDashedStorageType.setStatus("mandatory")


class _MscExampleDashedIndex_Type(DashedHexString):
    """Custom type mscExampleDashedIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedIndex_Type.__name__ = "DashedHexString"
_MscExampleDashedIndex_Object = MibTableColumn
mscExampleDashedIndex = _MscExampleDashedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1, 1, 10),
    _MscExampleDashedIndex_Type()
)
mscExampleDashedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedIndex.setStatus("mandatory")
_MscExampleDashedOperationalTable_Object = MibTable
mscExampleDashedOperationalTable = _MscExampleDashedOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 10)
)
if mibBuilder.loadTexts:
    mscExampleDashedOperationalTable.setStatus("mandatory")
_MscExampleDashedOperationalEntry_Object = MibTableRow
mscExampleDashedOperationalEntry = _MscExampleDashedOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 10, 1)
)
mscExampleDashedOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOperationalEntry.setStatus("mandatory")


class _MscExampleDashedOperStructDashed_Type(DashedHexString):
    """Custom type mscExampleDashedOperStructDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedOperStructDashed_Type.__name__ = "DashedHexString"
_MscExampleDashedOperStructDashed_Object = MibTableColumn
mscExampleDashedOperStructDashed = _MscExampleDashedOperStructDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 10, 1, 1),
    _MscExampleDashedOperStructDashed_Type()
)
mscExampleDashedOperStructDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOperStructDashed.setStatus("mandatory")


class _MscExampleDashedOperFreeDashed_Type(DashedHexString):
    """Custom type mscExampleDashedOperFreeDashed based on DashedHexString"""
    defaultHexValue = "123456"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedOperFreeDashed_Type.__name__ = "DashedHexString"
_MscExampleDashedOperFreeDashed_Object = MibTableColumn
mscExampleDashedOperFreeDashed = _MscExampleDashedOperFreeDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 10, 1, 2),
    _MscExampleDashedOperFreeDashed_Type()
)
mscExampleDashedOperFreeDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOperFreeDashed.setStatus("mandatory")
_MscExampleDashedProvisionalTable_Object = MibTable
mscExampleDashedProvisionalTable = _MscExampleDashedProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 11)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvisionalTable.setStatus("mandatory")
_MscExampleDashedProvisionalEntry_Object = MibTableRow
mscExampleDashedProvisionalEntry = _MscExampleDashedProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 11, 1)
)
mscExampleDashedProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvisionalEntry.setStatus("mandatory")


class _MscExampleDashedProvStructDashed_Type(DashedHexString):
    """Custom type mscExampleDashedProvStructDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedProvStructDashed_Type.__name__ = "DashedHexString"
_MscExampleDashedProvStructDashed_Object = MibTableColumn
mscExampleDashedProvStructDashed = _MscExampleDashedProvStructDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 11, 1, 1),
    _MscExampleDashedProvStructDashed_Type()
)
mscExampleDashedProvStructDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashed.setStatus("mandatory")


class _MscExampleDashedProvFreeDashed_Type(DashedHexString):
    """Custom type mscExampleDashedProvFreeDashed based on DashedHexString"""
    defaultHexValue = "123456"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedProvFreeDashed_Type.__name__ = "DashedHexString"
_MscExampleDashedProvFreeDashed_Object = MibTableColumn
mscExampleDashedProvFreeDashed = _MscExampleDashedProvFreeDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 11, 1, 2),
    _MscExampleDashedProvFreeDashed_Type()
)
mscExampleDashedProvFreeDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashed.setStatus("mandatory")
_MscExampleDashedOsDashedArrayTable_Object = MibTable
mscExampleDashedOsDashedArrayTable = _MscExampleDashedOsDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1088)
)
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedArrayTable.setStatus("mandatory")
_MscExampleDashedOsDashedArrayEntry_Object = MibTableRow
mscExampleDashedOsDashedArrayEntry = _MscExampleDashedOsDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1088, 1)
)
mscExampleDashedOsDashedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOsDashedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOsDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedArrayEntry.setStatus("mandatory")


class _MscExampleDashedOsDashedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDashedOsDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDashedOsDashedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDashedOsDashedArrayRowIndex_Object = MibTableColumn
mscExampleDashedOsDashedArrayRowIndex = _MscExampleDashedOsDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1088, 1, 1),
    _MscExampleDashedOsDashedArrayRowIndex_Type()
)
mscExampleDashedOsDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedArrayRowIndex.setStatus("mandatory")


class _MscExampleDashedOsDashedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDashedOsDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDashedOsDashedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDashedOsDashedArrayColumnIndex_Object = MibTableColumn
mscExampleDashedOsDashedArrayColumnIndex = _MscExampleDashedOsDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1088, 1, 2),
    _MscExampleDashedOsDashedArrayColumnIndex_Type()
)
mscExampleDashedOsDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedArrayColumnIndex.setStatus("mandatory")


class _MscExampleDashedOsDashedArrayValue_Type(DashedHexString):
    """Custom type mscExampleDashedOsDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedOsDashedArrayValue_Type.__name__ = "DashedHexString"
_MscExampleDashedOsDashedArrayValue_Object = MibTableColumn
mscExampleDashedOsDashedArrayValue = _MscExampleDashedOsDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1088, 1, 3),
    _MscExampleDashedOsDashedArrayValue_Type()
)
mscExampleDashedOsDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedArrayValue.setStatus("mandatory")
_MscExampleDashedOsDashedVectorTable_Object = MibTable
mscExampleDashedOsDashedVectorTable = _MscExampleDashedOsDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1089)
)
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedVectorTable.setStatus("mandatory")
_MscExampleDashedOsDashedVectorEntry_Object = MibTableRow
mscExampleDashedOsDashedVectorEntry = _MscExampleDashedOsDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1089, 1)
)
mscExampleDashedOsDashedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOsDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedVectorEntry.setStatus("mandatory")


class _MscExampleDashedOsDashedVectorIndex_Type(Integer32):
    """Custom type mscExampleDashedOsDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDashedOsDashedVectorIndex_Type.__name__ = "Integer32"
_MscExampleDashedOsDashedVectorIndex_Object = MibTableColumn
mscExampleDashedOsDashedVectorIndex = _MscExampleDashedOsDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1089, 1, 1),
    _MscExampleDashedOsDashedVectorIndex_Type()
)
mscExampleDashedOsDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedVectorIndex.setStatus("mandatory")


class _MscExampleDashedOsDashedVectorValue_Type(DashedHexString):
    """Custom type mscExampleDashedOsDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedOsDashedVectorValue_Type.__name__ = "DashedHexString"
_MscExampleDashedOsDashedVectorValue_Object = MibTableColumn
mscExampleDashedOsDashedVectorValue = _MscExampleDashedOsDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1089, 1, 2),
    _MscExampleDashedOsDashedVectorValue_Type()
)
mscExampleDashedOsDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOsDashedVectorValue.setStatus("mandatory")
_MscExampleDashedOfDashedListTable_Object = MibTable
mscExampleDashedOfDashedListTable = _MscExampleDashedOfDashedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1090)
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedListTable.setStatus("mandatory")
_MscExampleDashedOfDashedListEntry_Object = MibTableRow
mscExampleDashedOfDashedListEntry = _MscExampleDashedOfDashedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1090, 1)
)
mscExampleDashedOfDashedListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOfDashedListValue"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedListEntry.setStatus("mandatory")


class _MscExampleDashedOfDashedListValue_Type(DashedHexString):
    """Custom type mscExampleDashedOfDashedListValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedOfDashedListValue_Type.__name__ = "DashedHexString"
_MscExampleDashedOfDashedListValue_Object = MibTableColumn
mscExampleDashedOfDashedListValue = _MscExampleDashedOfDashedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1090, 1, 1),
    _MscExampleDashedOfDashedListValue_Type()
)
mscExampleDashedOfDashedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedListValue.setStatus("mandatory")
_MscExampleDashedOfDashedListRowStatus_Type = RowStatus
_MscExampleDashedOfDashedListRowStatus_Object = MibTableColumn
mscExampleDashedOfDashedListRowStatus = _MscExampleDashedOfDashedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1090, 1, 2),
    _MscExampleDashedOfDashedListRowStatus_Type()
)
mscExampleDashedOfDashedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedListRowStatus.setStatus("mandatory")
_MscExampleDashedOfDashedReplicatedTable_Object = MibTable
mscExampleDashedOfDashedReplicatedTable = _MscExampleDashedOfDashedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1091)
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedReplicatedTable.setStatus("mandatory")
_MscExampleDashedOfDashedReplicatedEntry_Object = MibTableRow
mscExampleDashedOfDashedReplicatedEntry = _MscExampleDashedOfDashedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1091, 1)
)
mscExampleDashedOfDashedReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOfDashedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedReplicatedEntry.setStatus("mandatory")


class _MscExampleDashedOfDashedReplicatedIndex_Type(DashedHexString):
    """Custom type mscExampleDashedOfDashedReplicatedIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedOfDashedReplicatedIndex_Type.__name__ = "DashedHexString"
_MscExampleDashedOfDashedReplicatedIndex_Object = MibTableColumn
mscExampleDashedOfDashedReplicatedIndex = _MscExampleDashedOfDashedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1091, 1, 1),
    _MscExampleDashedOfDashedReplicatedIndex_Type()
)
mscExampleDashedOfDashedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedReplicatedIndex.setStatus("mandatory")


class _MscExampleDashedOfDashedReplicatedValue_Type(DashedHexString):
    """Custom type mscExampleDashedOfDashedReplicatedValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedOfDashedReplicatedValue_Type.__name__ = "DashedHexString"
_MscExampleDashedOfDashedReplicatedValue_Object = MibTableColumn
mscExampleDashedOfDashedReplicatedValue = _MscExampleDashedOfDashedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1091, 1, 2),
    _MscExampleDashedOfDashedReplicatedValue_Type()
)
mscExampleDashedOfDashedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedReplicatedValue.setStatus("mandatory")
_MscExampleDashedOfDashedReplicatedRowStatus_Type = RowStatus
_MscExampleDashedOfDashedReplicatedRowStatus_Object = MibTableColumn
mscExampleDashedOfDashedReplicatedRowStatus = _MscExampleDashedOfDashedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1091, 1, 3),
    _MscExampleDashedOfDashedReplicatedRowStatus_Type()
)
mscExampleDashedOfDashedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedReplicatedRowStatus.setStatus("mandatory")
_MscExampleDashedOfDashedArrayTable_Object = MibTable
mscExampleDashedOfDashedArrayTable = _MscExampleDashedOfDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1092)
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedArrayTable.setStatus("mandatory")
_MscExampleDashedOfDashedArrayEntry_Object = MibTableRow
mscExampleDashedOfDashedArrayEntry = _MscExampleDashedOfDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1092, 1)
)
mscExampleDashedOfDashedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOfDashedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOfDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedArrayEntry.setStatus("mandatory")


class _MscExampleDashedOfDashedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDashedOfDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDashedOfDashedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDashedOfDashedArrayRowIndex_Object = MibTableColumn
mscExampleDashedOfDashedArrayRowIndex = _MscExampleDashedOfDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1092, 1, 1),
    _MscExampleDashedOfDashedArrayRowIndex_Type()
)
mscExampleDashedOfDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedArrayRowIndex.setStatus("mandatory")


class _MscExampleDashedOfDashedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDashedOfDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDashedOfDashedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDashedOfDashedArrayColumnIndex_Object = MibTableColumn
mscExampleDashedOfDashedArrayColumnIndex = _MscExampleDashedOfDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1092, 1, 2),
    _MscExampleDashedOfDashedArrayColumnIndex_Type()
)
mscExampleDashedOfDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedArrayColumnIndex.setStatus("mandatory")


class _MscExampleDashedOfDashedArrayValue_Type(DashedHexString):
    """Custom type mscExampleDashedOfDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedOfDashedArrayValue_Type.__name__ = "DashedHexString"
_MscExampleDashedOfDashedArrayValue_Object = MibTableColumn
mscExampleDashedOfDashedArrayValue = _MscExampleDashedOfDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1092, 1, 3),
    _MscExampleDashedOfDashedArrayValue_Type()
)
mscExampleDashedOfDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedArrayValue.setStatus("mandatory")
_MscExampleDashedOfDashedVectorTable_Object = MibTable
mscExampleDashedOfDashedVectorTable = _MscExampleDashedOfDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1093)
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedVectorTable.setStatus("mandatory")
_MscExampleDashedOfDashedVectorEntry_Object = MibTableRow
mscExampleDashedOfDashedVectorEntry = _MscExampleDashedOfDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1093, 1)
)
mscExampleDashedOfDashedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedOfDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedVectorEntry.setStatus("mandatory")


class _MscExampleDashedOfDashedVectorIndex_Type(Integer32):
    """Custom type mscExampleDashedOfDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDashedOfDashedVectorIndex_Type.__name__ = "Integer32"
_MscExampleDashedOfDashedVectorIndex_Object = MibTableColumn
mscExampleDashedOfDashedVectorIndex = _MscExampleDashedOfDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1093, 1, 1),
    _MscExampleDashedOfDashedVectorIndex_Type()
)
mscExampleDashedOfDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedVectorIndex.setStatus("mandatory")


class _MscExampleDashedOfDashedVectorValue_Type(DashedHexString):
    """Custom type mscExampleDashedOfDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedOfDashedVectorValue_Type.__name__ = "DashedHexString"
_MscExampleDashedOfDashedVectorValue_Object = MibTableColumn
mscExampleDashedOfDashedVectorValue = _MscExampleDashedOfDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1093, 1, 2),
    _MscExampleDashedOfDashedVectorValue_Type()
)
mscExampleDashedOfDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedOfDashedVectorValue.setStatus("mandatory")
_MscExampleDashedProvStructDashedArrayTable_Object = MibTable
mscExampleDashedProvStructDashedArrayTable = _MscExampleDashedProvStructDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1094)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedArrayTable.setStatus("mandatory")
_MscExampleDashedProvStructDashedArrayEntry_Object = MibTableRow
mscExampleDashedProvStructDashedArrayEntry = _MscExampleDashedProvStructDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1094, 1)
)
mscExampleDashedProvStructDashedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvStructDashedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvStructDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedArrayEntry.setStatus("mandatory")


class _MscExampleDashedProvStructDashedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDashedProvStructDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDashedProvStructDashedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDashedProvStructDashedArrayRowIndex_Object = MibTableColumn
mscExampleDashedProvStructDashedArrayRowIndex = _MscExampleDashedProvStructDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1094, 1, 1),
    _MscExampleDashedProvStructDashedArrayRowIndex_Type()
)
mscExampleDashedProvStructDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedArrayRowIndex.setStatus("mandatory")


class _MscExampleDashedProvStructDashedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDashedProvStructDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDashedProvStructDashedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDashedProvStructDashedArrayColumnIndex_Object = MibTableColumn
mscExampleDashedProvStructDashedArrayColumnIndex = _MscExampleDashedProvStructDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1094, 1, 2),
    _MscExampleDashedProvStructDashedArrayColumnIndex_Type()
)
mscExampleDashedProvStructDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedArrayColumnIndex.setStatus("mandatory")


class _MscExampleDashedProvStructDashedArrayValue_Type(DashedHexString):
    """Custom type mscExampleDashedProvStructDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleDashedProvStructDashedArrayValue_Type.__name__ = "DashedHexString"
_MscExampleDashedProvStructDashedArrayValue_Object = MibTableColumn
mscExampleDashedProvStructDashedArrayValue = _MscExampleDashedProvStructDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1094, 1, 3),
    _MscExampleDashedProvStructDashedArrayValue_Type()
)
mscExampleDashedProvStructDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedArrayValue.setStatus("mandatory")
_MscExampleDashedProvStructDashedVectorTable_Object = MibTable
mscExampleDashedProvStructDashedVectorTable = _MscExampleDashedProvStructDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1095)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedVectorTable.setStatus("mandatory")
_MscExampleDashedProvStructDashedVectorEntry_Object = MibTableRow
mscExampleDashedProvStructDashedVectorEntry = _MscExampleDashedProvStructDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1095, 1)
)
mscExampleDashedProvStructDashedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvStructDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedVectorEntry.setStatus("mandatory")


class _MscExampleDashedProvStructDashedVectorIndex_Type(Integer32):
    """Custom type mscExampleDashedProvStructDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDashedProvStructDashedVectorIndex_Type.__name__ = "Integer32"
_MscExampleDashedProvStructDashedVectorIndex_Object = MibTableColumn
mscExampleDashedProvStructDashedVectorIndex = _MscExampleDashedProvStructDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1095, 1, 1),
    _MscExampleDashedProvStructDashedVectorIndex_Type()
)
mscExampleDashedProvStructDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedVectorIndex.setStatus("mandatory")


class _MscExampleDashedProvStructDashedVectorValue_Type(DashedHexString):
    """Custom type mscExampleDashedProvStructDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleDashedProvStructDashedVectorValue_Type.__name__ = "DashedHexString"
_MscExampleDashedProvStructDashedVectorValue_Object = MibTableColumn
mscExampleDashedProvStructDashedVectorValue = _MscExampleDashedProvStructDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1095, 1, 2),
    _MscExampleDashedProvStructDashedVectorValue_Type()
)
mscExampleDashedProvStructDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvStructDashedVectorValue.setStatus("mandatory")
_MscExampleDashedProvFreeDashedListTable_Object = MibTable
mscExampleDashedProvFreeDashedListTable = _MscExampleDashedProvFreeDashedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1096)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedListTable.setStatus("mandatory")
_MscExampleDashedProvFreeDashedListEntry_Object = MibTableRow
mscExampleDashedProvFreeDashedListEntry = _MscExampleDashedProvFreeDashedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1096, 1)
)
mscExampleDashedProvFreeDashedListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvFreeDashedListValue"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedListEntry.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedListValue_Type(DashedHexString):
    """Custom type mscExampleDashedProvFreeDashedListValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedProvFreeDashedListValue_Type.__name__ = "DashedHexString"
_MscExampleDashedProvFreeDashedListValue_Object = MibTableColumn
mscExampleDashedProvFreeDashedListValue = _MscExampleDashedProvFreeDashedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1096, 1, 1),
    _MscExampleDashedProvFreeDashedListValue_Type()
)
mscExampleDashedProvFreeDashedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedListValue.setStatus("mandatory")
_MscExampleDashedProvFreeDashedListRowStatus_Type = RowStatus
_MscExampleDashedProvFreeDashedListRowStatus_Object = MibTableColumn
mscExampleDashedProvFreeDashedListRowStatus = _MscExampleDashedProvFreeDashedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1096, 1, 2),
    _MscExampleDashedProvFreeDashedListRowStatus_Type()
)
mscExampleDashedProvFreeDashedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedListRowStatus.setStatus("mandatory")
_MscExampleDashedProvFreeDashedReplicatedTable_Object = MibTable
mscExampleDashedProvFreeDashedReplicatedTable = _MscExampleDashedProvFreeDashedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1097)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedReplicatedTable.setStatus("mandatory")
_MscExampleDashedProvFreeDashedReplicatedEntry_Object = MibTableRow
mscExampleDashedProvFreeDashedReplicatedEntry = _MscExampleDashedProvFreeDashedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1097, 1)
)
mscExampleDashedProvFreeDashedReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvFreeDashedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedReplicatedEntry.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedReplicatedIndex_Type(DashedHexString):
    """Custom type mscExampleDashedProvFreeDashedReplicatedIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleDashedProvFreeDashedReplicatedIndex_Type.__name__ = "DashedHexString"
_MscExampleDashedProvFreeDashedReplicatedIndex_Object = MibTableColumn
mscExampleDashedProvFreeDashedReplicatedIndex = _MscExampleDashedProvFreeDashedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1097, 1, 1),
    _MscExampleDashedProvFreeDashedReplicatedIndex_Type()
)
mscExampleDashedProvFreeDashedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedReplicatedIndex.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedReplicatedValue_Type(DashedHexString):
    """Custom type mscExampleDashedProvFreeDashedReplicatedValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedProvFreeDashedReplicatedValue_Type.__name__ = "DashedHexString"
_MscExampleDashedProvFreeDashedReplicatedValue_Object = MibTableColumn
mscExampleDashedProvFreeDashedReplicatedValue = _MscExampleDashedProvFreeDashedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1097, 1, 2),
    _MscExampleDashedProvFreeDashedReplicatedValue_Type()
)
mscExampleDashedProvFreeDashedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedReplicatedValue.setStatus("mandatory")
_MscExampleDashedProvFreeDashedReplicatedRowStatus_Type = RowStatus
_MscExampleDashedProvFreeDashedReplicatedRowStatus_Object = MibTableColumn
mscExampleDashedProvFreeDashedReplicatedRowStatus = _MscExampleDashedProvFreeDashedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1097, 1, 3),
    _MscExampleDashedProvFreeDashedReplicatedRowStatus_Type()
)
mscExampleDashedProvFreeDashedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedReplicatedRowStatus.setStatus("mandatory")
_MscExampleDashedProvFreeDashedArrayTable_Object = MibTable
mscExampleDashedProvFreeDashedArrayTable = _MscExampleDashedProvFreeDashedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1098)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedArrayTable.setStatus("mandatory")
_MscExampleDashedProvFreeDashedArrayEntry_Object = MibTableRow
mscExampleDashedProvFreeDashedArrayEntry = _MscExampleDashedProvFreeDashedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1098, 1)
)
mscExampleDashedProvFreeDashedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvFreeDashedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvFreeDashedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedArrayEntry.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleDashedProvFreeDashedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleDashedProvFreeDashedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleDashedProvFreeDashedArrayRowIndex_Object = MibTableColumn
mscExampleDashedProvFreeDashedArrayRowIndex = _MscExampleDashedProvFreeDashedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1098, 1, 1),
    _MscExampleDashedProvFreeDashedArrayRowIndex_Type()
)
mscExampleDashedProvFreeDashedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedArrayRowIndex.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleDashedProvFreeDashedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleDashedProvFreeDashedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleDashedProvFreeDashedArrayColumnIndex_Object = MibTableColumn
mscExampleDashedProvFreeDashedArrayColumnIndex = _MscExampleDashedProvFreeDashedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1098, 1, 2),
    _MscExampleDashedProvFreeDashedArrayColumnIndex_Type()
)
mscExampleDashedProvFreeDashedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedArrayColumnIndex.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedArrayValue_Type(DashedHexString):
    """Custom type mscExampleDashedProvFreeDashedArrayValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleDashedProvFreeDashedArrayValue_Type.__name__ = "DashedHexString"
_MscExampleDashedProvFreeDashedArrayValue_Object = MibTableColumn
mscExampleDashedProvFreeDashedArrayValue = _MscExampleDashedProvFreeDashedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1098, 1, 3),
    _MscExampleDashedProvFreeDashedArrayValue_Type()
)
mscExampleDashedProvFreeDashedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedArrayValue.setStatus("mandatory")
_MscExampleDashedProvFreeDashedVectorTable_Object = MibTable
mscExampleDashedProvFreeDashedVectorTable = _MscExampleDashedProvFreeDashedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1099)
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedVectorTable.setStatus("mandatory")
_MscExampleDashedProvFreeDashedVectorEntry_Object = MibTableRow
mscExampleDashedProvFreeDashedVectorEntry = _MscExampleDashedProvFreeDashedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1099, 1)
)
mscExampleDashedProvFreeDashedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedProvFreeDashedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedVectorEntry.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedVectorIndex_Type(Integer32):
    """Custom type mscExampleDashedProvFreeDashedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleDashedProvFreeDashedVectorIndex_Type.__name__ = "Integer32"
_MscExampleDashedProvFreeDashedVectorIndex_Object = MibTableColumn
mscExampleDashedProvFreeDashedVectorIndex = _MscExampleDashedProvFreeDashedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1099, 1, 1),
    _MscExampleDashedProvFreeDashedVectorIndex_Type()
)
mscExampleDashedProvFreeDashedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedVectorIndex.setStatus("mandatory")


class _MscExampleDashedProvFreeDashedVectorValue_Type(DashedHexString):
    """Custom type mscExampleDashedProvFreeDashedVectorValue based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleDashedProvFreeDashedVectorValue_Type.__name__ = "DashedHexString"
_MscExampleDashedProvFreeDashedVectorValue_Object = MibTableColumn
mscExampleDashedProvFreeDashedVectorValue = _MscExampleDashedProvFreeDashedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 7, 1099, 1, 2),
    _MscExampleDashedProvFreeDashedVectorValue_Type()
)
mscExampleDashedProvFreeDashedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedProvFreeDashedVectorValue.setStatus("mandatory")
_MscExampleExtended_ObjectIdentity = ObjectIdentity
mscExampleExtended = _MscExampleExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8)
)
_MscExampleExtendedRowStatusTable_Object = MibTable
mscExampleExtendedRowStatusTable = _MscExampleExtendedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1)
)
if mibBuilder.loadTexts:
    mscExampleExtendedRowStatusTable.setStatus("mandatory")
_MscExampleExtendedRowStatusEntry_Object = MibTableRow
mscExampleExtendedRowStatusEntry = _MscExampleExtendedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1, 1)
)
mscExampleExtendedRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedRowStatusEntry.setStatus("mandatory")
_MscExampleExtendedRowStatus_Type = RowStatus
_MscExampleExtendedRowStatus_Object = MibTableColumn
mscExampleExtendedRowStatus = _MscExampleExtendedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1, 1, 1),
    _MscExampleExtendedRowStatus_Type()
)
mscExampleExtendedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedRowStatus.setStatus("mandatory")
_MscExampleExtendedComponentName_Type = DisplayString
_MscExampleExtendedComponentName_Object = MibTableColumn
mscExampleExtendedComponentName = _MscExampleExtendedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1, 1, 2),
    _MscExampleExtendedComponentName_Type()
)
mscExampleExtendedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleExtendedComponentName.setStatus("mandatory")
_MscExampleExtendedStorageType_Type = StorageType
_MscExampleExtendedStorageType_Object = MibTableColumn
mscExampleExtendedStorageType = _MscExampleExtendedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1, 1, 4),
    _MscExampleExtendedStorageType_Type()
)
mscExampleExtendedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleExtendedStorageType.setStatus("mandatory")
_MscExampleExtendedIndex_Type = NonReplicated
_MscExampleExtendedIndex_Object = MibTableColumn
mscExampleExtendedIndex = _MscExampleExtendedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1, 1, 10),
    _MscExampleExtendedIndex_Type()
)
mscExampleExtendedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedIndex.setStatus("mandatory")
_MscExampleExtendedOperationalTable_Object = MibTable
mscExampleExtendedOperationalTable = _MscExampleExtendedOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 10)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperationalTable.setStatus("mandatory")
_MscExampleExtendedOperationalEntry_Object = MibTableRow
mscExampleExtendedOperationalEntry = _MscExampleExtendedOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 10, 1)
)
mscExampleExtendedOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperationalEntry.setStatus("mandatory")


class _MscExampleExtendedOperStructExtended_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperStructExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleExtendedOperStructExtended_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperStructExtended_Object = MibTableColumn
mscExampleExtendedOperStructExtended = _MscExampleExtendedOperStructExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 10, 1, 1),
    _MscExampleExtendedOperStructExtended_Type()
)
mscExampleExtendedOperStructExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtended.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtended_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperFreeExtended based on ExtendedAsciiString"""
    defaultHexValue = "68656c6c6f5c6162"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleExtendedOperFreeExtended_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperFreeExtended_Object = MibTableColumn
mscExampleExtendedOperFreeExtended = _MscExampleExtendedOperFreeExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 10, 1, 2),
    _MscExampleExtendedOperFreeExtended_Type()
)
mscExampleExtendedOperFreeExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtended.setStatus("mandatory")
_MscExampleExtendedProvisionalTable_Object = MibTable
mscExampleExtendedProvisionalTable = _MscExampleExtendedProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 11)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvisionalTable.setStatus("mandatory")
_MscExampleExtendedProvisionalEntry_Object = MibTableRow
mscExampleExtendedProvisionalEntry = _MscExampleExtendedProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 11, 1)
)
mscExampleExtendedProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvisionalEntry.setStatus("mandatory")
_MscExampleExtendedProvEnumSub_Type = Link
_MscExampleExtendedProvEnumSub_Object = MibTableColumn
mscExampleExtendedProvEnumSub = _MscExampleExtendedProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 11, 1, 1),
    _MscExampleExtendedProvEnumSub_Type()
)
mscExampleExtendedProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvEnumSub.setStatus("mandatory")


class _MscExampleExtendedProvStructExtended_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvStructExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleExtendedProvStructExtended_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvStructExtended_Object = MibTableColumn
mscExampleExtendedProvStructExtended = _MscExampleExtendedProvStructExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 11, 1, 2),
    _MscExampleExtendedProvStructExtended_Type()
)
mscExampleExtendedProvStructExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtended.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtended_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvFreeExtended based on ExtendedAsciiString"""
    defaultHexValue = "48656c6c6f5c61626364"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleExtendedProvFreeExtended_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvFreeExtended_Object = MibTableColumn
mscExampleExtendedProvFreeExtended = _MscExampleExtendedProvFreeExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 11, 1, 3),
    _MscExampleExtendedProvFreeExtended_Type()
)
mscExampleExtendedProvFreeExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtended.setStatus("mandatory")
_MscExampleExtendedOperStructExtendedArrayTable_Object = MibTable
mscExampleExtendedOperStructExtendedArrayTable = _MscExampleExtendedOperStructExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1100)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedArrayTable.setStatus("mandatory")
_MscExampleExtendedOperStructExtendedArrayEntry_Object = MibTableRow
mscExampleExtendedOperStructExtendedArrayEntry = _MscExampleExtendedOperStructExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1100, 1)
)
mscExampleExtendedOperStructExtendedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperStructExtendedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperStructExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedArrayEntry.setStatus("mandatory")


class _MscExampleExtendedOperStructExtendedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleExtendedOperStructExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleExtendedOperStructExtendedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleExtendedOperStructExtendedArrayRowIndex_Object = MibTableColumn
mscExampleExtendedOperStructExtendedArrayRowIndex = _MscExampleExtendedOperStructExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1100, 1, 1),
    _MscExampleExtendedOperStructExtendedArrayRowIndex_Type()
)
mscExampleExtendedOperStructExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedArrayRowIndex.setStatus("mandatory")


class _MscExampleExtendedOperStructExtendedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleExtendedOperStructExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleExtendedOperStructExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleExtendedOperStructExtendedArrayColumnIndex_Object = MibTableColumn
mscExampleExtendedOperStructExtendedArrayColumnIndex = _MscExampleExtendedOperStructExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1100, 1, 2),
    _MscExampleExtendedOperStructExtendedArrayColumnIndex_Type()
)
mscExampleExtendedOperStructExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedArrayColumnIndex.setStatus("mandatory")


class _MscExampleExtendedOperStructExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperStructExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedOperStructExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperStructExtendedArrayValue_Object = MibTableColumn
mscExampleExtendedOperStructExtendedArrayValue = _MscExampleExtendedOperStructExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1100, 1, 3),
    _MscExampleExtendedOperStructExtendedArrayValue_Type()
)
mscExampleExtendedOperStructExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedArrayValue.setStatus("mandatory")
_MscExampleExtendedOperStructExtendedVectorTable_Object = MibTable
mscExampleExtendedOperStructExtendedVectorTable = _MscExampleExtendedOperStructExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1101)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedVectorTable.setStatus("mandatory")
_MscExampleExtendedOperStructExtendedVectorEntry_Object = MibTableRow
mscExampleExtendedOperStructExtendedVectorEntry = _MscExampleExtendedOperStructExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1101, 1)
)
mscExampleExtendedOperStructExtendedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperStructExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedVectorEntry.setStatus("mandatory")


class _MscExampleExtendedOperStructExtendedVectorIndex_Type(Integer32):
    """Custom type mscExampleExtendedOperStructExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleExtendedOperStructExtendedVectorIndex_Type.__name__ = "Integer32"
_MscExampleExtendedOperStructExtendedVectorIndex_Object = MibTableColumn
mscExampleExtendedOperStructExtendedVectorIndex = _MscExampleExtendedOperStructExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1101, 1, 1),
    _MscExampleExtendedOperStructExtendedVectorIndex_Type()
)
mscExampleExtendedOperStructExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedVectorIndex.setStatus("mandatory")


class _MscExampleExtendedOperStructExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperStructExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedOperStructExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperStructExtendedVectorValue_Object = MibTableColumn
mscExampleExtendedOperStructExtendedVectorValue = _MscExampleExtendedOperStructExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1101, 1, 2),
    _MscExampleExtendedOperStructExtendedVectorValue_Type()
)
mscExampleExtendedOperStructExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperStructExtendedVectorValue.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedListTable_Object = MibTable
mscExampleExtendedOperFreeExtendedListTable = _MscExampleExtendedOperFreeExtendedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1102)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedListTable.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedListEntry_Object = MibTableRow
mscExampleExtendedOperFreeExtendedListEntry = _MscExampleExtendedOperFreeExtendedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1102, 1)
)
mscExampleExtendedOperFreeExtendedListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperFreeExtendedListValue"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedListEntry.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedListValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperFreeExtendedListValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedOperFreeExtendedListValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperFreeExtendedListValue_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedListValue = _MscExampleExtendedOperFreeExtendedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1102, 1, 1),
    _MscExampleExtendedOperFreeExtendedListValue_Type()
)
mscExampleExtendedOperFreeExtendedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedListValue.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedListRowStatus_Type = RowStatus
_MscExampleExtendedOperFreeExtendedListRowStatus_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedListRowStatus = _MscExampleExtendedOperFreeExtendedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1102, 1, 2),
    _MscExampleExtendedOperFreeExtendedListRowStatus_Type()
)
mscExampleExtendedOperFreeExtendedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedListRowStatus.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedReplicatedTable_Object = MibTable
mscExampleExtendedOperFreeExtendedReplicatedTable = _MscExampleExtendedOperFreeExtendedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1103)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedReplicatedTable.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedReplicatedEntry_Object = MibTableRow
mscExampleExtendedOperFreeExtendedReplicatedEntry = _MscExampleExtendedOperFreeExtendedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1103, 1)
)
mscExampleExtendedOperFreeExtendedReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperFreeExtendedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedReplicatedEntry.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedReplicatedIndex_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperFreeExtendedReplicatedIndex based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedOperFreeExtendedReplicatedIndex_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperFreeExtendedReplicatedIndex_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedReplicatedIndex = _MscExampleExtendedOperFreeExtendedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1103, 1, 1),
    _MscExampleExtendedOperFreeExtendedReplicatedIndex_Type()
)
mscExampleExtendedOperFreeExtendedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedReplicatedIndex.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedReplicatedValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperFreeExtendedReplicatedValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleExtendedOperFreeExtendedReplicatedValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperFreeExtendedReplicatedValue_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedReplicatedValue = _MscExampleExtendedOperFreeExtendedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1103, 1, 2),
    _MscExampleExtendedOperFreeExtendedReplicatedValue_Type()
)
mscExampleExtendedOperFreeExtendedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedReplicatedValue.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedReplicatedRowStatus_Type = RowStatus
_MscExampleExtendedOperFreeExtendedReplicatedRowStatus_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedReplicatedRowStatus = _MscExampleExtendedOperFreeExtendedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1103, 1, 3),
    _MscExampleExtendedOperFreeExtendedReplicatedRowStatus_Type()
)
mscExampleExtendedOperFreeExtendedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedReplicatedRowStatus.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedArrayTable_Object = MibTable
mscExampleExtendedOperFreeExtendedArrayTable = _MscExampleExtendedOperFreeExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1104)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedArrayTable.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedArrayEntry_Object = MibTableRow
mscExampleExtendedOperFreeExtendedArrayEntry = _MscExampleExtendedOperFreeExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1104, 1)
)
mscExampleExtendedOperFreeExtendedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperFreeExtendedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperFreeExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedArrayEntry.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleExtendedOperFreeExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleExtendedOperFreeExtendedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleExtendedOperFreeExtendedArrayRowIndex_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedArrayRowIndex = _MscExampleExtendedOperFreeExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1104, 1, 1),
    _MscExampleExtendedOperFreeExtendedArrayRowIndex_Type()
)
mscExampleExtendedOperFreeExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedArrayRowIndex.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleExtendedOperFreeExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleExtendedOperFreeExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleExtendedOperFreeExtendedArrayColumnIndex_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedArrayColumnIndex = _MscExampleExtendedOperFreeExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1104, 1, 2),
    _MscExampleExtendedOperFreeExtendedArrayColumnIndex_Type()
)
mscExampleExtendedOperFreeExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedArrayColumnIndex.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperFreeExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedOperFreeExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperFreeExtendedArrayValue_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedArrayValue = _MscExampleExtendedOperFreeExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1104, 1, 3),
    _MscExampleExtendedOperFreeExtendedArrayValue_Type()
)
mscExampleExtendedOperFreeExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedArrayValue.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedVectorTable_Object = MibTable
mscExampleExtendedOperFreeExtendedVectorTable = _MscExampleExtendedOperFreeExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1105)
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedVectorTable.setStatus("mandatory")
_MscExampleExtendedOperFreeExtendedVectorEntry_Object = MibTableRow
mscExampleExtendedOperFreeExtendedVectorEntry = _MscExampleExtendedOperFreeExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1105, 1)
)
mscExampleExtendedOperFreeExtendedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedOperFreeExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedVectorEntry.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedVectorIndex_Type(Integer32):
    """Custom type mscExampleExtendedOperFreeExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleExtendedOperFreeExtendedVectorIndex_Type.__name__ = "Integer32"
_MscExampleExtendedOperFreeExtendedVectorIndex_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedVectorIndex = _MscExampleExtendedOperFreeExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1105, 1, 1),
    _MscExampleExtendedOperFreeExtendedVectorIndex_Type()
)
mscExampleExtendedOperFreeExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedVectorIndex.setStatus("mandatory")


class _MscExampleExtendedOperFreeExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedOperFreeExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedOperFreeExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedOperFreeExtendedVectorValue_Object = MibTableColumn
mscExampleExtendedOperFreeExtendedVectorValue = _MscExampleExtendedOperFreeExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1105, 1, 2),
    _MscExampleExtendedOperFreeExtendedVectorValue_Type()
)
mscExampleExtendedOperFreeExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedOperFreeExtendedVectorValue.setStatus("mandatory")
_MscExampleExtendedProvStructExtendedArrayTable_Object = MibTable
mscExampleExtendedProvStructExtendedArrayTable = _MscExampleExtendedProvStructExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1106)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedArrayTable.setStatus("mandatory")
_MscExampleExtendedProvStructExtendedArrayEntry_Object = MibTableRow
mscExampleExtendedProvStructExtendedArrayEntry = _MscExampleExtendedProvStructExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1106, 1)
)
mscExampleExtendedProvStructExtendedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvStructExtendedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvStructExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedArrayEntry.setStatus("mandatory")


class _MscExampleExtendedProvStructExtendedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleExtendedProvStructExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleExtendedProvStructExtendedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleExtendedProvStructExtendedArrayRowIndex_Object = MibTableColumn
mscExampleExtendedProvStructExtendedArrayRowIndex = _MscExampleExtendedProvStructExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1106, 1, 1),
    _MscExampleExtendedProvStructExtendedArrayRowIndex_Type()
)
mscExampleExtendedProvStructExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedArrayRowIndex.setStatus("mandatory")


class _MscExampleExtendedProvStructExtendedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleExtendedProvStructExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleExtendedProvStructExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleExtendedProvStructExtendedArrayColumnIndex_Object = MibTableColumn
mscExampleExtendedProvStructExtendedArrayColumnIndex = _MscExampleExtendedProvStructExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1106, 1, 2),
    _MscExampleExtendedProvStructExtendedArrayColumnIndex_Type()
)
mscExampleExtendedProvStructExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedArrayColumnIndex.setStatus("mandatory")


class _MscExampleExtendedProvStructExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvStructExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleExtendedProvStructExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvStructExtendedArrayValue_Object = MibTableColumn
mscExampleExtendedProvStructExtendedArrayValue = _MscExampleExtendedProvStructExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1106, 1, 3),
    _MscExampleExtendedProvStructExtendedArrayValue_Type()
)
mscExampleExtendedProvStructExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedArrayValue.setStatus("mandatory")
_MscExampleExtendedProvStructExtendedVectorTable_Object = MibTable
mscExampleExtendedProvStructExtendedVectorTable = _MscExampleExtendedProvStructExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1107)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedVectorTable.setStatus("mandatory")
_MscExampleExtendedProvStructExtendedVectorEntry_Object = MibTableRow
mscExampleExtendedProvStructExtendedVectorEntry = _MscExampleExtendedProvStructExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1107, 1)
)
mscExampleExtendedProvStructExtendedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvStructExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedVectorEntry.setStatus("mandatory")


class _MscExampleExtendedProvStructExtendedVectorIndex_Type(Integer32):
    """Custom type mscExampleExtendedProvStructExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleExtendedProvStructExtendedVectorIndex_Type.__name__ = "Integer32"
_MscExampleExtendedProvStructExtendedVectorIndex_Object = MibTableColumn
mscExampleExtendedProvStructExtendedVectorIndex = _MscExampleExtendedProvStructExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1107, 1, 1),
    _MscExampleExtendedProvStructExtendedVectorIndex_Type()
)
mscExampleExtendedProvStructExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedVectorIndex.setStatus("mandatory")


class _MscExampleExtendedProvStructExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvStructExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleExtendedProvStructExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvStructExtendedVectorValue_Object = MibTableColumn
mscExampleExtendedProvStructExtendedVectorValue = _MscExampleExtendedProvStructExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1107, 1, 2),
    _MscExampleExtendedProvStructExtendedVectorValue_Type()
)
mscExampleExtendedProvStructExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvStructExtendedVectorValue.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedListTable_Object = MibTable
mscExampleExtendedProvFreeExtendedListTable = _MscExampleExtendedProvFreeExtendedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1108)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedListTable.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedListEntry_Object = MibTableRow
mscExampleExtendedProvFreeExtendedListEntry = _MscExampleExtendedProvFreeExtendedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1108, 1)
)
mscExampleExtendedProvFreeExtendedListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvFreeExtendedListValue"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedListEntry.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedListValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvFreeExtendedListValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedProvFreeExtendedListValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvFreeExtendedListValue_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedListValue = _MscExampleExtendedProvFreeExtendedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1108, 1, 1),
    _MscExampleExtendedProvFreeExtendedListValue_Type()
)
mscExampleExtendedProvFreeExtendedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedListValue.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedListRowStatus_Type = RowStatus
_MscExampleExtendedProvFreeExtendedListRowStatus_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedListRowStatus = _MscExampleExtendedProvFreeExtendedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1108, 1, 2),
    _MscExampleExtendedProvFreeExtendedListRowStatus_Type()
)
mscExampleExtendedProvFreeExtendedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedListRowStatus.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedReplicatedTable_Object = MibTable
mscExampleExtendedProvFreeExtendedReplicatedTable = _MscExampleExtendedProvFreeExtendedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1109)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedReplicatedTable.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedReplicatedEntry_Object = MibTableRow
mscExampleExtendedProvFreeExtendedReplicatedEntry = _MscExampleExtendedProvFreeExtendedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1109, 1)
)
mscExampleExtendedProvFreeExtendedReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvFreeExtendedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedReplicatedEntry.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedReplicatedIndex_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvFreeExtendedReplicatedIndex based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MscExampleExtendedProvFreeExtendedReplicatedIndex_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvFreeExtendedReplicatedIndex_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedReplicatedIndex = _MscExampleExtendedProvFreeExtendedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1109, 1, 1),
    _MscExampleExtendedProvFreeExtendedReplicatedIndex_Type()
)
mscExampleExtendedProvFreeExtendedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedReplicatedIndex.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedReplicatedValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvFreeExtendedReplicatedValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleExtendedProvFreeExtendedReplicatedValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvFreeExtendedReplicatedValue_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedReplicatedValue = _MscExampleExtendedProvFreeExtendedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1109, 1, 2),
    _MscExampleExtendedProvFreeExtendedReplicatedValue_Type()
)
mscExampleExtendedProvFreeExtendedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedReplicatedValue.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedReplicatedRowStatus_Type = RowStatus
_MscExampleExtendedProvFreeExtendedReplicatedRowStatus_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedReplicatedRowStatus = _MscExampleExtendedProvFreeExtendedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1109, 1, 3),
    _MscExampleExtendedProvFreeExtendedReplicatedRowStatus_Type()
)
mscExampleExtendedProvFreeExtendedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedReplicatedRowStatus.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedArrayTable_Object = MibTable
mscExampleExtendedProvFreeExtendedArrayTable = _MscExampleExtendedProvFreeExtendedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1110)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedArrayTable.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedArrayEntry_Object = MibTableRow
mscExampleExtendedProvFreeExtendedArrayEntry = _MscExampleExtendedProvFreeExtendedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1110, 1)
)
mscExampleExtendedProvFreeExtendedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvFreeExtendedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvFreeExtendedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedArrayEntry.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleExtendedProvFreeExtendedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleExtendedProvFreeExtendedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleExtendedProvFreeExtendedArrayRowIndex_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedArrayRowIndex = _MscExampleExtendedProvFreeExtendedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1110, 1, 1),
    _MscExampleExtendedProvFreeExtendedArrayRowIndex_Type()
)
mscExampleExtendedProvFreeExtendedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedArrayRowIndex.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleExtendedProvFreeExtendedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleExtendedProvFreeExtendedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleExtendedProvFreeExtendedArrayColumnIndex_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedArrayColumnIndex = _MscExampleExtendedProvFreeExtendedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1110, 1, 2),
    _MscExampleExtendedProvFreeExtendedArrayColumnIndex_Type()
)
mscExampleExtendedProvFreeExtendedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedArrayColumnIndex.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedArrayValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvFreeExtendedArrayValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleExtendedProvFreeExtendedArrayValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvFreeExtendedArrayValue_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedArrayValue = _MscExampleExtendedProvFreeExtendedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1110, 1, 3),
    _MscExampleExtendedProvFreeExtendedArrayValue_Type()
)
mscExampleExtendedProvFreeExtendedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedArrayValue.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedVectorTable_Object = MibTable
mscExampleExtendedProvFreeExtendedVectorTable = _MscExampleExtendedProvFreeExtendedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1111)
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedVectorTable.setStatus("mandatory")
_MscExampleExtendedProvFreeExtendedVectorEntry_Object = MibTableRow
mscExampleExtendedProvFreeExtendedVectorEntry = _MscExampleExtendedProvFreeExtendedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1111, 1)
)
mscExampleExtendedProvFreeExtendedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleExtendedProvFreeExtendedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedVectorEntry.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedVectorIndex_Type(Integer32):
    """Custom type mscExampleExtendedProvFreeExtendedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleExtendedProvFreeExtendedVectorIndex_Type.__name__ = "Integer32"
_MscExampleExtendedProvFreeExtendedVectorIndex_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedVectorIndex = _MscExampleExtendedProvFreeExtendedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1111, 1, 1),
    _MscExampleExtendedProvFreeExtendedVectorIndex_Type()
)
mscExampleExtendedProvFreeExtendedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedVectorIndex.setStatus("mandatory")


class _MscExampleExtendedProvFreeExtendedVectorValue_Type(ExtendedAsciiString):
    """Custom type mscExampleExtendedProvFreeExtendedVectorValue based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleExtendedProvFreeExtendedVectorValue_Type.__name__ = "ExtendedAsciiString"
_MscExampleExtendedProvFreeExtendedVectorValue_Object = MibTableColumn
mscExampleExtendedProvFreeExtendedVectorValue = _MscExampleExtendedProvFreeExtendedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 8, 1111, 1, 2),
    _MscExampleExtendedProvFreeExtendedVectorValue_Type()
)
mscExampleExtendedProvFreeExtendedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleExtendedProvFreeExtendedVectorValue.setStatus("mandatory")
_MscExampleBcd_ObjectIdentity = ObjectIdentity
mscExampleBcd = _MscExampleBcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9)
)
_MscExampleBcdRowStatusTable_Object = MibTable
mscExampleBcdRowStatusTable = _MscExampleBcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1)
)
if mibBuilder.loadTexts:
    mscExampleBcdRowStatusTable.setStatus("mandatory")
_MscExampleBcdRowStatusEntry_Object = MibTableRow
mscExampleBcdRowStatusEntry = _MscExampleBcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1, 1)
)
mscExampleBcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdRowStatusEntry.setStatus("mandatory")
_MscExampleBcdRowStatus_Type = RowStatus
_MscExampleBcdRowStatus_Object = MibTableColumn
mscExampleBcdRowStatus = _MscExampleBcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1, 1, 1),
    _MscExampleBcdRowStatus_Type()
)
mscExampleBcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdRowStatus.setStatus("mandatory")
_MscExampleBcdComponentName_Type = DisplayString
_MscExampleBcdComponentName_Object = MibTableColumn
mscExampleBcdComponentName = _MscExampleBcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1, 1, 2),
    _MscExampleBcdComponentName_Type()
)
mscExampleBcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleBcdComponentName.setStatus("mandatory")
_MscExampleBcdStorageType_Type = StorageType
_MscExampleBcdStorageType_Object = MibTableColumn
mscExampleBcdStorageType = _MscExampleBcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1, 1, 4),
    _MscExampleBcdStorageType_Type()
)
mscExampleBcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleBcdStorageType.setStatus("mandatory")


class _MscExampleBcdIndex_Type(DigitString):
    """Custom type mscExampleBcdIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleBcdIndex_Type.__name__ = "DigitString"
_MscExampleBcdIndex_Object = MibTableColumn
mscExampleBcdIndex = _MscExampleBcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1, 1, 10),
    _MscExampleBcdIndex_Type()
)
mscExampleBcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdIndex.setStatus("mandatory")
_MscExampleBcdOperationalTable_Object = MibTable
mscExampleBcdOperationalTable = _MscExampleBcdOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 10)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperationalTable.setStatus("mandatory")
_MscExampleBcdOperationalEntry_Object = MibTableRow
mscExampleBcdOperationalEntry = _MscExampleBcdOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 10, 1)
)
mscExampleBcdOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperationalEntry.setStatus("mandatory")


class _MscExampleBcdOperStructBcd_Type(DigitString):
    """Custom type mscExampleBcdOperStructBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdOperStructBcd_Type.__name__ = "DigitString"
_MscExampleBcdOperStructBcd_Object = MibTableColumn
mscExampleBcdOperStructBcd = _MscExampleBcdOperStructBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 10, 1, 1),
    _MscExampleBcdOperStructBcd_Type()
)
mscExampleBcdOperStructBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcd.setStatus("mandatory")


class _MscExampleBcdOperFreeBcd_Type(DigitString):
    """Custom type mscExampleBcdOperFreeBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdOperFreeBcd_Type.__name__ = "DigitString"
_MscExampleBcdOperFreeBcd_Object = MibTableColumn
mscExampleBcdOperFreeBcd = _MscExampleBcdOperFreeBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 10, 1, 2),
    _MscExampleBcdOperFreeBcd_Type()
)
mscExampleBcdOperFreeBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcd.setStatus("mandatory")
_MscExampleBcdProvisionalTable_Object = MibTable
mscExampleBcdProvisionalTable = _MscExampleBcdProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 11)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvisionalTable.setStatus("mandatory")
_MscExampleBcdProvisionalEntry_Object = MibTableRow
mscExampleBcdProvisionalEntry = _MscExampleBcdProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 11, 1)
)
mscExampleBcdProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvisionalEntry.setStatus("mandatory")
_MscExampleBcdProvEnumSub_Type = Link
_MscExampleBcdProvEnumSub_Object = MibTableColumn
mscExampleBcdProvEnumSub = _MscExampleBcdProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 11, 1, 1),
    _MscExampleBcdProvEnumSub_Type()
)
mscExampleBcdProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvEnumSub.setStatus("mandatory")


class _MscExampleBcdProvStructBcd_Type(DigitString):
    """Custom type mscExampleBcdProvStructBcd based on DigitString"""
    defaultHexValue = "30313233343536373839"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdProvStructBcd_Type.__name__ = "DigitString"
_MscExampleBcdProvStructBcd_Object = MibTableColumn
mscExampleBcdProvStructBcd = _MscExampleBcdProvStructBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 11, 1, 2),
    _MscExampleBcdProvStructBcd_Type()
)
mscExampleBcdProvStructBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcd.setStatus("mandatory")


class _MscExampleBcdProvFreeBcd_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcd based on DigitString"""
    defaultHexValue = "31323334353637383930"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_MscExampleBcdProvFreeBcd_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcd_Object = MibTableColumn
mscExampleBcdProvFreeBcd = _MscExampleBcdProvFreeBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 11, 1, 3),
    _MscExampleBcdProvFreeBcd_Type()
)
mscExampleBcdProvFreeBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcd.setStatus("mandatory")


class _MscExampleBcdProvFreeBcd1_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcd1 based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_MscExampleBcdProvFreeBcd1_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcd1_Object = MibTableColumn
mscExampleBcdProvFreeBcd1 = _MscExampleBcdProvFreeBcd1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 11, 1, 4),
    _MscExampleBcdProvFreeBcd1_Type()
)
mscExampleBcdProvFreeBcd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcd1.setStatus("mandatory")
_MscExampleBcdOperStructBcdVectorTable_Object = MibTable
mscExampleBcdOperStructBcdVectorTable = _MscExampleBcdOperStructBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1120)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdVectorTable.setStatus("mandatory")
_MscExampleBcdOperStructBcdVectorEntry_Object = MibTableRow
mscExampleBcdOperStructBcdVectorEntry = _MscExampleBcdOperStructBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1120, 1)
)
mscExampleBcdOperStructBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperStructBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdVectorEntry.setStatus("mandatory")


class _MscExampleBcdOperStructBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleBcdOperStructBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleBcdOperStructBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleBcdOperStructBcdVectorIndex_Object = MibTableColumn
mscExampleBcdOperStructBcdVectorIndex = _MscExampleBcdOperStructBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1120, 1, 1),
    _MscExampleBcdOperStructBcdVectorIndex_Type()
)
mscExampleBcdOperStructBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdVectorIndex.setStatus("mandatory")


class _MscExampleBcdOperStructBcdVectorValue_Type(DigitString):
    """Custom type mscExampleBcdOperStructBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdOperStructBcdVectorValue_Type.__name__ = "DigitString"
_MscExampleBcdOperStructBcdVectorValue_Object = MibTableColumn
mscExampleBcdOperStructBcdVectorValue = _MscExampleBcdOperStructBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1120, 1, 2),
    _MscExampleBcdOperStructBcdVectorValue_Type()
)
mscExampleBcdOperStructBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdVectorValue.setStatus("mandatory")
_MscExampleBcdOperStructBcdArrayTable_Object = MibTable
mscExampleBcdOperStructBcdArrayTable = _MscExampleBcdOperStructBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1121)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdArrayTable.setStatus("mandatory")
_MscExampleBcdOperStructBcdArrayEntry_Object = MibTableRow
mscExampleBcdOperStructBcdArrayEntry = _MscExampleBcdOperStructBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1121, 1)
)
mscExampleBcdOperStructBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperStructBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperStructBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdArrayEntry.setStatus("mandatory")


class _MscExampleBcdOperStructBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleBcdOperStructBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleBcdOperStructBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleBcdOperStructBcdArrayRowIndex_Object = MibTableColumn
mscExampleBcdOperStructBcdArrayRowIndex = _MscExampleBcdOperStructBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1121, 1, 1),
    _MscExampleBcdOperStructBcdArrayRowIndex_Type()
)
mscExampleBcdOperStructBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleBcdOperStructBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleBcdOperStructBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleBcdOperStructBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleBcdOperStructBcdArrayColumnIndex_Object = MibTableColumn
mscExampleBcdOperStructBcdArrayColumnIndex = _MscExampleBcdOperStructBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1121, 1, 2),
    _MscExampleBcdOperStructBcdArrayColumnIndex_Type()
)
mscExampleBcdOperStructBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleBcdOperStructBcdArrayValue_Type(DigitString):
    """Custom type mscExampleBcdOperStructBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdOperStructBcdArrayValue_Type.__name__ = "DigitString"
_MscExampleBcdOperStructBcdArrayValue_Object = MibTableColumn
mscExampleBcdOperStructBcdArrayValue = _MscExampleBcdOperStructBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1121, 1, 3),
    _MscExampleBcdOperStructBcdArrayValue_Type()
)
mscExampleBcdOperStructBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperStructBcdArrayValue.setStatus("mandatory")
_MscExampleBcdOperFreeBcdVectorTable_Object = MibTable
mscExampleBcdOperFreeBcdVectorTable = _MscExampleBcdOperFreeBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1122)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdVectorTable.setStatus("mandatory")
_MscExampleBcdOperFreeBcdVectorEntry_Object = MibTableRow
mscExampleBcdOperFreeBcdVectorEntry = _MscExampleBcdOperFreeBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1122, 1)
)
mscExampleBcdOperFreeBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperFreeBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdVectorEntry.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleBcdOperFreeBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleBcdOperFreeBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleBcdOperFreeBcdVectorIndex_Object = MibTableColumn
mscExampleBcdOperFreeBcdVectorIndex = _MscExampleBcdOperFreeBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1122, 1, 1),
    _MscExampleBcdOperFreeBcdVectorIndex_Type()
)
mscExampleBcdOperFreeBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdVectorIndex.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdVectorValue_Type(DigitString):
    """Custom type mscExampleBcdOperFreeBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdOperFreeBcdVectorValue_Type.__name__ = "DigitString"
_MscExampleBcdOperFreeBcdVectorValue_Object = MibTableColumn
mscExampleBcdOperFreeBcdVectorValue = _MscExampleBcdOperFreeBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1122, 1, 2),
    _MscExampleBcdOperFreeBcdVectorValue_Type()
)
mscExampleBcdOperFreeBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdVectorValue.setStatus("mandatory")
_MscExampleBcdOperFreeBcdArrayTable_Object = MibTable
mscExampleBcdOperFreeBcdArrayTable = _MscExampleBcdOperFreeBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1123)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdArrayTable.setStatus("mandatory")
_MscExampleBcdOperFreeBcdArrayEntry_Object = MibTableRow
mscExampleBcdOperFreeBcdArrayEntry = _MscExampleBcdOperFreeBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1123, 1)
)
mscExampleBcdOperFreeBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperFreeBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperFreeBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdArrayEntry.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleBcdOperFreeBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleBcdOperFreeBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleBcdOperFreeBcdArrayRowIndex_Object = MibTableColumn
mscExampleBcdOperFreeBcdArrayRowIndex = _MscExampleBcdOperFreeBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1123, 1, 1),
    _MscExampleBcdOperFreeBcdArrayRowIndex_Type()
)
mscExampleBcdOperFreeBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleBcdOperFreeBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleBcdOperFreeBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleBcdOperFreeBcdArrayColumnIndex_Object = MibTableColumn
mscExampleBcdOperFreeBcdArrayColumnIndex = _MscExampleBcdOperFreeBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1123, 1, 2),
    _MscExampleBcdOperFreeBcdArrayColumnIndex_Type()
)
mscExampleBcdOperFreeBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdArrayValue_Type(DigitString):
    """Custom type mscExampleBcdOperFreeBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdOperFreeBcdArrayValue_Type.__name__ = "DigitString"
_MscExampleBcdOperFreeBcdArrayValue_Object = MibTableColumn
mscExampleBcdOperFreeBcdArrayValue = _MscExampleBcdOperFreeBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1123, 1, 3),
    _MscExampleBcdOperFreeBcdArrayValue_Type()
)
mscExampleBcdOperFreeBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdArrayValue.setStatus("mandatory")
_MscExampleBcdOperFreeBcdReplicatedTable_Object = MibTable
mscExampleBcdOperFreeBcdReplicatedTable = _MscExampleBcdOperFreeBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1124)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdReplicatedTable.setStatus("mandatory")
_MscExampleBcdOperFreeBcdReplicatedEntry_Object = MibTableRow
mscExampleBcdOperFreeBcdReplicatedEntry = _MscExampleBcdOperFreeBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1124, 1)
)
mscExampleBcdOperFreeBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperFreeBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdReplicatedEntry.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdReplicatedIndex_Type(DigitString):
    """Custom type mscExampleBcdOperFreeBcdReplicatedIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdOperFreeBcdReplicatedIndex_Type.__name__ = "DigitString"
_MscExampleBcdOperFreeBcdReplicatedIndex_Object = MibTableColumn
mscExampleBcdOperFreeBcdReplicatedIndex = _MscExampleBcdOperFreeBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1124, 1, 1),
    _MscExampleBcdOperFreeBcdReplicatedIndex_Type()
)
mscExampleBcdOperFreeBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdReplicatedIndex.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdReplicatedValue_Type(DigitString):
    """Custom type mscExampleBcdOperFreeBcdReplicatedValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdOperFreeBcdReplicatedValue_Type.__name__ = "DigitString"
_MscExampleBcdOperFreeBcdReplicatedValue_Object = MibTableColumn
mscExampleBcdOperFreeBcdReplicatedValue = _MscExampleBcdOperFreeBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1124, 1, 2),
    _MscExampleBcdOperFreeBcdReplicatedValue_Type()
)
mscExampleBcdOperFreeBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdReplicatedValue.setStatus("mandatory")
_MscExampleBcdOperFreeBcdReplicatedRowStatus_Type = RowStatus
_MscExampleBcdOperFreeBcdReplicatedRowStatus_Object = MibTableColumn
mscExampleBcdOperFreeBcdReplicatedRowStatus = _MscExampleBcdOperFreeBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1124, 1, 3),
    _MscExampleBcdOperFreeBcdReplicatedRowStatus_Type()
)
mscExampleBcdOperFreeBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdReplicatedRowStatus.setStatus("mandatory")
_MscExampleBcdOperFreeBcdListTable_Object = MibTable
mscExampleBcdOperFreeBcdListTable = _MscExampleBcdOperFreeBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1125)
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdListTable.setStatus("mandatory")
_MscExampleBcdOperFreeBcdListEntry_Object = MibTableRow
mscExampleBcdOperFreeBcdListEntry = _MscExampleBcdOperFreeBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1125, 1)
)
mscExampleBcdOperFreeBcdListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdOperFreeBcdListValue"),
)
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdListEntry.setStatus("mandatory")


class _MscExampleBcdOperFreeBcdListValue_Type(DigitString):
    """Custom type mscExampleBcdOperFreeBcdListValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdOperFreeBcdListValue_Type.__name__ = "DigitString"
_MscExampleBcdOperFreeBcdListValue_Object = MibTableColumn
mscExampleBcdOperFreeBcdListValue = _MscExampleBcdOperFreeBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1125, 1, 1),
    _MscExampleBcdOperFreeBcdListValue_Type()
)
mscExampleBcdOperFreeBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdListValue.setStatus("mandatory")
_MscExampleBcdOperFreeBcdListRowStatus_Type = RowStatus
_MscExampleBcdOperFreeBcdListRowStatus_Object = MibTableColumn
mscExampleBcdOperFreeBcdListRowStatus = _MscExampleBcdOperFreeBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1125, 1, 2),
    _MscExampleBcdOperFreeBcdListRowStatus_Type()
)
mscExampleBcdOperFreeBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleBcdOperFreeBcdListRowStatus.setStatus("mandatory")
_MscExampleBcdProvStructBcdVectorTable_Object = MibTable
mscExampleBcdProvStructBcdVectorTable = _MscExampleBcdProvStructBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1126)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdVectorTable.setStatus("mandatory")
_MscExampleBcdProvStructBcdVectorEntry_Object = MibTableRow
mscExampleBcdProvStructBcdVectorEntry = _MscExampleBcdProvStructBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1126, 1)
)
mscExampleBcdProvStructBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvStructBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdVectorEntry.setStatus("mandatory")


class _MscExampleBcdProvStructBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleBcdProvStructBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleBcdProvStructBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvStructBcdVectorIndex_Object = MibTableColumn
mscExampleBcdProvStructBcdVectorIndex = _MscExampleBcdProvStructBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1126, 1, 1),
    _MscExampleBcdProvStructBcdVectorIndex_Type()
)
mscExampleBcdProvStructBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdVectorIndex.setStatus("mandatory")


class _MscExampleBcdProvStructBcdVectorValue_Type(DigitString):
    """Custom type mscExampleBcdProvStructBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvStructBcdVectorValue_Type.__name__ = "DigitString"
_MscExampleBcdProvStructBcdVectorValue_Object = MibTableColumn
mscExampleBcdProvStructBcdVectorValue = _MscExampleBcdProvStructBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1126, 1, 2),
    _MscExampleBcdProvStructBcdVectorValue_Type()
)
mscExampleBcdProvStructBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdVectorValue.setStatus("mandatory")
_MscExampleBcdProvStructBcdArrayTable_Object = MibTable
mscExampleBcdProvStructBcdArrayTable = _MscExampleBcdProvStructBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1127)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdArrayTable.setStatus("mandatory")
_MscExampleBcdProvStructBcdArrayEntry_Object = MibTableRow
mscExampleBcdProvStructBcdArrayEntry = _MscExampleBcdProvStructBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1127, 1)
)
mscExampleBcdProvStructBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvStructBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvStructBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdArrayEntry.setStatus("mandatory")


class _MscExampleBcdProvStructBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleBcdProvStructBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleBcdProvStructBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvStructBcdArrayRowIndex_Object = MibTableColumn
mscExampleBcdProvStructBcdArrayRowIndex = _MscExampleBcdProvStructBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1127, 1, 1),
    _MscExampleBcdProvStructBcdArrayRowIndex_Type()
)
mscExampleBcdProvStructBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleBcdProvStructBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleBcdProvStructBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleBcdProvStructBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvStructBcdArrayColumnIndex_Object = MibTableColumn
mscExampleBcdProvStructBcdArrayColumnIndex = _MscExampleBcdProvStructBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1127, 1, 2),
    _MscExampleBcdProvStructBcdArrayColumnIndex_Type()
)
mscExampleBcdProvStructBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleBcdProvStructBcdArrayValue_Type(DigitString):
    """Custom type mscExampleBcdProvStructBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvStructBcdArrayValue_Type.__name__ = "DigitString"
_MscExampleBcdProvStructBcdArrayValue_Object = MibTableColumn
mscExampleBcdProvStructBcdArrayValue = _MscExampleBcdProvStructBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1127, 1, 3),
    _MscExampleBcdProvStructBcdArrayValue_Type()
)
mscExampleBcdProvStructBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvStructBcdArrayValue.setStatus("mandatory")
_MscExampleBcdProvFreeBcdVectorTable_Object = MibTable
mscExampleBcdProvFreeBcdVectorTable = _MscExampleBcdProvFreeBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1128)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVectorTable.setStatus("mandatory")
_MscExampleBcdProvFreeBcdVectorEntry_Object = MibTableRow
mscExampleBcdProvFreeBcdVectorEntry = _MscExampleBcdProvFreeBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1128, 1)
)
mscExampleBcdProvFreeBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVectorEntry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleBcdProvFreeBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleBcdProvFreeBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvFreeBcdVectorIndex_Object = MibTableColumn
mscExampleBcdProvFreeBcdVectorIndex = _MscExampleBcdProvFreeBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1128, 1, 1),
    _MscExampleBcdProvFreeBcdVectorIndex_Type()
)
mscExampleBcdProvFreeBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVectorIndex.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdVectorValue_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdVectorValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvFreeBcdVectorValue_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdVectorValue_Object = MibTableColumn
mscExampleBcdProvFreeBcdVectorValue = _MscExampleBcdProvFreeBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1128, 1, 2),
    _MscExampleBcdProvFreeBcdVectorValue_Type()
)
mscExampleBcdProvFreeBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVectorValue.setStatus("mandatory")
_MscExampleBcdProvFreeBcdVector1Table_Object = MibTable
mscExampleBcdProvFreeBcdVector1Table = _MscExampleBcdProvFreeBcdVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1129)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVector1Table.setStatus("mandatory")
_MscExampleBcdProvFreeBcdVector1Entry_Object = MibTableRow
mscExampleBcdProvFreeBcdVector1Entry = _MscExampleBcdProvFreeBcdVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1129, 1)
)
mscExampleBcdProvFreeBcdVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVector1Entry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdVector1Index_Type(Integer32):
    """Custom type mscExampleBcdProvFreeBcdVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscExampleBcdProvFreeBcdVector1Index_Type.__name__ = "Integer32"
_MscExampleBcdProvFreeBcdVector1Index_Object = MibTableColumn
mscExampleBcdProvFreeBcdVector1Index = _MscExampleBcdProvFreeBcdVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1129, 1, 1),
    _MscExampleBcdProvFreeBcdVector1Index_Type()
)
mscExampleBcdProvFreeBcdVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVector1Index.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdVector1Value_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdVector1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvFreeBcdVector1Value_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdVector1Value_Object = MibTableColumn
mscExampleBcdProvFreeBcdVector1Value = _MscExampleBcdProvFreeBcdVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1129, 1, 2),
    _MscExampleBcdProvFreeBcdVector1Value_Type()
)
mscExampleBcdProvFreeBcdVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdVector1Value.setStatus("mandatory")
_MscExampleBcdProvFreeBcdArrayTable_Object = MibTable
mscExampleBcdProvFreeBcdArrayTable = _MscExampleBcdProvFreeBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1130)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArrayTable.setStatus("mandatory")
_MscExampleBcdProvFreeBcdArrayEntry_Object = MibTableRow
mscExampleBcdProvFreeBcdArrayEntry = _MscExampleBcdProvFreeBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1130, 1)
)
mscExampleBcdProvFreeBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArrayEntry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleBcdProvFreeBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleBcdProvFreeBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvFreeBcdArrayRowIndex_Object = MibTableColumn
mscExampleBcdProvFreeBcdArrayRowIndex = _MscExampleBcdProvFreeBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1130, 1, 1),
    _MscExampleBcdProvFreeBcdArrayRowIndex_Type()
)
mscExampleBcdProvFreeBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleBcdProvFreeBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleBcdProvFreeBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvFreeBcdArrayColumnIndex_Object = MibTableColumn
mscExampleBcdProvFreeBcdArrayColumnIndex = _MscExampleBcdProvFreeBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1130, 1, 2),
    _MscExampleBcdProvFreeBcdArrayColumnIndex_Type()
)
mscExampleBcdProvFreeBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdArrayValue_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdArrayValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvFreeBcdArrayValue_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdArrayValue_Object = MibTableColumn
mscExampleBcdProvFreeBcdArrayValue = _MscExampleBcdProvFreeBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1130, 1, 3),
    _MscExampleBcdProvFreeBcdArrayValue_Type()
)
mscExampleBcdProvFreeBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArrayValue.setStatus("mandatory")
_MscExampleBcdProvFreeBcdArray1Table_Object = MibTable
mscExampleBcdProvFreeBcdArray1Table = _MscExampleBcdProvFreeBcdArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1131)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArray1Table.setStatus("mandatory")
_MscExampleBcdProvFreeBcdArray1Entry_Object = MibTableRow
mscExampleBcdProvFreeBcdArray1Entry = _MscExampleBcdProvFreeBcdArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1131, 1)
)
mscExampleBcdProvFreeBcdArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdArray1RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArray1Entry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdArray1RowIndex_Type(Integer32):
    """Custom type mscExampleBcdProvFreeBcdArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleBcdProvFreeBcdArray1RowIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvFreeBcdArray1RowIndex_Object = MibTableColumn
mscExampleBcdProvFreeBcdArray1RowIndex = _MscExampleBcdProvFreeBcdArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1131, 1, 1),
    _MscExampleBcdProvFreeBcdArray1RowIndex_Type()
)
mscExampleBcdProvFreeBcdArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArray1RowIndex.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdArray1ColumnIndex_Type(Integer32):
    """Custom type mscExampleBcdProvFreeBcdArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleBcdProvFreeBcdArray1ColumnIndex_Type.__name__ = "Integer32"
_MscExampleBcdProvFreeBcdArray1ColumnIndex_Object = MibTableColumn
mscExampleBcdProvFreeBcdArray1ColumnIndex = _MscExampleBcdProvFreeBcdArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1131, 1, 2),
    _MscExampleBcdProvFreeBcdArray1ColumnIndex_Type()
)
mscExampleBcdProvFreeBcdArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArray1ColumnIndex.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdArray1Value_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdArray1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvFreeBcdArray1Value_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdArray1Value_Object = MibTableColumn
mscExampleBcdProvFreeBcdArray1Value = _MscExampleBcdProvFreeBcdArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1131, 1, 3),
    _MscExampleBcdProvFreeBcdArray1Value_Type()
)
mscExampleBcdProvFreeBcdArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdArray1Value.setStatus("mandatory")
_MscExampleBcdProvFreeBcdReplicatedTable_Object = MibTable
mscExampleBcdProvFreeBcdReplicatedTable = _MscExampleBcdProvFreeBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1132)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicatedTable.setStatus("mandatory")
_MscExampleBcdProvFreeBcdReplicatedEntry_Object = MibTableRow
mscExampleBcdProvFreeBcdReplicatedEntry = _MscExampleBcdProvFreeBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1132, 1)
)
mscExampleBcdProvFreeBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicatedEntry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdReplicatedIndex_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdReplicatedIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvFreeBcdReplicatedIndex_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdReplicatedIndex_Object = MibTableColumn
mscExampleBcdProvFreeBcdReplicatedIndex = _MscExampleBcdProvFreeBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1132, 1, 1),
    _MscExampleBcdProvFreeBcdReplicatedIndex_Type()
)
mscExampleBcdProvFreeBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicatedIndex.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdReplicatedValue_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdReplicatedValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdProvFreeBcdReplicatedValue_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdReplicatedValue_Object = MibTableColumn
mscExampleBcdProvFreeBcdReplicatedValue = _MscExampleBcdProvFreeBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1132, 1, 2),
    _MscExampleBcdProvFreeBcdReplicatedValue_Type()
)
mscExampleBcdProvFreeBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicatedValue.setStatus("mandatory")
_MscExampleBcdProvFreeBcdReplicatedRowStatus_Type = RowStatus
_MscExampleBcdProvFreeBcdReplicatedRowStatus_Object = MibTableColumn
mscExampleBcdProvFreeBcdReplicatedRowStatus = _MscExampleBcdProvFreeBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1132, 1, 3),
    _MscExampleBcdProvFreeBcdReplicatedRowStatus_Type()
)
mscExampleBcdProvFreeBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicatedRowStatus.setStatus("mandatory")
_MscExampleBcdProvFreeBcdReplicated1Table_Object = MibTable
mscExampleBcdProvFreeBcdReplicated1Table = _MscExampleBcdProvFreeBcdReplicated1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1133)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicated1Table.setStatus("mandatory")
_MscExampleBcdProvFreeBcdReplicated1Entry_Object = MibTableRow
mscExampleBcdProvFreeBcdReplicated1Entry = _MscExampleBcdProvFreeBcdReplicated1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1133, 1)
)
mscExampleBcdProvFreeBcdReplicated1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdReplicated1Index"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicated1Entry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdReplicated1Index_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdReplicated1Index based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_MscExampleBcdProvFreeBcdReplicated1Index_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdReplicated1Index_Object = MibTableColumn
mscExampleBcdProvFreeBcdReplicated1Index = _MscExampleBcdProvFreeBcdReplicated1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1133, 1, 1),
    _MscExampleBcdProvFreeBcdReplicated1Index_Type()
)
mscExampleBcdProvFreeBcdReplicated1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicated1Index.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdReplicated1Value_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdReplicated1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleBcdProvFreeBcdReplicated1Value_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdReplicated1Value_Object = MibTableColumn
mscExampleBcdProvFreeBcdReplicated1Value = _MscExampleBcdProvFreeBcdReplicated1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1133, 1, 2),
    _MscExampleBcdProvFreeBcdReplicated1Value_Type()
)
mscExampleBcdProvFreeBcdReplicated1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicated1Value.setStatus("mandatory")
_MscExampleBcdProvFreeBcdReplicated1RowStatus_Type = RowStatus
_MscExampleBcdProvFreeBcdReplicated1RowStatus_Object = MibTableColumn
mscExampleBcdProvFreeBcdReplicated1RowStatus = _MscExampleBcdProvFreeBcdReplicated1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1133, 1, 3),
    _MscExampleBcdProvFreeBcdReplicated1RowStatus_Type()
)
mscExampleBcdProvFreeBcdReplicated1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdReplicated1RowStatus.setStatus("mandatory")
_MscExampleBcdProvFreeBcdListTable_Object = MibTable
mscExampleBcdProvFreeBcdListTable = _MscExampleBcdProvFreeBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1134)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdListTable.setStatus("mandatory")
_MscExampleBcdProvFreeBcdListEntry_Object = MibTableRow
mscExampleBcdProvFreeBcdListEntry = _MscExampleBcdProvFreeBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1134, 1)
)
mscExampleBcdProvFreeBcdListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdListValue"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdListEntry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdListValue_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdListValue based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdProvFreeBcdListValue_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdListValue_Object = MibTableColumn
mscExampleBcdProvFreeBcdListValue = _MscExampleBcdProvFreeBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1134, 1, 1),
    _MscExampleBcdProvFreeBcdListValue_Type()
)
mscExampleBcdProvFreeBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdListValue.setStatus("mandatory")
_MscExampleBcdProvFreeBcdListRowStatus_Type = RowStatus
_MscExampleBcdProvFreeBcdListRowStatus_Object = MibTableColumn
mscExampleBcdProvFreeBcdListRowStatus = _MscExampleBcdProvFreeBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1134, 1, 2),
    _MscExampleBcdProvFreeBcdListRowStatus_Type()
)
mscExampleBcdProvFreeBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdListRowStatus.setStatus("mandatory")
_MscExampleBcdProvFreeBcdList1Table_Object = MibTable
mscExampleBcdProvFreeBcdList1Table = _MscExampleBcdProvFreeBcdList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1135)
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdList1Table.setStatus("mandatory")
_MscExampleBcdProvFreeBcdList1Entry_Object = MibTableRow
mscExampleBcdProvFreeBcdList1Entry = _MscExampleBcdProvFreeBcdList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1135, 1)
)
mscExampleBcdProvFreeBcdList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdProvFreeBcdList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdList1Entry.setStatus("mandatory")


class _MscExampleBcdProvFreeBcdList1Value_Type(DigitString):
    """Custom type mscExampleBcdProvFreeBcdList1Value based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleBcdProvFreeBcdList1Value_Type.__name__ = "DigitString"
_MscExampleBcdProvFreeBcdList1Value_Object = MibTableColumn
mscExampleBcdProvFreeBcdList1Value = _MscExampleBcdProvFreeBcdList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1135, 1, 1),
    _MscExampleBcdProvFreeBcdList1Value_Type()
)
mscExampleBcdProvFreeBcdList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdList1Value.setStatus("mandatory")
_MscExampleBcdProvFreeBcdList1RowStatus_Type = RowStatus
_MscExampleBcdProvFreeBcdList1RowStatus_Object = MibTableColumn
mscExampleBcdProvFreeBcdList1RowStatus = _MscExampleBcdProvFreeBcdList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 9, 1135, 1, 2),
    _MscExampleBcdProvFreeBcdList1RowStatus_Type()
)
mscExampleBcdProvFreeBcdList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleBcdProvFreeBcdList1RowStatus.setStatus("mandatory")
_MscExampleWildBcd_ObjectIdentity = ObjectIdentity
mscExampleWildBcd = _MscExampleWildBcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10)
)
_MscExampleWildBcdRowStatusTable_Object = MibTable
mscExampleWildBcdRowStatusTable = _MscExampleWildBcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdRowStatusTable.setStatus("mandatory")
_MscExampleWildBcdRowStatusEntry_Object = MibTableRow
mscExampleWildBcdRowStatusEntry = _MscExampleWildBcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1, 1)
)
mscExampleWildBcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdRowStatusEntry.setStatus("mandatory")
_MscExampleWildBcdRowStatus_Type = RowStatus
_MscExampleWildBcdRowStatus_Object = MibTableColumn
mscExampleWildBcdRowStatus = _MscExampleWildBcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1, 1, 1),
    _MscExampleWildBcdRowStatus_Type()
)
mscExampleWildBcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdRowStatus.setStatus("mandatory")
_MscExampleWildBcdComponentName_Type = DisplayString
_MscExampleWildBcdComponentName_Object = MibTableColumn
mscExampleWildBcdComponentName = _MscExampleWildBcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1, 1, 2),
    _MscExampleWildBcdComponentName_Type()
)
mscExampleWildBcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleWildBcdComponentName.setStatus("mandatory")
_MscExampleWildBcdStorageType_Type = StorageType
_MscExampleWildBcdStorageType_Object = MibTableColumn
mscExampleWildBcdStorageType = _MscExampleWildBcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1, 1, 4),
    _MscExampleWildBcdStorageType_Type()
)
mscExampleWildBcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleWildBcdStorageType.setStatus("mandatory")


class _MscExampleWildBcdIndex_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleWildBcdIndex_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdIndex_Object = MibTableColumn
mscExampleWildBcdIndex = _MscExampleWildBcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1, 1, 10),
    _MscExampleWildBcdIndex_Type()
)
mscExampleWildBcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdIndex.setStatus("mandatory")
_MscExampleWildBcdOperationalTable_Object = MibTable
mscExampleWildBcdOperationalTable = _MscExampleWildBcdOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 10)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperationalTable.setStatus("mandatory")
_MscExampleWildBcdOperationalEntry_Object = MibTableRow
mscExampleWildBcdOperationalEntry = _MscExampleWildBcdOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 10, 1)
)
mscExampleWildBcdOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperationalEntry.setStatus("mandatory")


class _MscExampleWildBcdOperStructWildBcd_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperStructWildBcd based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdOperStructWildBcd_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperStructWildBcd_Object = MibTableColumn
mscExampleWildBcdOperStructWildBcd = _MscExampleWildBcdOperStructWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 10, 1, 1),
    _MscExampleWildBcdOperStructWildBcd_Type()
)
mscExampleWildBcdOperStructWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcd.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcd_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperFreeWildBcd based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdOperFreeWildBcd_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperFreeWildBcd_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcd = _MscExampleWildBcdOperFreeWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 10, 1, 2),
    _MscExampleWildBcdOperFreeWildBcd_Type()
)
mscExampleWildBcdOperFreeWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcd.setStatus("mandatory")
_MscExampleWildBcdProvisionalTable_Object = MibTable
mscExampleWildBcdProvisionalTable = _MscExampleWildBcdProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 11)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvisionalTable.setStatus("mandatory")
_MscExampleWildBcdProvisionalEntry_Object = MibTableRow
mscExampleWildBcdProvisionalEntry = _MscExampleWildBcdProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 11, 1)
)
mscExampleWildBcdProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvisionalEntry.setStatus("mandatory")


class _MscExampleWildBcdProvStructWildBcd_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvStructWildBcd based on WildcardedDigitString"""
    defaultHexValue = "30313233343536373839"

    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdProvStructWildBcd_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvStructWildBcd_Object = MibTableColumn
mscExampleWildBcdProvStructWildBcd = _MscExampleWildBcdProvStructWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 11, 1, 1),
    _MscExampleWildBcdProvStructWildBcd_Type()
)
mscExampleWildBcdProvStructWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcd.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcd_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvFreeWildBcd based on WildcardedDigitString"""
    defaultHexValue = "31323334353637383930"

    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_MscExampleWildBcdProvFreeWildBcd_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvFreeWildBcd_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcd = _MscExampleWildBcdProvFreeWildBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 11, 1, 2),
    _MscExampleWildBcdProvFreeWildBcd_Type()
)
mscExampleWildBcdProvFreeWildBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcd.setStatus("mandatory")
_MscExampleWildBcdOperStructWildBcdVectorTable_Object = MibTable
mscExampleWildBcdOperStructWildBcdVectorTable = _MscExampleWildBcdOperStructWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1136)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdVectorTable.setStatus("mandatory")
_MscExampleWildBcdOperStructWildBcdVectorEntry_Object = MibTableRow
mscExampleWildBcdOperStructWildBcdVectorEntry = _MscExampleWildBcdOperStructWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1136, 1)
)
mscExampleWildBcdOperStructWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperStructWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdVectorEntry.setStatus("mandatory")


class _MscExampleWildBcdOperStructWildBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleWildBcdOperStructWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleWildBcdOperStructWildBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdOperStructWildBcdVectorIndex_Object = MibTableColumn
mscExampleWildBcdOperStructWildBcdVectorIndex = _MscExampleWildBcdOperStructWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1136, 1, 1),
    _MscExampleWildBcdOperStructWildBcdVectorIndex_Type()
)
mscExampleWildBcdOperStructWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdVectorIndex.setStatus("mandatory")


class _MscExampleWildBcdOperStructWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperStructWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdOperStructWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperStructWildBcdVectorValue_Object = MibTableColumn
mscExampleWildBcdOperStructWildBcdVectorValue = _MscExampleWildBcdOperStructWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1136, 1, 2),
    _MscExampleWildBcdOperStructWildBcdVectorValue_Type()
)
mscExampleWildBcdOperStructWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdVectorValue.setStatus("mandatory")
_MscExampleWildBcdOperStructWildBcdArrayTable_Object = MibTable
mscExampleWildBcdOperStructWildBcdArrayTable = _MscExampleWildBcdOperStructWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1137)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdArrayTable.setStatus("mandatory")
_MscExampleWildBcdOperStructWildBcdArrayEntry_Object = MibTableRow
mscExampleWildBcdOperStructWildBcdArrayEntry = _MscExampleWildBcdOperStructWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1137, 1)
)
mscExampleWildBcdOperStructWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperStructWildBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperStructWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdArrayEntry.setStatus("mandatory")


class _MscExampleWildBcdOperStructWildBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleWildBcdOperStructWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleWildBcdOperStructWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdOperStructWildBcdArrayRowIndex_Object = MibTableColumn
mscExampleWildBcdOperStructWildBcdArrayRowIndex = _MscExampleWildBcdOperStructWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1137, 1, 1),
    _MscExampleWildBcdOperStructWildBcdArrayRowIndex_Type()
)
mscExampleWildBcdOperStructWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleWildBcdOperStructWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleWildBcdOperStructWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleWildBcdOperStructWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdOperStructWildBcdArrayColumnIndex_Object = MibTableColumn
mscExampleWildBcdOperStructWildBcdArrayColumnIndex = _MscExampleWildBcdOperStructWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1137, 1, 2),
    _MscExampleWildBcdOperStructWildBcdArrayColumnIndex_Type()
)
mscExampleWildBcdOperStructWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleWildBcdOperStructWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperStructWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdOperStructWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperStructWildBcdArrayValue_Object = MibTableColumn
mscExampleWildBcdOperStructWildBcdArrayValue = _MscExampleWildBcdOperStructWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1137, 1, 3),
    _MscExampleWildBcdOperStructWildBcdArrayValue_Type()
)
mscExampleWildBcdOperStructWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperStructWildBcdArrayValue.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdVectorTable_Object = MibTable
mscExampleWildBcdOperFreeWildBcdVectorTable = _MscExampleWildBcdOperFreeWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1138)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdVectorTable.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdVectorEntry_Object = MibTableRow
mscExampleWildBcdOperFreeWildBcdVectorEntry = _MscExampleWildBcdOperFreeWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1138, 1)
)
mscExampleWildBcdOperFreeWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperFreeWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdVectorEntry.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleWildBcdOperFreeWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleWildBcdOperFreeWildBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdOperFreeWildBcdVectorIndex_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdVectorIndex = _MscExampleWildBcdOperFreeWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1138, 1, 1),
    _MscExampleWildBcdOperFreeWildBcdVectorIndex_Type()
)
mscExampleWildBcdOperFreeWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdVectorIndex.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperFreeWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdOperFreeWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperFreeWildBcdVectorValue_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdVectorValue = _MscExampleWildBcdOperFreeWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1138, 1, 2),
    _MscExampleWildBcdOperFreeWildBcdVectorValue_Type()
)
mscExampleWildBcdOperFreeWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdVectorValue.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdArrayTable_Object = MibTable
mscExampleWildBcdOperFreeWildBcdArrayTable = _MscExampleWildBcdOperFreeWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1139)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdArrayTable.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdArrayEntry_Object = MibTableRow
mscExampleWildBcdOperFreeWildBcdArrayEntry = _MscExampleWildBcdOperFreeWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1139, 1)
)
mscExampleWildBcdOperFreeWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperFreeWildBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperFreeWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdArrayEntry.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleWildBcdOperFreeWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleWildBcdOperFreeWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdOperFreeWildBcdArrayRowIndex_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdArrayRowIndex = _MscExampleWildBcdOperFreeWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1139, 1, 1),
    _MscExampleWildBcdOperFreeWildBcdArrayRowIndex_Type()
)
mscExampleWildBcdOperFreeWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleWildBcdOperFreeWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleWildBcdOperFreeWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdOperFreeWildBcdArrayColumnIndex_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdArrayColumnIndex = _MscExampleWildBcdOperFreeWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1139, 1, 2),
    _MscExampleWildBcdOperFreeWildBcdArrayColumnIndex_Type()
)
mscExampleWildBcdOperFreeWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperFreeWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdOperFreeWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperFreeWildBcdArrayValue_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdArrayValue = _MscExampleWildBcdOperFreeWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1139, 1, 3),
    _MscExampleWildBcdOperFreeWildBcdArrayValue_Type()
)
mscExampleWildBcdOperFreeWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdArrayValue.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdReplicatedTable_Object = MibTable
mscExampleWildBcdOperFreeWildBcdReplicatedTable = _MscExampleWildBcdOperFreeWildBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1140)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdReplicatedTable.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdReplicatedEntry_Object = MibTableRow
mscExampleWildBcdOperFreeWildBcdReplicatedEntry = _MscExampleWildBcdOperFreeWildBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1140, 1)
)
mscExampleWildBcdOperFreeWildBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperFreeWildBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdReplicatedEntry.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdReplicatedIndex_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperFreeWildBcdReplicatedIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdOperFreeWildBcdReplicatedIndex_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperFreeWildBcdReplicatedIndex_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdReplicatedIndex = _MscExampleWildBcdOperFreeWildBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1140, 1, 1),
    _MscExampleWildBcdOperFreeWildBcdReplicatedIndex_Type()
)
mscExampleWildBcdOperFreeWildBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdReplicatedIndex.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdReplicatedValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperFreeWildBcdReplicatedValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdOperFreeWildBcdReplicatedValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperFreeWildBcdReplicatedValue_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdReplicatedValue = _MscExampleWildBcdOperFreeWildBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1140, 1, 2),
    _MscExampleWildBcdOperFreeWildBcdReplicatedValue_Type()
)
mscExampleWildBcdOperFreeWildBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdReplicatedValue.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Type = RowStatus
_MscExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdReplicatedRowStatus = _MscExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1140, 1, 3),
    _MscExampleWildBcdOperFreeWildBcdReplicatedRowStatus_Type()
)
mscExampleWildBcdOperFreeWildBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdReplicatedRowStatus.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdListTable_Object = MibTable
mscExampleWildBcdOperFreeWildBcdListTable = _MscExampleWildBcdOperFreeWildBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1141)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdListTable.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdListEntry_Object = MibTableRow
mscExampleWildBcdOperFreeWildBcdListEntry = _MscExampleWildBcdOperFreeWildBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1141, 1)
)
mscExampleWildBcdOperFreeWildBcdListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdOperFreeWildBcdListValue"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdListEntry.setStatus("mandatory")


class _MscExampleWildBcdOperFreeWildBcdListValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdOperFreeWildBcdListValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdOperFreeWildBcdListValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdOperFreeWildBcdListValue_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdListValue = _MscExampleWildBcdOperFreeWildBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1141, 1, 1),
    _MscExampleWildBcdOperFreeWildBcdListValue_Type()
)
mscExampleWildBcdOperFreeWildBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdListValue.setStatus("mandatory")
_MscExampleWildBcdOperFreeWildBcdListRowStatus_Type = RowStatus
_MscExampleWildBcdOperFreeWildBcdListRowStatus_Object = MibTableColumn
mscExampleWildBcdOperFreeWildBcdListRowStatus = _MscExampleWildBcdOperFreeWildBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1141, 1, 2),
    _MscExampleWildBcdOperFreeWildBcdListRowStatus_Type()
)
mscExampleWildBcdOperFreeWildBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleWildBcdOperFreeWildBcdListRowStatus.setStatus("mandatory")
_MscExampleWildBcdProvStructWildBcdVectorTable_Object = MibTable
mscExampleWildBcdProvStructWildBcdVectorTable = _MscExampleWildBcdProvStructWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1142)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdVectorTable.setStatus("mandatory")
_MscExampleWildBcdProvStructWildBcdVectorEntry_Object = MibTableRow
mscExampleWildBcdProvStructWildBcdVectorEntry = _MscExampleWildBcdProvStructWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1142, 1)
)
mscExampleWildBcdProvStructWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvStructWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdVectorEntry.setStatus("mandatory")


class _MscExampleWildBcdProvStructWildBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleWildBcdProvStructWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleWildBcdProvStructWildBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdProvStructWildBcdVectorIndex_Object = MibTableColumn
mscExampleWildBcdProvStructWildBcdVectorIndex = _MscExampleWildBcdProvStructWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1142, 1, 1),
    _MscExampleWildBcdProvStructWildBcdVectorIndex_Type()
)
mscExampleWildBcdProvStructWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdVectorIndex.setStatus("mandatory")


class _MscExampleWildBcdProvStructWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvStructWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdProvStructWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvStructWildBcdVectorValue_Object = MibTableColumn
mscExampleWildBcdProvStructWildBcdVectorValue = _MscExampleWildBcdProvStructWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1142, 1, 2),
    _MscExampleWildBcdProvStructWildBcdVectorValue_Type()
)
mscExampleWildBcdProvStructWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdVectorValue.setStatus("mandatory")
_MscExampleWildBcdProvStructWildBcdArrayTable_Object = MibTable
mscExampleWildBcdProvStructWildBcdArrayTable = _MscExampleWildBcdProvStructWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1143)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdArrayTable.setStatus("mandatory")
_MscExampleWildBcdProvStructWildBcdArrayEntry_Object = MibTableRow
mscExampleWildBcdProvStructWildBcdArrayEntry = _MscExampleWildBcdProvStructWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1143, 1)
)
mscExampleWildBcdProvStructWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvStructWildBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvStructWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdArrayEntry.setStatus("mandatory")


class _MscExampleWildBcdProvStructWildBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleWildBcdProvStructWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleWildBcdProvStructWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdProvStructWildBcdArrayRowIndex_Object = MibTableColumn
mscExampleWildBcdProvStructWildBcdArrayRowIndex = _MscExampleWildBcdProvStructWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1143, 1, 1),
    _MscExampleWildBcdProvStructWildBcdArrayRowIndex_Type()
)
mscExampleWildBcdProvStructWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleWildBcdProvStructWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleWildBcdProvStructWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleWildBcdProvStructWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdProvStructWildBcdArrayColumnIndex_Object = MibTableColumn
mscExampleWildBcdProvStructWildBcdArrayColumnIndex = _MscExampleWildBcdProvStructWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1143, 1, 2),
    _MscExampleWildBcdProvStructWildBcdArrayColumnIndex_Type()
)
mscExampleWildBcdProvStructWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleWildBcdProvStructWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvStructWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdProvStructWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvStructWildBcdArrayValue_Object = MibTableColumn
mscExampleWildBcdProvStructWildBcdArrayValue = _MscExampleWildBcdProvStructWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1143, 1, 3),
    _MscExampleWildBcdProvStructWildBcdArrayValue_Type()
)
mscExampleWildBcdProvStructWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvStructWildBcdArrayValue.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdVectorTable_Object = MibTable
mscExampleWildBcdProvFreeWildBcdVectorTable = _MscExampleWildBcdProvFreeWildBcdVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1144)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdVectorTable.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdVectorEntry_Object = MibTableRow
mscExampleWildBcdProvFreeWildBcdVectorEntry = _MscExampleWildBcdProvFreeWildBcdVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1144, 1)
)
mscExampleWildBcdProvFreeWildBcdVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvFreeWildBcdVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdVectorEntry.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdVectorIndex_Type(Integer32):
    """Custom type mscExampleWildBcdProvFreeWildBcdVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleWildBcdProvFreeWildBcdVectorIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdProvFreeWildBcdVectorIndex_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdVectorIndex = _MscExampleWildBcdProvFreeWildBcdVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1144, 1, 1),
    _MscExampleWildBcdProvFreeWildBcdVectorIndex_Type()
)
mscExampleWildBcdProvFreeWildBcdVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdVectorIndex.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdVectorValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvFreeWildBcdVectorValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdProvFreeWildBcdVectorValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvFreeWildBcdVectorValue_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdVectorValue = _MscExampleWildBcdProvFreeWildBcdVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1144, 1, 2),
    _MscExampleWildBcdProvFreeWildBcdVectorValue_Type()
)
mscExampleWildBcdProvFreeWildBcdVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdVectorValue.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdArrayTable_Object = MibTable
mscExampleWildBcdProvFreeWildBcdArrayTable = _MscExampleWildBcdProvFreeWildBcdArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1145)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdArrayTable.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdArrayEntry_Object = MibTableRow
mscExampleWildBcdProvFreeWildBcdArrayEntry = _MscExampleWildBcdProvFreeWildBcdArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1145, 1)
)
mscExampleWildBcdProvFreeWildBcdArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvFreeWildBcdArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvFreeWildBcdArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdArrayEntry.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdArrayRowIndex_Type(Integer32):
    """Custom type mscExampleWildBcdProvFreeWildBcdArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleWildBcdProvFreeWildBcdArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdProvFreeWildBcdArrayRowIndex_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdArrayRowIndex = _MscExampleWildBcdProvFreeWildBcdArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1145, 1, 1),
    _MscExampleWildBcdProvFreeWildBcdArrayRowIndex_Type()
)
mscExampleWildBcdProvFreeWildBcdArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdArrayRowIndex.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleWildBcdProvFreeWildBcdArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleWildBcdProvFreeWildBcdArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleWildBcdProvFreeWildBcdArrayColumnIndex_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdArrayColumnIndex = _MscExampleWildBcdProvFreeWildBcdArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1145, 1, 2),
    _MscExampleWildBcdProvFreeWildBcdArrayColumnIndex_Type()
)
mscExampleWildBcdProvFreeWildBcdArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdArrayColumnIndex.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdArrayValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvFreeWildBcdArrayValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdProvFreeWildBcdArrayValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvFreeWildBcdArrayValue_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdArrayValue = _MscExampleWildBcdProvFreeWildBcdArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1145, 1, 3),
    _MscExampleWildBcdProvFreeWildBcdArrayValue_Type()
)
mscExampleWildBcdProvFreeWildBcdArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdArrayValue.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdReplicatedTable_Object = MibTable
mscExampleWildBcdProvFreeWildBcdReplicatedTable = _MscExampleWildBcdProvFreeWildBcdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1146)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdReplicatedTable.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdReplicatedEntry_Object = MibTableRow
mscExampleWildBcdProvFreeWildBcdReplicatedEntry = _MscExampleWildBcdProvFreeWildBcdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1146, 1)
)
mscExampleWildBcdProvFreeWildBcdReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvFreeWildBcdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdReplicatedEntry.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdReplicatedIndex_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvFreeWildBcdReplicatedIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_MscExampleWildBcdProvFreeWildBcdReplicatedIndex_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvFreeWildBcdReplicatedIndex_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdReplicatedIndex = _MscExampleWildBcdProvFreeWildBcdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1146, 1, 1),
    _MscExampleWildBcdProvFreeWildBcdReplicatedIndex_Type()
)
mscExampleWildBcdProvFreeWildBcdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdReplicatedIndex.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdReplicatedValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvFreeWildBcdReplicatedValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdProvFreeWildBcdReplicatedValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvFreeWildBcdReplicatedValue_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdReplicatedValue = _MscExampleWildBcdProvFreeWildBcdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1146, 1, 2),
    _MscExampleWildBcdProvFreeWildBcdReplicatedValue_Type()
)
mscExampleWildBcdProvFreeWildBcdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdReplicatedValue.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Type = RowStatus
_MscExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdReplicatedRowStatus = _MscExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1146, 1, 3),
    _MscExampleWildBcdProvFreeWildBcdReplicatedRowStatus_Type()
)
mscExampleWildBcdProvFreeWildBcdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdReplicatedRowStatus.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdListTable_Object = MibTable
mscExampleWildBcdProvFreeWildBcdListTable = _MscExampleWildBcdProvFreeWildBcdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1147)
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdListTable.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdListEntry_Object = MibTableRow
mscExampleWildBcdProvFreeWildBcdListEntry = _MscExampleWildBcdProvFreeWildBcdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1147, 1)
)
mscExampleWildBcdProvFreeWildBcdListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleWildBcdProvFreeWildBcdListValue"),
)
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdListEntry.setStatus("mandatory")


class _MscExampleWildBcdProvFreeWildBcdListValue_Type(WildcardedDigitString):
    """Custom type mscExampleWildBcdProvFreeWildBcdListValue based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscExampleWildBcdProvFreeWildBcdListValue_Type.__name__ = "WildcardedDigitString"
_MscExampleWildBcdProvFreeWildBcdListValue_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdListValue = _MscExampleWildBcdProvFreeWildBcdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1147, 1, 1),
    _MscExampleWildBcdProvFreeWildBcdListValue_Type()
)
mscExampleWildBcdProvFreeWildBcdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdListValue.setStatus("mandatory")
_MscExampleWildBcdProvFreeWildBcdListRowStatus_Type = RowStatus
_MscExampleWildBcdProvFreeWildBcdListRowStatus_Object = MibTableColumn
mscExampleWildBcdProvFreeWildBcdListRowStatus = _MscExampleWildBcdProvFreeWildBcdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 10, 1147, 1, 2),
    _MscExampleWildBcdProvFreeWildBcdListRowStatus_Type()
)
mscExampleWildBcdProvFreeWildBcdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleWildBcdProvFreeWildBcdListRowStatus.setStatus("mandatory")
_MscExampleEnum_ObjectIdentity = ObjectIdentity
mscExampleEnum = _MscExampleEnum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11)
)
_MscExampleEnumRowStatusTable_Object = MibTable
mscExampleEnumRowStatusTable = _MscExampleEnumRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1)
)
if mibBuilder.loadTexts:
    mscExampleEnumRowStatusTable.setStatus("mandatory")
_MscExampleEnumRowStatusEntry_Object = MibTableRow
mscExampleEnumRowStatusEntry = _MscExampleEnumRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1, 1)
)
mscExampleEnumRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumRowStatusEntry.setStatus("mandatory")
_MscExampleEnumRowStatus_Type = RowStatus
_MscExampleEnumRowStatus_Object = MibTableColumn
mscExampleEnumRowStatus = _MscExampleEnumRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1, 1, 1),
    _MscExampleEnumRowStatus_Type()
)
mscExampleEnumRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumRowStatus.setStatus("mandatory")
_MscExampleEnumComponentName_Type = DisplayString
_MscExampleEnumComponentName_Object = MibTableColumn
mscExampleEnumComponentName = _MscExampleEnumComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1, 1, 2),
    _MscExampleEnumComponentName_Type()
)
mscExampleEnumComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleEnumComponentName.setStatus("mandatory")
_MscExampleEnumStorageType_Type = StorageType
_MscExampleEnumStorageType_Object = MibTableColumn
mscExampleEnumStorageType = _MscExampleEnumStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1, 1, 4),
    _MscExampleEnumStorageType_Type()
)
mscExampleEnumStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleEnumStorageType.setStatus("mandatory")


class _MscExampleEnumIndex_Type(Integer32):
    """Custom type mscExampleEnumIndex based on Integer32"""
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


_MscExampleEnumIndex_Type.__name__ = "Integer32"
_MscExampleEnumIndex_Object = MibTableColumn
mscExampleEnumIndex = _MscExampleEnumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1, 1, 10),
    _MscExampleEnumIndex_Type()
)
mscExampleEnumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumIndex.setStatus("mandatory")
_MscExampleEnumOperationalTable_Object = MibTable
mscExampleEnumOperationalTable = _MscExampleEnumOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 10)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperationalTable.setStatus("mandatory")
_MscExampleEnumOperationalEntry_Object = MibTableRow
mscExampleEnumOperationalEntry = _MscExampleEnumOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 10, 1)
)
mscExampleEnumOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperationalEntry.setStatus("mandatory")


class _MscExampleEnumOperStructEnum_Type(Integer32):
    """Custom type mscExampleEnumOperStructEnum based on Integer32"""
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


_MscExampleEnumOperStructEnum_Type.__name__ = "Integer32"
_MscExampleEnumOperStructEnum_Object = MibTableColumn
mscExampleEnumOperStructEnum = _MscExampleEnumOperStructEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 10, 1, 1),
    _MscExampleEnumOperStructEnum_Type()
)
mscExampleEnumOperStructEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnum.setStatus("mandatory")


class _MscExampleEnumOperStructEnumSet_Type(OctetString):
    """Custom type mscExampleEnumOperStructEnumSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscExampleEnumOperStructEnumSet_Type.__name__ = "OctetString"
_MscExampleEnumOperStructEnumSet_Object = MibTableColumn
mscExampleEnumOperStructEnumSet = _MscExampleEnumOperStructEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 10, 1, 2),
    _MscExampleEnumOperStructEnumSet_Type()
)
mscExampleEnumOperStructEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumSet.setStatus("mandatory")


class _MscExampleEnumOperFreeEnum_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnum based on Integer32"""
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


_MscExampleEnumOperFreeEnum_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnum_Object = MibTableColumn
mscExampleEnumOperFreeEnum = _MscExampleEnumOperFreeEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 10, 1, 3),
    _MscExampleEnumOperFreeEnum_Type()
)
mscExampleEnumOperFreeEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnum.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumSet_Type(OctetString):
    """Custom type mscExampleEnumOperFreeEnumSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscExampleEnumOperFreeEnumSet_Type.__name__ = "OctetString"
_MscExampleEnumOperFreeEnumSet_Object = MibTableColumn
mscExampleEnumOperFreeEnumSet = _MscExampleEnumOperFreeEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 10, 1, 4),
    _MscExampleEnumOperFreeEnumSet_Type()
)
mscExampleEnumOperFreeEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumSet.setStatus("mandatory")
_MscExampleEnumProvisionalTable_Object = MibTable
mscExampleEnumProvisionalTable = _MscExampleEnumProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvisionalTable.setStatus("mandatory")
_MscExampleEnumProvisionalEntry_Object = MibTableRow
mscExampleEnumProvisionalEntry = _MscExampleEnumProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1)
)
mscExampleEnumProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvisionalEntry.setStatus("mandatory")
_MscExampleEnumProvEnumSub_Type = Link
_MscExampleEnumProvEnumSub_Object = MibTableColumn
mscExampleEnumProvEnumSub = _MscExampleEnumProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 1),
    _MscExampleEnumProvEnumSub_Type()
)
mscExampleEnumProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvEnumSub.setStatus("mandatory")


class _MscExampleEnumProvStructEnum_Type(Integer32):
    """Custom type mscExampleEnumProvStructEnum based on Integer32"""
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


_MscExampleEnumProvStructEnum_Type.__name__ = "Integer32"
_MscExampleEnumProvStructEnum_Object = MibTableColumn
mscExampleEnumProvStructEnum = _MscExampleEnumProvStructEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 2),
    _MscExampleEnumProvStructEnum_Type()
)
mscExampleEnumProvStructEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnum.setStatus("mandatory")


class _MscExampleEnumProvStructEnumSet_Type(OctetString):
    """Custom type mscExampleEnumProvStructEnumSet based on OctetString"""
    defaultHexValue = "aa"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscExampleEnumProvStructEnumSet_Type.__name__ = "OctetString"
_MscExampleEnumProvStructEnumSet_Object = MibTableColumn
mscExampleEnumProvStructEnumSet = _MscExampleEnumProvStructEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 3),
    _MscExampleEnumProvStructEnumSet_Type()
)
mscExampleEnumProvStructEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumSet.setStatus("mandatory")


class _MscExampleEnumProvFreeEnum_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnum based on Integer32"""
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


_MscExampleEnumProvFreeEnum_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnum_Object = MibTableColumn
mscExampleEnumProvFreeEnum = _MscExampleEnumProvFreeEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 4),
    _MscExampleEnumProvFreeEnum_Type()
)
mscExampleEnumProvFreeEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnum.setStatus("mandatory")


class _MscExampleEnumProvFreeEnum1_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnum1 based on Integer32"""
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


_MscExampleEnumProvFreeEnum1_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnum1_Object = MibTableColumn
mscExampleEnumProvFreeEnum1 = _MscExampleEnumProvFreeEnum1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 5),
    _MscExampleEnumProvFreeEnum1_Type()
)
mscExampleEnumProvFreeEnum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnum1.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumSet_Type(OctetString):
    """Custom type mscExampleEnumProvFreeEnumSet based on OctetString"""
    defaultHexValue = "0070"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscExampleEnumProvFreeEnumSet_Type.__name__ = "OctetString"
_MscExampleEnumProvFreeEnumSet_Object = MibTableColumn
mscExampleEnumProvFreeEnumSet = _MscExampleEnumProvFreeEnumSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 6),
    _MscExampleEnumProvFreeEnumSet_Type()
)
mscExampleEnumProvFreeEnumSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumSet.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumSet1_Type(OctetString):
    """Custom type mscExampleEnumProvFreeEnumSet1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscExampleEnumProvFreeEnumSet1_Type.__name__ = "OctetString"
_MscExampleEnumProvFreeEnumSet1_Object = MibTableColumn
mscExampleEnumProvFreeEnumSet1 = _MscExampleEnumProvFreeEnumSet1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 11, 1, 7),
    _MscExampleEnumProvFreeEnumSet1_Type()
)
mscExampleEnumProvFreeEnumSet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumSet1.setStatus("mandatory")
_MscExampleEnumOperStructEnumVectorTable_Object = MibTable
mscExampleEnumOperStructEnumVectorTable = _MscExampleEnumOperStructEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1162)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumVectorTable.setStatus("mandatory")
_MscExampleEnumOperStructEnumVectorEntry_Object = MibTableRow
mscExampleEnumOperStructEnumVectorEntry = _MscExampleEnumOperStructEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1162, 1)
)
mscExampleEnumOperStructEnumVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperStructEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumVectorEntry.setStatus("mandatory")


class _MscExampleEnumOperStructEnumVectorIndex_Type(Integer32):
    """Custom type mscExampleEnumOperStructEnumVectorIndex based on Integer32"""
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


_MscExampleEnumOperStructEnumVectorIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperStructEnumVectorIndex_Object = MibTableColumn
mscExampleEnumOperStructEnumVectorIndex = _MscExampleEnumOperStructEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1162, 1, 1),
    _MscExampleEnumOperStructEnumVectorIndex_Type()
)
mscExampleEnumOperStructEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumVectorIndex.setStatus("mandatory")


class _MscExampleEnumOperStructEnumVectorValue_Type(Integer32):
    """Custom type mscExampleEnumOperStructEnumVectorValue based on Integer32"""
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


_MscExampleEnumOperStructEnumVectorValue_Type.__name__ = "Integer32"
_MscExampleEnumOperStructEnumVectorValue_Object = MibTableColumn
mscExampleEnumOperStructEnumVectorValue = _MscExampleEnumOperStructEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1162, 1, 2),
    _MscExampleEnumOperStructEnumVectorValue_Type()
)
mscExampleEnumOperStructEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumVectorValue.setStatus("mandatory")
_MscExampleEnumOperStructEnumArrayTable_Object = MibTable
mscExampleEnumOperStructEnumArrayTable = _MscExampleEnumOperStructEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1163)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumArrayTable.setStatus("mandatory")
_MscExampleEnumOperStructEnumArrayEntry_Object = MibTableRow
mscExampleEnumOperStructEnumArrayEntry = _MscExampleEnumOperStructEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1163, 1)
)
mscExampleEnumOperStructEnumArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperStructEnumArrayMonthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperStructEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumArrayEntry.setStatus("mandatory")


class _MscExampleEnumOperStructEnumArrayMonthIndex_Type(Integer32):
    """Custom type mscExampleEnumOperStructEnumArrayMonthIndex based on Integer32"""
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


_MscExampleEnumOperStructEnumArrayMonthIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperStructEnumArrayMonthIndex_Object = MibTableColumn
mscExampleEnumOperStructEnumArrayMonthIndex = _MscExampleEnumOperStructEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1163, 1, 1),
    _MscExampleEnumOperStructEnumArrayMonthIndex_Type()
)
mscExampleEnumOperStructEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumArrayMonthIndex.setStatus("mandatory")


class _MscExampleEnumOperStructEnumArrayDayIndex_Type(Integer32):
    """Custom type mscExampleEnumOperStructEnumArrayDayIndex based on Integer32"""
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


_MscExampleEnumOperStructEnumArrayDayIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperStructEnumArrayDayIndex_Object = MibTableColumn
mscExampleEnumOperStructEnumArrayDayIndex = _MscExampleEnumOperStructEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1163, 1, 2),
    _MscExampleEnumOperStructEnumArrayDayIndex_Type()
)
mscExampleEnumOperStructEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumArrayDayIndex.setStatus("mandatory")


class _MscExampleEnumOperStructEnumArrayValue_Type(Integer32):
    """Custom type mscExampleEnumOperStructEnumArrayValue based on Integer32"""
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


_MscExampleEnumOperStructEnumArrayValue_Type.__name__ = "Integer32"
_MscExampleEnumOperStructEnumArrayValue_Object = MibTableColumn
mscExampleEnumOperStructEnumArrayValue = _MscExampleEnumOperStructEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1163, 1, 3),
    _MscExampleEnumOperStructEnumArrayValue_Type()
)
mscExampleEnumOperStructEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperStructEnumArrayValue.setStatus("mandatory")
_MscExampleEnumOperFreeEnumVectorTable_Object = MibTable
mscExampleEnumOperFreeEnumVectorTable = _MscExampleEnumOperFreeEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1164)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumVectorTable.setStatus("mandatory")
_MscExampleEnumOperFreeEnumVectorEntry_Object = MibTableRow
mscExampleEnumOperFreeEnumVectorEntry = _MscExampleEnumOperFreeEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1164, 1)
)
mscExampleEnumOperFreeEnumVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperFreeEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumVectorEntry.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumVectorIndex_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumVectorIndex based on Integer32"""
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


_MscExampleEnumOperFreeEnumVectorIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumVectorIndex_Object = MibTableColumn
mscExampleEnumOperFreeEnumVectorIndex = _MscExampleEnumOperFreeEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1164, 1, 1),
    _MscExampleEnumOperFreeEnumVectorIndex_Type()
)
mscExampleEnumOperFreeEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumVectorIndex.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumVectorValue_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumVectorValue based on Integer32"""
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


_MscExampleEnumOperFreeEnumVectorValue_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumVectorValue_Object = MibTableColumn
mscExampleEnumOperFreeEnumVectorValue = _MscExampleEnumOperFreeEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1164, 1, 2),
    _MscExampleEnumOperFreeEnumVectorValue_Type()
)
mscExampleEnumOperFreeEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumVectorValue.setStatus("mandatory")
_MscExampleEnumOperFreeEnumArrayTable_Object = MibTable
mscExampleEnumOperFreeEnumArrayTable = _MscExampleEnumOperFreeEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1165)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumArrayTable.setStatus("mandatory")
_MscExampleEnumOperFreeEnumArrayEntry_Object = MibTableRow
mscExampleEnumOperFreeEnumArrayEntry = _MscExampleEnumOperFreeEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1165, 1)
)
mscExampleEnumOperFreeEnumArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperFreeEnumArrayMonthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperFreeEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumArrayEntry.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumArrayMonthIndex_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumArrayMonthIndex based on Integer32"""
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


_MscExampleEnumOperFreeEnumArrayMonthIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumArrayMonthIndex_Object = MibTableColumn
mscExampleEnumOperFreeEnumArrayMonthIndex = _MscExampleEnumOperFreeEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1165, 1, 1),
    _MscExampleEnumOperFreeEnumArrayMonthIndex_Type()
)
mscExampleEnumOperFreeEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumArrayMonthIndex.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumArrayDayIndex_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumArrayDayIndex based on Integer32"""
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


_MscExampleEnumOperFreeEnumArrayDayIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumArrayDayIndex_Object = MibTableColumn
mscExampleEnumOperFreeEnumArrayDayIndex = _MscExampleEnumOperFreeEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1165, 1, 2),
    _MscExampleEnumOperFreeEnumArrayDayIndex_Type()
)
mscExampleEnumOperFreeEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumArrayDayIndex.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumArrayValue_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumArrayValue based on Integer32"""
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


_MscExampleEnumOperFreeEnumArrayValue_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumArrayValue_Object = MibTableColumn
mscExampleEnumOperFreeEnumArrayValue = _MscExampleEnumOperFreeEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1165, 1, 3),
    _MscExampleEnumOperFreeEnumArrayValue_Type()
)
mscExampleEnumOperFreeEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumArrayValue.setStatus("mandatory")
_MscExampleEnumOperFreeEnumReplicatedTable_Object = MibTable
mscExampleEnumOperFreeEnumReplicatedTable = _MscExampleEnumOperFreeEnumReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1166)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumReplicatedTable.setStatus("mandatory")
_MscExampleEnumOperFreeEnumReplicatedEntry_Object = MibTableRow
mscExampleEnumOperFreeEnumReplicatedEntry = _MscExampleEnumOperFreeEnumReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1166, 1)
)
mscExampleEnumOperFreeEnumReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperFreeEnumReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumReplicatedEntry.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumReplicatedIndex_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumReplicatedIndex based on Integer32"""
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


_MscExampleEnumOperFreeEnumReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumReplicatedIndex_Object = MibTableColumn
mscExampleEnumOperFreeEnumReplicatedIndex = _MscExampleEnumOperFreeEnumReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1166, 1, 1),
    _MscExampleEnumOperFreeEnumReplicatedIndex_Type()
)
mscExampleEnumOperFreeEnumReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumReplicatedIndex.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumReplicatedValue_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumReplicatedValue based on Integer32"""
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


_MscExampleEnumOperFreeEnumReplicatedValue_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumReplicatedValue_Object = MibTableColumn
mscExampleEnumOperFreeEnumReplicatedValue = _MscExampleEnumOperFreeEnumReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1166, 1, 2),
    _MscExampleEnumOperFreeEnumReplicatedValue_Type()
)
mscExampleEnumOperFreeEnumReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumReplicatedValue.setStatus("mandatory")
_MscExampleEnumOperFreeEnumReplicatedRowStatus_Type = RowStatus
_MscExampleEnumOperFreeEnumReplicatedRowStatus_Object = MibTableColumn
mscExampleEnumOperFreeEnumReplicatedRowStatus = _MscExampleEnumOperFreeEnumReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1166, 1, 3),
    _MscExampleEnumOperFreeEnumReplicatedRowStatus_Type()
)
mscExampleEnumOperFreeEnumReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumReplicatedRowStatus.setStatus("mandatory")
_MscExampleEnumOperFreeEnumListTable_Object = MibTable
mscExampleEnumOperFreeEnumListTable = _MscExampleEnumOperFreeEnumListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1167)
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumListTable.setStatus("mandatory")
_MscExampleEnumOperFreeEnumListEntry_Object = MibTableRow
mscExampleEnumOperFreeEnumListEntry = _MscExampleEnumOperFreeEnumListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1167, 1)
)
mscExampleEnumOperFreeEnumListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumOperFreeEnumListValue"),
)
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumListEntry.setStatus("mandatory")


class _MscExampleEnumOperFreeEnumListValue_Type(Integer32):
    """Custom type mscExampleEnumOperFreeEnumListValue based on Integer32"""
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


_MscExampleEnumOperFreeEnumListValue_Type.__name__ = "Integer32"
_MscExampleEnumOperFreeEnumListValue_Object = MibTableColumn
mscExampleEnumOperFreeEnumListValue = _MscExampleEnumOperFreeEnumListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1167, 1, 1),
    _MscExampleEnumOperFreeEnumListValue_Type()
)
mscExampleEnumOperFreeEnumListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumListValue.setStatus("mandatory")
_MscExampleEnumOperFreeEnumListRowStatus_Type = RowStatus
_MscExampleEnumOperFreeEnumListRowStatus_Object = MibTableColumn
mscExampleEnumOperFreeEnumListRowStatus = _MscExampleEnumOperFreeEnumListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1167, 1, 2),
    _MscExampleEnumOperFreeEnumListRowStatus_Type()
)
mscExampleEnumOperFreeEnumListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleEnumOperFreeEnumListRowStatus.setStatus("mandatory")
_MscExampleEnumProvStructEnumVectorTable_Object = MibTable
mscExampleEnumProvStructEnumVectorTable = _MscExampleEnumProvStructEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1168)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumVectorTable.setStatus("mandatory")
_MscExampleEnumProvStructEnumVectorEntry_Object = MibTableRow
mscExampleEnumProvStructEnumVectorEntry = _MscExampleEnumProvStructEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1168, 1)
)
mscExampleEnumProvStructEnumVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvStructEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumVectorEntry.setStatus("mandatory")


class _MscExampleEnumProvStructEnumVectorIndex_Type(Integer32):
    """Custom type mscExampleEnumProvStructEnumVectorIndex based on Integer32"""
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


_MscExampleEnumProvStructEnumVectorIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvStructEnumVectorIndex_Object = MibTableColumn
mscExampleEnumProvStructEnumVectorIndex = _MscExampleEnumProvStructEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1168, 1, 1),
    _MscExampleEnumProvStructEnumVectorIndex_Type()
)
mscExampleEnumProvStructEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumVectorIndex.setStatus("mandatory")


class _MscExampleEnumProvStructEnumVectorValue_Type(Integer32):
    """Custom type mscExampleEnumProvStructEnumVectorValue based on Integer32"""
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


_MscExampleEnumProvStructEnumVectorValue_Type.__name__ = "Integer32"
_MscExampleEnumProvStructEnumVectorValue_Object = MibTableColumn
mscExampleEnumProvStructEnumVectorValue = _MscExampleEnumProvStructEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1168, 1, 2),
    _MscExampleEnumProvStructEnumVectorValue_Type()
)
mscExampleEnumProvStructEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumVectorValue.setStatus("mandatory")
_MscExampleEnumProvStructEnumArrayTable_Object = MibTable
mscExampleEnumProvStructEnumArrayTable = _MscExampleEnumProvStructEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1169)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumArrayTable.setStatus("mandatory")
_MscExampleEnumProvStructEnumArrayEntry_Object = MibTableRow
mscExampleEnumProvStructEnumArrayEntry = _MscExampleEnumProvStructEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1169, 1)
)
mscExampleEnumProvStructEnumArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvStructEnumArrayMonthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvStructEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumArrayEntry.setStatus("mandatory")


class _MscExampleEnumProvStructEnumArrayMonthIndex_Type(Integer32):
    """Custom type mscExampleEnumProvStructEnumArrayMonthIndex based on Integer32"""
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


_MscExampleEnumProvStructEnumArrayMonthIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvStructEnumArrayMonthIndex_Object = MibTableColumn
mscExampleEnumProvStructEnumArrayMonthIndex = _MscExampleEnumProvStructEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1169, 1, 1),
    _MscExampleEnumProvStructEnumArrayMonthIndex_Type()
)
mscExampleEnumProvStructEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumArrayMonthIndex.setStatus("mandatory")


class _MscExampleEnumProvStructEnumArrayDayIndex_Type(Integer32):
    """Custom type mscExampleEnumProvStructEnumArrayDayIndex based on Integer32"""
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


_MscExampleEnumProvStructEnumArrayDayIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvStructEnumArrayDayIndex_Object = MibTableColumn
mscExampleEnumProvStructEnumArrayDayIndex = _MscExampleEnumProvStructEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1169, 1, 2),
    _MscExampleEnumProvStructEnumArrayDayIndex_Type()
)
mscExampleEnumProvStructEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumArrayDayIndex.setStatus("mandatory")


class _MscExampleEnumProvStructEnumArrayValue_Type(Integer32):
    """Custom type mscExampleEnumProvStructEnumArrayValue based on Integer32"""
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


_MscExampleEnumProvStructEnumArrayValue_Type.__name__ = "Integer32"
_MscExampleEnumProvStructEnumArrayValue_Object = MibTableColumn
mscExampleEnumProvStructEnumArrayValue = _MscExampleEnumProvStructEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1169, 1, 3),
    _MscExampleEnumProvStructEnumArrayValue_Type()
)
mscExampleEnumProvStructEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvStructEnumArrayValue.setStatus("mandatory")
_MscExampleEnumProvFreeEnumVectorTable_Object = MibTable
mscExampleEnumProvFreeEnumVectorTable = _MscExampleEnumProvFreeEnumVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1170)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVectorTable.setStatus("mandatory")
_MscExampleEnumProvFreeEnumVectorEntry_Object = MibTableRow
mscExampleEnumProvFreeEnumVectorEntry = _MscExampleEnumProvFreeEnumVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1170, 1)
)
mscExampleEnumProvFreeEnumVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVectorEntry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumVectorIndex_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumVectorIndex based on Integer32"""
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


_MscExampleEnumProvFreeEnumVectorIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumVectorIndex_Object = MibTableColumn
mscExampleEnumProvFreeEnumVectorIndex = _MscExampleEnumProvFreeEnumVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1170, 1, 1),
    _MscExampleEnumProvFreeEnumVectorIndex_Type()
)
mscExampleEnumProvFreeEnumVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVectorIndex.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumVectorValue_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumVectorValue based on Integer32"""
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


_MscExampleEnumProvFreeEnumVectorValue_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumVectorValue_Object = MibTableColumn
mscExampleEnumProvFreeEnumVectorValue = _MscExampleEnumProvFreeEnumVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1170, 1, 2),
    _MscExampleEnumProvFreeEnumVectorValue_Type()
)
mscExampleEnumProvFreeEnumVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVectorValue.setStatus("mandatory")
_MscExampleEnumProvFreeEnumVector1Table_Object = MibTable
mscExampleEnumProvFreeEnumVector1Table = _MscExampleEnumProvFreeEnumVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1171)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVector1Table.setStatus("mandatory")
_MscExampleEnumProvFreeEnumVector1Entry_Object = MibTableRow
mscExampleEnumProvFreeEnumVector1Entry = _MscExampleEnumProvFreeEnumVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1171, 1)
)
mscExampleEnumProvFreeEnumVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVector1Entry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumVector1Index_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumVector1Index based on Integer32"""
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


_MscExampleEnumProvFreeEnumVector1Index_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumVector1Index_Object = MibTableColumn
mscExampleEnumProvFreeEnumVector1Index = _MscExampleEnumProvFreeEnumVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1171, 1, 1),
    _MscExampleEnumProvFreeEnumVector1Index_Type()
)
mscExampleEnumProvFreeEnumVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVector1Index.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumVector1Value_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumVector1Value based on Integer32"""
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


_MscExampleEnumProvFreeEnumVector1Value_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumVector1Value_Object = MibTableColumn
mscExampleEnumProvFreeEnumVector1Value = _MscExampleEnumProvFreeEnumVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1171, 1, 2),
    _MscExampleEnumProvFreeEnumVector1Value_Type()
)
mscExampleEnumProvFreeEnumVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumVector1Value.setStatus("mandatory")
_MscExampleEnumProvFreeEnumArrayTable_Object = MibTable
mscExampleEnumProvFreeEnumArrayTable = _MscExampleEnumProvFreeEnumArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1172)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArrayTable.setStatus("mandatory")
_MscExampleEnumProvFreeEnumArrayEntry_Object = MibTableRow
mscExampleEnumProvFreeEnumArrayEntry = _MscExampleEnumProvFreeEnumArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1172, 1)
)
mscExampleEnumProvFreeEnumArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumArrayMonthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumArrayDayIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArrayEntry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumArrayMonthIndex_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumArrayMonthIndex based on Integer32"""
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


_MscExampleEnumProvFreeEnumArrayMonthIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumArrayMonthIndex_Object = MibTableColumn
mscExampleEnumProvFreeEnumArrayMonthIndex = _MscExampleEnumProvFreeEnumArrayMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1172, 1, 1),
    _MscExampleEnumProvFreeEnumArrayMonthIndex_Type()
)
mscExampleEnumProvFreeEnumArrayMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArrayMonthIndex.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumArrayDayIndex_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumArrayDayIndex based on Integer32"""
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


_MscExampleEnumProvFreeEnumArrayDayIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumArrayDayIndex_Object = MibTableColumn
mscExampleEnumProvFreeEnumArrayDayIndex = _MscExampleEnumProvFreeEnumArrayDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1172, 1, 2),
    _MscExampleEnumProvFreeEnumArrayDayIndex_Type()
)
mscExampleEnumProvFreeEnumArrayDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArrayDayIndex.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumArrayValue_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumArrayValue based on Integer32"""
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


_MscExampleEnumProvFreeEnumArrayValue_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumArrayValue_Object = MibTableColumn
mscExampleEnumProvFreeEnumArrayValue = _MscExampleEnumProvFreeEnumArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1172, 1, 3),
    _MscExampleEnumProvFreeEnumArrayValue_Type()
)
mscExampleEnumProvFreeEnumArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArrayValue.setStatus("mandatory")
_MscExampleEnumProvFreeEnumArray1Table_Object = MibTable
mscExampleEnumProvFreeEnumArray1Table = _MscExampleEnumProvFreeEnumArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1173)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArray1Table.setStatus("mandatory")
_MscExampleEnumProvFreeEnumArray1Entry_Object = MibTableRow
mscExampleEnumProvFreeEnumArray1Entry = _MscExampleEnumProvFreeEnumArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1173, 1)
)
mscExampleEnumProvFreeEnumArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumArray1MonthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumArray1DayIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArray1Entry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumArray1MonthIndex_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumArray1MonthIndex based on Integer32"""
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


_MscExampleEnumProvFreeEnumArray1MonthIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumArray1MonthIndex_Object = MibTableColumn
mscExampleEnumProvFreeEnumArray1MonthIndex = _MscExampleEnumProvFreeEnumArray1MonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1173, 1, 1),
    _MscExampleEnumProvFreeEnumArray1MonthIndex_Type()
)
mscExampleEnumProvFreeEnumArray1MonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArray1MonthIndex.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumArray1DayIndex_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumArray1DayIndex based on Integer32"""
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


_MscExampleEnumProvFreeEnumArray1DayIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumArray1DayIndex_Object = MibTableColumn
mscExampleEnumProvFreeEnumArray1DayIndex = _MscExampleEnumProvFreeEnumArray1DayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1173, 1, 2),
    _MscExampleEnumProvFreeEnumArray1DayIndex_Type()
)
mscExampleEnumProvFreeEnumArray1DayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArray1DayIndex.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumArray1Value_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumArray1Value based on Integer32"""
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


_MscExampleEnumProvFreeEnumArray1Value_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumArray1Value_Object = MibTableColumn
mscExampleEnumProvFreeEnumArray1Value = _MscExampleEnumProvFreeEnumArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1173, 1, 3),
    _MscExampleEnumProvFreeEnumArray1Value_Type()
)
mscExampleEnumProvFreeEnumArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumArray1Value.setStatus("mandatory")
_MscExampleEnumProvFreeEnumReplicatedTable_Object = MibTable
mscExampleEnumProvFreeEnumReplicatedTable = _MscExampleEnumProvFreeEnumReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1174)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumReplicatedTable.setStatus("mandatory")
_MscExampleEnumProvFreeEnumReplicatedEntry_Object = MibTableRow
mscExampleEnumProvFreeEnumReplicatedEntry = _MscExampleEnumProvFreeEnumReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1174, 1)
)
mscExampleEnumProvFreeEnumReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumReplicatedEntry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumReplicatedIndex_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumReplicatedIndex based on Integer32"""
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


_MscExampleEnumProvFreeEnumReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumReplicatedIndex_Object = MibTableColumn
mscExampleEnumProvFreeEnumReplicatedIndex = _MscExampleEnumProvFreeEnumReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1174, 1, 1),
    _MscExampleEnumProvFreeEnumReplicatedIndex_Type()
)
mscExampleEnumProvFreeEnumReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumReplicatedIndex.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumReplicatedValue_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumReplicatedValue based on Integer32"""
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


_MscExampleEnumProvFreeEnumReplicatedValue_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumReplicatedValue_Object = MibTableColumn
mscExampleEnumProvFreeEnumReplicatedValue = _MscExampleEnumProvFreeEnumReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1174, 1, 2),
    _MscExampleEnumProvFreeEnumReplicatedValue_Type()
)
mscExampleEnumProvFreeEnumReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumReplicatedValue.setStatus("mandatory")
_MscExampleEnumProvFreeEnumReplicatedRowStatus_Type = RowStatus
_MscExampleEnumProvFreeEnumReplicatedRowStatus_Object = MibTableColumn
mscExampleEnumProvFreeEnumReplicatedRowStatus = _MscExampleEnumProvFreeEnumReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1174, 1, 3),
    _MscExampleEnumProvFreeEnumReplicatedRowStatus_Type()
)
mscExampleEnumProvFreeEnumReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumReplicatedRowStatus.setStatus("mandatory")
_MscExampleEnumProvFreeEnumListTable_Object = MibTable
mscExampleEnumProvFreeEnumListTable = _MscExampleEnumProvFreeEnumListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1175)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumListTable.setStatus("mandatory")
_MscExampleEnumProvFreeEnumListEntry_Object = MibTableRow
mscExampleEnumProvFreeEnumListEntry = _MscExampleEnumProvFreeEnumListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1175, 1)
)
mscExampleEnumProvFreeEnumListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumListValue"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumListEntry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumListValue_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumListValue based on Integer32"""
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


_MscExampleEnumProvFreeEnumListValue_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumListValue_Object = MibTableColumn
mscExampleEnumProvFreeEnumListValue = _MscExampleEnumProvFreeEnumListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1175, 1, 1),
    _MscExampleEnumProvFreeEnumListValue_Type()
)
mscExampleEnumProvFreeEnumListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumListValue.setStatus("mandatory")
_MscExampleEnumProvFreeEnumListRowStatus_Type = RowStatus
_MscExampleEnumProvFreeEnumListRowStatus_Object = MibTableColumn
mscExampleEnumProvFreeEnumListRowStatus = _MscExampleEnumProvFreeEnumListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1175, 1, 2),
    _MscExampleEnumProvFreeEnumListRowStatus_Type()
)
mscExampleEnumProvFreeEnumListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumListRowStatus.setStatus("mandatory")
_MscExampleEnumProvFreeEnumList1Table_Object = MibTable
mscExampleEnumProvFreeEnumList1Table = _MscExampleEnumProvFreeEnumList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1176)
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumList1Table.setStatus("mandatory")
_MscExampleEnumProvFreeEnumList1Entry_Object = MibTableRow
mscExampleEnumProvFreeEnumList1Entry = _MscExampleEnumProvFreeEnumList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1176, 1)
)
mscExampleEnumProvFreeEnumList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumProvFreeEnumList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumList1Entry.setStatus("mandatory")


class _MscExampleEnumProvFreeEnumList1Value_Type(Integer32):
    """Custom type mscExampleEnumProvFreeEnumList1Value based on Integer32"""
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


_MscExampleEnumProvFreeEnumList1Value_Type.__name__ = "Integer32"
_MscExampleEnumProvFreeEnumList1Value_Object = MibTableColumn
mscExampleEnumProvFreeEnumList1Value = _MscExampleEnumProvFreeEnumList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1176, 1, 1),
    _MscExampleEnumProvFreeEnumList1Value_Type()
)
mscExampleEnumProvFreeEnumList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumList1Value.setStatus("mandatory")
_MscExampleEnumProvFreeEnumList1RowStatus_Type = RowStatus
_MscExampleEnumProvFreeEnumList1RowStatus_Object = MibTableColumn
mscExampleEnumProvFreeEnumList1RowStatus = _MscExampleEnumProvFreeEnumList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 11, 1176, 1, 2),
    _MscExampleEnumProvFreeEnumList1RowStatus_Type()
)
mscExampleEnumProvFreeEnumList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleEnumProvFreeEnumList1RowStatus.setStatus("mandatory")
_MscExampleObjectId_ObjectIdentity = ObjectIdentity
mscExampleObjectId = _MscExampleObjectId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12)
)
_MscExampleObjectIdRowStatusTable_Object = MibTable
mscExampleObjectIdRowStatusTable = _MscExampleObjectIdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdRowStatusTable.setStatus("mandatory")
_MscExampleObjectIdRowStatusEntry_Object = MibTableRow
mscExampleObjectIdRowStatusEntry = _MscExampleObjectIdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1, 1)
)
mscExampleObjectIdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdRowStatusEntry.setStatus("mandatory")
_MscExampleObjectIdRowStatus_Type = RowStatus
_MscExampleObjectIdRowStatus_Object = MibTableColumn
mscExampleObjectIdRowStatus = _MscExampleObjectIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1, 1, 1),
    _MscExampleObjectIdRowStatus_Type()
)
mscExampleObjectIdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdRowStatus.setStatus("mandatory")
_MscExampleObjectIdComponentName_Type = DisplayString
_MscExampleObjectIdComponentName_Object = MibTableColumn
mscExampleObjectIdComponentName = _MscExampleObjectIdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1, 1, 2),
    _MscExampleObjectIdComponentName_Type()
)
mscExampleObjectIdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleObjectIdComponentName.setStatus("mandatory")
_MscExampleObjectIdStorageType_Type = StorageType
_MscExampleObjectIdStorageType_Object = MibTableColumn
mscExampleObjectIdStorageType = _MscExampleObjectIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1, 1, 4),
    _MscExampleObjectIdStorageType_Type()
)
mscExampleObjectIdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleObjectIdStorageType.setStatus("mandatory")
_MscExampleObjectIdIndex_Type = ObjectIdentifier
_MscExampleObjectIdIndex_Object = MibTableColumn
mscExampleObjectIdIndex = _MscExampleObjectIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1, 1, 10),
    _MscExampleObjectIdIndex_Type()
)
mscExampleObjectIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleObjectIdIndex.setStatus("mandatory")
_MscExampleObjectIdOperationalTable_Object = MibTable
mscExampleObjectIdOperationalTable = _MscExampleObjectIdOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 10)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdOperationalTable.setStatus("mandatory")
_MscExampleObjectIdOperationalEntry_Object = MibTableRow
mscExampleObjectIdOperationalEntry = _MscExampleObjectIdOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 10, 1)
)
mscExampleObjectIdOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdOperationalEntry.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjId_Type = ObjectIdentifier
_MscExampleObjectIdOperFreeObjId_Object = MibTableColumn
mscExampleObjectIdOperFreeObjId = _MscExampleObjectIdOperFreeObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 10, 1, 1),
    _MscExampleObjectIdOperFreeObjId_Type()
)
mscExampleObjectIdOperFreeObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjId.setStatus("mandatory")
_MscExampleObjectIdProvisionalTable_Object = MibTable
mscExampleObjectIdProvisionalTable = _MscExampleObjectIdProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 11)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdProvisionalTable.setStatus("mandatory")
_MscExampleObjectIdProvisionalEntry_Object = MibTableRow
mscExampleObjectIdProvisionalEntry = _MscExampleObjectIdProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 11, 1)
)
mscExampleObjectIdProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdProvisionalEntry.setStatus("mandatory")
_MscExampleObjectIdProvEnumSub_Type = Link
_MscExampleObjectIdProvEnumSub_Object = MibTableColumn
mscExampleObjectIdProvEnumSub = _MscExampleObjectIdProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 11, 1, 1),
    _MscExampleObjectIdProvEnumSub_Type()
)
mscExampleObjectIdProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvEnumSub.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjId_Type = ObjectIdentifier
_MscExampleObjectIdProvFreeObjId_Object = MibTableColumn
mscExampleObjectIdProvFreeObjId = _MscExampleObjectIdProvFreeObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 11, 1, 2),
    _MscExampleObjectIdProvFreeObjId_Type()
)
mscExampleObjectIdProvFreeObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjId.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdReplicatedTable_Object = MibTable
mscExampleObjectIdOperFreeObjIdReplicatedTable = _MscExampleObjectIdOperFreeObjIdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1116)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdReplicatedTable.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdReplicatedEntry_Object = MibTableRow
mscExampleObjectIdOperFreeObjIdReplicatedEntry = _MscExampleObjectIdOperFreeObjIdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1116, 1)
)
mscExampleObjectIdOperFreeObjIdReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdOperFreeObjIdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdReplicatedEntry.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdReplicatedIndex_Type = ObjectIdentifier
_MscExampleObjectIdOperFreeObjIdReplicatedIndex_Object = MibTableColumn
mscExampleObjectIdOperFreeObjIdReplicatedIndex = _MscExampleObjectIdOperFreeObjIdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1116, 1, 1),
    _MscExampleObjectIdOperFreeObjIdReplicatedIndex_Type()
)
mscExampleObjectIdOperFreeObjIdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdReplicatedIndex.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdReplicatedValue_Type = ObjectIdentifier
_MscExampleObjectIdOperFreeObjIdReplicatedValue_Object = MibTableColumn
mscExampleObjectIdOperFreeObjIdReplicatedValue = _MscExampleObjectIdOperFreeObjIdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1116, 1, 2),
    _MscExampleObjectIdOperFreeObjIdReplicatedValue_Type()
)
mscExampleObjectIdOperFreeObjIdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdReplicatedValue.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdReplicatedRowStatus_Type = RowStatus
_MscExampleObjectIdOperFreeObjIdReplicatedRowStatus_Object = MibTableColumn
mscExampleObjectIdOperFreeObjIdReplicatedRowStatus = _MscExampleObjectIdOperFreeObjIdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1116, 1, 3),
    _MscExampleObjectIdOperFreeObjIdReplicatedRowStatus_Type()
)
mscExampleObjectIdOperFreeObjIdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdReplicatedRowStatus.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdListTable_Object = MibTable
mscExampleObjectIdOperFreeObjIdListTable = _MscExampleObjectIdOperFreeObjIdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1117)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdListTable.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdListEntry_Object = MibTableRow
mscExampleObjectIdOperFreeObjIdListEntry = _MscExampleObjectIdOperFreeObjIdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1117, 1)
)
mscExampleObjectIdOperFreeObjIdListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdOperFreeObjIdListValue"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdListEntry.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdListValue_Type = IntegerSequence
_MscExampleObjectIdOperFreeObjIdListValue_Object = MibTableColumn
mscExampleObjectIdOperFreeObjIdListValue = _MscExampleObjectIdOperFreeObjIdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1117, 1, 1),
    _MscExampleObjectIdOperFreeObjIdListValue_Type()
)
mscExampleObjectIdOperFreeObjIdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdListValue.setStatus("mandatory")
_MscExampleObjectIdOperFreeObjIdListRowStatus_Type = RowStatus
_MscExampleObjectIdOperFreeObjIdListRowStatus_Object = MibTableColumn
mscExampleObjectIdOperFreeObjIdListRowStatus = _MscExampleObjectIdOperFreeObjIdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1117, 1, 2),
    _MscExampleObjectIdOperFreeObjIdListRowStatus_Type()
)
mscExampleObjectIdOperFreeObjIdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleObjectIdOperFreeObjIdListRowStatus.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdReplicatedTable_Object = MibTable
mscExampleObjectIdProvFreeObjIdReplicatedTable = _MscExampleObjectIdProvFreeObjIdReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1118)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdReplicatedTable.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdReplicatedEntry_Object = MibTableRow
mscExampleObjectIdProvFreeObjIdReplicatedEntry = _MscExampleObjectIdProvFreeObjIdReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1118, 1)
)
mscExampleObjectIdProvFreeObjIdReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdProvFreeObjIdReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdReplicatedEntry.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdReplicatedIndex_Type = ObjectIdentifier
_MscExampleObjectIdProvFreeObjIdReplicatedIndex_Object = MibTableColumn
mscExampleObjectIdProvFreeObjIdReplicatedIndex = _MscExampleObjectIdProvFreeObjIdReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1118, 1, 1),
    _MscExampleObjectIdProvFreeObjIdReplicatedIndex_Type()
)
mscExampleObjectIdProvFreeObjIdReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdReplicatedIndex.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdReplicatedValue_Type = ObjectIdentifier
_MscExampleObjectIdProvFreeObjIdReplicatedValue_Object = MibTableColumn
mscExampleObjectIdProvFreeObjIdReplicatedValue = _MscExampleObjectIdProvFreeObjIdReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1118, 1, 2),
    _MscExampleObjectIdProvFreeObjIdReplicatedValue_Type()
)
mscExampleObjectIdProvFreeObjIdReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdReplicatedValue.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdReplicatedRowStatus_Type = RowStatus
_MscExampleObjectIdProvFreeObjIdReplicatedRowStatus_Object = MibTableColumn
mscExampleObjectIdProvFreeObjIdReplicatedRowStatus = _MscExampleObjectIdProvFreeObjIdReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1118, 1, 3),
    _MscExampleObjectIdProvFreeObjIdReplicatedRowStatus_Type()
)
mscExampleObjectIdProvFreeObjIdReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdReplicatedRowStatus.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdListTable_Object = MibTable
mscExampleObjectIdProvFreeObjIdListTable = _MscExampleObjectIdProvFreeObjIdListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1119)
)
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdListTable.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdListEntry_Object = MibTableRow
mscExampleObjectIdProvFreeObjIdListEntry = _MscExampleObjectIdProvFreeObjIdListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1119, 1)
)
mscExampleObjectIdProvFreeObjIdListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjectIdProvFreeObjIdListValue"),
)
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdListEntry.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdListValue_Type = IntegerSequence
_MscExampleObjectIdProvFreeObjIdListValue_Object = MibTableColumn
mscExampleObjectIdProvFreeObjIdListValue = _MscExampleObjectIdProvFreeObjIdListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1119, 1, 1),
    _MscExampleObjectIdProvFreeObjIdListValue_Type()
)
mscExampleObjectIdProvFreeObjIdListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdListValue.setStatus("mandatory")
_MscExampleObjectIdProvFreeObjIdListRowStatus_Type = RowStatus
_MscExampleObjectIdProvFreeObjIdListRowStatus_Object = MibTableColumn
mscExampleObjectIdProvFreeObjIdListRowStatus = _MscExampleObjectIdProvFreeObjIdListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 12, 1119, 1, 2),
    _MscExampleObjectIdProvFreeObjIdListRowStatus_Type()
)
mscExampleObjectIdProvFreeObjIdListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleObjectIdProvFreeObjIdListRowStatus.setStatus("mandatory")
_MscExampleSequence_ObjectIdentity = ObjectIdentity
mscExampleSequence = _MscExampleSequence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13)
)
_MscExampleSequenceRowStatusTable_Object = MibTable
mscExampleSequenceRowStatusTable = _MscExampleSequenceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1)
)
if mibBuilder.loadTexts:
    mscExampleSequenceRowStatusTable.setStatus("mandatory")
_MscExampleSequenceRowStatusEntry_Object = MibTableRow
mscExampleSequenceRowStatusEntry = _MscExampleSequenceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1, 1)
)
mscExampleSequenceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceRowStatusEntry.setStatus("mandatory")
_MscExampleSequenceRowStatus_Type = RowStatus
_MscExampleSequenceRowStatus_Object = MibTableColumn
mscExampleSequenceRowStatus = _MscExampleSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1, 1, 1),
    _MscExampleSequenceRowStatus_Type()
)
mscExampleSequenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceRowStatus.setStatus("mandatory")
_MscExampleSequenceComponentName_Type = DisplayString
_MscExampleSequenceComponentName_Object = MibTableColumn
mscExampleSequenceComponentName = _MscExampleSequenceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1, 1, 2),
    _MscExampleSequenceComponentName_Type()
)
mscExampleSequenceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleSequenceComponentName.setStatus("mandatory")
_MscExampleSequenceStorageType_Type = StorageType
_MscExampleSequenceStorageType_Object = MibTableColumn
mscExampleSequenceStorageType = _MscExampleSequenceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1, 1, 4),
    _MscExampleSequenceStorageType_Type()
)
mscExampleSequenceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleSequenceStorageType.setStatus("mandatory")
_MscExampleSequenceIndex_Type = ObjectIdentifier
_MscExampleSequenceIndex_Object = MibTableColumn
mscExampleSequenceIndex = _MscExampleSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1, 1, 10),
    _MscExampleSequenceIndex_Type()
)
mscExampleSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSequenceIndex.setStatus("mandatory")
_MscExampleSequenceOperationalTable_Object = MibTable
mscExampleSequenceOperationalTable = _MscExampleSequenceOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 10)
)
if mibBuilder.loadTexts:
    mscExampleSequenceOperationalTable.setStatus("mandatory")
_MscExampleSequenceOperationalEntry_Object = MibTableRow
mscExampleSequenceOperationalEntry = _MscExampleSequenceOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 10, 1)
)
mscExampleSequenceOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceOperationalEntry.setStatus("mandatory")


class _MscExampleSequenceOperStructSequence_Type(IntegerSequence):
    """Custom type mscExampleSequenceOperStructSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscExampleSequenceOperStructSequence_Type.__name__ = "IntegerSequence"
_MscExampleSequenceOperStructSequence_Object = MibTableColumn
mscExampleSequenceOperStructSequence = _MscExampleSequenceOperStructSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 10, 1, 1),
    _MscExampleSequenceOperStructSequence_Type()
)
mscExampleSequenceOperStructSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceOperStructSequence.setStatus("mandatory")


class _MscExampleSequenceOperFreeSequence_Type(IntegerSequence):
    """Custom type mscExampleSequenceOperFreeSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscExampleSequenceOperFreeSequence_Type.__name__ = "IntegerSequence"
_MscExampleSequenceOperFreeSequence_Object = MibTableColumn
mscExampleSequenceOperFreeSequence = _MscExampleSequenceOperFreeSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 10, 1, 2),
    _MscExampleSequenceOperFreeSequence_Type()
)
mscExampleSequenceOperFreeSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequence.setStatus("mandatory")
_MscExampleSequenceProvisionalTable_Object = MibTable
mscExampleSequenceProvisionalTable = _MscExampleSequenceProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 11)
)
if mibBuilder.loadTexts:
    mscExampleSequenceProvisionalTable.setStatus("mandatory")
_MscExampleSequenceProvisionalEntry_Object = MibTableRow
mscExampleSequenceProvisionalEntry = _MscExampleSequenceProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 11, 1)
)
mscExampleSequenceProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceProvisionalEntry.setStatus("mandatory")


class _MscExampleSequenceProvStructSequence_Type(IntegerSequence):
    """Custom type mscExampleSequenceProvStructSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscExampleSequenceProvStructSequence_Type.__name__ = "IntegerSequence"
_MscExampleSequenceProvStructSequence_Object = MibTableColumn
mscExampleSequenceProvStructSequence = _MscExampleSequenceProvStructSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 11, 1, 1),
    _MscExampleSequenceProvStructSequence_Type()
)
mscExampleSequenceProvStructSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceProvStructSequence.setStatus("mandatory")


class _MscExampleSequenceProvFreeSequence_Type(IntegerSequence):
    """Custom type mscExampleSequenceProvFreeSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscExampleSequenceProvFreeSequence_Type.__name__ = "IntegerSequence"
_MscExampleSequenceProvFreeSequence_Object = MibTableColumn
mscExampleSequenceProvFreeSequence = _MscExampleSequenceProvFreeSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 11, 1, 2),
    _MscExampleSequenceProvFreeSequence_Type()
)
mscExampleSequenceProvFreeSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequence.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceReplicatedTable_Object = MibTable
mscExampleSequenceOperFreeSequenceReplicatedTable = _MscExampleSequenceOperFreeSequenceReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1112)
)
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceReplicatedTable.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceReplicatedEntry_Object = MibTableRow
mscExampleSequenceOperFreeSequenceReplicatedEntry = _MscExampleSequenceOperFreeSequenceReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1112, 1)
)
mscExampleSequenceOperFreeSequenceReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceOperFreeSequenceReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceReplicatedEntry.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceReplicatedIndex_Type = ObjectIdentifier
_MscExampleSequenceOperFreeSequenceReplicatedIndex_Object = MibTableColumn
mscExampleSequenceOperFreeSequenceReplicatedIndex = _MscExampleSequenceOperFreeSequenceReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1112, 1, 1),
    _MscExampleSequenceOperFreeSequenceReplicatedIndex_Type()
)
mscExampleSequenceOperFreeSequenceReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceReplicatedIndex.setStatus("mandatory")


class _MscExampleSequenceOperFreeSequenceReplicatedValue_Type(IntegerSequence):
    """Custom type mscExampleSequenceOperFreeSequenceReplicatedValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscExampleSequenceOperFreeSequenceReplicatedValue_Type.__name__ = "IntegerSequence"
_MscExampleSequenceOperFreeSequenceReplicatedValue_Object = MibTableColumn
mscExampleSequenceOperFreeSequenceReplicatedValue = _MscExampleSequenceOperFreeSequenceReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1112, 1, 2),
    _MscExampleSequenceOperFreeSequenceReplicatedValue_Type()
)
mscExampleSequenceOperFreeSequenceReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceReplicatedValue.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceReplicatedRowStatus_Type = RowStatus
_MscExampleSequenceOperFreeSequenceReplicatedRowStatus_Object = MibTableColumn
mscExampleSequenceOperFreeSequenceReplicatedRowStatus = _MscExampleSequenceOperFreeSequenceReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1112, 1, 3),
    _MscExampleSequenceOperFreeSequenceReplicatedRowStatus_Type()
)
mscExampleSequenceOperFreeSequenceReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceReplicatedRowStatus.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceListTable_Object = MibTable
mscExampleSequenceOperFreeSequenceListTable = _MscExampleSequenceOperFreeSequenceListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1113)
)
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceListTable.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceListEntry_Object = MibTableRow
mscExampleSequenceOperFreeSequenceListEntry = _MscExampleSequenceOperFreeSequenceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1113, 1)
)
mscExampleSequenceOperFreeSequenceListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceOperFreeSequenceListValue"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceListEntry.setStatus("mandatory")


class _MscExampleSequenceOperFreeSequenceListValue_Type(IntegerSequence):
    """Custom type mscExampleSequenceOperFreeSequenceListValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscExampleSequenceOperFreeSequenceListValue_Type.__name__ = "IntegerSequence"
_MscExampleSequenceOperFreeSequenceListValue_Object = MibTableColumn
mscExampleSequenceOperFreeSequenceListValue = _MscExampleSequenceOperFreeSequenceListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1113, 1, 1),
    _MscExampleSequenceOperFreeSequenceListValue_Type()
)
mscExampleSequenceOperFreeSequenceListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceListValue.setStatus("mandatory")
_MscExampleSequenceOperFreeSequenceListRowStatus_Type = RowStatus
_MscExampleSequenceOperFreeSequenceListRowStatus_Object = MibTableColumn
mscExampleSequenceOperFreeSequenceListRowStatus = _MscExampleSequenceOperFreeSequenceListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1113, 1, 2),
    _MscExampleSequenceOperFreeSequenceListRowStatus_Type()
)
mscExampleSequenceOperFreeSequenceListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSequenceOperFreeSequenceListRowStatus.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceReplicatedTable_Object = MibTable
mscExampleSequenceProvFreeSequenceReplicatedTable = _MscExampleSequenceProvFreeSequenceReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1114)
)
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceReplicatedTable.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceReplicatedEntry_Object = MibTableRow
mscExampleSequenceProvFreeSequenceReplicatedEntry = _MscExampleSequenceProvFreeSequenceReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1114, 1)
)
mscExampleSequenceProvFreeSequenceReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceProvFreeSequenceReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceReplicatedEntry.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceReplicatedIndex_Type = ObjectIdentifier
_MscExampleSequenceProvFreeSequenceReplicatedIndex_Object = MibTableColumn
mscExampleSequenceProvFreeSequenceReplicatedIndex = _MscExampleSequenceProvFreeSequenceReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1114, 1, 1),
    _MscExampleSequenceProvFreeSequenceReplicatedIndex_Type()
)
mscExampleSequenceProvFreeSequenceReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceReplicatedIndex.setStatus("mandatory")


class _MscExampleSequenceProvFreeSequenceReplicatedValue_Type(IntegerSequence):
    """Custom type mscExampleSequenceProvFreeSequenceReplicatedValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_MscExampleSequenceProvFreeSequenceReplicatedValue_Type.__name__ = "IntegerSequence"
_MscExampleSequenceProvFreeSequenceReplicatedValue_Object = MibTableColumn
mscExampleSequenceProvFreeSequenceReplicatedValue = _MscExampleSequenceProvFreeSequenceReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1114, 1, 2),
    _MscExampleSequenceProvFreeSequenceReplicatedValue_Type()
)
mscExampleSequenceProvFreeSequenceReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceReplicatedValue.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceReplicatedRowStatus_Type = RowStatus
_MscExampleSequenceProvFreeSequenceReplicatedRowStatus_Object = MibTableColumn
mscExampleSequenceProvFreeSequenceReplicatedRowStatus = _MscExampleSequenceProvFreeSequenceReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1114, 1, 3),
    _MscExampleSequenceProvFreeSequenceReplicatedRowStatus_Type()
)
mscExampleSequenceProvFreeSequenceReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceReplicatedRowStatus.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceListTable_Object = MibTable
mscExampleSequenceProvFreeSequenceListTable = _MscExampleSequenceProvFreeSequenceListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1115)
)
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceListTable.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceListEntry_Object = MibTableRow
mscExampleSequenceProvFreeSequenceListEntry = _MscExampleSequenceProvFreeSequenceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1115, 1)
)
mscExampleSequenceProvFreeSequenceListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceProvFreeSequenceListValue"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceListEntry.setStatus("mandatory")


class _MscExampleSequenceProvFreeSequenceListValue_Type(IntegerSequence):
    """Custom type mscExampleSequenceProvFreeSequenceListValue based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 9),
    )


_MscExampleSequenceProvFreeSequenceListValue_Type.__name__ = "IntegerSequence"
_MscExampleSequenceProvFreeSequenceListValue_Object = MibTableColumn
mscExampleSequenceProvFreeSequenceListValue = _MscExampleSequenceProvFreeSequenceListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1115, 1, 1),
    _MscExampleSequenceProvFreeSequenceListValue_Type()
)
mscExampleSequenceProvFreeSequenceListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceListValue.setStatus("mandatory")
_MscExampleSequenceProvFreeSequenceListRowStatus_Type = RowStatus
_MscExampleSequenceProvFreeSequenceListRowStatus_Object = MibTableColumn
mscExampleSequenceProvFreeSequenceListRowStatus = _MscExampleSequenceProvFreeSequenceListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 13, 1115, 1, 2),
    _MscExampleSequenceProvFreeSequenceListRowStatus_Type()
)
mscExampleSequenceProvFreeSequenceListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSequenceProvFreeSequenceListRowStatus.setStatus("mandatory")
_MscExampleSigned_ObjectIdentity = ObjectIdentity
mscExampleSigned = _MscExampleSigned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14)
)
_MscExampleSignedRowStatusTable_Object = MibTable
mscExampleSignedRowStatusTable = _MscExampleSignedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1)
)
if mibBuilder.loadTexts:
    mscExampleSignedRowStatusTable.setStatus("mandatory")
_MscExampleSignedRowStatusEntry_Object = MibTableRow
mscExampleSignedRowStatusEntry = _MscExampleSignedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1, 1)
)
mscExampleSignedRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedRowStatusEntry.setStatus("mandatory")
_MscExampleSignedRowStatus_Type = RowStatus
_MscExampleSignedRowStatus_Object = MibTableColumn
mscExampleSignedRowStatus = _MscExampleSignedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1, 1, 1),
    _MscExampleSignedRowStatus_Type()
)
mscExampleSignedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedRowStatus.setStatus("mandatory")
_MscExampleSignedComponentName_Type = DisplayString
_MscExampleSignedComponentName_Object = MibTableColumn
mscExampleSignedComponentName = _MscExampleSignedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1, 1, 2),
    _MscExampleSignedComponentName_Type()
)
mscExampleSignedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleSignedComponentName.setStatus("mandatory")
_MscExampleSignedStorageType_Type = StorageType
_MscExampleSignedStorageType_Object = MibTableColumn
mscExampleSignedStorageType = _MscExampleSignedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1, 1, 4),
    _MscExampleSignedStorageType_Type()
)
mscExampleSignedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleSignedStorageType.setStatus("mandatory")
_MscExampleSignedIndex_Type = NonReplicated
_MscExampleSignedIndex_Object = MibTableColumn
mscExampleSignedIndex = _MscExampleSignedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1, 1, 10),
    _MscExampleSignedIndex_Type()
)
mscExampleSignedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedIndex.setStatus("mandatory")
_MscExampleSignedOperationalTable_Object = MibTable
mscExampleSignedOperationalTable = _MscExampleSignedOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 10)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperationalTable.setStatus("mandatory")
_MscExampleSignedOperationalEntry_Object = MibTableRow
mscExampleSignedOperationalEntry = _MscExampleSignedOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 10, 1)
)
mscExampleSignedOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperationalEntry.setStatus("mandatory")


class _MscExampleSignedOperStructSigned_Type(Integer32):
    """Custom type mscExampleSignedOperStructSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_MscExampleSignedOperStructSigned_Type.__name__ = "Integer32"
_MscExampleSignedOperStructSigned_Object = MibTableColumn
mscExampleSignedOperStructSigned = _MscExampleSignedOperStructSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 10, 1, 1),
    _MscExampleSignedOperStructSigned_Type()
)
mscExampleSignedOperStructSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSigned.setStatus("mandatory")


class _MscExampleSignedOperFreeSigned_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_MscExampleSignedOperFreeSigned_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSigned_Object = MibTableColumn
mscExampleSignedOperFreeSigned = _MscExampleSignedOperFreeSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 10, 1, 2),
    _MscExampleSignedOperFreeSigned_Type()
)
mscExampleSignedOperFreeSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSigned.setStatus("mandatory")
_MscExampleSignedProvisionalTable_Object = MibTable
mscExampleSignedProvisionalTable = _MscExampleSignedProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 11)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvisionalTable.setStatus("mandatory")
_MscExampleSignedProvisionalEntry_Object = MibTableRow
mscExampleSignedProvisionalEntry = _MscExampleSignedProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 11, 1)
)
mscExampleSignedProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvisionalEntry.setStatus("mandatory")
_MscExampleSignedProvSignedSub_Type = Link
_MscExampleSignedProvSignedSub_Object = MibTableColumn
mscExampleSignedProvSignedSub = _MscExampleSignedProvSignedSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 11, 1, 1),
    _MscExampleSignedProvSignedSub_Type()
)
mscExampleSignedProvSignedSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvSignedSub.setStatus("mandatory")


class _MscExampleSignedProvStructSigned_Type(Integer32):
    """Custom type mscExampleSignedProvStructSigned based on Integer32"""
    defaultValue = -17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-17, -17),
        ValueRangeConstraint(-16, 16),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(18, 18),
    )


_MscExampleSignedProvStructSigned_Type.__name__ = "Integer32"
_MscExampleSignedProvStructSigned_Object = MibTableColumn
mscExampleSignedProvStructSigned = _MscExampleSignedProvStructSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 11, 1, 2),
    _MscExampleSignedProvStructSigned_Type()
)
mscExampleSignedProvStructSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSigned.setStatus("mandatory")


class _MscExampleSignedProvFreeSigned_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSigned based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_MscExampleSignedProvFreeSigned_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSigned_Object = MibTableColumn
mscExampleSignedProvFreeSigned = _MscExampleSignedProvFreeSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 11, 1, 3),
    _MscExampleSignedProvFreeSigned_Type()
)
mscExampleSignedProvFreeSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSigned.setStatus("mandatory")


class _MscExampleSignedProvFreeSigned1_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSigned1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_MscExampleSignedProvFreeSigned1_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSigned1_Object = MibTableColumn
mscExampleSignedProvFreeSigned1 = _MscExampleSignedProvFreeSigned1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 11, 1, 4),
    _MscExampleSignedProvFreeSigned1_Type()
)
mscExampleSignedProvFreeSigned1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSigned1.setStatus("mandatory")
_MscExampleSignedOperStructSignedVectorTable_Object = MibTable
mscExampleSignedOperStructSignedVectorTable = _MscExampleSignedOperStructSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1148)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedVectorTable.setStatus("mandatory")
_MscExampleSignedOperStructSignedVectorEntry_Object = MibTableRow
mscExampleSignedOperStructSignedVectorEntry = _MscExampleSignedOperStructSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1148, 1)
)
mscExampleSignedOperStructSignedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperStructSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedVectorEntry.setStatus("mandatory")


class _MscExampleSignedOperStructSignedVectorIndex_Type(Integer32):
    """Custom type mscExampleSignedOperStructSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleSignedOperStructSignedVectorIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperStructSignedVectorIndex_Object = MibTableColumn
mscExampleSignedOperStructSignedVectorIndex = _MscExampleSignedOperStructSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1148, 1, 1),
    _MscExampleSignedOperStructSignedVectorIndex_Type()
)
mscExampleSignedOperStructSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedVectorIndex.setStatus("mandatory")


class _MscExampleSignedOperStructSignedVectorValue_Type(Integer32):
    """Custom type mscExampleSignedOperStructSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedOperStructSignedVectorValue_Type.__name__ = "Integer32"
_MscExampleSignedOperStructSignedVectorValue_Object = MibTableColumn
mscExampleSignedOperStructSignedVectorValue = _MscExampleSignedOperStructSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1148, 1, 2),
    _MscExampleSignedOperStructSignedVectorValue_Type()
)
mscExampleSignedOperStructSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedVectorValue.setStatus("mandatory")
_MscExampleSignedOperStructSignedArrayTable_Object = MibTable
mscExampleSignedOperStructSignedArrayTable = _MscExampleSignedOperStructSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1149)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedArrayTable.setStatus("mandatory")
_MscExampleSignedOperStructSignedArrayEntry_Object = MibTableRow
mscExampleSignedOperStructSignedArrayEntry = _MscExampleSignedOperStructSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1149, 1)
)
mscExampleSignedOperStructSignedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperStructSignedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperStructSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedArrayEntry.setStatus("mandatory")


class _MscExampleSignedOperStructSignedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleSignedOperStructSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleSignedOperStructSignedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperStructSignedArrayRowIndex_Object = MibTableColumn
mscExampleSignedOperStructSignedArrayRowIndex = _MscExampleSignedOperStructSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1149, 1, 1),
    _MscExampleSignedOperStructSignedArrayRowIndex_Type()
)
mscExampleSignedOperStructSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedArrayRowIndex.setStatus("mandatory")


class _MscExampleSignedOperStructSignedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleSignedOperStructSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleSignedOperStructSignedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperStructSignedArrayColumnIndex_Object = MibTableColumn
mscExampleSignedOperStructSignedArrayColumnIndex = _MscExampleSignedOperStructSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1149, 1, 2),
    _MscExampleSignedOperStructSignedArrayColumnIndex_Type()
)
mscExampleSignedOperStructSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedArrayColumnIndex.setStatus("mandatory")


class _MscExampleSignedOperStructSignedArrayValue_Type(Integer32):
    """Custom type mscExampleSignedOperStructSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedOperStructSignedArrayValue_Type.__name__ = "Integer32"
_MscExampleSignedOperStructSignedArrayValue_Object = MibTableColumn
mscExampleSignedOperStructSignedArrayValue = _MscExampleSignedOperStructSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1149, 1, 3),
    _MscExampleSignedOperStructSignedArrayValue_Type()
)
mscExampleSignedOperStructSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperStructSignedArrayValue.setStatus("mandatory")
_MscExampleSignedOperFreeSignedVectorTable_Object = MibTable
mscExampleSignedOperFreeSignedVectorTable = _MscExampleSignedOperFreeSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1150)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedVectorTable.setStatus("mandatory")
_MscExampleSignedOperFreeSignedVectorEntry_Object = MibTableRow
mscExampleSignedOperFreeSignedVectorEntry = _MscExampleSignedOperFreeSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1150, 1)
)
mscExampleSignedOperFreeSignedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperFreeSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedVectorEntry.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedVectorIndex_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleSignedOperFreeSignedVectorIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedVectorIndex_Object = MibTableColumn
mscExampleSignedOperFreeSignedVectorIndex = _MscExampleSignedOperFreeSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1150, 1, 1),
    _MscExampleSignedOperFreeSignedVectorIndex_Type()
)
mscExampleSignedOperFreeSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedVectorIndex.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedVectorValue_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedOperFreeSignedVectorValue_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedVectorValue_Object = MibTableColumn
mscExampleSignedOperFreeSignedVectorValue = _MscExampleSignedOperFreeSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1150, 1, 2),
    _MscExampleSignedOperFreeSignedVectorValue_Type()
)
mscExampleSignedOperFreeSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedVectorValue.setStatus("mandatory")
_MscExampleSignedOperFreeSignedArrayTable_Object = MibTable
mscExampleSignedOperFreeSignedArrayTable = _MscExampleSignedOperFreeSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1151)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedArrayTable.setStatus("mandatory")
_MscExampleSignedOperFreeSignedArrayEntry_Object = MibTableRow
mscExampleSignedOperFreeSignedArrayEntry = _MscExampleSignedOperFreeSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1151, 1)
)
mscExampleSignedOperFreeSignedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperFreeSignedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperFreeSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedArrayEntry.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleSignedOperFreeSignedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedArrayRowIndex_Object = MibTableColumn
mscExampleSignedOperFreeSignedArrayRowIndex = _MscExampleSignedOperFreeSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1151, 1, 1),
    _MscExampleSignedOperFreeSignedArrayRowIndex_Type()
)
mscExampleSignedOperFreeSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedArrayRowIndex.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleSignedOperFreeSignedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedArrayColumnIndex_Object = MibTableColumn
mscExampleSignedOperFreeSignedArrayColumnIndex = _MscExampleSignedOperFreeSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1151, 1, 2),
    _MscExampleSignedOperFreeSignedArrayColumnIndex_Type()
)
mscExampleSignedOperFreeSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedArrayColumnIndex.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedArrayValue_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedOperFreeSignedArrayValue_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedArrayValue_Object = MibTableColumn
mscExampleSignedOperFreeSignedArrayValue = _MscExampleSignedOperFreeSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1151, 1, 3),
    _MscExampleSignedOperFreeSignedArrayValue_Type()
)
mscExampleSignedOperFreeSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedArrayValue.setStatus("mandatory")
_MscExampleSignedOperFreeSignedReplicatedTable_Object = MibTable
mscExampleSignedOperFreeSignedReplicatedTable = _MscExampleSignedOperFreeSignedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1152)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedReplicatedTable.setStatus("mandatory")
_MscExampleSignedOperFreeSignedReplicatedEntry_Object = MibTableRow
mscExampleSignedOperFreeSignedReplicatedEntry = _MscExampleSignedOperFreeSignedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1152, 1)
)
mscExampleSignedOperFreeSignedReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperFreeSignedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedReplicatedEntry.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedReplicatedIndex_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedOperFreeSignedReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedReplicatedIndex_Object = MibTableColumn
mscExampleSignedOperFreeSignedReplicatedIndex = _MscExampleSignedOperFreeSignedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1152, 1, 1),
    _MscExampleSignedOperFreeSignedReplicatedIndex_Type()
)
mscExampleSignedOperFreeSignedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedReplicatedIndex.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedReplicatedValue_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedReplicatedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_MscExampleSignedOperFreeSignedReplicatedValue_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedReplicatedValue_Object = MibTableColumn
mscExampleSignedOperFreeSignedReplicatedValue = _MscExampleSignedOperFreeSignedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1152, 1, 2),
    _MscExampleSignedOperFreeSignedReplicatedValue_Type()
)
mscExampleSignedOperFreeSignedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedReplicatedValue.setStatus("mandatory")
_MscExampleSignedOperFreeSignedReplicatedRowStatus_Type = RowStatus
_MscExampleSignedOperFreeSignedReplicatedRowStatus_Object = MibTableColumn
mscExampleSignedOperFreeSignedReplicatedRowStatus = _MscExampleSignedOperFreeSignedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1152, 1, 3),
    _MscExampleSignedOperFreeSignedReplicatedRowStatus_Type()
)
mscExampleSignedOperFreeSignedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedReplicatedRowStatus.setStatus("mandatory")
_MscExampleSignedOperFreeSignedListTable_Object = MibTable
mscExampleSignedOperFreeSignedListTable = _MscExampleSignedOperFreeSignedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1153)
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedListTable.setStatus("mandatory")
_MscExampleSignedOperFreeSignedListEntry_Object = MibTableRow
mscExampleSignedOperFreeSignedListEntry = _MscExampleSignedOperFreeSignedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1153, 1)
)
mscExampleSignedOperFreeSignedListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedOperFreeSignedListValue"),
)
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedListEntry.setStatus("mandatory")


class _MscExampleSignedOperFreeSignedListValue_Type(Integer32):
    """Custom type mscExampleSignedOperFreeSignedListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 16),
    )


_MscExampleSignedOperFreeSignedListValue_Type.__name__ = "Integer32"
_MscExampleSignedOperFreeSignedListValue_Object = MibTableColumn
mscExampleSignedOperFreeSignedListValue = _MscExampleSignedOperFreeSignedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1153, 1, 1),
    _MscExampleSignedOperFreeSignedListValue_Type()
)
mscExampleSignedOperFreeSignedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedListValue.setStatus("mandatory")
_MscExampleSignedOperFreeSignedListRowStatus_Type = RowStatus
_MscExampleSignedOperFreeSignedListRowStatus_Object = MibTableColumn
mscExampleSignedOperFreeSignedListRowStatus = _MscExampleSignedOperFreeSignedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1153, 1, 2),
    _MscExampleSignedOperFreeSignedListRowStatus_Type()
)
mscExampleSignedOperFreeSignedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSignedOperFreeSignedListRowStatus.setStatus("mandatory")
_MscExampleSignedProvStructSignedVectorTable_Object = MibTable
mscExampleSignedProvStructSignedVectorTable = _MscExampleSignedProvStructSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1154)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedVectorTable.setStatus("mandatory")
_MscExampleSignedProvStructSignedVectorEntry_Object = MibTableRow
mscExampleSignedProvStructSignedVectorEntry = _MscExampleSignedProvStructSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1154, 1)
)
mscExampleSignedProvStructSignedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvStructSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedVectorEntry.setStatus("mandatory")


class _MscExampleSignedProvStructSignedVectorIndex_Type(Integer32):
    """Custom type mscExampleSignedProvStructSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleSignedProvStructSignedVectorIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvStructSignedVectorIndex_Object = MibTableColumn
mscExampleSignedProvStructSignedVectorIndex = _MscExampleSignedProvStructSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1154, 1, 1),
    _MscExampleSignedProvStructSignedVectorIndex_Type()
)
mscExampleSignedProvStructSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedVectorIndex.setStatus("mandatory")


class _MscExampleSignedProvStructSignedVectorValue_Type(Integer32):
    """Custom type mscExampleSignedProvStructSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedProvStructSignedVectorValue_Type.__name__ = "Integer32"
_MscExampleSignedProvStructSignedVectorValue_Object = MibTableColumn
mscExampleSignedProvStructSignedVectorValue = _MscExampleSignedProvStructSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1154, 1, 2),
    _MscExampleSignedProvStructSignedVectorValue_Type()
)
mscExampleSignedProvStructSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedVectorValue.setStatus("mandatory")
_MscExampleSignedProvStructSignedArrayTable_Object = MibTable
mscExampleSignedProvStructSignedArrayTable = _MscExampleSignedProvStructSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1155)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedArrayTable.setStatus("mandatory")
_MscExampleSignedProvStructSignedArrayEntry_Object = MibTableRow
mscExampleSignedProvStructSignedArrayEntry = _MscExampleSignedProvStructSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1155, 1)
)
mscExampleSignedProvStructSignedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvStructSignedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvStructSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedArrayEntry.setStatus("mandatory")


class _MscExampleSignedProvStructSignedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleSignedProvStructSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleSignedProvStructSignedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvStructSignedArrayRowIndex_Object = MibTableColumn
mscExampleSignedProvStructSignedArrayRowIndex = _MscExampleSignedProvStructSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1155, 1, 1),
    _MscExampleSignedProvStructSignedArrayRowIndex_Type()
)
mscExampleSignedProvStructSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedArrayRowIndex.setStatus("mandatory")


class _MscExampleSignedProvStructSignedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleSignedProvStructSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleSignedProvStructSignedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvStructSignedArrayColumnIndex_Object = MibTableColumn
mscExampleSignedProvStructSignedArrayColumnIndex = _MscExampleSignedProvStructSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1155, 1, 2),
    _MscExampleSignedProvStructSignedArrayColumnIndex_Type()
)
mscExampleSignedProvStructSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedArrayColumnIndex.setStatus("mandatory")


class _MscExampleSignedProvStructSignedArrayValue_Type(Integer32):
    """Custom type mscExampleSignedProvStructSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedProvStructSignedArrayValue_Type.__name__ = "Integer32"
_MscExampleSignedProvStructSignedArrayValue_Object = MibTableColumn
mscExampleSignedProvStructSignedArrayValue = _MscExampleSignedProvStructSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1155, 1, 3),
    _MscExampleSignedProvStructSignedArrayValue_Type()
)
mscExampleSignedProvStructSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvStructSignedArrayValue.setStatus("mandatory")
_MscExampleSignedProvFreeSignedVectorTable_Object = MibTable
mscExampleSignedProvFreeSignedVectorTable = _MscExampleSignedProvFreeSignedVectorTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1156)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVectorTable.setStatus("mandatory")
_MscExampleSignedProvFreeSignedVectorEntry_Object = MibTableRow
mscExampleSignedProvFreeSignedVectorEntry = _MscExampleSignedProvFreeSignedVectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1156, 1)
)
mscExampleSignedProvFreeSignedVectorEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedVectorIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVectorEntry.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedVectorIndex_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedVectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleSignedProvFreeSignedVectorIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedVectorIndex_Object = MibTableColumn
mscExampleSignedProvFreeSignedVectorIndex = _MscExampleSignedProvFreeSignedVectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1156, 1, 1),
    _MscExampleSignedProvFreeSignedVectorIndex_Type()
)
mscExampleSignedProvFreeSignedVectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVectorIndex.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedVectorValue_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedVectorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedProvFreeSignedVectorValue_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedVectorValue_Object = MibTableColumn
mscExampleSignedProvFreeSignedVectorValue = _MscExampleSignedProvFreeSignedVectorValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1156, 1, 2),
    _MscExampleSignedProvFreeSignedVectorValue_Type()
)
mscExampleSignedProvFreeSignedVectorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVectorValue.setStatus("mandatory")
_MscExampleSignedProvFreeSignedVector1Table_Object = MibTable
mscExampleSignedProvFreeSignedVector1Table = _MscExampleSignedProvFreeSignedVector1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1157)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVector1Table.setStatus("mandatory")
_MscExampleSignedProvFreeSignedVector1Entry_Object = MibTableRow
mscExampleSignedProvFreeSignedVector1Entry = _MscExampleSignedProvFreeSignedVector1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1157, 1)
)
mscExampleSignedProvFreeSignedVector1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedVector1Index"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVector1Entry.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedVector1Index_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedVector1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleSignedProvFreeSignedVector1Index_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedVector1Index_Object = MibTableColumn
mscExampleSignedProvFreeSignedVector1Index = _MscExampleSignedProvFreeSignedVector1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1157, 1, 1),
    _MscExampleSignedProvFreeSignedVector1Index_Type()
)
mscExampleSignedProvFreeSignedVector1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVector1Index.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedVector1Value_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedVector1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_MscExampleSignedProvFreeSignedVector1Value_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedVector1Value_Object = MibTableColumn
mscExampleSignedProvFreeSignedVector1Value = _MscExampleSignedProvFreeSignedVector1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1157, 1, 2),
    _MscExampleSignedProvFreeSignedVector1Value_Type()
)
mscExampleSignedProvFreeSignedVector1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedVector1Value.setStatus("mandatory")
_MscExampleSignedProvFreeSignedArrayTable_Object = MibTable
mscExampleSignedProvFreeSignedArrayTable = _MscExampleSignedProvFreeSignedArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1158)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArrayTable.setStatus("mandatory")
_MscExampleSignedProvFreeSignedArrayEntry_Object = MibTableRow
mscExampleSignedProvFreeSignedArrayEntry = _MscExampleSignedProvFreeSignedArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1158, 1)
)
mscExampleSignedProvFreeSignedArrayEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedArrayRowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedArrayColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArrayEntry.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedArrayRowIndex_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedArrayRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleSignedProvFreeSignedArrayRowIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedArrayRowIndex_Object = MibTableColumn
mscExampleSignedProvFreeSignedArrayRowIndex = _MscExampleSignedProvFreeSignedArrayRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1158, 1, 1),
    _MscExampleSignedProvFreeSignedArrayRowIndex_Type()
)
mscExampleSignedProvFreeSignedArrayRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArrayRowIndex.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedArrayColumnIndex_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedArrayColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleSignedProvFreeSignedArrayColumnIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedArrayColumnIndex_Object = MibTableColumn
mscExampleSignedProvFreeSignedArrayColumnIndex = _MscExampleSignedProvFreeSignedArrayColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1158, 1, 2),
    _MscExampleSignedProvFreeSignedArrayColumnIndex_Type()
)
mscExampleSignedProvFreeSignedArrayColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArrayColumnIndex.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedArrayValue_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedArrayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 4000),
    )


_MscExampleSignedProvFreeSignedArrayValue_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedArrayValue_Object = MibTableColumn
mscExampleSignedProvFreeSignedArrayValue = _MscExampleSignedProvFreeSignedArrayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1158, 1, 3),
    _MscExampleSignedProvFreeSignedArrayValue_Type()
)
mscExampleSignedProvFreeSignedArrayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArrayValue.setStatus("mandatory")
_MscExampleSignedProvFreeSignedArray1Table_Object = MibTable
mscExampleSignedProvFreeSignedArray1Table = _MscExampleSignedProvFreeSignedArray1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1159)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArray1Table.setStatus("mandatory")
_MscExampleSignedProvFreeSignedArray1Entry_Object = MibTableRow
mscExampleSignedProvFreeSignedArray1Entry = _MscExampleSignedProvFreeSignedArray1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1159, 1)
)
mscExampleSignedProvFreeSignedArray1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedArray1RowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedArray1ColumnIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArray1Entry.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedArray1RowIndex_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedArray1RowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscExampleSignedProvFreeSignedArray1RowIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedArray1RowIndex_Object = MibTableColumn
mscExampleSignedProvFreeSignedArray1RowIndex = _MscExampleSignedProvFreeSignedArray1RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1159, 1, 1),
    _MscExampleSignedProvFreeSignedArray1RowIndex_Type()
)
mscExampleSignedProvFreeSignedArray1RowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArray1RowIndex.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedArray1ColumnIndex_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedArray1ColumnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscExampleSignedProvFreeSignedArray1ColumnIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedArray1ColumnIndex_Object = MibTableColumn
mscExampleSignedProvFreeSignedArray1ColumnIndex = _MscExampleSignedProvFreeSignedArray1ColumnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1159, 1, 2),
    _MscExampleSignedProvFreeSignedArray1ColumnIndex_Type()
)
mscExampleSignedProvFreeSignedArray1ColumnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArray1ColumnIndex.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedArray1Value_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedArray1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 4000),
    )


_MscExampleSignedProvFreeSignedArray1Value_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedArray1Value_Object = MibTableColumn
mscExampleSignedProvFreeSignedArray1Value = _MscExampleSignedProvFreeSignedArray1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1159, 1, 3),
    _MscExampleSignedProvFreeSignedArray1Value_Type()
)
mscExampleSignedProvFreeSignedArray1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedArray1Value.setStatus("mandatory")
_MscExampleSignedProvFreeSignedReplicatedTable_Object = MibTable
mscExampleSignedProvFreeSignedReplicatedTable = _MscExampleSignedProvFreeSignedReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1160)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedReplicatedTable.setStatus("mandatory")
_MscExampleSignedProvFreeSignedReplicatedEntry_Object = MibTableRow
mscExampleSignedProvFreeSignedReplicatedEntry = _MscExampleSignedProvFreeSignedReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1160, 1)
)
mscExampleSignedProvFreeSignedReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedReplicatedEntry.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedReplicatedIndex_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedReplicatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MscExampleSignedProvFreeSignedReplicatedIndex_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedReplicatedIndex_Object = MibTableColumn
mscExampleSignedProvFreeSignedReplicatedIndex = _MscExampleSignedProvFreeSignedReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1160, 1, 1),
    _MscExampleSignedProvFreeSignedReplicatedIndex_Type()
)
mscExampleSignedProvFreeSignedReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedReplicatedIndex.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedReplicatedValue_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedReplicatedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 13),
    )


_MscExampleSignedProvFreeSignedReplicatedValue_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedReplicatedValue_Object = MibTableColumn
mscExampleSignedProvFreeSignedReplicatedValue = _MscExampleSignedProvFreeSignedReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1160, 1, 2),
    _MscExampleSignedProvFreeSignedReplicatedValue_Type()
)
mscExampleSignedProvFreeSignedReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedReplicatedValue.setStatus("mandatory")
_MscExampleSignedProvFreeSignedReplicatedRowStatus_Type = RowStatus
_MscExampleSignedProvFreeSignedReplicatedRowStatus_Object = MibTableColumn
mscExampleSignedProvFreeSignedReplicatedRowStatus = _MscExampleSignedProvFreeSignedReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1160, 1, 3),
    _MscExampleSignedProvFreeSignedReplicatedRowStatus_Type()
)
mscExampleSignedProvFreeSignedReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedReplicatedRowStatus.setStatus("mandatory")
_MscExampleSignedProvFreeSignedListTable_Object = MibTable
mscExampleSignedProvFreeSignedListTable = _MscExampleSignedProvFreeSignedListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1161)
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedListTable.setStatus("mandatory")
_MscExampleSignedProvFreeSignedListEntry_Object = MibTableRow
mscExampleSignedProvFreeSignedListEntry = _MscExampleSignedProvFreeSignedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1161, 1)
)
mscExampleSignedProvFreeSignedListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSignedProvFreeSignedListValue"),
)
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedListEntry.setStatus("mandatory")


class _MscExampleSignedProvFreeSignedListValue_Type(Integer32):
    """Custom type mscExampleSignedProvFreeSignedListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 160),
    )


_MscExampleSignedProvFreeSignedListValue_Type.__name__ = "Integer32"
_MscExampleSignedProvFreeSignedListValue_Object = MibTableColumn
mscExampleSignedProvFreeSignedListValue = _MscExampleSignedProvFreeSignedListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1161, 1, 1),
    _MscExampleSignedProvFreeSignedListValue_Type()
)
mscExampleSignedProvFreeSignedListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedListValue.setStatus("mandatory")
_MscExampleSignedProvFreeSignedListRowStatus_Type = RowStatus
_MscExampleSignedProvFreeSignedListRowStatus_Object = MibTableColumn
mscExampleSignedProvFreeSignedListRowStatus = _MscExampleSignedProvFreeSignedListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 14, 1161, 1, 2),
    _MscExampleSignedProvFreeSignedListRowStatus_Type()
)
mscExampleSignedProvFreeSignedListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleSignedProvFreeSignedListRowStatus.setStatus("mandatory")
_MscExampleMiscellaneous_ObjectIdentity = ObjectIdentity
mscExampleMiscellaneous = _MscExampleMiscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15)
)
_MscExampleMiscellaneousRowStatusTable_Object = MibTable
mscExampleMiscellaneousRowStatusTable = _MscExampleMiscellaneousRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousRowStatusTable.setStatus("mandatory")
_MscExampleMiscellaneousRowStatusEntry_Object = MibTableRow
mscExampleMiscellaneousRowStatusEntry = _MscExampleMiscellaneousRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1, 1)
)
mscExampleMiscellaneousRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousRowStatusEntry.setStatus("mandatory")
_MscExampleMiscellaneousRowStatus_Type = RowStatus
_MscExampleMiscellaneousRowStatus_Object = MibTableColumn
mscExampleMiscellaneousRowStatus = _MscExampleMiscellaneousRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1, 1, 1),
    _MscExampleMiscellaneousRowStatus_Type()
)
mscExampleMiscellaneousRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousComponentName_Type = DisplayString
_MscExampleMiscellaneousComponentName_Object = MibTableColumn
mscExampleMiscellaneousComponentName = _MscExampleMiscellaneousComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1, 1, 2),
    _MscExampleMiscellaneousComponentName_Type()
)
mscExampleMiscellaneousComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousComponentName.setStatus("mandatory")
_MscExampleMiscellaneousStorageType_Type = StorageType
_MscExampleMiscellaneousStorageType_Object = MibTableColumn
mscExampleMiscellaneousStorageType = _MscExampleMiscellaneousStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1, 1, 4),
    _MscExampleMiscellaneousStorageType_Type()
)
mscExampleMiscellaneousStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousStorageType.setStatus("mandatory")
_MscExampleMiscellaneousIndex_Type = NonReplicated
_MscExampleMiscellaneousIndex_Object = MibTableColumn
mscExampleMiscellaneousIndex = _MscExampleMiscellaneousIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1, 1, 10),
    _MscExampleMiscellaneousIndex_Type()
)
mscExampleMiscellaneousIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousIndex.setStatus("mandatory")
_MscExampleMiscellaneousOperationalTable_Object = MibTable
mscExampleMiscellaneousOperationalTable = _MscExampleMiscellaneousOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperationalTable.setStatus("mandatory")
_MscExampleMiscellaneousOperationalEntry_Object = MibTableRow
mscExampleMiscellaneousOperationalEntry = _MscExampleMiscellaneousOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1)
)
mscExampleMiscellaneousOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperationalEntry.setStatus("mandatory")


class _MscExampleMiscellaneousOperStructLong_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousOperStructLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousOperStructLong_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousOperStructLong_Object = MibTableColumn
mscExampleMiscellaneousOperStructLong = _MscExampleMiscellaneousOperStructLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 1),
    _MscExampleMiscellaneousOperStructLong_Type()
)
mscExampleMiscellaneousOperStructLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperStructLong.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeLong_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousOperFreeLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousOperFreeLong_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousOperFreeLong_Object = MibTableColumn
mscExampleMiscellaneousOperFreeLong = _MscExampleMiscellaneousOperFreeLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 2),
    _MscExampleMiscellaneousOperFreeLong_Type()
)
mscExampleMiscellaneousOperFreeLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLong.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeTime_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousOperFreeTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscExampleMiscellaneousOperFreeTime_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousOperFreeTime_Object = MibTableColumn
mscExampleMiscellaneousOperFreeTime = _MscExampleMiscellaneousOperFreeTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 3),
    _MscExampleMiscellaneousOperFreeTime_Type()
)
mscExampleMiscellaneousOperFreeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTime.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeTimeDateOnly_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousOperFreeTimeDateOnly based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_MscExampleMiscellaneousOperFreeTimeDateOnly_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousOperFreeTimeDateOnly_Object = MibTableColumn
mscExampleMiscellaneousOperFreeTimeDateOnly = _MscExampleMiscellaneousOperFreeTimeDateOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 4),
    _MscExampleMiscellaneousOperFreeTimeDateOnly_Type()
)
mscExampleMiscellaneousOperFreeTimeDateOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeDateOnly.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeTimeTimeOnly_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousOperFreeTimeTimeOnly based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_MscExampleMiscellaneousOperFreeTimeTimeOnly_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousOperFreeTimeTimeOnly_Object = MibTableColumn
mscExampleMiscellaneousOperFreeTimeTimeOnly = _MscExampleMiscellaneousOperFreeTimeTimeOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 5),
    _MscExampleMiscellaneousOperFreeTimeTimeOnly_Type()
)
mscExampleMiscellaneousOperFreeTimeTimeOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeTimeOnly.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeTimeDateTimeMinute_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousOperFreeTimeDateTimeMinute based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_MscExampleMiscellaneousOperFreeTimeDateTimeMinute_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousOperFreeTimeDateTimeMinute_Object = MibTableColumn
mscExampleMiscellaneousOperFreeTimeDateTimeMinute = _MscExampleMiscellaneousOperFreeTimeDateTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 6),
    _MscExampleMiscellaneousOperFreeTimeDateTimeMinute_Type()
)
mscExampleMiscellaneousOperFreeTimeDateTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeDateTimeMinute.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeCounter64_Type = PassportCounter64
_MscExampleMiscellaneousOperFreeCounter64_Object = MibTableColumn
mscExampleMiscellaneousOperFreeCounter64 = _MscExampleMiscellaneousOperFreeCounter64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 7),
    _MscExampleMiscellaneousOperFreeCounter64_Type()
)
mscExampleMiscellaneousOperFreeCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeCounter64.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeGauge64_Type(Gauge64):
    """Custom type mscExampleMiscellaneousOperFreeGauge64 based on Gauge64"""
    subtypeSpec = Gauge64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousOperFreeGauge64_Type.__name__ = "Gauge64"
_MscExampleMiscellaneousOperFreeGauge64_Object = MibTableColumn
mscExampleMiscellaneousOperFreeGauge64 = _MscExampleMiscellaneousOperFreeGauge64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 8),
    _MscExampleMiscellaneousOperFreeGauge64_Type()
)
mscExampleMiscellaneousOperFreeGauge64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeGauge64.setStatus("mandatory")
_MscExampleMiscellaneousOperStructCounter64_Type = PassportCounter64
_MscExampleMiscellaneousOperStructCounter64_Object = MibTableColumn
mscExampleMiscellaneousOperStructCounter64 = _MscExampleMiscellaneousOperStructCounter64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 10, 1, 9),
    _MscExampleMiscellaneousOperStructCounter64_Type()
)
mscExampleMiscellaneousOperStructCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperStructCounter64.setStatus("mandatory")
_MscExampleMiscellaneousProvisionalTable_Object = MibTable
mscExampleMiscellaneousProvisionalTable = _MscExampleMiscellaneousProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvisionalTable.setStatus("mandatory")
_MscExampleMiscellaneousProvisionalEntry_Object = MibTableRow
mscExampleMiscellaneousProvisionalEntry = _MscExampleMiscellaneousProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1)
)
mscExampleMiscellaneousProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvisionalEntry.setStatus("mandatory")
_MscExampleMiscellaneousProvEnumSub_Type = Link
_MscExampleMiscellaneousProvEnumSub_Object = MibTableColumn
mscExampleMiscellaneousProvEnumSub = _MscExampleMiscellaneousProvEnumSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 1),
    _MscExampleMiscellaneousProvEnumSub_Type()
)
mscExampleMiscellaneousProvEnumSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvEnumSub.setStatus("mandatory")


class _MscExampleMiscellaneousProvStructLong_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousProvStructLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvStructLong_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousProvStructLong_Object = MibTableColumn
mscExampleMiscellaneousProvStructLong = _MscExampleMiscellaneousProvStructLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 2),
    _MscExampleMiscellaneousProvStructLong_Type()
)
mscExampleMiscellaneousProvStructLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvStructLong.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeLong_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousProvFreeLong based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvFreeLong_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousProvFreeLong_Object = MibTableColumn
mscExampleMiscellaneousProvFreeLong = _MscExampleMiscellaneousProvFreeLong_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 3),
    _MscExampleMiscellaneousProvFreeLong_Type()
)
mscExampleMiscellaneousProvFreeLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLong.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTime_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTime based on EnterpriseDateAndTime"""
    defaultHexValue = "313939322d31302d31352031303a33393a3030"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscExampleMiscellaneousProvFreeTime_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTime_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTime = _MscExampleMiscellaneousProvFreeTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 4),
    _MscExampleMiscellaneousProvFreeTime_Type()
)
mscExampleMiscellaneousProvFreeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTime.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeDateOnly_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeDateOnly based on EnterpriseDateAndTime"""
    defaultHexValue = "313939322d31302d3135"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_MscExampleMiscellaneousProvFreeTimeDateOnly_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeDateOnly_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeDateOnly = _MscExampleMiscellaneousProvFreeTimeDateOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 5),
    _MscExampleMiscellaneousProvFreeTimeDateOnly_Type()
)
mscExampleMiscellaneousProvFreeTimeDateOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeDateOnly.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeTimeOnly_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeTimeOnly based on EnterpriseDateAndTime"""
    defaultHexValue = "31303a3339"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_MscExampleMiscellaneousProvFreeTimeTimeOnly_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeTimeOnly_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeTimeOnly = _MscExampleMiscellaneousProvFreeTimeTimeOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 6),
    _MscExampleMiscellaneousProvFreeTimeTimeOnly_Type()
)
mscExampleMiscellaneousProvFreeTimeTimeOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeTimeOnly.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeDateTimeMinute_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeDateTimeMinute based on EnterpriseDateAndTime"""
    defaultHexValue = "313939322d31302d31352031303a3330"

    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_MscExampleMiscellaneousProvFreeTimeDateTimeMinute_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeDateTimeMinute_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeDateTimeMinute = _MscExampleMiscellaneousProvFreeTimeDateTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 7),
    _MscExampleMiscellaneousProvFreeTimeDateTimeMinute_Type()
)
mscExampleMiscellaneousProvFreeTimeDateTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeDateTimeMinute.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTime1_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTime1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscExampleMiscellaneousProvFreeTime1_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTime1_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTime1 = _MscExampleMiscellaneousProvFreeTime1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 8),
    _MscExampleMiscellaneousProvFreeTime1_Type()
)
mscExampleMiscellaneousProvFreeTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTime1.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeDateOnly1_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeDateOnly1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_MscExampleMiscellaneousProvFreeTimeDateOnly1_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeDateOnly1_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeDateOnly1 = _MscExampleMiscellaneousProvFreeTimeDateOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 9),
    _MscExampleMiscellaneousProvFreeTimeDateOnly1_Type()
)
mscExampleMiscellaneousProvFreeTimeDateOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeDateOnly1.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeTimeOnly1_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeTimeOnly1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvFreeTimeTimeOnly1_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeTimeOnly1_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeTimeOnly1 = _MscExampleMiscellaneousProvFreeTimeTimeOnly1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 10),
    _MscExampleMiscellaneousProvFreeTimeTimeOnly1_Type()
)
mscExampleMiscellaneousProvFreeTimeTimeOnly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeTimeOnly1.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeDateTimeMinute1_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeDateTimeMinute1 based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_MscExampleMiscellaneousProvFreeTimeDateTimeMinute1_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeDateTimeMinute1_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeDateTimeMinute1 = _MscExampleMiscellaneousProvFreeTimeDateTimeMinute1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 11, 1, 11),
    _MscExampleMiscellaneousProvFreeTimeDateTimeMinute1_Type()
)
mscExampleMiscellaneousProvFreeTimeDateTimeMinute1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeDateTimeMinute1.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongReplicatedTable_Object = MibTable
mscExampleMiscellaneousOperFreeLongReplicatedTable = _MscExampleMiscellaneousOperFreeLongReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1177)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongReplicatedTable.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongReplicatedEntry_Object = MibTableRow
mscExampleMiscellaneousOperFreeLongReplicatedEntry = _MscExampleMiscellaneousOperFreeLongReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1177, 1)
)
mscExampleMiscellaneousOperFreeLongReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousOperFreeLongReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongReplicatedEntry.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongReplicatedIndex_Type = Unsigned64
_MscExampleMiscellaneousOperFreeLongReplicatedIndex_Object = MibTableColumn
mscExampleMiscellaneousOperFreeLongReplicatedIndex = _MscExampleMiscellaneousOperFreeLongReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1177, 1, 1),
    _MscExampleMiscellaneousOperFreeLongReplicatedIndex_Type()
)
mscExampleMiscellaneousOperFreeLongReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongReplicatedIndex.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeLongReplicatedValue_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousOperFreeLongReplicatedValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousOperFreeLongReplicatedValue_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousOperFreeLongReplicatedValue_Object = MibTableColumn
mscExampleMiscellaneousOperFreeLongReplicatedValue = _MscExampleMiscellaneousOperFreeLongReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1177, 1, 2),
    _MscExampleMiscellaneousOperFreeLongReplicatedValue_Type()
)
mscExampleMiscellaneousOperFreeLongReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongReplicatedValue.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongReplicatedRowStatus_Type = RowStatus
_MscExampleMiscellaneousOperFreeLongReplicatedRowStatus_Object = MibTableColumn
mscExampleMiscellaneousOperFreeLongReplicatedRowStatus = _MscExampleMiscellaneousOperFreeLongReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1177, 1, 3),
    _MscExampleMiscellaneousOperFreeLongReplicatedRowStatus_Type()
)
mscExampleMiscellaneousOperFreeLongReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongReplicatedRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongListTable_Object = MibTable
mscExampleMiscellaneousOperFreeLongListTable = _MscExampleMiscellaneousOperFreeLongListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1178)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongListTable.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongListEntry_Object = MibTableRow
mscExampleMiscellaneousOperFreeLongListEntry = _MscExampleMiscellaneousOperFreeLongListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1178, 1)
)
mscExampleMiscellaneousOperFreeLongListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousOperFreeLongListValue"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongListEntry.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeLongListValue_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousOperFreeLongListValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousOperFreeLongListValue_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousOperFreeLongListValue_Object = MibTableColumn
mscExampleMiscellaneousOperFreeLongListValue = _MscExampleMiscellaneousOperFreeLongListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1178, 1, 1),
    _MscExampleMiscellaneousOperFreeLongListValue_Type()
)
mscExampleMiscellaneousOperFreeLongListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongListValue.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeLongListRowStatus_Type = RowStatus
_MscExampleMiscellaneousOperFreeLongListRowStatus_Object = MibTableColumn
mscExampleMiscellaneousOperFreeLongListRowStatus = _MscExampleMiscellaneousOperFreeLongListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1178, 1, 2),
    _MscExampleMiscellaneousOperFreeLongListRowStatus_Type()
)
mscExampleMiscellaneousOperFreeLongListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeLongListRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeTimeListTable_Object = MibTable
mscExampleMiscellaneousOperFreeTimeListTable = _MscExampleMiscellaneousOperFreeTimeListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1179)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeListTable.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeTimeListEntry_Object = MibTableRow
mscExampleMiscellaneousOperFreeTimeListEntry = _MscExampleMiscellaneousOperFreeTimeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1179, 1)
)
mscExampleMiscellaneousOperFreeTimeListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousOperFreeTimeListValue"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeListEntry.setStatus("mandatory")


class _MscExampleMiscellaneousOperFreeTimeListValue_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousOperFreeTimeListValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MscExampleMiscellaneousOperFreeTimeListValue_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousOperFreeTimeListValue_Object = MibTableColumn
mscExampleMiscellaneousOperFreeTimeListValue = _MscExampleMiscellaneousOperFreeTimeListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1179, 1, 1),
    _MscExampleMiscellaneousOperFreeTimeListValue_Type()
)
mscExampleMiscellaneousOperFreeTimeListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeListValue.setStatus("mandatory")
_MscExampleMiscellaneousOperFreeTimeListRowStatus_Type = RowStatus
_MscExampleMiscellaneousOperFreeTimeListRowStatus_Object = MibTableColumn
mscExampleMiscellaneousOperFreeTimeListRowStatus = _MscExampleMiscellaneousOperFreeTimeListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1179, 1, 2),
    _MscExampleMiscellaneousOperFreeTimeListRowStatus_Type()
)
mscExampleMiscellaneousOperFreeTimeListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousOperFreeTimeListRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongReplicatedTable_Object = MibTable
mscExampleMiscellaneousProvFreeLongReplicatedTable = _MscExampleMiscellaneousProvFreeLongReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1180)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongReplicatedTable.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongReplicatedEntry_Object = MibTableRow
mscExampleMiscellaneousProvFreeLongReplicatedEntry = _MscExampleMiscellaneousProvFreeLongReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1180, 1)
)
mscExampleMiscellaneousProvFreeLongReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeLongReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongReplicatedEntry.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongReplicatedIndex_Type = Unsigned64
_MscExampleMiscellaneousProvFreeLongReplicatedIndex_Object = MibTableColumn
mscExampleMiscellaneousProvFreeLongReplicatedIndex = _MscExampleMiscellaneousProvFreeLongReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1180, 1, 1),
    _MscExampleMiscellaneousProvFreeLongReplicatedIndex_Type()
)
mscExampleMiscellaneousProvFreeLongReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongReplicatedIndex.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeLongReplicatedValue_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousProvFreeLongReplicatedValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvFreeLongReplicatedValue_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousProvFreeLongReplicatedValue_Object = MibTableColumn
mscExampleMiscellaneousProvFreeLongReplicatedValue = _MscExampleMiscellaneousProvFreeLongReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1180, 1, 2),
    _MscExampleMiscellaneousProvFreeLongReplicatedValue_Type()
)
mscExampleMiscellaneousProvFreeLongReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongReplicatedValue.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongReplicatedRowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeLongReplicatedRowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeLongReplicatedRowStatus = _MscExampleMiscellaneousProvFreeLongReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1180, 1, 3),
    _MscExampleMiscellaneousProvFreeLongReplicatedRowStatus_Type()
)
mscExampleMiscellaneousProvFreeLongReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongReplicatedRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongListTable_Object = MibTable
mscExampleMiscellaneousProvFreeLongListTable = _MscExampleMiscellaneousProvFreeLongListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1181)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongListTable.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongListEntry_Object = MibTableRow
mscExampleMiscellaneousProvFreeLongListEntry = _MscExampleMiscellaneousProvFreeLongListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1181, 1)
)
mscExampleMiscellaneousProvFreeLongListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeLongListValue"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongListEntry.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeLongListValue_Type(Unsigned64):
    """Custom type mscExampleMiscellaneousProvFreeLongListValue based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvFreeLongListValue_Type.__name__ = "Unsigned64"
_MscExampleMiscellaneousProvFreeLongListValue_Object = MibTableColumn
mscExampleMiscellaneousProvFreeLongListValue = _MscExampleMiscellaneousProvFreeLongListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1181, 1, 1),
    _MscExampleMiscellaneousProvFreeLongListValue_Type()
)
mscExampleMiscellaneousProvFreeLongListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongListValue.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeLongListRowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeLongListRowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeLongListRowStatus = _MscExampleMiscellaneousProvFreeLongListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1181, 1, 2),
    _MscExampleMiscellaneousProvFreeLongListRowStatus_Type()
)
mscExampleMiscellaneousProvFreeLongListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeLongListRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeReplicatedTable_Object = MibTable
mscExampleMiscellaneousProvFreeTimeReplicatedTable = _MscExampleMiscellaneousProvFreeTimeReplicatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1182)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeReplicatedTable.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeReplicatedEntry_Object = MibTableRow
mscExampleMiscellaneousProvFreeTimeReplicatedEntry = _MscExampleMiscellaneousProvFreeTimeReplicatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1182, 1)
)
mscExampleMiscellaneousProvFreeTimeReplicatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeTimeReplicatedIndex"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeReplicatedEntry.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeReplicatedIndex_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeReplicatedIndex based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_MscExampleMiscellaneousProvFreeTimeReplicatedIndex_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeReplicatedIndex_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeReplicatedIndex = _MscExampleMiscellaneousProvFreeTimeReplicatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1182, 1, 1),
    _MscExampleMiscellaneousProvFreeTimeReplicatedIndex_Type()
)
mscExampleMiscellaneousProvFreeTimeReplicatedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeReplicatedIndex.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeReplicatedValue_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeReplicatedValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvFreeTimeReplicatedValue_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeReplicatedValue_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeReplicatedValue = _MscExampleMiscellaneousProvFreeTimeReplicatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1182, 1, 2),
    _MscExampleMiscellaneousProvFreeTimeReplicatedValue_Type()
)
mscExampleMiscellaneousProvFreeTimeReplicatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeReplicatedValue.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeReplicatedRowStatus = _MscExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1182, 1, 3),
    _MscExampleMiscellaneousProvFreeTimeReplicatedRowStatus_Type()
)
mscExampleMiscellaneousProvFreeTimeReplicatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeReplicatedRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeListTable_Object = MibTable
mscExampleMiscellaneousProvFreeTimeListTable = _MscExampleMiscellaneousProvFreeTimeListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1183)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeListTable.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeListEntry_Object = MibTableRow
mscExampleMiscellaneousProvFreeTimeListEntry = _MscExampleMiscellaneousProvFreeTimeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1183, 1)
)
mscExampleMiscellaneousProvFreeTimeListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeTimeListValue"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeListEntry.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeListValue_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeListValue based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_MscExampleMiscellaneousProvFreeTimeListValue_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeListValue_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeListValue = _MscExampleMiscellaneousProvFreeTimeListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1183, 1, 1),
    _MscExampleMiscellaneousProvFreeTimeListValue_Type()
)
mscExampleMiscellaneousProvFreeTimeListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeListValue.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeListRowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeTimeListRowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeListRowStatus = _MscExampleMiscellaneousProvFreeTimeListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1183, 1, 2),
    _MscExampleMiscellaneousProvFreeTimeListRowStatus_Type()
)
mscExampleMiscellaneousProvFreeTimeListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeListRowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList1Table_Object = MibTable
mscExampleMiscellaneousProvFreeTimeList1Table = _MscExampleMiscellaneousProvFreeTimeList1Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1184)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList1Table.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList1Entry_Object = MibTableRow
mscExampleMiscellaneousProvFreeTimeList1Entry = _MscExampleMiscellaneousProvFreeTimeList1Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1184, 1)
)
mscExampleMiscellaneousProvFreeTimeList1Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeTimeList1Value"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList1Entry.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeList1Value_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeList1Value based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_MscExampleMiscellaneousProvFreeTimeList1Value_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeList1Value_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeList1Value = _MscExampleMiscellaneousProvFreeTimeList1Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1184, 1, 1),
    _MscExampleMiscellaneousProvFreeTimeList1Value_Type()
)
mscExampleMiscellaneousProvFreeTimeList1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList1Value.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList1RowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeTimeList1RowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeList1RowStatus = _MscExampleMiscellaneousProvFreeTimeList1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1184, 1, 2),
    _MscExampleMiscellaneousProvFreeTimeList1RowStatus_Type()
)
mscExampleMiscellaneousProvFreeTimeList1RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList1RowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList2Table_Object = MibTable
mscExampleMiscellaneousProvFreeTimeList2Table = _MscExampleMiscellaneousProvFreeTimeList2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1185)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList2Table.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList2Entry_Object = MibTableRow
mscExampleMiscellaneousProvFreeTimeList2Entry = _MscExampleMiscellaneousProvFreeTimeList2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1185, 1)
)
mscExampleMiscellaneousProvFreeTimeList2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeTimeList2Value"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList2Entry.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeList2Value_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeList2Value based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscExampleMiscellaneousProvFreeTimeList2Value_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeList2Value_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeList2Value = _MscExampleMiscellaneousProvFreeTimeList2Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1185, 1, 1),
    _MscExampleMiscellaneousProvFreeTimeList2Value_Type()
)
mscExampleMiscellaneousProvFreeTimeList2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList2Value.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList2RowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeTimeList2RowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeList2RowStatus = _MscExampleMiscellaneousProvFreeTimeList2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1185, 1, 2),
    _MscExampleMiscellaneousProvFreeTimeList2RowStatus_Type()
)
mscExampleMiscellaneousProvFreeTimeList2RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList2RowStatus.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList3Table_Object = MibTable
mscExampleMiscellaneousProvFreeTimeList3Table = _MscExampleMiscellaneousProvFreeTimeList3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1186)
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList3Table.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList3Entry_Object = MibTableRow
mscExampleMiscellaneousProvFreeTimeList3Entry = _MscExampleMiscellaneousProvFreeTimeList3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1186, 1)
)
mscExampleMiscellaneousProvFreeTimeList3Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleMiscellaneousProvFreeTimeList3Value"),
)
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList3Entry.setStatus("mandatory")


class _MscExampleMiscellaneousProvFreeTimeList3Value_Type(EnterpriseDateAndTime):
    """Custom type mscExampleMiscellaneousProvFreeTimeList3Value based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MscExampleMiscellaneousProvFreeTimeList3Value_Type.__name__ = "EnterpriseDateAndTime"
_MscExampleMiscellaneousProvFreeTimeList3Value_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeList3Value = _MscExampleMiscellaneousProvFreeTimeList3Value_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1186, 1, 1),
    _MscExampleMiscellaneousProvFreeTimeList3Value_Type()
)
mscExampleMiscellaneousProvFreeTimeList3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList3Value.setStatus("mandatory")
_MscExampleMiscellaneousProvFreeTimeList3RowStatus_Type = RowStatus
_MscExampleMiscellaneousProvFreeTimeList3RowStatus_Object = MibTableColumn
mscExampleMiscellaneousProvFreeTimeList3RowStatus = _MscExampleMiscellaneousProvFreeTimeList3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 15, 1186, 1, 2),
    _MscExampleMiscellaneousProvFreeTimeList3RowStatus_Type()
)
mscExampleMiscellaneousProvFreeTimeList3RowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleMiscellaneousProvFreeTimeList3RowStatus.setStatus("mandatory")
_MscExampleOneIndex_ObjectIdentity = ObjectIdentity
mscExampleOneIndex = _MscExampleOneIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16)
)
_MscExampleOneIndexRowStatusTable_Object = MibTable
mscExampleOneIndexRowStatusTable = _MscExampleOneIndexRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 1)
)
if mibBuilder.loadTexts:
    mscExampleOneIndexRowStatusTable.setStatus("mandatory")
_MscExampleOneIndexRowStatusEntry_Object = MibTableRow
mscExampleOneIndexRowStatusEntry = _MscExampleOneIndexRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 1, 1)
)
mscExampleOneIndexRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOneIndexOneIndex"),
)
if mibBuilder.loadTexts:
    mscExampleOneIndexRowStatusEntry.setStatus("mandatory")
_MscExampleOneIndexRowStatus_Type = RowStatus
_MscExampleOneIndexRowStatus_Object = MibTableColumn
mscExampleOneIndexRowStatus = _MscExampleOneIndexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 1, 1, 1),
    _MscExampleOneIndexRowStatus_Type()
)
mscExampleOneIndexRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOneIndexRowStatus.setStatus("mandatory")
_MscExampleOneIndexComponentName_Type = DisplayString
_MscExampleOneIndexComponentName_Object = MibTableColumn
mscExampleOneIndexComponentName = _MscExampleOneIndexComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 1, 1, 2),
    _MscExampleOneIndexComponentName_Type()
)
mscExampleOneIndexComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleOneIndexComponentName.setStatus("mandatory")
_MscExampleOneIndexStorageType_Type = StorageType
_MscExampleOneIndexStorageType_Object = MibTableColumn
mscExampleOneIndexStorageType = _MscExampleOneIndexStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 1, 1, 4),
    _MscExampleOneIndexStorageType_Type()
)
mscExampleOneIndexStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleOneIndexStorageType.setStatus("mandatory")


class _MscExampleOneIndexOneIndex_Type(Integer32):
    """Custom type mscExampleOneIndexOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleOneIndexOneIndex_Type.__name__ = "Integer32"
_MscExampleOneIndexOneIndex_Object = MibTableColumn
mscExampleOneIndexOneIndex = _MscExampleOneIndexOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 1, 1, 10),
    _MscExampleOneIndexOneIndex_Type()
)
mscExampleOneIndexOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleOneIndexOneIndex.setStatus("mandatory")
_MscExampleOneIndexProvisionedTable_Object = MibTable
mscExampleOneIndexProvisionedTable = _MscExampleOneIndexProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 10)
)
if mibBuilder.loadTexts:
    mscExampleOneIndexProvisionedTable.setStatus("mandatory")
_MscExampleOneIndexProvisionedEntry_Object = MibTableRow
mscExampleOneIndexProvisionedEntry = _MscExampleOneIndexProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 10, 1)
)
mscExampleOneIndexProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOneIndexOneIndex"),
)
if mibBuilder.loadTexts:
    mscExampleOneIndexProvisionedEntry.setStatus("mandatory")


class _MscExampleOneIndexProvAttribute_Type(Unsigned32):
    """Custom type mscExampleOneIndexProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleOneIndexProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleOneIndexProvAttribute_Object = MibTableColumn
mscExampleOneIndexProvAttribute = _MscExampleOneIndexProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 16, 10, 1, 1),
    _MscExampleOneIndexProvAttribute_Type()
)
mscExampleOneIndexProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOneIndexProvAttribute.setStatus("mandatory")
_MscExampleTwoIndices_ObjectIdentity = ObjectIdentity
mscExampleTwoIndices = _MscExampleTwoIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17)
)
_MscExampleTwoIndicesRowStatusTable_Object = MibTable
mscExampleTwoIndicesRowStatusTable = _MscExampleTwoIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1)
)
if mibBuilder.loadTexts:
    mscExampleTwoIndicesRowStatusTable.setStatus("mandatory")
_MscExampleTwoIndicesRowStatusEntry_Object = MibTableRow
mscExampleTwoIndicesRowStatusEntry = _MscExampleTwoIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1, 1)
)
mscExampleTwoIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleTwoIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleTwoIndicesTwoIndex"),
)
if mibBuilder.loadTexts:
    mscExampleTwoIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleTwoIndicesRowStatus_Type = RowStatus
_MscExampleTwoIndicesRowStatus_Object = MibTableColumn
mscExampleTwoIndicesRowStatus = _MscExampleTwoIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1, 1, 1),
    _MscExampleTwoIndicesRowStatus_Type()
)
mscExampleTwoIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleTwoIndicesRowStatus.setStatus("mandatory")
_MscExampleTwoIndicesComponentName_Type = DisplayString
_MscExampleTwoIndicesComponentName_Object = MibTableColumn
mscExampleTwoIndicesComponentName = _MscExampleTwoIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1, 1, 2),
    _MscExampleTwoIndicesComponentName_Type()
)
mscExampleTwoIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleTwoIndicesComponentName.setStatus("mandatory")
_MscExampleTwoIndicesStorageType_Type = StorageType
_MscExampleTwoIndicesStorageType_Object = MibTableColumn
mscExampleTwoIndicesStorageType = _MscExampleTwoIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1, 1, 4),
    _MscExampleTwoIndicesStorageType_Type()
)
mscExampleTwoIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleTwoIndicesStorageType.setStatus("mandatory")


class _MscExampleTwoIndicesOneIndex_Type(Integer32):
    """Custom type mscExampleTwoIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleTwoIndicesOneIndex_Type.__name__ = "Integer32"
_MscExampleTwoIndicesOneIndex_Object = MibTableColumn
mscExampleTwoIndicesOneIndex = _MscExampleTwoIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1, 1, 10),
    _MscExampleTwoIndicesOneIndex_Type()
)
mscExampleTwoIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleTwoIndicesOneIndex.setStatus("mandatory")


class _MscExampleTwoIndicesTwoIndex_Type(Integer32):
    """Custom type mscExampleTwoIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleTwoIndicesTwoIndex_Type.__name__ = "Integer32"
_MscExampleTwoIndicesTwoIndex_Object = MibTableColumn
mscExampleTwoIndicesTwoIndex = _MscExampleTwoIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 1, 1, 11),
    _MscExampleTwoIndicesTwoIndex_Type()
)
mscExampleTwoIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleTwoIndicesTwoIndex.setStatus("mandatory")
_MscExampleTwoIndicesProvisionedTable_Object = MibTable
mscExampleTwoIndicesProvisionedTable = _MscExampleTwoIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 10)
)
if mibBuilder.loadTexts:
    mscExampleTwoIndicesProvisionedTable.setStatus("mandatory")
_MscExampleTwoIndicesProvisionedEntry_Object = MibTableRow
mscExampleTwoIndicesProvisionedEntry = _MscExampleTwoIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 10, 1)
)
mscExampleTwoIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleTwoIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleTwoIndicesTwoIndex"),
)
if mibBuilder.loadTexts:
    mscExampleTwoIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleTwoIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleTwoIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleTwoIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleTwoIndicesProvAttribute_Object = MibTableColumn
mscExampleTwoIndicesProvAttribute = _MscExampleTwoIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 17, 10, 1, 1),
    _MscExampleTwoIndicesProvAttribute_Type()
)
mscExampleTwoIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleTwoIndicesProvAttribute.setStatus("mandatory")
_MscExampleThreeIndices_ObjectIdentity = ObjectIdentity
mscExampleThreeIndices = _MscExampleThreeIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18)
)
_MscExampleThreeIndicesRowStatusTable_Object = MibTable
mscExampleThreeIndicesRowStatusTable = _MscExampleThreeIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1)
)
if mibBuilder.loadTexts:
    mscExampleThreeIndicesRowStatusTable.setStatus("mandatory")
_MscExampleThreeIndicesRowStatusEntry_Object = MibTableRow
mscExampleThreeIndicesRowStatusEntry = _MscExampleThreeIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1)
)
mscExampleThreeIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleThreeIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleThreeIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleThreeIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleThreeIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleThreeIndicesRowStatus_Type = RowStatus
_MscExampleThreeIndicesRowStatus_Object = MibTableColumn
mscExampleThreeIndicesRowStatus = _MscExampleThreeIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1, 1),
    _MscExampleThreeIndicesRowStatus_Type()
)
mscExampleThreeIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesRowStatus.setStatus("mandatory")
_MscExampleThreeIndicesComponentName_Type = DisplayString
_MscExampleThreeIndicesComponentName_Object = MibTableColumn
mscExampleThreeIndicesComponentName = _MscExampleThreeIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1, 2),
    _MscExampleThreeIndicesComponentName_Type()
)
mscExampleThreeIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesComponentName.setStatus("mandatory")
_MscExampleThreeIndicesStorageType_Type = StorageType
_MscExampleThreeIndicesStorageType_Object = MibTableColumn
mscExampleThreeIndicesStorageType = _MscExampleThreeIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1, 4),
    _MscExampleThreeIndicesStorageType_Type()
)
mscExampleThreeIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesStorageType.setStatus("mandatory")


class _MscExampleThreeIndicesOneIndex_Type(Integer32):
    """Custom type mscExampleThreeIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleThreeIndicesOneIndex_Type.__name__ = "Integer32"
_MscExampleThreeIndicesOneIndex_Object = MibTableColumn
mscExampleThreeIndicesOneIndex = _MscExampleThreeIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1, 10),
    _MscExampleThreeIndicesOneIndex_Type()
)
mscExampleThreeIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesOneIndex.setStatus("mandatory")


class _MscExampleThreeIndicesTwoIndex_Type(Integer32):
    """Custom type mscExampleThreeIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleThreeIndicesTwoIndex_Type.__name__ = "Integer32"
_MscExampleThreeIndicesTwoIndex_Object = MibTableColumn
mscExampleThreeIndicesTwoIndex = _MscExampleThreeIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1, 11),
    _MscExampleThreeIndicesTwoIndex_Type()
)
mscExampleThreeIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesTwoIndex.setStatus("mandatory")


class _MscExampleThreeIndicesThreeIndex_Type(Integer32):
    """Custom type mscExampleThreeIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleThreeIndicesThreeIndex_Type.__name__ = "Integer32"
_MscExampleThreeIndicesThreeIndex_Object = MibTableColumn
mscExampleThreeIndicesThreeIndex = _MscExampleThreeIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 1, 1, 12),
    _MscExampleThreeIndicesThreeIndex_Type()
)
mscExampleThreeIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesThreeIndex.setStatus("mandatory")
_MscExampleThreeIndicesProvisionedTable_Object = MibTable
mscExampleThreeIndicesProvisionedTable = _MscExampleThreeIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 10)
)
if mibBuilder.loadTexts:
    mscExampleThreeIndicesProvisionedTable.setStatus("mandatory")
_MscExampleThreeIndicesProvisionedEntry_Object = MibTableRow
mscExampleThreeIndicesProvisionedEntry = _MscExampleThreeIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 10, 1)
)
mscExampleThreeIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleThreeIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleThreeIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleThreeIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleThreeIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleThreeIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleThreeIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleThreeIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleThreeIndicesProvAttribute_Object = MibTableColumn
mscExampleThreeIndicesProvAttribute = _MscExampleThreeIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 18, 10, 1, 1),
    _MscExampleThreeIndicesProvAttribute_Type()
)
mscExampleThreeIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleThreeIndicesProvAttribute.setStatus("mandatory")
_MscExampleFourIndices_ObjectIdentity = ObjectIdentity
mscExampleFourIndices = _MscExampleFourIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19)
)
_MscExampleFourIndicesRowStatusTable_Object = MibTable
mscExampleFourIndicesRowStatusTable = _MscExampleFourIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1)
)
if mibBuilder.loadTexts:
    mscExampleFourIndicesRowStatusTable.setStatus("mandatory")
_MscExampleFourIndicesRowStatusEntry_Object = MibTableRow
mscExampleFourIndicesRowStatusEntry = _MscExampleFourIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1)
)
mscExampleFourIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesThreeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesFourIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFourIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleFourIndicesRowStatus_Type = RowStatus
_MscExampleFourIndicesRowStatus_Object = MibTableColumn
mscExampleFourIndicesRowStatus = _MscExampleFourIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 1),
    _MscExampleFourIndicesRowStatus_Type()
)
mscExampleFourIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFourIndicesRowStatus.setStatus("mandatory")
_MscExampleFourIndicesComponentName_Type = DisplayString
_MscExampleFourIndicesComponentName_Object = MibTableColumn
mscExampleFourIndicesComponentName = _MscExampleFourIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 2),
    _MscExampleFourIndicesComponentName_Type()
)
mscExampleFourIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleFourIndicesComponentName.setStatus("mandatory")
_MscExampleFourIndicesStorageType_Type = StorageType
_MscExampleFourIndicesStorageType_Object = MibTableColumn
mscExampleFourIndicesStorageType = _MscExampleFourIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 4),
    _MscExampleFourIndicesStorageType_Type()
)
mscExampleFourIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleFourIndicesStorageType.setStatus("mandatory")


class _MscExampleFourIndicesOneIndex_Type(Integer32):
    """Custom type mscExampleFourIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleFourIndicesOneIndex_Type.__name__ = "Integer32"
_MscExampleFourIndicesOneIndex_Object = MibTableColumn
mscExampleFourIndicesOneIndex = _MscExampleFourIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 10),
    _MscExampleFourIndicesOneIndex_Type()
)
mscExampleFourIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFourIndicesOneIndex.setStatus("mandatory")


class _MscExampleFourIndicesTwoIndex_Type(Integer32):
    """Custom type mscExampleFourIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleFourIndicesTwoIndex_Type.__name__ = "Integer32"
_MscExampleFourIndicesTwoIndex_Object = MibTableColumn
mscExampleFourIndicesTwoIndex = _MscExampleFourIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 11),
    _MscExampleFourIndicesTwoIndex_Type()
)
mscExampleFourIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFourIndicesTwoIndex.setStatus("mandatory")


class _MscExampleFourIndicesThreeIndex_Type(Integer32):
    """Custom type mscExampleFourIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleFourIndicesThreeIndex_Type.__name__ = "Integer32"
_MscExampleFourIndicesThreeIndex_Object = MibTableColumn
mscExampleFourIndicesThreeIndex = _MscExampleFourIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 12),
    _MscExampleFourIndicesThreeIndex_Type()
)
mscExampleFourIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFourIndicesThreeIndex.setStatus("mandatory")


class _MscExampleFourIndicesFourIndex_Type(Integer32):
    """Custom type mscExampleFourIndicesFourIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleFourIndicesFourIndex_Type.__name__ = "Integer32"
_MscExampleFourIndicesFourIndex_Object = MibTableColumn
mscExampleFourIndicesFourIndex = _MscExampleFourIndicesFourIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 1, 1, 13),
    _MscExampleFourIndicesFourIndex_Type()
)
mscExampleFourIndicesFourIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleFourIndicesFourIndex.setStatus("mandatory")
_MscExampleFourIndicesProvisionedTable_Object = MibTable
mscExampleFourIndicesProvisionedTable = _MscExampleFourIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 10)
)
if mibBuilder.loadTexts:
    mscExampleFourIndicesProvisionedTable.setStatus("mandatory")
_MscExampleFourIndicesProvisionedEntry_Object = MibTableRow
mscExampleFourIndicesProvisionedEntry = _MscExampleFourIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 10, 1)
)
mscExampleFourIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesThreeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleFourIndicesFourIndex"),
)
if mibBuilder.loadTexts:
    mscExampleFourIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleFourIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleFourIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleFourIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleFourIndicesProvAttribute_Object = MibTableColumn
mscExampleFourIndicesProvAttribute = _MscExampleFourIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 19, 10, 1, 1),
    _MscExampleFourIndicesProvAttribute_Type()
)
mscExampleFourIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleFourIndicesProvAttribute.setStatus("mandatory")
_MscExampleDecimalIndices_ObjectIdentity = ObjectIdentity
mscExampleDecimalIndices = _MscExampleDecimalIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20)
)
_MscExampleDecimalIndicesRowStatusTable_Object = MibTable
mscExampleDecimalIndicesRowStatusTable = _MscExampleDecimalIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1)
)
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesRowStatusTable.setStatus("mandatory")
_MscExampleDecimalIndicesRowStatusEntry_Object = MibTableRow
mscExampleDecimalIndicesRowStatusEntry = _MscExampleDecimalIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1)
)
mscExampleDecimalIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleDecimalIndicesRowStatus_Type = RowStatus
_MscExampleDecimalIndicesRowStatus_Object = MibTableColumn
mscExampleDecimalIndicesRowStatus = _MscExampleDecimalIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1, 1),
    _MscExampleDecimalIndicesRowStatus_Type()
)
mscExampleDecimalIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesRowStatus.setStatus("mandatory")
_MscExampleDecimalIndicesComponentName_Type = DisplayString
_MscExampleDecimalIndicesComponentName_Object = MibTableColumn
mscExampleDecimalIndicesComponentName = _MscExampleDecimalIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1, 2),
    _MscExampleDecimalIndicesComponentName_Type()
)
mscExampleDecimalIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesComponentName.setStatus("mandatory")
_MscExampleDecimalIndicesStorageType_Type = StorageType
_MscExampleDecimalIndicesStorageType_Object = MibTableColumn
mscExampleDecimalIndicesStorageType = _MscExampleDecimalIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1, 4),
    _MscExampleDecimalIndicesStorageType_Type()
)
mscExampleDecimalIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesStorageType.setStatus("mandatory")


class _MscExampleDecimalIndicesOneIndex_Type(Integer32):
    """Custom type mscExampleDecimalIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 100),
    )


_MscExampleDecimalIndicesOneIndex_Type.__name__ = "Integer32"
_MscExampleDecimalIndicesOneIndex_Object = MibTableColumn
mscExampleDecimalIndicesOneIndex = _MscExampleDecimalIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1, 10),
    _MscExampleDecimalIndicesOneIndex_Type()
)
mscExampleDecimalIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesOneIndex.setStatus("mandatory")


class _MscExampleDecimalIndicesTwoIndex_Type(Integer32):
    """Custom type mscExampleDecimalIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 100),
    )


_MscExampleDecimalIndicesTwoIndex_Type.__name__ = "Integer32"
_MscExampleDecimalIndicesTwoIndex_Object = MibTableColumn
mscExampleDecimalIndicesTwoIndex = _MscExampleDecimalIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1, 11),
    _MscExampleDecimalIndicesTwoIndex_Type()
)
mscExampleDecimalIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesTwoIndex.setStatus("mandatory")


class _MscExampleDecimalIndicesThreeIndex_Type(Integer32):
    """Custom type mscExampleDecimalIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(100, 100),
    )


_MscExampleDecimalIndicesThreeIndex_Type.__name__ = "Integer32"
_MscExampleDecimalIndicesThreeIndex_Object = MibTableColumn
mscExampleDecimalIndicesThreeIndex = _MscExampleDecimalIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 1, 1, 12),
    _MscExampleDecimalIndicesThreeIndex_Type()
)
mscExampleDecimalIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesThreeIndex.setStatus("mandatory")
_MscExampleDecimalIndicesProvisionedTable_Object = MibTable
mscExampleDecimalIndicesProvisionedTable = _MscExampleDecimalIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 10)
)
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesProvisionedTable.setStatus("mandatory")
_MscExampleDecimalIndicesProvisionedEntry_Object = MibTableRow
mscExampleDecimalIndicesProvisionedEntry = _MscExampleDecimalIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 10, 1)
)
mscExampleDecimalIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDecimalIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleDecimalIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleDecimalIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDecimalIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleDecimalIndicesProvAttribute_Object = MibTableColumn
mscExampleDecimalIndicesProvAttribute = _MscExampleDecimalIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 20, 10, 1, 1),
    _MscExampleDecimalIndicesProvAttribute_Type()
)
mscExampleDecimalIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDecimalIndicesProvAttribute.setStatus("mandatory")
_MscExampleHexIndices_ObjectIdentity = ObjectIdentity
mscExampleHexIndices = _MscExampleHexIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21)
)
_MscExampleHexIndicesRowStatusTable_Object = MibTable
mscExampleHexIndicesRowStatusTable = _MscExampleHexIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1)
)
if mibBuilder.loadTexts:
    mscExampleHexIndicesRowStatusTable.setStatus("mandatory")
_MscExampleHexIndicesRowStatusEntry_Object = MibTableRow
mscExampleHexIndicesRowStatusEntry = _MscExampleHexIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1)
)
mscExampleHexIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleHexIndicesRowStatus_Type = RowStatus
_MscExampleHexIndicesRowStatus_Object = MibTableColumn
mscExampleHexIndicesRowStatus = _MscExampleHexIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1, 1),
    _MscExampleHexIndicesRowStatus_Type()
)
mscExampleHexIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexIndicesRowStatus.setStatus("mandatory")
_MscExampleHexIndicesComponentName_Type = DisplayString
_MscExampleHexIndicesComponentName_Object = MibTableColumn
mscExampleHexIndicesComponentName = _MscExampleHexIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1, 2),
    _MscExampleHexIndicesComponentName_Type()
)
mscExampleHexIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleHexIndicesComponentName.setStatus("mandatory")
_MscExampleHexIndicesStorageType_Type = StorageType
_MscExampleHexIndicesStorageType_Object = MibTableColumn
mscExampleHexIndicesStorageType = _MscExampleHexIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1, 4),
    _MscExampleHexIndicesStorageType_Type()
)
mscExampleHexIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleHexIndicesStorageType.setStatus("mandatory")


class _MscExampleHexIndicesOneIndex_Type(Integer32):
    """Custom type mscExampleHexIndicesOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(256, 256),
    )


_MscExampleHexIndicesOneIndex_Type.__name__ = "Integer32"
_MscExampleHexIndicesOneIndex_Object = MibTableColumn
mscExampleHexIndicesOneIndex = _MscExampleHexIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1, 10),
    _MscExampleHexIndicesOneIndex_Type()
)
mscExampleHexIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexIndicesOneIndex.setStatus("mandatory")


class _MscExampleHexIndicesTwoIndex_Type(Integer32):
    """Custom type mscExampleHexIndicesTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(256, 256),
    )


_MscExampleHexIndicesTwoIndex_Type.__name__ = "Integer32"
_MscExampleHexIndicesTwoIndex_Object = MibTableColumn
mscExampleHexIndicesTwoIndex = _MscExampleHexIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1, 11),
    _MscExampleHexIndicesTwoIndex_Type()
)
mscExampleHexIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexIndicesTwoIndex.setStatus("mandatory")


class _MscExampleHexIndicesThreeIndex_Type(Integer32):
    """Custom type mscExampleHexIndicesThreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
        ValueRangeConstraint(256, 256),
    )


_MscExampleHexIndicesThreeIndex_Type.__name__ = "Integer32"
_MscExampleHexIndicesThreeIndex_Object = MibTableColumn
mscExampleHexIndicesThreeIndex = _MscExampleHexIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 1, 1, 12),
    _MscExampleHexIndicesThreeIndex_Type()
)
mscExampleHexIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexIndicesThreeIndex.setStatus("mandatory")
_MscExampleHexIndicesProvisionedTable_Object = MibTable
mscExampleHexIndicesProvisionedTable = _MscExampleHexIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 10)
)
if mibBuilder.loadTexts:
    mscExampleHexIndicesProvisionedTable.setStatus("mandatory")
_MscExampleHexIndicesProvisionedEntry_Object = MibTableRow
mscExampleHexIndicesProvisionedEntry = _MscExampleHexIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 10, 1)
)
mscExampleHexIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleHexIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleHexIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleHexIndicesProvAttribute_Object = MibTableColumn
mscExampleHexIndicesProvAttribute = _MscExampleHexIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 21, 10, 1, 1),
    _MscExampleHexIndicesProvAttribute_Type()
)
mscExampleHexIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexIndicesProvAttribute.setStatus("mandatory")
_MscExampleIpAddrIndices_ObjectIdentity = ObjectIdentity
mscExampleIpAddrIndices = _MscExampleIpAddrIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22)
)
_MscExampleIpAddrIndicesRowStatusTable_Object = MibTable
mscExampleIpAddrIndicesRowStatusTable = _MscExampleIpAddrIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1)
)
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesRowStatusTable.setStatus("mandatory")
_MscExampleIpAddrIndicesRowStatusEntry_Object = MibTableRow
mscExampleIpAddrIndicesRowStatusEntry = _MscExampleIpAddrIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1)
)
mscExampleIpAddrIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddrIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddrIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleIpAddrIndicesRowStatus_Type = RowStatus
_MscExampleIpAddrIndicesRowStatus_Object = MibTableColumn
mscExampleIpAddrIndicesRowStatus = _MscExampleIpAddrIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1, 1),
    _MscExampleIpAddrIndicesRowStatus_Type()
)
mscExampleIpAddrIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesRowStatus.setStatus("mandatory")
_MscExampleIpAddrIndicesComponentName_Type = DisplayString
_MscExampleIpAddrIndicesComponentName_Object = MibTableColumn
mscExampleIpAddrIndicesComponentName = _MscExampleIpAddrIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1, 2),
    _MscExampleIpAddrIndicesComponentName_Type()
)
mscExampleIpAddrIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesComponentName.setStatus("mandatory")
_MscExampleIpAddrIndicesStorageType_Type = StorageType
_MscExampleIpAddrIndicesStorageType_Object = MibTableColumn
mscExampleIpAddrIndicesStorageType = _MscExampleIpAddrIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1, 4),
    _MscExampleIpAddrIndicesStorageType_Type()
)
mscExampleIpAddrIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesStorageType.setStatus("mandatory")
_MscExampleIpAddrIndicesOneIndex_Type = IpAddress
_MscExampleIpAddrIndicesOneIndex_Object = MibTableColumn
mscExampleIpAddrIndicesOneIndex = _MscExampleIpAddrIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1, 10),
    _MscExampleIpAddrIndicesOneIndex_Type()
)
mscExampleIpAddrIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesOneIndex.setStatus("mandatory")
_MscExampleIpAddrIndicesTwoIndex_Type = IpAddress
_MscExampleIpAddrIndicesTwoIndex_Object = MibTableColumn
mscExampleIpAddrIndicesTwoIndex = _MscExampleIpAddrIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1, 11),
    _MscExampleIpAddrIndicesTwoIndex_Type()
)
mscExampleIpAddrIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesTwoIndex.setStatus("mandatory")
_MscExampleIpAddrIndicesThreeIndex_Type = IpAddress
_MscExampleIpAddrIndicesThreeIndex_Object = MibTableColumn
mscExampleIpAddrIndicesThreeIndex = _MscExampleIpAddrIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 1, 1, 12),
    _MscExampleIpAddrIndicesThreeIndex_Type()
)
mscExampleIpAddrIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesThreeIndex.setStatus("mandatory")
_MscExampleIpAddrIndicesProvisionedTable_Object = MibTable
mscExampleIpAddrIndicesProvisionedTable = _MscExampleIpAddrIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 10)
)
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesProvisionedTable.setStatus("mandatory")
_MscExampleIpAddrIndicesProvisionedEntry_Object = MibTableRow
mscExampleIpAddrIndicesProvisionedEntry = _MscExampleIpAddrIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 10, 1)
)
mscExampleIpAddrIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddrIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddrIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIpAddrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleIpAddrIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleIpAddrIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleIpAddrIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleIpAddrIndicesProvAttribute_Object = MibTableColumn
mscExampleIpAddrIndicesProvAttribute = _MscExampleIpAddrIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 22, 10, 1, 1),
    _MscExampleIpAddrIndicesProvAttribute_Type()
)
mscExampleIpAddrIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleIpAddrIndicesProvAttribute.setStatus("mandatory")
_MscExampleAsciiIndices_ObjectIdentity = ObjectIdentity
mscExampleAsciiIndices = _MscExampleAsciiIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23)
)
_MscExampleAsciiIndicesRowStatusTable_Object = MibTable
mscExampleAsciiIndicesRowStatusTable = _MscExampleAsciiIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1)
)
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesRowStatusTable.setStatus("mandatory")
_MscExampleAsciiIndicesRowStatusEntry_Object = MibTableRow
mscExampleAsciiIndicesRowStatusEntry = _MscExampleAsciiIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1)
)
mscExampleAsciiIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleAsciiIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleAsciiIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleAsciiIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleAsciiIndicesRowStatus_Type = RowStatus
_MscExampleAsciiIndicesRowStatus_Object = MibTableColumn
mscExampleAsciiIndicesRowStatus = _MscExampleAsciiIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1, 1),
    _MscExampleAsciiIndicesRowStatus_Type()
)
mscExampleAsciiIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesRowStatus.setStatus("mandatory")
_MscExampleAsciiIndicesComponentName_Type = DisplayString
_MscExampleAsciiIndicesComponentName_Object = MibTableColumn
mscExampleAsciiIndicesComponentName = _MscExampleAsciiIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1, 2),
    _MscExampleAsciiIndicesComponentName_Type()
)
mscExampleAsciiIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesComponentName.setStatus("mandatory")
_MscExampleAsciiIndicesStorageType_Type = StorageType
_MscExampleAsciiIndicesStorageType_Object = MibTableColumn
mscExampleAsciiIndicesStorageType = _MscExampleAsciiIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1, 4),
    _MscExampleAsciiIndicesStorageType_Type()
)
mscExampleAsciiIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesStorageType.setStatus("mandatory")


class _MscExampleAsciiIndicesOneIndex_Type(AsciiStringIndex):
    """Custom type mscExampleAsciiIndicesOneIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleAsciiIndicesOneIndex_Type.__name__ = "AsciiStringIndex"
_MscExampleAsciiIndicesOneIndex_Object = MibTableColumn
mscExampleAsciiIndicesOneIndex = _MscExampleAsciiIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1, 10),
    _MscExampleAsciiIndicesOneIndex_Type()
)
mscExampleAsciiIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesOneIndex.setStatus("mandatory")


class _MscExampleAsciiIndicesTwoIndex_Type(AsciiStringIndex):
    """Custom type mscExampleAsciiIndicesTwoIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleAsciiIndicesTwoIndex_Type.__name__ = "AsciiStringIndex"
_MscExampleAsciiIndicesTwoIndex_Object = MibTableColumn
mscExampleAsciiIndicesTwoIndex = _MscExampleAsciiIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1, 11),
    _MscExampleAsciiIndicesTwoIndex_Type()
)
mscExampleAsciiIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesTwoIndex.setStatus("mandatory")


class _MscExampleAsciiIndicesThreeIndex_Type(AsciiStringIndex):
    """Custom type mscExampleAsciiIndicesThreeIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleAsciiIndicesThreeIndex_Type.__name__ = "AsciiStringIndex"
_MscExampleAsciiIndicesThreeIndex_Object = MibTableColumn
mscExampleAsciiIndicesThreeIndex = _MscExampleAsciiIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 1, 1, 12),
    _MscExampleAsciiIndicesThreeIndex_Type()
)
mscExampleAsciiIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesThreeIndex.setStatus("mandatory")
_MscExampleAsciiIndicesProvisionedTable_Object = MibTable
mscExampleAsciiIndicesProvisionedTable = _MscExampleAsciiIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 10)
)
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesProvisionedTable.setStatus("mandatory")
_MscExampleAsciiIndicesProvisionedEntry_Object = MibTableRow
mscExampleAsciiIndicesProvisionedEntry = _MscExampleAsciiIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 10, 1)
)
mscExampleAsciiIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleAsciiIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleAsciiIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleAsciiIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleAsciiIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleAsciiIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleAsciiIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleAsciiIndicesProvAttribute_Object = MibTableColumn
mscExampleAsciiIndicesProvAttribute = _MscExampleAsciiIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 23, 10, 1, 1),
    _MscExampleAsciiIndicesProvAttribute_Type()
)
mscExampleAsciiIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleAsciiIndicesProvAttribute.setStatus("mandatory")
_MscExampleHexStrIndices_ObjectIdentity = ObjectIdentity
mscExampleHexStrIndices = _MscExampleHexStrIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24)
)
_MscExampleHexStrIndicesRowStatusTable_Object = MibTable
mscExampleHexStrIndicesRowStatusTable = _MscExampleHexStrIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1)
)
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesRowStatusTable.setStatus("mandatory")
_MscExampleHexStrIndicesRowStatusEntry_Object = MibTableRow
mscExampleHexStrIndicesRowStatusEntry = _MscExampleHexStrIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1)
)
mscExampleHexStrIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexStrIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexStrIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexStrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleHexStrIndicesRowStatus_Type = RowStatus
_MscExampleHexStrIndicesRowStatus_Object = MibTableColumn
mscExampleHexStrIndicesRowStatus = _MscExampleHexStrIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1, 1),
    _MscExampleHexStrIndicesRowStatus_Type()
)
mscExampleHexStrIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesRowStatus.setStatus("mandatory")
_MscExampleHexStrIndicesComponentName_Type = DisplayString
_MscExampleHexStrIndicesComponentName_Object = MibTableColumn
mscExampleHexStrIndicesComponentName = _MscExampleHexStrIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1, 2),
    _MscExampleHexStrIndicesComponentName_Type()
)
mscExampleHexStrIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesComponentName.setStatus("mandatory")
_MscExampleHexStrIndicesStorageType_Type = StorageType
_MscExampleHexStrIndicesStorageType_Object = MibTableColumn
mscExampleHexStrIndicesStorageType = _MscExampleHexStrIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1, 4),
    _MscExampleHexStrIndicesStorageType_Type()
)
mscExampleHexStrIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesStorageType.setStatus("mandatory")


class _MscExampleHexStrIndicesOneIndex_Type(HexString):
    """Custom type mscExampleHexStrIndicesOneIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleHexStrIndicesOneIndex_Type.__name__ = "HexString"
_MscExampleHexStrIndicesOneIndex_Object = MibTableColumn
mscExampleHexStrIndicesOneIndex = _MscExampleHexStrIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1, 10),
    _MscExampleHexStrIndicesOneIndex_Type()
)
mscExampleHexStrIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesOneIndex.setStatus("mandatory")


class _MscExampleHexStrIndicesTwoIndex_Type(HexString):
    """Custom type mscExampleHexStrIndicesTwoIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleHexStrIndicesTwoIndex_Type.__name__ = "HexString"
_MscExampleHexStrIndicesTwoIndex_Object = MibTableColumn
mscExampleHexStrIndicesTwoIndex = _MscExampleHexStrIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1, 11),
    _MscExampleHexStrIndicesTwoIndex_Type()
)
mscExampleHexStrIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesTwoIndex.setStatus("mandatory")


class _MscExampleHexStrIndicesThreeIndex_Type(HexString):
    """Custom type mscExampleHexStrIndicesThreeIndex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleHexStrIndicesThreeIndex_Type.__name__ = "HexString"
_MscExampleHexStrIndicesThreeIndex_Object = MibTableColumn
mscExampleHexStrIndicesThreeIndex = _MscExampleHexStrIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 1, 1, 12),
    _MscExampleHexStrIndicesThreeIndex_Type()
)
mscExampleHexStrIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesThreeIndex.setStatus("mandatory")
_MscExampleHexStrIndicesProvisionedTable_Object = MibTable
mscExampleHexStrIndicesProvisionedTable = _MscExampleHexStrIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 10)
)
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesProvisionedTable.setStatus("mandatory")
_MscExampleHexStrIndicesProvisionedEntry_Object = MibTableRow
mscExampleHexStrIndicesProvisionedEntry = _MscExampleHexStrIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 10, 1)
)
mscExampleHexStrIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexStrIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexStrIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleHexStrIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleHexStrIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleHexStrIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleHexStrIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleHexStrIndicesProvAttribute_Object = MibTableColumn
mscExampleHexStrIndicesProvAttribute = _MscExampleHexStrIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 24, 10, 1, 1),
    _MscExampleHexStrIndicesProvAttribute_Type()
)
mscExampleHexStrIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleHexStrIndicesProvAttribute.setStatus("mandatory")
_MscExampleBcdIndices_ObjectIdentity = ObjectIdentity
mscExampleBcdIndices = _MscExampleBcdIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25)
)
_MscExampleBcdIndicesRowStatusTable_Object = MibTable
mscExampleBcdIndicesRowStatusTable = _MscExampleBcdIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1)
)
if mibBuilder.loadTexts:
    mscExampleBcdIndicesRowStatusTable.setStatus("mandatory")
_MscExampleBcdIndicesRowStatusEntry_Object = MibTableRow
mscExampleBcdIndicesRowStatusEntry = _MscExampleBcdIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1)
)
mscExampleBcdIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleBcdIndicesRowStatus_Type = RowStatus
_MscExampleBcdIndicesRowStatus_Object = MibTableColumn
mscExampleBcdIndicesRowStatus = _MscExampleBcdIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1, 1),
    _MscExampleBcdIndicesRowStatus_Type()
)
mscExampleBcdIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesRowStatus.setStatus("mandatory")
_MscExampleBcdIndicesComponentName_Type = DisplayString
_MscExampleBcdIndicesComponentName_Object = MibTableColumn
mscExampleBcdIndicesComponentName = _MscExampleBcdIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1, 2),
    _MscExampleBcdIndicesComponentName_Type()
)
mscExampleBcdIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesComponentName.setStatus("mandatory")
_MscExampleBcdIndicesStorageType_Type = StorageType
_MscExampleBcdIndicesStorageType_Object = MibTableColumn
mscExampleBcdIndicesStorageType = _MscExampleBcdIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1, 4),
    _MscExampleBcdIndicesStorageType_Type()
)
mscExampleBcdIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesStorageType.setStatus("mandatory")


class _MscExampleBcdIndicesOneIndex_Type(DigitString):
    """Custom type mscExampleBcdIndicesOneIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleBcdIndicesOneIndex_Type.__name__ = "DigitString"
_MscExampleBcdIndicesOneIndex_Object = MibTableColumn
mscExampleBcdIndicesOneIndex = _MscExampleBcdIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1, 10),
    _MscExampleBcdIndicesOneIndex_Type()
)
mscExampleBcdIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesOneIndex.setStatus("mandatory")


class _MscExampleBcdIndicesTwoIndex_Type(DigitString):
    """Custom type mscExampleBcdIndicesTwoIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleBcdIndicesTwoIndex_Type.__name__ = "DigitString"
_MscExampleBcdIndicesTwoIndex_Object = MibTableColumn
mscExampleBcdIndicesTwoIndex = _MscExampleBcdIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1, 11),
    _MscExampleBcdIndicesTwoIndex_Type()
)
mscExampleBcdIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesTwoIndex.setStatus("mandatory")


class _MscExampleBcdIndicesThreeIndex_Type(DigitString):
    """Custom type mscExampleBcdIndicesThreeIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleBcdIndicesThreeIndex_Type.__name__ = "DigitString"
_MscExampleBcdIndicesThreeIndex_Object = MibTableColumn
mscExampleBcdIndicesThreeIndex = _MscExampleBcdIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 1, 1, 12),
    _MscExampleBcdIndicesThreeIndex_Type()
)
mscExampleBcdIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesThreeIndex.setStatus("mandatory")
_MscExampleBcdIndicesProvisionedTable_Object = MibTable
mscExampleBcdIndicesProvisionedTable = _MscExampleBcdIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 10)
)
if mibBuilder.loadTexts:
    mscExampleBcdIndicesProvisionedTable.setStatus("mandatory")
_MscExampleBcdIndicesProvisionedEntry_Object = MibTableRow
mscExampleBcdIndicesProvisionedEntry = _MscExampleBcdIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 10, 1)
)
mscExampleBcdIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleBcdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleBcdIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleBcdIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleBcdIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleBcdIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleBcdIndicesProvAttribute_Object = MibTableColumn
mscExampleBcdIndicesProvAttribute = _MscExampleBcdIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 25, 10, 1, 1),
    _MscExampleBcdIndicesProvAttribute_Type()
)
mscExampleBcdIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleBcdIndicesProvAttribute.setStatus("mandatory")
_MscExampleEnumIndices_ObjectIdentity = ObjectIdentity
mscExampleEnumIndices = _MscExampleEnumIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26)
)
_MscExampleEnumIndicesRowStatusTable_Object = MibTable
mscExampleEnumIndicesRowStatusTable = _MscExampleEnumIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1)
)
if mibBuilder.loadTexts:
    mscExampleEnumIndicesRowStatusTable.setStatus("mandatory")
_MscExampleEnumIndicesRowStatusEntry_Object = MibTableRow
mscExampleEnumIndicesRowStatusEntry = _MscExampleEnumIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1)
)
mscExampleEnumIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleEnumIndicesRowStatus_Type = RowStatus
_MscExampleEnumIndicesRowStatus_Object = MibTableColumn
mscExampleEnumIndicesRowStatus = _MscExampleEnumIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1, 1),
    _MscExampleEnumIndicesRowStatus_Type()
)
mscExampleEnumIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesRowStatus.setStatus("mandatory")
_MscExampleEnumIndicesComponentName_Type = DisplayString
_MscExampleEnumIndicesComponentName_Object = MibTableColumn
mscExampleEnumIndicesComponentName = _MscExampleEnumIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1, 2),
    _MscExampleEnumIndicesComponentName_Type()
)
mscExampleEnumIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesComponentName.setStatus("mandatory")
_MscExampleEnumIndicesStorageType_Type = StorageType
_MscExampleEnumIndicesStorageType_Object = MibTableColumn
mscExampleEnumIndicesStorageType = _MscExampleEnumIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1, 4),
    _MscExampleEnumIndicesStorageType_Type()
)
mscExampleEnumIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesStorageType.setStatus("mandatory")


class _MscExampleEnumIndicesOneIndex_Type(Integer32):
    """Custom type mscExampleEnumIndicesOneIndex based on Integer32"""
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


_MscExampleEnumIndicesOneIndex_Type.__name__ = "Integer32"
_MscExampleEnumIndicesOneIndex_Object = MibTableColumn
mscExampleEnumIndicesOneIndex = _MscExampleEnumIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1, 10),
    _MscExampleEnumIndicesOneIndex_Type()
)
mscExampleEnumIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesOneIndex.setStatus("mandatory")


class _MscExampleEnumIndicesTwoIndex_Type(Integer32):
    """Custom type mscExampleEnumIndicesTwoIndex based on Integer32"""
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


_MscExampleEnumIndicesTwoIndex_Type.__name__ = "Integer32"
_MscExampleEnumIndicesTwoIndex_Object = MibTableColumn
mscExampleEnumIndicesTwoIndex = _MscExampleEnumIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1, 11),
    _MscExampleEnumIndicesTwoIndex_Type()
)
mscExampleEnumIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesTwoIndex.setStatus("mandatory")


class _MscExampleEnumIndicesThreeIndex_Type(Integer32):
    """Custom type mscExampleEnumIndicesThreeIndex based on Integer32"""
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


_MscExampleEnumIndicesThreeIndex_Type.__name__ = "Integer32"
_MscExampleEnumIndicesThreeIndex_Object = MibTableColumn
mscExampleEnumIndicesThreeIndex = _MscExampleEnumIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 1, 1, 12),
    _MscExampleEnumIndicesThreeIndex_Type()
)
mscExampleEnumIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesThreeIndex.setStatus("mandatory")
_MscExampleEnumIndicesProvisionedTable_Object = MibTable
mscExampleEnumIndicesProvisionedTable = _MscExampleEnumIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 10)
)
if mibBuilder.loadTexts:
    mscExampleEnumIndicesProvisionedTable.setStatus("mandatory")
_MscExampleEnumIndicesProvisionedEntry_Object = MibTableRow
mscExampleEnumIndicesProvisionedEntry = _MscExampleEnumIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 10, 1)
)
mscExampleEnumIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleEnumIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleEnumIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleEnumIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleEnumIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleEnumIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleEnumIndicesProvAttribute_Object = MibTableColumn
mscExampleEnumIndicesProvAttribute = _MscExampleEnumIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 26, 10, 1, 1),
    _MscExampleEnumIndicesProvAttribute_Type()
)
mscExampleEnumIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleEnumIndicesProvAttribute.setStatus("mandatory")
_MscExampleSequenceIndices_ObjectIdentity = ObjectIdentity
mscExampleSequenceIndices = _MscExampleSequenceIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27)
)
_MscExampleSequenceIndicesRowStatusTable_Object = MibTable
mscExampleSequenceIndicesRowStatusTable = _MscExampleSequenceIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1)
)
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesRowStatusTable.setStatus("mandatory")
_MscExampleSequenceIndicesRowStatusEntry_Object = MibTableRow
mscExampleSequenceIndicesRowStatusEntry = _MscExampleSequenceIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1)
)
mscExampleSequenceIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleSequenceIndicesRowStatus_Type = RowStatus
_MscExampleSequenceIndicesRowStatus_Object = MibTableColumn
mscExampleSequenceIndicesRowStatus = _MscExampleSequenceIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1, 1),
    _MscExampleSequenceIndicesRowStatus_Type()
)
mscExampleSequenceIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesRowStatus.setStatus("mandatory")
_MscExampleSequenceIndicesComponentName_Type = DisplayString
_MscExampleSequenceIndicesComponentName_Object = MibTableColumn
mscExampleSequenceIndicesComponentName = _MscExampleSequenceIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1, 2),
    _MscExampleSequenceIndicesComponentName_Type()
)
mscExampleSequenceIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesComponentName.setStatus("mandatory")
_MscExampleSequenceIndicesStorageType_Type = StorageType
_MscExampleSequenceIndicesStorageType_Object = MibTableColumn
mscExampleSequenceIndicesStorageType = _MscExampleSequenceIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1, 4),
    _MscExampleSequenceIndicesStorageType_Type()
)
mscExampleSequenceIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesStorageType.setStatus("mandatory")
_MscExampleSequenceIndicesOneIndex_Type = ObjectIdentifier
_MscExampleSequenceIndicesOneIndex_Object = MibTableColumn
mscExampleSequenceIndicesOneIndex = _MscExampleSequenceIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1, 10),
    _MscExampleSequenceIndicesOneIndex_Type()
)
mscExampleSequenceIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesOneIndex.setStatus("mandatory")
_MscExampleSequenceIndicesTwoIndex_Type = ObjectIdentifier
_MscExampleSequenceIndicesTwoIndex_Object = MibTableColumn
mscExampleSequenceIndicesTwoIndex = _MscExampleSequenceIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1, 11),
    _MscExampleSequenceIndicesTwoIndex_Type()
)
mscExampleSequenceIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesTwoIndex.setStatus("mandatory")
_MscExampleSequenceIndicesThreeIndex_Type = ObjectIdentifier
_MscExampleSequenceIndicesThreeIndex_Object = MibTableColumn
mscExampleSequenceIndicesThreeIndex = _MscExampleSequenceIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 1, 1, 12),
    _MscExampleSequenceIndicesThreeIndex_Type()
)
mscExampleSequenceIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesThreeIndex.setStatus("mandatory")
_MscExampleSequenceIndicesProvisionedTable_Object = MibTable
mscExampleSequenceIndicesProvisionedTable = _MscExampleSequenceIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 10)
)
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesProvisionedTable.setStatus("mandatory")
_MscExampleSequenceIndicesProvisionedEntry_Object = MibTableRow
mscExampleSequenceIndicesProvisionedEntry = _MscExampleSequenceIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 10, 1)
)
mscExampleSequenceIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleSequenceIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleSequenceIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleSequenceIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleSequenceIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleSequenceIndicesProvAttribute_Object = MibTableColumn
mscExampleSequenceIndicesProvAttribute = _MscExampleSequenceIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 27, 10, 1, 1),
    _MscExampleSequenceIndicesProvAttribute_Type()
)
mscExampleSequenceIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleSequenceIndicesProvAttribute.setStatus("mandatory")
_MscExampleObjIdIndices_ObjectIdentity = ObjectIdentity
mscExampleObjIdIndices = _MscExampleObjIdIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28)
)
_MscExampleObjIdIndicesRowStatusTable_Object = MibTable
mscExampleObjIdIndicesRowStatusTable = _MscExampleObjIdIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1)
)
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesRowStatusTable.setStatus("mandatory")
_MscExampleObjIdIndicesRowStatusEntry_Object = MibTableRow
mscExampleObjIdIndicesRowStatusEntry = _MscExampleObjIdIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1)
)
mscExampleObjIdIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjIdIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjIdIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjIdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleObjIdIndicesRowStatus_Type = RowStatus
_MscExampleObjIdIndicesRowStatus_Object = MibTableColumn
mscExampleObjIdIndicesRowStatus = _MscExampleObjIdIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1, 1),
    _MscExampleObjIdIndicesRowStatus_Type()
)
mscExampleObjIdIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesRowStatus.setStatus("mandatory")
_MscExampleObjIdIndicesComponentName_Type = DisplayString
_MscExampleObjIdIndicesComponentName_Object = MibTableColumn
mscExampleObjIdIndicesComponentName = _MscExampleObjIdIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1, 2),
    _MscExampleObjIdIndicesComponentName_Type()
)
mscExampleObjIdIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesComponentName.setStatus("mandatory")
_MscExampleObjIdIndicesStorageType_Type = StorageType
_MscExampleObjIdIndicesStorageType_Object = MibTableColumn
mscExampleObjIdIndicesStorageType = _MscExampleObjIdIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1, 4),
    _MscExampleObjIdIndicesStorageType_Type()
)
mscExampleObjIdIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesStorageType.setStatus("mandatory")
_MscExampleObjIdIndicesOneIndex_Type = ObjectIdentifier
_MscExampleObjIdIndicesOneIndex_Object = MibTableColumn
mscExampleObjIdIndicesOneIndex = _MscExampleObjIdIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1, 10),
    _MscExampleObjIdIndicesOneIndex_Type()
)
mscExampleObjIdIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesOneIndex.setStatus("mandatory")
_MscExampleObjIdIndicesTwoIndex_Type = ObjectIdentifier
_MscExampleObjIdIndicesTwoIndex_Object = MibTableColumn
mscExampleObjIdIndicesTwoIndex = _MscExampleObjIdIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1, 11),
    _MscExampleObjIdIndicesTwoIndex_Type()
)
mscExampleObjIdIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesTwoIndex.setStatus("mandatory")
_MscExampleObjIdIndicesThreeIndex_Type = ObjectIdentifier
_MscExampleObjIdIndicesThreeIndex_Object = MibTableColumn
mscExampleObjIdIndicesThreeIndex = _MscExampleObjIdIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 1, 1, 12),
    _MscExampleObjIdIndicesThreeIndex_Type()
)
mscExampleObjIdIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesThreeIndex.setStatus("mandatory")
_MscExampleObjIdIndicesProvisionedTable_Object = MibTable
mscExampleObjIdIndicesProvisionedTable = _MscExampleObjIdIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 10)
)
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesProvisionedTable.setStatus("mandatory")
_MscExampleObjIdIndicesProvisionedEntry_Object = MibTableRow
mscExampleObjIdIndicesProvisionedEntry = _MscExampleObjIdIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 10, 1)
)
mscExampleObjIdIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjIdIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjIdIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleObjIdIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleObjIdIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleObjIdIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleObjIdIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleObjIdIndicesProvAttribute_Object = MibTableColumn
mscExampleObjIdIndicesProvAttribute = _MscExampleObjIdIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 28, 10, 1, 1),
    _MscExampleObjIdIndicesProvAttribute_Type()
)
mscExampleObjIdIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleObjIdIndicesProvAttribute.setStatus("mandatory")
_MscExampleDashedIndices_ObjectIdentity = ObjectIdentity
mscExampleDashedIndices = _MscExampleDashedIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30)
)
_MscExampleDashedIndicesRowStatusTable_Object = MibTable
mscExampleDashedIndicesRowStatusTable = _MscExampleDashedIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1)
)
if mibBuilder.loadTexts:
    mscExampleDashedIndicesRowStatusTable.setStatus("mandatory")
_MscExampleDashedIndicesRowStatusEntry_Object = MibTableRow
mscExampleDashedIndicesRowStatusEntry = _MscExampleDashedIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1)
)
mscExampleDashedIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleDashedIndicesRowStatus_Type = RowStatus
_MscExampleDashedIndicesRowStatus_Object = MibTableColumn
mscExampleDashedIndicesRowStatus = _MscExampleDashedIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1, 1),
    _MscExampleDashedIndicesRowStatus_Type()
)
mscExampleDashedIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesRowStatus.setStatus("mandatory")
_MscExampleDashedIndicesComponentName_Type = DisplayString
_MscExampleDashedIndicesComponentName_Object = MibTableColumn
mscExampleDashedIndicesComponentName = _MscExampleDashedIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1, 2),
    _MscExampleDashedIndicesComponentName_Type()
)
mscExampleDashedIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesComponentName.setStatus("mandatory")
_MscExampleDashedIndicesStorageType_Type = StorageType
_MscExampleDashedIndicesStorageType_Object = MibTableColumn
mscExampleDashedIndicesStorageType = _MscExampleDashedIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1, 4),
    _MscExampleDashedIndicesStorageType_Type()
)
mscExampleDashedIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesStorageType.setStatus("mandatory")


class _MscExampleDashedIndicesOneIndex_Type(DashedHexString):
    """Custom type mscExampleDashedIndicesOneIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedIndicesOneIndex_Type.__name__ = "DashedHexString"
_MscExampleDashedIndicesOneIndex_Object = MibTableColumn
mscExampleDashedIndicesOneIndex = _MscExampleDashedIndicesOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1, 10),
    _MscExampleDashedIndicesOneIndex_Type()
)
mscExampleDashedIndicesOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesOneIndex.setStatus("mandatory")


class _MscExampleDashedIndicesTwoIndex_Type(DashedHexString):
    """Custom type mscExampleDashedIndicesTwoIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedIndicesTwoIndex_Type.__name__ = "DashedHexString"
_MscExampleDashedIndicesTwoIndex_Object = MibTableColumn
mscExampleDashedIndicesTwoIndex = _MscExampleDashedIndicesTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1, 11),
    _MscExampleDashedIndicesTwoIndex_Type()
)
mscExampleDashedIndicesTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesTwoIndex.setStatus("mandatory")


class _MscExampleDashedIndicesThreeIndex_Type(DashedHexString):
    """Custom type mscExampleDashedIndicesThreeIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscExampleDashedIndicesThreeIndex_Type.__name__ = "DashedHexString"
_MscExampleDashedIndicesThreeIndex_Object = MibTableColumn
mscExampleDashedIndicesThreeIndex = _MscExampleDashedIndicesThreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 1, 1, 12),
    _MscExampleDashedIndicesThreeIndex_Type()
)
mscExampleDashedIndicesThreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesThreeIndex.setStatus("mandatory")
_MscExampleDashedIndicesProvisionedTable_Object = MibTable
mscExampleDashedIndicesProvisionedTable = _MscExampleDashedIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 10)
)
if mibBuilder.loadTexts:
    mscExampleDashedIndicesProvisionedTable.setStatus("mandatory")
_MscExampleDashedIndicesProvisionedEntry_Object = MibTableRow
mscExampleDashedIndicesProvisionedEntry = _MscExampleDashedIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 10, 1)
)
mscExampleDashedIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndicesOneIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndicesTwoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleDashedIndicesThreeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleDashedIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleDashedIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleDashedIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleDashedIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleDashedIndicesProvAttribute_Object = MibTableColumn
mscExampleDashedIndicesProvAttribute = _MscExampleDashedIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 30, 10, 1, 1),
    _MscExampleDashedIndicesProvAttribute_Type()
)
mscExampleDashedIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleDashedIndicesProvAttribute.setStatus("mandatory")
_MscExampleRequiredIndices_ObjectIdentity = ObjectIdentity
mscExampleRequiredIndices = _MscExampleRequiredIndices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31)
)
_MscExampleRequiredIndicesRowStatusTable_Object = MibTable
mscExampleRequiredIndicesRowStatusTable = _MscExampleRequiredIndicesRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1)
)
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesRowStatusTable.setStatus("mandatory")
_MscExampleRequiredIndicesRowStatusEntry_Object = MibTableRow
mscExampleRequiredIndicesRowStatusEntry = _MscExampleRequiredIndicesRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1, 1)
)
mscExampleRequiredIndicesRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleRequiredIndicesDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleRequiredIndicesEnumerationIndex"),
)
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesRowStatusEntry.setStatus("mandatory")
_MscExampleRequiredIndicesRowStatus_Type = RowStatus
_MscExampleRequiredIndicesRowStatus_Object = MibTableColumn
mscExampleRequiredIndicesRowStatus = _MscExampleRequiredIndicesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1, 1, 1),
    _MscExampleRequiredIndicesRowStatus_Type()
)
mscExampleRequiredIndicesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesRowStatus.setStatus("mandatory")
_MscExampleRequiredIndicesComponentName_Type = DisplayString
_MscExampleRequiredIndicesComponentName_Object = MibTableColumn
mscExampleRequiredIndicesComponentName = _MscExampleRequiredIndicesComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1, 1, 2),
    _MscExampleRequiredIndicesComponentName_Type()
)
mscExampleRequiredIndicesComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesComponentName.setStatus("mandatory")
_MscExampleRequiredIndicesStorageType_Type = StorageType
_MscExampleRequiredIndicesStorageType_Object = MibTableColumn
mscExampleRequiredIndicesStorageType = _MscExampleRequiredIndicesStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1, 1, 4),
    _MscExampleRequiredIndicesStorageType_Type()
)
mscExampleRequiredIndicesStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesStorageType.setStatus("mandatory")


class _MscExampleRequiredIndicesDecimalIndex_Type(Integer32):
    """Custom type mscExampleRequiredIndicesDecimalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscExampleRequiredIndicesDecimalIndex_Type.__name__ = "Integer32"
_MscExampleRequiredIndicesDecimalIndex_Object = MibTableColumn
mscExampleRequiredIndicesDecimalIndex = _MscExampleRequiredIndicesDecimalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1, 1, 10),
    _MscExampleRequiredIndicesDecimalIndex_Type()
)
mscExampleRequiredIndicesDecimalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesDecimalIndex.setStatus("mandatory")


class _MscExampleRequiredIndicesEnumerationIndex_Type(Integer32):
    """Custom type mscExampleRequiredIndicesEnumerationIndex based on Integer32"""
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


_MscExampleRequiredIndicesEnumerationIndex_Type.__name__ = "Integer32"
_MscExampleRequiredIndicesEnumerationIndex_Object = MibTableColumn
mscExampleRequiredIndicesEnumerationIndex = _MscExampleRequiredIndicesEnumerationIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 1, 1, 11),
    _MscExampleRequiredIndicesEnumerationIndex_Type()
)
mscExampleRequiredIndicesEnumerationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesEnumerationIndex.setStatus("mandatory")
_MscExampleRequiredIndicesProvisionedTable_Object = MibTable
mscExampleRequiredIndicesProvisionedTable = _MscExampleRequiredIndicesProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 10)
)
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesProvisionedTable.setStatus("mandatory")
_MscExampleRequiredIndicesProvisionedEntry_Object = MibTableRow
mscExampleRequiredIndicesProvisionedEntry = _MscExampleRequiredIndicesProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 10, 1)
)
mscExampleRequiredIndicesProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleRequiredIndicesDecimalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleRequiredIndicesEnumerationIndex"),
)
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesProvisionedEntry.setStatus("mandatory")


class _MscExampleRequiredIndicesProvAttribute_Type(Unsigned32):
    """Custom type mscExampleRequiredIndicesProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscExampleRequiredIndicesProvAttribute_Type.__name__ = "Unsigned32"
_MscExampleRequiredIndicesProvAttribute_Object = MibTableColumn
mscExampleRequiredIndicesProvAttribute = _MscExampleRequiredIndicesProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 31, 10, 1, 1),
    _MscExampleRequiredIndicesProvAttribute_Type()
)
mscExampleRequiredIndicesProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleRequiredIndicesProvAttribute.setStatus("mandatory")
_MscExampleNsap_ObjectIdentity = ObjectIdentity
mscExampleNsap = _MscExampleNsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32)
)
_MscExampleNsapRowStatusTable_Object = MibTable
mscExampleNsapRowStatusTable = _MscExampleNsapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1)
)
if mibBuilder.loadTexts:
    mscExampleNsapRowStatusTable.setStatus("mandatory")
_MscExampleNsapRowStatusEntry_Object = MibTableRow
mscExampleNsapRowStatusEntry = _MscExampleNsapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1, 1)
)
mscExampleNsapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleNsapIndex"),
)
if mibBuilder.loadTexts:
    mscExampleNsapRowStatusEntry.setStatus("mandatory")
_MscExampleNsapRowStatus_Type = RowStatus
_MscExampleNsapRowStatus_Object = MibTableColumn
mscExampleNsapRowStatus = _MscExampleNsapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1, 1, 1),
    _MscExampleNsapRowStatus_Type()
)
mscExampleNsapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleNsapRowStatus.setStatus("mandatory")
_MscExampleNsapComponentName_Type = DisplayString
_MscExampleNsapComponentName_Object = MibTableColumn
mscExampleNsapComponentName = _MscExampleNsapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1, 1, 2),
    _MscExampleNsapComponentName_Type()
)
mscExampleNsapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleNsapComponentName.setStatus("mandatory")
_MscExampleNsapStorageType_Type = StorageType
_MscExampleNsapStorageType_Object = MibTableColumn
mscExampleNsapStorageType = _MscExampleNsapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1, 1, 4),
    _MscExampleNsapStorageType_Type()
)
mscExampleNsapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscExampleNsapStorageType.setStatus("mandatory")


class _MscExampleNsapIndex_Type(AsciiStringIndex):
    """Custom type mscExampleNsapIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_MscExampleNsapIndex_Type.__name__ = "AsciiStringIndex"
_MscExampleNsapIndex_Object = MibTableColumn
mscExampleNsapIndex = _MscExampleNsapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1, 1, 10),
    _MscExampleNsapIndex_Type()
)
mscExampleNsapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleNsapIndex.setStatus("mandatory")
_MscExampleNsapAtmAddrTable_Object = MibTable
mscExampleNsapAtmAddrTable = _MscExampleNsapAtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 102)
)
if mibBuilder.loadTexts:
    mscExampleNsapAtmAddrTable.setStatus("mandatory")
_MscExampleNsapAtmAddrEntry_Object = MibTableRow
mscExampleNsapAtmAddrEntry = _MscExampleNsapAtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 102, 1)
)
mscExampleNsapAtmAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleNsapIndex"),
)
if mibBuilder.loadTexts:
    mscExampleNsapAtmAddrEntry.setStatus("mandatory")


class _MscExampleNsapNsapNativeAddress_Type(AsciiString):
    """Custom type mscExampleNsapNsapNativeAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_MscExampleNsapNsapNativeAddress_Type.__name__ = "AsciiString"
_MscExampleNsapNsapNativeAddress_Object = MibTableColumn
mscExampleNsapNsapNativeAddress = _MscExampleNsapNsapNativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 102, 1, 1246),
    _MscExampleNsapNsapNativeAddress_Type()
)
mscExampleNsapNsapNativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleNsapNsapNativeAddress.setStatus("mandatory")
_MscExampleNsapNativeTable_Object = MibTable
mscExampleNsapNativeTable = _MscExampleNsapNativeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1247)
)
if mibBuilder.loadTexts:
    mscExampleNsapNativeTable.setStatus("mandatory")
_MscExampleNsapNativeEntry_Object = MibTableRow
mscExampleNsapNativeEntry = _MscExampleNsapNativeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1247, 1)
)
mscExampleNsapNativeEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleNsapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleNsapNativeIndex"),
)
if mibBuilder.loadTexts:
    mscExampleNsapNativeEntry.setStatus("mandatory")


class _MscExampleNsapNativeIndex_Type(Integer32):
    """Custom type mscExampleNsapNativeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscExampleNsapNativeIndex_Type.__name__ = "Integer32"
_MscExampleNsapNativeIndex_Object = MibTableColumn
mscExampleNsapNativeIndex = _MscExampleNsapNativeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1247, 1, 1),
    _MscExampleNsapNativeIndex_Type()
)
mscExampleNsapNativeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscExampleNsapNativeIndex.setStatus("mandatory")


class _MscExampleNsapNativeValue_Type(AsciiString):
    """Custom type mscExampleNsapNativeValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_MscExampleNsapNativeValue_Type.__name__ = "AsciiString"
_MscExampleNsapNativeValue_Object = MibTableColumn
mscExampleNsapNativeValue = _MscExampleNsapNativeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 32, 1247, 1, 2),
    _MscExampleNsapNativeValue_Type()
)
mscExampleNsapNativeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleNsapNativeValue.setStatus("mandatory")
_MscExampleOperationalTable_Object = MibTable
mscExampleOperationalTable = _MscExampleOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 100)
)
if mibBuilder.loadTexts:
    mscExampleOperationalTable.setStatus("mandatory")
_MscExampleOperationalEntry_Object = MibTableRow
mscExampleOperationalEntry = _MscExampleOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 100, 1)
)
mscExampleOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
)
if mibBuilder.loadTexts:
    mscExampleOperationalEntry.setStatus("mandatory")
_MscExampleOperMyComponentName_Type = RowPointer
_MscExampleOperMyComponentName_Object = MibTableColumn
mscExampleOperMyComponentName = _MscExampleOperMyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 100, 1, 1),
    _MscExampleOperMyComponentName_Type()
)
mscExampleOperMyComponentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOperMyComponentName.setStatus("mandatory")
_MscExampleProvisionalTable_Object = MibTable
mscExampleProvisionalTable = _MscExampleProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 101)
)
if mibBuilder.loadTexts:
    mscExampleProvisionalTable.setStatus("mandatory")
_MscExampleProvisionalEntry_Object = MibTableRow
mscExampleProvisionalEntry = _MscExampleProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 101, 1)
)
mscExampleProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
)
if mibBuilder.loadTexts:
    mscExampleProvisionalEntry.setStatus("mandatory")
_MscExampleProvMyComponentName_Type = RowPointer
_MscExampleProvMyComponentName_Object = MibTableColumn
mscExampleProvMyComponentName = _MscExampleProvMyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 101, 1, 1),
    _MscExampleProvMyComponentName_Type()
)
mscExampleProvMyComponentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleProvMyComponentName.setStatus("mandatory")
_MscExampleOperDecimalSubCreatedTable_Object = MibTable
mscExampleOperDecimalSubCreatedTable = _MscExampleOperDecimalSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1002)
)
if mibBuilder.loadTexts:
    mscExampleOperDecimalSubCreatedTable.setStatus("mandatory")
_MscExampleOperDecimalSubCreatedEntry_Object = MibTableRow
mscExampleOperDecimalSubCreatedEntry = _MscExampleOperDecimalSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1002, 1)
)
mscExampleOperDecimalSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOperDecimalSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleOperDecimalSubCreatedEntry.setStatus("mandatory")
_MscExampleOperDecimalSubCreatedValue_Type = RowPointer
_MscExampleOperDecimalSubCreatedValue_Object = MibTableColumn
mscExampleOperDecimalSubCreatedValue = _MscExampleOperDecimalSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1002, 1, 1),
    _MscExampleOperDecimalSubCreatedValue_Type()
)
mscExampleOperDecimalSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOperDecimalSubCreatedValue.setStatus("mandatory")
_MscExampleOperDecimalSubCreatedRowStatus_Type = RowStatus
_MscExampleOperDecimalSubCreatedRowStatus_Object = MibTableColumn
mscExampleOperDecimalSubCreatedRowStatus = _MscExampleOperDecimalSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1002, 1, 2),
    _MscExampleOperDecimalSubCreatedRowStatus_Type()
)
mscExampleOperDecimalSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleOperDecimalSubCreatedRowStatus.setStatus("mandatory")
_MscExampleOperFixedPtSubcomponentsCreatedTable_Object = MibTable
mscExampleOperFixedPtSubcomponentsCreatedTable = _MscExampleOperFixedPtSubcomponentsCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1003)
)
if mibBuilder.loadTexts:
    mscExampleOperFixedPtSubcomponentsCreatedTable.setStatus("mandatory")
_MscExampleOperFixedPtSubcomponentsCreatedEntry_Object = MibTableRow
mscExampleOperFixedPtSubcomponentsCreatedEntry = _MscExampleOperFixedPtSubcomponentsCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1003, 1)
)
mscExampleOperFixedPtSubcomponentsCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOperFixedPtSubcomponentsCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleOperFixedPtSubcomponentsCreatedEntry.setStatus("mandatory")
_MscExampleOperFixedPtSubcomponentsCreatedValue_Type = RowPointer
_MscExampleOperFixedPtSubcomponentsCreatedValue_Object = MibTableColumn
mscExampleOperFixedPtSubcomponentsCreatedValue = _MscExampleOperFixedPtSubcomponentsCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1003, 1, 1),
    _MscExampleOperFixedPtSubcomponentsCreatedValue_Type()
)
mscExampleOperFixedPtSubcomponentsCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOperFixedPtSubcomponentsCreatedValue.setStatus("mandatory")
_MscExampleOperFixedPtSubcomponentsCreatedRowStatus_Type = RowStatus
_MscExampleOperFixedPtSubcomponentsCreatedRowStatus_Object = MibTableColumn
mscExampleOperFixedPtSubcomponentsCreatedRowStatus = _MscExampleOperFixedPtSubcomponentsCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1003, 1, 2),
    _MscExampleOperFixedPtSubcomponentsCreatedRowStatus_Type()
)
mscExampleOperFixedPtSubcomponentsCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleOperFixedPtSubcomponentsCreatedRowStatus.setStatus("mandatory")
_MscExampleOperStringSubCreatedTable_Object = MibTable
mscExampleOperStringSubCreatedTable = _MscExampleOperStringSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1004)
)
if mibBuilder.loadTexts:
    mscExampleOperStringSubCreatedTable.setStatus("mandatory")
_MscExampleOperStringSubCreatedEntry_Object = MibTableRow
mscExampleOperStringSubCreatedEntry = _MscExampleOperStringSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1004, 1)
)
mscExampleOperStringSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOperStringSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleOperStringSubCreatedEntry.setStatus("mandatory")
_MscExampleOperStringSubCreatedValue_Type = RowPointer
_MscExampleOperStringSubCreatedValue_Object = MibTableColumn
mscExampleOperStringSubCreatedValue = _MscExampleOperStringSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1004, 1, 1),
    _MscExampleOperStringSubCreatedValue_Type()
)
mscExampleOperStringSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOperStringSubCreatedValue.setStatus("mandatory")
_MscExampleOperStringSubCreatedRowStatus_Type = RowStatus
_MscExampleOperStringSubCreatedRowStatus_Object = MibTableColumn
mscExampleOperStringSubCreatedRowStatus = _MscExampleOperStringSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1004, 1, 2),
    _MscExampleOperStringSubCreatedRowStatus_Type()
)
mscExampleOperStringSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleOperStringSubCreatedRowStatus.setStatus("mandatory")
_MscExampleOperEnumSubCreatedTable_Object = MibTable
mscExampleOperEnumSubCreatedTable = _MscExampleOperEnumSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1005)
)
if mibBuilder.loadTexts:
    mscExampleOperEnumSubCreatedTable.setStatus("mandatory")
_MscExampleOperEnumSubCreatedEntry_Object = MibTableRow
mscExampleOperEnumSubCreatedEntry = _MscExampleOperEnumSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1005, 1)
)
mscExampleOperEnumSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOperEnumSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleOperEnumSubCreatedEntry.setStatus("mandatory")
_MscExampleOperEnumSubCreatedValue_Type = RowPointer
_MscExampleOperEnumSubCreatedValue_Object = MibTableColumn
mscExampleOperEnumSubCreatedValue = _MscExampleOperEnumSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1005, 1, 1),
    _MscExampleOperEnumSubCreatedValue_Type()
)
mscExampleOperEnumSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOperEnumSubCreatedValue.setStatus("mandatory")
_MscExampleOperEnumSubCreatedRowStatus_Type = RowStatus
_MscExampleOperEnumSubCreatedRowStatus_Object = MibTableColumn
mscExampleOperEnumSubCreatedRowStatus = _MscExampleOperEnumSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1005, 1, 2),
    _MscExampleOperEnumSubCreatedRowStatus_Type()
)
mscExampleOperEnumSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleOperEnumSubCreatedRowStatus.setStatus("mandatory")
_MscExampleOperSignedSubCreatedTable_Object = MibTable
mscExampleOperSignedSubCreatedTable = _MscExampleOperSignedSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1006)
)
if mibBuilder.loadTexts:
    mscExampleOperSignedSubCreatedTable.setStatus("mandatory")
_MscExampleOperSignedSubCreatedEntry_Object = MibTableRow
mscExampleOperSignedSubCreatedEntry = _MscExampleOperSignedSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1006, 1)
)
mscExampleOperSignedSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleOperSignedSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleOperSignedSubCreatedEntry.setStatus("mandatory")
_MscExampleOperSignedSubCreatedValue_Type = RowPointer
_MscExampleOperSignedSubCreatedValue_Object = MibTableColumn
mscExampleOperSignedSubCreatedValue = _MscExampleOperSignedSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1006, 1, 1),
    _MscExampleOperSignedSubCreatedValue_Type()
)
mscExampleOperSignedSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleOperSignedSubCreatedValue.setStatus("mandatory")
_MscExampleOperSignedSubCreatedRowStatus_Type = RowStatus
_MscExampleOperSignedSubCreatedRowStatus_Object = MibTableColumn
mscExampleOperSignedSubCreatedRowStatus = _MscExampleOperSignedSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1006, 1, 2),
    _MscExampleOperSignedSubCreatedRowStatus_Type()
)
mscExampleOperSignedSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleOperSignedSubCreatedRowStatus.setStatus("mandatory")
_MscExampleProvDecimalSubCreatedTable_Object = MibTable
mscExampleProvDecimalSubCreatedTable = _MscExampleProvDecimalSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1007)
)
if mibBuilder.loadTexts:
    mscExampleProvDecimalSubCreatedTable.setStatus("mandatory")
_MscExampleProvDecimalSubCreatedEntry_Object = MibTableRow
mscExampleProvDecimalSubCreatedEntry = _MscExampleProvDecimalSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1007, 1)
)
mscExampleProvDecimalSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleProvDecimalSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleProvDecimalSubCreatedEntry.setStatus("mandatory")
_MscExampleProvDecimalSubCreatedValue_Type = Link
_MscExampleProvDecimalSubCreatedValue_Object = MibTableColumn
mscExampleProvDecimalSubCreatedValue = _MscExampleProvDecimalSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1007, 1, 1),
    _MscExampleProvDecimalSubCreatedValue_Type()
)
mscExampleProvDecimalSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleProvDecimalSubCreatedValue.setStatus("mandatory")
_MscExampleProvDecimalSubCreatedRowStatus_Type = RowStatus
_MscExampleProvDecimalSubCreatedRowStatus_Object = MibTableColumn
mscExampleProvDecimalSubCreatedRowStatus = _MscExampleProvDecimalSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1007, 1, 2),
    _MscExampleProvDecimalSubCreatedRowStatus_Type()
)
mscExampleProvDecimalSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleProvDecimalSubCreatedRowStatus.setStatus("mandatory")
_MscExampleProvFixedPtSubCreatedTable_Object = MibTable
mscExampleProvFixedPtSubCreatedTable = _MscExampleProvFixedPtSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1008)
)
if mibBuilder.loadTexts:
    mscExampleProvFixedPtSubCreatedTable.setStatus("mandatory")
_MscExampleProvFixedPtSubCreatedEntry_Object = MibTableRow
mscExampleProvFixedPtSubCreatedEntry = _MscExampleProvFixedPtSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1008, 1)
)
mscExampleProvFixedPtSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleProvFixedPtSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleProvFixedPtSubCreatedEntry.setStatus("mandatory")
_MscExampleProvFixedPtSubCreatedValue_Type = Link
_MscExampleProvFixedPtSubCreatedValue_Object = MibTableColumn
mscExampleProvFixedPtSubCreatedValue = _MscExampleProvFixedPtSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1008, 1, 1),
    _MscExampleProvFixedPtSubCreatedValue_Type()
)
mscExampleProvFixedPtSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleProvFixedPtSubCreatedValue.setStatus("mandatory")
_MscExampleProvFixedPtSubCreatedRowStatus_Type = RowStatus
_MscExampleProvFixedPtSubCreatedRowStatus_Object = MibTableColumn
mscExampleProvFixedPtSubCreatedRowStatus = _MscExampleProvFixedPtSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1008, 1, 2),
    _MscExampleProvFixedPtSubCreatedRowStatus_Type()
)
mscExampleProvFixedPtSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleProvFixedPtSubCreatedRowStatus.setStatus("mandatory")
_MscExampleProvSignedSubCreatedTable_Object = MibTable
mscExampleProvSignedSubCreatedTable = _MscExampleProvSignedSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1009)
)
if mibBuilder.loadTexts:
    mscExampleProvSignedSubCreatedTable.setStatus("mandatory")
_MscExampleProvSignedSubCreatedEntry_Object = MibTableRow
mscExampleProvSignedSubCreatedEntry = _MscExampleProvSignedSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1009, 1)
)
mscExampleProvSignedSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleProvSignedSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleProvSignedSubCreatedEntry.setStatus("mandatory")
_MscExampleProvSignedSubCreatedValue_Type = Link
_MscExampleProvSignedSubCreatedValue_Object = MibTableColumn
mscExampleProvSignedSubCreatedValue = _MscExampleProvSignedSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1009, 1, 1),
    _MscExampleProvSignedSubCreatedValue_Type()
)
mscExampleProvSignedSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleProvSignedSubCreatedValue.setStatus("mandatory")
_MscExampleProvSignedSubCreatedRowStatus_Type = RowStatus
_MscExampleProvSignedSubCreatedRowStatus_Object = MibTableColumn
mscExampleProvSignedSubCreatedRowStatus = _MscExampleProvSignedSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1009, 1, 2),
    _MscExampleProvSignedSubCreatedRowStatus_Type()
)
mscExampleProvSignedSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleProvSignedSubCreatedRowStatus.setStatus("mandatory")
_MscExampleProvStringSubCreatedTable_Object = MibTable
mscExampleProvStringSubCreatedTable = _MscExampleProvStringSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1010)
)
if mibBuilder.loadTexts:
    mscExampleProvStringSubCreatedTable.setStatus("mandatory")
_MscExampleProvStringSubCreatedEntry_Object = MibTableRow
mscExampleProvStringSubCreatedEntry = _MscExampleProvStringSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1010, 1)
)
mscExampleProvStringSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleProvStringSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleProvStringSubCreatedEntry.setStatus("mandatory")
_MscExampleProvStringSubCreatedValue_Type = Link
_MscExampleProvStringSubCreatedValue_Object = MibTableColumn
mscExampleProvStringSubCreatedValue = _MscExampleProvStringSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1010, 1, 1),
    _MscExampleProvStringSubCreatedValue_Type()
)
mscExampleProvStringSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleProvStringSubCreatedValue.setStatus("mandatory")
_MscExampleProvStringSubCreatedRowStatus_Type = RowStatus
_MscExampleProvStringSubCreatedRowStatus_Object = MibTableColumn
mscExampleProvStringSubCreatedRowStatus = _MscExampleProvStringSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1010, 1, 2),
    _MscExampleProvStringSubCreatedRowStatus_Type()
)
mscExampleProvStringSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleProvStringSubCreatedRowStatus.setStatus("mandatory")
_MscExampleProvEnumSubCreatedTable_Object = MibTable
mscExampleProvEnumSubCreatedTable = _MscExampleProvEnumSubCreatedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1011)
)
if mibBuilder.loadTexts:
    mscExampleProvEnumSubCreatedTable.setStatus("mandatory")
_MscExampleProvEnumSubCreatedEntry_Object = MibTableRow
mscExampleProvEnumSubCreatedEntry = _MscExampleProvEnumSubCreatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1011, 1)
)
mscExampleProvEnumSubCreatedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscExampleProvEnumSubCreatedValue"),
)
if mibBuilder.loadTexts:
    mscExampleProvEnumSubCreatedEntry.setStatus("mandatory")
_MscExampleProvEnumSubCreatedValue_Type = Link
_MscExampleProvEnumSubCreatedValue_Object = MibTableColumn
mscExampleProvEnumSubCreatedValue = _MscExampleProvEnumSubCreatedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1011, 1, 1),
    _MscExampleProvEnumSubCreatedValue_Type()
)
mscExampleProvEnumSubCreatedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscExampleProvEnumSubCreatedValue.setStatus("mandatory")
_MscExampleProvEnumSubCreatedRowStatus_Type = RowStatus
_MscExampleProvEnumSubCreatedRowStatus_Object = MibTableColumn
mscExampleProvEnumSubCreatedRowStatus = _MscExampleProvEnumSubCreatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5000, 1011, 1, 2),
    _MscExampleProvEnumSubCreatedRowStatus_Type()
)
mscExampleProvEnumSubCreatedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscExampleProvEnumSubCreatedRowStatus.setStatus("mandatory")
_MscFri_ObjectIdentity = ObjectIdentity
mscFri = _MscFri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001)
)
_MscFriRowStatusTable_Object = MibTable
mscFriRowStatusTable = _MscFriRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1)
)
if mibBuilder.loadTexts:
    mscFriRowStatusTable.setStatus("mandatory")
_MscFriRowStatusEntry_Object = MibTableRow
mscFriRowStatusEntry = _MscFriRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1, 1)
)
mscFriRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
)
if mibBuilder.loadTexts:
    mscFriRowStatusEntry.setStatus("mandatory")
_MscFriRowStatus_Type = RowStatus
_MscFriRowStatus_Object = MibTableColumn
mscFriRowStatus = _MscFriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1, 1, 1),
    _MscFriRowStatus_Type()
)
mscFriRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriRowStatus.setStatus("mandatory")
_MscFriComponentName_Type = DisplayString
_MscFriComponentName_Object = MibTableColumn
mscFriComponentName = _MscFriComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1, 1, 2),
    _MscFriComponentName_Type()
)
mscFriComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriComponentName.setStatus("mandatory")
_MscFriStorageType_Type = StorageType
_MscFriStorageType_Object = MibTableColumn
mscFriStorageType = _MscFriStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1, 1, 4),
    _MscFriStorageType_Type()
)
mscFriStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriStorageType.setStatus("mandatory")


class _MscFriIndex_Type(Integer32):
    """Custom type mscFriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MscFriIndex_Type.__name__ = "Integer32"
_MscFriIndex_Object = MibTableColumn
mscFriIndex = _MscFriIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1, 1, 10),
    _MscFriIndex_Type()
)
mscFriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriIndex.setStatus("mandatory")
_MscFriDna_ObjectIdentity = ObjectIdentity
mscFriDna = _MscFriDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4)
)
_MscFriDnaRowStatusTable_Object = MibTable
mscFriDnaRowStatusTable = _MscFriDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 1)
)
if mibBuilder.loadTexts:
    mscFriDnaRowStatusTable.setStatus("mandatory")
_MscFriDnaRowStatusEntry_Object = MibTableRow
mscFriDnaRowStatusEntry = _MscFriDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 1, 1)
)
mscFriDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFriDnaRowStatusEntry.setStatus("mandatory")
_MscFriDnaRowStatus_Type = RowStatus
_MscFriDnaRowStatus_Object = MibTableColumn
mscFriDnaRowStatus = _MscFriDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 1, 1, 1),
    _MscFriDnaRowStatus_Type()
)
mscFriDnaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDnaRowStatus.setStatus("mandatory")
_MscFriDnaComponentName_Type = DisplayString
_MscFriDnaComponentName_Object = MibTableColumn
mscFriDnaComponentName = _MscFriDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 1, 1, 2),
    _MscFriDnaComponentName_Type()
)
mscFriDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDnaComponentName.setStatus("mandatory")
_MscFriDnaStorageType_Type = StorageType
_MscFriDnaStorageType_Object = MibTableColumn
mscFriDnaStorageType = _MscFriDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 1, 1, 4),
    _MscFriDnaStorageType_Type()
)
mscFriDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDnaStorageType.setStatus("mandatory")


class _MscFriDnaIndex_Type(Integer32):
    """Custom type mscFriDnaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFriDnaIndex_Type.__name__ = "Integer32"
_MscFriDnaIndex_Object = MibTableColumn
mscFriDnaIndex = _MscFriDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 1, 1, 10),
    _MscFriDnaIndex_Type()
)
mscFriDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDnaIndex.setStatus("mandatory")
_MscFriDnaOperationalTable_Object = MibTable
mscFriDnaOperationalTable = _MscFriDnaOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 10)
)
if mibBuilder.loadTexts:
    mscFriDnaOperationalTable.setStatus("mandatory")
_MscFriDnaOperationalEntry_Object = MibTableRow
mscFriDnaOperationalEntry = _MscFriDnaOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 10, 1)
)
mscFriDnaOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFriDnaOperationalEntry.setStatus("mandatory")


class _MscFriDnaAttribute_Type(Unsigned32):
    """Custom type mscFriDnaAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFriDnaAttribute_Type.__name__ = "Unsigned32"
_MscFriDnaAttribute_Object = MibTableColumn
mscFriDnaAttribute = _MscFriDnaAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 10, 1, 1),
    _MscFriDnaAttribute_Type()
)
mscFriDnaAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDnaAttribute.setStatus("mandatory")
_MscFriDnaProvisionalTable_Object = MibTable
mscFriDnaProvisionalTable = _MscFriDnaProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 11)
)
if mibBuilder.loadTexts:
    mscFriDnaProvisionalTable.setStatus("mandatory")
_MscFriDnaProvisionalEntry_Object = MibTableRow
mscFriDnaProvisionalEntry = _MscFriDnaProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 11, 1)
)
mscFriDnaProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFriDnaProvisionalEntry.setStatus("mandatory")


class _MscFriDnaTypeOfAddress_Type(Integer32):
    """Custom type mscFriDnaTypeOfAddress based on Integer32"""
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


_MscFriDnaTypeOfAddress_Type.__name__ = "Integer32"
_MscFriDnaTypeOfAddress_Object = MibTableColumn
mscFriDnaTypeOfAddress = _MscFriDnaTypeOfAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 11, 1, 1),
    _MscFriDnaTypeOfAddress_Type()
)
mscFriDnaTypeOfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDnaTypeOfAddress.setStatus("mandatory")


class _MscFriDnaNumberPlanIndicator_Type(Integer32):
    """Custom type mscFriDnaNumberPlanIndicator based on Integer32"""
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


_MscFriDnaNumberPlanIndicator_Type.__name__ = "Integer32"
_MscFriDnaNumberPlanIndicator_Object = MibTableColumn
mscFriDnaNumberPlanIndicator = _MscFriDnaNumberPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 11, 1, 2),
    _MscFriDnaNumberPlanIndicator_Type()
)
mscFriDnaNumberPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDnaNumberPlanIndicator.setStatus("mandatory")


class _MscFriDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscFriDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFriDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscFriDnaDataNetworkAddress_Object = MibTableColumn
mscFriDnaDataNetworkAddress = _MscFriDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 4, 11, 1, 3),
    _MscFriDnaDataNetworkAddress_Type()
)
mscFriDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDnaDataNetworkAddress.setStatus("mandatory")
_MscFriDynamic_ObjectIdentity = ObjectIdentity
mscFriDynamic = _MscFriDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7)
)
_MscFriDynamicRowStatusTable_Object = MibTable
mscFriDynamicRowStatusTable = _MscFriDynamicRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 1)
)
if mibBuilder.loadTexts:
    mscFriDynamicRowStatusTable.setStatus("mandatory")
_MscFriDynamicRowStatusEntry_Object = MibTableRow
mscFriDynamicRowStatusEntry = _MscFriDynamicRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 1, 1)
)
mscFriDynamicRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynamicIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynamicRowStatusEntry.setStatus("mandatory")
_MscFriDynamicRowStatus_Type = RowStatus
_MscFriDynamicRowStatus_Object = MibTableColumn
mscFriDynamicRowStatus = _MscFriDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 1, 1, 1),
    _MscFriDynamicRowStatus_Type()
)
mscFriDynamicRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynamicRowStatus.setStatus("mandatory")
_MscFriDynamicComponentName_Type = DisplayString
_MscFriDynamicComponentName_Object = MibTableColumn
mscFriDynamicComponentName = _MscFriDynamicComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 1, 1, 2),
    _MscFriDynamicComponentName_Type()
)
mscFriDynamicComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynamicComponentName.setStatus("mandatory")
_MscFriDynamicStorageType_Type = StorageType
_MscFriDynamicStorageType_Object = MibTableColumn
mscFriDynamicStorageType = _MscFriDynamicStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 1, 1, 4),
    _MscFriDynamicStorageType_Type()
)
mscFriDynamicStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynamicStorageType.setStatus("mandatory")


class _MscFriDynamicIndex_Type(Integer32):
    """Custom type mscFriDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFriDynamicIndex_Type.__name__ = "Integer32"
_MscFriDynamicIndex_Object = MibTableColumn
mscFriDynamicIndex = _MscFriDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 1, 1, 10),
    _MscFriDynamicIndex_Type()
)
mscFriDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDynamicIndex.setStatus("mandatory")
_MscFriDynamicOperationalTable_Object = MibTable
mscFriDynamicOperationalTable = _MscFriDynamicOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 10)
)
if mibBuilder.loadTexts:
    mscFriDynamicOperationalTable.setStatus("mandatory")
_MscFriDynamicOperationalEntry_Object = MibTableRow
mscFriDynamicOperationalEntry = _MscFriDynamicOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 10, 1)
)
mscFriDynamicOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynamicIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynamicOperationalEntry.setStatus("mandatory")


class _MscFriDynamicAttribute_Type(Unsigned32):
    """Custom type mscFriDynamicAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynamicAttribute_Type.__name__ = "Unsigned32"
_MscFriDynamicAttribute_Object = MibTableColumn
mscFriDynamicAttribute = _MscFriDynamicAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 7, 10, 1, 1),
    _MscFriDynamicAttribute_Type()
)
mscFriDynamicAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynamicAttribute.setStatus("mandatory")
_MscFriDynOp_ObjectIdentity = ObjectIdentity
mscFriDynOp = _MscFriDynOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8)
)
_MscFriDynOpRowStatusTable_Object = MibTable
mscFriDynOpRowStatusTable = _MscFriDynOpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 1)
)
if mibBuilder.loadTexts:
    mscFriDynOpRowStatusTable.setStatus("mandatory")
_MscFriDynOpRowStatusEntry_Object = MibTableRow
mscFriDynOpRowStatusEntry = _MscFriDynOpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 1, 1)
)
mscFriDynOpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpRowStatusEntry.setStatus("mandatory")
_MscFriDynOpRowStatus_Type = RowStatus
_MscFriDynOpRowStatus_Object = MibTableColumn
mscFriDynOpRowStatus = _MscFriDynOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 1, 1, 1),
    _MscFriDynOpRowStatus_Type()
)
mscFriDynOpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpRowStatus.setStatus("mandatory")
_MscFriDynOpComponentName_Type = DisplayString
_MscFriDynOpComponentName_Object = MibTableColumn
mscFriDynOpComponentName = _MscFriDynOpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 1, 1, 2),
    _MscFriDynOpComponentName_Type()
)
mscFriDynOpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpComponentName.setStatus("mandatory")
_MscFriDynOpStorageType_Type = StorageType
_MscFriDynOpStorageType_Object = MibTableColumn
mscFriDynOpStorageType = _MscFriDynOpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 1, 1, 4),
    _MscFriDynOpStorageType_Type()
)
mscFriDynOpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpStorageType.setStatus("mandatory")


class _MscFriDynOpIndex_Type(Integer32):
    """Custom type mscFriDynOpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFriDynOpIndex_Type.__name__ = "Integer32"
_MscFriDynOpIndex_Object = MibTableColumn
mscFriDynOpIndex = _MscFriDynOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 1, 1, 10),
    _MscFriDynOpIndex_Type()
)
mscFriDynOpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDynOpIndex.setStatus("mandatory")
_MscFriDynOpInitial_ObjectIdentity = ObjectIdentity
mscFriDynOpInitial = _MscFriDynOpInitial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2)
)
_MscFriDynOpInitialRowStatusTable_Object = MibTable
mscFriDynOpInitialRowStatusTable = _MscFriDynOpInitialRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscFriDynOpInitialRowStatusTable.setStatus("mandatory")
_MscFriDynOpInitialRowStatusEntry_Object = MibTableRow
mscFriDynOpInitialRowStatusEntry = _MscFriDynOpInitialRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 1, 1)
)
mscFriDynOpInitialRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpInitialIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpInitialRowStatusEntry.setStatus("mandatory")
_MscFriDynOpInitialRowStatus_Type = RowStatus
_MscFriDynOpInitialRowStatus_Object = MibTableColumn
mscFriDynOpInitialRowStatus = _MscFriDynOpInitialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 1, 1, 1),
    _MscFriDynOpInitialRowStatus_Type()
)
mscFriDynOpInitialRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpInitialRowStatus.setStatus("mandatory")
_MscFriDynOpInitialComponentName_Type = DisplayString
_MscFriDynOpInitialComponentName_Object = MibTableColumn
mscFriDynOpInitialComponentName = _MscFriDynOpInitialComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 1, 1, 2),
    _MscFriDynOpInitialComponentName_Type()
)
mscFriDynOpInitialComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpInitialComponentName.setStatus("mandatory")
_MscFriDynOpInitialStorageType_Type = StorageType
_MscFriDynOpInitialStorageType_Object = MibTableColumn
mscFriDynOpInitialStorageType = _MscFriDynOpInitialStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 1, 1, 4),
    _MscFriDynOpInitialStorageType_Type()
)
mscFriDynOpInitialStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpInitialStorageType.setStatus("mandatory")
_MscFriDynOpInitialIndex_Type = NonReplicated
_MscFriDynOpInitialIndex_Object = MibTableColumn
mscFriDynOpInitialIndex = _MscFriDynOpInitialIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 1, 1, 10),
    _MscFriDynOpInitialIndex_Type()
)
mscFriDynOpInitialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDynOpInitialIndex.setStatus("mandatory")
_MscFriDynOpInitialOperationalTable_Object = MibTable
mscFriDynOpInitialOperationalTable = _MscFriDynOpInitialOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscFriDynOpInitialOperationalTable.setStatus("mandatory")
_MscFriDynOpInitialOperationalEntry_Object = MibTableRow
mscFriDynOpInitialOperationalEntry = _MscFriDynOpInitialOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 10, 1)
)
mscFriDynOpInitialOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpInitialIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpInitialOperationalEntry.setStatus("mandatory")


class _MscFriDynOpInitialAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpInitialAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpInitialAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpInitialAttribute_Object = MibTableColumn
mscFriDynOpInitialAttribute = _MscFriDynOpInitialAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 10, 1, 1),
    _MscFriDynOpInitialAttribute_Type()
)
mscFriDynOpInitialAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpInitialAttribute.setStatus("mandatory")
_MscFriDynOpInitialProvisionedTable_Object = MibTable
mscFriDynOpInitialProvisionedTable = _MscFriDynOpInitialProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 11)
)
if mibBuilder.loadTexts:
    mscFriDynOpInitialProvisionedTable.setStatus("mandatory")
_MscFriDynOpInitialProvisionedEntry_Object = MibTableRow
mscFriDynOpInitialProvisionedEntry = _MscFriDynOpInitialProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 11, 1)
)
mscFriDynOpInitialProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpInitialIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpInitialProvisionedEntry.setStatus("mandatory")


class _MscFriDynOpInitialProvAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpInitialProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpInitialProvAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpInitialProvAttribute_Object = MibTableColumn
mscFriDynOpInitialProvAttribute = _MscFriDynOpInitialProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 2, 11, 1, 1),
    _MscFriDynOpInitialProvAttribute_Type()
)
mscFriDynOpInitialProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpInitialProvAttribute.setStatus("mandatory")
_MscFriDynOpOptional_ObjectIdentity = ObjectIdentity
mscFriDynOpOptional = _MscFriDynOpOptional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3)
)
_MscFriDynOpOptionalRowStatusTable_Object = MibTable
mscFriDynOpOptionalRowStatusTable = _MscFriDynOpOptionalRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 1)
)
if mibBuilder.loadTexts:
    mscFriDynOpOptionalRowStatusTable.setStatus("mandatory")
_MscFriDynOpOptionalRowStatusEntry_Object = MibTableRow
mscFriDynOpOptionalRowStatusEntry = _MscFriDynOpOptionalRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 1, 1)
)
mscFriDynOpOptionalRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpOptionalIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpOptionalRowStatusEntry.setStatus("mandatory")
_MscFriDynOpOptionalRowStatus_Type = RowStatus
_MscFriDynOpOptionalRowStatus_Object = MibTableColumn
mscFriDynOpOptionalRowStatus = _MscFriDynOpOptionalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 1, 1, 1),
    _MscFriDynOpOptionalRowStatus_Type()
)
mscFriDynOpOptionalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpOptionalRowStatus.setStatus("mandatory")
_MscFriDynOpOptionalComponentName_Type = DisplayString
_MscFriDynOpOptionalComponentName_Object = MibTableColumn
mscFriDynOpOptionalComponentName = _MscFriDynOpOptionalComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 1, 1, 2),
    _MscFriDynOpOptionalComponentName_Type()
)
mscFriDynOpOptionalComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpOptionalComponentName.setStatus("mandatory")
_MscFriDynOpOptionalStorageType_Type = StorageType
_MscFriDynOpOptionalStorageType_Object = MibTableColumn
mscFriDynOpOptionalStorageType = _MscFriDynOpOptionalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 1, 1, 4),
    _MscFriDynOpOptionalStorageType_Type()
)
mscFriDynOpOptionalStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpOptionalStorageType.setStatus("mandatory")
_MscFriDynOpOptionalIndex_Type = NonReplicated
_MscFriDynOpOptionalIndex_Object = MibTableColumn
mscFriDynOpOptionalIndex = _MscFriDynOpOptionalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 1, 1, 10),
    _MscFriDynOpOptionalIndex_Type()
)
mscFriDynOpOptionalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDynOpOptionalIndex.setStatus("mandatory")
_MscFriDynOpOptionalOperationalTable_Object = MibTable
mscFriDynOpOptionalOperationalTable = _MscFriDynOpOptionalOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 10)
)
if mibBuilder.loadTexts:
    mscFriDynOpOptionalOperationalTable.setStatus("mandatory")
_MscFriDynOpOptionalOperationalEntry_Object = MibTableRow
mscFriDynOpOptionalOperationalEntry = _MscFriDynOpOptionalOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 10, 1)
)
mscFriDynOpOptionalOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpOptionalIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpOptionalOperationalEntry.setStatus("mandatory")


class _MscFriDynOpOptionalAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpOptionalAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpOptionalAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpOptionalAttribute_Object = MibTableColumn
mscFriDynOpOptionalAttribute = _MscFriDynOpOptionalAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 10, 1, 1),
    _MscFriDynOpOptionalAttribute_Type()
)
mscFriDynOpOptionalAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpOptionalAttribute.setStatus("mandatory")
_MscFriDynOpOptionalProvisionedTable_Object = MibTable
mscFriDynOpOptionalProvisionedTable = _MscFriDynOpOptionalProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 11)
)
if mibBuilder.loadTexts:
    mscFriDynOpOptionalProvisionedTable.setStatus("mandatory")
_MscFriDynOpOptionalProvisionedEntry_Object = MibTableRow
mscFriDynOpOptionalProvisionedEntry = _MscFriDynOpOptionalProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 11, 1)
)
mscFriDynOpOptionalProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpOptionalIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpOptionalProvisionedEntry.setStatus("mandatory")


class _MscFriDynOpOptionalProvAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpOptionalProvAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpOptionalProvAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpOptionalProvAttribute_Object = MibTableColumn
mscFriDynOpOptionalProvAttribute = _MscFriDynOpOptionalProvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 3, 11, 1, 1),
    _MscFriDynOpOptionalProvAttribute_Type()
)
mscFriDynOpOptionalProvAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpOptionalProvAttribute.setStatus("mandatory")
_MscFriDynOpDynamic_ObjectIdentity = ObjectIdentity
mscFriDynOpDynamic = _MscFriDynOpDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4)
)
_MscFriDynOpDynamicRowStatusTable_Object = MibTable
mscFriDynOpDynamicRowStatusTable = _MscFriDynOpDynamicRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 1)
)
if mibBuilder.loadTexts:
    mscFriDynOpDynamicRowStatusTable.setStatus("mandatory")
_MscFriDynOpDynamicRowStatusEntry_Object = MibTableRow
mscFriDynOpDynamicRowStatusEntry = _MscFriDynOpDynamicRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 1, 1)
)
mscFriDynOpDynamicRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpDynamicIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpDynamicRowStatusEntry.setStatus("mandatory")
_MscFriDynOpDynamicRowStatus_Type = RowStatus
_MscFriDynOpDynamicRowStatus_Object = MibTableColumn
mscFriDynOpDynamicRowStatus = _MscFriDynOpDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 1, 1, 1),
    _MscFriDynOpDynamicRowStatus_Type()
)
mscFriDynOpDynamicRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpDynamicRowStatus.setStatus("mandatory")
_MscFriDynOpDynamicComponentName_Type = DisplayString
_MscFriDynOpDynamicComponentName_Object = MibTableColumn
mscFriDynOpDynamicComponentName = _MscFriDynOpDynamicComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 1, 1, 2),
    _MscFriDynOpDynamicComponentName_Type()
)
mscFriDynOpDynamicComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpDynamicComponentName.setStatus("mandatory")
_MscFriDynOpDynamicStorageType_Type = StorageType
_MscFriDynOpDynamicStorageType_Object = MibTableColumn
mscFriDynOpDynamicStorageType = _MscFriDynOpDynamicStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 1, 1, 4),
    _MscFriDynOpDynamicStorageType_Type()
)
mscFriDynOpDynamicStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpDynamicStorageType.setStatus("mandatory")
_MscFriDynOpDynamicIndex_Type = NonReplicated
_MscFriDynOpDynamicIndex_Object = MibTableColumn
mscFriDynOpDynamicIndex = _MscFriDynOpDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 1, 1, 10),
    _MscFriDynOpDynamicIndex_Type()
)
mscFriDynOpDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDynOpDynamicIndex.setStatus("mandatory")
_MscFriDynOpDynamicOperationalTable_Object = MibTable
mscFriDynOpDynamicOperationalTable = _MscFriDynOpDynamicOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 10)
)
if mibBuilder.loadTexts:
    mscFriDynOpDynamicOperationalTable.setStatus("mandatory")
_MscFriDynOpDynamicOperationalEntry_Object = MibTableRow
mscFriDynOpDynamicOperationalEntry = _MscFriDynOpDynamicOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 10, 1)
)
mscFriDynOpDynamicOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpDynamicIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpDynamicOperationalEntry.setStatus("mandatory")


class _MscFriDynOpDynamicAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpDynamicAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpDynamicAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpDynamicAttribute_Object = MibTableColumn
mscFriDynOpDynamicAttribute = _MscFriDynOpDynamicAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 4, 10, 1, 1),
    _MscFriDynOpDynamicAttribute_Type()
)
mscFriDynOpDynamicAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpDynamicAttribute.setStatus("mandatory")
_MscFriDynOpDynOpJr_ObjectIdentity = ObjectIdentity
mscFriDynOpDynOpJr = _MscFriDynOpDynOpJr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5)
)
_MscFriDynOpDynOpJrRowStatusTable_Object = MibTable
mscFriDynOpDynOpJrRowStatusTable = _MscFriDynOpDynOpJrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 1)
)
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrRowStatusTable.setStatus("mandatory")
_MscFriDynOpDynOpJrRowStatusEntry_Object = MibTableRow
mscFriDynOpDynOpJrRowStatusEntry = _MscFriDynOpDynOpJrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 1, 1)
)
mscFriDynOpDynOpJrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpDynOpJrIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrRowStatusEntry.setStatus("mandatory")
_MscFriDynOpDynOpJrRowStatus_Type = RowStatus
_MscFriDynOpDynOpJrRowStatus_Object = MibTableColumn
mscFriDynOpDynOpJrRowStatus = _MscFriDynOpDynOpJrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 1, 1, 1),
    _MscFriDynOpDynOpJrRowStatus_Type()
)
mscFriDynOpDynOpJrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrRowStatus.setStatus("mandatory")
_MscFriDynOpDynOpJrComponentName_Type = DisplayString
_MscFriDynOpDynOpJrComponentName_Object = MibTableColumn
mscFriDynOpDynOpJrComponentName = _MscFriDynOpDynOpJrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 1, 1, 2),
    _MscFriDynOpDynOpJrComponentName_Type()
)
mscFriDynOpDynOpJrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrComponentName.setStatus("mandatory")
_MscFriDynOpDynOpJrStorageType_Type = StorageType
_MscFriDynOpDynOpJrStorageType_Object = MibTableColumn
mscFriDynOpDynOpJrStorageType = _MscFriDynOpDynOpJrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 1, 1, 4),
    _MscFriDynOpDynOpJrStorageType_Type()
)
mscFriDynOpDynOpJrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrStorageType.setStatus("mandatory")
_MscFriDynOpDynOpJrIndex_Type = NonReplicated
_MscFriDynOpDynOpJrIndex_Object = MibTableColumn
mscFriDynOpDynOpJrIndex = _MscFriDynOpDynOpJrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 1, 1, 10),
    _MscFriDynOpDynOpJrIndex_Type()
)
mscFriDynOpDynOpJrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrIndex.setStatus("mandatory")
_MscFriDynOpDynOpJrOperationalTable_Object = MibTable
mscFriDynOpDynOpJrOperationalTable = _MscFriDynOpDynOpJrOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 10)
)
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrOperationalTable.setStatus("mandatory")
_MscFriDynOpDynOpJrOperationalEntry_Object = MibTableRow
mscFriDynOpDynOpJrOperationalEntry = _MscFriDynOpDynOpJrOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 10, 1)
)
mscFriDynOpDynOpJrOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpDynOpJrIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrOperationalEntry.setStatus("mandatory")


class _MscFriDynOpDynOpJrAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpDynOpJrAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpDynOpJrAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpDynOpJrAttribute_Object = MibTableColumn
mscFriDynOpDynOpJrAttribute = _MscFriDynOpDynOpJrAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 5, 10, 1, 1),
    _MscFriDynOpDynOpJrAttribute_Type()
)
mscFriDynOpDynOpJrAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpDynOpJrAttribute.setStatus("mandatory")
_MscFriDynOpOperationalTable_Object = MibTable
mscFriDynOpOperationalTable = _MscFriDynOpOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 10)
)
if mibBuilder.loadTexts:
    mscFriDynOpOperationalTable.setStatus("mandatory")
_MscFriDynOpOperationalEntry_Object = MibTableRow
mscFriDynOpOperationalEntry = _MscFriDynOpOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 10, 1)
)
mscFriDynOpOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriDynOpIndex"),
)
if mibBuilder.loadTexts:
    mscFriDynOpOperationalEntry.setStatus("mandatory")


class _MscFriDynOpAttribute_Type(Unsigned32):
    """Custom type mscFriDynOpAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriDynOpAttribute_Type.__name__ = "Unsigned32"
_MscFriDynOpAttribute_Object = MibTableColumn
mscFriDynOpAttribute = _MscFriDynOpAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 8, 10, 1, 1),
    _MscFriDynOpAttribute_Type()
)
mscFriDynOpAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriDynOpAttribute.setStatus("mandatory")
_MscFriEvent_ObjectIdentity = ObjectIdentity
mscFriEvent = _MscFriEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9)
)
_MscFriEventRowStatusTable_Object = MibTable
mscFriEventRowStatusTable = _MscFriEventRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9, 1)
)
if mibBuilder.loadTexts:
    mscFriEventRowStatusTable.setStatus("mandatory")
_MscFriEventRowStatusEntry_Object = MibTableRow
mscFriEventRowStatusEntry = _MscFriEventRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9, 1, 1)
)
mscFriEventRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriEventIndex"),
)
if mibBuilder.loadTexts:
    mscFriEventRowStatusEntry.setStatus("mandatory")
_MscFriEventRowStatus_Type = RowStatus
_MscFriEventRowStatus_Object = MibTableColumn
mscFriEventRowStatus = _MscFriEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9, 1, 1, 1),
    _MscFriEventRowStatus_Type()
)
mscFriEventRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriEventRowStatus.setStatus("mandatory")
_MscFriEventComponentName_Type = DisplayString
_MscFriEventComponentName_Object = MibTableColumn
mscFriEventComponentName = _MscFriEventComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9, 1, 1, 2),
    _MscFriEventComponentName_Type()
)
mscFriEventComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriEventComponentName.setStatus("mandatory")
_MscFriEventStorageType_Type = StorageType
_MscFriEventStorageType_Object = MibTableColumn
mscFriEventStorageType = _MscFriEventStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9, 1, 1, 4),
    _MscFriEventStorageType_Type()
)
mscFriEventStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriEventStorageType.setStatus("mandatory")
_MscFriEventIndex_Type = NonReplicated
_MscFriEventIndex_Object = MibTableColumn
mscFriEventIndex = _MscFriEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 9, 1, 1, 10),
    _MscFriEventIndex_Type()
)
mscFriEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriEventIndex.setStatus("mandatory")
_MscFriRegistered_ObjectIdentity = ObjectIdentity
mscFriRegistered = _MscFriRegistered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18)
)
_MscFriRegisteredRowStatusTable_Object = MibTable
mscFriRegisteredRowStatusTable = _MscFriRegisteredRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 1)
)
if mibBuilder.loadTexts:
    mscFriRegisteredRowStatusTable.setStatus("mandatory")
_MscFriRegisteredRowStatusEntry_Object = MibTableRow
mscFriRegisteredRowStatusEntry = _MscFriRegisteredRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 1, 1)
)
mscFriRegisteredRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriRegisteredIndex"),
)
if mibBuilder.loadTexts:
    mscFriRegisteredRowStatusEntry.setStatus("mandatory")
_MscFriRegisteredRowStatus_Type = RowStatus
_MscFriRegisteredRowStatus_Object = MibTableColumn
mscFriRegisteredRowStatus = _MscFriRegisteredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 1, 1, 1),
    _MscFriRegisteredRowStatus_Type()
)
mscFriRegisteredRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriRegisteredRowStatus.setStatus("mandatory")
_MscFriRegisteredComponentName_Type = DisplayString
_MscFriRegisteredComponentName_Object = MibTableColumn
mscFriRegisteredComponentName = _MscFriRegisteredComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 1, 1, 2),
    _MscFriRegisteredComponentName_Type()
)
mscFriRegisteredComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriRegisteredComponentName.setStatus("mandatory")
_MscFriRegisteredStorageType_Type = StorageType
_MscFriRegisteredStorageType_Object = MibTableColumn
mscFriRegisteredStorageType = _MscFriRegisteredStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 1, 1, 4),
    _MscFriRegisteredStorageType_Type()
)
mscFriRegisteredStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriRegisteredStorageType.setStatus("mandatory")


class _MscFriRegisteredIndex_Type(Integer32):
    """Custom type mscFriRegisteredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFriRegisteredIndex_Type.__name__ = "Integer32"
_MscFriRegisteredIndex_Object = MibTableColumn
mscFriRegisteredIndex = _MscFriRegisteredIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 1, 1, 10),
    _MscFriRegisteredIndex_Type()
)
mscFriRegisteredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFriRegisteredIndex.setStatus("mandatory")
_MscFriRegisteredDataTable_Object = MibTable
mscFriRegisteredDataTable = _MscFriRegisteredDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 10)
)
if mibBuilder.loadTexts:
    mscFriRegisteredDataTable.setStatus("mandatory")
_MscFriRegisteredDataEntry_Object = MibTableRow
mscFriRegisteredDataEntry = _MscFriRegisteredDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 10, 1)
)
mscFriRegisteredDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriRegisteredIndex"),
)
if mibBuilder.loadTexts:
    mscFriRegisteredDataEntry.setStatus("mandatory")


class _MscFriRegisteredAttribute_Type(Unsigned32):
    """Custom type mscFriRegisteredAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriRegisteredAttribute_Type.__name__ = "Unsigned32"
_MscFriRegisteredAttribute_Object = MibTableColumn
mscFriRegisteredAttribute = _MscFriRegisteredAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 18, 10, 1, 1),
    _MscFriRegisteredAttribute_Type()
)
mscFriRegisteredAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriRegisteredAttribute.setStatus("mandatory")
_MscFriOperationalTable_Object = MibTable
mscFriOperationalTable = _MscFriOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100)
)
if mibBuilder.loadTexts:
    mscFriOperationalTable.setStatus("mandatory")
_MscFriOperationalEntry_Object = MibTableRow
mscFriOperationalEntry = _MscFriOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1)
)
mscFriOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
)
if mibBuilder.loadTexts:
    mscFriOperationalEntry.setStatus("mandatory")


class _MscFriOperationalFreeSimpleAscii_Type(AsciiString):
    """Custom type mscFriOperationalFreeSimpleAscii based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalFreeSimpleAscii_Type.__name__ = "AsciiString"
_MscFriOperationalFreeSimpleAscii_Object = MibTableColumn
mscFriOperationalFreeSimpleAscii = _MscFriOperationalFreeSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 1),
    _MscFriOperationalFreeSimpleAscii_Type()
)
mscFriOperationalFreeSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleAscii.setStatus("mandatory")


class _MscFriOperationalFreeSimpleDashed_Type(DashedHexString):
    """Custom type mscFriOperationalFreeSimpleDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalFreeSimpleDashed_Type.__name__ = "DashedHexString"
_MscFriOperationalFreeSimpleDashed_Object = MibTableColumn
mscFriOperationalFreeSimpleDashed = _MscFriOperationalFreeSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 2),
    _MscFriOperationalFreeSimpleDashed_Type()
)
mscFriOperationalFreeSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleDashed.setStatus("mandatory")


class _MscFriOperationalFreeSimpleExtended_Type(ExtendedAsciiString):
    """Custom type mscFriOperationalFreeSimpleExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalFreeSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_MscFriOperationalFreeSimpleExtended_Object = MibTableColumn
mscFriOperationalFreeSimpleExtended = _MscFriOperationalFreeSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 3),
    _MscFriOperationalFreeSimpleExtended_Type()
)
mscFriOperationalFreeSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleExtended.setStatus("mandatory")


class _MscFriOperationalFreeSimpleBcd_Type(DigitString):
    """Custom type mscFriOperationalFreeSimpleBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_MscFriOperationalFreeSimpleBcd_Type.__name__ = "DigitString"
_MscFriOperationalFreeSimpleBcd_Object = MibTableColumn
mscFriOperationalFreeSimpleBcd = _MscFriOperationalFreeSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 4),
    _MscFriOperationalFreeSimpleBcd_Type()
)
mscFriOperationalFreeSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleBcd.setStatus("mandatory")


class _MscFriOperationalFreeSimpleSigned_Type(Integer32):
    """Custom type mscFriOperationalFreeSimpleSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 10),
    )


_MscFriOperationalFreeSimpleSigned_Type.__name__ = "Integer32"
_MscFriOperationalFreeSimpleSigned_Object = MibTableColumn
mscFriOperationalFreeSimpleSigned = _MscFriOperationalFreeSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 5),
    _MscFriOperationalFreeSimpleSigned_Type()
)
mscFriOperationalFreeSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleSigned.setStatus("mandatory")


class _MscFriOperationalFreeSimpleFixed_Type(FixedPoint1):
    """Custom type mscFriOperationalFreeSimpleFixed based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(55, 66),
    )


_MscFriOperationalFreeSimpleFixed_Type.__name__ = "FixedPoint1"
_MscFriOperationalFreeSimpleFixed_Object = MibTableColumn
mscFriOperationalFreeSimpleFixed = _MscFriOperationalFreeSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 6),
    _MscFriOperationalFreeSimpleFixed_Type()
)
mscFriOperationalFreeSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleFixed.setStatus("mandatory")


class _MscFriOperationalFreeSimpleSequence_Type(IntegerSequence):
    """Custom type mscFriOperationalFreeSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 11),
    )


_MscFriOperationalFreeSimpleSequence_Type.__name__ = "IntegerSequence"
_MscFriOperationalFreeSimpleSequence_Object = MibTableColumn
mscFriOperationalFreeSimpleSequence = _MscFriOperationalFreeSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 7),
    _MscFriOperationalFreeSimpleSequence_Type()
)
mscFriOperationalFreeSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleSequence.setStatus("mandatory")
_MscFriOperationalFreeSimpleObjId_Type = IntegerSequence
_MscFriOperationalFreeSimpleObjId_Object = MibTableColumn
mscFriOperationalFreeSimpleObjId = _MscFriOperationalFreeSimpleObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 8),
    _MscFriOperationalFreeSimpleObjId_Type()
)
mscFriOperationalFreeSimpleObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleObjId.setStatus("mandatory")
_MscFriOperationalFreeSimpleComponent_Type = RowPointer
_MscFriOperationalFreeSimpleComponent_Object = MibTableColumn
mscFriOperationalFreeSimpleComponent = _MscFriOperationalFreeSimpleComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 9),
    _MscFriOperationalFreeSimpleComponent_Type()
)
mscFriOperationalFreeSimpleComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleComponent.setStatus("mandatory")


class _MscFriOperationalFreeSimpleHex_Type(HexString):
    """Custom type mscFriOperationalFreeSimpleHex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscFriOperationalFreeSimpleHex_Type.__name__ = "HexString"
_MscFriOperationalFreeSimpleHex_Object = MibTableColumn
mscFriOperationalFreeSimpleHex = _MscFriOperationalFreeSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 10),
    _MscFriOperationalFreeSimpleHex_Type()
)
mscFriOperationalFreeSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalFreeSimpleHex.setStatus("mandatory")


class _MscFriOperationalStructSetEnumeration_Type(OctetString):
    """Custom type mscFriOperationalStructSetEnumeration based on OctetString"""
    defaultHexValue = "9100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFriOperationalStructSetEnumeration_Type.__name__ = "OctetString"
_MscFriOperationalStructSetEnumeration_Object = MibTableColumn
mscFriOperationalStructSetEnumeration = _MscFriOperationalStructSetEnumeration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 11),
    _MscFriOperationalStructSetEnumeration_Type()
)
mscFriOperationalStructSetEnumeration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSetEnumeration.setStatus("mandatory")


class _MscFriOperationalStructSetUnsigned_Type(OctetString):
    """Custom type mscFriOperationalStructSetUnsigned based on OctetString"""
    defaultHexValue = "54"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFriOperationalStructSetUnsigned_Type.__name__ = "OctetString"
_MscFriOperationalStructSetUnsigned_Object = MibTableColumn
mscFriOperationalStructSetUnsigned = _MscFriOperationalStructSetUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 12),
    _MscFriOperationalStructSetUnsigned_Type()
)
mscFriOperationalStructSetUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSetUnsigned.setStatus("mandatory")


class _MscFriOperationalStructSimpleAscii_Type(AsciiString):
    """Custom type mscFriOperationalStructSimpleAscii based on AsciiString"""
    defaultHexValue = "61313063686172737472696e67"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalStructSimpleAscii_Type.__name__ = "AsciiString"
_MscFriOperationalStructSimpleAscii_Object = MibTableColumn
mscFriOperationalStructSimpleAscii = _MscFriOperationalStructSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 13),
    _MscFriOperationalStructSimpleAscii_Type()
)
mscFriOperationalStructSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleAscii.setStatus("mandatory")


class _MscFriOperationalStructSimpleDashed_Type(DashedHexString):
    """Custom type mscFriOperationalStructSimpleDashed based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalStructSimpleDashed_Type.__name__ = "DashedHexString"
_MscFriOperationalStructSimpleDashed_Object = MibTableColumn
mscFriOperationalStructSimpleDashed = _MscFriOperationalStructSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 14),
    _MscFriOperationalStructSimpleDashed_Type()
)
mscFriOperationalStructSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleDashed.setStatus("mandatory")


class _MscFriOperationalStructSimpleExtended_Type(ExtendedAsciiString):
    """Custom type mscFriOperationalStructSimpleExtended based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalStructSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_MscFriOperationalStructSimpleExtended_Object = MibTableColumn
mscFriOperationalStructSimpleExtended = _MscFriOperationalStructSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 15),
    _MscFriOperationalStructSimpleExtended_Type()
)
mscFriOperationalStructSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleExtended.setStatus("mandatory")


class _MscFriOperationalStructSimpleBcd_Type(DigitString):
    """Custom type mscFriOperationalStructSimpleBcd based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_MscFriOperationalStructSimpleBcd_Type.__name__ = "DigitString"
_MscFriOperationalStructSimpleBcd_Object = MibTableColumn
mscFriOperationalStructSimpleBcd = _MscFriOperationalStructSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 16),
    _MscFriOperationalStructSimpleBcd_Type()
)
mscFriOperationalStructSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleBcd.setStatus("mandatory")


class _MscFriOperationalStructSimpleSigned_Type(Integer32):
    """Custom type mscFriOperationalStructSimpleSigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 10),
    )


_MscFriOperationalStructSimpleSigned_Type.__name__ = "Integer32"
_MscFriOperationalStructSimpleSigned_Object = MibTableColumn
mscFriOperationalStructSimpleSigned = _MscFriOperationalStructSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 17),
    _MscFriOperationalStructSimpleSigned_Type()
)
mscFriOperationalStructSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleSigned.setStatus("mandatory")


class _MscFriOperationalStructSimpleFixed_Type(FixedPoint1):
    """Custom type mscFriOperationalStructSimpleFixed based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 29),
    )


_MscFriOperationalStructSimpleFixed_Type.__name__ = "FixedPoint1"
_MscFriOperationalStructSimpleFixed_Object = MibTableColumn
mscFriOperationalStructSimpleFixed = _MscFriOperationalStructSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 18),
    _MscFriOperationalStructSimpleFixed_Type()
)
mscFriOperationalStructSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleFixed.setStatus("mandatory")


class _MscFriOperationalStructSimpleSequence_Type(IntegerSequence):
    """Custom type mscFriOperationalStructSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_MscFriOperationalStructSimpleSequence_Type.__name__ = "IntegerSequence"
_MscFriOperationalStructSimpleSequence_Object = MibTableColumn
mscFriOperationalStructSimpleSequence = _MscFriOperationalStructSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 19),
    _MscFriOperationalStructSimpleSequence_Type()
)
mscFriOperationalStructSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleSequence.setStatus("mandatory")


class _MscFriOperationalStructSimpleEnum_Type(Integer32):
    """Custom type mscFriOperationalStructSimpleEnum based on Integer32"""
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


_MscFriOperationalStructSimpleEnum_Type.__name__ = "Integer32"
_MscFriOperationalStructSimpleEnum_Object = MibTableColumn
mscFriOperationalStructSimpleEnum = _MscFriOperationalStructSimpleEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 20),
    _MscFriOperationalStructSimpleEnum_Type()
)
mscFriOperationalStructSimpleEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleEnum.setStatus("mandatory")


class _MscFriOperationalStructSimpleHex_Type(HexString):
    """Custom type mscFriOperationalStructSimpleHex based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriOperationalStructSimpleHex_Type.__name__ = "HexString"
_MscFriOperationalStructSimpleHex_Object = MibTableColumn
mscFriOperationalStructSimpleHex = _MscFriOperationalStructSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 21),
    _MscFriOperationalStructSimpleHex_Type()
)
mscFriOperationalStructSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleHex.setStatus("mandatory")


class _MscFriOperationalStructSimpleUnsigned_Type(Unsigned32):
    """Custom type mscFriOperationalStructSimpleUnsigned based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscFriOperationalStructSimpleUnsigned_Type.__name__ = "Unsigned32"
_MscFriOperationalStructSimpleUnsigned_Object = MibTableColumn
mscFriOperationalStructSimpleUnsigned = _MscFriOperationalStructSimpleUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 100, 1, 22),
    _MscFriOperationalStructSimpleUnsigned_Type()
)
mscFriOperationalStructSimpleUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOperationalStructSimpleUnsigned.setStatus("mandatory")
_MscFriProvisionalTable_Object = MibTable
mscFriProvisionalTable = _MscFriProvisionalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101)
)
if mibBuilder.loadTexts:
    mscFriProvisionalTable.setStatus("mandatory")
_MscFriProvisionalEntry_Object = MibTableRow
mscFriProvisionalEntry = _MscFriProvisionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1)
)
mscFriProvisionalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
)
if mibBuilder.loadTexts:
    mscFriProvisionalEntry.setStatus("mandatory")


class _MscFriProvisionalStructSetEnumeration_Type(OctetString):
    """Custom type mscFriProvisionalStructSetEnumeration based on OctetString"""
    defaultHexValue = "a8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFriProvisionalStructSetEnumeration_Type.__name__ = "OctetString"
_MscFriProvisionalStructSetEnumeration_Object = MibTableColumn
mscFriProvisionalStructSetEnumeration = _MscFriProvisionalStructSetEnumeration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 1),
    _MscFriProvisionalStructSetEnumeration_Type()
)
mscFriProvisionalStructSetEnumeration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSetEnumeration.setStatus("mandatory")


class _MscFriProvisionalStructSetUnsigned_Type(OctetString):
    """Custom type mscFriProvisionalStructSetUnsigned based on OctetString"""
    defaultHexValue = "aaa8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFriProvisionalStructSetUnsigned_Type.__name__ = "OctetString"
_MscFriProvisionalStructSetUnsigned_Object = MibTableColumn
mscFriProvisionalStructSetUnsigned = _MscFriProvisionalStructSetUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 2),
    _MscFriProvisionalStructSetUnsigned_Type()
)
mscFriProvisionalStructSetUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSetUnsigned.setStatus("mandatory")


class _MscFriProvisionalStructSimpleAscii_Type(AsciiString):
    """Custom type mscFriProvisionalStructSimpleAscii based on AsciiString"""
    defaultHexValue = "61737472696e676f663131"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalStructSimpleAscii_Type.__name__ = "AsciiString"
_MscFriProvisionalStructSimpleAscii_Object = MibTableColumn
mscFriProvisionalStructSimpleAscii = _MscFriProvisionalStructSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 3),
    _MscFriProvisionalStructSimpleAscii_Type()
)
mscFriProvisionalStructSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleAscii.setStatus("mandatory")


class _MscFriProvisionalStructSimpleDashed_Type(DashedHexString):
    """Custom type mscFriProvisionalStructSimpleDashed based on DashedHexString"""
    defaultHexValue = "01234556789abCDef0ee"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalStructSimpleDashed_Type.__name__ = "DashedHexString"
_MscFriProvisionalStructSimpleDashed_Object = MibTableColumn
mscFriProvisionalStructSimpleDashed = _MscFriProvisionalStructSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 4),
    _MscFriProvisionalStructSimpleDashed_Type()
)
mscFriProvisionalStructSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleDashed.setStatus("mandatory")


class _MscFriProvisionalStructSimpleExtended_Type(ExtendedAsciiString):
    """Custom type mscFriProvisionalStructSimpleExtended based on ExtendedAsciiString"""
    defaultHexValue = "61006211632264336544"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalStructSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_MscFriProvisionalStructSimpleExtended_Object = MibTableColumn
mscFriProvisionalStructSimpleExtended = _MscFriProvisionalStructSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 5),
    _MscFriProvisionalStructSimpleExtended_Type()
)
mscFriProvisionalStructSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleExtended.setStatus("mandatory")


class _MscFriProvisionalStructSimpleBcd_Type(DigitString):
    """Custom type mscFriProvisionalStructSimpleBcd based on DigitString"""
    defaultHexValue = "31323334"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_MscFriProvisionalStructSimpleBcd_Type.__name__ = "DigitString"
_MscFriProvisionalStructSimpleBcd_Object = MibTableColumn
mscFriProvisionalStructSimpleBcd = _MscFriProvisionalStructSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 6),
    _MscFriProvisionalStructSimpleBcd_Type()
)
mscFriProvisionalStructSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleBcd.setStatus("mandatory")


class _MscFriProvisionalStructSimpleSequence_Type(IntegerSequence):
    """Custom type mscFriProvisionalStructSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_MscFriProvisionalStructSimpleSequence_Type.__name__ = "IntegerSequence"
_MscFriProvisionalStructSimpleSequence_Object = MibTableColumn
mscFriProvisionalStructSimpleSequence = _MscFriProvisionalStructSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 7),
    _MscFriProvisionalStructSimpleSequence_Type()
)
mscFriProvisionalStructSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleSequence.setStatus("mandatory")


class _MscFriProvisionalStructSimpleEnum_Type(Integer32):
    """Custom type mscFriProvisionalStructSimpleEnum based on Integer32"""
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


_MscFriProvisionalStructSimpleEnum_Type.__name__ = "Integer32"
_MscFriProvisionalStructSimpleEnum_Object = MibTableColumn
mscFriProvisionalStructSimpleEnum = _MscFriProvisionalStructSimpleEnum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 8),
    _MscFriProvisionalStructSimpleEnum_Type()
)
mscFriProvisionalStructSimpleEnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleEnum.setStatus("mandatory")


class _MscFriProvisionalStructSimpleHex_Type(HexString):
    """Custom type mscFriProvisionalStructSimpleHex based on HexString"""
    defaultHexValue = "3039303930393039303930393039303930393039303930393039"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalStructSimpleHex_Type.__name__ = "HexString"
_MscFriProvisionalStructSimpleHex_Object = MibTableColumn
mscFriProvisionalStructSimpleHex = _MscFriProvisionalStructSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 9),
    _MscFriProvisionalStructSimpleHex_Type()
)
mscFriProvisionalStructSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleHex.setStatus("mandatory")


class _MscFriProvisionalStructSimpleUnsigned_Type(Unsigned32):
    """Custom type mscFriProvisionalStructSimpleUnsigned based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriProvisionalStructSimpleUnsigned_Type.__name__ = "Unsigned32"
_MscFriProvisionalStructSimpleUnsigned_Object = MibTableColumn
mscFriProvisionalStructSimpleUnsigned = _MscFriProvisionalStructSimpleUnsigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 10),
    _MscFriProvisionalStructSimpleUnsigned_Type()
)
mscFriProvisionalStructSimpleUnsigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleUnsigned.setStatus("mandatory")


class _MscFriProvisionalStructSimpleSigned_Type(Integer32):
    """Custom type mscFriProvisionalStructSimpleSigned based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_MscFriProvisionalStructSimpleSigned_Type.__name__ = "Integer32"
_MscFriProvisionalStructSimpleSigned_Object = MibTableColumn
mscFriProvisionalStructSimpleSigned = _MscFriProvisionalStructSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 11),
    _MscFriProvisionalStructSimpleSigned_Type()
)
mscFriProvisionalStructSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleSigned.setStatus("mandatory")


class _MscFriProvisionalStructSimpleFixed_Type(FixedPoint2):
    """Custom type mscFriProvisionalStructSimpleFixed based on FixedPoint2"""
    defaultValue = 350

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(254, 355),
    )


_MscFriProvisionalStructSimpleFixed_Type.__name__ = "FixedPoint2"
_MscFriProvisionalStructSimpleFixed_Object = MibTableColumn
mscFriProvisionalStructSimpleFixed = _MscFriProvisionalStructSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 12),
    _MscFriProvisionalStructSimpleFixed_Type()
)
mscFriProvisionalStructSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalStructSimpleFixed.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleAscii_Type(AsciiString):
    """Custom type mscFriProvisionalFreeSimpleAscii based on AsciiString"""
    defaultHexValue = "61737472696e676f663131"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalFreeSimpleAscii_Type.__name__ = "AsciiString"
_MscFriProvisionalFreeSimpleAscii_Object = MibTableColumn
mscFriProvisionalFreeSimpleAscii = _MscFriProvisionalFreeSimpleAscii_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 13),
    _MscFriProvisionalFreeSimpleAscii_Type()
)
mscFriProvisionalFreeSimpleAscii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleAscii.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleDashed_Type(DashedHexString):
    """Custom type mscFriProvisionalFreeSimpleDashed based on DashedHexString"""
    defaultHexValue = "00112233445566778899aabbccddeeff"

    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalFreeSimpleDashed_Type.__name__ = "DashedHexString"
_MscFriProvisionalFreeSimpleDashed_Object = MibTableColumn
mscFriProvisionalFreeSimpleDashed = _MscFriProvisionalFreeSimpleDashed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 14),
    _MscFriProvisionalFreeSimpleDashed_Type()
)
mscFriProvisionalFreeSimpleDashed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleDashed.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleExtended_Type(ExtendedAsciiString):
    """Custom type mscFriProvisionalFreeSimpleExtended based on ExtendedAsciiString"""
    defaultHexValue = "61626300006465665555676869"

    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalFreeSimpleExtended_Type.__name__ = "ExtendedAsciiString"
_MscFriProvisionalFreeSimpleExtended_Object = MibTableColumn
mscFriProvisionalFreeSimpleExtended = _MscFriProvisionalFreeSimpleExtended_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 15),
    _MscFriProvisionalFreeSimpleExtended_Type()
)
mscFriProvisionalFreeSimpleExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleExtended.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleBcd_Type(DigitString):
    """Custom type mscFriProvisionalFreeSimpleBcd based on DigitString"""
    defaultHexValue = "31323334"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_MscFriProvisionalFreeSimpleBcd_Type.__name__ = "DigitString"
_MscFriProvisionalFreeSimpleBcd_Object = MibTableColumn
mscFriProvisionalFreeSimpleBcd = _MscFriProvisionalFreeSimpleBcd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 16),
    _MscFriProvisionalFreeSimpleBcd_Type()
)
mscFriProvisionalFreeSimpleBcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleBcd.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleSequence_Type(IntegerSequence):
    """Custom type mscFriProvisionalFreeSimpleSequence based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )


_MscFriProvisionalFreeSimpleSequence_Type.__name__ = "IntegerSequence"
_MscFriProvisionalFreeSimpleSequence_Object = MibTableColumn
mscFriProvisionalFreeSimpleSequence = _MscFriProvisionalFreeSimpleSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 17),
    _MscFriProvisionalFreeSimpleSequence_Type()
)
mscFriProvisionalFreeSimpleSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleSequence.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleSigned_Type(Integer32):
    """Custom type mscFriProvisionalFreeSimpleSigned based on Integer32"""
    defaultValue = -11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MscFriProvisionalFreeSimpleSigned_Type.__name__ = "Integer32"
_MscFriProvisionalFreeSimpleSigned_Object = MibTableColumn
mscFriProvisionalFreeSimpleSigned = _MscFriProvisionalFreeSimpleSigned_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 18),
    _MscFriProvisionalFreeSimpleSigned_Type()
)
mscFriProvisionalFreeSimpleSigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleSigned.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleFixed_Type(FixedPoint2):
    """Custom type mscFriProvisionalFreeSimpleFixed based on FixedPoint2"""
    defaultValue = 122

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 233),
    )


_MscFriProvisionalFreeSimpleFixed_Type.__name__ = "FixedPoint2"
_MscFriProvisionalFreeSimpleFixed_Object = MibTableColumn
mscFriProvisionalFreeSimpleFixed = _MscFriProvisionalFreeSimpleFixed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 19),
    _MscFriProvisionalFreeSimpleFixed_Type()
)
mscFriProvisionalFreeSimpleFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleFixed.setStatus("mandatory")
_MscFriProvisionalFreeSimpleObjId_Type = IntegerSequence
_MscFriProvisionalFreeSimpleObjId_Object = MibTableColumn
mscFriProvisionalFreeSimpleObjId = _MscFriProvisionalFreeSimpleObjId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 20),
    _MscFriProvisionalFreeSimpleObjId_Type()
)
mscFriProvisionalFreeSimpleObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleObjId.setStatus("mandatory")
_MscFriProvisionalFreeSimpleComponent_Type = RowPointer
_MscFriProvisionalFreeSimpleComponent_Object = MibTableColumn
mscFriProvisionalFreeSimpleComponent = _MscFriProvisionalFreeSimpleComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 21),
    _MscFriProvisionalFreeSimpleComponent_Type()
)
mscFriProvisionalFreeSimpleComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleComponent.setStatus("mandatory")


class _MscFriProvisionalFreeSimpleHex_Type(HexString):
    """Custom type mscFriProvisionalFreeSimpleHex based on HexString"""
    defaultHexValue = "00112233445566778899aaBBcCDdeeFF313233"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 100),
    )


_MscFriProvisionalFreeSimpleHex_Type.__name__ = "HexString"
_MscFriProvisionalFreeSimpleHex_Object = MibTableColumn
mscFriProvisionalFreeSimpleHex = _MscFriProvisionalFreeSimpleHex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 22),
    _MscFriProvisionalFreeSimpleHex_Type()
)
mscFriProvisionalFreeSimpleHex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriProvisionalFreeSimpleHex.setStatus("mandatory")


class _MscFriEscapeCheckAttribute_Type(Unsigned32):
    """Custom type mscFriEscapeCheckAttribute based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriEscapeCheckAttribute_Type.__name__ = "Unsigned32"
_MscFriEscapeCheckAttribute_Object = MibTableColumn
mscFriEscapeCheckAttribute = _MscFriEscapeCheckAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 23),
    _MscFriEscapeCheckAttribute_Type()
)
mscFriEscapeCheckAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriEscapeCheckAttribute.setStatus("mandatory")


class _MscFriEscapeDefaultsComponent_Type(Unsigned32):
    """Custom type mscFriEscapeDefaultsComponent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriEscapeDefaultsComponent_Type.__name__ = "Unsigned32"
_MscFriEscapeDefaultsComponent_Object = MibTableColumn
mscFriEscapeDefaultsComponent = _MscFriEscapeDefaultsComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 24),
    _MscFriEscapeDefaultsComponent_Type()
)
mscFriEscapeDefaultsComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriEscapeDefaultsComponent.setStatus("mandatory")


class _MscFriEscapeDefaultsGroup_Type(Unsigned32):
    """Custom type mscFriEscapeDefaultsGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriEscapeDefaultsGroup_Type.__name__ = "Unsigned32"
_MscFriEscapeDefaultsGroup_Object = MibTableColumn
mscFriEscapeDefaultsGroup = _MscFriEscapeDefaultsGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 25),
    _MscFriEscapeDefaultsGroup_Type()
)
mscFriEscapeDefaultsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriEscapeDefaultsGroup.setStatus("mandatory")


class _MscFriEscapeSet_Type(AsciiString):
    """Custom type mscFriEscapeSet based on AsciiString"""
    defaultHexValue = "70617373776f7264"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_MscFriEscapeSet_Type.__name__ = "AsciiString"
_MscFriEscapeSet_Object = MibTableColumn
mscFriEscapeSet = _MscFriEscapeSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 26),
    _MscFriEscapeSet_Type()
)
mscFriEscapeSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriEscapeSet.setStatus("mandatory")


class _MscFriEscapeCopyComponent_Type(Unsigned32):
    """Custom type mscFriEscapeCopyComponent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFriEscapeCopyComponent_Type.__name__ = "Unsigned32"
_MscFriEscapeCopyComponent_Object = MibTableColumn
mscFriEscapeCopyComponent = _MscFriEscapeCopyComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 27),
    _MscFriEscapeCopyComponent_Type()
)
mscFriEscapeCopyComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriEscapeCopyComponent.setStatus("mandatory")


class _MscFriEscapeCopyGroup_Type(Unsigned32):
    """Custom type mscFriEscapeCopyGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFriEscapeCopyGroup_Type.__name__ = "Unsigned32"
_MscFriEscapeCopyGroup_Object = MibTableColumn
mscFriEscapeCopyGroup = _MscFriEscapeCopyGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 28),
    _MscFriEscapeCopyGroup_Type()
)
mscFriEscapeCopyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriEscapeCopyGroup.setStatus("mandatory")


class _MscFriEscapeCopyAttribute_Type(Unsigned32):
    """Custom type mscFriEscapeCopyAttribute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFriEscapeCopyAttribute_Type.__name__ = "Unsigned32"
_MscFriEscapeCopyAttribute_Object = MibTableColumn
mscFriEscapeCopyAttribute = _MscFriEscapeCopyAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 101, 1, 29),
    _MscFriEscapeCopyAttribute_Type()
)
mscFriEscapeCopyAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriEscapeCopyAttribute.setStatus("mandatory")
_MscFriStateTable_Object = MibTable
mscFriStateTable = _MscFriStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102)
)
if mibBuilder.loadTexts:
    mscFriStateTable.setStatus("mandatory")
_MscFriStateEntry_Object = MibTableRow
mscFriStateEntry = _MscFriStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1)
)
mscFriStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
)
if mibBuilder.loadTexts:
    mscFriStateEntry.setStatus("mandatory")


class _MscFriAdminState_Type(Integer32):
    """Custom type mscFriAdminState based on Integer32"""
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


_MscFriAdminState_Type.__name__ = "Integer32"
_MscFriAdminState_Object = MibTableColumn
mscFriAdminState = _MscFriAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 1),
    _MscFriAdminState_Type()
)
mscFriAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriAdminState.setStatus("mandatory")


class _MscFriOperationalState_Type(Integer32):
    """Custom type mscFriOperationalState based on Integer32"""
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


_MscFriOperationalState_Type.__name__ = "Integer32"
_MscFriOperationalState_Object = MibTableColumn
mscFriOperationalState = _MscFriOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 2),
    _MscFriOperationalState_Type()
)
mscFriOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriOperationalState.setStatus("mandatory")


class _MscFriUsageState_Type(Integer32):
    """Custom type mscFriUsageState based on Integer32"""
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


_MscFriUsageState_Type.__name__ = "Integer32"
_MscFriUsageState_Object = MibTableColumn
mscFriUsageState = _MscFriUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 3),
    _MscFriUsageState_Type()
)
mscFriUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriUsageState.setStatus("mandatory")


class _MscFriAvailabilityStatus_Type(OctetString):
    """Custom type mscFriAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFriAvailabilityStatus_Type.__name__ = "OctetString"
_MscFriAvailabilityStatus_Object = MibTableColumn
mscFriAvailabilityStatus = _MscFriAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 4),
    _MscFriAvailabilityStatus_Type()
)
mscFriAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriAvailabilityStatus.setStatus("mandatory")


class _MscFriProceduralStatus_Type(OctetString):
    """Custom type mscFriProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFriProceduralStatus_Type.__name__ = "OctetString"
_MscFriProceduralStatus_Object = MibTableColumn
mscFriProceduralStatus = _MscFriProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 5),
    _MscFriProceduralStatus_Type()
)
mscFriProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriProceduralStatus.setStatus("mandatory")


class _MscFriControlStatus_Type(OctetString):
    """Custom type mscFriControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFriControlStatus_Type.__name__ = "OctetString"
_MscFriControlStatus_Object = MibTableColumn
mscFriControlStatus = _MscFriControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 6),
    _MscFriControlStatus_Type()
)
mscFriControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriControlStatus.setStatus("mandatory")


class _MscFriAlarmStatus_Type(OctetString):
    """Custom type mscFriAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFriAlarmStatus_Type.__name__ = "OctetString"
_MscFriAlarmStatus_Object = MibTableColumn
mscFriAlarmStatus = _MscFriAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 7),
    _MscFriAlarmStatus_Type()
)
mscFriAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriAlarmStatus.setStatus("mandatory")


class _MscFriStandbyStatus_Type(Integer32):
    """Custom type mscFriStandbyStatus based on Integer32"""
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


_MscFriStandbyStatus_Type.__name__ = "Integer32"
_MscFriStandbyStatus_Object = MibTableColumn
mscFriStandbyStatus = _MscFriStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 8),
    _MscFriStandbyStatus_Type()
)
mscFriStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriStandbyStatus.setStatus("mandatory")


class _MscFriUnknownStatus_Type(Integer32):
    """Custom type mscFriUnknownStatus based on Integer32"""
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


_MscFriUnknownStatus_Type.__name__ = "Integer32"
_MscFriUnknownStatus_Object = MibTableColumn
mscFriUnknownStatus = _MscFriUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 102, 1, 9),
    _MscFriUnknownStatus_Type()
)
mscFriUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFriUnknownStatus.setStatus("mandatory")
_MscFriPfListAsciiTable_Object = MibTable
mscFriPfListAsciiTable = _MscFriPfListAsciiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1187)
)
if mibBuilder.loadTexts:
    mscFriPfListAsciiTable.setStatus("mandatory")
_MscFriPfListAsciiEntry_Object = MibTableRow
mscFriPfListAsciiEntry = _MscFriPfListAsciiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1187, 1)
)
mscFriPfListAsciiEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriPfListAsciiValue"),
)
if mibBuilder.loadTexts:
    mscFriPfListAsciiEntry.setStatus("mandatory")


class _MscFriPfListAsciiValue_Type(AsciiString):
    """Custom type mscFriPfListAsciiValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_MscFriPfListAsciiValue_Type.__name__ = "AsciiString"
_MscFriPfListAsciiValue_Object = MibTableColumn
mscFriPfListAsciiValue = _MscFriPfListAsciiValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1187, 1, 1),
    _MscFriPfListAsciiValue_Type()
)
mscFriPfListAsciiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriPfListAsciiValue.setStatus("mandatory")
_MscFriPfListAsciiRowStatus_Type = RowStatus
_MscFriPfListAsciiRowStatus_Object = MibTableColumn
mscFriPfListAsciiRowStatus = _MscFriPfListAsciiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1187, 1, 2),
    _MscFriPfListAsciiRowStatus_Type()
)
mscFriPfListAsciiRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriPfListAsciiRowStatus.setStatus("mandatory")
_MscFriPfListUnsignedTable_Object = MibTable
mscFriPfListUnsignedTable = _MscFriPfListUnsignedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1188)
)
if mibBuilder.loadTexts:
    mscFriPfListUnsignedTable.setStatus("mandatory")
_MscFriPfListUnsignedEntry_Object = MibTableRow
mscFriPfListUnsignedEntry = _MscFriPfListUnsignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1188, 1)
)
mscFriPfListUnsignedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriPfListUnsignedValue"),
)
if mibBuilder.loadTexts:
    mscFriPfListUnsignedEntry.setStatus("mandatory")


class _MscFriPfListUnsignedValue_Type(Integer32):
    """Custom type mscFriPfListUnsignedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFriPfListUnsignedValue_Type.__name__ = "Integer32"
_MscFriPfListUnsignedValue_Object = MibTableColumn
mscFriPfListUnsignedValue = _MscFriPfListUnsignedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1188, 1, 1),
    _MscFriPfListUnsignedValue_Type()
)
mscFriPfListUnsignedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriPfListUnsignedValue.setStatus("mandatory")
_MscFriPfListUnsignedRowStatus_Type = RowStatus
_MscFriPfListUnsignedRowStatus_Object = MibTableColumn
mscFriPfListUnsignedRowStatus = _MscFriPfListUnsignedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1188, 1, 2),
    _MscFriPfListUnsignedRowStatus_Type()
)
mscFriPfListUnsignedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriPfListUnsignedRowStatus.setStatus("mandatory")
_MscFriPfListFixedTable_Object = MibTable
mscFriPfListFixedTable = _MscFriPfListFixedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1189)
)
if mibBuilder.loadTexts:
    mscFriPfListFixedTable.setStatus("mandatory")
_MscFriPfListFixedEntry_Object = MibTableRow
mscFriPfListFixedEntry = _MscFriPfListFixedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1189, 1)
)
mscFriPfListFixedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriPfListFixedValue"),
)
if mibBuilder.loadTexts:
    mscFriPfListFixedEntry.setStatus("mandatory")


class _MscFriPfListFixedValue_Type(Integer32):
    """Custom type mscFriPfListFixedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2559),
    )


_MscFriPfListFixedValue_Type.__name__ = "Integer32"
_MscFriPfListFixedValue_Object = MibTableColumn
mscFriPfListFixedValue = _MscFriPfListFixedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1189, 1, 1),
    _MscFriPfListFixedValue_Type()
)
mscFriPfListFixedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriPfListFixedValue.setStatus("mandatory")
_MscFriPfListFixedRowStatus_Type = RowStatus
_MscFriPfListFixedRowStatus_Object = MibTableColumn
mscFriPfListFixedRowStatus = _MscFriPfListFixedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1189, 1, 2),
    _MscFriPfListFixedRowStatus_Type()
)
mscFriPfListFixedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriPfListFixedRowStatus.setStatus("mandatory")
_MscFriPfListSignedTable_Object = MibTable
mscFriPfListSignedTable = _MscFriPfListSignedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1190)
)
if mibBuilder.loadTexts:
    mscFriPfListSignedTable.setStatus("mandatory")
_MscFriPfListSignedEntry_Object = MibTableRow
mscFriPfListSignedEntry = _MscFriPfListSignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1190, 1)
)
mscFriPfListSignedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriPfListSignedValue"),
)
if mibBuilder.loadTexts:
    mscFriPfListSignedEntry.setStatus("mandatory")


class _MscFriPfListSignedValue_Type(Integer32):
    """Custom type mscFriPfListSignedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 255),
    )


_MscFriPfListSignedValue_Type.__name__ = "Integer32"
_MscFriPfListSignedValue_Object = MibTableColumn
mscFriPfListSignedValue = _MscFriPfListSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1190, 1, 1),
    _MscFriPfListSignedValue_Type()
)
mscFriPfListSignedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriPfListSignedValue.setStatus("mandatory")
_MscFriPfListSignedRowStatus_Type = RowStatus
_MscFriPfListSignedRowStatus_Object = MibTableColumn
mscFriPfListSignedRowStatus = _MscFriPfListSignedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1190, 1, 2),
    _MscFriPfListSignedRowStatus_Type()
)
mscFriPfListSignedRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriPfListSignedRowStatus.setStatus("mandatory")
_MscFriOfListComponentTable_Object = MibTable
mscFriOfListComponentTable = _MscFriOfListComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1191)
)
if mibBuilder.loadTexts:
    mscFriOfListComponentTable.setStatus("mandatory")
_MscFriOfListComponentEntry_Object = MibTableRow
mscFriOfListComponentEntry = _MscFriOfListComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1191, 1)
)
mscFriOfListComponentEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriOfListComponentValue"),
)
if mibBuilder.loadTexts:
    mscFriOfListComponentEntry.setStatus("mandatory")
_MscFriOfListComponentValue_Type = RowPointer
_MscFriOfListComponentValue_Object = MibTableColumn
mscFriOfListComponentValue = _MscFriOfListComponentValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1191, 1, 1),
    _MscFriOfListComponentValue_Type()
)
mscFriOfListComponentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOfListComponentValue.setStatus("mandatory")
_MscFriOfListComponentRowStatus_Type = RowStatus
_MscFriOfListComponentRowStatus_Object = MibTableColumn
mscFriOfListComponentRowStatus = _MscFriOfListComponentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1191, 1, 2),
    _MscFriOfListComponentRowStatus_Type()
)
mscFriOfListComponentRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriOfListComponentRowStatus.setStatus("mandatory")
_MscFriOfListEnumerationTable_Object = MibTable
mscFriOfListEnumerationTable = _MscFriOfListEnumerationTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1192)
)
if mibBuilder.loadTexts:
    mscFriOfListEnumerationTable.setStatus("mandatory")
_MscFriOfListEnumerationEntry_Object = MibTableRow
mscFriOfListEnumerationEntry = _MscFriOfListEnumerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1192, 1)
)
mscFriOfListEnumerationEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriIndex"),
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscFriOfListEnumerationValue"),
)
if mibBuilder.loadTexts:
    mscFriOfListEnumerationEntry.setStatus("mandatory")


class _MscFriOfListEnumerationValue_Type(Integer32):
    """Custom type mscFriOfListEnumerationValue based on Integer32"""
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


_MscFriOfListEnumerationValue_Type.__name__ = "Integer32"
_MscFriOfListEnumerationValue_Object = MibTableColumn
mscFriOfListEnumerationValue = _MscFriOfListEnumerationValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1192, 1, 1),
    _MscFriOfListEnumerationValue_Type()
)
mscFriOfListEnumerationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFriOfListEnumerationValue.setStatus("mandatory")
_MscFriOfListEnumerationRowStatus_Type = RowStatus
_MscFriOfListEnumerationRowStatus_Object = MibTableColumn
mscFriOfListEnumerationRowStatus = _MscFriOfListEnumerationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5001, 1192, 1, 2),
    _MscFriOfListEnumerationRowStatus_Type()
)
mscFriOfListEnumerationRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFriOfListEnumerationRowStatus.setStatus("mandatory")
_MscRegistered_ObjectIdentity = ObjectIdentity
mscRegistered = _MscRegistered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004)
)
_MscRegisteredRowStatusTable_Object = MibTable
mscRegisteredRowStatusTable = _MscRegisteredRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 1)
)
if mibBuilder.loadTexts:
    mscRegisteredRowStatusTable.setStatus("mandatory")
_MscRegisteredRowStatusEntry_Object = MibTableRow
mscRegisteredRowStatusEntry = _MscRegisteredRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 1, 1)
)
mscRegisteredRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscRegisteredIndex"),
)
if mibBuilder.loadTexts:
    mscRegisteredRowStatusEntry.setStatus("mandatory")
_MscRegisteredRowStatus_Type = RowStatus
_MscRegisteredRowStatus_Object = MibTableColumn
mscRegisteredRowStatus = _MscRegisteredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 1, 1, 1),
    _MscRegisteredRowStatus_Type()
)
mscRegisteredRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRegisteredRowStatus.setStatus("mandatory")
_MscRegisteredComponentName_Type = DisplayString
_MscRegisteredComponentName_Object = MibTableColumn
mscRegisteredComponentName = _MscRegisteredComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 1, 1, 2),
    _MscRegisteredComponentName_Type()
)
mscRegisteredComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRegisteredComponentName.setStatus("mandatory")
_MscRegisteredStorageType_Type = StorageType
_MscRegisteredStorageType_Object = MibTableColumn
mscRegisteredStorageType = _MscRegisteredStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 1, 1, 4),
    _MscRegisteredStorageType_Type()
)
mscRegisteredStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRegisteredStorageType.setStatus("mandatory")


class _MscRegisteredIndex_Type(Integer32):
    """Custom type mscRegisteredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscRegisteredIndex_Type.__name__ = "Integer32"
_MscRegisteredIndex_Object = MibTableColumn
mscRegisteredIndex = _MscRegisteredIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 1, 1, 10),
    _MscRegisteredIndex_Type()
)
mscRegisteredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRegisteredIndex.setStatus("mandatory")
_MscRegisteredDataTable_Object = MibTable
mscRegisteredDataTable = _MscRegisteredDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 10)
)
if mibBuilder.loadTexts:
    mscRegisteredDataTable.setStatus("mandatory")
_MscRegisteredDataEntry_Object = MibTableRow
mscRegisteredDataEntry = _MscRegisteredDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 10, 1)
)
mscRegisteredDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-CasTestMIB", "mscRegisteredIndex"),
)
if mibBuilder.loadTexts:
    mscRegisteredDataEntry.setStatus("mandatory")


class _MscRegisteredAttribute_Type(Unsigned32):
    """Custom type mscRegisteredAttribute based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRegisteredAttribute_Type.__name__ = "Unsigned32"
_MscRegisteredAttribute_Object = MibTableColumn
mscRegisteredAttribute = _MscRegisteredAttribute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5004, 10, 1, 1),
    _MscRegisteredAttribute_Type()
)
mscRegisteredAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRegisteredAttribute.setStatus("mandatory")
_CasTestMIB_ObjectIdentity = ObjectIdentity
casTestMIB = _CasTestMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103)
)
_CasTestGroup_ObjectIdentity = ObjectIdentity
casTestGroup = _CasTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 1)
)
_CasTestGroupCA_ObjectIdentity = ObjectIdentity
casTestGroupCA = _CasTestGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 1, 1)
)
_CasTestGroupCA02_ObjectIdentity = ObjectIdentity
casTestGroupCA02 = _CasTestGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 1, 1, 3)
)
_CasTestGroupCA02A_ObjectIdentity = ObjectIdentity
casTestGroupCA02A = _CasTestGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 1, 1, 3, 2)
)
_CasTestCapabilities_ObjectIdentity = ObjectIdentity
casTestCapabilities = _CasTestCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 3)
)
_CasTestCapabilitiesCA_ObjectIdentity = ObjectIdentity
casTestCapabilitiesCA = _CasTestCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 3, 1)
)
_CasTestCapabilitiesCA02_ObjectIdentity = ObjectIdentity
casTestCapabilitiesCA02 = _CasTestCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 3, 1, 3)
)
_CasTestCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
casTestCapabilitiesCA02A = _CasTestCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 103, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-CasTestMIB",
    **{"mscExample": mscExample,
       "mscExampleRowStatusTable": mscExampleRowStatusTable,
       "mscExampleRowStatusEntry": mscExampleRowStatusEntry,
       "mscExampleRowStatus": mscExampleRowStatus,
       "mscExampleComponentName": mscExampleComponentName,
       "mscExampleStorageType": mscExampleStorageType,
       "mscExampleIndex": mscExampleIndex,
       "mscExampleDecimal": mscExampleDecimal,
       "mscExampleDecimalRowStatusTable": mscExampleDecimalRowStatusTable,
       "mscExampleDecimalRowStatusEntry": mscExampleDecimalRowStatusEntry,
       "mscExampleDecimalRowStatus": mscExampleDecimalRowStatus,
       "mscExampleDecimalComponentName": mscExampleDecimalComponentName,
       "mscExampleDecimalStorageType": mscExampleDecimalStorageType,
       "mscExampleDecimalIndex": mscExampleDecimalIndex,
       "mscExampleDecimalOperationalTable": mscExampleDecimalOperationalTable,
       "mscExampleDecimalOperationalEntry": mscExampleDecimalOperationalEntry,
       "mscExampleDecimalOperStructInteger": mscExampleDecimalOperStructInteger,
       "mscExampleDecimalOperStructIntSet": mscExampleDecimalOperStructIntSet,
       "mscExampleDecimalOperFreeInteger": mscExampleDecimalOperFreeInteger,
       "mscExampleDecimalOperFreeIntSet": mscExampleDecimalOperFreeIntSet,
       "mscExampleDecimalOperFreeCounter32": mscExampleDecimalOperFreeCounter32,
       "mscExampleDecimalOperFreeGauge32": mscExampleDecimalOperFreeGauge32,
       "mscExampleDecimalOperFreeTimeInterval": mscExampleDecimalOperFreeTimeInterval,
       "mscExampleDecimalProvisionalTable": mscExampleDecimalProvisionalTable,
       "mscExampleDecimalProvisionalEntry": mscExampleDecimalProvisionalEntry,
       "mscExampleDecimalProvDecimalSub": mscExampleDecimalProvDecimalSub,
       "mscExampleDecimalProvStructInteger": mscExampleDecimalProvStructInteger,
       "mscExampleDecimalProvStructIntSet": mscExampleDecimalProvStructIntSet,
       "mscExampleDecimalProvFreeInteger": mscExampleDecimalProvFreeInteger,
       "mscExampleDecimalProvFreeInteger1": mscExampleDecimalProvFreeInteger1,
       "mscExampleDecimalProvFreeInteger2": mscExampleDecimalProvFreeInteger2,
       "mscExampleDecimalProvFreeIntSet": mscExampleDecimalProvFreeIntSet,
       "mscExampleDecimalProvFreeIntSet1": mscExampleDecimalProvFreeIntSet1,
       "mscExampleDecimalOsIntVectorTable": mscExampleDecimalOsIntVectorTable,
       "mscExampleDecimalOsIntVectorEntry": mscExampleDecimalOsIntVectorEntry,
       "mscExampleDecimalOsIntVectorIndex": mscExampleDecimalOsIntVectorIndex,
       "mscExampleDecimalOsIntVectorValue": mscExampleDecimalOsIntVectorValue,
       "mscExampleDecimalOsIntArrayTable": mscExampleDecimalOsIntArrayTable,
       "mscExampleDecimalOsIntArrayEntry": mscExampleDecimalOsIntArrayEntry,
       "mscExampleDecimalOsIntArrayRowIndex": mscExampleDecimalOsIntArrayRowIndex,
       "mscExampleDecimalOsIntArrayColumnIndex": mscExampleDecimalOsIntArrayColumnIndex,
       "mscExampleDecimalOsIntArrayValue": mscExampleDecimalOsIntArrayValue,
       "mscExampleDecimalOfIntVectorTable": mscExampleDecimalOfIntVectorTable,
       "mscExampleDecimalOfIntVectorEntry": mscExampleDecimalOfIntVectorEntry,
       "mscExampleDecimalOfIntVectorIndex": mscExampleDecimalOfIntVectorIndex,
       "mscExampleDecimalOfIntVectorValue": mscExampleDecimalOfIntVectorValue,
       "mscExampleDecimalOfIntArrayTable": mscExampleDecimalOfIntArrayTable,
       "mscExampleDecimalOfIntArrayEntry": mscExampleDecimalOfIntArrayEntry,
       "mscExampleDecimalOfIntArrayRowIndex": mscExampleDecimalOfIntArrayRowIndex,
       "mscExampleDecimalOfIntArrayColumnIndex": mscExampleDecimalOfIntArrayColumnIndex,
       "mscExampleDecimalOfIntArrayValue": mscExampleDecimalOfIntArrayValue,
       "mscExampleDecimalOfIntReplicatedTable": mscExampleDecimalOfIntReplicatedTable,
       "mscExampleDecimalOfIntReplicatedEntry": mscExampleDecimalOfIntReplicatedEntry,
       "mscExampleDecimalOfIntReplicatedIndex": mscExampleDecimalOfIntReplicatedIndex,
       "mscExampleDecimalOfIntReplicatedValue": mscExampleDecimalOfIntReplicatedValue,
       "mscExampleDecimalOfIntReplicatedRowStatus": mscExampleDecimalOfIntReplicatedRowStatus,
       "mscExampleDecimalOfIntListTable": mscExampleDecimalOfIntListTable,
       "mscExampleDecimalOfIntListEntry": mscExampleDecimalOfIntListEntry,
       "mscExampleDecimalOfIntListValue": mscExampleDecimalOfIntListValue,
       "mscExampleDecimalOfIntListRowStatus": mscExampleDecimalOfIntListRowStatus,
       "mscExampleDecimalPsIntVectorTable": mscExampleDecimalPsIntVectorTable,
       "mscExampleDecimalPsIntVectorEntry": mscExampleDecimalPsIntVectorEntry,
       "mscExampleDecimalPsIntVectorIndex": mscExampleDecimalPsIntVectorIndex,
       "mscExampleDecimalPsIntVectorValue": mscExampleDecimalPsIntVectorValue,
       "mscExampleDecimalPsIntArrayTable": mscExampleDecimalPsIntArrayTable,
       "mscExampleDecimalPsIntArrayEntry": mscExampleDecimalPsIntArrayEntry,
       "mscExampleDecimalPsIntArrayRowIndex": mscExampleDecimalPsIntArrayRowIndex,
       "mscExampleDecimalPsIntArrayColumnIndex": mscExampleDecimalPsIntArrayColumnIndex,
       "mscExampleDecimalPsIntArrayValue": mscExampleDecimalPsIntArrayValue,
       "mscExampleDecimalPfIntVectorTable": mscExampleDecimalPfIntVectorTable,
       "mscExampleDecimalPfIntVectorEntry": mscExampleDecimalPfIntVectorEntry,
       "mscExampleDecimalPfIntVectorIndex": mscExampleDecimalPfIntVectorIndex,
       "mscExampleDecimalPfIntVectorValue": mscExampleDecimalPfIntVectorValue,
       "mscExampleDecimalPfIntVector1Table": mscExampleDecimalPfIntVector1Table,
       "mscExampleDecimalPfIntVector1Entry": mscExampleDecimalPfIntVector1Entry,
       "mscExampleDecimalPfIntVector1Index": mscExampleDecimalPfIntVector1Index,
       "mscExampleDecimalPfIntVector1Value": mscExampleDecimalPfIntVector1Value,
       "mscExampleDecimalPfIntArrayTable": mscExampleDecimalPfIntArrayTable,
       "mscExampleDecimalPfIntArrayEntry": mscExampleDecimalPfIntArrayEntry,
       "mscExampleDecimalPfIntArrayRowIndex": mscExampleDecimalPfIntArrayRowIndex,
       "mscExampleDecimalPfIntArrayColumnIndex": mscExampleDecimalPfIntArrayColumnIndex,
       "mscExampleDecimalPfIntArrayValue": mscExampleDecimalPfIntArrayValue,
       "mscExampleDecimalPfIntArray1Table": mscExampleDecimalPfIntArray1Table,
       "mscExampleDecimalPfIntArray1Entry": mscExampleDecimalPfIntArray1Entry,
       "mscExampleDecimalPfIntArray1RowIndex": mscExampleDecimalPfIntArray1RowIndex,
       "mscExampleDecimalPfIntArray1ColumnIndex": mscExampleDecimalPfIntArray1ColumnIndex,
       "mscExampleDecimalPfIntArray1Value": mscExampleDecimalPfIntArray1Value,
       "mscExampleDecimalPfIntReplicatedTable": mscExampleDecimalPfIntReplicatedTable,
       "mscExampleDecimalPfIntReplicatedEntry": mscExampleDecimalPfIntReplicatedEntry,
       "mscExampleDecimalPfIntReplicatedIndex": mscExampleDecimalPfIntReplicatedIndex,
       "mscExampleDecimalPfIntReplicatedValue": mscExampleDecimalPfIntReplicatedValue,
       "mscExampleDecimalPfIntReplicatedRowStatus": mscExampleDecimalPfIntReplicatedRowStatus,
       "mscExampleDecimalPfIntReplicated1Table": mscExampleDecimalPfIntReplicated1Table,
       "mscExampleDecimalPfIntReplicated1Entry": mscExampleDecimalPfIntReplicated1Entry,
       "mscExampleDecimalPfIntReplicated1Index": mscExampleDecimalPfIntReplicated1Index,
       "mscExampleDecimalPfIntReplicated1Value": mscExampleDecimalPfIntReplicated1Value,
       "mscExampleDecimalPfIntReplicated1RowStatus": mscExampleDecimalPfIntReplicated1RowStatus,
       "mscExampleDecimalPfIntListTable": mscExampleDecimalPfIntListTable,
       "mscExampleDecimalPfIntListEntry": mscExampleDecimalPfIntListEntry,
       "mscExampleDecimalPfIntListValue": mscExampleDecimalPfIntListValue,
       "mscExampleDecimalPfIntListRowStatus": mscExampleDecimalPfIntListRowStatus,
       "mscExampleDecimalPfIntList1Table": mscExampleDecimalPfIntList1Table,
       "mscExampleDecimalPfIntList1Entry": mscExampleDecimalPfIntList1Entry,
       "mscExampleDecimalPfIntList1Value": mscExampleDecimalPfIntList1Value,
       "mscExampleDecimalPfIntList1RowStatus": mscExampleDecimalPfIntList1RowStatus,
       "mscExampleHex": mscExampleHex,
       "mscExampleHexRowStatusTable": mscExampleHexRowStatusTable,
       "mscExampleHexRowStatusEntry": mscExampleHexRowStatusEntry,
       "mscExampleHexRowStatus": mscExampleHexRowStatus,
       "mscExampleHexComponentName": mscExampleHexComponentName,
       "mscExampleHexStorageType": mscExampleHexStorageType,
       "mscExampleHexIndex": mscExampleHexIndex,
       "mscExampleHexOperationalTable": mscExampleHexOperationalTable,
       "mscExampleHexOperationalEntry": mscExampleHexOperationalEntry,
       "mscExampleHexOperStructHex": mscExampleHexOperStructHex,
       "mscExampleHexOperFreeHex": mscExampleHexOperFreeHex,
       "mscExampleHexProvisionalTable": mscExampleHexProvisionalTable,
       "mscExampleHexProvisionalEntry": mscExampleHexProvisionalEntry,
       "mscExampleHexProvEnumSub": mscExampleHexProvEnumSub,
       "mscExampleHexProvStructHex": mscExampleHexProvStructHex,
       "mscExampleHexProvFreeHex": mscExampleHexProvFreeHex,
       "mscExampleHexProvFreeHex1": mscExampleHexProvFreeHex1,
       "mscExampleHexOsHexVectorTable": mscExampleHexOsHexVectorTable,
       "mscExampleHexOsHexVectorEntry": mscExampleHexOsHexVectorEntry,
       "mscExampleHexOsHexVectorIndex": mscExampleHexOsHexVectorIndex,
       "mscExampleHexOsHexVectorValue": mscExampleHexOsHexVectorValue,
       "mscExampleHexOsHexArrayTable": mscExampleHexOsHexArrayTable,
       "mscExampleHexOsHexArrayEntry": mscExampleHexOsHexArrayEntry,
       "mscExampleHexOsHexArrayRowIndex": mscExampleHexOsHexArrayRowIndex,
       "mscExampleHexOsHexArrayColumnIndex": mscExampleHexOsHexArrayColumnIndex,
       "mscExampleHexOsHexArrayValue": mscExampleHexOsHexArrayValue,
       "mscExampleHexOfHexVectorTable": mscExampleHexOfHexVectorTable,
       "mscExampleHexOfHexVectorEntry": mscExampleHexOfHexVectorEntry,
       "mscExampleHexOfHexVectorIndex": mscExampleHexOfHexVectorIndex,
       "mscExampleHexOfHexVectorValue": mscExampleHexOfHexVectorValue,
       "mscExampleHexOfHexArrayTable": mscExampleHexOfHexArrayTable,
       "mscExampleHexOfHexArrayEntry": mscExampleHexOfHexArrayEntry,
       "mscExampleHexOfHexArrayRowIndex": mscExampleHexOfHexArrayRowIndex,
       "mscExampleHexOfHexArrayColumnIndex": mscExampleHexOfHexArrayColumnIndex,
       "mscExampleHexOfHexArrayValue": mscExampleHexOfHexArrayValue,
       "mscExampleHexOfHexReplicatedTable": mscExampleHexOfHexReplicatedTable,
       "mscExampleHexOfHexReplicatedEntry": mscExampleHexOfHexReplicatedEntry,
       "mscExampleHexOfHexReplicatedIndex": mscExampleHexOfHexReplicatedIndex,
       "mscExampleHexOfHexReplicatedValue": mscExampleHexOfHexReplicatedValue,
       "mscExampleHexOfHexReplicatedRowStatus": mscExampleHexOfHexReplicatedRowStatus,
       "mscExampleHexOfHexListTable": mscExampleHexOfHexListTable,
       "mscExampleHexOfHexListEntry": mscExampleHexOfHexListEntry,
       "mscExampleHexOfHexListValue": mscExampleHexOfHexListValue,
       "mscExampleHexOfHexListRowStatus": mscExampleHexOfHexListRowStatus,
       "mscExampleHexProvStructHexVectorTable": mscExampleHexProvStructHexVectorTable,
       "mscExampleHexProvStructHexVectorEntry": mscExampleHexProvStructHexVectorEntry,
       "mscExampleHexProvStructHexVectorIndex": mscExampleHexProvStructHexVectorIndex,
       "mscExampleHexProvStructHexVectorValue": mscExampleHexProvStructHexVectorValue,
       "mscExampleHexProvStructHexArrayTable": mscExampleHexProvStructHexArrayTable,
       "mscExampleHexProvStructHexArrayEntry": mscExampleHexProvStructHexArrayEntry,
       "mscExampleHexProvStructHexArrayRowIndex": mscExampleHexProvStructHexArrayRowIndex,
       "mscExampleHexProvStructHexArrayColumnIndex": mscExampleHexProvStructHexArrayColumnIndex,
       "mscExampleHexProvStructHexArrayValue": mscExampleHexProvStructHexArrayValue,
       "mscExampleHexProvFreeHexVectorTable": mscExampleHexProvFreeHexVectorTable,
       "mscExampleHexProvFreeHexVectorEntry": mscExampleHexProvFreeHexVectorEntry,
       "mscExampleHexProvFreeHexVectorIndex": mscExampleHexProvFreeHexVectorIndex,
       "mscExampleHexProvFreeHexVectorValue": mscExampleHexProvFreeHexVectorValue,
       "mscExampleHexProvFreeHexVector1Table": mscExampleHexProvFreeHexVector1Table,
       "mscExampleHexProvFreeHexVector1Entry": mscExampleHexProvFreeHexVector1Entry,
       "mscExampleHexProvFreeHexVector1Index": mscExampleHexProvFreeHexVector1Index,
       "mscExampleHexProvFreeHexVector1Value": mscExampleHexProvFreeHexVector1Value,
       "mscExampleHexProvFreeHexVector2Table": mscExampleHexProvFreeHexVector2Table,
       "mscExampleHexProvFreeHexVector2Entry": mscExampleHexProvFreeHexVector2Entry,
       "mscExampleHexProvFreeHexVector2Index": mscExampleHexProvFreeHexVector2Index,
       "mscExampleHexProvFreeHexVector2Value": mscExampleHexProvFreeHexVector2Value,
       "mscExampleHexProvFreeHexArrayTable": mscExampleHexProvFreeHexArrayTable,
       "mscExampleHexProvFreeHexArrayEntry": mscExampleHexProvFreeHexArrayEntry,
       "mscExampleHexProvFreeHexArrayRowIndex": mscExampleHexProvFreeHexArrayRowIndex,
       "mscExampleHexProvFreeHexArrayColumnIndex": mscExampleHexProvFreeHexArrayColumnIndex,
       "mscExampleHexProvFreeHexArrayValue": mscExampleHexProvFreeHexArrayValue,
       "mscExampleHexProvFreeHexArray1Table": mscExampleHexProvFreeHexArray1Table,
       "mscExampleHexProvFreeHexArray1Entry": mscExampleHexProvFreeHexArray1Entry,
       "mscExampleHexProvFreeHexArray1RowIndex": mscExampleHexProvFreeHexArray1RowIndex,
       "mscExampleHexProvFreeHexArray1ColumnIndex": mscExampleHexProvFreeHexArray1ColumnIndex,
       "mscExampleHexProvFreeHexArray1Value": mscExampleHexProvFreeHexArray1Value,
       "mscExampleHexProvFreeHexArray2Table": mscExampleHexProvFreeHexArray2Table,
       "mscExampleHexProvFreeHexArray2Entry": mscExampleHexProvFreeHexArray2Entry,
       "mscExampleHexProvFreeHexArray2RowIndex": mscExampleHexProvFreeHexArray2RowIndex,
       "mscExampleHexProvFreeHexArray2ColumnIndex": mscExampleHexProvFreeHexArray2ColumnIndex,
       "mscExampleHexProvFreeHexArray2Value": mscExampleHexProvFreeHexArray2Value,
       "mscExampleHexProvFreeHexReplicatedTable": mscExampleHexProvFreeHexReplicatedTable,
       "mscExampleHexProvFreeHexReplicatedEntry": mscExampleHexProvFreeHexReplicatedEntry,
       "mscExampleHexProvFreeHexReplicatedIndex": mscExampleHexProvFreeHexReplicatedIndex,
       "mscExampleHexProvFreeHexReplicatedValue": mscExampleHexProvFreeHexReplicatedValue,
       "mscExampleHexProvFreeHexReplicatedRowStatus": mscExampleHexProvFreeHexReplicatedRowStatus,
       "mscExampleHexProvFreeHexReplicated1Table": mscExampleHexProvFreeHexReplicated1Table,
       "mscExampleHexProvFreeHexReplicated1Entry": mscExampleHexProvFreeHexReplicated1Entry,
       "mscExampleHexProvFreeHexReplicated1Index": mscExampleHexProvFreeHexReplicated1Index,
       "mscExampleHexProvFreeHexReplicated1Value": mscExampleHexProvFreeHexReplicated1Value,
       "mscExampleHexProvFreeHexReplicated1RowStatus": mscExampleHexProvFreeHexReplicated1RowStatus,
       "mscExampleHexProvFreeHexListTable": mscExampleHexProvFreeHexListTable,
       "mscExampleHexProvFreeHexListEntry": mscExampleHexProvFreeHexListEntry,
       "mscExampleHexProvFreeHexListValue": mscExampleHexProvFreeHexListValue,
       "mscExampleHexProvFreeHexListRowStatus": mscExampleHexProvFreeHexListRowStatus,
       "mscExampleHexProvFreeHexList1Table": mscExampleHexProvFreeHexList1Table,
       "mscExampleHexProvFreeHexList1Entry": mscExampleHexProvFreeHexList1Entry,
       "mscExampleHexProvFreeHexList1Value": mscExampleHexProvFreeHexList1Value,
       "mscExampleHexProvFreeHexList1RowStatus": mscExampleHexProvFreeHexList1RowStatus,
       "mscExampleIpAddress": mscExampleIpAddress,
       "mscExampleIpAddressRowStatusTable": mscExampleIpAddressRowStatusTable,
       "mscExampleIpAddressRowStatusEntry": mscExampleIpAddressRowStatusEntry,
       "mscExampleIpAddressRowStatus": mscExampleIpAddressRowStatus,
       "mscExampleIpAddressComponentName": mscExampleIpAddressComponentName,
       "mscExampleIpAddressStorageType": mscExampleIpAddressStorageType,
       "mscExampleIpAddressIndex": mscExampleIpAddressIndex,
       "mscExampleIpAddressOperationalTable": mscExampleIpAddressOperationalTable,
       "mscExampleIpAddressOperationalEntry": mscExampleIpAddressOperationalEntry,
       "mscExampleIpAddressOperStructIpAddress": mscExampleIpAddressOperStructIpAddress,
       "mscExampleIpAddressOperFreeIpAddress": mscExampleIpAddressOperFreeIpAddress,
       "mscExampleIpAddressProvisionalTable": mscExampleIpAddressProvisionalTable,
       "mscExampleIpAddressProvisionalEntry": mscExampleIpAddressProvisionalEntry,
       "mscExampleIpAddressProvEnumSub": mscExampleIpAddressProvEnumSub,
       "mscExampleIpAddressProvStructIpAddress": mscExampleIpAddressProvStructIpAddress,
       "mscExampleIpAddressProvFreeIpAddress": mscExampleIpAddressProvFreeIpAddress,
       "mscExampleIpAddressProvFreeIpAddress1": mscExampleIpAddressProvFreeIpAddress1,
       "mscExampleIpAddressOperStructIpAddressVectorTable": mscExampleIpAddressOperStructIpAddressVectorTable,
       "mscExampleIpAddressOperStructIpAddressVectorEntry": mscExampleIpAddressOperStructIpAddressVectorEntry,
       "mscExampleIpAddressOperStructIpAddressVectorIndex": mscExampleIpAddressOperStructIpAddressVectorIndex,
       "mscExampleIpAddressOperStructIpAddressVectorValue": mscExampleIpAddressOperStructIpAddressVectorValue,
       "mscExampleIpAddressOperStructIpAddressArrayTable": mscExampleIpAddressOperStructIpAddressArrayTable,
       "mscExampleIpAddressOperStructIpAddressArrayEntry": mscExampleIpAddressOperStructIpAddressArrayEntry,
       "mscExampleIpAddressOperStructIpAddressArrayRowIndex": mscExampleIpAddressOperStructIpAddressArrayRowIndex,
       "mscExampleIpAddressOperStructIpAddressArrayColumnIndex": mscExampleIpAddressOperStructIpAddressArrayColumnIndex,
       "mscExampleIpAddressOperStructIpAddressArrayValue": mscExampleIpAddressOperStructIpAddressArrayValue,
       "mscExampleIpAddressOperFreeIpAddressVectorTable": mscExampleIpAddressOperFreeIpAddressVectorTable,
       "mscExampleIpAddressOperFreeIpAddressVectorEntry": mscExampleIpAddressOperFreeIpAddressVectorEntry,
       "mscExampleIpAddressOperFreeIpAddressVectorIndex": mscExampleIpAddressOperFreeIpAddressVectorIndex,
       "mscExampleIpAddressOperFreeIpAddressVectorValue": mscExampleIpAddressOperFreeIpAddressVectorValue,
       "mscExampleIpAddressOperFreeIpAddressArrayTable": mscExampleIpAddressOperFreeIpAddressArrayTable,
       "mscExampleIpAddressOperFreeIpAddressArrayEntry": mscExampleIpAddressOperFreeIpAddressArrayEntry,
       "mscExampleIpAddressOperFreeIpAddressArrayRowIndex": mscExampleIpAddressOperFreeIpAddressArrayRowIndex,
       "mscExampleIpAddressOperFreeIpAddressArrayColumnIndex": mscExampleIpAddressOperFreeIpAddressArrayColumnIndex,
       "mscExampleIpAddressOperFreeIpAddressArrayValue": mscExampleIpAddressOperFreeIpAddressArrayValue,
       "mscExampleIpAddressOperFreeIpAddressReplicatedTable": mscExampleIpAddressOperFreeIpAddressReplicatedTable,
       "mscExampleIpAddressOperFreeIpAddressReplicatedEntry": mscExampleIpAddressOperFreeIpAddressReplicatedEntry,
       "mscExampleIpAddressOperFreeIpAddressReplicatedIndex": mscExampleIpAddressOperFreeIpAddressReplicatedIndex,
       "mscExampleIpAddressOperFreeIpAddressReplicatedValue": mscExampleIpAddressOperFreeIpAddressReplicatedValue,
       "mscExampleIpAddressOperFreeIpAddressReplicatedRowStatus": mscExampleIpAddressOperFreeIpAddressReplicatedRowStatus,
       "mscExampleIpAddressOperFreeIpAddressListTable": mscExampleIpAddressOperFreeIpAddressListTable,
       "mscExampleIpAddressOperFreeIpAddressListEntry": mscExampleIpAddressOperFreeIpAddressListEntry,
       "mscExampleIpAddressOperFreeIpAddressListValue": mscExampleIpAddressOperFreeIpAddressListValue,
       "mscExampleIpAddressOperFreeIpAddressListRowStatus": mscExampleIpAddressOperFreeIpAddressListRowStatus,
       "mscExampleIpAddressProvStructIpAddressVectorTable": mscExampleIpAddressProvStructIpAddressVectorTable,
       "mscExampleIpAddressProvStructIpAddressVectorEntry": mscExampleIpAddressProvStructIpAddressVectorEntry,
       "mscExampleIpAddressProvStructIpAddressVectorIndex": mscExampleIpAddressProvStructIpAddressVectorIndex,
       "mscExampleIpAddressProvStructIpAddressVectorValue": mscExampleIpAddressProvStructIpAddressVectorValue,
       "mscExampleIpAddressProvStructIpAddressArrayTable": mscExampleIpAddressProvStructIpAddressArrayTable,
       "mscExampleIpAddressProvStructIpAddressArrayEntry": mscExampleIpAddressProvStructIpAddressArrayEntry,
       "mscExampleIpAddressProvStructIpAddressArrayRowIndex": mscExampleIpAddressProvStructIpAddressArrayRowIndex,
       "mscExampleIpAddressProvStructIpAddressArrayColumnIndex": mscExampleIpAddressProvStructIpAddressArrayColumnIndex,
       "mscExampleIpAddressProvStructIpAddressArrayValue": mscExampleIpAddressProvStructIpAddressArrayValue,
       "mscExampleIpAddressProvFreeIpAddressVectorTable": mscExampleIpAddressProvFreeIpAddressVectorTable,
       "mscExampleIpAddressProvFreeIpAddressVectorEntry": mscExampleIpAddressProvFreeIpAddressVectorEntry,
       "mscExampleIpAddressProvFreeIpAddressVectorIndex": mscExampleIpAddressProvFreeIpAddressVectorIndex,
       "mscExampleIpAddressProvFreeIpAddressVectorValue": mscExampleIpAddressProvFreeIpAddressVectorValue,
       "mscExampleIpAddressProvFreeIpAddressVector1Table": mscExampleIpAddressProvFreeIpAddressVector1Table,
       "mscExampleIpAddressProvFreeIpAddressVector1Entry": mscExampleIpAddressProvFreeIpAddressVector1Entry,
       "mscExampleIpAddressProvFreeIpAddressVector1Index": mscExampleIpAddressProvFreeIpAddressVector1Index,
       "mscExampleIpAddressProvFreeIpAddressVector1Value": mscExampleIpAddressProvFreeIpAddressVector1Value,
       "mscExampleIpAddressProvFreeIpAddressArrayTable": mscExampleIpAddressProvFreeIpAddressArrayTable,
       "mscExampleIpAddressProvFreeIpAddressArrayEntry": mscExampleIpAddressProvFreeIpAddressArrayEntry,
       "mscExampleIpAddressProvFreeIpAddressArrayRowIndex": mscExampleIpAddressProvFreeIpAddressArrayRowIndex,
       "mscExampleIpAddressProvFreeIpAddressArrayColumnIndex": mscExampleIpAddressProvFreeIpAddressArrayColumnIndex,
       "mscExampleIpAddressProvFreeIpAddressArrayValue": mscExampleIpAddressProvFreeIpAddressArrayValue,
       "mscExampleIpAddressProvFreeIpAddressArray1Table": mscExampleIpAddressProvFreeIpAddressArray1Table,
       "mscExampleIpAddressProvFreeIpAddressArray1Entry": mscExampleIpAddressProvFreeIpAddressArray1Entry,
       "mscExampleIpAddressProvFreeIpAddressArray1RowIndex": mscExampleIpAddressProvFreeIpAddressArray1RowIndex,
       "mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex": mscExampleIpAddressProvFreeIpAddressArray1ColumnIndex,
       "mscExampleIpAddressProvFreeIpAddressArray1Value": mscExampleIpAddressProvFreeIpAddressArray1Value,
       "mscExampleIpAddressProvFreeIpAddressReplicatedTable": mscExampleIpAddressProvFreeIpAddressReplicatedTable,
       "mscExampleIpAddressProvFreeIpAddressReplicatedEntry": mscExampleIpAddressProvFreeIpAddressReplicatedEntry,
       "mscExampleIpAddressProvFreeIpAddressReplicatedIndex": mscExampleIpAddressProvFreeIpAddressReplicatedIndex,
       "mscExampleIpAddressProvFreeIpAddressReplicatedValue": mscExampleIpAddressProvFreeIpAddressReplicatedValue,
       "mscExampleIpAddressProvFreeIpAddressReplicatedRowStatus": mscExampleIpAddressProvFreeIpAddressReplicatedRowStatus,
       "mscExampleIpAddressProvFreeIpAddressListTable": mscExampleIpAddressProvFreeIpAddressListTable,
       "mscExampleIpAddressProvFreeIpAddressListEntry": mscExampleIpAddressProvFreeIpAddressListEntry,
       "mscExampleIpAddressProvFreeIpAddressListValue": mscExampleIpAddressProvFreeIpAddressListValue,
       "mscExampleIpAddressProvFreeIpAddressListRowStatus": mscExampleIpAddressProvFreeIpAddressListRowStatus,
       "mscExampleIpAddressProvFreeIpAddressList1Table": mscExampleIpAddressProvFreeIpAddressList1Table,
       "mscExampleIpAddressProvFreeIpAddressList1Entry": mscExampleIpAddressProvFreeIpAddressList1Entry,
       "mscExampleIpAddressProvFreeIpAddressList1Value": mscExampleIpAddressProvFreeIpAddressList1Value,
       "mscExampleIpAddressProvFreeIpAddressList1RowStatus": mscExampleIpAddressProvFreeIpAddressList1RowStatus,
       "mscExampleString": mscExampleString,
       "mscExampleStringRowStatusTable": mscExampleStringRowStatusTable,
       "mscExampleStringRowStatusEntry": mscExampleStringRowStatusEntry,
       "mscExampleStringRowStatus": mscExampleStringRowStatus,
       "mscExampleStringComponentName": mscExampleStringComponentName,
       "mscExampleStringStorageType": mscExampleStringStorageType,
       "mscExampleStringIndex": mscExampleStringIndex,
       "mscExampleStringOperationalTable": mscExampleStringOperationalTable,
       "mscExampleStringOperationalEntry": mscExampleStringOperationalEntry,
       "mscExampleStringOperStructAsciiOnly": mscExampleStringOperStructAsciiOnly,
       "mscExampleStringOperStructHexOnly": mscExampleStringOperStructHexOnly,
       "mscExampleStringOperFreeAsciiOnly": mscExampleStringOperFreeAsciiOnly,
       "mscExampleStringOperFreeHexOnly": mscExampleStringOperFreeHexOnly,
       "mscExampleStringProvisionalTable": mscExampleStringProvisionalTable,
       "mscExampleStringProvisionalEntry": mscExampleStringProvisionalEntry,
       "mscExampleStringProvStringSub": mscExampleStringProvStringSub,
       "mscExampleStringProvStructAsciiOnly": mscExampleStringProvStructAsciiOnly,
       "mscExampleStringProvStructHexOnly": mscExampleStringProvStructHexOnly,
       "mscExampleStringProvFreeAsciiOnly": mscExampleStringProvFreeAsciiOnly,
       "mscExampleStringProvFreeAsciiOnly1": mscExampleStringProvFreeAsciiOnly1,
       "mscExampleStringProvFreeHexOnly": mscExampleStringProvFreeHexOnly,
       "mscExampleStringProvFreeHexOnly1": mscExampleStringProvFreeHexOnly1,
       "mscExampleStringOperStructStrVectorTable": mscExampleStringOperStructStrVectorTable,
       "mscExampleStringOperStructStrVectorEntry": mscExampleStringOperStructStrVectorEntry,
       "mscExampleStringOperStructStrVectorIndex": mscExampleStringOperStructStrVectorIndex,
       "mscExampleStringOperStructStrVectorValue": mscExampleStringOperStructStrVectorValue,
       "mscExampleStringOperStructStrArrayTable": mscExampleStringOperStructStrArrayTable,
       "mscExampleStringOperStructStrArrayEntry": mscExampleStringOperStructStrArrayEntry,
       "mscExampleStringOperStructStrArrayRowIndex": mscExampleStringOperStructStrArrayRowIndex,
       "mscExampleStringOperStructStrArrayColumnIndex": mscExampleStringOperStructStrArrayColumnIndex,
       "mscExampleStringOperStructStrArrayValue": mscExampleStringOperStructStrArrayValue,
       "mscExampleStringOperFreeStrVectorTable": mscExampleStringOperFreeStrVectorTable,
       "mscExampleStringOperFreeStrVectorEntry": mscExampleStringOperFreeStrVectorEntry,
       "mscExampleStringOperFreeStrVectorIndex": mscExampleStringOperFreeStrVectorIndex,
       "mscExampleStringOperFreeStrVectorValue": mscExampleStringOperFreeStrVectorValue,
       "mscExampleStringOperFreeStrArrayTable": mscExampleStringOperFreeStrArrayTable,
       "mscExampleStringOperFreeStrArrayEntry": mscExampleStringOperFreeStrArrayEntry,
       "mscExampleStringOperFreeStrArrayRowIndex": mscExampleStringOperFreeStrArrayRowIndex,
       "mscExampleStringOperFreeStrArrayColumnIndex": mscExampleStringOperFreeStrArrayColumnIndex,
       "mscExampleStringOperFreeStrArrayValue": mscExampleStringOperFreeStrArrayValue,
       "mscExampleStringOperFreeStrReplicatedTable": mscExampleStringOperFreeStrReplicatedTable,
       "mscExampleStringOperFreeStrReplicatedEntry": mscExampleStringOperFreeStrReplicatedEntry,
       "mscExampleStringOperFreeStrReplicatedIndex": mscExampleStringOperFreeStrReplicatedIndex,
       "mscExampleStringOperFreeStrReplicatedValue": mscExampleStringOperFreeStrReplicatedValue,
       "mscExampleStringOperFreeStrReplicatedRowStatus": mscExampleStringOperFreeStrReplicatedRowStatus,
       "mscExampleStringOperFreeStrListTable": mscExampleStringOperFreeStrListTable,
       "mscExampleStringOperFreeStrListEntry": mscExampleStringOperFreeStrListEntry,
       "mscExampleStringOperFreeStrListValue": mscExampleStringOperFreeStrListValue,
       "mscExampleStringOperFreeStrListRowStatus": mscExampleStringOperFreeStrListRowStatus,
       "mscExampleStringProvStructStrVectorTable": mscExampleStringProvStructStrVectorTable,
       "mscExampleStringProvStructStrVectorEntry": mscExampleStringProvStructStrVectorEntry,
       "mscExampleStringProvStructStrVectorIndex": mscExampleStringProvStructStrVectorIndex,
       "mscExampleStringProvStructStrVectorValue": mscExampleStringProvStructStrVectorValue,
       "mscExampleStringProvStructStrArrayTable": mscExampleStringProvStructStrArrayTable,
       "mscExampleStringProvStructStrArrayEntry": mscExampleStringProvStructStrArrayEntry,
       "mscExampleStringProvStructStrArrayRowIndex": mscExampleStringProvStructStrArrayRowIndex,
       "mscExampleStringProvStructStrArrayColumnIndex": mscExampleStringProvStructStrArrayColumnIndex,
       "mscExampleStringProvStructStrArrayValue": mscExampleStringProvStructStrArrayValue,
       "mscExampleStringProvFreeStrVectorTable": mscExampleStringProvFreeStrVectorTable,
       "mscExampleStringProvFreeStrVectorEntry": mscExampleStringProvFreeStrVectorEntry,
       "mscExampleStringProvFreeStrVectorIndex": mscExampleStringProvFreeStrVectorIndex,
       "mscExampleStringProvFreeStrVectorValue": mscExampleStringProvFreeStrVectorValue,
       "mscExampleStringProvFreeStrVector1Table": mscExampleStringProvFreeStrVector1Table,
       "mscExampleStringProvFreeStrVector1Entry": mscExampleStringProvFreeStrVector1Entry,
       "mscExampleStringProvFreeStrVector1Index": mscExampleStringProvFreeStrVector1Index,
       "mscExampleStringProvFreeStrVector1Value": mscExampleStringProvFreeStrVector1Value,
       "mscExampleStringProvFreeStrArrayTable": mscExampleStringProvFreeStrArrayTable,
       "mscExampleStringProvFreeStrArrayEntry": mscExampleStringProvFreeStrArrayEntry,
       "mscExampleStringProvFreeStrArrayRowIndex": mscExampleStringProvFreeStrArrayRowIndex,
       "mscExampleStringProvFreeStrArrayColumnIndex": mscExampleStringProvFreeStrArrayColumnIndex,
       "mscExampleStringProvFreeStrArrayValue": mscExampleStringProvFreeStrArrayValue,
       "mscExampleStringProvFreeStrArray1Table": mscExampleStringProvFreeStrArray1Table,
       "mscExampleStringProvFreeStrArray1Entry": mscExampleStringProvFreeStrArray1Entry,
       "mscExampleStringProvFreeStrArray1RowIndex": mscExampleStringProvFreeStrArray1RowIndex,
       "mscExampleStringProvFreeStrArray1ColumnIndex": mscExampleStringProvFreeStrArray1ColumnIndex,
       "mscExampleStringProvFreeStrArray1Value": mscExampleStringProvFreeStrArray1Value,
       "mscExampleStringProvFreeStrReplicatedTable": mscExampleStringProvFreeStrReplicatedTable,
       "mscExampleStringProvFreeStrReplicatedEntry": mscExampleStringProvFreeStrReplicatedEntry,
       "mscExampleStringProvFreeStrReplicatedIndex": mscExampleStringProvFreeStrReplicatedIndex,
       "mscExampleStringProvFreeStrReplicatedValue": mscExampleStringProvFreeStrReplicatedValue,
       "mscExampleStringProvFreeStrReplicatedRowStatus": mscExampleStringProvFreeStrReplicatedRowStatus,
       "mscExampleStringProvFreeStrListTable": mscExampleStringProvFreeStrListTable,
       "mscExampleStringProvFreeStrListEntry": mscExampleStringProvFreeStrListEntry,
       "mscExampleStringProvFreeStrListValue": mscExampleStringProvFreeStrListValue,
       "mscExampleStringProvFreeStrListRowStatus": mscExampleStringProvFreeStrListRowStatus,
       "mscExampleStringProvFreeStrList1Table": mscExampleStringProvFreeStrList1Table,
       "mscExampleStringProvFreeStrList1Entry": mscExampleStringProvFreeStrList1Entry,
       "mscExampleStringProvFreeStrList1Value": mscExampleStringProvFreeStrList1Value,
       "mscExampleStringProvFreeStrList1RowStatus": mscExampleStringProvFreeStrList1RowStatus,
       "mscExampleFixedPt": mscExampleFixedPt,
       "mscExampleFixedPtRowStatusTable": mscExampleFixedPtRowStatusTable,
       "mscExampleFixedPtRowStatusEntry": mscExampleFixedPtRowStatusEntry,
       "mscExampleFixedPtRowStatus": mscExampleFixedPtRowStatus,
       "mscExampleFixedPtComponentName": mscExampleFixedPtComponentName,
       "mscExampleFixedPtStorageType": mscExampleFixedPtStorageType,
       "mscExampleFixedPtIndex": mscExampleFixedPtIndex,
       "mscExampleFixedPtOperationalTable": mscExampleFixedPtOperationalTable,
       "mscExampleFixedPtOperationalEntry": mscExampleFixedPtOperationalEntry,
       "mscExampleFixedPtOperStructFixedPt": mscExampleFixedPtOperStructFixedPt,
       "mscExampleFixedPtOperFreeFixedPt": mscExampleFixedPtOperFreeFixedPt,
       "mscExampleFixedPtOperFreeFixedPtSet": mscExampleFixedPtOperFreeFixedPtSet,
       "mscExampleFixedPtProvisionalTable": mscExampleFixedPtProvisionalTable,
       "mscExampleFixedPtProvisionalEntry": mscExampleFixedPtProvisionalEntry,
       "mscExampleFixedPtProvFixedPtSubcomponent": mscExampleFixedPtProvFixedPtSubcomponent,
       "mscExampleFixedPtProvStructFixedPt": mscExampleFixedPtProvStructFixedPt,
       "mscExampleFixedPtProvStructFixedPtSet": mscExampleFixedPtProvStructFixedPtSet,
       "mscExampleFixedPtProvFreeFixedPt": mscExampleFixedPtProvFreeFixedPt,
       "mscExampleFixedPtProvFreeFixedPtSet": mscExampleFixedPtProvFreeFixedPtSet,
       "mscExampleFixedPtOperStructFixedPtVectorTable": mscExampleFixedPtOperStructFixedPtVectorTable,
       "mscExampleFixedPtOperStructFixedPtVectorEntry": mscExampleFixedPtOperStructFixedPtVectorEntry,
       "mscExampleFixedPtOperStructFixedPtVectorIndex": mscExampleFixedPtOperStructFixedPtVectorIndex,
       "mscExampleFixedPtOperStructFixedPtVectorValue": mscExampleFixedPtOperStructFixedPtVectorValue,
       "mscExampleFixedPtOperStructFixedPtArrayTable": mscExampleFixedPtOperStructFixedPtArrayTable,
       "mscExampleFixedPtOperStructFixedPtArrayEntry": mscExampleFixedPtOperStructFixedPtArrayEntry,
       "mscExampleFixedPtOperStructFixedPtArrayRowIndex": mscExampleFixedPtOperStructFixedPtArrayRowIndex,
       "mscExampleFixedPtOperStructFixedPtArrayColumnIndex": mscExampleFixedPtOperStructFixedPtArrayColumnIndex,
       "mscExampleFixedPtOperStructFixedPtArrayValue": mscExampleFixedPtOperStructFixedPtArrayValue,
       "mscExampleFixedPtOperFreeFixedPtVectorTable": mscExampleFixedPtOperFreeFixedPtVectorTable,
       "mscExampleFixedPtOperFreeFixedPtVectorEntry": mscExampleFixedPtOperFreeFixedPtVectorEntry,
       "mscExampleFixedPtOperFreeFixedPtVectorIndex": mscExampleFixedPtOperFreeFixedPtVectorIndex,
       "mscExampleFixedPtOperFreeFixedPtVectorValue": mscExampleFixedPtOperFreeFixedPtVectorValue,
       "mscExampleFixedPtOperFreeFixedPtArrayTable": mscExampleFixedPtOperFreeFixedPtArrayTable,
       "mscExampleFixedPtOperFreeFixedPtArrayEntry": mscExampleFixedPtOperFreeFixedPtArrayEntry,
       "mscExampleFixedPtOperFreeFixedPtArrayRowIndex": mscExampleFixedPtOperFreeFixedPtArrayRowIndex,
       "mscExampleFixedPtOperFreeFixedPtArrayColumnIndex": mscExampleFixedPtOperFreeFixedPtArrayColumnIndex,
       "mscExampleFixedPtOperFreeFixedPtArrayValue": mscExampleFixedPtOperFreeFixedPtArrayValue,
       "mscExampleFixedPtOperFreeFixedPtReplicatedTable": mscExampleFixedPtOperFreeFixedPtReplicatedTable,
       "mscExampleFixedPtOperFreeFixedPtReplicatedEntry": mscExampleFixedPtOperFreeFixedPtReplicatedEntry,
       "mscExampleFixedPtOperFreeFixedPtReplicatedIndex": mscExampleFixedPtOperFreeFixedPtReplicatedIndex,
       "mscExampleFixedPtOperFreeFixedPtReplicatedValue": mscExampleFixedPtOperFreeFixedPtReplicatedValue,
       "mscExampleFixedPtOperFreeFixedPtReplicatedRowStatus": mscExampleFixedPtOperFreeFixedPtReplicatedRowStatus,
       "mscExampleFixedPtOperFreeFixedPtListTable": mscExampleFixedPtOperFreeFixedPtListTable,
       "mscExampleFixedPtOperFreeFixedPtListEntry": mscExampleFixedPtOperFreeFixedPtListEntry,
       "mscExampleFixedPtOperFreeFixedPtListValue": mscExampleFixedPtOperFreeFixedPtListValue,
       "mscExampleFixedPtOperFreeFixedPtListRowStatus": mscExampleFixedPtOperFreeFixedPtListRowStatus,
       "mscExampleFixedPtProvStructFixedPtVectorTable": mscExampleFixedPtProvStructFixedPtVectorTable,
       "mscExampleFixedPtProvStructFixedPtVectorEntry": mscExampleFixedPtProvStructFixedPtVectorEntry,
       "mscExampleFixedPtProvStructFixedPtVectorIndex": mscExampleFixedPtProvStructFixedPtVectorIndex,
       "mscExampleFixedPtProvStructFixedPtVectorValue": mscExampleFixedPtProvStructFixedPtVectorValue,
       "mscExampleFixedPtProvStructFixedPtArrayTable": mscExampleFixedPtProvStructFixedPtArrayTable,
       "mscExampleFixedPtProvStructFixedPtArrayEntry": mscExampleFixedPtProvStructFixedPtArrayEntry,
       "mscExampleFixedPtProvStructFixedPtArrayRowIndex": mscExampleFixedPtProvStructFixedPtArrayRowIndex,
       "mscExampleFixedPtProvStructFixedPtArrayColumnIndex": mscExampleFixedPtProvStructFixedPtArrayColumnIndex,
       "mscExampleFixedPtProvStructFixedPtArrayValue": mscExampleFixedPtProvStructFixedPtArrayValue,
       "mscExampleFixedPtProvFreeFixedPtVectorTable": mscExampleFixedPtProvFreeFixedPtVectorTable,
       "mscExampleFixedPtProvFreeFixedPtVectorEntry": mscExampleFixedPtProvFreeFixedPtVectorEntry,
       "mscExampleFixedPtProvFreeFixedPtVectorIndex": mscExampleFixedPtProvFreeFixedPtVectorIndex,
       "mscExampleFixedPtProvFreeFixedPtVectorValue": mscExampleFixedPtProvFreeFixedPtVectorValue,
       "mscExampleFixedPtProvFreeFixedPtArrayTable": mscExampleFixedPtProvFreeFixedPtArrayTable,
       "mscExampleFixedPtProvFreeFixedPtArrayEntry": mscExampleFixedPtProvFreeFixedPtArrayEntry,
       "mscExampleFixedPtProvFreeFixedPtArrayRowIndex": mscExampleFixedPtProvFreeFixedPtArrayRowIndex,
       "mscExampleFixedPtProvFreeFixedPtArrayColumnIndex": mscExampleFixedPtProvFreeFixedPtArrayColumnIndex,
       "mscExampleFixedPtProvFreeFixedPtArrayValue": mscExampleFixedPtProvFreeFixedPtArrayValue,
       "mscExampleFixedPtProvFreeFixedPtReplicatedTable": mscExampleFixedPtProvFreeFixedPtReplicatedTable,
       "mscExampleFixedPtProvFreeFixedPtReplicatedEntry": mscExampleFixedPtProvFreeFixedPtReplicatedEntry,
       "mscExampleFixedPtProvFreeFixedPtReplicatedIndex": mscExampleFixedPtProvFreeFixedPtReplicatedIndex,
       "mscExampleFixedPtProvFreeFixedPtReplicatedValue": mscExampleFixedPtProvFreeFixedPtReplicatedValue,
       "mscExampleFixedPtProvFreeFixedPtReplicatedRowStatus": mscExampleFixedPtProvFreeFixedPtReplicatedRowStatus,
       "mscExampleFixedPtProvFreeFixedPtListTable": mscExampleFixedPtProvFreeFixedPtListTable,
       "mscExampleFixedPtProvFreeFixedPtListEntry": mscExampleFixedPtProvFreeFixedPtListEntry,
       "mscExampleFixedPtProvFreeFixedPtListValue": mscExampleFixedPtProvFreeFixedPtListValue,
       "mscExampleFixedPtProvFreeFixedPtListRowStatus": mscExampleFixedPtProvFreeFixedPtListRowStatus,
       "mscExampleDashed": mscExampleDashed,
       "mscExampleDashedRowStatusTable": mscExampleDashedRowStatusTable,
       "mscExampleDashedRowStatusEntry": mscExampleDashedRowStatusEntry,
       "mscExampleDashedRowStatus": mscExampleDashedRowStatus,
       "mscExampleDashedComponentName": mscExampleDashedComponentName,
       "mscExampleDashedStorageType": mscExampleDashedStorageType,
       "mscExampleDashedIndex": mscExampleDashedIndex,
       "mscExampleDashedOperationalTable": mscExampleDashedOperationalTable,
       "mscExampleDashedOperationalEntry": mscExampleDashedOperationalEntry,
       "mscExampleDashedOperStructDashed": mscExampleDashedOperStructDashed,
       "mscExampleDashedOperFreeDashed": mscExampleDashedOperFreeDashed,
       "mscExampleDashedProvisionalTable": mscExampleDashedProvisionalTable,
       "mscExampleDashedProvisionalEntry": mscExampleDashedProvisionalEntry,
       "mscExampleDashedProvStructDashed": mscExampleDashedProvStructDashed,
       "mscExampleDashedProvFreeDashed": mscExampleDashedProvFreeDashed,
       "mscExampleDashedOsDashedArrayTable": mscExampleDashedOsDashedArrayTable,
       "mscExampleDashedOsDashedArrayEntry": mscExampleDashedOsDashedArrayEntry,
       "mscExampleDashedOsDashedArrayRowIndex": mscExampleDashedOsDashedArrayRowIndex,
       "mscExampleDashedOsDashedArrayColumnIndex": mscExampleDashedOsDashedArrayColumnIndex,
       "mscExampleDashedOsDashedArrayValue": mscExampleDashedOsDashedArrayValue,
       "mscExampleDashedOsDashedVectorTable": mscExampleDashedOsDashedVectorTable,
       "mscExampleDashedOsDashedVectorEntry": mscExampleDashedOsDashedVectorEntry,
       "mscExampleDashedOsDashedVectorIndex": mscExampleDashedOsDashedVectorIndex,
       "mscExampleDashedOsDashedVectorValue": mscExampleDashedOsDashedVectorValue,
       "mscExampleDashedOfDashedListTable": mscExampleDashedOfDashedListTable,
       "mscExampleDashedOfDashedListEntry": mscExampleDashedOfDashedListEntry,
       "mscExampleDashedOfDashedListValue": mscExampleDashedOfDashedListValue,
       "mscExampleDashedOfDashedListRowStatus": mscExampleDashedOfDashedListRowStatus,
       "mscExampleDashedOfDashedReplicatedTable": mscExampleDashedOfDashedReplicatedTable,
       "mscExampleDashedOfDashedReplicatedEntry": mscExampleDashedOfDashedReplicatedEntry,
       "mscExampleDashedOfDashedReplicatedIndex": mscExampleDashedOfDashedReplicatedIndex,
       "mscExampleDashedOfDashedReplicatedValue": mscExampleDashedOfDashedReplicatedValue,
       "mscExampleDashedOfDashedReplicatedRowStatus": mscExampleDashedOfDashedReplicatedRowStatus,
       "mscExampleDashedOfDashedArrayTable": mscExampleDashedOfDashedArrayTable,
       "mscExampleDashedOfDashedArrayEntry": mscExampleDashedOfDashedArrayEntry,
       "mscExampleDashedOfDashedArrayRowIndex": mscExampleDashedOfDashedArrayRowIndex,
       "mscExampleDashedOfDashedArrayColumnIndex": mscExampleDashedOfDashedArrayColumnIndex,
       "mscExampleDashedOfDashedArrayValue": mscExampleDashedOfDashedArrayValue,
       "mscExampleDashedOfDashedVectorTable": mscExampleDashedOfDashedVectorTable,
       "mscExampleDashedOfDashedVectorEntry": mscExampleDashedOfDashedVectorEntry,
       "mscExampleDashedOfDashedVectorIndex": mscExampleDashedOfDashedVectorIndex,
       "mscExampleDashedOfDashedVectorValue": mscExampleDashedOfDashedVectorValue,
       "mscExampleDashedProvStructDashedArrayTable": mscExampleDashedProvStructDashedArrayTable,
       "mscExampleDashedProvStructDashedArrayEntry": mscExampleDashedProvStructDashedArrayEntry,
       "mscExampleDashedProvStructDashedArrayRowIndex": mscExampleDashedProvStructDashedArrayRowIndex,
       "mscExampleDashedProvStructDashedArrayColumnIndex": mscExampleDashedProvStructDashedArrayColumnIndex,
       "mscExampleDashedProvStructDashedArrayValue": mscExampleDashedProvStructDashedArrayValue,
       "mscExampleDashedProvStructDashedVectorTable": mscExampleDashedProvStructDashedVectorTable,
       "mscExampleDashedProvStructDashedVectorEntry": mscExampleDashedProvStructDashedVectorEntry,
       "mscExampleDashedProvStructDashedVectorIndex": mscExampleDashedProvStructDashedVectorIndex,
       "mscExampleDashedProvStructDashedVectorValue": mscExampleDashedProvStructDashedVectorValue,
       "mscExampleDashedProvFreeDashedListTable": mscExampleDashedProvFreeDashedListTable,
       "mscExampleDashedProvFreeDashedListEntry": mscExampleDashedProvFreeDashedListEntry,
       "mscExampleDashedProvFreeDashedListValue": mscExampleDashedProvFreeDashedListValue,
       "mscExampleDashedProvFreeDashedListRowStatus": mscExampleDashedProvFreeDashedListRowStatus,
       "mscExampleDashedProvFreeDashedReplicatedTable": mscExampleDashedProvFreeDashedReplicatedTable,
       "mscExampleDashedProvFreeDashedReplicatedEntry": mscExampleDashedProvFreeDashedReplicatedEntry,
       "mscExampleDashedProvFreeDashedReplicatedIndex": mscExampleDashedProvFreeDashedReplicatedIndex,
       "mscExampleDashedProvFreeDashedReplicatedValue": mscExampleDashedProvFreeDashedReplicatedValue,
       "mscExampleDashedProvFreeDashedReplicatedRowStatus": mscExampleDashedProvFreeDashedReplicatedRowStatus,
       "mscExampleDashedProvFreeDashedArrayTable": mscExampleDashedProvFreeDashedArrayTable,
       "mscExampleDashedProvFreeDashedArrayEntry": mscExampleDashedProvFreeDashedArrayEntry,
       "mscExampleDashedProvFreeDashedArrayRowIndex": mscExampleDashedProvFreeDashedArrayRowIndex,
       "mscExampleDashedProvFreeDashedArrayColumnIndex": mscExampleDashedProvFreeDashedArrayColumnIndex,
       "mscExampleDashedProvFreeDashedArrayValue": mscExampleDashedProvFreeDashedArrayValue,
       "mscExampleDashedProvFreeDashedVectorTable": mscExampleDashedProvFreeDashedVectorTable,
       "mscExampleDashedProvFreeDashedVectorEntry": mscExampleDashedProvFreeDashedVectorEntry,
       "mscExampleDashedProvFreeDashedVectorIndex": mscExampleDashedProvFreeDashedVectorIndex,
       "mscExampleDashedProvFreeDashedVectorValue": mscExampleDashedProvFreeDashedVectorValue,
       "mscExampleExtended": mscExampleExtended,
       "mscExampleExtendedRowStatusTable": mscExampleExtendedRowStatusTable,
       "mscExampleExtendedRowStatusEntry": mscExampleExtendedRowStatusEntry,
       "mscExampleExtendedRowStatus": mscExampleExtendedRowStatus,
       "mscExampleExtendedComponentName": mscExampleExtendedComponentName,
       "mscExampleExtendedStorageType": mscExampleExtendedStorageType,
       "mscExampleExtendedIndex": mscExampleExtendedIndex,
       "mscExampleExtendedOperationalTable": mscExampleExtendedOperationalTable,
       "mscExampleExtendedOperationalEntry": mscExampleExtendedOperationalEntry,
       "mscExampleExtendedOperStructExtended": mscExampleExtendedOperStructExtended,
       "mscExampleExtendedOperFreeExtended": mscExampleExtendedOperFreeExtended,
       "mscExampleExtendedProvisionalTable": mscExampleExtendedProvisionalTable,
       "mscExampleExtendedProvisionalEntry": mscExampleExtendedProvisionalEntry,
       "mscExampleExtendedProvEnumSub": mscExampleExtendedProvEnumSub,
       "mscExampleExtendedProvStructExtended": mscExampleExtendedProvStructExtended,
       "mscExampleExtendedProvFreeExtended": mscExampleExtendedProvFreeExtended,
       "mscExampleExtendedOperStructExtendedArrayTable": mscExampleExtendedOperStructExtendedArrayTable,
       "mscExampleExtendedOperStructExtendedArrayEntry": mscExampleExtendedOperStructExtendedArrayEntry,
       "mscExampleExtendedOperStructExtendedArrayRowIndex": mscExampleExtendedOperStructExtendedArrayRowIndex,
       "mscExampleExtendedOperStructExtendedArrayColumnIndex": mscExampleExtendedOperStructExtendedArrayColumnIndex,
       "mscExampleExtendedOperStructExtendedArrayValue": mscExampleExtendedOperStructExtendedArrayValue,
       "mscExampleExtendedOperStructExtendedVectorTable": mscExampleExtendedOperStructExtendedVectorTable,
       "mscExampleExtendedOperStructExtendedVectorEntry": mscExampleExtendedOperStructExtendedVectorEntry,
       "mscExampleExtendedOperStructExtendedVectorIndex": mscExampleExtendedOperStructExtendedVectorIndex,
       "mscExampleExtendedOperStructExtendedVectorValue": mscExampleExtendedOperStructExtendedVectorValue,
       "mscExampleExtendedOperFreeExtendedListTable": mscExampleExtendedOperFreeExtendedListTable,
       "mscExampleExtendedOperFreeExtendedListEntry": mscExampleExtendedOperFreeExtendedListEntry,
       "mscExampleExtendedOperFreeExtendedListValue": mscExampleExtendedOperFreeExtendedListValue,
       "mscExampleExtendedOperFreeExtendedListRowStatus": mscExampleExtendedOperFreeExtendedListRowStatus,
       "mscExampleExtendedOperFreeExtendedReplicatedTable": mscExampleExtendedOperFreeExtendedReplicatedTable,
       "mscExampleExtendedOperFreeExtendedReplicatedEntry": mscExampleExtendedOperFreeExtendedReplicatedEntry,
       "mscExampleExtendedOperFreeExtendedReplicatedIndex": mscExampleExtendedOperFreeExtendedReplicatedIndex,
       "mscExampleExtendedOperFreeExtendedReplicatedValue": mscExampleExtendedOperFreeExtendedReplicatedValue,
       "mscExampleExtendedOperFreeExtendedReplicatedRowStatus": mscExampleExtendedOperFreeExtendedReplicatedRowStatus,
       "mscExampleExtendedOperFreeExtendedArrayTable": mscExampleExtendedOperFreeExtendedArrayTable,
       "mscExampleExtendedOperFreeExtendedArrayEntry": mscExampleExtendedOperFreeExtendedArrayEntry,
       "mscExampleExtendedOperFreeExtendedArrayRowIndex": mscExampleExtendedOperFreeExtendedArrayRowIndex,
       "mscExampleExtendedOperFreeExtendedArrayColumnIndex": mscExampleExtendedOperFreeExtendedArrayColumnIndex,
       "mscExampleExtendedOperFreeExtendedArrayValue": mscExampleExtendedOperFreeExtendedArrayValue,
       "mscExampleExtendedOperFreeExtendedVectorTable": mscExampleExtendedOperFreeExtendedVectorTable,
       "mscExampleExtendedOperFreeExtendedVectorEntry": mscExampleExtendedOperFreeExtendedVectorEntry,
       "mscExampleExtendedOperFreeExtendedVectorIndex": mscExampleExtendedOperFreeExtendedVectorIndex,
       "mscExampleExtendedOperFreeExtendedVectorValue": mscExampleExtendedOperFreeExtendedVectorValue,
       "mscExampleExtendedProvStructExtendedArrayTable": mscExampleExtendedProvStructExtendedArrayTable,
       "mscExampleExtendedProvStructExtendedArrayEntry": mscExampleExtendedProvStructExtendedArrayEntry,
       "mscExampleExtendedProvStructExtendedArrayRowIndex": mscExampleExtendedProvStructExtendedArrayRowIndex,
       "mscExampleExtendedProvStructExtendedArrayColumnIndex": mscExampleExtendedProvStructExtendedArrayColumnIndex,
       "mscExampleExtendedProvStructExtendedArrayValue": mscExampleExtendedProvStructExtendedArrayValue,
       "mscExampleExtendedProvStructExtendedVectorTable": mscExampleExtendedProvStructExtendedVectorTable,
       "mscExampleExtendedProvStructExtendedVectorEntry": mscExampleExtendedProvStructExtendedVectorEntry,
       "mscExampleExtendedProvStructExtendedVectorIndex": mscExampleExtendedProvStructExtendedVectorIndex,
       "mscExampleExtendedProvStructExtendedVectorValue": mscExampleExtendedProvStructExtendedVectorValue,
       "mscExampleExtendedProvFreeExtendedListTable": mscExampleExtendedProvFreeExtendedListTable,
       "mscExampleExtendedProvFreeExtendedListEntry": mscExampleExtendedProvFreeExtendedListEntry,
       "mscExampleExtendedProvFreeExtendedListValue": mscExampleExtendedProvFreeExtendedListValue,
       "mscExampleExtendedProvFreeExtendedListRowStatus": mscExampleExtendedProvFreeExtendedListRowStatus,
       "mscExampleExtendedProvFreeExtendedReplicatedTable": mscExampleExtendedProvFreeExtendedReplicatedTable,
       "mscExampleExtendedProvFreeExtendedReplicatedEntry": mscExampleExtendedProvFreeExtendedReplicatedEntry,
       "mscExampleExtendedProvFreeExtendedReplicatedIndex": mscExampleExtendedProvFreeExtendedReplicatedIndex,
       "mscExampleExtendedProvFreeExtendedReplicatedValue": mscExampleExtendedProvFreeExtendedReplicatedValue,
       "mscExampleExtendedProvFreeExtendedReplicatedRowStatus": mscExampleExtendedProvFreeExtendedReplicatedRowStatus,
       "mscExampleExtendedProvFreeExtendedArrayTable": mscExampleExtendedProvFreeExtendedArrayTable,
       "mscExampleExtendedProvFreeExtendedArrayEntry": mscExampleExtendedProvFreeExtendedArrayEntry,
       "mscExampleExtendedProvFreeExtendedArrayRowIndex": mscExampleExtendedProvFreeExtendedArrayRowIndex,
       "mscExampleExtendedProvFreeExtendedArrayColumnIndex": mscExampleExtendedProvFreeExtendedArrayColumnIndex,
       "mscExampleExtendedProvFreeExtendedArrayValue": mscExampleExtendedProvFreeExtendedArrayValue,
       "mscExampleExtendedProvFreeExtendedVectorTable": mscExampleExtendedProvFreeExtendedVectorTable,
       "mscExampleExtendedProvFreeExtendedVectorEntry": mscExampleExtendedProvFreeExtendedVectorEntry,
       "mscExampleExtendedProvFreeExtendedVectorIndex": mscExampleExtendedProvFreeExtendedVectorIndex,
       "mscExampleExtendedProvFreeExtendedVectorValue": mscExampleExtendedProvFreeExtendedVectorValue,
       "mscExampleBcd": mscExampleBcd,
       "mscExampleBcdRowStatusTable": mscExampleBcdRowStatusTable,
       "mscExampleBcdRowStatusEntry": mscExampleBcdRowStatusEntry,
       "mscExampleBcdRowStatus": mscExampleBcdRowStatus,
       "mscExampleBcdComponentName": mscExampleBcdComponentName,
       "mscExampleBcdStorageType": mscExampleBcdStorageType,
       "mscExampleBcdIndex": mscExampleBcdIndex,
       "mscExampleBcdOperationalTable": mscExampleBcdOperationalTable,
       "mscExampleBcdOperationalEntry": mscExampleBcdOperationalEntry,
       "mscExampleBcdOperStructBcd": mscExampleBcdOperStructBcd,
       "mscExampleBcdOperFreeBcd": mscExampleBcdOperFreeBcd,
       "mscExampleBcdProvisionalTable": mscExampleBcdProvisionalTable,
       "mscExampleBcdProvisionalEntry": mscExampleBcdProvisionalEntry,
       "mscExampleBcdProvEnumSub": mscExampleBcdProvEnumSub,
       "mscExampleBcdProvStructBcd": mscExampleBcdProvStructBcd,
       "mscExampleBcdProvFreeBcd": mscExampleBcdProvFreeBcd,
       "mscExampleBcdProvFreeBcd1": mscExampleBcdProvFreeBcd1,
       "mscExampleBcdOperStructBcdVectorTable": mscExampleBcdOperStructBcdVectorTable,
       "mscExampleBcdOperStructBcdVectorEntry": mscExampleBcdOperStructBcdVectorEntry,
       "mscExampleBcdOperStructBcdVectorIndex": mscExampleBcdOperStructBcdVectorIndex,
       "mscExampleBcdOperStructBcdVectorValue": mscExampleBcdOperStructBcdVectorValue,
       "mscExampleBcdOperStructBcdArrayTable": mscExampleBcdOperStructBcdArrayTable,
       "mscExampleBcdOperStructBcdArrayEntry": mscExampleBcdOperStructBcdArrayEntry,
       "mscExampleBcdOperStructBcdArrayRowIndex": mscExampleBcdOperStructBcdArrayRowIndex,
       "mscExampleBcdOperStructBcdArrayColumnIndex": mscExampleBcdOperStructBcdArrayColumnIndex,
       "mscExampleBcdOperStructBcdArrayValue": mscExampleBcdOperStructBcdArrayValue,
       "mscExampleBcdOperFreeBcdVectorTable": mscExampleBcdOperFreeBcdVectorTable,
       "mscExampleBcdOperFreeBcdVectorEntry": mscExampleBcdOperFreeBcdVectorEntry,
       "mscExampleBcdOperFreeBcdVectorIndex": mscExampleBcdOperFreeBcdVectorIndex,
       "mscExampleBcdOperFreeBcdVectorValue": mscExampleBcdOperFreeBcdVectorValue,
       "mscExampleBcdOperFreeBcdArrayTable": mscExampleBcdOperFreeBcdArrayTable,
       "mscExampleBcdOperFreeBcdArrayEntry": mscExampleBcdOperFreeBcdArrayEntry,
       "mscExampleBcdOperFreeBcdArrayRowIndex": mscExampleBcdOperFreeBcdArrayRowIndex,
       "mscExampleBcdOperFreeBcdArrayColumnIndex": mscExampleBcdOperFreeBcdArrayColumnIndex,
       "mscExampleBcdOperFreeBcdArrayValue": mscExampleBcdOperFreeBcdArrayValue,
       "mscExampleBcdOperFreeBcdReplicatedTable": mscExampleBcdOperFreeBcdReplicatedTable,
       "mscExampleBcdOperFreeBcdReplicatedEntry": mscExampleBcdOperFreeBcdReplicatedEntry,
       "mscExampleBcdOperFreeBcdReplicatedIndex": mscExampleBcdOperFreeBcdReplicatedIndex,
       "mscExampleBcdOperFreeBcdReplicatedValue": mscExampleBcdOperFreeBcdReplicatedValue,
       "mscExampleBcdOperFreeBcdReplicatedRowStatus": mscExampleBcdOperFreeBcdReplicatedRowStatus,
       "mscExampleBcdOperFreeBcdListTable": mscExampleBcdOperFreeBcdListTable,
       "mscExampleBcdOperFreeBcdListEntry": mscExampleBcdOperFreeBcdListEntry,
       "mscExampleBcdOperFreeBcdListValue": mscExampleBcdOperFreeBcdListValue,
       "mscExampleBcdOperFreeBcdListRowStatus": mscExampleBcdOperFreeBcdListRowStatus,
       "mscExampleBcdProvStructBcdVectorTable": mscExampleBcdProvStructBcdVectorTable,
       "mscExampleBcdProvStructBcdVectorEntry": mscExampleBcdProvStructBcdVectorEntry,
       "mscExampleBcdProvStructBcdVectorIndex": mscExampleBcdProvStructBcdVectorIndex,
       "mscExampleBcdProvStructBcdVectorValue": mscExampleBcdProvStructBcdVectorValue,
       "mscExampleBcdProvStructBcdArrayTable": mscExampleBcdProvStructBcdArrayTable,
       "mscExampleBcdProvStructBcdArrayEntry": mscExampleBcdProvStructBcdArrayEntry,
       "mscExampleBcdProvStructBcdArrayRowIndex": mscExampleBcdProvStructBcdArrayRowIndex,
       "mscExampleBcdProvStructBcdArrayColumnIndex": mscExampleBcdProvStructBcdArrayColumnIndex,
       "mscExampleBcdProvStructBcdArrayValue": mscExampleBcdProvStructBcdArrayValue,
       "mscExampleBcdProvFreeBcdVectorTable": mscExampleBcdProvFreeBcdVectorTable,
       "mscExampleBcdProvFreeBcdVectorEntry": mscExampleBcdProvFreeBcdVectorEntry,
       "mscExampleBcdProvFreeBcdVectorIndex": mscExampleBcdProvFreeBcdVectorIndex,
       "mscExampleBcdProvFreeBcdVectorValue": mscExampleBcdProvFreeBcdVectorValue,
       "mscExampleBcdProvFreeBcdVector1Table": mscExampleBcdProvFreeBcdVector1Table,
       "mscExampleBcdProvFreeBcdVector1Entry": mscExampleBcdProvFreeBcdVector1Entry,
       "mscExampleBcdProvFreeBcdVector1Index": mscExampleBcdProvFreeBcdVector1Index,
       "mscExampleBcdProvFreeBcdVector1Value": mscExampleBcdProvFreeBcdVector1Value,
       "mscExampleBcdProvFreeBcdArrayTable": mscExampleBcdProvFreeBcdArrayTable,
       "mscExampleBcdProvFreeBcdArrayEntry": mscExampleBcdProvFreeBcdArrayEntry,
       "mscExampleBcdProvFreeBcdArrayRowIndex": mscExampleBcdProvFreeBcdArrayRowIndex,
       "mscExampleBcdProvFreeBcdArrayColumnIndex": mscExampleBcdProvFreeBcdArrayColumnIndex,
       "mscExampleBcdProvFreeBcdArrayValue": mscExampleBcdProvFreeBcdArrayValue,
       "mscExampleBcdProvFreeBcdArray1Table": mscExampleBcdProvFreeBcdArray1Table,
       "mscExampleBcdProvFreeBcdArray1Entry": mscExampleBcdProvFreeBcdArray1Entry,
       "mscExampleBcdProvFreeBcdArray1RowIndex": mscExampleBcdProvFreeBcdArray1RowIndex,
       "mscExampleBcdProvFreeBcdArray1ColumnIndex": mscExampleBcdProvFreeBcdArray1ColumnIndex,
       "mscExampleBcdProvFreeBcdArray1Value": mscExampleBcdProvFreeBcdArray1Value,
       "mscExampleBcdProvFreeBcdReplicatedTable": mscExampleBcdProvFreeBcdReplicatedTable,
       "mscExampleBcdProvFreeBcdReplicatedEntry": mscExampleBcdProvFreeBcdReplicatedEntry,
       "mscExampleBcdProvFreeBcdReplicatedIndex": mscExampleBcdProvFreeBcdReplicatedIndex,
       "mscExampleBcdProvFreeBcdReplicatedValue": mscExampleBcdProvFreeBcdReplicatedValue,
       "mscExampleBcdProvFreeBcdReplicatedRowStatus": mscExampleBcdProvFreeBcdReplicatedRowStatus,
       "mscExampleBcdProvFreeBcdReplicated1Table": mscExampleBcdProvFreeBcdReplicated1Table,
       "mscExampleBcdProvFreeBcdReplicated1Entry": mscExampleBcdProvFreeBcdReplicated1Entry,
       "mscExampleBcdProvFreeBcdReplicated1Index": mscExampleBcdProvFreeBcdReplicated1Index,
       "mscExampleBcdProvFreeBcdReplicated1Value": mscExampleBcdProvFreeBcdReplicated1Value,
       "mscExampleBcdProvFreeBcdReplicated1RowStatus": mscExampleBcdProvFreeBcdReplicated1RowStatus,
       "mscExampleBcdProvFreeBcdListTable": mscExampleBcdProvFreeBcdListTable,
       "mscExampleBcdProvFreeBcdListEntry": mscExampleBcdProvFreeBcdListEntry,
       "mscExampleBcdProvFreeBcdListValue": mscExampleBcdProvFreeBcdListValue,
       "mscExampleBcdProvFreeBcdListRowStatus": mscExampleBcdProvFreeBcdListRowStatus,
       "mscExampleBcdProvFreeBcdList1Table": mscExampleBcdProvFreeBcdList1Table,
       "mscExampleBcdProvFreeBcdList1Entry": mscExampleBcdProvFreeBcdList1Entry,
       "mscExampleBcdProvFreeBcdList1Value": mscExampleBcdProvFreeBcdList1Value,
       "mscExampleBcdProvFreeBcdList1RowStatus": mscExampleBcdProvFreeBcdList1RowStatus,
       "mscExampleWildBcd": mscExampleWildBcd,
       "mscExampleWildBcdRowStatusTable": mscExampleWildBcdRowStatusTable,
       "mscExampleWildBcdRowStatusEntry": mscExampleWildBcdRowStatusEntry,
       "mscExampleWildBcdRowStatus": mscExampleWildBcdRowStatus,
       "mscExampleWildBcdComponentName": mscExampleWildBcdComponentName,
       "mscExampleWildBcdStorageType": mscExampleWildBcdStorageType,
       "mscExampleWildBcdIndex": mscExampleWildBcdIndex,
       "mscExampleWildBcdOperationalTable": mscExampleWildBcdOperationalTable,
       "mscExampleWildBcdOperationalEntry": mscExampleWildBcdOperationalEntry,
       "mscExampleWildBcdOperStructWildBcd": mscExampleWildBcdOperStructWildBcd,
       "mscExampleWildBcdOperFreeWildBcd": mscExampleWildBcdOperFreeWildBcd,
       "mscExampleWildBcdProvisionalTable": mscExampleWildBcdProvisionalTable,
       "mscExampleWildBcdProvisionalEntry": mscExampleWildBcdProvisionalEntry,
       "mscExampleWildBcdProvStructWildBcd": mscExampleWildBcdProvStructWildBcd,
       "mscExampleWildBcdProvFreeWildBcd": mscExampleWildBcdProvFreeWildBcd,
       "mscExampleWildBcdOperStructWildBcdVectorTable": mscExampleWildBcdOperStructWildBcdVectorTable,
       "mscExampleWildBcdOperStructWildBcdVectorEntry": mscExampleWildBcdOperStructWildBcdVectorEntry,
       "mscExampleWildBcdOperStructWildBcdVectorIndex": mscExampleWildBcdOperStructWildBcdVectorIndex,
       "mscExampleWildBcdOperStructWildBcdVectorValue": mscExampleWildBcdOperStructWildBcdVectorValue,
       "mscExampleWildBcdOperStructWildBcdArrayTable": mscExampleWildBcdOperStructWildBcdArrayTable,
       "mscExampleWildBcdOperStructWildBcdArrayEntry": mscExampleWildBcdOperStructWildBcdArrayEntry,
       "mscExampleWildBcdOperStructWildBcdArrayRowIndex": mscExampleWildBcdOperStructWildBcdArrayRowIndex,
       "mscExampleWildBcdOperStructWildBcdArrayColumnIndex": mscExampleWildBcdOperStructWildBcdArrayColumnIndex,
       "mscExampleWildBcdOperStructWildBcdArrayValue": mscExampleWildBcdOperStructWildBcdArrayValue,
       "mscExampleWildBcdOperFreeWildBcdVectorTable": mscExampleWildBcdOperFreeWildBcdVectorTable,
       "mscExampleWildBcdOperFreeWildBcdVectorEntry": mscExampleWildBcdOperFreeWildBcdVectorEntry,
       "mscExampleWildBcdOperFreeWildBcdVectorIndex": mscExampleWildBcdOperFreeWildBcdVectorIndex,
       "mscExampleWildBcdOperFreeWildBcdVectorValue": mscExampleWildBcdOperFreeWildBcdVectorValue,
       "mscExampleWildBcdOperFreeWildBcdArrayTable": mscExampleWildBcdOperFreeWildBcdArrayTable,
       "mscExampleWildBcdOperFreeWildBcdArrayEntry": mscExampleWildBcdOperFreeWildBcdArrayEntry,
       "mscExampleWildBcdOperFreeWildBcdArrayRowIndex": mscExampleWildBcdOperFreeWildBcdArrayRowIndex,
       "mscExampleWildBcdOperFreeWildBcdArrayColumnIndex": mscExampleWildBcdOperFreeWildBcdArrayColumnIndex,
       "mscExampleWildBcdOperFreeWildBcdArrayValue": mscExampleWildBcdOperFreeWildBcdArrayValue,
       "mscExampleWildBcdOperFreeWildBcdReplicatedTable": mscExampleWildBcdOperFreeWildBcdReplicatedTable,
       "mscExampleWildBcdOperFreeWildBcdReplicatedEntry": mscExampleWildBcdOperFreeWildBcdReplicatedEntry,
       "mscExampleWildBcdOperFreeWildBcdReplicatedIndex": mscExampleWildBcdOperFreeWildBcdReplicatedIndex,
       "mscExampleWildBcdOperFreeWildBcdReplicatedValue": mscExampleWildBcdOperFreeWildBcdReplicatedValue,
       "mscExampleWildBcdOperFreeWildBcdReplicatedRowStatus": mscExampleWildBcdOperFreeWildBcdReplicatedRowStatus,
       "mscExampleWildBcdOperFreeWildBcdListTable": mscExampleWildBcdOperFreeWildBcdListTable,
       "mscExampleWildBcdOperFreeWildBcdListEntry": mscExampleWildBcdOperFreeWildBcdListEntry,
       "mscExampleWildBcdOperFreeWildBcdListValue": mscExampleWildBcdOperFreeWildBcdListValue,
       "mscExampleWildBcdOperFreeWildBcdListRowStatus": mscExampleWildBcdOperFreeWildBcdListRowStatus,
       "mscExampleWildBcdProvStructWildBcdVectorTable": mscExampleWildBcdProvStructWildBcdVectorTable,
       "mscExampleWildBcdProvStructWildBcdVectorEntry": mscExampleWildBcdProvStructWildBcdVectorEntry,
       "mscExampleWildBcdProvStructWildBcdVectorIndex": mscExampleWildBcdProvStructWildBcdVectorIndex,
       "mscExampleWildBcdProvStructWildBcdVectorValue": mscExampleWildBcdProvStructWildBcdVectorValue,
       "mscExampleWildBcdProvStructWildBcdArrayTable": mscExampleWildBcdProvStructWildBcdArrayTable,
       "mscExampleWildBcdProvStructWildBcdArrayEntry": mscExampleWildBcdProvStructWildBcdArrayEntry,
       "mscExampleWildBcdProvStructWildBcdArrayRowIndex": mscExampleWildBcdProvStructWildBcdArrayRowIndex,
       "mscExampleWildBcdProvStructWildBcdArrayColumnIndex": mscExampleWildBcdProvStructWildBcdArrayColumnIndex,
       "mscExampleWildBcdProvStructWildBcdArrayValue": mscExampleWildBcdProvStructWildBcdArrayValue,
       "mscExampleWildBcdProvFreeWildBcdVectorTable": mscExampleWildBcdProvFreeWildBcdVectorTable,
       "mscExampleWildBcdProvFreeWildBcdVectorEntry": mscExampleWildBcdProvFreeWildBcdVectorEntry,
       "mscExampleWildBcdProvFreeWildBcdVectorIndex": mscExampleWildBcdProvFreeWildBcdVectorIndex,
       "mscExampleWildBcdProvFreeWildBcdVectorValue": mscExampleWildBcdProvFreeWildBcdVectorValue,
       "mscExampleWildBcdProvFreeWildBcdArrayTable": mscExampleWildBcdProvFreeWildBcdArrayTable,
       "mscExampleWildBcdProvFreeWildBcdArrayEntry": mscExampleWildBcdProvFreeWildBcdArrayEntry,
       "mscExampleWildBcdProvFreeWildBcdArrayRowIndex": mscExampleWildBcdProvFreeWildBcdArrayRowIndex,
       "mscExampleWildBcdProvFreeWildBcdArrayColumnIndex": mscExampleWildBcdProvFreeWildBcdArrayColumnIndex,
       "mscExampleWildBcdProvFreeWildBcdArrayValue": mscExampleWildBcdProvFreeWildBcdArrayValue,
       "mscExampleWildBcdProvFreeWildBcdReplicatedTable": mscExampleWildBcdProvFreeWildBcdReplicatedTable,
       "mscExampleWildBcdProvFreeWildBcdReplicatedEntry": mscExampleWildBcdProvFreeWildBcdReplicatedEntry,
       "mscExampleWildBcdProvFreeWildBcdReplicatedIndex": mscExampleWildBcdProvFreeWildBcdReplicatedIndex,
       "mscExampleWildBcdProvFreeWildBcdReplicatedValue": mscExampleWildBcdProvFreeWildBcdReplicatedValue,
       "mscExampleWildBcdProvFreeWildBcdReplicatedRowStatus": mscExampleWildBcdProvFreeWildBcdReplicatedRowStatus,
       "mscExampleWildBcdProvFreeWildBcdListTable": mscExampleWildBcdProvFreeWildBcdListTable,
       "mscExampleWildBcdProvFreeWildBcdListEntry": mscExampleWildBcdProvFreeWildBcdListEntry,
       "mscExampleWildBcdProvFreeWildBcdListValue": mscExampleWildBcdProvFreeWildBcdListValue,
       "mscExampleWildBcdProvFreeWildBcdListRowStatus": mscExampleWildBcdProvFreeWildBcdListRowStatus,
       "mscExampleEnum": mscExampleEnum,
       "mscExampleEnumRowStatusTable": mscExampleEnumRowStatusTable,
       "mscExampleEnumRowStatusEntry": mscExampleEnumRowStatusEntry,
       "mscExampleEnumRowStatus": mscExampleEnumRowStatus,
       "mscExampleEnumComponentName": mscExampleEnumComponentName,
       "mscExampleEnumStorageType": mscExampleEnumStorageType,
       "mscExampleEnumIndex": mscExampleEnumIndex,
       "mscExampleEnumOperationalTable": mscExampleEnumOperationalTable,
       "mscExampleEnumOperationalEntry": mscExampleEnumOperationalEntry,
       "mscExampleEnumOperStructEnum": mscExampleEnumOperStructEnum,
       "mscExampleEnumOperStructEnumSet": mscExampleEnumOperStructEnumSet,
       "mscExampleEnumOperFreeEnum": mscExampleEnumOperFreeEnum,
       "mscExampleEnumOperFreeEnumSet": mscExampleEnumOperFreeEnumSet,
       "mscExampleEnumProvisionalTable": mscExampleEnumProvisionalTable,
       "mscExampleEnumProvisionalEntry": mscExampleEnumProvisionalEntry,
       "mscExampleEnumProvEnumSub": mscExampleEnumProvEnumSub,
       "mscExampleEnumProvStructEnum": mscExampleEnumProvStructEnum,
       "mscExampleEnumProvStructEnumSet": mscExampleEnumProvStructEnumSet,
       "mscExampleEnumProvFreeEnum": mscExampleEnumProvFreeEnum,
       "mscExampleEnumProvFreeEnum1": mscExampleEnumProvFreeEnum1,
       "mscExampleEnumProvFreeEnumSet": mscExampleEnumProvFreeEnumSet,
       "mscExampleEnumProvFreeEnumSet1": mscExampleEnumProvFreeEnumSet1,
       "mscExampleEnumOperStructEnumVectorTable": mscExampleEnumOperStructEnumVectorTable,
       "mscExampleEnumOperStructEnumVectorEntry": mscExampleEnumOperStructEnumVectorEntry,
       "mscExampleEnumOperStructEnumVectorIndex": mscExampleEnumOperStructEnumVectorIndex,
       "mscExampleEnumOperStructEnumVectorValue": mscExampleEnumOperStructEnumVectorValue,
       "mscExampleEnumOperStructEnumArrayTable": mscExampleEnumOperStructEnumArrayTable,
       "mscExampleEnumOperStructEnumArrayEntry": mscExampleEnumOperStructEnumArrayEntry,
       "mscExampleEnumOperStructEnumArrayMonthIndex": mscExampleEnumOperStructEnumArrayMonthIndex,
       "mscExampleEnumOperStructEnumArrayDayIndex": mscExampleEnumOperStructEnumArrayDayIndex,
       "mscExampleEnumOperStructEnumArrayValue": mscExampleEnumOperStructEnumArrayValue,
       "mscExampleEnumOperFreeEnumVectorTable": mscExampleEnumOperFreeEnumVectorTable,
       "mscExampleEnumOperFreeEnumVectorEntry": mscExampleEnumOperFreeEnumVectorEntry,
       "mscExampleEnumOperFreeEnumVectorIndex": mscExampleEnumOperFreeEnumVectorIndex,
       "mscExampleEnumOperFreeEnumVectorValue": mscExampleEnumOperFreeEnumVectorValue,
       "mscExampleEnumOperFreeEnumArrayTable": mscExampleEnumOperFreeEnumArrayTable,
       "mscExampleEnumOperFreeEnumArrayEntry": mscExampleEnumOperFreeEnumArrayEntry,
       "mscExampleEnumOperFreeEnumArrayMonthIndex": mscExampleEnumOperFreeEnumArrayMonthIndex,
       "mscExampleEnumOperFreeEnumArrayDayIndex": mscExampleEnumOperFreeEnumArrayDayIndex,
       "mscExampleEnumOperFreeEnumArrayValue": mscExampleEnumOperFreeEnumArrayValue,
       "mscExampleEnumOperFreeEnumReplicatedTable": mscExampleEnumOperFreeEnumReplicatedTable,
       "mscExampleEnumOperFreeEnumReplicatedEntry": mscExampleEnumOperFreeEnumReplicatedEntry,
       "mscExampleEnumOperFreeEnumReplicatedIndex": mscExampleEnumOperFreeEnumReplicatedIndex,
       "mscExampleEnumOperFreeEnumReplicatedValue": mscExampleEnumOperFreeEnumReplicatedValue,
       "mscExampleEnumOperFreeEnumReplicatedRowStatus": mscExampleEnumOperFreeEnumReplicatedRowStatus,
       "mscExampleEnumOperFreeEnumListTable": mscExampleEnumOperFreeEnumListTable,
       "mscExampleEnumOperFreeEnumListEntry": mscExampleEnumOperFreeEnumListEntry,
       "mscExampleEnumOperFreeEnumListValue": mscExampleEnumOperFreeEnumListValue,
       "mscExampleEnumOperFreeEnumListRowStatus": mscExampleEnumOperFreeEnumListRowStatus,
       "mscExampleEnumProvStructEnumVectorTable": mscExampleEnumProvStructEnumVectorTable,
       "mscExampleEnumProvStructEnumVectorEntry": mscExampleEnumProvStructEnumVectorEntry,
       "mscExampleEnumProvStructEnumVectorIndex": mscExampleEnumProvStructEnumVectorIndex,
       "mscExampleEnumProvStructEnumVectorValue": mscExampleEnumProvStructEnumVectorValue,
       "mscExampleEnumProvStructEnumArrayTable": mscExampleEnumProvStructEnumArrayTable,
       "mscExampleEnumProvStructEnumArrayEntry": mscExampleEnumProvStructEnumArrayEntry,
       "mscExampleEnumProvStructEnumArrayMonthIndex": mscExampleEnumProvStructEnumArrayMonthIndex,
       "mscExampleEnumProvStructEnumArrayDayIndex": mscExampleEnumProvStructEnumArrayDayIndex,
       "mscExampleEnumProvStructEnumArrayValue": mscExampleEnumProvStructEnumArrayValue,
       "mscExampleEnumProvFreeEnumVectorTable": mscExampleEnumProvFreeEnumVectorTable,
       "mscExampleEnumProvFreeEnumVectorEntry": mscExampleEnumProvFreeEnumVectorEntry,
       "mscExampleEnumProvFreeEnumVectorIndex": mscExampleEnumProvFreeEnumVectorIndex,
       "mscExampleEnumProvFreeEnumVectorValue": mscExampleEnumProvFreeEnumVectorValue,
       "mscExampleEnumProvFreeEnumVector1Table": mscExampleEnumProvFreeEnumVector1Table,
       "mscExampleEnumProvFreeEnumVector1Entry": mscExampleEnumProvFreeEnumVector1Entry,
       "mscExampleEnumProvFreeEnumVector1Index": mscExampleEnumProvFreeEnumVector1Index,
       "mscExampleEnumProvFreeEnumVector1Value": mscExampleEnumProvFreeEnumVector1Value,
       "mscExampleEnumProvFreeEnumArrayTable": mscExampleEnumProvFreeEnumArrayTable,
       "mscExampleEnumProvFreeEnumArrayEntry": mscExampleEnumProvFreeEnumArrayEntry,
       "mscExampleEnumProvFreeEnumArrayMonthIndex": mscExampleEnumProvFreeEnumArrayMonthIndex,
       "mscExampleEnumProvFreeEnumArrayDayIndex": mscExampleEnumProvFreeEnumArrayDayIndex,
       "mscExampleEnumProvFreeEnumArrayValue": mscExampleEnumProvFreeEnumArrayValue,
       "mscExampleEnumProvFreeEnumArray1Table": mscExampleEnumProvFreeEnumArray1Table,
       "mscExampleEnumProvFreeEnumArray1Entry": mscExampleEnumProvFreeEnumArray1Entry,
       "mscExampleEnumProvFreeEnumArray1MonthIndex": mscExampleEnumProvFreeEnumArray1MonthIndex,
       "mscExampleEnumProvFreeEnumArray1DayIndex": mscExampleEnumProvFreeEnumArray1DayIndex,
       "mscExampleEnumProvFreeEnumArray1Value": mscExampleEnumProvFreeEnumArray1Value,
       "mscExampleEnumProvFreeEnumReplicatedTable": mscExampleEnumProvFreeEnumReplicatedTable,
       "mscExampleEnumProvFreeEnumReplicatedEntry": mscExampleEnumProvFreeEnumReplicatedEntry,
       "mscExampleEnumProvFreeEnumReplicatedIndex": mscExampleEnumProvFreeEnumReplicatedIndex,
       "mscExampleEnumProvFreeEnumReplicatedValue": mscExampleEnumProvFreeEnumReplicatedValue,
       "mscExampleEnumProvFreeEnumReplicatedRowStatus": mscExampleEnumProvFreeEnumReplicatedRowStatus,
       "mscExampleEnumProvFreeEnumListTable": mscExampleEnumProvFreeEnumListTable,
       "mscExampleEnumProvFreeEnumListEntry": mscExampleEnumProvFreeEnumListEntry,
       "mscExampleEnumProvFreeEnumListValue": mscExampleEnumProvFreeEnumListValue,
       "mscExampleEnumProvFreeEnumListRowStatus": mscExampleEnumProvFreeEnumListRowStatus,
       "mscExampleEnumProvFreeEnumList1Table": mscExampleEnumProvFreeEnumList1Table,
       "mscExampleEnumProvFreeEnumList1Entry": mscExampleEnumProvFreeEnumList1Entry,
       "mscExampleEnumProvFreeEnumList1Value": mscExampleEnumProvFreeEnumList1Value,
       "mscExampleEnumProvFreeEnumList1RowStatus": mscExampleEnumProvFreeEnumList1RowStatus,
       "mscExampleObjectId": mscExampleObjectId,
       "mscExampleObjectIdRowStatusTable": mscExampleObjectIdRowStatusTable,
       "mscExampleObjectIdRowStatusEntry": mscExampleObjectIdRowStatusEntry,
       "mscExampleObjectIdRowStatus": mscExampleObjectIdRowStatus,
       "mscExampleObjectIdComponentName": mscExampleObjectIdComponentName,
       "mscExampleObjectIdStorageType": mscExampleObjectIdStorageType,
       "mscExampleObjectIdIndex": mscExampleObjectIdIndex,
       "mscExampleObjectIdOperationalTable": mscExampleObjectIdOperationalTable,
       "mscExampleObjectIdOperationalEntry": mscExampleObjectIdOperationalEntry,
       "mscExampleObjectIdOperFreeObjId": mscExampleObjectIdOperFreeObjId,
       "mscExampleObjectIdProvisionalTable": mscExampleObjectIdProvisionalTable,
       "mscExampleObjectIdProvisionalEntry": mscExampleObjectIdProvisionalEntry,
       "mscExampleObjectIdProvEnumSub": mscExampleObjectIdProvEnumSub,
       "mscExampleObjectIdProvFreeObjId": mscExampleObjectIdProvFreeObjId,
       "mscExampleObjectIdOperFreeObjIdReplicatedTable": mscExampleObjectIdOperFreeObjIdReplicatedTable,
       "mscExampleObjectIdOperFreeObjIdReplicatedEntry": mscExampleObjectIdOperFreeObjIdReplicatedEntry,
       "mscExampleObjectIdOperFreeObjIdReplicatedIndex": mscExampleObjectIdOperFreeObjIdReplicatedIndex,
       "mscExampleObjectIdOperFreeObjIdReplicatedValue": mscExampleObjectIdOperFreeObjIdReplicatedValue,
       "mscExampleObjectIdOperFreeObjIdReplicatedRowStatus": mscExampleObjectIdOperFreeObjIdReplicatedRowStatus,
       "mscExampleObjectIdOperFreeObjIdListTable": mscExampleObjectIdOperFreeObjIdListTable,
       "mscExampleObjectIdOperFreeObjIdListEntry": mscExampleObjectIdOperFreeObjIdListEntry,
       "mscExampleObjectIdOperFreeObjIdListValue": mscExampleObjectIdOperFreeObjIdListValue,
       "mscExampleObjectIdOperFreeObjIdListRowStatus": mscExampleObjectIdOperFreeObjIdListRowStatus,
       "mscExampleObjectIdProvFreeObjIdReplicatedTable": mscExampleObjectIdProvFreeObjIdReplicatedTable,
       "mscExampleObjectIdProvFreeObjIdReplicatedEntry": mscExampleObjectIdProvFreeObjIdReplicatedEntry,
       "mscExampleObjectIdProvFreeObjIdReplicatedIndex": mscExampleObjectIdProvFreeObjIdReplicatedIndex,
       "mscExampleObjectIdProvFreeObjIdReplicatedValue": mscExampleObjectIdProvFreeObjIdReplicatedValue,
       "mscExampleObjectIdProvFreeObjIdReplicatedRowStatus": mscExampleObjectIdProvFreeObjIdReplicatedRowStatus,
       "mscExampleObjectIdProvFreeObjIdListTable": mscExampleObjectIdProvFreeObjIdListTable,
       "mscExampleObjectIdProvFreeObjIdListEntry": mscExampleObjectIdProvFreeObjIdListEntry,
       "mscExampleObjectIdProvFreeObjIdListValue": mscExampleObjectIdProvFreeObjIdListValue,
       "mscExampleObjectIdProvFreeObjIdListRowStatus": mscExampleObjectIdProvFreeObjIdListRowStatus,
       "mscExampleSequence": mscExampleSequence,
       "mscExampleSequenceRowStatusTable": mscExampleSequenceRowStatusTable,
       "mscExampleSequenceRowStatusEntry": mscExampleSequenceRowStatusEntry,
       "mscExampleSequenceRowStatus": mscExampleSequenceRowStatus,
       "mscExampleSequenceComponentName": mscExampleSequenceComponentName,
       "mscExampleSequenceStorageType": mscExampleSequenceStorageType,
       "mscExampleSequenceIndex": mscExampleSequenceIndex,
       "mscExampleSequenceOperationalTable": mscExampleSequenceOperationalTable,
       "mscExampleSequenceOperationalEntry": mscExampleSequenceOperationalEntry,
       "mscExampleSequenceOperStructSequence": mscExampleSequenceOperStructSequence,
       "mscExampleSequenceOperFreeSequence": mscExampleSequenceOperFreeSequence,
       "mscExampleSequenceProvisionalTable": mscExampleSequenceProvisionalTable,
       "mscExampleSequenceProvisionalEntry": mscExampleSequenceProvisionalEntry,
       "mscExampleSequenceProvStructSequence": mscExampleSequenceProvStructSequence,
       "mscExampleSequenceProvFreeSequence": mscExampleSequenceProvFreeSequence,
       "mscExampleSequenceOperFreeSequenceReplicatedTable": mscExampleSequenceOperFreeSequenceReplicatedTable,
       "mscExampleSequenceOperFreeSequenceReplicatedEntry": mscExampleSequenceOperFreeSequenceReplicatedEntry,
       "mscExampleSequenceOperFreeSequenceReplicatedIndex": mscExampleSequenceOperFreeSequenceReplicatedIndex,
       "mscExampleSequenceOperFreeSequenceReplicatedValue": mscExampleSequenceOperFreeSequenceReplicatedValue,
       "mscExampleSequenceOperFreeSequenceReplicatedRowStatus": mscExampleSequenceOperFreeSequenceReplicatedRowStatus,
       "mscExampleSequenceOperFreeSequenceListTable": mscExampleSequenceOperFreeSequenceListTable,
       "mscExampleSequenceOperFreeSequenceListEntry": mscExampleSequenceOperFreeSequenceListEntry,
       "mscExampleSequenceOperFreeSequenceListValue": mscExampleSequenceOperFreeSequenceListValue,
       "mscExampleSequenceOperFreeSequenceListRowStatus": mscExampleSequenceOperFreeSequenceListRowStatus,
       "mscExampleSequenceProvFreeSequenceReplicatedTable": mscExampleSequenceProvFreeSequenceReplicatedTable,
       "mscExampleSequenceProvFreeSequenceReplicatedEntry": mscExampleSequenceProvFreeSequenceReplicatedEntry,
       "mscExampleSequenceProvFreeSequenceReplicatedIndex": mscExampleSequenceProvFreeSequenceReplicatedIndex,
       "mscExampleSequenceProvFreeSequenceReplicatedValue": mscExampleSequenceProvFreeSequenceReplicatedValue,
       "mscExampleSequenceProvFreeSequenceReplicatedRowStatus": mscExampleSequenceProvFreeSequenceReplicatedRowStatus,
       "mscExampleSequenceProvFreeSequenceListTable": mscExampleSequenceProvFreeSequenceListTable,
       "mscExampleSequenceProvFreeSequenceListEntry": mscExampleSequenceProvFreeSequenceListEntry,
       "mscExampleSequenceProvFreeSequenceListValue": mscExampleSequenceProvFreeSequenceListValue,
       "mscExampleSequenceProvFreeSequenceListRowStatus": mscExampleSequenceProvFreeSequenceListRowStatus,
       "mscExampleSigned": mscExampleSigned,
       "mscExampleSignedRowStatusTable": mscExampleSignedRowStatusTable,
       "mscExampleSignedRowStatusEntry": mscExampleSignedRowStatusEntry,
       "mscExampleSignedRowStatus": mscExampleSignedRowStatus,
       "mscExampleSignedComponentName": mscExampleSignedComponentName,
       "mscExampleSignedStorageType": mscExampleSignedStorageType,
       "mscExampleSignedIndex": mscExampleSignedIndex,
       "mscExampleSignedOperationalTable": mscExampleSignedOperationalTable,
       "mscExampleSignedOperationalEntry": mscExampleSignedOperationalEntry,
       "mscExampleSignedOperStructSigned": mscExampleSignedOperStructSigned,
       "mscExampleSignedOperFreeSigned": mscExampleSignedOperFreeSigned,
       "mscExampleSignedProvisionalTable": mscExampleSignedProvisionalTable,
       "mscExampleSignedProvisionalEntry": mscExampleSignedProvisionalEntry,
       "mscExampleSignedProvSignedSub": mscExampleSignedProvSignedSub,
       "mscExampleSignedProvStructSigned": mscExampleSignedProvStructSigned,
       "mscExampleSignedProvFreeSigned": mscExampleSignedProvFreeSigned,
       "mscExampleSignedProvFreeSigned1": mscExampleSignedProvFreeSigned1,
       "mscExampleSignedOperStructSignedVectorTable": mscExampleSignedOperStructSignedVectorTable,
       "mscExampleSignedOperStructSignedVectorEntry": mscExampleSignedOperStructSignedVectorEntry,
       "mscExampleSignedOperStructSignedVectorIndex": mscExampleSignedOperStructSignedVectorIndex,
       "mscExampleSignedOperStructSignedVectorValue": mscExampleSignedOperStructSignedVectorValue,
       "mscExampleSignedOperStructSignedArrayTable": mscExampleSignedOperStructSignedArrayTable,
       "mscExampleSignedOperStructSignedArrayEntry": mscExampleSignedOperStructSignedArrayEntry,
       "mscExampleSignedOperStructSignedArrayRowIndex": mscExampleSignedOperStructSignedArrayRowIndex,
       "mscExampleSignedOperStructSignedArrayColumnIndex": mscExampleSignedOperStructSignedArrayColumnIndex,
       "mscExampleSignedOperStructSignedArrayValue": mscExampleSignedOperStructSignedArrayValue,
       "mscExampleSignedOperFreeSignedVectorTable": mscExampleSignedOperFreeSignedVectorTable,
       "mscExampleSignedOperFreeSignedVectorEntry": mscExampleSignedOperFreeSignedVectorEntry,
       "mscExampleSignedOperFreeSignedVectorIndex": mscExampleSignedOperFreeSignedVectorIndex,
       "mscExampleSignedOperFreeSignedVectorValue": mscExampleSignedOperFreeSignedVectorValue,
       "mscExampleSignedOperFreeSignedArrayTable": mscExampleSignedOperFreeSignedArrayTable,
       "mscExampleSignedOperFreeSignedArrayEntry": mscExampleSignedOperFreeSignedArrayEntry,
       "mscExampleSignedOperFreeSignedArrayRowIndex": mscExampleSignedOperFreeSignedArrayRowIndex,
       "mscExampleSignedOperFreeSignedArrayColumnIndex": mscExampleSignedOperFreeSignedArrayColumnIndex,
       "mscExampleSignedOperFreeSignedArrayValue": mscExampleSignedOperFreeSignedArrayValue,
       "mscExampleSignedOperFreeSignedReplicatedTable": mscExampleSignedOperFreeSignedReplicatedTable,
       "mscExampleSignedOperFreeSignedReplicatedEntry": mscExampleSignedOperFreeSignedReplicatedEntry,
       "mscExampleSignedOperFreeSignedReplicatedIndex": mscExampleSignedOperFreeSignedReplicatedIndex,
       "mscExampleSignedOperFreeSignedReplicatedValue": mscExampleSignedOperFreeSignedReplicatedValue,
       "mscExampleSignedOperFreeSignedReplicatedRowStatus": mscExampleSignedOperFreeSignedReplicatedRowStatus,
       "mscExampleSignedOperFreeSignedListTable": mscExampleSignedOperFreeSignedListTable,
       "mscExampleSignedOperFreeSignedListEntry": mscExampleSignedOperFreeSignedListEntry,
       "mscExampleSignedOperFreeSignedListValue": mscExampleSignedOperFreeSignedListValue,
       "mscExampleSignedOperFreeSignedListRowStatus": mscExampleSignedOperFreeSignedListRowStatus,
       "mscExampleSignedProvStructSignedVectorTable": mscExampleSignedProvStructSignedVectorTable,
       "mscExampleSignedProvStructSignedVectorEntry": mscExampleSignedProvStructSignedVectorEntry,
       "mscExampleSignedProvStructSignedVectorIndex": mscExampleSignedProvStructSignedVectorIndex,
       "mscExampleSignedProvStructSignedVectorValue": mscExampleSignedProvStructSignedVectorValue,
       "mscExampleSignedProvStructSignedArrayTable": mscExampleSignedProvStructSignedArrayTable,
       "mscExampleSignedProvStructSignedArrayEntry": mscExampleSignedProvStructSignedArrayEntry,
       "mscExampleSignedProvStructSignedArrayRowIndex": mscExampleSignedProvStructSignedArrayRowIndex,
       "mscExampleSignedProvStructSignedArrayColumnIndex": mscExampleSignedProvStructSignedArrayColumnIndex,
       "mscExampleSignedProvStructSignedArrayValue": mscExampleSignedProvStructSignedArrayValue,
       "mscExampleSignedProvFreeSignedVectorTable": mscExampleSignedProvFreeSignedVectorTable,
       "mscExampleSignedProvFreeSignedVectorEntry": mscExampleSignedProvFreeSignedVectorEntry,
       "mscExampleSignedProvFreeSignedVectorIndex": mscExampleSignedProvFreeSignedVectorIndex,
       "mscExampleSignedProvFreeSignedVectorValue": mscExampleSignedProvFreeSignedVectorValue,
       "mscExampleSignedProvFreeSignedVector1Table": mscExampleSignedProvFreeSignedVector1Table,
       "mscExampleSignedProvFreeSignedVector1Entry": mscExampleSignedProvFreeSignedVector1Entry,
       "mscExampleSignedProvFreeSignedVector1Index": mscExampleSignedProvFreeSignedVector1Index,
       "mscExampleSignedProvFreeSignedVector1Value": mscExampleSignedProvFreeSignedVector1Value,
       "mscExampleSignedProvFreeSignedArrayTable": mscExampleSignedProvFreeSignedArrayTable,
       "mscExampleSignedProvFreeSignedArrayEntry": mscExampleSignedProvFreeSignedArrayEntry,
       "mscExampleSignedProvFreeSignedArrayRowIndex": mscExampleSignedProvFreeSignedArrayRowIndex,
       "mscExampleSignedProvFreeSignedArrayColumnIndex": mscExampleSignedProvFreeSignedArrayColumnIndex,
       "mscExampleSignedProvFreeSignedArrayValue": mscExampleSignedProvFreeSignedArrayValue,
       "mscExampleSignedProvFreeSignedArray1Table": mscExampleSignedProvFreeSignedArray1Table,
       "mscExampleSignedProvFreeSignedArray1Entry": mscExampleSignedProvFreeSignedArray1Entry,
       "mscExampleSignedProvFreeSignedArray1RowIndex": mscExampleSignedProvFreeSignedArray1RowIndex,
       "mscExampleSignedProvFreeSignedArray1ColumnIndex": mscExampleSignedProvFreeSignedArray1ColumnIndex,
       "mscExampleSignedProvFreeSignedArray1Value": mscExampleSignedProvFreeSignedArray1Value,
       "mscExampleSignedProvFreeSignedReplicatedTable": mscExampleSignedProvFreeSignedReplicatedTable,
       "mscExampleSignedProvFreeSignedReplicatedEntry": mscExampleSignedProvFreeSignedReplicatedEntry,
       "mscExampleSignedProvFreeSignedReplicatedIndex": mscExampleSignedProvFreeSignedReplicatedIndex,
       "mscExampleSignedProvFreeSignedReplicatedValue": mscExampleSignedProvFreeSignedReplicatedValue,
       "mscExampleSignedProvFreeSignedReplicatedRowStatus": mscExampleSignedProvFreeSignedReplicatedRowStatus,
       "mscExampleSignedProvFreeSignedListTable": mscExampleSignedProvFreeSignedListTable,
       "mscExampleSignedProvFreeSignedListEntry": mscExampleSignedProvFreeSignedListEntry,
       "mscExampleSignedProvFreeSignedListValue": mscExampleSignedProvFreeSignedListValue,
       "mscExampleSignedProvFreeSignedListRowStatus": mscExampleSignedProvFreeSignedListRowStatus,
       "mscExampleMiscellaneous": mscExampleMiscellaneous,
       "mscExampleMiscellaneousRowStatusTable": mscExampleMiscellaneousRowStatusTable,
       "mscExampleMiscellaneousRowStatusEntry": mscExampleMiscellaneousRowStatusEntry,
       "mscExampleMiscellaneousRowStatus": mscExampleMiscellaneousRowStatus,
       "mscExampleMiscellaneousComponentName": mscExampleMiscellaneousComponentName,
       "mscExampleMiscellaneousStorageType": mscExampleMiscellaneousStorageType,
       "mscExampleMiscellaneousIndex": mscExampleMiscellaneousIndex,
       "mscExampleMiscellaneousOperationalTable": mscExampleMiscellaneousOperationalTable,
       "mscExampleMiscellaneousOperationalEntry": mscExampleMiscellaneousOperationalEntry,
       "mscExampleMiscellaneousOperStructLong": mscExampleMiscellaneousOperStructLong,
       "mscExampleMiscellaneousOperFreeLong": mscExampleMiscellaneousOperFreeLong,
       "mscExampleMiscellaneousOperFreeTime": mscExampleMiscellaneousOperFreeTime,
       "mscExampleMiscellaneousOperFreeTimeDateOnly": mscExampleMiscellaneousOperFreeTimeDateOnly,
       "mscExampleMiscellaneousOperFreeTimeTimeOnly": mscExampleMiscellaneousOperFreeTimeTimeOnly,
       "mscExampleMiscellaneousOperFreeTimeDateTimeMinute": mscExampleMiscellaneousOperFreeTimeDateTimeMinute,
       "mscExampleMiscellaneousOperFreeCounter64": mscExampleMiscellaneousOperFreeCounter64,
       "mscExampleMiscellaneousOperFreeGauge64": mscExampleMiscellaneousOperFreeGauge64,
       "mscExampleMiscellaneousOperStructCounter64": mscExampleMiscellaneousOperStructCounter64,
       "mscExampleMiscellaneousProvisionalTable": mscExampleMiscellaneousProvisionalTable,
       "mscExampleMiscellaneousProvisionalEntry": mscExampleMiscellaneousProvisionalEntry,
       "mscExampleMiscellaneousProvEnumSub": mscExampleMiscellaneousProvEnumSub,
       "mscExampleMiscellaneousProvStructLong": mscExampleMiscellaneousProvStructLong,
       "mscExampleMiscellaneousProvFreeLong": mscExampleMiscellaneousProvFreeLong,
       "mscExampleMiscellaneousProvFreeTime": mscExampleMiscellaneousProvFreeTime,
       "mscExampleMiscellaneousProvFreeTimeDateOnly": mscExampleMiscellaneousProvFreeTimeDateOnly,
       "mscExampleMiscellaneousProvFreeTimeTimeOnly": mscExampleMiscellaneousProvFreeTimeTimeOnly,
       "mscExampleMiscellaneousProvFreeTimeDateTimeMinute": mscExampleMiscellaneousProvFreeTimeDateTimeMinute,
       "mscExampleMiscellaneousProvFreeTime1": mscExampleMiscellaneousProvFreeTime1,
       "mscExampleMiscellaneousProvFreeTimeDateOnly1": mscExampleMiscellaneousProvFreeTimeDateOnly1,
       "mscExampleMiscellaneousProvFreeTimeTimeOnly1": mscExampleMiscellaneousProvFreeTimeTimeOnly1,
       "mscExampleMiscellaneousProvFreeTimeDateTimeMinute1": mscExampleMiscellaneousProvFreeTimeDateTimeMinute1,
       "mscExampleMiscellaneousOperFreeLongReplicatedTable": mscExampleMiscellaneousOperFreeLongReplicatedTable,
       "mscExampleMiscellaneousOperFreeLongReplicatedEntry": mscExampleMiscellaneousOperFreeLongReplicatedEntry,
       "mscExampleMiscellaneousOperFreeLongReplicatedIndex": mscExampleMiscellaneousOperFreeLongReplicatedIndex,
       "mscExampleMiscellaneousOperFreeLongReplicatedValue": mscExampleMiscellaneousOperFreeLongReplicatedValue,
       "mscExampleMiscellaneousOperFreeLongReplicatedRowStatus": mscExampleMiscellaneousOperFreeLongReplicatedRowStatus,
       "mscExampleMiscellaneousOperFreeLongListTable": mscExampleMiscellaneousOperFreeLongListTable,
       "mscExampleMiscellaneousOperFreeLongListEntry": mscExampleMiscellaneousOperFreeLongListEntry,
       "mscExampleMiscellaneousOperFreeLongListValue": mscExampleMiscellaneousOperFreeLongListValue,
       "mscExampleMiscellaneousOperFreeLongListRowStatus": mscExampleMiscellaneousOperFreeLongListRowStatus,
       "mscExampleMiscellaneousOperFreeTimeListTable": mscExampleMiscellaneousOperFreeTimeListTable,
       "mscExampleMiscellaneousOperFreeTimeListEntry": mscExampleMiscellaneousOperFreeTimeListEntry,
       "mscExampleMiscellaneousOperFreeTimeListValue": mscExampleMiscellaneousOperFreeTimeListValue,
       "mscExampleMiscellaneousOperFreeTimeListRowStatus": mscExampleMiscellaneousOperFreeTimeListRowStatus,
       "mscExampleMiscellaneousProvFreeLongReplicatedTable": mscExampleMiscellaneousProvFreeLongReplicatedTable,
       "mscExampleMiscellaneousProvFreeLongReplicatedEntry": mscExampleMiscellaneousProvFreeLongReplicatedEntry,
       "mscExampleMiscellaneousProvFreeLongReplicatedIndex": mscExampleMiscellaneousProvFreeLongReplicatedIndex,
       "mscExampleMiscellaneousProvFreeLongReplicatedValue": mscExampleMiscellaneousProvFreeLongReplicatedValue,
       "mscExampleMiscellaneousProvFreeLongReplicatedRowStatus": mscExampleMiscellaneousProvFreeLongReplicatedRowStatus,
       "mscExampleMiscellaneousProvFreeLongListTable": mscExampleMiscellaneousProvFreeLongListTable,
       "mscExampleMiscellaneousProvFreeLongListEntry": mscExampleMiscellaneousProvFreeLongListEntry,
       "mscExampleMiscellaneousProvFreeLongListValue": mscExampleMiscellaneousProvFreeLongListValue,
       "mscExampleMiscellaneousProvFreeLongListRowStatus": mscExampleMiscellaneousProvFreeLongListRowStatus,
       "mscExampleMiscellaneousProvFreeTimeReplicatedTable": mscExampleMiscellaneousProvFreeTimeReplicatedTable,
       "mscExampleMiscellaneousProvFreeTimeReplicatedEntry": mscExampleMiscellaneousProvFreeTimeReplicatedEntry,
       "mscExampleMiscellaneousProvFreeTimeReplicatedIndex": mscExampleMiscellaneousProvFreeTimeReplicatedIndex,
       "mscExampleMiscellaneousProvFreeTimeReplicatedValue": mscExampleMiscellaneousProvFreeTimeReplicatedValue,
       "mscExampleMiscellaneousProvFreeTimeReplicatedRowStatus": mscExampleMiscellaneousProvFreeTimeReplicatedRowStatus,
       "mscExampleMiscellaneousProvFreeTimeListTable": mscExampleMiscellaneousProvFreeTimeListTable,
       "mscExampleMiscellaneousProvFreeTimeListEntry": mscExampleMiscellaneousProvFreeTimeListEntry,
       "mscExampleMiscellaneousProvFreeTimeListValue": mscExampleMiscellaneousProvFreeTimeListValue,
       "mscExampleMiscellaneousProvFreeTimeListRowStatus": mscExampleMiscellaneousProvFreeTimeListRowStatus,
       "mscExampleMiscellaneousProvFreeTimeList1Table": mscExampleMiscellaneousProvFreeTimeList1Table,
       "mscExampleMiscellaneousProvFreeTimeList1Entry": mscExampleMiscellaneousProvFreeTimeList1Entry,
       "mscExampleMiscellaneousProvFreeTimeList1Value": mscExampleMiscellaneousProvFreeTimeList1Value,
       "mscExampleMiscellaneousProvFreeTimeList1RowStatus": mscExampleMiscellaneousProvFreeTimeList1RowStatus,
       "mscExampleMiscellaneousProvFreeTimeList2Table": mscExampleMiscellaneousProvFreeTimeList2Table,
       "mscExampleMiscellaneousProvFreeTimeList2Entry": mscExampleMiscellaneousProvFreeTimeList2Entry,
       "mscExampleMiscellaneousProvFreeTimeList2Value": mscExampleMiscellaneousProvFreeTimeList2Value,
       "mscExampleMiscellaneousProvFreeTimeList2RowStatus": mscExampleMiscellaneousProvFreeTimeList2RowStatus,
       "mscExampleMiscellaneousProvFreeTimeList3Table": mscExampleMiscellaneousProvFreeTimeList3Table,
       "mscExampleMiscellaneousProvFreeTimeList3Entry": mscExampleMiscellaneousProvFreeTimeList3Entry,
       "mscExampleMiscellaneousProvFreeTimeList3Value": mscExampleMiscellaneousProvFreeTimeList3Value,
       "mscExampleMiscellaneousProvFreeTimeList3RowStatus": mscExampleMiscellaneousProvFreeTimeList3RowStatus,
       "mscExampleOneIndex": mscExampleOneIndex,
       "mscExampleOneIndexRowStatusTable": mscExampleOneIndexRowStatusTable,
       "mscExampleOneIndexRowStatusEntry": mscExampleOneIndexRowStatusEntry,
       "mscExampleOneIndexRowStatus": mscExampleOneIndexRowStatus,
       "mscExampleOneIndexComponentName": mscExampleOneIndexComponentName,
       "mscExampleOneIndexStorageType": mscExampleOneIndexStorageType,
       "mscExampleOneIndexOneIndex": mscExampleOneIndexOneIndex,
       "mscExampleOneIndexProvisionedTable": mscExampleOneIndexProvisionedTable,
       "mscExampleOneIndexProvisionedEntry": mscExampleOneIndexProvisionedEntry,
       "mscExampleOneIndexProvAttribute": mscExampleOneIndexProvAttribute,
       "mscExampleTwoIndices": mscExampleTwoIndices,
       "mscExampleTwoIndicesRowStatusTable": mscExampleTwoIndicesRowStatusTable,
       "mscExampleTwoIndicesRowStatusEntry": mscExampleTwoIndicesRowStatusEntry,
       "mscExampleTwoIndicesRowStatus": mscExampleTwoIndicesRowStatus,
       "mscExampleTwoIndicesComponentName": mscExampleTwoIndicesComponentName,
       "mscExampleTwoIndicesStorageType": mscExampleTwoIndicesStorageType,
       "mscExampleTwoIndicesOneIndex": mscExampleTwoIndicesOneIndex,
       "mscExampleTwoIndicesTwoIndex": mscExampleTwoIndicesTwoIndex,
       "mscExampleTwoIndicesProvisionedTable": mscExampleTwoIndicesProvisionedTable,
       "mscExampleTwoIndicesProvisionedEntry": mscExampleTwoIndicesProvisionedEntry,
       "mscExampleTwoIndicesProvAttribute": mscExampleTwoIndicesProvAttribute,
       "mscExampleThreeIndices": mscExampleThreeIndices,
       "mscExampleThreeIndicesRowStatusTable": mscExampleThreeIndicesRowStatusTable,
       "mscExampleThreeIndicesRowStatusEntry": mscExampleThreeIndicesRowStatusEntry,
       "mscExampleThreeIndicesRowStatus": mscExampleThreeIndicesRowStatus,
       "mscExampleThreeIndicesComponentName": mscExampleThreeIndicesComponentName,
       "mscExampleThreeIndicesStorageType": mscExampleThreeIndicesStorageType,
       "mscExampleThreeIndicesOneIndex": mscExampleThreeIndicesOneIndex,
       "mscExampleThreeIndicesTwoIndex": mscExampleThreeIndicesTwoIndex,
       "mscExampleThreeIndicesThreeIndex": mscExampleThreeIndicesThreeIndex,
       "mscExampleThreeIndicesProvisionedTable": mscExampleThreeIndicesProvisionedTable,
       "mscExampleThreeIndicesProvisionedEntry": mscExampleThreeIndicesProvisionedEntry,
       "mscExampleThreeIndicesProvAttribute": mscExampleThreeIndicesProvAttribute,
       "mscExampleFourIndices": mscExampleFourIndices,
       "mscExampleFourIndicesRowStatusTable": mscExampleFourIndicesRowStatusTable,
       "mscExampleFourIndicesRowStatusEntry": mscExampleFourIndicesRowStatusEntry,
       "mscExampleFourIndicesRowStatus": mscExampleFourIndicesRowStatus,
       "mscExampleFourIndicesComponentName": mscExampleFourIndicesComponentName,
       "mscExampleFourIndicesStorageType": mscExampleFourIndicesStorageType,
       "mscExampleFourIndicesOneIndex": mscExampleFourIndicesOneIndex,
       "mscExampleFourIndicesTwoIndex": mscExampleFourIndicesTwoIndex,
       "mscExampleFourIndicesThreeIndex": mscExampleFourIndicesThreeIndex,
       "mscExampleFourIndicesFourIndex": mscExampleFourIndicesFourIndex,
       "mscExampleFourIndicesProvisionedTable": mscExampleFourIndicesProvisionedTable,
       "mscExampleFourIndicesProvisionedEntry": mscExampleFourIndicesProvisionedEntry,
       "mscExampleFourIndicesProvAttribute": mscExampleFourIndicesProvAttribute,
       "mscExampleDecimalIndices": mscExampleDecimalIndices,
       "mscExampleDecimalIndicesRowStatusTable": mscExampleDecimalIndicesRowStatusTable,
       "mscExampleDecimalIndicesRowStatusEntry": mscExampleDecimalIndicesRowStatusEntry,
       "mscExampleDecimalIndicesRowStatus": mscExampleDecimalIndicesRowStatus,
       "mscExampleDecimalIndicesComponentName": mscExampleDecimalIndicesComponentName,
       "mscExampleDecimalIndicesStorageType": mscExampleDecimalIndicesStorageType,
       "mscExampleDecimalIndicesOneIndex": mscExampleDecimalIndicesOneIndex,
       "mscExampleDecimalIndicesTwoIndex": mscExampleDecimalIndicesTwoIndex,
       "mscExampleDecimalIndicesThreeIndex": mscExampleDecimalIndicesThreeIndex,
       "mscExampleDecimalIndicesProvisionedTable": mscExampleDecimalIndicesProvisionedTable,
       "mscExampleDecimalIndicesProvisionedEntry": mscExampleDecimalIndicesProvisionedEntry,
       "mscExampleDecimalIndicesProvAttribute": mscExampleDecimalIndicesProvAttribute,
       "mscExampleHexIndices": mscExampleHexIndices,
       "mscExampleHexIndicesRowStatusTable": mscExampleHexIndicesRowStatusTable,
       "mscExampleHexIndicesRowStatusEntry": mscExampleHexIndicesRowStatusEntry,
       "mscExampleHexIndicesRowStatus": mscExampleHexIndicesRowStatus,
       "mscExampleHexIndicesComponentName": mscExampleHexIndicesComponentName,
       "mscExampleHexIndicesStorageType": mscExampleHexIndicesStorageType,
       "mscExampleHexIndicesOneIndex": mscExampleHexIndicesOneIndex,
       "mscExampleHexIndicesTwoIndex": mscExampleHexIndicesTwoIndex,
       "mscExampleHexIndicesThreeIndex": mscExampleHexIndicesThreeIndex,
       "mscExampleHexIndicesProvisionedTable": mscExampleHexIndicesProvisionedTable,
       "mscExampleHexIndicesProvisionedEntry": mscExampleHexIndicesProvisionedEntry,
       "mscExampleHexIndicesProvAttribute": mscExampleHexIndicesProvAttribute,
       "mscExampleIpAddrIndices": mscExampleIpAddrIndices,
       "mscExampleIpAddrIndicesRowStatusTable": mscExampleIpAddrIndicesRowStatusTable,
       "mscExampleIpAddrIndicesRowStatusEntry": mscExampleIpAddrIndicesRowStatusEntry,
       "mscExampleIpAddrIndicesRowStatus": mscExampleIpAddrIndicesRowStatus,
       "mscExampleIpAddrIndicesComponentName": mscExampleIpAddrIndicesComponentName,
       "mscExampleIpAddrIndicesStorageType": mscExampleIpAddrIndicesStorageType,
       "mscExampleIpAddrIndicesOneIndex": mscExampleIpAddrIndicesOneIndex,
       "mscExampleIpAddrIndicesTwoIndex": mscExampleIpAddrIndicesTwoIndex,
       "mscExampleIpAddrIndicesThreeIndex": mscExampleIpAddrIndicesThreeIndex,
       "mscExampleIpAddrIndicesProvisionedTable": mscExampleIpAddrIndicesProvisionedTable,
       "mscExampleIpAddrIndicesProvisionedEntry": mscExampleIpAddrIndicesProvisionedEntry,
       "mscExampleIpAddrIndicesProvAttribute": mscExampleIpAddrIndicesProvAttribute,
       "mscExampleAsciiIndices": mscExampleAsciiIndices,
       "mscExampleAsciiIndicesRowStatusTable": mscExampleAsciiIndicesRowStatusTable,
       "mscExampleAsciiIndicesRowStatusEntry": mscExampleAsciiIndicesRowStatusEntry,
       "mscExampleAsciiIndicesRowStatus": mscExampleAsciiIndicesRowStatus,
       "mscExampleAsciiIndicesComponentName": mscExampleAsciiIndicesComponentName,
       "mscExampleAsciiIndicesStorageType": mscExampleAsciiIndicesStorageType,
       "mscExampleAsciiIndicesOneIndex": mscExampleAsciiIndicesOneIndex,
       "mscExampleAsciiIndicesTwoIndex": mscExampleAsciiIndicesTwoIndex,
       "mscExampleAsciiIndicesThreeIndex": mscExampleAsciiIndicesThreeIndex,
       "mscExampleAsciiIndicesProvisionedTable": mscExampleAsciiIndicesProvisionedTable,
       "mscExampleAsciiIndicesProvisionedEntry": mscExampleAsciiIndicesProvisionedEntry,
       "mscExampleAsciiIndicesProvAttribute": mscExampleAsciiIndicesProvAttribute,
       "mscExampleHexStrIndices": mscExampleHexStrIndices,
       "mscExampleHexStrIndicesRowStatusTable": mscExampleHexStrIndicesRowStatusTable,
       "mscExampleHexStrIndicesRowStatusEntry": mscExampleHexStrIndicesRowStatusEntry,
       "mscExampleHexStrIndicesRowStatus": mscExampleHexStrIndicesRowStatus,
       "mscExampleHexStrIndicesComponentName": mscExampleHexStrIndicesComponentName,
       "mscExampleHexStrIndicesStorageType": mscExampleHexStrIndicesStorageType,
       "mscExampleHexStrIndicesOneIndex": mscExampleHexStrIndicesOneIndex,
       "mscExampleHexStrIndicesTwoIndex": mscExampleHexStrIndicesTwoIndex,
       "mscExampleHexStrIndicesThreeIndex": mscExampleHexStrIndicesThreeIndex,
       "mscExampleHexStrIndicesProvisionedTable": mscExampleHexStrIndicesProvisionedTable,
       "mscExampleHexStrIndicesProvisionedEntry": mscExampleHexStrIndicesProvisionedEntry,
       "mscExampleHexStrIndicesProvAttribute": mscExampleHexStrIndicesProvAttribute,
       "mscExampleBcdIndices": mscExampleBcdIndices,
       "mscExampleBcdIndicesRowStatusTable": mscExampleBcdIndicesRowStatusTable,
       "mscExampleBcdIndicesRowStatusEntry": mscExampleBcdIndicesRowStatusEntry,
       "mscExampleBcdIndicesRowStatus": mscExampleBcdIndicesRowStatus,
       "mscExampleBcdIndicesComponentName": mscExampleBcdIndicesComponentName,
       "mscExampleBcdIndicesStorageType": mscExampleBcdIndicesStorageType,
       "mscExampleBcdIndicesOneIndex": mscExampleBcdIndicesOneIndex,
       "mscExampleBcdIndicesTwoIndex": mscExampleBcdIndicesTwoIndex,
       "mscExampleBcdIndicesThreeIndex": mscExampleBcdIndicesThreeIndex,
       "mscExampleBcdIndicesProvisionedTable": mscExampleBcdIndicesProvisionedTable,
       "mscExampleBcdIndicesProvisionedEntry": mscExampleBcdIndicesProvisionedEntry,
       "mscExampleBcdIndicesProvAttribute": mscExampleBcdIndicesProvAttribute,
       "mscExampleEnumIndices": mscExampleEnumIndices,
       "mscExampleEnumIndicesRowStatusTable": mscExampleEnumIndicesRowStatusTable,
       "mscExampleEnumIndicesRowStatusEntry": mscExampleEnumIndicesRowStatusEntry,
       "mscExampleEnumIndicesRowStatus": mscExampleEnumIndicesRowStatus,
       "mscExampleEnumIndicesComponentName": mscExampleEnumIndicesComponentName,
       "mscExampleEnumIndicesStorageType": mscExampleEnumIndicesStorageType,
       "mscExampleEnumIndicesOneIndex": mscExampleEnumIndicesOneIndex,
       "mscExampleEnumIndicesTwoIndex": mscExampleEnumIndicesTwoIndex,
       "mscExampleEnumIndicesThreeIndex": mscExampleEnumIndicesThreeIndex,
       "mscExampleEnumIndicesProvisionedTable": mscExampleEnumIndicesProvisionedTable,
       "mscExampleEnumIndicesProvisionedEntry": mscExampleEnumIndicesProvisionedEntry,
       "mscExampleEnumIndicesProvAttribute": mscExampleEnumIndicesProvAttribute,
       "mscExampleSequenceIndices": mscExampleSequenceIndices,
       "mscExampleSequenceIndicesRowStatusTable": mscExampleSequenceIndicesRowStatusTable,
       "mscExampleSequenceIndicesRowStatusEntry": mscExampleSequenceIndicesRowStatusEntry,
       "mscExampleSequenceIndicesRowStatus": mscExampleSequenceIndicesRowStatus,
       "mscExampleSequenceIndicesComponentName": mscExampleSequenceIndicesComponentName,
       "mscExampleSequenceIndicesStorageType": mscExampleSequenceIndicesStorageType,
       "mscExampleSequenceIndicesOneIndex": mscExampleSequenceIndicesOneIndex,
       "mscExampleSequenceIndicesTwoIndex": mscExampleSequenceIndicesTwoIndex,
       "mscExampleSequenceIndicesThreeIndex": mscExampleSequenceIndicesThreeIndex,
       "mscExampleSequenceIndicesProvisionedTable": mscExampleSequenceIndicesProvisionedTable,
       "mscExampleSequenceIndicesProvisionedEntry": mscExampleSequenceIndicesProvisionedEntry,
       "mscExampleSequenceIndicesProvAttribute": mscExampleSequenceIndicesProvAttribute,
       "mscExampleObjIdIndices": mscExampleObjIdIndices,
       "mscExampleObjIdIndicesRowStatusTable": mscExampleObjIdIndicesRowStatusTable,
       "mscExampleObjIdIndicesRowStatusEntry": mscExampleObjIdIndicesRowStatusEntry,
       "mscExampleObjIdIndicesRowStatus": mscExampleObjIdIndicesRowStatus,
       "mscExampleObjIdIndicesComponentName": mscExampleObjIdIndicesComponentName,
       "mscExampleObjIdIndicesStorageType": mscExampleObjIdIndicesStorageType,
       "mscExampleObjIdIndicesOneIndex": mscExampleObjIdIndicesOneIndex,
       "mscExampleObjIdIndicesTwoIndex": mscExampleObjIdIndicesTwoIndex,
       "mscExampleObjIdIndicesThreeIndex": mscExampleObjIdIndicesThreeIndex,
       "mscExampleObjIdIndicesProvisionedTable": mscExampleObjIdIndicesProvisionedTable,
       "mscExampleObjIdIndicesProvisionedEntry": mscExampleObjIdIndicesProvisionedEntry,
       "mscExampleObjIdIndicesProvAttribute": mscExampleObjIdIndicesProvAttribute,
       "mscExampleDashedIndices": mscExampleDashedIndices,
       "mscExampleDashedIndicesRowStatusTable": mscExampleDashedIndicesRowStatusTable,
       "mscExampleDashedIndicesRowStatusEntry": mscExampleDashedIndicesRowStatusEntry,
       "mscExampleDashedIndicesRowStatus": mscExampleDashedIndicesRowStatus,
       "mscExampleDashedIndicesComponentName": mscExampleDashedIndicesComponentName,
       "mscExampleDashedIndicesStorageType": mscExampleDashedIndicesStorageType,
       "mscExampleDashedIndicesOneIndex": mscExampleDashedIndicesOneIndex,
       "mscExampleDashedIndicesTwoIndex": mscExampleDashedIndicesTwoIndex,
       "mscExampleDashedIndicesThreeIndex": mscExampleDashedIndicesThreeIndex,
       "mscExampleDashedIndicesProvisionedTable": mscExampleDashedIndicesProvisionedTable,
       "mscExampleDashedIndicesProvisionedEntry": mscExampleDashedIndicesProvisionedEntry,
       "mscExampleDashedIndicesProvAttribute": mscExampleDashedIndicesProvAttribute,
       "mscExampleRequiredIndices": mscExampleRequiredIndices,
       "mscExampleRequiredIndicesRowStatusTable": mscExampleRequiredIndicesRowStatusTable,
       "mscExampleRequiredIndicesRowStatusEntry": mscExampleRequiredIndicesRowStatusEntry,
       "mscExampleRequiredIndicesRowStatus": mscExampleRequiredIndicesRowStatus,
       "mscExampleRequiredIndicesComponentName": mscExampleRequiredIndicesComponentName,
       "mscExampleRequiredIndicesStorageType": mscExampleRequiredIndicesStorageType,
       "mscExampleRequiredIndicesDecimalIndex": mscExampleRequiredIndicesDecimalIndex,
       "mscExampleRequiredIndicesEnumerationIndex": mscExampleRequiredIndicesEnumerationIndex,
       "mscExampleRequiredIndicesProvisionedTable": mscExampleRequiredIndicesProvisionedTable,
       "mscExampleRequiredIndicesProvisionedEntry": mscExampleRequiredIndicesProvisionedEntry,
       "mscExampleRequiredIndicesProvAttribute": mscExampleRequiredIndicesProvAttribute,
       "mscExampleNsap": mscExampleNsap,
       "mscExampleNsapRowStatusTable": mscExampleNsapRowStatusTable,
       "mscExampleNsapRowStatusEntry": mscExampleNsapRowStatusEntry,
       "mscExampleNsapRowStatus": mscExampleNsapRowStatus,
       "mscExampleNsapComponentName": mscExampleNsapComponentName,
       "mscExampleNsapStorageType": mscExampleNsapStorageType,
       "mscExampleNsapIndex": mscExampleNsapIndex,
       "mscExampleNsapAtmAddrTable": mscExampleNsapAtmAddrTable,
       "mscExampleNsapAtmAddrEntry": mscExampleNsapAtmAddrEntry,
       "mscExampleNsapNsapNativeAddress": mscExampleNsapNsapNativeAddress,
       "mscExampleNsapNativeTable": mscExampleNsapNativeTable,
       "mscExampleNsapNativeEntry": mscExampleNsapNativeEntry,
       "mscExampleNsapNativeIndex": mscExampleNsapNativeIndex,
       "mscExampleNsapNativeValue": mscExampleNsapNativeValue,
       "mscExampleOperationalTable": mscExampleOperationalTable,
       "mscExampleOperationalEntry": mscExampleOperationalEntry,
       "mscExampleOperMyComponentName": mscExampleOperMyComponentName,
       "mscExampleProvisionalTable": mscExampleProvisionalTable,
       "mscExampleProvisionalEntry": mscExampleProvisionalEntry,
       "mscExampleProvMyComponentName": mscExampleProvMyComponentName,
       "mscExampleOperDecimalSubCreatedTable": mscExampleOperDecimalSubCreatedTable,
       "mscExampleOperDecimalSubCreatedEntry": mscExampleOperDecimalSubCreatedEntry,
       "mscExampleOperDecimalSubCreatedValue": mscExampleOperDecimalSubCreatedValue,
       "mscExampleOperDecimalSubCreatedRowStatus": mscExampleOperDecimalSubCreatedRowStatus,
       "mscExampleOperFixedPtSubcomponentsCreatedTable": mscExampleOperFixedPtSubcomponentsCreatedTable,
       "mscExampleOperFixedPtSubcomponentsCreatedEntry": mscExampleOperFixedPtSubcomponentsCreatedEntry,
       "mscExampleOperFixedPtSubcomponentsCreatedValue": mscExampleOperFixedPtSubcomponentsCreatedValue,
       "mscExampleOperFixedPtSubcomponentsCreatedRowStatus": mscExampleOperFixedPtSubcomponentsCreatedRowStatus,
       "mscExampleOperStringSubCreatedTable": mscExampleOperStringSubCreatedTable,
       "mscExampleOperStringSubCreatedEntry": mscExampleOperStringSubCreatedEntry,
       "mscExampleOperStringSubCreatedValue": mscExampleOperStringSubCreatedValue,
       "mscExampleOperStringSubCreatedRowStatus": mscExampleOperStringSubCreatedRowStatus,
       "mscExampleOperEnumSubCreatedTable": mscExampleOperEnumSubCreatedTable,
       "mscExampleOperEnumSubCreatedEntry": mscExampleOperEnumSubCreatedEntry,
       "mscExampleOperEnumSubCreatedValue": mscExampleOperEnumSubCreatedValue,
       "mscExampleOperEnumSubCreatedRowStatus": mscExampleOperEnumSubCreatedRowStatus,
       "mscExampleOperSignedSubCreatedTable": mscExampleOperSignedSubCreatedTable,
       "mscExampleOperSignedSubCreatedEntry": mscExampleOperSignedSubCreatedEntry,
       "mscExampleOperSignedSubCreatedValue": mscExampleOperSignedSubCreatedValue,
       "mscExampleOperSignedSubCreatedRowStatus": mscExampleOperSignedSubCreatedRowStatus,
       "mscExampleProvDecimalSubCreatedTable": mscExampleProvDecimalSubCreatedTable,
       "mscExampleProvDecimalSubCreatedEntry": mscExampleProvDecimalSubCreatedEntry,
       "mscExampleProvDecimalSubCreatedValue": mscExampleProvDecimalSubCreatedValue,
       "mscExampleProvDecimalSubCreatedRowStatus": mscExampleProvDecimalSubCreatedRowStatus,
       "mscExampleProvFixedPtSubCreatedTable": mscExampleProvFixedPtSubCreatedTable,
       "mscExampleProvFixedPtSubCreatedEntry": mscExampleProvFixedPtSubCreatedEntry,
       "mscExampleProvFixedPtSubCreatedValue": mscExampleProvFixedPtSubCreatedValue,
       "mscExampleProvFixedPtSubCreatedRowStatus": mscExampleProvFixedPtSubCreatedRowStatus,
       "mscExampleProvSignedSubCreatedTable": mscExampleProvSignedSubCreatedTable,
       "mscExampleProvSignedSubCreatedEntry": mscExampleProvSignedSubCreatedEntry,
       "mscExampleProvSignedSubCreatedValue": mscExampleProvSignedSubCreatedValue,
       "mscExampleProvSignedSubCreatedRowStatus": mscExampleProvSignedSubCreatedRowStatus,
       "mscExampleProvStringSubCreatedTable": mscExampleProvStringSubCreatedTable,
       "mscExampleProvStringSubCreatedEntry": mscExampleProvStringSubCreatedEntry,
       "mscExampleProvStringSubCreatedValue": mscExampleProvStringSubCreatedValue,
       "mscExampleProvStringSubCreatedRowStatus": mscExampleProvStringSubCreatedRowStatus,
       "mscExampleProvEnumSubCreatedTable": mscExampleProvEnumSubCreatedTable,
       "mscExampleProvEnumSubCreatedEntry": mscExampleProvEnumSubCreatedEntry,
       "mscExampleProvEnumSubCreatedValue": mscExampleProvEnumSubCreatedValue,
       "mscExampleProvEnumSubCreatedRowStatus": mscExampleProvEnumSubCreatedRowStatus,
       "mscFri": mscFri,
       "mscFriRowStatusTable": mscFriRowStatusTable,
       "mscFriRowStatusEntry": mscFriRowStatusEntry,
       "mscFriRowStatus": mscFriRowStatus,
       "mscFriComponentName": mscFriComponentName,
       "mscFriStorageType": mscFriStorageType,
       "mscFriIndex": mscFriIndex,
       "mscFriDna": mscFriDna,
       "mscFriDnaRowStatusTable": mscFriDnaRowStatusTable,
       "mscFriDnaRowStatusEntry": mscFriDnaRowStatusEntry,
       "mscFriDnaRowStatus": mscFriDnaRowStatus,
       "mscFriDnaComponentName": mscFriDnaComponentName,
       "mscFriDnaStorageType": mscFriDnaStorageType,
       "mscFriDnaIndex": mscFriDnaIndex,
       "mscFriDnaOperationalTable": mscFriDnaOperationalTable,
       "mscFriDnaOperationalEntry": mscFriDnaOperationalEntry,
       "mscFriDnaAttribute": mscFriDnaAttribute,
       "mscFriDnaProvisionalTable": mscFriDnaProvisionalTable,
       "mscFriDnaProvisionalEntry": mscFriDnaProvisionalEntry,
       "mscFriDnaTypeOfAddress": mscFriDnaTypeOfAddress,
       "mscFriDnaNumberPlanIndicator": mscFriDnaNumberPlanIndicator,
       "mscFriDnaDataNetworkAddress": mscFriDnaDataNetworkAddress,
       "mscFriDynamic": mscFriDynamic,
       "mscFriDynamicRowStatusTable": mscFriDynamicRowStatusTable,
       "mscFriDynamicRowStatusEntry": mscFriDynamicRowStatusEntry,
       "mscFriDynamicRowStatus": mscFriDynamicRowStatus,
       "mscFriDynamicComponentName": mscFriDynamicComponentName,
       "mscFriDynamicStorageType": mscFriDynamicStorageType,
       "mscFriDynamicIndex": mscFriDynamicIndex,
       "mscFriDynamicOperationalTable": mscFriDynamicOperationalTable,
       "mscFriDynamicOperationalEntry": mscFriDynamicOperationalEntry,
       "mscFriDynamicAttribute": mscFriDynamicAttribute,
       "mscFriDynOp": mscFriDynOp,
       "mscFriDynOpRowStatusTable": mscFriDynOpRowStatusTable,
       "mscFriDynOpRowStatusEntry": mscFriDynOpRowStatusEntry,
       "mscFriDynOpRowStatus": mscFriDynOpRowStatus,
       "mscFriDynOpComponentName": mscFriDynOpComponentName,
       "mscFriDynOpStorageType": mscFriDynOpStorageType,
       "mscFriDynOpIndex": mscFriDynOpIndex,
       "mscFriDynOpInitial": mscFriDynOpInitial,
       "mscFriDynOpInitialRowStatusTable": mscFriDynOpInitialRowStatusTable,
       "mscFriDynOpInitialRowStatusEntry": mscFriDynOpInitialRowStatusEntry,
       "mscFriDynOpInitialRowStatus": mscFriDynOpInitialRowStatus,
       "mscFriDynOpInitialComponentName": mscFriDynOpInitialComponentName,
       "mscFriDynOpInitialStorageType": mscFriDynOpInitialStorageType,
       "mscFriDynOpInitialIndex": mscFriDynOpInitialIndex,
       "mscFriDynOpInitialOperationalTable": mscFriDynOpInitialOperationalTable,
       "mscFriDynOpInitialOperationalEntry": mscFriDynOpInitialOperationalEntry,
       "mscFriDynOpInitialAttribute": mscFriDynOpInitialAttribute,
       "mscFriDynOpInitialProvisionedTable": mscFriDynOpInitialProvisionedTable,
       "mscFriDynOpInitialProvisionedEntry": mscFriDynOpInitialProvisionedEntry,
       "mscFriDynOpInitialProvAttribute": mscFriDynOpInitialProvAttribute,
       "mscFriDynOpOptional": mscFriDynOpOptional,
       "mscFriDynOpOptionalRowStatusTable": mscFriDynOpOptionalRowStatusTable,
       "mscFriDynOpOptionalRowStatusEntry": mscFriDynOpOptionalRowStatusEntry,
       "mscFriDynOpOptionalRowStatus": mscFriDynOpOptionalRowStatus,
       "mscFriDynOpOptionalComponentName": mscFriDynOpOptionalComponentName,
       "mscFriDynOpOptionalStorageType": mscFriDynOpOptionalStorageType,
       "mscFriDynOpOptionalIndex": mscFriDynOpOptionalIndex,
       "mscFriDynOpOptionalOperationalTable": mscFriDynOpOptionalOperationalTable,
       "mscFriDynOpOptionalOperationalEntry": mscFriDynOpOptionalOperationalEntry,
       "mscFriDynOpOptionalAttribute": mscFriDynOpOptionalAttribute,
       "mscFriDynOpOptionalProvisionedTable": mscFriDynOpOptionalProvisionedTable,
       "mscFriDynOpOptionalProvisionedEntry": mscFriDynOpOptionalProvisionedEntry,
       "mscFriDynOpOptionalProvAttribute": mscFriDynOpOptionalProvAttribute,
       "mscFriDynOpDynamic": mscFriDynOpDynamic,
       "mscFriDynOpDynamicRowStatusTable": mscFriDynOpDynamicRowStatusTable,
       "mscFriDynOpDynamicRowStatusEntry": mscFriDynOpDynamicRowStatusEntry,
       "mscFriDynOpDynamicRowStatus": mscFriDynOpDynamicRowStatus,
       "mscFriDynOpDynamicComponentName": mscFriDynOpDynamicComponentName,
       "mscFriDynOpDynamicStorageType": mscFriDynOpDynamicStorageType,
       "mscFriDynOpDynamicIndex": mscFriDynOpDynamicIndex,
       "mscFriDynOpDynamicOperationalTable": mscFriDynOpDynamicOperationalTable,
       "mscFriDynOpDynamicOperationalEntry": mscFriDynOpDynamicOperationalEntry,
       "mscFriDynOpDynamicAttribute": mscFriDynOpDynamicAttribute,
       "mscFriDynOpDynOpJr": mscFriDynOpDynOpJr,
       "mscFriDynOpDynOpJrRowStatusTable": mscFriDynOpDynOpJrRowStatusTable,
       "mscFriDynOpDynOpJrRowStatusEntry": mscFriDynOpDynOpJrRowStatusEntry,
       "mscFriDynOpDynOpJrRowStatus": mscFriDynOpDynOpJrRowStatus,
       "mscFriDynOpDynOpJrComponentName": mscFriDynOpDynOpJrComponentName,
       "mscFriDynOpDynOpJrStorageType": mscFriDynOpDynOpJrStorageType,
       "mscFriDynOpDynOpJrIndex": mscFriDynOpDynOpJrIndex,
       "mscFriDynOpDynOpJrOperationalTable": mscFriDynOpDynOpJrOperationalTable,
       "mscFriDynOpDynOpJrOperationalEntry": mscFriDynOpDynOpJrOperationalEntry,
       "mscFriDynOpDynOpJrAttribute": mscFriDynOpDynOpJrAttribute,
       "mscFriDynOpOperationalTable": mscFriDynOpOperationalTable,
       "mscFriDynOpOperationalEntry": mscFriDynOpOperationalEntry,
       "mscFriDynOpAttribute": mscFriDynOpAttribute,
       "mscFriEvent": mscFriEvent,
       "mscFriEventRowStatusTable": mscFriEventRowStatusTable,
       "mscFriEventRowStatusEntry": mscFriEventRowStatusEntry,
       "mscFriEventRowStatus": mscFriEventRowStatus,
       "mscFriEventComponentName": mscFriEventComponentName,
       "mscFriEventStorageType": mscFriEventStorageType,
       "mscFriEventIndex": mscFriEventIndex,
       "mscFriRegistered": mscFriRegistered,
       "mscFriRegisteredRowStatusTable": mscFriRegisteredRowStatusTable,
       "mscFriRegisteredRowStatusEntry": mscFriRegisteredRowStatusEntry,
       "mscFriRegisteredRowStatus": mscFriRegisteredRowStatus,
       "mscFriRegisteredComponentName": mscFriRegisteredComponentName,
       "mscFriRegisteredStorageType": mscFriRegisteredStorageType,
       "mscFriRegisteredIndex": mscFriRegisteredIndex,
       "mscFriRegisteredDataTable": mscFriRegisteredDataTable,
       "mscFriRegisteredDataEntry": mscFriRegisteredDataEntry,
       "mscFriRegisteredAttribute": mscFriRegisteredAttribute,
       "mscFriOperationalTable": mscFriOperationalTable,
       "mscFriOperationalEntry": mscFriOperationalEntry,
       "mscFriOperationalFreeSimpleAscii": mscFriOperationalFreeSimpleAscii,
       "mscFriOperationalFreeSimpleDashed": mscFriOperationalFreeSimpleDashed,
       "mscFriOperationalFreeSimpleExtended": mscFriOperationalFreeSimpleExtended,
       "mscFriOperationalFreeSimpleBcd": mscFriOperationalFreeSimpleBcd,
       "mscFriOperationalFreeSimpleSigned": mscFriOperationalFreeSimpleSigned,
       "mscFriOperationalFreeSimpleFixed": mscFriOperationalFreeSimpleFixed,
       "mscFriOperationalFreeSimpleSequence": mscFriOperationalFreeSimpleSequence,
       "mscFriOperationalFreeSimpleObjId": mscFriOperationalFreeSimpleObjId,
       "mscFriOperationalFreeSimpleComponent": mscFriOperationalFreeSimpleComponent,
       "mscFriOperationalFreeSimpleHex": mscFriOperationalFreeSimpleHex,
       "mscFriOperationalStructSetEnumeration": mscFriOperationalStructSetEnumeration,
       "mscFriOperationalStructSetUnsigned": mscFriOperationalStructSetUnsigned,
       "mscFriOperationalStructSimpleAscii": mscFriOperationalStructSimpleAscii,
       "mscFriOperationalStructSimpleDashed": mscFriOperationalStructSimpleDashed,
       "mscFriOperationalStructSimpleExtended": mscFriOperationalStructSimpleExtended,
       "mscFriOperationalStructSimpleBcd": mscFriOperationalStructSimpleBcd,
       "mscFriOperationalStructSimpleSigned": mscFriOperationalStructSimpleSigned,
       "mscFriOperationalStructSimpleFixed": mscFriOperationalStructSimpleFixed,
       "mscFriOperationalStructSimpleSequence": mscFriOperationalStructSimpleSequence,
       "mscFriOperationalStructSimpleEnum": mscFriOperationalStructSimpleEnum,
       "mscFriOperationalStructSimpleHex": mscFriOperationalStructSimpleHex,
       "mscFriOperationalStructSimpleUnsigned": mscFriOperationalStructSimpleUnsigned,
       "mscFriProvisionalTable": mscFriProvisionalTable,
       "mscFriProvisionalEntry": mscFriProvisionalEntry,
       "mscFriProvisionalStructSetEnumeration": mscFriProvisionalStructSetEnumeration,
       "mscFriProvisionalStructSetUnsigned": mscFriProvisionalStructSetUnsigned,
       "mscFriProvisionalStructSimpleAscii": mscFriProvisionalStructSimpleAscii,
       "mscFriProvisionalStructSimpleDashed": mscFriProvisionalStructSimpleDashed,
       "mscFriProvisionalStructSimpleExtended": mscFriProvisionalStructSimpleExtended,
       "mscFriProvisionalStructSimpleBcd": mscFriProvisionalStructSimpleBcd,
       "mscFriProvisionalStructSimpleSequence": mscFriProvisionalStructSimpleSequence,
       "mscFriProvisionalStructSimpleEnum": mscFriProvisionalStructSimpleEnum,
       "mscFriProvisionalStructSimpleHex": mscFriProvisionalStructSimpleHex,
       "mscFriProvisionalStructSimpleUnsigned": mscFriProvisionalStructSimpleUnsigned,
       "mscFriProvisionalStructSimpleSigned": mscFriProvisionalStructSimpleSigned,
       "mscFriProvisionalStructSimpleFixed": mscFriProvisionalStructSimpleFixed,
       "mscFriProvisionalFreeSimpleAscii": mscFriProvisionalFreeSimpleAscii,
       "mscFriProvisionalFreeSimpleDashed": mscFriProvisionalFreeSimpleDashed,
       "mscFriProvisionalFreeSimpleExtended": mscFriProvisionalFreeSimpleExtended,
       "mscFriProvisionalFreeSimpleBcd": mscFriProvisionalFreeSimpleBcd,
       "mscFriProvisionalFreeSimpleSequence": mscFriProvisionalFreeSimpleSequence,
       "mscFriProvisionalFreeSimpleSigned": mscFriProvisionalFreeSimpleSigned,
       "mscFriProvisionalFreeSimpleFixed": mscFriProvisionalFreeSimpleFixed,
       "mscFriProvisionalFreeSimpleObjId": mscFriProvisionalFreeSimpleObjId,
       "mscFriProvisionalFreeSimpleComponent": mscFriProvisionalFreeSimpleComponent,
       "mscFriProvisionalFreeSimpleHex": mscFriProvisionalFreeSimpleHex,
       "mscFriEscapeCheckAttribute": mscFriEscapeCheckAttribute,
       "mscFriEscapeDefaultsComponent": mscFriEscapeDefaultsComponent,
       "mscFriEscapeDefaultsGroup": mscFriEscapeDefaultsGroup,
       "mscFriEscapeSet": mscFriEscapeSet,
       "mscFriEscapeCopyComponent": mscFriEscapeCopyComponent,
       "mscFriEscapeCopyGroup": mscFriEscapeCopyGroup,
       "mscFriEscapeCopyAttribute": mscFriEscapeCopyAttribute,
       "mscFriStateTable": mscFriStateTable,
       "mscFriStateEntry": mscFriStateEntry,
       "mscFriAdminState": mscFriAdminState,
       "mscFriOperationalState": mscFriOperationalState,
       "mscFriUsageState": mscFriUsageState,
       "mscFriAvailabilityStatus": mscFriAvailabilityStatus,
       "mscFriProceduralStatus": mscFriProceduralStatus,
       "mscFriControlStatus": mscFriControlStatus,
       "mscFriAlarmStatus": mscFriAlarmStatus,
       "mscFriStandbyStatus": mscFriStandbyStatus,
       "mscFriUnknownStatus": mscFriUnknownStatus,
       "mscFriPfListAsciiTable": mscFriPfListAsciiTable,
       "mscFriPfListAsciiEntry": mscFriPfListAsciiEntry,
       "mscFriPfListAsciiValue": mscFriPfListAsciiValue,
       "mscFriPfListAsciiRowStatus": mscFriPfListAsciiRowStatus,
       "mscFriPfListUnsignedTable": mscFriPfListUnsignedTable,
       "mscFriPfListUnsignedEntry": mscFriPfListUnsignedEntry,
       "mscFriPfListUnsignedValue": mscFriPfListUnsignedValue,
       "mscFriPfListUnsignedRowStatus": mscFriPfListUnsignedRowStatus,
       "mscFriPfListFixedTable": mscFriPfListFixedTable,
       "mscFriPfListFixedEntry": mscFriPfListFixedEntry,
       "mscFriPfListFixedValue": mscFriPfListFixedValue,
       "mscFriPfListFixedRowStatus": mscFriPfListFixedRowStatus,
       "mscFriPfListSignedTable": mscFriPfListSignedTable,
       "mscFriPfListSignedEntry": mscFriPfListSignedEntry,
       "mscFriPfListSignedValue": mscFriPfListSignedValue,
       "mscFriPfListSignedRowStatus": mscFriPfListSignedRowStatus,
       "mscFriOfListComponentTable": mscFriOfListComponentTable,
       "mscFriOfListComponentEntry": mscFriOfListComponentEntry,
       "mscFriOfListComponentValue": mscFriOfListComponentValue,
       "mscFriOfListComponentRowStatus": mscFriOfListComponentRowStatus,
       "mscFriOfListEnumerationTable": mscFriOfListEnumerationTable,
       "mscFriOfListEnumerationEntry": mscFriOfListEnumerationEntry,
       "mscFriOfListEnumerationValue": mscFriOfListEnumerationValue,
       "mscFriOfListEnumerationRowStatus": mscFriOfListEnumerationRowStatus,
       "mscRegistered": mscRegistered,
       "mscRegisteredRowStatusTable": mscRegisteredRowStatusTable,
       "mscRegisteredRowStatusEntry": mscRegisteredRowStatusEntry,
       "mscRegisteredRowStatus": mscRegisteredRowStatus,
       "mscRegisteredComponentName": mscRegisteredComponentName,
       "mscRegisteredStorageType": mscRegisteredStorageType,
       "mscRegisteredIndex": mscRegisteredIndex,
       "mscRegisteredDataTable": mscRegisteredDataTable,
       "mscRegisteredDataEntry": mscRegisteredDataEntry,
       "mscRegisteredAttribute": mscRegisteredAttribute,
       "casTestMIB": casTestMIB,
       "casTestGroup": casTestGroup,
       "casTestGroupCA": casTestGroupCA,
       "casTestGroupCA02": casTestGroupCA02,
       "casTestGroupCA02A": casTestGroupCA02A,
       "casTestCapabilities": casTestCapabilities,
       "casTestCapabilitiesCA": casTestCapabilitiesCA,
       "casTestCapabilitiesCA02": casTestCapabilitiesCA02,
       "casTestCapabilitiesCA02A": casTestCapabilitiesCA02A}
)
