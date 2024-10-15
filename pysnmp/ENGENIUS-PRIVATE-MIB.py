# SNMP MIB module (ENGENIUS-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENGENIUS-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:35 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

engeniusprivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2)
)
engeniusprivate.setRevisions(
        ("2009-06-11 11:00",
         "2009-06-10 16:00",
         "2009-05-14 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Engenius_ObjectIdentity = ObjectIdentity
engenius = _Engenius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1)
)


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    defaultValue = OctetString("Access Point")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SysPassword_Type(DisplayString):
    """Custom type sysPassword based on DisplayString"""
    defaultValue = OctetString("admin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysPassword_Type.__name__ = "DisplayString"
_SysPassword_Object = MibScalar
sysPassword = _SysPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 2),
    _SysPassword_Type()
)
sysPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPassword.setStatus("current")


class _ErrMsg_Type(DisplayString):
    """Custom type errMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ErrMsg_Type.__name__ = "DisplayString"
_ErrMsg_Object = MibScalar
errMsg = _ErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 3),
    _ErrMsg_Type()
)
errMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errMsg.setStatus("current")


class _StatusWLANSTAAssoc_Type(Integer32):
    """Custom type statusWLANSTAAssoc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusWLANSTAAssoc_Type.__name__ = "Integer32"
_StatusWLANSTAAssoc_Object = MibScalar
statusWLANSTAAssoc = _StatusWLANSTAAssoc_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 4),
    _StatusWLANSTAAssoc_Type()
)
statusWLANSTAAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusWLANSTAAssoc.setStatus("current")


class _ModelName_Type(DisplayString):
    """Custom type modelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ModelName_Type.__name__ = "DisplayString"
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 5),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")


class _WirelessMacAddress_Type(DisplayString):
    """Custom type wirelessMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_WirelessMacAddress_Type.__name__ = "DisplayString"
_WirelessMacAddress_Object = MibScalar
wirelessMacAddress = _WirelessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 6),
    _WirelessMacAddress_Type()
)
wirelessMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessMacAddress.setStatus("current")
_WanIPAddress_Type = DisplayString
_WanIPAddress_Object = MibScalar
wanIPAddress = _WanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 7),
    _WanIPAddress_Type()
)
wanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIPAddress.setStatus("current")
_WanSubnetMask_Type = DisplayString
_WanSubnetMask_Object = MibScalar
wanSubnetMask = _WanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 1, 1, 8),
    _WanSubnetMask_Type()
)
wanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanSubnetMask.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2)
)
_Wan_ObjectIdentity = ObjectIdentity
wan = _Wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1)
)


class _WanConnectionType_Type(Integer32):
    """Custom type wanConnectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("pppoe", 3),
          ("static", 2))
    )


_WanConnectionType_Type.__name__ = "Integer32"
_WanConnectionType_Object = MibScalar
wanConnectionType = _WanConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1, 1),
    _WanConnectionType_Type()
)
wanConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanConnectionType.setStatus("current")


class _WanGeneralAccount_Type(DisplayString):
    """Custom type wanGeneralAccount based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WanGeneralAccount_Type.__name__ = "DisplayString"
_WanGeneralAccount_Object = MibScalar
wanGeneralAccount = _WanGeneralAccount_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1, 2),
    _WanGeneralAccount_Type()
)
wanGeneralAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanGeneralAccount.setStatus("current")


class _WanGeneralDomain_Type(DisplayString):
    """Custom type wanGeneralDomain based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WanGeneralDomain_Type.__name__ = "DisplayString"
_WanGeneralDomain_Object = MibScalar
wanGeneralDomain = _WanGeneralDomain_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1, 3),
    _WanGeneralDomain_Type()
)
wanGeneralDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanGeneralDomain.setStatus("current")


class _WanGeneralIP_Type(IpAddress):
    """Custom type wanGeneralIP based on IpAddress"""
    defaultValue = OctetString("10.1.1.100")


_WanGeneralIP_Object = MibScalar
wanGeneralIP = _WanGeneralIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1, 4),
    _WanGeneralIP_Type()
)
wanGeneralIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanGeneralIP.setStatus("current")


class _WanGeneralSubnetMask_Type(IpAddress):
    """Custom type wanGeneralSubnetMask based on IpAddress"""
    defaultValue = OctetString("255.255.0.0")


_WanGeneralSubnetMask_Object = MibScalar
wanGeneralSubnetMask = _WanGeneralSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1, 5),
    _WanGeneralSubnetMask_Type()
)
wanGeneralSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanGeneralSubnetMask.setStatus("current")


class _WanGeneralGateway_Type(IpAddress):
    """Custom type wanGeneralGateway based on IpAddress"""
    defaultValue = OctetString("10.1.1.150")


_WanGeneralGateway_Object = MibScalar
wanGeneralGateway = _WanGeneralGateway_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 1, 6),
    _WanGeneralGateway_Type()
)
wanGeneralGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanGeneralGateway.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2)
)


class _WanPPPoELoginName_Type(DisplayString):
    """Custom type wanPPPoELoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WanPPPoELoginName_Type.__name__ = "DisplayString"
_WanPPPoELoginName_Object = MibScalar
wanPPPoELoginName = _WanPPPoELoginName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2, 1),
    _WanPPPoELoginName_Type()
)
wanPPPoELoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPPPoELoginName.setStatus("current")


class _WanPPPoEPassword_Type(DisplayString):
    """Custom type wanPPPoEPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WanPPPoEPassword_Type.__name__ = "DisplayString"
_WanPPPoEPassword_Object = MibScalar
wanPPPoEPassword = _WanPPPoEPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2, 2),
    _WanPPPoEPassword_Type()
)
wanPPPoEPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPPPoEPassword.setStatus("current")


class _WanPPPoEServiceName_Type(DisplayString):
    """Custom type wanPPPoEServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WanPPPoEServiceName_Type.__name__ = "DisplayString"
_WanPPPoEServiceName_Object = MibScalar
wanPPPoEServiceName = _WanPPPoEServiceName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2, 3),
    _WanPPPoEServiceName_Type()
)
wanPPPoEServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPPPoEServiceName.setStatus("current")


class _WanPPPoEConnectionType_Type(Integer32):
    """Custom type wanPPPoEConnectionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connectondemand", 1),
          ("keepalive", 0))
    )


_WanPPPoEConnectionType_Type.__name__ = "Integer32"
_WanPPPoEConnectionType_Object = MibScalar
wanPPPoEConnectionType = _WanPPPoEConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2, 4),
    _WanPPPoEConnectionType_Type()
)
wanPPPoEConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPPPoEConnectionType.setStatus("current")


class _WanPPPoEMaxIdleTime_Type(Integer32):
    """Custom type wanPPPoEMaxIdleTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WanPPPoEMaxIdleTime_Type.__name__ = "Integer32"
