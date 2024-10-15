# SNMP MIB module (HH3C-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:40 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(radiusAccClientServerPortNumber,
 radiusAccServerAddress,
 radiusAccServerIndex) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccClientServerPortNumber",
    "radiusAccServerAddress",
    "radiusAccServerIndex")

(radiusAuthClientServerPortNumber,
 radiusAuthServerAddress,
 radiusAuthServerIndex) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthClientServerPortNumber",
    "radiusAuthServerAddress",
    "radiusAuthServerIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13)
)
hh3cRadius.setRevisions(
        ("2014-06-07 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cRdObjects_ObjectIdentity = ObjectIdentity
hh3cRdObjects = _Hh3cRdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1)
)
_Hh3cRdInfoTable_Object = MibTable
hh3cRdInfoTable = _Hh3cRdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRdInfoTable.setStatus("current")
_Hh3cRdInfoEntry_Object = MibTableRow
hh3cRdInfoEntry = _Hh3cRdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1)
)
hh3cRdInfoEntry.setIndexNames(
    (0, "HH3C-RADIUS-MIB", "hh3cRdGroupName"),
)
if mibBuilder.loadTexts:
    hh3cRdInfoEntry.setStatus("current")


class _Hh3cRdGroupName_Type(DisplayString):
    """Custom type hh3cRdGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRdGroupName_Type.__name__ = "DisplayString"
_Hh3cRdGroupName_Object = MibTableColumn
hh3cRdGroupName = _Hh3cRdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 1),
    _Hh3cRdGroupName_Type()
)
hh3cRdGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdGroupName.setStatus("current")
_Hh3cRdPrimAuthIp_Type = IpAddress
_Hh3cRdPrimAuthIp_Object = MibTableColumn
hh3cRdPrimAuthIp = _Hh3cRdPrimAuthIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 2),
    _Hh3cRdPrimAuthIp_Type()
)
hh3cRdPrimAuthIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAuthIp.setStatus("deprecated")
_Hh3cRdPrimUdpPort_Type = Integer32
_Hh3cRdPrimUdpPort_Object = MibTableColumn
hh3cRdPrimUdpPort = _Hh3cRdPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 3),
    _Hh3cRdPrimUdpPort_Type()
)
hh3cRdPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimUdpPort.setStatus("current")


class _Hh3cRdPrimState_Type(Integer32):
    """Custom type hh3cRdPrimState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cRdPrimState_Type.__name__ = "Integer32"
_Hh3cRdPrimState_Object = MibTableColumn
hh3cRdPrimState = _Hh3cRdPrimState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 4),
    _Hh3cRdPrimState_Type()
)
hh3cRdPrimState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimState.setStatus("current")
_Hh3cRdSecAuthIp_Type = IpAddress
_Hh3cRdSecAuthIp_Object = MibTableColumn
hh3cRdSecAuthIp = _Hh3cRdSecAuthIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 5),
    _Hh3cRdSecAuthIp_Type()
)
hh3cRdSecAuthIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAuthIp.setStatus("deprecated")
_Hh3cRdSecUdpPort_Type = Integer32
_Hh3cRdSecUdpPort_Object = MibTableColumn
hh3cRdSecUdpPort = _Hh3cRdSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 6),
    _Hh3cRdSecUdpPort_Type()
)
hh3cRdSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecUdpPort.setStatus("current")


class _Hh3cRdSecState_Type(Integer32):
    """Custom type hh3cRdSecState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cRdSecState_Type.__name__ = "Integer32"
_Hh3cRdSecState_Object = MibTableColumn
hh3cRdSecState = _Hh3cRdSecState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 7),
    _Hh3cRdSecState_Type()
)
hh3cRdSecState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecState.setStatus("current")


class _Hh3cRdKey_Type(DisplayString):
    """Custom type hh3cRdKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cRdKey_Type.__name__ = "DisplayString"
_Hh3cRdKey_Object = MibTableColumn
hh3cRdKey = _Hh3cRdKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 8),
    _Hh3cRdKey_Type()
)
hh3cRdKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdKey.setStatus("current")
_Hh3cRdRetry_Type = Integer32
_Hh3cRdRetry_Object = MibTableColumn
hh3cRdRetry = _Hh3cRdRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 9),
    _Hh3cRdRetry_Type()
)
hh3cRdRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdRetry.setStatus("current")
_Hh3cRdTimeout_Type = Integer32
_Hh3cRdTimeout_Object = MibTableColumn
hh3cRdTimeout = _Hh3cRdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 10),
    _Hh3cRdTimeout_Type()
)
hh3cRdTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdTimeout.setStatus("current")
_Hh3cRdPrimAuthIpAddrType_Type = InetAddressType
_Hh3cRdPrimAuthIpAddrType_Object = MibTableColumn
hh3cRdPrimAuthIpAddrType = _Hh3cRdPrimAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 11),
    _Hh3cRdPrimAuthIpAddrType_Type()
)
hh3cRdPrimAuthIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAuthIpAddrType.setStatus("current")
_Hh3cRdPrimAuthIpAddr_Type = InetAddress
_Hh3cRdPrimAuthIpAddr_Object = MibTableColumn
hh3cRdPrimAuthIpAddr = _Hh3cRdPrimAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 12),
    _Hh3cRdPrimAuthIpAddr_Type()
)
hh3cRdPrimAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAuthIpAddr.setStatus("current")
_Hh3cRdSecAuthIpAddrType_Type = InetAddressType
_Hh3cRdSecAuthIpAddrType_Object = MibTableColumn
hh3cRdSecAuthIpAddrType = _Hh3cRdSecAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 13),
    _Hh3cRdSecAuthIpAddrType_Type()
)
hh3cRdSecAuthIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAuthIpAddrType.setStatus("current")
_Hh3cRdSecAuthIpAddr_Type = InetAddress
_Hh3cRdSecAuthIpAddr_Object = MibTableColumn
hh3cRdSecAuthIpAddr = _Hh3cRdSecAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 14),
    _Hh3cRdSecAuthIpAddr_Type()
)
hh3cRdSecAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAuthIpAddr.setStatus("current")


class _Hh3cRdServerType_Type(Integer32):
    """Custom type hh3cRdServerType based on Integer32"""
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
        *(("extended", 4),
          ("iphotel", 2),
          ("portal", 3),
          ("standard", 1))
    )


_Hh3cRdServerType_Type.__name__ = "Integer32"
_Hh3cRdServerType_Object = MibTableColumn
hh3cRdServerType = _Hh3cRdServerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 15),
    _Hh3cRdServerType_Type()
)
hh3cRdServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdServerType.setStatus("current")


class _Hh3cRdQuietTime_Type(Integer32):
    """Custom type hh3cRdQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cRdQuietTime_Type.__name__ = "Integer32"
_Hh3cRdQuietTime_Object = MibTableColumn
hh3cRdQuietTime = _Hh3cRdQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 16),
    _Hh3cRdQuietTime_Type()
)
hh3cRdQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdQuietTime.setStatus("current")


class _Hh3cRdUserNameFormat_Type(Integer32):
    """Custom type hh3cRdUserNameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keeporignal", 3),
          ("withdomain", 2),
          ("withoutdomain", 1))
    )


_Hh3cRdUserNameFormat_Type.__name__ = "Integer32"
_Hh3cRdUserNameFormat_Object = MibTableColumn
hh3cRdUserNameFormat = _Hh3cRdUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 17),
    _Hh3cRdUserNameFormat_Type()
)
hh3cRdUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdUserNameFormat.setStatus("current")
_Hh3cRdRowStatus_Type = RowStatus
_Hh3cRdRowStatus_Object = MibTableColumn
hh3cRdRowStatus = _Hh3cRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 18),
    _Hh3cRdRowStatus_Type()
)
hh3cRdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdRowStatus.setStatus("current")


