# SNMP MIB module (UPS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UPS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:37 2024
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

(ctUPS,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctUPS")

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

_UpsSystem_ObjectIdentity = ObjectIdentity
upsSystem = _UpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 1)
)


class _UpsNumUPSs_Type(Integer32):
    """Custom type upsNumUPSs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_UpsNumUPSs_Type.__name__ = "Integer32"
_UpsNumUPSs_Object = MibScalar
upsNumUPSs = _UpsNumUPSs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 1, 1),
    _UpsNumUPSs_Type()
)
upsNumUPSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsNumUPSs.setStatus("mandatory")
_UpsId_ObjectIdentity = ObjectIdentity
upsId = _UpsId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2)
)
_UpsIdTable_Object = MibTable
upsIdTable = _UpsIdTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    upsIdTable.setStatus("mandatory")
_UpsIdEntry_Object = MibTableRow
upsIdEntry = _UpsIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1)
)
upsIdEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsIdEntry.setStatus("mandatory")
_UpsIndex_Type = Integer32
_UpsIndex_Object = MibTableColumn
upsIndex = _UpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 1),
    _UpsIndex_Type()
)
upsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIndex.setStatus("mandatory")


class _UpsName_Type(DisplayString):
    """Custom type upsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UpsName_Type.__name__ = "DisplayString"
_UpsName_Object = MibTableColumn
upsName = _UpsName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 2),
    _UpsName_Type()
)
upsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsName.setStatus("mandatory")


class _UpsModelType_Type(Integer32):
    """Custom type upsModelType based on Integer32"""
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
        *(("matrixUps3000", 7),
          ("matrixUps5000", 8),
          ("other", 9),
          ("smartUps1250", 5),
          ("smartUps2000", 6),
          ("smartUps250", 1),
          ("smartUps400", 2),
          ("smartUps600", 3),
          ("smartUps900", 4))
    )


_UpsModelType_Type.__name__ = "Integer32"
_UpsModelType_Object = MibTableColumn
upsModelType = _UpsModelType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 3),
    _UpsModelType_Type()
)
upsModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsModelType.setStatus("mandatory")


class _UpsFwVersion_Type(DisplayString):
    """Custom type upsFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UpsFwVersion_Type.__name__ = "DisplayString"
_UpsFwVersion_Object = MibTableColumn
upsFwVersion = _UpsFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 4),
    _UpsFwVersion_Type()
)
upsFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsFwVersion.setStatus("mandatory")


class _UpsSerialNumber_Type(DisplayString):
    """Custom type upsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UpsSerialNumber_Type.__name__ = "DisplayString"
_UpsSerialNumber_Object = MibTableColumn
upsSerialNumber = _UpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 5),
    _UpsSerialNumber_Type()
)
upsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSerialNumber.setStatus("mandatory")


class _UpsManufDate_Type(DisplayString):
    """Custom type upsManufDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UpsManufDate_Type.__name__ = "DisplayString"
_UpsManufDate_Object = MibTableColumn
upsManufDate = _UpsManufDate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 6),
    _UpsManufDate_Type()
)
upsManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsManufDate.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3)
)
_UpsBatteryTable_Object = MibTable
upsBatteryTable = _UpsBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    upsBatteryTable.setStatus("mandatory")
_UpsBatteryEntry_Object = MibTableRow
upsBatteryEntry = _UpsBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1)
)
upsBatteryEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsBatteryEntry.setStatus("mandatory")
_UpsBatteryCapacity_Type = Integer32
_UpsBatteryCapacity_Object = MibTableColumn
upsBatteryCapacity = _UpsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 1),
    _UpsBatteryCapacity_Type()
)
upsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCapacity.setStatus("mandatory")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibTableColumn
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 2),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("mandatory")


class _UpsBatteryTest_Type(Integer32):
    """Custom type upsBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiateTest", 1)
    )


