# SNMP MIB module (WAG302) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WAG302
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:26 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wag302 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7)
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
_LanSettings_ObjectIdentity = ObjectIdentity
lanSettings = _LanSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1)
)


class _ApName_Type(DisplayString):
    """Custom type apName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApName_Type.__name__ = "DisplayString"
_ApName_Object = MibScalar
apName = _ApName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 1),
    _ApName_Type()
)
apName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apName.setStatus("current")
_SysMacAddress_Type = MacAddress
_SysMacAddress_Object = MibScalar
sysMacAddress = _SysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 2),
    _SysMacAddress_Type()
)
sysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAddress.setStatus("current")
_SysVersion_Type = DisplayString
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 3),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")


class _SysCountryRegion_Type(Integer32):
    """Custom type sysCountryRegion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              12,
              31,
              32,
              36,
              40,
              48,
              51,
              56,
              68,
              76,
              84,
              96,
              100,
              112,
              124,
              152,
              156,
              158,
              170,
              188,
              191,
              196,
              203,
              208,
              214,
              218,
              222,
              233,
              246,
              250,
              268,
              276,
              300,
              320,
              340,
              344,
              348,
              352,
              356,
              360,
              364,
              372,
              376,
              380,
              392,
              398,
              400,
              408,
              410,
              414,
              422,
              428,
              438,
              440,
              442,
              446,
              458,
              470,
              484,
              492,
              504,
              512,
              528,
              554,
              578,
              586,
              591,
              604,
              608,
              616,
              620,
              630,
              634,
              642,
              643,
              682,
              702,
              703,
              704,
              705,
              710,
              716,
              724,
              752,
              756,
              760,
              764,
              780,
              784,
              788,
              792,
              804,
              807,
              818,
              826,
              840,
              858,
              860,
              862,
              887)
        )
    )
    namedValues = NamedValues(
        *(("albania", 8),
          ("algeria", 12),
          ("argentina", 32),
          ("armenia", 51),
          ("australia", 36),
          ("austria", 40),
          ("azerbaijan", 31),
          ("bahrain", 48),
          ("belarus", 112),
          ("belgium", 56),
          ("belize", 84),
          ("bolivia", 68),
          ("brazil", 76),
          ("brunei", 96),
          ("bulgaria", 100),
          ("canada", 124),
          ("chile", 152),
          ("china", 156),
          ("colombia", 170),
          ("costaRica", 188),
          ("croatia", 191),
          ("cyprus", 196),
          ("czechRepublic", 203),
          ("denmark", 208),
          ("dominicanRepublic", 214),
          ("ecuador", 218),
          ("egypt", 818),
          ("elSalvador", 222),
          ("estonia", 233),
          ("finland", 246),
          ("france", 250),
          ("georgia", 268),
          ("germany", 276),
          ("greece", 300),
          ("guatemala", 320),
          ("honduras", 340),
          ("hongkong", 344),
          ("hungary", 348),
          ("iceland", 352),
          ("india", 356),
          ("indonesia", 360),
          ("iran", 364),
          ("ireland", 372),
          ("israel", 376),
          ("italy", 380),
          ("japan", 392),
          ("jordan", 400),
          ("kazakhstan", 398),
          ("koreaRepublic", 410),
          ("kuwait", 414),
          ("latvia", 428),
          ("lebanon", 422),
          ("liechtenstein", 438),
          ("lithuania", 440),
          ("luxembourg", 442),
          ("macau", 446),
          ("macedonia", 807),
          ("malaysia", 458),
          ("malta", 470),
          ("marocco", 504),
          ("mexico", 484),
          ("monaco", 492),
          ("netherlands", 528),
          ("newZealand", 554),
          ("northKorea", 408),
          ("norway", 578),
          ("oman", 512),
          ("pakistan", 586),
          ("panama", 591),
          ("peru", 604),
          ("philippines", 608),
          ("poland", 616),
          ("portugal", 620),
          ("puertoRico", 630),
          ("qatar", 634),
          ("romania", 642),
          ("russia", 643),
          ("saudiArabia", 682),
          ("singapore", 702),
          ("slovakRepublic", 703),
          ("slovenia", 705),
          ("southAfrica", 710),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("syria", 760),
          ("taiwan", 158),
          ("thailand", 764),
          ("trinidadandTobago", 780),
          ("tunisia", 788),
          ("turkey", 792),
          ("ukraine", 804),
          ("unitedArabEmirates", 784),
          ("unitedKingdom", 826),
          ("unitedStates", 840),
          ("uruguay", 858),
          ("uzbekistan", 860),
          ("venezuela", 862),
          ("vietnam", 704),
          ("yemen", 887),
          ("zimbabwe", 716))
    )


_SysCountryRegion_Type.__name__ = "Integer32"
_SysCountryRegion_Object = MibScalar
sysCountryRegion = _SysCountryRegion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 4),
    _SysCountryRegion_Type()
)
sysCountryRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCountryRegion.setStatus("current")


class _AdminName_Type(DisplayString):
    """Custom type adminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminName_Type.__name__ = "DisplayString"
_AdminName_Object = MibScalar
adminName = _AdminName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 5),
    _AdminName_Type()
)
adminName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminName.setStatus("obsolete")


class _AdminPasswd_Type(DisplayString):
    """Custom type adminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminPasswd_Type.__name__ = "DisplayString"
_AdminPasswd_Object = MibScalar
adminPasswd = _AdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 6),
    _AdminPasswd_Type()
)
adminPasswd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminPasswd.setStatus("obsolete")


class _DhcpStatus_Type(Integer32):
    """Custom type dhcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcpclient", 1),
          ("static", 0))
    )


_DhcpStatus_Type.__name__ = "Integer32"
_DhcpStatus_Object = MibScalar
dhcpStatus = _DhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 7),
    _DhcpStatus_Type()
)
dhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStatus.setStatus("current")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 8),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_NetmaskAddr_Type = IpAddress
_NetmaskAddr_Object = MibScalar
netmaskAddr = _NetmaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 9),
    _NetmaskAddr_Type()
)
netmaskAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netmaskAddr.setStatus("current")
_GatewayAddr_Type = IpAddress
_GatewayAddr_Object = MibScalar
gatewayAddr = _GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 10),
    _GatewayAddr_Type()
)
gatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayAddr.setStatus("current")
_PridnsipAddr_Type = IpAddress
_PridnsipAddr_Object = MibScalar
pridnsipAddr = _PridnsipAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 11),
    _PridnsipAddr_Type()
)
pridnsipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pridnsipAddr.setStatus("current")
_SnddnsipAddr_Type = IpAddress
_SnddnsipAddr_Object = MibScalar
snddnsipAddr = _SnddnsipAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 12),
    _SnddnsipAddr_Type()
)
snddnsipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snddnsipAddr.setStatus("current")
_Spantree_Type = TruthValue
_Spantree_Object = MibScalar
spantree = _Spantree_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 13),
    _Spantree_Type()
)
spantree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spantree.setStatus("current")
_VlanEnable_Type = TruthValue
_VlanEnable_Object = MibScalar
vlanEnable = _VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 14),
    _VlanEnable_Type()
)
vlanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanEnable.setStatus("current")


class _ManagementVlanID_Type(Integer32):
    """Custom type managementVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ManagementVlanID_Type.__name__ = "Integer32"
_ManagementVlanID_Object = MibScalar
managementVlanID = _ManagementVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 15),
    _ManagementVlanID_Type()
)
managementVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementVlanID.setStatus("current")


class _UntaggedVlanID_Type(Integer32):
    """Custom type untaggedVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_UntaggedVlanID_Type.__name__ = "Integer32"
_UntaggedVlanID_Object = MibScalar
untaggedVlanID = _UntaggedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 1, 16),
    _UntaggedVlanID_Type()
)
untaggedVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    untaggedVlanID.setStatus("current")
_WlanSettingTable_Object = MibTable
wlanSettingTable = _WlanSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2)
)
if mibBuilder.loadTexts:
    wlanSettingTable.setStatus("current")
_WlanSettingEntry_Object = MibTableRow
wlanSettingEntry = _WlanSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1)
)
wlanSettingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanSettingEntry.setStatus("current")


class _Operatemode_Type(Integer32):
    """Custom type operatemode based on Integer32"""
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


_Operatemode_Type.__name__ = "Integer32"
_Operatemode_Object = MibTableColumn
operatemode = _Operatemode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 1),
    _Operatemode_Type()
)
operatemode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatemode.setStatus("current")
_RadioEnable_Type = TruthValue
_RadioEnable_Object = MibTableColumn
radioEnable = _RadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 2),
    _RadioEnable_Type()
)
radioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioEnable.setStatus("current")


class _Channel_Type(Integer32):
    """Custom type channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_Channel_Type.__name__ = "Integer32"
