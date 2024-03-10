"""SNMP MIB module (XEROX-HOST-RESOURCES-EXT-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-HOST-RESOURCES-EXT-TC
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:09 2024
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

(TimeTicks,
 Integer32,
 ModuleIdentity,
 Gauge32,
 Unsigned32,
 IpAddress,
 MibIdentifier,
 iso,
 Counter64,
 Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ObjectIdentity,
 Bits,
 NotificationType) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "Integer32",
    "ModuleIdentity",
    "Gauge32",
    "Unsigned32",
    "IpAddress",
    "MibIdentifier",
    "iso",
    "Counter64",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ObjectIdentity",
    "Bits",
    "NotificationType")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmHrTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52)
)
xcmHrTC.setLastUpdated("1110120000Z")
if mibBuilder.loadTexts:
    xcmHrTC.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmHrTC.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmHrTC.setDescription("""\
Version: 6.001.pub The TC module for textual conventions, enumerated types,
OIDs, and other volatile elements of the companion Host Resources Extensions
MIB ('xcmHrMIB'), which supports extended configuration and management of
various host resources for network accessible host systems. These modules
augment and extend the original IETF Host Resources MIB (RFC 2790). Usage: This
MIB module introduces support for the 'realization' of both 'physical' and
'logical' devices, consistent with ISO DPA (Document Printing Application),
ISO/IEC 10175, as reflected in the object 'xcmHrDevInfoRealization'. Note:
Conforming implementations SHALL NOT 'bubble up' status from 'physical' devices
to associated 'logical' devices. All devices SHALL report their own status
ONLY. See: Section 9 'Supplement' in XCMI Extensions to IETF Host Resources TC,
for implementation guidance for this TC module. Copyright (C) 1995-2009 Xerox
Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmHrDevCalendarDayOfWeek(TextualConvention, Integer32):
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
        *(("businessClosedDay", 10),
          ("businessHoliday", 11),
          ("businessOpenDay", 9),
          ("everyDay", 8),
          ("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

    if mibBuilder.loadTexts:
        description = """\
The day of week when the command specified in a conceptual row in the
'xcmHrDevCalendarTable' SHALL be invoked.
"""


class XcmHrDevCalendarTimeOfDay(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12359),
    )

    if mibBuilder.loadTexts:
        description = """\
The time of day when the command specified in a conceptual row in the
'xcmHrDevCalendarTable' SHALL be invoked, specified as hours (0..23) multiplied
by 100, added to minutes (0..59), added to a constant bias of 10000 (avoids an
index value of zero in 'xcmHrDevCalendarTimeOfDay').
"""


class XcmHrDevDetailType(TextualConvention, Integer32):
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
              41,
              42,
              43,
              44,
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
              63,
              64,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              130,
              140,
              160,
              161,
              162,
              163,
              170,
              180,
              181,
              191,
              192,
              193,
              194,
              200,
              201,
              202,
              203,
              204,
              210,
              211,
              212,
              213,
              220,
              221,
              230,
              231,
              232,
              235,
              240,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              260,
              270,
              280,
              281,
              500,
              501,
              502,
              503)
        )
    )
    namedValues = NamedValues(
        *(("deviceAccountingUsage", 30),
          ("deviceAlias", 4),
          ("deviceAlienJobPolicy", 201),
          ("deviceCPMenuControl", 235),
          ("deviceCancelDocSupport", 76),
          ("deviceConfigurationSetting", 180),
          ("deviceContext", 9),
          ("deviceDaysUntilMaximumMsg", 28),
          ("deviceDaysUntilReorderMsg", 25),
          ("deviceDaysUntilReplaceMsg", 27),
          ("deviceDaysUntilWarningMsg", 26),
          ("deviceDeltaServiceUsage", 231),
          ("deviceDescription", 6),
          ("deviceDiskStorageAccess", 160),
          ("deviceDiskStorageCapacity", 163),
          ("deviceDiskStorageMedia", 161),
          ("deviceDiskStorageRemovable", 162),
          ("deviceEnergyStarSuspendMode", 125),
          ("deviceEventLogFullPolicy", 202),
          ("deviceFaxCountry", 280),
          ("deviceFaxDialType", 281),
          ("deviceFeatureInstallationKeyAvailability", 501),
          ("deviceFeatureInstallationKeyDate", 503),
          ("deviceFeatureInstallationKeyDisablement", 502),
          ("deviceFeedResolutionSupport", 86),
          ("deviceFontIndexReady", 101),
          ("deviceFontIndexSupport", 100),
          ("deviceForeignJobsVisible", 77),
          ("deviceGuestJobPolicy", 200),
          ("deviceHelpAddress", 61),
          ("deviceHelpDescription", 62),
          ("deviceHelpLocation", 63),
          ("deviceHelpName", 60),
          ("deviceHelpURI", 64),
          ("deviceID", 7),
          ("deviceInitialValueDocDefault", 79),
          ("deviceInitialValueDocSupport", 74),
          ("deviceInitialValueJobDefault", 78),
          ("deviceInitialValueJobSupport", 73),
          ("deviceInputMaxSpeed", 82),
          ("deviceInputMaxSpeedTimeUnit", 81),
          ("deviceInputMaxSpeedTrafficUnit", 80),
          ("deviceInstallDate", 260),
          ("deviceInstallationKeyCSVPrintSubmission", 500),
          ("deviceJobHistoryDeviceIndex", 99),
          ("deviceJobHoldDeleteTimeout", 193),
          ("deviceJobIncompleteTimeout", 191),
          ("deviceJobLogFullPolicy", 203),
          ("deviceJobPauseResumeTimeout", 194),
          ("deviceJobProgrammingTimeout", 192),
          ("deviceJobServiceDeviceIndex", 98),
          ("deviceLifeRemainingPercent", 251),
          ("deviceLifetimeAvgCoverage", 250),
          ("deviceLifetimeErrorCount", 35),
          ("deviceLifetimeErrorLimit", 36),
          ("deviceLifetimeMsgDisplay", 29),
          ("deviceLifetimeUsage", 20),
          ("deviceLifetimeWarningCount", 37),
          ("deviceLifetimeWarningLimit", 38),
          ("deviceLogicalIndexReady", 97),
          ("deviceLogicalIndexSupport", 96),
          ("deviceLogicalNameReady", 93),
          ("deviceLogicalNameSupport", 92),
          ("deviceManufacturer", 10),
          ("deviceManufacturerURI", 220),
          ("deviceMaximumLifetimeLimit", 24),
          ("deviceMaximumMsgSentDate", 54),
          ("deviceMaximumOnDate", 34),
          ("deviceMemorySize", 170),
          ("deviceModel", 11),
          ("deviceModelDescription", 212),
          ("deviceModelName", 211),
          ("deviceModelNumber", 213),
          ("deviceModelURI", 221),
          ("deviceMultipleDocSupport", 75),
          ("deviceName", 3),
          ("deviceNetworkIfIndex", 140),
          ("deviceNextCoolerModeIndex", 124),
          ("deviceNextWarmerModeIndex", 123),
          ("deviceOutputMaxSpeed", 85),
          ("deviceOutputMaxSpeedTimeUnit", 84),
          ("deviceOutputMaxSpeedTrafficUnit", 83),
          ("devicePhysicalIndexReady", 95),
          ("devicePhysicalIndexSupport", 94),
          ("devicePhysicalNameReady", 91),
          ("devicePhysicalNameSupport", 90),
          ("devicePowerCoolerDelay", 119),
          ("devicePowerCoolerDuration", 120),
          ("devicePowerCoolerSupport", 116),
          ("devicePowerCoolerTrigger", 122),
          ("devicePowerModeDescription", 112),
          ("devicePowerModeName", 110),
          ("devicePowerModeSupport", 113),
          ("devicePowerModeType", 111),
          ("devicePowerTimeUnit", 114),
          ("devicePowerWarmerDelay", 117),
          ("devicePowerWarmerDuration", 118),
          ("devicePowerWarmerSupport", 115),
          ("devicePowerWarmerTrigger", 121),
          ("deviceProcessorFrwID", 130),
          ("deviceRemainingImpressions", 252),
          ("deviceReorderConfirmDate", 56),
          ("deviceReorderLifetimeLimit", 21),
          ("deviceReorderMsgSentDate", 51),
          ("deviceReorderOnDate", 31),
          ("deviceReorderToVendorDate", 55),
          ("deviceReplaceByCustomer", 16),
          ("deviceReplaceByWarranty", 19),
          ("deviceReplaceDate", 57),
          ("deviceReplaceLifetimeLimit", 23),
          ("deviceReplaceMsgSentDate", 53),
          ("deviceReplaceOnDate", 33),
          ("deviceReplaceSystemUsage", 58),
          ("deviceReplaceWithGeneric", 59),
          ("deviceRequestLogFullPolicy", 204),
          ("deviceResourceIndexReady", 103),
          ("deviceResourceIndexSupport", 102),
          ("deviceRolloverValue", 232),
          ("deviceSchedulerReady", 89),
          ("deviceSchedulerSupport", 88),
          ("deviceSerialNumber", 12),
          ("deviceServiceByCustomer", 15),
          ("deviceServicePlanName", 17),
          ("deviceServicePlanPassword", 18),
          ("deviceServiceUsage", 230),
          ("deviceStatus", 270),
          ("deviceSuppliesClass", 253),
          ("deviceSuppliesCurrentLevel", 256),
          ("deviceSuppliesMaxCapacity", 255),
          ("deviceSupplyUnit", 254),
          ("deviceTimezone", 181),
          ("deviceTranslatorReady", 72),
          ("deviceTranslatorSupport", 71),
          ("deviceTree", 8),
          ("deviceTriggerDaysForMaximum", 44),
          ("deviceTriggerDaysForReorder", 41),
          ("deviceTriggerDaysForReplace", 43),
          ("deviceTriggerDaysForWarning", 42),
          ("deviceType", 5),
          ("deviceUniversalProductCode", 210),
          ("deviceUsageWarningThreshold", 240),
          ("deviceVendor", 13),
          ("deviceVersion", 14),
          ("deviceWarningLifetimeLimit", 22),
          ("deviceWarningMsgSentDate", 52),
          ("deviceWarningOnDate", 32),
          ("deviceXFeedResolutionSupport", 87),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of the device detail information specified in this conceptual row in
the 'xcmHrDevDetailTable'. Usage: Conforming management stations and management
agents SHALL implement specified semantics for device detail types.
"""


class XcmHrDevDetailUnitClass(TextualConvention, Integer32):
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("classDateAndTime", 4),
          ("classGenOptionValueSyntax", 3),
          ("classHrDevCalendarDayOfWeek", 5),
          ("classHrDevCalendarTimeOfDay", 6),
          ("classHrDevInfoStatus", 14),
          ("classHrDevInfoStatusMask", 15),
          ("classHrDevInfoXStatus", 16),
          ("classHrDevMgmtCommandRequest", 7),
          ("classHrDevPowerTimeUnit", 8),
          ("classHrDevTrafficUnit", 9),
          ("classHrDpaAvailability", 19),
          ("classHrDpaConditions", 18),
          ("classHrDpaJobValidateSupport", 21),
          ("classHrDpaObjectClassSupport", 20),
          ("classHrDpaState", 17),
          ("classJMJobState", 22),
          ("classJMJobStateMask", 23),
          ("classLogFullPolicy", 12),
          ("classLogFullPolicyMask", 13),
          ("classRowPersistence", 10),
          ("classRowPersistenceMask", 11),
          ("classSecGuestJobPolicy", 24),
          ("classSecGuestJobPolicyMask", 25),
          ("classSecPosixRights", 26),
          ("classSecPosixVerbs", 27),
          ("classSvcMonAttachmentPDLSupport", 29),
          ("classSvcMonJobConfirmSupport", 28),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The value unit class of the device detail information specified in this
conceptual row in the 'xcmHrDevDetailTable'. Usage: Used to select a textual
convention for specifying the units of this device detail value. Usage: Some of
the value unit class enumerations specify that the actual unit is REQUIRED to
be selected in '...DetailUnit' and REQUIRE '...DetailValueString' contains a
value in units (and are commented as such below). Usage: Some of the value unit
class enumerations specify the actual unit DIRECTLY and REQUIRE that
'...DetailUnit' be zero and REQUIRE '...DetailValueString' contains a value in
the named textual convention (or a bit-mask derived from it) (and are commented
as such below). Usage: Some of the value unit class enumerations specify that
'...DetailValueString' SHALL contain a bit-mask which is formed via the bit-
wise OR of '2**(n)', where (n) is each selected enumerated value in the named
textual convention. (see 'xcmGenBaseSNMPDomainSupport' object in XCMI General
MIB).
"""


class XcmHrDevInfoRealization(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("logical", 12),
          ("logicalAndPhysical", 13),
          ("other", 1),
          ("physical", 11),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
An extended device type (or device 'realization'), used by system
administrators and end users of this device. Usage: The use of either 'other'
or 'unknown' is uninformative and SHOULD be avoided by conforming
implementations. * 'physical' - 'real' device installed on this managed system;
* 'logical' - 'virtual' device configured on this managed system; *
'logicalAndPhysical' - 'combined' device (from ISO DPA ??).
"""


class XcmHrDevInfoStatus(TextualConvention, Integer32):
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
        *(("down", 5),
          ("running", 2),
          ("testing", 4),
          ("unknown", 1),
          ("warning", 3))
    )

    if mibBuilder.loadTexts:
        description = """\
The current operational state of the device described by this row of the table.
A value 'unknown(1)' indicates that the current state of the device is unknown.
'running(2)' indicates that the device is up and running and that no unusual
error conditions are known. The 'warning(3)' state indicates that agent has
been informed of an unusual error condition by the operational software (eg, a
disk device driver) but that the device is still 'operational'. An example
would be a high number of soft errors on a disk. A value of 'testing(4)',
indicates that the device is not available for use because it is in the testing
state. The state of 'down(5)' is used only when the agent has been informed
that the device is not available for any use. Usage: Conforming implementations
SHALL NOT 'bubble up' status from 'physical' devices to associated 'logical'
devices. All devices SHALL report their own status ONLY. Usage: Devices in the
'down' state SHOULD NOT be accepting new work (or still processing old work).
Devices in the 'running' state SHOULD be prepared to accept new work. Usage:
The use of the state 'unknown' is uninformative and SHOULD be avoided by
conforming implementations. Usage: This is a textual convention representation
of the 'hrDeviceStatus' enumeration in the IETF Host Resources MIB (RFC 2790),
rewritten from SMIv1 style (RFCs 1155 and 1212) into SMIv2 style (RFCs
1902/2578, 1903/2579, and 1904/2580).
"""


class XcmHrDevInfoXStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              99,
              100,
              200,
              300,
              400,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              600,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              10100,
              10200,
              10300,
              10400,
              10500,
              11100,
              11200,
              11300,
              11400,
              11500,
              11600,
              11700,
              11800,
              11900,
              12000,
              12100,
              12200,
              12300,
              20000,
              20001,
              20002,
              20003,
              20004,
              20005,
              20006,
              40000)
        )
    )
    namedValues = NamedValues(
        *(("accountingInterfaceNone", 12300),
          ("audioNone", 1100),
          ("clockNone", 1900),
          ("commonLast", 99),
          ("commonNone", 0),
          ("commonOther", 1),
          ("commonUnknown", 2),
          ("copierNone", 10300),
          ("coprocessorNone", 1200),
          ("cruFault", 20006),
          ("cruNone", 20000),
          ("cruOther", 20001),
          ("cruReady", 20003),
          ("cruReorder", 20004),
          ("cruReplace", 20005),
          ("cruUnknown", 20002),
          ("diskStorageNone", 600),
          ("embeddedFaxNone", 12000),
          ("faxNone", 10400),
          ("finisher3rdPartyNone", 11500),
          ("finisherBFMNone", 11200),
          ("finisherMFFNone", 11300),
          ("finisherXIMNone", 11400),
          ("foreignInterfaceNone", 12100),
          ("hostSystemNone", 10100),
          ("internetFaxNone", 11800),
          ("interposerNone", 11700),
          ("keyboardNone", 1300),
          ("mailboxNone", 10500),
          ("markerNone", 11100),
          ("modemNone", 1400),
          ("networkNone", 400),
          ("nonVolatileMemoryNone", 2100),
          ("otherNone", 100),
          ("parallelPortNone", 1500),
          ("paymentInterfaceNone", 11600),
          ("pointingNone", 1600),
          ("printerConnectingToPrinter", 513),
          ("printerIdle", 503),
          ("printerJobEndWait", 509),
          ("printerJobPasswordWait", 511),
          ("printerJobStartWait", 508),
          ("printerNeedsAttention", 505),
          ("printerNeedsKeyOperator", 510),
          ("printerNone", 500),
          ("printerOther", 501),
          ("printerPaused", 506),
          ("printerPrinting", 504),
          ("printerShutdown", 507),
          ("printerTimedOut", 512),
          ("printerUnknown", 502),
          ("processorNone", 300),
          ("reserved", 40000),
          ("scannerNone", 10200),
          ("securityInterfaceNone", 12200),
          ("serialPortNone", 1700),
          ("serverFaxNone", 11900),
          ("tapeNone", 1800),
          ("unknownNone", 200),
          ("videoNone", 1000),
          ("volatileMemoryNone", 2000))
    )

    if mibBuilder.loadTexts:
        description = """\
An extended device status, used by system administrators and end users of this
device (here, read 'state' for 'status'). Usage: Conforming implementations
SHALL NOT 'bubble up' status from 'physical' devices to associated 'logical'
devices. All devices SHALL report their own status ONLY. Usage: Exactly one
enumeration of extended device status SHALL be defined, with ranges for each
basic device type (eg, 'hrDevicePrinter'). The legal range for extended device
status for a given device type (either defined by RFC 2790 or by this MIB) is
found by multiplying the final arc of the the device type OID by 100 - the
result is the device specific range base - the end of the device specific range
is 99 larger. These device specific extended device status values SHALL be
reissued periodically in the 'XcmHrDevInfoXStatus' textual convention.
"""


class XcmHrDevInfoConditions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
A relatively generic description of the current 'conditions' of this device,
specified in a bit-mask. 1 : startupInProgress -- 2**0 2 :
resetWarningInProgresss -- 2**1 (optional) 4 : testInProgress -- 2**2 8 :
shutdownInProgress -- 2**3 (optional) 16 : quiesceInProgress -- 2**4 (optional)
32 : resetCountersInProgress -- 2**5 (optional) 64 : resetWarmInProgress --
2**6 128 : resetColdInProgress -- 2**7 256 : resetFactoryInProgress -- 2**8 512
: flushInputInProgress -- 2**9 1024 : flushOutputInProgress -- 2**10 2048 :
flushInOutInProgress -- 2**11 4096 : manageInProgress -- 2**12 (optional) The
above basic 'conditions' record the original intent of the current command,
when it results in delayed state transitions before arriving at the 'target'
state. They augment the state information available from 'hrDeviceStatus'. 8192
: warmUpDelayInProgress -- 2**13 (optional) 16384 : warmUpCycleInProgress --
2**14 (optional) 32768 : readyMode -- 2**15 (optional) 65536 :
coolDownDelayInProgress -- 2**16 (optional) 131072 : coolDownCycleInProgress --
2**17 (optional) 262144 : standbyMode -- 2**18 (optional) 524288 :
energySaveDelayInProgress -- 2**19 (optional) 1048576 :
energySaveCycleInProgress -- 2**20 (optional) 2097152 : sleepMode -- 2**21
(optional) 4194304 : wakeUpDelayInProgress -- 2**22 (optional) 8388608 :
wakeUpCycleInProgress -- 2**23 (optional) 16777216 : powerToReadyInProgress --
2**24 (optional) 33554432 : powerToStandbyInProgress -- 2**25 (optional)
67108864 : powerToSleepInProgress -- 2**26 (optional) The above optional
'conditions' record the progress of device 'warm up', 'cool down', 'energy
save', and 'wake up' power mgmt cycles and also define the device 'readyMode',
'standbyMode', and 'sleepMode' qualifiers to the generic 'hrDeviceStatus' of
'running(2)', 'warning(3)', or 'testing(4)' (but NOT 'down(5)'). See the power
management cycle feature support and feature time objects in the Device Power
Group of the Host Resources Ext MIB. Usage: It is desirable that the
implementor report 'conditions' of all devices corresponding to conceptual rows
in the 'hrDeviceTable' as accurately as feasible. 'Conditions' occur within or
across 'states' in a finite state machine (FSM) implementation of a device.
They represent both short term and long term conditions. Usage: A device with
'hrDeviceStatus' of 'running(2)' might have 'xcmHrDevInfoConditions' of
'quiesceInProgress', indicating that the device will soon transition to
'hrDeviceStatus' of 'down(5)'. Usage: A multi-bit example of
'xcmHrDevInfoConditions' is 'quiesceInProgress' concurrently with
'standbyMode', ie, the device has previously 'cooled down' and will soon
transition from 'hrDeviceStatus' of 'running(2)' to 'down(5)'.
"""


class XcmHrDevInfoXConditions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
A device specific description of the extended 'conditions' of this device,
specified in a bit-mask. Usage: For FUTURE expansion. Usage: Exactly one bit
mask of extended device conditions SHALL be defined for each basic device type
(eg, 'hrDevicePrinter'). These device specific extended device conditions
values SHALL be reissued periodically in the 'XcmHrDevInfoXConditions' textual
convention. These device specific extended device conditions are mutually
exclusive and 'overloaded' in the single reporting object
'xcmHrDevInfoXConditions'.
"""


class XcmHrDeviceStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("supplyMissing", 6),
          ("supplyReorder", 3),
          ("supplyReplace", 5),
          ("unknown", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
Used to describe the device status. Usage: used in xcmHrDetailTable for
supplies. Required because supplies are not in the hrDeviceTable and therefore
hrDeviceStatus cannot be used. Modeled after hrDeviceStatus where 2=running,
3=warning and 5=down.
"""


class XcmHrDevMgmtCommandRequest(TextualConvention, Integer32):
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
              1301,
              1302,
              1303,
              1304,
              1305,
              1306,
              1307,
              1308,
              1309,
              1310,
              1311,
              1312,
              1901,
              1902,
              1903,
              1904,
              1905,
              1906,
              1907,
              1908,
              1909,
              1910,
              1911,
              1912,
              2301,
              2302,
              2321,
              2322,
              2323,
              2324,
              2325,
              2326,
              2331,
              2332,
              2333,
              2334,
              2335,
              2336,
              2341,
              2342,
              2343,
              2901,
              2902,
              2921,
              2922,
              2923,
              2924,
              2925,
              2926,
              2931,
              2932,
              2933,
              2934,
              2935,
              2936,
              2941,
              2942)
        )
    )
    namedValues = NamedValues(
        *(("coolDown", 17),
          ("deviceBackup", 2323),
          ("deviceClean", 1305),
          ("deviceConfigure", 2325),
          ("deviceCreate", 1301),
          ("deviceDelete", 1302),
          ("deviceDiagnose", 2326),
          ("deviceDisable", 1306),
          ("deviceDiskOverwrite", 2343),
          ("deviceEnable", 1307),
          ("deviceFormat", 2335),
          ("deviceInstall", 2321),
          ("deviceJobCreate", 1312),
          ("deviceList", 1303),
          ("deviceLogin", 2341),
          ("deviceLogout", 2342),
          ("deviceManage", 2301),
          ("devicePause", 1308),
          ("deviceQueueList", 1311),
          ("deviceRefresh", 2336),
          ("deviceResetCold", 2333),
          ("deviceResetCounters", 2331),
          ("deviceResetFactory", 2334),
          ("deviceResetWarm", 2332),
          ("deviceRestart", 2302),
          ("deviceRestore", 2324),
          ("deviceResume", 1309),
          ("deviceSet", 1304),
          ("deviceShutdown", 1310),
          ("deviceUpgrade", 2322),
          ("energySave", 18),
          ("entityBackup", 2923),
          ("entityClean", 1905),
          ("entityConfigure", 2925),
          ("entityCreate", 1901),
          ("entityDelete", 1902),
          ("entityDiagnose", 2926),
          ("entityDisable", 1906),
          ("entityEnable", 1907),
          ("entityFormat", 2935),
          ("entityInstall", 2921),
          ("entityJobCreate", 1912),
          ("entityList", 1903),
          ("entityLogin", 2941),
          ("entityLogout", 2942),
          ("entityManage", 2901),
          ("entityPause", 1908),
          ("entityQueueList", 1911),
          ("entityRefresh", 2936),
          ("entityResetCold", 2933),
          ("entityResetCounters", 2931),
          ("entityResetFactory", 2934),
          ("entityResetWarm", 2932),
          ("entityRestart", 2902),
          ("entityRestore", 2924),
          ("entityResume", 1909),
          ("entitySet", 1904),
          ("entityShutdown", 1910),
          ("entityUpgrade", 2922),
          ("flushInOut", 13),
          ("flushInput", 11),
          ("flushOutput", 12),
          ("manage", 14),
          ("none", 1),
          ("powerToReady", 20),
          ("powerToSleep", 22),
          ("powerToStandby", 21),
          ("quiesce", 6),
          ("refresh", 15),
          ("resetCold", 9),
          ("resetCounters", 7),
          ("resetFactory", 10),
          ("resetWarm", 8),
          ("resetWarning", 3),
          ("shutdown", 5),
          ("startup", 2),
          ("test", 4),
          ("wakeUp", 19),
          ("warmUp", 16))
    )

    if mibBuilder.loadTexts:
        description = """\
A write of this type by an (authorized) management station invokes a command
for this device. A read of this type always returns the command currently in
progress or last completed. It is mandatory that a conforming management agent
ensure that the contents of this object remain 'in bounds' - an undefined value
SHALL be replaced by 'none' - ie, although rejected with error in the
SetResponse PDU, this object SHALL NOT contain any such undefined value. At
system initialization, this object SHALL contain 'none'. * 'none' - NO
action(s) SHALL be taken, except to clear '...CommandData' and set
'...CommandStatus' to 'noError'. * 'test' or 'manage' - the associated
'...CommandData' object SHOULD/SHALL be specified in the same SetRequest PDU. *
all other commands - the associated '...CommandData' object MAY be specified in
the same SetRequest PDU. * 'startup', 'resetWarm', 'resetCold', or
'resetFactory' - the final state SHALL be 'running' (after cycle completes) -
the sequence of states SHOULD be 'down' -> 'testing' -> 'running' - the final
power mode SHALL be 'ready'. * 'startup' - this device SHALL transition from
the 'down' state to the 'running' state and 'ready' power mode. *
'resetWarning' - this device SHALL transition from the 'warning' state to the
'running' state (because a management station has acknowledged the management
agent's previous warning). * 'test' - this device SHALL transition immediately
(ie, without attempting graceful quiesce) to the 'testing' state; it is a local
matter (ie, device specific) how this command is processed; however,
'...CommandData' SHOULD be specified. * 'shutdown' - this device SHALL
transition immediately (ie, without attempting graceful quiesce) to the 'down'
state and 'off' power mode. * 'quiesce' - this device MAY transition gracefully
to the 'down' state, or it MAY choose to treat a 'quiesce' as 'shutdown'. *
'resetCounters' - all device counters SHALL be reset to zero and the device
SHALL remain in the same state and power mode. * 'resetWarm' - a device 'warm
restart' SHALL be performed (ie, without a power cycle reset). * 'resetCold' -
a device 'cold restart' SHALL be performed (ie, with a power cycle reset). *
'resetFactory' - all factory defaults SHALL be restored, and a device 'cold
restart' SHALL be performed (ie, with a power cycle reset). * 'flushInput' -
all device input (in progress or internally queued) SHALL be gracefully
flushed. * 'flushOutput' - all device output (in progress or internally queued)
SHALL be gracefully flushed. * 'flushInOut' - all device input and output
output (in progress or internally queued) SHALL be gracefully flushed. *
'manage' - it is a local matter (ie, device specific) how this command is
processed; however, '...CommandData' SHALL be specified. * 'refresh' - the
device SHALL promptly read all of its manageable configuration parameters, but
SHALL NOT perform a reset. * 'warmUp' - the device SHALL transition from the
'standby' mode to the 'ready' mode - invalid from any other power mode
(optional command for remote device power management). * 'coolDown' - the
device SHALL transition from the 'ready' mode to the 'standby' mode - invalid
from any other power mode (optional command for remote device power
management). * 'energySave' - the device SHALL transition from the 'standby'
mode to the 'sleep' mode - invalid from any other power mode (optional command
for remote device power management). * 'wakeUp' - the device SHALL transition
from the 'sleep' mode to the 'standby' mode - invalid from any other power mode
(optional command for remote device power management). * 'powerToReady' - the
device SHALL transition from the 'standby' mode or the 'sleep' mode to the
'ready' mode (optional command for remote device power management). *
'powerToStandby' - the device SHALL transition from the 'ready' mode or the
'sleep' mode to the 'standby' mode (optional command for remote device power
management). * 'powerToSleep' - the device SHALL transition from the 'ready'
mode or the 'standby' mode to the 'sleep' mode (optional command for remote
device power management). Note: All of the POSIX and XCMI device level
operations are taken from the POSIX System Admin std (IEEE 1387.4) and aligned
with the high-end XCMI System Admin MIB.
"""