class _Hh3cRdSecKey_Type(DisplayString):
    """Custom type hh3cRdSecKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cRdSecKey_Type.__name__ = "DisplayString"
_Hh3cRdSecKey_Object = MibTableColumn
hh3cRdSecKey = _Hh3cRdSecKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 19),
    _Hh3cRdSecKey_Type()
)
hh3cRdSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecKey.setStatus("current")


class _Hh3cRdPrimVpnName_Type(DisplayString):
    """Custom type hh3cRdPrimVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cRdPrimVpnName_Type.__name__ = "DisplayString"
_Hh3cRdPrimVpnName_Object = MibTableColumn
hh3cRdPrimVpnName = _Hh3cRdPrimVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 20),
    _Hh3cRdPrimVpnName_Type()
)
hh3cRdPrimVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimVpnName.setStatus("current")


class _Hh3cRdSecVpnName_Type(DisplayString):
    """Custom type hh3cRdSecVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cRdSecVpnName_Type.__name__ = "DisplayString"
_Hh3cRdSecVpnName_Object = MibTableColumn
hh3cRdSecVpnName = _Hh3cRdSecVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 21),
    _Hh3cRdSecVpnName_Type()
)
hh3cRdSecVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecVpnName.setStatus("current")
_Hh3cRdAuthNasIpAddrType_Type = InetAddressType
_Hh3cRdAuthNasIpAddrType_Object = MibTableColumn
hh3cRdAuthNasIpAddrType = _Hh3cRdAuthNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 22),
    _Hh3cRdAuthNasIpAddrType_Type()
)
hh3cRdAuthNasIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAuthNasIpAddrType.setStatus("current")
_Hh3cRdAuthNasIpAddr_Type = IpAddress
_Hh3cRdAuthNasIpAddr_Object = MibTableColumn
hh3cRdAuthNasIpAddr = _Hh3cRdAuthNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 23),
    _Hh3cRdAuthNasIpAddr_Type()
)
hh3cRdAuthNasIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAuthNasIpAddr.setStatus("current")
_Hh3cRdAuthNasIpv6Addr_Type = Ipv6Address
_Hh3cRdAuthNasIpv6Addr_Object = MibTableColumn
hh3cRdAuthNasIpv6Addr = _Hh3cRdAuthNasIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 1, 1, 24),
    _Hh3cRdAuthNasIpv6Addr_Type()
)
hh3cRdAuthNasIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAuthNasIpv6Addr.setStatus("current")
_Hh3cRdAccInfoTable_Object = MibTable
hh3cRdAccInfoTable = _Hh3cRdAccInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cRdAccInfoTable.setStatus("current")
_Hh3cRdAccInfoEntry_Object = MibTableRow
hh3cRdAccInfoEntry = _Hh3cRdAccInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1)
)
hh3cRdAccInfoEntry.setIndexNames(
    (0, "HH3C-RADIUS-MIB", "hh3cRdAccGroupName"),
)
if mibBuilder.loadTexts:
    hh3cRdAccInfoEntry.setStatus("current")


class _Hh3cRdAccGroupName_Type(DisplayString):
    """Custom type hh3cRdAccGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRdAccGroupName_Type.__name__ = "DisplayString"
_Hh3cRdAccGroupName_Object = MibTableColumn
hh3cRdAccGroupName = _Hh3cRdAccGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 1),
    _Hh3cRdAccGroupName_Type()
)
hh3cRdAccGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdAccGroupName.setStatus("current")
_Hh3cRdPrimAccIpAddrType_Type = InetAddressType
_Hh3cRdPrimAccIpAddrType_Object = MibTableColumn
hh3cRdPrimAccIpAddrType = _Hh3cRdPrimAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 2),
    _Hh3cRdPrimAccIpAddrType_Type()
)
hh3cRdPrimAccIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAccIpAddrType.setStatus("current")
_Hh3cRdPrimAccIpAddr_Type = InetAddress
_Hh3cRdPrimAccIpAddr_Object = MibTableColumn
hh3cRdPrimAccIpAddr = _Hh3cRdPrimAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 3),
    _Hh3cRdPrimAccIpAddr_Type()
)
hh3cRdPrimAccIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAccIpAddr.setStatus("current")
_Hh3cRdPrimAccUdpPort_Type = Integer32
_Hh3cRdPrimAccUdpPort_Object = MibTableColumn
hh3cRdPrimAccUdpPort = _Hh3cRdPrimAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 4),
    _Hh3cRdPrimAccUdpPort_Type()
)
hh3cRdPrimAccUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAccUdpPort.setStatus("current")


class _Hh3cRdPrimAccState_Type(Integer32):
    """Custom type hh3cRdPrimAccState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cRdPrimAccState_Type.__name__ = "Integer32"
_Hh3cRdPrimAccState_Object = MibTableColumn
hh3cRdPrimAccState = _Hh3cRdPrimAccState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 5),
    _Hh3cRdPrimAccState_Type()
)
hh3cRdPrimAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAccState.setStatus("current")
_Hh3cRdSecAccIpAddrType_Type = InetAddressType
_Hh3cRdSecAccIpAddrType_Object = MibTableColumn
hh3cRdSecAccIpAddrType = _Hh3cRdSecAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 6),
    _Hh3cRdSecAccIpAddrType_Type()
)
hh3cRdSecAccIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAccIpAddrType.setStatus("current")
_Hh3cRdSecAccIpAddr_Type = InetAddress
_Hh3cRdSecAccIpAddr_Object = MibTableColumn
hh3cRdSecAccIpAddr = _Hh3cRdSecAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 7),
    _Hh3cRdSecAccIpAddr_Type()
)
hh3cRdSecAccIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAccIpAddr.setStatus("current")
_Hh3cRdSecAccUdpPort_Type = Integer32
_Hh3cRdSecAccUdpPort_Object = MibTableColumn
hh3cRdSecAccUdpPort = _Hh3cRdSecAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 8),
    _Hh3cRdSecAccUdpPort_Type()
)
hh3cRdSecAccUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAccUdpPort.setStatus("current")


class _Hh3cRdSecAccState_Type(Integer32):
    """Custom type hh3cRdSecAccState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cRdSecAccState_Type.__name__ = "Integer32"
_Hh3cRdSecAccState_Object = MibTableColumn
hh3cRdSecAccState = _Hh3cRdSecAccState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 9),
    _Hh3cRdSecAccState_Type()
)
hh3cRdSecAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAccState.setStatus("current")


class _Hh3cRdAccKey_Type(DisplayString):
    """Custom type hh3cRdAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cRdAccKey_Type.__name__ = "DisplayString"
_Hh3cRdAccKey_Object = MibTableColumn
hh3cRdAccKey = _Hh3cRdAccKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 10),
    _Hh3cRdAccKey_Type()
)
hh3cRdAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccKey.setStatus("current")
_Hh3cRdAccRetry_Type = Integer32
_Hh3cRdAccRetry_Object = MibTableColumn
hh3cRdAccRetry = _Hh3cRdAccRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 11),
    _Hh3cRdAccRetry_Type()
)
hh3cRdAccRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccRetry.setStatus("current")
_Hh3cRdAccTimeout_Type = Integer32
_Hh3cRdAccTimeout_Object = MibTableColumn
hh3cRdAccTimeout = _Hh3cRdAccTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 12),
    _Hh3cRdAccTimeout_Type()
)
hh3cRdAccTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccTimeout.setStatus("current")


class _Hh3cRdAccServerType_Type(Integer32):
    """Custom type hh3cRdAccServerType based on Integer32"""
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
        *(("extended", 4),
          ("iphotel", 2),
          ("portal", 3),
          ("standard", 1))
    )


_Hh3cRdAccServerType_Type.__name__ = "Integer32"
_Hh3cRdAccServerType_Object = MibTableColumn
hh3cRdAccServerType = _Hh3cRdAccServerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 13),
    _Hh3cRdAccServerType_Type()
)
hh3cRdAccServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccServerType.setStatus("current")


class _Hh3cRdAccQuietTime_Type(Integer32):
    """Custom type hh3cRdAccQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cRdAccQuietTime_Type.__name__ = "Integer32"
