# SNMP MIB module (WG102) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WG102
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:48 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wg102 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4)
)
_SysSettings_ObjectIdentity = ObjectIdentity
sysSettings = _SysSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1)
)


class _SysMacAddress_Type(DisplayString):
    """Custom type sysMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_SysMacAddress_Type.__name__ = "DisplayString"
_SysMacAddress_Object = MibScalar
sysMacAddress = _SysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 1),
    _SysMacAddress_Type()
)
sysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAddress.setStatus("current")
_SysVersion_Type = DisplayString
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 2),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")


class _SysAPName_Type(DisplayString):
    """Custom type sysAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SysAPName_Type.__name__ = "DisplayString"
_SysAPName_Object = MibScalar
sysAPName = _SysAPName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 3),
    _SysAPName_Type()
)
sysAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAPName.setStatus("current")


class _SysAdminName_Type(DisplayString):
    """Custom type sysAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysAdminName_Type.__name__ = "DisplayString"
_SysAdminName_Object = MibScalar
sysAdminName = _SysAdminName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 4),
    _SysAdminName_Type()
)
sysAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminName.setStatus("current")


class _SysAdminPasswd_Type(DisplayString):
    """Custom type sysAdminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysAdminPasswd_Type.__name__ = "DisplayString"
_SysAdminPasswd_Object = MibScalar
sysAdminPasswd = _SysAdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 5),
    _SysAdminPasswd_Type()
)
sysAdminPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminPasswd.setStatus("current")


class _SysCountryRegion_Type(Integer32):
    """Custom type sysCountryRegion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(36,
              40,
              124,
              208,
              246,
              250,
              276,
              340,
              372,
              380,
              392,
              410,
              484,
              528,
              554,
              578,
              630,
              724,
              752,
              756,
              826,
              840)
        )
    )
    namedValues = NamedValues(
        *(("asia", 410),
          ("australia", 36),
          ("canada", 124),
          ("denmark", 208),
          ("europe", 40),
          ("finland", 246),
          ("france", 250),
          ("germany", 276),
          ("ireland", 372),
          ("italy", 380),
          ("japan", 392),
          ("mexico", 484),
          ("netherlands", 528),
          ("newZealand", 554),
          ("norway", 578),
          ("puertoRico", 630),
          ("southAmerica", 340),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("unitedKingdom", 826),
          ("unitedStates", 840))
    )


_SysCountryRegion_Type.__name__ = "Integer32"
_SysCountryRegion_Object = MibScalar
sysCountryRegion = _SysCountryRegion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 7),
    _SysCountryRegion_Type()
)
sysCountryRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCountryRegion.setStatus("current")
_TimeSettings_ObjectIdentity = ObjectIdentity
timeSettings = _TimeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 8)
)


class _TimeCurrentTime_Type(DisplayString):
    """Custom type timeCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TimeCurrentTime_Type.__name__ = "DisplayString"
_TimeCurrentTime_Object = MibScalar
timeCurrentTime = _TimeCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 8, 1),
    _TimeCurrentTime_Type()
)
timeCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeCurrentTime.setStatus("current")


class _TimeTimeZone_Type(Integer32):
    """Custom type timeTimeZone based on Integer32"""
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
        *(("gmt00UkGreenWichCasablancaMonrovia", 0),
          ("gmteast01Europe", 16),
          ("gmteast02EgyptFinlandRomaniaTurkeyGreeceIsraelJordan", 17),
          ("gmteast03IraqSyriaRussia", 18),
          ("gmteast04ArmeniaAzerbaijan", 20),
          ("gmteast05RussiaPakistan", 22),
          ("gmteast06BangladeshRussia", 24),
          ("gmteast07RussiaThailandCombodiaLaos", 26),
          ("gmteast08RussiaChinaMongoliaIndonesiaPhilippinesTaiwanWA", 27),
          ("gmteast09RussiaJapanKorea", 28),
          ("gmteast10EasternStandardAustRussiaGaumPapuaNewGuinea", 30),
          ("gmteast3dot5Iran", 19),
          ("gmteast4dot5Afghanistan", 21),
          ("gmteast5dot5India", 23),
          ("gmteast6dot5Burma", 25),
          ("gmteast9dot5AdelaideDarwin", 29),
          ("gmtwest01AzoresCapeVerdeIs", 15),
          ("gmtwest02MidAtlantic", 14),
          ("gmtwest03BrasiliaBeunosAiresGeorgetown", 13),
          ("gmtwest04CaracasLaPaz", 11),
          ("gmtwest05EasternTimeUsBogotaLimaQuitoIndianaEast", 10),
          ("gmtwest06CentralTimeUsMexicoCityTequciqalpa", 9),
          ("gmtwest07MountainTimeUsArizona", 8),
          ("gmtwest08PacificTimeUsCanada", 7),
          ("gmtwest09Alaska", 5),
          ("gmtwest10Hawaii", 3),
          ("gmtwest11MidwayIslandSamoa", 2),
          ("gmtwest12EniwetokKwajalein", 1),
          ("gmtwest3dot5Newfoundland", 12),
          ("gmtwest8dot5PitciarnIs", 6),
          ("gmtwest9dot5MarqesasIs", 4))
    )


_TimeTimeZone_Type.__name__ = "Integer32"
_TimeTimeZone_Object = MibScalar
timeTimeZone = _TimeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 8, 2),
    _TimeTimeZone_Type()
)
timeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeTimeZone.setStatus("current")
_TimeDaylightSaving_Type = TruthValue
_TimeDaylightSaving_Object = MibScalar
timeDaylightSaving = _TimeDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 8, 3),
    _TimeDaylightSaving_Type()
)
timeDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSaving.setStatus("current")


class _TimeNtpServer_Type(DisplayString):
    """Custom type timeNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TimeNtpServer_Type.__name__ = "DisplayString"
_TimeNtpServer_Object = MibScalar
timeNtpServer = _TimeNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 8, 4),
    _TimeNtpServer_Type()
)
timeNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNtpServer.setStatus("current")
_IpSettings_ObjectIdentity = ObjectIdentity
ipSettings = _IpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 9)
)
_IpDhcpClientEnable_Type = TruthValue
_IpDhcpClientEnable_Object = MibScalar
ipDhcpClientEnable = _IpDhcpClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 9, 1),
    _IpDhcpClientEnable_Type()
)
ipDhcpClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpClientEnable.setStatus("current")
_IpIPAddress_Type = IpAddress
_IpIPAddress_Object = MibScalar
ipIPAddress = _IpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 9, 2),
    _IpIPAddress_Type()
)
ipIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIPAddress.setStatus("current")
_IpNetmask_Type = IpAddress
_IpNetmask_Object = MibScalar
ipNetmask = _IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 9, 3),
    _IpNetmask_Type()
)
ipNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetmask.setStatus("current")
_IpGateway_Type = IpAddress
_IpGateway_Object = MibScalar
ipGateway = _IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 9, 4),
    _IpGateway_Type()
)
ipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGateway.setStatus("current")
_IpDnsServer_Type = IpAddress
_IpDnsServer_Object = MibScalar
ipDnsServer = _IpDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1, 9, 5),
    _IpDnsServer_Type()
)
ipDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsServer.setStatus("current")
_WlanSettings_ObjectIdentity = ObjectIdentity
wlanSettings = _WlanSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2)
)
_WlanSettingTable_Object = MibTable
wlanSettingTable = _WlanSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wlanSettingTable.setStatus("current")
_WlanSettingEntry_Object = MibTableRow
wlanSettingEntry = _WlanSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1)
)
wlanSettingEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
)
if mibBuilder.loadTexts:
    wlanSettingEntry.setStatus("current")


class _RadioIndex_Type(Integer32):
    """Custom type radioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 0),
          ("dot11bg", 1))
    )


_RadioIndex_Type.__name__ = "Integer32"
_RadioIndex_Object = MibTableColumn
radioIndex = _RadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 1),
    _RadioIndex_Type()
)
radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIndex.setStatus("current")
_RadioEnable_Type = TruthValue
_RadioEnable_Object = MibTableColumn
radioEnable = _RadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 2),
    _RadioEnable_Type()
)
radioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioEnable.setStatus("current")


class _WirelessMode_Type(Integer32):
    """Custom type wirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_WirelessMode_Type.__name__ = "Integer32"
_WirelessMode_Object = MibTableColumn
wirelessMode = _WirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 5),
    _WirelessMode_Type()
)
wirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMode.setStatus("current")


class _Channel_Type(Integer32):
    """Custom type channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 165),
    )


_Channel_Type.__name__ = "Integer32"
_Channel_Object = MibTableColumn
channel = _Channel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 6),
    _Channel_Type()
)
channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channel.setStatus("current")


class _TxRate_Type(Integer32):
    """Custom type txRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("best", 0),
          ("rate11Mbps", 6),
          ("rate12Mbps", 7),
          ("rate18Mbps", 8),
          ("rate1Mbps", 1),
          ("rate24Mbps", 9),
          ("rate2Mbps", 2),
          ("rate36Mbps", 10),
          ("rate48Mbps", 11),
          ("rate54Mbps", 12),
          ("rate5dot5Mbps", 3),
          ("rate6Mbps", 4),
          ("rate9Mbps", 5))
    )


_TxRate_Type.__name__ = "Integer32"
_TxRate_Object = MibTableColumn
txRate = _TxRate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 7),
    _TxRate_Type()
)
txRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txRate.setStatus("current")


class _TxPower_Type(Integer32):
    """Custom type txPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 3),
          ("full", 0),
          ("half", 1),
          ("min", 4),
          ("quarter", 2))
    )