_WanPPPoEMaxIdleTime_Object = MibScalar
wanPPPoEMaxIdleTime = _WanPPPoEMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2, 5),
    _WanPPPoEMaxIdleTime_Type()
)
wanPPPoEMaxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPPPoEMaxIdleTime.setStatus("current")


class _WanPPPoERedialPeriod_Type(Integer32):
    """Custom type wanPPPoERedialPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 180),
    )


_WanPPPoERedialPeriod_Type.__name__ = "Integer32"
_WanPPPoERedialPeriod_Object = MibScalar
wanPPPoERedialPeriod = _WanPPPoERedialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 2, 6),
    _WanPPPoERedialPeriod_Type()
)
wanPPPoERedialPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPPPoERedialPeriod.setStatus("current")
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 3)
)


class _WanDNSSourc_Type(Integer32):
    """Custom type wanDNSSourc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isp", 0),
          ("specified", 1))
    )


_WanDNSSourc_Type.__name__ = "Integer32"
_WanDNSSourc_Object = MibScalar
wanDNSSourc = _WanDNSSourc_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 3, 1),
    _WanDNSSourc_Type()
)
wanDNSSourc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDNSSourc.setStatus("current")


class _WanPrimaryDNSIP_Type(IpAddress):
    """Custom type wanPrimaryDNSIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_WanPrimaryDNSIP_Object = MibScalar
wanPrimaryDNSIP = _WanPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 3, 2),
    _WanPrimaryDNSIP_Type()
)
wanPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPrimaryDNSIP.setStatus("current")


class _WanSecondaryDNSIP_Type(IpAddress):
    """Custom type wanSecondaryDNSIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_WanSecondaryDNSIP_Object = MibScalar
wanSecondaryDNSIP = _WanSecondaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 3, 3),
    _WanSecondaryDNSIP_Type()
)
wanSecondaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanSecondaryDNSIP.setStatus("current")
_Mtu_ObjectIdentity = ObjectIdentity
mtu = _Mtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 4)
)


class _WanMTUMode_Type(Integer32):
    """Custom type wanMTUMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_WanMTUMode_Type.__name__ = "Integer32"
_WanMTUMode_Object = MibScalar
wanMTUMode = _WanMTUMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 4, 1),
    _WanMTUMode_Type()
)
wanMTUMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanMTUMode.setStatus("current")


class _WanMTU_Type(Integer32):
    """Custom type wanMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1500),
    )


_WanMTU_Type.__name__ = "Integer32"
_WanMTU_Object = MibScalar
wanMTU = _WanMTU_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 4, 2),
    _WanMTU_Type()
)
wanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanMTU.setStatus("current")


class _PppoeMTU_Type(Integer32):
    """Custom type pppoeMTU based on Integer32"""
    defaultValue = 1492

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1492),
    )


_PppoeMTU_Type.__name__ = "Integer32"
_PppoeMTU_Object = MibScalar
pppoeMTU = _PppoeMTU_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 4, 3),
    _PppoeMTU_Type()
)
pppoeMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeMTU.setStatus("current")
_Landhcp_ObjectIdentity = ObjectIdentity
landhcp = _Landhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5)
)


class _LanDHCPC_Type(Integer32):
    """Custom type lanDHCPC based on Integer32"""
    defaultValue = 0

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


_LanDHCPC_Type.__name__ = "Integer32"
_LanDHCPC_Object = MibScalar
lanDHCPC = _LanDHCPC_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 1),
    _LanDHCPC_Type()
)
lanDHCPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanDHCPC.setStatus("current")


class _LanIP_Type(IpAddress):
    """Custom type lanIP based on IpAddress"""
    defaultValue = OctetString("192.168.1.1")


_LanIP_Object = MibScalar
lanIP = _LanIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 2),
    _LanIP_Type()
)
lanIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIP.setStatus("current")


class _LanSubnetmask_Type(IpAddress):
    """Custom type lanSubnetmask based on IpAddress"""
    defaultValue = OctetString("255.255.255.0")


_LanSubnetmask_Object = MibScalar
lanSubnetmask = _LanSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 3),
    _LanSubnetmask_Type()
)
lanSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanSubnetmask.setStatus("current")


class _LanGatewayIP_Type(IpAddress):
    """Custom type lanGatewayIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_LanGatewayIP_Object = MibScalar
lanGatewayIP = _LanGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 4),
    _LanGatewayIP_Type()
)
lanGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanGatewayIP.setStatus("current")


class _LanWINSAddr_Type(IpAddress):
    """Custom type lanWINSAddr based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_LanWINSAddr_Object = MibScalar
lanWINSAddr = _LanWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 5),
    _LanWINSAddr_Type()
)
lanWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanWINSAddr.setStatus("current")


class _LanDHCPSrvEnable_Type(Integer32):
    """Custom type lanDHCPSrvEnable based on Integer32"""
    defaultValue = 1

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


_LanDHCPSrvEnable_Type.__name__ = "Integer32"
_LanDHCPSrvEnable_Object = MibScalar
lanDHCPSrvEnable = _LanDHCPSrvEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 6),
    _LanDHCPSrvEnable_Type()
)
lanDHCPSrvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanDHCPSrvEnable.setStatus("current")


class _LanDHCPSrvStartAddr_Type(IpAddress):
    """Custom type lanDHCPSrvStartAddr based on IpAddress"""
    defaultValue = OctetString("192.168.1.2")


_LanDHCPSrvStartAddr_Object = MibScalar
lanDHCPSrvStartAddr = _LanDHCPSrvStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 7),
    _LanDHCPSrvStartAddr_Type()
)
lanDHCPSrvStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanDHCPSrvStartAddr.setStatus("current")


class _LanDHCPSrvStopAddr_Type(IpAddress):
    """Custom type lanDHCPSrvStopAddr based on IpAddress"""
    defaultValue = OctetString("192.168.1.254")


_LanDHCPSrvStopAddr_Object = MibScalar
lanDHCPSrvStopAddr = _LanDHCPSrvStopAddr_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 5, 8),
    _LanDHCPSrvStopAddr_Type()
)
lanDHCPSrvStopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanDHCPSrvStopAddr.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 6)
)


class _TimeSettingMode_Type(Integer32):
    """Custom type timeSettingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 0))
    )


_TimeSettingMode_Type.__name__ = "Integer32"
_TimeSettingMode_Object = MibScalar
timeSettingMode = _TimeSettingMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 6, 1),
    _TimeSettingMode_Type()
)
timeSettingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSettingMode.setStatus("current")


class _UserNTPSrvMode_Type(Integer32):
    """Custom type userNTPSrvMode based on Integer32"""
    defaultValue = 0

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


_UserNTPSrvMode_Type.__name__ = "Integer32"
_UserNTPSrvMode_Object = MibScalar
userNTPSrvMode = _UserNTPSrvMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 6, 2),
    _UserNTPSrvMode_Type()
)
userNTPSrvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userNTPSrvMode.setStatus("current")


class _UserNTPSrvIP_Type(IpAddress):
    """Custom type userNTPSrvIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_UserNTPSrvIP_Object = MibScalar