_Hh3cRdAccQuietTime_Object = MibTableColumn
hh3cRdAccQuietTime = _Hh3cRdAccQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 14),
    _Hh3cRdAccQuietTime_Type()
)
hh3cRdAccQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccQuietTime.setStatus("current")


class _Hh3cRdAccFailureAction_Type(Integer32):
    """Custom type hh3cRdAccFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("reject", 2))
    )


_Hh3cRdAccFailureAction_Type.__name__ = "Integer32"
_Hh3cRdAccFailureAction_Object = MibTableColumn
hh3cRdAccFailureAction = _Hh3cRdAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 15),
    _Hh3cRdAccFailureAction_Type()
)
hh3cRdAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccFailureAction.setStatus("current")


class _Hh3cRdAccRealTime_Type(Integer32):
    """Custom type hh3cRdAccRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Hh3cRdAccRealTime_Type.__name__ = "Integer32"
_Hh3cRdAccRealTime_Object = MibTableColumn
hh3cRdAccRealTime = _Hh3cRdAccRealTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 16),
    _Hh3cRdAccRealTime_Type()
)
hh3cRdAccRealTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccRealTime.setStatus("current")


class _Hh3cRdAccRealTimeRetry_Type(Integer32):
    """Custom type hh3cRdAccRealTimeRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cRdAccRealTimeRetry_Type.__name__ = "Integer32"
_Hh3cRdAccRealTimeRetry_Object = MibTableColumn
hh3cRdAccRealTimeRetry = _Hh3cRdAccRealTimeRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 17),
    _Hh3cRdAccRealTimeRetry_Type()
)
hh3cRdAccRealTimeRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccRealTimeRetry.setStatus("current")
_Hh3cRdAccSaveStopPktEnable_Type = TruthValue
_Hh3cRdAccSaveStopPktEnable_Object = MibTableColumn
hh3cRdAccSaveStopPktEnable = _Hh3cRdAccSaveStopPktEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 18),
    _Hh3cRdAccSaveStopPktEnable_Type()
)
hh3cRdAccSaveStopPktEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccSaveStopPktEnable.setStatus("current")


class _Hh3cRdAccStopRetry_Type(Integer32):
    """Custom type hh3cRdAccStopRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_Hh3cRdAccStopRetry_Type.__name__ = "Integer32"
_Hh3cRdAccStopRetry_Object = MibTableColumn
hh3cRdAccStopRetry = _Hh3cRdAccStopRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 19),
    _Hh3cRdAccStopRetry_Type()
)
hh3cRdAccStopRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccStopRetry.setStatus("current")


class _Hh3cRdAccDataFlowUnit_Type(Integer32):
    """Custom type hh3cRdAccDataFlowUnit based on Integer32"""
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
        *(("byte", 1),
          ("gigaByte", 4),
          ("kiloByte", 2),
          ("megaByte", 3))
    )


_Hh3cRdAccDataFlowUnit_Type.__name__ = "Integer32"
_Hh3cRdAccDataFlowUnit_Object = MibTableColumn
hh3cRdAccDataFlowUnit = _Hh3cRdAccDataFlowUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 20),
    _Hh3cRdAccDataFlowUnit_Type()
)
hh3cRdAccDataFlowUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccDataFlowUnit.setStatus("current")


class _Hh3cRdAccPacketUnit_Type(Integer32):
    """Custom type hh3cRdAccPacketUnit based on Integer32"""
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
        *(("gigaPacket", 4),
          ("kiloPacket", 2),
          ("megaPacket", 3),
          ("onePacket", 1))
    )


_Hh3cRdAccPacketUnit_Type.__name__ = "Integer32"
_Hh3cRdAccPacketUnit_Object = MibTableColumn
hh3cRdAccPacketUnit = _Hh3cRdAccPacketUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 21),
    _Hh3cRdAccPacketUnit_Type()
)
hh3cRdAccPacketUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccPacketUnit.setStatus("current")
_Hh3cRdAccRowStatus_Type = RowStatus
_Hh3cRdAccRowStatus_Object = MibTableColumn
hh3cRdAccRowStatus = _Hh3cRdAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 22),
    _Hh3cRdAccRowStatus_Type()
)
hh3cRdAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccRowStatus.setStatus("current")
_Hh3cRdAcctOnEnable_Type = TruthValue
_Hh3cRdAcctOnEnable_Object = MibTableColumn
hh3cRdAcctOnEnable = _Hh3cRdAcctOnEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 23),
    _Hh3cRdAcctOnEnable_Type()
)
hh3cRdAcctOnEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAcctOnEnable.setStatus("current")


class _Hh3cRdAcctOnSendTimes_Type(Integer32):
    """Custom type hh3cRdAcctOnSendTimes based on Integer32"""
    defaultValue = 50


_Hh3cRdAcctOnSendTimes_Object = MibTableColumn
hh3cRdAcctOnSendTimes = _Hh3cRdAcctOnSendTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 24),
    _Hh3cRdAcctOnSendTimes_Type()
)
hh3cRdAcctOnSendTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAcctOnSendTimes.setStatus("current")


class _Hh3cRdAcctOnSendInterval_Type(Integer32):
    """Custom type hh3cRdAcctOnSendInterval based on Integer32"""
    defaultValue = 3


_Hh3cRdAcctOnSendInterval_Object = MibTableColumn
hh3cRdAcctOnSendInterval = _Hh3cRdAcctOnSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 25),
    _Hh3cRdAcctOnSendInterval_Type()
)
hh3cRdAcctOnSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAcctOnSendInterval.setStatus("current")


class _Hh3cRdSecAccKey_Type(DisplayString):
    """Custom type hh3cRdSecAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cRdSecAccKey_Type.__name__ = "DisplayString"
_Hh3cRdSecAccKey_Object = MibTableColumn
hh3cRdSecAccKey = _Hh3cRdSecAccKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 26),
    _Hh3cRdSecAccKey_Type()
)
hh3cRdSecAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAccKey.setStatus("current")


class _Hh3cRdPrimAccVpnName_Type(DisplayString):
    """Custom type hh3cRdPrimAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cRdPrimAccVpnName_Type.__name__ = "DisplayString"
_Hh3cRdPrimAccVpnName_Object = MibTableColumn
hh3cRdPrimAccVpnName = _Hh3cRdPrimAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 27),
    _Hh3cRdPrimAccVpnName_Type()
)
hh3cRdPrimAccVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdPrimAccVpnName.setStatus("current")