_TxPower_Type.__name__ = "Integer32"
_TxPower_Object = MibTableColumn
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 8),
    _TxPower_Type()
)
txPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txPower.setStatus("current")


class _BeaconInterval_Type(Integer32):
    """Custom type beaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_BeaconInterval_Type.__name__ = "Integer32"
_BeaconInterval_Object = MibTableColumn
beaconInterval = _BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 9),
    _BeaconInterval_Type()
)
beaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    beaconInterval.setUnits("1024 microsecond")


class _DtimInterval_Type(Integer32):
    """Custom type dtimInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtimInterval_Type.__name__ = "Integer32"
_DtimInterval_Object = MibTableColumn
dtimInterval = _DtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 10),
    _DtimInterval_Type()
)
dtimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtimInterval.setStatus("current")


class _RtsThreshold_Type(Integer32):
    """Custom type rtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2346),
    )


_RtsThreshold_Type.__name__ = "Integer32"
_RtsThreshold_Object = MibTableColumn
rtsThreshold = _RtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 11),
    _RtsThreshold_Type()
)
rtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsThreshold.setStatus("current")


class _FragmentationThreshold_Type(Integer32):
    """Custom type fragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_FragmentationThreshold_Type.__name__ = "Integer32"
_FragmentationThreshold_Object = MibTableColumn
fragmentationThreshold = _FragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 12),
    _FragmentationThreshold_Type()
)
fragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fragmentationThreshold.setStatus("current")


class _Dot11bPreamble_Type(Integer32):
    """Custom type dot11bPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("long", 0))
    )


_Dot11bPreamble_Type.__name__ = "Integer32"
_Dot11bPreamble_Object = MibTableColumn
dot11bPreamble = _Dot11bPreamble_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 13),
    _Dot11bPreamble_Type()
)
dot11bPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11bPreamble.setStatus("current")
_SuperMode_Type = TruthValue
_SuperMode_Object = MibTableColumn
superMode = _SuperMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 14),
    _SuperMode_Type()
)
superMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superMode.setStatus("current")
_Wmm_Type = TruthValue
_Wmm_Object = MibTableColumn
wmm = _Wmm_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 15),
    _Wmm_Type()
)
wmm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmm.setStatus("current")
_WmmNoAck_Type = TruthValue
_WmmNoAck_Object = MibTableColumn
wmmNoAck = _WmmNoAck_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 16),
    _WmmNoAck_Type()
)
wmmNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmmNoAck.setStatus("current")
_AcEnabled_Type = TruthValue
_AcEnabled_Object = MibTableColumn
acEnabled = _AcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 17),
    _AcEnabled_Type()
)
acEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEnabled.setStatus("current")


class _AcEnhancedRFSecurity_Type(Integer32):
    """Custom type acEnhancedRFSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 3))
    )


_AcEnhancedRFSecurity_Type.__name__ = "Integer32"
_AcEnhancedRFSecurity_Object = MibTableColumn
acEnhancedRFSecurity = _AcEnhancedRFSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 18),
    _AcEnhancedRFSecurity_Type()
)
acEnhancedRFSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEnhancedRFSecurity.setStatus("current")
_AcRogueDevDetection_Type = TruthValue
_AcRogueDevDetection_Object = MibTableColumn
acRogueDevDetection = _AcRogueDevDetection_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 19),
    _AcRogueDevDetection_Type()
)
acRogueDevDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acRogueDevDetection.setStatus("current")


class _AccessControlMode_Type(Integer32):
    """Custom type accessControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("local", 2),
          ("server", 3))
    )


_AccessControlMode_Type.__name__ = "Integer32"
_AccessControlMode_Object = MibTableColumn
accessControlMode = _AccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 1, 1, 20),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("current")
_WlanSecurityTable_Object = MibTable
wlanSecurityTable = _WlanSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wlanSecurityTable.setStatus("current")
_WlanSecurityEntry_Object = MibTableRow
wlanSecurityEntry = _WlanSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1)
)
wlanSecurityEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "securityProfileNo"),
)
if mibBuilder.loadTexts:
    wlanSecurityEntry.setStatus("current")


class _SecurityProfileNo_Type(Integer32):
    """Custom type securityProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SecurityProfileNo_Type.__name__ = "Integer32"
_SecurityProfileNo_Object = MibTableColumn
securityProfileNo = _SecurityProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 1),
    _SecurityProfileNo_Type()
)
securityProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityProfileNo.setStatus("current")
_SecurityProfileEnabled_Type = TruthValue
_SecurityProfileEnabled_Object = MibTableColumn
securityProfileEnabled = _SecurityProfileEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 2),
    _SecurityProfileEnabled_Type()
)
securityProfileEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfileEnabled.setStatus("current")


class _SecurityProfileName_Type(DisplayString):
    """Custom type securityProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SecurityProfileName_Type.__name__ = "DisplayString"
_SecurityProfileName_Object = MibTableColumn
securityProfileName = _SecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 3),
    _SecurityProfileName_Type()
)
securityProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfileName.setStatus("current")


class _Ssid_Type(DisplayString):
    """Custom type ssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Ssid_Type.__name__ = "DisplayString"
_Ssid_Object = MibTableColumn
ssid = _Ssid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 4),
    _Ssid_Type()
)
ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssid.setStatus("current")
_SsidBroadcastEnable_Type = TruthValue
_SsidBroadcastEnable_Object = MibTableColumn
ssidBroadcastEnable = _SsidBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 5),
    _SsidBroadcastEnable_Type()
)
ssidBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssidBroadcastEnable.setStatus("current")


class _Authentication_Type(Integer32):
    """Custom type authentication based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("legacy8021x", 2),
          ("openSystem", 0),
          ("sharedKey", 1),
          ("wpa2-802dot1x", 7),
          ("wpa2-psk", 5),
          ("wpaPSK", 3),
          ("wpaRadius", 4),
          ("wpawpa2-802dot1x", 8),
          ("wpawpa2-psk", 6))
    )


_Authentication_Type.__name__ = "Integer32"
_Authentication_Object = MibTableColumn
authentication = _Authentication_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 6),
    _Authentication_Type()
)
authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authentication.setStatus("current")


class _Encryption_Type(Integer32):
    """Custom type encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aes", 6),
          ("aes-tkip", 5),
          ("none", 0),
          ("tkip", 4),
          ("wep128", 2),
          ("wep152", 3),
          ("wep64", 1))
    )


_Encryption_Type.__name__ = "Integer32"
_Encryption_Object = MibTableColumn
encryption = _Encryption_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 7),
    _Encryption_Type()
)
encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption.setStatus("current")


class _WepKey1_Type(DisplayString):
    """Custom type wepKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WepKey1_Type.__name__ = "DisplayString"
_WepKey1_Object = MibTableColumn
wepKey1 = _WepKey1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 8),
    _WepKey1_Type()
)
wepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKey1.setStatus("current")


class _WepKey2_Type(DisplayString):
    """Custom type wepKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WepKey2_Type.__name__ = "DisplayString"
_WepKey2_Object = MibTableColumn
wepKey2 = _WepKey2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 9),
    _WepKey2_Type()
)
wepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKey2.setStatus("current")


class _WepKey3_Type(DisplayString):
    """Custom type wepKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WepKey3_Type.__name__ = "DisplayString"
_WepKey3_Object = MibTableColumn
wepKey3 = _WepKey3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 10),
    _WepKey3_Type()
)
wepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKey3.setStatus("current")


class _WepKey4_Type(DisplayString):
    """Custom type wepKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WepKey4_Type.__name__ = "DisplayString"
_WepKey4_Object = MibTableColumn
wepKey4 = _WepKey4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 11),
    _WepKey4_Type()
)
wepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKey4.setStatus("current")


class _WepKeyDefault_Type(Integer32):
    """Custom type wepKeyDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WepKeyDefault_Type.__name__ = "Integer32"
_WepKeyDefault_Object = MibTableColumn
wepKeyDefault = _WepKeyDefault_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 12),
    _WepKeyDefault_Type()
)
wepKeyDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKeyDefault.setStatus("current")


class _WpaPSK_Type(DisplayString):
    """Custom type wpaPSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WpaPSK_Type.__name__ = "DisplayString"
_WpaPSK_Object = MibTableColumn
wpaPSK = _WpaPSK_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 13),
    _WpaPSK_Type()
)
wpaPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wpaPSK.setStatus("current")
_WlanSeparatorEnable_Type = TruthValue
_WlanSeparatorEnable_Object = MibTableColumn
wlanSeparatorEnable = _WlanSeparatorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 14),
    _WlanSeparatorEnable_Type()
)
wlanSeparatorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSeparatorEnable.setStatus("current")


class _WlanMaxUser_Type(Integer32):
    """Custom type wlanMaxUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WlanMaxUser_Type.__name__ = "Integer32"
_WlanMaxUser_Object = MibTableColumn
wlanMaxUser = _WlanMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 2, 1, 15),
    _WlanMaxUser_Type()
)
wlanMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMaxUser.setStatus("current")
_WlanAccessControlLocalTable_Object = MibTable
wlanAccessControlLocalTable = _WlanAccessControlLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 3)
)
if mibBuilder.loadTexts:
    wlanAccessControlLocalTable.setStatus("current")
_WlanAccessControlLocalEntry_Object = MibTableRow
wlanAccessControlLocalEntry = _WlanAccessControlLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 3, 1)
)
wlanAccessControlLocalEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "aclIndex"),
)
if mibBuilder.loadTexts:
    wlanAccessControlLocalEntry.setStatus("current")


class _AclIndex_Type(Integer32):
    """Custom type aclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
        ValueRangeConstraint(9999, 9999),
    )


