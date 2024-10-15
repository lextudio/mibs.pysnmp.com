# SNMP MIB module (XEROX-HOST-RESOURCES-EXT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-HOST-RESOURCES-EXT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:17 2024
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

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmHrTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmHrDevCalendarDayOfWeek(Integer32, TextualConvention):
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



class XcmHrDevCalendarTimeOfDay(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12359),
    )



class XcmHrDevDetailType(Integer32, TextualConvention):
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



class XcmHrDevDetailUnitClass(Integer32, TextualConvention):
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



class XcmHrDevInfoRealization(Integer32, TextualConvention):
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



class XcmHrDevInfoStatus(Integer32, TextualConvention):
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



class XcmHrDevInfoXStatus(Integer32, TextualConvention):
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



class XcmHrDevInfoConditions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmHrDevInfoXConditions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmHrDeviceStatusType(Integer32, TextualConvention):
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



class XcmHrDevMgmtCommandRequest(Integer32, TextualConvention):
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



class XcmHrDevMgmtCommandData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class XcmHrDevMgmtCommandDataTag(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class XcmHrDevPowerModeType(Integer32, TextualConvention):
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



class XcmHrDevPowerTimeUnit(Integer32, TextualConvention):
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



class XcmHrDevTrafficUnit(Integer32, TextualConvention):
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



class XcmHrGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmHrSWRunXStatus(Integer32, TextualConvention):
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



class XcmHrStorageDetailType(Integer32, TextualConvention):
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



class XcmHrStorageRealization(Integer32, TextualConvention):
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



class XcmHrDpaAvailability(Integer32, TextualConvention):
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



class XcmHrDpaConditions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmHrDpaJobValidateSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmHrDpaObjectClassSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmHrDpaState(Integer32, TextualConvention):
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



class XcmHrSuppliesClassTC(Integer32, TextualConvention):
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



class XcmHrDetailTableEnumTC(Integer32, TextualConvention):
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



class XcmHrConsoleDefaultService(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_XcmHrDeviceTypes_ObjectIdentity = ObjectIdentity
xcmHrDeviceTypes = _XcmHrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2)
)
if mibBuilder.loadTexts:
    xcmHrDeviceTypes.setStatus("current")
_XcmHrDevicePrinterHistory_ObjectIdentity = ObjectIdentity
xcmHrDevicePrinterHistory = _XcmHrDevicePrinterHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 55)
)
if mibBuilder.loadTexts:
    xcmHrDevicePrinterHistory.setStatus("current")
_XcmHrDeviceHostSystem_ObjectIdentity = ObjectIdentity
xcmHrDeviceHostSystem = _XcmHrDeviceHostSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 101)
)
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystem.setStatus("current")
_XcmHrDeviceScanner_ObjectIdentity = ObjectIdentity
xcmHrDeviceScanner = _XcmHrDeviceScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 102)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScanner.setStatus("current")
_XcmHrDeviceCopier_ObjectIdentity = ObjectIdentity
xcmHrDeviceCopier = _XcmHrDeviceCopier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 103)
)
if mibBuilder.loadTexts:
    xcmHrDeviceCopier.setStatus("current")
_XcmHrDeviceFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceFax = _XcmHrDeviceFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 104)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFax.setStatus("current")
_XcmHrDeviceMailbox_ObjectIdentity = ObjectIdentity
xcmHrDeviceMailbox = _XcmHrDeviceMailbox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 105)
)
if mibBuilder.loadTexts:
    xcmHrDeviceMailbox.setStatus("current")
_XcmHrDeviceFinisher_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisher = _XcmHrDeviceFinisher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 106)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisher.setStatus("current")
_XcmHrDeviceFeeder_ObjectIdentity = ObjectIdentity
xcmHrDeviceFeeder = _XcmHrDeviceFeeder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 107)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFeeder.setStatus("current")
_XcmHrDeviceSorter_ObjectIdentity = ObjectIdentity
xcmHrDeviceSorter = _XcmHrDeviceSorter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 108)
)
if mibBuilder.loadTexts:
    xcmHrDeviceSorter.setStatus("current")
_XcmHrDeviceMailboxSorter_ObjectIdentity = ObjectIdentity
xcmHrDeviceMailboxSorter = _XcmHrDeviceMailboxSorter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 109)
)
if mibBuilder.loadTexts:
    xcmHrDeviceMailboxSorter.setStatus("current")
