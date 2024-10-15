# SNMP MIB module (WG302-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WG302-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:51 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

accesspoint = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2)
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 1),
    _ApName_Type()
)
apName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apName.setStatus("current")


class _AdminName_Type(DisplayString):
    """Custom type adminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminName_Type.__name__ = "DisplayString"
_AdminName_Object = MibScalar
adminName = _AdminName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 2),
    _AdminName_Type()
)
adminName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminName.setStatus("current")


class _AdminPasswd_Type(DisplayString):
    """Custom type adminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminPasswd_Type.__name__ = "DisplayString"
_AdminPasswd_Object = MibScalar
adminPasswd = _AdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 3),
    _AdminPasswd_Type()
)
adminPasswd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminPasswd.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 4),
    _DhcpStatus_Type()
)
dhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStatus.setStatus("current")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 5),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_NetmaskAddr_Type = IpAddress
_NetmaskAddr_Object = MibScalar
netmaskAddr = _NetmaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 6),
    _NetmaskAddr_Type()
)
netmaskAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netmaskAddr.setStatus("current")
_GatewayAddr_Type = IpAddress
_GatewayAddr_Object = MibScalar
gatewayAddr = _GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 7),
    _GatewayAddr_Type()
)
gatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayAddr.setStatus("current")
_Spantree_Type = TruthValue
_Spantree_Object = MibScalar
spantree = _Spantree_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 8),
    _Spantree_Type()
)
spantree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spantree.setStatus("current")
_PridnsipAddr_Type = IpAddress
_PridnsipAddr_Object = MibScalar
pridnsipAddr = _PridnsipAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 9),
    _PridnsipAddr_Type()
)
pridnsipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pridnsipAddr.setStatus("current")
_SnddnsipAddr_Type = IpAddress
_SnddnsipAddr_Object = MibScalar
snddnsipAddr = _SnddnsipAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 1, 10),
    _SnddnsipAddr_Type()
)
snddnsipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snddnsipAddr.setStatus("current")
_WlanSettingTable_Object = MibTable
wlanSettingTable = _WlanSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2)
)
if mibBuilder.loadTexts:
    wlanSettingTable.setStatus("current")
_WlanSettingEntry_Object = MibTableRow
wlanSettingEntry = _WlanSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1)
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_Operatemode_Type.__name__ = "Integer32"
_Operatemode_Object = MibTableColumn
operatemode = _Operatemode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 1),
    _Operatemode_Type()
)
operatemode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatemode.setStatus("current")


class _Ssid_Type(DisplayString):
    """Custom type ssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ssid_Type.__name__ = "DisplayString"
_Ssid_Object = MibTableColumn
ssid = _Ssid_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 2),
    _Ssid_Type()
)
ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssid.setStatus("current")


class _Countrycode_Type(Integer32):
    """Custom type countrycode based on Integer32"""
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
          ("newzealand", 554),
          ("norway", 578),
          ("puertorico", 630),
          ("southamerica", 340),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("unitedkingdom", 826),
          ("unitedstates", 840))
    )


_Countrycode_Type.__name__ = "Integer32"
_Countrycode_Object = MibTableColumn
countrycode = _Countrycode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 3),
    _Countrycode_Type()
)
countrycode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countrycode.setStatus("current")


class _Channel_Type(Integer32):
    """Custom type channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Channel_Type.__name__ = "Integer32"
_Channel_Object = MibTableColumn
channel = _Channel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 4),
    _Channel_Type()
)
channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channel.setStatus("current")


class _Datarate_Type(DisplayString):
    """Custom type datarate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Datarate_Type.__name__ = "DisplayString"
_Datarate_Object = MibTableColumn
datarate = _Datarate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 5),
    _Datarate_Type()
)
datarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datarate.setStatus("current")


class _Beaconinterval_Type(Integer32):
    """Custom type beaconinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_Beaconinterval_Type.__name__ = "Integer32"
_Beaconinterval_Object = MibTableColumn
beaconinterval = _Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 6),
    _Beaconinterval_Type()
)
beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconinterval.setStatus("current")


