# SNMP MIB module (LIEBERT-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:03 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
_LiebertUps_ObjectIdentity = ObjectIdentity
liebertUps = _LiebertUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1)
)
_LuExtensions_ObjectIdentity = ObjectIdentity
luExtensions = _LuExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1)
)
_LuCore_ObjectIdentity = ObjectIdentity
luCore = _LuCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1)
)
_LcUpsIdent_ObjectIdentity = ObjectIdentity
lcUpsIdent = _LcUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1)
)


class _LcUpsIdentManufacturer_Type(DisplayString):
    """Custom type lcUpsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LcUpsIdentManufacturer_Type.__name__ = "DisplayString"
_LcUpsIdentManufacturer_Object = MibScalar
lcUpsIdentManufacturer = _LcUpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 1),
    _LcUpsIdentManufacturer_Type()
)
lcUpsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentManufacturer.setStatus("optional")


class _LcUpsIdentModel_Type(DisplayString):
    """Custom type lcUpsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LcUpsIdentModel_Type.__name__ = "DisplayString"
_LcUpsIdentModel_Object = MibScalar
lcUpsIdentModel = _LcUpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 2),
    _LcUpsIdentModel_Type()
)
lcUpsIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsIdentModel.setStatus("optional")


class _LcUpsIdentSoftwareVersion_Type(DisplayString):
    """Custom type lcUpsIdentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LcUpsIdentSoftwareVersion_Type.__name__ = "DisplayString"
_LcUpsIdentSoftwareVersion_Object = MibScalar
lcUpsIdentSoftwareVersion = _LcUpsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 3),
    _LcUpsIdentSoftwareVersion_Type()
)
lcUpsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSoftwareVersion.setStatus("optional")
_LcUpsIdentSpecific_Type = ObjectIdentifier
_LcUpsIdentSpecific_Object = MibScalar
lcUpsIdentSpecific = _LcUpsIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 4),
    _LcUpsIdentSpecific_Type()
)
lcUpsIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSpecific.setStatus("optional")


class _LcUpsIdentFirmwareVersion_Type(DisplayString):
    """Custom type lcUpsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_LcUpsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_LcUpsIdentFirmwareVersion_Object = MibScalar
lcUpsIdentFirmwareVersion = _LcUpsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 5),
    _LcUpsIdentFirmwareVersion_Type()
)
lcUpsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentFirmwareVersion.setStatus("optional")


class _LcUpsIdentSerialNumber_Type(DisplayString):
    """Custom type lcUpsIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LcUpsIdentSerialNumber_Type.__name__ = "DisplayString"
_LcUpsIdentSerialNumber_Object = MibScalar
lcUpsIdentSerialNumber = _LcUpsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 6),
    _LcUpsIdentSerialNumber_Type()
)
lcUpsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSerialNumber.setStatus("optional")


class _LcUpsIdentManufactureDate_Type(DisplayString):
    """Custom type lcUpsIdentManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LcUpsIdentManufactureDate_Type.__name__ = "DisplayString"
_LcUpsIdentManufactureDate_Object = MibScalar
lcUpsIdentManufactureDate = _LcUpsIdentManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 7),
    _LcUpsIdentManufactureDate_Type()
)
lcUpsIdentManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentManufactureDate.setStatus("optional")
_LcUpsBattery_ObjectIdentity = ObjectIdentity
lcUpsBattery = _LcUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2)
)


class _LcUpsBatTimeRemaining_Type(Integer32):
    """Custom type lcUpsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcUpsBatTimeRemaining_Type.__name__ = "Integer32"
_LcUpsBatTimeRemaining_Object = MibScalar
lcUpsBatTimeRemaining = _LcUpsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 1),
    _LcUpsBatTimeRemaining_Type()
)
lcUpsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTimeRemaining.setStatus("optional")


class _LcUpsBatTemperature_Type(Integer32):
    """Custom type lcUpsBatTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatTemperature_Type.__name__ = "Integer32"
_LcUpsBatTemperature_Object = MibScalar
lcUpsBatTemperature = _LcUpsBatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 2),
    _LcUpsBatTemperature_Type()
)
lcUpsBatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTemperature.setStatus("optional")


class _LcUpsBatVoltage_Type(Integer32):
    """Custom type lcUpsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatVoltage_Type.__name__ = "Integer32"
_LcUpsBatVoltage_Object = MibScalar
lcUpsBatVoltage = _LcUpsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 3),
    _LcUpsBatVoltage_Type()
)
lcUpsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatVoltage.setStatus("optional")


class _LcUpsBatCurrent_Type(Integer32):
    """Custom type lcUpsBatCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatCurrent_Type.__name__ = "Integer32"
_LcUpsBatCurrent_Object = MibScalar
lcUpsBatCurrent = _LcUpsBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 4),
    _LcUpsBatCurrent_Type()
)
lcUpsBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCurrent.setStatus("optional")


class _LcUpsBatCapacity_Type(Integer32):
    """Custom type lcUpsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcUpsBatCapacity_Type.__name__ = "Integer32"
_LcUpsBatCapacity_Object = MibScalar
lcUpsBatCapacity = _LcUpsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 6),
    _LcUpsBatCapacity_Type()
)
lcUpsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCapacity.setStatus("optional")
_LcUpsBatTotalDischCounts_Type = Counter32
_LcUpsBatTotalDischCounts_Object = MibScalar
lcUpsBatTotalDischCounts = _LcUpsBatTotalDischCounts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 7),
    _LcUpsBatTotalDischCounts_Type()
)
lcUpsBatTotalDischCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTotalDischCounts.setStatus("optional")
_LcUpsBatCycleDurationInSeconds_Type = Counter32
_LcUpsBatCycleDurationInSeconds_Object = MibScalar
lcUpsBatCycleDurationInSeconds = _LcUpsBatCycleDurationInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 8),
    _LcUpsBatCycleDurationInSeconds_Type()
)
lcUpsBatCycleDurationInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCycleDurationInSeconds.setStatus("optional")
_LcUpsBatAmpHours_Type = Counter32
_LcUpsBatAmpHours_Object = MibScalar
lcUpsBatAmpHours = _LcUpsBatAmpHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 9),
    _LcUpsBatAmpHours_Type()
)
lcUpsBatAmpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatAmpHours.setStatus("optional")
_LcUpsBatKWhours_Type = Counter32
_LcUpsBatKWhours_Object = MibScalar
lcUpsBatKWhours = _LcUpsBatKWhours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 10),
    _LcUpsBatKWhours_Type()
)
lcUpsBatKWhours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatKWhours.setStatus("optional")
_LcUpsBatWattHours_Type = Counter32
_LcUpsBatWattHours_Object = MibScalar
lcUpsBatWattHours = _LcUpsBatWattHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 11),
    _LcUpsBatWattHours_Type()
)
lcUpsBatWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatWattHours.setStatus("optional")
_LcUpsInput_ObjectIdentity = ObjectIdentity
lcUpsInput = _LcUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3)
)


class _LcUpsInputFrequency_Type(Integer32):
    """Custom type lcUpsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputFrequency_Type.__name__ = "Integer32"
_LcUpsInputFrequency_Object = MibScalar
lcUpsInputFrequency = _LcUpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 1),
    _LcUpsInputFrequency_Type()
)
lcUpsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputFrequency.setStatus("optional")
_LcUpsInputBrownOuts_Type = Counter32
_LcUpsInputBrownOuts_Object = MibScalar
lcUpsInputBrownOuts = _LcUpsInputBrownOuts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 2),
    _LcUpsInputBrownOuts_Type()
)
lcUpsInputBrownOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputBrownOuts.setStatus("optional")
_LcUpsInputBlackOuts_Type = Counter32
_LcUpsInputBlackOuts_Object = MibScalar
lcUpsInputBlackOuts = _LcUpsInputBlackOuts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 3),
    _LcUpsInputBlackOuts_Type()
)
lcUpsInputBlackOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputBlackOuts.setStatus("optional")
_LcUpsInputTransients_Type = Counter32
_LcUpsInputTransients_Object = MibScalar
lcUpsInputTransients = _LcUpsInputTransients_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 4),
    _LcUpsInputTransients_Type()
)
lcUpsInputTransients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputTransients.setStatus("optional")


class _LcUpsInputNumLines_Type(Integer32):
    """Custom type lcUpsInputNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsInputNumLines_Type.__name__ = "Integer32"
_LcUpsInputNumLines_Object = MibScalar
lcUpsInputNumLines = _LcUpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 5),
    _LcUpsInputNumLines_Type()
)
lcUpsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputNumLines.setStatus("optional")
_LcUpsInputTable_Object = MibTable
lcUpsInputTable = _LcUpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lcUpsInputTable.setStatus("optional")
_LcUpsInputEntry_Object = MibTableRow
lcUpsInputEntry = _LcUpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1)
)
lcUpsInputEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "lcUpsInputLine"),
)
if mibBuilder.loadTexts:
    lcUpsInputEntry.setStatus("optional")


class _LcUpsInputLine_Type(Integer32):
    """Custom type lcUpsInputLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsInputLine_Type.__name__ = "Integer32"
_LcUpsInputLine_Object = MibTableColumn
lcUpsInputLine = _LcUpsInputLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 1),
    _LcUpsInputLine_Type()
)
lcUpsInputLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputLine.setStatus("optional")


class _LcUpsInputVoltage_Type(Integer32):
    """Custom type lcUpsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputVoltage_Type.__name__ = "Integer32"
_LcUpsInputVoltage_Object = MibTableColumn
lcUpsInputVoltage = _LcUpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 2),
    _LcUpsInputVoltage_Type()
)
lcUpsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputVoltage.setStatus("optional")


class _LcUpsInputCurrent_Type(Integer32):
    """Custom type lcUpsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputCurrent_Type.__name__ = "Integer32"
_LcUpsInputCurrent_Object = MibTableColumn
lcUpsInputCurrent = _LcUpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 3),
    _LcUpsInputCurrent_Type()
)
lcUpsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputCurrent.setStatus("optional")


class _LcUpsInputVA_Type(Integer32):
    """Custom type lcUpsInputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsInputVA_Type.__name__ = "Integer32"
_LcUpsInputVA_Object = MibTableColumn
lcUpsInputVA = _LcUpsInputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 4),
    _LcUpsInputVA_Type()
)
lcUpsInputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputVA.setStatus("optional")
_LcUpsOutput_ObjectIdentity = ObjectIdentity
lcUpsOutput = _LcUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4)
)


class _LcUpsOutputFrequency_Type(Integer32):
    """Custom type lcUpsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputFrequency_Type.__name__ = "Integer32"
_LcUpsOutputFrequency_Object = MibScalar
lcUpsOutputFrequency = _LcUpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 1),
    _LcUpsOutputFrequency_Type()
)
lcUpsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputFrequency.setStatus("optional")


