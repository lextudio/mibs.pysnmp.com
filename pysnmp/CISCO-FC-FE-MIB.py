# SNMP MIB module (CISCO-FC-FE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-FE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:13 2024
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

(cieIfOperStatusCause,) = mibBuilder.importSymbols(
    "CISCO-IF-EXTENSION-MIB",
    "cieIfOperStatusCause")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcAddressId,
 FcClassOfServices,
 FcIfServiceStateType,
 FcIfSpeed,
 FcNameId,
 FcPortModuleTypes,
 FcPortTxTypes,
 FcPortTypes) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId",
    "FcClassOfServices",
    "FcIfServiceStateType",
    "FcIfSpeed",
    "FcNameId",
    "FcPortModuleTypes",
    "FcPortTxTypes",
    "FcPortTypes")

(MicroSeconds,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "MicroSeconds")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(FcList,) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcFeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289)
)
ciscoFcFeMIB.setRevisions(
        ("2014-02-06 00:00",
         "2013-04-09 00:00",
         "2012-11-19 00:00",
         "2011-06-15 00:00",
         "2010-08-18 09:00",
         "2010-03-04 09:00",
         "2009-05-13 09:00",
         "2009-02-05 09:00",
         "2008-12-03 09:00",
         "2007-08-02 00:00",
         "2007-01-18 00:00",
         "2007-01-09 00:00",
         "2006-11-26 00:00",
         "2006-05-10 00:00",
         "2006-04-13 00:00",
         "2006-02-20 00:00",
         "2005-02-15 00:00",
         "2004-10-19 00:00",
         "2004-03-30 00:00",
         "2003-11-14 00:00",
         "2003-11-06 00:00",
         "2003-10-17 00:00",
         "2003-09-22 00:00",
         "2003-08-18 00:00",
         "2003-06-12 00:00",
         "2003-05-14 00:00",
         "2003-04-18 00:00",
         "2003-03-25 00:00",
         "2002-11-11 00:00",
         "2002-11-01 00:00",
         "2002-10-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FcphVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FcBbCredit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )



class FcRxDataFieldSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 2112),
    )



class FcBbCreditModel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("regular", 1))
    )



class FcIfOperStatusReason(Integer32, TextualConvention):
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
              286)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 12),
          ("adminStateConfigChange", 276),
          ("authzPending", 147),
          ("badFramesRcvdFromLink", 286),
          ("bitErrRTThresExceeded", 79),
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
          ("domainInvalidRCFReceived", 22),
          ("domainManagerDisabled", 23),
          ("domainMaxReTxFailure", 36),
          ("domainNotAllowedIsolated", 120),
          ("domainOther", 131),
          ("domainOtherSideEportIsolation", 21),
          ("domainOverlapIsolation", 19),
          ("dot1xSecViolationErrDisabled", 165),
          ("dupTunnelConfigDetected", 160),
          ("ePortProhibited", 106),
          ("ecSuspendedLoop", 116),
          ("elpFailureAllZeroPeerWWNRcvd", 132),
          ("elpFailureClassFParamErr", 68),
          ("elpFailureClassNParamErr", 69),
          ("elpFailureInvalidFlowCTLParam", 71),
          ("elpFailureInvalidPayloadSize", 77),
          ("elpFailureInvalidPortName", 72),
          ("elpFailureInvalidSwitchName", 73),
          ("elpFailureInvalidTxBBCredit", 76),
          ("elpFailureIsolation", 17),
          ("elpFailureLoopbackDetected", 75),
          ("elpFailureRatovEdtovMismatch", 74),
          ("elpFailureRevMismatch", 67),
          ("elpFailureUnknownFlowCTLCode", 70),
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
          ("errorDisabledReInitLimitReached", 126),
          ("escFailureIsolation", 18),
          ("ethIntfInvalidBinding", 245),
          ("ethIntfNotLicensed", 266),
          ("ethL2VlanDown", 244),
          ("externallyDisabled", 138),
          ("fabricBindingDBMismatch", 111),
          ("fabricBindingDomainInvalid", 110),
          ("fabricBindingNoRspFromPeer", 112),
          ("fabricBindingSWWNNotFound", 109),
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
          ("fcotChksumErr", 99),
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
          ("ficonNoPortSwapLogicalPort", 269),
          ("ficonNoPortnumber", 104),
          ("ficonNotEnabled", 103),
          ("ficonVsanDown", 61),
          ("firstPortNotUp", 46),
          ("firstPortUpAsEport", 45),
          ("flowControlMismatch", 249),
          ("hotStdbyInBundle", 148),
          ("hwFailure", 3),
          ("hwProgrammingFailed", 151),
          ("ifSifLimitExceeded", 177),
          ("inactiveM1PortFpathActiveVlan", 253),
          ("incomAdminRxBBCreditPerBuf", 64),
          ("incompatibleAdminMode", 31),
          ("incompatibleAdminRxBBCredit", 41),
          ("incompatibleAdminRxBufferSize", 42),
          ("incompatibleAdminSpeed", 32),
          ("incompleteConfig", 149),
          ("incompleteTunnelCfg", 150),
          ("initializing", 10),
          ("interfaceRemoved", 28),
          ("invalidAttachment", 62),
          ("invalidConfig", 57),
          ("invalidEncapsulation", 259),
          ("invalidFabricBindExh", 101),
          ("invalidOtherSidePrincEFPReqRecd", 130),
          ("invalidSatFabricIf", 185),
          ("ipQosDcbxpCompatFailure", 234),
          ("ipQosMgrPolicyAppFailure", 217),
          ("ipSecHndshkInProgress", 261),
          ("isolateBundleLimitExceeded", 181),
          ("isolatedBundle", 117),
          ("l3NotReady", 247),
          ("linkFailCreditLoss", 89),
          ("linkFailCreditLossB2B", 93),
          ("linkFailDebounceTimeout", 87),
          ("linkFailLIPF8Rcvd", 96),
          ("linkFailLIPRcvdB2B", 92),
          ("linkFailLRRcvdB2B", 88),
          ("linkFailLineCardPortShutdown", 97),
          ("linkFailLinkReset", 80),
          ("linkFailLossOfSignal", 83),
          ("linkFailLossOfSync", 84),
          ("linkFailNOSRcvd", 85),
          ("linkFailOLSRcvd", 86),
          ("linkFailOPNYRETB2B", 95),
          ("linkFailOPNYTMOB2B", 94),
          ("linkFailPortInitFail", 81),
          ("linkFailPortUnusable", 82),
          ("linkFailRxQOverFlow", 90),
          ("linkFailTooManyINTR", 91),
          ("linkFailure", 7),
          ("localRcf", 128),
          ("loopbackDiagFailure", 4),
          ("loopbackIsolation", 39),
          ("lstGrpUplinkDown", 219),
          ("modemLineDeasserted", 260),
          ("moduleOffline", 191),
          ("moduleRemoved", 255),
          ("neighborMismatchUDLD", 146),
          ("noCommonVsanIsolation", 60),
          ("noFcoe", 179),
          ("noRemoteChassis", 186),
          ("nonCiscoHbaVfTag", 235),
          ("nonCorePortMct", 257),
          ("nonExistentVlan", 230),
          ("nonParticipating", 9),
          ("nonStickyExternallyDisabled", 226),
          ("none", 2),
          ("npivNotEnabledInUpstream", 210),
          ("offline", 8),
          ("ohmsExtLBTest", 100),
          ("other", 1),
          ("outOfGlblRxBuffers", 264),
          ("outOfService", 122),
          ("parentDown", 26),
          ("parentPortDown", 254),
          ("pauseRateLimitErrDisabled", 218),
          ("peerFCIPPortClosedConnection", 47),
          ("peerFCIPPortResetConnection", 48),
          ("peerNotSupportBundle", 118),
          ("phyIntfDown", 176),
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
          ("rcfInProgress", 16),
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
          ("tooManyInvalidFLOGIs", 65),
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
          ("vpcNoRspFromPeer", 198),
          ("vpcPeerLinkDown", 197),
          ("vpcPeerUpgrade", 233),
          ("vrfForwardReferencing", 159),
          ("vrfMismatch", 158),
          ("vrfUnusable", 162),
          ("vsanInactive", 11),
          ("vsanMismatchIsolation", 25),
          ("vsanMismatchWithUpstreamSwPort", 211),
          ("vsanNotFound", 114),
          ("vsanSuspended", 113),
          ("waitForFlogi", 208),
          ("xcvrAbsent", 239),
          ("xcvrAuthFailed", 285),
          ("xcvrInitializing", 238),
          ("xcvrInvalid", 240),
          ("zoneMergeFailureIsolation", 24),
          ("zoneRemoteNoRespIsolation", 44))
    )



class FcPerfBuffer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 145),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFcFeObjects_ObjectIdentity = ObjectIdentity
ciscoFcFeObjects = _CiscoFcFeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1)
)
_CffFcFeConfig_ObjectIdentity = ObjectIdentity
cffFcFeConfig = _CffFcFeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1)
)
_CffFcFeElementName_Type = FcNameId
_CffFcFeElementName_Object = MibScalar
cffFcFeElementName = _CffFcFeElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 1),
    _CffFcFeElementName_Type()
)
cffFcFeElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cffFcFeElementName.setStatus("current")
_FcIfTable_Object = MibTable
fcIfTable = _FcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fcIfTable.setStatus("current")
_FcIfEntry_Object = MibTableRow
fcIfEntry = _FcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1)
)
fcIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfEntry.setStatus("current")
_FcIfWwn_Type = FcNameId
_FcIfWwn_Object = MibTableColumn
fcIfWwn = _FcIfWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 1),
    _FcIfWwn_Type()
)
fcIfWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfWwn.setStatus("current")


class _FcIfAdminMode_Type(FcPortTypes):
    """Custom type fcIfAdminMode based on FcPortTypes"""


_FcIfAdminMode_Object = MibTableColumn
fcIfAdminMode = _FcIfAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 2),
    _FcIfAdminMode_Type()
)
fcIfAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminMode.setStatus("current")
_FcIfOperMode_Type = FcPortTypes
_FcIfOperMode_Object = MibTableColumn
fcIfOperMode = _FcIfOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 3),
    _FcIfOperMode_Type()
)
fcIfOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperMode.setStatus("current")


class _FcIfAdminSpeed_Type(FcIfSpeed):
    """Custom type fcIfAdminSpeed based on FcIfSpeed"""


_FcIfAdminSpeed_Object = MibTableColumn
fcIfAdminSpeed = _FcIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 4),
    _FcIfAdminSpeed_Type()
)
fcIfAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminSpeed.setStatus("current")


class _FcIfBeaconMode_Type(TruthValue):
    """Custom type fcIfBeaconMode based on TruthValue"""


_FcIfBeaconMode_Object = MibTableColumn
fcIfBeaconMode = _FcIfBeaconMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 5),
    _FcIfBeaconMode_Type()
)
fcIfBeaconMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfBeaconMode.setStatus("current")
_FcIfPortChannelIfIndex_Type = InterfaceIndexOrZero
_FcIfPortChannelIfIndex_Object = MibTableColumn
fcIfPortChannelIfIndex = _FcIfPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 6),
    _FcIfPortChannelIfIndex_Type()
)
fcIfPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfPortChannelIfIndex.setStatus("current")
_FcIfOperStatusCause_Type = FcIfOperStatusReason
_FcIfOperStatusCause_Object = MibTableColumn
fcIfOperStatusCause = _FcIfOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 7),
    _FcIfOperStatusCause_Type()
)
fcIfOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperStatusCause.setStatus("current")
_FcIfOperStatusCauseDescr_Type = SnmpAdminString
_FcIfOperStatusCauseDescr_Object = MibTableColumn
fcIfOperStatusCauseDescr = _FcIfOperStatusCauseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 8),
    _FcIfOperStatusCauseDescr_Type()
)
fcIfOperStatusCauseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperStatusCauseDescr.setStatus("current")


class _FcIfAdminTrunkMode_Type(Integer32):
    """Custom type fcIfAdminTrunkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("nonTrunk", 1),
          ("trunk", 2))
    )


_FcIfAdminTrunkMode_Type.__name__ = "Integer32"
_FcIfAdminTrunkMode_Object = MibTableColumn
fcIfAdminTrunkMode = _FcIfAdminTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 9),
    _FcIfAdminTrunkMode_Type()
)
fcIfAdminTrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminTrunkMode.setStatus("current")


class _FcIfOperTrunkMode_Type(Integer32):
    """Custom type fcIfOperTrunkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonTrunk", 1),
          ("trunk", 2))
    )


_FcIfOperTrunkMode_Type.__name__ = "Integer32"
_FcIfOperTrunkMode_Object = MibTableColumn
fcIfOperTrunkMode = _FcIfOperTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 10),
    _FcIfOperTrunkMode_Type()
)
fcIfOperTrunkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperTrunkMode.setStatus("current")
_FcIfAllowedVsanList2k_Type = FcList
_FcIfAllowedVsanList2k_Object = MibTableColumn
fcIfAllowedVsanList2k = _FcIfAllowedVsanList2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 11),
    _FcIfAllowedVsanList2k_Type()
)
fcIfAllowedVsanList2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAllowedVsanList2k.setStatus("current")
_FcIfAllowedVsanList4k_Type = FcList
_FcIfAllowedVsanList4k_Object = MibTableColumn
fcIfAllowedVsanList4k = _FcIfAllowedVsanList4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 12),
    _FcIfAllowedVsanList4k_Type()
)
fcIfAllowedVsanList4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAllowedVsanList4k.setStatus("current")
_FcIfActiveVsanList2k_Type = FcList
_FcIfActiveVsanList2k_Object = MibTableColumn
fcIfActiveVsanList2k = _FcIfActiveVsanList2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 13),
    _FcIfActiveVsanList2k_Type()
)
fcIfActiveVsanList2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfActiveVsanList2k.setStatus("current")
_FcIfActiveVsanList4k_Type = FcList
_FcIfActiveVsanList4k_Object = MibTableColumn
fcIfActiveVsanList4k = _FcIfActiveVsanList4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 14),
    _FcIfActiveVsanList4k_Type()
)
fcIfActiveVsanList4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfActiveVsanList4k.setStatus("current")
_FcIfBbCreditModel_Type = FcBbCreditModel
_FcIfBbCreditModel_Object = MibTableColumn
fcIfBbCreditModel = _FcIfBbCreditModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 15),
    _FcIfBbCreditModel_Type()
)
fcIfBbCreditModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfBbCreditModel.setStatus("current")
_FcIfHoldTime_Type = MicroSeconds
_FcIfHoldTime_Object = MibTableColumn
fcIfHoldTime = _FcIfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 16),
    _FcIfHoldTime_Type()
)
fcIfHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fcIfHoldTime.setUnits("microseconds")
_FcIfTransmitterType_Type = FcPortTxTypes
_FcIfTransmitterType_Object = MibTableColumn
fcIfTransmitterType = _FcIfTransmitterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 17),
    _FcIfTransmitterType_Type()
)
fcIfTransmitterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfTransmitterType.setStatus("current")
_FcIfConnectorType_Type = FcPortModuleTypes
_FcIfConnectorType_Object = MibTableColumn
fcIfConnectorType = _FcIfConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 18),
    _FcIfConnectorType_Type()
)
fcIfConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfConnectorType.setStatus("current")
_FcIfSerialNo_Type = SnmpAdminString
_FcIfSerialNo_Object = MibTableColumn
fcIfSerialNo = _FcIfSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 19),
    _FcIfSerialNo_Type()
)
fcIfSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfSerialNo.setStatus("current")
_FcIfRevision_Type = SnmpAdminString
_FcIfRevision_Object = MibTableColumn
fcIfRevision = _FcIfRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 20),
    _FcIfRevision_Type()
)
fcIfRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRevision.setStatus("current")
_FcIfVendor_Type = SnmpAdminString
_FcIfVendor_Object = MibTableColumn
fcIfVendor = _FcIfVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 21),
    _FcIfVendor_Type()
)
fcIfVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfVendor.setStatus("current")
_FcIfSFPSerialIDData_Type = SnmpAdminString
_FcIfSFPSerialIDData_Object = MibTableColumn
fcIfSFPSerialIDData = _FcIfSFPSerialIDData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 22),
    _FcIfSFPSerialIDData_Type()
)
fcIfSFPSerialIDData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfSFPSerialIDData.setStatus("current")
_FcIfPartNumber_Type = SnmpAdminString
_FcIfPartNumber_Object = MibTableColumn
fcIfPartNumber = _FcIfPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 23),
    _FcIfPartNumber_Type()
)
fcIfPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfPartNumber.setStatus("current")
_FcIfAdminRxBbCredit_Type = FcBbCredit
_FcIfAdminRxBbCredit_Object = MibTableColumn
fcIfAdminRxBbCredit = _FcIfAdminRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 24),
    _FcIfAdminRxBbCredit_Type()
)
fcIfAdminRxBbCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCredit.setStatus("current")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCredit.setUnits("buffers")
_FcIfAdminRxBbCreditModeISL_Type = FcBbCredit
_FcIfAdminRxBbCreditModeISL_Object = MibTableColumn
fcIfAdminRxBbCreditModeISL = _FcIfAdminRxBbCreditModeISL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 25),
    _FcIfAdminRxBbCreditModeISL_Type()
)
fcIfAdminRxBbCreditModeISL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCreditModeISL.setStatus("current")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCreditModeISL.setUnits("buffers")
_FcIfAdminRxBbCreditModeFx_Type = FcBbCredit
_FcIfAdminRxBbCreditModeFx_Object = MibTableColumn
fcIfAdminRxBbCreditModeFx = _FcIfAdminRxBbCreditModeFx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 26),
    _FcIfAdminRxBbCreditModeFx_Type()
)
fcIfAdminRxBbCreditModeFx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCreditModeFx.setStatus("current")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCreditModeFx.setUnits("buffers")
_FcIfOperRxBbCredit_Type = FcBbCredit
_FcIfOperRxBbCredit_Object = MibTableColumn
fcIfOperRxBbCredit = _FcIfOperRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 27),
    _FcIfOperRxBbCredit_Type()
)
fcIfOperRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperRxBbCredit.setStatus("current")
if mibBuilder.loadTexts:
    fcIfOperRxBbCredit.setUnits("buffers")