class XcmHrDevMgmtCommandData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
A write of this type specifies: a) a 'test' command subtype and any
accompanying 'test' device specific data; or b) a 'manage' command subtype and
any accompanying 'manage' device specific data; or c) device specific data
accompanying any other command. A read of this type always returns the data (if
any) which accompanied the current or last completed command.
"""


class XcmHrDevMgmtCommandDataTag(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )

    if mibBuilder.loadTexts:
        description = """\
XCMI device management commands are passed as enumerated types in
'xcmHrDevMgmtCommandRequest' in the XCMI HRX MIB. Other XCMI management
commands are passed as enumerated types in 'xcmCommsMgmtCommandRequest',
'xcmSimpleJobMgmtOperation', etc, in the XCMI Comms Engine, Simple Job Mgmt,
and other MIBs. XCMI management commands MAY also require one or more arguments
(in addition to any specific variable bindings of MIB objects). Required
arguments are passed as 'tagged string arguments' in 'xcmHrDevMgmtCommandData',
'xcmSimpleJobMgmtData', etc. Each 'tagged string argument' substring is of the
form: 'TT=value:' where: 'TT' two-character 'tag', naming argument type '='
literal equal sign, beginning argument value 'value' human-readable string,
encoding argument value ':' literal colon, terminating argument value XCMI
conforming management stations SHALL terminate ALL 'tagged string argument'
substrings properly with colon (':'). XCMI standard 'tagged string arguments'
MAY pass colon (':') in their 'value' by escaping it with backslash ('\'). XCMI
conforming management agents SHALL interpret backslash followed by ANY other
character as the literal value of the second character (ie, backslash is
permitted, and is NOT restricted to certain following characters). XCMI
standard 'tags' for data in 'tagged string arguments', (in
'xcmHrDevMgmtCommandData', 'xcmSimpleJobMgmtData', etc) are as follows: --
Generic Data (no object mapping to MIBs) -- For domain-specific future
extensions to operations * SC [Sub-Command - domain-specific, must be FIRST tag
present] -- syntax 'XcmFixedLocaleDisplayString (SIZE (0..255))' -- domain-
specific sub-command for management request -- passed in fixed locale (see
'xcmGenFixedLocalizationIndex') -- passed as character string, NOT as binary
value -- For generic access to any IETF or XCMI defined objects * OI [Object
Identifier - no object mapping] -- syntax 'OBJECT IDENTIFIER' -- object
identifier of object (WITHOUT instance qualifiers) -- passed as dotted decimal
OID or as object label -- (eg, 'hrDeviceID'), NOT as binary object identifier *
OV [Object Value - no object mapping] -- syntax 'XcmFixedLocaleDisplayString
(SIZE (0..255))' -- object value of object -- passed as character string, NOT
as binary value -- passed in fixed locale (see 'xcmGenFixedLocalizationIndex')
-- For protection against 'replay' attacks * DT [Date and Time - no object
mapping] -- (see 'hrSystemDate' in System group of IETF HR MIB) -- syntax
'DateAndTime' -- date and time stamp for management request -- passed as dotted
decimal string (ie, 'yyyy.mm.dd.hh.mm.ss'), -- NOT as binary value * NI [Noise
Information - no object mapping] -- syntax 'XcmFixedLocaleDisplayString (SIZE
(0..255))' -- arbitrary noise info for management request -- passed as
hexadecimal string, NOT as binary value * SI [Sequence Identifier - no object
mapping] -- syntax 'Ordinal32' -- sequence ID for management request (for
'secure streams') -- passed as decimal string, NOT as binary value -- Security
Data from XCMI Security MIB (63sec) -- For account-based authentication * AI
'xcmSecAccountIndex' -- syntax 'Ordinal32' -- index of account (ie, account ID)
-- passed as decimal string, NOT as binary value * AN 'xcmSecAccountName' --
syntax 'XcmFixedLocaleDisplayString (SIZE (0..255))' -- human-readable name of
account (ie, account label) -- passed in fixed locale (see
'xcmGenFixedLocalizationIndex') * AC 'xcmSecAccountPasscode' -- syntax
'XcmFixedLocaleDisplayString (SIZE (0..255))' -- protected numeric password of
account -- passed as hexadecimal string, NOT as binary value -- (protected text
form, NOT cleartext password) * AW 'xcmSecAccountPassword' -- syntax
'XcmFixedLocaleDisplayString (SIZE (0..255))' -- protected alphanumeric
password of account -- passed as hexadecimal string, NOT as binary value --
(protected text form, NOT cleartext password) -- For user-based authentication
* UI 'xcmSecUserIndex' -- syntax 'Ordinal32' -- index of user (ie, user ID) --
passed as decimal string, NOT as binary value * UN 'xcmSecUserName' -- syntax
'XcmFixedLocaleDisplayString (SIZE (0..255))' -- human-readable name of user
(ie, user label) -- passed in fixed locale (see 'xcmGenFixedLocalizationIndex')
* UC 'xcmSecUserPasscode' -- syntax 'XcmFixedLocaleDisplayString (SIZE
(0..255))' -- protected numeric password of user -- passed as hexadecimal
string, NOT as binary value -- (protected text form, NOT cleartext password) *
UW 'xcmSecUserPassword' -- syntax 'XcmFixedLocaleDisplayString (SIZE (0..255))'
-- protected alphanumeric password of user -- passed as hexadecimal string, NOT
as binary value -- (protected text form, NOT cleartext password) -- System
group of IETF MIB-II (RFC 1213) * ZD 'sysDescr' -- syntax 'DisplayString (SIZE
(0..255))' -- (NVT ASCII string) -- textual description of host system, --
passed as ASCII string, NOT as localized string -- (see XCMI MIB Implementer's
Guide for the format -- of sysDescr). -- (see 'hrDeviceDescr' of type
'DisplayString' in IETF HR MIB) * ZI 'sysObjectID' -- syntax 'OBJECT
IDENTIFIER' -- product ID of host system -- passed as dotted decimal OID or as
system product ID label -- (eg, 'xcmPidStarship20'), NOT as binary object
identifier -- (see 'hrDeviceID' of type 'ProductID' in IETF HR MIB) * ZS
'sysServices' -- syntax 'INTEGER (0..127)' -- bit-mask of services host system
offers -- passed as decimal string, NOT as binary value -- Interface group of
IETF MIB-II (RFC 1213) * IX 'ifIndex' -- syntax 'INTEGER (1..2147483647)' --
index of host system interface conceptual row -- (REQUIRED for 'entityCreate')
-- passed as decimal string, NOT as binary index * ID 'ifDescr' -- syntax
'DisplayString (SIZE (0..255))' -- (NVT ASCII string) -- textual description of
host system interface, -- including manufacturer, product name, version of
hardware * IY 'ifType' -- syntax 'INTEGER (1..2147483647)' (enumeration) --
(see 'IANAifType' textual convention in 'IANAifType-MIB') -- type of host
system interface -- passed as decimal string or as interface type enum label --
(eg, 'iso88025-tokenRing'), NOT as binary value * IM 'ifMtu' -- syntax 'INTEGER
(0..2147483647)' -- max transmission unit (datagram) on host system interface
-- passed as decimal string, NOT as binary value * IS 'ifSpeed' -- syntax
'INTEGER (0..2147483647)' -- speed (bits/second) of host system interface --
passed as decimal string, NOT as binary value * IP 'ifPhysAddress' -- syntax
'PhysAddress' -- physical address of host system interface -- passed as
hexadecimal string, NOT as binary value * IZ 'ifSpecific' -- syntax 'OBJECT
IDENTIFIER' -- reference to media-specific MIB for host system interface --
passed as dotted decimal OID or as media-specific MIB label -- (eg, 'EtherLike-
MIB'), NOT as binary value -- System group of IETF HR MIB (RFC 2790) * ZA
'hrSystemDate' -- syntax 'DateAndTime' -- local date and time on host system --
passed as dotted decimal string (ie, 'yyyy.mm.dd.hh.mm.ss'), -- NOT as binary
value * ZL 'hrSystemInitialLoadDevice' -- syntax 'INTEGER (1..2147483647)' --
(see 'hrDeviceIndex' in IETF HR MIB) -- index of 'hrDeviceEntry' for host
system boot device -- (usually a disk drive or ROM) -- passed as decimal
string, NOT as binary value * ZP 'hrSystemInitialLoadParameters' -- syntax
'InternationalDisplayString (SIZE (0..128))' -- host system boot parameters
(eg, pathname and options) -- passed in dynamic locale -- (see
'xcmGenCurrentLocalizationIndex') * ZM 'hrSystemMaxProcesses' -- syntax
'INTEGER (0..2147483647)' -- max number of process contexts supported on host
system -- or zero (if no fixed limit) -- passed as decimal string, NOT as
binary value -- Storage group of IETF HR MIB (RFC 2790) * SX 'hrStorageIndex'
-- syntax 'INTEGER (1..2147483647)' -- index of host system storage conceptual
row -- (REQUIRED for 'entityCreate') -- passed as decimal string, NOT as binary
index * SY 'hrStorageType' -- syntax 'OBJECT IDENTIFIER' -- (see
'hrStorageTypes' in IETF HR MIB) -- type of host system storage -- passed as
dotted decimal OID or as storage type label * SD 'hrStorageDescr' -- syntax
'DisplayString (SIZE (0..64))' -- (NVT ASCII string) -- textual description of
host system storage, -- including the type and instance of the storage --
passed as ASCII string, NOT as localized string * SU 'hrStorageAllocationUnits'
-- syntax 'INTEGER (1..2147483647)' -- (size in bytes) -- size of allocation
units on host system storage -- passed as decimal string, NOT as binary value *
SS 'hrStorageSize' -- syntax 'INTEGER (1..2147483647)' -- (size in allocation
units) -- size in 'hrStorageAllocationUnits' of host system storage -- passed
as decimal string, NOT as binary value -- Device table in Device group of IETF
HR MIB (RFC 2790) * DX 'hrDeviceIndex' -- syntax 'INTEGER (1..2147483647)' --
index of host system device conceptual row -- (REQUIRED for 'deviceCreate') --
passed as decimal string, NOT as binary index * DY 'hrDeviceType' -- syntax
'OBJECT IDENTIFIER' -- (see 'hrDeviceTypes' in IETF HR MIB) -- type of host
system device -- (certain device types make related table entries MANDATORY) --
passed as dotted decimal OID or as device type label -- (eg,
'hrDevicePrinter'), NOT as binary 'OBJECT IDENTIFIER' * DD 'hrDeviceDescr' --
syntax 'DisplayString' (SIZE (0..64)) -- (NVT ASCII string) -- textual
description of host system device, -- including manufacturer and revision, and
-- (optionally) serial number -- passed as ASCII string, NOT as localized
string * DI 'hrDeviceID' -- syntax 'ProductID' -- (manufacturer defined object
identifier) -- product ID of host system device -- passed as dotted decimal OID
or as device product ID label -- (eg, 'xcmPidStarship20'), NOT as binary object
identifier -- Processor table in Device group of IETF HR MIB (RFC 2790) * PI
'hrProcessorFrwID' -- syntax 'ProductID' -- (manufacturer defined object
identifier) -- product ID of firmware associated with processor device --
passed as dotted decimal OID or as firmware product ID label -- (for device
types 'hrDeviceProcessor' in HR Device table) -- Network table in Device group
of IETF HR MIB (RFC 2790) * NI 'hrNetworkIfIndex' -- syntax 'INTEGER
(1..2147483647)' -- (see 'ifIndex' in IETF MIB-II) -- index of 'ifEntry'
associated with network device -- passed as decimal string, NOT as binary index
-- (for device types 'hrDeviceNetwork' in HR Device table) -- Disk Storage
table in Device group of IETF HR MIB (RFC 2790) * KA 'hrDiskStorageAccess' --
syntax 'INTEGER (1..2)' (enumeration) -- access (including write-protect) of
disk storage device -- passed as decimal string or as access enum label -- (eg,
'readOnly'), NOT as binary value -- (for device types 'hrDeviceDiskStorage' in
HR Device table) * KM 'hrDiskStorageMedia' -- syntax 'INTEGER (1..8)'
(enumeration) -- type of media used in disk storage device -- passed as decimal
string or as media enum label -- (eg, 'hardDisk'), NOT as binary value -- (for
device types 'hrDeviceDiskStorage' in HR Device table) * KR
'hrDiskStorageRemoveble' -- syntax 'Boolean' (true/false, defined in IETF HR
MIB) -- indicates if media MAY be removed for disk storage device -- (note the
spelling error in 'hrDiskStorageRemoveble' !!) -- passed as decimal string or
as boolean enum label -- (eg, 'true'), NOT as binary value -- (for device types
'hrDeviceDiskStorage' in HR Device table) * KC 'hrDiskStorageCapacity' --
syntax 'KBytes' (kilobytes, defined in IETF HR MIB) -- total size of disk
storage device -- passed as decimal string, NOT as binary value -- (for device
types 'hrDeviceDiskStorage' in HR Device table) -- Partition table in Device
group of IETF HR MIB (RFC 2790) * XX 'hrPartitionIndex' -- syntax 'INTEGER
(1..2147483647)' -- index of disk storage partition -- (REQUIRED for
'entityCreate') -- passed as decimal string, NOT as binary index -- (for device
types 'hrDeviceDiskStorage' in HR Device table) * XL 'hrPartitionLabel' --
syntax 'InternationalDisplayString (SIZE (0..128))' -- textual description of
disk storage partition -- passed in dynamic locale -- (see
'xcmGenCurrentLocalizationIndex') -- (for device types 'hrDeviceDiskStorage' in
HR Device table) * XI 'hrPartitionID' -- syntax 'OCTET STRING (SIZE (0..128))'
-- descriptor (possibly binary) of disk storage partition -- passed as
hexadecimal string, NOT as binary value -- (for device types
'hrDeviceDiskStorage' in HR Device table) * XS 'hrPartitionSize' -- syntax
'KBytes' (kilobytes, defined in IETF HR MIB) -- total size of disk storage
partition -- passed as decimal string, NOT as binary value -- (for device types
'hrDeviceDiskStorage' in HR Device table) * XF 'hrPartitionFSIndex' -- syntax
'INTEGER (0..2147483647)' -- (see 'hrFSIndex' in IETF HR MIB) -- index of
'hrFSEntry' mounted on disk storage partition -- or zero, if none -- passed as
decimal string, NOT as binary value -- (exactly ONE file system MAY be mounted
on a partition) -- (note that multiple partitions MAY support ONE file system,
-- but multiple file systems MAY NOT reside on ONE partition) -- (for device
types 'hrDeviceDiskStorage' in HR Device table) -- File System table in Device
group of IETF HR MIB (RFC 2790) * FX 'hrFSIndex' -- syntax 'INTEGER
(1..2147483647)' -- index of file system -- (REQUIRED for 'entityCreate') --
passed as decimal string, NOT as binary index -- (for device types
'hrDeviceDiskStorage' in HR Device table) * FM 'hrFSMountPoint' -- syntax
'InternationalDisplayString (SIZE (0..128))' -- path name of the root of file
system -- passed in dynamic locale -- (see 'xcmGenCurrentLocalizationIndex') --
(for device types 'hrDeviceDiskStorage' in HR Device table) * FR
'hrFSRemoteMountPoint' -- syntax 'InternationalDisplayString (SIZE (0..128))'
-- name or address of server file system is mounted from -- passed in dynamic
locale -- (see 'xcmGenCurrentLocalizationIndex') -- (for device types
'hrDeviceDiskStorage' in HR Device table) * FY 'hrFSType' -- syntax 'OBJECT
IDENTIFIER' -- (see 'hrFSTypes' in IETF HR MIB) -- type of file system --
passed as dotted decimal OID or as file system type label -- (eg,
'hrFSiso9660'), NOT as binary 'OBJECT IDENTIFIER' -- (for device types
'hrDeviceDiskStorage' in HR Device table) * FA 'hrFSAccess' -- syntax 'INTEGER
(1..2)' (enumeration) -- access of WHOLE file system (NOT individual files) --
passed as decimal string or as access enum label -- (eg, 'readOnly'), NOT as
binary value -- (for device types 'hrDeviceDiskStorage' in HR Device table) *
FB 'hrFSBootable' -- syntax 'Boolean' (true/false, defined in IETF HR MIB) --
indicates if file system is bootable -- passed as decimal string or as boolean
enum label -- (eg, 'true'), NOT as binary value -- (for device types
'hrDeviceDiskStorage' in HR Device table) * FS 'hrFSStorageIndex' -- syntax
'INTEGER (0..2147483647)' -- (see 'hrStorageIndex' in IETF HR MIB) -- index of
'hrStorageEntry' for file system -- or zero, if none -- passed as decimal
string, NOT as binary value -- (exactly ONE file system MAY be mounted on a
partition) -- (note that multiple partitions MAY support ONE file system, --
but multiple file systems MAY NOT reside on ONE partition) -- (for device types
'hrDeviceDiskStorage' in HR Device table) -- Software Running group of IETF HR
MIB (RFC 2790) * RO 'hrSWOSIndex' -- syntax 'INTEGER (1..2147483647)' -- index
of operating system running software conceptual row -- passed as decimal
string, NOT as binary index * RX 'hrSWRunIndex' -- syntax 'INTEGER
(1..2147483647)' -- index of host system running software conceptual row --
(REQUIRED for 'entityCreate') -- passed as decimal string, NOT as binary index
* RN 'hrSWRunName' -- syntax 'InternationalDisplayString (SIZE (0..64))' --
textual description of running software, -- including manufacturer, revision,
local name, and -- (optionally) serial number -- passed in dynamic locale --
(see 'xcmGenCurrentLocalizationIndex') * RI 'hrSWRunID' -- syntax 'ProductID'
-- (manufacturer defined object identifier) -- product ID of running software
-- passed as dotted decimal OID or as software product ID label -- (eg,
'xcmPidStarship20'), NOT as binary object identifier * RF 'hrSWRunPath' --
syntax 'InternationalDisplayString (SIZE (0..128))' -- initial load path (file)
of running software -- passed in dynamic locale -- (see
'xcmGenCurrentLocalizationIndex') * RP 'hrSWRunParameters' -- syntax
'InternationalDisplayString (SIZE (0..128))' -- initial load parameters
(arguments) of running software -- passed in dynamic locale -- (see
'xcmGenCurrentLocalizationIndex') * RY 'hrSWRunType' -- syntax 'INTEGER (1..4)'
(enumeration) -- type of running software -- passed as decimal string or as
software type enum label -- (eg, 'application'), NOT as binary value --
Software Installed group of IETF HR MIB (RFC 2790) * WX 'hrSWInstalledIndex' --
syntax 'INTEGER (1..2147483647)' -- index of host system installed software
conceptual row -- (REQUIRED for 'entityCreate') -- passed as decimal string,
NOT as binary index * WN 'hrSWInstalledName' -- syntax
'InternationalDisplayString (SIZE (0..64))' -- textual description of installed
software, -- including manufacturer, revision, local name, and -- (optionally)
serial number -- passed in dynamic locale -- (see
'xcmGenCurrentLocalizationIndex') * WI 'hrSWInstalledID' -- syntax 'ProductID'
-- (manufacturer defined object identifier) -- product ID of installed software
-- passed as dotted decimal OID or as software product ID label -- (eg,
'xcmPidStarship20'), NOT as binary object identifier * WY 'hrSWInstalledType'
-- syntax 'INTEGER (1..4)' (enumeration) -- type of installed software --
passed as decimal string or as software type enum label -- (eg, 'application'),
NOT as binary value -- Color Calibration Information * CN [Color Name - no
object mapping] -- syntax 'DisplayString (SIZE (2))' -- name of a color (color
plus level) -- color: C=cyan, M=magenta, Y=yellow, K=Black -- color: R=red,
G=green, B=blue -- level: S=shadow, M=midbalance, H=highlight, W=whitepoint --
(eg, 'CN=CS:' specifies a color name of 'cyan-shadow') -- (see 'TCxx' system
color calibration tests below) * CV [Color Value - no object mapping] -- syntax
'INTEGER (0..100)' -- value of a color (specified by previous 'CN=xx' element)
-- (eg, 'CV=20:' specifies a color value of '20') -- (see 'TCxx' system color
calibration tests below) -- SNMP Community Names (for SNMPv1c and SNMPv2c) * CO
[Community Name Ordinal - no direct object mapping] -- syntax 'Ordinal32' --
ordinal for storing the 'CR|CW|CT' value below to an array -- (eg, 'CO=1'
refers to object 'xcmGenBaseSNMPxxxCommunity') -- (see 'CR', 'CW', and 'CT'
below) * CR 'xcmGenBaseSNMPReadCommunity' -- syntax
'XcmFixedLocaleDisplayString (SIZE (0..255))' -- read community name for SNMP
'Get|GetNext|GetBulk' PDUs -- passed in fixed locale (see
'xcmGenFixedLocalizationIndex') -- (eg, 'CR=:' clears all read community names)
-- (eg, 'CR=public:' sets a read community name of 'public') * CW
'xcmGenBaseSNMPWriteCommunity' -- syntax 'XcmFixedLocaleDisplayString (SIZE
(0..255))' -- write community name for SNMP 'Set|Get|GetNext|GetBulk' PDUs --
passed in fixed locale (see 'xcmGenFixedLocalizationIndex') * CT
'xcmGenBaseSNMPTrapCommunity' -- syntax 'XcmFixedLocaleDisplayString (SIZE
(0..255))' -- trap community name for SNMP 'Inform|Trap' PDUs -- passed in
fixed locale (see 'xcmGenFixedLocalizationIndex') -- Job Data from XCMI Job
Monitoring MIB (41jobmon) * JA 'xcmJobSubmittingApplication' -- syntax
'CodeIndexedStringIndex' -- job programmatic originator (as opposed to job
human owner) -- passed in fixed locale (see 'xcmGenFixedLocalizationIndex') *
JC 'xcmJobClientId' -- syntax 'XcmGlobalUniqueID' -- job client-assigned
identifier -- passed as dotted decimal string, NOT as a binary OID * JD
'xcmDocName' -- syntax 'CodeIndexedStringIndex' -- document name -- passed in
fixed locale (see 'xcmGenFixedLocalizationIndex') * JF 'xcmDocFileName' --
syntax 'CodeIndexedStringIndex' -- document filename (MAY be used for print-by-
reference) -- passed in fixed locale (see 'xcmGenFixedLocalizationIndex') * JH
'jobHoldSet' in 'xcmJobStateReasons' -- syntax 'TruthValue' -- job hold (for
creating job with held-by-user condition) -- passed as '1' (true) or '2'
(false), NOT as binary value * JM 'xcmJobMessageFromAdministrator' -- syntax
'CodeIndexedStringIndex' -- job message from system administrator -- passed in
fixed locale (see 'xcmGenFixedLocalizationIndex') * JN 'xcmJobName' -- syntax
'CodeIndexedStringIndex' -- job name -- passed in fixed locale (see
'xcmGenFixedLocalizationIndex') * JO 'xcmJobOwner' -- syntax
'CodeIndexedStringIndex' -- job human owner (as opposed to job programmatic
originator) -- passed in fixed locale (see 'xcmGenFixedLocalizationIndex') * JP
'xcmJobPriority' -- syntax 'INTEGER (0..100)' -- job priority (0=unspecified,
1=lowest, 100=highest) -- passed as decimal string, NOT as binary index * JR
'xcmJobRetentionPeriod' -- syntax 'Cardinal32' -- job retention period (in
seconds after completion) -- passed as decimal string, NOT as binary value * JS
'xcmJobServiceType' -- syntax 'XcmJMJobServiceTypeOID' (OBJECT IDENTIFIER) --
job service type -- passed as dotted decimal OID or as job service type label
-- (eg, 'xcmJobServicePrintOID'), -- NOT as binary 'OBJECT IDENTIFIER' * JT
'xcmJobProcessAfter' -- syntax 'DateAndTime' -- job process after calendar date
and time -- passed as dotted decimal string (ie, 'yyyy.mm.dd.hh.mm.ss'), -- NOT
as binary value * JU 'xcmJobComment' -- syntax 'CodeIndexedStringIndex' -- job
comment from user (eg, for banner sheet) -- passed in fixed locale (see
'xcmGenFixedLocalizationIndex') * JW ['system job' standard type - no object
mapping] -- syntax 'DisplayString' -- 'system job' standard type (standardized
below) -- (REQUIRED for 'deviceJobCreate') -- passed as ASCII string, NOT as
localized string -- (copied to 'xcmJobName', unless 'JN' tag is specified) * JX
['system job' extended type - no object mapping] -- syntax 'DisplayString' --
'system job' extended type (freeform, no standards) -- (OPTIONAL for
'deviceJobCreate') -- passed as ASCII string, NOT as localized string --
(appended to 'xcmJobName', unless 'JN' tag is specified) XCMI standard 'system
job' types for use in 'JW' arguments (in 'xcmHrDevMgmtCommandData' and
'xcmSimpleJobMgmtData') and for the value of 'xcmJobName' (unless 'JN' tag is
specified) are as follows: -- Accounting Reports * ACCT (basic) accounting
report * AEXT (extended) accounting report -- Configuration Reports * CONF
(basic) system configuration report * CEXT (extended) system configuration
report * CMEM (installed) memory configuration report * CMSR media (supported
and ready) configuration report * CNET network interfaces configuration report
* COPT (installed) optional devices configuration report * CPDL (JCL and/or
PDL) interpreters configuration report * CPRO network protocols configuration
report * CSWI (installed) software configuration report -- Demos * DEMO (basic)
demo job * DEXT (extended) demo job -- Font Reports * FONT (basic) fonts report
* FEXT (extended) fonts report * FPCL (installed) HP PCL fonts report * FPSX
(installed) Adobe PostScript fonts report -- List Directories and/or Files --
See section 3.4.1 'List Directory (LIST) Requests' -- in XCMI Ext to Host
Resources TC. * LIST list tree of disk directories (but NOT contents) * LALL
list tree of disk directories (including all files) * LDIR list (specific) disk
directory * LERR list system error file * LLOG list system log file * LFIL list
(specific) file -- Local UI Menu Reports * MENU (basic) local UI menu tree
report * MEXT (extended) local UI menu tree report -- Document Resources
Reports * RSRC (basic) document resources report * REXT (extended) document
resources report -- System Tests * TEST (basic) system test * TEXT (extended)
system test * TMEM (installed) memory verfication test report * TNET network
interfaces verification test report * TOPT (installed) optional devices test
report * TPAT print test pattern (especially for printers and copiers) * TPDL
(JCL and/or PDL) interpreters system test report * TPRO network protocols
verification test report * TSWI (installed) software verfication test report --
System Color Calibration Tests * TCAC print automatic color chart (auto
calibration) * TCBC print balance chart (manual calibration) * TCCC print
corrected color chart (color calibration) * TCSC scan automatic color chart
(auto calibration) * TCTC print tone chart (manual calibration) * TCUC print
uncorrected color chart (color calibration) * TCBV set balance values (manual
calibration) * TCTV set tone values (manual calibration) -- User Reports * USER
(basic) configured users report * UEXT (extended) configured users report The
above XCMI standard 'tags' MAY be extended in the future.
"""


class XcmHrDevPowerModeType(TextualConvention, Integer32):
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
        *(("offMode", 6),
          ("other", 1),
          ("readyMode", 3),
          ("sleepMode", 5),
          ("standbyMode", 4),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
A device power mode type, used by system administrators of this device for
power management details. Usage: Used in 'devicePowerModeType' Device Detail,
to clearly identify the referenced power mode (without resort to strings).
"""


