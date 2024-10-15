# SNMP MIB module (SAMSUNG-HOST-RESOURCES-EXT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-HOST-RESOURCES-EXT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:40 2024
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

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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

scmHrTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScmHrDevCalendarDayOfWeek(Integer32, TextualConvention):
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



class ScmHrDevCalendarTimeOfDay(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12359),
    )



class ScmHrDevDetailType(Integer32, TextualConvention):
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
              232)
        )
    )
    namedValues = NamedValues(
        *(("deviceAccountingUsage", 30),
          ("deviceAlias", 4),
          ("deviceAlienJobPolicy", 201),
          ("deviceCancelDocSupport", 76),
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
          ("deviceJobHistoryDeviceIndex", 99),
          ("deviceJobHoldDeleteTimeout", 193),
          ("deviceJobIncompleteTimeout", 191),
          ("deviceJobLogFullPolicy", 203),
          ("deviceJobPauseResumeTimeout", 194),
          ("deviceJobProgrammingTimeout", 192),
          ("deviceJobServiceDeviceIndex", 98),
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
          ("deviceTranslatorReady", 72),
          ("deviceTranslatorSupport", 71),
          ("deviceTree", 8),
          ("deviceTriggerDaysForMaximum", 44),
          ("deviceTriggerDaysForReorder", 41),
          ("deviceTriggerDaysForReplace", 43),
          ("deviceTriggerDaysForWarning", 42),
          ("deviceType", 5),
          ("deviceUniversalProductCode", 210),
          ("deviceVendor", 13),
          ("deviceVersion", 14),
          ("deviceWarningLifetimeLimit", 22),
          ("deviceWarningMsgSentDate", 52),
          ("deviceWarningOnDate", 32),
          ("deviceXFeedResolutionSupport", 87),
          ("other", 1),
          ("unknown", 2))
    )



class ScmHrDevDetailUnitClass(Integer32, TextualConvention):
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



class ScmHrDevInfoRealization(Integer32, TextualConvention):
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



class ScmHrDevInfoStatus(Integer32, TextualConvention):
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



class ScmHrDevInfoXStatus(Integer32, TextualConvention):
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
        *(("audioNone", 1100),
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
          ("faxNone", 10400),
          ("finisher3rdPartyNone", 11500),
          ("finisherBFMNone", 11200),
          ("finisherMFFNone", 11300),
          ("finisherXIMNone", 11400),
          ("hostSystemNone", 10100),
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
          ("serialPortNone", 1700),
          ("tapeNone", 1800),
          ("unknownNone", 200),
          ("videoNone", 1000),
          ("volatileMemoryNone", 2000))
    )



class ScmHrDevInfoConditions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmHrDevInfoXConditions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmHrDevMgmtCommandRequest(Integer32, TextualConvention):
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



class ScmHrDevMgmtCommandData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ScmHrDevMgmtCommandDataTag(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class ScmHrDevPowerModeType(Integer32, TextualConvention):
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



class ScmHrDevPowerTimeUnit(Integer32, TextualConvention):
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



class ScmHrDevTrafficUnit(Integer32, TextualConvention):
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
              67)
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



class ScmHrGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmHrSWRunXStatus(Integer32, TextualConvention):
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



class ScmHrStorageDetailType(Integer32, TextualConvention):
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



class ScmHrStorageRealization(Integer32, TextualConvention):
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



class ScmHrDpaAvailability(Integer32, TextualConvention):
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



class ScmHrDpaConditions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmHrDpaJobValidateSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmHrDpaObjectClassSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmHrDpaState(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_ScmHrDeviceTypes_ObjectIdentity = ObjectIdentity
scmHrDeviceTypes = _ScmHrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2)
)
if mibBuilder.loadTexts:
    scmHrDeviceTypes.setStatus("current")
_ScmHrDevicePrinterHistory_ObjectIdentity = ObjectIdentity
scmHrDevicePrinterHistory = _ScmHrDevicePrinterHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 55)
)
if mibBuilder.loadTexts:
    scmHrDevicePrinterHistory.setStatus("current")
_ScmHrDeviceHostSystem_ObjectIdentity = ObjectIdentity
scmHrDeviceHostSystem = _ScmHrDeviceHostSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 101)
)
if mibBuilder.loadTexts:
    scmHrDeviceHostSystem.setStatus("current")
_ScmHrDeviceScanner_ObjectIdentity = ObjectIdentity
scmHrDeviceScanner = _ScmHrDeviceScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 102)
)
if mibBuilder.loadTexts:
    scmHrDeviceScanner.setStatus("current")
_ScmHrDeviceCopier_ObjectIdentity = ObjectIdentity
scmHrDeviceCopier = _ScmHrDeviceCopier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 103)
)
if mibBuilder.loadTexts:
    scmHrDeviceCopier.setStatus("current")