_Channel_Object = MibTableColumn
channel = _Channel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 3),
    _Channel_Type()
)
channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channel.setStatus("current")


class _Datarate_Type(Integer32):
    """Custom type datarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1000,
              2000,
              5500,
              6000,
              9000,
              11000,
              12000,
              18000,
              24000,
              36000,
              48000,
              54000)
        )
    )
    namedValues = NamedValues(
        *(("best", 0),
          ("rate11Mbps", 11000),
          ("rate12Mbps", 12000),
          ("rate18Mbps", 18000),
          ("rate1Mbps", 1000),
          ("rate24Mbps", 24000),
          ("rate2Mbps", 2000),
          ("rate36Mbps", 36000),
          ("rate48Mbps", 48000),
          ("rate54Mbps", 54000),
          ("rate5dot5Mbps", 5500),
          ("rate6Mbps", 6000),
          ("rate9Mbps", 9000))
    )


_Datarate_Type.__name__ = "Integer32"
_Datarate_Object = MibTableColumn
datarate = _Datarate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 4),
    _Datarate_Type()
)
datarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datarate.setStatus("current")
_WmmSupport_Type = TruthValue
_WmmSupport_Object = MibTableColumn
wmmSupport = _WmmSupport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 5),
    _WmmSupport_Type()
)
wmmSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmmSupport.setStatus("current")


class _Beaconinterval_Type(Integer32):
    """Custom type beaconinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_Beaconinterval_Type.__name__ = "Integer32"
_Beaconinterval_Object = MibTableColumn
beaconinterval = _Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 6),
    _Beaconinterval_Type()
)
beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconinterval.setStatus("current")
if mibBuilder.loadTexts:
    beaconinterval.setUnits("1024 microsecond")


class _Rtsthreshold_Type(Integer32):
    """Custom type rtsthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2346),
    )


_Rtsthreshold_Type.__name__ = "Integer32"
_Rtsthreshold_Object = MibTableColumn
rtsthreshold = _Rtsthreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 7),
    _Rtsthreshold_Type()
)
rtsthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsthreshold.setStatus("current")


class _Fraglength_Type(Integer32):
    """Custom type fraglength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_Fraglength_Type.__name__ = "Integer32"
_Fraglength_Object = MibTableColumn
fraglength = _Fraglength_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 8),
    _Fraglength_Type()
)
fraglength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fraglength.setStatus("current")


class _Dtiminterval_Type(Integer32):
    """Custom type dtiminterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dtiminterval_Type.__name__ = "Integer32"
_Dtiminterval_Object = MibTableColumn
dtiminterval = _Dtiminterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 9),
    _Dtiminterval_Type()
)
dtiminterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtiminterval.setStatus("current")


class _Preambletype_Type(Integer32):
    """Custom type preambletype based on Integer32"""
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


_Preambletype_Type.__name__ = "Integer32"
_Preambletype_Object = MibTableColumn
preambletype = _Preambletype_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 10),
    _Preambletype_Type()
)
preambletype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preambletype.setStatus("current")


class _Txpower_Type(Integer32):
    """Custom type txpower based on Integer32"""
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


_Txpower_Type.__name__ = "Integer32"
_Txpower_Object = MibTableColumn
txpower = _Txpower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 11),
    _Txpower_Type()
)
txpower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txpower.setStatus("current")
_SuperG_Type = TruthValue
_SuperG_Object = MibTableColumn
superG = _SuperG_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 12),
    _SuperG_Type()
)
superG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superG.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 13),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("current")


class _Antenna_Type(Integer32):
    """Custom type antenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_Antenna_Type.__name__ = "Integer32"
_Antenna_Object = MibTableColumn
antenna = _Antenna_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 2, 1, 14),
    _Antenna_Type()
)
antenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antenna.setStatus("obsolete")
_VapSetting_ObjectIdentity = ObjectIdentity
vapSetting = _VapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3)
)
_VapWepAndGlobalSettingTable_Object = MibTable
vapWepAndGlobalSettingTable = _VapWepAndGlobalSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1)
)
if mibBuilder.loadTexts:
    vapWepAndGlobalSettingTable.setStatus("current")
_VapWepAndGlobalSettingEntry_Object = MibTableRow
vapWepAndGlobalSettingEntry = _VapWepAndGlobalSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1)
)
vapWepAndGlobalSettingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WAG302", "vapIndex"),
)
if mibBuilder.loadTexts:
    vapWepAndGlobalSettingEntry.setStatus("current")


class _WepKeyType_Type(Integer32):
    """Custom type wepKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(40,
              104,
              128)
        )
    )
    namedValues = NamedValues(
        *(("hex128", 104),
          ("hex152", 128),
          ("hex64", 40))
    )


_WepKeyType_Type.__name__ = "Integer32"
_WepKeyType_Object = MibTableColumn
wepKeyType = _WepKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1, 1),
    _WepKeyType_Type()
)
wepKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKeyType.setStatus("current")


class _Key1_Type(DisplayString):
    """Custom type key1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Key1_Type.__name__ = "DisplayString"
_Key1_Object = MibTableColumn
key1 = _Key1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1, 2),
    _Key1_Type()
)
key1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key1.setStatus("current")


class _Key2_Type(DisplayString):
    """Custom type key2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Key2_Type.__name__ = "DisplayString"
_Key2_Object = MibTableColumn
key2 = _Key2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1, 3),
    _Key2_Type()
)
key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key2.setStatus("current")


class _Key3_Type(DisplayString):
    """Custom type key3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Key3_Type.__name__ = "DisplayString"
_Key3_Object = MibTableColumn
key3 = _Key3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1, 4),
    _Key3_Type()
)
key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key3.setStatus("current")


class _Key4_Type(DisplayString):
    """Custom type key4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Key4_Type.__name__ = "DisplayString"
_Key4_Object = MibTableColumn
key4 = _Key4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1, 5),
    _Key4_Type()
)
key4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key4.setStatus("current")


class _WepPassPhrase_Type(DisplayString):
    """Custom type wepPassPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_WepPassPhrase_Type.__name__ = "DisplayString"
_WepPassPhrase_Object = MibTableColumn
wepPassPhrase = _WepPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 1, 1, 6),
    _WepPassPhrase_Type()
)
wepPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepPassPhrase.setStatus("current")
_VapSettingTable_Object = MibTable
vapSettingTable = _VapSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2)
)
if mibBuilder.loadTexts:
    vapSettingTable.setStatus("current")
_VapSettingEntry_Object = MibTableRow
vapSettingEntry = _VapSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1)
)
vapSettingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WAG302", "vapIndex"),
)
if mibBuilder.loadTexts:
    vapSettingEntry.setStatus("current")


class _VapIndex_Type(Integer32):
    """Custom type vapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VapIndex_Type.__name__ = "Integer32"
_VapIndex_Object = MibTableColumn
vapIndex = _VapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 1),
    _VapIndex_Type()
)
vapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapIndex.setStatus("current")
_VapEnable_Type = TruthValue
_VapEnable_Object = MibTableColumn
vapEnable = _VapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 2),
    _VapEnable_Type()
)
vapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapEnable.setStatus("current")


class _Ssid_Type(DisplayString):
    """Custom type ssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ssid_Type.__name__ = "DisplayString"
_Ssid_Object = MibTableColumn
ssid = _Ssid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 3),
    _Ssid_Type()
)
ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssid.setStatus("current")
_Hidenetworkname_Type = TruthValue
_Hidenetworkname_Object = MibTableColumn
hidenetworkname = _Hidenetworkname_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 4),
    _Hidenetworkname_Type()
)
hidenetworkname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hidenetworkname.setStatus("current")


class _VlanID_Type(Integer32):
    """Custom type vlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanID_Type.__name__ = "Integer32"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 5),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")


class _SecurityProfileName_Type(DisplayString):
    """Custom type securityProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SecurityProfileName_Type.__name__ = "DisplayString"
