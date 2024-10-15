# SNMP MIB module (CISCO-SYSLOG-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYSLOG-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:24 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SyslogSeverity,) = mibBuilder.importSymbols(
    "CISCO-SYSLOG-MIB",
    "SyslogSeverity")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSyslogExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 301)
)
ciscoSyslogExtMIB.setRevisions(
        ("2015-06-08 00:00",
         "2015-03-02 00:00",
         "2014-11-05 00:00",
         "2014-08-13 00:00",
         "2014-06-02 00:00",
         "2014-05-30 00:00",
         "2013-11-23 00:00",
         "2013-09-11 00:00",
         "2013-06-14 00:00",
         "2013-06-11 00:00",
         "2013-01-08 00:00",
         "2012-08-24 00:00",
         "2011-06-09 00:00",
         "2011-06-08 00:00",
         "2011-05-20 00:00",
         "2010-02-05 00:00",
         "2009-08-16 00:00",
         "2009-07-01 00:00",
         "2009-06-17 00:00",
         "2009-06-08 00:00",
         "2008-04-28 00:00",
         "2006-11-09 00:00",
         "2005-01-30 00:00",
         "2004-09-20 00:00",
         "2003-12-15 00:00",
         "2002-11-13 00:00",
         "2002-10-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              16,
              24,
              32,
              40,
              48,
              56,
              64,
              72,
              80,
              88,
              128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("auth", 32),
          ("authPriv", 80),
          ("cron", 72),
          ("daemon", 24),
          ("ftp", 88),
          ("kernel", 0),
          ("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184),
          ("lpr", 48),
          ("mail", 16),
          ("news", 56),
          ("syslog", 40),
          ("user", 8),
          ("uucp", 64))
    )



class SyslogExFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              16,
              24,
              32,
              40,
              48,
              56,
              64,
              72,
              80,
              88,
              128,
              136,
              144,
              152,
              160,
              168,
              176,
              184,
              200,
              208,
              216,
              224,
              232,
              240,
              248,
              256,
              264,
              272,
              280,
              288,
              296,
              304,
              312,
              320,
              328,
              336,
              344,
              352,
              360,
              368,
              376,
              384,
              392,
              400,
              408,
              416,
              424,
              432,
              440,
              448,
              456,
              464,
              472,
              480,
              488,
              496,
              504,
              512,
              520,
              536,
              552,
              576,
              584,
              592,
              608,
              648,
              656,
              672,
              688,
              704,
              736,
              816,
              848,
              920,
              928,
              960,
              976,
              992,
              1016,
              1064,
              1072,
              1096,
              1128,
              1136,
              1152,
              1160,
              1168,
              1192,
              1232,
              1240,
              1248,
              1256,
              1320,
              1328,
              1336,
              1344,
              1352,
              1360,
              1376,
              1392,
              1408,
              1432,
              1448,
              1456,
              1480,
              1488,
              1504,
              1512,
              1520,
              1536,
              1712,
              1720,
              1752,
              1768,
              1784,
              1792,
              1816,
              1872,
              1936,
              2048,
              2072,
              2080,
              2088,
              2112,
              2120,
              2144,
              2160,
              2176,
              2184,
              2240,
              2248,
              2368,
              2376,
              2384,
              2392,
              2400,
              2416,
              2440,
              2448,
              2528,
              2592,
              2600,
              2608,
              2616,
              2648,
              2656,
              2704,
              2728,
              2760,
              2800,
              2840,
              2848,
              2888,
              2896,
              2904,
              2920,
              2936,
              2944,
              2952,
              2960,
              2976,
              3048,
              3056,
              3080,
              3096,
              3112,
              3144,
              3152,
              3160,
              3168,
              3200,
              3216,
              3248,
              3296,
              3336,
              3360,
              3448,
              3496,
              3512,
              3544,
              3576,
              3680,
              3872,
              3888,
              3904,
              3920,
              3952,
              3960,
              3984,
              4008,
              4024,
              4032,
              4040,
              4048,
              4056,
              4064,
              4072,
              4088,
              4096,
              4104,
              4112,
              4120,
              4128,
              4136,
              4144,
              4152,
              4168,
              4192,
              4208,
              4224,
              4320,
              4368,
              4552,
              4592,
              4880,
              5168,
              5320,
              5328,
              5640,
              5744,
              5752,
              5776,
              5784,
              5808,
              5840,
              5848,
              5864,
              5920,
              5960,
              6016,
              6048,
              6168,
              6368)
        )
    )
    namedValues = NamedValues(
        *(("aaad", 1240),
          ("aam", 3680),
          ("acl", 1936),
          ("aclMgr", 312),
          ("acllog", 3360),
          ("aclmgr", 2240),
          ("aclqos", 2080),
          ("adbm", 6048),
          ("afm", 3952),
          ("altos", 4072),
          ("arp", 3080),
          ("assocMgr", 4368),
          ("auth", 32),
          ("authPriv", 80),
          ("avm", 736),
          ("bfd", 4208),
          ("bgp", 2384),
          ("blogger", 5776),
          ("bootvar", 552),
          ("callhome", 472),
          ("cdpd", 848),
          ("certEnroll", 1752),
          ("cfs", 1432),
          ("cimServer", 1328),
          ("clkmgr", 4592),
          ("cloud", 1712),
          ("cluster", 2728),
          ("cmond", 4880),
          ("confCheck", 1192),
          ("copp", 3216),
          ("cron", 72),
          ("cts", 3168),
          ("daemon", 24),
          ("dcbx", 4064),
          ("ddas", 1504),
          ("debugLib", 496),
          ("deviceTest", 3160),
          ("dhcpSnooping", 2608),
          ("diagclient", 2648),
          ("diagmgr", 2656),
          ("diagportlb", 3096),
          ("dns", 648),
          ("domainMgr", 216),
          ("dot1x", 2248),
          ("dpvm", 1480),
          ("dstats", 1448),
          ("ecp", 6016),
          ("eltm", 2112),
          ("enm", 4056),
          ("epp", 1168),
          ("ethPortChannel", 2840),
          ("ethPortMgr", 976),
          ("ethpc", 4040),
          ("ethpm", 1784),
          ("evc", 5168),
          ("evmc", 2416),
          ("evms", 2400),
          ("fabricConfMgr", 304),
          ("fc2", 488),
          ("fc2d", 1320),
          ("fcDns", 296),
          ("fcRedirect", 408),
          ("fcc", 376),
          ("fccLc", 1392),
          ("fcfwd", 432),
          ("fcoeMgr", 4152),
          ("fcpc", 4048),
          ("fcspmgr", 1160),
          ("fdmi", 1136),
          ("featureMgr", 1360),
          ("ficonContDev", 1096),
          ("ficonMgr", 1064),
          ("ficonStat", 1352),
          ("fpOam", 5920),
          ("fportServer", 336),
          ("fsDaemon", 1072),
          ("fscm", 1536),
          ("fspf", 208),
          ("ftp", 88),
          ("fvpd", 688),
          ("fwm", 3904),
          ("fwmCtrl", 4120),
          ("gatosUsd", 3960),
          ("giscm", 5840),
          ("glbp", 2600),
          ("hsrpEngine", 2376),
          ("ifMgr", 1816),
          ("ike", 1488),
          ("ilcHelper", 1408),
          ("ioa", 4168),
          ("ip", 3048),
          ("ipConfMgr", 272),
          ("ipaclMgr", 1016),
          ("ipfc", 280),
          ("ipqosMgr", 2800),
          ("ipsMgr", 480),
          ("ipsec", 1456),
          ("ipv6", 3056),
          ("ipv6Conf", 2760),
          ("iscm", 5640),
          ("isns", 1344),
          ("ivr", 1232),
          ("kernel", 0),
          ("l2fm", 2392),
          ("l2pt", 4552),
          ("l3vm", 2888),
          ("lacp", 2448),
          ("lcohmsd", 1336),
          ("ldap", 2048),
          ("licmgr", 1152),
          ("lim", 5960),
          ("linecardMgr", 232),
          ("lldp", 3576),
          ("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184),
          ("lpr", 48),
          ("lttd", 1376),
          ("m2rib", 3496),
          ("m6rib", 2896),
          ("mail", 16),
          ("mcast", 512),
          ("mfdm", 2160),
          ("migd", 928),
          ("monitor", 2440),
          ("mpls", 352),
          ("mplsTunnel", 816),
          ("mrib", 2904),
          ("mtsDaemon", 224),
          ("mvsh", 3296),
          ("news", 56),
          ("nfm", 2368),
          ("nicmgr", 4008),
          ("nohms", 4088),
          ("nppm", 4136),
          ("npv", 3152),
          ("nqosm", 4032),
          ("ntp", 440),
          ("ohmsd", 920),
          ("orib", 3448),
          ("otm", 2848),
          ("patchd", 6368),
          ("pfm", 3984),
          ("pim", 2920),
          ("pixm", 1792),
          ("pixmgl", 5744),
          ("pixmvl", 5752),
          ("plcmgr", 6168),
          ("plsm", 5808),
          ("pltfmCfg", 3336),
          ("pltmfmMgr", 448),
          ("plugin", 1872),
          ("portChMgr", 344),
          ("portMgr", 328),
          ("portResources", 2072),
          ("portSec", 960),
          ("portSecurity", 2088),
          ("ppm", 4192),
          ("prefpath", 704),
          ("procMgr", 400),
          ("pss", 576),
          ("qd", 4024),
          ("qosCtrl", 4128),
          ("qosMgr", 384),
          ("radiusd", 1256),
          ("rdl", 520),
          ("redwoodUsd", 4112),
          ("resMgr", 2976),
          ("rib", 656),
          ("rlir", 1128),
          ("rpm", 2936),
          ("rscn", 536),
          ("sal", 3200),
          ("sanExtTuner", 1520),
          ("satCtrl", 4104),
          ("satMgr", 4096),
          ("satSyslog", 4144),
          ("scheduler", 1512),
          ("sdv", 2592),
          ("security", 592),
          ("sifMgr", 3888),
          ("sim", 5848),
          ("slaResponder", 5328),
          ("slaSender", 5320),
          ("smartCard", 1720),
          ("sme", 3248),
          ("smm", 2960),
          ("snmp", 584),
          ("snmpmib", 5784),
          ("span", 416),
          ("spm", 3872),
          ("stp", 1768),
          ("svi", 2144),
          ("sysMgr", 240),
          ("sysMgrLib", 248),
          ("syslog", 40),
          ("tacacsd", 1248),
          ("tftpLib", 360),
          ("tlPortMgr", 320),
          ("tm", 3144),
          ("u2rib", 3544),
          ("u6rib", 2944),
          ("udld", 2120),
          ("ufdm", 2184),
          ("urib", 2952),
          ("user", 8),
          ("uucp", 64),
          ("vdcMgr", 2528),
          ("vedbMgr", 2704),
          ("vhba", 392),
          ("vhbad", 608),
          ("virtualIfMgr", 264),
          ("vlanMgr", 2176),
          ("vman", 5864),
          ("vmm", 3112),
          ("vntagMgr", 4320),
          ("vpc", 3512),
          ("vpm", 504),
          ("vrrpEngine", 464),
          ("vrrpMgr", 424),
          ("vsanMgr", 200),
          ("vshd", 672),
          ("wccp", 4224),
          ("wwnMgr", 368),
          ("xBarMgr", 288),
          ("xbarClient", 456),
          ("xmlma", 2616),
          ("zbm", 992),
          ("zoneServer", 256),
          ("zschk", 3920))
    )



class SyslogProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSyslogExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSyslogExtMIBObjects = _CiscoSyslogExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1)
)
_CseSyslogConfigurationGroup_ObjectIdentity = ObjectIdentity
cseSyslogConfigurationGroup = _CseSyslogConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1)
)