class _LcUpsOutputLoad_Type(Integer32):
    """Custom type lcUpsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcUpsOutputLoad_Type.__name__ = "Integer32"
_LcUpsOutputLoad_Object = MibScalar
lcUpsOutputLoad = _LcUpsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 2),
    _LcUpsOutputLoad_Type()
)
lcUpsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputLoad.setStatus("optional")


class _LcUpsOutputNumLines_Type(Integer32):
    """Custom type lcUpsOutputNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsOutputNumLines_Type.__name__ = "Integer32"
_LcUpsOutputNumLines_Object = MibScalar
lcUpsOutputNumLines = _LcUpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 3),
    _LcUpsOutputNumLines_Type()
)
lcUpsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputNumLines.setStatus("optional")
_LcUpsOutputTable_Object = MibTable
lcUpsOutputTable = _LcUpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lcUpsOutputTable.setStatus("optional")
_LcUpsOutputEntry_Object = MibTableRow
lcUpsOutputEntry = _LcUpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1)
)
lcUpsOutputEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "lcUpsOutputLine"),
)
if mibBuilder.loadTexts:
    lcUpsOutputEntry.setStatus("optional")


class _LcUpsOutputLine_Type(Integer32):
    """Custom type lcUpsOutputLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsOutputLine_Type.__name__ = "Integer32"
_LcUpsOutputLine_Object = MibTableColumn
lcUpsOutputLine = _LcUpsOutputLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 1),
    _LcUpsOutputLine_Type()
)
lcUpsOutputLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputLine.setStatus("optional")


class _LcUpsOutputVoltage_Type(Integer32):
    """Custom type lcUpsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputVoltage_Type.__name__ = "Integer32"
_LcUpsOutputVoltage_Object = MibTableColumn
lcUpsOutputVoltage = _LcUpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 2),
    _LcUpsOutputVoltage_Type()
)
lcUpsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputVoltage.setStatus("optional")


class _LcUpsOutputCurrent_Type(Integer32):
    """Custom type lcUpsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputCurrent_Type.__name__ = "Integer32"
_LcUpsOutputCurrent_Object = MibTableColumn
lcUpsOutputCurrent = _LcUpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 3),
    _LcUpsOutputCurrent_Type()
)
lcUpsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputCurrent.setStatus("optional")


class _LcUpsOutputVA_Type(Integer32):
    """Custom type lcUpsOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsOutputVA_Type.__name__ = "Integer32"
_LcUpsOutputVA_Object = MibTableColumn
lcUpsOutputVA = _LcUpsOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 4),
    _LcUpsOutputVA_Type()
)
lcUpsOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputVA.setStatus("optional")


class _LcUpsOutputWatts_Type(Integer32):
    """Custom type lcUpsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsOutputWatts_Type.__name__ = "Integer32"
_LcUpsOutputWatts_Object = MibScalar
lcUpsOutputWatts = _LcUpsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 5),
    _LcUpsOutputWatts_Type()
)
lcUpsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputWatts.setStatus("optional")
_LcUpsInverter_ObjectIdentity = ObjectIdentity
lcUpsInverter = _LcUpsInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5)
)


class _LcUpsInverterStatus_Type(Integer32):
    """Custom type lcUpsInverterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("unknown", 1))
    )


_LcUpsInverterStatus_Type.__name__ = "Integer32"
_LcUpsInverterStatus_Object = MibScalar
lcUpsInverterStatus = _LcUpsInverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 1),
    _LcUpsInverterStatus_Type()
)
lcUpsInverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInverterStatus.setStatus("optional")


class _LcUpsInverterTemp_Type(Integer32):
    """Custom type lcUpsInverterTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsInverterTemp_Type.__name__ = "Integer32"
_LcUpsInverterTemp_Object = MibScalar
lcUpsInverterTemp = _LcUpsInverterTemp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 2),
    _LcUpsInverterTemp_Type()
)
lcUpsInverterTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInverterTemp.setStatus("optional")
_LcUpsAlarm_ObjectIdentity = ObjectIdentity
lcUpsAlarm = _LcUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6)
)
_LcUpsAlarms_Type = Gauge32
_LcUpsAlarms_Object = MibScalar
lcUpsAlarms = _LcUpsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 1),
    _LcUpsAlarms_Type()
)
lcUpsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarms.setStatus("optional")
_LcUpsAlarmTable_Object = MibTable
lcUpsAlarmTable = _LcUpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lcUpsAlarmTable.setStatus("optional")
_LcUpsAlarmEntry_Object = MibTableRow
lcUpsAlarmEntry = _LcUpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1)
)
lcUpsAlarmEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "lcUpsAlarmId"),
)
if mibBuilder.loadTexts:
    lcUpsAlarmEntry.setStatus("optional")


class _LcUpsAlarmId_Type(Integer32):
    """Custom type lcUpsAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsAlarmId_Type.__name__ = "Integer32"
_LcUpsAlarmId_Object = MibTableColumn
lcUpsAlarmId = _LcUpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 1),
    _LcUpsAlarmId_Type()
)
lcUpsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmId.setStatus("optional")
_LcUpsAlarmDescr_Type = ObjectIdentifier
_LcUpsAlarmDescr_Object = MibTableColumn
lcUpsAlarmDescr = _LcUpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 2),
    _LcUpsAlarmDescr_Type()
)
lcUpsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmDescr.setStatus("optional")
_LcUpsAlarmTime_Type = TimeTicks
_LcUpsAlarmTime_Object = MibTableColumn
lcUpsAlarmTime = _LcUpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 3),
    _LcUpsAlarmTime_Type()
)
lcUpsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmTime.setStatus("optional")
_LcUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lcUpsAlarmConditions = _LcUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3)
)
_LcUpsAlarmLowBatteryWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmLowBatteryWarning = _LcUpsAlarmLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 1)
)
_LcUpsAlarmLowBatteryShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmLowBatteryShutdown = _LcUpsAlarmLowBatteryShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 2)
)
_LcUpsAlarmUtilFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmUtilFailed = _LcUpsAlarmUtilFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 3)
)
_LcUpsAlarmOverTempWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmOverTempWarning = _LcUpsAlarmOverTempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 4)
)
_LcUpsAlarmOverTempShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmOverTempShutdown = _LcUpsAlarmOverTempShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 5)
)
_LcUpsAlarmOutputOverloadWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverloadWarning = _LcUpsAlarmOutputOverloadWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 6)
)
_LcUpsAlarmOutputOverloadShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverloadShutdown = _LcUpsAlarmOutputOverloadShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 7)
)
_LcUpsAlarmInputOverVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputOverVoltage = _LcUpsAlarmInputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 8)
)
_LcUpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
lcUpsAlarmBatteryBad = _LcUpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 9)
)
_LcUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
lcUpsAlarmOnBattery = _LcUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 10)
)
_LcUpsAlarmStopNoticeIssued_ObjectIdentity = ObjectIdentity
lcUpsAlarmStopNoticeIssued = _LcUpsAlarmStopNoticeIssued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 11)
)
_LcUpsAlarmUpsOff_ObjectIdentity = ObjectIdentity
lcUpsAlarmUpsOff = _LcUpsAlarmUpsOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 12)
)
_LcUpsAlarmInputFreqError_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputFreqError = _LcUpsAlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 13)
)
_LcUpsAlarmOutputUnderVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputUnderVoltage = _LcUpsAlarmOutputUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 15)
)
_LcUpsAlarmOutputOverVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverVoltage = _LcUpsAlarmOutputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 16)
)
_LcUpsBadBypassPower_ObjectIdentity = ObjectIdentity
lcUpsBadBypassPower = _LcUpsBadBypassPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 17)
)
_LcUpsAlarmDCOverVoltageShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmDCOverVoltageShutdown = _LcUpsAlarmDCOverVoltageShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 18)
)
_LcUpsAlarmHardwareShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmHardwareShutdown = _LcUpsAlarmHardwareShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 23)
)
_LcUpsAlarmEmergencyXferToBypass_ObjectIdentity = ObjectIdentity
lcUpsAlarmEmergencyXferToBypass = _LcUpsAlarmEmergencyXferToBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 24)
)
_LcUpsAlarmInverterFault_ObjectIdentity = ObjectIdentity
lcUpsAlarmInverterFault = _LcUpsAlarmInverterFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 25)
)
_LcUpsAlarmPhaseRotationError_ObjectIdentity = ObjectIdentity
lcUpsAlarmPhaseRotationError = _LcUpsAlarmPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 26)
)
_LcUpsAlarmFuseBlown_ObjectIdentity = ObjectIdentity
lcUpsAlarmFuseBlown = _LcUpsAlarmFuseBlown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 28)
)
_LcUpsAlarmAmbientOverTemp_ObjectIdentity = ObjectIdentity
lcUpsAlarmAmbientOverTemp = _LcUpsAlarmAmbientOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 29)
)
_LcUpsAlarmEmergencyPowerOff_ObjectIdentity = ObjectIdentity
lcUpsAlarmEmergencyPowerOff = _LcUpsAlarmEmergencyPowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 30)
)
_LcUpsAlarmFanFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmFanFailed = _LcUpsAlarmFanFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 31)
)
_LcUpsAlarmControlPowerFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmControlPowerFailed = _LcUpsAlarmControlPowerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 32)
)
_LcUpsAlarmReversePower_ObjectIdentity = ObjectIdentity
lcUpsAlarmReversePower = _LcUpsAlarmReversePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 33)
)
_LcUpsAlarmDCgroundFault_ObjectIdentity = ObjectIdentity
lcUpsAlarmDCgroundFault = _LcUpsAlarmDCgroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 34)
)
_LcUpsAlarmLoadOnBypass_ObjectIdentity = ObjectIdentity
lcUpsAlarmLoadOnBypass = _LcUpsAlarmLoadOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 35)
)
_LcUpsAlarmBatteryCbOpen_ObjectIdentity = ObjectIdentity
lcUpsAlarmBatteryCbOpen = _LcUpsAlarmBatteryCbOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 37)
)
_LcUpsAlarmInputCbOpen_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputCbOpen = _LcUpsAlarmInputCbOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 38)
)
_LcUpsAlarmOutputCbOpen_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputCbOpen = _LcUpsAlarmOutputCbOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 39)
)
_LcUpsAlarmOutputFreqError_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputFreqError = _LcUpsAlarmOutputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 40)
)
_LcUpsAlarmStaticSwUnable_ObjectIdentity = ObjectIdentity
lcUpsAlarmStaticSwUnable = _LcUpsAlarmStaticSwUnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 41)
)
_LcUpsAlarmManualResetXfer_ObjectIdentity = ObjectIdentity
lcUpsAlarmManualResetXfer = _LcUpsAlarmManualResetXfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 42)
)
_LcUpsAlarmAutoRexferPrimed_ObjectIdentity = ObjectIdentity
lcUpsAlarmAutoRexferPrimed = _LcUpsAlarmAutoRexferPrimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 43)
)
_LcUpsAlarmBattCycleBuffWarn_ObjectIdentity = ObjectIdentity
lcUpsAlarmBattCycleBuffWarn = _LcUpsAlarmBattCycleBuffWarn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 44)
)
_LcUpsAlarmModuleSummary_ObjectIdentity = ObjectIdentity
lcUpsAlarmModuleSummary = _LcUpsAlarmModuleSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 45)
)
_LcUpsLineCorrectionActive_ObjectIdentity = ObjectIdentity
lcUpsLineCorrectionActive = _LcUpsLineCorrectionActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 46)
)
_LcUpsTest_ObjectIdentity = ObjectIdentity
lcUpsTest = _LcUpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7)
)


