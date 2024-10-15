# SNMP MIB module (CISCO-VISM-DSX0-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-DSX0-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:50 2024
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

(cardSpecific,
 dsx0Vism) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardSpecific",
    "dsx0Vism")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVismDsx0MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 81)
)
ciscoVismDsx0MIB.setRevisions(
        ("2004-03-11 00:00",
         "2003-08-03 00:00",
         "2003-06-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismDs0CardStats_ObjectIdentity = ObjectIdentity
vismDs0CardStats = _VismDs0CardStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24)
)


class _VismTotalDs0Count_Type(Integer32):
    """Custom type vismTotalDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismTotalDs0Count_Type.__name__ = "Integer32"
_VismTotalDs0Count_Object = MibScalar
vismTotalDs0Count = _VismTotalDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24, 1),
    _VismTotalDs0Count_Type()
)
vismTotalDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismTotalDs0Count.setStatus("current")


class _VismFreeDs0Count_Type(Integer32):
    """Custom type vismFreeDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismFreeDs0Count_Type.__name__ = "Integer32"
_VismFreeDs0Count_Object = MibScalar
vismFreeDs0Count = _VismFreeDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24, 2),
    _VismFreeDs0Count_Type()
)
vismFreeDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismFreeDs0Count.setStatus("current")


class _VismActiveDs0Count_Type(Integer32):
    """Custom type vismActiveDs0Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismActiveDs0Count_Type.__name__ = "Integer32"
_VismActiveDs0Count_Object = MibScalar
vismActiveDs0Count = _VismActiveDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24, 3),
    _VismActiveDs0Count_Type()
)
vismActiveDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismActiveDs0Count.setStatus("current")


class _VismBlockDs0Count_Type(Integer32):
    """Custom type vismBlockDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismBlockDs0Count_Type.__name__ = "Integer32"
_VismBlockDs0Count_Object = MibScalar
vismBlockDs0Count = _VismBlockDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24, 4),
    _VismBlockDs0Count_Type()
)
vismBlockDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismBlockDs0Count.setStatus("current")


class _VismActiveHighWaterMark_Type(Integer32):
    """Custom type vismActiveHighWaterMark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismActiveHighWaterMark_Type.__name__ = "Integer32"
_VismActiveHighWaterMark_Object = MibScalar
vismActiveHighWaterMark = _VismActiveHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24, 5),
    _VismActiveHighWaterMark_Type()
)
vismActiveHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismActiveHighWaterMark.setStatus("current")


class _VismDs0CardStatsClrButton_Type(Integer32):
    """Custom type vismDs0CardStatsClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_VismDs0CardStatsClrButton_Type.__name__ = "Integer32"
_VismDs0CardStatsClrButton_Object = MibScalar
vismDs0CardStatsClrButton = _VismDs0CardStatsClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 24, 6),
    _VismDs0CardStatsClrButton_Type()
)
vismDs0CardStatsClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDs0CardStatsClrButton.setStatus("current")
_Dsx0VismCnfTable_Object = MibTable
dsx0VismCnfTable = _Dsx0VismCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1)
)
if mibBuilder.loadTexts:
    dsx0VismCnfTable.setStatus("current")
_Dsx0VismCnfEntry_Object = MibTableRow
dsx0VismCnfEntry = _Dsx0VismCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1)
)
dsx0VismCnfEntry.setIndexNames(
    (0, "CISCO-VISM-DSX0-MIB", "ds0IfIndex"),
)
if mibBuilder.loadTexts:
    dsx0VismCnfEntry.setStatus("current")


class _Ds0IfIndex_Type(Integer32):
    """Custom type ds0IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_Ds0IfIndex_Type.__name__ = "Integer32"
_Ds0IfIndex_Object = MibTableColumn
ds0IfIndex = _Ds0IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 1),
    _Ds0IfIndex_Type()
)
ds0IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0IfIndex.setStatus("current")
_Ds0RobbedBitSignalling_Type = TruthValue
_Ds0RobbedBitSignalling_Object = MibTableColumn
ds0RobbedBitSignalling = _Ds0RobbedBitSignalling_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 2),
    _Ds0RobbedBitSignalling_Type()
)
ds0RobbedBitSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0RobbedBitSignalling.setStatus("current")


class _Ds0IdleCode_Type(Integer32):
    """Custom type ds0IdleCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ds0IdleCode_Type.__name__ = "Integer32"
_Ds0IdleCode_Object = MibTableColumn
ds0IdleCode = _Ds0IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 3),
    _Ds0IdleCode_Type()
)
ds0IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0IdleCode.setStatus("current")


class _Ds0SeizedCode_Type(Integer32):
    """Custom type ds0SeizedCode based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ds0SeizedCode_Type.__name__ = "Integer32"
_Ds0SeizedCode_Object = MibTableColumn
ds0SeizedCode = _Ds0SeizedCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 4),
    _Ds0SeizedCode_Type()
)
ds0SeizedCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0SeizedCode.setStatus("current")


class _Ds0ReceivedCode_Type(Integer32):
    """Custom type ds0ReceivedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ds0ReceivedCode_Type.__name__ = "Integer32"
_Ds0ReceivedCode_Object = MibTableColumn
ds0ReceivedCode = _Ds0ReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 5),
    _Ds0ReceivedCode_Type()
)
ds0ReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0ReceivedCode.setStatus("current")