_XcmHrDevicePrintAppliance_ObjectIdentity = ObjectIdentity
xcmHrDevicePrintAppliance = _XcmHrDevicePrintAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 110)
)
if mibBuilder.loadTexts:
    xcmHrDevicePrintAppliance.setStatus("current")
_XcmHrDeviceMarker_ObjectIdentity = ObjectIdentity
xcmHrDeviceMarker = _XcmHrDeviceMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 111)
)
if mibBuilder.loadTexts:
    xcmHrDeviceMarker.setStatus("current")
_XcmHrDeviceFinisherBFM_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisherBFM = _XcmHrDeviceFinisherBFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 112)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherBFM.setStatus("current")
_XcmHrDeviceFinisherMFF_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisherMFF = _XcmHrDeviceFinisherMFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 113)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherMFF.setStatus("current")
_XcmHrDeviceFinisherXIM_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisherXIM = _XcmHrDeviceFinisherXIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 114)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisherXIM.setStatus("current")
_XcmHrDeviceFinisher3rdParty_ObjectIdentity = ObjectIdentity
xcmHrDeviceFinisher3rdParty = _XcmHrDeviceFinisher3rdParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 115)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFinisher3rdParty.setStatus("current")
_XcmHrDevicePaymentInterface_ObjectIdentity = ObjectIdentity
xcmHrDevicePaymentInterface = _XcmHrDevicePaymentInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 116)
)
if mibBuilder.loadTexts:
    xcmHrDevicePaymentInterface.setStatus("current")
_XcmHrDeviceInterposer_ObjectIdentity = ObjectIdentity
xcmHrDeviceInterposer = _XcmHrDeviceInterposer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 117)
)
if mibBuilder.loadTexts:
    xcmHrDeviceInterposer.setStatus("current")
_XcmHrDeviceInternetFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceInternetFax = _XcmHrDeviceInternetFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 118)
)
if mibBuilder.loadTexts:
    xcmHrDeviceInternetFax.setStatus("current")
_XcmHrDeviceServerFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceServerFax = _XcmHrDeviceServerFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 119)
)
if mibBuilder.loadTexts:
    xcmHrDeviceServerFax.setStatus("current")
_XcmHrDeviceEmbeddedFax_ObjectIdentity = ObjectIdentity
xcmHrDeviceEmbeddedFax = _XcmHrDeviceEmbeddedFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 120)
)
if mibBuilder.loadTexts:
    xcmHrDeviceEmbeddedFax.setStatus("current")
_XcmHrDeviceForeignInterface_ObjectIdentity = ObjectIdentity
xcmHrDeviceForeignInterface = _XcmHrDeviceForeignInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 121)
)
if mibBuilder.loadTexts:
    xcmHrDeviceForeignInterface.setStatus("current")
_XcmHrDeviceSecurityInterface_ObjectIdentity = ObjectIdentity
xcmHrDeviceSecurityInterface = _XcmHrDeviceSecurityInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 122)
)
if mibBuilder.loadTexts:
    xcmHrDeviceSecurityInterface.setStatus("current")
_XcmHrDeviceAccountingInterface_ObjectIdentity = ObjectIdentity
xcmHrDeviceAccountingInterface = _XcmHrDeviceAccountingInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 123)
)
if mibBuilder.loadTexts:
    xcmHrDeviceAccountingInterface.setStatus("current")
_XcmHrDeviceFeederSFM_ObjectIdentity = ObjectIdentity
xcmHrDeviceFeederSFM = _XcmHrDeviceFeederSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 124)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFeederSFM.setStatus("current")
_XcmHrDeviceFeederLFF_ObjectIdentity = ObjectIdentity
xcmHrDeviceFeederLFF = _XcmHrDeviceFeederLFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 125)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFeederLFF.setStatus("current")
_XcmHrDeviceScannerADF_ObjectIdentity = ObjectIdentity
xcmHrDeviceScannerADF = _XcmHrDeviceScannerADF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 126)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScannerADF.setStatus("current")
_XcmHrDeviceScannerPlaten_ObjectIdentity = ObjectIdentity
xcmHrDeviceScannerPlaten = _XcmHrDeviceScannerPlaten_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 127)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScannerPlaten.setStatus("current")
_XcmHrDeviceColorScanningCard_ObjectIdentity = ObjectIdentity
xcmHrDeviceColorScanningCard = _XcmHrDeviceColorScanningCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 128)
)
if mibBuilder.loadTexts:
    xcmHrDeviceColorScanningCard.setStatus("current")
_XcmHrDeviceHostSystemHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceHostSystemHistory = _XcmHrDeviceHostSystemHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 151)
)
if mibBuilder.loadTexts:
    xcmHrDeviceHostSystemHistory.setStatus("current")
_XcmHrDeviceScannerHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceScannerHistory = _XcmHrDeviceScannerHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 152)
)
if mibBuilder.loadTexts:
    xcmHrDeviceScannerHistory.setStatus("current")
_XcmHrDeviceCopierHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceCopierHistory = _XcmHrDeviceCopierHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 153)
)
if mibBuilder.loadTexts:
    xcmHrDeviceCopierHistory.setStatus("current")
_XcmHrDeviceFaxHistory_ObjectIdentity = ObjectIdentity
xcmHrDeviceFaxHistory = _XcmHrDeviceFaxHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 154)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFaxHistory.setStatus("current")
_XcmHrCruXerographicModule_ObjectIdentity = ObjectIdentity
xcmHrCruXerographicModule = _XcmHrCruXerographicModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 201)
)
if mibBuilder.loadTexts:
    xcmHrCruXerographicModule.setStatus("current")
_XcmHrCruFuserModule_ObjectIdentity = ObjectIdentity
xcmHrCruFuserModule = _XcmHrCruFuserModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 202)
)
if mibBuilder.loadTexts:
    xcmHrCruFuserModule.setStatus("current")
_XcmHrCruTonerBottleModule_ObjectIdentity = ObjectIdentity
xcmHrCruTonerBottleModule = _XcmHrCruTonerBottleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 203)
)
if mibBuilder.loadTexts:
    xcmHrCruTonerBottleModule.setStatus("current")
_XcmHrCruCollectorBottleModule_ObjectIdentity = ObjectIdentity
xcmHrCruCollectorBottleModule = _XcmHrCruCollectorBottleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 204)
)
if mibBuilder.loadTexts:
    xcmHrCruCollectorBottleModule.setStatus("current")
_XcmHrCruTrayFeedHeadModule_ObjectIdentity = ObjectIdentity
xcmHrCruTrayFeedHeadModule = _XcmHrCruTrayFeedHeadModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 205)
)
if mibBuilder.loadTexts:
    xcmHrCruTrayFeedHeadModule.setStatus("current")
_XcmHrCruAdfFeedHeadModule_ObjectIdentity = ObjectIdentity
xcmHrCruAdfFeedHeadModule = _XcmHrCruAdfFeedHeadModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 206)
)
if mibBuilder.loadTexts:
    xcmHrCruAdfFeedHeadModule.setStatus("current")
_XcmHrCruFuserWebModule_ObjectIdentity = ObjectIdentity
xcmHrCruFuserWebModule = _XcmHrCruFuserWebModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 207)
)
if mibBuilder.loadTexts:
    xcmHrCruFuserWebModule.setStatus("current")
_XcmHrCruFilterModule_ObjectIdentity = ObjectIdentity
xcmHrCruFilterModule = _XcmHrCruFilterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 208)
)
if mibBuilder.loadTexts:
    xcmHrCruFilterModule.setStatus("current")
_XcmHrCruCleanerUnitModule_ObjectIdentity = ObjectIdentity
xcmHrCruCleanerUnitModule = _XcmHrCruCleanerUnitModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 209)
)
if mibBuilder.loadTexts:
    xcmHrCruCleanerUnitModule.setStatus("current")
_XcmHrCruTransferUnitModule_ObjectIdentity = ObjectIdentity
xcmHrCruTransferUnitModule = _XcmHrCruTransferUnitModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 210)
)
if mibBuilder.loadTexts:
    xcmHrCruTransferUnitModule.setStatus("current")
_XcmHrCruTransferRollerModule_ObjectIdentity = ObjectIdentity
xcmHrCruTransferRollerModule = _XcmHrCruTransferRollerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 211)
)
if mibBuilder.loadTexts:
    xcmHrCruTransferRollerModule.setStatus("current")
_XcmHrCruPFPFeedRollModule_ObjectIdentity = ObjectIdentity
xcmHrCruPFPFeedRollModule = _XcmHrCruPFPFeedRollModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 212)
)
if mibBuilder.loadTexts:
    xcmHrCruPFPFeedRollModule.setStatus("current")