class XcmHrDevPowerTimeUnit(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("day", 10),
          ("hour", 9),
          ("kilosecond", 6),
          ("megasecond", 7),
          ("microsecond", 3),
          ("millisecond", 4),
          ("minute", 8),
          ("month", 12),
          ("other", 1),
          ("second", 5),
          ("unknown", 2),
          ("week", 11),
          ("year", 13))
    )

    if mibBuilder.loadTexts:
        description = """\
A device power cycle time unit, used by system administrators of this device
for power management cycle times. Usage: Used to scale the values in the Device
Power group, for convenience and (optional) high resolution.
"""


class XcmHrDevTrafficUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              44,
              45,
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
              63,
              64,
              65,
              66,
              67,
              68,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("area100Sheet", 67),
          ("area100SqFoot", 65),
          ("area10SqMeter", 66),
          ("areaSheet", 59),
          ("areaSqCentimeter", 56),
          ("areaSqFoot", 51),
          ("areaSqInch", 50),
          ("areaSqKilometer", 58),
          ("areaSqMeter", 57),
          ("areaSqMicrometer", 54),
          ("areaSqMile", 53),
          ("areaSqMillimeter", 55),
          ("areaSqYard", 52),
          ("binaryBit", 11),
          ("binaryLine", 14),
          ("binaryNibble", 12),
          ("binaryOctet", 13),
          ("document", 68),
          ("inkStick", 100),
          ("length100Foot", 63),
          ("length100Meter", 64),
          ("lengthCentimeter", 35),
          ("lengthFoot", 30),
          ("lengthInch", 29),
          ("lengthKilometer", 37),
          ("lengthMeter", 36),
          ("lengthMicrometer", 33),
          ("lengthMile", 32),
          ("lengthMillimeter", 34),
          ("lengthYard", 31),
          ("media100Image", 60),
          ("media100Impression", 61),
          ("media100Sheet", 62),
          ("mediaBlock", 20),
          ("mediaCell", 25),
          ("mediaColumn", 23),
          ("mediaImage", 26),
          ("mediaImpression", 27),
          ("mediaPacket", 24),
          ("mediaRow", 22),
          ("mediaSector", 21),
          ("mediaSheet", 28),
          ("other", 1),
          ("textCharacter", 15),
          ("textLine", 17),
          ("textParagraph", 19),
          ("textSentence", 18),
          ("textWord", 16),
          ("totalItemsConsumed", 101),
          ("unknown", 2),
          ("volumeKiloliter", 41),
          ("volumeLiter", 40),
          ("volumeMicroliter", 38),
          ("volumeMilliliter", 39),
          ("weightGram", 44),
          ("weightKilogram", 45),
          ("weightMicrogram", 42),
          ("weightMilligram", 43))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of traffic unit used to measure input and/or output traffic for this