userNTPSrvIP = _UserNTPSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 6, 3),
    _UserNTPSrvIP_Type()
)
userNTPSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userNTPSrvIP.setStatus("current")


class _TimeZone_Type(DisplayString):
    """Custom type timeZone based on DisplayString"""
    defaultValue = OctetString("GMT0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TimeZone_Type.__name__ = "DisplayString"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 6, 4),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 8)
)


class _Username_Type(DisplayString):
    """Custom type username based on DisplayString"""
    defaultValue = OctetString("admin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_Username_Type.__name__ = "DisplayString"
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 8, 1),
    _Username_Type()
)
username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _RemoteManagementEnable_Type(Integer32):
    """Custom type remoteManagementEnable based on Integer32"""
    defaultValue = 0

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


_RemoteManagementEnable_Type.__name__ = "Integer32"
_RemoteManagementEnable_Object = MibScalar
remoteManagementEnable = _RemoteManagementEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 8, 3),
    _RemoteManagementEnable_Type()
)
remoteManagementEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteManagementEnable.setStatus("current")


class _RemoteUpgradeEnable_Type(Integer32):
    """Custom type remoteUpgradeEnable based on Integer32"""
    defaultValue = 0

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


_RemoteUpgradeEnable_Type.__name__ = "Integer32"
_RemoteUpgradeEnable_Object = MibScalar
remoteUpgradeEnable = _RemoteUpgradeEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 8, 4),
    _RemoteUpgradeEnable_Type()
)
remoteUpgradeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUpgradeEnable.setStatus("current")


class _RemoteManagementPort_Type(Integer32):
    """Custom type remoteManagementPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RemoteManagementPort_Type.__name__ = "Integer32"
_RemoteManagementPort_Object = MibScalar
remoteManagementPort = _RemoteManagementPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 8, 5),
    _RemoteManagementPort_Type()
)
remoteManagementPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteManagementPort.setStatus("current")


class _RemoteManagementVLANID_Type(Integer32):
    """Custom type remoteManagementVLANID based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_RemoteManagementVLANID_Type.__name__ = "Integer32"
_RemoteManagementVLANID_Object = MibScalar
remoteManagementVLANID = _RemoteManagementVLANID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 8, 6),
    _RemoteManagementVLANID_Type()
)
remoteManagementVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteManagementVLANID.setStatus("current")
_Wlan_ObjectIdentity = ObjectIdentity
wlan = _Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9)
)


class _WlanMode_Type(Integer32):
    """Custom type wlanMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("wlan11a", 1),
          ("wlan11astaticturbo", 5),
          ("wlan11b", 2),
          ("wlan11bg", 3),
          ("wlan11gdynamicturbo", 6),
          ("wlan11gpure", 9),
          ("wlan11gstaticturbo", 7))
    )


_WlanMode_Type.__name__ = "Integer32"
_WlanMode_Object = MibScalar
wlanMode = _WlanMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 1),
    _WlanMode_Type()
)
wlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMode.setStatus("current")


class _ChanBwMode_Type(Integer32):
    """Custom type chanBwMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wlan10MHz", 1),
          ("wlan20MHz", 0),
          ("wlan5MHz", 2))
    )


_ChanBwMode_Type.__name__ = "Integer32"
_ChanBwMode_Object = MibScalar
chanBwMode = _ChanBwMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 2),
    _ChanBwMode_Type()
)
chanBwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanBwMode.setStatus("current")


class _WlanaSSID_Type(DisplayString):
    """Custom type wlanaSSID based on DisplayString"""
    defaultValue = OctetString("EnGenius")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_WlanaSSID_Type.__name__ = "DisplayString"
_WlanaSSID_Object = MibScalar
wlanaSSID = _WlanaSSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 3),
    _WlanaSSID_Type()
)
wlanaSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanaSSID.setStatus("current")


class _WlanOpMode_Type(Integer32):
    """Custom type wlanOpMode based on Integer32"""
    defaultValue = 0

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
        *(("accesspoint", 0),
          ("aprouter", 4),
          ("clientbridge", 1),
          ("clientrouter", 5),
          ("mesh", 6),
          ("repeater", 3),
          ("wdsbridge", 2))
    )


_WlanOpMode_Type.__name__ = "Integer32"
_WlanOpMode_Object = MibScalar
wlanOpMode = _WlanOpMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 4),
    _WlanOpMode_Type()
)
wlanOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanOpMode.setStatus("current")


class _WlanCountryCode_Type(DisplayString):
    """Custom type wlanCountryCode based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_WlanCountryCode_Type.__name__ = "DisplayString"
_WlanCountryCode_Object = MibScalar
wlanCountryCode = _WlanCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 5),
    _WlanCountryCode_Type()
)
wlanCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCountryCode.setStatus("current")


class _WlanCountry_Type(DisplayString):
    """Custom type wlanCountry based on DisplayString"""
    defaultValue = OctetString("N/A")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WlanCountry_Type.__name__ = "DisplayString"
_WlanCountry_Object = MibScalar
wlanCountry = _WlanCountry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 6),
    _WlanCountry_Type()
)
wlanCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCountry.setStatus("current")


class _WlanChannel_Type(Integer32):
    """Custom type wlanChannel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WlanChannel_Type.__name__ = "Integer32"
_WlanChannel_Object = MibScalar
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 7),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("current")


class _WlanACLMode_Type(Integer32):
    """Custom type wlanACLMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("disable", 0))
    )


_WlanACLMode_Type.__name__ = "Integer32"
_WlanACLMode_Object = MibScalar
wlanACLMode = _WlanACLMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 8),
    _WlanACLMode_Type()
)
wlanACLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanACLMode.setStatus("current")


class _WlanOutdoorDistance_Type(Integer32):
    """Custom type wlanOutdoorDistance based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_WlanOutdoorDistance_Type.__name__ = "Integer32"
_WlanOutdoorDistance_Object = MibScalar
wlanOutdoorDistance = _WlanOutdoorDistance_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 9),
    _WlanOutdoorDistance_Type()
)
wlanOutdoorDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanOutdoorDistance.setStatus("current")


class _WlanDataRate_Type(DisplayString):
    """Custom type wlanDataRate based on DisplayString"""
    defaultValue = OctetString("auto")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_WlanDataRate_Type.__name__ = "DisplayString"
_WlanDataRate_Object = MibScalar
wlanDataRate = _WlanDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 10),
    _WlanDataRate_Type()
)
wlanDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDataRate.setStatus("current")


