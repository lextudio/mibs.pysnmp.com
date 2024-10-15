# SNMP MIB module (G6-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G6-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:32 2024
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
device.setRevisions(
        ("2015-05-22 10:59",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31)
)
_HardwareLedTest_Type = DisplayString
_HardwareLedTest_Object = MibScalar
hardwareLedTest = _HardwareLedTest_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 1),
    _HardwareLedTest_Type()
)
hardwareLedTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hardwareLedTest.setStatus("current")


class _HardwareLedMode_Type(Integer32):
    """Custom type hardwareLedMode based on Integer32"""
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
        *(("dark", 3),
          ("dynamic", 0),
          ("lightshow", 4),
          ("quiet", 2),
          ("static", 1))
    )


_HardwareLedMode_Type.__name__ = "Integer32"
_HardwareLedMode_Object = MibScalar
hardwareLedMode = _HardwareLedMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 2),
    _HardwareLedMode_Type()
)
hardwareLedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hardwareLedMode.setStatus("current")


class _HardwarePowerSupply1Monitored_Type(Integer32):
    """Custom type hardwarePowerSupply1Monitored based on Integer32"""
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


_HardwarePowerSupply1Monitored_Type.__name__ = "Integer32"
_HardwarePowerSupply1Monitored_Object = MibScalar
hardwarePowerSupply1Monitored = _HardwarePowerSupply1Monitored_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 3),
    _HardwarePowerSupply1Monitored_Type()
)
hardwarePowerSupply1Monitored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hardwarePowerSupply1Monitored.setStatus("current")


class _HardwarePowerSupply2Monitored_Type(Integer32):
    """Custom type hardwarePowerSupply2Monitored based on Integer32"""
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


_HardwarePowerSupply2Monitored_Type.__name__ = "Integer32"
_HardwarePowerSupply2Monitored_Object = MibScalar
hardwarePowerSupply2Monitored = _HardwarePowerSupply2Monitored_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 4),
    _HardwarePowerSupply2Monitored_Type()
)
hardwarePowerSupply2Monitored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hardwarePowerSupply2Monitored.setStatus("current")


class _HardwareFactoryResetButton_Type(Integer32):
    """Custom type hardwareFactoryResetButton based on Integer32"""
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


_HardwareFactoryResetButton_Type.__name__ = "Integer32"
_HardwareFactoryResetButton_Object = MibScalar
hardwareFactoryResetButton = _HardwareFactoryResetButton_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 5),
    _HardwareFactoryResetButton_Type()
)
hardwareFactoryResetButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hardwareFactoryResetButton.setStatus("current")
_CableTestConfigTable_Object = MibTable
cableTestConfigTable = _CableTestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 6)
)
if mibBuilder.loadTexts:
    cableTestConfigTable.setStatus("current")
_CableTestConfigEntry_Object = MibTableRow
cableTestConfigEntry = _CableTestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 6, 1)
)
cableTestConfigEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "cableTestConfigPortIndex"),
)
if mibBuilder.loadTexts:
    cableTestConfigEntry.setStatus("current")


class _CableTestConfigPortIndex_Type(Integer32):
    """Custom type cableTestConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CableTestConfigPortIndex_Type.__name__ = "Integer32"
_CableTestConfigPortIndex_Object = MibTableColumn
cableTestConfigPortIndex = _CableTestConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 6, 1, 1),
    _CableTestConfigPortIndex_Type()
)
cableTestConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableTestConfigPortIndex.setStatus("current")


class _CableTestConfigEnableAutoCableTest_Type(Integer32):
    """Custom type cableTestConfigEnableAutoCableTest based on Integer32"""
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


_CableTestConfigEnableAutoCableTest_Type.__name__ = "Integer32"
_CableTestConfigEnableAutoCableTest_Object = MibTableColumn
cableTestConfigEnableAutoCableTest = _CableTestConfigEnableAutoCableTest_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 6, 1, 2),
    _CableTestConfigEnableAutoCableTest_Type()
)
cableTestConfigEnableAutoCableTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableTestConfigEnableAutoCableTest.setStatus("current")


class _CableTestConfigEventGeneration_Type(Integer32):
    """Custom type cableTestConfigEventGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anyChange", 1),
          ("cableUnplugged", 2),
          ("disabled", 0))
    )


_CableTestConfigEventGeneration_Type.__name__ = "Integer32"
_CableTestConfigEventGeneration_Object = MibTableColumn
cableTestConfigEventGeneration = _CableTestConfigEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 6, 1, 3),
    _CableTestConfigEventGeneration_Type()
)
cableTestConfigEventGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableTestConfigEventGeneration.setStatus("current")
_CableTestConfigStartTestNow_Type = DisplayString
_CableTestConfigStartTestNow_Object = MibTableColumn
cableTestConfigStartTestNow = _CableTestConfigStartTestNow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 6, 1, 4),
    _CableTestConfigStartTestNow_Type()
)
cableTestConfigStartTestNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableTestConfigStartTestNow.setStatus("current")
_IoSignalConfigTable_Object = MibTable
ioSignalConfigTable = _IoSignalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7)
)
if mibBuilder.loadTexts:
    ioSignalConfigTable.setStatus("current")
_IoSignalConfigEntry_Object = MibTableRow
ioSignalConfigEntry = _IoSignalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1)
)
ioSignalConfigEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "ioSignalConfigIndex"),
)
if mibBuilder.loadTexts:
    ioSignalConfigEntry.setStatus("current")


class _IoSignalConfigIndex_Type(Integer32):
    """Custom type ioSignalConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_IoSignalConfigIndex_Type.__name__ = "Integer32"
_IoSignalConfigIndex_Object = MibTableColumn
ioSignalConfigIndex = _IoSignalConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 1),
    _IoSignalConfigIndex_Type()
)
ioSignalConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ioSignalConfigIndex.setStatus("current")


class _IoSignalConfigSignalMode_Type(Integer32):
    """Custom type ioSignalConfigSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ledBlink", 1),
          ("relayBlink", 2),
          ("static", 0))
    )


_IoSignalConfigSignalMode_Type.__name__ = "Integer32"
_IoSignalConfigSignalMode_Object = MibTableColumn
ioSignalConfigSignalMode = _IoSignalConfigSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 2),
    _IoSignalConfigSignalMode_Type()
)
ioSignalConfigSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigSignalMode.setStatus("current")


class _IoSignalConfigInput1Mode_Type(Integer32):
    """Custom type ioSignalConfigInput1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmWhenHigh", 1),
          ("alarmWhenLow", 2),
          ("disabled", 0))
    )


_IoSignalConfigInput1Mode_Type.__name__ = "Integer32"
_IoSignalConfigInput1Mode_Object = MibTableColumn
ioSignalConfigInput1Mode = _IoSignalConfigInput1Mode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 3),
    _IoSignalConfigInput1Mode_Type()
)
ioSignalConfigInput1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigInput1Mode.setStatus("current")
_IoSignalConfigInput1Name_Type = DisplayString
_IoSignalConfigInput1Name_Object = MibTableColumn
ioSignalConfigInput1Name = _IoSignalConfigInput1Name_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 4),
    _IoSignalConfigInput1Name_Type()
)
ioSignalConfigInput1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigInput1Name.setStatus("current")


class _IoSignalConfigInput2Mode_Type(Integer32):
    """Custom type ioSignalConfigInput2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmWhenHigh", 1),
          ("alarmWhenLow", 2),
          ("disabled", 0))
    )