_XcmHrCruPFPRetardRollModule_ObjectIdentity = ObjectIdentity
xcmHrCruPFPRetardRollModule = _XcmHrCruPFPRetardRollModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 213)
)
if mibBuilder.loadTexts:
    xcmHrCruPFPRetardRollModule.setStatus("current")
_XcmHrDeviceUSBPort_ObjectIdentity = ObjectIdentity
xcmHrDeviceUSBPort = _XcmHrDeviceUSBPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 250)
)
if mibBuilder.loadTexts:
    xcmHrDeviceUSBPort.setStatus("current")
_XcmHrDeviceFlashDIMMFileStore_ObjectIdentity = ObjectIdentity
xcmHrDeviceFlashDIMMFileStore = _XcmHrDeviceFlashDIMMFileStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 260)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDIMMFileStore.setStatus("current")
_XcmHrDeviceFlashDIMMBootLoader_ObjectIdentity = ObjectIdentity
xcmHrDeviceFlashDIMMBootLoader = _XcmHrDeviceFlashDIMMBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 261)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDIMMBootLoader.setStatus("current")
_XcmHrDeviceFlashDrive_ObjectIdentity = ObjectIdentity
xcmHrDeviceFlashDrive = _XcmHrDeviceFlashDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 2, 262)
)
if mibBuilder.loadTexts:
    xcmHrDeviceFlashDrive.setStatus("current")
_XcmHrAdminServiceTypes_ObjectIdentity = ObjectIdentity
xcmHrAdminServiceTypes = _XcmHrAdminServiceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3)
)
if mibBuilder.loadTexts:
    xcmHrAdminServiceTypes.setStatus("current")
_XcmHrAdminObjectService_ObjectIdentity = ObjectIdentity
xcmHrAdminObjectService = _XcmHrAdminObjectService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 1)
)
if mibBuilder.loadTexts:
    xcmHrAdminObjectService.setStatus("current")
_XcmHrAdminServerService_ObjectIdentity = ObjectIdentity
xcmHrAdminServerService = _XcmHrAdminServerService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 2)
)
if mibBuilder.loadTexts:
    xcmHrAdminServerService.setStatus("current")
_XcmHrAdminDeviceService_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceService = _XcmHrAdminDeviceService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 3)
)
if mibBuilder.loadTexts:
    xcmHrAdminDeviceService.setStatus("current")
_XcmHrAdminJobService_ObjectIdentity = ObjectIdentity
xcmHrAdminJobService = _XcmHrAdminJobService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 4)
)
if mibBuilder.loadTexts:
    xcmHrAdminJobService.setStatus("current")
_XcmHrAdminDocService_ObjectIdentity = ObjectIdentity
xcmHrAdminDocService = _XcmHrAdminDocService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 5)
)
if mibBuilder.loadTexts:
    xcmHrAdminDocService.setStatus("current")
_XcmHrAdminSecurityService_ObjectIdentity = ObjectIdentity
xcmHrAdminSecurityService = _XcmHrAdminSecurityService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 6)
)
if mibBuilder.loadTexts:
    xcmHrAdminSecurityService.setStatus("current")
_XcmHrAdminCommsService_ObjectIdentity = ObjectIdentity
xcmHrAdminCommsService = _XcmHrAdminCommsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 3, 7)
)
if mibBuilder.loadTexts:
    xcmHrAdminCommsService.setStatus("current")