class _CseSyslogConsoleEnable_Type(TruthValue):
    """Custom type cseSyslogConsoleEnable based on TruthValue"""


_CseSyslogConsoleEnable_Object = MibScalar
cseSyslogConsoleEnable = _CseSyslogConsoleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 1),
    _CseSyslogConsoleEnable_Type()
)
cseSyslogConsoleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogConsoleEnable.setStatus("current")


class _CseSyslogConsoleMsgSeverity_Type(SyslogSeverity):
    """Custom type cseSyslogConsoleMsgSeverity based on SyslogSeverity"""


_CseSyslogConsoleMsgSeverity_Object = MibScalar
cseSyslogConsoleMsgSeverity = _CseSyslogConsoleMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 2),
    _CseSyslogConsoleMsgSeverity_Type()
)
cseSyslogConsoleMsgSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogConsoleMsgSeverity.setStatus("current")


class _CseSyslogLogFileName_Type(SnmpAdminString):
    """Custom type cseSyslogLogFileName based on SnmpAdminString"""
    defaultValue = OctetString("messages")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CseSyslogLogFileName_Type.__name__ = "SnmpAdminString"
_CseSyslogLogFileName_Object = MibScalar
cseSyslogLogFileName = _CseSyslogLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 3),
    _CseSyslogLogFileName_Type()
)
cseSyslogLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogLogFileName.setStatus("current")


