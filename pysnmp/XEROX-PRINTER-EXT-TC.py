# SNMP MIB module (XEROX-PRINTER-EXT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-PRINTER-EXT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:26 2024
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

xcmPrintTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmPrtAuxSheetContent(Integer32, TextualConvention):
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
        *(("concise", 5),
          ("notSpecified", 3),
          ("other", 1),
          ("unknown", 2),
          ("verbose", 6))
    )



class XcmPrtAuxSheetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3,
              -2,
              -1,
              1,
              2,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("jobErrorSheet", 102),
          ("jobSetEnd", 2),
          ("jobSetStart", 1),
          ("notSpecified", -3),
          ("other", -1),
          ("printerStartupSheet", 101),
          ("unknown", -2))
    )



class XcmPrtChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              26,
              27,
              28,
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
              43)
        )
    )
    namedValues = NamedValues(
        *(("chAppSocket", 12),
          ("chAppleTalkADSP", 40),
          ("chAppleTalkPAP", 7),
          ("chBidirPortTCP", 38),
          ("chCPAP", 21),
          ("chDECLAT", 32),
          ("chDLCLLCPort", 15),
          ("chFTP", 13),
          ("chFax", 18),
          ("chIBM3270", 16),
          ("chIBM5250", 17),
          ("chIEEE1284Port", 5),
          ("chIEEE1394", 19),
          ("chIRDA", 35),
          ("chLPDServer", 8),
          ("chNDPS", 43),
          ("chNPAP", 33),
          ("chNetwarePServer", 10),
          ("chNetwareRPrinter", 9),
          ("chPCPrint", 26),
          ("chPSM", 28),
          ("chParallelPort", 4),
          ("chPort9100", 11),
          ("chPortHTTP", 42),
          ("chPortSPX", 41),
          ("chPortTCP", 37),
          ("chPrintXChange", 36),
          ("chSCSIPort", 6),
          ("chSerialPort", 3),
          ("chServerMessageBlock", 27),
          ("chSystemObjectManager", 31),
          ("chTFTP", 14),
          ("chTransport1", 20),
          ("chUNPP", 39),
          ("chUSB", 34),
          ("other", 1))
    )



class XcmPrtGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmPrtIETFPrintMIBGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmPrtInterpreterLangFamily(Integer32, TextualConvention):
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
              44,
              45,
              46,
              47,
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
              58)
        )
    )
    namedValues = NamedValues(
        *(("langART", 48),
          ("langAutomatic", 37),
          ("langCCITT", 26),
          ("langCPAP", 28),
          ("langCaPSL", 43),
          ("langCodeV", 22),
          ("langDDIF", 11),
          ("langDOC", 32),
          ("langDSCDSE", 23),
          ("langDecPPL", 29),
          ("langDiagnostic", 41),
          ("langEXCL", 44),
          ("langEpson", 10),
          ("langEscapeP", 9),
          ("langHPGL", 4),
          ("langIDP", 52),
          ("langIGP", 21),
          ("langIPDS", 7),
          ("langISO6429", 13),
          ("langIntermecIPL", 56),
          ("langInterpress", 12),
          ("langLCDS", 45),
          ("langLIPS", 39),
          ("langLN03", 25),
          ("langLineData", 14),
          ("langLinePrinter", 51),
          ("langMODCA", 15),
          ("langNEC201PL", 36),
          ("langNPAP", 31),
          ("langNPDL", 35),
          ("langPCL", 3),
          ("langPCLXL", 47),
          ("langPDF", 54),
          ("langPDS", 20),
          ("langPJL", 5),
          ("langPPDS", 8),
          ("langPS", 6),
          ("langPSPrinter", 42),
          ("langPages", 38),
          ("langPinwriter", 34),
          ("langPrescribe", 50),
          ("langQUIC", 27),
          ("langREGIS", 16),
          ("langRPDL", 55),
          ("langSCS", 17),
          ("langSPDL", 18),
          ("langSimpleText", 30),
          ("langTEK4014", 19),
          ("langTIFF", 40),
          ("langTIPSI", 49),
          ("langUBIDirectProtocol", 58),
          ("langUBIFingerprint", 57),
          ("langWPS", 24),
          ("langXES", 46),
          ("langXJCL", 53),
          ("langimPress", 33),
          ("other", 1),
          ("unknown", 2))
    )