class _LcUpsTestBattery_Type(Integer32):
    """Custom type lcUpsTestBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("start", 2),
          ("unknown", 1))
    )


_LcUpsTestBattery_Type.__name__ = "Integer32"
_LcUpsTestBattery_Object = MibScalar
lcUpsTestBattery = _LcUpsTestBattery_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 1),
    _LcUpsTestBattery_Type()
)
lcUpsTestBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsTestBattery.setStatus("optional")


class _LcUpsTestBatteryStatus_Type(Integer32):
    """Custom type lcUpsTestBatteryStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 4),
          ("inhibited", 7),
          ("notSupported", 6),
          ("passed", 2),
          ("sysFailure", 5),
          ("unknown", 1))
    )


_LcUpsTestBatteryStatus_Type.__name__ = "Integer32"
_LcUpsTestBatteryStatus_Object = MibScalar
lcUpsTestBatteryStatus = _LcUpsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 2),
    _LcUpsTestBatteryStatus_Type()
)
lcUpsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsTestBatteryStatus.setStatus("optional")


class _LcUpsTestDiag_Type(Integer32):
    """Custom type lcUpsTestDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("start", 2),
          ("unknown", 1))
    )


_LcUpsTestDiag_Type.__name__ = "Integer32"
_LcUpsTestDiag_Object = MibScalar
lcUpsTestDiag = _LcUpsTestDiag_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 3),
    _LcUpsTestDiag_Type()
)
lcUpsTestDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsTestDiag.setStatus("optional")


class _LcUpsTestDiagStatus_Type(Integer32):
    """Custom type lcUpsTestDiagStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 4),
          ("inhibited", 7),
          ("notSupported", 6),
          ("passed", 2),
          ("sysFailure", 5),
          ("unknown", 1))
    )


_LcUpsTestDiagStatus_Type.__name__ = "Integer32"
_LcUpsTestDiagStatus_Object = MibScalar
lcUpsTestDiagStatus = _LcUpsTestDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 4),
    _LcUpsTestDiagStatus_Type()
)
lcUpsTestDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsTestDiagStatus.setStatus("optional")
_LcUpsControl_ObjectIdentity = ObjectIdentity
lcUpsControl = _LcUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8)
)


class _LcUpsControlOutputOffDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOffDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOffDelay_Object = MibScalar
lcUpsControlOutputOffDelay = _LcUpsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 1),
    _LcUpsControlOutputOffDelay_Type()
)
lcUpsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOffDelay.setStatus("optional")


class _LcUpsControlOutputOnDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOnDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOnDelay_Object = MibScalar
lcUpsControlOutputOnDelay = _LcUpsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 2),
    _LcUpsControlOutputOnDelay_Type()
)
lcUpsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOnDelay.setStatus("optional")


class _LcUpsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOffTrapDelay_Object = MibScalar
lcUpsControlOutputOffTrapDelay = _LcUpsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 3),
    _LcUpsControlOutputOffTrapDelay_Type()
)
lcUpsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOffTrapDelay.setStatus("optional")


class _LcUpsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOnTrapDelay_Object = MibScalar
lcUpsControlOutputOnTrapDelay = _LcUpsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 4),
    _LcUpsControlOutputOnTrapDelay_Type()
)
lcUpsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOnTrapDelay.setStatus("optional")


class _LcUpsControlUnixShutdownDelay_Type(Integer32):
    """Custom type lcUpsControlUnixShutdownDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlUnixShutdownDelay_Type.__name__ = "Integer32"
_LcUpsControlUnixShutdownDelay_Object = MibScalar
lcUpsControlUnixShutdownDelay = _LcUpsControlUnixShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 5),
    _LcUpsControlUnixShutdownDelay_Type()
)
lcUpsControlUnixShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlUnixShutdownDelay.setStatus("optional")


class _LcUpsControlUnixShutdownTrapDelay_Type(Integer32):
    """Custom type lcUpsControlUnixShutdownTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlUnixShutdownTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlUnixShutdownTrapDelay_Object = MibScalar
lcUpsControlUnixShutdownTrapDelay = _LcUpsControlUnixShutdownTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 6),
    _LcUpsControlUnixShutdownTrapDelay_Type()
)
lcUpsControlUnixShutdownTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlUnixShutdownTrapDelay.setStatus("optional")


class _LcUpsControlCancelCommands_Type(Integer32):
    """Custom type lcUpsControlCancelCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("unknown", 1))
    )


_LcUpsControlCancelCommands_Type.__name__ = "Integer32"
_LcUpsControlCancelCommands_Object = MibScalar
lcUpsControlCancelCommands = _LcUpsControlCancelCommands_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 7),
    _LcUpsControlCancelCommands_Type()
)
lcUpsControlCancelCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlCancelCommands.setStatus("optional")


class _LcUpsControlRebootAgentDelay_Type(Integer32):
    """Custom type lcUpsControlRebootAgentDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlRebootAgentDelay_Type.__name__ = "Integer32"
_LcUpsControlRebootAgentDelay_Object = MibScalar
lcUpsControlRebootAgentDelay = _LcUpsControlRebootAgentDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 8),
    _LcUpsControlRebootAgentDelay_Type()
)
lcUpsControlRebootAgentDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlRebootAgentDelay.setStatus("optional")
_LcUpsNominal_ObjectIdentity = ObjectIdentity
lcUpsNominal = _LcUpsNominal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9)
)


class _LcUpsNominalOutputVoltage_Type(Integer32):
    """Custom type lcUpsNominalOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputVoltage_Type.__name__ = "Integer32"
_LcUpsNominalOutputVoltage_Object = MibScalar
lcUpsNominalOutputVoltage = _LcUpsNominalOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 1),
    _LcUpsNominalOutputVoltage_Type()
)
lcUpsNominalOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVoltage.setStatus("optional")


class _LcUpsNominalInputVoltage_Type(Integer32):
    """Custom type lcUpsNominalInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalInputVoltage_Type.__name__ = "Integer32"
_LcUpsNominalInputVoltage_Object = MibScalar
lcUpsNominalInputVoltage = _LcUpsNominalInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 2),
    _LcUpsNominalInputVoltage_Type()
)
lcUpsNominalInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalInputVoltage.setStatus("optional")


class _LcUpsNominalOutputVA_Type(Integer32):
    """Custom type lcUpsNominalOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputVA_Type.__name__ = "Integer32"
_LcUpsNominalOutputVA_Object = MibScalar
lcUpsNominalOutputVA = _LcUpsNominalOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 3),
    _LcUpsNominalOutputVA_Type()
)
lcUpsNominalOutputVA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVA.setStatus("optional")


class _LcUpsNominalOutputWatts_Type(Integer32):
    """Custom type lcUpsNominalOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputWatts_Type.__name__ = "Integer32"
_LcUpsNominalOutputWatts_Object = MibScalar
lcUpsNominalOutputWatts = _LcUpsNominalOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 4),
    _LcUpsNominalOutputWatts_Type()
)
lcUpsNominalOutputWatts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputWatts.setStatus("optional")


class _LcUpsNominalOutputFreq_Type(Integer32):
    """Custom type lcUpsNominalOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputFreq_Type.__name__ = "Integer32"
_LcUpsNominalOutputFreq_Object = MibScalar
lcUpsNominalOutputFreq = _LcUpsNominalOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 5),
    _LcUpsNominalOutputFreq_Type()
)
lcUpsNominalOutputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputFreq.setStatus("optional")


class _LcUpsNominalInputFreq_Type(Integer32):
    """Custom type lcUpsNominalInputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalInputFreq_Type.__name__ = "Integer32"
_LcUpsNominalInputFreq_Object = MibScalar
lcUpsNominalInputFreq = _LcUpsNominalInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 6),
    _LcUpsNominalInputFreq_Type()
)
lcUpsNominalInputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalInputFreq.setStatus("optional")


class _LcUpsNominalOutputVaRating_Type(Integer32):
    """Custom type lcUpsNominalOutputVaRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsNominalOutputVaRating_Type.__name__ = "Integer32"
_LcUpsNominalOutputVaRating_Object = MibScalar
lcUpsNominalOutputVaRating = _LcUpsNominalOutputVaRating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 7),
    _LcUpsNominalOutputVaRating_Type()
)
lcUpsNominalOutputVaRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVaRating.setStatus("optional")


class _LcUpsNominalOutputWattsRating_Type(Integer32):
    """Custom type lcUpsNominalOutputWattsRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsNominalOutputWattsRating_Type.__name__ = "Integer32"
_LcUpsNominalOutputWattsRating_Object = MibScalar
lcUpsNominalOutputWattsRating = _LcUpsNominalOutputWattsRating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 8),
    _LcUpsNominalOutputWattsRating_Type()
)
lcUpsNominalOutputWattsRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputWattsRating.setStatus("optional")
_LcUpsTraps_ObjectIdentity = ObjectIdentity
lcUpsTraps = _LcUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11)
)
_LcUpsSwitchedReceptacles_ObjectIdentity = ObjectIdentity
lcUpsSwitchedReceptacles = _LcUpsSwitchedReceptacles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12)
)


class _LcUpsSwitchedReceptMaxNum_Type(Integer32):
    """Custom type lcUpsSwitchedReceptMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcUpsSwitchedReceptMaxNum_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptMaxNum_Object = MibScalar
lcUpsSwitchedReceptMaxNum = _LcUpsSwitchedReceptMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 1),
    _LcUpsSwitchedReceptMaxNum_Type()
)
lcUpsSwitchedReceptMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptMaxNum.setStatus("optional")
_LcUpsSwitchedReceptTable_Object = MibTable
lcUpsSwitchedReceptTable = _LcUpsSwitchedReceptTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptTable.setStatus("optional")
_LcUpsSwitchedReceptEntry_Object = MibTableRow
lcUpsSwitchedReceptEntry = _LcUpsSwitchedReceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1)
)
lcUpsSwitchedReceptEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "lcUpsSwitchedReceptIndex"),
)
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptEntry.setStatus("optional")
_LcUpsSwitchedReceptIndex_Type = Integer32
_LcUpsSwitchedReceptIndex_Object = MibTableColumn
lcUpsSwitchedReceptIndex = _LcUpsSwitchedReceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 1),
    _LcUpsSwitchedReceptIndex_Type()
)
lcUpsSwitchedReceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptIndex.setStatus("optional")


class _LcUpsSwitchedReceptOnDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOnDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOnDelay_Object = MibTableColumn
lcUpsSwitchedReceptOnDelay = _LcUpsSwitchedReceptOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 2),
    _LcUpsSwitchedReceptOnDelay_Type()
)
lcUpsSwitchedReceptOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOnDelay.setStatus("optional")


class _LcUpsSwitchedReceptOnTrapDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOnTrapDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOnTrapDelay_Object = MibTableColumn
lcUpsSwitchedReceptOnTrapDelay = _LcUpsSwitchedReceptOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 3),
    _LcUpsSwitchedReceptOnTrapDelay_Type()
)
lcUpsSwitchedReceptOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOnTrapDelay.setStatus("optional")


class _LcUpsSwitchedReceptOffDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOffDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOffDelay_Object = MibTableColumn
lcUpsSwitchedReceptOffDelay = _LcUpsSwitchedReceptOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 4),
    _LcUpsSwitchedReceptOffDelay_Type()
)
lcUpsSwitchedReceptOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOffDelay.setStatus("optional")


class _LcUpsSwitchedReceptOffTrapDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOffTrapDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOffTrapDelay_Object = MibTableColumn
lcUpsSwitchedReceptOffTrapDelay = _LcUpsSwitchedReceptOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 5),
    _LcUpsSwitchedReceptOffTrapDelay_Type()
)
lcUpsSwitchedReceptOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOffTrapDelay.setStatus("optional")


class _LcUpsSwitchedReceptStatus_Type(Integer32):
    """Custom type lcUpsSwitchedReceptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LcUpsSwitchedReceptStatus_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptStatus_Object = MibTableColumn