_XcmHrAdminDeviceOperationTypes_ObjectIdentity = ObjectIdentity
xcmHrAdminDeviceOperationTypes = _XcmHrAdminDeviceOperationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 4)
)
if mibBuilder.loadTexts:
    xcmHrAdminDeviceOperationTypes.setStatus("current")
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
_XCmHrDevCalendarTimeOfDay_Type = XcmHrDevCalendarTimeOfDay
_XCmHrDevCalendarTimeOfDay_Object = MibScalar
xCmHrDevCalendarTimeOfDay = _XCmHrDevCalendarTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 2),
    _XCmHrDevCalendarTimeOfDay_Type()
)
xCmHrDevCalendarTimeOfDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevCalendarTimeOfDay.setStatus("current")
_XCmHrDevDetailType_Type = XcmHrDevDetailType
_XCmHrDevDetailType_Object = MibScalar
xCmHrDevDetailType = _XCmHrDevDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 3),
    _XCmHrDevDetailType_Type()
)
xCmHrDevDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevDetailType.setStatus("current")
_XCmHrDevDetailUnitClass_Type = XcmHrDevDetailUnitClass
_XCmHrDevDetailUnitClass_Object = MibScalar
xCmHrDevDetailUnitClass = _XCmHrDevDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 4),
    _XCmHrDevDetailUnitClass_Type()
)
xCmHrDevDetailUnitClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevDetailUnitClass.setStatus("current")
_XCmHrDevInfoRealization_Type = XcmHrDevInfoRealization
_XCmHrDevInfoRealization_Object = MibScalar
xCmHrDevInfoRealization = _XCmHrDevInfoRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 5),
    _XCmHrDevInfoRealization_Type()
)
xCmHrDevInfoRealization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoRealization.setStatus("current")
_XCmHrDevInfoStatus_Type = XcmHrDevInfoStatus
_XCmHrDevInfoStatus_Object = MibScalar
xCmHrDevInfoStatus = _XCmHrDevInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 6),
    _XCmHrDevInfoStatus_Type()
)
xCmHrDevInfoStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoStatus.setStatus("current")
_XCmHrDevInfoXStatus_Type = XcmHrDevInfoXStatus
_XCmHrDevInfoXStatus_Object = MibScalar
xCmHrDevInfoXStatus = _XCmHrDevInfoXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 7),
    _XCmHrDevInfoXStatus_Type()
)
xCmHrDevInfoXStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoXStatus.setStatus("current")
_XCmHrDevInfoConditions_Type = XcmHrDevInfoConditions
_XCmHrDevInfoConditions_Object = MibScalar
xCmHrDevInfoConditions = _XCmHrDevInfoConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 8),
    _XCmHrDevInfoConditions_Type()
)
xCmHrDevInfoConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoConditions.setStatus("current")
_XCmHrDevInfoXConditions_Type = XcmHrDevInfoXConditions
_XCmHrDevInfoXConditions_Object = MibScalar
xCmHrDevInfoXConditions = _XCmHrDevInfoXConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 9),
    _XCmHrDevInfoXConditions_Type()
)
xCmHrDevInfoXConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevInfoXConditions.setStatus("current")
_XCmHrDevMgmtCommandRequest_Type = XcmHrDevMgmtCommandRequest
_XCmHrDevMgmtCommandRequest_Object = MibScalar
xCmHrDevMgmtCommandRequest = _XCmHrDevMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 10),
    _XCmHrDevMgmtCommandRequest_Type()
)
xCmHrDevMgmtCommandRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandRequest.setStatus("current")
_XCmHrDevMgmtCommandData_Type = XcmHrDevMgmtCommandData
_XCmHrDevMgmtCommandData_Object = MibScalar
xCmHrDevMgmtCommandData = _XCmHrDevMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 11),
    _XCmHrDevMgmtCommandData_Type()
)
xCmHrDevMgmtCommandData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandData.setStatus("current")
_XCmHrDevMgmtCommandDataTag_Type = XcmHrDevMgmtCommandDataTag
_XCmHrDevMgmtCommandDataTag_Object = MibScalar
xCmHrDevMgmtCommandDataTag = _XCmHrDevMgmtCommandDataTag_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 12),
    _XCmHrDevMgmtCommandDataTag_Type()
)
xCmHrDevMgmtCommandDataTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevMgmtCommandDataTag.setStatus("current")
_XCmHrDevPowerModeType_Type = XcmHrDevPowerModeType
_XCmHrDevPowerModeType_Object = MibScalar
xCmHrDevPowerModeType = _XCmHrDevPowerModeType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 13),
    _XCmHrDevPowerModeType_Type()
)
xCmHrDevPowerModeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevPowerModeType.setStatus("current")
_XCmHrDevPowerTimeUnit_Type = XcmHrDevPowerTimeUnit
_XCmHrDevPowerTimeUnit_Object = MibScalar
xCmHrDevPowerTimeUnit = _XCmHrDevPowerTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 14),
    _XCmHrDevPowerTimeUnit_Type()
)
xCmHrDevPowerTimeUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevPowerTimeUnit.setStatus("current")
_XCmHrDevTrafficUnit_Type = XcmHrDevTrafficUnit
_XCmHrDevTrafficUnit_Object = MibScalar
xCmHrDevTrafficUnit = _XCmHrDevTrafficUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 15),
    _XCmHrDevTrafficUnit_Type()
)
xCmHrDevTrafficUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDevTrafficUnit.setStatus("current")
_XCmHrGroupSupport_Type = XcmHrGroupSupport
_XCmHrGroupSupport_Object = MibScalar
xCmHrGroupSupport = _XCmHrGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 16),
    _XCmHrGroupSupport_Type()
)
xCmHrGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrGroupSupport.setStatus("current")
_XCmHrSWRunXStatus_Type = XcmHrSWRunXStatus
_XCmHrSWRunXStatus_Object = MibScalar
xCmHrSWRunXStatus = _XCmHrSWRunXStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 17),
    _XCmHrSWRunXStatus_Type()
)
xCmHrSWRunXStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrSWRunXStatus.setStatus("current")
_XCmHrStorageDetailType_Type = XcmHrStorageDetailType
_XCmHrStorageDetailType_Object = MibScalar
xCmHrStorageDetailType = _XCmHrStorageDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 18),
    _XCmHrStorageDetailType_Type()
)
xCmHrStorageDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrStorageDetailType.setStatus("current")
_XCmHrStorageRealization_Type = XcmHrStorageRealization
_XCmHrStorageRealization_Object = MibScalar
xCmHrStorageRealization = _XCmHrStorageRealization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 19),
    _XCmHrStorageRealization_Type()
)
xCmHrStorageRealization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrStorageRealization.setStatus("current")
_XCmHrDpaAvailability_Type = XcmHrDpaAvailability
_XCmHrDpaAvailability_Object = MibScalar
xCmHrDpaAvailability = _XCmHrDpaAvailability_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 20),
    _XCmHrDpaAvailability_Type()
)
xCmHrDpaAvailability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaAvailability.setStatus("current")
_XCmHrDpaConditions_Type = XcmHrDpaConditions
_XCmHrDpaConditions_Object = MibScalar
xCmHrDpaConditions = _XCmHrDpaConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 21),
    _XCmHrDpaConditions_Type()
)
xCmHrDpaConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaConditions.setStatus("current")
_XCmHrDpaJobValidateSupport_Type = XcmHrDpaJobValidateSupport
_XCmHrDpaJobValidateSupport_Object = MibScalar
xCmHrDpaJobValidateSupport = _XCmHrDpaJobValidateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 22),
    _XCmHrDpaJobValidateSupport_Type()
)
xCmHrDpaJobValidateSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaJobValidateSupport.setStatus("current")
_XCmHrDpaObjectClassSupport_Type = XcmHrDpaObjectClassSupport
_XCmHrDpaObjectClassSupport_Object = MibScalar
xCmHrDpaObjectClassSupport = _XCmHrDpaObjectClassSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 23),
    _XCmHrDpaObjectClassSupport_Type()
)
xCmHrDpaObjectClassSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaObjectClassSupport.setStatus("current")
_XCmHrDpaState_Type = XcmHrDpaState
_XCmHrDpaState_Object = MibScalar
xCmHrDpaState = _XCmHrDpaState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 24),
    _XCmHrDpaState_Type()
)
xCmHrDpaState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDpaState.setStatus("current")
_XCmHrDetailTableEnumTC_Type = XcmHrDetailTableEnumTC
_XCmHrDetailTableEnumTC_Object = MibScalar
xCmHrDetailTableEnumTC = _XCmHrDetailTableEnumTC_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 25),
    _XCmHrDetailTableEnumTC_Type()
)
xCmHrDetailTableEnumTC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrDetailTableEnumTC.setStatus("current")
_XCmHrSuppliesClassTC_Type = XcmHrSuppliesClassTC
_XCmHrSuppliesClassTC_Object = MibScalar
xCmHrSuppliesClassTC = _XCmHrSuppliesClassTC_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 26),
    _XCmHrSuppliesClassTC_Type()
)
xCmHrSuppliesClassTC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrSuppliesClassTC.setStatus("current")
_XCmHrConsoleDefaultService_Type = XcmHrConsoleDefaultService
_XCmHrConsoleDefaultService_Object = MibScalar
xCmHrConsoleDefaultService = _XCmHrConsoleDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 52, 999, 27),
    _XCmHrConsoleDefaultService_Type()
)
xCmHrConsoleDefaultService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmHrConsoleDefaultService.setStatus("current")

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