_IoSignalConfigInput2Mode_Type.__name__ = "Integer32"
_IoSignalConfigInput2Mode_Object = MibTableColumn
ioSignalConfigInput2Mode = _IoSignalConfigInput2Mode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 5),
    _IoSignalConfigInput2Mode_Type()
)
ioSignalConfigInput2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigInput2Mode.setStatus("current")
_IoSignalConfigInput2Name_Type = DisplayString
_IoSignalConfigInput2Name_Object = MibTableColumn
ioSignalConfigInput2Name = _IoSignalConfigInput2Name_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 6),
    _IoSignalConfigInput2Name_Type()
)
ioSignalConfigInput2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigInput2Name.setStatus("current")


class _IoSignalConfigOutput1Trigger_Type(Integer32):
    """Custom type ioSignalConfigOutput1Trigger based on Integer32"""
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
        *(("disabled", 0),
          ("highTemp", 3),
          ("off", 4),
          ("on", 5),
          ("redundancyFail", 2),
          ("whileRunning", 1))
    )


_IoSignalConfigOutput1Trigger_Type.__name__ = "Integer32"
_IoSignalConfigOutput1Trigger_Object = MibTableColumn
ioSignalConfigOutput1Trigger = _IoSignalConfigOutput1Trigger_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 7),
    _IoSignalConfigOutput1Trigger_Type()
)
ioSignalConfigOutput1Trigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigOutput1Trigger.setStatus("current")
_IoSignalConfigOutput1Name_Type = DisplayString
_IoSignalConfigOutput1Name_Object = MibTableColumn
ioSignalConfigOutput1Name = _IoSignalConfigOutput1Name_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 8),
    _IoSignalConfigOutput1Name_Type()
)
ioSignalConfigOutput1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigOutput1Name.setStatus("current")


class _IoSignalConfigOutput2Trigger_Type(Integer32):
    """Custom type ioSignalConfigOutput2Trigger based on Integer32"""
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
        *(("disabled", 0),
          ("highTemp", 3),
          ("off", 4),
          ("on", 5),
          ("redundancyFail", 2),
          ("whileRunning", 1))
    )


_IoSignalConfigOutput2Trigger_Type.__name__ = "Integer32"
_IoSignalConfigOutput2Trigger_Object = MibTableColumn
ioSignalConfigOutput2Trigger = _IoSignalConfigOutput2Trigger_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 9),
    _IoSignalConfigOutput2Trigger_Type()
)
ioSignalConfigOutput2Trigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigOutput2Trigger.setStatus("current")
_IoSignalConfigOutput2Name_Type = DisplayString
_IoSignalConfigOutput2Name_Object = MibTableColumn
ioSignalConfigOutput2Name = _IoSignalConfigOutput2Name_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 7, 1, 10),
    _IoSignalConfigOutput2Name_Type()
)
ioSignalConfigOutput2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioSignalConfigOutput2Name.setStatus("current")


class _HardwarePowerSupply1Status_Type(Integer32):
    """Custom type hardwarePowerSupply1Status based on Integer32"""
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
        *(("fuseFail", 3),
          ("inputLow", 2),
          ("notApplicable", 4),
          ("notInstalled", 6),
          ("ok", 0),
          ("overload", 1),
          ("unmanaged", 5))
    )


_HardwarePowerSupply1Status_Type.__name__ = "Integer32"
_HardwarePowerSupply1Status_Object = MibScalar
hardwarePowerSupply1Status = _HardwarePowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 100),
    _HardwarePowerSupply1Status_Type()
)
hardwarePowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePowerSupply1Status.setStatus("current")


class _HardwarePowerSupply2Status_Type(Integer32):
    """Custom type hardwarePowerSupply2Status based on Integer32"""
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
        *(("fuseFail", 3),
          ("inputLow", 2),
          ("notApplicable", 4),
          ("notInstalled", 6),
          ("ok", 0),
          ("overload", 1),
          ("unmanaged", 5))
    )


_HardwarePowerSupply2Status_Type.__name__ = "Integer32"
_HardwarePowerSupply2Status_Object = MibScalar
hardwarePowerSupply2Status = _HardwarePowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 101),
    _HardwarePowerSupply2Status_Type()
)
hardwarePowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePowerSupply2Status.setStatus("current")


class _HardwareRunningOnPoe_Type(Integer32):
    """Custom type hardwareRunningOnPoe based on Integer32"""
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


_HardwareRunningOnPoe_Type.__name__ = "Integer32"
_HardwareRunningOnPoe_Object = MibScalar
hardwareRunningOnPoe = _HardwareRunningOnPoe_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 102),
    _HardwareRunningOnPoe_Type()
)
hardwareRunningOnPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRunningOnPoe.setStatus("current")


class _HardwareFanStatus_Type(Integer32):
    """Custom type hardwareFanStatus based on Integer32"""
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
        *(("degraded", 2),
          ("fail", 3),
          ("missing", 4),
          ("ok", 1),
          ("unused", 0))
    )


_HardwareFanStatus_Type.__name__ = "Integer32"
_HardwareFanStatus_Object = MibScalar
hardwareFanStatus = _HardwareFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 103),
    _HardwareFanStatus_Type()
)
hardwareFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareFanStatus.setStatus("current")


class _HardwareSdCardStatus_Type(Integer32):
    """Custom type hardwareSdCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("inserted", 1),
          ("writeProtected", 2),
          ("writing", 3))
    )


_HardwareSdCardStatus_Type.__name__ = "Integer32"
_HardwareSdCardStatus_Object = MibScalar
hardwareSdCardStatus = _HardwareSdCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 104),
    _HardwareSdCardStatus_Type()
)
hardwareSdCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareSdCardStatus.setStatus("current")


class _HardwareNumOfPorts_Type(Integer32):
    """Custom type hardwareNumOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HardwareNumOfPorts_Type.__name__ = "Integer32"
_HardwareNumOfPorts_Object = MibScalar
hardwareNumOfPorts = _HardwareNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 105),
    _HardwareNumOfPorts_Type()
)
hardwareNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareNumOfPorts.setStatus("current")
_HardwareMaskOfExistingPorts_Type = Integer32
_HardwareMaskOfExistingPorts_Object = MibScalar
hardwareMaskOfExistingPorts = _HardwareMaskOfExistingPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 106),
    _HardwareMaskOfExistingPorts_Type()
)
hardwareMaskOfExistingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMaskOfExistingPorts.setStatus("current")
_HardwareMaskOfSfpPorts_Type = Integer32
_HardwareMaskOfSfpPorts_Object = MibScalar
hardwareMaskOfSfpPorts = _HardwareMaskOfSfpPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 107),
    _HardwareMaskOfSfpPorts_Type()
)
hardwareMaskOfSfpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMaskOfSfpPorts.setStatus("current")
_HardwareMaskOfPoePorts_Type = Integer32
_HardwareMaskOfPoePorts_Object = MibScalar
hardwareMaskOfPoePorts = _HardwareMaskOfPoePorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 108),
    _HardwareMaskOfPoePorts_Type()
)
hardwareMaskOfPoePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareMaskOfPoePorts.setStatus("current")
_ModuleInfoTable_Object = MibTable
moduleInfoTable = _ModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109)
)
if mibBuilder.loadTexts:
    moduleInfoTable.setStatus("current")
