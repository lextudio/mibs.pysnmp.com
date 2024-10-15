# SNMP MIB module (IDRAC-MIB-SMIv2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IDRAC-MIB-SMIv2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:06 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

outOfBandGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5)
)
outOfBandGroup.setRevisions(
        ("2015-01-19 00:00",
         "2014-10-03 00:00",
         "2014-07-07 00:00",
         "2013-08-22 00:00",
         "2012-10-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class StringType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class String64(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class FQDDString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class MACAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class ObjectRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class Unsigned8BitRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class Unsigned16BitRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Unsigned32BitRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Signed32BitRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )



class BooleanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )



class DateName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )



class StateCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enableAndNotReadyCapable", 6),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )



class StateSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("enabledAndNotReady", 6),
          ("notReady", 4),
          ("unknown", 1))
    )



class ProbeCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("lowerNonCriticalThresholdDefaultCapable", 8),
          ("lowerNonCriticalThresholdSetCapable", 2),
          ("upperNonCriticalThresholdDefaultCapable", 4),
          ("upperNonCriticalThresholdSetCapable", 1))
    )



class StatusProbeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("criticalLower", 8),
          ("criticalUpper", 5),
          ("failed", 10),
          ("nonCriticalLower", 7),
          ("nonCriticalUpper", 4),
          ("nonRecoverableLower", 9),
          ("nonRecoverableUpper", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )



class StatusRedundancyEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("degraded", 4),
          ("full", 3),
          ("lost", 5),
          ("notRedundant", 6),
          ("other", 1),
          ("redundancyOffline", 7),
          ("unknown", 2))
    )



class ObjectStatusEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )



class RacTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16,
              17,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("idrac7modular", 17),
          ("idrac7monolithic", 16),
          ("idrac8modular", 33),
          ("idrac8monolithic", 32),
          ("other", 1),
          ("unknown", 2))
    )



class SystemFormFactorEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dualWidthFullHeight", 10),
          ("dualWidthHalfHeight", 8),
          ("other", 1),
          ("singleWidthFullHeight", 9),
          ("singleWidthHalfHeight", 7),
          ("singleWidthQuarterHeight", 11),
          ("u1", 3),
          ("u1FullWidth", 15),
          ("u1HalfWidth", 13),
          ("u1QuarterWidth", 14),
          ("u2", 4),
          ("u4", 5),
          ("u5", 12),
          ("u7", 6),
          ("unknown", 2))
    )



class BladeGeometryEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dualWidthFullHeight", 6),
          ("dualWidthHalfHeight", 4),
          ("other", 1),
          ("singleWidthFullHeight", 5),
          ("singleWidthHalfHeight", 3),
          ("singleWidthQuarterHeight", 7),
          ("u1FullWidth", 10),
          ("u1HalfWidth", 8),
          ("u1QuarterWidth", 9),
          ("unknown", 2))
    )



class PowerStateStatusEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("off", 3),
          ("on", 4),
          ("other", 1),
          ("unknown", 2))
    )



class StateCapabilitiesLogUniqueFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notReadyCapable", 4),
          ("onlineCapable", 2),
          ("resetCapable", 8),
          ("unknown", 1))
    )



class StateSettingsLogUniqueFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 4),
          ("online", 2),
          ("reset", 8),
          ("unknown", 1))
    )



class LogFormatType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("raw", 1),
          ("uniCode", 3))
    )



class ChassisTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("allInOne", 13),
          ("busExpansionChassis", 20),
          ("desktop", 3),
          ("dockingStation", 12),
          ("expansionChassis", 18),
          ("handHeld", 11),
          ("lapTop", 9),
          ("lowProfileDesktop", 4),
          ("lunchBox", 16),
          ("mainSystemChassis", 17),
          ("miniTower", 6),
          ("multiSystemChassis", 25),
          ("noteBook", 10),
          ("other", 1),
          ("peripheralChassis", 21),
          ("pizzaBox", 5),
          ("portable", 8),
          ("rackMountChassis", 23),
          ("raidChassis", 22),
          ("sealedCasePC", 24),
          ("spaceSaving", 15),
          ("subChassis", 19),
          ("subNoteBook", 14),
          ("tower", 7),
          ("unknown", 2))
    )



class ChassisSystemClassEnum(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("desktopClass", 5),
          ("netPCClass", 7),
          ("other", 1),
          ("portableClass", 6),
          ("serverClass", 4),
          ("storageClass", 8),
          ("unknown", 2),
          ("workstationClass", 3))
    )



class LEDControlCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alertOnErrorCapable", 2),
          ("alertOnWarningAndErrorCapable", 4),
          ("alertOnWarningOrErrorCapable", 6),
          ("unknown", 1))
    )



class LEDControlSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alertOnError", 2),
          ("alertOnWarningAndError", 4),
          ("unknown", 1))
    )



class ChassisIdentifyControlCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("enableCapable", 2),
          ("identifyCapable", 8),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )



class ChassisIdentifyControlSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("identifyChassis", 8),
          ("identifyChassisAndEnable", 10),
          ("notReady", 4),
          ("unknown", 1))
    )



class HostControlCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7,
              8,
              15,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("manualAllExceptOperatingSystemShutdownCapable", 7),
          ("manualFullyCapable", 15),
          ("manualOperatingSystemShutdownCapable", 8),
          ("manualPowerCycleCapable", 4),
          ("manualPowerCycleWithOSShutdownCapable", 256),
          ("manualPowerCycleWithoutOSShutdownCapable", 512),
          ("manualPowerOFFCapable", 2),
          ("manualPowerOffWithOSShutdownCapable", 64),
          ("manualPowerOffWithoutOSShutdownCapable", 128),
          ("manualRebootCapable", 1),
          ("manualRebootWithOSShutdownCapable", 16),
          ("manualRebootWithoutOSShutdownCapable", 32))
    )



class HostControlSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              9,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("manualOperatingSystemShutdown", 8),
          ("manualOperatingSystemShutdownThenPowerCycle", 12),
          ("manualOperatingSystemShutdownThenPowerOFF", 10),
          ("manualOperatingSystemShutdownThenReboot", 9),
          ("manualPowerCycle", 4),
          ("manualPowerOFF", 2),
          ("manualReboot", 1))
    )



class WatchDogControlCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              27,
              31)
        )
    )
    namedValues = NamedValues(
        *(("automaticAllExceptNotificationCapable", 27),
          ("automaticFullyCapable", 31),
          ("automaticNotificationCapable", 4),
          ("automaticPowerCycleCapable", 2),
          ("automaticPowerOffCapable", 16),
          ("automaticRebootCapable", 1),
          ("automaticWatchDogTimerCapable", 8))
    )



class WatchControlSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("automaticNotificationEnabled", 4),
          ("automaticPowerCycleEnabled", 2),
          ("automaticPowerOffEnabled", 8),
          ("automaticRebootEnabled", 1))
    )



class WatchDogTimerCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("type1Capable", 1),
          ("type2Capable", 2),
          ("type3Capable", 4))
    )



class PowerButtonControlCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableCapable", 2),
          ("unknownCapabilities", 1))
    )



class PowerButtonControlSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 2),
          ("unknown", 1))
    )



class NMIButtonControlCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableCapable", 2),
          ("unknownCapabilities", 1))
    )



class NMIButtonControlSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 2),
          ("unknown", 1))
    )



class SystemPropertiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("energySmart", 1)
    )



class FirmwareType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("iDRAC7", 21),
          ("iDRAC8", 22),
          ("lifecycleController", 20),
          ("other", 1),
          ("unknown", 2))
    )



class IntrusionReadingEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("chassisBreachSensorFailure", 4),
          ("chassisBreached", 2),
          ("chassisBreachedPrior", 3),
          ("chassisNotBreached", 1))
    )



class IntrusionTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassisBreachDetectionWhenPowerOFF", 2),
          ("chassisBreachDetectionWhenPowerON", 1))
    )



class LcLogCategoryEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("audit", 4),
          ("configuration", 5),
          ("storage", 2),
          ("system", 1),
          ("updates", 3),
          ("workNotes", 6))
    )



class PowerSupplyStateCapabilitiesUniqueFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notReadyCapable", 4),
          ("onlineCapable", 2),
          ("unknown", 1))
    )



class PowerSupplyStateSettingsUniqueFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              32,
              64,
              66,
              128,
              130,
              210,
              242)
        )
    )
    namedValues = NamedValues(
        *(("acPowerAndSwitchAreOnPowerSupplyIsOnIsOkAndOnline", 242),
          ("acPowerIsON", 128),
          ("acSwitchIsON", 64),
          ("fanFailure", 8),
          ("notReady", 4),
          ("onLine", 2),
          ("onlineAndAcPowerIsON", 130),
          ("onlineAndFanFailure", 10),
          ("onlineAndPredictiveFailure", 210),
          ("onlineandAcSwitchIsON", 66),
          ("powerSupplyIsOK", 32),
          ("powerSupplyIsON", 16),
          ("unknown", 1))
    )



class PowerSupplyTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyTypeIsAC", 9),
          ("powerSupplyTypeIsBattery", 5),
          ("powerSupplyTypeIsConverter", 7),
          ("powerSupplyTypeIsDC", 10),
          ("powerSupplyTypeIsLinear", 3),
          ("powerSupplyTypeIsOther", 1),
          ("powerSupplyTypeIsRegulator", 8),
          ("powerSupplyTypeIsSwitching", 4),
          ("powerSupplyTypeIsUPS", 6),
          ("powerSupplyTypeIsUnknown", 2),
          ("powerSupplyTypeIsVRM", 11))
    )



class PowerSupplySensorStateFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("acLostOrOutOfRange", 16),
          ("acOutOfRangeButPresent", 32),
          ("configurationError", 64),
          ("predictiveFailure", 4),
          ("presenceDetected", 1),
          ("psACLost", 8),
          ("psFailureDetected", 2))
    )



class PowerSupplyConfigurationErrorTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("processorMissing", 3),
          ("revisionMismatch", 2),
          ("vendorMismatch", 1))
    )



class VoltageTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("voltageProbeTypeIs12Volt", 7),
          ("voltageProbeTypeIs1Point5Volt", 3),
          ("voltageProbeTypeIs2Point5Volt", 14),
          ("voltageProbeTypeIs3Point3Volt", 4),
          ("voltageProbeTypeIs5Volt", 5),
          ("voltageProbeTypeIsBattery", 12),
          ("voltageProbeTypeIsCore", 10),
          ("voltageProbeTypeIsDiscrete", 16),
          ("voltageProbeTypeIsFLEA", 11),
          ("voltageProbeTypeIsGTL", 15),
          ("voltageProbeTypeIsGenericDiscrete", 17),
          ("voltageProbeTypeIsIO", 9),
          ("voltageProbeTypeIsMemoryStatus", 19),
          ("voltageProbeTypeIsMinus12Volt", 8),
          ("voltageProbeTypeIsMinus5Volt", 6),
          ("voltageProbeTypeIsOther", 1),
          ("voltageProbeTypeIsPSVoltage", 18),
          ("voltageProbeTypeIsTerminator", 13),
          ("voltageProbeTypeIsUnknown", 2))
    )



class VoltageDiscreteReadingEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voltageIsBad", 2),
          ("voltageIsGood", 1))
    )



class AmperageProbeTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("amperageProbeTypeIs12Volt", 7),
          ("amperageProbeTypeIs1Point5Volt", 3),
          ("amperageProbeTypeIs2Point5Volt", 14),
          ("amperageProbeTypeIs3Point3volt", 4),
          ("amperageProbeTypeIs5Volt", 5),
          ("amperageProbeTypeIsBattery", 12),
          ("amperageProbeTypeIsCore", 10),
          ("amperageProbeTypeIsDiscrete", 16),
          ("amperageProbeTypeIsFLEA", 11),
          ("amperageProbeTypeIsGTL", 15),
          ("amperageProbeTypeIsIO", 9),
          ("amperageProbeTypeIsMinus12Volt", 8),
          ("amperageProbeTypeIsMinus5Volt", 6),
          ("amperageProbeTypeIsOther", 1),
          ("amperageProbeTypeIsPowerSupplyAmps", 23),
          ("amperageProbeTypeIsPowerSupplyWatts", 24),
          ("amperageProbeTypeIsSystemAmps", 25),
          ("amperageProbeTypeIsSystemWatts", 26),
          ("amperageProbeTypeIsTerminator", 13),
          ("amperageProbeTypeIsUnknown", 2))
    )



class AmperageDiscreteReadingEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("amperageIsBad", 2),
          ("amperageIsGood", 1))
    )



class SystemBatteryReadingFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("predictiveFailure", 1),
          ("presenceDetected", 4))
    )



class PowerCapCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
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



class PowerCapSettingEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )



class CoolingDeviceTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("coolingDeviceTypeIsABlower", 4),
          ("coolingDeviceTypeIsACabinetFan", 6),
          ("coolingDeviceTypeIsAChipFan", 5),
          ("coolingDeviceTypeIsAFan", 3),
          ("coolingDeviceTypeIsAHeatPipe", 8),
          ("coolingDeviceTypeIsAPowerSupplyFan", 7),
          ("coolingDeviceTypeIsActiveCooling", 10),
          ("coolingDeviceTypeIsOther", 1),
          ("coolingDeviceTypeIsPassiveCooling", 11),
          ("coolingDeviceTypeIsRefrigeration", 9),
          ("coolingDeviceTypeIsUnknown", 2))
    )



class CoolingDeviceSubTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              16)
        )
    )
    namedValues = NamedValues(
        *(("coolingDeviceSubTypeIsAFanReadsONorOFF", 4),
          ("coolingDeviceSubTypeIsAFanThatReadsInRPM", 3),
          ("coolingDeviceSubTypeIsAPowerSupplyFanThatReadsONorOFF", 6),
          ("coolingDeviceSubTypeIsAPowerSupplyFanThatReadsinRPM", 5),
          ("coolingDeviceSubTypeIsDiscrete", 16),
          ("coolingDeviceSubTypeIsOther", 1),
          ("coolingDeviceSubTypeIsUnknown", 2))
    )



class CoolingDeviceDiscreteReadingEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coolingDeviceIsBad", 2),
          ("coolingDeviceIsGood", 1))
    )



class TemperatureProbeTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16)
        )
    )
    namedValues = NamedValues(
        *(("temperatureProbeTypeIsAmbientESM", 3),
          ("temperatureProbeTypeIsDiscrete", 16),
          ("temperatureProbeTypeIsOther", 1),
          ("temperatureProbeTypeIsUnknown", 2))
    )



class TemperatureDiscreteReadingEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureIsBad", 2),
          ("temperatureIsGood", 1))
    )



class ProcessorDeviceType(Integer32, TextualConvention):
    status = "current"
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
        *(("deviceTypeIsAVideoProcessor", 6),
          ("deviceTypeIsCPU", 3),
          ("deviceTypeIsDSP", 5),
          ("deviceTypeIsMathProcessor", 4),
          ("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2))
    )



class ProcessorDeviceFamily(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              64,
              65,
              66,
              67,
              68,
              69,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              96,
              97,
              98,
              99,
              100,
              101,
              112,
              120,
              121,
              122,
              128,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              179,
              180,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              221,
              222,
              223,
              224,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              250,
              251)
        )
    )
    namedValues = NamedValues(
        *(("deviceFamilyIs68000", 98),
          ("deviceFamilyIs68010", 99),
          ("deviceFamilyIs68020", 100),
          ("deviceFamilyIs68030", 101),
          ("deviceFamilyIs68040", 96),
          ("deviceFamilyIs68xxx", 97),
          ("deviceFamilyIs80286", 4),
          ("deviceFamilyIs80287", 8),
          ("deviceFamilyIs80387", 9),
          ("deviceFamilyIs80487", 10),
          ("deviceFamilyIs8086", 3),
          ("deviceFamilyIs8087", 7),
          ("deviceFamilyIsAMD2900", 30),
          ("deviceFamilyIsAMDAthlon", 29),
          ("deviceFamilyIsAMDAthlon64", 131),
          ("deviceFamilyIsAMDAthlon64X2DualCore", 136),
          ("deviceFamilyIsAMDAthlonDualCore", 234),
          ("deviceFamilyIsAMDAthlonII", 237),
          ("deviceFamilyIsAMDAthlonIIDualMobileM", 58),
          ("deviceFamilyIsAMDAthlonMP", 183),
          ("deviceFamilyIsAMDAthlonX2DualCore", 143),
          ("deviceFamilyIsAMDAthlonXP", 182),
          ("deviceFamilyIsAMDDuron", 184),
          ("deviceFamilyIsAMDOpteron", 132),
          ("deviceFamilyIsAMDOpteron4100", 60),
          ("deviceFamilyIsAMDOpteron4200", 62),
          ("deviceFamilyIsAMDOpteron6100", 59),
          ("deviceFamilyIsAMDOpteron6200", 61),
          ("deviceFamilyIsAMDPhenomFXQuadCore", 140),
          ("deviceFamilyIsAMDPhenomII", 236),
          ("deviceFamilyIsAMDPhenomTripleCore", 231),
          ("deviceFamilyIsAMDPhenomX2DualCore", 142),
          ("deviceFamilyIsAMDPhenomX4QuadCore", 141),
          ("deviceFamilyIsAMDSempron", 133),
          ("deviceFamilyIsAMDSempronM", 239),
          ("deviceFamilyIsAMDSempronSI", 235),
          ("deviceFamilyIsAMDTurion64Mobile", 134),
          ("deviceFamilyIsAMDTurion64X2Mobile", 137),
          ("deviceFamilyIsAMDTurionDualCoreMobile", 233),
          ("deviceFamilyIsAMDTurionIIDualMobileM", 57),
          ("deviceFamilyIsAMDTurionIIUltraDualMobileM", 56),
          ("deviceFamilyIsAMDTurionUltraDualCoreMobile", 232),
          ("deviceFamilyIsAS400", 180),
          ("deviceFamilyIsAlpha", 48),
          ("deviceFamilyIsAlpha21064", 49),
          ("deviceFamilyIsAlpha21066", 50),
          ("deviceFamilyIsAlpha21164", 51),
          ("deviceFamilyIsAlpha21164PC", 52),
          ("deviceFamilyIsAlpha21164a", 53),
          ("deviceFamilyIsAlpha21264", 54),
          ("deviceFamilyIsAlpha21364", 55),
          ("deviceFamilyIsCeleron", 15),
          ("deviceFamilyIsCrusoeTM3000", 121),
          ("deviceFamilyIsCrusoeTM5000", 120),
          ("deviceFamilyIsDualCoreAMDOpteron", 135),
          ("deviceFamilyIsDualCoreIntelCeleron", 199),
          ("deviceFamilyIsDualCoreIntelXeon3000", 162),
          ("deviceFamilyIsDualCoreIntelXeon3xxx", 215),
          ("deviceFamilyIsDualCoreIntelXeon5000", 165),
          ("deviceFamilyIsDualCoreIntelXeon5100", 164),
          ("deviceFamilyIsDualCoreIntelXeon5200", 171),
          ("deviceFamilyIsDualCoreIntelXeon5xxx", 218),
          ("deviceFamilyIsDualCoreIntelXeon7100", 168),
          ("deviceFamilyIsDualCoreIntelXeon7200", 172),
          ("deviceFamilyIsDualCoreIntelXeon7xxx", 221),
          ("deviceFamilyIsDualCoreIntelXeonLV", 166),
          ("deviceFamilyIsDualCoreIntelXeonULV", 167),
          ("deviceFamilyIsESA390G6", 203),
          ("deviceFamilyIsEfficeonTM8000", 122),
          ("deviceFamilyIsEmbeddedAMDOpertonQuadCore", 230),
          ("deviceFamilyIsG4", 201),
          ("deviceFamilyIsG5", 202),
          ("deviceFamilyIsHobbit", 112),
          ("deviceFamilyIsIBM390", 200),
          ("deviceFamilyIsIntel386", 5),
          ("deviceFamilyIsIntel486", 6),
          ("deviceFamilyIsIntelAtom", 43),
          ("deviceFamilyIsIntelCeleronD", 186),
          ("deviceFamilyIsIntelCeleronM", 130),
          ("deviceFamilyIsIntelCore2", 190),
          ("deviceFamilyIsIntelCore2Duo", 191),
          ("deviceFamilyIsIntelCore2DuoMobile", 196),
          ("deviceFamilyIsIntelCore2Extreme", 193),
          ("deviceFamilyIsIntelCore2ExtremeMobile", 195),
          ("deviceFamilyIsIntelCore2Quad", 194),
          ("deviceFamilyIsIntelCore2Solo", 192),
          ("deviceFamilyIsIntelCore2SoloMobile", 197),
          ("deviceFamilyIsIntelCoreDuo", 40),
          ("deviceFamilyIsIntelCoreDuoMobile", 41),
          ("deviceFamilyIsIntelCoreSolo", 189),
          ("deviceFamilyIsIntelCoreSoloMobile", 42),
          ("deviceFamilyIsIntelCorei3", 206),
          ("deviceFamilyIsIntelCorei5", 205),
          ("deviceFamilyIsIntelCorei7", 198),
          ("deviceFamilyIsIntelItanium2", 24),
          ("deviceFamilyIsIntelPentium4HT", 179),
          ("deviceFamilyIsIntelPentiumD", 187),
          ("deviceFamilyIsIntelPentiumExtreme", 188),
          ("deviceFamilyIsIntelPentiumM", 185),
          ("deviceFamilyIsIntelXeon", 21),
          ("deviceFamilyIsIntelXeonMP", 23),
          ("deviceFamilyIsItanium", 20),
          ("deviceFamilyIsK5", 25),
          ("deviceFamilyIsK6", 26),
          ("deviceFamilyIsK6Dash2", 27),
          ("deviceFamilyIsK6Dash2Plus", 31),
          ("deviceFamilyIsK6Dash3", 28),
          ("deviceFamilyIsM1", 176),
          ("deviceFamilyIsM2", 177),
          ("deviceFamilyIsMIPS", 64),
          ("deviceFamilyIsMIPSR10000", 69),
          ("deviceFamilyIsMIPSR4000", 65),
          ("deviceFamilyIsMIPSR4200", 66),
          ("deviceFamilyIsMIPSR4400", 67),
          ("deviceFamilyIsMIPSR4600", 68),
          ("deviceFamilyIsMultiCoreIntelXeon", 214),
          ("deviceFamilyIsMultiCoreIntelXeon3400", 224),
          ("deviceFamilyIsMultiCoreIntelXeon7400", 175),
          ("deviceFamilyIsMultiCoreIntelXeon7xxx", 223),
          ("deviceFamilyIsOther", 1),
          ("deviceFamilyIsPARISC", 144),
          ("deviceFamilyIsPARISC7100", 150),
          ("deviceFamilyIsPARISC7100LC", 149),
          ("deviceFamilyIsPARISC7200", 148),
          ("deviceFamilyIsPARISC7300LC", 147),
          ("deviceFamilyIsPARISC8000", 146),
          ("deviceFamilyIsPARISC8500", 145),
          ("deviceFamilyIsPentium", 11),
          ("deviceFamilyIsPentium4", 22),
          ("deviceFamilyIsPentiumII", 13),
          ("deviceFamilyIsPentiumIII", 17),
          ("deviceFamilyIsPentiumIIISpeedStep", 19),
          ("deviceFamilyIsPentiumIIIXeon", 18),
          ("deviceFamilyIsPentiumIIXeon", 16),
          ("deviceFamilyIsPentiumMMX", 14),
          ("deviceFamilyIsPentiumPro", 12),
          ("deviceFamilyIsPowerPC", 32),
          ("deviceFamilyIsPowerPC601", 33),
          ("deviceFamilyIsPowerPC603", 34),
          ("deviceFamilyIsPowerPC603Plus", 35),
          ("deviceFamilyIsPowerPC604", 36),
          ("deviceFamilyIsPowerPC620", 37),
          ("deviceFamilyIsPowerPC750", 39),
          ("deviceFamilyIsPowerPCx704", 38),
          ("deviceFamilyIsQuadCoreAMDOpteron", 138),
          ("deviceFamilyIsQuadCoreIntelXeon", 170),
          ("deviceFamilyIsQuadCoreIntelXeon3200", 161),
          ("deviceFamilyIsQuadCoreIntelXeon3xxx", 216),
          ("deviceFamilyIsQuadCoreIntelXeon5300", 163),
          ("deviceFamilyIsQuadCoreIntelXeon5400", 169),
          ("deviceFamilyIsQuadCoreIntelXeon5xxx", 219),
          ("deviceFamilyIsQuadCoreIntelXeon7300", 173),
          ("deviceFamilyIsQuadCoreIntelXeon7400", 174),
          ("deviceFamilyIsQuadCoreIntelXeon7xxx", 222),
          ("deviceFamilyIsSPARC", 80),
          ("deviceFamilyIsSixCoreAMDOpteron", 238),
          ("deviceFamilyIsSuperSPARC", 81),
          ("deviceFamilyIsThirdGenerationAMDOpteron", 139),
          ("deviceFamilyIsUltraSPARC", 84),
          ("deviceFamilyIsUltraSPARCII", 85),
          ("deviceFamilyIsUltraSPARCIII", 87),
          ("deviceFamilyIsUltraSPARCIIIi", 88),
          ("deviceFamilyIsUltraSPARCIIi", 86),
          ("deviceFamilyIsUnknown", 2),
          ("deviceFamilyIsV30", 160),
          ("deviceFamilyIsVIAC7", 212),
          ("deviceFamilyIsVIAC7D", 211),
          ("deviceFamilyIsVIAC7M", 210),
          ("deviceFamilyIsVIAEden", 213),
          ("deviceFamilyIsVIANano", 217),
          ("deviceFamilyIsWeitek", 128),
          ("deviceFamilyIsi860", 250),
          ("deviceFamilyIsi960", 251),
          ("deviceFamilyIsmicroSPARCII", 82),
          ("deviceFamilyIsmicroSPARCIIep", 83),
          ("deviceFamilyIszArchitectur", 204))
    )



class ProcessorDeviceStatusState(Integer32, TextualConvention):
    status = "current"
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
        *(("biosDisabled", 5),
          ("enabled", 3),
          ("idle", 6),
          ("other", 1),
          ("unknown", 2),
          ("userDisabled", 4))
    )



class ProcessorDeviceStatusReadingFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              32,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("configurationError", 32),
          ("internalError", 1),
          ("processorDisabled", 256),
          ("processorPresent", 128),
          ("processorThrottled", 1024),
          ("terminatorPresent", 512),
          ("thermalTrip", 2))
    )



class MemoryDeviceTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("deviceTypeIs3DRAM", 14),
          ("deviceTypeIsCDRAM", 13),
          ("deviceTypeIsDDR", 18),
          ("deviceTypeIsDDR2", 19),
          ("deviceTypeIsDDR2FBDIMM", 20),
          ("deviceTypeIsDDR3", 24),
          ("deviceTypeIsDDR4", 26),
          ("deviceTypeIsDRAM", 3),
          ("deviceTypeIsEDRAM", 4),
          ("deviceTypeIsEEPROM", 10),
          ("deviceTypeIsEPROM", 12),
          ("deviceTypeIsFBD2", 25),
          ("deviceTypeIsFEPROM", 11),
          ("deviceTypeIsFLASH", 9),
          ("deviceTypeIsOther", 1),
          ("deviceTypeIsRAM", 7),
          ("deviceTypeIsRDRAM", 17),
          ("deviceTypeIsROM", 8),
          ("deviceTypeIsSDRAM", 15),
          ("deviceTypeIsSGRAM", 16),
          ("deviceTypeIsSRAM", 6),
          ("deviceTypeIsUnknown", 2),
          ("deviceTypeIsVRAM", 5))
    )



class NetworkDeviceConnectionStatusEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2),
          ("driverBad", 3),
          ("driverDisabled", 4),
          ("hardwareClosing", 12),
          ("hardwareInitalizing", 10),
          ("hardwareNotReady", 13),
          ("hardwareResetting", 11))
    )



class NetworkDeviceTOECapabilityFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("cannotBeDetermined", 8),
          ("driverNotResponding", 16),
          ("notAvailable", 4),
          ("unknown", 1))
    )



class NetworkDeviceiSCSICapabilityFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("cannotBeDetermined", 8),
          ("driverNotResponding", 16),
          ("notAvailable", 4),
          ("unknown", 1))
    )



class NetworkDeviceCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fcoeOffload", 8),
          ("iscsiOffload", 4),
          ("supported", 1),
          ("toe", 2))
    )



class SystemSlotStateCapabilitiesFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              126,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32640,
              32766)
        )
    )
    namedValues = NamedValues(
        *(("canSupportAllHotPlugCapabilities", 126),
          ("canSupportAllSlotAndAllHotPlugCapabilities", 32766),
          ("canSupportAllSlotCapabilities", 32640),
          ("systemSlotCanProvide3Point3Volts", 256),
          ("systemSlotCanProvide5Volts", 128),
          ("systemSlotCanSignalIfShared", 512),
          ("systemSlotCanSupportCard16", 1024),
          ("systemSlotCanSupportCardBus", 2048),
          ("systemSlotCanSupportModemRingResume", 8192),
          ("systemSlotCanSupportPMESignal", 16384),
          ("systemSlotCanSupportZoomVideo", 4096),
          ("systemSlotHotPlugCanBePoweredOn", 4),
          ("systemSlotHotPlugCanSignalAdapterPresent", 32),
          ("systemSlotHotPlugCanSignalAttention", 8),
          ("systemSlotHotPlugCanSignalPowerButtonPressed", 64),
          ("systemSlotHotPlugCanSignalPowerFault", 16),
          ("systemSlotHotPlugIsHotPluggableCapable", 2),
          ("systemSlotHotPlugIsUnknown", 1))
    )



class SystemSlotStateSettingsFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              36,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              16770,
              16804,
              16806,
              17316)
        )
    )
    namedValues = NamedValues(
        *(("supportsPMEand3P3VIsSharedand5VhasAdapterOnandHotPlugable", 17316),
          ("supportsPMEand3P3Vand5VandHotPluggable", 16770),
          ("supportsPMEand3P3Vand5VhasAdapterOn", 16804),
          ("supportsPMEand3P3Vand5VhasAdapterOnandisHotPluggable", 16806),
          ("systemSlotHotPlugAdapterIsPresent", 32),
          ("systemSlotHotPlugAdapterPresentAndPoweredOn", 36),
          ("systemSlotHotPlugHasPowerFaulted", 16),
          ("systemSlotHotPlugIsAtAttention", 8),
          ("systemSlotHotPlugIsHotPluggable", 2),
          ("systemSlotHotPlugIsPoweredOn", 4),
          ("systemSlotHotPlugIsUnknown", 1),
          ("systemSlotHotPlugPowerButtonPressed", 64),
          ("systemSlotIsShared", 512),
          ("systemSlotProvides3Point3Volts", 256),
          ("systemSlotProvides5Volts", 128),
          ("systemSlotSupportsCard16", 1024),
          ("systemSlotSupportsCardBus", 2048),
          ("systemSlotSupportsModemRingResume", 8192),
          ("systemSlotSupportsPMESignal", 16384),
          ("systemSlotSupportsZoomVideo", 4096))
    )



class SystemSlotTypeEnum(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176)
        )
    )
    namedValues = NamedValues(
        *(("systemSlotIsAGP", 15),
          ("systemSlotIsAGP2X", 16),
          ("systemSlotIsAGP4X", 17),
          ("systemSlotIsAGP8X", 25),
          ("systemSlotIsEISA", 5),
          ("systemSlotIsIORiserCard", 12),
          ("systemSlotIsISA", 3),
          ("systemSlotIsMCA", 4),
          ("systemSlotIsNuBUS", 13),
          ("systemSlotIsOther", 1),
          ("systemSlotIsPC98C20", 18),
          ("systemSlotIsPC98C24", 19),
          ("systemSlotIsPC98Card", 22),
          ("systemSlotIsPC98E", 20),
          ("systemSlotIsPC98LocalBus", 21),
          ("systemSlotIsPCI", 6),
          ("systemSlotIsPCI66MHz", 14),
          ("systemSlotIsPCIExpress", 24),
          ("systemSlotIsPCIExpressGen2", 171),
          ("systemSlotIsPCIExpressGen2X1", 172),
          ("systemSlotIsPCIExpressGen2X16", 176),
          ("systemSlotIsPCIExpressGen2X2", 173),
          ("systemSlotIsPCIExpressGen2X4", 174),
          ("systemSlotIsPCIExpressGen2X8", 175),
          ("systemSlotIsPCIExpressX1", 166),
          ("systemSlotIsPCIExpressX16", 170),
          ("systemSlotIsPCIExpressX2", 167),
          ("systemSlotIsPCIExpressX4", 168),
          ("systemSlotIsPCIExpressX8", 169),
          ("systemSlotIsPCIX", 23),
          ("systemSlotIsPCMCIA", 7),
          ("systemSlotIsProcessorCard", 10),
          ("systemSlotIsProprietary", 9),
          ("systemSlotIsProprietaryMemory", 11),
          ("systemSlotIsUnknown", 2),
          ("systemSlotIsVLVESA", 8))
    )



class SystemSlotUsageEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("systemSlotUsageIsAvailable", 3),
          ("systemSlotUsageIsInUse", 4),
          ("systemSlotUsageIsOther", 1),
          ("systemSlotUsageIsUnknown", 2))
    )



class SystemSlotCategoryEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("systemSlotCategoryIsBusConnector", 3),
          ("systemSlotCategoryIsMotherboard", 5),
          ("systemSlotCategoryIsOther", 1),
          ("systemSlotCategoryIsPCMCIA", 4),
          ("systemSlotCategoryIsUnknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_InformationGroup_ObjectIdentity = ObjectIdentity
informationGroup = _InformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1)
)
_RacInfoGroup_ObjectIdentity = ObjectIdentity
racInfoGroup = _RacInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1)
)
_RacName_Type = StringType
_RacName_Object = MibScalar
racName = _RacName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 1),
    _RacName_Type()
)
racName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racName.setStatus("current")
_RacShortName_Type = StringType
_RacShortName_Object = MibScalar
racShortName = _RacShortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 2),
    _RacShortName_Type()
)
racShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racShortName.setStatus("current")
_RacDescription_Type = StringType
_RacDescription_Object = MibScalar
racDescription = _RacDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 3),
    _RacDescription_Type()
)
racDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racDescription.setStatus("current")
_RacManufacturer_Type = StringType
_RacManufacturer_Object = MibScalar
racManufacturer = _RacManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 4),
    _RacManufacturer_Type()
)
racManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racManufacturer.setStatus("current")
_RacVersion_Type = StringType
_RacVersion_Object = MibScalar
racVersion = _RacVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 5),
    _RacVersion_Type()
)
racVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racVersion.setStatus("current")
_RacURL_Type = StringType
_RacURL_Object = MibScalar
racURL = _RacURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 6),
    _RacURL_Type()
)
racURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racURL.setStatus("current")
_RacType_Type = RacTypeEnum
_RacType_Object = MibScalar
racType = _RacType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 7),
    _RacType_Type()
)
racType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racType.setStatus("current")
_RacFirmwareVersion_Type = StringType
_RacFirmwareVersion_Object = MibScalar
racFirmwareVersion = _RacFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 1, 8),
    _RacFirmwareVersion_Type()
)
racFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    racFirmwareVersion.setStatus("current")
_ChassisInfoGroup_ObjectIdentity = ObjectIdentity
chassisInfoGroup = _ChassisInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 2)
)
_ChassisServiceTag_Type = StringType
_ChassisServiceTag_Object = MibScalar
chassisServiceTag = _ChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 2, 1),
    _ChassisServiceTag_Type()
)
chassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisServiceTag.setStatus("current")
_ChassisNameModular_Type = StringType
_ChassisNameModular_Object = MibScalar
chassisNameModular = _ChassisNameModular_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 2, 2),
    _ChassisNameModular_Type()
)
chassisNameModular.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNameModular.setStatus("current")
_ChassisModelModular_Type = StringType
_ChassisModelModular_Object = MibScalar
chassisModelModular = _ChassisModelModular_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 2, 3),
    _ChassisModelModular_Type()
)
chassisModelModular.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModelModular.setStatus("current")
_SystemInfoGroup_ObjectIdentity = ObjectIdentity
systemInfoGroup = _SystemInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3)
)
_SystemFQDN_Type = StringType
_SystemFQDN_Object = MibScalar
systemFQDN = _SystemFQDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 1),
    _SystemFQDN_Type()
)
systemFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFQDN.setStatus("current")
_SystemServiceTag_Type = StringType
_SystemServiceTag_Object = MibScalar
systemServiceTag = _SystemServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 2),
    _SystemServiceTag_Type()
)
systemServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServiceTag.setStatus("current")
_SystemExpressServiceCode_Type = StringType
_SystemExpressServiceCode_Object = MibScalar
systemExpressServiceCode = _SystemExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 3),
    _SystemExpressServiceCode_Type()
)
systemExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemExpressServiceCode.setStatus("current")
_SystemAssetTag_Type = StringType
_SystemAssetTag_Object = MibScalar
systemAssetTag = _SystemAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 4),
    _SystemAssetTag_Type()
)
systemAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAssetTag.setStatus("current")
_SystemBladeSlotNumber_Type = StringType
_SystemBladeSlotNumber_Object = MibScalar
systemBladeSlotNumber = _SystemBladeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 5),
    _SystemBladeSlotNumber_Type()
)
systemBladeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBladeSlotNumber.setStatus("current")
_SystemOSName_Type = StringType
_SystemOSName_Object = MibScalar
systemOSName = _SystemOSName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 6),
    _SystemOSName_Type()
)
systemOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOSName.setStatus("current")
_SystemFormFactor_Type = SystemFormFactorEnum
_SystemFormFactor_Object = MibScalar
systemFormFactor = _SystemFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 7),
    _SystemFormFactor_Type()
)
systemFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFormFactor.setStatus("current")
_SystemDataCenterName_Type = StringType
_SystemDataCenterName_Object = MibScalar
systemDataCenterName = _SystemDataCenterName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 8),
    _SystemDataCenterName_Type()
)
systemDataCenterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDataCenterName.setStatus("current")
_SystemAisleName_Type = StringType
_SystemAisleName_Object = MibScalar
systemAisleName = _SystemAisleName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 9),
    _SystemAisleName_Type()
)
systemAisleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAisleName.setStatus("current")
_SystemRackName_Type = StringType
_SystemRackName_Object = MibScalar
systemRackName = _SystemRackName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 10),
    _SystemRackName_Type()
)
systemRackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRackName.setStatus("current")
_SystemRackSlot_Type = StringType
_SystemRackSlot_Object = MibScalar
systemRackSlot = _SystemRackSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 11),
    _SystemRackSlot_Type()
)
systemRackSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRackSlot.setStatus("current")
_SystemModelName_Type = StringType
_SystemModelName_Object = MibScalar
systemModelName = _SystemModelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 12),
    _SystemModelName_Type()
)
systemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModelName.setStatus("current")
_SystemSystemID_Type = Unsigned16BitRange
_SystemSystemID_Object = MibScalar
systemSystemID = _SystemSystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 13),
    _SystemSystemID_Type()
)
systemSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSystemID.setStatus("current")
_SystemOSVersion_Type = StringType
_SystemOSVersion_Object = MibScalar
systemOSVersion = _SystemOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 14),
    _SystemOSVersion_Type()
)
systemOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOSVersion.setStatus("current")
_SystemRoomName_Type = StringType
_SystemRoomName_Object = MibScalar
systemRoomName = _SystemRoomName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 15),
    _SystemRoomName_Type()
)
systemRoomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRoomName.setStatus("current")
_SystemChassisSystemHeight_Type = Unsigned8BitRange
_SystemChassisSystemHeight_Object = MibScalar
systemChassisSystemHeight = _SystemChassisSystemHeight_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 16),
    _SystemChassisSystemHeight_Type()
)
systemChassisSystemHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChassisSystemHeight.setStatus("current")
_SystemBladeGeometry_Type = BladeGeometryEnum
_SystemBladeGeometry_Object = MibScalar
systemBladeGeometry = _SystemBladeGeometry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 17),
    _SystemBladeGeometry_Type()
)
systemBladeGeometry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBladeGeometry.setStatus("current")
_SystemNodeID_Type = StringType
_SystemNodeID_Object = MibScalar
systemNodeID = _SystemNodeID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 1, 3, 18),
    _SystemNodeID_Type()
)
systemNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNodeID.setStatus("current")
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 2)
)
_GlobalSystemStatus_Type = ObjectStatusEnum
_GlobalSystemStatus_Object = MibScalar
globalSystemStatus = _GlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 2, 1),
    _GlobalSystemStatus_Type()
)
globalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalSystemStatus.setStatus("current")
_SystemLCDStatus_Type = ObjectStatusEnum
_SystemLCDStatus_Object = MibScalar
systemLCDStatus = _SystemLCDStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 2, 2),
    _SystemLCDStatus_Type()
)
systemLCDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLCDStatus.setStatus("current")
_GlobalStorageStatus_Type = ObjectStatusEnum
_GlobalStorageStatus_Object = MibScalar
globalStorageStatus = _GlobalStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 2, 3),
    _GlobalStorageStatus_Type()
)
globalStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStorageStatus.setStatus("current")
_SystemPowerState_Type = PowerStateStatusEnum
_SystemPowerState_Object = MibScalar
systemPowerState = _SystemPowerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 2, 4),
    _SystemPowerState_Type()
)
systemPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerState.setStatus("current")
_SystemPowerUpTime_Type = Unsigned32BitRange
_SystemPowerUpTime_Object = MibScalar
systemPowerUpTime = _SystemPowerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 2, 5),
    _SystemPowerUpTime_Type()
)
systemPowerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerUpTime.setStatus("current")
_AlertGroup_ObjectIdentity = ObjectIdentity
alertGroup = _AlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3)
)
_AlertVariablesGroup_ObjectIdentity = ObjectIdentity
alertVariablesGroup = _AlertVariablesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1)
)


