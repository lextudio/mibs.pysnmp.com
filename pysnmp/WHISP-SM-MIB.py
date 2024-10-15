# SNMP MIB module (WHISP-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WHISP-SM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:55 2024
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(dhcpRfPublicIp,
 whispBoxEsn) = mibBuilder.importSymbols(
    "WHISP-BOX-MIBV2-MIB",
    "dhcpRfPublicIp",
    "whispBoxEsn")

(whispAps,
 whispBox,
 whispModules,
 whispSm) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispAps",
    "whispBox",
    "whispModules",
    "whispSm")

(WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TCV2-MIB",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

whispSmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WhispSmConfig_ObjectIdentity = ObjectIdentity
whispSmConfig = _WhispSmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1)
)
_RfScanList_Type = DisplayString
_RfScanList_Object = MibScalar
rfScanList = _RfScanList_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 1),
    _RfScanList_Type()
)
rfScanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfScanList.setStatus("current")


class _PowerUpMode_Type(Integer32):
    """Custom type powerUpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aim", 1),
          ("operational", 0))
    )


_PowerUpMode_Type.__name__ = "Integer32"
_PowerUpMode_Object = MibScalar
powerUpMode = _PowerUpMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 2),
    _PowerUpMode_Type()
)
powerUpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerUpMode.setStatus("current")
_LanIpSm_Type = IpAddress
_LanIpSm_Object = MibScalar
lanIpSm = _LanIpSm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 3),
    _LanIpSm_Type()
)
lanIpSm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpSm.setStatus("current")
_LanMaskSm_Type = IpAddress
_LanMaskSm_Object = MibScalar
lanMaskSm = _LanMaskSm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 4),
    _LanMaskSm_Type()
)
lanMaskSm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanMaskSm.setStatus("current")
_DefaultGwSm_Type = IpAddress
_DefaultGwSm_Object = MibScalar
defaultGwSm = _DefaultGwSm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 5),
    _DefaultGwSm_Type()
)
defaultGwSm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGwSm.setStatus("current")


class _NetworkAccess_Type(Integer32):
    """Custom type networkAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("localIP", 0),
          ("publicIP", 1))
    )


_NetworkAccess_Type.__name__ = "Integer32"
_NetworkAccess_Object = MibScalar
networkAccess = _NetworkAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 6),
    _NetworkAccess_Type()
)
networkAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccess.setStatus("current")
_AuthKeySm_Type = DisplayString
_AuthKeySm_Object = MibScalar
authKeySm = _AuthKeySm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 7),
    _AuthKeySm_Type()
)
authKeySm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authKeySm.setStatus("current")


class _Enable8023link_Type(Integer32):
    """Custom type enable8023link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Enable8023link_Type.__name__ = "Integer32"
_Enable8023link_Object = MibScalar
enable8023link = _Enable8023link_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 8),
    _Enable8023link_Type()
)
enable8023link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable8023link.setStatus("current")


class _AuthKeyOption_Type(Integer32):
    """Custom type authKeyOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDefault", 0),
          ("useKeySet", 1))
    )


_AuthKeyOption_Type.__name__ = "Integer32"
_AuthKeyOption_Object = MibScalar
authKeyOption = _AuthKeyOption_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 9),
    _AuthKeyOption_Type()
)
authKeyOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authKeyOption.setStatus("current")


class _TimingPulseGated_Type(Integer32):
    """Custom type timingPulseGated based on Integer32"""
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


_TimingPulseGated_Type.__name__ = "Integer32"
_TimingPulseGated_Object = MibScalar
timingPulseGated = _TimingPulseGated_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 10),
    _TimingPulseGated_Type()
)
timingPulseGated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingPulseGated.setStatus("current")
_NaptPrivateIP_Type = IpAddress
_NaptPrivateIP_Object = MibScalar
naptPrivateIP = _NaptPrivateIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 11),
    _NaptPrivateIP_Type()
)
naptPrivateIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptPrivateIP.setStatus("current")
_NaptPrivateSubnetMask_Type = IpAddress
_NaptPrivateSubnetMask_Object = MibScalar
naptPrivateSubnetMask = _NaptPrivateSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 12),
    _NaptPrivateSubnetMask_Type()
)
naptPrivateSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptPrivateSubnetMask.setStatus("current")
_NaptPublicIP_Type = IpAddress
_NaptPublicIP_Object = MibScalar
naptPublicIP = _NaptPublicIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 13),
    _NaptPublicIP_Type()
)
naptPublicIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptPublicIP.setStatus("current")
_NaptPublicSubnetMask_Type = IpAddress
_NaptPublicSubnetMask_Object = MibScalar
naptPublicSubnetMask = _NaptPublicSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 14),
    _NaptPublicSubnetMask_Type()
)
naptPublicSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptPublicSubnetMask.setStatus("current")
_NaptPublicGatewayIP_Type = IpAddress
_NaptPublicGatewayIP_Object = MibScalar
naptPublicGatewayIP = _NaptPublicGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 15),
    _NaptPublicGatewayIP_Type()
)
naptPublicGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptPublicGatewayIP.setStatus("current")
_NaptRFPublicIP_Type = IpAddress
_NaptRFPublicIP_Object = MibScalar
naptRFPublicIP = _NaptRFPublicIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 16),
    _NaptRFPublicIP_Type()
)
naptRFPublicIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptRFPublicIP.setStatus("current")
_NaptRFPublicSubnetMask_Type = IpAddress
_NaptRFPublicSubnetMask_Object = MibScalar
naptRFPublicSubnetMask = _NaptRFPublicSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 17),
    _NaptRFPublicSubnetMask_Type()
)
naptRFPublicSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptRFPublicSubnetMask.setStatus("current")
_NaptRFPublicGateway_Type = IpAddress
_NaptRFPublicGateway_Object = MibScalar
naptRFPublicGateway = _NaptRFPublicGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 18),
    _NaptRFPublicGateway_Type()
)
naptRFPublicGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptRFPublicGateway.setStatus("current")


class _NaptEnable_Type(Integer32):
    """Custom type naptEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NaptEnable_Type.__name__ = "Integer32"
_NaptEnable_Object = MibScalar
naptEnable = _NaptEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 19),
    _NaptEnable_Type()
)
naptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptEnable.setStatus("current")
_ArpCacheTimeout_Type = Integer32
_ArpCacheTimeout_Object = MibScalar
arpCacheTimeout = _ArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 20),
    _ArpCacheTimeout_Type()
)
arpCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheTimeout.setStatus("current")
_TcpGarbageCollectTmout_Type = Integer32
_TcpGarbageCollectTmout_Object = MibScalar
tcpGarbageCollectTmout = _TcpGarbageCollectTmout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 21),
    _TcpGarbageCollectTmout_Type()
)
tcpGarbageCollectTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpGarbageCollectTmout.setStatus("current")
_UdpGarbageCollectTmout_Type = Integer32
_UdpGarbageCollectTmout_Object = MibScalar
udpGarbageCollectTmout = _UdpGarbageCollectTmout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 22),
    _UdpGarbageCollectTmout_Type()
)
udpGarbageCollectTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpGarbageCollectTmout.setStatus("current")


class _DhcpClientEnable_Type(Integer32):
    """Custom type dhcpClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpClientEnable_Type.__name__ = "Integer32"
_DhcpClientEnable_Object = MibScalar
dhcpClientEnable = _DhcpClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 23),
    _DhcpClientEnable_Type()
)
dhcpClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientEnable.setStatus("obsolete")


class _DhcpServerEnable_Type(Integer32):
    """Custom type dhcpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpServerEnable_Type.__name__ = "Integer32"
_DhcpServerEnable_Object = MibScalar
dhcpServerEnable = _DhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 24),
    _DhcpServerEnable_Type()
)
dhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerEnable.setStatus("current")
_DhcpServerLeaseTime_Type = Integer32
_DhcpServerLeaseTime_Object = MibScalar
dhcpServerLeaseTime = _DhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 25),
    _DhcpServerLeaseTime_Type()
)
dhcpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerLeaseTime.setStatus("current")
_DhcpIPStart_Type = IpAddress
_DhcpIPStart_Object = MibScalar
dhcpIPStart = _DhcpIPStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 26),
    _DhcpIPStart_Type()
)
dhcpIPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpIPStart.setStatus("current")


class _DnsAutomatic_Type(Integer32):
    """Custom type dnsAutomatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatically", 1),
          ("manually", 0))
    )


_DnsAutomatic_Type.__name__ = "Integer32"
_DnsAutomatic_Object = MibScalar
dnsAutomatic = _DnsAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 27),
    _DnsAutomatic_Type()
)
dnsAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsAutomatic.setStatus("current")
_PrefferedDNSIP_Type = IpAddress
_PrefferedDNSIP_Object = MibScalar
prefferedDNSIP = _PrefferedDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 28),
    _PrefferedDNSIP_Type()
)
prefferedDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedDNSIP.setStatus("current")
_AlternateDNSIP_Type = IpAddress
_AlternateDNSIP_Object = MibScalar
alternateDNSIP = _AlternateDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 29),
    _AlternateDNSIP_Type()
)
alternateDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateDNSIP.setStatus("current")
_DmzIP_Type = IpAddress
_DmzIP_Object = MibScalar
dmzIP = _DmzIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 30),
    _DmzIP_Type()
)
dmzIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzIP.setStatus("current")


class _DmzEnable_Type(Integer32):
    """Custom type dmzEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DmzEnable_Type.__name__ = "Integer32"
_DmzEnable_Object = MibScalar
dmzEnable = _DmzEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 31),
    _DmzEnable_Type()
)
dmzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzEnable.setStatus("current")
_DhcpNumIPsToLease_Type = Integer32
_DhcpNumIPsToLease_Object = MibScalar
dhcpNumIPsToLease = _DhcpNumIPsToLease_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 32),
    _DhcpNumIPsToLease_Type()
)
dhcpNumIPsToLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpNumIPsToLease.setStatus("current")


class _PppoeFilter_Type(Integer32):
    """Custom type pppoeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_PppoeFilter_Type.__name__ = "Integer32"
_PppoeFilter_Object = MibScalar
pppoeFilter = _PppoeFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 33),
    _PppoeFilter_Type()
)
pppoeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeFilter.setStatus("obsolete")


class _SmbFilter_Type(Integer32):
    """Custom type smbFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_SmbFilter_Type.__name__ = "Integer32"
_SmbFilter_Object = MibScalar
smbFilter = _SmbFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 34),
    _SmbFilter_Type()
)
smbFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smbFilter.setStatus("obsolete")


class _SnmpFilter_Type(Integer32):
    """Custom type snmpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_SnmpFilter_Type.__name__ = "Integer32"
_SnmpFilter_Object = MibScalar
snmpFilter = _SnmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 35),
    _SnmpFilter_Type()
)
snmpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFilter.setStatus("obsolete")


class _UserP1Filter_Type(Integer32):
    """Custom type userP1Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UserP1Filter_Type.__name__ = "Integer32"
_UserP1Filter_Object = MibScalar
userP1Filter = _UserP1Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 36),
    _UserP1Filter_Type()
)
userP1Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userP1Filter.setStatus("obsolete")


class _UserP2Filter_Type(Integer32):
    """Custom type userP2Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UserP2Filter_Type.__name__ = "Integer32"
_UserP2Filter_Object = MibScalar
userP2Filter = _UserP2Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 37),
    _UserP2Filter_Type()
)
userP2Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userP2Filter.setStatus("obsolete")


class _UserP3Filter_Type(Integer32):
    """Custom type userP3Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UserP3Filter_Type.__name__ = "Integer32"
_UserP3Filter_Object = MibScalar
userP3Filter = _UserP3Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 38),
    _UserP3Filter_Type()
)
userP3Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userP3Filter.setStatus("obsolete")


class _AllOtherIpFilter_Type(Integer32):
    """Custom type allOtherIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_AllOtherIpFilter_Type.__name__ = "Integer32"
_AllOtherIpFilter_Object = MibScalar
allOtherIpFilter = _AllOtherIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 39),
    _AllOtherIpFilter_Type()
)
allOtherIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allOtherIpFilter.setStatus("obsolete")


class _UpLinkBCastFilter_Type(Integer32):
    """Custom type upLinkBCastFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UpLinkBCastFilter_Type.__name__ = "Integer32"
_UpLinkBCastFilter_Object = MibScalar
upLinkBCastFilter = _UpLinkBCastFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 40),
    _UpLinkBCastFilter_Type()
)
upLinkBCastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLinkBCastFilter.setStatus("obsolete")


class _ArpFilter_Type(Integer32):
    """Custom type arpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_ArpFilter_Type.__name__ = "Integer32"
_ArpFilter_Object = MibScalar
arpFilter = _ArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 41),
    _ArpFilter_Type()
)
arpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpFilter.setStatus("obsolete")


class _AllOthersFilter_Type(Integer32):
    """Custom type allOthersFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_AllOthersFilter_Type.__name__ = "Integer32"
_AllOthersFilter_Object = MibScalar
allOthersFilter = _AllOthersFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 42),
    _AllOthersFilter_Type()
)
allOthersFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allOthersFilter.setStatus("obsolete")
_UserDefinedPort1_Type = Integer32
_UserDefinedPort1_Object = MibScalar
userDefinedPort1 = _UserDefinedPort1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 43),
    _UserDefinedPort1_Type()
)
userDefinedPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefinedPort1.setStatus("obsolete")


class _Port1TCPFilter_Type(Integer32):
    """Custom type port1TCPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port1TCPFilter_Type.__name__ = "Integer32"
_Port1TCPFilter_Object = MibScalar
port1TCPFilter = _Port1TCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 44),
    _Port1TCPFilter_Type()
)
port1TCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1TCPFilter.setStatus("obsolete")


class _Port1UDPFilter_Type(Integer32):
    """Custom type port1UDPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port1UDPFilter_Type.__name__ = "Integer32"
_Port1UDPFilter_Object = MibScalar
port1UDPFilter = _Port1UDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 45),
    _Port1UDPFilter_Type()
)
port1UDPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1UDPFilter.setStatus("obsolete")
_UserDefinedPort2_Type = Integer32
_UserDefinedPort2_Object = MibScalar
userDefinedPort2 = _UserDefinedPort2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 46),
    _UserDefinedPort2_Type()
)
userDefinedPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefinedPort2.setStatus("obsolete")


class _Port2TCPFilter_Type(Integer32):
    """Custom type port2TCPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port2TCPFilter_Type.__name__ = "Integer32"
_Port2TCPFilter_Object = MibScalar
port2TCPFilter = _Port2TCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 47),
    _Port2TCPFilter_Type()
)
port2TCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2TCPFilter.setStatus("obsolete")


class _Port2UDPFilter_Type(Integer32):
    """Custom type port2UDPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port2UDPFilter_Type.__name__ = "Integer32"
_Port2UDPFilter_Object = MibScalar
port2UDPFilter = _Port2UDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 48),
    _Port2UDPFilter_Type()
)
port2UDPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2UDPFilter.setStatus("obsolete")
_UserDefinedPort3_Type = Integer32
_UserDefinedPort3_Object = MibScalar
userDefinedPort3 = _UserDefinedPort3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 49),
    _UserDefinedPort3_Type()
)
userDefinedPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefinedPort3.setStatus("obsolete")


class _Port3TCPFilter_Type(Integer32):
    """Custom type port3TCPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port3TCPFilter_Type.__name__ = "Integer32"
_Port3TCPFilter_Object = MibScalar
port3TCPFilter = _Port3TCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 50),
    _Port3TCPFilter_Type()
)
port3TCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3TCPFilter.setStatus("obsolete")


class _Port3UDPFilter_Type(Integer32):
    """Custom type port3UDPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port3UDPFilter_Type.__name__ = "Integer32"
_Port3UDPFilter_Object = MibScalar
port3UDPFilter = _Port3UDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 51),
    _Port3UDPFilter_Type()
)
port3UDPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3UDPFilter.setStatus("obsolete")


class _BootpcFilter_Type(Integer32):
    """Custom type bootpcFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_BootpcFilter_Type.__name__ = "Integer32"
_BootpcFilter_Object = MibScalar
bootpcFilter = _BootpcFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 52),
    _BootpcFilter_Type()
)
bootpcFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpcFilter.setStatus("obsolete")


class _BootpsFilter_Type(Integer32):
    """Custom type bootpsFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_BootpsFilter_Type.__name__ = "Integer32"
_BootpsFilter_Object = MibScalar
bootpsFilter = _BootpsFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 53),
    _BootpsFilter_Type()
)
bootpsFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpsFilter.setStatus("obsolete")


class _Ip4MultFilter_Type(Integer32):
    """Custom type ip4MultFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Ip4MultFilter_Type.__name__ = "Integer32"
