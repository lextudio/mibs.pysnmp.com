# SNMP MIB module (A3COM-HUAWEI-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:57 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

h3cRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cRdObjects_ObjectIdentity = ObjectIdentity
h3cRdObjects = _H3cRdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1)
)
_H3cRdInfoTable_Object = MibTable
h3cRdInfoTable = _H3cRdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRdInfoTable.setStatus("current")
_H3cRdInfoEntry_Object = MibTableRow
h3cRdInfoEntry = _H3cRdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1)
)
h3cRdInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdGroupName"),
)
if mibBuilder.loadTexts:
    h3cRdInfoEntry.setStatus("current")


class _H3cRdGroupName_Type(DisplayString):
    """Custom type h3cRdGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRdGroupName_Type.__name__ = "DisplayString"
_H3cRdGroupName_Object = MibTableColumn
h3cRdGroupName = _H3cRdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 1),
    _H3cRdGroupName_Type()
)
h3cRdGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdGroupName.setStatus("current")
_H3cRdPrimAuthIp_Type = IpAddress
_H3cRdPrimAuthIp_Object = MibTableColumn
h3cRdPrimAuthIp = _H3cRdPrimAuthIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 2),
    _H3cRdPrimAuthIp_Type()
)
h3cRdPrimAuthIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAuthIp.setStatus("deprecated")
_H3cRdPrimUdpPort_Type = Integer32
_H3cRdPrimUdpPort_Object = MibTableColumn
h3cRdPrimUdpPort = _H3cRdPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 3),
    _H3cRdPrimUdpPort_Type()
)
h3cRdPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimUdpPort.setStatus("current")


class _H3cRdPrimState_Type(Integer32):
    """Custom type h3cRdPrimState based on Integer32"""
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


_H3cRdPrimState_Type.__name__ = "Integer32"
_H3cRdPrimState_Object = MibTableColumn
h3cRdPrimState = _H3cRdPrimState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 4),
    _H3cRdPrimState_Type()
)
h3cRdPrimState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimState.setStatus("current")
_H3cRdSecAuthIp_Type = IpAddress
_H3cRdSecAuthIp_Object = MibTableColumn
h3cRdSecAuthIp = _H3cRdSecAuthIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 5),
    _H3cRdSecAuthIp_Type()
)
h3cRdSecAuthIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAuthIp.setStatus("deprecated")
_H3cRdSecUdpPort_Type = Integer32
_H3cRdSecUdpPort_Object = MibTableColumn
h3cRdSecUdpPort = _H3cRdSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 6),
    _H3cRdSecUdpPort_Type()
)
h3cRdSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecUdpPort.setStatus("current")


class _H3cRdSecState_Type(Integer32):
    """Custom type h3cRdSecState based on Integer32"""
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


_H3cRdSecState_Type.__name__ = "Integer32"
_H3cRdSecState_Object = MibTableColumn
h3cRdSecState = _H3cRdSecState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 7),
    _H3cRdSecState_Type()
)
h3cRdSecState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecState.setStatus("current")


class _H3cRdKey_Type(DisplayString):
    """Custom type h3cRdKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRdKey_Type.__name__ = "DisplayString"
_H3cRdKey_Object = MibTableColumn
h3cRdKey = _H3cRdKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 8),
    _H3cRdKey_Type()
)
h3cRdKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdKey.setStatus("current")
_H3cRdRetry_Type = Integer32
_H3cRdRetry_Object = MibTableColumn
h3cRdRetry = _H3cRdRetry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 9),
    _H3cRdRetry_Type()
)
h3cRdRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdRetry.setStatus("current")
_H3cRdTimeout_Type = Integer32
_H3cRdTimeout_Object = MibTableColumn
h3cRdTimeout = _H3cRdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 10),
    _H3cRdTimeout_Type()
)
h3cRdTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdTimeout.setStatus("current")
_H3cRdPrimAuthIpAddrType_Type = InetAddressType
_H3cRdPrimAuthIpAddrType_Object = MibTableColumn
h3cRdPrimAuthIpAddrType = _H3cRdPrimAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 11),
    _H3cRdPrimAuthIpAddrType_Type()
)
h3cRdPrimAuthIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAuthIpAddrType.setStatus("current")
_H3cRdPrimAuthIpAddr_Type = InetAddress
_H3cRdPrimAuthIpAddr_Object = MibTableColumn
h3cRdPrimAuthIpAddr = _H3cRdPrimAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 12),
    _H3cRdPrimAuthIpAddr_Type()
)
h3cRdPrimAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAuthIpAddr.setStatus("current")
_H3cRdSecAuthIpAddrType_Type = InetAddressType
_H3cRdSecAuthIpAddrType_Object = MibTableColumn
h3cRdSecAuthIpAddrType = _H3cRdSecAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 13),
    _H3cRdSecAuthIpAddrType_Type()
)
h3cRdSecAuthIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAuthIpAddrType.setStatus("current")
_H3cRdSecAuthIpAddr_Type = InetAddress
_H3cRdSecAuthIpAddr_Object = MibTableColumn
h3cRdSecAuthIpAddr = _H3cRdSecAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 14),
    _H3cRdSecAuthIpAddr_Type()
)
h3cRdSecAuthIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAuthIpAddr.setStatus("current")


class _H3cRdServerType_Type(Integer32):
    """Custom type h3cRdServerType based on Integer32"""
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


_H3cRdServerType_Type.__name__ = "Integer32"
_H3cRdServerType_Object = MibTableColumn
h3cRdServerType = _H3cRdServerType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 15),
    _H3cRdServerType_Type()
)
h3cRdServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdServerType.setStatus("current")


class _H3cRdQuietTime_Type(Integer32):
    """Custom type h3cRdQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cRdQuietTime_Type.__name__ = "Integer32"
_H3cRdQuietTime_Object = MibTableColumn
h3cRdQuietTime = _H3cRdQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 16),
    _H3cRdQuietTime_Type()
)
h3cRdQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdQuietTime.setStatus("current")


class _H3cRdUserNameFormat_Type(Integer32):
    """Custom type h3cRdUserNameFormat based on Integer32"""
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


_H3cRdUserNameFormat_Type.__name__ = "Integer32"
_H3cRdUserNameFormat_Object = MibTableColumn
h3cRdUserNameFormat = _H3cRdUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 17),
    _H3cRdUserNameFormat_Type()
)
h3cRdUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdUserNameFormat.setStatus("current")
_H3cRdRowStatus_Type = RowStatus
_H3cRdRowStatus_Object = MibTableColumn
h3cRdRowStatus = _H3cRdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 18),
    _H3cRdRowStatus_Type()
)
h3cRdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdRowStatus.setStatus("current")


class _H3cRdSecKey_Type(DisplayString):
    """Custom type h3cRdSecKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRdSecKey_Type.__name__ = "DisplayString"
_H3cRdSecKey_Object = MibTableColumn
h3cRdSecKey = _H3cRdSecKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 19),
    _H3cRdSecKey_Type()
)
h3cRdSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecKey.setStatus("current")


