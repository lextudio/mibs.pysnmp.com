# SNMP MIB module (CYAN-DTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-DTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:06 2024
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

cyanDtmModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120)
)
cyanDtmModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanDtmMibObjects_ObjectIdentity = ObjectIdentity
cyanDtmMibObjects = _CyanDtmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1)
)
_CyanDtmTable_Object = MibTable
cyanDtmTable = _CyanDtmTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1)
)
if mibBuilder.loadTexts:
    cyanDtmTable.setStatus("current")
_CyanDtmEntry_Object = MibTableRow
cyanDtmEntry = _CyanDtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1)
)
cyanDtmEntry.setIndexNames(
    (0, "CYAN-DTM-MIB", "cyanDtmShelfId"),
    (0, "CYAN-DTM-MIB", "cyanDtmDtmId"),
)
if mibBuilder.loadTexts:
    cyanDtmEntry.setStatus("current")


class _CyanDtmShelfId_Type(Unsigned32):
    """Custom type cyanDtmShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanDtmShelfId_Type.__name__ = "Unsigned32"
_CyanDtmShelfId_Object = MibTableColumn
cyanDtmShelfId = _CyanDtmShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 1),
    _CyanDtmShelfId_Type()
)
cyanDtmShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanDtmShelfId.setStatus("current")
_CyanDtmDtmId_Type = Unsigned32
_CyanDtmDtmId_Object = MibTableColumn
cyanDtmDtmId = _CyanDtmDtmId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 2),
    _CyanDtmDtmId_Type()
)
cyanDtmDtmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanDtmDtmId.setStatus("current")
_CyanDtmActiveLed_Type = CyanLEDTc
_CyanDtmActiveLed_Object = MibTableColumn
cyanDtmActiveLed = _CyanDtmActiveLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 3),
    _CyanDtmActiveLed_Type()
)
cyanDtmActiveLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmActiveLed.setStatus("current")
_CyanDtmActivestandbyState_Type = CyanActvStdbyTc
_CyanDtmActivestandbyState_Object = MibTableColumn
cyanDtmActivestandbyState = _CyanDtmActivestandbyState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 4),
    _CyanDtmActivestandbyState_Type()
)
cyanDtmActivestandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmActivestandbyState.setStatus("current")
_CyanDtmAdminState_Type = CyanAdminStateTc
_CyanDtmAdminState_Object = MibTableColumn
cyanDtmAdminState = _CyanDtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 5),
    _CyanDtmAdminState_Type()
)
cyanDtmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmAdminState.setStatus("current")
_CyanDtmAlarmLed_Type = CyanLEDTc
_CyanDtmAlarmLed_Object = MibTableColumn
cyanDtmAlarmLed = _CyanDtmAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 6),
    _CyanDtmAlarmLed_Type()
)
cyanDtmAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmAlarmLed.setStatus("current")


class _CyanDtmAssetTag_Type(DisplayString):
    """Custom type cyanDtmAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 124),
    )


_CyanDtmAssetTag_Type.__name__ = "DisplayString"
_CyanDtmAssetTag_Object = MibTableColumn
cyanDtmAssetTag = _CyanDtmAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 7),
    _CyanDtmAssetTag_Type()
)
cyanDtmAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmAssetTag.setStatus("current")
_CyanDtmAutoinserviceSoakTimeSec_Type = Integer32
_CyanDtmAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanDtmAutoinserviceSoakTimeSec = _CyanDtmAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 8),
    _CyanDtmAutoinserviceSoakTimeSec_Type()
)
cyanDtmAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmAutoinserviceSoakTimeSec.setStatus("current")
_CyanDtmBaseMacAddress_Type = DisplayString
_CyanDtmBaseMacAddress_Object = MibTableColumn
cyanDtmBaseMacAddress = _CyanDtmBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 9),
    _CyanDtmBaseMacAddress_Type()
)
cyanDtmBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmBaseMacAddress.setStatus("current")
_CyanDtmCurrCyanSwBuildVersions_Type = DisplayString
_CyanDtmCurrCyanSwBuildVersions_Object = MibTableColumn
cyanDtmCurrCyanSwBuildVersions = _CyanDtmCurrCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 10),
    _CyanDtmCurrCyanSwBuildVersions_Type()
)
cyanDtmCurrCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmCurrCyanSwBuildVersions.setStatus("current")
_CyanDtmCurrCyanSwRelease_Type = DisplayString
_CyanDtmCurrCyanSwRelease_Object = MibTableColumn
cyanDtmCurrCyanSwRelease = _CyanDtmCurrCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 11),
    _CyanDtmCurrCyanSwRelease_Type()
)
cyanDtmCurrCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmCurrCyanSwRelease.setStatus("current")
_CyanDtmCurrent_Type = Integer32
_CyanDtmCurrent_Object = MibTableColumn
cyanDtmCurrent = _CyanDtmCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 12),
    _CyanDtmCurrent_Type()
)
cyanDtmCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmCurrent.setStatus("current")


