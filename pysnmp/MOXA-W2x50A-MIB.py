# SNMP MIB module (MOXA-W2x50A-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOXA-W2x50A-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:42 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

w2x50A = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_Nport_ObjectIdentity = ObjectIdentity
nport = _Nport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2)
)
_SwMgmt_ObjectIdentity = ObjectIdentity
swMgmt = _SwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1)
)
_Overview_ObjectIdentity = ObjectIdentity
overview = _Overview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1)
)
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 1),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_SerialNumber_Type = Integer32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 3),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_EthIPAddress_Type = DisplayString
_EthIPAddress_Object = MibScalar
ethIPAddress = _EthIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 4),
    _EthIPAddress_Type()
)
ethIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIPAddress.setStatus("current")
_EthMacAddress_Type = MacAddress
_EthMacAddress_Object = MibScalar
ethMacAddress = _EthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 5),
    _EthMacAddress_Type()
)
ethMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethMacAddress.setStatus("current")
_WlanIPAddress_Type = DisplayString
_WlanIPAddress_Object = MibScalar
wlanIPAddress = _WlanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 6),
    _WlanIPAddress_Type()
)
wlanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIPAddress.setStatus("current")
_WlanMacAddress_Type = MacAddress
_WlanMacAddress_Object = MibScalar
wlanMacAddress = _WlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 7),
    _WlanMacAddress_Type()
)
wlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMacAddress.setStatus("current")
_WlanSSID_Type = DisplayString
_WlanSSID_Object = MibScalar
wlanSSID = _WlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 8),
    _WlanSSID_Type()
)
wlanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSID.setStatus("current")
_WlanNetworkType_Type = DisplayString
_WlanNetworkType_Object = MibScalar
wlanNetworkType = _WlanNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 9),
    _WlanNetworkType_Type()
)
wlanNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanNetworkType.setStatus("current")
_WlanSecurityMode_Type = DisplayString
_WlanSecurityMode_Object = MibScalar
wlanSecurityMode = _WlanSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 10),
    _WlanSecurityMode_Type()
)
wlanSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSecurityMode.setStatus("current")
_WlanRFType_Type = DisplayString
_WlanRFType_Object = MibScalar
wlanRFType = _WlanRFType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 11),
    _WlanRFType_Type()
)
wlanRFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRFType.setStatus("current")
_WlanCountryCode_Type = DisplayString
_WlanCountryCode_Object = MibScalar
wlanCountryCode = _WlanCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 12),
    _WlanCountryCode_Type()
)
wlanCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCountryCode.setStatus("current")
_WlanFastRoaming_Type = DisplayString
_WlanFastRoaming_Object = MibScalar
wlanFastRoaming = _WlanFastRoaming_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 13),
    _WlanFastRoaming_Type()
)
wlanFastRoaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFastRoaming.setStatus("current")
_ActiveNetworkPort_Type = DisplayString
_ActiveNetworkPort_Object = MibScalar
activeNetworkPort = _ActiveNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 14),
    _ActiveNetworkPort_Type()
)
activeNetworkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNetworkPort.setStatus("current")
_UpTime_Type = DisplayString
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 15),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_SerialPort1_Type = DisplayString
_SerialPort1_Object = MibScalar
serialPort1 = _SerialPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 16),
    _SerialPort1_Type()
)
serialPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPort1.setStatus("current")
_SerialPort2_Type = DisplayString
_SerialPort2_Object = MibScalar
serialPort2 = _SerialPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 1, 17),
    _SerialPort2_Type()
)
serialPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPort2.setStatus("current")
_BasicSetting_ObjectIdentity = ObjectIdentity
basicSetting = _BasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2)
)
_ServerSetting_ObjectIdentity = ObjectIdentity
serverSetting = _ServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 1)
)
_ServerName_Type = DisplayString
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverName.setStatus("current")
_ServerLocation_Type = DisplayString
_ServerLocation_Object = MibScalar
serverLocation = _ServerLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 1, 2),
    _ServerLocation_Type()
)
serverLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverLocation.setStatus("current")
_TimeSetting_ObjectIdentity = ObjectIdentity
timeSetting = _TimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 2)
)


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("GMT-0100_Azores-Cape-Verde-Is", 21),
          ("GMT-0200_Mid-Atlantic", 20),
          ("GMT-0300_Brasilia", 18),
          ("GMT-0300_Buenos-Aires", 19),
          ("GMT-0330_Newfoundland", 17),
          ("GMT-0400_Atlantic-Time-Canada", 14),
          ("GMT-0400_Georgetown-La-Paz", 15),
          ("GMT-0400_Santiago", 16),
          ("GMT-0430_Caracas", 13),
          ("GMT-0500_Bogota-Lima-Quito", 10),
          ("GMT-0500_Eastern-Time-US_Canada", 11),
          ("GMT-0500_Indiana-East", 12),
          ("GMT-0600_Central-Time-US_Canada", 7),
          ("GMT-0600_Mexico-City-Tegucigalpa", 8),
          ("GMT-0600_Saskatchewan", 9),
          ("GMT-0700_Arizona", 5),
          ("GMT-0700_Mountain-Time-US_Canada", 6),
          ("GMT-0800_Pacific-Time-US_Canada-Tijuana", 4),
          ("GMT-0900_Alaska", 3),
          ("GMT-1000_Hawaii", 2),
          ("GMT-1100_Midway-Island-Samoa", 1),
          ("GMT-1200_Eniwetok-Kwajalein", 0),
          ("GMT_0100_Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 24),
          ("GMT_0100_Belgrade-Bratislava-Budapest-Ljubljana-Prague", 25),
          ("GMT_0100_Brussels-Copenhagen-Madrid-Paris-Vilnius", 26),
          ("GMT_0100_Sarajevo-Skopje-Warsaw-Zagreb", 27),
          ("GMT_0200_Athens-Istanbul-Minsk", 28),
          ("GMT_0200_Bucharest", 29),
          ("GMT_0200_Cairo", 30),
          ("GMT_0200_Harare-Pretoria", 31),
          ("GMT_0200_Helsinki-Riga-Sofia-Tallinn", 32),
          ("GMT_0200_Jerusalem", 33),
          ("GMT_0300_Baghdad-Kuwait-Riyadh", 34),
          ("GMT_0300_Mairobi", 36),
          ("GMT_0300_Moscow-St-Petersburg-Volgograd", 35),
          ("GMT_0330_Tehran", 37),
          ("GMT_0400_Abu-Dhabi-Muscat", 38),
          ("GMT_0400_Baku-Tbilisi", 39),
          ("GMT_0430_Kabul", 40),
          ("GMT_0500_Ekaterinburg", 41),
          ("GMT_0500_Islamabad-Karachi-Tashkent", 42),
          ("GMT_0530_Bombay-Calcutta-Madras-New-Delhi", 43),
          ("GMT_0600_Astana-Almaty-Dhaka", 44),
          ("GMT_0600_Colombo", 45),
          ("GMT_0700_Bangkok-Hanoi-Jakarta", 46),
          ("GMT_0800_Beijing-Chongqing-Hong-Kong-Urumqi", 47),
          ("GMT_0800_Perth", 48),
          ("GMT_0800_Singapore", 49),
          ("GMT_0800_Taipei", 50),
          ("GMT_0900_Osaka-Sapporo-Tokyo", 51),
          ("GMT_0900_Seoul", 52),
          ("GMT_0900_Yakutsk", 53),
          ("GMT_0930_Adelaide", 54),
          ("GMT_0930_Darwin", 55),
          ("GMT_1000_Brisbane", 56),
          ("GMT_1000_Canberra-Melbourne-Sydney", 57),
          ("GMT_1000_Guam-Port-Moresby", 58),
          ("GMT_1000_Hobart", 59),
          ("GMT_1000_Vladivostok", 60),
          ("GMT_1100_Magadan-Solomon-Is-New-Caledonia", 61),
          ("GMT_1200_Auckland-Wllington", 62),
          ("GMT_1200_Fiji-Kamchatka-Marshall-Is", 63),
          ("GMT_Casabanca-Monrovia", 22),
          ("GMT_Greenich-Mean-Time_Dublin-Edinburgh-Lisbon-London", 23))
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 2, 1),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _LocalTime_Type(DisplayString):
    """Custom type localTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_LocalTime_Type.__name__ = "DisplayString"
_LocalTime_Object = MibScalar
localTime = _LocalTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 2, 2),
    _LocalTime_Type()
)
localTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTime.setStatus("current")
_TimeServer_Type = DisplayString
_TimeServer_Object = MibScalar
timeServer = _TimeServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 2, 2, 3),
    _TimeServer_Type()
)
timeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3)
)
_GeneralSetting_ObjectIdentity = ObjectIdentity
generalSetting = _GeneralSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 1)
)
_DnsServer1IpAddr_Type = IpAddress
_DnsServer1IpAddr_Object = MibScalar
dnsServer1IpAddr = _DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 1, 1),
    _DnsServer1IpAddr_Type()
)
dnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1IpAddr.setStatus("current")
_DnsServer2IpAddr_Type = IpAddress
_DnsServer2IpAddr_Object = MibScalar
dnsServer2IpAddr = _DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 1, 2),
    _DnsServer2IpAddr_Type()
)
dnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2IpAddr.setStatus("current")
_EthernetSetting_ObjectIdentity = ObjectIdentity
ethernetSetting = _EthernetSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 2)
)


class _EthIpConfiguration_Type(Integer32):
    """Custom type ethIpConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 1),
          ("static", 0))
    )


_EthIpConfiguration_Type.__name__ = "Integer32"
_EthIpConfiguration_Object = MibScalar
ethIpConfiguration = _EthIpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 2, 1),
    _EthIpConfiguration_Type()
)
ethIpConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIpConfiguration.setStatus("current")
_EthIpAddress_Type = IpAddress
_EthIpAddress_Object = MibScalar
ethIpAddress = _EthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 2, 2),
    _EthIpAddress_Type()
)
ethIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIpAddress.setStatus("current")
_EthNetMask_Type = IpAddress
_EthNetMask_Object = MibScalar
ethNetMask = _EthNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 2, 3),
    _EthNetMask_Type()
)
ethNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethNetMask.setStatus("current")
_EthDefaultGateway_Type = IpAddress
_EthDefaultGateway_Object = MibScalar
ethDefaultGateway = _EthDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 2, 4),
    _EthDefaultGateway_Type()
)
ethDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDefaultGateway.setStatus("current")


class _EthBridgeMode_Type(Integer32):
    """Custom type ethBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EthBridgeMode_Type.__name__ = "Integer32"
_EthBridgeMode_Object = MibScalar
ethBridgeMode = _EthBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 2, 5),
    _EthBridgeMode_Type()
)
ethBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBridgeMode.setStatus("current")
_WlanSetting_ObjectIdentity = ObjectIdentity
wlanSetting = _WlanSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 3)
)


class _WlanIpConfiguration_Type(Integer32):
    """Custom type wlanIpConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 1),
          ("static", 0))
    )


_WlanIpConfiguration_Type.__name__ = "Integer32"
_WlanIpConfiguration_Object = MibScalar
wlanIpConfiguration = _WlanIpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 3, 1),
    _WlanIpConfiguration_Type()
)
wlanIpConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIpConfiguration.setStatus("current")
_WlanIpAddress_Type = IpAddress
_WlanIpAddress_Object = MibScalar
wlanIpAddress = _WlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 3, 2),
    _WlanIpAddress_Type()
)
wlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIpAddress.setStatus("current")
_WlanNetMask_Type = IpAddress
_WlanNetMask_Object = MibScalar
wlanNetMask = _WlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 3, 3),
    _WlanNetMask_Type()
)
wlanNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanNetMask.setStatus("current")
_WlanDefaultGateway_Type = IpAddress
_WlanDefaultGateway_Object = MibScalar
wlanDefaultGateway = _WlanDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 3, 4),
    _WlanDefaultGateway_Type()
)
wlanDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDefaultGateway.setStatus("current")
_ProfileSetting_ObjectIdentity = ObjectIdentity
profileSetting = _ProfileSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4)
)


class _NetworkType_Type(Integer32):
    """Custom type networkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ad-hoc", 0),
          ("infrastructure", 1))
    )


_NetworkType_Type.__name__ = "Integer32"
_NetworkType_Object = MibScalar
networkType = _NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 1),
    _NetworkType_Type()
)
networkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkType.setStatus("current")
_AdhocProfile_ObjectIdentity = ObjectIdentity
adhocProfile = _AdhocProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2)
)
_AdhocGeneralSetting_ObjectIdentity = ObjectIdentity
adhocGeneralSetting = _AdhocGeneralSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 1)
)


class _AdhocProfileName_Type(DisplayString):
    """Custom type adhocProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdhocProfileName_Type.__name__ = "DisplayString"
_AdhocProfileName_Object = MibScalar
adhocProfileName = _AdhocProfileName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 1, 1),
    _AdhocProfileName_Type()
)
adhocProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocProfileName.setStatus("current")


class _AdhocRFType_Type(Integer32):
    """Custom type adhocRFType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("w802_11b_g", 2)
    )


_AdhocRFType_Type.__name__ = "Integer32"
_AdhocRFType_Object = MibScalar
adhocRFType = _AdhocRFType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 1, 2),
    _AdhocRFType_Type()
)
adhocRFType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocRFType.setStatus("current")


class _AdhocWlanSSID_Type(DisplayString):
    """Custom type adhocWlanSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdhocWlanSSID_Type.__name__ = "DisplayString"
_AdhocWlanSSID_Object = MibScalar
adhocWlanSSID = _AdhocWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 1, 3),
    _AdhocWlanSSID_Type()
)
adhocWlanSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocWlanSSID.setStatus("current")
_AdhocChannel_Type = Integer32
_AdhocChannel_Object = MibScalar
adhocChannel = _AdhocChannel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 1, 4),
    _AdhocChannel_Type()
)
adhocChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocChannel.setStatus("current")
_AdhocSecuritySetting_ObjectIdentity = ObjectIdentity
adhocSecuritySetting = _AdhocSecuritySetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2)
)


class _AdhocAuthentication_Type(Integer32):
    """Custom type adhocAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("open-system", 0)
    )


_AdhocAuthentication_Type.__name__ = "Integer32"
_AdhocAuthentication_Object = MibScalar
adhocAuthentication = _AdhocAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2, 1),
    _AdhocAuthentication_Type()
)
adhocAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adhocAuthentication.setStatus("current")


class _AdhocEncryption_Type(Integer32):
    """Custom type adhocEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("wep", 1))
    )


_AdhocEncryption_Type.__name__ = "Integer32"
_AdhocEncryption_Object = MibScalar
adhocEncryption = _AdhocEncryption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2, 2),
    _AdhocEncryption_Type()
)
adhocEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocEncryption.setStatus("current")