class _Ds0TransmitCodesEnable_Type(TruthValue):
    """Custom type ds0TransmitCodesEnable based on TruthValue"""


_Ds0TransmitCodesEnable_Object = MibTableColumn
ds0TransmitCodesEnable = _Ds0TransmitCodesEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 6),
    _Ds0TransmitCodesEnable_Type()
)
ds0TransmitCodesEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0TransmitCodesEnable.setStatus("deprecated")


class _Ds0BundleMapped_Type(Integer32):
    """Custom type ds0BundleMapped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Ds0BundleMapped_Type.__name__ = "Integer32"
_Ds0BundleMapped_Object = MibTableColumn
ds0BundleMapped = _Ds0BundleMapped_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 7),
    _Ds0BundleMapped_Type()
)
ds0BundleMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0BundleMapped.setStatus("current")


class _Ds0IfType_Type(Integer32):
    """Custom type ds0IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              63,
              81)
        )
    )
    namedValues = NamedValues(
        *(("bearer", 81),
          ("ccs-signaling", 63),
          ("unknown", 1))
    )


_Ds0IfType_Type.__name__ = "Integer32"
_Ds0IfType_Object = MibTableColumn
ds0IfType = _Ds0IfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 8),
    _Ds0IfType_Type()
)
ds0IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0IfType.setStatus("current")


class _Ds0CasVariantName_Type(DisplayString):
    """Custom type ds0CasVariantName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ds0CasVariantName_Type.__name__ = "DisplayString"
_Ds0CasVariantName_Object = MibTableColumn
ds0CasVariantName = _Ds0CasVariantName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 9),
    _Ds0CasVariantName_Type()
)
ds0CasVariantName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasVariantName.setStatus("current")


class _Ds0CasCadenceOnTime_Type(Integer32):
    """Custom type ds0CasCadenceOnTime based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9999),
    )


_Ds0CasCadenceOnTime_Type.__name__ = "Integer32"
_Ds0CasCadenceOnTime_Object = MibTableColumn
ds0CasCadenceOnTime = _Ds0CasCadenceOnTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 10),
    _Ds0CasCadenceOnTime_Type()
)
ds0CasCadenceOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasCadenceOnTime.setStatus("current")


class _Ds0CasCadenceOffTime_Type(Integer32):
    """Custom type ds0CasCadenceOffTime based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Ds0CasCadenceOffTime_Type.__name__ = "Integer32"
_Ds0CasCadenceOffTime_Object = MibTableColumn
ds0CasCadenceOffTime = _Ds0CasCadenceOffTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 11),
    _Ds0CasCadenceOffTime_Type()
)
ds0CasCadenceOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasCadenceOffTime.setStatus("current")


class _Ds0InsertLocalCas_Type(TruthValue):
    """Custom type ds0InsertLocalCas based on TruthValue"""


_Ds0InsertLocalCas_Object = MibTableColumn
ds0InsertLocalCas = _Ds0InsertLocalCas_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 12),
    _Ds0InsertLocalCas_Type()
)
ds0InsertLocalCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0InsertLocalCas.setStatus("current")


class _Ds0LocalCasPattern_Type(Integer32):
    """Custom type ds0LocalCasPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ds0LocalCasPattern_Type.__name__ = "Integer32"
_Ds0LocalCasPattern_Object = MibTableColumn
ds0LocalCasPattern = _Ds0LocalCasPattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 13),
    _Ds0LocalCasPattern_Type()
)
ds0LocalCasPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0LocalCasPattern.setStatus("current")


class _Ds0LoopbackCommand_Type(Integer32):
    """Custom type ds0LoopbackCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localLoop", 3),
          ("noLoop", 1),
          ("remoteLoop", 2))
    )


_Ds0LoopbackCommand_Type.__name__ = "Integer32"
_Ds0LoopbackCommand_Object = MibTableColumn
ds0LoopbackCommand = _Ds0LoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 14),
    _Ds0LoopbackCommand_Type()
)
ds0LoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0LoopbackCommand.setStatus("current")


class _Ds0CasParameterSource_Type(Integer32):
    """Custom type ds0CasParameterSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("casAppl", 1),
          ("mibValue", 2))
    )


_Ds0CasParameterSource_Type.__name__ = "Integer32"
_Ds0CasParameterSource_Object = MibTableColumn
ds0CasParameterSource = _Ds0CasParameterSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 15),
    _Ds0CasParameterSource_Type()
)
ds0CasParameterSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasParameterSource.setStatus("current")


class _Ds0CasOnHookMinMakeTime_Type(Integer32):
    """Custom type ds0CasOnHookMinMakeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasOnHookMinMakeTime_Type.__name__ = "Integer32"
_Ds0CasOnHookMinMakeTime_Object = MibTableColumn
ds0CasOnHookMinMakeTime = _Ds0CasOnHookMinMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 16),
    _Ds0CasOnHookMinMakeTime_Type()
)
ds0CasOnHookMinMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasOnHookMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasOnHookMinMakeTime.setUnits("milliseconds")


class _Ds0CasOffHookMinMakeTime_Type(Integer32):
    """Custom type ds0CasOffHookMinMakeTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasOffHookMinMakeTime_Type.__name__ = "Integer32"