_UpsBatteryTest_Type.__name__ = "Integer32"
_UpsBatteryTest_Object = MibTableColumn
upsBatteryTest = _UpsBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 3),
    _UpsBatteryTest_Type()
)
upsBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTest.setStatus("mandatory")


class _UpsBatteryTestResult_Type(Integer32):
    """Custom type upsBatteryTestResult based on Integer32"""
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
        *(("batteryBad", 2),
          ("batteryOK", 1),
          ("invalidTestDueToOverload", 4),
          ("noRecentTest", 3))
    )


_UpsBatteryTestResult_Type.__name__ = "Integer32"
_UpsBatteryTestResult_Object = MibTableColumn
upsBatteryTestResult = _UpsBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 4),
    _UpsBatteryTestResult_Type()
)
upsBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTestResult.setStatus("mandatory")


class _UpsRunTimeCalibration_Type(Integer32):
    """Custom type upsRunTimeCalibration based on Integer32"""
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
        *(("abortTest", 2),
          ("performTest", 1),
          ("testInProgress", 3),
          ("testNotInProgress", 4))
    )


_UpsRunTimeCalibration_Type.__name__ = "Integer32"
_UpsRunTimeCalibration_Object = MibTableColumn
upsRunTimeCalibration = _UpsRunTimeCalibration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 5),
    _UpsRunTimeCalibration_Type()
)
upsRunTimeCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRunTimeCalibration.setStatus("mandatory")
_UpsEstimatedRunTimeRemaining_Type = Integer32
_UpsEstimatedRunTimeRemaining_Object = MibTableColumn
upsEstimatedRunTimeRemaining = _UpsEstimatedRunTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 6),
    _UpsEstimatedRunTimeRemaining_Type()
)
upsEstimatedRunTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedRunTimeRemaining.setStatus("mandatory")


class _UpsTransferCause_Type(Integer32):
    """Custom type upsTransferCause based on Integer32"""
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
        *(("inputHighVoltage", 5),
          ("inputLineFrequencyBad", 6),
          ("inputLineSpike", 3),
          ("inputLowVoltage", 4),
          ("noTransfer", 1),
          ("selfTest", 2))
    )


_UpsTransferCause_Type.__name__ = "Integer32"
_UpsTransferCause_Object = MibTableColumn
upsTransferCause = _UpsTransferCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 7),
    _UpsTransferCause_Type()
)
upsTransferCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTransferCause.setStatus("mandatory")


class _UpsBatteryTestTime_Type(Integer32):
    """Custom type upsBatteryTestTime based on Integer32"""
    defaultValue = 1

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
        *(("off", 4),
          ("oneWeek", 2),
          ("startupOnly", 3),
          ("twoWeeks", 1))
    )


_UpsBatteryTestTime_Type.__name__ = "Integer32"
_UpsBatteryTestTime_Object = MibTableColumn
upsBatteryTestTime = _UpsBatteryTestTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 8),
    _UpsBatteryTestTime_Type()
)
upsBatteryTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTestTime.setStatus("mandatory")


class _UpsLowBatteryWarning_Type(Integer32):
    """Custom type upsLowBatteryWarning based on Integer32"""
    defaultValue = 1

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
        *(("fiveMinutes", 2),
          ("sevenMinutes", 3),
          ("tenMinutes", 4),
          ("twoMinutes", 1))
    )


_UpsLowBatteryWarning_Type.__name__ = "Integer32"
_UpsLowBatteryWarning_Object = MibTableColumn
upsLowBatteryWarning = _UpsLowBatteryWarning_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 9),
    _UpsLowBatteryWarning_Type()
)
upsLowBatteryWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLowBatteryWarning.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4)
)
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("mandatory")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1)
)
upsInputEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("mandatory")


class _UpsInputUtilityVoltage_Type(Integer32):
    """Custom type upsInputUtilityVoltage based on Integer32"""
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
        *(("vac100", 1),
          ("vac120", 2),
          ("vac208", 3),
          ("vac220", 4))
    )