_ModuleInfoEntry_Object = MibTableRow
moduleInfoEntry = _ModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1)
)
moduleInfoEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "moduleInfoIndex"),
)
if mibBuilder.loadTexts:
    moduleInfoEntry.setStatus("current")


class _ModuleInfoIndex_Type(Integer32):
    """Custom type moduleInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ModuleInfoIndex_Type.__name__ = "Integer32"
_ModuleInfoIndex_Object = MibTableColumn
moduleInfoIndex = _ModuleInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 1),
    _ModuleInfoIndex_Type()
)
moduleInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleInfoIndex.setStatus("current")


class _ModuleInfoUnitType_Type(Integer32):
    """Custom type moduleInfoUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("baseUnit", 1),
          ("extension", 2),
          ("notPresent", 0))
    )


_ModuleInfoUnitType_Type.__name__ = "Integer32"
_ModuleInfoUnitType_Object = MibTableColumn
moduleInfoUnitType = _ModuleInfoUnitType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 2),
    _ModuleInfoUnitType_Type()
)
moduleInfoUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoUnitType.setStatus("current")
_ModuleInfoArticleNumber_Type = DisplayString
_ModuleInfoArticleNumber_Object = MibTableColumn
moduleInfoArticleNumber = _ModuleInfoArticleNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 3),
    _ModuleInfoArticleNumber_Type()
)
moduleInfoArticleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoArticleNumber.setStatus("current")
_ModuleInfoSerialNumber_Type = DisplayString
_ModuleInfoSerialNumber_Object = MibTableColumn
moduleInfoSerialNumber = _ModuleInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 4),
    _ModuleInfoSerialNumber_Type()
)
moduleInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoSerialNumber.setStatus("current")
_ModuleInfoHardwareVersion_Type = DisplayString
_ModuleInfoHardwareVersion_Object = MibTableColumn
moduleInfoHardwareVersion = _ModuleInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 5),
    _ModuleInfoHardwareVersion_Type()
)
moduleInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoHardwareVersion.setStatus("current")
_ModuleInfoProjectNumber_Type = DisplayString
_ModuleInfoProjectNumber_Object = MibTableColumn
moduleInfoProjectNumber = _ModuleInfoProjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 6),
    _ModuleInfoProjectNumber_Type()
)
moduleInfoProjectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoProjectNumber.setStatus("current")
_ModuleInfoOccupiedSlots_Type = DisplayString
_ModuleInfoOccupiedSlots_Object = MibTableColumn
moduleInfoOccupiedSlots = _ModuleInfoOccupiedSlots_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 7),
    _ModuleInfoOccupiedSlots_Type()
)
moduleInfoOccupiedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoOccupiedSlots.setStatus("current")
_ModuleInfoDescription_Type = DisplayString
_ModuleInfoDescription_Object = MibTableColumn
moduleInfoDescription = _ModuleInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 109, 1, 8),
    _ModuleInfoDescription_Type()
)
moduleInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInfoDescription.setStatus("current")
_SlotInfoTable_Object = MibTable
slotInfoTable = _SlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 110)
)
if mibBuilder.loadTexts:
    slotInfoTable.setStatus("current")
_SlotInfoEntry_Object = MibTableRow
slotInfoEntry = _SlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 110, 1)
)
slotInfoEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "slotInfoIndex"),
)
if mibBuilder.loadTexts:
    slotInfoEntry.setStatus("current")


class _SlotInfoIndex_Type(Integer32):
    """Custom type slotInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SlotInfoIndex_Type.__name__ = "Integer32"
_SlotInfoIndex_Object = MibTableColumn
slotInfoIndex = _SlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 110, 1, 1),
    _SlotInfoIndex_Type()
)
slotInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotInfoIndex.setStatus("current")


class _SlotInfoBoardType_Type(Integer32):
    """Custom type slotInfoBoardType based on Integer32"""
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
        *(("cpu", 3),
          ("io", 5),
          ("notPresent", 0),
          ("port", 4),
          ("power", 2),
          ("undefined", 1))
    )


_SlotInfoBoardType_Type.__name__ = "Integer32"
_SlotInfoBoardType_Object = MibTableColumn
slotInfoBoardType = _SlotInfoBoardType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 110, 1, 2),
    _SlotInfoBoardType_Type()
)
slotInfoBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInfoBoardType.setStatus("current")
_SlotInfoBoardId_Type = Unsigned32
_SlotInfoBoardId_Object = MibTableColumn
slotInfoBoardId = _SlotInfoBoardId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 110, 1, 3),
    _SlotInfoBoardId_Type()
)
slotInfoBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInfoBoardId.setStatus("current")


class _SlotInfoVersionBits_Type(Integer32):
    """Custom type slotInfoVersionBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlotInfoVersionBits_Type.__name__ = "Integer32"
_SlotInfoVersionBits_Object = MibTableColumn
slotInfoVersionBits = _SlotInfoVersionBits_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 110, 1, 4),
    _SlotInfoVersionBits_Type()
)
slotInfoVersionBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInfoVersionBits.setStatus("current")
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("current")
_PortInfoEntry_Object = MibTableRow
portInfoEntry = _PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1)
)
portInfoEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "portInfoPortIndex"),
)
if mibBuilder.loadTexts:
    portInfoEntry.setStatus("current")


class _PortInfoPortIndex_Type(Integer32):
    """Custom type portInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortInfoPortIndex_Type.__name__ = "Integer32"
_PortInfoPortIndex_Object = MibTableColumn
portInfoPortIndex = _PortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 1),
    _PortInfoPortIndex_Type()
)
portInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portInfoPortIndex.setStatus("current")


class _PortInfoSystemSlot_Type(Integer32):
    """Custom type portInfoSystemSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoSystemSlot_Type.__name__ = "Integer32"
_PortInfoSystemSlot_Object = MibTableColumn
portInfoSystemSlot = _PortInfoSystemSlot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 2),
    _PortInfoSystemSlot_Type()
)
portInfoSystemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSystemSlot.setStatus("current")


class _PortInfoSwitchPort_Type(Integer32):
    """Custom type portInfoSwitchPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoSwitchPort_Type.__name__ = "Integer32"
_PortInfoSwitchPort_Object = MibTableColumn
portInfoSwitchPort = _PortInfoSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 3),
    _PortInfoSwitchPort_Type()
)
portInfoSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSwitchPort.setStatus("current")


class _PortInfoUserSlot_Type(Integer32):
    """Custom type portInfoUserSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoUserSlot_Type.__name__ = "Integer32"