class _Hh3cRdSecAccVpnName_Type(DisplayString):
    """Custom type hh3cRdSecAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cRdSecAccVpnName_Type.__name__ = "DisplayString"
_Hh3cRdSecAccVpnName_Object = MibTableColumn
hh3cRdSecAccVpnName = _Hh3cRdSecAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 28),
    _Hh3cRdSecAccVpnName_Type()
)
hh3cRdSecAccVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecAccVpnName.setStatus("current")
_Hh3cRdAccNasIpAddrType_Type = InetAddressType
_Hh3cRdAccNasIpAddrType_Object = MibTableColumn
hh3cRdAccNasIpAddrType = _Hh3cRdAccNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 29),
    _Hh3cRdAccNasIpAddrType_Type()
)
hh3cRdAccNasIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccNasIpAddrType.setStatus("current")
_Hh3cRdAccNasIpAddr_Type = IpAddress
_Hh3cRdAccNasIpAddr_Object = MibTableColumn
hh3cRdAccNasIpAddr = _Hh3cRdAccNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 30),
    _Hh3cRdAccNasIpAddr_Type()
)
hh3cRdAccNasIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccNasIpAddr.setStatus("current")
_Hh3cRdAccNasIpv6Addr_Type = Ipv6Address
_Hh3cRdAccNasIpv6Addr_Object = MibTableColumn
hh3cRdAccNasIpv6Addr = _Hh3cRdAccNasIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 2, 1, 31),
    _Hh3cRdAccNasIpv6Addr_Type()
)
hh3cRdAccNasIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdAccNasIpv6Addr.setStatus("current")
_Hh3cRadiusGlobalConfig_ObjectIdentity = ObjectIdentity
hh3cRadiusGlobalConfig = _Hh3cRadiusGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 3)
)


class _Hh3cRadiusAuthErrThreshold_Type(Unsigned32):
    """Custom type hh3cRadiusAuthErrThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cRadiusAuthErrThreshold_Type.__name__ = "Unsigned32"
_Hh3cRadiusAuthErrThreshold_Object = MibScalar
hh3cRadiusAuthErrThreshold = _Hh3cRadiusAuthErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 3, 1),
    _Hh3cRadiusAuthErrThreshold_Type()
)
hh3cRadiusAuthErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRadiusAuthErrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRadiusAuthErrThreshold.setUnits("percentage")
_Hh3cRdSecondaryAuthServerTable_Object = MibTable
hh3cRdSecondaryAuthServerTable = _Hh3cRdSecondaryAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthServerTable.setStatus("current")
_Hh3cRdSecondaryAuthServerEntry_Object = MibTableRow
hh3cRdSecondaryAuthServerEntry = _Hh3cRdSecondaryAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1)
)
hh3cRdSecondaryAuthServerEntry.setIndexNames(
    (0, "HH3C-RADIUS-MIB", "hh3cRdGroupName"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAuthIpAddrType"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAuthIpAddr"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAuthVpnName"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAuthUdpPort"),
)
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthServerEntry.setStatus("current")
_Hh3cRdSecondaryAuthIpAddrType_Type = InetAddressType
_Hh3cRdSecondaryAuthIpAddrType_Object = MibTableColumn
hh3cRdSecondaryAuthIpAddrType = _Hh3cRdSecondaryAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 1),
    _Hh3cRdSecondaryAuthIpAddrType_Type()
)
hh3cRdSecondaryAuthIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthIpAddrType.setStatus("current")
_Hh3cRdSecondaryAuthIpAddr_Type = InetAddress
_Hh3cRdSecondaryAuthIpAddr_Object = MibTableColumn
hh3cRdSecondaryAuthIpAddr = _Hh3cRdSecondaryAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 2),
    _Hh3cRdSecondaryAuthIpAddr_Type()
)
hh3cRdSecondaryAuthIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthIpAddr.setStatus("current")


class _Hh3cRdSecondaryAuthVpnName_Type(DisplayString):
    """Custom type hh3cRdSecondaryAuthVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cRdSecondaryAuthVpnName_Type.__name__ = "DisplayString"
_Hh3cRdSecondaryAuthVpnName_Object = MibTableColumn
hh3cRdSecondaryAuthVpnName = _Hh3cRdSecondaryAuthVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 3),
    _Hh3cRdSecondaryAuthVpnName_Type()
)
hh3cRdSecondaryAuthVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthVpnName.setStatus("current")


class _Hh3cRdSecondaryAuthUdpPort_Type(Integer32):
    """Custom type hh3cRdSecondaryAuthUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cRdSecondaryAuthUdpPort_Type.__name__ = "Integer32"
_Hh3cRdSecondaryAuthUdpPort_Object = MibTableColumn
hh3cRdSecondaryAuthUdpPort = _Hh3cRdSecondaryAuthUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 4),
    _Hh3cRdSecondaryAuthUdpPort_Type()
)
hh3cRdSecondaryAuthUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthUdpPort.setStatus("current")


class _Hh3cRdSecondaryAuthState_Type(Integer32):
    """Custom type hh3cRdSecondaryAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cRdSecondaryAuthState_Type.__name__ = "Integer32"
_Hh3cRdSecondaryAuthState_Object = MibTableColumn
hh3cRdSecondaryAuthState = _Hh3cRdSecondaryAuthState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 5),
    _Hh3cRdSecondaryAuthState_Type()
)
hh3cRdSecondaryAuthState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthState.setStatus("current")


class _Hh3cRdSecondaryAuthKey_Type(DisplayString):
    """Custom type hh3cRdSecondaryAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cRdSecondaryAuthKey_Type.__name__ = "DisplayString"
_Hh3cRdSecondaryAuthKey_Object = MibTableColumn
hh3cRdSecondaryAuthKey = _Hh3cRdSecondaryAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 6),
    _Hh3cRdSecondaryAuthKey_Type()
)
hh3cRdSecondaryAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthKey.setStatus("current")
_Hh3cRdSecondaryAuthRowStatus_Type = RowStatus
_Hh3cRdSecondaryAuthRowStatus_Object = MibTableColumn
hh3cRdSecondaryAuthRowStatus = _Hh3cRdSecondaryAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 4, 1, 7),
    _Hh3cRdSecondaryAuthRowStatus_Type()
)
hh3cRdSecondaryAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAuthRowStatus.setStatus("current")
_Hh3cRdSecondaryAccServerTable_Object = MibTable
hh3cRdSecondaryAccServerTable = _Hh3cRdSecondaryAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccServerTable.setStatus("current")
_Hh3cRdSecondaryAccServerEntry_Object = MibTableRow
hh3cRdSecondaryAccServerEntry = _Hh3cRdSecondaryAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1)
)
hh3cRdSecondaryAccServerEntry.setIndexNames(
    (0, "HH3C-RADIUS-MIB", "hh3cRdAccGroupName"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAccIpAddrType"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAccIpAddr"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAccVpnName"),
    (0, "HH3C-RADIUS-MIB", "hh3cRdSecondaryAccUdpPort"),
)
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccServerEntry.setStatus("current")
_Hh3cRdSecondaryAccIpAddrType_Type = InetAddressType
_Hh3cRdSecondaryAccIpAddrType_Object = MibTableColumn
hh3cRdSecondaryAccIpAddrType = _Hh3cRdSecondaryAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 1),
    _Hh3cRdSecondaryAccIpAddrType_Type()
)
hh3cRdSecondaryAccIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccIpAddrType.setStatus("current")
_Hh3cRdSecondaryAccIpAddr_Type = InetAddress
_Hh3cRdSecondaryAccIpAddr_Object = MibTableColumn
hh3cRdSecondaryAccIpAddr = _Hh3cRdSecondaryAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 2),
    _Hh3cRdSecondaryAccIpAddr_Type()
)
hh3cRdSecondaryAccIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccIpAddr.setStatus("current")


class _Hh3cRdSecondaryAccVpnName_Type(DisplayString):
    """Custom type hh3cRdSecondaryAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cRdSecondaryAccVpnName_Type.__name__ = "DisplayString"
_Hh3cRdSecondaryAccVpnName_Object = MibTableColumn
hh3cRdSecondaryAccVpnName = _Hh3cRdSecondaryAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 3),
    _Hh3cRdSecondaryAccVpnName_Type()
)
hh3cRdSecondaryAccVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccVpnName.setStatus("current")


class _Hh3cRdSecondaryAccUdpPort_Type(Integer32):
    """Custom type hh3cRdSecondaryAccUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cRdSecondaryAccUdpPort_Type.__name__ = "Integer32"
_Hh3cRdSecondaryAccUdpPort_Object = MibTableColumn
hh3cRdSecondaryAccUdpPort = _Hh3cRdSecondaryAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 4),
    _Hh3cRdSecondaryAccUdpPort_Type()
)
hh3cRdSecondaryAccUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccUdpPort.setStatus("current")