_UpsInputUtilityVoltage_Type.__name__ = "Integer32"
_UpsInputUtilityVoltage_Object = MibTableColumn
upsInputUtilityVoltage = _UpsInputUtilityVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 1),
    _UpsInputUtilityVoltage_Type()
)
upsInputUtilityVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputUtilityVoltage.setStatus("mandatory")
_UpsInputVoltage_Type = Integer32
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 2),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")


class _UpsInputFailureSensitivity_Type(Integer32):
    """Custom type upsInputFailureSensitivity based on Integer32"""
    defaultValue = 1

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
        *(("auto", 4),
          ("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_UpsInputFailureSensitivity_Type.__name__ = "Integer32"
_UpsInputFailureSensitivity_Object = MibTableColumn
upsInputFailureSensitivity = _UpsInputFailureSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 3),
    _UpsInputFailureSensitivity_Type()
)
upsInputFailureSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInputFailureSensitivity.setStatus("mandatory")
_UpsInputMaxVoltage_Type = Integer32
_UpsInputMaxVoltage_Object = MibTableColumn
upsInputMaxVoltage = _UpsInputMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 4),
    _UpsInputMaxVoltage_Type()
)
upsInputMaxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputMaxVoltage.setStatus("mandatory")
_UpsInputMinVoltage_Type = Integer32
_UpsInputMinVoltage_Object = MibTableColumn
upsInputMinVoltage = _UpsInputMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 5),
    _UpsInputMinVoltage_Type()
)
upsInputMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputMinVoltage.setStatus("mandatory")
_UpsInputFrequency_Type = Integer32
_UpsInputFrequency_Object = MibTableColumn
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 6),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5)
)
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("mandatory")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1)
)
upsOutputEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("mandatory")
_UpsOutputVoltage_Type = Integer32
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1, 1),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")


class _UpsOutputUtilityVoltage_Type(Integer32):
    """Custom type upsOutputUtilityVoltage based on Integer32"""
    defaultValue = 1

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
        *(("vac220", 4),
          ("vac225", 1),
          ("vac230", 2),
          ("vac240", 3))
    )


_UpsOutputUtilityVoltage_Type.__name__ = "Integer32"
_UpsOutputUtilityVoltage_Object = MibTableColumn
upsOutputUtilityVoltage = _UpsOutputUtilityVoltage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1, 2),
    _UpsOutputUtilityVoltage_Type()
)
upsOutputUtilityVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsOutputUtilityVoltage.setStatus("mandatory")
_UpsOutputPower_Type = Integer32
_UpsOutputPower_Object = MibTableColumn
upsOutputPower = _UpsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1, 3),
    _UpsOutputPower_Type()
)
upsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPower.setStatus("mandatory")
_UpsStatus_ObjectIdentity = ObjectIdentity
upsStatus = _UpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6)
)
_UpsStatusTable_Object = MibTable
upsStatusTable = _UpsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1)
)
if mibBuilder.loadTexts:
    upsStatusTable.setStatus("mandatory")
_UpsStatusEntry_Object = MibTableRow
upsStatusEntry = _UpsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1)
)
upsStatusEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsStatusEntry.setStatus("mandatory")
_UpsStatusOperational_Type = Integer32
_UpsStatusOperational_Object = MibTableColumn
upsStatusOperational = _UpsStatusOperational_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1, 1),
    _UpsStatusOperational_Type()
)
upsStatusOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusOperational.setStatus("mandatory")
_UpsStatusFault_Type = Integer32
_UpsStatusFault_Object = MibTableColumn
upsStatusFault = _UpsStatusFault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1, 2),
    _UpsStatusFault_Type()
)
upsStatusFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusFault.setStatus("mandatory")
_UpsStatusTemp_Type = Integer32
_UpsStatusTemp_Object = MibTableColumn
upsStatusTemp = _UpsStatusTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1, 3),
    _UpsStatusTemp_Type()
)
upsStatusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusTemp.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7)
)
_UpsConfigTable_Object = MibTable
upsConfigTable = _UpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1)
)
if mibBuilder.loadTexts:
    upsConfigTable.setStatus("mandatory")