class _CseSyslogLogFileMsgSeverity_Type(SyslogSeverity):
    """Custom type cseSyslogLogFileMsgSeverity based on SyslogSeverity"""


_CseSyslogLogFileMsgSeverity_Object = MibScalar
cseSyslogLogFileMsgSeverity = _CseSyslogLogFileMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 4),
    _CseSyslogLogFileMsgSeverity_Type()
)
cseSyslogLogFileMsgSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogLogFileMsgSeverity.setStatus("current")


class _CseSyslogFileLoggingDisable_Type(Integer32):
    """Custom type cseSyslogFileLoggingDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("true", 1))
    )


_CseSyslogFileLoggingDisable_Type.__name__ = "Integer32"
_CseSyslogFileLoggingDisable_Object = MibScalar
cseSyslogFileLoggingDisable = _CseSyslogFileLoggingDisable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 5),
    _CseSyslogFileLoggingDisable_Type()
)
cseSyslogFileLoggingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogFileLoggingDisable.setStatus("current")


class _CseSyslogServerTableMaxEntries_Type(Unsigned32):
    """Custom type cseSyslogServerTableMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CseSyslogServerTableMaxEntries_Type.__name__ = "Unsigned32"
_CseSyslogServerTableMaxEntries_Object = MibScalar
cseSyslogServerTableMaxEntries = _CseSyslogServerTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 6),
    _CseSyslogServerTableMaxEntries_Type()
)
cseSyslogServerTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSyslogServerTableMaxEntries.setStatus("current")
_CseSyslogServerTable_Object = MibTable
cseSyslogServerTable = _CseSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cseSyslogServerTable.setStatus("current")
_CseSyslogServerEntry_Object = MibTableRow
cseSyslogServerEntry = _CseSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1)
)
cseSyslogServerEntry.setIndexNames(
    (0, "CISCO-SYSLOG-EXT-MIB", "cseSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    cseSyslogServerEntry.setStatus("current")


class _CseSyslogServerIndex_Type(Unsigned32):
    """Custom type cseSyslogServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CseSyslogServerIndex_Type.__name__ = "Unsigned32"
_CseSyslogServerIndex_Object = MibTableColumn
cseSyslogServerIndex = _CseSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 1),
    _CseSyslogServerIndex_Type()
)
cseSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSyslogServerIndex.setStatus("current")
_CseSyslogServerAddressType_Type = InetAddressType
_CseSyslogServerAddressType_Object = MibTableColumn
cseSyslogServerAddressType = _CseSyslogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 2),
    _CseSyslogServerAddressType_Type()
)
cseSyslogServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerAddressType.setStatus("current")
_CseSyslogServerAddress_Type = InetAddress
_CseSyslogServerAddress_Object = MibTableColumn
cseSyslogServerAddress = _CseSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 3),
    _CseSyslogServerAddress_Type()
)
cseSyslogServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerAddress.setStatus("current")


class _CseSyslogServerMsgSeverity_Type(SyslogSeverity):
    """Custom type cseSyslogServerMsgSeverity based on SyslogSeverity"""


_CseSyslogServerMsgSeverity_Object = MibTableColumn
cseSyslogServerMsgSeverity = _CseSyslogServerMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 4),
    _CseSyslogServerMsgSeverity_Type()
)
cseSyslogServerMsgSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerMsgSeverity.setStatus("current")
_CseSyslogServerStatus_Type = RowStatus
_CseSyslogServerStatus_Object = MibTableColumn
cseSyslogServerStatus = _CseSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 5),
    _CseSyslogServerStatus_Type()
)
cseSyslogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerStatus.setStatus("current")


class _CseSyslogServerFacility_Type(SyslogFacility):
    """Custom type cseSyslogServerFacility based on SyslogFacility"""


_CseSyslogServerFacility_Object = MibTableColumn
cseSyslogServerFacility = _CseSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 6),
    _CseSyslogServerFacility_Type()
)
cseSyslogServerFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerFacility.setStatus("current")


class _CseSyslogServerProtocol_Type(SyslogProtocol):
    """Custom type cseSyslogServerProtocol based on SyslogProtocol"""


_CseSyslogServerProtocol_Object = MibTableColumn
cseSyslogServerProtocol = _CseSyslogServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 7),
    _CseSyslogServerProtocol_Type()
)
cseSyslogServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerProtocol.setStatus("current")


class _CseSyslogServerPort_Type(InetPortNumber):
    """Custom type cseSyslogServerPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CseSyslogServerPort_Type.__name__ = "InetPortNumber"
_CseSyslogServerPort_Object = MibTableColumn
cseSyslogServerPort = _CseSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 8),
    _CseSyslogServerPort_Type()
)
cseSyslogServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerPort.setStatus("current")