_Ip4MultFilter_Object = MibScalar
ip4MultFilter = _Ip4MultFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 54),
    _Ip4MultFilter_Type()
)
ip4MultFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4MultFilter.setStatus("obsolete")
_IngressVID_Type = Integer32
_IngressVID_Object = MibScalar
ingressVID = _IngressVID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 55),
    _IngressVID_Type()
)
ingressVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressVID.setStatus("current")
_LowPriorityUplinkCIR_Type = Integer32
_LowPriorityUplinkCIR_Object = MibScalar
lowPriorityUplinkCIR = _LowPriorityUplinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 56),
    _LowPriorityUplinkCIR_Type()
)
lowPriorityUplinkCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowPriorityUplinkCIR.setStatus("current")
_LowPriorityDownlinkCIR_Type = Integer32
_LowPriorityDownlinkCIR_Object = MibScalar
lowPriorityDownlinkCIR = _LowPriorityDownlinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 57),
    _LowPriorityDownlinkCIR_Type()
)
lowPriorityDownlinkCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowPriorityDownlinkCIR.setStatus("current")


class _HiPriorityChannel_Type(Integer32):
    """Custom type hiPriorityChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enable", 1))
    )


_HiPriorityChannel_Type.__name__ = "Integer32"
_HiPriorityChannel_Object = MibScalar
hiPriorityChannel = _HiPriorityChannel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 58),
    _HiPriorityChannel_Type()
)
hiPriorityChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiPriorityChannel.setStatus("current")
_HiPriorityUplinkCIR_Type = Integer32
_HiPriorityUplinkCIR_Object = MibScalar
hiPriorityUplinkCIR = _HiPriorityUplinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 59),
    _HiPriorityUplinkCIR_Type()
)
hiPriorityUplinkCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiPriorityUplinkCIR.setStatus("current")
_HiPriorityDownlinkCIR_Type = Integer32
_HiPriorityDownlinkCIR_Object = MibScalar
hiPriorityDownlinkCIR = _HiPriorityDownlinkCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 60),
    _HiPriorityDownlinkCIR_Type()
)
hiPriorityDownlinkCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiPriorityDownlinkCIR.setStatus("current")


class _SmRateAdapt_Type(Integer32):
    """Custom type smRateAdapt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onex", 0),
          ("onextwox", 1),
          ("onextwoxthreex", 2))
    )


_SmRateAdapt_Type.__name__ = "Integer32"
_SmRateAdapt_Object = MibScalar
smRateAdapt = _SmRateAdapt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 61),
    _SmRateAdapt_Type()
)
smRateAdapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRateAdapt.setStatus("obsolete")
_UpLnkDataRate_Type = Integer32
_UpLnkDataRate_Object = MibScalar
upLnkDataRate = _UpLnkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 62),
    _UpLnkDataRate_Type()
)
upLnkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLnkDataRate.setStatus("current")
_UpLnkLimit_Type = Integer32
_UpLnkLimit_Object = MibScalar
upLnkLimit = _UpLnkLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 63),
    _UpLnkLimit_Type()
)
upLnkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLnkLimit.setStatus("current")
_DwnLnkDataRate_Type = Integer32
_DwnLnkDataRate_Object = MibScalar
dwnLnkDataRate = _DwnLnkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 64),
    _DwnLnkDataRate_Type()
)
dwnLnkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkDataRate.setStatus("current")
_DwnLnkLimit_Type = Integer32
_DwnLnkLimit_Object = MibScalar
dwnLnkLimit = _DwnLnkLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 65),
    _DwnLnkLimit_Type()
)
dwnLnkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkLimit.setStatus("current")


class _DfsConfig_Type(Integer32):
    """Custom type dfsConfig based on Integer32"""
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


_DfsConfig_Type.__name__ = "Integer32"
_DfsConfig_Object = MibScalar
dfsConfig = _DfsConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 66),
    _DfsConfig_Type()
)
dfsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsConfig.setStatus("obsolete")


class _EthAccessFilterEnable_Type(Integer32):
    """Custom type ethAccessFilterEnable based on Integer32"""
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


_EthAccessFilterEnable_Type.__name__ = "Integer32"
_EthAccessFilterEnable_Object = MibScalar
ethAccessFilterEnable = _EthAccessFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 67),
    _EthAccessFilterEnable_Type()
)
ethAccessFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAccessFilterEnable.setStatus("obsolete")


class _IpAccessFilterEnable_Type(Integer32):
    """Custom type ipAccessFilterEnable based on Integer32"""
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


_IpAccessFilterEnable_Type.__name__ = "Integer32"
_IpAccessFilterEnable_Object = MibScalar
ipAccessFilterEnable = _IpAccessFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 68),
    _IpAccessFilterEnable_Type()
)
ipAccessFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessFilterEnable.setStatus("current")
_AllowedIPAccess1_Type = IpAddress
_AllowedIPAccess1_Object = MibScalar
allowedIPAccess1 = _AllowedIPAccess1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 69),
    _AllowedIPAccess1_Type()
)
allowedIPAccess1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess1.setStatus("current")
_AllowedIPAccess2_Type = IpAddress
_AllowedIPAccess2_Object = MibScalar
allowedIPAccess2 = _AllowedIPAccess2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 70),
    _AllowedIPAccess2_Type()
)
allowedIPAccess2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess2.setStatus("current")
_AllowedIPAccess3_Type = IpAddress
_AllowedIPAccess3_Object = MibScalar
allowedIPAccess3 = _AllowedIPAccess3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 71),
    _AllowedIPAccess3_Type()
)
allowedIPAccess3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess3.setStatus("current")


class _RfDhcpState_Type(Integer32):
    """Custom type rfDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RfDhcpState_Type.__name__ = "Integer32"
_RfDhcpState_Object = MibScalar
rfDhcpState = _RfDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 72),
    _RfDhcpState_Type()
)
rfDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfDhcpState.setStatus("current")


class _BCastMIR_Type(Integer32):
    """Custom type bCastMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("disabled", 0)
    )


_BCastMIR_Type.__name__ = "Integer32"
_BCastMIR_Object = MibScalar
bCastMIR = _BCastMIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 73),
    _BCastMIR_Type()
)
bCastMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bCastMIR.setStatus("current")


class _BhsReReg_Type(Integer32):
    """Custom type bhsReReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BhsReReg_Type.__name__ = "Integer32"
_BhsReReg_Object = MibScalar
bhsReReg = _BhsReReg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 74),
    _BhsReReg_Type()
)
bhsReReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bhsReReg.setStatus("obsolete")


class _SmLEDModeFlag_Type(Integer32):
    """Custom type smLEDModeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 0),
          ("revised", 1))
    )


_SmLEDModeFlag_Type.__name__ = "Integer32"
_SmLEDModeFlag_Object = MibScalar
smLEDModeFlag = _SmLEDModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 75),
    _SmLEDModeFlag_Type()
)
smLEDModeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smLEDModeFlag.setStatus("current")


class _EthAccessEnable_Type(Integer32):
    """Custom type ethAccessEnable based on Integer32"""
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


_EthAccessEnable_Type.__name__ = "Integer32"
_EthAccessEnable_Object = MibScalar
ethAccessEnable = _EthAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 76),
    _EthAccessEnable_Type()
)
ethAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAccessEnable.setStatus("current")


class _PppoeEnable_Type(Integer32):
    """Custom type pppoeEnable based on Integer32"""
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


_PppoeEnable_Type.__name__ = "Integer32"
_PppoeEnable_Object = MibScalar
pppoeEnable = _PppoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 77),
    _PppoeEnable_Type()
)
pppoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeEnable.setStatus("current")


class _PppoeAuthenticationType_Type(Integer32):
    """Custom type pppoeAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chap-pap", 1),
          ("none", 0))
    )


_PppoeAuthenticationType_Type.__name__ = "Integer32"
_PppoeAuthenticationType_Object = MibScalar
pppoeAuthenticationType = _PppoeAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 78),
    _PppoeAuthenticationType_Type()
)
pppoeAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAuthenticationType.setStatus("current")
_PppoeAccessConcentrator_Type = DisplayString
_PppoeAccessConcentrator_Object = MibScalar
pppoeAccessConcentrator = _PppoeAccessConcentrator_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 79),
    _PppoeAccessConcentrator_Type()
)
pppoeAccessConcentrator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAccessConcentrator.setStatus("current")
_PppoeServiceName_Type = DisplayString
_PppoeServiceName_Object = MibScalar
pppoeServiceName = _PppoeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 80),
    _PppoeServiceName_Type()
)
pppoeServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeServiceName.setStatus("current")
_PppoeUserName_Type = DisplayString
_PppoeUserName_Object = MibScalar
pppoeUserName = _PppoeUserName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 81),
    _PppoeUserName_Type()
)
pppoeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeUserName.setStatus("current")
_PppoePassword_Type = DisplayString
_PppoePassword_Object = MibScalar
pppoePassword = _PppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 82),
    _PppoePassword_Type()
)
pppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePassword.setStatus("current")


class _PppoeTCPMSSClampEnable_Type(Integer32):
    """Custom type pppoeTCPMSSClampEnable based on Integer32"""
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


_PppoeTCPMSSClampEnable_Type.__name__ = "Integer32"
_PppoeTCPMSSClampEnable_Object = MibScalar
pppoeTCPMSSClampEnable = _PppoeTCPMSSClampEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 83),
    _PppoeTCPMSSClampEnable_Type()
)
pppoeTCPMSSClampEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTCPMSSClampEnable.setStatus("current")


class _PppoeMTUOverrideEnable_Type(Integer32):
    """Custom type pppoeMTUOverrideEnable based on Integer32"""
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


_PppoeMTUOverrideEnable_Type.__name__ = "Integer32"
_PppoeMTUOverrideEnable_Object = MibScalar
pppoeMTUOverrideEnable = _PppoeMTUOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 84),
    _PppoeMTUOverrideEnable_Type()
)
pppoeMTUOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeMTUOverrideEnable.setStatus("current")


class _PppoeMTUOverrideValue_Type(Integer32):
    """Custom type pppoeMTUOverrideValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1492),
    )


_PppoeMTUOverrideValue_Type.__name__ = "Integer32"
_PppoeMTUOverrideValue_Object = MibScalar
pppoeMTUOverrideValue = _PppoeMTUOverrideValue_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 85),
    _PppoeMTUOverrideValue_Type()
)
pppoeMTUOverrideValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeMTUOverrideValue.setStatus("current")


class _PppoeTimerType_Type(Integer32):
    """Custom type pppoeTimerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idleTimeout", 2),
          ("keepAlive", 1))
    )


_PppoeTimerType_Type.__name__ = "Integer32"
_PppoeTimerType_Object = MibScalar
pppoeTimerType = _PppoeTimerType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 86),
    _PppoeTimerType_Type()
)
pppoeTimerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTimerType.setStatus("current")
_PppoeTimeoutPeriod_Type = Integer32
_PppoeTimeoutPeriod_Object = MibScalar
pppoeTimeoutPeriod = _PppoeTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 87),
    _PppoeTimeoutPeriod_Type()
)
pppoeTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeTimeoutPeriod.setStatus("current")


class _TimedSpectrumAnalysisDuration_Type(Integer32):
    """Custom type timedSpectrumAnalysisDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TimedSpectrumAnalysisDuration_Type.__name__ = "Integer32"
_TimedSpectrumAnalysisDuration_Object = MibScalar
timedSpectrumAnalysisDuration = _TimedSpectrumAnalysisDuration_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 88),
    _TimedSpectrumAnalysisDuration_Type()
)
timedSpectrumAnalysisDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timedSpectrumAnalysisDuration.setStatus("deprecated")


class _SpectrumAnalysisOnBoot_Type(Integer32):
    """Custom type spectrumAnalysisOnBoot based on Integer32"""
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


_SpectrumAnalysisOnBoot_Type.__name__ = "Integer32"
_SpectrumAnalysisOnBoot_Object = MibScalar
spectrumAnalysisOnBoot = _SpectrumAnalysisOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 89),
    _SpectrumAnalysisOnBoot_Type()
)
spectrumAnalysisOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumAnalysisOnBoot.setStatus("current")


class _SpectrumAnalysisAction_Type(Integer32):
    """Custom type spectrumAnalysisAction based on Integer32"""
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
        *(("idleCompleteSpectrumAnalysis", 4),
          ("idleNoSpectrumAnalysis", 3),
          ("inProgressContinuousSpectrumAnalysis", 6),
          ("inProgressTimedSpectrumAnalysis", 5),
          ("startContinuousSpectrumAnalysis", 2),
          ("startTimedSpectrumAnalysis", 1),
          ("stopSpectrumAnalysis", 0))
    )


_SpectrumAnalysisAction_Type.__name__ = "Integer32"
_SpectrumAnalysisAction_Object = MibScalar
spectrumAnalysisAction = _SpectrumAnalysisAction_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 90),
    _SpectrumAnalysisAction_Type()
)
spectrumAnalysisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumAnalysisAction.setStatus("deprecated")


class _PppoeConnectOD_Type(Integer32):
    """Custom type pppoeConnectOD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("connectOnDemand", 1)
    )


_PppoeConnectOD_Type.__name__ = "Integer32"
_PppoeConnectOD_Object = MibScalar
pppoeConnectOD = _PppoeConnectOD_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 91),
    _PppoeConnectOD_Type()
)
pppoeConnectOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeConnectOD.setStatus("current")


class _PppoeDisconnectOD_Type(Integer32):
    """Custom type pppoeDisconnectOD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnectOnDemand", 1)
    )


_PppoeDisconnectOD_Type.__name__ = "Integer32"
_PppoeDisconnectOD_Object = MibScalar
pppoeDisconnectOD = _PppoeDisconnectOD_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 92),
    _PppoeDisconnectOD_Type()
)
pppoeDisconnectOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeDisconnectOD.setStatus("current")


class _SmAntennaType_Type(Integer32):
    """Custom type smAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("integrated", 0))
    )


_SmAntennaType_Type.__name__ = "Integer32"
_SmAntennaType_Object = MibScalar
smAntennaType = _SmAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 93),
    _SmAntennaType_Type()
)
smAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smAntennaType.setStatus("obsolete")


class _NatConnectionType_Type(Integer32):
    """Custom type natConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("pppoe", 2),
          ("staticIP", 0))
    )


_NatConnectionType_Type.__name__ = "Integer32"
_NatConnectionType_Object = MibScalar
natConnectionType = _NatConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 94),
    _NatConnectionType_Type()
)
natConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natConnectionType.setStatus("current")


class _WanPingReplyEnable_Type(Integer32):
    """Custom type wanPingReplyEnable based on Integer32"""
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


_WanPingReplyEnable_Type.__name__ = "Integer32"
_WanPingReplyEnable_Object = MibScalar
wanPingReplyEnable = _WanPingReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 95),
    _WanPingReplyEnable_Type()
)
wanPingReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanPingReplyEnable.setStatus("current")


class _PacketFilterDirection_Type(Integer32):
    """Custom type packetFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_PacketFilterDirection_Type.__name__ = "Integer32"
_PacketFilterDirection_Object = MibScalar
packetFilterDirection = _PacketFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 96),
    _PacketFilterDirection_Type()
)
packetFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetFilterDirection.setStatus("obsolete")


class _ColorCode2_Type(Integer32):
    """Custom type colorCode2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode2_Type.__name__ = "Integer32"
_ColorCode2_Object = MibScalar
colorCode2 = _ColorCode2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 97),
    _ColorCode2_Type()
)
colorCode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode2.setStatus("current")


class _ColorCodepriority2_Type(Integer32):
    """Custom type colorCodepriority2 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority2_Type.__name__ = "Integer32"
_ColorCodepriority2_Object = MibScalar
colorCodepriority2 = _ColorCodepriority2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 98),
    _ColorCodepriority2_Type()
)
colorCodepriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority2.setStatus("current")


class _ColorCode3_Type(Integer32):
    """Custom type colorCode3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode3_Type.__name__ = "Integer32"
_ColorCode3_Object = MibScalar
colorCode3 = _ColorCode3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 99),
    _ColorCode3_Type()
)
colorCode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode3.setStatus("current")


class _ColorCodepriority3_Type(Integer32):
    """Custom type colorCodepriority3 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority3_Type.__name__ = "Integer32"
_ColorCodepriority3_Object = MibScalar
colorCodepriority3 = _ColorCodepriority3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 100),
    _ColorCodepriority3_Type()
)
colorCodepriority3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority3.setStatus("current")


class _ColorCode4_Type(Integer32):
    """Custom type colorCode4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode4_Type.__name__ = "Integer32"
_ColorCode4_Object = MibScalar
colorCode4 = _ColorCode4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 101),
    _ColorCode4_Type()
)
colorCode4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode4.setStatus("current")