device. Usage: The use of either 'other' or 'unknown' is uninformative and
SHOULD be avoided by conforming implementations. Usage: 'mediaImage' - SHOULD
be used ONLY for softcopy INPUT page images (scan, copy, fax, etc.).
'mediaImpression' - SHOULD be used ONLY for hardcopy OUTPUT page impressions
(print, copy, fax, etc.) 'mediaSheet' - SHOULD be used ONLY for hardcopy OUTPUT
and does NOT always equal output pages (e.g., duplex or N-up printing).
"""


class XcmHrGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional IETF Host Resources MIB (RFC 2790) and XCMI Ext to Host Resources MIB
objects which are supported by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. The current set of
values (which MAY be extended in the future) is given below: -- IETF Host
Resources MIB object groups 1 : hrSystemGroup -- 2**0 2 : hrStorageGroup --
2**1 4 : hrDeviceGroup -- 2**2 8 : hrSWRunGroup -- 2**3 16 : hrSWRunPerfGroup
-- 2**4 32 : hrSWInstalledGroup -- 2**5 -- XCMI Ext to Host Resources MIB
object groups 64 : xcmHrDevInfoGroup -- 2**6 128 : xcmHrDevHelpGroup -- 2**7
256 : xcmHrDevMgmtGroup -- 2**8 512 : xcmHrDevPowerGroup -- 2**9 1024 :
xcmHrDevTrafficGroup -- 2**10 2048 : xcmHrSystemFaultGroup -- 2**11 4096 :
xcmHrGeneralGroup -- 2**12 8192 : xcmHrDevCalendarGroup -- 2**13 16384 :
xcmHrSWRunGroup -- 2**14 32768 : xcmHrSWInstalledGroup -- 2**15 65536 :
xcmHrDevDetailGroup -- 2**16 131072 : xcmHrStorageExtGroup -- 2**17 262144 :
xcmHrStorageDetailGroup -- 2**18 524288 : xcmHrDevCoverGroup -- 2**19 1048576 :
xcmHrDevAlertGroup -- 2**20 2097152 : xcmHrConsoleScreenGroup -- 2**21 4194304
: xcmHrConsoleTabGroup -- 2**22 -- IETF Host Resources MIB tables for specific
device types 33554432 : hrProcessorTable -- 2**25 67108864 : hrNetworkTable --
2**26 134217728 : hrPrinterTable -- 2**27 268435456 : hrDiskStorageTable --
2**28 536870912 : hrPartitionTable -- 2**29 1073741824 : hrFSTable -- 2**30 --
2**31 NOT used, due to 'Integer32|Cardinal32' semantics Usage: Conforming
management agents SHALL accurately report their support for IETF Host Resources
MIB (RFC 2790) and XCMI Ext to Host Resources MIB object groups.
"""


class XcmHrSWRunXStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("other", 1),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
An extended software status, used by system administrators and end users of
this software (here, read 'state' for 'status'). Note: This extended software
status is present for future extensions.
"""


class XcmHrStorageDetailType(TextualConvention, Integer32):
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
              20,
              21,
              22,
              23,
              24,
              30,
              31,
              32,
              33,
              40,
              41,
              42)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("storageAlias", 4),
          ("storageAllocationUnits", 7),
          ("storageBaseAddress", 40),
          ("storageContext", 9),
          ("storageDescription", 6),
          ("storageFontCache", 20),
          ("storageFormCache", 21),
          ("storageHeapMemory", 30),
          ("storageImageBuffer", 12),
          ("storageInputBuffer", 10),
          ("storageLogoCache", 22),
          ("storageMacroCache", 23),
          ("storageMarkerBuffer", 13),
          ("storageName", 3),
          ("storageOutputBuffer", 11),
          ("storagePageBuffer", 14),
          ("storagePageSize", 42),
          ("storagePrefixMemory", 31),
          ("storageStackMemory", 32),
          ("storageStyleCache", 24),
          ("storageTranslationBuffer", 15),
          ("storageTree", 8),
          ("storageType", 5),
          ("storageWordSize", 41),
          ("storageWorkingBuffer", 16),
          ("storageWorkingMemory", 33),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of the storage detail information specified in this conceptual row in
the 'xcmHrStorageDetailTable'. Usage: Used to describe system-, program-, or
thread-level memory allocations/reservations. Usage: 'hrStorageEntry' and
(optionally) 'xcmHrStorageEntry' MAY be referenced via
'xcmSecServiceHrStorageIndex' in the Service group of the XCMI Security MIB.
Usage: Conforming management stations and management agents SHALL implement
specified semantics for storage detail types.
"""


