# SNMP MIB module (CYAN-CEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-CEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:05 2024
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

(CyanTypeTc,
 cyanEntityModules) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "CyanTypeTc",
    "cyanEntityModules")

(CyanActvStdbyTc,
 CyanAdminStateTc,
 CyanLEDTc,
 CyanOffOnTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanActvStdbyTc",
    "CyanAdminStateTc",
    "CyanLEDTc",
    "CyanOffOnTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cyanCemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50)
)
cyanCemModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanCemMibObjects_ObjectIdentity = ObjectIdentity
cyanCemMibObjects = _CyanCemMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1)
)
_CyanCemTable_Object = MibTable
cyanCemTable = _CyanCemTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1)
)
if mibBuilder.loadTexts:
    cyanCemTable.setStatus("current")
_CyanCemEntry_Object = MibTableRow
cyanCemEntry = _CyanCemEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1)
)
cyanCemEntry.setIndexNames(
    (0, "CYAN-CEM-MIB", "cyanCemShelfId"),
    (0, "CYAN-CEM-MIB", "cyanCemCemId"),
)
if mibBuilder.loadTexts:
    cyanCemEntry.setStatus("current")


class _CyanCemShelfId_Type(Unsigned32):
    """Custom type cyanCemShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanCemShelfId_Type.__name__ = "Unsigned32"
_CyanCemShelfId_Object = MibTableColumn
cyanCemShelfId = _CyanCemShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 1),
    _CyanCemShelfId_Type()
)
cyanCemShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanCemShelfId.setStatus("current")
_CyanCemCemId_Type = Unsigned32
_CyanCemCemId_Object = MibTableColumn
cyanCemCemId = _CyanCemCemId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 2),
    _CyanCemCemId_Type()
)
cyanCemCemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanCemCemId.setStatus("current")
_CyanCemActiveLed_Type = CyanLEDTc
_CyanCemActiveLed_Object = MibTableColumn
cyanCemActiveLed = _CyanCemActiveLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 3),
    _CyanCemActiveLed_Type()
)
cyanCemActiveLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemActiveLed.setStatus("current")
_CyanCemActivestandbyState_Type = CyanActvStdbyTc
_CyanCemActivestandbyState_Object = MibTableColumn
cyanCemActivestandbyState = _CyanCemActivestandbyState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 4),
    _CyanCemActivestandbyState_Type()
)
cyanCemActivestandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemActivestandbyState.setStatus("current")
_CyanCemAdminState_Type = CyanAdminStateTc
_CyanCemAdminState_Object = MibTableColumn
cyanCemAdminState = _CyanCemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 5),
    _CyanCemAdminState_Type()
)
cyanCemAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemAdminState.setStatus("current")
_CyanCemAlarmLed_Type = CyanLEDTc
_CyanCemAlarmLed_Object = MibTableColumn
cyanCemAlarmLed = _CyanCemAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 6),
    _CyanCemAlarmLed_Type()
)
cyanCemAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemAlarmLed.setStatus("current")


class _CyanCemAssetTag_Type(DisplayString):
    """Custom type cyanCemAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanCemAssetTag_Type.__name__ = "DisplayString"