_Ds0CasOffHookMinMakeTime_Object = MibTableColumn
ds0CasOffHookMinMakeTime = _Ds0CasOffHookMinMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 17),
    _Ds0CasOffHookMinMakeTime_Type()
)
ds0CasOffHookMinMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasOffHookMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasOffHookMinMakeTime.setUnits("milliseconds")


class _Ds0CasWinkMinMakeTime_Type(Integer32):
    """Custom type ds0CasWinkMinMakeTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasWinkMinMakeTime_Type.__name__ = "Integer32"
_Ds0CasWinkMinMakeTime_Object = MibTableColumn
ds0CasWinkMinMakeTime = _Ds0CasWinkMinMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 18),
    _Ds0CasWinkMinMakeTime_Type()
)
ds0CasWinkMinMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasWinkMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasWinkMinMakeTime.setUnits("milliseconds")


class _Ds0CasWinkMaxMakeTime_Type(Integer32):
    """Custom type ds0CasWinkMaxMakeTime based on Integer32"""
    defaultValue = 350

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasWinkMaxMakeTime_Type.__name__ = "Integer32"
_Ds0CasWinkMaxMakeTime_Object = MibTableColumn
ds0CasWinkMaxMakeTime = _Ds0CasWinkMaxMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 19),
    _Ds0CasWinkMaxMakeTime_Type()
)
ds0CasWinkMaxMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasWinkMaxMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasWinkMaxMakeTime.setUnits("millisesconds")


class _Ds0CasWinkBreakTime_Type(Integer32):
    """Custom type ds0CasWinkBreakTime based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasWinkBreakTime_Type.__name__ = "Integer32"
_Ds0CasWinkBreakTime_Object = MibTableColumn
ds0CasWinkBreakTime = _Ds0CasWinkBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 20),
    _Ds0CasWinkBreakTime_Type()
)
ds0CasWinkBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasWinkBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasWinkBreakTime.setUnits("milliseconds")


class _Ds0CasGlareTime_Type(Integer32):
    """Custom type ds0CasGlareTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasGlareTime_Type.__name__ = "Integer32"
_Ds0CasGlareTime_Object = MibTableColumn
ds0CasGlareTime = _Ds0CasGlareTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 21),
    _Ds0CasGlareTime_Type()
)
ds0CasGlareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasGlareTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasGlareTime.setUnits("milliseconds")


class _Ds0CasGaurdTime_Type(Integer32):
    """Custom type ds0CasGaurdTime based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasGaurdTime_Type.__name__ = "Integer32"
_Ds0CasGaurdTime_Object = MibTableColumn
ds0CasGaurdTime = _Ds0CasGaurdTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 22),
    _Ds0CasGaurdTime_Type()
)
ds0CasGaurdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasGaurdTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasGaurdTime.setUnits("milliseconds")


class _Ds0CasDelayImmedStart_Type(Integer32):
    """Custom type ds0CasDelayImmedStart based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ds0CasDelayImmedStart_Type.__name__ = "Integer32"
_Ds0CasDelayImmedStart_Object = MibTableColumn
ds0CasDelayImmedStart = _Ds0CasDelayImmedStart_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 23),
    _Ds0CasDelayImmedStart_Type()
)
ds0CasDelayImmedStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasDelayImmedStart.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasDelayImmedStart.setUnits("milliseconds")


class _Ds0SignalingType_Type(Integer32):
    """Custom type ds0SignalingType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cas", 1),
          ("ccs", 2),
          ("none", 3))
    )


_Ds0SignalingType_Type.__name__ = "Integer32"
_Ds0SignalingType_Object = MibTableColumn
ds0SignalingType = _Ds0SignalingType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 24),
    _Ds0SignalingType_Type()
)
ds0SignalingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0SignalingType.setStatus("current")


class _Ds0CasMinDelayDialTime_Type(Integer32):
    """Custom type ds0CasMinDelayDialTime based on Integer32"""
    defaultValue = 100


_Ds0CasMinDelayDialTime_Object = MibTableColumn
ds0CasMinDelayDialTime = _Ds0CasMinDelayDialTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 25),
    _Ds0CasMinDelayDialTime_Type()
)
ds0CasMinDelayDialTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasMinDelayDialTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasMinDelayDialTime.setUnits("milliseconds")


class _Ds0CasMinStartDialTime_Type(Integer32):
    """Custom type ds0CasMinStartDialTime based on Integer32"""
    defaultValue = 70


_Ds0CasMinStartDialTime_Object = MibTableColumn
ds0CasMinStartDialTime = _Ds0CasMinStartDialTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 26),
    _Ds0CasMinStartDialTime_Type()
)
ds0CasMinStartDialTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasMinStartDialTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasMinStartDialTime.setUnits("milliseconds")


class _Ds0CasFlashMinMakeTime_Type(Integer32):
    """Custom type ds0CasFlashMinMakeTime based on Integer32"""
    defaultValue = 300


_Ds0CasFlashMinMakeTime_Object = MibTableColumn
ds0CasFlashMinMakeTime = _Ds0CasFlashMinMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 27),
    _Ds0CasFlashMinMakeTime_Type()
)
ds0CasFlashMinMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasFlashMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasFlashMinMakeTime.setUnits("milliseconds")


class _Ds0CasFlashMaxMakeTime_Type(Integer32):
    """Custom type ds0CasFlashMaxMakeTime based on Integer32"""
    defaultValue = 1400