class _H3cRdPrimVpnName_Type(DisplayString):
    """Custom type h3cRdPrimVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cRdPrimVpnName_Type.__name__ = "DisplayString"
_H3cRdPrimVpnName_Object = MibTableColumn
h3cRdPrimVpnName = _H3cRdPrimVpnName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 20),
    _H3cRdPrimVpnName_Type()
)
h3cRdPrimVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimVpnName.setStatus("current")


class _H3cRdSecVpnName_Type(DisplayString):
    """Custom type h3cRdSecVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cRdSecVpnName_Type.__name__ = "DisplayString"
_H3cRdSecVpnName_Object = MibTableColumn
h3cRdSecVpnName = _H3cRdSecVpnName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 21),
    _H3cRdSecVpnName_Type()
)
h3cRdSecVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecVpnName.setStatus("current")
_H3cRdAuthNasIpAddrType_Type = InetAddressType
_H3cRdAuthNasIpAddrType_Object = MibTableColumn
h3cRdAuthNasIpAddrType = _H3cRdAuthNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 22),
    _H3cRdAuthNasIpAddrType_Type()
)
h3cRdAuthNasIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAuthNasIpAddrType.setStatus("current")
_H3cRdAuthNasIpAddr_Type = InetAddress
_H3cRdAuthNasIpAddr_Object = MibTableColumn
h3cRdAuthNasIpAddr = _H3cRdAuthNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 23),
    _H3cRdAuthNasIpAddr_Type()
)
h3cRdAuthNasIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAuthNasIpAddr.setStatus("current")
_H3cRdAccInfoTable_Object = MibTable
h3cRdAccInfoTable = _H3cRdAccInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2)
)
if mibBuilder.loadTexts:
    h3cRdAccInfoTable.setStatus("current")
_H3cRdAccInfoEntry_Object = MibTableRow
h3cRdAccInfoEntry = _H3cRdAccInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1)
)
h3cRdAccInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdAccGroupName"),
)
if mibBuilder.loadTexts:
    h3cRdAccInfoEntry.setStatus("current")


class _H3cRdAccGroupName_Type(DisplayString):
    """Custom type h3cRdAccGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRdAccGroupName_Type.__name__ = "DisplayString"
_H3cRdAccGroupName_Object = MibTableColumn
h3cRdAccGroupName = _H3cRdAccGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 1),
    _H3cRdAccGroupName_Type()
)
h3cRdAccGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdAccGroupName.setStatus("current")
_H3cRdPrimAccIpAddrType_Type = InetAddressType
_H3cRdPrimAccIpAddrType_Object = MibTableColumn
h3cRdPrimAccIpAddrType = _H3cRdPrimAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 2),
    _H3cRdPrimAccIpAddrType_Type()
)
h3cRdPrimAccIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAccIpAddrType.setStatus("current")
_H3cRdPrimAccIpAddr_Type = InetAddress
_H3cRdPrimAccIpAddr_Object = MibTableColumn
h3cRdPrimAccIpAddr = _H3cRdPrimAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 3),
    _H3cRdPrimAccIpAddr_Type()
)
h3cRdPrimAccIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAccIpAddr.setStatus("current")
_H3cRdPrimAccUdpPort_Type = Integer32
_H3cRdPrimAccUdpPort_Object = MibTableColumn
h3cRdPrimAccUdpPort = _H3cRdPrimAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 4),
    _H3cRdPrimAccUdpPort_Type()
)
h3cRdPrimAccUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAccUdpPort.setStatus("current")


class _H3cRdPrimAccState_Type(Integer32):
    """Custom type h3cRdPrimAccState based on Integer32"""
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


_H3cRdPrimAccState_Type.__name__ = "Integer32"
_H3cRdPrimAccState_Object = MibTableColumn
h3cRdPrimAccState = _H3cRdPrimAccState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 5),
    _H3cRdPrimAccState_Type()
)
h3cRdPrimAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAccState.setStatus("current")
_H3cRdSecAccIpAddrType_Type = InetAddressType
_H3cRdSecAccIpAddrType_Object = MibTableColumn
h3cRdSecAccIpAddrType = _H3cRdSecAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 6),
    _H3cRdSecAccIpAddrType_Type()
)
h3cRdSecAccIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAccIpAddrType.setStatus("current")
_H3cRdSecAccIpAddr_Type = InetAddress
_H3cRdSecAccIpAddr_Object = MibTableColumn
h3cRdSecAccIpAddr = _H3cRdSecAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 7),
    _H3cRdSecAccIpAddr_Type()
)
h3cRdSecAccIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAccIpAddr.setStatus("current")
_H3cRdSecAccUdpPort_Type = Integer32
_H3cRdSecAccUdpPort_Object = MibTableColumn
h3cRdSecAccUdpPort = _H3cRdSecAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 8),
    _H3cRdSecAccUdpPort_Type()
)
h3cRdSecAccUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAccUdpPort.setStatus("current")


class _H3cRdSecAccState_Type(Integer32):
    """Custom type h3cRdSecAccState based on Integer32"""
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


_H3cRdSecAccState_Type.__name__ = "Integer32"
_H3cRdSecAccState_Object = MibTableColumn
h3cRdSecAccState = _H3cRdSecAccState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 9),
    _H3cRdSecAccState_Type()
)
h3cRdSecAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAccState.setStatus("current")


class _H3cRdAccKey_Type(DisplayString):
    """Custom type h3cRdAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRdAccKey_Type.__name__ = "DisplayString"
_H3cRdAccKey_Object = MibTableColumn
h3cRdAccKey = _H3cRdAccKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 10),
    _H3cRdAccKey_Type()
)
h3cRdAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccKey.setStatus("current")
_H3cRdAccRetry_Type = Integer32
_H3cRdAccRetry_Object = MibTableColumn
h3cRdAccRetry = _H3cRdAccRetry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 11),
    _H3cRdAccRetry_Type()
)
h3cRdAccRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccRetry.setStatus("current")
_H3cRdAccTimeout_Type = Integer32
_H3cRdAccTimeout_Object = MibTableColumn
h3cRdAccTimeout = _H3cRdAccTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 12),
    _H3cRdAccTimeout_Type()
)
h3cRdAccTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccTimeout.setStatus("current")


class _H3cRdAccServerType_Type(Integer32):
    """Custom type h3cRdAccServerType based on Integer32"""
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


_H3cRdAccServerType_Type.__name__ = "Integer32"
_H3cRdAccServerType_Object = MibTableColumn
h3cRdAccServerType = _H3cRdAccServerType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 13),
    _H3cRdAccServerType_Type()
)
h3cRdAccServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccServerType.setStatus("current")