class _WlanTxPower_Type(Integer32):
    """Custom type wlanTxPower based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WlanTxPower_Type.__name__ = "Integer32"
_WlanTxPower_Object = MibScalar
wlanTxPower = _WlanTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 11),
    _WlanTxPower_Type()
)
wlanTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanTxPower.setStatus("current")


class _Antennasel_Type(Integer32):
    """Custom type antennasel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 0),
          ("horizontal", 2),
          ("vertical", 1))
    )


_Antennasel_Type.__name__ = "Integer32"
_Antennasel_Object = MibScalar
antennasel = _Antennasel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 12),
    _Antennasel_Type()
)
antennasel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennasel.setStatus("current")


class _WlanBeaconInterval_Type(Integer32):
    """Custom type wlanBeaconInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
    )


_WlanBeaconInterval_Type.__name__ = "Integer32"
_WlanBeaconInterval_Object = MibScalar
wlanBeaconInterval = _WlanBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 13),
    _WlanBeaconInterval_Type()
)
wlanBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanBeaconInterval.setStatus("current")


class _WlanRTSTh_Type(Integer32):
    """Custom type wlanRTSTh based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2346),
    )


_WlanRTSTh_Type.__name__ = "Integer32"
_WlanRTSTh_Object = MibScalar
wlanRTSTh = _WlanRTSTh_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 15),
    _WlanRTSTh_Type()
)
wlanRTSTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRTSTh.setStatus("current")


class _WlanFragLen_Type(Integer32):
    """Custom type wlanFragLen based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WlanFragLen_Type.__name__ = "Integer32"
_WlanFragLen_Object = MibScalar
wlanFragLen = _WlanFragLen_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 16),
    _WlanFragLen_Type()
)
wlanFragLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanFragLen.setStatus("current")


class _WlanProtmode_Type(Integer32):
    """Custom type wlanProtmode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctsonly", 1),
          ("disable", 0),
          ("rtscts", 2))
    )


_WlanProtmode_Type.__name__ = "Integer32"
_WlanProtmode_Object = MibScalar
wlanProtmode = _WlanProtmode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 18),
    _WlanProtmode_Type()
)
wlanProtmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanProtmode.setStatus("current")
_WlanPreferBSSID_Type = DisplayString
_WlanPreferBSSID_Object = MibScalar
wlanPreferBSSID = _WlanPreferBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 19),
    _WlanPreferBSSID_Type()
)
wlanPreferBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPreferBSSID.setStatus("current")
_WlanTable_Object = MibTable
wlanTable = _WlanTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21)
)
if mibBuilder.loadTexts:
    wlanTable.setStatus("current")
_WlanTableEntry_Object = MibTableRow
wlanTableEntry = _WlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1)
)
wlanTableEntry.setIndexNames(
    (0, "ENGENIUS-PRIVATE-MIB", "wlanTableIndex"),
)
if mibBuilder.loadTexts:
    wlanTableEntry.setStatus("current")


class _WlanTableIndex_Type(Integer32):
    """Custom type wlanTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WlanTableIndex_Type.__name__ = "Integer32"
_WlanTableIndex_Object = MibTableColumn
wlanTableIndex = _WlanTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 1),
    _WlanTableIndex_Type()
)
wlanTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanTableIndex.setStatus("current")


class _WlanEnable_Type(Integer32):
    """Custom type wlanEnable based on Integer32"""
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


_WlanEnable_Type.__name__ = "Integer32"
_WlanEnable_Object = MibTableColumn
wlanEnable = _WlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 2),
    _WlanEnable_Type()
)
wlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEnable.setStatus("current")


class _WlanSSID_Type(DisplayString):
    """Custom type wlanSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanSSID_Type.__name__ = "DisplayString"
_WlanSSID_Object = MibTableColumn
wlanSSID = _WlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 3),
    _WlanSSID_Type()
)
wlanSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSID.setStatus("current")


class _WlanHideSSID_Type(Integer32):
    """Custom type wlanHideSSID based on Integer32"""
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


_WlanHideSSID_Type.__name__ = "Integer32"
_WlanHideSSID_Object = MibTableColumn
wlanHideSSID = _WlanHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 4),
    _WlanHideSSID_Type()
)
wlanHideSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHideSSID.setStatus("current")


class _WlanStaSeparation_Type(Integer32):
    """Custom type wlanStaSeparation based on Integer32"""
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


_WlanStaSeparation_Type.__name__ = "Integer32"
_WlanStaSeparation_Object = MibTableColumn
wlanStaSeparation = _WlanStaSeparation_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 5),
    _WlanStaSeparation_Type()
)
wlanStaSeparation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanStaSeparation.setStatus("current")


class _WlanVLANID_Type(Integer32):
    """Custom type wlanVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WlanVLANID_Type.__name__ = "Integer32"
_WlanVLANID_Object = MibTableColumn
wlanVLANID = _WlanVLANID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 6),
    _WlanVLANID_Type()
)
wlanVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANID.setStatus("current")


class _WlanAuth_Type(Integer32):
    """Custom type wlanAuth based on Integer32"""
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
        *(("auto", 3),
          ("open", 1),
          ("shared", 2),
          ("wlan8021x", 4),
          ("wpa", 5),
          ("wpa2", 7),
          ("wpa2psk", 8),
          ("wpamixed", 9),
          ("wpapsk", 6),
          ("wpapskmixed", 10))
    )


_WlanAuth_Type.__name__ = "Integer32"
_WlanAuth_Object = MibTableColumn
wlanAuth = _WlanAuth_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 7),
    _WlanAuth_Type()
)
wlanAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuth.setStatus("current")


class _WlanEncryption_Type(Integer32):
    """Custom type wlanEncryption based on Integer32"""
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
        *(("aes", 3),
          ("auto", 4),
          ("none", 0),
          ("tkip", 2),
          ("wep", 1))
    )


_WlanEncryption_Type.__name__ = "Integer32"
_WlanEncryption_Object = MibTableColumn
wlanEncryption = _WlanEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 8),
    _WlanEncryption_Type()
)
wlanEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEncryption.setStatus("current")


class _WlanWepDefaultKeyIdx_Type(Integer32):
    """Custom type wlanWepDefaultKeyIdx based on Integer32"""
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
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_WlanWepDefaultKeyIdx_Type.__name__ = "Integer32"
_WlanWepDefaultKeyIdx_Object = MibTableColumn
wlanWepDefaultKeyIdx = _WlanWepDefaultKeyIdx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 9),
    _WlanWepDefaultKeyIdx_Type()
)
wlanWepDefaultKeyIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepDefaultKeyIdx.setStatus("current")


class _WlanWepKey_Type(DisplayString):
    """Custom type wlanWepKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(26, 26),
        ValueSizeConstraint(32, 32),
    )