_ScmHrDeviceFax_ObjectIdentity = ObjectIdentity
scmHrDeviceFax = _ScmHrDeviceFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 104)
)
if mibBuilder.loadTexts:
    scmHrDeviceFax.setStatus("current")
_ScmHrDeviceMailbox_ObjectIdentity = ObjectIdentity
scmHrDeviceMailbox = _ScmHrDeviceMailbox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 105)
)
if mibBuilder.loadTexts:
    scmHrDeviceMailbox.setStatus("current")
_ScmHrDeviceFinisher_ObjectIdentity = ObjectIdentity
scmHrDeviceFinisher = _ScmHrDeviceFinisher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 106)
)
if mibBuilder.loadTexts:
    scmHrDeviceFinisher.setStatus("current")
_ScmHrDeviceFeeder_ObjectIdentity = ObjectIdentity
scmHrDeviceFeeder = _ScmHrDeviceFeeder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 107)
)
if mibBuilder.loadTexts:
    scmHrDeviceFeeder.setStatus("current")
_ScmHrDeviceSorter_ObjectIdentity = ObjectIdentity
scmHrDeviceSorter = _ScmHrDeviceSorter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 108)
)
if mibBuilder.loadTexts:
    scmHrDeviceSorter.setStatus("current")
_ScmHrDeviceMailboxSorter_ObjectIdentity = ObjectIdentity
scmHrDeviceMailboxSorter = _ScmHrDeviceMailboxSorter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 109)
)
if mibBuilder.loadTexts:
    scmHrDeviceMailboxSorter.setStatus("current")
_ScmHrDevicePrintAppliance_ObjectIdentity = ObjectIdentity
scmHrDevicePrintAppliance = _ScmHrDevicePrintAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 110)
)
if mibBuilder.loadTexts:
    scmHrDevicePrintAppliance.setStatus("current")
_ScmHrDeviceMarker_ObjectIdentity = ObjectIdentity
scmHrDeviceMarker = _ScmHrDeviceMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 111)
)
if mibBuilder.loadTexts:
    scmHrDeviceMarker.setStatus("current")
_ScmHrDeviceFinisherBFM_ObjectIdentity = ObjectIdentity
scmHrDeviceFinisherBFM = _ScmHrDeviceFinisherBFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 112)
)
if mibBuilder.loadTexts:
    scmHrDeviceFinisherBFM.setStatus("current")
_ScmHrDeviceFinisherMFF_ObjectIdentity = ObjectIdentity
scmHrDeviceFinisherMFF = _ScmHrDeviceFinisherMFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 113)
)
if mibBuilder.loadTexts:
    scmHrDeviceFinisherMFF.setStatus("current")
_ScmHrDeviceFinisherXIM_ObjectIdentity = ObjectIdentity
scmHrDeviceFinisherXIM = _ScmHrDeviceFinisherXIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 114)
)
if mibBuilder.loadTexts:
    scmHrDeviceFinisherXIM.setStatus("current")
_ScmHrDeviceFinisher3rdParty_ObjectIdentity = ObjectIdentity
scmHrDeviceFinisher3rdParty = _ScmHrDeviceFinisher3rdParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 115)
)
if mibBuilder.loadTexts:
    scmHrDeviceFinisher3rdParty.setStatus("current")
_ScmHrDevicePaymentInterface_ObjectIdentity = ObjectIdentity
scmHrDevicePaymentInterface = _ScmHrDevicePaymentInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 116)
)
if mibBuilder.loadTexts:
    scmHrDevicePaymentInterface.setStatus("current")
_ScmHrDeviceInterposer_ObjectIdentity = ObjectIdentity
scmHrDeviceInterposer = _ScmHrDeviceInterposer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 117)
)
if mibBuilder.loadTexts:
    scmHrDeviceInterposer.setStatus("current")
_ScmHrDeviceHostSystemHistory_ObjectIdentity = ObjectIdentity
scmHrDeviceHostSystemHistory = _ScmHrDeviceHostSystemHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 151)
)
if mibBuilder.loadTexts:
    scmHrDeviceHostSystemHistory.setStatus("current")
_ScmHrDeviceScannerHistory_ObjectIdentity = ObjectIdentity
scmHrDeviceScannerHistory = _ScmHrDeviceScannerHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 152)
)
if mibBuilder.loadTexts:
    scmHrDeviceScannerHistory.setStatus("current")
_ScmHrDeviceCopierHistory_ObjectIdentity = ObjectIdentity
scmHrDeviceCopierHistory = _ScmHrDeviceCopierHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 153)
)
if mibBuilder.loadTexts:
    scmHrDeviceCopierHistory.setStatus("current")
