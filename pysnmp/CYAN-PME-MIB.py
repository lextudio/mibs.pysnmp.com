# SNMP MIB module (CYAN-PME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-PME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:13 2024
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

cyanPmeModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110)
)
cyanPmeModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanPmeMibObjects_ObjectIdentity = ObjectIdentity
cyanPmeMibObjects = _CyanPmeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1)
)
_CyanPmeTable_Object = MibTable
cyanPmeTable = _CyanPmeTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1)
)
if mibBuilder.loadTexts:
    cyanPmeTable.setStatus("current")
_CyanPmeEntry_Object = MibTableRow
cyanPmeEntry = _CyanPmeEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1)
)
cyanPmeEntry.setIndexNames(
    (0, "CYAN-PME-MIB", "cyanPmeShelfId"),
    (0, "CYAN-PME-MIB", "cyanPmePmeId"),
)
if mibBuilder.loadTexts:
    cyanPmeEntry.setStatus("current")


class _CyanPmeShelfId_Type(Unsigned32):
    """Custom type cyanPmeShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanPmeShelfId_Type.__name__ = "Unsigned32"
_CyanPmeShelfId_Object = MibTableColumn
cyanPmeShelfId = _CyanPmeShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 1),
    _CyanPmeShelfId_Type()
)
cyanPmeShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanPmeShelfId.setStatus("current")
_CyanPmePmeId_Type = Unsigned32
_CyanPmePmeId_Object = MibTableColumn
cyanPmePmeId = _CyanPmePmeId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 2),
    _CyanPmePmeId_Type()
)
cyanPmePmeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanPmePmeId.setStatus("current")
_CyanPmeActiveLed_Type = CyanLEDTc
_CyanPmeActiveLed_Object = MibTableColumn
cyanPmeActiveLed = _CyanPmeActiveLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 3),
    _CyanPmeActiveLed_Type()
)
cyanPmeActiveLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeActiveLed.setStatus("current")
_CyanPmeActivestandbyState_Type = CyanActvStdbyTc
_CyanPmeActivestandbyState_Object = MibTableColumn
cyanPmeActivestandbyState = _CyanPmeActivestandbyState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 4),
    _CyanPmeActivestandbyState_Type()
)
cyanPmeActivestandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeActivestandbyState.setStatus("current")
_CyanPmeAdminState_Type = CyanAdminStateTc
_CyanPmeAdminState_Object = MibTableColumn
cyanPmeAdminState = _CyanPmeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 5),
    _CyanPmeAdminState_Type()
)
cyanPmeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeAdminState.setStatus("current")
_CyanPmeAlarmLed_Type = CyanLEDTc
_CyanPmeAlarmLed_Object = MibTableColumn
cyanPmeAlarmLed = _CyanPmeAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 6),
    _CyanPmeAlarmLed_Type()
)
cyanPmeAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeAlarmLed.setStatus("current")


class _CyanPmeAssetTag_Type(DisplayString):
    """Custom type cyanPmeAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanPmeAssetTag_Type.__name__ = "DisplayString"
_CyanPmeAssetTag_Object = MibTableColumn
cyanPmeAssetTag = _CyanPmeAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 7),
    _CyanPmeAssetTag_Type()
)
cyanPmeAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeAssetTag.setStatus("current")
_CyanPmeAutoinserviceSoakTimeSec_Type = Integer32
_CyanPmeAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanPmeAutoinserviceSoakTimeSec = _CyanPmeAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 8),
    _CyanPmeAutoinserviceSoakTimeSec_Type()
)
cyanPmeAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeAutoinserviceSoakTimeSec.setStatus("current")
_CyanPmeBaseMacAddress_Type = DisplayString
_CyanPmeBaseMacAddress_Object = MibTableColumn
cyanPmeBaseMacAddress = _CyanPmeBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 9),
    _CyanPmeBaseMacAddress_Type()
)
cyanPmeBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeBaseMacAddress.setStatus("current")
_CyanPmeCurrCyanSwBuildVersions_Type = DisplayString
_CyanPmeCurrCyanSwBuildVersions_Object = MibTableColumn
cyanPmeCurrCyanSwBuildVersions = _CyanPmeCurrCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 10),
    _CyanPmeCurrCyanSwBuildVersions_Type()
)
cyanPmeCurrCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeCurrCyanSwBuildVersions.setStatus("current")
_CyanPmeCurrCyanSwRelease_Type = DisplayString
_CyanPmeCurrCyanSwRelease_Object = MibTableColumn
cyanPmeCurrCyanSwRelease = _CyanPmeCurrCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 11),
    _CyanPmeCurrCyanSwRelease_Type()
)
cyanPmeCurrCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeCurrCyanSwRelease.setStatus("current")
_CyanPmeCurrent_Type = Integer32
_CyanPmeCurrent_Object = MibTableColumn
cyanPmeCurrent = _CyanPmeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 12),
    _CyanPmeCurrent_Type()
)
cyanPmeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeCurrent.setStatus("current")


