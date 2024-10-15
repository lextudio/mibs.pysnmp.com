# SNMP MIB module (XEROX-SERVICE-MONITORING-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SERVICE-MONITORING-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:35 2024
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

xcmSvcMonTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 73)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmSvcMonGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmSvcMonJobConfirmSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmSvcMonAttachmentPDLSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmSvcMonServiceMgmtOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              1201,
              1202,
              1203,
              1204,
              1205,
              1206,
              1207,
              1208,
              1209,
              1210,
              2201,
              2202,
              2221,
              2222,
              2223,
              2224,
              2225,
              2226,
              2231,
              2232,
              2233,
              2234,
              2241,
              2242)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("other", 1),
          ("serviceBackup", 2223),
          ("serviceClean", 1205),
          ("serviceConfigure", 2225),
          ("serviceCreate", 1201),
          ("serviceDelete", 1202),
          ("serviceDiagnose", 2226),
          ("serviceDisable", 1206),
          ("serviceEnable", 1207),
          ("serviceInstall", 2221),
          ("serviceList", 1203),
          ("serviceLogin", 2241),
          ("serviceLogout", 2242),
          ("serviceManage", 2201),
          ("servicePause", 1208),
          ("serviceResetCold", 2233),
          ("serviceResetCounters", 2231),
          ("serviceResetFactory", 2234),
          ("serviceResetWarm", 2232),
          ("serviceRestart", 2202),
          ("serviceRestore", 2224),
          ("serviceResume", 1209),
          ("serviceSet", 1204),
          ("serviceShutdown", 1210),
          ("serviceUpgrade", 2222),
          ("unknown", 2))
    )



class XcmSvcMonServiceMgmtData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class XcmSvcMonServiceDetailClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              200,
              201,
              202,
              203,
              250,
              251,
              252,
              253,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              400,
              401,
              402,
              403,
              404,
              450,
              451,
              452,
              453,
              454,
              500,
              501,
              562,
              563,
              564,
              570,
              600)
        )
    )
    namedValues = NamedValues(
        *(("localAccountingServer", 100),
          ("localApplicationRelay", 307),
          ("localApplicationServer", 101),
          ("localAutomaticDiagnosticService", 570),
          ("localDatalinkRelay", 302),
          ("localDevice", 600),
          ("localDocumentServer", 102),
          ("localFileServer", 103),
          ("localJobAccountingServer", 200),
          ("localJobLoggingServer", 201),
          ("localJobProcessingServer", 202),
          ("localJobTemplateServer", 203),
          ("localLoggingServer", 104),
          ("localMailServer", 108),
          ("localNameServer", 105),
          ("localNetMgmtAgent", 400),
          ("localNetMgmtEventSource", 401),
          ("localNetMgmtEventTarget", 402),
          ("localNetMgmtProxy", 403),
          ("localNetMgmtStation", 404),
          ("localNetworkRelay", 303),
          ("localNotificationServer", 106),
          ("localOther", 3),
          ("localPhysicalRelay", 301),
          ("localPresentationRelay", 306),
          ("localProtocolConfigurationServer", 109),
          ("localSecurityServer", 107),
          ("localSessionRelay", 305),
          ("localTransportRelay", 304),
          ("other", 1),
          ("remoteAccountingServer", 150),
          ("remoteApplicationRelay", 357),
          ("remoteApplicationServer", 151),
          ("remoteDatalinkRelay", 352),
          ("remoteDirectlyConnectHost", 501),
          ("remoteDocumentServer", 152),
          ("remoteFileServer", 153),
          ("remoteJobAccountingServer", 250),
          ("remoteJobLoggingServer", 251),
          ("remoteJobProcessingServer", 252),
          ("remoteJobTemplateServer", 253),
          ("remoteLoggingServer", 154),
          ("remoteMailServer", 158),
          ("remoteNameServer", 155),
          ("remoteNetMgmtAgent", 450),
          ("remoteNetMgmtEventSource", 451),
          ("remoteNetMgmtEventTarget", 452),
          ("remoteNetMgmtProxy", 453),
          ("remoteNetMgmtStation", 454),
          ("remoteNetworkRelay", 353),
          ("remoteNetworkedHost", 500),
          ("remoteNotificationServer", 156),
          ("remoteOther", 4),
          ("remotePhysicalRelay", 351),
          ("remotePresentationRelay", 356),
          ("remoteSecurityServer", 157),
          ("remoteSessionRelay", 355),
          ("remoteTransportRelay", 354),
          ("remoteValidationServer", 159),
          ("unknown", 2),
          ("wsPrintService", 563),
          ("wsScanService", 564),
          ("xeroxResourceService", 562))
    )