_Ds0CasFlashMaxMakeTime_Object = MibTableColumn
ds0CasFlashMaxMakeTime = _Ds0CasFlashMaxMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 28),
    _Ds0CasFlashMaxMakeTime_Type()
)
ds0CasFlashMaxMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasFlashMaxMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ds0CasFlashMaxMakeTime.setUnits("milliseconds")


class _Ds0CasDirectionality_Type(Integer32):
    """Custom type ds0CasDirectionality based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_Ds0CasDirectionality_Type.__name__ = "Integer32"
_Ds0CasDirectionality_Object = MibTableColumn
ds0CasDirectionality = _Ds0CasDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 29),
    _Ds0CasDirectionality_Type()
)
ds0CasDirectionality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasDirectionality.setStatus("current")


class _Ds0CasGlarePolicy_Type(Integer32):
    """Custom type ds0CasGlarePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlling", 1),
          ("releasing", 2))
    )


_Ds0CasGlarePolicy_Type.__name__ = "Integer32"
_Ds0CasGlarePolicy_Object = MibTableColumn
ds0CasGlarePolicy = _Ds0CasGlarePolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 30),
    _Ds0CasGlarePolicy_Type()
)
ds0CasGlarePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasGlarePolicy.setStatus("current")


class _Ds0CasIncomingMgcpPackage_Type(DisplayString):
    """Custom type ds0CasIncomingMgcpPackage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ds0CasIncomingMgcpPackage_Type.__name__ = "DisplayString"
_Ds0CasIncomingMgcpPackage_Object = MibTableColumn
ds0CasIncomingMgcpPackage = _Ds0CasIncomingMgcpPackage_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 31),
    _Ds0CasIncomingMgcpPackage_Type()
)
ds0CasIncomingMgcpPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasIncomingMgcpPackage.setStatus("current")


class _Ds0CasOutgoingMgcpPackage_Type(DisplayString):
    """Custom type ds0CasOutgoingMgcpPackage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ds0CasOutgoingMgcpPackage_Type.__name__ = "DisplayString"
_Ds0CasOutgoingMgcpPackage_Object = MibTableColumn
ds0CasOutgoingMgcpPackage = _Ds0CasOutgoingMgcpPackage_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 32),
    _Ds0CasOutgoingMgcpPackage_Type()
)
ds0CasOutgoingMgcpPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0CasOutgoingMgcpPackage.setStatus("current")


class _Ds0InputGain_Type(Integer32):
    """Custom type ds0InputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 14),
    )


_Ds0InputGain_Type.__name__ = "Integer32"
_Ds0InputGain_Object = MibTableColumn
ds0InputGain = _Ds0InputGain_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 33),
    _Ds0InputGain_Type()
)
ds0InputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0InputGain.setStatus("current")
if mibBuilder.loadTexts:
    ds0InputGain.setUnits("dB - decibel")


class _Ds0OutputAttenuation_Type(Integer32):
    """Custom type ds0OutputAttenuation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_Ds0OutputAttenuation_Type.__name__ = "Integer32"
_Ds0OutputAttenuation_Object = MibTableColumn
ds0OutputAttenuation = _Ds0OutputAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 34),
    _Ds0OutputAttenuation_Type()
)
ds0OutputAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0OutputAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    ds0OutputAttenuation.setUnits("dB - decibel")


class _Ds0MusicThreshold_Type(Integer32):
    """Custom type ds0MusicThreshold based on Integer32"""
    defaultValue = -38

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_Ds0MusicThreshold_Type.__name__ = "Integer32"
_Ds0MusicThreshold_Object = MibTableColumn
ds0MusicThreshold = _Ds0MusicThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 35),
    _Ds0MusicThreshold_Type()
)
ds0MusicThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0MusicThreshold.setStatus("current")


class _Ds0SidPacket_Type(TruthValue):
    """Custom type ds0SidPacket based on TruthValue"""


_Ds0SidPacket_Object = MibTableColumn
ds0SidPacket = _Ds0SidPacket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 36),
    _Ds0SidPacket_Type()
)
ds0SidPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0SidPacket.setStatus("current")


class _Ds0ExecDiag_Type(TruthValue):
    """Custom type ds0ExecDiag based on TruthValue"""


_Ds0ExecDiag_Object = MibTableColumn
ds0ExecDiag = _Ds0ExecDiag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 37),
    _Ds0ExecDiag_Type()
)
ds0ExecDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0ExecDiag.setStatus("current")


