"""SNMP MIB module (XEROX-COMMS-ENGINE-TC) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-COMMS-ENGINE-TC
Produced by pysmi-1.3.3 at Sun Mar 10 06:00:23 2024
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
 IpAddress,
 Counter64,
 ObjectIdentity,
 TimeTicks,
 Integer32,
 iso,
 MibIdentifier,
 NotificationType,
 Gauge32,
 ModuleIdentity,
 Unsigned32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Bits) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "IpAddress",
    "Counter64",
    "ObjectIdentity",
    "TimeTicks",
    "Integer32",
    "iso",
    "MibIdentifier",
    "NotificationType",
    "Gauge32",
    "ModuleIdentity",
    "Unsigned32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Bits")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmCommsEngineTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmCommsMgmtCommandRequest(TextualConvention, Integer32):
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
              1701,
              1702,
              1703,
              1704,
              1705,
              1706,
              1707,
              1708,
              1709,
              1710,
              2701,
              2702,
              2721,
              2722,
              2723,
              2724,
              2725,
              2726,
              2731,
              2732,
              2733,
              2734,
              2741,
              2742)
        )
    )
    namedValues = NamedValues(
        *(("close", 5),
          ("commsBackup", 2723),
          ("commsClean", 1705),
          ("commsConfigure", 2725),
          ("commsCreate", 1701),
          ("commsDelete", 1702),
          ("commsDiagnose", 2726),
          ("commsDisable", 1706),
          ("commsEnable", 1707),
          ("commsInstall", 2721),
          ("commsList", 1703),
          ("commsLogin", 2741),
          ("commsLogout", 2742),
          ("commsManage", 2701),
          ("commsPause", 1708),
          ("commsResetCold", 2733),
          ("commsResetCounters", 2731),
          ("commsResetFactory", 2734),
          ("commsResetWarm", 2732),
          ("commsRestart", 2702),
          ("commsRestore", 2724),
          ("commsResume", 1709),
          ("commsSet", 1704),
          ("commsShutdown", 1710),
          ("commsUpgrade", 2722),
          ("disable", 2),
          ("enable", 4),
          ("flushInOut", 15),
          ("flushInput", 13),
          ("flushOutput", 14),
          ("manage", 16),
          ("none", 1),
          ("open", 7),
          ("quiesce", 8),
          ("recover", 6),
          ("resetCold", 11),
          ("resetCounters", 9),
          ("resetFactory", 12),
          ("resetWarm", 10),
          ("test", 3))
    )



class XcmCommsMgmtCommandData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class XcmCommsMgmtState(TextualConvention, Integer32):
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
        *(("closed", 5),
          ("closing", 6),
          ("inoperative", 3),
          ("opened", 9),
          ("opening", 7),
          ("other", 1),
          ("recovering", 8),
          ("testing", 4),
          ("unknown", 2))
    )



class XcmCommsMgmtConditions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmCommsStackPosition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              8,
              9,
              10,
              12,
              16,
              17,
              18,
              20,
              25,
              26,
              28)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 1),
          ("bottomAndTop", 5),
          ("bottomBothMux", 25),
          ("bottomLowerMux", 9),
          ("bottomUpperMux", 17),
          ("lowerMux", 8),
          ("middle", 2),
          ("middleBothMux", 26),
          ("middleLowerMux", 10),
          ("middleUpperMux", 18),
          ("top", 4),
          ("topBothMux", 28),
          ("topLowerMux", 12),
          ("topUpperMux", 20),
          ("upperMux", 16))
    )



class XcmCommsStackExtPurpose(TextualConvention, Integer32):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("layerDataTransfer", 12),
          ("layerInterWorkingUnit", 15),
          ("layerManagement", 13),
          ("layerOther", 11),
          ("layerSecurity", 14),
          ("other", 1),
          ("systemDataTransfer", 17),
          ("systemInterWorkingUnit", 20),
          ("systemManagement", 18),
          ("systemOther", 16),
          ("systemSecurity", 19),
          ("unknown", 2))
    )



class XcmCommsStackExtRole(TextualConvention, Integer32):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("client", 15),
          ("multicaster", 14),
          ("other", 1),
          ("peer", 11),
          ("primary", 12),
          ("secondary", 13),
          ("server", 16),
          ("unknown", 2))
    )



class XcmCommsStackExtSuite(TextualConvention, Integer32):
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 18),
          ("decnet", 17),
          ("directPrint", 29),
          ("ibmbisync", 16),
          ("ibmsna", 15),
          ("internet", 14),
          ("lanmanager", 23),
          ("lanserver", 22),
          ("lantastic", 21),
          ("netbeui", 26),
          ("netbios", 25),
          ("netware", 19),
          ("ntas", 24),
          ("osilan", 11),
          ("osiman", 12),
          ("osiwan", 13),
          ("other", 1),
          ("parallel", 28),
          ("serial", 27),
          ("unknown", 2),
          ("usb", 30),
          ("vines", 20))
    )



class XcmCommsStackExtSuiteVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              110101,
              120101,
              130101,
              140101,
              150101,
              160101,
              170101,
              180101,
              181999,
              182999,
              190101,
              192999,
              193999,
              194999,
              200101,
              210101,
              220101,
              230101,
              240101,
              250101,
              260101,
              270101,
              280101,
              290101,
              300101)
        )
    )
    namedValues = NamedValues(
        *(("appletalkPhase1", 181999),
          ("appletalkPhase2", 182999),
          ("appletalkVersions", 180101),
          ("decnetVersions", 170101),
          ("directPrintVersions", 290101),
          ("ibmbisyncVersions", 160101),
          ("ibmsnaVersions", 150101),
          ("internetVersions", 140101),
          ("lanmanagerVersions", 230101),
          ("lanserverVersions", 220101),
          ("lantasticVersions", 210101),
          ("netbeuiVersions", 260101),
          ("netbiosVersions", 250101),
          ("netware2x", 192999),
          ("netware3x", 193999),
          ("netware4x", 194999),
          ("netwareVersions", 190101),
          ("ntasVersions", 240101),
          ("osilanVersions", 110101),
          ("osimanVersions", 120101),
          ("osiwanVersions", 130101),
          ("other", 1),
          ("parallelVersions", 280101),
          ("serialVersions", 270101),
          ("unknown", 2),
          ("usbVersions", 300101),
          ("vinesVersions", 200101))
    )



class XcmCommsStackExtLayer(TextualConvention, Integer32):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("application", 17),
          ("datalink", 12),
          ("network", 13),
          ("other", 1),
          ("physical", 11),
          ("presentation", 16),
          ("session", 15),
          ("transport", 14),
          ("unknown", 2))
    )



class XcmCommsStackExtProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              110101,
              111103,
              111104,
              111105,
              111107,
              111108,
              111113,
              111114,
              111115,
              111117,
              111118,
              111203,
              111204,
              111205,
              111207,
              111208,
              111215,
              111217,
              111218,
              111221,
              111222,
              111232,
              111234,
              111241,
              120101,
              121106,
              121116,
              121206,
              121216,
              130101,
              131201,
              131202,
              131203,
              131211,
              131212,
              131213,
              131221,
              131224,
              131241,
              131251,
              131261,
              131301,
              131302,
              131303,
              131304,
              131401,
              131402,
              131501,
              131502,
              131601,
              131602,
              131701,
              131702,
              131703,
              131704,
              131713,
              131714,
              131716,
              131740,
              131750,
              131751,
              131752,
              131770,
              131771,
              131780,
              140101,
              141201,
              141202,
              141301,
              141302,
              141303,
              141304,
              141305,
              141306,
              141310,
              141401,
              141402,
              141404,
              141405,
              141406,
              141501,
              141502,
              141503,
              141504,
              141505,
              141506,
              141507,
              141508,
              141509,
              141510,
              141511,
              141512,
              141513,
              141514,
              141515,
              141516,
              141519,
              141520,
              141521,
              141522,
              141523,
              141524,
              141525,
              141530,
              141531,
              141532,
              141533,
              141540,
              141551,
              141552,
              141561,
              141570,
              141571,
              141572,
              141591,
              141592,
              141593,
              150101,
              151201,
              151211,
              151221,
              151301,
              151401,
              151501,
              151502,
              151503,
              151504,
              151601,
              151602,
              151603,
              151604,
              151605,
              160101,
              161201,
              161601,
              161602,
              161603,
              161604,
              170101,
              180101,
              181201,
              181202,
              181203,
              181301,
              181303,
              181401,
              181402,
              181403,
              181404,
              181501,
              181502,
              181503,
              181507,
              181510,
              181511,
              181512,
              181513,
              181601,
              190101,
              191301,
              191402,
              191403,
              191404,
              191501,
              191502,
              191503,
              191504,
              191505,
              191507,
              191508,
              191509,
              191510,
              191511,
              191512,
              191513,
              191591,
              200101,
              201301,
              201302,
              201303,
              201311,
              201312,
              201313,
              201314,
              201401,
              201402,
              201411,
              201412,
              201501,
              201502,
              201503,
              201701,
              201702,
              201703,
              201704,
              210101,
              220101,
              230101,
              240101,
              250101,
              251501,
              251510,
              251511,
              251512,
              251513,
              251520,
              251521,
              251522,
              251591,
              251701,
              251702,
              251703,
              251704,
              251705,
              260101,
              261201,
              261221,
              261231,
              270101,
              280101,
              290101,
              300101)
        )
    )
    namedValues = NamedValues(
        *(("appletalkAARP", 181303),
          ("appletalkADSP", 181402),
          ("appletalkAEP", 181404),
          ("appletalkAFP", 181601),
          ("appletalkASP", 181501),
          ("appletalkATP", 181401),
          ("appletalkDDP", 181301),
          ("appletalkELAP", 181202),
          ("appletalkLLAP", 181201),
          ("appletalkNBP", 181507),
          ("appletalkPAP", 181503),
          ("appletalkRTMP", 181403),
          ("appletalkSNMP", 181510),
          ("appletalkSNMPv1", 181511),
          ("appletalkSNMPv2", 181512),
          ("appletalkSNMPv3", 181513),
          ("appletalkSuite", 180101),
          ("appletalkTLAP", 181203),
          ("appletalkZIP", 181502),
          ("decnetSuite", 170101),
          ("directPrintSuite", 290101),
          ("ibmbisync3270PS", 161602),
          ("ibmbisync5250PS", 161603),
          ("ibmbisyncDLC", 161201),
          ("ibmbisyncPS", 161601),
          ("ibmbisyncRJE", 161604),
          ("ibmbisyncSuite", 160101),
          ("ibmsna3270PS", 151602),
          ("ibmsna5250PS", 151603),
          ("ibmsnaAPPC", 151605),
          ("ibmsnaCSC", 151502),
          ("ibmsnaDFC", 151501),
          ("ibmsnaDLC", 151211),
          ("ibmsnaDLS", 151221),
          ("ibmsnaLUNS", 151504),
          ("ibmsnaPC", 151301),
          ("ibmsnaPS", 151601),
          ("ibmsnaPUNS", 151503),
          ("ibmsnaRJE", 151604),
          ("ibmsnaSDLC", 151201),
          ("ibmsnaSuite", 150101),
          ("ibmsnaTC", 151401),
          ("internetARP", 141303),
          ("internetBOOTP", 141305),
          ("internetCLDAP", 141552),
          ("internetDHCP", 141304),
          ("internetDNS", 141507),
          ("internetFTP", 141504),
          ("internetFax", 141516),
          ("internetHTTP", 141509),
          ("internetICMP", 141302),
          ("internetIMAP4", 141515),
          ("internetIP", 141301),
          ("internetIPP", 141502),
          ("internetIPv6", 141310),
          ("internetLDAP", 141551),
          ("internetLPR", 141503),
          ("internetOsfDceCDS", 141531),
          ("internetOsfDceKerberos", 141533),
          ("internetOsfDceRPC", 141532),
          ("internetOsfDceSuite", 141530),
          ("internetOsfDmeSuite", 141540),
          ("internetPOP3", 141514),
          ("internetPPP", 141202),
          ("internetPing", 141404),
          ("internetRARP", 141306),
          ("internetRaw", 141501),
          ("internetSLIP", 141201),
          ("internetSLP", 141591),
          ("internetSLPv1", 141592),
          ("internetSLPv2", 141593),
          ("internetSMTP", 141505),
          ("internetSNMP", 141510),
          ("internetSNMPv1", 141511),
          ("internetSNMPv2", 141512),
          ("internetSNMPv3", 141513),
          ("internetSSL3", 141405),
          ("internetSalutation", 141561),
          ("internetSuite", 140101),
          ("internetSunOncNIS", 141521),
          ("internetSunOncPlusNIS", 141522),
          ("internetSunOncPlusRPC", 141524),
          ("internetSunOncRPC", 141523),
          ("internetSunOncSuite", 141520),
          ("internetSunTiRPC", 141525),
          ("internetTCP", 141402),
          ("internetTFTP", 141508),
          ("internetTLS", 141406),
          ("internetTelnet", 141506),
          ("internetUDP", 141401),
          ("internetUpnpGENA", 141572),
          ("internetUpnpSSDP", 141571),
          ("internetUpnpSuite", 141570),
          ("internetWINS", 141519),
          ("lanmanagerSuite", 230101),
          ("lanserverSuite", 220101),
          ("lantasticSuite", 210101),
          ("netbeuiDLC", 261231),
          ("netbeuiDatalink", 261201),
          ("netbeuiLLC", 261221),
          ("netbeuiSuite", 260101),
          ("netbiosFClient", 251704),
          ("netbiosFServer", 251705),
          ("netbiosIntDistServer", 251522),
          ("netbiosIntEndNode", 251520),
          ("netbiosIntNameServer", 251521),
          ("netbiosNBP", 251501),
          ("netbiosPClient", 251702),
          ("netbiosPServer", 251703),
          ("netbiosSAP", 251591),
          ("netbiosSMB", 251701),
          ("netbiosSNMP", 251510),
          ("netbiosSNMPv1", 251511),
          ("netbiosSNMPv2", 251512),
          ("netbiosSNMPv3", 251513),
          ("netbiosSuite", 250101),
          ("netwareBindery", 191507),
          ("netwareEcho", 191404),
          ("netwareFServer", 191504),
          ("netwareIPX", 191301),
          ("netwareMHS", 191505),
          ("netwareNCP", 191501),
          ("netwareNDS", 191508),
          ("netwareNetbios", 191502),
          ("netwarePServer", 191503),
          ("netwareRIP", 191403),
          ("netwareRPrinter", 191509),
          ("netwareSAP", 191591),
          ("netwareSNMP", 191510),
          ("netwareSNMPv1", 191511),
          ("netwareSNMPv2", 191512),
          ("netwareSNMPv3", 191513),
          ("netwareSPX", 191402),
          ("netwareSuite", 190101),
          ("ntasSuite", 240101),
          ("osilan80210SDE", 111241),
          ("osilan80211MAC", 111208),
          ("osilan80211PHY", 111118),
          ("osilan80211PMD", 111108),
          ("osilan80211SMT", 111218),
          ("osilan8021BLMMP", 111232),
          ("osilan8021DBRG", 111234),
          ("osilan8022LLC", 111221),
          ("osilan8022LLCSNAP", 111222),
          ("osilan8023MAC", 111203),
          ("osilan8023PHY", 111113),
          ("osilan8023PMD", 111103),
          ("osilan8024MAC", 111204),
          ("osilan8024PHY", 111114),
          ("osilan8024PMD", 111104),
          ("osilan8025MAC", 111205),
          ("osilan8025PHY", 111115),
          ("osilan8025PMD", 111105),
          ("osilan8025SMT", 111215),
          ("osilanFDDIMAC", 111207),
          ("osilanFDDIPHY", 111117),
          ("osilanFDDIPMD", 111107),
          ("osilanFDDISMT", 111217),
          ("osilanSuite", 110101),
          ("osiman8026MAC", 121206),
          ("osiman8026PHY", 121116),
          ("osiman8026PMD", 121106),
          ("osiman8026SMT", 121216),
          ("osimanSuite", 120101),
          ("osiwanACSE", 131701),
          ("osiwanCCR", 131704),
          ("osiwanCLNP", 131301),
          ("osiwanCLPP", 131601),
          ("osiwanCLSP", 131501),
          ("osiwanCLTP", 131401),
          ("osiwanCMIP", 131771),
          ("osiwanCONP", 131302),
          ("osiwanCOPP", 131602),
          ("osiwanCOSP", 131502),
          ("osiwanCOTP", 131402),
          ("osiwanDAP", 131751),
          ("osiwanDPA", 131713),
          ("osiwanDS", 131750),
          ("osiwanDSP", 131752),
          ("osiwanESIS", 131303),
          ("osiwanFTAM", 131714),
          ("osiwanFax", 131241),
          ("osiwanHdlcABM", 131201),
          ("osiwanHdlcABME", 131211),
          ("osiwanHdlcARM", 131202),
          ("osiwanHdlcARME", 131212),
          ("osiwanHdlcLAPB", 131221),
          ("osiwanHdlcLAPD", 131224),
          ("osiwanHdlcNRM", 131203),
          ("osiwanHdlcNRME", 131213),
          ("osiwanISDN", 131261),
          ("osiwanISIS", 131304),
          ("osiwanMHS", 131740),
          ("osiwanMgmt", 131770),
          ("osiwanPSTN", 131251),
          ("osiwanROSE", 131703),
          ("osiwanRTSE", 131702),
          ("osiwanSec", 131780),
          ("osiwanSuite", 130101),
          ("osiwanVT", 131716),
          ("other", 1),
          ("parallelSuite", 280101),
          ("serialSuite", 270101),
          ("unknown", 2),
          ("usbSuite", 300101),
          ("vinesARP", 201313),
          ("vinesFiling", 201702),
          ("vinesICMP", 201312),
          ("vinesIP", 201311),
          ("vinesMail", 201703),
          ("vinesNetRPC", 201501),
          ("vinesNetbios", 201503),
          ("vinesPrint", 201701),
          ("vinesSocket", 201502),
          ("vinesStreetTalk", 201704),
          ("vinesSuite", 200101),
          ("vinesTCP", 201412),
          ("vinesUDP", 201411),
          ("vinesVARP", 201303),
          ("vinesVICP", 201302),
          ("vinesVIP", 201301),
          ("vinesVIPC", 201401),
          ("vinesVRTP", 201314),
          ("vinesVSPP", 201402))
    )



class XcmCommsAddressExtForm(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("email", 16),
          ("fax", 14),
          ("fullName", 17),
          ("other", 1),
          ("packet", 15),
          ("postal", 11),
          ("relName", 18),
          ("telex", 13),
          ("unknown", 2),
          ("voice", 12))
    )



class XcmCommsAddressExtScope(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("network", 13),
          ("other", 1),
          ("region", 12),
          ("subnet", 11),
          ("universe", 14),
          ("unknown", 2))
    )



class XcmCommsAddressExtFanout(TextualConvention, Integer32):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 13),
          ("broadcastMask", 17),
          ("multicast", 12),
          ("multicastMask", 16),
          ("other", 1),
          ("unicast", 11),
          ("unicastMask", 15),
          ("universe", 14),
          ("universeMask", 18),
          ("unknown", 2))
    )



class XcmCommsEngineGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_XCmCommsEngineDummy_ObjectIdentity = ObjectIdentity
xCmCommsEngineDummy = _XCmCommsEngineDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999)
)
_XCmCommsMgmtCommandRequest_Type = XcmCommsMgmtCommandRequest
_XCmCommsMgmtCommandRequest_Object = MibScalar
xCmCommsMgmtCommandRequest = _XCmCommsMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 1),
    _XCmCommsMgmtCommandRequest_Type()
)
xCmCommsMgmtCommandRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsMgmtCommandRequest.setStatus("current")
_XCmCommsMgmtCommandData_Type = XcmCommsMgmtCommandData
_XCmCommsMgmtCommandData_Object = MibScalar
xCmCommsMgmtCommandData = _XCmCommsMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 2),
    _XCmCommsMgmtCommandData_Type()
)
xCmCommsMgmtCommandData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsMgmtCommandData.setStatus("current")
_XCmCommsMgmtState_Type = XcmCommsMgmtState
_XCmCommsMgmtState_Object = MibScalar
xCmCommsMgmtState = _XCmCommsMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 3),
    _XCmCommsMgmtState_Type()
)
xCmCommsMgmtState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsMgmtState.setStatus("current")
_XCmCommsMgmtConditions_Type = XcmCommsMgmtConditions
_XCmCommsMgmtConditions_Object = MibScalar
xCmCommsMgmtConditions = _XCmCommsMgmtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 4),
    _XCmCommsMgmtConditions_Type()
)
xCmCommsMgmtConditions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsMgmtConditions.setStatus("current")
_XCmCommsStackPosition_Type = XcmCommsStackPosition
_XCmCommsStackPosition_Object = MibScalar
xCmCommsStackPosition = _XCmCommsStackPosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 5),
    _XCmCommsStackPosition_Type()
)
xCmCommsStackPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackPosition.setStatus("current")
_XCmCommsStackExtPurpose_Type = XcmCommsStackExtPurpose
_XCmCommsStackExtPurpose_Object = MibScalar
xCmCommsStackExtPurpose = _XCmCommsStackExtPurpose_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 6),
    _XCmCommsStackExtPurpose_Type()
)
xCmCommsStackExtPurpose.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackExtPurpose.setStatus("current")
_XCmCommsStackExtRole_Type = XcmCommsStackExtRole
_XCmCommsStackExtRole_Object = MibScalar
xCmCommsStackExtRole = _XCmCommsStackExtRole_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 7),
    _XCmCommsStackExtRole_Type()
)
xCmCommsStackExtRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackExtRole.setStatus("current")
_XCmCommsStackExtSuite_Type = XcmCommsStackExtSuite
_XCmCommsStackExtSuite_Object = MibScalar
xCmCommsStackExtSuite = _XCmCommsStackExtSuite_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 8),
    _XCmCommsStackExtSuite_Type()
)
xCmCommsStackExtSuite.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackExtSuite.setStatus("current")
_XCmCommsStackExtSuiteVersion_Type = XcmCommsStackExtSuiteVersion
_XCmCommsStackExtSuiteVersion_Object = MibScalar
xCmCommsStackExtSuiteVersion = _XCmCommsStackExtSuiteVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 9),
    _XCmCommsStackExtSuiteVersion_Type()
)
xCmCommsStackExtSuiteVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackExtSuiteVersion.setStatus("current")
_XCmCommsStackExtLayer_Type = XcmCommsStackExtLayer
_XCmCommsStackExtLayer_Object = MibScalar
xCmCommsStackExtLayer = _XCmCommsStackExtLayer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 10),
    _XCmCommsStackExtLayer_Type()
)
xCmCommsStackExtLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackExtLayer.setStatus("current")
_XCmCommsStackExtProtocol_Type = XcmCommsStackExtProtocol
_XCmCommsStackExtProtocol_Object = MibScalar
xCmCommsStackExtProtocol = _XCmCommsStackExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 11),
    _XCmCommsStackExtProtocol_Type()
)
xCmCommsStackExtProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsStackExtProtocol.setStatus("current")
_XCmCommsAddressExtForm_Type = XcmCommsAddressExtForm
_XCmCommsAddressExtForm_Object = MibScalar
xCmCommsAddressExtForm = _XCmCommsAddressExtForm_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 12),
    _XCmCommsAddressExtForm_Type()
)
xCmCommsAddressExtForm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsAddressExtForm.setStatus("current")
_XCmCommsAddressExtScope_Type = XcmCommsAddressExtScope
_XCmCommsAddressExtScope_Object = MibScalar
xCmCommsAddressExtScope = _XCmCommsAddressExtScope_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 13),
    _XCmCommsAddressExtScope_Type()
)
xCmCommsAddressExtScope.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsAddressExtScope.setStatus("current")
_XCmCommsAddressExtFanout_Type = XcmCommsAddressExtFanout
_XCmCommsAddressExtFanout_Object = MibScalar
xCmCommsAddressExtFanout = _XCmCommsAddressExtFanout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 14),
    _XCmCommsAddressExtFanout_Type()
)
xCmCommsAddressExtFanout.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsAddressExtFanout.setStatus("current")
_XCmCommsEngineGroupSupport_Type = XcmCommsEngineGroupSupport
_XCmCommsEngineGroupSupport_Object = MibScalar
xCmCommsEngineGroupSupport = _XCmCommsEngineGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 60, 999, 15),
    _XCmCommsEngineGroupSupport_Type()
)
xCmCommsEngineGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmCommsEngineGroupSupport.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-COMMS-ENGINE-TC",
    **{"XcmCommsMgmtCommandRequest": XcmCommsMgmtCommandRequest,
       "XcmCommsMgmtCommandData": XcmCommsMgmtCommandData,
       "XcmCommsMgmtState": XcmCommsMgmtState,
       "XcmCommsMgmtConditions": XcmCommsMgmtConditions,
       "XcmCommsStackPosition": XcmCommsStackPosition,
       "XcmCommsStackExtPurpose": XcmCommsStackExtPurpose,
       "XcmCommsStackExtRole": XcmCommsStackExtRole,
       "XcmCommsStackExtSuite": XcmCommsStackExtSuite,
       "XcmCommsStackExtSuiteVersion": XcmCommsStackExtSuiteVersion,
       "XcmCommsStackExtLayer": XcmCommsStackExtLayer,
       "XcmCommsStackExtProtocol": XcmCommsStackExtProtocol,
       "XcmCommsAddressExtForm": XcmCommsAddressExtForm,
       "XcmCommsAddressExtScope": XcmCommsAddressExtScope,
       "XcmCommsAddressExtFanout": XcmCommsAddressExtFanout,
       "XcmCommsEngineGroupSupport": XcmCommsEngineGroupSupport,
       "xcmCommsEngineTC": xcmCommsEngineTC,
       "xCmCommsEngineDummy": xCmCommsEngineDummy,
       "xCmCommsMgmtCommandRequest": xCmCommsMgmtCommandRequest,
       "xCmCommsMgmtCommandData": xCmCommsMgmtCommandData,
       "xCmCommsMgmtState": xCmCommsMgmtState,
       "xCmCommsMgmtConditions": xCmCommsMgmtConditions,
       "xCmCommsStackPosition": xCmCommsStackPosition,
       "xCmCommsStackExtPurpose": xCmCommsStackExtPurpose,
       "xCmCommsStackExtRole": xCmCommsStackExtRole,
       "xCmCommsStackExtSuite": xCmCommsStackExtSuite,
       "xCmCommsStackExtSuiteVersion": xCmCommsStackExtSuiteVersion,
       "xCmCommsStackExtLayer": xCmCommsStackExtLayer,
       "xCmCommsStackExtProtocol": xCmCommsStackExtProtocol,
       "xCmCommsAddressExtForm": xCmCommsAddressExtForm,
       "xCmCommsAddressExtScope": xCmCommsAddressExtScope,
       "xCmCommsAddressExtFanout": xCmCommsAddressExtFanout,
       "xCmCommsEngineGroupSupport": xCmCommsEngineGroupSupport}
)
