# SNMP MIB module (MOXA-CN2600-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOXA-CN2600-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:39 2024
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

cn2600 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11)
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1)
)
_Overview_ObjectIdentity = ObjectIdentity
overview = _Overview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1)
)
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 1),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_SerialNumber_Type = Integer32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 3),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_ViewLan1IpAddress_Type = IpAddress
_ViewLan1IpAddress_Object = MibScalar
viewLan1IpAddress = _ViewLan1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 4),
    _ViewLan1IpAddress_Type()
)
viewLan1IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLan1IpAddress.setStatus("current")
_ViewLan1MacAddress_Type = MacAddress
_ViewLan1MacAddress_Object = MibScalar
viewLan1MacAddress = _ViewLan1MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 5),
    _ViewLan1MacAddress_Type()
)
viewLan1MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLan1MacAddress.setStatus("current")
_ViewLan1Speed_Type = DisplayString
_ViewLan1Speed_Object = MibScalar
viewLan1Speed = _ViewLan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 6),
    _ViewLan1Speed_Type()
)
viewLan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLan1Speed.setStatus("current")
_ViewLan2IpAddress_Type = IpAddress
_ViewLan2IpAddress_Object = MibScalar
viewLan2IpAddress = _ViewLan2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 7),
    _ViewLan2IpAddress_Type()
)
viewLan2IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLan2IpAddress.setStatus("current")
_ViewLan2MacAddress_Type = MacAddress
_ViewLan2MacAddress_Object = MibScalar
viewLan2MacAddress = _ViewLan2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 8),
    _ViewLan2MacAddress_Type()
)
viewLan2MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLan2MacAddress.setStatus("current")
_ViewLan2Speed_Type = DisplayString
_ViewLan2Speed_Object = MibScalar
viewLan2Speed = _ViewLan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 9),
    _ViewLan2Speed_Type()
)
viewLan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewLan2Speed.setStatus("current")
_UpTime_Type = DisplayString
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 10),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")


class _Power1Status_Type(Integer32):
    """Custom type power1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("power-off", 0),
          ("power-on", 1))
    )


_Power1Status_Type.__name__ = "Integer32"
_Power1Status_Object = MibScalar
power1Status = _Power1Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 11),
    _Power1Status_Type()
)
power1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power1Status.setStatus("current")


class _Power2Status_Type(Integer32):
    """Custom type power2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("power-off", 0),
          ("power-on", 1))
    )


_Power2Status_Type.__name__ = "Integer32"
_Power2Status_Object = MibScalar
power2Status = _Power2Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 1, 12),
    _Power2Status_Type()
)
power2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power2Status.setStatus("current")
_BasicSetting_ObjectIdentity = ObjectIdentity
basicSetting = _BasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2)
)
_ServerSetting_ObjectIdentity = ObjectIdentity
serverSetting = _ServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 1)
)
_ServerName_Type = DisplayString
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverName.setStatus("current")
_ServerLocation_Type = DisplayString
_ServerLocation_Object = MibScalar
serverLocation = _ServerLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 1, 2),
    _ServerLocation_Type()
)
serverLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverLocation.setStatus("current")
_TimeSetting_ObjectIdentity = ObjectIdentity
timeSetting = _TimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 2)
)
_TimeZone_Type = Integer32
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 2, 1),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")
_LocalTime_Type = DateAndTime
_LocalTime_Object = MibScalar
localTime = _LocalTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 2, 2),
    _LocalTime_Type()
)
localTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTime.setStatus("current")
_TimeServer_Type = DisplayString
_TimeServer_Object = MibScalar
timeServer = _TimeServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 2, 2, 3),
    _TimeServer_Type()
)
timeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3)
)


class _Lan1IpConfiguration_Type(Integer32):
    """Custom type lan1IpConfiguration based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 1),
          ("dhcp-BOOTP", 2),
          ("pppoe", 4),
          ("static", 0))
    )


_Lan1IpConfiguration_Type.__name__ = "Integer32"
_Lan1IpConfiguration_Object = MibScalar
lan1IpConfiguration = _Lan1IpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 1),
    _Lan1IpConfiguration_Type()
)
lan1IpConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1IpConfiguration.setStatus("current")
_Lan1IpAddress_Type = IpAddress
_Lan1IpAddress_Object = MibScalar
lan1IpAddress = _Lan1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 2),
    _Lan1IpAddress_Type()
)
lan1IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1IpAddress.setStatus("current")
_Lan1NetMask_Type = IpAddress
_Lan1NetMask_Object = MibScalar
lan1NetMask = _Lan1NetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 3),
    _Lan1NetMask_Type()
)
lan1NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1NetMask.setStatus("current")
_Lan1DefaultGateway_Type = IpAddress
_Lan1DefaultGateway_Object = MibScalar
lan1DefaultGateway = _Lan1DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 4),
    _Lan1DefaultGateway_Type()
)
lan1DefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lan1DefaultGateway.setStatus("current")


class _Lan1Speed_Type(Integer32):
    """Custom type lan1Speed based on Integer32"""
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
        *(("auto-Negation", 0),
          ("hundredMbps-Full", 4),
          ("hundredMbps-Half", 3),
          ("tenMbps-Full", 2),
          ("tenMbps-Half", 1))
    )


_Lan1Speed_Type.__name__ = "Integer32"
_Lan1Speed_Object = MibScalar
lan1Speed = _Lan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 5),
    _Lan1Speed_Type()
)
lan1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1Speed.setStatus("current")
_Lan1PppoeUserAccount_Type = DisplayString
_Lan1PppoeUserAccount_Object = MibScalar
lan1PppoeUserAccount = _Lan1PppoeUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 6),
    _Lan1PppoeUserAccount_Type()
)
lan1PppoeUserAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1PppoeUserAccount.setStatus("current")
_Lan1PppoePassword_Type = DisplayString
_Lan1PppoePassword_Object = MibScalar
lan1PppoePassword = _Lan1PppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 7),
    _Lan1PppoePassword_Type()
)
lan1PppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1PppoePassword.setStatus("current")


class _Lan2IpConfiguration_Type(Integer32):
    """Custom type lan2IpConfiguration based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 1),
          ("dhcp-BOOTP", 2),
          ("pppoe", 4),
          ("static", 0))
    )


_Lan2IpConfiguration_Type.__name__ = "Integer32"
_Lan2IpConfiguration_Object = MibScalar
lan2IpConfiguration = _Lan2IpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 8),
    _Lan2IpConfiguration_Type()
)
lan2IpConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2IpConfiguration.setStatus("current")
_Lan2IpAddress_Type = IpAddress
_Lan2IpAddress_Object = MibScalar
lan2IpAddress = _Lan2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 9),
    _Lan2IpAddress_Type()
)
lan2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2IpAddress.setStatus("current")
_Lan2NetMask_Type = IpAddress
_Lan2NetMask_Object = MibScalar
lan2NetMask = _Lan2NetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 10),
    _Lan2NetMask_Type()
)
lan2NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2NetMask.setStatus("current")
_Lan2DefaultGateway_Type = IpAddress
_Lan2DefaultGateway_Object = MibScalar
lan2DefaultGateway = _Lan2DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 11),
    _Lan2DefaultGateway_Type()
)
lan2DefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lan2DefaultGateway.setStatus("current")


class _Lan2Speed_Type(Integer32):
    """Custom type lan2Speed based on Integer32"""
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
        *(("auto-Negation", 0),
          ("hundredMbps-Full", 4),
          ("hundredMbps-Half", 3),
          ("tenMbps-Full", 2),
          ("tenMbps-Half", 1))
    )


_Lan2Speed_Type.__name__ = "Integer32"
_Lan2Speed_Object = MibScalar
lan2Speed = _Lan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 12),
    _Lan2Speed_Type()
)
lan2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2Speed.setStatus("current")
_Lan2PppoeUserAccount_Type = DisplayString
_Lan2PppoeUserAccount_Object = MibScalar
lan2PppoeUserAccount = _Lan2PppoeUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 13),
    _Lan2PppoeUserAccount_Type()
)
lan2PppoeUserAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2PppoeUserAccount.setStatus("current")
_Lan2PppoePassword_Type = DisplayString
_Lan2PppoePassword_Object = MibScalar
lan2PppoePassword = _Lan2PppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 14),
    _Lan2PppoePassword_Type()
)
lan2PppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan2PppoePassword.setStatus("current")
_DnsServer1IpAddr_Type = IpAddress
_DnsServer1IpAddr_Object = MibScalar
dnsServer1IpAddr = _DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 15),
    _DnsServer1IpAddr_Type()
)
dnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1IpAddr.setStatus("current")
_DnsServer2IpAddr_Type = IpAddress
_DnsServer2IpAddr_Object = MibScalar
dnsServer2IpAddr = _DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 16),
    _DnsServer2IpAddr_Type()
)
dnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2IpAddr.setStatus("current")


class _WinsFunction_Type(Integer32):
    """Custom type winsFunction based on Integer32"""
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


_WinsFunction_Type.__name__ = "Integer32"
_WinsFunction_Object = MibScalar
winsFunction = _WinsFunction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 17),
    _WinsFunction_Type()
)
winsFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winsFunction.setStatus("current")
_WinsServer_Type = IpAddress
_WinsServer_Object = MibScalar
winsServer = _WinsServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 18),
    _WinsServer_Type()
)
winsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winsServer.setStatus("current")


class _RoutingProtocol_Type(Integer32):
    """Custom type routingProtocol based on Integer32"""
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
          ("rip-1", 1),
          ("rip-2", 2))
    )


_RoutingProtocol_Type.__name__ = "Integer32"
_RoutingProtocol_Object = MibScalar
routingProtocol = _RoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 19),
    _RoutingProtocol_Type()
)
routingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingProtocol.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 20),
    _GratuitousArp_Type()
)
gratuitousArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArp.setStatus("current")
_GratuitousArpSendPeriod_Type = Integer32
_GratuitousArpSendPeriod_Object = MibScalar
gratuitousArpSendPeriod = _GratuitousArpSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 3, 21),
    _GratuitousArpSendPeriod_Type()
)
gratuitousArpSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gratuitousArpSendPeriod.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4)
)
_OpModeSetting_ObjectIdentity = ObjectIdentity
opModeSetting = _OpModeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1)
)
_OpMode_ObjectIdentity = ObjectIdentity
opMode = _OpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 1)
)
_OpModePortTable_Object = MibTable
opModePortTable = _OpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    opModePortTable.setStatus("current")
_OpModePortEntry_Object = MibTableRow
opModePortEntry = _OpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 1, 1, 1)
)
opModePortEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    opModePortEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 1, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortApplication_Type(Integer32):
    """Custom type portApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("device-Control", 4),
          ("dial-InOut", 1),
          ("disable", 0),
          ("drdas", 9),
          ("redundant-Com", 5),
          ("reverse-Terminal", 3),
          ("socket", 11),
          ("terminal", 2))
    )


_PortApplication_Type.__name__ = "Integer32"
_PortApplication_Object = MibTableColumn
portApplication = _PortApplication_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 1, 1, 1, 2),
    _PortApplication_Type()
)
portApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portApplication.setStatus("current")


class _PortMode_Type(Integer32):
    """Custom type portMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              13,
              14,
              15,
              16,
              17,
              20,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("disable", 7),
          ("drdas-Real-Com", 23),
          ("drdas-Tcp-Server", 24),
          ("dynamic", 9),
          ("ppp", 6),
          ("pppd", 15),
          ("real-Com", 2),
          ("redundant-Com", 22),
          ("rfc-2217", 20),
          ("slip", 4),
          ("slipd", 5),
          ("tcp-Client", 13),
          ("tcp-Server", 10),
          ("telnetd", 8),
          ("term-ASC", 16),
          ("term-BIN", 17),
          ("udp", 14))
    )