_CyanCemAssetTag_Object = MibTableColumn
cyanCemAssetTag = _CyanCemAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 7),
    _CyanCemAssetTag_Type()
)
cyanCemAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemAssetTag.setStatus("current")
_CyanCemAutoinserviceSoakTimeSec_Type = Integer32
_CyanCemAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanCemAutoinserviceSoakTimeSec = _CyanCemAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 8),
    _CyanCemAutoinserviceSoakTimeSec_Type()
)
cyanCemAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemAutoinserviceSoakTimeSec.setStatus("current")
_CyanCemBaseMacAddress_Type = DisplayString
_CyanCemBaseMacAddress_Object = MibTableColumn
cyanCemBaseMacAddress = _CyanCemBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 9),
    _CyanCemBaseMacAddress_Type()
)
cyanCemBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemBaseMacAddress.setStatus("current")
_CyanCemCurrCyanSwBuildVersions_Type = DisplayString
_CyanCemCurrCyanSwBuildVersions_Object = MibTableColumn
cyanCemCurrCyanSwBuildVersions = _CyanCemCurrCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 10),
    _CyanCemCurrCyanSwBuildVersions_Type()
)
cyanCemCurrCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemCurrCyanSwBuildVersions.setStatus("current")
_CyanCemCurrent_Type = Integer32
_CyanCemCurrent_Object = MibTableColumn
cyanCemCurrent = _CyanCemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 11),
    _CyanCemCurrent_Type()
)
cyanCemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemCurrent.setStatus("current")


class _CyanCemDescription_Type(DisplayString):
    """Custom type cyanCemDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanCemDescription_Type.__name__ = "DisplayString"
_CyanCemDescription_Object = MibTableColumn
cyanCemDescription = _CyanCemDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 12),
    _CyanCemDescription_Type()
)
cyanCemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemDescription.setStatus("current")


class _CyanCemExhaustAirTemp_Type(Integer32):
    """Custom type cyanCemExhaustAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemExhaustAirTemp_Type.__name__ = "Integer32"
_CyanCemExhaustAirTemp_Object = MibTableColumn
cyanCemExhaustAirTemp = _CyanCemExhaustAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 13),
    _CyanCemExhaustAirTemp_Type()
)
cyanCemExhaustAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemExhaustAirTemp.setStatus("current")


class _CyanCemExhaustTempAlarmHighThres_Type(Integer32):
    """Custom type cyanCemExhaustTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemExhaustTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanCemExhaustTempAlarmHighThres_Object = MibTableColumn
cyanCemExhaustTempAlarmHighThres = _CyanCemExhaustTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 14),
    _CyanCemExhaustTempAlarmHighThres_Type()
)
cyanCemExhaustTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemExhaustTempAlarmHighThres.setStatus("current")


class _CyanCemExhaustTempAlarmLowThres_Type(Integer32):
    """Custom type cyanCemExhaustTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemExhaustTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanCemExhaustTempAlarmLowThres_Object = MibTableColumn
cyanCemExhaustTempAlarmLowThres = _CyanCemExhaustTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 15),
    _CyanCemExhaustTempAlarmLowThres_Type()
)
cyanCemExhaustTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemExhaustTempAlarmLowThres.setStatus("current")


class _CyanCemExhaustTempWarnHighThres_Type(Integer32):
    """Custom type cyanCemExhaustTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemExhaustTempWarnHighThres_Type.__name__ = "Integer32"
_CyanCemExhaustTempWarnHighThres_Object = MibTableColumn
cyanCemExhaustTempWarnHighThres = _CyanCemExhaustTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 16),
    _CyanCemExhaustTempWarnHighThres_Type()
)
cyanCemExhaustTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemExhaustTempWarnHighThres.setStatus("current")


class _CyanCemExhaustTempWarnLowThres_Type(Integer32):
    """Custom type cyanCemExhaustTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemExhaustTempWarnLowThres_Type.__name__ = "Integer32"
_CyanCemExhaustTempWarnLowThres_Object = MibTableColumn
cyanCemExhaustTempWarnLowThres = _CyanCemExhaustTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 17),
    _CyanCemExhaustTempWarnLowThres_Type()
)
cyanCemExhaustTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemExhaustTempWarnLowThres.setStatus("current")
_CyanCemExpectedTemperatureRise_Type = Integer32
_CyanCemExpectedTemperatureRise_Object = MibTableColumn
cyanCemExpectedTemperatureRise = _CyanCemExpectedTemperatureRise_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 18),
    _CyanCemExpectedTemperatureRise_Type()
)
cyanCemExpectedTemperatureRise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemExpectedTemperatureRise.setStatus("current")
_CyanCemIdentifier_Type = DisplayString
_CyanCemIdentifier_Object = MibTableColumn
cyanCemIdentifier = _CyanCemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 19),
    _CyanCemIdentifier_Type()
)
cyanCemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemIdentifier.setStatus("current")