class _CyanDtmDescription_Type(DisplayString):
    """Custom type cyanDtmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanDtmDescription_Type.__name__ = "DisplayString"
_CyanDtmDescription_Object = MibTableColumn
cyanDtmDescription = _CyanDtmDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 13),
    _CyanDtmDescription_Type()
)
cyanDtmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmDescription.setStatus("current")


class _CyanDtmExhaustAirTemp_Type(Integer32):
    """Custom type cyanDtmExhaustAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmExhaustAirTemp_Type.__name__ = "Integer32"
_CyanDtmExhaustAirTemp_Object = MibTableColumn
cyanDtmExhaustAirTemp = _CyanDtmExhaustAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 14),
    _CyanDtmExhaustAirTemp_Type()
)
cyanDtmExhaustAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmExhaustAirTemp.setStatus("current")


class _CyanDtmExhaustTempAlarmHighThres_Type(Integer32):
    """Custom type cyanDtmExhaustTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmExhaustTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanDtmExhaustTempAlarmHighThres_Object = MibTableColumn
cyanDtmExhaustTempAlarmHighThres = _CyanDtmExhaustTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 15),
    _CyanDtmExhaustTempAlarmHighThres_Type()
)
cyanDtmExhaustTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmExhaustTempAlarmHighThres.setStatus("current")


class _CyanDtmExhaustTempAlarmLowThres_Type(Integer32):
    """Custom type cyanDtmExhaustTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmExhaustTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanDtmExhaustTempAlarmLowThres_Object = MibTableColumn
cyanDtmExhaustTempAlarmLowThres = _CyanDtmExhaustTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 16),
    _CyanDtmExhaustTempAlarmLowThres_Type()
)
cyanDtmExhaustTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmExhaustTempAlarmLowThres.setStatus("current")


class _CyanDtmExhaustTempWarnHighThres_Type(Integer32):
    """Custom type cyanDtmExhaustTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmExhaustTempWarnHighThres_Type.__name__ = "Integer32"
_CyanDtmExhaustTempWarnHighThres_Object = MibTableColumn
cyanDtmExhaustTempWarnHighThres = _CyanDtmExhaustTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 17),
    _CyanDtmExhaustTempWarnHighThres_Type()
)
cyanDtmExhaustTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmExhaustTempWarnHighThres.setStatus("current")


class _CyanDtmExhaustTempWarnLowThres_Type(Integer32):
    """Custom type cyanDtmExhaustTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmExhaustTempWarnLowThres_Type.__name__ = "Integer32"
_CyanDtmExhaustTempWarnLowThres_Object = MibTableColumn
cyanDtmExhaustTempWarnLowThres = _CyanDtmExhaustTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 18),
    _CyanDtmExhaustTempWarnLowThres_Type()
)
cyanDtmExhaustTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmExhaustTempWarnLowThres.setStatus("current")
_CyanDtmExpectedTemperatureRise_Type = Integer32
_CyanDtmExpectedTemperatureRise_Object = MibTableColumn
cyanDtmExpectedTemperatureRise = _CyanDtmExpectedTemperatureRise_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 19),
    _CyanDtmExpectedTemperatureRise_Type()
)
cyanDtmExpectedTemperatureRise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmExpectedTemperatureRise.setStatus("current")
_CyanDtmIdentifier_Type = DisplayString
_CyanDtmIdentifier_Object = MibTableColumn
cyanDtmIdentifier = _CyanDtmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 20),
    _CyanDtmIdentifier_Type()
)
cyanDtmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmIdentifier.setStatus("current")


