# SNMP MIB module (CYAN-BOSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-BOSS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:04 2024
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

cyanBossModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100)
)
cyanBossModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanBossMibObjects_ObjectIdentity = ObjectIdentity
cyanBossMibObjects = _CyanBossMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1)
)
_CyanBossTable_Object = MibTable
cyanBossTable = _CyanBossTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1)
)
if mibBuilder.loadTexts:
    cyanBossTable.setStatus("current")
_CyanBossEntry_Object = MibTableRow
cyanBossEntry = _CyanBossEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1)
)
cyanBossEntry.setIndexNames(
    (0, "CYAN-BOSS-MIB", "cyanBossShelfId"),
    (0, "CYAN-BOSS-MIB", "cyanBossBossId"),
)
if mibBuilder.loadTexts:
    cyanBossEntry.setStatus("current")


class _CyanBossShelfId_Type(Unsigned32):
    """Custom type cyanBossShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanBossShelfId_Type.__name__ = "Unsigned32"
_CyanBossShelfId_Object = MibTableColumn
cyanBossShelfId = _CyanBossShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 1),
    _CyanBossShelfId_Type()
)
cyanBossShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanBossShelfId.setStatus("current")
_CyanBossBossId_Type = Unsigned32
_CyanBossBossId_Object = MibTableColumn
cyanBossBossId = _CyanBossBossId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 2),
    _CyanBossBossId_Type()
)
cyanBossBossId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanBossBossId.setStatus("current")
_CyanBossActiveLed_Type = CyanLEDTc
_CyanBossActiveLed_Object = MibTableColumn
cyanBossActiveLed = _CyanBossActiveLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 3),
    _CyanBossActiveLed_Type()
)
cyanBossActiveLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossActiveLed.setStatus("current")
_CyanBossActivestandbyState_Type = CyanActvStdbyTc
_CyanBossActivestandbyState_Object = MibTableColumn
cyanBossActivestandbyState = _CyanBossActivestandbyState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 4),
    _CyanBossActivestandbyState_Type()
)
cyanBossActivestandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossActivestandbyState.setStatus("current")
_CyanBossAdminState_Type = CyanAdminStateTc
_CyanBossAdminState_Object = MibTableColumn
cyanBossAdminState = _CyanBossAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 5),
    _CyanBossAdminState_Type()
)
cyanBossAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossAdminState.setStatus("current")
_CyanBossAlarmLed_Type = CyanLEDTc
_CyanBossAlarmLed_Object = MibTableColumn
cyanBossAlarmLed = _CyanBossAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 6),
    _CyanBossAlarmLed_Type()
)
cyanBossAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossAlarmLed.setStatus("current")


class _CyanBossAssetTag_Type(DisplayString):
    """Custom type cyanBossAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanBossAssetTag_Type.__name__ = "DisplayString"
_CyanBossAssetTag_Object = MibTableColumn
cyanBossAssetTag = _CyanBossAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 7),
    _CyanBossAssetTag_Type()
)
cyanBossAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossAssetTag.setStatus("current")
_CyanBossAutoinserviceSoakTimeSec_Type = Integer32
_CyanBossAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanBossAutoinserviceSoakTimeSec = _CyanBossAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 8),
    _CyanBossAutoinserviceSoakTimeSec_Type()
)
cyanBossAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossAutoinserviceSoakTimeSec.setStatus("current")
_CyanBossBaseMacAddress_Type = DisplayString
_CyanBossBaseMacAddress_Object = MibTableColumn
cyanBossBaseMacAddress = _CyanBossBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 9),
    _CyanBossBaseMacAddress_Type()
)
cyanBossBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossBaseMacAddress.setStatus("current")
_CyanBossCurrCyanSwBuildVersions_Type = DisplayString
_CyanBossCurrCyanSwBuildVersions_Object = MibTableColumn
cyanBossCurrCyanSwBuildVersions = _CyanBossCurrCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 10),
    _CyanBossCurrCyanSwBuildVersions_Type()
)
cyanBossCurrCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossCurrCyanSwBuildVersions.setStatus("current")
_CyanBossCurrCyanSwRelease_Type = DisplayString
_CyanBossCurrCyanSwRelease_Object = MibTableColumn
cyanBossCurrCyanSwRelease = _CyanBossCurrCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 11),
    _CyanBossCurrCyanSwRelease_Type()
)
cyanBossCurrCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossCurrCyanSwRelease.setStatus("current")
_CyanBossCurrent_Type = Integer32
_CyanBossCurrent_Object = MibTableColumn
cyanBossCurrent = _CyanBossCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 12),
    _CyanBossCurrent_Type()
)
cyanBossCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossCurrent.setStatus("current")