class _AdhocWepKeyLength_Type(Integer32):
    """Custom type adhocWepKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("key-128-bits", 1),
          ("key-64-bits", 0))
    )


_AdhocWepKeyLength_Type.__name__ = "Integer32"
_AdhocWepKeyLength_Object = MibScalar
adhocWepKeyLength = _AdhocWepKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2, 3),
    _AdhocWepKeyLength_Type()
)
adhocWepKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocWepKeyLength.setStatus("current")


class _AdhocWepKeyIndex_Type(Integer32):
    """Custom type adhocWepKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdhocWepKeyIndex_Type.__name__ = "Integer32"
_AdhocWepKeyIndex_Object = MibScalar
adhocWepKeyIndex = _AdhocWepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2, 4),
    _AdhocWepKeyIndex_Type()
)
adhocWepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocWepKeyIndex.setStatus("current")


class _AdhocWepKeyPassphrase_Type(DisplayString):
    """Custom type adhocWepKeyPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdhocWepKeyPassphrase_Type.__name__ = "DisplayString"
_AdhocWepKeyPassphrase_Object = MibScalar
adhocWepKeyPassphrase = _AdhocWepKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2, 5),
    _AdhocWepKeyPassphrase_Type()
)
adhocWepKeyPassphrase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adhocWepKeyPassphrase.setStatus("current")


class _AdhocWepKeyFormat_Type(Integer32):
    """Custom type adhocWepKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1))
    )


_AdhocWepKeyFormat_Type.__name__ = "Integer32"
_AdhocWepKeyFormat_Object = MibScalar
adhocWepKeyFormat = _AdhocWepKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 2, 2, 6),
    _AdhocWepKeyFormat_Type()
)
adhocWepKeyFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adhocWepKeyFormat.setStatus("current")
_InfrastructureProfile_ObjectIdentity = ObjectIdentity
infrastructureProfile = _InfrastructureProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3)
)
_InfraGeneralSetting_ObjectIdentity = ObjectIdentity
infraGeneralSetting = _InfraGeneralSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1)
)
_InfraGeneralSettingTable_Object = MibTable
infraGeneralSettingTable = _InfraGeneralSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    infraGeneralSettingTable.setStatus("current")
_InfraGeneralSettingEntry_Object = MibTableRow
infraGeneralSettingEntry = _InfraGeneralSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1, 1, 1)
)
infraGeneralSettingEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "profileIndex"),
)
if mibBuilder.loadTexts:
    infraGeneralSettingEntry.setStatus("current")


class _ProfileIndex_Type(Integer32):
    """Custom type profileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("profile1", 1)
    )


_ProfileIndex_Type.__name__ = "Integer32"
_ProfileIndex_Object = MibTableColumn
profileIndex = _ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1, 1, 1, 1),
    _ProfileIndex_Type()
)
profileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileIndex.setStatus("current")


class _ProfileName_Type(DisplayString):
    """Custom type profileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProfileName_Type.__name__ = "DisplayString"
_ProfileName_Object = MibTableColumn
profileName = _ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1, 1, 1, 2),
    _ProfileName_Type()
)
profileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileName.setStatus("current")


class _ProfileRFType_Type(Integer32):
    """Custom type profileRFType based on Integer32"""
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
        *(("auto", 0),
          ("w802_11a", 1),
          ("w802_11a_n", 3),
          ("w802_11b_g", 2),
          ("w802_11b_g_n", 4))
    )


_ProfileRFType_Type.__name__ = "Integer32"
_ProfileRFType_Object = MibTableColumn
profileRFType = _ProfileRFType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1, 1, 1, 3),
    _ProfileRFType_Type()
)
profileRFType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileRFType.setStatus("current")


class _ProfileWlanSSID_Type(DisplayString):
    """Custom type profileWlanSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProfileWlanSSID_Type.__name__ = "DisplayString"
_ProfileWlanSSID_Object = MibTableColumn
profileWlanSSID = _ProfileWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 1, 1, 1, 4),
    _ProfileWlanSSID_Type()
)
profileWlanSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileWlanSSID.setStatus("current")
_SecuritySetting_ObjectIdentity = ObjectIdentity
securitySetting = _SecuritySetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2)
)
_SecuritySettingTable_Object = MibTable
securitySettingTable = _SecuritySettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    securitySettingTable.setStatus("current")
_SecuritySettingEntry_Object = MibTableRow
securitySettingEntry = _SecuritySettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1)
)
securitySettingEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "profileIndex"),
)
if mibBuilder.loadTexts:
    securitySettingEntry.setStatus("current")


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
              5)
        )
    )
    namedValues = NamedValues(
        *(("open-system", 0),
          ("shared-key", 1),
          ("wpa", 2),
          ("wpa-psk", 3),
          ("wpa2", 4),
          ("wpa2-psk", 5))
    )


_Authentication_Type.__name__ = "Integer32"
_Authentication_Object = MibTableColumn
authentication = _Authentication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 1),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes-ccmp", 3),
          ("disable", 0),
          ("tkip", 2),
          ("wep", 1))
    )


_Encryption_Type.__name__ = "Integer32"
_Encryption_Object = MibTableColumn
encryption = _Encryption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 2),
    _Encryption_Type()
)
encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption.setStatus("current")


class _WepKeyLength_Type(Integer32):
    """Custom type wepKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("key-128-bits", 1),
          ("key-64-bits", 0))
    )


_WepKeyLength_Type.__name__ = "Integer32"
_WepKeyLength_Object = MibTableColumn
wepKeyLength = _WepKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 3),
    _WepKeyLength_Type()
)
wepKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKeyLength.setStatus("current")


class _WepKeyIndex_Type(Integer32):
    """Custom type wepKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WepKeyIndex_Type.__name__ = "Integer32"
_WepKeyIndex_Object = MibTableColumn
wepKeyIndex = _WepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 4),
    _WepKeyIndex_Type()
)
wepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKeyIndex.setStatus("current")


class _WepKeyPassphrase_Type(DisplayString):
    """Custom type wepKeyPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_WepKeyPassphrase_Type.__name__ = "DisplayString"
_WepKeyPassphrase_Object = MibTableColumn
wepKeyPassphrase = _WepKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 5),
    _WepKeyPassphrase_Type()
)
wepKeyPassphrase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wepKeyPassphrase.setStatus("current")


class _WepKeyFormat_Type(Integer32):
    """Custom type wepKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1))
    )


_WepKeyFormat_Type.__name__ = "Integer32"
_WepKeyFormat_Object = MibTableColumn
wepKeyFormat = _WepKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 6),
    _WepKeyFormat_Type()
)
wepKeyFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wepKeyFormat.setStatus("current")


class _EapMethod_Type(Integer32):
    """Custom type eapMethod based on Integer32"""
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
        *(("leap", 3),
          ("peap", 1),
          ("tls", 0),
          ("ttls", 2))
    )


_EapMethod_Type.__name__ = "Integer32"
_EapMethod_Object = MibTableColumn
eapMethod = _EapMethod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 12),
    _EapMethod_Type()
)
eapMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapMethod.setStatus("current")


class _TunneledAuth_Type(Integer32):
    """Custom type tunneledAuth based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("eap-gtc", 9),
          ("eap-md5", 10),
          ("eap-mschapv2", 8),
          ("eap-tls", 7),
          ("gtc", 0),
          ("md5", 1),
          ("mschap", 4),
          ("mschapv2", 5),
          ("pap", 2),
          ("tls", 6))
    )


_TunneledAuth_Type.__name__ = "Integer32"
_TunneledAuth_Object = MibTableColumn
tunneledAuth = _TunneledAuth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 13),
    _TunneledAuth_Type()
)
tunneledAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunneledAuth.setStatus("current")


class _WpaUsername_Type(DisplayString):
    """Custom type wpaUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_WpaUsername_Type.__name__ = "DisplayString"
_WpaUsername_Object = MibTableColumn
wpaUsername = _WpaUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 14),
    _WpaUsername_Type()
)
wpaUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wpaUsername.setStatus("current")


class _WpaAnonymousUsername_Type(DisplayString):
    """Custom type wpaAnonymousUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_WpaAnonymousUsername_Type.__name__ = "DisplayString"
_WpaAnonymousUsername_Object = MibTableColumn
wpaAnonymousUsername = _WpaAnonymousUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 16),
    _WpaAnonymousUsername_Type()
)
wpaAnonymousUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wpaAnonymousUsername.setStatus("current")


class _VerifyServerCert_Type(Integer32):
    """Custom type verifyServerCert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VerifyServerCert_Type.__name__ = "Integer32"
_VerifyServerCert_Object = MibTableColumn
verifyServerCert = _VerifyServerCert_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 17),
    _VerifyServerCert_Type()
)
verifyServerCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyServerCert.setStatus("current")


class _TrustedServerCert_Type(Integer32):
    """Custom type trustedServerCert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_TrustedServerCert_Type.__name__ = "Integer32"
_TrustedServerCert_Object = MibTableColumn
trustedServerCert = _TrustedServerCert_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 18),
    _TrustedServerCert_Type()
)
trustedServerCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedServerCert.setStatus("current")


class _UserCert_Type(Integer32):
    """Custom type userCert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_UserCert_Type.__name__ = "Integer32"
_UserCert_Object = MibTableColumn
userCert = _UserCert_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 19),
    _UserCert_Type()
)
userCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCert.setStatus("current")


class _UserPrivateKey_Type(Integer32):
    """Custom type userPrivateKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_UserPrivateKey_Type.__name__ = "Integer32"
_UserPrivateKey_Object = MibTableColumn
userPrivateKey = _UserPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 2, 1, 1, 20),
    _UserPrivateKey_Type()
)
userPrivateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPrivateKey.setStatus("current")


class _FastRoamingSetting_Type(Integer32):
    """Custom type fastRoamingSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FastRoamingSetting_Type.__name__ = "Integer32"
_FastRoamingSetting_Object = MibScalar
fastRoamingSetting = _FastRoamingSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 3),
    _FastRoamingSetting_Type()
)
fastRoamingSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRoamingSetting.setStatus("current")


class _FastRoamingScanChannels1_Type(Integer32):
    """Custom type fastRoamingScanChannels1 based on Integer32"""
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("channel_1", 1),
          ("channel_10", 10),
          ("channel_100", 23),
          ("channel_104", 24),
          ("channel_108", 25),
          ("channel_11", 11),
          ("channel_112", 26),
          ("channel_116", 27),
          ("channel_12", 12),
          ("channel_120", 28),
          ("channel_124", 29),
          ("channel_128", 30),
          ("channel_13", 13),
          ("channel_132", 31),
          ("channel_136", 32),
          ("channel_140", 33),
          ("channel_149", 34),
          ("channel_153", 35),
          ("channel_157", 36),
          ("channel_161", 37),
          ("channel_165", 38),
          ("channel_2", 2),
          ("channel_3", 3),
          ("channel_36", 15),
          ("channel_4", 4),
          ("channel_40", 16),
          ("channel_44", 17),
          ("channel_48", 18),
          ("channel_5", 5),
          ("channel_52", 19),
          ("channel_56", 20),
          ("channel_6", 6),
          ("channel_60", 21),
          ("channel_64", 22),
          ("channel_7", 7),
          ("channel_8", 8),
          ("channel_9", 9),
          ("n_a", 0))
    )


_FastRoamingScanChannels1_Type.__name__ = "Integer32"
_FastRoamingScanChannels1_Object = MibScalar
fastRoamingScanChannels1 = _FastRoamingScanChannels1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 4),
    _FastRoamingScanChannels1_Type()
)
fastRoamingScanChannels1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRoamingScanChannels1.setStatus("current")


class _FastRoamingScanChannels2_Type(Integer32):
    """Custom type fastRoamingScanChannels2 based on Integer32"""
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("channel_1", 1),
          ("channel_10", 10),
          ("channel_100", 23),
          ("channel_104", 24),
          ("channel_108", 25),
          ("channel_11", 11),
          ("channel_112", 26),
          ("channel_116", 27),
          ("channel_12", 12),
          ("channel_120", 28),
          ("channel_124", 29),
          ("channel_128", 30),
          ("channel_13", 13),
          ("channel_132", 31),
          ("channel_136", 32),
          ("channel_140", 33),
          ("channel_149", 34),
          ("channel_153", 35),
          ("channel_157", 36),
          ("channel_161", 37),
          ("channel_165", 38),
          ("channel_2", 2),
          ("channel_3", 3),
          ("channel_36", 15),
          ("channel_4", 4),
          ("channel_40", 16),
          ("channel_44", 17),
          ("channel_48", 18),
          ("channel_5", 5),
          ("channel_52", 19),
          ("channel_56", 20),
          ("channel_6", 6),
          ("channel_60", 21),
          ("channel_64", 22),
          ("channel_7", 7),
          ("channel_8", 8),
          ("channel_9", 9),
          ("n_a", 0))
    )


_FastRoamingScanChannels2_Type.__name__ = "Integer32"
_FastRoamingScanChannels2_Object = MibScalar
fastRoamingScanChannels2 = _FastRoamingScanChannels2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 5),
    _FastRoamingScanChannels2_Type()
)
fastRoamingScanChannels2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRoamingScanChannels2.setStatus("current")


class _FastRoamingScanChannels3_Type(Integer32):
    """Custom type fastRoamingScanChannels3 based on Integer32"""
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("channel_1", 1),
          ("channel_10", 10),
          ("channel_100", 23),
          ("channel_104", 24),
          ("channel_108", 25),
          ("channel_11", 11),
          ("channel_112", 26),
          ("channel_116", 27),
          ("channel_12", 12),
          ("channel_120", 28),
          ("channel_124", 29),
          ("channel_128", 30),
          ("channel_13", 13),
          ("channel_132", 31),
          ("channel_136", 32),
          ("channel_140", 33),
          ("channel_149", 34),
          ("channel_153", 35),
          ("channel_157", 36),
          ("channel_161", 37),
          ("channel_165", 38),
          ("channel_2", 2),
          ("channel_3", 3),
          ("channel_36", 15),
          ("channel_4", 4),
          ("channel_40", 16),
          ("channel_44", 17),
          ("channel_48", 18),
          ("channel_5", 5),
          ("channel_52", 19),
          ("channel_56", 20),
          ("channel_6", 6),
          ("channel_60", 21),
          ("channel_64", 22),
          ("channel_7", 7),
          ("channel_8", 8),
          ("channel_9", 9),
          ("n_a", 0))
    )


_FastRoamingScanChannels3_Type.__name__ = "Integer32"
_FastRoamingScanChannels3_Object = MibScalar
fastRoamingScanChannels3 = _FastRoamingScanChannels3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 6),
    _FastRoamingScanChannels3_Type()
)
fastRoamingScanChannels3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRoamingScanChannels3.setStatus("current")


class _FastRoamingThreshold_Type(Integer32):
    """Custom type fastRoamingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -40),
    )


_FastRoamingThreshold_Type.__name__ = "Integer32"
_FastRoamingThreshold_Object = MibScalar
fastRoamingThreshold = _FastRoamingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 7),
    _FastRoamingThreshold_Type()
)
fastRoamingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRoamingThreshold.setStatus("current")