class _CyanCemIntakeAirTemp_Type(Integer32):
    """Custom type cyanCemIntakeAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemIntakeAirTemp_Type.__name__ = "Integer32"
_CyanCemIntakeAirTemp_Object = MibTableColumn
cyanCemIntakeAirTemp = _CyanCemIntakeAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 20),
    _CyanCemIntakeAirTemp_Type()
)
cyanCemIntakeAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemIntakeAirTemp.setStatus("current")


class _CyanCemIntakeTempAlarmHighThres_Type(Integer32):
    """Custom type cyanCemIntakeTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemIntakeTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanCemIntakeTempAlarmHighThres_Object = MibTableColumn
cyanCemIntakeTempAlarmHighThres = _CyanCemIntakeTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 21),
    _CyanCemIntakeTempAlarmHighThres_Type()
)
cyanCemIntakeTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemIntakeTempAlarmHighThres.setStatus("current")


class _CyanCemIntakeTempAlarmLowThres_Type(Integer32):
    """Custom type cyanCemIntakeTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemIntakeTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanCemIntakeTempAlarmLowThres_Object = MibTableColumn
cyanCemIntakeTempAlarmLowThres = _CyanCemIntakeTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 22),
    _CyanCemIntakeTempAlarmLowThres_Type()
)
cyanCemIntakeTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemIntakeTempAlarmLowThres.setStatus("current")


class _CyanCemIntakeTempWarnHighThres_Type(Integer32):
    """Custom type cyanCemIntakeTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemIntakeTempWarnHighThres_Type.__name__ = "Integer32"
_CyanCemIntakeTempWarnHighThres_Object = MibTableColumn
cyanCemIntakeTempWarnHighThres = _CyanCemIntakeTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 23),
    _CyanCemIntakeTempWarnHighThres_Type()
)
cyanCemIntakeTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemIntakeTempWarnHighThres.setStatus("current")


class _CyanCemIntakeTempWarnLowThres_Type(Integer32):
    """Custom type cyanCemIntakeTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanCemIntakeTempWarnLowThres_Type.__name__ = "Integer32"
_CyanCemIntakeTempWarnLowThres_Object = MibTableColumn
cyanCemIntakeTempWarnLowThres = _CyanCemIntakeTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 24),
    _CyanCemIntakeTempWarnLowThres_Type()
)
cyanCemIntakeTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemIntakeTempWarnLowThres.setStatus("current")
_CyanCemLedTest_Type = Unsigned32
_CyanCemLedTest_Object = MibTableColumn
cyanCemLedTest = _CyanCemLedTest_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 25),
    _CyanCemLedTest_Type()
)
cyanCemLedTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemLedTest.setStatus("current")


class _CyanCemMacBlockSize_Type(Unsigned32):
    """Custom type cyanCemMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanCemMacBlockSize_Type.__name__ = "Unsigned32"
_CyanCemMacBlockSize_Object = MibTableColumn
cyanCemMacBlockSize = _CyanCemMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 26),
    _CyanCemMacBlockSize_Type()
)
cyanCemMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMacBlockSize.setStatus("current")


class _CyanCemMfgCleiCode_Type(DisplayString):
    """Custom type cyanCemMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanCemMfgCleiCode_Type.__name__ = "DisplayString"
_CyanCemMfgCleiCode_Object = MibTableColumn
cyanCemMfgCleiCode = _CyanCemMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 27),
    _CyanCemMfgCleiCode_Type()
)
cyanCemMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMfgCleiCode.setStatus("current")


class _CyanCemMfgEciCode_Type(DisplayString):
    """Custom type cyanCemMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanCemMfgEciCode_Type.__name__ = "DisplayString"