class _Rtsthreshold_Type(Integer32):
    """Custom type rtsthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2346),
    )


_Rtsthreshold_Type.__name__ = "Integer32"
_Rtsthreshold_Object = MibTableColumn
rtsthreshold = _Rtsthreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 10),
    _Preambletype_Type()
)
preambletype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preambletype.setStatus("current")
_Hidenetworkname_Type = TruthValue
_Hidenetworkname_Object = MibTableColumn
hidenetworkname = _Hidenetworkname_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 11),
    _Hidenetworkname_Type()
)
hidenetworkname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hidenetworkname.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 12),
    _Txpower_Type()
)
txpower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txpower.setStatus("current")
_SuperG_Type = TruthValue
_SuperG_Object = MibTableColumn
superG = _SuperG_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 13),
    _SuperG_Type()
)
superG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superG.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 2, 1, 14),
    _Antenna_Type()
)
antenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antenna.setStatus("current")
_SecurityTable_Object = MibTable
securityTable = _SecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3)
)
if mibBuilder.loadTexts:
    securityTable.setStatus("current")
_SecurityEntry_Object = MibTableRow
securityEntry = _SecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1)
)
securityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    securityEntry.setStatus("current")


class _Authenticationtype_Type(Integer32):
    """Custom type authenticationtype based on Integer32"""
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
        *(("legacy802dot1x", 2),
          ("open", 0),
          ("shared", 1),
          ("wpa", 3),
          ("wpapsk", 4))
    )


_Authenticationtype_Type.__name__ = "Integer32"
_Authenticationtype_Object = MibTableColumn
authenticationtype = _Authenticationtype_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 1),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tkip", 2),
          ("wep", 1))
    )


_Encryption_Type.__name__ = "Integer32"
_Encryption_Object = MibTableColumn
encryption = _Encryption_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 2),
    _Encryption_Type()
)
encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption.setStatus("current")


class _Encryptionstrength_Type(Integer32):
    """Custom type encryptionstrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              40,
              104,
              128)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep128", 104),
          ("wep152", 128),
          ("wep64", 40))
    )


_Encryptionstrength_Type.__name__ = "Integer32"
_Encryptionstrength_Object = MibTableColumn
encryptionstrength = _Encryptionstrength_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 3),
    _Encryptionstrength_Type()
)
encryptionstrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptionstrength.setStatus("current")


class _Keyno_Type(Integer32):
    """Custom type keyno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Keyno_Type.__name__ = "Integer32"
_Keyno_Object = MibTableColumn
keyno = _Keyno_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 4),
    _Keyno_Type()
)
keyno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyno.setStatus("current")


class _Key1_Type(DisplayString):
    """Custom type key1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Key1_Type.__name__ = "DisplayString"
_Key1_Object = MibTableColumn
key1 = _Key1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 8),
    _Key4_Type()
)
key4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key4.setStatus("current")
_Wlanseparator_Type = TruthValue
_Wlanseparator_Object = MibTableColumn
wlanseparator = _Wlanseparator_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 9),
    _Wlanseparator_Type()
)
wlanseparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanseparator.setStatus("current")


class _Presharekey_Type(DisplayString):
    """Custom type presharekey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Presharekey_Type.__name__ = "DisplayString"
_Presharekey_Object = MibTableColumn
presharekey = _Presharekey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 3, 1, 10),
    _Presharekey_Type()
)
presharekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presharekey.setStatus("current")
_RemoteSettings_ObjectIdentity = ObjectIdentity
remoteSettings = _RemoteSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 4)
)
_Sshd_Type = TruthValue
_Sshd_Object = MibScalar
sshd = _Sshd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 1),
    _Sshd_Type()
)
sshd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshd.setStatus("current")
_Snmpenable_Type = TruthValue
_Snmpenable_Object = MibScalar
snmpenable = _Snmpenable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 2),
    _Snmpenable_Type()
)
snmpenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpenable.setStatus("current")
_TrapServerIP_Type = IpAddress
_TrapServerIP_Object = MibScalar
trapServerIP = _TrapServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 3),
    _TrapServerIP_Type()
)
trapServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerIP.setStatus("current")


class _ReadOnlyCommunity_Type(DisplayString):
    """Custom type readOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ReadOnlyCommunity_Type.__name__ = "DisplayString"