_AclIndex_Type.__name__ = "Integer32"
_AclIndex_Object = MibTableColumn
aclIndex = _AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 3, 1, 1),
    _AclIndex_Type()
)
aclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIndex.setStatus("current")


class _AclMAC_Type(DisplayString):
    """Custom type aclMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_AclMAC_Type.__name__ = "DisplayString"
_AclMAC_Object = MibTableColumn
aclMAC = _AclMAC_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 3, 1, 2),
    _AclMAC_Type()
)
aclMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMAC.setStatus("current")
_WlanWdsTable_Object = MibTable
wlanWdsTable = _WlanWdsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4)
)
if mibBuilder.loadTexts:
    wlanWdsTable.setStatus("current")
_WlanWdsEntry_Object = MibTableRow
wlanWdsEntry = _WlanWdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1)
)
wlanWdsEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
)
if mibBuilder.loadTexts:
    wlanWdsEntry.setStatus("current")


class _OperationMode_Type(Integer32):
    """Custom type operationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ap", 0),
          ("ptp", 2),
          ("ptpAP", 3),
          ("pxp", 4),
          ("pxpAP", 5),
          ("repeater", 6))
    )


_OperationMode_Type.__name__ = "Integer32"
_OperationMode_Object = MibTableColumn
operationMode = _OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 1),
    _OperationMode_Type()
)
operationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationMode.setStatus("current")


class _LocalMacAddress_Type(DisplayString):
    """Custom type localMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_LocalMacAddress_Type.__name__ = "DisplayString"
_LocalMacAddress_Object = MibTableColumn
localMacAddress = _LocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 2),
    _LocalMacAddress_Type()
)
localMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localMacAddress.setStatus("current")


class _PtpRemoteMacAddress_Type(DisplayString):
    """Custom type ptpRemoteMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_PtpRemoteMacAddress_Type.__name__ = "DisplayString"
_PtpRemoteMacAddress_Object = MibTableColumn
ptpRemoteMacAddress = _PtpRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 3),
    _PtpRemoteMacAddress_Type()
)
ptpRemoteMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpRemoteMacAddress.setStatus("current")


class _PxpRemoteMacAddress1_Type(DisplayString):
    """Custom type pxpRemoteMacAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_PxpRemoteMacAddress1_Type.__name__ = "DisplayString"
_PxpRemoteMacAddress1_Object = MibTableColumn
pxpRemoteMacAddress1 = _PxpRemoteMacAddress1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 4),
    _PxpRemoteMacAddress1_Type()
)
pxpRemoteMacAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpRemoteMacAddress1.setStatus("current")


class _PxpRemoteMacAddress2_Type(DisplayString):
    """Custom type pxpRemoteMacAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_PxpRemoteMacAddress2_Type.__name__ = "DisplayString"
_PxpRemoteMacAddress2_Object = MibTableColumn
pxpRemoteMacAddress2 = _PxpRemoteMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 5),
    _PxpRemoteMacAddress2_Type()
)
pxpRemoteMacAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpRemoteMacAddress2.setStatus("current")


class _PxpRemoteMacAddress3_Type(DisplayString):
    """Custom type pxpRemoteMacAddress3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_PxpRemoteMacAddress3_Type.__name__ = "DisplayString"
_PxpRemoteMacAddress3_Object = MibTableColumn
pxpRemoteMacAddress3 = _PxpRemoteMacAddress3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 6),
    _PxpRemoteMacAddress3_Type()
)
pxpRemoteMacAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpRemoteMacAddress3.setStatus("current")


class _PxpRemoteMacAddress4_Type(DisplayString):
    """Custom type pxpRemoteMacAddress4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_PxpRemoteMacAddress4_Type.__name__ = "DisplayString"
_PxpRemoteMacAddress4_Object = MibTableColumn
pxpRemoteMacAddress4 = _PxpRemoteMacAddress4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 7),
    _PxpRemoteMacAddress4_Type()
)
pxpRemoteMacAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpRemoteMacAddress4.setStatus("current")


class _RepeaterParentMacAddress_Type(DisplayString):
    """Custom type repeaterParentMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_RepeaterParentMacAddress_Type.__name__ = "DisplayString"
_RepeaterParentMacAddress_Object = MibTableColumn
repeaterParentMacAddress = _RepeaterParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 8),
    _RepeaterParentMacAddress_Type()
)
repeaterParentMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterParentMacAddress.setStatus("current")


class _RepeaterChildMacAddress_Type(DisplayString):
    """Custom type repeaterChildMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_RepeaterChildMacAddress_Type.__name__ = "DisplayString"
_RepeaterChildMacAddress_Object = MibTableColumn
repeaterChildMacAddress = _RepeaterChildMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 4, 1, 9),
    _RepeaterChildMacAddress_Type()
)
repeaterChildMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterChildMacAddress.setStatus("current")
_WlanClientsTable_Object = MibTable
wlanClientsTable = _WlanClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5)
)
if mibBuilder.loadTexts:
    wlanClientsTable.setStatus("current")
_WlanClientsEntry_Object = MibTableRow
wlanClientsEntry = _WlanClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5, 1)
)
wlanClientsEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "clientIndex"),
)
if mibBuilder.loadTexts:
    wlanClientsEntry.setStatus("current")


class _ClientIndex_Type(Integer32):
    """Custom type clientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClientIndex_Type.__name__ = "Integer32"
_ClientIndex_Object = MibTableColumn
clientIndex = _ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5, 1, 1),
    _ClientIndex_Type()
)
clientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIndex.setStatus("current")


class _ClientMacAddress_Type(DisplayString):
    """Custom type clientMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_ClientMacAddress_Type.__name__ = "DisplayString"
_ClientMacAddress_Object = MibTableColumn
clientMacAddress = _ClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5, 1, 2),
    _ClientMacAddress_Type()
)
clientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMacAddress.setStatus("current")
_ClientIP_Type = IpAddress
_ClientIP_Object = MibTableColumn
clientIP = _ClientIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5, 1, 3),
    _ClientIP_Type()
)
clientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIP.setStatus("current")


class _ClientSSID_Type(DisplayString):
    """Custom type clientSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClientSSID_Type.__name__ = "DisplayString"
_ClientSSID_Object = MibTableColumn
clientSSID = _ClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5, 1, 4),
    _ClientSSID_Type()
)
clientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientSSID.setStatus("current")


class _ClientStatus_Type(Integer32):
    """Custom type clientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("associated", 4),
          ("associating", 3),
          ("authenticated", 2),
          ("authenticating", 1),
          ("blocked", 0))
    )


_ClientStatus_Type.__name__ = "Integer32"
_ClientStatus_Object = MibTableColumn
clientStatus = _ClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 5, 1, 5),
    _ClientStatus_Type()
)
clientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatus.setStatus("current")
_WlanUnknownApTable_Object = MibTable
wlanUnknownApTable = _WlanUnknownApTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6)
)
if mibBuilder.loadTexts:
    wlanUnknownApTable.setStatus("current")
_WlanUnknownApEntry_Object = MibTableRow
wlanUnknownApEntry = _WlanUnknownApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1)
)
wlanUnknownApEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "unknowApIndex"),
)
if mibBuilder.loadTexts:
    wlanUnknownApEntry.setStatus("current")


class _UnknowApIndex_Type(Integer32):
    """Custom type unknowApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UnknowApIndex_Type.__name__ = "Integer32"
_UnknowApIndex_Object = MibTableColumn
unknowApIndex = _UnknowApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1, 1),
    _UnknowApIndex_Type()
)
unknowApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowApIndex.setStatus("current")
_UnknowApAuthorize_Type = TruthValue
_UnknowApAuthorize_Object = MibTableColumn
unknowApAuthorize = _UnknowApAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1, 2),
    _UnknowApAuthorize_Type()
)
unknowApAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknowApAuthorize.setStatus("current")


class _UnknowApSSID_Type(DisplayString):
    """Custom type unknowApSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UnknowApSSID_Type.__name__ = "DisplayString"
_UnknowApSSID_Object = MibTableColumn
unknowApSSID = _UnknowApSSID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1, 3),
    _UnknowApSSID_Type()
)
unknowApSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowApSSID.setStatus("current")


class _UnknowApMacAddress_Type(DisplayString):
    """Custom type unknowApMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_UnknowApMacAddress_Type.__name__ = "DisplayString"
_UnknowApMacAddress_Object = MibTableColumn
unknowApMacAddress = _UnknowApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1, 4),
    _UnknowApMacAddress_Type()
)
unknowApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowApMacAddress.setStatus("current")


class _UnknowApChannel_Type(DisplayString):
    """Custom type unknowApChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_UnknowApChannel_Type.__name__ = "DisplayString"
_UnknowApChannel_Object = MibTableColumn
unknowApChannel = _UnknowApChannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1, 5),
    _UnknowApChannel_Type()
)
unknowApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowApChannel.setStatus("current")