_CyanCemMfgEciCode_Object = MibTableColumn
cyanCemMfgEciCode = _CyanCemMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 28),
    _CyanCemMfgEciCode_Type()
)
cyanCemMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMfgEciCode.setStatus("current")
_CyanCemMfgModuleId_Type = Unsigned32
_CyanCemMfgModuleId_Object = MibTableColumn
cyanCemMfgModuleId = _CyanCemMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 29),
    _CyanCemMfgModuleId_Type()
)
cyanCemMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMfgModuleId.setStatus("current")


class _CyanCemMfgPartNumber_Type(DisplayString):
    """Custom type cyanCemMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanCemMfgPartNumber_Type.__name__ = "DisplayString"
_CyanCemMfgPartNumber_Object = MibTableColumn
cyanCemMfgPartNumber = _CyanCemMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 30),
    _CyanCemMfgPartNumber_Type()
)
cyanCemMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMfgPartNumber.setStatus("current")


class _CyanCemMfgRevision_Type(DisplayString):
    """Custom type cyanCemMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanCemMfgRevision_Type.__name__ = "DisplayString"
_CyanCemMfgRevision_Object = MibTableColumn
cyanCemMfgRevision = _CyanCemMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 31),
    _CyanCemMfgRevision_Type()
)
cyanCemMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMfgRevision.setStatus("current")


class _CyanCemMfgSerialNumber_Type(DisplayString):
    """Custom type cyanCemMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanCemMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanCemMfgSerialNumber_Object = MibTableColumn
cyanCemMfgSerialNumber = _CyanCemMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 32),
    _CyanCemMfgSerialNumber_Type()
)
cyanCemMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemMfgSerialNumber.setStatus("current")
_CyanCemName_Type = DisplayString
_CyanCemName_Object = MibTableColumn
cyanCemName = _CyanCemName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 33),
    _CyanCemName_Type()
)
cyanCemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemName.setStatus("current")
_CyanCemOidClass_Type = DisplayString
_CyanCemOidClass_Object = MibTableColumn
cyanCemOidClass = _CyanCemOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 34),
    _CyanCemOidClass_Type()
)
cyanCemOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemOidClass.setStatus("current")
_CyanCemOperState_Type = CyanOpStateTc
_CyanCemOperState_Object = MibTableColumn
cyanCemOperState = _CyanCemOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 35),
    _CyanCemOperState_Type()
)
cyanCemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemOperState.setStatus("current")
_CyanCemOperStateQual_Type = CyanOpStateQualTc
_CyanCemOperStateQual_Object = MibTableColumn
cyanCemOperStateQual = _CyanCemOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 36),
    _CyanCemOperStateQual_Type()
)
cyanCemOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemOperStateQual.setStatus("current")


class _CyanCemOssLabel_Type(DisplayString):
    """Custom type cyanCemOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanCemOssLabel_Type.__name__ = "DisplayString"
_CyanCemOssLabel_Object = MibTableColumn
cyanCemOssLabel = _CyanCemOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 37),
    _CyanCemOssLabel_Type()
)
cyanCemOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemOssLabel.setStatus("current")
_CyanCemOvervoltageThreshold_Type = Integer32
_CyanCemOvervoltageThreshold_Object = MibTableColumn
cyanCemOvervoltageThreshold = _CyanCemOvervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 38),
    _CyanCemOvervoltageThreshold_Type()
)
cyanCemOvervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemOvervoltageThreshold.setStatus("current")


class _CyanCemOwner_Type(DisplayString):
    """Custom type cyanCemOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanCemOwner_Type.__name__ = "DisplayString"
_CyanCemOwner_Object = MibTableColumn
cyanCemOwner = _CyanCemOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 39),
    _CyanCemOwner_Type()
)
cyanCemOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemOwner.setStatus("current")


class _CyanCemPartNumber_Type(DisplayString):
    """Custom type cyanCemPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanCemPartNumber_Type.__name__ = "DisplayString"