class _AlertMessageID_Type(OctetString):
    """Custom type alertMessageID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlertMessageID_Type.__name__ = "OctetString"
_AlertMessageID_Object = MibScalar
alertMessageID = _AlertMessageID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 1),
    _AlertMessageID_Type()
)
alertMessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessageID.setStatus("current")
_AlertMessage_Type = StringType
_AlertMessage_Object = MibScalar
alertMessage = _AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 2),
    _AlertMessage_Type()
)
alertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessage.setStatus("current")
_AlertCurrentStatus_Type = ObjectStatusEnum
_AlertCurrentStatus_Object = MibScalar
alertCurrentStatus = _AlertCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 3),
    _AlertCurrentStatus_Type()
)
alertCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCurrentStatus.setStatus("current")


class _AlertSystemServiceTag_Type(OctetString):
    """Custom type alertSystemServiceTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlertSystemServiceTag_Type.__name__ = "OctetString"
_AlertSystemServiceTag_Object = MibScalar
alertSystemServiceTag = _AlertSystemServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 4),
    _AlertSystemServiceTag_Type()
)
alertSystemServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSystemServiceTag.setStatus("current")
_AlertSystemFQDN_Type = StringType
_AlertSystemFQDN_Object = MibScalar
alertSystemFQDN = _AlertSystemFQDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 5),
    _AlertSystemFQDN_Type()
)
alertSystemFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSystemFQDN.setStatus("current")


class _AlertFQDD_Type(OctetString):
    """Custom type alertFQDD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AlertFQDD_Type.__name__ = "OctetString"
_AlertFQDD_Object = MibScalar
alertFQDD = _AlertFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 6),
    _AlertFQDD_Type()
)
alertFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertFQDD.setStatus("current")


class _AlertDeviceDisplayName_Type(OctetString):
    """Custom type alertDeviceDisplayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AlertDeviceDisplayName_Type.__name__ = "OctetString"
_AlertDeviceDisplayName_Object = MibScalar
alertDeviceDisplayName = _AlertDeviceDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 7),
    _AlertDeviceDisplayName_Type()
)
alertDeviceDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertDeviceDisplayName.setStatus("current")
_AlertMessageArguments_Type = StringType
_AlertMessageArguments_Object = MibScalar
alertMessageArguments = _AlertMessageArguments_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 8),
    _AlertMessageArguments_Type()
)
alertMessageArguments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessageArguments.setStatus("current")


class _AlertChassisServiceTag_Type(OctetString):
    """Custom type alertChassisServiceTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlertChassisServiceTag_Type.__name__ = "OctetString"
_AlertChassisServiceTag_Object = MibScalar
alertChassisServiceTag = _AlertChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 9),
    _AlertChassisServiceTag_Type()
)
alertChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertChassisServiceTag.setStatus("current")


class _AlertChassisName_Type(OctetString):
    """Custom type alertChassisName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertChassisName_Type.__name__ = "OctetString"
_AlertChassisName_Object = MibScalar
alertChassisName = _AlertChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 10),
    _AlertChassisName_Type()
)
alertChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertChassisName.setStatus("current")
_AlertRacFQDN_Type = StringType
_AlertRacFQDN_Object = MibScalar
alertRacFQDN = _AlertRacFQDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 1, 11),
    _AlertRacFQDN_Type()
)
alertRacFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertRacFQDN.setStatus("current")
_AlertTrapGroup_ObjectIdentity = ObjectIdentity
alertTrapGroup = _AlertTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2)
)
_SystemAlertTrapGroup_ObjectIdentity = ObjectIdentity
systemAlertTrapGroup = _SystemAlertTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1)
)
_StorageAlertTrapGroup_ObjectIdentity = ObjectIdentity
storageAlertTrapGroup = _StorageAlertTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2)
)
_UpdatesAlertTrapGroup_ObjectIdentity = ObjectIdentity
updatesAlertTrapGroup = _UpdatesAlertTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 3)
)
_AuditAlertTrapGroup_ObjectIdentity = ObjectIdentity
auditAlertTrapGroup = _AuditAlertTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4)
)
_ConfigurationAlertTrapGroup_ObjectIdentity = ObjectIdentity
configurationAlertTrapGroup = _ConfigurationAlertTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5)
)
_SystemDetailsGroup_ObjectIdentity = ObjectIdentity
systemDetailsGroup = _SystemDetailsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4)
)
_MIBVersionGroup_ObjectIdentity = ObjectIdentity
mIBVersionGroup = _MIBVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1)
)
_MIBMajorVersionNumber_Type = Unsigned8BitRange
_MIBMajorVersionNumber_Object = MibScalar
mIBMajorVersionNumber = _MIBMajorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1, 1),
    _MIBMajorVersionNumber_Type()
)
mIBMajorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMajorVersionNumber.setStatus("current")
_MIBMinorVersionNumber_Type = Unsigned8BitRange
_MIBMinorVersionNumber_Object = MibScalar
mIBMinorVersionNumber = _MIBMinorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1, 2),
    _MIBMinorVersionNumber_Type()
)
mIBMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMinorVersionNumber.setStatus("current")
_MIBMaintenanceVersionNumber_Type = Unsigned8BitRange
_MIBMaintenanceVersionNumber_Object = MibScalar
mIBMaintenanceVersionNumber = _MIBMaintenanceVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1, 3),
    _MIBMaintenanceVersionNumber_Type()
)
mIBMaintenanceVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMaintenanceVersionNumber.setStatus("current")
_SystemStateGroup_ObjectIdentity = ObjectIdentity
systemStateGroup = _SystemStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200)
)
_SystemStateTable_Object = MibTable
systemStateTable = _SystemStateTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10)
)
if mibBuilder.loadTexts:
    systemStateTable.setStatus("current")
_SystemStateTableEntry_Object = MibTableRow
systemStateTableEntry = _SystemStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1)
)
systemStateTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "systemStatechassisIndex"),
)
if mibBuilder.loadTexts:
    systemStateTableEntry.setStatus("current")
_SystemStatechassisIndex_Type = ObjectRange
_SystemStatechassisIndex_Object = MibTableColumn
systemStatechassisIndex = _SystemStatechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 1),
    _SystemStatechassisIndex_Type()
)
systemStatechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatechassisIndex.setStatus("current")
_SystemStateGlobalSystemStatus_Type = ObjectStatusEnum
_SystemStateGlobalSystemStatus_Object = MibTableColumn
systemStateGlobalSystemStatus = _SystemStateGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 2),
    _SystemStateGlobalSystemStatus_Type()
)
systemStateGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateGlobalSystemStatus.setStatus("current")
_SystemStateChassisState_Type = StateSettingsFlags
_SystemStateChassisState_Object = MibTableColumn
systemStateChassisState = _SystemStateChassisState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 3),
    _SystemStateChassisState_Type()
)
systemStateChassisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisState.setStatus("current")
_SystemStateChassisStatus_Type = ObjectStatusEnum
_SystemStateChassisStatus_Object = MibTableColumn
systemStateChassisStatus = _SystemStateChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 4),
    _SystemStateChassisStatus_Type()
)
systemStateChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisStatus.setStatus("current")


class _SystemStatePowerUnitStateDetails_Type(OctetString):
    """Custom type systemStatePowerUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStateDetails_Type.__name__ = "OctetString"
_SystemStatePowerUnitStateDetails_Object = MibTableColumn
systemStatePowerUnitStateDetails = _SystemStatePowerUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 5),
    _SystemStatePowerUnitStateDetails_Type()
)
systemStatePowerUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStateDetails.setStatus("current")
_SystemStatePowerUnitStatusRedundancy_Type = StatusRedundancyEnum
_SystemStatePowerUnitStatusRedundancy_Object = MibTableColumn
systemStatePowerUnitStatusRedundancy = _SystemStatePowerUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 6),
    _SystemStatePowerUnitStatusRedundancy_Type()
)
systemStatePowerUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusRedundancy.setStatus("current")


class _SystemStatePowerUnitStatusDetails_Type(OctetString):
    """Custom type systemStatePowerUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStatePowerUnitStatusDetails_Object = MibTableColumn
systemStatePowerUnitStatusDetails = _SystemStatePowerUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 7),
    _SystemStatePowerUnitStatusDetails_Type()
)
systemStatePowerUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusDetails.setStatus("current")


class _SystemStatePowerSupplyStateDetails_Type(OctetString):
    """Custom type systemStatePowerSupplyStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerSupplyStateDetails_Type.__name__ = "OctetString"
_SystemStatePowerSupplyStateDetails_Object = MibTableColumn
systemStatePowerSupplyStateDetails = _SystemStatePowerSupplyStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 8),
    _SystemStatePowerSupplyStateDetails_Type()
)
systemStatePowerSupplyStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStateDetails.setStatus("current")
_SystemStatePowerSupplyStatusCombined_Type = ObjectStatusEnum
_SystemStatePowerSupplyStatusCombined_Object = MibTableColumn
systemStatePowerSupplyStatusCombined = _SystemStatePowerSupplyStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 9),
    _SystemStatePowerSupplyStatusCombined_Type()
)
systemStatePowerSupplyStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusCombined.setStatus("current")


class _SystemStatePowerSupplyStatusDetails_Type(OctetString):
    """Custom type systemStatePowerSupplyStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerSupplyStatusDetails_Type.__name__ = "OctetString"
_SystemStatePowerSupplyStatusDetails_Object = MibTableColumn
systemStatePowerSupplyStatusDetails = _SystemStatePowerSupplyStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 10),
    _SystemStatePowerSupplyStatusDetails_Type()
)
systemStatePowerSupplyStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusDetails.setStatus("current")


class _SystemStateVoltageStateDetails_Type(OctetString):
    """Custom type systemStateVoltageStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateVoltageStateDetails_Type.__name__ = "OctetString"
_SystemStateVoltageStateDetails_Object = MibTableColumn
systemStateVoltageStateDetails = _SystemStateVoltageStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 11),
    _SystemStateVoltageStateDetails_Type()
)
systemStateVoltageStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStateDetails.setStatus("current")
_SystemStateVoltageStatusCombined_Type = ObjectStatusEnum
_SystemStateVoltageStatusCombined_Object = MibTableColumn
systemStateVoltageStatusCombined = _SystemStateVoltageStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 12),
    _SystemStateVoltageStatusCombined_Type()
)
systemStateVoltageStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStatusCombined.setStatus("current")


class _SystemStateVoltageStatusDetails_Type(OctetString):
    """Custom type systemStateVoltageStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateVoltageStatusDetails_Type.__name__ = "OctetString"
_SystemStateVoltageStatusDetails_Object = MibTableColumn
systemStateVoltageStatusDetails = _SystemStateVoltageStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 13),
    _SystemStateVoltageStatusDetails_Type()
)
systemStateVoltageStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStatusDetails.setStatus("current")


class _SystemStateAmperageStateDetails_Type(OctetString):
    """Custom type systemStateAmperageStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateAmperageStateDetails_Type.__name__ = "OctetString"
_SystemStateAmperageStateDetails_Object = MibTableColumn
systemStateAmperageStateDetails = _SystemStateAmperageStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 14),
    _SystemStateAmperageStateDetails_Type()
)
systemStateAmperageStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStateDetails.setStatus("current")
_SystemStateAmperageStatusCombined_Type = ObjectStatusEnum
_SystemStateAmperageStatusCombined_Object = MibTableColumn
systemStateAmperageStatusCombined = _SystemStateAmperageStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 15),
    _SystemStateAmperageStatusCombined_Type()
)
systemStateAmperageStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStatusCombined.setStatus("current")


class _SystemStateAmperageStatusDetails_Type(OctetString):
    """Custom type systemStateAmperageStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateAmperageStatusDetails_Type.__name__ = "OctetString"
_SystemStateAmperageStatusDetails_Object = MibTableColumn
systemStateAmperageStatusDetails = _SystemStateAmperageStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 16),
    _SystemStateAmperageStatusDetails_Type()
)
systemStateAmperageStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStatusDetails.setStatus("current")


class _SystemStateCoolingUnitStateDetails_Type(OctetString):
    """Custom type systemStateCoolingUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStateDetails_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStateDetails_Object = MibTableColumn
systemStateCoolingUnitStateDetails = _SystemStateCoolingUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 17),
    _SystemStateCoolingUnitStateDetails_Type()
)
systemStateCoolingUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStateDetails.setStatus("current")
_SystemStateCoolingUnitStatusRedundancy_Type = StatusRedundancyEnum
_SystemStateCoolingUnitStatusRedundancy_Object = MibTableColumn
systemStateCoolingUnitStatusRedundancy = _SystemStateCoolingUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 18),
    _SystemStateCoolingUnitStatusRedundancy_Type()
)
systemStateCoolingUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusRedundancy.setStatus("current")


class _SystemStateCoolingUnitStatusDetails_Type(OctetString):
    """Custom type systemStateCoolingUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStatusDetails_Object = MibTableColumn
systemStateCoolingUnitStatusDetails = _SystemStateCoolingUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 19),
    _SystemStateCoolingUnitStatusDetails_Type()
)
systemStateCoolingUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusDetails.setStatus("current")


class _SystemStateCoolingDeviceStateDetails_Type(OctetString):
    """Custom type systemStateCoolingDeviceStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingDeviceStateDetails_Type.__name__ = "OctetString"
_SystemStateCoolingDeviceStateDetails_Object = MibTableColumn
systemStateCoolingDeviceStateDetails = _SystemStateCoolingDeviceStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 20),
    _SystemStateCoolingDeviceStateDetails_Type()
)
systemStateCoolingDeviceStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStateDetails.setStatus("current")
_SystemStateCoolingDeviceStatusCombined_Type = ObjectStatusEnum
_SystemStateCoolingDeviceStatusCombined_Object = MibTableColumn
systemStateCoolingDeviceStatusCombined = _SystemStateCoolingDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 21),
    _SystemStateCoolingDeviceStatusCombined_Type()
)
systemStateCoolingDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusCombined.setStatus("current")


class _SystemStateCoolingDeviceStatusDetails_Type(OctetString):
    """Custom type systemStateCoolingDeviceStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingDeviceStatusDetails_Type.__name__ = "OctetString"
_SystemStateCoolingDeviceStatusDetails_Object = MibTableColumn
systemStateCoolingDeviceStatusDetails = _SystemStateCoolingDeviceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 22),
    _SystemStateCoolingDeviceStatusDetails_Type()
)
systemStateCoolingDeviceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusDetails.setStatus("current")


class _SystemStateTemperatureStateDetails_Type(OctetString):
    """Custom type systemStateTemperatureStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStateDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStateDetails_Object = MibTableColumn
systemStateTemperatureStateDetails = _SystemStateTemperatureStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 23),
    _SystemStateTemperatureStateDetails_Type()
)
systemStateTemperatureStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStateDetails.setStatus("current")
_SystemStateTemperatureStatusCombined_Type = ObjectStatusEnum
_SystemStateTemperatureStatusCombined_Object = MibTableColumn
systemStateTemperatureStatusCombined = _SystemStateTemperatureStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 24),
    _SystemStateTemperatureStatusCombined_Type()
)
systemStateTemperatureStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusCombined.setStatus("current")


class _SystemStateTemperatureStatusDetails_Type(OctetString):
    """Custom type systemStateTemperatureStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStatusDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStatusDetails_Object = MibTableColumn
systemStateTemperatureStatusDetails = _SystemStateTemperatureStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 25),
    _SystemStateTemperatureStatusDetails_Type()
)
systemStateTemperatureStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusDetails.setStatus("current")


class _SystemStateMemoryDeviceStateDetails_Type(OctetString):
    """Custom type systemStateMemoryDeviceStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateMemoryDeviceStateDetails_Type.__name__ = "OctetString"
_SystemStateMemoryDeviceStateDetails_Object = MibTableColumn
systemStateMemoryDeviceStateDetails = _SystemStateMemoryDeviceStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 26),
    _SystemStateMemoryDeviceStateDetails_Type()
)
systemStateMemoryDeviceStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStateDetails.setStatus("current")
_SystemStateMemoryDeviceStatusCombined_Type = ObjectStatusEnum
_SystemStateMemoryDeviceStatusCombined_Object = MibTableColumn
systemStateMemoryDeviceStatusCombined = _SystemStateMemoryDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 27),
    _SystemStateMemoryDeviceStatusCombined_Type()
)
systemStateMemoryDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusCombined.setStatus("current")


class _SystemStateMemoryDeviceStatusDetails_Type(OctetString):
    """Custom type systemStateMemoryDeviceStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateMemoryDeviceStatusDetails_Type.__name__ = "OctetString"
_SystemStateMemoryDeviceStatusDetails_Object = MibTableColumn
systemStateMemoryDeviceStatusDetails = _SystemStateMemoryDeviceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 28),
    _SystemStateMemoryDeviceStatusDetails_Type()
)
systemStateMemoryDeviceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusDetails.setStatus("current")


class _SystemStateChassisIntrusionStateDetails_Type(OctetString):
    """Custom type systemStateChassisIntrusionStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateChassisIntrusionStateDetails_Type.__name__ = "OctetString"
_SystemStateChassisIntrusionStateDetails_Object = MibTableColumn
systemStateChassisIntrusionStateDetails = _SystemStateChassisIntrusionStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 29),
    _SystemStateChassisIntrusionStateDetails_Type()
)
systemStateChassisIntrusionStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStateDetails.setStatus("current")
_SystemStateChassisIntrusionStatusCombined_Type = ObjectStatusEnum
_SystemStateChassisIntrusionStatusCombined_Object = MibTableColumn
systemStateChassisIntrusionStatusCombined = _SystemStateChassisIntrusionStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 30),
    _SystemStateChassisIntrusionStatusCombined_Type()
)
systemStateChassisIntrusionStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusCombined.setStatus("current")


class _SystemStateChassisIntrusionStatusDetails_Type(OctetString):
    """Custom type systemStateChassisIntrusionStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateChassisIntrusionStatusDetails_Type.__name__ = "OctetString"
_SystemStateChassisIntrusionStatusDetails_Object = MibTableColumn
systemStateChassisIntrusionStatusDetails = _SystemStateChassisIntrusionStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 31),
    _SystemStateChassisIntrusionStatusDetails_Type()
)
systemStateChassisIntrusionStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusDetails.setStatus("current")
_SystemStatePowerUnitStatusCombined_Type = ObjectStatusEnum
_SystemStatePowerUnitStatusCombined_Object = MibTableColumn
systemStatePowerUnitStatusCombined = _SystemStatePowerUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 42),
    _SystemStatePowerUnitStatusCombined_Type()
)
systemStatePowerUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusCombined.setStatus("current")


class _SystemStatePowerUnitStatusList_Type(OctetString):
    """Custom type systemStatePowerUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStatusList_Type.__name__ = "OctetString"
_SystemStatePowerUnitStatusList_Object = MibTableColumn
systemStatePowerUnitStatusList = _SystemStatePowerUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 43),
    _SystemStatePowerUnitStatusList_Type()
)
systemStatePowerUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusList.setStatus("current")
_SystemStateCoolingUnitStatusCombined_Type = ObjectStatusEnum
_SystemStateCoolingUnitStatusCombined_Object = MibTableColumn
systemStateCoolingUnitStatusCombined = _SystemStateCoolingUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 44),
    _SystemStateCoolingUnitStatusCombined_Type()
)
systemStateCoolingUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusCombined.setStatus("current")


class _SystemStateCoolingUnitStatusList_Type(OctetString):
    """Custom type systemStateCoolingUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStatusList_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStatusList_Object = MibTableColumn
systemStateCoolingUnitStatusList = _SystemStateCoolingUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 45),
    _SystemStateCoolingUnitStatusList_Type()
)
systemStateCoolingUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusList.setStatus("current")
_SystemStateProcessorDeviceStatusCombined_Type = ObjectStatusEnum
_SystemStateProcessorDeviceStatusCombined_Object = MibTableColumn
systemStateProcessorDeviceStatusCombined = _SystemStateProcessorDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 50),
    _SystemStateProcessorDeviceStatusCombined_Type()
)
systemStateProcessorDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateProcessorDeviceStatusCombined.setStatus("current")


class _SystemStateProcessorDeviceStatusList_Type(OctetString):
    """Custom type systemStateProcessorDeviceStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateProcessorDeviceStatusList_Type.__name__ = "OctetString"
_SystemStateProcessorDeviceStatusList_Object = MibTableColumn
systemStateProcessorDeviceStatusList = _SystemStateProcessorDeviceStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 51),
    _SystemStateProcessorDeviceStatusList_Type()
)
systemStateProcessorDeviceStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateProcessorDeviceStatusList.setStatus("current")
_SystemStateBatteryStatusCombined_Type = ObjectStatusEnum
_SystemStateBatteryStatusCombined_Object = MibTableColumn
systemStateBatteryStatusCombined = _SystemStateBatteryStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 52),
    _SystemStateBatteryStatusCombined_Type()
)
systemStateBatteryStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateBatteryStatusCombined.setStatus("current")


class _SystemStateBatteryStatusList_Type(OctetString):
    """Custom type systemStateBatteryStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateBatteryStatusList_Type.__name__ = "OctetString"
_SystemStateBatteryStatusList_Object = MibTableColumn
systemStateBatteryStatusList = _SystemStateBatteryStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 53),
    _SystemStateBatteryStatusList_Type()
)
systemStateBatteryStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateBatteryStatusList.setStatus("current")
_SystemStateSDCardUnitStatusCombined_Type = ObjectStatusEnum
_SystemStateSDCardUnitStatusCombined_Object = MibTableColumn
systemStateSDCardUnitStatusCombined = _SystemStateSDCardUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 54),
    _SystemStateSDCardUnitStatusCombined_Type()
)
systemStateSDCardUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardUnitStatusCombined.setStatus("current")


class _SystemStateSDCardUnitStatusList_Type(OctetString):
    """Custom type systemStateSDCardUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateSDCardUnitStatusList_Type.__name__ = "OctetString"
_SystemStateSDCardUnitStatusList_Object = MibTableColumn
systemStateSDCardUnitStatusList = _SystemStateSDCardUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 55),
    _SystemStateSDCardUnitStatusList_Type()
)
systemStateSDCardUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardUnitStatusList.setStatus("current")
_SystemStateSDCardDeviceStatusCombined_Type = ObjectStatusEnum
_SystemStateSDCardDeviceStatusCombined_Object = MibTableColumn
systemStateSDCardDeviceStatusCombined = _SystemStateSDCardDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 56),
    _SystemStateSDCardDeviceStatusCombined_Type()
)
systemStateSDCardDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardDeviceStatusCombined.setStatus("current")


class _SystemStateSDCardDeviceStatusList_Type(OctetString):
    """Custom type systemStateSDCardDeviceStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateSDCardDeviceStatusList_Type.__name__ = "OctetString"
_SystemStateSDCardDeviceStatusList_Object = MibTableColumn
systemStateSDCardDeviceStatusList = _SystemStateSDCardDeviceStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 57),
    _SystemStateSDCardDeviceStatusList_Type()
)
systemStateSDCardDeviceStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateSDCardDeviceStatusList.setStatus("current")
_SystemStateIDSDMCardUnitStatusCombined_Type = ObjectStatusEnum
_SystemStateIDSDMCardUnitStatusCombined_Object = MibTableColumn
systemStateIDSDMCardUnitStatusCombined = _SystemStateIDSDMCardUnitStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 58),
    _SystemStateIDSDMCardUnitStatusCombined_Type()
)
systemStateIDSDMCardUnitStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateIDSDMCardUnitStatusCombined.setStatus("current")


class _SystemStateIDSDMCardUnitStatusList_Type(OctetString):
    """Custom type systemStateIDSDMCardUnitStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateIDSDMCardUnitStatusList_Type.__name__ = "OctetString"
_SystemStateIDSDMCardUnitStatusList_Object = MibTableColumn
systemStateIDSDMCardUnitStatusList = _SystemStateIDSDMCardUnitStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 59),
    _SystemStateIDSDMCardUnitStatusList_Type()
)
systemStateIDSDMCardUnitStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateIDSDMCardUnitStatusList.setStatus("current")
_SystemStateIDSDMCardDeviceStatusCombined_Type = ObjectStatusEnum
_SystemStateIDSDMCardDeviceStatusCombined_Object = MibTableColumn
systemStateIDSDMCardDeviceStatusCombined = _SystemStateIDSDMCardDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 60),
    _SystemStateIDSDMCardDeviceStatusCombined_Type()
)
systemStateIDSDMCardDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateIDSDMCardDeviceStatusCombined.setStatus("current")


class _SystemStateIDSDMCardDeviceStatusList_Type(OctetString):
    """Custom type systemStateIDSDMCardDeviceStatusList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateIDSDMCardDeviceStatusList_Type.__name__ = "OctetString"
_SystemStateIDSDMCardDeviceStatusList_Object = MibTableColumn
systemStateIDSDMCardDeviceStatusList = _SystemStateIDSDMCardDeviceStatusList_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 61),
    _SystemStateIDSDMCardDeviceStatusList_Type()
)
systemStateIDSDMCardDeviceStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateIDSDMCardDeviceStatusList.setStatus("current")


class _SystemStateTemperatureStatisticsStateDetails_Type(OctetString):
    """Custom type systemStateTemperatureStatisticsStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStatisticsStateDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStatisticsStateDetails_Object = MibTableColumn
systemStateTemperatureStatisticsStateDetails = _SystemStateTemperatureStatisticsStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 62),
    _SystemStateTemperatureStatisticsStateDetails_Type()
)
systemStateTemperatureStatisticsStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatisticsStateDetails.setStatus("current")
_SystemStateTemperatureStatisticsStatusCombined_Type = ObjectStatusEnum
_SystemStateTemperatureStatisticsStatusCombined_Object = MibTableColumn
systemStateTemperatureStatisticsStatusCombined = _SystemStateTemperatureStatisticsStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 63),
    _SystemStateTemperatureStatisticsStatusCombined_Type()
)
systemStateTemperatureStatisticsStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatisticsStatusCombined.setStatus("current")


class _SystemStateTemperatureStatisticsStatusDetails_Type(OctetString):
    """Custom type systemStateTemperatureStatisticsStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStatisticsStatusDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStatisticsStatusDetails_Object = MibTableColumn
systemStateTemperatureStatisticsStatusDetails = _SystemStateTemperatureStatisticsStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 200, 10, 1, 64),
    _SystemStateTemperatureStatisticsStatusDetails_Type()
)
systemStateTemperatureStatisticsStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatisticsStatusDetails.setStatus("current")
_ChassisInformationGroup_ObjectIdentity = ObjectIdentity
chassisInformationGroup = _ChassisInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300)
)
_NumEventLogEntries_Type = Unsigned32BitRange
_NumEventLogEntries_Object = MibScalar
numEventLogEntries = _NumEventLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 1),
    _NumEventLogEntries_Type()
)
numEventLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEventLogEntries.setStatus("current")
_NumLCLogEntries_Type = Unsigned32BitRange
_NumLCLogEntries_Object = MibScalar
numLCLogEntries = _NumLCLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 2),
    _NumLCLogEntries_Type()
)
numLCLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numLCLogEntries.setStatus("current")
_ChassisInformationTable_Object = MibTable
chassisInformationTable = _ChassisInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10)
)
if mibBuilder.loadTexts:
    chassisInformationTable.setStatus("current")
_ChassisInformationTableEntry_Object = MibTableRow
chassisInformationTableEntry = _ChassisInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1)
)
chassisInformationTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "chassisIndexChassisInformation"),
)
if mibBuilder.loadTexts:
    chassisInformationTableEntry.setStatus("current")
_ChassisIndexChassisInformation_Type = ObjectRange
_ChassisIndexChassisInformation_Object = MibTableColumn
chassisIndexChassisInformation = _ChassisIndexChassisInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 1),
    _ChassisIndexChassisInformation_Type()
)
chassisIndexChassisInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIndexChassisInformation.setStatus("current")
_ChassisStateCapabilities_Type = StateCapabilitiesFlags
_ChassisStateCapabilities_Object = MibTableColumn
chassisStateCapabilities = _ChassisStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 2),
    _ChassisStateCapabilities_Type()
)
chassisStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStateCapabilities.setStatus("current")
_ChassisStateSettings_Type = StateSettingsFlags
_ChassisStateSettings_Object = MibTableColumn
chassisStateSettings = _ChassisStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 3),
    _ChassisStateSettings_Type()
)
chassisStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStateSettings.setStatus("current")
_ChassisStatus_Type = ObjectStatusEnum
_ChassisStatus_Object = MibTableColumn
chassisStatus = _ChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 4),
    _ChassisStatus_Type()
)
chassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStatus.setStatus("current")
_ChassisparentIndexReference_Type = ObjectRange
_ChassisparentIndexReference_Object = MibTableColumn
chassisparentIndexReference = _ChassisparentIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 5),
    _ChassisparentIndexReference_Type()
)
chassisparentIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisparentIndexReference.setStatus("current")
_ChassisType_Type = ChassisTypeEnum
_ChassisType_Object = MibTableColumn
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 6),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("current")
_ChassisName_Type = String64
_ChassisName_Object = MibTableColumn
chassisName = _ChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 7),
    _ChassisName_Type()
)
chassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisName.setStatus("current")
_ChassisManufacturerName_Type = String64
_ChassisManufacturerName_Object = MibTableColumn
chassisManufacturerName = _ChassisManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 8),
    _ChassisManufacturerName_Type()
)
chassisManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisManufacturerName.setStatus("current")
_ChassisModelTypeName_Type = String64
_ChassisModelTypeName_Object = MibTableColumn
chassisModelTypeName = _ChassisModelTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 9),
    _ChassisModelTypeName_Type()
)
chassisModelTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModelTypeName.setStatus("current")


class _ChassisAssetTagName_Type(OctetString):
    """Custom type chassisAssetTagName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ChassisAssetTagName_Type.__name__ = "OctetString"
_ChassisAssetTagName_Object = MibTableColumn
chassisAssetTagName = _ChassisAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 10),
    _ChassisAssetTagName_Type()
)
chassisAssetTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisAssetTagName.setStatus("current")


class _ChassisServiceTagName_Type(OctetString):
    """Custom type chassisServiceTagName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChassisServiceTagName_Type.__name__ = "OctetString"
_ChassisServiceTagName_Object = MibTableColumn
chassisServiceTagName = _ChassisServiceTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 11),
    _ChassisServiceTagName_Type()
)
chassisServiceTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisServiceTagName.setStatus("current")
_ChassisID_Type = Unsigned8BitRange
_ChassisID_Object = MibTableColumn
chassisID = _ChassisID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 12),
    _ChassisID_Type()
)
chassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisID.setStatus("current")
_ChassisIDExtension_Type = Unsigned16BitRange
_ChassisIDExtension_Object = MibTableColumn
chassisIDExtension = _ChassisIDExtension_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 13),
    _ChassisIDExtension_Type()
)
chassisIDExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIDExtension.setStatus("current")
_ChassisSystemClass_Type = ChassisSystemClassEnum
_ChassisSystemClass_Object = MibTableColumn
chassisSystemClass = _ChassisSystemClass_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 14),
    _ChassisSystemClass_Type()
)
chassisSystemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemClass.setStatus("current")
_ChassisSystemName_Type = String64
_ChassisSystemName_Object = MibTableColumn
chassisSystemName = _ChassisSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 15),
    _ChassisSystemName_Type()
)
chassisSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemName.setStatus("current")
_ChassisLEDControlCapabilitiesUnique_Type = LEDControlCapabilitiesFlags
_ChassisLEDControlCapabilitiesUnique_Object = MibTableColumn
chassisLEDControlCapabilitiesUnique = _ChassisLEDControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 24),
    _ChassisLEDControlCapabilitiesUnique_Type()
)
chassisLEDControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLEDControlCapabilitiesUnique.setStatus("current")
_ChassisLEDControlSettingsUnique_Type = LEDControlSettingsFlags
_ChassisLEDControlSettingsUnique_Object = MibTableColumn
chassisLEDControlSettingsUnique = _ChassisLEDControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 25),
    _ChassisLEDControlSettingsUnique_Type()
)
chassisLEDControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLEDControlSettingsUnique.setStatus("current")
_ChassisIdentifyFlashControlCapabilities_Type = ChassisIdentifyControlCapabilitiesFlags
_ChassisIdentifyFlashControlCapabilities_Object = MibTableColumn
chassisIdentifyFlashControlCapabilities = _ChassisIdentifyFlashControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 28),
    _ChassisIdentifyFlashControlCapabilities_Type()
)
chassisIdentifyFlashControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlCapabilities.setStatus("current")
_ChassisIdentifyFlashControlSettings_Type = ChassisIdentifyControlSettingsFlags
_ChassisIdentifyFlashControlSettings_Object = MibTableColumn
chassisIdentifyFlashControlSettings = _ChassisIdentifyFlashControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 29),
    _ChassisIdentifyFlashControlSettings_Type()
)
chassisIdentifyFlashControlSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlSettings.setStatus("current")
_ChassisLockPresent_Type = BooleanType
_ChassisLockPresent_Object = MibTableColumn
chassisLockPresent = _ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 30),
    _ChassisLockPresent_Type()
)
chassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLockPresent.setStatus("current")
_ChassishostControlCapabilitiesUnique_Type = HostControlCapabilitiesFlags
_ChassishostControlCapabilitiesUnique_Object = MibTableColumn
chassishostControlCapabilitiesUnique = _ChassishostControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 31),
    _ChassishostControlCapabilitiesUnique_Type()
)
chassishostControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassishostControlCapabilitiesUnique.setStatus("current")
_ChassishostControlSettingsUnique_Type = HostControlSettingsFlags
_ChassishostControlSettingsUnique_Object = MibTableColumn
chassishostControlSettingsUnique = _ChassishostControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 32),
    _ChassishostControlSettingsUnique_Type()
)
chassishostControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassishostControlSettingsUnique.setStatus("current")
_ChassiswatchDogControlCapabilitiesUnique_Type = WatchDogControlCapabilitiesFlags
_ChassiswatchDogControlCapabilitiesUnique_Object = MibTableColumn
chassiswatchDogControlCapabilitiesUnique = _ChassiswatchDogControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 33),
    _ChassiswatchDogControlCapabilitiesUnique_Type()
)
chassiswatchDogControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlCapabilitiesUnique.setStatus("current")
_ChassiswatchDogControlSettingsUnique_Type = WatchControlSettingsFlags
_ChassiswatchDogControlSettingsUnique_Object = MibTableColumn
chassiswatchDogControlSettingsUnique = _ChassiswatchDogControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 34),
    _ChassiswatchDogControlSettingsUnique_Type()
)
chassiswatchDogControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlSettingsUnique.setStatus("current")
_ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Type = WatchDogTimerCapabilitiesFlags
_ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Object = MibTableColumn
chassiswatchDogControlExpiryTimeCapabilitiesUnique = _ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 35),
    _ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Type()
)
chassiswatchDogControlExpiryTimeCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTimeCapabilitiesUnique.setStatus("current")
_ChassiswatchDogControlExpiryTime_Type = Unsigned16BitRange
_ChassiswatchDogControlExpiryTime_Object = MibTableColumn
chassiswatchDogControlExpiryTime = _ChassiswatchDogControlExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 36),
    _ChassiswatchDogControlExpiryTime_Type()
)
chassiswatchDogControlExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTime.setStatus("current")
_ChassisPowerButtonControlCapabilitiesUnique_Type = PowerButtonControlCapabilitiesFlags
_ChassisPowerButtonControlCapabilitiesUnique_Object = MibTableColumn
chassisPowerButtonControlCapabilitiesUnique = _ChassisPowerButtonControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 38),
    _ChassisPowerButtonControlCapabilitiesUnique_Type()
)
chassisPowerButtonControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerButtonControlCapabilitiesUnique.setStatus("current")
_ChassisPowerButtonControlSettingsUnique_Type = PowerButtonControlSettingsFlags
_ChassisPowerButtonControlSettingsUnique_Object = MibTableColumn
chassisPowerButtonControlSettingsUnique = _ChassisPowerButtonControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 39),
    _ChassisPowerButtonControlSettingsUnique_Type()
)
chassisPowerButtonControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerButtonControlSettingsUnique.setStatus("current")
_ChassisNMIButtonControlCapabilitiesUnique_Type = NMIButtonControlCapabilitiesFlags
_ChassisNMIButtonControlCapabilitiesUnique_Object = MibTableColumn
chassisNMIButtonControlCapabilitiesUnique = _ChassisNMIButtonControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 44),
    _ChassisNMIButtonControlCapabilitiesUnique_Type()
)
chassisNMIButtonControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNMIButtonControlCapabilitiesUnique.setStatus("current")
_ChassisNMIButtonControlSettingsUnique_Type = NMIButtonControlSettingsFlags
_ChassisNMIButtonControlSettingsUnique_Object = MibTableColumn
chassisNMIButtonControlSettingsUnique = _ChassisNMIButtonControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 45),
    _ChassisNMIButtonControlSettingsUnique_Type()
)
chassisNMIButtonControlSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNMIButtonControlSettingsUnique.setStatus("current")
_ChassisSystemProperties_Type = SystemPropertiesFlags
_ChassisSystemProperties_Object = MibTableColumn
chassisSystemProperties = _ChassisSystemProperties_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 46),
    _ChassisSystemProperties_Type()
)
chassisSystemProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemProperties.setStatus("current")
_ChassisSystemRevisionNumber_Type = Unsigned8BitRange
_ChassisSystemRevisionNumber_Object = MibTableColumn
chassisSystemRevisionNumber = _ChassisSystemRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 47),
    _ChassisSystemRevisionNumber_Type()
)
chassisSystemRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemRevisionNumber.setStatus("current")
_ChassisSystemRevisionName_Type = String64
_ChassisSystemRevisionName_Object = MibTableColumn
chassisSystemRevisionName = _ChassisSystemRevisionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 48),
    _ChassisSystemRevisionName_Type()
)
chassisSystemRevisionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemRevisionName.setStatus("current")
_ChassisExpressServiceCodeName_Type = String64
_ChassisExpressServiceCodeName_Object = MibTableColumn
chassisExpressServiceCodeName = _ChassisExpressServiceCodeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 10, 1, 49),
    _ChassisExpressServiceCodeName_Type()
)
chassisExpressServiceCodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisExpressServiceCodeName.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogTableEntry_Object = MibTableRow
eventLogTableEntry = _EventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1)
)
eventLogTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "eventLogchassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "eventLogRecordIndex"),
)
if mibBuilder.loadTexts:
    eventLogTableEntry.setStatus("current")