_PortMode_Type.__name__ = "Integer32"
_PortMode_Object = MibTableColumn
portMode = _PortMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 1, 1, 1, 3),
    _PortMode_Type()
)
portMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMode.setStatus("current")
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2)
)
_DeviceControl_ObjectIdentity = ObjectIdentity
deviceControl = _DeviceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1)
)
_DeviceControlTable_Object = MibTable
deviceControlTable = _DeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deviceControlTable.setStatus("current")
_DeviceControlEntry_Object = MibTableRow
deviceControlEntry = _DeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1)
)
deviceControlEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    deviceControlEntry.setStatus("current")
_DeviceControlTcpAliveCheck_Type = Integer32
_DeviceControlTcpAliveCheck_Object = MibTableColumn
deviceControlTcpAliveCheck = _DeviceControlTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1, 1),
    _DeviceControlTcpAliveCheck_Type()
)
deviceControlTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlTcpAliveCheck.setStatus("current")
_DeviceControlMaxConnection_Type = Integer32
_DeviceControlMaxConnection_Object = MibTableColumn
deviceControlMaxConnection = _DeviceControlMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1, 2),
    _DeviceControlMaxConnection_Type()
)
deviceControlMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlMaxConnection.setStatus("current")


class _DeviceControlIgnoreJammedIp_Type(Integer32):
    """Custom type deviceControlIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DeviceControlIgnoreJammedIp_Type.__name__ = "Integer32"
_DeviceControlIgnoreJammedIp_Object = MibTableColumn
deviceControlIgnoreJammedIp = _DeviceControlIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1, 3),
    _DeviceControlIgnoreJammedIp_Type()
)
deviceControlIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlIgnoreJammedIp.setStatus("current")


class _DeviceControlAllowDriverControl_Type(Integer32):
    """Custom type deviceControlAllowDriverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DeviceControlAllowDriverControl_Type.__name__ = "Integer32"
_DeviceControlAllowDriverControl_Object = MibTableColumn
deviceControlAllowDriverControl = _DeviceControlAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1, 4),
    _DeviceControlAllowDriverControl_Type()
)
deviceControlAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlAllowDriverControl.setStatus("current")


class _DeviceControlConnectionDownRTS_Type(Integer32):
    """Custom type deviceControlConnectionDownRTS based on Integer32"""
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


_DeviceControlConnectionDownRTS_Type.__name__ = "Integer32"
_DeviceControlConnectionDownRTS_Object = MibTableColumn
deviceControlConnectionDownRTS = _DeviceControlConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1, 5),
    _DeviceControlConnectionDownRTS_Type()
)
deviceControlConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlConnectionDownRTS.setStatus("current")


class _DeviceControlConnectionDownDTR_Type(Integer32):
    """Custom type deviceControlConnectionDownDTR based on Integer32"""
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


_DeviceControlConnectionDownDTR_Type.__name__ = "Integer32"
_DeviceControlConnectionDownDTR_Object = MibTableColumn
deviceControlConnectionDownDTR = _DeviceControlConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 1, 1, 1, 6),
    _DeviceControlConnectionDownDTR_Type()
)
deviceControlConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceControlConnectionDownDTR.setStatus("current")
_Socket_ObjectIdentity = ObjectIdentity
socket = _Socket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2)
)
_SocketTable_Object = MibTable
socketTable = _SocketTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    socketTable.setStatus("current")
_SocketEntry_Object = MibTableRow
socketEntry = _SocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1)
)
socketEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    socketEntry.setStatus("current")
_SocketTcpAliveCheck_Type = Integer32
_SocketTcpAliveCheck_Object = MibTableColumn
socketTcpAliveCheck = _SocketTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 1),
    _SocketTcpAliveCheck_Type()
)
socketTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpAliveCheck.setStatus("current")
_SocketInactivityTime_Type = Integer32
_SocketInactivityTime_Object = MibTableColumn
socketInactivityTime = _SocketInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 2),
    _SocketInactivityTime_Type()
)
socketInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketInactivityTime.setStatus("current")
_SocketMaxConnection_Type = Integer32
_SocketMaxConnection_Object = MibTableColumn
socketMaxConnection = _SocketMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 3),
    _SocketMaxConnection_Type()
)
socketMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketMaxConnection.setStatus("current")


class _SocketIgnoreJammedIp_Type(Integer32):
    """Custom type socketIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SocketIgnoreJammedIp_Type.__name__ = "Integer32"
_SocketIgnoreJammedIp_Object = MibTableColumn
socketIgnoreJammedIp = _SocketIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 4),
    _SocketIgnoreJammedIp_Type()
)
socketIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketIgnoreJammedIp.setStatus("current")


class _SocketAllowDriverControl_Type(Integer32):
    """Custom type socketAllowDriverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SocketAllowDriverControl_Type.__name__ = "Integer32"
_SocketAllowDriverControl_Object = MibTableColumn
socketAllowDriverControl = _SocketAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 5),
    _SocketAllowDriverControl_Type()
)
socketAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketAllowDriverControl.setStatus("current")
_SocketTcpPort_Type = Integer32
_SocketTcpPort_Object = MibTableColumn
socketTcpPort = _SocketTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 6),
    _SocketTcpPort_Type()
)
socketTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpPort.setStatus("current")
_SocketCmdPort_Type = Integer32
_SocketCmdPort_Object = MibTableColumn
socketCmdPort = _SocketCmdPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 7),
    _SocketCmdPort_Type()
)
socketCmdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketCmdPort.setStatus("current")


class _SocketTcpServerConnectionDownRTS_Type(Integer32):
    """Custom type socketTcpServerConnectionDownRTS based on Integer32"""
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


_SocketTcpServerConnectionDownRTS_Type.__name__ = "Integer32"
_SocketTcpServerConnectionDownRTS_Object = MibTableColumn
socketTcpServerConnectionDownRTS = _SocketTcpServerConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 8),
    _SocketTcpServerConnectionDownRTS_Type()
)
socketTcpServerConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpServerConnectionDownRTS.setStatus("current")


class _SocketTcpServerConnectionDownDTR_Type(Integer32):
    """Custom type socketTcpServerConnectionDownDTR based on Integer32"""
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


_SocketTcpServerConnectionDownDTR_Type.__name__ = "Integer32"
_SocketTcpServerConnectionDownDTR_Object = MibTableColumn
socketTcpServerConnectionDownDTR = _SocketTcpServerConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 9),
    _SocketTcpServerConnectionDownDTR_Type()
)
socketTcpServerConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpServerConnectionDownDTR.setStatus("current")
_SocketTcpClientDestinationAddress1_Type = DisplayString
_SocketTcpClientDestinationAddress1_Object = MibTableColumn
socketTcpClientDestinationAddress1 = _SocketTcpClientDestinationAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 10),
    _SocketTcpClientDestinationAddress1_Type()
)
socketTcpClientDestinationAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress1.setStatus("current")
_SocketTcpClientDestinationPort1_Type = Integer32
_SocketTcpClientDestinationPort1_Object = MibTableColumn
socketTcpClientDestinationPort1 = _SocketTcpClientDestinationPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 11),
    _SocketTcpClientDestinationPort1_Type()
)
socketTcpClientDestinationPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort1.setStatus("current")
_SocketTcpClientDestinationAddress2_Type = DisplayString
_SocketTcpClientDestinationAddress2_Object = MibTableColumn
socketTcpClientDestinationAddress2 = _SocketTcpClientDestinationAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 12),
    _SocketTcpClientDestinationAddress2_Type()
)
socketTcpClientDestinationAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress2.setStatus("current")
_SocketTcpClientDestinationPort2_Type = Integer32
_SocketTcpClientDestinationPort2_Object = MibTableColumn
socketTcpClientDestinationPort2 = _SocketTcpClientDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 13),
    _SocketTcpClientDestinationPort2_Type()
)
socketTcpClientDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort2.setStatus("current")
_SocketTcpClientDestinationAddress3_Type = DisplayString
_SocketTcpClientDestinationAddress3_Object = MibTableColumn
socketTcpClientDestinationAddress3 = _SocketTcpClientDestinationAddress3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 14),
    _SocketTcpClientDestinationAddress3_Type()
)
socketTcpClientDestinationAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress3.setStatus("current")
_SocketTcpClientDestinationPort3_Type = Integer32
_SocketTcpClientDestinationPort3_Object = MibTableColumn
socketTcpClientDestinationPort3 = _SocketTcpClientDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 15),
    _SocketTcpClientDestinationPort3_Type()
)
socketTcpClientDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort3.setStatus("current")
_SocketTcpClientDestinationAddress4_Type = DisplayString
_SocketTcpClientDestinationAddress4_Object = MibTableColumn
socketTcpClientDestinationAddress4 = _SocketTcpClientDestinationAddress4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 16),
    _SocketTcpClientDestinationAddress4_Type()
)
socketTcpClientDestinationAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationAddress4.setStatus("current")
_SocketTcpClientDestinationPort4_Type = Integer32
_SocketTcpClientDestinationPort4_Object = MibTableColumn
socketTcpClientDestinationPort4 = _SocketTcpClientDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 17),
    _SocketTcpClientDestinationPort4_Type()
)
socketTcpClientDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDestinationPort4.setStatus("current")
_SocketTcpClientDesignatedLocalPort1_Type = Integer32
_SocketTcpClientDesignatedLocalPort1_Object = MibTableColumn
socketTcpClientDesignatedLocalPort1 = _SocketTcpClientDesignatedLocalPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 18),
    _SocketTcpClientDesignatedLocalPort1_Type()
)
socketTcpClientDesignatedLocalPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort1.setStatus("current")
_SocketTcpClientDesignatedLocalPort2_Type = Integer32
_SocketTcpClientDesignatedLocalPort2_Object = MibTableColumn
socketTcpClientDesignatedLocalPort2 = _SocketTcpClientDesignatedLocalPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 19),
    _SocketTcpClientDesignatedLocalPort2_Type()
)
socketTcpClientDesignatedLocalPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort2.setStatus("current")
_SocketTcpClientDesignatedLocalPort3_Type = Integer32
_SocketTcpClientDesignatedLocalPort3_Object = MibTableColumn
socketTcpClientDesignatedLocalPort3 = _SocketTcpClientDesignatedLocalPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 20),
    _SocketTcpClientDesignatedLocalPort3_Type()
)
socketTcpClientDesignatedLocalPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort3.setStatus("current")
_SocketTcpClientDesignatedLocalPort4_Type = Integer32
_SocketTcpClientDesignatedLocalPort4_Object = MibTableColumn
socketTcpClientDesignatedLocalPort4 = _SocketTcpClientDesignatedLocalPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 21),
    _SocketTcpClientDesignatedLocalPort4_Type()
)
socketTcpClientDesignatedLocalPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientDesignatedLocalPort4.setStatus("current")


class _SocketTcpClientConnectionControl_Type(Integer32):
    """Custom type socketTcpClientConnectionControl based on Integer32"""
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