_PortInfoUserSlot_Object = MibTableColumn
portInfoUserSlot = _PortInfoUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 4),
    _PortInfoUserSlot_Type()
)
portInfoUserSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoUserSlot.setStatus("current")


class _PortInfoUserPort_Type(Integer32):
    """Custom type portInfoUserPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoUserPort_Type.__name__ = "Integer32"
_PortInfoUserPort_Object = MibTableColumn
portInfoUserPort = _PortInfoUserPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 5),
    _PortInfoUserPort_Type()
)
portInfoUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoUserPort.setStatus("current")


class _PortInfoSnmpPort_Type(Integer32):
    """Custom type portInfoSnmpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortInfoSnmpPort_Type.__name__ = "Integer32"
_PortInfoSnmpPort_Object = MibTableColumn
portInfoSnmpPort = _PortInfoSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 6),
    _PortInfoSnmpPort_Type()
)
portInfoSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSnmpPort.setStatus("current")


class _PortInfoSnmpInstance_Type(Integer32):
    """Custom type portInfoSnmpInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoSnmpInstance_Type.__name__ = "Integer32"
_PortInfoSnmpInstance_Object = MibTableColumn
portInfoSnmpInstance = _PortInfoSnmpInstance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 7),
    _PortInfoSnmpInstance_Type()
)
portInfoSnmpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSnmpInstance.setStatus("current")


class _PortInfoHardwarePort_Type(Integer32):
    """Custom type portInfoHardwarePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoHardwarePort_Type.__name__ = "Integer32"
_PortInfoHardwarePort_Object = MibTableColumn
portInfoHardwarePort = _PortInfoHardwarePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 8),
    _PortInfoHardwarePort_Type()
)
portInfoHardwarePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoHardwarePort.setStatus("current")


class _PortInfoInterfaceType_Type(Integer32):
    """Custom type portInfoInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 0),
          ("dualMedia", 2),
          ("optical", 1))
    )


_PortInfoInterfaceType_Type.__name__ = "Integer32"
_PortInfoInterfaceType_Object = MibTableColumn
portInfoInterfaceType = _PortInfoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 9),
    _PortInfoInterfaceType_Type()
)
portInfoInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoInterfaceType.setStatus("current")


class _PortInfoProperties_Type(Bits):
    """Custom type portInfoProperties based on Bits"""
    namedValues = NamedValues(
        *(("csfp", 12),
          ("dualMedia", 10),
          ("internal", 0),
          ("linkPort", 11),
          ("ms1000Mb", 3),
          ("ms100Mb", 2),
          ("ms10Mb", 1),
          ("ms1x9", 6),
          ("pd", 9),
          ("poe", 7),
          ("poePlus", 8),
          ("rj45", 4),
          ("sfp", 5))
    )

_PortInfoProperties_Type.__name__ = "Bits"
_PortInfoProperties_Object = MibTableColumn
portInfoProperties = _PortInfoProperties_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 111, 1, 10),
    _PortInfoProperties_Type()
)
portInfoProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoProperties.setStatus("current")
_PortLedsTable_Object = MibTable
portLedsTable = _PortLedsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112)
)
if mibBuilder.loadTexts:
    portLedsTable.setStatus("current")
_PortLedsEntry_Object = MibTableRow
portLedsEntry = _PortLedsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112, 1)
)
portLedsEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "portLedsPortIndex"),
)
if mibBuilder.loadTexts:
    portLedsEntry.setStatus("current")


class _PortLedsPortIndex_Type(Integer32):
    """Custom type portLedsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PortLedsPortIndex_Type.__name__ = "Integer32"
_PortLedsPortIndex_Object = MibTableColumn
portLedsPortIndex = _PortLedsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112, 1, 1),
    _PortLedsPortIndex_Type()
)
portLedsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portLedsPortIndex.setStatus("current")


class _PortLedsEthernetColor_Type(Integer32):
    """Custom type portLedsEthernetColor based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_PortLedsEthernetColor_Type.__name__ = "Integer32"
_PortLedsEthernetColor_Object = MibTableColumn
portLedsEthernetColor = _PortLedsEthernetColor_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112, 1, 2),
    _PortLedsEthernetColor_Type()
)
portLedsEthernetColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLedsEthernetColor.setStatus("current")


class _PortLedsEthernetBlinking_Type(Integer32):
    """Custom type portLedsEthernetBlinking based on Integer32"""
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


_PortLedsEthernetBlinking_Type.__name__ = "Integer32"
_PortLedsEthernetBlinking_Object = MibTableColumn
portLedsEthernetBlinking = _PortLedsEthernetBlinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112, 1, 3),
    _PortLedsEthernetBlinking_Type()
)
portLedsEthernetBlinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLedsEthernetBlinking.setStatus("current")


class _PortLedsPoeColor_Type(Integer32):
    """Custom type portLedsPoeColor based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_PortLedsPoeColor_Type.__name__ = "Integer32"
_PortLedsPoeColor_Object = MibTableColumn
portLedsPoeColor = _PortLedsPoeColor_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112, 1, 4),
    _PortLedsPoeColor_Type()
)
portLedsPoeColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLedsPoeColor.setStatus("current")


class _PortLedsPoeBlinking_Type(Integer32):
    """Custom type portLedsPoeBlinking based on Integer32"""
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


_PortLedsPoeBlinking_Type.__name__ = "Integer32"
_PortLedsPoeBlinking_Object = MibTableColumn
portLedsPoeBlinking = _PortLedsPoeBlinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 112, 1, 5),
    _PortLedsPoeBlinking_Type()
)
portLedsPoeBlinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLedsPoeBlinking.setStatus("current")
_DeviceLedsTable_Object = MibTable
deviceLedsTable = _DeviceLedsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113)
)
if mibBuilder.loadTexts:
    deviceLedsTable.setStatus("current")
_DeviceLedsEntry_Object = MibTableRow
deviceLedsEntry = _DeviceLedsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1)
)
deviceLedsEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "deviceLedsIndex"),
)
if mibBuilder.loadTexts:
    deviceLedsEntry.setStatus("current")


class _DeviceLedsIndex_Type(Integer32):
    """Custom type deviceLedsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_DeviceLedsIndex_Type.__name__ = "Integer32"
_DeviceLedsIndex_Object = MibTableColumn
deviceLedsIndex = _DeviceLedsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 1),
    _DeviceLedsIndex_Type()
)
deviceLedsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceLedsIndex.setStatus("current")


class _DeviceLedsSystem1Color_Type(Integer32):
    """Custom type deviceLedsSystem1Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsSystem1Color_Type.__name__ = "Integer32"
_DeviceLedsSystem1Color_Object = MibTableColumn
deviceLedsSystem1Color = _DeviceLedsSystem1Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 2),
    _DeviceLedsSystem1Color_Type()
)
deviceLedsSystem1Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSystem1Color.setStatus("current")


class _DeviceLedsSystem1Blinking_Type(Integer32):
    """Custom type deviceLedsSystem1Blinking based on Integer32"""
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