class _CyanPmeDescription_Type(DisplayString):
    """Custom type cyanPmeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanPmeDescription_Type.__name__ = "DisplayString"
_CyanPmeDescription_Object = MibTableColumn
cyanPmeDescription = _CyanPmeDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 13),
    _CyanPmeDescription_Type()
)
cyanPmeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeDescription.setStatus("current")


class _CyanPmeExhaustAirTemp_Type(Integer32):
    """Custom type cyanPmeExhaustAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeExhaustAirTemp_Type.__name__ = "Integer32"
_CyanPmeExhaustAirTemp_Object = MibTableColumn
cyanPmeExhaustAirTemp = _CyanPmeExhaustAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 14),
    _CyanPmeExhaustAirTemp_Type()
)
cyanPmeExhaustAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeExhaustAirTemp.setStatus("current")


class _CyanPmeExhaustTempAlarmHighThres_Type(Integer32):
    """Custom type cyanPmeExhaustTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeExhaustTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanPmeExhaustTempAlarmHighThres_Object = MibTableColumn
cyanPmeExhaustTempAlarmHighThres = _CyanPmeExhaustTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 15),
    _CyanPmeExhaustTempAlarmHighThres_Type()
)
cyanPmeExhaustTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeExhaustTempAlarmHighThres.setStatus("current")


class _CyanPmeExhaustTempAlarmLowThres_Type(Integer32):
    """Custom type cyanPmeExhaustTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeExhaustTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanPmeExhaustTempAlarmLowThres_Object = MibTableColumn
cyanPmeExhaustTempAlarmLowThres = _CyanPmeExhaustTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 16),
    _CyanPmeExhaustTempAlarmLowThres_Type()
)
cyanPmeExhaustTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeExhaustTempAlarmLowThres.setStatus("current")


class _CyanPmeExhaustTempWarnHighThres_Type(Integer32):
    """Custom type cyanPmeExhaustTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeExhaustTempWarnHighThres_Type.__name__ = "Integer32"
_CyanPmeExhaustTempWarnHighThres_Object = MibTableColumn
cyanPmeExhaustTempWarnHighThres = _CyanPmeExhaustTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 17),
    _CyanPmeExhaustTempWarnHighThres_Type()
)
cyanPmeExhaustTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeExhaustTempWarnHighThres.setStatus("current")


class _CyanPmeExhaustTempWarnLowThres_Type(Integer32):
    """Custom type cyanPmeExhaustTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeExhaustTempWarnLowThres_Type.__name__ = "Integer32"
_CyanPmeExhaustTempWarnLowThres_Object = MibTableColumn
cyanPmeExhaustTempWarnLowThres = _CyanPmeExhaustTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 18),
    _CyanPmeExhaustTempWarnLowThres_Type()
)
cyanPmeExhaustTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeExhaustTempWarnLowThres.setStatus("current")
_CyanPmeExpectedTemperatureRise_Type = Integer32
_CyanPmeExpectedTemperatureRise_Object = MibTableColumn
cyanPmeExpectedTemperatureRise = _CyanPmeExpectedTemperatureRise_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 19),
    _CyanPmeExpectedTemperatureRise_Type()
)
cyanPmeExpectedTemperatureRise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeExpectedTemperatureRise.setStatus("current")
_CyanPmeIdentifier_Type = DisplayString
_CyanPmeIdentifier_Object = MibTableColumn
cyanPmeIdentifier = _CyanPmeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 20),
    _CyanPmeIdentifier_Type()
)
cyanPmeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeIdentifier.setStatus("current")