_ReadOnlyCommunity_Object = MibScalar
readOnlyCommunity = _ReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 4, 5),
    _ReadWriteCommunity_Type()
)
readWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readWriteCommunity.setStatus("current")
_Statistic_ObjectIdentity = ObjectIdentity
statistic = _Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5)
)
_Wiredethernetstat_ObjectIdentity = ObjectIdentity
wiredethernetstat = _Wiredethernetstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1)
)
_Lanrecvpacket_Type = Unsigned32
_Lanrecvpacket_Object = MibScalar
lanrecvpacket = _Lanrecvpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 1),
    _Lanrecvpacket_Type()
)
lanrecvpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanrecvpacket.setStatus("current")
_Lantranspacket_Type = Unsigned32
_Lantranspacket_Object = MibScalar
lantranspacket = _Lantranspacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 2),
    _Lantranspacket_Type()
)
lantranspacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lantranspacket.setStatus("current")
_Lanrecvbytes_Type = Unsigned32
_Lanrecvbytes_Object = MibScalar
lanrecvbytes = _Lanrecvbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 3),
    _Lanrecvbytes_Type()
)
lanrecvbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanrecvbytes.setStatus("current")
_Lantransbytes_Type = Unsigned32
_Lantransbytes_Object = MibScalar
lantransbytes = _Lantransbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 1, 4),
    _Lantransbytes_Type()
)
lantransbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lantransbytes.setStatus("current")
_Wirelessstat_ObjectIdentity = ObjectIdentity
wirelessstat = _Wirelessstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2)
)
_Wlanrecvunicastpacket_Type = Unsigned32
_Wlanrecvunicastpacket_Object = MibScalar
wlanrecvunicastpacket = _Wlanrecvunicastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 1),
    _Wlanrecvunicastpacket_Type()
)
wlanrecvunicastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvunicastpacket.setStatus("current")
_Wlantransunicastpacket_Type = Unsigned32
_Wlantransunicastpacket_Object = MibScalar
wlantransunicastpacket = _Wlantransunicastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 2),
    _Wlantransunicastpacket_Type()
)
wlantransunicastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransunicastpacket.setStatus("current")
_Wlanrecvbroadcastpacket_Type = Unsigned32
_Wlanrecvbroadcastpacket_Object = MibScalar
wlanrecvbroadcastpacket = _Wlanrecvbroadcastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 3),
    _Wlanrecvbroadcastpacket_Type()
)
wlanrecvbroadcastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvbroadcastpacket.setStatus("current")
_Wlantransbroadcastpacket_Type = Unsigned32
_Wlantransbroadcastpacket_Object = MibScalar
wlantransbroadcastpacket = _Wlantransbroadcastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 4),
    _Wlantransbroadcastpacket_Type()
)
wlantransbroadcastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransbroadcastpacket.setStatus("current")
_Wlanrecvmulticastpacket_Type = Unsigned32
_Wlanrecvmulticastpacket_Object = MibScalar
wlanrecvmulticastpacket = _Wlanrecvmulticastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 5),
    _Wlanrecvmulticastpacket_Type()
)
wlanrecvmulticastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvmulticastpacket.setStatus("current")
_Wlantransmulticastpacket_Type = Unsigned32
_Wlantransmulticastpacket_Object = MibScalar
wlantransmulticastpacket = _Wlantransmulticastpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 6),
    _Wlantransmulticastpacket_Type()
)
wlantransmulticastpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransmulticastpacket.setStatus("current")
_Wlanrecvpacket_Type = Unsigned32
_Wlanrecvpacket_Object = MibScalar
wlanrecvpacket = _Wlanrecvpacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 7),
    _Wlanrecvpacket_Type()
)
wlanrecvpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvpacket.setStatus("current")
_Wlantranspacket_Type = Unsigned32
_Wlantranspacket_Object = MibScalar
wlantranspacket = _Wlantranspacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 8),
    _Wlantranspacket_Type()
)
wlantranspacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantranspacket.setStatus("current")
_Wlanrecvbytes_Type = Unsigned32
_Wlanrecvbytes_Object = MibScalar
wlanrecvbytes = _Wlanrecvbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 9),
    _Wlanrecvbytes_Type()
)
wlanrecvbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanrecvbytes.setStatus("current")
_Wlantransbytes_Type = Unsigned32
_Wlantransbytes_Object = MibScalar
wlantransbytes = _Wlantransbytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 10),
    _Wlantransbytes_Type()
)
wlantransbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlantransbytes.setStatus("current")
_Stationnumber_Type = Unsigned32
_Stationnumber_Object = MibScalar
stationnumber = _Stationnumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 5, 2, 11),
    _Stationnumber_Type()
)
stationnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationnumber.setStatus("current")
_StationListTable_Object = MibTable
stationListTable = _StationListTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 6)
)
if mibBuilder.loadTexts:
    stationListTable.setStatus("current")
