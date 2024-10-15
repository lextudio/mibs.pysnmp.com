# SNMP MIB module (HPN-ICF-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:38 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfRdObjects_ObjectIdentity = ObjectIdentity
hpnicfRdObjects = _HpnicfRdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1)
)
_HpnicfRdInfoTable_Object = MibTable
hpnicfRdInfoTable = _HpnicfRdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfRdInfoTable.setStatus("current")
_HpnicfRdInfoEntry_Object = MibTableRow
hpnicfRdInfoEntry = _HpnicfRdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1)
)
hpnicfRdInfoEntry.setIndexNames(
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfRdInfoEntry.setStatus("current")


class _HpnicfRdGroupName_Type(DisplayString):
    """Custom type hpnicfRdGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfRdGroupName_Type.__name__ = "DisplayString"
_HpnicfRdGroupName_Object = MibTableColumn
hpnicfRdGroupName = _HpnicfRdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 1),
    _HpnicfRdGroupName_Type()
)
hpnicfRdGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdGroupName.setStatus("current")
_HpnicfRdPrimAuthIp_Type = IpAddress
_HpnicfRdPrimAuthIp_Object = MibTableColumn
hpnicfRdPrimAuthIp = _HpnicfRdPrimAuthIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 2),
    _HpnicfRdPrimAuthIp_Type()
)
hpnicfRdPrimAuthIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAuthIp.setStatus("deprecated")
_HpnicfRdPrimUdpPort_Type = Integer32
_HpnicfRdPrimUdpPort_Object = MibTableColumn
hpnicfRdPrimUdpPort = _HpnicfRdPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 3),
    _HpnicfRdPrimUdpPort_Type()
)
hpnicfRdPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimUdpPort.setStatus("current")


class _HpnicfRdPrimState_Type(Integer32):
    """Custom type hpnicfRdPrimState based on Integer32"""
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


_HpnicfRdPrimState_Type.__name__ = "Integer32"
_HpnicfRdPrimState_Object = MibTableColumn
hpnicfRdPrimState = _HpnicfRdPrimState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 4),
    _HpnicfRdPrimState_Type()
)
hpnicfRdPrimState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimState.setStatus("current")
_HpnicfRdSecAuthIp_Type = IpAddress
_HpnicfRdSecAuthIp_Object = MibTableColumn
hpnicfRdSecAuthIp = _HpnicfRdSecAuthIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 5),
    _HpnicfRdSecAuthIp_Type()
)
hpnicfRdSecAuthIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAuthIp.setStatus("deprecated")
_HpnicfRdSecUdpPort_Type = Integer32
_HpnicfRdSecUdpPort_Object = MibTableColumn
hpnicfRdSecUdpPort = _HpnicfRdSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 6),
    _HpnicfRdSecUdpPort_Type()
)
hpnicfRdSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecUdpPort.setStatus("current")


class _HpnicfRdSecState_Type(Integer32):
    """Custom type hpnicfRdSecState based on Integer32"""
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


_HpnicfRdSecState_Type.__name__ = "Integer32"
_HpnicfRdSecState_Object = MibTableColumn
hpnicfRdSecState = _HpnicfRdSecState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 7),
    _HpnicfRdSecState_Type()
)
hpnicfRdSecState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecState.setStatus("current")


class _HpnicfRdKey_Type(DisplayString):
    """Custom type hpnicfRdKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfRdKey_Type.__name__ = "DisplayString"
_HpnicfRdKey_Object = MibTableColumn
hpnicfRdKey = _HpnicfRdKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 8),
    _HpnicfRdKey_Type()
)
hpnicfRdKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdKey.setStatus("current")
_HpnicfRdRetry_Type = Integer32
_HpnicfRdRetry_Object = MibTableColumn
hpnicfRdRetry = _HpnicfRdRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 9),
    _HpnicfRdRetry_Type()
)
hpnicfRdRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdRetry.setStatus("current")
_HpnicfRdTimeout_Type = Integer32
_HpnicfRdTimeout_Object = MibTableColumn
hpnicfRdTimeout = _HpnicfRdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 10),
    _HpnicfRdTimeout_Type()
)
hpnicfRdTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdTimeout.setStatus("current")
_HpnicfRdPrimAuthIpAddrType_Type = InetAddressType
_HpnicfRdPrimAuthIpAddrType_Object = MibTableColumn
hpnicfRdPrimAuthIpAddrType = _HpnicfRdPrimAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 11),
    _HpnicfRdPrimAuthIpAddrType_Type()
)
hpnicfRdPrimAuthIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAuthIpAddrType.setStatus("current")
_HpnicfRdPrimAuthIpAddr_Type = InetAddress
_HpnicfRdPrimAuthIpAddr_Object = MibTableColumn
hpnicfRdPrimAuthIpAddr = _HpnicfRdPrimAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 12),
    _HpnicfRdPrimAuthIpAddr_Type()
)
hpnicfRdPrimAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAuthIpAddr.setStatus("current")
_HpnicfRdSecAuthIpAddrType_Type = InetAddressType
_HpnicfRdSecAuthIpAddrType_Object = MibTableColumn
hpnicfRdSecAuthIpAddrType = _HpnicfRdSecAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 13),
    _HpnicfRdSecAuthIpAddrType_Type()
)
hpnicfRdSecAuthIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAuthIpAddrType.setStatus("current")
_HpnicfRdSecAuthIpAddr_Type = InetAddress
_HpnicfRdSecAuthIpAddr_Object = MibTableColumn
hpnicfRdSecAuthIpAddr = _HpnicfRdSecAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 14),
    _HpnicfRdSecAuthIpAddr_Type()
)
hpnicfRdSecAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAuthIpAddr.setStatus("current")


class _HpnicfRdServerType_Type(Integer32):
    """Custom type hpnicfRdServerType based on Integer32"""
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


_HpnicfRdServerType_Type.__name__ = "Integer32"
_HpnicfRdServerType_Object = MibTableColumn
hpnicfRdServerType = _HpnicfRdServerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 15),
    _HpnicfRdServerType_Type()
)
hpnicfRdServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdServerType.setStatus("current")


class _HpnicfRdQuietTime_Type(Integer32):
    """Custom type hpnicfRdQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfRdQuietTime_Type.__name__ = "Integer32"
_HpnicfRdQuietTime_Object = MibTableColumn
hpnicfRdQuietTime = _HpnicfRdQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 16),
    _HpnicfRdQuietTime_Type()
)
hpnicfRdQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdQuietTime.setStatus("current")


class _HpnicfRdUserNameFormat_Type(Integer32):
    """Custom type hpnicfRdUserNameFormat based on Integer32"""
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


_HpnicfRdUserNameFormat_Type.__name__ = "Integer32"
_HpnicfRdUserNameFormat_Object = MibTableColumn
hpnicfRdUserNameFormat = _HpnicfRdUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 17),
    _HpnicfRdUserNameFormat_Type()
)
hpnicfRdUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdUserNameFormat.setStatus("current")
_HpnicfRdRowStatus_Type = RowStatus
_HpnicfRdRowStatus_Object = MibTableColumn
hpnicfRdRowStatus = _HpnicfRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 18),
    _HpnicfRdRowStatus_Type()
)
hpnicfRdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdRowStatus.setStatus("current")


class _HpnicfRdSecKey_Type(DisplayString):
    """Custom type hpnicfRdSecKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfRdSecKey_Type.__name__ = "DisplayString"
_HpnicfRdSecKey_Object = MibTableColumn
hpnicfRdSecKey = _HpnicfRdSecKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 19),
    _HpnicfRdSecKey_Type()
)
hpnicfRdSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecKey.setStatus("current")