_SecurityProfileName_Object = MibTableColumn
securityProfileName = _SecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 6),
    _SecurityProfileName_Type()
)
securityProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfileName.setStatus("current")


class _Presharekey_Type(DisplayString):
    """Custom type presharekey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Presharekey_Type.__name__ = "DisplayString"
_Presharekey_Object = MibTableColumn
presharekey = _Presharekey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 7),
    _Presharekey_Type()
)
presharekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presharekey.setStatus("current")


class _Authenticationtype_Type(Integer32):
    """Custom type authenticationtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              12,
              16,
              32,
              48)
        )
    )
    namedValues = NamedValues(
        *(("legacy802dot1x", 2),
          ("open", 0),
          ("shared", 1),
          ("wpa", 4),
          ("wpa2", 8),
          ("wpa2psk", 32),
          ("wpaORwpa2", 12),
          ("wpapsk", 16),
          ("wpapskORwpa2psk", 48))
    )


_Authenticationtype_Type.__name__ = "Integer32"
_Authenticationtype_Object = MibTableColumn
authenticationtype = _Authenticationtype_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 8),
    _Authenticationtype_Type()
)
authenticationtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationtype.setStatus("current")


class _Encryption_Type(Integer32):
    """Custom type encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aes", 4),
          ("none", 0),
          ("tkip", 2),
          ("tkipORaes", 6),
          ("wep", 1))
    )


_Encryption_Type.__name__ = "Integer32"
_Encryption_Object = MibTableColumn
encryption = _Encryption_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 9),
    _Encryption_Type()
)
encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption.setStatus("current")


class _Keyno_Type(Integer32):
    """Custom type keyno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Keyno_Type.__name__ = "Integer32"
_Keyno_Object = MibTableColumn
keyno = _Keyno_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 10),
    _Keyno_Type()
)
keyno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyno.setStatus("current")
_Wlanseparator_Type = TruthValue
_Wlanseparator_Object = MibTableColumn
wlanseparator = _Wlanseparator_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 3, 2, 1, 11),
    _Wlanseparator_Type()
)
wlanseparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanseparator.setStatus("current")
_RemoteSettings_ObjectIdentity = ObjectIdentity
remoteSettings = _RemoteSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4)
)
_Sshd_Type = TruthValue
_Sshd_Object = MibScalar
sshd = _Sshd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4, 1),
    _Sshd_Type()
)
sshd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshd.setStatus("current")
_Snmpenable_Type = TruthValue
_Snmpenable_Object = MibScalar
snmpenable = _Snmpenable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4, 2),
    _Snmpenable_Type()
)
snmpenable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpenable.setStatus("current")
_TrapServerIP_Type = IpAddress
_TrapServerIP_Object = MibScalar
trapServerIP = _TrapServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4, 3),
    _TrapServerIP_Type()
)
trapServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerIP.setStatus("current")


class _TrapServerCommunity_Type(DisplayString):
    """Custom type trapServerCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TrapServerCommunity_Type.__name__ = "DisplayString"
_TrapServerCommunity_Object = MibScalar
trapServerCommunity = _TrapServerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4, 4),
    _TrapServerCommunity_Type()
)
trapServerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerCommunity.setStatus("current")


class _ReadOnlyCommunity_Type(DisplayString):
    """Custom type readOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ReadOnlyCommunity_Type.__name__ = "DisplayString"
_ReadOnlyCommunity_Object = MibScalar
readOnlyCommunity = _ReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4, 5),
    _ReadOnlyCommunity_Type()
)
readOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readOnlyCommunity.setStatus("current")


class _ReadWriteCommunity_Type(DisplayString):
    """Custom type readWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ReadWriteCommunity_Type.__name__ = "DisplayString"
_ReadWriteCommunity_Object = MibScalar
readWriteCommunity = _ReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 4, 6),
    _ReadWriteCommunity_Type()
)
readWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readWriteCommunity.setStatus("current")
_Statistic_ObjectIdentity = ObjectIdentity
statistic = _Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5)
)
_Wiredethernetstat_ObjectIdentity = ObjectIdentity
wiredethernetstat = _Wiredethernetstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 1)
)
_Lanrecvpacket_Type = Unsigned32
_Lanrecvpacket_Object = MibScalar
lanrecvpacket = _Lanrecvpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 1, 1),
    _Lanrecvpacket_Type()
)
lanrecvpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanrecvpacket.setStatus("current")
_Lantranspacket_Type = Unsigned32
_Lantranspacket_Object = MibScalar
lantranspacket = _Lantranspacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 1, 2),
    _Lantranspacket_Type()
)
lantranspacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lantranspacket.setStatus("current")
_Lanrecvbytes_Type = Unsigned32
_Lanrecvbytes_Object = MibScalar
lanrecvbytes = _Lanrecvbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 1, 3),
    _Lanrecvbytes_Type()
)
lanrecvbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanrecvbytes.setStatus("current")
_Lantransbytes_Type = Unsigned32
_Lantransbytes_Object = MibScalar
lantransbytes = _Lantransbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 1, 4),
    _Lantransbytes_Type()
)
lantransbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lantransbytes.setStatus("current")
_WirelessStatTable_Object = MibTable
wirelessStatTable = _WirelessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2)
)
if mibBuilder.loadTexts:
    wirelessStatTable.setStatus("current")
_WirelessStatEntry_Object = MibTableRow
wirelessStatEntry = _WirelessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1)
)
wirelessStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wirelessStatEntry.setStatus("current")
_Wlanrecvunicastpacket_Type = Unsigned32
_Wlanrecvunicastpacket_Object = MibTableColumn
wlanrecvunicastpacket = _Wlanrecvunicastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 1),
    _Wlanrecvunicastpacket_Type()
)
wlanrecvunicastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvunicastpacket.setStatus("current")
_Wlantransunicastpacket_Type = Unsigned32
_Wlantransunicastpacket_Object = MibTableColumn
wlantransunicastpacket = _Wlantransunicastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 2),
    _Wlantransunicastpacket_Type()
)
wlantransunicastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransunicastpacket.setStatus("current")
_Wlanrecvbroadcastpacket_Type = Unsigned32
_Wlanrecvbroadcastpacket_Object = MibTableColumn
wlanrecvbroadcastpacket = _Wlanrecvbroadcastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 3),
    _Wlanrecvbroadcastpacket_Type()
)
wlanrecvbroadcastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvbroadcastpacket.setStatus("current")
_Wlantransbroadcastpacket_Type = Unsigned32
_Wlantransbroadcastpacket_Object = MibTableColumn
wlantransbroadcastpacket = _Wlantransbroadcastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 4),
    _Wlantransbroadcastpacket_Type()
)
wlantransbroadcastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransbroadcastpacket.setStatus("current")
_Wlanrecvmulticastpacket_Type = Unsigned32
_Wlanrecvmulticastpacket_Object = MibTableColumn
wlanrecvmulticastpacket = _Wlanrecvmulticastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 5),
    _Wlanrecvmulticastpacket_Type()
)
wlanrecvmulticastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvmulticastpacket.setStatus("current")
_Wlantransmulticastpacket_Type = Unsigned32
_Wlantransmulticastpacket_Object = MibTableColumn
wlantransmulticastpacket = _Wlantransmulticastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 6),
    _Wlantransmulticastpacket_Type()
)
wlantransmulticastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransmulticastpacket.setStatus("current")
_Wlanrecvpacket_Type = Unsigned32
_Wlanrecvpacket_Object = MibTableColumn
wlanrecvpacket = _Wlanrecvpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 7),
    _Wlanrecvpacket_Type()
)
wlanrecvpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvpacket.setStatus("current")
_Wlantranspacket_Type = Unsigned32
_Wlantranspacket_Object = MibTableColumn
wlantranspacket = _Wlantranspacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 8),
    _Wlantranspacket_Type()
)
wlantranspacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantranspacket.setStatus("current")
_Wlanrecvbytes_Type = Unsigned32
_Wlanrecvbytes_Object = MibTableColumn
wlanrecvbytes = _Wlanrecvbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 9),
    _Wlanrecvbytes_Type()
)
wlanrecvbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvbytes.setStatus("current")
_Wlantransbytes_Type = Unsigned32
_Wlantransbytes_Object = MibTableColumn
wlantransbytes = _Wlantransbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 5, 2, 1, 10),
    _Wlantransbytes_Type()
)
wlantransbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransbytes.setStatus("current")
_StationListTable_Object = MibTable
stationListTable = _StationListTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 6)
)
if mibBuilder.loadTexts:
    stationListTable.setStatus("current")
_StationListEntry_Object = MibTableRow
stationListEntry = _StationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 6, 1)
)
stationListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "WAG302", "macaddress"),
)
if mibBuilder.loadTexts:
    stationListEntry.setStatus("current")
_Macaddress_Type = MacAddress
_Macaddress_Object = MibTableColumn
macaddress = _Macaddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 6, 1, 1),
    _Macaddress_Type()
)
macaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macaddress.setStatus("current")
_ClientIpaddr_Type = IpAddress
_ClientIpaddr_Object = MibTableColumn
clientIpaddr = _ClientIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 6, 1, 2),
    _ClientIpaddr_Type()
)
clientIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIpaddr.setStatus("current")


class _ClientWirelessMode_Type(Integer32):
    """Custom type clientWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_ClientWirelessMode_Type.__name__ = "Integer32"