class _CyanDtmIntakeAirTemp_Type(Integer32):
    """Custom type cyanDtmIntakeAirTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmIntakeAirTemp_Type.__name__ = "Integer32"
_CyanDtmIntakeAirTemp_Object = MibTableColumn
cyanDtmIntakeAirTemp = _CyanDtmIntakeAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 21),
    _CyanDtmIntakeAirTemp_Type()
)
cyanDtmIntakeAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmIntakeAirTemp.setStatus("current")


class _CyanDtmIntakeTempAlarmHighThres_Type(Integer32):
    """Custom type cyanDtmIntakeTempAlarmHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmIntakeTempAlarmHighThres_Type.__name__ = "Integer32"
_CyanDtmIntakeTempAlarmHighThres_Object = MibTableColumn
cyanDtmIntakeTempAlarmHighThres = _CyanDtmIntakeTempAlarmHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 22),
    _CyanDtmIntakeTempAlarmHighThres_Type()
)
cyanDtmIntakeTempAlarmHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmIntakeTempAlarmHighThres.setStatus("current")


class _CyanDtmIntakeTempAlarmLowThres_Type(Integer32):
    """Custom type cyanDtmIntakeTempAlarmLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmIntakeTempAlarmLowThres_Type.__name__ = "Integer32"
_CyanDtmIntakeTempAlarmLowThres_Object = MibTableColumn
cyanDtmIntakeTempAlarmLowThres = _CyanDtmIntakeTempAlarmLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 23),
    _CyanDtmIntakeTempAlarmLowThres_Type()
)
cyanDtmIntakeTempAlarmLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmIntakeTempAlarmLowThres.setStatus("current")


class _CyanDtmIntakeTempWarnHighThres_Type(Integer32):
    """Custom type cyanDtmIntakeTempWarnHighThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmIntakeTempWarnHighThres_Type.__name__ = "Integer32"
_CyanDtmIntakeTempWarnHighThres_Object = MibTableColumn
cyanDtmIntakeTempWarnHighThres = _CyanDtmIntakeTempWarnHighThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 24),
    _CyanDtmIntakeTempWarnHighThres_Type()
)
cyanDtmIntakeTempWarnHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmIntakeTempWarnHighThres.setStatus("current")


class _CyanDtmIntakeTempWarnLowThres_Type(Integer32):
    """Custom type cyanDtmIntakeTempWarnLowThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_CyanDtmIntakeTempWarnLowThres_Type.__name__ = "Integer32"
_CyanDtmIntakeTempWarnLowThres_Object = MibTableColumn
cyanDtmIntakeTempWarnLowThres = _CyanDtmIntakeTempWarnLowThres_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 25),
    _CyanDtmIntakeTempWarnLowThres_Type()
)
cyanDtmIntakeTempWarnLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmIntakeTempWarnLowThres.setStatus("current")
_CyanDtmLedTest_Type = Unsigned32
_CyanDtmLedTest_Object = MibTableColumn
cyanDtmLedTest = _CyanDtmLedTest_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 26),
    _CyanDtmLedTest_Type()
)
cyanDtmLedTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmLedTest.setStatus("current")


class _CyanDtmMacBlockSize_Type(Unsigned32):
    """Custom type cyanDtmMacBlockSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanDtmMacBlockSize_Type.__name__ = "Unsigned32"
_CyanDtmMacBlockSize_Object = MibTableColumn
cyanDtmMacBlockSize = _CyanDtmMacBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 27),
    _CyanDtmMacBlockSize_Type()
)
cyanDtmMacBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMacBlockSize.setStatus("current")