_EventLogchassisIndex_Type = ObjectRange
_EventLogchassisIndex_Object = MibTableColumn
eventLogchassisIndex = _EventLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 1),
    _EventLogchassisIndex_Type()
)
eventLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogchassisIndex.setStatus("current")
_EventLogRecordIndex_Type = Unsigned32BitRange
_EventLogRecordIndex_Object = MibTableColumn
eventLogRecordIndex = _EventLogRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 2),
    _EventLogRecordIndex_Type()
)
eventLogRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRecordIndex.setStatus("current")
_EventLogStateCapabilitiesUnique_Type = StateCapabilitiesLogUniqueFlags
_EventLogStateCapabilitiesUnique_Object = MibTableColumn
eventLogStateCapabilitiesUnique = _EventLogStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 3),
    _EventLogStateCapabilitiesUnique_Type()
)
eventLogStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogStateCapabilitiesUnique.setStatus("current")
_EventLogStateSettingsUnique_Type = StateSettingsLogUniqueFlags
_EventLogStateSettingsUnique_Object = MibTableColumn
eventLogStateSettingsUnique = _EventLogStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 4),
    _EventLogStateSettingsUnique_Type()
)
eventLogStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogStateSettingsUnique.setStatus("current")


class _EventLogRecord_Type(OctetString):
    """Custom type eventLogRecord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_EventLogRecord_Type.__name__ = "OctetString"
_EventLogRecord_Object = MibTableColumn
eventLogRecord = _EventLogRecord_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 5),
    _EventLogRecord_Type()
)
eventLogRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRecord.setStatus("current")
_EventLogFormat_Type = LogFormatType
_EventLogFormat_Object = MibTableColumn
eventLogFormat = _EventLogFormat_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 6),
    _EventLogFormat_Type()
)
eventLogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogFormat.setStatus("current")
_EventLogSeverityStatus_Type = ObjectStatusEnum
_EventLogSeverityStatus_Object = MibTableColumn
eventLogSeverityStatus = _EventLogSeverityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 7),
    _EventLogSeverityStatus_Type()
)
eventLogSeverityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSeverityStatus.setStatus("current")
_EventLogDateName_Type = DateName
_EventLogDateName_Object = MibTableColumn
eventLogDateName = _EventLogDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 40, 1, 8),
    _EventLogDateName_Type()
)
eventLogDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDateName.setStatus("current")
_SystemBIOSTable_Object = MibTable
systemBIOSTable = _SystemBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50)
)
if mibBuilder.loadTexts:
    systemBIOSTable.setStatus("current")
_SystemBIOSTableEntry_Object = MibTableRow
systemBIOSTableEntry = _SystemBIOSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1)
)
systemBIOSTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "systemBIOSchassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "systemBIOSIndex"),
)
if mibBuilder.loadTexts:
    systemBIOSTableEntry.setStatus("current")
_SystemBIOSchassisIndex_Type = ObjectRange
_SystemBIOSchassisIndex_Object = MibTableColumn
systemBIOSchassisIndex = _SystemBIOSchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 1),
    _SystemBIOSchassisIndex_Type()
)
systemBIOSchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSchassisIndex.setStatus("current")
_SystemBIOSIndex_Type = ObjectRange
_SystemBIOSIndex_Object = MibTableColumn
systemBIOSIndex = _SystemBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 2),
    _SystemBIOSIndex_Type()
)
systemBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSIndex.setStatus("current")
_SystemBIOSStateCapabilities_Type = StateCapabilitiesFlags
_SystemBIOSStateCapabilities_Object = MibTableColumn
systemBIOSStateCapabilities = _SystemBIOSStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 3),
    _SystemBIOSStateCapabilities_Type()
)
systemBIOSStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStateCapabilities.setStatus("current")
_SystemBIOSStateSettings_Type = StateSettingsFlags
_SystemBIOSStateSettings_Object = MibTableColumn
systemBIOSStateSettings = _SystemBIOSStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 4),
    _SystemBIOSStateSettings_Type()
)
systemBIOSStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStateSettings.setStatus("current")
_SystemBIOSStatus_Type = ObjectStatusEnum
_SystemBIOSStatus_Object = MibTableColumn
systemBIOSStatus = _SystemBIOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 5),
    _SystemBIOSStatus_Type()
)
systemBIOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStatus.setStatus("current")
_SystemBIOSReleaseDateName_Type = DateName
_SystemBIOSReleaseDateName_Object = MibTableColumn
systemBIOSReleaseDateName = _SystemBIOSReleaseDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 7),
    _SystemBIOSReleaseDateName_Type()
)
systemBIOSReleaseDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSReleaseDateName.setStatus("current")
_SystemBIOSVersionName_Type = String64
_SystemBIOSVersionName_Object = MibTableColumn
systemBIOSVersionName = _SystemBIOSVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 8),
    _SystemBIOSVersionName_Type()
)
systemBIOSVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSVersionName.setStatus("current")
_SystemBIOSManufacturerName_Type = String64
_SystemBIOSManufacturerName_Object = MibTableColumn
systemBIOSManufacturerName = _SystemBIOSManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 50, 1, 11),
    _SystemBIOSManufacturerName_Type()
)
systemBIOSManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSManufacturerName.setStatus("current")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("current")
_FirmwareTableEntry_Object = MibTableRow
firmwareTableEntry = _FirmwareTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1)
)
firmwareTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "firmwarechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareTableEntry.setStatus("current")
_FirmwarechassisIndex_Type = ObjectRange
_FirmwarechassisIndex_Object = MibTableColumn
firmwarechassisIndex = _FirmwarechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 1),
    _FirmwarechassisIndex_Type()
)
firmwarechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwarechassisIndex.setStatus("current")
_FirmwareIndex_Type = ObjectRange
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 2),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("current")
_FirmwareStateCapabilities_Type = StateCapabilitiesFlags
_FirmwareStateCapabilities_Object = MibTableColumn
firmwareStateCapabilities = _FirmwareStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 3),
    _FirmwareStateCapabilities_Type()
)
firmwareStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStateCapabilities.setStatus("current")
_FirmwareStateSettings_Type = StateSettingsFlags
_FirmwareStateSettings_Object = MibTableColumn
firmwareStateSettings = _FirmwareStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 4),
    _FirmwareStateSettings_Type()
)
firmwareStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStateSettings.setStatus("current")
_FirmwareStatus_Type = ObjectStatusEnum
_FirmwareStatus_Object = MibTableColumn
firmwareStatus = _FirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 5),
    _FirmwareStatus_Type()
)
firmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStatus.setStatus("current")
_FirmwareSize_Type = Unsigned16BitRange
_FirmwareSize_Object = MibTableColumn
firmwareSize = _FirmwareSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 6),
    _FirmwareSize_Type()
)
firmwareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareSize.setStatus("current")
_FirmwareType_Type = FirmwareType
_FirmwareType_Object = MibTableColumn
firmwareType = _FirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 7),
    _FirmwareType_Type()
)
firmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareType.setStatus("current")
_FirmwareTypeName_Type = String64
_FirmwareTypeName_Object = MibTableColumn
firmwareTypeName = _FirmwareTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 8),
    _FirmwareTypeName_Type()
)
firmwareTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareTypeName.setStatus("current")
_FirmwareUpdateCapabilities_Type = Unsigned16BitRange
_FirmwareUpdateCapabilities_Object = MibTableColumn
firmwareUpdateCapabilities = _FirmwareUpdateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 9),
    _FirmwareUpdateCapabilities_Type()
)
firmwareUpdateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateCapabilities.setStatus("current")
_FirmwareVersionName_Type = String64
_FirmwareVersionName_Object = MibTableColumn
firmwareVersionName = _FirmwareVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 60, 1, 11),
    _FirmwareVersionName_Type()
)
firmwareVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionName.setStatus("current")
_IntrusionTable_Object = MibTable
intrusionTable = _IntrusionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70)
)
if mibBuilder.loadTexts:
    intrusionTable.setStatus("current")
_IntrusionTableEntry_Object = MibTableRow
intrusionTableEntry = _IntrusionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1)
)
intrusionTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "intrusionchassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "intrusionIndex"),
)
if mibBuilder.loadTexts:
    intrusionTableEntry.setStatus("current")
_IntrusionchassisIndex_Type = ObjectRange
_IntrusionchassisIndex_Object = MibTableColumn
intrusionchassisIndex = _IntrusionchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 1),
    _IntrusionchassisIndex_Type()
)
intrusionchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionchassisIndex.setStatus("current")
_IntrusionIndex_Type = ObjectRange
_IntrusionIndex_Object = MibTableColumn
intrusionIndex = _IntrusionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 2),
    _IntrusionIndex_Type()
)
intrusionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionIndex.setStatus("current")
_IntrusionStateCapabilities_Type = StateCapabilitiesFlags
_IntrusionStateCapabilities_Object = MibTableColumn
intrusionStateCapabilities = _IntrusionStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 3),
    _IntrusionStateCapabilities_Type()
)
intrusionStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStateCapabilities.setStatus("current")
_IntrusionStateSettings_Type = StateSettingsFlags
_IntrusionStateSettings_Object = MibTableColumn
intrusionStateSettings = _IntrusionStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 4),
    _IntrusionStateSettings_Type()
)
intrusionStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStateSettings.setStatus("current")
_IntrusionStatus_Type = ObjectStatusEnum
_IntrusionStatus_Object = MibTableColumn
intrusionStatus = _IntrusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 5),
    _IntrusionStatus_Type()
)
intrusionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStatus.setStatus("current")
_IntrusionReading_Type = IntrusionReadingEnum
_IntrusionReading_Object = MibTableColumn
intrusionReading = _IntrusionReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 6),
    _IntrusionReading_Type()
)
intrusionReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionReading.setStatus("current")
_IntrusionType_Type = IntrusionTypeEnum
_IntrusionType_Object = MibTableColumn
intrusionType = _IntrusionType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 7),
    _IntrusionType_Type()
)
intrusionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionType.setStatus("current")
_IntrusionLocationName_Type = String64
_IntrusionLocationName_Object = MibTableColumn
intrusionLocationName = _IntrusionLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 70, 1, 8),
    _IntrusionLocationName_Type()
)
intrusionLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionLocationName.setStatus("current")
_LcLogTable_Object = MibTable
lcLogTable = _LcLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90)
)
if mibBuilder.loadTexts:
    lcLogTable.setStatus("current")
_LcLogTableEntry_Object = MibTableRow
lcLogTableEntry = _LcLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1)
)
lcLogTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "lcLogChassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "lcLogRecordIndex"),
)
if mibBuilder.loadTexts:
    lcLogTableEntry.setStatus("current")
_LcLogChassisIndex_Type = ObjectRange
_LcLogChassisIndex_Object = MibTableColumn
lcLogChassisIndex = _LcLogChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 1),
    _LcLogChassisIndex_Type()
)
lcLogChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogChassisIndex.setStatus("current")
_LcLogRecordIndex_Type = Unsigned32BitRange
_LcLogRecordIndex_Object = MibTableColumn
lcLogRecordIndex = _LcLogRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 2),
    _LcLogRecordIndex_Type()
)
lcLogRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogRecordIndex.setStatus("current")
_LcLogSequenceNumber_Type = Unsigned32BitRange
_LcLogSequenceNumber_Object = MibTableColumn
lcLogSequenceNumber = _LcLogSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 3),
    _LcLogSequenceNumber_Type()
)
lcLogSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogSequenceNumber.setStatus("current")
_LcLogCategory_Type = LcLogCategoryEnum
_LcLogCategory_Object = MibTableColumn
lcLogCategory = _LcLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 4),
    _LcLogCategory_Type()
)
lcLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogCategory.setStatus("current")
_LcLogSeverityStatus_Type = ObjectStatusEnum
_LcLogSeverityStatus_Object = MibTableColumn
lcLogSeverityStatus = _LcLogSeverityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 5),
    _LcLogSeverityStatus_Type()
)
lcLogSeverityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogSeverityStatus.setStatus("current")
_LcLogDateName_Type = DateName
_LcLogDateName_Object = MibTableColumn
lcLogDateName = _LcLogDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 6),
    _LcLogDateName_Type()
)
lcLogDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogDateName.setStatus("current")
_LcLogFQDD_Type = FQDDString
_LcLogFQDD_Object = MibTableColumn
lcLogFQDD = _LcLogFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 7),
    _LcLogFQDD_Type()
)
lcLogFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogFQDD.setStatus("current")


class _LcLogMessageID_Type(OctetString):
    """Custom type lcLogMessageID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LcLogMessageID_Type.__name__ = "OctetString"
_LcLogMessageID_Object = MibTableColumn
lcLogMessageID = _LcLogMessageID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 8),
    _LcLogMessageID_Type()
)
lcLogMessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogMessageID.setStatus("current")


class _LcLogMessage_Type(OctetString):
    """Custom type lcLogMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LcLogMessage_Type.__name__ = "OctetString"
_LcLogMessage_Object = MibTableColumn
lcLogMessage = _LcLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 9),
    _LcLogMessage_Type()
)
lcLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogMessage.setStatus("current")


class _LcLogDetailedDescription_Type(OctetString):
    """Custom type lcLogDetailedDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_LcLogDetailedDescription_Type.__name__ = "OctetString"
_LcLogDetailedDescription_Object = MibTableColumn
lcLogDetailedDescription = _LcLogDetailedDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 10),
    _LcLogDetailedDescription_Type()
)
lcLogDetailedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogDetailedDescription.setStatus("current")


class _LcLogRecommededAction_Type(OctetString):
    """Custom type lcLogRecommededAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_LcLogRecommededAction_Type.__name__ = "OctetString"
_LcLogRecommededAction_Object = MibTableColumn
lcLogRecommededAction = _LcLogRecommededAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 11),
    _LcLogRecommededAction_Type()
)
lcLogRecommededAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogRecommededAction.setStatus("current")


class _LcLogComment_Type(OctetString):
    """Custom type lcLogComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcLogComment_Type.__name__ = "OctetString"
_LcLogComment_Object = MibTableColumn
lcLogComment = _LcLogComment_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 300, 90, 1, 12),
    _LcLogComment_Type()
)
lcLogComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLogComment.setStatus("current")
_PowerGroup_ObjectIdentity = ObjectIdentity
powerGroup = _PowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600)
)
_PowerUnitTable_Object = MibTable
powerUnitTable = _PowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10)
)
if mibBuilder.loadTexts:
    powerUnitTable.setStatus("current")
_PowerUnitTableEntry_Object = MibTableRow
powerUnitTableEntry = _PowerUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1)
)
powerUnitTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "powerUnitchassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "powerUnitIndex"),
)
if mibBuilder.loadTexts:
    powerUnitTableEntry.setStatus("current")
_PowerUnitchassisIndex_Type = ObjectRange
_PowerUnitchassisIndex_Object = MibTableColumn
powerUnitchassisIndex = _PowerUnitchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 1),
    _PowerUnitchassisIndex_Type()
)
powerUnitchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitchassisIndex.setStatus("current")
_PowerUnitIndex_Type = ObjectRange
_PowerUnitIndex_Object = MibTableColumn
powerUnitIndex = _PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 2),
    _PowerUnitIndex_Type()
)
powerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndex.setStatus("current")
_PowerUnitStateCapabilities_Type = StateCapabilitiesFlags
_PowerUnitStateCapabilities_Object = MibTableColumn
powerUnitStateCapabilities = _PowerUnitStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 3),
    _PowerUnitStateCapabilities_Type()
)
powerUnitStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStateCapabilities.setStatus("current")
_PowerUnitStateSettings_Type = StateSettingsFlags
_PowerUnitStateSettings_Object = MibTableColumn
powerUnitStateSettings = _PowerUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 4),
    _PowerUnitStateSettings_Type()
)
powerUnitStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStateSettings.setStatus("current")
_PowerUnitRedundancyStatus_Type = StatusRedundancyEnum
_PowerUnitRedundancyStatus_Object = MibTableColumn
powerUnitRedundancyStatus = _PowerUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 5),
    _PowerUnitRedundancyStatus_Type()
)
powerUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitRedundancyStatus.setStatus("current")
_PowerSupplyCountForRedundancy_Type = ObjectRange
_PowerSupplyCountForRedundancy_Object = MibTableColumn
powerSupplyCountForRedundancy = _PowerSupplyCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 6),
    _PowerSupplyCountForRedundancy_Type()
)
powerSupplyCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyCountForRedundancy.setStatus("current")
_PowerUnitName_Type = String64
_PowerUnitName_Object = MibTableColumn
powerUnitName = _PowerUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 7),
    _PowerUnitName_Type()
)
powerUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitName.setStatus("current")
_PowerUnitStatus_Type = ObjectStatusEnum
_PowerUnitStatus_Object = MibTableColumn
powerUnitStatus = _PowerUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 10, 1, 8),
    _PowerUnitStatus_Type()
)
powerUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatus.setStatus("current")
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("current")
_PowerSupplyTableEntry_Object = MibTableRow
powerSupplyTableEntry = _PowerSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1)
)
powerSupplyTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "powerSupplychassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyTableEntry.setStatus("current")
_PowerSupplychassisIndex_Type = ObjectRange
_PowerSupplychassisIndex_Object = MibTableColumn
powerSupplychassisIndex = _PowerSupplychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 1),
    _PowerSupplychassisIndex_Type()
)
powerSupplychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplychassisIndex.setStatus("current")
_PowerSupplyIndex_Type = ObjectRange
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 2),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("current")
_PowerSupplyStateCapabilitiesUnique_Type = PowerSupplyStateCapabilitiesUniqueFlags
_PowerSupplyStateCapabilitiesUnique_Object = MibTableColumn
powerSupplyStateCapabilitiesUnique = _PowerSupplyStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 3),
    _PowerSupplyStateCapabilitiesUnique_Type()
)
powerSupplyStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStateCapabilitiesUnique.setStatus("current")
_PowerSupplyStateSettingsUnique_Type = PowerSupplyStateSettingsUniqueFlags
_PowerSupplyStateSettingsUnique_Object = MibTableColumn
powerSupplyStateSettingsUnique = _PowerSupplyStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 4),
    _PowerSupplyStateSettingsUnique_Type()
)
powerSupplyStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStateSettingsUnique.setStatus("current")
_PowerSupplyStatus_Type = ObjectStatusEnum
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 5),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")
_PowerSupplyOutputWatts_Type = Signed32BitRange
_PowerSupplyOutputWatts_Object = MibTableColumn
powerSupplyOutputWatts = _PowerSupplyOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 6),
    _PowerSupplyOutputWatts_Type()
)
powerSupplyOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyOutputWatts.setStatus("current")
_PowerSupplyType_Type = PowerSupplyTypeEnum
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 7),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("current")
_PowerSupplyLocationName_Type = String64
_PowerSupplyLocationName_Object = MibTableColumn
powerSupplyLocationName = _PowerSupplyLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 8),
    _PowerSupplyLocationName_Type()
)
powerSupplyLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyLocationName.setStatus("current")
_PowerSupplyMaximumInputVoltage_Type = Signed32BitRange
_PowerSupplyMaximumInputVoltage_Object = MibTableColumn
powerSupplyMaximumInputVoltage = _PowerSupplyMaximumInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 9),
    _PowerSupplyMaximumInputVoltage_Type()
)
powerSupplyMaximumInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyMaximumInputVoltage.setStatus("current")
_PowerSupplypowerUnitIndexReference_Type = ObjectRange
_PowerSupplypowerUnitIndexReference_Object = MibTableColumn
powerSupplypowerUnitIndexReference = _PowerSupplypowerUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 10),
    _PowerSupplypowerUnitIndexReference_Type()
)
powerSupplypowerUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplypowerUnitIndexReference.setStatus("current")
_PowerSupplySensorState_Type = PowerSupplySensorStateFlags
_PowerSupplySensorState_Object = MibTableColumn
powerSupplySensorState = _PowerSupplySensorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 11),
    _PowerSupplySensorState_Type()
)
powerSupplySensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplySensorState.setStatus("current")
_PowerSupplyConfigurationErrorType_Type = PowerSupplyConfigurationErrorTypeEnum
_PowerSupplyConfigurationErrorType_Object = MibTableColumn
powerSupplyConfigurationErrorType = _PowerSupplyConfigurationErrorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 12),
    _PowerSupplyConfigurationErrorType_Type()
)
powerSupplyConfigurationErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyConfigurationErrorType.setStatus("current")
_PowerSupplyPowerMonitorCapable_Type = BooleanType
_PowerSupplyPowerMonitorCapable_Object = MibTableColumn
powerSupplyPowerMonitorCapable = _PowerSupplyPowerMonitorCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 13),
    _PowerSupplyPowerMonitorCapable_Type()
)
powerSupplyPowerMonitorCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPowerMonitorCapable.setStatus("current")
_PowerSupplyRatedInputWattage_Type = Signed32BitRange
_PowerSupplyRatedInputWattage_Object = MibTableColumn
powerSupplyRatedInputWattage = _PowerSupplyRatedInputWattage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 14),
    _PowerSupplyRatedInputWattage_Type()
)
powerSupplyRatedInputWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRatedInputWattage.setStatus("current")
_PowerSupplyFQDD_Type = FQDDString
_PowerSupplyFQDD_Object = MibTableColumn
powerSupplyFQDD = _PowerSupplyFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 15),
    _PowerSupplyFQDD_Type()
)
powerSupplyFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyFQDD.setStatus("current")
_PowerSupplyCurrentInputVoltage_Type = Signed32BitRange
_PowerSupplyCurrentInputVoltage_Object = MibTableColumn
powerSupplyCurrentInputVoltage = _PowerSupplyCurrentInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 12, 1, 16),
    _PowerSupplyCurrentInputVoltage_Type()
)
powerSupplyCurrentInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyCurrentInputVoltage.setStatus("current")
_VoltageProbeTable_Object = MibTable
voltageProbeTable = _VoltageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20)
)
if mibBuilder.loadTexts:
    voltageProbeTable.setStatus("current")
_VoltageProbeTableEntry_Object = MibTableRow
voltageProbeTableEntry = _VoltageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1)
)
voltageProbeTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "voltageProbechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "voltageProbeIndex"),
)
if mibBuilder.loadTexts:
    voltageProbeTableEntry.setStatus("current")
_VoltageProbechassisIndex_Type = ObjectRange
_VoltageProbechassisIndex_Object = MibTableColumn
voltageProbechassisIndex = _VoltageProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 1),
    _VoltageProbechassisIndex_Type()
)
voltageProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbechassisIndex.setStatus("current")
_VoltageProbeIndex_Type = ObjectRange
_VoltageProbeIndex_Object = MibTableColumn
voltageProbeIndex = _VoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 2),
    _VoltageProbeIndex_Type()
)
voltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeIndex.setStatus("current")
_VoltageProbeStateCapabilities_Type = StateCapabilitiesFlags
_VoltageProbeStateCapabilities_Object = MibTableColumn
voltageProbeStateCapabilities = _VoltageProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 3),
    _VoltageProbeStateCapabilities_Type()
)
voltageProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStateCapabilities.setStatus("current")
_VoltageProbeStateSettings_Type = StateSettingsFlags
_VoltageProbeStateSettings_Object = MibTableColumn
voltageProbeStateSettings = _VoltageProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 4),
    _VoltageProbeStateSettings_Type()
)
voltageProbeStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStateSettings.setStatus("current")
_VoltageProbeStatus_Type = StatusProbeEnum
_VoltageProbeStatus_Object = MibTableColumn
voltageProbeStatus = _VoltageProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 5),
    _VoltageProbeStatus_Type()
)
voltageProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStatus.setStatus("current")
_VoltageProbeReading_Type = Signed32BitRange
_VoltageProbeReading_Object = MibTableColumn
voltageProbeReading = _VoltageProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 6),
    _VoltageProbeReading_Type()
)
voltageProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeReading.setStatus("current")
_VoltageProbeType_Type = VoltageTypeEnum
_VoltageProbeType_Object = MibTableColumn
voltageProbeType = _VoltageProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 7),
    _VoltageProbeType_Type()
)
voltageProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeType.setStatus("current")
_VoltageProbeLocationName_Type = String64
_VoltageProbeLocationName_Object = MibTableColumn
voltageProbeLocationName = _VoltageProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 8),
    _VoltageProbeLocationName_Type()
)
voltageProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLocationName.setStatus("current")
_VoltageProbeUpperNonRecoverableThreshold_Type = Signed32BitRange
_VoltageProbeUpperNonRecoverableThreshold_Object = MibTableColumn
voltageProbeUpperNonRecoverableThreshold = _VoltageProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 9),
    _VoltageProbeUpperNonRecoverableThreshold_Type()
)
voltageProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperNonRecoverableThreshold.setStatus("current")
_VoltageProbeUpperCriticalThreshold_Type = Signed32BitRange
_VoltageProbeUpperCriticalThreshold_Object = MibTableColumn
voltageProbeUpperCriticalThreshold = _VoltageProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 10),
    _VoltageProbeUpperCriticalThreshold_Type()
)
voltageProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperCriticalThreshold.setStatus("current")
_VoltageProbeUpperNonCriticalThreshold_Type = Signed32BitRange
_VoltageProbeUpperNonCriticalThreshold_Object = MibTableColumn
voltageProbeUpperNonCriticalThreshold = _VoltageProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 11),
    _VoltageProbeUpperNonCriticalThreshold_Type()
)
voltageProbeUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperNonCriticalThreshold.setStatus("current")
_VoltageProbeLowerNonCriticalThreshold_Type = Signed32BitRange
_VoltageProbeLowerNonCriticalThreshold_Object = MibTableColumn
voltageProbeLowerNonCriticalThreshold = _VoltageProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 12),
    _VoltageProbeLowerNonCriticalThreshold_Type()
)
voltageProbeLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerNonCriticalThreshold.setStatus("current")
_VoltageProbeLowerCriticalThreshold_Type = Signed32BitRange
_VoltageProbeLowerCriticalThreshold_Object = MibTableColumn
voltageProbeLowerCriticalThreshold = _VoltageProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 13),
    _VoltageProbeLowerCriticalThreshold_Type()
)
voltageProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerCriticalThreshold.setStatus("current")
_VoltageProbeLowerNonRecoverableThreshold_Type = Signed32BitRange
_VoltageProbeLowerNonRecoverableThreshold_Object = MibTableColumn
voltageProbeLowerNonRecoverableThreshold = _VoltageProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 14),
    _VoltageProbeLowerNonRecoverableThreshold_Type()
)
voltageProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerNonRecoverableThreshold.setStatus("current")
_VoltageProbeProbeCapabilities_Type = ProbeCapabilitiesFlags
_VoltageProbeProbeCapabilities_Object = MibTableColumn
voltageProbeProbeCapabilities = _VoltageProbeProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 15),
    _VoltageProbeProbeCapabilities_Type()
)
voltageProbeProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeProbeCapabilities.setStatus("current")
_VoltageProbeDiscreteReading_Type = VoltageDiscreteReadingEnum
_VoltageProbeDiscreteReading_Object = MibTableColumn
voltageProbeDiscreteReading = _VoltageProbeDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 20, 1, 16),
    _VoltageProbeDiscreteReading_Type()
)
voltageProbeDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeDiscreteReading.setStatus("current")
_AmperageProbeTable_Object = MibTable
amperageProbeTable = _AmperageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30)
)
if mibBuilder.loadTexts:
    amperageProbeTable.setStatus("current")
_AmperageProbeTableEntry_Object = MibTableRow
amperageProbeTableEntry = _AmperageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1)
)
amperageProbeTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "amperageProbechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "amperageProbeIndex"),
)
if mibBuilder.loadTexts:
    amperageProbeTableEntry.setStatus("current")
_AmperageProbechassisIndex_Type = ObjectRange
_AmperageProbechassisIndex_Object = MibTableColumn
amperageProbechassisIndex = _AmperageProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 1),
    _AmperageProbechassisIndex_Type()
)
amperageProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbechassisIndex.setStatus("current")
_AmperageProbeIndex_Type = ObjectRange
_AmperageProbeIndex_Object = MibTableColumn
amperageProbeIndex = _AmperageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 2),
    _AmperageProbeIndex_Type()
)
amperageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeIndex.setStatus("current")
_AmperageProbeStateCapabilities_Type = StateCapabilitiesFlags
_AmperageProbeStateCapabilities_Object = MibTableColumn
amperageProbeStateCapabilities = _AmperageProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 3),
    _AmperageProbeStateCapabilities_Type()
)
amperageProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStateCapabilities.setStatus("current")
_AmperageProbeStateSettings_Type = StateSettingsFlags
_AmperageProbeStateSettings_Object = MibTableColumn
amperageProbeStateSettings = _AmperageProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 4),
    _AmperageProbeStateSettings_Type()
)
amperageProbeStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStateSettings.setStatus("current")
_AmperageProbeStatus_Type = StatusProbeEnum
_AmperageProbeStatus_Object = MibTableColumn
amperageProbeStatus = _AmperageProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 5),
    _AmperageProbeStatus_Type()
)
amperageProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStatus.setStatus("current")
_AmperageProbeReading_Type = Signed32BitRange
_AmperageProbeReading_Object = MibTableColumn
amperageProbeReading = _AmperageProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 6),
    _AmperageProbeReading_Type()
)
amperageProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeReading.setStatus("current")
_AmperageProbeType_Type = AmperageProbeTypeEnum
_AmperageProbeType_Object = MibTableColumn
amperageProbeType = _AmperageProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 7),
    _AmperageProbeType_Type()
)
amperageProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeType.setStatus("current")
_AmperageProbeLocationName_Type = String64
_AmperageProbeLocationName_Object = MibTableColumn
amperageProbeLocationName = _AmperageProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 8),
    _AmperageProbeLocationName_Type()
)
amperageProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLocationName.setStatus("current")
_AmperageProbeUpperNonRecoverableThreshold_Type = Signed32BitRange
_AmperageProbeUpperNonRecoverableThreshold_Object = MibTableColumn
amperageProbeUpperNonRecoverableThreshold = _AmperageProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 9),
    _AmperageProbeUpperNonRecoverableThreshold_Type()
)
amperageProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperNonRecoverableThreshold.setStatus("current")
_AmperageProbeUpperCriticalThreshold_Type = Signed32BitRange
_AmperageProbeUpperCriticalThreshold_Object = MibTableColumn
amperageProbeUpperCriticalThreshold = _AmperageProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 10),
    _AmperageProbeUpperCriticalThreshold_Type()
)
amperageProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperCriticalThreshold.setStatus("current")
_AmperageProbeUpperNonCriticalThreshold_Type = Signed32BitRange
_AmperageProbeUpperNonCriticalThreshold_Object = MibTableColumn
amperageProbeUpperNonCriticalThreshold = _AmperageProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 11),
    _AmperageProbeUpperNonCriticalThreshold_Type()
)
amperageProbeUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperNonCriticalThreshold.setStatus("current")
_AmperageProbeLowerNonCriticalThreshold_Type = Signed32BitRange
_AmperageProbeLowerNonCriticalThreshold_Object = MibTableColumn
amperageProbeLowerNonCriticalThreshold = _AmperageProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 12),
    _AmperageProbeLowerNonCriticalThreshold_Type()
)
amperageProbeLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerNonCriticalThreshold.setStatus("current")
_AmperageProbeLowerCriticalThreshold_Type = Signed32BitRange
_AmperageProbeLowerCriticalThreshold_Object = MibTableColumn
amperageProbeLowerCriticalThreshold = _AmperageProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 13),
    _AmperageProbeLowerCriticalThreshold_Type()
)
amperageProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerCriticalThreshold.setStatus("current")
_AmperageProbeLowerNonRecoverableThreshold_Type = Signed32BitRange
_AmperageProbeLowerNonRecoverableThreshold_Object = MibTableColumn
amperageProbeLowerNonRecoverableThreshold = _AmperageProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 14),
    _AmperageProbeLowerNonRecoverableThreshold_Type()
)
amperageProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerNonRecoverableThreshold.setStatus("current")
_AmperageProbeProbeCapabilities_Type = ProbeCapabilitiesFlags
_AmperageProbeProbeCapabilities_Object = MibTableColumn
amperageProbeProbeCapabilities = _AmperageProbeProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 15),
    _AmperageProbeProbeCapabilities_Type()
)
amperageProbeProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeProbeCapabilities.setStatus("current")
_AmperageProbeDiscreteReading_Type = AmperageDiscreteReadingEnum
_AmperageProbeDiscreteReading_Object = MibTableColumn
amperageProbeDiscreteReading = _AmperageProbeDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 30, 1, 16),
    _AmperageProbeDiscreteReading_Type()
)
amperageProbeDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeDiscreteReading.setStatus("current")
_SystemBatteryTable_Object = MibTable
systemBatteryTable = _SystemBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50)
)
if mibBuilder.loadTexts:
    systemBatteryTable.setStatus("current")
_SystemBatteryTableEntry_Object = MibTableRow
systemBatteryTableEntry = _SystemBatteryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1)
)
systemBatteryTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "systemBatteryChassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "systemBatteryIndex"),
)
if mibBuilder.loadTexts:
    systemBatteryTableEntry.setStatus("current")
_SystemBatteryChassisIndex_Type = ObjectRange
_SystemBatteryChassisIndex_Object = MibTableColumn
systemBatteryChassisIndex = _SystemBatteryChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 1),
    _SystemBatteryChassisIndex_Type()
)
systemBatteryChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryChassisIndex.setStatus("current")
_SystemBatteryIndex_Type = ObjectRange
_SystemBatteryIndex_Object = MibTableColumn
systemBatteryIndex = _SystemBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 2),
    _SystemBatteryIndex_Type()
)
systemBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryIndex.setStatus("current")
_SystemBatteryStateCapabilities_Type = StateCapabilitiesFlags
_SystemBatteryStateCapabilities_Object = MibTableColumn
systemBatteryStateCapabilities = _SystemBatteryStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 3),
    _SystemBatteryStateCapabilities_Type()
)
systemBatteryStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryStateCapabilities.setStatus("current")
_SystemBatteryStateSettings_Type = StateSettingsFlags
_SystemBatteryStateSettings_Object = MibTableColumn
systemBatteryStateSettings = _SystemBatteryStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 4),
    _SystemBatteryStateSettings_Type()
)
systemBatteryStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryStateSettings.setStatus("current")
_SystemBatteryStatus_Type = ObjectStatusEnum
_SystemBatteryStatus_Object = MibTableColumn
systemBatteryStatus = _SystemBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 5),
    _SystemBatteryStatus_Type()
)
systemBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryStatus.setStatus("current")
_SystemBatteryReading_Type = SystemBatteryReadingFlags
_SystemBatteryReading_Object = MibTableColumn
systemBatteryReading = _SystemBatteryReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 6),
    _SystemBatteryReading_Type()
)
systemBatteryReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryReading.setStatus("current")
_SystemBatteryLocationName_Type = String64
_SystemBatteryLocationName_Object = MibTableColumn
systemBatteryLocationName = _SystemBatteryLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 50, 1, 7),
    _SystemBatteryLocationName_Type()
)
systemBatteryLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBatteryLocationName.setStatus("current")
_PowerUsageTable_Object = MibTable
powerUsageTable = _PowerUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60)
)
if mibBuilder.loadTexts:
    powerUsageTable.setStatus("current")