_ClientWirelessMode_Object = MibTableColumn
clientWirelessMode = _ClientWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 6, 1, 3),
    _ClientWirelessMode_Type()
)
clientWirelessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientWirelessMode.setStatus("current")


class _Stationstatus_Type(Integer32):
    """Custom type stationstatus based on Integer32"""
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
          ("none", 0))
    )


_Stationstatus_Type.__name__ = "Integer32"
_Stationstatus_Object = MibTableColumn
stationstatus = _Stationstatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 6, 1, 4),
    _Stationstatus_Type()
)
stationstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationstatus.setStatus("current")
_WlanWdsTable_Object = MibTable
wlanWdsTable = _WlanWdsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7)
)
if mibBuilder.loadTexts:
    wlanWdsTable.setStatus("current")
_WlanWdsEntry_Object = MibTableRow
wlanWdsEntry = _WlanWdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1)
)
wlanWdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlanWdsEntry.setStatus("current")


class _Apmode_Type(Integer32):
    """Custom type apmode based on Integer32"""
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
          ("ptp-ap", 3),
          ("pxp", 4),
          ("pxp-ap", 5),
          ("repeater", 6))
    )


_Apmode_Type.__name__ = "Integer32"
_Apmode_Object = MibTableColumn
apmode = _Apmode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 1),
    _Apmode_Type()
)
apmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmode.setStatus("current")
_Ptpremotemacaddress_Type = MacAddress
_Ptpremotemacaddress_Object = MibTableColumn
ptpremotemacaddress = _Ptpremotemacaddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 2),
    _Ptpremotemacaddress_Type()
)
ptpremotemacaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpremotemacaddress.setStatus("current")
_Pxpremotemacaddress1_Type = MacAddress
_Pxpremotemacaddress1_Object = MibTableColumn
pxpremotemacaddress1 = _Pxpremotemacaddress1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 3),
    _Pxpremotemacaddress1_Type()
)
pxpremotemacaddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress1.setStatus("current")
_Pxpremotemacaddress2_Type = MacAddress
_Pxpremotemacaddress2_Object = MibTableColumn
pxpremotemacaddress2 = _Pxpremotemacaddress2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 4),
    _Pxpremotemacaddress2_Type()
)
pxpremotemacaddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress2.setStatus("current")
_Pxpremotemacaddress3_Type = MacAddress
_Pxpremotemacaddress3_Object = MibTableColumn
pxpremotemacaddress3 = _Pxpremotemacaddress3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 5),
    _Pxpremotemacaddress3_Type()
)
pxpremotemacaddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress3.setStatus("current")
_Pxpremotemacaddress4_Type = MacAddress
_Pxpremotemacaddress4_Object = MibTableColumn
pxpremotemacaddress4 = _Pxpremotemacaddress4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 6),
    _Pxpremotemacaddress4_Type()
)
pxpremotemacaddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress4.setStatus("current")
_Repremotemacaddress1_Type = MacAddress
_Repremotemacaddress1_Object = MibTableColumn
repremotemacaddress1 = _Repremotemacaddress1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 7),
    _Repremotemacaddress1_Type()
)
repremotemacaddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress1.setStatus("current")
_Repremotemacaddress2_Type = MacAddress
_Repremotemacaddress2_Object = MibTableColumn
repremotemacaddress2 = _Repremotemacaddress2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 8),
    _Repremotemacaddress2_Type()
)
repremotemacaddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress2.setStatus("current")
_Repremotemacaddress3_Type = MacAddress
_Repremotemacaddress3_Object = MibTableColumn
repremotemacaddress3 = _Repremotemacaddress3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 9),
    _Repremotemacaddress3_Type()
)
repremotemacaddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress3.setStatus("current")
_Repremotemacaddress4_Type = MacAddress
_Repremotemacaddress4_Object = MibTableColumn
repremotemacaddress4 = _Repremotemacaddress4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 10),
    _Repremotemacaddress4_Type()
)
repremotemacaddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress4.setStatus("current")
_LocalMacAddress_Type = MacAddress
_LocalMacAddress_Object = MibTableColumn
localMacAddress = _LocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 7, 1, 11),
    _LocalMacAddress_Type()
)
localMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localMacAddress.setStatus("current")
_Info802dot1x_ObjectIdentity = ObjectIdentity
info802dot1x = _Info802dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8)
)
_Authinfo_ObjectIdentity = ObjectIdentity
authinfo = _Authinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1)
)
_Priradipaddr_Type = IpAddress
_Priradipaddr_Object = MibScalar
priradipaddr = _Priradipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1, 1),
    _Priradipaddr_Type()
)
priradipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priradipaddr.setStatus("current")


class _Priradport_Type(Integer32):
    """Custom type priradport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Priradport_Type.__name__ = "Integer32"
_Priradport_Object = MibScalar
priradport = _Priradport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1, 2),
    _Priradport_Type()
)
priradport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priradport.setStatus("current")


class _Priradsharedsecret_Type(DisplayString):
    """Custom type priradsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Priradsharedsecret_Type.__name__ = "DisplayString"
_Priradsharedsecret_Object = MibScalar
priradsharedsecret = _Priradsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1, 3),
    _Priradsharedsecret_Type()
)
priradsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priradsharedsecret.setStatus("current")
_Sndradipaddr_Type = IpAddress
_Sndradipaddr_Object = MibScalar
sndradipaddr = _Sndradipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1, 4),
    _Sndradipaddr_Type()
)
sndradipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndradipaddr.setStatus("current")


class _Sndradport_Type(Integer32):
    """Custom type sndradport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sndradport_Type.__name__ = "Integer32"
_Sndradport_Object = MibScalar
sndradport = _Sndradport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1, 5),
    _Sndradport_Type()
)
sndradport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndradport.setStatus("current")


class _Sndradsharedsecret_Type(DisplayString):
    """Custom type sndradsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Sndradsharedsecret_Type.__name__ = "DisplayString"
_Sndradsharedsecret_Object = MibScalar
sndradsharedsecret = _Sndradsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 1, 6),
    _Sndradsharedsecret_Type()
)
sndradsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndradsharedsecret.setStatus("current")
_Accntinfo_ObjectIdentity = ObjectIdentity
accntinfo = _Accntinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2)
)
_Priacntipaddr_Type = IpAddress
_Priacntipaddr_Object = MibScalar
priacntipaddr = _Priacntipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2, 1),
    _Priacntipaddr_Type()
)
priacntipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priacntipaddr.setStatus("current")


class _Priacntport_Type(Integer32):
    """Custom type priacntport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Priacntport_Type.__name__ = "Integer32"
_Priacntport_Object = MibScalar
priacntport = _Priacntport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2, 2),
    _Priacntport_Type()
)
priacntport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priacntport.setStatus("current")


class _Priacntsharedsecret_Type(DisplayString):
    """Custom type priacntsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Priacntsharedsecret_Type.__name__ = "DisplayString"