class _CyanPmeIntakeAirTemp_Type(Integer32):
    """Custom type cyanPmeIntakeAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeIntakeAirTemp_Type.__name__ = "Integer32"
_CyanPmeIntakeAirTemp_Object = MibTableColumn
cyanPmeIntakeAirTemp = _CyanPmeIntakeAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 21),
    _CyanPmeIntakeAirTemp_Type()
)
cyanPmeIntakeAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeIntakeAirTemp.setStatus("current")


class _CyanPmeIntakeTempAlarmHighThres_Type(Integer32):
    """Custom type cyanPmeIntakeTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeIntakeTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanPmeIntakeTempAlarmHighThres_Object = MibTableColumn
cyanPmeIntakeTempAlarmHighThres = _CyanPmeIntakeTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 22),
    _CyanPmeIntakeTempAlarmHighThres_Type()
)
cyanPmeIntakeTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeIntakeTempAlarmHighThres.setStatus("current")


class _CyanPmeIntakeTempAlarmLowThres_Type(Integer32):
    """Custom type cyanPmeIntakeTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeIntakeTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanPmeIntakeTempAlarmLowThres_Object = MibTableColumn
cyanPmeIntakeTempAlarmLowThres = _CyanPmeIntakeTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 23),
    _CyanPmeIntakeTempAlarmLowThres_Type()
)
cyanPmeIntakeTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeIntakeTempAlarmLowThres.setStatus("current")


class _CyanPmeIntakeTempWarnHighThres_Type(Integer32):
    """Custom type cyanPmeIntakeTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeIntakeTempWarnHighThres_Type.__name__ = "Integer32"
_CyanPmeIntakeTempWarnHighThres_Object = MibTableColumn
cyanPmeIntakeTempWarnHighThres = _CyanPmeIntakeTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 24),
    _CyanPmeIntakeTempWarnHighThres_Type()
)
cyanPmeIntakeTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeIntakeTempWarnHighThres.setStatus("current")


class _CyanPmeIntakeTempWarnLowThres_Type(Integer32):
    """Custom type cyanPmeIntakeTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanPmeIntakeTempWarnLowThres_Type.__name__ = "Integer32"
_CyanPmeIntakeTempWarnLowThres_Object = MibTableColumn
cyanPmeIntakeTempWarnLowThres = _CyanPmeIntakeTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 25),
    _CyanPmeIntakeTempWarnLowThres_Type()
)
cyanPmeIntakeTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeIntakeTempWarnLowThres.setStatus("current")
_CyanPmeLedTest_Type = Unsigned32
_CyanPmeLedTest_Object = MibTableColumn
cyanPmeLedTest = _CyanPmeLedTest_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 26),
    _CyanPmeLedTest_Type()
)
cyanPmeLedTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeLedTest.setStatus("current")


class _CyanPmeMacBlockSize_Type(Unsigned32):
    """Custom type cyanPmeMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanPmeMacBlockSize_Type.__name__ = "Unsigned32"
_CyanPmeMacBlockSize_Object = MibTableColumn
cyanPmeMacBlockSize = _CyanPmeMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 27),
    _CyanPmeMacBlockSize_Type()
)
cyanPmeMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMacBlockSize.setStatus("current")


class _CyanPmeMfgCleiCode_Type(DisplayString):
    """Custom type cyanPmeMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanPmeMfgCleiCode_Type.__name__ = "DisplayString"
_CyanPmeMfgCleiCode_Object = MibTableColumn
cyanPmeMfgCleiCode = _CyanPmeMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 28),
    _CyanPmeMfgCleiCode_Type()
)
cyanPmeMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMfgCleiCode.setStatus("current")


class _CyanPmeMfgEciCode_Type(DisplayString):
    """Custom type cyanPmeMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanPmeMfgEciCode_Type.__name__ = "DisplayString"