_SocketTcpClientConnectionControl_Type.__name__ = "Integer32"
_SocketTcpClientConnectionControl_Object = MibTableColumn
socketTcpClientConnectionControl = _SocketTcpClientConnectionControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 22),
    _SocketTcpClientConnectionControl_Type()
)
socketTcpClientConnectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketTcpClientConnectionControl.setStatus("current")
_SocketUdpDestinationAddress1Begin_Type = IpAddress
_SocketUdpDestinationAddress1Begin_Object = MibTableColumn
socketUdpDestinationAddress1Begin = _SocketUdpDestinationAddress1Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 23),
    _SocketUdpDestinationAddress1Begin_Type()
)
socketUdpDestinationAddress1Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress1Begin.setStatus("current")
_SocketUdpDestinationAddress1End_Type = IpAddress
_SocketUdpDestinationAddress1End_Object = MibTableColumn
socketUdpDestinationAddress1End = _SocketUdpDestinationAddress1End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 24),
    _SocketUdpDestinationAddress1End_Type()
)
socketUdpDestinationAddress1End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress1End.setStatus("current")
_SocketUdpDestinationPort1_Type = Integer32
_SocketUdpDestinationPort1_Object = MibTableColumn
socketUdpDestinationPort1 = _SocketUdpDestinationPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 25),
    _SocketUdpDestinationPort1_Type()
)
socketUdpDestinationPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort1.setStatus("current")
_SocketUdpDestinationAddress2Begin_Type = IpAddress
_SocketUdpDestinationAddress2Begin_Object = MibTableColumn
socketUdpDestinationAddress2Begin = _SocketUdpDestinationAddress2Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 26),
    _SocketUdpDestinationAddress2Begin_Type()
)
socketUdpDestinationAddress2Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress2Begin.setStatus("current")
_SocketUdpDestinationAddress2End_Type = IpAddress
_SocketUdpDestinationAddress2End_Object = MibTableColumn
socketUdpDestinationAddress2End = _SocketUdpDestinationAddress2End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 27),
    _SocketUdpDestinationAddress2End_Type()
)
socketUdpDestinationAddress2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress2End.setStatus("current")
_SocketUdpDestinationPort2_Type = Integer32
_SocketUdpDestinationPort2_Object = MibTableColumn
socketUdpDestinationPort2 = _SocketUdpDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 28),
    _SocketUdpDestinationPort2_Type()
)
socketUdpDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort2.setStatus("current")
_SocketUdpDestinationAddress3Begin_Type = IpAddress
_SocketUdpDestinationAddress3Begin_Object = MibTableColumn
socketUdpDestinationAddress3Begin = _SocketUdpDestinationAddress3Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 29),
    _SocketUdpDestinationAddress3Begin_Type()
)
socketUdpDestinationAddress3Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress3Begin.setStatus("current")
_SocketUdpDestinationAddress3End_Type = IpAddress
_SocketUdpDestinationAddress3End_Object = MibTableColumn
socketUdpDestinationAddress3End = _SocketUdpDestinationAddress3End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 30),
    _SocketUdpDestinationAddress3End_Type()
)
socketUdpDestinationAddress3End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress3End.setStatus("current")
_SocketUdpDestinationPort3_Type = Integer32
_SocketUdpDestinationPort3_Object = MibTableColumn
socketUdpDestinationPort3 = _SocketUdpDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 31),
    _SocketUdpDestinationPort3_Type()
)
socketUdpDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort3.setStatus("current")
_SocketUdpDestinationAddress4Begin_Type = IpAddress
_SocketUdpDestinationAddress4Begin_Object = MibTableColumn
socketUdpDestinationAddress4Begin = _SocketUdpDestinationAddress4Begin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 32),
    _SocketUdpDestinationAddress4Begin_Type()
)
socketUdpDestinationAddress4Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress4Begin.setStatus("current")
_SocketUdpDestinationAddress4End_Type = IpAddress
_SocketUdpDestinationAddress4End_Object = MibTableColumn
socketUdpDestinationAddress4End = _SocketUdpDestinationAddress4End_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 33),
    _SocketUdpDestinationAddress4End_Type()
)
socketUdpDestinationAddress4End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationAddress4End.setStatus("current")
_SocketUdpDestinationPort4_Type = Integer32
_SocketUdpDestinationPort4_Object = MibTableColumn
socketUdpDestinationPort4 = _SocketUdpDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 34),
    _SocketUdpDestinationPort4_Type()
)
socketUdpDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpDestinationPort4.setStatus("current")
_SocketUdpLocalListenPort_Type = Integer32
_SocketUdpLocalListenPort_Object = MibTableColumn
socketUdpLocalListenPort = _SocketUdpLocalListenPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 2, 1, 1, 35),
    _SocketUdpLocalListenPort_Type()
)
socketUdpLocalListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketUdpLocalListenPort.setStatus("current")
_RedundantCom_ObjectIdentity = ObjectIdentity
redundantCom = _RedundantCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3)
)
_RedundantComTable_Object = MibTable
redundantComTable = _RedundantComTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    redundantComTable.setStatus("current")
_RedundantComEntry_Object = MibTableRow
redundantComEntry = _RedundantComEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1, 1)
)
redundantComEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    redundantComEntry.setStatus("current")
_RedundantComMaxConnection_Type = Integer32
_RedundantComMaxConnection_Object = MibTableColumn
redundantComMaxConnection = _RedundantComMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1, 1, 1),
    _RedundantComMaxConnection_Type()
)
redundantComMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantComMaxConnection.setStatus("current")


class _RedundantComIgnoreJammedIp_Type(Integer32):
    """Custom type redundantComIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RedundantComIgnoreJammedIp_Type.__name__ = "Integer32"
_RedundantComIgnoreJammedIp_Object = MibTableColumn
redundantComIgnoreJammedIp = _RedundantComIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1, 1, 2),
    _RedundantComIgnoreJammedIp_Type()
)
redundantComIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantComIgnoreJammedIp.setStatus("current")


class _RedundantComAllowDriverControl_Type(Integer32):
    """Custom type redundantComAllowDriverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RedundantComAllowDriverControl_Type.__name__ = "Integer32"
_RedundantComAllowDriverControl_Object = MibTableColumn
redundantComAllowDriverControl = _RedundantComAllowDriverControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1, 1, 3),
    _RedundantComAllowDriverControl_Type()
)
redundantComAllowDriverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantComAllowDriverControl.setStatus("current")


class _RedundantComConnectionDownRTS_Type(Integer32):
    """Custom type redundantComConnectionDownRTS based on Integer32"""
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


_RedundantComConnectionDownRTS_Type.__name__ = "Integer32"
_RedundantComConnectionDownRTS_Object = MibTableColumn
redundantComConnectionDownRTS = _RedundantComConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1, 1, 4),
    _RedundantComConnectionDownRTS_Type()
)
redundantComConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantComConnectionDownRTS.setStatus("current")


class _RedundantComConnectionDownDTR_Type(Integer32):
    """Custom type redundantComConnectionDownDTR based on Integer32"""
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


_RedundantComConnectionDownDTR_Type.__name__ = "Integer32"
_RedundantComConnectionDownDTR_Object = MibTableColumn
redundantComConnectionDownDTR = _RedundantComConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 3, 1, 1, 5),
    _RedundantComConnectionDownDTR_Type()
)
redundantComConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantComConnectionDownDTR.setStatus("current")
_Drdas_ObjectIdentity = ObjectIdentity
drdas = _Drdas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4)
)
_DrdasTable_Object = MibTable
drdasTable = _DrdasTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    drdasTable.setStatus("current")
_DrdasEntry_Object = MibTableRow
drdasEntry = _DrdasEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1)
)
drdasEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    drdasEntry.setStatus("current")
_DrdasTcpAliveCheck_Type = Integer32
_DrdasTcpAliveCheck_Object = MibTableColumn
drdasTcpAliveCheck = _DrdasTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 1),
    _DrdasTcpAliveCheck_Type()
)
drdasTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasTcpAliveCheck.setStatus("current")
_DrdasInactivityTime_Type = Integer32
_DrdasInactivityTime_Object = MibTableColumn
drdasInactivityTime = _DrdasInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 2),
    _DrdasInactivityTime_Type()
)
drdasInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasInactivityTime.setStatus("current")


class _DrdasIgnoreJammedIp_Type(Integer32):
    """Custom type drdasIgnoreJammedIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DrdasIgnoreJammedIp_Type.__name__ = "Integer32"
_DrdasIgnoreJammedIp_Object = MibTableColumn
drdasIgnoreJammedIp = _DrdasIgnoreJammedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 3),
    _DrdasIgnoreJammedIp_Type()
)
drdasIgnoreJammedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasIgnoreJammedIp.setStatus("current")
_DrdasPrimaryIpAddress_Type = IpAddress
_DrdasPrimaryIpAddress_Object = MibTableColumn
drdasPrimaryIpAddress = _DrdasPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 4),
    _DrdasPrimaryIpAddress_Type()
)
drdasPrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasPrimaryIpAddress.setStatus("current")
_DrdasBackup1IpAddress_Type = IpAddress
_DrdasBackup1IpAddress_Object = MibTableColumn
drdasBackup1IpAddress = _DrdasBackup1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 5),
    _DrdasBackup1IpAddress_Type()
)
drdasBackup1IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasBackup1IpAddress.setStatus("current")
_DrdasBackup2IpAddress_Type = IpAddress
_DrdasBackup2IpAddress_Object = MibTableColumn
drdasBackup2IpAddress = _DrdasBackup2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 6),
    _DrdasBackup2IpAddress_Type()
)
drdasBackup2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasBackup2IpAddress.setStatus("current")
_DrdasBackup3IpAddress_Type = IpAddress
_DrdasBackup3IpAddress_Object = MibTableColumn
drdasBackup3IpAddress = _DrdasBackup3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 7),
    _DrdasBackup3IpAddress_Type()
)
drdasBackup3IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasBackup3IpAddress.setStatus("current")
_DrdasTcpPort_Type = Integer32
_DrdasTcpPort_Object = MibTableColumn
drdasTcpPort = _DrdasTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 8),
    _DrdasTcpPort_Type()
)
drdasTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasTcpPort.setStatus("current")
_DrdasCmdPort_Type = Integer32
_DrdasCmdPort_Object = MibTableColumn
drdasCmdPort = _DrdasCmdPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 9),
    _DrdasCmdPort_Type()
)
drdasCmdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasCmdPort.setStatus("current")


class _DrdasConnectionDownRTS_Type(Integer32):
    """Custom type drdasConnectionDownRTS based on Integer32"""
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


_DrdasConnectionDownRTS_Type.__name__ = "Integer32"
_DrdasConnectionDownRTS_Object = MibTableColumn
drdasConnectionDownRTS = _DrdasConnectionDownRTS_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 10),
    _DrdasConnectionDownRTS_Type()
)
drdasConnectionDownRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasConnectionDownRTS.setStatus("current")


class _DrdasConnectionDownDTR_Type(Integer32):
    """Custom type drdasConnectionDownDTR based on Integer32"""
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


_DrdasConnectionDownDTR_Type.__name__ = "Integer32"
_DrdasConnectionDownDTR_Object = MibTableColumn
drdasConnectionDownDTR = _DrdasConnectionDownDTR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 4, 1, 1, 11),
    _DrdasConnectionDownDTR_Type()
)
drdasConnectionDownDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drdasConnectionDownDTR.setStatus("current")
_Terminal_ObjectIdentity = ObjectIdentity
terminal = _Terminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5)
)
_TerminalTable_Object = MibTable
terminalTable = _TerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    terminalTable.setStatus("current")
_TerminalEntry_Object = MibTableRow
terminalEntry = _TerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1)
)
terminalEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    terminalEntry.setStatus("current")
_TerminalTcpAliveCheck_Type = Integer32
_TerminalTcpAliveCheck_Object = MibTableColumn
terminalTcpAliveCheck = _TerminalTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 1),
    _TerminalTcpAliveCheck_Type()
)
terminalTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalTcpAliveCheck.setStatus("current")
_TerminalInactivityTime_Type = Integer32
_TerminalInactivityTime_Object = MibTableColumn
terminalInactivityTime = _TerminalInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 2),
    _TerminalInactivityTime_Type()
)
terminalInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalInactivityTime.setStatus("current")


class _TerminalAutoLinkProtocol_Type(Integer32):
    """Custom type terminalAutoLinkProtocol based on Integer32"""
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
          ("rlogin", 2),
          ("telnet", 1))
    )


_TerminalAutoLinkProtocol_Type.__name__ = "Integer32"
_TerminalAutoLinkProtocol_Object = MibTableColumn
terminalAutoLinkProtocol = _TerminalAutoLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 3),
    _TerminalAutoLinkProtocol_Type()
)
terminalAutoLinkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalAutoLinkProtocol.setStatus("current")


class _TerminalPrimaryHostAddress_Type(DisplayString):
    """Custom type terminalPrimaryHostAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TerminalPrimaryHostAddress_Type.__name__ = "DisplayString"
