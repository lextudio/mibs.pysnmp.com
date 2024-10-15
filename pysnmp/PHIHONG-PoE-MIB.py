# SNMP MIB module (PHIHONG-PoE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PHIHONG-PoE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:37 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Phihong_ObjectIdentity = ObjectIdentity
phihong = _Phihong_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24852)
)
_PoeProduct_ObjectIdentity = ObjectIdentity
poeProduct = _PoeProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24852, 2)
)
_PoeProductsPart_Type = DisplayString
_PoeProductsPart_Object = MibScalar
poeProductsPart = _PoeProductsPart_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 1),
    _PoeProductsPart_Type()
)
poeProductsPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeProductsPart.setStatus("current")
_PoeSystem_ObjectIdentity = ObjectIdentity
poeSystem = _PoeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2)
)


class _PoeSystemActionHubReset_Type(Integer32):
    """Custom type poeSystemActionHubReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("reset", 1))
    )


_PoeSystemActionHubReset_Type.__name__ = "Integer32"
_PoeSystemActionHubReset_Object = MibScalar
poeSystemActionHubReset = _PoeSystemActionHubReset_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 1),
    _PoeSystemActionHubReset_Type()
)
poeSystemActionHubReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    poeSystemActionHubReset.setStatus("current")


class _PoeSystemActionHubRestoreFactoryDefault_Type(Integer32):
    """Custom type poeSystemActionHubRestoreFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("restore", 1))
    )


_PoeSystemActionHubRestoreFactoryDefault_Type.__name__ = "Integer32"
_PoeSystemActionHubRestoreFactoryDefault_Object = MibScalar
poeSystemActionHubRestoreFactoryDefault = _PoeSystemActionHubRestoreFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 2),
    _PoeSystemActionHubRestoreFactoryDefault_Type()
)
poeSystemActionHubRestoreFactoryDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    poeSystemActionHubRestoreFactoryDefault.setStatus("current")


class _PoeSystemActionHubSaveConfiguration_Type(Integer32):
    """Custom type poeSystemActionHubSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("save", 1))
    )


_PoeSystemActionHubSaveConfiguration_Type.__name__ = "Integer32"
_PoeSystemActionHubSaveConfiguration_Object = MibScalar
poeSystemActionHubSaveConfiguration = _PoeSystemActionHubSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 3),
    _PoeSystemActionHubSaveConfiguration_Type()
)
poeSystemActionHubSaveConfiguration.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    poeSystemActionHubSaveConfiguration.setStatus("current")


class _PoeSystemAllPortPowerEnable_Type(Integer32):
    """Custom type poeSystemAllPortPowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("ready", 0))
    )


_PoeSystemAllPortPowerEnable_Type.__name__ = "Integer32"
_PoeSystemAllPortPowerEnable_Object = MibScalar
poeSystemAllPortPowerEnable = _PoeSystemAllPortPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 4),
    _PoeSystemAllPortPowerEnable_Type()
)
poeSystemAllPortPowerEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    poeSystemAllPortPowerEnable.setStatus("current")
_PoeSystemHWVersion_Type = DisplayString
_PoeSystemHWVersion_Object = MibScalar
poeSystemHWVersion = _PoeSystemHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 6),
    _PoeSystemHWVersion_Type()
)
poeSystemHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemHWVersion.setStatus("current")
_PoeSystemNumberOfChannel_Type = Integer32
_PoeSystemNumberOfChannel_Object = MibScalar
poeSystemNumberOfChannel = _PoeSystemNumberOfChannel_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 7),
    _PoeSystemNumberOfChannel_Type()
)
poeSystemNumberOfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemNumberOfChannel.setStatus("current")
_PoeSystemProductPartNumber_Type = DisplayString
_PoeSystemProductPartNumber_Object = MibScalar
poeSystemProductPartNumber = _PoeSystemProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 8),
    _PoeSystemProductPartNumber_Type()
)
poeSystemProductPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemProductPartNumber.setStatus("current")
_PoeSystemFirmwareVersion_Type = DisplayString
_PoeSystemFirmwareVersion_Object = MibScalar
poeSystemFirmwareVersion = _PoeSystemFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 10),
    _PoeSystemFirmwareVersion_Type()
)
poeSystemFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemFirmwareVersion.setStatus("current")