_UpsConfigEntry_Object = MibTableRow
upsConfigEntry = _UpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1, 1)
)
upsConfigEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsConfigEntry.setStatus("mandatory")


class _UpsConfigAlarm_Type(Integer32):
    """Custom type upsConfigAlarm based on Integer32"""
    defaultValue = 1

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
        *(("lowBatteryOnly", 3),
          ("noAudibleAlarm", 4),
          ("thirtySecondsAfterUtilityFailure", 2),
          ("uponUtilityFailure", 1))
    )


_UpsConfigAlarm_Type.__name__ = "Integer32"
_UpsConfigAlarm_Object = MibTableColumn
upsConfigAlarm = _UpsConfigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1, 1, 1),
    _UpsConfigAlarm_Type()
)
upsConfigAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAlarm.setStatus("mandatory")


class _UpsConfigRestoreDefaults_Type(Integer32):
    """Custom type upsConfigRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restoreDefaults", 1)
    )


_UpsConfigRestoreDefaults_Type.__name__ = "Integer32"
_UpsConfigRestoreDefaults_Object = MibTableColumn
upsConfigRestoreDefaults = _UpsConfigRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1, 1, 2),
    _UpsConfigRestoreDefaults_Type()
)
upsConfigRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigRestoreDefaults.setStatus("mandatory")
_UpsExtMeas_ObjectIdentity = ObjectIdentity
upsExtMeas = _UpsExtMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8)
)
_UpsExtMeasTable_Object = MibTable
upsExtMeasTable = _UpsExtMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1)
)
if mibBuilder.loadTexts:
    upsExtMeasTable.setStatus("mandatory")
_UpsExtMeasEntry_Object = MibTableRow
upsExtMeasEntry = _UpsExtMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1)
)
upsExtMeasEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsExtMeasEntry.setStatus("mandatory")


class _UpsExtMeasFwVersion_Type(DisplayString):
    """Custom type upsExtMeasFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_UpsExtMeasFwVersion_Type.__name__ = "DisplayString"
_UpsExtMeasFwVersion_Object = MibTableColumn
upsExtMeasFwVersion = _UpsExtMeasFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 1),
    _UpsExtMeasFwVersion_Type()
)
upsExtMeasFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtMeasFwVersion.setStatus("mandatory")
_UpsExtMeasTemp_Type = Integer32
_UpsExtMeasTemp_Object = MibTableColumn
upsExtMeasTemp = _UpsExtMeasTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 2),
    _UpsExtMeasTemp_Type()
)
upsExtMeasTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtMeasTemp.setStatus("mandatory")
_UpsExtMeasHumidity_Type = Integer32
_UpsExtMeasHumidity_Object = MibTableColumn
upsExtMeasHumidity = _UpsExtMeasHumidity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 3),
    _UpsExtMeasHumidity_Type()
)
upsExtMeasHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtMeasHumidity.setStatus("mandatory")
_UpsExtMeasAlarmStatus_Type = Integer32
_UpsExtMeasAlarmStatus_Object = MibTableColumn
upsExtMeasAlarmStatus = _UpsExtMeasAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 4),
    _UpsExtMeasAlarmStatus_Type()
)
upsExtMeasAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtMeasAlarmStatus.setStatus("mandatory")


class _UpsExtMeasMaxTemp_Type(Integer32):
    """Custom type upsExtMeasMaxTemp based on Integer32"""
    defaultValue = 1

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
        *(("ninetyDegreesF", 1),
          ("oneHundredFifteenDegreesF", 2),
          ("oneHundredSeventyFiveDegreesF", 4),
          ("oneHundredThirtyDegreesF", 3))
    )