class XcmHrStorageRealization(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("logicalProgram", 21),
          ("logicalSystem", 20),
          ("logicalThread", 22),
          ("other", 1),
          ("physicalProgram", 11),
          ("physicalSystem", 10),
          ("physicalThread", 12),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
An extended storage type (or storage 'realization'), used by system
administrators and end users of this storage. Usage: The use of either 'other'
or 'unknown' is uninformative and SHOULD be avoided by conforming
implementations. * 'physicalSystem' - 'real' memory installed on a 'system'
whose product is found via 'xcmHrStorageProductDeviceIndex' and whose CPU is
found via 'xcmHrStoragePlatformDeviceIndex' and whose self is found via
'xcmHrStorageMatchingDeviceIndex'; * 'physicalProgram' - 'real' memory assigned
to a 'program' (memory which is 'pinned' and is NOT paged to disk storage)
whose program is found via 'xcmHrStorageSWRunIndex'; * 'physicalThread' -
'real' memory assigned to a 'thread' (memory which is 'pinned' and is NOT paged
to disk storage) whose program/thread is found via 'xcmHrStorageSWRunIndex'; *
'logicalSystem' - 'virtual' memory assigned to a 'system' (memory which is NOT
'pinned' and MAY be paged to disk storage) whose product is found via
'xcmHrStorageProductDeviceIndex' and whose CPU is found via
'xcmHrStoragePlatformDeviceIndex' and whose self is found via
'xcmHrStorageMatchingDeviceIndex'; * 'logicalProgram' - 'virtual' memory
assigned to a 'program' (memory which is NOT 'pinned' and MAY be paged to disk
storage) whose program is found via 'xcmHrStorageSWRunIndex'; * 'logicalThread'
- 'virtual' memory assigned to a 'thread' (memory which is NOT 'pinned' and MAY
be paged to disk storage) whose program/thread is found via
'xcmHrStorageSWRunIndex'.
"""


class XcmHrDpaAvailability(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("none", 5),
          ("normal", 2),
          ("unknown", 6))
    )

    if mibBuilder.loadTexts:
        description = """\
The generic availability of this system, device, service, etc.
"""


class XcmHrDpaConditions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The generic conditions (ie, state reasons) of this system, device, service,
etc, specified in a bit-mask. -- DPA - Service level operations -- See section
D.2.3 of DPA Mgmt Service (ISO 10175-3) -- and section 4 of POSIX DPA Client
(IEEE 1387.4) 1 : cleanedByOperator -- 2**0 2 : cleanedBySystem -- 2**1 -- all
jobs deleted by operator/system -- 'serviceClean' in
'XcmSvcMonServiceMgmtOperation' -- 'pdclean' in POSIX DPA Client 4 :
disabledByOperator -- 2**2 8 : disabledBySystem -- 2**3 -- all new jobs
rejected by system -- 'serviceDisable' in 'XcmSvcMonServiceMgmtOperation' --
'pddisable' in POSIX DPA Client 16 : pausedByOperator -- 2**4 32 :
pausedBySystem -- 2**5 -- all existing job output suspended on system --
'servicePause' in 'XcmSvcMonServiceMgmtOperation' -- 'pdpause' in POSIX DPA
Client 64 : shutdownByOperator -- 2**6 - 'pdshutdown' 128 : shutdownBySystem --
2**7 - 'pdshutdown' -- service state is 'terminating', then 'unavailable' --
'serviceShutdown' in 'XcmSvcMonServiceMgmtOperation' -- 'pdshutdown' in POSIX
DPA Client -- XCMI - Service level extended operations 256 :
diagnosedByOperator -- 2**8 512 : diagnosedBySystem -- 2**9 --
'serviceDiagnose' in 'XcmSvcMonServiceMgmtOperation' 1024 : resetByOperator --
2**10 2048 : resetBySystem -- 2**11 -- 'serviceReset[Cold|Warm|Factory]' -- in
'XcmSvcMonServiceMgmtOperation' 4096 : startedByOperator -- 2**12 8192 :
startedBySystem -- 2**13 -- 'service[Create|Install|Upgrade|Restart]' -- in
'XcmSvcMonServiceMgmtOperation' -- XCMI - Document service activities (during
'ready' state) 65536 : activeCopy -- 2**16 131072 : activePrint -- 2**17 262144
: activeScan -- 2**18 524288 : activeFaxReceive -- 2**19 1048576 :
activeFaxSend -- 2**20 2097152 : activeFileReceive -- 2**21 4194304 :
activeFileSend -- 2**22 8388608 : activeMailReceive -- 2**23 16777216 :
activeMailSend -- 2**24 33554432 : activeImageProcess -- 2**25 67108864 :
activeOCR -- 2**26 134217728 : activeDistribute -- 2**27 Usage: The above
'conditions' augment the service state in
'xcmSvcMonService[Current|Previous]State' and the service mgmt information in
'xcmSvcMonServiceMgmt[Operation|InProgress]'. Usage: Conforming management
agents SHALL report all 'conditions' of entities accurately. 'Conditions' occur
within or across 'states' in a finite state machine implementation of a system,
device, service, etc. Usage: A service with 'xcmSvcMonServiceCurrentState' of
'ready(1)' might have 'xcmSvcMonServiceConditions' of 'disabledByOperator',
indicating that the service will not accept new jobs. Usage: Multi-bit examples
of 'xcmSvcMonServiceConditions' are 'disabledByOperator' concurrently with
'pausedByOperator' and 'activePrint' concurrently with 'activeMailSend'.
"""


class XcmHrDpaJobValidateSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The job validation support of this system, service, etc, specified in a bit-
mask. The current set of values (which MAY be extended in the future) is given
below: -- ISO DPA standard values 1 : validateAndProcess -- generalized from
DPA 'print' 2 : validateSubmitOnly -- error check, do NOT process -- XCMI
standard values 4 : validateSyntaxOnly -- check syntax only 8 :
validateSemanticsOnly -- check syntax/ranges/states 16 : validateLocalOnly --
check semantic/local services 32 : validateDistributed -- check distributed
services 64 : validateCreateLocal -- create local child jobs 128 :
validateCreateRemote -- create remote child jobs Usage: Conforming management
agents SHALL accurately report their support for job validation modes.
"""


class XcmHrDpaObjectClassSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The object class support of this system, service, etc, specified in a bit-mask.
The current set of values (which MAY be extended in the future) is given below:
-- ISO DPA standard values 1 : generic -- 2**0 2 : job -- 2**1 4 : printer --
2**2 8 : server -- 2**3 16 : medium -- 2**4 32 : font -- 2**5 256 :
transferMethod -- 2**8 512 : deliveryMethod -- 2**9 1024 : auxiliarySheet --
2**10 2048 : finishing -- 2**11 4096 : output -- 2**12 8192 : imposition --
2**13 16384 : scheduler -- 2**14 32768 : document -- 2**15 65536 : resource --
2**16 131072 : initialValueJob -- 2**17 262144 : initialValueDocument -- 2**18
524288 : resourceContext -- 2**19 1048576 : auxiliarySheetPackage -- 2**20 --
XCMI standard values 16777216 : deviceHostSystem -- 2**24 33554432 :
deviceScanner -- 2**25 67108864 : deviceCopier -- 2**26 134217728 : deviceFax
-- 2**27 268435456 : deviceMailbox -- 2**28 536870912 : deviceFinisher -- 2**29
1073741824 : deviceCRU -- 2**30 -- 2**31 NOT used, due to
'Integer32|Cardinal32' semantics Usage: Conforming management agents SHALL
accurately report their support for object classes (ISO DPA and XCMI).
"""


class XcmHrDpaState(TextualConvention, Integer32):
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
        *(("busy", 5),
          ("initializing", 6),
          ("onRequest", 2),
          ("ready", 1),
          ("terminating", 7),
          ("unavailable", 3),
          ("unknown", 4))
    )

    if mibBuilder.loadTexts:
        description = """\
The generic state of this object (system, device, service, etc.). The following
standard values are defined (in section 9.1.6.4 'State' of ISO 10175-1): *
'ready' - This object is ready to be used without human intervention. *
'onRequest' - This object requires human intervention in order to be used. *
'unavailable' - This object is NOT available for use even with human
intervention. * 'unknown' - This state of this object is NOT known. * 'busy' -
This object is temporarily inaccessible due to dynamic constraints, but will
become 'ready' without human intervention. * 'initializing' - This object is
being initialized (and is therefore temporarily inaccessible). * 'terminating'
- This object is being terminated (and is therefore permanently inaccessible).
"""