class _CyanBossDescription_Type(DisplayString):
    """Custom type cyanBossDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanBossDescription_Type.__name__ = "DisplayString"
_CyanBossDescription_Object = MibTableColumn
cyanBossDescription = _CyanBossDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 13),
    _CyanBossDescription_Type()
)
cyanBossDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossDescription.setStatus("current")


class _CyanBossExhaustAirTemp_Type(Integer32):
    """Custom type cyanBossExhaustAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossExhaustAirTemp_Type.__name__ = "Integer32"
_CyanBossExhaustAirTemp_Object = MibTableColumn
cyanBossExhaustAirTemp = _CyanBossExhaustAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 14),
    _CyanBossExhaustAirTemp_Type()
)
cyanBossExhaustAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossExhaustAirTemp.setStatus("current")


class _CyanBossExhaustTempAlarmHighThres_Type(Integer32):
    """Custom type cyanBossExhaustTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossExhaustTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanBossExhaustTempAlarmHighThres_Object = MibTableColumn
cyanBossExhaustTempAlarmHighThres = _CyanBossExhaustTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 15),
    _CyanBossExhaustTempAlarmHighThres_Type()
)
cyanBossExhaustTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossExhaustTempAlarmHighThres.setStatus("current")


class _CyanBossExhaustTempAlarmLowThres_Type(Integer32):
    """Custom type cyanBossExhaustTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossExhaustTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanBossExhaustTempAlarmLowThres_Object = MibTableColumn
cyanBossExhaustTempAlarmLowThres = _CyanBossExhaustTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 16),
    _CyanBossExhaustTempAlarmLowThres_Type()
)
cyanBossExhaustTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossExhaustTempAlarmLowThres.setStatus("current")


class _CyanBossExhaustTempWarnHighThres_Type(Integer32):
    """Custom type cyanBossExhaustTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossExhaustTempWarnHighThres_Type.__name__ = "Integer32"
_CyanBossExhaustTempWarnHighThres_Object = MibTableColumn
cyanBossExhaustTempWarnHighThres = _CyanBossExhaustTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 17),
    _CyanBossExhaustTempWarnHighThres_Type()
)
cyanBossExhaustTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossExhaustTempWarnHighThres.setStatus("current")


class _CyanBossExhaustTempWarnLowThres_Type(Integer32):
    """Custom type cyanBossExhaustTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossExhaustTempWarnLowThres_Type.__name__ = "Integer32"
_CyanBossExhaustTempWarnLowThres_Object = MibTableColumn
cyanBossExhaustTempWarnLowThres = _CyanBossExhaustTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 18),
    _CyanBossExhaustTempWarnLowThres_Type()
)
cyanBossExhaustTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossExhaustTempWarnLowThres.setStatus("current")
_CyanBossExpectedTemperatureRise_Type = Integer32
_CyanBossExpectedTemperatureRise_Object = MibTableColumn
cyanBossExpectedTemperatureRise = _CyanBossExpectedTemperatureRise_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 19),
    _CyanBossExpectedTemperatureRise_Type()
)
cyanBossExpectedTemperatureRise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossExpectedTemperatureRise.setStatus("current")
_CyanBossIdentifier_Type = DisplayString
_CyanBossIdentifier_Object = MibTableColumn
cyanBossIdentifier = _CyanBossIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 20),
    _CyanBossIdentifier_Type()
)
cyanBossIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossIdentifier.setStatus("current")


class _CyanBossIntakeAirTemp_Type(Integer32):
    """Custom type cyanBossIntakeAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossIntakeAirTemp_Type.__name__ = "Integer32"
_CyanBossIntakeAirTemp_Object = MibTableColumn
cyanBossIntakeAirTemp = _CyanBossIntakeAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 21),
    _CyanBossIntakeAirTemp_Type()
)
cyanBossIntakeAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossIntakeAirTemp.setStatus("current")


class _CyanBossIntakeTempAlarmHighThres_Type(Integer32):
    """Custom type cyanBossIntakeTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossIntakeTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanBossIntakeTempAlarmHighThres_Object = MibTableColumn