class _FastRoamingDifference_Type(Integer32):
    """Custom type fastRoamingDifference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FastRoamingDifference_Type.__name__ = "Integer32"
_FastRoamingDifference_Object = MibScalar
fastRoamingDifference = _FastRoamingDifference_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 4, 3, 8),
    _FastRoamingDifference_Type()
)
fastRoamingDifference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRoamingDifference.setStatus("current")
_WlanLogSetting_ObjectIdentity = ObjectIdentity
wlanLogSetting = _WlanLogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 5)
)


class _WlanLogEnable_Type(Integer32):
    """Custom type wlanLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlanLogEnable_Type.__name__ = "Integer32"
_WlanLogEnable_Object = MibScalar
wlanLogEnable = _WlanLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 5, 1),
    _WlanLogEnable_Type()
)
wlanLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanLogEnable.setStatus("current")
_AdvancedSetting_ObjectIdentity = ObjectIdentity
advancedSetting = _AdvancedSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6)
)


class _GratuitousArp_Type(Integer32):
    """Custom type gratuitousArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GratuitousArp_Type.__name__ = "Integer32"
_GratuitousArp_Object = MibScalar
gratuitousArp = _GratuitousArp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 1),
    _GratuitousArp_Type()
)
gratuitousArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArp.setStatus("current")


class _GratuitousArpSendPeriod_Type(Integer32):
    """Custom type gratuitousArpSendPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_GratuitousArpSendPeriod_Type.__name__ = "Integer32"
_GratuitousArpSendPeriod_Object = MibScalar
gratuitousArpSendPeriod = _GratuitousArpSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 2),
    _GratuitousArpSendPeriod_Type()
)
gratuitousArpSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpSendPeriod.setStatus("current")
_GratuitousArpIpAddress1_Type = DisplayString
_GratuitousArpIpAddress1_Object = MibScalar
gratuitousArpIpAddress1 = _GratuitousArpIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 3),
    _GratuitousArpIpAddress1_Type()
)
gratuitousArpIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpIpAddress1.setStatus("current")
_GratuitousArpMacAddress1_Type = DisplayString
_GratuitousArpMacAddress1_Object = MibScalar
gratuitousArpMacAddress1 = _GratuitousArpMacAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 4),
    _GratuitousArpMacAddress1_Type()
)
gratuitousArpMacAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpMacAddress1.setStatus("current")
_GratuitousArpIpAddress2_Type = DisplayString
_GratuitousArpIpAddress2_Object = MibScalar
gratuitousArpIpAddress2 = _GratuitousArpIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 5),
    _GratuitousArpIpAddress2_Type()
)
gratuitousArpIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpIpAddress2.setStatus("current")
_GratuitousArpMacAddress2_Type = DisplayString
_GratuitousArpMacAddress2_Object = MibScalar
gratuitousArpMacAddress2 = _GratuitousArpMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 6),
    _GratuitousArpMacAddress2_Type()
)
gratuitousArpMacAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpMacAddress2.setStatus("current")
_GratuitousArpIpAddress3_Type = DisplayString
_GratuitousArpIpAddress3_Object = MibScalar
gratuitousArpIpAddress3 = _GratuitousArpIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 7),
    _GratuitousArpIpAddress3_Type()
)
gratuitousArpIpAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpIpAddress3.setStatus("current")
_GratuitousArpMacAddress3_Type = DisplayString
_GratuitousArpMacAddress3_Object = MibScalar
gratuitousArpMacAddress3 = _GratuitousArpMacAddress3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 8),
    _GratuitousArpMacAddress3_Type()
)
gratuitousArpMacAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpMacAddress3.setStatus("current")
_GratuitousArpIpAddress4_Type = DisplayString
_GratuitousArpIpAddress4_Object = MibScalar
gratuitousArpIpAddress4 = _GratuitousArpIpAddress4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 9),
    _GratuitousArpIpAddress4_Type()
)
gratuitousArpIpAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpIpAddress4.setStatus("current")
_GratuitousArpMacAddress4_Type = DisplayString
_GratuitousArpMacAddress4_Object = MibScalar
gratuitousArpMacAddress4 = _GratuitousArpMacAddress4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 3, 6, 10),
    _GratuitousArpMacAddress4_Type()
)
gratuitousArpMacAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpMacAddress4.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4)
)
_OpModeSetting_ObjectIdentity = ObjectIdentity
opModeSetting = _OpModeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1)
)
_OpMode_ObjectIdentity = ObjectIdentity
opMode = _OpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 1)
)
_OpModePortTable_Object = MibTable
opModePortTable = _OpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    opModePortTable.setStatus("current")
_OpModePortEntry_Object = MibTableRow
opModePortEntry = _OpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 1, 1, 1)
)
opModePortEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    opModePortEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 1, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortMode_Type(Integer32):
    """Custom type portMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7,
              10,
              12,
              13,
              14,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("disable", 7),
          ("ethernet-modem", 12),
          ("pair-connection-master", 1),
          ("pair-connection-slave", 0),
          ("real-Com", 2),
          ("reverse-Terminal", 21),
          ("rfc-2217", 20),
          ("tcp-Client", 13),
          ("tcp-Server", 10),
          ("udp", 14))
    )


_PortMode_Type.__name__ = "Integer32"
_PortMode_Object = MibTableColumn
portMode = _PortMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 1, 1, 1, 2),
    _PortMode_Type()
)
portMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMode.setStatus("current")
_OpModeParam_ObjectIdentity = ObjectIdentity
opModeParam = _OpModeParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2)
)
_RealCOM_ObjectIdentity = ObjectIdentity
realCOM = _RealCOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1)
)
_RealCOMTable_Object = MibTable
realCOMTable = _RealCOMTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    realCOMTable.setStatus("current")
_RealCOMEntry_Object = MibTableRow
realCOMEntry = _RealCOMEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1)
)
realCOMEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    realCOMEntry.setStatus("current")
_RealCOMTcpAliveCheck_Type = Integer32
_RealCOMTcpAliveCheck_Object = MibTableColumn
realCOMTcpAliveCheck = _RealCOMTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1, 1),
    _RealCOMTcpAliveCheck_Type()
)
realCOMTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realCOMTcpAliveCheck.setStatus("current")
_RealCOMMaxConnection_Type = Integer32
_RealCOMMaxConnection_Object = MibTableColumn
realCOMMaxConnection = _RealCOMMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1, 2),
    _RealCOMMaxConnection_Type()
)
realCOMMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realCOMMaxConnection.setStatus("current")


class _RealCOMIgnoreJammedIp_Type(Integer32):
    """Custom type realCOMIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RealCOMIgnoreJammedIp_Type.__name__ = "Integer32"
_RealCOMIgnoreJammedIp_Object = MibTableColumn
realCOMIgnoreJammedIp = _RealCOMIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1, 3),
    _RealCOMIgnoreJammedIp_Type()
)
realCOMIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realCOMIgnoreJammedIp.setStatus("current")


class _RealCOMAllowDriverControl_Type(Integer32):
    """Custom type realCOMAllowDriverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RealCOMAllowDriverControl_Type.__name__ = "Integer32"
_RealCOMAllowDriverControl_Object = MibTableColumn
realCOMAllowDriverControl = _RealCOMAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1, 4),
    _RealCOMAllowDriverControl_Type()
)
realCOMAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realCOMAllowDriverControl.setStatus("current")


class _RealCOMConnectionDownRTS_Type(Integer32):
    """Custom type realCOMConnectionDownRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_RealCOMConnectionDownRTS_Type.__name__ = "Integer32"
_RealCOMConnectionDownRTS_Object = MibTableColumn
realCOMConnectionDownRTS = _RealCOMConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1, 5),
    _RealCOMConnectionDownRTS_Type()
)
realCOMConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realCOMConnectionDownRTS.setStatus("current")


class _RealCOMConnectionDownDTR_Type(Integer32):
    """Custom type realCOMConnectionDownDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_RealCOMConnectionDownDTR_Type.__name__ = "Integer32"
_RealCOMConnectionDownDTR_Object = MibTableColumn
realCOMConnectionDownDTR = _RealCOMConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 1, 1, 1, 6),
    _RealCOMConnectionDownDTR_Type()
)
realCOMConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realCOMConnectionDownDTR.setStatus("current")
_Rfc2217_ObjectIdentity = ObjectIdentity
rfc2217 = _Rfc2217_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 2)
)
_Rfc2217Table_Object = MibTable
rfc2217Table = _Rfc2217Table_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rfc2217Table.setStatus("current")
_Rfc2217Entry_Object = MibTableRow
rfc2217Entry = _Rfc2217Entry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 2, 1, 1)
)
rfc2217Entry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    rfc2217Entry.setStatus("current")
_Rfc2217TcpAliveCheck_Type = Integer32
_Rfc2217TcpAliveCheck_Object = MibTableColumn
rfc2217TcpAliveCheck = _Rfc2217TcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 2, 1, 1, 1),
    _Rfc2217TcpAliveCheck_Type()
)
rfc2217TcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfc2217TcpAliveCheck.setStatus("current")
_Rfc2217TcpPort_Type = Integer32
_Rfc2217TcpPort_Object = MibTableColumn
rfc2217TcpPort = _Rfc2217TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 2, 1, 1, 2),
    _Rfc2217TcpPort_Type()
)
rfc2217TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfc2217TcpPort.setStatus("current")
_TcpServer_ObjectIdentity = ObjectIdentity
tcpServer = _TcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3)
)
_TcpServerTable_Object = MibTable
tcpServerTable = _TcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tcpServerTable.setStatus("current")
_TcpServerEntry_Object = MibTableRow
tcpServerEntry = _TcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1)
)
tcpServerEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    tcpServerEntry.setStatus("current")
_TcpServerTcpAliveCheck_Type = Integer32
_TcpServerTcpAliveCheck_Object = MibTableColumn
tcpServerTcpAliveCheck = _TcpServerTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 1),
    _TcpServerTcpAliveCheck_Type()
)
tcpServerTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerTcpAliveCheck.setStatus("current")
_TcpServerInactivityTime_Type = Integer32
_TcpServerInactivityTime_Object = MibTableColumn
tcpServerInactivityTime = _TcpServerInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 2),
    _TcpServerInactivityTime_Type()
)
tcpServerInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerInactivityTime.setStatus("current")
_TcpServerMaxConnection_Type = Integer32
_TcpServerMaxConnection_Object = MibTableColumn
tcpServerMaxConnection = _TcpServerMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 3),
    _TcpServerMaxConnection_Type()
)
tcpServerMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerMaxConnection.setStatus("current")


class _TcpServerIgnoreJammedIp_Type(Integer32):
    """Custom type tcpServerIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TcpServerIgnoreJammedIp_Type.__name__ = "Integer32"
_TcpServerIgnoreJammedIp_Object = MibTableColumn
tcpServerIgnoreJammedIp = _TcpServerIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 4),
    _TcpServerIgnoreJammedIp_Type()
)
tcpServerIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerIgnoreJammedIp.setStatus("current")


class _TcpServerAllowDriverControl_Type(Integer32):
    """Custom type tcpServerAllowDriverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TcpServerAllowDriverControl_Type.__name__ = "Integer32"
_TcpServerAllowDriverControl_Object = MibTableColumn
tcpServerAllowDriverControl = _TcpServerAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 5),
    _TcpServerAllowDriverControl_Type()
)
tcpServerAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerAllowDriverControl.setStatus("current")
_TcpServerTcpPort_Type = Integer32
_TcpServerTcpPort_Object = MibTableColumn
tcpServerTcpPort = _TcpServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 6),
    _TcpServerTcpPort_Type()
)
tcpServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerTcpPort.setStatus("current")
_TcpServerCmdPort_Type = Integer32
_TcpServerCmdPort_Object = MibTableColumn
tcpServerCmdPort = _TcpServerCmdPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 7),
    _TcpServerCmdPort_Type()
)
tcpServerCmdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerCmdPort.setStatus("current")


class _TcpServerConnectionDownRTS_Type(Integer32):
    """Custom type tcpServerConnectionDownRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_TcpServerConnectionDownRTS_Type.__name__ = "Integer32"
_TcpServerConnectionDownRTS_Object = MibTableColumn
tcpServerConnectionDownRTS = _TcpServerConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 8),
    _TcpServerConnectionDownRTS_Type()
)
tcpServerConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerConnectionDownRTS.setStatus("current")


class _TcpServerConnectionDownDTR_Type(Integer32):
    """Custom type tcpServerConnectionDownDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-high", 0),
          ("always-low", 1))
    )


_TcpServerConnectionDownDTR_Type.__name__ = "Integer32"
_TcpServerConnectionDownDTR_Object = MibTableColumn
tcpServerConnectionDownDTR = _TcpServerConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 3, 1, 1, 9),
    _TcpServerConnectionDownDTR_Type()
)
tcpServerConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpServerConnectionDownDTR.setStatus("current")
_TcpClient_ObjectIdentity = ObjectIdentity
tcpClient = _TcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4)
)
_TcpClientTable_Object = MibTable
tcpClientTable = _TcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tcpClientTable.setStatus("current")
_TcpClientEntry_Object = MibTableRow
tcpClientEntry = _TcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1)
)
tcpClientEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    tcpClientEntry.setStatus("current")
_TcpClientTcpAliveCheck_Type = Integer32
_TcpClientTcpAliveCheck_Object = MibTableColumn
tcpClientTcpAliveCheck = _TcpClientTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 1),
    _TcpClientTcpAliveCheck_Type()
)
tcpClientTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientTcpAliveCheck.setStatus("current")
_TcpClientInactivityTime_Type = Integer32
_TcpClientInactivityTime_Object = MibTableColumn
tcpClientInactivityTime = _TcpClientInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 2),
    _TcpClientInactivityTime_Type()
)
tcpClientInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientInactivityTime.setStatus("current")


class _TcpClientIgnoreJammedIp_Type(Integer32):
    """Custom type tcpClientIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TcpClientIgnoreJammedIp_Type.__name__ = "Integer32"