lcUpsSwitchedReceptStatus = _LcUpsSwitchedReceptStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 6),
    _LcUpsSwitchedReceptStatus_Type()
)
lcUpsSwitchedReceptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptStatus.setStatus("optional")


class _LcUpsSwitchedReceptLabel_Type(DisplayString):
    """Custom type lcUpsSwitchedReceptLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LcUpsSwitchedReceptLabel_Type.__name__ = "DisplayString"
_LcUpsSwitchedReceptLabel_Object = MibTableColumn
lcUpsSwitchedReceptLabel = _LcUpsSwitchedReceptLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 7),
    _LcUpsSwitchedReceptLabel_Type()
)
lcUpsSwitchedReceptLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptLabel.setStatus("optional")
_LcUpsBypass_ObjectIdentity = ObjectIdentity
lcUpsBypass = _LcUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13)
)


class _LcUpsOnBypass_Type(Integer32):
    """Custom type lcUpsOnBypass based on Integer32"""
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
        *(("maintenance", 4),
          ("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LcUpsOnBypass_Type.__name__ = "Integer32"
_LcUpsOnBypass_Object = MibScalar
lcUpsOnBypass = _LcUpsOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 1),
    _LcUpsOnBypass_Type()
)
lcUpsOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOnBypass.setStatus("optional")


class _LcUpsBypassFrequency_Type(Integer32):
    """Custom type lcUpsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsBypassFrequency_Type.__name__ = "Integer32"
_LcUpsBypassFrequency_Object = MibScalar
lcUpsBypassFrequency = _LcUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 2),
    _LcUpsBypassFrequency_Type()
)
lcUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassFrequency.setStatus("optional")


class _LcUpsBypassNumLines_Type(Integer32):
    """Custom type lcUpsBypassNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsBypassNumLines_Type.__name__ = "Integer32"
_LcUpsBypassNumLines_Object = MibScalar
lcUpsBypassNumLines = _LcUpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 3),
    _LcUpsBypassNumLines_Type()
)
lcUpsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassNumLines.setStatus("optional")
_LcUpsBypassTable_Object = MibTable
lcUpsBypassTable = _LcUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    lcUpsBypassTable.setStatus("optional")
_LcUpsBypassEntry_Object = MibTableRow
lcUpsBypassEntry = _LcUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1)
)
lcUpsBypassEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "lcUpsBypassLine"),
)
if mibBuilder.loadTexts:
    lcUpsBypassEntry.setStatus("optional")


class _LcUpsBypassLine_Type(Integer32):
    """Custom type lcUpsBypassLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsBypassLine_Type.__name__ = "Integer32"
_LcUpsBypassLine_Object = MibTableColumn
lcUpsBypassLine = _LcUpsBypassLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1, 1),
    _LcUpsBypassLine_Type()
)
lcUpsBypassLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassLine.setStatus("optional")


class _LcUpsBypassVoltage_Type(Integer32):
    """Custom type lcUpsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsBypassVoltage_Type.__name__ = "Integer32"
_LcUpsBypassVoltage_Object = MibTableColumn
lcUpsBypassVoltage = _LcUpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1, 2),
    _LcUpsBypassVoltage_Type()
)
lcUpsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassVoltage.setStatus("optional")


class _LcUpsBypassCurrent_Type(Integer32):
    """Custom type lcUpsBypassCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsBypassCurrent_Type.__name__ = "Integer32"
_LcUpsBypassCurrent_Object = MibTableColumn
lcUpsBypassCurrent = _LcUpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1, 3),
    _LcUpsBypassCurrent_Type()
)
lcUpsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassCurrent.setStatus("optional")
_LcUpsConfig_ObjectIdentity = ObjectIdentity
lcUpsConfig = _LcUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14)
)


class _LcUpsConfigType_Type(Integer32):
    """Custom type lcUpsConfigType based on Integer32"""
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
        *(("lineinteractive", 4),
          ("offline", 3),
          ("online", 2),
          ("unknown", 1))
    )


_LcUpsConfigType_Type.__name__ = "Integer32"
_LcUpsConfigType_Object = MibScalar
lcUpsConfigType = _LcUpsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 1),
    _LcUpsConfigType_Type()
)
lcUpsConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsConfigType.setStatus("optional")


class _LcUpsConfigBypassInstalled_Type(Integer32):
    """Custom type lcUpsConfigBypassInstalled based on Integer32"""
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
        *(("dualinput", 4),
          ("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LcUpsConfigBypassInstalled_Type.__name__ = "Integer32"
_LcUpsConfigBypassInstalled_Object = MibScalar
lcUpsConfigBypassInstalled = _LcUpsConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 2),
    _LcUpsConfigBypassInstalled_Type()
)
lcUpsConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsConfigBypassInstalled.setStatus("optional")


class _LcUpsConfigModuleCount_Type(Integer32):
    """Custom type lcUpsConfigModuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LcUpsConfigModuleCount_Type.__name__ = "Integer32"
_LcUpsConfigModuleCount_Object = MibScalar
lcUpsConfigModuleCount = _LcUpsConfigModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 3),
    _LcUpsConfigModuleCount_Type()
)
lcUpsConfigModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsConfigModuleCount.setStatus("optional")


class _LcUpsConfigCurrentModule_Type(Integer32):
    """Custom type lcUpsConfigCurrentModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LcUpsConfigCurrentModule_Type.__name__ = "Integer32"
_LcUpsConfigCurrentModule_Object = MibScalar
lcUpsConfigCurrentModule = _LcUpsConfigCurrentModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 4),
    _LcUpsConfigCurrentModule_Type()
)
lcUpsConfigCurrentModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigCurrentModule.setStatus("optional")


class _LcUpsConfigAudibleStatus_Type(Integer32):
    """Custom type lcUpsConfigAudibleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("muted", 3))
    )


_LcUpsConfigAudibleStatus_Type.__name__ = "Integer32"
_LcUpsConfigAudibleStatus_Object = MibScalar
lcUpsConfigAudibleStatus = _LcUpsConfigAudibleStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 5),
    _LcUpsConfigAudibleStatus_Type()
)
lcUpsConfigAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigAudibleStatus.setStatus("optional")


class _LcUpsConfigLowBattTime_Type(Integer32):
    """Custom type lcUpsConfigLowBattTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcUpsConfigLowBattTime_Type.__name__ = "Integer32"
_LcUpsConfigLowBattTime_Object = MibScalar
lcUpsConfigLowBattTime = _LcUpsConfigLowBattTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 6),
    _LcUpsConfigLowBattTime_Type()
)
lcUpsConfigLowBattTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigLowBattTime.setStatus("optional")


class _LcUpsConfigAutoRestart_Type(Integer32):
    """Custom type lcUpsConfigAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_LcUpsConfigAutoRestart_Type.__name__ = "Integer32"
_LcUpsConfigAutoRestart_Object = MibScalar
lcUpsConfigAutoRestart = _LcUpsConfigAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 7),
    _LcUpsConfigAutoRestart_Type()
)
lcUpsConfigAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigAutoRestart.setStatus("optional")
_LuUPStationS_ObjectIdentity = ObjectIdentity
luUPStationS = _LuUPStationS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2)
)
_LsUpsIdent_ObjectIdentity = ObjectIdentity
lsUpsIdent = _LsUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 1)
)


class _LsUpsIdentFirmwareVersion_Type(DisplayString):
    """Custom type lsUpsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LsUpsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_LsUpsIdentFirmwareVersion_Object = MibScalar
lsUpsIdentFirmwareVersion = _LsUpsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 1, 1),
    _LsUpsIdentFirmwareVersion_Type()
)
lsUpsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsIdentFirmwareVersion.setStatus("optional")
_LsUpsAlarm_ObjectIdentity = ObjectIdentity
lsUpsAlarm = _LsUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 6)
)
_LsUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lsUpsAlarmConditions = _LsUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 6, 1)
)
_LsUpsAlarmCheckAirFilter_ObjectIdentity = ObjectIdentity
lsUpsAlarmCheckAirFilter = _LsUpsAlarmCheckAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 6, 1, 1)
)
_LsUpsTraps_ObjectIdentity = ObjectIdentity
lsUpsTraps = _LsUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 11)
)
_LsUpsConfig_ObjectIdentity = ObjectIdentity
lsUpsConfig = _LsUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 12)
)


class _LsUpsConfigBypassInstalled_Type(Integer32):
    """Custom type lsUpsConfigBypassInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LsUpsConfigBypassInstalled_Type.__name__ = "Integer32"
_LsUpsConfigBypassInstalled_Object = MibScalar
lsUpsConfigBypassInstalled = _LsUpsConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 12, 1),
    _LsUpsConfigBypassInstalled_Type()
)
lsUpsConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsConfigBypassInstalled.setStatus("optional")
_LsUpsBypass_ObjectIdentity = ObjectIdentity
lsUpsBypass = _LsUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13)
)


class _LsUpsOnBypass_Type(Integer32):
    """Custom type lsUpsOnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LsUpsOnBypass_Type.__name__ = "Integer32"
_LsUpsOnBypass_Object = MibScalar
lsUpsOnBypass = _LsUpsOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 1),
    _LsUpsOnBypass_Type()
)
lsUpsOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsOnBypass.setStatus("optional")


class _LsUpsBypassFrequency_Type(Integer32):
    """Custom type lsUpsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LsUpsBypassFrequency_Type.__name__ = "Integer32"
_LsUpsBypassFrequency_Object = MibScalar
lsUpsBypassFrequency = _LsUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 2),
    _LsUpsBypassFrequency_Type()
)
lsUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassFrequency.setStatus("optional")


class _LsUpsBypassNumLines_Type(Integer32):
    """Custom type lsUpsBypassNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LsUpsBypassNumLines_Type.__name__ = "Integer32"