class _ColorCodepriority4_Type(Integer32):
    """Custom type colorCodepriority4 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority4_Type.__name__ = "Integer32"
_ColorCodepriority4_Object = MibScalar
colorCodepriority4 = _ColorCodepriority4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 102),
    _ColorCodepriority4_Type()
)
colorCodepriority4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority4.setStatus("current")


class _ColorCode5_Type(Integer32):
    """Custom type colorCode5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode5_Type.__name__ = "Integer32"
_ColorCode5_Object = MibScalar
colorCode5 = _ColorCode5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 103),
    _ColorCode5_Type()
)
colorCode5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode5.setStatus("current")


class _ColorCodepriority5_Type(Integer32):
    """Custom type colorCodepriority5 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority5_Type.__name__ = "Integer32"
_ColorCodepriority5_Object = MibScalar
colorCodepriority5 = _ColorCodepriority5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 104),
    _ColorCodepriority5_Type()
)
colorCodepriority5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority5.setStatus("current")


class _ColorCode6_Type(Integer32):
    """Custom type colorCode6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode6_Type.__name__ = "Integer32"
_ColorCode6_Object = MibScalar
colorCode6 = _ColorCode6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 105),
    _ColorCode6_Type()
)
colorCode6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode6.setStatus("current")


class _ColorCodepriority6_Type(Integer32):
    """Custom type colorCodepriority6 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority6_Type.__name__ = "Integer32"
_ColorCodepriority6_Object = MibScalar
colorCodepriority6 = _ColorCodepriority6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 106),
    _ColorCodepriority6_Type()
)
colorCodepriority6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority6.setStatus("current")


class _ColorCode7_Type(Integer32):
    """Custom type colorCode7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode7_Type.__name__ = "Integer32"
_ColorCode7_Object = MibScalar
colorCode7 = _ColorCode7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 107),
    _ColorCode7_Type()
)
colorCode7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode7.setStatus("current")


class _ColorCodepriority7_Type(Integer32):
    """Custom type colorCodepriority7 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority7_Type.__name__ = "Integer32"
_ColorCodepriority7_Object = MibScalar
colorCodepriority7 = _ColorCodepriority7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 108),
    _ColorCodepriority7_Type()
)
colorCodepriority7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority7.setStatus("current")


class _ColorCode8_Type(Integer32):
    """Custom type colorCode8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode8_Type.__name__ = "Integer32"
_ColorCode8_Object = MibScalar
colorCode8 = _ColorCode8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 109),
    _ColorCode8_Type()
)
colorCode8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode8.setStatus("current")


class _ColorCodepriority8_Type(Integer32):
    """Custom type colorCodepriority8 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority8_Type.__name__ = "Integer32"
_ColorCodepriority8_Object = MibScalar
colorCodepriority8 = _ColorCodepriority8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 110),
    _ColorCodepriority8_Type()
)
colorCodepriority8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority8.setStatus("current")


class _ColorCode9_Type(Integer32):
    """Custom type colorCode9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode9_Type.__name__ = "Integer32"
_ColorCode9_Object = MibScalar
colorCode9 = _ColorCode9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 111),
    _ColorCode9_Type()
)
colorCode9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode9.setStatus("current")


class _ColorCodepriority9_Type(Integer32):
    """Custom type colorCodepriority9 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority9_Type.__name__ = "Integer32"
_ColorCodepriority9_Object = MibScalar
colorCodepriority9 = _ColorCodepriority9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 112),
    _ColorCodepriority9_Type()
)
colorCodepriority9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority9.setStatus("current")


class _ColorCode10_Type(Integer32):
    """Custom type colorCode10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode10_Type.__name__ = "Integer32"
_ColorCode10_Object = MibScalar
colorCode10 = _ColorCode10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 113),
    _ColorCode10_Type()
)
colorCode10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode10.setStatus("current")


class _ColorCodepriority10_Type(Integer32):
    """Custom type colorCodepriority10 based on Integer32"""
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
        *(("disable", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ColorCodepriority10_Type.__name__ = "Integer32"
_ColorCodepriority10_Object = MibScalar
colorCodepriority10 = _ColorCodepriority10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 114),
    _ColorCodepriority10_Type()
)
colorCodepriority10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodepriority10.setStatus("current")


class _NatDNSProxyEnable_Type(Integer32):
    """Custom type natDNSProxyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatDNSProxyEnable_Type.__name__ = "Integer32"
_NatDNSProxyEnable_Object = MibScalar
natDNSProxyEnable = _NatDNSProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 115),
    _NatDNSProxyEnable_Type()
)
natDNSProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDNSProxyEnable.setStatus("current")


class _AllIpv4Filter_Type(Integer32):
    """Custom type allIpv4Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_AllIpv4Filter_Type.__name__ = "Integer32"
_AllIpv4Filter_Object = MibScalar
allIpv4Filter = _AllIpv4Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 116),
    _AllIpv4Filter_Type()
)
allIpv4Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allIpv4Filter.setStatus("obsolete")


class _SpectrumAnalysisDisplay_Type(Integer32):
    """Custom type spectrumAnalysisDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("averaging", 0),
          ("instantaneous", 1))
    )


_SpectrumAnalysisDisplay_Type.__name__ = "Integer32"
_SpectrumAnalysisDisplay_Object = MibScalar
spectrumAnalysisDisplay = _SpectrumAnalysisDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 117),
    _SpectrumAnalysisDisplay_Type()
)
spectrumAnalysisDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumAnalysisDisplay.setStatus("current")


class _SyslogSMXmitSetting_Type(Integer32):
    """Custom type syslogSMXmitSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("obtain-from-AP", 0))
    )


_SyslogSMXmitSetting_Type.__name__ = "Integer32"
_SyslogSMXmitSetting_Object = MibScalar
syslogSMXmitSetting = _SyslogSMXmitSetting_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 118),
    _SyslogSMXmitSetting_Type()
)
syslogSMXmitSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSMXmitSetting.setStatus("deprecated")


class _SyslogServerApPreferred_Type(Integer32):
    """Custom type syslogServerApPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("use-AP-preferred", 1),
          ("use-local", 0))
    )


_SyslogServerApPreferred_Type.__name__ = "Integer32"
_SyslogServerApPreferred_Object = MibScalar
syslogServerApPreferred = _SyslogServerApPreferred_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 119),
    _SyslogServerApPreferred_Type()
)
syslogServerApPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerApPreferred.setStatus("current")


class _SyslogMinLevelApPreferred_Type(Integer32):
    """Custom type syslogMinLevelApPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("use-AP-preferred", 1),
          ("use-local", 0))
    )


_SyslogMinLevelApPreferred_Type.__name__ = "Integer32"
_SyslogMinLevelApPreferred_Object = MibScalar
syslogMinLevelApPreferred = _SyslogMinLevelApPreferred_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 120),
    _SyslogMinLevelApPreferred_Type()
)
syslogMinLevelApPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMinLevelApPreferred.setStatus("current")


class _SyslogSMXmitControl_Type(Integer32):
    """Custom type syslogSMXmitControl based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("obtain-from-AP-default-disabled", 0),
          ("obtain-from-AP-default-enabled", 1))
    )


_SyslogSMXmitControl_Type.__name__ = "Integer32"
_SyslogSMXmitControl_Object = MibScalar
syslogSMXmitControl = _SyslogSMXmitControl_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 121),
    _SyslogSMXmitControl_Type()
)
syslogSMXmitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSMXmitControl.setStatus("current")
_EapPeerAAAServerCommonName_Type = DisplayString
_EapPeerAAAServerCommonName_Object = MibScalar
eapPeerAAAServerCommonName = _EapPeerAAAServerCommonName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 126),
    _EapPeerAAAServerCommonName_Type()
)
eapPeerAAAServerCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapPeerAAAServerCommonName.setStatus("current")


class _RfScanListBandFilter_Type(Integer32):
    """Custom type rfScanListBandFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("band5400", 8),
          ("band5700", 9))
    )


_RfScanListBandFilter_Type.__name__ = "Integer32"
_RfScanListBandFilter_Object = MibScalar
rfScanListBandFilter = _RfScanListBandFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 127),
    _RfScanListBandFilter_Type()
)
rfScanListBandFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfScanListBandFilter.setStatus("obsolete")
_UpLnkMaxBurstDataRate_Type = Integer32
_UpLnkMaxBurstDataRate_Object = MibScalar
upLnkMaxBurstDataRate = _UpLnkMaxBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 128),
    _UpLnkMaxBurstDataRate_Type()
)
upLnkMaxBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLnkMaxBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    upLnkMaxBurstDataRate.setUnits("Kilobits/sec")
_DwnLnkMaxBurstDataRate_Type = Integer32
_DwnLnkMaxBurstDataRate_Object = MibScalar
dwnLnkMaxBurstDataRate = _DwnLnkMaxBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 129),
    _DwnLnkMaxBurstDataRate_Type()
)
dwnLnkMaxBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkMaxBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dwnLnkMaxBurstDataRate.setUnits("Kilobits/sec")
_CyclicPrefixScan_Type = DisplayString
_CyclicPrefixScan_Object = MibScalar
cyclicPrefixScan = _CyclicPrefixScan_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 130),
    _CyclicPrefixScan_Type()
)
cyclicPrefixScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyclicPrefixScan.setStatus("current")
_BandwidthScan_Type = DisplayString
_BandwidthScan_Object = MibScalar
bandwidthScan = _BandwidthScan_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 131),
    _BandwidthScan_Type()
)
bandwidthScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthScan.setStatus("current")


class _ApSelection_Type(Integer32):
    """Custom type apSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("optimizeForThroughput", 0),
          ("powerLevel", 1))
    )


_ApSelection_Type.__name__ = "Integer32"
_ApSelection_Object = MibScalar
apSelection = _ApSelection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 132),
    _ApSelection_Type()
)
apSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSelection.setStatus("current")


class _RadioBandscanConfig_Type(Integer32):
    """Custom type radioBandscanConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("delayed", 1),
          ("instant", 0))
    )


_RadioBandscanConfig_Type.__name__ = "Integer32"
_RadioBandscanConfig_Object = MibScalar
radioBandscanConfig = _RadioBandscanConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 133),
    _RadioBandscanConfig_Type()
)
radioBandscanConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioBandscanConfig.setStatus("current")
_Forcepoweradjust_Type = Integer32
_Forcepoweradjust_Object = MibScalar
forcepoweradjust = _Forcepoweradjust_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 134),
    _Forcepoweradjust_Type()
)
forcepoweradjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcepoweradjust.setStatus("current")
_ClearBerrResults_Type = Integer32
_ClearBerrResults_Object = MibScalar
clearBerrResults = _ClearBerrResults_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 135),
    _ClearBerrResults_Type()
)
clearBerrResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearBerrResults.setStatus("current")
_Berrautoupdateflag_Type = Integer32
_Berrautoupdateflag_Object = MibScalar
berrautoupdateflag = _Berrautoupdateflag_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 136),
    _Berrautoupdateflag_Type()
)
berrautoupdateflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berrautoupdateflag.setStatus("current")


class _TestSMBER_Type(Integer32):
    """Custom type testSMBER based on Integer32"""
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


_TestSMBER_Type.__name__ = "Integer32"
_TestSMBER_Object = MibScalar
testSMBER = _TestSMBER_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 137),
    _TestSMBER_Type()
)
testSMBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testSMBER.setStatus("current")


class _AllowedIPAccessNMLength1_Type(Integer32):
    """Custom type allowedIPAccessNMLength1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AllowedIPAccessNMLength1_Type.__name__ = "Integer32"
_AllowedIPAccessNMLength1_Object = MibScalar
allowedIPAccessNMLength1 = _AllowedIPAccessNMLength1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 138),
    _AllowedIPAccessNMLength1_Type()
)
allowedIPAccessNMLength1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccessNMLength1.setStatus("current")


class _AllowedIPAccessNMLength2_Type(Integer32):
    """Custom type allowedIPAccessNMLength2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AllowedIPAccessNMLength2_Type.__name__ = "Integer32"
_AllowedIPAccessNMLength2_Object = MibScalar
allowedIPAccessNMLength2 = _AllowedIPAccessNMLength2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 139),
    _AllowedIPAccessNMLength2_Type()
)
allowedIPAccessNMLength2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccessNMLength2.setStatus("current")


class _AllowedIPAccessNMLength3_Type(Integer32):
    """Custom type allowedIPAccessNMLength3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AllowedIPAccessNMLength3_Type.__name__ = "Integer32"
_AllowedIPAccessNMLength3_Object = MibScalar
allowedIPAccessNMLength3 = _AllowedIPAccessNMLength3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 140),
    _AllowedIPAccessNMLength3_Type()
)
allowedIPAccessNMLength3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccessNMLength3.setStatus("current")


class _NaptRemoteManage_Type(Integer32):
    """Custom type naptRemoteManage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable-standalone", 1),
          ("enable-wan", 2))
    )


_NaptRemoteManage_Type.__name__ = "Integer32"
_NaptRemoteManage_Object = MibScalar
naptRemoteManage = _NaptRemoteManage_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 141),
    _NaptRemoteManage_Type()
)
naptRemoteManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptRemoteManage.setStatus("current")


class _SpectrumAnalysisScanBandwidth_Type(Integer32):
    """Custom type spectrumAnalysisScanBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth10MHz", 1),
          ("bandwidth20MHz", 2),
          ("bandwidth5MHz", 0))
    )


_SpectrumAnalysisScanBandwidth_Type.__name__ = "Integer32"
_SpectrumAnalysisScanBandwidth_Object = MibScalar
spectrumAnalysisScanBandwidth = _SpectrumAnalysisScanBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 142),
    _SpectrumAnalysisScanBandwidth_Type()
)
spectrumAnalysisScanBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumAnalysisScanBandwidth.setStatus("current")


class _BerDeModSelect_Type(Integer32):
    """Custom type berDeModSelect based on Integer32"""
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
        *(("qam-16", 1),
          ("qam-256", 3),
          ("qam-64", 2),
          ("qpsk", 0))
    )


_BerDeModSelect_Type.__name__ = "Integer32"
_BerDeModSelect_Object = MibScalar
berDeModSelect = _BerDeModSelect_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 143),
    _BerDeModSelect_Type()
)
berDeModSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berDeModSelect.setStatus("current")
_MulticastVCRcvRate_Type = DisplayString
_MulticastVCRcvRate_Object = MibScalar
multicastVCRcvRate = _MulticastVCRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 144),
    _MulticastVCRcvRate_Type()
)
multicastVCRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVCRcvRate.setStatus("current")


class _Pmp430ApRegistrationOptions_Type(Integer32):
    """Custom type pmp430ApRegistrationOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("pmp430", 1),
          ("pmp450", 2))
    )


_Pmp430ApRegistrationOptions_Type.__name__ = "Integer32"
_Pmp430ApRegistrationOptions_Object = MibScalar
pmp430ApRegistrationOptions = _Pmp430ApRegistrationOptions_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 145),
    _Pmp430ApRegistrationOptions_Type()
)
pmp430ApRegistrationOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmp430ApRegistrationOptions.setStatus("current")


class _SwitchRadioModeAndReboot_Type(Integer32):
    """Custom type switchRadioModeAndReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finishedReboot", 0),
          ("switchRadioModeAndReboot", 1))
    )


_SwitchRadioModeAndReboot_Type.__name__ = "Integer32"
_SwitchRadioModeAndReboot_Object = MibScalar
switchRadioModeAndReboot = _SwitchRadioModeAndReboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 1, 146),
    _SwitchRadioModeAndReboot_Type()
)
switchRadioModeAndReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchRadioModeAndReboot.setStatus("current")
_WhispSmStatus_ObjectIdentity = ObjectIdentity
whispSmStatus = _WhispSmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2)
)
_SessionStatus_Type = DisplayString
_SessionStatus_Object = MibScalar
sessionStatus = _SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 1),
    _SessionStatus_Type()
)
sessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionStatus.setStatus("current")
_Rssi_Type = Integer32
_Rssi_Object = MibScalar
rssi = _Rssi_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 2),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("current")


class _Jitter_Type(Gauge32):
    """Custom type jitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Jitter_Type.__name__ = "Gauge32"