_FcIfRxDataFieldSize_Type = FcRxDataFieldSize
_FcIfRxDataFieldSize_Object = MibTableColumn
fcIfRxDataFieldSize = _FcIfRxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 28),
    _FcIfRxDataFieldSize_Type()
)
fcIfRxDataFieldSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfRxDataFieldSize.setStatus("current")
if mibBuilder.loadTexts:
    fcIfRxDataFieldSize.setUnits("bytes")
_FcIfActiveVsanUpList2k_Type = FcList
_FcIfActiveVsanUpList2k_Object = MibTableColumn
fcIfActiveVsanUpList2k = _FcIfActiveVsanUpList2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 29),
    _FcIfActiveVsanUpList2k_Type()
)
fcIfActiveVsanUpList2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfActiveVsanUpList2k.setStatus("current")
_FcIfActiveVsanUpList4k_Type = FcList
_FcIfActiveVsanUpList4k_Object = MibTableColumn
fcIfActiveVsanUpList4k = _FcIfActiveVsanUpList4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 30),
    _FcIfActiveVsanUpList4k_Type()
)
fcIfActiveVsanUpList4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfActiveVsanUpList4k.setStatus("current")


class _FcIfPortRateMode_Type(Integer32):
    """Custom type fcIfPortRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("shared", 2))
    )


_FcIfPortRateMode_Type.__name__ = "Integer32"
_FcIfPortRateMode_Object = MibTableColumn
fcIfPortRateMode = _FcIfPortRateMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 31),
    _FcIfPortRateMode_Type()
)
fcIfPortRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfPortRateMode.setStatus("current")


class _FcIfAdminRxPerfBuffer_Type(FcPerfBuffer):
    """Custom type fcIfAdminRxPerfBuffer based on FcPerfBuffer"""
    defaultValue = 0


_FcIfAdminRxPerfBuffer_Object = MibTableColumn
fcIfAdminRxPerfBuffer = _FcIfAdminRxPerfBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 32),
    _FcIfAdminRxPerfBuffer_Type()
)
fcIfAdminRxPerfBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminRxPerfBuffer.setStatus("current")
if mibBuilder.loadTexts:
    fcIfAdminRxPerfBuffer.setUnits("buffers")
_FcIfOperRxPerfBuffer_Type = FcPerfBuffer
_FcIfOperRxPerfBuffer_Object = MibTableColumn
fcIfOperRxPerfBuffer = _FcIfOperRxPerfBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 33),
    _FcIfOperRxPerfBuffer_Type()
)
fcIfOperRxPerfBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperRxPerfBuffer.setStatus("current")
if mibBuilder.loadTexts:
    fcIfOperRxPerfBuffer.setUnits("buffers")
_FcIfBbScn_Type = Unsigned32
_FcIfBbScn_Object = MibTableColumn
fcIfBbScn = _FcIfBbScn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 34),
    _FcIfBbScn_Type()
)
fcIfBbScn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfBbScn.setStatus("current")
_FcIfPortInitStatus_Type = TruthValue
_FcIfPortInitStatus_Object = MibTableColumn
fcIfPortInitStatus = _FcIfPortInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 35),
    _FcIfPortInitStatus_Type()
)
fcIfPortInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfPortInitStatus.setStatus("current")
_FcIfAdminRxBbCreditExtended_Type = FcBbCredit
_FcIfAdminRxBbCreditExtended_Object = MibTableColumn
fcIfAdminRxBbCreditExtended = _FcIfAdminRxBbCreditExtended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 36),
    _FcIfAdminRxBbCreditExtended_Type()
)
fcIfAdminRxBbCreditExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCreditExtended.setStatus("current")
if mibBuilder.loadTexts:
    fcIfAdminRxBbCreditExtended.setUnits("buffers")
_FcIfFcTunnelIfIndex_Type = InterfaceIndexOrZero
_FcIfFcTunnelIfIndex_Object = MibTableColumn
fcIfFcTunnelIfIndex = _FcIfFcTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 37),
    _FcIfFcTunnelIfIndex_Type()
)
fcIfFcTunnelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfFcTunnelIfIndex.setStatus("current")


class _FcIfServiceState_Type(FcIfServiceStateType):
    """Custom type fcIfServiceState based on FcIfServiceStateType"""


_FcIfServiceState_Object = MibTableColumn
fcIfServiceState = _FcIfServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 38),
    _FcIfServiceState_Type()
)
fcIfServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfServiceState.setStatus("current")


class _FcIfAdminBbScnMode_Type(TruthValue):
    """Custom type fcIfAdminBbScnMode based on TruthValue"""


_FcIfAdminBbScnMode_Object = MibTableColumn
fcIfAdminBbScnMode = _FcIfAdminBbScnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 39),
    _FcIfAdminBbScnMode_Type()
)
fcIfAdminBbScnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminBbScnMode.setStatus("current")


class _FcIfPortType_Type(Integer32):
    """Custom type fcIfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_FcIfPortType_Type.__name__ = "Integer32"
_FcIfPortType_Object = MibTableColumn
fcIfPortType = _FcIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 40),
    _FcIfPortType_Type()
)
fcIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfPortType.setStatus("current")


class _FcIfAdminFECState_Type(Integer32):
    """Custom type fcIfAdminFECState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_FcIfAdminFECState_Type.__name__ = "Integer32"
_FcIfAdminFECState_Object = MibTableColumn
fcIfAdminFECState = _FcIfAdminFECState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 41),
    _FcIfAdminFECState_Type()
)
fcIfAdminFECState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminFECState.setStatus("current")


class _FcIfOperFECState_Type(Integer32):
    """Custom type fcIfOperFECState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_FcIfOperFECState_Type.__name__ = "Integer32"
_FcIfOperFECState_Object = MibTableColumn
fcIfOperFECState = _FcIfOperFECState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 2, 1, 42),
    _FcIfOperFECState_Type()
)
fcIfOperFECState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperFECState.setStatus("current")
_FcTrunkIfTable_Object = MibTable
fcTrunkIfTable = _FcTrunkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fcTrunkIfTable.setStatus("current")
_FcTrunkIfEntry_Object = MibTableRow
fcTrunkIfEntry = _FcTrunkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 3, 1)
)
fcTrunkIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fcTrunkIfEntry.setStatus("current")


class _FcTrunkIfOperStatus_Type(Integer32):
    """Custom type fcTrunkIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_FcTrunkIfOperStatus_Type.__name__ = "Integer32"
_FcTrunkIfOperStatus_Object = MibTableColumn
fcTrunkIfOperStatus = _FcTrunkIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 3, 1, 1),
    _FcTrunkIfOperStatus_Type()
)
fcTrunkIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTrunkIfOperStatus.setStatus("current")
_FcTrunkIfOperStatusCause_Type = FcIfOperStatusReason
_FcTrunkIfOperStatusCause_Object = MibTableColumn
fcTrunkIfOperStatusCause = _FcTrunkIfOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 3, 1, 2),
    _FcTrunkIfOperStatusCause_Type()
)
fcTrunkIfOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTrunkIfOperStatusCause.setStatus("current")
_FcTrunkIfOperStatusCauseDescr_Type = SnmpAdminString
_FcTrunkIfOperStatusCauseDescr_Object = MibTableColumn
fcTrunkIfOperStatusCauseDescr = _FcTrunkIfOperStatusCauseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 3, 1, 3),
    _FcTrunkIfOperStatusCauseDescr_Type()
)
fcTrunkIfOperStatusCauseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTrunkIfOperStatusCauseDescr.setStatus("current")
_FcIfLoginEntryCount_Type = Unsigned32
_FcIfLoginEntryCount_Object = MibScalar
fcIfLoginEntryCount = _FcIfLoginEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 4),
    _FcIfLoginEntryCount_Type()
)
fcIfLoginEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLoginEntryCount.setStatus("current")
_FcIfFLoginTable_Object = MibTable
fcIfFLoginTable = _FcIfFLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcIfFLoginTable.setStatus("current")
_FcIfFLoginEntry_Object = MibTableRow
fcIfFLoginEntry = _FcIfFLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1)
)
fcIfFLoginEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FC-FE-MIB", "fcIfNxLoginIndex"),
)
if mibBuilder.loadTexts:
    fcIfFLoginEntry.setStatus("current")
_FcIfNxLoginIndex_Type = Unsigned32
_FcIfNxLoginIndex_Object = MibTableColumn
fcIfNxLoginIndex = _FcIfNxLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 1),
    _FcIfNxLoginIndex_Type()
)
fcIfNxLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcIfNxLoginIndex.setStatus("current")
_FcIfNxPortNodeName_Type = FcNameId
_FcIfNxPortNodeName_Object = MibTableColumn
fcIfNxPortNodeName = _FcIfNxPortNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 2),
    _FcIfNxPortNodeName_Type()
)
fcIfNxPortNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxPortNodeName.setStatus("current")
_FcIfNxPortName_Type = FcNameId
_FcIfNxPortName_Object = MibTableColumn
fcIfNxPortName = _FcIfNxPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 3),
    _FcIfNxPortName_Type()
)
fcIfNxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxPortName.setStatus("current")
_FcIfNxPortAddress_Type = FcAddressId
_FcIfNxPortAddress_Object = MibTableColumn
fcIfNxPortAddress = _FcIfNxPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 4),
    _FcIfNxPortAddress_Type()
)
fcIfNxPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxPortAddress.setStatus("current")
_FcIfNxFcphVersionAgreed_Type = FcphVersion
_FcIfNxFcphVersionAgreed_Object = MibTableColumn
fcIfNxFcphVersionAgreed = _FcIfNxFcphVersionAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 5),
    _FcIfNxFcphVersionAgreed_Type()
)
fcIfNxFcphVersionAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxFcphVersionAgreed.setStatus("current")
_FcIfNxRxBbCredit_Type = FcBbCredit
_FcIfNxRxBbCredit_Object = MibTableColumn
fcIfNxRxBbCredit = _FcIfNxRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 6),
    _FcIfNxRxBbCredit_Type()
)
fcIfNxRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxRxBbCredit.setStatus("current")
_FcIfNxTxBbCredit_Type = FcBbCredit
_FcIfNxTxBbCredit_Object = MibTableColumn
fcIfNxTxBbCredit = _FcIfNxTxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 7),
    _FcIfNxTxBbCredit_Type()
)
fcIfNxTxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxTxBbCredit.setStatus("current")
_FcIfNxClass2RxDataFieldSize_Type = FcRxDataFieldSize
_FcIfNxClass2RxDataFieldSize_Object = MibTableColumn
fcIfNxClass2RxDataFieldSize = _FcIfNxClass2RxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 8),
    _FcIfNxClass2RxDataFieldSize_Type()
)
fcIfNxClass2RxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxClass2RxDataFieldSize.setStatus("current")
_FcIfNxClass3RxDataFieldSize_Type = FcRxDataFieldSize
_FcIfNxClass3RxDataFieldSize_Object = MibTableColumn
fcIfNxClass3RxDataFieldSize = _FcIfNxClass3RxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 9),
    _FcIfNxClass3RxDataFieldSize_Type()
)
fcIfNxClass3RxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxClass3RxDataFieldSize.setStatus("current")
_FcIfNxCosSuppAgreed_Type = FcClassOfServices
_FcIfNxCosSuppAgreed_Object = MibTableColumn
fcIfNxCosSuppAgreed = _FcIfNxCosSuppAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 10),
    _FcIfNxCosSuppAgreed_Type()
)
fcIfNxCosSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxCosSuppAgreed.setStatus("current")
_FcIfNxClass2SeqDelivAgreed_Type = TruthValue
_FcIfNxClass2SeqDelivAgreed_Object = MibTableColumn
fcIfNxClass2SeqDelivAgreed = _FcIfNxClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 11),
    _FcIfNxClass2SeqDelivAgreed_Type()
)
fcIfNxClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxClass2SeqDelivAgreed.setStatus("current")
_FcIfNxClass3SeqDelivAgreed_Type = TruthValue
_FcIfNxClass3SeqDelivAgreed_Object = MibTableColumn
fcIfNxClass3SeqDelivAgreed = _FcIfNxClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 5, 1, 12),
    _FcIfNxClass3SeqDelivAgreed_Type()
)
fcIfNxClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNxClass3SeqDelivAgreed.setStatus("current")
_FcIfElpTable_Object = MibTable
fcIfElpTable = _FcIfElpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fcIfElpTable.setStatus("current")
_FcIfElpEntry_Object = MibTableRow
fcIfElpEntry = _FcIfElpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1)
)
fcIfElpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfElpEntry.setStatus("current")
_FcIfElpNbrNodeName_Type = FcNameId
_FcIfElpNbrNodeName_Object = MibTableColumn
fcIfElpNbrNodeName = _FcIfElpNbrNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 1),
    _FcIfElpNbrNodeName_Type()
)
fcIfElpNbrNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpNbrNodeName.setStatus("current")
_FcIfElpNbrPortName_Type = FcNameId
_FcIfElpNbrPortName_Object = MibTableColumn
fcIfElpNbrPortName = _FcIfElpNbrPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 2),
    _FcIfElpNbrPortName_Type()
)
fcIfElpNbrPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpNbrPortName.setStatus("current")
_FcIfElpRxBbCredit_Type = FcBbCredit
_FcIfElpRxBbCredit_Object = MibTableColumn
fcIfElpRxBbCredit = _FcIfElpRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 3),
    _FcIfElpRxBbCredit_Type()
)
fcIfElpRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpRxBbCredit.setStatus("current")
_FcIfElpTxBbCredit_Type = FcBbCredit
_FcIfElpTxBbCredit_Object = MibTableColumn
fcIfElpTxBbCredit = _FcIfElpTxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 4),
    _FcIfElpTxBbCredit_Type()
)
fcIfElpTxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpTxBbCredit.setStatus("current")
_FcIfElpCosSuppAgreed_Type = FcClassOfServices
_FcIfElpCosSuppAgreed_Object = MibTableColumn
fcIfElpCosSuppAgreed = _FcIfElpCosSuppAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 5),
    _FcIfElpCosSuppAgreed_Type()
)
fcIfElpCosSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpCosSuppAgreed.setStatus("current")
_FcIfElpClass2SeqDelivAgreed_Type = TruthValue
_FcIfElpClass2SeqDelivAgreed_Object = MibTableColumn
fcIfElpClass2SeqDelivAgreed = _FcIfElpClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 6),
    _FcIfElpClass2SeqDelivAgreed_Type()
)
fcIfElpClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClass2SeqDelivAgreed.setStatus("current")
_FcIfElpClass2RxDataFieldSize_Type = FcRxDataFieldSize
_FcIfElpClass2RxDataFieldSize_Object = MibTableColumn
fcIfElpClass2RxDataFieldSize = _FcIfElpClass2RxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 7),
    _FcIfElpClass2RxDataFieldSize_Type()
)
fcIfElpClass2RxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClass2RxDataFieldSize.setStatus("current")
_FcIfElpClass3SeqDelivAgreed_Type = TruthValue
_FcIfElpClass3SeqDelivAgreed_Object = MibTableColumn
fcIfElpClass3SeqDelivAgreed = _FcIfElpClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 8),
    _FcIfElpClass3SeqDelivAgreed_Type()
)
fcIfElpClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClass3SeqDelivAgreed.setStatus("current")
_FcIfElpClass3RxDataFieldSize_Type = FcRxDataFieldSize
_FcIfElpClass3RxDataFieldSize_Object = MibTableColumn
fcIfElpClass3RxDataFieldSize = _FcIfElpClass3RxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 9),
    _FcIfElpClass3RxDataFieldSize_Type()
)
fcIfElpClass3RxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClass3RxDataFieldSize.setStatus("current")
_FcIfElpClassFXII_Type = TruthValue
_FcIfElpClassFXII_Object = MibTableColumn
fcIfElpClassFXII = _FcIfElpClassFXII_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 10),
    _FcIfElpClassFXII_Type()
)
fcIfElpClassFXII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClassFXII.setStatus("current")
_FcIfElpClassFRxDataFieldSize_Type = FcRxDataFieldSize
_FcIfElpClassFRxDataFieldSize_Object = MibTableColumn
fcIfElpClassFRxDataFieldSize = _FcIfElpClassFRxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 11),
    _FcIfElpClassFRxDataFieldSize_Type()
)
fcIfElpClassFRxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClassFRxDataFieldSize.setStatus("current")


class _FcIfElpClassFConcurrentSeq_Type(Unsigned32):
    """Custom type fcIfElpClassFConcurrentSeq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcIfElpClassFConcurrentSeq_Type.__name__ = "Unsigned32"