class XcmSvcMonServiceDetailType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              101,
              102,
              103,
              104,
              105,
              106,
              108,
              109,
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
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              135,
              136,
              137,
              140,
              141,
              142,
              143,
              150,
              151,
              152,
              153,
              154,
              155,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
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
              181,
              182,
              183,
              184,
              185,
              186,
              187,
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
              220,
              221,
              222,
              223,
              224,
              225,
              226,
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
              240,
              241,
              242,
              243,
              244,
              245,
              250,
              251,
              252,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              281,
              282,
              283,
              284,
              285,
              287,
              288,
              291,
              292,
              293,
              294,
              295,
              299,
              301,
              302,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              400,
              401,
              402,
              403,
              404,
              405,
              500,
              501,
              502,
              503,
              504,
              510,
              515,
              520,
              550,
              551,
              570,
              571,
              600,
              601,
              602,
              603,
              604,
              610,
              700,
              701,
              702,
              703,
              704,
              705,
              706,
              720,
              721,
              722,
              723,
              730,
              731,
              732,
              733,
              740,
              741,
              742,
              743,
              744,
              745,
              746,
              747)
        )
    )
    namedValues = NamedValues(
        *(("accessPasswordRequired", 602),
          ("answerDelay", 721),
          ("autoDeleteEnabled", 600),
          ("autoDeleteInterval", 601),
          ("autoResendCount", 704),
          ("autoResendPolicy", 703),
          ("createPasswordRequired", 603),
          ("faxAutoActivityReportOn", 733),
          ("faxCountryCode", 743),
          ("faxFileFormat", 742),
          ("faxLineName", 745),
          ("faxLineNumber", 744),
          ("faxLineOptions", 746),
          ("faxReceiveHeader", 747),
          ("faxReceiveOn", 720),
          ("faxReducedImageOn", 732),
          ("faxRule", 740),
          ("faxRuleName", 741),
          ("faxSendOn", 700),
          ("faxStartingRate", 705),
          ("faxTransmissionHeader", 706),
          ("faxTransmissionReportOn", 730),
          ("faxTransmissionReportType", 731),
          ("junkFaxPrevention", 722),
          ("other", 1),
          ("redialCount", 701),
          ("redialTimeInterval", 702),
          ("scanMailboxName", 604),
          ("secureFaxOn", 723),
          ("systemAccountingEnabled", 341),
          ("systemAccountingUsage", 250),
          ("systemActivityReportEnabled", 340),
          ("systemAddress", 114),
          ("systemAlias", 126),
          ("systemAlienJobPolicy", 501),
          ("systemAuthMethod", 136),
          ("systemAuthSupport", 137),
          ("systemAvailability", 142),
          ("systemBillingConfiguration", 570),
          ("systemBillingSequenceNumber", 571),
          ("systemCancelDocSupport", 186),
          ("systemCertificateRequired", 105),
          ("systemChannelCopy", 319),
          ("systemChannelDiagnostic", 310),
          ("systemChannelFax", 311),
          ("systemChannelFileTransfer", 312),
          ("systemChannelImageProcess", 313),
          ("systemChannelMail", 314),
          ("systemChannelMultifunction", 315),
          ("systemChannelOCR", 318),
          ("systemChannelOther", 301),
          ("systemChannelPrint", 316),
          ("systemChannelScan", 317),
          ("systemChannelUnknown", 302),
          ("systemColorPassword", 610),
          ("systemConditions", 141),
          ("systemConfigurationSetting", 515),
          ("systemContext", 116),
          ("systemCurrentLocale", 119),
          ("systemCustomPaperTypeFileURI", 226),
          ("systemDescription", 112),
          ("systemDeviceStatusSupport", 179),
          ("systemDeviceXStatusSupport", 180),
          ("systemDirectoryAddressBookDefault", 389),
          ("systemDirectoryLDAPAttribute", 384),
          ("systemDirectoryLDAPObjectClass", 383),
          ("systemDirectoryLDAPSearchEnabled", 385),
          ("systemDirectoryLDAPServerType", 382),
          ("systemDirectoryLocalSearchEnabled", 386),
          ("systemDirectoryMaxSearchResult", 380),
          ("systemDirectorySearchFilter", 387),
          ("systemDirectorySearchSortKey", 388),
          ("systemDirectorySearchTimeout", 381),
          ("systemDiskCapacityAvailable", 348),
          ("systemEnabled", 143),
          ("systemEventLogFullPolicy", 502),
          ("systemEventSupport", 171),
          ("systemExcludeEventInteger", 401),
          ("systemExcludeEventOID", 403),
          ("systemExcludeEventString", 405),
          ("systemFaultLogFileURI", 224),
          ("systemFileDateTime", 222),
          ("systemFilePageCount", 223),
          ("systemFileSystemType", 200),
          ("systemFilename", 210),
          ("systemFilenameAccessRights", 221),
          ("systemFilenameConsole", 218),
          ("systemFilenameDefault", 215),
          ("systemFilenameDevice", 219),
          ("systemFilenameDirectory", 220),
          ("systemFilenameExtension", 212),
          ("systemFilenameHardLink", 217),
          ("systemFilenameIncrement", 213),
          ("systemFilenameOther", 201),
          ("systemFilenameRoot", 211),
          ("systemFilenameSoftLink", 216),
          ("systemFilenameUnknown", 202),
          ("systemFilenameWildcards", 214),
          ("systemForeignJobsVisible", 187),
          ("systemGuestJobPolicy", 500),
          ("systemHelpAddress", 131),
          ("systemHelpDescription", 132),
          ("systemHelpLocation", 133),
          ("systemHelpName", 130),
          ("systemIncludeEventInteger", 400),
          ("systemIncludeEventOID", 402),
          ("systemIncludeEventString", 404),
          ("systemInitialValDocSupport", 184),
          ("systemInitialValJobSupport", 183),
          ("systemJobAttributeDefault", 239),
          ("systemJobAttributeSupport", 238),
          ("systemJobAutoSuppression", 338),
          ("systemJobBlackColorBalance", 347),
          ("systemJobConfirmContent", 191),
          ("systemJobConfirmEnabled", 190),
          ("systemJobConfirmPolicy", 193),
          ("systemJobConfirmSheetColor", 198),
          ("systemJobConfirmSheetType", 199),
          ("systemJobConfirmSupport", 192),
          ("systemJobCopySenderEnabled", 299),
          ("systemJobCoverSheetContent", 272),
          ("systemJobCoverSheetContentKey", 273),
          ("systemJobCoverSheetContentOID", 274),
          ("systemJobCoverSheetContentText", 275),
          ("systemJobCoverSheetEnabled", 271),
          ("systemJobCyanColorBalance", 339),
          ("systemJobDayOfMonth", 324),
          ("systemJobDayOfWeek", 323),
          ("systemJobDefaultColorMode", 336),
          ("systemJobDefaultDepthResolution", 197),
          ("systemJobDefaultFeedResolution", 195),
          ("systemJobDefaultOriginalType", 337),
          ("systemJobDefaultPDL", 194),
          ("systemJobDefaultTray", 327),
          ("systemJobDefaultXFeedResolution", 196),
          ("systemJobErrorSheetContent", 282),
          ("systemJobErrorSheetContentKey", 283),
          ("systemJobErrorSheetContentOID", 284),
          ("systemJobErrorSheetContentText", 285),
          ("systemJobErrorSheetEnabled", 281),
          ("systemJobFinishingDefault", 231),
          ("systemJobFinishingSupport", 230),
          ("systemJobFrequency", 322),
          ("systemJobHoldDeleteTimeout", 333),
          ("systemJobIncompleteTimeout", 331),
          ("systemJobLogFullPolicy", 503),
          ("systemJobLogUserInformation", 320),
          ("systemJobLtrA4Substitution", 326),
          ("systemJobMagentaColorBalance", 345),
          ("systemJobMediaDefault", 237),
          ("systemJobMediaSupport", 236),
          ("systemJobOrientationDefault", 235),
          ("systemJobOrientationSupport", 234),
          ("systemJobPCLDraftMode", 328),
          ("systemJobPauseResumeTimeout", 334),
          ("systemJobPrintQuality", 329),
          ("systemJobProgrammingTimeout", 332),
          ("systemJobReceiveAttachmentType", 288),
          ("systemJobReceiveContentKey", 287),
          ("systemJobShowSenderContent", 292),
          ("systemJobShowSenderContentKey", 293),
          ("systemJobShowSenderContentOID", 294),
          ("systemJobShowSenderContentText", 295),
          ("systemJobShowSenderEnabled", 291),
          ("systemJobSidesDefault", 233),
          ("systemJobSidesSupport", 232),
          ("systemJobStateSupport", 177),
          ("systemJobTemplateAutoUpdate", 269),
          ("systemJobTemplateConfirmContent", 264),
          ("systemJobTemplateConfirmPolicy", 266),
          ("systemJobTemplateConfirmSheet", 263),
          ("systemJobTemplateConfirmSheetColor", 267),
          ("systemJobTemplateConfirmSheetType", 268),
          ("systemJobTemplateConfirmSupport", 265),
          ("systemJobTemplateCurrentCount", 262),
          ("systemJobTemplateMaxCount", 261),
          ("systemJobTemplateMaxStorage", 260),
          ("systemJobTemplateOther", 251),
          ("systemJobTemplateStatus", 270),
          ("systemJobTemplateUnknown", 252),
          ("systemJobTime", 325),
          ("systemJobUserDefinedScrns", 335),
          ("systemJobValidateSupport", 172),
          ("systemJobYellowColorBalance", 346),
          ("systemLifetimeErrorCount", 242),
          ("systemLifetimeErrorLimit", 243),
          ("systemLifetimeLimit", 241),
          ("systemLifetimeUsage", 240),
          ("systemLifetimeWarningCount", 244),
          ("systemLifetimeWarningLimit", 245),
          ("systemLocaleSupport", 175),
          ("systemLocation", 127),
          ("systemLoggingEnabled", 342),
          ("systemLogicalIndexReady", 167),
          ("systemLogicalIndexSupport", 166),
          ("systemLogicalNameReady", 163),
          ("systemLogicalNameSupport", 162),
          ("systemLoginCredentialsSource", 104),
          ("systemLoginDate", 124),
          ("systemLoginName", 122),
          ("systemLoginPassword", 123),
          ("systemLogoutDate", 125),
          ("systemMailAddress", 368),
          ("systemMailConfirmReply", 365),
          ("systemMailConfirmRequest", 364),
          ("systemMailConfirmTimeout", 366),
          ("systemMailFeatureReply", 367),
          ("systemMailImageQualityType", 378),
          ("systemMailMaxInAttachments", 371),
          ("systemMailMaxInFragments", 369),
          ("systemMailMaxInputAttach", 361),
          ("systemMailMaxInputSize", 373),
          ("systemMailMaxInputText", 360),
          ("systemMailMaxOutAttachments", 372),
          ("systemMailMaxOutFragments", 370),
          ("systemMailMaxOutputAttach", 363),
          ("systemMailMaxOutputSize", 374),
          ("systemMailMaxOutputText", 362),
          ("systemMailOutputUsage", 379),
          ("systemMailSenderGuestAuthSupport", 376),
          ("systemMailSenderNetAuthSupport", 375),
          ("systemMailSenderNoAuthSupport", 377),
          ("systemMailSignatureLine", 351),
          ("systemMailSubject", 350),
          ("systemModifyDocSupport", 173),
          ("systemMultipleDocSupport", 185),
          ("systemName", 113),
          ("systemNotificationEnabled", 343),
          ("systemOS", 110),
          ("systemOSVersion", 111),
          ("systemObjectClassSupport", 170),
          ("systemOperatorMessage", 128),
          ("systemOther", 101),
          ("systemPath", 118),
          ("systemPersonalName", 344),
          ("systemPhysicalIndexReady", 165),
          ("systemPhysicalIndexSupport", 164),
          ("systemPhysicalNameReady", 161),
          ("systemPhysicalNameSupport", 160),
          ("systemPollingEnabled", 155),
          ("systemPollingInterval", 154),
          ("systemPollingLastDate", 152),
          ("systemPollingLastTime", 153),
          ("systemPollingStartDate", 150),
          ("systemPollingStartTime", 151),
          ("systemPosixVerbsSupport", 176),
          ("systemPriority", 349),
          ("systemProblemMessage", 129),
          ("systemProtocol", 120),
          ("systemProtocolDetail", 121),
          ("systemProtocolSecurity", 135),
          ("systemRequestLogFullPolicy", 504),
          ("systemScanJobImageQualityType", 550),
          ("systemScanJobOriginalType", 551),
          ("systemScriptName", 510),
          ("systemServerTimeout", 103),
          ("systemServiceTypeSupport", 108),
          ("systemState", 140),
          ("systemTransferMethodSupport", 174),
          ("systemTranslatorReady", 182),
          ("systemTranslatorSupport", 181),
          ("systemTree", 115),
          ("systemURI", 109),
          ("systemUnknown", 102),
          ("systemUsageLogFileURI", 225),
          ("systemUseProxy", 106),
          ("systemValidationUserID", 520),
          ("systemVolume", 117),
          ("unknown", 2))
    )



class XcmSvcMonServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
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
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              550,
              560,
              561,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              700,
              701,
              702,
              703,
              704,
              705,
              706,
              707,
              708)
        )
    )
    namedValues = NamedValues(
        *(("adminCommsService", 207),
          ("adminDeviceService", 203),
          ("adminDocService", 205),
          ("adminJobService", 204),
          ("adminObjectService", 201),
          ("adminSecurityService", 206),
          ("adminServerService", 202),
          ("automaticMeterReadService", 603),
          ("automaticPagePackService", 607),
          ("automaticRemoteDiagnosticService", 606),
          ("automaticRemoteMonitoringService", 605),
          ("automaticSuppliesReplenishmentService", 604),
          ("jobServiceAnalogFax", 121),
          ("jobServiceCapturePrintSaveReprintService", 122),
          ("jobServiceCopy", 111),
          ("jobServiceFaxToFile", 105),
          ("jobServiceFaxToMailList", 107),
          ("jobServiceFaxToPrint", 106),
          ("jobServiceFileToFax", 109),
          ("jobServiceFileToFile", 112),
          ("jobServiceFileToMailList", 110),
          ("jobServiceMultifunction", 113),
          ("jobServicePrint", 108),
          ("jobServicePrintToAnalogFax", 120),
          ("jobServiceScanFromApplication", 123),
          ("jobServiceScanToAnalogFax", 116),
          ("jobServiceScanToFax", 103),
          ("jobServiceScanToFile", 101),
          ("jobServiceScanToHostFile", 118),
          ("jobServiceScanToInternetFax", 114),
          ("jobServiceScanToLocalFile", 119),
          ("jobServiceScanToMailList", 104),
          ("jobServiceScanToNetworkFile", 117),
          ("jobServiceScanToPrint", 102),
          ("jobServiceScanToServerFax", 115),
          ("localAccountingService", 400),
          ("localApplicationService", 401),
          ("localCBRService", 561),
          ("localDeviceBillingService", 415),
          ("localDiscoveryService", 560),
          ("localDiskEncryptionSecurityService", 410),
          ("localDocumentService", 402),
          ("localECommerceService", 550),
          ("localFileService", 403),
          ("localIDCardCopyService", 411),
          ("localImmediateDiskOverwriteSecurityService", 408),
          ("localLoggingService", 404),
          ("localNameService", 405),
          ("localNotificationService", 406),
          ("localOnDemandDiskOverwriteCompletionStatus", 414),
          ("localOnDemandDiskOverwriteCompletionTime", 413),
          ("localOnDemandDiskOverwriteSecurityService", 409),
          ("localSecurityService", 407),
          ("localTieredBillingService", 412),
          ("other", 1),
          ("remoteAccountingService", 500),
          ("remoteApplicationService", 501),
          ("remoteDeviceAuthenticationService", 508),
          ("remoteDocumentService", 502),
          ("remoteFileService", 503),
          ("remoteLoggingService", 504),
          ("remoteNameService", 505),
          ("remoteNotificationService", 506),
          ("remoteSecurityService", 507),
          ("systemBaseBusinessServices", 312),
          ("systemServiceAutoSoftwareUpgrade", 310),
          ("systemServiceCopy", 309),
          ("systemServiceDiagnostic", 300),
          ("systemServiceFax", 301),
          ("systemServiceFileTransfer", 302),
          ("systemServiceImageProcess", 303),
          ("systemServiceMail", 304),
          ("systemServiceMultifunction", 305),
          ("systemServiceOCR", 308),
          ("systemServicePrint", 306),
          ("systemServiceScan", 307),
          ("systemServiceSoftwareUpgrade", 311),
          ("unknown", 2),
          ("webClientCustomUIService", 601),
          ("webClientMetadataValidationService", 602),
          ("webClientTemplateManagementService", 600),
          ("webServerBillingService", 703),
          ("webServerCustomUIService", 701),
          ("webServerMcAfeeSecurityService", 707),
          ("webServerMetadataValidationService", 702),
          ("webServerProtocolConfigurationService", 705),
          ("webServerRemoteServicesConfigurationService", 708),
          ("webServerSecurityConfigurationService", 704),
          ("webServerServices", 706),
          ("webServerTemplateManagementService", 700))
    )