class XcmPrtMediaTypeErrorPolicy(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("abortJob", 4),
          ("ignore", 5),
          ("ignoreAfterTimeout", 11),
          ("interactWithOperator", 6),
          ("notSpecified", 3),
          ("other", 1),
          ("unknown", 2))
    )



class XcmPrtMediumClassType(Integer32, TextualConvention):
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
        *(("iso", 5),
          ("jis", 6),
          ("northAmerica", 4),
          ("notSpecified", 3),
          ("other", 1),
          ("unknown", 2))
    )



class XcmPrtMediumSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1063,
              1064,
              1065,
              1066,
              1067,
              1080,
              1081,
              1082,
              1083,
              1084,
              1085,
              1086,
              1087,
              1088,
              1089,
              1090,
              1100,
              1101,
              1102,
              1103,
              1104)
        )
    )
    namedValues = NamedValues(
        *(("a", 1011),
          ("b", 1012),
          ("c", 1013),
          ("d", 1014),
          ("e", 1015),
          ("executive", 1100),
          ("folio", 1101),
          ("invoice", 1102),
          ("isoA0", 1020),
          ("isoA1", 1021),
          ("isoA10", 1030),
          ("isoA2", 1022),
          ("isoA3", 1023),
          ("isoA4", 1024),
          ("isoA5", 1025),
          ("isoA6", 1026),
          ("isoA7", 1027),
          ("isoA8", 1028),
          ("isoA9", 1029),
          ("isoB0", 1040),
          ("isoB1", 1041),
          ("isoB10", 1050),
          ("isoB2", 1042),
          ("isoB3", 1043),
          ("isoB4", 1044),
          ("isoB5", 1045),
          ("isoB6", 1046),
          ("isoB7", 1047),
          ("isoB8", 1048),
          ("isoB9", 1049),
          ("isoC3", 1063),
          ("isoC4", 1064),
          ("isoC5", 1065),
          ("isoC6", 1066),
          ("isoDesignatedLong", 1067),
          ("jisB0", 1080),
          ("jisB1", 1081),
          ("jisB10", 1090),
          ("jisB2", 1082),
          ("jisB3", 1083),
          ("jisB4", 1084),
          ("jisB5", 1085),
          ("jisB6", 1086),
          ("jisB7", 1087),
          ("jisB8", 1088),
          ("jisB9", 1089),
          ("ledger", 1103),
          ("mediumSize13x18", 10),
          ("monarchEnvelope", 1016),
          ("na10x13Envelope", 1002),
          ("na10x14Envelope", 1007),
          ("na10x15Envelope", 1010),
          ("na6x9Envelope", 1009),
          ("na7x9Envelope", 1005),
          ("na9x11Envelope", 1006),
          ("na9x12Envelope", 1003),
          ("naLegal", 1001),
          ("naLetter", 1000),
          ("naNumber10Envelope", 1004),
          ("naNumber9Envelope", 1008),
          ("notSpecified", 3),
          ("other", 1),
          ("quarto", 1104),
          ("unknown", 2))
    )



class XcmPrtOutputOffsetStackingType(Integer32, TextualConvention):
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
        *(("noOffset", 4),
          ("notSpecified", 3),
          ("offsetOnJob", 5),
          ("offsetOnJobandCopy", 6),
          ("other", 1),
          ("unknown", 2))
    )