_FcIfElpClassFConcurrentSeq_Object = MibTableColumn
fcIfElpClassFConcurrentSeq = _FcIfElpClassFConcurrentSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 12),
    _FcIfElpClassFConcurrentSeq_Type()
)
fcIfElpClassFConcurrentSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClassFConcurrentSeq.setStatus("current")
_FcIfElpClassFEndToEndCredit_Type = Unsigned32
_FcIfElpClassFEndToEndCredit_Object = MibTableColumn
fcIfElpClassFEndToEndCredit = _FcIfElpClassFEndToEndCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 13),
    _FcIfElpClassFEndToEndCredit_Type()
)
fcIfElpClassFEndToEndCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClassFEndToEndCredit.setStatus("current")
_FcIfElpClassFOpenSeq_Type = Unsigned32
_FcIfElpClassFOpenSeq_Object = MibTableColumn
fcIfElpClassFOpenSeq = _FcIfElpClassFOpenSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 6, 1, 14),
    _FcIfElpClassFOpenSeq_Type()
)
fcIfElpClassFOpenSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfElpClassFOpenSeq.setStatus("current")
_FcIfCapTable_Object = MibTable
fcIfCapTable = _FcIfCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fcIfCapTable.setStatus("current")
_FcIfCapEntry_Object = MibTableRow
fcIfCapEntry = _FcIfCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1)
)
fcIfCapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfCapEntry.setStatus("current")
_FcIfCapFcphVersionHigh_Type = FcphVersion
_FcIfCapFcphVersionHigh_Object = MibTableColumn
fcIfCapFcphVersionHigh = _FcIfCapFcphVersionHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 1),
    _FcIfCapFcphVersionHigh_Type()
)
fcIfCapFcphVersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFcphVersionHigh.setStatus("current")
_FcIfCapFcphVersionLow_Type = FcphVersion
_FcIfCapFcphVersionLow_Object = MibTableColumn
fcIfCapFcphVersionLow = _FcIfCapFcphVersionLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 2),
    _FcIfCapFcphVersionLow_Type()
)
fcIfCapFcphVersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFcphVersionLow.setStatus("current")
_FcIfCapRxBbCreditMax_Type = FcBbCredit
_FcIfCapRxBbCreditMax_Object = MibTableColumn
fcIfCapRxBbCreditMax = _FcIfCapRxBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 3),
    _FcIfCapRxBbCreditMax_Type()
)
fcIfCapRxBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditMax.setUnits("buffers")
_FcIfCapRxBbCreditMin_Type = FcBbCredit
_FcIfCapRxBbCreditMin_Object = MibTableColumn
fcIfCapRxBbCreditMin = _FcIfCapRxBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 4),
    _FcIfCapRxBbCreditMin_Type()
)
fcIfCapRxBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditMin.setUnits("buffers")
_FcIfCapRxDataFieldSizeMax_Type = FcRxDataFieldSize
_FcIfCapRxDataFieldSizeMax_Object = MibTableColumn
fcIfCapRxDataFieldSizeMax = _FcIfCapRxDataFieldSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 5),
    _FcIfCapRxDataFieldSizeMax_Type()
)
fcIfCapRxDataFieldSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapRxDataFieldSizeMax.setStatus("current")
_FcIfCapRxDataFieldSizeMin_Type = FcRxDataFieldSize
_FcIfCapRxDataFieldSizeMin_Object = MibTableColumn
fcIfCapRxDataFieldSizeMin = _FcIfCapRxDataFieldSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 6),
    _FcIfCapRxDataFieldSizeMin_Type()
)
fcIfCapRxDataFieldSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapRxDataFieldSizeMin.setStatus("current")
_FcIfCapCos_Type = FcClassOfServices
_FcIfCapCos_Object = MibTableColumn
fcIfCapCos = _FcIfCapCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 7),
    _FcIfCapCos_Type()
)
fcIfCapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapCos.setStatus("current")
_FcIfCapClass2SeqDeliv_Type = TruthValue
_FcIfCapClass2SeqDeliv_Object = MibTableColumn
fcIfCapClass2SeqDeliv = _FcIfCapClass2SeqDeliv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 8),
    _FcIfCapClass2SeqDeliv_Type()
)
fcIfCapClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapClass2SeqDeliv.setStatus("current")
_FcIfCapClass3SeqDeliv_Type = TruthValue
_FcIfCapClass3SeqDeliv_Object = MibTableColumn
fcIfCapClass3SeqDeliv = _FcIfCapClass3SeqDeliv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 9),
    _FcIfCapClass3SeqDeliv_Type()
)
fcIfCapClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapClass3SeqDeliv.setStatus("current")
_FcIfCapHoldTimeMax_Type = MicroSeconds
_FcIfCapHoldTimeMax_Object = MibTableColumn
fcIfCapHoldTimeMax = _FcIfCapHoldTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 10),
    _FcIfCapHoldTimeMax_Type()
)
fcIfCapHoldTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapHoldTimeMax.setStatus("current")
_FcIfCapHoldTimeMin_Type = MicroSeconds
_FcIfCapHoldTimeMin_Object = MibTableColumn
fcIfCapHoldTimeMin = _FcIfCapHoldTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 11),
    _FcIfCapHoldTimeMin_Type()
)
fcIfCapHoldTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapHoldTimeMin.setStatus("current")
_FcIfCapISLRxBbCreditMax_Type = FcBbCredit
_FcIfCapISLRxBbCreditMax_Object = MibTableColumn
fcIfCapISLRxBbCreditMax = _FcIfCapISLRxBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 12),
    _FcIfCapISLRxBbCreditMax_Type()
)
fcIfCapISLRxBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapISLRxBbCreditMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfCapISLRxBbCreditMax.setUnits("buffers")
_FcIfCapISLRxBbCreditMin_Type = FcBbCredit
_FcIfCapISLRxBbCreditMin_Object = MibTableColumn
fcIfCapISLRxBbCreditMin = _FcIfCapISLRxBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 13),
    _FcIfCapISLRxBbCreditMin_Type()
)
fcIfCapISLRxBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapISLRxBbCreditMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfCapISLRxBbCreditMin.setUnits("buffers")
_FcIfCapRxBbCreditWriteable_Type = TruthValue
_FcIfCapRxBbCreditWriteable_Object = MibTableColumn
fcIfCapRxBbCreditWriteable = _FcIfCapRxBbCreditWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 14),
    _FcIfCapRxBbCreditWriteable_Type()
)
fcIfCapRxBbCreditWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditWriteable.setStatus("deprecated")
_FcIfCapRxBbCreditDefault_Type = FcBbCredit
_FcIfCapRxBbCreditDefault_Object = MibTableColumn
fcIfCapRxBbCreditDefault = _FcIfCapRxBbCreditDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 15),
    _FcIfCapRxBbCreditDefault_Type()
)
fcIfCapRxBbCreditDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditDefault.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfCapRxBbCreditDefault.setUnits("buffers")
_FcIfCapISLRxBbCreditDefault_Type = FcBbCredit
_FcIfCapISLRxBbCreditDefault_Object = MibTableColumn
fcIfCapISLRxBbCreditDefault = _FcIfCapISLRxBbCreditDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 16),
    _FcIfCapISLRxBbCreditDefault_Type()
)
fcIfCapISLRxBbCreditDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapISLRxBbCreditDefault.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfCapISLRxBbCreditDefault.setUnits("buffers")
_FcIfCapBbScnCapable_Type = TruthValue
_FcIfCapBbScnCapable_Object = MibTableColumn
fcIfCapBbScnCapable = _FcIfCapBbScnCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 17),
    _FcIfCapBbScnCapable_Type()
)
fcIfCapBbScnCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapBbScnCapable.setStatus("current")
_FcIfCapBbScnMax_Type = Unsigned32
_FcIfCapBbScnMax_Object = MibTableColumn
fcIfCapBbScnMax = _FcIfCapBbScnMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 18),
    _FcIfCapBbScnMax_Type()
)
fcIfCapBbScnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapBbScnMax.setStatus("current")
_FcIfCapOsmFrmCapable_Type = TruthValue
_FcIfCapOsmFrmCapable_Object = MibTableColumn
fcIfCapOsmFrmCapable = _FcIfCapOsmFrmCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 19),
    _FcIfCapOsmFrmCapable_Type()
)
fcIfCapOsmFrmCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmFrmCapable.setStatus("current")
_FcIfIsServiceStateCapable_Type = TruthValue
_FcIfIsServiceStateCapable_Object = MibTableColumn
fcIfIsServiceStateCapable = _FcIfIsServiceStateCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 20),
    _FcIfIsServiceStateCapable_Type()
)
fcIfIsServiceStateCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfIsServiceStateCapable.setStatus("current")
_FcIfIsPortRateModeCapable_Type = TruthValue
_FcIfIsPortRateModeCapable_Object = MibTableColumn
fcIfIsPortRateModeCapable = _FcIfIsPortRateModeCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 21),
    _FcIfIsPortRateModeCapable_Type()
)
fcIfIsPortRateModeCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfIsPortRateModeCapable.setStatus("current")
_FcIfIsAdminRxBbCreditExtendedCapable_Type = TruthValue
_FcIfIsAdminRxBbCreditExtendedCapable_Object = MibTableColumn
fcIfIsAdminRxBbCreditExtendedCapable = _FcIfIsAdminRxBbCreditExtendedCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 7, 1, 22),
    _FcIfIsAdminRxBbCreditExtendedCapable_Type()
)
fcIfIsAdminRxBbCreditExtendedCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfIsAdminRxBbCreditExtendedCapable.setStatus("current")


class _AdminTrunkProtocol_Type(Integer32):
    """Custom type adminTrunkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AdminTrunkProtocol_Type.__name__ = "Integer32"
_AdminTrunkProtocol_Object = MibScalar
adminTrunkProtocol = _AdminTrunkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 8),
    _AdminTrunkProtocol_Type()
)
adminTrunkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTrunkProtocol.setStatus("current")


class _FcIfElpRejectReasonCode_Type(Integer32):
    """Custom type fcIfElpRejectReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcIfElpRejectReasonCode_Type.__name__ = "Integer32"
_FcIfElpRejectReasonCode_Object = MibScalar
fcIfElpRejectReasonCode = _FcIfElpRejectReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 9),
    _FcIfElpRejectReasonCode_Type()
)
fcIfElpRejectReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fcIfElpRejectReasonCode.setStatus("current")


class _FcIfElpRejectReasonCodeExpl_Type(Integer32):
    """Custom type fcIfElpRejectReasonCodeExpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcIfElpRejectReasonCodeExpl_Type.__name__ = "Integer32"
_FcIfElpRejectReasonCodeExpl_Object = MibScalar
fcIfElpRejectReasonCodeExpl = _FcIfElpRejectReasonCodeExpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 10),
    _FcIfElpRejectReasonCodeExpl_Type()
)
fcIfElpRejectReasonCodeExpl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fcIfElpRejectReasonCodeExpl.setStatus("current")
_FcIfCapOsmTable_Object = MibTable
fcIfCapOsmTable = _FcIfCapOsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11)
)
if mibBuilder.loadTexts:
    fcIfCapOsmTable.setStatus("current")
_FcIfCapOsmEntry_Object = MibTableRow
fcIfCapOsmEntry = _FcIfCapOsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1)
)
fcIfCapOsmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfCapOsmEntry.setStatus("current")
_FcIfCapOsmRxBbCreditWriteable_Type = TruthValue
_FcIfCapOsmRxBbCreditWriteable_Object = MibTableColumn
fcIfCapOsmRxBbCreditWriteable = _FcIfCapOsmRxBbCreditWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 1),
    _FcIfCapOsmRxBbCreditWriteable_Type()
)
fcIfCapOsmRxBbCreditWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxBbCreditWriteable.setStatus("current")
_FcIfCapOsmRxBbCreditMax_Type = FcBbCredit
_FcIfCapOsmRxBbCreditMax_Object = MibTableColumn
fcIfCapOsmRxBbCreditMax = _FcIfCapOsmRxBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 2),
    _FcIfCapOsmRxBbCreditMax_Type()
)
fcIfCapOsmRxBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxBbCreditMax.setStatus("current")
_FcIfCapOsmRxBbCreditMin_Type = FcBbCredit
_FcIfCapOsmRxBbCreditMin_Object = MibTableColumn
fcIfCapOsmRxBbCreditMin = _FcIfCapOsmRxBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 3),
    _FcIfCapOsmRxBbCreditMin_Type()
)
fcIfCapOsmRxBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxBbCreditMin.setStatus("current")
_FcIfCapOsmRxBbCreditDefault_Type = FcBbCredit
_FcIfCapOsmRxBbCreditDefault_Object = MibTableColumn
fcIfCapOsmRxBbCreditDefault = _FcIfCapOsmRxBbCreditDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 4),
    _FcIfCapOsmRxBbCreditDefault_Type()
)
fcIfCapOsmRxBbCreditDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxBbCreditDefault.setStatus("current")
_FcIfCapOsmISLRxBbCreditMax_Type = FcBbCredit
_FcIfCapOsmISLRxBbCreditMax_Object = MibTableColumn
fcIfCapOsmISLRxBbCreditMax = _FcIfCapOsmISLRxBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 5),
    _FcIfCapOsmISLRxBbCreditMax_Type()
)
fcIfCapOsmISLRxBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmISLRxBbCreditMax.setStatus("current")
_FcIfCapOsmISLRxBbCreditMin_Type = FcBbCredit
_FcIfCapOsmISLRxBbCreditMin_Object = MibTableColumn
fcIfCapOsmISLRxBbCreditMin = _FcIfCapOsmISLRxBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 6),
    _FcIfCapOsmISLRxBbCreditMin_Type()
)
fcIfCapOsmISLRxBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmISLRxBbCreditMin.setStatus("current")
_FcIfCapOsmISLRxBbCreditDefault_Type = FcBbCredit
_FcIfCapOsmISLRxBbCreditDefault_Object = MibTableColumn
fcIfCapOsmISLRxBbCreditDefault = _FcIfCapOsmISLRxBbCreditDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 7),
    _FcIfCapOsmISLRxBbCreditDefault_Type()
)
fcIfCapOsmISLRxBbCreditDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmISLRxBbCreditDefault.setStatus("current")
_FcIfCapOsmRxPerfBufWriteable_Type = TruthValue
_FcIfCapOsmRxPerfBufWriteable_Object = MibTableColumn
fcIfCapOsmRxPerfBufWriteable = _FcIfCapOsmRxPerfBufWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 8),
    _FcIfCapOsmRxPerfBufWriteable_Type()
)
fcIfCapOsmRxPerfBufWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxPerfBufWriteable.setStatus("current")
_FcIfCapOsmRxPerfBufMax_Type = FcPerfBuffer
_FcIfCapOsmRxPerfBufMax_Object = MibTableColumn
fcIfCapOsmRxPerfBufMax = _FcIfCapOsmRxPerfBufMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 9),
    _FcIfCapOsmRxPerfBufMax_Type()
)
fcIfCapOsmRxPerfBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxPerfBufMax.setStatus("current")
_FcIfCapOsmRxPerfBufMin_Type = FcPerfBuffer
_FcIfCapOsmRxPerfBufMin_Object = MibTableColumn
fcIfCapOsmRxPerfBufMin = _FcIfCapOsmRxPerfBufMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 10),
    _FcIfCapOsmRxPerfBufMin_Type()
)
fcIfCapOsmRxPerfBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxPerfBufMin.setStatus("current")
_FcIfCapOsmRxPerfBufDefault_Type = FcPerfBuffer
_FcIfCapOsmRxPerfBufDefault_Object = MibTableColumn
fcIfCapOsmRxPerfBufDefault = _FcIfCapOsmRxPerfBufDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 11),
    _FcIfCapOsmRxPerfBufDefault_Type()
)
fcIfCapOsmRxPerfBufDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmRxPerfBufDefault.setStatus("current")
_FcIfCapOsmISLRxPerfBufMax_Type = FcPerfBuffer
_FcIfCapOsmISLRxPerfBufMax_Object = MibTableColumn
fcIfCapOsmISLRxPerfBufMax = _FcIfCapOsmISLRxPerfBufMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 12),
    _FcIfCapOsmISLRxPerfBufMax_Type()
)
fcIfCapOsmISLRxPerfBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmISLRxPerfBufMax.setStatus("current")
_FcIfCapOsmISLRxPerfBufMin_Type = FcPerfBuffer
_FcIfCapOsmISLRxPerfBufMin_Object = MibTableColumn
fcIfCapOsmISLRxPerfBufMin = _FcIfCapOsmISLRxPerfBufMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 13),
    _FcIfCapOsmISLRxPerfBufMin_Type()
)
fcIfCapOsmISLRxPerfBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmISLRxPerfBufMin.setStatus("current")
_FcIfCapOsmISLRxPerfBufDefault_Type = FcPerfBuffer
_FcIfCapOsmISLRxPerfBufDefault_Object = MibTableColumn
fcIfCapOsmISLRxPerfBufDefault = _FcIfCapOsmISLRxPerfBufDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 11, 1, 14),
    _FcIfCapOsmISLRxPerfBufDefault_Type()
)
fcIfCapOsmISLRxPerfBufDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapOsmISLRxPerfBufDefault.setStatus("current")
_FcIfCapFrmTable_Object = MibTable
fcIfCapFrmTable = _FcIfCapFrmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12)
)
if mibBuilder.loadTexts:
    fcIfCapFrmTable.setStatus("current")
_FcIfCapFrmEntry_Object = MibTableRow
fcIfCapFrmEntry = _FcIfCapFrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1)
)
fcIfCapFrmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfCapFrmEntry.setStatus("current")
_FcIfCapFrmRxBbCreditWriteable_Type = TruthValue
_FcIfCapFrmRxBbCreditWriteable_Object = MibTableColumn
fcIfCapFrmRxBbCreditWriteable = _FcIfCapFrmRxBbCreditWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 1),
    _FcIfCapFrmRxBbCreditWriteable_Type()
)
fcIfCapFrmRxBbCreditWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxBbCreditWriteable.setStatus("current")
_FcIfCapFrmRxBbCreditMax_Type = FcBbCredit
_FcIfCapFrmRxBbCreditMax_Object = MibTableColumn
fcIfCapFrmRxBbCreditMax = _FcIfCapFrmRxBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 2),
    _FcIfCapFrmRxBbCreditMax_Type()
)
fcIfCapFrmRxBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxBbCreditMax.setStatus("current")
_FcIfCapFrmRxBbCreditMin_Type = FcBbCredit
_FcIfCapFrmRxBbCreditMin_Object = MibTableColumn
fcIfCapFrmRxBbCreditMin = _FcIfCapFrmRxBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 3),
    _FcIfCapFrmRxBbCreditMin_Type()
)
fcIfCapFrmRxBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxBbCreditMin.setStatus("current")
_FcIfCapFrmRxBbCreditDefault_Type = FcBbCredit
_FcIfCapFrmRxBbCreditDefault_Object = MibTableColumn
fcIfCapFrmRxBbCreditDefault = _FcIfCapFrmRxBbCreditDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 4),
    _FcIfCapFrmRxBbCreditDefault_Type()
)
fcIfCapFrmRxBbCreditDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxBbCreditDefault.setStatus("current")
_FcIfCapFrmISLRxBbCreditMax_Type = FcBbCredit
_FcIfCapFrmISLRxBbCreditMax_Object = MibTableColumn
fcIfCapFrmISLRxBbCreditMax = _FcIfCapFrmISLRxBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 5),
    _FcIfCapFrmISLRxBbCreditMax_Type()
)
fcIfCapFrmISLRxBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmISLRxBbCreditMax.setStatus("current")
_FcIfCapFrmISLRxBbCreditMin_Type = FcBbCredit
_FcIfCapFrmISLRxBbCreditMin_Object = MibTableColumn
fcIfCapFrmISLRxBbCreditMin = _FcIfCapFrmISLRxBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 6),
    _FcIfCapFrmISLRxBbCreditMin_Type()
)
fcIfCapFrmISLRxBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmISLRxBbCreditMin.setStatus("current")
_FcIfCapFrmISLRxBbCreditDefault_Type = FcBbCredit
_FcIfCapFrmISLRxBbCreditDefault_Object = MibTableColumn
fcIfCapFrmISLRxBbCreditDefault = _FcIfCapFrmISLRxBbCreditDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 7),
    _FcIfCapFrmISLRxBbCreditDefault_Type()
)
fcIfCapFrmISLRxBbCreditDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmISLRxBbCreditDefault.setStatus("current")
_FcIfCapFrmRxPerfBufWriteable_Type = TruthValue
_FcIfCapFrmRxPerfBufWriteable_Object = MibTableColumn
fcIfCapFrmRxPerfBufWriteable = _FcIfCapFrmRxPerfBufWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 8),
    _FcIfCapFrmRxPerfBufWriteable_Type()
)
fcIfCapFrmRxPerfBufWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxPerfBufWriteable.setStatus("current")
_FcIfCapFrmRxPerfBufMax_Type = FcPerfBuffer
_FcIfCapFrmRxPerfBufMax_Object = MibTableColumn
fcIfCapFrmRxPerfBufMax = _FcIfCapFrmRxPerfBufMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 9),
    _FcIfCapFrmRxPerfBufMax_Type()
)
fcIfCapFrmRxPerfBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxPerfBufMax.setStatus("current")
_FcIfCapFrmRxPerfBufMin_Type = FcPerfBuffer
_FcIfCapFrmRxPerfBufMin_Object = MibTableColumn
fcIfCapFrmRxPerfBufMin = _FcIfCapFrmRxPerfBufMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 10),
    _FcIfCapFrmRxPerfBufMin_Type()
)
fcIfCapFrmRxPerfBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxPerfBufMin.setStatus("current")
_FcIfCapFrmRxPerfBufDefault_Type = FcPerfBuffer
_FcIfCapFrmRxPerfBufDefault_Object = MibTableColumn
fcIfCapFrmRxPerfBufDefault = _FcIfCapFrmRxPerfBufDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 11),
    _FcIfCapFrmRxPerfBufDefault_Type()
)
fcIfCapFrmRxPerfBufDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmRxPerfBufDefault.setStatus("current")
_FcIfCapFrmISLRxPerfBufMax_Type = FcPerfBuffer
_FcIfCapFrmISLRxPerfBufMax_Object = MibTableColumn
fcIfCapFrmISLRxPerfBufMax = _FcIfCapFrmISLRxPerfBufMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 12),
    _FcIfCapFrmISLRxPerfBufMax_Type()
)
fcIfCapFrmISLRxPerfBufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmISLRxPerfBufMax.setStatus("current")
_FcIfCapFrmISLRxPerfBufMin_Type = FcPerfBuffer
_FcIfCapFrmISLRxPerfBufMin_Object = MibTableColumn
fcIfCapFrmISLRxPerfBufMin = _FcIfCapFrmISLRxPerfBufMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 13),
    _FcIfCapFrmISLRxPerfBufMin_Type()
)
fcIfCapFrmISLRxPerfBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmISLRxPerfBufMin.setStatus("current")
_FcIfCapFrmISLRxPerfBufDefault_Type = FcPerfBuffer
_FcIfCapFrmISLRxPerfBufDefault_Object = MibTableColumn
fcIfCapFrmISLRxPerfBufDefault = _FcIfCapFrmISLRxPerfBufDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 12, 1, 14),
    _FcIfCapFrmISLRxPerfBufDefault_Type()
)
fcIfCapFrmISLRxPerfBufDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCapFrmISLRxPerfBufDefault.setStatus("current")
_FcIfRNIDInfoTable_Object = MibTable
fcIfRNIDInfoTable = _FcIfRNIDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fcIfRNIDInfoTable.setStatus("current")
_FcIfRNIDInfoEntry_Object = MibTableRow
fcIfRNIDInfoEntry = _FcIfRNIDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1)
)
fcIfRNIDInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fcIfRNIDInfoEntry.setStatus("current")


class _FcIfRNIDInfoStatus_Type(Integer32):
    """Custom type fcIfRNIDInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("old", 3),
          ("valid", 1))
    )