_UpsExtMeasMaxTemp_Type.__name__ = "Integer32"
_UpsExtMeasMaxTemp_Object = MibTableColumn
upsExtMeasMaxTemp = _UpsExtMeasMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 5),
    _UpsExtMeasMaxTemp_Type()
)
upsExtMeasMaxTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMaxTemp.setStatus("mandatory")


class _UpsExtMeasMinTemp_Type(Integer32):
    """Custom type upsExtMeasMinTemp based on Integer32"""
    defaultValue = 1

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
        *(("fiftyDegreesF", 2),
          ("fiftyEightDegreesF", 3),
          ("fortyDegreesF", 1),
          ("sixtyFiveDegreesF", 4))
    )


_UpsExtMeasMinTemp_Type.__name__ = "Integer32"
_UpsExtMeasMinTemp_Object = MibTableColumn
upsExtMeasMinTemp = _UpsExtMeasMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 6),
    _UpsExtMeasMinTemp_Type()
)
upsExtMeasMinTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMinTemp.setStatus("mandatory")


class _UpsExtMeasMaxHumidity_Type(Integer32):
    """Custom type upsExtMeasMaxHumidity based on Integer32"""
    defaultValue = 1

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
        *(("eightyFivePercent", 3),
          ("eightyPercent", 2),
          ("ninetyPercent", 4),
          ("seventyPercent", 1))
    )


_UpsExtMeasMaxHumidity_Type.__name__ = "Integer32"
_UpsExtMeasMaxHumidity_Object = MibTableColumn
upsExtMeasMaxHumidity = _UpsExtMeasMaxHumidity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 7),
    _UpsExtMeasMaxHumidity_Type()
)
upsExtMeasMaxHumidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMaxHumidity.setStatus("mandatory")


class _UpsExtMeasMinHumidity_Type(Integer32):
    """Custom type upsExtMeasMinHumidity based on Integer32"""
    defaultValue = 1

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
        *(("fortyPercent", 4),
          ("tenPercent", 1),
          ("thirtyPercent", 3),
          ("twentyPercent", 2))
    )


_UpsExtMeasMinHumidity_Type.__name__ = "Integer32"
_UpsExtMeasMinHumidity_Object = MibTableColumn
upsExtMeasMinHumidity = _UpsExtMeasMinHumidity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 8),
    _UpsExtMeasMinHumidity_Type()
)
upsExtMeasMinHumidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMinHumidity.setStatus("mandatory")


class _UpsExtMeasContact1AlarmControl_Type(Integer32):
    """Custom type upsExtMeasContact1AlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasContact1AlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasContact1AlarmControl_Object = MibTableColumn
upsExtMeasContact1AlarmControl = _UpsExtMeasContact1AlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 9),
    _UpsExtMeasContact1AlarmControl_Type()
)
upsExtMeasContact1AlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasContact1AlarmControl.setStatus("mandatory")


class _UpsExtMeasContact2AlarmControl_Type(Integer32):
    """Custom type upsExtMeasContact2AlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasContact2AlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasContact2AlarmControl_Object = MibTableColumn
upsExtMeasContact2AlarmControl = _UpsExtMeasContact2AlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 10),
    _UpsExtMeasContact2AlarmControl_Type()
)
upsExtMeasContact2AlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasContact2AlarmControl.setStatus("mandatory")


class _UpsExtMeasContact3AlarmControl_Type(Integer32):
    """Custom type upsExtMeasContact3AlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasContact3AlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasContact3AlarmControl_Object = MibTableColumn
upsExtMeasContact3AlarmControl = _UpsExtMeasContact3AlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 11),
    _UpsExtMeasContact3AlarmControl_Type()
)
upsExtMeasContact3AlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasContact3AlarmControl.setStatus("mandatory")


class _UpsExtMeasContact4AlarmControl_Type(Integer32):
    """Custom type upsExtMeasContact4AlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasContact4AlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasContact4AlarmControl_Object = MibTableColumn