_CyanCemPartNumber_Object = MibTableColumn
cyanCemPartNumber = _CyanCemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 40),
    _CyanCemPartNumber_Type()
)
cyanCemPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemPartNumber.setStatus("current")
_CyanCemPowerLed_Type = CyanLEDTc
_CyanCemPowerLed_Object = MibTableColumn
cyanCemPowerLed = _CyanCemPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 41),
    _CyanCemPowerLed_Type()
)
cyanCemPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemPowerLed.setStatus("current")
_CyanCemPwrFeedAStatus_Type = CyanOffOnTc
_CyanCemPwrFeedAStatus_Object = MibTableColumn
cyanCemPwrFeedAStatus = _CyanCemPwrFeedAStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 42),
    _CyanCemPwrFeedAStatus_Type()
)
cyanCemPwrFeedAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemPwrFeedAStatus.setStatus("current")
_CyanCemPwrFeedAVoltage_Type = Integer32
_CyanCemPwrFeedAVoltage_Object = MibTableColumn
cyanCemPwrFeedAVoltage = _CyanCemPwrFeedAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 43),
    _CyanCemPwrFeedAVoltage_Type()
)
cyanCemPwrFeedAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemPwrFeedAVoltage.setStatus("current")
_CyanCemPwrFeedBStatus_Type = CyanOffOnTc
_CyanCemPwrFeedBStatus_Object = MibTableColumn
cyanCemPwrFeedBStatus = _CyanCemPwrFeedBStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 44),
    _CyanCemPwrFeedBStatus_Type()
)
cyanCemPwrFeedBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemPwrFeedBStatus.setStatus("current")
_CyanCemPwrFeedBVoltage_Type = Integer32
_CyanCemPwrFeedBVoltage_Object = MibTableColumn
cyanCemPwrFeedBVoltage = _CyanCemPwrFeedBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 45),
    _CyanCemPwrFeedBVoltage_Type()
)
cyanCemPwrFeedBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemPwrFeedBVoltage.setStatus("current")
_CyanCemSecServState_Type = CyanSecServiceStateTc
_CyanCemSecServState_Object = MibTableColumn
cyanCemSecServState = _CyanCemSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 46),
    _CyanCemSecServState_Type()
)
cyanCemSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemSecServState.setStatus("current")
_CyanCemSynchLed_Type = CyanLEDTc
_CyanCemSynchLed_Object = MibTableColumn
cyanCemSynchLed = _CyanCemSynchLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 47),
    _CyanCemSynchLed_Type()
)
cyanCemSynchLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemSynchLed.setStatus("current")
_CyanCemType_Type = CyanTypeTc
_CyanCemType_Object = MibTableColumn
cyanCemType = _CyanCemType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 48),
    _CyanCemType_Type()
)
cyanCemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemType.setStatus("current")
_CyanCemUndervoltageThreshold_Type = Integer32
_CyanCemUndervoltageThreshold_Object = MibTableColumn
cyanCemUndervoltageThreshold = _CyanCemUndervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 1, 1, 1, 49),
    _CyanCemUndervoltageThreshold_Type()
)
cyanCemUndervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanCemUndervoltageThreshold.setStatus("current")

# Managed Objects groups

cyanCemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 20)
)
cyanCemObjectGroup.setObjects(
      *(("CYAN-CEM-MIB", "cyanCemActiveLed"),
        ("CYAN-CEM-MIB", "cyanCemActivestandbyState"),
        ("CYAN-CEM-MIB", "cyanCemAdminState"),
        ("CYAN-CEM-MIB", "cyanCemAlarmLed"),
        ("CYAN-CEM-MIB", "cyanCemAssetTag"),
        ("CYAN-CEM-MIB", "cyanCemAutoinserviceSoakTimeSec"),
        ("CYAN-CEM-MIB", "cyanCemBaseMacAddress"),
        ("CYAN-CEM-MIB", "cyanCemCurrCyanSwBuildVersions"),
        ("CYAN-CEM-MIB", "cyanCemCurrent"),
        ("CYAN-CEM-MIB", "cyanCemDescription"),
        ("CYAN-CEM-MIB", "cyanCemExhaustAirTemp"),
        ("CYAN-CEM-MIB", "cyanCemExhaustTempAlarmHighThres"),
        ("CYAN-CEM-MIB", "cyanCemExhaustTempAlarmLowThres"),
        ("CYAN-CEM-MIB", "cyanCemExhaustTempWarnHighThres"),
        ("CYAN-CEM-MIB", "cyanCemExhaustTempWarnLowThres"),
        ("CYAN-CEM-MIB", "cyanCemExpectedTemperatureRise"),
        ("CYAN-CEM-MIB", "cyanCemIdentifier"),
        ("CYAN-CEM-MIB", "cyanCemIntakeAirTemp"),
        ("CYAN-CEM-MIB", "cyanCemIntakeTempAlarmHighThres"),
        ("CYAN-CEM-MIB", "cyanCemIntakeTempAlarmLowThres"),
        ("CYAN-CEM-MIB", "cyanCemIntakeTempWarnHighThres"),
        ("CYAN-CEM-MIB", "cyanCemIntakeTempWarnLowThres"),
        ("CYAN-CEM-MIB", "cyanCemLedTest"),
        ("CYAN-CEM-MIB", "cyanCemMacBlockSize"),
        ("CYAN-CEM-MIB", "cyanCemMfgCleiCode"),
        ("CYAN-CEM-MIB", "cyanCemMfgEciCode"),
        ("CYAN-CEM-MIB", "cyanCemMfgModuleId"),
        ("CYAN-CEM-MIB", "cyanCemMfgPartNumber"),
        ("CYAN-CEM-MIB", "cyanCemMfgRevision"),
        ("CYAN-CEM-MIB", "cyanCemMfgSerialNumber"),
        ("CYAN-CEM-MIB", "cyanCemName"),
        ("CYAN-CEM-MIB", "cyanCemOidClass"),
        ("CYAN-CEM-MIB", "cyanCemOperState"),
        ("CYAN-CEM-MIB", "cyanCemOperStateQual"),
        ("CYAN-CEM-MIB", "cyanCemOssLabel"),
        ("CYAN-CEM-MIB", "cyanCemOvervoltageThreshold"),
        ("CYAN-CEM-MIB", "cyanCemOwner"),
        ("CYAN-CEM-MIB", "cyanCemPartNumber"),
        ("CYAN-CEM-MIB", "cyanCemPowerLed"),
        ("CYAN-CEM-MIB", "cyanCemPwrFeedAStatus"),
        ("CYAN-CEM-MIB", "cyanCemPwrFeedAVoltage"),
        ("CYAN-CEM-MIB", "cyanCemPwrFeedBStatus"),
        ("CYAN-CEM-MIB", "cyanCemPwrFeedBVoltage"),
        ("CYAN-CEM-MIB", "cyanCemSecServState"),
        ("CYAN-CEM-MIB", "cyanCemSynchLed"),
        ("CYAN-CEM-MIB", "cyanCemType"),
        ("CYAN-CEM-MIB", "cyanCemUndervoltageThreshold"))
)
if mibBuilder.loadTexts:
    cyanCemObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanCemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 50, 30)
)
if mibBuilder.loadTexts:
    cyanCemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-CEM-MIB",
    **{"cyanCemModule": cyanCemModule,
       "cyanCemMibObjects": cyanCemMibObjects,
       "cyanCemTable": cyanCemTable,
       "cyanCemEntry": cyanCemEntry,
       "cyanCemShelfId": cyanCemShelfId,
       "cyanCemCemId": cyanCemCemId,
       "cyanCemActiveLed": cyanCemActiveLed,
       "cyanCemActivestandbyState": cyanCemActivestandbyState,
       "cyanCemAdminState": cyanCemAdminState,
       "cyanCemAlarmLed": cyanCemAlarmLed,
       "cyanCemAssetTag": cyanCemAssetTag,
       "cyanCemAutoinserviceSoakTimeSec": cyanCemAutoinserviceSoakTimeSec,
       "cyanCemBaseMacAddress": cyanCemBaseMacAddress,
       "cyanCemCurrCyanSwBuildVersions": cyanCemCurrCyanSwBuildVersions,
       "cyanCemCurrent": cyanCemCurrent,
       "cyanCemDescription": cyanCemDescription,
       "cyanCemExhaustAirTemp": cyanCemExhaustAirTemp,
       "cyanCemExhaustTempAlarmHighThres": cyanCemExhaustTempAlarmHighThres,
       "cyanCemExhaustTempAlarmLowThres": cyanCemExhaustTempAlarmLowThres,
       "cyanCemExhaustTempWarnHighThres": cyanCemExhaustTempWarnHighThres,
       "cyanCemExhaustTempWarnLowThres": cyanCemExhaustTempWarnLowThres,
       "cyanCemExpectedTemperatureRise": cyanCemExpectedTemperatureRise,
       "cyanCemIdentifier": cyanCemIdentifier,
       "cyanCemIntakeAirTemp": cyanCemIntakeAirTemp,
       "cyanCemIntakeTempAlarmHighThres": cyanCemIntakeTempAlarmHighThres,
       "cyanCemIntakeTempAlarmLowThres": cyanCemIntakeTempAlarmLowThres,
       "cyanCemIntakeTempWarnHighThres": cyanCemIntakeTempWarnHighThres,
       "cyanCemIntakeTempWarnLowThres": cyanCemIntakeTempWarnLowThres,
       "cyanCemLedTest": cyanCemLedTest,
       "cyanCemMacBlockSize": cyanCemMacBlockSize,
       "cyanCemMfgCleiCode": cyanCemMfgCleiCode,
       "cyanCemMfgEciCode": cyanCemMfgEciCode,
       "cyanCemMfgModuleId": cyanCemMfgModuleId,
       "cyanCemMfgPartNumber": cyanCemMfgPartNumber,
       "cyanCemMfgRevision": cyanCemMfgRevision,
       "cyanCemMfgSerialNumber": cyanCemMfgSerialNumber,
       "cyanCemName": cyanCemName,
       "cyanCemOidClass": cyanCemOidClass,
       "cyanCemOperState": cyanCemOperState,
       "cyanCemOperStateQual": cyanCemOperStateQual,
       "cyanCemOssLabel": cyanCemOssLabel,
       "cyanCemOvervoltageThreshold": cyanCemOvervoltageThreshold,
       "cyanCemOwner": cyanCemOwner,
       "cyanCemPartNumber": cyanCemPartNumber,
       "cyanCemPowerLed": cyanCemPowerLed,
       "cyanCemPwrFeedAStatus": cyanCemPwrFeedAStatus,
       "cyanCemPwrFeedAVoltage": cyanCemPwrFeedAVoltage,
       "cyanCemPwrFeedBStatus": cyanCemPwrFeedBStatus,
       "cyanCemPwrFeedBVoltage": cyanCemPwrFeedBVoltage,
       "cyanCemSecServState": cyanCemSecServState,
       "cyanCemSynchLed": cyanCemSynchLed,
       "cyanCemType": cyanCemType,
       "cyanCemUndervoltageThreshold": cyanCemUndervoltageThreshold,
       "cyanCemObjectGroup": cyanCemObjectGroup,
       "cyanCemCompliance": cyanCemCompliance}
)