class XcmPrtOutputStaplePosition(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class XcmPrtPageSizeErrorPolicy(Integer32, TextualConvention):
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
        *(("abortJob", 4),
          ("ignore", 5),
          ("ignoreAfterTimeout", 11),
          ("interactWithOperator", 6),
          ("notSpecified", 3),
          ("other", 1),
          ("unknown", 2),
          ("useNearest", 9),
          ("useNearestAndAdjust", 7),
          ("useNextLarger", 10),
          ("useNextLargerAndAdjust", 8))
    )



class XcmPrtPCLFontSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              20,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              80)
        )
    )
    namedValues = NamedValues(
        *(("cartridge1", 61),
          ("cartridge2", 62),
          ("cartridge3", 63),
          ("cartridge4", 64),
          ("cartridge5", 65),
          ("cartridge6", 66),
          ("cartridge7", 67),
          ("cartridge8", 68),
          ("cartridge9", 69),
          ("internal", 20),
          ("notSpecified", 3),
          ("other", 1),
          ("permanentSoft", 80),
          ("romSimm1", 41),
          ("romSimm2", 42),
          ("romSimm3", 43),
          ("romSimm4", 44),
          ("romSimm5", 45),
          ("romSimm6", 46),
          ("romSimm7", 47),
          ("romSimm8", 48),
          ("romSimm9", 49),
          ("unknown", 2))
    )



class XcmPrtPlex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class XcmPrtPrintQuality(Integer32, TextualConvention):
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
        *(("draft", 4),
          ("high", 6),
          ("normal", 5),
          ("notSpecified", 3),
          ("other", 1),
          ("unknown", 2))
    )



class XcmPrtPrintScreen(Integer32, TextualConvention):
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
        *(("mode850", 5),
          ("mode852", 6),
          ("notSpecified", 3),
          ("off", 4),
          ("other", 1),
          ("unknown", 2))
    )



class XcmPrtTraySwitch(Integer32, TextualConvention):
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
        *(("notSpecified", 3),
          ("off", 4),
          ("other", 1),
          ("unknown", 2),
          ("useXcmPrtInputAliasTable", 6),
          ("useXcmPrtInputNextPrtInputIndex", 5))
    )



class XcmPrtGeneralMonoPrintOpt(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 5),
          ("optimizeForEconomy", 4),
          ("optimizeForSpeed", 3),
          ("other", 1))
    )



class XcmPrtOutputPunchPosition(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class XcmPrtInputTraysConfiguration(Integer32, TextualConvention):
    status = "current"
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
        *(("fiveTrays", 5),
          ("fiveTraysAndOneBypass", 12),
          ("fiveTraysAndOneBypassAndOneHCF", 15),
          ("fiveTraysAndOneHCF", 9),
          ("fourTrays", 4),
          ("fourTraysAndOneBypass", 11),
          ("fourTraysAndOneBypassAndOneHCF", 14),
          ("fourTraysAndOneHCF", 8),
          ("oneFeederWithFourTrays", 18),
          ("oneFeederWithTwoTrays", 16),
          ("oneTray", 1),
          ("sixTrays", 6),
          ("threeTrays", 3),
          ("threeTraysAndOneBypass", 10),
          ("threeTraysAndOneBypassAndOneHCF", 13),
          ("threeTraysAndOneHCF", 7),
          ("twoFeedersWithEightTrays", 19),
          ("twoFeedersWithFourTrays", 17),
          ("twoTrays", 2),
          ("undefined", 0))
    )



class XcmPrtFinisherDFAType(Integer32, TextualConvention):
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
        *(("dfaFinisher", 3),
          ("notInstalled", 2),
          ("other", 1),
          ("sbm", 4))
    )



class XcmPrtHighCapacityFeederType(Integer32, TextualConvention):
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
        *(("hcf", 3),
          ("hcfOversized", 4),
          ("hcfOversized2Trays", 5),
          ("notInstalled", 2),
          ("other", 1))
    )