class _PoeSystemDescription_Type(DisplayString):
    """Custom type poeSystemDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PoeSystemDescription_Type.__name__ = "DisplayString"
_PoeSystemDescription_Object = MibScalar
poeSystemDescription = _PoeSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 11),
    _PoeSystemDescription_Type()
)
poeSystemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSystemDescription.setStatus("current")
_PoeSystemConsumptionPower_Type = Integer32
_PoeSystemConsumptionPower_Object = MibScalar
poeSystemConsumptionPower = _PoeSystemConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 12),
    _PoeSystemConsumptionPower_Type()
)
poeSystemConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    poeSystemConsumptionPower.setUnits("Watts")
_PoeSystemControlACPower_Type = Integer32
_PoeSystemControlACPower_Object = MibScalar
poeSystemControlACPower = _PoeSystemControlACPower_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 13),
    _PoeSystemControlACPower_Type()
)
poeSystemControlACPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSystemControlACPower.setStatus("current")
if mibBuilder.loadTexts:
    poeSystemControlACPower.setUnits("Watts")
_PoeSystemControlDCPower_Type = Integer32
_PoeSystemControlDCPower_Object = MibScalar
poeSystemControlDCPower = _PoeSystemControlDCPower_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 14),
    _PoeSystemControlDCPower_Type()
)
poeSystemControlDCPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSystemControlDCPower.setStatus("current")
if mibBuilder.loadTexts:
    poeSystemControlDCPower.setUnits("Watts")
_PoeSystemControlBothPower_Type = Integer32
_PoeSystemControlBothPower_Object = MibScalar
poeSystemControlBothPower = _PoeSystemControlBothPower_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 15),
    _PoeSystemControlBothPower_Type()
)
poeSystemControlBothPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSystemControlBothPower.setStatus("current")
if mibBuilder.loadTexts:
    poeSystemControlBothPower.setUnits("Watts")


class _PoeSystemParameters_Type(DisplayString):
    """Custom type poeSystemParameters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_PoeSystemParameters_Type.__name__ = "DisplayString"
_PoeSystemParameters_Object = MibScalar
poeSystemParameters = _PoeSystemParameters_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 16),
    _PoeSystemParameters_Type()
)
poeSystemParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSystemParameters.setStatus("current")
_PoeSystemSnmpVersion_Type = DisplayString
_PoeSystemSnmpVersion_Object = MibScalar
poeSystemSnmpVersion = _PoeSystemSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 17),
    _PoeSystemSnmpVersion_Type()
)
poeSystemSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemSnmpVersion.setStatus("current")


class _PoeSystemPerPortPowerEnable_Type(DisplayString):
    """Custom type poeSystemPerPortPowerEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_PoeSystemPerPortPowerEnable_Type.__name__ = "DisplayString"
_PoeSystemPerPortPowerEnable_Object = MibScalar
poeSystemPerPortPowerEnable = _PoeSystemPerPortPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 18),
    _PoeSystemPerPortPowerEnable_Type()
)
poeSystemPerPortPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeSystemPerPortPowerEnable.setStatus("current")


class _PoeSystemStatus_Type(Integer32):
    """Custom type poeSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("overheat", 1))
    )


_PoeSystemStatus_Type.__name__ = "Integer32"
_PoeSystemStatus_Object = MibScalar
poeSystemStatus = _PoeSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 2, 19),
    _PoeSystemStatus_Type()
)
poeSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeSystemStatus.setStatus("current")
_PoePortTable_Object = MibTable
poePortTable = _PoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3)
)
if mibBuilder.loadTexts:
    poePortTable.setStatus("current")
_PoePortEntry_Object = MibTableRow
poePortEntry = _PoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1)
)
poePortEntry.setIndexNames(
    (0, "PHIHONG-PoE-MIB", "poePortIndex"),
)
if mibBuilder.loadTexts:
    poePortEntry.setStatus("current")