_LsUpsBypassNumLines_Object = MibScalar
lsUpsBypassNumLines = _LsUpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 3),
    _LsUpsBypassNumLines_Type()
)
lsUpsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassNumLines.setStatus("optional")
_LsUpsBypassTable_Object = MibTable
lsUpsBypassTable = _LsUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4)
)
if mibBuilder.loadTexts:
    lsUpsBypassTable.setStatus("optional")
_LsUpsBypassEntry_Object = MibTableRow
lsUpsBypassEntry = _LsUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1)
)
lsUpsBypassEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "lsUpsBypassLine"),
)
if mibBuilder.loadTexts:
    lsUpsBypassEntry.setStatus("optional")


class _LsUpsBypassLine_Type(Integer32):
    """Custom type lsUpsBypassLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LsUpsBypassLine_Type.__name__ = "Integer32"
_LsUpsBypassLine_Object = MibTableColumn
lsUpsBypassLine = _LsUpsBypassLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1, 1),
    _LsUpsBypassLine_Type()
)
lsUpsBypassLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassLine.setStatus("optional")


class _LsUpsBypassVoltage_Type(Integer32):
    """Custom type lsUpsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LsUpsBypassVoltage_Type.__name__ = "Integer32"
_LsUpsBypassVoltage_Object = MibTableColumn
lsUpsBypassVoltage = _LsUpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1, 2),
    _LsUpsBypassVoltage_Type()
)
lsUpsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassVoltage.setStatus("optional")


class _LsUpsBypassCurrent_Type(Integer32):
    """Custom type lsUpsBypassCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LsUpsBypassCurrent_Type.__name__ = "Integer32"
_LsUpsBypassCurrent_Object = MibTableColumn
lsUpsBypassCurrent = _LsUpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1, 3),
    _LsUpsBypassCurrent_Type()
)
lsUpsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassCurrent.setStatus("optional")
_LuUPStationD_ObjectIdentity = ObjectIdentity
luUPStationD = _LuUPStationD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3)
)
_LdUpsInput_ObjectIdentity = ObjectIdentity
ldUpsInput = _LdUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 3)
)


class _LdUpsInputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsInputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsInputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsInputMaxVoltsSinceLastPoll_Object = MibScalar
ldUpsInputMaxVoltsSinceLastPoll = _LdUpsInputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 3, 1),
    _LdUpsInputMaxVoltsSinceLastPoll_Type()
)
ldUpsInputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsInputMaxVoltsSinceLastPoll.setStatus("optional")


class _LdUpsInputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsInputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsInputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsInputMinVoltsSinceLastPoll_Object = MibScalar
ldUpsInputMinVoltsSinceLastPoll = _LdUpsInputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 3, 2),
    _LdUpsInputMinVoltsSinceLastPoll_Type()
)
ldUpsInputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsInputMinVoltsSinceLastPoll.setStatus("optional")
_LdUpsOutput_ObjectIdentity = ObjectIdentity
ldUpsOutput = _LdUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 4)
)


class _LdUpsOutputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsOutputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsOutputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsOutputMaxVoltsSinceLastPoll_Object = MibScalar
ldUpsOutputMaxVoltsSinceLastPoll = _LdUpsOutputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 4, 1),
    _LdUpsOutputMaxVoltsSinceLastPoll_Type()
)
ldUpsOutputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsOutputMaxVoltsSinceLastPoll.setStatus("optional")


class _LdUpsOutputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsOutputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsOutputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsOutputMinVoltsSinceLastPoll_Object = MibScalar
ldUpsOutputMinVoltsSinceLastPoll = _LdUpsOutputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 4, 2),
    _LdUpsOutputMinVoltsSinceLastPoll_Type()
)
ldUpsOutputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsOutputMinVoltsSinceLastPoll.setStatus("optional")
_LdUpsAlarm_ObjectIdentity = ObjectIdentity
ldUpsAlarm = _LdUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6)
)
_LdUpsAlarmConditions_ObjectIdentity = ObjectIdentity
ldUpsAlarmConditions = _LdUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1)
)
_LdUpsAlarmDCOverVoltageShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmDCOverVoltageShutdown = _LdUpsAlarmDCOverVoltageShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 1)
)
_LdUpsAlarmOutputShortShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmOutputShortShutdown = _LdUpsAlarmOutputShortShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 2)
)
_LdUpsAlarmLNReversedShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmLNReversedShutdown = _LdUpsAlarmLNReversedShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 3)
)
_LdUpsAlarmImminentShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmImminentShutdown = _LdUpsAlarmImminentShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 4)
)
_LdUpsAlarmInputFreqError_ObjectIdentity = ObjectIdentity
ldUpsAlarmInputFreqError = _LdUpsAlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 5)
)
_LdUpsAlarmBoostOn_ObjectIdentity = ObjectIdentity
ldUpsAlarmBoostOn = _LdUpsAlarmBoostOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 6)
)
_LdUpsAlarmReplaceBattery_ObjectIdentity = ObjectIdentity
ldUpsAlarmReplaceBattery = _LdUpsAlarmReplaceBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 7)
)
_LdUpsAlarmOutputOverVoltage_ObjectIdentity = ObjectIdentity
ldUpsAlarmOutputOverVoltage = _LdUpsAlarmOutputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 8)
)
_LdUpsAlarmOutputUnderVoltage_ObjectIdentity = ObjectIdentity
ldUpsAlarmOutputUnderVoltage = _LdUpsAlarmOutputUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 9)
)
_LdUpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
ldUpsAlarmChargerFailed = _LdUpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 10)
)
_LdUpsTraps_ObjectIdentity = ObjectIdentity
ldUpsTraps = _LdUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11)
)
_LuUPStationG_ObjectIdentity = ObjectIdentity
luUPStationG = _LuUPStationG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4)
)
_LgUpsAlarm_ObjectIdentity = ObjectIdentity
lgUpsAlarm = _LgUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6)
)
_LgUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lgUpsAlarmConditions = _LgUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1)
)
_LgUpsAlarmDCOverVoltageShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmDCOverVoltageShutdown = _LgUpsAlarmDCOverVoltageShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 1)
)
_LgUpsAlarmOutputShortShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmOutputShortShutdown = _LgUpsAlarmOutputShortShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 2)
)
_LgUpsAlarmLNReversedShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmLNReversedShutdown = _LgUpsAlarmLNReversedShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 3)
)
_LgUpsAlarmRemoteShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmRemoteShutdown = _LgUpsAlarmRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 4)
)
_LgUpsAlarmInputUVOnStartup_ObjectIdentity = ObjectIdentity
lgUpsAlarmInputUVOnStartup = _LgUpsAlarmInputUVOnStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 5)
)
_LgUpsAlarmPFCFailedOnStartup_ObjectIdentity = ObjectIdentity
lgUpsAlarmPFCFailedOnStartup = _LgUpsAlarmPFCFailedOnStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 6)
)
_LgUpsTraps_ObjectIdentity = ObjectIdentity
lgUpsTraps = _LgUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11)
)
_LuSeries300_ObjectIdentity = ObjectIdentity
luSeries300 = _LuSeries300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 5)
)
_LuExternal_ObjectIdentity = ObjectIdentity
luExternal = _LuExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 6)
)
_LuUPStationS3_ObjectIdentity = ObjectIdentity
luUPStationS3 = _LuUPStationS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 7)
)
_LuSeries200_ObjectIdentity = ObjectIdentity
luSeries200 = _LuSeries200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8)
)
_LuSeries200Input_ObjectIdentity = ObjectIdentity
luSeries200Input = _LuSeries200Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3)
)


class _LuSeries200InputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type luSeries200InputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LuSeries200InputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LuSeries200InputMaxVoltsSinceLastPoll_Object = MibScalar
luSeries200InputMaxVoltsSinceLastPoll = _LuSeries200InputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3, 1),
    _LuSeries200InputMaxVoltsSinceLastPoll_Type()
)
luSeries200InputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200InputMaxVoltsSinceLastPoll.setStatus("optional")


class _LuSeries200InputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type luSeries200InputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LuSeries200InputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LuSeries200InputMinVoltsSinceLastPoll_Object = MibScalar
luSeries200InputMinVoltsSinceLastPoll = _LuSeries200InputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3, 2),
    _LuSeries200InputMinVoltsSinceLastPoll_Type()
)
luSeries200InputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200InputMinVoltsSinceLastPoll.setStatus("optional")
_LuSeries200Alarm_ObjectIdentity = ObjectIdentity
luSeries200Alarm = _LuSeries200Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6)
)
_LuSeries200AlarmConditions_ObjectIdentity = ObjectIdentity
luSeries200AlarmConditions = _LuSeries200AlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6, 1)
)
_LuSeries200AlarmInputFreqError_ObjectIdentity = ObjectIdentity
luSeries200AlarmInputFreqError = _LuSeries200AlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6, 1, 1)
)
_LuSeries200Config_ObjectIdentity = ObjectIdentity
luSeries200Config = _LuSeries200Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12)
)


class _LuSeries200ConfigBypassInstalled_Type(Integer32):
    """Custom type luSeries200ConfigBypassInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LuSeries200ConfigBypassInstalled_Type.__name__ = "Integer32"
_LuSeries200ConfigBypassInstalled_Object = MibScalar
luSeries200ConfigBypassInstalled = _LuSeries200ConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12, 1),
    _LuSeries200ConfigBypassInstalled_Type()
)
luSeries200ConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200ConfigBypassInstalled.setStatus("optional")


class _LuSeries200ConfigFrequencyChangerModel_Type(Integer32):
    """Custom type luSeries200ConfigFrequencyChangerModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LuSeries200ConfigFrequencyChangerModel_Type.__name__ = "Integer32"
_LuSeries200ConfigFrequencyChangerModel_Object = MibScalar
luSeries200ConfigFrequencyChangerModel = _LuSeries200ConfigFrequencyChangerModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12, 2),
    _LuSeries200ConfigFrequencyChangerModel_Type()
)
luSeries200ConfigFrequencyChangerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200ConfigFrequencyChangerModel.setStatus("optional")
_LuSeries200Bypass_ObjectIdentity = ObjectIdentity
luSeries200Bypass = _LuSeries200Bypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 13)
)


class _LuSeries200OnBypass_Type(Integer32):
    """Custom type luSeries200OnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_LuSeries200OnBypass_Type.__name__ = "Integer32"
_LuSeries200OnBypass_Object = MibScalar
luSeries200OnBypass = _LuSeries200OnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 13, 1),
    _LuSeries200OnBypass_Type()
)
luSeries200OnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200OnBypass.setStatus("optional")
_LuSeries4300_ObjectIdentity = ObjectIdentity
luSeries4300 = _LuSeries4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10)
)
_Ls43cUpsIdent_ObjectIdentity = ObjectIdentity
ls43cUpsIdent = _Ls43cUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 1)
)