_DeviceLedsSystem1Blinking_Type.__name__ = "Integer32"
_DeviceLedsSystem1Blinking_Object = MibTableColumn
deviceLedsSystem1Blinking = _DeviceLedsSystem1Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 3),
    _DeviceLedsSystem1Blinking_Type()
)
deviceLedsSystem1Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSystem1Blinking.setStatus("current")


class _DeviceLedsSystem2Color_Type(Integer32):
    """Custom type deviceLedsSystem2Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsSystem2Color_Type.__name__ = "Integer32"
_DeviceLedsSystem2Color_Object = MibTableColumn
deviceLedsSystem2Color = _DeviceLedsSystem2Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 4),
    _DeviceLedsSystem2Color_Type()
)
deviceLedsSystem2Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSystem2Color.setStatus("current")


class _DeviceLedsSystem2Blinking_Type(Integer32):
    """Custom type deviceLedsSystem2Blinking based on Integer32"""
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


_DeviceLedsSystem2Blinking_Type.__name__ = "Integer32"
_DeviceLedsSystem2Blinking_Object = MibTableColumn
deviceLedsSystem2Blinking = _DeviceLedsSystem2Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 5),
    _DeviceLedsSystem2Blinking_Type()
)
deviceLedsSystem2Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSystem2Blinking.setStatus("current")


class _DeviceLedsPowerOn1Color_Type(Integer32):
    """Custom type deviceLedsPowerOn1Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsPowerOn1Color_Type.__name__ = "Integer32"
_DeviceLedsPowerOn1Color_Object = MibTableColumn
deviceLedsPowerOn1Color = _DeviceLedsPowerOn1Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 6),
    _DeviceLedsPowerOn1Color_Type()
)
deviceLedsPowerOn1Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsPowerOn1Color.setStatus("current")


class _DeviceLedsPowerOn1Blinking_Type(Integer32):
    """Custom type deviceLedsPowerOn1Blinking based on Integer32"""
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


_DeviceLedsPowerOn1Blinking_Type.__name__ = "Integer32"
_DeviceLedsPowerOn1Blinking_Object = MibTableColumn
deviceLedsPowerOn1Blinking = _DeviceLedsPowerOn1Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 7),
    _DeviceLedsPowerOn1Blinking_Type()
)
deviceLedsPowerOn1Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsPowerOn1Blinking.setStatus("current")


class _DeviceLedsPowerOn2Color_Type(Integer32):
    """Custom type deviceLedsPowerOn2Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsPowerOn2Color_Type.__name__ = "Integer32"
_DeviceLedsPowerOn2Color_Object = MibTableColumn
deviceLedsPowerOn2Color = _DeviceLedsPowerOn2Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 8),
    _DeviceLedsPowerOn2Color_Type()
)
deviceLedsPowerOn2Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsPowerOn2Color.setStatus("current")


class _DeviceLedsPowerOn2Blinking_Type(Integer32):
    """Custom type deviceLedsPowerOn2Blinking based on Integer32"""
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


_DeviceLedsPowerOn2Blinking_Type.__name__ = "Integer32"
_DeviceLedsPowerOn2Blinking_Object = MibTableColumn
deviceLedsPowerOn2Blinking = _DeviceLedsPowerOn2Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 9),
    _DeviceLedsPowerOn2Blinking_Type()
)
deviceLedsPowerOn2Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsPowerOn2Blinking.setStatus("current")


class _DeviceLedsRing1Color_Type(Integer32):
    """Custom type deviceLedsRing1Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsRing1Color_Type.__name__ = "Integer32"
_DeviceLedsRing1Color_Object = MibTableColumn
deviceLedsRing1Color = _DeviceLedsRing1Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 10),
    _DeviceLedsRing1Color_Type()
)
deviceLedsRing1Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsRing1Color.setStatus("current")


class _DeviceLedsRing1Blinking_Type(Integer32):
    """Custom type deviceLedsRing1Blinking based on Integer32"""
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


_DeviceLedsRing1Blinking_Type.__name__ = "Integer32"
_DeviceLedsRing1Blinking_Object = MibTableColumn
deviceLedsRing1Blinking = _DeviceLedsRing1Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 11),
    _DeviceLedsRing1Blinking_Type()
)
deviceLedsRing1Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsRing1Blinking.setStatus("current")


class _DeviceLedsRing2Color_Type(Integer32):
    """Custom type deviceLedsRing2Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsRing2Color_Type.__name__ = "Integer32"
_DeviceLedsRing2Color_Object = MibTableColumn
deviceLedsRing2Color = _DeviceLedsRing2Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 12),
    _DeviceLedsRing2Color_Type()
)
deviceLedsRing2Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsRing2Color.setStatus("current")


class _DeviceLedsRing2Blinking_Type(Integer32):
    """Custom type deviceLedsRing2Blinking based on Integer32"""
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


_DeviceLedsRing2Blinking_Type.__name__ = "Integer32"
_DeviceLedsRing2Blinking_Object = MibTableColumn
deviceLedsRing2Blinking = _DeviceLedsRing2Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 13),
    _DeviceLedsRing2Blinking_Type()
)
deviceLedsRing2Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsRing2Blinking.setStatus("current")


class _DeviceLedsSignalIn1Color_Type(Integer32):
    """Custom type deviceLedsSignalIn1Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsSignalIn1Color_Type.__name__ = "Integer32"
_DeviceLedsSignalIn1Color_Object = MibTableColumn
deviceLedsSignalIn1Color = _DeviceLedsSignalIn1Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 14),
    _DeviceLedsSignalIn1Color_Type()
)
deviceLedsSignalIn1Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalIn1Color.setStatus("current")


class _DeviceLedsSignalIn1Blinking_Type(Integer32):
    """Custom type deviceLedsSignalIn1Blinking based on Integer32"""
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


_DeviceLedsSignalIn1Blinking_Type.__name__ = "Integer32"
_DeviceLedsSignalIn1Blinking_Object = MibTableColumn
deviceLedsSignalIn1Blinking = _DeviceLedsSignalIn1Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 15),
    _DeviceLedsSignalIn1Blinking_Type()
)
deviceLedsSignalIn1Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalIn1Blinking.setStatus("current")


class _DeviceLedsSignalIn2Color_Type(Integer32):
    """Custom type deviceLedsSignalIn2Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsSignalIn2Color_Type.__name__ = "Integer32"
_DeviceLedsSignalIn2Color_Object = MibTableColumn
deviceLedsSignalIn2Color = _DeviceLedsSignalIn2Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 16),
    _DeviceLedsSignalIn2Color_Type()
)
deviceLedsSignalIn2Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalIn2Color.setStatus("current")


class _DeviceLedsSignalIn2Blinking_Type(Integer32):
    """Custom type deviceLedsSignalIn2Blinking based on Integer32"""
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


_DeviceLedsSignalIn2Blinking_Type.__name__ = "Integer32"
_DeviceLedsSignalIn2Blinking_Object = MibTableColumn
deviceLedsSignalIn2Blinking = _DeviceLedsSignalIn2Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 17),
    _DeviceLedsSignalIn2Blinking_Type()
)
deviceLedsSignalIn2Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalIn2Blinking.setStatus("current")


class _DeviceLedsSignalOut1Color_Type(Integer32):
    """Custom type deviceLedsSignalOut1Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsSignalOut1Color_Type.__name__ = "Integer32"