class _HpnicfRdPrimVpnName_Type(DisplayString):
    """Custom type hpnicfRdPrimVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfRdPrimVpnName_Type.__name__ = "DisplayString"
_HpnicfRdPrimVpnName_Object = MibTableColumn
hpnicfRdPrimVpnName = _HpnicfRdPrimVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 20),
    _HpnicfRdPrimVpnName_Type()
)
hpnicfRdPrimVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimVpnName.setStatus("current")


class _HpnicfRdSecVpnName_Type(DisplayString):
    """Custom type hpnicfRdSecVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfRdSecVpnName_Type.__name__ = "DisplayString"
_HpnicfRdSecVpnName_Object = MibTableColumn
hpnicfRdSecVpnName = _HpnicfRdSecVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 21),
    _HpnicfRdSecVpnName_Type()
)
hpnicfRdSecVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecVpnName.setStatus("current")
_HpnicfRdAuthNasIpAddrType_Type = InetAddressType
_HpnicfRdAuthNasIpAddrType_Object = MibTableColumn
hpnicfRdAuthNasIpAddrType = _HpnicfRdAuthNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 22),
    _HpnicfRdAuthNasIpAddrType_Type()
)
hpnicfRdAuthNasIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAuthNasIpAddrType.setStatus("current")
_HpnicfRdAuthNasIpAddr_Type = IpAddress
_HpnicfRdAuthNasIpAddr_Object = MibTableColumn
hpnicfRdAuthNasIpAddr = _HpnicfRdAuthNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 23),
    _HpnicfRdAuthNasIpAddr_Type()
)
hpnicfRdAuthNasIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAuthNasIpAddr.setStatus("current")
_HpnicfRdAuthNasIpv6Addr_Type = Ipv6Address
_HpnicfRdAuthNasIpv6Addr_Object = MibTableColumn
hpnicfRdAuthNasIpv6Addr = _HpnicfRdAuthNasIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 1, 1, 24),
    _HpnicfRdAuthNasIpv6Addr_Type()
)
hpnicfRdAuthNasIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAuthNasIpv6Addr.setStatus("current")
_HpnicfRdAccInfoTable_Object = MibTable
hpnicfRdAccInfoTable = _HpnicfRdAccInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfRdAccInfoTable.setStatus("current")
_HpnicfRdAccInfoEntry_Object = MibTableRow
hpnicfRdAccInfoEntry = _HpnicfRdAccInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1)
)
hpnicfRdAccInfoEntry.setIndexNames(
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdAccGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfRdAccInfoEntry.setStatus("current")


class _HpnicfRdAccGroupName_Type(DisplayString):
    """Custom type hpnicfRdAccGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfRdAccGroupName_Type.__name__ = "DisplayString"
_HpnicfRdAccGroupName_Object = MibTableColumn
hpnicfRdAccGroupName = _HpnicfRdAccGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 1),
    _HpnicfRdAccGroupName_Type()
)
hpnicfRdAccGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdAccGroupName.setStatus("current")
_HpnicfRdPrimAccIpAddrType_Type = InetAddressType
_HpnicfRdPrimAccIpAddrType_Object = MibTableColumn
hpnicfRdPrimAccIpAddrType = _HpnicfRdPrimAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 2),
    _HpnicfRdPrimAccIpAddrType_Type()
)
hpnicfRdPrimAccIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAccIpAddrType.setStatus("current")
_HpnicfRdPrimAccIpAddr_Type = InetAddress
_HpnicfRdPrimAccIpAddr_Object = MibTableColumn
hpnicfRdPrimAccIpAddr = _HpnicfRdPrimAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 3),
    _HpnicfRdPrimAccIpAddr_Type()
)
hpnicfRdPrimAccIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAccIpAddr.setStatus("current")
_HpnicfRdPrimAccUdpPort_Type = Integer32
_HpnicfRdPrimAccUdpPort_Object = MibTableColumn
hpnicfRdPrimAccUdpPort = _HpnicfRdPrimAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 4),
    _HpnicfRdPrimAccUdpPort_Type()
)
hpnicfRdPrimAccUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAccUdpPort.setStatus("current")


class _HpnicfRdPrimAccState_Type(Integer32):
    """Custom type hpnicfRdPrimAccState based on Integer32"""
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


_HpnicfRdPrimAccState_Type.__name__ = "Integer32"
_HpnicfRdPrimAccState_Object = MibTableColumn
hpnicfRdPrimAccState = _HpnicfRdPrimAccState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 5),
    _HpnicfRdPrimAccState_Type()
)
hpnicfRdPrimAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAccState.setStatus("current")
_HpnicfRdSecAccIpAddrType_Type = InetAddressType
_HpnicfRdSecAccIpAddrType_Object = MibTableColumn
hpnicfRdSecAccIpAddrType = _HpnicfRdSecAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 6),
    _HpnicfRdSecAccIpAddrType_Type()
)
hpnicfRdSecAccIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAccIpAddrType.setStatus("current")
_HpnicfRdSecAccIpAddr_Type = InetAddress
_HpnicfRdSecAccIpAddr_Object = MibTableColumn
hpnicfRdSecAccIpAddr = _HpnicfRdSecAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 7),
    _HpnicfRdSecAccIpAddr_Type()
)
hpnicfRdSecAccIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAccIpAddr.setStatus("current")
_HpnicfRdSecAccUdpPort_Type = Integer32
_HpnicfRdSecAccUdpPort_Object = MibTableColumn
hpnicfRdSecAccUdpPort = _HpnicfRdSecAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 8),
    _HpnicfRdSecAccUdpPort_Type()
)
hpnicfRdSecAccUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAccUdpPort.setStatus("current")


class _HpnicfRdSecAccState_Type(Integer32):
    """Custom type hpnicfRdSecAccState based on Integer32"""
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


_HpnicfRdSecAccState_Type.__name__ = "Integer32"
_HpnicfRdSecAccState_Object = MibTableColumn
hpnicfRdSecAccState = _HpnicfRdSecAccState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 9),
    _HpnicfRdSecAccState_Type()
)
hpnicfRdSecAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAccState.setStatus("current")


class _HpnicfRdAccKey_Type(DisplayString):
    """Custom type hpnicfRdAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfRdAccKey_Type.__name__ = "DisplayString"
_HpnicfRdAccKey_Object = MibTableColumn
hpnicfRdAccKey = _HpnicfRdAccKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 10),
    _HpnicfRdAccKey_Type()
)
hpnicfRdAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccKey.setStatus("current")
_HpnicfRdAccRetry_Type = Integer32
_HpnicfRdAccRetry_Object = MibTableColumn
hpnicfRdAccRetry = _HpnicfRdAccRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 11),
    _HpnicfRdAccRetry_Type()
)
hpnicfRdAccRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccRetry.setStatus("current")
_HpnicfRdAccTimeout_Type = Integer32
_HpnicfRdAccTimeout_Object = MibTableColumn
hpnicfRdAccTimeout = _HpnicfRdAccTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 12),
    _HpnicfRdAccTimeout_Type()
)
hpnicfRdAccTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccTimeout.setStatus("current")


class _HpnicfRdAccServerType_Type(Integer32):
    """Custom type hpnicfRdAccServerType based on Integer32"""
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


_HpnicfRdAccServerType_Type.__name__ = "Integer32"
_HpnicfRdAccServerType_Object = MibTableColumn
hpnicfRdAccServerType = _HpnicfRdAccServerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 13),
    _HpnicfRdAccServerType_Type()
)
hpnicfRdAccServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccServerType.setStatus("current")