_FcIfRNIDInfoStatus_Type.__name__ = "Integer32"
_FcIfRNIDInfoStatus_Object = MibTableColumn
fcIfRNIDInfoStatus = _FcIfRNIDInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 1),
    _FcIfRNIDInfoStatus_Type()
)
fcIfRNIDInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfRNIDInfoStatus.setStatus("current")
_FcIfRNIDInfoTypeNumber_Type = SnmpAdminString
_FcIfRNIDInfoTypeNumber_Object = MibTableColumn
fcIfRNIDInfoTypeNumber = _FcIfRNIDInfoTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 2),
    _FcIfRNIDInfoTypeNumber_Type()
)
fcIfRNIDInfoTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoTypeNumber.setStatus("current")
_FcIfRNIDInfoModelNumber_Type = SnmpAdminString
_FcIfRNIDInfoModelNumber_Object = MibTableColumn
fcIfRNIDInfoModelNumber = _FcIfRNIDInfoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 3),
    _FcIfRNIDInfoModelNumber_Type()
)
fcIfRNIDInfoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoModelNumber.setStatus("current")
_FcIfRNIDInfoManufacturer_Type = SnmpAdminString
_FcIfRNIDInfoManufacturer_Object = MibTableColumn
fcIfRNIDInfoManufacturer = _FcIfRNIDInfoManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 4),
    _FcIfRNIDInfoManufacturer_Type()
)
fcIfRNIDInfoManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoManufacturer.setStatus("current")
_FcIfRNIDInfoPlantOfMfg_Type = SnmpAdminString
_FcIfRNIDInfoPlantOfMfg_Object = MibTableColumn
fcIfRNIDInfoPlantOfMfg = _FcIfRNIDInfoPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 5),
    _FcIfRNIDInfoPlantOfMfg_Type()
)
fcIfRNIDInfoPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoPlantOfMfg.setStatus("current")
_FcIfRNIDInfoSerialNumber_Type = SnmpAdminString
_FcIfRNIDInfoSerialNumber_Object = MibTableColumn
fcIfRNIDInfoSerialNumber = _FcIfRNIDInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 6),
    _FcIfRNIDInfoSerialNumber_Type()
)
fcIfRNIDInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoSerialNumber.setStatus("current")


class _FcIfRNIDInfoUnitType_Type(Integer32):
    """Custom type fcIfRNIDInfoUnitType based on Integer32"""
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
        *(("channel", 1),
          ("controlUnit", 2),
          ("fabric", 3),
          ("unknown", 4))
    )


_FcIfRNIDInfoUnitType_Type.__name__ = "Integer32"
_FcIfRNIDInfoUnitType_Object = MibTableColumn
fcIfRNIDInfoUnitType = _FcIfRNIDInfoUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 7),
    _FcIfRNIDInfoUnitType_Type()
)
fcIfRNIDInfoUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoUnitType.setStatus("current")


class _FcIfRNIDInfoPortId_Type(Integer32):
    """Custom type fcIfRNIDInfoPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcIfRNIDInfoPortId_Type.__name__ = "Integer32"
_FcIfRNIDInfoPortId_Object = MibTableColumn
fcIfRNIDInfoPortId = _FcIfRNIDInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 13, 1, 8),
    _FcIfRNIDInfoPortId_Type()
)
fcIfRNIDInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRNIDInfoPortId.setStatus("current")
_FcIfGigETable_Object = MibTable
fcIfGigETable = _FcIfGigETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 14)
)
if mibBuilder.loadTexts:
    fcIfGigETable.setStatus("current")
_FcIfGigEEntry_Object = MibTableRow
fcIfGigEEntry = _FcIfGigEEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 14, 1)
)
fcIfGigEEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfGigEEntry.setStatus("current")
_FcIfGigEPortChannelIfIndex_Type = InterfaceIndexOrZero
_FcIfGigEPortChannelIfIndex_Object = MibTableColumn
fcIfGigEPortChannelIfIndex = _FcIfGigEPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 14, 1, 1),
    _FcIfGigEPortChannelIfIndex_Type()
)
fcIfGigEPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfGigEPortChannelIfIndex.setStatus("current")


class _FcIfGigEAutoNegotiate_Type(Integer32):
    """Custom type fcIfGigEAutoNegotiate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FcIfGigEAutoNegotiate_Type.__name__ = "Integer32"
_FcIfGigEAutoNegotiate_Object = MibTableColumn
fcIfGigEAutoNegotiate = _FcIfGigEAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 14, 1, 2),
    _FcIfGigEAutoNegotiate_Type()
)
fcIfGigEAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfGigEAutoNegotiate.setStatus("current")


class _FcIfGigEBeaconMode_Type(TruthValue):
    """Custom type fcIfGigEBeaconMode based on TruthValue"""


_FcIfGigEBeaconMode_Object = MibTableColumn
fcIfGigEBeaconMode = _FcIfGigEBeaconMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 14, 1, 3),
    _FcIfGigEBeaconMode_Type()
)
fcIfGigEBeaconMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfGigEBeaconMode.setStatus("current")
_FcIfGigConnectorType_Type = FcPortModuleTypes
_FcIfGigConnectorType_Object = MibTableColumn
fcIfGigConnectorType = _FcIfGigConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 14, 1, 4),
    _FcIfGigConnectorType_Type()
)
fcIfGigConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfGigConnectorType.setStatus("current")
_FcIfModuleTable_Object = MibTable
fcIfModuleTable = _FcIfModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fcIfModuleTable.setStatus("current")
_FcIfModuleEntry_Object = MibTableRow
fcIfModuleEntry = _FcIfModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 15, 1)
)
fcIfModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fcIfModuleEntry.setStatus("current")


class _FcIfModuleOverSubscriptionRatioConfig_Type(Integer32):
    """Custom type fcIfModuleOverSubscriptionRatioConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FcIfModuleOverSubscriptionRatioConfig_Type.__name__ = "Integer32"
_FcIfModuleOverSubscriptionRatioConfig_Object = MibTableColumn
fcIfModuleOverSubscriptionRatioConfig = _FcIfModuleOverSubscriptionRatioConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 15, 1, 1),
    _FcIfModuleOverSubscriptionRatioConfig_Type()
)
fcIfModuleOverSubscriptionRatioConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfModuleOverSubscriptionRatioConfig.setStatus("current")


class _FcIfModuleBandwidthFairnessConfig_Type(Integer32):
    """Custom type fcIfModuleBandwidthFairnessConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FcIfModuleBandwidthFairnessConfig_Type.__name__ = "Integer32"
_FcIfModuleBandwidthFairnessConfig_Object = MibTableColumn
fcIfModuleBandwidthFairnessConfig = _FcIfModuleBandwidthFairnessConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 15, 1, 2),
    _FcIfModuleBandwidthFairnessConfig_Type()
)
fcIfModuleBandwidthFairnessConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfModuleBandwidthFairnessConfig.setStatus("current")


class _FcIfModuleBandwidthFairnessOper_Type(Integer32):
    """Custom type fcIfModuleBandwidthFairnessOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FcIfModuleBandwidthFairnessOper_Type.__name__ = "Integer32"
_FcIfModuleBandwidthFairnessOper_Object = MibTableColumn
fcIfModuleBandwidthFairnessOper = _FcIfModuleBandwidthFairnessOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 15, 1, 3),
    _FcIfModuleBandwidthFairnessOper_Type()
)
fcIfModuleBandwidthFairnessOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfModuleBandwidthFairnessOper.setStatus("current")


class _FcIfModuleXcvrFrequencyConfig_Type(Integer32):
    """Custom type fcIfModuleXcvrFrequencyConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("xcvrFreqX2Eth", 3),
          ("xcvrFreqX2FC", 2))
    )


_FcIfModuleXcvrFrequencyConfig_Type.__name__ = "Integer32"
_FcIfModuleXcvrFrequencyConfig_Object = MibTableColumn
fcIfModuleXcvrFrequencyConfig = _FcIfModuleXcvrFrequencyConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 15, 1, 4),
    _FcIfModuleXcvrFrequencyConfig_Type()
)
fcIfModuleXcvrFrequencyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfModuleXcvrFrequencyConfig.setStatus("current")
_FcIfToggleCtrlConfigTable_Object = MibTable
fcIfToggleCtrlConfigTable = _FcIfToggleCtrlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 16)
)
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigTable.setStatus("deprecated")
_FcIfToggleCtrlConfigEntry_Object = MibTableRow
fcIfToggleCtrlConfigEntry = _FcIfToggleCtrlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 16, 1)
)
fcIfToggleCtrlConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigEntry.setStatus("deprecated")
_FcIfToggleCtrlConfigEnable_Type = TruthValue
_FcIfToggleCtrlConfigEnable_Object = MibTableColumn
fcIfToggleCtrlConfigEnable = _FcIfToggleCtrlConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 16, 1, 1),
    _FcIfToggleCtrlConfigEnable_Type()
)
fcIfToggleCtrlConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigEnable.setStatus("deprecated")


class _FcIfToggleCtrlConfigReason_Type(Integer32):
    """Custom type fcIfToggleCtrlConfigReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkFailure", 2),
          ("notApplicable", 1))
    )


_FcIfToggleCtrlConfigReason_Type.__name__ = "Integer32"
_FcIfToggleCtrlConfigReason_Object = MibTableColumn
fcIfToggleCtrlConfigReason = _FcIfToggleCtrlConfigReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 16, 1, 2),
    _FcIfToggleCtrlConfigReason_Type()
)
fcIfToggleCtrlConfigReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigReason.setStatus("deprecated")


class _FcIfToggleCtrlConfigDuration_Type(Unsigned32):
    """Custom type fcIfToggleCtrlConfigDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_FcIfToggleCtrlConfigDuration_Type.__name__ = "Unsigned32"
_FcIfToggleCtrlConfigDuration_Object = MibTableColumn
fcIfToggleCtrlConfigDuration = _FcIfToggleCtrlConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 16, 1, 3),
    _FcIfToggleCtrlConfigDuration_Type()
)
fcIfToggleCtrlConfigDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigDuration.setStatus("deprecated")
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigDuration.setUnits("seconds")


class _FcIfToggleCtrlConfigNumFlaps_Type(Unsigned32):
    """Custom type fcIfToggleCtrlConfigNumFlaps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_FcIfToggleCtrlConfigNumFlaps_Type.__name__ = "Unsigned32"
_FcIfToggleCtrlConfigNumFlaps_Object = MibTableColumn
fcIfToggleCtrlConfigNumFlaps = _FcIfToggleCtrlConfigNumFlaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 16, 1, 4),
    _FcIfToggleCtrlConfigNumFlaps_Type()
)
fcIfToggleCtrlConfigNumFlaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigNumFlaps.setStatus("deprecated")
_FcIfFlapCtrlConfigTable_Object = MibTable
fcIfFlapCtrlConfigTable = _FcIfFlapCtrlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 17)
)
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigTable.setStatus("current")
_FcIfFlapCtrlConfigEntry_Object = MibTableRow
fcIfFlapCtrlConfigEntry = _FcIfFlapCtrlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 17, 1)
)
fcIfFlapCtrlConfigEntry.setIndexNames(
    (0, "CISCO-FC-FE-MIB", "fcIfFlapCtrlConfigReason"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigEntry.setStatus("current")


class _FcIfFlapCtrlConfigReason_Type(Integer32):
    """Custom type fcIfFlapCtrlConfigReason based on Integer32"""
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
        *(("bitErrorRate", 3),
          ("creditLoss", 7),
          ("linkFailure", 1),
          ("linkReset", 6),
          ("signalLoss", 4),
          ("syncLoss", 5),
          ("trustSecViolation", 2))
    )


_FcIfFlapCtrlConfigReason_Type.__name__ = "Integer32"
_FcIfFlapCtrlConfigReason_Object = MibTableColumn
fcIfFlapCtrlConfigReason = _FcIfFlapCtrlConfigReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 17, 1, 1),
    _FcIfFlapCtrlConfigReason_Type()
)
fcIfFlapCtrlConfigReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigReason.setStatus("current")
_FcIfFlapCtrlConfigEnable_Type = TruthValue
_FcIfFlapCtrlConfigEnable_Object = MibTableColumn
fcIfFlapCtrlConfigEnable = _FcIfFlapCtrlConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 17, 1, 2),
    _FcIfFlapCtrlConfigEnable_Type()
)
fcIfFlapCtrlConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigEnable.setStatus("current")


class _FcIfFlapCtrlConfigDuration_Type(Unsigned32):
    """Custom type fcIfFlapCtrlConfigDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_FcIfFlapCtrlConfigDuration_Type.__name__ = "Unsigned32"