class _UnknowApAutoCellEnabled_Type(DisplayString):
    """Custom type unknowApAutoCellEnabled based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_UnknowApAutoCellEnabled_Type.__name__ = "DisplayString"
_UnknowApAutoCellEnabled_Object = MibTableColumn
unknowApAutoCellEnabled = _UnknowApAutoCellEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 6, 1, 6),
    _UnknowApAutoCellEnabled_Type()
)
unknowApAutoCellEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowApAutoCellEnabled.setStatus("current")
_WlanAuthorizedApTable_Object = MibTable
wlanAuthorizedApTable = _WlanAuthorizedApTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7)
)
if mibBuilder.loadTexts:
    wlanAuthorizedApTable.setStatus("current")
_WlanAuthorizedApEntry_Object = MibTableRow
wlanAuthorizedApEntry = _WlanAuthorizedApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1)
)
wlanAuthorizedApEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "unknowApIndex"),
)
if mibBuilder.loadTexts:
    wlanAuthorizedApEntry.setStatus("current")


class _AuthorizedApIndex_Type(Integer32):
    """Custom type authorizedApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AuthorizedApIndex_Type.__name__ = "Integer32"
_AuthorizedApIndex_Object = MibTableColumn
authorizedApIndex = _AuthorizedApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1, 1),
    _AuthorizedApIndex_Type()
)
authorizedApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedApIndex.setStatus("current")
_AuthorizedApDelete_Type = TruthValue
_AuthorizedApDelete_Object = MibTableColumn
authorizedApDelete = _AuthorizedApDelete_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1, 2),
    _AuthorizedApDelete_Type()
)
authorizedApDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizedApDelete.setStatus("current")


class _AuthorizedApSSID_Type(DisplayString):
    """Custom type authorizedApSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AuthorizedApSSID_Type.__name__ = "DisplayString"
_AuthorizedApSSID_Object = MibTableColumn
authorizedApSSID = _AuthorizedApSSID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1, 3),
    _AuthorizedApSSID_Type()
)
authorizedApSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedApSSID.setStatus("current")


class _AuthorizedApMacAddress_Type(DisplayString):
    """Custom type authorizedApMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_AuthorizedApMacAddress_Type.__name__ = "DisplayString"
_AuthorizedApMacAddress_Object = MibTableColumn
authorizedApMacAddress = _AuthorizedApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1, 4),
    _AuthorizedApMacAddress_Type()
)
authorizedApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedApMacAddress.setStatus("current")


class _AuthorizedApChannel_Type(DisplayString):
    """Custom type authorizedApChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_AuthorizedApChannel_Type.__name__ = "DisplayString"
_AuthorizedApChannel_Object = MibTableColumn
authorizedApChannel = _AuthorizedApChannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1, 5),
    _AuthorizedApChannel_Type()
)
authorizedApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedApChannel.setStatus("current")


class _AuthorizedApAutoCellEnabled_Type(DisplayString):
    """Custom type authorizedApAutoCellEnabled based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_AuthorizedApAutoCellEnabled_Type.__name__ = "DisplayString"
_AuthorizedApAutoCellEnabled_Object = MibTableColumn
authorizedApAutoCellEnabled = _AuthorizedApAutoCellEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 7, 1, 6),
    _AuthorizedApAutoCellEnabled_Type()
)
authorizedApAutoCellEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedApAutoCellEnabled.setStatus("current")
_WlanUnknownStationTable_Object = MibTable
wlanUnknownStationTable = _WlanUnknownStationTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8)
)
if mibBuilder.loadTexts:
    wlanUnknownStationTable.setStatus("current")
_WlanUnknownStationEntry_Object = MibTableRow
wlanUnknownStationEntry = _WlanUnknownStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8, 1)
)
wlanUnknownStationEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "unknowStationIndex"),
)
if mibBuilder.loadTexts:
    wlanUnknownStationEntry.setStatus("current")


class _UnknowStationIndex_Type(Integer32):
    """Custom type unknowStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UnknowStationIndex_Type.__name__ = "Integer32"
_UnknowStationIndex_Object = MibTableColumn
unknowStationIndex = _UnknowStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8, 1, 1),
    _UnknowStationIndex_Type()
)
unknowStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowStationIndex.setStatus("current")
_UnknowStationAuthorize_Type = TruthValue
_UnknowStationAuthorize_Object = MibTableColumn
unknowStationAuthorize = _UnknowStationAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8, 1, 2),
    _UnknowStationAuthorize_Type()
)
unknowStationAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknowStationAuthorize.setStatus("current")


class _UnknowStationMacAddress_Type(DisplayString):
    """Custom type unknowStationMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_UnknowStationMacAddress_Type.__name__ = "DisplayString"
_UnknowStationMacAddress_Object = MibTableColumn
unknowStationMacAddress = _UnknowStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8, 1, 3),
    _UnknowStationMacAddress_Type()
)
unknowStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowStationMacAddress.setStatus("current")


class _UnknowStationChannel_Type(DisplayString):
    """Custom type unknowStationChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_UnknowStationChannel_Type.__name__ = "DisplayString"
_UnknowStationChannel_Object = MibTableColumn
unknowStationChannel = _UnknowStationChannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8, 1, 4),
    _UnknowStationChannel_Type()
)
unknowStationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowStationChannel.setStatus("current")


class _UnknowStationAutoCellEnabled_Type(DisplayString):
    """Custom type unknowStationAutoCellEnabled based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_UnknowStationAutoCellEnabled_Type.__name__ = "DisplayString"
_UnknowStationAutoCellEnabled_Object = MibTableColumn
unknowStationAutoCellEnabled = _UnknowStationAutoCellEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 8, 1, 5),
    _UnknowStationAutoCellEnabled_Type()
)
unknowStationAutoCellEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknowStationAutoCellEnabled.setStatus("current")
_WlanAuthorizedStationTable_Object = MibTable
wlanAuthorizedStationTable = _WlanAuthorizedStationTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9)
)
if mibBuilder.loadTexts:
    wlanAuthorizedStationTable.setStatus("current")
_WlanAuthorizedStationEntry_Object = MibTableRow
wlanAuthorizedStationEntry = _WlanAuthorizedStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9, 1)
)
wlanAuthorizedStationEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
    (0, "WG102", "unknowStationIndex"),
)
if mibBuilder.loadTexts:
    wlanAuthorizedStationEntry.setStatus("current")


class _AuthorizedStationIndex_Type(Integer32):
    """Custom type authorizedStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AuthorizedStationIndex_Type.__name__ = "Integer32"
_AuthorizedStationIndex_Object = MibTableColumn
authorizedStationIndex = _AuthorizedStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9, 1, 1),
    _AuthorizedStationIndex_Type()
)
authorizedStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedStationIndex.setStatus("current")
_AuthorizedStationDelete_Type = TruthValue
_AuthorizedStationDelete_Object = MibTableColumn
authorizedStationDelete = _AuthorizedStationDelete_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9, 1, 2),
    _AuthorizedStationDelete_Type()
)
authorizedStationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizedStationDelete.setStatus("current")


class _AuthorizedStationMacAddress_Type(DisplayString):
    """Custom type authorizedStationMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 17),
    )


_AuthorizedStationMacAddress_Type.__name__ = "DisplayString"
_AuthorizedStationMacAddress_Object = MibTableColumn
authorizedStationMacAddress = _AuthorizedStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9, 1, 3),
    _AuthorizedStationMacAddress_Type()
)
authorizedStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedStationMacAddress.setStatus("current")


class _AuthorizedStationChannel_Type(DisplayString):
    """Custom type authorizedStationChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_AuthorizedStationChannel_Type.__name__ = "DisplayString"
_AuthorizedStationChannel_Object = MibTableColumn
authorizedStationChannel = _AuthorizedStationChannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9, 1, 4),
    _AuthorizedStationChannel_Type()
)
authorizedStationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedStationChannel.setStatus("current")


class _AuthorizedStationAutoCellEnabled_Type(DisplayString):
    """Custom type authorizedStationAutoCellEnabled based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_AuthorizedStationAutoCellEnabled_Type.__name__ = "DisplayString"
_AuthorizedStationAutoCellEnabled_Object = MibTableColumn
authorizedStationAutoCellEnabled = _AuthorizedStationAutoCellEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 2, 9, 1, 5),
    _AuthorizedStationAutoCellEnabled_Type()
)
authorizedStationAutoCellEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizedStationAutoCellEnabled.setStatus("current")
_VlanSettings_ObjectIdentity = ObjectIdentity
vlanSettings = _VlanSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3)
)
_VlanEnable_Type = TruthValue
_VlanEnable_Object = MibScalar
vlanEnable = _VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3, 1),
    _VlanEnable_Type()
)
vlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEnable.setStatus("current")


class _ManagementVlanId_Type(Integer32):
    """Custom type managementVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ManagementVlanId_Type.__name__ = "Integer32"
_ManagementVlanId_Object = MibScalar
managementVlanId = _ManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3, 2),
    _ManagementVlanId_Type()
)
managementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVlanId.setStatus("current")
_SecurityProfileVlanTable_Object = MibTable
securityProfileVlanTable = _SecurityProfileVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3, 3)
)
if mibBuilder.loadTexts:
    securityProfileVlanTable.setStatus("current")
_SecurityProfileVlanEntry_Object = MibTableRow
securityProfileVlanEntry = _SecurityProfileVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3, 3, 1)
)
securityProfileVlanEntry.setIndexNames(
    (0, "WG102", "wlanSecurityProfileNo"),
)
if mibBuilder.loadTexts:
    securityProfileVlanEntry.setStatus("current")


class _ProfileNo_Type(Integer32):
    """Custom type profileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ProfileNo_Type.__name__ = "Integer32"