class XcmSvcMonServiceStateDetail(Integer32, TextualConvention):
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
              42)
        )
    )
    namedValues = NamedValues(
        *(("communicationFaultWithHost", 27),
          ("communicationWithHostManuallyDisabled", 28),
          ("criticalFaultImpactingService", 40),
          ("deregistrationPending", 32),
          ("hardwareOptionNotEnabled", 10),
          ("internalError", 33),
          ("noFaultsImpactingService", 42),
          ("nonCriticalFaultDegradingService", 41),
          ("notRegistered", 25),
          ("other", 1),
          ("proxyModeOnly", 24),
          ("rebootRequiredToDisableService", 13),
          ("rebootRequiredToEnableService", 12),
          ("registeredServiceNotEnabled", 26),
          ("registrationPending", 31),
          ("rejectedByHostAlreadyRegistered", 29),
          ("rejectedByHostInvalidSerialNo", 30),
          ("requestPending", 34),
          ("requiredHardwareNotInstalled", 8),
          ("requiredSoftwareNotInstalled", 9),
          ("serviceNotConfigured", 15),
          ("serviceNotStarted", 14),
          ("softwareOptionNotEnabled", 11),
          ("undefined16", 16),
          ("undefined17", 17),
          ("undefined18", 18),
          ("undefined19", 19),
          ("undefined20", 20),
          ("undefined21", 21),
          ("undefined22", 22),
          ("undefined23", 23),
          ("undefined3", 3),
          ("undefined35", 35),
          ("undefined36", 36),
          ("undefined37", 37),
          ("undefined38", 38),
          ("undefined39", 39),
          ("undefined4", 4),
          ("undefined5", 5),
          ("undefined6", 6),
          ("undefined7", 7),
          ("unknown", 2))
    )