class _Hh3cRdSecondaryAccState_Type(Integer32):
    """Custom type hh3cRdSecondaryAccState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cRdSecondaryAccState_Type.__name__ = "Integer32"
_Hh3cRdSecondaryAccState_Object = MibTableColumn
hh3cRdSecondaryAccState = _Hh3cRdSecondaryAccState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 5),
    _Hh3cRdSecondaryAccState_Type()
)
hh3cRdSecondaryAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccState.setStatus("current")


class _Hh3cRdSecondaryAccKey_Type(DisplayString):
    """Custom type hh3cRdSecondaryAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cRdSecondaryAccKey_Type.__name__ = "DisplayString"
_Hh3cRdSecondaryAccKey_Object = MibTableColumn
hh3cRdSecondaryAccKey = _Hh3cRdSecondaryAccKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 6),
    _Hh3cRdSecondaryAccKey_Type()
)
hh3cRdSecondaryAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccKey.setStatus("current")
_Hh3cRdSecondaryAccRowStatus_Type = RowStatus
_Hh3cRdSecondaryAccRowStatus_Object = MibTableColumn
hh3cRdSecondaryAccRowStatus = _Hh3cRdSecondaryAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 1, 5, 1, 7),
    _Hh3cRdSecondaryAccRowStatus_Type()
)
hh3cRdSecondaryAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRdSecondaryAccRowStatus.setStatus("current")
_Hh3cRadiusAccounting_ObjectIdentity = ObjectIdentity
hh3cRadiusAccounting = _Hh3cRadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2)
)
_Hh3cRadiusAccClient_ObjectIdentity = ObjectIdentity
hh3cRadiusAccClient = _Hh3cRadiusAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1)
)
_Hh3cRadiusAccServerTable_Object = MibTable
hh3cRadiusAccServerTable = _Hh3cRadiusAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRadiusAccServerTable.setStatus("current")
_Hh3cRadiusAccServerEntry_Object = MibTableRow
hh3cRadiusAccServerEntry = _Hh3cRadiusAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1)
)
hh3cRadiusAccServerEntry.setIndexNames(
    (0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    hh3cRadiusAccServerEntry.setStatus("current")
_Hh3cRadiusAccClientStartRequests_Type = Counter32
_Hh3cRadiusAccClientStartRequests_Object = MibTableColumn
hh3cRadiusAccClientStartRequests = _Hh3cRadiusAccClientStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1, 1),
    _Hh3cRadiusAccClientStartRequests_Type()
)
hh3cRadiusAccClientStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAccClientStartRequests.setStatus("current")
_Hh3cRadiusAccClientStartResponses_Type = Counter32
_Hh3cRadiusAccClientStartResponses_Object = MibTableColumn
hh3cRadiusAccClientStartResponses = _Hh3cRadiusAccClientStartResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1, 2),
    _Hh3cRadiusAccClientStartResponses_Type()
)
hh3cRadiusAccClientStartResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAccClientStartResponses.setStatus("current")
_Hh3cRadiusAccClientInterimRequests_Type = Counter32
_Hh3cRadiusAccClientInterimRequests_Object = MibTableColumn
hh3cRadiusAccClientInterimRequests = _Hh3cRadiusAccClientInterimRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1, 3),
    _Hh3cRadiusAccClientInterimRequests_Type()
)
hh3cRadiusAccClientInterimRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAccClientInterimRequests.setStatus("current")
_Hh3cRadiusAccClientInterimResponses_Type = Counter32
_Hh3cRadiusAccClientInterimResponses_Object = MibTableColumn
hh3cRadiusAccClientInterimResponses = _Hh3cRadiusAccClientInterimResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1, 4),
    _Hh3cRadiusAccClientInterimResponses_Type()
)
hh3cRadiusAccClientInterimResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAccClientInterimResponses.setStatus("current")
_Hh3cRadiusAccClientStopRequests_Type = Counter32
_Hh3cRadiusAccClientStopRequests_Object = MibTableColumn
hh3cRadiusAccClientStopRequests = _Hh3cRadiusAccClientStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1, 5),
    _Hh3cRadiusAccClientStopRequests_Type()
)
hh3cRadiusAccClientStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAccClientStopRequests.setStatus("current")
_Hh3cRadiusAccClientStopResponses_Type = Counter32
_Hh3cRadiusAccClientStopResponses_Object = MibTableColumn
hh3cRadiusAccClientStopResponses = _Hh3cRadiusAccClientStopResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 2, 1, 1, 1, 6),
    _Hh3cRadiusAccClientStopResponses_Type()
)
hh3cRadiusAccClientStopResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAccClientStopResponses.setStatus("current")
_Hh3cRadiusServerTrap_ObjectIdentity = ObjectIdentity
hh3cRadiusServerTrap = _Hh3cRadiusServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3)
)
_Hh3cRadiusServerTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cRadiusServerTrapPrefix = _Hh3cRadiusServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3, 0)
)
_Hh3cRadiusAuthenticating_ObjectIdentity = ObjectIdentity
hh3cRadiusAuthenticating = _Hh3cRadiusAuthenticating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4)
)
_Hh3cRadiusAuthClient_ObjectIdentity = ObjectIdentity
hh3cRadiusAuthClient = _Hh3cRadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4, 1)
)
_Hh3cRadiusAuthServerTable_Object = MibTable
hh3cRadiusAuthServerTable = _Hh3cRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cRadiusAuthServerTable.setStatus("current")
_Hh3cRadiusAuthServerEntry_Object = MibTableRow
hh3cRadiusAuthServerEntry = _Hh3cRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4, 1, 1, 1)
)
hh3cRadiusAuthServerEntry.setIndexNames(
    (0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    hh3cRadiusAuthServerEntry.setStatus("current")
_Hh3cRadiusAuthFailureTimes_Type = Counter32
_Hh3cRadiusAuthFailureTimes_Object = MibTableColumn
hh3cRadiusAuthFailureTimes = _Hh3cRadiusAuthFailureTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4, 1, 1, 1, 1),
    _Hh3cRadiusAuthFailureTimes_Type()
)
hh3cRadiusAuthFailureTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAuthFailureTimes.setStatus("current")
_Hh3cRadiusAuthTimeoutTimes_Type = Counter32
_Hh3cRadiusAuthTimeoutTimes_Object = MibTableColumn
hh3cRadiusAuthTimeoutTimes = _Hh3cRadiusAuthTimeoutTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4, 1, 1, 1, 2),
    _Hh3cRadiusAuthTimeoutTimes_Type()
)
hh3cRadiusAuthTimeoutTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAuthTimeoutTimes.setStatus("current")
_Hh3cRadiusAuthRejectTimes_Type = Counter32
_Hh3cRadiusAuthRejectTimes_Object = MibTableColumn
hh3cRadiusAuthRejectTimes = _Hh3cRadiusAuthRejectTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 4, 1, 1, 1, 3),
    _Hh3cRadiusAuthRejectTimes_Type()
)
hh3cRadiusAuthRejectTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusAuthRejectTimes.setStatus("current")
_Hh3cRadiusExtend_ObjectIdentity = ObjectIdentity
hh3cRadiusExtend = _Hh3cRadiusExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5)
)
_Hh3cRadiusExtendObjects_ObjectIdentity = ObjectIdentity
hh3cRadiusExtendObjects = _Hh3cRadiusExtendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 1)
)
_Hh3cRadiusExtendTables_ObjectIdentity = ObjectIdentity
hh3cRadiusExtendTables = _Hh3cRadiusExtendTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2)
)
_Hh3cRadiusSchAuthTable_Object = MibTable
hh3cRadiusSchAuthTable = _Hh3cRadiusSchAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthTable.setStatus("current")
_Hh3cRadiusSchAuthEntry_Object = MibTableRow
hh3cRadiusSchAuthEntry = _Hh3cRadiusSchAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1)
)
hh3cRadiusSchAuthEntry.setIndexNames(
    (0, "HH3C-RADIUS-MIB", "hh3cRadiusSchAuthGroupName"),
)
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthEntry.setStatus("current")
_Hh3cRadiusSchAuthGroupName_Type = DisplayString
_Hh3cRadiusSchAuthGroupName_Object = MibTableColumn
hh3cRadiusSchAuthGroupName = _Hh3cRadiusSchAuthGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 1),
    _Hh3cRadiusSchAuthGroupName_Type()
)
hh3cRadiusSchAuthGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthGroupName.setStatus("current")
_Hh3cRadiusSchAuthPrimIpAddr_Type = IpAddress
_Hh3cRadiusSchAuthPrimIpAddr_Object = MibTableColumn
hh3cRadiusSchAuthPrimIpAddr = _Hh3cRadiusSchAuthPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 2),
    _Hh3cRadiusSchAuthPrimIpAddr_Type()
)
hh3cRadiusSchAuthPrimIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthPrimIpAddr.setStatus("current")


