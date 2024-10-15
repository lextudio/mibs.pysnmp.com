# SNMP MIB module (CISCO-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:23 2024
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

(ciscoModules,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules")

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

ciscoTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 1)
)
ciscoTextualConventions.setRevisions(
        ("2015-06-09 00:00",
         "2014-07-23 00:00",
         "2012-08-06 00:00",
         "2012-02-01 00:00",
         "2011-11-11 00:00",
         "2011-06-17 00:00",
         "2010-02-24 00:00",
         "2009-06-18 00:00",
         "2009-03-10 00:00",
         "2009-02-26 00:00",
         "2008-04-02 00:00",
         "2007-02-15 00:00",
         "2006-07-06 00:00",
         "2006-04-13 00:00",
         "2005-06-24 00:00",
         "2005-06-16 00:00",
         "2004-10-11 00:00",
         "2004-06-08 00:00",
         "2004-04-14 00:00",
         "2002-12-18 00:00",
         "2002-12-12 16:00",
         "2002-12-02 00:00",
         "2002-09-22 00:00",
         "2002-09-17 00:00",
         "2002-04-16 00:00",
         "2001-07-07 00:00",
         "2001-01-18 00:00",
         "2000-11-21 00:00",
         "1998-10-28 00:00",
         "1997-03-13 00:00",
         "1996-08-14 00:00",
         "1996-07-08 00:00",
         "1996-02-22 00:00",
         "1995-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Layer2Cos(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class CiscoNetworkProtocol(Integer32, TextualConvention):
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
              65535)
        )
    )
    namedValues = NamedValues(
        *(("apollo", 12),
          ("appletalk", 7),
          ("atmIlmi", 17),
          ("bpxIgx", 23),
          ("bstun", 18),
          ("cdm", 21),
          ("chaos", 4),
          ("clns", 8),
          ("clnsPfx", 24),
          ("cons", 11),
          ("decnet", 2),
          ("http", 25),
          ("ip", 1),
          ("ipv6", 20),
          ("lat", 9),
          ("nbf", 22),
          ("novell", 14),
          ("pup", 3),
          ("qllc", 15),
          ("snapshot", 16),
          ("stun", 13),
          ("unknown", 65535),
          ("vines", 10),
          ("x121", 6),
          ("x25pvc", 19),
          ("xns", 5))
    )



class CiscoNetworkAddress(OctetString, TextualConvention):
    status = "current"


class Unsigned64(Counter64, TextualConvention):
    status = "current"


class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SAPType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )



class CountryCode(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )



class CountryCodeITU(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EntPhysicalIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CiscoRowOperStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("activeDependencies", 2),
          ("inactiveDependency", 3),
          ("missingDependency", 4))
    )



class CiscoPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CiscoIpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CiscoLocationClass(Integer32, TextualConvention):
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
        *(("channel", 7),
          ("chassis", 1),
          ("port", 5),
          ("shelf", 2),
          ("slot", 3),
          ("subChannel", 8),
          ("subPort", 6),
          ("subSlot", 4))
    )



class CiscoLocationSpecifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CiscoInetAddressMask(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class CiscoAbsZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class CiscoSnapShotAbsCounter32(Unsigned32, TextualConvention):
    status = "current"


class CiscoAlarmSeverity(Integer32, TextualConvention):
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("info", 7),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class PerfHighIntervalCount(Counter64, TextualConvention):
    status = "current"


class ConfigIterator(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BulkConfigResult(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ListIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ListIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TimeIntervalSec(Unsigned32, TextualConvention):
    status = "current"


class TimeIntervalMin(Unsigned32, TextualConvention):
    status = "current"


class CiscoMilliSeconds(Unsigned32, TextualConvention):
    status = "current"


class MicroSeconds(Unsigned32, TextualConvention):
    status = "current"


class CiscoPortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class CiscoPortListRange(Integer32, TextualConvention):
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
        *(("eightKto10K", 5),
          ("fourKto6K", 3),
          ("fourteenKto16K", 8),
          ("oneto2k", 1),
          ("sixKto8K", 4),
          ("tenKto12K", 6),
          ("twelveKto14K", 7),
          ("twoKto4K", 2))
    )



class IfOperStatusReason(Integer32, TextualConvention):
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
              69,
              70,
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
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
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
              178,
              179,
              180,
              181,
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
              207,
              208,
              209,
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
              227,
              228,
              229,
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
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
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
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              310,
              311,
              312,
              313)
        )
    )
    namedValues = NamedValues(
        *(("acessPortOnBd", 294),
          ("aclQosNoResource", 304),
          ("adminDown", 12),
          ("adminStateConfigChange", 276),
          ("authzPending", 147),
          ("badFramesRcvdFromLink", 286),
          ("bitErrRuntimeThreshExceeded", 79),
          ("bundleMisCfg", 78),
          ("bundleStandby", 124),
          ("cdpInfoUnavailable", 201),
          ("cellularModemUnattached", 263),
          ("channelAdminDown", 13),
          ("channelConfigurationInProgress", 15),
          ("channelErrDisabled", 157),
          ("channelOperSuspended", 14),
          ("corePortMct", 256),
          ("dcxCompatMismatch", 180),
          ("dcxHundredPdusRcvdNoAck", 223),
          ("dcxMultipleMsapIds", 222),
          ("deniedDueToPortBinding", 66),
          ("domainAddrAssignFailureIsolation", 20),
          ("domainIdConfigMismatch", 236),
          ("domainIdsInvalid", 267),
          ("domainInvalidRcfReceived", 22),
          ("domainManagerDisabled", 23),
          ("domainMaxReTxFailure", 36),
          ("domainNotAllowedIsolated", 120),
          ("domainOther", 131),
          ("domainOtherSideEportIsolation", 21),
          ("domainOverlapIsolation", 19),
          ("dot1qMisConfig", 310),
          ("dot1xSecViolationErrDisabled", 165),
          ("dpvmVsanNotFound", 114),
          ("dpvmVsanSuspended", 113),
          ("dupTunnelConfigDetected", 160),
          ("ePortProhibited", 106),
          ("ecSuspendedOnLoop", 116),
          ("edpError", 302),
          ("elpFailureAllZeroPeerWWNRcvd", 132),
          ("elpFailureClassFParamErr", 68),
          ("elpFailureClassNParamErr", 69),
          ("elpFailureInvalidFlowCtlParam", 71),
          ("elpFailureInvalidPayloadSize", 77),
          ("elpFailureInvalidPortName", 72),
          ("elpFailureInvalidSwitchName", 73),
          ("elpFailureInvalidTxBbCredit", 76),
          ("elpFailureIsolation", 17),
          ("elpFailureLoopbackDetected", 75),
          ("elpFailureRatovEdtovMismatch", 74),
          ("elpFailureRevMismatch", 67),
          ("elpFailureUnknownFlowCtlCode", 70),
          ("emptyEchoUDLD", 166),
          ("enmLoopDetected", 225),
          ("enmPinFailLinkDown", 252),
          ("enmSatIncompatibleUplink", 224),
          ("eppFailure", 37),
          ("errDisableHandShkFailure", 163),
          ("errDisabledBPDUGuard", 164),
          ("errDisabledIpConflict", 203),
          ("errDisabledLacpMiscfg", 183),
          ("errorDisabled", 5),
          ("errorDisabledReInitLmtReached", 126),
          ("escFailureIsolation", 18),
          ("ethIntfInvalidBinding", 245),
          ("ethIntfNotLicensed", 266),
          ("ethL2VlanDown", 244),
          ("externallyDisabled", 138),
          ("fabricBindingDbMismatch", 111),
          ("fabricBindingDomainInvalid", 110),
          ("fabricBindingNoRspFromPeer", 112),
          ("fabricBindingSwitchWwnNotFound", 109),
          ("fabricNameInvalid", 268),
          ("fcRedirectIsolation", 134),
          ("fcidAllocationFailed", 137),
          ("fcipPortAdminCfgChange", 54),
          ("fcipPortKeepAliveTimerExpire", 50),
          ("fcipPortMaxReTx", 49),
          ("fcipPortPersistTimerExpire", 51),
          ("fcipPortSrcAdminDown", 53),
          ("fcipPortSrcLinkDown", 52),
          ("fcipSrcModuleNotOnline", 56),
          ("fcipSrcPortRemoved", 55),
          ("fcotChecksumError", 99),
          ("fcotClkRateMismatch", 204),
          ("fcotNotPresent", 29),
          ("fcotValidationFailedAtDriver", 273),
          ("fcotVendorNotSupported", 30),
          ("fcspAuthenfailure", 98),
          ("fexSfpInvalid", 202),
          ("ficonBeingEnabled", 105),
          ("ficonDupPortNum", 127),
          ("ficonInorderNotActive", 258),
          ("ficonInvalidPortNum", 270),
          ("ficonNoPortNumber", 104),
          ("ficonNoPortSwapLogicalPort", 269),
          ("ficonNotEnabled", 103),
          ("ficonVsanDown", 61),
          ("firstPortNotUp", 46),
          ("firstPortUpAsEport", 45),
          ("flowControlMismatch", 249),
          ("fortyGMemberPort", 300),
          ("fpcMinLinkNotMet", 291),
          ("goldLoopBackTest", 301),
          ("hotStdbyInBundle", 148),
          ("hwFailure", 3),
          ("hwProgrammingFailed", 151),
          ("ifSifLimitExceeded", 177),
          ("inactiveM1PortFpathActiveVlan", 253),
          ("incomAdminRxBbCreditPerBuf", 64),
          ("incompatibleAdminMode", 31),
          ("incompatibleAdminRxBbCredit", 41),
          ("incompatibleAdminRxBufferSize", 42),
          ("incompatibleAdminSpeed", 32),
          ("incompleteConfig", 149),
          ("incompleteTunnelCfg", 150),
          ("initializing", 10),
          ("interfaceRemoved", 28),
          ("invalidAttachment", 62),
          ("invalidConfig", 57),
          ("invalidEncapsulation", 259),
          ("invalidFabricBindExchange", 101),
          ("invalidOtherSidePrincEFPReqRecd", 130),
          ("invalidSatFabricIf", 185),
          ("ipQosDcbxpCompatFailure", 234),
          ("ipQosMgrPolicyAppFailure", 217),
          ("ipSecHndshkInProgress", 261),
          ("isolateBundleLimitExceeded", 181),
          ("isolateBundleMisCfg", 117),
          ("l3NotReady", 247),
          ("lacpMisConfig", 295),
          ("linkFailBbCreditLoss", 93),
          ("linkFailCreditLoss", 89),
          ("linkFailDebounceTimeout", 87),
          ("linkFailLineCardPortShutdown", 97),
          ("linkFailLinkReset", 80),
          ("linkFailLipF8Rcvd", 96),
          ("linkFailLipRcvdBb", 92),
          ("linkFailLossOfSignal", 83),
          ("linkFailLossOfSync", 84),
          ("linkFailLrRcvd", 88),
          ("linkFailNosRcvd", 85),
          ("linkFailOLSRcvd", 86),
          ("linkFailOpenPrimSignalReturned", 95),
          ("linkFailOpenPrimSignalTimeout", 94),
          ("linkFailPortInitFail", 81),
          ("linkFailPortUnusable", 82),
          ("linkFailRxQOverflow", 90),
          ("linkFailTooManyInterrupts", 91),
          ("linkFailure", 7),
          ("localRcf", 128),
          ("loopbackDiagFailure", 4),
          ("loopbackIsolation", 39),
          ("lstGrpUplinkDown", 219),
          ("mdMisMatch", 311),
          ("misCabling", 292),
          ("modemLineDeasserted", 260),
          ("moduleOffline", 191),
          ("moduleRemoved", 255),
          ("neighborMismatchUDLD", 146),
          ("noCommonVsanIsolation", 60),
          ("noFcoe", 179),
          ("noPeerBundleSupport", 118),
          ("noRemoteChassis", 186),
          ("nonCiscoHbaVfTag", 235),
          ("nonCorePortMct", 257),
          ("nonExistentVlan", 230),
          ("nonParticipating", 9),
          ("nonStickyExternallyDisabled", 226),
          ("none", 2),
          ("notAvailable", 313),
          ("notPcMember", 306),
          ("npivNotEnabledInUpstream", 210),
          ("offline", 8),
          ("ohmsExtLoopbackTest", 100),
          ("other", 1),
          ("outOfGlblRxBuffers", 264),
          ("outOfService", 122),
          ("parentDown", 26),
          ("parentPortDown", 254),
          ("pauseRateLimitErrDisabled", 218),
          ("peerFCIPPortClosedConnection", 47),
          ("peerFCIPPortResetConnection", 48),
          ("phyIntfDown", 176),
          ("physicalPortHotStandBy", 287),
          ("pmonFailure", 246),
          ("portActLicenseNotAvailable", 135),
          ("portAuthFailed", 123),
          ("portBindFailure", 58),
          ("portBlocked", 63),
          ("portBringupIsolation", 119),
          ("portCapabilitiesUnknown", 156),
          ("portChannelMembersDown", 43),
          ("portConnectorTypeErr", 125),
          ("portDisabled", 168),
          ("portFabricBindFailure", 59),
          ("portGracefulShutdown", 107),
          ("portGuardBitErrRate", 212),
          ("portGuardCreditLoss", 216),
          ("portGuardLinkReset", 215),
          ("portGuardSigLoss", 213),
          ("portGuardSyncLoss", 214),
          ("portGuardTrustSecViolation", 205),
          ("portVsanMismatchIsolation", 38),
          ("pppAuthFailed", 284),
          ("pppPeerNotResponding", 283),
          ("preferredPathIsolation", 133),
          ("primaryVLANDown", 161),
          ("profileNotFound", 229),
          ("protoPortSuspend", 199),
          ("pvlanNativeVlanErr", 243),
          ("rbhModulo", 290),
          ("rcfInProgress", 16),
          ("rcvSrpOnNonFcoeFex", 293),
          ("remotePortInL2vpnDown", 271),
          ("routerMacFailure", 221),
          ("satFabricIfDown", 184),
          ("satIncompatTopo", 207),
          ("satNotConfigured", 209),
          ("sdmIsolation", 136),
          ("sdpTimeout", 206),
          ("setPortStateFailed", 194),
          ("sfpAbsent", 155),
          ("sfpEthCompliantErr", 262),
          ("sfpFcCompliantErr", 265),
          ("sfpInvalid", 154),
          ("sfpReadError", 141),
          ("sfpSpeedMismatch", 237),
          ("sifAdminDown", 175),
          ("sifHoldDown", 178),
          ("sifNotBound", 182),
          ("speedGroupConfigMisMatch", 308),
          ("speedMismatch", 248),
          ("srcPortNotBound", 27),
          ("stickyDnLinkFailure", 220),
          ("stickyDownOnLinkFailure", 142),
          ("stpInconsVpcPeerDisabled", 193),
          ("stpNotFwdingInFcoeMappedVlan", 190),
          ("subGroupIdNotAssigned", 227),
          ("suspendByMtu", 153),
          ("suspendedByMode", 33),
          ("suspendedBySpeed", 34),
          ("suspendedByVpc", 195),
          ("suspendedByWWN", 35),
          ("suspendedDueToMinLinks", 251),
          ("suspendedDueToNoLacpPdus", 272),
          ("swFailure", 6),
          ("systemIntfShut", 307),
          ("tooManyInvalidFlogis", 65),
          ("tooManyLinkFlapsErr", 143),
          ("tovMismatch", 102),
          ("trackedPortDown", 115),
          ("trunkNotFullyActive", 108),
          ("tunnelDstNotConfigured", 171),
          ("tunnelDstUnreachable", 152),
          ("tunnelModeNotConfigured", 169),
          ("tunnelSrcDown", 200),
          ("tunnelSrcNotConfigured", 170),
          ("tunnelUnableToResolveDstIP", 173),
          ("tunnelUnableToResolveSrcIP", 172),
          ("tunnelVrfDown", 174),
          ("twoSwitchesWithSameWWN", 129),
          ("txRxLoopUDLD", 145),
          ("udldAggModeLinkFailure", 192),
          ("unavailableNPVPrefUpstreamPort", 140),
          ("unavailableNPVUpstreamPort", 139),
          ("unidirectionalUDLD", 144),
          ("unsupportedTransceiver", 275),
          ("unsupportedTransceiverMd5DigestNotSame", 274),
          ("upgradeInProgress", 40),
          ("vdcMode", 250),
          ("vemUnlicensed", 228),
          ("vfTaggingCapErr", 167),
          ("vfcBindingInvalid", 241),
          ("vicDisableReceived", 188),
          ("vicEnableNotReceived", 187),
          ("virtualIvrDomainOverlapIsolation", 121),
          ("vlanAllowedList", 277),
          ("vlanAllowedListAdd", 279),
          ("vlanAllowedListOverride", 278),
          ("vlanAllowedRemove", 280),
          ("vlanCfgDelete", 282),
          ("vlanCfgStateChange", 281),
          ("vlanDown", 232),
          ("vlanInvalidType", 231),
          ("vlanNotFcoeEnabled", 242),
          ("vlanVsanMappingNotEnabled", 189),
          ("vpcCfgInProgress", 196),
          ("vpcCompCheckFailed", 303),
          ("vpcNoRspFromPeer", 198),
          ("vpcPeerLinkDown", 197),
          ("vpcPeerLinkShut", 312),
          ("vpcPeerUpgrade", 233),
          ("vpcShutdown", 305),
          ("vrfForwardReferencing", 159),
          ("vrfMismatch", 158),
          ("vrfUnusable", 162),
          ("vsanInactive", 11),
          ("vsanMismatchIsolation", 25),
          ("vsanMismatchWithUpstreamSwPort", 211),
          ("waitForFlogi", 208),
          ("wimaxModemUnattached", 288),
          ("wpanModemUnattached", 289),
          ("xcvrAbsent", 239),
          ("xcvrAuthFailed", 285),
          ("xcvrInitializing", 238),
          ("xcvrInvalid", 240),
          ("zoneMergeFailureIsolation", 24),
          ("zoneRemoteNoRespIsolation", 44))
    )



class EntLogicalIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CiscoURLString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class CiscoURLStringOrEmpty(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CiscoHTTPResponseStatusCode(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 599),
    )



class CvE164Address(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class CiscoVlanList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CiscoCosList(Bits, TextualConvention):
    status = "current"


class CiscoPbbServiceIdentifier(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777216),
    )



class CiscoBridgeDomain(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Cisco2KVlanList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class CiscoInterfaceIndexList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class CiscoVrfName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CiscoEntityIndexList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class CiscoVlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class CiscoAbsZeroBasedCounter64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TC",
    **{"Layer2Cos": Layer2Cos,
       "CiscoNetworkProtocol": CiscoNetworkProtocol,
       "CiscoNetworkAddress": CiscoNetworkAddress,
       "Unsigned64": Unsigned64,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "CountryCodeITU": CountryCodeITU,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "CiscoRowOperStatus": CiscoRowOperStatus,
       "CiscoPort": CiscoPort,
       "CiscoIpProtocol": CiscoIpProtocol,
       "CiscoLocationClass": CiscoLocationClass,
       "CiscoLocationSpecifier": CiscoLocationSpecifier,
       "CiscoInetAddressMask": CiscoInetAddressMask,
       "CiscoAbsZeroBasedCounter32": CiscoAbsZeroBasedCounter32,
       "CiscoSnapShotAbsCounter32": CiscoSnapShotAbsCounter32,
       "CiscoAlarmSeverity": CiscoAlarmSeverity,
       "PerfHighIntervalCount": PerfHighIntervalCount,
       "ConfigIterator": ConfigIterator,
       "BulkConfigResult": BulkConfigResult,
       "ListIndex": ListIndex,
       "ListIndexOrZero": ListIndexOrZero,
       "TimeIntervalSec": TimeIntervalSec,
       "TimeIntervalMin": TimeIntervalMin,
       "CiscoMilliSeconds": CiscoMilliSeconds,
       "MicroSeconds": MicroSeconds,
       "CiscoPortList": CiscoPortList,
       "CiscoPortListRange": CiscoPortListRange,
       "IfOperStatusReason": IfOperStatusReason,
       "EntLogicalIndexOrZero": EntLogicalIndexOrZero,
       "CiscoURLString": CiscoURLString,
       "CiscoURLStringOrEmpty": CiscoURLStringOrEmpty,
       "CiscoHTTPResponseStatusCode": CiscoHTTPResponseStatusCode,
       "CvE164Address": CvE164Address,
       "CiscoVlanList": CiscoVlanList,
       "CiscoCosList": CiscoCosList,
       "CiscoPbbServiceIdentifier": CiscoPbbServiceIdentifier,
       "CiscoBridgeDomain": CiscoBridgeDomain,
       "Cisco2KVlanList": Cisco2KVlanList,
       "CiscoInterfaceIndexList": CiscoInterfaceIndexList,
       "CiscoVrfName": CiscoVrfName,
       "CiscoEntityIndexList": CiscoEntityIndexList,
       "CiscoVlanIndex": CiscoVlanIndex,
       "CiscoAbsZeroBasedCounter64": CiscoAbsZeroBasedCounter64,
       "ciscoTextualConventions": ciscoTextualConventions}
)