_TerminalPrimaryHostAddress_Object = MibTableColumn
terminalPrimaryHostAddress = _TerminalPrimaryHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 4),
    _TerminalPrimaryHostAddress_Type()
)
terminalPrimaryHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalPrimaryHostAddress.setStatus("current")


class _TerminalSecondHostAddress_Type(DisplayString):
    """Custom type terminalSecondHostAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TerminalSecondHostAddress_Type.__name__ = "DisplayString"
_TerminalSecondHostAddress_Object = MibTableColumn
terminalSecondHostAddress = _TerminalSecondHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 5),
    _TerminalSecondHostAddress_Type()
)
terminalSecondHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalSecondHostAddress.setStatus("current")
_TerminalTelnetTcpPort_Type = Integer32
_TerminalTelnetTcpPort_Object = MibTableColumn
terminalTelnetTcpPort = _TerminalTelnetTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 6),
    _TerminalTelnetTcpPort_Type()
)
terminalTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalTelnetTcpPort.setStatus("current")


class _TerminalType_Type(DisplayString):
    """Custom type terminalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TerminalType_Type.__name__ = "DisplayString"
_TerminalType_Object = MibTableColumn
terminalType = _TerminalType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 7),
    _TerminalType_Type()
)
terminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalType.setStatus("current")
_TerminalMaxSessions_Type = Integer32
_TerminalMaxSessions_Object = MibTableColumn
terminalMaxSessions = _TerminalMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 8),
    _TerminalMaxSessions_Type()
)
terminalMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalMaxSessions.setStatus("current")


class _TerminalChangeSession_Type(DisplayString):
    """Custom type terminalChangeSession based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalChangeSession_Type.__name__ = "DisplayString"
_TerminalChangeSession_Object = MibTableColumn
terminalChangeSession = _TerminalChangeSession_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 9),
    _TerminalChangeSession_Type()
)
terminalChangeSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalChangeSession.setStatus("current")


class _TerminalQuit_Type(DisplayString):
    """Custom type terminalQuit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalQuit_Type.__name__ = "DisplayString"
_TerminalQuit_Object = MibTableColumn
terminalQuit = _TerminalQuit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 10),
    _TerminalQuit_Type()
)
terminalQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalQuit.setStatus("current")


class _TerminalBreak_Type(DisplayString):
    """Custom type terminalBreak based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalBreak_Type.__name__ = "DisplayString"
_TerminalBreak_Object = MibTableColumn
terminalBreak = _TerminalBreak_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 11),
    _TerminalBreak_Type()
)
terminalBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalBreak.setStatus("current")


class _TerminalInterrupt_Type(DisplayString):
    """Custom type terminalInterrupt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TerminalInterrupt_Type.__name__ = "DisplayString"
_TerminalInterrupt_Object = MibTableColumn
terminalInterrupt = _TerminalInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 12),
    _TerminalInterrupt_Type()
)
terminalInterrupt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalInterrupt.setStatus("current")


class _TerminalAuthenticationType_Type(Integer32):
    """Custom type terminalAuthenticationType based on Integer32"""
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


_TerminalAuthenticationType_Type.__name__ = "Integer32"
_TerminalAuthenticationType_Object = MibTableColumn
terminalAuthenticationType = _TerminalAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 13),
    _TerminalAuthenticationType_Type()
)
terminalAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalAuthenticationType.setStatus("current")


class _TerminalAutoLoginPrompt_Type(DisplayString):
    """Custom type terminalAutoLoginPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalAutoLoginPrompt_Type.__name__ = "DisplayString"
_TerminalAutoLoginPrompt_Object = MibTableColumn
terminalAutoLoginPrompt = _TerminalAutoLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 14),
    _TerminalAutoLoginPrompt_Type()
)
terminalAutoLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalAutoLoginPrompt.setStatus("current")


class _TerminalPasswordPrompt_Type(DisplayString):
    """Custom type terminalPasswordPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalPasswordPrompt_Type.__name__ = "DisplayString"
_TerminalPasswordPrompt_Object = MibTableColumn
terminalPasswordPrompt = _TerminalPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 15),
    _TerminalPasswordPrompt_Type()
)
terminalPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalPasswordPrompt.setStatus("current")


class _TerminalLoginUserName_Type(DisplayString):
    """Custom type terminalLoginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalLoginUserName_Type.__name__ = "DisplayString"
_TerminalLoginUserName_Object = MibTableColumn
terminalLoginUserName = _TerminalLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 16),
    _TerminalLoginUserName_Type()
)
terminalLoginUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalLoginUserName.setStatus("current")


class _TerminalLoginPassword_Type(DisplayString):
    """Custom type terminalLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TerminalLoginPassword_Type.__name__ = "DisplayString"
_TerminalLoginPassword_Object = MibTableColumn
terminalLoginPassword = _TerminalLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 5, 1, 1, 17),
    _TerminalLoginPassword_Type()
)
terminalLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalLoginPassword.setStatus("current")
_ReverseTerminal_ObjectIdentity = ObjectIdentity
reverseTerminal = _ReverseTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6)
)
_ReverseTerminalTable_Object = MibTable
reverseTerminalTable = _ReverseTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    reverseTerminalTable.setStatus("current")
_ReverseTerminalEntry_Object = MibTableRow
reverseTerminalEntry = _ReverseTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1, 1)
)
reverseTerminalEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    reverseTerminalEntry.setStatus("current")
_ReverseTerminalTcpAliveCheck_Type = Integer32
_ReverseTerminalTcpAliveCheck_Object = MibTableColumn
reverseTerminalTcpAliveCheck = _ReverseTerminalTcpAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1, 1, 1),
    _ReverseTerminalTcpAliveCheck_Type()
)
reverseTerminalTcpAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalTcpAliveCheck.setStatus("current")
_ReverseTerminalInactivityTime_Type = Integer32
_ReverseTerminalInactivityTime_Object = MibTableColumn
reverseTerminalInactivityTime = _ReverseTerminalInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1, 1, 2),
    _ReverseTerminalInactivityTime_Type()
)
reverseTerminalInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalInactivityTime.setStatus("current")
_ReverseTerminalTcpPort_Type = Integer32
_ReverseTerminalTcpPort_Object = MibTableColumn
reverseTerminalTcpPort = _ReverseTerminalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 6, 1, 1, 5),
    _ReverseTerminalMapKeys_Type()
)
reverseTerminalMapKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reverseTerminalMapKeys.setStatus("current")
_Dial_ObjectIdentity = ObjectIdentity
dial = _Dial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7)
)
_DialTable_Object = MibTable
dialTable = _DialTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dialTable.setStatus("current")
_DialEntry_Object = MibTableRow
dialEntry = _DialEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1)
)
dialEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dialEntry.setStatus("current")


class _DialTERMBINMode_Type(Integer32):
    """Custom type dialTERMBINMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DialTERMBINMode_Type.__name__ = "Integer32"
_DialTERMBINMode_Object = MibTableColumn
dialTERMBINMode = _DialTERMBINMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 1),
    _DialTERMBINMode_Type()
)
dialTERMBINMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialTERMBINMode.setStatus("current")


class _DialPPPDMode_Type(Integer32):
    """Custom type dialPPPDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DialPPPDMode_Type.__name__ = "Integer32"
_DialPPPDMode_Object = MibTableColumn
dialPPPDMode = _DialPPPDMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 2),
    _DialPPPDMode_Type()
)
dialPPPDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPPPDMode.setStatus("current")


class _DialSLIPDMode_Type(Integer32):
    """Custom type dialSLIPDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DialSLIPDMode_Type.__name__ = "Integer32"
_DialSLIPDMode_Object = MibTableColumn
dialSLIPDMode = _DialSLIPDMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 3),
    _DialSLIPDMode_Type()
)
dialSLIPDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialSLIPDMode.setStatus("current")


class _DialAuthType_Type(Integer32):
    """Custom type dialAuthType based on Integer32"""
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


_DialAuthType_Type.__name__ = "Integer32"
_DialAuthType_Object = MibTableColumn
dialAuthType = _DialAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 4),
    _DialAuthType_Type()
)
dialAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialAuthType.setStatus("current")


class _DialDisconnectBy_Type(Integer32):
    """Custom type dialDisconnectBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dcd-off", 2),
          ("dsr-off", 4),
          ("none", 0))
    )


_DialDisconnectBy_Type.__name__ = "Integer32"
_DialDisconnectBy_Object = MibTableColumn
dialDisconnectBy = _DialDisconnectBy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 5),
    _DialDisconnectBy_Type()
)
dialDisconnectBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialDisconnectBy.setStatus("current")
_DialDestinationIpAddress_Type = IpAddress
_DialDestinationIpAddress_Object = MibTableColumn
dialDestinationIpAddress = _DialDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 6),
    _DialDestinationIpAddress_Type()
)
dialDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialDestinationIpAddress.setStatus("current")
_DialSourceIpAddress_Type = IpAddress
_DialSourceIpAddress_Object = MibTableColumn
dialSourceIpAddress = _DialSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 7),
    _DialSourceIpAddress_Type()
)
dialSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialSourceIpAddress.setStatus("current")
_DialIpNetmask_Type = IpAddress
_DialIpNetmask_Object = MibTableColumn
dialIpNetmask = _DialIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 8),
    _DialIpNetmask_Type()
)
dialIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialIpNetmask.setStatus("current")


class _DialTcpIpCompression_Type(Integer32):
    """Custom type dialTcpIpCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DialTcpIpCompression_Type.__name__ = "Integer32"
_DialTcpIpCompression_Object = MibTableColumn
dialTcpIpCompression = _DialTcpIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 9),
    _DialTcpIpCompression_Type()
)
dialTcpIpCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialTcpIpCompression.setStatus("current")
_DialInactivityTime_Type = Integer32
_DialInactivityTime_Object = MibTableColumn
dialInactivityTime = _DialInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 10),
    _DialInactivityTime_Type()
)
dialInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialInactivityTime.setStatus("current")


class _DialLinkQualityReport_Type(Integer32):
    """Custom type dialLinkQualityReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DialLinkQualityReport_Type.__name__ = "Integer32"
_DialLinkQualityReport_Object = MibTableColumn
dialLinkQualityReport = _DialLinkQualityReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 11),
    _DialLinkQualityReport_Type()
)
dialLinkQualityReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialLinkQualityReport.setStatus("current")
_DialOutgoingPAPID_Type = DisplayString
_DialOutgoingPAPID_Object = MibTableColumn
dialOutgoingPAPID = _DialOutgoingPAPID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 12),
    _DialOutgoingPAPID_Type()
)
dialOutgoingPAPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialOutgoingPAPID.setStatus("current")
_DialPAPPassword_Type = DisplayString
_DialPAPPassword_Object = MibTableColumn
dialPAPPassword = _DialPAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 13),
    _DialPAPPassword_Type()
)
dialPAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPAPPassword.setStatus("current")


class _DialIncomingPAPCheck_Type(Integer32):
    """Custom type dialIncomingPAPCheck based on Integer32"""
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