class _H3cRdAccQuietTime_Type(Integer32):
    """Custom type h3cRdAccQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cRdAccQuietTime_Type.__name__ = "Integer32"
_H3cRdAccQuietTime_Object = MibTableColumn
h3cRdAccQuietTime = _H3cRdAccQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 14),
    _H3cRdAccQuietTime_Type()
)
h3cRdAccQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccQuietTime.setStatus("current")


class _H3cRdAccFailureAction_Type(Integer32):
    """Custom type h3cRdAccFailureAction based on Integer32"""
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


_H3cRdAccFailureAction_Type.__name__ = "Integer32"
_H3cRdAccFailureAction_Object = MibTableColumn
h3cRdAccFailureAction = _H3cRdAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 15),
    _H3cRdAccFailureAction_Type()
)
h3cRdAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccFailureAction.setStatus("current")


class _H3cRdAccRealTime_Type(Integer32):
    """Custom type h3cRdAccRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_H3cRdAccRealTime_Type.__name__ = "Integer32"
_H3cRdAccRealTime_Object = MibTableColumn
h3cRdAccRealTime = _H3cRdAccRealTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 16),
    _H3cRdAccRealTime_Type()
)
h3cRdAccRealTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccRealTime.setStatus("current")


class _H3cRdAccRealTimeRetry_Type(Integer32):
    """Custom type h3cRdAccRealTimeRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cRdAccRealTimeRetry_Type.__name__ = "Integer32"
_H3cRdAccRealTimeRetry_Object = MibTableColumn
h3cRdAccRealTimeRetry = _H3cRdAccRealTimeRetry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 17),
    _H3cRdAccRealTimeRetry_Type()
)
h3cRdAccRealTimeRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccRealTimeRetry.setStatus("current")
_H3cRdAccSaveStopPktEnable_Type = TruthValue
_H3cRdAccSaveStopPktEnable_Object = MibTableColumn
h3cRdAccSaveStopPktEnable = _H3cRdAccSaveStopPktEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 18),
    _H3cRdAccSaveStopPktEnable_Type()
)
h3cRdAccSaveStopPktEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccSaveStopPktEnable.setStatus("current")


class _H3cRdAccStopRetry_Type(Integer32):
    """Custom type h3cRdAccStopRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_H3cRdAccStopRetry_Type.__name__ = "Integer32"
_H3cRdAccStopRetry_Object = MibTableColumn
h3cRdAccStopRetry = _H3cRdAccStopRetry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 19),
    _H3cRdAccStopRetry_Type()
)
h3cRdAccStopRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccStopRetry.setStatus("current")


class _H3cRdAccDataFlowUnit_Type(Integer32):
    """Custom type h3cRdAccDataFlowUnit based on Integer32"""
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


_H3cRdAccDataFlowUnit_Type.__name__ = "Integer32"
_H3cRdAccDataFlowUnit_Object = MibTableColumn
h3cRdAccDataFlowUnit = _H3cRdAccDataFlowUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 20),
    _H3cRdAccDataFlowUnit_Type()
)
h3cRdAccDataFlowUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccDataFlowUnit.setStatus("current")


class _H3cRdAccPacketUnit_Type(Integer32):
    """Custom type h3cRdAccPacketUnit based on Integer32"""
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


_H3cRdAccPacketUnit_Type.__name__ = "Integer32"
_H3cRdAccPacketUnit_Object = MibTableColumn
h3cRdAccPacketUnit = _H3cRdAccPacketUnit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 21),
    _H3cRdAccPacketUnit_Type()
)
h3cRdAccPacketUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccPacketUnit.setStatus("current")
_H3cRdAccRowStatus_Type = RowStatus
_H3cRdAccRowStatus_Object = MibTableColumn
h3cRdAccRowStatus = _H3cRdAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 22),
    _H3cRdAccRowStatus_Type()
)
h3cRdAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccRowStatus.setStatus("current")
_H3cRdAcctOnEnable_Type = TruthValue
_H3cRdAcctOnEnable_Object = MibTableColumn
h3cRdAcctOnEnable = _H3cRdAcctOnEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 23),
    _H3cRdAcctOnEnable_Type()
)
h3cRdAcctOnEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAcctOnEnable.setStatus("current")


class _H3cRdAcctOnSendTimes_Type(Integer32):
    """Custom type h3cRdAcctOnSendTimes based on Integer32"""
    defaultValue = 15


_H3cRdAcctOnSendTimes_Object = MibTableColumn
h3cRdAcctOnSendTimes = _H3cRdAcctOnSendTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 24),
    _H3cRdAcctOnSendTimes_Type()
)
h3cRdAcctOnSendTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAcctOnSendTimes.setStatus("current")


class _H3cRdAcctOnSendInterval_Type(Integer32):
    """Custom type h3cRdAcctOnSendInterval based on Integer32"""
    defaultValue = 3


_H3cRdAcctOnSendInterval_Object = MibTableColumn
h3cRdAcctOnSendInterval = _H3cRdAcctOnSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 25),
    _H3cRdAcctOnSendInterval_Type()
)
h3cRdAcctOnSendInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAcctOnSendInterval.setStatus("current")


class _H3cRdSecAccKey_Type(DisplayString):
    """Custom type h3cRdSecAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRdSecAccKey_Type.__name__ = "DisplayString"
_H3cRdSecAccKey_Object = MibTableColumn
h3cRdSecAccKey = _H3cRdSecAccKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 26),
    _H3cRdSecAccKey_Type()
)
h3cRdSecAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAccKey.setStatus("current")


class _H3cRdPrimAccVpnName_Type(DisplayString):
    """Custom type h3cRdPrimAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cRdPrimAccVpnName_Type.__name__ = "DisplayString"
_H3cRdPrimAccVpnName_Object = MibTableColumn
h3cRdPrimAccVpnName = _H3cRdPrimAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 27),
    _H3cRdPrimAccVpnName_Type()
)
h3cRdPrimAccVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdPrimAccVpnName.setStatus("current")


class _H3cRdSecAccVpnName_Type(DisplayString):
    """Custom type h3cRdSecAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cRdSecAccVpnName_Type.__name__ = "DisplayString"
_H3cRdSecAccVpnName_Object = MibTableColumn
h3cRdSecAccVpnName = _H3cRdSecAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 28),
    _H3cRdSecAccVpnName_Type()
)
h3cRdSecAccVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecAccVpnName.setStatus("current")
_H3cRdAccNasIpAddrType_Type = InetAddressType
_H3cRdAccNasIpAddrType_Object = MibTableColumn
h3cRdAccNasIpAddrType = _H3cRdAccNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 29),
    _H3cRdAccNasIpAddrType_Type()
)
h3cRdAccNasIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccNasIpAddrType.setStatus("current")
_H3cRdAccNasIpAddr_Type = InetAddress
_H3cRdAccNasIpAddr_Object = MibTableColumn
h3cRdAccNasIpAddr = _H3cRdAccNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 30),
    _H3cRdAccNasIpAddr_Type()
)
h3cRdAccNasIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdAccNasIpAddr.setStatus("current")
_H3cRadiusGlobalConfig_ObjectIdentity = ObjectIdentity
h3cRadiusGlobalConfig = _H3cRadiusGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 3)
)


class _H3cRadiusAuthErrThreshold_Type(Unsigned32):
    """Custom type h3cRadiusAuthErrThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cRadiusAuthErrThreshold_Type.__name__ = "Unsigned32"