class _HpnicfRdAccQuietTime_Type(Integer32):
    """Custom type hpnicfRdAccQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfRdAccQuietTime_Type.__name__ = "Integer32"
_HpnicfRdAccQuietTime_Object = MibTableColumn
hpnicfRdAccQuietTime = _HpnicfRdAccQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 14),
    _HpnicfRdAccQuietTime_Type()
)
hpnicfRdAccQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccQuietTime.setStatus("current")


class _HpnicfRdAccFailureAction_Type(Integer32):
    """Custom type hpnicfRdAccFailureAction based on Integer32"""
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


_HpnicfRdAccFailureAction_Type.__name__ = "Integer32"
_HpnicfRdAccFailureAction_Object = MibTableColumn
hpnicfRdAccFailureAction = _HpnicfRdAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 15),
    _HpnicfRdAccFailureAction_Type()
)
hpnicfRdAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccFailureAction.setStatus("current")


class _HpnicfRdAccRealTime_Type(Integer32):
    """Custom type hpnicfRdAccRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HpnicfRdAccRealTime_Type.__name__ = "Integer32"
_HpnicfRdAccRealTime_Object = MibTableColumn
hpnicfRdAccRealTime = _HpnicfRdAccRealTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 16),
    _HpnicfRdAccRealTime_Type()
)
hpnicfRdAccRealTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccRealTime.setStatus("current")


class _HpnicfRdAccRealTimeRetry_Type(Integer32):
    """Custom type hpnicfRdAccRealTimeRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfRdAccRealTimeRetry_Type.__name__ = "Integer32"
_HpnicfRdAccRealTimeRetry_Object = MibTableColumn
hpnicfRdAccRealTimeRetry = _HpnicfRdAccRealTimeRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 17),
    _HpnicfRdAccRealTimeRetry_Type()
)
hpnicfRdAccRealTimeRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccRealTimeRetry.setStatus("current")
_HpnicfRdAccSaveStopPktEnable_Type = TruthValue
_HpnicfRdAccSaveStopPktEnable_Object = MibTableColumn
hpnicfRdAccSaveStopPktEnable = _HpnicfRdAccSaveStopPktEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 18),
    _HpnicfRdAccSaveStopPktEnable_Type()
)
hpnicfRdAccSaveStopPktEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccSaveStopPktEnable.setStatus("current")


class _HpnicfRdAccStopRetry_Type(Integer32):
    """Custom type hpnicfRdAccStopRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_HpnicfRdAccStopRetry_Type.__name__ = "Integer32"
_HpnicfRdAccStopRetry_Object = MibTableColumn
hpnicfRdAccStopRetry = _HpnicfRdAccStopRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 19),
    _HpnicfRdAccStopRetry_Type()
)
hpnicfRdAccStopRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccStopRetry.setStatus("current")


class _HpnicfRdAccDataFlowUnit_Type(Integer32):
    """Custom type hpnicfRdAccDataFlowUnit based on Integer32"""
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


_HpnicfRdAccDataFlowUnit_Type.__name__ = "Integer32"
_HpnicfRdAccDataFlowUnit_Object = MibTableColumn
hpnicfRdAccDataFlowUnit = _HpnicfRdAccDataFlowUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 20),
    _HpnicfRdAccDataFlowUnit_Type()
)
hpnicfRdAccDataFlowUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccDataFlowUnit.setStatus("current")


class _HpnicfRdAccPacketUnit_Type(Integer32):
    """Custom type hpnicfRdAccPacketUnit based on Integer32"""
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


_HpnicfRdAccPacketUnit_Type.__name__ = "Integer32"
_HpnicfRdAccPacketUnit_Object = MibTableColumn
hpnicfRdAccPacketUnit = _HpnicfRdAccPacketUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 21),
    _HpnicfRdAccPacketUnit_Type()
)
hpnicfRdAccPacketUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccPacketUnit.setStatus("current")
_HpnicfRdAccRowStatus_Type = RowStatus
_HpnicfRdAccRowStatus_Object = MibTableColumn
hpnicfRdAccRowStatus = _HpnicfRdAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 22),
    _HpnicfRdAccRowStatus_Type()
)
hpnicfRdAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccRowStatus.setStatus("current")
_HpnicfRdAcctOnEnable_Type = TruthValue
_HpnicfRdAcctOnEnable_Object = MibTableColumn
hpnicfRdAcctOnEnable = _HpnicfRdAcctOnEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 23),
    _HpnicfRdAcctOnEnable_Type()
)
hpnicfRdAcctOnEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAcctOnEnable.setStatus("current")


class _HpnicfRdAcctOnSendTimes_Type(Integer32):
    """Custom type hpnicfRdAcctOnSendTimes based on Integer32"""
    defaultValue = 50


_HpnicfRdAcctOnSendTimes_Object = MibTableColumn
hpnicfRdAcctOnSendTimes = _HpnicfRdAcctOnSendTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 24),
    _HpnicfRdAcctOnSendTimes_Type()
)
hpnicfRdAcctOnSendTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAcctOnSendTimes.setStatus("current")


class _HpnicfRdAcctOnSendInterval_Type(Integer32):
    """Custom type hpnicfRdAcctOnSendInterval based on Integer32"""
    defaultValue = 3


_HpnicfRdAcctOnSendInterval_Object = MibTableColumn
hpnicfRdAcctOnSendInterval = _HpnicfRdAcctOnSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 25),
    _HpnicfRdAcctOnSendInterval_Type()
)
hpnicfRdAcctOnSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAcctOnSendInterval.setStatus("current")


class _HpnicfRdSecAccKey_Type(DisplayString):
    """Custom type hpnicfRdSecAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfRdSecAccKey_Type.__name__ = "DisplayString"
_HpnicfRdSecAccKey_Object = MibTableColumn
hpnicfRdSecAccKey = _HpnicfRdSecAccKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 26),
    _HpnicfRdSecAccKey_Type()
)
hpnicfRdSecAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAccKey.setStatus("current")


class _HpnicfRdPrimAccVpnName_Type(DisplayString):
    """Custom type hpnicfRdPrimAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfRdPrimAccVpnName_Type.__name__ = "DisplayString"
_HpnicfRdPrimAccVpnName_Object = MibTableColumn
hpnicfRdPrimAccVpnName = _HpnicfRdPrimAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 27),
    _HpnicfRdPrimAccVpnName_Type()
)
hpnicfRdPrimAccVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdPrimAccVpnName.setStatus("current")


class _HpnicfRdSecAccVpnName_Type(DisplayString):
    """Custom type hpnicfRdSecAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfRdSecAccVpnName_Type.__name__ = "DisplayString"
_HpnicfRdSecAccVpnName_Object = MibTableColumn
hpnicfRdSecAccVpnName = _HpnicfRdSecAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 28),
    _HpnicfRdSecAccVpnName_Type()
)
hpnicfRdSecAccVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecAccVpnName.setStatus("current")
_HpnicfRdAccNasIpAddrType_Type = InetAddressType
_HpnicfRdAccNasIpAddrType_Object = MibTableColumn
hpnicfRdAccNasIpAddrType = _HpnicfRdAccNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 29),
    _HpnicfRdAccNasIpAddrType_Type()
)
hpnicfRdAccNasIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccNasIpAddrType.setStatus("current")
_HpnicfRdAccNasIpAddr_Type = IpAddress
_HpnicfRdAccNasIpAddr_Object = MibTableColumn
hpnicfRdAccNasIpAddr = _HpnicfRdAccNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 30),
    _HpnicfRdAccNasIpAddr_Type()
)
hpnicfRdAccNasIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccNasIpAddr.setStatus("current")
_HpnicfRdAccNasIpv6Addr_Type = Ipv6Address
_HpnicfRdAccNasIpv6Addr_Object = MibTableColumn
hpnicfRdAccNasIpv6Addr = _HpnicfRdAccNasIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 2, 1, 31),
    _HpnicfRdAccNasIpv6Addr_Type()
)
hpnicfRdAccNasIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdAccNasIpv6Addr.setStatus("current")
_HpnicfRadiusGlobalConfig_ObjectIdentity = ObjectIdentity
hpnicfRadiusGlobalConfig = _HpnicfRadiusGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 3)
)


class _HpnicfRadiusAuthErrThreshold_Type(Unsigned32):
    """Custom type hpnicfRadiusAuthErrThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfRadiusAuthErrThreshold_Type.__name__ = "Unsigned32"