_PowerUsageTableEntry_Object = MibTableRow
powerUsageTableEntry = _PowerUsageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1)
)
powerUsageTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "powerUsageChassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "powerUsageIndex"),
)
if mibBuilder.loadTexts:
    powerUsageTableEntry.setStatus("current")
_PowerUsageChassisIndex_Type = ObjectRange
_PowerUsageChassisIndex_Object = MibTableColumn
powerUsageChassisIndex = _PowerUsageChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 1),
    _PowerUsageChassisIndex_Type()
)
powerUsageChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageChassisIndex.setStatus("current")
_PowerUsageIndex_Type = ObjectRange
_PowerUsageIndex_Object = MibTableColumn
powerUsageIndex = _PowerUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 2),
    _PowerUsageIndex_Type()
)
powerUsageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageIndex.setStatus("current")
_PowerUsageStateCapabilities_Type = StateCapabilitiesFlags
_PowerUsageStateCapabilities_Object = MibTableColumn
powerUsageStateCapabilities = _PowerUsageStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 3),
    _PowerUsageStateCapabilities_Type()
)
powerUsageStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageStateCapabilities.setStatus("current")
_PowerUsageStateSettings_Type = StateSettingsFlags
_PowerUsageStateSettings_Object = MibTableColumn
powerUsageStateSettings = _PowerUsageStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 4),
    _PowerUsageStateSettings_Type()
)
powerUsageStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageStateSettings.setStatus("current")
_PowerUsageStatus_Type = ObjectStatusEnum
_PowerUsageStatus_Object = MibTableColumn
powerUsageStatus = _PowerUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 5),
    _PowerUsageStatus_Type()
)
powerUsageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageStatus.setStatus("current")
_PowerUsageEntityName_Type = String64
_PowerUsageEntityName_Object = MibTableColumn
powerUsageEntityName = _PowerUsageEntityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 6),
    _PowerUsageEntityName_Type()
)
powerUsageEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageEntityName.setStatus("current")
_PowerUsageCumulativeWattage_Type = Unsigned32BitRange
_PowerUsageCumulativeWattage_Object = MibTableColumn
powerUsageCumulativeWattage = _PowerUsageCumulativeWattage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 7),
    _PowerUsageCumulativeWattage_Type()
)
powerUsageCumulativeWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageCumulativeWattage.setStatus("current")
_PowerUsageCumulativeWattageStartDateName_Type = DateName
_PowerUsageCumulativeWattageStartDateName_Object = MibTableColumn
powerUsageCumulativeWattageStartDateName = _PowerUsageCumulativeWattageStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 8),
    _PowerUsageCumulativeWattageStartDateName_Type()
)
powerUsageCumulativeWattageStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageCumulativeWattageStartDateName.setStatus("current")
_PowerUsagePeakWatts_Type = Unsigned32BitRange
_PowerUsagePeakWatts_Object = MibTableColumn
powerUsagePeakWatts = _PowerUsagePeakWatts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 9),
    _PowerUsagePeakWatts_Type()
)
powerUsagePeakWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakWatts.setStatus("current")
_PowerUsagePeakWattsStartDateName_Type = DateName
_PowerUsagePeakWattsStartDateName_Object = MibTableColumn
powerUsagePeakWattsStartDateName = _PowerUsagePeakWattsStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 10),
    _PowerUsagePeakWattsStartDateName_Type()
)
powerUsagePeakWattsStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakWattsStartDateName.setStatus("current")
_PowerUsagePeakWattsReadingDateName_Type = DateName
_PowerUsagePeakWattsReadingDateName_Object = MibTableColumn
powerUsagePeakWattsReadingDateName = _PowerUsagePeakWattsReadingDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 11),
    _PowerUsagePeakWattsReadingDateName_Type()
)
powerUsagePeakWattsReadingDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakWattsReadingDateName.setStatus("current")
_PowerUsagePeakAmps_Type = Unsigned32BitRange
_PowerUsagePeakAmps_Object = MibTableColumn
powerUsagePeakAmps = _PowerUsagePeakAmps_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 12),
    _PowerUsagePeakAmps_Type()
)
powerUsagePeakAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakAmps.setStatus("current")
_PowerUsagePeakAmpsStartDateName_Type = DateName
_PowerUsagePeakAmpsStartDateName_Object = MibTableColumn
powerUsagePeakAmpsStartDateName = _PowerUsagePeakAmpsStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 13),
    _PowerUsagePeakAmpsStartDateName_Type()
)
powerUsagePeakAmpsStartDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakAmpsStartDateName.setStatus("current")
_PowerUsagePeakAmpsReadingDateName_Type = DateName
_PowerUsagePeakAmpsReadingDateName_Object = MibTableColumn
powerUsagePeakAmpsReadingDateName = _PowerUsagePeakAmpsReadingDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 14),
    _PowerUsagePeakAmpsReadingDateName_Type()
)
powerUsagePeakAmpsReadingDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakAmpsReadingDateName.setStatus("current")
_PowerUsageIdlePower_Type = Unsigned32BitRange
_PowerUsageIdlePower_Object = MibTableColumn
powerUsageIdlePower = _PowerUsageIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 15),
    _PowerUsageIdlePower_Type()
)
powerUsageIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageIdlePower.setStatus("current")
_PowerUsageMaxPotentialPower_Type = Unsigned32BitRange
_PowerUsageMaxPotentialPower_Object = MibTableColumn
powerUsageMaxPotentialPower = _PowerUsageMaxPotentialPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 16),
    _PowerUsageMaxPotentialPower_Type()
)
powerUsageMaxPotentialPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageMaxPotentialPower.setStatus("current")
_PowerUsagePowerCapCapabilities_Type = PowerCapCapabilitiesFlags
_PowerUsagePowerCapCapabilities_Object = MibTableColumn
powerUsagePowerCapCapabilities = _PowerUsagePowerCapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 17),
    _PowerUsagePowerCapCapabilities_Type()
)
powerUsagePowerCapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePowerCapCapabilities.setStatus("current")
_PowerUsagePowerCapSetting_Type = PowerCapSettingEnum
_PowerUsagePowerCapSetting_Object = MibTableColumn
powerUsagePowerCapSetting = _PowerUsagePowerCapSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 18),
    _PowerUsagePowerCapSetting_Type()
)
powerUsagePowerCapSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePowerCapSetting.setStatus("current")
_PowerUsagePowerCapValue_Type = Unsigned32BitRange
_PowerUsagePowerCapValue_Object = MibTableColumn
powerUsagePowerCapValue = _PowerUsagePowerCapValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 19),
    _PowerUsagePowerCapValue_Type()
)
powerUsagePowerCapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePowerCapValue.setStatus("current")
_PowerUsageInstantaneousHeadroom_Type = Unsigned32BitRange
_PowerUsageInstantaneousHeadroom_Object = MibTableColumn
powerUsageInstantaneousHeadroom = _PowerUsageInstantaneousHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 20),
    _PowerUsageInstantaneousHeadroom_Type()
)
powerUsageInstantaneousHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsageInstantaneousHeadroom.setStatus("current")
_PowerUsagePeakHeadroom_Type = Unsigned32BitRange
_PowerUsagePeakHeadroom_Object = MibTableColumn
powerUsagePeakHeadroom = _PowerUsagePeakHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 600, 60, 1, 21),
    _PowerUsagePeakHeadroom_Type()
)
powerUsagePeakHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUsagePeakHeadroom.setStatus("current")
_ThermalGroup_ObjectIdentity = ObjectIdentity
thermalGroup = _ThermalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700)
)
_CoolingUnitTable_Object = MibTable
coolingUnitTable = _CoolingUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10)
)
if mibBuilder.loadTexts:
    coolingUnitTable.setStatus("current")
_CoolingUnitTableEntry_Object = MibTableRow
coolingUnitTableEntry = _CoolingUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1)
)
coolingUnitTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "coolingUnitchassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "coolingUnitIndex"),
)
if mibBuilder.loadTexts:
    coolingUnitTableEntry.setStatus("current")
_CoolingUnitchassisIndex_Type = ObjectRange
_CoolingUnitchassisIndex_Object = MibTableColumn
coolingUnitchassisIndex = _CoolingUnitchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 1),
    _CoolingUnitchassisIndex_Type()
)
coolingUnitchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitchassisIndex.setStatus("current")
_CoolingUnitIndex_Type = ObjectRange
_CoolingUnitIndex_Object = MibTableColumn
coolingUnitIndex = _CoolingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 2),
    _CoolingUnitIndex_Type()
)
coolingUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitIndex.setStatus("current")
_CoolingUnitStateCapabilties_Type = StateCapabilitiesFlags
_CoolingUnitStateCapabilties_Object = MibTableColumn
coolingUnitStateCapabilties = _CoolingUnitStateCapabilties_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 3),
    _CoolingUnitStateCapabilties_Type()
)
coolingUnitStateCapabilties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStateCapabilties.setStatus("current")
_CoolingUnitStateSettings_Type = StateSettingsFlags
_CoolingUnitStateSettings_Object = MibTableColumn
coolingUnitStateSettings = _CoolingUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 4),
    _CoolingUnitStateSettings_Type()
)
coolingUnitStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStateSettings.setStatus("current")
_CoolingUnitRedundancyStatus_Type = StatusRedundancyEnum
_CoolingUnitRedundancyStatus_Object = MibTableColumn
coolingUnitRedundancyStatus = _CoolingUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 5),
    _CoolingUnitRedundancyStatus_Type()
)
coolingUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitRedundancyStatus.setStatus("current")
_CoolingDeviceCountForRedundancy_Type = ObjectRange
_CoolingDeviceCountForRedundancy_Object = MibTableColumn
coolingDeviceCountForRedundancy = _CoolingDeviceCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 6),
    _CoolingDeviceCountForRedundancy_Type()
)
coolingDeviceCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceCountForRedundancy.setStatus("current")
_CoolingUnitName_Type = String64
_CoolingUnitName_Object = MibTableColumn
coolingUnitName = _CoolingUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 7),
    _CoolingUnitName_Type()
)
coolingUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitName.setStatus("current")
_CoolingUnitStatus_Type = ObjectStatusEnum
_CoolingUnitStatus_Object = MibTableColumn
coolingUnitStatus = _CoolingUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 10, 1, 8),
    _CoolingUnitStatus_Type()
)
coolingUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStatus.setStatus("current")
_CoolingDeviceTable_Object = MibTable
coolingDeviceTable = _CoolingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12)
)
if mibBuilder.loadTexts:
    coolingDeviceTable.setStatus("current")
_CoolingDeviceTableEntry_Object = MibTableRow
coolingDeviceTableEntry = _CoolingDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1)
)
coolingDeviceTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "coolingDevicechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "coolingDeviceIndex"),
)
if mibBuilder.loadTexts:
    coolingDeviceTableEntry.setStatus("current")
_CoolingDevicechassisIndex_Type = ObjectRange
_CoolingDevicechassisIndex_Object = MibTableColumn
coolingDevicechassisIndex = _CoolingDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 1),
    _CoolingDevicechassisIndex_Type()
)
coolingDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDevicechassisIndex.setStatus("current")
_CoolingDeviceIndex_Type = ObjectRange
_CoolingDeviceIndex_Object = MibTableColumn
coolingDeviceIndex = _CoolingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 2),
    _CoolingDeviceIndex_Type()
)
coolingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceIndex.setStatus("current")
_CoolingDeviceStateCapabilities_Type = StateCapabilitiesFlags
_CoolingDeviceStateCapabilities_Object = MibTableColumn
coolingDeviceStateCapabilities = _CoolingDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 3),
    _CoolingDeviceStateCapabilities_Type()
)
coolingDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStateCapabilities.setStatus("current")
_CoolingDeviceStateSettings_Type = StateSettingsFlags
_CoolingDeviceStateSettings_Object = MibTableColumn
coolingDeviceStateSettings = _CoolingDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 4),
    _CoolingDeviceStateSettings_Type()
)
coolingDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStateSettings.setStatus("current")
_CoolingDeviceStatus_Type = StatusProbeEnum
_CoolingDeviceStatus_Object = MibTableColumn
coolingDeviceStatus = _CoolingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 5),
    _CoolingDeviceStatus_Type()
)
coolingDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStatus.setStatus("current")
_CoolingDeviceReading_Type = Signed32BitRange
_CoolingDeviceReading_Object = MibTableColumn
coolingDeviceReading = _CoolingDeviceReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 6),
    _CoolingDeviceReading_Type()
)
coolingDeviceReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceReading.setStatus("current")
_CoolingDeviceType_Type = CoolingDeviceTypeEnum
_CoolingDeviceType_Object = MibTableColumn
coolingDeviceType = _CoolingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 7),
    _CoolingDeviceType_Type()
)
coolingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceType.setStatus("current")
_CoolingDeviceLocationName_Type = String64
_CoolingDeviceLocationName_Object = MibTableColumn
coolingDeviceLocationName = _CoolingDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 8),
    _CoolingDeviceLocationName_Type()
)
coolingDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLocationName.setStatus("current")
_CoolingDeviceUpperNonRecoverableThreshold_Type = Signed32BitRange
_CoolingDeviceUpperNonRecoverableThreshold_Object = MibTableColumn
coolingDeviceUpperNonRecoverableThreshold = _CoolingDeviceUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 9),
    _CoolingDeviceUpperNonRecoverableThreshold_Type()
)
coolingDeviceUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonRecoverableThreshold.setStatus("current")
_CoolingDeviceUpperCriticalThreshold_Type = Signed32BitRange
_CoolingDeviceUpperCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperCriticalThreshold = _CoolingDeviceUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 10),
    _CoolingDeviceUpperCriticalThreshold_Type()
)
coolingDeviceUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperCriticalThreshold.setStatus("current")
_CoolingDeviceUpperNonCriticalThreshold_Type = Signed32BitRange
_CoolingDeviceUpperNonCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperNonCriticalThreshold = _CoolingDeviceUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 11),
    _CoolingDeviceUpperNonCriticalThreshold_Type()
)
coolingDeviceUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonCriticalThreshold.setStatus("current")
_CoolingDeviceLowerNonCriticalThreshold_Type = Signed32BitRange
_CoolingDeviceLowerNonCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerNonCriticalThreshold = _CoolingDeviceLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 12),
    _CoolingDeviceLowerNonCriticalThreshold_Type()
)
coolingDeviceLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonCriticalThreshold.setStatus("current")
_CoolingDeviceLowerCriticalThreshold_Type = Signed32BitRange
_CoolingDeviceLowerCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerCriticalThreshold = _CoolingDeviceLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 13),
    _CoolingDeviceLowerCriticalThreshold_Type()
)
coolingDeviceLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerCriticalThreshold.setStatus("current")
_CoolingDeviceLowerNonRecoverableThreshold_Type = Signed32BitRange
_CoolingDeviceLowerNonRecoverableThreshold_Object = MibTableColumn
coolingDeviceLowerNonRecoverableThreshold = _CoolingDeviceLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 14),
    _CoolingDeviceLowerNonRecoverableThreshold_Type()
)
coolingDeviceLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonRecoverableThreshold.setStatus("current")
_CoolingDevicecoolingUnitIndexReference_Type = ObjectRange
_CoolingDevicecoolingUnitIndexReference_Object = MibTableColumn
coolingDevicecoolingUnitIndexReference = _CoolingDevicecoolingUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 15),
    _CoolingDevicecoolingUnitIndexReference_Type()
)
coolingDevicecoolingUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDevicecoolingUnitIndexReference.setStatus("current")
_CoolingDeviceSubType_Type = CoolingDeviceSubTypeEnum
_CoolingDeviceSubType_Object = MibTableColumn
coolingDeviceSubType = _CoolingDeviceSubType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 16),
    _CoolingDeviceSubType_Type()
)
coolingDeviceSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceSubType.setStatus("current")
_CoolingDeviceProbeCapabilities_Type = ProbeCapabilitiesFlags
_CoolingDeviceProbeCapabilities_Object = MibTableColumn
coolingDeviceProbeCapabilities = _CoolingDeviceProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 17),
    _CoolingDeviceProbeCapabilities_Type()
)
coolingDeviceProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceProbeCapabilities.setStatus("current")
_CoolingDeviceDiscreteReading_Type = CoolingDeviceDiscreteReadingEnum
_CoolingDeviceDiscreteReading_Object = MibTableColumn
coolingDeviceDiscreteReading = _CoolingDeviceDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 18),
    _CoolingDeviceDiscreteReading_Type()
)
coolingDeviceDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceDiscreteReading.setStatus("current")
_CoolingDeviceFQDD_Type = FQDDString
_CoolingDeviceFQDD_Object = MibTableColumn
coolingDeviceFQDD = _CoolingDeviceFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 12, 1, 19),
    _CoolingDeviceFQDD_Type()
)
coolingDeviceFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceFQDD.setStatus("current")
_TemperatureProbeTable_Object = MibTable
temperatureProbeTable = _TemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20)
)
if mibBuilder.loadTexts:
    temperatureProbeTable.setStatus("current")
_TemperatureProbeTableEntry_Object = MibTableRow
temperatureProbeTableEntry = _TemperatureProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1)
)
temperatureProbeTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "temperatureProbechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "temperatureProbeIndex"),
)
if mibBuilder.loadTexts:
    temperatureProbeTableEntry.setStatus("current")
_TemperatureProbechassisIndex_Type = ObjectRange
_TemperatureProbechassisIndex_Object = MibTableColumn
temperatureProbechassisIndex = _TemperatureProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 1),
    _TemperatureProbechassisIndex_Type()
)
temperatureProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbechassisIndex.setStatus("current")
_TemperatureProbeIndex_Type = ObjectRange
_TemperatureProbeIndex_Object = MibTableColumn
temperatureProbeIndex = _TemperatureProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 2),
    _TemperatureProbeIndex_Type()
)
temperatureProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeIndex.setStatus("current")
_TemperatureProbeStateCapabilities_Type = StateCapabilitiesFlags
_TemperatureProbeStateCapabilities_Object = MibTableColumn
temperatureProbeStateCapabilities = _TemperatureProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 3),
    _TemperatureProbeStateCapabilities_Type()
)
temperatureProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStateCapabilities.setStatus("current")
_TemperatureProbeStateSettings_Type = StateSettingsFlags
_TemperatureProbeStateSettings_Object = MibTableColumn
temperatureProbeStateSettings = _TemperatureProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 4),
    _TemperatureProbeStateSettings_Type()
)
temperatureProbeStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStateSettings.setStatus("current")
_TemperatureProbeStatus_Type = StatusProbeEnum
_TemperatureProbeStatus_Object = MibTableColumn
temperatureProbeStatus = _TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 5),
    _TemperatureProbeStatus_Type()
)
temperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStatus.setStatus("current")
_TemperatureProbeReading_Type = Signed32BitRange
_TemperatureProbeReading_Object = MibTableColumn
temperatureProbeReading = _TemperatureProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 6),
    _TemperatureProbeReading_Type()
)
temperatureProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeReading.setStatus("current")
_TemperatureProbeType_Type = TemperatureProbeTypeEnum
_TemperatureProbeType_Object = MibTableColumn
temperatureProbeType = _TemperatureProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 7),
    _TemperatureProbeType_Type()
)
temperatureProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeType.setStatus("current")
_TemperatureProbeLocationName_Type = String64
_TemperatureProbeLocationName_Object = MibTableColumn
temperatureProbeLocationName = _TemperatureProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 8),
    _TemperatureProbeLocationName_Type()
)
temperatureProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLocationName.setStatus("current")
_TemperatureProbeUpperNonRecoverableThreshold_Type = Signed32BitRange
_TemperatureProbeUpperNonRecoverableThreshold_Object = MibTableColumn
temperatureProbeUpperNonRecoverableThreshold = _TemperatureProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 9),
    _TemperatureProbeUpperNonRecoverableThreshold_Type()
)
temperatureProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonRecoverableThreshold.setStatus("current")
_TemperatureProbeUpperCriticalThreshold_Type = Signed32BitRange
_TemperatureProbeUpperCriticalThreshold_Object = MibTableColumn
temperatureProbeUpperCriticalThreshold = _TemperatureProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 10),
    _TemperatureProbeUpperCriticalThreshold_Type()
)
temperatureProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperCriticalThreshold.setStatus("current")
_TemperatureProbeUpperNonCriticalThreshold_Type = Signed32BitRange
_TemperatureProbeUpperNonCriticalThreshold_Object = MibTableColumn
temperatureProbeUpperNonCriticalThreshold = _TemperatureProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 11),
    _TemperatureProbeUpperNonCriticalThreshold_Type()
)
temperatureProbeUpperNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonCriticalThreshold.setStatus("current")
_TemperatureProbeLowerNonCriticalThreshold_Type = Signed32BitRange
_TemperatureProbeLowerNonCriticalThreshold_Object = MibTableColumn
temperatureProbeLowerNonCriticalThreshold = _TemperatureProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 12),
    _TemperatureProbeLowerNonCriticalThreshold_Type()
)
temperatureProbeLowerNonCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonCriticalThreshold.setStatus("current")
_TemperatureProbeLowerCriticalThreshold_Type = Signed32BitRange
_TemperatureProbeLowerCriticalThreshold_Object = MibTableColumn
temperatureProbeLowerCriticalThreshold = _TemperatureProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 13),
    _TemperatureProbeLowerCriticalThreshold_Type()
)
temperatureProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerCriticalThreshold.setStatus("current")
_TemperatureProbeLowerNonRecoverableThreshold_Type = Signed32BitRange
_TemperatureProbeLowerNonRecoverableThreshold_Object = MibTableColumn
temperatureProbeLowerNonRecoverableThreshold = _TemperatureProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 14),
    _TemperatureProbeLowerNonRecoverableThreshold_Type()
)
temperatureProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonRecoverableThreshold.setStatus("current")
_TemperatureProbeProbeCapabilities_Type = ProbeCapabilitiesFlags
_TemperatureProbeProbeCapabilities_Object = MibTableColumn
temperatureProbeProbeCapabilities = _TemperatureProbeProbeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 15),
    _TemperatureProbeProbeCapabilities_Type()
)
temperatureProbeProbeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeProbeCapabilities.setStatus("current")
_TemperatureProbeDiscreteReading_Type = TemperatureDiscreteReadingEnum
_TemperatureProbeDiscreteReading_Object = MibTableColumn
temperatureProbeDiscreteReading = _TemperatureProbeDiscreteReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 700, 20, 1, 16),
    _TemperatureProbeDiscreteReading_Type()
)
temperatureProbeDiscreteReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeDiscreteReading.setStatus("current")
_DeviceGroup_ObjectIdentity = ObjectIdentity
deviceGroup = _DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100)
)
_ProcessorDeviceTable_Object = MibTable
processorDeviceTable = _ProcessorDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30)
)
if mibBuilder.loadTexts:
    processorDeviceTable.setStatus("current")
_ProcessorDeviceTableEntry_Object = MibTableRow
processorDeviceTableEntry = _ProcessorDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1)
)
processorDeviceTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "processorDevicechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "processorDeviceIndex"),
)
if mibBuilder.loadTexts:
    processorDeviceTableEntry.setStatus("current")
_ProcessorDevicechassisIndex_Type = ObjectRange
_ProcessorDevicechassisIndex_Object = MibTableColumn
processorDevicechassisIndex = _ProcessorDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 1),
    _ProcessorDevicechassisIndex_Type()
)
processorDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDevicechassisIndex.setStatus("current")
_ProcessorDeviceIndex_Type = ObjectRange
_ProcessorDeviceIndex_Object = MibTableColumn
processorDeviceIndex = _ProcessorDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 2),
    _ProcessorDeviceIndex_Type()
)
processorDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceIndex.setStatus("current")
_ProcessorDeviceStateCapabilities_Type = StateCapabilitiesFlags
_ProcessorDeviceStateCapabilities_Object = MibTableColumn
processorDeviceStateCapabilities = _ProcessorDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 3),
    _ProcessorDeviceStateCapabilities_Type()
)
processorDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStateCapabilities.setStatus("current")
_ProcessorDeviceStateSettings_Type = StateSettingsFlags
_ProcessorDeviceStateSettings_Object = MibTableColumn
processorDeviceStateSettings = _ProcessorDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 4),
    _ProcessorDeviceStateSettings_Type()
)
processorDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStateSettings.setStatus("current")
_ProcessorDeviceStatus_Type = ObjectStatusEnum
_ProcessorDeviceStatus_Object = MibTableColumn
processorDeviceStatus = _ProcessorDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 5),
    _ProcessorDeviceStatus_Type()
)
processorDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatus.setStatus("current")
_ProcessorDeviceType_Type = ProcessorDeviceType
_ProcessorDeviceType_Object = MibTableColumn
processorDeviceType = _ProcessorDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 7),
    _ProcessorDeviceType_Type()
)
processorDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceType.setStatus("current")
_ProcessorDeviceManufacturerName_Type = String64
_ProcessorDeviceManufacturerName_Object = MibTableColumn
processorDeviceManufacturerName = _ProcessorDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 8),
    _ProcessorDeviceManufacturerName_Type()
)
processorDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceManufacturerName.setStatus("current")
_ProcessorDeviceStatusState_Type = ProcessorDeviceStatusState
_ProcessorDeviceStatusState_Object = MibTableColumn
processorDeviceStatusState = _ProcessorDeviceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 9),
    _ProcessorDeviceStatusState_Type()
)
processorDeviceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusState.setStatus("current")
_ProcessorDeviceFamily_Type = ProcessorDeviceFamily
_ProcessorDeviceFamily_Object = MibTableColumn
processorDeviceFamily = _ProcessorDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 10),
    _ProcessorDeviceFamily_Type()
)
processorDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceFamily.setStatus("current")
_ProcessorDeviceMaximumSpeed_Type = Unsigned32BitRange
_ProcessorDeviceMaximumSpeed_Object = MibTableColumn
processorDeviceMaximumSpeed = _ProcessorDeviceMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 11),
    _ProcessorDeviceMaximumSpeed_Type()
)
processorDeviceMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceMaximumSpeed.setStatus("current")
_ProcessorDeviceCurrentSpeed_Type = Unsigned32BitRange
_ProcessorDeviceCurrentSpeed_Object = MibTableColumn
processorDeviceCurrentSpeed = _ProcessorDeviceCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 12),
    _ProcessorDeviceCurrentSpeed_Type()
)
processorDeviceCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCurrentSpeed.setStatus("current")
_ProcessorDeviceExternalClockSpeed_Type = Unsigned32BitRange
_ProcessorDeviceExternalClockSpeed_Object = MibTableColumn
processorDeviceExternalClockSpeed = _ProcessorDeviceExternalClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 13),
    _ProcessorDeviceExternalClockSpeed_Type()
)
processorDeviceExternalClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExternalClockSpeed.setStatus("current")
_ProcessorDeviceVoltage_Type = Signed32BitRange
_ProcessorDeviceVoltage_Object = MibTableColumn
processorDeviceVoltage = _ProcessorDeviceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 14),
    _ProcessorDeviceVoltage_Type()
)
processorDeviceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceVoltage.setStatus("current")
_ProcessorDeviceVersionName_Type = String64
_ProcessorDeviceVersionName_Object = MibTableColumn
processorDeviceVersionName = _ProcessorDeviceVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 16),
    _ProcessorDeviceVersionName_Type()
)
processorDeviceVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceVersionName.setStatus("current")
_ProcessorDeviceCoreCount_Type = Unsigned32BitRange
_ProcessorDeviceCoreCount_Object = MibTableColumn
processorDeviceCoreCount = _ProcessorDeviceCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 17),
    _ProcessorDeviceCoreCount_Type()
)
processorDeviceCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCoreCount.setStatus("current")
_ProcessorDeviceCoreEnabledCount_Type = Unsigned32BitRange
_ProcessorDeviceCoreEnabledCount_Object = MibTableColumn
processorDeviceCoreEnabledCount = _ProcessorDeviceCoreEnabledCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 18),
    _ProcessorDeviceCoreEnabledCount_Type()
)
processorDeviceCoreEnabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCoreEnabledCount.setStatus("current")
_ProcessorDeviceThreadCount_Type = Unsigned32BitRange
_ProcessorDeviceThreadCount_Object = MibTableColumn
processorDeviceThreadCount = _ProcessorDeviceThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 19),
    _ProcessorDeviceThreadCount_Type()
)
processorDeviceThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceThreadCount.setStatus("current")
_ProcessorDeviceCharacteristics_Type = Unsigned16BitRange
_ProcessorDeviceCharacteristics_Object = MibTableColumn
processorDeviceCharacteristics = _ProcessorDeviceCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 20),
    _ProcessorDeviceCharacteristics_Type()
)
processorDeviceCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCharacteristics.setStatus("current")
_ProcessorDeviceExtendedCapabilities_Type = Unsigned16BitRange
_ProcessorDeviceExtendedCapabilities_Object = MibTableColumn
processorDeviceExtendedCapabilities = _ProcessorDeviceExtendedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 21),
    _ProcessorDeviceExtendedCapabilities_Type()
)
processorDeviceExtendedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExtendedCapabilities.setStatus("current")
_ProcessorDeviceExtendedSettings_Type = Unsigned16BitRange
_ProcessorDeviceExtendedSettings_Object = MibTableColumn
processorDeviceExtendedSettings = _ProcessorDeviceExtendedSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 22),
    _ProcessorDeviceExtendedSettings_Type()
)
processorDeviceExtendedSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExtendedSettings.setStatus("current")
_ProcessorDeviceBrandName_Type = String64
_ProcessorDeviceBrandName_Object = MibTableColumn
processorDeviceBrandName = _ProcessorDeviceBrandName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 23),
    _ProcessorDeviceBrandName_Type()
)
processorDeviceBrandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceBrandName.setStatus("current")
_ProcessorDeviceFQDD_Type = FQDDString
_ProcessorDeviceFQDD_Object = MibTableColumn
processorDeviceFQDD = _ProcessorDeviceFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 30, 1, 26),
    _ProcessorDeviceFQDD_Type()
)
processorDeviceFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceFQDD.setStatus("current")
_ProcessorDeviceStatusTable_Object = MibTable
processorDeviceStatusTable = _ProcessorDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32)
)
if mibBuilder.loadTexts:
    processorDeviceStatusTable.setStatus("current")
_ProcessorDeviceStatusTableEntry_Object = MibTableRow
processorDeviceStatusTableEntry = _ProcessorDeviceStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1)
)
processorDeviceStatusTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "processorDeviceStatusChassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "processorDeviceStatusIndex"),
)
if mibBuilder.loadTexts:
    processorDeviceStatusTableEntry.setStatus("current")
_ProcessorDeviceStatusChassisIndex_Type = ObjectRange
_ProcessorDeviceStatusChassisIndex_Object = MibTableColumn
processorDeviceStatusChassisIndex = _ProcessorDeviceStatusChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 1),
    _ProcessorDeviceStatusChassisIndex_Type()
)
processorDeviceStatusChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusChassisIndex.setStatus("current")
_ProcessorDeviceStatusIndex_Type = ObjectRange
_ProcessorDeviceStatusIndex_Object = MibTableColumn
processorDeviceStatusIndex = _ProcessorDeviceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 2),
    _ProcessorDeviceStatusIndex_Type()
)
processorDeviceStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusIndex.setStatus("current")
_ProcessorDeviceStatusStateCapabilities_Type = StateCapabilitiesFlags
_ProcessorDeviceStatusStateCapabilities_Object = MibTableColumn
processorDeviceStatusStateCapabilities = _ProcessorDeviceStatusStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 3),
    _ProcessorDeviceStatusStateCapabilities_Type()
)
processorDeviceStatusStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusStateCapabilities.setStatus("current")
_ProcessorDeviceStatusStateSettings_Type = StateSettingsFlags
_ProcessorDeviceStatusStateSettings_Object = MibTableColumn
processorDeviceStatusStateSettings = _ProcessorDeviceStatusStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 4),
    _ProcessorDeviceStatusStateSettings_Type()
)
processorDeviceStatusStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusStateSettings.setStatus("current")
_ProcessorDeviceStatusStatus_Type = ObjectStatusEnum
_ProcessorDeviceStatusStatus_Object = MibTableColumn
processorDeviceStatusStatus = _ProcessorDeviceStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 5),
    _ProcessorDeviceStatusStatus_Type()
)
processorDeviceStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusStatus.setStatus("current")
_ProcessorDeviceStatusReading_Type = ProcessorDeviceStatusReadingFlags
_ProcessorDeviceStatusReading_Object = MibTableColumn
processorDeviceStatusReading = _ProcessorDeviceStatusReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 6),
    _ProcessorDeviceStatusReading_Type()
)
processorDeviceStatusReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusReading.setStatus("current")
_ProcessorDeviceStatusLocationName_Type = String64
_ProcessorDeviceStatusLocationName_Object = MibTableColumn
processorDeviceStatusLocationName = _ProcessorDeviceStatusLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 32, 1, 7),
    _ProcessorDeviceStatusLocationName_Type()
)
processorDeviceStatusLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusLocationName.setStatus("current")
_MemoryDeviceTable_Object = MibTable
memoryDeviceTable = _MemoryDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50)
)
if mibBuilder.loadTexts:
    memoryDeviceTable.setStatus("current")
_MemoryDeviceTableEntry_Object = MibTableRow
memoryDeviceTableEntry = _MemoryDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1)
)
memoryDeviceTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "memoryDevicechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "memoryDeviceIndex"),
)
if mibBuilder.loadTexts:
    memoryDeviceTableEntry.setStatus("current")
_MemoryDevicechassisIndex_Type = ObjectRange
_MemoryDevicechassisIndex_Object = MibTableColumn
memoryDevicechassisIndex = _MemoryDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 1),
    _MemoryDevicechassisIndex_Type()
)
memoryDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicechassisIndex.setStatus("current")
_MemoryDeviceIndex_Type = ObjectRange
_MemoryDeviceIndex_Object = MibTableColumn
memoryDeviceIndex = _MemoryDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 2),
    _MemoryDeviceIndex_Type()
)
memoryDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceIndex.setStatus("current")
_MemoryDeviceStateCapabilities_Type = StateCapabilitiesFlags
_MemoryDeviceStateCapabilities_Object = MibTableColumn
memoryDeviceStateCapabilities = _MemoryDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 3),
    _MemoryDeviceStateCapabilities_Type()
)
memoryDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStateCapabilities.setStatus("current")
_MemoryDeviceStateSettings_Type = StateSettingsFlags
_MemoryDeviceStateSettings_Object = MibTableColumn
memoryDeviceStateSettings = _MemoryDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 4),
    _MemoryDeviceStateSettings_Type()
)
memoryDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStateSettings.setStatus("current")
_MemoryDeviceStatus_Type = ObjectStatusEnum
_MemoryDeviceStatus_Object = MibTableColumn
memoryDeviceStatus = _MemoryDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 5),
    _MemoryDeviceStatus_Type()
)
memoryDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStatus.setStatus("current")
_MemoryDeviceType_Type = MemoryDeviceTypeEnum
_MemoryDeviceType_Object = MibTableColumn
memoryDeviceType = _MemoryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 7),
    _MemoryDeviceType_Type()
)
memoryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceType.setStatus("current")
_MemoryDeviceLocationName_Type = String64
_MemoryDeviceLocationName_Object = MibTableColumn
memoryDeviceLocationName = _MemoryDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 8),
    _MemoryDeviceLocationName_Type()
)
memoryDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceLocationName.setStatus("current")
_MemoryDeviceBankLocationName_Type = String64
_MemoryDeviceBankLocationName_Object = MibTableColumn
memoryDeviceBankLocationName = _MemoryDeviceBankLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 10),
    _MemoryDeviceBankLocationName_Type()
)
memoryDeviceBankLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceBankLocationName.setStatus("current")
_MemoryDeviceSize_Type = Unsigned32BitRange
_MemoryDeviceSize_Object = MibTableColumn
memoryDeviceSize = _MemoryDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 14),
    _MemoryDeviceSize_Type()
)
memoryDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSize.setStatus("current")
_MemoryDeviceSpeed_Type = Unsigned32BitRange
_MemoryDeviceSpeed_Object = MibTableColumn
memoryDeviceSpeed = _MemoryDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 15),
    _MemoryDeviceSpeed_Type()
)
memoryDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSpeed.setStatus("current")
_MemoryDeviceManufacturerName_Type = String64
_MemoryDeviceManufacturerName_Object = MibTableColumn
memoryDeviceManufacturerName = _MemoryDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 21),
    _MemoryDeviceManufacturerName_Type()
)
memoryDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceManufacturerName.setStatus("current")
_MemoryDevicePartNumberName_Type = String64
_MemoryDevicePartNumberName_Object = MibTableColumn
memoryDevicePartNumberName = _MemoryDevicePartNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 22),
    _MemoryDevicePartNumberName_Type()
)
memoryDevicePartNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePartNumberName.setStatus("current")
_MemoryDeviceSerialNumberName_Type = String64
_MemoryDeviceSerialNumberName_Object = MibTableColumn
memoryDeviceSerialNumberName = _MemoryDeviceSerialNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 23),
    _MemoryDeviceSerialNumberName_Type()
)
memoryDeviceSerialNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSerialNumberName.setStatus("current")
_MemoryDeviceFQDD_Type = FQDDString
_MemoryDeviceFQDD_Object = MibTableColumn
memoryDeviceFQDD = _MemoryDeviceFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 26),
    _MemoryDeviceFQDD_Type()
)
memoryDeviceFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceFQDD.setStatus("current")
_MemoryDeviceCurrentOperatingSpeed_Type = Unsigned32BitRange
_MemoryDeviceCurrentOperatingSpeed_Object = MibTableColumn
memoryDeviceCurrentOperatingSpeed = _MemoryDeviceCurrentOperatingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 50, 1, 27),
    _MemoryDeviceCurrentOperatingSpeed_Type()
)
memoryDeviceCurrentOperatingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceCurrentOperatingSpeed.setStatus("current")
_PCIDeviceTable_Object = MibTable
pCIDeviceTable = _PCIDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80)
)
if mibBuilder.loadTexts:
    pCIDeviceTable.setStatus("current")
_PCIDeviceTableEntry_Object = MibTableRow
pCIDeviceTableEntry = _PCIDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1)
)
pCIDeviceTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "pCIDevicechassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "pCIDeviceIndex"),
)
if mibBuilder.loadTexts:
    pCIDeviceTableEntry.setStatus("current")