class XcmHrSuppliesClassTC(TextualConvention, Integer32):
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
        *(("customerReplacable", 4),
          ("notReplacable", 7),
          ("other", 1),
          ("rarelyReplaced", 6),
          ("replenishable", 3),
          ("serviceReplacable", 5),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of a supply.
"""


class XcmHrDetailTableEnumTC(TextualConvention, Integer32):
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
        *(("finisherSuppliesTable", 3),
          ("markerSuppliesTable", 2),
          ("suppliesTable", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
The table referenced by a row in the xcmHrDetail table. Add additional tables
as details are required.
"""


class XcmHrConsoleDefaultService(TextualConvention, Integer32):
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
        *(("copyService", 1),
          ("faxService", 3),
          ("printService", 4),
          ("scanService", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The default service shown on the console user interface.
"""


# MIB Managed Objects in the order of their OIDs

_XcmHrDeviceTypes_ObjectIdentity = ObjectIdentity
xcmHrDeviceTypes = _XcmHrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2)
)
if mibBuilder.loadTexts:
    xcmHrDeviceTypes.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceTypes.setDescription("""\
The root of all additional device types defined in HRX TC.
""")
_XcmHrDevicePrinterHistory_ObjectIdentity = ObjectIdentity
xcmHrDevicePrinterHistory = _XcmHrDevicePrinterHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 55)
)
if mibBuilder.loadTexts:
    xcmHrDevicePrinterHistory.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevicePrinterHistory.setReference("""\
See: 'hrDevicePrinter' in the IETF HR MIB.
""")
if mibBuilder.loadTexts:
    xcmHrDevicePrinterHistory.setDescription("""\
Printer history device type - manufacturer independent.
""")
_XcmHrDeviceHostSystem_ObjectIdentity = ObjectIdentity
xcmHrDeviceHostSystem = _XcmHrDeviceHostSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 101)
)
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystem.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystem.setReference("""\
See: 'xcmHrDeviceHostSystemHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystem.setDescription("""\
Host system device type - manufacturer independent. For host systems which
instrument multiple devices and support MIBs with tables INDEXed by
'hrDeviceIndex', the single 'xcmHrDeviceHostSystem' device represents the
'root' device which MAY be used to manage overall host system defaults,
configuration, status, etc.
""")
_XcmHrDeviceScanner_ObjectIdentity = ObjectIdentity
xcmHrDeviceScanner = _XcmHrDeviceScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 102)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScanner.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceScanner.setReference("""\
See: 'xcmHrDeviceScannerHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceScanner.setDescription("""\
Scanner device type - manufacturer independent. An 'xcmHrDeviceScanner' device
with 'xcmHrDevInfoRealization' of 'physical' is a 'real' input device (eg, a
'scan channel' on a multifunction printer). An 'xcmHrDeviceScanner' device with
'xcmHrDevInfoRealization' of 'logical' is a 'virtual' input device (eg, a
'personality' of a 'scan channel' on a multifunction printer).
""")
_XcmHrDeviceCopier_ObjectIdentity = ObjectIdentity
xcmHrDeviceCopier = _XcmHrDeviceCopier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 103)
)
if mibBuilder.loadTexts:
    xcmHrDeviceCopier.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceCopier.setReference("""\
See: 'xcmHrDeviceCopierHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceCopier.setDescription("""\
Copier device type - manufacturer independent. An 'xcmHrDeviceCopier' device
with 'xcmHrDevInfoRealization' of 'physical' is a 'real' I/O device (eg, a
'copier' on a multifunction printer). An 'xcmHrDeviceCopier' device with
'xcmHrDevInfoRealization' of 'logical' is a 'virtual' I/O device (eg, a
'personality' of a 'copier' on a multifunction printer).
""")
_XcmHrDeviceFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceFax = _XcmHrDeviceFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 104)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFax.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFax.setReference("""\
See: 'xcmHrDeviceFaxHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceFax.setDescription("""\
Fax device type - manufacturer independent. xcmHrDeviceFax is maintained for
legacy products. It is recommended that the hrDeviceType is explicitly defined
using xcmHrDeviceEmbeddedFax, xcmHrDeviceServerFax or xcmHrDeviceInternetFax.
An 'xcmHrDeviceFax' device with 'xcmHrDevInfoRealization' of 'physical' is a
'real' I/O device (eg, a 'fax channel' on a multifunction printer). An
'xcmHrDeviceFax' device with 'xcmHrDevInfoRealization' of 'logical' is a
'virtual' I/O device (eg, a 'personality' of a 'fax channel' on a multifunction
printer).
""")
_XcmHrDeviceMailbox_ObjectIdentity = ObjectIdentity
xcmHrDeviceMailbox = _XcmHrDeviceMailbox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 105)
)
if mibBuilder.loadTexts:
    xcmHrDeviceMailbox.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceMailbox.setReference("""\
See: 'xcmHrDeviceMailboxSorter' and 'xcmHrDeviceSorter'.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceMailbox.setDescription("""\
Mailbox device type - manufacturer independent. An 'xcmHrDeviceMailbox' device
is a 'multi-bin' output device, with each 'bin' assigned to a user, group,
account, etc, and (optionally) physical security associated with each 'bin'. An
'xcmHrDeviceMailbox' device with 'xcmHrDevInfoRealization' of 'physical' is a
'real' output device (eg, a 'tower mailbox' on a high-end printer). An
'xcmHrDeviceMailbox' device with 'xcmHrDevInfoRealization' of 'logical' is a
'virtual' output device (eg, a 'personality' of a 'tower mailbox' on a high-end
printer). An 'xcmHrDeviceMailbox' device with 'xcmHrDevInfoRealization' of
'logical' MAY also indicate the current configuration of a 'physical' device of
type 'xcmHrDeviceMailboxSorter'.
""")
_XcmHrDeviceFinisher_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisher = _XcmHrDeviceFinisher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 106)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisher.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFinisher.setDescription("""\
Finisher device type - manufacturer independent. An 'xcmHrDeviceFinisher'
device is an output finishing device. An 'xcmHrDeviceFinisher' device with
'xcmHrDevInfoRealization' of 'physical' is a 'real' output device (eg, a
'stapler' on a high-end printer). An 'xcmHrDeviceFinisher' device with
'xcmHrDevInfoRealization' of 'logical' is a 'virtual' output device (eg, a
'personality' of a 'stapler' on a high-end printer).
""")
_XcmHrDeviceFeeder_ObjectIdentity = ObjectIdentity
xcmHrDeviceFeeder = _XcmHrDeviceFeeder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 107)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFeeder.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFeeder.setDescription("""\
Feeder device type - manufacturer independent. An 'xcmHrDeviceFeeder' device is
an input device. An 'xcmHrDeviceFeeder' device with 'xcmHrDevInfoRealization'
of 'physical' is a 'real' output device (eg, a 'high-capacity feeder' on a
high-end printer). An 'xcmHrDeviceFeeder' device with 'xcmHrDevInfoRealization'
of 'logical' is a 'virtual' output device (eg, a 'personality' of a 'high-
capacity feeder' on a high-end printer).
""")
_XcmHrDeviceSorter_ObjectIdentity = ObjectIdentity
xcmHrDeviceSorter = _XcmHrDeviceSorter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 108)
)
if mibBuilder.loadTexts:
    xcmHrDeviceSorter.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceSorter.setReference("""\
See: 'xcmHrDeviceMailboxSorter' and 'xcmHrDeviceMailbox'.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceSorter.setDescription("""\
Sorter device type - manufacturer independent. An 'xcmHrDeviceSorter' device is
a 'multi-bin' output device, with each 'bin' assigned to a copy of the current
job, and NO physical security associated with each 'bin'. An
'xcmHrDeviceSorter' device with 'xcmHrDevInfoRealization' of 'physical' is a
'real' output device (eg, a '10-bin sorter' on a mid-range printer). An
'xcmHrDeviceSorter' device with 'xcmHrDevInfoRealization' of 'logical' is a
'virtual' output device (eg, a 'personality' of a '10-bin sorter' on a mid-
range printer). An 'xcmHrDeviceSorter' device with 'xcmHrDevInfoRealization' of
'logical' MAY also indicate the current configuration of a 'physical' device of
type 'xcmHrDeviceMailboxSorter'.
""")
_XcmHrDeviceMailboxSorter_ObjectIdentity = ObjectIdentity
xcmHrDeviceMailboxSorter = _XcmHrDeviceMailboxSorter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 109)
)
if mibBuilder.loadTexts:
    xcmHrDeviceMailboxSorter.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceMailboxSorter.setDescription("""\
MailboxSorter device type - manufacturer independent. An
'xcmHrDeviceMailboxSorter' is a 'multi-bin' output device, which MAY be
configured as either a 'mailbox' or a 'sorter', by a system adminstrator or by
default product configuration. An 'xcmHrDeviceMailboxSorter' with
'xcmHrDevInfoRealization' of 'physical' is a 'real' output device and
associated with associated with exactly two 'logical' output devices of types
'xcmHrDeviceMailbox' and 'xcmHrDeviceSorter' - one of these 'logical' devices
MAY be 'running' (currently configured) - at least one SHALL be 'down' (NOT
currently configured).
""")
_XcmHrDevicePrintAppliance_ObjectIdentity = ObjectIdentity
xcmHrDevicePrintAppliance = _XcmHrDevicePrintAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 110)
)
if mibBuilder.loadTexts:
    xcmHrDevicePrintAppliance.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevicePrintAppliance.setReference("""\
See: 'hrDevicePrinter' in IETF Host Resources MIB (RFC 2790). See:
'xcmHrDevicePrinterHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDevicePrintAppliance.setDescription("""\
Print appliance device type - manufacturer independent. An
'xcmHrDevicePrintAppliance' is a network printing appliance with
'xcmHrDevInfoRealization' of 'physical'. An 'xcmHrDevicePrintAppliance' SHALL
statically and/or actively discover available network printers and SHOULD
advertise them as supported output devices, using rows in 'hrDeviceTable' of
IETF HR MIB (RFC 2790) and 'prtGeneralTable' of the Printer MIB (RFC 1759 or
successor), with 'hrDeviceType' set to 'hrDevicePrinter'. An
'xcmHrDevicePrintAppliance' SHALL NOT use 'hrDeviceIndex' of '1' (first row)
for an 'hrDevicePrinter' row, because a network printing appliance is an
enhanced spooler and NOT a printer.
""")
_XcmHrDeviceMarker_ObjectIdentity = ObjectIdentity
xcmHrDeviceMarker = _XcmHrDeviceMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 111)
)
if mibBuilder.loadTexts:
    xcmHrDeviceMarker.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceMarker.setDescription("""\
Marker Engine device type - manufacturer independent. An 'xcmHrDeviceMarker'
device with 'xcmHrDevInfoRealization' of 'physical' is a 'real' output device
(eg, the 'marking engine' on a multifunction printer or copier). The marking
engine is the module that accepts a print ready image and physical media as
input and outputs physical media with a physical representation of the print
ready input image. The 'xcmHrDeviceMarker' is a single module within a group of
modules that cumulatively are represented by 'hrDevicePrinter'. The marker
shall represent the whole marker as a single physical unit and should maintain
a single entry in the 'hrDeviceTable' for all products that support a single
marking engine regardless of internal engine mark points. (e.g. B&W, Highlight
Color and Full Color Presses shall have a single entry in 'hrDeviceTable').
Multiple entries of 'xcmHrDeviceMarker' may exist in the 'hrDeviceTable' if the
system supports multiple print engines whether chained, in parallel or in any
other configuration. An 'xcmHrDeviceMarker' SHALL NOT use 'hrDeviceIndex' of
'1' (first row). The index 1 is reserved for an 'hrDevicePrinter' row.
""")
_XcmHrDeviceFinisherBFM_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisherBFM = _XcmHrDeviceFinisherBFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 112)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherBFM.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherBFM.setDescription("""\
Basic Finisher Module device type - manufacturer independent. An
'xcmHrDeviceFinisherBFM' device is a basic output finishing device. An
'xcmHrDeviceFinisherBFM' device with 'xcmHrDevInfoRealization' of 'physical' is
a 'real' output device (eg, a 'stapler' on a high-end printer). An
'xcmHrDeviceFinisherBFM' device with 'xcmHrDevInfoRealization' of 'logical' is
a 'virtual' output device (eg, a 'personality' of a 'stapler' on a high-end
printer).
""")
_XcmHrDeviceFinisherMFF_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisherMFF = _XcmHrDeviceFinisherMFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 113)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherMFF.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherMFF.setDescription("""\
Multi-Function Finisher device type - manufacturer independent. An
'xcmHrDeviceFinisherMFF' device is a multi-function output finishing device. An
'xcmHrDeviceFinisherMFF' device with 'xcmHrDevInfoRealization' of 'physical' is
a 'real' output device (eg, a 'saddle stitcher', 'C-Folder', 'Z-Folder', 'Hole
Puncher' on a high-end printer). An 'xcmHrDeviceFinisherMFF' device with
'xcmHrDevInfoRealization' of 'logical' is a 'virtual' output device (eg, a
'personality' of a 'saddle stitcher', 'C-Folder', 'Z-Folder', 'Hole Puncher' on
a high-end printer).
""")
_XcmHrDeviceFinisherXIM_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisherXIM = _XcmHrDeviceFinisherXIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 114)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherXIM.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherXIM.setDescription("""\
eXternal Interface Module Finisher device type. An 'xcmHrDeviceFinisherXIM'
device is a hardware interface used to pass media from a Xerox printing device
to a 3rd party finishing devices. The 'xcmHrDeviceFinihserXIM' may or may not
contain its own output trays or finishing capabilities. An
'xcmHrDeviceFinisherXIM' device with 'xcmHrDevInfoRealization' of 'physical' is
a 'real' output device (e.g., an 'output bridge' on a high-end printer).
""")
_XcmHrDeviceFinisher3rdParty_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisher3rdParty = _XcmHrDeviceFinisher3rdParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 115)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisher3rdParty.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFinisher3rdParty.setDescription("""\
3rd Party Finisher device type - manufacturer independent. An
'xcmHrDeviceFinisher3rdParty' device is an output finishing device. An
'xcmHrDeviceFinisher3rdParty' device with 'xcmHrDevInfoRealization' of
'physical' is a 'real' output device (eg, a 'stapler' on a high-end printer).
An 'xcmHrDeviceFinisher3rdParty' device with 'xcmHrDevInfoRealization' of
'logical' is a 'virtual' output device (eg, a 'personality' of a 'stapler' on a
high-end printer).
""")
_XcmHrDevicePaymentInterface_ObjectIdentity = ObjectIdentity
xcmHrDevicePaymentInterface = _XcmHrDevicePaymentInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 116)
)
if mibBuilder.loadTexts:
    xcmHrDevicePaymentInterface.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDevicePaymentInterface.setDescription("""\
Payment Interface device type - manufacturer independent. An
'xcmHrDevicePaymentInterface' device is an payment authorization device. An
'xcmHrDevicePaymentInterface' device with 'xcmHrDevInfoRealization' of
'physical' is a 'real' point of purchase validation device (eg, a 'coin
operated', 'smart card' or other form of point of purchase payment for services
rendered on a multi-function printer or copier). An
'xcmHrDevicePaymentInterface' device with 'xcmHrDevInfoRealization' of
'logical' is a 'virtual' point of purchase validation device (eg, a software
service that accepts payment through the Web or some other form of remote point
of purchase payment for services rendered on a multi-function printer or
copier).
""")
_XcmHrDeviceInterposer_ObjectIdentity = ObjectIdentity
xcmHrDeviceInterposer = _XcmHrDeviceInterposer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 117)
)
if mibBuilder.loadTexts:
    xcmHrDeviceInterposer.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceInterposer.setDescription("""\
Interposer device type - manufacturer independent. An 'xcmHrDeviceInterposer'
device is an input device which physically resides downstream of the print
engine amongst finishing modules. An 'xcmHrDeviceInterposer' device with
'xcmHrDevInfoRealization' of 'physical' is a 'real' input device (eg, a 'high-
capacity Interposing feeder' that physically resides amongst finishing modules
on a high-end printer). An 'xcmHrDeviceInterposer' device with
'xcmHrDevInfoRealization' of 'logical' is a 'virtual' input device (eg, a
'personality' of a 'high-capacity Interposing feeder' that physically resides
amongst finishing modules on a high-end printer). Interposers are essentially
feeders that are placed downstream of the print engine paper path and upstream
of finishing devices. Interposer fed media is not marked by the print engine;
instead media fed from an interposer is inserted before, between or after
marked pages. The media constitutes covers, separators etc.
""")
_XcmHrDeviceInternetFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceInternetFax = _XcmHrDeviceInternetFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 118)
)
if mibBuilder.loadTexts:
    xcmHrDeviceInternetFax.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceInternetFax.setReference("""\
See: 'xcmHrDeviceFax' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceInternetFax.setDescription("""\
Internet Fax device type - manufacturer independent. A local Fax service which
sends and/or receives faxes over the internet
""")
_XcmHrDeviceServerFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceServerFax = _XcmHrDeviceServerFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 119)
)
if mibBuilder.loadTexts:
    xcmHrDeviceServerFax.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceServerFax.setReference("""\
See: 'xcmHrDeviceFax' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceServerFax.setDescription("""\
Server Fax device type - manufacturer independent. A Fax service which works
with a server on the network to send and/or receive faxes over a remote modem
and phone lines
""")
_XcmHrDeviceEmbeddedFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceEmbeddedFax = _XcmHrDeviceEmbeddedFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 120)
)
if mibBuilder.loadTexts:
    xcmHrDeviceEmbeddedFax.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceEmbeddedFax.setReference("""\
See: 'xcmHrDeviceFax' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceEmbeddedFax.setDescription("""\
Embedded Fax device type - manufacturer independent. A local fax service which
sends and/or receives fax directly over a modem and phone lines.
""")
_XcmHrDeviceForeignInterface_ObjectIdentity = ObjectIdentity
xcmHrDeviceForeignInterface = _XcmHrDeviceForeignInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 121)
)
if mibBuilder.loadTexts:
    xcmHrDeviceForeignInterface.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceForeignInterface.setDescription("""\
Foreign Interface device type - manufacturer independent. A physical connection
provided by a device for the purpose of connecting an external accessory. This
accessory may be capable of tracking data (e.g. Auditron) or may enable/
disable device operation (e.g. card reader, coin operator, etc.). This device
type shall only be used when the device cannot detect the type of external
accessory that is physically connected. If the device can detect the type of
external accessory which can be physically connected, then the appropriate
device type for that interface should be used instead. (e.g.
xcmHrDevicePaymentInterface, xcmHrDeviceSecurityInterface, or
xcmHrDeviceAccountingInterface
""")
_XcmHrDeviceSecurityInterface_ObjectIdentity = ObjectIdentity
xcmHrDeviceSecurityInterface = _XcmHrDeviceSecurityInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 122)
)
if mibBuilder.loadTexts:
    xcmHrDeviceSecurityInterface.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceSecurityInterface.setDescription("""\
Security device type - manufacturer independent. A physical connection provided
by a device for the purpose of connecting an external security-related
accessory. This accessory may consist of a card reader or biometric device
which would restrict access to a machine to only authorized users.
""")
_XcmHrDeviceAccountingInterface_ObjectIdentity = ObjectIdentity
xcmHrDeviceAccountingInterface = _XcmHrDeviceAccountingInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 123)
)
if mibBuilder.loadTexts:
    xcmHrDeviceAccountingInterface.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceAccountingInterface.setDescription("""\
Accounting device type - manufacturer independent. A physical connection
provided by a device for the purpose of connecting an external accounting-
related accessory. This accessory would provide the capability to track machine
usage but would not restrict access to the machine as would an accessory
defined by type xcmHrDevicePaymentInterface.
""")
_XcmHrDeviceFeederSFM_ObjectIdentity = ObjectIdentity
xcmHrDeviceFeederSFM = _XcmHrDeviceFeederSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 124)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFeederSFM.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFeederSFM.setDescription("""\
Feeder device type - Xerox Substraite Feeding Module An 'xcmHrDeviceFeederSFM'
device is an input device. An 'xcmHrDeviceFeederSFM' device with
'xcmHrDevInfoRealization' of 'physical' is a 'real' output device (eg, a 'high-
capacity feeder' on a high-end printer). An 'xcmHrDeviceFeeder' device with
'xcmHrDevInfoRealization' of 'logical' is a 'virtual' output device (eg, a
'personality' of a 'high-capacity feeder' on a high-end printer).
""")
_XcmHrDeviceFeederLFF_ObjectIdentity = ObjectIdentity
xcmHrDeviceFeederLFF = _XcmHrDeviceFeederLFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 125)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFeederLFF.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFeederLFF.setDescription("""\
Feeder device type - Xerox Large Format Feeder. An 'xcmHrDeviceFeederLFF'
device is an input device. An 'xcmHrDeviceFeeder' device with
'xcmHrDevInfoRealization' of 'physical' is a 'real' output device (eg, a 'high-
capacity large format feeder' on a high-end printer). An 'xcmHrDeviceFeeder'
device with 'xcmHrDevInfoRealization' of 'logical' is a 'virtual' output device
(eg, a 'personality' of a 'high-capacity large format feeder' on a high-end
printer).
""")
_XcmHrDeviceScannerADF_ObjectIdentity = ObjectIdentity
xcmHrDeviceScannerADF = _XcmHrDeviceScannerADF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 126)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScannerADF.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceScannerADF.setReference("""\
See: 'xcmHrDeviceScannerHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceScannerADF.setDescription("""\
Scanner device type - manufacturer independent automatic document feeding
scanner. An 'xcmHrDeviceScannerADF' device with 'xcmHrDevInfoRealization' of
'physical' is a 'real' input device (eg, a 'scan channel' on a multifunction
printer). An 'xcmHrDeviceScannerADF' device with 'xcmHrDevInfoRealization' of
'logical' is a 'virtual' input device (eg, a 'personality' of a 'scan channel'
on a multifunction printer).
""")
_XcmHrDeviceScannerPlaten_ObjectIdentity = ObjectIdentity
xcmHrDeviceScannerPlaten = _XcmHrDeviceScannerPlaten_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 127)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScannerPlaten.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceScannerPlaten.setReference("""\
See: 'xcmHrDeviceScannerHistory' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceScannerPlaten.setDescription("""\
Scanner device type - manufacturer independent platen glass scanner. An
'xcmHrDeviceScannerPlaten' device with 'xcmHrDevInfoRealization' of 'physical'
is a 'real' input device (eg, a 'scan channel' on a multifunction printer). An
'xcmHrDeviceScannerPlaten' device with 'xcmHrDevInfoRealization' of 'logical'
is a 'virtual' input device (eg, a 'personality' of a 'scan channel' on a
multifunction printer).
""")
_XcmHrDeviceColorScanningCard_ObjectIdentity = ObjectIdentity
xcmHrDeviceColorScanningCard = _XcmHrDeviceColorScanningCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 128)
)
if mibBuilder.loadTexts:
    xcmHrDeviceColorScanningCard.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceColorScanningCard.setDescription("""\
An xcmHrDeviceColorScanningCard is a physical card that allows for scanning of
color, or monochrome, images from the printer to a remote device.
""")
_XcmHrDeviceHostSystemHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceHostSystemHistory = _XcmHrDeviceHostSystemHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 151)
)
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystemHistory.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystemHistory.setReference("""\
See: 'xcmHrDeviceHostSystem' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystemHistory.setDescription("""\
Host system history device type - manufacturer independent.
""")
_XcmHrDeviceScannerHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceScannerHistory = _XcmHrDeviceScannerHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 152)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScannerHistory.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceScannerHistory.setReference("""\
See: 'xcmHrDeviceScanner' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceScannerHistory.setDescription("""\
Scanner history device type - manufacturer independent.
""")
_XcmHrDeviceCopierHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceCopierHistory = _XcmHrDeviceCopierHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 153)
)
if mibBuilder.loadTexts:
    xcmHrDeviceCopierHistory.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceCopierHistory.setReference("""\
See: 'xcmHrDeviceCopier' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceCopierHistory.setDescription("""\
Copier history device type - manufacturer independent.
""")
_XcmHrDeviceFaxHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceFaxHistory = _XcmHrDeviceFaxHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 154)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFaxHistory.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFaxHistory.setReference("""\
See: 'xcmHrDeviceFax' in this XCMI HRX TC.
""")
if mibBuilder.loadTexts:
    xcmHrDeviceFaxHistory.setDescription("""\
Fax history device type - manufacturer independent.
""")
_XcmHrCruXerographicModule_ObjectIdentity = ObjectIdentity
xcmHrCruXerographicModule = _XcmHrCruXerographicModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 201)
)
if mibBuilder.loadTexts:
    xcmHrCruXerographicModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruXerographicModule.setDescription("""\
CRU xerographic module - manufacturer independent. An
'xcmHrCruXerographicModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruFuserModule_ObjectIdentity = ObjectIdentity
xcmHrCruFuserModule = _XcmHrCruFuserModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 202)
)
if mibBuilder.loadTexts:
    xcmHrCruFuserModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruFuserModule.setDescription("""\
CRU fuser module - manufacturer independent. An 'xcmHrCruFuserModule' device is
a customer replaceable unit, with 'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruTonerBottleModule_ObjectIdentity = ObjectIdentity
xcmHrCruTonerBottleModule = _XcmHrCruTonerBottleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 203)
)
if mibBuilder.loadTexts:
    xcmHrCruTonerBottleModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruTonerBottleModule.setDescription("""\
CRU toner bottle module - manufacturer independent. An
'xcmHrCruTonerBottleModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruCollectorBottleModule_ObjectIdentity = ObjectIdentity
xcmHrCruCollectorBottleModule = _XcmHrCruCollectorBottleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 204)
)
if mibBuilder.loadTexts:
    xcmHrCruCollectorBottleModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruCollectorBottleModule.setDescription("""\
CRU (developer) collector bottle - manufacturer independent. An
'xcmHrCruCollectorBottleModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruTrayFeedHeadModule_ObjectIdentity = ObjectIdentity
xcmHrCruTrayFeedHeadModule = _XcmHrCruTrayFeedHeadModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 205)
)
if mibBuilder.loadTexts:
    xcmHrCruTrayFeedHeadModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruTrayFeedHeadModule.setDescription("""\
CRU tray feed head module - manufacturer independent. An
'xcmHrCruTrayFeedHeadModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruAdfFeedHeadModule_ObjectIdentity = ObjectIdentity
xcmHrCruAdfFeedHeadModule = _XcmHrCruAdfFeedHeadModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 206)
)
if mibBuilder.loadTexts:
    xcmHrCruAdfFeedHeadModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruAdfFeedHeadModule.setDescription("""\
CRU ADF feed head module - manufacturer independent. An
'xcmHrCruAdfFeedHeadModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'. Note: ADF is an acronym for 'automatic
document feeder'.
""")
_XcmHrCruFuserWebModule_ObjectIdentity = ObjectIdentity
xcmHrCruFuserWebModule = _XcmHrCruFuserWebModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 207)
)
if mibBuilder.loadTexts:
    xcmHrCruFuserWebModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruFuserWebModule.setDescription("""\
CRU fuser web module - manufacturer independent. An 'xcmHrCruFuserWebModule'
device is a customer replaceable unit, with 'xcmHrDevInfoRealization' of
'physical'. Note: A 'fuser web' is an oil-soaked fiber roll in a fuser, which
prevents toner from getting on the fuser roll. The 'fuser web' device would
normally be replaced several times before the actual fuser device
('xcmHrCRUFuserModule') is replaced.
""")
_XcmHrCruFilterModule_ObjectIdentity = ObjectIdentity
xcmHrCruFilterModule = _XcmHrCruFilterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 208)
)
if mibBuilder.loadTexts:
    xcmHrCruFilterModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruFilterModule.setDescription("""\
CRU filter module - manufacturer independent. An 'xcmHrCruFilterModule' device
is a customer replaceable filter or filter unit, with 'xcmHrDevInfoRealization'
of 'physical'.
""")
_XcmHrCruCleanerUnitModule_ObjectIdentity = ObjectIdentity
xcmHrCruCleanerUnitModule = _XcmHrCruCleanerUnitModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 209)
)
if mibBuilder.loadTexts:
    xcmHrCruCleanerUnitModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruCleanerUnitModule.setReference("""\
See: 'cleanerUnit' in 'PrtMarkerSuppliesTypeTC' in the Printer MIB v2.
""")
if mibBuilder.loadTexts:
    xcmHrCruCleanerUnitModule.setDescription("""\
CRU cleaner unit module - manufacturer independent. An
'xcmHrCruCleanerUnitModule' device is a customer replaceable cleaner unit, with
'xcmHrDevInfoRealization' of 'physical' (eg, a belt cleaner or a photoreceptor
cleaner).
""")
_XcmHrCruTransferUnitModule_ObjectIdentity = ObjectIdentity
xcmHrCruTransferUnitModule = _XcmHrCruTransferUnitModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 210)
)
if mibBuilder.loadTexts:
    xcmHrCruTransferUnitModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruTransferUnitModule.setReference("""\
See: 'transferUnit' in 'PrtMarkerSuppliesTypeTC' in the Printer MIB v2.
""")
if mibBuilder.loadTexts:
    xcmHrCruTransferUnitModule.setDescription("""\
CRU transfer unit module - manufacturer independent. An
'xcmHrCruTransferUnitModule' device is a customer replaceable transfer unit,
with 'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruTransferRollerModule_ObjectIdentity = ObjectIdentity
xcmHrCruTransferRollerModule = _XcmHrCruTransferRollerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 211)
)
if mibBuilder.loadTexts:
    xcmHrCruTransferRollerModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruTransferRollerModule.setReference("""\
See: 'transferUnit' in 'PrtMarkerSuppliesTypeTC' in the Printer MIB v2.
""")
if mibBuilder.loadTexts:
    xcmHrCruTransferRollerModule.setDescription("""\
CRU transfer roller module - manufacturer independent. An
'xcmHrCruTransferRollerModule' device is a customer replaceable transfer
roller, with 'xcmHrDevInfoRealization' of 'physical' (eg, a biased transfer
roller).
""")
_XcmHrCruPFPFeedRollModule_ObjectIdentity = ObjectIdentity
xcmHrCruPFPFeedRollModule = _XcmHrCruPFPFeedRollModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 212)
)
if mibBuilder.loadTexts:
    xcmHrCruPFPFeedRollModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruPFPFeedRollModule.setDescription("""\
CRU Paper Feed Platform module - manufacturer independent. An
'xcmHrCruPaperFeedModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrCruPFPRetardRollModule_ObjectIdentity = ObjectIdentity
xcmHrCruPFPRetardRollModule = _XcmHrCruPFPRetardRollModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 213)
)
if mibBuilder.loadTexts:
    xcmHrCruPFPRetardRollModule.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrCruPFPRetardRollModule.setDescription("""\
CRU PFP Retard Roll module - manufacturer independent. An
'xcmHrCruPFPRetardRollModule' device is a customer replaceable unit, with
'xcmHrDevInfoRealization' of 'physical'.
""")
_XcmHrDeviceUSBPort_ObjectIdentity = ObjectIdentity
xcmHrDeviceUSBPort = _XcmHrDeviceUSBPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 250)
)
if mibBuilder.loadTexts:
    xcmHrDeviceUSBPort.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceUSBPort.setDescription("""\
The device type identifier used for a Universal Serial Bus port.
""")
_XcmHrDeviceFlashDIMMFileStore_ObjectIdentity = ObjectIdentity
xcmHrDeviceFlashDIMMFileStore = _XcmHrDeviceFlashDIMMFileStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 260)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDIMMFileStore.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDIMMFileStore.setDescription("""\
The device type identifier used for a Flash DIMM that contains a file system
that is used to store files such as font files. opposed to a Flash DIMM that
contains a boot loader.
""")
_XcmHrDeviceFlashDIMMBootLoader_ObjectIdentity = ObjectIdentity
xcmHrDeviceFlashDIMMBootLoader = _XcmHrDeviceFlashDIMMBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 261)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDIMMBootLoader.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDIMMBootLoader.setDescription("""\
The device type identifier used for a Flash DIMM that contains the boot loader
for a device. Files may or may not be stored o this device. As opposed to a
Flash DIMM that contains a file store system.
""")
_XcmHrDeviceFlashDrive_ObjectIdentity = ObjectIdentity
xcmHrDeviceFlashDrive = _XcmHrDeviceFlashDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 262)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDrive.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDrive.setDescription("""\
The device type identifier used for a Flash Drive for a device Files may or may
not be stored on this device. As opposed to a Flash DIMM that contains a file
store system or a bootloader.
""")
_XcmHrAdminServiceTypes_ObjectIdentity = ObjectIdentity
xcmHrAdminServiceTypes = _XcmHrAdminServiceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3)
)
if mibBuilder.loadTexts:
    xcmHrAdminServiceTypes.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminServiceTypes.setReference("""\
See: 'XcmSecPosixVerbs' and 'xcmSecServiceTypeOID' in XCMI Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminServiceTypes.setDescription("""\
The root of all host system management service types (classes) defined in the
Host Resources Extensions TC.
""")
_XcmHrAdminObjectService_ObjectIdentity = ObjectIdentity
xcmHrAdminObjectService = _XcmHrAdminObjectService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 1)
)
if mibBuilder.loadTexts:
    xcmHrAdminObjectService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminObjectService.setReference("""\
See: 'xcmSysAdminObject...' in XCMI System Admin MIB. See: 'XcmSecPosixVerbs'
and 'xcmSecServiceTypeOID' in XCMI Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminObjectService.setDescription("""\
The host system object management service.
""")
_XcmHrAdminServerService_ObjectIdentity = ObjectIdentity
xcmHrAdminServerService = _XcmHrAdminServerService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 2)
)
if mibBuilder.loadTexts:
    xcmHrAdminServerService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminServerService.setReference("""\
See: 'xcmSysAdminServer...' in XCMI System Admin MIB,
'hrSW[Running|Installed]Table' in IETF HR MIB, and
'xcmHrSW[Running|Installed]ExtTable' in XCMI HRX MIB. See: 'XcmSecPosixVerbs'
and 'xcmSecServiceTypeOID' in XCMI Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminServerService.setDescription("""\
The host system server management service.
""")
_XcmHrAdminDeviceService_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceService = _XcmHrAdminDeviceService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 3)
)
if mibBuilder.loadTexts:
    xcmHrAdminDeviceService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminDeviceService.setReference("""\
See: 'xcmSysAdminDevice...' in XCMI System Admin MIB, 'hrDeviceTable' in IETF
HR MIB, and 'xcmHrDev[Info|Help|Mgmt|Power|Traffic|Calendar]Table' in XCMI HRX
MIB. See: 'XcmSecPosixVerbs' and 'xcmSecServiceTypeOID' in XCMI Security
TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminDeviceService.setDescription("""\
The host system device management service.
""")
_XcmHrAdminJobService_ObjectIdentity = ObjectIdentity
xcmHrAdminJobService = _XcmHrAdminJobService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 4)
)
if mibBuilder.loadTexts:
    xcmHrAdminJobService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminJobService.setReference("""\
See: 'xcmSysAdminJob...' in XCMI System Admin MIB, and 'xcmJob[...]Table' in
XCMI Job Monitoring MIB. See: 'XcmSecPosixVerbs' and 'xcmSecServiceTypeOID' in
XCMI Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminJobService.setDescription("""\
The host system job management service.
""")
_XcmHrAdminDocService_ObjectIdentity = ObjectIdentity
xcmHrAdminDocService = _XcmHrAdminDocService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 5)
)
if mibBuilder.loadTexts:
    xcmHrAdminDocService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminDocService.setReference("""\
See: 'xcmSysAdminDoc...' in XCMI System Admin MIB, and 'xcmDoc[...]Table' in
XCMI Job Monitoring MIB. See: 'XcmSecPosixVerbs' and 'xcmSecServiceTypeOID' in
XCMI Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminDocService.setDescription("""\
The host system document management service.
""")
_XcmHrAdminSecurityService_ObjectIdentity = ObjectIdentity
xcmHrAdminSecurityService = _XcmHrAdminSecurityService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 6)
)
if mibBuilder.loadTexts:
    xcmHrAdminSecurityService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminSecurityService.setReference("""\
See: 'xcmSysAdminSecurity...' in XCMI System Admin MIB. See: 'XcmSecPosixVerbs'
and 'xcmSecServiceTypeOID' in XCMI Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminSecurityService.setDescription("""\
The host system security management service.
""")
_XcmHrAdminCommsService_ObjectIdentity = ObjectIdentity
xcmHrAdminCommsService = _XcmHrAdminCommsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 7)
)
if mibBuilder.loadTexts:
    xcmHrAdminCommsService.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminCommsService.setReference("""\
See: 'xcmSysAdminComms...' in XCMI System Admin MIB and XCMI Comms Config and
Comms Engine MIBs. See: 'XcmSecPosixVerbs' and 'xcmSecServiceTypeOID' in XCMI
Security TC/MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminCommsService.setDescription("""\
The host system communications management service.
""")
_XcmHrAdminDeviceOperationTypes_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceOperationTypes = _XcmHrAdminDeviceOperationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4)
)
if mibBuilder.loadTexts:
    xcmHrAdminDeviceOperationTypes.setStatus("current")