_TcpClientIgnoreJammedIp_Object = MibTableColumn
tcpClientIgnoreJammedIp = _TcpClientIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 3),
    _TcpClientIgnoreJammedIp_Type()
)
tcpClientIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientIgnoreJammedIp.setStatus("current")
_TcpClientDestinationAddress1_Type = DisplayString
_TcpClientDestinationAddress1_Object = MibTableColumn
tcpClientDestinationAddress1 = _TcpClientDestinationAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 4),
    _TcpClientDestinationAddress1_Type()
)
tcpClientDestinationAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationAddress1.setStatus("current")
_TcpClientDestinationPort1_Type = Integer32
_TcpClientDestinationPort1_Object = MibTableColumn
tcpClientDestinationPort1 = _TcpClientDestinationPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 5),
    _TcpClientDestinationPort1_Type()
)
tcpClientDestinationPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationPort1.setStatus("current")
_TcpClientDestinationAddress2_Type = DisplayString
_TcpClientDestinationAddress2_Object = MibTableColumn
tcpClientDestinationAddress2 = _TcpClientDestinationAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 6),
    _TcpClientDestinationAddress2_Type()
)
tcpClientDestinationAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationAddress2.setStatus("current")
_TcpClientDestinationPort2_Type = Integer32
_TcpClientDestinationPort2_Object = MibTableColumn
tcpClientDestinationPort2 = _TcpClientDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 7),
    _TcpClientDestinationPort2_Type()
)
tcpClientDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationPort2.setStatus("current")
_TcpClientDestinationAddress3_Type = DisplayString
_TcpClientDestinationAddress3_Object = MibTableColumn
tcpClientDestinationAddress3 = _TcpClientDestinationAddress3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 8),
    _TcpClientDestinationAddress3_Type()
)
tcpClientDestinationAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationAddress3.setStatus("current")
_TcpClientDestinationPort3_Type = Integer32
_TcpClientDestinationPort3_Object = MibTableColumn
tcpClientDestinationPort3 = _TcpClientDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 9),
    _TcpClientDestinationPort3_Type()
)
tcpClientDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationPort3.setStatus("current")
_TcpClientDestinationAddress4_Type = DisplayString
_TcpClientDestinationAddress4_Object = MibTableColumn
tcpClientDestinationAddress4 = _TcpClientDestinationAddress4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 10),
    _TcpClientDestinationAddress4_Type()
)
tcpClientDestinationAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationAddress4.setStatus("current")
_TcpClientDestinationPort4_Type = Integer32
_TcpClientDestinationPort4_Object = MibTableColumn
tcpClientDestinationPort4 = _TcpClientDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 11),
    _TcpClientDestinationPort4_Type()
)
tcpClientDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDestinationPort4.setStatus("current")
_TcpClientDesignatedLocalPort1_Type = Integer32
_TcpClientDesignatedLocalPort1_Object = MibTableColumn
tcpClientDesignatedLocalPort1 = _TcpClientDesignatedLocalPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 12),
    _TcpClientDesignatedLocalPort1_Type()
)
tcpClientDesignatedLocalPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDesignatedLocalPort1.setStatus("current")
_TcpClientDesignatedLocalPort2_Type = Integer32
_TcpClientDesignatedLocalPort2_Object = MibTableColumn
tcpClientDesignatedLocalPort2 = _TcpClientDesignatedLocalPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 13),
    _TcpClientDesignatedLocalPort2_Type()
)
tcpClientDesignatedLocalPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDesignatedLocalPort2.setStatus("current")
_TcpClientDesignatedLocalPort3_Type = Integer32
_TcpClientDesignatedLocalPort3_Object = MibTableColumn
tcpClientDesignatedLocalPort3 = _TcpClientDesignatedLocalPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 14),
    _TcpClientDesignatedLocalPort3_Type()
)
tcpClientDesignatedLocalPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDesignatedLocalPort3.setStatus("current")
_TcpClientDesignatedLocalPort4_Type = Integer32
_TcpClientDesignatedLocalPort4_Object = MibTableColumn
tcpClientDesignatedLocalPort4 = _TcpClientDesignatedLocalPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 15),
    _TcpClientDesignatedLocalPort4_Type()
)
tcpClientDesignatedLocalPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientDesignatedLocalPort4.setStatus("current")


class _TcpClientConnectionControl_Type(Integer32):
    """Custom type tcpClientConnectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(257,
              258,
              260,
              264,
              514,
              1028,
              2056)
        )
    )
    namedValues = NamedValues(
        *(("anyCharacter-InactivityTime", 514),
          ("anyCharacter-None", 258),
          ("dcdOn-DCD-Off", 2056),
          ("dcdOn-None", 264),
          ("dsrOn-DSR-Off", 1028),
          ("dsrOn-None", 260),
          ("startup-None", 257))
    )


_TcpClientConnectionControl_Type.__name__ = "Integer32"
_TcpClientConnectionControl_Object = MibTableColumn
tcpClientConnectionControl = _TcpClientConnectionControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 4, 1, 1, 16),
    _TcpClientConnectionControl_Type()
)
tcpClientConnectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClientConnectionControl.setStatus("current")
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5)
)
_UdpTable_Object = MibTable
udpTable = _UdpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    udpTable.setStatus("current")
_UdpEntry_Object = MibTableRow
udpEntry = _UdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1)
)
udpEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    udpEntry.setStatus("current")
_UdpDestinationAddress1Begin_Type = IpAddress
_UdpDestinationAddress1Begin_Object = MibTableColumn
udpDestinationAddress1Begin = _UdpDestinationAddress1Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 1),
    _UdpDestinationAddress1Begin_Type()
)
udpDestinationAddress1Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress1Begin.setStatus("current")
_UdpDestinationAddress1End_Type = IpAddress
_UdpDestinationAddress1End_Object = MibTableColumn
udpDestinationAddress1End = _UdpDestinationAddress1End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 2),
    _UdpDestinationAddress1End_Type()
)
udpDestinationAddress1End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress1End.setStatus("current")
_UdpDestinationPort1_Type = Integer32
_UdpDestinationPort1_Object = MibTableColumn
udpDestinationPort1 = _UdpDestinationPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 3),
    _UdpDestinationPort1_Type()
)
udpDestinationPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationPort1.setStatus("current")
_UdpDestinationAddress2Begin_Type = IpAddress
_UdpDestinationAddress2Begin_Object = MibTableColumn
udpDestinationAddress2Begin = _UdpDestinationAddress2Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 4),
    _UdpDestinationAddress2Begin_Type()
)
udpDestinationAddress2Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress2Begin.setStatus("current")
_UdpDestinationAddress2End_Type = IpAddress
_UdpDestinationAddress2End_Object = MibTableColumn
udpDestinationAddress2End = _UdpDestinationAddress2End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 5),
    _UdpDestinationAddress2End_Type()
)
udpDestinationAddress2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress2End.setStatus("current")
_UdpDestinationPort2_Type = Integer32
_UdpDestinationPort2_Object = MibTableColumn
udpDestinationPort2 = _UdpDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 6),
    _UdpDestinationPort2_Type()
)
udpDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationPort2.setStatus("current")
_UdpDestinationAddress3Begin_Type = IpAddress
_UdpDestinationAddress3Begin_Object = MibTableColumn
udpDestinationAddress3Begin = _UdpDestinationAddress3Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 7),
    _UdpDestinationAddress3Begin_Type()
)
udpDestinationAddress3Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress3Begin.setStatus("current")
_UdpDestinationAddress3End_Type = IpAddress
_UdpDestinationAddress3End_Object = MibTableColumn
udpDestinationAddress3End = _UdpDestinationAddress3End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 8),
    _UdpDestinationAddress3End_Type()
)
udpDestinationAddress3End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress3End.setStatus("current")
_UdpDestinationPort3_Type = Integer32
_UdpDestinationPort3_Object = MibTableColumn
udpDestinationPort3 = _UdpDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 9),
    _UdpDestinationPort3_Type()
)
udpDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationPort3.setStatus("current")
_UdpDestinationAddress4Begin_Type = IpAddress
_UdpDestinationAddress4Begin_Object = MibTableColumn
udpDestinationAddress4Begin = _UdpDestinationAddress4Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 10),
    _UdpDestinationAddress4Begin_Type()
)
udpDestinationAddress4Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress4Begin.setStatus("current")
_UdpDestinationAddress4End_Type = IpAddress
_UdpDestinationAddress4End_Object = MibTableColumn
udpDestinationAddress4End = _UdpDestinationAddress4End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 11),
    _UdpDestinationAddress4End_Type()
)
udpDestinationAddress4End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationAddress4End.setStatus("current")
_UdpDestinationPort4_Type = Integer32
_UdpDestinationPort4_Object = MibTableColumn
udpDestinationPort4 = _UdpDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 12),
    _UdpDestinationPort4_Type()
)
udpDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpDestinationPort4.setStatus("current")
_UdpLocalListenPort_Type = Integer32
_UdpLocalListenPort_Object = MibTableColumn
udpLocalListenPort = _UdpLocalListenPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 5, 1, 1, 13),
    _UdpLocalListenPort_Type()
)
udpLocalListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpLocalListenPort.setStatus("current")
_PairConnectionMaster_ObjectIdentity = ObjectIdentity
pairConnectionMaster = _PairConnectionMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 6)
)
_PairConnectionMasterTable_Object = MibTable
pairConnectionMasterTable = _PairConnectionMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pairConnectionMasterTable.setStatus("current")
_PairConnectionMasterEntry_Object = MibTableRow
pairConnectionMasterEntry = _PairConnectionMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 6, 1, 1)
)
pairConnectionMasterEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    pairConnectionMasterEntry.setStatus("current")
_PairConnectionMasterTcpAliveCheck_Type = Integer32
_PairConnectionMasterTcpAliveCheck_Object = MibTableColumn
pairConnectionMasterTcpAliveCheck = _PairConnectionMasterTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 6, 1, 1, 1),
    _PairConnectionMasterTcpAliveCheck_Type()
)
pairConnectionMasterTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionMasterTcpAliveCheck.setStatus("current")
_PairConnectionMasterDestnationAddress_Type = DisplayString
_PairConnectionMasterDestnationAddress_Object = MibTableColumn
pairConnectionMasterDestnationAddress = _PairConnectionMasterDestnationAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 6, 1, 1, 2),
    _PairConnectionMasterDestnationAddress_Type()
)
pairConnectionMasterDestnationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionMasterDestnationAddress.setStatus("current")
_PairConnectionMasterDestnationTcpPort_Type = Integer32
_PairConnectionMasterDestnationTcpPort_Object = MibTableColumn
pairConnectionMasterDestnationTcpPort = _PairConnectionMasterDestnationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 6, 1, 1, 3),
    _PairConnectionMasterDestnationTcpPort_Type()
)
pairConnectionMasterDestnationTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionMasterDestnationTcpPort.setStatus("current")
_PairConnectionSlave_ObjectIdentity = ObjectIdentity
pairConnectionSlave = _PairConnectionSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 7)
)
_PairConnectionSlaveTable_Object = MibTable
pairConnectionSlaveTable = _PairConnectionSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    pairConnectionSlaveTable.setStatus("current")
_PairConnectionSlaveEntry_Object = MibTableRow
pairConnectionSlaveEntry = _PairConnectionSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 7, 1, 1)
)
pairConnectionSlaveEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    pairConnectionSlaveEntry.setStatus("current")
_PairConnectionSlaveTcpAliveCheck_Type = Integer32
_PairConnectionSlaveTcpAliveCheck_Object = MibTableColumn
pairConnectionSlaveTcpAliveCheck = _PairConnectionSlaveTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 7, 1, 1, 1),
    _PairConnectionSlaveTcpAliveCheck_Type()
)
pairConnectionSlaveTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionSlaveTcpAliveCheck.setStatus("current")
_PairConnectionSlaveLocalTcpPort_Type = Integer32
_PairConnectionSlaveLocalTcpPort_Object = MibTableColumn
pairConnectionSlaveLocalTcpPort = _PairConnectionSlaveLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 7, 1, 1, 2),
    _PairConnectionSlaveLocalTcpPort_Type()
)
pairConnectionSlaveLocalTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairConnectionSlaveLocalTcpPort.setStatus("current")
_EthernetModem_ObjectIdentity = ObjectIdentity
ethernetModem = _EthernetModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 8)
)
_EthernetModemTable_Object = MibTable
ethernetModemTable = _EthernetModemTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ethernetModemTable.setStatus("current")
_EthernetModemEntry_Object = MibTableRow
ethernetModemEntry = _EthernetModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 8, 1, 1)
)
ethernetModemEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    ethernetModemEntry.setStatus("current")
_EthernetModemTcpAliveCheck_Type = Integer32
_EthernetModemTcpAliveCheck_Object = MibTableColumn
ethernetModemTcpAliveCheck = _EthernetModemTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 8, 1, 1, 1),
    _EthernetModemTcpAliveCheck_Type()
)
ethernetModemTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetModemTcpAliveCheck.setStatus("current")
_EthernetModemLocalTcpPort_Type = Integer32
_EthernetModemLocalTcpPort_Object = MibTableColumn
ethernetModemLocalTcpPort = _EthernetModemLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 8, 1, 1, 2),
    _EthernetModemLocalTcpPort_Type()
)
ethernetModemLocalTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetModemLocalTcpPort.setStatus("current")
_ReverseTerminal_ObjectIdentity = ObjectIdentity
reverseTerminal = _ReverseTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9)
)
_ReverseTerminalTable_Object = MibTable
reverseTerminalTable = _ReverseTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    reverseTerminalTable.setStatus("current")
_ReverseTerminalEntry_Object = MibTableRow
reverseTerminalEntry = _ReverseTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1, 1)
)
reverseTerminalEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    reverseTerminalEntry.setStatus("current")
_ReverseTerminalTcpAliveCheck_Type = Integer32
_ReverseTerminalTcpAliveCheck_Object = MibTableColumn
reverseTerminalTcpAliveCheck = _ReverseTerminalTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1, 1, 1),
    _ReverseTerminalTcpAliveCheck_Type()
)
reverseTerminalTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalTcpAliveCheck.setStatus("current")
_ReverseTerminalInactivityTime_Type = Integer32
_ReverseTerminalInactivityTime_Object = MibTableColumn
reverseTerminalInactivityTime = _ReverseTerminalInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1, 1, 2),
    _ReverseTerminalInactivityTime_Type()
)
reverseTerminalInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalInactivityTime.setStatus("current")
_ReverseTerminalTcpPort_Type = Integer32
_ReverseTerminalTcpPort_Object = MibTableColumn
reverseTerminalTcpPort = _ReverseTerminalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1, 1, 3),
    _ReverseTerminalTcpPort_Type()
)
reverseTerminalTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalTcpPort.setStatus("current")


class _ReverseTerminalAuthenticationType_Type(Integer32):
    """Custom type reverseTerminalAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 0),
          ("radius", 2))
    )


_ReverseTerminalAuthenticationType_Type.__name__ = "Integer32"
_ReverseTerminalAuthenticationType_Object = MibTableColumn
reverseTerminalAuthenticationType = _ReverseTerminalAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1, 1, 4),
    _ReverseTerminalAuthenticationType_Type()
)
reverseTerminalAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalAuthenticationType.setStatus("current")


class _ReverseTerminalMapKeys_Type(Integer32):
    """Custom type reverseTerminalMapKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cr", 1),
          ("cr-lf", 0),
          ("lf", 2))
    )


_ReverseTerminalMapKeys_Type.__name__ = "Integer32"
_ReverseTerminalMapKeys_Object = MibTableColumn
reverseTerminalMapKeys = _ReverseTerminalMapKeys_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 2, 9, 1, 1, 5),
    _ReverseTerminalMapKeys_Type()
)
reverseTerminalMapKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalMapKeys.setStatus("current")
_DataPacking_ObjectIdentity = ObjectIdentity
dataPacking = _DataPacking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3)
)
_DataPackingPortTable_Object = MibTable
dataPackingPortTable = _DataPackingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dataPackingPortTable.setStatus("current")
_DataPackingPortEntry_Object = MibTableRow
dataPackingPortEntry = _DataPackingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1)
)
dataPackingPortEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dataPackingPortEntry.setStatus("current")
_PortPacketLength_Type = Integer32
_PortPacketLength_Object = MibTableColumn
portPacketLength = _PortPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 1),
    _PortPacketLength_Type()
)
portPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPacketLength.setStatus("current")


class _PortDelimiter1Enable_Type(Integer32):
    """Custom type portDelimiter1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortDelimiter1Enable_Type.__name__ = "Integer32"