_Jitter_Object = MibScalar
jitter = _Jitter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 3),
    _Jitter_Type()
)
jitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitter.setStatus("current")
_AirDelay_Type = Unsigned32
_AirDelay_Object = MibScalar
airDelay = _AirDelay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 4),
    _AirDelay_Type()
)
airDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airDelay.setStatus("current")
_RadioSlicingSm_Type = Integer32
_RadioSlicingSm_Object = MibScalar
radioSlicingSm = _RadioSlicingSm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 5),
    _RadioSlicingSm_Type()
)
radioSlicingSm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioSlicingSm.setStatus("obsolete")
_RadioTxGainSm_Type = Integer32
_RadioTxGainSm_Object = MibScalar
radioTxGainSm = _RadioTxGainSm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 6),
    _RadioTxGainSm_Type()
)
radioTxGainSm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxGainSm.setStatus("current")
_CalibrationStatus_Type = DisplayString
_CalibrationStatus_Object = MibScalar
calibrationStatus = _CalibrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 7),
    _CalibrationStatus_Type()
)
calibrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calibrationStatus.setStatus("deprecated")
_RadioDbm_Type = DisplayString
_RadioDbm_Object = MibScalar
radioDbm = _RadioDbm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 8),
    _RadioDbm_Type()
)
radioDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDbm.setStatus("current")
_RegisteredToAp_Type = DisplayString
_RegisteredToAp_Object = MibScalar
registeredToAp = _RegisteredToAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 9),
    _RegisteredToAp_Type()
)
registeredToAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registeredToAp.setStatus("current")
_DhcpCip_Type = IpAddress
_DhcpCip_Object = MibScalar
dhcpCip = _DhcpCip_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 10),
    _DhcpCip_Type()
)
dhcpCip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCip.setStatus("current")
_DhcpSip_Type = IpAddress
_DhcpSip_Object = MibScalar
dhcpSip = _DhcpSip_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 11),
    _DhcpSip_Type()
)
dhcpSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSip.setStatus("current")
_DhcpClientLease_Type = TimeTicks
_DhcpClientLease_Object = MibScalar
dhcpClientLease = _DhcpClientLease_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 12),
    _DhcpClientLease_Type()
)
dhcpClientLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientLease.setStatus("current")
_DhcpCSMask_Type = IpAddress
_DhcpCSMask_Object = MibScalar
dhcpCSMask = _DhcpCSMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 13),
    _DhcpCSMask_Type()
)
dhcpCSMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCSMask.setStatus("current")
_DhcpDfltRterIP_Type = IpAddress
_DhcpDfltRterIP_Object = MibScalar
dhcpDfltRterIP = _DhcpDfltRterIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 14),
    _DhcpDfltRterIP_Type()
)
dhcpDfltRterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDfltRterIP.setStatus("current")
_Dhcpcdns1_Type = IpAddress
_Dhcpcdns1_Object = MibScalar
dhcpcdns1 = _Dhcpcdns1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 15),
    _Dhcpcdns1_Type()
)
dhcpcdns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpcdns1.setStatus("current")
_Dhcpcdns2_Type = IpAddress
_Dhcpcdns2_Object = MibScalar
dhcpcdns2 = _Dhcpcdns2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 16),
    _Dhcpcdns2_Type()
)
dhcpcdns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpcdns2.setStatus("current")
_Dhcpcdns3_Type = IpAddress
_Dhcpcdns3_Object = MibScalar
dhcpcdns3 = _Dhcpcdns3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 17),
    _Dhcpcdns3_Type()
)
dhcpcdns3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpcdns3.setStatus("current")
_DhcpDomName_Type = DisplayString
_DhcpDomName_Object = MibScalar
dhcpDomName = _DhcpDomName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 18),
    _DhcpDomName_Type()
)
dhcpDomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDomName.setStatus("current")
_DhcpServerTable_Object = MibTable
dhcpServerTable = _DhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 19)
)
if mibBuilder.loadTexts:
    dhcpServerTable.setStatus("current")
_DhcpServerEntry_Object = MibTableRow
dhcpServerEntry = _DhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 19, 1)
)
dhcpServerEntry.setIndexNames(
    (0, "WHISP-SM-MIB", "hostIp"),
)
if mibBuilder.loadTexts:
    dhcpServerEntry.setStatus("current")
_HostIp_Type = IpAddress
_HostIp_Object = MibTableColumn
hostIp = _HostIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 19, 1, 1),
    _HostIp_Type()
)
hostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIp.setStatus("current")
_HostMacAddress_Type = PhysAddress
_HostMacAddress_Object = MibTableColumn
hostMacAddress = _HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 19, 1, 2),
    _HostMacAddress_Type()
)
hostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMacAddress.setStatus("current")
_HostLease_Type = TimeTicks
_HostLease_Object = MibTableColumn
hostLease = _HostLease_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 19, 1, 3),
    _HostLease_Type()
)
hostLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostLease.setStatus("current")
_AdaptRate_Type = DisplayString
_AdaptRate_Object = MibScalar
adaptRate = _AdaptRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 20),
    _AdaptRate_Type()
)
adaptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptRate.setStatus("current")
_RadioDbmInt_Type = Integer32
_RadioDbmInt_Object = MibScalar
radioDbmInt = _RadioDbmInt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 21),
    _RadioDbmInt_Type()
)
radioDbmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDbmInt.setStatus("current")
_DfsStatus_Type = DisplayString
_DfsStatus_Object = MibScalar
dfsStatus = _DfsStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 22),
    _DfsStatus_Type()
)
dfsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStatus.setStatus("current")
_RadioTxPwr_Type = DisplayString
_RadioTxPwr_Object = MibScalar
radioTxPwr = _RadioTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 23),
    _RadioTxPwr_Type()
)
radioTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxPwr.setStatus("current")
_ActiveRegion_Type = DisplayString
_ActiveRegion_Object = MibScalar
activeRegion = _ActiveRegion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 24),
    _ActiveRegion_Type()
)
activeRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeRegion.setStatus("current")


class _SnmpBerLevel_Type(Integer32):
    """Custom type snmpBerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fourLevelOrMimo16QAM", 4),
          ("mimo256QAM", 8),
          ("mimo64QAM", 6),
          ("twoLevelOrMimoQPSK", 2))
    )


_SnmpBerLevel_Type.__name__ = "Integer32"
_SnmpBerLevel_Object = MibScalar
snmpBerLevel = _SnmpBerLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 25),
    _SnmpBerLevel_Type()
)
snmpBerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpBerLevel.setStatus("current")
_NbBitsRcvd_Type = Counter64
_NbBitsRcvd_Object = MibScalar
nbBitsRcvd = _NbBitsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 26),
    _NbBitsRcvd_Type()
)
nbBitsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbBitsRcvd.setStatus("current")
_NbPriBitsErr_Type = Counter32
_NbPriBitsErr_Object = MibScalar
nbPriBitsErr = _NbPriBitsErr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 27),
    _NbPriBitsErr_Type()
)
nbPriBitsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbPriBitsErr.setStatus("current")
_NbSndBitsErr_Type = Counter32
_NbSndBitsErr_Object = MibScalar
nbSndBitsErr = _NbSndBitsErr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 28),
    _NbSndBitsErr_Type()
)
nbSndBitsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSndBitsErr.setStatus("current")
_PrimaryBER_Type = Integer32
_PrimaryBER_Object = MibScalar
primaryBER = _PrimaryBER_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 29),
    _PrimaryBER_Type()
)
primaryBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryBER.setStatus("obsolete")
_SecondaryBER_Type = Integer32
_SecondaryBER_Object = MibScalar
secondaryBER = _SecondaryBER_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 30),
    _SecondaryBER_Type()
)
secondaryBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryBER.setStatus("obsolete")
_TotalBER_Type = Integer32
_TotalBER_Object = MibScalar
totalBER = _TotalBER_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 31),
    _TotalBER_Type()
)
totalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBER.setStatus("obsolete")
_MinRSSI_Type = Integer32
_MinRSSI_Object = MibScalar
minRSSI = _MinRSSI_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 32),
    _MinRSSI_Type()
)
minRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minRSSI.setStatus("current")
_MaxRSSI_Type = Integer32
_MaxRSSI_Object = MibScalar
maxRSSI = _MaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 33),
    _MaxRSSI_Type()
)
maxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRSSI.setStatus("current")


class _MinJitter_Type(Gauge32):
    """Custom type minJitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MinJitter_Type.__name__ = "Gauge32"
_MinJitter_Object = MibScalar
minJitter = _MinJitter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 34),
    _MinJitter_Type()
)
minJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minJitter.setStatus("current")


class _MaxJitter_Type(Gauge32):
    """Custom type maxJitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MaxJitter_Type.__name__ = "Gauge32"
_MaxJitter_Object = MibScalar
maxJitter = _MaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 35),
    _MaxJitter_Type()
)
maxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxJitter.setStatus("current")
_SmSessionTimer_Type = TimeTicks
_SmSessionTimer_Object = MibScalar
smSessionTimer = _SmSessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 36),
    _SmSessionTimer_Type()
)
smSessionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSessionTimer.setStatus("current")
_PppoeSessionStatus_Type = DisplayString
_PppoeSessionStatus_Object = MibScalar
pppoeSessionStatus = _PppoeSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 37),
    _PppoeSessionStatus_Type()
)
pppoeSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionStatus.setStatus("current")
_PppoeSessionID_Type = Integer32
_PppoeSessionID_Object = MibScalar
pppoeSessionID = _PppoeSessionID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 38),
    _PppoeSessionID_Type()
)
pppoeSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionID.setStatus("current")
_PppoeIPCPAddress_Type = IpAddress
_PppoeIPCPAddress_Object = MibScalar
pppoeIPCPAddress = _PppoeIPCPAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 39),
    _PppoeIPCPAddress_Type()
)
pppoeIPCPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIPCPAddress.setStatus("current")


class _PppoeMTUOverrideEn_Type(Integer32):
    """Custom type pppoeMTUOverrideEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PppoeMTUOverrideEn_Type.__name__ = "Integer32"
_PppoeMTUOverrideEn_Object = MibScalar
pppoeMTUOverrideEn = _PppoeMTUOverrideEn_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 40),
    _PppoeMTUOverrideEn_Type()
)
pppoeMTUOverrideEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeMTUOverrideEn.setStatus("current")
_PppoeMTUValue_Type = Integer32
_PppoeMTUValue_Object = MibScalar
pppoeMTUValue = _PppoeMTUValue_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 41),
    _PppoeMTUValue_Type()
)
pppoeMTUValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeMTUValue.setStatus("current")


class _PppoeTimerTypeValue_Type(Integer32):
    """Custom type pppoeTimerTypeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("idleTimeout", 2),
          ("keepAlive", 1))
    )


_PppoeTimerTypeValue_Type.__name__ = "Integer32"
_PppoeTimerTypeValue_Object = MibScalar
pppoeTimerTypeValue = _PppoeTimerTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 42),
    _PppoeTimerTypeValue_Type()
)
pppoeTimerTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTimerTypeValue.setStatus("current")
_PppoeTimeoutValue_Type = Integer32
_PppoeTimeoutValue_Object = MibScalar
pppoeTimeoutValue = _PppoeTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 43),
    _PppoeTimeoutValue_Type()
)
pppoeTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTimeoutValue.setStatus("current")
_PppoeDNSServer1_Type = IpAddress
_PppoeDNSServer1_Object = MibScalar
pppoeDNSServer1 = _PppoeDNSServer1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 44),
    _PppoeDNSServer1_Type()
)
pppoeDNSServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeDNSServer1.setStatus("current")
_PppoeDNSServer2_Type = IpAddress
_PppoeDNSServer2_Object = MibScalar
pppoeDNSServer2 = _PppoeDNSServer2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 45),
    _PppoeDNSServer2_Type()
)
pppoeDNSServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeDNSServer2.setStatus("current")
_PppoeControlBytesSent_Type = Counter32
_PppoeControlBytesSent_Object = MibScalar
pppoeControlBytesSent = _PppoeControlBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 46),
    _PppoeControlBytesSent_Type()
)
pppoeControlBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeControlBytesSent.setStatus("current")
_PppoeControlBytesReceived_Type = Counter32
_PppoeControlBytesReceived_Object = MibScalar
pppoeControlBytesReceived = _PppoeControlBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 47),
    _PppoeControlBytesReceived_Type()
)
pppoeControlBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeControlBytesReceived.setStatus("current")
_PppoeDataBytesSent_Type = Counter32
_PppoeDataBytesSent_Object = MibScalar
pppoeDataBytesSent = _PppoeDataBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 48),
    _PppoeDataBytesSent_Type()
)
pppoeDataBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeDataBytesSent.setStatus("current")
_PppoeDataBytesReceived_Type = Counter32
_PppoeDataBytesReceived_Object = MibScalar
pppoeDataBytesReceived = _PppoeDataBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 49),
    _PppoeDataBytesReceived_Type()
)
pppoeDataBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeDataBytesReceived.setStatus("current")


class _PppoeEnabledStatus_Type(Integer32):
    """Custom type pppoeEnabledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PppoeEnabledStatus_Type.__name__ = "Integer32"
_PppoeEnabledStatus_Object = MibScalar
pppoeEnabledStatus = _PppoeEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 50),
    _PppoeEnabledStatus_Type()
)
pppoeEnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeEnabledStatus.setStatus("current")