_CyanPmeMfgEciCode_Object = MibTableColumn
cyanPmeMfgEciCode = _CyanPmeMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 29),
    _CyanPmeMfgEciCode_Type()
)
cyanPmeMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMfgEciCode.setStatus("current")
_CyanPmeMfgModuleId_Type = Unsigned32
_CyanPmeMfgModuleId_Object = MibTableColumn
cyanPmeMfgModuleId = _CyanPmeMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 30),
    _CyanPmeMfgModuleId_Type()
)
cyanPmeMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMfgModuleId.setStatus("current")


class _CyanPmeMfgPartNumber_Type(DisplayString):
    """Custom type cyanPmeMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanPmeMfgPartNumber_Type.__name__ = "DisplayString"
_CyanPmeMfgPartNumber_Object = MibTableColumn
cyanPmeMfgPartNumber = _CyanPmeMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 31),
    _CyanPmeMfgPartNumber_Type()
)
cyanPmeMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMfgPartNumber.setStatus("current")


class _CyanPmeMfgRevision_Type(DisplayString):
    """Custom type cyanPmeMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanPmeMfgRevision_Type.__name__ = "DisplayString"
_CyanPmeMfgRevision_Object = MibTableColumn
cyanPmeMfgRevision = _CyanPmeMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 32),
    _CyanPmeMfgRevision_Type()
)
cyanPmeMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMfgRevision.setStatus("current")


class _CyanPmeMfgSerialNumber_Type(DisplayString):
    """Custom type cyanPmeMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanPmeMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanPmeMfgSerialNumber_Object = MibTableColumn
cyanPmeMfgSerialNumber = _CyanPmeMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 33),
    _CyanPmeMfgSerialNumber_Type()
)
cyanPmeMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeMfgSerialNumber.setStatus("current")
_CyanPmeName_Type = DisplayString
_CyanPmeName_Object = MibTableColumn
cyanPmeName = _CyanPmeName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 34),
    _CyanPmeName_Type()
)
cyanPmeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeName.setStatus("current")
_CyanPmeOidClass_Type = DisplayString
_CyanPmeOidClass_Object = MibTableColumn
cyanPmeOidClass = _CyanPmeOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 35),
    _CyanPmeOidClass_Type()
)
cyanPmeOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeOidClass.setStatus("current")
_CyanPmeOperState_Type = CyanOpStateTc
_CyanPmeOperState_Object = MibTableColumn
cyanPmeOperState = _CyanPmeOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 36),
    _CyanPmeOperState_Type()
)
cyanPmeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeOperState.setStatus("current")
_CyanPmeOperStateQual_Type = CyanOpStateQualTc
_CyanPmeOperStateQual_Object = MibTableColumn
cyanPmeOperStateQual = _CyanPmeOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 37),
    _CyanPmeOperStateQual_Type()
)
cyanPmeOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeOperStateQual.setStatus("current")


class _CyanPmeOssLabel_Type(DisplayString):
    """Custom type cyanPmeOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanPmeOssLabel_Type.__name__ = "DisplayString"
_CyanPmeOssLabel_Object = MibTableColumn
cyanPmeOssLabel = _CyanPmeOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 38),
    _CyanPmeOssLabel_Type()
)
cyanPmeOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeOssLabel.setStatus("current")
_CyanPmeOvervoltageThreshold_Type = Integer32
_CyanPmeOvervoltageThreshold_Object = MibTableColumn
cyanPmeOvervoltageThreshold = _CyanPmeOvervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 39),
    _CyanPmeOvervoltageThreshold_Type()
)
cyanPmeOvervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeOvervoltageThreshold.setStatus("current")