_H3cRadiusAuthErrThreshold_Object = MibScalar
h3cRadiusAuthErrThreshold = _H3cRadiusAuthErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 3, 1),
    _H3cRadiusAuthErrThreshold_Type()
)
h3cRadiusAuthErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRadiusAuthErrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cRadiusAuthErrThreshold.setUnits("percentage")
_H3cRdSecondaryAuthServerTable_Object = MibTable
h3cRdSecondaryAuthServerTable = _H3cRdSecondaryAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4)
)
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthServerTable.setStatus("current")
_H3cRdSecondaryAuthServerEntry_Object = MibTableRow
h3cRdSecondaryAuthServerEntry = _H3cRdSecondaryAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1)
)
h3cRdSecondaryAuthServerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdGroupName"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthIpAddrType"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthIpAddr"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthVpnName"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthUdpPort"),
)
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthServerEntry.setStatus("current")
_H3cRdSecondaryAuthIpAddrType_Type = InetAddressType
_H3cRdSecondaryAuthIpAddrType_Object = MibTableColumn
h3cRdSecondaryAuthIpAddrType = _H3cRdSecondaryAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 1),
    _H3cRdSecondaryAuthIpAddrType_Type()
)
h3cRdSecondaryAuthIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthIpAddrType.setStatus("current")
_H3cRdSecondaryAuthIpAddr_Type = InetAddress
_H3cRdSecondaryAuthIpAddr_Object = MibTableColumn
h3cRdSecondaryAuthIpAddr = _H3cRdSecondaryAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 2),
    _H3cRdSecondaryAuthIpAddr_Type()
)
h3cRdSecondaryAuthIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthIpAddr.setStatus("current")


class _H3cRdSecondaryAuthVpnName_Type(DisplayString):
    """Custom type h3cRdSecondaryAuthVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cRdSecondaryAuthVpnName_Type.__name__ = "DisplayString"
_H3cRdSecondaryAuthVpnName_Object = MibTableColumn
h3cRdSecondaryAuthVpnName = _H3cRdSecondaryAuthVpnName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 3),
    _H3cRdSecondaryAuthVpnName_Type()
)
h3cRdSecondaryAuthVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthVpnName.setStatus("current")


class _H3cRdSecondaryAuthUdpPort_Type(Integer32):
    """Custom type h3cRdSecondaryAuthUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cRdSecondaryAuthUdpPort_Type.__name__ = "Integer32"
_H3cRdSecondaryAuthUdpPort_Object = MibTableColumn
h3cRdSecondaryAuthUdpPort = _H3cRdSecondaryAuthUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 4),
    _H3cRdSecondaryAuthUdpPort_Type()
)
h3cRdSecondaryAuthUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthUdpPort.setStatus("current")


class _H3cRdSecondaryAuthState_Type(Integer32):
    """Custom type h3cRdSecondaryAuthState based on Integer32"""
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


_H3cRdSecondaryAuthState_Type.__name__ = "Integer32"
_H3cRdSecondaryAuthState_Object = MibTableColumn
h3cRdSecondaryAuthState = _H3cRdSecondaryAuthState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 5),
    _H3cRdSecondaryAuthState_Type()
)
h3cRdSecondaryAuthState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthState.setStatus("current")


class _H3cRdSecondaryAuthKey_Type(DisplayString):
    """Custom type h3cRdSecondaryAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRdSecondaryAuthKey_Type.__name__ = "DisplayString"
_H3cRdSecondaryAuthKey_Object = MibTableColumn
h3cRdSecondaryAuthKey = _H3cRdSecondaryAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 6),
    _H3cRdSecondaryAuthKey_Type()
)
h3cRdSecondaryAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthKey.setStatus("current")
_H3cRdSecondaryAuthRowStatus_Type = RowStatus
_H3cRdSecondaryAuthRowStatus_Object = MibTableColumn
h3cRdSecondaryAuthRowStatus = _H3cRdSecondaryAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 7),
    _H3cRdSecondaryAuthRowStatus_Type()
)
h3cRdSecondaryAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecondaryAuthRowStatus.setStatus("current")
_H3cRdSecondaryAccServerTable_Object = MibTable
h3cRdSecondaryAccServerTable = _H3cRdSecondaryAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5)
)
if mibBuilder.loadTexts:
    h3cRdSecondaryAccServerTable.setStatus("current")
_H3cRdSecondaryAccServerEntry_Object = MibTableRow
h3cRdSecondaryAccServerEntry = _H3cRdSecondaryAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1)
)
h3cRdSecondaryAccServerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdAccGroupName"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccIpAddrType"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccIpAddr"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccVpnName"),
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccUdpPort"),
)
if mibBuilder.loadTexts:
    h3cRdSecondaryAccServerEntry.setStatus("current")
_H3cRdSecondaryAccIpAddrType_Type = InetAddressType
_H3cRdSecondaryAccIpAddrType_Object = MibTableColumn
h3cRdSecondaryAccIpAddrType = _H3cRdSecondaryAccIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 1),
    _H3cRdSecondaryAccIpAddrType_Type()
)
h3cRdSecondaryAccIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccIpAddrType.setStatus("current")
_H3cRdSecondaryAccIpAddr_Type = InetAddress
_H3cRdSecondaryAccIpAddr_Object = MibTableColumn
h3cRdSecondaryAccIpAddr = _H3cRdSecondaryAccIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 2),
    _H3cRdSecondaryAccIpAddr_Type()
)
h3cRdSecondaryAccIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccIpAddr.setStatus("current")


class _H3cRdSecondaryAccVpnName_Type(DisplayString):
    """Custom type h3cRdSecondaryAccVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cRdSecondaryAccVpnName_Type.__name__ = "DisplayString"
_H3cRdSecondaryAccVpnName_Object = MibTableColumn
h3cRdSecondaryAccVpnName = _H3cRdSecondaryAccVpnName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 3),
    _H3cRdSecondaryAccVpnName_Type()
)
h3cRdSecondaryAccVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccVpnName.setStatus("current")


class _H3cRdSecondaryAccUdpPort_Type(Integer32):
    """Custom type h3cRdSecondaryAccUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cRdSecondaryAccUdpPort_Type.__name__ = "Integer32"
_H3cRdSecondaryAccUdpPort_Object = MibTableColumn
h3cRdSecondaryAccUdpPort = _H3cRdSecondaryAccUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 4),
    _H3cRdSecondaryAccUdpPort_Type()
)
h3cRdSecondaryAccUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccUdpPort.setStatus("current")


class _H3cRdSecondaryAccState_Type(Integer32):
    """Custom type h3cRdSecondaryAccState based on Integer32"""
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


_H3cRdSecondaryAccState_Type.__name__ = "Integer32"
_H3cRdSecondaryAccState_Object = MibTableColumn
h3cRdSecondaryAccState = _H3cRdSecondaryAccState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 5),
    _H3cRdSecondaryAccState_Type()
)
h3cRdSecondaryAccState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccState.setStatus("current")


class _H3cRdSecondaryAccKey_Type(DisplayString):
    """Custom type h3cRdSecondaryAccKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cRdSecondaryAccKey_Type.__name__ = "DisplayString"