class XcmSvcMonSystemMailSenderNetAuthSupport(Integer32, TextualConvention):
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
        *(("ldapEditableOnEither", 4),
          ("ldapEditableOnFailure", 3),
          ("ldapEditableOnSuccess", 2),
          ("ldapNotEditable", 1),
          ("nonLdapAuthEditable", 6),
          ("nonLdapAuthNotEditable", 5))
    )



class XcmImageQualityType(Integer32, TextualConvention):
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
        *(("auto", 5),
          ("halftone", 4),
          ("map", 7),
          ("newspaperMagazine", 6),
          ("photo", 1),
          ("phototext", 3),
          ("text", 2))
    )



class XcmOriginalType(Integer32, TextualConvention):
    status = "current"
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
        *(("inkjetOriginal", 4),
          ("none", 0),
          ("photocopiedOriginal", 2),
          ("photograph", 3),
          ("printedOriginal", 1),
          ("solidInkOriginal", 5))
    )



class XcmOutputUsage(Integer32, TextualConvention):
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
        *(("archivalRecord", 3),
          ("custom", 5),
          ("highQualityPrinting", 2),
          ("ocr", 4),
          ("sharingAndPrinting", 1),
          ("simpleScan", 6))
    )



class XcmLoginCredentialsSource(Integer32, TextualConvention):
    status = "current"
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
        *(("domainUser", 5),
          ("none", 0),
          ("promptAlways", 3),
          ("promptIfNeeded", 4),
          ("system", 2),
          ("user", 1))
    )