_DialIncomingPAPCheck_Type.__name__ = "Integer32"
_DialIncomingPAPCheck_Object = MibTableColumn
dialIncomingPAPCheck = _DialIncomingPAPCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 2, 7, 1, 1, 14),
    _DialIncomingPAPCheck_Type()
)
dialIncomingPAPCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialIncomingPAPCheck.setStatus("current")
_DataPacking_ObjectIdentity = ObjectIdentity
dataPacking = _DataPacking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3)
)
_DataPackingPortTable_Object = MibTable
dataPackingPortTable = _DataPackingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dataPackingPortTable.setStatus("current")
_DataPackingPortEntry_Object = MibTableRow
dataPackingPortEntry = _DataPackingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1)
)
dataPackingPortEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dataPackingPortEntry.setStatus("current")
_PortPacketLength_Type = Integer32
_PortPacketLength_Object = MibTableColumn
portPacketLength = _PortPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 6),
    _PortDelimiterProcess_Type()
)
portDelimiterProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDelimiterProcess.setStatus("current")
_PortForceTransmit_Type = Integer32
_PortForceTransmit_Object = MibTableColumn
portForceTransmit = _PortForceTransmit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 1, 3, 1, 1, 7),
    _PortForceTransmit_Type()
)
portForceTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForceTransmit.setStatus("current")
_ComParamSetting_ObjectIdentity = ObjectIdentity
comParamSetting = _ComParamSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2)
)
_ComParamPortTable_Object = MibTable
comParamPortTable = _ComParamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    comParamPortTable.setStatus("current")
_ComParamPortEntry_Object = MibTableRow
comParamPortEntry = _ComParamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1)
)
comParamPortEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 1),
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
          ("rs-485-2-wire", 2),
          ("rs-485-4-wire", 3))
    )


_PortInterface_Type.__name__ = "Integer32"
_PortInterface_Object = MibTableColumn
portInterface = _PortInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 2),
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
          ("b7200", 11),
          ("b75", 1),
          ("b921600", 19),
          ("b9600", 12))
    )


_PortBaudRate_Type.__name__ = "Integer32"
_PortBaudRate_Object = MibTableColumn
portBaudRate = _PortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 3),
    _PortBaudRate_Type()
)
portBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaudRate.setStatus("current")
_PortBaudRateManual_Type = Integer32
_PortBaudRateManual_Object = MibTableColumn
portBaudRateManual = _PortBaudRateManual_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 4),
    _PortBaudRateManual_Type()
)
portBaudRateManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaudRateManual.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 6),
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
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("mark", 3),
          ("none", 0),
          ("odd", 1),
          ("space", 4))
    )


_PortParity_Type.__name__ = "Integer32"
_PortParity_Object = MibTableColumn
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 7),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtr-dsr", 3),
          ("none", 0),
          ("rts-cts", 1),
          ("xon-xoff", 2))
    )


_PortFlowControl_Type.__name__ = "Integer32"
_PortFlowControl_Object = MibTableColumn
portFlowControl = _PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 2, 1, 1, 9),
    _PortFIFO_Type()
)
portFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFIFO.setStatus("current")
_DataBuffering_ObjectIdentity = ObjectIdentity
dataBuffering = _DataBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 3)
)
_DataBufferingPortTable_Object = MibTable
dataBufferingPortTable = _DataBufferingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dataBufferingPortTable.setStatus("current")
_DataBufferingPortEntry_Object = MibTableRow
dataBufferingPortEntry = _DataBufferingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 3, 1, 1)
)
dataBufferingPortEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
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
        *(("no", 0),
          ("yes", 1))
    )


_PortBufferingEnable_Type.__name__ = "Integer32"
_PortBufferingEnable_Object = MibTableColumn
portBufferingEnable = _PortBufferingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 3, 1, 1, 1),
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
        *(("no", 0),
          ("yes", 1))
    )


_PortSerialDataLoggingEnable_Type.__name__ = "Integer32"
_PortSerialDataLoggingEnable_Object = MibTableColumn
portSerialDataLoggingEnable = _PortSerialDataLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 3, 1, 1, 2),
    _PortSerialDataLoggingEnable_Type()
)
portSerialDataLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSerialDataLoggingEnable.setStatus("current")
_ModemSettings_ObjectIdentity = ObjectIdentity
modemSettings = _ModemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4)
)
_ModemSettingsPortTable_Object = MibTable
modemSettingsPortTable = _ModemSettingsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    modemSettingsPortTable.setStatus("current")
_ModemSettingsPortEntry_Object = MibTableRow
modemSettingsPortEntry = _ModemSettingsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4, 1, 1)
)
modemSettingsPortEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    modemSettingsPortEntry.setStatus("current")


class _PortEnableModem_Type(Integer32):
    """Custom type portEnableModem based on Integer32"""
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


_PortEnableModem_Type.__name__ = "Integer32"
_PortEnableModem_Object = MibTableColumn
portEnableModem = _PortEnableModem_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4, 1, 1, 1),
    _PortEnableModem_Type()
)
portEnableModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnableModem.setStatus("current")


class _PortInitialString_Type(DisplayString):
    """Custom type portInitialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PortInitialString_Type.__name__ = "DisplayString"
_PortInitialString_Object = MibTableColumn
portInitialString = _PortInitialString_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4, 1, 1, 2),
    _PortInitialString_Type()
)
portInitialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInitialString.setStatus("current")


class _PortDialUp_Type(DisplayString):
    """Custom type portDialUp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortDialUp_Type.__name__ = "DisplayString"
_PortDialUp_Object = MibTableColumn
portDialUp = _PortDialUp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4, 1, 1, 3),
    _PortDialUp_Type()
)
portDialUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDialUp.setStatus("current")


class _PortPhoneNumber_Type(DisplayString):
    """Custom type portPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortPhoneNumber_Type.__name__ = "DisplayString"
_PortPhoneNumber_Object = MibTableColumn
portPhoneNumber = _PortPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 4, 1, 1, 4),
    _PortPhoneNumber_Type()
)
portPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhoneNumber.setStatus("current")
_WelcomeMessage_ObjectIdentity = ObjectIdentity
welcomeMessage = _WelcomeMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 5)
)


class _PortEnableWelcomeMessage_Type(Integer32):
    """Custom type portEnableWelcomeMessage based on Integer32"""
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


_PortEnableWelcomeMessage_Type.__name__ = "Integer32"
_PortEnableWelcomeMessage_Object = MibScalar
portEnableWelcomeMessage = _PortEnableWelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 5, 1),
    _PortEnableWelcomeMessage_Type()
)
portEnableWelcomeMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnableWelcomeMessage.setStatus("current")


class _PortMessage_Type(DisplayString):
    """Custom type portMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1280),
    )


_PortMessage_Type.__name__ = "DisplayString"
_PortMessage_Object = MibScalar
portMessage = _PortMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 4, 5, 2),
    _PortMessage_Type()
)
portMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMessage.setStatus("current")
_SysManagement_ObjectIdentity = ObjectIdentity
sysManagement = _SysManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5)
)
_MiscNetworkSettings_ObjectIdentity = ObjectIdentity
miscNetworkSettings = _MiscNetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1)
)
_AccessibleIp_ObjectIdentity = ObjectIdentity
accessibleIp = _AccessibleIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 1),
    _EnableAccessibleIpList_Type()
)
enableAccessibleIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAccessibleIpList.setStatus("current")
_AccessibleIpListTable_Object = MibTable
accessibleIpListTable = _AccessibleIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    accessibleIpListTable.setStatus("current")
_AccessibleIpListEntry_Object = MibTableRow
accessibleIpListEntry = _AccessibleIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 2, 1)
)
accessibleIpListEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "activeAccessibleIpList"),
)
if mibBuilder.loadTexts:
    accessibleIpListEntry.setStatus("current")
_AccessibleIpListIndex_Type = Integer32
_AccessibleIpListIndex_Object = MibTableColumn
accessibleIpListIndex = _AccessibleIpListIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 2, 1, 2),
    _ActiveAccessibleIpList_Type()
)
activeAccessibleIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAccessibleIpList.setStatus("current")
_AccessibleIpListAddress_Type = IpAddress
_AccessibleIpListAddress_Object = MibTableColumn
accessibleIpListAddress = _AccessibleIpListAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 2, 1, 3),
    _AccessibleIpListAddress_Type()
)
accessibleIpListAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessibleIpListAddress.setStatus("current")
_AccessibleIpListNetmask_Type = IpAddress
_AccessibleIpListNetmask_Object = MibTableColumn
accessibleIpListNetmask = _AccessibleIpListNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 1, 2, 1, 4),
    _AccessibleIpListNetmask_Type()
)
accessibleIpListNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessibleIpListNetmask.setStatus("current")
_SnmpAgentSettings_ObjectIdentity = ObjectIdentity
snmpAgentSettings = _SnmpAgentSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 2, 3),
    _SnmpLocation_Type()
)
snmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLocation.setStatus("current")
_DDNS_ObjectIdentity = ObjectIdentity
dDNS = _DDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 3)
)


class _DDNSEnable_Type(Integer32):
    """Custom type dDNSEnable based on Integer32"""
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


_DDNSEnable_Type.__name__ = "Integer32"
_DDNSEnable_Object = MibScalar
dDNSEnable = _DDNSEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 3, 1),
    _DDNSEnable_Type()
)
dDNSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSEnable.setStatus("current")


class _DDNSServerAddress_Type(Integer32):
    """Custom type dDNSServerAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("dynDns-org", 0)
    )


_DDNSServerAddress_Type.__name__ = "Integer32"
_DDNSServerAddress_Object = MibScalar
dDNSServerAddress = _DDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 3, 2),
    _DDNSServerAddress_Type()
)
dDNSServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSServerAddress.setStatus("current")


class _DDNSHostName_Type(DisplayString):
    """Custom type dDNSHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DDNSHostName_Type.__name__ = "DisplayString"
_DDNSHostName_Object = MibScalar
dDNSHostName = _DDNSHostName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 3, 3),
    _DDNSHostName_Type()
)
dDNSHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSHostName.setStatus("current")


class _DDNSUserName_Type(DisplayString):
    """Custom type dDNSUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DDNSUserName_Type.__name__ = "DisplayString"
_DDNSUserName_Object = MibScalar
dDNSUserName = _DDNSUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 3, 4),
    _DDNSUserName_Type()
)
dDNSUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSUserName.setStatus("current")


class _DDNSPassword_Type(DisplayString):
    """Custom type dDNSPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DDNSPassword_Type.__name__ = "DisplayString"
_DDNSPassword_Object = MibScalar
dDNSPassword = _DDNSPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 3, 5),
    _DDNSPassword_Type()
)
dDNSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDNSPassword.setStatus("current")
_HostTable_ObjectIdentity = ObjectIdentity
hostTable = _HostTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 4)
)
_HostTableTable_Object = MibTable
hostTableTable = _HostTableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hostTableTable.setStatus("current")
_HostTableEntry_Object = MibTableRow
hostTableEntry = _HostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 4, 1, 1)
)
hostTableEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "hostTableIndex"),
)
if mibBuilder.loadTexts:
    hostTableEntry.setStatus("current")
_HostTableIndex_Type = Integer32
_HostTableIndex_Object = MibTableColumn
hostTableIndex = _HostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 4, 1, 1, 1),
    _HostTableIndex_Type()
)
hostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTableIndex.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 4, 1, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_HostIpAddress_Type = IpAddress
_HostIpAddress_Object = MibTableColumn
hostIpAddress = _HostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 4, 1, 1, 3),
    _HostIpAddress_Type()
)
hostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIpAddress.setStatus("current")
_RouteTable_ObjectIdentity = ObjectIdentity
routeTable = _RouteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5)
)
_RouteTableTable_Object = MibTable
routeTableTable = _RouteTableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    routeTableTable.setStatus("current")
_RouteTableEntry_Object = MibTableRow
routeTableEntry = _RouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1)
)
routeTableEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "routeTableIndex"),
)
if mibBuilder.loadTexts:
    routeTableEntry.setStatus("current")