class _PoePortIndex_Type(Integer32):
    """Custom type poePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PoePortIndex_Type.__name__ = "Integer32"
_PoePortIndex_Object = MibTableColumn
poePortIndex = _PoePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 1),
    _PoePortIndex_Type()
)
poePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortIndex.setStatus("current")


class _PoePortPowerEnable_Type(Integer32):
    """Custom type poePortPowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PoePortPowerEnable_Type.__name__ = "Integer32"
_PoePortPowerEnable_Object = MibTableColumn
poePortPowerEnable = _PoePortPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 2),
    _PoePortPowerEnable_Type()
)
poePortPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPowerEnable.setStatus("current")
_PoePortControlMaxPower_Type = Integer32
_PoePortControlMaxPower_Object = MibTableColumn
poePortControlMaxPower = _PoePortControlMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 3),
    _PoePortControlMaxPower_Type()
)
poePortControlMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortControlMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    poePortControlMaxPower.setUnits("mWatts")


class _PoePortDescription_Type(DisplayString):
    """Custom type poePortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PoePortDescription_Type.__name__ = "DisplayString"
_PoePortDescription_Object = MibTableColumn
poePortDescription = _PoePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 6),
    _PoePortDescription_Type()
)
poePortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortDescription.setStatus("current")


class _PoePortDetectionStatus_Type(Integer32):
    """Custom type poePortDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("class", 3),
          ("discC", 2),
          ("discR", 1),
          ("off", 0),
          ("ramPOEown", 5),
          ("rampUp", 4),
          ("sampleI", 8),
          ("sampleV", 9))
    )


_PoePortDetectionStatus_Type.__name__ = "Integer32"
_PoePortDetectionStatus_Object = MibTableColumn
poePortDetectionStatus = _PoePortDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 7),
    _PoePortDetectionStatus_Type()
)
poePortDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortDetectionStatus.setStatus("current")


class _PoePortPowerClassifications_Type(Integer32):
    """Custom type poePortPowerClassifications based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PoePortPowerClassifications_Type.__name__ = "Integer32"
_PoePortPowerClassifications_Object = MibTableColumn
poePortPowerClassifications = _PoePortPowerClassifications_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 8),
    _PoePortPowerClassifications_Type()
)
poePortPowerClassifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortPowerClassifications.setStatus("current")


class _PoePortPowerDetectionControl_Type(Integer32):
    """Custom type poePortPowerDetectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PoePortPowerDetectionControl_Type.__name__ = "Integer32"
_PoePortPowerDetectionControl_Object = MibTableColumn
poePortPowerDetectionControl = _PoePortPowerDetectionControl_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 9),
    _PoePortPowerDetectionControl_Type()
)
poePortPowerDetectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPowerDetectionControl.setStatus("current")


class _PoePortPowerPriority_Type(Integer32):
    """Custom type poePortPowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_PoePortPowerPriority_Type.__name__ = "Integer32"
_PoePortPowerPriority_Object = MibTableColumn
poePortPowerPriority = _PoePortPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 10),
    _PoePortPowerPriority_Type()
)
poePortPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortPowerPriority.setStatus("current")
_PoePortPower_Type = Integer32
_PoePortPower_Object = MibTableColumn
poePortPower = _PoePortPower_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 11),
    _PoePortPower_Type()
)
poePortPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortPower.setStatus("current")
if mibBuilder.loadTexts:
    poePortPower.setUnits("mWattes")
_PoePortVoltage_Type = DisplayString
_PoePortVoltage_Object = MibTableColumn
poePortVoltage = _PoePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 12),
    _PoePortVoltage_Type()
)
poePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    poePortVoltage.setUnits("dVoltage")
_PoePortCurrent_Type = Integer32
_PoePortCurrent_Object = MibTableColumn
poePortCurrent = _PoePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 13),
    _PoePortCurrent_Type()
)
poePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortCurrent.setStatus("current")
if mibBuilder.loadTexts:
    poePortCurrent.setUnits("mAmps")
_PoePortResistance_Type = Integer32
_PoePortResistance_Object = MibTableColumn
poePortResistance = _PoePortResistance_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 14),
    _PoePortResistance_Type()
)
poePortResistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortResistance.setStatus("current")
if mibBuilder.loadTexts:
    poePortResistance.setUnits("ohms")


class _PoePortFlags_Type(DisplayString):
    """Custom type poePortFlags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_PoePortFlags_Type.__name__ = "DisplayString"