_PortDelimiter1Enable_Object = MibTableColumn
portDelimiter1Enable = _PortDelimiter1Enable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 2),
    _PortDelimiter1Enable_Type()
)
portDelimiter1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter1Enable.setStatus("current")


class _PortDelimiter1_Type(DisplayString):
    """Custom type portDelimiter1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_PortDelimiter1_Type.__name__ = "DisplayString"
_PortDelimiter1_Object = MibTableColumn
portDelimiter1 = _PortDelimiter1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 3),
    _PortDelimiter1_Type()
)
portDelimiter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter1.setStatus("current")


class _PortDelimiter2Enable_Type(Integer32):
    """Custom type portDelimiter2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortDelimiter2Enable_Type.__name__ = "Integer32"
_PortDelimiter2Enable_Object = MibTableColumn
portDelimiter2Enable = _PortDelimiter2Enable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 4),
    _PortDelimiter2Enable_Type()
)
portDelimiter2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter2Enable.setStatus("current")


class _PortDelimiter2_Type(DisplayString):
    """Custom type portDelimiter2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_PortDelimiter2_Type.__name__ = "DisplayString"
_PortDelimiter2_Object = MibTableColumn
portDelimiter2 = _PortDelimiter2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 5),
    _PortDelimiter2_Type()
)
portDelimiter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiter2.setStatus("current")


class _PortDelimiterProcess_Type(Integer32):
    """Custom type portDelimiterProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("delimiterAddOne", 2),
          ("delimiterAddTwo", 4),
          ("doNothing", 1),
          ("stripDelimiter", 8))
    )


_PortDelimiterProcess_Type.__name__ = "Integer32"
_PortDelimiterProcess_Object = MibTableColumn
portDelimiterProcess = _PortDelimiterProcess_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 6),
    _PortDelimiterProcess_Type()
)
portDelimiterProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiterProcess.setStatus("current")
_PortForceTransmit_Type = Integer32
_PortForceTransmit_Object = MibTableColumn
portForceTransmit = _PortForceTransmit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 1, 3, 1, 1, 7),
    _PortForceTransmit_Type()
)
portForceTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForceTransmit.setStatus("current")
_ComParamSetting_ObjectIdentity = ObjectIdentity
comParamSetting = _ComParamSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2)
)
_ComParamPortTable_Object = MibTable
comParamPortTable = _ComParamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    comParamPortTable.setStatus("current")
_ComParamPortEntry_Object = MibTableRow
comParamPortEntry = _ComParamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1)
)
comParamPortEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    comParamPortEntry.setStatus("current")


class _PortAlias_Type(DisplayString):
    """Custom type portAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortAlias_Type.__name__ = "DisplayString"
_PortAlias_Object = MibTableColumn
portAlias = _PortAlias_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 1),
    _PortAlias_Type()
)
portAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAlias.setStatus("current")


class _PortInterface_Type(Integer32):
    """Custom type portInterface based on Integer32"""
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
        *(("rs-232", 0),
          ("rs-422", 1),
          ("rs-485-2wire", 2),
          ("rs-485-4wire", 3))
    )


_PortInterface_Type.__name__ = "Integer32"
_PortInterface_Object = MibTableColumn
portInterface = _PortInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 2),
    _PortInterface_Type()
)
portInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInterface.setStatus("current")


class _PortBaudRate_Type(Integer32):
    """Custom type portBaudRate based on Integer32"""
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
        *(("b110", 2),
          ("b115200", 16),
          ("b1200", 7),
          ("b134", 3),
          ("b150", 4),
          ("b1800", 8),
          ("b19200", 13),
          ("b230400", 17),
          ("b2400", 9),
          ("b300", 5),
          ("b38400", 14),
          ("b460800", 18),
          ("b4800", 10),
          ("b50", 0),
          ("b57600", 15),
          ("b600", 6),
          ("b75", 1),
          ("b921600", 19),
          ("b9600", 12))
    )


_PortBaudRate_Type.__name__ = "Integer32"
_PortBaudRate_Object = MibTableColumn
portBaudRate = _PortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 3),
    _PortBaudRate_Type()
)
portBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaudRate.setStatus("current")


class _PortDataBits_Type(Integer32):
    """Custom type portDataBits based on Integer32"""
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
        *(("bits-5", 0),
          ("bits-6", 1),
          ("bits-7", 2),
          ("bits-8", 3))
    )


_PortDataBits_Type.__name__ = "Integer32"
_PortDataBits_Object = MibTableColumn
portDataBits = _PortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 4),
    _PortDataBits_Type()
)
portDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDataBits.setStatus("current")


class _PortStopBits_Type(Integer32):
    """Custom type portStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits-1", 0),
          ("bits-1dot5", 1),
          ("bits-2", 2))
    )


_PortStopBits_Type.__name__ = "Integer32"
_PortStopBits_Object = MibTableColumn
portStopBits = _PortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 5),
    _PortStopBits_Type()
)
portStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStopBits.setStatus("current")


class _PortParity_Type(Integer32):
    """Custom type portParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("mark", 5),
          ("none", 0),
          ("odd", 1),
          ("space", 7))
    )


_PortParity_Type.__name__ = "Integer32"
_PortParity_Object = MibTableColumn
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 6),
    _PortParity_Type()
)
portParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portParity.setStatus("current")


class _PortFlowControl_Type(Integer32):
    """Custom type portFlowControl based on Integer32"""
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
          ("rts-cts", 1),
          ("xon-xoff", 2))
    )


_PortFlowControl_Type.__name__ = "Integer32"
_PortFlowControl_Object = MibTableColumn
portFlowControl = _PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 7),
    _PortFlowControl_Type()
)
portFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowControl.setStatus("current")


class _PortFIFO_Type(Integer32):
    """Custom type portFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortFIFO_Type.__name__ = "Integer32"
_PortFIFO_Object = MibTableColumn
portFIFO = _PortFIFO_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 2, 1, 1, 8),
    _PortFIFO_Type()
)
portFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFIFO.setStatus("current")
_DataBuffering_ObjectIdentity = ObjectIdentity
dataBuffering = _DataBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 3)
)
_DataBufferingPortTable_Object = MibTable
dataBufferingPortTable = _DataBufferingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dataBufferingPortTable.setStatus("current")
_DataBufferingPortEntry_Object = MibTableRow
dataBufferingPortEntry = _DataBufferingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 3, 1, 1)
)
dataBufferingPortEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dataBufferingPortEntry.setStatus("current")


class _PortBufferingEnable_Type(Integer32):
    """Custom type portBufferingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortBufferingEnable_Type.__name__ = "Integer32"
_PortBufferingEnable_Object = MibTableColumn
portBufferingEnable = _PortBufferingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 3, 1, 1, 1),
    _PortBufferingEnable_Type()
)
portBufferingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBufferingEnable.setStatus("current")


class _PortSerialDataLoggingEnable_Type(Integer32):
    """Custom type portSerialDataLoggingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortSerialDataLoggingEnable_Type.__name__ = "Integer32"
_PortSerialDataLoggingEnable_Object = MibTableColumn
portSerialDataLoggingEnable = _PortSerialDataLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 4, 3, 1, 1, 2),
    _PortSerialDataLoggingEnable_Type()
)
portSerialDataLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSerialDataLoggingEnable.setStatus("current")
_SysManagement_ObjectIdentity = ObjectIdentity
sysManagement = _SysManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5)
)
_MiscNetworkSettings_ObjectIdentity = ObjectIdentity
miscNetworkSettings = _MiscNetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1)
)
_AccessibleIp_ObjectIdentity = ObjectIdentity
accessibleIp = _AccessibleIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1)
)


class _EnableAccessibleIpList_Type(Integer32):
    """Custom type enableAccessibleIpList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableAccessibleIpList_Type.__name__ = "Integer32"
_EnableAccessibleIpList_Object = MibScalar
enableAccessibleIpList = _EnableAccessibleIpList_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 1),
    _EnableAccessibleIpList_Type()
)
enableAccessibleIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAccessibleIpList.setStatus("current")
_AccessibleIpListTable_Object = MibTable
accessibleIpListTable = _AccessibleIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    accessibleIpListTable.setStatus("current")
_AccessibleIpListEntry_Object = MibTableRow
accessibleIpListEntry = _AccessibleIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 2, 1)
)
accessibleIpListEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "accessibleIpListIndex"),
)
if mibBuilder.loadTexts:
    accessibleIpListEntry.setStatus("current")


class _AccessibleIpListIndex_Type(Integer32):
    """Custom type accessibleIpListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AccessibleIpListIndex_Type.__name__ = "Integer32"
_AccessibleIpListIndex_Object = MibTableColumn
accessibleIpListIndex = _AccessibleIpListIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 2, 1, 1),
    _AccessibleIpListIndex_Type()
)
accessibleIpListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessibleIpListIndex.setStatus("current")


class _ActiveAccessibleIpList_Type(Integer32):
    """Custom type activeAccessibleIpList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ActiveAccessibleIpList_Type.__name__ = "Integer32"
_ActiveAccessibleIpList_Object = MibTableColumn
activeAccessibleIpList = _ActiveAccessibleIpList_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 2, 1, 2),
    _ActiveAccessibleIpList_Type()
)
activeAccessibleIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAccessibleIpList.setStatus("current")
_AccessibleIpListAddress_Type = IpAddress
_AccessibleIpListAddress_Object = MibTableColumn
accessibleIpListAddress = _AccessibleIpListAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 2, 1, 3),
    _AccessibleIpListAddress_Type()
)
accessibleIpListAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessibleIpListAddress.setStatus("current")
_AccessibleIpListNetmask_Type = IpAddress
_AccessibleIpListNetmask_Object = MibTableColumn
accessibleIpListNetmask = _AccessibleIpListNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 1, 2, 1, 4),
    _AccessibleIpListNetmask_Type()
)
accessibleIpListNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessibleIpListNetmask.setStatus("current")
_SnmpAgentSettings_ObjectIdentity = ObjectIdentity
snmpAgentSettings = _SnmpAgentSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 2)
)


class _SnmpEnable_Type(Integer32):
    """Custom type snmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnmpEnable_Type.__name__ = "Integer32"
_SnmpEnable_Object = MibScalar
snmpEnable = _SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 2, 1),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")


class _SnmpContactName_Type(DisplayString):
    """Custom type snmpContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SnmpContactName_Type.__name__ = "DisplayString"
_SnmpContactName_Object = MibScalar
snmpContactName = _SnmpContactName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 2, 2),
    _SnmpContactName_Type()
)
snmpContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpContactName.setStatus("current")


class _SnmpLocation_Type(DisplayString):
    """Custom type snmpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SnmpLocation_Type.__name__ = "DisplayString"
_SnmpLocation_Object = MibScalar
snmpLocation = _SnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 2, 3),
    _SnmpLocation_Type()
)
snmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLocation.setStatus("current")
_AuthenticationServer_ObjectIdentity = ObjectIdentity
authenticationServer = _AuthenticationServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 4)
)


class _RadiusServerIp_Type(DisplayString):
    """Custom type radiusServerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RadiusServerIp_Type.__name__ = "DisplayString"
_RadiusServerIp_Object = MibScalar
radiusServerIp = _RadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 4, 1),
    _RadiusServerIp_Type()
)
radiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIp.setStatus("current")


class _UdpPortAuthenticationServer_Type(Integer32):
    """Custom type udpPortAuthenticationServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1645,
              1812)
        )
    )
    namedValues = NamedValues(
        *(("port1645", 1645),
          ("port1812", 1812))
    )


_UdpPortAuthenticationServer_Type.__name__ = "Integer32"
_UdpPortAuthenticationServer_Object = MibScalar
udpPortAuthenticationServer = _UdpPortAuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 4, 3),
    _UdpPortAuthenticationServer_Type()
)
udpPortAuthenticationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpPortAuthenticationServer.setStatus("current")


class _RadiusAccounting_Type(Integer32):
    """Custom type radiusAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RadiusAccounting_Type.__name__ = "Integer32"
_RadiusAccounting_Object = MibScalar
radiusAccounting = _RadiusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 4, 4),
    _RadiusAccounting_Type()
)
radiusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccounting.setStatus("current")
_SysLogSettings_ObjectIdentity = ObjectIdentity
sysLogSettings = _SysLogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 5)
)


class _SysLocalLog_Type(Integer32):
    """Custom type sysLocalLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SysLocalLog_Type.__name__ = "Integer32"
_SysLocalLog_Object = MibScalar
sysLocalLog = _SysLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 5, 1),
    _SysLocalLog_Type()
)
sysLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalLog.setStatus("current")


class _NetworkLocalLog_Type(Integer32):
    """Custom type networkLocalLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NetworkLocalLog_Type.__name__ = "Integer32"
_NetworkLocalLog_Object = MibScalar
networkLocalLog = _NetworkLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 5, 2),
    _NetworkLocalLog_Type()
)
networkLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLocalLog.setStatus("current")


class _ConfigLocalLog_Type(Integer32):
    """Custom type configLocalLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ConfigLocalLog_Type.__name__ = "Integer32"
_ConfigLocalLog_Object = MibScalar
configLocalLog = _ConfigLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 5, 3),
    _ConfigLocalLog_Type()
)
configLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLocalLog.setStatus("current")


class _OpModeLocalLog_Type(Integer32):
    """Custom type opModeLocalLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OpModeLocalLog_Type.__name__ = "Integer32"
_OpModeLocalLog_Object = MibScalar
opModeLocalLog = _OpModeLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 1, 5, 4),
    _OpModeLocalLog_Type()
)
opModeLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opModeLocalLog.setStatus("current")
_AutoWarningSettings_ObjectIdentity = ObjectIdentity
autoWarningSettings = _AutoWarningSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2)
)
_EventSettings_ObjectIdentity = ObjectIdentity
eventSettings = _EventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1)
)


class _MailWarningColdStart_Type(Integer32):
    """Custom type mailWarningColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailWarningColdStart_Type.__name__ = "Integer32"
_MailWarningColdStart_Object = MibScalar
mailWarningColdStart = _MailWarningColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 1),
    _MailWarningColdStart_Type()
)
mailWarningColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningColdStart.setStatus("current")


class _MailWarningWarmStart_Type(Integer32):
    """Custom type mailWarningWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailWarningWarmStart_Type.__name__ = "Integer32"
_MailWarningWarmStart_Object = MibScalar
mailWarningWarmStart = _MailWarningWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 2),
    _MailWarningWarmStart_Type()
)
mailWarningWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningWarmStart.setStatus("current")


class _MailWarningAuthFailure_Type(Integer32):
    """Custom type mailWarningAuthFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailWarningAuthFailure_Type.__name__ = "Integer32"
_MailWarningAuthFailure_Object = MibScalar
mailWarningAuthFailure = _MailWarningAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 3),
    _MailWarningAuthFailure_Type()
)
mailWarningAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningAuthFailure.setStatus("current")