class _Ds0Companding_Type(Integer32):
    """Custom type ds0Companding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_Ds0Companding_Type.__name__ = "Integer32"
_Ds0Companding_Object = MibTableColumn
ds0Companding = _Ds0Companding_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 38),
    _Ds0Companding_Type()
)
ds0Companding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0Companding.setStatus("current")
_Ds0RxCasTransTblName_Type = DisplayString
_Ds0RxCasTransTblName_Object = MibTableColumn
ds0RxCasTransTblName = _Ds0RxCasTransTblName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 39),
    _Ds0RxCasTransTblName_Type()
)
ds0RxCasTransTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0RxCasTransTblName.setStatus("current")
_Ds0TxCasTransTblName_Type = DisplayString
_Ds0TxCasTransTblName_Object = MibTableColumn
ds0TxCasTransTblName = _Ds0TxCasTransTblName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 40),
    _Ds0TxCasTransTblName_Type()
)
ds0TxCasTransTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0TxCasTransTblName.setStatus("current")


class _Ds0TxRxCasConfig_Type(Integer32):
    """Custom type ds0TxRxCasConfig based on Integer32"""
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
        *(("bidirectional", 3),
          ("none", 4),
          ("receive", 2),
          ("transmit", 1))
    )


_Ds0TxRxCasConfig_Type.__name__ = "Integer32"
_Ds0TxRxCasConfig_Object = MibTableColumn
ds0TxRxCasConfig = _Ds0TxRxCasConfig_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 1, 1, 41),
    _Ds0TxRxCasConfig_Type()
)
ds0TxRxCasConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0TxRxCasConfig.setStatus("current")
_Dsx0VismChanMapTable_Object = MibTable
dsx0VismChanMapTable = _Dsx0VismChanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 2)
)
if mibBuilder.loadTexts:
    dsx0VismChanMapTable.setStatus("current")
_Dsx0VismChanMapEntry_Object = MibTableRow
dsx0VismChanMapEntry = _Dsx0VismChanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 2, 1)
)
dsx0VismChanMapEntry.setIndexNames(
    (0, "CISCO-VISM-DSX0-MIB", "dsx1LineNum"),
    (0, "CISCO-VISM-DSX0-MIB", "ds0ChanNum"),
)
if mibBuilder.loadTexts:
    dsx0VismChanMapEntry.setStatus("current")


class _Dsx1LineNum_Type(Integer32):
    """Custom type dsx1LineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dsx1LineNum_Type.__name__ = "Integer32"
_Dsx1LineNum_Object = MibTableColumn
dsx1LineNum = _Dsx1LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 2, 1, 1),
    _Dsx1LineNum_Type()
)
dsx1LineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LineNum.setStatus("current")


class _Ds0ChanNum_Type(Integer32):
    """Custom type ds0ChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Ds0ChanNum_Type.__name__ = "Integer32"
_Ds0ChanNum_Object = MibTableColumn
ds0ChanNum = _Ds0ChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 2, 1, 2),
    _Ds0ChanNum_Type()
)
ds0ChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0ChanNum.setStatus("current")


class _Ds0ChanMapIfIndex_Type(Integer32):
    """Custom type ds0ChanMapIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ds0ChanMapIfIndex_Type.__name__ = "Integer32"
_Ds0ChanMapIfIndex_Object = MibTableColumn
ds0ChanMapIfIndex = _Ds0ChanMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 2, 1, 3),
    _Ds0ChanMapIfIndex_Type()
)
ds0ChanMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0ChanMapIfIndex.setStatus("current")
_VismDs0LineStatsTable_Object = MibTable
vismDs0LineStatsTable = _VismDs0LineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3)
)
if mibBuilder.loadTexts:
    vismDs0LineStatsTable.setStatus("current")
_VismDs0LineStatsEntry_Object = MibTableRow
vismDs0LineStatsEntry = _VismDs0LineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1)
)
vismDs0LineStatsEntry.setIndexNames(
    (0, "CISCO-VISM-DSX0-MIB", "ds0LineNum"),
)
if mibBuilder.loadTexts:
    vismDs0LineStatsEntry.setStatus("current")


class _Ds0LineNum_Type(Integer32):
    """Custom type ds0LineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ds0LineNum_Type.__name__ = "Integer32"
_Ds0LineNum_Object = MibTableColumn
ds0LineNum = _Ds0LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 1),
    _Ds0LineNum_Type()
)
ds0LineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0LineNum.setStatus("current")


class _LineTotalDs0Count_Type(Integer32):
    """Custom type lineTotalDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LineTotalDs0Count_Type.__name__ = "Integer32"
_LineTotalDs0Count_Object = MibTableColumn
lineTotalDs0Count = _LineTotalDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 2),
    _LineTotalDs0Count_Type()
)
lineTotalDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTotalDs0Count.setStatus("current")


class _LineFreeDs0Count_Type(Integer32):
    """Custom type lineFreeDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LineFreeDs0Count_Type.__name__ = "Integer32"
_LineFreeDs0Count_Object = MibTableColumn
lineFreeDs0Count = _LineFreeDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 3),
    _LineFreeDs0Count_Type()
)
lineFreeDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineFreeDs0Count.setStatus("current")


class _LineActiveDs0Count_Type(Integer32):
    """Custom type lineActiveDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LineActiveDs0Count_Type.__name__ = "Integer32"
_LineActiveDs0Count_Object = MibTableColumn
lineActiveDs0Count = _LineActiveDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 4),
    _LineActiveDs0Count_Type()
)
lineActiveDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineActiveDs0Count.setStatus("current")


class _LineBlockDs0Count_Type(Integer32):
    """Custom type lineBlockDs0Count based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LineBlockDs0Count_Type.__name__ = "Integer32"
_LineBlockDs0Count_Object = MibTableColumn
lineBlockDs0Count = _LineBlockDs0Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 5),
    _LineBlockDs0Count_Type()
)
lineBlockDs0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineBlockDs0Count.setStatus("current")


class _LineActiveHighWaterMark_Type(Integer32):
    """Custom type lineActiveHighWaterMark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LineActiveHighWaterMark_Type.__name__ = "Integer32"
_LineActiveHighWaterMark_Object = MibTableColumn
lineActiveHighWaterMark = _LineActiveHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 6),
    _LineActiveHighWaterMark_Type()
)
lineActiveHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineActiveHighWaterMark.setStatus("current")