class XcmPrtHolePunchUnitType(Integer32, TextualConvention):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 2),
          ("other", 1),
          ("punch2And3And4HoleStack", 24),
          ("punch2And3And5HoleNASheet", 21),
          ("punch2And3HoleNAStack", 10),
          ("punch2And3HoleStack", 22),
          ("punch2And4HoleEUStack", 11),
          ("punch2And4HoleStack", 23),
          ("punch2HoleEUSheet", 5),
          ("punch2HoleEUStack", 14),
          ("punch2HoleNASheet", 4),
          ("punch2HoleNAStack", 13),
          ("punch2HoleSheet", 3),
          ("punch2HoleStack", 12),
          ("punch3HoleNASheet", 6),
          ("punch3HoleNAStack", 16),
          ("punch3HoleStack", 15),
          ("punch4HoleEUSheet", 8),
          ("punch4HoleEUStack", 18),
          ("punch4HoleSheet", 7),
          ("punch4HoleStack", 17),
          ("punch4HoleSwedishSheet", 9),
          ("punch4HoleSwedishStack", 19),
          ("punch5HoleNASheet", 20))
    )



class XcmPrtFaxOutType(Integer32, TextualConvention):
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
        *(("faxLanAndIp", 5),
          ("faxWithsip", 4),
          ("installed", 3),
          ("notPresent", 2),
          ("other", 1))
    )



class XcmPrtPhaserModuleType(Integer32, TextualConvention):
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
        *(("b", 3),
          ("dn", 5),
          ("dp", 9),
          ("dt", 6),
          ("dx", 7),
          ("dxf", 10),
          ("gx", 8),
          ("n", 4),
          ("notSpecified", 2),
          ("other", 1))
    )



class XcmPrtPrintEngineType(Integer32, TextualConvention):
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
        *(("dual", 3),
          ("other", 1),
          ("single", 2))
    )



class XcmPrtAsciiJobTicketType(Integer32, TextualConvention):
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
        *(("asciiJobTicketAllowed", 4),
          ("asciiJobTicketRequired", 3),
          ("notPresent", 2),
          ("other", 1))
    )



class XcmPrtAuthenticationModeType(Integer32, TextualConvention):
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
        *(("commonAccessCardPiv", 3),
          ("notPresent", 2),
          ("other", 1),
          ("password", 6),
          ("pin", 5),
          ("s3", 4),
          ("smartCard", 7))
    )



class XcmPrtHoldForAuthenModeType(Integer32, TextualConvention):
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
        *(("notPresent", 2),
          ("other", 1),
          ("pin", 3),
          ("userId", 4))
    )



class XcmPrtAccountingSystemType(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("accountingGreenAccountOnly", 6),
          ("accountingGreenAll", 9),
          ("accountingGreenBillingOnly", 7),
          ("accountingGreenUserAndAccount", 8),
          ("accountingGreenUserOnly", 5),
          ("network", 4),
          ("notPresent", 2),
          ("other", 1),
          ("standard", 3))
    )



# MIB Managed Objects in the order of their OIDs

