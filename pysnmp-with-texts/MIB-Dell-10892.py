"""SNMP MIB module (MIB-Dell-10892) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIB-DELL-10892
Produced by pysmi-1.3.3 at Sun Mar 10 11:24:26 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(Counter32,
 TimeTicks,
 NotificationType,
 iso,
 Bits,
 NotificationType,
 IpAddress,
 Counter64,
 Integer32,
 enterprises,
 ModuleIdentity,
 ObjectIdentity,
 Gauge32,
 Unsigned32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 MibIdentifier) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "TimeTicks",
    "NotificationType",
    "iso",
    "Bits",
    "NotificationType",
    "IpAddress",
    "Counter64",
    "Integer32",
    "enterprises",
    "ModuleIdentity",
    "ObjectIdentity",
    "Gauge32",
    "Unsigned32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "MibIdentifier")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DellSecurityString(DisplayString):
    """Custom type DellSecurityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class DellCostofOwnershipString(DisplayString):
    """Custom type DellCostofOwnershipString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DellObjectRange(Integer32):
    """Custom type DellObjectRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )





class DellUnsigned8BitRange(Integer32):
    """Custom type DellUnsigned8BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DellUnsigned16BitRange(Integer32):
    """Custom type DellUnsigned16BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DellUnsigned32BitRange(Integer32):
    """Custom type DellUnsigned32BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class DellSigned32BitRange(Integer32):
    """Custom type DellSigned32BitRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )





class DellBoolean(Integer32):
    """Custom type DellBoolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )





class DellStateCapabilities(Integer32):
    """Custom type DellStateCapabilities based on Integer32"""
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





class DellStateSettings(Integer32):
    """Custom type DellStateSettings based on Integer32"""
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





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
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





class DellStatusRedundancy(Integer32):
    """Custom type DellStatusRedundancy based on Integer32"""
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





class DellStatusProbe(Integer32):
    """Custom type DellStatusProbe based on Integer32"""
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





class DellUnsigned64BitRange(OctetString):
    """Custom type DellUnsigned64BitRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class DellDateName(DisplayString):
    """Custom type DellDateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )





class SMSSupportedTypes(Integer32):
    """Custom type SMSSupportedTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("supportsCIMOM", 4),
          ("supportsDMI", 2),
          ("supportsSNMP", 1),
          ("supportsSNMPandDMIandCIMOM", 7))
    )





class DellLogFormat(Integer32):
    """Custom type DellLogFormat based on Integer32"""
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





class DellChassisType(Integer32):
    """Custom type DellChassisType based on Integer32"""
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
              24)
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





class DellConnectionStatus(Integer32):
    """Custom type DellConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failure", 4),
          ("ok", 3),
          ("unknown", 2))
    )





class DellFanControlCapabilities(Integer32):
    """Custom type DellFanControlCapabilities based on Integer32"""
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
        *(("highSpeedCapable", 4),
          ("lowOrHighSpeedCapable", 6),
          ("lowSpeedCapable", 2),
          ("unknown", 1))
    )





class DellFanControlSettings(Integer32):
    """Custom type DellFanControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("highSpeed", 4),
          ("lowSpeed", 2),
          ("unknown", 1))
    )





class DellLEDControlCapabilities(Integer32):
    """Custom type DellLEDControlCapabilities based on Integer32"""
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





class DellLEDControlSettings(Integer32):
    """Custom type DellLEDControlSettings based on Integer32"""
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





class DellHDFaultLEDControlCapabilities(Integer32):
    """Custom type DellHDFaultLEDControlCapabilities based on Integer32"""
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
          ("notReadyCapable", 4),
          ("resetCapable", 8),
          ("unknownCapabilities", 1))
    )





class DellHDFaultLEDControlSettings(Integer32):
    """Custom type DellHDFaultLEDControlSettings based on Integer32"""
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
          ("notReady", 4),
          ("reset", 8),
          ("resetAndEnable", 10),
          ("unknown", 1))
    )





class DellChassisIdentifyControlCapabilities(Integer32):
    """Custom type DellChassisIdentifyControlCapabilities based on Integer32"""
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





class DellChassisIdentifyControlSettings(Integer32):
    """Custom type DellChassisIdentifyControlSettings based on Integer32"""
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





class DellHostControlCapabilities(Integer32):
    """Custom type DellHostControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("manualAllExceptOperatingSystemShutdownCapable", 7),
          ("manualFullyCapable", 15),
          ("manualOperatingSystemShutdownCapable", 8),
          ("manualPowerCycleCapable", 4),
          ("manualPowerOFFCapable", 2),
          ("manualRebootCapable", 1))
    )





class DellHostControlSettings(Integer32):
    """Custom type DellHostControlSettings based on Integer32"""
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





class DellWatchDogControlCapabilities(Integer32):
    """Custom type DellWatchDogControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("automaticAllExceptNotificationCapable", 11),
          ("automaticFullyCapable", 15),
          ("automaticNotificationCapable", 4),
          ("automaticPowerCycleCapable", 2),
          ("automaticRebootCapable", 1),
          ("automaticWatchDogTimerCapable", 8))
    )





class DelllWatchControlSettings(Integer32):
    """Custom type DelllWatchControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("automaticNotificationEnabled", 4),
          ("automaticPowerCycleEnabled", 2),
          ("automaticRebootEnabled", 1))
    )





class DellWatchDogTimerCapabilities(Integer32):
    """Custom type DellWatchDogTimerCapabilities based on Integer32"""
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





class DellPowerButtonControlCapabilities(Integer32):
    """Custom type DellPowerButtonControlCapabilities based on Integer32"""
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





class DellPowerButtonControlSettings(Integer32):
    """Custom type DellPowerButtonControlSettings based on Integer32"""
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





class DellChassisSystemClass(Integer32):
    """Custom type DellChassisSystemClass based on Integer32"""
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





class DellUUIDType(Integer32):
    """Custom type DellUUIDType based on Integer32"""
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
        *(("motherBoard", 3),
          ("other", 1),
          ("peripheralBayBackPlane", 6),
          ("powerSupplyParallelingBoard", 5),
          ("secondaryBackPlane", 7),
          ("systemBackPlane", 4),
          ("unknown", 2))
    )





class DellStateCapabilitiesLogUnique(Integer32):
    """Custom type DellStateCapabilitiesLogUnique based on Integer32"""
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





class DellStateSettingsLogUnique(Integer32):
    """Custom type DellStateSettingsLogUnique based on Integer32"""
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





class DellFirwareType(Integer32):
    """Custom type DellFirwareType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("baseboardManagementController", 10),
          ("embeddedSystemManagementController", 4),
          ("frontPanel", 9),
          ("hendrixApplication", 8),
          ("hendrixKernel", 7),
          ("hotPlugPCI", 11),
          ("other", 1),
          ("peripheralBay", 13),
          ("powerSupplyParallelingBoard", 5),
          ("secondaryBackPlane", 14),
          ("sensorData", 12),
          ("systemBOIS", 3),
          ("systemBackPlane", 6),
          ("unknown", 2))
    )





class DellIntrusionReading(Integer32):
    """Custom type DellIntrusionReading based on Integer32"""
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





class DellIntrusionType(Integer32):
    """Custom type DellIntrusionType based on Integer32"""
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





class DellSystemResourceMapType(Integer32):
    """Custom type DellSystemResourceMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("typeOne", 3),
          ("unknown", 2))
    )





class DellResourceOwnerInterfaceType(Integer32):
    """Custom type DellResourceOwnerInterfaceType based on Integer32"""
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
        *(("typeIsEISA", 5),
          ("typeIsISA", 4),
          ("typeIsInternal", 3),
          ("typeIsMCA", 6),
          ("typeIsOther", 1),
          ("typeIsPCI", 8),
          ("typeIsTurboChannel", 7),
          ("typeIsUnknown", 2))
    )





class DellResourceShareDisposition(Integer32):
    """Custom type DellResourceShareDisposition based on Integer32"""
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
        *(("shareIsDeviceExclusive", 3),
          ("shareIsDriverExclusive", 4),
          ("shareIsOther", 1),
          ("shareIsShared", 5),
          ("shareIsUnknown", 2))
    )





class DellResourceMemoryFlags(Integer32):
    """Custom type DellResourceMemoryFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("memoryIsCombinedWritable", 8),
          ("memoryIsF24", 16),
          ("memoryIsPreFetchable", 4),
          ("memoryIsReadAndWrite", 3),
          ("memoryIsReadOnly", 1),
          ("memoryIsWriteOnly", 2))
    )





class DellResourceInterruptType(Integer32):
    """Custom type DellResourceInterruptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interruptIsLatched", 2),
          ("interruptIsLevelSensitive", 1))
    )





class DellResourceInterruptTrigger(Integer32):
    """Custom type DellResourceInterruptTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interruptIsActiveWhenHigh", 2),
          ("interruptIsActiveWhenLow", 1))
    )





class DellResourceDMATransferWidth(Integer32):
    """Custom type DellResourceDMATransferWidth based on Integer32"""
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
        *(("dmaTransferWidthIs128Bits", 7),
          ("dmaTransferWidthIs16Bits", 4),
          ("dmaTransferWidthIs32Bits", 5),
          ("dmaTransferWidthIs64Bits", 6),
          ("dmaTransferWidthIs8Bits", 3),
          ("dmaTransferWidthIsOther", 1),
          ("dmaTransferWidthIsunknown", 2))
    )





class DellResourceDMABusMaster(Integer32):
    """Custom type DellResourceDMABusMaster based on Integer32"""
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
        *(("dmaIsABusmaster", 4),
          ("dmaIsNotABusmaster", 3),
          ("dmaIsOther", 1),
          ("dmaIsUnknown", 2))
    )





class DellPowerSupplyStateCapabilitiesUnique(Integer32):
    """Custom type DellPowerSupplyStateCapabilitiesUnique based on Integer32"""
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





class DellPowerSupplyStateSettingsUnique(Integer32):
    """Custom type DellPowerSupplyStateSettingsUnique based on Integer32"""
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
              66,
              128,
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
          ("onlineandAcSwitchIsON", 66),
          ("powerSupplyIsOK", 32),
          ("powerSupplyIsON", 16),
          ("unknown", 1))
    )





class DellPowerSupplyType(Integer32):
    """Custom type DellPowerSupplyType based on Integer32"""
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
        *(("powerSupplyTypeIsBattery", 5),
          ("powerSupplyTypeIsConverter", 7),
          ("powerSupplyTypeIsLinear", 3),
          ("powerSupplyTypeIsOther", 1),
          ("powerSupplyTypeIsRegulator", 8),
          ("powerSupplyTypeIsSwitching", 4),
          ("powerSupplyTypeIsUPS", 6),
          ("powerSupplyTypeIsUnknown", 2))
    )





class DellVoltageType(Integer32):
    """Custom type DellVoltageType based on Integer32"""
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
        *(("voltageProbeTypeIs12Volt", 7),
          ("voltageProbeTypeIs1Point5Volt", 3),
          ("voltageProbeTypeIs2Point5Volt", 14),
          ("voltageProbeTypeIs3Point3Volt", 4),
          ("voltageProbeTypeIs5Volt", 5),
          ("voltageProbeTypeIsBattery", 12),
          ("voltageProbeTypeIsCore", 10),
          ("voltageProbeTypeIsFLEA", 11),
          ("voltageProbeTypeIsGTL", 15),
          ("voltageProbeTypeIsIO", 9),
          ("voltageProbeTypeIsMinus12Volt", 8),
          ("voltageProbeTypeIsMinus5Volt", 6),
          ("voltageProbeTypeIsOther", 1),
          ("voltageProbeTypeIsTerminator", 13),
          ("voltageProbeTypeIsUnknown", 2))
    )





class DellAmperageProbeType(Integer32):
    """Custom type DellAmperageProbeType based on Integer32"""
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
        *(("amperageProbeTypeIs12Volt", 7),
          ("amperageProbeTypeIs1Point5Volt", 3),
          ("amperageProbeTypeIs2Point5Volt", 14),
          ("amperageProbeTypeIs3Point3volt", 4),
          ("amperageProbeTypeIs5Volt", 5),
          ("amperageProbeTypeIsBattery", 12),
          ("amperageProbeTypeIsCore", 10),
          ("amperageProbeTypeIsFLEA", 11),
          ("amperageProbeTypeIsGTL", 15),
          ("amperageProbeTypeIsIO", 9),
          ("amperageProbeTypeIsMinus12Volt", 8),
          ("amperageProbeTypeIsMinus5Volt", 6),
          ("amperageProbeTypeIsOther", 1),
          ("amperageProbeTypeIsTerminator", 13),
          ("amperageProbeTypeIsUnknown", 2))
    )





class DellACPowerSwitchCapabilities(Integer32):
    """Custom type DellACPowerSwitchCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              14,
              16,
              30,
              32,
              62)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceAllCapable", 62),
          ("inputSourceAllExceptSharedCapable", 30),
          ("inputSourceCord1NoReturnCapable", 2),
          ("inputSourceCord1NoReturnCord1ReturnAndCord2NoReturnCapable", 14),
          ("inputSourceCord1ReturnCapable", 4),
          ("inputSourceCord2NoReturnCapable", 8),
          ("inputSourceCord2ReturnCapable", 16),
          ("inputSourceSharedCapable", 32),
          ("unknownCapabilities", 1))
    )





class DellACPowerSwitchSettings(Integer32):
    """Custom type DellACPowerSwitchSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceCord1NoReturn", 2),
          ("inputSourceCord1Return", 4),
          ("inputSourceCord2NoReturn", 8),
          ("inputSourceCord2Return", 16),
          ("inputSourceShared", 32),
          ("unknown", 1))
    )





class DellACPowerSwitchRedundancyMode(Integer32):
    """Custom type DellACPowerSwitchRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRedundant", 1),
          ("redundant", 2))
    )





class DellACPowerCordStateCapabilities(Integer32):
    """Custom type DellACPowerCordStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknown", 1))
    )





class DellACPowerCordStateSettings(Integer32):
    """Custom type DellACPowerCordStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              26)
        )
    )
    namedValues = NamedValues(
        *(("acPowerCordHasPower", 8),
          ("acPowerCordIsActiveSource", 16),
          ("acPowerCordIsEnabledAndHasPower", 10),
          ("acPowerCordIsEnabledHasPowerAndIsActiveSource", 26),
          ("enabled", 2),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellCoolingDeviceType(Integer32):
    """Custom type DellCoolingDeviceType based on Integer32"""
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





class DellCoolingDeviceSubType(Integer32):
    """Custom type DellCoolingDeviceSubType based on Integer32"""
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
        *(("coolingDeviceSubTypeIsAFanReadsONorOFF", 4),
          ("coolingDeviceSubTypeIsAFanThatReadsInRPM", 3),
          ("coolingDeviceSubTypeIsAPowerSupplyFanThatReadsONorOFF", 6),
          ("coolingDeviceSubTypeIsAPowerSupplyFanThatReadsinRPM", 5),
          ("coolingDeviceSubTypeIsOther", 1),
          ("coolingDeviceSubTypeIsUnknown", 2))
    )





class DellTemperatureProbeType(Integer32):
    """Custom type DellTemperatureProbeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("temperatureProbeTypeIsAmbientESM", 3),
          ("temperatureProbeTypeIsOther", 1),
          ("temperatureProbeTypeIsUnknown", 2))
    )





class DellRemoteFlashBIOSStateCapabilitiesUnique(Integer32):
    """Custom type DellRemoteFlashBIOSStateCapabilitiesUnique based on Integer32"""
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
        *(("cancelCapable", 8),
          ("enableAndCancelCapable", 10),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknown", 1))
    )





class DellRemoteFlashBIOSStateSettingsUnique(Integer32):
    """Custom type DellRemoteFlashBIOSStateSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("canceled", 8),
          ("enabled", 2),
          ("notReady", 4),
          ("other", 32),
          ("pending", 16),
          ("unknown", 1))
    )





class DellRemoteFlashBIOSCompletionCode(Integer32):
    """Custom type DellRemoteFlashBIOSCompletionCode based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("completionCodeIsBadImage", 4),
          ("completionCodeIsDataMiscompare", 15),
          ("completionCodeIsDisabled", 7),
          ("completionCodeIsFlashMemoryFailed", 13),
          ("completionCodeIsGeneralFailure", 14),
          ("completionCodeIsNo12VoltRemoval", 12),
          ("completionCodeIsNo12VoltSet", 11),
          ("completionCodeIsNoBattery", 8),
          ("completionCodeIsNoChargedBattery", 9),
          ("completionCodeIsNoExternalPower", 10),
          ("completionCodeIsNoFileAccess", 5),
          ("completionCodeIsNoImageFound", 16),
          ("completionCodeIsNoUpdatePerformed", 17),
          ("completionCodeIsNotReady", 6),
          ("completionCodeIsOK", 3),
          ("completionCodeIsOther", 1),
          ("completionCodeIsUnknown", 2))
    )





class DellGenericPortConnectorType(Integer32):
    """Custom type DellGenericPortConnectorType based on Integer32"""
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("portConnectorTypeISSASCSI", 21),
          ("portConnectorTypeIs1394", 35),
          ("portConnectorTypeIsAccessBussUSB", 20),
          ("portConnectorTypeIsBNC", 34),
          ("portConnectorTypeIsCDROMLineOut", 30),
          ("portConnectorTypeIsCentronics", 3),
          ("portConnectorTypeIsCirdin8Female", 23),
          ("portConnectorTypeIsCirdin8Male", 22),
          ("portConnectorTypeIsDB15Female", 9),
          ("portConnectorTypeIsDB15Male", 8),
          ("portConnectorTypeIsDB25Female", 7),
          ("portConnectorTypeIsDB25Male", 6),
          ("portConnectorTypeIsDB9Female", 11),
          ("portConnectorTypeIsDB9Male", 10),
          ("portConnectorTypeIsDIN25Pin", 27),
          ("portConnectorTypeIsDIN50Pin", 28),
          ("portConnectorTypeIsDIN68Pin", 29),
          ("portConnectorTypeIsDIN9Pin", 26),
          ("portConnectorTypeIsFloppy", 25),
          ("portConnectorTypeIsHPHIL", 19),
          ("portConnectorTypeIsIDE", 24),
          ("portConnectorTypeIsInfrared", 18),
          ("portConnectorTypeIsMicroDIN", 16),
          ("portConnectorTypeIsMiniCentronics", 4),
          ("portConnectorTypeIsMiniCentronics14", 31),
          ("portConnectorTypeIsMiniCentronics26", 32),
          ("portConnectorTypeIsMiniDIN", 15),
          ("portConnectorTypeIsMiniJack", 33),
          ("portConnectorTypeIsMiniSCSI50Pin", 14),
          ("portConnectorTypeIsNone", 2),
          ("portConnectorTypeIsOther", 1),
          ("portConnectorTypeIsPC98", 36),
          ("portConnectorTypeIsPC98Full", 40),
          ("portConnectorTypeIsPC98Hireso", 37),
          ("portConnectorTypeIsPC98Note", 39),
          ("portConnectorTypeIsPCH98", 38),
          ("portConnectorTypeIsPS2", 17),
          ("portConnectorTypeIsProprietary", 5),
          ("portConnectorTypeIsRJ11", 12),
          ("portConnectorTypeIsRJ45", 13))
    )





class DellPortSecurityState(Integer32):
    """Custom type DellPortSecurityState based on Integer32"""
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
        *(("bootByPass", 6),
          ("externalIsDisabled", 4),
          ("externalIsEnabled", 5),
          ("none", 3),
          ("other", 1),
          ("unknown", 2))
    )





class DellPointingPortConnectorType(Integer32):
    """Custom type DellPointingPortConnectorType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsADB", 8),
          ("connectorPortTypeIsAccessBusUSB", 11),
          ("connectorPortTypeIsBusMouse", 7),
          ("connectorPortTypeIsDB9", 9),
          ("connectorPortTypeIsHPHIL", 6),
          ("connectorPortTypeIsInfrared", 5),
          ("connectorPortTypeIsMicroDIN", 10),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsPC98", 12),
          ("connectorPortTypeIsPS2", 4),
          ("connectorPortTypeIsSerial", 3),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellKeyboardPortConnectorType(Integer32):
    """Custom type DellKeyboardPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsAccessBusUSB", 9),
          ("connectorPortTypeIsDB9", 8),
          ("connectorPortTypeIsHPHIL", 7),
          ("connectorPortTypeIsInfrared", 6),
          ("connectorPortTypeIsMicroDIN", 4),
          ("connectorPortTypeIsMiniDIN", 3),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsPC98", 10),
          ("connectorPortTypeIsPS2", 5),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellProcessorPortConnectorType(Integer32):
    """Custom type DellProcessorPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsAPiggyBackBoard", 5),
          ("connectorPortTypeIsDaughterdBoard", 3),
          ("connectorPortTypeIsLIFSocket", 7),
          ("connectorPortTypeIsNone", 6),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsP370", 10),
          ("connectorPortTypeIsSlot1", 8),
          ("connectorPortTypeIsSlot2", 9),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsZIFSocket", 4))
    )





class DellMemoryDevicePortConnectorType(Integer32):
    """Custom type DellMemoryDevicePortConnectorType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsAChip", 5),
          ("connectorPortTypeIsAProprietaryCard", 8),
          ("connectorPortTypeIsARowOfChips", 11),
          ("connectorPortTypeIsDIMM", 9),
          ("connectorPortTypeIsDIP", 6),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsRIMM", 12),
          ("connectorPortTypeIsSIMM", 3),
          ("connectorPortTypeIsSIP", 4),
          ("connectorPortTypeIsSODIMM", 13),
          ("connectorPortTypeIsSRIMM", 14),
          ("connectorPortTypeIsTSOP", 10),
          ("connectorPortTypeIsUnknown", 2),
          ("connectorPortTypeIsZIP", 7))
    )





class DellMonitorPortConnectorType(Integer32):
    """Custom type DellMonitorPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsDB15PinFemale", 4),
          ("connectorPortTypeIsDB15PinMale", 3),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellSCSIPortConnectorType(Integer32):
    """Custom type DellSCSIPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsDIN25pin", 3),
          ("connectorPortTypeIsDIN50pin", 4),
          ("connectorPortTypeIsDIN68pin", 5),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellParallelPortConnectorType(Integer32):
    """Custom type DellParallelPortConnectorType based on Integer32"""
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
        *(("connectorPortTypeIsCentronics", 5),
          ("connectorPortTypeIsCentronics14", 8),
          ("connectorPortTypeIsDB25PinFemale", 3),
          ("connectorPortTypeIsDB25PinMale", 4),
          ("connectorPortTypeIsDB36PinFemale", 9),
          ("connectorPortTypeIsMiniCentronics", 6),
          ("connectorPortTypeIsMiniCentronics20", 10),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsProprietary", 7),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellParallelPortConnectorPinout(Integer32):
    """Custom type DellParallelPortConnectorPinout based on Integer32"""
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
        *(("connectorPortPinoutIsIEEE1284", 5),
          ("connectorPortPinoutIsOther", 1),
          ("connectorPortPinoutIsPC98", 7),
          ("connectorPortPinoutIsPC98Full", 10),
          ("connectorPortPinoutIsPC98Hireso", 8),
          ("connectorPortPinoutIsPC98Note", 9),
          ("connectorPortPinoutIsPS2", 4),
          ("connectorPortPinoutIsProprietary", 6),
          ("connectorPortPinoutIsUnknown", 2),
          ("connectorPortPinoutIsXTorAT", 3))
    )





class DellParallelPortCapabilitiesUnique(Integer32):
    """Custom type DellParallelPortCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              30,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("atCapable", 2),
          ("atOrPS2OrECPOrEPPCapable", 30),
          ("ecpCapable", 8),
          ("eppCapable", 16),
          ("pc98Capable", 32),
          ("pc98HCapable", 128),
          ("pc98HiresoCapable", 64),
          ("ps2Capable", 4),
          ("unknown", 1))
    )





class DellSerialPortConnectorType(Integer32):
    """Custom type DellSerialPortConnectorType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsCirdin8Female", 11),
          ("connectorPortTypeIsCirdin8Male", 10),
          ("connectorPortTypeIsDB25PinFemale", 6),
          ("connectorPortTypeIsDB25PinMale", 5),
          ("connectorPortTypeIsDB9PinFemale", 4),
          ("connectorPortTypeIsDB9PinMale", 3),
          ("connectorPortTypeIsMiniCentronics14", 12),
          ("connectorPortTypeIsMiniCentronics26", 13),
          ("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsProprietary", 9),
          ("connectorPortTypeIsRJ11", 7),
          ("connectorPortTypeIsRJ45", 8),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellSerialPortCapabilitiesUnique(Integer32):
    """Custom type DellSerialPortCapabilitiesUnique based on Integer32"""
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
              128)
        )
    )
    namedValues = NamedValues(
        *(("c16450Capable", 8),
          ("c16550Capable", 16),
          ("c16550aCapable", 32),
          ("c8251Capable", 64),
          ("c8251FIFOCapable", 128),
          ("other", 1),
          ("unknown", 2),
          ("xtorATCapable", 4))
    )





class DellUSBPortConnectorType(Integer32):
    """Custom type DellUSBPortConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectorPortTypeIsOther", 1),
          ("connectorPortTypeIsUSB", 3),
          ("connectorPortTypeIsUnknown", 2))
    )





class DellPointingDeviceType(Integer32):
    """Custom type DellPointingDeviceType based on Integer32"""
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
        *(("deviceTypeIsAGlidePoint", 6),
          ("deviceTypeIsAMouse", 3),
          ("deviceTypeIsATouchPad", 7),
          ("deviceTypeIsATrackBall", 4),
          ("deviceTypeIsATrackPoint", 5),
          ("deviceTypeIsOther", 1),
          ("deviceTypeIsUnknown", 2))
    )





class DellProcessorDeviceType(Integer32):
    """Custom type DellProcessorDeviceType based on Integer32"""
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





class DellProcessorDeviceFamily(Integer32):
    """Custom type DellProcessorDeviceFamily based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("deviceFamilyIs80286", 4),
          ("deviceFamilyIs80287", 8),
          ("deviceFamilyIs80386", 5),
          ("deviceFamilyIs80387", 9),
          ("deviceFamilyIs80486", 6),
          ("deviceFamilyIs80487", 10),
          ("deviceFamilyIs8086", 3),
          ("deviceFamilyIs8087", 7),
          ("deviceFamilyIsCeleron", 15),
          ("deviceFamilyIsIntelXeon", 21),
          ("deviceFamilyIsOther", 1),
          ("deviceFamilyIsPentium", 11),
          ("deviceFamilyIsPentium2", 13),
          ("deviceFamilyIsPentium3", 17),
          ("deviceFamilyIsPentium3Step", 19),
          ("deviceFamilyIsPentium3Xeon", 18),
          ("deviceFamilyIsPentiumItanium", 20),
          ("deviceFamilyIsPentiumMMX", 14),
          ("deviceFamilyIsPentiumPro", 12),
          ("deviceFamilyIsUnknown", 2),
          ("deviceFamilyIsXeon", 16))
    )





class DellProcessorDeviceStatusState(Integer32):
    """Custom type DellProcessorDeviceStatusState based on Integer32"""
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





class DellProcessorUpgradeInformation(Integer32):
    """Custom type DellProcessorUpgradeInformation based on Integer32"""
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
        *(("processorUpgradeIsByDaughterBoard", 3),
          ("processorUpgradeIsByLIFSocket", 7),
          ("processorUpgradeIsByP370", 10),
          ("processorUpgradeIsByReplacement", 5),
          ("processorUpgradeIsBySlot1", 8),
          ("processorUpgradeIsBySlot2", 9),
          ("processorUpgradeIsByZIFSocket", 4),
          ("processorUpgradeIsNone", 6),
          ("processorUpgradeIsOther", 1),
          ("processorUpgradeIsUnknown", 2))
    )





class DellCacheDeviceType(Integer32):
    """Custom type DellCacheDeviceType based on Integer32"""
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
        *(("deviceTypeIsData", 4),
          ("deviceTypeIsInstruction", 3),
          ("deviceTypeIsOther", 1),
          ("deviceTypeIsUnified", 5),
          ("deviceTypeIsUnknown", 2))
    )





class DellCacheDeviceLevel(Integer32):
    """Custom type DellCacheDeviceLevel based on Integer32"""
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
        *(("deviceLevelIsOther", 1),
          ("deviceLevelIsPrimary", 3),
          ("deviceLevelIsSecondary", 4),
          ("deviceLevelIsTertiary", 5),
          ("deviceLevelIsUnknown", 2))
    )





class DellCacheDeviceWritePolicy(Integer32):
    """Custom type DellCacheDeviceWritePolicy based on Integer32"""
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
        *(("deviceWritePolicyIsDeterminedByIO", 6),
          ("deviceWritePolicyIsOther", 1),
          ("deviceWritePolicyIsUnknown", 2),
          ("deviceWritePolicyIsVariesByAddress", 5),
          ("deviceWritePolicyIsWriteBack", 3),
          ("deviceWritePolicyIsWriteThrough", 4))
    )





class DellCacheDeviceStatusState(Integer32):
    """Custom type DellCacheDeviceStatusState based on Integer32"""
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
        *(("biosDisabled", 5),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2),
          ("userDisabled", 4))
    )





class DellCacheDeviceECCType(Integer32):
    """Custom type DellCacheDeviceECCType based on Integer32"""
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
        *(("deviceECCTypeIsCRC", 7),
          ("deviceECCTypeIsMultiBitECC", 6),
          ("deviceECCTypeIsNone", 3),
          ("deviceECCTypeIsOther", 1),
          ("deviceECCTypeIsParity", 4),
          ("deviceECCTypeIsSingleBitECC", 5),
          ("deviceECCTypeIsUnknown", 2))
    )





class DellCacheDeviceAssociativity(Integer32):
    """Custom type DellCacheDeviceAssociativity based on Integer32"""
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
        *(("deviceAssociativityIsDirectMapped", 3),
          ("deviceAssociativityIsFourWaySetAssociative", 5),
          ("deviceAssociativityIsFullyAssociative", 6),
          ("deviceAssociativityIsOther", 1),
          ("deviceAssociativityIsTwoWaySetAssociative", 4),
          ("deviceAssociativityIsUnknown", 2))
    )





class DellCacheDeviceLocation(Integer32):
    """Custom type DellCacheDeviceLocation based on Integer32"""
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
        *(("deviceLocationIsExternal", 4),
          ("deviceLocationIsInternal", 3),
          ("deviceLocationIsOther", 1),
          ("deviceLocationIsUnknown", 2))
    )





class DellCacheDeviceSRAMType(Integer32):
    """Custom type DellCacheDeviceSRAMType based on Integer32"""
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
        *(("deviceSRAMTypeIsAsynchronous", 7),
          ("deviceSRAMTypeIsBurst", 4),
          ("deviceSRAMTypeIsNonBurst", 3),
          ("deviceSRAMTypeIsOther", 1),
          ("deviceSRAMTypeIsPipeBurst", 5),
          ("deviceSRAMTypeIsSynchronous", 6),
          ("deviceSRAMTypeIsUnknown", 2))
    )





class DellMemoryDeviceFormFactor(Integer32):
    """Custom type DellMemoryDeviceFormFactor based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("deviceFormFactorIsAChip", 5),
          ("deviceFormFactorIsAProprietaryCard", 8),
          ("deviceFormFactorIsARowOfChips", 11),
          ("deviceFormFactorIsDIMM", 9),
          ("deviceFormFactorIsDIP", 6),
          ("deviceFormFactorIsOther", 1),
          ("deviceFormFactorIsRIMM", 12),
          ("deviceFormFactorIsSIMM", 3),
          ("deviceFormFactorIsSIP", 4),
          ("deviceFormFactorIsSODIMM", 13),
          ("deviceFormFactorIsSRIMM", 14),
          ("deviceFormFactorIsTSOP", 10),
          ("deviceFormFactorIsUnknown", 2),
          ("deviceFormFactorIsZIP", 7))
    )





class DellMemoryDeviceType(Integer32):
    """Custom type DellMemoryDeviceType based on Integer32"""
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
        *(("deviceTypeIs3DRAM", 14),
          ("deviceTypeIsCDRAM", 13),
          ("deviceTypeIsDDR", 18),
          ("deviceTypeIsDRAM", 3),
          ("deviceTypeIsEDRAM", 4),
          ("deviceTypeIsEEPROM", 10),
          ("deviceTypeIsEPROM", 12),
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





class DellMemoryDeviceTypeDetails(Integer32):
    """Custom type DellMemoryDeviceTypeDetails based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("deviceTypeDeatilIsOther", 1),
          ("deviceTypeDetailIsCMOS", 8),
          ("deviceTypeDetailIsCacheDRAM", 11),
          ("deviceTypeDetailIsEDO", 9),
          ("deviceTypeDetailIsFastPaged", 3),
          ("deviceTypeDetailIsNonVolatile", 12),
          ("deviceTypeDetailIsPseudoStatic", 5),
          ("deviceTypeDetailIsRAMBUS", 6),
          ("deviceTypeDetailIsStaticColumn", 4),
          ("deviceTypeDetailIsSynchronous", 7),
          ("deviceTypeDetailIsUnknown", 2),
          ("deviceTypeDetailIsWindowDRAM", 10))
    )





class DellGenericDeviceType(Integer32):
    """Custom type DellGenericDeviceType based on Integer32"""
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
        *(("deviceTypeIsASCSIController", 4),
          ("deviceTypeIsASoundDevice", 7),
          ("deviceTypeIsAVideoDevice", 3),
          ("deviceTypeIsAnEthernetDevice", 5),
          ("deviceTypeIsOther", 1),
          ("deviceTypeIsTokenRingDevice", 6),
          ("deviceTypeIsUnknown", 2))
    )





class DellSystemSlotStateCapabilities(Integer32):
    """Custom type DellSystemSlotStateCapabilities based on Integer32"""
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





class DellSystemSlotStateSettings(Integer32):
    """Custom type DellSystemSlotStateSettings based on Integer32"""
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





class DellSystemSlotType(Integer32):
    """Custom type DellSystemSlotType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("systemSlotIsAGP", 15),
          ("systemSlotIsAGPx2", 16),
          ("systemSlotIsAGPx4", 17),
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
          ("systemSlotIsPCMCIA", 7),
          ("systemSlotIsProcessorCard", 10),
          ("systemSlotIsProprietary", 9),
          ("systemSlotIsProprietaryMemory", 11),
          ("systemSlotIsUnknown", 2),
          ("systemSlotIsVLVESA", 8))
    )





class DellSystemSlotUsage(Integer32):
    """Custom type DellSystemSlotUsage based on Integer32"""
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





class DellSystemSlotLength(Integer32):
    """Custom type DellSystemSlotLength based on Integer32"""
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
        *(("systemSlotLengthIsLong", 4),
          ("systemSlotLengthIsOther", 1),
          ("systemSlotLengthIsShort", 3),
          ("systemSlotLengthIsUnknown", 2))
    )





class DellSystemSlotCategory(Integer32):
    """Custom type DellSystemSlotCategory based on Integer32"""
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





class DellSystemSlotHotPlugBusWidth(Integer32):
    """Custom type DellSystemSlotHotPlugBusWidth based on Integer32"""
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
        *(("busWidthIs128bits", 7),
          ("busWidthIs16bits", 4),
          ("busWidthIs32bits", 5),
          ("busWidthIs64bits", 6),
          ("busWidthIs8bits", 3),
          ("busWidthIsOther", 1),
          ("busWidthIsUnknown", 2))
    )





class DellPhysicalMemoryArrayLocation(Integer32):
    """Custom type DellPhysicalMemoryArrayLocation based on Integer32"""
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
        *(("memoryArrayLocationIsEISA", 5),
          ("memoryArrayLocationIsISA", 4),
          ("memoryArrayLocationIsMCA", 7),
          ("memoryArrayLocationIsNUBUS", 10),
          ("memoryArrayLocationIsOther", 1),
          ("memoryArrayLocationIsPC98C20", 11),
          ("memoryArrayLocationIsPC98C24", 12),
          ("memoryArrayLocationIsPC98Card", 15),
          ("memoryArrayLocationIsPC98E", 13),
          ("memoryArrayLocationIsPC98LocalBus", 14),
          ("memoryArrayLocationIsPCI", 6),
          ("memoryArrayLocationIsPCMCIA", 8),
          ("memoryArrayLocationIsProprietary", 9),
          ("memoryArrayLocationIsSystemOrMotherboard", 3),
          ("memoryArrayLocationIsUnknown", 2))
    )





class DellPhysicalMemoryArrayUse(Integer32):
    """Custom type DellPhysicalMemoryArrayUse based on Integer32"""
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
        *(("memoryArrayUseIsCacheMemory", 7),
          ("memoryArrayUseIsFLASHMemory", 5),
          ("memoryArrayUseIsNonVolatileRAMMemory", 6),
          ("memoryArrayUseIsOther", 1),
          ("memoryArrayUseIsSystemMemory", 3),
          ("memoryArrayUseIsUnknown", 2),
          ("memoryArrayUseIsVideoMemory", 4))
    )





class DellPhysicalMemoryArrayECCType(Integer32):
    """Custom type DellPhysicalMemoryArrayECCType based on Integer32"""
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
        *(("memoryArrayECCTypeIsCRC", 7),
          ("memoryArrayECCTypeIsMultiBitECC", 6),
          ("memoryArrayECCTypeIsNone", 3),
          ("memoryArrayECCTypeIsOther", 1),
          ("memoryArrayECCTypeIsParity", 4),
          ("memoryArrayECCTypeIsSingleBitECC", 5),
          ("memoryArrayECCTypeIsUnknown", 2))
    )





class DellSpeakerControlCapabilitiesUnique(Integer32):
    """Custom type DellSpeakerControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("allVolumeCapable", 30),
          ("enableCapable", 2),
          ("highCapable", 16),
          ("lowCapable", 4),
          ("mediumCapable", 8),
          ("unknown", 1))
    )





class DellSpeakerControlSettingsUnique(Integer32):
    """Custom type DellSpeakerControlSettingsUnique based on Integer32"""
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
        *(("enabled", 2),
          ("high", 16),
          ("low", 4),
          ("medium", 8),
          ("unknown", 1))
    )





class DellNIFwakeonLanControlCapabilitiesUnique(Integer32):
    """Custom type DellNIFwakeonLanControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              14)
        )
    )
    namedValues = NamedValues(
        *(("addInCardCapable", 4),
          ("bothCapable", 14),
          ("enableCapable", 2),
          ("onBoardCapable", 8),
          ("unknown", 1))
    )





class DellNIFwakeonLanControlSettingsUnique(Integer32):
    """Custom type DellNIFwakeonLanControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("addInCard", 4),
          ("addInCardOrOnBoard", 12),
          ("enabled", 2),
          ("onBoard", 8),
          ("unknown", 1))
    )





class DellBootSequenceControlCapabilitiesUnique(Integer32):
    """Custom type DellBootSequenceControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("allFirstCapable", 30),
          ("bootFromCDROMFirstCapable", 16),
          ("bootFromDeviceListCapable", 8),
          ("bootFromDisketteFirstCapable", 2),
          ("bootFromDisketteORHardDriveFirstCapable", 6),
          ("bootFromhardDriveFirstCapable", 4),
          ("bootSequenceUnknown", 1))
    )





class DellBootSequenceControlSettingsUnique(Integer32):
    """Custom type DellBootSequenceControlSettingsUnique based on Integer32"""
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
        *(("bootFromCDROMFirst", 16),
          ("bootFromDeviceList", 8),
          ("bootFromDisketteFirst", 2),
          ("bootFromHardDriveFirst", 4),
          ("bootSequenceUnknown", 1))
    )





class DellBIOSPasswordControlCapabilitiesUnique(Integer32):
    """Custom type DellBIOSPasswordControlCapabilitiesUnique based on Integer32"""
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
        *(("passwordControlCapabilitiesUnknown", 1),
          ("passwordControlEnableANDJumperDisableCapable", 6),
          ("passwordControlEnableCapable", 2),
          ("passwordControlJumperDisableCapable", 4))
    )





class DellBIOSPasswordControlSettingsUnique(Integer32):
    """Custom type DellBIOSPasswordControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("passwordControlEnabled", 2),
          ("passwordControlJumperDisabled", 4),
          ("passwordControlSettingsUnknown", 1))
    )





class DellParallelPortControlCapabilitiesUnique(Integer32):
    """Custom type DellParallelPortControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18,
              30)
        )
    )
    namedValues = NamedValues(
        *(("allParallelPortCapable", 30),
          ("enableCapable", 2),
          ("lpt1Capable", 4),
          ("lpt1andEnableCapable", 6),
          ("lpt2Capable", 8),
          ("lpt2andEnableCapable", 10),
          ("lpt3Capable", 16),
          ("lpt3andEnableCapable", 18),
          ("unknown", 1))
    )





class DellParallelPortControlSettingsUnique(Integer32):
    """Custom type DellParallelPortControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("lpt1", 4),
          ("lpt1Enabled", 6),
          ("lpt2", 8),
          ("lpt2Enabled", 10),
          ("lpt3", 16),
          ("lpt3Enabled", 18),
          ("unknown", 1))
    )





class DellParallelPortControlModeCapabilitiesUnique(Integer32):
    """Custom type DellParallelPortControlModeCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("allModeCapable", 30),
          ("atAndPS2Capable", 6),
          ("atCapable", 2),
          ("ecpCapable", 8),
          ("eppCapable", 16),
          ("ps2Capable", 4),
          ("unknown", 1))
    )





class DellParallelPortControlModeSettingsUnique(Integer32):
    """Custom type DellParallelPortControlModeSettingsUnique based on Integer32"""
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
        *(("atModeEnabled", 2),
          ("ecpModeEnabled", 8),
          ("eppModeEnabled", 16),
          ("ps2ModeEnabled", 4),
          ("unknown", 1))
    )





class DellSerialPortControlCapabilitiesUnique(Integer32):
    """Custom type DellSerialPortControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18,
              32,
              34,
              64,
              86,
              106,
              126)
        )
    )
    namedValues = NamedValues(
        *(("allcomCapable", 126),
          ("autoConfigCapable", 64),
          ("com1Capable", 4),
          ("com1OrCom3CapableAndAutoConfigCapable", 86),
          ("com2Capable", 8),
          ("com2OrCom4CapableAndAutoConfigCapable", 106),
          ("com3Capable", 16),
          ("com4Capable", 32),
          ("enableAndCom1Capable", 6),
          ("enableAndCom2Capable", 10),
          ("enableAndCom3Capable", 18),
          ("enableAndCom4Capable", 34),
          ("enableCapable", 2),
          ("unknown", 1))
    )





class DellSerialPortControlSettingsUnique(Integer32):
    """Custom type DellSerialPortControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              16,
              18,
              32,
              34,
              64,
              66)
        )
    )
    namedValues = NamedValues(
        *(("com1", 4),
          ("com1Enabled", 6),
          ("com2", 8),
          ("com2Enabled", 10),
          ("com3", 16),
          ("com3Enabled", 18),
          ("com4", 32),
          ("com4Enabled", 34),
          ("comPortsAutoConfig", 64),
          ("enabled", 2),
          ("enabledAndAutoConfig", 66),
          ("unknown", 1))
    )





class DellideControlCapabilitiesUnique(Integer32):
    """Custom type DellideControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ideControlAutoConfigOrEnableCapable", 2),
          ("unknown", 1))
    )





class DellideControlSettingsUnique(Integer32):
    """Custom type DellideControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ideControlAutoConfigEnabledOrEnabled", 2),
          ("unknown", 1))
    )





class DellDisketteControlCapabilitiesUnique(Integer32):
    """Custom type DellDisketteControlCapabilitiesUnique based on Integer32"""
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
        *(("disketteAutoConfigOrEnableCapable", 2),
          ("disketteAutoConfigOrEnableCapableandReadOnlyCapable", 6),
          ("disketteReadOnlyCapable", 4),
          ("unknown", 1))
    )





class DellDisketteControlSettingsUnique(Integer32):
    """Custom type DellDisketteControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disketteAutoConfigEnabledOrEnabled", 2),
          ("disketteisReadOnly", 4),
          ("unknown", 1))
    )





class DellNetworkInterfaceControlCapabilitiesUnique(Integer32):
    """Custom type DellNetworkInterfaceControlCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enableCapable", 2),
          ("enableWithoutPXECapable", 4),
          ("unknown", 1))
    )





class DellNetworkInterfaceControlSettingsUnique(Integer32):
    """Custom type DellNetworkInterfaceControlSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("enabledWithoutPXE", 4),
          ("unknown", 1))
    )





class DellLocalResponseAgentCapabilitiesUnique(Integer32):
    """Custom type DellLocalResponseAgentCapabilitiesUnique based on Integer32"""
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
              256,
              383)
        )
    )
    namedValues = NamedValues(
        *(("broadcastMessageCapable", 4),
          ("consoleAlertCapable", 2),
          ("executeApplicationCapable", 256),
          ("lraFullyCapable", 383),
          ("osShutDownCapable", 8),
          ("powerCycleCapable", 32),
          ("powerOFFCapable", 64),
          ("rebootCapable", 16),
          ("speakerControlCapable", 1))
    )





class DellLRAThermalShutdownCapabilitiesUnique(Integer32):
    """Custom type DellLRAThermalShutdownCapabilitiesUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              14)
        )
    )
    namedValues = NamedValues(
        *(("enableCapable", 2),
          ("enableOnFailureCapable", 10),
          ("enableOnWarningCapable", 6),
          ("enableOnWarningOrFailureCapable", 14),
          ("failureCapable", 8),
          ("unknownCapabilities", 1),
          ("warningCapable", 4))
    )





class DellLRAThermalShutdownStateSettingsUnique(Integer32):
    """Custom type DellLRAThermalShutdownStateSettingsUnique based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("activatedOnFailure", 10),
          ("activatedOnWarning", 6),
          ("unknown", 1))
    )





class DellLocalResponseAgentSettingsUnique(Integer32):
    """Custom type DellLocalResponseAgentSettingsUnique based on Integer32"""
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
              256,
              511)
        )
    )
    namedValues = NamedValues(
        *(("allLRASettingsUnique", 511),
          ("broadcastMessage", 4),
          ("consoleAlert", 2),
          ("executeApplication", 256),
          ("osShutDown", 8),
          ("powerCycle", 32),
          ("powerOFF", 64),
          ("reboot", 16),
          ("speakerControl", 1))
    )





class DellCooOwnershipCodes(Integer32):
    """Custom type DellCooOwnershipCodes based on Integer32"""
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
        *(("leased", 4),
          ("offOfLease", 6),
          ("other", 1),
          ("owned", 3),
          ("rented", 5),
          ("transfer", 7),
          ("unknown", 2))
    )





class DellCooHourDayDurationType(Integer32):
    """Custom type DellCooHourDayDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("days", 3),
          ("hours", 2),
          ("unknown", 1))
    )





class DellCooDayMonthDurationType(Integer32):
    """Custom type DellCooDayMonthDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("days", 3),
          ("months", 4),
          ("unknown", 1))
    )





class DellCooMonthYearDurationType(Integer32):
    """Custom type DellCooMonthYearDurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("months", 4),
          ("unknown", 1),
          ("years", 5))
    )





class DellRemoteAccessType(Integer32):
    """Custom type DellRemoteAccessType based on Integer32"""
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
        *(("remoteAccessTypeIsDRSC", 3),
          ("remoteAccessTypeIsDRSP", 4),
          ("remoteAccessTypeIsOther", 1),
          ("remoteAccessTypeIsUnknown", 2))
    )





class DellRemoteAccessControlCapabilities(Integer32):
    """Custom type DellRemoteAccessControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              62,
              64,
              126)
        )
    )
    namedValues = NamedValues(
        *(("allResetAndShutdownCapable", 126),
          ("allResetCapable", 62),
          ("defaultConfigResetCapable", 32),
          ("gracefulResetCapable", 16),
          ("hardResetCapable", 4),
          ("logResetCapable", 2),
          ("shutdownCapable", 64),
          ("softResetCapable", 8),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessControlSettings(Integer32):
    """Custom type DellRemoteAccessControlSettings based on Integer32"""
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
        *(("defaultConfigReset", 32),
          ("gracefulReset", 16),
          ("hardReset", 4),
          ("logReset", 2),
          ("shutdown", 64),
          ("softReset", 8),
          ("unknown", 1))
    )





class DellRemoteAccessMonitorCapabilities(Integer32):
    """Custom type DellRemoteAccessMonitorCapabilities based on Integer32"""
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
        *(("extPwrSupplyMonitorAlwaysEnabledCapable", 4),
          ("extPwrSupplyMonitorIfConnectedAndAlwaysEnabledCapable", 6),
          ("extPwrSupplyMonitorIfConnectedCapable", 2),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessMonitorSettings(Integer32):
    """Custom type DellRemoteAccessMonitorSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("extPwrSupplyMonitorAlwaysEnabledEnabled", 4),
          ("extPwrSupplyMonitorIfConnectedEnabled", 2),
          ("unknown", 1))
    )





class DellRemoteAccessLANCapabilities(Integer32):
    """Custom type DellRemoteAccessLANCapabilities based on Integer32"""
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
        *(("nicAndNicDHCPCapable", 6),
          ("nicCapable", 2),
          ("nicDHCPCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessLANSettings(Integer32):
    """Custom type DellRemoteAccessLANSettings based on Integer32"""
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
        *(("nicAndNicDHCPEnabled", 6),
          ("nicDHCPEnabled", 4),
          ("nicEnabled", 2),
          ("unknown", 1))
    )





class DellRemoteAccessHostCapabilities(Integer32):
    """Custom type DellRemoteAccessHostCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("smtpEmailAndTftpRemoteFloppyAndFwUpdateCapable", 14),
          ("smtpEmailAndTftpRemoteFloppyCapable", 6),
          ("smtpEmailAndTftpRemoteFwUpdateCapable", 10),
          ("smtpEmailCapable", 2),
          ("tftpRemoteFloppyAndFwUpdateCapable", 12),
          ("tftpRemoteFloppyCapable", 4),
          ("tftpRemoteFwUpdateCapable", 8),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessHostSettings(Integer32):
    """Custom type DellRemoteAccessHostSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("smtpEmailAndTftpRemoteFloppyAndFwUpdateEnabled", 14),
          ("smtpEmailAndTftpRemoteFloppyEnabled", 6),
          ("smtpEmailAndTftpRemoteFwUpdateEnabled", 10),
          ("smtpEmailEnabled", 2),
          ("tftpRemoteFloppyAndFwUpdateEnabled", 12),
          ("tftpRemoteFloppyEnabled", 4),
          ("tftpRemoteFwUpdateEnabled", 8),
          ("unknown", 1))
    )





class DellRemoteAccessOutOfBandSNMPCapabilities(Integer32):
    """Custom type DellRemoteAccessOutOfBandSNMPCapabilities based on Integer32"""
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
        *(("oobSNMPAgentAndTrapsCapable", 6),
          ("oobSNMPAgentCapable", 2),
          ("oobSNMPTrapsCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteAccessOutOfBandSNMPSettings(Integer32):
    """Custom type DellRemoteAccessOutOfBandSNMPSettings based on Integer32"""
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
        *(("oobSNMPAgentAndTrapsEnabled", 6),
          ("oobSNMPAgentEnabled", 2),
          ("oobSNMPTrapsEnabled", 4),
          ("unknown", 1))
    )





class DellRemoteUserAdminStateCapabilities(Integer32):
    """Custom type DellRemoteUserAdminStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              24,
              32,
              56,
              64,
              120)
        )
    )
    namedValues = NamedValues(
        *(("alphaPagerCapable", 16),
          ("emailCapable", 32),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("numericPagerAlphaPagerAndEmailCapable", 56),
          ("numericPagerAlphaPagerEmailAndPrivilegeCapable", 120),
          ("numericPagerAndAlphaPagerCapable", 24),
          ("numericPagerCapable", 8),
          ("privilegeCapable", 64),
          ("unknownCapabilities", 1))
    )





class DellRemoteUserAdminStateSettings(Integer32):
    """Custom type DellRemoteUserAdminStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18,
              26,
              32,
              34,
              42,
              50,
              58)
        )
    )
    namedValues = NamedValues(
        *(("alphaPagerEnabled", 16),
          ("emailEnabled", 32),
          ("enabled", 2),
          ("enabledAndAlphaPagerAndEmailEnabled", 50),
          ("enabledAndAlphaPagerEnabled", 18),
          ("enabledAndEmailEnabled", 34),
          ("enabledAndNumericPagerAlphaPagerAndEmailEnabled", 58),
          ("enabledAndNumericPagerAndAlphaPagerEnabled", 26),
          ("enabledAndNumericPagerAndEmailEnabled", 42),
          ("enabledAndNumericPagerEnabled", 10),
          ("notReady", 4),
          ("numericPagerEnabled", 8),
          ("unknown", 1))
    )





class DellRemoteUserAdminControlCapabilities(Integer32):
    """Custom type DellRemoteUserAdminControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              14)
        )
    )
    namedValues = NamedValues(
        *(("alphaPagerTestCapable", 4),
          ("emailTestCapable", 8),
          ("numericPagerTestAlphaPagerTestAndEmailTestCapable", 14),
          ("numericPagerTestAndAlphaPagerTestCapable", 6),
          ("numericPagerTestCapable", 2),
          ("unknownCapabilities", 1))
    )





class DellRemoteUserAdminControlSettings(Integer32):
    """Custom type DellRemoteUserAdminControlSettings based on Integer32"""
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
        *(("alphaPagerTest", 4),
          ("emailTest", 8),
          ("numericPagerTest", 2),
          ("unknown", 1))
    )





class DellRemoteUserAdminAlphaProtocolType(Integer32):
    """Custom type DellRemoteUserAdminAlphaProtocolType based on Integer32"""
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
        *(("alpha7E0", 3),
          ("alpha8N1", 4),
          ("other", 1),
          ("unknown", 2))
    )





class DellRemoteUserAdminAlphaBaudType(Integer32):
    """Custom type DellRemoteUserAdminAlphaBaudType based on Integer32"""
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
        *(("alphaBaud1200", 4),
          ("alphaBaud300", 3),
          ("other", 1),
          ("unknown", 2))
    )





class DellRemoteSNMPTrapStateCapabilities(Integer32):
    """Custom type DellRemoteSNMPTrapStateCapabilities based on Integer32"""
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





class DellRemoteSNMPTrapStateSettings(Integer32):
    """Custom type DellRemoteSNMPTrapStateSettings based on Integer32"""
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





class DellRemoteSNMPTrapControlCapabilities(Integer32):
    """Custom type DellRemoteSNMPTrapControlCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapTestCapable", 2),
          ("unknownCapabilities", 1))
    )





class DellRemoteSNMPTrapControlSettings(Integer32):
    """Custom type DellRemoteSNMPTrapControlSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapTest", 2),
          ("unknown", 1))
    )





class DellRemoteDialUpStateCapabilities(Integer32):
    """Custom type DellRemoteDialUpStateCapabilities based on Integer32"""
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
              120,
              128,
              248,
              256,
              504)
        )
    )
    namedValues = NamedValues(
        *(("dialInAndOutAndDialInDHCPAndAllAuthCapable", 504),
          ("dialInAndOutAndDialInDHCPAndAuthAnyAndEncryptedCapable", 248),
          ("dialInAndOutAndDialInDHCPAndAuthAnyCapable", 120),
          ("dialInAuthAnyCapable", 64),
          ("dialInAuthEncryptedCapable", 128),
          ("dialInAuthMschapCapable", 256),
          ("dialInCapable", 8),
          ("dialInDHCPCapable", 32),
          ("dialOutCapable", 16),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteDialUpStateSettings(Integer32):
    """Custom type DellRemoteDialUpStateSettings based on Integer32"""
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
              90,
              122,
              128,
              154,
              186,
              256,
              282,
              314)
        )
    )
    namedValues = NamedValues(
        *(("dialInAuthAnyEnabled", 64),
          ("dialInAuthEncryptedEnabled", 128),
          ("dialInAuthMschapEnabled", 256),
          ("dialInDHCPEnabled", 32),
          ("dialInEnabled", 8),
          ("dialOutEnabled", 16),
          ("enabled", 2),
          ("enabledDialInAndOutAndDialInAuthAnyEnabled", 90),
          ("enabledDialInAndOutAndDialInAuthEncryptedEnabled", 154),
          ("enabledDialInAndOutAndDialInAuthMschapEnabled", 282),
          ("enabledDialInAndOutAndDialInDHCPAndAuthAnyEnabled", 122),
          ("enabledDialInAndOutAndDialInDHCPAndAuthEncryptedEnabled", 186),
          ("enabledDialInAndOutAndDialInDHCPAndAuthMschapEnabled", 314),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellRemoteDialUpModemDialType(Integer32):
    """Custom type DellRemoteDialUpModemDialType based on Integer32"""
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
        *(("remoteDialUpIsOther", 1),
          ("remoteDialUpIsPulse", 4),
          ("remoteDialUpIsTone", 3),
          ("remoteDialUpIsUnknown", 2))
    )





class DellRemoteUserDialInStateCapabilities(Integer32):
    """Custom type DellRemoteUserDialInStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18,
              24,
              26)
        )
    )
    namedValues = NamedValues(
        *(("dialInCallbackPresetNumberAndUserSpecifiedCapable", 24),
          ("dialInCallbackPresetNumberCapable", 8),
          ("dialInCallbackUserSpecifiedCapable", 16),
          ("enableAndDialInCallbackPresetNumberAndUserSpecifiedCapable", 26),
          ("enableAndDialInCallbackPresetNumberCapable", 10),
          ("enableAndDialInCallbackUserSpecifiedCapable", 18),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteUserDialInStateSettings(Integer32):
    """Custom type DellRemoteUserDialInStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18)
        )
    )
    namedValues = NamedValues(
        *(("dialInCallbackPresetNumberEnabled", 8),
          ("dialInCallbackUserSpecifiedEnabled", 16),
          ("enabled", 2),
          ("enabledAndDialInCallbackPresetNumberEnabled", 10),
          ("enabledAndDialInCallbackUserSpecifiedEnabled", 18),
          ("notReady", 4),
          ("unknown", 1))
    )





class DellRemoteDialOutStateCapabilities(Integer32):
    """Custom type DellRemoteDialOutStateCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              24,
              32,
              40,
              48,
              56)
        )
    )
    namedValues = NamedValues(
        *(("dialOutPPPAuthAnyAndEncryptedCapable", 24),
          ("dialOutPPPAuthAnyAndMschapCapable", 40),
          ("dialOutPPPAuthAnyCapable", 8),
          ("dialOutPPPAuthAnyEncryptedAndMschapCapable", 56),
          ("dialOutPPPAuthEncryptedAndMschapCapable", 48),
          ("dialOutPPPAuthEncryptedCapable", 16),
          ("dialOutPPPAuthMschapCapable", 32),
          ("enableCapable", 2),
          ("notReadyCapable", 4),
          ("unknownCapabilities", 1))
    )





class DellRemoteDialOutStateSettings(Integer32):
    """Custom type DellRemoteDialOutStateSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              18,
              32,
              34)
        )
    )
    namedValues = NamedValues(
        *(("dialOutPPPAuthAnyEnabled", 8),
          ("dialOutPPPAuthEncryptedEnabled", 16),
          ("dialOutPPPAuthMschapEnabled", 32),
          ("enabled", 2),
          ("enabledAnddialOutPPPAuthAnyEnabled", 10),
          ("enabledAnddialOutPPPAuthEncryptedEnabled", 18),
          ("enabledAnddialOutPPPAuthMschapEnabled", 34),
          ("notReady", 4),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_BaseboardGroup_ObjectIdentity = ObjectIdentity
baseboardGroup = _BaseboardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1)
)
_MIBVersionGroup_ObjectIdentity = ObjectIdentity
mIBVersionGroup = _MIBVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1)
)
_MIBMajorVersionNumber_Type = DellUnsigned8BitRange
_MIBMajorVersionNumber_Object = MibScalar
mIBMajorVersionNumber = _MIBMajorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1, 1),
    _MIBMajorVersionNumber_Type()
)
mIBMajorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMajorVersionNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    mIBMajorVersionNumber.setDescription("""\
0001.0001 This attribute defines the major version number of the Dell
Enterprise Server Group MIB (Management Information Base).
""")
_MIBMinorVersionNumber_Type = DellUnsigned8BitRange
_MIBMinorVersionNumber_Object = MibScalar
mIBMinorVersionNumber = _MIBMinorVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1, 2),
    _MIBMinorVersionNumber_Type()
)
mIBMinorVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIBMinorVersionNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    mIBMinorVersionNumber.setDescription("""\
0001.0002 This attribute defines the minor version number of the Dell
Enterprise Server Group MIB (Management Information Base).
""")
_SystemManagementSoftwareGroup_ObjectIdentity = ObjectIdentity
systemManagementSoftwareGroup = _SystemManagementSoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100)
)
_SystemManagementSoftwareName_Type = DellString
_SystemManagementSoftwareName_Object = MibScalar
systemManagementSoftwareName = _SystemManagementSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 1),
    _SystemManagementSoftwareName_Type()
)
systemManagementSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwareName.setDescription("""\
0100.0001 This attribute defines the Dell Systems Management Software product
name.
""")
_SystemManagementSoftwareVersionNumberName_Type = DellString
_SystemManagementSoftwareVersionNumberName_Object = MibScalar
systemManagementSoftwareVersionNumberName = _SystemManagementSoftwareVersionNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 2),
    _SystemManagementSoftwareVersionNumberName_Type()
)
systemManagementSoftwareVersionNumberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareVersionNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwareVersionNumberName.setDescription("""\
0100.0002 This attribute defines the version number of the Dell Systems
Management Software that instruments this component.
""")
_SystemManagementSoftwareBuildNumber_Type = DellUnsigned16BitRange
_SystemManagementSoftwareBuildNumber_Object = MibScalar
systemManagementSoftwareBuildNumber = _SystemManagementSoftwareBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 3),
    _SystemManagementSoftwareBuildNumber_Type()
)
systemManagementSoftwareBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareBuildNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwareBuildNumber.setDescription("""\
0100.0003 This attribute defines the build number of the Dell Systems
Management Software that instruments this component.
""")
_SystemManagementSoftwareDescriptionName_Type = DellString
_SystemManagementSoftwareDescriptionName_Object = MibScalar
systemManagementSoftwareDescriptionName = _SystemManagementSoftwareDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 4),
    _SystemManagementSoftwareDescriptionName_Type()
)
systemManagementSoftwareDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwareDescriptionName.setDescription("""\
0100.0004 This attribute defines the systems management software component
description name.
""")
_SystemManagementSoftwareSupportedProtocol_Type = SMSSupportedTypes
_SystemManagementSoftwareSupportedProtocol_Object = MibScalar
systemManagementSoftwareSupportedProtocol = _SystemManagementSoftwareSupportedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 5),
    _SystemManagementSoftwareSupportedProtocol_Type()
)
systemManagementSoftwareSupportedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareSupportedProtocol.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwareSupportedProtocol.setDescription("""\
0100.0005 This attribute defines the protocols supported by the systems
management software.
""")
_SystemManagementSoftwarePreferredProtocol_Type = SMSSupportedTypes
_SystemManagementSoftwarePreferredProtocol_Object = MibScalar
systemManagementSoftwarePreferredProtocol = _SystemManagementSoftwarePreferredProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 6),
    _SystemManagementSoftwarePreferredProtocol_Type()
)
systemManagementSoftwarePreferredProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwarePreferredProtocol.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwarePreferredProtocol.setDescription("""\
0100.0006 This attribute defines the preferred protocol for the systems
management software.
""")
_SystemManagementSoftwareUpdateLevelName_Type = DellString
_SystemManagementSoftwareUpdateLevelName_Object = MibScalar
systemManagementSoftwareUpdateLevelName = _SystemManagementSoftwareUpdateLevelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 100, 7),
    _SystemManagementSoftwareUpdateLevelName_Type()
)
systemManagementSoftwareUpdateLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManagementSoftwareUpdateLevelName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemManagementSoftwareUpdateLevelName.setDescription("""\
0100.0007 This attribute defines the update level of the system management
software.
""")
_SystemStateGroup_ObjectIdentity = ObjectIdentity
systemStateGroup = _SystemStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200)
)
_SystemStateTable_Object = MibTable
systemStateTable = _SystemStateTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10)
)
if mibBuilder.loadTexts:
    systemStateTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateTable.setDescription("""\
0200.0010 This Group defines the Dell System State Table.
""")
_SystemStateTableEntry_Object = MibTableRow
systemStateTableEntry = _SystemStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1)
)
systemStateTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemStatechassisIndex"),
)
if mibBuilder.loadTexts:
    systemStateTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateTableEntry.setDescription("""\
0200.0010.0001 This Group defines the Dell System State Table Entry.
""")
_SystemStatechassisIndex_Type = DellObjectRange
_SystemStatechassisIndex_Object = MibTableColumn
systemStatechassisIndex = _SystemStatechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 1),
    _SystemStatechassisIndex_Type()
)
systemStatechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatechassisIndex.setDescription("""\
0200.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemStateGlobalSystemStatus_Type = DellStatus
_SystemStateGlobalSystemStatus_Object = MibTableColumn
systemStateGlobalSystemStatus = _SystemStateGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 2),
    _SystemStateGlobalSystemStatus_Type()
)
systemStateGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateGlobalSystemStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateGlobalSystemStatus.setDescription("""\
0200.0010.0001.0002 This attribute defines the global system status of all Dell
chassis being monitored by this instrumentation instance.
""")
_SystemStateChassisState_Type = DellStateSettings
_SystemStateChassisState_Object = MibTableColumn
systemStateChassisState = _SystemStateChassisState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 3),
    _SystemStateChassisState_Type()
)
systemStateChassisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisState.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateChassisState.setDescription("""\
0200.0010.0001.0003 This attribute defines the system state of this Dell
chassis.
""")
_SystemStateChassisStatus_Type = DellStatus
_SystemStateChassisStatus_Object = MibTableColumn
systemStateChassisStatus = _SystemStateChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 4),
    _SystemStateChassisStatus_Type()
)
systemStateChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateChassisStatus.setDescription("""\
0200.0010.0001.0004 This attribute defines the system status of this Dell
chassis.
""")


class _SystemStatePowerUnitStateDetails_Type(OctetString):
    """Custom type systemStatePowerUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStateDetails_Type.__name__ = "OctetString"
_SystemStatePowerUnitStateDetails_Object = MibTableColumn
systemStatePowerUnitStateDetails = _SystemStatePowerUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 5),
    _SystemStatePowerUnitStateDetails_Type()
)
systemStatePowerUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatePowerUnitStateDetails.setDescription("""\
0200.0010.0001.0005 This attribute defines the power unit state of all power
units in this Dell chassis. The results are returned as a binary octet string,
each byte of the octet string represents the state of the specific object. The
first byte returned represents the state of the first object, etc. The bytes
have the same definition type as DellStateSettings.
""")
_SystemStatePowerUnitStatusRedundancy_Type = DellStatusRedundancy
_SystemStatePowerUnitStatusRedundancy_Object = MibTableColumn
systemStatePowerUnitStatusRedundancy = _SystemStatePowerUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 6),
    _SystemStatePowerUnitStatusRedundancy_Type()
)
systemStatePowerUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusRedundancy.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusRedundancy.setDescription("""\
0200.0010.0001.0006 This attribute defines the system status of the power
unit(s) of this Dell chassis.
""")


class _SystemStatePowerUnitStatusDetails_Type(OctetString):
    """Custom type systemStatePowerUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStatePowerUnitStatusDetails_Object = MibTableColumn
systemStatePowerUnitStatusDetails = _SystemStatePowerUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 7),
    _SystemStatePowerUnitStatusDetails_Type()
)
systemStatePowerUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatePowerUnitStatusDetails.setDescription("""\
0200.0010.0001.0007 This attribute defines the power unit status of all power
units in this Dell chassis. The results are returned as a binary octet string,
each byte of the octet string represents the status of the specific object. The
first byte returned represents the status of the first object, etc. The bytes
have the same definition type as DellStatusRedundancy.
""")


class _SystemStatePowerSupplyStateDetails_Type(OctetString):
    """Custom type systemStatePowerSupplyStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerSupplyStateDetails_Type.__name__ = "OctetString"
_SystemStatePowerSupplyStateDetails_Object = MibTableColumn
systemStatePowerSupplyStateDetails = _SystemStatePowerSupplyStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 8),
    _SystemStatePowerSupplyStateDetails_Type()
)
systemStatePowerSupplyStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStateDetails.setDescription("""\
0200.0010.0001.0008 This attribute defines the power supply state of all power
supplies in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the state of the specific
object. The first byte returned represents the state of the first object, etc.
The bytes have the same definition type as DellStateSettings.
""")
_SystemStatePowerSupplyStatusCombined_Type = DellStatus
_SystemStatePowerSupplyStatusCombined_Object = MibTableColumn
systemStatePowerSupplyStatusCombined = _SystemStatePowerSupplyStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 9),
    _SystemStatePowerSupplyStatusCombined_Type()
)
systemStatePowerSupplyStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusCombined.setDescription("""\
0200.0010.0001.0009 This attribute defines the power supply status of all power
supplies in this Dell chassis. The result is returned as a combined status
value. The value has the same definition type as DellStatus.
""")


class _SystemStatePowerSupplyStatusDetails_Type(OctetString):
    """Custom type systemStatePowerSupplyStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatePowerSupplyStatusDetails_Type.__name__ = "OctetString"
_SystemStatePowerSupplyStatusDetails_Object = MibTableColumn
systemStatePowerSupplyStatusDetails = _SystemStatePowerSupplyStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 10),
    _SystemStatePowerSupplyStatusDetails_Type()
)
systemStatePowerSupplyStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStatePowerSupplyStatusDetails.setDescription("""\
0200.0010.0001.0010 This attribute defines the power supply status of all power
supplies in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the status of the specific
object. The first byte returned represents the status of the first object, etc.
The bytes have the same definition type as DellStatus.
""")


class _SystemStateVoltageStateDetails_Type(OctetString):
    """Custom type systemStateVoltageStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateVoltageStateDetails_Type.__name__ = "OctetString"
_SystemStateVoltageStateDetails_Object = MibTableColumn
systemStateVoltageStateDetails = _SystemStateVoltageStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 11),
    _SystemStateVoltageStateDetails_Type()
)
systemStateVoltageStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateVoltageStateDetails.setDescription("""\
0200.0010.0001.0011 This attribute defines the voltage state of all voltage
probes in this Dell chassis. The results are returned as a binary octet string,
each byte of the octet string represents the state of the specific object. The
first byte returned represents the state of the first object, etc. The bytes
have the same definition type as DellStateSettings.
""")
_SystemStateVoltageStatusCombined_Type = DellStatus
_SystemStateVoltageStatusCombined_Object = MibTableColumn
systemStateVoltageStatusCombined = _SystemStateVoltageStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 12),
    _SystemStateVoltageStatusCombined_Type()
)
systemStateVoltageStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateVoltageStatusCombined.setDescription("""\
0200.0010.0001.0012 This attribute defines the voltage status of all voltage
probes in this Dell chassis. The result is returned as a combined status value.
The value has the same definition type as DellStatus.
""")


class _SystemStateVoltageStatusDetails_Type(OctetString):
    """Custom type systemStateVoltageStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateVoltageStatusDetails_Type.__name__ = "OctetString"
_SystemStateVoltageStatusDetails_Object = MibTableColumn
systemStateVoltageStatusDetails = _SystemStateVoltageStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 13),
    _SystemStateVoltageStatusDetails_Type()
)
systemStateVoltageStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateVoltageStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateVoltageStatusDetails.setDescription("""\
0200.0010.0001.0013 This attribute defines the voltage status of all voltage
probes in this Dell chassis. The results are returned as a binary octet string,
each byte of the octet string represents the status of the specific object. The
first byte returned represents the status of the first object, etc. The bytes
have the same definition type as DellStatus.
""")


class _SystemStateAmperageStateDetails_Type(OctetString):
    """Custom type systemStateAmperageStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateAmperageStateDetails_Type.__name__ = "OctetString"
_SystemStateAmperageStateDetails_Object = MibTableColumn
systemStateAmperageStateDetails = _SystemStateAmperageStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 14),
    _SystemStateAmperageStateDetails_Type()
)
systemStateAmperageStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateAmperageStateDetails.setDescription("""\
0200.0010.0001.0014 This attribute defines the state of all current probes in
this Dell chassis. The results are returned as a binary octet string, each byte
of the octet string represents the state of the specific object. The first byte
returned represents the state of the first object, etc. The bytes have the same
definition type as DellStateSettings.
""")
_SystemStateAmperageStatusCombined_Type = DellStatus
_SystemStateAmperageStatusCombined_Object = MibTableColumn
systemStateAmperageStatusCombined = _SystemStateAmperageStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 15),
    _SystemStateAmperageStatusCombined_Type()
)
systemStateAmperageStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateAmperageStatusCombined.setDescription("""\
0200.0010.0001.0015 This attribute defines the amperage status of all amperage
probes in this Dell chassis. The result is returned as a combined status value.
The value has the same definition type as DellStatus.
""")


class _SystemStateAmperageStatusDetails_Type(OctetString):
    """Custom type systemStateAmperageStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateAmperageStatusDetails_Type.__name__ = "OctetString"
_SystemStateAmperageStatusDetails_Object = MibTableColumn
systemStateAmperageStatusDetails = _SystemStateAmperageStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 16),
    _SystemStateAmperageStatusDetails_Type()
)
systemStateAmperageStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateAmperageStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateAmperageStatusDetails.setDescription("""\
0200.0010.0001.0016 This attribute defines the status of all current probes in
this Dell chassis. The results are returned as a binary octet string, each byte
of the octet string represents the status of the specific object. The first
byte returned represents the status of the first object, etc. The bytes have
the same definition type as DellStatus.
""")


class _SystemStateCoolingUnitStateDetails_Type(OctetString):
    """Custom type systemStateCoolingUnitStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStateDetails_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStateDetails_Object = MibTableColumn
systemStateCoolingUnitStateDetails = _SystemStateCoolingUnitStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 17),
    _SystemStateCoolingUnitStateDetails_Type()
)
systemStateCoolingUnitStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStateDetails.setDescription("""\
0200.0010.0001.0017 This attribute defines the cooling unit state of all
cooling units in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the state of the specific
object. The first byte returned represents the state of the first object, etc.
The bytes have the same definition type as DellStateSettings.
""")
_SystemStateCoolingUnitStatusRedundancy_Type = DellStatusRedundancy
_SystemStateCoolingUnitStatusRedundancy_Object = MibTableColumn
systemStateCoolingUnitStatusRedundancy = _SystemStateCoolingUnitStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 18),
    _SystemStateCoolingUnitStatusRedundancy_Type()
)
systemStateCoolingUnitStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusRedundancy.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusRedundancy.setDescription("""\
0200.0010.0001.0018 This attribute defines the system status of the cooling
units in this Dell chassis. The returned value has the same definition type as
DellStatusRedundancy.
""")


class _SystemStateCoolingUnitStatusDetails_Type(OctetString):
    """Custom type systemStateCoolingUnitStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingUnitStatusDetails_Type.__name__ = "OctetString"
_SystemStateCoolingUnitStatusDetails_Object = MibTableColumn
systemStateCoolingUnitStatusDetails = _SystemStateCoolingUnitStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 19),
    _SystemStateCoolingUnitStatusDetails_Type()
)
systemStateCoolingUnitStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateCoolingUnitStatusDetails.setDescription("""\
0200.0010.0001.0019 This attribute defines the cooling unit status of all
cooling units in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the status of the specific
object. The first byte returned represents the status of the first object, etc.
The bytes have the same definition type as DellStatusRedundancy.
""")


class _SystemStateCoolingDeviceStateDetails_Type(OctetString):
    """Custom type systemStateCoolingDeviceStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingDeviceStateDetails_Type.__name__ = "OctetString"
_SystemStateCoolingDeviceStateDetails_Object = MibTableColumn
systemStateCoolingDeviceStateDetails = _SystemStateCoolingDeviceStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 20),
    _SystemStateCoolingDeviceStateDetails_Type()
)
systemStateCoolingDeviceStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStateDetails.setDescription("""\
0200.0010.0001.0020 This attribute defines the cooling device state of all
cooling devices in this Dell chassis. The results are returned as a binary
octet string, each byte of the octet string represents the state of the
specific object. The first byte returned represents the state of the first
object, etc. The bytes have the same definition type as DellStateSettings.
""")
_SystemStateCoolingDeviceStatusCombined_Type = DellStatus
_SystemStateCoolingDeviceStatusCombined_Object = MibTableColumn
systemStateCoolingDeviceStatusCombined = _SystemStateCoolingDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 21),
    _SystemStateCoolingDeviceStatusCombined_Type()
)
systemStateCoolingDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusCombined.setDescription("""\
0200.0010.0001.0021 This attribute defines the cooling device status of all
cooling devices in this Dell chassis. The result is returned as a combined
status value. The value has the same definition type as DellStatus.
""")


class _SystemStateCoolingDeviceStatusDetails_Type(OctetString):
    """Custom type systemStateCoolingDeviceStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateCoolingDeviceStatusDetails_Type.__name__ = "OctetString"
_SystemStateCoolingDeviceStatusDetails_Object = MibTableColumn
systemStateCoolingDeviceStatusDetails = _SystemStateCoolingDeviceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 22),
    _SystemStateCoolingDeviceStatusDetails_Type()
)
systemStateCoolingDeviceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateCoolingDeviceStatusDetails.setDescription("""\
0200.0010.0001.0022 This attribute defines the cooling device status of all
cooling devices in this Dell chassis. The results are returned as a binary
octet string, each byte of the octet string represents the status of the
specific object. The first byte returned represents the status of the first
object, etc. The bytes have the same definition type as DellStatus.
""")


class _SystemStateTemperatureStateDetails_Type(OctetString):
    """Custom type systemStateTemperatureStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStateDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStateDetails_Object = MibTableColumn
systemStateTemperatureStateDetails = _SystemStateTemperatureStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 23),
    _SystemStateTemperatureStateDetails_Type()
)
systemStateTemperatureStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateTemperatureStateDetails.setDescription("""\
0200.0010.0001.0023 This attribute defines the temperature probe state of all
temperature probes in this Dell chassis. The results are returned as a binary
octet string, each byte of the octet string represents the state of the
specific object. The first byte returned represents the state of the first
object, etc. The bytes have the same definition type as DellStateSettings.
""")
_SystemStateTemperatureStatusCombined_Type = DellStatus
_SystemStateTemperatureStatusCombined_Object = MibTableColumn
systemStateTemperatureStatusCombined = _SystemStateTemperatureStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 24),
    _SystemStateTemperatureStatusCombined_Type()
)
systemStateTemperatureStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusCombined.setDescription("""\
0200.0010.0001.0024 This attribute defines the temperature status of all
temperature probes in this Dell chassis. The result is returned as a combined
status value. The value has the same definition type as DellStatus.
""")


class _SystemStateTemperatureStatusDetails_Type(OctetString):
    """Custom type systemStateTemperatureStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateTemperatureStatusDetails_Type.__name__ = "OctetString"
_SystemStateTemperatureStatusDetails_Object = MibTableColumn
systemStateTemperatureStatusDetails = _SystemStateTemperatureStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 25),
    _SystemStateTemperatureStatusDetails_Type()
)
systemStateTemperatureStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateTemperatureStatusDetails.setDescription("""\
0200.0010.0001.0025 This attribute defines the temperature probe status of all
temperature probes in this Dell chassis. The results are returned as a binary
octet string, each byte of the octet string represents the status of the
specific object. The first byte returned represents the status of the first
object, etc. The bytes have the same definition type as DellStatus.
""")


class _SystemStateMemoryDeviceStateDetails_Type(OctetString):
    """Custom type systemStateMemoryDeviceStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateMemoryDeviceStateDetails_Type.__name__ = "OctetString"
_SystemStateMemoryDeviceStateDetails_Object = MibTableColumn
systemStateMemoryDeviceStateDetails = _SystemStateMemoryDeviceStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 26),
    _SystemStateMemoryDeviceStateDetails_Type()
)
systemStateMemoryDeviceStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStateDetails.setDescription("""\
0200.0010.0001.0026 This attribute defines the memory device state of all
memory devices in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the state of the specific
object. The first byte returned represents the state of the first object, etc.
The bytes have the same definition type as DellStateSettings.
""")
_SystemStateMemoryDeviceStatusCombined_Type = DellStatus
_SystemStateMemoryDeviceStatusCombined_Object = MibTableColumn
systemStateMemoryDeviceStatusCombined = _SystemStateMemoryDeviceStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 27),
    _SystemStateMemoryDeviceStatusCombined_Type()
)
systemStateMemoryDeviceStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusCombined.setDescription("""\
0200.0010.0001.0027 This attribute defines the memory device status of all
memory devices in this Dell chassis. The result is returned as a combined
status value. The value has the same definition type as DellStatus.
""")


class _SystemStateMemoryDeviceStatusDetails_Type(OctetString):
    """Custom type systemStateMemoryDeviceStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateMemoryDeviceStatusDetails_Type.__name__ = "OctetString"
_SystemStateMemoryDeviceStatusDetails_Object = MibTableColumn
systemStateMemoryDeviceStatusDetails = _SystemStateMemoryDeviceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 28),
    _SystemStateMemoryDeviceStatusDetails_Type()
)
systemStateMemoryDeviceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateMemoryDeviceStatusDetails.setDescription("""\
0200.0010.0001.0028 This attribute defines the memory device status of all
memory devices in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the status of the specific
object. The first byte returned represents the status of the first object, etc.
The bytes have the same definition type as DellStatus.
""")


class _SystemStateChassisIntrusionStateDetails_Type(OctetString):
    """Custom type systemStateChassisIntrusionStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateChassisIntrusionStateDetails_Type.__name__ = "OctetString"
_SystemStateChassisIntrusionStateDetails_Object = MibTableColumn
systemStateChassisIntrusionStateDetails = _SystemStateChassisIntrusionStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 29),
    _SystemStateChassisIntrusionStateDetails_Type()
)
systemStateChassisIntrusionStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStateDetails.setDescription("""\
0200.0010.0001.0029 This attribute defines the intrusion state of all intrusion
detection devices in this Dell chassis. The results are returned as a binary
octet string, each byte of the octet string represents the state of the
specific object. The first byte returned represents the state of the first
object, etc. The bytes have the same definition type as DellStateSettings.
""")
_SystemStateChassisIntrusionStatusCombined_Type = DellStatus
_SystemStateChassisIntrusionStatusCombined_Object = MibTableColumn
systemStateChassisIntrusionStatusCombined = _SystemStateChassisIntrusionStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 30),
    _SystemStateChassisIntrusionStatusCombined_Type()
)
systemStateChassisIntrusionStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusCombined.setDescription("""\
0200.0010.0001.0030 This attribute defines the intrusion reading of all
intrusion detection devices in this Dell chassis. The result is returned as a
combined status value. The value has the same definition type as DellStatus.
""")


class _SystemStateChassisIntrusionStatusDetails_Type(OctetString):
    """Custom type systemStateChassisIntrusionStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateChassisIntrusionStatusDetails_Type.__name__ = "OctetString"
_SystemStateChassisIntrusionStatusDetails_Object = MibTableColumn
systemStateChassisIntrusionStatusDetails = _SystemStateChassisIntrusionStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 31),
    _SystemStateChassisIntrusionStatusDetails_Type()
)
systemStateChassisIntrusionStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateChassisIntrusionStatusDetails.setDescription("""\
0200.0010.0001.0031 This attribute defines the intrusion status of all
intrustion detection devices in this Dell chassis. The results are returned as
a binary octet string, each byte of the octet string represents the value of
the specific object. The first byte returned represents the value of the first
object, etc. The bytes have the same definition type as DellStatus.
""")


class _SystemStateACPowerSwitchStateDetails_Type(OctetString):
    """Custom type systemStateACPowerSwitchStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerSwitchStateDetails_Type.__name__ = "OctetString"
_SystemStateACPowerSwitchStateDetails_Object = MibTableColumn
systemStateACPowerSwitchStateDetails = _SystemStateACPowerSwitchStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 32),
    _SystemStateACPowerSwitchStateDetails_Type()
)
systemStateACPowerSwitchStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStateDetails.setDescription("""\
0200.0010.0001.00032 This attribute defines the individual state of all AC
power switches in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the state of the specific
object. The first byte returned represents the state of the first object, etc.
The bytes have the same definition type as DellStateSettings.
""")
_SystemStateACPowerSwitchStatusRedundancy_Type = DellStatusRedundancy
_SystemStateACPowerSwitchStatusRedundancy_Object = MibTableColumn
systemStateACPowerSwitchStatusRedundancy = _SystemStateACPowerSwitchStatusRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 33),
    _SystemStateACPowerSwitchStatusRedundancy_Type()
)
systemStateACPowerSwitchStatusRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusRedundancy.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusRedundancy.setDescription("""\
0200.0010.0001.0033 This attribute defines the overall redundancy status of the
AC power switch(es) in this Dell chassis.
""")


class _SystemStateACPowerSwitchStatusDetails_Type(OctetString):
    """Custom type systemStateACPowerSwitchStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerSwitchStatusDetails_Type.__name__ = "OctetString"
_SystemStateACPowerSwitchStatusDetails_Object = MibTableColumn
systemStateACPowerSwitchStatusDetails = _SystemStateACPowerSwitchStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 34),
    _SystemStateACPowerSwitchStatusDetails_Type()
)
systemStateACPowerSwitchStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateACPowerSwitchStatusDetails.setDescription("""\
0200.0010.0001.0034 This attribute defines the individual status of all AC
power switches in this Dell chassis. The results are returned as a binary octet
string, each byte of the octet string represents the status of the specific
object. The first byte returned represents the status of the first object, etc.
The bytes have the same definition type as DellStatusRedundancy.
""")


class _SystemStateACPowerCordStateDetails_Type(OctetString):
    """Custom type systemStateACPowerCordStateDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerCordStateDetails_Type.__name__ = "OctetString"
_SystemStateACPowerCordStateDetails_Object = MibTableColumn
systemStateACPowerCordStateDetails = _SystemStateACPowerCordStateDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 35),
    _SystemStateACPowerCordStateDetails_Type()
)
systemStateACPowerCordStateDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerCordStateDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateACPowerCordStateDetails.setDescription("""\
0200.0010.0001.0035 This attribute defines the individual state of all AC power
cords for any AC power switches in this Dell chassis. The results are returned
as a binary octet string, each byte of the octet string represents the state of
the specific object. The first byte returned represents the state of the first
object, etc. The bytes have the same definition type as DellStateSettings.
""")
_SystemStateACPowerCordStatusCombined_Type = DellStatus
_SystemStateACPowerCordStatusCombined_Object = MibTableColumn
systemStateACPowerCordStatusCombined = _SystemStateACPowerCordStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 36),
    _SystemStateACPowerCordStatusCombined_Type()
)
systemStateACPowerCordStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerCordStatusCombined.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateACPowerCordStatusCombined.setDescription("""\
0200.0010.0001.0036 This attribute defines the overall status of all AC power
cords for any AC power switches in this Dell chassis. The result is returned as
a combined status value. The value has the same definition type as DellStatus.
""")


class _SystemStateACPowerCordStatusDetails_Type(OctetString):
    """Custom type systemStateACPowerCordStatusDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStateACPowerCordStatusDetails_Type.__name__ = "OctetString"
_SystemStateACPowerCordStatusDetails_Object = MibTableColumn
systemStateACPowerCordStatusDetails = _SystemStateACPowerCordStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 200, 10, 1, 37),
    _SystemStateACPowerCordStatusDetails_Type()
)
systemStateACPowerCordStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStateACPowerCordStatusDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemStateACPowerCordStatusDetails.setDescription("""\
0200.0010.0001.0037 This attribute defines the individual status of all AC
power cords for any AC power switches in this Dell chassis. The results are
returned as a binary octet string, each byte of the octet string represents the
status of the specific object. The first byte returned represents the status of
the first object, etc. The bytes have the same definition type as DellStatus.
""")
_ChassisInformationGroup_ObjectIdentity = ObjectIdentity
chassisInformationGroup = _ChassisInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300)
)
_ChassisInformationTable_Object = MibTable
chassisInformationTable = _ChassisInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10)
)
if mibBuilder.loadTexts:
    chassisInformationTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisInformationTable.setDescription("""\
0300.0010 This Group defines the Dell Chassis Table.
""")
_ChassisInformationTableEntry_Object = MibTableRow
chassisInformationTableEntry = _ChassisInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1)
)
chassisInformationTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "chassisIndexChassisInformation"),
)
if mibBuilder.loadTexts:
    chassisInformationTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisInformationTableEntry.setDescription("""\
0300.0010.0001 This Group defines the Dell Chassis Table Entry.
""")
_ChassisIndexChassisInformation_Type = DellObjectRange
_ChassisIndexChassisInformation_Object = MibTableColumn
chassisIndexChassisInformation = _ChassisIndexChassisInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 1),
    _ChassisIndexChassisInformation_Type()
)
chassisIndexChassisInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIndexChassisInformation.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisIndexChassisInformation.setDescription("""\
0300.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_ChassisStateCapabilities_Type = DellStateCapabilities
_ChassisStateCapabilities_Object = MibTableColumn
chassisStateCapabilities = _ChassisStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 2),
    _ChassisStateCapabilities_Type()
)
chassisStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisStateCapabilities.setDescription("""\
0300.0010.0001.0002 This attribute defines the capabilities of the Dell
chassis.
""")
_ChassisStateSettings_Type = DellStateSettings
_ChassisStateSettings_Object = MibTableColumn
chassisStateSettings = _ChassisStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 3),
    _ChassisStateSettings_Type()
)
chassisStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisStateSettings.setDescription("""\
0300.0010.0001.0003 This attribute defines the state of this Dell chassis.
""")
_ChassisStatus_Type = DellStatus
_ChassisStatus_Object = MibTableColumn
chassisStatus = _ChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 4),
    _ChassisStatus_Type()
)
chassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisStatus.setDescription("""\
0300.0010.0001.0004 This attribute defines the status of the Dell chassis.
""")
_ChassisparentIndexReference_Type = DellObjectRange
_ChassisparentIndexReference_Object = MibTableColumn
chassisparentIndexReference = _ChassisparentIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 5),
    _ChassisparentIndexReference_Type()
)
chassisparentIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisparentIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisparentIndexReference.setDescription("""\
0300.0010.0001.0005 This attribute defines the index (one based) to the parent
Dell chassis of this chassis, if any.
""")
_ChassisType_Type = DellChassisType
_ChassisType_Object = MibTableColumn
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 6),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisType.setDescription("""\
0300.0010.0001.0006 This attribute defines the chassis type of the Dell
chassis.
""")
_ChassisName_Type = DellString
_ChassisName_Object = MibTableColumn
chassisName = _ChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 7),
    _ChassisName_Type()
)
chassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisName.setDescription("""\
0300.0010.0001.0007 This attribute defines the user assigned chassis name of
the Dell chassis.
""")
_ChassisManufacturerName_Type = DellString
_ChassisManufacturerName_Object = MibTableColumn
chassisManufacturerName = _ChassisManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 8),
    _ChassisManufacturerName_Type()
)
chassisManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisManufacturerName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisManufacturerName.setDescription("""\
0300.0010.0001.0008 This attribute defines the manufacturer's name of the Dell
chassis.
""")
_ChassisModelName_Type = DellString
_ChassisModelName_Object = MibTableColumn
chassisModelName = _ChassisModelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 9),
    _ChassisModelName_Type()
)
chassisModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModelName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisModelName.setDescription("""\
0300.0010.0001.0009 This attribute defines the system model type of the Dell
chassis.
""")


class _ChassisAssetTagName_Type(DisplayString):
    """Custom type chassisAssetTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ChassisAssetTagName_Type.__name__ = "DisplayString"
_ChassisAssetTagName_Object = MibTableColumn
chassisAssetTagName = _ChassisAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 10),
    _ChassisAssetTagName_Type()
)
chassisAssetTagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAssetTagName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisAssetTagName.setDescription("""\
0300.0010.0001.0010 This attribute defines the asset tag name of the Dell
chassis.
""")


class _ChassisServiceTagName_Type(DisplayString):
    """Custom type chassisServiceTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChassisServiceTagName_Type.__name__ = "DisplayString"
_ChassisServiceTagName_Object = MibTableColumn
chassisServiceTagName = _ChassisServiceTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 11),
    _ChassisServiceTagName_Type()
)
chassisServiceTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisServiceTagName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisServiceTagName.setDescription("""\
0300.0010.0001.0011 This attribute defines the service tag name of the Dell
chassis.
""")
_ChassisID_Type = DellUnsigned8BitRange
_ChassisID_Object = MibTableColumn
chassisID = _ChassisID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 12),
    _ChassisID_Type()
)
chassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisID.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisID.setDescription("""\
0300.0010.0001.0012 This attribute defines the BIOS Machine ID of the Dell
chassis.
""")
_ChassisIDExtension_Type = DellUnsigned16BitRange
_ChassisIDExtension_Object = MibTableColumn
chassisIDExtension = _ChassisIDExtension_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 13),
    _ChassisIDExtension_Type()
)
chassisIDExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIDExtension.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisIDExtension.setDescription("""\
0300.0010.0001.0013 This attribute defines the SMBIOS Machine ID of the Dell
chassis.
""")
_ChassisSystemClass_Type = DellChassisSystemClass
_ChassisSystemClass_Object = MibTableColumn
chassisSystemClass = _ChassisSystemClass_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 14),
    _ChassisSystemClass_Type()
)
chassisSystemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemClass.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemClass.setDescription("""\
0300.0010.0001.0014 This attribute defines the chassis class of the Dell
chassis.
""")
_ChassisSystemName_Type = DellString
_ChassisSystemName_Object = MibTableColumn
chassisSystemName = _ChassisSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 15),
    _ChassisSystemName_Type()
)
chassisSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemName.setDescription("""\
0300.0010.0001.0015 This attribute defines system name of the Dell System.
""")
_ChassisSystemBootDateName_Type = DellDateName
_ChassisSystemBootDateName_Object = MibTableColumn
chassisSystemBootDateName = _ChassisSystemBootDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 16),
    _ChassisSystemBootDateName_Type()
)
chassisSystemBootDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemBootDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemBootDateName.setDescription("""\
0300.0010.0001.0016 This attribute defines boot time of the Dell System. Dates
are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_ChassisSystemDateName_Type = DellDateName
_ChassisSystemDateName_Object = MibTableColumn
chassisSystemDateName = _ChassisSystemDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 17),
    _ChassisSystemDateName_Type()
)
chassisSystemDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSystemDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemDateName.setDescription("""\
0300.0010.0001.0017 This attribute defines the current time of the Dell System.
Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_ChassisSystemLocationName_Type = DellString
_ChassisSystemLocationName_Object = MibTableColumn
chassisSystemLocationName = _ChassisSystemLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 18),
    _ChassisSystemLocationName_Type()
)
chassisSystemLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSystemLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemLocationName.setDescription("""\
0300.0010.0001.0018 This attribute defines the location of the Dell System.
""")
_ChassisSystemPrimaryUserName_Type = DellString
_ChassisSystemPrimaryUserName_Object = MibTableColumn
chassisSystemPrimaryUserName = _ChassisSystemPrimaryUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 19),
    _ChassisSystemPrimaryUserName_Type()
)
chassisSystemPrimaryUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSystemPrimaryUserName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemPrimaryUserName.setDescription("""\
0300.0010.0001.0019 This attribute defines the name of the primary user of the
Dell System.
""")
_ChassisSystemUserPhoneNumberName_Type = DellString
_ChassisSystemUserPhoneNumberName_Object = MibTableColumn
chassisSystemUserPhoneNumberName = _ChassisSystemUserPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 20),
    _ChassisSystemUserPhoneNumberName_Type()
)
chassisSystemUserPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSystemUserPhoneNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisSystemUserPhoneNumberName.setDescription("""\
0300.0010.0001.0020 This attribute defines the phone number of the primary user
of the Dell System.
""")
_ChassisConnectionStatusUnique_Type = DellConnectionStatus
_ChassisConnectionStatusUnique_Object = MibTableColumn
chassisConnectionStatusUnique = _ChassisConnectionStatusUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 21),
    _ChassisConnectionStatusUnique_Type()
)
chassisConnectionStatusUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisConnectionStatusUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisConnectionStatusUnique.setDescription("""\
0300.0010.0001.0021 This attribute defines the status of the connection of the
Dell chassis.
""")
_ChassisFanControlCapabilitiesUnique_Type = DellFanControlCapabilities
_ChassisFanControlCapabilitiesUnique_Object = MibTableColumn
chassisFanControlCapabilitiesUnique = _ChassisFanControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 22),
    _ChassisFanControlCapabilitiesUnique_Type()
)
chassisFanControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisFanControlCapabilitiesUnique.setDescription("""\
0300.0010.0001.0022 This attribute defines the capabilities of the fan control
function in the Dell chassis.
""")
_ChassisFanControlSettingsUnique_Type = DellFanControlSettings
_ChassisFanControlSettingsUnique_Object = MibTableColumn
chassisFanControlSettingsUnique = _ChassisFanControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 23),
    _ChassisFanControlSettingsUnique_Type()
)
chassisFanControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisFanControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisFanControlSettingsUnique.setDescription("""\
0300.0010.0001.0023 This attribute defines the reading and setting of the fan
control hardware in the Dell chassis.
""")
_ChassisLEDControlCapabilitiesUnique_Type = DellLEDControlCapabilities
_ChassisLEDControlCapabilitiesUnique_Object = MibTableColumn
chassisLEDControlCapabilitiesUnique = _ChassisLEDControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 24),
    _ChassisLEDControlCapabilitiesUnique_Type()
)
chassisLEDControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLEDControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisLEDControlCapabilitiesUnique.setDescription("""\
0300.0010.0001.0024 This attribute defines the capabilities of the LED control
function in the Dell chassis.
""")
_ChassisLEDControlSettingsUnique_Type = DellLEDControlSettings
_ChassisLEDControlSettingsUnique_Object = MibTableColumn
chassisLEDControlSettingsUnique = _ChassisLEDControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 25),
    _ChassisLEDControlSettingsUnique_Type()
)
chassisLEDControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisLEDControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisLEDControlSettingsUnique.setDescription("""\
0300.0010.0001.0025 This attribute defines the reading and setting of the LED
control hardware in the Dell chassis.
""")
_ChassisHDFaultClearControlCapabilities_Type = DellHDFaultLEDControlCapabilities
_ChassisHDFaultClearControlCapabilities_Object = MibTableColumn
chassisHDFaultClearControlCapabilities = _ChassisHDFaultClearControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 26),
    _ChassisHDFaultClearControlCapabilities_Type()
)
chassisHDFaultClearControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHDFaultClearControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisHDFaultClearControlCapabilities.setDescription("""\
0300.0010.0001.0026 This attribute defines if the chassis allows reset of the
chassis hard disk drive fault LED.
""")
_ChassisHDFaultClearControlSettings_Type = DellHDFaultLEDControlSettings
_ChassisHDFaultClearControlSettings_Object = MibTableColumn
chassisHDFaultClearControlSettings = _ChassisHDFaultClearControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 27),
    _ChassisHDFaultClearControlSettings_Type()
)
chassisHDFaultClearControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisHDFaultClearControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisHDFaultClearControlSettings.setDescription("""\
0300.0010.0001.0027 This attribute allows reset of a chassis hard disk drive
fault LED.
""")
_ChassisIdentifyFlashControlCapabilities_Type = DellChassisIdentifyControlCapabilities
_ChassisIdentifyFlashControlCapabilities_Object = MibTableColumn
chassisIdentifyFlashControlCapabilities = _ChassisIdentifyFlashControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 28),
    _ChassisIdentifyFlashControlCapabilities_Type()
)
chassisIdentifyFlashControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlCapabilities.setDescription("""\
0300.0010.0001.0028 This attribute defines if the chassis allows setting of the
chassis front panel LED's to flash.
""")
_ChassisIdentifyFlashControlSettings_Type = DellChassisIdentifyControlSettings
_ChassisIdentifyFlashControlSettings_Object = MibTableColumn
chassisIdentifyFlashControlSettings = _ChassisIdentifyFlashControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 29),
    _ChassisIdentifyFlashControlSettings_Type()
)
chassisIdentifyFlashControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisIdentifyFlashControlSettings.setDescription("""\
0300.0010.0001.0029 This attribute setting causes the chassis front panel LED's
to flash.
""")
_ChassisLockPresent_Type = DellBoolean
_ChassisLockPresent_Object = MibTableColumn
chassisLockPresent = _ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 30),
    _ChassisLockPresent_Type()
)
chassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLockPresent.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisLockPresent.setReference("""\
'DMTF|Physical Container Global Table|002' 3
""")
if mibBuilder.loadTexts:
    chassisLockPresent.setDescription("""\
0300.0010.0001.0030 If true, a chassis lock is present on the chassis.
""")
_ChassishostControlCapabilitiesUnique_Type = DellHostControlCapabilities
_ChassishostControlCapabilitiesUnique_Object = MibTableColumn
chassishostControlCapabilitiesUnique = _ChassishostControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 31),
    _ChassishostControlCapabilitiesUnique_Type()
)
chassishostControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassishostControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassishostControlCapabilitiesUnique.setDescription("""\
0300.0010.0001.031 This attribute defines the capabilities of the Dell Host
Control object.
""")
_ChassishostControlSettingsUnique_Type = DellHostControlSettings
_ChassishostControlSettingsUnique_Object = MibTableColumn
chassishostControlSettingsUnique = _ChassishostControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 32),
    _ChassishostControlSettingsUnique_Type()
)
chassishostControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassishostControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassishostControlSettingsUnique.setDescription("""\
0300.0010.0001.0032 This attribute defines the current settings of the Dell
Host Control object.
""")
_ChassiswatchDogControlCapabilitiesUnique_Type = DellWatchDogControlCapabilities
_ChassiswatchDogControlCapabilitiesUnique_Object = MibTableColumn
chassiswatchDogControlCapabilitiesUnique = _ChassiswatchDogControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 33),
    _ChassiswatchDogControlCapabilitiesUnique_Type()
)
chassiswatchDogControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassiswatchDogControlCapabilitiesUnique.setDescription("""\
0300.0010.0001.0033 This attribute defines the capabilities of the Dell Watch
Dog Timer object.
""")
_ChassiswatchDogControlSettingsUnique_Type = DelllWatchControlSettings
_ChassiswatchDogControlSettingsUnique_Object = MibTableColumn
chassiswatchDogControlSettingsUnique = _ChassiswatchDogControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 34),
    _ChassiswatchDogControlSettingsUnique_Type()
)
chassiswatchDogControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassiswatchDogControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassiswatchDogControlSettingsUnique.setDescription("""\
0300.0010.0001.0034 This attribute defines the current settings of the Dell
Watch Dog Timer object.
""")
_ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Type = DellWatchDogTimerCapabilities
_ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Object = MibTableColumn
chassiswatchDogControlExpiryTimeCapabilitiesUnique = _ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 35),
    _ChassiswatchDogControlExpiryTimeCapabilitiesUnique_Type()
)
chassiswatchDogControlExpiryTimeCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTimeCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTimeCapabilitiesUnique.setDescription("""\
0300.0010.0001.0035 This attribute defines the capabilities of the Dell Watch
Dog Expiry Timer object.
""")
_ChassiswatchDogControlExpiryTime_Type = DellUnsigned16BitRange
_ChassiswatchDogControlExpiryTime_Object = MibTableColumn
chassiswatchDogControlExpiryTime = _ChassiswatchDogControlExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 36),
    _ChassiswatchDogControlExpiryTime_Type()
)
chassiswatchDogControlExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassiswatchDogControlExpiryTime.setDescription("""\
0300.0010.0001.0036 This attribute defines the current watchdog timer value in
seconds.
""")
_ChassisallowSETCommandsfromSNMP_Type = DellBoolean
_ChassisallowSETCommandsfromSNMP_Object = MibTableColumn
chassisallowSETCommandsfromSNMP = _ChassisallowSETCommandsfromSNMP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 37),
    _ChassisallowSETCommandsfromSNMP_Type()
)
chassisallowSETCommandsfromSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisallowSETCommandsfromSNMP.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisallowSETCommandsfromSNMP.setDescription("""\
0300.0010.0001.0037 This attribute defines if SNMP SET type commands are
allowed or not.
""")
_ChassisPowerButtonControlCapabilitiesUnique_Type = DellPowerButtonControlCapabilities
_ChassisPowerButtonControlCapabilitiesUnique_Object = MibTableColumn
chassisPowerButtonControlCapabilitiesUnique = _ChassisPowerButtonControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 38),
    _ChassisPowerButtonControlCapabilitiesUnique_Type()
)
chassisPowerButtonControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerButtonControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisPowerButtonControlCapabilitiesUnique.setDescription("""\
0300.0010.0001.0038 This attribute defines the capabilities of the power button
control function in the Dell chassis.
""")
_ChassisPowerButtonControlSettingsUnique_Type = DellPowerButtonControlSettings
_ChassisPowerButtonControlSettingsUnique_Object = MibTableColumn
chassisPowerButtonControlSettingsUnique = _ChassisPowerButtonControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 10, 1, 39),
    _ChassisPowerButtonControlSettingsUnique_Type()
)
chassisPowerButtonControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisPowerButtonControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    chassisPowerButtonControlSettingsUnique.setDescription("""\
0300.0010.0001.0039 This attribute defines the reading and setting of the power
button control hardware in the Dell chassis.
""")
_UUIDTable_Object = MibTable
uUIDTable = _UUIDTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20)
)
if mibBuilder.loadTexts:
    uUIDTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    uUIDTable.setDescription("""\
0300.0020 This group defines the Dell Universal Unique Identification
Information Table.
""")
_UUIDTableEntry_Object = MibTableRow
uUIDTableEntry = _UUIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1)
)
uUIDTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "uUIDchassisIndex"),
    (0, "MIB-Dell-10892", "uUIDIndex"),
)
if mibBuilder.loadTexts:
    uUIDTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    uUIDTableEntry.setDescription("""\
0300.0020.0001 This group defines the Dell Universal Unique Identification
Information Table Entry.
""")
_UUIDchassisIndex_Type = DellObjectRange
_UUIDchassisIndex_Object = MibTableColumn
uUIDchassisIndex = _UUIDchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 1),
    _UUIDchassisIndex_Type()
)
uUIDchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    uUIDchassisIndex.setDescription("""\
0300.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_UUIDIndex_Type = DellObjectRange
_UUIDIndex_Object = MibTableColumn
uUIDIndex = _UUIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 2),
    _UUIDIndex_Type()
)
uUIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    uUIDIndex.setDescription("""\
0300.0020.0001.0002 This attribute defines the type of Universal Unique
Identification Information of the Dell chassis.
""")
_UUIDType_Type = DellUUIDType
_UUIDType_Object = MibTableColumn
uUIDType = _UUIDType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 3),
    _UUIDType_Type()
)
uUIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDType.setStatus("mandatory")
if mibBuilder.loadTexts:
    uUIDType.setDescription("""\
0300.0020.0001.0003 This attribute defines the type of Universal Unique
Identification Information of the Dell chassis.
""")


class _UUIDValue_Type(OctetString):
    """Custom type uUIDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_UUIDValue_Type.__name__ = "OctetString"
_UUIDValue_Object = MibTableColumn
uUIDValue = _UUIDValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 20, 1, 4),
    _UUIDValue_Type()
)
uUIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uUIDValue.setStatus("mandatory")
if mibBuilder.loadTexts:
    uUIDValue.setDescription("""\
0300.0020.0001.0004 This attribute defines the value of the Universal Unique
Identification Information of the Dell chassis.
""")
_PostLogTable_Object = MibTable
postLogTable = _PostLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30)
)
if mibBuilder.loadTexts:
    postLogTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogTable.setDescription("""\
0300.0030 This group defines the Dell POST Log Table.
""")
_PostLogTableEntry_Object = MibTableRow
postLogTableEntry = _PostLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1)
)
postLogTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "postLogchassisIndex"),
    (0, "MIB-Dell-10892", "postLogRecordIndex"),
)
if mibBuilder.loadTexts:
    postLogTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogTableEntry.setDescription("""\
0300.0030.0001 This group defines the Dell POST Log Table Entry.
""")
_PostLogchassisIndex_Type = DellObjectRange
_PostLogchassisIndex_Object = MibTableColumn
postLogchassisIndex = _PostLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 1),
    _PostLogchassisIndex_Type()
)
postLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogchassisIndex.setDescription("""\
0300.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PostLogRecordIndex_Type = DellUnsigned32BitRange
_PostLogRecordIndex_Object = MibTableColumn
postLogRecordIndex = _PostLogRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 2),
    _PostLogRecordIndex_Type()
)
postLogRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogRecordIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogRecordIndex.setDescription("""\
0300.0030.0001.0002 This attribute defines the record number of the POST log to
be returned.
""")
_PostLogStateCapabilitiesUnique_Type = DellStateCapabilitiesLogUnique
_PostLogStateCapabilitiesUnique_Object = MibTableColumn
postLogStateCapabilitiesUnique = _PostLogStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 3),
    _PostLogStateCapabilitiesUnique_Type()
)
postLogStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogStateCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogStateCapabilitiesUnique.setDescription("""\
0300.0030.0001.0003 This attribute defines the capabilities of the object that
is writing the POST log.
""")
_PostLogStateSettingsUnique_Type = DellStateSettingsLogUnique
_PostLogStateSettingsUnique_Object = MibTableColumn
postLogStateSettingsUnique = _PostLogStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 4),
    _PostLogStateSettingsUnique_Type()
)
postLogStateSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postLogStateSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogStateSettingsUnique.setDescription("""\
0300.0030.0001.0004 This attribute defines the state of the object that is
writing the POST log.
""")


class _PostLogRecord_Type(DisplayString):
    """Custom type postLogRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PostLogRecord_Type.__name__ = "DisplayString"
_PostLogRecord_Object = MibTableColumn
postLogRecord = _PostLogRecord_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 5),
    _PostLogRecord_Type()
)
postLogRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogRecord.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogRecord.setDescription("""\
0300.0030.0001.0005 This attribute defines the data of the postLogRecordNumber
in the POST log being returned.
""")
_PostLogFormat_Type = DellLogFormat
_PostLogFormat_Object = MibTableColumn
postLogFormat = _PostLogFormat_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 30, 1, 6),
    _PostLogFormat_Type()
)
postLogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postLogFormat.setStatus("mandatory")
if mibBuilder.loadTexts:
    postLogFormat.setDescription("""\
0300.0030.0001.0006 This attribute defines the format of the POST log.
""")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogTable.setDescription("""\
0300.0040 This group defines the Dell Event Log Table.
""")
_EventLogTableEntry_Object = MibTableRow
eventLogTableEntry = _EventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1)
)
eventLogTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "eventLogchassisIndex"),
    (0, "MIB-Dell-10892", "eventLogRecordIndex"),
)
if mibBuilder.loadTexts:
    eventLogTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogTableEntry.setDescription("""\
0300.0040.0001 This group defines the Dell Event Log Table Entry.
""")
_EventLogchassisIndex_Type = DellObjectRange
_EventLogchassisIndex_Object = MibTableColumn
eventLogchassisIndex = _EventLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 1),
    _EventLogchassisIndex_Type()
)
eventLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogchassisIndex.setDescription("""\
0300.0040.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_EventLogRecordIndex_Type = DellUnsigned32BitRange
_EventLogRecordIndex_Object = MibTableColumn
eventLogRecordIndex = _EventLogRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 2),
    _EventLogRecordIndex_Type()
)
eventLogRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRecordIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogRecordIndex.setDescription("""\
0300.0040.0001.0002 This attribute defines the record number of the Event log
to be returned.
""")
_EventLogStateCapabilitiesUnique_Type = DellStateCapabilitiesLogUnique
_EventLogStateCapabilitiesUnique_Object = MibTableColumn
eventLogStateCapabilitiesUnique = _EventLogStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 3),
    _EventLogStateCapabilitiesUnique_Type()
)
eventLogStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogStateCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogStateCapabilitiesUnique.setDescription("""\
0300.0040.0001.0003 This attribute defines the capabilities of the object that
is writing the Event log.
""")
_EventLogStateSettingsUnique_Type = DellStateSettingsLogUnique
_EventLogStateSettingsUnique_Object = MibTableColumn
eventLogStateSettingsUnique = _EventLogStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 4),
    _EventLogStateSettingsUnique_Type()
)
eventLogStateSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogStateSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogStateSettingsUnique.setDescription("""\
0300.0040.0001.0004 This attribute defines the state of the object that is
writing the Event log.
""")


class _EventLogRecord_Type(DisplayString):
    """Custom type eventLogRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_EventLogRecord_Type.__name__ = "DisplayString"
_EventLogRecord_Object = MibTableColumn
eventLogRecord = _EventLogRecord_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 5),
    _EventLogRecord_Type()
)
eventLogRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRecord.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogRecord.setDescription("""\
0300.0040.0001.0005 This attribute defines the data of the eventLogRecordNumber
in the Event log being returned.
""")
_EventLogFormat_Type = DellLogFormat
_EventLogFormat_Object = MibTableColumn
eventLogFormat = _EventLogFormat_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 6),
    _EventLogFormat_Type()
)
eventLogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogFormat.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogFormat.setDescription("""\
0300.0040.0001.0006 This attribute defines the format of the Event log.
""")
_EventLogSeverityStatus_Type = DellStatus
_EventLogSeverityStatus_Object = MibTableColumn
eventLogSeverityStatus = _EventLogSeverityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 7),
    _EventLogSeverityStatus_Type()
)
eventLogSeverityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSeverityStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogSeverityStatus.setDescription("""\
0300.0040.0001.0007 This attribute defines the severity of the Event log
record.
""")
_EventLogDateName_Type = DellDateName
_EventLogDateName_Object = MibTableColumn
eventLogDateName = _EventLogDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 40, 1, 8),
    _EventLogDateName_Type()
)
eventLogDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    eventLogDateName.setDescription("""\
0300.0040.0001.0008 This attribute defines the date and time of the Event log
record.
""")
_SystemBIOSTable_Object = MibTable
systemBIOSTable = _SystemBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50)
)
if mibBuilder.loadTexts:
    systemBIOSTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSTable.setDescription("""\
0300.0050 This group defines the Dell System BIOS Table.
""")
_SystemBIOSTableEntry_Object = MibTableRow
systemBIOSTableEntry = _SystemBIOSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1)
)
systemBIOSTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemBIOSchassisIndex"),
    (0, "MIB-Dell-10892", "systemBIOSIndex"),
)
if mibBuilder.loadTexts:
    systemBIOSTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSTableEntry.setDescription("""\
0300.0050.0001 This group defines the Dell System BIOS Table Entry.
""")
_SystemBIOSchassisIndex_Type = DellObjectRange
_SystemBIOSchassisIndex_Object = MibTableColumn
systemBIOSchassisIndex = _SystemBIOSchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 1),
    _SystemBIOSchassisIndex_Type()
)
systemBIOSchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSchassisIndex.setDescription("""\
0300.0050.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemBIOSIndex_Type = DellObjectRange
_SystemBIOSIndex_Object = MibTableColumn
systemBIOSIndex = _SystemBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 2),
    _SystemBIOSIndex_Type()
)
systemBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSIndex.setDescription("""\
0300.0050.0001.0002 This attribute defines the index of the system BIOS of this
object.
""")
_SystemBIOSStateCapabilities_Type = DellStateCapabilities
_SystemBIOSStateCapabilities_Object = MibTableColumn
systemBIOSStateCapabilities = _SystemBIOSStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 3),
    _SystemBIOSStateCapabilities_Type()
)
systemBIOSStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSStateCapabilities.setDescription("""\
0300.0050.0001.0003 This attribute defines the capabilities of the system BIOS
of this object.
""")
_SystemBIOSStateSettings_Type = DellStateSettings
_SystemBIOSStateSettings_Object = MibTableColumn
systemBIOSStateSettings = _SystemBIOSStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 4),
    _SystemBIOSStateSettings_Type()
)
systemBIOSStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBIOSStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSStateSettings.setDescription("""\
0300.0050.0001.0004 This attribute defines the state of the system BIOS of this
object.
""")
_SystemBIOSStatus_Type = DellStatus
_SystemBIOSStatus_Object = MibTableColumn
systemBIOSStatus = _SystemBIOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 5),
    _SystemBIOSStatus_Type()
)
systemBIOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSStatus.setDescription("""\
0300.0060.0001.0005 This attribute defines the status of the Dell BIOS.
""")
_SystemBIOSSize_Type = DellUnsigned32BitRange
_SystemBIOSSize_Object = MibTableColumn
systemBIOSSize = _SystemBIOSSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 6),
    _SystemBIOSSize_Type()
)
systemBIOSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSSize.setDescription("""\
0300.0050.0001.0006 This attribute defines the image size of the System BIOS in
Kbytes. 0 (zero) indicates size unknown.
""")
_SystemBIOSReleaseDateName_Type = DellDateName
_SystemBIOSReleaseDateName_Object = MibTableColumn
systemBIOSReleaseDateName = _SystemBIOSReleaseDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 7),
    _SystemBIOSReleaseDateName_Type()
)
systemBIOSReleaseDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSReleaseDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSReleaseDateName.setDescription("""\
0300.0050.0001.0007 This attribute defines the release date name of the system
BIOS.
""")
_SystemBIOSVersionName_Type = DellString
_SystemBIOSVersionName_Object = MibTableColumn
systemBIOSVersionName = _SystemBIOSVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 8),
    _SystemBIOSVersionName_Type()
)
systemBIOSVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSVersionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSVersionName.setDescription("""\
0300.0050.0001.0008 This attribute defines the version name of the System BIOS.
""")
_SystemBIOSStartingAddress_Type = DellUnsigned64BitRange
_SystemBIOSStartingAddress_Object = MibTableColumn
systemBIOSStartingAddress = _SystemBIOSStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 9),
    _SystemBIOSStartingAddress_Type()
)
systemBIOSStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSStartingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSStartingAddress.setDescription("""\
0300.0050.0001.0009 This attribute defines the starting address of the system
BIOS. 0 (zero) indicates the starting address is unknown.
""")
_SystemBIOSEndingAddress_Type = DellUnsigned64BitRange
_SystemBIOSEndingAddress_Object = MibTableColumn
systemBIOSEndingAddress = _SystemBIOSEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 10),
    _SystemBIOSEndingAddress_Type()
)
systemBIOSEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSEndingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSEndingAddress.setDescription("""\
0300.0050.0001.0010 This attribute defines the ending address of the system
BIOS. 0 (zero) indicates the starting address is unknown.
""")
_SystemBIOSManufacturerName_Type = DellString
_SystemBIOSManufacturerName_Object = MibTableColumn
systemBIOSManufacturerName = _SystemBIOSManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 50, 1, 11),
    _SystemBIOSManufacturerName_Type()
)
systemBIOSManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBIOSManufacturerName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemBIOSManufacturerName.setDescription("""\
0300.0050.0001.0011 This attribute defines the manufacturer's name of the Dell
System BIOS.
""")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareTable.setDescription("""\
0300.0060 This Group defines the Dell Firmware Table.
""")
_FirmwareTableEntry_Object = MibTableRow
firmwareTableEntry = _FirmwareTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1)
)
firmwareTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "firmwarechassisIndex"),
    (0, "MIB-Dell-10892", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareTableEntry.setDescription("""\
0300.0060.0001 This Group defines the Dell Firmware Table Entry.
""")
_FirmwarechassisIndex_Type = DellObjectRange
_FirmwarechassisIndex_Object = MibTableColumn
firmwarechassisIndex = _FirmwarechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 1),
    _FirmwarechassisIndex_Type()
)
firmwarechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwarechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwarechassisIndex.setDescription("""\
0300.0060.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_FirmwareIndex_Type = DellObjectRange
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 2),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareIndex.setDescription("""\
0300.0060.0001.0002 This attribute defines the index of Dell firmware in this
chassis.
""")
_FirmwareStateCapabilities_Type = DellStateCapabilities
_FirmwareStateCapabilities_Object = MibTableColumn
firmwareStateCapabilities = _FirmwareStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 3),
    _FirmwareStateCapabilities_Type()
)
firmwareStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareStateCapabilities.setDescription("""\
0300.0060.0001.0003 This attribute defines the capabilities of the Dell
firmware states.
""")
_FirmwareStateSettings_Type = DellStateSettings
_FirmwareStateSettings_Object = MibTableColumn
firmwareStateSettings = _FirmwareStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 4),
    _FirmwareStateSettings_Type()
)
firmwareStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareStateSettings.setDescription("""\
0300.0060.0001.0004 This attribute defines the state of the Dell firmware.
""")
_FirmwareStatus_Type = DellStatus
_FirmwareStatus_Object = MibTableColumn
firmwareStatus = _FirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 5),
    _FirmwareStatus_Type()
)
firmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareStatus.setDescription("""\
0300.0060.0001.0005 This attribute defines the status of the Dell firmware.
""")
_FirmwareSize_Type = DellUnsigned16BitRange
_FirmwareSize_Object = MibTableColumn
firmwareSize = _FirmwareSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 6),
    _FirmwareSize_Type()
)
firmwareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareSize.setDescription("""\
0300.0060.0001.0006 This attribute defines the image size of the firmware in
Kbytes. 0 (zero) indicates size unknown.
""")
_FirmwareType_Type = DellFirwareType
_FirmwareType_Object = MibTableColumn
firmwareType = _FirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 7),
    _FirmwareType_Type()
)
firmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareType.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareType.setDescription("""\
0300.0060.0001.0007 This attribute defines the type of firmware.
""")
_FirmwareTypeName_Type = DellString
_FirmwareTypeName_Object = MibTableColumn
firmwareTypeName = _FirmwareTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 8),
    _FirmwareTypeName_Type()
)
firmwareTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareTypeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareTypeName.setDescription("""\
0300.0060.0001.0008 This attribute defines the type name of the firmware.
""")
_FirmwareUpdateCapabilities_Type = DellUnsigned16BitRange
_FirmwareUpdateCapabilities_Object = MibTableColumn
firmwareUpdateCapabilities = _FirmwareUpdateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 9),
    _FirmwareUpdateCapabilities_Type()
)
firmwareUpdateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareUpdateCapabilities.setDescription("""\
0300.0060.0001.0009 This attribute defines the bitmap of supported methods for
firmware update.
""")


class _FirmwareDateName_Type(OctetString):
    """Custom type firmwareDateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FirmwareDateName_Type.__name__ = "OctetString"
_FirmwareDateName_Object = MibTableColumn
firmwareDateName = _FirmwareDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 10),
    _FirmwareDateName_Type()
)
firmwareDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareDateName.setDescription("""\
0300.0060.0001.0010 This attribute defines the date of the firmware.
""")
_FirmwareVersionName_Type = DellString
_FirmwareVersionName_Object = MibTableColumn
firmwareVersionName = _FirmwareVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 60, 1, 11),
    _FirmwareVersionName_Type()
)
firmwareVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareVersionName.setDescription("""\
0300.0060.0001.0011 This attribute defines the Version Name of the firmware.
""")
_IntrusionTable_Object = MibTable
intrusionTable = _IntrusionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70)
)
if mibBuilder.loadTexts:
    intrusionTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionTable.setDescription("""\
0300.0070 This Group defines the Dell intrusion Table.
""")
_IntrusionTableEntry_Object = MibTableRow
intrusionTableEntry = _IntrusionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1)
)
intrusionTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "intrusionchassisIndex"),
    (0, "MIB-Dell-10892", "intrusionIndex"),
)
if mibBuilder.loadTexts:
    intrusionTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionTableEntry.setDescription("""\
0300.0070.0001 This Group defines the Dell intrusion Table Entry.
""")
_IntrusionchassisIndex_Type = DellObjectRange
_IntrusionchassisIndex_Object = MibTableColumn
intrusionchassisIndex = _IntrusionchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 1),
    _IntrusionchassisIndex_Type()
)
intrusionchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionchassisIndex.setDescription("""\
0300.0070.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_IntrusionIndex_Type = DellObjectRange
_IntrusionIndex_Object = MibTableColumn
intrusionIndex = _IntrusionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 2),
    _IntrusionIndex_Type()
)
intrusionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionIndex.setDescription("""\
0300.0070.0001.0002 This attribute defines the index of Dell intrusion objects
in this subGroup.
""")
_IntrusionStateCapabilities_Type = DellStateCapabilities
_IntrusionStateCapabilities_Object = MibTableColumn
intrusionStateCapabilities = _IntrusionStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 3),
    _IntrusionStateCapabilities_Type()
)
intrusionStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionStateCapabilities.setDescription("""\
0300.0070.0001.0003 This attribute defines the capabilities of the Dell
intrusion object.
""")
_IntrusionStateSettings_Type = DellStateSettings
_IntrusionStateSettings_Object = MibTableColumn
intrusionStateSettings = _IntrusionStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 4),
    _IntrusionStateSettings_Type()
)
intrusionStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intrusionStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionStateSettings.setDescription("""\
0300.0070.0001.0004 This attribute defines the state of the Dell intrusion
object.
""")
_IntrusionStatus_Type = DellStatus
_IntrusionStatus_Object = MibTableColumn
intrusionStatus = _IntrusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 5),
    _IntrusionStatus_Type()
)
intrusionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionStatus.setDescription("""\
0300.0070.0001.0005 This attribute defines the status of the Dell intrusion
object.
""")
_IntrusionReading_Type = DellIntrusionReading
_IntrusionReading_Object = MibTableColumn
intrusionReading = _IntrusionReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 6),
    _IntrusionReading_Type()
)
intrusionReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionReading.setReference("""\
'DMTF|Physical Container Global Table|002' 12
""")
if mibBuilder.loadTexts:
    intrusionReading.setDescription("""\
0300.0070.0001.0006 This attribute defines the reading of the Dell intrusion
object.
""")
_IntrusionType_Type = DellIntrusionType
_IntrusionType_Object = MibTableColumn
intrusionType = _IntrusionType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 7),
    _IntrusionType_Type()
)
intrusionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionType.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionType.setDescription("""\
0300.0070.0001.0007 This attribute defines the type of the Dell intrusion
object.
""")
_IntrusionLocationName_Type = DellString
_IntrusionLocationName_Object = MibTableColumn
intrusionLocationName = _IntrusionLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 300, 70, 1, 8),
    _IntrusionLocationName_Type()
)
intrusionLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intrusionLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    intrusionLocationName.setDescription("""\
0300.0070.0001.0008 This attribute defines the location name of the Dell
intrusion object in this subGroup
""")
_OperatingSystemGroup_ObjectIdentity = ObjectIdentity
operatingSystemGroup = _OperatingSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400)
)
_OperatingSystemTable_Object = MibTable
operatingSystemTable = _OperatingSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10)
)
if mibBuilder.loadTexts:
    operatingSystemTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemTable.setDescription("""\
0400.0010 This Group defines the Operating System Table.
""")
_OperatingSystemTableEntry_Object = MibTableRow
operatingSystemTableEntry = _OperatingSystemTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1)
)
operatingSystemTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "operatingSystemchassisIndex"),
)
if mibBuilder.loadTexts:
    operatingSystemTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemTableEntry.setDescription("""\
0400.0010.0001 This Group defines the Operating System Table Entry.
""")
_OperatingSystemchassisIndex_Type = DellObjectRange
_OperatingSystemchassisIndex_Object = MibTableColumn
operatingSystemchassisIndex = _OperatingSystemchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 1),
    _OperatingSystemchassisIndex_Type()
)
operatingSystemchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemchassisIndex.setDescription("""\
0400.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_OperatingSystemStateCapabilities_Type = DellStateCapabilities
_OperatingSystemStateCapabilities_Object = MibTableColumn
operatingSystemStateCapabilities = _OperatingSystemStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 2),
    _OperatingSystemStateCapabilities_Type()
)
operatingSystemStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemStateCapabilities.setDescription("""\
0400.0010.0001.0002 This attribute defines the capabilities of the Operating
System.
""")
_OperatingSystemStateSettings_Type = DellStateSettings
_OperatingSystemStateSettings_Object = MibTableColumn
operatingSystemStateSettings = _OperatingSystemStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 3),
    _OperatingSystemStateSettings_Type()
)
operatingSystemStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatingSystemStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemStateSettings.setDescription("""\
0400.0010.0001.0003 This attribute defines the state of the Operating System.
""")
_OperatingSystemStatus_Type = DellStatus
_OperatingSystemStatus_Object = MibTableColumn
operatingSystemStatus = _OperatingSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 4),
    _OperatingSystemStatus_Type()
)
operatingSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemStatus.setDescription("""\
0400.0010.0001.0004 This attribute defines the status of the Operating System.
""")
_OperatingSystemIsPrimary_Type = DellBoolean
_OperatingSystemIsPrimary_Object = MibTableColumn
operatingSystemIsPrimary = _OperatingSystemIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 5),
    _OperatingSystemIsPrimary_Type()
)
operatingSystemIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemIsPrimary.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemIsPrimary.setDescription("""\
0400.0010.0001.0005 This attribute defines if this operating system is the
primary operating system or not.
""")
_OperatingSystemOperatingSystemName_Type = DellString
_OperatingSystemOperatingSystemName_Object = MibTableColumn
operatingSystemOperatingSystemName = _OperatingSystemOperatingSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 6),
    _OperatingSystemOperatingSystemName_Type()
)
operatingSystemOperatingSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemOperatingSystemName.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemOperatingSystemName.setDescription("""\
0400.0010.0001.0006 This attribute defines the name of the Operating System.
""")
_OperatingSystemOperatingSystemVersionName_Type = DellString
_OperatingSystemOperatingSystemVersionName_Object = MibTableColumn
operatingSystemOperatingSystemVersionName = _OperatingSystemOperatingSystemVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 10, 1, 7),
    _OperatingSystemOperatingSystemVersionName_Type()
)
operatingSystemOperatingSystemVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemOperatingSystemVersionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemOperatingSystemVersionName.setDescription("""\
0400.0010.0001.0007 This attribute defines the version of the Operating System.
""")
_OperatingSystemMemoryTable_Object = MibTable
operatingSystemMemoryTable = _OperatingSystemMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20)
)
if mibBuilder.loadTexts:
    operatingSystemMemoryTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryTable.setDescription("""\
0400.0020 This Group defines the Operating System Memory Table.
""")
_OperatingSystemMemoryTableEntry_Object = MibTableRow
operatingSystemMemoryTableEntry = _OperatingSystemMemoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1)
)
operatingSystemMemoryTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "operatingSystemMemorychassisIndex"),
)
if mibBuilder.loadTexts:
    operatingSystemMemoryTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryTableEntry.setDescription("""\
0400.0020.0001 This Group defines the Operating System Memory Table Entry.
""")
_OperatingSystemMemorychassisIndex_Type = DellObjectRange
_OperatingSystemMemorychassisIndex_Object = MibTableColumn
operatingSystemMemorychassisIndex = _OperatingSystemMemorychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 1),
    _OperatingSystemMemorychassisIndex_Type()
)
operatingSystemMemorychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemorychassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemorychassisIndex.setDescription("""\
0400.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_OperatingSystemMemoryStateCapabilities_Type = DellStateCapabilities
_OperatingSystemMemoryStateCapabilities_Object = MibTableColumn
operatingSystemMemoryStateCapabilities = _OperatingSystemMemoryStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 2),
    _OperatingSystemMemoryStateCapabilities_Type()
)
operatingSystemMemoryStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryStateCapabilities.setDescription("""\
0400.0020.0001.0002 This attribute defines the capabilities of the Operating
System Memory.
""")
_OperatingSystemMemoryStateSettings_Type = DellStateSettings
_OperatingSystemMemoryStateSettings_Object = MibTableColumn
operatingSystemMemoryStateSettings = _OperatingSystemMemoryStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 3),
    _OperatingSystemMemoryStateSettings_Type()
)
operatingSystemMemoryStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatingSystemMemoryStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryStateSettings.setDescription("""\
0400.0020.0001.0003 This attribute defines the state of the Operating System
Memory.
""")
_OperatingSystemMemoryStatus_Type = DellStatus
_OperatingSystemMemoryStatus_Object = MibTableColumn
operatingSystemMemoryStatus = _OperatingSystemMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 4),
    _OperatingSystemMemoryStatus_Type()
)
operatingSystemMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryStatus.setDescription("""\
0400.0020.0001.0004 This attribute defines the status of the Operating System
Memory.
""")
_OperatingSystemMemoryTotalPhysicalSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryTotalPhysicalSize_Object = MibTableColumn
operatingSystemMemoryTotalPhysicalSize = _OperatingSystemMemoryTotalPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 5),
    _OperatingSystemMemoryTotalPhysicalSize_Type()
)
operatingSystemMemoryTotalPhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalPhysicalSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalPhysicalSize.setDescription("""\
0400.0020.0001.0005 This attribute defines the total physical memory in the
Operating System Memory in Kbytes.
""")
_OperatingSystemMemoryAvailablePhysicalSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryAvailablePhysicalSize_Object = MibTableColumn
operatingSystemMemoryAvailablePhysicalSize = _OperatingSystemMemoryAvailablePhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 6),
    _OperatingSystemMemoryAvailablePhysicalSize_Type()
)
operatingSystemMemoryAvailablePhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailablePhysicalSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailablePhysicalSize.setDescription("""\
0400.0020.0001.0006 This attribute defines the available physical memory in the
Operating System Memory in Kbytes.
""")
_OperatingSystemMemoryTotalPageFileSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryTotalPageFileSize_Object = MibTableColumn
operatingSystemMemoryTotalPageFileSize = _OperatingSystemMemoryTotalPageFileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 7),
    _OperatingSystemMemoryTotalPageFileSize_Type()
)
operatingSystemMemoryTotalPageFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalPageFileSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalPageFileSize.setDescription("""\
0400.0020.0001.0007 This attribute defines the total page file memory in the
Operating System Memory in Kbytes.
""")
_OperatingSystemMemoryAvailablePageFileSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryAvailablePageFileSize_Object = MibTableColumn
operatingSystemMemoryAvailablePageFileSize = _OperatingSystemMemoryAvailablePageFileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 8),
    _OperatingSystemMemoryAvailablePageFileSize_Type()
)
operatingSystemMemoryAvailablePageFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailablePageFileSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailablePageFileSize.setDescription("""\
0400.0020.0001.0008 This attribute defines the available page file memory in
the Operating System Memory in Kbytes.
""")
_OperatingSystemMemoryTotalVirtualSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryTotalVirtualSize_Object = MibTableColumn
operatingSystemMemoryTotalVirtualSize = _OperatingSystemMemoryTotalVirtualSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 9),
    _OperatingSystemMemoryTotalVirtualSize_Type()
)
operatingSystemMemoryTotalVirtualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalVirtualSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryTotalVirtualSize.setDescription("""\
0400.0020.0001.0009 This attribute defines the total virtual memory in the
Operating System Memory in Kbytes.
""")
_OperatingSystemMemoryAvailableVirtualSize_Type = DellUnsigned32BitRange
_OperatingSystemMemoryAvailableVirtualSize_Object = MibTableColumn
operatingSystemMemoryAvailableVirtualSize = _OperatingSystemMemoryAvailableVirtualSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 400, 20, 1, 10),
    _OperatingSystemMemoryAvailableVirtualSize_Type()
)
operatingSystemMemoryAvailableVirtualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailableVirtualSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    operatingSystemMemoryAvailableVirtualSize.setDescription("""\
0400.0020.0001.0010 This attribute defines the available virtual memory in the
Operating System Memory in Kbytes.
""")
_SystemResourceGroup_ObjectIdentity = ObjectIdentity
systemResourceGroup = _SystemResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500)
)
_SystemResourceMapTable_Object = MibTable
systemResourceMapTable = _SystemResourceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10)
)
if mibBuilder.loadTexts:
    systemResourceMapTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapTable.setDescription("""\
0500.0010 This Group defines the Dell System Resource Map Table.
""")
_SystemResourceMapTableEntry_Object = MibTableRow
systemResourceMapTableEntry = _SystemResourceMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1)
)
systemResourceMapTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceMapchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceMapIndex"),
)
if mibBuilder.loadTexts:
    systemResourceMapTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapTableEntry.setDescription("""\
0500.0010.0001 This Group defines the Dell System Resource Map Table Entry.
""")
_SystemResourceMapchassisIndex_Type = DellObjectRange
_SystemResourceMapchassisIndex_Object = MibTableColumn
systemResourceMapchassisIndex = _SystemResourceMapchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 1),
    _SystemResourceMapchassisIndex_Type()
)
systemResourceMapchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapchassisIndex.setDescription("""\
0500.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemResourceMapIndex_Type = DellObjectRange
_SystemResourceMapIndex_Object = MibTableColumn
systemResourceMapIndex = _SystemResourceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 2),
    _SystemResourceMapIndex_Type()
)
systemResourceMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapIndex.setDescription("""\
0500.0010.0001.0002 This attribute defines the index of Dell System Resource
Maps in this chassis.
""")
_SystemResourceMapStateCapabilities_Type = DellStateCapabilities
_SystemResourceMapStateCapabilities_Object = MibTableColumn
systemResourceMapStateCapabilities = _SystemResourceMapStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 3),
    _SystemResourceMapStateCapabilities_Type()
)
systemResourceMapStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapStateCapabilities.setDescription("""\
0500.0010.0001.0003 This attribute defines the capabilities of this system map.
""")
_SystemResourceMapStateSettings_Type = DellStateSettings
_SystemResourceMapStateSettings_Object = MibTableColumn
systemResourceMapStateSettings = _SystemResourceMapStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 4),
    _SystemResourceMapStateSettings_Type()
)
systemResourceMapStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResourceMapStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapStateSettings.setDescription("""\
0500.0010.0001.0004 This attribute defines the state of this system map.
""")
_SystemResourceMapStatus_Type = DellStatus
_SystemResourceMapStatus_Object = MibTableColumn
systemResourceMapStatus = _SystemResourceMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 5),
    _SystemResourceMapStatus_Type()
)
systemResourceMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapStatus.setDescription("""\
0500.0010.0001.0005 This attribute defines the status of this system map.
""")
_SystemResourceMapType_Type = DellSystemResourceMapType
_SystemResourceMapType_Object = MibTableColumn
systemResourceMapType = _SystemResourceMapType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 10, 1, 6),
    _SystemResourceMapType_Type()
)
systemResourceMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapType.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapType.setDescription("""\
0500.0010.0001.0006 This attribute defines the type of this system map.
""")
_SystemResourceOwnerTable_Object = MibTable
systemResourceOwnerTable = _SystemResourceOwnerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20)
)
if mibBuilder.loadTexts:
    systemResourceOwnerTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerTable.setDescription("""\
0500.0020 This Group defines the Dell System Resource Owner Table. The
variables in this group reference the Dell System Resource Map index.
""")
_SystemResourceOwnerTableEntry_Object = MibTableRow
systemResourceOwnerTableEntry = _SystemResourceOwnerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1)
)
systemResourceOwnerTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceOwnerchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceOwnerIndex"),
)
if mibBuilder.loadTexts:
    systemResourceOwnerTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerTableEntry.setDescription("""\
0500.0020.0001 This Group defines the Dell System Resource Owner Table Entry.
""")
_SystemResourceOwnerchassisIndex_Type = DellObjectRange
_SystemResourceOwnerchassisIndex_Object = MibTableColumn
systemResourceOwnerchassisIndex = _SystemResourceOwnerchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 1),
    _SystemResourceOwnerchassisIndex_Type()
)
systemResourceOwnerchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerchassisIndex.setDescription("""\
0500.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemResourceOwnerIndex_Type = DellObjectRange
_SystemResourceOwnerIndex_Object = MibTableColumn
systemResourceOwnerIndex = _SystemResourceOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 2),
    _SystemResourceOwnerIndex_Type()
)
systemResourceOwnerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerIndex.setDescription("""\
0500.0020.0001.0002 This attribute defines the index of Dell System Resource
Owners in this chassis.
""")
_SystemResourceOwnerStateCapabilities_Type = DellStateCapabilities
_SystemResourceOwnerStateCapabilities_Object = MibTableColumn
systemResourceOwnerStateCapabilities = _SystemResourceOwnerStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 3),
    _SystemResourceOwnerStateCapabilities_Type()
)
systemResourceOwnerStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerStateCapabilities.setDescription("""\
0500.0020.0001.0003 This attribute defines the capabilities of this system
resource owner.
""")
_SystemResourceOwnerStateSettings_Type = DellStateSettings
_SystemResourceOwnerStateSettings_Object = MibTableColumn
systemResourceOwnerStateSettings = _SystemResourceOwnerStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 4),
    _SystemResourceOwnerStateSettings_Type()
)
systemResourceOwnerStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResourceOwnerStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerStateSettings.setDescription("""\
0500.0020.0001.0004 This attribute defines the state of this system resource
owner.
""")
_SystemResourceOwnerStatus_Type = DellStatus
_SystemResourceOwnerStatus_Object = MibTableColumn
systemResourceOwnerStatus = _SystemResourceOwnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 5),
    _SystemResourceOwnerStatus_Type()
)
systemResourceOwnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerStatus.setDescription("""\
0500.0020.0001.0005 This attribute defines the status of this system resource
owner.
""")
_SystemResourceOwnerInterfaceType_Type = DellResourceOwnerInterfaceType
_SystemResourceOwnerInterfaceType_Object = MibTableColumn
systemResourceOwnerInterfaceType = _SystemResourceOwnerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 6),
    _SystemResourceOwnerInterfaceType_Type()
)
systemResourceOwnerInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerInterfaceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerInterfaceType.setDescription("""\
0500.0020.0001.0006 This attribute defines the interface type of this system
resource owner.
""")
_SystemResourceMapIndexReference_Type = DellObjectRange
_SystemResourceMapIndexReference_Object = MibTableColumn
systemResourceMapIndexReference = _SystemResourceMapIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 7),
    _SystemResourceMapIndexReference_Type()
)
systemResourceMapIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMapIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMapIndexReference.setDescription("""\
0500.0020.0001.0007 This attribute defines the index to the associated Dell
System Resource Map in this chassis.
""")
_SystemResourceOwnerDescriptionName_Type = DellString
_SystemResourceOwnerDescriptionName_Object = MibTableColumn
systemResourceOwnerDescriptionName = _SystemResourceOwnerDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 8),
    _SystemResourceOwnerDescriptionName_Type()
)
systemResourceOwnerDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerDescriptionName.setDescription("""\
0500.0020.0001.0008 This attribute defines the description name of the system
resource owner.
""")
_SystemResourceOwnerInterfaceInstance_Type = DellObjectRange
_SystemResourceOwnerInterfaceInstance_Object = MibTableColumn
systemResourceOwnerInterfaceInstance = _SystemResourceOwnerInterfaceInstance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 20, 1, 9),
    _SystemResourceOwnerInterfaceInstance_Type()
)
systemResourceOwnerInterfaceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceOwnerInterfaceInstance.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceOwnerInterfaceInstance.setDescription("""\
0500.0020.0001.0009 This attribute defines the index to the associated system
resource owner interface type in this chassis.
""")
_SystemResourceIOPortTable_Object = MibTable
systemResourceIOPortTable = _SystemResourceIOPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30)
)
if mibBuilder.loadTexts:
    systemResourceIOPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortTable.setDescription("""\
0500.0030 This Group defines the Dell System Resource IO Port Table.
""")
_SystemResourceIOPortTableEntry_Object = MibTableRow
systemResourceIOPortTableEntry = _SystemResourceIOPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1)
)
systemResourceIOPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceIOPortchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceIOPortIndex"),
)
if mibBuilder.loadTexts:
    systemResourceIOPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortTableEntry.setDescription("""\
0500.0030.0001 This Group defines the Dell System Resource IO Port Table Entry.
""")
_SystemResourceIOPortchassisIndex_Type = DellObjectRange
_SystemResourceIOPortchassisIndex_Object = MibTableColumn
systemResourceIOPortchassisIndex = _SystemResourceIOPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 1),
    _SystemResourceIOPortchassisIndex_Type()
)
systemResourceIOPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortchassisIndex.setDescription("""\
0500.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemResourceIOPortIndex_Type = DellObjectRange
_SystemResourceIOPortIndex_Object = MibTableColumn
systemResourceIOPortIndex = _SystemResourceIOPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 2),
    _SystemResourceIOPortIndex_Type()
)
systemResourceIOPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortIndex.setDescription("""\
0500.0030.0001.0002 This attribute defines the index of Dell System Resource IO
Ports in this chassis.
""")
_SystemResourceIOPortStateCapabilities_Type = DellStateCapabilities
_SystemResourceIOPortStateCapabilities_Object = MibTableColumn
systemResourceIOPortStateCapabilities = _SystemResourceIOPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 3),
    _SystemResourceIOPortStateCapabilities_Type()
)
systemResourceIOPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortStateCapabilities.setDescription("""\
0500.0030.0001.0003 This attribute defines the capabilities of this System
Resource IO Port.
""")
_SystemResourceIOPortStateSettings_Type = DellStateSettings
_SystemResourceIOPortStateSettings_Object = MibTableColumn
systemResourceIOPortStateSettings = _SystemResourceIOPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 4),
    _SystemResourceIOPortStateSettings_Type()
)
systemResourceIOPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResourceIOPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortStateSettings.setDescription("""\
0500.0030.0001.0004 This attribute defines the state of this System Resource IO
Port.
""")
_SystemResourceIOPortStatus_Type = DellStatus
_SystemResourceIOPortStatus_Object = MibTableColumn
systemResourceIOPortStatus = _SystemResourceIOPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 5),
    _SystemResourceIOPortStatus_Type()
)
systemResourceIOPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortStatus.setDescription("""\
0500.0030.0001.0005 This attribute defines the status of this System Resource
IO Port.
""")
_SystemResourceIOPortOwnerIndexReference_Type = DellObjectRange
_SystemResourceIOPortOwnerIndexReference_Object = MibTableColumn
systemResourceIOPortOwnerIndexReference = _SystemResourceIOPortOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 6),
    _SystemResourceIOPortOwnerIndexReference_Type()
)
systemResourceIOPortOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortOwnerIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortOwnerIndexReference.setDescription("""\
0500.0030.0001.0006 This attribute defines the index to the associated Dell
System Resource Owner in this chassis.
""")
_SystemResourceIOPortShareDisposition_Type = DellResourceShareDisposition
_SystemResourceIOPortShareDisposition_Object = MibTableColumn
systemResourceIOPortShareDisposition = _SystemResourceIOPortShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 7),
    _SystemResourceIOPortShareDisposition_Type()
)
systemResourceIOPortShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortShareDisposition.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortShareDisposition.setDescription("""\
0500.0030.0001.0007 This attribute defines the share disposition of the Dell
System Resource IO Port.
""")
_SystemResourceIOPortStartingAddress_Type = DellUnsigned64BitRange
_SystemResourceIOPortStartingAddress_Object = MibTableColumn
systemResourceIOPortStartingAddress = _SystemResourceIOPortStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 8),
    _SystemResourceIOPortStartingAddress_Type()
)
systemResourceIOPortStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortStartingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortStartingAddress.setDescription("""\
0500.0030.0001.0008 This attribute defines the sixty-four bits of the starting
address of the Dell System Resource IO Port.
""")
_SystemResourceIOPortEndingAddress_Type = DellUnsigned64BitRange
_SystemResourceIOPortEndingAddress_Object = MibTableColumn
systemResourceIOPortEndingAddress = _SystemResourceIOPortEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 30, 1, 9),
    _SystemResourceIOPortEndingAddress_Type()
)
systemResourceIOPortEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceIOPortEndingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceIOPortEndingAddress.setDescription("""\
0500.0030.0001.0009 This attribute defines the sixty-four bits of the ending
address of the Dell System Resource IO Port.
""")
_SystemResourceMemoryTable_Object = MibTable
systemResourceMemoryTable = _SystemResourceMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40)
)
if mibBuilder.loadTexts:
    systemResourceMemoryTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryTable.setDescription("""\
0500.0040 This Group defines the Dell System Resource Memory Table.
""")
_SystemResourceMemoryTableEntry_Object = MibTableRow
systemResourceMemoryTableEntry = _SystemResourceMemoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1)
)
systemResourceMemoryTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceMemorychassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceMemoryIndex"),
)
if mibBuilder.loadTexts:
    systemResourceMemoryTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryTableEntry.setDescription("""\
0500.0040.0001 This Group defines the Dell System Resource Memory Table Entry.
""")
_SystemResourceMemorychassisIndex_Type = DellObjectRange
_SystemResourceMemorychassisIndex_Object = MibTableColumn
systemResourceMemorychassisIndex = _SystemResourceMemorychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 1),
    _SystemResourceMemorychassisIndex_Type()
)
systemResourceMemorychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemorychassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemorychassisIndex.setDescription("""\
0500.0040.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemResourceMemoryIndex_Type = DellObjectRange
_SystemResourceMemoryIndex_Object = MibTableColumn
systemResourceMemoryIndex = _SystemResourceMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 2),
    _SystemResourceMemoryIndex_Type()
)
systemResourceMemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryIndex.setDescription("""\
0500.0040.0001.0002 This attribute defines the index of Dell System Resource
Memories in this chassis.
""")
_SystemResourceMemoryStateCapabilities_Type = DellStateCapabilities
_SystemResourceMemoryStateCapabilities_Object = MibTableColumn
systemResourceMemoryStateCapabilities = _SystemResourceMemoryStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 3),
    _SystemResourceMemoryStateCapabilities_Type()
)
systemResourceMemoryStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryStateCapabilities.setDescription("""\
0500.0040.0001.0003 This attribute defines the capabilities of this System
Resource Memory.
""")
_SystemResourceMemoryStateSettings_Type = DellStateSettings
_SystemResourceMemoryStateSettings_Object = MibTableColumn
systemResourceMemoryStateSettings = _SystemResourceMemoryStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 4),
    _SystemResourceMemoryStateSettings_Type()
)
systemResourceMemoryStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResourceMemoryStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryStateSettings.setDescription("""\
0500.0040.0001.0004 This attribute defines the state of this System Resource
Memory.
""")
_SystemResourceMemoryStatus_Type = DellStatus
_SystemResourceMemoryStatus_Object = MibTableColumn
systemResourceMemoryStatus = _SystemResourceMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 5),
    _SystemResourceMemoryStatus_Type()
)
systemResourceMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryStatus.setDescription("""\
0500.0040.0001.0005 This attribute defines the status of this System Resource
Memory.
""")
_SystemResourceMemoryOwnerIndexReference_Type = DellObjectRange
_SystemResourceMemoryOwnerIndexReference_Object = MibTableColumn
systemResourceMemoryOwnerIndexReference = _SystemResourceMemoryOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 6),
    _SystemResourceMemoryOwnerIndexReference_Type()
)
systemResourceMemoryOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryOwnerIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryOwnerIndexReference.setDescription("""\
0500.0040.0001.0006 This attribute defines the index to the associated Dell
System Resource Owner in this chassis.
""")
_SystemResourceMemoryShareDisposition_Type = DellResourceShareDisposition
_SystemResourceMemoryShareDisposition_Object = MibTableColumn
systemResourceMemoryShareDisposition = _SystemResourceMemoryShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 7),
    _SystemResourceMemoryShareDisposition_Type()
)
systemResourceMemoryShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryShareDisposition.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryShareDisposition.setDescription("""\
0500.0040.0001.0007 This attribute defines the share disposition of the Dell
System Resource Memory.
""")
_SystemResourceMemoryStartingAddress_Type = DellUnsigned64BitRange
_SystemResourceMemoryStartingAddress_Object = MibTableColumn
systemResourceMemoryStartingAddress = _SystemResourceMemoryStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 8),
    _SystemResourceMemoryStartingAddress_Type()
)
systemResourceMemoryStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryStartingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryStartingAddress.setDescription("""\
0500.0040.0001.0008 This attribute defines the sixty-four bits of the starting
address of the Dell System Resource Memory.
""")
_SystemResourceMemoryEndingAddress_Type = DellUnsigned64BitRange
_SystemResourceMemoryEndingAddress_Object = MibTableColumn
systemResourceMemoryEndingAddress = _SystemResourceMemoryEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 9),
    _SystemResourceMemoryEndingAddress_Type()
)
systemResourceMemoryEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryEndingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryEndingAddress.setDescription("""\
0500.0040.0001.0009 This attribute defines the sixty-four bits of the ending
address of the Dell System Resource Memory.
""")
_SystemResourceMemoryFlags_Type = DellResourceMemoryFlags
_SystemResourceMemoryFlags_Object = MibTableColumn
systemResourceMemoryFlags = _SystemResourceMemoryFlags_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 40, 1, 10),
    _SystemResourceMemoryFlags_Type()
)
systemResourceMemoryFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceMemoryFlags.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceMemoryFlags.setDescription("""\
0500.0040.0001.0010 This attribute defines the permission flags of the Dell
System Resource Memory.
""")
_SystemResourceInterruptTable_Object = MibTable
systemResourceInterruptTable = _SystemResourceInterruptTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50)
)
if mibBuilder.loadTexts:
    systemResourceInterruptTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptTable.setDescription("""\
0500.0050 This Group defines the Dell System Resource Interrupts Table.
""")
_SystemResourceInterruptTableEntry_Object = MibTableRow
systemResourceInterruptTableEntry = _SystemResourceInterruptTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1)
)
systemResourceInterruptTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceInterruptchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceInterruptIndex"),
)
if mibBuilder.loadTexts:
    systemResourceInterruptTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptTableEntry.setDescription("""\
0500.0050.0001 This Group defines the Dell System Resource Interrupts Table
Entry.
""")
_SystemResourceInterruptchassisIndex_Type = DellObjectRange
_SystemResourceInterruptchassisIndex_Object = MibTableColumn
systemResourceInterruptchassisIndex = _SystemResourceInterruptchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 1),
    _SystemResourceInterruptchassisIndex_Type()
)
systemResourceInterruptchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptchassisIndex.setDescription("""\
0500.0050.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemResourceInterruptIndex_Type = DellObjectRange
_SystemResourceInterruptIndex_Object = MibTableColumn
systemResourceInterruptIndex = _SystemResourceInterruptIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 2),
    _SystemResourceInterruptIndex_Type()
)
systemResourceInterruptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptIndex.setDescription("""\
0500.0050.0001.0002 This attribute defines the index of Dell System Resource
Interrupts in this chassis.
""")
_SystemResourceInterruptStateCapabilities_Type = DellStateCapabilities
_SystemResourceInterruptStateCapabilities_Object = MibTableColumn
systemResourceInterruptStateCapabilities = _SystemResourceInterruptStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 3),
    _SystemResourceInterruptStateCapabilities_Type()
)
systemResourceInterruptStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptStateCapabilities.setDescription("""\
0500.0050.0001.0003 This attribute defines the capabilities of this System
Resource Interrupt.
""")
_SystemResourceInterruptStateSettings_Type = DellStateSettings
_SystemResourceInterruptStateSettings_Object = MibTableColumn
systemResourceInterruptStateSettings = _SystemResourceInterruptStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 4),
    _SystemResourceInterruptStateSettings_Type()
)
systemResourceInterruptStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResourceInterruptStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptStateSettings.setDescription("""\
0500.0050.0001.0004 This attribute defines the state of this System Resource
Interrupt.
""")
_SystemResourceInterruptStatus_Type = DellStatus
_SystemResourceInterruptStatus_Object = MibTableColumn
systemResourceInterruptStatus = _SystemResourceInterruptStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 5),
    _SystemResourceInterruptStatus_Type()
)
systemResourceInterruptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptStatus.setDescription("""\
0500.0050.0001.0005 This attribute defines the status of this System Resource
Interrupt.
""")
_SystemResourceInterruptOwnerIndexReference_Type = DellObjectRange
_SystemResourceInterruptOwnerIndexReference_Object = MibTableColumn
systemResourceInterruptOwnerIndexReference = _SystemResourceInterruptOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 6),
    _SystemResourceInterruptOwnerIndexReference_Type()
)
systemResourceInterruptOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptOwnerIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptOwnerIndexReference.setDescription("""\
0500.0050.0001.0006 This attribute defines the index to the associated Dell
System Resource Owner in this chassis.
""")
_SystemResourceInterruptShareDisposition_Type = DellResourceShareDisposition
_SystemResourceInterruptShareDisposition_Object = MibTableColumn
systemResourceInterruptShareDisposition = _SystemResourceInterruptShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 7),
    _SystemResourceInterruptShareDisposition_Type()
)
systemResourceInterruptShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptShareDisposition.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptShareDisposition.setDescription("""\
0500.0050.0001.0007 This attribute defines the share disposition of the Dell
System Resource Interrupt.
""")
_SystemResourceInterruptLevel_Type = DellUnsigned32BitRange
_SystemResourceInterruptLevel_Object = MibTableColumn
systemResourceInterruptLevel = _SystemResourceInterruptLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 8),
    _SystemResourceInterruptLevel_Type()
)
systemResourceInterruptLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptLevel.setDescription("""\
0500.0050.0001.0008 This attribute defines the interrupt request level (IRQ) of
the Dell System Resource Interrupt.
""")
_SystemResourceInterruptType_Type = DellResourceInterruptType
_SystemResourceInterruptType_Object = MibTableColumn
systemResourceInterruptType = _SystemResourceInterruptType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 9),
    _SystemResourceInterruptType_Type()
)
systemResourceInterruptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptType.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptType.setDescription("""\
0500.0050.0001.0009 This attribute defines the interrupt type of the Dell
System Resource Interrupt.
""")
_SystemResourceInterruptTrigger_Type = DellResourceInterruptTrigger
_SystemResourceInterruptTrigger_Object = MibTableColumn
systemResourceInterruptTrigger = _SystemResourceInterruptTrigger_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 50, 1, 10),
    _SystemResourceInterruptTrigger_Type()
)
systemResourceInterruptTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceInterruptTrigger.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceInterruptTrigger.setDescription("""\
0500.0050.0001.0010 This attribute defines the interrupt trigger of the Dell
System Resource Interrupt.
""")
_SystemResourceDMATable_Object = MibTable
systemResourceDMATable = _SystemResourceDMATable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60)
)
if mibBuilder.loadTexts:
    systemResourceDMATable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMATable.setDescription("""\
0500.0060 This Group defines the Dell System Resource DMA Table.
""")
_SystemResourceDMATableEntry_Object = MibTableRow
systemResourceDMATableEntry = _SystemResourceDMATableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1)
)
systemResourceDMATableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemResourceDMAchassisIndex"),
    (0, "MIB-Dell-10892", "systemResourceDMAIndex"),
)
if mibBuilder.loadTexts:
    systemResourceDMATableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMATableEntry.setDescription("""\
0500.0060.0001 This Group defines the Dell System Resource DMA Table Entry.
""")
_SystemResourceDMAchassisIndex_Type = DellObjectRange
_SystemResourceDMAchassisIndex_Object = MibTableColumn
systemResourceDMAchassisIndex = _SystemResourceDMAchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 1),
    _SystemResourceDMAchassisIndex_Type()
)
systemResourceDMAchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAchassisIndex.setDescription("""\
0500.0060.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemResourceDMAIndex_Type = DellObjectRange
_SystemResourceDMAIndex_Object = MibTableColumn
systemResourceDMAIndex = _SystemResourceDMAIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 2),
    _SystemResourceDMAIndex_Type()
)
systemResourceDMAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAIndex.setDescription("""\
0500.0060.0001.0002 This attribute defines the index of Dell System Resource
DMAs in this chassis.
""")
_SystemResourceDMAStateCapabilities_Type = DellStateCapabilities
_SystemResourceDMAStateCapabilities_Object = MibTableColumn
systemResourceDMAStateCapabilities = _SystemResourceDMAStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 3),
    _SystemResourceDMAStateCapabilities_Type()
)
systemResourceDMAStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAStateCapabilities.setDescription("""\
0500.0060.0001.0003 This attribute defines the capabilities of this System
Resource DMA.
""")
_SystemResourceDMAStateSettings_Type = DellStateSettings
_SystemResourceDMAStateSettings_Object = MibTableColumn
systemResourceDMAStateSettings = _SystemResourceDMAStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 4),
    _SystemResourceDMAStateSettings_Type()
)
systemResourceDMAStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResourceDMAStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAStateSettings.setDescription("""\
0500.0060.0001.0004 This attribute defines the state of this System Resource
DMA.
""")
_SystemResourceDMAStatus_Type = DellStatus
_SystemResourceDMAStatus_Object = MibTableColumn
systemResourceDMAStatus = _SystemResourceDMAStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 5),
    _SystemResourceDMAStatus_Type()
)
systemResourceDMAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAStatus.setDescription("""\
0500.0060.0001.0005 This attribute defines the status of this System Resource
DMA.
""")
_SystemResourceDMAOwnerIndexReference_Type = DellObjectRange
_SystemResourceDMAOwnerIndexReference_Object = MibTableColumn
systemResourceDMAOwnerIndexReference = _SystemResourceDMAOwnerIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 6),
    _SystemResourceDMAOwnerIndexReference_Type()
)
systemResourceDMAOwnerIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAOwnerIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAOwnerIndexReference.setDescription("""\
0500.0060.0001.0006 This attribute defines the index to the associated Dell
System Resource Owner in this chassis.
""")
_SystemResourceDMAShareDisposition_Type = DellResourceShareDisposition
_SystemResourceDMAShareDisposition_Object = MibTableColumn
systemResourceDMAShareDisposition = _SystemResourceDMAShareDisposition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 7),
    _SystemResourceDMAShareDisposition_Type()
)
systemResourceDMAShareDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAShareDisposition.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAShareDisposition.setDescription("""\
0500.0060.0001.0007 This attribute defines the share disposition of the Dell
System Resource DMA.
""")
_SystemResourceDMAMaximumTransferSize_Type = DellUnsigned32BitRange
_SystemResourceDMAMaximumTransferSize_Object = MibTableColumn
systemResourceDMAMaximumTransferSize = _SystemResourceDMAMaximumTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 8),
    _SystemResourceDMAMaximumTransferSize_Type()
)
systemResourceDMAMaximumTransferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMAMaximumTransferSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMAMaximumTransferSize.setDescription("""\
0500.0060.0001.0008 This attribute defines the maximum size of a memory
transfer in bytes for the Dell System Resource DMA.
""")
_SystemResourceDMATransferWidth_Type = DellResourceDMATransferWidth
_SystemResourceDMATransferWidth_Object = MibTableColumn
systemResourceDMATransferWidth = _SystemResourceDMATransferWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 9),
    _SystemResourceDMATransferWidth_Type()
)
systemResourceDMATransferWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMATransferWidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMATransferWidth.setDescription("""\
0500.0060.0001.0009 This attribute defines the tranfer width of the Dell System
Resource DMA.
""")
_SystemResourceDMABusMaster_Type = DellResourceDMABusMaster
_SystemResourceDMABusMaster_Object = MibTableColumn
systemResourceDMABusMaster = _SystemResourceDMABusMaster_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 500, 60, 1, 10),
    _SystemResourceDMABusMaster_Type()
)
systemResourceDMABusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemResourceDMABusMaster.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemResourceDMABusMaster.setDescription("""\
0500.0060.0001.0010 This attribute defines the bus mastering capabilities of
the Dell System Resource DMA.
""")
_PowerGroup_ObjectIdentity = ObjectIdentity
powerGroup = _PowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600)
)
_PowerUnitTable_Object = MibTable
powerUnitTable = _PowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10)
)
if mibBuilder.loadTexts:
    powerUnitTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitTable.setDescription("""\
0600.0010 This Group defines the Dell Power Unit Table.
""")
_PowerUnitTableEntry_Object = MibTableRow
powerUnitTableEntry = _PowerUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1)
)
powerUnitTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "powerUnitchassisIndex"),
    (0, "MIB-Dell-10892", "powerUnitIndex"),
)
if mibBuilder.loadTexts:
    powerUnitTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitTableEntry.setDescription("""\
0600.0010.0001 This Group defines the Dell Power Unit Table Entry.
""")
_PowerUnitchassisIndex_Type = DellObjectRange
_PowerUnitchassisIndex_Object = MibTableColumn
powerUnitchassisIndex = _PowerUnitchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 1),
    _PowerUnitchassisIndex_Type()
)
powerUnitchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitchassisIndex.setDescription("""\
0600.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PowerUnitIndex_Type = DellObjectRange
_PowerUnitIndex_Object = MibTableColumn
powerUnitIndex = _PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 2),
    _PowerUnitIndex_Type()
)
powerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitIndex.setDescription("""\
0600.0010.0001.0002 This defines the index (one based) of a Dell power units.
""")
_PowerUnitStateCapabilities_Type = DellStateCapabilities
_PowerUnitStateCapabilities_Object = MibTableColumn
powerUnitStateCapabilities = _PowerUnitStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 3),
    _PowerUnitStateCapabilities_Type()
)
powerUnitStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitStateCapabilities.setDescription("""\
0600.0010.0001.0003 This attribute defines the capabilities of the Dell power
unit.
""")
_PowerUnitStateSettings_Type = DellStateSettings
_PowerUnitStateSettings_Object = MibTableColumn
powerUnitStateSettings = _PowerUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 4),
    _PowerUnitStateSettings_Type()
)
powerUnitStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerUnitStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitStateSettings.setDescription("""\
0600.0010.0001.0004 This attribute defines the state of the Dell power unit.
""")
_PowerUnitRedundancyStatus_Type = DellStatusRedundancy
_PowerUnitRedundancyStatus_Object = MibTableColumn
powerUnitRedundancyStatus = _PowerUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 5),
    _PowerUnitRedundancyStatus_Type()
)
powerUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitRedundancyStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitRedundancyStatus.setDescription("""\
0600.0010.0001.0005 This attribute defines the redundancy status of the Dell
power unit.
""")
_PowerSupplyCountForRedundancy_Type = DellObjectRange
_PowerSupplyCountForRedundancy_Object = MibTableColumn
powerSupplyCountForRedundancy = _PowerSupplyCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 6),
    _PowerSupplyCountForRedundancy_Type()
)
powerSupplyCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyCountForRedundancy.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyCountForRedundancy.setDescription("""\
0600.0010.0001.0006 This attribute defines the total number of Dell power
supplies required for this power unit to have redundancy.
""")
_PowerUnitName_Type = DellString
_PowerUnitName_Object = MibTableColumn
powerUnitName = _PowerUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 10, 1, 7),
    _PowerUnitName_Type()
)
powerUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitName.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerUnitName.setDescription("""\
0600.0010.0001.0007 This is the name of the Dell power unit in this chassis.
""")
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyTable.setDescription("""\
0600.0012 This Group defines the Dell Power Supply Table.
""")
_PowerSupplyTableEntry_Object = MibTableRow
powerSupplyTableEntry = _PowerSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1)
)
powerSupplyTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "powerSupplychassisIndex"),
    (0, "MIB-Dell-10892", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyTableEntry.setDescription("""\
0600.0012.0001 This Group defines the Dell Power Supply Table Entry.
""")
_PowerSupplychassisIndex_Type = DellObjectRange
_PowerSupplychassisIndex_Object = MibTableColumn
powerSupplychassisIndex = _PowerSupplychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 1),
    _PowerSupplychassisIndex_Type()
)
powerSupplychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplychassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplychassisIndex.setDescription("""\
0600.0012.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PowerSupplyIndex_Type = DellObjectRange
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 2),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyIndex.setDescription("""\
0600.0012.0001.0002 This attribute defines the index of Dell power supply.
""")
_PowerSupplyStateCapabilitiesUnique_Type = DellPowerSupplyStateCapabilitiesUnique
_PowerSupplyStateCapabilitiesUnique_Object = MibTableColumn
powerSupplyStateCapabilitiesUnique = _PowerSupplyStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 3),
    _PowerSupplyStateCapabilitiesUnique_Type()
)
powerSupplyStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStateCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyStateCapabilitiesUnique.setDescription("""\
0600.0012.0001.0003 This attribute defines the capabilities of the Dell power
supply.
""")
_PowerSupplyStateSettingsUnique_Type = DellPowerSupplyStateSettingsUnique
_PowerSupplyStateSettingsUnique_Object = MibTableColumn
powerSupplyStateSettingsUnique = _PowerSupplyStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 4),
    _PowerSupplyStateSettingsUnique_Type()
)
powerSupplyStateSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupplyStateSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyStateSettingsUnique.setDescription("""\
0600.0012.0001.0004 This attribute defines the state of the Dell power supply.
""")
_PowerSupplyStatus_Type = DellStatus
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 5),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyStatus.setDescription("""\
0600.0012.0001.0005 This attribute defines the status of the Dell power supply.
""")
_PowerSupplyOutputWatts_Type = DellSigned32BitRange
_PowerSupplyOutputWatts_Object = MibTableColumn
powerSupplyOutputWatts = _PowerSupplyOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 6),
    _PowerSupplyOutputWatts_Type()
)
powerSupplyOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyOutputWatts.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyOutputWatts.setDescription("""\
0600.0012.0001.0006 This attribute defines the maximum sustained output wattage
of the power supply, in tenths of watts.
""")
_PowerSupplyType_Type = DellPowerSupplyType
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 7),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyType.setDescription("""\
0600.0012.0001.0007 This attribute defines the type of Dell power supply.
""")
_PowerSupplyLocationName_Type = DellString
_PowerSupplyLocationName_Object = MibTableColumn
powerSupplyLocationName = _PowerSupplyLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 8),
    _PowerSupplyLocationName_Type()
)
powerSupplyLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyLocationName.setDescription("""\
0600.0012.0001.0008 This attribute defines the location name of the power
supply.
""")
_PowerSupplyInputVoltage_Type = DellSigned32BitRange
_PowerSupplyInputVoltage_Object = MibTableColumn
powerSupplyInputVoltage = _PowerSupplyInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 9),
    _PowerSupplyInputVoltage_Type()
)
powerSupplyInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyInputVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplyInputVoltage.setDescription("""\
0600.0012.0001.0009 This attribute defines the input voltage to the power
supply, in volts.
""")
_PowerSupplypowerUnitIndexReference_Type = DellObjectRange
_PowerSupplypowerUnitIndexReference_Object = MibTableColumn
powerSupplypowerUnitIndexReference = _PowerSupplypowerUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 12, 1, 10),
    _PowerSupplypowerUnitIndexReference_Type()
)
powerSupplypowerUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplypowerUnitIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerSupplypowerUnitIndexReference.setDescription("""\
0600.0012.0001.0010 This attribute defines the index to the associated Dell
System Power Unit in this chassis.
""")
_VoltageProbeTable_Object = MibTable
voltageProbeTable = _VoltageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20)
)
if mibBuilder.loadTexts:
    voltageProbeTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeTable.setDescription("""\
0600.0020 This Group defines the Dell Voltage Probe Table.
""")
_VoltageProbeTableEntry_Object = MibTableRow
voltageProbeTableEntry = _VoltageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1)
)
voltageProbeTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "voltageProbechassisIndex"),
    (0, "MIB-Dell-10892", "voltageProbeIndex"),
)
if mibBuilder.loadTexts:
    voltageProbeTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeTableEntry.setDescription("""\
0600.0020.001 This Group defines the Dell Voltage Probe Table Entry.
""")
_VoltageProbechassisIndex_Type = DellObjectRange
_VoltageProbechassisIndex_Object = MibTableColumn
voltageProbechassisIndex = _VoltageProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 1),
    _VoltageProbechassisIndex_Type()
)
voltageProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbechassisIndex.setDescription("""\
0600.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_VoltageProbeIndex_Type = DellObjectRange
_VoltageProbeIndex_Object = MibTableColumn
voltageProbeIndex = _VoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 2),
    _VoltageProbeIndex_Type()
)
voltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeIndex.setDescription("""\
0600.0020.0001.0002 This attribute defines the index of Dell voltage probes in
this chassis.
""")
_VoltageProbeStateCapabilities_Type = DellStateCapabilities
_VoltageProbeStateCapabilities_Object = MibTableColumn
voltageProbeStateCapabilities = _VoltageProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 3),
    _VoltageProbeStateCapabilities_Type()
)
voltageProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeStateCapabilities.setDescription("""\
0600.0020.0001.0003 This attribute defines the capabilities of the Dell voltage
probe.
""")
_VoltageProbeStateSettings_Type = DellStateSettings
_VoltageProbeStateSettings_Object = MibTableColumn
voltageProbeStateSettings = _VoltageProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 4),
    _VoltageProbeStateSettings_Type()
)
voltageProbeStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageProbeStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeStateSettings.setDescription("""\
0600.0020.0001.0004 This attribute defines the state of the Dell voltage probe.
""")
_VoltageProbeStatus_Type = DellStatusProbe
_VoltageProbeStatus_Object = MibTableColumn
voltageProbeStatus = _VoltageProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 5),
    _VoltageProbeStatus_Type()
)
voltageProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeStatus.setDescription("""\
0600.0020.0001.0005 This attribute defines the status of the Dell voltage
probe.
""")
_VoltageProbeReading_Type = DellSigned32BitRange
_VoltageProbeReading_Object = MibTableColumn
voltageProbeReading = _VoltageProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 6),
    _VoltageProbeReading_Type()
)
voltageProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeReading.setDescription("""\
0600.0020.0001.0006 This attribute defines the value of the Dell voltage probe.
The value is an integer representing the voltage the probe is reading in
millivolts.
""")
_VoltageProbeType_Type = DellVoltageType
_VoltageProbeType_Object = MibTableColumn
voltageProbeType = _VoltageProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 7),
    _VoltageProbeType_Type()
)
voltageProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeType.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeType.setDescription("""\
0600.0020.0001.0007 This attribute defines the subtype of the Dell voltage
probe.
""")
_VoltageProbeLocationName_Type = DellString
_VoltageProbeLocationName_Object = MibTableColumn
voltageProbeLocationName = _VoltageProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 8),
    _VoltageProbeLocationName_Type()
)
voltageProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeLocationName.setDescription("""\
0600.0020.0001.0008 This attribute defines the location of the voltage probe in
this chassis.
""")
_VoltageProbeUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_VoltageProbeUpperNonRecoverableThreshold_Object = MibTableColumn
voltageProbeUpperNonRecoverableThreshold = _VoltageProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 9),
    _VoltageProbeUpperNonRecoverableThreshold_Type()
)
voltageProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeUpperNonRecoverableThreshold.setDescription("""\
0600.0020.0001.0009 This attribute defines the value of the Dell voltage probes
upper nonrecoverable threshold. The value is an integer representing the
voltage the probe is reading in millivolts.
""")
_VoltageProbeUpperCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeUpperCriticalThreshold_Object = MibTableColumn
voltageProbeUpperCriticalThreshold = _VoltageProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 10),
    _VoltageProbeUpperCriticalThreshold_Type()
)
voltageProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeUpperCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeUpperCriticalThreshold.setDescription("""\
0600.0020.0001.0010 This attribute defines the value of the Dell voltage probes
upper critical threshold. The value is an integer representing the voltage the
probe is reading in millivolts.
""")
_VoltageProbeUpperNonCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeUpperNonCriticalThreshold_Object = MibTableColumn
voltageProbeUpperNonCriticalThreshold = _VoltageProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 11),
    _VoltageProbeUpperNonCriticalThreshold_Type()
)
voltageProbeUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageProbeUpperNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeUpperNonCriticalThreshold.setDescription("""\
0600.0020.0001.0011 This attribute defines the value of the Dell voltage probes
upper noncritical threshold. The value is an integer representing the voltage
the probe is reading in millivolts.
""")
_VoltageProbeLowerNonCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeLowerNonCriticalThreshold_Object = MibTableColumn
voltageProbeLowerNonCriticalThreshold = _VoltageProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 12),
    _VoltageProbeLowerNonCriticalThreshold_Type()
)
voltageProbeLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageProbeLowerNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeLowerNonCriticalThreshold.setDescription("""\
0600.0020.0001.0012 This attribute defines the value of the Dell voltage probes
lower noncritical threshold. The value is an integer representing the voltage
the probe is reading in millivolts.
""")
_VoltageProbeLowerCriticalThreshold_Type = DellSigned32BitRange
_VoltageProbeLowerCriticalThreshold_Object = MibTableColumn
voltageProbeLowerCriticalThreshold = _VoltageProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 13),
    _VoltageProbeLowerCriticalThreshold_Type()
)
voltageProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeLowerCriticalThreshold.setDescription("""\
0600.0020.0001.0013 This attribute defines the value of the Dell voltage probes
lower critical threshold. The value is an integer representing the voltage the
probe is reading in millivolts.
""")
_VoltageProbeLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_VoltageProbeLowerNonRecoverableThreshold_Object = MibTableColumn
voltageProbeLowerNonRecoverableThreshold = _VoltageProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 20, 1, 14),
    _VoltageProbeLowerNonRecoverableThreshold_Type()
)
voltageProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageProbeLowerNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltageProbeLowerNonRecoverableThreshold.setDescription("""\
0600.0020.0001.0014 This attribute defines the value of the Dell voltage probes
lower nonrecoverable threshold. The value is an integer representing the
voltage the probe is reading in millivolts.
""")
_AmperageProbeTable_Object = MibTable
amperageProbeTable = _AmperageProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30)
)
if mibBuilder.loadTexts:
    amperageProbeTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeTable.setDescription("""\
0600.0030 This Group defines the Dell Amperage Probe Table.
""")
_AmperageProbeTableEntry_Object = MibTableRow
amperageProbeTableEntry = _AmperageProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1)
)
amperageProbeTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "amperageProbechassisIndex"),
    (0, "MIB-Dell-10892", "amperageProbeIndex"),
)
if mibBuilder.loadTexts:
    amperageProbeTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeTableEntry.setDescription("""\
0600.0030.0001 This Group defines the Dell Amperage Probe Table Entry.
""")
_AmperageProbechassisIndex_Type = DellObjectRange
_AmperageProbechassisIndex_Object = MibTableColumn
amperageProbechassisIndex = _AmperageProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 1),
    _AmperageProbechassisIndex_Type()
)
amperageProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbechassisIndex.setDescription("""\
0600.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_AmperageProbeIndex_Type = DellObjectRange
_AmperageProbeIndex_Object = MibTableColumn
amperageProbeIndex = _AmperageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 2),
    _AmperageProbeIndex_Type()
)
amperageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeIndex.setDescription("""\
0600.0030.0001.0002 This attribute defines the index of Dell amperage probes in
this chassis.
""")
_AmperageProbeStateCapabilities_Type = DellStateCapabilities
_AmperageProbeStateCapabilities_Object = MibTableColumn
amperageProbeStateCapabilities = _AmperageProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 3),
    _AmperageProbeStateCapabilities_Type()
)
amperageProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeStateCapabilities.setDescription("""\
0600.0030.0001.0003 This attribute defines the capabilities of the Dell
amperage probe.
""")
_AmperageProbeStateSettings_Type = DellStateSettings
_AmperageProbeStateSettings_Object = MibTableColumn
amperageProbeStateSettings = _AmperageProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 4),
    _AmperageProbeStateSettings_Type()
)
amperageProbeStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperageProbeStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeStateSettings.setDescription("""\
0600.0030.0001.0004 This attribute defines the state of the Dell amperage
probe.
""")
_AmperageProbeStatus_Type = DellStatusProbe
_AmperageProbeStatus_Object = MibTableColumn
amperageProbeStatus = _AmperageProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 5),
    _AmperageProbeStatus_Type()
)
amperageProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeStatus.setDescription("""\
0600.0030.0001.0005 This attribute defines the status of the Dell amperage
probe.
""")
_AmperageProbeReading_Type = DellSigned32BitRange
_AmperageProbeReading_Object = MibTableColumn
amperageProbeReading = _AmperageProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 6),
    _AmperageProbeReading_Type()
)
amperageProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeReading.setDescription("""\
0600.0030.0001.0006 This attribute defines the value of the Dell amperage
probe. The value is an integer representing the amperage the probe is reading
in milliamps.
""")
_AmperageProbeType_Type = DellAmperageProbeType
_AmperageProbeType_Object = MibTableColumn
amperageProbeType = _AmperageProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 7),
    _AmperageProbeType_Type()
)
amperageProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeType.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeType.setDescription("""\
0600.0030.0001.0007 This attribute defines the type of the Dell amperage probe.
""")
_AmperageProbeLocationName_Type = DellString
_AmperageProbeLocationName_Object = MibTableColumn
amperageProbeLocationName = _AmperageProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 8),
    _AmperageProbeLocationName_Type()
)
amperageProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeLocationName.setDescription("""\
0600.0030.0001.0008 This attribute defines the location name of the amperage
probe in this chassis.
""")
_AmperageProbeUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_AmperageProbeUpperNonRecoverableThreshold_Object = MibTableColumn
amperageProbeUpperNonRecoverableThreshold = _AmperageProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 9),
    _AmperageProbeUpperNonRecoverableThreshold_Type()
)
amperageProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeUpperNonRecoverableThreshold.setDescription("""\
0600.0030.0001.0009 This attribute defines the value of the Dell amperage
probes upper nonrecoverable threshold. The value is an integer representing the
amperage the probe is reading in milliamps.
""")
_AmperageProbeUpperCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeUpperCriticalThreshold_Object = MibTableColumn
amperageProbeUpperCriticalThreshold = _AmperageProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 10),
    _AmperageProbeUpperCriticalThreshold_Type()
)
amperageProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeUpperCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeUpperCriticalThreshold.setDescription("""\
0600.0030.0001.0010 This attribute defines the value of the Dell amperage
probes upper critical threshold. The value is an integer representing the
amperage the probe is reading in milliamps.
""")
_AmperageProbeUpperNonCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeUpperNonCriticalThreshold_Object = MibTableColumn
amperageProbeUpperNonCriticalThreshold = _AmperageProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 11),
    _AmperageProbeUpperNonCriticalThreshold_Type()
)
amperageProbeUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperageProbeUpperNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeUpperNonCriticalThreshold.setDescription("""\
0600.0030.0001.0011 This attribute defines the value of the Dell amperage
probes upper noncritical threshold. The value is an integer representing the
amperage the probe is reading in milliamps.
""")
_AmperageProbeLowerNonCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeLowerNonCriticalThreshold_Object = MibTableColumn
amperageProbeLowerNonCriticalThreshold = _AmperageProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 12),
    _AmperageProbeLowerNonCriticalThreshold_Type()
)
amperageProbeLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amperageProbeLowerNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeLowerNonCriticalThreshold.setDescription("""\
0600.0030.0001.0012 This attribute defines the value of the Dell amperage
probes lower noncritical threshold. The value is an integer representing the
amperage the probe is reading in milliamps.
""")
_AmperageProbeLowerCriticalThreshold_Type = DellSigned32BitRange
_AmperageProbeLowerCriticalThreshold_Object = MibTableColumn
amperageProbeLowerCriticalThreshold = _AmperageProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 13),
    _AmperageProbeLowerCriticalThreshold_Type()
)
amperageProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeLowerCriticalThreshold.setDescription("""\
0600.0030.0001.0013 This attribute defines the value of the Dell amperage
probes lower critical threshold. The value is an integer representing the
amperage the probe is reading in milliamps.
""")
_AmperageProbeLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_AmperageProbeLowerNonRecoverableThreshold_Object = MibTableColumn
amperageProbeLowerNonRecoverableThreshold = _AmperageProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 30, 1, 14),
    _AmperageProbeLowerNonRecoverableThreshold_Type()
)
amperageProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amperageProbeLowerNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    amperageProbeLowerNonRecoverableThreshold.setDescription("""\
0600.0030.0001.0014 This attribute defines the value of the Dell amperage
probes lower nonrecoverable threshold. The value is an integer representing the
amperage the probe is reading in milliamps.
""")
_ACPowerSwitchTable_Object = MibTable
aCPowerSwitchTable = _ACPowerSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40)
)
if mibBuilder.loadTexts:
    aCPowerSwitchTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchTable.setDescription("""\
0600.0040 This Group defines the Dell AC Power Switch Table.
""")
_ACPowerSwitchTableEntry_Object = MibTableRow
aCPowerSwitchTableEntry = _ACPowerSwitchTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1)
)
aCPowerSwitchTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "aCPowerSwitchchassisIndex"),
    (0, "MIB-Dell-10892", "aCPowerSwitchIndex"),
)
if mibBuilder.loadTexts:
    aCPowerSwitchTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchTableEntry.setDescription("""\
0600.0040.0001 This Group defines the Dell AC Power Switch Table Entry.
""")
_ACPowerSwitchchassisIndex_Type = DellObjectRange
_ACPowerSwitchchassisIndex_Object = MibTableColumn
aCPowerSwitchchassisIndex = _ACPowerSwitchchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 1),
    _ACPowerSwitchchassisIndex_Type()
)
aCPowerSwitchchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchchassisIndex.setDescription("""\
0600.0040.0001.0001 This attribute defines the index (one based) of the chassis
containing this Dell AC power switch.
""")
_ACPowerSwitchIndex_Type = DellObjectRange
_ACPowerSwitchIndex_Object = MibTableColumn
aCPowerSwitchIndex = _ACPowerSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 2),
    _ACPowerSwitchIndex_Type()
)
aCPowerSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchIndex.setDescription("""\
0600.0040.0001.0002 This attribute defines the index (one based) of this Dell
AC power switch.
""")
_ACPowerSwitchCapabilities_Type = DellACPowerSwitchCapabilities
_ACPowerSwitchCapabilities_Object = MibTableColumn
aCPowerSwitchCapabilities = _ACPowerSwitchCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 3),
    _ACPowerSwitchCapabilities_Type()
)
aCPowerSwitchCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchCapabilities.setDescription("""\
0600.0040.0001.0003 This attribute defines the capabilities of this Dell AC
power switch.
""")
_ACPowerSwitchSettings_Type = DellACPowerSwitchSettings
_ACPowerSwitchSettings_Object = MibTableColumn
aCPowerSwitchSettings = _ACPowerSwitchSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 4),
    _ACPowerSwitchSettings_Type()
)
aCPowerSwitchSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aCPowerSwitchSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchSettings.setDescription("""\
0600.0040.0001.0004 This attribute defines the settings of this Dell AC power
switch.
""")
_ACPowerSwitchRedundancyStatus_Type = DellStatusRedundancy
_ACPowerSwitchRedundancyStatus_Object = MibTableColumn
aCPowerSwitchRedundancyStatus = _ACPowerSwitchRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 5),
    _ACPowerSwitchRedundancyStatus_Type()
)
aCPowerSwitchRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchRedundancyStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchRedundancyStatus.setDescription("""\
0600.0040.0001.0005 This attribute defines the redundancy status of this Dell
AC power switch.
""")
_ACPowerCordCountForRedundancy_Type = DellObjectRange
_ACPowerCordCountForRedundancy_Object = MibTableColumn
aCPowerCordCountForRedundancy = _ACPowerCordCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 6),
    _ACPowerCordCountForRedundancy_Type()
)
aCPowerCordCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordCountForRedundancy.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordCountForRedundancy.setDescription("""\
0600.0040.0001.0006 This attribute defines the total number of Dell AC power
cords required for this Dell AC power switch to have redundancy.
""")
_ACPowerSwitchName_Type = DellString
_ACPowerSwitchName_Object = MibTableColumn
aCPowerSwitchName = _ACPowerSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 7),
    _ACPowerSwitchName_Type()
)
aCPowerSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerSwitchName.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchName.setDescription("""\
0600.0040.0001.0007 This attribute defines the name of this Dell AC power
switch.
""")
_ACPowerSwitchRedundancyMode_Type = DellACPowerSwitchRedundancyMode
_ACPowerSwitchRedundancyMode_Object = MibTableColumn
aCPowerSwitchRedundancyMode = _ACPowerSwitchRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 40, 1, 8),
    _ACPowerSwitchRedundancyMode_Type()
)
aCPowerSwitchRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aCPowerSwitchRedundancyMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerSwitchRedundancyMode.setDescription("""\
0600.0040.0001.0008 This attribute defines the redundancy mode of this Dell AC
power switch.
""")
_ACPowerCordTable_Object = MibTable
aCPowerCordTable = _ACPowerCordTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42)
)
if mibBuilder.loadTexts:
    aCPowerCordTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordTable.setDescription("""\
0600.0042 This Group defines the Dell AC Power Cord Table.
""")
_ACPowerCordTableEntry_Object = MibTableRow
aCPowerCordTableEntry = _ACPowerCordTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1)
)
aCPowerCordTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "aCPowerCordchassisIndex"),
    (0, "MIB-Dell-10892", "aCPowerCordIndex"),
)
if mibBuilder.loadTexts:
    aCPowerCordTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordTableEntry.setDescription("""\
0600.0042.0001 This Group defines the Dell AC Power Cord Table Entry.
""")
_ACPowerCordchassisIndex_Type = DellObjectRange
_ACPowerCordchassisIndex_Object = MibTableColumn
aCPowerCordchassisIndex = _ACPowerCordchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 1),
    _ACPowerCordchassisIndex_Type()
)
aCPowerCordchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordchassisIndex.setDescription("""\
0600.0042.0001.0001 This attribute defines the index (one based) of the chassis
containing this Dell AC power cord.
""")
_ACPowerCordIndex_Type = DellObjectRange
_ACPowerCordIndex_Object = MibTableColumn
aCPowerCordIndex = _ACPowerCordIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 2),
    _ACPowerCordIndex_Type()
)
aCPowerCordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordIndex.setDescription("""\
0600.0042.0001.0002 This attribute defines the index (one based) of this Dell
AC power cord.
""")
_ACPowerCordStateCapabilities_Type = DellACPowerCordStateCapabilities
_ACPowerCordStateCapabilities_Object = MibTableColumn
aCPowerCordStateCapabilities = _ACPowerCordStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 3),
    _ACPowerCordStateCapabilities_Type()
)
aCPowerCordStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordStateCapabilities.setDescription("""\
0600.0042.0001.0003 This attribute defines the capabilities of this Dell AC
power cord.
""")
_ACPowerCordStateSettings_Type = DellACPowerCordStateSettings
_ACPowerCordStateSettings_Object = MibTableColumn
aCPowerCordStateSettings = _ACPowerCordStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 4),
    _ACPowerCordStateSettings_Type()
)
aCPowerCordStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aCPowerCordStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordStateSettings.setDescription("""\
0600.0042.0001.0004 This attribute defines the state of this Dell AC power
cord.
""")
_ACPowerCordStatus_Type = DellStatus
_ACPowerCordStatus_Object = MibTableColumn
aCPowerCordStatus = _ACPowerCordStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 5),
    _ACPowerCordStatus_Type()
)
aCPowerCordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordStatus.setDescription("""\
0600.0042.0001.0005 This attribute defines the status of this Dell AC power
cord.
""")
_ACPowerCordaCPowerSwitchIndexReference_Type = DellObjectRange
_ACPowerCordaCPowerSwitchIndexReference_Object = MibTableColumn
aCPowerCordaCPowerSwitchIndexReference = _ACPowerCordaCPowerSwitchIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 6),
    _ACPowerCordaCPowerSwitchIndexReference_Type()
)
aCPowerCordaCPowerSwitchIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordaCPowerSwitchIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordaCPowerSwitchIndexReference.setDescription("""\
0600.0042.0001.0006 This attribute defines the index (one based) to the
associated Dell AC power switch for this Dell AC power cord.
""")
_ACPowerCordLocationName_Type = DellString
_ACPowerCordLocationName_Object = MibTableColumn
aCPowerCordLocationName = _ACPowerCordLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 600, 42, 1, 7),
    _ACPowerCordLocationName_Type()
)
aCPowerCordLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCPowerCordLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    aCPowerCordLocationName.setDescription("""\
0600.0042.0001.0007 This attribute defines the location name of this Dell AC
power cord.
""")
_ThermalGroup_ObjectIdentity = ObjectIdentity
thermalGroup = _ThermalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700)
)
_CoolingUnitTable_Object = MibTable
coolingUnitTable = _CoolingUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10)
)
if mibBuilder.loadTexts:
    coolingUnitTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitTable.setDescription("""\
0700.0010 This Group defines the Dell Cooling Unit Table.
""")
_CoolingUnitTableEntry_Object = MibTableRow
coolingUnitTableEntry = _CoolingUnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1)
)
coolingUnitTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "coolingUnitchassisIndex"),
    (0, "MIB-Dell-10892", "coolingUnitIndex"),
)
if mibBuilder.loadTexts:
    coolingUnitTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitTableEntry.setDescription("""\
0700.0010.0001 This Group defines the Dell Cooling Unit Table Entry.
""")
_CoolingUnitchassisIndex_Type = DellObjectRange
_CoolingUnitchassisIndex_Object = MibTableColumn
coolingUnitchassisIndex = _CoolingUnitchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 1),
    _CoolingUnitchassisIndex_Type()
)
coolingUnitchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitchassisIndex.setDescription("""\
0700.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CoolingUnitIndex_Type = DellObjectRange
_CoolingUnitIndex_Object = MibTableColumn
coolingUnitIndex = _CoolingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 2),
    _CoolingUnitIndex_Type()
)
coolingUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitIndex.setDescription("""\
0700.0010.0001.0002 This defines the index (one based) of Dell cooling units.
""")
_CoolingUnitStateCapabilties_Type = DellStateCapabilities
_CoolingUnitStateCapabilties_Object = MibTableColumn
coolingUnitStateCapabilties = _CoolingUnitStateCapabilties_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 3),
    _CoolingUnitStateCapabilties_Type()
)
coolingUnitStateCapabilties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitStateCapabilties.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitStateCapabilties.setDescription("""\
0700.0010.0001.0003 This attribute defines the capabilities of the Dell cooling
unit.
""")
_CoolingUnitStateSettings_Type = DellStateSettings
_CoolingUnitStateSettings_Object = MibTableColumn
coolingUnitStateSettings = _CoolingUnitStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 4),
    _CoolingUnitStateSettings_Type()
)
coolingUnitStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingUnitStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitStateSettings.setDescription("""\
0700.0010.0001.0004 This attribute defines the state of the Dell cooling unit.
""")
_CoolingUnitRedundancyStatus_Type = DellStatusRedundancy
_CoolingUnitRedundancyStatus_Object = MibTableColumn
coolingUnitRedundancyStatus = _CoolingUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 5),
    _CoolingUnitRedundancyStatus_Type()
)
coolingUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitRedundancyStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitRedundancyStatus.setDescription("""\
0700.0010.0001.0005 This attribute defines the redundancy status of the Dell
cooling unit.
""")
_CoolingDeviceCountForRedundancy_Type = DellObjectRange
_CoolingDeviceCountForRedundancy_Object = MibTableColumn
coolingDeviceCountForRedundancy = _CoolingDeviceCountForRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 6),
    _CoolingDeviceCountForRedundancy_Type()
)
coolingDeviceCountForRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceCountForRedundancy.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceCountForRedundancy.setDescription("""\
0700.0010.0001.0006 This attribute defines the total number of Dell cooling
devices required for this cooling unit to have redundancy.
""")
_CoolingUnitName_Type = DellString
_CoolingUnitName_Object = MibTableColumn
coolingUnitName = _CoolingUnitName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 10, 1, 7),
    _CoolingUnitName_Type()
)
coolingUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingUnitName.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingUnitName.setDescription("""\
0700.0010.0001.0007 This is the name of the Dell cooling unit in this chassis.
""")
_CoolingDeviceTable_Object = MibTable
coolingDeviceTable = _CoolingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12)
)
if mibBuilder.loadTexts:
    coolingDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceTable.setDescription("""\
0700.0012 This Group defines the Dell Cooling Table.
""")
_CoolingDeviceTableEntry_Object = MibTableRow
coolingDeviceTableEntry = _CoolingDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1)
)
coolingDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "coolingDevicechassisIndex"),
    (0, "MIB-Dell-10892", "coolingDeviceIndex"),
)
if mibBuilder.loadTexts:
    coolingDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceTableEntry.setDescription("""\
0700.0012.0001 This Group defines the Dell Cooling Table Entry.
""")
_CoolingDevicechassisIndex_Type = DellObjectRange
_CoolingDevicechassisIndex_Object = MibTableColumn
coolingDevicechassisIndex = _CoolingDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 1),
    _CoolingDevicechassisIndex_Type()
)
coolingDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDevicechassisIndex.setDescription("""\
0700.0012.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CoolingDeviceIndex_Type = DellObjectRange
_CoolingDeviceIndex_Object = MibTableColumn
coolingDeviceIndex = _CoolingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 2),
    _CoolingDeviceIndex_Type()
)
coolingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceIndex.setDescription("""\
0700.0012.0001.0002 This attribute defines the index of Dell cooling device in
this chassis.
""")
_CoolingDeviceStateCapabilities_Type = DellStateCapabilities
_CoolingDeviceStateCapabilities_Object = MibTableColumn
coolingDeviceStateCapabilities = _CoolingDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 3),
    _CoolingDeviceStateCapabilities_Type()
)
coolingDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceStateCapabilities.setDescription("""\
0700.0012.0001.0003 This attribute defines the capabilities of the Dell cooling
device.
""")
_CoolingDeviceStateSettings_Type = DellStateSettings
_CoolingDeviceStateSettings_Object = MibTableColumn
coolingDeviceStateSettings = _CoolingDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 4),
    _CoolingDeviceStateSettings_Type()
)
coolingDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceStateSettings.setDescription("""\
0700.0012.0001.0004 This attribute defines the state of the Dell cooling
device.
""")
_CoolingDeviceStatus_Type = DellStatusProbe
_CoolingDeviceStatus_Object = MibTableColumn
coolingDeviceStatus = _CoolingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 5),
    _CoolingDeviceStatus_Type()
)
coolingDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceStatus.setDescription("""\
0700.0012.0001.0005 This attribute defines the status of the Dell cooling
device.
""")
_CoolingDeviceReading_Type = DellSigned32BitRange
_CoolingDeviceReading_Object = MibTableColumn
coolingDeviceReading = _CoolingDeviceReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 6),
    _CoolingDeviceReading_Type()
)
coolingDeviceReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceReading.setDescription("""\
0700.0012.0001.0006 This attribute defines the speed in RPM or the OFF/ON value
of the Dell fan.
""")
_CoolingDeviceType_Type = DellCoolingDeviceType
_CoolingDeviceType_Object = MibTableColumn
coolingDeviceType = _CoolingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 7),
    _CoolingDeviceType_Type()
)
coolingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceType.setDescription("""\
0700.0012.0001.0007 This attribute defines the type of the Dell cooling device.
""")
_CoolingDeviceLocationName_Type = DellString
_CoolingDeviceLocationName_Object = MibTableColumn
coolingDeviceLocationName = _CoolingDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 8),
    _CoolingDeviceLocationName_Type()
)
coolingDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceLocationName.setDescription("""\
0700.0012.0001.0008 This attribute defines the location of the cooling device
in this chassis.
""")
_CoolingDeviceUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_CoolingDeviceUpperNonRecoverableThreshold_Object = MibTableColumn
coolingDeviceUpperNonRecoverableThreshold = _CoolingDeviceUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 9),
    _CoolingDeviceUpperNonRecoverableThreshold_Type()
)
coolingDeviceUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonRecoverableThreshold.setDescription("""\
0700.0012.0001.0009 This attribute defines the value of the Dell fans upper
nonrecoverable threshold. The value is an integer representing fan speed in
revolutions per minute, it is not applicable to OFF/ON type fans or nonFan
types.
""")
_CoolingDeviceUpperCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceUpperCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperCriticalThreshold = _CoolingDeviceUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 10),
    _CoolingDeviceUpperCriticalThreshold_Type()
)
coolingDeviceUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceUpperCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceUpperCriticalThreshold.setDescription("""\
0700.0012.0001.0010 This attribute defines the value of the Dell fans upper
critical threshold. The value is an integer representing fan speed in
revolutions per minute, it is not applicable to OFF/ON type fans or nonFan
types.
""")
_CoolingDeviceUpperNonCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceUpperNonCriticalThreshold_Object = MibTableColumn
coolingDeviceUpperNonCriticalThreshold = _CoolingDeviceUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 11),
    _CoolingDeviceUpperNonCriticalThreshold_Type()
)
coolingDeviceUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceUpperNonCriticalThreshold.setDescription("""\
0700.0012.0001.0011 This attribute defines the value of the Dell fans upper
noncritical threshold. The value is an integer representing fan speed in
revolutions per minute, it is not applicable to OFF/ON type fans or nonFan
types.
""")
_CoolingDeviceLowerNonCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceLowerNonCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerNonCriticalThreshold = _CoolingDeviceLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 12),
    _CoolingDeviceLowerNonCriticalThreshold_Type()
)
coolingDeviceLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonCriticalThreshold.setDescription("""\
0700.0012.0001.0012 This attribute defines the value of the Dell fans lower
noncritical threshold. The value is an integer representing fan speed in
revolutions per minute, it is not applicable to OFF/ON type fans or nonFan
types.
""")
_CoolingDeviceLowerCriticalThreshold_Type = DellSigned32BitRange
_CoolingDeviceLowerCriticalThreshold_Object = MibTableColumn
coolingDeviceLowerCriticalThreshold = _CoolingDeviceLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 13),
    _CoolingDeviceLowerCriticalThreshold_Type()
)
coolingDeviceLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceLowerCriticalThreshold.setDescription("""\
0700.0012.0001.0013 This attribute defines the value of the Dell fans lower
critical threshold. The value is an integer representing fan speed in
revolutions per minute, it is not applicable to OFF/ON type fans or nonFan
types.
""")
_CoolingDeviceLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_CoolingDeviceLowerNonRecoverableThreshold_Object = MibTableColumn
coolingDeviceLowerNonRecoverableThreshold = _CoolingDeviceLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 14),
    _CoolingDeviceLowerNonRecoverableThreshold_Type()
)
coolingDeviceLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceLowerNonRecoverableThreshold.setDescription("""\
0700.0012.0001.0014 This attribute defines the value of the Dell fans lower
nonrecoverable threshold. The value is an integer representing fan speed in
revolutions per minute, it is not applicable to OFF/ON type fans or nonFan
types.
""")
_CoolingDevicecoolingUnitIndexReference_Type = DellObjectRange
_CoolingDevicecoolingUnitIndexReference_Object = MibTableColumn
coolingDevicecoolingUnitIndexReference = _CoolingDevicecoolingUnitIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 15),
    _CoolingDevicecoolingUnitIndexReference_Type()
)
coolingDevicecoolingUnitIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDevicecoolingUnitIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDevicecoolingUnitIndexReference.setDescription("""\
0700.0012.0001.0015 This attribute defines the index to the associated Dell
System Cooling Unit in this chassis.
""")
_CoolingDeviceSubType_Type = DellCoolingDeviceSubType
_CoolingDeviceSubType_Object = MibTableColumn
coolingDeviceSubType = _CoolingDeviceSubType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 12, 1, 16),
    _CoolingDeviceSubType_Type()
)
coolingDeviceSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingDeviceSubType.setStatus("mandatory")
if mibBuilder.loadTexts:
    coolingDeviceSubType.setDescription("""\
0700.0012.0001.0016 This attribute defines the subtype of the Dell cooling
device.
""")
_TemperatureProbeTable_Object = MibTable
temperatureProbeTable = _TemperatureProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20)
)
if mibBuilder.loadTexts:
    temperatureProbeTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeTable.setDescription("""\
0700.0020 This Group defines the Dell Temperature Probe Table.
""")
_TemperatureProbeTableEntry_Object = MibTableRow
temperatureProbeTableEntry = _TemperatureProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1)
)
temperatureProbeTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "temperatureProbechassisIndex"),
    (0, "MIB-Dell-10892", "temperatureProbeIndex"),
)
if mibBuilder.loadTexts:
    temperatureProbeTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeTableEntry.setDescription("""\
0700.0020.0001 This Group defines the Dell Temperature Probe Table Entry.
""")
_TemperatureProbechassisIndex_Type = DellObjectRange
_TemperatureProbechassisIndex_Object = MibTableColumn
temperatureProbechassisIndex = _TemperatureProbechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 1),
    _TemperatureProbechassisIndex_Type()
)
temperatureProbechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbechassisIndex.setDescription("""\
0700.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_TemperatureProbeIndex_Type = DellObjectRange
_TemperatureProbeIndex_Object = MibTableColumn
temperatureProbeIndex = _TemperatureProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 2),
    _TemperatureProbeIndex_Type()
)
temperatureProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeIndex.setDescription("""\
0700.0020.0001.0002 This attribute defines the index of Dell temperature probes
in this chassis.
""")
_TemperatureProbeStateCapabilities_Type = DellStateCapabilities
_TemperatureProbeStateCapabilities_Object = MibTableColumn
temperatureProbeStateCapabilities = _TemperatureProbeStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 3),
    _TemperatureProbeStateCapabilities_Type()
)
temperatureProbeStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeStateCapabilities.setDescription("""\
0700.0020.0001.0003 This attribute defines the capabilities of the Dell
temperature probe.
""")
_TemperatureProbeStateSettings_Type = DellStateSettings
_TemperatureProbeStateSettings_Object = MibTableColumn
temperatureProbeStateSettings = _TemperatureProbeStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 4),
    _TemperatureProbeStateSettings_Type()
)
temperatureProbeStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureProbeStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeStateSettings.setDescription("""\
0700.0020.0001.0004 This attribute defines the state of the Dell temperature
probe.
""")
_TemperatureProbeStatus_Type = DellStatusProbe
_TemperatureProbeStatus_Object = MibTableColumn
temperatureProbeStatus = _TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 5),
    _TemperatureProbeStatus_Type()
)
temperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeStatus.setDescription("""\
0700.0020.0001.0005 This attribute defines the status of the Dell temperature
probe.
""")
_TemperatureProbeReading_Type = DellSigned32BitRange
_TemperatureProbeReading_Object = MibTableColumn
temperatureProbeReading = _TemperatureProbeReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 6),
    _TemperatureProbeReading_Type()
)
temperatureProbeReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeReading.setDescription("""\
0700.0020.0001.0006 This attribute defines the value of the Dell temperature
probe. The value is an integer representing temperature in tenths of degrees
Centigrade.
""")
_TemperatureProbeType_Type = DellTemperatureProbeType
_TemperatureProbeType_Object = MibTableColumn
temperatureProbeType = _TemperatureProbeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 7),
    _TemperatureProbeType_Type()
)
temperatureProbeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeType.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeType.setDescription("""\
0700.0020.0001.0007 This attribute defines the type of the Dell temperature
probe.
""")
_TemperatureProbeLocationName_Type = DellString
_TemperatureProbeLocationName_Object = MibTableColumn
temperatureProbeLocationName = _TemperatureProbeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 8),
    _TemperatureProbeLocationName_Type()
)
temperatureProbeLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeLocationName.setDescription("""\
0700.0020.0001.0008 This attribute defines the location of the temperature
probe in this chassis.
""")
_TemperatureProbeUpperNonRecoverableThreshold_Type = DellSigned32BitRange
_TemperatureProbeUpperNonRecoverableThreshold_Object = MibTableColumn
temperatureProbeUpperNonRecoverableThreshold = _TemperatureProbeUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 9),
    _TemperatureProbeUpperNonRecoverableThreshold_Type()
)
temperatureProbeUpperNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonRecoverableThreshold.setDescription("""\
0700.0020.0001.0009 This attribute defines the value of the Dell temperature
probes upper nonrecoverable threshold. The value is an integer representing
temperature in tenths of degrees Centigrade.
""")
_TemperatureProbeUpperCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeUpperCriticalThreshold_Object = MibTableColumn
temperatureProbeUpperCriticalThreshold = _TemperatureProbeUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 10),
    _TemperatureProbeUpperCriticalThreshold_Type()
)
temperatureProbeUpperCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeUpperCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeUpperCriticalThreshold.setDescription("""\
0700.0020.0001.0010 This attribute defines the value of the Dell temperature
probes upper critical threshold. The value is an integer representing
temperature in tenths of degrees Centigrade.
""")
_TemperatureProbeUpperNonCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeUpperNonCriticalThreshold_Object = MibTableColumn
temperatureProbeUpperNonCriticalThreshold = _TemperatureProbeUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 11),
    _TemperatureProbeUpperNonCriticalThreshold_Type()
)
temperatureProbeUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeUpperNonCriticalThreshold.setDescription("""\
0700.0020.0001.0011 This attribute defines the value of the Dell temperature
probes upper noncritical threshold. The value is an integer representing
temperature in tenths of degrees Centigrade.
""")
_TemperatureProbeLowerNonCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeLowerNonCriticalThreshold_Object = MibTableColumn
temperatureProbeLowerNonCriticalThreshold = _TemperatureProbeLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 12),
    _TemperatureProbeLowerNonCriticalThreshold_Type()
)
temperatureProbeLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonCriticalThreshold.setDescription("""\
0700.0020.0001.0012 This attribute defines the value of the Dell temperature
probes lower noncritical threshold. The value is an integer representing
temperature in tenths of degrees Centigrade.
""")
_TemperatureProbeLowerCriticalThreshold_Type = DellSigned32BitRange
_TemperatureProbeLowerCriticalThreshold_Object = MibTableColumn
temperatureProbeLowerCriticalThreshold = _TemperatureProbeLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 13),
    _TemperatureProbeLowerCriticalThreshold_Type()
)
temperatureProbeLowerCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeLowerCriticalThreshold.setDescription("""\
0700.0020.0001.0013 This attribute defines the value of the Dell temperature
probes lower critical threshold. The value is an integer representing
temperature in tenths of degrees Centigrade.
""")
_TemperatureProbeLowerNonRecoverableThreshold_Type = DellSigned32BitRange
_TemperatureProbeLowerNonRecoverableThreshold_Object = MibTableColumn
temperatureProbeLowerNonRecoverableThreshold = _TemperatureProbeLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 700, 20, 1, 14),
    _TemperatureProbeLowerNonRecoverableThreshold_Type()
)
temperatureProbeLowerNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    temperatureProbeLowerNonRecoverableThreshold.setDescription("""\
0700.0020.0001.0014 This attribute defines the value of the Dell temperature
probes lower nonrecoverable threshold. The value is an integer representing
temperature in tenths of degrees Centigrade.
""")
_UserSecurityGroup_ObjectIdentity = ObjectIdentity
userSecurityGroup = _UserSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800)
)
_UserSecurityTable_Object = MibTable
userSecurityTable = _UserSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10)
)
if mibBuilder.loadTexts:
    userSecurityTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecurityTable.setDescription("""\
0800.0010 This table contains the database of users that are authorized to
perform Set operations on a managed Dell system.
""")
_UserSecurityTableEntry_Object = MibTableRow
userSecurityTableEntry = _UserSecurityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1)
)
userSecurityTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "userSecuritychassisIndex"),
    (0, "MIB-Dell-10892", "userSecurityIndex"),
)
if mibBuilder.loadTexts:
    userSecurityTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecurityTableEntry.setDescription("""\
0800.0010.0001 A row in the user table.
""")
_UserSecuritychassisIndex_Type = DellObjectRange
_UserSecuritychassisIndex_Object = MibTableColumn
userSecuritychassisIndex = _UserSecuritychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 1),
    _UserSecuritychassisIndex_Type()
)
userSecuritychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecuritychassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecuritychassisIndex.setDescription("""\
0800.0010.0001.0001 Chassis index.
""")
_UserSecurityIndex_Type = DellObjectRange
_UserSecurityIndex_Object = MibTableColumn
userSecurityIndex = _UserSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 2),
    _UserSecurityIndex_Type()
)
userSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecurityIndex.setDescription("""\
0800.0010.0001.0002 User index.
""")
_UserSecurityUserName_Type = DellSecurityString
_UserSecurityUserName_Object = MibTableColumn
userSecurityUserName = _UserSecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 3),
    _UserSecurityUserName_Type()
)
userSecurityUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityUserName.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecurityUserName.setDescription("""\
0800.0010.0001.0003 User name.
""")
_UserSecurityControlName_Type = DellSecurityString
_UserSecurityControlName_Object = MibTableColumn
userSecurityControlName = _UserSecurityControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 4),
    _UserSecurityControlName_Type()
)
userSecurityControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecurityControlName.setDescription("""\
0800.0010.0001.0004 User control. Used for creating/deleting/editing users.
""")
_UserSecurityRequestName_Type = DellSecurityString
_UserSecurityRequestName_Object = MibTableColumn
userSecurityRequestName = _UserSecurityRequestName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 800, 10, 1, 5),
    _UserSecurityRequestName_Type()
)
userSecurityRequestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityRequestName.setStatus("mandatory")
if mibBuilder.loadTexts:
    userSecurityRequestName.setDescription("""\
0800.0010.0001.0005 Set request control. Used for Set operations.
""")
_RemoteFlashBIOSGroup_ObjectIdentity = ObjectIdentity
remoteFlashBIOSGroup = _RemoteFlashBIOSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900)
)
_RemoteFlashBIOSTable_Object = MibTable
remoteFlashBIOSTable = _RemoteFlashBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10)
)
if mibBuilder.loadTexts:
    remoteFlashBIOSTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSTable.setDescription("""\
0900.0010 This Table defines the settings for Dell Remote BIOS updates.
""")
_RemoteFlashBIOSTableEntry_Object = MibTableRow
remoteFlashBIOSTableEntry = _RemoteFlashBIOSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1)
)
remoteFlashBIOSTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteFlashBIOSchassisIndex"),
    (0, "MIB-Dell-10892", "remoteFlashBIOSIndex"),
)
if mibBuilder.loadTexts:
    remoteFlashBIOSTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSTableEntry.setDescription("""\
0900.0010.0001 This Group defines the Dell Remote Flash BIOS Table Entry.
""")
_RemoteFlashBIOSchassisIndex_Type = DellObjectRange
_RemoteFlashBIOSchassisIndex_Object = MibTableColumn
remoteFlashBIOSchassisIndex = _RemoteFlashBIOSchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 1),
    _RemoteFlashBIOSchassisIndex_Type()
)
remoteFlashBIOSchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSchassisIndex.setDescription("""\
0900.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_RemoteFlashBIOSIndex_Type = DellObjectRange
_RemoteFlashBIOSIndex_Object = MibTableColumn
remoteFlashBIOSIndex = _RemoteFlashBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 2),
    _RemoteFlashBIOSIndex_Type()
)
remoteFlashBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSIndex.setDescription("""\
0900.0010.0001.0002 This attribute defines the index to the Dell Remote BIOS
update hardware on this Dell System.
""")
_RemoteFlashBIOSStateCapabilitiesUnique_Type = DellRemoteFlashBIOSStateCapabilitiesUnique
_RemoteFlashBIOSStateCapabilitiesUnique_Object = MibTableColumn
remoteFlashBIOSStateCapabilitiesUnique = _RemoteFlashBIOSStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 3),
    _RemoteFlashBIOSStateCapabilitiesUnique_Type()
)
remoteFlashBIOSStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSStateCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSStateCapabilitiesUnique.setDescription("""\
0900.0010.0001.0003 This attribute defines the capabilities of the Dell Remote
BIOS update on this Dell System.
""")
_RemoteFlashBIOSStateSettingsUnique_Type = DellRemoteFlashBIOSStateSettingsUnique
_RemoteFlashBIOSStateSettingsUnique_Object = MibTableColumn
remoteFlashBIOSStateSettingsUnique = _RemoteFlashBIOSStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 4),
    _RemoteFlashBIOSStateSettingsUnique_Type()
)
remoteFlashBIOSStateSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteFlashBIOSStateSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSStateSettingsUnique.setDescription("""\
0900.0010.0001.0004 This attribute defines the state of the Dell Remote BIOS
update on this Dell System.
""")
_RemoteFlashBIOSStatus_Type = DellStatus
_RemoteFlashBIOSStatus_Object = MibTableColumn
remoteFlashBIOSStatus = _RemoteFlashBIOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 5),
    _RemoteFlashBIOSStatus_Type()
)
remoteFlashBIOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSStatus.setDescription("""\
0900.0010.0001.0005 This attribute defines the status of the Dell Remote BIOS
update on this Dell System.
""")
_RemoteFlashBIOSLastBIOSDateName_Type = DellDateName
_RemoteFlashBIOSLastBIOSDateName_Object = MibTableColumn
remoteFlashBIOSLastBIOSDateName = _RemoteFlashBIOSLastBIOSDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 6),
    _RemoteFlashBIOSLastBIOSDateName_Type()
)
remoteFlashBIOSLastBIOSDateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSLastBIOSDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSLastBIOSDateName.setDescription("""\
0900.0010.0001.0006 This attribute defines the date of last BIOS update. Dates
are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_RemoteFlashBIOSCompletionCode_Type = DellRemoteFlashBIOSCompletionCode
_RemoteFlashBIOSCompletionCode_Object = MibTableColumn
remoteFlashBIOSCompletionCode = _RemoteFlashBIOSCompletionCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 7),
    _RemoteFlashBIOSCompletionCode_Type()
)
remoteFlashBIOSCompletionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSCompletionCode.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSCompletionCode.setDescription("""\
0900.0010.0001.0007 This attribute defines the completion code of the last BIOS
update.
""")
_RemoteFlashBIOSMinimumContiguousMemory_Type = DellUnsigned32BitRange
_RemoteFlashBIOSMinimumContiguousMemory_Object = MibTableColumn
remoteFlashBIOSMinimumContiguousMemory = _RemoteFlashBIOSMinimumContiguousMemory_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 900, 10, 1, 8),
    _RemoteFlashBIOSMinimumContiguousMemory_Type()
)
remoteFlashBIOSMinimumContiguousMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteFlashBIOSMinimumContiguousMemory.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteFlashBIOSMinimumContiguousMemory.setDescription("""\
0900.0010.0001.0008 This attribute defines the minimum size of contiguous
memory required for remote BIOS update in kilobytes.
""")
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000)
)
_PointingPortTable_Object = MibTable
pointingPortTable = _PointingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10)
)
if mibBuilder.loadTexts:
    pointingPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortTable.setDescription("""\
1000.0010 This Group defines the Dell Pointing Port Table.
""")
_PointingPortTableEntry_Object = MibTableRow
pointingPortTableEntry = _PointingPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1)
)
pointingPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pointingPortchassisIndex"),
    (0, "MIB-Dell-10892", "pointingPortIndex"),
)
if mibBuilder.loadTexts:
    pointingPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortTableEntry.setDescription("""\
1000.0010.0001 This Group defines the Dell Pointing Port Table Entry.
""")
_PointingPortchassisIndex_Type = DellObjectRange
_PointingPortchassisIndex_Object = MibTableColumn
pointingPortchassisIndex = _PointingPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 1),
    _PointingPortchassisIndex_Type()
)
pointingPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortchassisIndex.setDescription("""\
1000.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PointingPortIndex_Type = DellObjectRange
_PointingPortIndex_Object = MibTableColumn
pointingPortIndex = _PointingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 2),
    _PointingPortIndex_Type()
)
pointingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortIndex.setDescription("""\
1000.0010.0001.0002 This attribute defines the index of the Dell Pointing Port
in this chassis.
""")
_PointingPortStateCapabilities_Type = DellStateCapabilities
_PointingPortStateCapabilities_Object = MibTableColumn
pointingPortStateCapabilities = _PointingPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 3),
    _PointingPortStateCapabilities_Type()
)
pointingPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortStateCapabilities.setDescription("""\
1000.0010.0001.0003 This attribute defines the capabilities of the Dell
Pointing Port.
""")
_PointingPortStateSettings_Type = DellStateSettings
_PointingPortStateSettings_Object = MibTableColumn
pointingPortStateSettings = _PointingPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 4),
    _PointingPortStateSettings_Type()
)
pointingPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pointingPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortStateSettings.setDescription("""\
1000.0010.0001.0004 This attribute defines the state of the Dell Pointing Port.
""")
_PointingPortStatus_Type = DellStatus
_PointingPortStatus_Object = MibTableColumn
pointingPortStatus = _PointingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 5),
    _PointingPortStatus_Type()
)
pointingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortStatus.setDescription("""\
1000.0010.0001.0005 This attribute defines the status of the Dell Pointing
Port.
""")
_PointingPortSecurityState_Type = DellPortSecurityState
_PointingPortSecurityState_Object = MibTableColumn
pointingPortSecurityState = _PointingPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 6),
    _PointingPortSecurityState_Type()
)
pointingPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortSecurityState.setDescription("""\
1000.0010.0001.0006 This attribute defines if security settings of the Dell
Pointing Port.
""")
_PointingPortConnectorType_Type = DellPointingPortConnectorType
_PointingPortConnectorType_Object = MibTableColumn
pointingPortConnectorType = _PointingPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 7),
    _PointingPortConnectorType_Type()
)
pointingPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortConnectorType.setDescription("""\
1000.0010.0001.0007 This attribute defines the connector type of the Dell
Pointing Port.
""")
_PointingPortName_Type = DellString
_PointingPortName_Object = MibTableColumn
pointingPortName = _PointingPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 8),
    _PointingPortName_Type()
)
pointingPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortName.setDescription("""\
1000.0010.0001.0008 This attribute defines name of the Dell Pointing Port.
""")
_PointingPortBIOSConnectorType_Type = DellGenericPortConnectorType
_PointingPortBIOSConnectorType_Object = MibTableColumn
pointingPortBIOSConnectorType = _PointingPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 10, 1, 9),
    _PointingPortBIOSConnectorType_Type()
)
pointingPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortBIOSConnectorType.setDescription("""\
1000.0010.0001.0009 This attribute defines the BIOS connector type of the Dell
Pointing Port.
""")
_KeyboardPortTable_Object = MibTable
keyboardPortTable = _KeyboardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20)
)
if mibBuilder.loadTexts:
    keyboardPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortTable.setDescription("""\
1000.0020 This Group defines the Dell Keyboard Port Table.
""")
_KeyboardPortTableEntry_Object = MibTableRow
keyboardPortTableEntry = _KeyboardPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1)
)
keyboardPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "keyboardPortchassisIndex"),
    (0, "MIB-Dell-10892", "keyboardPortIndex"),
)
if mibBuilder.loadTexts:
    keyboardPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortTableEntry.setDescription("""\
1000.0020.0001 This Group defines the Dell Keyboard Port Table Entry.
""")
_KeyboardPortchassisIndex_Type = DellObjectRange
_KeyboardPortchassisIndex_Object = MibTableColumn
keyboardPortchassisIndex = _KeyboardPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 1),
    _KeyboardPortchassisIndex_Type()
)
keyboardPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortchassisIndex.setDescription("""\
1000.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_KeyboardPortIndex_Type = DellObjectRange
_KeyboardPortIndex_Object = MibTableColumn
keyboardPortIndex = _KeyboardPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 2),
    _KeyboardPortIndex_Type()
)
keyboardPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortIndex.setDescription("""\
1000.0020.0001.0002 This attribute defines the index of the Dell Keyboard Port
in this chassis.
""")
_KeyboardPortStateCapabilities_Type = DellStateCapabilities
_KeyboardPortStateCapabilities_Object = MibTableColumn
keyboardPortStateCapabilities = _KeyboardPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 3),
    _KeyboardPortStateCapabilities_Type()
)
keyboardPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortStateCapabilities.setDescription("""\
1000.0020.0001.0003 This attribute defines the capabilities of the Dell
Keyboard Port.
""")
_KeyboardPortStateSettings_Type = DellStateSettings
_KeyboardPortStateSettings_Object = MibTableColumn
keyboardPortStateSettings = _KeyboardPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 4),
    _KeyboardPortStateSettings_Type()
)
keyboardPortStateSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortStateSettings.setDescription("""\
1000.0020.0001.0004 This attribute defines the state of the Dell Keyboard Port.
""")
_KeyboardPortStatus_Type = DellStatus
_KeyboardPortStatus_Object = MibTableColumn
keyboardPortStatus = _KeyboardPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 5),
    _KeyboardPortStatus_Type()
)
keyboardPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortStatus.setDescription("""\
1000.0020.0001.0005 This attribute defines the status of the Dell Keyboard
Port.
""")
_KeyboardPortSecurityState_Type = DellPortSecurityState
_KeyboardPortSecurityState_Object = MibTableColumn
keyboardPortSecurityState = _KeyboardPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 6),
    _KeyboardPortSecurityState_Type()
)
keyboardPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortSecurityState.setDescription("""\
1000.0020.0001.0006 This attribute defines if security settings of the Dell
Keyboard Port.
""")
_KeyboardPortConnectorType_Type = DellKeyboardPortConnectorType
_KeyboardPortConnectorType_Object = MibTableColumn
keyboardPortConnectorType = _KeyboardPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 7),
    _KeyboardPortConnectorType_Type()
)
keyboardPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortConnectorType.setDescription("""\
1000.0020.0001.0007 This attribute defines the connector type of the Dell
Keyboard Port.
""")
_KeyboardPortName_Type = DellString
_KeyboardPortName_Object = MibTableColumn
keyboardPortName = _KeyboardPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 8),
    _KeyboardPortName_Type()
)
keyboardPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortName.setDescription("""\
1000.0020.0001.0008 This attribute defines name of the Dell Keyboard Port.
""")
_KeyboardPortBIOSConnectorType_Type = DellGenericPortConnectorType
_KeyboardPortBIOSConnectorType_Object = MibTableColumn
keyboardPortBIOSConnectorType = _KeyboardPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 20, 1, 9),
    _KeyboardPortBIOSConnectorType_Type()
)
keyboardPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortBIOSConnectorType.setDescription("""\
1000.0020.0001.0009 This attribute defines the BIOS connector type of the Dell
Keyboard Port.
""")
_ProcessorPortTable_Object = MibTable
processorPortTable = _ProcessorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30)
)
if mibBuilder.loadTexts:
    processorPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortTable.setDescription("""\
1000.0030 This Group defines the Dell Processor Port Table.
""")
_ProcessorPortTableEntry_Object = MibTableRow
processorPortTableEntry = _ProcessorPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1)
)
processorPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "processorPortchassisIndex"),
    (0, "MIB-Dell-10892", "processorPortIndex"),
)
if mibBuilder.loadTexts:
    processorPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortTableEntry.setDescription("""\
1000.0030.0001 This Group defines the Dell Processor Port Table Entry.
""")
_ProcessorPortchassisIndex_Type = DellObjectRange
_ProcessorPortchassisIndex_Object = MibTableColumn
processorPortchassisIndex = _ProcessorPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 1),
    _ProcessorPortchassisIndex_Type()
)
processorPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortchassisIndex.setDescription("""\
1000.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_ProcessorPortIndex_Type = DellObjectRange
_ProcessorPortIndex_Object = MibTableColumn
processorPortIndex = _ProcessorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 2),
    _ProcessorPortIndex_Type()
)
processorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortIndex.setDescription("""\
1000.0030.0001.0002 This attribute defines the index of the Dell Processor Port
in this chassis.
""")
_ProcessorPortStateCapabilities_Type = DellStateCapabilities
_ProcessorPortStateCapabilities_Object = MibTableColumn
processorPortStateCapabilities = _ProcessorPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 3),
    _ProcessorPortStateCapabilities_Type()
)
processorPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortStateCapabilities.setDescription("""\
1000.0030.0001.0003 This attribute defines the capabilities of the Dell
Processor Port.
""")
_ProcessorPortStateSettings_Type = DellStateSettings
_ProcessorPortStateSettings_Object = MibTableColumn
processorPortStateSettings = _ProcessorPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 4),
    _ProcessorPortStateSettings_Type()
)
processorPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processorPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortStateSettings.setDescription("""\
1000.0030.0001.0004 This attribute defines the state of the Dell Processor
Port.
""")
_ProcessorPortStatus_Type = DellStatus
_ProcessorPortStatus_Object = MibTableColumn
processorPortStatus = _ProcessorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 5),
    _ProcessorPortStatus_Type()
)
processorPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortStatus.setDescription("""\
1000.0030.0001.0005 This attribute defines the status of the Dell Processor
Port.
""")
_ProcessorPortSecurityState_Type = DellPortSecurityState
_ProcessorPortSecurityState_Object = MibTableColumn
processorPortSecurityState = _ProcessorPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 6),
    _ProcessorPortSecurityState_Type()
)
processorPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortSecurityState.setDescription("""\
1000.0030.0001.0006 This attribute defines the security settings of the Dell
Processor Port.
""")
_ProcessorPortConnectorType_Type = DellProcessorPortConnectorType
_ProcessorPortConnectorType_Object = MibTableColumn
processorPortConnectorType = _ProcessorPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 7),
    _ProcessorPortConnectorType_Type()
)
processorPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortConnectorType.setDescription("""\
1000.0030.0001.0007 This attribute defines the connector type of the Dell
Processor Port.
""")
_ProcessorPortName_Type = DellString
_ProcessorPortName_Object = MibTableColumn
processorPortName = _ProcessorPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 8),
    _ProcessorPortName_Type()
)
processorPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortName.setDescription("""\
1000.0030.0001.0008 This attribute defines name of the Dell Processor Port.
""")
_ProcessorPortBIOSConnectorType_Type = DellGenericPortConnectorType
_ProcessorPortBIOSConnectorType_Object = MibTableColumn
processorPortBIOSConnectorType = _ProcessorPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 30, 1, 9),
    _ProcessorPortBIOSConnectorType_Type()
)
processorPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortBIOSConnectorType.setDescription("""\
1000.0030.0001.0009 This attribute defines the BIOS connector type of the Dell
Processor Port.
""")
_MemoryDevicePortTable_Object = MibTable
memoryDevicePortTable = _MemoryDevicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40)
)
if mibBuilder.loadTexts:
    memoryDevicePortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortTable.setDescription("""\
1000.0040 This Group defines the Dell Memory Device Port Table.
""")
_MemoryDevicePortTableEntry_Object = MibTableRow
memoryDevicePortTableEntry = _MemoryDevicePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1)
)
memoryDevicePortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "memoryDevicePortchassisIndex"),
    (0, "MIB-Dell-10892", "memoryDevicePortIndex"),
)
if mibBuilder.loadTexts:
    memoryDevicePortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortTableEntry.setDescription("""\
1000.0040.0001 This Group defines the Dell Memory Device Port Table Entry.
""")
_MemoryDevicePortchassisIndex_Type = DellObjectRange
_MemoryDevicePortchassisIndex_Object = MibTableColumn
memoryDevicePortchassisIndex = _MemoryDevicePortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 1),
    _MemoryDevicePortchassisIndex_Type()
)
memoryDevicePortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortchassisIndex.setDescription("""\
1000.0040.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_MemoryDevicePortIndex_Type = DellObjectRange
_MemoryDevicePortIndex_Object = MibTableColumn
memoryDevicePortIndex = _MemoryDevicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 2),
    _MemoryDevicePortIndex_Type()
)
memoryDevicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortIndex.setDescription("""\
1000.0040.0001.0002 This attribute defines the index of the Dell Memory Device
Port in this chassis.
""")
_MemoryDevicePortStateCapabilities_Type = DellStateCapabilities
_MemoryDevicePortStateCapabilities_Object = MibTableColumn
memoryDevicePortStateCapabilities = _MemoryDevicePortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 3),
    _MemoryDevicePortStateCapabilities_Type()
)
memoryDevicePortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortStateCapabilities.setDescription("""\
1000.0040.0001.0003 This attribute defines the capabilities of the Dell Memory
Device Port.
""")
_MemoryDevicePortStateSettings_Type = DellStateSettings
_MemoryDevicePortStateSettings_Object = MibTableColumn
memoryDevicePortStateSettings = _MemoryDevicePortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 4),
    _MemoryDevicePortStateSettings_Type()
)
memoryDevicePortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDevicePortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortStateSettings.setDescription("""\
1000.0040.0001.0004 This attribute defines the state of the Dell Memory Device
Port.
""")
_MemoryDevicePortStatus_Type = DellStatus
_MemoryDevicePortStatus_Object = MibTableColumn
memoryDevicePortStatus = _MemoryDevicePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 5),
    _MemoryDevicePortStatus_Type()
)
memoryDevicePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortStatus.setDescription("""\
1000.0040.0001.0005 This attribute defines the status of the Dell Memory Device
Port.
""")
_MemoryDevicePortSecurityState_Type = DellPortSecurityState
_MemoryDevicePortSecurityState_Object = MibTableColumn
memoryDevicePortSecurityState = _MemoryDevicePortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 6),
    _MemoryDevicePortSecurityState_Type()
)
memoryDevicePortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortSecurityState.setDescription("""\
1000.0040.0001.0006 This attribute defines the security settings of the Dell
Memory Device Port.
""")
_MemoryDevicePortConnectorType_Type = DellMemoryDevicePortConnectorType
_MemoryDevicePortConnectorType_Object = MibTableColumn
memoryDevicePortConnectorType = _MemoryDevicePortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 7),
    _MemoryDevicePortConnectorType_Type()
)
memoryDevicePortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortConnectorType.setDescription("""\
1000.0040.0001.0007 This attribute defines the connector type of the Dell
Memory Device Port.
""")
_MemoryDevicePortName_Type = DellString
_MemoryDevicePortName_Object = MibTableColumn
memoryDevicePortName = _MemoryDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 8),
    _MemoryDevicePortName_Type()
)
memoryDevicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortName.setDescription("""\
1000.0040.0001.0008 This attribute defines name of the Dell Memory Device Port.
""")
_MemoryDevicePortBIOSConnectorType_Type = DellGenericPortConnectorType
_MemoryDevicePortBIOSConnectorType_Object = MibTableColumn
memoryDevicePortBIOSConnectorType = _MemoryDevicePortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 9),
    _MemoryDevicePortBIOSConnectorType_Type()
)
memoryDevicePortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortBIOSConnectorType.setDescription("""\
1000.0040.0001.0009 This attribute defines the BIOS connector type of the Dell
Memory Device Port.
""")
_MemoryDevicePortPhysicalMemoryArrayIndexReference_Type = DellUnsigned32BitRange
_MemoryDevicePortPhysicalMemoryArrayIndexReference_Object = MibTableColumn
memoryDevicePortPhysicalMemoryArrayIndexReference = _MemoryDevicePortPhysicalMemoryArrayIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 40, 1, 10),
    _MemoryDevicePortPhysicalMemoryArrayIndexReference_Type()
)
memoryDevicePortPhysicalMemoryArrayIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicePortPhysicalMemoryArrayIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicePortPhysicalMemoryArrayIndexReference.setDescription("""\
1000.0040.0001.0010 This attribute defines the index value of the Physical
Memory Array that this memory device is associated with.
""")
_MonitorPortTable_Object = MibTable
monitorPortTable = _MonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50)
)
if mibBuilder.loadTexts:
    monitorPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortTable.setDescription("""\
1000.0050 This Group defines the Dell Monitor Port Table.
""")
_MonitorPortTableEntry_Object = MibTableRow
monitorPortTableEntry = _MonitorPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1)
)
monitorPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "monitorPortchassisIndex"),
    (0, "MIB-Dell-10892", "monitorPortIndex"),
)
if mibBuilder.loadTexts:
    monitorPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortTableEntry.setDescription("""\
1000.0050.0001 This Group defines the Dell Monitor Port Table Entry.
""")
_MonitorPortchassisIndex_Type = DellObjectRange
_MonitorPortchassisIndex_Object = MibTableColumn
monitorPortchassisIndex = _MonitorPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 1),
    _MonitorPortchassisIndex_Type()
)
monitorPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortchassisIndex.setDescription("""\
1000.0050.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_MonitorPortIndex_Type = DellObjectRange
_MonitorPortIndex_Object = MibTableColumn
monitorPortIndex = _MonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 2),
    _MonitorPortIndex_Type()
)
monitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortIndex.setDescription("""\
1000.0050.0001.0002 This attribute defines the index of the Dell Monitor Port
in this chassis.
""")
_MonitorPortStateCapabilities_Type = DellStateCapabilities
_MonitorPortStateCapabilities_Object = MibTableColumn
monitorPortStateCapabilities = _MonitorPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 3),
    _MonitorPortStateCapabilities_Type()
)
monitorPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortStateCapabilities.setDescription("""\
1000.0050.0001.0003 This attribute defines the capabilities of the Dell Monitor
Port.
""")
_MonitorPortStateSettings_Type = DellStateSettings
_MonitorPortStateSettings_Object = MibTableColumn
monitorPortStateSettings = _MonitorPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 4),
    _MonitorPortStateSettings_Type()
)
monitorPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortStateSettings.setDescription("""\
1000.0050.0001.0004 This attribute defines the state of the Dell Monitor Port.
""")
_MonitorPortStatus_Type = DellStatus
_MonitorPortStatus_Object = MibTableColumn
monitorPortStatus = _MonitorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 5),
    _MonitorPortStatus_Type()
)
monitorPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortStatus.setDescription("""\
1000.0050.0001.0005 This attribute defines the status of the Dell Monitor Port.
""")
_MonitorPortSecurityState_Type = DellPortSecurityState
_MonitorPortSecurityState_Object = MibTableColumn
monitorPortSecurityState = _MonitorPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 6),
    _MonitorPortSecurityState_Type()
)
monitorPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortSecurityState.setDescription("""\
1000.0050.0001.0006 This attribute defines if security settings of the Dell
Monitor Port.
""")
_MonitorPortConnectorType_Type = DellMonitorPortConnectorType
_MonitorPortConnectorType_Object = MibTableColumn
monitorPortConnectorType = _MonitorPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 7),
    _MonitorPortConnectorType_Type()
)
monitorPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortConnectorType.setDescription("""\
1000.0050.0001.0007 This attribute defines the connector type of the Dell
Monitor Port.
""")
_MonitorPortName_Type = DellString
_MonitorPortName_Object = MibTableColumn
monitorPortName = _MonitorPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 8),
    _MonitorPortName_Type()
)
monitorPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortName.setDescription("""\
1000.0050.0001.0008 This attribute defines name of the Dell Monitor Port.
""")
_MonitorPortBIOSConnectorType_Type = DellGenericPortConnectorType
_MonitorPortBIOSConnectorType_Object = MibTableColumn
monitorPortBIOSConnectorType = _MonitorPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 50, 1, 9),
    _MonitorPortBIOSConnectorType_Type()
)
monitorPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    monitorPortBIOSConnectorType.setDescription("""\
1000.0050.0001.0009 This attribute defines the BIOS connector type of the Dell
Monitor Port.
""")
_SCSIPortTable_Object = MibTable
sCSIPortTable = _SCSIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60)
)
if mibBuilder.loadTexts:
    sCSIPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortTable.setDescription("""\
1000.0060 This Group defines the Dell SCSI Port Table.
""")
_SCSIPortTableEntry_Object = MibTableRow
sCSIPortTableEntry = _SCSIPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1)
)
sCSIPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "sCSIPortchassisIndex"),
    (0, "MIB-Dell-10892", "sCSIPortIndex"),
)
if mibBuilder.loadTexts:
    sCSIPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortTableEntry.setDescription("""\
1000.0060.0001 This Group defines the Dell SCSI Port Table Entry.
""")
_SCSIPortchassisIndex_Type = DellObjectRange
_SCSIPortchassisIndex_Object = MibTableColumn
sCSIPortchassisIndex = _SCSIPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 1),
    _SCSIPortchassisIndex_Type()
)
sCSIPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortchassisIndex.setDescription("""\
1000.0060.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SCSIPortIndex_Type = DellObjectRange
_SCSIPortIndex_Object = MibTableColumn
sCSIPortIndex = _SCSIPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 2),
    _SCSIPortIndex_Type()
)
sCSIPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortIndex.setDescription("""\
1000.0060.0001.0002 This attribute defines the index of the Dell SCSI Port in
this chassis.
""")
_SCSIPortStateCapabilities_Type = DellStateCapabilities
_SCSIPortStateCapabilities_Object = MibTableColumn
sCSIPortStateCapabilities = _SCSIPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 3),
    _SCSIPortStateCapabilities_Type()
)
sCSIPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortStateCapabilities.setDescription("""\
1000.0060.0001.0003 This attribute defines the capabilities of the Dell SCSI
Port.
""")
_SCSIPortStateSettings_Type = DellStateSettings
_SCSIPortStateSettings_Object = MibTableColumn
sCSIPortStateSettings = _SCSIPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 4),
    _SCSIPortStateSettings_Type()
)
sCSIPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCSIPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortStateSettings.setDescription("""\
1000.0060.0001.0004 This attribute defines the state of the Dell SCSI Port.
""")
_SCSIPortStatus_Type = DellStatus
_SCSIPortStatus_Object = MibTableColumn
sCSIPortStatus = _SCSIPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 5),
    _SCSIPortStatus_Type()
)
sCSIPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortStatus.setDescription("""\
1000.0060.0001.0005 This attribute defines the status of the Dell SCSI Port.
""")
_SCSIPortSecurityState_Type = DellPortSecurityState
_SCSIPortSecurityState_Object = MibTableColumn
sCSIPortSecurityState = _SCSIPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 6),
    _SCSIPortSecurityState_Type()
)
sCSIPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortSecurityState.setDescription("""\
1000.0060.0001.0006 This attribute defines if security settings of the Dell
SCSI Port.
""")
_SCSIPortConnectorType_Type = DellSCSIPortConnectorType
_SCSIPortConnectorType_Object = MibTableColumn
sCSIPortConnectorType = _SCSIPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 7),
    _SCSIPortConnectorType_Type()
)
sCSIPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortConnectorType.setDescription("""\
1000.0060.0001.0007 This attribute defines the connector type of the Dell SCSI
Port.
""")
_SCSIPortName_Type = DellString
_SCSIPortName_Object = MibTableColumn
sCSIPortName = _SCSIPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 8),
    _SCSIPortName_Type()
)
sCSIPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortName.setDescription("""\
1000.0060.0001.0008 This attribute defines name of the Dell SCSI Port.
""")
_SCSIPortBIOSConnectorType_Type = DellGenericPortConnectorType
_SCSIPortBIOSConnectorType_Object = MibTableColumn
sCSIPortBIOSConnectorType = _SCSIPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 60, 1, 9),
    _SCSIPortBIOSConnectorType_Type()
)
sCSIPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIPortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIPortBIOSConnectorType.setDescription("""\
1000.0060.0001.0009 This attribute defines the BIOS connector type of the Dell
SCSI Port.
""")
_ParallelPortTable_Object = MibTable
parallelPortTable = _ParallelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70)
)
if mibBuilder.loadTexts:
    parallelPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortTable.setDescription("""\
1000.0070 This Group defines the Dell Parallel Port Table.
""")
_ParallelPortTableEntry_Object = MibTableRow
parallelPortTableEntry = _ParallelPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1)
)
parallelPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "parallelPortchassisIndex"),
    (0, "MIB-Dell-10892", "parallelPortIndex"),
)
if mibBuilder.loadTexts:
    parallelPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortTableEntry.setDescription("""\
1000.0070.0001 This Group defines the Dell Parallel Port Table Entry.
""")
_ParallelPortchassisIndex_Type = DellObjectRange
_ParallelPortchassisIndex_Object = MibTableColumn
parallelPortchassisIndex = _ParallelPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 1),
    _ParallelPortchassisIndex_Type()
)
parallelPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortchassisIndex.setDescription("""\
1000.0070.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_ParallelPortIndex_Type = DellObjectRange
_ParallelPortIndex_Object = MibTableColumn
parallelPortIndex = _ParallelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 2),
    _ParallelPortIndex_Type()
)
parallelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortIndex.setDescription("""\
1000.0070.0001.0002 This attribute defines the index of the Dell Parallel Port
in this chassis.
""")
_ParallelPortStateCapabilities_Type = DellStateCapabilities
_ParallelPortStateCapabilities_Object = MibTableColumn
parallelPortStateCapabilities = _ParallelPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 3),
    _ParallelPortStateCapabilities_Type()
)
parallelPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortStateCapabilities.setDescription("""\
1000.0070.0001.0003 This attribute defines the capabilities of the Dell
Parallel Port.
""")
_ParallelPortStateSettings_Type = DellStateSettings
_ParallelPortStateSettings_Object = MibTableColumn
parallelPortStateSettings = _ParallelPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 4),
    _ParallelPortStateSettings_Type()
)
parallelPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parallelPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortStateSettings.setDescription("""\
1000.0070.0001.0004 This attribute defines the state of the Dell Parallel Port.
""")
_ParallelPortStatus_Type = DellStatus
_ParallelPortStatus_Object = MibTableColumn
parallelPortStatus = _ParallelPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 5),
    _ParallelPortStatus_Type()
)
parallelPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortStatus.setDescription("""\
1000.0070.0001.0005 This attribute defines the status of the Dell Parallel
Port.
""")
_ParallelPortSecurityState_Type = DellPortSecurityState
_ParallelPortSecurityState_Object = MibTableColumn
parallelPortSecurityState = _ParallelPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 6),
    _ParallelPortSecurityState_Type()
)
parallelPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortSecurityState.setDescription("""\
1000.0070.0001.0006 This attribute defines if security state of the Dell
Parallel Port.
""")
_ParallelPortConnectorType_Type = DellParallelPortConnectorType
_ParallelPortConnectorType_Object = MibTableColumn
parallelPortConnectorType = _ParallelPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 7),
    _ParallelPortConnectorType_Type()
)
parallelPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortConnectorType.setDescription("""\
1000.0070.0001.0007 This attribute defines the connector type of the Dell
Parallel Port.
""")
_ParallelPortName_Type = DellString
_ParallelPortName_Object = MibTableColumn
parallelPortName = _ParallelPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 8),
    _ParallelPortName_Type()
)
parallelPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortName.setDescription("""\
1000.0070.0001.0008 This attribute defines the name of the Dell Parallel Port.
""")
_ParallelPortConnectorPinOut_Type = DellParallelPortConnectorPinout
_ParallelPortConnectorPinOut_Object = MibTableColumn
parallelPortConnectorPinOut = _ParallelPortConnectorPinOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 9),
    _ParallelPortConnectorPinOut_Type()
)
parallelPortConnectorPinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortConnectorPinOut.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortConnectorPinOut.setDescription("""\
1000.0070.0001.0009 This attribute defines the pinout of the Dell Parallel
Port.
""")
_ParallelPortCapabilitiesUnique_Type = DellParallelPortCapabilitiesUnique
_ParallelPortCapabilitiesUnique_Object = MibTableColumn
parallelPortCapabilitiesUnique = _ParallelPortCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 10),
    _ParallelPortCapabilitiesUnique_Type()
)
parallelPortCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortCapabilitiesUnique.setDescription("""\
1000.0070.0001.0010 This attribute defines the capabilities of the Dell
Parallel Port.
""")
_ParallelPortBaseIOAddress_Type = DellUnsigned64BitRange
_ParallelPortBaseIOAddress_Object = MibTableColumn
parallelPortBaseIOAddress = _ParallelPortBaseIOAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 11),
    _ParallelPortBaseIOAddress_Type()
)
parallelPortBaseIOAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortBaseIOAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortBaseIOAddress.setDescription("""\
1000.0070.0001.0011 This attribute defines the Base Input Output address of the
Dell Parallel Port.
""")
_ParallelPortIRQLevel_Type = DellUnsigned8BitRange
_ParallelPortIRQLevel_Object = MibTableColumn
parallelPortIRQLevel = _ParallelPortIRQLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 12),
    _ParallelPortIRQLevel_Type()
)
parallelPortIRQLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortIRQLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortIRQLevel.setDescription("""\
1000.0070.0001.0012 This attribute defines the Interrupt Request Level of the
Dell Parallel Port.
""")
_ParallelPortDMASupport_Type = DellBoolean
_ParallelPortDMASupport_Object = MibTableColumn
parallelPortDMASupport = _ParallelPortDMASupport_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 70, 1, 13),
    _ParallelPortDMASupport_Type()
)
parallelPortDMASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortDMASupport.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortDMASupport.setDescription("""\
1000.0070.0001.0013 This attribute defines if DMA is supported by the Dell
Parallel Port.
""")
_SerialPortTable_Object = MibTable
serialPortTable = _SerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80)
)
if mibBuilder.loadTexts:
    serialPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortTable.setDescription("""\
1000.0080 This Group defines the Dell Serial Port Table.
""")
_SerialPortTableEntry_Object = MibTableRow
serialPortTableEntry = _SerialPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1)
)
serialPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "serialPortchassisIndex"),
    (0, "MIB-Dell-10892", "serialPortIndex"),
)
if mibBuilder.loadTexts:
    serialPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortTableEntry.setDescription("""\
1000.0080.0001 This Group defines the Dell Serial Port Table Entry.
""")
_SerialPortchassisIndex_Type = DellObjectRange
_SerialPortchassisIndex_Object = MibTableColumn
serialPortchassisIndex = _SerialPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 1),
    _SerialPortchassisIndex_Type()
)
serialPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortchassisIndex.setDescription("""\
1000.0080.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SerialPortIndex_Type = DellObjectRange
_SerialPortIndex_Object = MibTableColumn
serialPortIndex = _SerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 2),
    _SerialPortIndex_Type()
)
serialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortIndex.setDescription("""\
1000.0080.0001.0002 This attribute defines the index of the Dell Serial Port in
this chassis.
""")
_SerialPortStateCapabilities_Type = DellStateCapabilities
_SerialPortStateCapabilities_Object = MibTableColumn
serialPortStateCapabilities = _SerialPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 3),
    _SerialPortStateCapabilities_Type()
)
serialPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortStateCapabilities.setDescription("""\
1000.0080.0001.0003 This attribute defines the capabilities of the Dell Serial
Port.
""")
_SerialPortStateSettings_Type = DellStateSettings
_SerialPortStateSettings_Object = MibTableColumn
serialPortStateSettings = _SerialPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 4),
    _SerialPortStateSettings_Type()
)
serialPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortStateSettings.setDescription("""\
1000.0080.0001.0004 This attribute defines the state of the Dell Serial Port.
""")
_SerialPortStatus_Type = DellStatus
_SerialPortStatus_Object = MibTableColumn
serialPortStatus = _SerialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 5),
    _SerialPortStatus_Type()
)
serialPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortStatus.setDescription("""\
1000.0080.0001.0005 This attribute defines the status of the Dell Serial Port.
""")
_SerialPortSecurityState_Type = DellPortSecurityState
_SerialPortSecurityState_Object = MibTableColumn
serialPortSecurityState = _SerialPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 6),
    _SerialPortSecurityState_Type()
)
serialPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortSecurityState.setDescription("""\
1000.0080.0001.0006 This attribute defines the security settings of the Dell
Serial Port.
""")
_SerialPortConnectorType_Type = DellSerialPortConnectorType
_SerialPortConnectorType_Object = MibTableColumn
serialPortConnectorType = _SerialPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 7),
    _SerialPortConnectorType_Type()
)
serialPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortConnectorType.setDescription("""\
1000.0080.0001.0007 This attribute defines the connector type of the Dell
Serial Port.
""")
_SerialPortName_Type = DellString
_SerialPortName_Object = MibTableColumn
serialPortName = _SerialPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 8),
    _SerialPortName_Type()
)
serialPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortName.setDescription("""\
1000.0080.0001.0008 This attribute defines the name of the Dell Serial Port.
""")
_SerialPortMaximumSpeed_Type = DellUnsigned32BitRange
_SerialPortMaximumSpeed_Object = MibTableColumn
serialPortMaximumSpeed = _SerialPortMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 9),
    _SerialPortMaximumSpeed_Type()
)
serialPortMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortMaximumSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortMaximumSpeed.setDescription("""\
1000.0080.0001.0009 This attribute defines the maximum speed the serial
interface can support in BPS (bits per second). 0 (zero) indicated maximum port
speed is unknown.
""")
_SerialPortCapabilitiesUnique_Type = DellSerialPortCapabilitiesUnique
_SerialPortCapabilitiesUnique_Object = MibTableColumn
serialPortCapabilitiesUnique = _SerialPortCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 10),
    _SerialPortCapabilitiesUnique_Type()
)
serialPortCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortCapabilitiesUnique.setDescription("""\
1000.0080.0001.0010 This attribute defines the capabilities of the Dell Serial
Port.
""")
_SerialPortBaseIOAddress_Type = DellUnsigned64BitRange
_SerialPortBaseIOAddress_Object = MibTableColumn
serialPortBaseIOAddress = _SerialPortBaseIOAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 11),
    _SerialPortBaseIOAddress_Type()
)
serialPortBaseIOAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortBaseIOAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortBaseIOAddress.setDescription("""\
1000.0080.0001.0011 This attribute defines the Base Input Output address of the
Dell Serial Port.
""")
_SerialPortIRQLevel_Type = DellUnsigned8BitRange
_SerialPortIRQLevel_Object = MibTableColumn
serialPortIRQLevel = _SerialPortIRQLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 80, 1, 12),
    _SerialPortIRQLevel_Type()
)
serialPortIRQLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortIRQLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortIRQLevel.setDescription("""\
1000.0080.0001.0012 This attribute defines the Interrupt Request Level of the
Dell Serial Port.
""")
_USBPortTable_Object = MibTable
uSBPortTable = _USBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90)
)
if mibBuilder.loadTexts:
    uSBPortTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortTable.setDescription("""\
1000.0090 This Group defines the Dell USB Port Table.
""")
_USBPortTableEntry_Object = MibTableRow
uSBPortTableEntry = _USBPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1)
)
uSBPortTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "uSBPortchassisIndex"),
    (0, "MIB-Dell-10892", "uSBPortIndex"),
)
if mibBuilder.loadTexts:
    uSBPortTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortTableEntry.setDescription("""\
1000.0090.0001 This Group defines the Dell USB Port Table Entry.
""")
_USBPortchassisIndex_Type = DellObjectRange
_USBPortchassisIndex_Object = MibTableColumn
uSBPortchassisIndex = _USBPortchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 1),
    _USBPortchassisIndex_Type()
)
uSBPortchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortchassisIndex.setDescription("""\
1000.0090.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_USBPortIndex_Type = DellObjectRange
_USBPortIndex_Object = MibTableColumn
uSBPortIndex = _USBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 2),
    _USBPortIndex_Type()
)
uSBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortIndex.setDescription("""\
1000.0090.0001.0002 This attribute defines the index of the Dell USB Port in
this chassis.
""")
_USBPortStateCapabilities_Type = DellStateCapabilities
_USBPortStateCapabilities_Object = MibTableColumn
uSBPortStateCapabilities = _USBPortStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 3),
    _USBPortStateCapabilities_Type()
)
uSBPortStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortStateCapabilities.setDescription("""\
1000.0090.0001.0003 This attribute defines the capabilities the Dell USB Port.
""")
_USBPortStateSettings_Type = DellStateSettings
_USBPortStateSettings_Object = MibTableColumn
uSBPortStateSettings = _USBPortStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 4),
    _USBPortStateSettings_Type()
)
uSBPortStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uSBPortStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortStateSettings.setDescription("""\
1000.0090.0001.0004 This attribute defines the status of the Dell USB Port.
""")
_USBPortStatus_Type = DellStatus
_USBPortStatus_Object = MibTableColumn
uSBPortStatus = _USBPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 5),
    _USBPortStatus_Type()
)
uSBPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortStatus.setDescription("""\
1000.0090.0001.0005 This attribute defines the state of the Dell USB Port.
""")
_USBPortSecurityState_Type = DellPortSecurityState
_USBPortSecurityState_Object = MibTableColumn
uSBPortSecurityState = _USBPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 6),
    _USBPortSecurityState_Type()
)
uSBPortSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortSecurityState.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortSecurityState.setDescription("""\
1000.0090.0001.0006 This attribute defines the security settings of the Dell
USB Port.
""")
_USBPortConnectorType_Type = DellUSBPortConnectorType
_USBPortConnectorType_Object = MibTableColumn
uSBPortConnectorType = _USBPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 7),
    _USBPortConnectorType_Type()
)
uSBPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortConnectorType.setDescription("""\
1000.0090.0001.0007 This attribute defines the connector type of the Dell USB
Port.
""")
_USBPortName_Type = DellString
_USBPortName_Object = MibTableColumn
uSBPortName = _USBPortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 8),
    _USBPortName_Type()
)
uSBPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortName.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortName.setDescription("""\
1000.0090.0001.0008 This attribute defines name of the Dell USB Port.
""")
_USBPortBIOSConnectorType_Type = DellGenericPortConnectorType
_USBPortBIOSConnectorType_Object = MibTableColumn
uSBPortBIOSConnectorType = _USBPortBIOSConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1000, 90, 1, 9),
    _USBPortBIOSConnectorType_Type()
)
uSBPortBIOSConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSBPortBIOSConnectorType.setStatus("mandatory")
if mibBuilder.loadTexts:
    uSBPortBIOSConnectorType.setDescription("""\
1000.0090.0001.0009 This attribute defines the BIOS connector type of the Dell
USB Port.
""")
_DeviceGroup_ObjectIdentity = ObjectIdentity
deviceGroup = _DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100)
)
_PointingDeviceTable_Object = MibTable
pointingDeviceTable = _PointingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10)
)
if mibBuilder.loadTexts:
    pointingDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceTable.setDescription("""\
1100.0010 This Group defines the Dell Pointing Device Table. It references the
Dell Pointing Port Index.
""")
_PointingDeviceTableEntry_Object = MibTableRow
pointingDeviceTableEntry = _PointingDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1)
)
pointingDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pointingDevicechassisIndex"),
    (0, "MIB-Dell-10892", "pointingDeviceIndex"),
)
if mibBuilder.loadTexts:
    pointingDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceTableEntry.setDescription("""\
1100.0010.0001 This Group defines the Dell Pointing Device Table Entry.
""")
_PointingDevicechassisIndex_Type = DellObjectRange
_PointingDevicechassisIndex_Object = MibTableColumn
pointingDevicechassisIndex = _PointingDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 1),
    _PointingDevicechassisIndex_Type()
)
pointingDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDevicechassisIndex.setDescription("""\
1100.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PointingDeviceIndex_Type = DellObjectRange
_PointingDeviceIndex_Object = MibTableColumn
pointingDeviceIndex = _PointingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 2),
    _PointingDeviceIndex_Type()
)
pointingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceIndex.setDescription("""\
1100.0010.0001.0002 This attribute defines the index of the Dell Pointing
Device in this chassis.
""")
_PointingDeviceStateCapabilities_Type = DellStateCapabilities
_PointingDeviceStateCapabilities_Object = MibTableColumn
pointingDeviceStateCapabilities = _PointingDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 3),
    _PointingDeviceStateCapabilities_Type()
)
pointingDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceStateCapabilities.setDescription("""\
1100.0010.0001.0003 This attribute defines the capabilities of the Dell
Pointing Device.
""")
_PointingDeviceStateSettings_Type = DellStateSettings
_PointingDeviceStateSettings_Object = MibTableColumn
pointingDeviceStateSettings = _PointingDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 4),
    _PointingDeviceStateSettings_Type()
)
pointingDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pointingDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceStateSettings.setDescription("""\
1100.0010.0001.0004 This attribute defines the state of the Dell Pointing
Device.
""")
_PointingDeviceStatus_Type = DellStatus
_PointingDeviceStatus_Object = MibTableColumn
pointingDeviceStatus = _PointingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 5),
    _PointingDeviceStatus_Type()
)
pointingDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceStatus.setDescription("""\
1100.0010.0001.0005 This attribute defines the status of the Dell Pointing
Device.
""")
_PointingPortIndexReference_Type = DellObjectRange
_PointingPortIndexReference_Object = MibTableColumn
pointingPortIndexReference = _PointingPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 6),
    _PointingPortIndexReference_Type()
)
pointingPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingPortIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingPortIndexReference.setDescription("""\
1100.0010.0001.0006 This attribute defines the index to the associated Dell
Pointing Port in this chassis.
""")
_PointingDeviceType_Type = DellPointingDeviceType
_PointingDeviceType_Object = MibTableColumn
pointingDeviceType = _PointingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 7),
    _PointingDeviceType_Type()
)
pointingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceType.setDescription("""\
1100.0010.0001.0007 This attribute defines the type of the Dell Pointing
Device.
""")
_PointingDeviceNumberofButtons_Type = DellUnsigned8BitRange
_PointingDeviceNumberofButtons_Object = MibTableColumn
pointingDeviceNumberofButtons = _PointingDeviceNumberofButtons_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 10, 1, 8),
    _PointingDeviceNumberofButtons_Type()
)
pointingDeviceNumberofButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceNumberofButtons.setStatus("mandatory")
if mibBuilder.loadTexts:
    pointingDeviceNumberofButtons.setDescription("""\
1100.0010.0001.0008 This attribute defines the number of buttons on the Dell
Pointing Device.
""")
_KeyboardDeviceTable_Object = MibTable
keyboardDeviceTable = _KeyboardDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20)
)
if mibBuilder.loadTexts:
    keyboardDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceTable.setDescription("""\
1100.0020 This Group defines the Dell Keyboard Device Table. It references the
Dell Keyboard Port Index.
""")
_KeyboardDeviceTableEntry_Object = MibTableRow
keyboardDeviceTableEntry = _KeyboardDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1)
)
keyboardDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "keyboardDevicechassisIndex"),
    (0, "MIB-Dell-10892", "keyboardDeviceIndex"),
)
if mibBuilder.loadTexts:
    keyboardDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceTableEntry.setDescription("""\
1100.0020.0001 This Group defines the Dell Keyboard Device Table Entry.
""")
_KeyboardDevicechassisIndex_Type = DellObjectRange
_KeyboardDevicechassisIndex_Object = MibTableColumn
keyboardDevicechassisIndex = _KeyboardDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 1),
    _KeyboardDevicechassisIndex_Type()
)
keyboardDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDevicechassisIndex.setDescription("""\
1100.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_KeyboardDeviceIndex_Type = DellObjectRange
_KeyboardDeviceIndex_Object = MibTableColumn
keyboardDeviceIndex = _KeyboardDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 2),
    _KeyboardDeviceIndex_Type()
)
keyboardDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceIndex.setDescription("""\
1100.0020.0001.0002 This attribute defines the index of the Dell Keyboard
Device in this chassis.
""")
_KeyboardDeviceStateCapabilities_Type = DellStateCapabilities
_KeyboardDeviceStateCapabilities_Object = MibTableColumn
keyboardDeviceStateCapabilities = _KeyboardDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 3),
    _KeyboardDeviceStateCapabilities_Type()
)
keyboardDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceStateCapabilities.setDescription("""\
1100.0020.0001.0003 This attribute defines the capabilities of the Dell
Keyboard Device.
""")
_KeyboardDeviceStateSettings_Type = DellStateSettings
_KeyboardDeviceStateSettings_Object = MibTableColumn
keyboardDeviceStateSettings = _KeyboardDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 4),
    _KeyboardDeviceStateSettings_Type()
)
keyboardDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyboardDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceStateSettings.setDescription("""\
1100.0020.0001.0004 This attribute defines the state of the Dell Keyboard
Device.
""")
_KeyboardDeviceStatus_Type = DellStatus
_KeyboardDeviceStatus_Object = MibTableColumn
keyboardDeviceStatus = _KeyboardDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 5),
    _KeyboardDeviceStatus_Type()
)
keyboardDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceStatus.setDescription("""\
1100.0020.0001.0005 This attribute defines the status of the Dell Keyboard
Device.
""")
_KeyboardPortIndexReference_Type = DellObjectRange
_KeyboardPortIndexReference_Object = MibTableColumn
keyboardPortIndexReference = _KeyboardPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 6),
    _KeyboardPortIndexReference_Type()
)
keyboardPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardPortIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardPortIndexReference.setDescription("""\
1100.0020.0001.0006 This attribute defines the index to the associated Dell
Keyboard Port in this chassis.
""")
_KeyboardDeviceTypeName_Type = DellString
_KeyboardDeviceTypeName_Object = MibTableColumn
keyboardDeviceTypeName = _KeyboardDeviceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 7),
    _KeyboardDeviceTypeName_Type()
)
keyboardDeviceTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceTypeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceTypeName.setDescription("""\
1100.0020.0001.0007 This is the name of the Dell keyboard type.
""")
_KeyboardDeviceLayoutName_Type = DellString
_KeyboardDeviceLayoutName_Object = MibTableColumn
keyboardDeviceLayoutName = _KeyboardDeviceLayoutName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 20, 1, 8),
    _KeyboardDeviceLayoutName_Type()
)
keyboardDeviceLayoutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyboardDeviceLayoutName.setStatus("mandatory")
if mibBuilder.loadTexts:
    keyboardDeviceLayoutName.setDescription("""\
1100.0020.0001.0008 This is the name of the Dell keyboard layout.
""")
_ProcessorDeviceTable_Object = MibTable
processorDeviceTable = _ProcessorDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30)
)
if mibBuilder.loadTexts:
    processorDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceTable.setDescription("""\
1100.0030 This Group defines the Dell Processor Device Table. It references the
Dell Processor Port Index.
""")
_ProcessorDeviceTableEntry_Object = MibTableRow
processorDeviceTableEntry = _ProcessorDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1)
)
processorDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "processorDevicechassisIndex"),
    (0, "MIB-Dell-10892", "processorDeviceIndex"),
)
if mibBuilder.loadTexts:
    processorDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceTableEntry.setDescription("""\
1100.0030.0001 This Group defines the Dell Processor Device Table Entry.
""")
_ProcessorDevicechassisIndex_Type = DellObjectRange
_ProcessorDevicechassisIndex_Object = MibTableColumn
processorDevicechassisIndex = _ProcessorDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 1),
    _ProcessorDevicechassisIndex_Type()
)
processorDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDevicechassisIndex.setDescription("""\
1100.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_ProcessorDeviceIndex_Type = DellObjectRange
_ProcessorDeviceIndex_Object = MibTableColumn
processorDeviceIndex = _ProcessorDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 2),
    _ProcessorDeviceIndex_Type()
)
processorDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceIndex.setDescription("""\
1100.0030.0001.0002 This attribute defines the index of the Dell Processor
Device in this chassis.
""")
_ProcessorDeviceStateCapabilities_Type = DellStateCapabilities
_ProcessorDeviceStateCapabilities_Object = MibTableColumn
processorDeviceStateCapabilities = _ProcessorDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 3),
    _ProcessorDeviceStateCapabilities_Type()
)
processorDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceStateCapabilities.setDescription("""\
1100.0030.0001.0003 This attribute defines the capabilities of the Dell
Processor Device.
""")
_ProcessorDeviceStateSettings_Type = DellStateSettings
_ProcessorDeviceStateSettings_Object = MibTableColumn
processorDeviceStateSettings = _ProcessorDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 4),
    _ProcessorDeviceStateSettings_Type()
)
processorDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processorDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceStateSettings.setDescription("""\
1100.0030.0001.0004 This attribute defines the state of the Dell Processor
Device.
""")
_ProcessorDeviceStatus_Type = DellStatus
_ProcessorDeviceStatus_Object = MibTableColumn
processorDeviceStatus = _ProcessorDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 5),
    _ProcessorDeviceStatus_Type()
)
processorDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceStatus.setDescription("""\
1100.0030.0001.0005 This attribute defines the status of the Dell Processor
Device.
""")
_ProcessorPortIndexReference_Type = DellObjectRange
_ProcessorPortIndexReference_Object = MibTableColumn
processorPortIndexReference = _ProcessorPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 6),
    _ProcessorPortIndexReference_Type()
)
processorPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorPortIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorPortIndexReference.setDescription("""\
1100.0030.0001.0006 This attribute defines the index to the associated Dell
Processor Port in this chassis.
""")
_ProcessorDeviceType_Type = DellProcessorDeviceType
_ProcessorDeviceType_Object = MibTableColumn
processorDeviceType = _ProcessorDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 7),
    _ProcessorDeviceType_Type()
)
processorDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceType.setDescription("""\
1100.0030.0001.0007 This attribute defines the type of Dell Processor Device.
""")
_ProcessorDeviceManufacturerName_Type = DellString
_ProcessorDeviceManufacturerName_Object = MibTableColumn
processorDeviceManufacturerName = _ProcessorDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 8),
    _ProcessorDeviceManufacturerName_Type()
)
processorDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceManufacturerName.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceManufacturerName.setDescription("""\
1100.0030.0001.0008 This is the name of manufacturer of the Dell processor.
""")
_ProcessorDeviceStatusState_Type = DellProcessorDeviceStatusState
_ProcessorDeviceStatusState_Object = MibTableColumn
processorDeviceStatusState = _ProcessorDeviceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 9),
    _ProcessorDeviceStatusState_Type()
)
processorDeviceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceStatusState.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceStatusState.setDescription("""\
1100.0030.0001.0009 This attribute defines the status state of the Dell
Processor Device.
""")
_ProcessorDeviceFamily_Type = DellProcessorDeviceFamily
_ProcessorDeviceFamily_Object = MibTableColumn
processorDeviceFamily = _ProcessorDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 10),
    _ProcessorDeviceFamily_Type()
)
processorDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceFamily.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceFamily.setDescription("""\
1100.0030.0001.0010 This attribute defines the family of the Dell Processor
Device.
""")
_ProcessorDeviceMaximumSpeed_Type = DellUnsigned32BitRange
_ProcessorDeviceMaximumSpeed_Object = MibTableColumn
processorDeviceMaximumSpeed = _ProcessorDeviceMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 11),
    _ProcessorDeviceMaximumSpeed_Type()
)
processorDeviceMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceMaximumSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceMaximumSpeed.setDescription("""\
1100.0030.0001.0011 This attribute defines the maximum speed of the Dell
Processor Device in MHz, a 0 (zero) indicates the speed is unknown.
""")
_ProcessorDeviceCurrentSpeed_Type = DellUnsigned32BitRange
_ProcessorDeviceCurrentSpeed_Object = MibTableColumn
processorDeviceCurrentSpeed = _ProcessorDeviceCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 12),
    _ProcessorDeviceCurrentSpeed_Type()
)
processorDeviceCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceCurrentSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceCurrentSpeed.setDescription("""\
1100.0030.0001.0012 This attribute defines the current speed of the Dell
Processor Device in MHz, a 0 (zero) indicates the speed is unknown.
""")
_ProcessorDeviceExternalClockSpeed_Type = DellUnsigned32BitRange
_ProcessorDeviceExternalClockSpeed_Object = MibTableColumn
processorDeviceExternalClockSpeed = _ProcessorDeviceExternalClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 13),
    _ProcessorDeviceExternalClockSpeed_Type()
)
processorDeviceExternalClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceExternalClockSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceExternalClockSpeed.setDescription("""\
1100.0030.0001.0013 This attribute defines the speed of the external clock for
the Dell Processor Device in MHz, a 0 (zero) indicates the speed is unknown.
""")
_ProcessorDeviceVoltage_Type = DellSigned32BitRange
_ProcessorDeviceVoltage_Object = MibTableColumn
processorDeviceVoltage = _ProcessorDeviceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 14),
    _ProcessorDeviceVoltage_Type()
)
processorDeviceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceVoltage.setDescription("""\
1100.0030.0001.0014 This attribute defines the voltage powering the Dell
Processor Device in millivolts, a 0 (zero) indicates the speed is unknown.
""")
_ProcessorDeviceUpgradeInformation_Type = DellProcessorUpgradeInformation
_ProcessorDeviceUpgradeInformation_Object = MibTableColumn
processorDeviceUpgradeInformation = _ProcessorDeviceUpgradeInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 15),
    _ProcessorDeviceUpgradeInformation_Type()
)
processorDeviceUpgradeInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceUpgradeInformation.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceUpgradeInformation.setDescription("""\
1100.0030.0001.0015 This attribute defines the processor upgrade information
for the Dell Processor Device.
""")
_ProcessorDeviceVersionName_Type = DellString
_ProcessorDeviceVersionName_Object = MibTableColumn
processorDeviceVersionName = _ProcessorDeviceVersionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 30, 1, 16),
    _ProcessorDeviceVersionName_Type()
)
processorDeviceVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorDeviceVersionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    processorDeviceVersionName.setDescription("""\
1100.0030.0001.0016 This is the name of the version of the Dell processor.
""")
_CacheDeviceTable_Object = MibTable
cacheDeviceTable = _CacheDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40)
)
if mibBuilder.loadTexts:
    cacheDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceTable.setDescription("""\
1100.0040 This Group defines the Dell Cache Device Table.
""")
_CacheDeviceTableEntry_Object = MibTableRow
cacheDeviceTableEntry = _CacheDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1)
)
cacheDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cacheDevicechassisIndex"),
    (0, "MIB-Dell-10892", "cacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    cacheDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceTableEntry.setDescription("""\
1100.0040.0001 This Group defines the Dell Cache Device Table Entry.
""")
_CacheDevicechassisIndex_Type = DellObjectRange
_CacheDevicechassisIndex_Object = MibTableColumn
cacheDevicechassisIndex = _CacheDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 1),
    _CacheDevicechassisIndex_Type()
)
cacheDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDevicechassisIndex.setDescription("""\
1100.0040.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CacheDeviceIndex_Type = DellObjectRange
_CacheDeviceIndex_Object = MibTableColumn
cacheDeviceIndex = _CacheDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 2),
    _CacheDeviceIndex_Type()
)
cacheDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceIndex.setDescription("""\
1100.0040.0001.0002 This attribute defines the index of the Dell Cache Device
in this chassis.
""")
_CacheDeviceStateCapabilities_Type = DellStateCapabilities
_CacheDeviceStateCapabilities_Object = MibTableColumn
cacheDeviceStateCapabilities = _CacheDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 3),
    _CacheDeviceStateCapabilities_Type()
)
cacheDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceStateCapabilities.setDescription("""\
1100.0040.0001.0003 This attribute defines the capabilities of the Dell Cache
Device.
""")
_CacheDeviceStateSettings_Type = DellStateSettings
_CacheDeviceStateSettings_Object = MibTableColumn
cacheDeviceStateSettings = _CacheDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 4),
    _CacheDeviceStateSettings_Type()
)
cacheDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceStateSettings.setDescription("""\
1100.0040.0001.0004 This attribute defines the state of the Dell Cache Device.
""")
_CacheDeviceStatus_Type = DellStatus
_CacheDeviceStatus_Object = MibTableColumn
cacheDeviceStatus = _CacheDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 5),
    _CacheDeviceStatus_Type()
)
cacheDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceStatus.setDescription("""\
1100.0040.0001.0005 This attribute defines the status of the Dell Cache Device.
""")
_CacheDeviceprocessorDeviceIndexReference_Type = DellObjectRange
_CacheDeviceprocessorDeviceIndexReference_Object = MibTableColumn
cacheDeviceprocessorDeviceIndexReference = _CacheDeviceprocessorDeviceIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 6),
    _CacheDeviceprocessorDeviceIndexReference_Type()
)
cacheDeviceprocessorDeviceIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceprocessorDeviceIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceprocessorDeviceIndexReference.setDescription("""\
1100.0040.0001.0006 This attribute defines the index number of the processor
device that this Dell cache Device is associated with.
""")
_CacheDeviceType_Type = DellCacheDeviceType
_CacheDeviceType_Object = MibTableColumn
cacheDeviceType = _CacheDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 7),
    _CacheDeviceType_Type()
)
cacheDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceType.setDescription("""\
1100.0040.0001.0007 This attribute defines the type of Dell Cache Device.
""")
_CacheDeviceLocation_Type = DellCacheDeviceLocation
_CacheDeviceLocation_Object = MibTableColumn
cacheDeviceLocation = _CacheDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 8),
    _CacheDeviceLocation_Type()
)
cacheDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceLocation.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceLocation.setDescription("""\
1100.0040.0001.0008 This is the location of the Dell cache.
""")
_CacheDeviceStatusState_Type = DellCacheDeviceStatusState
_CacheDeviceStatusState_Object = MibTableColumn
cacheDeviceStatusState = _CacheDeviceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 9),
    _CacheDeviceStatusState_Type()
)
cacheDeviceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceStatusState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceStatusState.setDescription("""\
1100.0040.0001.0009 This attribute defines the status state of the Dell Cache
Device.
""")
_CacheDeviceExternalSocketName_Type = DellString
_CacheDeviceExternalSocketName_Object = MibTableColumn
cacheDeviceExternalSocketName = _CacheDeviceExternalSocketName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 10),
    _CacheDeviceExternalSocketName_Type()
)
cacheDeviceExternalSocketName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceExternalSocketName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceExternalSocketName.setDescription("""\
1100.0040.0001.0010 This is the name of the external socket name of the Dell
cache if the cache is socketed.
""")
_CacheDeviceLevel_Type = DellCacheDeviceLevel
_CacheDeviceLevel_Object = MibTableColumn
cacheDeviceLevel = _CacheDeviceLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 11),
    _CacheDeviceLevel_Type()
)
cacheDeviceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceLevel.setDescription("""\
1100.0040.0001.0011 This attribute defines the level of the Dell Cache Device.
""")
_CacheDeviceMaximumSize_Type = DellUnsigned32BitRange
_CacheDeviceMaximumSize_Object = MibTableColumn
cacheDeviceMaximumSize = _CacheDeviceMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 12),
    _CacheDeviceMaximumSize_Type()
)
cacheDeviceMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceMaximumSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceMaximumSize.setDescription("""\
1100.0040.0001.0012 This attribute defines the maximum size of the Dell Cache
Device in KBytes, a 0 (zero) indicates the size is unknown.
""")
_CacheDeviceCurrentSize_Type = DellUnsigned32BitRange
_CacheDeviceCurrentSize_Object = MibTableColumn
cacheDeviceCurrentSize = _CacheDeviceCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 13),
    _CacheDeviceCurrentSize_Type()
)
cacheDeviceCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceCurrentSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceCurrentSize.setDescription("""\
1100.0040.0001.0013 This attribute defines the current size of the Dell Cache
Device in KBytes, a 0 (zero) indicates the size is unknown.
""")
_CacheDeviceSpeed_Type = DellUnsigned32BitRange
_CacheDeviceSpeed_Object = MibTableColumn
cacheDeviceSpeed = _CacheDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 14),
    _CacheDeviceSpeed_Type()
)
cacheDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceSpeed.setDescription("""\
1100.0040.0001.0014 This attribute defines the speed of the Dell Cache Device
in nanoseconds, a 0 (zero) indicates the speed is unknown.
""")
_CacheDeviceWritePolicy_Type = DellCacheDeviceWritePolicy
_CacheDeviceWritePolicy_Object = MibTableColumn
cacheDeviceWritePolicy = _CacheDeviceWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 15),
    _CacheDeviceWritePolicy_Type()
)
cacheDeviceWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceWritePolicy.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceWritePolicy.setDescription("""\
1100.0040.0001.0015 This attribute defines the write policy of the Dell Cache
Device.
""")
_CacheDeviceIsSocketed_Type = DellBoolean
_CacheDeviceIsSocketed_Object = MibTableColumn
cacheDeviceIsSocketed = _CacheDeviceIsSocketed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 16),
    _CacheDeviceIsSocketed_Type()
)
cacheDeviceIsSocketed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceIsSocketed.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceIsSocketed.setDescription("""\
1100.0040.0001.0016 This is the attribute that defines if the Dell cache is
socketed or not.
""")
_CacheDeviceECCType_Type = DellCacheDeviceECCType
_CacheDeviceECCType_Object = MibTableColumn
cacheDeviceECCType = _CacheDeviceECCType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 17),
    _CacheDeviceECCType_Type()
)
cacheDeviceECCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceECCType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceECCType.setDescription("""\
1100.0040.0001.0017 This is the type of error correction in use by the Dell
cache.
""")
_CacheDeviceAssociativity_Type = DellCacheDeviceAssociativity
_CacheDeviceAssociativity_Object = MibTableColumn
cacheDeviceAssociativity = _CacheDeviceAssociativity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 18),
    _CacheDeviceAssociativity_Type()
)
cacheDeviceAssociativity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceAssociativity.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceAssociativity.setDescription("""\
1100.0040.0001.0018 This is the type of associativity in use by the Dell cache.
""")
_CacheDeviceSupportedType_Type = DellCacheDeviceSRAMType
_CacheDeviceSupportedType_Object = MibTableColumn
cacheDeviceSupportedType = _CacheDeviceSupportedType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 19),
    _CacheDeviceSupportedType_Type()
)
cacheDeviceSupportedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceSupportedType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceSupportedType.setDescription("""\
1100.0040.0001.0019 This is the type of SRAM the Dell cache can support.
""")
_CacheDeviceCurrentType_Type = DellCacheDeviceSRAMType
_CacheDeviceCurrentType_Object = MibTableColumn
cacheDeviceCurrentType = _CacheDeviceCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 40, 1, 20),
    _CacheDeviceCurrentType_Type()
)
cacheDeviceCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeviceCurrentType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cacheDeviceCurrentType.setDescription("""\
1100.0040.0001.0020 This is the current type of SRAM for the Dell cache.
""")
_MemoryDeviceTable_Object = MibTable
memoryDeviceTable = _MemoryDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50)
)
if mibBuilder.loadTexts:
    memoryDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceTable.setDescription("""\
1100.0050 This Group defines the Dell Memory Device Table.
""")
_MemoryDeviceTableEntry_Object = MibTableRow
memoryDeviceTableEntry = _MemoryDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1)
)
memoryDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "memoryDevicechassisIndex"),
    (0, "MIB-Dell-10892", "memoryDeviceIndex"),
)
if mibBuilder.loadTexts:
    memoryDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceTableEntry.setDescription("""\
1100.0050.0001 This Group defines the Dell Memory Device Table Entry.
""")
_MemoryDevicechassisIndex_Type = DellObjectRange
_MemoryDevicechassisIndex_Object = MibTableColumn
memoryDevicechassisIndex = _MemoryDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 1),
    _MemoryDevicechassisIndex_Type()
)
memoryDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDevicechassisIndex.setDescription("""\
1100.0050.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_MemoryDeviceIndex_Type = DellObjectRange
_MemoryDeviceIndex_Object = MibTableColumn
memoryDeviceIndex = _MemoryDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 2),
    _MemoryDeviceIndex_Type()
)
memoryDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceIndex.setDescription("""\
1100.0050.0001.0002 This attribute defines the index of the Dell Memory Device
in this chassis.
""")
_MemoryDeviceStateCapabilities_Type = DellStateCapabilities
_MemoryDeviceStateCapabilities_Object = MibTableColumn
memoryDeviceStateCapabilities = _MemoryDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 3),
    _MemoryDeviceStateCapabilities_Type()
)
memoryDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceStateCapabilities.setDescription("""\
1100.0050.0001.0003 This attribute defines the capabilities of the Dell Memory
Device.
""")
_MemoryDeviceStateSettings_Type = DellStateSettings
_MemoryDeviceStateSettings_Object = MibTableColumn
memoryDeviceStateSettings = _MemoryDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 4),
    _MemoryDeviceStateSettings_Type()
)
memoryDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceStateSettings.setDescription("""\
1100.0050.0001.0004 This attribute defines the state of the Dell Memory Device.
""")
_MemoryDeviceStatus_Type = DellStatus
_MemoryDeviceStatus_Object = MibTableColumn
memoryDeviceStatus = _MemoryDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 5),
    _MemoryDeviceStatus_Type()
)
memoryDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceStatus.setDescription("""\
1100.0050.0001.0005 This attribute defines the status of the Dell Memory
Device.
""")
_MemoryDeviceMemoryPortIndexReference_Type = DellObjectRange
_MemoryDeviceMemoryPortIndexReference_Object = MibTableColumn
memoryDeviceMemoryPortIndexReference = _MemoryDeviceMemoryPortIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 6),
    _MemoryDeviceMemoryPortIndexReference_Type()
)
memoryDeviceMemoryPortIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMemoryPortIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMemoryPortIndexReference.setDescription("""\
1100.0050.0001.0006 This attribute defines the index of the Dell memory port
that this memory device is part of.
""")
_MemoryDeviceType_Type = DellMemoryDeviceType
_MemoryDeviceType_Object = MibTableColumn
memoryDeviceType = _MemoryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 7),
    _MemoryDeviceType_Type()
)
memoryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceType.setDescription("""\
1100.0050.0001.0007 This attribute defines the type of the Dell Memory Device.
""")
_MemoryDeviceLocationName_Type = DellString
_MemoryDeviceLocationName_Object = MibTableColumn
memoryDeviceLocationName = _MemoryDeviceLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 8),
    _MemoryDeviceLocationName_Type()
)
memoryDeviceLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceLocationName.setDescription("""\
1100.0050.0001.0008 This attribute defines location name of the Dell Memory
Device.
""")
_MemoryDeviceErrorCount_Type = DellSigned32BitRange
_MemoryDeviceErrorCount_Object = MibTableColumn
memoryDeviceErrorCount = _MemoryDeviceErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 9),
    _MemoryDeviceErrorCount_Type()
)
memoryDeviceErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDeviceErrorCount.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceErrorCount.setDescription("""\
1100.0050.0001.0009 This attribute defines the total number of ECC errors
detected by the Dell Memory Device. Writing a 0 (zero) to this variable, will
reset the devices error counts.
""")
_MemoryDeviceBankLocationName_Type = DellString
_MemoryDeviceBankLocationName_Object = MibTableColumn
memoryDeviceBankLocationName = _MemoryDeviceBankLocationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 10),
    _MemoryDeviceBankLocationName_Type()
)
memoryDeviceBankLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDeviceBankLocationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceBankLocationName.setDescription("""\
1100.0050.0001.0010 This attribute defines bank location name of the Dell
Memory Device.
""")
_MemoryDeviceTypeDetails_Type = DellMemoryDeviceTypeDetails
_MemoryDeviceTypeDetails_Object = MibTableColumn
memoryDeviceTypeDetails = _MemoryDeviceTypeDetails_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 11),
    _MemoryDeviceTypeDetails_Type()
)
memoryDeviceTypeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTypeDetails.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceTypeDetails.setDescription("""\
1100.0050.0001.0011 This attribute defines the detailed type of the Dell Memory
Device.
""")
_MemoryDeviceFormFactor_Type = DellMemoryDeviceFormFactor
_MemoryDeviceFormFactor_Object = MibTableColumn
memoryDeviceFormFactor = _MemoryDeviceFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 12),
    _MemoryDeviceFormFactor_Type()
)
memoryDeviceFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceFormFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceFormFactor.setDescription("""\
1100.0050.0001.0012 This attribute defines the form factor of the Dell Memory
Device.
""")
_MemoryDeviceSet_Type = DellUnsigned32BitRange
_MemoryDeviceSet_Object = MibTableColumn
memoryDeviceSet = _MemoryDeviceSet_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 13),
    _MemoryDeviceSet_Type()
)
memoryDeviceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSet.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceSet.setDescription("""\
1100.0050.0001.0013 This attribute defines if the Dell Memory Device is a part
of a set. 0 (zero) indicates it is not part of a set, 2,147,483,647 indicates
it is unknown if it is a part of a set.
""")
_MemoryDeviceSize_Type = DellUnsigned32BitRange
_MemoryDeviceSize_Object = MibTableColumn
memoryDeviceSize = _MemoryDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 14),
    _MemoryDeviceSize_Type()
)
memoryDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceSize.setDescription("""\
1100.0050.0001.0014 This attribute defines the size in KBytes of the Dell
Memory Device. 0 (zero) indicates no memory installed, 2,147,483,647 indicates
an unknown memory size.
""")
_MemoryDeviceSpeed_Type = DellUnsigned32BitRange
_MemoryDeviceSpeed_Object = MibTableColumn
memoryDeviceSpeed = _MemoryDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 15),
    _MemoryDeviceSpeed_Type()
)
memoryDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceSpeed.setDescription("""\
1100.0050.0001.0015 This attribute defines the speed in NanoSeconds of the Dell
Memory Device. 0 (zero) indicates an unknown speed.
""")
_MemoryDeviceTotalBusWidth_Type = DellUnsigned32BitRange
_MemoryDeviceTotalBusWidth_Object = MibTableColumn
memoryDeviceTotalBusWidth = _MemoryDeviceTotalBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 16),
    _MemoryDeviceTotalBusWidth_Type()
)
memoryDeviceTotalBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTotalBusWidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceTotalBusWidth.setDescription("""\
1100.0050.0001.0016 This attribute defines the total number bits, including
ECC, used by the Dell Memory Device. 2,147,483,647 indicates an unknown number
of bits.
""")
_MemoryDeviceTotalDataBusWidth_Type = DellUnsigned32BitRange
_MemoryDeviceTotalDataBusWidth_Object = MibTableColumn
memoryDeviceTotalDataBusWidth = _MemoryDeviceTotalDataBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 17),
    _MemoryDeviceTotalDataBusWidth_Type()
)
memoryDeviceTotalDataBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceTotalDataBusWidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceTotalDataBusWidth.setDescription("""\
1100.0050.0001.0017 This attribute defines the total number of data bits used
by the Dell Memory Device. 2,147,483,647 indicates an unknown number of bits.
""")
_MemoryDeviceSingleBitErrorCount_Type = DellSigned32BitRange
_MemoryDeviceSingleBitErrorCount_Object = MibTableColumn
memoryDeviceSingleBitErrorCount = _MemoryDeviceSingleBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 18),
    _MemoryDeviceSingleBitErrorCount_Type()
)
memoryDeviceSingleBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceSingleBitErrorCount.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceSingleBitErrorCount.setDescription("""\
1100.0050.0001.0018 This attribute defines the total number of single bit ECC
errors detected by the Dell Memory Device.
""")
_MemoryDeviceMultiBitErrorCount_Type = DellSigned32BitRange
_MemoryDeviceMultiBitErrorCount_Object = MibTableColumn
memoryDeviceMultiBitErrorCount = _MemoryDeviceMultiBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 50, 1, 19),
    _MemoryDeviceMultiBitErrorCount_Type()
)
memoryDeviceMultiBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMultiBitErrorCount.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMultiBitErrorCount.setDescription("""\
1100.0050.0001.0019 This attribute defines the total number of multibit ECC
errors detected by the Dell Memory Device.
""")
_MemoryDeviceMappedAddressTable_Object = MibTable
memoryDeviceMappedAddressTable = _MemoryDeviceMappedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60)
)
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressTable.setDescription("""\
1100.0060 This Group defines the Dell Memory Device Mapped Address Table. It
references the Memory Device Index.
""")
_MemoryDeviceMappedAddressTableEntry_Object = MibTableRow
memoryDeviceMappedAddressTableEntry = _MemoryDeviceMappedAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1)
)
memoryDeviceMappedAddressTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "memoryDeviceMappedAddresschassisIndex"),
    (0, "MIB-Dell-10892", "memoryDeviceMappedAddressIndex"),
)
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressTableEntry.setDescription("""\
1100.0060.0001 This Group defines the Dell Memory Device Mapped Address Table
Entry.
""")
_MemoryDeviceMappedAddresschassisIndex_Type = DellObjectRange
_MemoryDeviceMappedAddresschassisIndex_Object = MibTableColumn
memoryDeviceMappedAddresschassisIndex = _MemoryDeviceMappedAddresschassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 1),
    _MemoryDeviceMappedAddresschassisIndex_Type()
)
memoryDeviceMappedAddresschassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddresschassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddresschassisIndex.setDescription("""\
1100.0060.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_MemoryDeviceMappedAddressIndex_Type = DellObjectRange
_MemoryDeviceMappedAddressIndex_Object = MibTableColumn
memoryDeviceMappedAddressIndex = _MemoryDeviceMappedAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 2),
    _MemoryDeviceMappedAddressIndex_Type()
)
memoryDeviceMappedAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressIndex.setDescription("""\
1100.0060.0001.0002 This attribute defines the index of the Dell Memory Device
Mapped Address in this chassis.
""")
_MemoryDeviceMappedAddressStateCapabilities_Type = DellStateCapabilities
_MemoryDeviceMappedAddressStateCapabilities_Object = MibTableColumn
memoryDeviceMappedAddressStateCapabilities = _MemoryDeviceMappedAddressStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 3),
    _MemoryDeviceMappedAddressStateCapabilities_Type()
)
memoryDeviceMappedAddressStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStateCapabilities.setDescription("""\
1100.0060.0001.0003 This attribute defines the capabilities of the Dell Memory
Device Mapped Address.
""")
_MemoryDeviceMappedAddressStateSettings_Type = DellStateSettings
_MemoryDeviceMappedAddressStateSettings_Object = MibTableColumn
memoryDeviceMappedAddressStateSettings = _MemoryDeviceMappedAddressStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 4),
    _MemoryDeviceMappedAddressStateSettings_Type()
)
memoryDeviceMappedAddressStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStateSettings.setDescription("""\
1100.0060.0001.0004 This attribute defines the state of the Dell Memory Device
Mapped Address.
""")
_MemoryDeviceMappedAddressStatus_Type = DellStatus
_MemoryDeviceMappedAddressStatus_Object = MibTableColumn
memoryDeviceMappedAddressStatus = _MemoryDeviceMappedAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 5),
    _MemoryDeviceMappedAddressStatus_Type()
)
memoryDeviceMappedAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStatus.setDescription("""\
1100.0060.0001.0005 This attribute defines the status of the Dell Memory Device
Mapped Address.
""")
_MemoryDeviceIndexReference_Type = DellObjectRange
_MemoryDeviceIndexReference_Object = MibTableColumn
memoryDeviceIndexReference = _MemoryDeviceIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 6),
    _MemoryDeviceIndexReference_Type()
)
memoryDeviceIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceIndexReference.setDescription("""\
1100.0060.0001.0006 This attribute defines the index of the memory device(s)
associated with this Dell Memory Device Mapped Address.
""")
_MemoryDeviceMappedAddressRowPosition_Type = DellUnsigned32BitRange
_MemoryDeviceMappedAddressRowPosition_Object = MibTableColumn
memoryDeviceMappedAddressRowPosition = _MemoryDeviceMappedAddressRowPosition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 7),
    _MemoryDeviceMappedAddressRowPosition_Type()
)
memoryDeviceMappedAddressRowPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressRowPosition.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressRowPosition.setDescription("""\
1100.0060.0001.0007 This attribute defines the position of the referenced
memory in a row of the Dell Memory Device Mapped Address. 2,147,483,647
indicates an unknown position.
""")
_MemoryDeviceMappedAddressInterleavePosition_Type = DellUnsigned32BitRange
_MemoryDeviceMappedAddressInterleavePosition_Object = MibTableColumn
memoryDeviceMappedAddressInterleavePosition = _MemoryDeviceMappedAddressInterleavePosition_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 8),
    _MemoryDeviceMappedAddressInterleavePosition_Type()
)
memoryDeviceMappedAddressInterleavePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressInterleavePosition.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressInterleavePosition.setDescription("""\
1100.0060.0001.0008 This attribute defines the position of the referenced
memory in an interleave of the Dell Memory Device Mapped Address. 2,147,483,647
indicates an unknown position.
""")
_MemoryDeviceMappedAddressInterleaveDepth_Type = DellUnsigned32BitRange
_MemoryDeviceMappedAddressInterleaveDepth_Object = MibTableColumn
memoryDeviceMappedAddressInterleaveDepth = _MemoryDeviceMappedAddressInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 9),
    _MemoryDeviceMappedAddressInterleaveDepth_Type()
)
memoryDeviceMappedAddressInterleaveDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressInterleaveDepth.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressInterleaveDepth.setDescription("""\
1100.0060.0001.0009 This attribute defines the maximum number of consecutive
rows from the referenced Memory Device that are accessed in a single
interleaved transfer in the Dell Memory Device Mapped Address. 2,147,483,647
indicates an unknown number of rows.
""")
_MemoryDeviceMappedAddressStartingAddress_Type = DellUnsigned64BitRange
_MemoryDeviceMappedAddressStartingAddress_Object = MibTableColumn
memoryDeviceMappedAddressStartingAddress = _MemoryDeviceMappedAddressStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 10),
    _MemoryDeviceMappedAddressStartingAddress_Type()
)
memoryDeviceMappedAddressStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStartingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressStartingAddress.setDescription("""\
1100.0060.0001.0010 This attribute defines the physical starting address in
KBytes of the Dell Memory Device Mapped Address.
""")
_MemoryDeviceMappedAddressEndingAddress_Type = DellUnsigned64BitRange
_MemoryDeviceMappedAddressEndingAddress_Object = MibTableColumn
memoryDeviceMappedAddressEndingAddress = _MemoryDeviceMappedAddressEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 60, 1, 11),
    _MemoryDeviceMappedAddressEndingAddress_Type()
)
memoryDeviceMappedAddressEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressEndingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    memoryDeviceMappedAddressEndingAddress.setDescription("""\
1100.0060.0001.0011 This attribute defines the physical ending address in
KBytes of the Dell Memory Device Mapped Address.
""")
_GenericDeviceTable_Object = MibTable
genericDeviceTable = _GenericDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70)
)
if mibBuilder.loadTexts:
    genericDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceTable.setDescription("""\
1100.0070 This Group defines the Dell Generic Device Table.
""")
_GenericDeviceTableEntry_Object = MibTableRow
genericDeviceTableEntry = _GenericDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1)
)
genericDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "genericDevicechassisIndex"),
    (0, "MIB-Dell-10892", "genericDeviceIndex"),
)
if mibBuilder.loadTexts:
    genericDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceTableEntry.setDescription("""\
1100.0070.0001 This Group defines the Dell Generic Device Table Entry.
""")
_GenericDevicechassisIndex_Type = DellObjectRange
_GenericDevicechassisIndex_Object = MibTableColumn
genericDevicechassisIndex = _GenericDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 1),
    _GenericDevicechassisIndex_Type()
)
genericDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDevicechassisIndex.setDescription("""\
1100.0070.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_GenericDeviceIndex_Type = DellObjectRange
_GenericDeviceIndex_Object = MibTableColumn
genericDeviceIndex = _GenericDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 2),
    _GenericDeviceIndex_Type()
)
genericDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceIndex.setDescription("""\
1100.0070.0001.0002 This attribute defines the index of the Dell Generic Device
in this chassis.
""")
_GenericDeviceStateCapabilities_Type = DellStateCapabilities
_GenericDeviceStateCapabilities_Object = MibTableColumn
genericDeviceStateCapabilities = _GenericDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 3),
    _GenericDeviceStateCapabilities_Type()
)
genericDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceStateCapabilities.setDescription("""\
1100.0070.0001.0003 This attribute defines the capabilities of the Dell Generic
Device.
""")
_GenericDeviceStateSettings_Type = DellStateSettings
_GenericDeviceStateSettings_Object = MibTableColumn
genericDeviceStateSettings = _GenericDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 4),
    _GenericDeviceStateSettings_Type()
)
genericDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceStateSettings.setDescription("""\
1100.0070.0001.0004 This attribute defines the state of the Dell Generic
Device.
""")
_GenericDeviceStatus_Type = DellStatus
_GenericDeviceStatus_Object = MibTableColumn
genericDeviceStatus = _GenericDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 5),
    _GenericDeviceStatus_Type()
)
genericDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceStatus.setDescription("""\
1100.0070.0001.0005 This attribute defines the status of the Dell Generic
Device.
""")
_GenericDeviceSystemSlotIndexReference_Type = DellObjectRange
_GenericDeviceSystemSlotIndexReference_Object = MibTableColumn
genericDeviceSystemSlotIndexReference = _GenericDeviceSystemSlotIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 6),
    _GenericDeviceSystemSlotIndexReference_Type()
)
genericDeviceSystemSlotIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceSystemSlotIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceSystemSlotIndexReference.setDescription("""\
1100.0070.0001.0006 This attribute defines the index of the system slot this
generic device is plugged into.
""")
_GenericDeviceType_Type = DellGenericDeviceType
_GenericDeviceType_Object = MibTableColumn
genericDeviceType = _GenericDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 7),
    _GenericDeviceType_Type()
)
genericDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceType.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceType.setDescription("""\
1100.0070.0001.0007 This attribute defines the type of the Dell Generic Device.
""")
_GenericDeviceName_Type = DellString
_GenericDeviceName_Object = MibTableColumn
genericDeviceName = _GenericDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 70, 1, 8),
    _GenericDeviceName_Type()
)
genericDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericDeviceName.setStatus("mandatory")
if mibBuilder.loadTexts:
    genericDeviceName.setDescription("""\
1100.0070.0001.0008 This is the name of the Dell Generic Device.
""")
_PCIDeviceTable_Object = MibTable
pCIDeviceTable = _PCIDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80)
)
if mibBuilder.loadTexts:
    pCIDeviceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceTable.setDescription("""\
1100.0080 This Group defines the Dell PCI Device Detail Table.
""")
_PCIDeviceTableEntry_Object = MibTableRow
pCIDeviceTableEntry = _PCIDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1)
)
pCIDeviceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pCIDevicechassisIndex"),
    (0, "MIB-Dell-10892", "pCIDeviceIndex"),
)
if mibBuilder.loadTexts:
    pCIDeviceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceTableEntry.setDescription("""\
1100.0080.0001 This Group defines the Dell PCI Device Table Entry.
""")
_PCIDevicechassisIndex_Type = DellObjectRange
_PCIDevicechassisIndex_Object = MibTableColumn
pCIDevicechassisIndex = _PCIDevicechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 1),
    _PCIDevicechassisIndex_Type()
)
pCIDevicechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDevicechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDevicechassisIndex.setDescription("""\
1100.0080.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PCIDeviceIndex_Type = DellObjectRange
_PCIDeviceIndex_Object = MibTableColumn
pCIDeviceIndex = _PCIDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 2),
    _PCIDeviceIndex_Type()
)
pCIDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceIndex.setDescription("""\
1100.0080.0001.0002 This attribute defines the index of the Dell PCI Device in
this chassis.
""")
_PCIDeviceStateCapabilities_Type = DellStateCapabilities
_PCIDeviceStateCapabilities_Object = MibTableColumn
pCIDeviceStateCapabilities = _PCIDeviceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 3),
    _PCIDeviceStateCapabilities_Type()
)
pCIDeviceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceStateCapabilities.setDescription("""\
1100.0080.0001.0003 This attribute defines the capabilities of the Dell PCI
Device.
""")
_PCIDeviceStateSettings_Type = DellStateSettings
_PCIDeviceStateSettings_Object = MibTableColumn
pCIDeviceStateSettings = _PCIDeviceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 4),
    _PCIDeviceStateSettings_Type()
)
pCIDeviceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCIDeviceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceStateSettings.setDescription("""\
1100.0080.0001.0004 This attribute defines the state of the Dell PCI Device.
""")
_PCIDeviceStatus_Type = DellStatus
_PCIDeviceStatus_Object = MibTableColumn
pCIDeviceStatus = _PCIDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 5),
    _PCIDeviceStatus_Type()
)
pCIDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceStatus.setDescription("""\
1100.0080.0001.0005 This attribute defines the status of the Dell PCI Device.
""")
_PCIDeviceSystemSlotIndexReference_Type = DellObjectRange
_PCIDeviceSystemSlotIndexReference_Object = MibTableColumn
pCIDeviceSystemSlotIndexReference = _PCIDeviceSystemSlotIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 6),
    _PCIDeviceSystemSlotIndexReference_Type()
)
pCIDeviceSystemSlotIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceSystemSlotIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceSystemSlotIndexReference.setDescription("""\
1100.0080.0001.0006 This attribute defines the index number of the system slot
that this Dell PCI Device is in.
""")
_PCIDeviceDataBusWidth_Type = DellUnsigned32BitRange
_PCIDeviceDataBusWidth_Object = MibTableColumn
pCIDeviceDataBusWidth = _PCIDeviceDataBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 7),
    _PCIDeviceDataBusWidth_Type()
)
pCIDeviceDataBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceDataBusWidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceDataBusWidth.setDescription("""\
1100.0080.0001.0007 This attribute defines the bus width of the Dell PCI Device
in this chassis.
""")
_PCIDeviceManufacturerName_Type = DellString
_PCIDeviceManufacturerName_Object = MibTableColumn
pCIDeviceManufacturerName = _PCIDeviceManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 8),
    _PCIDeviceManufacturerName_Type()
)
pCIDeviceManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceManufacturerName.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceManufacturerName.setDescription("""\
1100.0080.0001.0008 This is the name of the Dell PCI Device manufacturer.
""")
_PCIDeviceDescriptionName_Type = DellString
_PCIDeviceDescriptionName_Object = MibTableColumn
pCIDeviceDescriptionName = _PCIDeviceDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 9),
    _PCIDeviceDescriptionName_Type()
)
pCIDeviceDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceDescriptionName.setDescription("""\
1100.0080.0001.0009 This is the descriptive name of the Dell PCI Device.
""")
_PCIDeviceSpeed_Type = DellUnsigned32BitRange
_PCIDeviceSpeed_Object = MibTableColumn
pCIDeviceSpeed = _PCIDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 10),
    _PCIDeviceSpeed_Type()
)
pCIDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceSpeed.setDescription("""\
1100.0080.0001.0010 This attribute defines the bus speed in MHz of the Dell PCI
Device in this chassis, 0 (zero) indicates the speed is unknown.
""")
_PCIDeviceAdapterFault_Type = DellBoolean
_PCIDeviceAdapterFault_Object = MibTableColumn
pCIDeviceAdapterFault = _PCIDeviceAdapterFault_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 80, 1, 11),
    _PCIDeviceAdapterFault_Type()
)
pCIDeviceAdapterFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceAdapterFault.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceAdapterFault.setDescription("""\
1100.0080.0001.0011 This attribute defines if Dell PCI Device in this chassis
has detected a fault or not.
""")
_PCIDeviceConfigurationSpaceTable_Object = MibTable
pCIDeviceConfigurationSpaceTable = _PCIDeviceConfigurationSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82)
)
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceTable.setDescription("""\
1100.0082 This Group defines the Dell PCI Device Configuration Table.
""")
_PCIDeviceConfigurationSpaceTableEntry_Object = MibTableRow
pCIDeviceConfigurationSpaceTableEntry = _PCIDeviceConfigurationSpaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1)
)
pCIDeviceConfigurationSpaceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "pCIDeviceConfigurationSpacechassisIndex"),
    (0, "MIB-Dell-10892", "pCIDeviceConfigurationSpaceIndex"),
)
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceTableEntry.setDescription("""\
1100.0082.0001 This Group defines the Dell PCI Device Configuration Table
Entry.
""")
_PCIDeviceConfigurationSpacechassisIndex_Type = DellObjectRange
_PCIDeviceConfigurationSpacechassisIndex_Object = MibTableColumn
pCIDeviceConfigurationSpacechassisIndex = _PCIDeviceConfigurationSpacechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 1),
    _PCIDeviceConfigurationSpacechassisIndex_Type()
)
pCIDeviceConfigurationSpacechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpacechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpacechassisIndex.setDescription("""\
1100.0082.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PCIDeviceConfigurationSpaceIndex_Type = DellObjectRange
_PCIDeviceConfigurationSpaceIndex_Object = MibTableColumn
pCIDeviceConfigurationSpaceIndex = _PCIDeviceConfigurationSpaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 2),
    _PCIDeviceConfigurationSpaceIndex_Type()
)
pCIDeviceConfigurationSpaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceIndex.setDescription("""\
1100.0082.0001.0002 This attribute defines the index of the Dell PCI Device
Configuration in this chassis.
""")
_PCIDeviceConfigurationSpaceStateCapabilities_Type = DellStateCapabilities
_PCIDeviceConfigurationSpaceStateCapabilities_Object = MibTableColumn
pCIDeviceConfigurationSpaceStateCapabilities = _PCIDeviceConfigurationSpaceStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 3),
    _PCIDeviceConfigurationSpaceStateCapabilities_Type()
)
pCIDeviceConfigurationSpaceStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStateCapabilities.setDescription("""\
1100.0082.0001.0003 This attribute defines the capabilities of the Dell PCI
Device Configuration.
""")
_PCIDeviceConfigurationSpaceStateSettings_Type = DellStateSettings
_PCIDeviceConfigurationSpaceStateSettings_Object = MibTableColumn
pCIDeviceConfigurationSpaceStateSettings = _PCIDeviceConfigurationSpaceStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 4),
    _PCIDeviceConfigurationSpaceStateSettings_Type()
)
pCIDeviceConfigurationSpaceStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStateSettings.setDescription("""\
1100.0082.0001.0004 This attribute defines the state of the Dell PCI Device
Configuration.
""")
_PCIDeviceConfigurationSpaceStatus_Type = DellStatus
_PCIDeviceConfigurationSpaceStatus_Object = MibTableColumn
pCIDeviceConfigurationSpaceStatus = _PCIDeviceConfigurationSpaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 5),
    _PCIDeviceConfigurationSpaceStatus_Type()
)
pCIDeviceConfigurationSpaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceStatus.setDescription("""\
1100.0082.0001.0005 This attribute defines the status of the Dell PCI Device
Configuration.
""")
_PCIDeviceIndexReference_Type = DellObjectRange
_PCIDeviceIndexReference_Object = MibTableColumn
pCIDeviceIndexReference = _PCIDeviceIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 6),
    _PCIDeviceIndexReference_Type()
)
pCIDeviceIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceIndexReference.setDescription("""\
1100.0082.0001.0006 This attribute defines the index number of PCI device that
this configuration applies too.
""")
_PCIDeviceConfigurationSpaceBusNumber_Type = DellUnsigned32BitRange
_PCIDeviceConfigurationSpaceBusNumber_Object = MibTableColumn
pCIDeviceConfigurationSpaceBusNumber = _PCIDeviceConfigurationSpaceBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 7),
    _PCIDeviceConfigurationSpaceBusNumber_Type()
)
pCIDeviceConfigurationSpaceBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceBusNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceBusNumber.setDescription("""\
1100.0082.0001.0007 This attribute defines the bus number of the Dell PCI
Device Configuration in this chassis.
""")
_PCIDeviceConfigurationSpaceDeviceNumber_Type = DellUnsigned32BitRange
_PCIDeviceConfigurationSpaceDeviceNumber_Object = MibTableColumn
pCIDeviceConfigurationSpaceDeviceNumber = _PCIDeviceConfigurationSpaceDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 8),
    _PCIDeviceConfigurationSpaceDeviceNumber_Type()
)
pCIDeviceConfigurationSpaceDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceDeviceNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceDeviceNumber.setDescription("""\
1100.0082.0001.0008 This attribute defines the device number of the Dell PCI
Device in this chassis.
""")
_PCIDeviceConfigurationSpaceFunctionNumber_Type = DellUnsigned32BitRange
_PCIDeviceConfigurationSpaceFunctionNumber_Object = MibTableColumn
pCIDeviceConfigurationSpaceFunctionNumber = _PCIDeviceConfigurationSpaceFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 9),
    _PCIDeviceConfigurationSpaceFunctionNumber_Type()
)
pCIDeviceConfigurationSpaceFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceFunctionNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceFunctionNumber.setDescription("""\
1100.0082.0001.0009 This attribute defines the function number of the Dell PCI
Device in this chassis.
""")


class _PCIDeviceConfigurationSpaceHeader_Type(OctetString):
    """Custom type pCIDeviceConfigurationSpaceHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1025),
    )


_PCIDeviceConfigurationSpaceHeader_Type.__name__ = "OctetString"
_PCIDeviceConfigurationSpaceHeader_Object = MibTableColumn
pCIDeviceConfigurationSpaceHeader = _PCIDeviceConfigurationSpaceHeader_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1100, 82, 1, 10),
    _PCIDeviceConfigurationSpaceHeader_Type()
)
pCIDeviceConfigurationSpaceHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceHeader.setStatus("mandatory")
if mibBuilder.loadTexts:
    pCIDeviceConfigurationSpaceHeader.setDescription("""\
1100.0082.0001.0010 This attribute defines the common configuration space
header of the Dell PCI Device.
""")
_SlotGroup_ObjectIdentity = ObjectIdentity
slotGroup = _SlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200)
)
_SystemSlotTable_Object = MibTable
systemSlotTable = _SystemSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10)
)
if mibBuilder.loadTexts:
    systemSlotTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotTable.setDescription("""\
1200.0010 This Group defines the Dell System Slot Table.
""")
_SystemSlotTableEntry_Object = MibTableRow
systemSlotTableEntry = _SystemSlotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1)
)
systemSlotTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "systemSlotchassisIndex"),
    (0, "MIB-Dell-10892", "systemSlotIndex"),
)
if mibBuilder.loadTexts:
    systemSlotTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotTableEntry.setDescription("""\
1200.0010.0001 This Group defines the Dell System Slot Table Entry.
""")
_SystemSlotchassisIndex_Type = DellObjectRange
_SystemSlotchassisIndex_Object = MibTableColumn
systemSlotchassisIndex = _SystemSlotchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 1),
    _SystemSlotchassisIndex_Type()
)
systemSlotchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotchassisIndex.setDescription("""\
1200.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SystemSlotIndex_Type = DellObjectRange
_SystemSlotIndex_Object = MibTableColumn
systemSlotIndex = _SystemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 2),
    _SystemSlotIndex_Type()
)
systemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotIndex.setDescription("""\
1200.0010.0001.0002 This attribute defines the index of the Dell System Slot in
this chassis.
""")
_SystemSlotStateCapabilitiesUnique_Type = DellSystemSlotStateCapabilities
_SystemSlotStateCapabilitiesUnique_Object = MibTableColumn
systemSlotStateCapabilitiesUnique = _SystemSlotStateCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 3),
    _SystemSlotStateCapabilitiesUnique_Type()
)
systemSlotStateCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStateCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotStateCapabilitiesUnique.setDescription("""\
1200.0010.0001.0003 This attribute defines the capabilities of the Dell System
Slot.
""")
_SystemSlotStateSettingsUnique_Type = DellSystemSlotStateSettings
_SystemSlotStateSettingsUnique_Object = MibTableColumn
systemSlotStateSettingsUnique = _SystemSlotStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 4),
    _SystemSlotStateSettingsUnique_Type()
)
systemSlotStateSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSlotStateSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotStateSettingsUnique.setDescription("""\
1200.0010.0001.0004 This attribute defines the state of the Dell System Slot.
""")
_SystemSlotStatus_Type = DellStatus
_SystemSlotStatus_Object = MibTableColumn
systemSlotStatus = _SystemSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 5),
    _SystemSlotStatus_Type()
)
systemSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotStatus.setDescription("""\
1200.0010.0001.0005 This attribute defines the status of the Dell System Slot.
""")
_SystemSlotCurrentUsage_Type = DellSystemSlotUsage
_SystemSlotCurrentUsage_Object = MibTableColumn
systemSlotCurrentUsage = _SystemSlotCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 6),
    _SystemSlotCurrentUsage_Type()
)
systemSlotCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotCurrentUsage.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotCurrentUsage.setDescription("""\
1200.0010.0001.0006 This attribute defines the current usage of the Dell System
Slot.
""")
_SystemSlotType_Type = DellSystemSlotType
_SystemSlotType_Object = MibTableColumn
systemSlotType = _SystemSlotType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 7),
    _SystemSlotType_Type()
)
systemSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotType.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotType.setDescription("""\
1200.0010.0001.0007 This attribute defines the type of the Dell System Slot.
""")
_SystemSlotSlotExternalSlotName_Type = DellString
_SystemSlotSlotExternalSlotName_Object = MibTableColumn
systemSlotSlotExternalSlotName = _SystemSlotSlotExternalSlotName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 8),
    _SystemSlotSlotExternalSlotName_Type()
)
systemSlotSlotExternalSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotSlotExternalSlotName.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotSlotExternalSlotName.setDescription("""\
1200.0010.0001.0008 This attribute defines name of the external connector name
of the Dell System Slot.
""")
_SystemSlotLength_Type = DellSystemSlotLength
_SystemSlotLength_Object = MibTableColumn
systemSlotLength = _SystemSlotLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 9),
    _SystemSlotLength_Type()
)
systemSlotLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotLength.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotLength.setDescription("""\
1200.0010.0001.0009 This attribute defines the length of the Dell System Slot.
""")
_SystemSlotSlotID_Type = DellUnsigned32BitRange
_SystemSlotSlotID_Object = MibTableColumn
systemSlotSlotID = _SystemSlotSlotID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 10),
    _SystemSlotSlotID_Type()
)
systemSlotSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotSlotID.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotSlotID.setDescription("""\
1200.0010.0001.0010 This attribute defines the slot identification number of
the Dell System Slot.
""")
_SystemSlotCategory_Type = DellSystemSlotCategory
_SystemSlotCategory_Object = MibTableColumn
systemSlotCategory = _SystemSlotCategory_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 11),
    _SystemSlotCategory_Type()
)
systemSlotCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotCategory.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotCategory.setDescription("""\
1200.0010.0001.0011 This attribute defines the category of the Dell System
Slot.
""")
_SystemSlotHotPlugBusWidth_Type = DellSystemSlotHotPlugBusWidth
_SystemSlotHotPlugBusWidth_Object = MibTableColumn
systemSlotHotPlugBusWidth = _SystemSlotHotPlugBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 12),
    _SystemSlotHotPlugBusWidth_Type()
)
systemSlotHotPlugBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotHotPlugBusWidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotHotPlugBusWidth.setDescription("""\
1200.0010.0001.0012 This attribute defines the bus width of the Dell Hot Plug
System Slot.
""")
_SystemSlotHotPlugSlotSpeed_Type = DellUnsigned32BitRange
_SystemSlotHotPlugSlotSpeed_Object = MibTableColumn
systemSlotHotPlugSlotSpeed = _SystemSlotHotPlugSlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 13),
    _SystemSlotHotPlugSlotSpeed_Type()
)
systemSlotHotPlugSlotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotHotPlugSlotSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotHotPlugSlotSpeed.setDescription("""\
1200.0010.0001.0013 This attribute defines the slot speed in MHz of the Dell
Hot Plug System Slot. Zero, (0) indicated the slot speed is unknown.
""")
_SystemSlotHotPlugAdapterSpeed_Type = DellUnsigned32BitRange
_SystemSlotHotPlugAdapterSpeed_Object = MibTableColumn
systemSlotHotPlugAdapterSpeed = _SystemSlotHotPlugAdapterSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1200, 10, 1, 14),
    _SystemSlotHotPlugAdapterSpeed_Type()
)
systemSlotHotPlugAdapterSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSlotHotPlugAdapterSpeed.setStatus("mandatory")
if mibBuilder.loadTexts:
    systemSlotHotPlugAdapterSpeed.setDescription("""\
1200.0010.0001.0014 This attribute defines the adapter speed in MHz of the Dell
Hot Plug System Slot. Zero, (0) indicated the slot speed is unknown.
""")
_MemoryGroup_ObjectIdentity = ObjectIdentity
memoryGroup = _MemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300)
)
_PhysicalMemoryArrayTable_Object = MibTable
physicalMemoryArrayTable = _PhysicalMemoryArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10)
)
if mibBuilder.loadTexts:
    physicalMemoryArrayTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayTable.setDescription("""\
1300.0010 This Group defines the Dell Physical Memory Array Table.
""")
_PhysicalMemoryArrayTableEntry_Object = MibTableRow
physicalMemoryArrayTableEntry = _PhysicalMemoryArrayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1)
)
physicalMemoryArrayTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryArraychassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryArrayIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryArrayTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayTableEntry.setDescription("""\
1300.0010.0001 This Group defines the Dell Physical Memory Array Table Entry.
""")
_PhysicalMemoryArraychassisIndex_Type = DellObjectRange
_PhysicalMemoryArraychassisIndex_Object = MibTableColumn
physicalMemoryArraychassisIndex = _PhysicalMemoryArraychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 1),
    _PhysicalMemoryArraychassisIndex_Type()
)
physicalMemoryArraychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArraychassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArraychassisIndex.setDescription("""\
1300.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PhysicalMemoryArrayIndex_Type = DellObjectRange
_PhysicalMemoryArrayIndex_Object = MibTableColumn
physicalMemoryArrayIndex = _PhysicalMemoryArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 2),
    _PhysicalMemoryArrayIndex_Type()
)
physicalMemoryArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayIndex.setDescription("""\
1300.0010.0001.0002 This attribute defines the index of the Dell Physical
Memory Array in this chassis.
""")
_PhysicalMemoryArrayStateCapabilities_Type = DellStateCapabilities
_PhysicalMemoryArrayStateCapabilities_Object = MibTableColumn
physicalMemoryArrayStateCapabilities = _PhysicalMemoryArrayStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 3),
    _PhysicalMemoryArrayStateCapabilities_Type()
)
physicalMemoryArrayStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayStateCapabilities.setDescription("""\
1300.0010.0001.0003 This attribute defines the capabilities of the Dell
Physical Memory Array.
""")
_PhysicalMemoryArrayStateSettings_Type = DellStateSettings
_PhysicalMemoryArrayStateSettings_Object = MibTableColumn
physicalMemoryArrayStateSettings = _PhysicalMemoryArrayStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 4),
    _PhysicalMemoryArrayStateSettings_Type()
)
physicalMemoryArrayStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalMemoryArrayStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayStateSettings.setDescription("""\
1300.0010.0001.0004 This attribute defines the state of the Dell Physical
Memory Array.
""")
_PhysicalMemoryArrayStatus_Type = DellStatus
_PhysicalMemoryArrayStatus_Object = MibTableColumn
physicalMemoryArrayStatus = _PhysicalMemoryArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 5),
    _PhysicalMemoryArrayStatus_Type()
)
physicalMemoryArrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayStatus.setDescription("""\
1300.0010.0001.0005 This attribute defines the status of the Dell Physical
Memory Array.
""")
_PhysicalMemoryArrayUse_Type = DellPhysicalMemoryArrayUse
_PhysicalMemoryArrayUse_Object = MibTableColumn
physicalMemoryArrayUse = _PhysicalMemoryArrayUse_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 6),
    _PhysicalMemoryArrayUse_Type()
)
physicalMemoryArrayUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayUse.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayUse.setDescription("""\
1300.0010.0001.0006 This attribute defines the use of the Dell Physical Memory
Array.
""")
_PhysicalMemoryArrayECCType_Type = DellPhysicalMemoryArrayECCType
_PhysicalMemoryArrayECCType_Object = MibTableColumn
physicalMemoryArrayECCType = _PhysicalMemoryArrayECCType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 7),
    _PhysicalMemoryArrayECCType_Type()
)
physicalMemoryArrayECCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCType.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCType.setDescription("""\
1300.0010.0001.0007 This attribute defines the error correction type used by
the Dell Physical Memory Array.
""")
_PhysicalMemoryArrayLocation_Type = DellPhysicalMemoryArrayLocation
_PhysicalMemoryArrayLocation_Object = MibTableColumn
physicalMemoryArrayLocation = _PhysicalMemoryArrayLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 8),
    _PhysicalMemoryArrayLocation_Type()
)
physicalMemoryArrayLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayLocation.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayLocation.setDescription("""\
1300.0010.0001.0008 This attribute defines the location of the Dell Physical
Memory Array.
""")
_PhysicalMemoryArrayMaximumSize_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayMaximumSize_Object = MibTableColumn
physicalMemoryArrayMaximumSize = _PhysicalMemoryArrayMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 9),
    _PhysicalMemoryArrayMaximumSize_Type()
)
physicalMemoryArrayMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMaximumSize.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMaximumSize.setDescription("""\
1300.0010.0001.0009 This attribute defines the size in KBytes of the Dell
Physical Memory Array. 0 (zero) inicates no memory installed, 2,147,483,647
indicates an unknown memory size.
""")
_PhysicalMemoryArrayTotalNumberSockets_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayTotalNumberSockets_Object = MibTableColumn
physicalMemoryArrayTotalNumberSockets = _PhysicalMemoryArrayTotalNumberSockets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 10),
    _PhysicalMemoryArrayTotalNumberSockets_Type()
)
physicalMemoryArrayTotalNumberSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayTotalNumberSockets.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayTotalNumberSockets.setDescription("""\
1300.0010.0001.0010 This attribute defines the total number of memory sockets
available for the Dell Physical Memory Array. 2,147,483,647 indicates an
unknown number of sockets.
""")
_PhysicalMemoryArrayInUseNumberSockets_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayInUseNumberSockets_Object = MibTableColumn
physicalMemoryArrayInUseNumberSockets = _PhysicalMemoryArrayInUseNumberSockets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 11),
    _PhysicalMemoryArrayInUseNumberSockets_Type()
)
physicalMemoryArrayInUseNumberSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayInUseNumberSockets.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayInUseNumberSockets.setDescription("""\
1300.0010.0001.0011 This attribute defines the total number of memory sockets
in use by the Dell Physical Memory Array. 2,147,483,647 indicates an unknown
number of sockets.
""")
_PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Type = DellSigned32BitRange
_PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Object = MibTableColumn
physicalMemoryArrayECCErrorNonRecoverableThreshold = _PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 12),
    _PhysicalMemoryArrayECCErrorNonRecoverableThreshold_Type()
)
physicalMemoryArrayECCErrorNonRecoverableThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorNonRecoverableThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorNonRecoverableThreshold.setDescription("""\
1300.0010.0001.0012 This attribute defines the value of the Dell physical
memory array ECC error nonrecoverable threshold. The value is an integer
representing the the number of errors detected.
""")
_PhysicalMemoryArrayECCErrorCriticalThreshold_Type = DellSigned32BitRange
_PhysicalMemoryArrayECCErrorCriticalThreshold_Object = MibTableColumn
physicalMemoryArrayECCErrorCriticalThreshold = _PhysicalMemoryArrayECCErrorCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 13),
    _PhysicalMemoryArrayECCErrorCriticalThreshold_Type()
)
physicalMemoryArrayECCErrorCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorCriticalThreshold.setDescription("""\
1300.0010.0001.00013 This attribute defines the value of the Dell physical
memory array ECC error critical threshold. The value is an integer representing
the the number of errors detected.
""")
_PhysicalMemoryArrayECCErrorNonCriticalThreshold_Type = DellSigned32BitRange
_PhysicalMemoryArrayECCErrorNonCriticalThreshold_Object = MibTableColumn
physicalMemoryArrayECCErrorNonCriticalThreshold = _PhysicalMemoryArrayECCErrorNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 10, 1, 14),
    _PhysicalMemoryArrayECCErrorNonCriticalThreshold_Type()
)
physicalMemoryArrayECCErrorNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorNonCriticalThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayECCErrorNonCriticalThreshold.setDescription("""\
1300.0010.0001.00014 This attribute defines the value of the Dell physical
memory array ECC error noncritical threshold. The value is an integer
representing the the number of errors detected.
""")
_PhysicalMemoryArrayMappedTable_Object = MibTable
physicalMemoryArrayMappedTable = _PhysicalMemoryArrayMappedTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20)
)
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedTable.setDescription("""\
1300.0020 This Group defines the Dell Physical Memory Array Mapped Table. It
references the Physical Memory Array Index.
""")
_PhysicalMemoryArrayMappedTableEntry_Object = MibTableRow
physicalMemoryArrayMappedTableEntry = _PhysicalMemoryArrayMappedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1)
)
physicalMemoryArrayMappedTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "physicalMemoryArrayMappedchassisIndex"),
    (0, "MIB-Dell-10892", "physicalMemoryArrayMappedIndex"),
)
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedTableEntry.setDescription("""\
1300.0020.0001 This Group defines the Dell Physical Memory Array Mapped Table
Entry.
""")
_PhysicalMemoryArrayMappedchassisIndex_Type = DellObjectRange
_PhysicalMemoryArrayMappedchassisIndex_Object = MibTableColumn
physicalMemoryArrayMappedchassisIndex = _PhysicalMemoryArrayMappedchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 1),
    _PhysicalMemoryArrayMappedchassisIndex_Type()
)
physicalMemoryArrayMappedchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedchassisIndex.setDescription("""\
1300.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_PhysicalMemoryArrayMappedIndex_Type = DellObjectRange
_PhysicalMemoryArrayMappedIndex_Object = MibTableColumn
physicalMemoryArrayMappedIndex = _PhysicalMemoryArrayMappedIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 2),
    _PhysicalMemoryArrayMappedIndex_Type()
)
physicalMemoryArrayMappedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedIndex.setDescription("""\
1300.0020.0001.0002 This attribute defines the index of the Dell Memory Array
Mapped Address in this chassis.
""")
_PhysicalMemoryArrayMappedStateCapabilities_Type = DellStateCapabilities
_PhysicalMemoryArrayMappedStateCapabilities_Object = MibTableColumn
physicalMemoryArrayMappedStateCapabilities = _PhysicalMemoryArrayMappedStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 3),
    _PhysicalMemoryArrayMappedStateCapabilities_Type()
)
physicalMemoryArrayMappedStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStateCapabilities.setDescription("""\
1300.0020.0001.0003 This attribute defines the capabilities of the Dell Memory
Array Mapped Address.
""")
_PhysicalMemoryArrayMappedStateSettings_Type = DellStateSettings
_PhysicalMemoryArrayMappedStateSettings_Object = MibTableColumn
physicalMemoryArrayMappedStateSettings = _PhysicalMemoryArrayMappedStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 4),
    _PhysicalMemoryArrayMappedStateSettings_Type()
)
physicalMemoryArrayMappedStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStateSettings.setDescription("""\
1300.0020.0001.0004 This attribute defines the state of the Dell Memory Array
Mapped Address.
""")
_PhysicalMemoryArrayMappedStatus_Type = DellStatus
_PhysicalMemoryArrayMappedStatus_Object = MibTableColumn
physicalMemoryArrayMappedStatus = _PhysicalMemoryArrayMappedStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 5),
    _PhysicalMemoryArrayMappedStatus_Type()
)
physicalMemoryArrayMappedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStatus.setDescription("""\
1300.0020.0001.0005 This attribute defines the status of the Dell Memory Array
Mapped Address.
""")
_PhysicalMemoryArrayIndexReference_Type = DellObjectRange
_PhysicalMemoryArrayIndexReference_Object = MibTableColumn
physicalMemoryArrayIndexReference = _PhysicalMemoryArrayIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 6),
    _PhysicalMemoryArrayIndexReference_Type()
)
physicalMemoryArrayIndexReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayIndexReference.setDescription("""\
1300.0020.0001.0006 This attribute defines the index to the associated Dell
Physical Memory Array in this chassis.
""")
_PhysicalMemoryArrayMappedStartingAddress_Type = DellUnsigned64BitRange
_PhysicalMemoryArrayMappedStartingAddress_Object = MibTableColumn
physicalMemoryArrayMappedStartingAddress = _PhysicalMemoryArrayMappedStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 7),
    _PhysicalMemoryArrayMappedStartingAddress_Type()
)
physicalMemoryArrayMappedStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStartingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedStartingAddress.setDescription("""\
1300.0020.0001.0007 This attribute defines the physical starting address in
KBytes of the Dell Memory Array Mapped Address.
""")
_PhysicalMemoryArrayMappedEndingAddress_Type = DellUnsigned64BitRange
_PhysicalMemoryArrayMappedEndingAddress_Object = MibTableColumn
physicalMemoryArrayMappedEndingAddress = _PhysicalMemoryArrayMappedEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 8),
    _PhysicalMemoryArrayMappedEndingAddress_Type()
)
physicalMemoryArrayMappedEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedEndingAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedEndingAddress.setDescription("""\
1300.0020.0001.0008 This attribute defines the physical ending address in
KBytes of the Dell Memory Array Mapped Address.
""")
_PhysicalMemoryArrayMappedPartitionWidth_Type = DellUnsigned32BitRange
_PhysicalMemoryArrayMappedPartitionWidth_Object = MibTableColumn
physicalMemoryArrayMappedPartitionWidth = _PhysicalMemoryArrayMappedPartitionWidth_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1300, 20, 1, 9),
    _PhysicalMemoryArrayMappedPartitionWidth_Type()
)
physicalMemoryArrayMappedPartitionWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedPartitionWidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    physicalMemoryArrayMappedPartitionWidth.setDescription("""\
1300.0020.0001.0009 This attribute defines the number of memory devices that
form a single row in the Dell Memory Array Mapped Address. 2,147,483,647
indicates an unknown number of memory devices.
""")
_BiosSetUpControlGroup_ObjectIdentity = ObjectIdentity
biosSetUpControlGroup = _BiosSetUpControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400)
)
_BiosSetUpControlTable_Object = MibTable
biosSetUpControlTable = _BiosSetUpControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10)
)
if mibBuilder.loadTexts:
    biosSetUpControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    biosSetUpControlTable.setDescription("""\
1400.0010 This Group defines the set of single devices in a Dell chassis
controlled by BIOS.
""")
_BiosSetUpControlTableEntry_Object = MibTableRow
biosSetUpControlTableEntry = _BiosSetUpControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1)
)
biosSetUpControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "biosSetUpControlchassisIndex"),
)
if mibBuilder.loadTexts:
    biosSetUpControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    biosSetUpControlTableEntry.setDescription("""\
1400.0010.0001 This Group defines the Dell BIOS Control Device Table Entry.
""")
_BiosSetUpControlchassisIndex_Type = DellObjectRange
_BiosSetUpControlchassisIndex_Object = MibTableColumn
biosSetUpControlchassisIndex = _BiosSetUpControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 1),
    _BiosSetUpControlchassisIndex_Type()
)
biosSetUpControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosSetUpControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    biosSetUpControlchassisIndex.setDescription("""\
1400.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_BSUCpointingDeviceControlCapabilities_Type = DellStateCapabilities
_BSUCpointingDeviceControlCapabilities_Object = MibTableColumn
bSUCpointingDeviceControlCapabilities = _BSUCpointingDeviceControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 2),
    _BSUCpointingDeviceControlCapabilities_Type()
)
bSUCpointingDeviceControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlCapabilities.setDescription("""\
1400.0010.0001.0002 This attribute defines the capabilities of the Dell
pointing Device.
""")
_BSUCpointingDeviceControlSettings_Type = DellStateSettings
_BSUCpointingDeviceControlSettings_Object = MibTableColumn
bSUCpointingDeviceControlSettings = _BSUCpointingDeviceControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 3),
    _BSUCpointingDeviceControlSettings_Type()
)
bSUCpointingDeviceControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlSettings.setDescription("""\
1400.0010.0001.0003 This attribute defines the state of the Dell pointing
Device.
""")
_BSUCpointingDeviceControlStatus_Type = DellStatus
_BSUCpointingDeviceControlStatus_Object = MibTableColumn
bSUCpointingDeviceControlStatus = _BSUCpointingDeviceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 4),
    _BSUCpointingDeviceControlStatus_Type()
)
bSUCpointingDeviceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlStatus.setDescription("""\
1400.0010.0001.0004 This attribute defines the status of the Dell pointing
Device.
""")
_BSUCpointingDeviceControlName_Type = DellString
_BSUCpointingDeviceControlName_Object = MibTableColumn
bSUCpointingDeviceControlName = _BSUCpointingDeviceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 5),
    _BSUCpointingDeviceControlName_Type()
)
bSUCpointingDeviceControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCpointingDeviceControlName.setDescription("""\
1400.0010.0001.0005 This attribute defines the setup BIOS name of the pointing
device.
""")
_BSUCnumLockControlCapabilities_Type = DellStateCapabilities
_BSUCnumLockControlCapabilities_Object = MibTableColumn
bSUCnumLockControlCapabilities = _BSUCnumLockControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 6),
    _BSUCnumLockControlCapabilities_Type()
)
bSUCnumLockControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnumLockControlCapabilities.setDescription("""\
1400.0010.0001.0006 This attribute defines the capabilities of the Dell Numeric
Lock.
""")
_BSUCnumLockControlSettings_Type = DellStateSettings
_BSUCnumLockControlSettings_Object = MibTableColumn
bSUCnumLockControlSettings = _BSUCnumLockControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 7),
    _BSUCnumLockControlSettings_Type()
)
bSUCnumLockControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCnumLockControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnumLockControlSettings.setDescription("""\
1400.0010.0001.0007 This attribute defines the state of the Dell Numeric Lock.
""")
_BSUCnumLockControlStatus_Type = DellStatus
_BSUCnumLockControlStatus_Object = MibTableColumn
bSUCnumLockControlStatus = _BSUCnumLockControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 8),
    _BSUCnumLockControlStatus_Type()
)
bSUCnumLockControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnumLockControlStatus.setDescription("""\
1400.0010.0001.0008 This attribute defines the status of the Dell Numeric Lock.
""")
_BSUCnumLockControlName_Type = DellString
_BSUCnumLockControlName_Object = MibTableColumn
bSUCnumLockControlName = _BSUCnumLockControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 9),
    _BSUCnumLockControlName_Type()
)
bSUCnumLockControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnumLockControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnumLockControlName.setDescription("""\
1400.0010.0001.0009 This attribute defines the setup BIOS name of the numeric
lock.
""")
_BSUCprocessorSerialNumberControlCapabilities_Type = DellStateCapabilities
_BSUCprocessorSerialNumberControlCapabilities_Object = MibTableColumn
bSUCprocessorSerialNumberControlCapabilities = _BSUCprocessorSerialNumberControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 10),
    _BSUCprocessorSerialNumberControlCapabilities_Type()
)
bSUCprocessorSerialNumberControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlCapabilities.setDescription("""\
1400.0010.0001.0010 This attribute defines the capabilities of the Dell
Processor Serial Number.
""")
_BSUCprocessorSerialNumberControlSettings_Type = DellStateSettings
_BSUCprocessorSerialNumberControlSettings_Object = MibTableColumn
bSUCprocessorSerialNumberControlSettings = _BSUCprocessorSerialNumberControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 11),
    _BSUCprocessorSerialNumberControlSettings_Type()
)
bSUCprocessorSerialNumberControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlSettings.setDescription("""\
1400.0010.0001.0011 This attribute defines the state of the Dell Processor
Serial Number.
""")
_BSUCprocessorSerialNumberControlStatus_Type = DellStatus
_BSUCprocessorSerialNumberControlStatus_Object = MibTableColumn
bSUCprocessorSerialNumberControlStatus = _BSUCprocessorSerialNumberControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 12),
    _BSUCprocessorSerialNumberControlStatus_Type()
)
bSUCprocessorSerialNumberControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlStatus.setDescription("""\
1400.0010.0001.0012 This attribute defines the status of the Dell Processor
Serial Number.
""")
_BSUCprocessorSerialNumberControlName_Type = DellString
_BSUCprocessorSerialNumberControlName_Object = MibTableColumn
bSUCprocessorSerialNumberControlName = _BSUCprocessorSerialNumberControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 13),
    _BSUCprocessorSerialNumberControlName_Type()
)
bSUCprocessorSerialNumberControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCprocessorSerialNumberControlName.setDescription("""\
1400.0010.0001.0013 This attribute defines the setup BIOS name of the Processor
Serial Number.
""")
_BSUCspeakerControlCapabilitiesUnique_Type = DellSpeakerControlCapabilitiesUnique
_BSUCspeakerControlCapabilitiesUnique_Object = MibTableColumn
bSUCspeakerControlCapabilitiesUnique = _BSUCspeakerControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 14),
    _BSUCspeakerControlCapabilitiesUnique_Type()
)
bSUCspeakerControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCspeakerControlCapabilitiesUnique.setDescription("""\
1400.0010.0001.0014 This attribute defines the capabilities of the Dell Speaker
Control.
""")
_BSUCspeakerControlSettingsUnique_Type = DellSpeakerControlSettingsUnique
_BSUCspeakerControlSettingsUnique_Object = MibTableColumn
bSUCspeakerControlSettingsUnique = _BSUCspeakerControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 15),
    _BSUCspeakerControlSettingsUnique_Type()
)
bSUCspeakerControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCspeakerControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCspeakerControlSettingsUnique.setDescription("""\
1400.0010.0001.0015 This attribute defines the state of the Dell Speaker
Control.
""")
_BSUCspeakerControlStatus_Type = DellStatus
_BSUCspeakerControlStatus_Object = MibTableColumn
bSUCspeakerControlStatus = _BSUCspeakerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 16),
    _BSUCspeakerControlStatus_Type()
)
bSUCspeakerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCspeakerControlStatus.setDescription("""\
1400.0010.0001.0016 This attribute defines the status of the Dell Speaker
Control.
""")
_BSUCspeakerControlName_Type = DellString
_BSUCspeakerControlName_Object = MibTableColumn
bSUCspeakerControlName = _BSUCspeakerControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 17),
    _BSUCspeakerControlName_Type()
)
bSUCspeakerControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCspeakerControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCspeakerControlName.setDescription("""\
1400.0010.0001.0017 This attribute defines the setup BIOS name of the Speaker
Control.
""")
_BSUCnIFwakeonLanControlCapabilitiesUnique_Type = DellNIFwakeonLanControlCapabilitiesUnique
_BSUCnIFwakeonLanControlCapabilitiesUnique_Object = MibTableColumn
bSUCnIFwakeonLanControlCapabilitiesUnique = _BSUCnIFwakeonLanControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 18),
    _BSUCnIFwakeonLanControlCapabilitiesUnique_Type()
)
bSUCnIFwakeonLanControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlCapabilitiesUnique.setDescription("""\
1400.0010.0001.0018 This attribute defines the capabilities of the Dell NIF
wake on Lan.
""")
_BSUCnIFwakeonLanControlSettingsUnique_Type = DellNIFwakeonLanControlSettingsUnique
_BSUCnIFwakeonLanControlSettingsUnique_Object = MibTableColumn
bSUCnIFwakeonLanControlSettingsUnique = _BSUCnIFwakeonLanControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 19),
    _BSUCnIFwakeonLanControlSettingsUnique_Type()
)
bSUCnIFwakeonLanControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlSettingsUnique.setDescription("""\
1400.0010.0001.0019 This attribute defines the state of the Dell NIF wake on
Lan.
""")
_BSUCnIFwakeonLanControlStatus_Type = DellStatus
_BSUCnIFwakeonLanControlStatus_Object = MibTableColumn
bSUCnIFwakeonLanControlStatus = _BSUCnIFwakeonLanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 20),
    _BSUCnIFwakeonLanControlStatus_Type()
)
bSUCnIFwakeonLanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlStatus.setDescription("""\
1400.0010.0001.0020 This attribute defines the status of the Dell NIF wake on
Lan.
""")
_BSUCnIFwakeonLanControlName_Type = DellString
_BSUCnIFwakeonLanControlName_Object = MibTableColumn
bSUCnIFwakeonLanControlName = _BSUCnIFwakeonLanControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 21),
    _BSUCnIFwakeonLanControlName_Type()
)
bSUCnIFwakeonLanControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCnIFwakeonLanControlName.setDescription("""\
1400.0010.0001.0021 This attribute defines the setup BIOS name of the NIF wake
on Lan.
""")
_BSUCbootSequenceControlCapabilitiesUnique_Type = DellBootSequenceControlCapabilitiesUnique
_BSUCbootSequenceControlCapabilitiesUnique_Object = MibTableColumn
bSUCbootSequenceControlCapabilitiesUnique = _BSUCbootSequenceControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 22),
    _BSUCbootSequenceControlCapabilitiesUnique_Type()
)
bSUCbootSequenceControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlCapabilitiesUnique.setDescription("""\
1400.0010.0001.0022 This attribute defines the capabilities of the Dell Boot
Sequence.
""")
_BSUCbootSequenceControlSettingsUnique_Type = DellBootSequenceControlSettingsUnique
_BSUCbootSequenceControlSettingsUnique_Object = MibTableColumn
bSUCbootSequenceControlSettingsUnique = _BSUCbootSequenceControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 23),
    _BSUCbootSequenceControlSettingsUnique_Type()
)
bSUCbootSequenceControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlSettingsUnique.setDescription("""\
1400.0010.0001.0023 This attribute defines the state of the Dell Boot Sequence.
""")
_BSUCbootSequenceControlStatus_Type = DellStatus
_BSUCbootSequenceControlStatus_Object = MibTableColumn
bSUCbootSequenceControlStatus = _BSUCbootSequenceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 24),
    _BSUCbootSequenceControlStatus_Type()
)
bSUCbootSequenceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlStatus.setDescription("""\
1400.0010.0001.0024 This attribute defines the status of the Dell Boot
Sequence.
""")
_BSUCbootSequenceControlName_Type = DellString
_BSUCbootSequenceControlName_Object = MibTableColumn
bSUCbootSequenceControlName = _BSUCbootSequenceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 25),
    _BSUCbootSequenceControlName_Type()
)
bSUCbootSequenceControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCbootSequenceControlName.setDescription("""\
1400.0010.0001.0025 This attribute defines the setup BIOS name of the Boot
Sequence.
""")
_BSUCadministratorPasswordControlCapabilitiesUnique_Type = DellBIOSPasswordControlCapabilitiesUnique
_BSUCadministratorPasswordControlCapabilitiesUnique_Object = MibTableColumn
bSUCadministratorPasswordControlCapabilitiesUnique = _BSUCadministratorPasswordControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 26),
    _BSUCadministratorPasswordControlCapabilitiesUnique_Type()
)
bSUCadministratorPasswordControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlCapabilitiesUnique.setDescription("""\
1400.0010.0001.0026 This attribute defines the capabilities of the Dell
Administrator Password Control.
""")
_BSUCadministratorPasswordControlSettingsUnique_Type = DellBIOSPasswordControlSettingsUnique
_BSUCadministratorPasswordControlSettingsUnique_Object = MibTableColumn
bSUCadministratorPasswordControlSettingsUnique = _BSUCadministratorPasswordControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 27),
    _BSUCadministratorPasswordControlSettingsUnique_Type()
)
bSUCadministratorPasswordControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlSettingsUnique.setDescription("""\
1400.0010.0001.0027 This attribute defines the state of the Dell Administrator
Password Control.
""")
_BSUCadministratorPasswordControlStatus_Type = DellStatus
_BSUCadministratorPasswordControlStatus_Object = MibTableColumn
bSUCadministratorPasswordControlStatus = _BSUCadministratorPasswordControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 28),
    _BSUCadministratorPasswordControlStatus_Type()
)
bSUCadministratorPasswordControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordControlStatus.setDescription("""\
1400.0010.0001.0028 This attribute defines the status of the Dell Administrator
Password Control.
""")
_BSUCadministratorPasswordPasswordVerifyName_Type = DellString
_BSUCadministratorPasswordPasswordVerifyName_Object = MibTableColumn
bSUCadministratorPasswordPasswordVerifyName = _BSUCadministratorPasswordPasswordVerifyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 29),
    _BSUCadministratorPasswordPasswordVerifyName_Type()
)
bSUCadministratorPasswordPasswordVerifyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordPasswordVerifyName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordPasswordVerifyName.setDescription("""\
1400.0010.0001.0029 This attribute defines the setup BIOS name of the current
Administrator Password.
""")
_BSUCadministratorPasswordNewPasswordName_Type = DellString
_BSUCadministratorPasswordNewPasswordName_Object = MibTableColumn
bSUCadministratorPasswordNewPasswordName = _BSUCadministratorPasswordNewPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 30),
    _BSUCadministratorPasswordNewPasswordName_Type()
)
bSUCadministratorPasswordNewPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordNewPasswordName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCadministratorPasswordNewPasswordName.setDescription("""\
1400.0010.0001.0030 This attribute defines the setup BIOS name of the new
Administrator Password. To set a new Administrator Password, a successful set
of the current Administrator Password must have been done immediately
preceeding this set.
""")
_BSUCuserPasswordControlCapabilitiesUnique_Type = DellBIOSPasswordControlCapabilitiesUnique
_BSUCuserPasswordControlCapabilitiesUnique_Object = MibTableColumn
bSUCuserPasswordControlCapabilitiesUnique = _BSUCuserPasswordControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 31),
    _BSUCuserPasswordControlCapabilitiesUnique_Type()
)
bSUCuserPasswordControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlCapabilitiesUnique.setDescription("""\
1400.0010.0001.0031 This attribute defines the capabilities of the Dell User
Password Control.
""")
_BSUCuserPasswordControlSettingsUnique_Type = DellBIOSPasswordControlSettingsUnique
_BSUCuserPasswordControlSettingsUnique_Object = MibTableColumn
bSUCuserPasswordControlSettingsUnique = _BSUCuserPasswordControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 32),
    _BSUCuserPasswordControlSettingsUnique_Type()
)
bSUCuserPasswordControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlSettingsUnique.setDescription("""\
1400.0010.0001.0032 This attribute defines the state of the Dell User Password
Control.
""")
_BSUCuserPasswordControlStatus_Type = DellStatus
_BSUCuserPasswordControlStatus_Object = MibTableColumn
bSUCuserPasswordControlStatus = _BSUCuserPasswordControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 33),
    _BSUCuserPasswordControlStatus_Type()
)
bSUCuserPasswordControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCuserPasswordControlStatus.setDescription("""\
1400.0010.0001.0033 This attribute defines the status of the Dell User Password
Control.
""")
_BSUCuserPasswordPasswordVerifyName_Type = DellString
_BSUCuserPasswordPasswordVerifyName_Object = MibTableColumn
bSUCuserPasswordPasswordVerifyName = _BSUCuserPasswordPasswordVerifyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 34),
    _BSUCuserPasswordPasswordVerifyName_Type()
)
bSUCuserPasswordPasswordVerifyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCuserPasswordPasswordVerifyName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCuserPasswordPasswordVerifyName.setDescription("""\
1400.0010.0001.0034 This attribute defines the setup BIOS name of the current
User Password.
""")
_BSUCuserPasswordNewPasswordName_Type = DellString
_BSUCuserPasswordNewPasswordName_Object = MibTableColumn
bSUCuserPasswordNewPasswordName = _BSUCuserPasswordNewPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 10, 1, 35),
    _BSUCuserPasswordNewPasswordName_Type()
)
bSUCuserPasswordNewPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bSUCuserPasswordNewPasswordName.setStatus("mandatory")
if mibBuilder.loadTexts:
    bSUCuserPasswordNewPasswordName.setDescription("""\
1400.0010.0001.0035 This attribute defines the setup BIOS name of the new User
Password. To set a new User Password, a successful set of the current User
Password must have been done immediately preceeding this set.
""")
_SCSIControlTable_Object = MibTable
sCSIControlTable = _SCSIControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20)
)
if mibBuilder.loadTexts:
    sCSIControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlTable.setDescription("""\
1400.0020 This Group defines the Dell SCSI Table.
""")
_SCSIControlTableEntry_Object = MibTableRow
sCSIControlTableEntry = _SCSIControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1)
)
sCSIControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "sCSIControlchassisIndex"),
    (0, "MIB-Dell-10892", "sCSIControlIndex"),
)
if mibBuilder.loadTexts:
    sCSIControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlTableEntry.setDescription("""\
1400.0020.0001 This Group defines the Dell SCSI Table Entry.
""")
_SCSIControlchassisIndex_Type = DellObjectRange
_SCSIControlchassisIndex_Object = MibTableColumn
sCSIControlchassisIndex = _SCSIControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 1),
    _SCSIControlchassisIndex_Type()
)
sCSIControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlchassisIndex.setDescription("""\
1400.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SCSIControlIndex_Type = DellObjectRange
_SCSIControlIndex_Object = MibTableColumn
sCSIControlIndex = _SCSIControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 2),
    _SCSIControlIndex_Type()
)
sCSIControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlIndex.setDescription("""\
1400.0020.0001.0002 This attribute defines the index of the Dell SCSI
controller in this chassis.
""")
_SCSIControlCapabilities_Type = DellStateCapabilities
_SCSIControlCapabilities_Object = MibTableColumn
sCSIControlCapabilities = _SCSIControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 3),
    _SCSIControlCapabilities_Type()
)
sCSIControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlCapabilities.setDescription("""\
1400.0020.0001.0003 This attribute defines the capabilities of the Dell SCSI
controller.
""")
_SCSIControlSettings_Type = DellStateSettings
_SCSIControlSettings_Object = MibTableColumn
sCSIControlSettings = _SCSIControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 4),
    _SCSIControlSettings_Type()
)
sCSIControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCSIControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlSettings.setDescription("""\
1400.0020.0001.0004 This attribute defines the state of the Dell SCSI
controller.
""")
_SCSIControlStatus_Type = DellStatus
_SCSIControlStatus_Object = MibTableColumn
sCSIControlStatus = _SCSIControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 5),
    _SCSIControlStatus_Type()
)
sCSIControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlStatus.setDescription("""\
1400.0020.0001.0005 This attribute defines the status of the Dell SCSI
controller.
""")
_SCSIControlName_Type = DellString
_SCSIControlName_Object = MibTableColumn
sCSIControlName = _SCSIControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 20, 1, 6),
    _SCSIControlName_Type()
)
sCSIControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCSIControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    sCSIControlName.setDescription("""\
1400.0020.0001.0006 This attribute defines the setup BIOS name of the Dell SCSI
controller.
""")
_ParallelPortControlTable_Object = MibTable
parallelPortControlTable = _ParallelPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30)
)
if mibBuilder.loadTexts:
    parallelPortControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlTable.setDescription("""\
1400.0030 This Group defines the Dell Parallel Port Table.
""")
_ParallelPortControlTableEntry_Object = MibTableRow
parallelPortControlTableEntry = _ParallelPortControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1)
)
parallelPortControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "parallelPortControlchassisIndex"),
    (0, "MIB-Dell-10892", "parallelPortControlIndex"),
)
if mibBuilder.loadTexts:
    parallelPortControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlTableEntry.setDescription("""\
1400.0030.0001 This Group defines the Dell Parallel Port Table Entry.
""")
_ParallelPortControlchassisIndex_Type = DellObjectRange
_ParallelPortControlchassisIndex_Object = MibTableColumn
parallelPortControlchassisIndex = _ParallelPortControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 1),
    _ParallelPortControlchassisIndex_Type()
)
parallelPortControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlchassisIndex.setDescription("""\
1400.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_ParallelPortControlIndex_Type = DellObjectRange
_ParallelPortControlIndex_Object = MibTableColumn
parallelPortControlIndex = _ParallelPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 2),
    _ParallelPortControlIndex_Type()
)
parallelPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlIndex.setDescription("""\
1400.0030.0001.0002 This attribute defines the index of the Dell Parallel Port
in this chassis.
""")
_ParallelPortControlCapabilitiesUnique_Type = DellParallelPortControlCapabilitiesUnique
_ParallelPortControlCapabilitiesUnique_Object = MibTableColumn
parallelPortControlCapabilitiesUnique = _ParallelPortControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 3),
    _ParallelPortControlCapabilitiesUnique_Type()
)
parallelPortControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlCapabilitiesUnique.setDescription("""\
1400.0030.0001.0003 This attribute defines the capabilities of the Dell
Parallel Port.
""")
_ParallelPortControlSettingsUnique_Type = DellParallelPortControlSettingsUnique
_ParallelPortControlSettingsUnique_Object = MibTableColumn
parallelPortControlSettingsUnique = _ParallelPortControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 4),
    _ParallelPortControlSettingsUnique_Type()
)
parallelPortControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parallelPortControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlSettingsUnique.setDescription("""\
1400.0030.0001.0004 This attribute defines the state of the Dell Parallel Port.
""")
_ParallelPortControlStatus_Type = DellStatus
_ParallelPortControlStatus_Object = MibTableColumn
parallelPortControlStatus = _ParallelPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 5),
    _ParallelPortControlStatus_Type()
)
parallelPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlStatus.setDescription("""\
1400.0030.0001.0005 This attribute defines the status of the Dell Parallel
Port.
""")
_ParallelPortControlName_Type = DellString
_ParallelPortControlName_Object = MibTableColumn
parallelPortControlName = _ParallelPortControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 6),
    _ParallelPortControlName_Type()
)
parallelPortControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlName.setDescription("""\
1400.0030.0001.0006 This attribute defines the setup BIOS name of the Parallel
Port.
""")
_ParallelPortControlModeCapabilitiesUnique_Type = DellParallelPortControlModeCapabilitiesUnique
_ParallelPortControlModeCapabilitiesUnique_Object = MibTableColumn
parallelPortControlModeCapabilitiesUnique = _ParallelPortControlModeCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 7),
    _ParallelPortControlModeCapabilitiesUnique_Type()
)
parallelPortControlModeCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelPortControlModeCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlModeCapabilitiesUnique.setDescription("""\
1400.0030.0001.0007 This attribute defines the mode capabilities of the Dell
Parallel Port.
""")
_ParallelPortControlModeSettingsUnique_Type = DellParallelPortControlModeSettingsUnique
_ParallelPortControlModeSettingsUnique_Object = MibTableColumn
parallelPortControlModeSettingsUnique = _ParallelPortControlModeSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 30, 1, 8),
    _ParallelPortControlModeSettingsUnique_Type()
)
parallelPortControlModeSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parallelPortControlModeSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    parallelPortControlModeSettingsUnique.setDescription("""\
1400.0030.0001.0008 This attribute defines the mode state of the Dell Parallel
Port.
""")
_SerialPortControlTable_Object = MibTable
serialPortControlTable = _SerialPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40)
)
if mibBuilder.loadTexts:
    serialPortControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlTable.setDescription("""\
1400.0040 This Group defines the Dell Serial Port Table.
""")
_SerialPortControlTableEntry_Object = MibTableRow
serialPortControlTableEntry = _SerialPortControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1)
)
serialPortControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "serialPortControlchassisIndex"),
    (0, "MIB-Dell-10892", "serialPortControlIndex"),
)
if mibBuilder.loadTexts:
    serialPortControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlTableEntry.setDescription("""\
1400.0040.0001 This Group defines the Dell Serial Port Table Entry.
""")
_SerialPortControlchassisIndex_Type = DellObjectRange
_SerialPortControlchassisIndex_Object = MibTableColumn
serialPortControlchassisIndex = _SerialPortControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 1),
    _SerialPortControlchassisIndex_Type()
)
serialPortControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlchassisIndex.setDescription("""\
1400.0040.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_SerialPortControlIndex_Type = DellObjectRange
_SerialPortControlIndex_Object = MibTableColumn
serialPortControlIndex = _SerialPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 2),
    _SerialPortControlIndex_Type()
)
serialPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlIndex.setDescription("""\
1400.0040.0001.0002 This attribute defines the index of the Dell Serial Port in
this chassis.
""")
_SerialPortControlCapabilitiesUnique_Type = DellSerialPortControlCapabilitiesUnique
_SerialPortControlCapabilitiesUnique_Object = MibTableColumn
serialPortControlCapabilitiesUnique = _SerialPortControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 3),
    _SerialPortControlCapabilitiesUnique_Type()
)
serialPortControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlCapabilitiesUnique.setDescription("""\
1400.0040.0001.0003 This attribute defines the capabilities of the Dell Serial
Port.
""")
_SerialPortControlSettingsUnique_Type = DellSerialPortControlSettingsUnique
_SerialPortControlSettingsUnique_Object = MibTableColumn
serialPortControlSettingsUnique = _SerialPortControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 4),
    _SerialPortControlSettingsUnique_Type()
)
serialPortControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlSettingsUnique.setDescription("""\
1400.0040.0001.0004 This attribute defines the state of the Dell Serial Port.
""")
_SerialPortControlStatus_Type = DellStatus
_SerialPortControlStatus_Object = MibTableColumn
serialPortControlStatus = _SerialPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 5),
    _SerialPortControlStatus_Type()
)
serialPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlStatus.setDescription("""\
1400.0040.0001.0005 This attribute defines the status of the Dell Serial Port.
""")
_SerialPortControlName_Type = DellString
_SerialPortControlName_Object = MibTableColumn
serialPortControlName = _SerialPortControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 40, 1, 6),
    _SerialPortControlName_Type()
)
serialPortControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialPortControlName.setDescription("""\
1400.0040.0001.0006 This attribute defines the setup BIOS name of the Serial
Port.
""")
_UsbControlTable_Object = MibTable
usbControlTable = _UsbControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50)
)
if mibBuilder.loadTexts:
    usbControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlTable.setDescription("""\
1400.0050 This Group defines the Dell Universal Serial Bus Table.
""")
_UsbControlTableEntry_Object = MibTableRow
usbControlTableEntry = _UsbControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1)
)
usbControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "usbControlchassisIndex"),
    (0, "MIB-Dell-10892", "usbControlIndex"),
)
if mibBuilder.loadTexts:
    usbControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlTableEntry.setDescription("""\
1400.0050.0001 This Group defines the Dell Universal Serial Bus Table Entry.
""")
_UsbControlchassisIndex_Type = DellObjectRange
_UsbControlchassisIndex_Object = MibTableColumn
usbControlchassisIndex = _UsbControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 1),
    _UsbControlchassisIndex_Type()
)
usbControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlchassisIndex.setDescription("""\
1400.0050.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_UsbControlIndex_Type = DellObjectRange
_UsbControlIndex_Object = MibTableColumn
usbControlIndex = _UsbControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 2),
    _UsbControlIndex_Type()
)
usbControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlIndex.setDescription("""\
1400.0050.0001.0002 This attribute defines the index of the Dell Universal
Serial Bus in this chassis.
""")
_UsbControlCapabilities_Type = DellStateCapabilities
_UsbControlCapabilities_Object = MibTableColumn
usbControlCapabilities = _UsbControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 3),
    _UsbControlCapabilities_Type()
)
usbControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlCapabilities.setDescription("""\
1400.0050.0001.0003 This attribute defines the capabilities of the Dell
Universal Serial Bus.
""")
_UsbControlSettings_Type = DellStateSettings
_UsbControlSettings_Object = MibTableColumn
usbControlSettings = _UsbControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 4),
    _UsbControlSettings_Type()
)
usbControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlSettings.setDescription("""\
1400.0050.0001.0004 This attribute defines the state of the Dell Universal
Serial Bus.
""")
_UsbControlStatus_Type = DellStatus
_UsbControlStatus_Object = MibTableColumn
usbControlStatus = _UsbControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 5),
    _UsbControlStatus_Type()
)
usbControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlStatus.setDescription("""\
1400.0050.0001.0005 This attribute defines the status of the Dell Universal
Serial Bus.
""")
_UsbControlName_Type = DellString
_UsbControlName_Object = MibTableColumn
usbControlName = _UsbControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 50, 1, 6),
    _UsbControlName_Type()
)
usbControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    usbControlName.setDescription("""\
1400.0050.0001.0006 This attribute defines the setup BIOS name of the Universal
Serial Bus.
""")
_IdeControlTable_Object = MibTable
ideControlTable = _IdeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60)
)
if mibBuilder.loadTexts:
    ideControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlTable.setDescription("""\
1400.0060 This Group defines the Dell IDE Table.
""")
_IdeControlTableEntry_Object = MibTableRow
ideControlTableEntry = _IdeControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1)
)
ideControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "ideControlchassisIndex"),
    (0, "MIB-Dell-10892", "ideControlIndex"),
)
if mibBuilder.loadTexts:
    ideControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlTableEntry.setDescription("""\
1400.0060.0001 This Group defines the Dell IDE Table Entry.
""")
_IdeControlchassisIndex_Type = DellObjectRange
_IdeControlchassisIndex_Object = MibTableColumn
ideControlchassisIndex = _IdeControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 1),
    _IdeControlchassisIndex_Type()
)
ideControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlchassisIndex.setDescription("""\
1400.0060.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_IdeControlIndex_Type = DellObjectRange
_IdeControlIndex_Object = MibTableColumn
ideControlIndex = _IdeControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 2),
    _IdeControlIndex_Type()
)
ideControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlIndex.setDescription("""\
1400.0060.0001.0002 This attribute defines the index of the Dell IDE controller
in this chassis.
""")
_IdeControlCapabilitiesUnique_Type = DellideControlCapabilitiesUnique
_IdeControlCapabilitiesUnique_Object = MibTableColumn
ideControlCapabilitiesUnique = _IdeControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 3),
    _IdeControlCapabilitiesUnique_Type()
)
ideControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlCapabilitiesUnique.setDescription("""\
1400.0060.0001.0003 This attribute defines the capabilities of the Dell IDE
controller.
""")
_IdeControlSettingsUnique_Type = DellideControlSettingsUnique
_IdeControlSettingsUnique_Object = MibTableColumn
ideControlSettingsUnique = _IdeControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 4),
    _IdeControlSettingsUnique_Type()
)
ideControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ideControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlSettingsUnique.setDescription("""\
1400.0060.0001.0004 This attribute defines the state of the Dell IDE
controller.
""")
_IdeControlStatus_Type = DellStatus
_IdeControlStatus_Object = MibTableColumn
ideControlStatus = _IdeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 5),
    _IdeControlStatus_Type()
)
ideControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlStatus.setDescription("""\
1400.0060.0001.0005 This attribute defines the state of the Dell IDE
controller.
""")
_IdeControlName_Type = DellString
_IdeControlName_Object = MibTableColumn
ideControlName = _IdeControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 60, 1, 6),
    _IdeControlName_Type()
)
ideControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ideControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    ideControlName.setDescription("""\
1400.0060.0001.0006 This attribute defines the setup BIOS name of the IDE
controller.
""")
_DisketteControlTable_Object = MibTable
disketteControlTable = _DisketteControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70)
)
if mibBuilder.loadTexts:
    disketteControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlTable.setDescription("""\
1400.0070 This Group defines the Dell Diskette Control Table.
""")
_DisketteControlTableEntry_Object = MibTableRow
disketteControlTableEntry = _DisketteControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1)
)
disketteControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "disketteControlchassisIndex"),
    (0, "MIB-Dell-10892", "disketteControlIndex"),
)
if mibBuilder.loadTexts:
    disketteControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlTableEntry.setDescription("""\
1400.0070.0001 This Group defines the Dell Diskette Control Table Entry.
""")
_DisketteControlchassisIndex_Type = DellObjectRange
_DisketteControlchassisIndex_Object = MibTableColumn
disketteControlchassisIndex = _DisketteControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 1),
    _DisketteControlchassisIndex_Type()
)
disketteControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlchassisIndex.setDescription("""\
1400.0070.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_DisketteControlIndex_Type = DellObjectRange
_DisketteControlIndex_Object = MibTableColumn
disketteControlIndex = _DisketteControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 2),
    _DisketteControlIndex_Type()
)
disketteControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlIndex.setDescription("""\
1400.0070.0001.0002 This attribute defines the index of Dell diskette
controllers in this chassis.
""")
_DisketteControlCapabilitiesUnique_Type = DellDisketteControlCapabilitiesUnique
_DisketteControlCapabilitiesUnique_Object = MibTableColumn
disketteControlCapabilitiesUnique = _DisketteControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 3),
    _DisketteControlCapabilitiesUnique_Type()
)
disketteControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlCapabilitiesUnique.setDescription("""\
1400.0070.0001.0003 This attribute defines the capabilities of the Dell
diskette controller.
""")
_DisketteControlSettingsUnique_Type = DellDisketteControlSettingsUnique
_DisketteControlSettingsUnique_Object = MibTableColumn
disketteControlSettingsUnique = _DisketteControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 4),
    _DisketteControlSettingsUnique_Type()
)
disketteControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disketteControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlSettingsUnique.setDescription("""\
1400.0070.0001.0004 This attribute defines the settings of the Dell diskette
controller.
""")
_DisketteControlStatus_Type = DellStatus
_DisketteControlStatus_Object = MibTableColumn
disketteControlStatus = _DisketteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 5),
    _DisketteControlStatus_Type()
)
disketteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlStatus.setDescription("""\
1400.0070.0001.0005 This attribute defines the status of the Dell diskette
controller.
""")
_DisketteControlName_Type = DellString
_DisketteControlName_Object = MibTableColumn
disketteControlName = _DisketteControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 70, 1, 6),
    _DisketteControlName_Type()
)
disketteControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disketteControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    disketteControlName.setDescription("""\
1400.0070.0001.0006 This attribute defines the setup BIOS name of the diskette
controller.
""")
_NetworkInterfaceControlTable_Object = MibTable
networkInterfaceControlTable = _NetworkInterfaceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80)
)
if mibBuilder.loadTexts:
    networkInterfaceControlTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlTable.setDescription("""\
1400.0080 This Group defines the Dell Network Interface Table.
""")
_NetworkInterfaceControlTableEntry_Object = MibTableRow
networkInterfaceControlTableEntry = _NetworkInterfaceControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1)
)
networkInterfaceControlTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "networkInterfaceControlchassisIndex"),
    (0, "MIB-Dell-10892", "networkInterfaceControlIndex"),
)
if mibBuilder.loadTexts:
    networkInterfaceControlTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlTableEntry.setDescription("""\
1400.0080.0001 This Group defines the Dell Network Interface Table Entry.
""")
_NetworkInterfaceControlchassisIndex_Type = DellObjectRange
_NetworkInterfaceControlchassisIndex_Object = MibTableColumn
networkInterfaceControlchassisIndex = _NetworkInterfaceControlchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 1),
    _NetworkInterfaceControlchassisIndex_Type()
)
networkInterfaceControlchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlchassisIndex.setDescription("""\
1400.0080.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_NetworkInterfaceControlIndex_Type = DellObjectRange
_NetworkInterfaceControlIndex_Object = MibTableColumn
networkInterfaceControlIndex = _NetworkInterfaceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 2),
    _NetworkInterfaceControlIndex_Type()
)
networkInterfaceControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlIndex.setDescription("""\
1400.0080.0001.0002 This attribute defines the index of Dell network interfaces
in this chassis.
""")
_NetworkInterfaceControlCapabilitiesUnique_Type = DellNetworkInterfaceControlCapabilitiesUnique
_NetworkInterfaceControlCapabilitiesUnique_Object = MibTableColumn
networkInterfaceControlCapabilitiesUnique = _NetworkInterfaceControlCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 3),
    _NetworkInterfaceControlCapabilitiesUnique_Type()
)
networkInterfaceControlCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlCapabilitiesUnique.setDescription("""\
1400.0080.0001.0003 This attribute defines the capabilities of the Dell network
interface.
""")
_NetworkInterfaceControlSettingsUnique_Type = DellNetworkInterfaceControlSettingsUnique
_NetworkInterfaceControlSettingsUnique_Object = MibTableColumn
networkInterfaceControlSettingsUnique = _NetworkInterfaceControlSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 4),
    _NetworkInterfaceControlSettingsUnique_Type()
)
networkInterfaceControlSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkInterfaceControlSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlSettingsUnique.setDescription("""\
1400.0080.0001.0004 This attribute defines the state of the Dell network
interface.
""")
_NetworkInterfaceControlStatus_Type = DellStatus
_NetworkInterfaceControlStatus_Object = MibTableColumn
networkInterfaceControlStatus = _NetworkInterfaceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 5),
    _NetworkInterfaceControlStatus_Type()
)
networkInterfaceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceControlStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlStatus.setDescription("""\
1400.0080.0001.0005 This attribute defines the status of the Dell network
interface.
""")
_NetworkInterfaceControlName_Type = DellString
_NetworkInterfaceControlName_Object = MibTableColumn
networkInterfaceControlName = _NetworkInterfaceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1400, 80, 1, 6),
    _NetworkInterfaceControlName_Type()
)
networkInterfaceControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkInterfaceControlName.setStatus("mandatory")
if mibBuilder.loadTexts:
    networkInterfaceControlName.setDescription("""\
1400.0080.0001.0006 This attribute defines the setup BIOS name of the network
interface.
""")
_LraGroup_ObjectIdentity = ObjectIdentity
lraGroup = _LraGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500)
)
_LRAGlobalSettingsTable_Object = MibTable
lRAGlobalSettingsTable = _LRAGlobalSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10)
)
if mibBuilder.loadTexts:
    lRAGlobalSettingsTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalSettingsTable.setDescription("""\
1500.0010 This Group defines the Dell Global Settings Local Response Agent
Table.
""")
_LRAGlobalSettingsTableEntry_Object = MibTableRow
lRAGlobalSettingsTableEntry = _LRAGlobalSettingsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1)
)
lRAGlobalSettingsTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "lRAGlobalchassisIndex"),
)
if mibBuilder.loadTexts:
    lRAGlobalSettingsTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalSettingsTableEntry.setDescription("""\
1500.0010.0001 This Group defines the Dell Global Settings Local Response Agent
Table Entry.
""")
_LRAGlobalchassisIndex_Type = DellObjectRange
_LRAGlobalchassisIndex_Object = MibTableColumn
lRAGlobalchassisIndex = _LRAGlobalchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 1),
    _LRAGlobalchassisIndex_Type()
)
lRAGlobalchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalchassisIndex.setDescription("""\
1500.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_LRAGlobalState_Type = DellStateSettings
_LRAGlobalState_Object = MibTableColumn
lRAGlobalState = _LRAGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 2),
    _LRAGlobalState_Type()
)
lRAGlobalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalState.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalState.setDescription("""\
1500.0010.0001.0002 This attribute defines the state of the Dell Global
Settings Local Response Agent.
""")
_LRAGlobalSettingsDisableTimeoutValue_Type = DellUnsigned32BitRange
_LRAGlobalSettingsDisableTimeoutValue_Object = MibTableColumn
lRAGlobalSettingsDisableTimeoutValue = _LRAGlobalSettingsDisableTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 3),
    _LRAGlobalSettingsDisableTimeoutValue_Type()
)
lRAGlobalSettingsDisableTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalSettingsDisableTimeoutValue.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalSettingsDisableTimeoutValue.setDescription("""\
1500.0010.0001.0003 This attribute defines the timeout duration in seconds the
that Dell Global Settings Local Response Agent will be disabled after a machine
shutdown and reboot.
""")
_LRAGlobalSettingsCapabilitiesUnique_Type = DellLocalResponseAgentCapabilitiesUnique
_LRAGlobalSettingsCapabilitiesUnique_Object = MibTableColumn
lRAGlobalSettingsCapabilitiesUnique = _LRAGlobalSettingsCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 4),
    _LRAGlobalSettingsCapabilitiesUnique_Type()
)
lRAGlobalSettingsCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalSettingsCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalSettingsCapabilitiesUnique.setDescription("""\
1500.0010.0001.0004 This attribute defines the set of Global Capabilities that
all Local Response Agents may or may not allow to be set or reset.
""")
_LRAGlobalThermalShutdownCapabilitiesUnique_Type = DellLRAThermalShutdownCapabilitiesUnique
_LRAGlobalThermalShutdownCapabilitiesUnique_Object = MibTableColumn
lRAGlobalThermalShutdownCapabilitiesUnique = _LRAGlobalThermalShutdownCapabilitiesUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 5),
    _LRAGlobalThermalShutdownCapabilitiesUnique_Type()
)
lRAGlobalThermalShutdownCapabilitiesUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAGlobalThermalShutdownCapabilitiesUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalThermalShutdownCapabilitiesUnique.setDescription("""\
1500.0010.0001.0005 This attribute defines the set of Thermal Shutdown
Capabilities that the Local Response Agent supports.
""")
_LRAGlobalThermalShutdownStateSettingsUnique_Type = DellLRAThermalShutdownStateSettingsUnique
_LRAGlobalThermalShutdownStateSettingsUnique_Object = MibTableColumn
lRAGlobalThermalShutdownStateSettingsUnique = _LRAGlobalThermalShutdownStateSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 10, 1, 6),
    _LRAGlobalThermalShutdownStateSettingsUnique_Type()
)
lRAGlobalThermalShutdownStateSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lRAGlobalThermalShutdownStateSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAGlobalThermalShutdownStateSettingsUnique.setDescription("""\
1500.0010.0001.0006 This attribute defines the Thermal Shutdown state that the
Local Response Agent supports.
""")
_LRAActionTableTable_Object = MibTable
lRAActionTableTable = _LRAActionTableTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20)
)
if mibBuilder.loadTexts:
    lRAActionTableTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAActionTableTable.setDescription("""\
1500.0020 This Group defines the Dell Local Response Agent Action Table.
""")
_LRAActionTableTableEntry_Object = MibTableRow
lRAActionTableTableEntry = _LRAActionTableTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1)
)
lRAActionTableTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "lRAActionTablechassisIndex"),
    (0, "MIB-Dell-10892", "lRAActionTableActionNumberIndex"),
)
if mibBuilder.loadTexts:
    lRAActionTableTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAActionTableTableEntry.setDescription("""\
1500.0020.0001 This Group defines the Dell Local Response Agent Table Entry.
""")
_LRAActionTablechassisIndex_Type = DellObjectRange
_LRAActionTablechassisIndex_Object = MibTableColumn
lRAActionTablechassisIndex = _LRAActionTablechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 1),
    _LRAActionTablechassisIndex_Type()
)
lRAActionTablechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAActionTablechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAActionTablechassisIndex.setDescription("""\
1500.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_LRAActionTableActionNumberIndex_Type = DellUnsigned16BitRange
_LRAActionTableActionNumberIndex_Object = MibTableColumn
lRAActionTableActionNumberIndex = _LRAActionTableActionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 2),
    _LRAActionTableActionNumberIndex_Type()
)
lRAActionTableActionNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRAActionTableActionNumberIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAActionTableActionNumberIndex.setDescription("""\
1500.0020.0001.0002 This attribute defines the action number index of the Dell
Local Response Agent. These currently supported values are: 160 temperature
failure action definition 168 cooling device failure action definition 172
voltage failure action definition 200 temperature warning action definition 202
voltage warning action definition 204 cooling device warning action definition
206 amperage failure action definition 208 amperage warning action definition
210 a power or cooling unit redundancy lost action definition 212 a power or
cooling unit redundancy degraded action definition 214 power supply failed
action definition 220 chassis intrusion action definition 228 memory device
warning action definition 474 memory device failure action definition
""")


class _LRAActionTableUserApplicationName_Type(DisplayString):
    """Custom type lRAActionTableUserApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LRAActionTableUserApplicationName_Type.__name__ = "DisplayString"
_LRAActionTableUserApplicationName_Object = MibTableColumn
lRAActionTableUserApplicationName = _LRAActionTableUserApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 3),
    _LRAActionTableUserApplicationName_Type()
)
lRAActionTableUserApplicationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lRAActionTableUserApplicationName.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAActionTableUserApplicationName.setDescription("""\
1500.0020.0001.0003 This is the name of the user application executable path
and file name to execute by the Dell Local Response Agent if the value execute
application was set.
""")
_LRAActionTableSettingsUnique_Type = DellLocalResponseAgentSettingsUnique
_LRAActionTableSettingsUnique_Object = MibTableColumn
lRAActionTableSettingsUnique = _LRAActionTableSettingsUnique_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1500, 20, 1, 4),
    _LRAActionTableSettingsUnique_Type()
)
lRAActionTableSettingsUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lRAActionTableSettingsUnique.setStatus("mandatory")
if mibBuilder.loadTexts:
    lRAActionTableSettingsUnique.setDescription("""\
1500.0020.0001.0004 This attribute defines the capabilities of the Dell Local
Response Agent.
""")
_CooGroup_ObjectIdentity = ObjectIdentity
cooGroup = _CooGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600)
)
_CooTable_Object = MibTable
cooTable = _CooTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10)
)
if mibBuilder.loadTexts:
    cooTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTable.setDescription("""\
1600.0010 This Group defines the Dell Cost of Ownership: Table.
""")
_CooTableEntry_Object = MibTableRow
cooTableEntry = _CooTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1)
)
cooTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "coochassisIndex"),
)
if mibBuilder.loadTexts:
    cooTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTableEntry.setDescription("""\
1600.0010.0001 This Group defines the Dell Cost of Ownership: Table Entry.
""")
_CoochassisIndex_Type = DellObjectRange
_CoochassisIndex_Object = MibTableColumn
coochassisIndex = _CoochassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 1),
    _CoochassisIndex_Type()
)
coochassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coochassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    coochassisIndex.setDescription("""\
1600.0010.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooState_Type = DellStateSettings
_CooState_Object = MibTableColumn
cooState = _CooState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 2),
    _CooState_Type()
)
cooState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooState.setDescription("""\
1600.0010.0001.0002 This attribute defines the Dell Cost of Ownership:
Aquisition state of the Dell System.
""")
_CooAquisitionPurchaseCost_Type = DellUnsigned32BitRange
_CooAquisitionPurchaseCost_Object = MibTableColumn
cooAquisitionPurchaseCost = _CooAquisitionPurchaseCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 3),
    _CooAquisitionPurchaseCost_Type()
)
cooAquisitionPurchaseCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseCost.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseCost.setDescription("""\
1600.0010.0001.0003 This attribute defines the purchase cost of the Dell
System.
""")
_CooAquisitionWayBillNumber_Type = DellUnsigned32BitRange
_CooAquisitionWayBillNumber_Object = MibTableColumn
cooAquisitionWayBillNumber = _CooAquisitionWayBillNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 4),
    _CooAquisitionWayBillNumber_Type()
)
cooAquisitionWayBillNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooAquisitionWayBillNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooAquisitionWayBillNumber.setDescription("""\
1600.0010.0001.0004 This attribute defines the waybill number of the Dell
System.
""")
_CooAquisitionInstallDateName_Type = DellDateName
_CooAquisitionInstallDateName_Object = MibTableColumn
cooAquisitionInstallDateName = _CooAquisitionInstallDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 5),
    _CooAquisitionInstallDateName_Type()
)
cooAquisitionInstallDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooAquisitionInstallDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooAquisitionInstallDateName.setDescription("""\
1600.0010.0001.0005 This attribute defines the install time of the Dell System.
Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooAquisitionPurchaseOrder_Type = DellUnsigned32BitRange
_CooAquisitionPurchaseOrder_Object = MibTableColumn
cooAquisitionPurchaseOrder = _CooAquisitionPurchaseOrder_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 6),
    _CooAquisitionPurchaseOrder_Type()
)
cooAquisitionPurchaseOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseOrder.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseOrder.setDescription("""\
1600.0010.0001.0006 This attribute defines the purchase order number of the
Dell System.
""")
_CooAquisitionPurchaseDateName_Type = DellDateName
_CooAquisitionPurchaseDateName_Object = MibTableColumn
cooAquisitionPurchaseDateName = _CooAquisitionPurchaseDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 7),
    _CooAquisitionPurchaseDateName_Type()
)
cooAquisitionPurchaseDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooAquisitionPurchaseDateName.setDescription("""\
1600.0010.0001.0007 This attribute defines the purchase time of the Dell
System. Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooAquisitionSigningAuthorityName_Type = DellCostofOwnershipString
_CooAquisitionSigningAuthorityName_Object = MibTableColumn
cooAquisitionSigningAuthorityName = _CooAquisitionSigningAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 8),
    _CooAquisitionSigningAuthorityName_Type()
)
cooAquisitionSigningAuthorityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooAquisitionSigningAuthorityName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooAquisitionSigningAuthorityName.setDescription("""\
1600.0010.0001.0008 This attribute defines the name of the signing authority
for the Dell System.
""")
_CooOriginalMachineConfigurationExpensed_Type = DellBoolean
_CooOriginalMachineConfigurationExpensed_Object = MibTableColumn
cooOriginalMachineConfigurationExpensed = _CooOriginalMachineConfigurationExpensed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 9),
    _CooOriginalMachineConfigurationExpensed_Type()
)
cooOriginalMachineConfigurationExpensed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOriginalMachineConfigurationExpensed.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOriginalMachineConfigurationExpensed.setDescription("""\
1600.0010.0001.0009 This attribute defines the purchase of the Dell System was
expensed or not.
""")
_CooOriginalMachineConfigurationVendorName_Type = DellCostofOwnershipString
_CooOriginalMachineConfigurationVendorName_Object = MibTableColumn
cooOriginalMachineConfigurationVendorName = _CooOriginalMachineConfigurationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 10),
    _CooOriginalMachineConfigurationVendorName_Type()
)
cooOriginalMachineConfigurationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOriginalMachineConfigurationVendorName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOriginalMachineConfigurationVendorName.setDescription("""\
1600.0010.0001.0010 This attribute defines the vendor name of the Dell System.
""")
_CooCostCenterInformationVendorName_Type = DellCostofOwnershipString
_CooCostCenterInformationVendorName_Object = MibTableColumn
cooCostCenterInformationVendorName = _CooCostCenterInformationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 11),
    _CooCostCenterInformationVendorName_Type()
)
cooCostCenterInformationVendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooCostCenterInformationVendorName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostCenterInformationVendorName.setDescription("""\
1600.0010.0001.0011 This attribute defines the cost center name of the Dell
System.
""")
_CooUserInformationUserName_Type = DellCostofOwnershipString
_CooUserInformationUserName_Object = MibTableColumn
cooUserInformationUserName = _CooUserInformationUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 12),
    _CooUserInformationUserName_Type()
)
cooUserInformationUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooUserInformationUserName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooUserInformationUserName.setDescription("""\
1600.0010.0001.0012 This attribute defines the user name of the Dell System.
""")
_CooExtendedWarrantyStartDateName_Type = DellDateName
_CooExtendedWarrantyStartDateName_Object = MibTableColumn
cooExtendedWarrantyStartDateName = _CooExtendedWarrantyStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 13),
    _CooExtendedWarrantyStartDateName_Type()
)
cooExtendedWarrantyStartDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooExtendedWarrantyStartDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooExtendedWarrantyStartDateName.setDescription("""\
1600.0010.0001.0013 This attribute defines Extended Warranty start date for the
Dell System. Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff
or yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooExtendedWarrantyEndDateName_Type = DellDateName
_CooExtendedWarrantyEndDateName_Object = MibTableColumn
cooExtendedWarrantyEndDateName = _CooExtendedWarrantyEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 14),
    _CooExtendedWarrantyEndDateName_Type()
)
cooExtendedWarrantyEndDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooExtendedWarrantyEndDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooExtendedWarrantyEndDateName.setDescription("""\
1600.0010.0001.0014 This attribute defines Extended Warranty end date for the
Dell System. Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff
or yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooExtendedWarrantyCost_Type = DellUnsigned32BitRange
_CooExtendedWarrantyCost_Object = MibTableColumn
cooExtendedWarrantyCost = _CooExtendedWarrantyCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 15),
    _CooExtendedWarrantyCost_Type()
)
cooExtendedWarrantyCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooExtendedWarrantyCost.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooExtendedWarrantyCost.setDescription("""\
1600.0010.0001.0015 This attribute defines Extended Warranty cost for the Dell
System.
""")
_CooExtendedWarrantyProviderName_Type = DellCostofOwnershipString
_CooExtendedWarrantyProviderName_Object = MibTableColumn
cooExtendedWarrantyProviderName = _CooExtendedWarrantyProviderName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 16),
    _CooExtendedWarrantyProviderName_Type()
)
cooExtendedWarrantyProviderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooExtendedWarrantyProviderName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooExtendedWarrantyProviderName.setDescription("""\
1600.0010.0001.0016 This attribute defines the Extended Warranty service
provider name for the Dell System.
""")
_CooOwnershipCode_Type = DellCooOwnershipCodes
_CooOwnershipCode_Object = MibTableColumn
cooOwnershipCode = _CooOwnershipCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 17),
    _CooOwnershipCode_Type()
)
cooOwnershipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOwnershipCode.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOwnershipCode.setDescription("""\
1600.0010.0001.0017 This attribute defines ownership code for the Dell System.
""")
_CooCorporateOwnerName_Type = DellCostofOwnershipString
_CooCorporateOwnerName_Object = MibTableColumn
cooCorporateOwnerName = _CooCorporateOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 18),
    _CooCorporateOwnerName_Type()
)
cooCorporateOwnerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooCorporateOwnerName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCorporateOwnerName.setDescription("""\
1600.0010.0001.0018 This attribute defines the name of the corporate owner for
the Dell System.
""")
_CooHazardousWasteCodeName_Type = DellCostofOwnershipString
_CooHazardousWasteCodeName_Object = MibTableColumn
cooHazardousWasteCodeName = _CooHazardousWasteCodeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 19),
    _CooHazardousWasteCodeName_Type()
)
cooHazardousWasteCodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooHazardousWasteCodeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooHazardousWasteCodeName.setDescription("""\
1600.0010.0001.0019 This attribute defines the name Hazardous Waste code for
the Dell System.
""")
_CooDeploymentDateLength_Type = DellUnsigned32BitRange
_CooDeploymentDateLength_Object = MibTableColumn
cooDeploymentDateLength = _CooDeploymentDateLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 20),
    _CooDeploymentDateLength_Type()
)
cooDeploymentDateLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooDeploymentDateLength.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooDeploymentDateLength.setDescription("""\
1600.0010.0001.0020 This attribute defines the Deployment Time for the Dell
System.
""")
_CooDeploymentDurationType_Type = DellCooHourDayDurationType
_CooDeploymentDurationType_Object = MibTableColumn
cooDeploymentDurationType = _CooDeploymentDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 21),
    _CooDeploymentDurationType_Type()
)
cooDeploymentDurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooDeploymentDurationType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooDeploymentDurationType.setDescription("""\
1600.0010.0001.0021 This attribute defines the Deployment Time units for the
Dell System.
""")
_CooTrainingName_Type = DellCostofOwnershipString
_CooTrainingName_Object = MibTableColumn
cooTrainingName = _CooTrainingName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 22),
    _CooTrainingName_Type()
)
cooTrainingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooTrainingName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTrainingName.setDescription("""\
1600.0010.0001.0022 This attribute defines the training the user has for the
Dell System.
""")
_CooOutsourcingProblemDescriptionName_Type = DellCostofOwnershipString
_CooOutsourcingProblemDescriptionName_Object = MibTableColumn
cooOutsourcingProblemDescriptionName = _CooOutsourcingProblemDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 23),
    _CooOutsourcingProblemDescriptionName_Type()
)
cooOutsourcingProblemDescriptionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOutsourcingProblemDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOutsourcingProblemDescriptionName.setDescription("""\
1600.0010.0001.0023 This attribute defines the problem description name of the
Outsourcing service provider.
""")
_CooOutsourcingServiceFeeName_Type = DellCostofOwnershipString
_CooOutsourcingServiceFeeName_Object = MibTableColumn
cooOutsourcingServiceFeeName = _CooOutsourcingServiceFeeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 24),
    _CooOutsourcingServiceFeeName_Type()
)
cooOutsourcingServiceFeeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOutsourcingServiceFeeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOutsourcingServiceFeeName.setDescription("""\
1600.0010.0001.0024 This attribute defines the Outsourcing vendors' charge for
service.
""")
_CooOutsourcingSigningAuthorityName_Type = DellCostofOwnershipString
_CooOutsourcingSigningAuthorityName_Object = MibTableColumn
cooOutsourcingSigningAuthorityName = _CooOutsourcingSigningAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 25),
    _CooOutsourcingSigningAuthorityName_Type()
)
cooOutsourcingSigningAuthorityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOutsourcingSigningAuthorityName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOutsourcingSigningAuthorityName.setDescription("""\
1600.0010.0001.0025 This attribute defines the name of the person who has
signing authority for service.
""")
_CooOutsourcingProviderFeeName_Type = DellCostofOwnershipString
_CooOutsourcingProviderFeeName_Object = MibTableColumn
cooOutsourcingProviderFeeName = _CooOutsourcingProviderFeeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 26),
    _CooOutsourcingProviderFeeName_Type()
)
cooOutsourcingProviderFeeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOutsourcingProviderFeeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOutsourcingProviderFeeName.setDescription("""\
1600.0010.0001.0026 This attribute defines any additional Outsourcing charge
for service.
""")
_CooOutsourcingProviderServiceLevelName_Type = DellCostofOwnershipString
_CooOutsourcingProviderServiceLevelName_Object = MibTableColumn
cooOutsourcingProviderServiceLevelName = _CooOutsourcingProviderServiceLevelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 27),
    _CooOutsourcingProviderServiceLevelName_Type()
)
cooOutsourcingProviderServiceLevelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOutsourcingProviderServiceLevelName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOutsourcingProviderServiceLevelName.setDescription("""\
1600.0010.0001.0027 This attribute defines service level agreement for service.
""")
_CooInsuranceCompanyName_Type = DellCostofOwnershipString
_CooInsuranceCompanyName_Object = MibTableColumn
cooInsuranceCompanyName = _CooInsuranceCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 28),
    _CooInsuranceCompanyName_Type()
)
cooInsuranceCompanyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooInsuranceCompanyName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooInsuranceCompanyName.setDescription("""\
1600.0010.0001.0028 This attribute defines the name of the company insuring the
Dell System.
""")
_CooBoxAssetTagName_Type = DellCostofOwnershipString
_CooBoxAssetTagName_Object = MibTableColumn
cooBoxAssetTagName = _CooBoxAssetTagName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 29),
    _CooBoxAssetTagName_Type()
)
cooBoxAssetTagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooBoxAssetTagName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooBoxAssetTagName.setDescription("""\
1600.0010.0001.0029 This attribute defines the name the Dell System asset tag.
""")
_CooBoxSystemName_Type = DellCostofOwnershipString
_CooBoxSystemName_Object = MibTableColumn
cooBoxSystemName = _CooBoxSystemName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 30),
    _CooBoxSystemName_Type()
)
cooBoxSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooBoxSystemName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooBoxSystemName.setDescription("""\
1600.0010.0001.0030 This attribute defines the name of the Dell System.
""")
_CooBoxCPUSerialNumberName_Type = DellCostofOwnershipString
_CooBoxCPUSerialNumberName_Object = MibTableColumn
cooBoxCPUSerialNumberName = _CooBoxCPUSerialNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 31),
    _CooBoxCPUSerialNumberName_Type()
)
cooBoxCPUSerialNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooBoxCPUSerialNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooBoxCPUSerialNumberName.setDescription("""\
1600.0010.0001.0031 This attribute defines the name of the CPU serial number in
the Dell System.
""")
_CooOperatingSystemUpgradeTypeName_Type = DellCostofOwnershipString
_CooOperatingSystemUpgradeTypeName_Object = MibTableColumn
cooOperatingSystemUpgradeTypeName = _CooOperatingSystemUpgradeTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 32),
    _CooOperatingSystemUpgradeTypeName_Type()
)
cooOperatingSystemUpgradeTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradeTypeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradeTypeName.setDescription("""\
1600.0010.0001.0032 This attribute defines the name the operating system on the
Dell System.
""")
_CooOperatingSystemUpgradePatchLevelName_Type = DellCostofOwnershipString
_CooOperatingSystemUpgradePatchLevelName_Object = MibTableColumn
cooOperatingSystemUpgradePatchLevelName = _CooOperatingSystemUpgradePatchLevelName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 33),
    _CooOperatingSystemUpgradePatchLevelName_Type()
)
cooOperatingSystemUpgradePatchLevelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradePatchLevelName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradePatchLevelName.setDescription("""\
1600.0010.0001.0033 This attribute defines the name of the operating system
patch level of the Dell System.
""")
_CooOperatingSystemUpgradeDate_Type = DellCostofOwnershipString
_CooOperatingSystemUpgradeDate_Object = MibTableColumn
cooOperatingSystemUpgradeDate = _CooOperatingSystemUpgradeDate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 34),
    _CooOperatingSystemUpgradeDate_Type()
)
cooOperatingSystemUpgradeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradeDate.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOperatingSystemUpgradeDate.setDescription("""\
1600.0010.0001.0034 This attribute defines the upgrade file date.
""")
_CooDepreciationDuration_Type = DellUnsigned32BitRange
_CooDepreciationDuration_Object = MibTableColumn
cooDepreciationDuration = _CooDepreciationDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 35),
    _CooDepreciationDuration_Type()
)
cooDepreciationDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooDepreciationDuration.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooDepreciationDuration.setDescription("""\
1600.0010.0001.0035 This attribute defines the Depreciation duration for the
Dell System.
""")
_CooDepreciationDurationType_Type = DellCooMonthYearDurationType
_CooDepreciationDurationType_Object = MibTableColumn
cooDepreciationDurationType = _CooDepreciationDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 36),
    _CooDepreciationDurationType_Type()
)
cooDepreciationDurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooDepreciationDurationType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooDepreciationDurationType.setDescription("""\
1600.0010.0001.0036 This attribute defines the unit of time for Depreciation
for the Dell System.
""")
_CooDepreciationPercentage_Type = DellUnsigned32BitRange
_CooDepreciationPercentage_Object = MibTableColumn
cooDepreciationPercentage = _CooDepreciationPercentage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 37),
    _CooDepreciationPercentage_Type()
)
cooDepreciationPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooDepreciationPercentage.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooDepreciationPercentage.setDescription("""\
1600.0010.0001.0037 This attribute defines the percentage of Depreciation for
the Dell System.
""")
_CooDepreciationMethodName_Type = DellCostofOwnershipString
_CooDepreciationMethodName_Object = MibTableColumn
cooDepreciationMethodName = _CooDepreciationMethodName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 38),
    _CooDepreciationMethodName_Type()
)
cooDepreciationMethodName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooDepreciationMethodName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooDepreciationMethodName.setDescription("""\
1600.0010.0001.0038 This attribute defines the method name of Depreciation for
the Dell System.
""")
_CooRegistrationIsRegistered_Type = DellBoolean
_CooRegistrationIsRegistered_Object = MibTableColumn
cooRegistrationIsRegistered = _CooRegistrationIsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 10, 1, 39),
    _CooRegistrationIsRegistered_Type()
)
cooRegistrationIsRegistered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooRegistrationIsRegistered.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRegistrationIsRegistered.setDescription("""\
1600.0010.0001.0039 This attribute defines if the Dell System is registered or
not.
""")
_CooServiceContractTable_Object = MibTable
cooServiceContractTable = _CooServiceContractTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20)
)
if mibBuilder.loadTexts:
    cooServiceContractTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractTable.setDescription("""\
1600.0020 This Group defines the Dell Cost of Ownership: Service Contract
Table.
""")
_CooServiceContractTableEntry_Object = MibTableRow
cooServiceContractTableEntry = _CooServiceContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1)
)
cooServiceContractTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooServiceContractchassisIndex"),
    (0, "MIB-Dell-10892", "cooServiceContractIndex"),
)
if mibBuilder.loadTexts:
    cooServiceContractTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractTableEntry.setDescription("""\
1600.0020.0001 This Group defines the Dell Cost of Ownership: Service Contract
Table Entry.
""")
_CooServiceContractchassisIndex_Type = DellObjectRange
_CooServiceContractchassisIndex_Object = MibTableColumn
cooServiceContractchassisIndex = _CooServiceContractchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 1),
    _CooServiceContractchassisIndex_Type()
)
cooServiceContractchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractchassisIndex.setDescription("""\
1600.0020.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooServiceContractIndex_Type = DellObjectRange
_CooServiceContractIndex_Object = MibTableColumn
cooServiceContractIndex = _CooServiceContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 2),
    _CooServiceContractIndex_Type()
)
cooServiceContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractIndex.setDescription("""\
1600.0020.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Service Contract.
""")
_CooServiceContractState_Type = DellStateSettings
_CooServiceContractState_Object = MibTableColumn
cooServiceContractState = _CooServiceContractState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 3),
    _CooServiceContractState_Type()
)
cooServiceContractState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooServiceContractState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractState.setDescription("""\
1600.0020.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Service Contract state of the Dell System.
""")
_CooServiceContractWasRenewed_Type = DellBoolean
_CooServiceContractWasRenewed_Object = MibTableColumn
cooServiceContractWasRenewed = _CooServiceContractWasRenewed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 4),
    _CooServiceContractWasRenewed_Type()
)
cooServiceContractWasRenewed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooServiceContractWasRenewed.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractWasRenewed.setDescription("""\
1600.0020.0001.0004 This attribute defines if the Dell System Service Contract
was renewed not.
""")
_CooServiceContractTypeName_Type = DellCostofOwnershipString
_CooServiceContractTypeName_Object = MibTableColumn
cooServiceContractTypeName = _CooServiceContractTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 5),
    _CooServiceContractTypeName_Type()
)
cooServiceContractTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooServiceContractTypeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractTypeName.setDescription("""\
1600.0020.0001.0005 This attribute defines the name of the Service Contract
type for the Dell System.
""")
_CooServiceContractVendorName_Type = DellCostofOwnershipString
_CooServiceContractVendorName_Object = MibTableColumn
cooServiceContractVendorName = _CooServiceContractVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 20, 1, 6),
    _CooServiceContractVendorName_Type()
)
cooServiceContractVendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooServiceContractVendorName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooServiceContractVendorName.setDescription("""\
1600.0020.0001.0006 This attribute defines the name of the Service Contract
provider for the Dell System.
""")
_CooCostEventLogTable_Object = MibTable
cooCostEventLogTable = _CooCostEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30)
)
if mibBuilder.loadTexts:
    cooCostEventLogTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogTable.setDescription("""\
1600.0030 This Group defines the Dell Cost of Ownership: Cost Event Log Table.
""")
_CooCostEventLogTableEntry_Object = MibTableRow
cooCostEventLogTableEntry = _CooCostEventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1)
)
cooCostEventLogTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooCostEventLogchassisIndex"),
    (0, "MIB-Dell-10892", "cooCostEventLogIndex"),
)
if mibBuilder.loadTexts:
    cooCostEventLogTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogTableEntry.setDescription("""\
1600.0030.0001 This Group defines the Dell Cost of Ownership: Cost Event Log
Table Entry.
""")
_CooCostEventLogchassisIndex_Type = DellObjectRange
_CooCostEventLogchassisIndex_Object = MibTableColumn
cooCostEventLogchassisIndex = _CooCostEventLogchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 1),
    _CooCostEventLogchassisIndex_Type()
)
cooCostEventLogchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogchassisIndex.setDescription("""\
1600.0030.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooCostEventLogIndex_Type = DellObjectRange
_CooCostEventLogIndex_Object = MibTableColumn
cooCostEventLogIndex = _CooCostEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 2),
    _CooCostEventLogIndex_Type()
)
cooCostEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogIndex.setDescription("""\
1600.0030.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Cost Event Log.
""")
_CooCostEventLogState_Type = DellStateSettings
_CooCostEventLogState_Object = MibTableColumn
cooCostEventLogState = _CooCostEventLogState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 3),
    _CooCostEventLogState_Type()
)
cooCostEventLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCostEventLogState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogState.setDescription("""\
1600.0030.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Cost Event Log state of the Dell System.
""")
_CooCostEventLogDuration_Type = DellUnsigned32BitRange
_CooCostEventLogDuration_Object = MibTableColumn
cooCostEventLogDuration = _CooCostEventLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 4),
    _CooCostEventLogDuration_Type()
)
cooCostEventLogDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooCostEventLogDuration.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogDuration.setDescription("""\
1600.0030.0001.0004 This attribute defines duration of the event.
""")
_CooCostEventLogDurationType_Type = DellCooHourDayDurationType
_CooCostEventLogDurationType_Object = MibTableColumn
cooCostEventLogDurationType = _CooCostEventLogDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 5),
    _CooCostEventLogDurationType_Type()
)
cooCostEventLogDurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooCostEventLogDurationType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogDurationType.setDescription("""\
1600.0030.0001.0005 This attribute defines the of the Cost Event Log duration
type for the Dell System.
""")
_CooCostEventLogDescriptionName_Type = DellCostofOwnershipString
_CooCostEventLogDescriptionName_Object = MibTableColumn
cooCostEventLogDescriptionName = _CooCostEventLogDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 30, 1, 6),
    _CooCostEventLogDescriptionName_Type()
)
cooCostEventLogDescriptionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooCostEventLogDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooCostEventLogDescriptionName.setDescription("""\
1600.0030.0001.0006 This attribute defines the name of the event description
logged for the event.
""")
_CooWarrantyTable_Object = MibTable
cooWarrantyTable = _CooWarrantyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40)
)
if mibBuilder.loadTexts:
    cooWarrantyTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyTable.setDescription("""\
1600.0040 This Group defines the Dell Cost of Ownership: Warranty Table.
""")
_CooWarrantyTableEntry_Object = MibTableRow
cooWarrantyTableEntry = _CooWarrantyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1)
)
cooWarrantyTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooWarrantychassisIndex"),
    (0, "MIB-Dell-10892", "cooWarrantyIndex"),
)
if mibBuilder.loadTexts:
    cooWarrantyTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyTableEntry.setDescription("""\
1600.0040.0001 This Group defines the Dell Cost of Ownership: Warranty Table
Entry.
""")
_CooWarrantychassisIndex_Type = DellObjectRange
_CooWarrantychassisIndex_Object = MibTableColumn
cooWarrantychassisIndex = _CooWarrantychassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 1),
    _CooWarrantychassisIndex_Type()
)
cooWarrantychassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantychassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantychassisIndex.setDescription("""\
1600.0040.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooWarrantyIndex_Type = DellObjectRange
_CooWarrantyIndex_Object = MibTableColumn
cooWarrantyIndex = _CooWarrantyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 2),
    _CooWarrantyIndex_Type()
)
cooWarrantyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyIndex.setDescription("""\
1600.0040.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Warranty.
""")
_CooWarrantyState_Type = DellStateSettings
_CooWarrantyState_Object = MibTableColumn
cooWarrantyState = _CooWarrantyState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 3),
    _CooWarrantyState_Type()
)
cooWarrantyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooWarrantyState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyState.setDescription("""\
1600.0040.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Warranty state of the Dell System.
""")
_CooWarrantyDuration_Type = DellUnsigned32BitRange
_CooWarrantyDuration_Object = MibTableColumn
cooWarrantyDuration = _CooWarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 4),
    _CooWarrantyDuration_Type()
)
cooWarrantyDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooWarrantyDuration.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyDuration.setDescription("""\
1600.0040.0001.0004 This attribute defines duration of the warranty.
""")
_CooWarrantyDurationType_Type = DellCooDayMonthDurationType
_CooWarrantyDurationType_Object = MibTableColumn
cooWarrantyDurationType = _CooWarrantyDurationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 5),
    _CooWarrantyDurationType_Type()
)
cooWarrantyDurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooWarrantyDurationType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyDurationType.setDescription("""\
1600.0040.0001.0005 This attribute defines the Warranty duration type for the
Dell System.
""")
_CooWarrantyEndDateName_Type = DellDateName
_CooWarrantyEndDateName_Object = MibTableColumn
cooWarrantyEndDateName = _CooWarrantyEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 6),
    _CooWarrantyEndDateName_Type()
)
cooWarrantyEndDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooWarrantyEndDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyEndDateName.setDescription("""\
1600.0040.0001.0006 This attribute defines the Warranty end date for the Dell
System. Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooWarrantyCost_Type = DellUnsigned32BitRange
_CooWarrantyCost_Object = MibTableColumn
cooWarrantyCost = _CooWarrantyCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 40, 1, 7),
    _CooWarrantyCost_Type()
)
cooWarrantyCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooWarrantyCost.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooWarrantyCost.setDescription("""\
1600.0040.0001.0007 This attribute defines the Warranty cost for the Dell
System.
""")
_CooLeaseInformationTable_Object = MibTable
cooLeaseInformationTable = _CooLeaseInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50)
)
if mibBuilder.loadTexts:
    cooLeaseInformationTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationTable.setDescription("""\
1600.0050 This Group defines the Dell Cost of Ownership: Lease Information
Table.
""")
_CooLeaseInformationTableEntry_Object = MibTableRow
cooLeaseInformationTableEntry = _CooLeaseInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1)
)
cooLeaseInformationTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooLeaseInformationchassisIndex"),
    (0, "MIB-Dell-10892", "cooLeaseInformationIndex"),
)
if mibBuilder.loadTexts:
    cooLeaseInformationTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationTableEntry.setDescription("""\
1600.0050.0001 This Group defines the Dell Cost of Ownership: Lease Information
Table Entry.
""")
_CooLeaseInformationchassisIndex_Type = DellObjectRange
_CooLeaseInformationchassisIndex_Object = MibTableColumn
cooLeaseInformationchassisIndex = _CooLeaseInformationchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 1),
    _CooLeaseInformationchassisIndex_Type()
)
cooLeaseInformationchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationchassisIndex.setDescription("""\
1600.0050.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooLeaseInformationIndex_Type = DellObjectRange
_CooLeaseInformationIndex_Object = MibTableColumn
cooLeaseInformationIndex = _CooLeaseInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 2),
    _CooLeaseInformationIndex_Type()
)
cooLeaseInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationIndex.setDescription("""\
1600.0050.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Lease Information.
""")
_CooLeaseInformationState_Type = DellStateSettings
_CooLeaseInformationState_Object = MibTableColumn
cooLeaseInformationState = _CooLeaseInformationState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 3),
    _CooLeaseInformationState_Type()
)
cooLeaseInformationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationState.setDescription("""\
1600.0050.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Lease Information state of the Dell System.
""")
_CooLeaseInformationMultipleSchedules_Type = DellBoolean
_CooLeaseInformationMultipleSchedules_Object = MibTableColumn
cooLeaseInformationMultipleSchedules = _CooLeaseInformationMultipleSchedules_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 4),
    _CooLeaseInformationMultipleSchedules_Type()
)
cooLeaseInformationMultipleSchedules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooLeaseInformationMultipleSchedules.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationMultipleSchedules.setDescription("""\
1600.0050.0001.0004 This attribute defines if there are multiple schedules for
this lease.
""")
_CooLeaseInformationBuyOutAmount_Type = DellUnsigned32BitRange
_CooLeaseInformationBuyOutAmount_Object = MibTableColumn
cooLeaseInformationBuyOutAmount = _CooLeaseInformationBuyOutAmount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 5),
    _CooLeaseInformationBuyOutAmount_Type()
)
cooLeaseInformationBuyOutAmount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooLeaseInformationBuyOutAmount.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationBuyOutAmount.setDescription("""\
1600.0050.0001.0005 This attribute defines buy out amount for this lease.
""")
_CooLeaseInformationLeaseRateFactor_Type = DellUnsigned32BitRange
_CooLeaseInformationLeaseRateFactor_Object = MibTableColumn
cooLeaseInformationLeaseRateFactor = _CooLeaseInformationLeaseRateFactor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 6),
    _CooLeaseInformationLeaseRateFactor_Type()
)
cooLeaseInformationLeaseRateFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooLeaseInformationLeaseRateFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationLeaseRateFactor.setDescription("""\
1600.0050.0001.0006 This attribute defines the Lease Information lease rate
factor.
""")
_CooLeaseInformationEndDateName_Type = DellDateName
_CooLeaseInformationEndDateName_Object = MibTableColumn
cooLeaseInformationEndDateName = _CooLeaseInformationEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 7),
    _CooLeaseInformationEndDateName_Type()
)
cooLeaseInformationEndDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooLeaseInformationEndDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationEndDateName.setDescription("""\
1600.0050.0001.0007 This attribute defines the Lease Information end date for
the Dell System. Dates are defined in the ASCII format:
yyyyMMddhhmmss.uuuuuu+fff or yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year,
MM is the month, dd is the day, hh are the hours, mm are the minutes and ss are
the seconds. uuuuuu is the number of microseconds, and +fff or -fff is the
offset from UTC in minutes.
""")
_CooLeaseInformationFairMarketValue_Type = DellUnsigned32BitRange
_CooLeaseInformationFairMarketValue_Object = MibTableColumn
cooLeaseInformationFairMarketValue = _CooLeaseInformationFairMarketValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 8),
    _CooLeaseInformationFairMarketValue_Type()
)
cooLeaseInformationFairMarketValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooLeaseInformationFairMarketValue.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationFairMarketValue.setDescription("""\
1600.0050.0001.0008 This attribute defines the Lease Information fair market
value for the Dell System.
""")
_CooLeaseInformationLessorName_Type = DellCostofOwnershipString
_CooLeaseInformationLessorName_Object = MibTableColumn
cooLeaseInformationLessorName = _CooLeaseInformationLessorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 50, 1, 9),
    _CooLeaseInformationLessorName_Type()
)
cooLeaseInformationLessorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooLeaseInformationLessorName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooLeaseInformationLessorName.setDescription("""\
1600.0050.0001.0009 This attribute defines the Lease Information Lessor's name.
""")
_CooScheduleNumberTable_Object = MibTable
cooScheduleNumberTable = _CooScheduleNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60)
)
if mibBuilder.loadTexts:
    cooScheduleNumberTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberTable.setDescription("""\
1600.0060 This Group defines the Dell Cost of Ownership: Schedule Number
Information Table.
""")
_CooScheduleNumberTableEntry_Object = MibTableRow
cooScheduleNumberTableEntry = _CooScheduleNumberTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1)
)
cooScheduleNumberTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooScheduleNumberchassisIndex"),
    (0, "MIB-Dell-10892", "cooScheduleNumberIndex"),
)
if mibBuilder.loadTexts:
    cooScheduleNumberTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberTableEntry.setDescription("""\
1600.0060.0001 This Group defines the Dell Cost of Ownership: Schedule Number
Information Table Entry.
""")
_CooScheduleNumberchassisIndex_Type = DellObjectRange
_CooScheduleNumberchassisIndex_Object = MibTableColumn
cooScheduleNumberchassisIndex = _CooScheduleNumberchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 1),
    _CooScheduleNumberchassisIndex_Type()
)
cooScheduleNumberchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberchassisIndex.setDescription("""\
1600.0060.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooScheduleNumberIndex_Type = DellObjectRange
_CooScheduleNumberIndex_Object = MibTableColumn
cooScheduleNumberIndex = _CooScheduleNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 2),
    _CooScheduleNumberIndex_Type()
)
cooScheduleNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberIndex.setDescription("""\
1600.0060.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Schedule Number Information.
""")
_CooScheduleNumberState_Type = DellStateSettings
_CooScheduleNumberState_Object = MibTableColumn
cooScheduleNumberState = _CooScheduleNumberState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 3),
    _CooScheduleNumberState_Type()
)
cooScheduleNumberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooScheduleNumberState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberState.setDescription("""\
1600.0060.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Schedule Number Information state of the Dell System.
""")
_CooScheduleNumberLeaseInformationIndexReference_Type = DellUnsigned32BitRange
_CooScheduleNumberLeaseInformationIndexReference_Object = MibTableColumn
cooScheduleNumberLeaseInformationIndexReference = _CooScheduleNumberLeaseInformationIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 4),
    _CooScheduleNumberLeaseInformationIndexReference_Type()
)
cooScheduleNumberLeaseInformationIndexReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooScheduleNumberLeaseInformationIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberLeaseInformationIndexReference.setDescription("""\
1600.0060.0001.0004 This attribute defines the Lease Information index number
to reference this Schedule Number too.
""")
_CooScheduleNumberDescriptionName_Type = DellCostofOwnershipString
_CooScheduleNumberDescriptionName_Object = MibTableColumn
cooScheduleNumberDescriptionName = _CooScheduleNumberDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 60, 1, 5),
    _CooScheduleNumberDescriptionName_Type()
)
cooScheduleNumberDescriptionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooScheduleNumberDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooScheduleNumberDescriptionName.setDescription("""\
1600.0060.0001.0005 This attribute defines the Schedule Number Information
description name.
""")
_CooOptionsTable_Object = MibTable
cooOptionsTable = _CooOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70)
)
if mibBuilder.loadTexts:
    cooOptionsTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionsTable.setDescription("""\
1600.0070 This Group defines the Dell Cost of Ownership: Option Information
Table.
""")
_CooOptionsTableEntry_Object = MibTableRow
cooOptionsTableEntry = _CooOptionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1)
)
cooOptionsTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooOptionschassisIndex"),
    (0, "MIB-Dell-10892", "cooOptionsIndex"),
)
if mibBuilder.loadTexts:
    cooOptionsTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionsTableEntry.setDescription("""\
1600.0070.0001 This Group defines the Dell Cost of Ownership: Option
Information Table Entry.
""")
_CooOptionschassisIndex_Type = DellObjectRange
_CooOptionschassisIndex_Object = MibTableColumn
cooOptionschassisIndex = _CooOptionschassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 1),
    _CooOptionschassisIndex_Type()
)
cooOptionschassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionschassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionschassisIndex.setDescription("""\
1600.0070.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooOptionsIndex_Type = DellObjectRange
_CooOptionsIndex_Object = MibTableColumn
cooOptionsIndex = _CooOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 2),
    _CooOptionsIndex_Type()
)
cooOptionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionsIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionsIndex.setDescription("""\
1600.0070.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Option Information.
""")
_CooOptionsState_Type = DellStateSettings
_CooOptionsState_Object = MibTableColumn
cooOptionsState = _CooOptionsState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 3),
    _CooOptionsState_Type()
)
cooOptionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOptionsState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionsState.setDescription("""\
1600.0070.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Option Information state of the Dell System.
""")
_CooOptionsLeaseInformationIndexReference_Type = DellUnsigned32BitRange
_CooOptionsLeaseInformationIndexReference_Object = MibTableColumn
cooOptionsLeaseInformationIndexReference = _CooOptionsLeaseInformationIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 4),
    _CooOptionsLeaseInformationIndexReference_Type()
)
cooOptionsLeaseInformationIndexReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOptionsLeaseInformationIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionsLeaseInformationIndexReference.setDescription("""\
1600.0070.0001.0004 This attribute defines the Lease Information index number
to reference this option with.
""")
_CooOptionsDescriptionName_Type = DellCostofOwnershipString
_CooOptionsDescriptionName_Object = MibTableColumn
cooOptionsDescriptionName = _CooOptionsDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 70, 1, 5),
    _CooOptionsDescriptionName_Type()
)
cooOptionsDescriptionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOptionsDescriptionName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooOptionsDescriptionName.setDescription("""\
1600.0070.0001.0005 This attribute defines the Option Information description
name.
""")
_CooMaintenanceTable_Object = MibTable
cooMaintenanceTable = _CooMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80)
)
if mibBuilder.loadTexts:
    cooMaintenanceTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceTable.setDescription("""\
1600.0080 This Group defines the Dell Cost of Ownership: Maintenance
Information Table.
""")
_CooMaintenanceTableEntry_Object = MibTableRow
cooMaintenanceTableEntry = _CooMaintenanceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1)
)
cooMaintenanceTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooMaintenancechassisIndex"),
    (0, "MIB-Dell-10892", "cooMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    cooMaintenanceTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceTableEntry.setDescription("""\
1600.0080.0001 This Group defines the Dell Cost of Ownership: Maintenance
Information Table Entry.
""")
_CooMaintenancechassisIndex_Type = DellObjectRange
_CooMaintenancechassisIndex_Object = MibTableColumn
cooMaintenancechassisIndex = _CooMaintenancechassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 1),
    _CooMaintenancechassisIndex_Type()
)
cooMaintenancechassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenancechassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenancechassisIndex.setDescription("""\
1600.0080.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooMaintenanceIndex_Type = DellObjectRange
_CooMaintenanceIndex_Object = MibTableColumn
cooMaintenanceIndex = _CooMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 2),
    _CooMaintenanceIndex_Type()
)
cooMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceIndex.setDescription("""\
1600.0080.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Maintenance Information.
""")
_CooMaintenanceState_Type = DellStateSettings
_CooMaintenanceState_Object = MibTableColumn
cooMaintenanceState = _CooMaintenanceState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 3),
    _CooMaintenanceState_Type()
)
cooMaintenanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooMaintenanceState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceState.setDescription("""\
1600.0080.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Maintenance Information state of the Dell System.
""")
_CooMaintenanceStartDateName_Type = DellDateName
_CooMaintenanceStartDateName_Object = MibTableColumn
cooMaintenanceStartDateName = _CooMaintenanceStartDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 4),
    _CooMaintenanceStartDateName_Type()
)
cooMaintenanceStartDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooMaintenanceStartDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceStartDateName.setDescription("""\
1600.0080.0001.0004 This attribute defines the start date for Maintenance.
Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooMaintenanceEndDateName_Type = DellDateName
_CooMaintenanceEndDateName_Object = MibTableColumn
cooMaintenanceEndDateName = _CooMaintenanceEndDateName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 5),
    _CooMaintenanceEndDateName_Type()
)
cooMaintenanceEndDateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooMaintenanceEndDateName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceEndDateName.setDescription("""\
1600.0080.0001.0005 This attribute defines the ending date for Maintenance.
Dates are defined in the ASCII format: yyyyMMddhhmmss.uuuuuu+fff or
yyyyMMddhhmmss.uuuuuu-fff where yyyy is the year, MM is the month, dd is the
day, hh are the hours, mm are the minutes and ss are the seconds. uuuuuu is the
number of microseconds, and +fff or -fff is the offset from UTC in minutes.
""")
_CooMaintenanceProviderName_Type = DellCostofOwnershipString
_CooMaintenanceProviderName_Object = MibTableColumn
cooMaintenanceProviderName = _CooMaintenanceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 6),
    _CooMaintenanceProviderName_Type()
)
cooMaintenanceProviderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooMaintenanceProviderName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceProviderName.setDescription("""\
1600.0080.0001.0006 This attribute defines the Maintenance provider's name.
""")
_CooMaintenanceRestrictionsName_Type = DellCostofOwnershipString
_CooMaintenanceRestrictionsName_Object = MibTableColumn
cooMaintenanceRestrictionsName = _CooMaintenanceRestrictionsName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 80, 1, 7),
    _CooMaintenanceRestrictionsName_Type()
)
cooMaintenanceRestrictionsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooMaintenanceRestrictionsName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooMaintenanceRestrictionsName.setDescription("""\
1600.0080.0001.0007 This attribute defines the text of the Maintenance
agreement restrictions.
""")
_CooRepairTable_Object = MibTable
cooRepairTable = _CooRepairTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90)
)
if mibBuilder.loadTexts:
    cooRepairTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairTable.setDescription("""\
1600.0090 This Group defines the Dell Cost of Ownership: Repair Information
Table.
""")
_CooRepairTableEntry_Object = MibTableRow
cooRepairTableEntry = _CooRepairTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1)
)
cooRepairTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooRepairchassisIndex"),
    (0, "MIB-Dell-10892", "cooRepairIndex"),
)
if mibBuilder.loadTexts:
    cooRepairTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairTableEntry.setDescription("""\
1600.0090.0001 This Group defines the Dell Cost of Ownership: Repair
Information Table Entry.
""")
_CooRepairchassisIndex_Type = DellObjectRange
_CooRepairchassisIndex_Object = MibTableColumn
cooRepairchassisIndex = _CooRepairchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 1),
    _CooRepairchassisIndex_Type()
)
cooRepairchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairchassisIndex.setDescription("""\
1600.0090.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooRepairIndex_Type = DellObjectRange
_CooRepairIndex_Object = MibTableColumn
cooRepairIndex = _CooRepairIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 2),
    _CooRepairIndex_Type()
)
cooRepairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairIndex.setDescription("""\
1600.0090.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Repair Information.
""")
_CooRepairState_Type = DellStateSettings
_CooRepairState_Object = MibTableColumn
cooRepairState = _CooRepairState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 3),
    _CooRepairState_Type()
)
cooRepairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooRepairState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairState.setDescription("""\
1600.0090.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Repair Information state of the Dell System.
""")
_CooRepairCounter_Type = DellUnsigned32BitRange
_CooRepairCounter_Object = MibTableColumn
cooRepairCounter = _CooRepairCounter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 4),
    _CooRepairCounter_Type()
)
cooRepairCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooRepairCounter.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairCounter.setDescription("""\
1600.0090.0001.0004 This attribute defines the number of repairs this system
has had.
""")
_CooRepairVendorName_Type = DellCostofOwnershipString
_CooRepairVendorName_Object = MibTableColumn
cooRepairVendorName = _CooRepairVendorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 90, 1, 5),
    _CooRepairVendorName_Type()
)
cooRepairVendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooRepairVendorName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooRepairVendorName.setDescription("""\
1600.0090.0001.0005 This attribute defines the Repair vendors's name.
""")
_CooSupportInformationTable_Object = MibTable
cooSupportInformationTable = _CooSupportInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100)
)
if mibBuilder.loadTexts:
    cooSupportInformationTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationTable.setDescription("""\
1600.0100 This Group defines the Dell Cost of Ownership: Support Information
Table.
""")
_CooSupportInformationTableEntry_Object = MibTableRow
cooSupportInformationTableEntry = _CooSupportInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1)
)
cooSupportInformationTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooSupportInformationchassisIndex"),
    (0, "MIB-Dell-10892", "cooSupportInformationIndex"),
)
if mibBuilder.loadTexts:
    cooSupportInformationTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationTableEntry.setDescription("""\
1600.0100.0001 This Group defines the Dell Cost of Ownership: Support
Information Table Entry.
""")
_CooSupportInformationchassisIndex_Type = DellObjectRange
_CooSupportInformationchassisIndex_Object = MibTableColumn
cooSupportInformationchassisIndex = _CooSupportInformationchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 1),
    _CooSupportInformationchassisIndex_Type()
)
cooSupportInformationchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationchassisIndex.setDescription("""\
1600.0100.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooSupportInformationIndex_Type = DellObjectRange
_CooSupportInformationIndex_Object = MibTableColumn
cooSupportInformationIndex = _CooSupportInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 2),
    _CooSupportInformationIndex_Type()
)
cooSupportInformationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationIndex.setDescription("""\
1600.0100.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Support Information.
""")
_CooSupportInformationState_Type = DellStateSettings
_CooSupportInformationState_Object = MibTableColumn
cooSupportInformationState = _CooSupportInformationState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 3),
    _CooSupportInformationState_Type()
)
cooSupportInformationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooSupportInformationState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationState.setDescription("""\
1600.0100.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Support Information state of the Dell System.
""")
_CooSupportInformationIsOutsourced_Type = DellBoolean
_CooSupportInformationIsOutsourced_Object = MibTableColumn
cooSupportInformationIsOutsourced = _CooSupportInformationIsOutsourced_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 4),
    _CooSupportInformationIsOutsourced_Type()
)
cooSupportInformationIsOutsourced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooSupportInformationIsOutsourced.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationIsOutsourced.setDescription("""\
1600.0100.0001.0004 This attribute defines if support is outsourced or not.
""")
_CooSupportInformationType_Type = DellUnsigned32BitRange
_CooSupportInformationType_Object = MibTableColumn
cooSupportInformationType = _CooSupportInformationType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 5),
    _CooSupportInformationType_Type()
)
cooSupportInformationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooSupportInformationType.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationType.setDescription("""\
1600.0100.0001.0005 This attribute defines the type of of conmponent, system or
network problem that occured.
""")
_CooSupportInformationHelpDeskName_Type = DellCostofOwnershipString
_CooSupportInformationHelpDeskName_Object = MibTableColumn
cooSupportInformationHelpDeskName = _CooSupportInformationHelpDeskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 6),
    _CooSupportInformationHelpDeskName_Type()
)
cooSupportInformationHelpDeskName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooSupportInformationHelpDeskName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationHelpDeskName.setDescription("""\
1600.0100.0001.0006 This attribute defines the help desk support Information
provided.
""")
_CooSupportInformationFixTypeName_Type = DellCostofOwnershipString
_CooSupportInformationFixTypeName_Object = MibTableColumn
cooSupportInformationFixTypeName = _CooSupportInformationFixTypeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 100, 1, 7),
    _CooSupportInformationFixTypeName_Type()
)
cooSupportInformationFixTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooSupportInformationFixTypeName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooSupportInformationFixTypeName.setDescription("""\
1600.0100.0001.0007 This attribute defines the method used to fix the problem.
""")
_CooTroubleTicketTable_Object = MibTable
cooTroubleTicketTable = _CooTroubleTicketTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110)
)
if mibBuilder.loadTexts:
    cooTroubleTicketTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketTable.setDescription("""\
1600.0110 This Group defines the Dell Cost of Ownership: Trouble Ticket
Information Table.
""")
_CooTroubleTicketTableEntry_Object = MibTableRow
cooTroubleTicketTableEntry = _CooTroubleTicketTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1)
)
cooTroubleTicketTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "cooTroubleTicketchassisIndex"),
    (0, "MIB-Dell-10892", "cooTroubleTicketIndex"),
)
if mibBuilder.loadTexts:
    cooTroubleTicketTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketTableEntry.setDescription("""\
1600.0110.0001 This Group defines the Dell Cost of Ownership: Trouble Ticket
Information Table Entry.
""")
_CooTroubleTicketchassisIndex_Type = DellObjectRange
_CooTroubleTicketchassisIndex_Object = MibTableColumn
cooTroubleTicketchassisIndex = _CooTroubleTicketchassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 1),
    _CooTroubleTicketchassisIndex_Type()
)
cooTroubleTicketchassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketchassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketchassisIndex.setDescription("""\
1600.0110.0001.0001 This attribute defines the index (one based) of this Dell
chassis.
""")
_CooTroubleTicketIndex_Type = DellObjectRange
_CooTroubleTicketIndex_Object = MibTableColumn
cooTroubleTicketIndex = _CooTroubleTicketIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 2),
    _CooTroubleTicketIndex_Type()
)
cooTroubleTicketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketIndex.setDescription("""\
1600.0110.0001.0002 This attribute defines the index of the Dell Systems Cost
of Ownership: Trouble Ticket Information.
""")
_CooTroubleTicketState_Type = DellStateSettings
_CooTroubleTicketState_Object = MibTableColumn
cooTroubleTicketState = _CooTroubleTicketState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 3),
    _CooTroubleTicketState_Type()
)
cooTroubleTicketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooTroubleTicketState.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketState.setDescription("""\
1600.0110.0001.0003 This attribute defines the Dell Systems Cost of Ownership:
Trouble Ticket Information state of the Dell System.
""")
_CooTroubleTicketSupportInformationIndexReference_Type = DellUnsigned32BitRange
_CooTroubleTicketSupportInformationIndexReference_Object = MibTableColumn
cooTroubleTicketSupportInformationIndexReference = _CooTroubleTicketSupportInformationIndexReference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 4),
    _CooTroubleTicketSupportInformationIndexReference_Type()
)
cooTroubleTicketSupportInformationIndexReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooTroubleTicketSupportInformationIndexReference.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketSupportInformationIndexReference.setDescription("""\
1600.0110.0001.0004 This attribute defines the Support Information index number
to reference this Trouble Ticket with.
""")
_CooTroubleTicketNumberName_Type = DellCostofOwnershipString
_CooTroubleTicketNumberName_Object = MibTableColumn
cooTroubleTicketNumberName = _CooTroubleTicketNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1600, 110, 1, 5),
    _CooTroubleTicketNumberName_Type()
)
cooTroubleTicketNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooTroubleTicketNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    cooTroubleTicketNumberName.setDescription("""\
1600.0110.0001.0005 This attribute defines the Trouble Ticket number
description name.
""")
_RemoteAccessGroup_ObjectIdentity = ObjectIdentity
remoteAccessGroup = _RemoteAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700)
)
_RemoteAccessTable_Object = MibTable
remoteAccessTable = _RemoteAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10)
)
if mibBuilder.loadTexts:
    remoteAccessTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessTable.setDescription("""\
1700.0010 This object defines the Remote Access table.
""")
_RemoteAccessTableEntry_Object = MibTableRow
remoteAccessTableEntry = _RemoteAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1)
)
remoteAccessTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteAccessChassisIndex"),
    (0, "MIB-Dell-10892", "remoteAccessAdapterIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessTableEntry.setDescription("""\
1700.0010.0001 This object defines the Remote Access table entry.
""")
_RemoteAccessChassisIndex_Type = DellObjectRange
_RemoteAccessChassisIndex_Object = MibTableColumn
remoteAccessChassisIndex = _RemoteAccessChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 1),
    _RemoteAccessChassisIndex_Type()
)
remoteAccessChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessChassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessChassisIndex.setDescription("""\
1700.0010.0001.0001 This attribute defines the index (one based) of the chassis
containing the Remote Access hardware.
""")
_RemoteAccessAdapterIndex_Type = DellObjectRange
_RemoteAccessAdapterIndex_Object = MibTableColumn
remoteAccessAdapterIndex = _RemoteAccessAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 2),
    _RemoteAccessAdapterIndex_Type()
)
remoteAccessAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessAdapterIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessAdapterIndex.setDescription("""\
1700.0010.0001.0002 This attribute defines the index (one based) of the Remote
Access hardware.
""")
_RemoteAccessType_Type = DellRemoteAccessType
_RemoteAccessType_Object = MibTableColumn
remoteAccessType = _RemoteAccessType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 3),
    _RemoteAccessType_Type()
)
remoteAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessType.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessType.setDescription("""\
1700.0010.0001.0003 This attribute defines the type of the Remote Access
hardware.
""")
_RemoteAccessStateCapabilities_Type = DellStateCapabilities
_RemoteAccessStateCapabilities_Object = MibTableColumn
remoteAccessStateCapabilities = _RemoteAccessStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 4),
    _RemoteAccessStateCapabilities_Type()
)
remoteAccessStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessStateCapabilities.setDescription("""\
1700.0010.0001.0004 This attribute defines the state capabilities of the Remote
Access hardware.
""")
_RemoteAccessStateSettings_Type = DellStateSettings
_RemoteAccessStateSettings_Object = MibTableColumn
remoteAccessStateSettings = _RemoteAccessStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 5),
    _RemoteAccessStateSettings_Type()
)
remoteAccessStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessStateSettings.setDescription("""\
1700.0010.0001.0005 This attribute defines the state setting of the Remote
Access hardware.
""")
_RemoteAccessStatus_Type = DellStatus
_RemoteAccessStatus_Object = MibTableColumn
remoteAccessStatus = _RemoteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 6),
    _RemoteAccessStatus_Type()
)
remoteAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessStatus.setDescription("""\
1700.0010.0001.0006 This attribute defines the status of the Remote Access
hardware.
""")


class _RemoteAccessProductInfoName_Type(DisplayString):
    """Custom type remoteAccessProductInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessProductInfoName_Type.__name__ = "DisplayString"
_RemoteAccessProductInfoName_Object = MibTableColumn
remoteAccessProductInfoName = _RemoteAccessProductInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 7),
    _RemoteAccessProductInfoName_Type()
)
remoteAccessProductInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessProductInfoName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessProductInfoName.setDescription("""\
1700.0010.0001.0007 This attribute defines the name of the product providing
the Remote Access functionality.
""")


class _RemoteAccessDescriptionInfoName_Type(DisplayString):
    """Custom type remoteAccessDescriptionInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteAccessDescriptionInfoName_Type.__name__ = "DisplayString"
_RemoteAccessDescriptionInfoName_Object = MibTableColumn
remoteAccessDescriptionInfoName = _RemoteAccessDescriptionInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 8),
    _RemoteAccessDescriptionInfoName_Type()
)
remoteAccessDescriptionInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessDescriptionInfoName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessDescriptionInfoName.setDescription("""\
1700.0010.0001.0008 This attribute defines the description of the product
providing the Remote Access functionality.
""")


class _RemoteAccessVersionInfoName_Type(DisplayString):
    """Custom type remoteAccessVersionInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessVersionInfoName_Type.__name__ = "DisplayString"
_RemoteAccessVersionInfoName_Object = MibTableColumn
remoteAccessVersionInfoName = _RemoteAccessVersionInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 9),
    _RemoteAccessVersionInfoName_Type()
)
remoteAccessVersionInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessVersionInfoName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessVersionInfoName.setDescription("""\
1700.0010.0001.0009 This attribute defines the version of the product providing
the Remote Access functionality.
""")
_RemoteAccessControlCapabilities_Type = DellRemoteAccessControlCapabilities
_RemoteAccessControlCapabilities_Object = MibTableColumn
remoteAccessControlCapabilities = _RemoteAccessControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 10),
    _RemoteAccessControlCapabilities_Type()
)
remoteAccessControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessControlCapabilities.setDescription("""\
1700.0010.0001.0010 This attribute defines the control capabilities of the
Remote Access hardware.
""")
_RemoteAccessControlSettings_Type = DellRemoteAccessControlSettings
_RemoteAccessControlSettings_Object = MibTableColumn
remoteAccessControlSettings = _RemoteAccessControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 11),
    _RemoteAccessControlSettings_Type()
)
remoteAccessControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessControlSettings.setDescription("""\
1700.0010.0001.0011 This attribute defines the control settings of the Remote
Access hardware.
""")
_RemoteAccessMonitorCapabilities_Type = DellRemoteAccessMonitorCapabilities
_RemoteAccessMonitorCapabilities_Object = MibTableColumn
remoteAccessMonitorCapabilities = _RemoteAccessMonitorCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 12),
    _RemoteAccessMonitorCapabilities_Type()
)
remoteAccessMonitorCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessMonitorCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessMonitorCapabilities.setDescription("""\
1700.0010.0001.0012 This attribute defines the monitor capabilities of the
Remote Access hardware.
""")
_RemoteAccessMonitorSettings_Type = DellRemoteAccessMonitorSettings
_RemoteAccessMonitorSettings_Object = MibTableColumn
remoteAccessMonitorSettings = _RemoteAccessMonitorSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 13),
    _RemoteAccessMonitorSettings_Type()
)
remoteAccessMonitorSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessMonitorSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessMonitorSettings.setDescription("""\
1700.0010.0001.0013 This attribute defines the monitor settings of the Remote
Access hardware.
""")
_RemoteAccessLANCapabilities_Type = DellRemoteAccessLANCapabilities
_RemoteAccessLANCapabilities_Object = MibTableColumn
remoteAccessLANCapabilities = _RemoteAccessLANCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 14),
    _RemoteAccessLANCapabilities_Type()
)
remoteAccessLANCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessLANCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessLANCapabilities.setDescription("""\
1700.0010.0001.0014 This attribute defines the LAN capabilities of the Remote
Access hardware.
""")
_RemoteAccessLANSettings_Type = DellRemoteAccessLANSettings
_RemoteAccessLANSettings_Object = MibTableColumn
remoteAccessLANSettings = _RemoteAccessLANSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 15),
    _RemoteAccessLANSettings_Type()
)
remoteAccessLANSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessLANSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessLANSettings.setDescription("""\
1700.0010.0001.0015 This attribute defines the LAN settings of the Remote
Access hardware.
""")
_RemoteAccessHostCapabilities_Type = DellRemoteAccessHostCapabilities
_RemoteAccessHostCapabilities_Object = MibTableColumn
remoteAccessHostCapabilities = _RemoteAccessHostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 16),
    _RemoteAccessHostCapabilities_Type()
)
remoteAccessHostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessHostCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessHostCapabilities.setDescription("""\
1700.0010.0001.0016 This attribute defines the host capabilities of the Remote
Access hardware.
""")
_RemoteAccessHostSettings_Type = DellRemoteAccessHostSettings
_RemoteAccessHostSettings_Object = MibTableColumn
remoteAccessHostSettings = _RemoteAccessHostSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 17),
    _RemoteAccessHostSettings_Type()
)
remoteAccessHostSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessHostSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessHostSettings.setDescription("""\
1700.0010.0001.0017 This attribute defines the host settings of the Remote
Access hardware.
""")
_RemoteAccessOutOfBandSNMPCapabilities_Type = DellRemoteAccessOutOfBandSNMPCapabilities
_RemoteAccessOutOfBandSNMPCapabilities_Object = MibTableColumn
remoteAccessOutOfBandSNMPCapabilities = _RemoteAccessOutOfBandSNMPCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 18),
    _RemoteAccessOutOfBandSNMPCapabilities_Type()
)
remoteAccessOutOfBandSNMPCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessOutOfBandSNMPCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessOutOfBandSNMPCapabilities.setDescription("""\
1700.0010.0001.0018 This attribute defines the out-of-band SNMP capabilities of
the Remote Access hardware.
""")
_RemoteAccessOutOfBandSNMPSettings_Type = DellRemoteAccessOutOfBandSNMPSettings
_RemoteAccessOutOfBandSNMPSettings_Object = MibTableColumn
remoteAccessOutOfBandSNMPSettings = _RemoteAccessOutOfBandSNMPSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 19),
    _RemoteAccessOutOfBandSNMPSettings_Type()
)
remoteAccessOutOfBandSNMPSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessOutOfBandSNMPSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessOutOfBandSNMPSettings.setDescription("""\
1700.0010.0001.0019 This attribute defines the out-of-band SNMP settings of the
Remote Access hardware.
""")
_RemoteAccessSMTPServerIPAddress_Type = IpAddress
_RemoteAccessSMTPServerIPAddress_Object = MibTableColumn
remoteAccessSMTPServerIPAddress = _RemoteAccessSMTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 20),
    _RemoteAccessSMTPServerIPAddress_Type()
)
remoteAccessSMTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessSMTPServerIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessSMTPServerIPAddress.setDescription("""\
1700.0010.0001.0020 This attribute defines the IP address of the SMTP server
provided by the Remote Access hardware.
""")
_RemoteAccessFloppyTFTPIPAddress_Type = IpAddress
_RemoteAccessFloppyTFTPIPAddress_Object = MibTableColumn
remoteAccessFloppyTFTPIPAddress = _RemoteAccessFloppyTFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 21),
    _RemoteAccessFloppyTFTPIPAddress_Type()
)
remoteAccessFloppyTFTPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFloppyTFTPIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessFloppyTFTPIPAddress.setDescription("""\
1700.0010.0001.0021 This attribute defines the IP address of the TFTP server
providing the operating system image used by the Remote Access hardware.
""")


class _RemoteAccessFloppyTFTPPathName_Type(DisplayString):
    """Custom type remoteAccessFloppyTFTPPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteAccessFloppyTFTPPathName_Type.__name__ = "DisplayString"
_RemoteAccessFloppyTFTPPathName_Object = MibTableColumn
remoteAccessFloppyTFTPPathName = _RemoteAccessFloppyTFTPPathName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 22),
    _RemoteAccessFloppyTFTPPathName_Type()
)
remoteAccessFloppyTFTPPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFloppyTFTPPathName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessFloppyTFTPPathName.setDescription("""\
1700.0010.0001.0022 This attribute defines the file name of the the operating
system image obtained from the TFTP server used by the Remote Access hardware.
""")
_RemoteAccessFirmwareUpdateIPAddress_Type = IpAddress
_RemoteAccessFirmwareUpdateIPAddress_Object = MibTableColumn
remoteAccessFirmwareUpdateIPAddress = _RemoteAccessFirmwareUpdateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 23),
    _RemoteAccessFirmwareUpdateIPAddress_Type()
)
remoteAccessFirmwareUpdateIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFirmwareUpdateIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessFirmwareUpdateIPAddress.setDescription("""\
1700.0010.0001.0023 This attribute defines the IP address of the update server
providing the firmware image used by the Remote Access hardware.
""")


class _RemoteAccessFirmwareUpdatePathName_Type(DisplayString):
    """Custom type remoteAccessFirmwareUpdatePathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteAccessFirmwareUpdatePathName_Type.__name__ = "DisplayString"
_RemoteAccessFirmwareUpdatePathName_Object = MibTableColumn
remoteAccessFirmwareUpdatePathName = _RemoteAccessFirmwareUpdatePathName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 24),
    _RemoteAccessFirmwareUpdatePathName_Type()
)
remoteAccessFirmwareUpdatePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessFirmwareUpdatePathName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessFirmwareUpdatePathName.setDescription("""\
1700.0010.0001.0024 This attribute defines the file name of the the firmware
image obtained from the update server used by the Remote Access hardware.
""")
_RemoteAccessNICStaticIPAddress_Type = IpAddress
_RemoteAccessNICStaticIPAddress_Object = MibTableColumn
remoteAccessNICStaticIPAddress = _RemoteAccessNICStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 25),
    _RemoteAccessNICStaticIPAddress_Type()
)
remoteAccessNICStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessNICStaticIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICStaticIPAddress.setDescription("""\
1700.0010.0001.0025 This attribute defines the static IP address to be used by
the onboard NIC provided by the Remote Access hardware.
""")
_RemoteAccessNICStaticNetmaskAddress_Type = IpAddress
_RemoteAccessNICStaticNetmaskAddress_Object = MibTableColumn
remoteAccessNICStaticNetmaskAddress = _RemoteAccessNICStaticNetmaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 26),
    _RemoteAccessNICStaticNetmaskAddress_Type()
)
remoteAccessNICStaticNetmaskAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessNICStaticNetmaskAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICStaticNetmaskAddress.setDescription("""\
1700.0010.0001.0026 This attribute defines the netmask for the static IP
address to be used by the onboard NIC provided by the Remote Access hardware.
""")
_RemoteAccessNICStaticGatewayAddress_Type = IpAddress
_RemoteAccessNICStaticGatewayAddress_Object = MibTableColumn
remoteAccessNICStaticGatewayAddress = _RemoteAccessNICStaticGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 27),
    _RemoteAccessNICStaticGatewayAddress_Type()
)
remoteAccessNICStaticGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessNICStaticGatewayAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICStaticGatewayAddress.setDescription("""\
1700.0010.0001.0027 This attribute defines the IP address for the gateway
associated with the static IP address to be used by the onboard NIC provided by
the Remote Access hardware.
""")


class _RemoteAccessPCMCIAInfoName_Type(DisplayString):
    """Custom type remoteAccessPCMCIAInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessPCMCIAInfoName_Type.__name__ = "DisplayString"
_RemoteAccessPCMCIAInfoName_Object = MibTableColumn
remoteAccessPCMCIAInfoName = _RemoteAccessPCMCIAInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 28),
    _RemoteAccessPCMCIAInfoName_Type()
)
remoteAccessPCMCIAInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessPCMCIAInfoName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessPCMCIAInfoName.setDescription("""\
1700.0010.0001.0028 This attribute defines the information for the PCMCIA
device used by the Remote Access hardware.
""")


class _RemoteAccessMiscInfoName_Type(DisplayString):
    """Custom type remoteAccessMiscInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAccessMiscInfoName_Type.__name__ = "DisplayString"
_RemoteAccessMiscInfoName_Object = MibTableColumn
remoteAccessMiscInfoName = _RemoteAccessMiscInfoName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 29),
    _RemoteAccessMiscInfoName_Type()
)
remoteAccessMiscInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessMiscInfoName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessMiscInfoName.setDescription("""\
1700.0010.0001.0029 This attribute defines miscellaneous information for the
Remote Access hardware.
""")
_RemoteAccessNICCurrentIPAddress_Type = IpAddress
_RemoteAccessNICCurrentIPAddress_Object = MibTableColumn
remoteAccessNICCurrentIPAddress = _RemoteAccessNICCurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 30),
    _RemoteAccessNICCurrentIPAddress_Type()
)
remoteAccessNICCurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentIPAddress.setDescription("""\
1700.0010.0001.0030 This attribute defines the IP address currently being used
by the onboard NIC provided by the Remote Access hardware.
""")
_RemoteAccessNICCurrentNetmaskAddress_Type = IpAddress
_RemoteAccessNICCurrentNetmaskAddress_Object = MibTableColumn
remoteAccessNICCurrentNetmaskAddress = _RemoteAccessNICCurrentNetmaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 31),
    _RemoteAccessNICCurrentNetmaskAddress_Type()
)
remoteAccessNICCurrentNetmaskAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentNetmaskAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentNetmaskAddress.setDescription("""\
1700.0010.0001.0031 This attribute defines the netmask currently being used by
the onboard NIC provided by the Remote Access hardware.
""")
_RemoteAccessNICCurrentGatewayAddress_Type = IpAddress
_RemoteAccessNICCurrentGatewayAddress_Object = MibTableColumn
remoteAccessNICCurrentGatewayAddress = _RemoteAccessNICCurrentGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 32),
    _RemoteAccessNICCurrentGatewayAddress_Type()
)
remoteAccessNICCurrentGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentGatewayAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentGatewayAddress.setDescription("""\
1700.0010.0001.0032 This attribute defines the IP address for the gateway
currently being used by the onboard NIC provided by the Remote Access hardware.
""")
_RemoteAccessNICCurrentInfoFromDHCP_Type = DellBoolean
_RemoteAccessNICCurrentInfoFromDHCP_Object = MibTableColumn
remoteAccessNICCurrentInfoFromDHCP = _RemoteAccessNICCurrentInfoFromDHCP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 10, 1, 33),
    _RemoteAccessNICCurrentInfoFromDHCP_Type()
)
remoteAccessNICCurrentInfoFromDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentInfoFromDHCP.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteAccessNICCurrentInfoFromDHCP.setDescription("""\
1700.0010.0001.0033 This attribute defines if DHCP was used to obtain the NIC
information currently being used by the onboard NIC provided by the Remote
Access hardware.
""")
_RemoteUserAdminTable_Object = MibTable
remoteUserAdminTable = _RemoteUserAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20)
)
if mibBuilder.loadTexts:
    remoteUserAdminTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminTable.setDescription("""\
1700.0020 This object defines the Remote Access User Administration table.
""")
_RemoteUserAdminTableEntry_Object = MibTableRow
remoteUserAdminTableEntry = _RemoteUserAdminTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1)
)
remoteUserAdminTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteUserAdminChassisIndex"),
    (0, "MIB-Dell-10892", "remoteUserAdminAdapterIndex"),
    (0, "MIB-Dell-10892", "remoteUserAdminUserIndex"),
)
if mibBuilder.loadTexts:
    remoteUserAdminTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminTableEntry.setDescription("""\
1700.0020.0001 This object defines the Remote Access User Administration table
entry.
""")
_RemoteUserAdminChassisIndex_Type = DellObjectRange
_RemoteUserAdminChassisIndex_Object = MibTableColumn
remoteUserAdminChassisIndex = _RemoteUserAdminChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 1),
    _RemoteUserAdminChassisIndex_Type()
)
remoteUserAdminChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminChassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminChassisIndex.setDescription("""\
1700.0020.0001.0001 This attribute defines the index (one based) of the chassis
containing the Remote Access hardware.
""")
_RemoteUserAdminAdapterIndex_Type = DellObjectRange
_RemoteUserAdminAdapterIndex_Object = MibTableColumn
remoteUserAdminAdapterIndex = _RemoteUserAdminAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 2),
    _RemoteUserAdminAdapterIndex_Type()
)
remoteUserAdminAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminAdapterIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminAdapterIndex.setDescription("""\
1700.0020.0001.0002 This attribute defines the index (one based) of the Remote
Access hardware used by this Remote Access user.
""")
_RemoteUserAdminUserIndex_Type = DellObjectRange
_RemoteUserAdminUserIndex_Object = MibTableColumn
remoteUserAdminUserIndex = _RemoteUserAdminUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 3),
    _RemoteUserAdminUserIndex_Type()
)
remoteUserAdminUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminUserIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminUserIndex.setDescription("""\
1700.0020.0001.0003 This attribute defines the index (one based) of this Remote
Access user.
""")
_RemoteUserAdminStateCapabilities_Type = DellRemoteUserAdminStateCapabilities
_RemoteUserAdminStateCapabilities_Object = MibTableColumn
remoteUserAdminStateCapabilities = _RemoteUserAdminStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 4),
    _RemoteUserAdminStateCapabilities_Type()
)
remoteUserAdminStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminStateCapabilities.setDescription("""\
1700.0020.0001.0004 This attribute defines the state capabilities for this
Remote Access user.
""")
_RemoteUserAdminStateSettings_Type = DellRemoteUserAdminStateSettings
_RemoteUserAdminStateSettings_Object = MibTableColumn
remoteUserAdminStateSettings = _RemoteUserAdminStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 5),
    _RemoteUserAdminStateSettings_Type()
)
remoteUserAdminStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminStateSettings.setDescription("""\
1700.0020.0001.0005 This attribute defines the state settings for this Remote
Access user.
""")
_RemoteUserAdminStatus_Type = DellStatus
_RemoteUserAdminStatus_Object = MibTableColumn
remoteUserAdminStatus = _RemoteUserAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 6),
    _RemoteUserAdminStatus_Type()
)
remoteUserAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminStatus.setDescription("""\
1700.0020.0001.0006 This attribute defines the status for this Remote Access
user.
""")


class _RemoteUserAdminUserName_Type(DisplayString):
    """Custom type remoteUserAdminUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RemoteUserAdminUserName_Type.__name__ = "DisplayString"
_RemoteUserAdminUserName_Object = MibTableColumn
remoteUserAdminUserName = _RemoteUserAdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 7),
    _RemoteUserAdminUserName_Type()
)
remoteUserAdminUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminUserName.setDescription("""\
1700.0020.0001.0007 This attribute defines the name for this Remote Access
user.
""")


class _RemoteUserAdminUserPasswordName_Type(DisplayString):
    """Custom type remoteUserAdminUserPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteUserAdminUserPasswordName_Type.__name__ = "DisplayString"
_RemoteUserAdminUserPasswordName_Object = MibTableColumn
remoteUserAdminUserPasswordName = _RemoteUserAdminUserPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 8),
    _RemoteUserAdminUserPasswordName_Type()
)
remoteUserAdminUserPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserPasswordName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminUserPasswordName.setDescription("""\
1700.0020.0001.0008 This attribute defines the password for this Remote Access
user.
""")


class _RemoteUserAdminUserPrivilege_Type(DisplayString):
    """Custom type remoteUserAdminUserPrivilege based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminUserPrivilege_Type.__name__ = "DisplayString"
_RemoteUserAdminUserPrivilege_Object = MibTableColumn
remoteUserAdminUserPrivilege = _RemoteUserAdminUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 9),
    _RemoteUserAdminUserPrivilege_Type()
)
remoteUserAdminUserPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserPrivilege.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminUserPrivilege.setDescription("""\
1700.0020.0001.0009 This attribute defines the privileges for this Remote
Access user.
""")


class _RemoteUserAdminUserPrivilegeCapabilities_Type(DisplayString):
    """Custom type remoteUserAdminUserPrivilegeCapabilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminUserPrivilegeCapabilities_Type.__name__ = "DisplayString"
_RemoteUserAdminUserPrivilegeCapabilities_Object = MibTableColumn
remoteUserAdminUserPrivilegeCapabilities = _RemoteUserAdminUserPrivilegeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 10),
    _RemoteUserAdminUserPrivilegeCapabilities_Type()
)
remoteUserAdminUserPrivilegeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminUserPrivilegeCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminUserPrivilegeCapabilities.setDescription("""\
1700.0020.0001.0010 This attribute defines the privilege capabilities for this
Remote Access user.
""")
_RemoteUserAdminAlertFilterDrsEventsMask_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterDrsEventsMask_Object = MibTableColumn
remoteUserAdminAlertFilterDrsEventsMask = _RemoteUserAdminAlertFilterDrsEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 11),
    _RemoteUserAdminAlertFilterDrsEventsMask_Type()
)
remoteUserAdminAlertFilterDrsEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterDrsEventsMask.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterDrsEventsMask.setDescription("""\
1700.0020.0001.0011 This attribute defines the DRS events filter mask for this
Remote Access user.
""")
_RemoteUserAdminAlertFilterSysEventsMask_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterSysEventsMask_Object = MibTableColumn
remoteUserAdminAlertFilterSysEventsMask = _RemoteUserAdminAlertFilterSysEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 12),
    _RemoteUserAdminAlertFilterSysEventsMask_Type()
)
remoteUserAdminAlertFilterSysEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterSysEventsMask.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterSysEventsMask.setDescription("""\
1700.0020.0001.0012 This attribute defines the system events filter mask for
this Remote Access user.
""")
_RemoteUserAdminAlertFilterDrsCapabilities_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterDrsCapabilities_Object = MibTableColumn
remoteUserAdminAlertFilterDrsCapabilities = _RemoteUserAdminAlertFilterDrsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 13),
    _RemoteUserAdminAlertFilterDrsCapabilities_Type()
)
remoteUserAdminAlertFilterDrsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterDrsCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterDrsCapabilities.setDescription("""\
1700.0020.0001.0013 This attribute defines the DRS events filter capabilities
for this Remote Access user.
""")
_RemoteUserAdminAlertFilterSysCapabilities_Type = DellUnsigned32BitRange
_RemoteUserAdminAlertFilterSysCapabilities_Object = MibTableColumn
remoteUserAdminAlertFilterSysCapabilities = _RemoteUserAdminAlertFilterSysCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 14),
    _RemoteUserAdminAlertFilterSysCapabilities_Type()
)
remoteUserAdminAlertFilterSysCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterSysCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminAlertFilterSysCapabilities.setDescription("""\
1700.0020.0001.0014 This attribute defines the system events filter
capabilities for this Remote Access user.
""")


class _RemoteUserAdminPagerNumericNumberName_Type(DisplayString):
    """Custom type remoteUserAdminPagerNumericNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteUserAdminPagerNumericNumberName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerNumericNumberName_Object = MibTableColumn
remoteUserAdminPagerNumericNumberName = _RemoteUserAdminPagerNumericNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 15),
    _RemoteUserAdminPagerNumericNumberName_Type()
)
remoteUserAdminPagerNumericNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericNumberName.setDescription("""\
1700.0020.0001.0015 This attribute defines the numeric pager number for this
for this Remote Access user.
""")


class _RemoteUserAdminPagerNumericMessageName_Type(DisplayString):
    """Custom type remoteUserAdminPagerNumericMessageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerNumericMessageName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerNumericMessageName_Object = MibTableColumn
remoteUserAdminPagerNumericMessageName = _RemoteUserAdminPagerNumericMessageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 16),
    _RemoteUserAdminPagerNumericMessageName_Type()
)
remoteUserAdminPagerNumericMessageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericMessageName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericMessageName.setDescription("""\
1700.0020.0001.0016 This attribute defines the message to send to the numeric
pager for this Remote Access user.
""")
_RemoteUserAdminPagerNumericHangupDelay_Type = DellUnsigned32BitRange
_RemoteUserAdminPagerNumericHangupDelay_Object = MibTableColumn
remoteUserAdminPagerNumericHangupDelay = _RemoteUserAdminPagerNumericHangupDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 17),
    _RemoteUserAdminPagerNumericHangupDelay_Type()
)
remoteUserAdminPagerNumericHangupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericHangupDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerNumericHangupDelay.setDescription("""\
1700.0020.0001.0017 This attribute defines the numeric pager hangup delay for
this Remote Access user.
""")


class _RemoteUserAdminPagerAlphaPhoneNumberName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaPhoneNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteUserAdminPagerAlphaPhoneNumberName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaPhoneNumberName_Object = MibTableColumn
remoteUserAdminPagerAlphaPhoneNumberName = _RemoteUserAdminPagerAlphaPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 18),
    _RemoteUserAdminPagerAlphaPhoneNumberName_Type()
)
remoteUserAdminPagerAlphaPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPhoneNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPhoneNumberName.setDescription("""\
1700.0020.0001.0018 This attribute defines the alphanumeric pager phone number
for this Remote Access user.
""")
_RemoteUserAdminPagerAlphaProtocol_Type = DellRemoteUserAdminAlphaProtocolType
_RemoteUserAdminPagerAlphaProtocol_Object = MibTableColumn
remoteUserAdminPagerAlphaProtocol = _RemoteUserAdminPagerAlphaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 19),
    _RemoteUserAdminPagerAlphaProtocol_Type()
)
remoteUserAdminPagerAlphaProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaProtocol.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaProtocol.setDescription("""\
1700.0020.0001.0019 This attribute defines the protocol used by the
alphanumeric pager provider for this Remote Access user.
""")
_RemoteUserAdminPagerAlphaBaudRate_Type = DellRemoteUserAdminAlphaBaudType
_RemoteUserAdminPagerAlphaBaudRate_Object = MibTableColumn
remoteUserAdminPagerAlphaBaudRate = _RemoteUserAdminPagerAlphaBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 20),
    _RemoteUserAdminPagerAlphaBaudRate_Type()
)
remoteUserAdminPagerAlphaBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaBaudRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaBaudRate.setDescription("""\
1700.0020.0001.0020 This attribute defines the baud rate used by the
alphanumeric pager provider for this Remote Access user.
""")


class _RemoteUserAdminPagerAlphaCustomMessageName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaCustomMessageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerAlphaCustomMessageName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaCustomMessageName_Object = MibTableColumn
remoteUserAdminPagerAlphaCustomMessageName = _RemoteUserAdminPagerAlphaCustomMessageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 21),
    _RemoteUserAdminPagerAlphaCustomMessageName_Type()
)
remoteUserAdminPagerAlphaCustomMessageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaCustomMessageName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaCustomMessageName.setDescription("""\
1700.0020.0001.0021 This attribute defines the message to be sent to the
alphanumeric pager to inform the user of a call by this Remote Access user.
""")
_RemoteUserAdminPagerAlphaModemConnectTimeout_Type = DellUnsigned32BitRange
_RemoteUserAdminPagerAlphaModemConnectTimeout_Object = MibTableColumn
remoteUserAdminPagerAlphaModemConnectTimeout = _RemoteUserAdminPagerAlphaModemConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 22),
    _RemoteUserAdminPagerAlphaModemConnectTimeout_Type()
)
remoteUserAdminPagerAlphaModemConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaModemConnectTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaModemConnectTimeout.setDescription("""\
1700.0020.0001.0022 This attribute defines the modem connection timeout for the
alhpanumeric pager for this Remote Access user.
""")


class _RemoteUserAdminPagerAlphaPagerIdName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaPagerIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerAlphaPagerIdName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaPagerIdName_Object = MibTableColumn
remoteUserAdminPagerAlphaPagerIdName = _RemoteUserAdminPagerAlphaPagerIdName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 23),
    _RemoteUserAdminPagerAlphaPagerIdName_Type()
)
remoteUserAdminPagerAlphaPagerIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPagerIdName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPagerIdName.setDescription("""\
1700.0020.0001.0023 This attribute defines the ID to be sent to the
alphanumeric pager to inform the user of a call by this Remote Access user.
""")


class _RemoteUserAdminPagerAlphaPasswordName_Type(DisplayString):
    """Custom type remoteUserAdminPagerAlphaPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerAlphaPasswordName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerAlphaPasswordName_Object = MibTableColumn
remoteUserAdminPagerAlphaPasswordName = _RemoteUserAdminPagerAlphaPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 24),
    _RemoteUserAdminPagerAlphaPasswordName_Type()
)
remoteUserAdminPagerAlphaPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPasswordName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerAlphaPasswordName.setDescription("""\
1700.0020.0001.0024 This attribute defines the password for the alphanumeric
pager for this Remote Access user.
""")


class _RemoteUserAdminPagerModemInitStringName_Type(DisplayString):
    """Custom type remoteUserAdminPagerModemInitStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminPagerModemInitStringName_Type.__name__ = "DisplayString"
_RemoteUserAdminPagerModemInitStringName_Object = MibTableColumn
remoteUserAdminPagerModemInitStringName = _RemoteUserAdminPagerModemInitStringName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 25),
    _RemoteUserAdminPagerModemInitStringName_Type()
)
remoteUserAdminPagerModemInitStringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerModemInitStringName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerModemInitStringName.setDescription("""\
1700.0020.0001.0025 This attribute defines the initialization string to be sent
to the pager modem for this Remote Access user.
""")
_RemoteUserAdminPagerModemPort_Type = DellUnsigned32BitRange
_RemoteUserAdminPagerModemPort_Object = MibTableColumn
remoteUserAdminPagerModemPort = _RemoteUserAdminPagerModemPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 26),
    _RemoteUserAdminPagerModemPort_Type()
)
remoteUserAdminPagerModemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminPagerModemPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminPagerModemPort.setDescription("""\
1700.0020.0001.0026 This attribute defines the port for the pager modem for
this Remote Access user.
""")


class _RemoteUserAdminEmailAddressName_Type(DisplayString):
    """Custom type remoteUserAdminEmailAddressName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteUserAdminEmailAddressName_Type.__name__ = "DisplayString"
_RemoteUserAdminEmailAddressName_Object = MibTableColumn
remoteUserAdminEmailAddressName = _RemoteUserAdminEmailAddressName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 27),
    _RemoteUserAdminEmailAddressName_Type()
)
remoteUserAdminEmailAddressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminEmailAddressName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminEmailAddressName.setDescription("""\
1700.0020.0001.0027 This attribute defines the email address for this Remote
Access user.
""")


class _RemoteUserAdminEmailCustomMessageName_Type(DisplayString):
    """Custom type remoteUserAdminEmailCustomMessageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteUserAdminEmailCustomMessageName_Type.__name__ = "DisplayString"
_RemoteUserAdminEmailCustomMessageName_Object = MibTableColumn
remoteUserAdminEmailCustomMessageName = _RemoteUserAdminEmailCustomMessageName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 28),
    _RemoteUserAdminEmailCustomMessageName_Type()
)
remoteUserAdminEmailCustomMessageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminEmailCustomMessageName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminEmailCustomMessageName.setDescription("""\
1700.0020.0001.0028 This attribute defines the email message to send to this
Remote Access user.
""")
_RemoteUserAdminControlCapabilities_Type = DellRemoteUserAdminControlCapabilities
_RemoteUserAdminControlCapabilities_Object = MibTableColumn
remoteUserAdminControlCapabilities = _RemoteUserAdminControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 29),
    _RemoteUserAdminControlCapabilities_Type()
)
remoteUserAdminControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserAdminControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminControlCapabilities.setDescription("""\
1700.0020.0001.0029 This attribute defines the control capabilities for this
Remote Access user.
""")
_RemoteUserAdminControlSettings_Type = DellRemoteUserAdminControlSettings
_RemoteUserAdminControlSettings_Object = MibTableColumn
remoteUserAdminControlSettings = _RemoteUserAdminControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 30),
    _RemoteUserAdminControlSettings_Type()
)
remoteUserAdminControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminControlSettings.setDescription("""\
1700.0020.0001.0030 This attribute defines the control settings for this Remote
Access user.
""")
_RemoteUserAdminUserType_Type = DellUnsigned8BitRange
_RemoteUserAdminUserType_Object = MibTableColumn
remoteUserAdminUserType = _RemoteUserAdminUserType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 20, 1, 31),
    _RemoteUserAdminUserType_Type()
)
remoteUserAdminUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserAdminUserType.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserAdminUserType.setDescription("""\
1700.0020.0001.0031 This attribute defines the type of this Remote Access user.
""")
_RemoteSNMPTrapTable_Object = MibTable
remoteSNMPTrapTable = _RemoteSNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30)
)
if mibBuilder.loadTexts:
    remoteSNMPTrapTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapTable.setDescription("""\
1700.0030 This object defines the Remote Access SNMP Trap Destination table.
""")
_RemoteSNMPTrapTableEntry_Object = MibTableRow
remoteSNMPTrapTableEntry = _RemoteSNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1)
)
remoteSNMPTrapTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteSNMPTrapChassisIndex"),
    (0, "MIB-Dell-10892", "remoteSNMPTrapAdapterIndex"),
    (0, "MIB-Dell-10892", "remoteSNMPTrapIndex"),
)
if mibBuilder.loadTexts:
    remoteSNMPTrapTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapTableEntry.setDescription("""\
1700.0030.0001 This object defines the Remote Access SNMP Trap Destination
table entry.
""")
_RemoteSNMPTrapChassisIndex_Type = DellObjectRange
_RemoteSNMPTrapChassisIndex_Object = MibTableColumn
remoteSNMPTrapChassisIndex = _RemoteSNMPTrapChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 1),
    _RemoteSNMPTrapChassisIndex_Type()
)
remoteSNMPTrapChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapChassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapChassisIndex.setDescription("""\
1700.0030.0001.0001 This attribute defines the index (one based) of the chassis
containing the Remote Access hardware.
""")
_RemoteSNMPTrapAdapterIndex_Type = DellObjectRange
_RemoteSNMPTrapAdapterIndex_Object = MibTableColumn
remoteSNMPTrapAdapterIndex = _RemoteSNMPTrapAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 2),
    _RemoteSNMPTrapAdapterIndex_Type()
)
remoteSNMPTrapAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapAdapterIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapAdapterIndex.setDescription("""\
1700.0030.0001.0002 This attribute defines the index (one based) of the Remote
Access hardware that uses this SNMP trap destination.
""")
_RemoteSNMPTrapIndex_Type = DellObjectRange
_RemoteSNMPTrapIndex_Object = MibTableColumn
remoteSNMPTrapIndex = _RemoteSNMPTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 3),
    _RemoteSNMPTrapIndex_Type()
)
remoteSNMPTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapIndex.setDescription("""\
1700.0030.0001.0003 This attribute defines the index (one based) of this Remote
Access SNMP trap destination.
""")
_RemoteSNMPTrapStateCapabilities_Type = DellRemoteSNMPTrapStateCapabilities
_RemoteSNMPTrapStateCapabilities_Object = MibTableColumn
remoteSNMPTrapStateCapabilities = _RemoteSNMPTrapStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 4),
    _RemoteSNMPTrapStateCapabilities_Type()
)
remoteSNMPTrapStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapStateCapabilities.setDescription("""\
1700.0030.0001.0004 This attribute defines the state capabilities of this
Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapStateSettings_Type = DellRemoteSNMPTrapStateSettings
_RemoteSNMPTrapStateSettings_Object = MibTableColumn
remoteSNMPTrapStateSettings = _RemoteSNMPTrapStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 5),
    _RemoteSNMPTrapStateSettings_Type()
)
remoteSNMPTrapStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapStateSettings.setDescription("""\
1700.0030.0001.0005 This attribute defines the state settings of this Remote
Access SNMP trap destination.
""")
_RemoteSNMPTrapStatus_Type = DellStatus
_RemoteSNMPTrapStatus_Object = MibTableColumn
remoteSNMPTrapStatus = _RemoteSNMPTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 6),
    _RemoteSNMPTrapStatus_Type()
)
remoteSNMPTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapStatus.setDescription("""\
1700.0030.0001.0006 This attribute defines the status of this Remote Access
SNMP trap destination.
""")
_RemoteSNMPTrapDestinationIPAddress_Type = IpAddress
_RemoteSNMPTrapDestinationIPAddress_Object = MibTableColumn
remoteSNMPTrapDestinationIPAddress = _RemoteSNMPTrapDestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 7),
    _RemoteSNMPTrapDestinationIPAddress_Type()
)
remoteSNMPTrapDestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapDestinationIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapDestinationIPAddress.setDescription("""\
1700.0030.0001.0007 This attribute defines the IP address of this Remote Access
SNMP trap destination.
""")


class _RemoteSNMPTrapSNMPCommunityName_Type(DisplayString):
    """Custom type remoteSNMPTrapSNMPCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteSNMPTrapSNMPCommunityName_Type.__name__ = "DisplayString"
_RemoteSNMPTrapSNMPCommunityName_Object = MibTableColumn
remoteSNMPTrapSNMPCommunityName = _RemoteSNMPTrapSNMPCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 8),
    _RemoteSNMPTrapSNMPCommunityName_Type()
)
remoteSNMPTrapSNMPCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapSNMPCommunityName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapSNMPCommunityName.setDescription("""\
1700.0030.0001.0008 This attribute defines the community for traps sent to this
Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapFilterDrsEventsMask_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterDrsEventsMask_Object = MibTableColumn
remoteSNMPTrapFilterDrsEventsMask = _RemoteSNMPTrapFilterDrsEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 9),
    _RemoteSNMPTrapFilterDrsEventsMask_Type()
)
remoteSNMPTrapFilterDrsEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterDrsEventsMask.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterDrsEventsMask.setDescription("""\
1700.0030.0001.0009 This attribute defines the DRS events filter mask for this
Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapFilterSysEventsMask_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterSysEventsMask_Object = MibTableColumn
remoteSNMPTrapFilterSysEventsMask = _RemoteSNMPTrapFilterSysEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 10),
    _RemoteSNMPTrapFilterSysEventsMask_Type()
)
remoteSNMPTrapFilterSysEventsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterSysEventsMask.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterSysEventsMask.setDescription("""\
1700.0030.0001.0010 This attribute defines the system events filter mask for
this Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapFilterDrsCapabilities_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterDrsCapabilities_Object = MibTableColumn
remoteSNMPTrapFilterDrsCapabilities = _RemoteSNMPTrapFilterDrsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 11),
    _RemoteSNMPTrapFilterDrsCapabilities_Type()
)
remoteSNMPTrapFilterDrsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterDrsCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterDrsCapabilities.setDescription("""\
1700.0030.0001.0011 This attribute defines the DRS events filter capabilities
for this Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapFilterSysCapabilities_Type = DellUnsigned32BitRange
_RemoteSNMPTrapFilterSysCapabilities_Object = MibTableColumn
remoteSNMPTrapFilterSysCapabilities = _RemoteSNMPTrapFilterSysCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 12),
    _RemoteSNMPTrapFilterSysCapabilities_Type()
)
remoteSNMPTrapFilterSysCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterSysCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapFilterSysCapabilities.setDescription("""\
1700.0030.0001.0012 This attribute defines the system events filter
capabilities for this Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapControlCapabilities_Type = DellRemoteSNMPTrapControlCapabilities
_RemoteSNMPTrapControlCapabilities_Object = MibTableColumn
remoteSNMPTrapControlCapabilities = _RemoteSNMPTrapControlCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 13),
    _RemoteSNMPTrapControlCapabilities_Type()
)
remoteSNMPTrapControlCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSNMPTrapControlCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapControlCapabilities.setDescription("""\
1700.0030.0001.0013 This attribute defines the control capabilities of this
Remote Access SNMP trap destination.
""")
_RemoteSNMPTrapControlSettings_Type = DellRemoteSNMPTrapControlSettings
_RemoteSNMPTrapControlSettings_Object = MibTableColumn
remoteSNMPTrapControlSettings = _RemoteSNMPTrapControlSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 30, 1, 14),
    _RemoteSNMPTrapControlSettings_Type()
)
remoteSNMPTrapControlSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNMPTrapControlSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteSNMPTrapControlSettings.setDescription("""\
1700.0030.0001.0014 This attribute defines the control settings of this Remote
Access SNMP trap destination.
""")
_RemoteDialUpTable_Object = MibTable
remoteDialUpTable = _RemoteDialUpTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40)
)
if mibBuilder.loadTexts:
    remoteDialUpTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpTable.setDescription("""\
1700.0040 This object defines the Remote Access Dial Up table.
""")
_RemoteDialUpTableEntry_Object = MibTableRow
remoteDialUpTableEntry = _RemoteDialUpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1)
)
remoteDialUpTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteDialUpChassisIndex"),
    (0, "MIB-Dell-10892", "remoteDialUpAdapterIndex"),
    (0, "MIB-Dell-10892", "remoteDialUpIndex"),
)
if mibBuilder.loadTexts:
    remoteDialUpTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpTableEntry.setDescription("""\
1700.0040.0001 This object defines the Remote Access Dial Up table entry.
""")
_RemoteDialUpChassisIndex_Type = DellObjectRange
_RemoteDialUpChassisIndex_Object = MibTableColumn
remoteDialUpChassisIndex = _RemoteDialUpChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 1),
    _RemoteDialUpChassisIndex_Type()
)
remoteDialUpChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpChassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpChassisIndex.setDescription("""\
1700.0040.0001.0001 This attribute defines the index (one based) of the chassis
containing the Remote Access hardware.
""")
_RemoteDialUpAdapterIndex_Type = DellObjectRange
_RemoteDialUpAdapterIndex_Object = MibTableColumn
remoteDialUpAdapterIndex = _RemoteDialUpAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 2),
    _RemoteDialUpAdapterIndex_Type()
)
remoteDialUpAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpAdapterIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpAdapterIndex.setDescription("""\
1700.0040.0001.0002 This attribute defines the index (one based) of the Remote
Access hardware that supports this Remote Access Dial Up functionality.
""")
_RemoteDialUpIndex_Type = DellObjectRange
_RemoteDialUpIndex_Object = MibTableColumn
remoteDialUpIndex = _RemoteDialUpIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 3),
    _RemoteDialUpIndex_Type()
)
remoteDialUpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpIndex.setDescription("""\
1700.0040.0001.0003 This attribute defines the index (one based) of this Remote
Access Dial Up functionality.
""")
_RemoteDialUpStateCapabilities_Type = DellRemoteDialUpStateCapabilities
_RemoteDialUpStateCapabilities_Object = MibTableColumn
remoteDialUpStateCapabilities = _RemoteDialUpStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 4),
    _RemoteDialUpStateCapabilities_Type()
)
remoteDialUpStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpStateCapabilities.setDescription("""\
1700.0040.0001.0004 This attribute defines the state capabilities of this
Remote Access Dial Up functionality.
""")
_RemoteDialUpStateSettings_Type = DellRemoteDialUpStateSettings
_RemoteDialUpStateSettings_Object = MibTableColumn
remoteDialUpStateSettings = _RemoteDialUpStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 5),
    _RemoteDialUpStateSettings_Type()
)
remoteDialUpStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpStateSettings.setDescription("""\
1700.0040.0001.0005 This attribute defines the state settings of this Remote
Access Dial Up functionality.
""")
_RemoteDialUpStatus_Type = DellStatus
_RemoteDialUpStatus_Object = MibTableColumn
remoteDialUpStatus = _RemoteDialUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 6),
    _RemoteDialUpStatus_Type()
)
remoteDialUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialUpStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpStatus.setDescription("""\
1700.0040.0001.0006 This attribute defines the status of this Remote Access
Dial Up functionality.
""")
_RemoteDialUpPPPDialInBaseIPAddress_Type = IpAddress
_RemoteDialUpPPPDialInBaseIPAddress_Object = MibTableColumn
remoteDialUpPPPDialInBaseIPAddress = _RemoteDialUpPPPDialInBaseIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 7),
    _RemoteDialUpPPPDialInBaseIPAddress_Type()
)
remoteDialUpPPPDialInBaseIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInBaseIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInBaseIPAddress.setDescription("""\
1700.0040.0001.0007 This attribute defines the base IP address of the PPP
server for this Remote Access Dial Up functionality.
""")
_RemoteDialUpPPPDialInIdleTimeout_Type = DellUnsigned32BitRange
_RemoteDialUpPPPDialInIdleTimeout_Object = MibTableColumn
remoteDialUpPPPDialInIdleTimeout = _RemoteDialUpPPPDialInIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 8),
    _RemoteDialUpPPPDialInIdleTimeout_Type()
)
remoteDialUpPPPDialInIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInIdleTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInIdleTimeout.setDescription("""\
1700.0040.0001.0008 This attribute defines the PPP idle timeout value in
seconds for this Remote Access Dial Up functionality.
""")
_RemoteDialUpPPPDialInMaxConnectTimeout_Type = DellUnsigned32BitRange
_RemoteDialUpPPPDialInMaxConnectTimeout_Object = MibTableColumn
remoteDialUpPPPDialInMaxConnectTimeout = _RemoteDialUpPPPDialInMaxConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 9),
    _RemoteDialUpPPPDialInMaxConnectTimeout_Type()
)
remoteDialUpPPPDialInMaxConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInMaxConnectTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpPPPDialInMaxConnectTimeout.setDescription("""\
1700.0040.0001.0009 This attribute defines the PPP connect timeout value in
seconds for this Remote Access Dial Up functionality.
""")
_RemoteDialUpDialOutModemConnectTimeout_Type = DellUnsigned32BitRange
_RemoteDialUpDialOutModemConnectTimeout_Object = MibTableColumn
remoteDialUpDialOutModemConnectTimeout = _RemoteDialUpDialOutModemConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 10),
    _RemoteDialUpDialOutModemConnectTimeout_Type()
)
remoteDialUpDialOutModemConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpDialOutModemConnectTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpDialOutModemConnectTimeout.setDescription("""\
1700.0040.0001.0010 This attribute defines the modem dial out connect timeout
value in seconds for this Remote Access Dial Up functionality.
""")
_RemoteDialUpModemDialType_Type = DellRemoteDialUpModemDialType
_RemoteDialUpModemDialType_Object = MibTableColumn
remoteDialUpModemDialType = _RemoteDialUpModemDialType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 11),
    _RemoteDialUpModemDialType_Type()
)
remoteDialUpModemDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemDialType.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpModemDialType.setDescription("""\
1700.0040.0001.0011 This attribute defines the dial type for the modem used by
this Remote Access Dial Up functionality.
""")


class _RemoteDialUpModemInitStringName_Type(DisplayString):
    """Custom type remoteDialUpModemInitStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteDialUpModemInitStringName_Type.__name__ = "DisplayString"
_RemoteDialUpModemInitStringName_Object = MibTableColumn
remoteDialUpModemInitStringName = _RemoteDialUpModemInitStringName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 12),
    _RemoteDialUpModemInitStringName_Type()
)
remoteDialUpModemInitStringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemInitStringName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpModemInitStringName.setDescription("""\
1700.0040.0001.0012 This attribute defines the initialization string to be sent
to the modem for this Remote Access Dial Up functionality.
""")
_RemoteDialUpModemBaudRate_Type = DellUnsigned32BitRange
_RemoteDialUpModemBaudRate_Object = MibTableColumn
remoteDialUpModemBaudRate = _RemoteDialUpModemBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 13),
    _RemoteDialUpModemBaudRate_Type()
)
remoteDialUpModemBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemBaudRate.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpModemBaudRate.setDescription("""\
1700.0040.0001.0013 This attribute defines the baud rate for the modem used by
this Remote Access Dial Up functionality.
""")
_RemoteDialUpModemPort_Type = DellUnsigned32BitRange
_RemoteDialUpModemPort_Object = MibTableColumn
remoteDialUpModemPort = _RemoteDialUpModemPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 40, 1, 14),
    _RemoteDialUpModemPort_Type()
)
remoteDialUpModemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialUpModemPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialUpModemPort.setDescription("""\
1700.0040.0001.0014 This attribute defines the port for the modem used by this
Remote Access Dial Up functionality.
""")
_RemoteUserDialInCfgTable_Object = MibTable
remoteUserDialInCfgTable = _RemoteUserDialInCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50)
)
if mibBuilder.loadTexts:
    remoteUserDialInCfgTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgTable.setDescription("""\
1700.0050 This object defines the Remote Access User Dial In Configuration
table.
""")
_RemoteUserDialInCfgTableEntry_Object = MibTableRow
remoteUserDialInCfgTableEntry = _RemoteUserDialInCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1)
)
remoteUserDialInCfgTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteUserDialInCfgChassisIndex"),
    (0, "MIB-Dell-10892", "remoteUserDialInCfgAdapterIndex"),
    (0, "MIB-Dell-10892", "remoteUserDialInCfgUserIndex"),
)
if mibBuilder.loadTexts:
    remoteUserDialInCfgTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgTableEntry.setDescription("""\
1700.0050.0001 This object defines the Remote Access User Dial In Configuration
table entry.
""")
_RemoteUserDialInCfgChassisIndex_Type = DellObjectRange
_RemoteUserDialInCfgChassisIndex_Object = MibTableColumn
remoteUserDialInCfgChassisIndex = _RemoteUserDialInCfgChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 1),
    _RemoteUserDialInCfgChassisIndex_Type()
)
remoteUserDialInCfgChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgChassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgChassisIndex.setDescription("""\
1700.0050.0001.0001 This attribute defines the index (one based) of the chassis
containing the Remote Access hardware.
""")
_RemoteUserDialInCfgAdapterIndex_Type = DellObjectRange
_RemoteUserDialInCfgAdapterIndex_Object = MibTableColumn
remoteUserDialInCfgAdapterIndex = _RemoteUserDialInCfgAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 2),
    _RemoteUserDialInCfgAdapterIndex_Type()
)
remoteUserDialInCfgAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgAdapterIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgAdapterIndex.setDescription("""\
1700.0050.0001.0002 This attribute defines the index (one based) of Remote
Access hardware that supports this Remote Access Dial In user.
""")
_RemoteUserDialInCfgUserIndex_Type = DellObjectRange
_RemoteUserDialInCfgUserIndex_Object = MibTableColumn
remoteUserDialInCfgUserIndex = _RemoteUserDialInCfgUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 3),
    _RemoteUserDialInCfgUserIndex_Type()
)
remoteUserDialInCfgUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgUserIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgUserIndex.setDescription("""\
1700.0050.0001.0003 This attribute defines the index (one based) of this Remote
Access Dial In user.
""")
_RemoteUserDialInCfgStateCapabilities_Type = DellRemoteUserDialInStateCapabilities
_RemoteUserDialInCfgStateCapabilities_Object = MibTableColumn
remoteUserDialInCfgStateCapabilities = _RemoteUserDialInCfgStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 4),
    _RemoteUserDialInCfgStateCapabilities_Type()
)
remoteUserDialInCfgStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStateCapabilities.setDescription("""\
1700.0050.0001.0004 This attribute defines the state capabilities of this
Remote Access Dial In user.
""")
_RemoteUserDialInCfgStateSettings_Type = DellRemoteUserDialInStateSettings
_RemoteUserDialInCfgStateSettings_Object = MibTableColumn
remoteUserDialInCfgStateSettings = _RemoteUserDialInCfgStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 5),
    _RemoteUserDialInCfgStateSettings_Type()
)
remoteUserDialInCfgStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStateSettings.setDescription("""\
1700.0050.0001.0005 This attribute defines the state settings of this Remote
Access Dial In user.
""")
_RemoteUserDialInCfgStatus_Type = DellStatus
_RemoteUserDialInCfgStatus_Object = MibTableColumn
remoteUserDialInCfgStatus = _RemoteUserDialInCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 6),
    _RemoteUserDialInCfgStatus_Type()
)
remoteUserDialInCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgStatus.setDescription("""\
1700.0050.0001.0006 This attribute defines the status of this Remote Access
Dial In user.
""")


class _RemoteUserDialInCfgPPPUserName_Type(DisplayString):
    """Custom type remoteUserDialInCfgPPPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteUserDialInCfgPPPUserName_Type.__name__ = "DisplayString"
_RemoteUserDialInCfgPPPUserName_Object = MibTableColumn
remoteUserDialInCfgPPPUserName = _RemoteUserDialInCfgPPPUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 7),
    _RemoteUserDialInCfgPPPUserName_Type()
)
remoteUserDialInCfgPPPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgPPPUserName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgPPPUserName.setDescription("""\
1700.0050.0001.0007 This attribute defines the PPP user name of this Remote
Access Dial In user.
""")


class _RemoteUserDialInCfgPPPUserPasswordName_Type(DisplayString):
    """Custom type remoteUserDialInCfgPPPUserPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RemoteUserDialInCfgPPPUserPasswordName_Type.__name__ = "DisplayString"
_RemoteUserDialInCfgPPPUserPasswordName_Object = MibTableColumn
remoteUserDialInCfgPPPUserPasswordName = _RemoteUserDialInCfgPPPUserPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 8),
    _RemoteUserDialInCfgPPPUserPasswordName_Type()
)
remoteUserDialInCfgPPPUserPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgPPPUserPasswordName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgPPPUserPasswordName.setDescription("""\
1700.0050.0001.0008 This attribute defines the PPP password for this Remote
Access Dial In user.
""")


class _RemoteUserDialInCfgCallbackPhoneNumberName_Type(DisplayString):
    """Custom type remoteUserDialInCfgCallbackPhoneNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RemoteUserDialInCfgCallbackPhoneNumberName_Type.__name__ = "DisplayString"
_RemoteUserDialInCfgCallbackPhoneNumberName_Object = MibTableColumn
remoteUserDialInCfgCallbackPhoneNumberName = _RemoteUserDialInCfgCallbackPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 50, 1, 9),
    _RemoteUserDialInCfgCallbackPhoneNumberName_Type()
)
remoteUserDialInCfgCallbackPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDialInCfgCallbackPhoneNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteUserDialInCfgCallbackPhoneNumberName.setDescription("""\
1700.0050.0001.0009 This attribute defines the callback phone number for this
Remote Access Dial In user.
""")
_RemoteDialOutTable_Object = MibTable
remoteDialOutTable = _RemoteDialOutTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60)
)
if mibBuilder.loadTexts:
    remoteDialOutTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutTable.setDescription("""\
1700.0060 This object defines the Remote Access Dial Out table.
""")
_RemoteDialOutTableEntry_Object = MibTableRow
remoteDialOutTableEntry = _RemoteDialOutTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1)
)
remoteDialOutTableEntry.setIndexNames(
    (0, "MIB-Dell-10892", "remoteDialOutChassisIndex"),
    (0, "MIB-Dell-10892", "remoteDialOutAdapterIndex"),
    (0, "MIB-Dell-10892", "remoteDialOutDialOutIndex"),
)
if mibBuilder.loadTexts:
    remoteDialOutTableEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutTableEntry.setDescription("""\
1700.0060.0001 This object defines the Remote Access Dial Out table entry.
""")
_RemoteDialOutChassisIndex_Type = DellObjectRange
_RemoteDialOutChassisIndex_Object = MibTableColumn
remoteDialOutChassisIndex = _RemoteDialOutChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 1),
    _RemoteDialOutChassisIndex_Type()
)
remoteDialOutChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutChassisIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutChassisIndex.setDescription("""\
1700.0060.0001.0001 This attribute defines the index (one based) of the chassis
containing the Remote Access hardware.
""")
_RemoteDialOutAdapterIndex_Type = DellObjectRange
_RemoteDialOutAdapterIndex_Object = MibTableColumn
remoteDialOutAdapterIndex = _RemoteDialOutAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 2),
    _RemoteDialOutAdapterIndex_Type()
)
remoteDialOutAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutAdapterIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutAdapterIndex.setDescription("""\
1700.0060.0001.0002 This attribute defines the index (one based) of the Remote
Access hardware that supports this Remote Access Dial Out functionality.
""")
_RemoteDialOutDialOutIndex_Type = DellObjectRange
_RemoteDialOutDialOutIndex_Object = MibTableColumn
remoteDialOutDialOutIndex = _RemoteDialOutDialOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 3),
    _RemoteDialOutDialOutIndex_Type()
)
remoteDialOutDialOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutDialOutIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutDialOutIndex.setDescription("""\
1700.0060.0001.0003 This attribute defines the index (one based) of this Remote
Access Dial Out functionality.
""")
_RemoteDialOutStateCapabilities_Type = DellRemoteDialOutStateCapabilities
_RemoteDialOutStateCapabilities_Object = MibTableColumn
remoteDialOutStateCapabilities = _RemoteDialOutStateCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 4),
    _RemoteDialOutStateCapabilities_Type()
)
remoteDialOutStateCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutStateCapabilities.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutStateCapabilities.setDescription("""\
1700.0060.0001.0004 This attribute defines the state capabilities of this
Remote Access Dial Out functionality.
""")
_RemoteDialOutStateSettings_Type = DellRemoteDialOutStateSettings
_RemoteDialOutStateSettings_Object = MibTableColumn
remoteDialOutStateSettings = _RemoteDialOutStateSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 5),
    _RemoteDialOutStateSettings_Type()
)
remoteDialOutStateSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutStateSettings.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutStateSettings.setDescription("""\
1700.0060.0001.0005 This attribute defines the state settings of this Remote
Access Dial Out functionality.
""")
_RemoteDialOutStatus_Type = DellStatus
_RemoteDialOutStatus_Object = MibTableColumn
remoteDialOutStatus = _RemoteDialOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 6),
    _RemoteDialOutStatus_Type()
)
remoteDialOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDialOutStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutStatus.setDescription("""\
1700.0060.0001.0006 This attribute defines the status of this Remote Dial Out
functionality.
""")
_RemoteDialOutIPAddress_Type = IpAddress
_RemoteDialOutIPAddress_Object = MibTableColumn
remoteDialOutIPAddress = _RemoteDialOutIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 7),
    _RemoteDialOutIPAddress_Type()
)
remoteDialOutIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutIPAddress.setDescription("""\
1700.0060.0001.0007 This attribute defines the IP address for this Remote
Access Dial Out destination.
""")


class _RemoteDialOutPhoneNumberName_Type(DisplayString):
    """Custom type remoteDialOutPhoneNumberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_RemoteDialOutPhoneNumberName_Type.__name__ = "DisplayString"
_RemoteDialOutPhoneNumberName_Object = MibTableColumn
remoteDialOutPhoneNumberName = _RemoteDialOutPhoneNumberName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 8),
    _RemoteDialOutPhoneNumberName_Type()
)
remoteDialOutPhoneNumberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutPhoneNumberName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutPhoneNumberName.setDescription("""\
1700.0060.0001.0008 This attribute defines the phone number for this Remote
Access Dial Out destination.
""")


class _RemoteDialOutPPPUserName_Type(DisplayString):
    """Custom type remoteDialOutPPPUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteDialOutPPPUserName_Type.__name__ = "DisplayString"
_RemoteDialOutPPPUserName_Object = MibTableColumn
remoteDialOutPPPUserName = _RemoteDialOutPPPUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 9),
    _RemoteDialOutPPPUserName_Type()
)
remoteDialOutPPPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutPPPUserName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutPPPUserName.setDescription("""\
1700.0060.0001.0009 This attribute defines the PPP user name for this Remote
Access Dial Out destination.
""")


class _RemoteDialOutPPPPasswordName_Type(DisplayString):
    """Custom type remoteDialOutPPPPasswordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_RemoteDialOutPPPPasswordName_Type.__name__ = "DisplayString"
_RemoteDialOutPPPPasswordName_Object = MibTableColumn
remoteDialOutPPPPasswordName = _RemoteDialOutPPPPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 1700, 60, 1, 10),
    _RemoteDialOutPPPPasswordName_Type()
)
remoteDialOutPPPPasswordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDialOutPPPPasswordName.setStatus("mandatory")
if mibBuilder.loadTexts:
    remoteDialOutPPPPasswordName.setDescription("""\
1700.0060.0001.0010 This attribute defines the PPP password for this Remote
Access Dial Out destination.
""")
_AlertGroup_ObjectIdentity = ObjectIdentity
alertGroup = _AlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000)
)
_AlertVariables_ObjectIdentity = ObjectIdentity
alertVariables = _AlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10)
)


class _AlertSystem_Type(DisplayString):
    """Custom type alertSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlertSystem_Type.__name__ = "DisplayString"
_AlertSystem_Object = MibScalar
alertSystem = _AlertSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 1),
    _AlertSystem_Type()
)
alertSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSystem.setStatus("mandatory")
if mibBuilder.loadTexts:
    alertSystem.setDescription("""\
5000.0010.0001 Name of the system generating the alert.
""")
_AlertTableIndexOID_Type = ObjectIdentifier
_AlertTableIndexOID_Object = MibScalar
alertTableIndexOID = _AlertTableIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 2),
    _AlertTableIndexOID_Type()
)
alertTableIndexOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertTableIndexOID.setStatus("mandatory")
if mibBuilder.loadTexts:
    alertTableIndexOID.setDescription("""\
5000.0010.0002 OID for the index attribute in the table that contains the
object causing the alert. This value can be used to uniquely identify the
object causing the alert and to correlate different alerts caused by an object.
If not applicable, the value will be 0.0.
""")


class _AlertMessage_Type(DisplayString):
    """Custom type alertMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertMessage_Type.__name__ = "DisplayString"
_AlertMessage_Object = MibScalar
alertMessage = _AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 3),
    _AlertMessage_Type()
)
alertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMessage.setStatus("mandatory")
if mibBuilder.loadTexts:
    alertMessage.setDescription("""\
5000.0010.0003 Message describing the alert.
""")
_AlertCurrentStatus_Type = DellStatus
_AlertCurrentStatus_Object = MibScalar
alertCurrentStatus = _AlertCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 4),
    _AlertCurrentStatus_Type()
)
alertCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCurrentStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    alertCurrentStatus.setDescription("""\
5000.0010.0004 Current status of object causing the alert.
""")
_AlertPreviousStatus_Type = DellStatus
_AlertPreviousStatus_Object = MibScalar
alertPreviousStatus = _AlertPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 5),
    _AlertPreviousStatus_Type()
)
alertPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertPreviousStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    alertPreviousStatus.setDescription("""\
5000.0010.0005 Previous status of object causing the alert.
""")


class _AlertData_Type(OctetString):
    """Custom type alertData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AlertData_Type.__name__ = "OctetString"
_AlertData_Object = MibScalar
alertData = _AlertData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 5000, 10, 6),
    _AlertData_Type()
)
alertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertData.setStatus("mandatory")
if mibBuilder.loadTexts:
    alertData.setDescription("""\
5000.0010.0006 Alert data.
""")
_DrsOutOfBandGroup_ObjectIdentity = ObjectIdentity
drsOutOfBandGroup = _DrsOutOfBandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2)
)

# Managed Objects groups


# Notification objects

alertSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1001)
)
alertSystemUp.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertSystemUp.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertSystemUp.setDescription("""\
Dell system has started.
""")

alertThermalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1004)
)
alertThermalShutdown.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertThermalShutdown.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertThermalShutdown.setDescription("""\
Thermal shutdown protection has been initiated.
""")

alertTemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1052)
)
alertTemperatureProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertTemperatureProbeNormal.setDescription("""\
Temperature probe has returned to a normal value.
""")

alertTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1053)
)
alertTemperatureProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeWarning.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertTemperatureProbeWarning.setDescription("""\
Temperature probe has detected a warning value.
""")

alertTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1054)
)
alertTemperatureProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertTemperatureProbeFailure.setDescription("""\
Temperature probe has detected a failure value.
""")

alertTemperatureProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1055)
)
alertTemperatureProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertTemperatureProbeNonRecoverable.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertTemperatureProbeNonRecoverable.setDescription("""\
Temperature probe has detected a non-recoverable value.
""")

alertCoolingDeviceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1102)
)
alertCoolingDeviceNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertCoolingDeviceNormal.setDescription("""\
Cooling device sensor has returned to a normal value.
""")

alertCoolingDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1103)
)
alertCoolingDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceWarning.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertCoolingDeviceWarning.setDescription("""\
Cooling device sensor has detected a warning value.
""")

alertCoolingDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1104)
)
alertCoolingDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertCoolingDeviceFailure.setDescription("""\
Cooling device sensor has detected a failure value.
""")

alertCoolingDeviceNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1105)
)
alertCoolingDeviceNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertCoolingDeviceNonRecoverable.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertCoolingDeviceNonRecoverable.setDescription("""\
Cooling device sensor has detected a non-recoverable value.
""")

alertVoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1152)
)
alertVoltageProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertVoltageProbeNormal.setDescription("""\
Voltage probe has returned to a normal value.
""")

alertVoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1153)
)
alertVoltageProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeWarning.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertVoltageProbeWarning.setDescription("""\
Voltage probe has detected a warning value.
""")

alertVoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1154)
)
alertVoltageProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertVoltageProbeFailure.setDescription("""\
Voltage probe has detected a failure value.
""")

alertVoltageProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1155)
)
alertVoltageProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertVoltageProbeNonRecoverable.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertVoltageProbeNonRecoverable.setDescription("""\
Voltage probe has detected a non-recoverable value.
""")

alertAmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1202)
)
alertAmperageProbeNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertAmperageProbeNormal.setDescription("""\
Amperage probe has returned to a normal value.
""")

alertAmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1203)
)
alertAmperageProbeWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeWarning.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertAmperageProbeWarning.setDescription("""\
Amperage probe has detected a warning value.
""")

alertAmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1204)
)
alertAmperageProbeFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertAmperageProbeFailure.setDescription("""\
Amperage probe has detected a failure value.
""")

alertAmperageProbeNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1205)
)
alertAmperageProbeNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertAmperageProbeNonRecoverable.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertAmperageProbeNonRecoverable.setDescription("""\
Amperage probe has detected a non-recoverable value.
""")

alertChassisIntrusionNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1252)
)
alertChassisIntrusionNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertChassisIntrusionNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertChassisIntrusionNormal.setDescription("""\
Chassis intrusion has returned to normal.
""")

alertChassisIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1254)
)
alertChassisIntrusionDetected.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertChassisIntrusionDetected.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertChassisIntrusionDetected.setDescription("""\
Chassis intrusion has been detected.
""")

alertRedundancyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1304)
)
alertRedundancyNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertRedundancyNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertRedundancyNormal.setDescription("""\
Redundancy has returned to normal.
""")

alertRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1305)
)
alertRedundancyDegraded.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertRedundancyDegraded.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertRedundancyDegraded.setDescription("""\
Redundancy has been degraded.
""")

alertRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1306)
)
alertRedundancyLost.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertRedundancyLost.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertRedundancyLost.setDescription("""\
Redundancy has been lost.
""")

alertPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1352)
)
alertPowerSupplyNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertPowerSupplyNormal.setDescription("""\
Power supply has returned to normal.
""")

alertPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1354)
)
alertPowerSupplyFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertPowerSupplyFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertPowerSupplyFailure.setDescription("""\
Power supply has failed.
""")

alertMemoryDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1403)
)
alertMemoryDeviceWarning.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceWarning.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertMemoryDeviceWarning.setDescription("""\
Memory device pre-failure sensor has detected a warning value.
""")

alertMemoryDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1404)
)
alertMemoryDeviceFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertMemoryDeviceFailure.setDescription("""\
Memory device pre-failure sensor has detected a failure value.
""")

alertMemoryDeviceNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1405)
)
alertMemoryDeviceNonRecoverable.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertMemoryDeviceNonRecoverable.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertMemoryDeviceNonRecoverable.setDescription("""\
Memory device pre-failure sensor has detected a non-recoverable value.
""")

alertFanEnclosureInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1452)
)
alertFanEnclosureInsertion.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertFanEnclosureInsertion.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertFanEnclosureInsertion.setDescription("""\
Fan enclosure has been inserted into system.
""")

alertFanEnclosureRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1453)
)
alertFanEnclosureRemoval.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertFanEnclosureRemoval.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertFanEnclosureRemoval.setDescription("""\
Fan enclosure has been removed from system.
""")

alertFanEnclosureExtendedRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1454)
)
alertFanEnclosureExtendedRemoval.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertFanEnclosureExtendedRemoval.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertFanEnclosureExtendedRemoval.setDescription("""\
Fan enclosure has been removed from system for an extended amount of time.
""")

alertACPowerCordNoPowerNonRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1501)
)
alertACPowerCordNoPowerNonRedundant.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertACPowerCordNoPowerNonRedundant.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertACPowerCordNoPowerNonRedundant.setDescription("""\
AC power cord does not have power, and the reduncancy mode for its AC power
switch has been set to non-redundant.
""")

alertACPowerCordNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1502)
)
alertACPowerCordNormal.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertACPowerCordNormal.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertACPowerCordNormal.setDescription("""\
AC power cord has regained power.
""")

alertACPowerCordFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 1, 0, 1504)
)
alertACPowerCordFailure.setObjects(
      *(("MIB-Dell-10892", "alertSystem"),
        ("MIB-Dell-10892", "alertTableIndexOID"),
        ("MIB-Dell-10892", "alertMessage"),
        ("MIB-Dell-10892", "alertCurrentStatus"),
        ("MIB-Dell-10892", "alertPreviousStatus"),
        ("MIB-Dell-10892", "alertData"))
)
if mibBuilder.loadTexts:
    alertACPowerCordFailure.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    alertACPowerCordFailure.setDescription("""\
AC power cord has lost power.
""")


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-Dell-10892",
    **{"dell": dell,
       "server3": server3,
       "baseboardGroup": baseboardGroup,
       "alertSystemUp": alertSystemUp,
       "alertThermalShutdown": alertThermalShutdown,
       "alertTemperatureProbeNormal": alertTemperatureProbeNormal,
       "alertTemperatureProbeWarning": alertTemperatureProbeWarning,
       "alertTemperatureProbeFailure": alertTemperatureProbeFailure,
       "alertTemperatureProbeNonRecoverable": alertTemperatureProbeNonRecoverable,
       "alertCoolingDeviceNormal": alertCoolingDeviceNormal,
       "alertCoolingDeviceWarning": alertCoolingDeviceWarning,
       "alertCoolingDeviceFailure": alertCoolingDeviceFailure,
       "alertCoolingDeviceNonRecoverable": alertCoolingDeviceNonRecoverable,
       "alertVoltageProbeNormal": alertVoltageProbeNormal,
       "alertVoltageProbeWarning": alertVoltageProbeWarning,
       "alertVoltageProbeFailure": alertVoltageProbeFailure,
       "alertVoltageProbeNonRecoverable": alertVoltageProbeNonRecoverable,
       "alertAmperageProbeNormal": alertAmperageProbeNormal,
       "alertAmperageProbeWarning": alertAmperageProbeWarning,
       "alertAmperageProbeFailure": alertAmperageProbeFailure,
       "alertAmperageProbeNonRecoverable": alertAmperageProbeNonRecoverable,
       "alertChassisIntrusionNormal": alertChassisIntrusionNormal,
       "alertChassisIntrusionDetected": alertChassisIntrusionDetected,
       "alertRedundancyNormal": alertRedundancyNormal,
       "alertRedundancyDegraded": alertRedundancyDegraded,
       "alertRedundancyLost": alertRedundancyLost,
       "alertPowerSupplyNormal": alertPowerSupplyNormal,
       "alertPowerSupplyFailure": alertPowerSupplyFailure,
       "alertMemoryDeviceWarning": alertMemoryDeviceWarning,
       "alertMemoryDeviceFailure": alertMemoryDeviceFailure,
       "alertMemoryDeviceNonRecoverable": alertMemoryDeviceNonRecoverable,
       "alertFanEnclosureInsertion": alertFanEnclosureInsertion,
       "alertFanEnclosureRemoval": alertFanEnclosureRemoval,
       "alertFanEnclosureExtendedRemoval": alertFanEnclosureExtendedRemoval,
       "alertACPowerCordNoPowerNonRedundant": alertACPowerCordNoPowerNonRedundant,
       "alertACPowerCordNormal": alertACPowerCordNormal,
       "alertACPowerCordFailure": alertACPowerCordFailure,
       "mIBVersionGroup": mIBVersionGroup,
       "mIBMajorVersionNumber": mIBMajorVersionNumber,
       "mIBMinorVersionNumber": mIBMinorVersionNumber,
       "systemManagementSoftwareGroup": systemManagementSoftwareGroup,
       "systemManagementSoftwareName": systemManagementSoftwareName,
       "systemManagementSoftwareVersionNumberName": systemManagementSoftwareVersionNumberName,
       "systemManagementSoftwareBuildNumber": systemManagementSoftwareBuildNumber,
       "systemManagementSoftwareDescriptionName": systemManagementSoftwareDescriptionName,
       "systemManagementSoftwareSupportedProtocol": systemManagementSoftwareSupportedProtocol,
       "systemManagementSoftwarePreferredProtocol": systemManagementSoftwarePreferredProtocol,
       "systemManagementSoftwareUpdateLevelName": systemManagementSoftwareUpdateLevelName,
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
       "systemStateACPowerSwitchStateDetails": systemStateACPowerSwitchStateDetails,
       "systemStateACPowerSwitchStatusRedundancy": systemStateACPowerSwitchStatusRedundancy,
       "systemStateACPowerSwitchStatusDetails": systemStateACPowerSwitchStatusDetails,
       "systemStateACPowerCordStateDetails": systemStateACPowerCordStateDetails,
       "systemStateACPowerCordStatusCombined": systemStateACPowerCordStatusCombined,
       "systemStateACPowerCordStatusDetails": systemStateACPowerCordStatusDetails,
       "chassisInformationGroup": chassisInformationGroup,
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
       "chassisModelName": chassisModelName,
       "chassisAssetTagName": chassisAssetTagName,
       "chassisServiceTagName": chassisServiceTagName,
       "chassisID": chassisID,
       "chassisIDExtension": chassisIDExtension,
       "chassisSystemClass": chassisSystemClass,
       "chassisSystemName": chassisSystemName,
       "chassisSystemBootDateName": chassisSystemBootDateName,
       "chassisSystemDateName": chassisSystemDateName,
       "chassisSystemLocationName": chassisSystemLocationName,
       "chassisSystemPrimaryUserName": chassisSystemPrimaryUserName,
       "chassisSystemUserPhoneNumberName": chassisSystemUserPhoneNumberName,
       "chassisConnectionStatusUnique": chassisConnectionStatusUnique,
       "chassisFanControlCapabilitiesUnique": chassisFanControlCapabilitiesUnique,
       "chassisFanControlSettingsUnique": chassisFanControlSettingsUnique,
       "chassisLEDControlCapabilitiesUnique": chassisLEDControlCapabilitiesUnique,
       "chassisLEDControlSettingsUnique": chassisLEDControlSettingsUnique,
       "chassisHDFaultClearControlCapabilities": chassisHDFaultClearControlCapabilities,
       "chassisHDFaultClearControlSettings": chassisHDFaultClearControlSettings,
       "chassisIdentifyFlashControlCapabilities": chassisIdentifyFlashControlCapabilities,
       "chassisIdentifyFlashControlSettings": chassisIdentifyFlashControlSettings,
       "chassisLockPresent": chassisLockPresent,
       "chassishostControlCapabilitiesUnique": chassishostControlCapabilitiesUnique,
       "chassishostControlSettingsUnique": chassishostControlSettingsUnique,
       "chassiswatchDogControlCapabilitiesUnique": chassiswatchDogControlCapabilitiesUnique,
       "chassiswatchDogControlSettingsUnique": chassiswatchDogControlSettingsUnique,
       "chassiswatchDogControlExpiryTimeCapabilitiesUnique": chassiswatchDogControlExpiryTimeCapabilitiesUnique,
       "chassiswatchDogControlExpiryTime": chassiswatchDogControlExpiryTime,
       "chassisallowSETCommandsfromSNMP": chassisallowSETCommandsfromSNMP,
       "chassisPowerButtonControlCapabilitiesUnique": chassisPowerButtonControlCapabilitiesUnique,
       "chassisPowerButtonControlSettingsUnique": chassisPowerButtonControlSettingsUnique,
       "uUIDTable": uUIDTable,
       "uUIDTableEntry": uUIDTableEntry,
       "uUIDchassisIndex": uUIDchassisIndex,
       "uUIDIndex": uUIDIndex,
       "uUIDType": uUIDType,
       "uUIDValue": uUIDValue,
       "postLogTable": postLogTable,
       "postLogTableEntry": postLogTableEntry,
       "postLogchassisIndex": postLogchassisIndex,
       "postLogRecordIndex": postLogRecordIndex,
       "postLogStateCapabilitiesUnique": postLogStateCapabilitiesUnique,
       "postLogStateSettingsUnique": postLogStateSettingsUnique,
       "postLogRecord": postLogRecord,
       "postLogFormat": postLogFormat,
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
       "systemBIOSSize": systemBIOSSize,
       "systemBIOSReleaseDateName": systemBIOSReleaseDateName,
       "systemBIOSVersionName": systemBIOSVersionName,
       "systemBIOSStartingAddress": systemBIOSStartingAddress,
       "systemBIOSEndingAddress": systemBIOSEndingAddress,
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
       "firmwareDateName": firmwareDateName,
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
       "operatingSystemGroup": operatingSystemGroup,
       "operatingSystemTable": operatingSystemTable,
       "operatingSystemTableEntry": operatingSystemTableEntry,
       "operatingSystemchassisIndex": operatingSystemchassisIndex,
       "operatingSystemStateCapabilities": operatingSystemStateCapabilities,
       "operatingSystemStateSettings": operatingSystemStateSettings,
       "operatingSystemStatus": operatingSystemStatus,
       "operatingSystemIsPrimary": operatingSystemIsPrimary,
       "operatingSystemOperatingSystemName": operatingSystemOperatingSystemName,
       "operatingSystemOperatingSystemVersionName": operatingSystemOperatingSystemVersionName,
       "operatingSystemMemoryTable": operatingSystemMemoryTable,
       "operatingSystemMemoryTableEntry": operatingSystemMemoryTableEntry,
       "operatingSystemMemorychassisIndex": operatingSystemMemorychassisIndex,
       "operatingSystemMemoryStateCapabilities": operatingSystemMemoryStateCapabilities,
       "operatingSystemMemoryStateSettings": operatingSystemMemoryStateSettings,
       "operatingSystemMemoryStatus": operatingSystemMemoryStatus,
       "operatingSystemMemoryTotalPhysicalSize": operatingSystemMemoryTotalPhysicalSize,
       "operatingSystemMemoryAvailablePhysicalSize": operatingSystemMemoryAvailablePhysicalSize,
       "operatingSystemMemoryTotalPageFileSize": operatingSystemMemoryTotalPageFileSize,
       "operatingSystemMemoryAvailablePageFileSize": operatingSystemMemoryAvailablePageFileSize,
       "operatingSystemMemoryTotalVirtualSize": operatingSystemMemoryTotalVirtualSize,
       "operatingSystemMemoryAvailableVirtualSize": operatingSystemMemoryAvailableVirtualSize,
       "systemResourceGroup": systemResourceGroup,
       "systemResourceMapTable": systemResourceMapTable,
       "systemResourceMapTableEntry": systemResourceMapTableEntry,
       "systemResourceMapchassisIndex": systemResourceMapchassisIndex,
       "systemResourceMapIndex": systemResourceMapIndex,
       "systemResourceMapStateCapabilities": systemResourceMapStateCapabilities,
       "systemResourceMapStateSettings": systemResourceMapStateSettings,
       "systemResourceMapStatus": systemResourceMapStatus,
       "systemResourceMapType": systemResourceMapType,
       "systemResourceOwnerTable": systemResourceOwnerTable,
       "systemResourceOwnerTableEntry": systemResourceOwnerTableEntry,
       "systemResourceOwnerchassisIndex": systemResourceOwnerchassisIndex,
       "systemResourceOwnerIndex": systemResourceOwnerIndex,
       "systemResourceOwnerStateCapabilities": systemResourceOwnerStateCapabilities,
       "systemResourceOwnerStateSettings": systemResourceOwnerStateSettings,
       "systemResourceOwnerStatus": systemResourceOwnerStatus,
       "systemResourceOwnerInterfaceType": systemResourceOwnerInterfaceType,
       "systemResourceMapIndexReference": systemResourceMapIndexReference,
       "systemResourceOwnerDescriptionName": systemResourceOwnerDescriptionName,
       "systemResourceOwnerInterfaceInstance": systemResourceOwnerInterfaceInstance,
       "systemResourceIOPortTable": systemResourceIOPortTable,
       "systemResourceIOPortTableEntry": systemResourceIOPortTableEntry,
       "systemResourceIOPortchassisIndex": systemResourceIOPortchassisIndex,
       "systemResourceIOPortIndex": systemResourceIOPortIndex,
       "systemResourceIOPortStateCapabilities": systemResourceIOPortStateCapabilities,
       "systemResourceIOPortStateSettings": systemResourceIOPortStateSettings,
       "systemResourceIOPortStatus": systemResourceIOPortStatus,
       "systemResourceIOPortOwnerIndexReference": systemResourceIOPortOwnerIndexReference,
       "systemResourceIOPortShareDisposition": systemResourceIOPortShareDisposition,
       "systemResourceIOPortStartingAddress": systemResourceIOPortStartingAddress,
       "systemResourceIOPortEndingAddress": systemResourceIOPortEndingAddress,
       "systemResourceMemoryTable": systemResourceMemoryTable,
       "systemResourceMemoryTableEntry": systemResourceMemoryTableEntry,
       "systemResourceMemorychassisIndex": systemResourceMemorychassisIndex,
       "systemResourceMemoryIndex": systemResourceMemoryIndex,
       "systemResourceMemoryStateCapabilities": systemResourceMemoryStateCapabilities,
       "systemResourceMemoryStateSettings": systemResourceMemoryStateSettings,
       "systemResourceMemoryStatus": systemResourceMemoryStatus,
       "systemResourceMemoryOwnerIndexReference": systemResourceMemoryOwnerIndexReference,
       "systemResourceMemoryShareDisposition": systemResourceMemoryShareDisposition,
       "systemResourceMemoryStartingAddress": systemResourceMemoryStartingAddress,
       "systemResourceMemoryEndingAddress": systemResourceMemoryEndingAddress,
       "systemResourceMemoryFlags": systemResourceMemoryFlags,
       "systemResourceInterruptTable": systemResourceInterruptTable,
       "systemResourceInterruptTableEntry": systemResourceInterruptTableEntry,
       "systemResourceInterruptchassisIndex": systemResourceInterruptchassisIndex,
       "systemResourceInterruptIndex": systemResourceInterruptIndex,
       "systemResourceInterruptStateCapabilities": systemResourceInterruptStateCapabilities,
       "systemResourceInterruptStateSettings": systemResourceInterruptStateSettings,
       "systemResourceInterruptStatus": systemResourceInterruptStatus,
       "systemResourceInterruptOwnerIndexReference": systemResourceInterruptOwnerIndexReference,
       "systemResourceInterruptShareDisposition": systemResourceInterruptShareDisposition,
       "systemResourceInterruptLevel": systemResourceInterruptLevel,
       "systemResourceInterruptType": systemResourceInterruptType,
       "systemResourceInterruptTrigger": systemResourceInterruptTrigger,
       "systemResourceDMATable": systemResourceDMATable,
       "systemResourceDMATableEntry": systemResourceDMATableEntry,
       "systemResourceDMAchassisIndex": systemResourceDMAchassisIndex,
       "systemResourceDMAIndex": systemResourceDMAIndex,
       "systemResourceDMAStateCapabilities": systemResourceDMAStateCapabilities,
       "systemResourceDMAStateSettings": systemResourceDMAStateSettings,
       "systemResourceDMAStatus": systemResourceDMAStatus,
       "systemResourceDMAOwnerIndexReference": systemResourceDMAOwnerIndexReference,
       "systemResourceDMAShareDisposition": systemResourceDMAShareDisposition,
       "systemResourceDMAMaximumTransferSize": systemResourceDMAMaximumTransferSize,
       "systemResourceDMATransferWidth": systemResourceDMATransferWidth,
       "systemResourceDMABusMaster": systemResourceDMABusMaster,
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
       "powerSupplyInputVoltage": powerSupplyInputVoltage,
       "powerSupplypowerUnitIndexReference": powerSupplypowerUnitIndexReference,
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
       "aCPowerSwitchTable": aCPowerSwitchTable,
       "aCPowerSwitchTableEntry": aCPowerSwitchTableEntry,
       "aCPowerSwitchchassisIndex": aCPowerSwitchchassisIndex,
       "aCPowerSwitchIndex": aCPowerSwitchIndex,
       "aCPowerSwitchCapabilities": aCPowerSwitchCapabilities,
       "aCPowerSwitchSettings": aCPowerSwitchSettings,
       "aCPowerSwitchRedundancyStatus": aCPowerSwitchRedundancyStatus,
       "aCPowerCordCountForRedundancy": aCPowerCordCountForRedundancy,
       "aCPowerSwitchName": aCPowerSwitchName,
       "aCPowerSwitchRedundancyMode": aCPowerSwitchRedundancyMode,
       "aCPowerCordTable": aCPowerCordTable,
       "aCPowerCordTableEntry": aCPowerCordTableEntry,
       "aCPowerCordchassisIndex": aCPowerCordchassisIndex,
       "aCPowerCordIndex": aCPowerCordIndex,
       "aCPowerCordStateCapabilities": aCPowerCordStateCapabilities,
       "aCPowerCordStateSettings": aCPowerCordStateSettings,
       "aCPowerCordStatus": aCPowerCordStatus,
       "aCPowerCordaCPowerSwitchIndexReference": aCPowerCordaCPowerSwitchIndexReference,
       "aCPowerCordLocationName": aCPowerCordLocationName,
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
       "userSecurityGroup": userSecurityGroup,
       "userSecurityTable": userSecurityTable,
       "userSecurityTableEntry": userSecurityTableEntry,
       "userSecuritychassisIndex": userSecuritychassisIndex,
       "userSecurityIndex": userSecurityIndex,
       "userSecurityUserName": userSecurityUserName,
       "userSecurityControlName": userSecurityControlName,
       "userSecurityRequestName": userSecurityRequestName,
       "remoteFlashBIOSGroup": remoteFlashBIOSGroup,
       "remoteFlashBIOSTable": remoteFlashBIOSTable,
       "remoteFlashBIOSTableEntry": remoteFlashBIOSTableEntry,
       "remoteFlashBIOSchassisIndex": remoteFlashBIOSchassisIndex,
       "remoteFlashBIOSIndex": remoteFlashBIOSIndex,
       "remoteFlashBIOSStateCapabilitiesUnique": remoteFlashBIOSStateCapabilitiesUnique,
       "remoteFlashBIOSStateSettingsUnique": remoteFlashBIOSStateSettingsUnique,
       "remoteFlashBIOSStatus": remoteFlashBIOSStatus,
       "remoteFlashBIOSLastBIOSDateName": remoteFlashBIOSLastBIOSDateName,
       "remoteFlashBIOSCompletionCode": remoteFlashBIOSCompletionCode,
       "remoteFlashBIOSMinimumContiguousMemory": remoteFlashBIOSMinimumContiguousMemory,
       "portGroup": portGroup,
       "pointingPortTable": pointingPortTable,
       "pointingPortTableEntry": pointingPortTableEntry,
       "pointingPortchassisIndex": pointingPortchassisIndex,
       "pointingPortIndex": pointingPortIndex,
       "pointingPortStateCapabilities": pointingPortStateCapabilities,
       "pointingPortStateSettings": pointingPortStateSettings,
       "pointingPortStatus": pointingPortStatus,
       "pointingPortSecurityState": pointingPortSecurityState,
       "pointingPortConnectorType": pointingPortConnectorType,
       "pointingPortName": pointingPortName,
       "pointingPortBIOSConnectorType": pointingPortBIOSConnectorType,
       "keyboardPortTable": keyboardPortTable,
       "keyboardPortTableEntry": keyboardPortTableEntry,
       "keyboardPortchassisIndex": keyboardPortchassisIndex,
       "keyboardPortIndex": keyboardPortIndex,
       "keyboardPortStateCapabilities": keyboardPortStateCapabilities,
       "keyboardPortStateSettings": keyboardPortStateSettings,
       "keyboardPortStatus": keyboardPortStatus,
       "keyboardPortSecurityState": keyboardPortSecurityState,
       "keyboardPortConnectorType": keyboardPortConnectorType,
       "keyboardPortName": keyboardPortName,
       "keyboardPortBIOSConnectorType": keyboardPortBIOSConnectorType,
       "processorPortTable": processorPortTable,
       "processorPortTableEntry": processorPortTableEntry,
       "processorPortchassisIndex": processorPortchassisIndex,
       "processorPortIndex": processorPortIndex,
       "processorPortStateCapabilities": processorPortStateCapabilities,
       "processorPortStateSettings": processorPortStateSettings,
       "processorPortStatus": processorPortStatus,
       "processorPortSecurityState": processorPortSecurityState,
       "processorPortConnectorType": processorPortConnectorType,
       "processorPortName": processorPortName,
       "processorPortBIOSConnectorType": processorPortBIOSConnectorType,
       "memoryDevicePortTable": memoryDevicePortTable,
       "memoryDevicePortTableEntry": memoryDevicePortTableEntry,
       "memoryDevicePortchassisIndex": memoryDevicePortchassisIndex,
       "memoryDevicePortIndex": memoryDevicePortIndex,
       "memoryDevicePortStateCapabilities": memoryDevicePortStateCapabilities,
       "memoryDevicePortStateSettings": memoryDevicePortStateSettings,
       "memoryDevicePortStatus": memoryDevicePortStatus,
       "memoryDevicePortSecurityState": memoryDevicePortSecurityState,
       "memoryDevicePortConnectorType": memoryDevicePortConnectorType,
       "memoryDevicePortName": memoryDevicePortName,
       "memoryDevicePortBIOSConnectorType": memoryDevicePortBIOSConnectorType,
       "memoryDevicePortPhysicalMemoryArrayIndexReference": memoryDevicePortPhysicalMemoryArrayIndexReference,
       "monitorPortTable": monitorPortTable,
       "monitorPortTableEntry": monitorPortTableEntry,
       "monitorPortchassisIndex": monitorPortchassisIndex,
       "monitorPortIndex": monitorPortIndex,
       "monitorPortStateCapabilities": monitorPortStateCapabilities,
       "monitorPortStateSettings": monitorPortStateSettings,
       "monitorPortStatus": monitorPortStatus,
       "monitorPortSecurityState": monitorPortSecurityState,
       "monitorPortConnectorType": monitorPortConnectorType,
       "monitorPortName": monitorPortName,
       "monitorPortBIOSConnectorType": monitorPortBIOSConnectorType,
       "sCSIPortTable": sCSIPortTable,
       "sCSIPortTableEntry": sCSIPortTableEntry,
       "sCSIPortchassisIndex": sCSIPortchassisIndex,
       "sCSIPortIndex": sCSIPortIndex,
       "sCSIPortStateCapabilities": sCSIPortStateCapabilities,
       "sCSIPortStateSettings": sCSIPortStateSettings,
       "sCSIPortStatus": sCSIPortStatus,
       "sCSIPortSecurityState": sCSIPortSecurityState,
       "sCSIPortConnectorType": sCSIPortConnectorType,
       "sCSIPortName": sCSIPortName,
       "sCSIPortBIOSConnectorType": sCSIPortBIOSConnectorType,
       "parallelPortTable": parallelPortTable,
       "parallelPortTableEntry": parallelPortTableEntry,
       "parallelPortchassisIndex": parallelPortchassisIndex,
       "parallelPortIndex": parallelPortIndex,
       "parallelPortStateCapabilities": parallelPortStateCapabilities,
       "parallelPortStateSettings": parallelPortStateSettings,
       "parallelPortStatus": parallelPortStatus,
       "parallelPortSecurityState": parallelPortSecurityState,
       "parallelPortConnectorType": parallelPortConnectorType,
       "parallelPortName": parallelPortName,
       "parallelPortConnectorPinOut": parallelPortConnectorPinOut,
       "parallelPortCapabilitiesUnique": parallelPortCapabilitiesUnique,
       "parallelPortBaseIOAddress": parallelPortBaseIOAddress,
       "parallelPortIRQLevel": parallelPortIRQLevel,
       "parallelPortDMASupport": parallelPortDMASupport,
       "serialPortTable": serialPortTable,
       "serialPortTableEntry": serialPortTableEntry,
       "serialPortchassisIndex": serialPortchassisIndex,
       "serialPortIndex": serialPortIndex,
       "serialPortStateCapabilities": serialPortStateCapabilities,
       "serialPortStateSettings": serialPortStateSettings,
       "serialPortStatus": serialPortStatus,
       "serialPortSecurityState": serialPortSecurityState,
       "serialPortConnectorType": serialPortConnectorType,
       "serialPortName": serialPortName,
       "serialPortMaximumSpeed": serialPortMaximumSpeed,
       "serialPortCapabilitiesUnique": serialPortCapabilitiesUnique,
       "serialPortBaseIOAddress": serialPortBaseIOAddress,
       "serialPortIRQLevel": serialPortIRQLevel,
       "uSBPortTable": uSBPortTable,
       "uSBPortTableEntry": uSBPortTableEntry,
       "uSBPortchassisIndex": uSBPortchassisIndex,
       "uSBPortIndex": uSBPortIndex,
       "uSBPortStateCapabilities": uSBPortStateCapabilities,
       "uSBPortStateSettings": uSBPortStateSettings,
       "uSBPortStatus": uSBPortStatus,
       "uSBPortSecurityState": uSBPortSecurityState,
       "uSBPortConnectorType": uSBPortConnectorType,
       "uSBPortName": uSBPortName,
       "uSBPortBIOSConnectorType": uSBPortBIOSConnectorType,
       "deviceGroup": deviceGroup,
       "pointingDeviceTable": pointingDeviceTable,
       "pointingDeviceTableEntry": pointingDeviceTableEntry,
       "pointingDevicechassisIndex": pointingDevicechassisIndex,
       "pointingDeviceIndex": pointingDeviceIndex,
       "pointingDeviceStateCapabilities": pointingDeviceStateCapabilities,
       "pointingDeviceStateSettings": pointingDeviceStateSettings,
       "pointingDeviceStatus": pointingDeviceStatus,
       "pointingPortIndexReference": pointingPortIndexReference,
       "pointingDeviceType": pointingDeviceType,
       "pointingDeviceNumberofButtons": pointingDeviceNumberofButtons,
       "keyboardDeviceTable": keyboardDeviceTable,
       "keyboardDeviceTableEntry": keyboardDeviceTableEntry,
       "keyboardDevicechassisIndex": keyboardDevicechassisIndex,
       "keyboardDeviceIndex": keyboardDeviceIndex,
       "keyboardDeviceStateCapabilities": keyboardDeviceStateCapabilities,
       "keyboardDeviceStateSettings": keyboardDeviceStateSettings,
       "keyboardDeviceStatus": keyboardDeviceStatus,
       "keyboardPortIndexReference": keyboardPortIndexReference,
       "keyboardDeviceTypeName": keyboardDeviceTypeName,
       "keyboardDeviceLayoutName": keyboardDeviceLayoutName,
       "processorDeviceTable": processorDeviceTable,
       "processorDeviceTableEntry": processorDeviceTableEntry,
       "processorDevicechassisIndex": processorDevicechassisIndex,
       "processorDeviceIndex": processorDeviceIndex,
       "processorDeviceStateCapabilities": processorDeviceStateCapabilities,
       "processorDeviceStateSettings": processorDeviceStateSettings,
       "processorDeviceStatus": processorDeviceStatus,
       "processorPortIndexReference": processorPortIndexReference,
       "processorDeviceType": processorDeviceType,
       "processorDeviceManufacturerName": processorDeviceManufacturerName,
       "processorDeviceStatusState": processorDeviceStatusState,
       "processorDeviceFamily": processorDeviceFamily,
       "processorDeviceMaximumSpeed": processorDeviceMaximumSpeed,
       "processorDeviceCurrentSpeed": processorDeviceCurrentSpeed,
       "processorDeviceExternalClockSpeed": processorDeviceExternalClockSpeed,
       "processorDeviceVoltage": processorDeviceVoltage,
       "processorDeviceUpgradeInformation": processorDeviceUpgradeInformation,
       "processorDeviceVersionName": processorDeviceVersionName,
       "cacheDeviceTable": cacheDeviceTable,
       "cacheDeviceTableEntry": cacheDeviceTableEntry,
       "cacheDevicechassisIndex": cacheDevicechassisIndex,
       "cacheDeviceIndex": cacheDeviceIndex,
       "cacheDeviceStateCapabilities": cacheDeviceStateCapabilities,
       "cacheDeviceStateSettings": cacheDeviceStateSettings,
       "cacheDeviceStatus": cacheDeviceStatus,
       "cacheDeviceprocessorDeviceIndexReference": cacheDeviceprocessorDeviceIndexReference,
       "cacheDeviceType": cacheDeviceType,
       "cacheDeviceLocation": cacheDeviceLocation,
       "cacheDeviceStatusState": cacheDeviceStatusState,
       "cacheDeviceExternalSocketName": cacheDeviceExternalSocketName,
       "cacheDeviceLevel": cacheDeviceLevel,
       "cacheDeviceMaximumSize": cacheDeviceMaximumSize,
       "cacheDeviceCurrentSize": cacheDeviceCurrentSize,
       "cacheDeviceSpeed": cacheDeviceSpeed,
       "cacheDeviceWritePolicy": cacheDeviceWritePolicy,
       "cacheDeviceIsSocketed": cacheDeviceIsSocketed,
       "cacheDeviceECCType": cacheDeviceECCType,
       "cacheDeviceAssociativity": cacheDeviceAssociativity,
       "cacheDeviceSupportedType": cacheDeviceSupportedType,
       "cacheDeviceCurrentType": cacheDeviceCurrentType,
       "memoryDeviceTable": memoryDeviceTable,
       "memoryDeviceTableEntry": memoryDeviceTableEntry,
       "memoryDevicechassisIndex": memoryDevicechassisIndex,
       "memoryDeviceIndex": memoryDeviceIndex,
       "memoryDeviceStateCapabilities": memoryDeviceStateCapabilities,
       "memoryDeviceStateSettings": memoryDeviceStateSettings,
       "memoryDeviceStatus": memoryDeviceStatus,
       "memoryDeviceMemoryPortIndexReference": memoryDeviceMemoryPortIndexReference,
       "memoryDeviceType": memoryDeviceType,
       "memoryDeviceLocationName": memoryDeviceLocationName,
       "memoryDeviceErrorCount": memoryDeviceErrorCount,
       "memoryDeviceBankLocationName": memoryDeviceBankLocationName,
       "memoryDeviceTypeDetails": memoryDeviceTypeDetails,
       "memoryDeviceFormFactor": memoryDeviceFormFactor,
       "memoryDeviceSet": memoryDeviceSet,
       "memoryDeviceSize": memoryDeviceSize,
       "memoryDeviceSpeed": memoryDeviceSpeed,
       "memoryDeviceTotalBusWidth": memoryDeviceTotalBusWidth,
       "memoryDeviceTotalDataBusWidth": memoryDeviceTotalDataBusWidth,
       "memoryDeviceSingleBitErrorCount": memoryDeviceSingleBitErrorCount,
       "memoryDeviceMultiBitErrorCount": memoryDeviceMultiBitErrorCount,
       "memoryDeviceMappedAddressTable": memoryDeviceMappedAddressTable,
       "memoryDeviceMappedAddressTableEntry": memoryDeviceMappedAddressTableEntry,
       "memoryDeviceMappedAddresschassisIndex": memoryDeviceMappedAddresschassisIndex,
       "memoryDeviceMappedAddressIndex": memoryDeviceMappedAddressIndex,
       "memoryDeviceMappedAddressStateCapabilities": memoryDeviceMappedAddressStateCapabilities,
       "memoryDeviceMappedAddressStateSettings": memoryDeviceMappedAddressStateSettings,
       "memoryDeviceMappedAddressStatus": memoryDeviceMappedAddressStatus,
       "memoryDeviceIndexReference": memoryDeviceIndexReference,
       "memoryDeviceMappedAddressRowPosition": memoryDeviceMappedAddressRowPosition,
       "memoryDeviceMappedAddressInterleavePosition": memoryDeviceMappedAddressInterleavePosition,
       "memoryDeviceMappedAddressInterleaveDepth": memoryDeviceMappedAddressInterleaveDepth,
       "memoryDeviceMappedAddressStartingAddress": memoryDeviceMappedAddressStartingAddress,
       "memoryDeviceMappedAddressEndingAddress": memoryDeviceMappedAddressEndingAddress,
       "genericDeviceTable": genericDeviceTable,
       "genericDeviceTableEntry": genericDeviceTableEntry,
       "genericDevicechassisIndex": genericDevicechassisIndex,
       "genericDeviceIndex": genericDeviceIndex,
       "genericDeviceStateCapabilities": genericDeviceStateCapabilities,
       "genericDeviceStateSettings": genericDeviceStateSettings,
       "genericDeviceStatus": genericDeviceStatus,
       "genericDeviceSystemSlotIndexReference": genericDeviceSystemSlotIndexReference,
       "genericDeviceType": genericDeviceType,
       "genericDeviceName": genericDeviceName,
       "pCIDeviceTable": pCIDeviceTable,
       "pCIDeviceTableEntry": pCIDeviceTableEntry,
       "pCIDevicechassisIndex": pCIDevicechassisIndex,
       "pCIDeviceIndex": pCIDeviceIndex,
       "pCIDeviceStateCapabilities": pCIDeviceStateCapabilities,
       "pCIDeviceStateSettings": pCIDeviceStateSettings,
       "pCIDeviceStatus": pCIDeviceStatus,
       "pCIDeviceSystemSlotIndexReference": pCIDeviceSystemSlotIndexReference,
       "pCIDeviceDataBusWidth": pCIDeviceDataBusWidth,
       "pCIDeviceManufacturerName": pCIDeviceManufacturerName,
       "pCIDeviceDescriptionName": pCIDeviceDescriptionName,
       "pCIDeviceSpeed": pCIDeviceSpeed,
       "pCIDeviceAdapterFault": pCIDeviceAdapterFault,
       "pCIDeviceConfigurationSpaceTable": pCIDeviceConfigurationSpaceTable,
       "pCIDeviceConfigurationSpaceTableEntry": pCIDeviceConfigurationSpaceTableEntry,
       "pCIDeviceConfigurationSpacechassisIndex": pCIDeviceConfigurationSpacechassisIndex,
       "pCIDeviceConfigurationSpaceIndex": pCIDeviceConfigurationSpaceIndex,
       "pCIDeviceConfigurationSpaceStateCapabilities": pCIDeviceConfigurationSpaceStateCapabilities,
       "pCIDeviceConfigurationSpaceStateSettings": pCIDeviceConfigurationSpaceStateSettings,
       "pCIDeviceConfigurationSpaceStatus": pCIDeviceConfigurationSpaceStatus,
       "pCIDeviceIndexReference": pCIDeviceIndexReference,
       "pCIDeviceConfigurationSpaceBusNumber": pCIDeviceConfigurationSpaceBusNumber,
       "pCIDeviceConfigurationSpaceDeviceNumber": pCIDeviceConfigurationSpaceDeviceNumber,
       "pCIDeviceConfigurationSpaceFunctionNumber": pCIDeviceConfigurationSpaceFunctionNumber,
       "pCIDeviceConfigurationSpaceHeader": pCIDeviceConfigurationSpaceHeader,
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
       "systemSlotLength": systemSlotLength,
       "systemSlotSlotID": systemSlotSlotID,
       "systemSlotCategory": systemSlotCategory,
       "systemSlotHotPlugBusWidth": systemSlotHotPlugBusWidth,
       "systemSlotHotPlugSlotSpeed": systemSlotHotPlugSlotSpeed,
       "systemSlotHotPlugAdapterSpeed": systemSlotHotPlugAdapterSpeed,
       "memoryGroup": memoryGroup,
       "physicalMemoryArrayTable": physicalMemoryArrayTable,
       "physicalMemoryArrayTableEntry": physicalMemoryArrayTableEntry,
       "physicalMemoryArraychassisIndex": physicalMemoryArraychassisIndex,
       "physicalMemoryArrayIndex": physicalMemoryArrayIndex,
       "physicalMemoryArrayStateCapabilities": physicalMemoryArrayStateCapabilities,
       "physicalMemoryArrayStateSettings": physicalMemoryArrayStateSettings,
       "physicalMemoryArrayStatus": physicalMemoryArrayStatus,
       "physicalMemoryArrayUse": physicalMemoryArrayUse,
       "physicalMemoryArrayECCType": physicalMemoryArrayECCType,
       "physicalMemoryArrayLocation": physicalMemoryArrayLocation,
       "physicalMemoryArrayMaximumSize": physicalMemoryArrayMaximumSize,
       "physicalMemoryArrayTotalNumberSockets": physicalMemoryArrayTotalNumberSockets,
       "physicalMemoryArrayInUseNumberSockets": physicalMemoryArrayInUseNumberSockets,
       "physicalMemoryArrayECCErrorNonRecoverableThreshold": physicalMemoryArrayECCErrorNonRecoverableThreshold,
       "physicalMemoryArrayECCErrorCriticalThreshold": physicalMemoryArrayECCErrorCriticalThreshold,
       "physicalMemoryArrayECCErrorNonCriticalThreshold": physicalMemoryArrayECCErrorNonCriticalThreshold,
       "physicalMemoryArrayMappedTable": physicalMemoryArrayMappedTable,
       "physicalMemoryArrayMappedTableEntry": physicalMemoryArrayMappedTableEntry,
       "physicalMemoryArrayMappedchassisIndex": physicalMemoryArrayMappedchassisIndex,
       "physicalMemoryArrayMappedIndex": physicalMemoryArrayMappedIndex,
       "physicalMemoryArrayMappedStateCapabilities": physicalMemoryArrayMappedStateCapabilities,
       "physicalMemoryArrayMappedStateSettings": physicalMemoryArrayMappedStateSettings,
       "physicalMemoryArrayMappedStatus": physicalMemoryArrayMappedStatus,
       "physicalMemoryArrayIndexReference": physicalMemoryArrayIndexReference,
       "physicalMemoryArrayMappedStartingAddress": physicalMemoryArrayMappedStartingAddress,
       "physicalMemoryArrayMappedEndingAddress": physicalMemoryArrayMappedEndingAddress,
       "physicalMemoryArrayMappedPartitionWidth": physicalMemoryArrayMappedPartitionWidth,
       "biosSetUpControlGroup": biosSetUpControlGroup,
       "biosSetUpControlTable": biosSetUpControlTable,
       "biosSetUpControlTableEntry": biosSetUpControlTableEntry,
       "biosSetUpControlchassisIndex": biosSetUpControlchassisIndex,
       "bSUCpointingDeviceControlCapabilities": bSUCpointingDeviceControlCapabilities,
       "bSUCpointingDeviceControlSettings": bSUCpointingDeviceControlSettings,
       "bSUCpointingDeviceControlStatus": bSUCpointingDeviceControlStatus,
       "bSUCpointingDeviceControlName": bSUCpointingDeviceControlName,
       "bSUCnumLockControlCapabilities": bSUCnumLockControlCapabilities,
       "bSUCnumLockControlSettings": bSUCnumLockControlSettings,
       "bSUCnumLockControlStatus": bSUCnumLockControlStatus,
       "bSUCnumLockControlName": bSUCnumLockControlName,
       "bSUCprocessorSerialNumberControlCapabilities": bSUCprocessorSerialNumberControlCapabilities,
       "bSUCprocessorSerialNumberControlSettings": bSUCprocessorSerialNumberControlSettings,
       "bSUCprocessorSerialNumberControlStatus": bSUCprocessorSerialNumberControlStatus,
       "bSUCprocessorSerialNumberControlName": bSUCprocessorSerialNumberControlName,
       "bSUCspeakerControlCapabilitiesUnique": bSUCspeakerControlCapabilitiesUnique,
       "bSUCspeakerControlSettingsUnique": bSUCspeakerControlSettingsUnique,
       "bSUCspeakerControlStatus": bSUCspeakerControlStatus,
       "bSUCspeakerControlName": bSUCspeakerControlName,
       "bSUCnIFwakeonLanControlCapabilitiesUnique": bSUCnIFwakeonLanControlCapabilitiesUnique,
       "bSUCnIFwakeonLanControlSettingsUnique": bSUCnIFwakeonLanControlSettingsUnique,
       "bSUCnIFwakeonLanControlStatus": bSUCnIFwakeonLanControlStatus,
       "bSUCnIFwakeonLanControlName": bSUCnIFwakeonLanControlName,
       "bSUCbootSequenceControlCapabilitiesUnique": bSUCbootSequenceControlCapabilitiesUnique,
       "bSUCbootSequenceControlSettingsUnique": bSUCbootSequenceControlSettingsUnique,
       "bSUCbootSequenceControlStatus": bSUCbootSequenceControlStatus,
       "bSUCbootSequenceControlName": bSUCbootSequenceControlName,
       "bSUCadministratorPasswordControlCapabilitiesUnique": bSUCadministratorPasswordControlCapabilitiesUnique,
       "bSUCadministratorPasswordControlSettingsUnique": bSUCadministratorPasswordControlSettingsUnique,
       "bSUCadministratorPasswordControlStatus": bSUCadministratorPasswordControlStatus,
       "bSUCadministratorPasswordPasswordVerifyName": bSUCadministratorPasswordPasswordVerifyName,
       "bSUCadministratorPasswordNewPasswordName": bSUCadministratorPasswordNewPasswordName,
       "bSUCuserPasswordControlCapabilitiesUnique": bSUCuserPasswordControlCapabilitiesUnique,
       "bSUCuserPasswordControlSettingsUnique": bSUCuserPasswordControlSettingsUnique,
       "bSUCuserPasswordControlStatus": bSUCuserPasswordControlStatus,
       "bSUCuserPasswordPasswordVerifyName": bSUCuserPasswordPasswordVerifyName,
       "bSUCuserPasswordNewPasswordName": bSUCuserPasswordNewPasswordName,
       "sCSIControlTable": sCSIControlTable,
       "sCSIControlTableEntry": sCSIControlTableEntry,
       "sCSIControlchassisIndex": sCSIControlchassisIndex,
       "sCSIControlIndex": sCSIControlIndex,
       "sCSIControlCapabilities": sCSIControlCapabilities,
       "sCSIControlSettings": sCSIControlSettings,
       "sCSIControlStatus": sCSIControlStatus,
       "sCSIControlName": sCSIControlName,
       "parallelPortControlTable": parallelPortControlTable,
       "parallelPortControlTableEntry": parallelPortControlTableEntry,
       "parallelPortControlchassisIndex": parallelPortControlchassisIndex,
       "parallelPortControlIndex": parallelPortControlIndex,
       "parallelPortControlCapabilitiesUnique": parallelPortControlCapabilitiesUnique,
       "parallelPortControlSettingsUnique": parallelPortControlSettingsUnique,
       "parallelPortControlStatus": parallelPortControlStatus,
       "parallelPortControlName": parallelPortControlName,
       "parallelPortControlModeCapabilitiesUnique": parallelPortControlModeCapabilitiesUnique,
       "parallelPortControlModeSettingsUnique": parallelPortControlModeSettingsUnique,
       "serialPortControlTable": serialPortControlTable,
       "serialPortControlTableEntry": serialPortControlTableEntry,
       "serialPortControlchassisIndex": serialPortControlchassisIndex,
       "serialPortControlIndex": serialPortControlIndex,
       "serialPortControlCapabilitiesUnique": serialPortControlCapabilitiesUnique,
       "serialPortControlSettingsUnique": serialPortControlSettingsUnique,
       "serialPortControlStatus": serialPortControlStatus,
       "serialPortControlName": serialPortControlName,
       "usbControlTable": usbControlTable,
       "usbControlTableEntry": usbControlTableEntry,
       "usbControlchassisIndex": usbControlchassisIndex,
       "usbControlIndex": usbControlIndex,
       "usbControlCapabilities": usbControlCapabilities,
       "usbControlSettings": usbControlSettings,
       "usbControlStatus": usbControlStatus,
       "usbControlName": usbControlName,
       "ideControlTable": ideControlTable,
       "ideControlTableEntry": ideControlTableEntry,
       "ideControlchassisIndex": ideControlchassisIndex,
       "ideControlIndex": ideControlIndex,
       "ideControlCapabilitiesUnique": ideControlCapabilitiesUnique,
       "ideControlSettingsUnique": ideControlSettingsUnique,
       "ideControlStatus": ideControlStatus,
       "ideControlName": ideControlName,
       "disketteControlTable": disketteControlTable,
       "disketteControlTableEntry": disketteControlTableEntry,
       "disketteControlchassisIndex": disketteControlchassisIndex,
       "disketteControlIndex": disketteControlIndex,
       "disketteControlCapabilitiesUnique": disketteControlCapabilitiesUnique,
       "disketteControlSettingsUnique": disketteControlSettingsUnique,
       "disketteControlStatus": disketteControlStatus,
       "disketteControlName": disketteControlName,
       "networkInterfaceControlTable": networkInterfaceControlTable,
       "networkInterfaceControlTableEntry": networkInterfaceControlTableEntry,
       "networkInterfaceControlchassisIndex": networkInterfaceControlchassisIndex,
       "networkInterfaceControlIndex": networkInterfaceControlIndex,
       "networkInterfaceControlCapabilitiesUnique": networkInterfaceControlCapabilitiesUnique,
       "networkInterfaceControlSettingsUnique": networkInterfaceControlSettingsUnique,
       "networkInterfaceControlStatus": networkInterfaceControlStatus,
       "networkInterfaceControlName": networkInterfaceControlName,
       "lraGroup": lraGroup,
       "lRAGlobalSettingsTable": lRAGlobalSettingsTable,
       "lRAGlobalSettingsTableEntry": lRAGlobalSettingsTableEntry,
       "lRAGlobalchassisIndex": lRAGlobalchassisIndex,
       "lRAGlobalState": lRAGlobalState,
       "lRAGlobalSettingsDisableTimeoutValue": lRAGlobalSettingsDisableTimeoutValue,
       "lRAGlobalSettingsCapabilitiesUnique": lRAGlobalSettingsCapabilitiesUnique,
       "lRAGlobalThermalShutdownCapabilitiesUnique": lRAGlobalThermalShutdownCapabilitiesUnique,
       "lRAGlobalThermalShutdownStateSettingsUnique": lRAGlobalThermalShutdownStateSettingsUnique,
       "lRAActionTableTable": lRAActionTableTable,
       "lRAActionTableTableEntry": lRAActionTableTableEntry,
       "lRAActionTablechassisIndex": lRAActionTablechassisIndex,
       "lRAActionTableActionNumberIndex": lRAActionTableActionNumberIndex,
       "lRAActionTableUserApplicationName": lRAActionTableUserApplicationName,
       "lRAActionTableSettingsUnique": lRAActionTableSettingsUnique,
       "cooGroup": cooGroup,
       "cooTable": cooTable,
       "cooTableEntry": cooTableEntry,
       "coochassisIndex": coochassisIndex,
       "cooState": cooState,
       "cooAquisitionPurchaseCost": cooAquisitionPurchaseCost,
       "cooAquisitionWayBillNumber": cooAquisitionWayBillNumber,
       "cooAquisitionInstallDateName": cooAquisitionInstallDateName,
       "cooAquisitionPurchaseOrder": cooAquisitionPurchaseOrder,
       "cooAquisitionPurchaseDateName": cooAquisitionPurchaseDateName,
       "cooAquisitionSigningAuthorityName": cooAquisitionSigningAuthorityName,
       "cooOriginalMachineConfigurationExpensed": cooOriginalMachineConfigurationExpensed,
       "cooOriginalMachineConfigurationVendorName": cooOriginalMachineConfigurationVendorName,
       "cooCostCenterInformationVendorName": cooCostCenterInformationVendorName,
       "cooUserInformationUserName": cooUserInformationUserName,
       "cooExtendedWarrantyStartDateName": cooExtendedWarrantyStartDateName,
       "cooExtendedWarrantyEndDateName": cooExtendedWarrantyEndDateName,
       "cooExtendedWarrantyCost": cooExtendedWarrantyCost,
       "cooExtendedWarrantyProviderName": cooExtendedWarrantyProviderName,
       "cooOwnershipCode": cooOwnershipCode,
       "cooCorporateOwnerName": cooCorporateOwnerName,
       "cooHazardousWasteCodeName": cooHazardousWasteCodeName,
       "cooDeploymentDateLength": cooDeploymentDateLength,
       "cooDeploymentDurationType": cooDeploymentDurationType,
       "cooTrainingName": cooTrainingName,
       "cooOutsourcingProblemDescriptionName": cooOutsourcingProblemDescriptionName,
       "cooOutsourcingServiceFeeName": cooOutsourcingServiceFeeName,
       "cooOutsourcingSigningAuthorityName": cooOutsourcingSigningAuthorityName,
       "cooOutsourcingProviderFeeName": cooOutsourcingProviderFeeName,
       "cooOutsourcingProviderServiceLevelName": cooOutsourcingProviderServiceLevelName,
       "cooInsuranceCompanyName": cooInsuranceCompanyName,
       "cooBoxAssetTagName": cooBoxAssetTagName,
       "cooBoxSystemName": cooBoxSystemName,
       "cooBoxCPUSerialNumberName": cooBoxCPUSerialNumberName,
       "cooOperatingSystemUpgradeTypeName": cooOperatingSystemUpgradeTypeName,
       "cooOperatingSystemUpgradePatchLevelName": cooOperatingSystemUpgradePatchLevelName,
       "cooOperatingSystemUpgradeDate": cooOperatingSystemUpgradeDate,
       "cooDepreciationDuration": cooDepreciationDuration,
       "cooDepreciationDurationType": cooDepreciationDurationType,
       "cooDepreciationPercentage": cooDepreciationPercentage,
       "cooDepreciationMethodName": cooDepreciationMethodName,
       "cooRegistrationIsRegistered": cooRegistrationIsRegistered,
       "cooServiceContractTable": cooServiceContractTable,
       "cooServiceContractTableEntry": cooServiceContractTableEntry,
       "cooServiceContractchassisIndex": cooServiceContractchassisIndex,
       "cooServiceContractIndex": cooServiceContractIndex,
       "cooServiceContractState": cooServiceContractState,
       "cooServiceContractWasRenewed": cooServiceContractWasRenewed,
       "cooServiceContractTypeName": cooServiceContractTypeName,
       "cooServiceContractVendorName": cooServiceContractVendorName,
       "cooCostEventLogTable": cooCostEventLogTable,
       "cooCostEventLogTableEntry": cooCostEventLogTableEntry,
       "cooCostEventLogchassisIndex": cooCostEventLogchassisIndex,
       "cooCostEventLogIndex": cooCostEventLogIndex,
       "cooCostEventLogState": cooCostEventLogState,
       "cooCostEventLogDuration": cooCostEventLogDuration,
       "cooCostEventLogDurationType": cooCostEventLogDurationType,
       "cooCostEventLogDescriptionName": cooCostEventLogDescriptionName,
       "cooWarrantyTable": cooWarrantyTable,
       "cooWarrantyTableEntry": cooWarrantyTableEntry,
       "cooWarrantychassisIndex": cooWarrantychassisIndex,
       "cooWarrantyIndex": cooWarrantyIndex,
       "cooWarrantyState": cooWarrantyState,
       "cooWarrantyDuration": cooWarrantyDuration,
       "cooWarrantyDurationType": cooWarrantyDurationType,
       "cooWarrantyEndDateName": cooWarrantyEndDateName,
       "cooWarrantyCost": cooWarrantyCost,
       "cooLeaseInformationTable": cooLeaseInformationTable,
       "cooLeaseInformationTableEntry": cooLeaseInformationTableEntry,
       "cooLeaseInformationchassisIndex": cooLeaseInformationchassisIndex,
       "cooLeaseInformationIndex": cooLeaseInformationIndex,
       "cooLeaseInformationState": cooLeaseInformationState,
       "cooLeaseInformationMultipleSchedules": cooLeaseInformationMultipleSchedules,
       "cooLeaseInformationBuyOutAmount": cooLeaseInformationBuyOutAmount,
       "cooLeaseInformationLeaseRateFactor": cooLeaseInformationLeaseRateFactor,
       "cooLeaseInformationEndDateName": cooLeaseInformationEndDateName,
       "cooLeaseInformationFairMarketValue": cooLeaseInformationFairMarketValue,
       "cooLeaseInformationLessorName": cooLeaseInformationLessorName,
       "cooScheduleNumberTable": cooScheduleNumberTable,
       "cooScheduleNumberTableEntry": cooScheduleNumberTableEntry,
       "cooScheduleNumberchassisIndex": cooScheduleNumberchassisIndex,
       "cooScheduleNumberIndex": cooScheduleNumberIndex,
       "cooScheduleNumberState": cooScheduleNumberState,
       "cooScheduleNumberLeaseInformationIndexReference": cooScheduleNumberLeaseInformationIndexReference,
       "cooScheduleNumberDescriptionName": cooScheduleNumberDescriptionName,
       "cooOptionsTable": cooOptionsTable,
       "cooOptionsTableEntry": cooOptionsTableEntry,
       "cooOptionschassisIndex": cooOptionschassisIndex,
       "cooOptionsIndex": cooOptionsIndex,
       "cooOptionsState": cooOptionsState,
       "cooOptionsLeaseInformationIndexReference": cooOptionsLeaseInformationIndexReference,
       "cooOptionsDescriptionName": cooOptionsDescriptionName,
       "cooMaintenanceTable": cooMaintenanceTable,
       "cooMaintenanceTableEntry": cooMaintenanceTableEntry,
       "cooMaintenancechassisIndex": cooMaintenancechassisIndex,
       "cooMaintenanceIndex": cooMaintenanceIndex,
       "cooMaintenanceState": cooMaintenanceState,
       "cooMaintenanceStartDateName": cooMaintenanceStartDateName,
       "cooMaintenanceEndDateName": cooMaintenanceEndDateName,
       "cooMaintenanceProviderName": cooMaintenanceProviderName,
       "cooMaintenanceRestrictionsName": cooMaintenanceRestrictionsName,
       "cooRepairTable": cooRepairTable,
       "cooRepairTableEntry": cooRepairTableEntry,
       "cooRepairchassisIndex": cooRepairchassisIndex,
       "cooRepairIndex": cooRepairIndex,
       "cooRepairState": cooRepairState,
       "cooRepairCounter": cooRepairCounter,
       "cooRepairVendorName": cooRepairVendorName,
       "cooSupportInformationTable": cooSupportInformationTable,
       "cooSupportInformationTableEntry": cooSupportInformationTableEntry,
       "cooSupportInformationchassisIndex": cooSupportInformationchassisIndex,
       "cooSupportInformationIndex": cooSupportInformationIndex,
       "cooSupportInformationState": cooSupportInformationState,
       "cooSupportInformationIsOutsourced": cooSupportInformationIsOutsourced,
       "cooSupportInformationType": cooSupportInformationType,
       "cooSupportInformationHelpDeskName": cooSupportInformationHelpDeskName,
       "cooSupportInformationFixTypeName": cooSupportInformationFixTypeName,
       "cooTroubleTicketTable": cooTroubleTicketTable,
       "cooTroubleTicketTableEntry": cooTroubleTicketTableEntry,
       "cooTroubleTicketchassisIndex": cooTroubleTicketchassisIndex,
       "cooTroubleTicketIndex": cooTroubleTicketIndex,
       "cooTroubleTicketState": cooTroubleTicketState,
       "cooTroubleTicketSupportInformationIndexReference": cooTroubleTicketSupportInformationIndexReference,
       "cooTroubleTicketNumberName": cooTroubleTicketNumberName,
       "remoteAccessGroup": remoteAccessGroup,
       "remoteAccessTable": remoteAccessTable,
       "remoteAccessTableEntry": remoteAccessTableEntry,
       "remoteAccessChassisIndex": remoteAccessChassisIndex,
       "remoteAccessAdapterIndex": remoteAccessAdapterIndex,
       "remoteAccessType": remoteAccessType,
       "remoteAccessStateCapabilities": remoteAccessStateCapabilities,
       "remoteAccessStateSettings": remoteAccessStateSettings,
       "remoteAccessStatus": remoteAccessStatus,
       "remoteAccessProductInfoName": remoteAccessProductInfoName,
       "remoteAccessDescriptionInfoName": remoteAccessDescriptionInfoName,
       "remoteAccessVersionInfoName": remoteAccessVersionInfoName,
       "remoteAccessControlCapabilities": remoteAccessControlCapabilities,
       "remoteAccessControlSettings": remoteAccessControlSettings,
       "remoteAccessMonitorCapabilities": remoteAccessMonitorCapabilities,
       "remoteAccessMonitorSettings": remoteAccessMonitorSettings,
       "remoteAccessLANCapabilities": remoteAccessLANCapabilities,
       "remoteAccessLANSettings": remoteAccessLANSettings,
       "remoteAccessHostCapabilities": remoteAccessHostCapabilities,
       "remoteAccessHostSettings": remoteAccessHostSettings,
       "remoteAccessOutOfBandSNMPCapabilities": remoteAccessOutOfBandSNMPCapabilities,
       "remoteAccessOutOfBandSNMPSettings": remoteAccessOutOfBandSNMPSettings,
       "remoteAccessSMTPServerIPAddress": remoteAccessSMTPServerIPAddress,
       "remoteAccessFloppyTFTPIPAddress": remoteAccessFloppyTFTPIPAddress,
       "remoteAccessFloppyTFTPPathName": remoteAccessFloppyTFTPPathName,
       "remoteAccessFirmwareUpdateIPAddress": remoteAccessFirmwareUpdateIPAddress,
       "remoteAccessFirmwareUpdatePathName": remoteAccessFirmwareUpdatePathName,
       "remoteAccessNICStaticIPAddress": remoteAccessNICStaticIPAddress,
       "remoteAccessNICStaticNetmaskAddress": remoteAccessNICStaticNetmaskAddress,
       "remoteAccessNICStaticGatewayAddress": remoteAccessNICStaticGatewayAddress,
       "remoteAccessPCMCIAInfoName": remoteAccessPCMCIAInfoName,
       "remoteAccessMiscInfoName": remoteAccessMiscInfoName,
       "remoteAccessNICCurrentIPAddress": remoteAccessNICCurrentIPAddress,
       "remoteAccessNICCurrentNetmaskAddress": remoteAccessNICCurrentNetmaskAddress,
       "remoteAccessNICCurrentGatewayAddress": remoteAccessNICCurrentGatewayAddress,
       "remoteAccessNICCurrentInfoFromDHCP": remoteAccessNICCurrentInfoFromDHCP,
       "remoteUserAdminTable": remoteUserAdminTable,
       "remoteUserAdminTableEntry": remoteUserAdminTableEntry,
       "remoteUserAdminChassisIndex": remoteUserAdminChassisIndex,
       "remoteUserAdminAdapterIndex": remoteUserAdminAdapterIndex,
       "remoteUserAdminUserIndex": remoteUserAdminUserIndex,
       "remoteUserAdminStateCapabilities": remoteUserAdminStateCapabilities,
       "remoteUserAdminStateSettings": remoteUserAdminStateSettings,
       "remoteUserAdminStatus": remoteUserAdminStatus,
       "remoteUserAdminUserName": remoteUserAdminUserName,
       "remoteUserAdminUserPasswordName": remoteUserAdminUserPasswordName,
       "remoteUserAdminUserPrivilege": remoteUserAdminUserPrivilege,
       "remoteUserAdminUserPrivilegeCapabilities": remoteUserAdminUserPrivilegeCapabilities,
       "remoteUserAdminAlertFilterDrsEventsMask": remoteUserAdminAlertFilterDrsEventsMask,
       "remoteUserAdminAlertFilterSysEventsMask": remoteUserAdminAlertFilterSysEventsMask,
       "remoteUserAdminAlertFilterDrsCapabilities": remoteUserAdminAlertFilterDrsCapabilities,
       "remoteUserAdminAlertFilterSysCapabilities": remoteUserAdminAlertFilterSysCapabilities,
       "remoteUserAdminPagerNumericNumberName": remoteUserAdminPagerNumericNumberName,
       "remoteUserAdminPagerNumericMessageName": remoteUserAdminPagerNumericMessageName,
       "remoteUserAdminPagerNumericHangupDelay": remoteUserAdminPagerNumericHangupDelay,
       "remoteUserAdminPagerAlphaPhoneNumberName": remoteUserAdminPagerAlphaPhoneNumberName,
       "remoteUserAdminPagerAlphaProtocol": remoteUserAdminPagerAlphaProtocol,
       "remoteUserAdminPagerAlphaBaudRate": remoteUserAdminPagerAlphaBaudRate,
       "remoteUserAdminPagerAlphaCustomMessageName": remoteUserAdminPagerAlphaCustomMessageName,
       "remoteUserAdminPagerAlphaModemConnectTimeout": remoteUserAdminPagerAlphaModemConnectTimeout,
       "remoteUserAdminPagerAlphaPagerIdName": remoteUserAdminPagerAlphaPagerIdName,
       "remoteUserAdminPagerAlphaPasswordName": remoteUserAdminPagerAlphaPasswordName,
       "remoteUserAdminPagerModemInitStringName": remoteUserAdminPagerModemInitStringName,
       "remoteUserAdminPagerModemPort": remoteUserAdminPagerModemPort,
       "remoteUserAdminEmailAddressName": remoteUserAdminEmailAddressName,
       "remoteUserAdminEmailCustomMessageName": remoteUserAdminEmailCustomMessageName,
       "remoteUserAdminControlCapabilities": remoteUserAdminControlCapabilities,
       "remoteUserAdminControlSettings": remoteUserAdminControlSettings,
       "remoteUserAdminUserType": remoteUserAdminUserType,
       "remoteSNMPTrapTable": remoteSNMPTrapTable,
       "remoteSNMPTrapTableEntry": remoteSNMPTrapTableEntry,
       "remoteSNMPTrapChassisIndex": remoteSNMPTrapChassisIndex,
       "remoteSNMPTrapAdapterIndex": remoteSNMPTrapAdapterIndex,
       "remoteSNMPTrapIndex": remoteSNMPTrapIndex,
       "remoteSNMPTrapStateCapabilities": remoteSNMPTrapStateCapabilities,
       "remoteSNMPTrapStateSettings": remoteSNMPTrapStateSettings,
       "remoteSNMPTrapStatus": remoteSNMPTrapStatus,
       "remoteSNMPTrapDestinationIPAddress": remoteSNMPTrapDestinationIPAddress,
       "remoteSNMPTrapSNMPCommunityName": remoteSNMPTrapSNMPCommunityName,
       "remoteSNMPTrapFilterDrsEventsMask": remoteSNMPTrapFilterDrsEventsMask,
       "remoteSNMPTrapFilterSysEventsMask": remoteSNMPTrapFilterSysEventsMask,
       "remoteSNMPTrapFilterDrsCapabilities": remoteSNMPTrapFilterDrsCapabilities,
       "remoteSNMPTrapFilterSysCapabilities": remoteSNMPTrapFilterSysCapabilities,
       "remoteSNMPTrapControlCapabilities": remoteSNMPTrapControlCapabilities,
       "remoteSNMPTrapControlSettings": remoteSNMPTrapControlSettings,
       "remoteDialUpTable": remoteDialUpTable,
       "remoteDialUpTableEntry": remoteDialUpTableEntry,
       "remoteDialUpChassisIndex": remoteDialUpChassisIndex,
       "remoteDialUpAdapterIndex": remoteDialUpAdapterIndex,
       "remoteDialUpIndex": remoteDialUpIndex,
       "remoteDialUpStateCapabilities": remoteDialUpStateCapabilities,
       "remoteDialUpStateSettings": remoteDialUpStateSettings,
       "remoteDialUpStatus": remoteDialUpStatus,
       "remoteDialUpPPPDialInBaseIPAddress": remoteDialUpPPPDialInBaseIPAddress,
       "remoteDialUpPPPDialInIdleTimeout": remoteDialUpPPPDialInIdleTimeout,
       "remoteDialUpPPPDialInMaxConnectTimeout": remoteDialUpPPPDialInMaxConnectTimeout,
       "remoteDialUpDialOutModemConnectTimeout": remoteDialUpDialOutModemConnectTimeout,
       "remoteDialUpModemDialType": remoteDialUpModemDialType,
       "remoteDialUpModemInitStringName": remoteDialUpModemInitStringName,
       "remoteDialUpModemBaudRate": remoteDialUpModemBaudRate,
       "remoteDialUpModemPort": remoteDialUpModemPort,
       "remoteUserDialInCfgTable": remoteUserDialInCfgTable,
       "remoteUserDialInCfgTableEntry": remoteUserDialInCfgTableEntry,
       "remoteUserDialInCfgChassisIndex": remoteUserDialInCfgChassisIndex,
       "remoteUserDialInCfgAdapterIndex": remoteUserDialInCfgAdapterIndex,
       "remoteUserDialInCfgUserIndex": remoteUserDialInCfgUserIndex,
       "remoteUserDialInCfgStateCapabilities": remoteUserDialInCfgStateCapabilities,
       "remoteUserDialInCfgStateSettings": remoteUserDialInCfgStateSettings,
       "remoteUserDialInCfgStatus": remoteUserDialInCfgStatus,
       "remoteUserDialInCfgPPPUserName": remoteUserDialInCfgPPPUserName,
       "remoteUserDialInCfgPPPUserPasswordName": remoteUserDialInCfgPPPUserPasswordName,
       "remoteUserDialInCfgCallbackPhoneNumberName": remoteUserDialInCfgCallbackPhoneNumberName,
       "remoteDialOutTable": remoteDialOutTable,
       "remoteDialOutTableEntry": remoteDialOutTableEntry,
       "remoteDialOutChassisIndex": remoteDialOutChassisIndex,
       "remoteDialOutAdapterIndex": remoteDialOutAdapterIndex,
       "remoteDialOutDialOutIndex": remoteDialOutDialOutIndex,
       "remoteDialOutStateCapabilities": remoteDialOutStateCapabilities,
       "remoteDialOutStateSettings": remoteDialOutStateSettings,
       "remoteDialOutStatus": remoteDialOutStatus,
       "remoteDialOutIPAddress": remoteDialOutIPAddress,
       "remoteDialOutPhoneNumberName": remoteDialOutPhoneNumberName,
       "remoteDialOutPPPUserName": remoteDialOutPPPUserName,
       "remoteDialOutPPPPasswordName": remoteDialOutPPPPasswordName,
       "alertGroup": alertGroup,
       "alertVariables": alertVariables,
       "alertSystem": alertSystem,
       "alertTableIndexOID": alertTableIndexOID,
       "alertMessage": alertMessage,
       "alertCurrentStatus": alertCurrentStatus,
       "alertPreviousStatus": alertPreviousStatus,
       "alertData": alertData,
       "drsOutOfBandGroup": drsOutOfBandGroup}
)
