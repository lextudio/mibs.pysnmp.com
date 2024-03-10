"""SNMP MIB module (XEROX-PRINTER-EXT-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-PRINTER-EXT-TC
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:17 2024
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
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Integer32,
 Gauge32,
 Bits,
 MibIdentifier,
 TimeTicks,
 Counter64,
 ModuleIdentity,
 NotificationType,
 iso,
 Unsigned32,
 IpAddress) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "Gauge32",
    "Bits",
    "MibIdentifier",
    "TimeTicks",
    "Counter64",
    "ModuleIdentity",
    "NotificationType",
    "iso",
    "Unsigned32",
    "IpAddress")

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
xcmPrintTC.setLastUpdated("1304100000Z")
if mibBuilder.loadTexts:
    xcmPrintTC.setOrganization("""\
Xerox Common Management Interface Working Group
""")
xcmPrintTC.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmPrintTC.setDescription("""\
 Version: 6.004.pub XCMI Extensions to Printer MIB Textual Conventions. This
Module provides Xerox extensions of the IETF Printer MIB. Copyright (C)
1997-2013 Xerox Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmPrtAuxSheetContent(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 Auxiliary sheets are added by the printing system and are not part of the
actual print job. Examples include error pages and banner pages. This textual
convention is used to specify the information content of auxiliary sheets.
"""


class XcmPrtAuxSheetType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 Auxiliary sheets are added by the printing system and are not part of the
actual print job. This attribute uniquely identifies an auxiliary-sheet, which
includes the types jobErrorSheet and printerStartupSheet. 'printerStartupSheet'
is a sheet printed shortly after power-up when the device is ready. Typical
startup pages include test patterns and/or printer configuration information.
'jobErrorSheet' is a sheet printed with error messages generated during the
printing of a job-result-set that is to be printed with the hardcopy output of
that job-result-set, and should be printed on an ending sheet of the job-
result-set, or some similar sheet. These sheets are not a part of any job-copy.
If no error messages have been generated, the device need not print an extra
page. The default for this page type should be 'On'. The following Auxiliary-
sheet-package types can be specified either for a job component (job result set
or job copy) or document (document result set or document copy). For now, only
the jobSetStart package has been enumerated. 'jobSetStart' - Auxiliary-sheet
starts each result-set Sometimes referred to as a jobBanner sheet 'jobSetEnd' -
Auxiliary-sheet at the end of a result set
"""


class XcmPrtChannelType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 This enumeration indicates the type of channel that is receiving jobs. This
enumeration is being added to the IETF Printer MIB. This is an IETF type 2
enum.
"""


class XcmPrtGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional Printer MIB Extension object groups, specified in a bit-mask. The
current set of values (which may be extended in the future) is given below: 1 :
xcmPrtBaseGroup -- 2**0 2 : xcmPrtGeneralGroup -- 2**1 4 : xcmPrtInputGroup --
2**2 8 : xcmPrtOutputGroup -- 2**3 16 : xcmPrtChannelGroup -- 2**4 32 :
xcmPrtInterpreterGroup -- 2**5 64 : xcmPrtInputAliasGroup -- 2**6 128 :
xcmPrtGeneralAuxSheetGroup -- 2**7 256 : xcmPrtGeneralProdSpecificGroup -- 2**8
512 : xcmPrtAuxPackageGroup -- 2**9 1024 : xcmPrtChannelProdSpecificGroup --
2**10 2048 : xcmPrtInterpProdSpecificGroup -- 2**11 4096 : xcmPrtInterpPCLGroup
-- 2**12 8192 : xcmPrtInterpPCLProdSpecificGroup -- 2**13 16384 :
xcmPrtMediumTypeSupportedGroup -- 2**14 32768 :
xcmPrtGeneralInstalledOptionsGroup -- 2**15 Usage: Conforming management agents
shall ALWAYS accurately report their support for XCMI Printer MIB Extensions
object groups.
"""


class XcmPrtIETFPrintMIBGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional IETF Printer MIB object groups, specified in a bit-mask. The current
set of values (which may be extended in the future) is given below: 1 :
prtGeneralGroup -- 2**0 (mandatory) 2 : prtResponsiblePartyGroup -- 2**1 4 :
prtInputGroup -- 2**2 (mandatory) 8 : prtExtendedInputGroup -- 2**3 16 :
prtInputMediaGroup -- 2**4 32 : prtOutputGroup -- 2**5 (mandatory) 64 :
prtExtendedOutputGroup -- 2**6 128 : prtOutputDimensionsGroup -- 2**7 256 :
prtOutputFeaturesGroup -- 2**8 512 : prtMarkerGroup -- 2**9 (mandatory) 1024 :
prtMarkerSuppliesGroup -- 2**10 2048 : prtMarkerColorantGroup -- 2**11 4096 :
prtMediaPathGroup -- 2**12 (mandatory) 8192 : prtChannelGroup -- 2**13
(mandatory) 16384 : prtInterpreterGroup -- 2**14 (mandatory) 32768 :
prtConsoleGroup -- 2**15 (mandatory) 65536 : prtAlertTableGroup -- 2**16
(mandatory) 131072 : prtAuxiliarySheetGroup -- 2**17 262144 :
prtInputSwitchingGroup -- 2**18 Usage: Conforming management agents shall
ALWAYS accurately report their support for IETF Printer MIB object groups.
"""


class XcmPrtInterpreterLangFamily(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 This enumeration indicates the type of interpreter that is receiving jobs.
This enumeration is being added to the IETF Printer MIB. This value is an IETF
type 2 enumeration.
"""


class XcmPrtMediaTypeErrorPolicy(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 Controls interpreter behavior when the requested Media Type is not currently
available. * The values 'other' and 'unknown' are deprecated for conforming
implementations. * 'abortJob' will cause the interpreter to abort the job with
an appropriate error condition. * 'ignore' will cause the job to be printed on
the default media as specified by xcmPrtInterpInputIndexDefault OR
xcmPrtInterpPaperSizeDefault OR any available media deemed appropriate by the
implementation. No adjustment will be made to the image size. Exact semantics
of this setting are product specific. * 'interactWithOperator' will cause the
printer to interact with the operator to determine what to do. For example,
display a message at the operator console requesting the desired media. The
semantics of this policy vary among different products and environments. *
'ignoreAfterTimeout' will cause the job to be ignored same as 'ignore' above,
but not till after xcmPrtInterpErrorPolicyTimeout expires.
"""


class XcmPrtMediumClassType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 Paper size classes for a printer.
"""


class XcmPrtMediumSize(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 This attribute specifies the size of this medium by means of a pre-defined
value. The medium size specified in this manner may be one of the standard
sizes to which object identifiers have been assigned in ISO/IEC 10175 (DPA), or
another applicable standard, or for which a value has been created.
Enumerations for DPA defined medium sizes are derived by adding 1000 to the
ISO/IEC 10175 enumerations. XCMI defined enumerations start at 10.
"""


class XcmPrtOutputOffsetStackingType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 Offset stacking types further refining that specified by the object
prtOutputOffsetStacking in the Printer MIB. - offsetOnJob means that each job
is offset but copies within the job are not offset. - offsetOnJobAndCopy means
that there is an offset on job and copy boundaries.
"""


class XcmPrtOutputStaplePosition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 This Textual Convention enumerates possible staple positions. The staple
positions enumerated are relative to the physical layout of the finishing
device. The observer is on the front side of the finisher which is defined as
for sheets passing through the finisher. The 'front' side is the side from
which staples are pushed. The physical corners of the finishing device are
specified by designating the corner of the finisher where a portrait long-edge
fed sheet with english/left-to-right text is stapled as staplePosCorner1, and
then the other corners are numbered in a counter-clockwise direction with the
observer on the front side of the finisher. 'staplePosCorner1',
'staplePosCorner2', 'staplePosCorner3', and 'staplePosCorner4' indicate a
single staple in the specified corner. This object does not specify the angle
of the staple, e.g. 90, 45 or zero degrees. 'stapleEdge...' indicates multiple
staples on the edge specified. 'stapleEdge12' is the edge which include Corner1
and Corner2. The current set of values (which may be extended in the future) is
given below: 1 : staplePosCorner1 -- 2**0 2 : staplePosCorner2 -- 2**1 4 :
staplePosCorner3 -- 2**2 8 : staplePosCorner4 -- 2**3 16 : stapleEdge12 -- 2**4
32 : stapleEdge23 -- 2**5 64 : stapleEdge34 -- 2**6 128 : stapleEdge14 -- 2**7
"""


class XcmPrtPageSizeErrorPolicy(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 Controls interpreter behavior when the requested Page Size is not currently
available. * The values 'other' and 'unknown' are deprecated for conforming
implementations. * 'abortJob' will cause the interpreter to abort the job with
an appropriate error condition. * 'ignore' will cause the job to be printed on
the default media as specified by xcmPrtInterpInputIndexDefault OR
xcmPrtInterpPaperSizeDefault OR any available media deemed appropriate by the
implementation. No adjustment will be made to the image size. Exact semantics
of this setting are product specific. * 'interactWithOperator' will cause the
printer to interact with the operator to determine what to do. For example,
display a message at the operator console requesting the desired media. The
semantics of this policy vary among different products and environments. *
'useNearestAndAdjust' will cause the job to be printed on the nearest available
media (as described below). The interpreter will adjust the image size (by
scaling and centering) to fit. * 'useNextLargerAndAdjust' will cause the job to
be printed on the next larger available media (as described below). The
interpreter will adjust the image size (by scaling and centering) to fit. *
'useNearest' will cause the job to be printed on the nearest available media
(as described below). No adjustment will be made to the image size. *
'useNextLarger' will cause the job to be printed on the next larger available
media (as described below). No adjustment will be made to the image size. *
'ignoreAfterTimeout' will cause the job to be ignored same as ignore' above,
but not till after xcmPrtInterpErrorPolicyTimeout expires. In the above
descriptions, nearest size is defined as the one closest in area to the
requested size. The next larger size is the one that is at least as large as
the requested size in both width and height and is smallest in area. To adjust
the page means to scale the page image (if necessary) to fit the medium, then
center the image on the medium.
"""


class XcmPrtPCLFontSource(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\

"""


class XcmPrtPlex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 This Textual Convention enumerates plex modes which may be supported by a
printer or interpreter. A plex mode specifies whether pages are to be printed
one-sided or two-sided, as well as the content orientation between consecutive
pages. For the XcmPrtPlex TC, the following definitions apply: 'one-sided' -
Print on only one side of each sheet. 'two-sided' - Print on both sides of each
sheet. 'simplex' - The document pages are to be oriented so as to condition
them for one-sided printing. 'long-edge-bind' - The document pages are to be
oriented so as to condition them for two-sided printing, bound along the length
(the longer edge) of the physical page. 'short-edge-bind' - The document pages
are to be oriented so as to condition them for two-sided printing, bound along
the width (the shorter edge) of the physical page. XcmPrtPlex's representation
is bit-encoded, so that a device may show multiple plex modes supported. The
value zero shall mean notSpecified. The following XcmPrtPlex values and
meanings are defined: 0x001 simplex, one-sided 0X002 simplex, two-sided 0x010
long-edge-bind, one-sided 0x020 long-edge-bind, two-sided 0x040 short-edge-
bind, one-sided 0x080 short-edge-bind, two-sided The following describes the
relationship of the xcmPrtPlex modes to DPA, PostScript and PCL. DPA: In DPA,
Plex specifies whether the page images of the output document are to be
conditioned for (eventual) one-sided or two-sided printing, and also specifies
whether the relative orientation between consecutive page-images is to be
altered. In DPA, the Plex modes specified are named 'Simplex', 'Duplex' and
'Tumble'. However, 'Duplex' would more accurately be named bindLongEdge, and
'Tumble' would more accurately be named bindShortEdge. As written in DPA,
'Whether the images are portrait or landscape, the binding edge is parallel to:
the y axis for 'duplex', and the x axis for 'tumble'. This last observation is
important for understanding when to use 'tumble'. If the binding edge of the
document is along the y-axis, the plex is 'duplex', whether the orientation is
portrait or landscape, and if the binding-edge is along the x-axis, the plex is
'tumble', whether the orientation is portrait or landscape. In DPA, a separate
attribute, 'Sides', specifies 1-sided or 2-sided printing. In DPA, the value of
this attribute may also be used by the presentation processes of some document
formats to determine whether or not to print certain designated pages (e.g. the
extra blank pages needed in two-sided printing to cause sections to begin on
the righthand side of a book, or recto page). The following enumerations are
relevant to DPA: simplexOneSided, simplexTwoSided, bindLongEdgeOneSided,
bindLongEdgeTwoSided, bindShortEdgeOneSided, bindShortEdgeTwoSided. PostScript:
In PostScript, the keys 'duplex' and 'tumble' are booleans which specify
relative orientation between consecutive pages, and to the number of sides
printed. If 'Duplex' is False, pages are printed 1-sided, i.e. 'simplex'. If
'Duplex' is True, pages are printed 2-sided. (For most PostScript interpreters,
only when 'Duplex' is set to True) 'Tumble' specifies how the page images on
opposite sides of a sheet are oriented with respect to each other. If 'Tumble'
is False, the default user spaces of the two pages are oriented such that the
highest value of y in the two spaces lie along the same edge of the media.
Informally, a Tumble value of False produces output suitable for binding on the
left or right. When the default user space is set to a portrait 'pagesize',
setting Tumble to false is the same as using the XcmPrtPlex attribute
longEdgeBind. When the default user space is set to a landscape 'pagesize',
setting Tumble to false is the same as using the XcmPrtPlex attribute
shortEdgeBind. If 'Tumble' is True, the default user spaces of the two pages
are oriented such that the highest value of y in the two spaces lie along
opposite edges of the media. Informally, a Tumble value of True produces output
suitable for binding on the top or bottom. When the default user space is set
to a landscape 'pagesize', setting Tumble to true is the same as using the
XcmPrtPlex attribute shortEdgeBind. When the default user space is set to a
landscape 'pagesize', setting Tumble to true is the same as using the
XcmPrtPlex attribute longEdgeBind. The following XcmPrtPlex enumerations are
relevant to PostScript: bindLongEdgeOneSided, bindLongEdgeTwoSided,
bindShortEdgeOneSided, bindShortEdgeTwoSided. Typically (ie, for a Portrait
default user space): OneSided maps to the duplex boolean set to false TwoSided
maps to the duplex boolean set to true bindEdgeLong maps to the tumble boolean
set to false bindEdgeShort maps to the tumble boolean set to true PCL: In PCL,
the attributes simplex, duplex long-edge-binding, and duplex short-edge-
binding, along with content orientation, landscape or portrait, detail the
number of sides to be printed, content orientation, and relative orientation
between consecutive pages. The PCL model matches that of DPA. The following
XcmPrtPlex enumerations are relevant to PCL: simplexOneSided,
bindLongEdgeTwoSided, bindShortEdgeTwoSided.
"""


class XcmPrtPrintQuality(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 These attributes specify the output quality of the printed document. Some
printers have programmatically controlled output quality. This attribute allows
the user to specify the level of output quality desired from printers. The
following standard values are defined: - 'draft' means lowest quality available
on the printer. Uses include increasing the printer's speed and saving toner. -
'normal' means normal or intermediate quality on the printer. - 'high' means
highest quality available on the printer.
"""


class XcmPrtPrintScreen(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 This Textual-Convention enumerates special modes for 80 character screen dumps
onto A4 size paper, which is usually 77 characters wide. This function is
useful when printing the 80 characters per line width of computer displays. The
PrintScreen mode enables characters to be printed as shown on the display when
PrintScreen is executed from the host. When mode850 or mode852 is set, the
following is done: - Symbol set value changed to PC-850 or PC-852. with the
current Symbol set value being stored. - A4 size horizontal printable area
expanded to being 80 characters wide. When the special mode is returned to Off,
the following is done: - Symbol set value returned to the stored SymbolSet
Value. - A4 size horizontal printable area returned to being 77 characters.
"""


class XcmPrtTraySwitch(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 This Textual-Convention enumerates which tray switching declaration mechanism
is used.
"""


class XcmPrtGeneralMonoPrintOpt(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 These attributes specify the printing performance / economy mode setting.
"""


class XcmPrtOutputPunchPosition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = """\
 This Textual Convention enumerates possible punch positions. The punch
positions enumerated are the number of punch positions that can be supported by
the finishing device. punchPos2Hole is used to indicate a two-hole punch
option. punchPos3Hole is used to indicate a three-hole punch option.
punchPos4Hole is used to indicate a four-hole punch option. The current set of
values (which may be extended in the future) is given below: 1 : punchPos2Hole
-- 2**0 2 : punchPos3Hole -- 2**1 4 : punchPos4Hole -- 2**2
"""


class XcmPrtInputTraysConfiguration(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
 This Textual Convention identifies all possible input tray combinations for a
print device.
"""


class XcmPrtFinisherDFAType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of Finisher DFA
modules that could be installed within a print device.
"""


class XcmPrtHighCapacityFeederType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of High Capacity
Feeders that could be installed within a print device.
"""


class XcmPrtHolePunchUnitType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of Hole Punch
Units that could be installed within a print device.
"""


class XcmPrtFaxOutType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of Fax Out Units
that could be installed within a print device.
"""


class XcmPrtPhaserModuleType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of configurations
for a Phaser print device.
"""


class XcmPrtPrintEngineType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of print engine
configurations that could be supported by a print device.
"""


class XcmPrtAsciiJobTicketType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of ASCII Job
Tickets that could be supported by a print device.
"""


class XcmPrtAuthenticationModeType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of Authentication
Modes that could be supported by a print device.
"""


class XcmPrtHoldForAuthenModeType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of Hold for
Authentication Modes that could be supported by a print device.
"""


class XcmPrtAccountingSystemType(TextualConvention, Integer32):
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

    if mibBuilder.loadTexts:
        description = """\
This collection of enumerations indicate the posssible types of Accounting
Systems that could be supported by a print device.
"""


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
if mibBuilder.loadTexts:
    xCmPrtTCAuxSheetContent.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCXcmPrtAuxSheetType_Type = XcmPrtAuxSheetType
_XCmPrtTCXcmPrtAuxSheetType_Object = MibScalar
xCmPrtTCXcmPrtAuxSheetType = _XCmPrtTCXcmPrtAuxSheetType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 2),
    _XCmPrtTCXcmPrtAuxSheetType_Type()
)
xCmPrtTCXcmPrtAuxSheetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCXcmPrtAuxSheetType.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCXcmPrtAuxSheetType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCTCChannelType_Type = XcmPrtChannelType
_XCmPrtTCTCChannelType_Object = MibScalar
xCmPrtTCTCChannelType = _XCmPrtTCTCChannelType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 3),
    _XCmPrtTCTCChannelType_Type()
)
xCmPrtTCTCChannelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCTCChannelType.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCTCChannelType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCGroupSupport_Type = XcmPrtGroupSupport
_XCmPrtTCGroupSupport_Object = MibScalar
xCmPrtTCGroupSupport = _XCmPrtTCGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 4),
    _XCmPrtTCGroupSupport_Type()
)
xCmPrtTCGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCGroupSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCIETFPrintMIBGroupSupport_Type = XcmPrtIETFPrintMIBGroupSupport
_XCmPrtTCIETFPrintMIBGroupSupport_Object = MibScalar
xCmPrtTCIETFPrintMIBGroupSupport = _XCmPrtTCIETFPrintMIBGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 5),
    _XCmPrtTCIETFPrintMIBGroupSupport_Type()
)
xCmPrtTCIETFPrintMIBGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCIETFPrintMIBGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCIETFPrintMIBGroupSupport.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCInterpreterLangFamily_Type = XcmPrtInterpreterLangFamily
_XCmPrtTCInterpreterLangFamily_Object = MibScalar
xCmPrtTCInterpreterLangFamily = _XCmPrtTCInterpreterLangFamily_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 6),
    _XCmPrtTCInterpreterLangFamily_Type()
)
xCmPrtTCInterpreterLangFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCInterpreterLangFamily.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCInterpreterLangFamily.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCMediaTypeErrorPolicy_Type = XcmPrtMediaTypeErrorPolicy
_XCmPrtTCMediaTypeErrorPolicy_Object = MibScalar
xCmPrtTCMediaTypeErrorPolicy = _XCmPrtTCMediaTypeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 7),
    _XCmPrtTCMediaTypeErrorPolicy_Type()
)
xCmPrtTCMediaTypeErrorPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCMediaTypeErrorPolicy.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCMediaTypeErrorPolicy.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCMediumClassType_Type = XcmPrtMediumClassType
_XCmPrtTCMediumClassType_Object = MibScalar
xCmPrtTCMediumClassType = _XCmPrtTCMediumClassType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 8),
    _XCmPrtTCMediumClassType_Type()
)
xCmPrtTCMediumClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCMediumClassType.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCMediumClassType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCMediumSize_Type = XcmPrtMediumSize
_XCmPrtTCMediumSize_Object = MibScalar
xCmPrtTCMediumSize = _XCmPrtTCMediumSize_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 9),
    _XCmPrtTCMediumSize_Type()
)
xCmPrtTCMediumSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCMediumSize.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCMediumSize.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCOutputOffsetStackingType_Type = XcmPrtOutputOffsetStackingType
_XCmPrtTCOutputOffsetStackingType_Object = MibScalar
xCmPrtTCOutputOffsetStackingType = _XCmPrtTCOutputOffsetStackingType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 10),
    _XCmPrtTCOutputOffsetStackingType_Type()
)
xCmPrtTCOutputOffsetStackingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCOutputOffsetStackingType.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCOutputOffsetStackingType.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtOutputStaplePosition_Type = XcmPrtOutputStaplePosition
_XCmPrtOutputStaplePosition_Object = MibScalar
xCmPrtOutputStaplePosition = _XCmPrtOutputStaplePosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 11),
    _XCmPrtOutputStaplePosition_Type()
)
xCmPrtOutputStaplePosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtOutputStaplePosition.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtOutputStaplePosition.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCPageSizeErrorPolicy_Type = XcmPrtPageSizeErrorPolicy
_XCmPrtTCPageSizeErrorPolicy_Object = MibScalar
xCmPrtTCPageSizeErrorPolicy = _XCmPrtTCPageSizeErrorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 12),
    _XCmPrtTCPageSizeErrorPolicy_Type()
)
xCmPrtTCPageSizeErrorPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPageSizeErrorPolicy.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCPageSizeErrorPolicy.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCPCLFontSource_Type = XcmPrtPCLFontSource
_XCmPrtTCPCLFontSource_Object = MibScalar
xCmPrtTCPCLFontSource = _XCmPrtTCPCLFontSource_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 13),
    _XCmPrtTCPCLFontSource_Type()
)
xCmPrtTCPCLFontSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPCLFontSource.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCPCLFontSource.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCPlex_Type = XcmPrtPlex
_XCmPrtTCPlex_Object = MibScalar
xCmPrtTCPlex = _XCmPrtTCPlex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 14),
    _XCmPrtTCPlex_Type()
)
xCmPrtTCPlex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPlex.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCPlex.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCPrintQuality_Type = XcmPrtPrintQuality
_XCmPrtTCPrintQuality_Object = MibScalar
xCmPrtTCPrintQuality = _XCmPrtTCPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 15),
    _XCmPrtTCPrintQuality_Type()
)
xCmPrtTCPrintQuality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPrintQuality.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCPrintQuality.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCPrintScreen_Type = XcmPrtPrintScreen
_XCmPrtTCPrintScreen_Object = MibScalar
xCmPrtTCPrintScreen = _XCmPrtTCPrintScreen_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 16),
    _XCmPrtTCPrintScreen_Type()
)
xCmPrtTCPrintScreen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCPrintScreen.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCPrintScreen.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCTraySwitch_Type = XcmPrtTraySwitch
_XCmPrtTCTraySwitch_Object = MibScalar
xCmPrtTCTraySwitch = _XCmPrtTCTraySwitch_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 17),
    _XCmPrtTCTraySwitch_Type()
)
xCmPrtTCTraySwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCTraySwitch.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCTraySwitch.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtTCGeneralMonoPrintOpt_Type = XcmPrtGeneralMonoPrintOpt
_XCmPrtTCGeneralMonoPrintOpt_Object = MibScalar
xCmPrtTCGeneralMonoPrintOpt = _XCmPrtTCGeneralMonoPrintOpt_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 18),
    _XCmPrtTCGeneralMonoPrintOpt_Type()
)
xCmPrtTCGeneralMonoPrintOpt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtTCGeneralMonoPrintOpt.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtTCGeneralMonoPrintOpt.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtOutputPunchPosition_Type = XcmPrtOutputPunchPosition
_XCmPrtOutputPunchPosition_Object = MibScalar
xCmPrtOutputPunchPosition = _XCmPrtOutputPunchPosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 19),
    _XCmPrtOutputPunchPosition_Type()
)
xCmPrtOutputPunchPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtOutputPunchPosition.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtOutputPunchPosition.setDescription("""\
Dummy - DO NOT USE
""")
_XCmPrtInputTraysConfiguration_Type = XcmPrtInputTraysConfiguration
_XCmPrtInputTraysConfiguration_Object = MibScalar
xCmPrtInputTraysConfiguration = _XCmPrtInputTraysConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 54, 999, 20),
    _XCmPrtInputTraysConfiguration_Type()
)
xCmPrtInputTraysConfiguration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmPrtInputTraysConfiguration.setStatus("current")
if mibBuilder.loadTexts:
    xCmPrtInputTraysConfiguration.setDescription("""\
Dummy - DO NOT USE
""")

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