class _MailWarningIpChanged_Type(Integer32):
    """Custom type mailWarningIpChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailWarningIpChanged_Type.__name__ = "Integer32"
_MailWarningIpChanged_Object = MibScalar
mailWarningIpChanged = _MailWarningIpChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 4),
    _MailWarningIpChanged_Type()
)
mailWarningIpChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningIpChanged.setStatus("current")


class _MailWarningPasswordChanged_Type(Integer32):
    """Custom type mailWarningPasswordChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailWarningPasswordChanged_Type.__name__ = "Integer32"
_MailWarningPasswordChanged_Object = MibScalar
mailWarningPasswordChanged = _MailWarningPasswordChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 5),
    _MailWarningPasswordChanged_Type()
)
mailWarningPasswordChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningPasswordChanged.setStatus("current")


class _TrapServerColdStart_Type(Integer32):
    """Custom type trapServerColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TrapServerColdStart_Type.__name__ = "Integer32"
_TrapServerColdStart_Object = MibScalar
trapServerColdStart = _TrapServerColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 6),
    _TrapServerColdStart_Type()
)
trapServerColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerColdStart.setStatus("current")


class _TrapServerWarmStart_Type(Integer32):
    """Custom type trapServerWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TrapServerWarmStart_Type.__name__ = "Integer32"
_TrapServerWarmStart_Object = MibScalar
trapServerWarmStart = _TrapServerWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 7),
    _TrapServerWarmStart_Type()
)
trapServerWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerWarmStart.setStatus("current")


class _TrapServerAuthFailure_Type(Integer32):
    """Custom type trapServerAuthFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TrapServerAuthFailure_Type.__name__ = "Integer32"
_TrapServerAuthFailure_Object = MibScalar
trapServerAuthFailure = _TrapServerAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 1, 8),
    _TrapServerAuthFailure_Type()
)
trapServerAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerAuthFailure.setStatus("current")
_SerialEventSettings_ObjectIdentity = ObjectIdentity
serialEventSettings = _SerialEventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2)
)
_PortEventSettingsTable_Object = MibTable
portEventSettingsTable = _PortEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    portEventSettingsTable.setStatus("current")
_PortEventSettingsEntry_Object = MibTableRow
portEventSettingsEntry = _PortEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2, 1, 1)
)
portEventSettingsEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEventSettingsEntry.setStatus("current")


class _MailDCDchange_Type(Integer32):
    """Custom type mailDCDchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailDCDchange_Type.__name__ = "Integer32"
_MailDCDchange_Object = MibTableColumn
mailDCDchange = _MailDCDchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2, 1, 1, 1),
    _MailDCDchange_Type()
)
mailDCDchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailDCDchange.setStatus("current")


class _TrapDCDchange_Type(Integer32):
    """Custom type trapDCDchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TrapDCDchange_Type.__name__ = "Integer32"
_TrapDCDchange_Object = MibTableColumn
trapDCDchange = _TrapDCDchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2, 1, 1, 2),
    _TrapDCDchange_Type()
)
trapDCDchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDCDchange.setStatus("current")


class _MailDSRchange_Type(Integer32):
    """Custom type mailDSRchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MailDSRchange_Type.__name__ = "Integer32"
_MailDSRchange_Object = MibTableColumn
mailDSRchange = _MailDSRchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2, 1, 1, 3),
    _MailDSRchange_Type()
)
mailDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailDSRchange.setStatus("current")


class _TrapDSRchange_Type(Integer32):
    """Custom type trapDSRchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TrapDSRchange_Type.__name__ = "Integer32"
_TrapDSRchange_Object = MibTableColumn
trapDSRchange = _TrapDSRchange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 2, 1, 1, 4),
    _TrapDSRchange_Type()
)
trapDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDSRchange.setStatus("current")
_EmailAlert_ObjectIdentity = ObjectIdentity
emailAlert = _EmailAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3)
)
_EmailWarningMailServer_Type = DisplayString
_EmailWarningMailServer_Object = MibScalar
emailWarningMailServer = _EmailWarningMailServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 1),
    _EmailWarningMailServer_Type()
)
emailWarningMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningMailServer.setStatus("current")


class _EmailRequiresAuthentication_Type(Integer32):
    """Custom type emailRequiresAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-require", 0),
          ("require", 1))
    )


_EmailRequiresAuthentication_Type.__name__ = "Integer32"
_EmailRequiresAuthentication_Object = MibScalar
emailRequiresAuthentication = _EmailRequiresAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 2),
    _EmailRequiresAuthentication_Type()
)
emailRequiresAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailRequiresAuthentication.setStatus("current")
_EmailWarningUserName_Type = DisplayString
_EmailWarningUserName_Object = MibScalar
emailWarningUserName = _EmailWarningUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 3),
    _EmailWarningUserName_Type()
)
emailWarningUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningUserName.setStatus("current")
_EmailWarningFromEmail_Type = DisplayString
_EmailWarningFromEmail_Object = MibScalar
emailWarningFromEmail = _EmailWarningFromEmail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 5),
    _EmailWarningFromEmail_Type()
)
emailWarningFromEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFromEmail.setStatus("current")
_EmailWarningFirstEmailAddr_Type = DisplayString
_EmailWarningFirstEmailAddr_Object = MibScalar
emailWarningFirstEmailAddr = _EmailWarningFirstEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 6),
    _EmailWarningFirstEmailAddr_Type()
)
emailWarningFirstEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFirstEmailAddr.setStatus("current")
_EmailWarningSecondEmailAddr_Type = DisplayString
_EmailWarningSecondEmailAddr_Object = MibScalar
emailWarningSecondEmailAddr = _EmailWarningSecondEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 7),
    _EmailWarningSecondEmailAddr_Type()
)
emailWarningSecondEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSecondEmailAddr.setStatus("current")
_EmailWarningThirdEmailAddr_Type = DisplayString
_EmailWarningThirdEmailAddr_Object = MibScalar
emailWarningThirdEmailAddr = _EmailWarningThirdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 8),
    _EmailWarningThirdEmailAddr_Type()
)
emailWarningThirdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningThirdEmailAddr.setStatus("current")
_EmailWarningFourthEmailAddr_Type = DisplayString
_EmailWarningFourthEmailAddr_Object = MibScalar
emailWarningFourthEmailAddr = _EmailWarningFourthEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 3, 9),
    _EmailWarningFourthEmailAddr_Type()
)
emailWarningFourthEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFourthEmailAddr.setStatus("current")
_SnmpTrap_ObjectIdentity = ObjectIdentity
snmpTrap = _SnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 4)
)
_SnmpTrapReceiverIp_Type = DisplayString
_SnmpTrapReceiverIp_Object = MibScalar
snmpTrapReceiverIp = _SnmpTrapReceiverIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 4, 1),
    _SnmpTrapReceiverIp_Type()
)
snmpTrapReceiverIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapReceiverIp.setStatus("current")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibScalar
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 2, 4, 2),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3)
)
_ConsoleSettings_ObjectIdentity = ObjectIdentity
consoleSettings = _ConsoleSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1)
)


class _HttpConsole_Type(Integer32):
    """Custom type httpConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpConsole_Type.__name__ = "Integer32"
_HttpConsole_Object = MibScalar
httpConsole = _HttpConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1, 1),
    _HttpConsole_Type()
)
httpConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpConsole.setStatus("current")


class _HttpsConsole_Type(Integer32):
    """Custom type httpsConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpsConsole_Type.__name__ = "Integer32"
_HttpsConsole_Object = MibScalar
httpsConsole = _HttpsConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1, 2),
    _HttpsConsole_Type()
)
httpsConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsConsole.setStatus("current")


class _TelnetConsole_Type(Integer32):
    """Custom type telnetConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TelnetConsole_Type.__name__ = "Integer32"
_TelnetConsole_Object = MibScalar
telnetConsole = _TelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1, 3),
    _TelnetConsole_Type()
)
telnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetConsole.setStatus("current")


class _SshConsole_Type(Integer32):
    """Custom type sshConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SshConsole_Type.__name__ = "Integer32"
_SshConsole_Object = MibScalar
sshConsole = _SshConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1, 4),
    _SshConsole_Type()
)
sshConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshConsole.setStatus("current")


class _SerialConsole_Type(Integer32):
    """Custom type serialConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SerialConsole_Type.__name__ = "Integer32"
_SerialConsole_Object = MibScalar
serialConsole = _SerialConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1, 5),
    _SerialConsole_Type()
)
serialConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialConsole.setStatus("current")


class _ResetButton_Type(Integer32):
    """Custom type resetButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Always_enable", 1),
          ("Disable_after_60_sec", 0))
    )


_ResetButton_Type.__name__ = "Integer32"
_ResetButton_Object = MibScalar
resetButton = _ResetButton_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 1, 6),
    _ResetButton_Type()
)
resetButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetButton.setStatus("current")
_LoadFactoryDefault_ObjectIdentity = ObjectIdentity
loadFactoryDefault = _LoadFactoryDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 2)
)


class _LoadFactoryDefaultSetting_Type(Integer32):
    """Custom type loadFactoryDefaultSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resetToFactoryDefault", 1),
          ("resetToFactoryDefault-ExcludingIpConfiguration", 0))
    )


_LoadFactoryDefaultSetting_Type.__name__ = "Integer32"
_LoadFactoryDefaultSetting_Object = MibScalar
loadFactoryDefaultSetting = _LoadFactoryDefaultSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 5, 3, 2, 1),
    _LoadFactoryDefaultSetting_Type()
)
loadFactoryDefaultSetting.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    loadFactoryDefaultSetting.setStatus("current")
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6)
)
_S2eConnections_ObjectIdentity = ObjectIdentity
s2eConnections = _S2eConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 1)
)
_MonitorRemoteIpTable_Object = MibTable
monitorRemoteIpTable = _MonitorRemoteIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    monitorRemoteIpTable.setStatus("current")
_MonitorRemoteIpEntry_Object = MibTableRow
monitorRemoteIpEntry = _MonitorRemoteIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 1, 1, 1)
)
monitorRemoteIpEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
    (0, "MOXA-W2x50A-MIB", "remoteIpIndex"),
)
if mibBuilder.loadTexts:
    monitorRemoteIpEntry.setStatus("current")


class _RemoteIpIndex_Type(Integer32):
    """Custom type remoteIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RemoteIpIndex_Type.__name__ = "Integer32"
_RemoteIpIndex_Object = MibTableColumn
remoteIpIndex = _RemoteIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 1, 1, 1, 1),
    _RemoteIpIndex_Type()
)
remoteIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIpIndex.setStatus("current")
_MonitorRemoteIp_Type = IpAddress
_MonitorRemoteIp_Object = MibTableColumn
monitorRemoteIp = _MonitorRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 1, 1, 1, 2),
    _MonitorRemoteIp_Type()
)
monitorRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRemoteIp.setStatus("current")
_SerialPortStatus_ObjectIdentity = ObjectIdentity
serialPortStatus = _SerialPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2)
)
_MonitorSerialPortStatusTable_Object = MibTable
monitorSerialPortStatusTable = _MonitorSerialPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortStatusTable.setStatus("current")
_MonitorSerialPortStatusEntry_Object = MibTableRow
monitorSerialPortStatusEntry = _MonitorSerialPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1)
)
monitorSerialPortStatusEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortStatusEntry.setStatus("current")
_MonitorTxCount_Type = Integer32
_MonitorTxCount_Object = MibTableColumn
monitorTxCount = _MonitorTxCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 1),
    _MonitorTxCount_Type()
)
monitorTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxCount.setStatus("current")
_MonitorRxCount_Type = Integer32
_MonitorRxCount_Object = MibTableColumn
monitorRxCount = _MonitorRxCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 2),
    _MonitorRxCount_Type()
)
monitorRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxCount.setStatus("current")
_MonitorTxTotalCount_Type = Integer32
_MonitorTxTotalCount_Object = MibTableColumn
monitorTxTotalCount = _MonitorTxTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 3),
    _MonitorTxTotalCount_Type()
)
monitorTxTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxTotalCount.setStatus("current")
_MonitorRxTotalCount_Type = Integer32
_MonitorRxTotalCount_Object = MibTableColumn
monitorRxTotalCount = _MonitorRxTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 4),
    _MonitorRxTotalCount_Type()
)
monitorRxTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxTotalCount.setStatus("current")


class _MonitorDSR_Type(Integer32):
    """Custom type monitorDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDSR_Type.__name__ = "Integer32"
_MonitorDSR_Object = MibTableColumn
monitorDSR = _MonitorDSR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 5),
    _MonitorDSR_Type()
)
monitorDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDSR.setStatus("current")


class _MonitorDTR_Type(Integer32):
    """Custom type monitorDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDTR_Type.__name__ = "Integer32"
_MonitorDTR_Object = MibTableColumn
monitorDTR = _MonitorDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 6),
    _MonitorDTR_Type()
)
monitorDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDTR.setStatus("current")


class _MonitorRTS_Type(Integer32):
    """Custom type monitorRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorRTS_Type.__name__ = "Integer32"
_MonitorRTS_Object = MibTableColumn
monitorRTS = _MonitorRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 7),
    _MonitorRTS_Type()
)
monitorRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRTS.setStatus("current")


class _MonitorCTS_Type(Integer32):
    """Custom type monitorCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorCTS_Type.__name__ = "Integer32"
_MonitorCTS_Object = MibTableColumn
monitorCTS = _MonitorCTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 8),
    _MonitorCTS_Type()
)
monitorCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorCTS.setStatus("current")