class _Hh3cRadiusSchAuthPrimUdpPort_Type(Integer32):
    """Custom type hh3cRadiusSchAuthPrimUdpPort based on Integer32"""
    defaultValue = 1812


_Hh3cRadiusSchAuthPrimUdpPort_Object = MibTableColumn
hh3cRadiusSchAuthPrimUdpPort = _Hh3cRadiusSchAuthPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 3),
    _Hh3cRadiusSchAuthPrimUdpPort_Type()
)
hh3cRadiusSchAuthPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthPrimUdpPort.setStatus("current")
_Hh3cRadiusSchAuthPrimKey_Type = DisplayString
_Hh3cRadiusSchAuthPrimKey_Object = MibTableColumn
hh3cRadiusSchAuthPrimKey = _Hh3cRadiusSchAuthPrimKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 4),
    _Hh3cRadiusSchAuthPrimKey_Type()
)
hh3cRadiusSchAuthPrimKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthPrimKey.setStatus("current")
_Hh3cRadiusSchAuthSecIpAddr_Type = IpAddress
_Hh3cRadiusSchAuthSecIpAddr_Object = MibTableColumn
hh3cRadiusSchAuthSecIpAddr = _Hh3cRadiusSchAuthSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 5),
    _Hh3cRadiusSchAuthSecIpAddr_Type()
)
hh3cRadiusSchAuthSecIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthSecIpAddr.setStatus("current")


class _Hh3cRadiusSchAuthSecUdpPort_Type(Integer32):
    """Custom type hh3cRadiusSchAuthSecUdpPort based on Integer32"""
    defaultValue = 1812


_Hh3cRadiusSchAuthSecUdpPort_Object = MibTableColumn
hh3cRadiusSchAuthSecUdpPort = _Hh3cRadiusSchAuthSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 6),
    _Hh3cRadiusSchAuthSecUdpPort_Type()
)
hh3cRadiusSchAuthSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthSecUdpPort.setStatus("current")
_Hh3cRadiusSchAuthSecKey_Type = DisplayString
_Hh3cRadiusSchAuthSecKey_Object = MibTableColumn
hh3cRadiusSchAuthSecKey = _Hh3cRadiusSchAuthSecKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 7),
    _Hh3cRadiusSchAuthSecKey_Type()
)
hh3cRadiusSchAuthSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthSecKey.setStatus("current")
_Hh3cRadiusSchAuthRowStatus_Type = RowStatus
_Hh3cRadiusSchAuthRowStatus_Object = MibTableColumn
hh3cRadiusSchAuthRowStatus = _Hh3cRadiusSchAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 1, 1, 8),
    _Hh3cRadiusSchAuthRowStatus_Type()
)
hh3cRadiusSchAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAuthRowStatus.setStatus("current")
_Hh3cRadiusSchAccTable_Object = MibTable
hh3cRadiusSchAccTable = _Hh3cRadiusSchAccTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRadiusSchAccTable.setStatus("current")
_Hh3cRadiusSchAccEntry_Object = MibTableRow
hh3cRadiusSchAccEntry = _Hh3cRadiusSchAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1)
)
hh3cRadiusSchAccEntry.setIndexNames(
    (0, "HH3C-RADIUS-MIB", "hh3cRadiusSchAccGroupName"),
)
if mibBuilder.loadTexts:
    hh3cRadiusSchAccEntry.setStatus("current")
_Hh3cRadiusSchAccGroupName_Type = DisplayString
_Hh3cRadiusSchAccGroupName_Object = MibTableColumn
hh3cRadiusSchAccGroupName = _Hh3cRadiusSchAccGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 1),
    _Hh3cRadiusSchAccGroupName_Type()
)
hh3cRadiusSchAccGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccGroupName.setStatus("current")
_Hh3cRadiusSchAccPrimIpAddr_Type = IpAddress
_Hh3cRadiusSchAccPrimIpAddr_Object = MibTableColumn
hh3cRadiusSchAccPrimIpAddr = _Hh3cRadiusSchAccPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 2),
    _Hh3cRadiusSchAccPrimIpAddr_Type()
)
hh3cRadiusSchAccPrimIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccPrimIpAddr.setStatus("current")


class _Hh3cRadiusSchAccPrimUdpPort_Type(Integer32):
    """Custom type hh3cRadiusSchAccPrimUdpPort based on Integer32"""
    defaultValue = 1813


_Hh3cRadiusSchAccPrimUdpPort_Object = MibTableColumn
hh3cRadiusSchAccPrimUdpPort = _Hh3cRadiusSchAccPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 3),
    _Hh3cRadiusSchAccPrimUdpPort_Type()
)
hh3cRadiusSchAccPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccPrimUdpPort.setStatus("current")
_Hh3cRadiusSchAccPrimKey_Type = DisplayString
_Hh3cRadiusSchAccPrimKey_Object = MibTableColumn
hh3cRadiusSchAccPrimKey = _Hh3cRadiusSchAccPrimKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 4),
    _Hh3cRadiusSchAccPrimKey_Type()
)
hh3cRadiusSchAccPrimKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccPrimKey.setStatus("current")
_Hh3cRadiusSchAccSecIpAddr_Type = IpAddress
_Hh3cRadiusSchAccSecIpAddr_Object = MibTableColumn
hh3cRadiusSchAccSecIpAddr = _Hh3cRadiusSchAccSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 5),
    _Hh3cRadiusSchAccSecIpAddr_Type()
)
hh3cRadiusSchAccSecIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccSecIpAddr.setStatus("current")


class _Hh3cRadiusSchAccSecUdpPort_Type(Integer32):
    """Custom type hh3cRadiusSchAccSecUdpPort based on Integer32"""
    defaultValue = 1813