_RouteTableIndex_Type = Integer32
_RouteTableIndex_Object = MibTableColumn
routeTableIndex = _RouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1, 1),
    _RouteTableIndex_Type()
)
routeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeTableIndex.setStatus("current")
_GatewayRouteTable_Type = IpAddress
_GatewayRouteTable_Object = MibTableColumn
gatewayRouteTable = _GatewayRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1, 2),
    _GatewayRouteTable_Type()
)
gatewayRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayRouteTable.setStatus("current")
_DestinationRouteTable_Type = IpAddress
_DestinationRouteTable_Object = MibTableColumn
destinationRouteTable = _DestinationRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1, 3),
    _DestinationRouteTable_Type()
)
destinationRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationRouteTable.setStatus("current")
_NetmaskRouteTable_Type = IpAddress
_NetmaskRouteTable_Object = MibTableColumn
netmaskRouteTable = _NetmaskRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1, 4),
    _NetmaskRouteTable_Type()
)
netmaskRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netmaskRouteTable.setStatus("current")
_MetricRouteTable_Type = Integer32
_MetricRouteTable_Object = MibTableColumn
metricRouteTable = _MetricRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1, 5),
    _MetricRouteTable_Type()
)
metricRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metricRouteTable.setStatus("current")


class _InterfaceRouteTable_Type(Integer32):
    """Custom type interfaceRouteTable based on Integer32"""
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
              256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 256),
          ("lan2", 257),
          ("port1", 0),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8))
    )


_InterfaceRouteTable_Type.__name__ = "Integer32"
_InterfaceRouteTable_Object = MibTableColumn
interfaceRouteTable = _InterfaceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 5, 1, 1, 6),
    _InterfaceRouteTable_Type()
)
interfaceRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceRouteTable.setStatus("current")
_UserTable_ObjectIdentity = ObjectIdentity
userTable = _UserTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6)
)
_UserTableTable_Object = MibTable
userTableTable = _UserTableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6, 1)
)
if mibBuilder.loadTexts:
    userTableTable.setStatus("current")
_UserTableEntry_Object = MibTableRow
userTableEntry = _UserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6, 1, 1)
)
userTableEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "userTableIndex"),
)
if mibBuilder.loadTexts:
    userTableEntry.setStatus("current")
_UserTableIndex_Type = Integer32
_UserTableIndex_Object = MibTableColumn
userTableIndex = _UserTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6, 1, 1, 1),
    _UserTableIndex_Type()
)
userTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTableIndex.setStatus("current")


class _UserNameUserTable_Type(DisplayString):
    """Custom type userNameUserTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UserNameUserTable_Type.__name__ = "DisplayString"
_UserNameUserTable_Object = MibTableColumn
userNameUserTable = _UserNameUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6, 1, 1, 2),
    _UserNameUserTable_Type()
)
userNameUserTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userNameUserTable.setStatus("current")


class _PasswordUserTable_Type(DisplayString):
    """Custom type passwordUserTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PasswordUserTable_Type.__name__ = "DisplayString"
_PasswordUserTable_Object = MibTableColumn
passwordUserTable = _PasswordUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6, 1, 1, 3),
    _PasswordUserTable_Type()
)
passwordUserTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordUserTable.setStatus("current")


class _PhoneNumberUserTable_Type(DisplayString):
    """Custom type phoneNumberUserTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhoneNumberUserTable_Type.__name__ = "DisplayString"
_PhoneNumberUserTable_Object = MibTableColumn
phoneNumberUserTable = _PhoneNumberUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 6, 1, 1, 4),
    _PhoneNumberUserTable_Type()
)
phoneNumberUserTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneNumberUserTable.setStatus("current")
_AuthenticationServer_ObjectIdentity = ObjectIdentity
authenticationServer = _AuthenticationServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 7)
)
_RadiusServerIp_Type = DisplayString
_RadiusServerIp_Object = MibScalar
radiusServerIp = _RadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 7, 1),
    _RadiusServerIp_Type()
)
radiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIp.setStatus("current")


class _RadiusKey_Type(DisplayString):
    """Custom type radiusKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RadiusKey_Type.__name__ = "DisplayString"
_RadiusKey_Object = MibScalar
radiusKey = _RadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 7, 2),
    _RadiusKey_Type()
)
radiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusKey.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 7, 4),
    _RadiusAccounting_Type()
)
radiusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccounting.setStatus("current")
_SysLogSettings_ObjectIdentity = ObjectIdentity
sysLogSettings = _SysLogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 8)
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 8, 3),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 1, 8, 4),
    _OpModeLocalLog_Type()
)
opModeLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opModeLocalLog.setStatus("current")
_AutoWarningSettings_ObjectIdentity = ObjectIdentity
autoWarningSettings = _AutoWarningSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2)
)
_EventSettings_ObjectIdentity = ObjectIdentity
eventSettings = _EventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 2),
    _MailWarningWarmStart_Type()
)
mailWarningWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningWarmStart.setStatus("current")


class _MailWarningPower1Down_Type(Integer32):
    """Custom type mailWarningPower1Down based on Integer32"""
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


_MailWarningPower1Down_Type.__name__ = "Integer32"
_MailWarningPower1Down_Object = MibScalar
mailWarningPower1Down = _MailWarningPower1Down_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 3),
    _MailWarningPower1Down_Type()
)
mailWarningPower1Down.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningPower1Down.setStatus("current")


class _MailWarningPower2Down_Type(Integer32):
    """Custom type mailWarningPower2Down based on Integer32"""
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


_MailWarningPower2Down_Type.__name__ = "Integer32"
_MailWarningPower2Down_Object = MibScalar
mailWarningPower2Down = _MailWarningPower2Down_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 4),
    _MailWarningPower2Down_Type()
)
mailWarningPower2Down.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningPower2Down.setStatus("current")


class _MailWarningEthernet1LinkDown_Type(Integer32):
    """Custom type mailWarningEthernet1LinkDown based on Integer32"""
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


_MailWarningEthernet1LinkDown_Type.__name__ = "Integer32"
_MailWarningEthernet1LinkDown_Object = MibScalar
mailWarningEthernet1LinkDown = _MailWarningEthernet1LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 5),
    _MailWarningEthernet1LinkDown_Type()
)
mailWarningEthernet1LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningEthernet1LinkDown.setStatus("current")


class _MailWarningEthernet2LinkDown_Type(Integer32):
    """Custom type mailWarningEthernet2LinkDown based on Integer32"""
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


_MailWarningEthernet2LinkDown_Type.__name__ = "Integer32"
_MailWarningEthernet2LinkDown_Object = MibScalar
mailWarningEthernet2LinkDown = _MailWarningEthernet2LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 6),
    _MailWarningEthernet2LinkDown_Type()
)
mailWarningEthernet2LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailWarningEthernet2LinkDown.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 11),
    _TrapServerWarmStart_Type()
)
trapServerWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerWarmStart.setStatus("current")


class _TrapServerEthernet1LinkDown_Type(Integer32):
    """Custom type trapServerEthernet1LinkDown based on Integer32"""
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


_TrapServerEthernet1LinkDown_Type.__name__ = "Integer32"
_TrapServerEthernet1LinkDown_Object = MibScalar
trapServerEthernet1LinkDown = _TrapServerEthernet1LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 12),
    _TrapServerEthernet1LinkDown_Type()
)
trapServerEthernet1LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerEthernet1LinkDown.setStatus("current")


class _TrapServerEthernet2LinkDown_Type(Integer32):
    """Custom type trapServerEthernet2LinkDown based on Integer32"""
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


_TrapServerEthernet2LinkDown_Type.__name__ = "Integer32"
_TrapServerEthernet2LinkDown_Object = MibScalar
trapServerEthernet2LinkDown = _TrapServerEthernet2LinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 13),
    _TrapServerEthernet2LinkDown_Type()
)
trapServerEthernet2LinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerEthernet2LinkDown.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 1, 14),
    _TrapServerAuthFailure_Type()
)
trapServerAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerAuthFailure.setStatus("current")
_SerialEventSettings_ObjectIdentity = ObjectIdentity
serialEventSettings = _SerialEventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2)
)
_PortEventSettingsTable_Object = MibTable
portEventSettingsTable = _PortEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    portEventSettingsTable.setStatus("current")
_PortEventSettingsEntry_Object = MibTableRow
portEventSettingsEntry = _PortEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2, 1, 1)
)
portEventSettingsEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 2, 1, 1, 4),
    _TrapDSRchange_Type()
)
trapDSRchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDSRchange.setStatus("current")
_EmailAlert_ObjectIdentity = ObjectIdentity
emailAlert = _EmailAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3)
)
_EmailWarningMailServer_Type = DisplayString
_EmailWarningMailServer_Object = MibScalar
emailWarningMailServer = _EmailWarningMailServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 2),
    _EmailRequiresAuthentication_Type()
)
emailRequiresAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailRequiresAuthentication.setStatus("current")
_EmailWarningUserName_Type = DisplayString
_EmailWarningUserName_Object = MibScalar
emailWarningUserName = _EmailWarningUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 3),
    _EmailWarningUserName_Type()
)
emailWarningUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningUserName.setStatus("current")
_EmailWarningPassword_Type = DisplayString
_EmailWarningPassword_Object = MibScalar
emailWarningPassword = _EmailWarningPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 4),
    _EmailWarningPassword_Type()
)
emailWarningPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningPassword.setStatus("current")
_EmailWarningFromEmail_Type = DisplayString
_EmailWarningFromEmail_Object = MibScalar
emailWarningFromEmail = _EmailWarningFromEmail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 5),
    _EmailWarningFromEmail_Type()
)
emailWarningFromEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFromEmail.setStatus("current")
_EmailWarningFirstEmailAddr_Type = DisplayString
_EmailWarningFirstEmailAddr_Object = MibScalar
emailWarningFirstEmailAddr = _EmailWarningFirstEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 6),
    _EmailWarningFirstEmailAddr_Type()
)
emailWarningFirstEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFirstEmailAddr.setStatus("current")
_EmailWarningSecondEmailAddr_Type = DisplayString
_EmailWarningSecondEmailAddr_Object = MibScalar
emailWarningSecondEmailAddr = _EmailWarningSecondEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 7),
    _EmailWarningSecondEmailAddr_Type()
)
emailWarningSecondEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSecondEmailAddr.setStatus("current")
_EmailWarningThirdEmailAddr_Type = DisplayString
_EmailWarningThirdEmailAddr_Object = MibScalar
emailWarningThirdEmailAddr = _EmailWarningThirdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 8),
    _EmailWarningThirdEmailAddr_Type()
)
emailWarningThirdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningThirdEmailAddr.setStatus("current")
_EmailWarningFourthEmailAddr_Type = DisplayString
_EmailWarningFourthEmailAddr_Object = MibScalar
emailWarningFourthEmailAddr = _EmailWarningFourthEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 3, 9),
    _EmailWarningFourthEmailAddr_Type()
)
emailWarningFourthEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFourthEmailAddr.setStatus("current")
_SnmpTrap_ObjectIdentity = ObjectIdentity
snmpTrap = _SnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 4)
)
_SnmpTrapReceiverIp_Type = DisplayString
_SnmpTrapReceiverIp_Object = MibScalar
snmpTrapReceiverIp = _SnmpTrapReceiverIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 2, 4, 2),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3)
)
_ConsoleSettings_ObjectIdentity = ObjectIdentity
consoleSettings = _ConsoleSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1)
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
        *(("disable", 1),
          ("enable", 0))
    )