_DeviceLedsSignalOut1Color_Object = MibTableColumn
deviceLedsSignalOut1Color = _DeviceLedsSignalOut1Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 18),
    _DeviceLedsSignalOut1Color_Type()
)
deviceLedsSignalOut1Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalOut1Color.setStatus("current")


class _DeviceLedsSignalOut1Blinking_Type(Integer32):
    """Custom type deviceLedsSignalOut1Blinking based on Integer32"""
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


_DeviceLedsSignalOut1Blinking_Type.__name__ = "Integer32"
_DeviceLedsSignalOut1Blinking_Object = MibTableColumn
deviceLedsSignalOut1Blinking = _DeviceLedsSignalOut1Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 19),
    _DeviceLedsSignalOut1Blinking_Type()
)
deviceLedsSignalOut1Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalOut1Blinking.setStatus("current")


class _DeviceLedsSignalOut2Color_Type(Integer32):
    """Custom type deviceLedsSignalOut2Color based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 5),
          ("green", 2),
          ("magenta", 6),
          ("noLed", 8),
          ("off", 0),
          ("orange", 4),
          ("red", 3),
          ("white", 7))
    )


_DeviceLedsSignalOut2Color_Type.__name__ = "Integer32"
_DeviceLedsSignalOut2Color_Object = MibTableColumn
deviceLedsSignalOut2Color = _DeviceLedsSignalOut2Color_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 20),
    _DeviceLedsSignalOut2Color_Type()
)
deviceLedsSignalOut2Color.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalOut2Color.setStatus("current")


class _DeviceLedsSignalOut2Blinking_Type(Integer32):
    """Custom type deviceLedsSignalOut2Blinking based on Integer32"""
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


_DeviceLedsSignalOut2Blinking_Type.__name__ = "Integer32"
_DeviceLedsSignalOut2Blinking_Object = MibTableColumn
deviceLedsSignalOut2Blinking = _DeviceLedsSignalOut2Blinking_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 113, 1, 21),
    _DeviceLedsSignalOut2Blinking_Type()
)
deviceLedsSignalOut2Blinking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceLedsSignalOut2Blinking.setStatus("current")
_CableTestStatusTable_Object = MibTable
cableTestStatusTable = _CableTestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114)
)
if mibBuilder.loadTexts:
    cableTestStatusTable.setStatus("current")
_CableTestStatusEntry_Object = MibTableRow
cableTestStatusEntry = _CableTestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1)
)
cableTestStatusEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "cableTestStatusPortIndex"),
)
if mibBuilder.loadTexts:
    cableTestStatusEntry.setStatus("current")


class _CableTestStatusPortIndex_Type(Integer32):
    """Custom type cableTestStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CableTestStatusPortIndex_Type.__name__ = "Integer32"
_CableTestStatusPortIndex_Object = MibTableColumn
cableTestStatusPortIndex = _CableTestStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 1),
    _CableTestStatusPortIndex_Type()
)
cableTestStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableTestStatusPortIndex.setStatus("current")
_CableTestStatusUpdateTimeStamp_Type = DisplayString
_CableTestStatusUpdateTimeStamp_Object = MibTableColumn
cableTestStatusUpdateTimeStamp = _CableTestStatusUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 2),
    _CableTestStatusUpdateTimeStamp_Type()
)
cableTestStatusUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusUpdateTimeStamp.setStatus("current")


class _CableTestStatusPair0State_Type(Integer32):
    """Custom type cableTestStatusPair0State based on Integer32"""
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
        *(("crossPairShort", 4),
          ("notAvailable", 0),
          ("pairOk", 1),
          ("pairOpen", 2),
          ("samePairShort", 3))
    )


_CableTestStatusPair0State_Type.__name__ = "Integer32"
_CableTestStatusPair0State_Object = MibTableColumn
cableTestStatusPair0State = _CableTestStatusPair0State_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 3),
    _CableTestStatusPair0State_Type()
)
cableTestStatusPair0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair0State.setStatus("current")


class _CableTestStatusPair0DistanceToFault_Type(Integer32):
    """Custom type cableTestStatusPair0DistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CableTestStatusPair0DistanceToFault_Type.__name__ = "Integer32"
_CableTestStatusPair0DistanceToFault_Object = MibTableColumn
cableTestStatusPair0DistanceToFault = _CableTestStatusPair0DistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 4),
    _CableTestStatusPair0DistanceToFault_Type()
)
cableTestStatusPair0DistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair0DistanceToFault.setStatus("current")


class _CableTestStatusPair1State_Type(Integer32):
    """Custom type cableTestStatusPair1State based on Integer32"""
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
        *(("crossPairShort", 4),
          ("notAvailable", 0),
          ("pairOk", 1),
          ("pairOpen", 2),
          ("samePairShort", 3))
    )


_CableTestStatusPair1State_Type.__name__ = "Integer32"
_CableTestStatusPair1State_Object = MibTableColumn
cableTestStatusPair1State = _CableTestStatusPair1State_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 5),
    _CableTestStatusPair1State_Type()
)
cableTestStatusPair1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair1State.setStatus("current")


class _CableTestStatusPair1DistanceToFault_Type(Integer32):
    """Custom type cableTestStatusPair1DistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CableTestStatusPair1DistanceToFault_Type.__name__ = "Integer32"
_CableTestStatusPair1DistanceToFault_Object = MibTableColumn
cableTestStatusPair1DistanceToFault = _CableTestStatusPair1DistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 6),
    _CableTestStatusPair1DistanceToFault_Type()
)
cableTestStatusPair1DistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair1DistanceToFault.setStatus("current")


class _CableTestStatusPair2State_Type(Integer32):
    """Custom type cableTestStatusPair2State based on Integer32"""
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
        *(("crossPairShort", 4),
          ("notAvailable", 0),
          ("pairOk", 1),
          ("pairOpen", 2),
          ("samePairShort", 3))
    )


_CableTestStatusPair2State_Type.__name__ = "Integer32"
_CableTestStatusPair2State_Object = MibTableColumn
cableTestStatusPair2State = _CableTestStatusPair2State_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 7),
    _CableTestStatusPair2State_Type()
)
cableTestStatusPair2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair2State.setStatus("current")


class _CableTestStatusPair2DistanceToFault_Type(Integer32):
    """Custom type cableTestStatusPair2DistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CableTestStatusPair2DistanceToFault_Type.__name__ = "Integer32"
_CableTestStatusPair2DistanceToFault_Object = MibTableColumn
cableTestStatusPair2DistanceToFault = _CableTestStatusPair2DistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 8),
    _CableTestStatusPair2DistanceToFault_Type()
)
cableTestStatusPair2DistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair2DistanceToFault.setStatus("current")


class _CableTestStatusPair3State_Type(Integer32):
    """Custom type cableTestStatusPair3State based on Integer32"""
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
        *(("crossPairShort", 4),
          ("notAvailable", 0),
          ("pairOk", 1),
          ("pairOpen", 2),
          ("samePairShort", 3))
    )


_CableTestStatusPair3State_Type.__name__ = "Integer32"
_CableTestStatusPair3State_Object = MibTableColumn
cableTestStatusPair3State = _CableTestStatusPair3State_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 9),
    _CableTestStatusPair3State_Type()
)
cableTestStatusPair3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair3State.setStatus("current")


class _CableTestStatusPair3DistanceToFault_Type(Integer32):
    """Custom type cableTestStatusPair3DistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CableTestStatusPair3DistanceToFault_Type.__name__ = "Integer32"