_WlanWepKey_Type.__name__ = "DisplayString"
_WlanWepKey_Object = MibTableColumn
wlanWepKey = _WlanWepKey_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 10),
    _WlanWepKey_Type()
)
wlanWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey.setStatus("current")


class _WlanWpapskPassphrase_Type(DisplayString):
    """Custom type wlanWpapskPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanWpapskPassphrase_Type.__name__ = "DisplayString"
_WlanWpapskPassphrase_Object = MibTableColumn
wlanWpapskPassphrase = _WlanWpapskPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 11),
    _WlanWpapskPassphrase_Type()
)
wlanWpapskPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWpapskPassphrase.setStatus("current")
_WlanWpaRadiusSrvIP_Type = IpAddress
_WlanWpaRadiusSrvIP_Object = MibTableColumn
wlanWpaRadiusSrvIP = _WlanWpaRadiusSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 12),
    _WlanWpaRadiusSrvIP_Type()
)
wlanWpaRadiusSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWpaRadiusSrvIP.setStatus("current")


class _WlanWpaRadiusSrvPort_Type(Integer32):
    """Custom type wlanWpaRadiusSrvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WlanWpaRadiusSrvPort_Type.__name__ = "Integer32"
_WlanWpaRadiusSrvPort_Object = MibTableColumn
wlanWpaRadiusSrvPort = _WlanWpaRadiusSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 13),
    _WlanWpaRadiusSrvPort_Type()
)
wlanWpaRadiusSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWpaRadiusSrvPort.setStatus("current")


class _WlanWpaRadiusSrvSecret_Type(DisplayString):
    """Custom type wlanWpaRadiusSrvSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanWpaRadiusSrvSecret_Type.__name__ = "DisplayString"
_WlanWpaRadiusSrvSecret_Object = MibTableColumn
wlanWpaRadiusSrvSecret = _WlanWpaRadiusSrvSecret_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 14),
    _WlanWpaRadiusSrvSecret_Type()
)
wlanWpaRadiusSrvSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWpaRadiusSrvSecret.setStatus("current")


class _WlanWpaGroupKeyUpdateInterval_Type(Integer32):
    """Custom type wlanWpaGroupKeyUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_WlanWpaGroupKeyUpdateInterval_Type.__name__ = "Integer32"
_WlanWpaGroupKeyUpdateInterval_Object = MibTableColumn
wlanWpaGroupKeyUpdateInterval = _WlanWpaGroupKeyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 9, 21, 1, 15),
    _WlanWpaGroupKeyUpdateInterval_Type()
)
wlanWpaGroupKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWpaGroupKeyUpdateInterval.setStatus("current")
_Wlansta_ObjectIdentity = ObjectIdentity
wlansta = _Wlansta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 10)
)


class _WlanSTAAuth_Type(Integer32):
    """Custom type wlanSTAAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("shared", 2),
          ("wpa2psk", 8),
          ("wpapsk", 6),
          ("wpapskmixed", 10))
    )


_WlanSTAAuth_Type.__name__ = "Integer32"
_WlanSTAAuth_Object = MibScalar
wlanSTAAuth = _WlanSTAAuth_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 10, 1),
    _WlanSTAAuth_Type()
)
wlanSTAAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSTAAuth.setStatus("current")


class _WlanSTAEncryption_Type(Integer32):
    """Custom type wlanSTAEncryption based on Integer32"""
    defaultValue = 0

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
        *(("aes", 3),
          ("auto", 4),
          ("none", 0),
          ("tkip", 2),
          ("wep", 1))
    )


_WlanSTAEncryption_Type.__name__ = "Integer32"
_WlanSTAEncryption_Object = MibScalar
wlanSTAEncryption = _WlanSTAEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 10, 2),
    _WlanSTAEncryption_Type()
)
wlanSTAEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSTAEncryption.setStatus("current")


class _WlanSTAWepDefaultKeyIdx_Type(Integer32):
    """Custom type wlanSTAWepDefaultKeyIdx based on Integer32"""
    defaultValue = 1

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
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_WlanSTAWepDefaultKeyIdx_Type.__name__ = "Integer32"
_WlanSTAWepDefaultKeyIdx_Object = MibScalar
wlanSTAWepDefaultKeyIdx = _WlanSTAWepDefaultKeyIdx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 10, 3),
    _WlanSTAWepDefaultKeyIdx_Type()
)
wlanSTAWepDefaultKeyIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSTAWepDefaultKeyIdx.setStatus("current")


class _WlanSTAWepKey_Type(DisplayString):
    """Custom type wlanSTAWepKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(26, 26),
        ValueSizeConstraint(32, 32),
    )


_WlanSTAWepKey_Type.__name__ = "DisplayString"
_WlanSTAWepKey_Object = MibScalar
wlanSTAWepKey = _WlanSTAWepKey_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 10, 4),
    _WlanSTAWepKey_Type()
)
wlanSTAWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSTAWepKey.setStatus("current")


class _WlanSTAWpapskPassphrase_Type(DisplayString):
    """Custom type wlanSTAWpapskPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanSTAWpapskPassphrase_Type.__name__ = "DisplayString"
_WlanSTAWpapskPassphrase_Object = MibScalar
wlanSTAWpapskPassphrase = _WlanSTAWpapskPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 10, 5),
    _WlanSTAWpapskPassphrase_Type()
)
wlanSTAWpapskPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSTAWpapskPassphrase.setStatus("current")
_Wlanmesh_ObjectIdentity = ObjectIdentity
wlanmesh = _Wlanmesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11)
)


class _WlanMESHSSID_Type(DisplayString):
    """Custom type wlanMESHSSID based on DisplayString"""
    defaultValue = OctetString("EnGeniusMesh")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_WlanMESHSSID_Type.__name__ = "DisplayString"
_WlanMESHSSID_Object = MibScalar
wlanMESHSSID = _WlanMESHSSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 1),
    _WlanMESHSSID_Type()
)
wlanMESHSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHSSID.setStatus("current")


class _WlanMESHGateway_Type(Integer32):
    """Custom type wlanMESHGateway based on Integer32"""
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


_WlanMESHGateway_Type.__name__ = "Integer32"
_WlanMESHGateway_Object = MibScalar
wlanMESHGateway = _WlanMESHGateway_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 2),
    _WlanMESHGateway_Type()
)
wlanMESHGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHGateway.setStatus("current")


class _WlanMESHAuth_Type(Integer32):
    """Custom type wlanMESHAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("shared", 2))
    )


_WlanMESHAuth_Type.__name__ = "Integer32"
_WlanMESHAuth_Object = MibScalar
wlanMESHAuth = _WlanMESHAuth_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 4),
    _WlanMESHAuth_Type()
)
wlanMESHAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHAuth.setStatus("current")