_StationListEntry_Object = MibTableRow
stationListEntry = _StationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1)
)
stationListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    stationListEntry.setStatus("current")
_Macaddress_Type = MacAddress
_Macaddress_Object = MibTableColumn
macaddress = _Macaddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1, 1),
    _Macaddress_Type()
)
macaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macaddress.setStatus("current")
_Ipaddr_Type = IpAddress
_Ipaddr_Object = MibTableColumn
ipaddr = _Ipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1, 2),
    _Ipaddr_Type()
)
ipaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddr.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 6, 1, 3),
    _Stationstatus_Type()
)
stationstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationstatus.setStatus("current")
_Operationapmode_ObjectIdentity = ObjectIdentity
operationapmode = _Operationapmode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7)
)


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
_Apmode_Object = MibScalar
apmode = _Apmode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 1),
    _Apmode_Type()
)
apmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmode.setStatus("current")
_Ptpremotemacaddress_Type = MacAddress
_Ptpremotemacaddress_Object = MibScalar
ptpremotemacaddress = _Ptpremotemacaddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 2),
    _Ptpremotemacaddress_Type()
)
ptpremotemacaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpremotemacaddress.setStatus("current")
_Pxpremotemacaddress1_Type = MacAddress
_Pxpremotemacaddress1_Object = MibScalar
pxpremotemacaddress1 = _Pxpremotemacaddress1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 3),
    _Pxpremotemacaddress1_Type()
)
pxpremotemacaddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress1.setStatus("current")
_Pxpremotemacaddress2_Type = MacAddress
_Pxpremotemacaddress2_Object = MibScalar
pxpremotemacaddress2 = _Pxpremotemacaddress2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 4),
    _Pxpremotemacaddress2_Type()
)
pxpremotemacaddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress2.setStatus("current")
_Pxpremotemacaddress3_Type = MacAddress
_Pxpremotemacaddress3_Object = MibScalar
pxpremotemacaddress3 = _Pxpremotemacaddress3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 5),
    _Pxpremotemacaddress3_Type()
)
pxpremotemacaddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress3.setStatus("current")
_Pxpremotemacaddress4_Type = MacAddress
_Pxpremotemacaddress4_Object = MibScalar
pxpremotemacaddress4 = _Pxpremotemacaddress4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 6),
    _Pxpremotemacaddress4_Type()
)
pxpremotemacaddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxpremotemacaddress4.setStatus("current")
_Repremotemacaddress1_Type = MacAddress
_Repremotemacaddress1_Object = MibScalar
repremotemacaddress1 = _Repremotemacaddress1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 7),
    _Repremotemacaddress1_Type()
)
repremotemacaddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress1.setStatus("current")
_Repremotemacaddress2_Type = MacAddress
_Repremotemacaddress2_Object = MibScalar
repremotemacaddress2 = _Repremotemacaddress2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 8),
    _Repremotemacaddress2_Type()
)
repremotemacaddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress2.setStatus("current")
_Repremotemacaddress3_Type = MacAddress
_Repremotemacaddress3_Object = MibScalar
repremotemacaddress3 = _Repremotemacaddress3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 9),
    _Repremotemacaddress3_Type()
)
repremotemacaddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress3.setStatus("current")
_Repremotemacaddress4_Type = MacAddress
_Repremotemacaddress4_Object = MibScalar
repremotemacaddress4 = _Repremotemacaddress4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 7, 10),
    _Repremotemacaddress4_Type()
)
repremotemacaddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repremotemacaddress4.setStatus("current")
_Info802dot1x_ObjectIdentity = ObjectIdentity
info802dot1x = _Info802dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8)
)
_Authinfo_ObjectIdentity = ObjectIdentity
authinfo = _Authinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1)
)
_Priradipaddr_Type = IpAddress
_Priradipaddr_Object = MibScalar
priradipaddr = _Priradipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 1),
    _Priradipaddr_Type()
)
priradipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priradipaddr.setStatus("current")
_Priradport_Type = Integer32
_Priradport_Object = MibScalar
priradport = _Priradport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 2),
    _Priradport_Type()
)
priradport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priradport.setStatus("current")