class _MonitorDCD_Type(Integer32):
    """Custom type monitorDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorDCD_Type.__name__ = "Integer32"
_MonitorDCD_Object = MibTableColumn
monitorDCD = _MonitorDCD_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 2, 1, 1, 9),
    _MonitorDCD_Type()
)
monitorDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDCD.setStatus("current")
_SerialPortErrorCount_ObjectIdentity = ObjectIdentity
serialPortErrorCount = _SerialPortErrorCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3)
)
_MonitorSerialPortErrorCountTable_Object = MibTable
monitorSerialPortErrorCountTable = _MonitorSerialPortErrorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortErrorCountTable.setStatus("current")
_MonitorSerialPortErrorCountEntry_Object = MibTableRow
monitorSerialPortErrorCountEntry = _MonitorSerialPortErrorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3, 1, 1)
)
monitorSerialPortErrorCountEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortErrorCountEntry.setStatus("current")
_MonitorErrorCountFrame_Type = Integer32
_MonitorErrorCountFrame_Object = MibTableColumn
monitorErrorCountFrame = _MonitorErrorCountFrame_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3, 1, 1, 1),
    _MonitorErrorCountFrame_Type()
)
monitorErrorCountFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountFrame.setStatus("current")
_MonitorErrorCountParity_Type = Integer32
_MonitorErrorCountParity_Object = MibTableColumn
monitorErrorCountParity = _MonitorErrorCountParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3, 1, 1, 2),
    _MonitorErrorCountParity_Type()
)
monitorErrorCountParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountParity.setStatus("current")
_MonitorErrorCountOverrun_Type = Integer32
_MonitorErrorCountOverrun_Object = MibTableColumn
monitorErrorCountOverrun = _MonitorErrorCountOverrun_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3, 1, 1, 3),
    _MonitorErrorCountOverrun_Type()
)
monitorErrorCountOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountOverrun.setStatus("current")
_MonitorErrorCountBreak_Type = Integer32
_MonitorErrorCountBreak_Object = MibTableColumn
monitorErrorCountBreak = _MonitorErrorCountBreak_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 3, 1, 1, 4),
    _MonitorErrorCountBreak_Type()
)
monitorErrorCountBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountBreak.setStatus("current")
_SerialPortSettings_ObjectIdentity = ObjectIdentity
serialPortSettings = _SerialPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4)
)
_MonitorSerialPortSettingsTable_Object = MibTable
monitorSerialPortSettingsTable = _MonitorSerialPortSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortSettingsTable.setStatus("current")
_MonitorSerialPortSettingsEntry_Object = MibTableRow
monitorSerialPortSettingsEntry = _MonitorSerialPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1)
)
monitorSerialPortSettingsEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortSettingsEntry.setStatus("current")
_MonitorBaudRate_Type = Integer32
_MonitorBaudRate_Object = MibTableColumn
monitorBaudRate = _MonitorBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 1),
    _MonitorBaudRate_Type()
)
monitorBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorBaudRate.setStatus("current")


class _MonitorDataBits_Type(Integer32):
    """Custom type monitorDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bits-5", 5),
          ("bits-6", 6),
          ("bits-7", 7),
          ("bits-8", 8))
    )


_MonitorDataBits_Type.__name__ = "Integer32"
_MonitorDataBits_Object = MibTableColumn
monitorDataBits = _MonitorDataBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 2),
    _MonitorDataBits_Type()
)
monitorDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDataBits.setStatus("current")
_MonitorStopBits_Type = DisplayString
_MonitorStopBits_Object = MibTableColumn
monitorStopBits = _MonitorStopBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 3),
    _MonitorStopBits_Type()
)
monitorStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorStopBits.setStatus("current")


class _MonitorParity_Type(Integer32):
    """Custom type monitorParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              24,
              40,
              56)
        )
    )
    namedValues = NamedValues(
        *(("even", 24),
          ("mark", 40),
          ("none", 0),
          ("odd", 8),
          ("space", 56))
    )


_MonitorParity_Type.__name__ = "Integer32"
_MonitorParity_Object = MibTableColumn
monitorParity = _MonitorParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 4),
    _MonitorParity_Type()
)
monitorParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorParity.setStatus("current")


class _MonitorRTSCTSFlowControl_Type(Integer32):
    """Custom type monitorRTSCTSFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorRTSCTSFlowControl_Type.__name__ = "Integer32"
_MonitorRTSCTSFlowControl_Object = MibTableColumn
monitorRTSCTSFlowControl = _MonitorRTSCTSFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 5),
    _MonitorRTSCTSFlowControl_Type()
)
monitorRTSCTSFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRTSCTSFlowControl.setStatus("current")


class _MonitorXONXOFFFlowControl_Type(Integer32):
    """Custom type monitorXONXOFFFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorXONXOFFFlowControl_Type.__name__ = "Integer32"
_MonitorXONXOFFFlowControl_Object = MibTableColumn
monitorXONXOFFFlowControl = _MonitorXONXOFFFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 6),
    _MonitorXONXOFFFlowControl_Type()
)
monitorXONXOFFFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorXONXOFFFlowControl.setStatus("current")


class _MonitorFIFO_Type(Integer32):
    """Custom type monitorFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MonitorFIFO_Type.__name__ = "Integer32"
_MonitorFIFO_Object = MibTableColumn
monitorFIFO = _MonitorFIFO_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 7),
    _MonitorFIFO_Type()
)
monitorFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFIFO.setStatus("current")


class _MonitorInterface_Type(Integer32):
    """Custom type monitorInterface based on Integer32"""
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
        *(("rs-232", 0),
          ("rs-422", 1),
          ("rs-485-2-wire", 2),
          ("rs-485-4-wire", 3))
    )


_MonitorInterface_Type.__name__ = "Integer32"
_MonitorInterface_Object = MibTableColumn
monitorInterface = _MonitorInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 4, 1, 1, 8),
    _MonitorInterface_Type()
)
monitorInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorInterface.setStatus("current")
_SerialPortBuffering_ObjectIdentity = ObjectIdentity
serialPortBuffering = _SerialPortBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 5)
)
_MonitorSerialPortBufferingTable_Object = MibTable
monitorSerialPortBufferingTable = _MonitorSerialPortBufferingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortBufferingTable.setStatus("current")
_MonitorSerialPortBufferingEntry_Object = MibTableRow
monitorSerialPortBufferingEntry = _MonitorSerialPortBufferingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 5, 1, 1)
)
monitorSerialPortBufferingEntry.setIndexNames(
    (0, "MOXA-W2x50A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortBufferingEntry.setStatus("current")
_MonitorBuffering_Type = Integer32
_MonitorBuffering_Object = MibTableColumn
monitorBuffering = _MonitorBuffering_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 5, 1, 1, 1),
    _MonitorBuffering_Type()
)
monitorBuffering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorBuffering.setStatus("current")
_SysWlanStatus_ObjectIdentity = ObjectIdentity
sysWlanStatus = _SysWlanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6)
)
_WlanStatusActiveProfileName_Type = DisplayString
_WlanStatusActiveProfileName_Object = MibScalar
wlanStatusActiveProfileName = _WlanStatusActiveProfileName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 1),
    _WlanStatusActiveProfileName_Type()
)
wlanStatusActiveProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusActiveProfileName.setStatus("current")


class _WlanStatusIpConfiguration_Type(Integer32):
    """Custom type wlanStatusIpConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 1),
          ("static", 0))
    )


_WlanStatusIpConfiguration_Type.__name__ = "Integer32"
_WlanStatusIpConfiguration_Object = MibScalar
wlanStatusIpConfiguration = _WlanStatusIpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 2),
    _WlanStatusIpConfiguration_Type()
)
wlanStatusIpConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusIpConfiguration.setStatus("current")
_WlanStatusIpAddress_Type = IpAddress
_WlanStatusIpAddress_Object = MibScalar
wlanStatusIpAddress = _WlanStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 3),
    _WlanStatusIpAddress_Type()
)
wlanStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusIpAddress.setStatus("current")
_WlanStatusNetMask_Type = IpAddress
_WlanStatusNetMask_Object = MibScalar
wlanStatusNetMask = _WlanStatusNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 4),
    _WlanStatusNetMask_Type()
)
wlanStatusNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusNetMask.setStatus("current")
_WlanStatusDefaultGateway_Type = IpAddress
_WlanStatusDefaultGateway_Object = MibScalar
wlanStatusDefaultGateway = _WlanStatusDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 5),
    _WlanStatusDefaultGateway_Type()
)
wlanStatusDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusDefaultGateway.setStatus("current")
_WlanStatusNetworkType_Type = DisplayString
_WlanStatusNetworkType_Object = MibScalar
wlanStatusNetworkType = _WlanStatusNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 6),
    _WlanStatusNetworkType_Type()
)
wlanStatusNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusNetworkType.setStatus("current")
_WlanStatusRFType_Type = DisplayString
_WlanStatusRFType_Object = MibScalar
wlanStatusRFType = _WlanStatusRFType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 7),
    _WlanStatusRFType_Type()
)
wlanStatusRFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusRFType.setStatus("current")
_WlanStatusSSID_Type = DisplayString
_WlanStatusSSID_Object = MibScalar
wlanStatusSSID = _WlanStatusSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 8),
    _WlanStatusSSID_Type()
)
wlanStatusSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusSSID.setStatus("current")
_WlanStatusChannel_Type = DisplayString
_WlanStatusChannel_Object = MibScalar
wlanStatusChannel = _WlanStatusChannel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 9),
    _WlanStatusChannel_Type()
)
wlanStatusChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusChannel.setStatus("current")
_WlanStatusAuthentication_Type = DisplayString
_WlanStatusAuthentication_Object = MibScalar
wlanStatusAuthentication = _WlanStatusAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 10),
    _WlanStatusAuthentication_Type()
)
wlanStatusAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusAuthentication.setStatus("current")
_WlanStatusEncryption_Type = DisplayString
_WlanStatusEncryption_Object = MibScalar
wlanStatusEncryption = _WlanStatusEncryption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 11),
    _WlanStatusEncryption_Type()
)
wlanStatusEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusEncryption.setStatus("current")
_WlanStatusRegion_Type = DisplayString
_WlanStatusRegion_Object = MibScalar
wlanStatusRegion = _WlanStatusRegion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 12),
    _WlanStatusRegion_Type()
)
wlanStatusRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusRegion.setStatus("current")
_WlanStatusSignalStrength_Type = DisplayString
_WlanStatusSignalStrength_Object = MibScalar
wlanStatusSignalStrength = _WlanStatusSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 13),
    _WlanStatusSignalStrength_Type()
)
wlanStatusSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusSignalStrength.setStatus("current")
_WlanStatusConnectionSpeed_Type = DisplayString
_WlanStatusConnectionSpeed_Object = MibScalar
wlanStatusConnectionSpeed = _WlanStatusConnectionSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 14),
    _WlanStatusConnectionSpeed_Type()
)
wlanStatusConnectionSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusConnectionSpeed.setStatus("current")
_WlanStatusCurrentBSSID_Type = DisplayString
_WlanStatusCurrentBSSID_Object = MibScalar
wlanStatusCurrentBSSID = _WlanStatusCurrentBSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 6, 6, 15),
    _WlanStatusCurrentBSSID_Type()
)
wlanStatusCurrentBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatusCurrentBSSID.setStatus("current")
_ActivateSettings_ObjectIdentity = ObjectIdentity
activateSettings = _ActivateSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 7)
)


class _DoActivate_Type(Integer32):
    """Custom type doActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_DoActivate_Type.__name__ = "Integer32"
_DoActivate_Object = MibScalar
doActivate = _DoActivate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 7, 1),
    _DoActivate_Type()
)
doActivate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    doActivate.setStatus("current")
_Restart_ObjectIdentity = ObjectIdentity
restart = _Restart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 8)
)


class _RestartPorts_Type(Integer32):
    """Custom type restartPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1))
    )


_RestartPorts_Type.__name__ = "Integer32"
_RestartPorts_Object = MibScalar
restartPorts = _RestartPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 8, 1),
    _RestartPorts_Type()
)
restartPorts.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartPorts.setStatus("current")


class _RestartSystem_Type(Integer32):
    """Custom type restartSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_RestartSystem_Type.__name__ = "Integer32"