class _PppoeTCPMSSClampEnableStatus_Type(Integer32):
    """Custom type pppoeTCPMSSClampEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PppoeTCPMSSClampEnableStatus_Type.__name__ = "Integer32"
_PppoeTCPMSSClampEnableStatus_Object = MibScalar
pppoeTCPMSSClampEnableStatus = _PppoeTCPMSSClampEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 51),
    _PppoeTCPMSSClampEnableStatus_Type()
)
pppoeTCPMSSClampEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeTCPMSSClampEnableStatus.setStatus("current")
_PppoeACNameStatus_Type = DisplayString
_PppoeACNameStatus_Object = MibScalar
pppoeACNameStatus = _PppoeACNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 52),
    _PppoeACNameStatus_Type()
)
pppoeACNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeACNameStatus.setStatus("current")
_PppoeSvcNameStatus_Type = DisplayString
_PppoeSvcNameStatus_Object = MibScalar
pppoeSvcNameStatus = _PppoeSvcNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 53),
    _PppoeSvcNameStatus_Type()
)
pppoeSvcNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSvcNameStatus.setStatus("current")
_PppoeSessUptime_Type = TimeTicks
_PppoeSessUptime_Object = MibScalar
pppoeSessUptime = _PppoeSessUptime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 54),
    _PppoeSessUptime_Type()
)
pppoeSessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessUptime.setStatus("current")
_PrimaryBERDisplay_Type = DisplayString
_PrimaryBERDisplay_Object = MibScalar
primaryBERDisplay = _PrimaryBERDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 55),
    _PrimaryBERDisplay_Type()
)
primaryBERDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryBERDisplay.setStatus("current")
_SecondaryBERDisplay_Type = DisplayString
_SecondaryBERDisplay_Object = MibScalar
secondaryBERDisplay = _SecondaryBERDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 56),
    _SecondaryBERDisplay_Type()
)
secondaryBERDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryBERDisplay.setStatus("current")
_TotalBERDisplay_Type = DisplayString
_TotalBERDisplay_Object = MibScalar
totalBERDisplay = _TotalBERDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 57),
    _TotalBERDisplay_Type()
)
totalBERDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBERDisplay.setStatus("current")
_MinRadioDbm_Type = Integer32
_MinRadioDbm_Object = MibScalar
minRadioDbm = _MinRadioDbm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 58),
    _MinRadioDbm_Type()
)
minRadioDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minRadioDbm.setStatus("current")
_MaxRadioDbm_Type = Integer32
_MaxRadioDbm_Object = MibScalar
maxRadioDbm = _MaxRadioDbm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 59),
    _MaxRadioDbm_Type()
)
maxRadioDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRadioDbm.setStatus("current")
_PppoeSessIdleTime_Type = TimeTicks
_PppoeSessIdleTime_Object = MibScalar
pppoeSessIdleTime = _PppoeSessIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 60),
    _PppoeSessIdleTime_Type()
)
pppoeSessIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessIdleTime.setStatus("current")
_RadioDbmAvg_Type = Integer32
_RadioDbmAvg_Object = MibScalar
radioDbmAvg = _RadioDbmAvg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 61),
    _RadioDbmAvg_Type()
)
radioDbmAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDbmAvg.setStatus("current")
_ZoltarFPGAFreqOffset_Type = Integer32
_ZoltarFPGAFreqOffset_Object = MibScalar
zoltarFPGAFreqOffset = _ZoltarFPGAFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 62),
    _ZoltarFPGAFreqOffset_Type()
)
zoltarFPGAFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoltarFPGAFreqOffset.setStatus("current")
_ZoltarSWFreqOffset_Type = Integer32
_ZoltarSWFreqOffset_Object = MibScalar
zoltarSWFreqOffset = _ZoltarSWFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 63),
    _ZoltarSWFreqOffset_Type()
)
zoltarSWFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoltarSWFreqOffset.setStatus("current")
_AirDelayns_Type = Unsigned32
_AirDelayns_Object = MibScalar
airDelayns = _AirDelayns_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 64),
    _AirDelayns_Type()
)
airDelayns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airDelayns.setStatus("current")
_CurrentColorCode_Type = Integer32
_CurrentColorCode_Object = MibScalar
currentColorCode = _CurrentColorCode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 65),
    _CurrentColorCode_Type()
)
currentColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentColorCode.setStatus("current")


class _CurrentColorCodePri_Type(Integer32):
    """Custom type currentColorCodePri based on Integer32"""
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
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_CurrentColorCodePri_Type.__name__ = "Integer32"
_CurrentColorCodePri_Object = MibScalar
currentColorCodePri = _CurrentColorCodePri_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 66),
    _CurrentColorCodePri_Type()
)
currentColorCodePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentColorCodePri.setStatus("current")
_CurrentChanFreq_Type = Unsigned32
_CurrentChanFreq_Object = MibScalar
currentChanFreq = _CurrentChanFreq_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 67),
    _CurrentChanFreq_Type()
)
currentChanFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentChanFreq.setStatus("current")
_LinkQualityBeacon_Type = DisplayString
_LinkQualityBeacon_Object = MibScalar
linkQualityBeacon = _LinkQualityBeacon_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 68),
    _LinkQualityBeacon_Type()
)
linkQualityBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityBeacon.setStatus("current")
_DhcpServerPktXmt_Type = Counter32
_DhcpServerPktXmt_Object = MibScalar
dhcpServerPktXmt = _DhcpServerPktXmt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 72),
    _DhcpServerPktXmt_Type()
)
dhcpServerPktXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerPktXmt.setStatus("current")
_DhcpServerPktRcv_Type = Counter32
_DhcpServerPktRcv_Object = MibScalar
dhcpServerPktRcv = _DhcpServerPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 73),
    _DhcpServerPktRcv_Type()
)
dhcpServerPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerPktRcv.setStatus("current")
_DhcpServerPktToss_Type = Counter32
_DhcpServerPktToss_Object = MibScalar
dhcpServerPktToss = _DhcpServerPktToss_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 74),
    _DhcpServerPktToss_Type()
)
dhcpServerPktToss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerPktToss.setStatus("current")
_ReceiveFragmentsModulationPercentage_Type = DisplayString
_ReceiveFragmentsModulationPercentage_Object = MibScalar
receiveFragmentsModulationPercentage = _ReceiveFragmentsModulationPercentage_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 86),
    _ReceiveFragmentsModulationPercentage_Type()
)
receiveFragmentsModulationPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFragmentsModulationPercentage.setStatus("current")
_FragmentsReceived1XVertical_Type = Counter32
_FragmentsReceived1XVertical_Object = MibScalar
fragmentsReceived1XVertical = _FragmentsReceived1XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 87),
    _FragmentsReceived1XVertical_Type()
)
fragmentsReceived1XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived1XVertical.setStatus("current")
_FragmentsReceived2XVertical_Type = Counter32
_FragmentsReceived2XVertical_Object = MibScalar
fragmentsReceived2XVertical = _FragmentsReceived2XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 88),
    _FragmentsReceived2XVertical_Type()
)
fragmentsReceived2XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived2XVertical.setStatus("current")
_FragmentsReceived3XVertical_Type = Counter32
_FragmentsReceived3XVertical_Object = MibScalar
fragmentsReceived3XVertical = _FragmentsReceived3XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 89),
    _FragmentsReceived3XVertical_Type()
)
fragmentsReceived3XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived3XVertical.setStatus("current")
_FragmentsReceived4XVertical_Type = Counter32
_FragmentsReceived4XVertical_Object = MibScalar
fragmentsReceived4XVertical = _FragmentsReceived4XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 90),
    _FragmentsReceived4XVertical_Type()
)
fragmentsReceived4XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived4XVertical.setStatus("current")
_LinkQualityData1XVertical_Type = DisplayString
_LinkQualityData1XVertical_Object = MibScalar
linkQualityData1XVertical = _LinkQualityData1XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 91),
    _LinkQualityData1XVertical_Type()
)
linkQualityData1XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData1XVertical.setStatus("current")
_LinkQualityData2XVertical_Type = DisplayString
_LinkQualityData2XVertical_Object = MibScalar
linkQualityData2XVertical = _LinkQualityData2XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 92),
    _LinkQualityData2XVertical_Type()
)
linkQualityData2XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData2XVertical.setStatus("current")
_LinkQualityData3XVertical_Type = DisplayString
_LinkQualityData3XVertical_Object = MibScalar
linkQualityData3XVertical = _LinkQualityData3XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 93),
    _LinkQualityData3XVertical_Type()
)
linkQualityData3XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData3XVertical.setStatus("current")
_LinkQualityData4XVertical_Type = DisplayString
_LinkQualityData4XVertical_Object = MibScalar
linkQualityData4XVertical = _LinkQualityData4XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 94),
    _LinkQualityData4XVertical_Type()
)
linkQualityData4XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData4XVertical.setStatus("current")
_SignalToNoiseRatioSMVertical_Type = Integer32
_SignalToNoiseRatioSMVertical_Object = MibScalar
signalToNoiseRatioSMVertical = _SignalToNoiseRatioSMVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 95),
    _SignalToNoiseRatioSMVertical_Type()
)
signalToNoiseRatioSMVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioSMVertical.setStatus("current")
_RfStatTxSuppressionCount_Type = Counter32
_RfStatTxSuppressionCount_Object = MibScalar
rfStatTxSuppressionCount = _RfStatTxSuppressionCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 96),
    _RfStatTxSuppressionCount_Type()
)
rfStatTxSuppressionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatTxSuppressionCount.setStatus("current")
_BridgecbUplinkCreditRate_Type = Unsigned32
_BridgecbUplinkCreditRate_Object = MibScalar
bridgecbUplinkCreditRate = _BridgecbUplinkCreditRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 97),
    _BridgecbUplinkCreditRate_Type()
)
bridgecbUplinkCreditRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgecbUplinkCreditRate.setStatus("current")
_BridgecbUplinkCreditLimit_Type = Unsigned32
_BridgecbUplinkCreditLimit_Object = MibScalar
bridgecbUplinkCreditLimit = _BridgecbUplinkCreditLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 98),
    _BridgecbUplinkCreditLimit_Type()
)
bridgecbUplinkCreditLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgecbUplinkCreditLimit.setStatus("current")
_BridgecbDownlinkCreditRate_Type = Unsigned32
_BridgecbDownlinkCreditRate_Object = MibScalar
bridgecbDownlinkCreditRate = _BridgecbDownlinkCreditRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 99),
    _BridgecbDownlinkCreditRate_Type()
)
bridgecbDownlinkCreditRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgecbDownlinkCreditRate.setStatus("current")
_BridgecbDownlinkCreditLimit_Type = Unsigned32
_BridgecbDownlinkCreditLimit_Object = MibScalar
bridgecbDownlinkCreditLimit = _BridgecbDownlinkCreditLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 100),
    _BridgecbDownlinkCreditLimit_Type()
)
bridgecbDownlinkCreditLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgecbDownlinkCreditLimit.setStatus("current")
_MimoQpskBerDisplay_Type = DisplayString
_MimoQpskBerDisplay_Object = MibScalar
mimoQpskBerDisplay = _MimoQpskBerDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 101),
    _MimoQpskBerDisplay_Type()
)
mimoQpskBerDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimoQpskBerDisplay.setStatus("current")
_Mimo16QamBerDisplay_Type = DisplayString
_Mimo16QamBerDisplay_Object = MibScalar
mimo16QamBerDisplay = _Mimo16QamBerDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 102),
    _Mimo16QamBerDisplay_Type()
)
mimo16QamBerDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimo16QamBerDisplay.setStatus("current")
_Mimo64QamBerDisplay_Type = DisplayString
_Mimo64QamBerDisplay_Object = MibScalar
mimo64QamBerDisplay = _Mimo64QamBerDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 103),
    _Mimo64QamBerDisplay_Type()
)
mimo64QamBerDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimo64QamBerDisplay.setStatus("current")
_Mimo256QamBerDisplay_Type = DisplayString
_Mimo256QamBerDisplay_Object = MibScalar
mimo256QamBerDisplay = _Mimo256QamBerDisplay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 104),
    _Mimo256QamBerDisplay_Type()
)
mimo256QamBerDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimo256QamBerDisplay.setStatus("current")
_MimoBerRcvModulationType_Type = DisplayString
_MimoBerRcvModulationType_Object = MibScalar
mimoBerRcvModulationType = _MimoBerRcvModulationType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 105),
    _MimoBerRcvModulationType_Type()
)
mimoBerRcvModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimoBerRcvModulationType.setStatus("current")
_SignalToNoiseRatioSMHorizontal_Type = Integer32
_SignalToNoiseRatioSMHorizontal_Object = MibScalar
signalToNoiseRatioSMHorizontal = _SignalToNoiseRatioSMHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 106),
    _SignalToNoiseRatioSMHorizontal_Type()
)
signalToNoiseRatioSMHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioSMHorizontal.setStatus("current")
_MaxRadioDbmDeprecated_Type = Integer32
_MaxRadioDbmDeprecated_Object = MibScalar
maxRadioDbmDeprecated = _MaxRadioDbmDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 107),
    _MaxRadioDbmDeprecated_Type()
)
maxRadioDbmDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRadioDbmDeprecated.setStatus("deprecated")
_SignalStrengthRatio_Type = DisplayString
_SignalStrengthRatio_Object = MibScalar
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 108),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("current")
_FragmentsReceived1XHorizontal_Type = Counter32
_FragmentsReceived1XHorizontal_Object = MibScalar
fragmentsReceived1XHorizontal = _FragmentsReceived1XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 109),
    _FragmentsReceived1XHorizontal_Type()
)
fragmentsReceived1XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived1XHorizontal.setStatus("current")
_FragmentsReceived2XHorizontal_Type = Counter32
_FragmentsReceived2XHorizontal_Object = MibScalar
fragmentsReceived2XHorizontal = _FragmentsReceived2XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 110),
    _FragmentsReceived2XHorizontal_Type()
)
fragmentsReceived2XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived2XHorizontal.setStatus("current")
_FragmentsReceived3XHorizontal_Type = Counter32
_FragmentsReceived3XHorizontal_Object = MibScalar
fragmentsReceived3XHorizontal = _FragmentsReceived3XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 111),
    _FragmentsReceived3XHorizontal_Type()
)
fragmentsReceived3XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived3XHorizontal.setStatus("current")
_FragmentsReceived4XHorizontal_Type = Counter32
_FragmentsReceived4XHorizontal_Object = MibScalar
fragmentsReceived4XHorizontal = _FragmentsReceived4XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 112),
    _FragmentsReceived4XHorizontal_Type()
)
fragmentsReceived4XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentsReceived4XHorizontal.setStatus("current")
_LinkQualityData1XHorizontal_Type = DisplayString
_LinkQualityData1XHorizontal_Object = MibScalar
linkQualityData1XHorizontal = _LinkQualityData1XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 113),
    _LinkQualityData1XHorizontal_Type()
)
linkQualityData1XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData1XHorizontal.setStatus("current")
_LinkQualityData2XHorizontal_Type = DisplayString
_LinkQualityData2XHorizontal_Object = MibScalar
linkQualityData2XHorizontal = _LinkQualityData2XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 114),
    _LinkQualityData2XHorizontal_Type()
)
linkQualityData2XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData2XHorizontal.setStatus("current")
_LinkQualityData3XHorizontal_Type = DisplayString
_LinkQualityData3XHorizontal_Object = MibScalar
linkQualityData3XHorizontal = _LinkQualityData3XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 115),
    _LinkQualityData3XHorizontal_Type()
)
linkQualityData3XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData3XHorizontal.setStatus("current")
_LinkQualityData4XHorizontal_Type = DisplayString
_LinkQualityData4XHorizontal_Object = MibScalar
linkQualityData4XHorizontal = _LinkQualityData4XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 116),
    _LinkQualityData4XHorizontal_Type()
)
linkQualityData4XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityData4XHorizontal.setStatus("current")
_RadioDbmHorizontal_Type = DisplayString
_RadioDbmHorizontal_Object = MibScalar
radioDbmHorizontal = _RadioDbmHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 117),
    _RadioDbmHorizontal_Type()
)
radioDbmHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDbmHorizontal.setStatus("current")
_RadioDbmVertical_Type = DisplayString
_RadioDbmVertical_Object = MibScalar
radioDbmVertical = _RadioDbmVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 118),
    _RadioDbmVertical_Type()
)
radioDbmVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDbmVertical.setStatus("current")
_BridgecbDownlinkMaxBurstBitRate_Type = Unsigned32
_BridgecbDownlinkMaxBurstBitRate_Object = MibScalar
bridgecbDownlinkMaxBurstBitRate = _BridgecbDownlinkMaxBurstBitRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 119),
    _BridgecbDownlinkMaxBurstBitRate_Type()
)
bridgecbDownlinkMaxBurstBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgecbDownlinkMaxBurstBitRate.setStatus("current")
_BridgecbUplinkMaxBurstBitRate_Type = Unsigned32
_BridgecbUplinkMaxBurstBitRate_Object = MibScalar
bridgecbUplinkMaxBurstBitRate = _BridgecbUplinkMaxBurstBitRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 120),
    _BridgecbUplinkMaxBurstBitRate_Type()
)
bridgecbUplinkMaxBurstBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgecbUplinkMaxBurstBitRate.setStatus("current")


class _CurrentCyclicPrefix_Type(Integer32):
    """Custom type currentCyclicPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-eighth", 1),
          ("one-quarter", 0),
          ("one-sixteenth", 2))
    )


_CurrentCyclicPrefix_Type.__name__ = "Integer32"
_CurrentCyclicPrefix_Object = MibScalar
currentCyclicPrefix = _CurrentCyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 121),
    _CurrentCyclicPrefix_Type()
)
currentCyclicPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentCyclicPrefix.setStatus("current")


class _CurrentBandwidth_Type(Integer32):
    """Custom type currentBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth10mhz", 3),
          ("bandwidth20mhz", 5),
          ("bandwidth5mhz", 1))
    )


_CurrentBandwidth_Type.__name__ = "Integer32"
_CurrentBandwidth_Object = MibScalar
currentBandwidth = _CurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 122),
    _CurrentBandwidth_Type()
)
currentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentBandwidth.setStatus("current")
_BerPwrRxFPGAPathA_Type = Integer32
_BerPwrRxFPGAPathA_Object = MibScalar
berPwrRxFPGAPathA = _BerPwrRxFPGAPathA_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 123),
    _BerPwrRxFPGAPathA_Type()
)
berPwrRxFPGAPathA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berPwrRxFPGAPathA.setStatus("current")
_BerPwrRxFPGAPathB_Type = Integer32
_BerPwrRxFPGAPathB_Object = MibScalar
berPwrRxFPGAPathB = _BerPwrRxFPGAPathB_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 124),
    _BerPwrRxFPGAPathB_Type()
)
berPwrRxFPGAPathB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berPwrRxFPGAPathB.setStatus("current")
_RawBERPwrRxPathA_Type = Integer32
_RawBERPwrRxPathA_Object = MibScalar
rawBERPwrRxPathA = _RawBERPwrRxPathA_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 125),
    _RawBERPwrRxPathA_Type()
)
rawBERPwrRxPathA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawBERPwrRxPathA.setStatus("current")
_RawBERPwrRxPathB_Type = Integer32
_RawBERPwrRxPathB_Object = MibScalar
rawBERPwrRxPathB = _RawBERPwrRxPathB_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 126),
    _RawBERPwrRxPathB_Type()
)
rawBERPwrRxPathB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawBERPwrRxPathB.setStatus("current")


class _RadioModeStatus_Type(Integer32):
    """Custom type radioModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pmp430", 1),
          ("pmp450Interoperability", 2),
          ("undefined", 0))
    )


_RadioModeStatus_Type.__name__ = "Integer32"
_RadioModeStatus_Object = MibScalar
radioModeStatus = _RadioModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 127),
    _RadioModeStatus_Type()
)
radioModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioModeStatus.setStatus("current")


class _AdaptRateLowPri_Type(Integer32):
    """Custom type adaptRateLowPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noSession", 0),
          ("rate1X", 1),
          ("rate2X", 2),
          ("rate4X", 4),
          ("rate6X", 6),
          ("rate8X", 8),
          ("rete3X", 3))
    )


_AdaptRateLowPri_Type.__name__ = "Integer32"
_AdaptRateLowPri_Object = MibScalar
adaptRateLowPri = _AdaptRateLowPri_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 128),
    _AdaptRateLowPri_Type()
)
adaptRateLowPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptRateLowPri.setStatus("current")


class _AdaptRateHighPri_Type(Integer32):
    """Custom type adaptRateHighPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noHighPriorityChannel", -1),
          ("noSession", 0),
          ("rate1X", 1),
          ("rate2X", 2),
          ("rate4X", 4),
          ("rate6X", 6),
          ("rate8X", 8),
          ("rete3X", 3))
    )