class _LineStatsClrButton_Type(Integer32):
    """Custom type lineStatsClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_LineStatsClrButton_Type.__name__ = "Integer32"
_LineStatsClrButton_Object = MibTableColumn
lineStatsClrButton = _LineStatsClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 3, 1, 7),
    _LineStatsClrButton_Type()
)
lineStatsClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineStatsClrButton.setStatus("current")
_VismDs0StatusTable_Object = MibTable
vismDs0StatusTable = _VismDs0StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 4)
)
if mibBuilder.loadTexts:
    vismDs0StatusTable.setStatus("current")
_VismDs0StatusEntry_Object = MibTableRow
vismDs0StatusEntry = _VismDs0StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 4, 1)
)
vismDs0StatusEntry.setIndexNames(
    (0, "CISCO-VISM-DSX0-MIB", "ds0LineNumber"),
    (0, "CISCO-VISM-DSX0-MIB", "ds0Number"),
)
if mibBuilder.loadTexts:
    vismDs0StatusEntry.setStatus("current")


class _Ds0LineNumber_Type(Integer32):
    """Custom type ds0LineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ds0LineNumber_Type.__name__ = "Integer32"
_Ds0LineNumber_Object = MibTableColumn
ds0LineNumber = _Ds0LineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 4, 1, 1),
    _Ds0LineNumber_Type()
)
ds0LineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0LineNumber.setStatus("current")


class _Ds0Number_Type(Integer32):
    """Custom type ds0Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Ds0Number_Type.__name__ = "Integer32"
_Ds0Number_Object = MibTableColumn
ds0Number = _Ds0Number_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 4, 1, 2),
    _Ds0Number_Type()
)
ds0Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0Number.setStatus("current")


class _Ds0Status_Type(Integer32):
    """Custom type ds0Status based on Integer32"""
    defaultValue = 5

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
        *(("block", 4),
          ("busy", 2),
          ("fault", 3),
          ("idle", 1),
          ("unknown", 5))
    )


_Ds0Status_Type.__name__ = "Integer32"
_Ds0Status_Object = MibTableColumn
ds0Status = _Ds0Status_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 4, 1, 3),
    _Ds0Status_Type()
)
ds0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0Status.setStatus("current")


class _Ds0StatusClrButton_Type(Integer32):
    """Custom type ds0StatusClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_Ds0StatusClrButton_Type.__name__ = "Integer32"
_Ds0StatusClrButton_Object = MibTableColumn
ds0StatusClrButton = _Ds0StatusClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7, 4, 1, 4),
    _Ds0StatusClrButton_Type()
)
ds0StatusClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0StatusClrButton.setStatus("current")
_CiscoVismDsx0MIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismDsx0MIBConformance = _CiscoVismDsx0MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2)
)
_CiscoVismDsx0MIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismDsx0MIBGroups = _CiscoVismDsx0MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1)
)
_CiscoVismDsx0MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismDsx0MIBCompliances = _CiscoVismDsx0MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 2)
)

# Managed Objects groups

ciscoVismCardStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 1)
)
ciscoVismCardStatsGroup.setObjects(
      *(("CISCO-VISM-DSX0-MIB", "vismTotalDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "vismFreeDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "vismActiveDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "vismBlockDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "vismActiveHighWaterMark"),
        ("CISCO-VISM-DSX0-MIB", "vismDs0CardStatsClrButton"))
)
if mibBuilder.loadTexts:
    ciscoVismCardStatsGroup.setStatus("current")

ciscoVismDsx0LineStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 2)
)
ciscoVismDsx0LineStatsGroup.setObjects(
      *(("CISCO-VISM-DSX0-MIB", "ds0LineNum"),
        ("CISCO-VISM-DSX0-MIB", "lineTotalDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "lineFreeDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "lineActiveDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "lineBlockDs0Count"),
        ("CISCO-VISM-DSX0-MIB", "lineActiveHighWaterMark"),
        ("CISCO-VISM-DSX0-MIB", "lineStatsClrButton"))
)
if mibBuilder.loadTexts:
    ciscoVismDsx0LineStatsGroup.setStatus("current")

ciscoVismDsx0StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 3)
)
ciscoVismDsx0StatusGroup.setObjects(
      *(("CISCO-VISM-DSX0-MIB", "ds0LineNumber"),
        ("CISCO-VISM-DSX0-MIB", "ds0Number"),
        ("CISCO-VISM-DSX0-MIB", "ds0Status"),
        ("CISCO-VISM-DSX0-MIB", "ds0StatusClrButton"))
)
if mibBuilder.loadTexts:
    ciscoVismDsx0StatusGroup.setStatus("current")