# MIB Managed Objects in the order of their OIDs

_XCmSvcMonDummy_ObjectIdentity = ObjectIdentity
xCmSvcMonDummy = _XCmSvcMonDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999)
)
_XCmSvcMonGroupSupport_Type = XcmSvcMonGroupSupport
_XCmSvcMonGroupSupport_Object = MibScalar
xCmSvcMonGroupSupport = _XCmSvcMonGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 1),
    _XCmSvcMonGroupSupport_Type()
)
xCmSvcMonGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonGroupSupport.setStatus("current")
_XCmSvcMonServiceMgmtOperation_Type = XcmSvcMonServiceMgmtOperation
_XCmSvcMonServiceMgmtOperation_Object = MibScalar
xCmSvcMonServiceMgmtOperation = _XCmSvcMonServiceMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 2),
    _XCmSvcMonServiceMgmtOperation_Type()
)
xCmSvcMonServiceMgmtOperation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonServiceMgmtOperation.setStatus("current")
_XCmSvcMonServiceMgmtData_Type = XcmSvcMonServiceMgmtData
_XCmSvcMonServiceMgmtData_Object = MibScalar
xCmSvcMonServiceMgmtData = _XCmSvcMonServiceMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 3),
    _XCmSvcMonServiceMgmtData_Type()
)
xCmSvcMonServiceMgmtData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonServiceMgmtData.setStatus("current")
_XCmSvcMonServiceDetailClass_Type = XcmSvcMonServiceDetailClass
_XCmSvcMonServiceDetailClass_Object = MibScalar
xCmSvcMonServiceDetailClass = _XCmSvcMonServiceDetailClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 4),
    _XCmSvcMonServiceDetailClass_Type()
)
xCmSvcMonServiceDetailClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonServiceDetailClass.setStatus("current")
_XCmSvcMonServiceDetailType_Type = XcmSvcMonServiceDetailType
_XCmSvcMonServiceDetailType_Object = MibScalar
xCmSvcMonServiceDetailType = _XCmSvcMonServiceDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 5),
    _XCmSvcMonServiceDetailType_Type()
)
xCmSvcMonServiceDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonServiceDetailType.setStatus("current")
_XCmSvcMonServiceType_Type = XcmSvcMonServiceType
_XCmSvcMonServiceType_Object = MibScalar
xCmSvcMonServiceType = _XCmSvcMonServiceType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 6),
    _XCmSvcMonServiceType_Type()
)
xCmSvcMonServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonServiceType.setStatus("current")
_XCmSvcMonJobConfirmSupport_Type = XcmSvcMonJobConfirmSupport
_XCmSvcMonJobConfirmSupport_Object = MibScalar
xCmSvcMonJobConfirmSupport = _XCmSvcMonJobConfirmSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 7),
    _XCmSvcMonJobConfirmSupport_Type()
)
xCmSvcMonJobConfirmSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonJobConfirmSupport.setStatus("current")
_XCmSvcMonSystemMailSenderNetAuthSupport_Type = XcmSvcMonSystemMailSenderNetAuthSupport
_XCmSvcMonSystemMailSenderNetAuthSupport_Object = MibScalar
xCmSvcMonSystemMailSenderNetAuthSupport = _XCmSvcMonSystemMailSenderNetAuthSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 8),
    _XCmSvcMonSystemMailSenderNetAuthSupport_Type()
)
xCmSvcMonSystemMailSenderNetAuthSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonSystemMailSenderNetAuthSupport.setStatus("current")
_XCmSvcMonAttachmentPDLSupport_Type = XcmSvcMonAttachmentPDLSupport
_XCmSvcMonAttachmentPDLSupport_Object = MibScalar
xCmSvcMonAttachmentPDLSupport = _XCmSvcMonAttachmentPDLSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 9),
    _XCmSvcMonAttachmentPDLSupport_Type()
)
xCmSvcMonAttachmentPDLSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmSvcMonAttachmentPDLSupport.setStatus("current")
_XCmImageQualityType_Type = XcmImageQualityType
_XCmImageQualityType_Object = MibScalar
xCmImageQualityType = _XCmImageQualityType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 10),
    _XCmImageQualityType_Type()
)
xCmImageQualityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmImageQualityType.setStatus("current")
_XCmOutputUsage_Type = XcmOutputUsage
_XCmOutputUsage_Object = MibScalar
xCmOutputUsage = _XCmOutputUsage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 11),
    _XCmOutputUsage_Type()
)
xCmOutputUsage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmOutputUsage.setStatus("current")
_XCMLoginCredentialsSource_Type = XcmLoginCredentialsSource
_XCMLoginCredentialsSource_Object = MibScalar
xCMLoginCredentialsSource = _XCMLoginCredentialsSource_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 73, 999, 12),
    _XCMLoginCredentialsSource_Type()
)
xCMLoginCredentialsSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCMLoginCredentialsSource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-SERVICE-MONITORING-TC",
    **{"XcmSvcMonGroupSupport": XcmSvcMonGroupSupport,
       "XcmSvcMonJobConfirmSupport": XcmSvcMonJobConfirmSupport,
       "XcmSvcMonAttachmentPDLSupport": XcmSvcMonAttachmentPDLSupport,
       "XcmSvcMonServiceMgmtOperation": XcmSvcMonServiceMgmtOperation,
       "XcmSvcMonServiceMgmtData": XcmSvcMonServiceMgmtData,
       "XcmSvcMonServiceDetailClass": XcmSvcMonServiceDetailClass,
       "XcmSvcMonServiceDetailType": XcmSvcMonServiceDetailType,
       "XcmSvcMonServiceType": XcmSvcMonServiceType,
       "XcmSvcMonServiceStateDetail": XcmSvcMonServiceStateDetail,
       "XcmSvcMonSystemMailSenderNetAuthSupport": XcmSvcMonSystemMailSenderNetAuthSupport,
       "XcmImageQualityType": XcmImageQualityType,
       "XcmOriginalType": XcmOriginalType,
       "XcmOutputUsage": XcmOutputUsage,
       "XcmLoginCredentialsSource": XcmLoginCredentialsSource,
       "xcmSvcMonTC": xcmSvcMonTC,
       "xCmSvcMonDummy": xCmSvcMonDummy,
       "xCmSvcMonGroupSupport": xCmSvcMonGroupSupport,
       "xCmSvcMonServiceMgmtOperation": xCmSvcMonServiceMgmtOperation,
       "xCmSvcMonServiceMgmtData": xCmSvcMonServiceMgmtData,
       "xCmSvcMonServiceDetailClass": xCmSvcMonServiceDetailClass,
       "xCmSvcMonServiceDetailType": xCmSvcMonServiceDetailType,
       "xCmSvcMonServiceType": xCmSvcMonServiceType,
       "xCmSvcMonJobConfirmSupport": xCmSvcMonJobConfirmSupport,
       "xCmSvcMonSystemMailSenderNetAuthSupport": xCmSvcMonSystemMailSenderNetAuthSupport,
       "xCmSvcMonAttachmentPDLSupport": xCmSvcMonAttachmentPDLSupport,
       "xCmImageQualityType": xCmImageQualityType,
       "xCmOutputUsage": xCmOutputUsage,
       "xCMLoginCredentialsSource": xCMLoginCredentialsSource}
)