class _CyanPmeOwner_Type(DisplayString):
    """Custom type cyanPmeOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanPmeOwner_Type.__name__ = "DisplayString"
_CyanPmeOwner_Object = MibTableColumn
cyanPmeOwner = _CyanPmeOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 40),
    _CyanPmeOwner_Type()
)
cyanPmeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeOwner.setStatus("current")


class _CyanPmePartNumber_Type(DisplayString):
    """Custom type cyanPmePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanPmePartNumber_Type.__name__ = "DisplayString"
_CyanPmePartNumber_Object = MibTableColumn
cyanPmePartNumber = _CyanPmePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 41),
    _CyanPmePartNumber_Type()
)
cyanPmePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePartNumber.setStatus("current")
_CyanPmePowerLed_Type = CyanLEDTc
_CyanPmePowerLed_Object = MibTableColumn
cyanPmePowerLed = _CyanPmePowerLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 42),
    _CyanPmePowerLed_Type()
)
cyanPmePowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePowerLed.setStatus("current")


class _CyanPmePsuTemperature_Type(Integer32):
    """Custom type cyanPmePsuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25000, 85000),
    )


_CyanPmePsuTemperature_Type.__name__ = "Integer32"
_CyanPmePsuTemperature_Object = MibTableColumn
cyanPmePsuTemperature = _CyanPmePsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 43),
    _CyanPmePsuTemperature_Type()
)
cyanPmePsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePsuTemperature.setStatus("current")
_CyanPmePwrFeedAStatus_Type = CyanOffOnTc
_CyanPmePwrFeedAStatus_Object = MibTableColumn
cyanPmePwrFeedAStatus = _CyanPmePwrFeedAStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 44),
    _CyanPmePwrFeedAStatus_Type()
)
cyanPmePwrFeedAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePwrFeedAStatus.setStatus("current")
_CyanPmePwrFeedAVoltage_Type = Integer32
_CyanPmePwrFeedAVoltage_Object = MibTableColumn
cyanPmePwrFeedAVoltage = _CyanPmePwrFeedAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 45),
    _CyanPmePwrFeedAVoltage_Type()
)
cyanPmePwrFeedAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePwrFeedAVoltage.setStatus("current")
_CyanPmePwrFeedBStatus_Type = CyanOffOnTc
_CyanPmePwrFeedBStatus_Object = MibTableColumn
cyanPmePwrFeedBStatus = _CyanPmePwrFeedBStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 46),
    _CyanPmePwrFeedBStatus_Type()
)
cyanPmePwrFeedBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePwrFeedBStatus.setStatus("current")
_CyanPmePwrFeedBVoltage_Type = Integer32
_CyanPmePwrFeedBVoltage_Object = MibTableColumn
cyanPmePwrFeedBVoltage = _CyanPmePwrFeedBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 47),
    _CyanPmePwrFeedBVoltage_Type()
)
cyanPmePwrFeedBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmePwrFeedBVoltage.setStatus("current")


class _CyanPmeResendEthlinkoamPdus_Type(Unsigned32):
    """Custom type cyanPmeResendEthlinkoamPdus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CyanPmeResendEthlinkoamPdus_Type.__name__ = "Unsigned32"