ciscoVismDsx0ConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 4)
)
ciscoVismDsx0ConfGroup.setObjects(
      *(("CISCO-VISM-DSX0-MIB", "ds0IfIndex"),
        ("CISCO-VISM-DSX0-MIB", "ds0RobbedBitSignalling"),
        ("CISCO-VISM-DSX0-MIB", "ds0IdleCode"),
        ("CISCO-VISM-DSX0-MIB", "ds0SeizedCode"),
        ("CISCO-VISM-DSX0-MIB", "ds0ReceivedCode"),
        ("CISCO-VISM-DSX0-MIB", "ds0BundleMapped"),
        ("CISCO-VISM-DSX0-MIB", "ds0IfType"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasVariantName"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasCadenceOnTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasCadenceOffTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0InsertLocalCas"),
        ("CISCO-VISM-DSX0-MIB", "ds0LocalCasPattern"),
        ("CISCO-VISM-DSX0-MIB", "ds0LoopbackCommand"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasParameterSource"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasOnHookMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasOffHookMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasWinkMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasWinkMaxMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasWinkBreakTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasGlareTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasGaurdTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasDelayImmedStart"),
        ("CISCO-VISM-DSX0-MIB", "ds0SignalingType"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasMinDelayDialTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasMinStartDialTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasFlashMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasFlashMaxMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasDirectionality"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasGlarePolicy"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasIncomingMgcpPackage"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasOutgoingMgcpPackage"),
        ("CISCO-VISM-DSX0-MIB", "ds0InputGain"),
        ("CISCO-VISM-DSX0-MIB", "ds0OutputAttenuation"),
        ("CISCO-VISM-DSX0-MIB", "ds0MusicThreshold"),
        ("CISCO-VISM-DSX0-MIB", "ds0SidPacket"),
        ("CISCO-VISM-DSX0-MIB", "ds0ExecDiag"))
)
if mibBuilder.loadTexts:
    ciscoVismDsx0ConfGroup.setStatus("deprecated")

ciscoVismDsx0ChanMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 5)
)
ciscoVismDsx0ChanMapGroup.setObjects(
      *(("CISCO-VISM-DSX0-MIB", "dsx1LineNum"),
        ("CISCO-VISM-DSX0-MIB", "ds0ChanNum"),
        ("CISCO-VISM-DSX0-MIB", "ds0ChanMapIfIndex"))
)
if mibBuilder.loadTexts:
    ciscoVismDsx0ChanMapGroup.setStatus("current")

ciscoVismDsx0ConfDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 6)
)
ciscoVismDsx0ConfDeprecatedGroup.setObjects(
    ("CISCO-VISM-DSX0-MIB", "ds0TransmitCodesEnable")
)
if mibBuilder.loadTexts:
    ciscoVismDsx0ConfDeprecatedGroup.setStatus("deprecated")

ciscoVismDsx0ConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 1, 7)
)
ciscoVismDsx0ConfGroup2.setObjects(
      *(("CISCO-VISM-DSX0-MIB", "ds0IfIndex"),
        ("CISCO-VISM-DSX0-MIB", "ds0RobbedBitSignalling"),
        ("CISCO-VISM-DSX0-MIB", "ds0IdleCode"),
        ("CISCO-VISM-DSX0-MIB", "ds0SeizedCode"),
        ("CISCO-VISM-DSX0-MIB", "ds0ReceivedCode"),
        ("CISCO-VISM-DSX0-MIB", "ds0BundleMapped"),
        ("CISCO-VISM-DSX0-MIB", "ds0IfType"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasVariantName"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasCadenceOnTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasCadenceOffTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0InsertLocalCas"),
        ("CISCO-VISM-DSX0-MIB", "ds0LocalCasPattern"),
        ("CISCO-VISM-DSX0-MIB", "ds0LoopbackCommand"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasParameterSource"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasOnHookMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasOffHookMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasWinkMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasWinkMaxMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasWinkBreakTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasGlareTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasGaurdTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasDelayImmedStart"),
        ("CISCO-VISM-DSX0-MIB", "ds0SignalingType"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasMinDelayDialTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasMinStartDialTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasFlashMinMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasFlashMaxMakeTime"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasDirectionality"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasGlarePolicy"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasIncomingMgcpPackage"),
        ("CISCO-VISM-DSX0-MIB", "ds0CasOutgoingMgcpPackage"),
        ("CISCO-VISM-DSX0-MIB", "ds0InputGain"),
        ("CISCO-VISM-DSX0-MIB", "ds0OutputAttenuation"),
        ("CISCO-VISM-DSX0-MIB", "ds0MusicThreshold"),
        ("CISCO-VISM-DSX0-MIB", "ds0SidPacket"),
        ("CISCO-VISM-DSX0-MIB", "ds0ExecDiag"),
        ("CISCO-VISM-DSX0-MIB", "ds0Companding"),
        ("CISCO-VISM-DSX0-MIB", "ds0RxCasTransTblName"),
        ("CISCO-VISM-DSX0-MIB", "ds0TxCasTransTblName"),
        ("CISCO-VISM-DSX0-MIB", "ds0TxRxCasConfig"))
)
if mibBuilder.loadTexts:
    ciscoVismDsx0ConfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismDsx0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismDsx0Compliance.setStatus(
        "deprecated"
    )