_Hh3cRadiusSchAccSecUdpPort_Object = MibTableColumn
hh3cRadiusSchAccSecUdpPort = _Hh3cRadiusSchAccSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 6),
    _Hh3cRadiusSchAccSecUdpPort_Type()
)
hh3cRadiusSchAccSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccSecUdpPort.setStatus("current")
_Hh3cRadiusSchAccSecKey_Type = DisplayString
_Hh3cRadiusSchAccSecKey_Object = MibTableColumn
hh3cRadiusSchAccSecKey = _Hh3cRadiusSchAccSecKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 7),
    _Hh3cRadiusSchAccSecKey_Type()
)
hh3cRadiusSchAccSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccSecKey.setStatus("current")
_Hh3cRadiusSchAccRowStatus_Type = RowStatus
_Hh3cRadiusSchAccRowStatus_Object = MibTableColumn
hh3cRadiusSchAccRowStatus = _Hh3cRadiusSchAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 2, 2, 1, 8),
    _Hh3cRadiusSchAccRowStatus_Type()
)
hh3cRadiusSchAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRadiusSchAccRowStatus.setStatus("current")
_Hh3cRadiusExtendTraps_ObjectIdentity = ObjectIdentity
hh3cRadiusExtendTraps = _Hh3cRadiusExtendTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 5, 3)
)
_Hh3cRadiusStatistic_ObjectIdentity = ObjectIdentity
hh3cRadiusStatistic = _Hh3cRadiusStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 6)
)
_Hh3cRadiusStatAccReq_Type = Counter64
_Hh3cRadiusStatAccReq_Object = MibScalar
hh3cRadiusStatAccReq = _Hh3cRadiusStatAccReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 6, 1),
    _Hh3cRadiusStatAccReq_Type()
)
hh3cRadiusStatAccReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusStatAccReq.setStatus("current")
_Hh3cRadiusStatAccAck_Type = Counter64
_Hh3cRadiusStatAccAck_Object = MibScalar
hh3cRadiusStatAccAck = _Hh3cRadiusStatAccAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 6, 2),
    _Hh3cRadiusStatAccAck_Type()
)
hh3cRadiusStatAccAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusStatAccAck.setStatus("current")
_Hh3cRadiusStatLogoutReq_Type = Counter64
_Hh3cRadiusStatLogoutReq_Object = MibScalar
hh3cRadiusStatLogoutReq = _Hh3cRadiusStatLogoutReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 6, 3),
    _Hh3cRadiusStatLogoutReq_Type()
)
hh3cRadiusStatLogoutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusStatLogoutReq.setStatus("current")
_Hh3cRadiusStatLogoutAck_Type = Counter64
_Hh3cRadiusStatLogoutAck_Object = MibScalar
hh3cRadiusStatLogoutAck = _Hh3cRadiusStatLogoutAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 6, 4),
    _Hh3cRadiusStatLogoutAck_Type()
)
hh3cRadiusStatLogoutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRadiusStatLogoutAck.setStatus("current")
_Hh3cRadiusServerTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cRadiusServerTrapVarObjects = _Hh3cRadiusServerTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 7)
)
_Hh3cRadiusServerFirstTrapTime_Type = TimeTicks
_Hh3cRadiusServerFirstTrapTime_Object = MibScalar
hh3cRadiusServerFirstTrapTime = _Hh3cRadiusServerFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 7, 1),
    _Hh3cRadiusServerFirstTrapTime_Type()
)
hh3cRadiusServerFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRadiusServerFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cRadiusAuthServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3, 0, 1)
)
hh3cRadiusAuthServerUpTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("HH3C-RADIUS-MIB", "hh3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cRadiusAuthServerUpTrap.setStatus(
        "current"
    )

hh3cRadiusAccServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3, 0, 2)
)
hh3cRadiusAccServerUpTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("HH3C-RADIUS-MIB", "hh3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cRadiusAccServerUpTrap.setStatus(
        "current"
    )

hh3cRadiusAuthErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3, 0, 3)
)
hh3cRadiusAuthErrTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    hh3cRadiusAuthErrTrap.setStatus(
        "current"
    )

hh3cRadiusAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3, 1)
)
hh3cRadiusAuthServerDownTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("HH3C-RADIUS-MIB", "hh3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cRadiusAuthServerDownTrap.setStatus(
        "current"
    )