_ProfileNo_Object = MibTableColumn
profileNo = _ProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3, 3, 1, 1),
    _ProfileNo_Type()
)
profileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileNo.setStatus("current")


class _ProfileVlan_Type(Integer32):
    """Custom type profileVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ProfileVlan_Type.__name__ = "Integer32"
_ProfileVlan_Object = MibTableColumn
profileVlan = _ProfileVlan_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 3, 3, 1, 2),
    _ProfileVlan_Type()
)
profileVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileVlan.setStatus("current")
_SysStatistics_ObjectIdentity = ObjectIdentity
sysStatistics = _SysStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4)
)
_EthernetStat_ObjectIdentity = ObjectIdentity
ethernetStat = _EthernetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 1)
)
_EthInPackets_Type = Unsigned32
_EthInPackets_Object = MibScalar
ethInPackets = _EthInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 1, 1),
    _EthInPackets_Type()
)
ethInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInPackets.setStatus("current")
_EthOutPackets_Type = Unsigned32
_EthOutPackets_Object = MibScalar
ethOutPackets = _EthOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 1, 2),
    _EthOutPackets_Type()
)
ethOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutPackets.setStatus("current")
_EthInBytes_Type = Unsigned32
_EthInBytes_Object = MibScalar
ethInBytes = _EthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 1, 3),
    _EthInBytes_Type()
)
ethInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethInBytes.setStatus("current")
_EthOutBytes_Type = Unsigned32
_EthOutBytes_Object = MibScalar
ethOutBytes = _EthOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 1, 4),
    _EthOutBytes_Type()
)
ethOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOutBytes.setStatus("current")
_WirelessStatTable_Object = MibTable
wirelessStatTable = _WirelessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2)
)
if mibBuilder.loadTexts:
    wirelessStatTable.setStatus("current")
_WirelessStatEntry_Object = MibTableRow
wirelessStatEntry = _WirelessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1)
)
wirelessStatEntry.setIndexNames(
    (0, "WG102", "radioIndex"),
)
if mibBuilder.loadTexts:
    wirelessStatEntry.setStatus("current")


class _WlanSecurityProfileNo_Type(Integer32):
    """Custom type wlanSecurityProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlanSecurityProfileNo_Type.__name__ = "Integer32"
_WlanSecurityProfileNo_Object = MibTableColumn
wlanSecurityProfileNo = _WlanSecurityProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 1),
    _WlanSecurityProfileNo_Type()
)
wlanSecurityProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSecurityProfileNo.setStatus("current")
_WlanInPacketsUnicast_Type = Unsigned32
_WlanInPacketsUnicast_Object = MibTableColumn
wlanInPacketsUnicast = _WlanInPacketsUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 2),
    _WlanInPacketsUnicast_Type()
)
wlanInPacketsUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInPacketsUnicast.setStatus("current")
_WlanOutPacketsUnicast_Type = Unsigned32
_WlanOutPacketsUnicast_Object = MibTableColumn
wlanOutPacketsUnicast = _WlanOutPacketsUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 3),
    _WlanOutPacketsUnicast_Type()
)
wlanOutPacketsUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanOutPacketsUnicast.setStatus("current")
_WlanInPacketsBroadcast_Type = Unsigned32
_WlanInPacketsBroadcast_Object = MibTableColumn
wlanInPacketsBroadcast = _WlanInPacketsBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 4),
    _WlanInPacketsBroadcast_Type()
)
wlanInPacketsBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInPacketsBroadcast.setStatus("current")
_WlanOutPacketsBroadcast_Type = Unsigned32
_WlanOutPacketsBroadcast_Object = MibTableColumn
wlanOutPacketsBroadcast = _WlanOutPacketsBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 5),
    _WlanOutPacketsBroadcast_Type()
)
wlanOutPacketsBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanOutPacketsBroadcast.setStatus("current")
_WlanInPacketsMulticast_Type = Unsigned32
_WlanInPacketsMulticast_Object = MibTableColumn
wlanInPacketsMulticast = _WlanInPacketsMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 6),
    _WlanInPacketsMulticast_Type()
)
wlanInPacketsMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInPacketsMulticast.setStatus("current")
_WlanOutPacketsMulticast_Type = Unsigned32
_WlanOutPacketsMulticast_Object = MibTableColumn
wlanOutPacketsMulticast = _WlanOutPacketsMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 7),
    _WlanOutPacketsMulticast_Type()
)
wlanOutPacketsMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanOutPacketsMulticast.setStatus("current")
_WlanInPacketsTotal_Type = Unsigned32
_WlanInPacketsTotal_Object = MibTableColumn
wlanInPacketsTotal = _WlanInPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 8),
    _WlanInPacketsTotal_Type()
)
wlanInPacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInPacketsTotal.setStatus("current")
_WlanOutPacketsTotal_Type = Unsigned32
_WlanOutPacketsTotal_Object = MibTableColumn
wlanOutPacketsTotal = _WlanOutPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 9),
    _WlanOutPacketsTotal_Type()
)
wlanOutPacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanOutPacketsTotal.setStatus("current")
_WlanInBytesTotal_Type = Unsigned32
_WlanInBytesTotal_Object = MibTableColumn
wlanInBytesTotal = _WlanInBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 10),
    _WlanInBytesTotal_Type()
)
wlanInBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanInBytesTotal.setStatus("current")
_WlanOutBytesTotal_Type = Unsigned32
_WlanOutBytesTotal_Object = MibTableColumn
wlanOutBytesTotal = _WlanOutBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 2, 1, 11),
    _WlanOutBytesTotal_Type()
)
wlanOutBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanOutBytesTotal.setStatus("current")
_EthWrongPackets_Type = Unsigned32
_EthWrongPackets_Object = MibScalar
ethWrongPackets = _EthWrongPackets_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 3),
    _EthWrongPackets_Type()
)
ethWrongPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethWrongPackets.setStatus("current")
_WrongWLANSTAPackets_Type = Unsigned32
_WrongWLANSTAPackets_Object = MibScalar
wrongWLANSTAPackets = _WrongWLANSTAPackets_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 4),
    _WrongWLANSTAPackets_Type()
)
wrongWLANSTAPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrongWLANSTAPackets.setStatus("current")
_WlanStationCount_Type = Unsigned32
_WlanStationCount_Object = MibScalar
wlanStationCount = _WlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 5),
    _WlanStationCount_Type()
)
wlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStationCount.setStatus("current")
_WirelessLinkStatTable_Object = MibTable
wirelessLinkStatTable = _WirelessLinkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6)
)
if mibBuilder.loadTexts:
    wirelessLinkStatTable.setStatus("current")
_WirelessLinkStatEntry_Object = MibTableRow
wirelessLinkStatEntry = _WirelessLinkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1)
)
wirelessLinkStatEntry.setIndexNames(
    (0, "WG102", "wirelessLinkStatIndex"),
)
if mibBuilder.loadTexts:
    wirelessLinkStatEntry.setStatus("current")


class _WirelessLinkStatIndex_Type(Integer32):
    """Custom type wirelessLinkStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_WirelessLinkStatIndex_Type.__name__ = "Integer32"
_WirelessLinkStatIndex_Object = MibTableColumn
wirelessLinkStatIndex = _WirelessLinkStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 1),
    _WirelessLinkStatIndex_Type()
)
wirelessLinkStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatIndex.setStatus("current")


class _WirelessLinkStatDate_Type(DisplayString):
    """Custom type wirelessLinkStatDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_WirelessLinkStatDate_Type.__name__ = "DisplayString"
_WirelessLinkStatDate_Object = MibTableColumn
wirelessLinkStatDate = _WirelessLinkStatDate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 2),
    _WirelessLinkStatDate_Type()
)
wirelessLinkStatDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatDate.setStatus("current")