_Priacntsharedsecret_Object = MibScalar
priacntsharedsecret = _Priacntsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2, 3),
    _Priacntsharedsecret_Type()
)
priacntsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priacntsharedsecret.setStatus("current")
_Sndacntipaddr_Type = IpAddress
_Sndacntipaddr_Object = MibScalar
sndacntipaddr = _Sndacntipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2, 4),
    _Sndacntipaddr_Type()
)
sndacntipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndacntipaddr.setStatus("current")


class _Sndacntport_Type(Integer32):
    """Custom type sndacntport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sndacntport_Type.__name__ = "Integer32"
_Sndacntport_Object = MibScalar
sndacntport = _Sndacntport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2, 5),
    _Sndacntport_Type()
)
sndacntport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndacntport.setStatus("current")


class _Sndacntsharedsecret_Type(DisplayString):
    """Custom type sndacntsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Sndacntsharedsecret_Type.__name__ = "DisplayString"
_Sndacntsharedsecret_Object = MibScalar
sndacntsharedsecret = _Sndacntsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 8, 2, 6),
    _Sndacntsharedsecret_Type()
)
sndacntsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndacntsharedsecret.setStatus("current")
_UserCommand_ObjectIdentity = ObjectIdentity
userCommand = _UserCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 9)
)
_ResetAP_Type = Integer32
_ResetAP_Object = MibScalar
resetAP = _ResetAP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 9, 1),
    _ResetAP_Type()
)
resetAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAP.setStatus("current")
_TimeSettings_ObjectIdentity = ObjectIdentity
timeSettings = _TimeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 10)
)


class _Currenttime_Type(DisplayString):
    """Custom type currenttime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Currenttime_Type.__name__ = "DisplayString"
_Currenttime_Object = MibScalar
currenttime = _Currenttime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 10, 1),
    _Currenttime_Type()
)
currenttime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currenttime.setStatus("current")


class _Timezone_Type(Integer32):
    """Custom type timezone based on Integer32"""
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
              279)
        )
    )
    namedValues = NamedValues(
        *(("afghanistan", 0),
          ("albania", 1),
          ("algeria", 2),
          ("american-samoa", 3),
          ("andorra", 4),
          ("angola", 5),
          ("anguilla", 6),
          ("antigua-and-barbuda", 7),
          ("argentina", 8),
          ("armenia", 9),
          ("aruba", 10),
          ("australia-lordHoweIsland", 11),
          ("australia-new-south-wales-capitol-territory-victoria", 12),
          ("australia-northern-territory", 13),
          ("australia-queensland", 14),
          ("australia-south-australia-and-broken-hill", 15),
          ("australia-tasmania", 16),
          ("australia-western", 17),
          ("austria", 18),
          ("azerbaijan", 19),
          ("bahamas", 20),
          ("bahrain", 21),
          ("bangladesh", 22),
          ("barbados", 23),
          ("belarus", 24),
          ("belgium", 25),
          ("belize", 26),
          ("benin", 27),
          ("bermuda", 28),
          ("bhutan", 29),
          ("bolivia", 30),
          ("bonaire", 31),
          ("bosnia-herzegovina", 32),
          ("botswana", 33),
          ("brazil-east-including-all-coast-and-brasilia", 34),
          ("brazil-fernando-de-noronha", 35),
          ("brazil-trinity-of-acre", 36),
          ("brazil-west", 37),
          ("british-virgin-islands", 38),
          ("brunei", 39),
          ("bulgaria", 40),
          ("burkina-faso", 41),
          ("burma", 42),
          ("burundi", 43),
          ("cambodia", 44),
          ("cameroon", 45),
          ("canada-atlantic", 46),
          ("canada-central", 47),
          ("canada-eastern", 48),
          ("canada-mountain", 49),
          ("canada-newfoundland", 50),
          ("canada-pacific-and-yukon", 51),
          ("canada-saskatchewan", 52),
          ("cape-verde", 53),
          ("cayman-islands", 54),
          ("central-african-republic", 55),
          ("chad", 56),
          ("chile", 57),
          ("chile-easter-island", 58),
          ("china", 59),
          ("christmas-islands", 60),
          ("cocos-keeling-islands", 61),
          ("colombia", 62),
          ("congo", 63),
          ("cook-islands", 64),
          ("costa-rica", 65),
          ("cote-d-ivoire", 66),
          ("croatia", 67),
          ("cuba", 68),
          ("curacao", 69),
          ("cyprus", 70),
          ("czech-republic", 71),
          ("denmark", 72),
          ("djibouti", 73),
          ("dominica", 74),
          ("ecuador", 76),
          ("ecuador-galapagos-islands", 77),
          ("egypt", 78),
          ("el-salvador", 79),
          ("equatorial-guinea", 80),
          ("eritrea", 81),
          ("estonia", 82),
          ("ethiopia", 83),
          ("faroe-islands", 84),
          ("fiji", 85),
          ("finland", 86),
          ("france", 87),
          ("french-guiana", 88),
          ("french-polynesia", 89),
          ("gabon", 90),
          ("georgia", 92),
          ("germany", 93),
          ("ghana", 94),
          ("gibraltar", 95),
          ("greece", 96),
          ("greenland-scorsbysund", 97),
          ("greenland-thule", 98),
          ("grenada", 99),
          ("guadeloupe", 100),
          ("guam", 101),
          ("guatemala", 102),
          ("guinea-bissau", 103),
          ("guyana", 104),
          ("haiti", 105),
          ("hawaii", 106),
          ("honduras", 107),
          ("hong-kong", 108),
          ("hungary", 109),
          ("iceland", 110),
          ("india", 111),
          ("indonesia-central", 112),
          ("indonesia-east", 113),
          ("indonesia-west", 114),
          ("iran", 115),
          ("iraq", 116),
          ("ireland", 117),
          ("israel", 118),
          ("italy", 119),
          ("jamaica", 120),
          ("japan", 121),
          ("johnston-islands", 122),
          ("jordan", 123),
          ("juan-fernandez-islands", 124),
          ("kazakhstan", 125),
          ("kenya", 126),
          ("kiribati", 127),
          ("kuwait", 128),
          ("kyrgyzstan", 129),
          ("laos", 130),
          ("latvia", 131),
          ("lebanon", 132),
          ("leeward-islands", 133),
          ("lesotho", 134),
          ("liberia", 135),
          ("libya", 136),
          ("liechtenstein", 137),
          ("lithuania", 138),
          ("luxembourg", 139),
          ("macao", 140),
          ("macedonia", 141),
          ("madagascar", 142),
          ("malawi", 143),
          ("malaysia", 144),
          ("maldives", 145),
          ("mali", 146),
          ("malta", 147),
          ("mariana-Islands", 148),
          ("martinique", 149),
          ("mauritania", 150),
          ("mauritius", 151),
          ("mayotte", 152),
          ("mexico", 153),
          ("mexico-baj-n", 154),
          ("mexico-baj-s", 155),
          ("midway-islands", 156),
          ("moldova", 157),
          ("monaco", 158),
          ("mongolia", 159),
          ("montenegro", 160),
          ("montserrat", 161),
          ("morocco", 162),
          ("mozambique", 163),
          ("namibia", 164),
          ("nauru", 165),
          ("nepal", 166),
          ("new-caledonia", 169),
          ("new-hebrides", 170),
          ("new-zealand-chatham-island", 172),
          ("new-zealand9", 171),
          ("nicaragua", 173),
          ("niger", 174),
          ("nigeria", 175),
          ("niue-islands", 176),
          ("norfolk-island", 177),
          ("north-korea", 178),
          ("norway", 179),
          ("oman", 180),
          ("pakistan", 181),
          ("palau", 182),
          ("panama", 183),
          ("papua-new-guinea", 184),
          ("paraguay", 185),
          ("peru", 186),
          ("philippines", 187),
          ("pitcairn-island", 188),
          ("poland", 189),
          ("portugal-azores", 190),
          ("portugal-madeira", 191),
          ("puerto-rico", 192),
          ("qatar", 193),
          ("reunion", 194),
          ("romania", 195),
          ("russia-moscow", 196),
          ("russian-fed-zone-1-kaliningrad", 197),
          ("russian-fed-zone-10-magadan", 198),
          ("russian-fed-zone-11-petropavlovsk-kamchatsky", 199),
          ("russian-fed-zone-2-st-petersburg", 200),
          ("russian-fed-zone-3-izhevsk", 201),
          ("russian-fed-zone-4-ekaterinburg", 202),
          ("russian-fed-zone-5-novosibirsk", 203),
          ("russian-fed-zone-6-krasnojarsk", 204),
          ("russian-fed-zone-7-irkutsk", 205),
          ("russian-fed-zone-8-yakatsk", 206),
          ("russian-fed-zone-9-vladivostok", 207),
          ("rwanda", 208),
          ("saint-pierre-and-miquelon", 209),
          ("san-marino", 210),
          ("sao-tome-and-principe", 211),
          ("saudi-arabia", 212),
          ("senegal", 213),
          ("serbia", 214),
          ("sierra-leone", 216),
          ("singapore", 217),
          ("slovakia", 218),
          ("slovenia", 219),
          ("solomon-islands", 220),
          ("somalia", 221),
          ("south-africa", 222),
          ("south-georgia", 223),
          ("south-korea", 224),
          ("spain", 225),
          ("spain-canary-islands", 226),
          ("sri-lanka", 227),
          ("st-helena", 228),
          ("st-kitts-nevis", 229),
          ("st-lucia", 230),
          ("st-vincent-and-the-grenadines", 231),
          ("sudan", 232),
          ("suriname", 233),
          ("swaziland", 234),
          ("sweden", 235),
          ("switzerland", 236),
          ("syria", 237),
          ("tahiti", 238),
          ("taiwan", 239),
          ("tajikistan", 240),
          ("tanzania", 241),
          ("thailand", 242),
          ("the-dominican-republic", 75),
          ("the-gambia", 91),
          ("the-netherlands", 168),
          ("the-netherlands-antilles", 167),
          ("the-seychelles", 215),
          ("togo", 243),
          ("tonga", 244),
          ("trinidad-and-tobago", 245),
          ("tunisia", 246),
          ("turkey", 247),
          ("turkmenistan", 248),
          ("turks-and-caicos-islands", 249),
          ("tuvalu", 250),
          ("uganda", 251),
          ("ukraine", 252),
          ("ukraine-simferopol", 253),
          ("united-arab-emirates", 254),
          ("united-kingdom", 255),
          ("uruguay", 256),
          ("us-virgin-islands", 257),
          ("usa-alaska", 258),
          ("usa-aleutian-islands", 259),
          ("usa-arizona", 260),
          ("usa-central", 261),
          ("usa-eastern", 262),
          ("usa-indiana", 263),
          ("usa-mountain", 264),
          ("usa-pacific", 265),
          ("uzbekistan", 266),
          ("vanuatu", 267),
          ("vatican-city", 268),
          ("venezuela", 269),
          ("vietnam", 270),
          ("wake-islands", 271),
          ("wallis-and-futana-islands", 272),
          ("western-samoa", 273),
          ("windward-islands", 274),
          ("yemen", 275),
          ("zaire-kasai", 276),
          ("zaire-kinshasa", 277),
          ("zambia", 278),
          ("zimbabwe", 279))
    )


_Timezone_Type.__name__ = "Integer32"
_Timezone_Object = MibScalar
timezone = _Timezone_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 10, 2),
    _Timezone_Type()
)
timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timezone.setStatus("current")
_Daylightsaving_Type = TruthValue
_Daylightsaving_Object = MibScalar
daylightsaving = _Daylightsaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 10, 3),
    _Daylightsaving_Type()
)
daylightsaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightsaving.setStatus("current")
_DhcpsSettings_ObjectIdentity = ObjectIdentity
dhcpsSettings = _DhcpsSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11)
)
_Dhcpserver_Type = TruthValue
_Dhcpserver_Object = MibScalar
dhcpserver = _Dhcpserver_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 1),
    _Dhcpserver_Type()
)
dhcpserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpserver.setStatus("current")
_Dhcpsipstart_Type = IpAddress
_Dhcpsipstart_Object = MibScalar
dhcpsipstart = _Dhcpsipstart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 2),
    _Dhcpsipstart_Type()
)
dhcpsipstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsipstart.setStatus("current")
_Dhcpsipend_Type = IpAddress
_Dhcpsipend_Object = MibScalar
dhcpsipend = _Dhcpsipend_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 3),
    _Dhcpsipend_Type()
)
dhcpsipend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsipend.setStatus("current")
_Dhcpnetmask_Type = IpAddress
_Dhcpnetmask_Object = MibScalar
dhcpnetmask = _Dhcpnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 4),
    _Dhcpnetmask_Type()
)
dhcpnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpnetmask.setStatus("current")
_Dhcpsgateway_Type = IpAddress
_Dhcpsgateway_Object = MibScalar
dhcpsgateway = _Dhcpsgateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 5),
    _Dhcpsgateway_Type()
)
dhcpsgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsgateway.setStatus("current")
_Dhcpspridns_Type = IpAddress
_Dhcpspridns_Object = MibScalar
dhcpspridns = _Dhcpspridns_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 6),
    _Dhcpspridns_Type()
)
dhcpspridns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspridns.setStatus("current")
_Dhcpspsnddns_Type = IpAddress
_Dhcpspsnddns_Object = MibScalar
dhcpspsnddns = _Dhcpspsnddns_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 7),
    _Dhcpspsnddns_Type()
)
dhcpspsnddns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspsnddns.setStatus("current")
_Dhcpspriwins_Type = IpAddress
_Dhcpspriwins_Object = MibScalar
dhcpspriwins = _Dhcpspriwins_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 8),
    _Dhcpspriwins_Type()
)
dhcpspriwins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspriwins.setStatus("current")
_Dhcpspsndwins_Type = IpAddress
_Dhcpspsndwins_Object = MibScalar
dhcpspsndwins = _Dhcpspsndwins_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 9),
    _Dhcpspsndwins_Type()
)
dhcpspsndwins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspsndwins.setStatus("current")


class _Dhcpsleasetime_Type(Integer32):
    """Custom type dhcpsleasetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 44640),
    )