class _Priradsharedsecret_Type(DisplayString):
    """Custom type priradsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Priradsharedsecret_Type.__name__ = "DisplayString"
_Priradsharedsecret_Object = MibScalar
priradsharedsecret = _Priradsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 3),
    _Priradsharedsecret_Type()
)
priradsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priradsharedsecret.setStatus("current")
_Sndradipaddr_Type = IpAddress
_Sndradipaddr_Object = MibScalar
sndradipaddr = _Sndradipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 4),
    _Sndradipaddr_Type()
)
sndradipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndradipaddr.setStatus("current")
_Sndradport_Type = Integer32
_Sndradport_Object = MibScalar
sndradport = _Sndradport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 5),
    _Sndradport_Type()
)
sndradport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndradport.setStatus("current")


class _Sndradsharedsecret_Type(DisplayString):
    """Custom type sndradsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sndradsharedsecret_Type.__name__ = "DisplayString"
_Sndradsharedsecret_Object = MibScalar
sndradsharedsecret = _Sndradsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 6),
    _Sndradsharedsecret_Type()
)
sndradsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndradsharedsecret.setStatus("current")
_Reauthtime_Type = Integer32
_Reauthtime_Object = MibScalar
reauthtime = _Reauthtime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 1, 7),
    _Reauthtime_Type()
)
reauthtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reauthtime.setStatus("current")
_Accntinfo_ObjectIdentity = ObjectIdentity
accntinfo = _Accntinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2)
)
_Priacntipaddr_Type = IpAddress
_Priacntipaddr_Object = MibScalar
priacntipaddr = _Priacntipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 1),
    _Priacntipaddr_Type()
)
priacntipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priacntipaddr.setStatus("current")
_Priacntport_Type = Integer32
_Priacntport_Object = MibScalar
priacntport = _Priacntport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 2),
    _Priacntport_Type()
)
priacntport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priacntport.setStatus("current")


class _Priacntsharedsecret_Type(DisplayString):
    """Custom type priacntsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Priacntsharedsecret_Type.__name__ = "DisplayString"
_Priacntsharedsecret_Object = MibScalar
priacntsharedsecret = _Priacntsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 3),
    _Priacntsharedsecret_Type()
)
priacntsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priacntsharedsecret.setStatus("current")
_Sndacntipaddr_Type = IpAddress
_Sndacntipaddr_Object = MibScalar
sndacntipaddr = _Sndacntipaddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 4),
    _Sndacntipaddr_Type()
)
sndacntipaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndacntipaddr.setStatus("current")
_Sndacntport_Type = Integer32
_Sndacntport_Object = MibScalar
sndacntport = _Sndacntport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 5),
    _Sndacntport_Type()
)
sndacntport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndacntport.setStatus("current")


class _Sndacntsharedsecret_Type(DisplayString):
    """Custom type sndacntsharedsecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sndacntsharedsecret_Type.__name__ = "DisplayString"