_PCIDevicechassisIndex_Type = ObjectRange
_PCIDevicechassisIndex_Object = MibTableColumn
pCIDevicechassisIndex = _PCIDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 1),
    _PCIDevicechassisIndex_Type()
)
pCIDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDevicechassisIndex.setStatus("current")
_PCIDeviceIndex_Type = ObjectRange
_PCIDeviceIndex_Object = MibTableColumn
pCIDeviceIndex = _PCIDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 2),
    _PCIDeviceIndex_Type()
)
pCIDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceIndex.setStatus("current")
_PCIDeviceStateCapabilities_Type = StateCapabilitiesFlags
_PCIDeviceStateCapabilities_Object = MibTableColumn
pCIDeviceStateCapabilities = _PCIDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 3),
    _PCIDeviceStateCapabilities_Type()
)
pCIDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStateCapabilities.setStatus("current")
_PCIDeviceStateSettings_Type = StateSettingsFlags
_PCIDeviceStateSettings_Object = MibTableColumn
pCIDeviceStateSettings = _PCIDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 4),
    _PCIDeviceStateSettings_Type()
)
pCIDeviceStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStateSettings.setStatus("current")
_PCIDeviceStatus_Type = ObjectStatusEnum
_PCIDeviceStatus_Object = MibTableColumn
pCIDeviceStatus = _PCIDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 5),
    _PCIDeviceStatus_Type()
)
pCIDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStatus.setStatus("current")
_PCIDeviceDataBusWidth_Type = Unsigned32BitRange
_PCIDeviceDataBusWidth_Object = MibTableColumn
pCIDeviceDataBusWidth = _PCIDeviceDataBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 7),
    _PCIDeviceDataBusWidth_Type()
)
pCIDeviceDataBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceDataBusWidth.setStatus("current")
_PCIDeviceManufacturerName_Type = String64
_PCIDeviceManufacturerName_Object = MibTableColumn
pCIDeviceManufacturerName = _PCIDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 8),
    _PCIDeviceManufacturerName_Type()
)
pCIDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceManufacturerName.setStatus("current")
_PCIDeviceDescriptionName_Type = String64
_PCIDeviceDescriptionName_Object = MibTableColumn
pCIDeviceDescriptionName = _PCIDeviceDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 9),
    _PCIDeviceDescriptionName_Type()
)
pCIDeviceDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceDescriptionName.setStatus("current")
_PCIDeviceFQDD_Type = FQDDString
_PCIDeviceFQDD_Object = MibTableColumn
pCIDeviceFQDD = _PCIDeviceFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 80, 1, 12),
    _PCIDeviceFQDD_Type()
)
pCIDeviceFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceFQDD.setStatus("current")
_NetworkDeviceTable_Object = MibTable
networkDeviceTable = _NetworkDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90)
)
if mibBuilder.loadTexts:
    networkDeviceTable.setStatus("current")
_NetworkDeviceTableEntry_Object = MibTableRow
networkDeviceTableEntry = _NetworkDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1)
)
networkDeviceTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "networkDeviceChassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "networkDeviceIndex"),
)
if mibBuilder.loadTexts:
    networkDeviceTableEntry.setStatus("current")
_NetworkDeviceChassisIndex_Type = ObjectRange
_NetworkDeviceChassisIndex_Object = MibTableColumn
networkDeviceChassisIndex = _NetworkDeviceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 1),
    _NetworkDeviceChassisIndex_Type()
)
networkDeviceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceChassisIndex.setStatus("current")
_NetworkDeviceIndex_Type = ObjectRange
_NetworkDeviceIndex_Object = MibTableColumn
networkDeviceIndex = _NetworkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 2),
    _NetworkDeviceIndex_Type()
)
networkDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIndex.setStatus("current")
_NetworkDeviceStatus_Type = ObjectStatusEnum
_NetworkDeviceStatus_Object = MibTableColumn
networkDeviceStatus = _NetworkDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 3),
    _NetworkDeviceStatus_Type()
)
networkDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceStatus.setStatus("current")
_NetworkDeviceConnectionStatus_Type = NetworkDeviceConnectionStatusEnum
_NetworkDeviceConnectionStatus_Object = MibTableColumn
networkDeviceConnectionStatus = _NetworkDeviceConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 4),
    _NetworkDeviceConnectionStatus_Type()
)
networkDeviceConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceConnectionStatus.setStatus("current")
_NetworkDeviceProductName_Type = String64
_NetworkDeviceProductName_Object = MibTableColumn
networkDeviceProductName = _NetworkDeviceProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 6),
    _NetworkDeviceProductName_Type()
)
networkDeviceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceProductName.setStatus("current")
_NetworkDeviceVendorName_Type = String64
_NetworkDeviceVendorName_Object = MibTableColumn
networkDeviceVendorName = _NetworkDeviceVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 7),
    _NetworkDeviceVendorName_Type()
)
networkDeviceVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceVendorName.setStatus("current")
_NetworkDeviceCurrentMACAddress_Type = MACAddress
_NetworkDeviceCurrentMACAddress_Object = MibTableColumn
networkDeviceCurrentMACAddress = _NetworkDeviceCurrentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 15),
    _NetworkDeviceCurrentMACAddress_Type()
)
networkDeviceCurrentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceCurrentMACAddress.setStatus("current")
_NetworkDevicePermanentMACAddress_Type = MACAddress
_NetworkDevicePermanentMACAddress_Object = MibTableColumn
networkDevicePermanentMACAddress = _NetworkDevicePermanentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 16),
    _NetworkDevicePermanentMACAddress_Type()
)
networkDevicePermanentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePermanentMACAddress.setStatus("current")
_NetworkDevicePCIBusNumber_Type = Unsigned8BitRange
_NetworkDevicePCIBusNumber_Object = MibTableColumn
networkDevicePCIBusNumber = _NetworkDevicePCIBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 17),
    _NetworkDevicePCIBusNumber_Type()
)
networkDevicePCIBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePCIBusNumber.setStatus("current")
_NetworkDevicePCIDeviceNumber_Type = Unsigned8BitRange
_NetworkDevicePCIDeviceNumber_Object = MibTableColumn
networkDevicePCIDeviceNumber = _NetworkDevicePCIDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 18),
    _NetworkDevicePCIDeviceNumber_Type()
)
networkDevicePCIDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePCIDeviceNumber.setStatus("current")
_NetworkDevicePCIFunctionNumber_Type = Unsigned8BitRange
_NetworkDevicePCIFunctionNumber_Object = MibTableColumn
networkDevicePCIFunctionNumber = _NetworkDevicePCIFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 19),
    _NetworkDevicePCIFunctionNumber_Type()
)
networkDevicePCIFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDevicePCIFunctionNumber.setStatus("current")
_NetworkDeviceTOECapabilityFlags_Type = NetworkDeviceTOECapabilityFlags
_NetworkDeviceTOECapabilityFlags_Object = MibTableColumn
networkDeviceTOECapabilityFlags = _NetworkDeviceTOECapabilityFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 23),
    _NetworkDeviceTOECapabilityFlags_Type()
)
networkDeviceTOECapabilityFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceTOECapabilityFlags.setStatus("current")
_NetworkDeviceiSCSICapabilityFlags_Type = NetworkDeviceiSCSICapabilityFlags
_NetworkDeviceiSCSICapabilityFlags_Object = MibTableColumn
networkDeviceiSCSICapabilityFlags = _NetworkDeviceiSCSICapabilityFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 27),
    _NetworkDeviceiSCSICapabilityFlags_Type()
)
networkDeviceiSCSICapabilityFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceiSCSICapabilityFlags.setStatus("current")
_NetworkDeviceiSCSIEnabled_Type = BooleanType
_NetworkDeviceiSCSIEnabled_Object = MibTableColumn
networkDeviceiSCSIEnabled = _NetworkDeviceiSCSIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 28),
    _NetworkDeviceiSCSIEnabled_Type()
)
networkDeviceiSCSIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceiSCSIEnabled.setStatus("current")
_NetworkDeviceCapabilities_Type = NetworkDeviceCapabilitiesFlags
_NetworkDeviceCapabilities_Object = MibTableColumn
networkDeviceCapabilities = _NetworkDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 29),
    _NetworkDeviceCapabilities_Type()
)
networkDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceCapabilities.setStatus("current")
_NetworkDeviceFQDD_Type = FQDDString
_NetworkDeviceFQDD_Object = MibTableColumn
networkDeviceFQDD = _NetworkDeviceFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1100, 90, 1, 30),
    _NetworkDeviceFQDD_Type()
)
networkDeviceFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceFQDD.setStatus("current")
_SlotGroup_ObjectIdentity = ObjectIdentity
slotGroup = _SlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200)
)
_SystemSlotTable_Object = MibTable
systemSlotTable = _SystemSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10)
)
if mibBuilder.loadTexts:
    systemSlotTable.setStatus("current")
_SystemSlotTableEntry_Object = MibTableRow
systemSlotTableEntry = _SystemSlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1)
)
systemSlotTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "systemSlotchassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "systemSlotIndex"),
)
if mibBuilder.loadTexts:
    systemSlotTableEntry.setStatus("current")
_SystemSlotchassisIndex_Type = ObjectRange
_SystemSlotchassisIndex_Object = MibTableColumn
systemSlotchassisIndex = _SystemSlotchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 1),
    _SystemSlotchassisIndex_Type()
)
systemSlotchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotchassisIndex.setStatus("current")
_SystemSlotIndex_Type = ObjectRange
_SystemSlotIndex_Object = MibTableColumn
systemSlotIndex = _SystemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 2),
    _SystemSlotIndex_Type()
)
systemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotIndex.setStatus("current")
_SystemSlotStateCapabilitiesUnique_Type = SystemSlotStateCapabilitiesFlags
_SystemSlotStateCapabilitiesUnique_Object = MibTableColumn
systemSlotStateCapabilitiesUnique = _SystemSlotStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 3),
    _SystemSlotStateCapabilitiesUnique_Type()
)
systemSlotStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStateCapabilitiesUnique.setStatus("current")
_SystemSlotStateSettingsUnique_Type = SystemSlotStateSettingsFlags
_SystemSlotStateSettingsUnique_Object = MibTableColumn
systemSlotStateSettingsUnique = _SystemSlotStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 4),
    _SystemSlotStateSettingsUnique_Type()
)
systemSlotStateSettingsUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStateSettingsUnique.setStatus("current")
_SystemSlotStatus_Type = ObjectStatusEnum
_SystemSlotStatus_Object = MibTableColumn
systemSlotStatus = _SystemSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 5),
    _SystemSlotStatus_Type()
)
systemSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStatus.setStatus("current")
_SystemSlotCurrentUsage_Type = SystemSlotUsageEnum
_SystemSlotCurrentUsage_Object = MibTableColumn
systemSlotCurrentUsage = _SystemSlotCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 6),
    _SystemSlotCurrentUsage_Type()
)
systemSlotCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotCurrentUsage.setStatus("current")
_SystemSlotType_Type = SystemSlotTypeEnum
_SystemSlotType_Object = MibTableColumn
systemSlotType = _SystemSlotType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 7),
    _SystemSlotType_Type()
)
systemSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotType.setStatus("current")
_SystemSlotSlotExternalSlotName_Type = String64
_SystemSlotSlotExternalSlotName_Object = MibTableColumn
systemSlotSlotExternalSlotName = _SystemSlotSlotExternalSlotName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 8),
    _SystemSlotSlotExternalSlotName_Type()
)
systemSlotSlotExternalSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotSlotExternalSlotName.setStatus("current")
_SystemSlotCategory_Type = SystemSlotCategoryEnum
_SystemSlotCategory_Object = MibTableColumn
systemSlotCategory = _SystemSlotCategory_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 1200, 10, 1, 11),
    _SystemSlotCategory_Type()
)
systemSlotCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotCategory.setStatus("current")
_FruGroup_ObjectIdentity = ObjectIdentity
fruGroup = _FruGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000)
)
_FruTable_Object = MibTable
fruTable = _FruTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10)
)
if mibBuilder.loadTexts:
    fruTable.setStatus("current")
_FruTableEntry_Object = MibTableRow
fruTableEntry = _FruTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1)
)
fruTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "fruChassisIndex"),
    (0, "IDRAC-MIB-SMIv2", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruTableEntry.setStatus("current")
_FruChassisIndex_Type = ObjectRange
_FruChassisIndex_Object = MibTableColumn
fruChassisIndex = _FruChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 1),
    _FruChassisIndex_Type()
)
fruChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruChassisIndex.setStatus("current")
_FruIndex_Type = ObjectRange
_FruIndex_Object = MibTableColumn
fruIndex = _FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 2),
    _FruIndex_Type()
)
fruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruIndex.setStatus("current")
_FruInformationStatus_Type = ObjectStatusEnum
_FruInformationStatus_Object = MibTableColumn
fruInformationStatus = _FruInformationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 3),
    _FruInformationStatus_Type()
)
fruInformationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruInformationStatus.setStatus("current")


class _FruManufacturerName_Type(OctetString):
    """Custom type fruManufacturerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruManufacturerName_Type.__name__ = "OctetString"
_FruManufacturerName_Object = MibTableColumn
fruManufacturerName = _FruManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 6),
    _FruManufacturerName_Type()
)
fruManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruManufacturerName.setStatus("current")


class _FruSerialNumberName_Type(OctetString):
    """Custom type fruSerialNumberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruSerialNumberName_Type.__name__ = "OctetString"
_FruSerialNumberName_Object = MibTableColumn
fruSerialNumberName = _FruSerialNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 7),
    _FruSerialNumberName_Type()
)
fruSerialNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSerialNumberName.setStatus("current")


class _FruPartNumberName_Type(OctetString):
    """Custom type fruPartNumberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruPartNumberName_Type.__name__ = "OctetString"
_FruPartNumberName_Object = MibTableColumn
fruPartNumberName = _FruPartNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 8),
    _FruPartNumberName_Type()
)
fruPartNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPartNumberName.setStatus("current")


class _FruRevisionName_Type(OctetString):
    """Custom type fruRevisionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruRevisionName_Type.__name__ = "OctetString"
_FruRevisionName_Object = MibTableColumn
fruRevisionName = _FruRevisionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 9),
    _FruRevisionName_Type()
)
fruRevisionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruRevisionName.setStatus("current")
_FruFQDD_Type = FQDDString
_FruFQDD_Object = MibTableColumn
fruFQDD = _FruFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 4, 2000, 10, 1, 12),
    _FruFQDD_Type()
)
fruFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruFQDD.setStatus("current")
_StorageDetailsGroup_ObjectIdentity = ObjectIdentity
storageDetailsGroup = _StorageDetailsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1)
)
_StorageManagement_ObjectIdentity = ObjectIdentity
storageManagement = _StorageManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20)
)
_PhysicalDevices_ObjectIdentity = ObjectIdentity
physicalDevices = _PhysicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("current")
_ControllerTableEntry_Object = MibTableRow
controllerTableEntry = _ControllerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1)
)
controllerTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "controllerNumber"),
)
if mibBuilder.loadTexts:
    controllerTableEntry.setStatus("current")


class _ControllerNumber_Type(Integer32):
    """Custom type controllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ControllerNumber_Type.__name__ = "Integer32"
_ControllerNumber_Object = MibTableColumn
controllerNumber = _ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 1),
    _ControllerNumber_Type()
)
controllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNumber.setStatus("current")
_ControllerName_Type = DisplayString
_ControllerName_Object = MibTableColumn
controllerName = _ControllerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 2),
    _ControllerName_Type()
)
controllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerName.setStatus("current")


class _ControllerRebuildRate_Type(Integer32):
    """Custom type controllerRebuildRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerRebuildRate_Type.__name__ = "Integer32"
_ControllerRebuildRate_Object = MibTableColumn
controllerRebuildRate = _ControllerRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 7),
    _ControllerRebuildRate_Type()
)
controllerRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRebuildRate.setStatus("current")
_ControllerFWVersion_Type = DisplayString
_ControllerFWVersion_Object = MibTableColumn
controllerFWVersion = _ControllerFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 8),
    _ControllerFWVersion_Type()
)
controllerFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFWVersion.setStatus("current")
_ControllerCacheSizeInMB_Type = Integer32
_ControllerCacheSizeInMB_Object = MibTableColumn
controllerCacheSizeInMB = _ControllerCacheSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 9),
    _ControllerCacheSizeInMB_Type()
)
controllerCacheSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCacheSizeInMB.setStatus("current")
_ControllerRollUpStatus_Type = ObjectStatusEnum
_ControllerRollUpStatus_Object = MibTableColumn
controllerRollUpStatus = _ControllerRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 37),
    _ControllerRollUpStatus_Type()
)
controllerRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRollUpStatus.setStatus("current")
_ControllerComponentStatus_Type = ObjectStatusEnum
_ControllerComponentStatus_Object = MibTableColumn
controllerComponentStatus = _ControllerComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 38),
    _ControllerComponentStatus_Type()
)
controllerComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerComponentStatus.setStatus("current")
_ControllerDriverVersion_Type = DisplayString
_ControllerDriverVersion_Object = MibTableColumn
controllerDriverVersion = _ControllerDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 41),
    _ControllerDriverVersion_Type()
)
controllerDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDriverVersion.setStatus("current")
_ControllerPCISlot_Type = DisplayString
_ControllerPCISlot_Object = MibTableColumn
controllerPCISlot = _ControllerPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 42),
    _ControllerPCISlot_Type()
)
controllerPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPCISlot.setStatus("current")


class _ControllerReconstructRate_Type(Integer32):
    """Custom type controllerReconstructRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerReconstructRate_Type.__name__ = "Integer32"
_ControllerReconstructRate_Object = MibTableColumn
controllerReconstructRate = _ControllerReconstructRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 48),
    _ControllerReconstructRate_Type()
)
controllerReconstructRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerReconstructRate.setStatus("current")


class _ControllerPatrolReadRate_Type(Integer32):
    """Custom type controllerPatrolReadRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerPatrolReadRate_Type.__name__ = "Integer32"
_ControllerPatrolReadRate_Object = MibTableColumn
controllerPatrolReadRate = _ControllerPatrolReadRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 49),
    _ControllerPatrolReadRate_Type()
)
controllerPatrolReadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadRate.setStatus("current")


class _ControllerBGIRate_Type(Integer32):
    """Custom type controllerBGIRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerBGIRate_Type.__name__ = "Integer32"
_ControllerBGIRate_Object = MibTableColumn
controllerBGIRate = _ControllerBGIRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 50),
    _ControllerBGIRate_Type()
)
controllerBGIRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBGIRate.setStatus("current")


class _ControllerCheckConsistencyRate_Type(Integer32):
    """Custom type controllerCheckConsistencyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ControllerCheckConsistencyRate_Type.__name__ = "Integer32"
_ControllerCheckConsistencyRate_Object = MibTableColumn
controllerCheckConsistencyRate = _ControllerCheckConsistencyRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 51),
    _ControllerCheckConsistencyRate_Type()
)
controllerCheckConsistencyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCheckConsistencyRate.setStatus("current")


class _ControllerPatrolReadMode_Type(Integer32):
    """Custom type controllerPatrolReadMode based on Integer32"""
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
        *(("auto", 4),
          ("disabled", 3),
          ("manual", 5),
          ("notSupported", 2),
          ("other", 1))
    )


_ControllerPatrolReadMode_Type.__name__ = "Integer32"
_ControllerPatrolReadMode_Object = MibTableColumn
controllerPatrolReadMode = _ControllerPatrolReadMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 52),
    _ControllerPatrolReadMode_Type()
)
controllerPatrolReadMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadMode.setStatus("current")


class _ControllerPatrolReadState_Type(Integer32):
    """Custom type controllerPatrolReadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("other", 1),
          ("stopped", 2))
    )


_ControllerPatrolReadState_Type.__name__ = "Integer32"
_ControllerPatrolReadState_Object = MibTableColumn
controllerPatrolReadState = _ControllerPatrolReadState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 53),
    _ControllerPatrolReadState_Type()
)
controllerPatrolReadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPatrolReadState.setStatus("current")
_ControllerPersistentHotSpare_Type = BooleanType
_ControllerPersistentHotSpare_Object = MibTableColumn
controllerPersistentHotSpare = _ControllerPersistentHotSpare_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 59),
    _ControllerPersistentHotSpare_Type()
)
controllerPersistentHotSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPersistentHotSpare.setStatus("current")
_ControllerSpinDownUnconfiguredDrives_Type = BooleanType
_ControllerSpinDownUnconfiguredDrives_Object = MibTableColumn
controllerSpinDownUnconfiguredDrives = _ControllerSpinDownUnconfiguredDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 60),
    _ControllerSpinDownUnconfiguredDrives_Type()
)
controllerSpinDownUnconfiguredDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownUnconfiguredDrives.setStatus("current")
_ControllerSpinDownHotSpareDrives_Type = BooleanType
_ControllerSpinDownHotSpareDrives_Object = MibTableColumn
controllerSpinDownHotSpareDrives = _ControllerSpinDownHotSpareDrives_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 61),
    _ControllerSpinDownHotSpareDrives_Type()
)
controllerSpinDownHotSpareDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownHotSpareDrives.setStatus("current")


class _ControllerSpinDownTimeInterval_Type(Integer32):
    """Custom type controllerSpinDownTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_ControllerSpinDownTimeInterval_Type.__name__ = "Integer32"
_ControllerSpinDownTimeInterval_Object = MibTableColumn
controllerSpinDownTimeInterval = _ControllerSpinDownTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 62),
    _ControllerSpinDownTimeInterval_Type()
)
controllerSpinDownTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSpinDownTimeInterval.setStatus("current")
_ControllerPreservedCache_Type = BooleanType
_ControllerPreservedCache_Object = MibTableColumn
controllerPreservedCache = _ControllerPreservedCache_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 69),
    _ControllerPreservedCache_Type()
)
controllerPreservedCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerPreservedCache.setStatus("current")


class _ControllerCheckConsistencyMode_Type(Integer32):
    """Custom type controllerCheckConsistencyMode based on Integer32"""
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
        *(("normal", 3),
          ("other", 1),
          ("stopOnError", 4),
          ("unsupported", 2))
    )


_ControllerCheckConsistencyMode_Type.__name__ = "Integer32"
_ControllerCheckConsistencyMode_Object = MibTableColumn
controllerCheckConsistencyMode = _ControllerCheckConsistencyMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 70),
    _ControllerCheckConsistencyMode_Type()
)
controllerCheckConsistencyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCheckConsistencyMode.setStatus("current")


class _ControllerCopyBackMode_Type(Integer32):
    """Custom type controllerCopyBackMode based on Integer32"""
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
        *(("off", 5),
          ("on", 3),
          ("onWithSmart", 4),
          ("other", 1),
          ("unsupported", 2))
    )


_ControllerCopyBackMode_Type.__name__ = "Integer32"
_ControllerCopyBackMode_Object = MibTableColumn
controllerCopyBackMode = _ControllerCopyBackMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 71),
    _ControllerCopyBackMode_Type()
)
controllerCopyBackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerCopyBackMode.setStatus("current")


class _ControllerSecurityStatus_Type(Integer32):
    """Custom type controllerSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lkm", 3),
          ("none", 2),
          ("unknown", 1))
    )


_ControllerSecurityStatus_Type.__name__ = "Integer32"
_ControllerSecurityStatus_Object = MibTableColumn
controllerSecurityStatus = _ControllerSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 72),
    _ControllerSecurityStatus_Type()
)
controllerSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSecurityStatus.setStatus("current")
_ControllerEncryptionKeyPresent_Type = BooleanType
_ControllerEncryptionKeyPresent_Object = MibTableColumn
controllerEncryptionKeyPresent = _ControllerEncryptionKeyPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 73),
    _ControllerEncryptionKeyPresent_Type()
)
controllerEncryptionKeyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionKeyPresent.setStatus("current")


class _ControllerEncryptionCapability_Type(Integer32):
    """Custom type controllerEncryptionCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lkm", 3),
          ("none", 2),
          ("other", 1))
    )


_ControllerEncryptionCapability_Type.__name__ = "Integer32"
_ControllerEncryptionCapability_Object = MibTableColumn
controllerEncryptionCapability = _ControllerEncryptionCapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 74),
    _ControllerEncryptionCapability_Type()
)
controllerEncryptionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEncryptionCapability.setStatus("current")


class _ControllerLoadBalanceSetting_Type(Integer32):
    """Custom type controllerLoadBalanceSetting based on Integer32"""
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
        *(("auto", 3),
          ("none", 4),
          ("other", 1),
          ("unsupported", 2))
    )


_ControllerLoadBalanceSetting_Type.__name__ = "Integer32"
_ControllerLoadBalanceSetting_Object = MibTableColumn
controllerLoadBalanceSetting = _ControllerLoadBalanceSetting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 75),
    _ControllerLoadBalanceSetting_Type()
)
controllerLoadBalanceSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerLoadBalanceSetting.setStatus("current")


class _ControllerMaxCapSpeed_Type(Integer32):
    """Custom type controllerMaxCapSpeed based on Integer32"""
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
        *(("oneDotFiveGbps", 2),
          ("sixGbps", 4),
          ("threeGbps", 3),
          ("twelveGbps", 5),
          ("unknown", 1))
    )


_ControllerMaxCapSpeed_Type.__name__ = "Integer32"
_ControllerMaxCapSpeed_Object = MibTableColumn
controllerMaxCapSpeed = _ControllerMaxCapSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 76),
    _ControllerMaxCapSpeed_Type()
)
controllerMaxCapSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerMaxCapSpeed.setStatus("current")
_ControllerSASAddress_Type = DisplayString
_ControllerSASAddress_Object = MibTableColumn
controllerSASAddress = _ControllerSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 77),
    _ControllerSASAddress_Type()
)
controllerSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerSASAddress.setStatus("current")
_ControllerFQDD_Type = FQDDString
_ControllerFQDD_Object = MibTableColumn
controllerFQDD = _ControllerFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 78),
    _ControllerFQDD_Type()
)
controllerFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerFQDD.setStatus("current")
_ControllerDisplayName_Type = DisplayString
_ControllerDisplayName_Object = MibTableColumn
controllerDisplayName = _ControllerDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 79),
    _ControllerDisplayName_Type()
)
controllerDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerDisplayName.setStatus("current")


class _ControllerT10PICapability_Type(Integer32):
    """Custom type controllerT10PICapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capable", 2),
          ("notCapable", 3),
          ("other", 1))
    )


_ControllerT10PICapability_Type.__name__ = "Integer32"
_ControllerT10PICapability_Object = MibTableColumn
controllerT10PICapability = _ControllerT10PICapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 80),
    _ControllerT10PICapability_Type()
)
controllerT10PICapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerT10PICapability.setStatus("current")
_ControllerRAID10UnevenSpansSupported_Type = BooleanType
_ControllerRAID10UnevenSpansSupported_Object = MibTableColumn
controllerRAID10UnevenSpansSupported = _ControllerRAID10UnevenSpansSupported_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 81),
    _ControllerRAID10UnevenSpansSupported_Type()
)
controllerRAID10UnevenSpansSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerRAID10UnevenSpansSupported.setStatus("current")


class _ControllerEnhancedAutoImportForeignConfigMode_Type(Integer32):
    """Custom type controllerEnhancedAutoImportForeignConfigMode based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_ControllerEnhancedAutoImportForeignConfigMode_Type.__name__ = "Integer32"
_ControllerEnhancedAutoImportForeignConfigMode_Object = MibTableColumn
controllerEnhancedAutoImportForeignConfigMode = _ControllerEnhancedAutoImportForeignConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 82),
    _ControllerEnhancedAutoImportForeignConfigMode_Type()
)
controllerEnhancedAutoImportForeignConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerEnhancedAutoImportForeignConfigMode.setStatus("current")
_ControllerBootModeSupported_Type = BooleanType
_ControllerBootModeSupported_Object = MibTableColumn
controllerBootModeSupported = _ControllerBootModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 83),
    _ControllerBootModeSupported_Type()
)
controllerBootModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBootModeSupported.setStatus("current")


class _ControllerBootMode_Type(Integer32):
    """Custom type controllerBootMode based on Integer32"""
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
        *(("contOnError", 3),
          ("headlessContOnError", 4),
          ("headlessSafe", 5),
          ("notApplicable", 1),
          ("user", 2))
    )


_ControllerBootMode_Type.__name__ = "Integer32"
_ControllerBootMode_Object = MibTableColumn
controllerBootMode = _ControllerBootMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 1, 1, 84),
    _ControllerBootMode_Type()
)
controllerBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerBootMode.setStatus("current")
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("current")
_EnclosureTableEntry_Object = MibTableRow
enclosureTableEntry = _EnclosureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1)
)
enclosureTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "enclosureNumber"),
)
if mibBuilder.loadTexts:
    enclosureTableEntry.setStatus("current")


class _EnclosureNumber_Type(Integer32):
    """Custom type enclosureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureNumber_Type.__name__ = "Integer32"
_EnclosureNumber_Object = MibTableColumn
enclosureNumber = _EnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 1),
    _EnclosureNumber_Type()
)
enclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumber.setStatus("current")
_EnclosureName_Type = DisplayString
_EnclosureName_Object = MibTableColumn
enclosureName = _EnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 2),
    _EnclosureName_Type()
)
enclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureName.setStatus("current")


class _EnclosureState_Type(Integer32):
    """Custom type enclosureState based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("missing", 4),
          ("ready", 2),
          ("unknown", 1))
    )


_EnclosureState_Type.__name__ = "Integer32"
_EnclosureState_Object = MibTableColumn
enclosureState = _EnclosureState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 4),
    _EnclosureState_Type()
)
enclosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureState.setStatus("current")
_EnclosureServiceTag_Type = DisplayString
_EnclosureServiceTag_Object = MibTableColumn
enclosureServiceTag = _EnclosureServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 8),
    _EnclosureServiceTag_Type()
)
enclosureServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureServiceTag.setStatus("current")
_EnclosureAssetTag_Type = DisplayString
_EnclosureAssetTag_Object = MibTableColumn
enclosureAssetTag = _EnclosureAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 9),
    _EnclosureAssetTag_Type()
)
enclosureAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureAssetTag.setStatus("current")
_EnclosureConnectedPort_Type = DisplayString
_EnclosureConnectedPort_Object = MibTableColumn
enclosureConnectedPort = _EnclosureConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 19),
    _EnclosureConnectedPort_Type()
)
enclosureConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureConnectedPort.setStatus("current")
_EnclosureRollUpStatus_Type = ObjectStatusEnum
_EnclosureRollUpStatus_Object = MibTableColumn
enclosureRollUpStatus = _EnclosureRollUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 23),
    _EnclosureRollUpStatus_Type()
)
enclosureRollUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureRollUpStatus.setStatus("current")
_EnclosureComponentStatus_Type = ObjectStatusEnum
_EnclosureComponentStatus_Object = MibTableColumn
enclosureComponentStatus = _EnclosureComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 24),
    _EnclosureComponentStatus_Type()
)
enclosureComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureComponentStatus.setStatus("current")
_EnclosureFirmwareVersion_Type = DisplayString
_EnclosureFirmwareVersion_Object = MibTableColumn
enclosureFirmwareVersion = _EnclosureFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 26),
    _EnclosureFirmwareVersion_Type()
)
enclosureFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFirmwareVersion.setStatus("current")
_EnclosureSASAddress_Type = DisplayString
_EnclosureSASAddress_Object = MibTableColumn
enclosureSASAddress = _EnclosureSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 30),
    _EnclosureSASAddress_Type()
)
enclosureSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSASAddress.setStatus("current")
_EnclosureDriveCount_Type = Integer32
_EnclosureDriveCount_Object = MibTableColumn
enclosureDriveCount = _EnclosureDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 31),
    _EnclosureDriveCount_Type()
)
enclosureDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureDriveCount.setStatus("current")
_EnclosureTotalSlots_Type = Integer32
_EnclosureTotalSlots_Object = MibTableColumn
enclosureTotalSlots = _EnclosureTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 32),
    _EnclosureTotalSlots_Type()
)
enclosureTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTotalSlots.setStatus("current")
_EnclosureFanCount_Type = DisplayString
_EnclosureFanCount_Object = MibTableColumn
enclosureFanCount = _EnclosureFanCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 40),
    _EnclosureFanCount_Type()
)
enclosureFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanCount.setStatus("current")
_EnclosurePSUCount_Type = DisplayString
_EnclosurePSUCount_Object = MibTableColumn
enclosurePSUCount = _EnclosurePSUCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 41),
    _EnclosurePSUCount_Type()
)
enclosurePSUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePSUCount.setStatus("current")
_EnclosureEMMCount_Type = DisplayString
_EnclosureEMMCount_Object = MibTableColumn
enclosureEMMCount = _EnclosureEMMCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 42),
    _EnclosureEMMCount_Type()
)
enclosureEMMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureEMMCount.setStatus("current")
_EnclosureTempProbeCount_Type = DisplayString
_EnclosureTempProbeCount_Object = MibTableColumn
enclosureTempProbeCount = _EnclosureTempProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 43),
    _EnclosureTempProbeCount_Type()
)
enclosureTempProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTempProbeCount.setStatus("current")
_EnclosureRedundantPath_Type = DisplayString
_EnclosureRedundantPath_Object = MibTableColumn
enclosureRedundantPath = _EnclosureRedundantPath_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 44),
    _EnclosureRedundantPath_Type()
)
enclosureRedundantPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureRedundantPath.setStatus("current")
_EnclosurePosition_Type = DisplayString
_EnclosurePosition_Object = MibTableColumn
enclosurePosition = _EnclosurePosition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 45),
    _EnclosurePosition_Type()
)
enclosurePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePosition.setStatus("current")
_EnclosureBackplaneBayID_Type = DisplayString
_EnclosureBackplaneBayID_Object = MibTableColumn
enclosureBackplaneBayID = _EnclosureBackplaneBayID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 46),
    _EnclosureBackplaneBayID_Type()
)
enclosureBackplaneBayID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureBackplaneBayID.setStatus("current")
_EnclosureFQDD_Type = FQDDString
_EnclosureFQDD_Object = MibTableColumn
enclosureFQDD = _EnclosureFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 47),
    _EnclosureFQDD_Type()
)
enclosureFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFQDD.setStatus("current")
_EnclosureDisplayName_Type = DisplayString
_EnclosureDisplayName_Object = MibTableColumn
enclosureDisplayName = _EnclosureDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 48),
    _EnclosureDisplayName_Type()
)
enclosureDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureDisplayName.setStatus("current")


class _EnclosureType_Type(Integer32):
    """Custom type enclosureType based on Integer32"""
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
        *(("notApplicable", 2),
          ("other", 1),
          ("pcie", 4),
          ("sassata", 3),
          ("universal", 5))
    )


_EnclosureType_Type.__name__ = "Integer32"
_EnclosureType_Object = MibTableColumn
enclosureType = _EnclosureType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 3, 1, 49),
    _EnclosureType_Type()
)
enclosureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureType.setStatus("current")
_PhysicalDiskTable_Object = MibTable
physicalDiskTable = _PhysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4)
)
if mibBuilder.loadTexts:
    physicalDiskTable.setStatus("current")
_PhysicalDiskTableEntry_Object = MibTableRow
physicalDiskTableEntry = _PhysicalDiskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1)
)
physicalDiskTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "physicalDiskNumber"),
)
if mibBuilder.loadTexts:
    physicalDiskTableEntry.setStatus("current")


class _PhysicalDiskNumber_Type(Integer32):
    """Custom type physicalDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_PhysicalDiskNumber_Type.__name__ = "Integer32"
_PhysicalDiskNumber_Object = MibTableColumn
physicalDiskNumber = _PhysicalDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 1),
    _PhysicalDiskNumber_Type()
)
physicalDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskNumber.setStatus("current")
_PhysicalDiskName_Type = DisplayString
_PhysicalDiskName_Object = MibTableColumn
physicalDiskName = _PhysicalDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 2),
    _PhysicalDiskName_Type()
)
physicalDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskName.setStatus("current")
_PhysicalDiskManufacturer_Type = DisplayString
_PhysicalDiskManufacturer_Object = MibTableColumn
physicalDiskManufacturer = _PhysicalDiskManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 3),
    _PhysicalDiskManufacturer_Type()
)
physicalDiskManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufacturer.setStatus("current")


class _PhysicalDiskState_Type(Integer32):
    """Custom type physicalDiskState based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 6),
          ("failed", 7),
          ("foreign", 4),
          ("nonraid", 8),
          ("offline", 5),
          ("online", 3),
          ("readonly", 10),
          ("ready", 2),
          ("removed", 9),
          ("unknown", 1))
    )


_PhysicalDiskState_Type.__name__ = "Integer32"
_PhysicalDiskState_Object = MibTableColumn
physicalDiskState = _PhysicalDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 4),
    _PhysicalDiskState_Type()
)
physicalDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskState.setStatus("current")
_PhysicalDiskProductID_Type = DisplayString
_PhysicalDiskProductID_Object = MibTableColumn
physicalDiskProductID = _PhysicalDiskProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 6),
    _PhysicalDiskProductID_Type()
)
physicalDiskProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskProductID.setStatus("current")
_PhysicalDiskSerialNo_Type = DisplayString
_PhysicalDiskSerialNo_Object = MibTableColumn
physicalDiskSerialNo = _PhysicalDiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 7),
    _PhysicalDiskSerialNo_Type()
)
physicalDiskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSerialNo.setStatus("current")
_PhysicalDiskRevision_Type = DisplayString
_PhysicalDiskRevision_Object = MibTableColumn
physicalDiskRevision = _PhysicalDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 8),
    _PhysicalDiskRevision_Type()
)
physicalDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskRevision.setStatus("current")
_PhysicalDiskCapacityInMB_Type = Integer32
_PhysicalDiskCapacityInMB_Object = MibTableColumn
physicalDiskCapacityInMB = _PhysicalDiskCapacityInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 11),
    _PhysicalDiskCapacityInMB_Type()
)
physicalDiskCapacityInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskCapacityInMB.setStatus("current")
_PhysicalDiskUsedSpaceInMB_Type = Integer32
_PhysicalDiskUsedSpaceInMB_Object = MibTableColumn
physicalDiskUsedSpaceInMB = _PhysicalDiskUsedSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 17),
    _PhysicalDiskUsedSpaceInMB_Type()
)
physicalDiskUsedSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskUsedSpaceInMB.setStatus("current")
_PhysicalDiskFreeSpaceInMB_Type = Integer32
_PhysicalDiskFreeSpaceInMB_Object = MibTableColumn
physicalDiskFreeSpaceInMB = _PhysicalDiskFreeSpaceInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 19),
    _PhysicalDiskFreeSpaceInMB_Type()
)
physicalDiskFreeSpaceInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFreeSpaceInMB.setStatus("current")


class _PhysicalDiskBusType_Type(Integer32):
    """Custom type physicalDiskBusType based on Integer32"""
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
        *(("fibre", 5),
          ("pcie", 6),
          ("sas", 3),
          ("sata", 4),
          ("scsi", 2),
          ("unknown", 1))
    )