class _WlanMESHEncryption_Type(Integer32):
    """Custom type wlanMESHEncryption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("none", 0),
          ("wep", 1))
    )


_WlanMESHEncryption_Type.__name__ = "Integer32"
_WlanMESHEncryption_Object = MibScalar
wlanMESHEncryption = _WlanMESHEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 5),
    _WlanMESHEncryption_Type()
)
wlanMESHEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHEncryption.setStatus("current")


class _WlanMESHWepDefaultKeyIdx_Type(Integer32):
    """Custom type wlanMESHWepDefaultKeyIdx based on Integer32"""
    defaultValue = 1

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
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_WlanMESHWepDefaultKeyIdx_Type.__name__ = "Integer32"
_WlanMESHWepDefaultKeyIdx_Object = MibScalar
wlanMESHWepDefaultKeyIdx = _WlanMESHWepDefaultKeyIdx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 6),
    _WlanMESHWepDefaultKeyIdx_Type()
)
wlanMESHWepDefaultKeyIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHWepDefaultKeyIdx.setStatus("current")


class _WlanMESHWepKey_Type(DisplayString):
    """Custom type wlanMESHWepKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(26, 26),
        ValueSizeConstraint(32, 32),
    )


_WlanMESHWepKey_Type.__name__ = "DisplayString"
_WlanMESHWepKey_Object = MibScalar
wlanMESHWepKey = _WlanMESHWepKey_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 7),
    _WlanMESHWepKey_Type()
)
wlanMESHWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHWepKey.setStatus("current")


class _WlanMESHWpapskPassphrase_Type(DisplayString):
    """Custom type wlanMESHWpapskPassphrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanMESHWpapskPassphrase_Type.__name__ = "DisplayString"
_WlanMESHWpapskPassphrase_Object = MibScalar
wlanMESHWpapskPassphrase = _WlanMESHWpapskPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 11, 8),
    _WlanMESHWpapskPassphrase_Type()
)
wlanMESHWpapskPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMESHWpapskPassphrase.setStatus("current")
_Wlanstawds_ObjectIdentity = ObjectIdentity
wlanstawds = _Wlanstawds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 14)
)


class _StaWDS_Type(Integer32):
    """Custom type staWDS based on Integer32"""
    defaultValue = 1

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


_StaWDS_Type.__name__ = "Integer32"
_StaWDS_Object = MibScalar
staWDS = _StaWDS_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 14, 1),
    _StaWDS_Type()
)
staWDS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staWDS.setStatus("current")
_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 15)
)


class _StpMode_Type(Integer32):
    """Custom type stpMode based on Integer32"""
    defaultValue = 0

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


_StpMode_Type.__name__ = "Integer32"
_StpMode_Object = MibScalar
stpMode = _StpMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 15, 1),
    _StpMode_Type()
)
stpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMode.setStatus("current")


class _StpHelloTime_Type(Integer32):
    """Custom type stpHelloTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpHelloTime_Type.__name__ = "Integer32"
_StpHelloTime_Object = MibScalar
stpHelloTime = _StpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 15, 2),
    _StpHelloTime_Type()
)
stpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpHelloTime.setStatus("current")


class _StpMaxAge_Type(Integer32):
    """Custom type stpMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpMaxAge_Type.__name__ = "Integer32"
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 15, 3),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("current")


class _StpForwardDelay_Type(Integer32):
    """Custom type stpForwardDelay based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StpForwardDelay_Type.__name__ = "Integer32"
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 15, 4),
    _StpForwardDelay_Type()
)
stpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpForwardDelay.setStatus("current")


class _StpPriority_Type(Integer32):
    """Custom type stpPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpPriority_Type.__name__ = "Integer32"
_StpPriority_Object = MibScalar
stpPriority = _StpPriority_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 15, 5),
    _StpPriority_Type()
)
stpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPriority.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16)
)


class _SnmpEnable_Type(Integer32):
    """Custom type snmpEnable based on Integer32"""
    defaultValue = 1

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
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 1),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")


class _SnmpCmntyRO_Type(DisplayString):
    """Custom type snmpCmntyRO based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SnmpCmntyRO_Type.__name__ = "DisplayString"
_SnmpCmntyRO_Object = MibScalar
snmpCmntyRO = _SnmpCmntyRO_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 2),
    _SnmpCmntyRO_Type()
)
snmpCmntyRO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCmntyRO.setStatus("current")


class _SnmpCmntyRW_Type(DisplayString):
    """Custom type snmpCmntyRW based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SnmpCmntyRW_Type.__name__ = "DisplayString"
_SnmpCmntyRW_Object = MibScalar
snmpCmntyRW = _SnmpCmntyRW_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 3),
    _SnmpCmntyRW_Type()
)
snmpCmntyRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCmntyRW.setStatus("current")


class _SnmpTrapDstIP_Type(IpAddress):
    """Custom type snmpTrapDstIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_SnmpTrapDstIP_Object = MibScalar
snmpTrapDstIP = _SnmpTrapDstIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 4),
    _SnmpTrapDstIP_Type()
)
snmpTrapDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDstIP.setStatus("current")


class _SnmpTrapCmnty_Type(DisplayString):
    """Custom type snmpTrapCmnty based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SnmpTrapCmnty_Type.__name__ = "DisplayString"
_SnmpTrapCmnty_Object = MibScalar
snmpTrapCmnty = _SnmpTrapCmnty_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 5),
    _SnmpTrapCmnty_Type()
)
snmpTrapCmnty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCmnty.setStatus("current")


class _SnmpCont_Type(DisplayString):
    """Custom type snmpCont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnmpCont_Type.__name__ = "DisplayString"
_SnmpCont_Object = MibScalar
snmpCont = _SnmpCont_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 6),
    _SnmpCont_Type()
)
snmpCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCont.setStatus("current")


class _SnmpLocation_Type(DisplayString):
    """Custom type snmpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnmpLocation_Type.__name__ = "DisplayString"
_SnmpLocation_Object = MibScalar
snmpLocation = _SnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 7),
    _SnmpLocation_Type()
)
snmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLocation.setStatus("current")


class _SysObjectID_Type(DisplayString):
    """Custom type sysObjectID based on DisplayString"""
    defaultValue = OctetString("1.3.6.1.4.1.14125")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysObjectID_Type.__name__ = "DisplayString"
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 16, 8),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("current")
_Wmm_ObjectIdentity = ObjectIdentity
wmm = _Wmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 17)
)


class _WmmEnable_Type(Integer32):
    """Custom type wmmEnable based on Integer32"""
    defaultValue = 0

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


_WmmEnable_Type.__name__ = "Integer32"
_WmmEnable_Object = MibScalar
wmmEnable = _WmmEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 17, 1),
    _WmmEnable_Type()
)
wmmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wmmEnable.setStatus("current")
_Logemail_ObjectIdentity = ObjectIdentity
logemail = _Logemail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 20)
)


class _LogServerEnable_Type(Integer32):
    """Custom type logServerEnable based on Integer32"""
    defaultValue = 0

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


_LogServerEnable_Type.__name__ = "Integer32"
_LogServerEnable_Object = MibScalar
logServerEnable = _LogServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 20, 1),
    _LogServerEnable_Type()
)
logServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logServerEnable.setStatus("current")


class _LogServerIP_Type(IpAddress):
    """Custom type logServerIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_LogServerIP_Object = MibScalar