cyanBossIntakeTempAlarmHighThres = _CyanBossIntakeTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 22),
    _CyanBossIntakeTempAlarmHighThres_Type()
)
cyanBossIntakeTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossIntakeTempAlarmHighThres.setStatus("current")


class _CyanBossIntakeTempAlarmLowThres_Type(Integer32):
    """Custom type cyanBossIntakeTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossIntakeTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanBossIntakeTempAlarmLowThres_Object = MibTableColumn
cyanBossIntakeTempAlarmLowThres = _CyanBossIntakeTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 23),
    _CyanBossIntakeTempAlarmLowThres_Type()
)
cyanBossIntakeTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossIntakeTempAlarmLowThres.setStatus("current")


class _CyanBossIntakeTempWarnHighThres_Type(Integer32):
    """Custom type cyanBossIntakeTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossIntakeTempWarnHighThres_Type.__name__ = "Integer32"
_CyanBossIntakeTempWarnHighThres_Object = MibTableColumn
cyanBossIntakeTempWarnHighThres = _CyanBossIntakeTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 24),
    _CyanBossIntakeTempWarnHighThres_Type()
)
cyanBossIntakeTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossIntakeTempWarnHighThres.setStatus("current")


class _CyanBossIntakeTempWarnLowThres_Type(Integer32):
    """Custom type cyanBossIntakeTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanBossIntakeTempWarnLowThres_Type.__name__ = "Integer32"
_CyanBossIntakeTempWarnLowThres_Object = MibTableColumn
cyanBossIntakeTempWarnLowThres = _CyanBossIntakeTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 25),
    _CyanBossIntakeTempWarnLowThres_Type()
)
cyanBossIntakeTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossIntakeTempWarnLowThres.setStatus("current")
_CyanBossLedTest_Type = Unsigned32
_CyanBossLedTest_Object = MibTableColumn
cyanBossLedTest = _CyanBossLedTest_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 26),
    _CyanBossLedTest_Type()
)
cyanBossLedTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossLedTest.setStatus("current")


class _CyanBossMacBlockSize_Type(Unsigned32):
    """Custom type cyanBossMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanBossMacBlockSize_Type.__name__ = "Unsigned32"
_CyanBossMacBlockSize_Object = MibTableColumn
cyanBossMacBlockSize = _CyanBossMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 27),
    _CyanBossMacBlockSize_Type()
)
cyanBossMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMacBlockSize.setStatus("current")


class _CyanBossMfgCleiCode_Type(DisplayString):
    """Custom type cyanBossMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanBossMfgCleiCode_Type.__name__ = "DisplayString"
_CyanBossMfgCleiCode_Object = MibTableColumn
cyanBossMfgCleiCode = _CyanBossMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 28),
    _CyanBossMfgCleiCode_Type()
)
cyanBossMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMfgCleiCode.setStatus("current")


class _CyanBossMfgEciCode_Type(DisplayString):
    """Custom type cyanBossMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanBossMfgEciCode_Type.__name__ = "DisplayString"
_CyanBossMfgEciCode_Object = MibTableColumn
cyanBossMfgEciCode = _CyanBossMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 29),
    _CyanBossMfgEciCode_Type()
)
cyanBossMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMfgEciCode.setStatus("current")
_CyanBossMfgModuleId_Type = Unsigned32
_CyanBossMfgModuleId_Object = MibTableColumn
cyanBossMfgModuleId = _CyanBossMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 30),
    _CyanBossMfgModuleId_Type()
)
cyanBossMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMfgModuleId.setStatus("current")


class _CyanBossMfgPartNumber_Type(DisplayString):
    """Custom type cyanBossMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanBossMfgPartNumber_Type.__name__ = "DisplayString"
_CyanBossMfgPartNumber_Object = MibTableColumn
cyanBossMfgPartNumber = _CyanBossMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 31),
    _CyanBossMfgPartNumber_Type()
)
cyanBossMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMfgPartNumber.setStatus("current")


class _CyanBossMfgRevision_Type(DisplayString):
    """Custom type cyanBossMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanBossMfgRevision_Type.__name__ = "DisplayString"
_CyanBossMfgRevision_Object = MibTableColumn
cyanBossMfgRevision = _CyanBossMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 32),
    _CyanBossMfgRevision_Type()
)
cyanBossMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMfgRevision.setStatus("current")