_H3cRdSecondaryAccKey_Object = MibTableColumn
h3cRdSecondaryAccKey = _H3cRdSecondaryAccKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 6),
    _H3cRdSecondaryAccKey_Type()
)
h3cRdSecondaryAccKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccKey.setStatus("current")
_H3cRdSecondaryAccRowStatus_Type = RowStatus
_H3cRdSecondaryAccRowStatus_Object = MibTableColumn
h3cRdSecondaryAccRowStatus = _H3cRdSecondaryAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 7),
    _H3cRdSecondaryAccRowStatus_Type()
)
h3cRdSecondaryAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRdSecondaryAccRowStatus.setStatus("current")
_H3cRadiusAccounting_ObjectIdentity = ObjectIdentity
h3cRadiusAccounting = _H3cRadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2)
)
_H3cRadiusAccClient_ObjectIdentity = ObjectIdentity
h3cRadiusAccClient = _H3cRadiusAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1)
)
_H3cRadiusAccServerTable_Object = MibTable
h3cRadiusAccServerTable = _H3cRadiusAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRadiusAccServerTable.setStatus("current")
_H3cRadiusAccServerEntry_Object = MibTableRow
h3cRadiusAccServerEntry = _H3cRadiusAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1)
)
h3cRadiusAccServerEntry.setIndexNames(
    (0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    h3cRadiusAccServerEntry.setStatus("current")
_H3cRadiusAccClientStartRequests_Type = Counter32
_H3cRadiusAccClientStartRequests_Object = MibTableColumn
h3cRadiusAccClientStartRequests = _H3cRadiusAccClientStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 1),
    _H3cRadiusAccClientStartRequests_Type()
)
h3cRadiusAccClientStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAccClientStartRequests.setStatus("current")
_H3cRadiusAccClientStartResponses_Type = Counter32
_H3cRadiusAccClientStartResponses_Object = MibTableColumn
h3cRadiusAccClientStartResponses = _H3cRadiusAccClientStartResponses_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 2),
    _H3cRadiusAccClientStartResponses_Type()
)
h3cRadiusAccClientStartResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAccClientStartResponses.setStatus("current")
_H3cRadiusAccClientInterimRequests_Type = Counter32
_H3cRadiusAccClientInterimRequests_Object = MibTableColumn
h3cRadiusAccClientInterimRequests = _H3cRadiusAccClientInterimRequests_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 3),
    _H3cRadiusAccClientInterimRequests_Type()
)
h3cRadiusAccClientInterimRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAccClientInterimRequests.setStatus("current")
_H3cRadiusAccClientInterimResponses_Type = Counter32
_H3cRadiusAccClientInterimResponses_Object = MibTableColumn
h3cRadiusAccClientInterimResponses = _H3cRadiusAccClientInterimResponses_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 4),
    _H3cRadiusAccClientInterimResponses_Type()
)
h3cRadiusAccClientInterimResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAccClientInterimResponses.setStatus("current")
_H3cRadiusAccClientStopRequests_Type = Counter32
_H3cRadiusAccClientStopRequests_Object = MibTableColumn
h3cRadiusAccClientStopRequests = _H3cRadiusAccClientStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 5),
    _H3cRadiusAccClientStopRequests_Type()
)
h3cRadiusAccClientStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAccClientStopRequests.setStatus("current")
_H3cRadiusAccClientStopResponses_Type = Counter32
_H3cRadiusAccClientStopResponses_Object = MibTableColumn
h3cRadiusAccClientStopResponses = _H3cRadiusAccClientStopResponses_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 6),
    _H3cRadiusAccClientStopResponses_Type()
)
h3cRadiusAccClientStopResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAccClientStopResponses.setStatus("current")
_H3cRadiusServerTrap_ObjectIdentity = ObjectIdentity
h3cRadiusServerTrap = _H3cRadiusServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3)
)
_H3cRadiusServerTrapPrefix_ObjectIdentity = ObjectIdentity
h3cRadiusServerTrapPrefix = _H3cRadiusServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0)
)
_H3cRadiusAuthenticating_ObjectIdentity = ObjectIdentity
h3cRadiusAuthenticating = _H3cRadiusAuthenticating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4)
)
_H3cRadiusAuthClient_ObjectIdentity = ObjectIdentity
h3cRadiusAuthClient = _H3cRadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1)
)
_H3cRadiusAuthServerTable_Object = MibTable
h3cRadiusAuthServerTable = _H3cRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRadiusAuthServerTable.setStatus("current")
_H3cRadiusAuthServerEntry_Object = MibTableRow
h3cRadiusAuthServerEntry = _H3cRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1)
)
h3cRadiusAuthServerEntry.setIndexNames(
    (0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    h3cRadiusAuthServerEntry.setStatus("current")
_H3cRadiusAuthFailureTimes_Type = Counter32
_H3cRadiusAuthFailureTimes_Object = MibTableColumn
h3cRadiusAuthFailureTimes = _H3cRadiusAuthFailureTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1, 1),
    _H3cRadiusAuthFailureTimes_Type()
)
h3cRadiusAuthFailureTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAuthFailureTimes.setStatus("current")
_H3cRadiusAuthTimeoutTimes_Type = Counter32
_H3cRadiusAuthTimeoutTimes_Object = MibTableColumn
h3cRadiusAuthTimeoutTimes = _H3cRadiusAuthTimeoutTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1, 2),
    _H3cRadiusAuthTimeoutTimes_Type()
)
h3cRadiusAuthTimeoutTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAuthTimeoutTimes.setStatus("current")
_H3cRadiusAuthRejectTimes_Type = Counter32
_H3cRadiusAuthRejectTimes_Object = MibTableColumn
h3cRadiusAuthRejectTimes = _H3cRadiusAuthRejectTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1, 3),
    _H3cRadiusAuthRejectTimes_Type()
)
h3cRadiusAuthRejectTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusAuthRejectTimes.setStatus("current")
_H3cRadiusExtend_ObjectIdentity = ObjectIdentity
h3cRadiusExtend = _H3cRadiusExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5)
)
_H3cRadiusExtendObjects_ObjectIdentity = ObjectIdentity
h3cRadiusExtendObjects = _H3cRadiusExtendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 1)
)
_H3cRadiusExtendTables_ObjectIdentity = ObjectIdentity
h3cRadiusExtendTables = _H3cRadiusExtendTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2)
)
_H3cRadiusSchAuthTable_Object = MibTable
h3cRadiusSchAuthTable = _H3cRadiusSchAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1)
)
if mibBuilder.loadTexts:
    h3cRadiusSchAuthTable.setStatus("current")
_H3cRadiusSchAuthEntry_Object = MibTableRow
h3cRadiusSchAuthEntry = _H3cRadiusSchAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1)
)
h3cRadiusSchAuthEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusSchAuthGroupName"),
)
if mibBuilder.loadTexts:
    h3cRadiusSchAuthEntry.setStatus("current")