upsExtMeasContact4AlarmControl = _UpsExtMeasContact4AlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 12),
    _UpsExtMeasContact4AlarmControl_Type()
)
upsExtMeasContact4AlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasContact4AlarmControl.setStatus("mandatory")


class _UpsExtMeasMaxTempAlarmControl_Type(Integer32):
    """Custom type upsExtMeasMaxTempAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasMaxTempAlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasMaxTempAlarmControl_Object = MibTableColumn
upsExtMeasMaxTempAlarmControl = _UpsExtMeasMaxTempAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 13),
    _UpsExtMeasMaxTempAlarmControl_Type()
)
upsExtMeasMaxTempAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMaxTempAlarmControl.setStatus("mandatory")


class _UpsExtMeasMinTempAlarmControl_Type(Integer32):
    """Custom type upsExtMeasMinTempAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasMinTempAlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasMinTempAlarmControl_Object = MibTableColumn
upsExtMeasMinTempAlarmControl = _UpsExtMeasMinTempAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 14),
    _UpsExtMeasMinTempAlarmControl_Type()
)
upsExtMeasMinTempAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMinTempAlarmControl.setStatus("mandatory")


class _UpsExtMeasMaxHumidityAlarmControl_Type(Integer32):
    """Custom type upsExtMeasMaxHumidityAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasMaxHumidityAlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasMaxHumidityAlarmControl_Object = MibTableColumn
upsExtMeasMaxHumidityAlarmControl = _UpsExtMeasMaxHumidityAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 15),
    _UpsExtMeasMaxHumidityAlarmControl_Type()
)
upsExtMeasMaxHumidityAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMaxHumidityAlarmControl.setStatus("mandatory")


class _UpsExtMeasMinHumidityAlarmControl_Type(Integer32):
    """Custom type upsExtMeasMinHumidityAlarmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsExtMeasMinHumidityAlarmControl_Type.__name__ = "Integer32"
_UpsExtMeasMinHumidityAlarmControl_Object = MibTableColumn
upsExtMeasMinHumidityAlarmControl = _UpsExtMeasMinHumidityAlarmControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 16),
    _UpsExtMeasMinHumidityAlarmControl_Type()
)
upsExtMeasMinHumidityAlarmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsExtMeasMinHumidityAlarmControl.setStatus("mandatory")
_UpsAddlFuncs_ObjectIdentity = ObjectIdentity
upsAddlFuncs = _UpsAddlFuncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9)
)
_UpsAddlFuncsTable_Object = MibTable
upsAddlFuncsTable = _UpsAddlFuncsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1)
)
if mibBuilder.loadTexts:
    upsAddlFuncsTable.setStatus("mandatory")
_UpsAddlFuncsEntry_Object = MibTableRow
upsAddlFuncsEntry = _UpsAddlFuncsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1)
)
upsAddlFuncsEntry.setIndexNames(
    (0, "UPS2-MIB", "upsIndex"),
)
if mibBuilder.loadTexts:
    upsAddlFuncsEntry.setStatus("mandatory")