class _CyanBossMfgSerialNumber_Type(DisplayString):
    """Custom type cyanBossMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanBossMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanBossMfgSerialNumber_Object = MibTableColumn
cyanBossMfgSerialNumber = _CyanBossMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 33),
    _CyanBossMfgSerialNumber_Type()
)
cyanBossMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossMfgSerialNumber.setStatus("current")
_CyanBossName_Type = DisplayString
_CyanBossName_Object = MibTableColumn
cyanBossName = _CyanBossName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 34),
    _CyanBossName_Type()
)
cyanBossName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossName.setStatus("current")
_CyanBossOidClass_Type = DisplayString
_CyanBossOidClass_Object = MibTableColumn
cyanBossOidClass = _CyanBossOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 35),
    _CyanBossOidClass_Type()
)
cyanBossOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossOidClass.setStatus("current")
_CyanBossOperState_Type = CyanOpStateTc
_CyanBossOperState_Object = MibTableColumn
cyanBossOperState = _CyanBossOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 36),
    _CyanBossOperState_Type()
)
cyanBossOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossOperState.setStatus("current")
_CyanBossOperStateQual_Type = CyanOpStateQualTc
_CyanBossOperStateQual_Object = MibTableColumn
cyanBossOperStateQual = _CyanBossOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 37),
    _CyanBossOperStateQual_Type()
)
cyanBossOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossOperStateQual.setStatus("current")


class _CyanBossOssLabel_Type(DisplayString):
    """Custom type cyanBossOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanBossOssLabel_Type.__name__ = "DisplayString"
_CyanBossOssLabel_Object = MibTableColumn
cyanBossOssLabel = _CyanBossOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 38),
    _CyanBossOssLabel_Type()
)
cyanBossOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossOssLabel.setStatus("current")
_CyanBossOvervoltageThreshold_Type = Integer32
_CyanBossOvervoltageThreshold_Object = MibTableColumn
cyanBossOvervoltageThreshold = _CyanBossOvervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 39),
    _CyanBossOvervoltageThreshold_Type()
)
cyanBossOvervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossOvervoltageThreshold.setStatus("current")


class _CyanBossOwner_Type(DisplayString):
    """Custom type cyanBossOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanBossOwner_Type.__name__ = "DisplayString"
_CyanBossOwner_Object = MibTableColumn
cyanBossOwner = _CyanBossOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 40),
    _CyanBossOwner_Type()
)
cyanBossOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossOwner.setStatus("current")


class _CyanBossPartNumber_Type(DisplayString):
    """Custom type cyanBossPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanBossPartNumber_Type.__name__ = "DisplayString"
_CyanBossPartNumber_Object = MibTableColumn
cyanBossPartNumber = _CyanBossPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 41),
    _CyanBossPartNumber_Type()
)
cyanBossPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPartNumber.setStatus("current")
_CyanBossPowerLed_Type = CyanLEDTc
_CyanBossPowerLed_Object = MibTableColumn
cyanBossPowerLed = _CyanBossPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 42),
    _CyanBossPowerLed_Type()
)
cyanBossPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPowerLed.setStatus("current")