_CyanPmeResendEthlinkoamPdus_Object = MibTableColumn
cyanPmeResendEthlinkoamPdus = _CyanPmeResendEthlinkoamPdus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 48),
    _CyanPmeResendEthlinkoamPdus_Type()
)
cyanPmeResendEthlinkoamPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeResendEthlinkoamPdus.setStatus("current")
_CyanPmeRevertCyanSwBuildVersions_Type = DisplayString
_CyanPmeRevertCyanSwBuildVersions_Object = MibTableColumn
cyanPmeRevertCyanSwBuildVersions = _CyanPmeRevertCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 49),
    _CyanPmeRevertCyanSwBuildVersions_Type()
)
cyanPmeRevertCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeRevertCyanSwBuildVersions.setStatus("current")
_CyanPmeRevertCyanSwRelease_Type = DisplayString
_CyanPmeRevertCyanSwRelease_Object = MibTableColumn
cyanPmeRevertCyanSwRelease = _CyanPmeRevertCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 50),
    _CyanPmeRevertCyanSwRelease_Type()
)
cyanPmeRevertCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeRevertCyanSwRelease.setStatus("current")
_CyanPmeSecServState_Type = CyanSecServiceStateTc
_CyanPmeSecServState_Object = MibTableColumn
cyanPmeSecServState = _CyanPmeSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 51),
    _CyanPmeSecServState_Type()
)
cyanPmeSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeSecServState.setStatus("current")
_CyanPmeSynchLed_Type = CyanLEDTc
_CyanPmeSynchLed_Object = MibTableColumn
cyanPmeSynchLed = _CyanPmeSynchLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 52),
    _CyanPmeSynchLed_Type()
)
cyanPmeSynchLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeSynchLed.setStatus("current")
_CyanPmeType_Type = CyanTypeTc
_CyanPmeType_Object = MibTableColumn
cyanPmeType = _CyanPmeType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 53),
    _CyanPmeType_Type()
)
cyanPmeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeType.setStatus("current")
_CyanPmeUndervoltageThreshold_Type = Integer32
_CyanPmeUndervoltageThreshold_Object = MibTableColumn
cyanPmeUndervoltageThreshold = _CyanPmeUndervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 54),
    _CyanPmeUndervoltageThreshold_Type()
)
cyanPmeUndervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeUndervoltageThreshold.setStatus("current")
_CyanPmeUpgradeCyanSwBuildVersions_Type = DisplayString
_CyanPmeUpgradeCyanSwBuildVersions_Object = MibTableColumn
cyanPmeUpgradeCyanSwBuildVersions = _CyanPmeUpgradeCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 55),
    _CyanPmeUpgradeCyanSwBuildVersions_Type()
)
cyanPmeUpgradeCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeUpgradeCyanSwBuildVersions.setStatus("current")
_CyanPmeUpgradeCyanSwRelease_Type = DisplayString
_CyanPmeUpgradeCyanSwRelease_Object = MibTableColumn
cyanPmeUpgradeCyanSwRelease = _CyanPmeUpgradeCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 56),
    _CyanPmeUpgradeCyanSwRelease_Type()
)
cyanPmeUpgradeCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanPmeUpgradeCyanSwRelease.setStatus("current")

# Managed Objects groups

cyanPmeObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 20)
)
cyanPmeObjectGroup.setObjects(
      *(("CYAN-PME-MIB", "cyanPmeActiveLed"),
        ("CYAN-PME-MIB", "cyanPmeActivestandbyState"),
        ("CYAN-PME-MIB", "cyanPmeAdminState"),
        ("CYAN-PME-MIB", "cyanPmeAlarmLed"),
        ("CYAN-PME-MIB", "cyanPmeAssetTag"),
        ("CYAN-PME-MIB", "cyanPmeAutoinserviceSoakTimeSec"),
        ("CYAN-PME-MIB", "cyanPmeBaseMacAddress"),
        ("CYAN-PME-MIB", "cyanPmeCurrCyanSwBuildVersions"),
        ("CYAN-PME-MIB", "cyanPmeCurrCyanSwRelease"),
        ("CYAN-PME-MIB", "cyanPmeCurrent"),
        ("CYAN-PME-MIB", "cyanPmeDescription"),
        ("CYAN-PME-MIB", "cyanPmeExhaustAirTemp"),
        ("CYAN-PME-MIB", "cyanPmeExhaustTempAlarmHighThres"),
        ("CYAN-PME-MIB", "cyanPmeExhaustTempAlarmLowThres"),
        ("CYAN-PME-MIB", "cyanPmeExhaustTempWarnHighThres"),
        ("CYAN-PME-MIB", "cyanPmeExhaustTempWarnLowThres"),
        ("CYAN-PME-MIB", "cyanPmeExpectedTemperatureRise"),
        ("CYAN-PME-MIB", "cyanPmeIdentifier"),
        ("CYAN-PME-MIB", "cyanPmeIntakeAirTemp"),
        ("CYAN-PME-MIB", "cyanPmeIntakeTempAlarmHighThres"),
        ("CYAN-PME-MIB", "cyanPmeIntakeTempAlarmLowThres"),
        ("CYAN-PME-MIB", "cyanPmeIntakeTempWarnHighThres"),
        ("CYAN-PME-MIB", "cyanPmeIntakeTempWarnLowThres"),
        ("CYAN-PME-MIB", "cyanPmeLedTest"),
        ("CYAN-PME-MIB", "cyanPmeMacBlockSize"),
        ("CYAN-PME-MIB", "cyanPmeMfgCleiCode"),
        ("CYAN-PME-MIB", "cyanPmeMfgEciCode"),
        ("CYAN-PME-MIB", "cyanPmeMfgModuleId"),
        ("CYAN-PME-MIB", "cyanPmeMfgPartNumber"),
        ("CYAN-PME-MIB", "cyanPmeMfgRevision"),
        ("CYAN-PME-MIB", "cyanPmeMfgSerialNumber"),
        ("CYAN-PME-MIB", "cyanPmeName"),
        ("CYAN-PME-MIB", "cyanPmeOidClass"),
        ("CYAN-PME-MIB", "cyanPmeOperState"),
        ("CYAN-PME-MIB", "cyanPmeOperStateQual"),
        ("CYAN-PME-MIB", "cyanPmeOssLabel"),
        ("CYAN-PME-MIB", "cyanPmeOvervoltageThreshold"),
        ("CYAN-PME-MIB", "cyanPmeOwner"),
        ("CYAN-PME-MIB", "cyanPmePartNumber"),
        ("CYAN-PME-MIB", "cyanPmePowerLed"),
        ("CYAN-PME-MIB", "cyanPmePsuTemperature"),
        ("CYAN-PME-MIB", "cyanPmePwrFeedAStatus"),
        ("CYAN-PME-MIB", "cyanPmePwrFeedAVoltage"),
        ("CYAN-PME-MIB", "cyanPmePwrFeedBStatus"),
        ("CYAN-PME-MIB", "cyanPmePwrFeedBVoltage"),
        ("CYAN-PME-MIB", "cyanPmeResendEthlinkoamPdus"),
        ("CYAN-PME-MIB", "cyanPmeRevertCyanSwBuildVersions"),
        ("CYAN-PME-MIB", "cyanPmeRevertCyanSwRelease"),
        ("CYAN-PME-MIB", "cyanPmeSecServState"),
        ("CYAN-PME-MIB", "cyanPmeSynchLed"),
        ("CYAN-PME-MIB", "cyanPmeType"),
        ("CYAN-PME-MIB", "cyanPmeUndervoltageThreshold"),
        ("CYAN-PME-MIB", "cyanPmeUpgradeCyanSwBuildVersions"),
        ("CYAN-PME-MIB", "cyanPmeUpgradeCyanSwRelease"))
)
if mibBuilder.loadTexts:
    cyanPmeObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanPmeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 30)
)
if mibBuilder.loadTexts:
    cyanPmeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-PME-MIB",
    **{"cyanPmeModule": cyanPmeModule,
       "cyanPmeMibObjects": cyanPmeMibObjects,
       "cyanPmeTable": cyanPmeTable,
       "cyanPmeEntry": cyanPmeEntry,
       "cyanPmeShelfId": cyanPmeShelfId,
       "cyanPmePmeId": cyanPmePmeId,
       "cyanPmeActiveLed": cyanPmeActiveLed,
       "cyanPmeActivestandbyState": cyanPmeActivestandbyState,
       "cyanPmeAdminState": cyanPmeAdminState,
       "cyanPmeAlarmLed": cyanPmeAlarmLed,
       "cyanPmeAssetTag": cyanPmeAssetTag,
       "cyanPmeAutoinserviceSoakTimeSec": cyanPmeAutoinserviceSoakTimeSec,
       "cyanPmeBaseMacAddress": cyanPmeBaseMacAddress,
       "cyanPmeCurrCyanSwBuildVersions": cyanPmeCurrCyanSwBuildVersions,
       "cyanPmeCurrCyanSwRelease": cyanPmeCurrCyanSwRelease,
       "cyanPmeCurrent": cyanPmeCurrent,
       "cyanPmeDescription": cyanPmeDescription,
       "cyanPmeExhaustAirTemp": cyanPmeExhaustAirTemp,
       "cyanPmeExhaustTempAlarmHighThres": cyanPmeExhaustTempAlarmHighThres,
       "cyanPmeExhaustTempAlarmLowThres": cyanPmeExhaustTempAlarmLowThres,
       "cyanPmeExhaustTempWarnHighThres": cyanPmeExhaustTempWarnHighThres,
       "cyanPmeExhaustTempWarnLowThres": cyanPmeExhaustTempWarnLowThres,
       "cyanPmeExpectedTemperatureRise": cyanPmeExpectedTemperatureRise,
       "cyanPmeIdentifier": cyanPmeIdentifier,
       "cyanPmeIntakeAirTemp": cyanPmeIntakeAirTemp,
       "cyanPmeIntakeTempAlarmHighThres": cyanPmeIntakeTempAlarmHighThres,
       "cyanPmeIntakeTempAlarmLowThres": cyanPmeIntakeTempAlarmLowThres,
       "cyanPmeIntakeTempWarnHighThres": cyanPmeIntakeTempWarnHighThres,
       "cyanPmeIntakeTempWarnLowThres": cyanPmeIntakeTempWarnLowThres,
       "cyanPmeLedTest": cyanPmeLedTest,
       "cyanPmeMacBlockSize": cyanPmeMacBlockSize,
       "cyanPmeMfgCleiCode": cyanPmeMfgCleiCode,
       "cyanPmeMfgEciCode": cyanPmeMfgEciCode,
       "cyanPmeMfgModuleId": cyanPmeMfgModuleId,
       "cyanPmeMfgPartNumber": cyanPmeMfgPartNumber,
       "cyanPmeMfgRevision": cyanPmeMfgRevision,
       "cyanPmeMfgSerialNumber": cyanPmeMfgSerialNumber,
       "cyanPmeName": cyanPmeName,
       "cyanPmeOidClass": cyanPmeOidClass,
       "cyanPmeOperState": cyanPmeOperState,
       "cyanPmeOperStateQual": cyanPmeOperStateQual,
       "cyanPmeOssLabel": cyanPmeOssLabel,
       "cyanPmeOvervoltageThreshold": cyanPmeOvervoltageThreshold,
       "cyanPmeOwner": cyanPmeOwner,
       "cyanPmePartNumber": cyanPmePartNumber,
       "cyanPmePowerLed": cyanPmePowerLed,
       "cyanPmePsuTemperature": cyanPmePsuTemperature,
       "cyanPmePwrFeedAStatus": cyanPmePwrFeedAStatus,
       "cyanPmePwrFeedAVoltage": cyanPmePwrFeedAVoltage,
       "cyanPmePwrFeedBStatus": cyanPmePwrFeedBStatus,
       "cyanPmePwrFeedBVoltage": cyanPmePwrFeedBVoltage,
       "cyanPmeResendEthlinkoamPdus": cyanPmeResendEthlinkoamPdus,
       "cyanPmeRevertCyanSwBuildVersions": cyanPmeRevertCyanSwBuildVersions,
       "cyanPmeRevertCyanSwRelease": cyanPmeRevertCyanSwRelease,
       "cyanPmeSecServState": cyanPmeSecServState,
       "cyanPmeSynchLed": cyanPmeSynchLed,
       "cyanPmeType": cyanPmeType,
       "cyanPmeUndervoltageThreshold": cyanPmeUndervoltageThreshold,
       "cyanPmeUpgradeCyanSwBuildVersions": cyanPmeUpgradeCyanSwBuildVersions,
       "cyanPmeUpgradeCyanSwRelease": cyanPmeUpgradeCyanSwRelease,
       "cyanPmeObjectGroup": cyanPmeObjectGroup,
       "cyanPmeCompliance": cyanPmeCompliance}
)