_CableTestStatusPair3DistanceToFault_Object = MibTableColumn
cableTestStatusPair3DistanceToFault = _CableTestStatusPair3DistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 10),
    _CableTestStatusPair3DistanceToFault_Type()
)
cableTestStatusPair3DistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusPair3DistanceToFault.setStatus("current")


class _CableTestStatusCableStatus_Type(Integer32):
    """Custom type cableTestStatusCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("open", 2),
          ("pluggedIn", 1))
    )


_CableTestStatusCableStatus_Type.__name__ = "Integer32"
_CableTestStatusCableStatus_Object = MibTableColumn
cableTestStatusCableStatus = _CableTestStatusCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 114, 1, 11),
    _CableTestStatusCableStatus_Type()
)
cableTestStatusCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableTestStatusCableStatus.setStatus("current")
_IoSignalStatusTable_Object = MibTable
ioSignalStatusTable = _IoSignalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115)
)
if mibBuilder.loadTexts:
    ioSignalStatusTable.setStatus("current")
_IoSignalStatusEntry_Object = MibTableRow
ioSignalStatusEntry = _IoSignalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115, 1)
)
ioSignalStatusEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "ioSignalStatusIndex"),
)
if mibBuilder.loadTexts:
    ioSignalStatusEntry.setStatus("current")


class _IoSignalStatusIndex_Type(Integer32):
    """Custom type ioSignalStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_IoSignalStatusIndex_Type.__name__ = "Integer32"
_IoSignalStatusIndex_Object = MibTableColumn
ioSignalStatusIndex = _IoSignalStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115, 1, 1),
    _IoSignalStatusIndex_Type()
)
ioSignalStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ioSignalStatusIndex.setStatus("current")


class _IoSignalStatusInput1AlarmActive_Type(Integer32):
    """Custom type ioSignalStatusInput1AlarmActive based on Integer32"""
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


_IoSignalStatusInput1AlarmActive_Type.__name__ = "Integer32"
_IoSignalStatusInput1AlarmActive_Object = MibTableColumn
ioSignalStatusInput1AlarmActive = _IoSignalStatusInput1AlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115, 1, 2),
    _IoSignalStatusInput1AlarmActive_Type()
)
ioSignalStatusInput1AlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSignalStatusInput1AlarmActive.setStatus("current")


class _IoSignalStatusInput2AlarmActive_Type(Integer32):
    """Custom type ioSignalStatusInput2AlarmActive based on Integer32"""
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


_IoSignalStatusInput2AlarmActive_Type.__name__ = "Integer32"
_IoSignalStatusInput2AlarmActive_Object = MibTableColumn
ioSignalStatusInput2AlarmActive = _IoSignalStatusInput2AlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115, 1, 3),
    _IoSignalStatusInput2AlarmActive_Type()
)
ioSignalStatusInput2AlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSignalStatusInput2AlarmActive.setStatus("current")


class _IoSignalStatusOutput1RelayActive_Type(Integer32):
    """Custom type ioSignalStatusOutput1RelayActive based on Integer32"""
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


_IoSignalStatusOutput1RelayActive_Type.__name__ = "Integer32"
_IoSignalStatusOutput1RelayActive_Object = MibTableColumn
ioSignalStatusOutput1RelayActive = _IoSignalStatusOutput1RelayActive_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115, 1, 4),
    _IoSignalStatusOutput1RelayActive_Type()
)
ioSignalStatusOutput1RelayActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSignalStatusOutput1RelayActive.setStatus("current")


class _IoSignalStatusOutput2RelayActive_Type(Integer32):
    """Custom type ioSignalStatusOutput2RelayActive based on Integer32"""
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


_IoSignalStatusOutput2RelayActive_Type.__name__ = "Integer32"
_IoSignalStatusOutput2RelayActive_Object = MibTableColumn
ioSignalStatusOutput2RelayActive = _IoSignalStatusOutput2RelayActive_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 115, 1, 5),
    _IoSignalStatusOutput2RelayActive_Type()
)
ioSignalStatusOutput2RelayActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSignalStatusOutput2RelayActive.setStatus("current")
_TcamStatusTable_Object = MibTable
tcamStatusTable = _TcamStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 116)
)
if mibBuilder.loadTexts:
    tcamStatusTable.setStatus("current")
_TcamStatusEntry_Object = MibTableRow
tcamStatusEntry = _TcamStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 116, 1)
)
tcamStatusEntry.setIndexNames(
    (0, "G6-HARDWARE-MIB", "tcamStatusIndex"),
)
if mibBuilder.loadTexts:
    tcamStatusEntry.setStatus("current")