if mibBuilder.loadTexts:
    xcmHrAdminDeviceOperationTypes.setReference("""\
See: 'xcmSec[Master|Policy]VerbTypeOID' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmHrAdminDeviceOperationTypes.setDescription("""\
The root of all host resources admin device operation types defined in the Host
Resources Extensions TC. Usage: The following OIDs support access control for
the simple device admin operations defined in 'XcmHrDevMgmtCommandRequest' and
used in 'xcmHrDevMgmtCommandRequest' in the XCMI HRX MIB, via
'xcmSec[Master|Policy]VerbTypeOID' in the XCMI Security MIB, WITHOUT requiring
implementation of the XCMI System Admin MIB.
""")
_XcmHrAdminDeviceNone_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceNone = _XcmHrAdminDeviceNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 1)
)
_XcmHrAdminDeviceStartup_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceStartup = _XcmHrAdminDeviceStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 2)
)
_XcmHrAdminDeviceResetWarning_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceResetWarning = _XcmHrAdminDeviceResetWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 3)
)
_XcmHrAdminDeviceTest_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceTest = _XcmHrAdminDeviceTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 4)
)
_XcmHrAdminDeviceShutdown_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceShutdown = _XcmHrAdminDeviceShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 5)
)
_XcmHrAdminDeviceQuiesce_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceQuiesce = _XcmHrAdminDeviceQuiesce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 6)
)
_XcmHrAdminDeviceResetCounters_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceResetCounters = _XcmHrAdminDeviceResetCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 7)
)
_XcmHrAdminDeviceResetWarm_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceResetWarm = _XcmHrAdminDeviceResetWarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 8)
)
_XcmHrAdminDeviceResetCold_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceResetCold = _XcmHrAdminDeviceResetCold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 9)
)
_XcmHrAdminDeviceResetFactory_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceResetFactory = _XcmHrAdminDeviceResetFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 10)
)
_XcmHrAdminDeviceFlushInput_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceFlushInput = _XcmHrAdminDeviceFlushInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 11)
)
_XcmHrAdminDeviceFlushOutput_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceFlushOutput = _XcmHrAdminDeviceFlushOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 12)
)
_XcmHrAdminDeviceFlushInOut_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceFlushInOut = _XcmHrAdminDeviceFlushInOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 13)
)
_XcmHrAdminDeviceManage_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceManage = _XcmHrAdminDeviceManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 14)
)
_XcmHrAdminDeviceRefresh_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceRefresh = _XcmHrAdminDeviceRefresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 15)
)
_XcmHrAdminDeviceWarmUp_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceWarmUp = _XcmHrAdminDeviceWarmUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 16)
)
_XcmHrAdminDeviceCoolDown_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceCoolDown = _XcmHrAdminDeviceCoolDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 17)
)
_XcmHrAdminDeviceEnergySave_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceEnergySave = _XcmHrAdminDeviceEnergySave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 18)
)
_XcmHrAdminDeviceWakeUp_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceWakeUp = _XcmHrAdminDeviceWakeUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 19)
)
_XcmHrAdminDevicePowerToReady_ObjectIdentity = ObjectIdentity
xcmHrAdminDevicePowerToReady = _XcmHrAdminDevicePowerToReady_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 20)
)
_XcmHrAdminDevicePowerToStandby_ObjectIdentity = ObjectIdentity
xcmHrAdminDevicePowerToStandby = _XcmHrAdminDevicePowerToStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 21)
)
_XcmHrAdminDevicePowerToSleep_ObjectIdentity = ObjectIdentity
xcmHrAdminDevicePowerToSleep = _XcmHrAdminDevicePowerToSleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4, 22)
)
_XCmHrDummy_ObjectIdentity = ObjectIdentity
xCmHrDummy = _XCmHrDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999)
)
_XCmHrDevCalendarDayOfWeek_Type = XcmHrDevCalendarDayOfWeek
_XCmHrDevCalendarDayOfWeek_Object = MibScalar
xCmHrDevCalendarDayOfWeek = _XCmHrDevCalendarDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 1),
    _XCmHrDevCalendarDayOfWeek_Type()
)
xCmHrDevCalendarDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevCalendarDayOfWeek.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevCalendarDayOfWeek.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevCalendarTimeOfDay_Type = XcmHrDevCalendarTimeOfDay
_XCmHrDevCalendarTimeOfDay_Object = MibScalar
xCmHrDevCalendarTimeOfDay = _XCmHrDevCalendarTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 2),
    _XCmHrDevCalendarTimeOfDay_Type()
)
xCmHrDevCalendarTimeOfDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevCalendarTimeOfDay.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevCalendarTimeOfDay.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevDetailType_Type = XcmHrDevDetailType
_XCmHrDevDetailType_Object = MibScalar
xCmHrDevDetailType = _XCmHrDevDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 3),
    _XCmHrDevDetailType_Type()
)
xCmHrDevDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevDetailType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevDetailUnitClass_Type = XcmHrDevDetailUnitClass
_XCmHrDevDetailUnitClass_Object = MibScalar
xCmHrDevDetailUnitClass = _XCmHrDevDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 4),
    _XCmHrDevDetailUnitClass_Type()
)
xCmHrDevDetailUnitClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevDetailUnitClass.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevDetailUnitClass.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevInfoRealization_Type = XcmHrDevInfoRealization
_XCmHrDevInfoRealization_Object = MibScalar
xCmHrDevInfoRealization = _XCmHrDevInfoRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 5),
    _XCmHrDevInfoRealization_Type()
)
xCmHrDevInfoRealization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoRealization.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevInfoRealization.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevInfoStatus_Type = XcmHrDevInfoStatus
_XCmHrDevInfoStatus_Object = MibScalar
xCmHrDevInfoStatus = _XCmHrDevInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 6),
    _XCmHrDevInfoStatus_Type()
)
xCmHrDevInfoStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoStatus.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevInfoStatus.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevInfoXStatus_Type = XcmHrDevInfoXStatus
_XCmHrDevInfoXStatus_Object = MibScalar
xCmHrDevInfoXStatus = _XCmHrDevInfoXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 7),
    _XCmHrDevInfoXStatus_Type()
)
xCmHrDevInfoXStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoXStatus.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevInfoXStatus.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevInfoConditions_Type = XcmHrDevInfoConditions
_XCmHrDevInfoConditions_Object = MibScalar
xCmHrDevInfoConditions = _XCmHrDevInfoConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 8),
    _XCmHrDevInfoConditions_Type()
)
xCmHrDevInfoConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoConditions.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevInfoConditions.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevInfoXConditions_Type = XcmHrDevInfoXConditions
_XCmHrDevInfoXConditions_Object = MibScalar
xCmHrDevInfoXConditions = _XCmHrDevInfoXConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 9),
    _XCmHrDevInfoXConditions_Type()
)
xCmHrDevInfoXConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoXConditions.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevInfoXConditions.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevMgmtCommandRequest_Type = XcmHrDevMgmtCommandRequest
_XCmHrDevMgmtCommandRequest_Object = MibScalar
xCmHrDevMgmtCommandRequest = _XCmHrDevMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 10),
    _XCmHrDevMgmtCommandRequest_Type()
)
xCmHrDevMgmtCommandRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandRequest.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandRequest.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevMgmtCommandData_Type = XcmHrDevMgmtCommandData
_XCmHrDevMgmtCommandData_Object = MibScalar
xCmHrDevMgmtCommandData = _XCmHrDevMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 11),
    _XCmHrDevMgmtCommandData_Type()
)
xCmHrDevMgmtCommandData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandData.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandData.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevMgmtCommandDataTag_Type = XcmHrDevMgmtCommandDataTag
_XCmHrDevMgmtCommandDataTag_Object = MibScalar
xCmHrDevMgmtCommandDataTag = _XCmHrDevMgmtCommandDataTag_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 12),
    _XCmHrDevMgmtCommandDataTag_Type()
)
xCmHrDevMgmtCommandDataTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandDataTag.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandDataTag.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevPowerModeType_Type = XcmHrDevPowerModeType
_XCmHrDevPowerModeType_Object = MibScalar
xCmHrDevPowerModeType = _XCmHrDevPowerModeType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 13),
    _XCmHrDevPowerModeType_Type()
)
xCmHrDevPowerModeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevPowerModeType.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevPowerModeType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevPowerTimeUnit_Type = XcmHrDevPowerTimeUnit
_XCmHrDevPowerTimeUnit_Object = MibScalar
xCmHrDevPowerTimeUnit = _XCmHrDevPowerTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 14),
    _XCmHrDevPowerTimeUnit_Type()
)
xCmHrDevPowerTimeUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevPowerTimeUnit.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevPowerTimeUnit.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDevTrafficUnit_Type = XcmHrDevTrafficUnit
_XCmHrDevTrafficUnit_Object = MibScalar
xCmHrDevTrafficUnit = _XCmHrDevTrafficUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 15),
    _XCmHrDevTrafficUnit_Type()
)
xCmHrDevTrafficUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevTrafficUnit.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDevTrafficUnit.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrGroupSupport_Type = XcmHrGroupSupport
_XCmHrGroupSupport_Object = MibScalar
xCmHrGroupSupport = _XCmHrGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 16),
    _XCmHrGroupSupport_Type()
)
xCmHrGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrGroupSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrSWRunXStatus_Type = XcmHrSWRunXStatus
_XCmHrSWRunXStatus_Object = MibScalar
xCmHrSWRunXStatus = _XCmHrSWRunXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 17),
    _XCmHrSWRunXStatus_Type()
)
xCmHrSWRunXStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrSWRunXStatus.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrSWRunXStatus.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrStorageDetailType_Type = XcmHrStorageDetailType
_XCmHrStorageDetailType_Object = MibScalar
xCmHrStorageDetailType = _XCmHrStorageDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 18),
    _XCmHrStorageDetailType_Type()
)
xCmHrStorageDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrStorageDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrStorageDetailType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrStorageRealization_Type = XcmHrStorageRealization
_XCmHrStorageRealization_Object = MibScalar
xCmHrStorageRealization = _XCmHrStorageRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 19),
    _XCmHrStorageRealization_Type()
)
xCmHrStorageRealization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrStorageRealization.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrStorageRealization.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDpaAvailability_Type = XcmHrDpaAvailability
_XCmHrDpaAvailability_Object = MibScalar
xCmHrDpaAvailability = _XCmHrDpaAvailability_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 20),
    _XCmHrDpaAvailability_Type()
)
xCmHrDpaAvailability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaAvailability.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDpaAvailability.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDpaConditions_Type = XcmHrDpaConditions
_XCmHrDpaConditions_Object = MibScalar
xCmHrDpaConditions = _XCmHrDpaConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 21),
    _XCmHrDpaConditions_Type()
)
xCmHrDpaConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaConditions.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDpaConditions.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDpaJobValidateSupport_Type = XcmHrDpaJobValidateSupport
_XCmHrDpaJobValidateSupport_Object = MibScalar
xCmHrDpaJobValidateSupport = _XCmHrDpaJobValidateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 22),
    _XCmHrDpaJobValidateSupport_Type()
)
xCmHrDpaJobValidateSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaJobValidateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDpaJobValidateSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDpaObjectClassSupport_Type = XcmHrDpaObjectClassSupport
_XCmHrDpaObjectClassSupport_Object = MibScalar
xCmHrDpaObjectClassSupport = _XCmHrDpaObjectClassSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 23),
    _XCmHrDpaObjectClassSupport_Type()
)
xCmHrDpaObjectClassSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaObjectClassSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDpaObjectClassSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDpaState_Type = XcmHrDpaState
_XCmHrDpaState_Object = MibScalar
xCmHrDpaState = _XCmHrDpaState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 24),
    _XCmHrDpaState_Type()
)
xCmHrDpaState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaState.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDpaState.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrDetailTableEnumTC_Type = XcmHrDetailTableEnumTC
_XCmHrDetailTableEnumTC_Object = MibScalar
xCmHrDetailTableEnumTC = _XCmHrDetailTableEnumTC_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 25),
    _XCmHrDetailTableEnumTC_Type()
)
xCmHrDetailTableEnumTC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDetailTableEnumTC.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrDetailTableEnumTC.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrSuppliesClassTC_Type = XcmHrSuppliesClassTC
_XCmHrSuppliesClassTC_Object = MibScalar
xCmHrSuppliesClassTC = _XCmHrSuppliesClassTC_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 26),
    _XCmHrSuppliesClassTC_Type()
)
xCmHrSuppliesClassTC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrSuppliesClassTC.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrSuppliesClassTC.setDescription("""\
Dummy - DO NOT USE
""")
_XCmHrConsoleDefaultService_Type = XcmHrConsoleDefaultService
_XCmHrConsoleDefaultService_Object = MibScalar
xCmHrConsoleDefaultService = _XCmHrConsoleDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 27),
    _XCmHrConsoleDefaultService_Type()
)
xCmHrConsoleDefaultService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrConsoleDefaultService.setStatus("current")
if mibBuilder.loadTexts:
    xCmHrConsoleDefaultService.setDescription("""\
Dummy - DO NOT USE
""")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    **{"XcmHrDevCalendarDayOfWeek": XcmHrDevCalendarDayOfWeek,
       "XcmHrDevCalendarTimeOfDay": XcmHrDevCalendarTimeOfDay,
       "XcmHrDevDetailType": XcmHrDevDetailType,
       "XcmHrDevDetailUnitClass": XcmHrDevDetailUnitClass,
       "XcmHrDevInfoRealization": XcmHrDevInfoRealization,
       "XcmHrDevInfoStatus": XcmHrDevInfoStatus,
       "XcmHrDevInfoXStatus": XcmHrDevInfoXStatus,
       "XcmHrDevInfoConditions": XcmHrDevInfoConditions,
       "XcmHrDevInfoXConditions": XcmHrDevInfoXConditions,
       "XcmHrDeviceStatusType": XcmHrDeviceStatusType,
       "XcmHrDevMgmtCommandRequest": XcmHrDevMgmtCommandRequest,
       "XcmHrDevMgmtCommandData": XcmHrDevMgmtCommandData,
       "XcmHrDevMgmtCommandDataTag": XcmHrDevMgmtCommandDataTag,
       "XcmHrDevPowerModeType": XcmHrDevPowerModeType,
       "XcmHrDevPowerTimeUnit": XcmHrDevPowerTimeUnit,
       "XcmHrDevTrafficUnit": XcmHrDevTrafficUnit,
       "XcmHrGroupSupport": XcmHrGroupSupport,
       "XcmHrSWRunXStatus": XcmHrSWRunXStatus,
       "XcmHrStorageDetailType": XcmHrStorageDetailType,
       "XcmHrStorageRealization": XcmHrStorageRealization,
       "XcmHrDpaAvailability": XcmHrDpaAvailability,
       "XcmHrDpaConditions": XcmHrDpaConditions,
       "XcmHrDpaJobValidateSupport": XcmHrDpaJobValidateSupport,
       "XcmHrDpaObjectClassSupport": XcmHrDpaObjectClassSupport,
       "XcmHrDpaState": XcmHrDpaState,
       "XcmHrSuppliesClassTC": XcmHrSuppliesClassTC,
       "XcmHrDetailTableEnumTC": XcmHrDetailTableEnumTC,
       "XcmHrConsoleDefaultService": XcmHrConsoleDefaultService,
       "xcmHrTC": xcmHrTC,
       "xcmHrDeviceTypes": xcmHrDeviceTypes,
       "xcmHrDevicePrinterHistory": xcmHrDevicePrinterHistory,
       "xcmHrDeviceHostSystem": xcmHrDeviceHostSystem,
       "xcmHrDeviceScanner": xcmHrDeviceScanner,
       "xcmHrDeviceCopier": xcmHrDeviceCopier,
       "xcmHrDeviceFax": xcmHrDeviceFax,
       "xcmHrDeviceMailbox": xcmHrDeviceMailbox,
       "xcmHrDeviceFinisher": xcmHrDeviceFinisher,
       "xcmHrDeviceFeeder": xcmHrDeviceFeeder,
       "xcmHrDeviceSorter": xcmHrDeviceSorter,
       "xcmHrDeviceMailboxSorter": xcmHrDeviceMailboxSorter,
       "xcmHrDevicePrintAppliance": xcmHrDevicePrintAppliance,
       "xcmHrDeviceMarker": xcmHrDeviceMarker,
       "xcmHrDeviceFinisherBFM": xcmHrDeviceFinisherBFM,
       "xcmHrDeviceFinisherMFF": xcmHrDeviceFinisherMFF,
       "xcmHrDeviceFinisherXIM": xcmHrDeviceFinisherXIM,
       "xcmHrDeviceFinisher3rdParty": xcmHrDeviceFinisher3rdParty,
       "xcmHrDevicePaymentInterface": xcmHrDevicePaymentInterface,
       "xcmHrDeviceInterposer": xcmHrDeviceInterposer,
       "xcmHrDeviceInternetFax": xcmHrDeviceInternetFax,
       "xcmHrDeviceServerFax": xcmHrDeviceServerFax,
       "xcmHrDeviceEmbeddedFax": xcmHrDeviceEmbeddedFax,
       "xcmHrDeviceForeignInterface": xcmHrDeviceForeignInterface,
       "xcmHrDeviceSecurityInterface": xcmHrDeviceSecurityInterface,
       "xcmHrDeviceAccountingInterface": xcmHrDeviceAccountingInterface,
       "xcmHrDeviceFeederSFM": xcmHrDeviceFeederSFM,
       "xcmHrDeviceFeederLFF": xcmHrDeviceFeederLFF,
       "xcmHrDeviceScannerADF": xcmHrDeviceScannerADF,
       "xcmHrDeviceScannerPlaten": xcmHrDeviceScannerPlaten,
       "xcmHrDeviceColorScanningCard": xcmHrDeviceColorScanningCard,
       "xcmHrDeviceHostSystemHistory": xcmHrDeviceHostSystemHistory,
       "xcmHrDeviceScannerHistory": xcmHrDeviceScannerHistory,
       "xcmHrDeviceCopierHistory": xcmHrDeviceCopierHistory,
       "xcmHrDeviceFaxHistory": xcmHrDeviceFaxHistory,
       "xcmHrCruXerographicModule": xcmHrCruXerographicModule,
       "xcmHrCruFuserModule": xcmHrCruFuserModule,
       "xcmHrCruTonerBottleModule": xcmHrCruTonerBottleModule,
       "xcmHrCruCollectorBottleModule": xcmHrCruCollectorBottleModule,
       "xcmHrCruTrayFeedHeadModule": xcmHrCruTrayFeedHeadModule,
       "xcmHrCruAdfFeedHeadModule": xcmHrCruAdfFeedHeadModule,
       "xcmHrCruFuserWebModule": xcmHrCruFuserWebModule,
       "xcmHrCruFilterModule": xcmHrCruFilterModule,
       "xcmHrCruCleanerUnitModule": xcmHrCruCleanerUnitModule,
       "xcmHrCruTransferUnitModule": xcmHrCruTransferUnitModule,
       "xcmHrCruTransferRollerModule": xcmHrCruTransferRollerModule,
       "xcmHrCruPFPFeedRollModule": xcmHrCruPFPFeedRollModule,
       "xcmHrCruPFPRetardRollModule": xcmHrCruPFPRetardRollModule,
       "xcmHrDeviceUSBPort": xcmHrDeviceUSBPort,
       "xcmHrDeviceFlashDIMMFileStore": xcmHrDeviceFlashDIMMFileStore,
       "xcmHrDeviceFlashDIMMBootLoader": xcmHrDeviceFlashDIMMBootLoader,
       "xcmHrDeviceFlashDrive": xcmHrDeviceFlashDrive,
       "xcmHrAdminServiceTypes": xcmHrAdminServiceTypes,
       "xcmHrAdminObjectService": xcmHrAdminObjectService,
       "xcmHrAdminServerService": xcmHrAdminServerService,
       "xcmHrAdminDeviceService": xcmHrAdminDeviceService,
       "xcmHrAdminJobService": xcmHrAdminJobService,
       "xcmHrAdminDocService": xcmHrAdminDocService,
       "xcmHrAdminSecurityService": xcmHrAdminSecurityService,
       "xcmHrAdminCommsService": xcmHrAdminCommsService,
       "xcmHrAdminDeviceOperationTypes": xcmHrAdminDeviceOperationTypes,
       "xcmHrAdminDeviceNone": xcmHrAdminDeviceNone,
       "xcmHrAdminDeviceStartup": xcmHrAdminDeviceStartup,
       "xcmHrAdminDeviceResetWarning": xcmHrAdminDeviceResetWarning,
       "xcmHrAdminDeviceTest": xcmHrAdminDeviceTest,
       "xcmHrAdminDeviceShutdown": xcmHrAdminDeviceShutdown,
       "xcmHrAdminDeviceQuiesce": xcmHrAdminDeviceQuiesce,
       "xcmHrAdminDeviceResetCounters": xcmHrAdminDeviceResetCounters,
       "xcmHrAdminDeviceResetWarm": xcmHrAdminDeviceResetWarm,
       "xcmHrAdminDeviceResetCold": xcmHrAdminDeviceResetCold,
       "xcmHrAdminDeviceResetFactory": xcmHrAdminDeviceResetFactory,
       "xcmHrAdminDeviceFlushInput": xcmHrAdminDeviceFlushInput,
       "xcmHrAdminDeviceFlushOutput": xcmHrAdminDeviceFlushOutput,
       "xcmHrAdminDeviceFlushInOut": xcmHrAdminDeviceFlushInOut,
       "xcmHrAdminDeviceManage": xcmHrAdminDeviceManage,
       "xcmHrAdminDeviceRefresh": xcmHrAdminDeviceRefresh,
       "xcmHrAdminDeviceWarmUp": xcmHrAdminDeviceWarmUp,
       "xcmHrAdminDeviceCoolDown": xcmHrAdminDeviceCoolDown,
       "xcmHrAdminDeviceEnergySave": xcmHrAdminDeviceEnergySave,
       "xcmHrAdminDeviceWakeUp": xcmHrAdminDeviceWakeUp,
       "xcmHrAdminDevicePowerToReady": xcmHrAdminDevicePowerToReady,
       "xcmHrAdminDevicePowerToStandby": xcmHrAdminDevicePowerToStandby,
       "xcmHrAdminDevicePowerToSleep": xcmHrAdminDevicePowerToSleep,
       "xCmHrDummy": xCmHrDummy,
       "xCmHrDevCalendarDayOfWeek": xCmHrDevCalendarDayOfWeek,
       "xCmHrDevCalendarTimeOfDay": xCmHrDevCalendarTimeOfDay,
       "xCmHrDevDetailType": xCmHrDevDetailType,
       "xCmHrDevDetailUnitClass": xCmHrDevDetailUnitClass,
       "xCmHrDevInfoRealization": xCmHrDevInfoRealization,
       "xCmHrDevInfoStatus": xCmHrDevInfoStatus,
       "xCmHrDevInfoXStatus": xCmHrDevInfoXStatus,
       "xCmHrDevInfoConditions": xCmHrDevInfoConditions,
       "xCmHrDevInfoXConditions": xCmHrDevInfoXConditions,
       "xCmHrDevMgmtCommandRequest": xCmHrDevMgmtCommandRequest,
       "xCmHrDevMgmtCommandData": xCmHrDevMgmtCommandData,
       "xCmHrDevMgmtCommandDataTag": xCmHrDevMgmtCommandDataTag,
       "xCmHrDevPowerModeType": xCmHrDevPowerModeType,
       "xCmHrDevPowerTimeUnit": xCmHrDevPowerTimeUnit,
       "xCmHrDevTrafficUnit": xCmHrDevTrafficUnit,
       "xCmHrGroupSupport": xCmHrGroupSupport,
       "xCmHrSWRunXStatus": xCmHrSWRunXStatus,
       "xCmHrStorageDetailType": xCmHrStorageDetailType,
       "xCmHrStorageRealization": xCmHrStorageRealization,
       "xCmHrDpaAvailability": xCmHrDpaAvailability,
       "xCmHrDpaConditions": xCmHrDpaConditions,
       "xCmHrDpaJobValidateSupport": xCmHrDpaJobValidateSupport,
       "xCmHrDpaObjectClassSupport": xCmHrDpaObjectClassSupport,
       "xCmHrDpaState": xCmHrDpaState,
       "xCmHrDetailTableEnumTC": xCmHrDetailTableEnumTC,
       "xCmHrSuppliesClassTC": xCmHrSuppliesClassTC,
       "xCmHrConsoleDefaultService": xCmHrConsoleDefaultService}
)