_XCmPrintTCDummy_ObjectIdentity = ObjectIdentity
xCmPrintTCDummy = _XCmPrintTCDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999)
)
_XCmPrtTCAuxSheetContent_Type = XcmPrtAuxSheetContent
_XCmPrtTCAuxSheetContent_Object = MibScalar
xCmPrtTCAuxSheetContent = _XCmPrtTCAuxSheetContent_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 1),
    _XCmPrtTCAuxSheetContent_Type()
)
xCmPrtTCAuxSheetContent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCAuxSheetContent.setStatus("current")
_XCmPrtTCXcmPrtAuxSheetType_Type = XcmPrtAuxSheetType
_XCmPrtTCXcmPrtAuxSheetType_Object = MibScalar
xCmPrtTCXcmPrtAuxSheetType = _XCmPrtTCXcmPrtAuxSheetType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 2),
    _XCmPrtTCXcmPrtAuxSheetType_Type()
)
xCmPrtTCXcmPrtAuxSheetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCXcmPrtAuxSheetType.setStatus("current")
_XCmPrtTCTCChannelType_Type = XcmPrtChannelType
_XCmPrtTCTCChannelType_Object = MibScalar
xCmPrtTCTCChannelType = _XCmPrtTCTCChannelType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 3),
    _XCmPrtTCTCChannelType_Type()
)
xCmPrtTCTCChannelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCTCChannelType.setStatus("current")
_XCmPrtTCGroupSupport_Type = XcmPrtGroupSupport
_XCmPrtTCGroupSupport_Object = MibScalar
xCmPrtTCGroupSupport = _XCmPrtTCGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 4),
    _XCmPrtTCGroupSupport_Type()
)
xCmPrtTCGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCGroupSupport.setStatus("current")
_XCmPrtTCIETFPrintMIBGroupSupport_Type = XcmPrtIETFPrintMIBGroupSupport
_XCmPrtTCIETFPrintMIBGroupSupport_Object = MibScalar
xCmPrtTCIETFPrintMIBGroupSupport = _XCmPrtTCIETFPrintMIBGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 5),
    _XCmPrtTCIETFPrintMIBGroupSupport_Type()
)
xCmPrtTCIETFPrintMIBGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCIETFPrintMIBGroupSupport.setStatus("current")
_XCmPrtTCInterpreterLangFamily_Type = XcmPrtInterpreterLangFamily
_XCmPrtTCInterpreterLangFamily_Object = MibScalar
xCmPrtTCInterpreterLangFamily = _XCmPrtTCInterpreterLangFamily_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 6),
    _XCmPrtTCInterpreterLangFamily_Type()
)
xCmPrtTCInterpreterLangFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCInterpreterLangFamily.setStatus("current")
_XCmPrtTCMediaTypeErrorPolicy_Type = XcmPrtMediaTypeErrorPolicy
_XCmPrtTCMediaTypeErrorPolicy_Object = MibScalar
xCmPrtTCMediaTypeErrorPolicy = _XCmPrtTCMediaTypeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 7),
    _XCmPrtTCMediaTypeErrorPolicy_Type()
)
xCmPrtTCMediaTypeErrorPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCMediaTypeErrorPolicy.setStatus("current")
_XCmPrtTCMediumClassType_Type = XcmPrtMediumClassType
_XCmPrtTCMediumClassType_Object = MibScalar
xCmPrtTCMediumClassType = _XCmPrtTCMediumClassType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 8),
    _XCmPrtTCMediumClassType_Type()
)
xCmPrtTCMediumClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCMediumClassType.setStatus("current")
_XCmPrtTCMediumSize_Type = XcmPrtMediumSize
_XCmPrtTCMediumSize_Object = MibScalar
xCmPrtTCMediumSize = _XCmPrtTCMediumSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 9),
    _XCmPrtTCMediumSize_Type()
)
xCmPrtTCMediumSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCMediumSize.setStatus("current")
_XCmPrtTCOutputOffsetStackingType_Type = XcmPrtOutputOffsetStackingType
_XCmPrtTCOutputOffsetStackingType_Object = MibScalar
xCmPrtTCOutputOffsetStackingType = _XCmPrtTCOutputOffsetStackingType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 10),
    _XCmPrtTCOutputOffsetStackingType_Type()
)
xCmPrtTCOutputOffsetStackingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCOutputOffsetStackingType.setStatus("current")
_XCmPrtOutputStaplePosition_Type = XcmPrtOutputStaplePosition
_XCmPrtOutputStaplePosition_Object = MibScalar
xCmPrtOutputStaplePosition = _XCmPrtOutputStaplePosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 11),
    _XCmPrtOutputStaplePosition_Type()
)
xCmPrtOutputStaplePosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtOutputStaplePosition.setStatus("current")
_XCmPrtTCPageSizeErrorPolicy_Type = XcmPrtPageSizeErrorPolicy
_XCmPrtTCPageSizeErrorPolicy_Object = MibScalar
xCmPrtTCPageSizeErrorPolicy = _XCmPrtTCPageSizeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 12),
    _XCmPrtTCPageSizeErrorPolicy_Type()
)
xCmPrtTCPageSizeErrorPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPageSizeErrorPolicy.setStatus("current")
_XCmPrtTCPCLFontSource_Type = XcmPrtPCLFontSource
_XCmPrtTCPCLFontSource_Object = MibScalar
xCmPrtTCPCLFontSource = _XCmPrtTCPCLFontSource_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 13),
    _XCmPrtTCPCLFontSource_Type()
)
xCmPrtTCPCLFontSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPCLFontSource.setStatus("current")
_XCmPrtTCPlex_Type = XcmPrtPlex
_XCmPrtTCPlex_Object = MibScalar
xCmPrtTCPlex = _XCmPrtTCPlex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 14),
    _XCmPrtTCPlex_Type()
)
xCmPrtTCPlex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPlex.setStatus("current")
_XCmPrtTCPrintQuality_Type = XcmPrtPrintQuality
_XCmPrtTCPrintQuality_Object = MibScalar
xCmPrtTCPrintQuality = _XCmPrtTCPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 15),
    _XCmPrtTCPrintQuality_Type()
)
xCmPrtTCPrintQuality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPrintQuality.setStatus("current")
_XCmPrtTCPrintScreen_Type = XcmPrtPrintScreen
_XCmPrtTCPrintScreen_Object = MibScalar
xCmPrtTCPrintScreen = _XCmPrtTCPrintScreen_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 16),
    _XCmPrtTCPrintScreen_Type()
)
xCmPrtTCPrintScreen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPrintScreen.setStatus("current")
_XCmPrtTCTraySwitch_Type = XcmPrtTraySwitch
_XCmPrtTCTraySwitch_Object = MibScalar
xCmPrtTCTraySwitch = _XCmPrtTCTraySwitch_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 17),
    _XCmPrtTCTraySwitch_Type()
)
xCmPrtTCTraySwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCTraySwitch.setStatus("current")
_XCmPrtTCGeneralMonoPrintOpt_Type = XcmPrtGeneralMonoPrintOpt
_XCmPrtTCGeneralMonoPrintOpt_Object = MibScalar
xCmPrtTCGeneralMonoPrintOpt = _XCmPrtTCGeneralMonoPrintOpt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 18),
    _XCmPrtTCGeneralMonoPrintOpt_Type()
)
xCmPrtTCGeneralMonoPrintOpt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCGeneralMonoPrintOpt.setStatus("current")
_XCmPrtOutputPunchPosition_Type = XcmPrtOutputPunchPosition
_XCmPrtOutputPunchPosition_Object = MibScalar
xCmPrtOutputPunchPosition = _XCmPrtOutputPunchPosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 19),
    _XCmPrtOutputPunchPosition_Type()
)
xCmPrtOutputPunchPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtOutputPunchPosition.setStatus("current")
_XCmPrtInputTraysConfiguration_Type = XcmPrtInputTraysConfiguration
_XCmPrtInputTraysConfiguration_Object = MibScalar
xCmPrtInputTraysConfiguration = _XCmPrtInputTraysConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 20),
    _XCmPrtInputTraysConfiguration_Type()
)
xCmPrtInputTraysConfiguration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtInputTraysConfiguration.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-PRINTER-EXT-TC",
    **{"XcmPrtAuxSheetContent": XcmPrtAuxSheetContent,
       "XcmPrtAuxSheetType": XcmPrtAuxSheetType,
       "XcmPrtChannelType": XcmPrtChannelType,
       "XcmPrtGroupSupport": XcmPrtGroupSupport,
       "XcmPrtIETFPrintMIBGroupSupport": XcmPrtIETFPrintMIBGroupSupport,
       "XcmPrtInterpreterLangFamily": XcmPrtInterpreterLangFamily,
       "XcmPrtMediaTypeErrorPolicy": XcmPrtMediaTypeErrorPolicy,
       "XcmPrtMediumClassType": XcmPrtMediumClassType,
       "XcmPrtMediumSize": XcmPrtMediumSize,
       "XcmPrtOutputOffsetStackingType": XcmPrtOutputOffsetStackingType,
       "XcmPrtOutputStaplePosition": XcmPrtOutputStaplePosition,
       "XcmPrtPageSizeErrorPolicy": XcmPrtPageSizeErrorPolicy,
       "XcmPrtPCLFontSource": XcmPrtPCLFontSource,
       "XcmPrtPlex": XcmPrtPlex,
       "XcmPrtPrintQuality": XcmPrtPrintQuality,
       "XcmPrtPrintScreen": XcmPrtPrintScreen,
       "XcmPrtTraySwitch": XcmPrtTraySwitch,
       "XcmPrtGeneralMonoPrintOpt": XcmPrtGeneralMonoPrintOpt,
       "XcmPrtOutputPunchPosition": XcmPrtOutputPunchPosition,
       "XcmPrtInputTraysConfiguration": XcmPrtInputTraysConfiguration,
       "XcmPrtFinisherDFAType": XcmPrtFinisherDFAType,
       "XcmPrtHighCapacityFeederType": XcmPrtHighCapacityFeederType,
       "XcmPrtHolePunchUnitType": XcmPrtHolePunchUnitType,
       "XcmPrtFaxOutType": XcmPrtFaxOutType,
       "XcmPrtPhaserModuleType": XcmPrtPhaserModuleType,
       "XcmPrtPrintEngineType": XcmPrtPrintEngineType,
       "XcmPrtAsciiJobTicketType": XcmPrtAsciiJobTicketType,
       "XcmPrtAuthenticationModeType": XcmPrtAuthenticationModeType,
       "XcmPrtHoldForAuthenModeType": XcmPrtHoldForAuthenModeType,
       "XcmPrtAccountingSystemType": XcmPrtAccountingSystemType,
       "xcmPrintTC": xcmPrintTC,
       "xCmPrintTCDummy": xCmPrintTCDummy,
       "xCmPrtTCAuxSheetContent": xCmPrtTCAuxSheetContent,
       "xCmPrtTCXcmPrtAuxSheetType": xCmPrtTCXcmPrtAuxSheetType,
       "xCmPrtTCTCChannelType": xCmPrtTCTCChannelType,
       "xCmPrtTCGroupSupport": xCmPrtTCGroupSupport,
       "xCmPrtTCIETFPrintMIBGroupSupport": xCmPrtTCIETFPrintMIBGroupSupport,
       "xCmPrtTCInterpreterLangFamily": xCmPrtTCInterpreterLangFamily,
       "xCmPrtTCMediaTypeErrorPolicy": xCmPrtTCMediaTypeErrorPolicy,
       "xCmPrtTCMediumClassType": xCmPrtTCMediumClassType,
       "xCmPrtTCMediumSize": xCmPrtTCMediumSize,
       "xCmPrtTCOutputOffsetStackingType": xCmPrtTCOutputOffsetStackingType,
       "xCmPrtOutputStaplePosition": xCmPrtOutputStaplePosition,
       "xCmPrtTCPageSizeErrorPolicy": xCmPrtTCPageSizeErrorPolicy,
       "xCmPrtTCPCLFontSource": xCmPrtTCPCLFontSource,
       "xCmPrtTCPlex": xCmPrtTCPlex,
       "xCmPrtTCPrintQuality": xCmPrtTCPrintQuality,
       "xCmPrtTCPrintScreen": xCmPrtTCPrintScreen,
       "xCmPrtTCTraySwitch": xCmPrtTCTraySwitch,
       "xCmPrtTCGeneralMonoPrintOpt": xCmPrtTCGeneralMonoPrintOpt,
       "xCmPrtOutputPunchPosition": xCmPrtOutputPunchPosition,
       "xCmPrtInputTraysConfiguration": xCmPrtInputTraysConfiguration}
)