_ScmHrDeviceFaxHistory_ObjectIdentity = ObjectIdentity
scmHrDeviceFaxHistory = _ScmHrDeviceFaxHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 154)
)
if mibBuilder.loadTexts:
    scmHrDeviceFaxHistory.setStatus("current")
_ScmHrCruXerographicModule_ObjectIdentity = ObjectIdentity
scmHrCruXerographicModule = _ScmHrCruXerographicModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 201)
)
if mibBuilder.loadTexts:
    scmHrCruXerographicModule.setStatus("current")
_ScmHrCruFuserModule_ObjectIdentity = ObjectIdentity
scmHrCruFuserModule = _ScmHrCruFuserModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 202)
)
if mibBuilder.loadTexts:
    scmHrCruFuserModule.setStatus("current")
_ScmHrCruTonerBottleModule_ObjectIdentity = ObjectIdentity
scmHrCruTonerBottleModule = _ScmHrCruTonerBottleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 203)
)
if mibBuilder.loadTexts:
    scmHrCruTonerBottleModule.setStatus("current")
_ScmHrCruCollectorBottleModule_ObjectIdentity = ObjectIdentity
scmHrCruCollectorBottleModule = _ScmHrCruCollectorBottleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 204)
)
if mibBuilder.loadTexts:
    scmHrCruCollectorBottleModule.setStatus("current")
_ScmHrCruTrayFeedHeadModule_ObjectIdentity = ObjectIdentity
scmHrCruTrayFeedHeadModule = _ScmHrCruTrayFeedHeadModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 205)
)
if mibBuilder.loadTexts:
    scmHrCruTrayFeedHeadModule.setStatus("current")
_ScmHrCruAdfFeedHeadModule_ObjectIdentity = ObjectIdentity
scmHrCruAdfFeedHeadModule = _ScmHrCruAdfFeedHeadModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 206)
)
if mibBuilder.loadTexts:
    scmHrCruAdfFeedHeadModule.setStatus("current")
_ScmHrCruFuserWebModule_ObjectIdentity = ObjectIdentity
scmHrCruFuserWebModule = _ScmHrCruFuserWebModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 207)
)
if mibBuilder.loadTexts:
    scmHrCruFuserWebModule.setStatus("current")
_ScmHrCruFilterModule_ObjectIdentity = ObjectIdentity
scmHrCruFilterModule = _ScmHrCruFilterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 208)
)
if mibBuilder.loadTexts:
    scmHrCruFilterModule.setStatus("current")
_ScmHrCruCleanerUnitModule_ObjectIdentity = ObjectIdentity
scmHrCruCleanerUnitModule = _ScmHrCruCleanerUnitModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 209)
)
if mibBuilder.loadTexts:
    scmHrCruCleanerUnitModule.setStatus("current")
_ScmHrCruTransferUnitModule_ObjectIdentity = ObjectIdentity
scmHrCruTransferUnitModule = _ScmHrCruTransferUnitModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 210)
)
if mibBuilder.loadTexts:
    scmHrCruTransferUnitModule.setStatus("current")
_ScmHrCruTransferRollerModule_ObjectIdentity = ObjectIdentity
scmHrCruTransferRollerModule = _ScmHrCruTransferRollerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 211)
)
if mibBuilder.loadTexts:
    scmHrCruTransferRollerModule.setStatus("current")
_ScmHrCruPFPFeedRollModule_ObjectIdentity = ObjectIdentity
scmHrCruPFPFeedRollModule = _ScmHrCruPFPFeedRollModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 212)
)
if mibBuilder.loadTexts:
    scmHrCruPFPFeedRollModule.setStatus("current")
_ScmHrCruPFPRetardRollModule_ObjectIdentity = ObjectIdentity
scmHrCruPFPRetardRollModule = _ScmHrCruPFPRetardRollModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 213)
)
if mibBuilder.loadTexts:
    scmHrCruPFPRetardRollModule.setStatus("current")
_ScmHrDeviceUSBPort_ObjectIdentity = ObjectIdentity
scmHrDeviceUSBPort = _ScmHrDeviceUSBPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 250)
)
if mibBuilder.loadTexts:
    scmHrDeviceUSBPort.setStatus("current")
_ScmHrDeviceFlashDIMMFileStore_ObjectIdentity = ObjectIdentity
scmHrDeviceFlashDIMMFileStore = _ScmHrDeviceFlashDIMMFileStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 260)
)
if mibBuilder.loadTexts:
    scmHrDeviceFlashDIMMFileStore.setStatus("current")
_ScmHrDeviceFlashDIMMBootLoader_ObjectIdentity = ObjectIdentity
scmHrDeviceFlashDIMMBootLoader = _ScmHrDeviceFlashDIMMBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 2, 261)
)
if mibBuilder.loadTexts:
    scmHrDeviceFlashDIMMBootLoader.setStatus("current")