_Sndacntsharedsecret_Object = MibScalar
sndacntsharedsecret = _Sndacntsharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 8, 2, 6),
    _Sndacntsharedsecret_Type()
)
sndacntsharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndacntsharedsecret.setStatus("current")
_UserCommand_ObjectIdentity = ObjectIdentity
userCommand = _UserCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 9)
)
_ResetAP_Type = Integer32
_ResetAP_Object = MibScalar
resetAP = _ResetAP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 9, 1),
    _ResetAP_Type()
)
resetAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAP.setStatus("current")
_SetWirelessstatus_Type = TruthValue
_SetWirelessstatus_Object = MibScalar
setWirelessstatus = _SetWirelessstatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 9, 2),
    _SetWirelessstatus_Type()
)
setWirelessstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWirelessstatus.setStatus("current")
_TimeSettings_ObjectIdentity = ObjectIdentity
timeSettings = _TimeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 10, 1),
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
              74)
        )
    )
    namedValues = NamedValues(
        *(("gmt00-casablanca-monrovia", 25),
          ("gmt00-greenwich-mean-time-dublin-edinburgh-lisbon-London", 26),
          ("gmteast01-amsterdam-berlin-bern-rome-stockholm-vienna", 27),
          ("gmteast01-belgrade-bratislava-budapest-ljubljana-prague", 28),
          ("gmteast01-brussels-copenhagen-madrid-paris", 29),
          ("gmteast01-sarajevo-skopje-warsaw-zagreb", 30),
          ("gmteast01-west-central-africa", 31),
          ("gmteast02-athens-istanbul-minsk", 32),
          ("gmteast02-bucharest", 33),
          ("gmteast02-cairo", 34),
          ("gmteast02-harare-pretoria", 35),
          ("gmteast02-helsinki-kyiv-riga-sofia-tallinn-vilnius", 36),
          ("gmteast02-jerusalem", 37),
          ("gmteast03-baghdad", 38),
          ("gmteast03-kuwait-riyadh", 39),
          ("gmteast03-moscow-st-petersburg-volgograd", 40),
          ("gmteast03-nairobi", 41),
          ("gmteast03-tehran", 42),
          ("gmteast04-abu-dhabi-muscat", 43),
          ("gmteast04-baku-tbilisi-yerevan", 44),
          ("gmteast04-kabul", 45),
          ("gmteast05-chennai-kolkata-mumbai-new-delhi", 48),
          ("gmteast05-ekaterinburg", 46),
          ("gmteast05-islamabad-karachi-kashkent", 47),
          ("gmteast05-kathmandu", 49),
          ("gmteast06-almaty-novosibirsk", 50),
          ("gmteast06-astana-dhaka", 51),
          ("gmteast06-rangoon", 53),
          ("gmteast06-sri-jayawardenepura", 52),
          ("gmteast07-bangkok-hanoi-jakarta", 54),
          ("gmteast07-krasnoyarsk", 55),
          ("gmteast08-beijing-chongqing-hong-kong-urumqi", 56),
          ("gmteast08-irkutsk-ulaan-bataar", 57),
          ("gmteast08-kuala-lumpur-singapore", 58),
          ("gmteast08-perth", 59),
          ("gmteast08-taipei", 60),
          ("gmteast09-adelaide", 64),
          ("gmteast09-darwin", 65),
          ("gmteast09-osaka-sapporo-tokyo", 61),
          ("gmteast09-seoul", 62),
          ("gmteast09-yakutsk", 63),
          ("gmteast10-brisbane", 66),
          ("gmteast10-canberra-melbourne-sydney", 67),
          ("gmteast10-guam-port-moresby", 68),
          ("gmteast10-hobart", 69),
          ("gmteast10-vladivostok", 70),
          ("gmteast11-magadan-solomon-is-new-caledonia", 71),
          ("gmteast12-auckland-wellington", 72),
          ("gmteast12-fiji-kamchatka-marshall-is", 73),
          ("gmteast13-nuku-alofa", 74),
          ("gmtwest01-azores", 23),
          ("gmtwest01-cape-verde-is", 24),
          ("gmtwest02-mid-atlantic", 22),
          ("gmtwest03-30-newfoundland", 18),
          ("gmtwest03-brasilia", 19),
          ("gmtwest03-buenos-aires-georgetown", 20),
          ("gmtwest03-greenland", 21),
          ("gmtwest04-atlantic-Time-canada", 15),
          ("gmtwest04-caracas-la-paz", 16),
          ("gmtwest04-santiago", 17),
          ("gmtwest05-bogota-lima-quito", 12),
          ("gmtwest05-eastern-time-us-canada", 13),
          ("gmtwest05-indiana-east", 14),
          ("gmtwest06-central-america", 8),
          ("gmtwest06-central-time-us-canada", 9),
          ("gmtwest06-guadalajara-mexico-city-monterrey", 10),
          ("gmtwest06-saskatchewan", 11),
          ("gmtwest07-arizona", 5),
          ("gmtwest07-chihuahua-la-paz-mazatlan", 6),
          ("gmtwest07-mountain-time-us-canada", 7),
          ("gmtwest08-pacific-time-us-canada-tijuana", 4),
          ("gmtwest09-alaska", 3),
          ("gmtwest10-hawaii", 2),
          ("gmtwest11-midway-island-samoa", 1),
          ("gmtwest12-international-date-line-west", 0))
    )