_H3cRadiusSchAuthGroupName_Type = DisplayString
_H3cRadiusSchAuthGroupName_Object = MibTableColumn
h3cRadiusSchAuthGroupName = _H3cRadiusSchAuthGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 1),
    _H3cRadiusSchAuthGroupName_Type()
)
h3cRadiusSchAuthGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthGroupName.setStatus("current")
_H3cRadiusSchAuthPrimIpAddr_Type = IpAddress
_H3cRadiusSchAuthPrimIpAddr_Object = MibTableColumn
h3cRadiusSchAuthPrimIpAddr = _H3cRadiusSchAuthPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 2),
    _H3cRadiusSchAuthPrimIpAddr_Type()
)
h3cRadiusSchAuthPrimIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthPrimIpAddr.setStatus("current")


class _H3cRadiusSchAuthPrimUdpPort_Type(Integer32):
    """Custom type h3cRadiusSchAuthPrimUdpPort based on Integer32"""
    defaultValue = 1812


_H3cRadiusSchAuthPrimUdpPort_Object = MibTableColumn
h3cRadiusSchAuthPrimUdpPort = _H3cRadiusSchAuthPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 3),
    _H3cRadiusSchAuthPrimUdpPort_Type()
)
h3cRadiusSchAuthPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthPrimUdpPort.setStatus("current")
_H3cRadiusSchAuthPrimKey_Type = DisplayString
_H3cRadiusSchAuthPrimKey_Object = MibTableColumn
h3cRadiusSchAuthPrimKey = _H3cRadiusSchAuthPrimKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 4),
    _H3cRadiusSchAuthPrimKey_Type()
)
h3cRadiusSchAuthPrimKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthPrimKey.setStatus("current")
_H3cRadiusSchAuthSecIpAddr_Type = IpAddress
_H3cRadiusSchAuthSecIpAddr_Object = MibTableColumn
h3cRadiusSchAuthSecIpAddr = _H3cRadiusSchAuthSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 5),
    _H3cRadiusSchAuthSecIpAddr_Type()
)
h3cRadiusSchAuthSecIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthSecIpAddr.setStatus("current")


class _H3cRadiusSchAuthSecUdpPort_Type(Integer32):
    """Custom type h3cRadiusSchAuthSecUdpPort based on Integer32"""
    defaultValue = 1812


_H3cRadiusSchAuthSecUdpPort_Object = MibTableColumn
h3cRadiusSchAuthSecUdpPort = _H3cRadiusSchAuthSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 6),
    _H3cRadiusSchAuthSecUdpPort_Type()
)
h3cRadiusSchAuthSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthSecUdpPort.setStatus("current")
_H3cRadiusSchAuthSecKey_Type = DisplayString
_H3cRadiusSchAuthSecKey_Object = MibTableColumn
h3cRadiusSchAuthSecKey = _H3cRadiusSchAuthSecKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 7),
    _H3cRadiusSchAuthSecKey_Type()
)
h3cRadiusSchAuthSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthSecKey.setStatus("current")
_H3cRadiusSchAuthRowStatus_Type = RowStatus
_H3cRadiusSchAuthRowStatus_Object = MibTableColumn
h3cRadiusSchAuthRowStatus = _H3cRadiusSchAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 8),
    _H3cRadiusSchAuthRowStatus_Type()
)
h3cRadiusSchAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAuthRowStatus.setStatus("current")
_H3cRadiusSchAccTable_Object = MibTable
h3cRadiusSchAccTable = _H3cRadiusSchAccTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRadiusSchAccTable.setStatus("current")
_H3cRadiusSchAccEntry_Object = MibTableRow
h3cRadiusSchAccEntry = _H3cRadiusSchAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1)
)
h3cRadiusSchAccEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusSchAccGroupName"),
)
if mibBuilder.loadTexts:
    h3cRadiusSchAccEntry.setStatus("current")
_H3cRadiusSchAccGroupName_Type = DisplayString
_H3cRadiusSchAccGroupName_Object = MibTableColumn
h3cRadiusSchAccGroupName = _H3cRadiusSchAccGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 1),
    _H3cRadiusSchAccGroupName_Type()
)
h3cRadiusSchAccGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRadiusSchAccGroupName.setStatus("current")
_H3cRadiusSchAccPrimIpAddr_Type = IpAddress
_H3cRadiusSchAccPrimIpAddr_Object = MibTableColumn
h3cRadiusSchAccPrimIpAddr = _H3cRadiusSchAccPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 2),
    _H3cRadiusSchAccPrimIpAddr_Type()
)
h3cRadiusSchAccPrimIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccPrimIpAddr.setStatus("current")


class _H3cRadiusSchAccPrimUdpPort_Type(Integer32):
    """Custom type h3cRadiusSchAccPrimUdpPort based on Integer32"""
    defaultValue = 1812


_H3cRadiusSchAccPrimUdpPort_Object = MibTableColumn
h3cRadiusSchAccPrimUdpPort = _H3cRadiusSchAccPrimUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 3),
    _H3cRadiusSchAccPrimUdpPort_Type()
)
h3cRadiusSchAccPrimUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccPrimUdpPort.setStatus("current")
_H3cRadiusSchAccPrimKey_Type = DisplayString
_H3cRadiusSchAccPrimKey_Object = MibTableColumn
h3cRadiusSchAccPrimKey = _H3cRadiusSchAccPrimKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 4),
    _H3cRadiusSchAccPrimKey_Type()
)
h3cRadiusSchAccPrimKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccPrimKey.setStatus("current")
_H3cRadiusSchAccSecIpAddr_Type = IpAddress
_H3cRadiusSchAccSecIpAddr_Object = MibTableColumn
h3cRadiusSchAccSecIpAddr = _H3cRadiusSchAccSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 5),
    _H3cRadiusSchAccSecIpAddr_Type()
)
h3cRadiusSchAccSecIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccSecIpAddr.setStatus("current")


class _H3cRadiusSchAccSecUdpPort_Type(Integer32):
    """Custom type h3cRadiusSchAccSecUdpPort based on Integer32"""
    defaultValue = 1812