logServerIP = _LogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 20, 2),
    _LogServerIP_Type()
)
logServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logServerIP.setStatus("current")


class _LogLocalEnable_Type(Integer32):
    """Custom type logLocalEnable based on Integer32"""
    defaultValue = 0

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


_LogLocalEnable_Type.__name__ = "Integer32"
_LogLocalEnable_Object = MibScalar
logLocalEnable = _LogLocalEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 20, 3),
    _LogLocalEnable_Type()
)
logLocalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLocalEnable.setStatus("current")


class _LogLevel_Type(Integer32):
    """Custom type logLevel based on Integer32"""
    defaultValue = 8

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
        *(("alert", 1),
          ("all", 8),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("information", 6),
          ("notice", 5),
          ("warning", 4))
    )


_LogLevel_Type.__name__ = "Integer32"
_LogLevel_Object = MibScalar
logLevel = _LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 20, 4),
    _LogLevel_Type()
)
logLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLevel.setStatus("current")
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 21)
)


class _VpnPassthroughPPTP_Type(Integer32):
    """Custom type vpnPassthroughPPTP based on Integer32"""
    defaultValue = 1

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


_VpnPassthroughPPTP_Type.__name__ = "Integer32"
_VpnPassthroughPPTP_Object = MibScalar
vpnPassthroughPPTP = _VpnPassthroughPPTP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 21, 1),
    _VpnPassthroughPPTP_Type()
)
vpnPassthroughPPTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnPassthroughPPTP.setStatus("current")


class _VpnPassthroughL2TP_Type(Integer32):
    """Custom type vpnPassthroughL2TP based on Integer32"""
    defaultValue = 1

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


_VpnPassthroughL2TP_Type.__name__ = "Integer32"
_VpnPassthroughL2TP_Object = MibScalar
vpnPassthroughL2TP = _VpnPassthroughL2TP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 21, 2),
    _VpnPassthroughL2TP_Type()
)
vpnPassthroughL2TP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnPassthroughL2TP.setStatus("current")


class _VpnPassthroughIPSec_Type(Integer32):
    """Custom type vpnPassthroughIPSec based on Integer32"""
    defaultValue = 1

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


_VpnPassthroughIPSec_Type.__name__ = "Integer32"
_VpnPassthroughIPSec_Object = MibScalar
vpnPassthroughIPSec = _VpnPassthroughIPSec_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 21, 3),
    _VpnPassthroughIPSec_Type()
)
vpnPassthroughIPSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnPassthroughIPSec.setStatus("current")
_Traffic_ObjectIdentity = ObjectIdentity
traffic = _Traffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 22)
)


class _TcEnable_Type(Integer32):
    """Custom type tcEnable based on Integer32"""
    defaultValue = 0

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


_TcEnable_Type.__name__ = "Integer32"
_TcEnable_Object = MibScalar
tcEnable = _TcEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 22, 1),
    _TcEnable_Type()
)
tcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcEnable.setStatus("current")


class _TcInRate_Type(Integer32):
    """Custom type tcInRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_TcInRate_Type.__name__ = "Integer32"
_TcInRate_Object = MibScalar
tcInRate = _TcInRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 22, 2),
    _TcInRate_Type()
)
tcInRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcInRate.setStatus("current")


class _TcInBurst_Type(Integer32):
    """Custom type tcInBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_TcInBurst_Type.__name__ = "Integer32"
_TcInBurst_Object = MibScalar
tcInBurst = _TcInBurst_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 22, 3),
    _TcInBurst_Type()
)
tcInBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcInBurst.setStatus("current")


class _TcOutRate_Type(Integer32):
    """Custom type tcOutRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_TcOutRate_Type.__name__ = "Integer32"
_TcOutRate_Object = MibScalar
tcOutRate = _TcOutRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 22, 4),
    _TcOutRate_Type()
)
tcOutRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcOutRate.setStatus("current")


class _TcOutBurst_Type(Integer32):
    """Custom type tcOutBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_TcOutBurst_Type.__name__ = "Integer32"
_TcOutBurst_Object = MibScalar
tcOutBurst = _TcOutBurst_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 2, 22, 5),
    _TcOutBurst_Type()
)
tcOutBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcOutBurst.setStatus("current")
_Command_ObjectIdentity = ObjectIdentity
command = _Command_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3)
)
_SaveCmd_ObjectIdentity = ObjectIdentity
saveCmd = _SaveCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3, 1)
)


class _ExecuteSaveCmd_Type(Integer32):
    """Custom type executeSaveCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ExecuteSaveCmd_Type.__name__ = "Integer32"
_ExecuteSaveCmd_Object = MibScalar
executeSaveCmd = _ExecuteSaveCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3, 1, 1),
    _ExecuteSaveCmd_Type()
)
executeSaveCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    executeSaveCmd.setStatus("current")
_ResetCmd_ObjectIdentity = ObjectIdentity
resetCmd = _ResetCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3, 2)
)


class _ExecuteResetCmd_Type(Integer32):
    """Custom type executeResetCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ExecuteResetCmd_Type.__name__ = "Integer32"
_ExecuteResetCmd_Object = MibScalar
executeResetCmd = _ExecuteResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3, 2, 1),
    _ExecuteResetCmd_Type()
)
executeResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    executeResetCmd.setStatus("current")
_RebootCmd_ObjectIdentity = ObjectIdentity
rebootCmd = _RebootCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3, 3)
)