_Timezone_Type.__name__ = "Integer32"
_Timezone_Object = MibScalar
timezone = _Timezone_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 10, 2),
    _Timezone_Type()
)
timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timezone.setStatus("current")
_Daylightsaving_Type = TruthValue
_Daylightsaving_Object = MibScalar
daylightsaving = _Daylightsaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 10, 3),
    _Daylightsaving_Type()
)
daylightsaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightsaving.setStatus("current")
_DhcpsSettings_ObjectIdentity = ObjectIdentity
dhcpsSettings = _DhcpsSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11)
)
_Dhcpserver_Type = TruthValue
_Dhcpserver_Object = MibScalar
dhcpserver = _Dhcpserver_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 1),
    _Dhcpserver_Type()
)
dhcpserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpserver.setStatus("current")
_Dhcpsipstart_Type = IpAddress
_Dhcpsipstart_Object = MibScalar
dhcpsipstart = _Dhcpsipstart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 2),
    _Dhcpsipstart_Type()
)
dhcpsipstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsipstart.setStatus("current")
_Dhcpsipend_Type = IpAddress
_Dhcpsipend_Object = MibScalar
dhcpsipend = _Dhcpsipend_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 3),
    _Dhcpsipend_Type()
)
dhcpsipend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsipend.setStatus("current")
_Dhcpnetmask_Type = IpAddress
_Dhcpnetmask_Object = MibScalar
dhcpnetmask = _Dhcpnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 4),
    _Dhcpnetmask_Type()
)
dhcpnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpnetmask.setStatus("current")
_Dhcpsgateway_Type = IpAddress
_Dhcpsgateway_Object = MibScalar
dhcpsgateway = _Dhcpsgateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 5),
    _Dhcpsgateway_Type()
)
dhcpsgateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsgateway.setStatus("current")
_Dhcpspridns_Type = IpAddress
_Dhcpspridns_Object = MibScalar
dhcpspridns = _Dhcpspridns_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 6),
    _Dhcpspridns_Type()
)
dhcpspridns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspridns.setStatus("current")
_Dhcpspsnddns_Type = IpAddress
_Dhcpspsnddns_Object = MibScalar
dhcpspsnddns = _Dhcpspsnddns_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 7),
    _Dhcpspsnddns_Type()
)
dhcpspsnddns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspsnddns.setStatus("current")
_Dhcpspriwins_Type = IpAddress
_Dhcpspriwins_Object = MibScalar
dhcpspriwins = _Dhcpspriwins_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 8),
    _Dhcpspriwins_Type()
)
dhcpspriwins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpspriwins.setStatus("current")
_Dhcpspsndwins_Type = IpAddress
_Dhcpspsndwins_Object = MibScalar
dhcpspsndwins = _Dhcpspsndwins_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 9),
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
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 10),
    _Dhcpsleasetime_Type()
)
dhcpsleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsleasetime.setStatus("current")
_Anyip_Type = TruthValue
_Anyip_Object = MibScalar
anyip = _Anyip_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 11, 11),
    _Anyip_Type()
)
anyip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anyip.setStatus("current")
_LogSettings_ObjectIdentity = ObjectIdentity
logSettings = _LogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 12)
)
_Syslog_Type = TruthValue
_Syslog_Object = MibScalar
syslog = _Syslog_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 12, 1),
    _Syslog_Type()
)
syslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslog.setStatus("current")
_Syslogsrvip_Type = IpAddress
_Syslogsrvip_Object = MibScalar
syslogsrvip = _Syslogsrvip_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 12, 2),
    _Syslogsrvip_Type()
)
syslogsrvip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogsrvip.setStatus("current")
_Syslogsrvport_Type = Integer32
_Syslogsrvport_Object = MibScalar
syslogsrvport = _Syslogsrvport_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2, 12, 3),
    _Syslogsrvport_Type()
)
syslogsrvport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogsrvport.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WG302-MIB",
    **{"netgear": netgear,
       "wireless": wireless,
       "accesspoint": accesspoint,
       "lanSettings": lanSettings,
       "apName": apName,
       "adminName": adminName,
       "adminPasswd": adminPasswd,
       "dhcpStatus": dhcpStatus,
       "ipAddr": ipAddr,
       "netmaskAddr": netmaskAddr,
       "gatewayAddr": gatewayAddr,
       "spantree": spantree,
       "pridnsipAddr": pridnsipAddr,
       "snddnsipAddr": snddnsipAddr,
       "wlanSettingTable": wlanSettingTable,
       "wlanSettingEntry": wlanSettingEntry,
       "operatemode": operatemode,
       "ssid": ssid,
       "countrycode": countrycode,
       "channel": channel,
       "datarate": datarate,
       "beaconinterval": beaconinterval,
       "rtsthreshold": rtsthreshold,
       "fraglength": fraglength,
       "dtiminterval": dtiminterval,
       "preambletype": preambletype,
       "hidenetworkname": hidenetworkname,
       "txpower": txpower,
       "superG": superG,
       "antenna": antenna,
       "securityTable": securityTable,
       "securityEntry": securityEntry,
       "authenticationtype": authenticationtype,
       "encryption": encryption,
       "encryptionstrength": encryptionstrength,
       "keyno": keyno,
       "key1": key1,
       "key2": key2,
       "key3": key3,
       "key4": key4,
       "wlanseparator": wlanseparator,
       "presharekey": presharekey,
       "remoteSettings": remoteSettings,
       "sshd": sshd,
       "snmpenable": snmpenable,
       "trapServerIP": trapServerIP,
       "readOnlyCommunity": readOnlyCommunity,
       "readWriteCommunity": readWriteCommunity,
       "statistic": statistic,
       "wiredethernetstat": wiredethernetstat,
       "lanrecvpacket": lanrecvpacket,
       "lantranspacket": lantranspacket,
       "lanrecvbytes": lanrecvbytes,
       "lantransbytes": lantransbytes,
       "wirelessstat": wirelessstat,
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
       "stationnumber": stationnumber,
       "stationListTable": stationListTable,
       "stationListEntry": stationListEntry,
       "macaddress": macaddress,
       "ipaddr": ipaddr,
       "stationstatus": stationstatus,
       "operationapmode": operationapmode,
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
       "info802dot1x": info802dot1x,
       "authinfo": authinfo,
       "priradipaddr": priradipaddr,
       "priradport": priradport,
       "priradsharedsecret": priradsharedsecret,
       "sndradipaddr": sndradipaddr,
       "sndradport": sndradport,
       "sndradsharedsecret": sndradsharedsecret,
       "reauthtime": reauthtime,
       "accntinfo": accntinfo,
       "priacntipaddr": priacntipaddr,
       "priacntport": priacntport,
       "priacntsharedsecret": priacntsharedsecret,
       "sndacntipaddr": sndacntipaddr,
       "sndacntport": sndacntport,
       "sndacntsharedsecret": sndacntsharedsecret,
       "userCommand": userCommand,
       "resetAP": resetAP,
       "setWirelessstatus": setWirelessstatus,
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
       "anyip": anyip,
       "logSettings": logSettings,
       "syslog": syslog,
       "syslogsrvip": syslogsrvip,
       "syslogsrvport": syslogsrvport}
)