_HpnicfRadiusAuthErrThreshold_Object = MibScalar
hpnicfRadiusAuthErrThreshold = _HpnicfRadiusAuthErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 3, 1),
    _HpnicfRadiusAuthErrThreshold_Type()
)
hpnicfRadiusAuthErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRadiusAuthErrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRadiusAuthErrThreshold.setUnits("percentage")
_HpnicfRdSecondaryAuthServerTable_Object = MibTable
hpnicfRdSecondaryAuthServerTable = _HpnicfRdSecondaryAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthServerTable.setStatus("current")
_HpnicfRdSecondaryAuthServerEntry_Object = MibTableRow
hpnicfRdSecondaryAuthServerEntry = _HpnicfRdSecondaryAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1)
)
hpnicfRdSecondaryAuthServerEntry.setIndexNames(
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdGroupName"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAuthIpAddrType"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAuthIpAddr"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAuthVpnName"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAuthUdpPort"),
)
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthServerEntry.setStatus("current")
_HpnicfRdSecondaryAuthIpAddrType_Type = InetAddressType
_HpnicfRdSecondaryAuthIpAddrType_Object = MibTableColumn
hpnicfRdSecondaryAuthIpAddrType = _HpnicfRdSecondaryAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 1),
    _HpnicfRdSecondaryAuthIpAddrType_Type()
)
hpnicfRdSecondaryAuthIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthIpAddrType.setStatus("current")
_HpnicfRdSecondaryAuthIpAddr_Type = InetAddress
_HpnicfRdSecondaryAuthIpAddr_Object = MibTableColumn
hpnicfRdSecondaryAuthIpAddr = _HpnicfRdSecondaryAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 2),
    _HpnicfRdSecondaryAuthIpAddr_Type()
)
hpnicfRdSecondaryAuthIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthIpAddr.setStatus("current")


class _HpnicfRdSecondaryAuthVpnName_Type(DisplayString):
    """Custom type hpnicfRdSecondaryAuthVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfRdSecondaryAuthVpnName_Type.__name__ = "DisplayString"
_HpnicfRdSecondaryAuthVpnName_Object = MibTableColumn
hpnicfRdSecondaryAuthVpnName = _HpnicfRdSecondaryAuthVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 3),
    _HpnicfRdSecondaryAuthVpnName_Type()
)
hpnicfRdSecondaryAuthVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthVpnName.setStatus("current")


class _HpnicfRdSecondaryAuthUdpPort_Type(Integer32):
    """Custom type hpnicfRdSecondaryAuthUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfRdSecondaryAuthUdpPort_Type.__name__ = "Integer32"
_HpnicfRdSecondaryAuthUdpPort_Object = MibTableColumn
hpnicfRdSecondaryAuthUdpPort = _HpnicfRdSecondaryAuthUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 4),
    _HpnicfRdSecondaryAuthUdpPort_Type()
)
hpnicfRdSecondaryAuthUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthUdpPort.setStatus("current")


class _HpnicfRdSecondaryAuthState_Type(Integer32):
    """Custom type hpnicfRdSecondaryAuthState based on Integer32"""
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


_HpnicfRdSecondaryAuthState_Type.__name__ = "Integer32"
_HpnicfRdSecondaryAuthState_Object = MibTableColumn
hpnicfRdSecondaryAuthState = _HpnicfRdSecondaryAuthState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 5),
    _HpnicfRdSecondaryAuthState_Type()
)
hpnicfRdSecondaryAuthState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthState.setStatus("current")


class _HpnicfRdSecondaryAuthKey_Type(DisplayString):
    """Custom type hpnicfRdSecondaryAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfRdSecondaryAuthKey_Type.__name__ = "DisplayString"
_HpnicfRdSecondaryAuthKey_Object = MibTableColumn
hpnicfRdSecondaryAuthKey = _HpnicfRdSecondaryAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 6),
    _HpnicfRdSecondaryAuthKey_Type()
)
hpnicfRdSecondaryAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthKey.setStatus("current")
_HpnicfRdSecondaryAuthRowStatus_Type = RowStatus
_HpnicfRdSecondaryAuthRowStatus_Object = MibTableColumn
hpnicfRdSecondaryAuthRowStatus = _HpnicfRdSecondaryAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 4, 1, 7),
    _HpnicfRdSecondaryAuthRowStatus_Type()
)
hpnicfRdSecondaryAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAuthRowStatus.setStatus("current")
_HpnicfRdSecondaryAccServerTable_Object = MibTable
hpnicfRdSecondaryAccServerTable = _HpnicfRdSecondaryAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccServerTable.setStatus("current")
_HpnicfRdSecondaryAccServerEntry_Object = MibTableRow
hpnicfRdSecondaryAccServerEntry = _HpnicfRdSecondaryAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1)
)
hpnicfRdSecondaryAccServerEntry.setIndexNames(
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdAccGroupName"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAccIpAddrType"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAccIpAddr"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAccVpnName"),
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRdSecondaryAccUdpPort"),
)
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccServerEntry.setStatus("current")
_HpnicfRdSecondaryAccIpAddrType_Type = InetAddressType
_HpnicfRdSecondaryAccIpAddrType_Object = MibTableColumn
hpnicfRdSecondaryAccIpAddrType = _HpnicfRdSecondaryAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 1),
    _HpnicfRdSecondaryAccIpAddrType_Type()
)
hpnicfRdSecondaryAccIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccIpAddrType.setStatus("current")
_HpnicfRdSecondaryAccIpAddr_Type = InetAddress
_HpnicfRdSecondaryAccIpAddr_Object = MibTableColumn
hpnicfRdSecondaryAccIpAddr = _HpnicfRdSecondaryAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 2),
    _HpnicfRdSecondaryAccIpAddr_Type()
)
hpnicfRdSecondaryAccIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccIpAddr.setStatus("current")


class _HpnicfRdSecondaryAccVpnName_Type(DisplayString):
    """Custom type hpnicfRdSecondaryAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfRdSecondaryAccVpnName_Type.__name__ = "DisplayString"
_HpnicfRdSecondaryAccVpnName_Object = MibTableColumn
hpnicfRdSecondaryAccVpnName = _HpnicfRdSecondaryAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 3),
    _HpnicfRdSecondaryAccVpnName_Type()
)
hpnicfRdSecondaryAccVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccVpnName.setStatus("current")


class _HpnicfRdSecondaryAccUdpPort_Type(Integer32):
    """Custom type hpnicfRdSecondaryAccUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfRdSecondaryAccUdpPort_Type.__name__ = "Integer32"
_HpnicfRdSecondaryAccUdpPort_Object = MibTableColumn
hpnicfRdSecondaryAccUdpPort = _HpnicfRdSecondaryAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 4),
    _HpnicfRdSecondaryAccUdpPort_Type()
)
hpnicfRdSecondaryAccUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccUdpPort.setStatus("current")


class _HpnicfRdSecondaryAccState_Type(Integer32):
    """Custom type hpnicfRdSecondaryAccState based on Integer32"""
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


_HpnicfRdSecondaryAccState_Type.__name__ = "Integer32"
_HpnicfRdSecondaryAccState_Object = MibTableColumn
hpnicfRdSecondaryAccState = _HpnicfRdSecondaryAccState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 5),
    _HpnicfRdSecondaryAccState_Type()
)
hpnicfRdSecondaryAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccState.setStatus("current")


class _HpnicfRdSecondaryAccKey_Type(DisplayString):
    """Custom type hpnicfRdSecondaryAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfRdSecondaryAccKey_Type.__name__ = "DisplayString"