_H3cRadiusSchAccSecUdpPort_Object = MibTableColumn
h3cRadiusSchAccSecUdpPort = _H3cRadiusSchAccSecUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 6),
    _H3cRadiusSchAccSecUdpPort_Type()
)
h3cRadiusSchAccSecUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccSecUdpPort.setStatus("current")
_H3cRadiusSchAccSecKey_Type = DisplayString
_H3cRadiusSchAccSecKey_Object = MibTableColumn
h3cRadiusSchAccSecKey = _H3cRadiusSchAccSecKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 7),
    _H3cRadiusSchAccSecKey_Type()
)
h3cRadiusSchAccSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccSecKey.setStatus("current")
_H3cRadiusSchAccRowStatus_Type = RowStatus
_H3cRadiusSchAccRowStatus_Object = MibTableColumn
h3cRadiusSchAccRowStatus = _H3cRadiusSchAccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 8),
    _H3cRadiusSchAccRowStatus_Type()
)
h3cRadiusSchAccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRadiusSchAccRowStatus.setStatus("current")
_H3cRadiusExtendTraps_ObjectIdentity = ObjectIdentity
h3cRadiusExtendTraps = _H3cRadiusExtendTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 3)
)
_H3cRadiusStatistic_ObjectIdentity = ObjectIdentity
h3cRadiusStatistic = _H3cRadiusStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6)
)
_H3cRadiusStatAccReq_Type = Counter64
_H3cRadiusStatAccReq_Object = MibScalar
h3cRadiusStatAccReq = _H3cRadiusStatAccReq_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 1),
    _H3cRadiusStatAccReq_Type()
)
h3cRadiusStatAccReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusStatAccReq.setStatus("current")
_H3cRadiusStatAccAck_Type = Counter64
_H3cRadiusStatAccAck_Object = MibScalar
h3cRadiusStatAccAck = _H3cRadiusStatAccAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 2),
    _H3cRadiusStatAccAck_Type()
)
h3cRadiusStatAccAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusStatAccAck.setStatus("current")
_H3cRadiusStatLogoutReq_Type = Counter64
_H3cRadiusStatLogoutReq_Object = MibScalar
h3cRadiusStatLogoutReq = _H3cRadiusStatLogoutReq_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 3),
    _H3cRadiusStatLogoutReq_Type()
)
h3cRadiusStatLogoutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusStatLogoutReq.setStatus("current")
_H3cRadiusStatLogoutAck_Type = Counter64
_H3cRadiusStatLogoutAck_Object = MibScalar
h3cRadiusStatLogoutAck = _H3cRadiusStatLogoutAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 4),
    _H3cRadiusStatLogoutAck_Type()
)
h3cRadiusStatLogoutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRadiusStatLogoutAck.setStatus("current")
_H3cRadiusServerTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cRadiusServerTrapVarObjects = _H3cRadiusServerTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 7)
)
_H3cRadiusServerFirstTrapTime_Type = TimeTicks
_H3cRadiusServerFirstTrapTime_Object = MibScalar
h3cRadiusServerFirstTrapTime = _H3cRadiusServerFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 7, 1),
    _H3cRadiusServerFirstTrapTime_Type()
)
h3cRadiusServerFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRadiusServerFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

h3cRadiusAuthServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0, 1)
)
h3cRadiusAuthServerUpTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cRadiusAuthServerUpTrap.setStatus(
        "current"
    )

h3cRadiusAccServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0, 2)
)
h3cRadiusAccServerUpTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cRadiusAccServerUpTrap.setStatus(
        "current"
    )

h3cRadiusAuthErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0, 3)
)
h3cRadiusAuthErrTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    h3cRadiusAuthErrTrap.setStatus(
        "current"
    )

h3cRadiusAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 1)
)
h3cRadiusAuthServerDownTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cRadiusAuthServerDownTrap.setStatus(
        "current"
    )