hh3cRadiusAccServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13, 3, 2)
)
hh3cRadiusAccServerDownTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("HH3C-RADIUS-MIB", "hh3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cRadiusAccServerDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RADIUS-MIB",
    **{"hh3cRadius": hh3cRadius,
       "hh3cRdObjects": hh3cRdObjects,
       "hh3cRdInfoTable": hh3cRdInfoTable,
       "hh3cRdInfoEntry": hh3cRdInfoEntry,
       "hh3cRdGroupName": hh3cRdGroupName,
       "hh3cRdPrimAuthIp": hh3cRdPrimAuthIp,
       "hh3cRdPrimUdpPort": hh3cRdPrimUdpPort,
       "hh3cRdPrimState": hh3cRdPrimState,
       "hh3cRdSecAuthIp": hh3cRdSecAuthIp,
       "hh3cRdSecUdpPort": hh3cRdSecUdpPort,
       "hh3cRdSecState": hh3cRdSecState,
       "hh3cRdKey": hh3cRdKey,
       "hh3cRdRetry": hh3cRdRetry,
       "hh3cRdTimeout": hh3cRdTimeout,
       "hh3cRdPrimAuthIpAddrType": hh3cRdPrimAuthIpAddrType,
       "hh3cRdPrimAuthIpAddr": hh3cRdPrimAuthIpAddr,
       "hh3cRdSecAuthIpAddrType": hh3cRdSecAuthIpAddrType,
       "hh3cRdSecAuthIpAddr": hh3cRdSecAuthIpAddr,
       "hh3cRdServerType": hh3cRdServerType,
       "hh3cRdQuietTime": hh3cRdQuietTime,
       "hh3cRdUserNameFormat": hh3cRdUserNameFormat,
       "hh3cRdRowStatus": hh3cRdRowStatus,
       "hh3cRdSecKey": hh3cRdSecKey,
       "hh3cRdPrimVpnName": hh3cRdPrimVpnName,
       "hh3cRdSecVpnName": hh3cRdSecVpnName,
       "hh3cRdAuthNasIpAddrType": hh3cRdAuthNasIpAddrType,
       "hh3cRdAuthNasIpAddr": hh3cRdAuthNasIpAddr,
       "hh3cRdAuthNasIpv6Addr": hh3cRdAuthNasIpv6Addr,
       "hh3cRdAccInfoTable": hh3cRdAccInfoTable,
       "hh3cRdAccInfoEntry": hh3cRdAccInfoEntry,
       "hh3cRdAccGroupName": hh3cRdAccGroupName,
       "hh3cRdPrimAccIpAddrType": hh3cRdPrimAccIpAddrType,
       "hh3cRdPrimAccIpAddr": hh3cRdPrimAccIpAddr,
       "hh3cRdPrimAccUdpPort": hh3cRdPrimAccUdpPort,
       "hh3cRdPrimAccState": hh3cRdPrimAccState,
       "hh3cRdSecAccIpAddrType": hh3cRdSecAccIpAddrType,
       "hh3cRdSecAccIpAddr": hh3cRdSecAccIpAddr,
       "hh3cRdSecAccUdpPort": hh3cRdSecAccUdpPort,
       "hh3cRdSecAccState": hh3cRdSecAccState,
       "hh3cRdAccKey": hh3cRdAccKey,
       "hh3cRdAccRetry": hh3cRdAccRetry,
       "hh3cRdAccTimeout": hh3cRdAccTimeout,
       "hh3cRdAccServerType": hh3cRdAccServerType,
       "hh3cRdAccQuietTime": hh3cRdAccQuietTime,
       "hh3cRdAccFailureAction": hh3cRdAccFailureAction,
       "hh3cRdAccRealTime": hh3cRdAccRealTime,
       "hh3cRdAccRealTimeRetry": hh3cRdAccRealTimeRetry,
       "hh3cRdAccSaveStopPktEnable": hh3cRdAccSaveStopPktEnable,
       "hh3cRdAccStopRetry": hh3cRdAccStopRetry,
       "hh3cRdAccDataFlowUnit": hh3cRdAccDataFlowUnit,
       "hh3cRdAccPacketUnit": hh3cRdAccPacketUnit,
       "hh3cRdAccRowStatus": hh3cRdAccRowStatus,
       "hh3cRdAcctOnEnable": hh3cRdAcctOnEnable,
       "hh3cRdAcctOnSendTimes": hh3cRdAcctOnSendTimes,
       "hh3cRdAcctOnSendInterval": hh3cRdAcctOnSendInterval,
       "hh3cRdSecAccKey": hh3cRdSecAccKey,
       "hh3cRdPrimAccVpnName": hh3cRdPrimAccVpnName,
       "hh3cRdSecAccVpnName": hh3cRdSecAccVpnName,
       "hh3cRdAccNasIpAddrType": hh3cRdAccNasIpAddrType,
       "hh3cRdAccNasIpAddr": hh3cRdAccNasIpAddr,
       "hh3cRdAccNasIpv6Addr": hh3cRdAccNasIpv6Addr,
       "hh3cRadiusGlobalConfig": hh3cRadiusGlobalConfig,
       "hh3cRadiusAuthErrThreshold": hh3cRadiusAuthErrThreshold,
       "hh3cRdSecondaryAuthServerTable": hh3cRdSecondaryAuthServerTable,
       "hh3cRdSecondaryAuthServerEntry": hh3cRdSecondaryAuthServerEntry,
       "hh3cRdSecondaryAuthIpAddrType": hh3cRdSecondaryAuthIpAddrType,
       "hh3cRdSecondaryAuthIpAddr": hh3cRdSecondaryAuthIpAddr,
       "hh3cRdSecondaryAuthVpnName": hh3cRdSecondaryAuthVpnName,
       "hh3cRdSecondaryAuthUdpPort": hh3cRdSecondaryAuthUdpPort,
       "hh3cRdSecondaryAuthState": hh3cRdSecondaryAuthState,
       "hh3cRdSecondaryAuthKey": hh3cRdSecondaryAuthKey,
       "hh3cRdSecondaryAuthRowStatus": hh3cRdSecondaryAuthRowStatus,
       "hh3cRdSecondaryAccServerTable": hh3cRdSecondaryAccServerTable,
       "hh3cRdSecondaryAccServerEntry": hh3cRdSecondaryAccServerEntry,
       "hh3cRdSecondaryAccIpAddrType": hh3cRdSecondaryAccIpAddrType,
       "hh3cRdSecondaryAccIpAddr": hh3cRdSecondaryAccIpAddr,
       "hh3cRdSecondaryAccVpnName": hh3cRdSecondaryAccVpnName,
       "hh3cRdSecondaryAccUdpPort": hh3cRdSecondaryAccUdpPort,
       "hh3cRdSecondaryAccState": hh3cRdSecondaryAccState,
       "hh3cRdSecondaryAccKey": hh3cRdSecondaryAccKey,
       "hh3cRdSecondaryAccRowStatus": hh3cRdSecondaryAccRowStatus,
       "hh3cRadiusAccounting": hh3cRadiusAccounting,
       "hh3cRadiusAccClient": hh3cRadiusAccClient,
       "hh3cRadiusAccServerTable": hh3cRadiusAccServerTable,
       "hh3cRadiusAccServerEntry": hh3cRadiusAccServerEntry,
       "hh3cRadiusAccClientStartRequests": hh3cRadiusAccClientStartRequests,
       "hh3cRadiusAccClientStartResponses": hh3cRadiusAccClientStartResponses,
       "hh3cRadiusAccClientInterimRequests": hh3cRadiusAccClientInterimRequests,
       "hh3cRadiusAccClientInterimResponses": hh3cRadiusAccClientInterimResponses,
       "hh3cRadiusAccClientStopRequests": hh3cRadiusAccClientStopRequests,
       "hh3cRadiusAccClientStopResponses": hh3cRadiusAccClientStopResponses,
       "hh3cRadiusServerTrap": hh3cRadiusServerTrap,
       "hh3cRadiusServerTrapPrefix": hh3cRadiusServerTrapPrefix,
       "hh3cRadiusAuthServerUpTrap": hh3cRadiusAuthServerUpTrap,
       "hh3cRadiusAccServerUpTrap": hh3cRadiusAccServerUpTrap,
       "hh3cRadiusAuthErrTrap": hh3cRadiusAuthErrTrap,
       "hh3cRadiusAuthServerDownTrap": hh3cRadiusAuthServerDownTrap,
       "hh3cRadiusAccServerDownTrap": hh3cRadiusAccServerDownTrap,
       "hh3cRadiusAuthenticating": hh3cRadiusAuthenticating,
       "hh3cRadiusAuthClient": hh3cRadiusAuthClient,
       "hh3cRadiusAuthServerTable": hh3cRadiusAuthServerTable,
       "hh3cRadiusAuthServerEntry": hh3cRadiusAuthServerEntry,
       "hh3cRadiusAuthFailureTimes": hh3cRadiusAuthFailureTimes,
       "hh3cRadiusAuthTimeoutTimes": hh3cRadiusAuthTimeoutTimes,
       "hh3cRadiusAuthRejectTimes": hh3cRadiusAuthRejectTimes,
       "hh3cRadiusExtend": hh3cRadiusExtend,
       "hh3cRadiusExtendObjects": hh3cRadiusExtendObjects,
       "hh3cRadiusExtendTables": hh3cRadiusExtendTables,
       "hh3cRadiusSchAuthTable": hh3cRadiusSchAuthTable,
       "hh3cRadiusSchAuthEntry": hh3cRadiusSchAuthEntry,
       "hh3cRadiusSchAuthGroupName": hh3cRadiusSchAuthGroupName,
       "hh3cRadiusSchAuthPrimIpAddr": hh3cRadiusSchAuthPrimIpAddr,
       "hh3cRadiusSchAuthPrimUdpPort": hh3cRadiusSchAuthPrimUdpPort,
       "hh3cRadiusSchAuthPrimKey": hh3cRadiusSchAuthPrimKey,
       "hh3cRadiusSchAuthSecIpAddr": hh3cRadiusSchAuthSecIpAddr,
       "hh3cRadiusSchAuthSecUdpPort": hh3cRadiusSchAuthSecUdpPort,
       "hh3cRadiusSchAuthSecKey": hh3cRadiusSchAuthSecKey,
       "hh3cRadiusSchAuthRowStatus": hh3cRadiusSchAuthRowStatus,
       "hh3cRadiusSchAccTable": hh3cRadiusSchAccTable,
       "hh3cRadiusSchAccEntry": hh3cRadiusSchAccEntry,
       "hh3cRadiusSchAccGroupName": hh3cRadiusSchAccGroupName,
       "hh3cRadiusSchAccPrimIpAddr": hh3cRadiusSchAccPrimIpAddr,
       "hh3cRadiusSchAccPrimUdpPort": hh3cRadiusSchAccPrimUdpPort,
       "hh3cRadiusSchAccPrimKey": hh3cRadiusSchAccPrimKey,
       "hh3cRadiusSchAccSecIpAddr": hh3cRadiusSchAccSecIpAddr,
       "hh3cRadiusSchAccSecUdpPort": hh3cRadiusSchAccSecUdpPort,
       "hh3cRadiusSchAccSecKey": hh3cRadiusSchAccSecKey,
       "hh3cRadiusSchAccRowStatus": hh3cRadiusSchAccRowStatus,
       "hh3cRadiusExtendTraps": hh3cRadiusExtendTraps,
       "hh3cRadiusStatistic": hh3cRadiusStatistic,
       "hh3cRadiusStatAccReq": hh3cRadiusStatAccReq,
       "hh3cRadiusStatAccAck": hh3cRadiusStatAccAck,
       "hh3cRadiusStatLogoutReq": hh3cRadiusStatLogoutReq,
       "hh3cRadiusStatLogoutAck": hh3cRadiusStatLogoutAck,
       "hh3cRadiusServerTrapVarObjects": hh3cRadiusServerTrapVarObjects,
       "hh3cRadiusServerFirstTrapTime": hh3cRadiusServerFirstTrapTime}
)