_FcIfFlapCtrlConfigDuration_Object = MibTableColumn
fcIfFlapCtrlConfigDuration = _FcIfFlapCtrlConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 17, 1, 3),
    _FcIfFlapCtrlConfigDuration_Type()
)
fcIfFlapCtrlConfigDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigDuration.setStatus("current")
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigDuration.setUnits("seconds")


class _FcIfFlapCtrlConfigNumFlaps_Type(Unsigned32):
    """Custom type fcIfFlapCtrlConfigNumFlaps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_FcIfFlapCtrlConfigNumFlaps_Type.__name__ = "Unsigned32"
_FcIfFlapCtrlConfigNumFlaps_Object = MibTableColumn
fcIfFlapCtrlConfigNumFlaps = _FcIfFlapCtrlConfigNumFlaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 1, 17, 1, 4),
    _FcIfFlapCtrlConfigNumFlaps_Type()
)
fcIfFlapCtrlConfigNumFlaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigNumFlaps.setStatus("current")
_CffFcFeStatistics_ObjectIdentity = ObjectIdentity
cffFcFeStatistics = _CffFcFeStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2)
)
_FcIfErrorTable_Object = MibTable
fcIfErrorTable = _FcIfErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcIfErrorTable.setStatus("current")
_FcIfErrorEntry_Object = MibTableRow
fcIfErrorEntry = _FcIfErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1)
)
fcIfErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfErrorEntry.setStatus("current")
_FcIfLinkFailures_Type = Counter32
_FcIfLinkFailures_Object = MibTableColumn
fcIfLinkFailures = _FcIfLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 1),
    _FcIfLinkFailures_Type()
)
fcIfLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLinkFailures.setStatus("current")
_FcIfSyncLosses_Type = Counter32
_FcIfSyncLosses_Object = MibTableColumn
fcIfSyncLosses = _FcIfSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 2),
    _FcIfSyncLosses_Type()
)
fcIfSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfSyncLosses.setStatus("current")
_FcIfSigLosses_Type = Counter32
_FcIfSigLosses_Object = MibTableColumn
fcIfSigLosses = _FcIfSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 3),
    _FcIfSigLosses_Type()
)
fcIfSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfSigLosses.setStatus("current")
_FcIfPrimSeqProtoErrors_Type = Counter32
_FcIfPrimSeqProtoErrors_Object = MibTableColumn
fcIfPrimSeqProtoErrors = _FcIfPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 4),
    _FcIfPrimSeqProtoErrors_Type()
)
fcIfPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfPrimSeqProtoErrors.setStatus("current")
_FcIfInvalidTxWords_Type = Counter32
_FcIfInvalidTxWords_Object = MibTableColumn
fcIfInvalidTxWords = _FcIfInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 5),
    _FcIfInvalidTxWords_Type()
)
fcIfInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfInvalidTxWords.setStatus("current")
_FcIfInvalidCrcs_Type = Counter32
_FcIfInvalidCrcs_Object = MibTableColumn
fcIfInvalidCrcs = _FcIfInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 6),
    _FcIfInvalidCrcs_Type()
)
fcIfInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfInvalidCrcs.setStatus("current")
_FcIfDelimiterErrors_Type = Counter32
_FcIfDelimiterErrors_Object = MibTableColumn
fcIfDelimiterErrors = _FcIfDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 7),
    _FcIfDelimiterErrors_Type()
)
fcIfDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfDelimiterErrors.setStatus("current")
_FcIfAddressIdErrors_Type = Counter32
_FcIfAddressIdErrors_Object = MibTableColumn
fcIfAddressIdErrors = _FcIfAddressIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 8),
    _FcIfAddressIdErrors_Type()
)
fcIfAddressIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfAddressIdErrors.setStatus("current")
_FcIfLinkResetIns_Type = Counter32
_FcIfLinkResetIns_Object = MibTableColumn
fcIfLinkResetIns = _FcIfLinkResetIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 9),
    _FcIfLinkResetIns_Type()
)
fcIfLinkResetIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLinkResetIns.setStatus("current")
_FcIfLinkResetOuts_Type = Counter32
_FcIfLinkResetOuts_Object = MibTableColumn
fcIfLinkResetOuts = _FcIfLinkResetOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 10),
    _FcIfLinkResetOuts_Type()
)
fcIfLinkResetOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLinkResetOuts.setStatus("current")
_FcIfOlsIns_Type = Counter32
_FcIfOlsIns_Object = MibTableColumn
fcIfOlsIns = _FcIfOlsIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 11),
    _FcIfOlsIns_Type()
)
fcIfOlsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOlsIns.setStatus("current")
_FcIfOlsOuts_Type = Counter32
_FcIfOlsOuts_Object = MibTableColumn
fcIfOlsOuts = _FcIfOlsOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 12),
    _FcIfOlsOuts_Type()
)
fcIfOlsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOlsOuts.setStatus("current")
_FcIfRuntFramesIn_Type = Counter32
_FcIfRuntFramesIn_Object = MibTableColumn
fcIfRuntFramesIn = _FcIfRuntFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 13),
    _FcIfRuntFramesIn_Type()
)
fcIfRuntFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRuntFramesIn.setStatus("current")
_FcIfJabberFramesIn_Type = Counter32
_FcIfJabberFramesIn_Object = MibTableColumn
fcIfJabberFramesIn = _FcIfJabberFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 14),
    _FcIfJabberFramesIn_Type()
)
fcIfJabberFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfJabberFramesIn.setStatus("current")
_FcIfTxWaitCount_Type = Counter32
_FcIfTxWaitCount_Object = MibTableColumn
fcIfTxWaitCount = _FcIfTxWaitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 15),
    _FcIfTxWaitCount_Type()
)
fcIfTxWaitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfTxWaitCount.setStatus("current")
_FcIfFramesTooLong_Type = Counter32
_FcIfFramesTooLong_Object = MibTableColumn
fcIfFramesTooLong = _FcIfFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 16),
    _FcIfFramesTooLong_Type()
)
fcIfFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFramesTooLong.setStatus("current")
_FcIfFramesTooShort_Type = Counter32
_FcIfFramesTooShort_Object = MibTableColumn
fcIfFramesTooShort = _FcIfFramesTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 17),
    _FcIfFramesTooShort_Type()
)
fcIfFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFramesTooShort.setStatus("current")
_FcIfLRRIn_Type = Counter32
_FcIfLRRIn_Object = MibTableColumn
fcIfLRRIn = _FcIfLRRIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 18),
    _FcIfLRRIn_Type()
)
fcIfLRRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLRRIn.setStatus("current")
_FcIfLRROut_Type = Counter32
_FcIfLRROut_Object = MibTableColumn
fcIfLRROut = _FcIfLRROut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 19),
    _FcIfLRROut_Type()
)
fcIfLRROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLRROut.setStatus("current")
_FcIfNOSIn_Type = Counter32
_FcIfNOSIn_Object = MibTableColumn
fcIfNOSIn = _FcIfNOSIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 20),
    _FcIfNOSIn_Type()
)
fcIfNOSIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNOSIn.setStatus("current")
_FcIfNOSOut_Type = Counter32
_FcIfNOSOut_Object = MibTableColumn
fcIfNOSOut = _FcIfNOSOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 21),
    _FcIfNOSOut_Type()
)
fcIfNOSOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNOSOut.setStatus("current")
_FcIfFragFrames_Type = Counter32
_FcIfFragFrames_Object = MibTableColumn
fcIfFragFrames = _FcIfFragFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 22),
    _FcIfFragFrames_Type()
)
fcIfFragFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFragFrames.setStatus("current")
_FcIfEOFaFrames_Type = Counter32
_FcIfEOFaFrames_Object = MibTableColumn
fcIfEOFaFrames = _FcIfEOFaFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 23),
    _FcIfEOFaFrames_Type()
)
fcIfEOFaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfEOFaFrames.setStatus("current")
_FcIfUnknownClassFrames_Type = Counter32
_FcIfUnknownClassFrames_Object = MibTableColumn
fcIfUnknownClassFrames = _FcIfUnknownClassFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 24),
    _FcIfUnknownClassFrames_Type()
)
fcIfUnknownClassFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfUnknownClassFrames.setStatus("current")
_FcIf8b10bDisparityErrors_Type = Counter32
_FcIf8b10bDisparityErrors_Object = MibTableColumn
fcIf8b10bDisparityErrors = _FcIf8b10bDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 25),
    _FcIf8b10bDisparityErrors_Type()
)
fcIf8b10bDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIf8b10bDisparityErrors.setStatus("current")
_FcIfFramesDiscard_Type = Counter32
_FcIfFramesDiscard_Object = MibTableColumn
fcIfFramesDiscard = _FcIfFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 26),
    _FcIfFramesDiscard_Type()
)
fcIfFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFramesDiscard.setStatus("current")
_FcIfELPFailures_Type = Counter32
_FcIfELPFailures_Object = MibTableColumn
fcIfELPFailures = _FcIfELPFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 27),
    _FcIfELPFailures_Type()
)
fcIfELPFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfELPFailures.setStatus("current")
_FcIfBBCreditTransistionFromZero_Type = Counter32
_FcIfBBCreditTransistionFromZero_Object = MibTableColumn
fcIfBBCreditTransistionFromZero = _FcIfBBCreditTransistionFromZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 28),
    _FcIfBBCreditTransistionFromZero_Type()
)
fcIfBBCreditTransistionFromZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfBBCreditTransistionFromZero.setStatus("current")
_FcIfEISLFramesDiscard_Type = Counter32
_FcIfEISLFramesDiscard_Object = MibTableColumn
fcIfEISLFramesDiscard = _FcIfEISLFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 29),
    _FcIfEISLFramesDiscard_Type()
)
fcIfEISLFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfEISLFramesDiscard.setStatus("current")
_FcIfFramingErrorFrames_Type = Counter32
_FcIfFramingErrorFrames_Object = MibTableColumn
fcIfFramingErrorFrames = _FcIfFramingErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 30),
    _FcIfFramingErrorFrames_Type()
)
fcIfFramingErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFramingErrorFrames.setStatus("current")
_FcIfLipF8In_Type = Counter32
_FcIfLipF8In_Object = MibTableColumn
fcIfLipF8In = _FcIfLipF8In_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 31),
    _FcIfLipF8In_Type()
)
fcIfLipF8In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLipF8In.setStatus("current")
_FcIfLipF8Out_Type = Counter32
_FcIfLipF8Out_Object = MibTableColumn
fcIfLipF8Out = _FcIfLipF8Out_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 32),
    _FcIfLipF8Out_Type()
)
fcIfLipF8Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLipF8Out.setStatus("current")
_FcIfNonLipF8In_Type = Counter32
_FcIfNonLipF8In_Object = MibTableColumn
fcIfNonLipF8In = _FcIfNonLipF8In_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 33),
    _FcIfNonLipF8In_Type()
)
fcIfNonLipF8In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNonLipF8In.setStatus("current")
_FcIfNonLipF8Out_Type = Counter32
_FcIfNonLipF8Out_Object = MibTableColumn
fcIfNonLipF8Out = _FcIfNonLipF8Out_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 34),
    _FcIfNonLipF8Out_Type()
)
fcIfNonLipF8Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfNonLipF8Out.setStatus("current")
_FcIfTimeOutDiscards_Type = Counter64
_FcIfTimeOutDiscards_Object = MibTableColumn
fcIfTimeOutDiscards = _FcIfTimeOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 35),
    _FcIfTimeOutDiscards_Type()
)
fcIfTimeOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfTimeOutDiscards.setStatus("current")
_FcIfOutDiscards_Type = Counter64
_FcIfOutDiscards_Object = MibTableColumn
fcIfOutDiscards = _FcIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 36),
    _FcIfOutDiscards_Type()
)
fcIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOutDiscards.setStatus("current")
_FcIfCreditLoss_Type = Counter64
_FcIfCreditLoss_Object = MibTableColumn
fcIfCreditLoss = _FcIfCreditLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 37),
    _FcIfCreditLoss_Type()
)
fcIfCreditLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCreditLoss.setStatus("current")
_FcIfTxWtAvgBBCreditTransitionToZero_Type = Counter64
_FcIfTxWtAvgBBCreditTransitionToZero_Object = MibTableColumn
fcIfTxWtAvgBBCreditTransitionToZero = _FcIfTxWtAvgBBCreditTransitionToZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 38),
    _FcIfTxWtAvgBBCreditTransitionToZero_Type()
)
fcIfTxWtAvgBBCreditTransitionToZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfTxWtAvgBBCreditTransitionToZero.setStatus("current")
_FcIfBBCreditTransistionToZero_Type = Counter32
_FcIfBBCreditTransistionToZero_Object = MibTableColumn
fcIfBBCreditTransistionToZero = _FcIfBBCreditTransistionToZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 39),
    _FcIfBBCreditTransistionToZero_Type()
)
fcIfBBCreditTransistionToZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfBBCreditTransistionToZero.setStatus("current")
_FcHCIfBBCreditTransistionFromZero_Type = Counter64
_FcHCIfBBCreditTransistionFromZero_Object = MibTableColumn
fcHCIfBBCreditTransistionFromZero = _FcHCIfBBCreditTransistionFromZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 40),
    _FcHCIfBBCreditTransistionFromZero_Type()
)
fcHCIfBBCreditTransistionFromZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcHCIfBBCreditTransistionFromZero.setStatus("current")
_FcHCIfBBCreditTransistionToZero_Type = Counter64
_FcHCIfBBCreditTransistionToZero_Object = MibTableColumn
fcHCIfBBCreditTransistionToZero = _FcHCIfBBCreditTransistionToZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 41),
    _FcHCIfBBCreditTransistionToZero_Type()
)
fcHCIfBBCreditTransistionToZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcHCIfBBCreditTransistionToZero.setStatus("current")
_FcIfFECCorrectedBlks_Type = Counter64
_FcIfFECCorrectedBlks_Object = MibTableColumn
fcIfFECCorrectedBlks = _FcIfFECCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 42),
    _FcIfFECCorrectedBlks_Type()
)
fcIfFECCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFECCorrectedBlks.setStatus("current")
_FcIfFECUncorrectedBlks_Type = Counter64
_FcIfFECUncorrectedBlks_Object = MibTableColumn
fcIfFECUncorrectedBlks = _FcIfFECUncorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 1, 1, 43),
    _FcIfFECUncorrectedBlks_Type()
)
fcIfFECUncorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFECUncorrectedBlks.setStatus("current")
_FcIfC2AccountingTable_Object = MibTable
fcIfC2AccountingTable = _FcIfC2AccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fcIfC2AccountingTable.setStatus("current")
_FcIfC2AccountingEntry_Object = MibTableRow
fcIfC2AccountingEntry = _FcIfC2AccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1)
)
fcIfC2AccountingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfC2AccountingEntry.setStatus("current")
_FcIfC2InFrames_Type = Counter64
_FcIfC2InFrames_Object = MibTableColumn
fcIfC2InFrames = _FcIfC2InFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 1),
    _FcIfC2InFrames_Type()
)
fcIfC2InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2InFrames.setStatus("current")
_FcIfC2OutFrames_Type = Counter64
_FcIfC2OutFrames_Object = MibTableColumn
fcIfC2OutFrames = _FcIfC2OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 2),
    _FcIfC2OutFrames_Type()
)
fcIfC2OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2OutFrames.setStatus("current")
_FcIfC2InOctets_Type = Counter64
_FcIfC2InOctets_Object = MibTableColumn
fcIfC2InOctets = _FcIfC2InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 3),
    _FcIfC2InOctets_Type()
)
fcIfC2InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2InOctets.setStatus("current")
_FcIfC2OutOctets_Type = Counter64
_FcIfC2OutOctets_Object = MibTableColumn
fcIfC2OutOctets = _FcIfC2OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 4),
    _FcIfC2OutOctets_Type()
)
fcIfC2OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2OutOctets.setStatus("current")
_FcIfC2Discards_Type = Counter32
_FcIfC2Discards_Object = MibTableColumn
fcIfC2Discards = _FcIfC2Discards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 5),
    _FcIfC2Discards_Type()
)
fcIfC2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2Discards.setStatus("current")
_FcIfC2FbsyFrames_Type = Counter32
_FcIfC2FbsyFrames_Object = MibTableColumn
fcIfC2FbsyFrames = _FcIfC2FbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 6),
    _FcIfC2FbsyFrames_Type()
)
fcIfC2FbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2FbsyFrames.setStatus("current")
_FcIfC2FrjtFrames_Type = Counter32
_FcIfC2FrjtFrames_Object = MibTableColumn
fcIfC2FrjtFrames = _FcIfC2FrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 7),
    _FcIfC2FrjtFrames_Type()
)
fcIfC2FrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2FrjtFrames.setStatus("current")
_FcIfC2PBSYFrames_Type = Counter32
_FcIfC2PBSYFrames_Object = MibTableColumn
fcIfC2PBSYFrames = _FcIfC2PBSYFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 8),
    _FcIfC2PBSYFrames_Type()
)
fcIfC2PBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2PBSYFrames.setStatus("current")
_FcIfC2PRJTFrames_Type = Counter32
_FcIfC2PRJTFrames_Object = MibTableColumn
fcIfC2PRJTFrames = _FcIfC2PRJTFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 2, 1, 9),
    _FcIfC2PRJTFrames_Type()
)
fcIfC2PRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC2PRJTFrames.setStatus("current")
_FcIfC3AccountingTable_Object = MibTable
fcIfC3AccountingTable = _FcIfC3AccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fcIfC3AccountingTable.setStatus("current")
_FcIfC3AccountingEntry_Object = MibTableRow
fcIfC3AccountingEntry = _FcIfC3AccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3, 1)
)
fcIfC3AccountingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfC3AccountingEntry.setStatus("current")
_FcIfC3InFrames_Type = Counter64
_FcIfC3InFrames_Object = MibTableColumn
fcIfC3InFrames = _FcIfC3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3, 1, 1),
    _FcIfC3InFrames_Type()
)
fcIfC3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC3InFrames.setStatus("current")
_FcIfC3OutFrames_Type = Counter64
_FcIfC3OutFrames_Object = MibTableColumn
fcIfC3OutFrames = _FcIfC3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3, 1, 2),
    _FcIfC3OutFrames_Type()
)
fcIfC3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC3OutFrames.setStatus("current")
_FcIfC3InOctets_Type = Counter64
_FcIfC3InOctets_Object = MibTableColumn
fcIfC3InOctets = _FcIfC3InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3, 1, 3),
    _FcIfC3InOctets_Type()
)
fcIfC3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC3InOctets.setStatus("current")
_FcIfC3OutOctets_Type = Counter64
_FcIfC3OutOctets_Object = MibTableColumn
fcIfC3OutOctets = _FcIfC3OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3, 1, 4),
    _FcIfC3OutOctets_Type()
)
fcIfC3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC3OutOctets.setStatus("current")
_FcIfC3Discards_Type = Counter32
_FcIfC3Discards_Object = MibTableColumn
fcIfC3Discards = _FcIfC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 3, 1, 5),
    _FcIfC3Discards_Type()
)
fcIfC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfC3Discards.setStatus("current")
_FcIfCfAccountingTable_Object = MibTable
fcIfCfAccountingTable = _FcIfCfAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fcIfCfAccountingTable.setStatus("current")
_FcIfCfAccountingEntry_Object = MibTableRow
fcIfCfAccountingEntry = _FcIfCfAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4, 1)
)
fcIfCfAccountingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfCfAccountingEntry.setStatus("current")
_FcIfCfInFrames_Type = Counter64
_FcIfCfInFrames_Object = MibTableColumn
fcIfCfInFrames = _FcIfCfInFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4, 1, 1),
    _FcIfCfInFrames_Type()
)
fcIfCfInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCfInFrames.setStatus("current")
_FcIfCfOutFrames_Type = Counter64
_FcIfCfOutFrames_Object = MibTableColumn
fcIfCfOutFrames = _FcIfCfOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4, 1, 2),
    _FcIfCfOutFrames_Type()
)
fcIfCfOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCfOutFrames.setStatus("current")
_FcIfCfInOctets_Type = Counter64
_FcIfCfInOctets_Object = MibTableColumn
fcIfCfInOctets = _FcIfCfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4, 1, 3),
    _FcIfCfInOctets_Type()
)
fcIfCfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCfInOctets.setStatus("current")
_FcIfCfOutOctets_Type = Counter64
_FcIfCfOutOctets_Object = MibTableColumn
fcIfCfOutOctets = _FcIfCfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4, 1, 4),
    _FcIfCfOutOctets_Type()
)
fcIfCfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCfOutOctets.setStatus("current")
_FcIfCfDiscards_Type = Counter32
_FcIfCfDiscards_Object = MibTableColumn
fcIfCfDiscards = _FcIfCfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 4, 1, 5),
    _FcIfCfDiscards_Type()
)
fcIfCfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCfDiscards.setStatus("current")
_FcIfStatTable_Object = MibTable
fcIfStatTable = _FcIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fcIfStatTable.setStatus("current")
_FcIfStatEntry_Object = MibTableRow
fcIfStatEntry = _FcIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 5, 1)
)
fcIfStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcIfStatEntry.setStatus("current")
_FcIfCurrRxBbCredit_Type = FcBbCredit
_FcIfCurrRxBbCredit_Object = MibTableColumn
fcIfCurrRxBbCredit = _FcIfCurrRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 5, 1, 1),
    _FcIfCurrRxBbCredit_Type()
)
fcIfCurrRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCurrRxBbCredit.setStatus("current")
_FcIfCurrTxBbCredit_Type = FcBbCredit
_FcIfCurrTxBbCredit_Object = MibTableColumn
fcIfCurrTxBbCredit = _FcIfCurrTxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 2, 5, 1, 2),
    _FcIfCurrTxBbCredit_Type()
)
fcIfCurrTxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfCurrTxBbCredit.setStatus("current")
_CffFcFeNotification_ObjectIdentity = ObjectIdentity
cffFcFeNotification = _CffFcFeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3)
)
_CffFcFeNotifications_ObjectIdentity = ObjectIdentity
cffFcFeNotifications = _CffFcFeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3, 0)
)
_CffFcFeMIBConformance_ObjectIdentity = ObjectIdentity
cffFcFeMIBConformance = _CffFcFeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2)
)
_CffFcFeMIBCompliances_ObjectIdentity = ObjectIdentity
cffFcFeMIBCompliances = _CffFcFeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1)
)
_CffFcFeMIBGroups_ObjectIdentity = ObjectIdentity
cffFcFeMIBGroups = _CffFcFeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2)
)

# Managed Objects groups

fcFeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 1)
)
fcFeGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "cffFcFeElementName"),
        ("CISCO-FC-FE-MIB", "adminTrunkProtocol"),
        ("CISCO-FC-FE-MIB", "fcIfElpRejectReasonCode"),
        ("CISCO-FC-FE-MIB", "fcIfElpRejectReasonCodeExpl"))
)
if mibBuilder.loadTexts:
    fcFeGroup.setStatus("current")

fcIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 2)
)
fcIfGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfWwn"),
        ("CISCO-FC-FE-MIB", "fcIfAdminMode"),
        ("CISCO-FC-FE-MIB", "fcIfOperMode"),
        ("CISCO-FC-FE-MIB", "fcIfAdminSpeed"),
        ("CISCO-FC-FE-MIB", "fcIfBeaconMode"),
        ("CISCO-FC-FE-MIB", "fcIfPortChannelIfIndex"),
        ("CISCO-FC-FE-MIB", "fcIfOperStatusCause"),
        ("CISCO-FC-FE-MIB", "fcIfOperStatusCauseDescr"),
        ("CISCO-FC-FE-MIB", "fcIfAdminTrunkMode"),
        ("CISCO-FC-FE-MIB", "fcIfOperTrunkMode"),
        ("CISCO-FC-FE-MIB", "fcIfAllowedVsanList2k"),
        ("CISCO-FC-FE-MIB", "fcIfAllowedVsanList4k"),
        ("CISCO-FC-FE-MIB", "fcIfActiveVsanList2k"),
        ("CISCO-FC-FE-MIB", "fcIfActiveVsanList4k"),
        ("CISCO-FC-FE-MIB", "fcIfBbCreditModel"),
        ("CISCO-FC-FE-MIB", "fcIfHoldTime"),
        ("CISCO-FC-FE-MIB", "fcIfTransmitterType"),
        ("CISCO-FC-FE-MIB", "fcIfConnectorType"),
        ("CISCO-FC-FE-MIB", "fcIfSerialNo"),
        ("CISCO-FC-FE-MIB", "fcIfRevision"),
        ("CISCO-FC-FE-MIB", "fcIfVendor"),
        ("CISCO-FC-FE-MIB", "fcIfSFPSerialIDData"),
        ("CISCO-FC-FE-MIB", "fcIfPartNumber"),
        ("CISCO-FC-FE-MIB", "fcIfAdminRxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfAdminRxBbCreditModeISL"),
        ("CISCO-FC-FE-MIB", "fcIfAdminRxBbCreditModeFx"),
        ("CISCO-FC-FE-MIB", "fcIfOperRxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfRxDataFieldSize"))
)
if mibBuilder.loadTexts:
    fcIfGroup.setStatus("current")

fcTrunkIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 3)
)
fcTrunkIfGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcTrunkIfOperStatus"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfOperStatusCause"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfOperStatusCauseDescr"))
)
if mibBuilder.loadTexts:
    fcTrunkIfGroup.setStatus("current")

fcIfLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 4)
)
fcIfLoginGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfLoginEntryCount"),
        ("CISCO-FC-FE-MIB", "fcIfNxPortNodeName"),
        ("CISCO-FC-FE-MIB", "fcIfNxPortName"),
        ("CISCO-FC-FE-MIB", "fcIfNxPortAddress"),
        ("CISCO-FC-FE-MIB", "fcIfNxFcphVersionAgreed"),
        ("CISCO-FC-FE-MIB", "fcIfNxRxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfNxTxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfNxClass2RxDataFieldSize"),
        ("CISCO-FC-FE-MIB", "fcIfNxClass3RxDataFieldSize"),
        ("CISCO-FC-FE-MIB", "fcIfNxCosSuppAgreed"),
        ("CISCO-FC-FE-MIB", "fcIfNxClass2SeqDelivAgreed"),
        ("CISCO-FC-FE-MIB", "fcIfNxClass3SeqDelivAgreed"))
)
if mibBuilder.loadTexts:
    fcIfLoginGroup.setStatus("current")

fcIfElpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 5)
)
fcIfElpGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfElpNbrNodeName"),
        ("CISCO-FC-FE-MIB", "fcIfElpNbrPortName"),
        ("CISCO-FC-FE-MIB", "fcIfElpRxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfElpTxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfElpCosSuppAgreed"),
        ("CISCO-FC-FE-MIB", "fcIfElpClass2SeqDelivAgreed"),
        ("CISCO-FC-FE-MIB", "fcIfElpClass2RxDataFieldSize"),
        ("CISCO-FC-FE-MIB", "fcIfElpClass3SeqDelivAgreed"),
        ("CISCO-FC-FE-MIB", "fcIfElpClass3RxDataFieldSize"),
        ("CISCO-FC-FE-MIB", "fcIfElpClassFXII"),
        ("CISCO-FC-FE-MIB", "fcIfElpClassFRxDataFieldSize"),
        ("CISCO-FC-FE-MIB", "fcIfElpClassFConcurrentSeq"),
        ("CISCO-FC-FE-MIB", "fcIfElpClassFEndToEndCredit"),
        ("CISCO-FC-FE-MIB", "fcIfElpClassFOpenSeq"))
)
if mibBuilder.loadTexts:
    fcIfElpGroup.setStatus("current")

fcIfCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 6)
)
fcIfCapGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfCapFcphVersionHigh"),
        ("CISCO-FC-FE-MIB", "fcIfCapFcphVersionLow"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxBbCreditMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxBbCreditMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxDataFieldSizeMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxDataFieldSizeMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapCos"),
        ("CISCO-FC-FE-MIB", "fcIfCapClass2SeqDeliv"),
        ("CISCO-FC-FE-MIB", "fcIfCapClass3SeqDeliv"),
        ("CISCO-FC-FE-MIB", "fcIfCapHoldTimeMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapHoldTimeMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapISLRxBbCreditMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapISLRxBbCreditMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxBbCreditWriteable"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxBbCreditDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapISLRxBbCreditDefault"))
)
if mibBuilder.loadTexts:
    fcIfCapGroup.setStatus("deprecated")

fcIfErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 7)
)
fcIfErrorGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfLinkFailures"),
        ("CISCO-FC-FE-MIB", "fcIfSyncLosses"),
        ("CISCO-FC-FE-MIB", "fcIfSigLosses"),
        ("CISCO-FC-FE-MIB", "fcIfPrimSeqProtoErrors"),
        ("CISCO-FC-FE-MIB", "fcIfInvalidTxWords"),
        ("CISCO-FC-FE-MIB", "fcIfInvalidCrcs"),
        ("CISCO-FC-FE-MIB", "fcIfDelimiterErrors"),
        ("CISCO-FC-FE-MIB", "fcIfAddressIdErrors"),
        ("CISCO-FC-FE-MIB", "fcIfLinkResetIns"),
        ("CISCO-FC-FE-MIB", "fcIfLinkResetOuts"),
        ("CISCO-FC-FE-MIB", "fcIfOlsIns"),
        ("CISCO-FC-FE-MIB", "fcIfOlsOuts"),
        ("CISCO-FC-FE-MIB", "fcIfRuntFramesIn"),
        ("CISCO-FC-FE-MIB", "fcIfJabberFramesIn"),
        ("CISCO-FC-FE-MIB", "fcIfTxWaitCount"),
        ("CISCO-FC-FE-MIB", "fcIfFramesTooLong"),
        ("CISCO-FC-FE-MIB", "fcIfFramesTooShort"),
        ("CISCO-FC-FE-MIB", "fcIfLRRIn"),
        ("CISCO-FC-FE-MIB", "fcIfLRROut"),
        ("CISCO-FC-FE-MIB", "fcIfNOSIn"),
        ("CISCO-FC-FE-MIB", "fcIfNOSOut"),
        ("CISCO-FC-FE-MIB", "fcIfFragFrames"),
        ("CISCO-FC-FE-MIB", "fcIfEOFaFrames"),
        ("CISCO-FC-FE-MIB", "fcIfUnknownClassFrames"),
        ("CISCO-FC-FE-MIB", "fcIf8b10bDisparityErrors"),
        ("CISCO-FC-FE-MIB", "fcIfFramesDiscard"),
        ("CISCO-FC-FE-MIB", "fcIfELPFailures"),
        ("CISCO-FC-FE-MIB", "fcIfBBCreditTransistionFromZero"),
        ("CISCO-FC-FE-MIB", "fcIfEISLFramesDiscard"),
        ("CISCO-FC-FE-MIB", "fcIfFramingErrorFrames"))
)
if mibBuilder.loadTexts:
    fcIfErrorGroup.setStatus("current")

fcIfC2AccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 8)
)
fcIfC2AccountingGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfC2InFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC2OutFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC2InOctets"),
        ("CISCO-FC-FE-MIB", "fcIfC2OutOctets"),
        ("CISCO-FC-FE-MIB", "fcIfC2Discards"),
        ("CISCO-FC-FE-MIB", "fcIfC2FbsyFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC2FrjtFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC2PBSYFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC2PRJTFrames"))
)
if mibBuilder.loadTexts:
    fcIfC2AccountingGroup.setStatus("current")

fcIfC3AccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 9)
)
fcIfC3AccountingGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfC3InFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC3OutFrames"),
        ("CISCO-FC-FE-MIB", "fcIfC3InOctets"),
        ("CISCO-FC-FE-MIB", "fcIfC3OutOctets"),
        ("CISCO-FC-FE-MIB", "fcIfC3Discards"))
)
if mibBuilder.loadTexts:
    fcIfC3AccountingGroup.setStatus("current")

fcIfCfAccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 10)
)
fcIfCfAccountingGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfCfInFrames"),
        ("CISCO-FC-FE-MIB", "fcIfCfOutFrames"),
        ("CISCO-FC-FE-MIB", "fcIfCfInOctets"),
        ("CISCO-FC-FE-MIB", "fcIfCfOutOctets"),
        ("CISCO-FC-FE-MIB", "fcIfCfDiscards"))
)
if mibBuilder.loadTexts:
    fcIfCfAccountingGroup.setStatus("current")

fcIfGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 12)
)
fcIfGroupRev1.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfActiveVsanUpList2k"),
        ("CISCO-FC-FE-MIB", "fcIfActiveVsanUpList4k"))
)
if mibBuilder.loadTexts:
    fcIfGroupRev1.setStatus("current")

fcIfCapGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 13)
)
fcIfCapGroupRev1.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfCapFcphVersionHigh"),
        ("CISCO-FC-FE-MIB", "fcIfCapFcphVersionLow"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxDataFieldSizeMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapRxDataFieldSizeMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapCos"),
        ("CISCO-FC-FE-MIB", "fcIfCapClass2SeqDeliv"),
        ("CISCO-FC-FE-MIB", "fcIfCapClass3SeqDeliv"),
        ("CISCO-FC-FE-MIB", "fcIfCapHoldTimeMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapHoldTimeMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapBbScnCapable"),
        ("CISCO-FC-FE-MIB", "fcIfCapBbScnMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmFrmCapable"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxBbCreditWriteable"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxBbCreditMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxBbCreditMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxBbCreditDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmISLRxBbCreditMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmISLRxBbCreditMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmISLRxBbCreditDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxPerfBufWriteable"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxPerfBufMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxPerfBufMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmRxPerfBufDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmISLRxPerfBufMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmISLRxPerfBufMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapOsmISLRxPerfBufDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxBbCreditWriteable"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxBbCreditMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxBbCreditMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxBbCreditDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmISLRxBbCreditMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmISLRxBbCreditMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmISLRxBbCreditDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxPerfBufWriteable"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxPerfBufMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxPerfBufMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmRxPerfBufDefault"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmISLRxPerfBufMax"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmISLRxPerfBufMin"),
        ("CISCO-FC-FE-MIB", "fcIfCapFrmISLRxPerfBufDefault"))
)
if mibBuilder.loadTexts:
    fcIfCapGroupRev1.setStatus("current")

fcIfGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 14)
)
fcIfGroupRev2.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfPortRateMode"),
        ("CISCO-FC-FE-MIB", "fcIfAdminRxPerfBuffer"),
        ("CISCO-FC-FE-MIB", "fcIfOperRxPerfBuffer"),
        ("CISCO-FC-FE-MIB", "fcIfBbScn"))
)
if mibBuilder.loadTexts:
    fcIfGroupRev2.setStatus("current")

fcIfStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 15)
)
fcIfStatGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfCurrRxBbCredit"),
        ("CISCO-FC-FE-MIB", "fcIfCurrTxBbCredit"))
)
if mibBuilder.loadTexts:
    fcIfStatGroup.setStatus("current")

fcIfErrorGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 16)
)
fcIfErrorGroupRev1.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfLipF8In"),
        ("CISCO-FC-FE-MIB", "fcIfLipF8Out"),
        ("CISCO-FC-FE-MIB", "fcIfNonLipF8In"),
        ("CISCO-FC-FE-MIB", "fcIfNonLipF8Out"))
)
if mibBuilder.loadTexts:
    fcIfErrorGroupRev1.setStatus("current")

fcIfGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 17)
)
fcIfGroupRev3.setObjects(
    ("CISCO-FC-FE-MIB", "fcIfPortInitStatus")
)
if mibBuilder.loadTexts:
    fcIfGroupRev3.setStatus("current")

fcIfRNIDInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 18)
)
fcIfRNIDInfoGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfRNIDInfoStatus"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoTypeNumber"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoModelNumber"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoManufacturer"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoPlantOfMfg"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoSerialNumber"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoUnitType"),
        ("CISCO-FC-FE-MIB", "fcIfRNIDInfoPortId"))
)
if mibBuilder.loadTexts:
    fcIfRNIDInfoGroup.setStatus("current")

fcIfGigEInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 19)
)
fcIfGigEInfoGroup.setObjects(
    ("CISCO-FC-FE-MIB", "fcIfGigEPortChannelIfIndex")
)
if mibBuilder.loadTexts:
    fcIfGigEInfoGroup.setStatus("current")

fcIfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 21)
)
fcIfInfoGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfAdminRxBbCreditExtended"),
        ("CISCO-FC-FE-MIB", "fcIfFcTunnelIfIndex"),
        ("CISCO-FC-FE-MIB", "fcIfServiceState"))
)
if mibBuilder.loadTexts:
    fcIfInfoGroup.setStatus("current")

fcIfGigEinfoExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 22)
)
fcIfGigEinfoExtGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfGigEAutoNegotiate"),
        ("CISCO-FC-FE-MIB", "fcIfGigEBeaconMode"))
)
if mibBuilder.loadTexts:
    fcIfGigEinfoExtGroup.setStatus("current")

fcIfBbScnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 23)
)
fcIfBbScnGroup.setObjects(
    ("CISCO-FC-FE-MIB", "fcIfAdminBbScnMode")
)
if mibBuilder.loadTexts:
    fcIfBbScnGroup.setStatus("current")

fcIfCapableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 24)
)
fcIfCapableGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfIsServiceStateCapable"),
        ("CISCO-FC-FE-MIB", "fcIfIsPortRateModeCapable"),
        ("CISCO-FC-FE-MIB", "fcIfIsAdminRxBbCreditExtendedCapable"))
)
if mibBuilder.loadTexts:
    fcIfCapableGroup.setStatus("current")

fcIfInfoPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 25)
)
fcIfInfoPortGroup.setObjects(
    ("CISCO-FC-FE-MIB", "fcIfPortType")
)
if mibBuilder.loadTexts:
    fcIfInfoPortGroup.setStatus("current")

fcIfModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 26)
)
fcIfModuleGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfModuleOverSubscriptionRatioConfig"),
        ("CISCO-FC-FE-MIB", "fcIfModuleBandwidthFairnessConfig"),
        ("CISCO-FC-FE-MIB", "fcIfModuleBandwidthFairnessOper"))
)
if mibBuilder.loadTexts:
    fcIfModuleGroup.setStatus("deprecated")

fcIfToggleCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 27)
)
fcIfToggleCtrlConfigGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfToggleCtrlConfigEnable"),
        ("CISCO-FC-FE-MIB", "fcIfToggleCtrlConfigReason"),
        ("CISCO-FC-FE-MIB", "fcIfToggleCtrlConfigDuration"),
        ("CISCO-FC-FE-MIB", "fcIfToggleCtrlConfigNumFlaps"))
)
if mibBuilder.loadTexts:
    fcIfToggleCtrlConfigGroup.setStatus("deprecated")

fcIfFlapCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 28)
)
fcIfFlapCtrlConfigGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfFlapCtrlConfigEnable"),
        ("CISCO-FC-FE-MIB", "fcIfFlapCtrlConfigDuration"),
        ("CISCO-FC-FE-MIB", "fcIfFlapCtrlConfigNumFlaps"))
)
if mibBuilder.loadTexts:
    fcIfFlapCtrlConfigGroup.setStatus("current")

fcIfModuleGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 29)
)
fcIfModuleGroupRev1.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfModuleOverSubscriptionRatioConfig"),
        ("CISCO-FC-FE-MIB", "fcIfModuleBandwidthFairnessConfig"),
        ("CISCO-FC-FE-MIB", "fcIfModuleBandwidthFairnessOper"),
        ("CISCO-FC-FE-MIB", "fcIfModuleXcvrFrequencyConfig"))
)
if mibBuilder.loadTexts:
    fcIfModuleGroupRev1.setStatus("current")

fcIfGigEinfoExtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 30)
)
fcIfGigEinfoExtGroupRev1.setObjects(
    ("CISCO-FC-FE-MIB", "fcIfGigConnectorType")
)
if mibBuilder.loadTexts:
    fcIfGigEinfoExtGroupRev1.setStatus("current")

fcIfErrorGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 31)
)
fcIfErrorGroupRev2.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfTimeOutDiscards"),
        ("CISCO-FC-FE-MIB", "fcIfOutDiscards"),
        ("CISCO-FC-FE-MIB", "fcIfCreditLoss"),
        ("CISCO-FC-FE-MIB", "fcIfTxWtAvgBBCreditTransitionToZero"))
)
if mibBuilder.loadTexts:
    fcIfErrorGroupRev2.setStatus("current")

fcIfErrorGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 32)
)
fcIfErrorGroupRev3.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfBBCreditTransistionToZero"),
        ("CISCO-FC-FE-MIB", "fcHCIfBBCreditTransistionFromZero"),
        ("CISCO-FC-FE-MIB", "fcHCIfBBCreditTransistionToZero"))
)
if mibBuilder.loadTexts:
    fcIfErrorGroupRev3.setStatus("current")

fcIfGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 33)
)
fcIfGroupRev4.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfAdminFECState"),
        ("CISCO-FC-FE-MIB", "fcIfOperFECState"))
)
if mibBuilder.loadTexts:
    fcIfGroupRev4.setStatus("current")

fcIfErrorGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 34)
)
fcIfErrorGroupRev4.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfFECCorrectedBlks"),
        ("CISCO-FC-FE-MIB", "fcIfFECUncorrectedBlks"))
)
if mibBuilder.loadTexts:
    fcIfErrorGroupRev4.setStatus("current")


# Notification objects

fcTrunkIfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3, 0, 1)
)
fcTrunkIfDownNotify.setObjects(
      *(("CISCO-FC-FE-MIB", "fcTrunkIfOperStatus"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfOperStatusCause"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfOperStatusCauseDescr"))
)
if mibBuilder.loadTexts:
    fcTrunkIfDownNotify.setStatus(
        "current"
    )

fcTrunkIfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3, 0, 2)
)
fcTrunkIfUpNotify.setObjects(
      *(("CISCO-FC-FE-MIB", "fcTrunkIfOperStatus"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfOperStatusCause"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfOperStatusCauseDescr"))
)
if mibBuilder.loadTexts:
    fcTrunkIfUpNotify.setStatus(
        "current"
    )

fcIfElpReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3, 0, 3)
)
fcIfElpReject.setObjects(
      *(("CISCO-FC-FE-MIB", "fcIfElpNbrNodeName"),
        ("CISCO-FC-FE-MIB", "fcIfElpNbrPortName"),
        ("CISCO-FC-FE-MIB", "fcIfElpRejectReasonCode"),
        ("CISCO-FC-FE-MIB", "fcIfElpRejectReasonCodeExpl"))
)
if mibBuilder.loadTexts:
    fcIfElpReject.setStatus(
        "current"
    )

fcotInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3, 0, 4)
)
fcotInserted.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause")
)
if mibBuilder.loadTexts:
    fcotInserted.setStatus(
        "current"
    )

fcotRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 1, 3, 0, 5)
)
fcotRemoved.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause")
)
if mibBuilder.loadTexts:
    fcotRemoved.setStatus(
        "current"
    )


# Notifications groups

fcIfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 11)
)
fcIfNotificationGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcTrunkIfDownNotify"),
        ("CISCO-FC-FE-MIB", "fcTrunkIfUpNotify"),
        ("CISCO-FC-FE-MIB", "fcIfElpReject"))
)
if mibBuilder.loadTexts:
    fcIfNotificationGroup.setStatus(
        "current"
    )

fcotInfoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 2, 20)
)
fcotInfoNotificationGroup.setObjects(
      *(("CISCO-FC-FE-MIB", "fcotInserted"),
        ("CISCO-FC-FE-MIB", "fcotRemoved"))
)
if mibBuilder.loadTexts:
    fcotInfoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cffFcFeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cffFcFeMIBCompliance.setStatus(
        "deprecated"
    )

cffFcFeMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cffFcFeMIBCompliance1.setStatus(
        "deprecated"
    )

cffFcFeMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cffFcFeMIBCompliance2.setStatus(
        "deprecated"
    )

cffFcFeMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cffFcFeMIBCompliance3.setStatus(
        "deprecated"
    )

cffFcFeMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cffFcFeMIBCompliance4.setStatus(
        "deprecated"
    )

cffFcFeMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cffFcFeMIBCompliance5.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev6.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 8)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev7.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 9)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev8.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 10)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev9.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 11)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev10.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 12)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev11.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 13)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev12.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 14)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev13.setStatus(
        "deprecated"
    )

cffFcFeMIBComplianceRev14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 289, 2, 1, 15)
)
if mibBuilder.loadTexts:
    cffFcFeMIBComplianceRev14.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-FE-MIB",
    **{"FcphVersion": FcphVersion,
       "FcBbCredit": FcBbCredit,
       "FcRxDataFieldSize": FcRxDataFieldSize,
       "FcBbCreditModel": FcBbCreditModel,
       "FcIfOperStatusReason": FcIfOperStatusReason,
       "FcPerfBuffer": FcPerfBuffer,
       "ciscoFcFeMIB": ciscoFcFeMIB,
       "ciscoFcFeObjects": ciscoFcFeObjects,
       "cffFcFeConfig": cffFcFeConfig,
       "cffFcFeElementName": cffFcFeElementName,
       "fcIfTable": fcIfTable,
       "fcIfEntry": fcIfEntry,
       "fcIfWwn": fcIfWwn,
       "fcIfAdminMode": fcIfAdminMode,
       "fcIfOperMode": fcIfOperMode,
       "fcIfAdminSpeed": fcIfAdminSpeed,
       "fcIfBeaconMode": fcIfBeaconMode,
       "fcIfPortChannelIfIndex": fcIfPortChannelIfIndex,
       "fcIfOperStatusCause": fcIfOperStatusCause,
       "fcIfOperStatusCauseDescr": fcIfOperStatusCauseDescr,
       "fcIfAdminTrunkMode": fcIfAdminTrunkMode,
       "fcIfOperTrunkMode": fcIfOperTrunkMode,
       "fcIfAllowedVsanList2k": fcIfAllowedVsanList2k,
       "fcIfAllowedVsanList4k": fcIfAllowedVsanList4k,
       "fcIfActiveVsanList2k": fcIfActiveVsanList2k,
       "fcIfActiveVsanList4k": fcIfActiveVsanList4k,
       "fcIfBbCreditModel": fcIfBbCreditModel,
       "fcIfHoldTime": fcIfHoldTime,
       "fcIfTransmitterType": fcIfTransmitterType,
       "fcIfConnectorType": fcIfConnectorType,
       "fcIfSerialNo": fcIfSerialNo,
       "fcIfRevision": fcIfRevision,
       "fcIfVendor": fcIfVendor,
       "fcIfSFPSerialIDData": fcIfSFPSerialIDData,
       "fcIfPartNumber": fcIfPartNumber,
       "fcIfAdminRxBbCredit": fcIfAdminRxBbCredit,
       "fcIfAdminRxBbCreditModeISL": fcIfAdminRxBbCreditModeISL,
       "fcIfAdminRxBbCreditModeFx": fcIfAdminRxBbCreditModeFx,
       "fcIfOperRxBbCredit": fcIfOperRxBbCredit,
       "fcIfRxDataFieldSize": fcIfRxDataFieldSize,
       "fcIfActiveVsanUpList2k": fcIfActiveVsanUpList2k,
       "fcIfActiveVsanUpList4k": fcIfActiveVsanUpList4k,
       "fcIfPortRateMode": fcIfPortRateMode,
       "fcIfAdminRxPerfBuffer": fcIfAdminRxPerfBuffer,
       "fcIfOperRxPerfBuffer": fcIfOperRxPerfBuffer,
       "fcIfBbScn": fcIfBbScn,
       "fcIfPortInitStatus": fcIfPortInitStatus,
       "fcIfAdminRxBbCreditExtended": fcIfAdminRxBbCreditExtended,
       "fcIfFcTunnelIfIndex": fcIfFcTunnelIfIndex,
       "fcIfServiceState": fcIfServiceState,
       "fcIfAdminBbScnMode": fcIfAdminBbScnMode,
       "fcIfPortType": fcIfPortType,
       "fcIfAdminFECState": fcIfAdminFECState,
       "fcIfOperFECState": fcIfOperFECState,
       "fcTrunkIfTable": fcTrunkIfTable,
       "fcTrunkIfEntry": fcTrunkIfEntry,
       "fcTrunkIfOperStatus": fcTrunkIfOperStatus,
       "fcTrunkIfOperStatusCause": fcTrunkIfOperStatusCause,
       "fcTrunkIfOperStatusCauseDescr": fcTrunkIfOperStatusCauseDescr,
       "fcIfLoginEntryCount": fcIfLoginEntryCount,
       "fcIfFLoginTable": fcIfFLoginTable,
       "fcIfFLoginEntry": fcIfFLoginEntry,
       "fcIfNxLoginIndex": fcIfNxLoginIndex,
       "fcIfNxPortNodeName": fcIfNxPortNodeName,
       "fcIfNxPortName": fcIfNxPortName,
       "fcIfNxPortAddress": fcIfNxPortAddress,
       "fcIfNxFcphVersionAgreed": fcIfNxFcphVersionAgreed,
       "fcIfNxRxBbCredit": fcIfNxRxBbCredit,
       "fcIfNxTxBbCredit": fcIfNxTxBbCredit,
       "fcIfNxClass2RxDataFieldSize": fcIfNxClass2RxDataFieldSize,
       "fcIfNxClass3RxDataFieldSize": fcIfNxClass3RxDataFieldSize,
       "fcIfNxCosSuppAgreed": fcIfNxCosSuppAgreed,
       "fcIfNxClass2SeqDelivAgreed": fcIfNxClass2SeqDelivAgreed,
       "fcIfNxClass3SeqDelivAgreed": fcIfNxClass3SeqDelivAgreed,
       "fcIfElpTable": fcIfElpTable,
       "fcIfElpEntry": fcIfElpEntry,
       "fcIfElpNbrNodeName": fcIfElpNbrNodeName,
       "fcIfElpNbrPortName": fcIfElpNbrPortName,
       "fcIfElpRxBbCredit": fcIfElpRxBbCredit,
       "fcIfElpTxBbCredit": fcIfElpTxBbCredit,
       "fcIfElpCosSuppAgreed": fcIfElpCosSuppAgreed,
       "fcIfElpClass2SeqDelivAgreed": fcIfElpClass2SeqDelivAgreed,
       "fcIfElpClass2RxDataFieldSize": fcIfElpClass2RxDataFieldSize,
       "fcIfElpClass3SeqDelivAgreed": fcIfElpClass3SeqDelivAgreed,
       "fcIfElpClass3RxDataFieldSize": fcIfElpClass3RxDataFieldSize,
       "fcIfElpClassFXII": fcIfElpClassFXII,
       "fcIfElpClassFRxDataFieldSize": fcIfElpClassFRxDataFieldSize,
       "fcIfElpClassFConcurrentSeq": fcIfElpClassFConcurrentSeq,
       "fcIfElpClassFEndToEndCredit": fcIfElpClassFEndToEndCredit,
       "fcIfElpClassFOpenSeq": fcIfElpClassFOpenSeq,
       "fcIfCapTable": fcIfCapTable,
       "fcIfCapEntry": fcIfCapEntry,
       "fcIfCapFcphVersionHigh": fcIfCapFcphVersionHigh,
       "fcIfCapFcphVersionLow": fcIfCapFcphVersionLow,
       "fcIfCapRxBbCreditMax": fcIfCapRxBbCreditMax,
       "fcIfCapRxBbCreditMin": fcIfCapRxBbCreditMin,
       "fcIfCapRxDataFieldSizeMax": fcIfCapRxDataFieldSizeMax,
       "fcIfCapRxDataFieldSizeMin": fcIfCapRxDataFieldSizeMin,
       "fcIfCapCos": fcIfCapCos,
       "fcIfCapClass2SeqDeliv": fcIfCapClass2SeqDeliv,
       "fcIfCapClass3SeqDeliv": fcIfCapClass3SeqDeliv,
       "fcIfCapHoldTimeMax": fcIfCapHoldTimeMax,
       "fcIfCapHoldTimeMin": fcIfCapHoldTimeMin,
       "fcIfCapISLRxBbCreditMax": fcIfCapISLRxBbCreditMax,
       "fcIfCapISLRxBbCreditMin": fcIfCapISLRxBbCreditMin,
       "fcIfCapRxBbCreditWriteable": fcIfCapRxBbCreditWriteable,
       "fcIfCapRxBbCreditDefault": fcIfCapRxBbCreditDefault,
       "fcIfCapISLRxBbCreditDefault": fcIfCapISLRxBbCreditDefault,
       "fcIfCapBbScnCapable": fcIfCapBbScnCapable,
       "fcIfCapBbScnMax": fcIfCapBbScnMax,
       "fcIfCapOsmFrmCapable": fcIfCapOsmFrmCapable,
       "fcIfIsServiceStateCapable": fcIfIsServiceStateCapable,
       "fcIfIsPortRateModeCapable": fcIfIsPortRateModeCapable,
       "fcIfIsAdminRxBbCreditExtendedCapable": fcIfIsAdminRxBbCreditExtendedCapable,
       "adminTrunkProtocol": adminTrunkProtocol,
       "fcIfElpRejectReasonCode": fcIfElpRejectReasonCode,
       "fcIfElpRejectReasonCodeExpl": fcIfElpRejectReasonCodeExpl,
       "fcIfCapOsmTable": fcIfCapOsmTable,
       "fcIfCapOsmEntry": fcIfCapOsmEntry,
       "fcIfCapOsmRxBbCreditWriteable": fcIfCapOsmRxBbCreditWriteable,
       "fcIfCapOsmRxBbCreditMax": fcIfCapOsmRxBbCreditMax,
       "fcIfCapOsmRxBbCreditMin": fcIfCapOsmRxBbCreditMin,
       "fcIfCapOsmRxBbCreditDefault": fcIfCapOsmRxBbCreditDefault,
       "fcIfCapOsmISLRxBbCreditMax": fcIfCapOsmISLRxBbCreditMax,
       "fcIfCapOsmISLRxBbCreditMin": fcIfCapOsmISLRxBbCreditMin,
       "fcIfCapOsmISLRxBbCreditDefault": fcIfCapOsmISLRxBbCreditDefault,
       "fcIfCapOsmRxPerfBufWriteable": fcIfCapOsmRxPerfBufWriteable,
       "fcIfCapOsmRxPerfBufMax": fcIfCapOsmRxPerfBufMax,
       "fcIfCapOsmRxPerfBufMin": fcIfCapOsmRxPerfBufMin,
       "fcIfCapOsmRxPerfBufDefault": fcIfCapOsmRxPerfBufDefault,
       "fcIfCapOsmISLRxPerfBufMax": fcIfCapOsmISLRxPerfBufMax,
       "fcIfCapOsmISLRxPerfBufMin": fcIfCapOsmISLRxPerfBufMin,
       "fcIfCapOsmISLRxPerfBufDefault": fcIfCapOsmISLRxPerfBufDefault,
       "fcIfCapFrmTable": fcIfCapFrmTable,
       "fcIfCapFrmEntry": fcIfCapFrmEntry,
       "fcIfCapFrmRxBbCreditWriteable": fcIfCapFrmRxBbCreditWriteable,
       "fcIfCapFrmRxBbCreditMax": fcIfCapFrmRxBbCreditMax,
       "fcIfCapFrmRxBbCreditMin": fcIfCapFrmRxBbCreditMin,
       "fcIfCapFrmRxBbCreditDefault": fcIfCapFrmRxBbCreditDefault,
       "fcIfCapFrmISLRxBbCreditMax": fcIfCapFrmISLRxBbCreditMax,
       "fcIfCapFrmISLRxBbCreditMin": fcIfCapFrmISLRxBbCreditMin,
       "fcIfCapFrmISLRxBbCreditDefault": fcIfCapFrmISLRxBbCreditDefault,
       "fcIfCapFrmRxPerfBufWriteable": fcIfCapFrmRxPerfBufWriteable,
       "fcIfCapFrmRxPerfBufMax": fcIfCapFrmRxPerfBufMax,
       "fcIfCapFrmRxPerfBufMin": fcIfCapFrmRxPerfBufMin,
       "fcIfCapFrmRxPerfBufDefault": fcIfCapFrmRxPerfBufDefault,
       "fcIfCapFrmISLRxPerfBufMax": fcIfCapFrmISLRxPerfBufMax,
       "fcIfCapFrmISLRxPerfBufMin": fcIfCapFrmISLRxPerfBufMin,
       "fcIfCapFrmISLRxPerfBufDefault": fcIfCapFrmISLRxPerfBufDefault,
       "fcIfRNIDInfoTable": fcIfRNIDInfoTable,
       "fcIfRNIDInfoEntry": fcIfRNIDInfoEntry,
       "fcIfRNIDInfoStatus": fcIfRNIDInfoStatus,
       "fcIfRNIDInfoTypeNumber": fcIfRNIDInfoTypeNumber,
       "fcIfRNIDInfoModelNumber": fcIfRNIDInfoModelNumber,
       "fcIfRNIDInfoManufacturer": fcIfRNIDInfoManufacturer,
       "fcIfRNIDInfoPlantOfMfg": fcIfRNIDInfoPlantOfMfg,
       "fcIfRNIDInfoSerialNumber": fcIfRNIDInfoSerialNumber,
       "fcIfRNIDInfoUnitType": fcIfRNIDInfoUnitType,
       "fcIfRNIDInfoPortId": fcIfRNIDInfoPortId,
       "fcIfGigETable": fcIfGigETable,
       "fcIfGigEEntry": fcIfGigEEntry,
       "fcIfGigEPortChannelIfIndex": fcIfGigEPortChannelIfIndex,
       "fcIfGigEAutoNegotiate": fcIfGigEAutoNegotiate,
       "fcIfGigEBeaconMode": fcIfGigEBeaconMode,
       "fcIfGigConnectorType": fcIfGigConnectorType,
       "fcIfModuleTable": fcIfModuleTable,
       "fcIfModuleEntry": fcIfModuleEntry,
       "fcIfModuleOverSubscriptionRatioConfig": fcIfModuleOverSubscriptionRatioConfig,
       "fcIfModuleBandwidthFairnessConfig": fcIfModuleBandwidthFairnessConfig,
       "fcIfModuleBandwidthFairnessOper": fcIfModuleBandwidthFairnessOper,
       "fcIfModuleXcvrFrequencyConfig": fcIfModuleXcvrFrequencyConfig,
       "fcIfToggleCtrlConfigTable": fcIfToggleCtrlConfigTable,
       "fcIfToggleCtrlConfigEntry": fcIfToggleCtrlConfigEntry,
       "fcIfToggleCtrlConfigEnable": fcIfToggleCtrlConfigEnable,
       "fcIfToggleCtrlConfigReason": fcIfToggleCtrlConfigReason,
       "fcIfToggleCtrlConfigDuration": fcIfToggleCtrlConfigDuration,
       "fcIfToggleCtrlConfigNumFlaps": fcIfToggleCtrlConfigNumFlaps,
       "fcIfFlapCtrlConfigTable": fcIfFlapCtrlConfigTable,
       "fcIfFlapCtrlConfigEntry": fcIfFlapCtrlConfigEntry,
       "fcIfFlapCtrlConfigReason": fcIfFlapCtrlConfigReason,
       "fcIfFlapCtrlConfigEnable": fcIfFlapCtrlConfigEnable,
       "fcIfFlapCtrlConfigDuration": fcIfFlapCtrlConfigDuration,
       "fcIfFlapCtrlConfigNumFlaps": fcIfFlapCtrlConfigNumFlaps,
       "cffFcFeStatistics": cffFcFeStatistics,
       "fcIfErrorTable": fcIfErrorTable,
       "fcIfErrorEntry": fcIfErrorEntry,
       "fcIfLinkFailures": fcIfLinkFailures,
       "fcIfSyncLosses": fcIfSyncLosses,
       "fcIfSigLosses": fcIfSigLosses,
       "fcIfPrimSeqProtoErrors": fcIfPrimSeqProtoErrors,
       "fcIfInvalidTxWords": fcIfInvalidTxWords,
       "fcIfInvalidCrcs": fcIfInvalidCrcs,
       "fcIfDelimiterErrors": fcIfDelimiterErrors,
       "fcIfAddressIdErrors": fcIfAddressIdErrors,
       "fcIfLinkResetIns": fcIfLinkResetIns,
       "fcIfLinkResetOuts": fcIfLinkResetOuts,
       "fcIfOlsIns": fcIfOlsIns,
       "fcIfOlsOuts": fcIfOlsOuts,
       "fcIfRuntFramesIn": fcIfRuntFramesIn,
       "fcIfJabberFramesIn": fcIfJabberFramesIn,
       "fcIfTxWaitCount": fcIfTxWaitCount,
       "fcIfFramesTooLong": fcIfFramesTooLong,
       "fcIfFramesTooShort": fcIfFramesTooShort,
       "fcIfLRRIn": fcIfLRRIn,
       "fcIfLRROut": fcIfLRROut,
       "fcIfNOSIn": fcIfNOSIn,
       "fcIfNOSOut": fcIfNOSOut,
       "fcIfFragFrames": fcIfFragFrames,
       "fcIfEOFaFrames": fcIfEOFaFrames,
       "fcIfUnknownClassFrames": fcIfUnknownClassFrames,
       "fcIf8b10bDisparityErrors": fcIf8b10bDisparityErrors,
       "fcIfFramesDiscard": fcIfFramesDiscard,
       "fcIfELPFailures": fcIfELPFailures,
       "fcIfBBCreditTransistionFromZero": fcIfBBCreditTransistionFromZero,
       "fcIfEISLFramesDiscard": fcIfEISLFramesDiscard,
       "fcIfFramingErrorFrames": fcIfFramingErrorFrames,
       "fcIfLipF8In": fcIfLipF8In,
       "fcIfLipF8Out": fcIfLipF8Out,
       "fcIfNonLipF8In": fcIfNonLipF8In,
       "fcIfNonLipF8Out": fcIfNonLipF8Out,
       "fcIfTimeOutDiscards": fcIfTimeOutDiscards,
       "fcIfOutDiscards": fcIfOutDiscards,
       "fcIfCreditLoss": fcIfCreditLoss,
       "fcIfTxWtAvgBBCreditTransitionToZero": fcIfTxWtAvgBBCreditTransitionToZero,
       "fcIfBBCreditTransistionToZero": fcIfBBCreditTransistionToZero,
       "fcHCIfBBCreditTransistionFromZero": fcHCIfBBCreditTransistionFromZero,
       "fcHCIfBBCreditTransistionToZero": fcHCIfBBCreditTransistionToZero,
       "fcIfFECCorrectedBlks": fcIfFECCorrectedBlks,
       "fcIfFECUncorrectedBlks": fcIfFECUncorrectedBlks,
       "fcIfC2AccountingTable": fcIfC2AccountingTable,
       "fcIfC2AccountingEntry": fcIfC2AccountingEntry,
       "fcIfC2InFrames": fcIfC2InFrames,
       "fcIfC2OutFrames": fcIfC2OutFrames,
       "fcIfC2InOctets": fcIfC2InOctets,
       "fcIfC2OutOctets": fcIfC2OutOctets,
       "fcIfC2Discards": fcIfC2Discards,
       "fcIfC2FbsyFrames": fcIfC2FbsyFrames,
       "fcIfC2FrjtFrames": fcIfC2FrjtFrames,
       "fcIfC2PBSYFrames": fcIfC2PBSYFrames,
       "fcIfC2PRJTFrames": fcIfC2PRJTFrames,
       "fcIfC3AccountingTable": fcIfC3AccountingTable,
       "fcIfC3AccountingEntry": fcIfC3AccountingEntry,
       "fcIfC3InFrames": fcIfC3InFrames,
       "fcIfC3OutFrames": fcIfC3OutFrames,
       "fcIfC3InOctets": fcIfC3InOctets,
       "fcIfC3OutOctets": fcIfC3OutOctets,
       "fcIfC3Discards": fcIfC3Discards,
       "fcIfCfAccountingTable": fcIfCfAccountingTable,
       "fcIfCfAccountingEntry": fcIfCfAccountingEntry,
       "fcIfCfInFrames": fcIfCfInFrames,
       "fcIfCfOutFrames": fcIfCfOutFrames,
       "fcIfCfInOctets": fcIfCfInOctets,
       "fcIfCfOutOctets": fcIfCfOutOctets,
       "fcIfCfDiscards": fcIfCfDiscards,
       "fcIfStatTable": fcIfStatTable,
       "fcIfStatEntry": fcIfStatEntry,
       "fcIfCurrRxBbCredit": fcIfCurrRxBbCredit,
       "fcIfCurrTxBbCredit": fcIfCurrTxBbCredit,
       "cffFcFeNotification": cffFcFeNotification,
       "cffFcFeNotifications": cffFcFeNotifications,
       "fcTrunkIfDownNotify": fcTrunkIfDownNotify,
       "fcTrunkIfUpNotify": fcTrunkIfUpNotify,
       "fcIfElpReject": fcIfElpReject,
       "fcotInserted": fcotInserted,
       "fcotRemoved": fcotRemoved,
       "cffFcFeMIBConformance": cffFcFeMIBConformance,
       "cffFcFeMIBCompliances": cffFcFeMIBCompliances,
       "cffFcFeMIBCompliance": cffFcFeMIBCompliance,
       "cffFcFeMIBCompliance1": cffFcFeMIBCompliance1,
       "cffFcFeMIBCompliance2": cffFcFeMIBCompliance2,
       "cffFcFeMIBCompliance3": cffFcFeMIBCompliance3,
       "cffFcFeMIBCompliance4": cffFcFeMIBCompliance4,
       "cffFcFeMIBCompliance5": cffFcFeMIBCompliance5,
       "cffFcFeMIBComplianceRev6": cffFcFeMIBComplianceRev6,
       "cffFcFeMIBComplianceRev7": cffFcFeMIBComplianceRev7,
       "cffFcFeMIBComplianceRev8": cffFcFeMIBComplianceRev8,
       "cffFcFeMIBComplianceRev9": cffFcFeMIBComplianceRev9,
       "cffFcFeMIBComplianceRev10": cffFcFeMIBComplianceRev10,
       "cffFcFeMIBComplianceRev11": cffFcFeMIBComplianceRev11,
       "cffFcFeMIBComplianceRev12": cffFcFeMIBComplianceRev12,
       "cffFcFeMIBComplianceRev13": cffFcFeMIBComplianceRev13,
       "cffFcFeMIBComplianceRev14": cffFcFeMIBComplianceRev14,
       "cffFcFeMIBGroups": cffFcFeMIBGroups,
       "fcFeGroup": fcFeGroup,
       "fcIfGroup": fcIfGroup,
       "fcTrunkIfGroup": fcTrunkIfGroup,
       "fcIfLoginGroup": fcIfLoginGroup,
       "fcIfElpGroup": fcIfElpGroup,
       "fcIfCapGroup": fcIfCapGroup,
       "fcIfErrorGroup": fcIfErrorGroup,
       "fcIfC2AccountingGroup": fcIfC2AccountingGroup,
       "fcIfC3AccountingGroup": fcIfC3AccountingGroup,
       "fcIfCfAccountingGroup": fcIfCfAccountingGroup,
       "fcIfNotificationGroup": fcIfNotificationGroup,
       "fcIfGroupRev1": fcIfGroupRev1,
       "fcIfCapGroupRev1": fcIfCapGroupRev1,
       "fcIfGroupRev2": fcIfGroupRev2,
       "fcIfStatGroup": fcIfStatGroup,
       "fcIfErrorGroupRev1": fcIfErrorGroupRev1,
       "fcIfGroupRev3": fcIfGroupRev3,
       "fcIfRNIDInfoGroup": fcIfRNIDInfoGroup,
       "fcIfGigEInfoGroup": fcIfGigEInfoGroup,
       "fcotInfoNotificationGroup": fcotInfoNotificationGroup,
       "fcIfInfoGroup": fcIfInfoGroup,
       "fcIfGigEinfoExtGroup": fcIfGigEinfoExtGroup,
       "fcIfBbScnGroup": fcIfBbScnGroup,
       "fcIfCapableGroup": fcIfCapableGroup,
       "fcIfInfoPortGroup": fcIfInfoPortGroup,
       "fcIfModuleGroup": fcIfModuleGroup,
       "fcIfToggleCtrlConfigGroup": fcIfToggleCtrlConfigGroup,
       "fcIfFlapCtrlConfigGroup": fcIfFlapCtrlConfigGroup,
       "fcIfModuleGroupRev1": fcIfModuleGroupRev1,
       "fcIfGigEinfoExtGroupRev1": fcIfGigEinfoExtGroupRev1,
       "fcIfErrorGroupRev2": fcIfErrorGroupRev2,
       "fcIfErrorGroupRev3": fcIfErrorGroupRev3,
       "fcIfGroupRev4": fcIfGroupRev4,
       "fcIfErrorGroupRev4": fcIfErrorGroupRev4}
)