_ScmHrAdminServiceTypes_ObjectIdentity = ObjectIdentity
scmHrAdminServiceTypes = _ScmHrAdminServiceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3)
)
if mibBuilder.loadTexts:
    scmHrAdminServiceTypes.setStatus("current")
_ScmHrAdminObjectService_ObjectIdentity = ObjectIdentity
scmHrAdminObjectService = _ScmHrAdminObjectService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 1)
)
if mibBuilder.loadTexts:
    scmHrAdminObjectService.setStatus("current")
_ScmHrAdminServerService_ObjectIdentity = ObjectIdentity
scmHrAdminServerService = _ScmHrAdminServerService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 2)
)
if mibBuilder.loadTexts:
    scmHrAdminServerService.setStatus("current")
_ScmHrAdminDeviceService_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceService = _ScmHrAdminDeviceService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 3)
)
if mibBuilder.loadTexts:
    scmHrAdminDeviceService.setStatus("current")
_ScmHrAdminJobService_ObjectIdentity = ObjectIdentity
scmHrAdminJobService = _ScmHrAdminJobService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 4)
)
if mibBuilder.loadTexts:
    scmHrAdminJobService.setStatus("current")
_ScmHrAdminDocService_ObjectIdentity = ObjectIdentity
scmHrAdminDocService = _ScmHrAdminDocService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 5)
)
if mibBuilder.loadTexts:
    scmHrAdminDocService.setStatus("current")
_ScmHrAdminSecurityService_ObjectIdentity = ObjectIdentity
scmHrAdminSecurityService = _ScmHrAdminSecurityService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 6)
)
if mibBuilder.loadTexts:
    scmHrAdminSecurityService.setStatus("current")
_ScmHrAdminCommsService_ObjectIdentity = ObjectIdentity
scmHrAdminCommsService = _ScmHrAdminCommsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 3, 7)
)
if mibBuilder.loadTexts:
    scmHrAdminCommsService.setStatus("current")
_ScmHrAdminDeviceOperationTypes_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceOperationTypes = _ScmHrAdminDeviceOperationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4)
)
if mibBuilder.loadTexts:
    scmHrAdminDeviceOperationTypes.setStatus("current")