class _CyanBossPsuTemperature_Type(Integer32):
    """Custom type cyanBossPsuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25000, 85000),
    )


_CyanBossPsuTemperature_Type.__name__ = "Integer32"
_CyanBossPsuTemperature_Object = MibTableColumn
cyanBossPsuTemperature = _CyanBossPsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 43),
    _CyanBossPsuTemperature_Type()
)
cyanBossPsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPsuTemperature.setStatus("current")
_CyanBossPwrFeedAStatus_Type = CyanOffOnTc
_CyanBossPwrFeedAStatus_Object = MibTableColumn
cyanBossPwrFeedAStatus = _CyanBossPwrFeedAStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 44),
    _CyanBossPwrFeedAStatus_Type()
)
cyanBossPwrFeedAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPwrFeedAStatus.setStatus("current")
_CyanBossPwrFeedAVoltage_Type = Integer32
_CyanBossPwrFeedAVoltage_Object = MibTableColumn
cyanBossPwrFeedAVoltage = _CyanBossPwrFeedAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 45),
    _CyanBossPwrFeedAVoltage_Type()
)
cyanBossPwrFeedAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPwrFeedAVoltage.setStatus("current")
_CyanBossPwrFeedBStatus_Type = CyanOffOnTc
_CyanBossPwrFeedBStatus_Object = MibTableColumn
cyanBossPwrFeedBStatus = _CyanBossPwrFeedBStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 46),
    _CyanBossPwrFeedBStatus_Type()
)
cyanBossPwrFeedBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPwrFeedBStatus.setStatus("current")
_CyanBossPwrFeedBVoltage_Type = Integer32
_CyanBossPwrFeedBVoltage_Object = MibTableColumn
cyanBossPwrFeedBVoltage = _CyanBossPwrFeedBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 47),
    _CyanBossPwrFeedBVoltage_Type()
)
cyanBossPwrFeedBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossPwrFeedBVoltage.setStatus("current")
_CyanBossRevertCyanSwBuildVersions_Type = DisplayString
_CyanBossRevertCyanSwBuildVersions_Object = MibTableColumn
cyanBossRevertCyanSwBuildVersions = _CyanBossRevertCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 48),
    _CyanBossRevertCyanSwBuildVersions_Type()
)
cyanBossRevertCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossRevertCyanSwBuildVersions.setStatus("current")
_CyanBossRevertCyanSwRelease_Type = DisplayString
_CyanBossRevertCyanSwRelease_Object = MibTableColumn
cyanBossRevertCyanSwRelease = _CyanBossRevertCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 49),
    _CyanBossRevertCyanSwRelease_Type()
)
cyanBossRevertCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossRevertCyanSwRelease.setStatus("current")
_CyanBossSecServState_Type = CyanSecServiceStateTc
_CyanBossSecServState_Object = MibTableColumn
cyanBossSecServState = _CyanBossSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 50),
    _CyanBossSecServState_Type()
)
cyanBossSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossSecServState.setStatus("current")
_CyanBossSynchLed_Type = CyanLEDTc
_CyanBossSynchLed_Object = MibTableColumn
cyanBossSynchLed = _CyanBossSynchLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 51),
    _CyanBossSynchLed_Type()
)
cyanBossSynchLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossSynchLed.setStatus("current")
_CyanBossType_Type = CyanTypeTc
_CyanBossType_Object = MibTableColumn
cyanBossType = _CyanBossType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 52),
    _CyanBossType_Type()
)
cyanBossType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossType.setStatus("current")
_CyanBossUndervoltageThreshold_Type = Integer32
_CyanBossUndervoltageThreshold_Object = MibTableColumn
cyanBossUndervoltageThreshold = _CyanBossUndervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 53),
    _CyanBossUndervoltageThreshold_Type()
)
cyanBossUndervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossUndervoltageThreshold.setStatus("current")
_CyanBossUpgradeCyanSwBuildVersions_Type = DisplayString
_CyanBossUpgradeCyanSwBuildVersions_Object = MibTableColumn
cyanBossUpgradeCyanSwBuildVersions = _CyanBossUpgradeCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 54),
    _CyanBossUpgradeCyanSwBuildVersions_Type()
)
cyanBossUpgradeCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossUpgradeCyanSwBuildVersions.setStatus("current")
_CyanBossUpgradeCyanSwRelease_Type = DisplayString
_CyanBossUpgradeCyanSwRelease_Object = MibTableColumn
cyanBossUpgradeCyanSwRelease = _CyanBossUpgradeCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 1, 1, 1, 55),
    _CyanBossUpgradeCyanSwRelease_Type()
)
cyanBossUpgradeCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanBossUpgradeCyanSwRelease.setStatus("current")

# Managed Objects groups

cyanBossObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 20)
)
cyanBossObjectGroup.setObjects(
      *(("CYAN-BOSS-MIB", "cyanBossActiveLed"),
        ("CYAN-BOSS-MIB", "cyanBossActivestandbyState"),
        ("CYAN-BOSS-MIB", "cyanBossAdminState"),
        ("CYAN-BOSS-MIB", "cyanBossAlarmLed"),
        ("CYAN-BOSS-MIB", "cyanBossAssetTag"),
        ("CYAN-BOSS-MIB", "cyanBossAutoinserviceSoakTimeSec"),
        ("CYAN-BOSS-MIB", "cyanBossBaseMacAddress"),
        ("CYAN-BOSS-MIB", "cyanBossCurrCyanSwBuildVersions"),
        ("CYAN-BOSS-MIB", "cyanBossCurrCyanSwRelease"),
        ("CYAN-BOSS-MIB", "cyanBossCurrent"),
        ("CYAN-BOSS-MIB", "cyanBossDescription"),
        ("CYAN-BOSS-MIB", "cyanBossExhaustAirTemp"),
        ("CYAN-BOSS-MIB", "cyanBossExhaustTempAlarmHighThres"),
        ("CYAN-BOSS-MIB", "cyanBossExhaustTempAlarmLowThres"),
        ("CYAN-BOSS-MIB", "cyanBossExhaustTempWarnHighThres"),
        ("CYAN-BOSS-MIB", "cyanBossExhaustTempWarnLowThres"),
        ("CYAN-BOSS-MIB", "cyanBossExpectedTemperatureRise"),
        ("CYAN-BOSS-MIB", "cyanBossIdentifier"),
        ("CYAN-BOSS-MIB", "cyanBossIntakeAirTemp"),
        ("CYAN-BOSS-MIB", "cyanBossIntakeTempAlarmHighThres"),
        ("CYAN-BOSS-MIB", "cyanBossIntakeTempAlarmLowThres"),
        ("CYAN-BOSS-MIB", "cyanBossIntakeTempWarnHighThres"),
        ("CYAN-BOSS-MIB", "cyanBossIntakeTempWarnLowThres"),
        ("CYAN-BOSS-MIB", "cyanBossLedTest"),
        ("CYAN-BOSS-MIB", "cyanBossMacBlockSize"),
        ("CYAN-BOSS-MIB", "cyanBossMfgCleiCode"),
        ("CYAN-BOSS-MIB", "cyanBossMfgEciCode"),
        ("CYAN-BOSS-MIB", "cyanBossMfgModuleId"),
        ("CYAN-BOSS-MIB", "cyanBossMfgPartNumber"),
        ("CYAN-BOSS-MIB", "cyanBossMfgRevision"),
        ("CYAN-BOSS-MIB", "cyanBossMfgSerialNumber"),
        ("CYAN-BOSS-MIB", "cyanBossName"),
        ("CYAN-BOSS-MIB", "cyanBossOidClass"),
        ("CYAN-BOSS-MIB", "cyanBossOperState"),
        ("CYAN-BOSS-MIB", "cyanBossOperStateQual"),
        ("CYAN-BOSS-MIB", "cyanBossOssLabel"),
        ("CYAN-BOSS-MIB", "cyanBossOvervoltageThreshold"),
        ("CYAN-BOSS-MIB", "cyanBossOwner"),
        ("CYAN-BOSS-MIB", "cyanBossPartNumber"),
        ("CYAN-BOSS-MIB", "cyanBossPowerLed"),
        ("CYAN-BOSS-MIB", "cyanBossPsuTemperature"),
        ("CYAN-BOSS-MIB", "cyanBossPwrFeedAStatus"),
        ("CYAN-BOSS-MIB", "cyanBossPwrFeedAVoltage"),
        ("CYAN-BOSS-MIB", "cyanBossPwrFeedBStatus"),
        ("CYAN-BOSS-MIB", "cyanBossPwrFeedBVoltage"),
        ("CYAN-BOSS-MIB", "cyanBossRevertCyanSwBuildVersions"),
        ("CYAN-BOSS-MIB", "cyanBossRevertCyanSwRelease"),
        ("CYAN-BOSS-MIB", "cyanBossSecServState"),
        ("CYAN-BOSS-MIB", "cyanBossSynchLed"),
        ("CYAN-BOSS-MIB", "cyanBossType"),
        ("CYAN-BOSS-MIB", "cyanBossUndervoltageThreshold"),
        ("CYAN-BOSS-MIB", "cyanBossUpgradeCyanSwBuildVersions"),
        ("CYAN-BOSS-MIB", "cyanBossUpgradeCyanSwRelease"))
)
if mibBuilder.loadTexts:
    cyanBossObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanBossCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 100, 30)
)
if mibBuilder.loadTexts:
    cyanBossCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-BOSS-MIB",
    **{"cyanBossModule": cyanBossModule,
       "cyanBossMibObjects": cyanBossMibObjects,
       "cyanBossTable": cyanBossTable,
       "cyanBossEntry": cyanBossEntry,
       "cyanBossShelfId": cyanBossShelfId,
       "cyanBossBossId": cyanBossBossId,
       "cyanBossActiveLed": cyanBossActiveLed,
       "cyanBossActivestandbyState": cyanBossActivestandbyState,
       "cyanBossAdminState": cyanBossAdminState,
       "cyanBossAlarmLed": cyanBossAlarmLed,
       "cyanBossAssetTag": cyanBossAssetTag,
       "cyanBossAutoinserviceSoakTimeSec": cyanBossAutoinserviceSoakTimeSec,
       "cyanBossBaseMacAddress": cyanBossBaseMacAddress,
       "cyanBossCurrCyanSwBuildVersions": cyanBossCurrCyanSwBuildVersions,
       "cyanBossCurrCyanSwRelease": cyanBossCurrCyanSwRelease,
       "cyanBossCurrent": cyanBossCurrent,
       "cyanBossDescription": cyanBossDescription,
       "cyanBossExhaustAirTemp": cyanBossExhaustAirTemp,
       "cyanBossExhaustTempAlarmHighThres": cyanBossExhaustTempAlarmHighThres,
       "cyanBossExhaustTempAlarmLowThres": cyanBossExhaustTempAlarmLowThres,
       "cyanBossExhaustTempWarnHighThres": cyanBossExhaustTempWarnHighThres,
       "cyanBossExhaustTempWarnLowThres": cyanBossExhaustTempWarnLowThres,
       "cyanBossExpectedTemperatureRise": cyanBossExpectedTemperatureRise,
       "cyanBossIdentifier": cyanBossIdentifier,
       "cyanBossIntakeAirTemp": cyanBossIntakeAirTemp,
       "cyanBossIntakeTempAlarmHighThres": cyanBossIntakeTempAlarmHighThres,
       "cyanBossIntakeTempAlarmLowThres": cyanBossIntakeTempAlarmLowThres,
       "cyanBossIntakeTempWarnHighThres": cyanBossIntakeTempWarnHighThres,
       "cyanBossIntakeTempWarnLowThres": cyanBossIntakeTempWarnLowThres,
       "cyanBossLedTest": cyanBossLedTest,
       "cyanBossMacBlockSize": cyanBossMacBlockSize,
       "cyanBossMfgCleiCode": cyanBossMfgCleiCode,
       "cyanBossMfgEciCode": cyanBossMfgEciCode,
       "cyanBossMfgModuleId": cyanBossMfgModuleId,
       "cyanBossMfgPartNumber": cyanBossMfgPartNumber,
       "cyanBossMfgRevision": cyanBossMfgRevision,
       "cyanBossMfgSerialNumber": cyanBossMfgSerialNumber,
       "cyanBossName": cyanBossName,
       "cyanBossOidClass": cyanBossOidClass,
       "cyanBossOperState": cyanBossOperState,
       "cyanBossOperStateQual": cyanBossOperStateQual,
       "cyanBossOssLabel": cyanBossOssLabel,
       "cyanBossOvervoltageThreshold": cyanBossOvervoltageThreshold,
       "cyanBossOwner": cyanBossOwner,
       "cyanBossPartNumber": cyanBossPartNumber,
       "cyanBossPowerLed": cyanBossPowerLed,
       "cyanBossPsuTemperature": cyanBossPsuTemperature,
       "cyanBossPwrFeedAStatus": cyanBossPwrFeedAStatus,
       "cyanBossPwrFeedAVoltage": cyanBossPwrFeedAVoltage,
       "cyanBossPwrFeedBStatus": cyanBossPwrFeedBStatus,
       "cyanBossPwrFeedBVoltage": cyanBossPwrFeedBVoltage,
       "cyanBossRevertCyanSwBuildVersions": cyanBossRevertCyanSwBuildVersions,
       "cyanBossRevertCyanSwRelease": cyanBossRevertCyanSwRelease,
       "cyanBossSecServState": cyanBossSecServState,
       "cyanBossSynchLed": cyanBossSynchLed,
       "cyanBossType": cyanBossType,
       "cyanBossUndervoltageThreshold": cyanBossUndervoltageThreshold,
       "cyanBossUpgradeCyanSwBuildVersions": cyanBossUpgradeCyanSwBuildVersions,
       "cyanBossUpgradeCyanSwRelease": cyanBossUpgradeCyanSwRelease,
       "cyanBossObjectGroup": cyanBossObjectGroup,
       "cyanBossCompliance": cyanBossCompliance}
)