_PoePortFlags_Object = MibTableColumn
poePortFlags = _PoePortFlags_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 15),
    _PoePortFlags_Type()
)
poePortFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poePortFlags.setStatus("current")


class _PoePortBypassFlags_Type(DisplayString):
    """Custom type poePortBypassFlags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PoePortBypassFlags_Type.__name__ = "DisplayString"
_PoePortBypassFlags_Object = MibTableColumn
poePortBypassFlags = _PoePortBypassFlags_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 16),
    _PoePortBypassFlags_Type()
)
poePortBypassFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortBypassFlags.setStatus("current")


class _PoePortUseClassificationforPowerLimit_Type(Integer32):
    """Custom type poePortUseClassificationforPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PoePortUseClassificationforPowerLimit_Type.__name__ = "Integer32"
_PoePortUseClassificationforPowerLimit_Object = MibTableColumn
poePortUseClassificationforPowerLimit = _PoePortUseClassificationforPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 17),
    _PoePortUseClassificationforPowerLimit_Type()
)
poePortUseClassificationforPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortUseClassificationforPowerLimit.setStatus("current")


class _PoePortLegacyDetection_Type(Integer32):
    """Custom type poePortLegacyDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PoePortLegacyDetection_Type.__name__ = "Integer32"
_PoePortLegacyDetection_Object = MibTableColumn
poePortLegacyDetection = _PoePortLegacyDetection_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 3, 1, 18),
    _PoePortLegacyDetection_Type()
)
poePortLegacyDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePortLegacyDetection.setStatus("current")
_PoeTrapsControlTable_Object = MibTable
poeTrapsControlTable = _PoeTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 4)
)
if mibBuilder.loadTexts:
    poeTrapsControlTable.setStatus("current")
_PoeTrapsControlEntry_Object = MibTableRow
poeTrapsControlEntry = _PoeTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 4, 1)
)
poeTrapsControlEntry.setIndexNames(
    (0, "PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
)
if mibBuilder.loadTexts:
    poeTrapsControlEntry.setStatus("current")


class _PoeTrapsControlGroupIndex_Type(Integer32):
    """Custom type poeTrapsControlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoeTrapsControlGroupIndex_Type.__name__ = "Integer32"
_PoeTrapsControlGroupIndex_Object = MibTableColumn
poeTrapsControlGroupIndex = _PoeTrapsControlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 4, 1, 1),
    _PoeTrapsControlGroupIndex_Type()
)
poeTrapsControlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poeTrapsControlGroupIndex.setStatus("current")


