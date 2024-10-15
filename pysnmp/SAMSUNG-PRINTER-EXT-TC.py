# SNMP MIB module (SAMSUNG-PRINTER-EXT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-PRINTER-EXT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:41 2024
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

scmPrintTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScmPrtAuxSheetContent(Integer32, TextualConvention):
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



class ScmPrtAuxSheetType(Integer32, TextualConvention):
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



class ScmPrtChannelType(Integer32, TextualConvention):
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



class ScmPrtGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmPrtIETFPrintMIBGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScmPrtInterpreterLangFamily(Integer32, TextualConvention):
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



class ScmPrtMediaTypeErrorPolicy(Integer32, TextualConvention):
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



class ScmPrtMediumClassType(Integer32, TextualConvention):
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



class ScmPrtMediumSize(Integer32, TextualConvention):
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



class ScmPrtOutputOffsetStackingType(Integer32, TextualConvention):
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



class ScmPrtOutputStaplePosition(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ScmPrtPageSizeErrorPolicy(Integer32, TextualConvention):
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



class ScmPrtPCLFontSource(Integer32, TextualConvention):
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



class ScmPrtPlex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ScmPrtPrintQuality(Integer32, TextualConvention):
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



class ScmPrtPrintScreen(Integer32, TextualConvention):
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



class ScmPrtTraySwitch(Integer32, TextualConvention):
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
          ("useScmPrtInputAliasTable", 6),
          ("useScmPrtInputNextPrtInputIndex", 5))
    )