_HttpConsole_Type.__name__ = "Integer32"
_HttpConsole_Object = MibScalar
httpConsole = _HttpConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1, 1),
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
        *(("disable", 1),
          ("enable", 0))
    )


_HttpsConsole_Type.__name__ = "Integer32"
_HttpsConsole_Object = MibScalar
httpsConsole = _HttpsConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1, 2),
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
        *(("disable", 1),
          ("enable", 0))
    )


_TelnetConsole_Type.__name__ = "Integer32"
_TelnetConsole_Object = MibScalar
telnetConsole = _TelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1, 3),
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
        *(("disable", 1),
          ("enable", 0))
    )


_SshConsole_Type.__name__ = "Integer32"
_SshConsole_Object = MibScalar
sshConsole = _SshConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1, 4),
    _SshConsole_Type()
)
sshConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshConsole.setStatus("current")


class _ResetButtonFunction_Type(Integer32):
    """Custom type resetButtonFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always-enable", 0),
          ("disable-after-60-sec", 1))
    )


_ResetButtonFunction_Type.__name__ = "Integer32"
_ResetButtonFunction_Object = MibScalar
resetButtonFunction = _ResetButtonFunction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1, 5),
    _ResetButtonFunction_Type()
)
resetButtonFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetButtonFunction.setStatus("current")


class _LcmReadOnlyProtect_Type(Integer32):
    """Custom type lcmReadOnlyProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("writable", 0))
    )


_LcmReadOnlyProtect_Type.__name__ = "Integer32"
_LcmReadOnlyProtect_Object = MibScalar
lcmReadOnlyProtect = _LcmReadOnlyProtect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 1, 6),
    _LcmReadOnlyProtect_Type()
)
lcmReadOnlyProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcmReadOnlyProtect.setStatus("current")
_LoadFactoryDefault_ObjectIdentity = ObjectIdentity
loadFactoryDefault = _LoadFactoryDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 2)
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 5, 3, 2, 1),
    _LoadFactoryDefaultSetting_Type()
)
loadFactoryDefaultSetting.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    loadFactoryDefaultSetting.setStatus("current")
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6)
)
_S2eConnections_ObjectIdentity = ObjectIdentity
s2eConnections = _S2eConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 1)
)
_MonitorRemoteIpTable_Object = MibTable
monitorRemoteIpTable = _MonitorRemoteIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    monitorRemoteIpTable.setStatus("current")
_MonitorRemoteIpEntry_Object = MibTableRow
monitorRemoteIpEntry = _MonitorRemoteIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 1, 1, 1)
)
monitorRemoteIpEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
    (0, "MOXA-CN2600-MIB", "remoteIpIndex"),
)
if mibBuilder.loadTexts:
    monitorRemoteIpEntry.setStatus("current")
_RemoteIpIndex_Type = Integer32
_RemoteIpIndex_Object = MibTableColumn
remoteIpIndex = _RemoteIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 1, 1, 1, 1),
    _RemoteIpIndex_Type()
)
remoteIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIpIndex.setStatus("current")
_MonitorRemoteIp_Type = IpAddress
_MonitorRemoteIp_Object = MibTableColumn
monitorRemoteIp = _MonitorRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 1, 1, 1, 2),
    _MonitorRemoteIp_Type()
)
monitorRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRemoteIp.setStatus("current")
_SerialPortStatus_ObjectIdentity = ObjectIdentity
serialPortStatus = _SerialPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2)
)
_MonitorSerialPortStatusTable_Object = MibTable
monitorSerialPortStatusTable = _MonitorSerialPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortStatusTable.setStatus("current")
_MonitorSerialPortStatusEntry_Object = MibTableRow
monitorSerialPortStatusEntry = _MonitorSerialPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1)
)
monitorSerialPortStatusEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortStatusEntry.setStatus("current")
_MonitorTxCount_Type = Integer32
_MonitorTxCount_Object = MibTableColumn
monitorTxCount = _MonitorTxCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 1),
    _MonitorTxCount_Type()
)
monitorTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxCount.setStatus("current")
_MonitorRxCount_Type = Integer32
_MonitorRxCount_Object = MibTableColumn
monitorRxCount = _MonitorRxCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 2),
    _MonitorRxCount_Type()
)
monitorRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxCount.setStatus("current")
_MonitorTxTotalCount_Type = Integer32
_MonitorTxTotalCount_Object = MibTableColumn
monitorTxTotalCount = _MonitorTxTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 3),
    _MonitorTxTotalCount_Type()
)
monitorTxTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxTotalCount.setStatus("current")
_MonitorRxTotalCount_Type = Integer32
_MonitorRxTotalCount_Object = MibTableColumn
monitorRxTotalCount = _MonitorRxTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 2, 1, 1, 9),
    _MonitorDCD_Type()
)
monitorDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDCD.setStatus("current")
_SerialPortErrorCount_ObjectIdentity = ObjectIdentity
serialPortErrorCount = _SerialPortErrorCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3)
)
_MonitorSerialPortErrorCountTable_Object = MibTable
monitorSerialPortErrorCountTable = _MonitorSerialPortErrorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortErrorCountTable.setStatus("current")
_MonitorSerialPortErrorCountEntry_Object = MibTableRow
monitorSerialPortErrorCountEntry = _MonitorSerialPortErrorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3, 1, 1)
)
monitorSerialPortErrorCountEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortErrorCountEntry.setStatus("current")
_MonitorErrorCountFrame_Type = Integer32
_MonitorErrorCountFrame_Object = MibTableColumn
monitorErrorCountFrame = _MonitorErrorCountFrame_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3, 1, 1, 1),
    _MonitorErrorCountFrame_Type()
)
monitorErrorCountFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountFrame.setStatus("current")
_MonitorErrorCountParity_Type = Integer32
_MonitorErrorCountParity_Object = MibTableColumn
monitorErrorCountParity = _MonitorErrorCountParity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3, 1, 1, 2),
    _MonitorErrorCountParity_Type()
)
monitorErrorCountParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountParity.setStatus("current")
_MonitorErrorCountOverrun_Type = Integer32
_MonitorErrorCountOverrun_Object = MibTableColumn
monitorErrorCountOverrun = _MonitorErrorCountOverrun_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3, 1, 1, 3),
    _MonitorErrorCountOverrun_Type()
)
monitorErrorCountOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountOverrun.setStatus("current")
_MonitorErrorCountBreak_Type = Integer32
_MonitorErrorCountBreak_Object = MibTableColumn
monitorErrorCountBreak = _MonitorErrorCountBreak_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 3, 1, 1, 4),
    _MonitorErrorCountBreak_Type()
)
monitorErrorCountBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorErrorCountBreak.setStatus("current")
_SerialPortSettings_ObjectIdentity = ObjectIdentity
serialPortSettings = _SerialPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4)
)
_MonitorSerialPortSettingsTable_Object = MibTable
monitorSerialPortSettingsTable = _MonitorSerialPortSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortSettingsTable.setStatus("current")
_MonitorSerialPortSettingsEntry_Object = MibTableRow
monitorSerialPortSettingsEntry = _MonitorSerialPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1)
)
monitorSerialPortSettingsEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortSettingsEntry.setStatus("current")
_MonitorBaudRate_Type = Integer32
_MonitorBaudRate_Object = MibTableColumn
monitorBaudRate = _MonitorBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 1),
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


_MonitorDataBits_Type.__name__ = "Integer32"
_MonitorDataBits_Object = MibTableColumn
monitorDataBits = _MonitorDataBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 2),
    _MonitorDataBits_Type()
)
monitorDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDataBits.setStatus("current")
_MonitorStopBits_Type = DisplayString
_MonitorStopBits_Object = MibTableColumn
monitorStopBits = _MonitorStopBits_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 6),
    _MonitorXONXOFFFlowControl_Type()
)
monitorXONXOFFFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorXONXOFFFlowControl.setStatus("current")


class _MonitorDTRDSRFlowControl_Type(Integer32):
    """Custom type monitorDTRDSRFlowControl based on Integer32"""
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


_MonitorDTRDSRFlowControl_Type.__name__ = "Integer32"
_MonitorDTRDSRFlowControl_Object = MibTableColumn
monitorDTRDSRFlowControl = _MonitorDTRDSRFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 7),
    _MonitorDTRDSRFlowControl_Type()
)
monitorDTRDSRFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDTRDSRFlowControl.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 4, 1, 1, 9),
    _MonitorInterface_Type()
)
monitorInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorInterface.setStatus("current")
_SerialPortBuffering_ObjectIdentity = ObjectIdentity
serialPortBuffering = _SerialPortBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 5)
)
_MonitorSerialPortBufferingTable_Object = MibTable
monitorSerialPortBufferingTable = _MonitorSerialPortBufferingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    monitorSerialPortBufferingTable.setStatus("current")
_MonitorSerialPortBufferingEntry_Object = MibTableRow
monitorSerialPortBufferingEntry = _MonitorSerialPortBufferingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 5, 1, 1)
)
monitorSerialPortBufferingEntry.setIndexNames(
    (0, "MOXA-CN2600-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSerialPortBufferingEntry.setStatus("current")
_MonitorBuffering_Type = Integer32
_MonitorBuffering_Object = MibTableColumn
monitorBuffering = _MonitorBuffering_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 6, 5, 1, 1, 1),
    _MonitorBuffering_Type()
)
monitorBuffering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorBuffering.setStatus("current")
_SaveConfiguration_ObjectIdentity = ObjectIdentity
saveConfiguration = _SaveConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 7)
)


class _SaveConfig_Type(Integer32):
    """Custom type saveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_SaveConfig_Type.__name__ = "Integer32"
_SaveConfig_Object = MibScalar
saveConfig = _SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 7, 1),
    _SaveConfig_Type()
)
saveConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    saveConfig.setStatus("current")
_Restart_ObjectIdentity = ObjectIdentity
restart = _Restart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 8)
)


class _RestartPorts_Type(Integer32):
    """Custom type restartPorts based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("port1", 0),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11),
          ("port13", 12),
          ("port14", 13),
          ("port15", 14),
          ("port16", 15),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8))
    )