class _CyanDtmMfgCleiCode_Type(DisplayString):
    """Custom type cyanDtmMfgCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CyanDtmMfgCleiCode_Type.__name__ = "DisplayString"
_CyanDtmMfgCleiCode_Object = MibTableColumn
cyanDtmMfgCleiCode = _CyanDtmMfgCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 28),
    _CyanDtmMfgCleiCode_Type()
)
cyanDtmMfgCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMfgCleiCode.setStatus("current")


class _CyanDtmMfgEciCode_Type(DisplayString):
    """Custom type cyanDtmMfgEciCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CyanDtmMfgEciCode_Type.__name__ = "DisplayString"
_CyanDtmMfgEciCode_Object = MibTableColumn
cyanDtmMfgEciCode = _CyanDtmMfgEciCode_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 29),
    _CyanDtmMfgEciCode_Type()
)
cyanDtmMfgEciCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMfgEciCode.setStatus("current")
_CyanDtmMfgModuleId_Type = Unsigned32
_CyanDtmMfgModuleId_Object = MibTableColumn
cyanDtmMfgModuleId = _CyanDtmMfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 30),
    _CyanDtmMfgModuleId_Type()
)
cyanDtmMfgModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMfgModuleId.setStatus("current")


class _CyanDtmMfgPartNumber_Type(DisplayString):
    """Custom type cyanDtmMfgPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanDtmMfgPartNumber_Type.__name__ = "DisplayString"
_CyanDtmMfgPartNumber_Object = MibTableColumn
cyanDtmMfgPartNumber = _CyanDtmMfgPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 31),
    _CyanDtmMfgPartNumber_Type()
)
cyanDtmMfgPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMfgPartNumber.setStatus("current")


class _CyanDtmMfgRevision_Type(DisplayString):
    """Custom type cyanDtmMfgRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CyanDtmMfgRevision_Type.__name__ = "DisplayString"
_CyanDtmMfgRevision_Object = MibTableColumn
cyanDtmMfgRevision = _CyanDtmMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 32),
    _CyanDtmMfgRevision_Type()
)
cyanDtmMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMfgRevision.setStatus("current")


class _CyanDtmMfgSerialNumber_Type(DisplayString):
    """Custom type cyanDtmMfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CyanDtmMfgSerialNumber_Type.__name__ = "DisplayString"
_CyanDtmMfgSerialNumber_Object = MibTableColumn
cyanDtmMfgSerialNumber = _CyanDtmMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 33),
    _CyanDtmMfgSerialNumber_Type()
)
cyanDtmMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmMfgSerialNumber.setStatus("current")
_CyanDtmName_Type = DisplayString
_CyanDtmName_Object = MibTableColumn
cyanDtmName = _CyanDtmName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 34),
    _CyanDtmName_Type()
)
cyanDtmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmName.setStatus("current")
_CyanDtmOidClass_Type = DisplayString
_CyanDtmOidClass_Object = MibTableColumn
cyanDtmOidClass = _CyanDtmOidClass_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 35),
    _CyanDtmOidClass_Type()
)
cyanDtmOidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmOidClass.setStatus("current")
_CyanDtmOperState_Type = CyanOpStateTc
_CyanDtmOperState_Object = MibTableColumn
cyanDtmOperState = _CyanDtmOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 36),
    _CyanDtmOperState_Type()
)
cyanDtmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmOperState.setStatus("current")
_CyanDtmOperStateQual_Type = CyanOpStateQualTc
_CyanDtmOperStateQual_Object = MibTableColumn
cyanDtmOperStateQual = _CyanDtmOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 37),
    _CyanDtmOperStateQual_Type()
)
cyanDtmOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmOperStateQual.setStatus("current")


class _CyanDtmOssLabel_Type(DisplayString):
    """Custom type cyanDtmOssLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanDtmOssLabel_Type.__name__ = "DisplayString"