class _WirelessLinkStatTime_Type(Integer32):
    """Custom type wirelessLinkStatTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WirelessLinkStatTime_Type.__name__ = "Integer32"
_WirelessLinkStatTime_Object = MibTableColumn
wirelessLinkStatTime = _WirelessLinkStatTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 3),
    _WirelessLinkStatTime_Type()
)
wirelessLinkStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatTime.setStatus("current")
_WirelessLinkStatRequest_Type = Unsigned32
_WirelessLinkStatRequest_Object = MibTableColumn
wirelessLinkStatRequest = _WirelessLinkStatRequest_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 4),
    _WirelessLinkStatRequest_Type()
)
wirelessLinkStatRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatRequest.setStatus("current")
_WirelessLinkStatResponse_Type = Unsigned32
_WirelessLinkStatResponse_Object = MibTableColumn
wirelessLinkStatResponse = _WirelessLinkStatResponse_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 5),
    _WirelessLinkStatResponse_Type()
)
wirelessLinkStatResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatResponse.setStatus("current")
_WirelessLinkStatGrant_Type = Unsigned32
_WirelessLinkStatGrant_Object = MibTableColumn
wirelessLinkStatGrant = _WirelessLinkStatGrant_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 6),
    _WirelessLinkStatGrant_Type()
)
wirelessLinkStatGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatGrant.setStatus("current")
_WirelessLinkStatDisconnect_Type = Unsigned32
_WirelessLinkStatDisconnect_Object = MibTableColumn
wirelessLinkStatDisconnect = _WirelessLinkStatDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 7),
    _WirelessLinkStatDisconnect_Type()
)
wirelessLinkStatDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatDisconnect.setStatus("current")
_WirelessLinkStatDisconnectAll_Type = Unsigned32
_WirelessLinkStatDisconnectAll_Object = MibTableColumn
wirelessLinkStatDisconnectAll = _WirelessLinkStatDisconnectAll_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 8),
    _WirelessLinkStatDisconnectAll_Type()
)
wirelessLinkStatDisconnectAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatDisconnectAll.setStatus("current")
_WirelessLinkStatFlag_Type = TruthValue
_WirelessLinkStatFlag_Object = MibTableColumn
wirelessLinkStatFlag = _WirelessLinkStatFlag_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 6, 1, 9),
    _WirelessLinkStatFlag_Type()
)
wirelessLinkStatFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessLinkStatFlag.setStatus("current")
_WlanAuthenticatedStationCount_Type = Unsigned32
_WlanAuthenticatedStationCount_Object = MibScalar
wlanAuthenticatedStationCount = _WlanAuthenticatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 8),
    _WlanAuthenticatedStationCount_Type()
)
wlanAuthenticatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAuthenticatedStationCount.setStatus("current")
_SysTotalMemory_Type = Unsigned32
_SysTotalMemory_Object = MibScalar
sysTotalMemory = _SysTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 9),
    _SysTotalMemory_Type()
)
sysTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTotalMemory.setStatus("current")
_SysFreeMemory_Type = Unsigned32
_SysFreeMemory_Object = MibScalar
sysFreeMemory = _SysFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 10),
    _SysFreeMemory_Type()
)
sysFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFreeMemory.setStatus("current")
_SysRuntime_Type = TimeTicks
_SysRuntime_Object = MibScalar
sysRuntime = _SysRuntime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 4, 11),
    _SysRuntime_Type()
)
sysRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRuntime.setStatus("current")
_RadiusSettings_ObjectIdentity = ObjectIdentity
radiusSettings = _RadiusSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5)
)
_RadiusAuthPrimaryServer_ObjectIdentity = ObjectIdentity
radiusAuthPrimaryServer = _RadiusAuthPrimaryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 1)
)
_RadiusAuthPrimaryServerIP_Type = IpAddress
_RadiusAuthPrimaryServerIP_Object = MibScalar
radiusAuthPrimaryServerIP = _RadiusAuthPrimaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 1, 1),
    _RadiusAuthPrimaryServerIP_Type()
)
radiusAuthPrimaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryServerIP.setStatus("current")


class _RadiusAuthPrimaryServerPort_Type(Integer32):
    """Custom type radiusAuthPrimaryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAuthPrimaryServerPort_Type.__name__ = "Integer32"
_RadiusAuthPrimaryServerPort_Object = MibScalar
radiusAuthPrimaryServerPort = _RadiusAuthPrimaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 1, 2),
    _RadiusAuthPrimaryServerPort_Type()
)
radiusAuthPrimaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryServerPort.setStatus("current")


class _RadiusAuthPrimaryServerSecret_Type(DisplayString):
    """Custom type radiusAuthPrimaryServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RadiusAuthPrimaryServerSecret_Type.__name__ = "DisplayString"
_RadiusAuthPrimaryServerSecret_Object = MibScalar
radiusAuthPrimaryServerSecret = _RadiusAuthPrimaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 1, 3),
    _RadiusAuthPrimaryServerSecret_Type()
)
radiusAuthPrimaryServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthPrimaryServerSecret.setStatus("current")
_RadiusAuthSecondaryServer_ObjectIdentity = ObjectIdentity
radiusAuthSecondaryServer = _RadiusAuthSecondaryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 2)
)
_RadiusAuthSecondaryServerIP_Type = IpAddress
_RadiusAuthSecondaryServerIP_Object = MibScalar
radiusAuthSecondaryServerIP = _RadiusAuthSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 2, 1),
    _RadiusAuthSecondaryServerIP_Type()
)
radiusAuthSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryServerIP.setStatus("current")


class _RadiusAuthSecondaryServerPort_Type(Integer32):
    """Custom type radiusAuthSecondaryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAuthSecondaryServerPort_Type.__name__ = "Integer32"
_RadiusAuthSecondaryServerPort_Object = MibScalar
radiusAuthSecondaryServerPort = _RadiusAuthSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 2, 2),
    _RadiusAuthSecondaryServerPort_Type()
)
radiusAuthSecondaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryServerPort.setStatus("current")


class _RadiusAuthSecondaryServerSecret_Type(DisplayString):
    """Custom type radiusAuthSecondaryServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RadiusAuthSecondaryServerSecret_Type.__name__ = "DisplayString"
_RadiusAuthSecondaryServerSecret_Object = MibScalar
radiusAuthSecondaryServerSecret = _RadiusAuthSecondaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 2, 3),
    _RadiusAuthSecondaryServerSecret_Type()
)
radiusAuthSecondaryServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSecondaryServerSecret.setStatus("current")
_AuthenticationSettings_ObjectIdentity = ObjectIdentity
authenticationSettings = _AuthenticationSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 3)
)


class _ReauthTime_Type(Integer32):
    """Custom type reauthTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 36000),
    )


_ReauthTime_Type.__name__ = "Integer32"
_ReauthTime_Object = MibScalar
reauthTime = _ReauthTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 3, 1),
    _ReauthTime_Type()
)
reauthTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reauthTime.setStatus("current")


class _WpaGroupKeyUpdateCondition_Type(Integer32):
    """Custom type wpaGroupKeyUpdateCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("never", 0),
          ("seconds", 1),
          ("secondsAndDisconnect", 3))
    )


_WpaGroupKeyUpdateCondition_Type.__name__ = "Integer32"
_WpaGroupKeyUpdateCondition_Object = MibScalar
wpaGroupKeyUpdateCondition = _WpaGroupKeyUpdateCondition_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 3, 2),
    _WpaGroupKeyUpdateCondition_Type()
)
wpaGroupKeyUpdateCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wpaGroupKeyUpdateCondition.setStatus("current")


class _WpaGroupKeyUpdateIntervalSecond_Type(Integer32):
    """Custom type wpaGroupKeyUpdateIntervalSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WpaGroupKeyUpdateIntervalSecond_Type.__name__ = "Integer32"
_WpaGroupKeyUpdateIntervalSecond_Object = MibScalar
wpaGroupKeyUpdateIntervalSecond = _WpaGroupKeyUpdateIntervalSecond_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 3, 3),
    _WpaGroupKeyUpdateIntervalSecond_Type()
)
wpaGroupKeyUpdateIntervalSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wpaGroupKeyUpdateIntervalSecond.setStatus("current")
_RadiusAccountPrimaryServer_ObjectIdentity = ObjectIdentity
radiusAccountPrimaryServer = _RadiusAccountPrimaryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 4)
)
_RadiusAccountPrimaryServerIP_Type = IpAddress
_RadiusAccountPrimaryServerIP_Object = MibScalar
radiusAccountPrimaryServerIP = _RadiusAccountPrimaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 4, 1),
    _RadiusAccountPrimaryServerIP_Type()
)
radiusAccountPrimaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountPrimaryServerIP.setStatus("current")


class _RadiusAccountPrimaryServerPort_Type(Integer32):
    """Custom type radiusAccountPrimaryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAccountPrimaryServerPort_Type.__name__ = "Integer32"
_RadiusAccountPrimaryServerPort_Object = MibScalar
radiusAccountPrimaryServerPort = _RadiusAccountPrimaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 4, 2),
    _RadiusAccountPrimaryServerPort_Type()
)
radiusAccountPrimaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountPrimaryServerPort.setStatus("current")


class _RadiusAccountPrimaryServerSecret_Type(DisplayString):
    """Custom type radiusAccountPrimaryServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RadiusAccountPrimaryServerSecret_Type.__name__ = "DisplayString"
_RadiusAccountPrimaryServerSecret_Object = MibScalar
radiusAccountPrimaryServerSecret = _RadiusAccountPrimaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 4, 3),
    _RadiusAccountPrimaryServerSecret_Type()
)
radiusAccountPrimaryServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountPrimaryServerSecret.setStatus("current")
_RadiusAccountSecondaryServer_ObjectIdentity = ObjectIdentity
radiusAccountSecondaryServer = _RadiusAccountSecondaryServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 5)
)
_RadiusAccountSecondaryServerIP_Type = IpAddress
_RadiusAccountSecondaryServerIP_Object = MibScalar
radiusAccountSecondaryServerIP = _RadiusAccountSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 5, 1),
    _RadiusAccountSecondaryServerIP_Type()
)
radiusAccountSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountSecondaryServerIP.setStatus("current")


class _RadiusAccountSecondaryServerPort_Type(Integer32):
    """Custom type radiusAccountSecondaryServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusAccountSecondaryServerPort_Type.__name__ = "Integer32"
_RadiusAccountSecondaryServerPort_Object = MibScalar
radiusAccountSecondaryServerPort = _RadiusAccountSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 5, 2),
    _RadiusAccountSecondaryServerPort_Type()
)
radiusAccountSecondaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountSecondaryServerPort.setStatus("current")


class _RadiusAccountSecondaryServerSecret_Type(DisplayString):
    """Custom type radiusAccountSecondaryServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RadiusAccountSecondaryServerSecret_Type.__name__ = "DisplayString"