class _TcamStatusIndex_Type(Integer32):
    """Custom type tcamStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TcamStatusIndex_Type.__name__ = "Integer32"
_TcamStatusIndex_Object = MibTableColumn
tcamStatusIndex = _TcamStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 116, 1, 1),
    _TcamStatusIndex_Type()
)
tcamStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcamStatusIndex.setStatus("current")
_TcamStatusControlFile_Type = DisplayString
_TcamStatusControlFile_Object = MibTableColumn
tcamStatusControlFile = _TcamStatusControlFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 116, 1, 2),
    _TcamStatusControlFile_Type()
)
tcamStatusControlFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcamStatusControlFile.setStatus("current")
_TcamStatusDescription_Type = DisplayString
_TcamStatusDescription_Object = MibTableColumn
tcamStatusDescription = _TcamStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 31, 116, 1, 3),
    _TcamStatusDescription_Type()
)
tcamStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcamStatusDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-HARDWARE-MIB",
    **{"device": device,
       "hardware": hardware,
       "hardwareLedTest": hardwareLedTest,
       "hardwareLedMode": hardwareLedMode,
       "hardwarePowerSupply1Monitored": hardwarePowerSupply1Monitored,
       "hardwarePowerSupply2Monitored": hardwarePowerSupply2Monitored,
       "hardwareFactoryResetButton": hardwareFactoryResetButton,
       "cableTestConfigTable": cableTestConfigTable,
       "cableTestConfigEntry": cableTestConfigEntry,
       "cableTestConfigPortIndex": cableTestConfigPortIndex,
       "cableTestConfigEnableAutoCableTest": cableTestConfigEnableAutoCableTest,
       "cableTestConfigEventGeneration": cableTestConfigEventGeneration,
       "cableTestConfigStartTestNow": cableTestConfigStartTestNow,
       "ioSignalConfigTable": ioSignalConfigTable,
       "ioSignalConfigEntry": ioSignalConfigEntry,
       "ioSignalConfigIndex": ioSignalConfigIndex,
       "ioSignalConfigSignalMode": ioSignalConfigSignalMode,
       "ioSignalConfigInput1Mode": ioSignalConfigInput1Mode,
       "ioSignalConfigInput1Name": ioSignalConfigInput1Name,
       "ioSignalConfigInput2Mode": ioSignalConfigInput2Mode,
       "ioSignalConfigInput2Name": ioSignalConfigInput2Name,
       "ioSignalConfigOutput1Trigger": ioSignalConfigOutput1Trigger,
       "ioSignalConfigOutput1Name": ioSignalConfigOutput1Name,
       "ioSignalConfigOutput2Trigger": ioSignalConfigOutput2Trigger,
       "ioSignalConfigOutput2Name": ioSignalConfigOutput2Name,
       "hardwarePowerSupply1Status": hardwarePowerSupply1Status,
       "hardwarePowerSupply2Status": hardwarePowerSupply2Status,
       "hardwareRunningOnPoe": hardwareRunningOnPoe,
       "hardwareFanStatus": hardwareFanStatus,
       "hardwareSdCardStatus": hardwareSdCardStatus,
       "hardwareNumOfPorts": hardwareNumOfPorts,
       "hardwareMaskOfExistingPorts": hardwareMaskOfExistingPorts,
       "hardwareMaskOfSfpPorts": hardwareMaskOfSfpPorts,
       "hardwareMaskOfPoePorts": hardwareMaskOfPoePorts,
       "moduleInfoTable": moduleInfoTable,
       "moduleInfoEntry": moduleInfoEntry,
       "moduleInfoIndex": moduleInfoIndex,
       "moduleInfoUnitType": moduleInfoUnitType,
       "moduleInfoArticleNumber": moduleInfoArticleNumber,
       "moduleInfoSerialNumber": moduleInfoSerialNumber,
       "moduleInfoHardwareVersion": moduleInfoHardwareVersion,
       "moduleInfoProjectNumber": moduleInfoProjectNumber,
       "moduleInfoOccupiedSlots": moduleInfoOccupiedSlots,
       "moduleInfoDescription": moduleInfoDescription,
       "slotInfoTable": slotInfoTable,
       "slotInfoEntry": slotInfoEntry,
       "slotInfoIndex": slotInfoIndex,
       "slotInfoBoardType": slotInfoBoardType,
       "slotInfoBoardId": slotInfoBoardId,
       "slotInfoVersionBits": slotInfoVersionBits,
       "portInfoTable": portInfoTable,
       "portInfoEntry": portInfoEntry,
       "portInfoPortIndex": portInfoPortIndex,
       "portInfoSystemSlot": portInfoSystemSlot,
       "portInfoSwitchPort": portInfoSwitchPort,
       "portInfoUserSlot": portInfoUserSlot,
       "portInfoUserPort": portInfoUserPort,
       "portInfoSnmpPort": portInfoSnmpPort,
       "portInfoSnmpInstance": portInfoSnmpInstance,
       "portInfoHardwarePort": portInfoHardwarePort,
       "portInfoInterfaceType": portInfoInterfaceType,
       "portInfoProperties": portInfoProperties,
       "portLedsTable": portLedsTable,
       "portLedsEntry": portLedsEntry,
       "portLedsPortIndex": portLedsPortIndex,
       "portLedsEthernetColor": portLedsEthernetColor,
       "portLedsEthernetBlinking": portLedsEthernetBlinking,
       "portLedsPoeColor": portLedsPoeColor,
       "portLedsPoeBlinking": portLedsPoeBlinking,
       "deviceLedsTable": deviceLedsTable,
       "deviceLedsEntry": deviceLedsEntry,
       "deviceLedsIndex": deviceLedsIndex,
       "deviceLedsSystem1Color": deviceLedsSystem1Color,
       "deviceLedsSystem1Blinking": deviceLedsSystem1Blinking,
       "deviceLedsSystem2Color": deviceLedsSystem2Color,
       "deviceLedsSystem2Blinking": deviceLedsSystem2Blinking,
       "deviceLedsPowerOn1Color": deviceLedsPowerOn1Color,
       "deviceLedsPowerOn1Blinking": deviceLedsPowerOn1Blinking,
       "deviceLedsPowerOn2Color": deviceLedsPowerOn2Color,
       "deviceLedsPowerOn2Blinking": deviceLedsPowerOn2Blinking,
       "deviceLedsRing1Color": deviceLedsRing1Color,
       "deviceLedsRing1Blinking": deviceLedsRing1Blinking,
       "deviceLedsRing2Color": deviceLedsRing2Color,
       "deviceLedsRing2Blinking": deviceLedsRing2Blinking,
       "deviceLedsSignalIn1Color": deviceLedsSignalIn1Color,
       "deviceLedsSignalIn1Blinking": deviceLedsSignalIn1Blinking,
       "deviceLedsSignalIn2Color": deviceLedsSignalIn2Color,
       "deviceLedsSignalIn2Blinking": deviceLedsSignalIn2Blinking,
       "deviceLedsSignalOut1Color": deviceLedsSignalOut1Color,
       "deviceLedsSignalOut1Blinking": deviceLedsSignalOut1Blinking,
       "deviceLedsSignalOut2Color": deviceLedsSignalOut2Color,
       "deviceLedsSignalOut2Blinking": deviceLedsSignalOut2Blinking,
       "cableTestStatusTable": cableTestStatusTable,
       "cableTestStatusEntry": cableTestStatusEntry,
       "cableTestStatusPortIndex": cableTestStatusPortIndex,
       "cableTestStatusUpdateTimeStamp": cableTestStatusUpdateTimeStamp,
       "cableTestStatusPair0State": cableTestStatusPair0State,
       "cableTestStatusPair0DistanceToFault": cableTestStatusPair0DistanceToFault,
       "cableTestStatusPair1State": cableTestStatusPair1State,
       "cableTestStatusPair1DistanceToFault": cableTestStatusPair1DistanceToFault,
       "cableTestStatusPair2State": cableTestStatusPair2State,
       "cableTestStatusPair2DistanceToFault": cableTestStatusPair2DistanceToFault,
       "cableTestStatusPair3State": cableTestStatusPair3State,
       "cableTestStatusPair3DistanceToFault": cableTestStatusPair3DistanceToFault,
       "cableTestStatusCableStatus": cableTestStatusCableStatus,
       "ioSignalStatusTable": ioSignalStatusTable,
       "ioSignalStatusEntry": ioSignalStatusEntry,
       "ioSignalStatusIndex": ioSignalStatusIndex,
       "ioSignalStatusInput1AlarmActive": ioSignalStatusInput1AlarmActive,
       "ioSignalStatusInput2AlarmActive": ioSignalStatusInput2AlarmActive,
       "ioSignalStatusOutput1RelayActive": ioSignalStatusOutput1RelayActive,
       "ioSignalStatusOutput2RelayActive": ioSignalStatusOutput2RelayActive,
       "tcamStatusTable": tcamStatusTable,
       "tcamStatusEntry": tcamStatusEntry,
       "tcamStatusIndex": tcamStatusIndex,
       "tcamStatusControlFile": tcamStatusControlFile,
       "tcamStatusDescription": tcamStatusDescription}
)