class _CseSyslogServerProtocolFallback_Type(SyslogProtocol):
    """Custom type cseSyslogServerProtocolFallback based on SyslogProtocol"""


_CseSyslogServerProtocolFallback_Object = MibTableColumn
cseSyslogServerProtocolFallback = _CseSyslogServerProtocolFallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 7, 1, 9),
    _CseSyslogServerProtocolFallback_Type()
)
cseSyslogServerProtocolFallback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseSyslogServerProtocolFallback.setStatus("current")
_CseSyslogMessageControlTable_Object = MibTable
cseSyslogMessageControlTable = _CseSyslogMessageControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cseSyslogMessageControlTable.setStatus("current")
_CseSyslogMessageControlEntry_Object = MibTableRow
cseSyslogMessageControlEntry = _CseSyslogMessageControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 8, 1)
)
cseSyslogMessageControlEntry.setIndexNames(
    (0, "CISCO-SYSLOG-EXT-MIB", "cseSyslogMessageFacility"),
)
if mibBuilder.loadTexts:
    cseSyslogMessageControlEntry.setStatus("current")
_CseSyslogMessageFacility_Type = SyslogExFacility
_CseSyslogMessageFacility_Object = MibTableColumn
cseSyslogMessageFacility = _CseSyslogMessageFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 8, 1, 1),
    _CseSyslogMessageFacility_Type()
)
cseSyslogMessageFacility.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSyslogMessageFacility.setStatus("current")
_CseSyslogMessageSeverity_Type = SyslogSeverity
_CseSyslogMessageSeverity_Object = MibTableColumn
cseSyslogMessageSeverity = _CseSyslogMessageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 8, 1, 2),
    _CseSyslogMessageSeverity_Type()
)
cseSyslogMessageSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogMessageSeverity.setStatus("current")