_UpsAddlFuncsNumBatteryPacks_Type = Integer32
_UpsAddlFuncsNumBatteryPacks_Object = MibTableColumn
upsAddlFuncsNumBatteryPacks = _UpsAddlFuncsNumBatteryPacks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 1),
    _UpsAddlFuncsNumBatteryPacks_Type()
)
upsAddlFuncsNumBatteryPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAddlFuncsNumBatteryPacks.setStatus("mandatory")
_UpsAddlFuncsNumBadBatteryPacks_Type = Integer32
_UpsAddlFuncsNumBadBatteryPacks_Object = MibTableColumn
upsAddlFuncsNumBadBatteryPacks = _UpsAddlFuncsNumBadBatteryPacks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 2),
    _UpsAddlFuncsNumBadBatteryPacks_Type()
)
upsAddlFuncsNumBadBatteryPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAddlFuncsNumBadBatteryPacks.setStatus("mandatory")
_UpsAddlFuncsOutputCurrent_Type = Integer32
_UpsAddlFuncsOutputCurrent_Object = MibTableColumn
upsAddlFuncsOutputCurrent = _UpsAddlFuncsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 3),
    _UpsAddlFuncsOutputCurrent_Type()
)
upsAddlFuncsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAddlFuncsOutputCurrent.setStatus("mandatory")
_UpsAddlFuncsOutputApparentPower_Type = Integer32
_UpsAddlFuncsOutputApparentPower_Object = MibTableColumn
upsAddlFuncsOutputApparentPower = _UpsAddlFuncsOutputApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 4),
    _UpsAddlFuncsOutputApparentPower_Type()
)
upsAddlFuncsOutputApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAddlFuncsOutputApparentPower.setStatus("mandatory")
_UpsAddlFuncsStatusOperational_Type = Integer32
_UpsAddlFuncsStatusOperational_Object = MibTableColumn
upsAddlFuncsStatusOperational = _UpsAddlFuncsStatusOperational_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 5),
    _UpsAddlFuncsStatusOperational_Type()
)
upsAddlFuncsStatusOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAddlFuncsStatusOperational.setStatus("mandatory")
_UpsAddlFuncsStatusFault_Type = Integer32
_UpsAddlFuncsStatusFault_Object = MibTableColumn
upsAddlFuncsStatusFault = _UpsAddlFuncsStatusFault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 6),
    _UpsAddlFuncsStatusFault_Type()
)
upsAddlFuncsStatusFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAddlFuncsStatusFault.setStatus("mandatory")
_UpsAddlFuncsConfigPassword_Type = OctetString
_UpsAddlFuncsConfigPassword_Object = MibTableColumn
upsAddlFuncsConfigPassword = _UpsAddlFuncsConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 7),
    _UpsAddlFuncsConfigPassword_Type()
)
upsAddlFuncsConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAddlFuncsConfigPassword.setStatus("mandatory")


class _UpsAddlFuncsConfigDisable_Type(Integer32):
    """Custom type upsAddlFuncsConfigDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disableUps", 1)
    )


_UpsAddlFuncsConfigDisable_Type.__name__ = "Integer32"
_UpsAddlFuncsConfigDisable_Object = MibTableColumn
upsAddlFuncsConfigDisable = _UpsAddlFuncsConfigDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 8),
    _UpsAddlFuncsConfigDisable_Type()
)
upsAddlFuncsConfigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAddlFuncsConfigDisable.setStatus("mandatory")


class _UpsAddlFuncsConfigBypass_Type(Integer32):
    """Custom type upsAddlFuncsConfigBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassMode", 1),
          ("exitBypassMode", 2))
    )