_HpnicfRdSecondaryAccKey_Object = MibTableColumn
hpnicfRdSecondaryAccKey = _HpnicfRdSecondaryAccKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 6),
    _HpnicfRdSecondaryAccKey_Type()
)
hpnicfRdSecondaryAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccKey.setStatus("current")
_HpnicfRdSecondaryAccRowStatus_Type = RowStatus
_HpnicfRdSecondaryAccRowStatus_Object = MibTableColumn
hpnicfRdSecondaryAccRowStatus = _HpnicfRdSecondaryAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 1, 5, 1, 7),
    _HpnicfRdSecondaryAccRowStatus_Type()
)
hpnicfRdSecondaryAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRdSecondaryAccRowStatus.setStatus("current")
_HpnicfRadiusAccounting_ObjectIdentity = ObjectIdentity
hpnicfRadiusAccounting = _HpnicfRadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2)
)
_HpnicfRadiusAccClient_ObjectIdentity = ObjectIdentity
hpnicfRadiusAccClient = _HpnicfRadiusAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1)
)
_HpnicfRadiusAccServerTable_Object = MibTable
hpnicfRadiusAccServerTable = _HpnicfRadiusAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfRadiusAccServerTable.setStatus("current")
_HpnicfRadiusAccServerEntry_Object = MibTableRow
hpnicfRadiusAccServerEntry = _HpnicfRadiusAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1)
)
hpnicfRadiusAccServerEntry.setIndexNames(
    (0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRadiusAccServerEntry.setStatus("current")
_HpnicfRadiusAccClientStartRequests_Type = Counter32
_HpnicfRadiusAccClientStartRequests_Object = MibTableColumn
hpnicfRadiusAccClientStartRequests = _HpnicfRadiusAccClientStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1, 1),
    _HpnicfRadiusAccClientStartRequests_Type()
)
hpnicfRadiusAccClientStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAccClientStartRequests.setStatus("current")
_HpnicfRadiusAccClientStartResponses_Type = Counter32
_HpnicfRadiusAccClientStartResponses_Object = MibTableColumn
hpnicfRadiusAccClientStartResponses = _HpnicfRadiusAccClientStartResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1, 2),
    _HpnicfRadiusAccClientStartResponses_Type()
)
hpnicfRadiusAccClientStartResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAccClientStartResponses.setStatus("current")
_HpnicfRadiusAccClientInterimRequests_Type = Counter32
_HpnicfRadiusAccClientInterimRequests_Object = MibTableColumn
hpnicfRadiusAccClientInterimRequests = _HpnicfRadiusAccClientInterimRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1, 3),
    _HpnicfRadiusAccClientInterimRequests_Type()
)
hpnicfRadiusAccClientInterimRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAccClientInterimRequests.setStatus("current")
_HpnicfRadiusAccClientInterimResponses_Type = Counter32
_HpnicfRadiusAccClientInterimResponses_Object = MibTableColumn
hpnicfRadiusAccClientInterimResponses = _HpnicfRadiusAccClientInterimResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1, 4),
    _HpnicfRadiusAccClientInterimResponses_Type()
)
hpnicfRadiusAccClientInterimResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAccClientInterimResponses.setStatus("current")
_HpnicfRadiusAccClientStopRequests_Type = Counter32
_HpnicfRadiusAccClientStopRequests_Object = MibTableColumn
hpnicfRadiusAccClientStopRequests = _HpnicfRadiusAccClientStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1, 5),
    _HpnicfRadiusAccClientStopRequests_Type()
)
hpnicfRadiusAccClientStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAccClientStopRequests.setStatus("current")
_HpnicfRadiusAccClientStopResponses_Type = Counter32
_HpnicfRadiusAccClientStopResponses_Object = MibTableColumn
hpnicfRadiusAccClientStopResponses = _HpnicfRadiusAccClientStopResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 2, 1, 1, 1, 6),
    _HpnicfRadiusAccClientStopResponses_Type()
)
hpnicfRadiusAccClientStopResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAccClientStopResponses.setStatus("current")
_HpnicfRadiusServerTrap_ObjectIdentity = ObjectIdentity
hpnicfRadiusServerTrap = _HpnicfRadiusServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3)
)
_HpnicfRadiusServerTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfRadiusServerTrapPrefix = _HpnicfRadiusServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3, 0)
)
_HpnicfRadiusAuthenticating_ObjectIdentity = ObjectIdentity
hpnicfRadiusAuthenticating = _HpnicfRadiusAuthenticating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4)
)
_HpnicfRadiusAuthClient_ObjectIdentity = ObjectIdentity
hpnicfRadiusAuthClient = _HpnicfRadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4, 1)
)
_HpnicfRadiusAuthServerTable_Object = MibTable
hpnicfRadiusAuthServerTable = _HpnicfRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfRadiusAuthServerTable.setStatus("current")
_HpnicfRadiusAuthServerEntry_Object = MibTableRow
hpnicfRadiusAuthServerEntry = _HpnicfRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4, 1, 1, 1)
)
hpnicfRadiusAuthServerEntry.setIndexNames(
    (0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRadiusAuthServerEntry.setStatus("current")
_HpnicfRadiusAuthFailureTimes_Type = Counter32
_HpnicfRadiusAuthFailureTimes_Object = MibTableColumn
hpnicfRadiusAuthFailureTimes = _HpnicfRadiusAuthFailureTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4, 1, 1, 1, 1),
    _HpnicfRadiusAuthFailureTimes_Type()
)
hpnicfRadiusAuthFailureTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAuthFailureTimes.setStatus("current")
_HpnicfRadiusAuthTimeoutTimes_Type = Counter32
_HpnicfRadiusAuthTimeoutTimes_Object = MibTableColumn
hpnicfRadiusAuthTimeoutTimes = _HpnicfRadiusAuthTimeoutTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4, 1, 1, 1, 2),
    _HpnicfRadiusAuthTimeoutTimes_Type()
)
hpnicfRadiusAuthTimeoutTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAuthTimeoutTimes.setStatus("current")
_HpnicfRadiusAuthRejectTimes_Type = Counter32
_HpnicfRadiusAuthRejectTimes_Object = MibTableColumn
hpnicfRadiusAuthRejectTimes = _HpnicfRadiusAuthRejectTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 4, 1, 1, 1, 3),
    _HpnicfRadiusAuthRejectTimes_Type()
)
hpnicfRadiusAuthRejectTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusAuthRejectTimes.setStatus("current")
_HpnicfRadiusExtend_ObjectIdentity = ObjectIdentity
hpnicfRadiusExtend = _HpnicfRadiusExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5)
)
_HpnicfRadiusExtendObjects_ObjectIdentity = ObjectIdentity
hpnicfRadiusExtendObjects = _HpnicfRadiusExtendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 1)
)
_HpnicfRadiusExtendTables_ObjectIdentity = ObjectIdentity
hpnicfRadiusExtendTables = _HpnicfRadiusExtendTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2)
)
_HpnicfRadiusSchAuthTable_Object = MibTable
hpnicfRadiusSchAuthTable = _HpnicfRadiusSchAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthTable.setStatus("current")
_HpnicfRadiusSchAuthEntry_Object = MibTableRow
hpnicfRadiusSchAuthEntry = _HpnicfRadiusSchAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1)
)
hpnicfRadiusSchAuthEntry.setIndexNames(
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRadiusSchAuthGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthEntry.setStatus("current")
_HpnicfRadiusSchAuthGroupName_Type = DisplayString
_HpnicfRadiusSchAuthGroupName_Object = MibTableColumn
hpnicfRadiusSchAuthGroupName = _HpnicfRadiusSchAuthGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 1),
    _HpnicfRadiusSchAuthGroupName_Type()
)
hpnicfRadiusSchAuthGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthGroupName.setStatus("current")
_HpnicfRadiusSchAuthPrimIpAddr_Type = IpAddress
_HpnicfRadiusSchAuthPrimIpAddr_Object = MibTableColumn
hpnicfRadiusSchAuthPrimIpAddr = _HpnicfRadiusSchAuthPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 2),
    _HpnicfRadiusSchAuthPrimIpAddr_Type()
)
hpnicfRadiusSchAuthPrimIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthPrimIpAddr.setStatus("current")