class _CseSyslogTerminalEnable_Type(TruthValue):
    """Custom type cseSyslogTerminalEnable based on TruthValue"""


_CseSyslogTerminalEnable_Object = MibScalar
cseSyslogTerminalEnable = _CseSyslogTerminalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 9),
    _CseSyslogTerminalEnable_Type()
)
cseSyslogTerminalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogTerminalEnable.setStatus("current")


class _CseSyslogTerminalMsgSeverity_Type(SyslogSeverity):
    """Custom type cseSyslogTerminalMsgSeverity based on SyslogSeverity"""


_CseSyslogTerminalMsgSeverity_Object = MibScalar
cseSyslogTerminalMsgSeverity = _CseSyslogTerminalMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 10),
    _CseSyslogTerminalMsgSeverity_Type()
)
cseSyslogTerminalMsgSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogTerminalMsgSeverity.setStatus("current")


class _CseSyslogLinecardEnable_Type(TruthValue):
    """Custom type cseSyslogLinecardEnable based on TruthValue"""


_CseSyslogLinecardEnable_Object = MibScalar
cseSyslogLinecardEnable = _CseSyslogLinecardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 11),
    _CseSyslogLinecardEnable_Type()
)
cseSyslogLinecardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogLinecardEnable.setStatus("current")


class _CseSyslogLinecardMsgSeverity_Type(SyslogSeverity):
    """Custom type cseSyslogLinecardMsgSeverity based on SyslogSeverity"""


_CseSyslogLinecardMsgSeverity_Object = MibScalar
cseSyslogLinecardMsgSeverity = _CseSyslogLinecardMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 1, 1, 12),
    _CseSyslogLinecardMsgSeverity_Type()
)
cseSyslogLinecardMsgSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSyslogLinecardMsgSeverity.setStatus("current")
_CiscoSyslogExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSyslogExtMIBConformance = _CiscoSyslogExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2)
)
_CiscoSyslogExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSyslogExtMIBCompliances = _CiscoSyslogExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2, 1)
)
_CiscoSyslogExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSyslogExtMIBGroups = _CiscoSyslogExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2, 2)
)