_RestartPorts_Type.__name__ = "Integer32"
_RestartPorts_Object = MibScalar
restartPorts = _RestartPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 8691, 2, 11, 1, 8, 2),
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
    "MOXA-CN2600-MIB",
    **{"PortList": PortList,
       "moxa": moxa,
       "nport": nport,
       "cn2600": cn2600,
       "swMgmt": swMgmt,
       "overview": overview,
       "modelName": modelName,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "viewLan1IpAddress": viewLan1IpAddress,
       "viewLan1MacAddress": viewLan1MacAddress,
       "viewLan1Speed": viewLan1Speed,
       "viewLan2IpAddress": viewLan2IpAddress,
       "viewLan2MacAddress": viewLan2MacAddress,
       "viewLan2Speed": viewLan2Speed,
       "upTime": upTime,
       "power1Status": power1Status,
       "power2Status": power2Status,
       "basicSetting": basicSetting,
       "serverSetting": serverSetting,
       "serverName": serverName,
       "serverLocation": serverLocation,
       "timeSetting": timeSetting,
       "timeZone": timeZone,
       "localTime": localTime,
       "timeServer": timeServer,
       "networkSetting": networkSetting,
       "lan1IpConfiguration": lan1IpConfiguration,
       "lan1IpAddress": lan1IpAddress,
       "lan1NetMask": lan1NetMask,
       "lan1DefaultGateway": lan1DefaultGateway,
       "lan1Speed": lan1Speed,
       "lan1PppoeUserAccount": lan1PppoeUserAccount,
       "lan1PppoePassword": lan1PppoePassword,
       "lan2IpConfiguration": lan2IpConfiguration,
       "lan2IpAddress": lan2IpAddress,
       "lan2NetMask": lan2NetMask,
       "lan2DefaultGateway": lan2DefaultGateway,
       "lan2Speed": lan2Speed,
       "lan2PppoeUserAccount": lan2PppoeUserAccount,
       "lan2PppoePassword": lan2PppoePassword,
       "dnsServer1IpAddr": dnsServer1IpAddr,
       "dnsServer2IpAddr": dnsServer2IpAddr,
       "winsFunction": winsFunction,
       "winsServer": winsServer,
       "routingProtocol": routingProtocol,
       "gratuitousArp": gratuitousArp,
       "gratuitousArpSendPeriod": gratuitousArpSendPeriod,
       "portSetting": portSetting,
       "opModeSetting": opModeSetting,
       "opMode": opMode,
       "opModePortTable": opModePortTable,
       "opModePortEntry": opModePortEntry,
       "portIndex": portIndex,
       "portApplication": portApplication,
       "portMode": portMode,
       "application": application,
       "deviceControl": deviceControl,
       "deviceControlTable": deviceControlTable,
       "deviceControlEntry": deviceControlEntry,
       "deviceControlTcpAliveCheck": deviceControlTcpAliveCheck,
       "deviceControlMaxConnection": deviceControlMaxConnection,
       "deviceControlIgnoreJammedIp": deviceControlIgnoreJammedIp,
       "deviceControlAllowDriverControl": deviceControlAllowDriverControl,
       "deviceControlConnectionDownRTS": deviceControlConnectionDownRTS,
       "deviceControlConnectionDownDTR": deviceControlConnectionDownDTR,
       "socket": socket,
       "socketTable": socketTable,
       "socketEntry": socketEntry,
       "socketTcpAliveCheck": socketTcpAliveCheck,
       "socketInactivityTime": socketInactivityTime,
       "socketMaxConnection": socketMaxConnection,
       "socketIgnoreJammedIp": socketIgnoreJammedIp,
       "socketAllowDriverControl": socketAllowDriverControl,
       "socketTcpPort": socketTcpPort,
       "socketCmdPort": socketCmdPort,
       "socketTcpServerConnectionDownRTS": socketTcpServerConnectionDownRTS,
       "socketTcpServerConnectionDownDTR": socketTcpServerConnectionDownDTR,
       "socketTcpClientDestinationAddress1": socketTcpClientDestinationAddress1,
       "socketTcpClientDestinationPort1": socketTcpClientDestinationPort1,
       "socketTcpClientDestinationAddress2": socketTcpClientDestinationAddress2,
       "socketTcpClientDestinationPort2": socketTcpClientDestinationPort2,
       "socketTcpClientDestinationAddress3": socketTcpClientDestinationAddress3,
       "socketTcpClientDestinationPort3": socketTcpClientDestinationPort3,
       "socketTcpClientDestinationAddress4": socketTcpClientDestinationAddress4,
       "socketTcpClientDestinationPort4": socketTcpClientDestinationPort4,
       "socketTcpClientDesignatedLocalPort1": socketTcpClientDesignatedLocalPort1,
       "socketTcpClientDesignatedLocalPort2": socketTcpClientDesignatedLocalPort2,
       "socketTcpClientDesignatedLocalPort3": socketTcpClientDesignatedLocalPort3,
       "socketTcpClientDesignatedLocalPort4": socketTcpClientDesignatedLocalPort4,
       "socketTcpClientConnectionControl": socketTcpClientConnectionControl,
       "socketUdpDestinationAddress1Begin": socketUdpDestinationAddress1Begin,
       "socketUdpDestinationAddress1End": socketUdpDestinationAddress1End,
       "socketUdpDestinationPort1": socketUdpDestinationPort1,
       "socketUdpDestinationAddress2Begin": socketUdpDestinationAddress2Begin,
       "socketUdpDestinationAddress2End": socketUdpDestinationAddress2End,
       "socketUdpDestinationPort2": socketUdpDestinationPort2,
       "socketUdpDestinationAddress3Begin": socketUdpDestinationAddress3Begin,
       "socketUdpDestinationAddress3End": socketUdpDestinationAddress3End,
       "socketUdpDestinationPort3": socketUdpDestinationPort3,
       "socketUdpDestinationAddress4Begin": socketUdpDestinationAddress4Begin,
       "socketUdpDestinationAddress4End": socketUdpDestinationAddress4End,
       "socketUdpDestinationPort4": socketUdpDestinationPort4,
       "socketUdpLocalListenPort": socketUdpLocalListenPort,
       "redundantCom": redundantCom,
       "redundantComTable": redundantComTable,
       "redundantComEntry": redundantComEntry,
       "redundantComMaxConnection": redundantComMaxConnection,
       "redundantComIgnoreJammedIp": redundantComIgnoreJammedIp,
       "redundantComAllowDriverControl": redundantComAllowDriverControl,
       "redundantComConnectionDownRTS": redundantComConnectionDownRTS,
       "redundantComConnectionDownDTR": redundantComConnectionDownDTR,
       "drdas": drdas,
       "drdasTable": drdasTable,
       "drdasEntry": drdasEntry,
       "drdasTcpAliveCheck": drdasTcpAliveCheck,
       "drdasInactivityTime": drdasInactivityTime,
       "drdasIgnoreJammedIp": drdasIgnoreJammedIp,
       "drdasPrimaryIpAddress": drdasPrimaryIpAddress,
       "drdasBackup1IpAddress": drdasBackup1IpAddress,
       "drdasBackup2IpAddress": drdasBackup2IpAddress,
       "drdasBackup3IpAddress": drdasBackup3IpAddress,
       "drdasTcpPort": drdasTcpPort,
       "drdasCmdPort": drdasCmdPort,
       "drdasConnectionDownRTS": drdasConnectionDownRTS,
       "drdasConnectionDownDTR": drdasConnectionDownDTR,
       "terminal": terminal,
       "terminalTable": terminalTable,
       "terminalEntry": terminalEntry,
       "terminalTcpAliveCheck": terminalTcpAliveCheck,
       "terminalInactivityTime": terminalInactivityTime,
       "terminalAutoLinkProtocol": terminalAutoLinkProtocol,
       "terminalPrimaryHostAddress": terminalPrimaryHostAddress,
       "terminalSecondHostAddress": terminalSecondHostAddress,
       "terminalTelnetTcpPort": terminalTelnetTcpPort,
       "terminalType": terminalType,
       "terminalMaxSessions": terminalMaxSessions,
       "terminalChangeSession": terminalChangeSession,
       "terminalQuit": terminalQuit,
       "terminalBreak": terminalBreak,
       "terminalInterrupt": terminalInterrupt,
       "terminalAuthenticationType": terminalAuthenticationType,
       "terminalAutoLoginPrompt": terminalAutoLoginPrompt,
       "terminalPasswordPrompt": terminalPasswordPrompt,
       "terminalLoginUserName": terminalLoginUserName,
       "terminalLoginPassword": terminalLoginPassword,
       "reverseTerminal": reverseTerminal,
       "reverseTerminalTable": reverseTerminalTable,
       "reverseTerminalEntry": reverseTerminalEntry,
       "reverseTerminalTcpAliveCheck": reverseTerminalTcpAliveCheck,
       "reverseTerminalInactivityTime": reverseTerminalInactivityTime,
       "reverseTerminalTcpPort": reverseTerminalTcpPort,
       "reverseTerminalAuthenticationType": reverseTerminalAuthenticationType,
       "reverseTerminalMapKeys": reverseTerminalMapKeys,
       "dial": dial,
       "dialTable": dialTable,
       "dialEntry": dialEntry,
       "dialTERMBINMode": dialTERMBINMode,
       "dialPPPDMode": dialPPPDMode,
       "dialSLIPDMode": dialSLIPDMode,
       "dialAuthType": dialAuthType,
       "dialDisconnectBy": dialDisconnectBy,
       "dialDestinationIpAddress": dialDestinationIpAddress,
       "dialSourceIpAddress": dialSourceIpAddress,
       "dialIpNetmask": dialIpNetmask,
       "dialTcpIpCompression": dialTcpIpCompression,
       "dialInactivityTime": dialInactivityTime,
       "dialLinkQualityReport": dialLinkQualityReport,
       "dialOutgoingPAPID": dialOutgoingPAPID,
       "dialPAPPassword": dialPAPPassword,
       "dialIncomingPAPCheck": dialIncomingPAPCheck,
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
       "portBaudRateManual": portBaudRateManual,
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
       "modemSettings": modemSettings,
       "modemSettingsPortTable": modemSettingsPortTable,
       "modemSettingsPortEntry": modemSettingsPortEntry,
       "portEnableModem": portEnableModem,
       "portInitialString": portInitialString,
       "portDialUp": portDialUp,
       "portPhoneNumber": portPhoneNumber,
       "welcomeMessage": welcomeMessage,
       "portEnableWelcomeMessage": portEnableWelcomeMessage,
       "portMessage": portMessage,
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
       "dDNS": dDNS,
       "dDNSEnable": dDNSEnable,
       "dDNSServerAddress": dDNSServerAddress,
       "dDNSHostName": dDNSHostName,
       "dDNSUserName": dDNSUserName,
       "dDNSPassword": dDNSPassword,
       "hostTable": hostTable,
       "hostTableTable": hostTableTable,
       "hostTableEntry": hostTableEntry,
       "hostTableIndex": hostTableIndex,
       "hostName": hostName,
       "hostIpAddress": hostIpAddress,
       "routeTable": routeTable,
       "routeTableTable": routeTableTable,
       "routeTableEntry": routeTableEntry,
       "routeTableIndex": routeTableIndex,
       "gatewayRouteTable": gatewayRouteTable,
       "destinationRouteTable": destinationRouteTable,
       "netmaskRouteTable": netmaskRouteTable,
       "metricRouteTable": metricRouteTable,
       "interfaceRouteTable": interfaceRouteTable,
       "userTable": userTable,
       "userTableTable": userTableTable,
       "userTableEntry": userTableEntry,
       "userTableIndex": userTableIndex,
       "userNameUserTable": userNameUserTable,
       "passwordUserTable": passwordUserTable,
       "phoneNumberUserTable": phoneNumberUserTable,
       "authenticationServer": authenticationServer,
       "radiusServerIp": radiusServerIp,
       "radiusKey": radiusKey,
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
       "mailWarningPower1Down": mailWarningPower1Down,
       "mailWarningPower2Down": mailWarningPower2Down,
       "mailWarningEthernet1LinkDown": mailWarningEthernet1LinkDown,
       "mailWarningEthernet2LinkDown": mailWarningEthernet2LinkDown,
       "mailWarningAuthFailure": mailWarningAuthFailure,
       "mailWarningIpChanged": mailWarningIpChanged,
       "mailWarningPasswordChanged": mailWarningPasswordChanged,
       "trapServerColdStart": trapServerColdStart,
       "trapServerWarmStart": trapServerWarmStart,
       "trapServerEthernet1LinkDown": trapServerEthernet1LinkDown,
       "trapServerEthernet2LinkDown": trapServerEthernet2LinkDown,
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
       "emailWarningPassword": emailWarningPassword,
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
       "resetButtonFunction": resetButtonFunction,
       "lcmReadOnlyProtect": lcmReadOnlyProtect,
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
       "monitorDTRDSRFlowControl": monitorDTRDSRFlowControl,
       "monitorFIFO": monitorFIFO,
       "monitorInterface": monitorInterface,
       "serialPortBuffering": serialPortBuffering,
       "monitorSerialPortBufferingTable": monitorSerialPortBufferingTable,
       "monitorSerialPortBufferingEntry": monitorSerialPortBufferingEntry,
       "monitorBuffering": monitorBuffering,
       "saveConfiguration": saveConfiguration,
       "saveConfig": saveConfig,
       "restart": restart,
       "restartPorts": restartPorts,
       "restartSystem": restartSystem}
)