_CyanDtmOssLabel_Object = MibTableColumn
cyanDtmOssLabel = _CyanDtmOssLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 38),
    _CyanDtmOssLabel_Type()
)
cyanDtmOssLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmOssLabel.setStatus("current")
_CyanDtmOvervoltageThreshold_Type = Integer32
_CyanDtmOvervoltageThreshold_Object = MibTableColumn
cyanDtmOvervoltageThreshold = _CyanDtmOvervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 39),
    _CyanDtmOvervoltageThreshold_Type()
)
cyanDtmOvervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmOvervoltageThreshold.setStatus("current")


class _CyanDtmOwner_Type(DisplayString):
    """Custom type cyanDtmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CyanDtmOwner_Type.__name__ = "DisplayString"
_CyanDtmOwner_Object = MibTableColumn
cyanDtmOwner = _CyanDtmOwner_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 40),
    _CyanDtmOwner_Type()
)
cyanDtmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmOwner.setStatus("current")


class _CyanDtmPartNumber_Type(DisplayString):
    """Custom type cyanDtmPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CyanDtmPartNumber_Type.__name__ = "DisplayString"
_CyanDtmPartNumber_Object = MibTableColumn
cyanDtmPartNumber = _CyanDtmPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 41),
    _CyanDtmPartNumber_Type()
)
cyanDtmPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPartNumber.setStatus("current")
_CyanDtmPowerLed_Type = CyanLEDTc
_CyanDtmPowerLed_Object = MibTableColumn
cyanDtmPowerLed = _CyanDtmPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 42),
    _CyanDtmPowerLed_Type()
)
cyanDtmPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPowerLed.setStatus("current")