_RestartSystem_Object = MibScalar
restartSystem = _RestartSystem_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 13, 1, 8, 2),
    _RestartSystem_Type()
)
restartSystem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartSystem.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-W2x50A-MIB",
    **{"PortList": PortList,
       "moxa": moxa,
       "nport": nport,
       "w2x50A": w2x50A,
       "swMgmt": swMgmt,
       "overview": overview,
       "modelName": modelName,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "ethIPAddress": ethIPAddress,
       "ethMacAddress": ethMacAddress,
       "wlanIPAddress": wlanIPAddress,
       "wlanMacAddress": wlanMacAddress,
       "wlanSSID": wlanSSID,
       "wlanNetworkType": wlanNetworkType,
       "wlanSecurityMode": wlanSecurityMode,
       "wlanRFType": wlanRFType,
       "wlanCountryCode": wlanCountryCode,
       "wlanFastRoaming": wlanFastRoaming,
       "activeNetworkPort": activeNetworkPort,
       "upTime": upTime,
       "serialPort1": serialPort1,
       "serialPort2": serialPort2,
       "basicSetting": basicSetting,
       "serverSetting": serverSetting,
       "serverName": serverName,
       "serverLocation": serverLocation,
       "timeSetting": timeSetting,
       "timeZone": timeZone,
       "localTime": localTime,
       "timeServer": timeServer,
       "networkSetting": networkSetting,
       "generalSetting": generalSetting,
       "dnsServer1IpAddr": dnsServer1IpAddr,
       "dnsServer2IpAddr": dnsServer2IpAddr,
       "ethernetSetting": ethernetSetting,
       "ethIpConfiguration": ethIpConfiguration,
       "ethIpAddress": ethIpAddress,
       "ethNetMask": ethNetMask,
       "ethDefaultGateway": ethDefaultGateway,
       "ethBridgeMode": ethBridgeMode,
       "wlanSetting": wlanSetting,
       "wlanIpConfiguration": wlanIpConfiguration,
       "wlanIpAddress": wlanIpAddress,
       "wlanNetMask": wlanNetMask,
       "wlanDefaultGateway": wlanDefaultGateway,
       "profileSetting": profileSetting,
       "networkType": networkType,
       "adhocProfile": adhocProfile,
       "adhocGeneralSetting": adhocGeneralSetting,
       "adhocProfileName": adhocProfileName,
       "adhocRFType": adhocRFType,
       "adhocWlanSSID": adhocWlanSSID,
       "adhocChannel": adhocChannel,
       "adhocSecuritySetting": adhocSecuritySetting,
       "adhocAuthentication": adhocAuthentication,
       "adhocEncryption": adhocEncryption,
       "adhocWepKeyLength": adhocWepKeyLength,
       "adhocWepKeyIndex": adhocWepKeyIndex,
       "adhocWepKeyPassphrase": adhocWepKeyPassphrase,
       "adhocWepKeyFormat": adhocWepKeyFormat,
       "infrastructureProfile": infrastructureProfile,
       "infraGeneralSetting": infraGeneralSetting,
       "infraGeneralSettingTable": infraGeneralSettingTable,
       "infraGeneralSettingEntry": infraGeneralSettingEntry,
       "profileIndex": profileIndex,
       "profileName": profileName,
       "profileRFType": profileRFType,
       "profileWlanSSID": profileWlanSSID,
       "securitySetting": securitySetting,
       "securitySettingTable": securitySettingTable,
       "securitySettingEntry": securitySettingEntry,
       "authentication": authentication,
       "encryption": encryption,
       "wepKeyLength": wepKeyLength,
       "wepKeyIndex": wepKeyIndex,
       "wepKeyPassphrase": wepKeyPassphrase,
       "wepKeyFormat": wepKeyFormat,
       "eapMethod": eapMethod,
       "tunneledAuth": tunneledAuth,
       "wpaUsername": wpaUsername,
       "wpaAnonymousUsername": wpaAnonymousUsername,
       "verifyServerCert": verifyServerCert,
       "trustedServerCert": trustedServerCert,
       "userCert": userCert,
       "userPrivateKey": userPrivateKey,
       "fastRoamingSetting": fastRoamingSetting,
       "fastRoamingScanChannels1": fastRoamingScanChannels1,
       "fastRoamingScanChannels2": fastRoamingScanChannels2,
       "fastRoamingScanChannels3": fastRoamingScanChannels3,
       "fastRoamingThreshold": fastRoamingThreshold,
       "fastRoamingDifference": fastRoamingDifference,
       "wlanLogSetting": wlanLogSetting,
       "wlanLogEnable": wlanLogEnable,
       "advancedSetting": advancedSetting,
       "gratuitousArp": gratuitousArp,
       "gratuitousArpSendPeriod": gratuitousArpSendPeriod,
       "gratuitousArpIpAddress1": gratuitousArpIpAddress1,
       "gratuitousArpMacAddress1": gratuitousArpMacAddress1,
       "gratuitousArpIpAddress2": gratuitousArpIpAddress2,
       "gratuitousArpMacAddress2": gratuitousArpMacAddress2,
       "gratuitousArpIpAddress3": gratuitousArpIpAddress3,
       "gratuitousArpMacAddress3": gratuitousArpMacAddress3,
       "gratuitousArpIpAddress4": gratuitousArpIpAddress4,
       "gratuitousArpMacAddress4": gratuitousArpMacAddress4,
       "portSetting": portSetting,
       "opModeSetting": opModeSetting,
       "opMode": opMode,
       "opModePortTable": opModePortTable,
       "opModePortEntry": opModePortEntry,
       "portIndex": portIndex,
       "portMode": portMode,
       "opModeParam": opModeParam,
       "realCOM": realCOM,
       "realCOMTable": realCOMTable,
       "realCOMEntry": realCOMEntry,
       "realCOMTcpAliveCheck": realCOMTcpAliveCheck,
       "realCOMMaxConnection": realCOMMaxConnection,
       "realCOMIgnoreJammedIp": realCOMIgnoreJammedIp,
       "realCOMAllowDriverControl": realCOMAllowDriverControl,
       "realCOMConnectionDownRTS": realCOMConnectionDownRTS,
       "realCOMConnectionDownDTR": realCOMConnectionDownDTR,
       "rfc2217": rfc2217,
       "rfc2217Table": rfc2217Table,
       "rfc2217Entry": rfc2217Entry,
       "rfc2217TcpAliveCheck": rfc2217TcpAliveCheck,
       "rfc2217TcpPort": rfc2217TcpPort,
       "tcpServer": tcpServer,
       "tcpServerTable": tcpServerTable,
       "tcpServerEntry": tcpServerEntry,
       "tcpServerTcpAliveCheck": tcpServerTcpAliveCheck,
       "tcpServerInactivityTime": tcpServerInactivityTime,
       "tcpServerMaxConnection": tcpServerMaxConnection,
       "tcpServerIgnoreJammedIp": tcpServerIgnoreJammedIp,
       "tcpServerAllowDriverControl": tcpServerAllowDriverControl,
       "tcpServerTcpPort": tcpServerTcpPort,
       "tcpServerCmdPort": tcpServerCmdPort,
       "tcpServerConnectionDownRTS": tcpServerConnectionDownRTS,
       "tcpServerConnectionDownDTR": tcpServerConnectionDownDTR,
       "tcpClient": tcpClient,
       "tcpClientTable": tcpClientTable,
       "tcpClientEntry": tcpClientEntry,
       "tcpClientTcpAliveCheck": tcpClientTcpAliveCheck,
       "tcpClientInactivityTime": tcpClientInactivityTime,
       "tcpClientIgnoreJammedIp": tcpClientIgnoreJammedIp,
       "tcpClientDestinationAddress1": tcpClientDestinationAddress1,
       "tcpClientDestinationPort1": tcpClientDestinationPort1,
       "tcpClientDestinationAddress2": tcpClientDestinationAddress2,
       "tcpClientDestinationPort2": tcpClientDestinationPort2,
       "tcpClientDestinationAddress3": tcpClientDestinationAddress3,
       "tcpClientDestinationPort3": tcpClientDestinationPort3,
       "tcpClientDestinationAddress4": tcpClientDestinationAddress4,
       "tcpClientDestinationPort4": tcpClientDestinationPort4,
       "tcpClientDesignatedLocalPort1": tcpClientDesignatedLocalPort1,
       "tcpClientDesignatedLocalPort2": tcpClientDesignatedLocalPort2,
       "tcpClientDesignatedLocalPort3": tcpClientDesignatedLocalPort3,
       "tcpClientDesignatedLocalPort4": tcpClientDesignatedLocalPort4,
       "tcpClientConnectionControl": tcpClientConnectionControl,
       "udp": udp,
       "udpTable": udpTable,
       "udpEntry": udpEntry,
       "udpDestinationAddress1Begin": udpDestinationAddress1Begin,
       "udpDestinationAddress1End": udpDestinationAddress1End,
       "udpDestinationPort1": udpDestinationPort1,
       "udpDestinationAddress2Begin": udpDestinationAddress2Begin,
       "udpDestinationAddress2End": udpDestinationAddress2End,
       "udpDestinationPort2": udpDestinationPort2,
       "udpDestinationAddress3Begin": udpDestinationAddress3Begin,
       "udpDestinationAddress3End": udpDestinationAddress3End,
       "udpDestinationPort3": udpDestinationPort3,
       "udpDestinationAddress4Begin": udpDestinationAddress4Begin,
       "udpDestinationAddress4End": udpDestinationAddress4End,
       "udpDestinationPort4": udpDestinationPort4,
       "udpLocalListenPort": udpLocalListenPort,
       "pairConnectionMaster": pairConnectionMaster,
       "pairConnectionMasterTable": pairConnectionMasterTable,
       "pairConnectionMasterEntry": pairConnectionMasterEntry,
       "pairConnectionMasterTcpAliveCheck": pairConnectionMasterTcpAliveCheck,
       "pairConnectionMasterDestnationAddress": pairConnectionMasterDestnationAddress,
       "pairConnectionMasterDestnationTcpPort": pairConnectionMasterDestnationTcpPort,
       "pairConnectionSlave": pairConnectionSlave,
       "pairConnectionSlaveTable": pairConnectionSlaveTable,
       "pairConnectionSlaveEntry": pairConnectionSlaveEntry,
       "pairConnectionSlaveTcpAliveCheck": pairConnectionSlaveTcpAliveCheck,
       "pairConnectionSlaveLocalTcpPort": pairConnectionSlaveLocalTcpPort,
       "ethernetModem": ethernetModem,
       "ethernetModemTable": ethernetModemTable,
       "ethernetModemEntry": ethernetModemEntry,
       "ethernetModemTcpAliveCheck": ethernetModemTcpAliveCheck,
       "ethernetModemLocalTcpPort": ethernetModemLocalTcpPort,
       "reverseTerminal": reverseTerminal,
       "reverseTerminalTable": reverseTerminalTable,
       "reverseTerminalEntry": reverseTerminalEntry,
       "reverseTerminalTcpAliveCheck": reverseTerminalTcpAliveCheck,
       "reverseTerminalInactivityTime": reverseTerminalInactivityTime,
       "reverseTerminalTcpPort": reverseTerminalTcpPort,
       "reverseTerminalAuthenticationType": reverseTerminalAuthenticationType,
       "reverseTerminalMapKeys": reverseTerminalMapKeys,
       "dataPacking": dataPacking,
       "dataPackingPortTable": dataPackingPortTable,
       "dataPackingPortEntry": dataPackingPortEntry,
       "portPacketLength": portPacketLength,
       "portDelimiter1Enable": portDelimiter1Enable,
       "portDelimiter1": portDelimiter1,
       "portDelimiter2Enable": portDelimiter2Enable,
       "portDelimiter2": portDelimiter2,
       "portDelimiterProcess": portDelimiterProcess,
       "portForceTransmit": portForceTransmit,
       "comParamSetting": comParamSetting,
       "comParamPortTable": comParamPortTable,
       "comParamPortEntry": comParamPortEntry,
       "portAlias": portAlias,
       "portInterface": portInterface,
       "portBaudRate": portBaudRate,
       "portDataBits": portDataBits,
       "portStopBits": portStopBits,
       "portParity": portParity,
       "portFlowControl": portFlowControl,
       "portFIFO": portFIFO,
       "dataBuffering": dataBuffering,
       "dataBufferingPortTable": dataBufferingPortTable,
       "dataBufferingPortEntry": dataBufferingPortEntry,
       "portBufferingEnable": portBufferingEnable,
       "portSerialDataLoggingEnable": portSerialDataLoggingEnable,
       "sysManagement": sysManagement,
       "miscNetworkSettings": miscNetworkSettings,
       "accessibleIp": accessibleIp,
       "enableAccessibleIpList": enableAccessibleIpList,
       "accessibleIpListTable": accessibleIpListTable,
       "accessibleIpListEntry": accessibleIpListEntry,
       "accessibleIpListIndex": accessibleIpListIndex,
       "activeAccessibleIpList": activeAccessibleIpList,
       "accessibleIpListAddress": accessibleIpListAddress,
       "accessibleIpListNetmask": accessibleIpListNetmask,
       "snmpAgentSettings": snmpAgentSettings,
       "snmpEnable": snmpEnable,
       "snmpContactName": snmpContactName,
       "snmpLocation": snmpLocation,
       "authenticationServer": authenticationServer,
       "radiusServerIp": radiusServerIp,
       "udpPortAuthenticationServer": udpPortAuthenticationServer,
       "radiusAccounting": radiusAccounting,
       "sysLogSettings": sysLogSettings,
       "sysLocalLog": sysLocalLog,
       "networkLocalLog": networkLocalLog,
       "configLocalLog": configLocalLog,
       "opModeLocalLog": opModeLocalLog,
       "autoWarningSettings": autoWarningSettings,
       "eventSettings": eventSettings,
       "mailWarningColdStart": mailWarningColdStart,
       "mailWarningWarmStart": mailWarningWarmStart,
       "mailWarningAuthFailure": mailWarningAuthFailure,
       "mailWarningIpChanged": mailWarningIpChanged,
       "mailWarningPasswordChanged": mailWarningPasswordChanged,
       "trapServerColdStart": trapServerColdStart,
       "trapServerWarmStart": trapServerWarmStart,
       "trapServerAuthFailure": trapServerAuthFailure,
       "serialEventSettings": serialEventSettings,
       "portEventSettingsTable": portEventSettingsTable,
       "portEventSettingsEntry": portEventSettingsEntry,
       "mailDCDchange": mailDCDchange,
       "trapDCDchange": trapDCDchange,
       "mailDSRchange": mailDSRchange,
       "trapDSRchange": trapDSRchange,
       "emailAlert": emailAlert,
       "emailWarningMailServer": emailWarningMailServer,
       "emailRequiresAuthentication": emailRequiresAuthentication,
       "emailWarningUserName": emailWarningUserName,
       "emailWarningFromEmail": emailWarningFromEmail,
       "emailWarningFirstEmailAddr": emailWarningFirstEmailAddr,
       "emailWarningSecondEmailAddr": emailWarningSecondEmailAddr,
       "emailWarningThirdEmailAddr": emailWarningThirdEmailAddr,
       "emailWarningFourthEmailAddr": emailWarningFourthEmailAddr,
       "snmpTrap": snmpTrap,
       "snmpTrapReceiverIp": snmpTrapReceiverIp,
       "trapVersion": trapVersion,
       "maintenance": maintenance,
       "consoleSettings": consoleSettings,
       "httpConsole": httpConsole,
       "httpsConsole": httpsConsole,
       "telnetConsole": telnetConsole,
       "sshConsole": sshConsole,
       "serialConsole": serialConsole,
       "resetButton": resetButton,
       "loadFactoryDefault": loadFactoryDefault,
       "loadFactoryDefaultSetting": loadFactoryDefaultSetting,
       "sysStatus": sysStatus,
       "s2eConnections": s2eConnections,
       "monitorRemoteIpTable": monitorRemoteIpTable,
       "monitorRemoteIpEntry": monitorRemoteIpEntry,
       "remoteIpIndex": remoteIpIndex,
       "monitorRemoteIp": monitorRemoteIp,
       "serialPortStatus": serialPortStatus,
       "monitorSerialPortStatusTable": monitorSerialPortStatusTable,
       "monitorSerialPortStatusEntry": monitorSerialPortStatusEntry,
       "monitorTxCount": monitorTxCount,
       "monitorRxCount": monitorRxCount,
       "monitorTxTotalCount": monitorTxTotalCount,
       "monitorRxTotalCount": monitorRxTotalCount,
       "monitorDSR": monitorDSR,
       "monitorDTR": monitorDTR,
       "monitorRTS": monitorRTS,
       "monitorCTS": monitorCTS,
       "monitorDCD": monitorDCD,
       "serialPortErrorCount": serialPortErrorCount,
       "monitorSerialPortErrorCountTable": monitorSerialPortErrorCountTable,
       "monitorSerialPortErrorCountEntry": monitorSerialPortErrorCountEntry,
       "monitorErrorCountFrame": monitorErrorCountFrame,
       "monitorErrorCountParity": monitorErrorCountParity,
       "monitorErrorCountOverrun": monitorErrorCountOverrun,
       "monitorErrorCountBreak": monitorErrorCountBreak,
       "serialPortSettings": serialPortSettings,
       "monitorSerialPortSettingsTable": monitorSerialPortSettingsTable,
       "monitorSerialPortSettingsEntry": monitorSerialPortSettingsEntry,
       "monitorBaudRate": monitorBaudRate,
       "monitorDataBits": monitorDataBits,
       "monitorStopBits": monitorStopBits,
       "monitorParity": monitorParity,
       "monitorRTSCTSFlowControl": monitorRTSCTSFlowControl,
       "monitorXONXOFFFlowControl": monitorXONXOFFFlowControl,
       "monitorFIFO": monitorFIFO,
       "monitorInterface": monitorInterface,
       "serialPortBuffering": serialPortBuffering,
       "monitorSerialPortBufferingTable": monitorSerialPortBufferingTable,
       "monitorSerialPortBufferingEntry": monitorSerialPortBufferingEntry,
       "monitorBuffering": monitorBuffering,
       "sysWlanStatus": sysWlanStatus,
       "wlanStatusActiveProfileName": wlanStatusActiveProfileName,
       "wlanStatusIpConfiguration": wlanStatusIpConfiguration,
       "wlanStatusIpAddress": wlanStatusIpAddress,
       "wlanStatusNetMask": wlanStatusNetMask,
       "wlanStatusDefaultGateway": wlanStatusDefaultGateway,
       "wlanStatusNetworkType": wlanStatusNetworkType,
       "wlanStatusRFType": wlanStatusRFType,
       "wlanStatusSSID": wlanStatusSSID,
       "wlanStatusChannel": wlanStatusChannel,
       "wlanStatusAuthentication": wlanStatusAuthentication,
       "wlanStatusEncryption": wlanStatusEncryption,
       "wlanStatusRegion": wlanStatusRegion,
       "wlanStatusSignalStrength": wlanStatusSignalStrength,
       "wlanStatusConnectionSpeed": wlanStatusConnectionSpeed,
       "wlanStatusCurrentBSSID": wlanStatusCurrentBSSID,
       "activateSettings": activateSettings,
       "doActivate": doActivate,
       "restart": restart,
       "restartPorts": restartPorts,
       "restartSystem": restartSystem}
)