# Managed Objects groups

ciscoSyslogExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2, 2, 1)
)
ciscoSyslogExtGroup.setObjects(
      *(("CISCO-SYSLOG-EXT-MIB", "cseSyslogConsoleEnable"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogLogFileName"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogFileLoggingDisable"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogConsoleMsgSeverity"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogLogFileMsgSeverity"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerTableMaxEntries"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerAddress"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerAddressType"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerMsgSeverity"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerStatus"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerFacility"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogMessageSeverity"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogTerminalEnable"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogTerminalMsgSeverity"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogLinecardEnable"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogLinecardMsgSeverity"))
)
if mibBuilder.loadTexts:
    ciscoSyslogExtGroup.setStatus("current")

ciscoSyslogProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2, 2, 2)
)
ciscoSyslogProtocolGroup.setObjects(
      *(("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerProtocol"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerPort"),
        ("CISCO-SYSLOG-EXT-MIB", "cseSyslogServerProtocolFallback"))
)
if mibBuilder.loadTexts:
    ciscoSyslogProtocolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSyslogExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSyslogExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSyslogExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 301, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSyslogExtMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYSLOG-EXT-MIB",
    **{"SyslogFacility": SyslogFacility,
       "SyslogExFacility": SyslogExFacility,
       "SyslogProtocol": SyslogProtocol,
       "ciscoSyslogExtMIB": ciscoSyslogExtMIB,
       "ciscoSyslogExtMIBObjects": ciscoSyslogExtMIBObjects,
       "cseSyslogConfigurationGroup": cseSyslogConfigurationGroup,
       "cseSyslogConsoleEnable": cseSyslogConsoleEnable,
       "cseSyslogConsoleMsgSeverity": cseSyslogConsoleMsgSeverity,
       "cseSyslogLogFileName": cseSyslogLogFileName,
       "cseSyslogLogFileMsgSeverity": cseSyslogLogFileMsgSeverity,
       "cseSyslogFileLoggingDisable": cseSyslogFileLoggingDisable,
       "cseSyslogServerTableMaxEntries": cseSyslogServerTableMaxEntries,
       "cseSyslogServerTable": cseSyslogServerTable,
       "cseSyslogServerEntry": cseSyslogServerEntry,
       "cseSyslogServerIndex": cseSyslogServerIndex,
       "cseSyslogServerAddressType": cseSyslogServerAddressType,
       "cseSyslogServerAddress": cseSyslogServerAddress,
       "cseSyslogServerMsgSeverity": cseSyslogServerMsgSeverity,
       "cseSyslogServerStatus": cseSyslogServerStatus,
       "cseSyslogServerFacility": cseSyslogServerFacility,
       "cseSyslogServerProtocol": cseSyslogServerProtocol,
       "cseSyslogServerPort": cseSyslogServerPort,
       "cseSyslogServerProtocolFallback": cseSyslogServerProtocolFallback,
       "cseSyslogMessageControlTable": cseSyslogMessageControlTable,
       "cseSyslogMessageControlEntry": cseSyslogMessageControlEntry,
       "cseSyslogMessageFacility": cseSyslogMessageFacility,
       "cseSyslogMessageSeverity": cseSyslogMessageSeverity,
       "cseSyslogTerminalEnable": cseSyslogTerminalEnable,
       "cseSyslogTerminalMsgSeverity": cseSyslogTerminalMsgSeverity,
       "cseSyslogLinecardEnable": cseSyslogLinecardEnable,
       "cseSyslogLinecardMsgSeverity": cseSyslogLinecardMsgSeverity,
       "ciscoSyslogExtMIBConformance": ciscoSyslogExtMIBConformance,
       "ciscoSyslogExtMIBCompliances": ciscoSyslogExtMIBCompliances,
       "ciscoSyslogExtMIBCompliance": ciscoSyslogExtMIBCompliance,
       "ciscoSyslogExtMIBComplianceRev2": ciscoSyslogExtMIBComplianceRev2,
       "ciscoSyslogExtMIBGroups": ciscoSyslogExtMIBGroups,
       "ciscoSyslogExtGroup": ciscoSyslogExtGroup,
       "ciscoSyslogProtocolGroup": ciscoSyslogProtocolGroup}
)