class _PoeTrapsControlEnable_Type(Integer32):
    """Custom type poeTrapsControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapsDisabled", 1),
          ("trapsEnabled", 2))
    )


_PoeTrapsControlEnable_Type.__name__ = "Integer32"
_PoeTrapsControlEnable_Object = MibTableColumn
poeTrapsControlEnable = _PoeTrapsControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 24852, 2, 4, 1, 2),
    _PoeTrapsControlEnable_Type()
)
poeTrapsControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeTrapsControlEnable.setStatus("current")
_PoeTraps_ObjectIdentity = ObjectIdentity
poeTraps = _PoeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5)
)

# Managed Objects groups


# Notification objects

poePortHWFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 1)
)
poePortHWFailTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortVoltage"))
)
if mibBuilder.loadTexts:
    poePortHWFailTrap.setStatus(
        "current"
    )

poePortPeakOverCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 2)
)
poePortPeakOverCurrentTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortCurrent"))
)
if mibBuilder.loadTexts:
    poePortPeakOverCurrentTrap.setStatus(
        "current"
    )

poePortOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 3)
)
poePortOverloadTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortDetectionStatus"))
)
if mibBuilder.loadTexts:
    poePortOverloadTrap.setStatus(
        "current"
    )

poePortDiscoveryFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 4)
)
poePortDiscoveryFailTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortVoltage"))
)
if mibBuilder.loadTexts:
    poePortDiscoveryFailTrap.setStatus(
        "current"
    )

poePortClassificationFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 5)
)
poePortClassificationFailTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortVoltage"))
)
if mibBuilder.loadTexts:
    poePortClassificationFailTrap.setStatus(
        "current"
    )

poePortDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 6)
)
poePortDisconnectTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortDetectionStatus"))
)
if mibBuilder.loadTexts:
    poePortDisconnectTrap.setStatus(
        "current"
    )

poePortVoltageFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 7)
)
poePortVoltageFailTrap.setObjects(
      *(("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex"),
        ("PHIHONG-PoE-MIB", "poePortVoltage"))
)
if mibBuilder.loadTexts:
    poePortVoltageFailTrap.setStatus(
        "current"
    )

poeSystemOverheatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 24852, 2, 5, 8)
)
poeSystemOverheatTrap.setObjects(
    ("PHIHONG-PoE-MIB", "poeTrapsControlGroupIndex")
)
if mibBuilder.loadTexts:
    poeSystemOverheatTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PHIHONG-PoE-MIB",
    **{"phihong": phihong,
       "poeProduct": poeProduct,
       "poeProductsPart": poeProductsPart,
       "poeSystem": poeSystem,
       "poeSystemActionHubReset": poeSystemActionHubReset,
       "poeSystemActionHubRestoreFactoryDefault": poeSystemActionHubRestoreFactoryDefault,
       "poeSystemActionHubSaveConfiguration": poeSystemActionHubSaveConfiguration,
       "poeSystemAllPortPowerEnable": poeSystemAllPortPowerEnable,
       "poeSystemHWVersion": poeSystemHWVersion,
       "poeSystemNumberOfChannel": poeSystemNumberOfChannel,
       "poeSystemProductPartNumber": poeSystemProductPartNumber,
       "poeSystemFirmwareVersion": poeSystemFirmwareVersion,
       "poeSystemDescription": poeSystemDescription,
       "poeSystemConsumptionPower": poeSystemConsumptionPower,
       "poeSystemControlACPower": poeSystemControlACPower,
       "poeSystemControlDCPower": poeSystemControlDCPower,
       "poeSystemControlBothPower": poeSystemControlBothPower,
       "poeSystemParameters": poeSystemParameters,
       "poeSystemSnmpVersion": poeSystemSnmpVersion,
       "poeSystemPerPortPowerEnable": poeSystemPerPortPowerEnable,
       "poeSystemStatus": poeSystemStatus,
       "poePortTable": poePortTable,
       "poePortEntry": poePortEntry,
       "poePortIndex": poePortIndex,
       "poePortPowerEnable": poePortPowerEnable,
       "poePortControlMaxPower": poePortControlMaxPower,
       "poePortDescription": poePortDescription,
       "poePortDetectionStatus": poePortDetectionStatus,
       "poePortPowerClassifications": poePortPowerClassifications,
       "poePortPowerDetectionControl": poePortPowerDetectionControl,
       "poePortPowerPriority": poePortPowerPriority,
       "poePortPower": poePortPower,
       "poePortVoltage": poePortVoltage,
       "poePortCurrent": poePortCurrent,
       "poePortResistance": poePortResistance,
       "poePortFlags": poePortFlags,
       "poePortBypassFlags": poePortBypassFlags,
       "poePortUseClassificationforPowerLimit": poePortUseClassificationforPowerLimit,
       "poePortLegacyDetection": poePortLegacyDetection,
       "poeTrapsControlTable": poeTrapsControlTable,
       "poeTrapsControlEntry": poeTrapsControlEntry,
       "poeTrapsControlGroupIndex": poeTrapsControlGroupIndex,
       "poeTrapsControlEnable": poeTrapsControlEnable,
       "poeTraps": poeTraps,
       "poePortHWFailTrap": poePortHWFailTrap,
       "poePortPeakOverCurrentTrap": poePortPeakOverCurrentTrap,
       "poePortOverloadTrap": poePortOverloadTrap,
       "poePortDiscoveryFailTrap": poePortDiscoveryFailTrap,
       "poePortClassificationFailTrap": poePortClassificationFailTrap,
       "poePortDisconnectTrap": poePortDisconnectTrap,
       "poePortVoltageFailTrap": poePortVoltageFailTrap,
       "poeSystemOverheatTrap": poeSystemOverheatTrap}
)