_Dhcpsleasetime_Type.__name__ = "Integer32"
_Dhcpsleasetime_Object = MibScalar
dhcpsleasetime = _Dhcpsleasetime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 11, 10),
    _Dhcpsleasetime_Type()
)
dhcpsleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsleasetime.setStatus("current")
_LogSettings_ObjectIdentity = ObjectIdentity
logSettings = _LogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 12)
)
_Syslog_Type = TruthValue
_Syslog_Object = MibScalar
syslog = _Syslog_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 12, 1),
    _Syslog_Type()
)
syslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslog.setStatus("current")
_Syslogsrvip_Type = IpAddress
_Syslogsrvip_Object = MibScalar
syslogsrvip = _Syslogsrvip_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 12, 2),
    _Syslogsrvip_Type()
)
syslogsrvip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogsrvip.setStatus("current")


class _Syslogsrvport_Type(Integer32):
    """Custom type syslogsrvport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Syslogsrvport_Type.__name__ = "Integer32"
_Syslogsrvport_Object = MibScalar
syslogsrvport = _Syslogsrvport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 12, 3),
    _Syslogsrvport_Type()
)
syslogsrvport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogsrvport.setStatus("current")
_HttpRedirectSettings_ObjectIdentity = ObjectIdentity
httpRedirectSettings = _HttpRedirectSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 13)
)
_HttpRedirectEnable_Type = TruthValue
_HttpRedirectEnable_Object = MibScalar
httpRedirectEnable = _HttpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 13, 1),
    _HttpRedirectEnable_Type()
)
httpRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRedirectEnable.setStatus("current")


class _HttpRedirectURL_Type(DisplayString):
    """Custom type httpRedirectURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_HttpRedirectURL_Type.__name__ = "DisplayString"
_HttpRedirectURL_Object = MibScalar
httpRedirectURL = _HttpRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 13, 2),
    _HttpRedirectURL_Type()
)
httpRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpRedirectURL.setStatus("current")
_DetectedApTable_Object = MibTable
detectedApTable = _DetectedApTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14)
)
if mibBuilder.loadTexts:
    detectedApTable.setStatus("current")
_DetectedApEntry_Object = MibTableRow
detectedApEntry = _DetectedApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1)
)
detectedApEntry.setIndexNames(
    (0, "WAG302", "apmac"),
)
if mibBuilder.loadTexts:
    detectedApEntry.setStatus("current")