class _CyanDtmPsuTemperature_Type(Integer32):
    """Custom type cyanDtmPsuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25000, 85000),
    )


_CyanDtmPsuTemperature_Type.__name__ = "Integer32"
_CyanDtmPsuTemperature_Object = MibTableColumn
cyanDtmPsuTemperature = _CyanDtmPsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 43),
    _CyanDtmPsuTemperature_Type()
)
cyanDtmPsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPsuTemperature.setStatus("current")
_CyanDtmPwrFeedAStatus_Type = CyanOffOnTc
_CyanDtmPwrFeedAStatus_Object = MibTableColumn
cyanDtmPwrFeedAStatus = _CyanDtmPwrFeedAStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 44),
    _CyanDtmPwrFeedAStatus_Type()
)
cyanDtmPwrFeedAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPwrFeedAStatus.setStatus("current")
_CyanDtmPwrFeedAVoltage_Type = Integer32
_CyanDtmPwrFeedAVoltage_Object = MibTableColumn
cyanDtmPwrFeedAVoltage = _CyanDtmPwrFeedAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 45),
    _CyanDtmPwrFeedAVoltage_Type()
)
cyanDtmPwrFeedAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPwrFeedAVoltage.setStatus("current")
_CyanDtmPwrFeedBStatus_Type = CyanOffOnTc
_CyanDtmPwrFeedBStatus_Object = MibTableColumn
cyanDtmPwrFeedBStatus = _CyanDtmPwrFeedBStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 46),
    _CyanDtmPwrFeedBStatus_Type()
)
cyanDtmPwrFeedBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPwrFeedBStatus.setStatus("current")
_CyanDtmPwrFeedBVoltage_Type = Integer32
_CyanDtmPwrFeedBVoltage_Object = MibTableColumn
cyanDtmPwrFeedBVoltage = _CyanDtmPwrFeedBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 47),
    _CyanDtmPwrFeedBVoltage_Type()
)
cyanDtmPwrFeedBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmPwrFeedBVoltage.setStatus("current")
_CyanDtmRevertCyanSwBuildVersions_Type = DisplayString
_CyanDtmRevertCyanSwBuildVersions_Object = MibTableColumn
cyanDtmRevertCyanSwBuildVersions = _CyanDtmRevertCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 48),
    _CyanDtmRevertCyanSwBuildVersions_Type()
)
cyanDtmRevertCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmRevertCyanSwBuildVersions.setStatus("current")
_CyanDtmRevertCyanSwRelease_Type = DisplayString
_CyanDtmRevertCyanSwRelease_Object = MibTableColumn
cyanDtmRevertCyanSwRelease = _CyanDtmRevertCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 49),
    _CyanDtmRevertCyanSwRelease_Type()
)
cyanDtmRevertCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmRevertCyanSwRelease.setStatus("current")
_CyanDtmSecServState_Type = CyanSecServiceStateTc
_CyanDtmSecServState_Object = MibTableColumn
cyanDtmSecServState = _CyanDtmSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 50),
    _CyanDtmSecServState_Type()
)
cyanDtmSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmSecServState.setStatus("current")
_CyanDtmSynchLed_Type = CyanLEDTc
_CyanDtmSynchLed_Object = MibTableColumn
cyanDtmSynchLed = _CyanDtmSynchLed_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 51),
    _CyanDtmSynchLed_Type()
)
cyanDtmSynchLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmSynchLed.setStatus("current")
_CyanDtmType_Type = CyanTypeTc
_CyanDtmType_Object = MibTableColumn
cyanDtmType = _CyanDtmType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 52),
    _CyanDtmType_Type()
)
cyanDtmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmType.setStatus("current")
_CyanDtmUndervoltageThreshold_Type = Integer32
_CyanDtmUndervoltageThreshold_Object = MibTableColumn
cyanDtmUndervoltageThreshold = _CyanDtmUndervoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 53),
    _CyanDtmUndervoltageThreshold_Type()
)
cyanDtmUndervoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmUndervoltageThreshold.setStatus("current")
_CyanDtmUpgradeCyanSwBuildVersions_Type = DisplayString
_CyanDtmUpgradeCyanSwBuildVersions_Object = MibTableColumn
cyanDtmUpgradeCyanSwBuildVersions = _CyanDtmUpgradeCyanSwBuildVersions_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 54),
    _CyanDtmUpgradeCyanSwBuildVersions_Type()
)
cyanDtmUpgradeCyanSwBuildVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmUpgradeCyanSwBuildVersions.setStatus("current")
_CyanDtmUpgradeCyanSwRelease_Type = DisplayString
_CyanDtmUpgradeCyanSwRelease_Object = MibTableColumn
cyanDtmUpgradeCyanSwRelease = _CyanDtmUpgradeCyanSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 1, 1, 1, 55),
    _CyanDtmUpgradeCyanSwRelease_Type()
)
cyanDtmUpgradeCyanSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanDtmUpgradeCyanSwRelease.setStatus("current")

# Managed Objects groups

cyanDtmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 20)
)
cyanDtmObjectGroup.setObjects(
      *(("CYAN-DTM-MIB", "cyanDtmActiveLed"),
        ("CYAN-DTM-MIB", "cyanDtmActivestandbyState"),
        ("CYAN-DTM-MIB", "cyanDtmAdminState"),
        ("CYAN-DTM-MIB", "cyanDtmAlarmLed"),
        ("CYAN-DTM-MIB", "cyanDtmAssetTag"),
        ("CYAN-DTM-MIB", "cyanDtmAutoinserviceSoakTimeSec"),
        ("CYAN-DTM-MIB", "cyanDtmBaseMacAddress"),
        ("CYAN-DTM-MIB", "cyanDtmCurrCyanSwBuildVersions"),
        ("CYAN-DTM-MIB", "cyanDtmCurrCyanSwRelease"),
        ("CYAN-DTM-MIB", "cyanDtmCurrent"),
        ("CYAN-DTM-MIB", "cyanDtmDescription"),
        ("CYAN-DTM-MIB", "cyanDtmExhaustAirTemp"),
        ("CYAN-DTM-MIB", "cyanDtmExhaustTempAlarmHighThres"),
        ("CYAN-DTM-MIB", "cyanDtmExhaustTempAlarmLowThres"),
        ("CYAN-DTM-MIB", "cyanDtmExhaustTempWarnHighThres"),
        ("CYAN-DTM-MIB", "cyanDtmExhaustTempWarnLowThres"),
        ("CYAN-DTM-MIB", "cyanDtmExpectedTemperatureRise"),
        ("CYAN-DTM-MIB", "cyanDtmIdentifier"),
        ("CYAN-DTM-MIB", "cyanDtmIntakeAirTemp"),
        ("CYAN-DTM-MIB", "cyanDtmIntakeTempAlarmHighThres"),
        ("CYAN-DTM-MIB", "cyanDtmIntakeTempAlarmLowThres"),
        ("CYAN-DTM-MIB", "cyanDtmIntakeTempWarnHighThres"),
        ("CYAN-DTM-MIB", "cyanDtmIntakeTempWarnLowThres"),
        ("CYAN-DTM-MIB", "cyanDtmLedTest"),
        ("CYAN-DTM-MIB", "cyanDtmMacBlockSize"),
        ("CYAN-DTM-MIB", "cyanDtmMfgCleiCode"),
        ("CYAN-DTM-MIB", "cyanDtmMfgEciCode"),
        ("CYAN-DTM-MIB", "cyanDtmMfgModuleId"),
        ("CYAN-DTM-MIB", "cyanDtmMfgPartNumber"),
        ("CYAN-DTM-MIB", "cyanDtmMfgRevision"),
        ("CYAN-DTM-MIB", "cyanDtmMfgSerialNumber"),
        ("CYAN-DTM-MIB", "cyanDtmName"),
        ("CYAN-DTM-MIB", "cyanDtmOidClass"),
        ("CYAN-DTM-MIB", "cyanDtmOperState"),
        ("CYAN-DTM-MIB", "cyanDtmOperStateQual"),
        ("CYAN-DTM-MIB", "cyanDtmOssLabel"),
        ("CYAN-DTM-MIB", "cyanDtmOvervoltageThreshold"),
        ("CYAN-DTM-MIB", "cyanDtmOwner"),
        ("CYAN-DTM-MIB", "cyanDtmPartNumber"),
        ("CYAN-DTM-MIB", "cyanDtmPowerLed"),
        ("CYAN-DTM-MIB", "cyanDtmPsuTemperature"),
        ("CYAN-DTM-MIB", "cyanDtmPwrFeedAStatus"),
        ("CYAN-DTM-MIB", "cyanDtmPwrFeedAVoltage"),
        ("CYAN-DTM-MIB", "cyanDtmPwrFeedBStatus"),
        ("CYAN-DTM-MIB", "cyanDtmPwrFeedBVoltage"),
        ("CYAN-DTM-MIB", "cyanDtmRevertCyanSwBuildVersions"),
        ("CYAN-DTM-MIB", "cyanDtmRevertCyanSwRelease"),
        ("CYAN-DTM-MIB", "cyanDtmSecServState"),
        ("CYAN-DTM-MIB", "cyanDtmSynchLed"),
        ("CYAN-DTM-MIB", "cyanDtmType"),
        ("CYAN-DTM-MIB", "cyanDtmUndervoltageThreshold"),
        ("CYAN-DTM-MIB", "cyanDtmUpgradeCyanSwBuildVersions"),
        ("CYAN-DTM-MIB", "cyanDtmUpgradeCyanSwRelease"))
)
if mibBuilder.loadTexts:
    cyanDtmObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanDtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 120, 30)
)
if mibBuilder.loadTexts:
    cyanDtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-DTM-MIB",
    **{"cyanDtmModule": cyanDtmModule,
       "cyanDtmMibObjects": cyanDtmMibObjects,
       "cyanDtmTable": cyanDtmTable,
       "cyanDtmEntry": cyanDtmEntry,
       "cyanDtmShelfId": cyanDtmShelfId,
       "cyanDtmDtmId": cyanDtmDtmId,
       "cyanDtmActiveLed": cyanDtmActiveLed,
       "cyanDtmActivestandbyState": cyanDtmActivestandbyState,
       "cyanDtmAdminState": cyanDtmAdminState,
       "cyanDtmAlarmLed": cyanDtmAlarmLed,
       "cyanDtmAssetTag": cyanDtmAssetTag,
       "cyanDtmAutoinserviceSoakTimeSec": cyanDtmAutoinserviceSoakTimeSec,
       "cyanDtmBaseMacAddress": cyanDtmBaseMacAddress,
       "cyanDtmCurrCyanSwBuildVersions": cyanDtmCurrCyanSwBuildVersions,
       "cyanDtmCurrCyanSwRelease": cyanDtmCurrCyanSwRelease,
       "cyanDtmCurrent": cyanDtmCurrent,
       "cyanDtmDescription": cyanDtmDescription,
       "cyanDtmExhaustAirTemp": cyanDtmExhaustAirTemp,
       "cyanDtmExhaustTempAlarmHighThres": cyanDtmExhaustTempAlarmHighThres,
       "cyanDtmExhaustTempAlarmLowThres": cyanDtmExhaustTempAlarmLowThres,
       "cyanDtmExhaustTempWarnHighThres": cyanDtmExhaustTempWarnHighThres,
       "cyanDtmExhaustTempWarnLowThres": cyanDtmExhaustTempWarnLowThres,
       "cyanDtmExpectedTemperatureRise": cyanDtmExpectedTemperatureRise,
       "cyanDtmIdentifier": cyanDtmIdentifier,
       "cyanDtmIntakeAirTemp": cyanDtmIntakeAirTemp,
       "cyanDtmIntakeTempAlarmHighThres": cyanDtmIntakeTempAlarmHighThres,
       "cyanDtmIntakeTempAlarmLowThres": cyanDtmIntakeTempAlarmLowThres,
       "cyanDtmIntakeTempWarnHighThres": cyanDtmIntakeTempWarnHighThres,
       "cyanDtmIntakeTempWarnLowThres": cyanDtmIntakeTempWarnLowThres,
       "cyanDtmLedTest": cyanDtmLedTest,
       "cyanDtmMacBlockSize": cyanDtmMacBlockSize,
       "cyanDtmMfgCleiCode": cyanDtmMfgCleiCode,
       "cyanDtmMfgEciCode": cyanDtmMfgEciCode,
       "cyanDtmMfgModuleId": cyanDtmMfgModuleId,
       "cyanDtmMfgPartNumber": cyanDtmMfgPartNumber,
       "cyanDtmMfgRevision": cyanDtmMfgRevision,
       "cyanDtmMfgSerialNumber": cyanDtmMfgSerialNumber,
       "cyanDtmName": cyanDtmName,
       "cyanDtmOidClass": cyanDtmOidClass,
       "cyanDtmOperState": cyanDtmOperState,
       "cyanDtmOperStateQual": cyanDtmOperStateQual,
       "cyanDtmOssLabel": cyanDtmOssLabel,
       "cyanDtmOvervoltageThreshold": cyanDtmOvervoltageThreshold,
       "cyanDtmOwner": cyanDtmOwner,
       "cyanDtmPartNumber": cyanDtmPartNumber,
       "cyanDtmPowerLed": cyanDtmPowerLed,
       "cyanDtmPsuTemperature": cyanDtmPsuTemperature,
       "cyanDtmPwrFeedAStatus": cyanDtmPwrFeedAStatus,
       "cyanDtmPwrFeedAVoltage": cyanDtmPwrFeedAVoltage,
       "cyanDtmPwrFeedBStatus": cyanDtmPwrFeedBStatus,
       "cyanDtmPwrFeedBVoltage": cyanDtmPwrFeedBVoltage,
       "cyanDtmRevertCyanSwBuildVersions": cyanDtmRevertCyanSwBuildVersions,
       "cyanDtmRevertCyanSwRelease": cyanDtmRevertCyanSwRelease,
       "cyanDtmSecServState": cyanDtmSecServState,
       "cyanDtmSynchLed": cyanDtmSynchLed,
       "cyanDtmType": cyanDtmType,
       "cyanDtmUndervoltageThreshold": cyanDtmUndervoltageThreshold,
       "cyanDtmUpgradeCyanSwBuildVersions": cyanDtmUpgradeCyanSwBuildVersions,
       "cyanDtmUpgradeCyanSwRelease": cyanDtmUpgradeCyanSwRelease,
       "cyanDtmObjectGroup": cyanDtmObjectGroup,
       "cyanDtmCompliance": cyanDtmCompliance}
)