class _HpnicfRadiusSchAuthPrimUdpPort_Type(Integer32):
    """Custom type hpnicfRadiusSchAuthPrimUdpPort based on Integer32"""
    defaultValue = 1812


_HpnicfRadiusSchAuthPrimUdpPort_Object = MibTableColumn
hpnicfRadiusSchAuthPrimUdpPort = _HpnicfRadiusSchAuthPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 3),
    _HpnicfRadiusSchAuthPrimUdpPort_Type()
)
hpnicfRadiusSchAuthPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthPrimUdpPort.setStatus("current")
_HpnicfRadiusSchAuthPrimKey_Type = DisplayString
_HpnicfRadiusSchAuthPrimKey_Object = MibTableColumn
hpnicfRadiusSchAuthPrimKey = _HpnicfRadiusSchAuthPrimKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 4),
    _HpnicfRadiusSchAuthPrimKey_Type()
)
hpnicfRadiusSchAuthPrimKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthPrimKey.setStatus("current")
_HpnicfRadiusSchAuthSecIpAddr_Type = IpAddress
_HpnicfRadiusSchAuthSecIpAddr_Object = MibTableColumn
hpnicfRadiusSchAuthSecIpAddr = _HpnicfRadiusSchAuthSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 5),
    _HpnicfRadiusSchAuthSecIpAddr_Type()
)
hpnicfRadiusSchAuthSecIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthSecIpAddr.setStatus("current")


class _HpnicfRadiusSchAuthSecUdpPort_Type(Integer32):
    """Custom type hpnicfRadiusSchAuthSecUdpPort based on Integer32"""
    defaultValue = 1812


_HpnicfRadiusSchAuthSecUdpPort_Object = MibTableColumn
hpnicfRadiusSchAuthSecUdpPort = _HpnicfRadiusSchAuthSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 6),
    _HpnicfRadiusSchAuthSecUdpPort_Type()
)
hpnicfRadiusSchAuthSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthSecUdpPort.setStatus("current")
_HpnicfRadiusSchAuthSecKey_Type = DisplayString
_HpnicfRadiusSchAuthSecKey_Object = MibTableColumn
hpnicfRadiusSchAuthSecKey = _HpnicfRadiusSchAuthSecKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 7),
    _HpnicfRadiusSchAuthSecKey_Type()
)
hpnicfRadiusSchAuthSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthSecKey.setStatus("current")
_HpnicfRadiusSchAuthRowStatus_Type = RowStatus
_HpnicfRadiusSchAuthRowStatus_Object = MibTableColumn
hpnicfRadiusSchAuthRowStatus = _HpnicfRadiusSchAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 1, 1, 8),
    _HpnicfRadiusSchAuthRowStatus_Type()
)
hpnicfRadiusSchAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAuthRowStatus.setStatus("current")
_HpnicfRadiusSchAccTable_Object = MibTable
hpnicfRadiusSchAccTable = _HpnicfRadiusSchAccTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccTable.setStatus("current")
_HpnicfRadiusSchAccEntry_Object = MibTableRow
hpnicfRadiusSchAccEntry = _HpnicfRadiusSchAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1)
)
hpnicfRadiusSchAccEntry.setIndexNames(
    (0, "HPN-ICF-RADIUS-MIB", "hpnicfRadiusSchAccGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccEntry.setStatus("current")
_HpnicfRadiusSchAccGroupName_Type = DisplayString
_HpnicfRadiusSchAccGroupName_Object = MibTableColumn
hpnicfRadiusSchAccGroupName = _HpnicfRadiusSchAccGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 1),
    _HpnicfRadiusSchAccGroupName_Type()
)
hpnicfRadiusSchAccGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccGroupName.setStatus("current")
_HpnicfRadiusSchAccPrimIpAddr_Type = IpAddress
_HpnicfRadiusSchAccPrimIpAddr_Object = MibTableColumn
hpnicfRadiusSchAccPrimIpAddr = _HpnicfRadiusSchAccPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 2),
    _HpnicfRadiusSchAccPrimIpAddr_Type()
)
hpnicfRadiusSchAccPrimIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccPrimIpAddr.setStatus("current")


class _HpnicfRadiusSchAccPrimUdpPort_Type(Integer32):
    """Custom type hpnicfRadiusSchAccPrimUdpPort based on Integer32"""
    defaultValue = 1813


_HpnicfRadiusSchAccPrimUdpPort_Object = MibTableColumn
hpnicfRadiusSchAccPrimUdpPort = _HpnicfRadiusSchAccPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 3),
    _HpnicfRadiusSchAccPrimUdpPort_Type()
)
hpnicfRadiusSchAccPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccPrimUdpPort.setStatus("current")
_HpnicfRadiusSchAccPrimKey_Type = DisplayString
_HpnicfRadiusSchAccPrimKey_Object = MibTableColumn
hpnicfRadiusSchAccPrimKey = _HpnicfRadiusSchAccPrimKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 4),
    _HpnicfRadiusSchAccPrimKey_Type()
)
hpnicfRadiusSchAccPrimKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccPrimKey.setStatus("current")
_HpnicfRadiusSchAccSecIpAddr_Type = IpAddress
_HpnicfRadiusSchAccSecIpAddr_Object = MibTableColumn
hpnicfRadiusSchAccSecIpAddr = _HpnicfRadiusSchAccSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 5),
    _HpnicfRadiusSchAccSecIpAddr_Type()
)
hpnicfRadiusSchAccSecIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccSecIpAddr.setStatus("current")


class _HpnicfRadiusSchAccSecUdpPort_Type(Integer32):
    """Custom type hpnicfRadiusSchAccSecUdpPort based on Integer32"""
    defaultValue = 1813