_Apmac_Type = MacAddress
_Apmac_Object = MibTableColumn
apmac = _Apmac_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 1),
    _Apmac_Type()
)
apmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmac.setStatus("current")
_Apssid_Type = DisplayString
_Apssid_Object = MibTableColumn
apssid = _Apssid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 2),
    _Apssid_Type()
)
apssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apssid.setStatus("current")
_Apprivacy_Type = TruthValue
_Apprivacy_Object = MibTableColumn
apprivacy = _Apprivacy_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 3),
    _Apprivacy_Type()
)
apprivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apprivacy.setStatus("current")
_Apband_Type = DisplayString
_Apband_Object = MibTableColumn
apband = _Apband_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 4),
    _Apband_Type()
)
apband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apband.setStatus("current")
_Apchannel_Type = Integer32
_Apchannel_Object = MibTableColumn
apchannel = _Apchannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 5),
    _Apchannel_Type()
)
apchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apchannel.setStatus("current")
_Aprate_Type = Integer32
_Aprate_Object = MibTableColumn
aprate = _Aprate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 6),
    _Aprate_Type()
)
aprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aprate.setStatus("current")
_ApbeaconInterval_Type = Integer32
_ApbeaconInterval_Object = MibTableColumn
apbeaconInterval = _ApbeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 7),
    _ApbeaconInterval_Type()
)
apbeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apbeaconInterval.setStatus("current")
_ApnumBeacons_Type = Integer32
_ApnumBeacons_Object = MibTableColumn
apnumBeacons = _ApnumBeacons_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 8),
    _ApnumBeacons_Type()
)
apnumBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnumBeacons.setStatus("current")
_AplastBeacon_Type = Integer32
_AplastBeacon_Object = MibTableColumn
aplastBeacon = _AplastBeacon_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 14, 1, 9),
    _AplastBeacon_Type()
)
aplastBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aplastBeacon.setStatus("current")
_KnownApTable_Object = MibTable
knownApTable = _KnownApTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15)
)
if mibBuilder.loadTexts:
    knownApTable.setStatus("current")
_KnownApEntry_Object = MibTableRow
knownApEntry = _KnownApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1)
)
knownApEntry.setIndexNames(
    (0, "WAG302", "knownapmac"),
)
if mibBuilder.loadTexts:
    knownApEntry.setStatus("current")
_Knownapmac_Type = MacAddress
_Knownapmac_Object = MibTableColumn
knownapmac = _Knownapmac_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 1),
    _Knownapmac_Type()
)
knownapmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapmac.setStatus("current")
_Knownapssid_Type = DisplayString
_Knownapssid_Object = MibTableColumn
knownapssid = _Knownapssid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 2),
    _Knownapssid_Type()
)
knownapssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapssid.setStatus("current")
_Knownapprivacy_Type = TruthValue
_Knownapprivacy_Object = MibTableColumn
knownapprivacy = _Knownapprivacy_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 3),
    _Knownapprivacy_Type()
)
knownapprivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapprivacy.setStatus("current")
_Knownapband_Type = DisplayString
_Knownapband_Object = MibTableColumn
knownapband = _Knownapband_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 4),
    _Knownapband_Type()
)
knownapband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapband.setStatus("current")
_Knownapchannel_Type = Integer32
_Knownapchannel_Object = MibTableColumn
knownapchannel = _Knownapchannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 5),
    _Knownapchannel_Type()
)
knownapchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapchannel.setStatus("current")
_Knownaprate_Type = Integer32
_Knownaprate_Object = MibTableColumn
knownaprate = _Knownaprate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 6),
    _Knownaprate_Type()
)
knownaprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownaprate.setStatus("current")
_KnownapbeaconInterval_Type = Integer32
_KnownapbeaconInterval_Object = MibTableColumn
knownapbeaconInterval = _KnownapbeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 7),
    _KnownapbeaconInterval_Type()
)
knownapbeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapbeaconInterval.setStatus("current")
_KnownapnumBeacons_Type = Integer32
_KnownapnumBeacons_Object = MibTableColumn
knownapnumBeacons = _KnownapnumBeacons_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 8),
    _KnownapnumBeacons_Type()
)
knownapnumBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownapnumBeacons.setStatus("current")
_KnownaplastBeacon_Type = Integer32
_KnownaplastBeacon_Object = MibTableColumn
knownaplastBeacon = _KnownaplastBeacon_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 9),
    _KnownaplastBeacon_Type()
)
knownaplastBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownaplastBeacon.setStatus("current")
_KnownapEntryStatus_Type = Integer32
_KnownapEntryStatus_Object = MibTableColumn
knownapEntryStatus = _KnownapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 15, 1, 10),
    _KnownapEntryStatus_Type()
)
knownapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    knownapEntryStatus.setStatus("current")
_UnknownApTable_Object = MibTable
unknownApTable = _UnknownApTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16)
)
if mibBuilder.loadTexts:
    unknownApTable.setStatus("current")
_UnknownApEntry_Object = MibTableRow
unknownApEntry = _UnknownApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1)
)
unknownApEntry.setIndexNames(
    (0, "WAG302", "unknownapmac"),
)
if mibBuilder.loadTexts:
    unknownApEntry.setStatus("current")
_Unknownapmac_Type = MacAddress
_Unknownapmac_Object = MibTableColumn
unknownapmac = _Unknownapmac_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 1),
    _Unknownapmac_Type()
)
unknownapmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapmac.setStatus("current")
_Unknownapssid_Type = DisplayString
_Unknownapssid_Object = MibTableColumn
unknownapssid = _Unknownapssid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 2),
    _Unknownapssid_Type()
)
unknownapssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapssid.setStatus("current")
_Unknownapprivacy_Type = TruthValue
_Unknownapprivacy_Object = MibTableColumn
unknownapprivacy = _Unknownapprivacy_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 3),
    _Unknownapprivacy_Type()
)
unknownapprivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapprivacy.setStatus("current")
_Unknownapband_Type = DisplayString
_Unknownapband_Object = MibTableColumn
unknownapband = _Unknownapband_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 4),
    _Unknownapband_Type()
)
unknownapband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapband.setStatus("current")
_Unknownapchannel_Type = Integer32
_Unknownapchannel_Object = MibTableColumn
unknownapchannel = _Unknownapchannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 5),
    _Unknownapchannel_Type()
)
unknownapchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapchannel.setStatus("current")
_Unknownaprate_Type = Integer32
_Unknownaprate_Object = MibTableColumn
unknownaprate = _Unknownaprate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 6),
    _Unknownaprate_Type()
)
unknownaprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownaprate.setStatus("current")
_UnknownapbeaconInterval_Type = Integer32
_UnknownapbeaconInterval_Object = MibTableColumn
unknownapbeaconInterval = _UnknownapbeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 7),
    _UnknownapbeaconInterval_Type()
)
unknownapbeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapbeaconInterval.setStatus("current")
_UnknownapnumBeacons_Type = Integer32
_UnknownapnumBeacons_Object = MibTableColumn
unknownapnumBeacons = _UnknownapnumBeacons_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 8),
    _UnknownapnumBeacons_Type()
)
unknownapnumBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownapnumBeacons.setStatus("current")
_UnknownaplastBeacon_Type = Integer32
_UnknownaplastBeacon_Object = MibTableColumn
unknownaplastBeacon = _UnknownaplastBeacon_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 16, 1, 9),
    _UnknownaplastBeacon_Type()
)
unknownaplastBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownaplastBeacon.setStatus("current")
_WlanAccessControlLocalTable_Object = MibTable
wlanAccessControlLocalTable = _WlanAccessControlLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 17)
)
if mibBuilder.loadTexts:
    wlanAccessControlLocalTable.setStatus("current")
_WlanAccessControlLocalEntry_Object = MibTableRow
wlanAccessControlLocalEntry = _WlanAccessControlLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 17, 1)
)
wlanAccessControlLocalEntry.setIndexNames(
    (0, "WAG302", "aclMAC"),
)
if mibBuilder.loadTexts:
    wlanAccessControlLocalEntry.setStatus("current")