_PhysicalDiskBusType_Type.__name__ = "Integer32"
_PhysicalDiskBusType_Object = MibTableColumn
physicalDiskBusType = _PhysicalDiskBusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 21),
    _PhysicalDiskBusType_Type()
)
physicalDiskBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskBusType.setStatus("current")


class _PhysicalDiskSpareState_Type(Integer32):
    """Custom type physicalDiskSpareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedHotSpare", 2),
          ("globalHotSpare", 3),
          ("notASpare", 1))
    )


_PhysicalDiskSpareState_Type.__name__ = "Integer32"
_PhysicalDiskSpareState_Object = MibTableColumn
physicalDiskSpareState = _PhysicalDiskSpareState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 22),
    _PhysicalDiskSpareState_Type()
)
physicalDiskSpareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSpareState.setStatus("current")
_PhysicalDiskComponentStatus_Type = ObjectStatusEnum
_PhysicalDiskComponentStatus_Object = MibTableColumn
physicalDiskComponentStatus = _PhysicalDiskComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 24),
    _PhysicalDiskComponentStatus_Type()
)
physicalDiskComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskComponentStatus.setStatus("current")
_PhysicalDiskPartNumber_Type = DisplayString
_PhysicalDiskPartNumber_Object = MibTableColumn
physicalDiskPartNumber = _PhysicalDiskPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 27),
    _PhysicalDiskPartNumber_Type()
)
physicalDiskPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPartNumber.setStatus("current")
_PhysicalDiskSASAddress_Type = DisplayString
_PhysicalDiskSASAddress_Object = MibTableColumn
physicalDiskSASAddress = _PhysicalDiskSASAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 28),
    _PhysicalDiskSASAddress_Type()
)
physicalDiskSASAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSASAddress.setStatus("current")


class _PhysicalDiskNegotiatedSpeed_Type(Integer32):
    """Custom type physicalDiskNegotiatedSpeed based on Integer32"""
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
        *(("eightGTps", 7),
          ("fiveGTps", 6),
          ("oneDotFiveGbps", 2),
          ("sixGbps", 4),
          ("threeGbps", 3),
          ("twelveGbps", 5),
          ("unknown", 1))
    )


_PhysicalDiskNegotiatedSpeed_Type.__name__ = "Integer32"
_PhysicalDiskNegotiatedSpeed_Object = MibTableColumn
physicalDiskNegotiatedSpeed = _PhysicalDiskNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 29),
    _PhysicalDiskNegotiatedSpeed_Type()
)
physicalDiskNegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskNegotiatedSpeed.setStatus("current")


class _PhysicalDiskCapableSpeed_Type(Integer32):
    """Custom type physicalDiskCapableSpeed based on Integer32"""
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
        *(("eightGTps", 7),
          ("fiveGTps", 6),
          ("oneDotFiveGbps", 2),
          ("sixGbps", 4),
          ("threeGbps", 3),
          ("twelveGbps", 5),
          ("unknown", 1))
    )


_PhysicalDiskCapableSpeed_Type.__name__ = "Integer32"
_PhysicalDiskCapableSpeed_Object = MibTableColumn
physicalDiskCapableSpeed = _PhysicalDiskCapableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 30),
    _PhysicalDiskCapableSpeed_Type()
)
physicalDiskCapableSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskCapableSpeed.setStatus("current")
_PhysicalDiskSmartAlertIndication_Type = BooleanType
_PhysicalDiskSmartAlertIndication_Object = MibTableColumn
physicalDiskSmartAlertIndication = _PhysicalDiskSmartAlertIndication_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 31),
    _PhysicalDiskSmartAlertIndication_Type()
)
physicalDiskSmartAlertIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSmartAlertIndication.setStatus("current")
_PhysicalDiskManufactureDay_Type = DisplayString
_PhysicalDiskManufactureDay_Object = MibTableColumn
physicalDiskManufactureDay = _PhysicalDiskManufactureDay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 32),
    _PhysicalDiskManufactureDay_Type()
)
physicalDiskManufactureDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufactureDay.setStatus("current")
_PhysicalDiskManufactureWeek_Type = DisplayString
_PhysicalDiskManufactureWeek_Object = MibTableColumn
physicalDiskManufactureWeek = _PhysicalDiskManufactureWeek_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 33),
    _PhysicalDiskManufactureWeek_Type()
)
physicalDiskManufactureWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufactureWeek.setStatus("current")
_PhysicalDiskManufactureYear_Type = DisplayString
_PhysicalDiskManufactureYear_Object = MibTableColumn
physicalDiskManufactureYear = _PhysicalDiskManufactureYear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 34),
    _PhysicalDiskManufactureYear_Type()
)
physicalDiskManufactureYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskManufactureYear.setStatus("current")


class _PhysicalDiskMediaType_Type(Integer32):
    """Custom type physicalDiskMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdd", 2),
          ("ssd", 3),
          ("unknown", 1))
    )


_PhysicalDiskMediaType_Type.__name__ = "Integer32"
_PhysicalDiskMediaType_Object = MibTableColumn
physicalDiskMediaType = _PhysicalDiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 35),
    _PhysicalDiskMediaType_Type()
)
physicalDiskMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskMediaType.setStatus("current")


class _PhysicalDiskPowerState_Type(Integer32):
    """Custom type physicalDiskPowerState based on Integer32"""
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
        *(("on", 5),
          ("other", 1),
          ("spunDown", 3),
          ("spunUp", 2),
          ("transition", 4))
    )


_PhysicalDiskPowerState_Type.__name__ = "Integer32"
_PhysicalDiskPowerState_Object = MibTableColumn
physicalDiskPowerState = _PhysicalDiskPowerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 42),
    _PhysicalDiskPowerState_Type()
)
physicalDiskPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPowerState.setStatus("current")


class _PhysicalDiskRemainingRatedWriteEndurance_Type(Integer32):
    """Custom type physicalDiskRemainingRatedWriteEndurance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhysicalDiskRemainingRatedWriteEndurance_Type.__name__ = "Integer32"
_PhysicalDiskRemainingRatedWriteEndurance_Object = MibTableColumn
physicalDiskRemainingRatedWriteEndurance = _PhysicalDiskRemainingRatedWriteEndurance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 49),
    _PhysicalDiskRemainingRatedWriteEndurance_Type()
)
physicalDiskRemainingRatedWriteEndurance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskRemainingRatedWriteEndurance.setStatus("current")


class _PhysicalDiskOperationalState_Type(Integer32):
    """Custom type physicalDiskOperationalState based on Integer32"""
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
        *(("clear", 3),
          ("copyback", 4),
          ("notApplicable", 1),
          ("rebuild", 2))
    )


_PhysicalDiskOperationalState_Type.__name__ = "Integer32"
_PhysicalDiskOperationalState_Object = MibTableColumn
physicalDiskOperationalState = _PhysicalDiskOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 50),
    _PhysicalDiskOperationalState_Type()
)
physicalDiskOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskOperationalState.setStatus("current")


class _PhysicalDiskProgress_Type(Integer32):
    """Custom type physicalDiskProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PhysicalDiskProgress_Type.__name__ = "Integer32"
_PhysicalDiskProgress_Object = MibTableColumn
physicalDiskProgress = _PhysicalDiskProgress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 51),
    _PhysicalDiskProgress_Type()
)
physicalDiskProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskProgress.setStatus("current")


class _PhysicalDiskSecurityStatus_Type(Integer32):
    """Custom type physicalDiskSecurityStatus based on Integer32"""
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
        *(("foreign", 5),
          ("locked", 4),
          ("notSupported", 2),
          ("secured", 3),
          ("supported", 1))
    )


_PhysicalDiskSecurityStatus_Type.__name__ = "Integer32"
_PhysicalDiskSecurityStatus_Object = MibTableColumn
physicalDiskSecurityStatus = _PhysicalDiskSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 52),
    _PhysicalDiskSecurityStatus_Type()
)
physicalDiskSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskSecurityStatus.setStatus("current")


class _PhysicalDiskFormFactor_Type(Integer32):
    """Custom type physicalDiskFormFactor based on Integer32"""
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
        *(("oneDotEight", 2),
          ("threeDotFive", 4),
          ("twoDotFive", 3),
          ("unknown", 1))
    )


_PhysicalDiskFormFactor_Type.__name__ = "Integer32"
_PhysicalDiskFormFactor_Object = MibTableColumn
physicalDiskFormFactor = _PhysicalDiskFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 53),
    _PhysicalDiskFormFactor_Type()
)
physicalDiskFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFormFactor.setStatus("current")
_PhysicalDiskFQDD_Type = FQDDString
_PhysicalDiskFQDD_Object = MibTableColumn
physicalDiskFQDD = _PhysicalDiskFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 54),
    _PhysicalDiskFQDD_Type()
)
physicalDiskFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskFQDD.setStatus("current")
_PhysicalDiskDisplayName_Type = DisplayString
_PhysicalDiskDisplayName_Object = MibTableColumn
physicalDiskDisplayName = _PhysicalDiskDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 55),
    _PhysicalDiskDisplayName_Type()
)
physicalDiskDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskDisplayName.setStatus("current")


class _PhysicalDiskT10PICapability_Type(Integer32):
    """Custom type physicalDiskT10PICapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capable", 2),
          ("notCapable", 3),
          ("other", 1))
    )


_PhysicalDiskT10PICapability_Type.__name__ = "Integer32"
_PhysicalDiskT10PICapability_Object = MibTableColumn
physicalDiskT10PICapability = _PhysicalDiskT10PICapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 57),
    _PhysicalDiskT10PICapability_Type()
)
physicalDiskT10PICapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskT10PICapability.setStatus("current")
_PhysicalDiskBlockSizeInBytes_Type = Integer32
_PhysicalDiskBlockSizeInBytes_Object = MibTableColumn
physicalDiskBlockSizeInBytes = _PhysicalDiskBlockSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 58),
    _PhysicalDiskBlockSizeInBytes_Type()
)
physicalDiskBlockSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskBlockSizeInBytes.setStatus("current")
_PhysicalDiskProtocolVersion_Type = DisplayString
_PhysicalDiskProtocolVersion_Object = MibTableColumn
physicalDiskProtocolVersion = _PhysicalDiskProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 59),
    _PhysicalDiskProtocolVersion_Type()
)
physicalDiskProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskProtocolVersion.setStatus("current")


class _PhysicalDiskPCIeNegotiatedLinkWidth_Type(Integer32):
    """Custom type physicalDiskPCIeNegotiatedLinkWidth based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("byEight", 6),
          ("byFour", 5),
          ("byOne", 3),
          ("bySixteen", 7),
          ("byThirtyTwp", 8),
          ("byTwp", 4),
          ("notApplicable", 2),
          ("other", 1))
    )


_PhysicalDiskPCIeNegotiatedLinkWidth_Type.__name__ = "Integer32"
_PhysicalDiskPCIeNegotiatedLinkWidth_Object = MibTableColumn
physicalDiskPCIeNegotiatedLinkWidth = _PhysicalDiskPCIeNegotiatedLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 60),
    _PhysicalDiskPCIeNegotiatedLinkWidth_Type()
)
physicalDiskPCIeNegotiatedLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPCIeNegotiatedLinkWidth.setStatus("current")


class _PhysicalDiskPCIeCapableLinkWidth_Type(Integer32):
    """Custom type physicalDiskPCIeCapableLinkWidth based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("byEight", 6),
          ("byFour", 5),
          ("byOne", 3),
          ("bySixteen", 7),
          ("byThirtyTwp", 8),
          ("byTwp", 4),
          ("notApplicable", 2),
          ("other", 1))
    )


_PhysicalDiskPCIeCapableLinkWidth_Type.__name__ = "Integer32"
_PhysicalDiskPCIeCapableLinkWidth_Object = MibTableColumn
physicalDiskPCIeCapableLinkWidth = _PhysicalDiskPCIeCapableLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 4, 1, 61),
    _PhysicalDiskPCIeCapableLinkWidth_Type()
)
physicalDiskPCIeCapableLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalDiskPCIeCapableLinkWidth.setStatus("current")
_EnclosureFanTable_Object = MibTable
enclosureFanTable = _EnclosureFanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7)
)
if mibBuilder.loadTexts:
    enclosureFanTable.setStatus("current")
_EnclosureFanTableEntry_Object = MibTableRow
enclosureFanTableEntry = _EnclosureFanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1)
)
enclosureFanTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "enclosureFanNumber"),
)
if mibBuilder.loadTexts:
    enclosureFanTableEntry.setStatus("current")


class _EnclosureFanNumber_Type(Integer32):
    """Custom type enclosureFanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureFanNumber_Type.__name__ = "Integer32"
_EnclosureFanNumber_Object = MibTableColumn
enclosureFanNumber = _EnclosureFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 1),
    _EnclosureFanNumber_Type()
)
enclosureFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanNumber.setStatus("current")
_EnclosureFanName_Type = DisplayString
_EnclosureFanName_Object = MibTableColumn
enclosureFanName = _EnclosureFanName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 2),
    _EnclosureFanName_Type()
)
enclosureFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanName.setStatus("current")


class _EnclosureFanState_Type(Integer32):
    """Custom type enclosureFanState based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("missing", 4),
          ("ready", 2),
          ("unknown", 1))
    )


_EnclosureFanState_Type.__name__ = "Integer32"
_EnclosureFanState_Object = MibTableColumn
enclosureFanState = _EnclosureFanState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 4),
    _EnclosureFanState_Type()
)
enclosureFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanState.setStatus("current")


class _EnclosureFanSpeed_Type(Integer32):
    """Custom type enclosureFanSpeed based on Integer32"""
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
        *(("fast", 5),
          ("medium", 4),
          ("slow", 3),
          ("stopped", 2),
          ("unknown", 1))
    )


_EnclosureFanSpeed_Type.__name__ = "Integer32"
_EnclosureFanSpeed_Object = MibTableColumn
enclosureFanSpeed = _EnclosureFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 11),
    _EnclosureFanSpeed_Type()
)
enclosureFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanSpeed.setStatus("current")
_EnclosureFanComponentStatus_Type = ObjectStatusEnum
_EnclosureFanComponentStatus_Object = MibTableColumn
enclosureFanComponentStatus = _EnclosureFanComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 15),
    _EnclosureFanComponentStatus_Type()
)
enclosureFanComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanComponentStatus.setStatus("current")
_EnclosureFanFQDD_Type = FQDDString
_EnclosureFanFQDD_Object = MibTableColumn
enclosureFanFQDD = _EnclosureFanFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 20),
    _EnclosureFanFQDD_Type()
)
enclosureFanFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanFQDD.setStatus("current")
_EnclosureFanDisplayName_Type = DisplayString
_EnclosureFanDisplayName_Object = MibTableColumn
enclosureFanDisplayName = _EnclosureFanDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 7, 1, 21),
    _EnclosureFanDisplayName_Type()
)
enclosureFanDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureFanDisplayName.setStatus("current")
_EnclosurePowerSupplyTable_Object = MibTable
enclosurePowerSupplyTable = _EnclosurePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9)
)
if mibBuilder.loadTexts:
    enclosurePowerSupplyTable.setStatus("current")
_EnclosurePowerSupplyTableEntry_Object = MibTableRow
enclosurePowerSupplyTableEntry = _EnclosurePowerSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1)
)
enclosurePowerSupplyTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "enclosurePowerSupplyNumber"),
)
if mibBuilder.loadTexts:
    enclosurePowerSupplyTableEntry.setStatus("current")


class _EnclosurePowerSupplyNumber_Type(Integer32):
    """Custom type enclosurePowerSupplyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosurePowerSupplyNumber_Type.__name__ = "Integer32"
_EnclosurePowerSupplyNumber_Object = MibTableColumn
enclosurePowerSupplyNumber = _EnclosurePowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 1),
    _EnclosurePowerSupplyNumber_Type()
)
enclosurePowerSupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyNumber.setStatus("current")
_EnclosurePowerSupplyName_Type = DisplayString
_EnclosurePowerSupplyName_Object = MibTableColumn
enclosurePowerSupplyName = _EnclosurePowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 2),
    _EnclosurePowerSupplyName_Type()
)
enclosurePowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyName.setStatus("current")


class _EnclosurePowerSupplyState_Type(Integer32):
    """Custom type enclosurePowerSupplyState based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("missing", 4),
          ("ready", 2),
          ("unknown", 1))
    )


_EnclosurePowerSupplyState_Type.__name__ = "Integer32"
_EnclosurePowerSupplyState_Object = MibTableColumn
enclosurePowerSupplyState = _EnclosurePowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 4),
    _EnclosurePowerSupplyState_Type()
)
enclosurePowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyState.setStatus("current")
_EnclosurePowerSupplyPartNumber_Type = DisplayString
_EnclosurePowerSupplyPartNumber_Object = MibTableColumn
enclosurePowerSupplyPartNumber = _EnclosurePowerSupplyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 7),
    _EnclosurePowerSupplyPartNumber_Type()
)
enclosurePowerSupplyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyPartNumber.setStatus("current")
_EnclosurePowerSupplyComponentStatus_Type = ObjectStatusEnum
_EnclosurePowerSupplyComponentStatus_Object = MibTableColumn
enclosurePowerSupplyComponentStatus = _EnclosurePowerSupplyComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 9),
    _EnclosurePowerSupplyComponentStatus_Type()
)
enclosurePowerSupplyComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyComponentStatus.setStatus("current")
_EnclosurePowerSupplyFQDD_Type = FQDDString
_EnclosurePowerSupplyFQDD_Object = MibTableColumn
enclosurePowerSupplyFQDD = _EnclosurePowerSupplyFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 15),
    _EnclosurePowerSupplyFQDD_Type()
)
enclosurePowerSupplyFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyFQDD.setStatus("current")
_EnclosurePowerSupplyDisplayName_Type = DisplayString
_EnclosurePowerSupplyDisplayName_Object = MibTableColumn
enclosurePowerSupplyDisplayName = _EnclosurePowerSupplyDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 9, 1, 16),
    _EnclosurePowerSupplyDisplayName_Type()
)
enclosurePowerSupplyDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePowerSupplyDisplayName.setStatus("current")
_EnclosureTemperatureProbeTable_Object = MibTable
enclosureTemperatureProbeTable = _EnclosureTemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11)
)
if mibBuilder.loadTexts:
    enclosureTemperatureProbeTable.setStatus("current")
_EnclosureTemperatureProbeTableEntry_Object = MibTableRow
enclosureTemperatureProbeTableEntry = _EnclosureTemperatureProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1)
)
enclosureTemperatureProbeTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "enclosureTemperatureProbeNumber"),
)
if mibBuilder.loadTexts:
    enclosureTemperatureProbeTableEntry.setStatus("current")


class _EnclosureTemperatureProbeNumber_Type(Integer32):
    """Custom type enclosureTemperatureProbeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureTemperatureProbeNumber_Type.__name__ = "Integer32"
_EnclosureTemperatureProbeNumber_Object = MibTableColumn
enclosureTemperatureProbeNumber = _EnclosureTemperatureProbeNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 1),
    _EnclosureTemperatureProbeNumber_Type()
)
enclosureTemperatureProbeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeNumber.setStatus("current")
_EnclosureTemperatureProbeName_Type = DisplayString
_EnclosureTemperatureProbeName_Object = MibTableColumn
enclosureTemperatureProbeName = _EnclosureTemperatureProbeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 2),
    _EnclosureTemperatureProbeName_Type()
)
enclosureTemperatureProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeName.setStatus("current")


class _EnclosureTemperatureProbeState_Type(Integer32):
    """Custom type enclosureTemperatureProbeState based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("missing", 4),
          ("ready", 2),
          ("unknown", 1))
    )


_EnclosureTemperatureProbeState_Type.__name__ = "Integer32"
_EnclosureTemperatureProbeState_Object = MibTableColumn
enclosureTemperatureProbeState = _EnclosureTemperatureProbeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 4),
    _EnclosureTemperatureProbeState_Type()
)
enclosureTemperatureProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeState.setStatus("current")
_EnclosureTemperatureProbeMinWarningValue_Type = Integer32
_EnclosureTemperatureProbeMinWarningValue_Object = MibTableColumn
enclosureTemperatureProbeMinWarningValue = _EnclosureTemperatureProbeMinWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 7),
    _EnclosureTemperatureProbeMinWarningValue_Type()
)
enclosureTemperatureProbeMinWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMinWarningValue.setStatus("current")
_EnclosureTemperatureProbeMinCriticalValue_Type = Integer32
_EnclosureTemperatureProbeMinCriticalValue_Object = MibTableColumn
enclosureTemperatureProbeMinCriticalValue = _EnclosureTemperatureProbeMinCriticalValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 8),
    _EnclosureTemperatureProbeMinCriticalValue_Type()
)
enclosureTemperatureProbeMinCriticalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMinCriticalValue.setStatus("current")
_EnclosureTemperatureProbeMaxWarningValue_Type = Integer32
_EnclosureTemperatureProbeMaxWarningValue_Object = MibTableColumn
enclosureTemperatureProbeMaxWarningValue = _EnclosureTemperatureProbeMaxWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 9),
    _EnclosureTemperatureProbeMaxWarningValue_Type()
)
enclosureTemperatureProbeMaxWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMaxWarningValue.setStatus("current")
_EnclosureTemperatureProbeMaxCriticalValue_Type = Integer32
_EnclosureTemperatureProbeMaxCriticalValue_Object = MibTableColumn
enclosureTemperatureProbeMaxCriticalValue = _EnclosureTemperatureProbeMaxCriticalValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 10),
    _EnclosureTemperatureProbeMaxCriticalValue_Type()
)
enclosureTemperatureProbeMaxCriticalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeMaxCriticalValue.setStatus("current")
_EnclosureTemperatureProbeCurValue_Type = Integer32
_EnclosureTemperatureProbeCurValue_Object = MibTableColumn
enclosureTemperatureProbeCurValue = _EnclosureTemperatureProbeCurValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 11),
    _EnclosureTemperatureProbeCurValue_Type()
)
enclosureTemperatureProbeCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeCurValue.setStatus("current")
_EnclosureTemperatureProbeComponentStatus_Type = ObjectStatusEnum
_EnclosureTemperatureProbeComponentStatus_Object = MibTableColumn
enclosureTemperatureProbeComponentStatus = _EnclosureTemperatureProbeComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 13),
    _EnclosureTemperatureProbeComponentStatus_Type()
)
enclosureTemperatureProbeComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeComponentStatus.setStatus("current")
_EnclosureTemperatureProbeFQDD_Type = FQDDString
_EnclosureTemperatureProbeFQDD_Object = MibTableColumn
enclosureTemperatureProbeFQDD = _EnclosureTemperatureProbeFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 15),
    _EnclosureTemperatureProbeFQDD_Type()
)
enclosureTemperatureProbeFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeFQDD.setStatus("current")
_EnclosureTemperatureProbeDisplayName_Type = DisplayString
_EnclosureTemperatureProbeDisplayName_Object = MibTableColumn
enclosureTemperatureProbeDisplayName = _EnclosureTemperatureProbeDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 11, 1, 16),
    _EnclosureTemperatureProbeDisplayName_Type()
)
enclosureTemperatureProbeDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureTemperatureProbeDisplayName.setStatus("current")
_EnclosureManagementModuleTable_Object = MibTable
enclosureManagementModuleTable = _EnclosureManagementModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13)
)
if mibBuilder.loadTexts:
    enclosureManagementModuleTable.setStatus("current")
_EnclosureManagementModuleTableEntry_Object = MibTableRow
enclosureManagementModuleTableEntry = _EnclosureManagementModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1)
)
enclosureManagementModuleTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "enclosureManagementModuleNumber"),
)
if mibBuilder.loadTexts:
    enclosureManagementModuleTableEntry.setStatus("current")


class _EnclosureManagementModuleNumber_Type(Integer32):
    """Custom type enclosureManagementModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EnclosureManagementModuleNumber_Type.__name__ = "Integer32"
_EnclosureManagementModuleNumber_Object = MibTableColumn
enclosureManagementModuleNumber = _EnclosureManagementModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 1),
    _EnclosureManagementModuleNumber_Type()
)
enclosureManagementModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleNumber.setStatus("current")
_EnclosureManagementModuleName_Type = DisplayString
_EnclosureManagementModuleName_Object = MibTableColumn
enclosureManagementModuleName = _EnclosureManagementModuleName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 2),
    _EnclosureManagementModuleName_Type()
)
enclosureManagementModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleName.setStatus("current")


class _EnclosureManagementModuleState_Type(Integer32):
    """Custom type enclosureManagementModuleState based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("missing", 4),
          ("ready", 2),
          ("unknown", 1))
    )


_EnclosureManagementModuleState_Type.__name__ = "Integer32"
_EnclosureManagementModuleState_Object = MibTableColumn
enclosureManagementModuleState = _EnclosureManagementModuleState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 4),
    _EnclosureManagementModuleState_Type()
)
enclosureManagementModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleState.setStatus("current")
_EnclosureManagementModulePartNumber_Type = DisplayString
_EnclosureManagementModulePartNumber_Object = MibTableColumn
enclosureManagementModulePartNumber = _EnclosureManagementModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 6),
    _EnclosureManagementModulePartNumber_Type()
)
enclosureManagementModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModulePartNumber.setStatus("current")
_EnclosureManagementModuleFWVersion_Type = DisplayString
_EnclosureManagementModuleFWVersion_Object = MibTableColumn
enclosureManagementModuleFWVersion = _EnclosureManagementModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 8),
    _EnclosureManagementModuleFWVersion_Type()
)
enclosureManagementModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleFWVersion.setStatus("current")
_EnclosureManagementModuleComponentStatus_Type = ObjectStatusEnum
_EnclosureManagementModuleComponentStatus_Object = MibTableColumn
enclosureManagementModuleComponentStatus = _EnclosureManagementModuleComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 11),
    _EnclosureManagementModuleComponentStatus_Type()
)
enclosureManagementModuleComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleComponentStatus.setStatus("current")
_EnclosureManagementModuleFQDD_Type = FQDDString
_EnclosureManagementModuleFQDD_Object = MibTableColumn
enclosureManagementModuleFQDD = _EnclosureManagementModuleFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 15),
    _EnclosureManagementModuleFQDD_Type()
)
enclosureManagementModuleFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleFQDD.setStatus("current")
_EnclosureManagementModuleDisplayName_Type = DisplayString
_EnclosureManagementModuleDisplayName_Object = MibTableColumn
enclosureManagementModuleDisplayName = _EnclosureManagementModuleDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 13, 1, 16),
    _EnclosureManagementModuleDisplayName_Type()
)
enclosureManagementModuleDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureManagementModuleDisplayName.setStatus("current")
_BatteryTable_Object = MibTable
batteryTable = _BatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15)
)
if mibBuilder.loadTexts:
    batteryTable.setStatus("current")
_BatteryTableEntry_Object = MibTableRow
batteryTableEntry = _BatteryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1)
)
batteryTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "batteryNumber"),
)
if mibBuilder.loadTexts:
    batteryTableEntry.setStatus("current")


class _BatteryNumber_Type(Integer32):
    """Custom type batteryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BatteryNumber_Type.__name__ = "Integer32"
_BatteryNumber_Object = MibTableColumn
batteryNumber = _BatteryNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1, 1),
    _BatteryNumber_Type()
)
batteryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNumber.setStatus("current")


class _BatteryState_Type(Integer32):
    """Custom type batteryState based on Integer32"""
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
        *(("belowThreshold", 7),
          ("charging", 6),
          ("degraded", 4),
          ("failed", 3),
          ("missing", 5),
          ("ready", 2),
          ("unknown", 1))
    )


_BatteryState_Type.__name__ = "Integer32"
_BatteryState_Object = MibTableColumn
batteryState = _BatteryState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1, 4),
    _BatteryState_Type()
)
batteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryState.setStatus("current")
_BatteryComponentStatus_Type = ObjectStatusEnum
_BatteryComponentStatus_Object = MibTableColumn
batteryComponentStatus = _BatteryComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1, 6),
    _BatteryComponentStatus_Type()
)
batteryComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryComponentStatus.setStatus("current")


class _BatteryPredictedCapacity_Type(Integer32):
    """Custom type batteryPredictedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ready", 3),
          ("unknown", 1))
    )


_BatteryPredictedCapacity_Type.__name__ = "Integer32"
_BatteryPredictedCapacity_Object = MibTableColumn
batteryPredictedCapacity = _BatteryPredictedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1, 10),
    _BatteryPredictedCapacity_Type()
)
batteryPredictedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryPredictedCapacity.setStatus("obsolete")
_BatteryFQDD_Type = DisplayString
_BatteryFQDD_Object = MibTableColumn
batteryFQDD = _BatteryFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1, 20),
    _BatteryFQDD_Type()
)
batteryFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFQDD.setStatus("current")
_BatteryDisplayName_Type = DisplayString
_BatteryDisplayName_Object = MibTableColumn
batteryDisplayName = _BatteryDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 130, 15, 1, 21),
    _BatteryDisplayName_Type()
)
batteryDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDisplayName.setStatus("current")
_LogicalDevices_ObjectIdentity = ObjectIdentity
logicalDevices = _LogicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140)
)
_VirtualDiskTable_Object = MibTable
virtualDiskTable = _VirtualDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1)
)
if mibBuilder.loadTexts:
    virtualDiskTable.setStatus("current")
_VirtualDiskTableEntry_Object = MibTableRow
virtualDiskTableEntry = _VirtualDiskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1)
)
virtualDiskTableEntry.setIndexNames(
    (0, "IDRAC-MIB-SMIv2", "virtualDiskNumber"),
)
if mibBuilder.loadTexts:
    virtualDiskTableEntry.setStatus("current")


class _VirtualDiskNumber_Type(Integer32):
    """Custom type virtualDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_VirtualDiskNumber_Type.__name__ = "Integer32"
_VirtualDiskNumber_Object = MibTableColumn
virtualDiskNumber = _VirtualDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 1),
    _VirtualDiskNumber_Type()
)
virtualDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNumber.setStatus("current")
_VirtualDiskName_Type = DisplayString
_VirtualDiskName_Object = MibTableColumn
virtualDiskName = _VirtualDiskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 2),
    _VirtualDiskName_Type()
)
virtualDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskName.setStatus("current")


class _VirtualDiskState_Type(Integer32):
    """Custom type virtualDiskState based on Integer32"""
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
        *(("degraded", 4),
          ("failed", 3),
          ("online", 2),
          ("unknown", 1))
    )


_VirtualDiskState_Type.__name__ = "Integer32"
_VirtualDiskState_Object = MibTableColumn
virtualDiskState = _VirtualDiskState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 4),
    _VirtualDiskState_Type()
)
virtualDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskState.setStatus("current")
_VirtualDiskSizeInMB_Type = Integer32
_VirtualDiskSizeInMB_Object = MibTableColumn
virtualDiskSizeInMB = _VirtualDiskSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 6),
    _VirtualDiskSizeInMB_Type()
)
virtualDiskSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskSizeInMB.setStatus("current")


class _VirtualDiskWritePolicy_Type(Integer32):
    """Custom type virtualDiskWritePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("writeBack", 2),
          ("writeBackForce", 3),
          ("writeThrough", 1))
    )


_VirtualDiskWritePolicy_Type.__name__ = "Integer32"
_VirtualDiskWritePolicy_Object = MibTableColumn
virtualDiskWritePolicy = _VirtualDiskWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 10),
    _VirtualDiskWritePolicy_Type()
)
virtualDiskWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskWritePolicy.setStatus("current")


class _VirtualDiskReadPolicy_Type(Integer32):
    """Custom type virtualDiskReadPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveReadAhead", 3),
          ("noReadAhead", 1),
          ("readAhead", 2))
    )


_VirtualDiskReadPolicy_Type.__name__ = "Integer32"
_VirtualDiskReadPolicy_Object = MibTableColumn
virtualDiskReadPolicy = _VirtualDiskReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 11),
    _VirtualDiskReadPolicy_Type()
)
virtualDiskReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskReadPolicy.setStatus("current")


class _VirtualDiskLayout_Type(Integer32):
    """Custom type virtualDiskLayout based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("concatRaid1", 9),
          ("concatRaid5", 10),
          ("other", 1),
          ("r0", 2),
          ("r1", 3),
          ("r10", 6),
          ("r5", 4),
          ("r50", 7),
          ("r6", 5),
          ("r60", 8))
    )


_VirtualDiskLayout_Type.__name__ = "Integer32"
_VirtualDiskLayout_Object = MibTableColumn
virtualDiskLayout = _VirtualDiskLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 13),
    _VirtualDiskLayout_Type()
)
virtualDiskLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskLayout.setStatus("current")


class _VirtualDiskStripeSize_Type(Integer32):
    """Custom type virtualDiskStripeSize based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("eightKilobytes", 7),
          ("eightMegabytes", 17),
          ("fiveHundredAndTwelvebytes", 3),
          ("fiveOneTwoKilobytes", 13),
          ("fourKilobytes", 6),
          ("fourMegabytes", 16),
          ("oneKilobytes", 4),
          ("oneMegabye", 14),
          ("oneTwentyEightKilobytes", 11),
          ("other", 1),
          ("sixteenKilobytes", 8),
          ("sixteenMegabytes", 18),
          ("sixtyFourKilobytes", 10),
          ("thirtyTwoKilobytes", 9),
          ("twoFiftySixKilobytes", 12),
          ("twoKilobytes", 5),
          ("twoMegabytes", 15))
    )


_VirtualDiskStripeSize_Type.__name__ = "Integer32"
_VirtualDiskStripeSize_Object = MibTableColumn
virtualDiskStripeSize = _VirtualDiskStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 14),
    _VirtualDiskStripeSize_Type()
)
virtualDiskStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskStripeSize.setStatus("current")
_VirtualDiskComponentStatus_Type = ObjectStatusEnum
_VirtualDiskComponentStatus_Object = MibTableColumn
virtualDiskComponentStatus = _VirtualDiskComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 20),
    _VirtualDiskComponentStatus_Type()
)
virtualDiskComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskComponentStatus.setStatus("current")
_VirtualDiskBadBlocksDetected_Type = BooleanType
_VirtualDiskBadBlocksDetected_Object = MibTableColumn
virtualDiskBadBlocksDetected = _VirtualDiskBadBlocksDetected_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 23),
    _VirtualDiskBadBlocksDetected_Type()
)
virtualDiskBadBlocksDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskBadBlocksDetected.setStatus("current")
_VirtualDiskSecured_Type = BooleanType
_VirtualDiskSecured_Object = MibTableColumn
virtualDiskSecured = _VirtualDiskSecured_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 24),
    _VirtualDiskSecured_Type()
)
virtualDiskSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskSecured.setStatus("current")
_VirtualDiskIsCacheCade_Type = BooleanType
_VirtualDiskIsCacheCade_Object = MibTableColumn
virtualDiskIsCacheCade = _VirtualDiskIsCacheCade_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 25),
    _VirtualDiskIsCacheCade_Type()
)
virtualDiskIsCacheCade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskIsCacheCade.setStatus("current")


class _VirtualDiskDiskCachePolicy_Type(Integer32):
    """Custom type virtualDiskDiskCachePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defullt", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_VirtualDiskDiskCachePolicy_Type.__name__ = "Integer32"
_VirtualDiskDiskCachePolicy_Object = MibTableColumn
virtualDiskDiskCachePolicy = _VirtualDiskDiskCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 26),
    _VirtualDiskDiskCachePolicy_Type()
)
virtualDiskDiskCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskDiskCachePolicy.setStatus("current")


class _VirtualDiskOperationalState_Type(Integer32):
    """Custom type virtualDiskOperationalState based on Integer32"""
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
        *(("backgroundInit", 5),
          ("initializing", 4),
          ("notApplicable", 1),
          ("reconstructing", 2),
          ("resynching", 3))
    )


_VirtualDiskOperationalState_Type.__name__ = "Integer32"
_VirtualDiskOperationalState_Object = MibTableColumn
virtualDiskOperationalState = _VirtualDiskOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 30),
    _VirtualDiskOperationalState_Type()
)
virtualDiskOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskOperationalState.setStatus("current")


class _VirtualDiskProgress_Type(Integer32):
    """Custom type virtualDiskProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VirtualDiskProgress_Type.__name__ = "Integer32"
_VirtualDiskProgress_Object = MibTableColumn
virtualDiskProgress = _VirtualDiskProgress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 31),
    _VirtualDiskProgress_Type()
)
virtualDiskProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskProgress.setStatus("current")
_VirtualDiskAvailableProtocols_Type = DisplayString
_VirtualDiskAvailableProtocols_Object = MibTableColumn
virtualDiskAvailableProtocols = _VirtualDiskAvailableProtocols_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 32),
    _VirtualDiskAvailableProtocols_Type()
)
virtualDiskAvailableProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskAvailableProtocols.setStatus("current")
_VirtualDiskMediaType_Type = DisplayString
_VirtualDiskMediaType_Object = MibTableColumn
virtualDiskMediaType = _VirtualDiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 33),
    _VirtualDiskMediaType_Type()
)
virtualDiskMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskMediaType.setStatus("current")


class _VirtualDiskRemainingRedundancy_Type(Integer32):
    """Custom type virtualDiskRemainingRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VirtualDiskRemainingRedundancy_Type.__name__ = "Integer32"
_VirtualDiskRemainingRedundancy_Object = MibTableColumn
virtualDiskRemainingRedundancy = _VirtualDiskRemainingRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 34),
    _VirtualDiskRemainingRedundancy_Type()
)
virtualDiskRemainingRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskRemainingRedundancy.setStatus("current")
_VirtualDiskFQDD_Type = FQDDString
_VirtualDiskFQDD_Object = MibTableColumn
virtualDiskFQDD = _VirtualDiskFQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 35),
    _VirtualDiskFQDD_Type()
)
virtualDiskFQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskFQDD.setStatus("current")
_VirtualDiskDisplayName_Type = DisplayString
_VirtualDiskDisplayName_Object = MibTableColumn
virtualDiskDisplayName = _VirtualDiskDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 36),
    _VirtualDiskDisplayName_Type()
)
virtualDiskDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskDisplayName.setStatus("current")


class _VirtualDiskT10PIStatus_Type(Integer32):
    """Custom type virtualDiskT10PIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_VirtualDiskT10PIStatus_Type.__name__ = "Integer32"
_VirtualDiskT10PIStatus_Object = MibTableColumn
virtualDiskT10PIStatus = _VirtualDiskT10PIStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 37),
    _VirtualDiskT10PIStatus_Type()
)
virtualDiskT10PIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskT10PIStatus.setStatus("current")
_VirtualDiskBlockSizeInBytes_Type = Integer32
_VirtualDiskBlockSizeInBytes_Object = MibTableColumn
virtualDiskBlockSizeInBytes = _VirtualDiskBlockSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 5, 1, 20, 140, 1, 1, 38),
    _VirtualDiskBlockSizeInBytes_Type()
)
virtualDiskBlockSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskBlockSizeInBytes.setStatus("current")