ciscoVismDsx0Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 81, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoVismDsx0Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-DSX0-MIB",
    **{"vismDs0CardStats": vismDs0CardStats,
       "vismTotalDs0Count": vismTotalDs0Count,
       "vismFreeDs0Count": vismFreeDs0Count,
       "vismActiveDs0Count": vismActiveDs0Count,
       "vismBlockDs0Count": vismBlockDs0Count,
       "vismActiveHighWaterMark": vismActiveHighWaterMark,
       "vismDs0CardStatsClrButton": vismDs0CardStatsClrButton,
       "dsx0VismCnfTable": dsx0VismCnfTable,
       "dsx0VismCnfEntry": dsx0VismCnfEntry,
       "ds0IfIndex": ds0IfIndex,
       "ds0RobbedBitSignalling": ds0RobbedBitSignalling,
       "ds0IdleCode": ds0IdleCode,
       "ds0SeizedCode": ds0SeizedCode,
       "ds0ReceivedCode": ds0ReceivedCode,
       "ds0TransmitCodesEnable": ds0TransmitCodesEnable,
       "ds0BundleMapped": ds0BundleMapped,
       "ds0IfType": ds0IfType,
       "ds0CasVariantName": ds0CasVariantName,
       "ds0CasCadenceOnTime": ds0CasCadenceOnTime,
       "ds0CasCadenceOffTime": ds0CasCadenceOffTime,
       "ds0InsertLocalCas": ds0InsertLocalCas,
       "ds0LocalCasPattern": ds0LocalCasPattern,
       "ds0LoopbackCommand": ds0LoopbackCommand,
       "ds0CasParameterSource": ds0CasParameterSource,
       "ds0CasOnHookMinMakeTime": ds0CasOnHookMinMakeTime,
       "ds0CasOffHookMinMakeTime": ds0CasOffHookMinMakeTime,
       "ds0CasWinkMinMakeTime": ds0CasWinkMinMakeTime,
       "ds0CasWinkMaxMakeTime": ds0CasWinkMaxMakeTime,
       "ds0CasWinkBreakTime": ds0CasWinkBreakTime,
       "ds0CasGlareTime": ds0CasGlareTime,
       "ds0CasGaurdTime": ds0CasGaurdTime,
       "ds0CasDelayImmedStart": ds0CasDelayImmedStart,
       "ds0SignalingType": ds0SignalingType,
       "ds0CasMinDelayDialTime": ds0CasMinDelayDialTime,
       "ds0CasMinStartDialTime": ds0CasMinStartDialTime,
       "ds0CasFlashMinMakeTime": ds0CasFlashMinMakeTime,
       "ds0CasFlashMaxMakeTime": ds0CasFlashMaxMakeTime,
       "ds0CasDirectionality": ds0CasDirectionality,
       "ds0CasGlarePolicy": ds0CasGlarePolicy,
       "ds0CasIncomingMgcpPackage": ds0CasIncomingMgcpPackage,
       "ds0CasOutgoingMgcpPackage": ds0CasOutgoingMgcpPackage,
       "ds0InputGain": ds0InputGain,
       "ds0OutputAttenuation": ds0OutputAttenuation,
       "ds0MusicThreshold": ds0MusicThreshold,
       "ds0SidPacket": ds0SidPacket,
       "ds0ExecDiag": ds0ExecDiag,
       "ds0Companding": ds0Companding,
       "ds0RxCasTransTblName": ds0RxCasTransTblName,
       "ds0TxCasTransTblName": ds0TxCasTransTblName,
       "ds0TxRxCasConfig": ds0TxRxCasConfig,
       "dsx0VismChanMapTable": dsx0VismChanMapTable,
       "dsx0VismChanMapEntry": dsx0VismChanMapEntry,
       "dsx1LineNum": dsx1LineNum,
       "ds0ChanNum": ds0ChanNum,
       "ds0ChanMapIfIndex": ds0ChanMapIfIndex,
       "vismDs0LineStatsTable": vismDs0LineStatsTable,
       "vismDs0LineStatsEntry": vismDs0LineStatsEntry,
       "ds0LineNum": ds0LineNum,
       "lineTotalDs0Count": lineTotalDs0Count,
       "lineFreeDs0Count": lineFreeDs0Count,
       "lineActiveDs0Count": lineActiveDs0Count,
       "lineBlockDs0Count": lineBlockDs0Count,
       "lineActiveHighWaterMark": lineActiveHighWaterMark,
       "lineStatsClrButton": lineStatsClrButton,
       "vismDs0StatusTable": vismDs0StatusTable,
       "vismDs0StatusEntry": vismDs0StatusEntry,
       "ds0LineNumber": ds0LineNumber,
       "ds0Number": ds0Number,
       "ds0Status": ds0Status,
       "ds0StatusClrButton": ds0StatusClrButton,
       "ciscoVismDsx0MIB": ciscoVismDsx0MIB,
       "ciscoVismDsx0MIBConformance": ciscoVismDsx0MIBConformance,
       "ciscoVismDsx0MIBGroups": ciscoVismDsx0MIBGroups,
       "ciscoVismCardStatsGroup": ciscoVismCardStatsGroup,
       "ciscoVismDsx0LineStatsGroup": ciscoVismDsx0LineStatsGroup,
       "ciscoVismDsx0StatusGroup": ciscoVismDsx0StatusGroup,
       "ciscoVismDsx0ConfGroup": ciscoVismDsx0ConfGroup,
       "ciscoVismDsx0ChanMapGroup": ciscoVismDsx0ChanMapGroup,
       "ciscoVismDsx0ConfDeprecatedGroup": ciscoVismDsx0ConfDeprecatedGroup,
       "ciscoVismDsx0ConfGroup2": ciscoVismDsx0ConfGroup2,
       "ciscoVismDsx0MIBCompliances": ciscoVismDsx0MIBCompliances,
       "ciscoVismDsx0Compliance": ciscoVismDsx0Compliance,
       "ciscoVismDsx0Compliance2": ciscoVismDsx0Compliance2}
)