_RadiusAccountSecondaryServerSecret_Object = MibScalar
radiusAccountSecondaryServerSecret = _RadiusAccountSecondaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 5, 5, 3),
    _RadiusAccountSecondaryServerSecret_Type()
)
radiusAccountSecondaryServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountSecondaryServerSecret.setStatus("current")
_HotspotSettings_ObjectIdentity = ObjectIdentity
hotspotSettings = _HotspotSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 6)
)
_HttpRedirectEnable_Type = TruthValue
_HttpRedirectEnable_Object = MibScalar
httpRedirectEnable = _HttpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 6, 1),
    _HttpRedirectEnable_Type()
)
httpRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRedirectEnable.setStatus("current")


class _HttpRedirectUrl_Type(DisplayString):
    """Custom type httpRedirectUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HttpRedirectUrl_Type.__name__ = "DisplayString"
_HttpRedirectUrl_Object = MibScalar
httpRedirectUrl = _HttpRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 6, 2),
    _HttpRedirectUrl_Type()
)
httpRedirectUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRedirectUrl.setStatus("current")
_SyslogSettings_ObjectIdentity = ObjectIdentity
syslogSettings = _SyslogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 7)
)
_SyslogEnable_Type = TruthValue
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 7, 1),
    _SyslogEnable_Type()
)
syslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnable.setStatus("current")
_SyslogServerIP_Type = IpAddress
_SyslogServerIP_Object = MibScalar
syslogServerIP = _SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 7, 2),
    _SyslogServerIP_Type()
)
syslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIP.setStatus("current")


class _SyslogServerPort_Type(Integer32):
    """Custom type syslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyslogServerPort_Type.__name__ = "Integer32"
_SyslogServerPort_Object = MibScalar
syslogServerPort = _SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 7, 3),
    _SyslogServerPort_Type()
)
syslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPort.setStatus("current")
_RemoteMgmtSettings_ObjectIdentity = ObjectIdentity
remoteMgmtSettings = _RemoteMgmtSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8)
)
_SnmpEnable_Type = TruthValue
_SnmpEnable_Object = MibScalar
snmpEnable = _SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 1),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")
_SnmpManageIP_Type = IpAddress
_SnmpManageIP_Object = MibScalar
snmpManageIP = _SnmpManageIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 2),
    _SnmpManageIP_Type()
)
snmpManageIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManageIP.setStatus("current")
_SnmpTrapServerIP_Type = IpAddress
_SnmpTrapServerIP_Object = MibScalar
snmpTrapServerIP = _SnmpTrapServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 3),
    _SnmpTrapServerIP_Type()
)
snmpTrapServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerIP.setStatus("current")


class _SnmpReadCommunity_Type(DisplayString):
    """Custom type snmpReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpReadCommunity_Type.__name__ = "DisplayString"
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 4),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")


class _SnmpWriteCommunity_Type(DisplayString):
    """Custom type snmpWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpWriteCommunity_Type.__name__ = "DisplayString"
_SnmpWriteCommunity_Object = MibScalar
snmpWriteCommunity = _SnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 5),
    _SnmpWriteCommunity_Type()
)
snmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunity.setStatus("current")


class _SnmpTrapPort_Type(Integer32):
    """Custom type snmpTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpTrapPort_Type.__name__ = "Integer32"
_SnmpTrapPort_Object = MibScalar
snmpTrapPort = _SnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 6),
    _SnmpTrapPort_Type()
)
snmpTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapPort.setStatus("current")
_MgmtWebAccessCtrl_Type = TruthValue
_MgmtWebAccessCtrl_Object = MibScalar
mgmtWebAccessCtrl = _MgmtWebAccessCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 8),
    _MgmtWebAccessCtrl_Type()
)
mgmtWebAccessCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebAccessCtrl.setStatus("current")


class _MgmtWebIPSubnet1_Type(DisplayString):
    """Custom type mgmtWebIPSubnet1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet1_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet1_Object = MibScalar
mgmtWebIPSubnet1 = _MgmtWebIPSubnet1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 9),
    _MgmtWebIPSubnet1_Type()
)
mgmtWebIPSubnet1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet1.setStatus("current")


class _MgmtWebIPSubnet2_Type(DisplayString):
    """Custom type mgmtWebIPSubnet2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet2_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet2_Object = MibScalar
mgmtWebIPSubnet2 = _MgmtWebIPSubnet2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 10),
    _MgmtWebIPSubnet2_Type()
)
mgmtWebIPSubnet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet2.setStatus("current")


class _MgmtWebIPSubnet3_Type(DisplayString):
    """Custom type mgmtWebIPSubnet3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet3_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet3_Object = MibScalar
mgmtWebIPSubnet3 = _MgmtWebIPSubnet3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 11),
    _MgmtWebIPSubnet3_Type()
)
mgmtWebIPSubnet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet3.setStatus("current")


class _MgmtWebIPSubnet4_Type(DisplayString):
    """Custom type mgmtWebIPSubnet4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet4_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet4_Object = MibScalar
mgmtWebIPSubnet4 = _MgmtWebIPSubnet4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 12),
    _MgmtWebIPSubnet4_Type()
)
mgmtWebIPSubnet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet4.setStatus("current")


class _MgmtWebIPSubnet5_Type(DisplayString):
    """Custom type mgmtWebIPSubnet5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet5_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet5_Object = MibScalar
mgmtWebIPSubnet5 = _MgmtWebIPSubnet5_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 13),
    _MgmtWebIPSubnet5_Type()
)
mgmtWebIPSubnet5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet5.setStatus("current")


class _MgmtWebIPSubnet6_Type(DisplayString):
    """Custom type mgmtWebIPSubnet6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet6_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet6_Object = MibScalar
mgmtWebIPSubnet6 = _MgmtWebIPSubnet6_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 14),
    _MgmtWebIPSubnet6_Type()
)
mgmtWebIPSubnet6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet6.setStatus("current")


class _MgmtWebIPSubnet7_Type(DisplayString):
    """Custom type mgmtWebIPSubnet7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet7_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet7_Object = MibScalar
mgmtWebIPSubnet7 = _MgmtWebIPSubnet7_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 15),
    _MgmtWebIPSubnet7_Type()
)
mgmtWebIPSubnet7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet7.setStatus("current")