_HpnicfRadiusSchAccSecUdpPort_Object = MibTableColumn
hpnicfRadiusSchAccSecUdpPort = _HpnicfRadiusSchAccSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 6),
    _HpnicfRadiusSchAccSecUdpPort_Type()
)
hpnicfRadiusSchAccSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccSecUdpPort.setStatus("current")
_HpnicfRadiusSchAccSecKey_Type = DisplayString
_HpnicfRadiusSchAccSecKey_Object = MibTableColumn
hpnicfRadiusSchAccSecKey = _HpnicfRadiusSchAccSecKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 7),
    _HpnicfRadiusSchAccSecKey_Type()
)
hpnicfRadiusSchAccSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccSecKey.setStatus("current")
_HpnicfRadiusSchAccRowStatus_Type = RowStatus
_HpnicfRadiusSchAccRowStatus_Object = MibTableColumn
hpnicfRadiusSchAccRowStatus = _HpnicfRadiusSchAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 2, 2, 1, 8),
    _HpnicfRadiusSchAccRowStatus_Type()
)
hpnicfRadiusSchAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRadiusSchAccRowStatus.setStatus("current")
_HpnicfRadiusExtendTraps_ObjectIdentity = ObjectIdentity
hpnicfRadiusExtendTraps = _HpnicfRadiusExtendTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 5, 3)
)
_HpnicfRadiusStatistic_ObjectIdentity = ObjectIdentity
hpnicfRadiusStatistic = _HpnicfRadiusStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 6)
)
_HpnicfRadiusStatAccReq_Type = Counter64
_HpnicfRadiusStatAccReq_Object = MibScalar
hpnicfRadiusStatAccReq = _HpnicfRadiusStatAccReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 6, 1),
    _HpnicfRadiusStatAccReq_Type()
)
hpnicfRadiusStatAccReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusStatAccReq.setStatus("current")
_HpnicfRadiusStatAccAck_Type = Counter64
_HpnicfRadiusStatAccAck_Object = MibScalar
hpnicfRadiusStatAccAck = _HpnicfRadiusStatAccAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 6, 2),
    _HpnicfRadiusStatAccAck_Type()
)
hpnicfRadiusStatAccAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusStatAccAck.setStatus("current")
_HpnicfRadiusStatLogoutReq_Type = Counter64
_HpnicfRadiusStatLogoutReq_Object = MibScalar
hpnicfRadiusStatLogoutReq = _HpnicfRadiusStatLogoutReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 6, 3),
    _HpnicfRadiusStatLogoutReq_Type()
)
hpnicfRadiusStatLogoutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusStatLogoutReq.setStatus("current")
_HpnicfRadiusStatLogoutAck_Type = Counter64
_HpnicfRadiusStatLogoutAck_Object = MibScalar
hpnicfRadiusStatLogoutAck = _HpnicfRadiusStatLogoutAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 6, 4),
    _HpnicfRadiusStatLogoutAck_Type()
)
hpnicfRadiusStatLogoutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRadiusStatLogoutAck.setStatus("current")
_HpnicfRadiusServerTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfRadiusServerTrapVarObjects = _HpnicfRadiusServerTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 7)
)
_HpnicfRadiusServerFirstTrapTime_Type = TimeTicks
_HpnicfRadiusServerFirstTrapTime_Object = MibScalar
hpnicfRadiusServerFirstTrapTime = _HpnicfRadiusServerFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 7, 1),
    _HpnicfRadiusServerFirstTrapTime_Type()
)
hpnicfRadiusServerFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRadiusServerFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfRadiusAuthServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3, 0, 1)
)
hpnicfRadiusAuthServerUpTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("HPN-ICF-RADIUS-MIB", "hpnicfRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfRadiusAuthServerUpTrap.setStatus(
        "current"
    )

hpnicfRadiusAccServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3, 0, 2)
)
hpnicfRadiusAccServerUpTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("HPN-ICF-RADIUS-MIB", "hpnicfRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfRadiusAccServerUpTrap.setStatus(
        "current"
    )

hpnicfRadiusAuthErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3, 0, 3)
)
hpnicfRadiusAuthErrTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    hpnicfRadiusAuthErrTrap.setStatus(
        "current"
    )

hpnicfRadiusAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3, 1)
)
hpnicfRadiusAuthServerDownTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("HPN-ICF-RADIUS-MIB", "hpnicfRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfRadiusAuthServerDownTrap.setStatus(
        "current"
    )

hpnicfRadiusAccServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13, 3, 2)
)
hpnicfRadiusAccServerDownTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("HPN-ICF-RADIUS-MIB", "hpnicfRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfRadiusAccServerDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RADIUS-MIB",
    **{"hpnicfRadius": hpnicfRadius,
       "hpnicfRdObjects": hpnicfRdObjects,
       "hpnicfRdInfoTable": hpnicfRdInfoTable,
       "hpnicfRdInfoEntry": hpnicfRdInfoEntry,
       "hpnicfRdGroupName": hpnicfRdGroupName,
       "hpnicfRdPrimAuthIp": hpnicfRdPrimAuthIp,
       "hpnicfRdPrimUdpPort": hpnicfRdPrimUdpPort,
       "hpnicfRdPrimState": hpnicfRdPrimState,
       "hpnicfRdSecAuthIp": hpnicfRdSecAuthIp,
       "hpnicfRdSecUdpPort": hpnicfRdSecUdpPort,
       "hpnicfRdSecState": hpnicfRdSecState,
       "hpnicfRdKey": hpnicfRdKey,
       "hpnicfRdRetry": hpnicfRdRetry,
       "hpnicfRdTimeout": hpnicfRdTimeout,
       "hpnicfRdPrimAuthIpAddrType": hpnicfRdPrimAuthIpAddrType,
       "hpnicfRdPrimAuthIpAddr": hpnicfRdPrimAuthIpAddr,
       "hpnicfRdSecAuthIpAddrType": hpnicfRdSecAuthIpAddrType,
       "hpnicfRdSecAuthIpAddr": hpnicfRdSecAuthIpAddr,
       "hpnicfRdServerType": hpnicfRdServerType,
       "hpnicfRdQuietTime": hpnicfRdQuietTime,
       "hpnicfRdUserNameFormat": hpnicfRdUserNameFormat,
       "hpnicfRdRowStatus": hpnicfRdRowStatus,
       "hpnicfRdSecKey": hpnicfRdSecKey,
       "hpnicfRdPrimVpnName": hpnicfRdPrimVpnName,
       "hpnicfRdSecVpnName": hpnicfRdSecVpnName,
       "hpnicfRdAuthNasIpAddrType": hpnicfRdAuthNasIpAddrType,
       "hpnicfRdAuthNasIpAddr": hpnicfRdAuthNasIpAddr,
       "hpnicfRdAuthNasIpv6Addr": hpnicfRdAuthNasIpv6Addr,
       "hpnicfRdAccInfoTable": hpnicfRdAccInfoTable,
       "hpnicfRdAccInfoEntry": hpnicfRdAccInfoEntry,
       "hpnicfRdAccGroupName": hpnicfRdAccGroupName,
       "hpnicfRdPrimAccIpAddrType": hpnicfRdPrimAccIpAddrType,
       "hpnicfRdPrimAccIpAddr": hpnicfRdPrimAccIpAddr,
       "hpnicfRdPrimAccUdpPort": hpnicfRdPrimAccUdpPort,
       "hpnicfRdPrimAccState": hpnicfRdPrimAccState,
       "hpnicfRdSecAccIpAddrType": hpnicfRdSecAccIpAddrType,
       "hpnicfRdSecAccIpAddr": hpnicfRdSecAccIpAddr,
       "hpnicfRdSecAccUdpPort": hpnicfRdSecAccUdpPort,
       "hpnicfRdSecAccState": hpnicfRdSecAccState,
       "hpnicfRdAccKey": hpnicfRdAccKey,
       "hpnicfRdAccRetry": hpnicfRdAccRetry,
       "hpnicfRdAccTimeout": hpnicfRdAccTimeout,
       "hpnicfRdAccServerType": hpnicfRdAccServerType,
       "hpnicfRdAccQuietTime": hpnicfRdAccQuietTime,
       "hpnicfRdAccFailureAction": hpnicfRdAccFailureAction,
       "hpnicfRdAccRealTime": hpnicfRdAccRealTime,
       "hpnicfRdAccRealTimeRetry": hpnicfRdAccRealTimeRetry,
       "hpnicfRdAccSaveStopPktEnable": hpnicfRdAccSaveStopPktEnable,
       "hpnicfRdAccStopRetry": hpnicfRdAccStopRetry,
       "hpnicfRdAccDataFlowUnit": hpnicfRdAccDataFlowUnit,
       "hpnicfRdAccPacketUnit": hpnicfRdAccPacketUnit,
       "hpnicfRdAccRowStatus": hpnicfRdAccRowStatus,
       "hpnicfRdAcctOnEnable": hpnicfRdAcctOnEnable,
       "hpnicfRdAcctOnSendTimes": hpnicfRdAcctOnSendTimes,
       "hpnicfRdAcctOnSendInterval": hpnicfRdAcctOnSendInterval,
       "hpnicfRdSecAccKey": hpnicfRdSecAccKey,
       "hpnicfRdPrimAccVpnName": hpnicfRdPrimAccVpnName,
       "hpnicfRdSecAccVpnName": hpnicfRdSecAccVpnName,
       "hpnicfRdAccNasIpAddrType": hpnicfRdAccNasIpAddrType,
       "hpnicfRdAccNasIpAddr": hpnicfRdAccNasIpAddr,
       "hpnicfRdAccNasIpv6Addr": hpnicfRdAccNasIpv6Addr,
       "hpnicfRadiusGlobalConfig": hpnicfRadiusGlobalConfig,
       "hpnicfRadiusAuthErrThreshold": hpnicfRadiusAuthErrThreshold,
       "hpnicfRdSecondaryAuthServerTable": hpnicfRdSecondaryAuthServerTable,
       "hpnicfRdSecondaryAuthServerEntry": hpnicfRdSecondaryAuthServerEntry,
       "hpnicfRdSecondaryAuthIpAddrType": hpnicfRdSecondaryAuthIpAddrType,
       "hpnicfRdSecondaryAuthIpAddr": hpnicfRdSecondaryAuthIpAddr,
       "hpnicfRdSecondaryAuthVpnName": hpnicfRdSecondaryAuthVpnName,
       "hpnicfRdSecondaryAuthUdpPort": hpnicfRdSecondaryAuthUdpPort,
       "hpnicfRdSecondaryAuthState": hpnicfRdSecondaryAuthState,
       "hpnicfRdSecondaryAuthKey": hpnicfRdSecondaryAuthKey,
       "hpnicfRdSecondaryAuthRowStatus": hpnicfRdSecondaryAuthRowStatus,
       "hpnicfRdSecondaryAccServerTable": hpnicfRdSecondaryAccServerTable,
       "hpnicfRdSecondaryAccServerEntry": hpnicfRdSecondaryAccServerEntry,
       "hpnicfRdSecondaryAccIpAddrType": hpnicfRdSecondaryAccIpAddrType,
       "hpnicfRdSecondaryAccIpAddr": hpnicfRdSecondaryAccIpAddr,
       "hpnicfRdSecondaryAccVpnName": hpnicfRdSecondaryAccVpnName,
       "hpnicfRdSecondaryAccUdpPort": hpnicfRdSecondaryAccUdpPort,
       "hpnicfRdSecondaryAccState": hpnicfRdSecondaryAccState,
       "hpnicfRdSecondaryAccKey": hpnicfRdSecondaryAccKey,
       "hpnicfRdSecondaryAccRowStatus": hpnicfRdSecondaryAccRowStatus,
       "hpnicfRadiusAccounting": hpnicfRadiusAccounting,
       "hpnicfRadiusAccClient": hpnicfRadiusAccClient,
       "hpnicfRadiusAccServerTable": hpnicfRadiusAccServerTable,
       "hpnicfRadiusAccServerEntry": hpnicfRadiusAccServerEntry,
       "hpnicfRadiusAccClientStartRequests": hpnicfRadiusAccClientStartRequests,
       "hpnicfRadiusAccClientStartResponses": hpnicfRadiusAccClientStartResponses,
       "hpnicfRadiusAccClientInterimRequests": hpnicfRadiusAccClientInterimRequests,
       "hpnicfRadiusAccClientInterimResponses": hpnicfRadiusAccClientInterimResponses,
       "hpnicfRadiusAccClientStopRequests": hpnicfRadiusAccClientStopRequests,
       "hpnicfRadiusAccClientStopResponses": hpnicfRadiusAccClientStopResponses,
       "hpnicfRadiusServerTrap": hpnicfRadiusServerTrap,
       "hpnicfRadiusServerTrapPrefix": hpnicfRadiusServerTrapPrefix,
       "hpnicfRadiusAuthServerUpTrap": hpnicfRadiusAuthServerUpTrap,
       "hpnicfRadiusAccServerUpTrap": hpnicfRadiusAccServerUpTrap,
       "hpnicfRadiusAuthErrTrap": hpnicfRadiusAuthErrTrap,
       "hpnicfRadiusAuthServerDownTrap": hpnicfRadiusAuthServerDownTrap,
       "hpnicfRadiusAccServerDownTrap": hpnicfRadiusAccServerDownTrap,
       "hpnicfRadiusAuthenticating": hpnicfRadiusAuthenticating,
       "hpnicfRadiusAuthClient": hpnicfRadiusAuthClient,
       "hpnicfRadiusAuthServerTable": hpnicfRadiusAuthServerTable,
       "hpnicfRadiusAuthServerEntry": hpnicfRadiusAuthServerEntry,
       "hpnicfRadiusAuthFailureTimes": hpnicfRadiusAuthFailureTimes,
       "hpnicfRadiusAuthTimeoutTimes": hpnicfRadiusAuthTimeoutTimes,
       "hpnicfRadiusAuthRejectTimes": hpnicfRadiusAuthRejectTimes,
       "hpnicfRadiusExtend": hpnicfRadiusExtend,
       "hpnicfRadiusExtendObjects": hpnicfRadiusExtendObjects,
       "hpnicfRadiusExtendTables": hpnicfRadiusExtendTables,
       "hpnicfRadiusSchAuthTable": hpnicfRadiusSchAuthTable,
       "hpnicfRadiusSchAuthEntry": hpnicfRadiusSchAuthEntry,
       "hpnicfRadiusSchAuthGroupName": hpnicfRadiusSchAuthGroupName,
       "hpnicfRadiusSchAuthPrimIpAddr": hpnicfRadiusSchAuthPrimIpAddr,
       "hpnicfRadiusSchAuthPrimUdpPort": hpnicfRadiusSchAuthPrimUdpPort,
       "hpnicfRadiusSchAuthPrimKey": hpnicfRadiusSchAuthPrimKey,
       "hpnicfRadiusSchAuthSecIpAddr": hpnicfRadiusSchAuthSecIpAddr,
       "hpnicfRadiusSchAuthSecUdpPort": hpnicfRadiusSchAuthSecUdpPort,
       "hpnicfRadiusSchAuthSecKey": hpnicfRadiusSchAuthSecKey,
       "hpnicfRadiusSchAuthRowStatus": hpnicfRadiusSchAuthRowStatus,
       "hpnicfRadiusSchAccTable": hpnicfRadiusSchAccTable,
       "hpnicfRadiusSchAccEntry": hpnicfRadiusSchAccEntry,
       "hpnicfRadiusSchAccGroupName": hpnicfRadiusSchAccGroupName,
       "hpnicfRadiusSchAccPrimIpAddr": hpnicfRadiusSchAccPrimIpAddr,
       "hpnicfRadiusSchAccPrimUdpPort": hpnicfRadiusSchAccPrimUdpPort,
       "hpnicfRadiusSchAccPrimKey": hpnicfRadiusSchAccPrimKey,
       "hpnicfRadiusSchAccSecIpAddr": hpnicfRadiusSchAccSecIpAddr,
       "hpnicfRadiusSchAccSecUdpPort": hpnicfRadiusSchAccSecUdpPort,
       "hpnicfRadiusSchAccSecKey": hpnicfRadiusSchAccSecKey,
       "hpnicfRadiusSchAccRowStatus": hpnicfRadiusSchAccRowStatus,
       "hpnicfRadiusExtendTraps": hpnicfRadiusExtendTraps,
       "hpnicfRadiusStatistic": hpnicfRadiusStatistic,
       "hpnicfRadiusStatAccReq": hpnicfRadiusStatAccReq,
       "hpnicfRadiusStatAccAck": hpnicfRadiusStatAccAck,
       "hpnicfRadiusStatLogoutReq": hpnicfRadiusStatLogoutReq,
       "hpnicfRadiusStatLogoutAck": hpnicfRadiusStatLogoutAck,
       "hpnicfRadiusServerTrapVarObjects": hpnicfRadiusServerTrapVarObjects,
       "hpnicfRadiusServerFirstTrapTime": hpnicfRadiusServerFirstTrapTime}
)