_UpsAddlFuncsConfigBypass_Type.__name__ = "Integer32"
_UpsAddlFuncsConfigBypass_Object = MibTableColumn
upsAddlFuncsConfigBypass = _UpsAddlFuncsConfigBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 9),
    _UpsAddlFuncsConfigBypass_Type()
)
upsAddlFuncsConfigBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAddlFuncsConfigBypass.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UPS2-MIB",
    **{"upsSystem": upsSystem,
       "upsNumUPSs": upsNumUPSs,
       "upsId": upsId,
       "upsIdTable": upsIdTable,
       "upsIdEntry": upsIdEntry,
       "upsIndex": upsIndex,
       "upsName": upsName,
       "upsModelType": upsModelType,
       "upsFwVersion": upsFwVersion,
       "upsSerialNumber": upsSerialNumber,
       "upsManufDate": upsManufDate,
       "upsBattery": upsBattery,
       "upsBatteryTable": upsBatteryTable,
       "upsBatteryEntry": upsBatteryEntry,
       "upsBatteryCapacity": upsBatteryCapacity,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryTest": upsBatteryTest,
       "upsBatteryTestResult": upsBatteryTestResult,
       "upsRunTimeCalibration": upsRunTimeCalibration,
       "upsEstimatedRunTimeRemaining": upsEstimatedRunTimeRemaining,
       "upsTransferCause": upsTransferCause,
       "upsBatteryTestTime": upsBatteryTestTime,
       "upsLowBatteryWarning": upsLowBatteryWarning,
       "upsInput": upsInput,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputUtilityVoltage": upsInputUtilityVoltage,
       "upsInputVoltage": upsInputVoltage,
       "upsInputFailureSensitivity": upsInputFailureSensitivity,
       "upsInputMaxVoltage": upsInputMaxVoltage,
       "upsInputMinVoltage": upsInputMinVoltage,
       "upsInputFrequency": upsInputFrequency,
       "upsOutput": upsOutput,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputUtilityVoltage": upsOutputUtilityVoltage,
       "upsOutputPower": upsOutputPower,
       "upsStatus": upsStatus,
       "upsStatusTable": upsStatusTable,
       "upsStatusEntry": upsStatusEntry,
       "upsStatusOperational": upsStatusOperational,
       "upsStatusFault": upsStatusFault,
       "upsStatusTemp": upsStatusTemp,
       "upsConfig": upsConfig,
       "upsConfigTable": upsConfigTable,
       "upsConfigEntry": upsConfigEntry,
       "upsConfigAlarm": upsConfigAlarm,
       "upsConfigRestoreDefaults": upsConfigRestoreDefaults,
       "upsExtMeas": upsExtMeas,
       "upsExtMeasTable": upsExtMeasTable,
       "upsExtMeasEntry": upsExtMeasEntry,
       "upsExtMeasFwVersion": upsExtMeasFwVersion,
       "upsExtMeasTemp": upsExtMeasTemp,
       "upsExtMeasHumidity": upsExtMeasHumidity,
       "upsExtMeasAlarmStatus": upsExtMeasAlarmStatus,
       "upsExtMeasMaxTemp": upsExtMeasMaxTemp,
       "upsExtMeasMinTemp": upsExtMeasMinTemp,
       "upsExtMeasMaxHumidity": upsExtMeasMaxHumidity,
       "upsExtMeasMinHumidity": upsExtMeasMinHumidity,
       "upsExtMeasContact1AlarmControl": upsExtMeasContact1AlarmControl,
       "upsExtMeasContact2AlarmControl": upsExtMeasContact2AlarmControl,
       "upsExtMeasContact3AlarmControl": upsExtMeasContact3AlarmControl,
       "upsExtMeasContact4AlarmControl": upsExtMeasContact4AlarmControl,
       "upsExtMeasMaxTempAlarmControl": upsExtMeasMaxTempAlarmControl,
       "upsExtMeasMinTempAlarmControl": upsExtMeasMinTempAlarmControl,
       "upsExtMeasMaxHumidityAlarmControl": upsExtMeasMaxHumidityAlarmControl,
       "upsExtMeasMinHumidityAlarmControl": upsExtMeasMinHumidityAlarmControl,
       "upsAddlFuncs": upsAddlFuncs,
       "upsAddlFuncsTable": upsAddlFuncsTable,
       "upsAddlFuncsEntry": upsAddlFuncsEntry,
       "upsAddlFuncsNumBatteryPacks": upsAddlFuncsNumBatteryPacks,
       "upsAddlFuncsNumBadBatteryPacks": upsAddlFuncsNumBadBatteryPacks,
       "upsAddlFuncsOutputCurrent": upsAddlFuncsOutputCurrent,
       "upsAddlFuncsOutputApparentPower": upsAddlFuncsOutputApparentPower,
       "upsAddlFuncsStatusOperational": upsAddlFuncsStatusOperational,
       "upsAddlFuncsStatusFault": upsAddlFuncsStatusFault,
       "upsAddlFuncsConfigPassword": upsAddlFuncsConfigPassword,
       "upsAddlFuncsConfigDisable": upsAddlFuncsConfigDisable,
       "upsAddlFuncsConfigBypass": upsAddlFuncsConfigBypass}
)