_AclMAC_Type = MacAddress
_AclMAC_Object = MibTableColumn
aclMAC = _AclMAC_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 17, 1, 1),
    _AclMAC_Type()
)
aclMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMAC.setStatus("current")
_AclMacStatus_Type = Integer32
_AclMacStatus_Object = MibTableColumn
aclMacStatus = _AclMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7, 17, 1, 2),
    _AclMacStatus_Type()
)
aclMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAG302",
    **{"netgear": netgear,
       "wireless": wireless,
       "wag302": wag302,
       "lanSettings": lanSettings,
       "apName": apName,
       "sysMacAddress": sysMacAddress,
       "sysVersion": sysVersion,
       "sysCountryRegion": sysCountryRegion,
       "adminName": adminName,
       "adminPasswd": adminPasswd,
       "dhcpStatus": dhcpStatus,
       "ipAddr": ipAddr,
       "netmaskAddr": netmaskAddr,
       "gatewayAddr": gatewayAddr,
       "pridnsipAddr": pridnsipAddr,
       "snddnsipAddr": snddnsipAddr,
       "spantree": spantree,
       "vlanEnable": vlanEnable,
       "managementVlanID": managementVlanID,
       "untaggedVlanID": untaggedVlanID,
       "wlanSettingTable": wlanSettingTable,
       "wlanSettingEntry": wlanSettingEntry,
       "operatemode": operatemode,
       "radioEnable": radioEnable,
       "channel": channel,
       "datarate": datarate,
       "wmmSupport": wmmSupport,
       "beaconinterval": beaconinterval,
       "rtsthreshold": rtsthreshold,
       "fraglength": fraglength,
       "dtiminterval": dtiminterval,
       "preambletype": preambletype,
       "txpower": txpower,
       "superG": superG,
       "accessControlMode": accessControlMode,
       "antenna": antenna,
       "vapSetting": vapSetting,
       "vapWepAndGlobalSettingTable": vapWepAndGlobalSettingTable,
       "vapWepAndGlobalSettingEntry": vapWepAndGlobalSettingEntry,
       "wepKeyType": wepKeyType,
       "key1": key1,
       "key2": key2,
       "key3": key3,
       "key4": key4,
       "wepPassPhrase": wepPassPhrase,
       "vapSettingTable": vapSettingTable,
       "vapSettingEntry": vapSettingEntry,
       "vapIndex": vapIndex,
       "vapEnable": vapEnable,
       "ssid": ssid,
       "hidenetworkname": hidenetworkname,
       "vlanID": vlanID,
       "securityProfileName": securityProfileName,
       "presharekey": presharekey,
       "authenticationtype": authenticationtype,
       "encryption": encryption,
       "keyno": keyno,
       "wlanseparator": wlanseparator,
       "remoteSettings": remoteSettings,
       "sshd": sshd,
       "snmpenable": snmpenable,
       "trapServerIP": trapServerIP,
       "trapServerCommunity": trapServerCommunity,
       "readOnlyCommunity": readOnlyCommunity,
       "readWriteCommunity": readWriteCommunity,
       "statistic": statistic,
       "wiredethernetstat": wiredethernetstat,
       "lanrecvpacket": lanrecvpacket,
       "lantranspacket": lantranspacket,
       "lanrecvbytes": lanrecvbytes,
       "lantransbytes": lantransbytes,
       "wirelessStatTable": wirelessStatTable,
       "wirelessStatEntry": wirelessStatEntry,
       "wlanrecvunicastpacket": wlanrecvunicastpacket,
       "wlantransunicastpacket": wlantransunicastpacket,
       "wlanrecvbroadcastpacket": wlanrecvbroadcastpacket,
       "wlantransbroadcastpacket": wlantransbroadcastpacket,
       "wlanrecvmulticastpacket": wlanrecvmulticastpacket,
       "wlantransmulticastpacket": wlantransmulticastpacket,
       "wlanrecvpacket": wlanrecvpacket,
       "wlantranspacket": wlantranspacket,
       "wlanrecvbytes": wlanrecvbytes,
       "wlantransbytes": wlantransbytes,
       "stationListTable": stationListTable,
       "stationListEntry": stationListEntry,
       "macaddress": macaddress,
       "clientIpaddr": clientIpaddr,
       "clientWirelessMode": clientWirelessMode,
       "stationstatus": stationstatus,
       "wlanWdsTable": wlanWdsTable,
       "wlanWdsEntry": wlanWdsEntry,
       "apmode": apmode,
       "ptpremotemacaddress": ptpremotemacaddress,
       "pxpremotemacaddress1": pxpremotemacaddress1,
       "pxpremotemacaddress2": pxpremotemacaddress2,
       "pxpremotemacaddress3": pxpremotemacaddress3,
       "pxpremotemacaddress4": pxpremotemacaddress4,
       "repremotemacaddress1": repremotemacaddress1,
       "repremotemacaddress2": repremotemacaddress2,
       "repremotemacaddress3": repremotemacaddress3,
       "repremotemacaddress4": repremotemacaddress4,
       "localMacAddress": localMacAddress,
       "info802dot1x": info802dot1x,
       "authinfo": authinfo,
       "priradipaddr": priradipaddr,
       "priradport": priradport,
       "priradsharedsecret": priradsharedsecret,
       "sndradipaddr": sndradipaddr,
       "sndradport": sndradport,
       "sndradsharedsecret": sndradsharedsecret,
       "accntinfo": accntinfo,
       "priacntipaddr": priacntipaddr,
       "priacntport": priacntport,
       "priacntsharedsecret": priacntsharedsecret,
       "sndacntipaddr": sndacntipaddr,
       "sndacntport": sndacntport,
       "sndacntsharedsecret": sndacntsharedsecret,
       "userCommand": userCommand,
       "resetAP": resetAP,
       "timeSettings": timeSettings,
       "currenttime": currenttime,
       "timezone": timezone,
       "daylightsaving": daylightsaving,
       "dhcpsSettings": dhcpsSettings,
       "dhcpserver": dhcpserver,
       "dhcpsipstart": dhcpsipstart,
       "dhcpsipend": dhcpsipend,
       "dhcpnetmask": dhcpnetmask,
       "dhcpsgateway": dhcpsgateway,
       "dhcpspridns": dhcpspridns,
       "dhcpspsnddns": dhcpspsnddns,
       "dhcpspriwins": dhcpspriwins,
       "dhcpspsndwins": dhcpspsndwins,
       "dhcpsleasetime": dhcpsleasetime,
       "logSettings": logSettings,
       "syslog": syslog,
       "syslogsrvip": syslogsrvip,
       "syslogsrvport": syslogsrvport,
       "httpRedirectSettings": httpRedirectSettings,
       "httpRedirectEnable": httpRedirectEnable,
       "httpRedirectURL": httpRedirectURL,
       "detectedApTable": detectedApTable,
       "detectedApEntry": detectedApEntry,
       "apmac": apmac,
       "apssid": apssid,
       "apprivacy": apprivacy,
       "apband": apband,
       "apchannel": apchannel,
       "aprate": aprate,
       "apbeaconInterval": apbeaconInterval,
       "apnumBeacons": apnumBeacons,
       "aplastBeacon": aplastBeacon,
       "knownApTable": knownApTable,
       "knownApEntry": knownApEntry,
       "knownapmac": knownapmac,
       "knownapssid": knownapssid,
       "knownapprivacy": knownapprivacy,
       "knownapband": knownapband,
       "knownapchannel": knownapchannel,
       "knownaprate": knownaprate,
       "knownapbeaconInterval": knownapbeaconInterval,
       "knownapnumBeacons": knownapnumBeacons,
       "knownaplastBeacon": knownaplastBeacon,
       "knownapEntryStatus": knownapEntryStatus,
       "unknownApTable": unknownApTable,
       "unknownApEntry": unknownApEntry,
       "unknownapmac": unknownapmac,
       "unknownapssid": unknownapssid,
       "unknownapprivacy": unknownapprivacy,
       "unknownapband": unknownapband,
       "unknownapchannel": unknownapchannel,
       "unknownaprate": unknownaprate,
       "unknownapbeaconInterval": unknownapbeaconInterval,
       "unknownapnumBeacons": unknownapnumBeacons,
       "unknownaplastBeacon": unknownaplastBeacon,
       "wlanAccessControlLocalTable": wlanAccessControlLocalTable,
       "wlanAccessControlLocalEntry": wlanAccessControlLocalEntry,
       "aclMAC": aclMAC,
       "aclMacStatus": aclMacStatus}
)