class _MgmtWebIPSubnet8_Type(DisplayString):
    """Custom type mgmtWebIPSubnet8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 31),
    )


_MgmtWebIPSubnet8_Type.__name__ = "DisplayString"
_MgmtWebIPSubnet8_Object = MibScalar
mgmtWebIPSubnet8 = _MgmtWebIPSubnet8_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 8, 16),
    _MgmtWebIPSubnet8_Type()
)
mgmtWebIPSubnet8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtWebIPSubnet8.setStatus("current")
_AuxCommand_ObjectIdentity = ObjectIdentity
auxCommand = _AuxCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 9)
)
_ResetAP_Type = TruthValue
_ResetAP_Object = MibScalar
resetAP = _ResetAP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 9, 1),
    _ResetAP_Type()
)
resetAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAP.setStatus("current")
_ResetToFactoryDefault_Type = TruthValue
_ResetToFactoryDefault_Object = MibScalar
resetToFactoryDefault = _ResetToFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 9, 2),
    _ResetToFactoryDefault_Type()
)
resetToFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetToFactoryDefault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WG102",
    **{"netgear": netgear,
       "wireless": wireless,
       "wg102": wg102,
       "sysSettings": sysSettings,
       "sysMacAddress": sysMacAddress,
       "sysVersion": sysVersion,
       "sysAPName": sysAPName,
       "sysAdminName": sysAdminName,
       "sysAdminPasswd": sysAdminPasswd,
       "sysCountryRegion": sysCountryRegion,
       "timeSettings": timeSettings,
       "timeCurrentTime": timeCurrentTime,
       "timeTimeZone": timeTimeZone,
       "timeDaylightSaving": timeDaylightSaving,
       "timeNtpServer": timeNtpServer,
       "ipSettings": ipSettings,
       "ipDhcpClientEnable": ipDhcpClientEnable,
       "ipIPAddress": ipIPAddress,
       "ipNetmask": ipNetmask,
       "ipGateway": ipGateway,
       "ipDnsServer": ipDnsServer,
       "wlanSettings": wlanSettings,
       "wlanSettingTable": wlanSettingTable,
       "wlanSettingEntry": wlanSettingEntry,
       "radioIndex": radioIndex,
       "radioEnable": radioEnable,
       "wirelessMode": wirelessMode,
       "channel": channel,
       "txRate": txRate,
       "txPower": txPower,
       "beaconInterval": beaconInterval,
       "dtimInterval": dtimInterval,
       "rtsThreshold": rtsThreshold,
       "fragmentationThreshold": fragmentationThreshold,
       "dot11bPreamble": dot11bPreamble,
       "superMode": superMode,
       "wmm": wmm,
       "wmmNoAck": wmmNoAck,
       "acEnabled": acEnabled,
       "acEnhancedRFSecurity": acEnhancedRFSecurity,
       "acRogueDevDetection": acRogueDevDetection,
       "accessControlMode": accessControlMode,
       "wlanSecurityTable": wlanSecurityTable,
       "wlanSecurityEntry": wlanSecurityEntry,
       "securityProfileNo": securityProfileNo,
       "securityProfileEnabled": securityProfileEnabled,
       "securityProfileName": securityProfileName,
       "ssid": ssid,
       "ssidBroadcastEnable": ssidBroadcastEnable,
       "authentication": authentication,
       "encryption": encryption,
       "wepKey1": wepKey1,
       "wepKey2": wepKey2,
       "wepKey3": wepKey3,
       "wepKey4": wepKey4,
       "wepKeyDefault": wepKeyDefault,
       "wpaPSK": wpaPSK,
       "wlanSeparatorEnable": wlanSeparatorEnable,
       "wlanMaxUser": wlanMaxUser,
       "wlanAccessControlLocalTable": wlanAccessControlLocalTable,
       "wlanAccessControlLocalEntry": wlanAccessControlLocalEntry,
       "aclIndex": aclIndex,
       "aclMAC": aclMAC,
       "wlanWdsTable": wlanWdsTable,
       "wlanWdsEntry": wlanWdsEntry,
       "operationMode": operationMode,
       "localMacAddress": localMacAddress,
       "ptpRemoteMacAddress": ptpRemoteMacAddress,
       "pxpRemoteMacAddress1": pxpRemoteMacAddress1,
       "pxpRemoteMacAddress2": pxpRemoteMacAddress2,
       "pxpRemoteMacAddress3": pxpRemoteMacAddress3,
       "pxpRemoteMacAddress4": pxpRemoteMacAddress4,
       "repeaterParentMacAddress": repeaterParentMacAddress,
       "repeaterChildMacAddress": repeaterChildMacAddress,
       "wlanClientsTable": wlanClientsTable,
       "wlanClientsEntry": wlanClientsEntry,
       "clientIndex": clientIndex,
       "clientMacAddress": clientMacAddress,
       "clientIP": clientIP,
       "clientSSID": clientSSID,
       "clientStatus": clientStatus,
       "wlanUnknownApTable": wlanUnknownApTable,
       "wlanUnknownApEntry": wlanUnknownApEntry,
       "unknowApIndex": unknowApIndex,
       "unknowApAuthorize": unknowApAuthorize,
       "unknowApSSID": unknowApSSID,
       "unknowApMacAddress": unknowApMacAddress,
       "unknowApChannel": unknowApChannel,
       "unknowApAutoCellEnabled": unknowApAutoCellEnabled,
       "wlanAuthorizedApTable": wlanAuthorizedApTable,
       "wlanAuthorizedApEntry": wlanAuthorizedApEntry,
       "authorizedApIndex": authorizedApIndex,
       "authorizedApDelete": authorizedApDelete,
       "authorizedApSSID": authorizedApSSID,
       "authorizedApMacAddress": authorizedApMacAddress,
       "authorizedApChannel": authorizedApChannel,
       "authorizedApAutoCellEnabled": authorizedApAutoCellEnabled,
       "wlanUnknownStationTable": wlanUnknownStationTable,
       "wlanUnknownStationEntry": wlanUnknownStationEntry,
       "unknowStationIndex": unknowStationIndex,
       "unknowStationAuthorize": unknowStationAuthorize,
       "unknowStationMacAddress": unknowStationMacAddress,
       "unknowStationChannel": unknowStationChannel,
       "unknowStationAutoCellEnabled": unknowStationAutoCellEnabled,
       "wlanAuthorizedStationTable": wlanAuthorizedStationTable,
       "wlanAuthorizedStationEntry": wlanAuthorizedStationEntry,
       "authorizedStationIndex": authorizedStationIndex,
       "authorizedStationDelete": authorizedStationDelete,
       "authorizedStationMacAddress": authorizedStationMacAddress,
       "authorizedStationChannel": authorizedStationChannel,
       "authorizedStationAutoCellEnabled": authorizedStationAutoCellEnabled,
       "vlanSettings": vlanSettings,
       "vlanEnable": vlanEnable,
       "managementVlanId": managementVlanId,
       "securityProfileVlanTable": securityProfileVlanTable,
       "securityProfileVlanEntry": securityProfileVlanEntry,
       "profileNo": profileNo,
       "profileVlan": profileVlan,
       "sysStatistics": sysStatistics,
       "ethernetStat": ethernetStat,
       "ethInPackets": ethInPackets,
       "ethOutPackets": ethOutPackets,
       "ethInBytes": ethInBytes,
       "ethOutBytes": ethOutBytes,
       "wirelessStatTable": wirelessStatTable,
       "wirelessStatEntry": wirelessStatEntry,
       "wlanSecurityProfileNo": wlanSecurityProfileNo,
       "wlanInPacketsUnicast": wlanInPacketsUnicast,
       "wlanOutPacketsUnicast": wlanOutPacketsUnicast,
       "wlanInPacketsBroadcast": wlanInPacketsBroadcast,
       "wlanOutPacketsBroadcast": wlanOutPacketsBroadcast,
       "wlanInPacketsMulticast": wlanInPacketsMulticast,
       "wlanOutPacketsMulticast": wlanOutPacketsMulticast,
       "wlanInPacketsTotal": wlanInPacketsTotal,
       "wlanOutPacketsTotal": wlanOutPacketsTotal,
       "wlanInBytesTotal": wlanInBytesTotal,
       "wlanOutBytesTotal": wlanOutBytesTotal,
       "ethWrongPackets": ethWrongPackets,
       "wrongWLANSTAPackets": wrongWLANSTAPackets,
       "wlanStationCount": wlanStationCount,
       "wirelessLinkStatTable": wirelessLinkStatTable,
       "wirelessLinkStatEntry": wirelessLinkStatEntry,
       "wirelessLinkStatIndex": wirelessLinkStatIndex,
       "wirelessLinkStatDate": wirelessLinkStatDate,
       "wirelessLinkStatTime": wirelessLinkStatTime,
       "wirelessLinkStatRequest": wirelessLinkStatRequest,
       "wirelessLinkStatResponse": wirelessLinkStatResponse,
       "wirelessLinkStatGrant": wirelessLinkStatGrant,
       "wirelessLinkStatDisconnect": wirelessLinkStatDisconnect,
       "wirelessLinkStatDisconnectAll": wirelessLinkStatDisconnectAll,
       "wirelessLinkStatFlag": wirelessLinkStatFlag,
       "wlanAuthenticatedStationCount": wlanAuthenticatedStationCount,
       "sysTotalMemory": sysTotalMemory,
       "sysFreeMemory": sysFreeMemory,
       "sysRuntime": sysRuntime,
       "radiusSettings": radiusSettings,
       "radiusAuthPrimaryServer": radiusAuthPrimaryServer,
       "radiusAuthPrimaryServerIP": radiusAuthPrimaryServerIP,
       "radiusAuthPrimaryServerPort": radiusAuthPrimaryServerPort,
       "radiusAuthPrimaryServerSecret": radiusAuthPrimaryServerSecret,
       "radiusAuthSecondaryServer": radiusAuthSecondaryServer,
       "radiusAuthSecondaryServerIP": radiusAuthSecondaryServerIP,
       "radiusAuthSecondaryServerPort": radiusAuthSecondaryServerPort,
       "radiusAuthSecondaryServerSecret": radiusAuthSecondaryServerSecret,
       "authenticationSettings": authenticationSettings,
       "reauthTime": reauthTime,
       "wpaGroupKeyUpdateCondition": wpaGroupKeyUpdateCondition,
       "wpaGroupKeyUpdateIntervalSecond": wpaGroupKeyUpdateIntervalSecond,
       "radiusAccountPrimaryServer": radiusAccountPrimaryServer,
       "radiusAccountPrimaryServerIP": radiusAccountPrimaryServerIP,
       "radiusAccountPrimaryServerPort": radiusAccountPrimaryServerPort,
       "radiusAccountPrimaryServerSecret": radiusAccountPrimaryServerSecret,
       "radiusAccountSecondaryServer": radiusAccountSecondaryServer,
       "radiusAccountSecondaryServerIP": radiusAccountSecondaryServerIP,
       "radiusAccountSecondaryServerPort": radiusAccountSecondaryServerPort,
       "radiusAccountSecondaryServerSecret": radiusAccountSecondaryServerSecret,
       "hotspotSettings": hotspotSettings,
       "httpRedirectEnable": httpRedirectEnable,
       "httpRedirectUrl": httpRedirectUrl,
       "syslogSettings": syslogSettings,
       "syslogEnable": syslogEnable,
       "syslogServerIP": syslogServerIP,
       "syslogServerPort": syslogServerPort,
       "remoteMgmtSettings": remoteMgmtSettings,
       "snmpEnable": snmpEnable,
       "snmpManageIP": snmpManageIP,
       "snmpTrapServerIP": snmpTrapServerIP,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpWriteCommunity": snmpWriteCommunity,
       "snmpTrapPort": snmpTrapPort,
       "mgmtWebAccessCtrl": mgmtWebAccessCtrl,
       "mgmtWebIPSubnet1": mgmtWebIPSubnet1,
       "mgmtWebIPSubnet2": mgmtWebIPSubnet2,
       "mgmtWebIPSubnet3": mgmtWebIPSubnet3,
       "mgmtWebIPSubnet4": mgmtWebIPSubnet4,
       "mgmtWebIPSubnet5": mgmtWebIPSubnet5,
       "mgmtWebIPSubnet6": mgmtWebIPSubnet6,
       "mgmtWebIPSubnet7": mgmtWebIPSubnet7,
       "mgmtWebIPSubnet8": mgmtWebIPSubnet8,
       "auxCommand": auxCommand,
       "resetAP": resetAP,
       "resetToFactoryDefault": resetToFactoryDefault}
)