_ScmHrAdminDeviceNone_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceNone = _ScmHrAdminDeviceNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 1)
)
_ScmHrAdminDeviceStartup_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceStartup = _ScmHrAdminDeviceStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 2)
)
_ScmHrAdminDeviceResetWarning_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceResetWarning = _ScmHrAdminDeviceResetWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 3)
)
_ScmHrAdminDeviceTest_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceTest = _ScmHrAdminDeviceTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 4)
)
_ScmHrAdminDeviceShutdown_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceShutdown = _ScmHrAdminDeviceShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 5)
)
_ScmHrAdminDeviceQuiesce_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceQuiesce = _ScmHrAdminDeviceQuiesce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 6)
)
_ScmHrAdminDeviceResetCounters_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceResetCounters = _ScmHrAdminDeviceResetCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 7)
)
_ScmHrAdminDeviceResetWarm_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceResetWarm = _ScmHrAdminDeviceResetWarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 8)
)
_ScmHrAdminDeviceResetCold_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceResetCold = _ScmHrAdminDeviceResetCold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 9)
)
_ScmHrAdminDeviceResetFactory_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceResetFactory = _ScmHrAdminDeviceResetFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 10)
)
_ScmHrAdminDeviceFlushInput_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceFlushInput = _ScmHrAdminDeviceFlushInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 11)
)
_ScmHrAdminDeviceFlushOutput_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceFlushOutput = _ScmHrAdminDeviceFlushOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 12)
)
_ScmHrAdminDeviceFlushInOut_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceFlushInOut = _ScmHrAdminDeviceFlushInOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 13)
)
_ScmHrAdminDeviceManage_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceManage = _ScmHrAdminDeviceManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 14)
)
_ScmHrAdminDeviceRefresh_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceRefresh = _ScmHrAdminDeviceRefresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 15)
)
_ScmHrAdminDeviceWarmUp_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceWarmUp = _ScmHrAdminDeviceWarmUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 16)
)
_ScmHrAdminDeviceCoolDown_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceCoolDown = _ScmHrAdminDeviceCoolDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 17)
)
_ScmHrAdminDeviceEnergySave_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceEnergySave = _ScmHrAdminDeviceEnergySave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 18)
)
_ScmHrAdminDeviceWakeUp_ObjectIdentity = ObjectIdentity
scmHrAdminDeviceWakeUp = _ScmHrAdminDeviceWakeUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 19)
)
_ScmHrAdminDevicePowerToReady_ObjectIdentity = ObjectIdentity
scmHrAdminDevicePowerToReady = _ScmHrAdminDevicePowerToReady_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 20)
)
_ScmHrAdminDevicePowerToStandby_ObjectIdentity = ObjectIdentity
scmHrAdminDevicePowerToStandby = _ScmHrAdminDevicePowerToStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 21)
)
_ScmHrAdminDevicePowerToSleep_ObjectIdentity = ObjectIdentity
scmHrAdminDevicePowerToSleep = _ScmHrAdminDevicePowerToSleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 4, 22)
)
_SCmHrDummy_ObjectIdentity = ObjectIdentity
sCmHrDummy = _SCmHrDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999)
)
_SCmHrDevCalendarDayOfWeek_Type = ScmHrDevCalendarDayOfWeek
_SCmHrDevCalendarDayOfWeek_Object = MibScalar
sCmHrDevCalendarDayOfWeek = _SCmHrDevCalendarDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 1),
    _SCmHrDevCalendarDayOfWeek_Type()
)
sCmHrDevCalendarDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevCalendarDayOfWeek.setStatus("current")
_SCmHrDevCalendarTimeOfDay_Type = ScmHrDevCalendarTimeOfDay
_SCmHrDevCalendarTimeOfDay_Object = MibScalar
sCmHrDevCalendarTimeOfDay = _SCmHrDevCalendarTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 2),
    _SCmHrDevCalendarTimeOfDay_Type()
)
sCmHrDevCalendarTimeOfDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevCalendarTimeOfDay.setStatus("current")
_SCmHrDevDetailType_Type = ScmHrDevDetailType
_SCmHrDevDetailType_Object = MibScalar
sCmHrDevDetailType = _SCmHrDevDetailType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 3),
    _SCmHrDevDetailType_Type()
)
sCmHrDevDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevDetailType.setStatus("current")
_SCmHrDevDetailUnitClass_Type = ScmHrDevDetailUnitClass
_SCmHrDevDetailUnitClass_Object = MibScalar
sCmHrDevDetailUnitClass = _SCmHrDevDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 4),
    _SCmHrDevDetailUnitClass_Type()
)
sCmHrDevDetailUnitClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevDetailUnitClass.setStatus("current")
_SCmHrDevInfoRealization_Type = ScmHrDevInfoRealization
_SCmHrDevInfoRealization_Object = MibScalar
sCmHrDevInfoRealization = _SCmHrDevInfoRealization_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 5),
    _SCmHrDevInfoRealization_Type()
)
sCmHrDevInfoRealization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevInfoRealization.setStatus("current")
_SCmHrDevInfoStatus_Type = ScmHrDevInfoStatus
_SCmHrDevInfoStatus_Object = MibScalar
sCmHrDevInfoStatus = _SCmHrDevInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 6),
    _SCmHrDevInfoStatus_Type()
)
sCmHrDevInfoStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevInfoStatus.setStatus("current")
_SCmHrDevInfoXStatus_Type = ScmHrDevInfoXStatus
_SCmHrDevInfoXStatus_Object = MibScalar
sCmHrDevInfoXStatus = _SCmHrDevInfoXStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 7),
    _SCmHrDevInfoXStatus_Type()
)
sCmHrDevInfoXStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevInfoXStatus.setStatus("current")
_SCmHrDevInfoConditions_Type = ScmHrDevInfoConditions
_SCmHrDevInfoConditions_Object = MibScalar
sCmHrDevInfoConditions = _SCmHrDevInfoConditions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 8),
    _SCmHrDevInfoConditions_Type()
)
sCmHrDevInfoConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevInfoConditions.setStatus("current")
_SCmHrDevInfoXConditions_Type = ScmHrDevInfoXConditions
_SCmHrDevInfoXConditions_Object = MibScalar
sCmHrDevInfoXConditions = _SCmHrDevInfoXConditions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 9),
    _SCmHrDevInfoXConditions_Type()
)
sCmHrDevInfoXConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevInfoXConditions.setStatus("current")
_SCmHrDevMgmtCommandRequest_Type = ScmHrDevMgmtCommandRequest
_SCmHrDevMgmtCommandRequest_Object = MibScalar
sCmHrDevMgmtCommandRequest = _SCmHrDevMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 10),
    _SCmHrDevMgmtCommandRequest_Type()
)
sCmHrDevMgmtCommandRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevMgmtCommandRequest.setStatus("current")
_SCmHrDevMgmtCommandData_Type = ScmHrDevMgmtCommandData
_SCmHrDevMgmtCommandData_Object = MibScalar
sCmHrDevMgmtCommandData = _SCmHrDevMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 11),
    _SCmHrDevMgmtCommandData_Type()
)
sCmHrDevMgmtCommandData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevMgmtCommandData.setStatus("current")
_SCmHrDevMgmtCommandDataTag_Type = ScmHrDevMgmtCommandDataTag
_SCmHrDevMgmtCommandDataTag_Object = MibScalar
sCmHrDevMgmtCommandDataTag = _SCmHrDevMgmtCommandDataTag_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 12),
    _SCmHrDevMgmtCommandDataTag_Type()
)
sCmHrDevMgmtCommandDataTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevMgmtCommandDataTag.setStatus("current")
_SCmHrDevPowerModeType_Type = ScmHrDevPowerModeType
_SCmHrDevPowerModeType_Object = MibScalar
sCmHrDevPowerModeType = _SCmHrDevPowerModeType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 13),
    _SCmHrDevPowerModeType_Type()
)
sCmHrDevPowerModeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevPowerModeType.setStatus("current")
_SCmHrDevPowerTimeUnit_Type = ScmHrDevPowerTimeUnit
_SCmHrDevPowerTimeUnit_Object = MibScalar
sCmHrDevPowerTimeUnit = _SCmHrDevPowerTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 14),
    _SCmHrDevPowerTimeUnit_Type()
)
sCmHrDevPowerTimeUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevPowerTimeUnit.setStatus("current")
_SCmHrDevTrafficUnit_Type = ScmHrDevTrafficUnit
_SCmHrDevTrafficUnit_Object = MibScalar
sCmHrDevTrafficUnit = _SCmHrDevTrafficUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 15),
    _SCmHrDevTrafficUnit_Type()
)
sCmHrDevTrafficUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDevTrafficUnit.setStatus("current")
_SCmHrGroupSupport_Type = ScmHrGroupSupport
_SCmHrGroupSupport_Object = MibScalar
sCmHrGroupSupport = _SCmHrGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 16),
    _SCmHrGroupSupport_Type()
)
sCmHrGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrGroupSupport.setStatus("current")
_SCmHrSWRunXStatus_Type = ScmHrSWRunXStatus
_SCmHrSWRunXStatus_Object = MibScalar
sCmHrSWRunXStatus = _SCmHrSWRunXStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 17),
    _SCmHrSWRunXStatus_Type()
)
sCmHrSWRunXStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrSWRunXStatus.setStatus("current")
_SCmHrStorageDetailType_Type = ScmHrStorageDetailType
_SCmHrStorageDetailType_Object = MibScalar
sCmHrStorageDetailType = _SCmHrStorageDetailType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 18),
    _SCmHrStorageDetailType_Type()
)
sCmHrStorageDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrStorageDetailType.setStatus("current")
_SCmHrStorageRealization_Type = ScmHrStorageRealization
_SCmHrStorageRealization_Object = MibScalar
sCmHrStorageRealization = _SCmHrStorageRealization_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 19),
    _SCmHrStorageRealization_Type()
)
sCmHrStorageRealization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrStorageRealization.setStatus("current")
_SCmHrDpaAvailability_Type = ScmHrDpaAvailability
_SCmHrDpaAvailability_Object = MibScalar
sCmHrDpaAvailability = _SCmHrDpaAvailability_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 20),
    _SCmHrDpaAvailability_Type()
)
sCmHrDpaAvailability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDpaAvailability.setStatus("current")
_SCmHrDpaConditions_Type = ScmHrDpaConditions
_SCmHrDpaConditions_Object = MibScalar
sCmHrDpaConditions = _SCmHrDpaConditions_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 21),
    _SCmHrDpaConditions_Type()
)
sCmHrDpaConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDpaConditions.setStatus("current")
_SCmHrDpaJobValidateSupport_Type = ScmHrDpaJobValidateSupport
_SCmHrDpaJobValidateSupport_Object = MibScalar
sCmHrDpaJobValidateSupport = _SCmHrDpaJobValidateSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 22),
    _SCmHrDpaJobValidateSupport_Type()
)
sCmHrDpaJobValidateSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDpaJobValidateSupport.setStatus("current")
_SCmHrDpaObjectClassSupport_Type = ScmHrDpaObjectClassSupport
_SCmHrDpaObjectClassSupport_Object = MibScalar
sCmHrDpaObjectClassSupport = _SCmHrDpaObjectClassSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 23),
    _SCmHrDpaObjectClassSupport_Type()
)
sCmHrDpaObjectClassSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDpaObjectClassSupport.setStatus("current")
_SCmHrDpaState_Type = ScmHrDpaState
_SCmHrDpaState_Object = MibScalar
sCmHrDpaState = _SCmHrDpaState_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 52, 999, 24),
    _SCmHrDpaState_Type()
)
sCmHrDpaState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmHrDpaState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-HOST-RESOURCES-EXT-TC",
    **{"ScmHrDevCalendarDayOfWeek": ScmHrDevCalendarDayOfWeek,
       "ScmHrDevCalendarTimeOfDay": ScmHrDevCalendarTimeOfDay,
       "ScmHrDevDetailType": ScmHrDevDetailType,
       "ScmHrDevDetailUnitClass": ScmHrDevDetailUnitClass,
       "ScmHrDevInfoRealization": ScmHrDevInfoRealization,
       "ScmHrDevInfoStatus": ScmHrDevInfoStatus,
       "ScmHrDevInfoXStatus": ScmHrDevInfoXStatus,
       "ScmHrDevInfoConditions": ScmHrDevInfoConditions,
       "ScmHrDevInfoXConditions": ScmHrDevInfoXConditions,
       "ScmHrDevMgmtCommandRequest": ScmHrDevMgmtCommandRequest,
       "ScmHrDevMgmtCommandData": ScmHrDevMgmtCommandData,
       "ScmHrDevMgmtCommandDataTag": ScmHrDevMgmtCommandDataTag,
       "ScmHrDevPowerModeType": ScmHrDevPowerModeType,
       "ScmHrDevPowerTimeUnit": ScmHrDevPowerTimeUnit,
       "ScmHrDevTrafficUnit": ScmHrDevTrafficUnit,
       "ScmHrGroupSupport": ScmHrGroupSupport,
       "ScmHrSWRunXStatus": ScmHrSWRunXStatus,
       "ScmHrStorageDetailType": ScmHrStorageDetailType,
       "ScmHrStorageRealization": ScmHrStorageRealization,
       "ScmHrDpaAvailability": ScmHrDpaAvailability,
       "ScmHrDpaConditions": ScmHrDpaConditions,
       "ScmHrDpaJobValidateSupport": ScmHrDpaJobValidateSupport,
       "ScmHrDpaObjectClassSupport": ScmHrDpaObjectClassSupport,
       "ScmHrDpaState": ScmHrDpaState,
       "scmHrTC": scmHrTC,
       "scmHrDeviceTypes": scmHrDeviceTypes,
       "scmHrDevicePrinterHistory": scmHrDevicePrinterHistory,
       "scmHrDeviceHostSystem": scmHrDeviceHostSystem,
       "scmHrDeviceScanner": scmHrDeviceScanner,
       "scmHrDeviceCopier": scmHrDeviceCopier,
       "scmHrDeviceFax": scmHrDeviceFax,
       "scmHrDeviceMailbox": scmHrDeviceMailbox,
       "scmHrDeviceFinisher": scmHrDeviceFinisher,
       "scmHrDeviceFeeder": scmHrDeviceFeeder,
       "scmHrDeviceSorter": scmHrDeviceSorter,
       "scmHrDeviceMailboxSorter": scmHrDeviceMailboxSorter,
       "scmHrDevicePrintAppliance": scmHrDevicePrintAppliance,
       "scmHrDeviceMarker": scmHrDeviceMarker,
       "scmHrDeviceFinisherBFM": scmHrDeviceFinisherBFM,
       "scmHrDeviceFinisherMFF": scmHrDeviceFinisherMFF,
       "scmHrDeviceFinisherXIM": scmHrDeviceFinisherXIM,
       "scmHrDeviceFinisher3rdParty": scmHrDeviceFinisher3rdParty,
       "scmHrDevicePaymentInterface": scmHrDevicePaymentInterface,
       "scmHrDeviceInterposer": scmHrDeviceInterposer,
       "scmHrDeviceHostSystemHistory": scmHrDeviceHostSystemHistory,
       "scmHrDeviceScannerHistory": scmHrDeviceScannerHistory,
       "scmHrDeviceCopierHistory": scmHrDeviceCopierHistory,
       "scmHrDeviceFaxHistory": scmHrDeviceFaxHistory,
       "scmHrCruXerographicModule": scmHrCruXerographicModule,
       "scmHrCruFuserModule": scmHrCruFuserModule,
       "scmHrCruTonerBottleModule": scmHrCruTonerBottleModule,
       "scmHrCruCollectorBottleModule": scmHrCruCollectorBottleModule,
       "scmHrCruTrayFeedHeadModule": scmHrCruTrayFeedHeadModule,
       "scmHrCruAdfFeedHeadModule": scmHrCruAdfFeedHeadModule,
       "scmHrCruFuserWebModule": scmHrCruFuserWebModule,
       "scmHrCruFilterModule": scmHrCruFilterModule,
       "scmHrCruCleanerUnitModule": scmHrCruCleanerUnitModule,
       "scmHrCruTransferUnitModule": scmHrCruTransferUnitModule,
       "scmHrCruTransferRollerModule": scmHrCruTransferRollerModule,
       "scmHrCruPFPFeedRollModule": scmHrCruPFPFeedRollModule,
       "scmHrCruPFPRetardRollModule": scmHrCruPFPRetardRollModule,
       "scmHrDeviceUSBPort": scmHrDeviceUSBPort,
       "scmHrDeviceFlashDIMMFileStore": scmHrDeviceFlashDIMMFileStore,
       "scmHrDeviceFlashDIMMBootLoader": scmHrDeviceFlashDIMMBootLoader,
       "scmHrAdminServiceTypes": scmHrAdminServiceTypes,
       "scmHrAdminObjectService": scmHrAdminObjectService,
       "scmHrAdminServerService": scmHrAdminServerService,
       "scmHrAdminDeviceService": scmHrAdminDeviceService,
       "scmHrAdminJobService": scmHrAdminJobService,
       "scmHrAdminDocService": scmHrAdminDocService,
       "scmHrAdminSecurityService": scmHrAdminSecurityService,
       "scmHrAdminCommsService": scmHrAdminCommsService,
       "scmHrAdminDeviceOperationTypes": scmHrAdminDeviceOperationTypes,
       "scmHrAdminDeviceNone": scmHrAdminDeviceNone,
       "scmHrAdminDeviceStartup": scmHrAdminDeviceStartup,
       "scmHrAdminDeviceResetWarning": scmHrAdminDeviceResetWarning,
       "scmHrAdminDeviceTest": scmHrAdminDeviceTest,
       "scmHrAdminDeviceShutdown": scmHrAdminDeviceShutdown,
       "scmHrAdminDeviceQuiesce": scmHrAdminDeviceQuiesce,
       "scmHrAdminDeviceResetCounters": scmHrAdminDeviceResetCounters,
       "scmHrAdminDeviceResetWarm": scmHrAdminDeviceResetWarm,
       "scmHrAdminDeviceResetCold": scmHrAdminDeviceResetCold,
       "scmHrAdminDeviceResetFactory": scmHrAdminDeviceResetFactory,
       "scmHrAdminDeviceFlushInput": scmHrAdminDeviceFlushInput,
       "scmHrAdminDeviceFlushOutput": scmHrAdminDeviceFlushOutput,
       "scmHrAdminDeviceFlushInOut": scmHrAdminDeviceFlushInOut,
       "scmHrAdminDeviceManage": scmHrAdminDeviceManage,
       "scmHrAdminDeviceRefresh": scmHrAdminDeviceRefresh,
       "scmHrAdminDeviceWarmUp": scmHrAdminDeviceWarmUp,
       "scmHrAdminDeviceCoolDown": scmHrAdminDeviceCoolDown,
       "scmHrAdminDeviceEnergySave": scmHrAdminDeviceEnergySave,
       "scmHrAdminDeviceWakeUp": scmHrAdminDeviceWakeUp,
       "scmHrAdminDevicePowerToReady": scmHrAdminDevicePowerToReady,
       "scmHrAdminDevicePowerToStandby": scmHrAdminDevicePowerToStandby,
       "scmHrAdminDevicePowerToSleep": scmHrAdminDevicePowerToSleep,
       "sCmHrDummy": sCmHrDummy,
       "sCmHrDevCalendarDayOfWeek": sCmHrDevCalendarDayOfWeek,
       "sCmHrDevCalendarTimeOfDay": sCmHrDevCalendarTimeOfDay,
       "sCmHrDevDetailType": sCmHrDevDetailType,
       "sCmHrDevDetailUnitClass": sCmHrDevDetailUnitClass,
       "sCmHrDevInfoRealization": sCmHrDevInfoRealization,
       "sCmHrDevInfoStatus": sCmHrDevInfoStatus,
       "sCmHrDevInfoXStatus": sCmHrDevInfoXStatus,
       "sCmHrDevInfoConditions": sCmHrDevInfoConditions,
       "sCmHrDevInfoXConditions": sCmHrDevInfoXConditions,
       "sCmHrDevMgmtCommandRequest": sCmHrDevMgmtCommandRequest,
       "sCmHrDevMgmtCommandData": sCmHrDevMgmtCommandData,
       "sCmHrDevMgmtCommandDataTag": sCmHrDevMgmtCommandDataTag,
       "sCmHrDevPowerModeType": sCmHrDevPowerModeType,
       "sCmHrDevPowerTimeUnit": sCmHrDevPowerTimeUnit,
       "sCmHrDevTrafficUnit": sCmHrDevTrafficUnit,
       "sCmHrGroupSupport": sCmHrGroupSupport,
       "sCmHrSWRunXStatus": sCmHrSWRunXStatus,
       "sCmHrStorageDetailType": sCmHrStorageDetailType,
       "sCmHrStorageRealization": sCmHrStorageRealization,
       "sCmHrDpaAvailability": sCmHrDpaAvailability,
       "sCmHrDpaConditions": sCmHrDpaConditions,
       "sCmHrDpaJobValidateSupport": sCmHrDpaJobValidateSupport,
       "sCmHrDpaObjectClassSupport": sCmHrDpaObjectClassSupport,
       "sCmHrDpaState": sCmHrDpaState}
)