class _Ls43cUpsIdentFirmwareVersion_Type(DisplayString):
    """Custom type ls43cUpsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_Ls43cUpsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_Ls43cUpsIdentFirmwareVersion_Object = MibScalar
ls43cUpsIdentFirmwareVersion = _Ls43cUpsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 1, 1),
    _Ls43cUpsIdentFirmwareVersion_Type()
)
ls43cUpsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsIdentFirmwareVersion.setStatus("optional")
_Ls43cUpsConfig_ObjectIdentity = ObjectIdentity
ls43cUpsConfig = _Ls43cUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 12)
)


class _Ls43cUpsConfigBypassInstalled_Type(Integer32):
    """Custom type ls43cUpsConfigBypassInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_Ls43cUpsConfigBypassInstalled_Type.__name__ = "Integer32"
_Ls43cUpsConfigBypassInstalled_Object = MibScalar
ls43cUpsConfigBypassInstalled = _Ls43cUpsConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 12, 1),
    _Ls43cUpsConfigBypassInstalled_Type()
)
ls43cUpsConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsConfigBypassInstalled.setStatus("optional")
_Ls43cUpsBypass_ObjectIdentity = ObjectIdentity
ls43cUpsBypass = _Ls43cUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13)
)


class _Ls43cUpsOnBypass_Type(Integer32):
    """Custom type ls43cUpsOnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unknown", 1),
          ("yes", 2))
    )


_Ls43cUpsOnBypass_Type.__name__ = "Integer32"
_Ls43cUpsOnBypass_Object = MibScalar
ls43cUpsOnBypass = _Ls43cUpsOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 1),
    _Ls43cUpsOnBypass_Type()
)
ls43cUpsOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsOnBypass.setStatus("optional")


class _Ls43cUpsBypassFrequency_Type(Integer32):
    """Custom type ls43cUpsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Ls43cUpsBypassFrequency_Type.__name__ = "Integer32"
_Ls43cUpsBypassFrequency_Object = MibScalar
ls43cUpsBypassFrequency = _Ls43cUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 2),
    _Ls43cUpsBypassFrequency_Type()
)
ls43cUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassFrequency.setStatus("optional")


class _Ls43cUpsBypassNumLines_Type(Integer32):
    """Custom type ls43cUpsBypassNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ls43cUpsBypassNumLines_Type.__name__ = "Integer32"
_Ls43cUpsBypassNumLines_Object = MibScalar
ls43cUpsBypassNumLines = _Ls43cUpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 3),
    _Ls43cUpsBypassNumLines_Type()
)
ls43cUpsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassNumLines.setStatus("optional")
_Ls43cUpsBypassTable_Object = MibTable
ls43cUpsBypassTable = _Ls43cUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4)
)
if mibBuilder.loadTexts:
    ls43cUpsBypassTable.setStatus("optional")
_Ls43cUpsBypassEntry_Object = MibTableRow
ls43cUpsBypassEntry = _Ls43cUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1)
)
ls43cUpsBypassEntry.setIndexNames(
    (0, "LIEBERT-UPS-MIB", "ls43cUpsBypassLine"),
)
if mibBuilder.loadTexts:
    ls43cUpsBypassEntry.setStatus("optional")


class _Ls43cUpsBypassLine_Type(Integer32):
    """Custom type ls43cUpsBypassLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ls43cUpsBypassLine_Type.__name__ = "Integer32"
_Ls43cUpsBypassLine_Object = MibTableColumn
ls43cUpsBypassLine = _Ls43cUpsBypassLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1, 1),
    _Ls43cUpsBypassLine_Type()
)
ls43cUpsBypassLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassLine.setStatus("optional")


class _Ls43cUpsBypassVoltage_Type(Integer32):
    """Custom type ls43cUpsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Ls43cUpsBypassVoltage_Type.__name__ = "Integer32"
_Ls43cUpsBypassVoltage_Object = MibTableColumn
ls43cUpsBypassVoltage = _Ls43cUpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1, 2),
    _Ls43cUpsBypassVoltage_Type()
)
ls43cUpsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassVoltage.setStatus("optional")


class _Ls43cUpsBypassCurrent_Type(Integer32):
    """Custom type ls43cUpsBypassCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Ls43cUpsBypassCurrent_Type.__name__ = "Integer32"
_Ls43cUpsBypassCurrent_Object = MibTableColumn
ls43cUpsBypassCurrent = _Ls43cUpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1, 3),
    _Ls43cUpsBypassCurrent_Type()
)
ls43cUpsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassCurrent.setStatus("optional")
_LuUpsModule_ObjectIdentity = ObjectIdentity
luUpsModule = _LuUpsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 11)
)
_LuSystemCabinet_ObjectIdentity = ObjectIdentity
luSystemCabinet = _LuSystemCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 12)
)
_LuUPStationGxt_ObjectIdentity = ObjectIdentity
luUPStationGxt = _LuUPStationGxt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 14)
)
_LuPowerSure_ObjectIdentity = ObjectIdentity
luPowerSure = _LuPowerSure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 15)
)
_LuExperimental_ObjectIdentity = ObjectIdentity
luExperimental = _LuExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 2)
)
_LuPrivate_ObjectIdentity = ObjectIdentity
luPrivate = _LuPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 3)
)

# Managed Objects groups


# Notification objects

lcUpsOverloadWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 1)
)
lcUpsOverloadWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadWarningTrap.setStatus(
        ""
    )

lcUpsOverloadShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 2)
)
lcUpsOverloadShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadShutdownTrap.setStatus(
        ""
    )

lcUpsOnBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 3)
)
lcUpsOnBatteryTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOnBatteryTrap.setStatus(
        ""
    )

lcUpsLowBatteryWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 4)
)
lcUpsLowBatteryWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryWarningTrap.setStatus(
        ""
    )

lcUpsLowBatteryShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 5)
)
lcUpsLowBatteryShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryShutdownTrap.setStatus(
        ""
    )

lcUpsUtilPowerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 6)
)
lcUpsUtilPowerFailedTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerFailedTrap.setStatus(
        ""
    )

lcUpsUtilPowerRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 7)
)
lcUpsUtilPowerRestoredTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerRestoredTrap.setStatus(
        ""
    )

lcUpsInputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 8)
)
lcUpsInputOverVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInputOverVoltageTrap.setStatus(
        ""
    )

lcUpsOverTempWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 9)
)
lcUpsOverTempWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempWarningTrap.setStatus(
        ""
    )

lcUpsOverTempShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 10)
)
lcUpsOverTempShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempShutdownTrap.setStatus(
        ""
    )

lcUpsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 11)
)
lcUpsAlarmTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsAlarmTrap.setStatus(
        ""
    )

lcUpsOutputOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 12)
)
lcUpsOutputOffTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffTrap.setStatus(
        ""
    )

lcUpsOutputOffWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 13)
)
lcUpsOutputOffWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffWarningTrap.setStatus(
        ""
    )

lcUpsOutputOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 14)
)
lcUpsOutputOnTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnTrap.setStatus(
        ""
    )

lcUpsOutputOnWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 15)
)
lcUpsOutputOnWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnWarningTrap.setStatus(
        ""
    )

lcUpsUnixShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 16)
)
lcUpsUnixShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUnixShutdownTrap.setStatus(
        ""
    )

lcUpsUnixShutdownWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 17)
)
lcUpsUnixShutdownWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUnixShutdownWarningTrap.setStatus(
        ""
    )

lcUpsReceptOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 18)
)
lcUpsReceptOffTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-UPS-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOffTrap.setStatus(
        ""
    )

lcUpsReceptOffWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 19)
)
lcUpsReceptOffWarningTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-UPS-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOffWarningTrap.setStatus(
        ""
    )

lcUpsReceptOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 20)
)
lcUpsReceptOnTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-UPS-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOnTrap.setStatus(
        ""
    )

lcUpsReceptOnWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 21)
)
lcUpsReceptOnWarningTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-UPS-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOnWarningTrap.setStatus(
        ""
    )

lcUpsInputFreqErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 22)
)
lcUpsInputFreqErrorTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInputFreqErrorTrap.setStatus(
        ""
    )

lcUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 23)
)
lcUpsDCOverVoltageShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

lcUpsOutputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 24)
)
lcUpsOutputOverVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOverVoltageTrap.setStatus(
        ""
    )

lcUpsFuseBlownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 25)
)
lcUpsFuseBlownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsFuseBlownTrap.setStatus(
        ""
    )

lcUpsEmergencyPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 26)
)
lcUpsEmergencyPowerOffTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsEmergencyPowerOffTrap.setStatus(
        ""
    )

lcUpsControlPowerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 27)
)
lcUpsControlPowerFailureTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsControlPowerFailureTrap.setStatus(
        ""
    )

lcUpsReversePowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 28)
)
lcUpsReversePowerTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsReversePowerTrap.setStatus(
        ""
    )

lcUpsPhaseRotationErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 29)
)
lcUpsPhaseRotationErrorTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsPhaseRotationErrorTrap.setStatus(
        ""
    )

lcUpsLoadOnBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 30)
)
lcUpsLoadOnBypassTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLoadOnBypassTrap.setStatus(
        ""
    )

lcUpsEmergencyXferToBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 31)
)
lcUpsEmergencyXferToBypassTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsEmergencyXferToBypassTrap.setStatus(
        ""
    )

lcUpsInverterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 34)
)
lcUpsInverterFaultTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInverterFaultTrap.setStatus(
        ""
    )

lsUpsCheckAirFilterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 11, 0, 1)
)
lsUpsCheckAirFilterTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lsUpsCheckAirFilterTrap.setStatus(
        ""
    )

ldUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 1)
)
ldUpsDCOverVoltageShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

ldUpsOutputShortShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 2)
)
ldUpsOutputShortShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsOutputShortShutdownTrap.setStatus(
        ""
    )

ldUpsLNReversedShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 3)
)
ldUpsLNReversedShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsLNReversedShutdownTrap.setStatus(
        ""
    )

ldUpsImminentShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 4)
)
ldUpsImminentShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsImminentShutdownTrap.setStatus(
        ""
    )

ldUpsInputFreqErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 5)
)
ldUpsInputFreqErrorTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsInputFreqErrorTrap.setStatus(
        ""
    )

ldUpsOutputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 6)
)
ldUpsOutputOverVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsOutputOverVoltageTrap.setStatus(
        ""
    )

ldUpsOutputUnderVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 7)
)
ldUpsOutputUnderVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsOutputUnderVoltageTrap.setStatus(
        ""
    )

ldUpsChargerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 8)
)
ldUpsChargerFailedTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsChargerFailedTrap.setStatus(
        ""
    )

lgUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 1)
)
lgUpsDCOverVoltageShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

lgUpsOutputShortShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 2)
)
lgUpsOutputShortShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsOutputShortShutdownTrap.setStatus(
        ""
    )

lgUpsLNReversedShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 3)
)
lgUpsLNReversedShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsLNReversedShutdownTrap.setStatus(
        ""
    )

lgUpsInputUVOnStartupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 4)
)
lgUpsInputUVOnStartupTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsInputUVOnStartupTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-UPS-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertUps": liebertUps,
       "luExtensions": luExtensions,
       "luCore": luCore,
       "lcUpsIdent": lcUpsIdent,
       "lcUpsIdentManufacturer": lcUpsIdentManufacturer,
       "lcUpsIdentModel": lcUpsIdentModel,
       "lcUpsIdentSoftwareVersion": lcUpsIdentSoftwareVersion,
       "lcUpsIdentSpecific": lcUpsIdentSpecific,
       "lcUpsIdentFirmwareVersion": lcUpsIdentFirmwareVersion,
       "lcUpsIdentSerialNumber": lcUpsIdentSerialNumber,
       "lcUpsIdentManufactureDate": lcUpsIdentManufactureDate,
       "lcUpsBattery": lcUpsBattery,
       "lcUpsBatTimeRemaining": lcUpsBatTimeRemaining,
       "lcUpsBatTemperature": lcUpsBatTemperature,
       "lcUpsBatVoltage": lcUpsBatVoltage,
       "lcUpsBatCurrent": lcUpsBatCurrent,
       "lcUpsBatCapacity": lcUpsBatCapacity,
       "lcUpsBatTotalDischCounts": lcUpsBatTotalDischCounts,
       "lcUpsBatCycleDurationInSeconds": lcUpsBatCycleDurationInSeconds,
       "lcUpsBatAmpHours": lcUpsBatAmpHours,
       "lcUpsBatKWhours": lcUpsBatKWhours,
       "lcUpsBatWattHours": lcUpsBatWattHours,
       "lcUpsInput": lcUpsInput,
       "lcUpsInputFrequency": lcUpsInputFrequency,
       "lcUpsInputBrownOuts": lcUpsInputBrownOuts,
       "lcUpsInputBlackOuts": lcUpsInputBlackOuts,
       "lcUpsInputTransients": lcUpsInputTransients,
       "lcUpsInputNumLines": lcUpsInputNumLines,
       "lcUpsInputTable": lcUpsInputTable,
       "lcUpsInputEntry": lcUpsInputEntry,
       "lcUpsInputLine": lcUpsInputLine,
       "lcUpsInputVoltage": lcUpsInputVoltage,
       "lcUpsInputCurrent": lcUpsInputCurrent,
       "lcUpsInputVA": lcUpsInputVA,
       "lcUpsOutput": lcUpsOutput,
       "lcUpsOutputFrequency": lcUpsOutputFrequency,
       "lcUpsOutputLoad": lcUpsOutputLoad,
       "lcUpsOutputNumLines": lcUpsOutputNumLines,
       "lcUpsOutputTable": lcUpsOutputTable,
       "lcUpsOutputEntry": lcUpsOutputEntry,
       "lcUpsOutputLine": lcUpsOutputLine,
       "lcUpsOutputVoltage": lcUpsOutputVoltage,
       "lcUpsOutputCurrent": lcUpsOutputCurrent,
       "lcUpsOutputVA": lcUpsOutputVA,
       "lcUpsOutputWatts": lcUpsOutputWatts,
       "lcUpsInverter": lcUpsInverter,
       "lcUpsInverterStatus": lcUpsInverterStatus,
       "lcUpsInverterTemp": lcUpsInverterTemp,
       "lcUpsAlarm": lcUpsAlarm,
       "lcUpsAlarms": lcUpsAlarms,
       "lcUpsAlarmTable": lcUpsAlarmTable,
       "lcUpsAlarmEntry": lcUpsAlarmEntry,
       "lcUpsAlarmId": lcUpsAlarmId,
       "lcUpsAlarmDescr": lcUpsAlarmDescr,
       "lcUpsAlarmTime": lcUpsAlarmTime,
       "lcUpsAlarmConditions": lcUpsAlarmConditions,
       "lcUpsAlarmLowBatteryWarning": lcUpsAlarmLowBatteryWarning,
       "lcUpsAlarmLowBatteryShutdown": lcUpsAlarmLowBatteryShutdown,
       "lcUpsAlarmUtilFailed": lcUpsAlarmUtilFailed,
       "lcUpsAlarmOverTempWarning": lcUpsAlarmOverTempWarning,
       "lcUpsAlarmOverTempShutdown": lcUpsAlarmOverTempShutdown,
       "lcUpsAlarmOutputOverloadWarning": lcUpsAlarmOutputOverloadWarning,
       "lcUpsAlarmOutputOverloadShutdown": lcUpsAlarmOutputOverloadShutdown,
       "lcUpsAlarmInputOverVoltage": lcUpsAlarmInputOverVoltage,
       "lcUpsAlarmBatteryBad": lcUpsAlarmBatteryBad,
       "lcUpsAlarmOnBattery": lcUpsAlarmOnBattery,
       "lcUpsAlarmStopNoticeIssued": lcUpsAlarmStopNoticeIssued,
       "lcUpsAlarmUpsOff": lcUpsAlarmUpsOff,
       "lcUpsAlarmInputFreqError": lcUpsAlarmInputFreqError,
       "lcUpsAlarmOutputUnderVoltage": lcUpsAlarmOutputUnderVoltage,
       "lcUpsAlarmOutputOverVoltage": lcUpsAlarmOutputOverVoltage,
       "lcUpsBadBypassPower": lcUpsBadBypassPower,
       "lcUpsAlarmDCOverVoltageShutdown": lcUpsAlarmDCOverVoltageShutdown,
       "lcUpsAlarmHardwareShutdown": lcUpsAlarmHardwareShutdown,
       "lcUpsAlarmEmergencyXferToBypass": lcUpsAlarmEmergencyXferToBypass,
       "lcUpsAlarmInverterFault": lcUpsAlarmInverterFault,
       "lcUpsAlarmPhaseRotationError": lcUpsAlarmPhaseRotationError,
       "lcUpsAlarmFuseBlown": lcUpsAlarmFuseBlown,
       "lcUpsAlarmAmbientOverTemp": lcUpsAlarmAmbientOverTemp,
       "lcUpsAlarmEmergencyPowerOff": lcUpsAlarmEmergencyPowerOff,
       "lcUpsAlarmFanFailed": lcUpsAlarmFanFailed,
       "lcUpsAlarmControlPowerFailed": lcUpsAlarmControlPowerFailed,
       "lcUpsAlarmReversePower": lcUpsAlarmReversePower,
       "lcUpsAlarmDCgroundFault": lcUpsAlarmDCgroundFault,
       "lcUpsAlarmLoadOnBypass": lcUpsAlarmLoadOnBypass,
       "lcUpsAlarmBatteryCbOpen": lcUpsAlarmBatteryCbOpen,
       "lcUpsAlarmInputCbOpen": lcUpsAlarmInputCbOpen,
       "lcUpsAlarmOutputCbOpen": lcUpsAlarmOutputCbOpen,
       "lcUpsAlarmOutputFreqError": lcUpsAlarmOutputFreqError,
       "lcUpsAlarmStaticSwUnable": lcUpsAlarmStaticSwUnable,
       "lcUpsAlarmManualResetXfer": lcUpsAlarmManualResetXfer,
       "lcUpsAlarmAutoRexferPrimed": lcUpsAlarmAutoRexferPrimed,
       "lcUpsAlarmBattCycleBuffWarn": lcUpsAlarmBattCycleBuffWarn,
       "lcUpsAlarmModuleSummary": lcUpsAlarmModuleSummary,
       "lcUpsLineCorrectionActive": lcUpsLineCorrectionActive,
       "lcUpsTest": lcUpsTest,
       "lcUpsTestBattery": lcUpsTestBattery,
       "lcUpsTestBatteryStatus": lcUpsTestBatteryStatus,
       "lcUpsTestDiag": lcUpsTestDiag,
       "lcUpsTestDiagStatus": lcUpsTestDiagStatus,
       "lcUpsControl": lcUpsControl,
       "lcUpsControlOutputOffDelay": lcUpsControlOutputOffDelay,
       "lcUpsControlOutputOnDelay": lcUpsControlOutputOnDelay,
       "lcUpsControlOutputOffTrapDelay": lcUpsControlOutputOffTrapDelay,
       "lcUpsControlOutputOnTrapDelay": lcUpsControlOutputOnTrapDelay,
       "lcUpsControlUnixShutdownDelay": lcUpsControlUnixShutdownDelay,
       "lcUpsControlUnixShutdownTrapDelay": lcUpsControlUnixShutdownTrapDelay,
       "lcUpsControlCancelCommands": lcUpsControlCancelCommands,
       "lcUpsControlRebootAgentDelay": lcUpsControlRebootAgentDelay,
       "lcUpsNominal": lcUpsNominal,
       "lcUpsNominalOutputVoltage": lcUpsNominalOutputVoltage,
       "lcUpsNominalInputVoltage": lcUpsNominalInputVoltage,
       "lcUpsNominalOutputVA": lcUpsNominalOutputVA,
       "lcUpsNominalOutputWatts": lcUpsNominalOutputWatts,
       "lcUpsNominalOutputFreq": lcUpsNominalOutputFreq,
       "lcUpsNominalInputFreq": lcUpsNominalInputFreq,
       "lcUpsNominalOutputVaRating": lcUpsNominalOutputVaRating,
       "lcUpsNominalOutputWattsRating": lcUpsNominalOutputWattsRating,
       "lcUpsTraps": lcUpsTraps,
       "lcUpsOverloadWarningTrap": lcUpsOverloadWarningTrap,
       "lcUpsOverloadShutdownTrap": lcUpsOverloadShutdownTrap,
       "lcUpsOnBatteryTrap": lcUpsOnBatteryTrap,
       "lcUpsLowBatteryWarningTrap": lcUpsLowBatteryWarningTrap,
       "lcUpsLowBatteryShutdownTrap": lcUpsLowBatteryShutdownTrap,
       "lcUpsUtilPowerFailedTrap": lcUpsUtilPowerFailedTrap,
       "lcUpsUtilPowerRestoredTrap": lcUpsUtilPowerRestoredTrap,
       "lcUpsInputOverVoltageTrap": lcUpsInputOverVoltageTrap,
       "lcUpsOverTempWarningTrap": lcUpsOverTempWarningTrap,
       "lcUpsOverTempShutdownTrap": lcUpsOverTempShutdownTrap,
       "lcUpsAlarmTrap": lcUpsAlarmTrap,
       "lcUpsOutputOffTrap": lcUpsOutputOffTrap,
       "lcUpsOutputOffWarningTrap": lcUpsOutputOffWarningTrap,
       "lcUpsOutputOnTrap": lcUpsOutputOnTrap,
       "lcUpsOutputOnWarningTrap": lcUpsOutputOnWarningTrap,
       "lcUpsUnixShutdownTrap": lcUpsUnixShutdownTrap,
       "lcUpsUnixShutdownWarningTrap": lcUpsUnixShutdownWarningTrap,
       "lcUpsReceptOffTrap": lcUpsReceptOffTrap,
       "lcUpsReceptOffWarningTrap": lcUpsReceptOffWarningTrap,
       "lcUpsReceptOnTrap": lcUpsReceptOnTrap,
       "lcUpsReceptOnWarningTrap": lcUpsReceptOnWarningTrap,
       "lcUpsInputFreqErrorTrap": lcUpsInputFreqErrorTrap,
       "lcUpsDCOverVoltageShutdownTrap": lcUpsDCOverVoltageShutdownTrap,
       "lcUpsOutputOverVoltageTrap": lcUpsOutputOverVoltageTrap,
       "lcUpsFuseBlownTrap": lcUpsFuseBlownTrap,
       "lcUpsEmergencyPowerOffTrap": lcUpsEmergencyPowerOffTrap,
       "lcUpsControlPowerFailureTrap": lcUpsControlPowerFailureTrap,
       "lcUpsReversePowerTrap": lcUpsReversePowerTrap,
       "lcUpsPhaseRotationErrorTrap": lcUpsPhaseRotationErrorTrap,
       "lcUpsLoadOnBypassTrap": lcUpsLoadOnBypassTrap,
       "lcUpsEmergencyXferToBypassTrap": lcUpsEmergencyXferToBypassTrap,
       "lcUpsInverterFaultTrap": lcUpsInverterFaultTrap,
       "lcUpsSwitchedReceptacles": lcUpsSwitchedReceptacles,
       "lcUpsSwitchedReceptMaxNum": lcUpsSwitchedReceptMaxNum,
       "lcUpsSwitchedReceptTable": lcUpsSwitchedReceptTable,
       "lcUpsSwitchedReceptEntry": lcUpsSwitchedReceptEntry,
       "lcUpsSwitchedReceptIndex": lcUpsSwitchedReceptIndex,
       "lcUpsSwitchedReceptOnDelay": lcUpsSwitchedReceptOnDelay,
       "lcUpsSwitchedReceptOnTrapDelay": lcUpsSwitchedReceptOnTrapDelay,
       "lcUpsSwitchedReceptOffDelay": lcUpsSwitchedReceptOffDelay,
       "lcUpsSwitchedReceptOffTrapDelay": lcUpsSwitchedReceptOffTrapDelay,
       "lcUpsSwitchedReceptStatus": lcUpsSwitchedReceptStatus,
       "lcUpsSwitchedReceptLabel": lcUpsSwitchedReceptLabel,
       "lcUpsBypass": lcUpsBypass,
       "lcUpsOnBypass": lcUpsOnBypass,
       "lcUpsBypassFrequency": lcUpsBypassFrequency,
       "lcUpsBypassNumLines": lcUpsBypassNumLines,
       "lcUpsBypassTable": lcUpsBypassTable,
       "lcUpsBypassEntry": lcUpsBypassEntry,
       "lcUpsBypassLine": lcUpsBypassLine,
       "lcUpsBypassVoltage": lcUpsBypassVoltage,
       "lcUpsBypassCurrent": lcUpsBypassCurrent,
       "lcUpsConfig": lcUpsConfig,
       "lcUpsConfigType": lcUpsConfigType,
       "lcUpsConfigBypassInstalled": lcUpsConfigBypassInstalled,
       "lcUpsConfigModuleCount": lcUpsConfigModuleCount,
       "lcUpsConfigCurrentModule": lcUpsConfigCurrentModule,
       "lcUpsConfigAudibleStatus": lcUpsConfigAudibleStatus,
       "lcUpsConfigLowBattTime": lcUpsConfigLowBattTime,
       "lcUpsConfigAutoRestart": lcUpsConfigAutoRestart,
       "luUPStationS": luUPStationS,
       "lsUpsIdent": lsUpsIdent,
       "lsUpsIdentFirmwareVersion": lsUpsIdentFirmwareVersion,
       "lsUpsAlarm": lsUpsAlarm,
       "lsUpsAlarmConditions": lsUpsAlarmConditions,
       "lsUpsAlarmCheckAirFilter": lsUpsAlarmCheckAirFilter,
       "lsUpsTraps": lsUpsTraps,
       "lsUpsCheckAirFilterTrap": lsUpsCheckAirFilterTrap,
       "lsUpsConfig": lsUpsConfig,
       "lsUpsConfigBypassInstalled": lsUpsConfigBypassInstalled,
       "lsUpsBypass": lsUpsBypass,
       "lsUpsOnBypass": lsUpsOnBypass,
       "lsUpsBypassFrequency": lsUpsBypassFrequency,
       "lsUpsBypassNumLines": lsUpsBypassNumLines,
       "lsUpsBypassTable": lsUpsBypassTable,
       "lsUpsBypassEntry": lsUpsBypassEntry,
       "lsUpsBypassLine": lsUpsBypassLine,
       "lsUpsBypassVoltage": lsUpsBypassVoltage,
       "lsUpsBypassCurrent": lsUpsBypassCurrent,
       "luUPStationD": luUPStationD,
       "ldUpsInput": ldUpsInput,
       "ldUpsInputMaxVoltsSinceLastPoll": ldUpsInputMaxVoltsSinceLastPoll,
       "ldUpsInputMinVoltsSinceLastPoll": ldUpsInputMinVoltsSinceLastPoll,
       "ldUpsOutput": ldUpsOutput,
       "ldUpsOutputMaxVoltsSinceLastPoll": ldUpsOutputMaxVoltsSinceLastPoll,
       "ldUpsOutputMinVoltsSinceLastPoll": ldUpsOutputMinVoltsSinceLastPoll,
       "ldUpsAlarm": ldUpsAlarm,
       "ldUpsAlarmConditions": ldUpsAlarmConditions,
       "ldUpsAlarmDCOverVoltageShutdown": ldUpsAlarmDCOverVoltageShutdown,
       "ldUpsAlarmOutputShortShutdown": ldUpsAlarmOutputShortShutdown,
       "ldUpsAlarmLNReversedShutdown": ldUpsAlarmLNReversedShutdown,
       "ldUpsAlarmImminentShutdown": ldUpsAlarmImminentShutdown,
       "ldUpsAlarmInputFreqError": ldUpsAlarmInputFreqError,
       "ldUpsAlarmBoostOn": ldUpsAlarmBoostOn,
       "ldUpsAlarmReplaceBattery": ldUpsAlarmReplaceBattery,
       "ldUpsAlarmOutputOverVoltage": ldUpsAlarmOutputOverVoltage,
       "ldUpsAlarmOutputUnderVoltage": ldUpsAlarmOutputUnderVoltage,
       "ldUpsAlarmChargerFailed": ldUpsAlarmChargerFailed,
       "ldUpsTraps": ldUpsTraps,
       "ldUpsDCOverVoltageShutdownTrap": ldUpsDCOverVoltageShutdownTrap,
       "ldUpsOutputShortShutdownTrap": ldUpsOutputShortShutdownTrap,
       "ldUpsLNReversedShutdownTrap": ldUpsLNReversedShutdownTrap,
       "ldUpsImminentShutdownTrap": ldUpsImminentShutdownTrap,
       "ldUpsInputFreqErrorTrap": ldUpsInputFreqErrorTrap,
       "ldUpsOutputOverVoltageTrap": ldUpsOutputOverVoltageTrap,
       "ldUpsOutputUnderVoltageTrap": ldUpsOutputUnderVoltageTrap,
       "ldUpsChargerFailedTrap": ldUpsChargerFailedTrap,
       "luUPStationG": luUPStationG,
       "lgUpsAlarm": lgUpsAlarm,
       "lgUpsAlarmConditions": lgUpsAlarmConditions,
       "lgUpsAlarmDCOverVoltageShutdown": lgUpsAlarmDCOverVoltageShutdown,
       "lgUpsAlarmOutputShortShutdown": lgUpsAlarmOutputShortShutdown,
       "lgUpsAlarmLNReversedShutdown": lgUpsAlarmLNReversedShutdown,
       "lgUpsAlarmRemoteShutdown": lgUpsAlarmRemoteShutdown,
       "lgUpsAlarmInputUVOnStartup": lgUpsAlarmInputUVOnStartup,
       "lgUpsAlarmPFCFailedOnStartup": lgUpsAlarmPFCFailedOnStartup,
       "lgUpsTraps": lgUpsTraps,
       "lgUpsDCOverVoltageShutdownTrap": lgUpsDCOverVoltageShutdownTrap,
       "lgUpsOutputShortShutdownTrap": lgUpsOutputShortShutdownTrap,
       "lgUpsLNReversedShutdownTrap": lgUpsLNReversedShutdownTrap,
       "lgUpsInputUVOnStartupTrap": lgUpsInputUVOnStartupTrap,
       "luSeries300": luSeries300,
       "luExternal": luExternal,
       "luUPStationS3": luUPStationS3,
       "luSeries200": luSeries200,
       "luSeries200Input": luSeries200Input,
       "luSeries200InputMaxVoltsSinceLastPoll": luSeries200InputMaxVoltsSinceLastPoll,
       "luSeries200InputMinVoltsSinceLastPoll": luSeries200InputMinVoltsSinceLastPoll,
       "luSeries200Alarm": luSeries200Alarm,
       "luSeries200AlarmConditions": luSeries200AlarmConditions,
       "luSeries200AlarmInputFreqError": luSeries200AlarmInputFreqError,
       "luSeries200Config": luSeries200Config,
       "luSeries200ConfigBypassInstalled": luSeries200ConfigBypassInstalled,
       "luSeries200ConfigFrequencyChangerModel": luSeries200ConfigFrequencyChangerModel,
       "luSeries200Bypass": luSeries200Bypass,
       "luSeries200OnBypass": luSeries200OnBypass,
       "luSeries4300": luSeries4300,
       "ls43cUpsIdent": ls43cUpsIdent,
       "ls43cUpsIdentFirmwareVersion": ls43cUpsIdentFirmwareVersion,
       "ls43cUpsConfig": ls43cUpsConfig,
       "ls43cUpsConfigBypassInstalled": ls43cUpsConfigBypassInstalled,
       "ls43cUpsBypass": ls43cUpsBypass,
       "ls43cUpsOnBypass": ls43cUpsOnBypass,
       "ls43cUpsBypassFrequency": ls43cUpsBypassFrequency,
       "ls43cUpsBypassNumLines": ls43cUpsBypassNumLines,
       "ls43cUpsBypassTable": ls43cUpsBypassTable,
       "ls43cUpsBypassEntry": ls43cUpsBypassEntry,
       "ls43cUpsBypassLine": ls43cUpsBypassLine,
       "ls43cUpsBypassVoltage": ls43cUpsBypassVoltage,
       "ls43cUpsBypassCurrent": ls43cUpsBypassCurrent,
       "luUpsModule": luUpsModule,
       "luSystemCabinet": luSystemCabinet,
       "luUPStationGxt": luUPStationGxt,
       "luPowerSure": luPowerSure,
       "luExperimental": luExperimental,
       "luPrivate": luPrivate}
)