_AdaptRateHighPri_Type.__name__ = "Integer32"
_AdaptRateHighPri_Object = MibScalar
adaptRateHighPri = _AdaptRateHighPri_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 129),
    _AdaptRateHighPri_Type()
)
adaptRateHighPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptRateHighPri.setStatus("current")
_BitErrorsQSPKpathA_Type = Counter64
_BitErrorsQSPKpathA_Object = MibScalar
bitErrorsQSPKpathA = _BitErrorsQSPKpathA_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 130),
    _BitErrorsQSPKpathA_Type()
)
bitErrorsQSPKpathA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsQSPKpathA.setStatus("current")
_BitErrorsQSPKpathB_Type = Counter64
_BitErrorsQSPKpathB_Object = MibScalar
bitErrorsQSPKpathB = _BitErrorsQSPKpathB_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 131),
    _BitErrorsQSPKpathB_Type()
)
bitErrorsQSPKpathB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsQSPKpathB.setStatus("current")
_BitErrors16QAMpathA_Type = Counter64
_BitErrors16QAMpathA_Object = MibScalar
bitErrors16QAMpathA = _BitErrors16QAMpathA_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 132),
    _BitErrors16QAMpathA_Type()
)
bitErrors16QAMpathA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrors16QAMpathA.setStatus("current")
_BitErrors16QAMpathB_Type = Counter64
_BitErrors16QAMpathB_Object = MibScalar
bitErrors16QAMpathB = _BitErrors16QAMpathB_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 133),
    _BitErrors16QAMpathB_Type()
)
bitErrors16QAMpathB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrors16QAMpathB.setStatus("current")
_BitErrors64QAMpathA_Type = Counter64
_BitErrors64QAMpathA_Object = MibScalar
bitErrors64QAMpathA = _BitErrors64QAMpathA_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 134),
    _BitErrors64QAMpathA_Type()
)
bitErrors64QAMpathA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrors64QAMpathA.setStatus("current")
_BitErrors64QAMpathB_Type = Counter64
_BitErrors64QAMpathB_Object = MibScalar
bitErrors64QAMpathB = _BitErrors64QAMpathB_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 135),
    _BitErrors64QAMpathB_Type()
)
bitErrors64QAMpathB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrors64QAMpathB.setStatus("current")
_BitErrors256QAMpathA_Type = Counter64
_BitErrors256QAMpathA_Object = MibScalar
bitErrors256QAMpathA = _BitErrors256QAMpathA_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 136),
    _BitErrors256QAMpathA_Type()
)
bitErrors256QAMpathA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrors256QAMpathA.setStatus("current")
_BitErrors256QAMpathB_Type = Counter64
_BitErrors256QAMpathB_Object = MibScalar
bitErrors256QAMpathB = _BitErrors256QAMpathB_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 137),
    _BitErrors256QAMpathB_Type()
)
bitErrors256QAMpathB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrors256QAMpathB.setStatus("current")
_BitsReceivedPerPathModulation_Type = Counter64
_BitsReceivedPerPathModulation_Object = MibScalar
bitsReceivedPerPathModulation = _BitsReceivedPerPathModulation_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 2, 138),
    _BitsReceivedPerPathModulation_Type()
)
bitsReceivedPerPathModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsReceivedPerPathModulation.setStatus("current")
_WhispSmGroups_ObjectIdentity = ObjectIdentity
whispSmGroups = _WhispSmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 3)
)
_WhispSmEvent_ObjectIdentity = ObjectIdentity
whispSmEvent = _WhispSmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4)
)
_WhispSmDfsEvent_ObjectIdentity = ObjectIdentity
whispSmDfsEvent = _WhispSmDfsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 1)
)
_WhispSmSpAnEvent_ObjectIdentity = ObjectIdentity
whispSmSpAnEvent = _WhispSmSpAnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 2)
)
_WhispSmDHCPClientEvent_ObjectIdentity = ObjectIdentity
whispSmDHCPClientEvent = _WhispSmDHCPClientEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 3)
)
_WhispMappingTable_Object = MibTable
whispMappingTable = _WhispMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 5)
)
if mibBuilder.loadTexts:
    whispMappingTable.setStatus("current")
_WhispMappingEntry_Object = MibTableRow
whispMappingEntry = _WhispMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 5, 1)
)
whispMappingEntry.setIndexNames(
    (0, "WHISP-SM-MIB", "tableIndex"),
)
if mibBuilder.loadTexts:
    whispMappingEntry.setStatus("current")


class _TableIndex_Type(Integer32):
    """Custom type tableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TableIndex_Type.__name__ = "Integer32"
_TableIndex_Object = MibTableColumn
tableIndex = _TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 5, 1, 1),
    _TableIndex_Type()
)
tableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tableIndex.setStatus("current")
_Protocol_Type = Integer32
_Protocol_Object = MibTableColumn
protocol = _Protocol_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 5, 1, 2),
    _Protocol_Type()
)
protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocol.setStatus("current")
_Port_Type = Integer32
_Port_Object = MibTableColumn
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 5, 1, 3),
    _Port_Type()
)
port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port.setStatus("current")
_LocalIp_Type = IpAddress
_LocalIp_Object = MibTableColumn
localIp = _LocalIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 5, 1, 4),
    _LocalIp_Type()
)
localIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIp.setStatus("current")
_WhispSmTranslationTable_Object = MibTable
whispSmTranslationTable = _WhispSmTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 6)
)
if mibBuilder.loadTexts:
    whispSmTranslationTable.setStatus("current")
_WhispSmTranslationTableEntry_Object = MibTableRow
whispSmTranslationTableEntry = _WhispSmTranslationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 6, 1)
)
whispSmTranslationTableEntry.setIndexNames(
    (0, "WHISP-SM-MIB", "whispTranslationTableIndex"),
)
if mibBuilder.loadTexts:
    whispSmTranslationTableEntry.setStatus("current")


class _WhispTranslationTableIndex_Type(Integer32):
    """Custom type whispTranslationTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WhispTranslationTableIndex_Type.__name__ = "Integer32"
_WhispTranslationTableIndex_Object = MibTableColumn
whispTranslationTableIndex = _WhispTranslationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 6, 1, 1),
    _WhispTranslationTableIndex_Type()
)
whispTranslationTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispTranslationTableIndex.setStatus("current")
_WhispTranslationTableMacAddr_Type = MacAddress
_WhispTranslationTableMacAddr_Object = MibTableColumn
whispTranslationTableMacAddr = _WhispTranslationTableMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 6, 1, 2),
    _WhispTranslationTableMacAddr_Type()
)
whispTranslationTableMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispTranslationTableMacAddr.setStatus("current")
_WhispTranslationTableIpAddr_Type = IpAddress
_WhispTranslationTableIpAddr_Object = MibTableColumn
whispTranslationTableIpAddr = _WhispTranslationTableIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 6, 1, 3),
    _WhispTranslationTableIpAddr_Type()
)
whispTranslationTableIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispTranslationTableIpAddr.setStatus("current")
_WhispTranslationTableAge_Type = Counter32
_WhispTranslationTableAge_Object = MibTableColumn
whispTranslationTableAge = _WhispTranslationTableAge_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 6, 1, 4),
    _WhispTranslationTableAge_Type()
)
whispTranslationTableAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispTranslationTableAge.setStatus("current")
_WhispSmSecurity_ObjectIdentity = ObjectIdentity
whispSmSecurity = _WhispSmSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7)
)
_CertTable_Object = MibTable
certTable = _CertTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    certTable.setStatus("current")
_CertEntry_Object = MibTableRow
certEntry = _CertEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 1, 1)
)
certEntry.setIndexNames(
    (0, "WHISP-SM-MIB", "certIndex"),
)
if mibBuilder.loadTexts:
    certEntry.setStatus("current")


class _CertIndex_Type(Integer32):
    """Custom type certIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CertIndex_Type.__name__ = "Integer32"
_CertIndex_Object = MibTableColumn
certIndex = _CertIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 1, 1, 1),
    _CertIndex_Type()
)
certIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIndex.setStatus("current")


class _Cert_Type(Integer32):
    """Custom type cert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cert_Type.__name__ = "Integer32"
_Cert_Object = MibTableColumn
cert = _Cert_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 1, 1, 2),
    _Cert_Type()
)
cert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cert.setStatus("current")


class _Action_Type(Integer32):
    """Custom type action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("noop", 0))
    )


_Action_Type.__name__ = "Integer32"
_Action_Object = MibTableColumn
action = _Action_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 1, 1, 3),
    _Action_Type()
)
action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    action.setStatus("current")
_CertificateDN_Type = DisplayString
_CertificateDN_Object = MibTableColumn
certificateDN = _CertificateDN_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 1, 1, 4),
    _CertificateDN_Type()
)
certificateDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateDN.setStatus("current")
_NumAuthCerts_Type = Integer32
_NumAuthCerts_Object = MibScalar
numAuthCerts = _NumAuthCerts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 2),
    _NumAuthCerts_Type()
)
numAuthCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numAuthCerts.setStatus("current")


class _AuthenticationEnforce_Type(Integer32):
    """Custom type authenticationEnforce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aaa", 1),
          ("disable", 0),
          ("presharedkey", 2))
    )


_AuthenticationEnforce_Type.__name__ = "Integer32"
_AuthenticationEnforce_Object = MibScalar
authenticationEnforce = _AuthenticationEnforce_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 3),
    _AuthenticationEnforce_Type()
)
authenticationEnforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationEnforce.setStatus("current")


class _Phase1_Type(Integer32):
    """Custom type phase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eapMSChapV2", 1),
          ("eapttls", 0))
    )


_Phase1_Type.__name__ = "Integer32"
_Phase1_Object = MibScalar
phase1 = _Phase1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 4),
    _Phase1_Type()
)
phase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phase1.setStatus("current")


class _Phase2_Type(Integer32):
    """Custom type phase2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("mschapv2", 2),
          ("pap", 0))
    )


_Phase2_Type.__name__ = "Integer32"
_Phase2_Object = MibScalar
phase2 = _Phase2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 5),
    _Phase2_Type()
)
phase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phase2.setStatus("current")