class _ExecuteRebootCmd_Type(Integer32):
    """Custom type executeRebootCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ExecuteRebootCmd_Type.__name__ = "Integer32"
_ExecuteRebootCmd_Object = MibScalar
executeRebootCmd = _ExecuteRebootCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 2, 3, 3, 1),
    _ExecuteRebootCmd_Type()
)
executeRebootCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    executeRebootCmd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENGENIUS-PRIVATE-MIB",
    **{"engenius": engenius,
       "engeniusprivate": engeniusprivate,
       "status": status,
       "system": system,
       "systemName": systemName,
       "sysPassword": sysPassword,
       "errMsg": errMsg,
       "statusWLANSTAAssoc": statusWLANSTAAssoc,
       "modelName": modelName,
       "wirelessMacAddress": wirelessMacAddress,
       "wanIPAddress": wanIPAddress,
       "wanSubnetMask": wanSubnetMask,
       "configuration": configuration,
       "wan": wan,
       "wanConnectionType": wanConnectionType,
       "wanGeneralAccount": wanGeneralAccount,
       "wanGeneralDomain": wanGeneralDomain,
       "wanGeneralIP": wanGeneralIP,
       "wanGeneralSubnetMask": wanGeneralSubnetMask,
       "wanGeneralGateway": wanGeneralGateway,
       "pppoe": pppoe,
       "wanPPPoELoginName": wanPPPoELoginName,
       "wanPPPoEPassword": wanPPPoEPassword,
       "wanPPPoEServiceName": wanPPPoEServiceName,
       "wanPPPoEConnectionType": wanPPPoEConnectionType,
       "wanPPPoEMaxIdleTime": wanPPPoEMaxIdleTime,
       "wanPPPoERedialPeriod": wanPPPoERedialPeriod,
       "dns": dns,
       "wanDNSSourc": wanDNSSourc,
       "wanPrimaryDNSIP": wanPrimaryDNSIP,
       "wanSecondaryDNSIP": wanSecondaryDNSIP,
       "mtu": mtu,
       "wanMTUMode": wanMTUMode,
       "wanMTU": wanMTU,
       "pppoeMTU": pppoeMTU,
       "landhcp": landhcp,
       "lanDHCPC": lanDHCPC,
       "lanIP": lanIP,
       "lanSubnetmask": lanSubnetmask,
       "lanGatewayIP": lanGatewayIP,
       "lanWINSAddr": lanWINSAddr,
       "lanDHCPSrvEnable": lanDHCPSrvEnable,
       "lanDHCPSrvStartAddr": lanDHCPSrvStartAddr,
       "lanDHCPSrvStopAddr": lanDHCPSrvStopAddr,
       "ntp": ntp,
       "timeSettingMode": timeSettingMode,
       "userNTPSrvMode": userNTPSrvMode,
       "userNTPSrvIP": userNTPSrvIP,
       "timeZone": timeZone,
       "admin": admin,
       "username": username,
       "remoteManagementEnable": remoteManagementEnable,
       "remoteUpgradeEnable": remoteUpgradeEnable,
       "remoteManagementPort": remoteManagementPort,
       "remoteManagementVLANID": remoteManagementVLANID,
       "wlan": wlan,
       "wlanMode": wlanMode,
       "chanBwMode": chanBwMode,
       "wlanaSSID": wlanaSSID,
       "wlanOpMode": wlanOpMode,
       "wlanCountryCode": wlanCountryCode,
       "wlanCountry": wlanCountry,
       "wlanChannel": wlanChannel,
       "wlanACLMode": wlanACLMode,
       "wlanOutdoorDistance": wlanOutdoorDistance,
       "wlanDataRate": wlanDataRate,
       "wlanTxPower": wlanTxPower,
       "antennasel": antennasel,
       "wlanBeaconInterval": wlanBeaconInterval,
       "wlanRTSTh": wlanRTSTh,
       "wlanFragLen": wlanFragLen,
       "wlanProtmode": wlanProtmode,
       "wlanPreferBSSID": wlanPreferBSSID,
       "wlanTable": wlanTable,
       "wlanTableEntry": wlanTableEntry,
       "wlanTableIndex": wlanTableIndex,
       "wlanEnable": wlanEnable,
       "wlanSSID": wlanSSID,
       "wlanHideSSID": wlanHideSSID,
       "wlanStaSeparation": wlanStaSeparation,
       "wlanVLANID": wlanVLANID,
       "wlanAuth": wlanAuth,
       "wlanEncryption": wlanEncryption,
       "wlanWepDefaultKeyIdx": wlanWepDefaultKeyIdx,
       "wlanWepKey": wlanWepKey,
       "wlanWpapskPassphrase": wlanWpapskPassphrase,
       "wlanWpaRadiusSrvIP": wlanWpaRadiusSrvIP,
       "wlanWpaRadiusSrvPort": wlanWpaRadiusSrvPort,
       "wlanWpaRadiusSrvSecret": wlanWpaRadiusSrvSecret,
       "wlanWpaGroupKeyUpdateInterval": wlanWpaGroupKeyUpdateInterval,
       "wlansta": wlansta,
       "wlanSTAAuth": wlanSTAAuth,
       "wlanSTAEncryption": wlanSTAEncryption,
       "wlanSTAWepDefaultKeyIdx": wlanSTAWepDefaultKeyIdx,
       "wlanSTAWepKey": wlanSTAWepKey,
       "wlanSTAWpapskPassphrase": wlanSTAWpapskPassphrase,
       "wlanmesh": wlanmesh,
       "wlanMESHSSID": wlanMESHSSID,
       "wlanMESHGateway": wlanMESHGateway,
       "wlanMESHAuth": wlanMESHAuth,
       "wlanMESHEncryption": wlanMESHEncryption,
       "wlanMESHWepDefaultKeyIdx": wlanMESHWepDefaultKeyIdx,
       "wlanMESHWepKey": wlanMESHWepKey,
       "wlanMESHWpapskPassphrase": wlanMESHWpapskPassphrase,
       "wlanstawds": wlanstawds,
       "staWDS": staWDS,
       "stp": stp,
       "stpMode": stpMode,
       "stpHelloTime": stpHelloTime,
       "stpMaxAge": stpMaxAge,
       "stpForwardDelay": stpForwardDelay,
       "stpPriority": stpPriority,
       "snmp": snmp,
       "snmpEnable": snmpEnable,
       "snmpCmntyRO": snmpCmntyRO,
       "snmpCmntyRW": snmpCmntyRW,
       "snmpTrapDstIP": snmpTrapDstIP,
       "snmpTrapCmnty": snmpTrapCmnty,
       "snmpCont": snmpCont,
       "snmpLocation": snmpLocation,
       "sysObjectID": sysObjectID,
       "wmm": wmm,
       "wmmEnable": wmmEnable,
       "logemail": logemail,
       "logServerEnable": logServerEnable,
       "logServerIP": logServerIP,
       "logLocalEnable": logLocalEnable,
       "logLevel": logLevel,
       "vpn": vpn,
       "vpnPassthroughPPTP": vpnPassthroughPPTP,
       "vpnPassthroughL2TP": vpnPassthroughL2TP,
       "vpnPassthroughIPSec": vpnPassthroughIPSec,
       "traffic": traffic,
       "tcEnable": tcEnable,
       "tcInRate": tcInRate,
       "tcInBurst": tcInBurst,
       "tcOutRate": tcOutRate,
       "tcOutBurst": tcOutBurst,
       "command": command,
       "saveCmd": saveCmd,
       "executeSaveCmd": executeSaveCmd,
       "resetCmd": resetCmd,
       "executeResetCmd": executeResetCmd,
       "rebootCmd": rebootCmd,
       "executeRebootCmd": executeRebootCmd}
)