h3cRadiusAccServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 2)
)
h3cRadiusAccServerDownTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cRadiusAccServerDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-RADIUS-MIB",
    **{"DisplayString": DisplayString,
       "h3cRadius": h3cRadius,
       "h3cRdObjects": h3cRdObjects,
       "h3cRdInfoTable": h3cRdInfoTable,
       "h3cRdInfoEntry": h3cRdInfoEntry,
       "h3cRdGroupName": h3cRdGroupName,
       "h3cRdPrimAuthIp": h3cRdPrimAuthIp,
       "h3cRdPrimUdpPort": h3cRdPrimUdpPort,
       "h3cRdPrimState": h3cRdPrimState,
       "h3cRdSecAuthIp": h3cRdSecAuthIp,
       "h3cRdSecUdpPort": h3cRdSecUdpPort,
       "h3cRdSecState": h3cRdSecState,
       "h3cRdKey": h3cRdKey,
       "h3cRdRetry": h3cRdRetry,
       "h3cRdTimeout": h3cRdTimeout,
       "h3cRdPrimAuthIpAddrType": h3cRdPrimAuthIpAddrType,
       "h3cRdPrimAuthIpAddr": h3cRdPrimAuthIpAddr,
       "h3cRdSecAuthIpAddrType": h3cRdSecAuthIpAddrType,
       "h3cRdSecAuthIpAddr": h3cRdSecAuthIpAddr,
       "h3cRdServerType": h3cRdServerType,
       "h3cRdQuietTime": h3cRdQuietTime,
       "h3cRdUserNameFormat": h3cRdUserNameFormat,
       "h3cRdRowStatus": h3cRdRowStatus,
       "h3cRdSecKey": h3cRdSecKey,
       "h3cRdPrimVpnName": h3cRdPrimVpnName,
       "h3cRdSecVpnName": h3cRdSecVpnName,
       "h3cRdAuthNasIpAddrType": h3cRdAuthNasIpAddrType,
       "h3cRdAuthNasIpAddr": h3cRdAuthNasIpAddr,
       "h3cRdAccInfoTable": h3cRdAccInfoTable,
       "h3cRdAccInfoEntry": h3cRdAccInfoEntry,
       "h3cRdAccGroupName": h3cRdAccGroupName,
       "h3cRdPrimAccIpAddrType": h3cRdPrimAccIpAddrType,
       "h3cRdPrimAccIpAddr": h3cRdPrimAccIpAddr,
       "h3cRdPrimAccUdpPort": h3cRdPrimAccUdpPort,
       "h3cRdPrimAccState": h3cRdPrimAccState,
       "h3cRdSecAccIpAddrType": h3cRdSecAccIpAddrType,
       "h3cRdSecAccIpAddr": h3cRdSecAccIpAddr,
       "h3cRdSecAccUdpPort": h3cRdSecAccUdpPort,
       "h3cRdSecAccState": h3cRdSecAccState,
       "h3cRdAccKey": h3cRdAccKey,
       "h3cRdAccRetry": h3cRdAccRetry,
       "h3cRdAccTimeout": h3cRdAccTimeout,
       "h3cRdAccServerType": h3cRdAccServerType,
       "h3cRdAccQuietTime": h3cRdAccQuietTime,
       "h3cRdAccFailureAction": h3cRdAccFailureAction,
       "h3cRdAccRealTime": h3cRdAccRealTime,
       "h3cRdAccRealTimeRetry": h3cRdAccRealTimeRetry,
       "h3cRdAccSaveStopPktEnable": h3cRdAccSaveStopPktEnable,
       "h3cRdAccStopRetry": h3cRdAccStopRetry,
       "h3cRdAccDataFlowUnit": h3cRdAccDataFlowUnit,
       "h3cRdAccPacketUnit": h3cRdAccPacketUnit,
       "h3cRdAccRowStatus": h3cRdAccRowStatus,
       "h3cRdAcctOnEnable": h3cRdAcctOnEnable,
       "h3cRdAcctOnSendTimes": h3cRdAcctOnSendTimes,
       "h3cRdAcctOnSendInterval": h3cRdAcctOnSendInterval,
       "h3cRdSecAccKey": h3cRdSecAccKey,
       "h3cRdPrimAccVpnName": h3cRdPrimAccVpnName,
       "h3cRdSecAccVpnName": h3cRdSecAccVpnName,
       "h3cRdAccNasIpAddrType": h3cRdAccNasIpAddrType,
       "h3cRdAccNasIpAddr": h3cRdAccNasIpAddr,
       "h3cRadiusGlobalConfig": h3cRadiusGlobalConfig,
       "h3cRadiusAuthErrThreshold": h3cRadiusAuthErrThreshold,
       "h3cRdSecondaryAuthServerTable": h3cRdSecondaryAuthServerTable,
       "h3cRdSecondaryAuthServerEntry": h3cRdSecondaryAuthServerEntry,
       "h3cRdSecondaryAuthIpAddrType": h3cRdSecondaryAuthIpAddrType,
       "h3cRdSecondaryAuthIpAddr": h3cRdSecondaryAuthIpAddr,
       "h3cRdSecondaryAuthVpnName": h3cRdSecondaryAuthVpnName,
       "h3cRdSecondaryAuthUdpPort": h3cRdSecondaryAuthUdpPort,
       "h3cRdSecondaryAuthState": h3cRdSecondaryAuthState,
       "h3cRdSecondaryAuthKey": h3cRdSecondaryAuthKey,
       "h3cRdSecondaryAuthRowStatus": h3cRdSecondaryAuthRowStatus,
       "h3cRdSecondaryAccServerTable": h3cRdSecondaryAccServerTable,
       "h3cRdSecondaryAccServerEntry": h3cRdSecondaryAccServerEntry,
       "h3cRdSecondaryAccIpAddrType": h3cRdSecondaryAccIpAddrType,
       "h3cRdSecondaryAccIpAddr": h3cRdSecondaryAccIpAddr,
       "h3cRdSecondaryAccVpnName": h3cRdSecondaryAccVpnName,
       "h3cRdSecondaryAccUdpPort": h3cRdSecondaryAccUdpPort,
       "h3cRdSecondaryAccState": h3cRdSecondaryAccState,
       "h3cRdSecondaryAccKey": h3cRdSecondaryAccKey,
       "h3cRdSecondaryAccRowStatus": h3cRdSecondaryAccRowStatus,
       "h3cRadiusAccounting": h3cRadiusAccounting,
       "h3cRadiusAccClient": h3cRadiusAccClient,
       "h3cRadiusAccServerTable": h3cRadiusAccServerTable,
       "h3cRadiusAccServerEntry": h3cRadiusAccServerEntry,
       "h3cRadiusAccClientStartRequests": h3cRadiusAccClientStartRequests,
       "h3cRadiusAccClientStartResponses": h3cRadiusAccClientStartResponses,
       "h3cRadiusAccClientInterimRequests": h3cRadiusAccClientInterimRequests,
       "h3cRadiusAccClientInterimResponses": h3cRadiusAccClientInterimResponses,
       "h3cRadiusAccClientStopRequests": h3cRadiusAccClientStopRequests,
       "h3cRadiusAccClientStopResponses": h3cRadiusAccClientStopResponses,
       "h3cRadiusServerTrap": h3cRadiusServerTrap,
       "h3cRadiusServerTrapPrefix": h3cRadiusServerTrapPrefix,
       "h3cRadiusAuthServerUpTrap": h3cRadiusAuthServerUpTrap,
       "h3cRadiusAccServerUpTrap": h3cRadiusAccServerUpTrap,
       "h3cRadiusAuthErrTrap": h3cRadiusAuthErrTrap,
       "h3cRadiusAuthServerDownTrap": h3cRadiusAuthServerDownTrap,
       "h3cRadiusAccServerDownTrap": h3cRadiusAccServerDownTrap,
       "h3cRadiusAuthenticating": h3cRadiusAuthenticating,
       "h3cRadiusAuthClient": h3cRadiusAuthClient,
       "h3cRadiusAuthServerTable": h3cRadiusAuthServerTable,
       "h3cRadiusAuthServerEntry": h3cRadiusAuthServerEntry,
       "h3cRadiusAuthFailureTimes": h3cRadiusAuthFailureTimes,
       "h3cRadiusAuthTimeoutTimes": h3cRadiusAuthTimeoutTimes,
       "h3cRadiusAuthRejectTimes": h3cRadiusAuthRejectTimes,
       "h3cRadiusExtend": h3cRadiusExtend,
       "h3cRadiusExtendObjects": h3cRadiusExtendObjects,
       "h3cRadiusExtendTables": h3cRadiusExtendTables,
       "h3cRadiusSchAuthTable": h3cRadiusSchAuthTable,
       "h3cRadiusSchAuthEntry": h3cRadiusSchAuthEntry,
       "h3cRadiusSchAuthGroupName": h3cRadiusSchAuthGroupName,
       "h3cRadiusSchAuthPrimIpAddr": h3cRadiusSchAuthPrimIpAddr,
       "h3cRadiusSchAuthPrimUdpPort": h3cRadiusSchAuthPrimUdpPort,
       "h3cRadiusSchAuthPrimKey": h3cRadiusSchAuthPrimKey,
       "h3cRadiusSchAuthSecIpAddr": h3cRadiusSchAuthSecIpAddr,
       "h3cRadiusSchAuthSecUdpPort": h3cRadiusSchAuthSecUdpPort,
       "h3cRadiusSchAuthSecKey": h3cRadiusSchAuthSecKey,
       "h3cRadiusSchAuthRowStatus": h3cRadiusSchAuthRowStatus,
       "h3cRadiusSchAccTable": h3cRadiusSchAccTable,
       "h3cRadiusSchAccEntry": h3cRadiusSchAccEntry,
       "h3cRadiusSchAccGroupName": h3cRadiusSchAccGroupName,
       "h3cRadiusSchAccPrimIpAddr": h3cRadiusSchAccPrimIpAddr,
       "h3cRadiusSchAccPrimUdpPort": h3cRadiusSchAccPrimUdpPort,
       "h3cRadiusSchAccPrimKey": h3cRadiusSchAccPrimKey,
       "h3cRadiusSchAccSecIpAddr": h3cRadiusSchAccSecIpAddr,
       "h3cRadiusSchAccSecUdpPort": h3cRadiusSchAccSecUdpPort,
       "h3cRadiusSchAccSecKey": h3cRadiusSchAccSecKey,
       "h3cRadiusSchAccRowStatus": h3cRadiusSchAccRowStatus,
       "h3cRadiusExtendTraps": h3cRadiusExtendTraps,
       "h3cRadiusStatistic": h3cRadiusStatistic,
       "h3cRadiusStatAccReq": h3cRadiusStatAccReq,
       "h3cRadiusStatAccAck": h3cRadiusStatAccAck,
       "h3cRadiusStatLogoutReq": h3cRadiusStatLogoutReq,
       "h3cRadiusStatLogoutAck": h3cRadiusStatLogoutAck,
       "h3cRadiusServerTrapVarObjects": h3cRadiusServerTrapVarObjects,
       "h3cRadiusServerFirstTrapTime": h3cRadiusServerFirstTrapTime}
)