class ScmPrtGeneralMonoPrintOpt(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_SCmPrintTCDummy_ObjectIdentity = ObjectIdentity
sCmPrintTCDummy = _SCmPrintTCDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999)
)
_SCmPrtTCAuxSheetContent_Type = ScmPrtAuxSheetContent
_SCmPrtTCAuxSheetContent_Object = MibScalar
sCmPrtTCAuxSheetContent = _SCmPrtTCAuxSheetContent_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 1),
    _SCmPrtTCAuxSheetContent_Type()
)
sCmPrtTCAuxSheetContent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCAuxSheetContent.setStatus("current")
_SCmPrtTCScmPrtAuxSheetType_Type = ScmPrtAuxSheetType
_SCmPrtTCScmPrtAuxSheetType_Object = MibScalar
sCmPrtTCScmPrtAuxSheetType = _SCmPrtTCScmPrtAuxSheetType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 2),
    _SCmPrtTCScmPrtAuxSheetType_Type()
)
sCmPrtTCScmPrtAuxSheetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCScmPrtAuxSheetType.setStatus("current")
_SCmPrtTCTCChannelType_Type = ScmPrtChannelType
_SCmPrtTCTCChannelType_Object = MibScalar
sCmPrtTCTCChannelType = _SCmPrtTCTCChannelType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 3),
    _SCmPrtTCTCChannelType_Type()
)
sCmPrtTCTCChannelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCTCChannelType.setStatus("current")
_SCmPrtTCGroupSupport_Type = ScmPrtGroupSupport
_SCmPrtTCGroupSupport_Object = MibScalar
sCmPrtTCGroupSupport = _SCmPrtTCGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 4),
    _SCmPrtTCGroupSupport_Type()
)
sCmPrtTCGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCGroupSupport.setStatus("current")
_SCmPrtTCIETFPrintMIBGroupSupport_Type = ScmPrtIETFPrintMIBGroupSupport
_SCmPrtTCIETFPrintMIBGroupSupport_Object = MibScalar
sCmPrtTCIETFPrintMIBGroupSupport = _SCmPrtTCIETFPrintMIBGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 5),
    _SCmPrtTCIETFPrintMIBGroupSupport_Type()
)
sCmPrtTCIETFPrintMIBGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCIETFPrintMIBGroupSupport.setStatus("current")
_SCmPrtTCInterpreterLangFamily_Type = ScmPrtInterpreterLangFamily
_SCmPrtTCInterpreterLangFamily_Object = MibScalar
sCmPrtTCInterpreterLangFamily = _SCmPrtTCInterpreterLangFamily_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 6),
    _SCmPrtTCInterpreterLangFamily_Type()
)
sCmPrtTCInterpreterLangFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCInterpreterLangFamily.setStatus("current")
_SCmPrtTCMediaTypeErrorPolicy_Type = ScmPrtMediaTypeErrorPolicy
_SCmPrtTCMediaTypeErrorPolicy_Object = MibScalar
sCmPrtTCMediaTypeErrorPolicy = _SCmPrtTCMediaTypeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 7),
    _SCmPrtTCMediaTypeErrorPolicy_Type()
)
sCmPrtTCMediaTypeErrorPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCMediaTypeErrorPolicy.setStatus("current")
_SCmPrtTCMediumClassType_Type = ScmPrtMediumClassType
_SCmPrtTCMediumClassType_Object = MibScalar
sCmPrtTCMediumClassType = _SCmPrtTCMediumClassType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 8),
    _SCmPrtTCMediumClassType_Type()
)
sCmPrtTCMediumClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCMediumClassType.setStatus("current")
_SCmPrtTCMediumSize_Type = ScmPrtMediumSize
_SCmPrtTCMediumSize_Object = MibScalar
sCmPrtTCMediumSize = _SCmPrtTCMediumSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 9),
    _SCmPrtTCMediumSize_Type()
)
sCmPrtTCMediumSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCMediumSize.setStatus("current")
_SCmPrtTCOutputOffsetStackingType_Type = ScmPrtOutputOffsetStackingType
_SCmPrtTCOutputOffsetStackingType_Object = MibScalar
sCmPrtTCOutputOffsetStackingType = _SCmPrtTCOutputOffsetStackingType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 10),
    _SCmPrtTCOutputOffsetStackingType_Type()
)
sCmPrtTCOutputOffsetStackingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCOutputOffsetStackingType.setStatus("current")
_SCmPrtOutputStaplePosition_Type = ScmPrtOutputStaplePosition
_SCmPrtOutputStaplePosition_Object = MibScalar
sCmPrtOutputStaplePosition = _SCmPrtOutputStaplePosition_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 11),
    _SCmPrtOutputStaplePosition_Type()
)
sCmPrtOutputStaplePosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtOutputStaplePosition.setStatus("current")
_SCmPrtTCPageSizeErrorPolicy_Type = ScmPrtPageSizeErrorPolicy
_SCmPrtTCPageSizeErrorPolicy_Object = MibScalar
sCmPrtTCPageSizeErrorPolicy = _SCmPrtTCPageSizeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 12),
    _SCmPrtTCPageSizeErrorPolicy_Type()
)
sCmPrtTCPageSizeErrorPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCPageSizeErrorPolicy.setStatus("current")
_SCmPrtTCPCLFontSource_Type = ScmPrtPCLFontSource
_SCmPrtTCPCLFontSource_Object = MibScalar
sCmPrtTCPCLFontSource = _SCmPrtTCPCLFontSource_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 13),
    _SCmPrtTCPCLFontSource_Type()
)
sCmPrtTCPCLFontSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCPCLFontSource.setStatus("current")
_SCmPrtTCPlex_Type = ScmPrtPlex
_SCmPrtTCPlex_Object = MibScalar
sCmPrtTCPlex = _SCmPrtTCPlex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 14),
    _SCmPrtTCPlex_Type()
)
sCmPrtTCPlex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCPlex.setStatus("current")
_SCmPrtTCPrintQuality_Type = ScmPrtPrintQuality
_SCmPrtTCPrintQuality_Object = MibScalar
sCmPrtTCPrintQuality = _SCmPrtTCPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 15),
    _SCmPrtTCPrintQuality_Type()
)
sCmPrtTCPrintQuality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCPrintQuality.setStatus("current")
_SCmPrtTCPrintScreen_Type = ScmPrtPrintScreen
_SCmPrtTCPrintScreen_Object = MibScalar
sCmPrtTCPrintScreen = _SCmPrtTCPrintScreen_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 16),
    _SCmPrtTCPrintScreen_Type()
)
sCmPrtTCPrintScreen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCPrintScreen.setStatus("current")
_SCmPrtTCTraySwitch_Type = ScmPrtTraySwitch
_SCmPrtTCTraySwitch_Object = MibScalar
sCmPrtTCTraySwitch = _SCmPrtTCTraySwitch_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 17),
    _SCmPrtTCTraySwitch_Type()
)
sCmPrtTCTraySwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCTraySwitch.setStatus("current")
_SCmPrtTCGeneralMonoPrintOpt_Type = ScmPrtGeneralMonoPrintOpt
_SCmPrtTCGeneralMonoPrintOpt_Object = MibScalar
sCmPrtTCGeneralMonoPrintOpt = _SCmPrtTCGeneralMonoPrintOpt_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 18),
    _SCmPrtTCGeneralMonoPrintOpt_Type()
)
sCmPrtTCGeneralMonoPrintOpt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCmPrtTCGeneralMonoPrintOpt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-PRINTER-EXT-TC",
    **{"ScmPrtAuxSheetContent": ScmPrtAuxSheetContent,
       "ScmPrtAuxSheetType": ScmPrtAuxSheetType,
       "ScmPrtChannelType": ScmPrtChannelType,
       "ScmPrtGroupSupport": ScmPrtGroupSupport,
       "ScmPrtIETFPrintMIBGroupSupport": ScmPrtIETFPrintMIBGroupSupport,
       "ScmPrtInterpreterLangFamily": ScmPrtInterpreterLangFamily,
       "ScmPrtMediaTypeErrorPolicy": ScmPrtMediaTypeErrorPolicy,
       "ScmPrtMediumClassType": ScmPrtMediumClassType,
       "ScmPrtMediumSize": ScmPrtMediumSize,
       "ScmPrtOutputOffsetStackingType": ScmPrtOutputOffsetStackingType,
       "ScmPrtOutputStaplePosition": ScmPrtOutputStaplePosition,
       "ScmPrtPageSizeErrorPolicy": ScmPrtPageSizeErrorPolicy,
       "ScmPrtPCLFontSource": ScmPrtPCLFontSource,
       "ScmPrtPlex": ScmPrtPlex,
       "ScmPrtPrintQuality": ScmPrtPrintQuality,
       "ScmPrtPrintScreen": ScmPrtPrintScreen,
       "ScmPrtTraySwitch": ScmPrtTraySwitch,
       "ScmPrtGeneralMonoPrintOpt": ScmPrtGeneralMonoPrintOpt,
       "scmPrintTC": scmPrintTC,
       "sCmPrintTCDummy": sCmPrintTCDummy,
       "sCmPrtTCAuxSheetContent": sCmPrtTCAuxSheetContent,
       "sCmPrtTCScmPrtAuxSheetType": sCmPrtTCScmPrtAuxSheetType,
       "sCmPrtTCTCChannelType": sCmPrtTCTCChannelType,
       "sCmPrtTCGroupSupport": sCmPrtTCGroupSupport,
       "sCmPrtTCIETFPrintMIBGroupSupport": sCmPrtTCIETFPrintMIBGroupSupport,
       "sCmPrtTCInterpreterLangFamily": sCmPrtTCInterpreterLangFamily,
       "sCmPrtTCMediaTypeErrorPolicy": sCmPrtTCMediaTypeErrorPolicy,
       "sCmPrtTCMediumClassType": sCmPrtTCMediumClassType,
       "sCmPrtTCMediumSize": sCmPrtTCMediumSize,
       "sCmPrtTCOutputOffsetStackingType": sCmPrtTCOutputOffsetStackingType,
       "sCmPrtOutputStaplePosition": sCmPrtOutputStaplePosition,
       "sCmPrtTCPageSizeErrorPolicy": sCmPrtTCPageSizeErrorPolicy,
       "sCmPrtTCPCLFontSource": sCmPrtTCPCLFontSource,
       "sCmPrtTCPlex": sCmPrtTCPlex,
       "sCmPrtTCPrintQuality": sCmPrtTCPrintQuality,
       "sCmPrtTCPrintScreen": sCmPrtTCPrintScreen,
       "sCmPrtTCTraySwitch": sCmPrtTCTraySwitch,
       "sCmPrtTCGeneralMonoPrintOpt": sCmPrtTCGeneralMonoPrintOpt}
)