# Managed Objects groups


# Notification objects

alertNetworkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2089)
)
alertNetworkFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertNetworkFailure.setStatus(
        "current"
    )

alertNetworkWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2090)
)
alertNetworkWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertNetworkWarning.setStatus(
        "current"
    )

alertNetworkInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2091)
)
alertNetworkInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertNetworkInformation.setStatus(
        "current"
    )

alertFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2153)
)
alertFanFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertFanFailure.setStatus(
        "current"
    )

alertFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2154)
)
alertFanWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertFanWarning.setStatus(
        "current"
    )

alertFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2155)
)
alertFanInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertFanInformation.setStatus(
        "current"
    )

alertTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2161)
)
alertTemperatureProbeFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeFailure.setStatus(
        "current"
    )

alertTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2162)
)
alertTemperatureProbeWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeWarning.setStatus(
        "current"
    )

alertTemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2163)
)
alertTemperatureProbeNormal.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNormal.setStatus(
        "current"
    )

alertVoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2169)
)
alertVoltageProbeFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeFailure.setStatus(
        "current"
    )

alertVoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2170)
)
alertVoltageProbeWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeWarning.setStatus(
        "current"
    )

alertVoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2171)
)
alertVoltageProbeNormal.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeNormal.setStatus(
        "current"
    )

alertAmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2177)
)
alertAmperageProbeFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeFailure.setStatus(
        "current"
    )

alertAmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2178)
)
alertAmperageProbeWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeWarning.setStatus(
        "current"
    )

alertAmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2179)
)
alertAmperageProbeNormal.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeNormal.setStatus(
        "current"
    )

alertPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2185)
)
alertPowerSupplyFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyFailure.setStatus(
        "current"
    )

alertPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2186)
)
alertPowerSupplyWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyWarning.setStatus(
        "current"
    )

alertPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2187)
)
alertPowerSupplyNormal.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyNormal.setStatus(
        "current"
    )

alertIntegratedDualSDModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2209)
)
alertIntegratedDualSDModuleFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleFailure.setStatus(
        "current"
    )

alertIntegratedDualSDModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2210)
)
alertIntegratedDualSDModuleWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleWarning.setStatus(
        "current"
    )

alertIntegratedDualSDModuleInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2211)
)
alertIntegratedDualSDModuleInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleInformation.setStatus(
        "current"
    )

alertBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2225)
)
alertBatteryFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertBatteryFailure.setStatus(
        "current"
    )

alertBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2226)
)
alertBatteryWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertBatteryWarning.setStatus(
        "current"
    )

alertBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2227)
)
alertBatteryNormal.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertBatteryNormal.setStatus(
        "current"
    )

alertAutomaticSystemRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2233)
)
alertAutomaticSystemRecovery.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertAutomaticSystemRecovery.setStatus(
        "current"
    )

alertProcessorDeviceStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2241)
)
alertProcessorDeviceStatusFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceStatusFailure.setStatus(
        "current"
    )

alertProcessorDeviceStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2242)
)
alertProcessorDeviceStatusWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceStatusWarning.setStatus(
        "current"
    )

alertProcessorDeviceStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2243)
)
alertProcessorDeviceStatusNormal.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceStatusNormal.setStatus(
        "current"
    )

alertLinkStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2249)
)
alertLinkStatusFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertLinkStatusFailure.setStatus(
        "current"
    )

alertLinkStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2250)
)
alertLinkStatusWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertLinkStatusWarning.setStatus(
        "current"
    )

alertLinkStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2251)
)
alertLinkStatusInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertLinkStatusInformation.setStatus(
        "current"
    )

alertMemoryDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2265)
)
alertMemoryDeviceFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceFailure.setStatus(
        "current"
    )

alertMemoryDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2266)
)
alertMemoryDeviceWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceWarning.setStatus(
        "current"
    )

alertMemoryDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2267)
)
alertMemoryDeviceInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceInformation.setStatus(
        "current"
    )

alertPowerUsageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2273)
)
alertPowerUsageFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerUsageFailure.setStatus(
        "current"
    )

alertPowerUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2274)
)
alertPowerUsageWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerUsageWarning.setStatus(
        "current"
    )

alertPowerUsageInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2275)
)
alertPowerUsageInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerUsageInformation.setStatus(
        "current"
    )

alertPhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2297)
)
alertPhysicalDiskFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPhysicalDiskFailure.setStatus(
        "current"
    )

alertPhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2298)
)
alertPhysicalDiskWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPhysicalDiskWarning.setStatus(
        "current"
    )

alertPhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2299)
)
alertPhysicalDiskInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPhysicalDiskInformation.setStatus(
        "current"
    )

alertHardwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2329)
)
alertHardwareConfigurationFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertHardwareConfigurationFailure.setStatus(
        "current"
    )

alertHardwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2330)
)
alertHardwareConfigurationWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertHardwareConfigurationWarning.setStatus(
        "current"
    )

alertHardwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2331)
)
alertHardwareConfigurationInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertHardwareConfigurationInformation.setStatus(
        "current"
    )

alertSoftwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2337)
)
alertSoftwareConfigurationFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSoftwareConfigurationFailure.setStatus(
        "current"
    )

alertSoftwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2338)
)
alertSoftwareConfigurationWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSoftwareConfigurationWarning.setStatus(
        "current"
    )

alertSoftwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2339)
)
alertSoftwareConfigurationInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSoftwareConfigurationInformation.setStatus(
        "current"
    )

alertSystemEventLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2377)
)
alertSystemEventLogFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSystemEventLogFailure.setStatus(
        "current"
    )

alertSystemEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2378)
)
alertSystemEventLogWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSystemEventLogWarning.setStatus(
        "current"
    )

alertSystemEventLogInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2379)
)
alertSystemEventLogInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSystemEventLogInformation.setStatus(
        "current"
    )

alertSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2385)
)
alertSecurityFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSecurityFailure.setStatus(
        "current"
    )

alertSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2386)
)
alertSecurityWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSecurityWarning.setStatus(
        "current"
    )

alertSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2387)
)
alertSecurityInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSecurityInformation.setStatus(
        "current"
    )

alertCableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2393)
)
alertCableFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertCableFailure.setStatus(
        "current"
    )

alertOSFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2409)
)
alertOSFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertOSFailure.setStatus(
        "current"
    )

alertOSInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2411)
)
alertOSInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertOSInformation.setStatus(
        "current"
    )

alertPCIDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2417)
)
alertPCIDeviceFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPCIDeviceFailure.setStatus(
        "current"
    )

alertPCIDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2418)
)
alertPCIDeviceWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPCIDeviceWarning.setStatus(
        "current"
    )

alertPCIDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2419)
)
alertPCIDeviceInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPCIDeviceInformation.setStatus(
        "current"
    )

alertBiosPostFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2425)
)
alertBiosPostFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertBiosPostFailure.setStatus(
        "current"
    )

alertProcessorDeviceAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2457)
)
alertProcessorDeviceAbsent.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertProcessorDeviceAbsent.setStatus(
        "current"
    )

alertPowerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2465)
)
alertPowerSupplyAbsent.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyAbsent.setStatus(
        "current"
    )

alertRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2473)
)
alertRedundancyLost.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertRedundancyLost.setStatus(
        "current"
    )

alertRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2474)
)
alertRedundancyDegraded.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertRedundancyDegraded.setStatus(
        "current"
    )

alertRedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2475)
)
alertRedundancyInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertRedundancyInformation.setStatus(
        "current"
    )

alertIntegratedDualSDModuleAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2481)
)
alertIntegratedDualSDModuleAbsent.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleAbsent.setStatus(
        "current"
    )

alertIntegratedDualSDModuleRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2489)
)
alertIntegratedDualSDModuleRedundancyLost.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleRedundancyLost.setStatus(
        "current"
    )

alertIntegratedDualSDModuleRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2490)
)
alertIntegratedDualSDModuleRedundancyDegraded.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleRedundancyDegraded.setStatus(
        "current"
    )

alertIntegratedDualSDModuleRedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2491)
)
alertIntegratedDualSDModuleRedundancyInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIntegratedDualSDModuleRedundancyInformation.setStatus(
        "current"
    )

alertvFlashMediaDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2505)
)
alertvFlashMediaDeviceFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertvFlashMediaDeviceFailure.setStatus(
        "current"
    )

alertvFlashMediaDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2506)
)
alertvFlashMediaDeviceWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertvFlashMediaDeviceWarning.setStatus(
        "current"
    )

alertvFlashMediaDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2507)
)
alertvFlashMediaDeviceInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertvFlashMediaDeviceInformation.setStatus(
        "current"
    )

alertvFlashMediaDeviceAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2515)
)
alertvFlashMediaDeviceAbsent.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertvFlashMediaDeviceAbsent.setStatus(
        "current"
    )

alertTemperatureStatisticsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2521)
)
alertTemperatureStatisticsFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertTemperatureStatisticsFailure.setStatus(
        "current"
    )

alertTemperatureStatisticsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2522)
)
alertTemperatureStatisticsWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertTemperatureStatisticsWarning.setStatus(
        "current"
    )

alertRACInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2531)
)
alertRACInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertRACInformation.setStatus(
        "current"
    )

alertFiberChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2537)
)
alertFiberChannelFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertFiberChannelFailure.setStatus(
        "current"
    )

alertFiberChannelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2538)
)
alertFiberChannelWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertFiberChannelWarning.setStatus(
        "current"
    )

alertFiberChannelInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2539)
)
alertFiberChannelInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertFiberChannelInformation.setStatus(
        "current"
    )

alertCMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2545)
)
alertCMCFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertCMCFailure.setStatus(
        "current"
    )

alertCMCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2546)
)
alertCMCWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertCMCWarning.setStatus(
        "current"
    )

alertIOVirtualizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2553)
)
alertIOVirtualizationFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIOVirtualizationFailure.setStatus(
        "current"
    )

alertSystemPerformanceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 1, 0, 2650)
)
alertSystemPerformanceWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSystemPerformanceWarning.setStatus(
        "current"
    )

alertStorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4177)
)
alertStorageManagementFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageManagementFailure.setStatus(
        "current"
    )

alertStorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4178)
)
alertStorageManagementWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageManagementWarning.setStatus(
        "current"
    )

alertStorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4179)
)
alertStorageManagementInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageManagementInformation.setStatus(
        "current"
    )

alertStorageFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4201)
)
alertStorageFanFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageFanFailure.setStatus(
        "current"
    )

alertStorageFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4202)
)
alertStorageFanWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageFanWarning.setStatus(
        "current"
    )

alertStorageFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4203)
)
alertStorageFanInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageFanInformation.setStatus(
        "current"
    )

alertStorageTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4209)
)
alertStorageTemperatureProbeFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageTemperatureProbeFailure.setStatus(
        "current"
    )

alertStorageTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4210)
)
alertStorageTemperatureProbeWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageTemperatureProbeWarning.setStatus(
        "current"
    )

alertStorageTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4211)
)
alertStorageTemperatureProbeInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageTemperatureProbeInformation.setStatus(
        "current"
    )

alertStoragePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4233)
)
alertStoragePowerSupplyFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStoragePowerSupplyFailure.setStatus(
        "current"
    )

alertStoragePowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4234)
)
alertStoragePowerSupplyWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStoragePowerSupplyWarning.setStatus(
        "current"
    )

alertStoragePowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4235)
)
alertStoragePowerSupplyInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStoragePowerSupplyInformation.setStatus(
        "current"
    )

alertStorageBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4273)
)
alertStorageBatteryFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageBatteryFailure.setStatus(
        "current"
    )

alertStorageBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4274)
)
alertStorageBatteryWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageBatteryWarning.setStatus(
        "current"
    )

alertStorageBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4275)
)
alertStorageBatteryInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageBatteryInformation.setStatus(
        "current"
    )

alertStorageControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4329)
)
alertStorageControllerFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageControllerFailure.setStatus(
        "current"
    )

alertStorageControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4330)
)
alertStorageControllerWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageControllerWarning.setStatus(
        "current"
    )

alertStorageControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4331)
)
alertStorageControllerInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageControllerInformation.setStatus(
        "current"
    )

alertStorageEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4337)
)
alertStorageEnclosureFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageEnclosureFailure.setStatus(
        "current"
    )

alertStorageEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4338)
)
alertStorageEnclosureWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageEnclosureWarning.setStatus(
        "current"
    )

alertStorageEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4339)
)
alertStorageEnclosureInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageEnclosureInformation.setStatus(
        "current"
    )

alertStoragePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4345)
)
alertStoragePhysicalDiskFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStoragePhysicalDiskFailure.setStatus(
        "current"
    )

alertStoragePhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4346)
)
alertStoragePhysicalDiskWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStoragePhysicalDiskWarning.setStatus(
        "current"
    )

alertStoragePhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4347)
)
alertStoragePhysicalDiskInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStoragePhysicalDiskInformation.setStatus(
        "current"
    )

alertStorageVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4353)
)
alertStorageVirtualDiskFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageVirtualDiskFailure.setStatus(
        "current"
    )

alertStorageVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4354)
)
alertStorageVirtualDiskWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageVirtualDiskWarning.setStatus(
        "current"
    )

alertStorageVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4355)
)
alertStorageVirtualDiskInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageVirtualDiskInformation.setStatus(
        "current"
    )

alertStorageSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4433)
)
alertStorageSecurityFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageSecurityFailure.setStatus(
        "current"
    )

alertStorageSecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4434)
)
alertStorageSecurityWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageSecurityWarning.setStatus(
        "current"
    )

alertStorageSecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 2, 0, 4435)
)
alertStorageSecurityInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertStorageSecurityInformation.setStatus(
        "current"
    )

alertUpdateJobInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 3, 0, 6211)
)
alertUpdateJobInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertUpdateJobInformation.setStatus(
        "current"
    )

alertSoftwareChangeUpdateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 3, 0, 6314)
)
alertSoftwareChangeUpdateWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSoftwareChangeUpdateWarning.setStatus(
        "current"
    )

alertPowerSupplyAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8329)
)
alertPowerSupplyAuditFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyAuditFailure.setStatus(
        "current"
    )

alertPowerSupplyAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8330)
)
alertPowerSupplyAuditWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyAuditWarning.setStatus(
        "current"
    )

alertPowerUsageAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8417)
)
alertPowerUsageAuditFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerUsageAuditFailure.setStatus(
        "current"
    )

alertPowerUsageAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8418)
)
alertPowerUsageAuditWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerUsageAuditWarning.setStatus(
        "current"
    )

alertPowerUsageAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8419)
)
alertPowerUsageAuditInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPowerUsageAuditInformation.setStatus(
        "current"
    )

alertUserTrackingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8490)
)
alertUserTrackingWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertUserTrackingWarning.setStatus(
        "current"
    )

alertiDRACIPAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8499)
)
alertiDRACIPAddressChange.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertiDRACIPAddressChange.setStatus(
        "current"
    )

alertLicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8513)
)
alertLicenseFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertLicenseFailure.setStatus(
        "current"
    )

alertLicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8514)
)
alertLicenseWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertLicenseWarning.setStatus(
        "current"
    )

alertLicenseInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8515)
)
alertLicenseInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertLicenseInformation.setStatus(
        "current"
    )

alertPCIDeviceAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8562)
)
alertPCIDeviceAuditWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPCIDeviceAuditWarning.setStatus(
        "current"
    )

alertSystemPowerStateChangeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8579)
)
alertSystemPowerStateChangeInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSystemPowerStateChangeInformation.setStatus(
        "current"
    )

alertDebugWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8594)
)
alertDebugWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertDebugWarning.setStatus(
        "current"
    )

alertDebugInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8595)
)
alertDebugInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertDebugInformation.setStatus(
        "current"
    )

alertCMCAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8689)
)
alertCMCAuditFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertCMCAuditFailure.setStatus(
        "current"
    )

alertCMCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8690)
)
alertCMCAuditWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertCMCAuditWarning.setStatus(
        "current"
    )

alertCMCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 4, 0, 8691)
)
alertCMCAuditInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertCMCAuditInformation.setStatus(
        "current"
    )

alertJobControlConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10267)
)
alertJobControlConfigurationInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertJobControlConfigurationInformation.setStatus(
        "current"
    )

alertTestTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10395)
)
alertTestTrapEvent.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertTestTrapEvent.setStatus(
        "current"
    )

alertSWCConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10529)
)
alertSWCConfigurationFailure.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSWCConfigurationFailure.setStatus(
        "current"
    )

alertSWCConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10530)
)
alertSWCConfigurationWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSWCConfigurationWarning.setStatus(
        "current"
    )

alertIPAddressConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10547)
)
alertIPAddressConfigurationInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertIPAddressConfigurationInformation.setStatus(
        "current"
    )

alertSecurityConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10578)
)
alertSecurityConfigurationWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertSecurityConfigurationWarning.setStatus(
        "current"
    )

alertPCIDeviceConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10611)
)
alertPCIDeviceConfigurationInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertPCIDeviceConfigurationInformation.setStatus(
        "current"
    )

alertAutoDiscoveryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10635)
)
alertAutoDiscoveryInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertAutoDiscoveryInformation.setStatus(
        "current"
    )

alertNetworkConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10770)
)
alertNetworkConfigurationWarning.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertNetworkConfigurationWarning.setStatus(
        "current"
    )

alertNetworkConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 5, 3, 2, 5, 0, 10771)
)
alertNetworkConfigurationInformation.setObjects(
      *(("IDRAC-MIB-SMIv2", "alertMessageID"),
        ("IDRAC-MIB-SMIv2", "alertMessage"),
        ("IDRAC-MIB-SMIv2", "alertCurrentStatus"),
        ("IDRAC-MIB-SMIv2", "alertSystemServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertSystemFQDN"),
        ("IDRAC-MIB-SMIv2", "alertFQDD"),
        ("IDRAC-MIB-SMIv2", "alertDeviceDisplayName"),
        ("IDRAC-MIB-SMIv2", "alertMessageArguments"),
        ("IDRAC-MIB-SMIv2", "alertChassisServiceTag"),
        ("IDRAC-MIB-SMIv2", "alertChassisName"),
        ("IDRAC-MIB-SMIv2", "alertRacFQDN"))
)
if mibBuilder.loadTexts:
    alertNetworkConfigurationInformation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IDRAC-MIB-SMIv2",
    **{"StringType": StringType,
       "String64": String64,
       "FQDDString": FQDDString,
       "MACAddress": MACAddress,
       "ObjectRange": ObjectRange,
       "Unsigned8BitRange": Unsigned8BitRange,
       "Unsigned16BitRange": Unsigned16BitRange,
       "Unsigned32BitRange": Unsigned32BitRange,
       "Signed32BitRange": Signed32BitRange,
       "BooleanType": BooleanType,
       "DateName": DateName,
       "StateCapabilitiesFlags": StateCapabilitiesFlags,
       "StateSettingsFlags": StateSettingsFlags,
       "ProbeCapabilitiesFlags": ProbeCapabilitiesFlags,
       "StatusProbeEnum": StatusProbeEnum,
       "StatusRedundancyEnum": StatusRedundancyEnum,
       "ObjectStatusEnum": ObjectStatusEnum,
       "RacTypeEnum": RacTypeEnum,
       "SystemFormFactorEnum": SystemFormFactorEnum,
       "BladeGeometryEnum": BladeGeometryEnum,
       "PowerStateStatusEnum": PowerStateStatusEnum,
       "StateCapabilitiesLogUniqueFlags": StateCapabilitiesLogUniqueFlags,
       "StateSettingsLogUniqueFlags": StateSettingsLogUniqueFlags,
       "LogFormatType": LogFormatType,
       "ChassisTypeEnum": ChassisTypeEnum,
       "ChassisSystemClassEnum": ChassisSystemClassEnum,
       "LEDControlCapabilitiesFlags": LEDControlCapabilitiesFlags,
       "LEDControlSettingsFlags": LEDControlSettingsFlags,
       "ChassisIdentifyControlCapabilitiesFlags": ChassisIdentifyControlCapabilitiesFlags,
       "ChassisIdentifyControlSettingsFlags": ChassisIdentifyControlSettingsFlags,
       "HostControlCapabilitiesFlags": HostControlCapabilitiesFlags,
       "HostControlSettingsFlags": HostControlSettingsFlags,
       "WatchDogControlCapabilitiesFlags": WatchDogControlCapabilitiesFlags,
       "WatchControlSettingsFlags": WatchControlSettingsFlags,
       "WatchDogTimerCapabilitiesFlags": WatchDogTimerCapabilitiesFlags,
       "PowerButtonControlCapabilitiesFlags": PowerButtonControlCapabilitiesFlags,
       "PowerButtonControlSettingsFlags": PowerButtonControlSettingsFlags,
       "NMIButtonControlCapabilitiesFlags": NMIButtonControlCapabilitiesFlags,
       "NMIButtonControlSettingsFlags": NMIButtonControlSettingsFlags,
       "SystemPropertiesFlags": SystemPropertiesFlags,
       "FirmwareType": FirmwareType,
       "IntrusionReadingEnum": IntrusionReadingEnum,
       "IntrusionTypeEnum": IntrusionTypeEnum,
       "LcLogCategoryEnum": LcLogCategoryEnum,
       "PowerSupplyStateCapabilitiesUniqueFlags": PowerSupplyStateCapabilitiesUniqueFlags,
       "PowerSupplyStateSettingsUniqueFlags": PowerSupplyStateSettingsUniqueFlags,
       "PowerSupplyTypeEnum": PowerSupplyTypeEnum,
       "PowerSupplySensorStateFlags": PowerSupplySensorStateFlags,
       "PowerSupplyConfigurationErrorTypeEnum": PowerSupplyConfigurationErrorTypeEnum,
       "VoltageTypeEnum": VoltageTypeEnum,
       "VoltageDiscreteReadingEnum": VoltageDiscreteReadingEnum,
       "AmperageProbeTypeEnum": AmperageProbeTypeEnum,
       "AmperageDiscreteReadingEnum": AmperageDiscreteReadingEnum,
       "SystemBatteryReadingFlags": SystemBatteryReadingFlags,
       "PowerCapCapabilitiesFlags": PowerCapCapabilitiesFlags,
       "PowerCapSettingEnum": PowerCapSettingEnum,
       "CoolingDeviceTypeEnum": CoolingDeviceTypeEnum,
       "CoolingDeviceSubTypeEnum": CoolingDeviceSubTypeEnum,
       "CoolingDeviceDiscreteReadingEnum": CoolingDeviceDiscreteReadingEnum,
       "TemperatureProbeTypeEnum": TemperatureProbeTypeEnum,
       "TemperatureDiscreteReadingEnum": TemperatureDiscreteReadingEnum,
       "ProcessorDeviceType": ProcessorDeviceType,
       "ProcessorDeviceFamily": ProcessorDeviceFamily,
       "ProcessorDeviceStatusState": ProcessorDeviceStatusState,
       "ProcessorDeviceStatusReadingFlags": ProcessorDeviceStatusReadingFlags,
       "MemoryDeviceTypeEnum": MemoryDeviceTypeEnum,
       "NetworkDeviceConnectionStatusEnum": NetworkDeviceConnectionStatusEnum,
       "NetworkDeviceTOECapabilityFlags": NetworkDeviceTOECapabilityFlags,
       "NetworkDeviceiSCSICapabilityFlags": NetworkDeviceiSCSICapabilityFlags,
       "NetworkDeviceCapabilitiesFlags": NetworkDeviceCapabilitiesFlags,
       "SystemSlotStateCapabilitiesFlags": SystemSlotStateCapabilitiesFlags,
       "SystemSlotStateSettingsFlags": SystemSlotStateSettingsFlags,
       "SystemSlotTypeEnum": SystemSlotTypeEnum,
       "SystemSlotUsageEnum": SystemSlotUsageEnum,
       "SystemSlotCategoryEnum": SystemSlotCategoryEnum,
       "outOfBandGroup": outOfBandGroup,
       "informationGroup": informationGroup,
       "racInfoGroup": racInfoGroup,
       "racName": racName,
       "racShortName": racShortName,
       "racDescription": racDescription,
       "racManufacturer": racManufacturer,
       "racVersion": racVersion,
       "racURL": racURL,
       "racType": racType,
       "racFirmwareVersion": racFirmwareVersion,
       "chassisInfoGroup": chassisInfoGroup,
       "chassisServiceTag": chassisServiceTag,
       "chassisNameModular": chassisNameModular,
       "chassisModelModular": chassisModelModular,
       "systemInfoGroup": systemInfoGroup,
       "systemFQDN": systemFQDN,
       "systemServiceTag": systemServiceTag,
       "systemExpressServiceCode": systemExpressServiceCode,
       "systemAssetTag": systemAssetTag,
       "systemBladeSlotNumber": systemBladeSlotNumber,
       "systemOSName": systemOSName,
       "systemFormFactor": systemFormFactor,
       "systemDataCenterName": systemDataCenterName,
       "systemAisleName": systemAisleName,
       "systemRackName": systemRackName,
       "systemRackSlot": systemRackSlot,
       "systemModelName": systemModelName,
       "systemSystemID": systemSystemID,
       "systemOSVersion": systemOSVersion,
       "systemRoomName": systemRoomName,
       "systemChassisSystemHeight": systemChassisSystemHeight,
       "systemBladeGeometry": systemBladeGeometry,
       "systemNodeID": systemNodeID,
       "statusGroup": statusGroup,
       "globalSystemStatus": globalSystemStatus,
       "systemLCDStatus": systemLCDStatus,
       "globalStorageStatus": globalStorageStatus,
       "systemPowerState": systemPowerState,
       "systemPowerUpTime": systemPowerUpTime,
       "alertGroup": alertGroup,
       "alertVariablesGroup": alertVariablesGroup,
       "alertMessageID": alertMessageID,
       "alertMessage": alertMessage,
       "alertCurrentStatus": alertCurrentStatus,
       "alertSystemServiceTag": alertSystemServiceTag,
       "alertSystemFQDN": alertSystemFQDN,
       "alertFQDD": alertFQDD,
       "alertDeviceDisplayName": alertDeviceDisplayName,
       "alertMessageArguments": alertMessageArguments,
       "alertChassisServiceTag": alertChassisServiceTag,
       "alertChassisName": alertChassisName,
       "alertRacFQDN": alertRacFQDN,
       "alertTrapGroup": alertTrapGroup,
       "systemAlertTrapGroup": systemAlertTrapGroup,
       "alertNetworkFailure": alertNetworkFailure,
       "alertNetworkWarning": alertNetworkWarning,
       "alertNetworkInformation": alertNetworkInformation,
       "alertFanFailure": alertFanFailure,
       "alertFanWarning": alertFanWarning,
       "alertFanInformation": alertFanInformation,
       "alertTemperatureProbeFailure": alertTemperatureProbeFailure,
       "alertTemperatureProbeWarning": alertTemperatureProbeWarning,
       "alertTemperatureProbeNormal": alertTemperatureProbeNormal,
       "alertVoltageProbeFailure": alertVoltageProbeFailure,
       "alertVoltageProbeWarning": alertVoltageProbeWarning,
       "alertVoltageProbeNormal": alertVoltageProbeNormal,
       "alertAmperageProbeFailure": alertAmperageProbeFailure,
       "alertAmperageProbeWarning": alertAmperageProbeWarning,
       "alertAmperageProbeNormal": alertAmperageProbeNormal,
       "alertPowerSupplyFailure": alertPowerSupplyFailure,
       "alertPowerSupplyWarning": alertPowerSupplyWarning,
       "alertPowerSupplyNormal": alertPowerSupplyNormal,
       "alertIntegratedDualSDModuleFailure": alertIntegratedDualSDModuleFailure,
       "alertIntegratedDualSDModuleWarning": alertIntegratedDualSDModuleWarning,
       "alertIntegratedDualSDModuleInformation": alertIntegratedDualSDModuleInformation,
       "alertBatteryFailure": alertBatteryFailure,
       "alertBatteryWarning": alertBatteryWarning,
       "alertBatteryNormal": alertBatteryNormal,
       "alertAutomaticSystemRecovery": alertAutomaticSystemRecovery,
       "alertProcessorDeviceStatusFailure": alertProcessorDeviceStatusFailure,
       "alertProcessorDeviceStatusWarning": alertProcessorDeviceStatusWarning,
       "alertProcessorDeviceStatusNormal": alertProcessorDeviceStatusNormal,
       "alertLinkStatusFailure": alertLinkStatusFailure,
       "alertLinkStatusWarning": alertLinkStatusWarning,
       "alertLinkStatusInformation": alertLinkStatusInformation,
       "alertMemoryDeviceFailure": alertMemoryDeviceFailure,
       "alertMemoryDeviceWarning": alertMemoryDeviceWarning,
       "alertMemoryDeviceInformation": alertMemoryDeviceInformation,
       "alertPowerUsageFailure": alertPowerUsageFailure,
       "alertPowerUsageWarning": alertPowerUsageWarning,
       "alertPowerUsageInformation": alertPowerUsageInformation,
       "alertPhysicalDiskFailure": alertPhysicalDiskFailure,
       "alertPhysicalDiskWarning": alertPhysicalDiskWarning,
       "alertPhysicalDiskInformation": alertPhysicalDiskInformation,
       "alertHardwareConfigurationFailure": alertHardwareConfigurationFailure,
       "alertHardwareConfigurationWarning": alertHardwareConfigurationWarning,
       "alertHardwareConfigurationInformation": alertHardwareConfigurationInformation,
       "alertSoftwareConfigurationFailure": alertSoftwareConfigurationFailure,
       "alertSoftwareConfigurationWarning": alertSoftwareConfigurationWarning,
       "alertSoftwareConfigurationInformation": alertSoftwareConfigurationInformation,
       "alertSystemEventLogFailure": alertSystemEventLogFailure,
       "alertSystemEventLogWarning": alertSystemEventLogWarning,
       "alertSystemEventLogInformation": alertSystemEventLogInformation,
       "alertSecurityFailure": alertSecurityFailure,
       "alertSecurityWarning": alertSecurityWarning,
       "alertSecurityInformation": alertSecurityInformation,
       "alertCableFailure": alertCableFailure,
       "alertOSFailure": alertOSFailure,
       "alertOSInformation": alertOSInformation,
       "alertPCIDeviceFailure": alertPCIDeviceFailure,
       "alertPCIDeviceWarning": alertPCIDeviceWarning,
       "alertPCIDeviceInformation": alertPCIDeviceInformation,
       "alertBiosPostFailure": alertBiosPostFailure,
       "alertProcessorDeviceAbsent": alertProcessorDeviceAbsent,
       "alertPowerSupplyAbsent": alertPowerSupplyAbsent,
       "alertRedundancyLost": alertRedundancyLost,
       "alertRedundancyDegraded": alertRedundancyDegraded,
       "alertRedundancyInformation": alertRedundancyInformation,
       "alertIntegratedDualSDModuleAbsent": alertIntegratedDualSDModuleAbsent,
       "alertIntegratedDualSDModuleRedundancyLost": alertIntegratedDualSDModuleRedundancyLost,
       "alertIntegratedDualSDModuleRedundancyDegraded": alertIntegratedDualSDModuleRedundancyDegraded,
       "alertIntegratedDualSDModuleRedundancyInformation": alertIntegratedDualSDModuleRedundancyInformation,
       "alertvFlashMediaDeviceFailure": alertvFlashMediaDeviceFailure,
       "alertvFlashMediaDeviceWarning": alertvFlashMediaDeviceWarning,
       "alertvFlashMediaDeviceInformation": alertvFlashMediaDeviceInformation,
       "alertvFlashMediaDeviceAbsent": alertvFlashMediaDeviceAbsent,
       "alertTemperatureStatisticsFailure": alertTemperatureStatisticsFailure,
       "alertTemperatureStatisticsWarning": alertTemperatureStatisticsWarning,
       "alertRACInformation": alertRACInformation,
       "alertFiberChannelFailure": alertFiberChannelFailure,
       "alertFiberChannelWarning": alertFiberChannelWarning,
       "alertFiberChannelInformation": alertFiberChannelInformation,
       "alertCMCFailure": alertCMCFailure,
       "alertCMCWarning": alertCMCWarning,
       "alertIOVirtualizationFailure": alertIOVirtualizationFailure,
       "alertSystemPerformanceWarning": alertSystemPerformanceWarning,
       "storageAlertTrapGroup": storageAlertTrapGroup,
       "alertStorageManagementFailure": alertStorageManagementFailure,
       "alertStorageManagementWarning": alertStorageManagementWarning,
       "alertStorageManagementInformation": alertStorageManagementInformation,
       "alertStorageFanFailure": alertStorageFanFailure,
       "alertStorageFanWarning": alertStorageFanWarning,
       "alertStorageFanInformation": alertStorageFanInformation,
       "alertStorageTemperatureProbeFailure": alertStorageTemperatureProbeFailure,
       "alertStorageTemperatureProbeWarning": alertStorageTemperatureProbeWarning,
       "alertStorageTemperatureProbeInformation": alertStorageTemperatureProbeInformation,
       "alertStoragePowerSupplyFailure": alertStoragePowerSupplyFailure,
       "alertStoragePowerSupplyWarning": alertStoragePowerSupplyWarning,
       "alertStoragePowerSupplyInformation": alertStoragePowerSupplyInformation,
       "alertStorageBatteryFailure": alertStorageBatteryFailure,
       "alertStorageBatteryWarning": alertStorageBatteryWarning,
       "alertStorageBatteryInformation": alertStorageBatteryInformation,
       "alertStorageControllerFailure": alertStorageControllerFailure,
       "alertStorageControllerWarning": alertStorageControllerWarning,
       "alertStorageControllerInformation": alertStorageControllerInformation,
       "alertStorageEnclosureFailure": alertStorageEnclosureFailure,
       "alertStorageEnclosureWarning": alertStorageEnclosureWarning,
       "alertStorageEnclosureInformation": alertStorageEnclosureInformation,
       "alertStoragePhysicalDiskFailure": alertStoragePhysicalDiskFailure,
       "alertStoragePhysicalDiskWarning": alertStoragePhysicalDiskWarning,
       "alertStoragePhysicalDiskInformation": alertStoragePhysicalDiskInformation,
       "alertStorageVirtualDiskFailure": alertStorageVirtualDiskFailure,
       "alertStorageVirtualDiskWarning": alertStorageVirtualDiskWarning,
       "alertStorageVirtualDiskInformation": alertStorageVirtualDiskInformation,
       "alertStorageSecurityFailure": alertStorageSecurityFailure,
       "alertStorageSecurityWarning": alertStorageSecurityWarning,
       "alertStorageSecurityInformation": alertStorageSecurityInformation,
       "updatesAlertTrapGroup": updatesAlertTrapGroup,
       "alertUpdateJobInformation": alertUpdateJobInformation,
       "alertSoftwareChangeUpdateWarning": alertSoftwareChangeUpdateWarning,
       "auditAlertTrapGroup": auditAlertTrapGroup,
       "alertPowerSupplyAuditFailure": alertPowerSupplyAuditFailure,
       "alertPowerSupplyAuditWarning": alertPowerSupplyAuditWarning,
       "alertPowerUsageAuditFailure": alertPowerUsageAuditFailure,
       "alertPowerUsageAuditWarning": alertPowerUsageAuditWarning,
       "alertPowerUsageAuditInformation": alertPowerUsageAuditInformation,
       "alertUserTrackingWarning": alertUserTrackingWarning,
       "alertiDRACIPAddressChange": alertiDRACIPAddressChange,
       "alertLicenseFailure": alertLicenseFailure,
       "alertLicenseWarning": alertLicenseWarning,
       "alertLicenseInformation": alertLicenseInformation,
       "alertPCIDeviceAuditWarning": alertPCIDeviceAuditWarning,
       "alertSystemPowerStateChangeInformation": alertSystemPowerStateChangeInformation,
       "alertDebugWarning": alertDebugWarning,
       "alertDebugInformation": alertDebugInformation,
       "alertCMCAuditFailure": alertCMCAuditFailure,
       "alertCMCAuditWarning": alertCMCAuditWarning,
       "alertCMCAuditInformation": alertCMCAuditInformation,
       "configurationAlertTrapGroup": configurationAlertTrapGroup,
       "alertJobControlConfigurationInformation": alertJobControlConfigurationInformation,
       "alertTestTrapEvent": alertTestTrapEvent,
       "alertSWCConfigurationFailure": alertSWCConfigurationFailure,
       "alertSWCConfigurationWarning": alertSWCConfigurationWarning,
       "alertIPAddressConfigurationInformation": alertIPAddressConfigurationInformation,
       "alertSecurityConfigurationWarning": alertSecurityConfigurationWarning,
       "alertPCIDeviceConfigurationInformation": alertPCIDeviceConfigurationInformation,
       "alertAutoDiscoveryInformation": alertAutoDiscoveryInformation,
       "alertNetworkConfigurationWarning": alertNetworkConfigurationWarning,
       "alertNetworkConfigurationInformation": alertNetworkConfigurationInformation,
       "systemDetailsGroup": systemDetailsGroup,
       "mIBVersionGroup": mIBVersionGroup,
       "mIBMajorVersionNumber": mIBMajorVersionNumber,
       "mIBMinorVersionNumber": mIBMinorVersionNumber,
       "mIBMaintenanceVersionNumber": mIBMaintenanceVersionNumber,
       "systemStateGroup": systemStateGroup,
       "systemStateTable": systemStateTable,
       "systemStateTableEntry": systemStateTableEntry,
       "systemStatechassisIndex": systemStatechassisIndex,
       "systemStateGlobalSystemStatus": systemStateGlobalSystemStatus,
       "systemStateChassisState": systemStateChassisState,
       "systemStateChassisStatus": systemStateChassisStatus,
       "systemStatePowerUnitStateDetails": systemStatePowerUnitStateDetails,
       "systemStatePowerUnitStatusRedundancy": systemStatePowerUnitStatusRedundancy,
       "systemStatePowerUnitStatusDetails": systemStatePowerUnitStatusDetails,
       "systemStatePowerSupplyStateDetails": systemStatePowerSupplyStateDetails,
       "systemStatePowerSupplyStatusCombined": systemStatePowerSupplyStatusCombined,
       "systemStatePowerSupplyStatusDetails": systemStatePowerSupplyStatusDetails,
       "systemStateVoltageStateDetails": systemStateVoltageStateDetails,
       "systemStateVoltageStatusCombined": systemStateVoltageStatusCombined,
       "systemStateVoltageStatusDetails": systemStateVoltageStatusDetails,
       "systemStateAmperageStateDetails": systemStateAmperageStateDetails,
       "systemStateAmperageStatusCombined": systemStateAmperageStatusCombined,
       "systemStateAmperageStatusDetails": systemStateAmperageStatusDetails,
       "systemStateCoolingUnitStateDetails": systemStateCoolingUnitStateDetails,
       "systemStateCoolingUnitStatusRedundancy": systemStateCoolingUnitStatusRedundancy,
       "systemStateCoolingUnitStatusDetails": systemStateCoolingUnitStatusDetails,
       "systemStateCoolingDeviceStateDetails": systemStateCoolingDeviceStateDetails,
       "systemStateCoolingDeviceStatusCombined": systemStateCoolingDeviceStatusCombined,
       "systemStateCoolingDeviceStatusDetails": systemStateCoolingDeviceStatusDetails,
       "systemStateTemperatureStateDetails": systemStateTemperatureStateDetails,
       "systemStateTemperatureStatusCombined": systemStateTemperatureStatusCombined,
       "systemStateTemperatureStatusDetails": systemStateTemperatureStatusDetails,
       "systemStateMemoryDeviceStateDetails": systemStateMemoryDeviceStateDetails,
       "systemStateMemoryDeviceStatusCombined": systemStateMemoryDeviceStatusCombined,
       "systemStateMemoryDeviceStatusDetails": systemStateMemoryDeviceStatusDetails,
       "systemStateChassisIntrusionStateDetails": systemStateChassisIntrusionStateDetails,
       "systemStateChassisIntrusionStatusCombined": systemStateChassisIntrusionStatusCombined,
       "systemStateChassisIntrusionStatusDetails": systemStateChassisIntrusionStatusDetails,
       "systemStatePowerUnitStatusCombined": systemStatePowerUnitStatusCombined,
       "systemStatePowerUnitStatusList": systemStatePowerUnitStatusList,
       "systemStateCoolingUnitStatusCombined": systemStateCoolingUnitStatusCombined,
       "systemStateCoolingUnitStatusList": systemStateCoolingUnitStatusList,
       "systemStateProcessorDeviceStatusCombined": systemStateProcessorDeviceStatusCombined,
       "systemStateProcessorDeviceStatusList": systemStateProcessorDeviceStatusList,
       "systemStateBatteryStatusCombined": systemStateBatteryStatusCombined,
       "systemStateBatteryStatusList": systemStateBatteryStatusList,
       "systemStateSDCardUnitStatusCombined": systemStateSDCardUnitStatusCombined,
       "systemStateSDCardUnitStatusList": systemStateSDCardUnitStatusList,
       "systemStateSDCardDeviceStatusCombined": systemStateSDCardDeviceStatusCombined,
       "systemStateSDCardDeviceStatusList": systemStateSDCardDeviceStatusList,
       "systemStateIDSDMCardUnitStatusCombined": systemStateIDSDMCardUnitStatusCombined,
       "systemStateIDSDMCardUnitStatusList": systemStateIDSDMCardUnitStatusList,
       "systemStateIDSDMCardDeviceStatusCombined": systemStateIDSDMCardDeviceStatusCombined,
       "systemStateIDSDMCardDeviceStatusList": systemStateIDSDMCardDeviceStatusList,
       "systemStateTemperatureStatisticsStateDetails": systemStateTemperatureStatisticsStateDetails,
       "systemStateTemperatureStatisticsStatusCombined": systemStateTemperatureStatisticsStatusCombined,
       "systemStateTemperatureStatisticsStatusDetails": systemStateTemperatureStatisticsStatusDetails,
       "chassisInformationGroup": chassisInformationGroup,
       "numEventLogEntries": numEventLogEntries,
       "numLCLogEntries": numLCLogEntries,
       "chassisInformationTable": chassisInformationTable,
       "chassisInformationTableEntry": chassisInformationTableEntry,
       "chassisIndexChassisInformation": chassisIndexChassisInformation,
       "chassisStateCapabilities": chassisStateCapabilities,
       "chassisStateSettings": chassisStateSettings,
       "chassisStatus": chassisStatus,
       "chassisparentIndexReference": chassisparentIndexReference,
       "chassisType": chassisType,
       "chassisName": chassisName,
       "chassisManufacturerName": chassisManufacturerName,
       "chassisModelTypeName": chassisModelTypeName,
       "chassisAssetTagName": chassisAssetTagName,
       "chassisServiceTagName": chassisServiceTagName,
       "chassisID": chassisID,
       "chassisIDExtension": chassisIDExtension,
       "chassisSystemClass": chassisSystemClass,
       "chassisSystemName": chassisSystemName,
       "chassisLEDControlCapabilitiesUnique": chassisLEDControlCapabilitiesUnique,
       "chassisLEDControlSettingsUnique": chassisLEDControlSettingsUnique,
       "chassisIdentifyFlashControlCapabilities": chassisIdentifyFlashControlCapabilities,
       "chassisIdentifyFlashControlSettings": chassisIdentifyFlashControlSettings,
       "chassisLockPresent": chassisLockPresent,
       "chassishostControlCapabilitiesUnique": chassishostControlCapabilitiesUnique,
       "chassishostControlSettingsUnique": chassishostControlSettingsUnique,
       "chassiswatchDogControlCapabilitiesUnique": chassiswatchDogControlCapabilitiesUnique,
       "chassiswatchDogControlSettingsUnique": chassiswatchDogControlSettingsUnique,
       "chassiswatchDogControlExpiryTimeCapabilitiesUnique": chassiswatchDogControlExpiryTimeCapabilitiesUnique,
       "chassiswatchDogControlExpiryTime": chassiswatchDogControlExpiryTime,
       "chassisPowerButtonControlCapabilitiesUnique": chassisPowerButtonControlCapabilitiesUnique,
       "chassisPowerButtonControlSettingsUnique": chassisPowerButtonControlSettingsUnique,
       "chassisNMIButtonControlCapabilitiesUnique": chassisNMIButtonControlCapabilitiesUnique,
       "chassisNMIButtonControlSettingsUnique": chassisNMIButtonControlSettingsUnique,
       "chassisSystemProperties": chassisSystemProperties,
       "chassisSystemRevisionNumber": chassisSystemRevisionNumber,
       "chassisSystemRevisionName": chassisSystemRevisionName,
       "chassisExpressServiceCodeName": chassisExpressServiceCodeName,
       "eventLogTable": eventLogTable,
       "eventLogTableEntry": eventLogTableEntry,
       "eventLogchassisIndex": eventLogchassisIndex,
       "eventLogRecordIndex": eventLogRecordIndex,
       "eventLogStateCapabilitiesUnique": eventLogStateCapabilitiesUnique,
       "eventLogStateSettingsUnique": eventLogStateSettingsUnique,
       "eventLogRecord": eventLogRecord,
       "eventLogFormat": eventLogFormat,
       "eventLogSeverityStatus": eventLogSeverityStatus,
       "eventLogDateName": eventLogDateName,
       "systemBIOSTable": systemBIOSTable,
       "systemBIOSTableEntry": systemBIOSTableEntry,
       "systemBIOSchassisIndex": systemBIOSchassisIndex,
       "systemBIOSIndex": systemBIOSIndex,
       "systemBIOSStateCapabilities": systemBIOSStateCapabilities,
       "systemBIOSStateSettings": systemBIOSStateSettings,
       "systemBIOSStatus": systemBIOSStatus,
       "systemBIOSReleaseDateName": systemBIOSReleaseDateName,
       "systemBIOSVersionName": systemBIOSVersionName,
       "systemBIOSManufacturerName": systemBIOSManufacturerName,
       "firmwareTable": firmwareTable,
       "firmwareTableEntry": firmwareTableEntry,
       "firmwarechassisIndex": firmwarechassisIndex,
       "firmwareIndex": firmwareIndex,
       "firmwareStateCapabilities": firmwareStateCapabilities,
       "firmwareStateSettings": firmwareStateSettings,
       "firmwareStatus": firmwareStatus,
       "firmwareSize": firmwareSize,
       "firmwareType": firmwareType,
       "firmwareTypeName": firmwareTypeName,
       "firmwareUpdateCapabilities": firmwareUpdateCapabilities,
       "firmwareVersionName": firmwareVersionName,
       "intrusionTable": intrusionTable,
       "intrusionTableEntry": intrusionTableEntry,
       "intrusionchassisIndex": intrusionchassisIndex,
       "intrusionIndex": intrusionIndex,
       "intrusionStateCapabilities": intrusionStateCapabilities,
       "intrusionStateSettings": intrusionStateSettings,
       "intrusionStatus": intrusionStatus,
       "intrusionReading": intrusionReading,
       "intrusionType": intrusionType,
       "intrusionLocationName": intrusionLocationName,
       "lcLogTable": lcLogTable,
       "lcLogTableEntry": lcLogTableEntry,
       "lcLogChassisIndex": lcLogChassisIndex,
       "lcLogRecordIndex": lcLogRecordIndex,
       "lcLogSequenceNumber": lcLogSequenceNumber,
       "lcLogCategory": lcLogCategory,
       "lcLogSeverityStatus": lcLogSeverityStatus,
       "lcLogDateName": lcLogDateName,
       "lcLogFQDD": lcLogFQDD,
       "lcLogMessageID": lcLogMessageID,
       "lcLogMessage": lcLogMessage,
       "lcLogDetailedDescription": lcLogDetailedDescription,
       "lcLogRecommededAction": lcLogRecommededAction,
       "lcLogComment": lcLogComment,
       "powerGroup": powerGroup,
       "powerUnitTable": powerUnitTable,
       "powerUnitTableEntry": powerUnitTableEntry,
       "powerUnitchassisIndex": powerUnitchassisIndex,
       "powerUnitIndex": powerUnitIndex,
       "powerUnitStateCapabilities": powerUnitStateCapabilities,
       "powerUnitStateSettings": powerUnitStateSettings,
       "powerUnitRedundancyStatus": powerUnitRedundancyStatus,
       "powerSupplyCountForRedundancy": powerSupplyCountForRedundancy,
       "powerUnitName": powerUnitName,
       "powerUnitStatus": powerUnitStatus,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyTableEntry": powerSupplyTableEntry,
       "powerSupplychassisIndex": powerSupplychassisIndex,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyStateCapabilitiesUnique": powerSupplyStateCapabilitiesUnique,
       "powerSupplyStateSettingsUnique": powerSupplyStateSettingsUnique,
       "powerSupplyStatus": powerSupplyStatus,
       "powerSupplyOutputWatts": powerSupplyOutputWatts,
       "powerSupplyType": powerSupplyType,
       "powerSupplyLocationName": powerSupplyLocationName,
       "powerSupplyMaximumInputVoltage": powerSupplyMaximumInputVoltage,
       "powerSupplypowerUnitIndexReference": powerSupplypowerUnitIndexReference,
       "powerSupplySensorState": powerSupplySensorState,
       "powerSupplyConfigurationErrorType": powerSupplyConfigurationErrorType,
       "powerSupplyPowerMonitorCapable": powerSupplyPowerMonitorCapable,
       "powerSupplyRatedInputWattage": powerSupplyRatedInputWattage,
       "powerSupplyFQDD": powerSupplyFQDD,
       "powerSupplyCurrentInputVoltage": powerSupplyCurrentInputVoltage,
       "voltageProbeTable": voltageProbeTable,
       "voltageProbeTableEntry": voltageProbeTableEntry,
       "voltageProbechassisIndex": voltageProbechassisIndex,
       "voltageProbeIndex": voltageProbeIndex,
       "voltageProbeStateCapabilities": voltageProbeStateCapabilities,
       "voltageProbeStateSettings": voltageProbeStateSettings,
       "voltageProbeStatus": voltageProbeStatus,
       "voltageProbeReading": voltageProbeReading,
       "voltageProbeType": voltageProbeType,
       "voltageProbeLocationName": voltageProbeLocationName,
       "voltageProbeUpperNonRecoverableThreshold": voltageProbeUpperNonRecoverableThreshold,
       "voltageProbeUpperCriticalThreshold": voltageProbeUpperCriticalThreshold,
       "voltageProbeUpperNonCriticalThreshold": voltageProbeUpperNonCriticalThreshold,
       "voltageProbeLowerNonCriticalThreshold": voltageProbeLowerNonCriticalThreshold,
       "voltageProbeLowerCriticalThreshold": voltageProbeLowerCriticalThreshold,
       "voltageProbeLowerNonRecoverableThreshold": voltageProbeLowerNonRecoverableThreshold,
       "voltageProbeProbeCapabilities": voltageProbeProbeCapabilities,
       "voltageProbeDiscreteReading": voltageProbeDiscreteReading,
       "amperageProbeTable": amperageProbeTable,
       "amperageProbeTableEntry": amperageProbeTableEntry,
       "amperageProbechassisIndex": amperageProbechassisIndex,
       "amperageProbeIndex": amperageProbeIndex,
       "amperageProbeStateCapabilities": amperageProbeStateCapabilities,
       "amperageProbeStateSettings": amperageProbeStateSettings,
       "amperageProbeStatus": amperageProbeStatus,
       "amperageProbeReading": amperageProbeReading,
       "amperageProbeType": amperageProbeType,
       "amperageProbeLocationName": amperageProbeLocationName,
       "amperageProbeUpperNonRecoverableThreshold": amperageProbeUpperNonRecoverableThreshold,
       "amperageProbeUpperCriticalThreshold": amperageProbeUpperCriticalThreshold,
       "amperageProbeUpperNonCriticalThreshold": amperageProbeUpperNonCriticalThreshold,
       "amperageProbeLowerNonCriticalThreshold": amperageProbeLowerNonCriticalThreshold,
       "amperageProbeLowerCriticalThreshold": amperageProbeLowerCriticalThreshold,
       "amperageProbeLowerNonRecoverableThreshold": amperageProbeLowerNonRecoverableThreshold,
       "amperageProbeProbeCapabilities": amperageProbeProbeCapabilities,
       "amperageProbeDiscreteReading": amperageProbeDiscreteReading,
       "systemBatteryTable": systemBatteryTable,
       "systemBatteryTableEntry": systemBatteryTableEntry,
       "systemBatteryChassisIndex": systemBatteryChassisIndex,
       "systemBatteryIndex": systemBatteryIndex,
       "systemBatteryStateCapabilities": systemBatteryStateCapabilities,
       "systemBatteryStateSettings": systemBatteryStateSettings,
       "systemBatteryStatus": systemBatteryStatus,
       "systemBatteryReading": systemBatteryReading,
       "systemBatteryLocationName": systemBatteryLocationName,
       "powerUsageTable": powerUsageTable,
       "powerUsageTableEntry": powerUsageTableEntry,
       "powerUsageChassisIndex": powerUsageChassisIndex,
       "powerUsageIndex": powerUsageIndex,
       "powerUsageStateCapabilities": powerUsageStateCapabilities,
       "powerUsageStateSettings": powerUsageStateSettings,
       "powerUsageStatus": powerUsageStatus,
       "powerUsageEntityName": powerUsageEntityName,
       "powerUsageCumulativeWattage": powerUsageCumulativeWattage,
       "powerUsageCumulativeWattageStartDateName": powerUsageCumulativeWattageStartDateName,
       "powerUsagePeakWatts": powerUsagePeakWatts,
       "powerUsagePeakWattsStartDateName": powerUsagePeakWattsStartDateName,
       "powerUsagePeakWattsReadingDateName": powerUsagePeakWattsReadingDateName,
       "powerUsagePeakAmps": powerUsagePeakAmps,
       "powerUsagePeakAmpsStartDateName": powerUsagePeakAmpsStartDateName,
       "powerUsagePeakAmpsReadingDateName": powerUsagePeakAmpsReadingDateName,
       "powerUsageIdlePower": powerUsageIdlePower,
       "powerUsageMaxPotentialPower": powerUsageMaxPotentialPower,
       "powerUsagePowerCapCapabilities": powerUsagePowerCapCapabilities,
       "powerUsagePowerCapSetting": powerUsagePowerCapSetting,
       "powerUsagePowerCapValue": powerUsagePowerCapValue,
       "powerUsageInstantaneousHeadroom": powerUsageInstantaneousHeadroom,
       "powerUsagePeakHeadroom": powerUsagePeakHeadroom,
       "thermalGroup": thermalGroup,
       "coolingUnitTable": coolingUnitTable,
       "coolingUnitTableEntry": coolingUnitTableEntry,
       "coolingUnitchassisIndex": coolingUnitchassisIndex,
       "coolingUnitIndex": coolingUnitIndex,
       "coolingUnitStateCapabilties": coolingUnitStateCapabilties,
       "coolingUnitStateSettings": coolingUnitStateSettings,
       "coolingUnitRedundancyStatus": coolingUnitRedundancyStatus,
       "coolingDeviceCountForRedundancy": coolingDeviceCountForRedundancy,
       "coolingUnitName": coolingUnitName,
       "coolingUnitStatus": coolingUnitStatus,
       "coolingDeviceTable": coolingDeviceTable,
       "coolingDeviceTableEntry": coolingDeviceTableEntry,
       "coolingDevicechassisIndex": coolingDevicechassisIndex,
       "coolingDeviceIndex": coolingDeviceIndex,
       "coolingDeviceStateCapabilities": coolingDeviceStateCapabilities,
       "coolingDeviceStateSettings": coolingDeviceStateSettings,
       "coolingDeviceStatus": coolingDeviceStatus,
       "coolingDeviceReading": coolingDeviceReading,
       "coolingDeviceType": coolingDeviceType,
       "coolingDeviceLocationName": coolingDeviceLocationName,
       "coolingDeviceUpperNonRecoverableThreshold": coolingDeviceUpperNonRecoverableThreshold,
       "coolingDeviceUpperCriticalThreshold": coolingDeviceUpperCriticalThreshold,
       "coolingDeviceUpperNonCriticalThreshold": coolingDeviceUpperNonCriticalThreshold,
       "coolingDeviceLowerNonCriticalThreshold": coolingDeviceLowerNonCriticalThreshold,
       "coolingDeviceLowerCriticalThreshold": coolingDeviceLowerCriticalThreshold,
       "coolingDeviceLowerNonRecoverableThreshold": coolingDeviceLowerNonRecoverableThreshold,
       "coolingDevicecoolingUnitIndexReference": coolingDevicecoolingUnitIndexReference,
       "coolingDeviceSubType": coolingDeviceSubType,
       "coolingDeviceProbeCapabilities": coolingDeviceProbeCapabilities,
       "coolingDeviceDiscreteReading": coolingDeviceDiscreteReading,
       "coolingDeviceFQDD": coolingDeviceFQDD,
       "temperatureProbeTable": temperatureProbeTable,
       "temperatureProbeTableEntry": temperatureProbeTableEntry,
       "temperatureProbechassisIndex": temperatureProbechassisIndex,
       "temperatureProbeIndex": temperatureProbeIndex,
       "temperatureProbeStateCapabilities": temperatureProbeStateCapabilities,
       "temperatureProbeStateSettings": temperatureProbeStateSettings,
       "temperatureProbeStatus": temperatureProbeStatus,
       "temperatureProbeReading": temperatureProbeReading,
       "temperatureProbeType": temperatureProbeType,
       "temperatureProbeLocationName": temperatureProbeLocationName,
       "temperatureProbeUpperNonRecoverableThreshold": temperatureProbeUpperNonRecoverableThreshold,
       "temperatureProbeUpperCriticalThreshold": temperatureProbeUpperCriticalThreshold,
       "temperatureProbeUpperNonCriticalThreshold": temperatureProbeUpperNonCriticalThreshold,
       "temperatureProbeLowerNonCriticalThreshold": temperatureProbeLowerNonCriticalThreshold,
       "temperatureProbeLowerCriticalThreshold": temperatureProbeLowerCriticalThreshold,
       "temperatureProbeLowerNonRecoverableThreshold": temperatureProbeLowerNonRecoverableThreshold,
       "temperatureProbeProbeCapabilities": temperatureProbeProbeCapabilities,
       "temperatureProbeDiscreteReading": temperatureProbeDiscreteReading,
       "deviceGroup": deviceGroup,
       "processorDeviceTable": processorDeviceTable,
       "processorDeviceTableEntry": processorDeviceTableEntry,
       "processorDevicechassisIndex": processorDevicechassisIndex,
       "processorDeviceIndex": processorDeviceIndex,
       "processorDeviceStateCapabilities": processorDeviceStateCapabilities,
       "processorDeviceStateSettings": processorDeviceStateSettings,
       "processorDeviceStatus": processorDeviceStatus,
       "processorDeviceType": processorDeviceType,
       "processorDeviceManufacturerName": processorDeviceManufacturerName,
       "processorDeviceStatusState": processorDeviceStatusState,
       "processorDeviceFamily": processorDeviceFamily,
       "processorDeviceMaximumSpeed": processorDeviceMaximumSpeed,
       "processorDeviceCurrentSpeed": processorDeviceCurrentSpeed,
       "processorDeviceExternalClockSpeed": processorDeviceExternalClockSpeed,
       "processorDeviceVoltage": processorDeviceVoltage,
       "processorDeviceVersionName": processorDeviceVersionName,
       "processorDeviceCoreCount": processorDeviceCoreCount,
       "processorDeviceCoreEnabledCount": processorDeviceCoreEnabledCount,
       "processorDeviceThreadCount": processorDeviceThreadCount,
       "processorDeviceCharacteristics": processorDeviceCharacteristics,
       "processorDeviceExtendedCapabilities": processorDeviceExtendedCapabilities,
       "processorDeviceExtendedSettings": processorDeviceExtendedSettings,
       "processorDeviceBrandName": processorDeviceBrandName,
       "processorDeviceFQDD": processorDeviceFQDD,
       "processorDeviceStatusTable": processorDeviceStatusTable,
       "processorDeviceStatusTableEntry": processorDeviceStatusTableEntry,
       "processorDeviceStatusChassisIndex": processorDeviceStatusChassisIndex,
       "processorDeviceStatusIndex": processorDeviceStatusIndex,
       "processorDeviceStatusStateCapabilities": processorDeviceStatusStateCapabilities,
       "processorDeviceStatusStateSettings": processorDeviceStatusStateSettings,
       "processorDeviceStatusStatus": processorDeviceStatusStatus,
       "processorDeviceStatusReading": processorDeviceStatusReading,
       "processorDeviceStatusLocationName": processorDeviceStatusLocationName,
       "memoryDeviceTable": memoryDeviceTable,
       "memoryDeviceTableEntry": memoryDeviceTableEntry,
       "memoryDevicechassisIndex": memoryDevicechassisIndex,
       "memoryDeviceIndex": memoryDeviceIndex,
       "memoryDeviceStateCapabilities": memoryDeviceStateCapabilities,
       "memoryDeviceStateSettings": memoryDeviceStateSettings,
       "memoryDeviceStatus": memoryDeviceStatus,
       "memoryDeviceType": memoryDeviceType,
       "memoryDeviceLocationName": memoryDeviceLocationName,
       "memoryDeviceBankLocationName": memoryDeviceBankLocationName,
       "memoryDeviceSize": memoryDeviceSize,
       "memoryDeviceSpeed": memoryDeviceSpeed,
       "memoryDeviceManufacturerName": memoryDeviceManufacturerName,
       "memoryDevicePartNumberName": memoryDevicePartNumberName,
       "memoryDeviceSerialNumberName": memoryDeviceSerialNumberName,
       "memoryDeviceFQDD": memoryDeviceFQDD,
       "memoryDeviceCurrentOperatingSpeed": memoryDeviceCurrentOperatingSpeed,
       "pCIDeviceTable": pCIDeviceTable,
       "pCIDeviceTableEntry": pCIDeviceTableEntry,
       "pCIDevicechassisIndex": pCIDevicechassisIndex,
       "pCIDeviceIndex": pCIDeviceIndex,
       "pCIDeviceStateCapabilities": pCIDeviceStateCapabilities,
       "pCIDeviceStateSettings": pCIDeviceStateSettings,
       "pCIDeviceStatus": pCIDeviceStatus,
       "pCIDeviceDataBusWidth": pCIDeviceDataBusWidth,
       "pCIDeviceManufacturerName": pCIDeviceManufacturerName,
       "pCIDeviceDescriptionName": pCIDeviceDescriptionName,
       "pCIDeviceFQDD": pCIDeviceFQDD,
       "networkDeviceTable": networkDeviceTable,
       "networkDeviceTableEntry": networkDeviceTableEntry,
       "networkDeviceChassisIndex": networkDeviceChassisIndex,
       "networkDeviceIndex": networkDeviceIndex,
       "networkDeviceStatus": networkDeviceStatus,
       "networkDeviceConnectionStatus": networkDeviceConnectionStatus,
       "networkDeviceProductName": networkDeviceProductName,
       "networkDeviceVendorName": networkDeviceVendorName,
       "networkDeviceCurrentMACAddress": networkDeviceCurrentMACAddress,
       "networkDevicePermanentMACAddress": networkDevicePermanentMACAddress,
       "networkDevicePCIBusNumber": networkDevicePCIBusNumber,
       "networkDevicePCIDeviceNumber": networkDevicePCIDeviceNumber,
       "networkDevicePCIFunctionNumber": networkDevicePCIFunctionNumber,
       "networkDeviceTOECapabilityFlags": networkDeviceTOECapabilityFlags,
       "networkDeviceiSCSICapabilityFlags": networkDeviceiSCSICapabilityFlags,
       "networkDeviceiSCSIEnabled": networkDeviceiSCSIEnabled,
       "networkDeviceCapabilities": networkDeviceCapabilities,
       "networkDeviceFQDD": networkDeviceFQDD,
       "slotGroup": slotGroup,
       "systemSlotTable": systemSlotTable,
       "systemSlotTableEntry": systemSlotTableEntry,
       "systemSlotchassisIndex": systemSlotchassisIndex,
       "systemSlotIndex": systemSlotIndex,
       "systemSlotStateCapabilitiesUnique": systemSlotStateCapabilitiesUnique,
       "systemSlotStateSettingsUnique": systemSlotStateSettingsUnique,
       "systemSlotStatus": systemSlotStatus,
       "systemSlotCurrentUsage": systemSlotCurrentUsage,
       "systemSlotType": systemSlotType,
       "systemSlotSlotExternalSlotName": systemSlotSlotExternalSlotName,
       "systemSlotCategory": systemSlotCategory,
       "fruGroup": fruGroup,
       "fruTable": fruTable,
       "fruTableEntry": fruTableEntry,
       "fruChassisIndex": fruChassisIndex,
       "fruIndex": fruIndex,
       "fruInformationStatus": fruInformationStatus,
       "fruManufacturerName": fruManufacturerName,
       "fruSerialNumberName": fruSerialNumberName,
       "fruPartNumberName": fruPartNumberName,
       "fruRevisionName": fruRevisionName,
       "fruFQDD": fruFQDD,
       "storageDetailsGroup": storageDetailsGroup,
       "software": software,
       "storageManagement": storageManagement,
       "physicalDevices": physicalDevices,
       "controllerTable": controllerTable,
       "controllerTableEntry": controllerTableEntry,
       "controllerNumber": controllerNumber,
       "controllerName": controllerName,
       "controllerRebuildRate": controllerRebuildRate,
       "controllerFWVersion": controllerFWVersion,
       "controllerCacheSizeInMB": controllerCacheSizeInMB,
       "controllerRollUpStatus": controllerRollUpStatus,
       "controllerComponentStatus": controllerComponentStatus,
       "controllerDriverVersion": controllerDriverVersion,
       "controllerPCISlot": controllerPCISlot,
       "controllerReconstructRate": controllerReconstructRate,
       "controllerPatrolReadRate": controllerPatrolReadRate,
       "controllerBGIRate": controllerBGIRate,
       "controllerCheckConsistencyRate": controllerCheckConsistencyRate,
       "controllerPatrolReadMode": controllerPatrolReadMode,
       "controllerPatrolReadState": controllerPatrolReadState,
       "controllerPersistentHotSpare": controllerPersistentHotSpare,
       "controllerSpinDownUnconfiguredDrives": controllerSpinDownUnconfiguredDrives,
       "controllerSpinDownHotSpareDrives": controllerSpinDownHotSpareDrives,
       "controllerSpinDownTimeInterval": controllerSpinDownTimeInterval,
       "controllerPreservedCache": controllerPreservedCache,
       "controllerCheckConsistencyMode": controllerCheckConsistencyMode,
       "controllerCopyBackMode": controllerCopyBackMode,
       "controllerSecurityStatus": controllerSecurityStatus,
       "controllerEncryptionKeyPresent": controllerEncryptionKeyPresent,
       "controllerEncryptionCapability": controllerEncryptionCapability,
       "controllerLoadBalanceSetting": controllerLoadBalanceSetting,
       "controllerMaxCapSpeed": controllerMaxCapSpeed,
       "controllerSASAddress": controllerSASAddress,
       "controllerFQDD": controllerFQDD,
       "controllerDisplayName": controllerDisplayName,
       "controllerT10PICapability": controllerT10PICapability,
       "controllerRAID10UnevenSpansSupported": controllerRAID10UnevenSpansSupported,
       "controllerEnhancedAutoImportForeignConfigMode": controllerEnhancedAutoImportForeignConfigMode,
       "controllerBootModeSupported": controllerBootModeSupported,
       "controllerBootMode": controllerBootMode,
       "enclosureTable": enclosureTable,
       "enclosureTableEntry": enclosureTableEntry,
       "enclosureNumber": enclosureNumber,
       "enclosureName": enclosureName,
       "enclosureState": enclosureState,
       "enclosureServiceTag": enclosureServiceTag,
       "enclosureAssetTag": enclosureAssetTag,
       "enclosureConnectedPort": enclosureConnectedPort,
       "enclosureRollUpStatus": enclosureRollUpStatus,
       "enclosureComponentStatus": enclosureComponentStatus,
       "enclosureFirmwareVersion": enclosureFirmwareVersion,
       "enclosureSASAddress": enclosureSASAddress,
       "enclosureDriveCount": enclosureDriveCount,
       "enclosureTotalSlots": enclosureTotalSlots,
       "enclosureFanCount": enclosureFanCount,
       "enclosurePSUCount": enclosurePSUCount,
       "enclosureEMMCount": enclosureEMMCount,
       "enclosureTempProbeCount": enclosureTempProbeCount,
       "enclosureRedundantPath": enclosureRedundantPath,
       "enclosurePosition": enclosurePosition,
       "enclosureBackplaneBayID": enclosureBackplaneBayID,
       "enclosureFQDD": enclosureFQDD,
       "enclosureDisplayName": enclosureDisplayName,
       "enclosureType": enclosureType,
       "physicalDiskTable": physicalDiskTable,
       "physicalDiskTableEntry": physicalDiskTableEntry,
       "physicalDiskNumber": physicalDiskNumber,
       "physicalDiskName": physicalDiskName,
       "physicalDiskManufacturer": physicalDiskManufacturer,
       "physicalDiskState": physicalDiskState,
       "physicalDiskProductID": physicalDiskProductID,
       "physicalDiskSerialNo": physicalDiskSerialNo,
       "physicalDiskRevision": physicalDiskRevision,
       "physicalDiskCapacityInMB": physicalDiskCapacityInMB,
       "physicalDiskUsedSpaceInMB": physicalDiskUsedSpaceInMB,
       "physicalDiskFreeSpaceInMB": physicalDiskFreeSpaceInMB,
       "physicalDiskBusType": physicalDiskBusType,
       "physicalDiskSpareState": physicalDiskSpareState,
       "physicalDiskComponentStatus": physicalDiskComponentStatus,
       "physicalDiskPartNumber": physicalDiskPartNumber,
       "physicalDiskSASAddress": physicalDiskSASAddress,
       "physicalDiskNegotiatedSpeed": physicalDiskNegotiatedSpeed,
       "physicalDiskCapableSpeed": physicalDiskCapableSpeed,
       "physicalDiskSmartAlertIndication": physicalDiskSmartAlertIndication,
       "physicalDiskManufactureDay": physicalDiskManufactureDay,
       "physicalDiskManufactureWeek": physicalDiskManufactureWeek,
       "physicalDiskManufactureYear": physicalDiskManufactureYear,
       "physicalDiskMediaType": physicalDiskMediaType,
       "physicalDiskPowerState": physicalDiskPowerState,
       "physicalDiskRemainingRatedWriteEndurance": physicalDiskRemainingRatedWriteEndurance,
       "physicalDiskOperationalState": physicalDiskOperationalState,
       "physicalDiskProgress": physicalDiskProgress,
       "physicalDiskSecurityStatus": physicalDiskSecurityStatus,
       "physicalDiskFormFactor": physicalDiskFormFactor,
       "physicalDiskFQDD": physicalDiskFQDD,
       "physicalDiskDisplayName": physicalDiskDisplayName,
       "physicalDiskT10PICapability": physicalDiskT10PICapability,
       "physicalDiskBlockSizeInBytes": physicalDiskBlockSizeInBytes,
       "physicalDiskProtocolVersion": physicalDiskProtocolVersion,
       "physicalDiskPCIeNegotiatedLinkWidth": physicalDiskPCIeNegotiatedLinkWidth,
       "physicalDiskPCIeCapableLinkWidth": physicalDiskPCIeCapableLinkWidth,
       "enclosureFanTable": enclosureFanTable,
       "enclosureFanTableEntry": enclosureFanTableEntry,
       "enclosureFanNumber": enclosureFanNumber,
       "enclosureFanName": enclosureFanName,
       "enclosureFanState": enclosureFanState,
       "enclosureFanSpeed": enclosureFanSpeed,
       "enclosureFanComponentStatus": enclosureFanComponentStatus,
       "enclosureFanFQDD": enclosureFanFQDD,
       "enclosureFanDisplayName": enclosureFanDisplayName,
       "enclosurePowerSupplyTable": enclosurePowerSupplyTable,
       "enclosurePowerSupplyTableEntry": enclosurePowerSupplyTableEntry,
       "enclosurePowerSupplyNumber": enclosurePowerSupplyNumber,
       "enclosurePowerSupplyName": enclosurePowerSupplyName,
       "enclosurePowerSupplyState": enclosurePowerSupplyState,
       "enclosurePowerSupplyPartNumber": enclosurePowerSupplyPartNumber,
       "enclosurePowerSupplyComponentStatus": enclosurePowerSupplyComponentStatus,
       "enclosurePowerSupplyFQDD": enclosurePowerSupplyFQDD,
       "enclosurePowerSupplyDisplayName": enclosurePowerSupplyDisplayName,
       "enclosureTemperatureProbeTable": enclosureTemperatureProbeTable,
       "enclosureTemperatureProbeTableEntry": enclosureTemperatureProbeTableEntry,
       "enclosureTemperatureProbeNumber": enclosureTemperatureProbeNumber,
       "enclosureTemperatureProbeName": enclosureTemperatureProbeName,
       "enclosureTemperatureProbeState": enclosureTemperatureProbeState,
       "enclosureTemperatureProbeMinWarningValue": enclosureTemperatureProbeMinWarningValue,
       "enclosureTemperatureProbeMinCriticalValue": enclosureTemperatureProbeMinCriticalValue,
       "enclosureTemperatureProbeMaxWarningValue": enclosureTemperatureProbeMaxWarningValue,
       "enclosureTemperatureProbeMaxCriticalValue": enclosureTemperatureProbeMaxCriticalValue,
       "enclosureTemperatureProbeCurValue": enclosureTemperatureProbeCurValue,
       "enclosureTemperatureProbeComponentStatus": enclosureTemperatureProbeComponentStatus,
       "enclosureTemperatureProbeFQDD": enclosureTemperatureProbeFQDD,
       "enclosureTemperatureProbeDisplayName": enclosureTemperatureProbeDisplayName,
       "enclosureManagementModuleTable": enclosureManagementModuleTable,
       "enclosureManagementModuleTableEntry": enclosureManagementModuleTableEntry,
       "enclosureManagementModuleNumber": enclosureManagementModuleNumber,
       "enclosureManagementModuleName": enclosureManagementModuleName,
       "enclosureManagementModuleState": enclosureManagementModuleState,
       "enclosureManagementModulePartNumber": enclosureManagementModulePartNumber,
       "enclosureManagementModuleFWVersion": enclosureManagementModuleFWVersion,
       "enclosureManagementModuleComponentStatus": enclosureManagementModuleComponentStatus,
       "enclosureManagementModuleFQDD": enclosureManagementModuleFQDD,
       "enclosureManagementModuleDisplayName": enclosureManagementModuleDisplayName,
       "batteryTable": batteryTable,
       "batteryTableEntry": batteryTableEntry,
       "batteryNumber": batteryNumber,
       "batteryState": batteryState,
       "batteryComponentStatus": batteryComponentStatus,
       "batteryPredictedCapacity": batteryPredictedCapacity,
       "batteryFQDD": batteryFQDD,
       "batteryDisplayName": batteryDisplayName,
       "logicalDevices": logicalDevices,
       "virtualDiskTable": virtualDiskTable,
       "virtualDiskTableEntry": virtualDiskTableEntry,
       "virtualDiskNumber": virtualDiskNumber,
       "virtualDiskName": virtualDiskName,
       "virtualDiskState": virtualDiskState,
       "virtualDiskSizeInMB": virtualDiskSizeInMB,
       "virtualDiskWritePolicy": virtualDiskWritePolicy,
       "virtualDiskReadPolicy": virtualDiskReadPolicy,
       "virtualDiskLayout": virtualDiskLayout,
       "virtualDiskStripeSize": virtualDiskStripeSize,
       "virtualDiskComponentStatus": virtualDiskComponentStatus,
       "virtualDiskBadBlocksDetected": virtualDiskBadBlocksDetected,
       "virtualDiskSecured": virtualDiskSecured,
       "virtualDiskIsCacheCade": virtualDiskIsCacheCade,
       "virtualDiskDiskCachePolicy": virtualDiskDiskCachePolicy,
       "virtualDiskOperationalState": virtualDiskOperationalState,
       "virtualDiskProgress": virtualDiskProgress,
       "virtualDiskAvailableProtocols": virtualDiskAvailableProtocols,
       "virtualDiskMediaType": virtualDiskMediaType,
       "virtualDiskRemainingRedundancy": virtualDiskRemainingRedundancy,
       "virtualDiskFQDD": virtualDiskFQDD,
       "virtualDiskDisplayName": virtualDiskDisplayName,
       "virtualDiskT10PIStatus": virtualDiskT10PIStatus,
       "virtualDiskBlockSizeInBytes": virtualDiskBlockSizeInBytes}
)