class _AuthOuterId_Type(OctetString):
    """Custom type authOuterId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_AuthOuterId_Type.__name__ = "OctetString"
_AuthOuterId_Object = MibScalar
authOuterId = _AuthOuterId_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 6),
    _AuthOuterId_Type()
)
authOuterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authOuterId.setStatus("current")
_AuthPassword_Type = DisplayString
_AuthPassword_Object = MibScalar
authPassword = _AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 7),
    _AuthPassword_Type()
)
authPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authPassword.setStatus("current")
_AuthUsername_Type = DisplayString
_AuthUsername_Object = MibScalar
authUsername = _AuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 8),
    _AuthUsername_Type()
)
authUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUsername.setStatus("current")


class _UseRealm_Type(Integer32):
    """Custom type useRealm based on Integer32"""
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


_UseRealm_Type.__name__ = "Integer32"
_UseRealm_Object = MibScalar
useRealm = _UseRealm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 9),
    _UseRealm_Type()
)
useRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useRealm.setStatus("current")
_Realm_Type = DisplayString
_Realm_Object = MibScalar
realm = _Realm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 7, 10),
    _Realm_Type()
)
realm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realm.setStatus("current")
_WhispSmControls_ObjectIdentity = ObjectIdentity
whispSmControls = _WhispSmControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 8)
)
_ClearLinkStats_Type = Integer32
_ClearLinkStats_Object = MibScalar
clearLinkStats = _ClearLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 8, 1),
    _ClearLinkStats_Type()
)
clearLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearLinkStats.setStatus("current")

# Managed Objects groups

whispSmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 3, 1)
)
whispSmConfigGroup.setObjects(
      *(("WHISP-SM-MIB", "rfScanList"),
        ("WHISP-SM-MIB", "rfScanListBandFilter"),
        ("WHISP-SM-MIB", "powerUpMode"),
        ("WHISP-SM-MIB", "lanIpSm"),
        ("WHISP-SM-MIB", "lanMaskSm"),
        ("WHISP-SM-MIB", "defaultGwSm"),
        ("WHISP-SM-MIB", "networkAccess"),
        ("WHISP-SM-MIB", "authKeySm"),
        ("WHISP-SM-MIB", "enable8023link"),
        ("WHISP-SM-MIB", "authKeyOption"),
        ("WHISP-SM-MIB", "timingPulseGated"),
        ("WHISP-SM-MIB", "naptPrivateIP"),
        ("WHISP-SM-MIB", "naptPrivateSubnetMask"),
        ("WHISP-SM-MIB", "naptPublicIP"),
        ("WHISP-SM-MIB", "naptPublicSubnetMask"),
        ("WHISP-SM-MIB", "naptPublicGatewayIP"),
        ("WHISP-SM-MIB", "naptRFPublicIP"),
        ("WHISP-SM-MIB", "naptRFPublicSubnetMask"),
        ("WHISP-SM-MIB", "naptRFPublicGateway"),
        ("WHISP-SM-MIB", "naptEnable"),
        ("WHISP-SM-MIB", "arpCacheTimeout"),
        ("WHISP-SM-MIB", "tcpGarbageCollectTmout"),
        ("WHISP-SM-MIB", "udpGarbageCollectTmout"),
        ("WHISP-SM-MIB", "dhcpClientEnable"),
        ("WHISP-SM-MIB", "dhcpServerEnable"),
        ("WHISP-SM-MIB", "dhcpServerLeaseTime"),
        ("WHISP-SM-MIB", "dhcpIPStart"),
        ("WHISP-SM-MIB", "dnsAutomatic"),
        ("WHISP-SM-MIB", "prefferedDNSIP"),
        ("WHISP-SM-MIB", "alternateDNSIP"),
        ("WHISP-SM-MIB", "natDNSProxyEnable"),
        ("WHISP-SM-MIB", "spectrumAnalysisDisplay"),
        ("WHISP-SM-MIB", "dmzIP"),
        ("WHISP-SM-MIB", "dmzEnable"),
        ("WHISP-SM-MIB", "dhcpNumIPsToLease"),
        ("WHISP-SM-MIB", "pppoeFilter"),
        ("WHISP-SM-MIB", "smbFilter"),
        ("WHISP-SM-MIB", "snmpFilter"),
        ("WHISP-SM-MIB", "userP1Filter"),
        ("WHISP-SM-MIB", "userP2Filter"),
        ("WHISP-SM-MIB", "userP3Filter"),
        ("WHISP-SM-MIB", "allOtherIpFilter"),
        ("WHISP-SM-MIB", "allIpv4Filter"),
        ("WHISP-SM-MIB", "upLinkBCastFilter"),
        ("WHISP-SM-MIB", "arpFilter"),
        ("WHISP-SM-MIB", "allOthersFilter"),
        ("WHISP-SM-MIB", "userDefinedPort1"),
        ("WHISP-SM-MIB", "port1TCPFilter"),
        ("WHISP-SM-MIB", "port1UDPFilter"),
        ("WHISP-SM-MIB", "userDefinedPort2"),
        ("WHISP-SM-MIB", "port2TCPFilter"),
        ("WHISP-SM-MIB", "port2UDPFilter"),
        ("WHISP-SM-MIB", "userDefinedPort3"),
        ("WHISP-SM-MIB", "port3TCPFilter"),
        ("WHISP-SM-MIB", "port3UDPFilter"),
        ("WHISP-SM-MIB", "bootpcFilter"),
        ("WHISP-SM-MIB", "bootpsFilter"),
        ("WHISP-SM-MIB", "ip4MultFilter"),
        ("WHISP-SM-MIB", "ingressVID"),
        ("WHISP-SM-MIB", "lowPriorityUplinkCIR"),
        ("WHISP-SM-MIB", "lowPriorityDownlinkCIR"),
        ("WHISP-SM-MIB", "hiPriorityChannel"),
        ("WHISP-SM-MIB", "hiPriorityUplinkCIR"),
        ("WHISP-SM-MIB", "hiPriorityDownlinkCIR"),
        ("WHISP-SM-MIB", "smRateAdapt"),
        ("WHISP-SM-MIB", "upLnkMaxBurstDataRate"),
        ("WHISP-SM-MIB", "upLnkDataRate"),
        ("WHISP-SM-MIB", "upLnkLimit"),
        ("WHISP-SM-MIB", "dwnLnkMaxBurstDataRate"),
        ("WHISP-SM-MIB", "cyclicPrefixScan"),
        ("WHISP-SM-MIB", "bandwidthScan"),
        ("WHISP-SM-MIB", "apSelection"),
        ("WHISP-SM-MIB", "radioBandscanConfig"),
        ("WHISP-SM-MIB", "forcepoweradjust"),
        ("WHISP-SM-MIB", "clearBerrResults"),
        ("WHISP-SM-MIB", "berrautoupdateflag"),
        ("WHISP-SM-MIB", "testSMBER"),
        ("WHISP-SM-MIB", "dwnLnkDataRate"),
        ("WHISP-SM-MIB", "dwnLnkLimit"),
        ("WHISP-SM-MIB", "dfsConfig"),
        ("WHISP-SM-MIB", "ethAccessFilterEnable"),
        ("WHISP-SM-MIB", "ipAccessFilterEnable"),
        ("WHISP-SM-MIB", "allowedIPAccess1"),
        ("WHISP-SM-MIB", "allowedIPAccess2"),
        ("WHISP-SM-MIB", "allowedIPAccess3"),
        ("WHISP-SM-MIB", "allowedIPAccessNMLength1"),
        ("WHISP-SM-MIB", "allowedIPAccessNMLength2"),
        ("WHISP-SM-MIB", "allowedIPAccessNMLength3"),
        ("WHISP-SM-MIB", "rfDhcpState"),
        ("WHISP-SM-MIB", "bCastMIR"),
        ("WHISP-SM-MIB", "bhsReReg"),
        ("WHISP-SM-MIB", "smLEDModeFlag"),
        ("WHISP-SM-MIB", "ethAccessEnable"),
        ("WHISP-SM-MIB", "pppoeEnable"),
        ("WHISP-SM-MIB", "pppoeAuthenticationType"),
        ("WHISP-SM-MIB", "pppoeAccessConcentrator"),
        ("WHISP-SM-MIB", "pppoeServiceName"),
        ("WHISP-SM-MIB", "pppoeUserName"),
        ("WHISP-SM-MIB", "pppoePassword"),
        ("WHISP-SM-MIB", "pppoeTCPMSSClampEnable"),
        ("WHISP-SM-MIB", "pppoeMTUOverrideEnable"),
        ("WHISP-SM-MIB", "pppoeMTUOverrideValue"),
        ("WHISP-SM-MIB", "pppoeTimerType"),
        ("WHISP-SM-MIB", "pppoeTimeoutPeriod"),
        ("WHISP-SM-MIB", "timedSpectrumAnalysisDuration"),
        ("WHISP-SM-MIB", "spectrumAnalysisScanBandwidth"),
        ("WHISP-SM-MIB", "spectrumAnalysisOnBoot"),
        ("WHISP-SM-MIB", "spectrumAnalysisAction"),
        ("WHISP-SM-MIB", "pppoeConnectOD"),
        ("WHISP-SM-MIB", "pppoeDisconnectOD"),
        ("WHISP-SM-MIB", "smAntennaType"),
        ("WHISP-SM-MIB", "natConnectionType"),
        ("WHISP-SM-MIB", "wanPingReplyEnable"),
        ("WHISP-SM-MIB", "packetFilterDirection"),
        ("WHISP-SM-MIB", "colorCode2"),
        ("WHISP-SM-MIB", "colorCodepriority2"),
        ("WHISP-SM-MIB", "colorCode3"),
        ("WHISP-SM-MIB", "colorCodepriority3"),
        ("WHISP-SM-MIB", "colorCode4"),
        ("WHISP-SM-MIB", "colorCodepriority4"),
        ("WHISP-SM-MIB", "colorCode5"),
        ("WHISP-SM-MIB", "colorCodepriority5"),
        ("WHISP-SM-MIB", "colorCode6"),
        ("WHISP-SM-MIB", "colorCodepriority6"),
        ("WHISP-SM-MIB", "colorCode7"),
        ("WHISP-SM-MIB", "colorCodepriority7"),
        ("WHISP-SM-MIB", "colorCode8"),
        ("WHISP-SM-MIB", "colorCodepriority8"),
        ("WHISP-SM-MIB", "colorCode9"),
        ("WHISP-SM-MIB", "colorCodepriority9"),
        ("WHISP-SM-MIB", "colorCode10"),
        ("WHISP-SM-MIB", "colorCodepriority10"),
        ("WHISP-SM-MIB", "berDeModSelect"),
        ("WHISP-SM-MIB", "multicastVCRcvRate"),
        ("WHISP-SM-MIB", "syslogServerApPreferred"),
        ("WHISP-SM-MIB", "syslogMinLevelApPreferred"),
        ("WHISP-SM-MIB", "syslogSMXmitSetting"),
        ("WHISP-SM-MIB", "syslogSMXmitControl"),
        ("WHISP-SM-MIB", "naptRemoteManage"),
        ("WHISP-SM-MIB", "eapPeerAAAServerCommonName"),
        ("WHISP-SM-MIB", "pmp430ApRegistrationOptions"),
        ("WHISP-SM-MIB", "switchRadioModeAndReboot"))
)
if mibBuilder.loadTexts:
    whispSmConfigGroup.setStatus("current")

whispSmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 3, 2)
)
whispSmStatusGroup.setObjects(
      *(("WHISP-SM-MIB", "sessionStatus"),
        ("WHISP-SM-MIB", "rssi"),
        ("WHISP-SM-MIB", "jitter"),
        ("WHISP-SM-MIB", "airDelay"),
        ("WHISP-SM-MIB", "radioSlicingSm"),
        ("WHISP-SM-MIB", "radioTxGainSm"),
        ("WHISP-SM-MIB", "calibrationStatus"),
        ("WHISP-SM-MIB", "radioDbm"),
        ("WHISP-SM-MIB", "registeredToAp"),
        ("WHISP-SM-MIB", "dhcpCip"),
        ("WHISP-SM-MIB", "dhcpSip"),
        ("WHISP-SM-MIB", "dhcpClientLease"),
        ("WHISP-SM-MIB", "dhcpCSMask"),
        ("WHISP-SM-MIB", "dhcpDfltRterIP"),
        ("WHISP-SM-MIB", "dhcpcdns1"),
        ("WHISP-SM-MIB", "dhcpcdns2"),
        ("WHISP-SM-MIB", "dhcpcdns3"),
        ("WHISP-SM-MIB", "dhcpDomName"),
        ("WHISP-SM-MIB", "adaptRate"),
        ("WHISP-SM-MIB", "adaptRateLowPri"),
        ("WHISP-SM-MIB", "adaptRateHighPri"),
        ("WHISP-SM-MIB", "bitErrorsQSPKpathA"),
        ("WHISP-SM-MIB", "bitErrorsQSPKpathB"),
        ("WHISP-SM-MIB", "bitErrors16QAMpathA"),
        ("WHISP-SM-MIB", "bitErrors16QAMpathB"),
        ("WHISP-SM-MIB", "bitErrors64QAMpathA"),
        ("WHISP-SM-MIB", "bitErrors64QAMpathB"),
        ("WHISP-SM-MIB", "bitErrors256QAMpathA"),
        ("WHISP-SM-MIB", "bitErrors256QAMpathB"),
        ("WHISP-SM-MIB", "bitsReceivedPerPathModulation"),
        ("WHISP-SM-MIB", "radioDbmInt"),
        ("WHISP-SM-MIB", "dfsStatus"),
        ("WHISP-SM-MIB", "radioTxPwr"),
        ("WHISP-SM-MIB", "activeRegion"),
        ("WHISP-SM-MIB", "snmpBerLevel"),
        ("WHISP-SM-MIB", "nbBitsRcvd"),
        ("WHISP-SM-MIB", "nbPriBitsErr"),
        ("WHISP-SM-MIB", "nbSndBitsErr"),
        ("WHISP-SM-MIB", "primaryBER"),
        ("WHISP-SM-MIB", "secondaryBER"),
        ("WHISP-SM-MIB", "totalBER"),
        ("WHISP-SM-MIB", "minRSSI"),
        ("WHISP-SM-MIB", "maxRSSI"),
        ("WHISP-SM-MIB", "minJitter"),
        ("WHISP-SM-MIB", "maxJitter"),
        ("WHISP-SM-MIB", "smSessionTimer"),
        ("WHISP-SM-MIB", "pppoeSessionStatus"),
        ("WHISP-SM-MIB", "pppoeSessionID"),
        ("WHISP-SM-MIB", "pppoeIPCPAddress"),
        ("WHISP-SM-MIB", "pppoeMTUOverrideEn"),
        ("WHISP-SM-MIB", "pppoeMTUValue"),
        ("WHISP-SM-MIB", "pppoeTimerTypeValue"),
        ("WHISP-SM-MIB", "pppoeTimeoutValue"),
        ("WHISP-SM-MIB", "pppoeDNSServer1"),
        ("WHISP-SM-MIB", "pppoeDNSServer2"),
        ("WHISP-SM-MIB", "pppoeControlBytesSent"),
        ("WHISP-SM-MIB", "pppoeControlBytesReceived"),
        ("WHISP-SM-MIB", "pppoeDataBytesSent"),
        ("WHISP-SM-MIB", "pppoeDataBytesReceived"),
        ("WHISP-SM-MIB", "pppoeEnabledStatus"),
        ("WHISP-SM-MIB", "pppoeTCPMSSClampEnableStatus"),
        ("WHISP-SM-MIB", "pppoeACNameStatus"),
        ("WHISP-SM-MIB", "pppoeSvcNameStatus"),
        ("WHISP-SM-MIB", "pppoeSessUptime"),
        ("WHISP-SM-MIB", "primaryBERDisplay"),
        ("WHISP-SM-MIB", "secondaryBERDisplay"),
        ("WHISP-SM-MIB", "totalBERDisplay"),
        ("WHISP-SM-MIB", "mimoQpskBerDisplay"),
        ("WHISP-SM-MIB", "mimo16QamBerDisplay"),
        ("WHISP-SM-MIB", "mimo64QamBerDisplay"),
        ("WHISP-SM-MIB", "mimo256QamBerDisplay"),
        ("WHISP-SM-MIB", "mimoBerRcvModulationType"),
        ("WHISP-SM-MIB", "minRadioDbm"),
        ("WHISP-SM-MIB", "maxRadioDbm"),
        ("WHISP-SM-MIB", "maxRadioDbmDeprecated"),
        ("WHISP-SM-MIB", "pppoeSessIdleTime"),
        ("WHISP-SM-MIB", "radioDbmAvg"),
        ("WHISP-SM-MIB", "zoltarFPGAFreqOffset"),
        ("WHISP-SM-MIB", "zoltarSWFreqOffset"),
        ("WHISP-SM-MIB", "airDelayns"),
        ("WHISP-SM-MIB", "currentColorCode"),
        ("WHISP-SM-MIB", "currentColorCodePri"),
        ("WHISP-SM-MIB", "currentChanFreq"),
        ("WHISP-SM-MIB", "linkQualityBeacon"),
        ("WHISP-SM-MIB", "currentCyclicPrefix"),
        ("WHISP-SM-MIB", "currentBandwidth"),
        ("WHISP-SM-MIB", "berPwrRxFPGAPathA"),
        ("WHISP-SM-MIB", "berPwrRxFPGAPathB"),
        ("WHISP-SM-MIB", "rawBERPwrRxPathA"),
        ("WHISP-SM-MIB", "rawBERPwrRxPathB"),
        ("WHISP-SM-MIB", "linkQualityData1XVertical"),
        ("WHISP-SM-MIB", "linkQualityData2XVertical"),
        ("WHISP-SM-MIB", "linkQualityData3XVertical"),
        ("WHISP-SM-MIB", "linkQualityData4XVertical"),
        ("WHISP-SM-MIB", "linkQualityData1XHorizontal"),
        ("WHISP-SM-MIB", "linkQualityData2XHorizontal"),
        ("WHISP-SM-MIB", "linkQualityData3XHorizontal"),
        ("WHISP-SM-MIB", "linkQualityData4XHorizontal"),
        ("WHISP-SM-MIB", "signalToNoiseRatioSMVertical"),
        ("WHISP-SM-MIB", "signalToNoiseRatioSMHorizontal"),
        ("WHISP-SM-MIB", "signalStrengthRatio"),
        ("WHISP-SM-MIB", "radioDbmHorizontal"),
        ("WHISP-SM-MIB", "radioDbmVertical"),
        ("WHISP-SM-MIB", "rfStatTxSuppressionCount"),
        ("WHISP-SM-MIB", "receiveFragmentsModulationPercentage"),
        ("WHISP-SM-MIB", "fragmentsReceived1XVertical"),
        ("WHISP-SM-MIB", "fragmentsReceived2XVertical"),
        ("WHISP-SM-MIB", "fragmentsReceived3XVertical"),
        ("WHISP-SM-MIB", "fragmentsReceived4XVertical"),
        ("WHISP-SM-MIB", "fragmentsReceived1XHorizontal"),
        ("WHISP-SM-MIB", "fragmentsReceived2XHorizontal"),
        ("WHISP-SM-MIB", "fragmentsReceived3XHorizontal"),
        ("WHISP-SM-MIB", "fragmentsReceived4XHorizontal"),
        ("WHISP-SM-MIB", "bridgecbUplinkCreditRate"),
        ("WHISP-SM-MIB", "bridgecbUplinkCreditLimit"),
        ("WHISP-SM-MIB", "bridgecbDownlinkCreditRate"),
        ("WHISP-SM-MIB", "bridgecbDownlinkCreditLimit"),
        ("WHISP-SM-MIB", "bridgecbDownlinkMaxBurstBitRate"),
        ("WHISP-SM-MIB", "bridgecbUplinkMaxBurstBitRate"),
        ("WHISP-SM-MIB", "radioModeStatus"))
)
if mibBuilder.loadTexts:
    whispSmStatusGroup.setStatus("current")

whispMappingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 3, 4)
)
whispMappingTableGroup.setObjects(
      *(("WHISP-SM-MIB", "tableIndex"),
        ("WHISP-SM-MIB", "protocol"),
        ("WHISP-SM-MIB", "port"),
        ("WHISP-SM-MIB", "localIp"))
)
if mibBuilder.loadTexts:
    whispMappingTableGroup.setStatus("current")


# Notification objects

whispRadarDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 1, 1)
)
whispRadarDetected.setObjects(
      *(("WHISP-SM-MIB", "dfsStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    whispRadarDetected.setStatus(
        "current"
    )

whispRadarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 1, 2)
)
whispRadarEnd.setObjects(
      *(("WHISP-SM-MIB", "dfsStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    whispRadarEnd.setStatus(
        "current"
    )

enterSpectrumAnalysis = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 2, 1)
)
enterSpectrumAnalysis.setObjects(
    ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn")
)
if mibBuilder.loadTexts:
    enterSpectrumAnalysis.setStatus(
        "current"
    )

availableSpectrumAnalysis = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 2, 2)
)
availableSpectrumAnalysis.setObjects(
    ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn")
)
if mibBuilder.loadTexts:
    availableSpectrumAnalysis.setStatus(
        "current"
    )

smNatWanDHCPClientEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 3, 1)
)
smNatWanDHCPClientEvent.setObjects(
      *(("WHISP-SM-MIB", "dhcpCip"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    smNatWanDHCPClientEvent.setStatus(
        "current"
    )

smNatRFPubDHCPClientEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 4, 3, 2)
)
smNatRFPubDHCPClientEvent.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "dhcpRfPublicIp"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    smNatRFPubDHCPClientEvent.setStatus(
        "current"
    )


# Notifications groups

whispSmNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 2, 3, 3)
)
whispSmNotifGroup.setObjects(
      *(("WHISP-SM-MIB", "enterSpectrumAnalysis"),
        ("WHISP-SM-MIB", "availableSpectrumAnalysis"),
        ("WHISP-SM-MIB", "whispRadarDetected"),
        ("WHISP-SM-MIB", "whispRadarEnd"),
        ("WHISP-SM-MIB", "smNatWanDHCPClientEvent"),
        ("WHISP-SM-MIB", "smNatRFPubDHCPClientEvent"))
)
if mibBuilder.loadTexts:
    whispSmNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-SM-MIB",
    **{"whispSmMibModule": whispSmMibModule,
       "whispSmConfig": whispSmConfig,
       "rfScanList": rfScanList,
       "powerUpMode": powerUpMode,
       "lanIpSm": lanIpSm,
       "lanMaskSm": lanMaskSm,
       "defaultGwSm": defaultGwSm,
       "networkAccess": networkAccess,
       "authKeySm": authKeySm,
       "enable8023link": enable8023link,
       "authKeyOption": authKeyOption,
       "timingPulseGated": timingPulseGated,
       "naptPrivateIP": naptPrivateIP,
       "naptPrivateSubnetMask": naptPrivateSubnetMask,
       "naptPublicIP": naptPublicIP,
       "naptPublicSubnetMask": naptPublicSubnetMask,
       "naptPublicGatewayIP": naptPublicGatewayIP,
       "naptRFPublicIP": naptRFPublicIP,
       "naptRFPublicSubnetMask": naptRFPublicSubnetMask,
       "naptRFPublicGateway": naptRFPublicGateway,
       "naptEnable": naptEnable,
       "arpCacheTimeout": arpCacheTimeout,
       "tcpGarbageCollectTmout": tcpGarbageCollectTmout,
       "udpGarbageCollectTmout": udpGarbageCollectTmout,
       "dhcpClientEnable": dhcpClientEnable,
       "dhcpServerEnable": dhcpServerEnable,
       "dhcpServerLeaseTime": dhcpServerLeaseTime,
       "dhcpIPStart": dhcpIPStart,
       "dnsAutomatic": dnsAutomatic,
       "prefferedDNSIP": prefferedDNSIP,
       "alternateDNSIP": alternateDNSIP,
       "dmzIP": dmzIP,
       "dmzEnable": dmzEnable,
       "dhcpNumIPsToLease": dhcpNumIPsToLease,
       "pppoeFilter": pppoeFilter,
       "smbFilter": smbFilter,
       "snmpFilter": snmpFilter,
       "userP1Filter": userP1Filter,
       "userP2Filter": userP2Filter,
       "userP3Filter": userP3Filter,
       "allOtherIpFilter": allOtherIpFilter,
       "upLinkBCastFilter": upLinkBCastFilter,
       "arpFilter": arpFilter,
       "allOthersFilter": allOthersFilter,
       "userDefinedPort1": userDefinedPort1,
       "port1TCPFilter": port1TCPFilter,
       "port1UDPFilter": port1UDPFilter,
       "userDefinedPort2": userDefinedPort2,
       "port2TCPFilter": port2TCPFilter,
       "port2UDPFilter": port2UDPFilter,
       "userDefinedPort3": userDefinedPort3,
       "port3TCPFilter": port3TCPFilter,
       "port3UDPFilter": port3UDPFilter,
       "bootpcFilter": bootpcFilter,
       "bootpsFilter": bootpsFilter,
       "ip4MultFilter": ip4MultFilter,
       "ingressVID": ingressVID,
       "lowPriorityUplinkCIR": lowPriorityUplinkCIR,
       "lowPriorityDownlinkCIR": lowPriorityDownlinkCIR,
       "hiPriorityChannel": hiPriorityChannel,
       "hiPriorityUplinkCIR": hiPriorityUplinkCIR,
       "hiPriorityDownlinkCIR": hiPriorityDownlinkCIR,
       "smRateAdapt": smRateAdapt,
       "upLnkDataRate": upLnkDataRate,
       "upLnkLimit": upLnkLimit,
       "dwnLnkDataRate": dwnLnkDataRate,
       "dwnLnkLimit": dwnLnkLimit,
       "dfsConfig": dfsConfig,
       "ethAccessFilterEnable": ethAccessFilterEnable,
       "ipAccessFilterEnable": ipAccessFilterEnable,
       "allowedIPAccess1": allowedIPAccess1,
       "allowedIPAccess2": allowedIPAccess2,
       "allowedIPAccess3": allowedIPAccess3,
       "rfDhcpState": rfDhcpState,
       "bCastMIR": bCastMIR,
       "bhsReReg": bhsReReg,
       "smLEDModeFlag": smLEDModeFlag,
       "ethAccessEnable": ethAccessEnable,
       "pppoeEnable": pppoeEnable,
       "pppoeAuthenticationType": pppoeAuthenticationType,
       "pppoeAccessConcentrator": pppoeAccessConcentrator,
       "pppoeServiceName": pppoeServiceName,
       "pppoeUserName": pppoeUserName,
       "pppoePassword": pppoePassword,
       "pppoeTCPMSSClampEnable": pppoeTCPMSSClampEnable,
       "pppoeMTUOverrideEnable": pppoeMTUOverrideEnable,
       "pppoeMTUOverrideValue": pppoeMTUOverrideValue,
       "pppoeTimerType": pppoeTimerType,
       "pppoeTimeoutPeriod": pppoeTimeoutPeriod,
       "timedSpectrumAnalysisDuration": timedSpectrumAnalysisDuration,
       "spectrumAnalysisOnBoot": spectrumAnalysisOnBoot,
       "spectrumAnalysisAction": spectrumAnalysisAction,
       "pppoeConnectOD": pppoeConnectOD,
       "pppoeDisconnectOD": pppoeDisconnectOD,
       "smAntennaType": smAntennaType,
       "natConnectionType": natConnectionType,
       "wanPingReplyEnable": wanPingReplyEnable,
       "packetFilterDirection": packetFilterDirection,
       "colorCode2": colorCode2,
       "colorCodepriority2": colorCodepriority2,
       "colorCode3": colorCode3,
       "colorCodepriority3": colorCodepriority3,
       "colorCode4": colorCode4,
       "colorCodepriority4": colorCodepriority4,
       "colorCode5": colorCode5,
       "colorCodepriority5": colorCodepriority5,
       "colorCode6": colorCode6,
       "colorCodepriority6": colorCodepriority6,
       "colorCode7": colorCode7,
       "colorCodepriority7": colorCodepriority7,
       "colorCode8": colorCode8,
       "colorCodepriority8": colorCodepriority8,
       "colorCode9": colorCode9,
       "colorCodepriority9": colorCodepriority9,
       "colorCode10": colorCode10,
       "colorCodepriority10": colorCodepriority10,
       "natDNSProxyEnable": natDNSProxyEnable,
       "allIpv4Filter": allIpv4Filter,
       "spectrumAnalysisDisplay": spectrumAnalysisDisplay,
       "syslogSMXmitSetting": syslogSMXmitSetting,
       "syslogServerApPreferred": syslogServerApPreferred,
       "syslogMinLevelApPreferred": syslogMinLevelApPreferred,
       "syslogSMXmitControl": syslogSMXmitControl,
       "eapPeerAAAServerCommonName": eapPeerAAAServerCommonName,
       "rfScanListBandFilter": rfScanListBandFilter,
       "upLnkMaxBurstDataRate": upLnkMaxBurstDataRate,
       "dwnLnkMaxBurstDataRate": dwnLnkMaxBurstDataRate,
       "cyclicPrefixScan": cyclicPrefixScan,
       "bandwidthScan": bandwidthScan,
       "apSelection": apSelection,
       "radioBandscanConfig": radioBandscanConfig,
       "forcepoweradjust": forcepoweradjust,
       "clearBerrResults": clearBerrResults,
       "berrautoupdateflag": berrautoupdateflag,
       "testSMBER": testSMBER,
       "allowedIPAccessNMLength1": allowedIPAccessNMLength1,
       "allowedIPAccessNMLength2": allowedIPAccessNMLength2,
       "allowedIPAccessNMLength3": allowedIPAccessNMLength3,
       "naptRemoteManage": naptRemoteManage,
       "spectrumAnalysisScanBandwidth": spectrumAnalysisScanBandwidth,
       "berDeModSelect": berDeModSelect,
       "multicastVCRcvRate": multicastVCRcvRate,
       "pmp430ApRegistrationOptions": pmp430ApRegistrationOptions,
       "switchRadioModeAndReboot": switchRadioModeAndReboot,
       "whispSmStatus": whispSmStatus,
       "sessionStatus": sessionStatus,
       "rssi": rssi,
       "jitter": jitter,
       "airDelay": airDelay,
       "radioSlicingSm": radioSlicingSm,
       "radioTxGainSm": radioTxGainSm,
       "calibrationStatus": calibrationStatus,
       "radioDbm": radioDbm,
       "registeredToAp": registeredToAp,
       "dhcpCip": dhcpCip,
       "dhcpSip": dhcpSip,
       "dhcpClientLease": dhcpClientLease,
       "dhcpCSMask": dhcpCSMask,
       "dhcpDfltRterIP": dhcpDfltRterIP,
       "dhcpcdns1": dhcpcdns1,
       "dhcpcdns2": dhcpcdns2,
       "dhcpcdns3": dhcpcdns3,
       "dhcpDomName": dhcpDomName,
       "dhcpServerTable": dhcpServerTable,
       "dhcpServerEntry": dhcpServerEntry,
       "hostIp": hostIp,
       "hostMacAddress": hostMacAddress,
       "hostLease": hostLease,
       "adaptRate": adaptRate,
       "radioDbmInt": radioDbmInt,
       "dfsStatus": dfsStatus,
       "radioTxPwr": radioTxPwr,
       "activeRegion": activeRegion,
       "snmpBerLevel": snmpBerLevel,
       "nbBitsRcvd": nbBitsRcvd,
       "nbPriBitsErr": nbPriBitsErr,
       "nbSndBitsErr": nbSndBitsErr,
       "primaryBER": primaryBER,
       "secondaryBER": secondaryBER,
       "totalBER": totalBER,
       "minRSSI": minRSSI,
       "maxRSSI": maxRSSI,
       "minJitter": minJitter,
       "maxJitter": maxJitter,
       "smSessionTimer": smSessionTimer,
       "pppoeSessionStatus": pppoeSessionStatus,
       "pppoeSessionID": pppoeSessionID,
       "pppoeIPCPAddress": pppoeIPCPAddress,
       "pppoeMTUOverrideEn": pppoeMTUOverrideEn,
       "pppoeMTUValue": pppoeMTUValue,
       "pppoeTimerTypeValue": pppoeTimerTypeValue,
       "pppoeTimeoutValue": pppoeTimeoutValue,
       "pppoeDNSServer1": pppoeDNSServer1,
       "pppoeDNSServer2": pppoeDNSServer2,
       "pppoeControlBytesSent": pppoeControlBytesSent,
       "pppoeControlBytesReceived": pppoeControlBytesReceived,
       "pppoeDataBytesSent": pppoeDataBytesSent,
       "pppoeDataBytesReceived": pppoeDataBytesReceived,
       "pppoeEnabledStatus": pppoeEnabledStatus,
       "pppoeTCPMSSClampEnableStatus": pppoeTCPMSSClampEnableStatus,
       "pppoeACNameStatus": pppoeACNameStatus,
       "pppoeSvcNameStatus": pppoeSvcNameStatus,
       "pppoeSessUptime": pppoeSessUptime,
       "primaryBERDisplay": primaryBERDisplay,
       "secondaryBERDisplay": secondaryBERDisplay,
       "totalBERDisplay": totalBERDisplay,
       "minRadioDbm": minRadioDbm,
       "maxRadioDbm": maxRadioDbm,
       "pppoeSessIdleTime": pppoeSessIdleTime,
       "radioDbmAvg": radioDbmAvg,
       "zoltarFPGAFreqOffset": zoltarFPGAFreqOffset,
       "zoltarSWFreqOffset": zoltarSWFreqOffset,
       "airDelayns": airDelayns,
       "currentColorCode": currentColorCode,
       "currentColorCodePri": currentColorCodePri,
       "currentChanFreq": currentChanFreq,
       "linkQualityBeacon": linkQualityBeacon,
       "dhcpServerPktXmt": dhcpServerPktXmt,
       "dhcpServerPktRcv": dhcpServerPktRcv,
       "dhcpServerPktToss": dhcpServerPktToss,
       "receiveFragmentsModulationPercentage": receiveFragmentsModulationPercentage,
       "fragmentsReceived1XVertical": fragmentsReceived1XVertical,
       "fragmentsReceived2XVertical": fragmentsReceived2XVertical,
       "fragmentsReceived3XVertical": fragmentsReceived3XVertical,
       "fragmentsReceived4XVertical": fragmentsReceived4XVertical,
       "linkQualityData1XVertical": linkQualityData1XVertical,
       "linkQualityData2XVertical": linkQualityData2XVertical,
       "linkQualityData3XVertical": linkQualityData3XVertical,
       "linkQualityData4XVertical": linkQualityData4XVertical,
       "signalToNoiseRatioSMVertical": signalToNoiseRatioSMVertical,
       "rfStatTxSuppressionCount": rfStatTxSuppressionCount,
       "bridgecbUplinkCreditRate": bridgecbUplinkCreditRate,
       "bridgecbUplinkCreditLimit": bridgecbUplinkCreditLimit,
       "bridgecbDownlinkCreditRate": bridgecbDownlinkCreditRate,
       "bridgecbDownlinkCreditLimit": bridgecbDownlinkCreditLimit,
       "mimoQpskBerDisplay": mimoQpskBerDisplay,
       "mimo16QamBerDisplay": mimo16QamBerDisplay,
       "mimo64QamBerDisplay": mimo64QamBerDisplay,
       "mimo256QamBerDisplay": mimo256QamBerDisplay,
       "mimoBerRcvModulationType": mimoBerRcvModulationType,
       "signalToNoiseRatioSMHorizontal": signalToNoiseRatioSMHorizontal,
       "maxRadioDbmDeprecated": maxRadioDbmDeprecated,
       "signalStrengthRatio": signalStrengthRatio,
       "fragmentsReceived1XHorizontal": fragmentsReceived1XHorizontal,
       "fragmentsReceived2XHorizontal": fragmentsReceived2XHorizontal,
       "fragmentsReceived3XHorizontal": fragmentsReceived3XHorizontal,
       "fragmentsReceived4XHorizontal": fragmentsReceived4XHorizontal,
       "linkQualityData1XHorizontal": linkQualityData1XHorizontal,
       "linkQualityData2XHorizontal": linkQualityData2XHorizontal,
       "linkQualityData3XHorizontal": linkQualityData3XHorizontal,
       "linkQualityData4XHorizontal": linkQualityData4XHorizontal,
       "radioDbmHorizontal": radioDbmHorizontal,
       "radioDbmVertical": radioDbmVertical,
       "bridgecbDownlinkMaxBurstBitRate": bridgecbDownlinkMaxBurstBitRate,
       "bridgecbUplinkMaxBurstBitRate": bridgecbUplinkMaxBurstBitRate,
       "currentCyclicPrefix": currentCyclicPrefix,
       "currentBandwidth": currentBandwidth,
       "berPwrRxFPGAPathA": berPwrRxFPGAPathA,
       "berPwrRxFPGAPathB": berPwrRxFPGAPathB,
       "rawBERPwrRxPathA": rawBERPwrRxPathA,
       "rawBERPwrRxPathB": rawBERPwrRxPathB,
       "radioModeStatus": radioModeStatus,
       "adaptRateLowPri": adaptRateLowPri,
       "adaptRateHighPri": adaptRateHighPri,
       "bitErrorsQSPKpathA": bitErrorsQSPKpathA,
       "bitErrorsQSPKpathB": bitErrorsQSPKpathB,
       "bitErrors16QAMpathA": bitErrors16QAMpathA,
       "bitErrors16QAMpathB": bitErrors16QAMpathB,
       "bitErrors64QAMpathA": bitErrors64QAMpathA,
       "bitErrors64QAMpathB": bitErrors64QAMpathB,
       "bitErrors256QAMpathA": bitErrors256QAMpathA,
       "bitErrors256QAMpathB": bitErrors256QAMpathB,
       "bitsReceivedPerPathModulation": bitsReceivedPerPathModulation,
       "whispSmGroups": whispSmGroups,
       "whispSmConfigGroup": whispSmConfigGroup,
       "whispSmStatusGroup": whispSmStatusGroup,
       "whispSmNotifGroup": whispSmNotifGroup,
       "whispMappingTableGroup": whispMappingTableGroup,
       "whispSmEvent": whispSmEvent,
       "whispSmDfsEvent": whispSmDfsEvent,
       "whispRadarDetected": whispRadarDetected,
       "whispRadarEnd": whispRadarEnd,
       "whispSmSpAnEvent": whispSmSpAnEvent,
       "enterSpectrumAnalysis": enterSpectrumAnalysis,
       "availableSpectrumAnalysis": availableSpectrumAnalysis,
       "whispSmDHCPClientEvent": whispSmDHCPClientEvent,
       "smNatWanDHCPClientEvent": smNatWanDHCPClientEvent,
       "smNatRFPubDHCPClientEvent": smNatRFPubDHCPClientEvent,
       "whispMappingTable": whispMappingTable,
       "whispMappingEntry": whispMappingEntry,
       "tableIndex": tableIndex,
       "protocol": protocol,
       "port": port,
       "localIp": localIp,
       "whispSmTranslationTable": whispSmTranslationTable,
       "whispSmTranslationTableEntry": whispSmTranslationTableEntry,
       "whispTranslationTableIndex": whispTranslationTableIndex,
       "whispTranslationTableMacAddr": whispTranslationTableMacAddr,
       "whispTranslationTableIpAddr": whispTranslationTableIpAddr,
       "whispTranslationTableAge": whispTranslationTableAge,
       "whispSmSecurity": whispSmSecurity,
       "certTable": certTable,
       "certEntry": certEntry,
       "certIndex": certIndex,
       "cert": cert,
       "action": action,
       "certificateDN": certificateDN,
       "numAuthCerts": numAuthCerts,
       "authenticationEnforce": authenticationEnforce,
       "phase1": phase1,
       "phase2": phase2,
       "authOuterId": authOuterId,
       "authPassword": authPassword,
       "authUsername": authUsername,
       "useRealm": useRealm,
       "realm": realm,
       "whispSmControls": whispSmControls,
       "clearLinkStats": clearLinkStats}
)
